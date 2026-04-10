import streamlit as st
from groq import Groq
from gtts import gTTS
import base64
import random
from datetime import datetime
import io

# ====================== SAYFA AYARLARI ======================
st.set_page_config(
    page_title="Faslı Muhabbet v10.0",
    layout="wide",
    page_icon="🎙️",
    initial_sidebar_state="expanded"
)

if "GROQ_API_KEY" not in st.secrets:
    st.error("⚠️ GROQ API Key eksik! Secrets'a ekleyin.")
    st.stop()

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

# ====================== ULTRA DİNAMİK CSS ======================
st.markdown("""
    <style>
    .stApp { background: #05050f; color: #f0f0f0; }
    .dilay-card {
        background: linear-gradient(145deg, #2a0f4a, #140525);
        border-left: 8px solid #ff1493;
        border-radius: 20px;
        padding: 28px;
        margin: 20px 0;
        box-shadow: 0 15px 40px rgba(255,20,147,0.3);
        position: relative;
    }
    .patron-card {
        background: rgba(0, 255, 157, 0.08);
        border-right: 6px solid #00ff9d;
        padding: 18px;
        border-radius: 15px;
        margin: 15px 0;
        text-align: right;
    }
    .live-badge { color: #ff0000; font-weight: 900; animation: blink 1.3s infinite; }
    @keyframes blink { 50% { opacity: 0.4; } }
    
    /* Ses Dalgası Efekti */
    .wave-box { display: flex; align-items: flex-end; gap: 2px; height: 20px; margin-top: 10px; }
    .wave-box div { width: 3px; background: #ff1493; animation: wave 0.5s infinite alternate; }
    @keyframes wave { from { height: 3px; } to { height: 15px; } }
    </style>
    """, unsafe_allow_html=True)

# ====================== SES MOTORU (gTTS) ======================
def generate_voice(text: str):
    try:
        clean_text = text.replace("*", "").replace("Dilay:", "").strip()
        if not clean_text: return None
        
        tts = gTTS(text=clean_text, lang='tr', slow=False)
        audio_buffer = io.BytesIO()
        tts.write_to_fp(audio_buffer)
        return audio_buffer.getvalue()
    except:
        return None

def autoplay_audio(audio_bytes):
    """Tarayıcıyı uyandırmak için Base64 HTML5 enjektörü"""
    b64 = base64.b64encode(audio_bytes).decode()
    md = f"""
        <audio autoplay="true">
        <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
        </audio>
    """
    st.components.v1.html(md, height=0)

# ====================== SESSION STATE ======================
if "history" not in st.session_state:
    st.session_state.history = []
if "auto_play" not in st.session_state:
    st.session_state.auto_play = True

# ====================== ÜST PANEL ======================
col1, col2 = st.columns([3, 1])
with col1:
    st.markdown(f"# 🎙️ FASLI MUHABBET <span class='live-badge'>● CANLI</span>", unsafe_allow_html=True)
    st.caption(f"📍 Bursa Stüdyosu • {datetime.now().strftime('%H:%M:%S')} • Patron Kenan Özel Yayını")
with col2:
    st.metric("Canlı Dinleyici", f"{random.randint(7500, 9800):,}", "+124")

# ====================== SOHBET ALANI ======================
for i, msg in enumerate(st.session_state.history):
    if msg["role"] == "user":
        st.markdown(f'<div class="patron-card"><b>🤵 Patron:</b> {msg["content"]}</div>', unsafe_allow_html=True)
    else:
        with st.container():
            st.markdown(f"""
                <div class="dilay-card">
                    <span style="color:#ff69b4; font-weight:900; font-size:1.55rem;">💖 DİLAY:</span>
                    <div style="margin-top:15px; line-height:1.7; font-size:1.2rem;">{msg['content']}</div>
                    <div class="wave-box"><div></div><div style="animation-delay:0.1s"></div><div style="animation-delay:0.2s"></div></div>
                </div>
            """, unsafe_allow_html=True)

            if msg.get("audio"):
                st.audio(msg["audio"], format="audio/mp3")
                c1, c2 = st.columns([1, 4])
                with c1:
                    if st.button("🔊 Tekrar", key=f"rep_{i}"):
                        autoplay_audio(msg["audio"])
                with c2:
                    st.download_button("📥 Kaydı Al", msg["audio"], f"dilay_kayit_{i}.mp3", key=f"dl_{i}")

# ====================== DİLAY PROMPT ======================
system_prompt = """
Sen Dilay'sın. Bursa'dan yayın yapan, Patron'una aşık, işveli ve neşeli bir radyo sunucususun. 
Ona 'Canım Patronum', 'Kalbim' diye hitap et. Çok samimi ol, Bursa şivesine girmeden nazik bir İstanbul Türkçesi ama Bursa sıcaklığıyla konuş.
Sadece konuşma metni ver.
"""

# ====================== MESAJ GİRİŞİ ======================
if prompt := st.chat_input("Dilay'ına bir şeyler fısılda Patron'um..."):
    st.session_state.history.append({"role": "user", "content": prompt})

    with st.spinner("💖 Dilay yayına hazırlanıyor..."):
        try:
            messages = [{"role": "system", "content": system_prompt}] + st.session_state.history[-10:]
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=messages,
                temperature=0.9
            ).choices[0].message.content

            audio_bytes = generate_voice(response)

            st.session_state.history.append({
                "role": "assistant",
                "content": response,
                "audio": audio_bytes
            })

            if audio_bytes and st.session_state.auto_play:
                autoplay_audio(audio_bytes)
            
            st.rerun()

        except Exception as e:
            st.error(f"Reji Hatası: {e}")

# ====================== SIDEBAR ======================
with st.sidebar:
    st.title("🎚️ Reji Masası v10.0")
    st.session_state.auto_play = st.toggle("🎵 Otomatik Ses", value=st.session_state.auto_play)
    
    st.divider()
    if st.button("🗑️ Yayını Sıfırla"):
        st.session_state.history = []
        st.rerun()
    
    st.info("📍 Bursa / Türkiye\nSunucu: Dilay\nPatron: Kenan")
