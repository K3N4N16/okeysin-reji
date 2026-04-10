import streamlit as st
from groq import Groq
from gtts import gTTS
from rvc_python.infer import RVCInference # RVC Motoru
import os
import requests
import io
import base64
from datetime import datetime

# ====================== MODEL MERKEZİ ======================
PTH_URL = "https://huggingface.co/matroks/dilay/resolve/main/my-project_60e_660s.pth"
INDEX_URL = "https://huggingface.co/matroks/dilay/resolve/main/my-project.index"

# Dosyaları İndirme Kontrolü
def setup_rvc_model():
    if not os.path.exists("models"):
        os.makedirs("models")
    
    pth_path = "models/dilay.pth"
    index_path = "models/dilay.index"
    
    if not os.path.exists(pth_path):
        with st.spinner("📥 Dilay Modeli (PTH) indiriliyor..."):
            r = requests.get(PTH_URL)
            open(pth_path, "wb").write(r.content)
            
    if not os.path.exists(index_path):
        with st.spinner("📥 İndeks dosyası indiriliyor..."):
            r = requests.get(INDEX_URL)
            open(index_path, "wb").write(r.content)
    
    return pth_path, index_path

# ====================== SAYFA AYARLARI ======================
st.set_page_config(page_title="Dilay RVC v14.0", layout="wide", page_icon="🎙️")

if "GROQ_API_KEY" not in st.secrets:
    st.error("⚠️ GROQ API Key Eksik!")
    st.stop()

client = Groq(api_key=st.secrets["GROQ_API_KEY"])
pth_file, index_file = setup_rvc_model()

# ====================== RVC DÖNÜŞÜM MOTORU ======================
def get_klon_ses(text):
    """Metni gTTS ile üretir, RVC ile senin sesine çevirir."""
    try:
        # 1. Ham Ses (Kaynak)
        tts = gTTS(text=text, lang='tr')
        source_path = "temp_source.mp3"
        output_path = "temp_output.wav"
        tts.save(source_path)

        # 2. RVC Dönüşümü (Senin Modeline Göre)
        rvc = RVCInference()
        rvc.set_model(pth_file) # Senin .pth dosyanı takıyoruz
        
        # Sesi Dönüştür (f0_method: 'rmvpe' en kalitelisidir)
        rvc.infer(
            input_path=source_path,
            output_path=output_path,
            index_path=index_file, # Senin .index dosyan
            f0_method="rmvpe", 
            f0_up_key=0 # Gerekirse sesi inceltmek/kalınlaştırmak için burayı oynarız
        )

        with open(output_path, "rb") as f:
            return f.read()
            
    except Exception as e:
        st.error(f"Klonlama Hatası: {e}")
        return None

# ====================== RADYO ARAYÜZÜ ======================
st.markdown(f"## 🎙️ FASLI MUHABBET <span style='color:#ff1493;'>● RVC AKTİF</span>", unsafe_allow_html=True)
st.caption(f"Bursa Stüdyosu | Model: {pth_file}")

if "chat" not in st.session_state:
    st.session_state.chat = []

# Mesajları Görüntüle
for m in st.session_state.chat:
    with st.chat_message(m["role"]):
        st.write(m["content"])
        if "audio" in m:
            st.audio(m["audio"])

# Yeni Mesaj
if prompt := st.chat_input("Patron, modelini konuştur..."):
    st.session_state.chat.append({"role": "user", "content": prompt})
    with st.chat_message("user"): st.write(prompt)

    with st.chat_message("assistant"):
        with st.spinner("💖 Dilay ruhunu modele üflüyor..."):
            # Llama Cevabı
            res = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[{"role": "system", "content": "Sen Dilay'sın, Bursa'dan neşeli bir radyo sunucususun."}] + st.session_state.chat[-5:]
            ).choices[0].message.content
            
            # Ses Dönüşümü
            audio = get_klon_ses(res)
            
            st.write(res)
            if audio:
                st.audio(audio)
                st.session_state.chat.append({"role": "assistant", "content": res, "audio": audio})
