import streamlit as st
from groq import Groq
import os
import random
import asyncio
import edge_tts
import base64

# ====================== 1. GENEL YAPILANDIRMA ======================
st.set_page_config(
    page_title="Aşk-ı Muhabbet v11.0",
    layout="wide",
    page_icon="🎙️"
)

# Groq API Kontrolü
if "GROQ_API_KEY" not in st.secrets:
    st.error("⚠️ GROQ_API_KEY eksik! Lütfen secrets.toml dosyasını kontrol edin.")
    st.stop()

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

# ====================== 2. SES SİSTEMİ (EDGE-TTS) ======================
# Bu fonksiyon metni Microsoft seslerine dönüştürür
async def text_to_speech_edge(text, voice):
    communicate = edge_tts.Communicate(text, voice)
    audio_data = b""
    async for chunk in communicate.stream():
        if chunk["type"] == "audio":
            audio_data += chunk["data"]
    return audio_data

# ====================== 3. SESSION STATE (BELLEK) ======================
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# ====================== 4. TASARIM VE GÖRSEL (CSS) ======================
st.markdown("""
    <style>
    .stApp { background-color: #05050a; color: #ffffff; }
    .host-card { padding: 25px; border-radius: 20px; margin-bottom: 20px; border-left: 12px solid; transition: 0.3s; }
    .dilay-theme { background: linear-gradient(145deg, #2a0a25, #120315); border-color: #ff1493; box-shadow: 0 10px 30px rgba(255, 20, 147, 0.15); }
    .mert-theme { background: linear-gradient(145deg, #0a252a, #031215); border-color: #00d4ff; box-shadow: 0 10px 30px rgba(0, 212, 255, 0.15); }
    .patron-bubble { background: rgba(0, 255, 157, 0.05); border-right: 5px solid #00ff9d; padding: 15px; border-radius: 12px; margin: 10px 0; text-align: right; font-style: italic; }
    .live-badge { color: #ff0000; font-weight: 900; animation: blink 1.2s infinite; }
    @keyframes blink { 50% { opacity: 0.3; } }
    </style>
    """, unsafe_allow_html=True)

# ====================== 5. REJİ MASASI (SIDEBAR) ======================
with st.sidebar:
    st.header("🎚️ REJİ MASASI")
    st.divider()
    
    secilen_sunucu = st.radio("Mikrofon Kimde?", ["Dilay 💖", "Mert 🎙️"])
    
    yayin_enerjisi = st.select_slider(
        "Yayın Enerjisi",
        options=["Sakin", "Duygusal", "Standart", "Coşkulu", "Muzip"]
    )
    
    st.divider()
    st.markdown("### 📊 Yayın İstatistikleri")
    col_s1, col_s2 = st.columns(2)
    col_s1.metric("Dinleyici", f"{random.randint(20000, 25000):,}")
    col_s2.metric("Beğeni", f"{random.randint(1000, 5000):,}")
    
    if st.button("🗑️ Yayını Sıfırla"):
        st.session_state.chat_history = []
        st.rerun()

# ====================== 6. ANA YAYIN AKIŞI ======================
st.markdown(f"<h1>🎙️ AŞK-I MUHABBET <span class='live-badge'>● CANLI</span></h1>", unsafe_allow_html=True)

# Karakter ve Ses Tanımları
# Dilay: tr-TR-EmelNeural | Mert: tr-TR-AhmetNeural
personalar = {
    "Dilay 💖": {
        "prompt": f"Sen Dilay'sın. Aşk-ı Muhabbet'in sıcak, neşeli, cilveli kadın sunucususun. Patronuna 'Canım Patronum' dersin. Mod: {yayin_enerjisi}",
        "voice": "tr-TR-EmelNeural",
        "class": "dilay-theme"
    },
    "Mert 🎙️": {
        "prompt": f"Sen Mert'sin. Ağırbaşlı, samimi ve beyefendi bir erkek sunucusun. Patronuna 'Üstadım' dersin. Mod: {yayin_enerjisi}",
        "voice": "tr-TR-AhmetNeural",
        "class": "mert-theme"
    }
}

# Mesajları Ekrana Bas
for i, chat in enumerate(st.session_state.chat_history):
    if chat["role"] == "user":
        st.markdown(f'<div class="patron-bubble"><b>Patron:</b> {chat["content"]}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f"""
            <div class="host-card {chat['class']}">
                <b style="font-size: 1.2em;">{chat['host']}</b><br>
                <div style="margin-top: 10px;">{chat['content']}</div>
            </div>
        """, unsafe_allow_html=True)
        
        if chat.get("audio"):
            is_latest = (i == len(st.session_state.chat_history) - 1)
            st.audio(chat["audio"], format="audio/wav", autoplay=is_latest, key=f"voice_{i}")

# ====================== 7. AI VE SES ÜRETİMİ ======================
if prompt := st.chat_input("Patron, yayına bağlan..."):
    # 1. Patron mesajını kaydet
    st.session_state.chat_history.append({"role": "user", "content": prompt})
    
    with st.spinner(f"🎙️ {secilen_sunucu} cevap veriyor..."):
        # 2. Groq'tan yanıt al
        messages = [{"role": "system", "content": personalar[secilen_sunucu]["prompt"]}] + \
                   [{"role": m["role"], "content": m["content"]} for m in st.session_state.chat_history[-6:]]
        
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=messages,
            temperature=0.8
        )
        response_text = completion.choices[0].message.content

        # 3. Ses Üret (Edge-TTS)
        audio_content = asyncio.run(text_to_speech_edge(
            response_text, 
            personalar[secilen_sunucu]["voice"]
        ))

        # 4. Geçmişe kaydet
        st.session_state.chat_history.append({
            "role": "assistant",
            "host": secilen_sunucu,
            "content": response_text,
            "audio": audio_content,
            "class": personalar[secilen_sunucu]["class"]
        })
        
        st.rerun()

st.divider()
st.caption("Aşk-ı Muhabbet v11.0 | Altyapı: Groq & Microsoft Edge-TTS")
