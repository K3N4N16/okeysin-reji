import streamlit as st
from groq import Groq
from gtts import gTTS
import os
import base64
import time
import librosa
import numpy as np
import torch

# ====================== REJİ ÖZEL AYARLARI (v47.0) ======================
try:
    from fairseq.data.dictionary import Dictionary
    if hasattr(torch.serialization, 'add_safe_globals'):
        torch.serialization.add_safe_globals([Dictionary])
except: pass

import rvc_python.lib.audio as rvc_audio
import rvc_python.modules.vc.modules as rvc_modules

def ultra_safe_load(file, sr):
    try:
        y, _ = librosa.load(file, sr=sr)
        return y
    except: return np.zeros(sr)

rvc_audio.load_audio = ultra_safe_load
rvc_modules.load_audio = ultra_safe_load
# =====================================================================

GROQ_KEY = os.environ.get("GROQ_API_KEY") or st.secrets.get("GROQ_API_KEY")
client = Groq(api_key=GROQ_KEY)

BASE_DIR = os.getcwd()
RVC_MODELS_DIR = os.path.join(BASE_DIR, "rvc_models")
MODEL_NAME = "dilay" 

def process_rvc(text: str):
    temp_raw = "temp_raw.mp3"
    output_wav = "emel_executive.wav"
    try:
        # 1. Kaynak Sesi Üret
        tts = gTTS(text=text, lang='tr', slow=False)
        tts.save(temp_raw)

        # 2. RVC Dönüşümü
        from rvc_python.infer import RVCInference
        rvc = RVCInference(device="cpu", models_dir=RVC_MODELS_DIR)
        rvc.load_model(MODEL_NAME)

        # EXECUTIVE AYARLAR: 
        # f0_up_key=-2 sesi kalınlaştırır ve daha 'seksi/buğulu' hale getirir.
        rvc.infer_file(
            input_path=temp_raw, 
            output_path=output_wav,
            f0_up_key=-2,   # SESİ KALINLAŞTIRMA (İdeal derinlik: -2 veya -3)
            f0_method="pm",
            index_rate=0.9, # KLON BENZERLİĞİNİ MAKSİMUMA ÇIKARMA
        )

        timeout = 20
        start_time = time.time()
        while not os.path.exists(output_wav):
            if time.time() - start_time > timeout: break
            time.sleep(0.5)

        if os.path.exists(output_wav):
            with open(output_wav, "rb") as f:
                return f.read()
    except Exception as e:
        st.warning(f"Reji: Ses işleme senkronize ediliyor...")
        if os.path.exists(temp_raw):
            with open(temp_raw, "rb") as f: return f.read()
    finally:
        for f in [temp_raw, output_wav]:
            if os.path.exists(f): 
                try: os.remove(f)
                except: pass
    return None

# ====================== STREAMLIT RADYO ARAYÜZÜ ======================
st.set_page_config(page_title="Aşk-ı Muhabbet v47", layout="wide")

st.title("🎙️ AŞK-I MUHABBET - EXECUTIVE REJİ")
st.caption("📍 Bursa | v47.0 | Profesyonel Klon, Derin ve Akıcı Ses")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
        if "audio_bytes" in msg:
            st.audio(msg["audio_bytes"], format="audio/wav")

if prompt := st.chat_input("Patron, anonsunu gönder..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"): st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("🎧 Emel o buğulu sesiyle hazırlanıyor..."):
            try:
                clean_history = [{"role": m["role"], "content": m["content"]} for m in st.session_state.messages[-4:]]
                
                # AKIŞ VE TARZ TALİMATI:
                completion = client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=[{"role": "system", "content": 
                        "Sen profesyonel radyo sunucusu Emel'sin. Bursa semalarında gece kuşağı sunuyorsun. "
                        "Konuşma tarzın: Oldukça akıcı, hızlı, kendinden emin, profesyonel, "
                        "hafif buğulu, seksi ve derin bir ses tonuyla olmalı. "
                        "Cümlelerin kısa ama etkileyici olsun. Kelimeleri yuvarlamadan, tutkuyla söyle."}] + clean_history,
                    max_tokens=250
                )
                response_text = completion.choices[0].message.content.strip()
                st.markdown(response_text)
                
                audio_data = process_rvc(response_text)

                if audio_data:
                    st.audio(audio_data, format="audio/wav")
                    st.session_state.messages.append({
                        "role": "assistant", 
                        "content": response_text, 
                        "audio_bytes": audio_data
                    })
            except Exception as e:
                st.error(f"Reji Hatası: {e}")

st.divider()
st.caption("❤️ Bursa’nın En Derin Sesi | Kenan’ın Executive Rejisi")
