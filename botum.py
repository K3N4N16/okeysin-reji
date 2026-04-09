import streamlit as st
from groq import Groq
import asyncio
import edge_tts
import time
from datetime import datetime
import random

st.set_page_config(
    page_title="Faslı Muhabbet v12.0 - Üçlü Sarmal Yayın",
    layout="wide",
    page_icon="🎙️"
)

if "GROQ_API_KEY" not in st.secrets:
    st.error("⚠️ GROQ API Key eksik! Secrets.toml dosyasına ekleyin.")
    st.stop()

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

if "history" not in st.session_state:
    st.session_state.history = []
if "last_speaker" not in st.session_state:
    st.session_state.last_speaker = None
if "ses_acik" not in st.session_state:
    st.session_state.ses_acik = True

# ====================== ÜÇ SUNUCU ======================
SUNUCULAR = {
    "Nilay 💖": {
        "voice": "tr-TR-EmelNeural",
        "color": "#ff1493",
        "persona": "Cilveli, nazlı, işveli, şiirsel konuşan, duygusal ve neşeli kadın sunucu. Kerem ve Mert'e nazlı nazlı laf atar."
    },
    "Kerem 🎙️": {
        "voice": "tr-TR-AhmetNeural",
        "color": "#00d4ff",
        "persona": "Samimi, esprili, ağırbaşlı, genel kültürü yüksek, şarkı yorumları yapan erkek sunucu."
    },
    "Mert 🎙️": {
        "voice": "tr-TR-AhmetNeural",
        "color": "#00ff9d",
        "persona": "Derin, şairane, felsefi, şiir okuyan, duygusal ve zeki erkek sunucu."
    }
}

async def generate_audio(text: str, voice: str):
    try:
        communicate = edge_tts.Communicate(text, voice, rate="+3%")
        audio_bytes = b""
        async for chunk in communicate.stream():
            if chunk["type"] == "audio":
                audio_bytes += chunk["data"]
        return audio_bytes
    except:
        return None

def run_async_safe(coro):
    try:
        return asyncio.run(coro)
    except:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        try:
            return loop.run_until_complete(coro)
        except:
            return None

# ====================== TASARIM ======================
st.markdown("""
    <style>
    .stApp { background: #05050f; color: #f0f0f0; }
    .nilay-card { background: linear-gradient(145deg, #2a0f4a, #140525); border-left: 10px solid #ff1493; border-radius: 22px; padding: 25px; margin: 18px 0; }
    .kerem-card { background: linear-gradient(145deg, #0f2a4a, #051428); border-left: 10px solid #00d4ff; border-radius: 22px; padding: 25px; margin: 18px 0; }
    .mert-card  { background: linear-gradient(145deg, #0f4a2a, #051f14); border-left: 10px solid #00ff9d; border-radius: 22px; padding: 25px; margin: 18px 0; }
    .patron-card { background: rgba(0, 255, 157, 0.1); border-right: 8px solid #00ff9d; padding: 18px; border-radius: 16px; margin: 15px 0; text-align: right; }
    .live-badge { color: #ff0000; font-weight: 900; animation: blink 1.4s infinite; }
    @keyframes blink { 50% { opacity: 0.35; } }
    </style>
    """, unsafe_allow_html=True)

st.markdown(f"<h1 style='text-align: center; color: #ff1493;'>🎙️ FASLI MUHABBET <span class='live-badge'>● ÜÇLÜ SARMAL v12.0</span></h1>", unsafe_allow_html=True)

# ====================== SOHBET GÖSTERİM ======================
for msg in st.session_state.history:
    if msg["role"] == "user":
        st.markdown(f'<div class="patron-card"><b>🤵 Patron:</b> {msg["content"]}</div>', unsafe_allow_html=True)
    else:
        if "Nilay" in msg["host"]:
            card_class = "nilay-card"
        elif "Kerem" in msg["host"]:
            card_class = "kerem-card"
        else:
            card_class = "mert-card"
        
        color = SUNUCULAR[msg["host"]]["color"]
        st.markdown(f"""
            <div class="{card_class}">
                <span style="color:{color}; font-weight:900; font-size:1.6rem;">{msg['host']}</span><br><br>
                <div style="line-height:1.75;">{msg['content']}</div>
            </div>
            """, unsafe_allow_html=True)
        
        if st.session_state.ses_acik and msg.get("audio"):
            try:
                st.audio(msg["audio"], format="audio/mpeg", autoplay=True)
            except:
                pass

# ====================== SİSTEM PROMPT ======================
def get_system_prompt(speaker, next_speaker):
    return f"""Sen {speaker}'sın. Faslı Muhabbet'in çok yetenekli, genel kültürü yüksek, şiirsel ve profesyonel sunucususun.
Partnerlerin {next_speaker} ve diğer sunucularla sarmal, kapışmalı, eğlenceli bir radyo programı yapıyorsun.
Şarkı önerileri yap, şarkılar üzerine derin yorumlar yap, şiir oku, nazlı ve cilveli konuş, espri yap.
Muhabbeti asla koparma, birbirinize güzel paslar atın. Radyo akışını çok profesyonel ve sıcak tut."""

# ====================== YAYIN AKIŞI ======================
if prompt := st.chat_input("Patronum, bu akşam ne muhabbeti açalım? Konuyu söyle, onlar sarmala girsin..."):
    st.session_state.history.append({"role": "user", "content": prompt})
    
    with st.spinner("🎙️ Stüdyo ışıkları yanıyor... Nilay, Kerem ve Mert yayına giriyor ❤️"):
        speakers_order = ["Nilay 💖", "Kerem 🎙️", "Mert 🎙️"]
        
        for _ in range(9):  # 9 tur = 3 tur herkes konuşsun (daha uzun akış için artırabilirsin)
            # Sırayı belirle
            if st.session_state.last_speaker is None:
                speaker = speakers_order[0]
            else:
                idx = speakers_order.index(st.session_state.last_speaker)
                speaker = speakers_order[(idx + 1) % 3]
            
            st.session_state.last_speaker = speaker
            next_speaker = speakers_order[(speakers_order.index(speaker) + 1) % 3]
            
            try:
                messages = [{"role": "system", "content": get_system_prompt(speaker, next_speaker)}]
                for h in st.session_state.history[-12:]:
                    role = "user" if h["role"] == "user" else "assistant"
                    messages.append({"role": role, "content": h["content"]})

                response = client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=messages,
                    temperature=0.91,
                    max_tokens=750
                ).choices[0].message.content

            except Exception:
                response = f"{speaker.split()[0]}, canım, teknik ufak bir takılma oldu ama hemen toparlıyoruz. Devam edelim mi?"

            # Ses üretimi
            audio = None
            if st.session_state.ses_acik:
                audio = run_async_safe(generate_audio(response, SUNUCULAR[speaker]["voice"]))

            st.session_state.history.append({
                "role": "assistant",
                "host": speaker,
                "content": response,
                "audio": audio
            })
            
            time.sleep(0.9)  # Daha doğal radyo geçişi
            st.rerun()

# ====================== REJİ MASASI ======================
with st.sidebar:
    st.title("🎚️ Reji Odası")
    st.session_state.ses_acik = st.toggle("🔊 Sesleri Aç (Otomatik Çalsın)", value=st.session_state.ses_acik)
    
    if st.button("🔴 Yayını Durdur ve Temizle"):
        st.session_state.history = []
        st.session_state.last_speaker = None
        st.rerun()
    
    st.info("""
    ✨ Bu Akışta:
    • Nilay, Kerem ve Mert sırayla konuşur
    • Şarkı önerileri + yorumlar
    • Şiir, espri, cilveli paslaşmalar
    • Tam sarmal radyo programı
    """)
    
    st.caption("Sesler:\n• Nilay → EmelNeural\n• Kerem & Mert → AhmetNeural")

st.caption("Faslı Muhabbet v12.0 • Üçlü Sarmal Yayın • Kenan ile birlikte geliştiriyoruz 💖🎙️")