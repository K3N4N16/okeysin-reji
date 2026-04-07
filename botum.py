import streamlit as st
from groq import Groq
import requests # ElevenLabs API için
import asyncio
import base64
from datetime import datetime
import random

# ====================== SAYFA AYARLARI ======================
st.set_page_config(
    page_title="Faslı Muhabbet v6.1",
    layout="wide",
    page_icon="🎙️",
    initial_sidebar_state="expanded"
)

# API Anahtarları Kontrolü
if "GROQ_API_KEY" not in st.secrets or "ELEVENLABS_API_KEY" not in st.secrets:
    st.error("⚠️ API Keyler eksik! GROQ_API_KEY ve ELEVENLABS_API_KEY'i ekleyin.")
    st.stop()

client = Groq(api_key=st.secrets["GROQ_API_KEY"])
ELEVENLABS_API_KEY = st.secrets["ELEVENLABS_API_KEY"]

# ====================== SES MOTORU (ELEVENLABS - Ultra Kalite) ======================
def generate_voice_elevenlabs(text: str):
    """ElevenLabs ile yüksek kaliteli ve duygusal ses üretimi"""
    # Popüler bir kadın sesi ID'si (Örn: 'EXAVITQu4vr4xnSDxMaL' - Bella veya Türkçe uyumlu biri)
    # ElevenLabs panelinden kendi beğendiğiniz sesin ID'sini buraya yapıştırabilirsiniz.
    VOICE_ID = "21m0pTJHtn71Zo8YvJ35" 
    
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}"
    
    headers = {
        "Accept": "audio/mpeg",
        "Content-Type": "application/json",
        "xi-api-key": ELEVENLABS_API_KEY
    }
    
    data = {
        "text": text,
        "model_id": "eleven_multilingual_v2", # En iyi Türkçe desteği bu modelde
        "voice_settings": {
            "stability": 0.45,       # Daha duygusal ve değişken tonlama için düşürüldü
            "similarity_boost": 0.75,
            "style": 0.6,            # İşve ve duygu katması için yükseltildi
            "use_speaker_boost": True
        }
    }

    try:
        response = requests.post(url, json=data, headers=headers)
        if response.status_code == 200:
            return response.content
        else:
            st.error(f"Ses hatası: {response.text}")
            return None
    except Exception as e:
        st.error(f"Bağlantı hatası: {e}")
        return None

# ====================== DİLAY PROMPT (Ses Uyumu İçin Optimize Edildi) ======================
dilay_prompt = """
Sen Dilay'sın. Faslı Muhabbet'in çok samimi, işveli, neşeli ve duygusal sunucususun.
Patron'una (Kenan) çok bağlısın. Ona "Canım Patronum", "Kalbim", "Ah be Patron’um" diye hitap et.
Konuşurken aralara "Hımm", "Yaa", "Canım benim" gibi küçük ünlemler ekle ki ses motoru daha doğal tepkiler versin.
Sadece konuşma metnini ver, asla teknik not yazma.
"""

# ... (CSS ve Session State kısımları aynı kalabilir) ...

# ====================== MESAJ İŞLEME (GÜNCEL) ======================
if prompt := st.chat_input("Patron'um, gönlünden ne geçiyorsa söyle..."):
    st.session_state.history.append({"role": "user", "content": prompt})

    with st.spinner("💖 Dilay hazırlanıyor, sesi ayarlanıyor..."):
        try:
            messages = [{"role": "system", "content": dilay_prompt}] + st.session_state.history[-12:]
            
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=messages,
                temperature=0.9
            ).choices[0].message.content

            # ElevenLabs ile kaliteli ses üretimi
            audio_bytes = generate_voice_elevenlabs(response)

            st.session_state.history.append({
                "role": "assistant",
                "content": response,
                "audio": audio_bytes
            })
            st.rerun()

        except Exception as e:
            st.error(f"Hata: {e}")
