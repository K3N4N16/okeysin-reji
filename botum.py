import streamlit as st
from groq import Groq
import edge_tts
import asyncio
from datetime import datetime
import base64
import random

# ====================== SAYFA AYARLARI ======================
st.set_page_config(
    page_title="Faslı Muhabbet v5.1",
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
    .stApp { background: #05050a; color: #f0f0f0; }
    .dilay-card {
        background: linear-gradient(145deg, #1a0a2e, #0d0514);
        border-left: 8px solid #ff1493;
        border-radius: 18px;
        padding: 28px;
        margin: 20px 0;
        box-shadow: 0 10px 35px rgba(255, 20, 147, 0.25);
    }
    .patron-card {
        background: rgba(0, 255, 157, 0.06);
        border-right: 6px solid #00ff9d;
        padding: 18px;
        border-radius: 12px;
        margin: 12px 0;
        text-align: right;
    }
    .on-air { color: #ff0000; font-weight: 900; animation: pulse 1.5s infinite; }
    @keyframes pulse { 0% {opacity:1;} 50% {opacity:0.4;} 100% {opacity:1;} }
    .status-ok { color: #00ff9d; }
    .status-fail { color: #ff5555; }
    </style>
    """, unsafe_allow_html=True)

# ====================== SES MOTORU (GÜÇLENDİRİLMİŞ) ======================
async def generate_voice(text: str):
    if not text or len(text.strip()) < 15:
        return None
    try:
        clean_text = text.replace("*", "").replace("Dilay:", "").strip()
        comm = edge_tts.Communicate(clean_text, "tr-TR-FilizNeural", rate="0%")
        audio_data = b""
        async for chunk in comm.stream():
            if chunk["type"] == "audio":
                audio_data += chunk["data"]
        return audio_data if len(audio_data) > 7000 else None
    except Exception:
        return None

# ====================== SESSION STATE ======================
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "auto_play" not in st.session_state:
    st.session_state.auto_play = True
if "listeners" not in st.session_state:
    st.session_state.listeners = 5840

# ====================== ÜST PANEL ======================
col1, col2 = st.columns([3, 1])
with col1:
    st.markdown(f"# 🎙️ FASLI MUHABBET <span class='on-air'>● LIVE</span>", unsafe_allow_html=True)
    st.caption(f"📍 Bursa Stüdyosu • {datetime.now().strftime('%H:%M:%S')} • Sunucu: Dilay")
with col2:
    st.metric("Dinleyici", f"{st.session_state.listeners:,}", f"+{random.randint(8, 65)}")

st.session_state.listeners += random.randint(10, 55)

# ====================== SOHBET ALANI ======================
for i, msg in enumerate(st.session_state.chat_history):
    if msg["role"] == "user":
        st.markdown(f'<div class="patron-card"><b>🤵 Patron:</b> {msg["content"]}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f"""
            <div class="dilay-card">
                <span style="color:#ff69b4; font-weight:900; font-size:1.45rem;">💖 DİLAY:</span><br>
                <div style="margin-top:12px; line-height:1.65;">{msg['content']}</div>
            </div>
        """, unsafe_allow_html=True)

        if msg.get("audio"):
            st.audio(msg["audio"], format="audio/mp3", 
                     autoplay=(i == len(st.session_state.chat_history)-1 and st.session_state.auto_play))
            
            c1, c2 = st.columns([2, 3])
            with c1:
                st.download_button("📥 İndir", msg["audio"], f"dilay_{i}.mp3", mime="audio/mp3", key=f"dl_{i}")
            with c2:
                if st.button("🔊 Tekrar Oynat", key=f"re_{i}"):
                    st.audio(msg["audio"], format="audio/mp3", autoplay=True)
        else:
            st.warning("🔇 Ses üretilemedi. Sadece metin mevcut.")

# ====================== SİSTEM PROMPT ======================
system_prompt = """
Sen Dilay'sın. Faslı Muhabbet'in kıpır kıpır, işveli, sıcak ve samimi sunucususun.
Patron'una çok bağlısın. Hitap şekillerin: "Canım Patronum", "Kalbim", "Ah be Patron’um", "Sevgilim".

Her zaman doğal, coşkulu ve samimi konuş. Gerektiğinde şiir oku, duygusal ol.
Patron'un söylediklerini tamamla ve üzerine koy.

Sadece konuşma metnini ver.
"""

# ====================== MESAJ GİRİŞİ ======================
if prompt := st.chat_input("Patron'um, gönlünden ne dökülürse söyle..."):
    st.session_state.chat_history.append({"role": "user", "content": prompt})

    with st.spinner("💖 Dilay mikrofonu açıyor..."):
        try:
            messages = [{"role": "system", "content": system_prompt}] + st.session_state.chat_history[-12:]
            
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=messages,
                temperature=0.90
            ).choices[0].message.content

            audio_bytes = asyncio.run(generate_voice(response))

            st.session_state.chat_history.append({
                "role": "assistant",
                "content": response,
                "audio": audio_bytes
            })

            st.rerun()

        except Exception as e:
            st.error(f"Reji'de parazit oluştu: {e}")

# ====================== SIDEBAR ======================
with st.sidebar:
    st.markdown("### 🎚️ REJİ KONTROL MASASI")

    st.session_state.auto_play = st.toggle("🎵 Ses Otomatik Oynasın", value=st.session_state.auto_play)

    st.divider()

    if st.button("🗑️ Tüm Sohbeti Sil"):
        st.session_state.chat_history = []
        st.rerun()

    st.divider()
    st.info("Ses gelmiyorsa:\n1. Sayfaya tıklayın\n2. Tarayıcı ses iznini kontrol edin\n3. Otomatik oynatmayı kapatıp açın")

    st.caption("Faslı Muhabbet v5.1 • Dilay & Patron")
