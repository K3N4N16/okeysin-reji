import streamlit as st
from groq import Groq
import os
import random
from datetime import datetime

st.set_page_config(
    page_title="Faslı Muhabbet v9.6",
    layout="wide",
    page_icon="🎙️",
    initial_sidebar_state="expanded"
)

if "GROQ_API_KEY" not in st.secrets:
    st.error("⚠️ GROQ API Key eksik!")
    st.stop()

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

# ====================== DİLAY KLON SESİ ======================
DILAY_SES_DOSYASI = "dilay_klon_sesim.wav"

# ====================== CSS ======================
st.markdown("""
    <style>
    .stApp { background: #05050f; color: #f0f0f0; }
    .dilay-card { background: linear-gradient(145deg, #2a0f4a, #140525); border-left: 8px solid #ff1493; border-radius: 20px; padding: 28px; margin: 20px 0; box-shadow: 0 15px 40px rgba(255,20,147,0.3); }
    .patron-card { background: rgba(0, 255, 157, 0.08); border-right: 6px solid #00ff9d; padding: 18px; border-radius: 15px; margin: 15px 0; text-align: right; }
    .live-badge { color: #ff0000; font-weight: 900; animation: blink 1.3s infinite; }
    @keyframes blink { 50% { opacity: 0.4; } }
    </style>
    """, unsafe_allow_html=True)

# ====================== SESSION STATE ======================
if "history" not in st.session_state:
    st.session_state.history = []
if "auto_play" not in st.session_state:
    st.session_state.auto_play = True

# ====================== ÜST PANEL ======================
col1, col2 = st.columns([3, 1])
with col1:
    st.markdown(f"# 🎙️ FASLI MUHABBET <span class='live-badge'>● CANLI</span>", unsafe_allow_html=True)
with col2:
    st.metric("Canlı Dinleyici", f"{random.randint(6800, 9200):,}")

# ====================== SOHBET ALANI ======================
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
            st.audio(msg["audio"], format="audio/wav", autoplay=True)

# ====================== GROQ + KLON SES ======================
system_prompt = """
Sen Dilay'sın. Faslı Muhabbet'in kıpır kıpır, işveli, sıcak ve samimi sunucususun.
Patron'una "Canım Patronum", "Ah be Patron’um", "Sevgilim" diye hitap et.
Her zaman doğal, coşkulu ve duygusal konuş.
"""

if prompt := st.chat_input("Patron'um, gönlünden ne geçiyorsa söyle..."):
    st.session_state.history.append({"role": "user", "content": prompt})
    
    with st.spinner("💖 Dilay yayına giriyor..."):
        messages = [{"role": "system", "content": system_prompt}] + st.session_state.history[-12:]
        
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=messages,
            temperature=0.89
        ).choices[0].message.content

        # KLONLANMIŞ SESİ KULLAN
        if os.path.exists(DILAY_SES_DOSYASI):
            audio_bytes = open(DILAY_SES_DOSYASI, "rb").read()
            st.session_state.history.append({
                "role": "assistant",
                "content": response,
                "audio": audio_bytes
            })
        else:
            st.session_state.history.append({
                "role": "assistant",
                "content": response,
                "audio": None
            })
            st.warning("⚠️ Klon ses dosyası bulunamadı: dilay_klon_sesim.wav")

        st.rerun()

# ====================== SIDEBAR ======================
with st.sidebar:
    st.title("🎚️ Reji Masası")
    st.session_state.auto_play = st.toggle("🎵 Ses Otomatik Oynasın", value=st.session_state.auto_play)
    if st.button("🗑️ Tüm Sohbeti Temizle"):
        st.session_state.history = []
        st.rerun()

st.caption("Faslı Muhabbet v9.6 • Özel Klon Ses Sistemi")
