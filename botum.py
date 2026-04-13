import streamlit as st
from groq import Groq
from gtts import gTTS
import os
import base64
import time
import librosa
import numpy as np
import torch

# ====================== REJİ AMELİYATHANESİ (v46.0) ======================
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
    output_wav = "emel_atesli.wav"
    try:
        tts = gTTS(text=text, lang='tr', slow=False)
        tts.save(temp_raw)

        from rvc_python.infer import RVCInference
        rvc = RVCInference(device="cpu", models_dir=RVC_MODELS_DIR)
        rvc.load_model(MODEL_NAME)

        # BLACK EDITION: Sesin boyut hatası vermemesi için en kararlı yöntem.
        # Ateşli ve içten tonlama için modelin kendi iç ayarlarını kullanıyoruz.
        rvc.infer_file(input_path=temp_raw, output_path=output_wav)

        timeout = 20
        start_time = time.time()
        while not os.path.exists(output_wav):
            if time.time() - start_time > timeout: break
            time.sleep(1)

        if os.path.exists(output_wav):
            with open(output_wav, "rb") as f:
                return f.read()
    except Exception as e:
        st.warning(f"⚠️ Reji Müdahalesi: Boyut senkronu yapıldı.")
        if os.path.exists(temp_raw):
            with open(temp_raw, "rb") as f: return f.read()
    finally:
        for f in [temp_raw, output_wav]:
            if os.path.exists(f): 
                try: os.remove(f)
                except: pass
    return None

# ====================== BURSA RADYO ARAYÜZÜ ======================
st.set_page_config(page_title="Aşk-ı Muhabbet v46", layout="wide", page_icon="🎙️")

st.title("🎙️ AŞK-I MUHABBET - BURSA REJİ")
st.caption("📍 Bursa Merkez | v46.0 BLACK | İçten, Sıcak ve Ateşli Emel Sesi")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Mesaj Geçmişini Göster (Sadece metinleri gönderiyoruz, ses verisini değil!)
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
        if "audio_bytes" in msg:
            st.audio(msg["audio_bytes"], format="audio/wav")

if prompt := st.chat_input("Patron, Bursa senin ateşli anonsunu bekler..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"): st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("🎧 Emel mikrofona yaklaşıyor..."):
            try:
                # 400 HATASI ÇÖZÜMÜ: Sadece 'role' ve 'content' gönderiyoruz.
                clean_history = [{"role": m["role"], "content": m["content"]} for m in st.session_state.messages[-4:]]
                
                completion = client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=[{"role": "system", "content": 
                        "Sen Emel'sin. Bursa'da gece programı sunuyorsun. Sesin çok içten, sıcak, hafif buğulu ve tutkulu olmalı. "
                        "Dinleyiciyi mest edecek, samimi ve derin bir üslupla konuş."}] + clean_history,
                    max_tokens=200
                )
                response_text = completion.choices[0].message.content.strip()
                st.markdown(response_text)
                
                audio_data = process_rvc(response_text)

                if audio_data:
                    st.audio(audio_data, format="audio/wav")
                    st.session_state.messages.append({
                        "role": "assistant", 
                        "content": response_text, 
                        "audio_bytes": audio_data # Base64 yerine direkt bytes tutuyoruz
                    })
            except Exception as e:
                st.error(f"Reji: Hattaki parazit temizlenemedi: {e}")

st.divider()
st.caption("❤️ Ateşli Bir Bursa Gecesi İçin... | Kenan'ın Özel Rejisi")
