import streamlit as st
from groq import Groq
import os
import random
import asyncio
import edge_tts
import time

# ====================== 1. GENEL AYARLAR ======================
st.set_page_config(page_title="Aşk-ı Muhabbet v11.5", layout="wide")

# API Kontrol
if "GROQ_API_KEY" not in st.secrets:
    st.error("GROQ_API_KEY bulunamadı!")
    st.stop()

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

# ====================== 2. SİSTEM BAŞLATMA ======================
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# ====================== 3. SES MOTORU (EDGE-TTS) ======================
async def generate_voice(text, voice_name):
    communicate = edge_tts.Communicate(text, voice_name)
    audio_data = b""
    async for chunk in communicate.stream():
        if chunk["type"] == "audio":
            audio_data += chunk["data"]
    return audio_data

# ====================== 4. TASARIM (CSS) ======================
st.markdown("""
    <style>
    .stApp { background-color: #05050a; color: #ffffff; }
    .host-card { padding: 20px; border-radius: 15px; margin-bottom: 15px; border-left: 10px solid; }
    .dilay-theme { background: #2a0a25; border-color: #ff1493; }
    .mert-theme { background: #0a252a; border-color: #00d4ff; }
    .patron-bubble { background: rgba(0, 255, 157, 0.1); border-right: 5px solid #00ff9d; padding: 10px; text-align: right; }
    </style>
    """, unsafe_allow_html=True)

# ====================== 5. REJİ VE AKIŞ ======================
with st.sidebar:
    st.title("🎚️ REJİ")
    secilen_sunucu = st.radio("Sunucu:", ["Dilay 💖", "Mert 🎙️"])
    yayin_enerjisi = st.select_slider("Enerji:", ["Sakin", "Standart", "Muzip"])
    if st.button("Yayını Temizle"):
        st.session_state.chat_history = []
        st.rerun()

st.title("🎙️ AŞK-I MUHABBET CANLI")

# SARMAL DÖNGÜ: Mesajları ve Sesleri Ekrana Bas
for i, chat in enumerate(st.session_state.chat_history):
    if chat["role"] == "user":
        st.markdown(f'<div class="patron-bubble">{chat["content"]}</div>', unsafe_allow_html=True)
    else:
        tema = "dilay-theme" if chat["host"] == "Dilay 💖" else "mert-theme"
        st.markdown(f'<div class="host-card {tema}"><b>{chat["host"]}</b><br>{chat["content"]}</div>', unsafe_allow_html=True)
        
        if chat.get("audio"):
            # Sadece en son mesajın otomatik çalması için kontrol
            is_latest = (i == len(st.session_state.chat_history) - 1)
            # Benzersiz KEY (Hatanın çözümü burasıdır)
            unique_key = f"audio_v11_{i}_{int(time.time())}"
            st.audio(chat["audio"], format="audio/wav", autoplay=is_latest, key=unique_key)

# ====================== 6. AI VE SES TETİKLEME ======================
personalar = {
    "Dilay 💖": {"prompt": "Sen Dilay'sın. Cilveli ve neşelisin.", "voice": "tr-TR-EmelNeural"},
    "Mert 🎙️": {"prompt": "Sen Mert'sin. Ağırbaşlı ve samimisin.", "voice": "tr-TR-AhmetNeural"}
}

if prompt := st.chat_input("Mesajınızı yazın..."):
    st.session_state.chat_history.append({"role": "user", "content": prompt})
    
    with st.spinner("Seslendiriliyor..."):
        # AI Yanıtı
        messages = [{"role": "system", "content": personalar[secilen_sunucu]["prompt"]}] + \
                   [{"role": m["role"], "content": m["content"]} for m in st.session_state.chat_history[-6:]]
        
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=messages,
            temperature=0.7
        ).choices[0].message.content

        # Ses Üretimi (Asenkron çalıştırma)
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        audio_content = loop.run_until_complete(generate_voice(response, personalar[secilen_sunucu]["voice"]))

        st.session_state.chat_history.append({
            "role": "assistant",
            "host": secilen_sunucu,
            "content": response,
            "audio": audio_content
        })
        st.rerun()
