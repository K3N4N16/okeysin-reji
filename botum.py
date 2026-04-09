import streamlit as st
from groq import Groq
import asyncio
import edge_tts
import time
from datetime import datetime

st.set_page_config(
    page_title="Faslı Muhabbet v9.8",
    layout="wide",
    page_icon="🎙️",
    initial_sidebar_state="expanded"
)

if "GROQ_API_KEY" not in st.secrets:
    st.error("⚠️ GROQ API Key eksik! Secrets.toml dosyasına ekle.")
    st.stop()

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

if "history" not in st.session_state:
    st.session_state.history = []
if "last_speaker" not in st.session_state:
    st.session_state.last_speaker = None

# ====================== KURUMSAL SESLER ======================
VOICES = {
    "Dilay 💖": "tr-TR-EmelNeural",   # Cilveli, sıcak bayan sesi
    "Mert 🎙️": "tr-TR-AhmetNeural"    # Samimi, ağırbaşlı erkek sesi
}

async def produce_voice(text: str, voice: str):
    if not text or len(text.strip()) < 3:
        return None
    try:
        communicate = edge_tts.Communicate(text, voice)
        audio_data = b""
        async for chunk in communicate.stream():
            if chunk["type"] == "audio":
                audio_data += chunk["data"]
        return audio_data
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

# ====================== CSS ======================
st.markdown("""
    <style>
    .stApp { background: #05050f; color: #f0f0f0; }
    .dilay-card { background: linear-gradient(145deg, #2a0f4a, #140525); border-left: 8px solid #ff1493; 
                  border-radius: 20px; padding: 28px; margin: 20px 0; box-shadow: 0 15px 40px rgba(255,20,147,0.3); }
    .mert-card { background: linear-gradient(145deg, #0f2a4a, #051428); border-left: 8px solid #00d4ff; 
                 border-radius: 20px; padding: 28px; margin: 20px 0; box-shadow: 0 15px 40px rgba(0,212,255,0.3); }
    .patron-card { background: rgba(0, 255, 157, 0.08); border-right: 6px solid #00ff9d; 
                   padding: 18px; border-radius: 15px; margin: 15px 0; text-align: right; }
    .live-badge { color: #ff0000; font-weight: 900; animation: blink 1.3s infinite; }
    @keyframes blink { 50% { opacity: 0.4; } }
    </style>
    """, unsafe_allow_html=True)

# ====================== ÜST PANEL ======================
col1, col2 = st.columns([3, 1])
with col1:
    st.markdown(f"# 🎙️ FASLI MUHABBET <span class='live-badge'>● CANLI</span>", unsafe_allow_html=True)
with col2:
    st.metric("Canlı Dinleyici", "7,892")

# ====================== SOHBET ALANI ======================
for i, msg in enumerate(st.session_state.history):
    if msg["role"] == "user":
        st.markdown(f'<div class="patron-card"><b>🤵 Patron:</b> {msg["content"]}</div>', unsafe_allow_html=True)
    else:
        card_class = "dilay-card" if "Dilay" in msg["host"] else "mert-card"
        st.markdown(f"""
            <div class="{card_class}">
                <span style="color:#ff69b4; font-weight:900; font-size:1.55rem;">{msg['host']}</span><br>
                <div style="margin-top:15px; line-height:1.7;">{msg['content']}</div>
            </div>
            """, unsafe_allow_html=True)
        
        if msg.get("audio"):
            try:
                st.audio(msg["audio"], format="audio/mpeg", autoplay=True)
            except:
                pass

# ====================== PROMPT'LAR ======================
def get_prompt(host):
    if "Dilay" in host:
        return """Sen Dilay'sın. Faslı Muhabbet'in kıpır kıpır, işveli, sıcak ve cilveli kadın sunucususun. 
        Patron'a "Canım Patronum", "Ah be Patron’um", "Sevgilim" diye hitap et. 
        Konuşmalarında Mert'le kapışmalı, atışmalı, eğlenceli muhabbet et."""
    else:
        return """Sen Mert'sin. Faslı Muhabbet'in samimi, ağırbaşlı ve esprili erkek sunucususun. 
        Dilay'la kapışmalı, atışmalı, birbirinize laf yetiştirerek eğlenceli muhabbet edin."""

# ====================== YAYIN AKIŞI ======================
if prompt := st.chat_input("Patron'um, gönlünden ne geçiyorsa söyle..."):
    st.session_state.history.append({"role": "user", "content": prompt})
    
    with st.spinner("🎙️ Mikrofonlar açılıyor... Dilay ve Mert yayına giriyor ❤️"):
        speakers = ["Dilay 💖", "Mert 🎙️"]
        start_idx = 0 if st.session_state.last_speaker is None else (speakers.index(st.session_state.last_speaker) + 1) % 2
        
        for i in range(2):  # İkisi de sırayla konuşsun
            speaker = speakers[(start_idx + i) % 2]
            st.session_state.last_speaker = speaker
            
            try:
                messages = [{"role": "system", "content": get_prompt(speaker)}] + \
                           [{"role": m["role"], "content": m["content"]} for m in st.session_state.history[-12:]]
                
                response = client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=messages,
                    temperature=0.92,
                    max_tokens=650
                ).choices[0].message.content
            except:
                response = f"{speaker.split()[0]}, ufak bir takılma oldu ama hemen toparladım. Devam edelim mi sevgilim?"

            # Kurumsal ses üret
            voice_name = VOICES[speaker]
            audio_bytes = run_async_safe(produce_voice(response, voice_name))

            st.session_state.history.append({
                "role": "assistant",
                "host": speaker,
                "content": response,
                "audio": audio_bytes
            })
            
            time.sleep(0.6)  # Doğal geçiş hissi
            st.rerun()

# ====================== SIDEBAR ======================
with st.sidebar:
    st.title("🎚️ Reji Masası")
    if st.button("🗑️ Sohbeti Temizle"):
        st.session_state.history = []
        st.session_state.last_speaker = None
        st.rerun()
    st.caption("Kurumsal Sesler:\n• Dilay → EmelNeural (Bayan)\n• Mert → AhmetNeural (Erkek)")

st.caption("Faslı Muhabbet v9.8 • Sarmal İkili Diyalog • Gerçek Zamanlı Kurumsal Ses 💖🎙️")