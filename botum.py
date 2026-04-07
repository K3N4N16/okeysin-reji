import streamlit as st
from groq import Groq
import edge_tts
import asyncio
import io
import re
import base64
from datetime import datetime

# ====================== SAYFA AYARLARI ======================
st.set_page_config(page_title="Faslı Muhabbet v8.0", layout="wide", page_icon="🎙️")

if "GROQ_API_KEY" not in st.secrets:
    st.error("⚠️ GROQ API Key eksik!")
    st.stop()

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

# ====================== SES ÜRETİMİ (EN STABİL YÖNTEM) ======================
def generate_voice_sync(text):
    """Asenkron yapıyı senkronize ederek ses üretir - Kütüphane hatasını önler"""
    async def amain():
        # AI sesini bozan karakterleri temizle
        clean_text = re.sub(r'[*_#~>]', '', text).strip()
        if not clean_text:
            return None
        
        # En popüler Türkçe ses: Dilara
        communicate = edge_tts.Communicate(clean_text, "tr-TR-DilaraNeural", rate="+7%")
        audio_bytes = b""
        async for chunk in communicate.stream():
            if chunk["type"] == "audio":
                audio_bytes += chunk["data"]
        return audio_bytes

    # Streamlit döngüsü içinde asenkronu çalıştırmanın en güvenli yolu
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        return loop.run_until_complete(amain())
    finally:
        loop.close()

# ====================== UI & CSS ======================
st.markdown("""
    <style>
    .stApp { background: #0a0a0a; color: white; }
    .dilay-msg {
        background: #1e0035; border-left: 5px solid #ff007f;
        padding: 20px; border-radius: 10px; margin: 10px 0;
    }
    .audio-player { width: 100%; margin-top: 10px; }
    </style>
    """, unsafe_allow_html=True)

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# ====================== SOHBET EKRANI ======================
st.title("🎙️ FASLI MUHABBET")

for i, msg in enumerate(st.session_state.chat_history):
    if msg["role"] == "user":
        st.write(f"🤵 **Patron Kenan:** {msg['content']}")
    else:
        st.markdown(f'<div class="dilay-msg">💖 <b>DİLAY:</b><br>{msg["content"]}</div>', unsafe_allow_html=True)
        if msg.get("audio_b64"):
            # HTML5 Audio Player - Her koşulda görünür ve manuel basılabilir
            audio_html = f"""
                <audio controls class="audio-player">
                    <source src="data:audio/mp3;base64,{msg['audio_b64']}" type="audio/mp3">
                </audio>
                """
            st.markdown(audio_html, unsafe_allow_html=True)

# ====================== AKIŞ ======================
if prompt := st.chat_input("Mesajını yaz patron..."):
    st.session_state.chat_history.append({"role": "user", "content": prompt})
    
    with st.spinner("Dilay konuşuyor..."):
        # 1. Metin Üret
        sys_msg = "Sen Dilay'sın. Neşeli, samimi radyo sunucususun. Patronun Kenan'a hitap et."
        messages = [{"role": "system", "content": sys_msg}] + st.session_state.chat_history[-5:]
        response = client.chat.completions.create(model="llama-3.3-70b-versatile", messages=messages).choices[0].message.content
        
        # 2. Ses Üret ve Base64'e çevir (Oynatıcıda görünmesi için şart)
        audio_data = generate_voice_sync(response)
        audio_b64 = base64.b64encode(audio_data).decode() if audio_data else None
        
        # 3. Kaydet ve Yenile
        st.session_state.chat_history.append({
            "role": "assistant", 
            "content": response, 
            "audio_b64": audio_b64
        })
        st.rerun()

with st.sidebar:
    if st.button("Sohbeti Temizle"):
        st.session_state.chat_history = []
        st.rerun()
