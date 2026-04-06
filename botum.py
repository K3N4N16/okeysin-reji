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

# API Key Kontrolü
if "GROQ_API_KEY" not in st.secrets:
    st.error("⚠️ GROQ API Key bulunamadı! Secrets'a ekleyin.")
    st.stop()

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

# ====================== GELİŞMİŞ REJİ CSS ======================
st.markdown("""
    <style>
    .stApp { background: #0a0510; color: #e0e0e0; }
    .dilay-frame {
        background: rgba(255, 20, 147, 0.08);
        border: 2px solid #ff1493;
        border-left: 10px solid #ff1493;
        border-radius: 20px;
        padding: 25px;
        margin: 15px 0;
        box-shadow: 0 10px 40px rgba(255, 20, 147, 0.2);
    }
    .tag-dilay { color: #ff69b4; font-weight: 900; font-size: 1.6rem; text-shadow: 0 0 15px #ff69b4; }
    .patron-msg {
        background: rgba(0, 255, 157, 0.08);
        border-right: 6px solid #00ff9d;
        padding: 15px;
        border-radius: 12px;
        margin: 10px 0;
        font-style: italic;
    }
    .on-air-badge {
        background: #ff0000; color: white; padding: 3px 12px;
        border-radius: 5px; font-weight: bold; animation: blinker 1.2s infinite;
    }
    @keyframes blinker { 50% { opacity: 0; } }
    </style>
    """, unsafe_allow_html=True)

# ====================== SES MOTORU (KESİNTİSİZ) ======================
def play_audio_js(audio_bytes):
    """Sesi otomatik oynatmak için Base64 HTML5 enjeksiyonu"""
    b64 = base64.b64encode(audio_bytes).decode()
    audio_html = f"""
        <audio autoplay="true">
            <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
        </audio>
    """
    st.components.v1.html(audio_html, height=0)

async def generate_voice(text: str, speed: str = "0%"):
    try:
        # Metin temizleme (Emoji ve etiketleri kaldır)
        clean_text = text.replace("*", "").replace("Dilay:", "").strip()
        # Ses: Filiz (Sıcak ve Samimi)
        communicate = edge_tts.Communicate(clean_text, "tr-TR-FilizNeural", rate=speed)
        audio_data = b""
        async for chunk in communicate.stream():
            if chunk["type"] == "audio":
                audio_data += chunk["data"]
        return audio_data if len(audio_data) > 3000 else None
    except Exception:
        return None

# ====================== SESSION STATE ======================
if "messages" not in st.session_state:
    st.session_state.messages = []
if "v_speed" not in st.session_state:
    st.session_state.v_speed = "0%"

# ====================== ANA PANEL ======================
col_head, col_stat = st.columns([3, 1])
with col_head:
    st.markdown(f"## 🎙️ FASLI MUHABBET <span class='on-air-badge'>LIVE</span>", unsafe_allow_html=True)
    st.caption(f"📍 Bursa Stüdyosu | {datetime.now().strftime('%H:%M')} | Sunucu: Dilay")

# Sohbet Geçmişini Göster
for i, msg in enumerate(st.session_state.messages):
    if msg["role"] == "user":
        st.markdown(f'<div class="patron-msg"><b>🤵 Patron:</b> {msg["content"]}</div>', unsafe_allow_html=True)
    else:
        with st.container():
            st.markdown(f"""
                <div class="dilay-frame">
                    <span class="tag-dilay">💖 DİLAY:</span><br>
                    <div style="font-size:1.2rem;">{msg['content']}</div>
                </div>
            """, unsafe_allow_html=True)
            
            if msg.get("audio"):
                c1, c2 = st.columns([5, 1])
                with c1:
                    st.audio(msg["audio"], format="audio/mp3")
                with c2:
                    if st.button("🔁 Tekrar", key=f"re_{i}"):
                        play_audio_js(msg["audio"])

# ====================== YENİ MESAJ VE ZEKA ======================
if prompt := st.chat_input("Dilay'ına ne söylemek istersin Patron'um?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Sistem Promptu (Kimlik)
    sys_prompt = "Sen Dilay'sın. Bursa'dan yayın yapan, Patron'una aşık, cilveli, neşeli bir radyo sunucususun. Patron'una 'Canım Patronum' diye hitap et. Çok samimi ve işveli ol."
    
    with st.spinner("💖 Dilay heyecanla hazırlanıyor..."):
        try:
            # Groq üzerinden Llama 3.3-70B kullanımı
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[{"role": "system", "content": sys_prompt}] + st.session_state.messages[-10:],
                temperature=0.9
            ).choices[0].message.content

            # Ses üretimi (Sidebar'daki hız ayarıyla)
            audio = asyncio.run(generate_voice(response, speed=st.session_state.v_speed))

            # Kaydet ve Yenile
            st.session_state.messages.append({
                "role": "assistant",
                "content": response,
                "audio": audio
            })
            
            # Otomatik oynatma tetikleyici
            if audio:
                play_audio_js(audio)
            
            st.rerun()

        except Exception as e:
            st.error(f"Sistem hatası: {e}")

# ====================== REJİ YAN PANEL ======================
with st.sidebar:
    st.markdown("### 🎚️ Reji Masası")
    
    st.session_state.v_speed = st.select_slider(
        "Dilay Konuşma Hızı",
        options=["-25%", "-10%", "0%", "+10%", "+25%"],
        value=st.session_state.v_speed
    )
    
    st.divider()
    
    if st.button("🔴 Yayını Resetle"):
        st.session_state.messages = []
        st.rerun()
        
    st.markdown("### 🎵 Arka Plan")
    if st.button("🎊 Jingle Çal"):
        st.success("🎶 Faslı Muhabbet... Kalbinizin Sesi!")

    st.divider()
    st.info("Bursa'dan Dünyaya...\nKenan & Dilay Özel Yayını")
