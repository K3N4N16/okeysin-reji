import streamlit as st
from groq import Groq
import asyncio
import edge_tts
import time
from datetime import datetime

st.set_page_config(page_title="Aşk-ı Muhabbet v12.4", layout="wide", page_icon="🎙️")

if "GROQ_API_KEY" not in st.secrets:
    st.error("❌ GROQ_API_KEY secrets.toml dosyasında yok! Lütfen ekle ve yeniden başlat.")
    st.stop()

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# ====================== SES ÜRETİMİ ======================
async def get_voice_bytes(text: str, voice: str):
    if not text or len(text.strip()) < 3:
        return None
    try:
        communicate = edge_tts.Communicate(text, voice)
        audio_data = b""
        async for chunk in communicate.stream():
            if chunk["type"] == "audio":
                audio_data += chunk["data"]
        return audio_data
    except Exception as e:
        st.warning(f"🎙️ Ses üretilemedi: {str(e)[:100]}... Ama metin görünüyor.")
        return None

def run_async_safe(coro):
    try:
        return asyncio.run(coro)
    except:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        return loop.run_until_complete(coro)

# ====================== TASARIM ======================
st.markdown("""
    <style>
    .stApp { background-color: #05050a; color: #ffffff; }
    .dilay-card { padding: 20px; border-radius: 16px; margin: 12px 0; border-left: 10px solid #ff1493; background: linear-gradient(135deg, #2a0a25, #4a1a3a); }
    .patron-bubble { background: rgba(0, 255, 157, 0.12); border-right: 6px solid #00ff9d; padding: 14px; border-radius: 12px; margin: 12px 0; text-align: right; }
    .live-text { color: #ff2d55; font-weight: bold; animation: blinker 1.2s linear infinite; }
    @keyframes blinker { 50% { opacity: 0.4; } }
    </style>
    """, unsafe_allow_html=True)

# ====================== REJİ ======================
with st.sidebar:
    st.title("🎚️ REJİ MASASI")
    enerji = st.select_slider("Enerji Seviyesi", ["Sakin", "Coşkulu", "Tam Gaz Muzip"], value="Coşkulu")
    if st.button("🔄 Yayını Sıfırla", type="primary"):
        st.session_state.chat_history = []
        st.rerun()

st.markdown(f"<h1 style='text-align:center;'>🎙️ AŞK-I MUHABBET <span class='live-text'>● CANLI</span> v12.4</h1>", unsafe_allow_html=True)
st.caption(f"{datetime.now().strftime('%H:%M')} • Sadece Dilay ile test ediyoruz")

# ====================== SOHBET GÖSTERİM ======================
for i, chat in enumerate(st.session_state.chat_history):
    if chat["role"] == "user":
        st.markdown(f'<div class="patron-bubble"><b>👑 Patron:</b> {chat["content"]}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f"""
            <div class="dilay-card">
                <b>Dilay 💖</b><br>
                {chat['content']}
            </div>
            """, unsafe_allow_html=True)
        if chat.get("audio"):
            st.audio(chat["audio"], format="audio/mpeg", key=f"audio_{i}_{chat.get('ts', i)}")

# ====================== DILAY PROMPT ======================
def get_dilay_prompt():
    return f"""Sen Dilay'sın. Kenan ile Faslı Muhabbet'in neşeli, cilveli, sıcak kadın sunucususun. 
    Dinleyicilere "canım", "ailem", "güzel insanlar" diye hitap edersin. 
    {'Bol bol espri yap, kıpır kıpır ve işveli ol.' if enerji == 'Tam Gaz Muzip' else 'Coşkulu ve hayat dolu konuş.'}
    Mod: {enerji}"""

# ====================== ANA YAYIN AKIŞI ======================
user_input = st.chat_input("👑 Patron, yayına bağlan... Bu akşam ne muhabbet edelim?")

if user_input:
    st.session_state.chat_history.append({"role": "user", "content": user_input, "ts": int(time.time())})
    
    with st.spinner("🎙️ Dilay hazırlanıyor... Mikrofon ısınsın canım ❤️"):
        try:
            messages = [{"role": "system", "content": get_dilay_prompt()}] + \
                       [{"role": m["role"], "content": m["content"]} for m in st.session_state.chat_history[-6:]]
            
            comp = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=messages,
                temperature=0.85,
                max_tokens=600
            )
            response_text = comp.choices[0].message.content.strip()
            
            st.success("✅ Groq'dan cevap geldi!")
            
        except Exception as e:
            response_text = f"Canım patron, biraz teknik bir takılma oldu ama hemen toparladım. {user_input} hakkında ne muhabbet edelim?"
            st.error(f"❌ Groq hatası: {str(e)[:150]}")

        # Ses üret
        audio_bytes = run_async_safe(get_voice_bytes(response_text, "tr-TR-EmelNeural"))
        
        st.session_state.chat_history.append({
            "role": "assistant",
            "content": response_text,
            "audio": audio_bytes,
            "ts": int(time.time())
        })
        
        st.rerun()

st.caption("❤️ v12.4 • Sadece Dilay ile basit ve stabil test • Hata görürsen tam mesajı söyle")