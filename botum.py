import streamlit as st
from groq import Groq
import os
import random
import asyncio
import edge_tts
import time

# ====================== 1. BAŞLATMA & AYARLAR ======================
st.set_page_config(page_title="Aşk-ı Muhabbet v12.0", layout="wide", page_icon="🎙️")

if "GROQ_API_KEY" not in st.secrets:
    st.error("GROQ_API_KEY bulunamadı!")
    st.stop()

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# ====================== 2. SES ÜRETİM MOTORU ======================
async def get_voice_bytes(text, voice):
    """Metni sese çevirir ve bytes olarak döndürür."""
    try:
        communicate = edge_tts.Communicate(text, voice)
        audio_data = b""
        async for chunk in communicate.stream():
            if chunk["type"] == "audio":
                audio_data += chunk["data"]
        return audio_data
    except Exception as e:
        print(f"Ses üretim hatası: {e}")
        return None

# ====================== 3. TASARIM (CSS) ======================
st.markdown("""
    <style>
    .stApp { background-color: #05050a; color: #ffffff; }
    .host-card { padding: 20px; border-radius: 15px; margin-bottom: 15px; border-left: 10px solid; }
    .dilay-theme { background: #2a0a25; border-color: #ff1493; }
    .mert-theme { background: #0a252a; border-color: #00d4ff; }
    .patron-bubble { background: rgba(0, 255, 157, 0.1); border-right: 5px solid #00ff9d; padding: 12px; border-radius: 10px; margin: 10px 0; text-align: right; }
    .live-text { color: red; font-weight: bold; animation: blinker 1.2s linear infinite; }
    @keyframes blinker { 50% { opacity: 0; } }
    </style>
    """, unsafe_allow_html=True)

# ====================== 4. REJİ VE PANEL ======================
with st.sidebar:
    st.title("🎚️ REJİ MASASI")
    secilen_sunucu = st.radio("Mikrofon Kimde?", ["Dilay 💖", "Mert 🎙️"])
    yayin_enerjisi = st.select_slider("Enerji:", ["Sakin", "Duygusal", "Standart", "Coşkulu", "Muzip"])
    if st.button("Yayını Sıfırla"):
        st.session_state.chat_history = []
        st.rerun()

st.markdown(f"<h1>🎙️ AŞK-I MUHABBET <span class='live-text'>● CANLI</span></h1>", unsafe_allow_html=True)

# ====================== 5. SOHBET VE SES AKIŞI ======================
for i, chat in enumerate(st.session_state.chat_history):
    if chat["role"] == "user":
        st.markdown(f'<div class="patron-bubble"><b>Patron:</b> {chat["content"]}</div>', unsafe_allow_html=True)
    else:
        tema = "dilay-theme" if chat["host"] == "Dilay 💖" else "mert-theme"
        st.markdown(f"""
            <div class="host-card {tema}">
                <b>{chat['host']}</b><br>{chat['content']}
            </div>
        """, unsafe_allow_html=True)
        
        # SES OYNATICI (TypeError önleyici kontrol)
        if chat.get("audio") is not None:
            is_latest = (i == len(st.session_state.chat_history) - 1)
            # Her audio nesnesine benzersiz, zamana bağlı bir ID veriyoruz
            st.audio(chat["audio"], format="audio/wav", autoplay=is_latest, key=f"snd_{i}_{hash(chat['content'])}")

# ====================== 6. AI VE SES ÜRETİMİ ======================
personalar = {
    "Dilay 💖": {"prompt": f"Sen Dilay'sın. Neşeli ve cilvelisin. Modun: {yayin_enerjisi}", "voice": "tr-TR-EmelNeural"},
    "Mert 🎙️": {"prompt": f"Sen Mert'sin. Ağırbaşlı ve samimisin. Modun: {yayin_enerjisi}", "voice": "tr-TR-AhmetNeural"}
}

if prompt := st.chat_input("Patron, yayına bağlan..."):
    st.session_state.chat_history.append({"role": "user", "content": prompt})
    
    with st.spinner("🎙️ Yayın hazırlanıyor..."):
        # 1. Groq'tan Metin Al
        messages = [{"role": "system", "content": personalar[secilen_sunucu]["prompt"]}] + \
                   [{"role": m["role"], "content": m["content"]} for m in st.session_state.chat_history[-6:]]
        
        comp = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=messages,
            temperature=0.8
        )
        response_text = comp.choices[0].message.content

        # 2. Ses Üret (Async yönetimi)
        try:
            audio_bytes = asyncio.run(get_voice_bytes(response_text, personalar[secilen_sunucu]["voice"]))
        except:
            # Eğer asyncio.run hata verirse (bazı Streamlit sürümlerinde olur)
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            audio_bytes = loop.run_until_complete(get_voice_bytes(response_text, personalar[secilen_sunucu]["voice"]))

        # 3. Geçmişe Ekle (Sadece ses varsa audio ekle)
        st.session_state.chat_history.append({
            "role": "assistant",
            "host": secilen_sunucu,
            "content": response_text,
            "audio": audio_bytes if audio_bytes else None
        })
        
        st.rerun()
