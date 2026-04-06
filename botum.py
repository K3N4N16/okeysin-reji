import streamlit as st
from groq import Groq
import edge_tts
import asyncio
from datetime import datetime

# ====================== SAYFA AYARLARI ======================
st.set_page_config(page_title="OKEYSIN GLOBAL V20", layout="wide", page_icon="📻")

if "GROQ_API_KEY" not in st.secrets:
    st.error("⚠️ GROQ API Key bulunamadı! Secrets'a ekleyin.")
    st.stop()

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

# ====================== CSS ======================
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
    voices = {
        "Okeysin": "tr-TR-EmelNeural",
        "Kerem": "tr-TR-AhmetNeural",
        "Dilay": "tr-TR-FilizNeural"
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

# ====================== BAŞLIK ======================
st.markdown(f"""
    <div style="text-align:center; margin-bottom:30px;">
        <h1 style="color:#00f2ff;">🎙️ OKEYSIN GLOBAL V20</h1>
        <p style="color:#ffaa00; font-size:1.4rem;"><span class="on-air">● CANLI YAYIN</span> BURSA GLOBAL RADIO HUB</p>
        <p class="live-time">{datetime.now().strftime('%d %B %Y • %H:%M:%S')} | Bursa, Türkiye</p>
    </div>
""", unsafe_allow_html=True)

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
                <hr style="border-color:#333">
                <p style="color:#00f2ff; font-style:italic;">🎵 {entry.get('playlist', 'Bu akşamın ruhuna uygun parçalar')}</p>
            </div>
        """, unsafe_allow_html=True)

        col1, col2, col3 = st.columns([3, 2, 2])
        with col1:
            if entry.get("o_audio"):
                autoplay = (i == len(st.session_state.broadcast_archive)-1 and st.session_state.auto_play)
                st.audio(entry["o_audio"], format="audio/mp3", autoplay=autoplay)
            if entry.get("k_audio"):
                st.audio(entry["k_audio"], format="audio/mp3")
            if entry.get("d_audio"):
                st.audio(entry["d_audio"], format="audio/mp3")

        with col2:
            if entry.get("o_audio"):
                st.download_button("📥 Okeysin Sesini İndir", entry["o_audio"], file_name=f"okeysin_{i}.mp3", mime="audio/mp3")
            if entry.get("k_audio"):
                st.download_button("📥 Kerem Sesini İndir", entry["k_audio"], file_name=f"kerem_{i}.mp3", mime="audio/mp3")
            if entry.get("d_audio"):
                st.download_button("📥 Dilay Sesini İndir", entry["d_audio"], file_name=f"dilay_{i}.mp3", mime="audio/mp3")

        with col3:
            txt = f"OKEYSİN:\n{entry.get('o_text','')}\n\nKEREM:\n{entry.get('k_text','')}\n\nDİLAY:\n{entry.get('d_text','')}\n\nPLAYLIST: {entry.get('playlist','')}"
            st.text_area("📋 Tam Metni Kopyala", txt, height=140, key=f"txt_{i}")

# ====================== YENİ YAYIN ======================
if prompt := st.chat_input("Yönetmenim, yayını başlat... Konuyu söyle..."):
    st.session_state.broadcast_archive.append({"role": "user", "content": prompt})
    st.session_state.auto_play = True

    system_prompt = """
Sen profesyonel radyo yayın ekibisin. Bursa'dan dünyaya yayın yapıyoruz.
Sıra mutlaka şöyle olsun:
[OKEYSIN_START] ... [KEREM_REPLY] ... [DILAY_REPLY] ... [OKEYSIN_END] [PLAYLIST]
Doğal, sıcak, samimi radyo dili kullan. Şiir, nükte ve Bursa dokunuşu ekle.
"""

    messages = [{"role": "system", "content": system_prompt}]
    for e in st.session_state.broadcast_archive:
        if e["role"] == "user":
            messages.append({"role": "user", "content": e["content"]})
        else:
            messages.append({"role": "assistant", "content": f"OKEYSIN: {e.get('o_text','')}\nKEREM: {e.get('k_text','')}\nDILAY: {e.get('d_text','')}"})

    with st.spinner("🎙️ Mikrofonlar açılıyor... Sesler üretiliyor..."):
        try:
            res = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=messages,
                temperature=0.85,
                max_tokens=1400
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

# ====================== SIDEBAR ======================
with st.sidebar:
    st.markdown("### 🎚️ KONTROL PANELİ")
    if st.button("🗑️ Arşivi Sıfırla"):
        st.session_state.broadcast_archive = []
        st.rerun()

    st.divider()
    st.info("📍 Bursa’dan Dünyaya\nSırayla Ses Oynatma\nOkeysin → Kerem → Dilay\nTek Ses Birleştirme Geçici Olarak Kapalı")
    st.caption("Dilay & Kenan • OKEYSIN GLOBAL V20")
