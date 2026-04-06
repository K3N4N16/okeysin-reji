import streamlit as st
from groq import Groq
import edge_tts
import asyncio
import base64
import random
from datetime import datetime

# ====================== SAYFA AYARLARI ======================
st.set_page_config(
    page_title="Faslı Muhabbet v7.0",
    layout="wide",
    page_icon="🎙️",
    initial_sidebar_state="expanded"
)

if "GROQ_API_KEY" not in st.secrets:
    st.error("⚠️ GROQ API Key Eksik!")
    st.stop()

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

# ====================== REJİ MASASI ÖZEL CSS ======================
st.markdown("""
    <style>
    .stApp { background: #05000a; color: #ffffff; }
    
    /* Dilay'ın Yayın Çerçevesi */
    .studio-box {
        background: rgba(255, 20, 147, 0.05);
        border: 2px dashed #ff1493;
        border-radius: 30px;
        padding: 40px;
        margin: 25px 0;
        box-shadow: 0 0 50px rgba(255, 20, 147, 0.15);
        text-align: center;
    }
    
    /* Yüzen Ses Butonu */
    .float-audio-btn {
        position: fixed;
        bottom: 30px;
        right: 30px;
        background: #ff1493;
        color: white;
        padding: 20px;
        border-radius: 50%;
        border: none;
        box-shadow: 0 0 30px #ff1493;
        cursor: pointer;
        z-index: 1000;
        font-weight: bold;
        animation: pulse-pink 2s infinite;
    }
    @keyframes pulse-pink { 0% { transform: scale(1); } 50% { transform: scale(1.1); } 100% { transform: scale(1); } }
    
    .patron-text { color: #00ff9d; font-family: monospace; border-left: 3px solid #00ff9d; padding-left: 10px; }
    .dilay-text { font-size: 1.5rem; line-height: 1.6; color: #ff69b4; text-shadow: 0 0 10px rgba(255, 105, 180, 0.5); }
    </style>
    """, unsafe_allow_html=True)

# ====================== SES MOTORU (JS KÖPRÜSÜ) ======================
async def produce_audio(text: str, speed: str = "0%"):
    try:
        clean_text = text.replace("*", "").strip()
        communicate = edge_tts.Communicate(clean_text, "tr-TR-FilizNeural", rate=speed)
        data = b""
        async for chunk in communicate.stream():
            if chunk["type"] == "audio":
                data += chunk["data"]
        return data
    except:
        return None

def force_play_audio(audio_bytes):
    """Sesi JavaScript üzerinden zorla oynatır (Tarayıcıyı uyandırır)"""
    b64 = base64.b64encode(audio_bytes).decode()
    js_code = f"""
        <script>
            var audio = new Audio("data:audio/mp3;base64,{b64}");
            audio.play().catch(e => {{
                console.log("Otomatik oynatma için kullanıcı tıklaması bekleniyor.");
            }});
        </script>
    """
    st.components.v1.html(js_code, height=0)

# ====================== SESSION STATE ======================
if "history" not in st.session_state:
    st.session_state.history = []
if "v_speed" not in st.session_state:
    st.session_state.v_speed = "0%"

# ====================== BAŞLIK PANELİ ======================
st.markdown(f"""
    <div style="text-align:center;">
        <h1 style="color:#ff1493; font-size:3.5rem; margin-bottom:0;">🎙️ FASLI MUHABBET</h1>
        <p style="color:#aaa; letter-spacing:3px;">BURSA REJİ MASASI • v7.0 ULTRA</p>
    </div>
""", unsafe_allow_html=True)

# ====================== YAYIN AKIŞI ======================
for i, chat in enumerate(st.session_state.history):
    if chat["role"] == "user":
        st.markdown(f'<p class="patron-text">🤵 <b>Patron:</b> {chat["content"]}</p>', unsafe_allow_html=True)
    else:
        with st.container():
            st.markdown(f"""
                <div class="studio-box">
                    <div style="color:#ff1493; font-weight:bold; margin-bottom:15px;">💖 DİLAY YAYINDA</div>
                    <div class="dilay-text">{chat['content']}</div>
                </div>
            """, unsafe_allow_html=True)
            
            if chat.get("audio"):
                # Sabit Ses Çubuğu (Garanti Çözüm)
                st.audio(chat["audio"], format="audio/mp3")
                
                col1, col2 = st.columns([1, 4])
                with col1:
                    if st.button("🔊 Tekrar", key=f"re_{i}"):
                        force_play_audio(chat["audio"])

# ====================== MESAJ GİRİŞİ ======================
if prompt := st.chat_input("Dilay'ına bir mesaj bırak Patron..."):
    st.session_state.history.append({"role": "user", "content": prompt})

    with st.spinner("💖 Dilay heyecanla mikrofona yaklaşıyor..."):
        sys_prompt = "Sen Dilay'sın. Bursa'lı, Patronuna aşık, cilveli radyo sunucususun. Samimi ve neşeli konuş."
        
        # Groq Zekası
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "system", "content": sys_prompt}] + st.session_state.history[-10:],
            temperature=0.9
        ).choices[0].message.content

        # Ses Üretimi
        audio_data = asyncio.run(produce_audio(response, speed=st.session_state.v_speed))

        # Kaydet
        st.session_state.history.append({
            "role": "assistant",
            "content": response,
            "audio": audio_data
        })

        # Sesi hemen tetikle
        if audio_data:
            force_play_audio(audio_data)
        
        st.rerun()

# ====================== SIDEBAR & EKSTRALAR ======================
with st.sidebar:
    st.title("🎚️ Kontrol Paneli")
    st.session_state.v_speed = st.select_slider("Konuşma Hızı", 
                                              options=["-20%", "-10%", "0%", "+10%", "+20%"], 
                                              value=st.session_state.v_speed)
    
    st.divider()
    if st.button("🔴 Yayını Resetle"):
        st.session_state.history = []
        st.rerun()

    st.markdown("### 🛠️ SES GELMİYORSA:")
    st.warning("1. Sayfada herhangi bir yere tıklayın.\n2. Alttaki ses çubuğundan 'Oynat'a basın.\n3. Tarayıcıda 'Ses İzni' verildiğinden emin olun.")

# Yüzen Bilgi
st.markdown('<button class="float-audio-btn">🎙️</button>', unsafe_allow_html=True)
