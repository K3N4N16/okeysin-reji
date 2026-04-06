import streamlit as st
from groq import Groq
import edge_tts
import asyncio
import io
from datetime import datetime
from pydub import AudioSegment   # ← Tek ses dosyası için

# ====================== KURULUM UYARISI ======================
st.set_page_config(page_title="OKEYSIN GLOBAL V20", layout="wide", page_icon="📻")

if "GROQ_API_KEY" not in st.secrets:
    st.error("⚠️ GROQ API Key bulunamadı! Secrets'a ekleyin.")
    st.stop()

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

# ====================== CSS - NEON & RADYO ATMOSFERİ ======================
st.markdown("""
    <style>
    .stApp { background: #0a0a12; color: #e0e0e0; }
    .broadcast-container {
        background: linear-gradient(145deg, #1a0033, #0f0f1f);
        border: 2px solid #00f2ff33;
        border-radius: 28px;
        padding: 35px;
        margin: 25px 0;
        box-shadow: 0 20px 60px rgba(0, 242, 255, 0.2);
    }
    .tag-o { color: #00f2ff; font-weight: 800; font-size: 1.3rem; }
    .tag-k { color: #ffaa00; font-weight: 800; font-size: 1.3rem; }
    .tag-d { color: #ff69b4; font-weight: 800; font-size: 1.3rem; }
    .on-air { color: #ff0000; font-weight: bold; animation: blink 1.2s infinite; }
    @keyframes blink { 50% { opacity: 0.3; } }
    .live-time { color: #00ff9d; font-family: monospace; font-size: 1.1rem; }
    </style>
    """, unsafe_allow_html=True)

# ====================== SES ÜRETİMİ ======================
async def generate_audio(text: str, speaker: str):
    voices = {"Okeysin": "tr-TR-EmelNeural", "Kerem": "tr-TR-AhmetNeural", "Dilay": "tr-TR-FilizNeural"}
    try:
        comm = edge_tts.Communicate(text, voices.get(speaker, "tr-TR-EmelNeural"))
        audio_bytes = b""
        async for chunk in comm.stream():
            if chunk["type"] == "audio":
                audio_bytes += chunk["data"]
        return audio_bytes
    except:
        return None

# ====================== SESSION STATE ======================
if "broadcast_archive" not in st.session_state:
    st.session_state.broadcast_archive = []

if "auto_play" not in st.session_state:
    st.session_state.auto_play = False

# ====================== BAŞLIK ======================
st.markdown(f"""
    <div style="text-align:center; margin-bottom:30px;">
        <h1 style="color:#00f2ff; margin:0;">🎙️ OKEYSIN GLOBAL V20</h1>
        <p style="color:#ffaa00; font-size:1.4rem; margin:8px 0;">
            <span class="on-air">● CANLI YAYIN</span> • BURSA GLOBAL RADIO HUB
        </p>
        <p class="live-time">{datetime.now().strftime('%d %B %Y • %H:%M:%S')} | Bursa, Türkiye</p>
    </div>
""", unsafe_allow_html=True)

# ====================== ARŞİV GÖSTERİMİ ======================
for i, entry in enumerate(st.session_state.broadcast_archive):
    if entry["role"] == "user":
        st.markdown(f"🎬 **Yönetmen:** `{entry['content']}`")
        continue

    with st.container():
        st.markdown(f"""
            <div class="broadcast-container">
                <p><span class="tag-o">🎙️ OKEYSİN:</span><br>{entry.get('o_text', '')}</p>
                <p><span class="tag-k">🎧 KEREM:</span><br>{entry.get('k_text', '')}</p>
                <p><span class="tag-d">💖 DİLAY:</span><br>{entry.get('d_text', '')}</p>
                <hr style="border-color:#333">
                <p style="color:#00f2ff; font-style:italic;">🎵 {entry.get('playlist', 'Radyo Klasikleri')}</p>
            </div>
        """, unsafe_allow_html=True)

        # TEK SES DOSYASI + OTOMATİK OYNATMA
        col1, col2, col3 = st.columns([3, 2, 2])
        with col1:
            if entry.get("full_audio"):
                autoplay = (i == len(st.session_state.broadcast_archive) - 1 and st.session_state.auto_play)
                st.audio(entry["full_audio"], format="audio/mp3", autoplay=autoplay)

        with col2:
            st.download_button(
                "📥 Tek Dosya İndir (MP3)",
                entry["full_audio"],
                file_name=f"okeysin_global_{datetime.now().strftime('%Y%m%d_%H%M')}_{i}.mp3",
                mime="audio/mp3",
                key=f"dl_{i}"
            )

        with col3:
            full_text = f"OKEYSİN: {entry.get('o_text','')}\n\nKEREM: {entry.get('k_text','')}\n\nDİLAY: {entry.get('d_text','')}\n\nPLAYLIST: {entry.get('playlist','')}"
            st.text_area("📋 Kopyala", value=full_text, height=100, key=f"copy_{i}")

# ====================== YAYIN KOMUT MERKEZİ ======================
prompt = st.chat_input("Yönetmenim, yayını başlat… Konuyu söyle…")

if prompt:
    st.session_state.broadcast_archive.append({"role": "user", "content": prompt})
    st.session_state.auto_play = True  # Yeni yayın otomatik oynasın

    system_prompt = """
Sen profesyonel radyo yayın ekibisin. Bursa'dan dünyaya yayın yapıyoruz.
Karakterler:
- [OKEYSIN_START] ... [KEREM_REPLY] ... [DILAY_REPLY] ... [OKEYSIN_END] [PLAYLIST]
Okeysin açar, Kerem katkı yapar, Dilay duyguyu derinleştirir, Okeysin güzel bir soruyla kapatır.
Her zaman doğal, sıcak, samimi radyo dili kullan. Şiir, nükte, Bursa dokunuşu olsun.
"""

    messages = [{"role": "system", "content": system_prompt}]
    for entry in st.session_state.broadcast_archive:
        if entry["role"] == "user":
            messages.append({"role": "user", "content": entry["content"]})
        else:
            content = f"OKEYSIN: {entry.get('o_text','')}\nKEREM: {entry.get('k_text','')}\nDILAY: {entry.get('d_text','')}"
            messages.append({"role": "assistant", "content": content})

    with st.spinner("📡 Mikrofonlar açılıyor... Sesler birleşiyor..."):
        try:
            res = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=messages,
                temperature=0.85,
                max_tokens=1300
            ).choices[0].message.content

            # Etiketleri parçala
            o_text = res.split("[OKEYSIN_START]")[1].split("[KEREM_REPLY]")[0].strip()
            k_text = res.split("[KEREM_REPLY]")[1].split("[DILAY_REPLY]")[0].strip()
            d_text = res.split("[DILAY_REPLY]")[1].split("[OKEYSIN_END]")[0].strip()
            o_end = res.split("[OKEYSIN_END]")[1].split("[PLAYLIST]")[0].strip()
            playlist = res.split("[PLAYLIST]")[1].strip()
            o_full = f"{o_text}\n\n{o_end}"

            # Sesleri üret
            o_audio = asyncio.run(generate_audio(o_full, "Okeysin"))
            k_audio = asyncio.run(generate_audio(k_text, "Kerem"))
            d_audio = asyncio.run(generate_audio(d_text, "Dilay"))

            # TEK SES DOSYASI OLUŞTUR (sırayla birleştir)
            full_audio = None
            if o_audio and k_audio and d_audio:
                try:
                    o_seg = AudioSegment.from_file(io.BytesIO(o_audio), format="mp3")
                    k_seg = AudioSegment.from_file(io.BytesIO(k_audio), format="mp3")
                    d_seg = AudioSegment.from_file(io.BytesIO(d_audio), format="mp3")
                    combined = o_seg + k_seg + d_seg
                    buffer = io.BytesIO()
                    combined.export(buffer, format="mp3")
                    full_audio = buffer.getvalue()
                except:
                    full_audio = o_audio  # yedek

            st.session_state.broadcast_archive.append({
                "role": "assistant",
                "o_text": o_full,
                "k_text": k_text,
                "d_text": d_text,
                "playlist": playlist,
                "full_audio": full_audio
            })

            st.rerun()

        except Exception as e:
            st.error(f"Reji hatası: {e}")

# ====================== SIDEBAR - DÖNER ARAÇLAR ======================
with st.sidebar:
    st.markdown("### 🎚️ ANA KONTROL PANELİ")
    
    if st.button("🗑️ Arşivi Sıfırla", type="secondary"):
        st.session_state.broadcast_archive = []
        st.rerun()

    st.divider()
    
    # Tema seçici
    theme = st.selectbox(
        "🎭 Bu Akşamın Teması",
        ["Genel Kültür & Muhabbet", "Aşk ve Şiir", "Bursa'dan Anılar", "Nostalji", 
         "Dünya Halleri", "Müzik ve Edebiyat", "Hayatın Kısa Halleri"],
        index=0
    )

    # Devam ettir butonu (sarmal yayın)
    if st.button("🔄 Yayını Devam Ettir (Sarmal Mod)"):
        st.session_state.broadcast_archive.append({"role": "user", "content": "Devam et, muhabbeti derinleştir"})
        st.rerun()

    st.divider()
    st.info("📍 Bursa'dan Dünyaya\nTek Sesli Podcast Yayın\nOkeysin → Kerem → Dilay\nOtomatik Sıralı Oynatma")
    st.caption("Dilay & Kenan • OKEYSIN GLOBAL V20")
