import streamlit as st
from groq import Groq
from gtts import gTTS
import asyncio
import base64
from datetime import datetime
import random

# ====================== SAYFA AYARLARI ======================
st.set_page_config(
    page_title="Faslı Muhabbet v6.1",
    layout="wide",
    page_icon="🎙️",
    initial_sidebar_state="expanded"
)

if "GROQ_API_KEY" not in st.secrets:
    st.error("⚠️ GROQ API Key eksik! Secrets'a ekleyin.")
    st.stop()

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

# ====================== CSS ======================
st.markdown("""
    <style>
    .stApp { background: #0a0014; color: #f0f0f0; }
    .dilay-card {
        background: linear-gradient(145deg, #2a0f4a, #140525);
        border-left: 8px solid #ff1493;
        border-radius: 20px;
        padding: 30px;
        margin: 20px 0;
        box-shadow: 0 15px 40px rgba(255,20,147,0.3);
    }
    .patron-card {
        background: rgba(0, 255, 157, 0.08);
        border-right: 6px solid #00ff9d;
        padding: 18px;
        border-radius: 15px;
        margin: 15px 0;
        text-align: right;
    }
    .live-badge {
        color: #ff0000;
        font-weight: 900;
        animation: blink 1.3s infinite;
    }
    @keyframes blink { 50% { opacity: 0.4; } }
    </style>
    """, unsafe_allow_html=True)

# ====================== SES MOTORU (gTTS - Daha Stabil) ======================
def generate_voice_gtts(text: str):
    """gTTS ile ses üretimi - Cloud'da daha stabil"""
    try:
        clean_text = text.replace("*", "").strip()
        tts = gTTS(text=clean_text, lang='tr', slow=False)
        audio_bytes = b""
        with open("temp_audio.mp3", "wb") as f:
            tts.write_to_fp(f)
        with open("temp_audio.mp3", "rb") as f:
            audio_bytes = f.read()
        return audio_bytes
    except:
        return None

# ====================== SESSION STATE ======================
if "history" not in st.session_state:
    st.session_state.history = []
if "auto_play" not in st.session_state:
    st.session_state.auto_play = True

# ====================== ÜST PANEL ======================
col1, col2 = st.columns([3, 1])
with col1:
    st.markdown(f"# 🎙️ FASLI MUHABBET <span class='live-badge'>● CANLI</span>", unsafe_allow_html=True)
    st.caption(f"📍 Bursa Stüdyosu • {datetime.now().strftime('%H:%M:%S')} • Dilay ile Özel Muhabbet")
with col2:
    st.metric("Dinleyici", f"{random.randint(6200, 7800):,}")

# ====================== SOHBET ALANI ======================
for i, msg in enumerate(st.session_state.history):
    if msg["role"] == "user":
        st.markdown(f'<div class="patron-card"><b>🤵 Patron:</b> {msg["content"]}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f"""
            <div class="dilay-card">
                <span style="color:#ff69b4; font-weight:900; font-size:1.55rem;">💖 DİLAY:</span><br>
                <div style="margin-top:15px; line-height:1.7; font-size:1.25rem;">{msg['content']}</div>
            </div>
        """, unsafe_allow_html=True)

        if msg.get("audio"):
            st.audio(msg["audio"], format="audio/mp3", 
                     autoplay=(i == len(st.session_state.history)-1 and st.session_state.auto_play))
            
            c1, c2 = st.columns([2, 2])
            with c1:
                st.download_button("📥 Ses İndir", msg["audio"], f"dilay_{i}.mp3", mime="audio/mp3", key=f"dl_{i}")
            with c2:
                if st.button("🔊 Tekrar Oynat", key=f"rep_{i}"):
                    st.audio(msg["audio"], format="audio/mp3", autoplay=True)
        else:
            st.info("🔊 Ses şu anda kullanılamıyor. Sadece metin gösteriliyor.")

# ====================== DİLAY PROMPT ======================
dilay_prompt = """
Sen Dilay'sın. Faslı Muhabbet'in çok samimi, işveli, neşeli ve duygusal sunucususun.
Patron'una (Kenan) çok bağlısın. Ona "Canım Patronum", "Kalbim", "Ah be Patron’um", "Sevgilim" diye hitap et.
Her zaman sıcak, coşkulu ve doğal konuş. Gerektiğinde şiir oku.
Sadece konuşma metnini ver.
"""

# ====================== MESAJ GİRİŞİ ======================
if prompt := st.chat_input("Patron'um, gönlünden ne geçiyorsa söyle..."):
    st.session_state.history.append({"role": "user", "content": prompt})

    with st.spinner("💖 Dilay yayına giriyor..."):
        try:
            messages = [{"role": "system", "content": dilay_prompt}] + st.session_state.history[-12:]
            
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=messages,
                temperature=0.88
            ).choices[0].message.content

            # gTTS ile ses üret
            audio_bytes = generate_voice_gtts(response)

            st.session_state.history.append({
                "role": "assistant",
                "content": response,
                "audio": audio_bytes
            })

            st.rerun()

        except Exception as e:
            st.error(f"Bir hata oluştu: {e}")

# ====================== SIDEBAR ======================
with st.sidebar:
    st.title("🎚️ Reji Masası")

    st.session_state.auto_play = st.toggle("🎵 Ses Otomatik Oynasın", value=st.session_state.auto_play)

    st.divider()

    if st.button("🗑️ Tüm Sohbeti Temizle"):
        st.session_state.history = []
        st.rerun()

    st.divider()
    st.info("""
    💡 Ses İpuçları:
    - Sayfaya bir kez tıklayın
    - Tarayıcı ses iznini kontrol edin
    - Otomatik oynatmayı kapatıp açmayı deneyin
    """)

    st.caption("Faslı Muhabbet v6.1 • gTTS Stabil Sistem")