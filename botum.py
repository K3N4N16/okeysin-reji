import streamlit as st
from groq import Groq
import edge_tts
import asyncio
import io
import re
import base64
from datetime import datetime
import random

# ====================== SAYFA AYARLARI ======================
st.set_page_config(
    page_title="Faslı Muhabbet v7.5",
    layout="wide",
    page_icon="🎙️"
)

# API Key Kontrolü
if "GROQ_API_KEY" not in st.secrets:
    st.error("⚠️ GROQ API Key eksik! Lütfen Streamlit Secrets'a ekleyin.")
    st.stop()

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

# ====================== SES MOTORU & OTOMATİK OYNATICI ======================
async def get_voice_bytes(text):
    """Dilara sesiyle kaliteli ses üretir"""
    try:
        # AI sesini bozan karakterleri temizle
        clean_text = re.sub(r'[*_#~>]', '', text).strip()
        if not clean_text: return None

        voice = "tr-TR-DilaraNeural"
        communicate = edge_tts.Communicate(clean_text, voice, rate="+7%", pitch="+2Hz")
        
        audio_stream = io.BytesIO()
        async for chunk in communicate.stream():
            if chunk["type"] == "audio":
                audio_stream.write(chunk["data"])
        return audio_stream.getvalue()
    except:
        return None

def autoplay_audio(audio_bytes):
    """Sesi sayfaya gömer ve otomatik oynatmayı tetikler"""
    b64 = base64.b64encode(audio_bytes).decode()
    md = f"""
        <audio autoplay="true" controls style="width: 100%; border-radius: 10px; margin-top: 10px;">
        <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
        </audio>
    """
    st.markdown(md, unsafe_allow_html=True)

# ====================== MODERN UI ======================
st.markdown("""
    <style>
    .stApp { background: #0a0a0a; color: #ffffff; }
    .dilay-card {
        background: linear-gradient(135deg, #2b0040 0%, #000000 100%);
        border-left: 5px solid #ff007f;
        padding: 20px;
        border-radius: 15px;
        margin: 15px 0;
        box-shadow: 0 4px 15px rgba(255,0,127,0.3);
    }
    .patron-card {
        background: #1a1a1a;
        border-right: 4px solid #00f2fe;
        padding: 12px;
        border-radius: 10px;
        text-align: right;
        margin: 10px 0;
    }
    </style>
    """, unsafe_allow_html=True)

# ====================== SESSION STATE ======================
if "messages" not in st.session_state:
    st.session_state.messages = []

# ====================== ÜST PANEL ======================
st.markdown(f"## 🎙️ FASLI MUHABBET <span style='color:red; font-size:15px;'>● CANLI</span>", unsafe_allow_html=True)
st.caption(f"📍 Bursa Stüdyoları | Popüler Dilara Ses Motoru Aktif")

# ====================== SOHBET AKIŞI ======================
for i, msg in enumerate(st.session_state.messages):
    if msg["role"] == "user":
        st.markdown(f'<div class="patron-card">🤵 <b>Patron Kenan:</b> {msg["content"]}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f"""
            <div class="dilay-card">
                <b style="color:#ff007f;">💖 DİLAY:</b><br>{msg['content']}
            </div>
        """, unsafe_allow_html=True)
        
        # Ses verisi varsa oynatıcıyı göster
        if msg.get("audio"):
            if i == len(st.session_state.messages) - 1:
                autoplay_audio(msg["audio"]) # En son mesajı otomatik oynat
            else:
                st.audio(msg["audio"], format="audio/mp3") # Eskileri manuel bırak

# ====================== MESAJ GİRİŞİ ======================
if prompt := st.chat_input("Patron'um, gönlünden ne geçiyorsa söyle..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    with st.spinner("🎤 Dilay yayına bağlanıyor..."):
        try:
            # 1. Metin (Groq)
            sys_prompt = "Sen Dilay'sın. Faslı Muhabbet'in neşeli, işveli radyo sunucususun. Patronun Kenan'a sevgiyle hitap et."
            history = [{"role": "system", "content": sys_prompt}] + st.session_state.messages[-8:]
            res = client.chat.completions.create(model="llama-3.3-70b-versatile", messages=history).choices[0].message.content

            # 2. Ses (Edge-TTS)
            audio_data = asyncio.run(get_voice_bytes(res))

            # 3. Kaydet
            st.session_state.messages.append({"role": "assistant", "content": res, "audio": audio_data})
            st.rerun()

        except Exception as e:
            st.error(f"Hata oluştu: {e}")

# ====================== REJİ ======================
with st.sidebar:
    st.title("🎚️ Reji Masası")
    if st.button("🗑️ Yayını Sıfırla"):
        st.session_state.messages = []
        st.rerun()
    st.write("---")
    st.write("📢 **Ses Duyulmuyor mu?**")
    st.caption("1. Sayfada herhangi bir yere tıklayın.\n2. Tarayıcı sesinin açık olduğundan emin olun.\n3. Mobil cihazda 'Sessiz Mod'u kapatın.")
