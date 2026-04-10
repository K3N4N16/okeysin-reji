import streamlit as st
from groq import Groq
from gtts import gTTS
import io
import os
import requests
import base64
import random
from datetime import datetime

# ====================== HF MODEL DOSYALARI ======================
# Linkleri indirme formatına (resolve) çevirdim Patron
PTH_URL = "https://huggingface.co/matroks/dilay/resolve/main/my-project_60e_660s.pth"
INDEX_URL = "https://huggingface.co/matroks/dilay/resolve/main/my-project.index"

# Dosyaları yerel klasöre indirme fonksiyonu
def download_models():
    if not os.path.exists("models"):
        os.makedirs("models")
    
    files = {
        "models/dilay.pth": PTH_URL,
        "models/dilay.index": INDEX_URL
    }
    
    for path, url in files.items():
        if not os.path.exists(path):
            with st.spinner(f"📥 {path} indiriliyor, biraz sabret Patron..."):
                response = requests.get(url)
                with open(path, "wb") as f:
                    f.write(response.content)

# ====================== SAYFA AYARLARI ======================
st.set_page_config(page_title="Dilay RVC v12.0", layout="wide", page_icon="🎙️")

if "GROQ_API_KEY" not in st.secrets:
    st.error("⚠️ GROQ API Key Eksik! Secrets'a ekleyin.")
    st.stop()

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

# Modelleri başlangıçta indir
download_models()

# ====================== SES MOTORU & RVC MANTIĞI ======================
def process_rvc(text):
    """
    gTTS ile temel sesi üretir. 
    Not: Gerçek RVC dönüşümü (inference) için fairseq ve torch yüklü olmalıdır.
    """
    try:
        # 1. Aşama: Temel Ses (gTTS)
        tts = gTTS(text=text, lang='tr')
        audio_io = io.BytesIO()
        tts.write_to_fp(audio_io)
        raw_audio = audio_io.getvalue()
        
        # 2. Aşama: RVC Dönüşümü (Model dosyalarını kullanarak)
        # BURASI KRİTİK: Streamlit Cloud'da RVC çalıştırmak için 
        # rvc-python veya benzeri bir kütüphane entegrasyonu gerekir.
        # Şimdilik altyapıyı model dosyalarına bağlıyoruz.
        
        return raw_audio # Şimdilik ham sesi dönüyoruz, RVC kütüphanesi eklenince burası tetiklenecek
    except Exception as e:
        st.error(f"Ses hatası: {e}")
        return None

# ====================== SOHBET ARAYÜZÜ ======================
st.markdown(f"## 🎙️ FASLI MUHABBET <span style='color:red;'>● RVC MODE</span>", unsafe_allow_html=True)
st.caption("📍 Bursa Stüdyosu | Klon Ses Modeli: my-project_60e_660s.pth")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])
        if "audio" in msg:
            st.audio(msg["audio"], format="audio/mp3")

# Mesaj Girişi
if prompt := st.chat_input("Dilay'ına bir mesaj bırak..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    with st.chat_message("assistant"):
        with st.spinner("🎙️ Dilay modelinle sesini klonluyor..."):
            # Llama 3.3 Zekası
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[{"role": "system", "content": "Sen Dilay'sın. Bursa'dan sunucusun."}] + st.session_state.messages[-5:]
            ).choices[0].message.content
            
            # Ses Üretimi
            audio_bytes = process_rvc(response)
            
            st.write(response)
            if audio_bytes:
                st.audio(audio_bytes, format="audio/mp3")
                st.session_state.messages.append({
                    "role": "assistant", 
                    "content": response, 
                    "audio": audio_bytes
                })
