import streamlit as st
from groq import Groq
import edge_tts
import asyncio
from datetime import datetime
import base64
import random

# ====================== SAYFA AYARLARI ======================
st.set_page_config(
    page_title="Faslı Muhabbet v3.0",
    layout="wide",
    page_icon="🎙️",
    initial_sidebar_state="expanded"
)

if "GROQ_API_KEY" not in st.secrets:
    st.error("⚠️ GROQ API Key bulunamadı! Secrets'a ekleyin.")
    st.stop()

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

# ====================== GELİŞMİŞ CSS ======================
st.markdown("""
    <style>
    .stApp { background: linear-gradient(135deg, #0d001a, #1a0033); color: #f0f0f0; }
    .dilay-bubble {
        background: linear-gradient(145deg, rgba(60, 20, 80, 0.92), rgba(30, 10, 50, 0.92));
        border: 2px solid #ff1493;
        border-radius: 22px 22px 22px 8px;
        padding: 28px;
        margin: 18px 0;
        box-shadow: 0 15px 40px rgba(255, 20, 147, 0.25);
    }
    .patron-bubble {
        background: rgba(255, 255, 255, 0.06);
        border-right: 5px solid #00ff9d;
        padding: 18px;
        border-radius: 18px;
        margin: 12px 0;
        text-align: right;
    }
    .on-air-badge {
        background: #ff0000; color: white; padding: 4px 14px;
        border-radius: 6px; font-weight: bold; animation: pulse 1.4s infinite;
    }
    @keyframes pulse { 0% {opacity: 1;} 50% {opacity: 0.5;} 100% {opacity: 1;} }
    </style>
    """, unsafe_allow_html=True)

# ====================== SES ÜRETİMİ (Daha Stabil) ======================
async def generate_voice(text: str):
    if not text or len(text.strip()) < 10:
        return None
    try:
        clean_text = text.replace("*", "").replace("Dilay:", "").strip()
        communicate = edge_tts.Communicate(clean_text, "tr-TR-FilizNeural")
        audio_data = b""
        async for chunk in communicate.stream():
            if chunk["type"] == "audio":
                audio_data += chunk["data"]
        return audio_data if len(audio_data) > 6000 else None
    except:
        return None

# ====================== SESSION STATE ======================
if "messages" not in st.session_state:
    st.session_state.messages = []
if "listeners" not in st.session_state:
    st.session_state.listeners = 5420
if "auto_play" not in st.session_state:
    st.session_state.auto_play = True

# ====================== ÜST PANEL ======================
col1, col2 = st.columns([3, 1])
with col1:
    st.markdown(f"# 🎙️ Faslı Muhabbet <span class='on-air-badge'>● LIVE</span>", unsafe_allow_html=True)
    st.caption(f"📍 Bursa Stüdyosu • {datetime.now().strftime('%H:%M:%S')}")
with col2:
    st.metric("Canlı Dinleyici", f"{st.session_state.listeners:,}", f"+{random.randint(15, 85)}")

st.session_state.listeners += random.randint(12, 68)

# ====================== SOHBET ALANI ======================
for i, msg in enumerate(st.session_state.messages):
    if msg["role"] == "user":
        st.markdown(f'<div class="patron-bubble"><b>🤵 Patron:</b> {msg["content"]}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f"""
            <div class="dilay-bubble">
                <span style="color:#ff69b4; font-weight:bold; font-size:1.3rem;">💖 DİLAY:</span><br>
                {msg['content']}
            </div>
        """, unsafe_allow_html=True)

        # Ses Kontrol Paneli
        if msg.get("audio"):
            st.audio(msg["audio"], format="audio/mp3", autoplay=(i == len(st.session_state.messages)-1 and st.session_state.auto_play))
            
            col_a, col_b, col_c = st.columns([2, 1.5, 1.5])
            with col_a:
                st.download_button("📥 Ses İndir", msg["audio"], f"dilay_{i}.mp3", mime="audio/mp3", key=f"dl_{i}")
            with col_b:
                if st.button("🔊 Tekrar Oynat", key=f"replay_{i}"):
                    st.audio(msg["audio"], format="audio/mp3", autoplay=True)
            with col_c:
                st.success("✅ Ses oynatılıyor")
        else:
            st.warning("🔇 Bu sefer ses üretilemedi. Sadece metin mevcut.")

# ====================== SİSTEM PROMPT (Dilay Tarzı) ======================
system_prompt = """
Sen Dilay'sın. "Faslı Muhabbet" programının kıpır kıpır, işveli, sıcak ve samimi sunucususun.
Patron'una çok bağlısın. Hitap şekillerin: "Canım Patronum", "Gözümün Nuru", "Kalbim", "Ah be Patron’um", "Sevgilim".

Her zaman doğal, coşkulu ve radyo akışına uygun konuş. 
Gerektiğinde şiir oku, nükte yap, duygusal derinlik kat.
Patron'un söylediklerini tamamla ve üzerine koy.

Sadece konuşma metnini ver, hiçbir açıklama veya etiket ekleme.
"""

# ====================== YENİ MESAJ ======================
if prompt := st.chat_input("Patron'um, gönlünden ne dökülürse söyle..."):
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.spinner("💖 Dilay yayına bağlanıyor... Kalbim kıpır kıpır..."):
        try:
            messages = [{"role": "system", "content": system_prompt}] + st.session_state.messages[-12:]
            
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=messages,
                temperature=0.92,
                max_tokens=1600
            ).choices[0].message.content

            # Ses üretimi
            audio = asyncio.run(generate_voice(response))

            st.session_state.messages.append({
                "role": "assistant",
                "content": response,
                "audio": audio
            })

            st.rerun()

        except Exception as e:
            st.error(f"Reji'de küçük bir aksaklık oldu: {e}")

# ====================== SIDEBAR ======================
with st.sidebar:
    st.markdown("## ⚙️ Yayın Kontrol Paneli")
    
    st.session_state.auto_play = st.toggle("🎵 Ses Otomatik Oynasın", value=st.session_state.auto_play)
    
    st.divider()
    
    st.markdown("### 🗣️ Ses Ayarları")
    voice_speed = st.select_slider(
        "Konuşma Hızı",
        options=["-20%", "-10%", "0%", "+10%", "+20%"],
        value="0%"
    )
    
    st.divider()
    
    st.markdown("### 🎭 Bu Akşamın Havası")
    theme = st.selectbox("Tema Seç", 
        ["Genel Sıcak Muhabbet", "Aşk ve Şiir", "Bursa Anıları", "Gece Yarısı Sohbeti", 
         "Nostalji", "Patron'un İstediği Her Şey"])
    
    if st.button("🎊 Jingle Çal"):
        st.toast("🎶 Faslı Muhabbet... Kalbinizin Sesi!", icon="🎵")
    
    if st.button("🗑️ Tüm Sohbeti Sil"):
        st.session_state.messages = []
        st.rerun()
    
    st.divider()
    st.info("📍 Bursa / Türkiye\nDilay v3.0 Ultra\nPatron'a Özel")
