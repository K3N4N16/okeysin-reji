import streamlit as st
from groq import Groq
from gtts import gTTS
import edge_tts
import asyncio
import io
from datetime import datetime
import random

st.set_page_config(
    page_title="Faslı Muhabbet",
    layout="wide",
    page_icon="🎙️"
)

if "GROQ_API_KEY" not in st.secrets:
    st.error("⚠️ GROQ API Key eksik!")
    st.stop()

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

# ====================== SES MOTORU (gTTS Ana + Edge Yedek) ======================
def generate_voice(text: str):
    # 1. Önce gTTS dene (daha stabil)
    try:
        clean_text = text.replace("*", "").strip()
        tts = gTTS(text=clean_text, lang='tr', slow=False)
        buffer = io.BytesIO()
        tts.write_to_fp(buffer)
        buffer.seek(0)
        return buffer.read()
    except:
        pass

    # 2. Yedek olarak edge-tts dene
    try:
        clean_text = text.replace("*", "").strip()
        communicate = edge_tts.Communicate(clean_text, "tr-TR-DilaraNeural")
        audio_data = b""
        async for chunk in communicate.stream():
            if chunk["type"] == "audio":
                audio_data += chunk["data"]
        return audio_data if len(audio_data) > 5000 else None
    except:
        return None

# ====================== SESSION STATE ======================
if "history" not in st.session_state:
    st.session_state.history = []
if "auto_play" not in st.session_state:
    st.session_state.auto_play = True

# ====================== ÜST PANEL ======================
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
                st.download_button("📥 Ses İndir", msg["audio"], f"dilay_{i}.mp3", mime="audio/mp3", key=f"dl_{i}")
            with c2:
                if st.button("🔊 Tekrar Oynat", key=f"rep_{i}"):
                    st.audio(msg["audio"], format="audio/mp3", autoplay=True)
        else:
            st.warning("🔇 Ses üretilemedi. Sadece metin gösteriliyor.")

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

    st.caption("Faslı Muhabbet v9.9 • gTTS + Edge Yedek")
