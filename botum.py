import streamlit as st  # 'i' harfi küçük olmalı
from groq import Groq
import os
import random

# ====================== 1. AYARLAR VE BAĞLANTILAR ======================
# Bu komut her zaman en üstte, diğer tüm st komutlarından önce gelmeli
st.set_page_config(
    page_title="Aşk-ı Muhabbet v10.2",
    layout="wide",
    page_icon="🎙️"
)

# API Kontrolü
if "GROQ_API_KEY" not in st.secrets:
    st.error("⚠️ GROQ_API_KEY eksik! Lütfen secrets.toml dosyasını kontrol et.")
    st.stop()

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

# ====================== 2. VERİ BAŞLATMA ======================
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# ====================== 3. TASARIM (CSS) ======================
st.markdown("""
    <style>
    .stApp { background-color: #08080e; color: #ffffff; }
    .host-card { padding: 20px; border-radius: 15px; margin-bottom: 20px; border-left: 10px solid; }
    .dilay-theme { background: linear-gradient(135deg, #320a2e 0%, #15051a 100%); border-color: #ff007f; }
    .mert-theme { background: linear-gradient(135deg, #0a2332 0%, #05101a 100%); border-color: #00d4ff; }
    .patron-bubble { background: rgba(0, 255, 157, 0.1); border-right: 4px solid #00ff9d; padding: 15px; border-radius: 10px; margin: 10px 0; text-align: right; }
    .live-text { color: red; font-weight: bold; animation: blinker 1.5s linear infinite; }
    @keyframes blinker { 50% { opacity: 0; } }
    </style>
    """, unsafe_allow_html=True)

# ====================== 4. YAN PANEL (REJİ) ======================
with st.sidebar:
    st.markdown("## 🎚️ REJİ MASASI")
    secilen_sunucu = st.radio("Mikrofon Kimde?", ["Dilay 💖", "Mert 🎙️"])
    yayin_tonu = st.select_slider("Yayın Enerjisi", options=["Sakin", "Duygusal", "Standart", "Coşkulu", "Muzip"])
    
    if st.button("🗑️ Yayını Sıfırla"):
        st.session_state.chat_history = []
        st.rerun()

# ====================== 5. ANA PANEL VE AKIŞ ======================
st.markdown(f"<h1>🎙️ AŞK-I MUHABBET <span class='live-text'>● CANLI</span></h1>", unsafe_allow_html=True)

for i, chat in enumerate(st.session_state.chat_history):
    if chat["role"] == "user":
        st.markdown(f'<div class="patron-bubble"><b>Patron:</b> {chat["content"]}</div>', unsafe_allow_html=True)
    else:
        tema = "dilay-theme" if chat["host"] == "Dilay 💖" else "mert-theme"
        st.markdown(f"""
            <div class="host-card {tema}">
                <b style="font-size: 1.2em;">{chat['host']}</b><br>
                <div style="margin-top: 10px;">{chat['content']}</div>
            </div>
        """, unsafe_allow_html=True)
        
        if chat.get("audio"):
            is_latest = (i == len(st.session_state.chat_history) - 1)
            # Benzersiz ID için key ekledik
            st.audio(chat["audio"], format="audio/wav", autoplay=is_latest, key=f"audio_v10_{i}")

# ====================== 6. AI VE SES TETİKLEME ======================
personalar = {
    "Dilay 💖": f"Sen Dilay'sın. Yayının neşesi, Patronun kıymetlisisin. Hitabın: 'Canım Patronum'. Modun: {yayin_tonu}.",
    "Mert 🎙️": f"Sen Mert'sin. Ağırbaşlı, samimi, beyefendi bir sunucusun. Hitabın: 'Üstadım'. Modun: {yayin_tonu}."
}

ses_dosyalari = {
    "Dilay 💖": "dilay_klon_sesim.wav",
    "Mert 🎙️": "mert_klon_sesim.wav"
}

if prompt := st.chat_input("Patron, yayına bir not bırak..."):
    st.session_state.chat_history.append({"role": "user", "content": prompt})
    
    with st.spinner("Mikrofon açılıyor..."):
        messages = [{"role": "system", "content": personalar[secilen_sunucu]}] + \
                   [{"role": m["role"], "content": m["content"]} for m in st.session_state.chat_history[-8:]]
        
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=messages,
            temperature=0.8
        ).choices[0].message.content

        audio_data = None
        if os.path.exists(ses_dosyalari[secilen_sunucu]):
            with open(ses_dosyalari[secilen_sunucu], "rb") as f:
                audio_data = f.read()

        st.session_state.chat_history.append({
            "role": "assistant",
            "host": secilen_sunucu,
            "content": response,
            "audio": audio_data
        })
        st.rerun()
