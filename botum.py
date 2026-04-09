import streamlit as st
from groq import Groq
import asyncio
import edge_tts
import time
from datetime import datetime

st.set_page_config(page_title="Aşk-ı Muhabbet v12.3", layout="wide", page_icon="🎙️")

if "GROQ_API_KEY" not in st.secrets:
    st.error("❌ GROQ_API_KEY secrets.toml dosyasında yok! Lütfen ekle.")
    st.stop()

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "last_speaker" not in st.session_state:
    st.session_state.last_speaker = None

# ====================== SES ÜRETİMİ ======================
async def get_voice_bytes(text: str, voice: str, rate="+0%", pitch="+0Hz"):
    if not text or len(text.strip()) < 2:
        return None
    try:
        communicate = edge_tts.Communicate(text, voice, rate=rate, pitch=pitch)
        audio_data = b""
        async for chunk in communicate.stream():
            if chunk["type"] == "audio":
                audio_data += chunk["data"]
        return audio_data
    except Exception as e:
        st.warning(f"Ses üretimi takıldı: {e}")
        return None

def run_async_safe(coro):
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
    .host-card { padding: 20px; border-radius: 16px; margin: 12px 0; border-left: 10px solid; box-shadow: 0 4px 12px rgba(0,0,0,0.4); }
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
    mod = st.radio("Yayın Modu", ["Tek Sunucu (Dilay)", "Sarmal İkili Sohbet (Dilay + Mert)"])
    enerji = st.select_slider("Enerji Seviyesi", ["Sakin", "Duygusal", "Coşkulu", "Tam Gaz Muzip"], value="Coşkulu")
    if st.button("🔄 Yayını Sıfırla", type="primary"):
        st.session_state.chat_history = []
        st.session_state.last_speaker = None
        st.rerun()

st.markdown(f"<h1 style='text-align:center;'>🎙️ AŞK-I MUHABBET <span class='live-text'>● CANLI</span> v12.3</h1>", unsafe_allow_html=True)
st.caption(f"{datetime.now().strftime('%H:%M')} • Kenan ile Faslı Muhabbet Stüdyosu")

# ====================== SOHBET GÖSTERİM ======================
for i, chat in enumerate(st.session_state.chat_history):
    if chat["role"] == "user":
        st.markdown(f'<div class="patron-bubble"><b>👑 Patron:</b> {chat["content"]}</div>', unsafe_allow_html=True)
    else:
        tema = "dilay-theme" if "Dilay" in chat.get("host", "") else "mert-theme"
        st.markdown(f"""
            <div class="host-card {tema}">
                <b>{chat.get('host', 'Sunucu')}</b><br>
                {chat['content']}
            </div>
            """, unsafe_allow_html=True)
        if chat.get("audio"):
            st.audio(chat["audio"], format="audio/mpeg", key=f"audio_{i}_{chat.get('ts', i)}")

# ====================== KİŞİLİKLER ======================
voices = {
    "Dilay 💖": {"voice": "tr-TR-EmelNeural", "rate": "+5%" if enerji in ["Coşkulu", "Tam Gaz Muzip"] else "+0%", "pitch": "+3Hz"},
    "Mert 🎙️": {"voice": "tr-TR-AhmetNeural", "rate": "+2%", "pitch": "-2Hz"}
}

def get_prompt(host):
    if "Dilay" in host:
        return f"""Sen Dilay'sın. Kenan ile Faslı Muhabbet'in neşeli, cilveli, sıcak kadın sunucususun. 
        Dinleyicilere 'canım', 'ailem', 'güzel insanlar' diye hitap edersin. 
        {'Bol bol espri yap, kıpır kıpır ve işveli ol.' if enerji == 'Tam Gaz Muzip' else 
         'Daha duygusal ve içten konuş.' if enerji == 'Duygusal' else 'Coşkulu ve hayat dolu ol.'}
        Mod: {enerji}"""
    else:
        return f"""Sen Mert'sin. Samimi, ağırbaşlı, güven veren erkek sunucusun. 
        {'Esprili ve kıpır kıpır ol.' if enerji == 'Tam Gaz Muzip' else 
         'Daha derin ve duygusal konuş.' if enerji == 'Duygusal' else 'Coşkulu ve samimi ol.'}
        Mod: {enerji}"""

# ====================== ANA YAYIN AKIŞI ======================
user_prompt = st.chat_input("👑 Patron, yayına bağlan... Bu akşam ne muhabbet edelim?")

if user_prompt:
    st.session_state.chat_history.append({"role": "user", "content": user_prompt, "ts": int(time.time())})
    st.rerun()

if st.button("🎤 Şimdi Konuşsunlar") or (user_prompt and mod == "Sarmal İkili Sohbet (Dilay + Mert)"):
    speakers_order = ["Dilay 💖", "Mert 🎙️"]
    start_idx = 0 if st.session_state.last_speaker is None else (speakers_order.index(st.session_state.last_speaker) + 1) % 2
    
    with st.spinner("🎙️ Mikrofonlar açılıyor... Dilay ve Mert hazırlanıyor ❤️"):
        for i in range(2 if mod == "Sarmal İkili Sohbet (Dilay + Mert)" else 1):
            speaker = speakers_order[(start_idx + i) % 2]
            st.session_state.last_speaker = speaker
            
            try:
                messages = [{"role": "system", "content": get_prompt(speaker)}] + \
                           [{"role": m["role"], "content": m["content"]} for m in st.session_state.chat_history[-8:]]
                
                comp = client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=messages,
                    temperature=0.82,
                    max_tokens=750
                )
                response_text = comp.choices[0].message.content.strip()
            except Exception as e:
                response_text = f"{speaker.split()[0]}, biraz teknik takılma oldu canım ama hemen toparladım. Devam edelim mi?"
            
            # Ses üret
            v = voices[speaker]
            audio_bytes = run_async_safe(get_voice_bytes(response_text, v["voice"], v["rate"], v["pitch"]))
            
            st.session_state.chat_history.append({
                "role": "assistant",
                "host": speaker,
                "content": response_text,
                "audio": audio_bytes,
                "ts": int(time.time())
            })
            
            time.sleep(0.7)  # Doğal geçiş hissi
            st.rerun()  # Her konuşmadan sonra yenile → ses sırayla çalsın

st.caption("❤️ v12.3 • Stabil Sarmal Radyo • Ses + Groq düzeltildi • Kenan’la birlikte geliştiriyoruz")