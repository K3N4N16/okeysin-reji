import streamlit as st
from groq import Groq
import edge_tts
import asyncio
import io
import re
from datetime import datetime
import random

# ====================== SAYFA AYARLARI ======================
st.set_page_config(
    page_title="Faslı Muhabbet v7.0",
    layout="wide",
    page_icon="🎙️"
)

# API Key Kontrolü
if "GROQ_API_KEY" not in st.secrets:
    st.error("⚠️ GROQ API Key eksik! Lütfen Streamlit Secrets'a ekleyin.")
    st.stop()

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

# ====================== SES MOTORU (GÜNCEL & STABİL) ======================
async def text_to_speech_edge(text):
    """En popüler AI sesi Dilara ile hata korumalı ses üretimi"""
    try:
        # Metni temizle (Yıldızlar, fazla emojiler ve semboller AI sesini bozabilir)
        clean_text = re.sub(r'[*_#~>]', '', text).strip()
        
        if not clean_text:
            return None

        # tr-TR-DilaraNeural: En popüler, akıcı ve doğal Türkçe ses
        voice = "tr-TR-DilaraNeural"
        communicate = edge_tts.Communicate(clean_text, voice, rate="+7%", pitch="+2Hz")
        
        audio_stream = io.BytesIO()
        async for chunk in communicate.stream():
            if chunk["type"] == "audio":
                audio_stream.write(chunk["data"])
        
        return audio_stream.getvalue()
    except Exception as e:
        print(f"Ses Hatası: {e}")
        return None

# ====================== MODERN UI (CSS) ======================
st.markdown("""
    <style>
    .stApp { background: #0d0d0d; color: #e0e0e0; }
    .dilay-box {
        background: linear-gradient(145deg, #1e0035, #0a0014);
        border-left: 6px solid #ff007f;
        border-radius: 15px;
        padding: 25px;
        margin: 20px 0;
        box-shadow: 0 10px 25px rgba(255, 0, 127, 0.2);
    }
    .patron-box {
        background: #1a1a1a;
        border-right: 4px solid #00f2fe;
        padding: 15px;
        border-radius: 12px;
        margin: 10px 0;
        text-align: right;
    }
    .live-dot {
        height: 10px; width: 10px;
        background-color: #ff0000;
        border-radius: 50%;
        display: inline-block;
        animation: blink 1s infinite;
    }
    @keyframes blink { 50% { opacity: 0; } }
    </style>
    """, unsafe_allow_html=True)

# ====================== SESSION STATE ======================
if "messages" not in st.session_state:
    st.session_state.messages = []

# ====================== ÜST PANEL ======================
col1, col2 = st.columns([4, 1])
with col1:
    st.markdown(f"## <span class='live-dot'></span> FASLI MUHABBET | CANLI", unsafe_allow_html=True)
    st.caption(f"📍 Bursa Stüdyoları • {datetime.now().strftime('%H:%M')} • Ses: Dilara AI")
with col2:
    st.metric("Dinleyici", f"{random.randint(9200, 11500):,}")

# ====================== SOHBET GEÇMİŞİ ======================
for i, msg in enumerate(st.session_state.messages):
    if msg["role"] == "user":
        st.markdown(f'<div class="patron-box"><b>Patron Kenan:</b> {msg["content"]}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f"""
            <div class="dilay-box">
                <b style="color:#ff007f; font-size:1.3rem;">💖 DİLAY:</b><br>
                <div style="margin-top:10px; font-size:1.15rem;">{msg['content']}</div>
            </div>
        """, unsafe_allow_html=True)
        
        if msg.get("audio"):
            st.audio(msg["audio"], format="audio/mp3", autoplay=(i == len(st.session_state.messages)-1))

# ====================== DİLAY KARAKTER PROMPT ======================
system_prompt = """
Sen Dilay'sın. Radyo dünyasının en neşeli, samimi ve biraz da cilveli sunucususun. 
Patronun Kenan'a (ona bazen Paşam, bazen Canım Patronum dersin) çok bağlısın.
Cümlelerin doğal olsun, radyo atmosferini hissettir. 
Asla teknik detay verme, sadece karakterinle konuş.
"""

# ====================== MESAJ GİRİŞİ ======================
if prompt := st.chat_input("Dilay'a bir şeyler söyle patron..."):
    # Patron mesajını ekle
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    with st.spinner("🎤 Dilay mikrofonu açıyor..."):
        try:
            # 1. Metin Üretimi (Groq)
            history = [{"role": "system", "content": system_prompt}] + st.session_state.messages[-10:]
            completion = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=history,
                temperature=0.85
            )
            response_text = completion.choices[0].message.content

            # 2. Ses Üretimi (Edge-TTS)
            # Streamlit içinde asenkron fonksiyonu çağırmak için:
            audio_bytes = asyncio.run(text_to_speech_edge(response_text))

            # 3. Geçmişe Kaydet
            st.session_state.messages.append({
                "role": "assistant", 
                "content": response_text,
                "audio": audio_bytes
            })
            
            st.rerun()

        except Exception as e:
            st.error(f"⚠️ Yayında bir parazit var: {e}")

# ====================== SIDEBAR ======================
with st.sidebar:
    st.title("🎚️ Yayın Kontrol")
    if st.button("🗑️ Yayını Sıfırla"):
        st.session_state.messages = []
        st.rerun()
    
    st.divider()
    st.info("💡 Not: Sesin otomatik çalması için tarayıcıda sayfa üzerine bir kez tıklamanız gerekebilir.")
    st.caption("Faslı Muhabbet v7.0 - Powered by Edge AI")
