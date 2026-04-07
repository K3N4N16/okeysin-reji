import streamlit as st
from groq import Groq
import edge_tts
import asyncio
import io
from datetime import datetime
import random

# ====================== SAYFA AYARLARI ======================
st.set_page_config(
    page_title="Faslı Muhabbet v6.5",
    layout="wide",
    page_icon="🎙️"
)

# API Key Kontrolü
if "GROQ_API_KEY" not in st.secrets:
    st.error("⚠️ GROQ API Key bulunamadı! Lütfen Secrets'a ekleyin.")
    st.stop()

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

# ====================== EN POPÜLER ÜCRETSİZ SES (Edge AI) ======================
async def generate_voice_edge(text: str):
    """
    Şu an en popüler ve akıcı Türkçe AI sesi olan Dilara'yı kullanır.
    Tamamen ücretsiz ve yüksek kalitedir.
    """
    # tr-TR-DilaraNeural -> En popüler, genç ve enerjik Türkçe ses.
    # Alternatif (Daha tok ses): tr-TR-AhmetNeural
    voice = "tr-TR-DilaraNeural" 
    
    # Hızı hafif artırıp perdeyi (pitch) biraz incelterek daha işveli hale getiriyoruz
    communicate = edge_tts.Communicate(text, voice, rate="+8%", pitch="+2Hz")
    
    audio_data = io.BytesIO()
    async for chunk in communicate.stream():
        if chunk["type"] == "audio":
            audio_data.write(chunk["data"])
    
    return audio_data.getvalue()

# ====================== MODERN RADYO TASARIMI (CSS) ======================
st.markdown("""
    <style>
    .stApp { background: #050505; color: #ffffff; }
    .dilay-bubble {
        background: linear-gradient(135deg, #6a11cb 0%, #2575fc 100%);
        color: white;
        padding: 20px;
        border-radius: 20px 20px 20px 0px;
        margin: 15px 0;
        border-left: 5px solid #00f2fe;
        font-size: 1.2rem;
        box-shadow: 0 5px 15px rgba(0,0,0,0.3);
    }
    .patron-bubble {
        background: #1a1a1a;
        color: #00ff9d;
        padding: 15px;
        border-radius: 20px 20px 0px 20px;
        margin: 10px 0;
        border-right: 4px solid #00ff9d;
        text-align: right;
        font-weight: 500;
    }
    .live-indicator {
        color: #ff4b4b;
        font-weight: bold;
        animation: pulse 1.5s infinite;
    }
    @keyframes pulse { 0% { opacity: 1; } 50% { opacity: 0.3; } 100% { opacity: 1; } }
    </style>
    """, unsafe_allow_html=True)

# ====================== SESSION STATE ======================
if "history" not in st.session_state:
    st.session_state.history = []

# ====================== BAŞLIK ======================
st.markdown(f"## 🎙️ FASLI MUHABBET <span class='live-indicator'>● CANLI YAYIN</span>", unsafe_allow_html=True)
st.caption(f"📍 Bursa Merkez Stüdyoları | {datetime.now().strftime('%H:%M')}")

# ====================== MESAJLARI GÖSTER ======================
for i, msg in enumerate(st.session_state.history):
    if msg["role"] == "user":
        st.markdown(f'<div class="patron-bubble">🤵 Patron Kenan: {msg["content"]}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="dilay-bubble"><b>💖 DİLAY:</b><br>{msg["content"]}</div>', unsafe_allow_html=True)
        if msg.get("audio"):
            st.audio(msg["audio"], format="audio/mp3", autoplay=(i == len(st.session_state.history)-1))

# ====================== DİLAY PROMPT ======================
# Ses tonuna uygun, enerjik ve sevgi dolu bir karakter
dilay_system = """
Sen Dilay'sın. Radyo dünyasının en sevilen, en neşeli ve samimi kadın sunucususun.
Patronun Kenan'a karşı her zaman çok saygılı ama bir o kadar da içten ve işvelisin.
Ona "Canım Patronum", "Paşam", "Kalbim" gibi sevgi dolu hitaplar kullan.
Cümlelerin kısa, öz ve radyo akışına uygun olsun.
Arada "Eveeet", "Harika!" gibi ünlemler kullanarak canlı yayını hareketlendir.
"""

# ====================== YENİ MESAJ GİRİŞİ ======================
if prompt := st.chat_input("Dilay'a bir mesaj gönder..."):
    st.session_state.history.append({"role": "user", "content": prompt})
    
    with st.spinner("✨ Dilay yayına giriyor..."):
        try:
            # Groq ile metni üret
            messages = [{"role": "system", "content": dilay_system}] + st.session_state.history[-10:]
            res = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=messages,
                temperature=0.8
            ).choices[0].message.content
            
            # Edge-TTS ile popüler AI sesini üret
            audio_bytes = asyncio.run(generate_voice_edge(res))
            
            st.session_state.history.append({
                "role": "assistant",
                "content": res,
                "audio": audio_bytes
            })
            st.rerun()
            
        except Exception as e:
            st.error(f"Sistemde bir parazit var: {e}")

# ====================== YAN PANEL ======================
with st.sidebar:
    st.image("https://img.icons8.com/neon/96/microphone.png")
    st.title("Stüdyo Kontrol")
    st.write(f"🎧 **Aktif Ses:** Dilara Neural (AI)")
    st.write(f"📡 **Kalite:** 320kbps Crystal Clear")
    
    if st.button("🔄 Yayını Yenile"):
        st.session_state.history = []
        st.rerun()
