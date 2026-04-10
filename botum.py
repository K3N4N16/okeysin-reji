import streamlit as st
from groq import Groq
from gtts import gTTS
import os
import base64
import io

# ====================== RVC GÜVENLİK DUVARI ======================
try:
    from rvc_python.infer import RVCInference
    RVC_ENABLED = True
except (ImportError, ModuleNotFoundError):
    RVC_ENABLED = False

# ====================== SAYFA AYARLARI ======================
st.set_page_config(page_title="Faslı Muhabbet v15.0", layout="wide", page_icon="🎙️")

if "GROQ_API_KEY" not in st.secrets:
    st.error("⚠️ GROQ API Key Eksik!")
    st.stop()

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

# ====================== SES MOTORU (AKILLI SEÇİM) ======================
def generate_voice_dynamic(text):
    clean_text = text.replace("*", "").strip()
    
    # 1. Senaryo: RVC Kütüphanesi ve Modeller Hazırsa
    if RVC_ENABLED and os.path.exists("models/dilay.pth"):
        try:
            # RVC Dönüşümü
            tts = gTTS(text=clean_text, lang='tr')
            tts.save("source.mp3")
            
            rvc = RVCInference()
            rvc.set_model("models/dilay.pth")
            rvc.infer("source.mp3", "output.wav", index_path="models/dilay.index")
            
            with open("output.wav", "rb") as f:
                return f.read()
        except Exception as e:
            st.warning(f"RVC İşlenemedi, Yedek Sese Geçiliyor... (Hata: {e})")
    
    # 2. Senaryo: RVC Yoksa Standart gTTS (Yedek Plan)
    tts = gTTS(text=clean_text, lang='tr')
    audio_io = io.BytesIO()
    tts.write_to_fp(audio_io)
    return audio_io.getvalue()

# ====================== REJİ PANELİ ======================
st.markdown(f"## 🎙️ FASLI MUHABBET <span style='color:red;'>● CANLI</span>", unsafe_allow_html=True)

if RVC_ENABLED:
    st.success("✅ RVC Motoru Hazır: Klon Ses Aktif!")
else:
    st.info("ℹ️ Yedek Ses Motoru Aktif (Klon kütüphanesi yüklenemedi).")

# Sohbet Akışı
if "history" not in st.session_state:
    st.session_state.history = []

for msg in st.session_state.history:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])
        if "audio" in msg:
            st.audio(msg["audio"])

# Mesaj Girişi
if prompt := st.chat_input("Mesajını yaz Patron..."):
    st.session_state.history.append({"role": "user", "content": prompt})
    
    with st.spinner("💖 Dilay hazırlanıyor..."):
        res = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "system", "content": "Sen Dilay'sın."}] + st.session_state.history[-5:]
        ).choices[0].message.content
        
        audio = generate_voice_dynamic(res)
        
        st.session_state.history.append({"role": "assistant", "content": res, "audio": audio})
        st.rerun()
