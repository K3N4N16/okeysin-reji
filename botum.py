import streamlit as st
from groq import Groq
import asyncio
import edge_tts
import time
import base64

# Sayfa Yapılandırması
st.set_page_config(page_title="Faslı Muhabbet v10.0", layout="wide", page_icon="🎙️")

# API Kontrol
if "GROQ_API_KEY" not in st.secrets:
    st.error("⚠️ API Key Eksik!")
    st.stop()

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

# Session State Yönetimi
if "history" not in st.session_state:
    st.session_state.history = []
if "is_broadcasting" not in st.session_state:
    st.session_state.is_broadcasting = False

# Ses Tanımları
VOICES = {
    "Dilay 💖": "tr-TR-EmelNeural",
    "Mert 🎙️": "tr-TR-AhmetNeural"
}

# 

async def produce_voice(text, voice):
    communicate = edge_tts.Communicate(text, voice, rate="+5%", pitch="+0Hz")
    audio_bytes = b""
    async for chunk in communicate.stream():
        if chunk["type"] == "audio":
            audio_bytes += chunk["data"]
    return audio_bytes

# CSS: Cyberpunk Radyo Teması
st.markdown("""
    <style>
    .stApp { background: #020205; color: #e0e0e0; }
    .broadcast-box { 
        border: 2px solid #ff1493; border-radius: 15px; padding: 20px;
        background: rgba(255, 20, 147, 0.05); box-shadow: 0 0 20px rgba(255, 20, 147, 0.2);
    }
    .host-dilay { color: #ff69b4; text-shadow: 0 0 10px #ff69b4; font-weight: bold; }
    .host-mert { color: #00d4ff; text-shadow: 0 0 10px #00d4ff; font-weight: bold; }
    .on-air { background: red; color: white; padding: 2px 8px; border-radius: 5px; font-size: 12px; animation: blink 1s infinite; }
    @keyframes blink { 50% { opacity: 0; } }
    </style>
    """, unsafe_allow_html=True)

# Başlık Paneli
col_title, col_stat = st.columns([4, 1])
with col_title:
    st.markdown("## 🎙️ FASLI MUHABBET <span class='on-air'>ON AIR</span>", unsafe_allow_html=True)
with col_stat:
    st.write(f"🎧 {7892 + (int(time.time()) % 100)} Dinleyici")

# Sohbet Geçmişi Render
chat_container = st.container()
with chat_container:
    for msg in st.session_state.history:
        if msg["role"] == "user":
            st.markdown(f"**🤵 Patron:** {msg['content']}")
        else:
            style = "host-dilay" if "Dilay" in msg["host"] else "host-mert"
            st.markdown(f"<div class='broadcast-box'><span class='{style}'>{msg['host']}:</span><br>{msg['content']}</div>", unsafe_allow_html=True)
            if msg.get("audio"):
                st.audio(msg["audio"], format="audio/mp3")

# Gelişmiş Prompt Mühendisliği
def get_system_prompt(host, partner_name):
    base = f"Sen {host} karakterisin. Faslı Muhabbet isimli radyo programını {partner_name} ile beraber sunuyorsun."
    if "Dilay" in host:
        return base + """ Karakterin: Cilveli, neşeli, bazen Mert'e takılan ama ona çok değer veren bir kadın. 
        Mert'in laflarına mutlaka karşılık ver, onunla şakalaş. Patron'una 'Canım Patronum' diye hitap et. 
        Kısa, enerjik ve radyo dilinde konuş."""
    else:
        return base + """ Karakterin: Hafif maço ama beyefendi, esprili ve hazırcevap bir erkek. 
        Dilay'ın cilvelerine karşı hem onu koruyan hem de ona laf yetiştiren bir tavır takın. 
        Radyo yayını akıcılığında konuş."""

# Yayın Tetikleyici
if prompt := st.chat_input("Patron, bir konu ver yayına başlayalım..."):
    st.session_state.history.append({"role": "user", "content": prompt})
    
    # Sırasıyla Konuşturma Mantığı
    hosts = [("Dilay 💖", "Mert 🎙️"), ("Mert 🎙️", "Dilay 💖")]
    
    for host_name, partner in hosts:
        with st.spinner(f"🎙️ {host_name} konuşuyor..."):
            # Geçmişi hatırla (İkili diyalog için son 10 mesajı gönder)
            messages = [{"role": "system", "content": get_system_prompt(host_name, partner)}]
            for h in st.session_state.history[-10:]:
                messages.append({"role": h["role"], "content": h["content"]})
            
            # Groq'tan yanıt al
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=messages,
                temperature=0.85
            ).choices[0].message.content
            
            # Ses Üret
            audio_data = asyncio.run(produce_voice(response, VOICES[host_name]))
            
            # Kaydet ve Göster
            st.session_state.history.append({
                "role": "assistant",
                "host": host_name,
                "content": response,
                "audio": audio_data
            })
            st.rerun()
