import streamlit as st
from groq import Groq
import asyncio
import edge_tts
import time
from datetime import datetime

st.set_page_config(
    page_title="Faslı Muhabbet v11.1 - Sarmal İkili Yayın",
    layout="wide",
    page_icon="🎙️"
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
HOSTS = {
    "Dilay 💖": {"voice": "tr-TR-EmelNeural", "color": "#ff1493", "persona": "İşveli, neşeli, cilveli, Mert'e laf atan, coşkulu kadın sunucu."},
    "Mert 🎙️": {"voice": "tr-TR-AhmetNeural", "color": "#00d4ff", "persona": "Ağırbaşlı, esprili, Dilay'ın paslarını gole çeviren, samimi erkek sunucu."}
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
    .dilay-card { background: linear-gradient(145deg, #2a0f4a, #140525); border-left: 10px solid #ff1493; 
                  border-radius: 22px; padding: 25px; margin: 18px 0; box-shadow: 0 10px 30px rgba(255,20,147,0.25); }
    .mert-card { background: linear-gradient(145deg, #0f2a4a, #051428); border-left: 10px solid #00d4ff; 
                 border-radius: 22px; padding: 25px; margin: 18px 0; box-shadow: 0 10px 30px rgba(0,212,255,0.25); }
    .patron-card { background: rgba(0, 255, 157, 0.1); border-right: 8px solid #00ff9d; 
                   padding: 18px; border-radius: 16px; margin: 15px 0; text-align: right; }
    .live-badge { color: #ff0000; font-weight: 900; animation: blink 1.4s infinite; }
    @keyframes blink { 50% { opacity: 0.35; } }
    </style>
    """, unsafe_allow_html=True)

st.markdown(f"<h1 style='text-align: center; color: #ff1493;'>🎙️ FASLI MUHABBET <span class='live-badge'>● SARMAL CANLI YAYIN v11.1</span></h1>", unsafe_allow_html=True)

# ====================== SOHBET GÖSTERİM ======================
for msg in st.session_state.history:
    if msg["role"] == "user":
        st.markdown(f'<div class="patron-card"><b>🤵 Patron:</b> {msg["content"]}</div>', unsafe_allow_html=True)
    else:
        card_class = "dilay-card" if "Dilay" in msg["host"] else "mert-card"
        color = HOSTS[msg["host"]]["color"] if msg["host"] in HOSTS else "#ffffff"
        
        st.markdown(f"""
            <div class="{card_class}">
                <span style="color:{color}; font-weight:900; font-size:1.6rem;">{msg['host']}</span><br><br>
                <div style="line-height:1.75;">{msg['content']}</div>
            </div>
            """, unsafe_allow_html=True)
        
        if msg.get("audio"):
            try:
                st.audio(msg["audio"], format="audio/mpeg", autoplay=True)
            except:
                pass

# ====================== PROMPT ======================
def get_system_prompt(speaker, partner):
    return f"""Sen {speaker}. {HOSTS[speaker]['persona']}
Partnerin {partner} ile kapışmalı, atışmalı, eğlenceli bir radyo muhabbetindesin.
Birbirinize laf yetiştirin, soru sorun, pas atın, muhabbeti asla koparmayın.
Kısa, akıcı ve doğal konuş. Radyo yayını gibi olsun."""

# ====================== ANA YAYIN AKIŞI ======================
if prompt := st.chat_input("Patronum, konuyu ver... Onlar kendi aralarında sarmal muhabbet etsin..."):
    st.session_state.history.append({"role": "user", "content": prompt})
    
    with st.spinner("🎙️ Yayın başlıyor... Dilay ve Mert yayına giriyor ❤️"):
        speakers = ["Dilay 💖", "Mert 🎙️"]
        
        # Konu geldiyse tur başlat
        for _ in range(6):  # 6 tur = 3 Dilay + 3 Mert (istediğin kadar artırabilirsin)
            # Son konuşanı bul, diğerine geç
            if st.session_state.last_speaker is None:
                speaker = speakers[0]
            else:
                speaker = speakers[1] if st.session_state.last_speaker == speakers[0] else speakers[0]
            
            st.session_state.last_speaker = speaker
            partner = speakers[1] if speaker == speakers[0] else speakers[0]
            
            try:
                messages = [
                    {"role": "system", "content": get_system_prompt(speaker, partner)}
                ]
                # Son konuşmaları hafızaya ekle
                for h in st.session_state.history[-8:]:
                    if h["role"] == "assistant":
                        messages.append({"role": "assistant", "content": h["content"]})
                    elif h["role"] == "user":
                        messages.append({"role": "user", "content": h["content"]})

                response = client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=messages,
                    temperature=0.92,
                    max_tokens=680
                ).choices[0].message.content

            except Exception:
                response = f"{speaker.split()[0]}, canım, ufak bir takılma oldu ama seni bekletmem. Devam edelim mi?"

            # Ses üret
            audio = run_async_safe(generate_audio(response, HOSTS[speaker]["voice"]))

            st.session_state.history.append({
                "role": "assistant",
                "host": speaker,
                "content": response,
                "audio": audio
            })
            
            time.sleep(0.7)   # Doğal geçiş için kısa bekleme
            st.rerun()        # Her konuşmadan sonra ekranı yenile → ses sırayla çalsın

# ====================== REJİ ======================
with st.sidebar:
    st.title("🎚️ Reji Odası")
    if st.button("🔴 Yayını Durdur ve Temizle"):
        st.session_state.history = []
        st.session_state.last_speaker = None
        st.rerun()
    
    st.info("""
    ✨ Nasıl Çalışır?
    • Patron konu verir
    • Dilay ve Mert sırayla konuşur
    • Biri bitince diğeri devam eder
    • Tam sarmal, kapışmalı muhabbet!
    """)
    
    st.caption("Kurumsal Sesler:\n• Dilay → EmelNeural\n• Mert → AhmetNeural")

st.caption("Faslı Muhabbet v11.1 • Sarmal İkili Yayın • Kenan ile geliştiriyoruz 💖🎙️")