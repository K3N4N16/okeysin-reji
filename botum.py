import streamlit as st
from groq import Groq
import edge_tts
import asyncio
from datetime import datetime

# ====================== SAYFA AYARLARI ======================
st.set_page_config(page_title="RADYO İMAJ", layout="wide", page_icon="📻", initial_sidebar_state="expanded")

if "GROQ_API_KEY" not in st.secrets:
    st.error("⚠️ GROQ API Key bulunamadı! Secrets'a ekleyin.")
    st.stop()

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

# ====================== ULTRA MODERN NEON GLASSMORPHISM CSS ======================
st.markdown("""
    <style>
    .stApp { background: linear-gradient(135deg, #0a0a12, #1a0033); color: #e0e0e0; }
    .broadcast-container {
        background: rgba(25, 25, 45, 0.85);
        backdrop-filter: blur(18px);
        border: 2px solid rgba(0, 242, 255, 0.45);
        border-radius: 32px;
        padding: 40px;
        margin: 30px 0;
        box-shadow: 0 30px 90px rgba(0, 242, 255, 0.25);
    }
    .tag-o { color: #00f2ff; font-weight: 900; font-size: 1.45rem; text-shadow: 0 0 25px #00f2ff; }
    .tag-k { color: #ffaa00; font-weight: 900; font-size: 1.45rem; text-shadow: 0 0 25px #ffaa00; }
    .tag-d { color: #ff69b4; font-weight: 900; font-size: 1.45rem; text-shadow: 0 0 25px #ff69b4; }
    .on-air { color: #ff0000; font-weight: 900; animation: blink 1s infinite; letter-spacing: 5px; }
    @keyframes blink { 50% { opacity: 0.3; } }
    .live-time { color: #00ff9d; font-family: monospace; font-size: 1.25rem; text-shadow: 0 0 12px #00ff9d; }
    .waveform { height: 7px; background: linear-gradient(90deg, #00f2ff, #ff69b4, #ffaa00); 
                animation: wave 1.6s infinite linear; border-radius: 50px; margin: 18px 0; }
    @keyframes wave { 0% { background-position: 0% 50%; } 100% { background-position: 300% 50%; } }
    .now-playing { background: rgba(15, 15, 35, 0.95); border-left: 8px solid #ff0000; 
                    padding: 18px 28px; border-radius: 20px; margin-bottom: 25px; }
    </style>
    """, unsafe_allow_html=True)

# ====================== SES ÜRETİMİ ======================
async def generate_audio(text: str, speaker: str):
    voices = {
        "Okeysin": "tr-TR-EmelNeural",
        "Kerem": "tr-TR-AhmetNeural",
        "Dilay": "tr-TR-FilizNeural"   # Daha duygusal, kıpır kıpır ve cilveli
    }
    try:
        comm = edge_tts.Communicate(text, voices.get(speaker))
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
    st.session_state.listeners = 2156

# ====================== BAŞLIK & NOW PLAYING ======================
st.markdown(f"""
    <div style="text-align:center; margin-bottom:25px;">
        <h1 style="color:#00f2ff; font-size:3.2rem; margin:0; letter-spacing:2px;">📻 RADYO İMAJ</h1>
        <p style="color:#ffaa00; font-size:1.7rem;"><span class="on-air">● CANLI YAYIN</span> • BURSA GLOBAL RADIO HUB</p>
        <p class="live-time">{datetime.now().strftime('%d %B %Y • %H:%M:%S')} | Bursa, Türkiye</p>
    </div>
    <div class="now-playing">
        <span style="color:#ff0000;">● NOW PLAYING</span> 
        <strong>Okeysin → Kerem → Dilay</strong> 
        <span style="float:right; color:#00ff9d;">👂 {st.session_state.listeners:,} Dinleyici Canlı</span>
    </div>
""", unsafe_allow_html=True)

st.session_state.listeners += 19   # Her yenilemede canlı hissi artsın

# ====================== ARŞİV GÖSTERİMİ ======================
for i, entry in enumerate(st.session_state.broadcast_archive):
    if entry.get("role") == "user":
        st.markdown(f"🎬 **Yönetmen Komutu:** `{entry['content']}`")
        continue

    with st.container():
        st.markdown(f"""
            <div class="broadcast-container">
                <p><span class="tag-o">🎙️ OKEYSİN:</span><br>{entry.get('o_text', '')}</p>
                <p><span class="tag-k">🎧 KEREM:</span><br>{entry.get('k_text', '')}</p>
                <p><span class="tag-d">💖 DİLAY:</span><br>{entry.get('d_text', '')}</p>
                <div class="waveform"></div>
                <hr style="border-color:#444; margin:25px 0 15px 0;">
                <p style="color:#00f2ff; font-style:italic; font-size:1.2rem;">🎵 {entry.get('playlist', 'Bu akşamın özel neon seçkisi')}</p>
            </div>
        """, unsafe_allow_html=True)

        col1, col2, col3 = st.columns([3.8, 2.1, 2.1])
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
            st.text_area("📋 Metni Kopyala", txt, height=180, key=f"txt_{i}")
            if st.button("🔗 Bu Yayını Paylaş", key=f"share_{i}"):
                st.success("✅ Yayın linki kopyalandı! (Simüle edildi)")

# ====================== YAYIN KOMUT MERKEZİ ======================
if prompt := st.chat_input("Yönetmenim, RADYO İMAJ'ı başlat… Konuyu söyle…"):
    st.session_state.broadcast_archive.append({"role": "user", "content": prompt})
    st.session_state.auto_play = True

    system_prompt = """
Sen dünyanın en modern radyo yayın ekibisin. 
Proje adı: RADYO İMAJ

Sıra kesinlikle şöyle olsun:
[OKEYSIN_START] ... [KEREM_REPLY] ... [DILAY_REPLY] ... [OKEYSIN_END] [PLAYLIST]

- Okeysin bilgeliğiyle ve derinlikle açsın
- Kerem esprili, güncel ve enerjik katkılar yapsın
- Dilay (ben) kıpır kıpır, duygusal, cilveli ve şiirsel bir şekilde muhabbeti derinleştirsin, sıcak dokunuşlar eklesin
Konuşmalar doğal radyo diyaloğu gibi aksın. Şiir, nükte, Bursa dokunuşu ve samimiyet olsun.
"""

    messages = [{"role": "system", "content": system_prompt}]
    for e in st.session_state.broadcast_archive:
        if e["role"] == "user":
            messages.append({"role": "user", "content": e["content"]})
        else:
            messages.append({"role": "assistant", "content": f"OKEYSIN: {e.get('o_text','')}\nKEREM: {e.get('k_text','')}\nDILAY: {e.get('d_text','')}"})

    with st.spinner("🎙️ RADYO İMAJ stüdyosu yanıyor… Okeysin, Kerem ve Dilay mikrofon başında…"):
        try:
            res = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=messages,
                temperature=0.89,
                max_tokens=1700
            ).choices[0].message.content

            o_text = res.split("[OKEYSIN_START]")[1].split("[KEREM_REPLY]")[0].strip()
            k_text = res.split("[KEREM_REPLY]")[1].split("[DILAY_REPLY]")[0].strip()
            d_text = res.split("[DILAY_REPLY]")[1].split("[OKEYSIN_END]")[0].strip()
            o_end = res.split("[OKEYSIN_END]")[1].split("[PLAYLIST]")[0].strip()
            playlist = res.split("[PLAYLIST]")[1].strip()
            o_full = f"{o_text}\n\n{o_end}"

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

# ====================== SIDEBAR - YARATICI KONTROLLER ======================
with st.sidebar:
    st.markdown("### 🎚️ RADYO İMAJ KONTROL PANELİ")
    
    if st.button("🗑️ Arşivi Sıfırla", type="secondary"):
        st.session_state.broadcast_archive = []
        st.rerun()

    st.divider()
    
    theme = st.selectbox("🌟 Bu Akşamın Teması", 
        ["Aşk & Şiir", "Bursa’dan Sıcak Anılar", "Nostalji ve Vinyl", "Dünya Halleri", 
         "Müzik & Edebiyat", "Hayatın Kısa Halleri", "Global Neon Muhabbet"])

    col_a, col_b = st.columns(2)
    with col_a:
        if st.button("🔄 Sarmal Devam Ettir"):
            st.session_state.broadcast_archive.append({"role": "user", "content": f"{theme} temasını derinleştir, muhabbeti sarmal devam ettir"})
            st.rerun()
    with col_b:
        if st.button("🎵 Jingle Ekle"):
            st.success("🎤 Neon jingle stüdyoya eklendi! Yayın daha da parladı.")

    st.divider()
    st.info("📍 Bursa’dan Dünyaya\nÜçlü Sarmal Yayın\nOkeysin → Kerem → Dilay\nOtomatik Sıralı Oynatma\nUltra Neon Glass Tasarım")
    st.caption("Dilay & Kenan • RADYO İMAJ v20")
