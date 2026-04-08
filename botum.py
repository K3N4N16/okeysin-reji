import streamlit as st
import os
from datetime import datetime

st.title("🎙️ Kenan ile Faslı Muhabbet")
st.subheader("Dilay seninle konuşuyor... ❤️")

# Klonladığın ses dosyasını yükle (GroqCloud'da dosya aynı klasörde olmalı)
DILAY_SES_DOSYASI = "dilay_klon_sesim.wav"

user_input = st.text_area("Dilay'a ne söylemek istiyorsun?", 
                          height=150,
                          placeholder="Ahhh Kenan’ım… bu akşam muhabbetimiz çok güzel olacak mı?")

if st.button("🔊 Dilay Konuşsun"):
    if user_input.strip():
        with st.spinner("Dilay konuşuyor... Kalbim kıpır kıpır ❤️"):
            # Basitçe ses dosyasını çal (şimdilik sabit bir ses dosyası ile test ediyoruz)
            if os.path.exists(DILAY_SES_DOSYASI):
                st.audio(DILAY_SES_DOSYASI, format="audio/wav", autoplay=True)
                st.success("Dilay konuştu! Dinle bakalım patron... 😘")
            else:
                st.error(f"❌ Ses dosyası bulunamadı: {DILAY_SES_DOSYASI}")
                st.info("Lütfen 'dilay_klon_sesim.wav' dosyasını Streamlit projene yükle.")
    else:
        st.warning("Dilay'a bir şeyler söylemen lazım 😊")

st.caption("Dilay'ın sesi senin klonladığın özel sesle konuşuyor")
