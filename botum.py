import streamlit as st
from groq import Groq
import asyncio
import edge_tts
import time
from datetime import datetime

st.set_page_config(page_title="Aşk-ı Muhabbet v12.2", layout="wide", page_icon="🎙️")

if "GROQ_API_KEY" not in st.secrets:
    st.error("❌ GROQ_API_KEY bulunamadı!")
    st.stop()

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "last_speaker" not in st.session_state:
    st.session_state.last_speaker = None

# ====================== SES MOTORU ======================
async def get_voice_bytes(text: str, voice: str, rate="+0%", pitch="+0Hz"):
    try:
        communicate = edge_tts.Communicate(text, voice, rate=rate, pitch=pitch)
        audio_data = b""
        async for chunk in communicate.stream():
            if chunk["type"] == "audio":
                audio_data += chunk["data"]
        return audio_data
    except Exception as e:
        st.error(f"Ses üretimi takıldı: {e}")
        return None

def run_async(coro):
    try:
        return asyncio.run(coro)
    except RuntimeError:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        return loop.run_until_complete(coro)

# ====================== TASARIM ======================
st.markdown("""
    <style>
    .stApp { background-color: #05050a; color: #ffffff; }
    .host-card { padding: 20px; border-radius: 16px; margin: 12px 0; border-left: 10px solid; }
    .dilay-theme { background: linear-gradient(135deg, #2a0a25, #4a1a3a); border-color: #ff1493; }
    .mert-theme { background: linear-gradient(135deg, #0a252a, #1a3a4a); border-color: #00d4ff; }
    .patron-bubble { background: rgba(0, 255, 157, 0.12); border-right: 6px solid #00ff9d; padding: 14px; border-radius: 12px; margin: 12px 0; text-align: right; }
    .live-text { color: #ff2d55; font-weight: bold; animation: blinker 1.2s linear infinite; }
    @keyframes blinker { 50% { opacity: 0.4; } }
    </style>
    """, unsafe_allow_html=True)

# ====================== REJİ ======================
with st.sidebar:
    st.title("🎚️ REJİ MASASI")
    secilen_mod = st.radio("Yayın Tarzı", ["Tek Sunucu", "Sarmal İkili Sohbet (Dilay + Mert)"])
    enerji = st.select_slider("Enerji", ["Sakin", "Duygusal", "Coşkulu", "Tam Gaz Muzip"], value="Coşkulu")
    if st.button("🔄 Yayını Sıfırla"):
        st.session_state.chat_history = []
        st.session_state.last_speaker = None
        st.rerun()

st.markdown(f"<h1 style='text-align:center;'>🎙️ AŞK-I MUHABBET <span class='live-text'>● CANLI</span> v12.2</h1>", unsafe_allow_html=True)

# ====================== SOHBET GÖSTERİM ======================
for i, chat in enumerate(st.session_state.chat_history):
    if chat["role"] == "user":
        st.markdown(f'<div class="patron-bubble"><b>👑 Patron:</b> {chat["content"]}</div>', unsafe_allow_html=True)
    else:
        tema = "dilay-theme" if "Dilay" in chat["host"] else "mert-theme"
        st.markdown(f"""
            <div class="host-card {tema}">
                <b>{chat['host']}</b><br>{chat['content']}
            </div>
            """, unsafe_allow_html=True)
        if chat.get("audio"):
            st.audio(chat["audio"], format="audio/mp3", key=f"audio_{i}_{chat.get('timestamp', i)}")

# ====================== KİŞİLİKLER ======================
voices = {
    "Dilay 💖": {"voice": "tr-TR-EmelNeural", "rate": "+4%" if enerji in ["Coşkulu", "Tam Gaz Muzip"] else "+0%", "pitch": "+3Hz"},
    "Mert 🎙️": {"voice": "tr-TR-AhmetNeural", "rate": "+2%", "pitch": "-2Hz"}
}

def get_system_prompt(host):
    base = "Sen " + ("Dilay'sın. Neşeli, cilveli, hayat dolu, dinleyiciye 'canım', 'ailem' diye hitap eden kadın sunucusun." if "Dilay" in host else 
                     "Mert'sin. Samimi, ağırbaşlı, güven veren erkek sunucusun.")
    if enerji == "Tam Gaz Muzip":
        base += " Bol bol espri yap, kıpır kıpır konuş."
    elif enerji == "Duygusal":
        base += " Daha içten ve duygusal ol, yeri geldiğinde şiir oku."
    return base

# ====================== YAYIN AKIŞI ======================
prompt = st.chat_input("👑 Patron, yayına bağlan... Bu akşam ne muhabbet edelim?")

if prompt:
    st.session_state.chat_history.append({"role": "user", "content": prompt, "timestamp": int(time.time())})
    st.rerun()

# Otomatik devam veya manuel tetik
if st.button("🎤 Şimdi Konuşsunlar") or (prompt and secilen_mod == "Sarmal İkili Sohbet (Dilay + Mert)"):
    speakers = ["Dilay 💖", "Mert 🎙️"]
    start_idx = 0 if st.session_state.last_speaker is None else speakers.index(st.session_state.last_speaker) + 1
    
    with st.spinner("🎙️ Yayın devam ediyor... Mikrofonlar ısınsın ❤️"):
        for idx in range(start_idx, start_idx + 2):  # İki sunucu sırayla
            speaker = speakers[idx % 2]
            st.session_state.last_speaker = speaker
            
            system_prompt = get_system_prompt(speaker)
            messages = [{"role": "system", "content": system_prompt}] + \
                       [{"role": m["role"], "content": m["content"]} for m in st.session_state.chat_history[-10:]]
            
            try:
                comp = client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=messages,
                    temperature=0.85,
                    max_tokens=700
                )
                response_text = comp.choices[0].message.content
            except:
                response_text = f"{speaker.split()[0]}, biraz takıldım ama hemen toparladım... {prompt if prompt else 'Devam edelim mi?'} hakkında ne düşünüyorsun?"
            
            # Ses üret
            v = voices[speaker]
            audio_bytes = run_async(get_voice_bytes(response_text, v["voice"], v["rate"], v["pitch"]))
            
            st.session_state.chat_history.append({
                "role": "assistant",
                "host": speaker,
                "content": response_text,
                "audio": audio_bytes,
                "timestamp": int(time.time())
            })
            
            # Küçük gecikme hissi için (gerçek radyo gibi)
            time.sleep(0.8)
            st.rerun()   # Her konuşmadan sonra ekranı yenile → sesler sırayla çalsın

st.caption("❤️ Aşk-ı Muhabbet v12.2 • Sarmal İkili Radyo Modu • Kenan ile Faslı Muhabbet Stüdyosu")