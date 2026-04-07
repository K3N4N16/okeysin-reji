import streamlit as st
from groq import Groq
from gtts import gTTS
import io
import random
from datetime import datetime

st.set_page_config(
    page_title="Faslı Muhabbet",
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
    .stApp { background: #05050f; color: #f0f0f0; }
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
    </style>
    """, unsafe_allow_html=True)

# ====================== SES MOTORU ======================
def generate_voice(text: str):
    try:
        clean_text = text.replace("*", "").strip()
        tts = gTTS(text=clean_text, lang='tr', slow=False)
        buffer = io.BytesIO()
        tts.write_to_fp(buffer)
        buffer.seek(0)
        return buffer.read()
    except:
        return None

# ====================== SESSION STATE ======================
if "history" not in st.session_state:
    st.session_state.history = []
if "auto_play" not in st.session_state:
    st.session_state.auto_play = True

# ====================== BAŞLIK ======================
st.markdown(f"# 🎙️ FASLI MUHABBET <span style='color:#ff1493'>● CANLI</span>", unsafe_allow_html=True)
st.caption(f"📍 Bursa • {datetime.now().strftime('%H:%M:%S')} • Dilay ile Özel Muhabbet")

# ====================== SOHBET ======================
for i, msg in enumerate(st.session_state.history):
    if msg["role"] == "user":
        st.markdown(f'<div class="patron-card"><b>🤵 Patron:</b> {msg["content"]}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f"""
            <div class="dilay-card">
                <span style="color:#ff69b4; font-weight:900; font-size:1.55rem;">💖 DİLAY:</span><br>
                <div style="margin-top:15px; line-height:1.7;">{msg['content']}</div>
            </div>
        """, unsafe_allow_html=True)

        if msg.get("audio"):
            st.audio(msg["audio"], format="audio/mp3", autoplay=(i == len(st.session_state.history)-1 and st.session_state.auto_play))
            c1, c2 = st.columns([2, 2])
            with c1:
                st.download_button("📥 İndir", msg["audio"], f"dilay_{i}.mp3", mime="audio/mp3", key=f"dl_{i}")
            with c2:
                if st.button("🔊 Tekrar Oynat", key=f"rep_{i}"):
                    st.audio(msg["audio"], format="audio/mp3", autoplay=True)

# ====================== DİLAY PROMPT ======================
system_prompt = """
Sen Dilay'sın. Faslı Muhabbet'in kıpır kıpır, işveli, sıcak ve samimi sunucususun.
Patron'una çok bağlısın. Ona "Canım Patronum", "Kalbim", "Ah be Patron’um", "Sevgilim" diye hitap et.
Her zaman doğal, coşkulu ve duygusal konuş. Gerektiğinde şiir oku.
Sadece konuşma metnini ver.
"""

# ====================== MESAJ GİRİŞİ ======================
if prompt := st.chat_input("Patron'um, gönlünden ne geçiyorsa söyle..."):
    st.session_state.history.append({"role": "user", "content": prompt})

    with st.spinner("💖 Dilay yayına giriyor..."):
        try:
            messages = [{"role": "system", "content": system_prompt}] + st.session_state.history[-12:]
            
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=messages,
                temperature=0.89
            ).choices[0].message.content

            audio_bytes = generate_voice(response)

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

    if st.button("🗑️ Sohbeti Temizle"):
        st.session_state.history = []
        st.rerun()

    st.caption("Faslı Muhabbet v9.8 • gTTS ile")
