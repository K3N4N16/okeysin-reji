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
st.set_page_config(page_title="Faslı Muhabbet v9.5", layout="wide", page_icon="🎙️")

if "GROQ_API_KEY" not in st.secrets:
    st.error("⚠️ GROQ API Key eksik! Lütfen Streamlit Secrets'a ekleyin.")
    st.stop()

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

# ====================== SES MOTORU (KESİN ÇÖZÜM) ======================
async def generate_voice_edge(text: str):
    """Metni temizler ve asenkron olarak sesi üretir"""
    try:
        # AI sesini bozan karakterleri (emoji, yıldız vs.) tamamen temizle
        clean_text = re.sub(r'[^\w\s\d,?.!]', '', text).strip()
        if not clean_text:
            return None

        # Popüler ve stabil: Dilara
        voice = "tr-TR-DilaraNeural"
        communicate = edge_tts.Communicate(clean_text, voice, rate="+5%")
        
        audio_bytes = b""
        async for chunk in communicate.stream():
            if chunk["type"] == "audio":
                audio_bytes += chunk["data"]
        
        return audio_bytes if audio_bytes else None
    except Exception as e:
        st.error(f"Ses motoru hatası: {e}")
        return None

# ====================== MODERN TASARIM (CSS) ======================
st.markdown("""
    <style>
    .stApp { background-color: #050505; color: #ffffff; }
    .dilay-bubble {
        background: linear-gradient(135deg, #2b0040 0%, #000000 100%);
        border-left: 6px solid #ff007f;
        padding: 20px; border-radius: 15px; margin: 10px 0;
        box-shadow: 0 4px 15px rgba(255,0,127,0.3);
    }
    .patron-bubble {
        background: #111; border-right: 4px solid #00f2fe;
        padding: 12px; border-radius: 10px; text-align: right; margin: 10px 0;
    }
    </style>
    """, unsafe_allow_html=True)

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# ====================== EKRAN AKIŞI ======================
st.markdown("## 🎙️ FASLI MUHABBET <span style='color:red; font-size:14px;'>● CANLI</span>", unsafe_allow_html=True)

for i, msg in enumerate(st.session_state.chat_history):
    if msg["role"] == "user":
        st.markdown(f'<div class="patron-bubble">🤵 <b>Patron Kenan:</b> {msg["content"]}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="dilay-bubble">💖 <b>DİLAY:</b><br>{msg["content"]}</div>', unsafe_allow_html=True)
        if msg.get("audio_b64"):
            # HTML5 Audio Player - Manuel buton her zaman görünür
            audio_html = f"""
                <audio controls style="width: 100%; border-radius: 10px; margin-top: 5px;">
                    <source src="data:audio/mp3;base64,{msg['audio_b64']}" type="audio/mp3">
                </audio>
            """
            st.markdown(audio_html, unsafe_allow_html=True)

# ====================== YENİ MESAJ İŞLEME ======================
if prompt := st.chat_input("Yayına bağlan patron..."):
    st.session_state.chat_history.append({"role": "user", "content": prompt})
    
    with st.spinner("🎧 Dilay hazırlanıyor..."):
        try:
            # 1. Metin (Groq - Llama 3.3)
            sys_msg = "Sen Dilay'sın. Samimi, neşeli, işveli radyo sunucususun. Patronun Kenan'a sevgiyle hitap et."
            messages = [{"role": "system", "content": sys_msg}] + st.session_state.chat_history[-6:]
            response = client.chat.completions.create(model="llama-3.3-70b-versatile", messages=messages).choices[0].message.content
            
            # 2. Ses Üretimi (Asyncio Safe Loop)
            try:
                loop = asyncio.get_running_loop()
            except RuntimeError:
                loop = asyncio.new_event_loop()
                asyncio.set_event_loop(loop)
            
            # Sesi üret ve Base64'e çevir (Oynatıcı için şart)
            audio_data = loop.run_until_complete(generate_voice_edge(response))
            
            audio_b64 = None
            if audio_data:
                audio_b64 = base64.b64encode(audio_data).decode()
            
            # 3. Kaydet ve Yenile
            st.session_state.chat_history.append({
                "role": "assistant", 
                "content": response, 
                "audio_b64": audio_b64
            })
            st.rerun()

        except Exception as e:
            st.error(f"Yayında Parazit Var: {e}")

with st.sidebar:
    st.header("🎚️ Reji")
    if st.button("🗑️ Yayını Sıfırla"):
        st.session_state.chat_history = []
        st.rerun()
    st.divider()
    st.caption("Faslı Muhabbet v9.5 | Ses: Dilara AI")
