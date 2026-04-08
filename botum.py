import streamlit as st
import torch
from TTS.api import TTS
import os
from datetime import datetime

# ====================== DİLAY SES AYARLARI ======================
# Klonladığın ses dosyasının adı (çok önemli!)
DILAY_SES_DOSYASI = "dilay_klon_sesim.wav"

# Dilay'ın konuşma tarzı ayarları
SPEED = 0.91          # 0.88 = daha ağır ve derin, 0.95 = daha kıpır kıpır
TEMPERATURE = 0.66    # Daha duygusal ve işveli olsun

# Modeli yükle (bir kere yüklenir)
@st.cache_resource
def load_dilay_tts():
    device = "cuda" if torch.cuda.is_available() else "cpu"
    st.write(f"🎙️ Dilay'ın sesi yükleniyor... ({device})")
    model = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(device)
    return model

dilay_tts = load_dilay_tts()

# ====================== DİLAY KONUŞSUN ======================
def dilay_konus(metin: str):
    if not metin or metin.strip() == "":
        st.warning("Dilay'a bir şeyler söylemen lazım patron 😊")
        return None
    
    output_file = f"dilay_konusuyor_{datetime.now().strftime('%H%M%S')}.wav"
    
    with st.spinner("Dilay konuşuyor... Kalbim kıpır kıpır ❤️"):
        try:
            dilay_tts.tts_to_file(
                text=metin,
                speaker_wav=DILAY_SES_DOSYASI,
                language="tr",
                file_path=output_file,
                speed=SPEED,
                temperature=TEMPERATURE
            )
            return output_file
        except Exception as e:
            st.error(f"Dilay konuşurken hata: {e}")
            return None

# ====================== STREAMLIT ARAYÜZ ======================
st.title("🎙️ Kenan ile Faslı Muhabbet")
st.subheader("Dilay seninle konuşuyor...")

user_input = st.text_area("Dilay'a ne söylemek istiyorsun?", 
                          height=150,
                          placeholder="Ahhh Kenan’ım… bu akşam muhabbetimiz çok güzel olacak mı?")

if st.button("🔊 Dilay Konuşsun"):
    ses_dosyasi = dilay_konus(user_input)
    if ses_dosyasi:
        st.audio(ses_dosyasi, format="audio/wav", autoplay=True)
        st.success("Dilay konuştu! Dinle bakalım patron... 😘")

st.caption("Dilay'ın sesi senin klonladığın özel sesle konuşuyor ❤️")
