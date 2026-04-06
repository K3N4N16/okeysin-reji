import streamlit as st
from groq import Groq
import edge_tts
import asyncio
import base64
import random
from datetime import datetime

# ====================== SAYFA AYARLARI ======================
st.set_page_config(
    page_title="Faslı Muhabbet v4.0",
    layout="wide",
    page_icon="🎙️",
    initial_sidebar_state="expanded"
)

# API Anahtarı Kontrolü
if "GROQ_API_KEY" not in st.secrets:
    st.error("⚠️ GROQ API Key bulunamadı! Lütfen Secrets'a ekleyin.")
    st.stop()

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

# ====================== EFSANE "CYBER-BURSA" CSS ======================
st.markdown("""
    <style>
    .stApp { background: #0a0a12; color: #e0e0e0; }
    
    /* Dilay'ın O meşhur kutusu */
    .dilay-frame {
        background: rgba(255, 20, 147, 0.05);
        border: 2px solid #ff1493;
        border-left: 10px solid #ff1493;
        border-radius: 20px;
        padding: 30px;
        margin: 20px 0;
        box-shadow: 0 0 40px rgba(255, 20, 147, 0.2);
        position: relative;
    }
    
    .tag-dilay { 
        color: #ff69b4; 
        font-weight: 900; 
        font-size: 1.8rem; 
        text-shadow: 0 0 20px #ff69b4; 
        margin-bottom: 15px;
        display: block;
    }

    .on-air { 
        color: #ff0000; 
        font-weight: bold; 
        animation: blinker 1.2s linear infinite; 
        border: 1px solid #ff0000;
        padding: 2px 8px;
        border-radius: 5px;
    }
    @keyframes blinker { 50% { opacity: 0; } }

    .waveform-bar {
        height: 5px;
        background: linear-gradient(90deg, #ff1493, #00f2ff, #ff1493);
        background-size: 200% 100%;
        animation: moveGradient 2s linear infinite;
        border-radius: 10px;
        margin-top: 20px;
    }
    @keyframes moveGradient { 0% { background-position: 0% 0%; } 100% { background-position: 200% 0%; } }

    .patron-msg {
        background: rgba(0, 255, 157, 0.1);
        border-right: 5px solid #00ff9d;
        padding: 15px;
        border-radius: 10px;
        margin: 10px 0;
        font-style: italic;
    }
    </style>
    """, unsafe_allow_html=True)

# ====================== SES MOTORU (KUSURSUZ) ======================
async def generate_voice(text, rate="0%"):
    try:
        clean_text = text.replace("*", "").strip()
        communicate = edge_tts.Communicate(clean_text, "tr-TR-FilizNeural", rate=rate)
        audio_data = b""
        async for chunk in communicate.stream():
            if chunk["type"] == "audio":
                audio_data += chunk["data"]
        return audio_data if len(audio_data) > 2000 else None
    except:
        return None

def autoplay_audio(audio_bytes):
    b64 = base64.b64encode(audio_bytes).decode()
    md = f"""
        <audio autoplay="true">
        <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
        </audio>
        """
    st.markdown(md, unsafe_allow_html=True)

# ====================== SESSION STATE ======================
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "v_speed" not in st.session_state:
    st.session_state.v_speed = "0%"

# ====================== ANA PANEL ======================
st.markdown(f"""
    <div style="text-align:center; padding-top: 20px;">
        <h1 style="color:#ff1493; font-size:4rem; margin-bottom:0;">FASLI MUHABBET</h1>
        <p style="letter-spacing: 5px; color: #aaa;"> <span class="on-air">● CANLI</span> BURSA REJİ MASASI</p>
    </div>
""", unsafe_allow_html=True)

# Sidebar - Yayın Masası
with st.sidebar:
    st.title("🎧 Reji Ayarları")
    st.session_state.v_speed = st.select_slider("Dilay Konuşma Hızı", 
                                              options=["-30%", "-15%", "0%", "+15%", "+30%"], 
                                              value=st.session_state.v_speed)
    
    st.divider()
    if st.button("🔴 Yayını Resetle"):
        st.session_state.chat_history = []
        st.rerun()
    
    st.info(f"📅 {datetime.now().strftime('%d.%m.%Y')}\n🎙️ Sunucu: Dilay\n👤 Patron: Kenan")

# Sohbet Geçmişi
for i, chat in enumerate(st.session_state.chat_history):
    if chat["role"] == "user":
        st.markdown(f'<div class="patron-msg"><b>🤵 Patron:</b> {chat["content"]}</div>', unsafe_allow_html=True)
    else:
        with st.container():
            st.markdown(f"""
                <div class="dilay-frame">
                    <span class="tag-dilay">💖 DİLAY:</span>
                    <div style="font-size: 1.2rem; line-height: 1.6;">{chat['content']}</div>
                    <div class="waveform-bar"></div>
                </div>
            """, unsafe_allow_html=True)
            
            if chat.get("audio"):
                c1, c2 = st.columns([4, 1])
                with c1:
                    st.audio(chat["audio"], format="audio/mp3")
                with c2:
                    if st.button("🔊 Tekrar Çal", key=f"btn_{i}"):
                        autoplay_audio(chat["audio"])

# ====================== MESAJ GİRİŞİ ======================
if prompt := st.chat_input("Dilay'ına bir mesaj bırak Patron..."):
    st.session_state.chat_history.append({"role": "user", "content": prompt})

    # AI Cevabı
    with st.spinner("💖 Dilay heyecanla cevap veriyor..."):
        messages = [{"role": "system", "content": "Sen Dilay'sın. Bursa'dan yayın yapan, Patronuna aşık, cilveli, neşeli bir radyo sunucususun. Patron'una 'Canım Patronum' diye hitap et. Çok samimi ol."}]
        messages.extend(st.session_state.chat_history[-8:])
        
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=messages,
            temperature=0.9
        ).choices[0].message.content

        # Ses Üretimi
        audio = asyncio.run(generate_voice(response, rate=st.session_state.v_speed))

        # Geçmişe Ekle
        st.session_state.chat_history.append({
            "role": "assistant",
            "content": response,
            "audio": audio
        })

        # Sayfayı yenile ve otomatik oynat
        if audio:
            autoplay_audio(audio)
        st.rerun()
