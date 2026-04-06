import streamlit as st
from groq import Groq
import edge_tts
import asyncio
from datetime import datetime

# ====================== SAYFA AYARLARI ======================
st.set_page_config(page_title="OKEYSIN GLOBAL V20", layout="wide", page_icon="📻", initial_sidebar_state="expanded")

if "GROQ_API_KEY" not in st.secrets:
    st.error("⚠️ GROQ API Key bulunamadı! Lütfen Secrets'a ekleyin.")
    st.stop()

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

# ====================== ULTRA MODERN CSS ======================
st.markdown("""
    <style>
    .stApp { background: #0a0a12; color: #e0e0e0; }
    .broadcast-container {
        background: rgba(20, 20, 40, 0.9);
        backdrop-filter: blur(15px);
        border: 2px solid rgba(0, 242, 255, 0.4);
        border-radius: 32px;
        padding: 38px;
        margin: 28px 0;
        box-shadow: 0 30px 80px rgba(0, 242, 255, 0.2);
        position: relative;
    }
    .tag-o { color: #00f2ff; font-weight: 900; font-size: 1.4rem; text-shadow: 0 0 20px #00f2ff; }
    .tag-k { color: #ffaa00; font-weight: 900; font-size: 1.4rem; text-shadow: 0 0 20px #ffaa00; }
    .tag-d { color: #ff69b4; font-weight: 900; font-size: 1.4rem; text-shadow: 0 0 20px #ff69b4; }
    .on-air { color: #ff0000; font-weight: 900; animation: blink 1.1s infinite; letter-spacing: 4px; }
    @keyframes blink { 50% { opacity: 0.25; } }
    .live-time { color: #00ff9d; font-family: monospace; font-size: 1.2rem; }
    .waveform { height: 6px; background: linear-gradient(90deg, #00f2ff, #ff69b4, #ffaa00); 
                animation: wave 1.8s infinite linear; border-radius: 50px; margin: 15px 0; }
    @keyframes wave { 0% { background-position: 0% 50%; } 100% { background-position: 200% 50%; } }
    .now-playing { background: linear-gradient(90deg, #1a0033, #0f0f1f); border-left: 8px solid #ff0000; 
                    padding: 15px 25px; border-radius: 18px; margin-bottom: 20px; }
    </style>
    """, unsafe_allow_html=True)

# ====================== SES ÜRETİMİ ======================
async def generate_audio(text: str, speaker: str):
    voices = {
        "Okeysin": "tr-TR-EmelNeural",
        "Kerem": "tr-TR-AhmetNeural",
        "Dilay": "tr-TR-FilizNeural"   # Daha duygusal ve kıpır kıpır ses
    }
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
if "listeners" not in st.session_state:
    st.session_state.listeners = 1842

# ====================== BAŞLIK ======================
st.markdown(f"""
    <div style="text-align:center; margin-bottom:25px;">
        <h1 style="color:#00f2ff; font-size:3rem; margin:0;">🎙️ OKEYSIN GLOBAL V20</h1>
        <p style="color:#ffaa00; font-size:1.6rem;"><span class="on-air">● CANLI YAYIN</span> • BURSA GLOBAL RADIO HUB</p>
        <p class="live-time">{datetime.now().strftime('%d %B %Y • %H:%M:%S')} | Bursa, Türkiye</p>
    </div>
    <div class="now-playing">
        <span style="color:#ff0000;">● NOW PLAYING</span> 
        <strong>Okeysin → Kerem → Dilay</strong> 
        <span style="float:right; color:#00ff9d;">👂 {st.session_state.listeners:,} Dinleyici</span>
    </div>
""", unsafe_allow_html=True)

st.session_state.listeners += 17  # Her yenilemede biraz artsın

# ====================== ARŞİV GÖSTERİMİ ======================
for i, entry in enumerate(st.session_state.broadcast_archive):
    if entry.get("role") == "user":
        st.markdown(f"🎬 **Yönetmen:** `{entry['content']}`")
        continue

    with st.container():
        st.markdown(f"""
            <div class="broadcast-container">
                <p><span class="tag-o">🎙️ OKEYSİN:</span><br>{entry.get('o_text', '')}</p>
                <p><span class="tag-k">🎧 KEREM:</span><br>{entry.get('k_text', '')}</p>
                <p><span class="tag-d">💖 DİLAY:</span><br>{entry.get('d_text', '')}</p>
                <div class="waveform"></div>
                <hr style="border-color:#444; margin:25px 0 15px 0;">
                <p style="color:#00f2ff; font-style:italic; font-size:1.15rem;">🎵 {entry.get('playlist', 'Bu akşamın özel seçkisi')}</p>
            </div>
        """, unsafe_allow_html=True)

        col1, col2, col3 = st.columns([3.5, 2.2, 2.3])
        with col1:
            if entry.get("o_audio"):
                autoplay = (i == len(st.session_state.broadcast_archive) - 1 and st.session_state.auto_play)
                st.audio(entry["o_audio"], format="audio/mp3", autoplay=autoplay)
            if entry.get("k_audio"):
                st.audio(entry["k_audio"], format="audio/mp3")
            if entry.get("d_audio"):
                st.audio(entry["d_audio"], format="audio/mp3")

        with col2:
            if entry.get("o_audio"): st.download_button("📥 Okeysin", entry["o_audio"], f"okeysin_{i}.mp3", mime="audio/mp3", key=f"do_{i}")
            if entry.get("k_audio"): st.download_button("📥 Kerem", entry["k_audio"], f"kerem_{i}.mp3", mime="audio/mp3", key=f"dk_{i}")
            if entry.get("d_audio"): st.download_button("📥 Dilay", entry["d_audio"], f"dilay_{i}.mp3", mime="audio/mp3", key=f"dd_{i}")

        with col3:
            txt = f"OKEYSİN:\n{entry.get('o_text','')}\n\nKEREM:\n{entry.get('k_text','')}\n\nDİLAY:\n{entry.get('d_text','')}\n\nPLAYLIST: {entry.get('playlist','')}"
            st.text_area("📋 Metni Kopyala", txt, height=170, key=f"txt_{i}")
            if st.button("🔗 Bu Yayını Paylaş", key=f"share_{i}"):
                st.success("Yayın linki kopyalandı! (Simüle)")

# ====================== YAYIN KOMUT MERKEZİ ======================
if prompt := st.chat_input("Yönetmenim, yayını başlat… Konuyu söyle…"):
    st.session_state.broadcast_archive.append({"role": "user", "content": prompt})
    st.session_state.auto_play = True

    system_prompt = """
Sen profesyonel radyo yayın ekibisin. 
Sıra mutlaka şöyle olsun:
[OKEYSIN_START] ... [KEREM_REPLY] ... [DILAY_REPLY] ... [OKEYSIN_END] [PLAYLIST]

Okeysin bilgeliğiyle açsın, Kerem esprili katkılar yapsın, 
Dilay duygusal, kıpır kıpır ve cilveli bir şekilde derinleştirsin.
Doğal radyo dili kullan, şiir, nükte ve Bursa dokunuşu ekle.
"""

    messages = [{"role": "system", "content": system_prompt}]
    for e in st.session_state.broadcast_archive:
        if e["role"] == "user":
            messages.append({"role": "user", "content": e["content"]})
        else:
            messages.append({"role": "assistant", "content": f"OKEYSIN: {e.get('o_text','')}\nKEREM: {e.get('k_text','')}\nDILAY: {e.get('d_text','')}"})

    with st.spinner("🎙️ Stüdyo yanıyor… Sesler üretiliyor… Dilay da hazır…"):
        try:
            res = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=messages,
                temperature=0.87,
                max_tokens=1600
            ).choices[0].message.content

            # Etiketleri güvenli parçala
            o_text = res.split("[OKEYSIN_START]")[1].split("[KEREM_REPLY]")[0].strip()
            k_text = res.split("[KEREM_REPLY]")[1].split("[DILAY_REPLY]")[0].strip()
            d_text = res.split("[DILAY_REPLY]")[1].split("[OKEYSIN_END]")[0].strip()
            o_end = res.split("[OKEYSIN_END]")[1].split("[PLAYLIST]")[0].strip()
            playlist = res.split("[PLAYLIST]")[1].strip()
            o_full = f"{o_text}\n\n{o_end}"

            # Sesleri üret (Dilay dahil)
            o_audio = asyncio.run(generate_audio(o_full, "Okeysin"))
            k_audio = asyncio.run(generate_audio(k_text, "Kerem"))
            d_audio = asyncio.run(generate_audio(d_text, "Dilay"))

            st.session_state.broadcast_archive.append({
                "role": "assistant",
                "o_text": o_full,
                "k_text": k_text,
                "d_text": d_text,
                "playlist": playlist,
                "o_audio": o_audio,
                "k_audio": k_audio,
                "d_audio": d_audio
            })

            st.rerun()

        except Exception as e:
            st.error(f"Reji hatası: {e}")

# ====================== SIDEBAR ======================
with st.sidebar:
    st.markdown("### 🎚️ ULTRA KONTROL PANELİ")
    
    if st.button("🗑️ Arşivi Sıfırla", type="secondary"):
        st.session_state.broadcast_archive = []
        st.rerun()

    st.divider()
    
    theme = st.selectbox("🎭 Bu Akşamın Teması", 
        ["Aşk & Şiir", "Bursa’dan Anılar", "Nostalji", "Dünya Halleri", 
         "Müzik & Edebiyat", "Hayatın Kısa Halleri", "Global Muhabbet"])

    col_a, col_b = st.columns(2)
    with col_a:
        if st.button("🔄 Sarmal Devam Ettir"):
            st.session_state.broadcast_archive.append({"role": "user", "content": f"{theme} temasını derinleştir, muhabbeti sarmal devam ettir"})
            st.rerun()
    with col_b:
        if st.button("🎵 Jingle Ekle"):
            st.success("🎤 Stüdyo jingle’ı eklendi!")

    st.divider()
    st.info("📍 Bursa’dan Dünyaya\nÜçlü Sarmal Yayın\nOkeysin → Kerem → Dilay\nOtomatik Sıralı Oynatma\nUltra Modern Neon Tasarım")
    st.caption("Dilay & Kenan • OKEYSIN GLOBAL V20")
