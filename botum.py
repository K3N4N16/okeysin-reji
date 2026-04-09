import streamlit as st
from groq import Groq
import asyncio
import edge_tts
import time
from datetime import datetime

# ====================== 1. BAŞLATMA ======================
st.set_page_config(page_title="Aşk-ı Muhabbet v12.1", layout="wide", page_icon="🎙️")

if "GROQ_API_KEY" not in st.secrets:
    st.error("❌ GROQ_API_KEY bulunamadı! Secrets'e eklemeyi unutma.")
    st.stop()

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# ====================== 2. ASYNC SES MOTORU ======================
async def get_voice_bytes(text: str, voice: str, rate: str = "+0%", pitch: str = "+0Hz"):
    try:
        communicate = edge_tts.Communicate(text, voice, rate=rate, pitch=pitch)
        audio_data = b""
        async for chunk in communicate.stream():
            if chunk["type"] == "audio":
                audio_data += chunk["data"]
        return audio_data
    except Exception as e:
        st.error(f"Ses üretiminde ufak bir takılma oldu: {e}")
        return None

def run_async(coro):
    try:
        return asyncio.run(coro)
    except RuntimeError:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        return loop.run_until_complete(coro)

# ====================== 3. TASARIM ======================
st.markdown("""
    <style>
    .stApp { background-color: #05050a; color: #ffffff; }
    .host-card { padding: 22px; border-radius: 18px; margin: 15px 0; border-left: 12px solid; box-shadow: 0 4px 15px rgba(0,0,0,0.3); }
    .dilay-theme { background: linear-gradient(135deg, #2a0a25, #4a1a3a); border-color: #ff1493; }
    .mert-theme { background: linear-gradient(135deg, #0a252a, #1a3a4a); border-color: #00d4ff; }
    .patron-bubble { background: rgba(0, 255, 157, 0.12); border-right: 6px solid #00ff9d; padding: 15px; border-radius: 12px; margin: 12px 0; text-align: right; }
    .live-text { color: #ff2d55; font-weight: bold; animation: blinker 1.1s linear infinite; }
    @keyframes blinker { 50% { opacity: 0.3; } }
    </style>
    """, unsafe_allow_html=True)

# ====================== 4. REJİ MASASI ======================
with st.sidebar:
    st.title("🎚️ REJİ MASASI")
    secilen_sunucu = st.radio("🎤 Mikrofon Kimde?", ["Dilay 💖", "Mert 🎙️"])
    
    yayin_modu = st.selectbox("Yayın Modu", 
        ["Standart Muhabbet", "Neşeli & Cilveli", "Duygusal Gece", "Şiir Saati", "Coşkulu Radyo"])
    
    enerji = st.select_slider("Enerji Seviyesi", 
        options=["Sakin", "Duygusal", "Standart", "Coşkulu", "Tam Gaz Muzip"], value="Coşkulu")
    
    if st.button("🔄 Yayını Sıfırla", type="primary"):
        st.session_state.chat_history = []
        st.rerun()

st.markdown(f"<h1 style='text-align:center;'>🎙️ AŞK-I MUHABBET <span class='live-text'>● CANLI</span> v12.1</h1>", unsafe_allow_html=True)
st.caption(f"Şu an {secilen_sunucu.split()[0]} yayın yapıyor • {datetime.now().strftime('%H:%M')}")

# ====================== 5. SOHBET GÖSTERİM ======================
for i, chat in enumerate(st.session_state.chat_history):
    if chat["role"] == "user":
        st.markdown(f'<div class="patron-bubble"><b>👑 Patron:</b> {chat["content"]}</div>', unsafe_allow_html=True)
    else:
        tema = "dilay-theme" if chat["host"] == "Dilay 💖" else "mert-theme"
        st.markdown(f"""
            <div class="host-card {tema}">
                <b>{chat['host']}</b><br>
                {chat['content']}
            </div>
            """, unsafe_allow_html=True)
        
        if chat.get("audio") is not None:
            st.audio(chat["audio"], format="audio/mp3", key=f"audio_{i}_{int(time.time()*1000)}")

# ====================== 6. KİŞİLİKLER ======================
mod_prompt_ek = {
    "Neşeli & Cilveli": " Çok kıpır kıpır, işveli, sık sık gülümseyerek konuş, hafif cilveli ol.",
    "Duygusal Gece": " Daha derin, duygusal, yer yer şiirsel ve içten ol.",
    "Şiir Saati": " Konuşmana sık sık güzel dizeler serpiştir, edebi bir hava kat.",
    "Coşkulu Radyo": " Yüksek enerji, coşkulu, dinleyiciyi ateşle!",
    "Standart Muhabbet": ""
}

personalar = {
    "Dilay 💖": {
        "prompt": f"""Sen Dilay'sın. Kenan ile Faslı Muhabbet'in neşeli, hayat dolu, cilveli kadın sunucususun. 
        Sıcak, samimi, kucaklayıcı bir üslubun var. Dinleyicilere "canım", "ailem", "güzel insanlar" diye hitap edersin. 
        {mod_prompt_ek[yayin_modu]}
        Modun: {enerji}""",
        "voice": "tr-TR-EmelNeural",
        "rate": "+5%" if enerji in ["Coşkulu", "Tam Gaz Muzip"] else "+0%",
        "pitch": "+2Hz" if enerji in ["Neşeli & Cilveli", "Tam Gaz Muzip"] else "+0Hz"
    },
    "Mert 🎙️": {
        "prompt": f"""Sen Mert'sin. Ağırbaşlı, samimi, güven veren erkek sunucusun. 
        Derinlikli ve içten konuşursun. {mod_prompt_ek[yayin_modu]}
        Modun: {enerji}""",
        "voice": "tr-TR-AhmetNeural",
        "rate": "+3%" if enerji == "Coşkulu" else "+0%",
        "pitch": "-1Hz"
    }
}

# ====================== 7. YAYIN AKIŞI ======================
if prompt := st.chat_input("👑 Patron, yayına bağlan... Ne muhabbet edelim bu akşam?"):
    st.session_state.chat_history.append({"role": "user", "content": prompt})
    
    with st.spinner(f"🎙️ {secilen_sunucu.split()[0]} hazırlanıyor... Mikrofon ısınsın biraz ❤️"):
        
        system_prompt = personalar[secilen_sunucu]["prompt"]
        messages = [{"role": "system", "content": system_prompt}] + \
                   [{"role": m["role"], "content": m["content"]} for m in st.session_state.chat_history[-8:]]
        
        try:
            comp = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=messages,
                temperature=0.85,
                max_tokens=800
            )
            response_text = comp.choices[0].message.content
        except Exception as e:
            response_text = f"Biraz teknik bir takılma oldu canım, ama hemen toparlıyorum... {prompt} hakkında ne diyecektim ben?"
        
        voice_params = personalar[secilen_sunucu]
        audio_bytes = run_async(get_voice_bytes(
            response_text, 
            voice_params["voice"],
            rate=voice_params["rate"],
            pitch=voice_params["pitch"]
        ))
        
        st.session_state.chat_history.append({
            "role": "assistant",
            "host": secilen_sunucu,
            "content": response_text,
            "audio": audio_bytes
        })
        
        st.rerun()

# ====================== 8. ALT BARI ======================
st.markdown("---")
st.caption(" Aşk-ı Muhabbet • Kenan ile Faslı Muhabbet'in dijital stüdyosu • v12.1")