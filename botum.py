import streamlit as st
from groq import Groq
import asyncio
import edge_tts
import time
from datetime import datetime

st.set_page_config(page_title="Aşk-ı Muhabbet v12.8", layout="wide", page_icon="🎙️")

if "GROQ_API_KEY" not in st.secrets:
    st.error("❌ GROQ_API_KEY secrets.toml dosyasında yok!")
    st.stop()

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# ====================== KURUMSAL SES ÜRETİMİ ======================
async def get_voice_bytes(text: str):
    if not text or len(text.strip()) < 3:
        return None
    try:
        communicate = edge_tts.Communicate(text, "tr-TR-EmelNeural")  # Kurumsal kaliteli kadın sesi
        audio_data = b""
        async for chunk in communicate.stream():
            if chunk["type"] == "audio":
                audio_data += chunk["data"]
        return audio_data
    except:
        return None  # Sessizce None dön, uygulama çökmesin

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
    .stApp { background-color: #05050a; color: #ffffff; }
    .dilay-card { padding: 25px; border-radius: 20px; margin: 15px 0; border-left: 12px solid #ff1493; 
                  background: linear-gradient(135deg, #2a0a25, #4a1a3a); box-shadow: 0 6px 20px rgba(0,0,0,0.4); }
    .patron-bubble { background: rgba(0, 255, 157, 0.15); border-right: 8px solid #00ff9d; padding: 18px; 
                     border-radius: 16px; margin: 15px 0; text-align: right; }
    .live-text { color: #ff2d55; font-weight: bold; animation: blinker 1.4s linear infinite; }
    @keyframes blinker { 50% { opacity: 0.3; } }
    </style>
    """, unsafe_allow_html=True)

# ====================== REJİ ======================
with st.sidebar:
    st.title("🎚️ REJİ MASASI")
    enerji = st.select_slider("Enerji Seviyesi", ["Coşkulu", "Tam Gaz Muzip", "Duygusal"], value="Coşkulu")
    if st.button("🔄 Yayını Sıfırla", type="primary"):
        st.session_state.chat_history = []
        st.rerun()

st.markdown(f"<h1 style='text-align:center;'>🎙️ AŞK-I MUHABBET <span class='live-text'>● CANLI</span> v12.8</h1>", unsafe_allow_html=True)
st.caption(f"{datetime.now().strftime('%H:%M')} • Kurumsal Ses Modu")

# ====================== SOHBET GÖSTERİM ======================
for i, chat in enumerate(st.session_state.chat_history):
    if chat["role"] == "user":
        st.markdown(f'<div class="patron-bubble"><b>👑 Patron:</b> {chat["content"]}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f"""
            <div class="dilay-card">
                <b>Dilay 💖</b><br><br>
                {chat.get('content', 'Cevap alınamadı...')}
            </div>
            """, unsafe_allow_html=True)
        
        # Ses varsa göster (hata vermeden)
        if chat.get("audio") is not None and len(chat.get("audio", b"")) > 200:
            try:
                st.audio(chat["audio"], format="audio/mpeg", key=f"audio_{i}_{chat.get('ts', i)}")
            except:
                pass  # Sessizce geç

# ====================== DILAY PROMPT ======================
def get_dilay_prompt(enerji):
    return f"""Sen Dilay'sın. Kenan ile Faslı Muhabbet'in neşeli, cilveli, hayat dolu kadın sunucususun. 
    Dinleyicilere "canım", "ailem", "güzel insanlar" diye hitap edersin. 
    {'Bol bol espri yap, kıpır kıpır ve işveli konuş.' if enerji == 'Tam Gaz Muzip' else 
     'Daha duygusal ve içten konuş.' if enerji == 'Duygusal' else 'Coşkulu ve sıcak bir şekilde cevap ver.'}
    Mod: {enerji}"""

# ====================== YAYIN AKIŞI ======================
user_input = st.chat_input("👑 Patron, yayına bağlan... Bu akşam ne muhabbet edelim?")

if user_input:
    st.session_state.chat_history.append({"role": "user", "content": user_input, "ts": int(time.time())})
    
    with st.spinner("🎙️ Dilay hazırlanıyor... Kurumsal ses yükleniyor ❤️"):
        try:
            messages = [{"role": "system", "content": get_dilay_prompt(enerji)}] + \
                       [{"role": m["role"], "content": m["content"]} for m in st.session_state.chat_history[-6:]]
            
            comp = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=messages,
                temperature=0.85,
                max_tokens=700
            )
            response_text = comp.choices[0].message.content.strip()
        except Exception:
            response_text = f"Canım patron, seni duydum. {user_input} hakkında ne güzel muhabbet edelim bu akşam?"

        # Kurumsal ses üret
        audio_bytes = run_async_safe(get_voice_bytes(response_text))
        
        st.session_state.chat_history.append({
            "role": "assistant",
            "content": response_text,
            "audio": audio_bytes,
            "ts": int(time.time())
        })
        
        st.rerun()

st.caption("❤️ v12.8 • Kurumsal Türkçe Ses (EmelNeural) • Stabil mod • Kenan’la geliştiriyoruz")