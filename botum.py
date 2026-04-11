import streamlit as st
from groq import Groq
import edge_tts
from gtts import gTTS
import asyncio
import os
import io
import base64
from datetime import datetime

# ====================== RVC GÜVENLİK KONTROLÜ ======================
# Kütüphane yüklenemezse hata vermemesi için korumaya alıyoruz
try:
    from rvc_python.infer import RVCInference
    RVC_AVAILABLE = True
except (ImportError, ModuleNotFoundError):
    RVC_AVAILABLE = False

# ====================== SAYFA AYARLARI ======================
st.set_page_config(page_title="Faslı Muhabbet v16.0", layout="wide", page_icon="🎙️")

if "GROQ_API_KEY" not in st.secrets:
    st.error("⚠️ GROQ API Key Eksik! Lütfen Streamlit Secrets'a ekle Patron.")
    st.stop()

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

# ====================== SES ÜRETİM MOTORLARI ======================

async def generate_edge_voice(text):
    """Edge-TTS: En kaliteli yedek ses (Filiz)"""
    try:
        communicate = edge_tts.Communicate(text, "tr-TR-FilizNeural")
        audio_data = b""
        async for chunk in communicate.stream():
            if chunk["type"] == "audio":
                audio_data += chunk["data"]
        return audio_data
    except:
        return None

def generate_gtts_voice(text):
    """gTTS: En garantici yedek ses"""
    tts = gTTS(text=text, lang='tr')
    fp = io.BytesIO()
    tts.write_to_fp(fp)
    return fp.getvalue()

# ====================== ANA REJİ MANTIĞI ======================
st.markdown(f"## 🎙️ FASLI MUHABBET <span style='color:red;'>● CANLI</span>", unsafe_allow_html=True)
st.caption(f"📍 Bursa Stüdyosu | Sunucu: Dilay | {datetime.now().strftime('%H:%M')}")

if not RVC_AVAILABLE:
    st.info("ℹ️ **Bilgi:** Klon motoru bu sunucuda desteklenmiyor. Dilay şu an **Yedek Ses Sistemi (Filiz)** üzerinden konuşuyor.")

if "history" not in st.session_state:
    st.session_state.history = []

# Mesajları Göster
for msg in st.session_state.history:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])
        if "audio" in msg:
            st.audio(msg["audio"])

# Giriş Alanı
if prompt := st.chat_input("Patron, bir şeyler fısılda..."):
    st.session_state.history.append({"role": "user", "content": prompt})
    
    with st.spinner("💖 Dilay hazırlanıyor..."):
        # Llama 3.3 Cevabı
        sys_msg = "Sen Dilay'sın. Bursa'dan neşeli, işveli bir radyo sunucususun. Patronuna (Kenan) aşıksın."
        res = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "system", "content": sys_msg}] + st.session_state.history[-5:]
        ).choices[0].message.content
        
        # Önce Edge-TTS deniyoruz, olmazsa gTTS
        audio = asyncio.run(generate_edge_voice(res))
        if not audio:
            audio = generate_gtts_voice(res)
            
        st.session_state.history.append({"role": "assistant", "content": res, "audio": audio})
        st.rerun()
