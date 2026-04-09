import streamlit as st
from groq import Groq
import asyncio
import edge_tts
import time
from datetime import datetime

st.set_page_config(
    page_title="Faslı Muhabbet v11.2 - Nilay & Kerem Sarmal",
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
if "ses_acik" not in st.session_state:
    st.session_state.ses_acik = True

# ====================== SUNUCULAR (Kurumsal Sesler) ======================
SUNUCULAR = {
    "Nilay 💖": {"voice": "tr-TR-EmelNeural", "color": "#ff1493", "persona": "İşveli, neşeli, cilveli, Kerem'e laf atan, coşkulu kadın sunucu."},
    "Kerem 🎙️": {"voice": "tr-TR-AhmetNeural", "color": "#00d4ff", "persona": "Samimi, esprili, ağırbaşlı, Nilay'ın paslarını gole çeviren erkek sunucu."}
}

async def generate_audio(text: str, voice: str):
    try:
        communicate = edge_tts.Communicate(text, voice, rate="+4%")
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
    .nilay-card { background: linear-gradient(145deg, #2a0f4a, #140525); border-left: 10px solid #ff1493; 
                  border-radius: 22px; padding: 25px; margin: 18px 0; box-shadow: 0 10px 30px rgba(255,20,147,0.25); }
    .kerem-card { background: linear-gradient(145deg, #0f2a4a, #051428); border-left: 10px solid #00d4ff; 
                  border-radius: 22px; padding: 25px; margin: 18px 0; box-shadow: 0 10px 30px rgba(0,212,255,0.25); }
    .patron-card { background: rgba(0, 255, 157, 0.1); border-right: 8px solid #00ff9d; 
                   padding: 18px; border-radius: 16px; margin: 15px 0; text-align: right; }
    .live-badge { color: #ff0000; font-weight: 900; animation: blink 1.4s infinite; }
    @keyframes blink { 50% { opacity: 0.35; } }
    </style>
    """, unsafe_allow_html=True)

st.markdown(f"<h1 style='text-align: center; color: #ff1493;'>🎙️ FASLI MUHABBET <span class='live-badge'>● NILAY & KEREM SARMAL v11.2</span></h1>", unsafe_allow_html=True)

# ====================== SOHBET GÖSTERİM ======================
for msg in st.session_state.history:
    if msg["role"] == "user":
        st.markdown(f'<div class="patron-card"><b>🤵 Patron:</b> {msg["content"]}</div>', unsafe_allow_html=True)
    else:
        card_class = "nilay-card" if "Nilay" in msg["host"] else "kerem-card"
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

# ====================== PROMPT ======================
def get_system_prompt(speaker, partner):
    return f"""Sen {speaker}. {SUNUCULAR[speaker]['persona']}
Partnerin {partner} ile kapışmalı, atışmalı, eğlenceli bir radyo muhabbetindesin.
Birbirinize soru sorun, laf yetiştirin, pas atın, muhabbeti sıcak ve akıcı tutun.
Kısa cümleler kur, doğal konuş."""

# ====================== YAYIN AKIŞI ======================
if prompt := st.chat_input("Patronum, konuyu veya mesajı ver... Nilay ve Kerem sarmal muhabbete başlasın..."):
    st.session_state.history.append({"role": "user", "content": prompt})
    
    with st.spinner("🎙️ Mikrofonlar açılıyor... Nilay ve Kerem yayına giriyor ❤️"):
        speakers = ["Nilay 💖", "Kerem 🎙️"]
        
        for _ in range(6):  # 6 tur (3 Nilay + 3 Kerem) - Daha fazla istersen artır
            # Sırayı belirle
            if st.session_state.last_speaker is None:
                speaker = speakers[0]
            else:
                speaker = speakers[1] if st.session_state.last_speaker == speakers[0] else speakers[0]
            
            st.session_state.last_speaker = speaker
            partner = speakers[1] if speaker == speakers[0] else speakers[0]
            
            try:
                messages = [{"role": "system", "content": get_system_prompt(speaker, partner)}]
                for h in st.session_state.history[-10:]:
                    if h["role"] == "user":
                        messages.append({"role": "user", "content": h["content"]})
                    elif h["role"] == "assistant":
                        messages.append({"role": "assistant", "content": h["content"]})

                response = client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=messages,
                    temperature=0.93,
                    max_tokens=700
                ).choices[0].message.content

            except Exception:
                response = f"{speaker.split()[0]}, canım, ufak bir takılma oldu ama hemen devam ediyoruz!"

            # Ses üret (sadece ses açıksa)
            audio = None
            if st.session_state.ses_acik:
                audio = run_async_safe(generate_audio(response, SUNUCULAR[speaker]["voice"]))

            st.session_state.history.append({
                "role": "assistant",
                "host": speaker,
                "content": response,
                "audio": audio
            })
            
            time.sleep(0.8)   # Doğal radyo geçiş hissi
            st.rerun()

# ====================== REJİ MASASI ======================
with st.sidebar:
    st.title("🎚️ Reji Odası")
    st.session_state.ses_acik = st.toggle("🔊 Ses Açık (Otomatik Çalsın)", value=st.session_state.ses_acik)
    
    if st.button("🔴 Yayını Durdur ve Temizle"):
        st.session_state.history = []
        st.session_state.last_speaker = None
        st.rerun()
    
    st.info("""
    ✨ Nasıl Çalışır?
    • Konu veya mesaj yaz
    • Nilay başlar, Kerem cevap verir
    • Biri bitince diğeri devam eder (sarmal atışma)
    • Ses toggle ile aç/kapa
    """)
    
    st.caption("Kurumsal Sesler:\n• Nilay → EmelNeural (Cilveli Bayan)\n• Kerem → AhmetNeural (Samimi Erkek)")

st.caption("Faslı Muhabbet v11.2 • Nilay & Kerem Sarmal Yayın • Kenan ile geliştiriyoruz 💖🎙️")