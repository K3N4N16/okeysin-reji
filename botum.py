import streamlit as st
from groq import Groq
import os
import random

# ====================== SİSTEM AYARLARI ======================
st.set_page_config(
    page_title="Aşk-ı Muhabbet v10.1",
    layout="wide",
    page_icon="🎙️",
    initial_sidebar_state="expanded"
)

# Groq API Bağlantısı
if "GROQ_API_KEY" not in st.secrets:
    st.error("⚠️ GROQ_API_KEY bulunamadı! Lütfen secrets.toml dosyasını kontrol et.")
    st.stop()

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

# ====================== STİL VE TASARIM (CSS) ======================
st.markdown("""
    <style>
    /* Ana Tema */
    .stApp { background-color: #08080e; color: #ffffff; }
    
    /* Sunucu Kartları */
    .host-card {
        padding: 20px;
        border-radius: 15px;
        margin-bottom: 20px;
        border-left: 10px solid;
    }
    .dilay-theme { 
        background: linear-gradient(135deg, #320a2e 0%, #15051a 100%); 
        border-color: #ff007f;
        box-shadow: 0 10px 25px rgba(255, 0, 127, 0.2);
    }
    .mert-theme { 
        background: linear-gradient(135deg, #0a2332 0%, #05101a 100%); 
        border-color: #00d4ff;
        box-shadow: 0 10px 25px rgba(0, 212, 255, 0.2);
    }
    
    /* Patron Mesajı */
    .patron-bubble {
        background: rgba(0, 255, 157, 0.1);
        border-right: 4px solid #00ff9d;
        padding: 15px;
        border-radius: 10px;
        margin: 10px 0;
        text-align: right;
    }
    
    /* Canlı Yayın Efekti */
    .live-text { color: red; font-weight: bold; animation: blinker 1.5s linear infinite; }
    @keyframes blinker { 50% { opacity: 0; } }
    </style>
    """, unsafe_allow_html=True)

# ====================== VERİ YÖNETİMİ ======================
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# ====================== YAN PANEL (REJİ MASASI) ======================
with st.sidebar:
    st.markdown("## 🎚️ REJİ MASASI")
    st.divider()
    
    # Karakter Seçimi
    secilen_sunucu = st.radio("Mikrofon Kimde?", ["Dilay 💖", "Mert 🎙️"])
    
    # Yayın Tonu
    yayin_tonu = st.select_slider(
        "Yayın Enerjisi",
        options=["Sakin", "Duygusal", "Standart", "Coşkulu", "Muzip"]
    )
    
    st.divider()
    if st.button("🗑️ Yayını Sıfırla"):
        st.session_state.chat_history = []
        st.rerun()

# ====================== ANA PANEL ======================
c1, c2 = st.columns([4, 1])
with c1:
    st.markdown(f"<h1>🎙️ AŞK-I MUHABBET <span class='live-text'>● CANLI</span></h1>", unsafe_allow_html=True)
with c2:
    st.metric("Dinleyici", f"{random.randint(15000, 22000):,}")

# Sohbet Akışı
for chat in st.session_state.chat_history:
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
            st.audio(chat["audio"], format="audio/wav", autoplay=True)

# ====================== AI VE SES TETİKLEME ======================
# Karakter Tanımları
personalar = {
    "Dilay 💖": f"Sen Dilay'sın. Yayının neşesi, Patronun kıymetlisisin. Hitabın: 'Canım Patronum'. Modun: {yayin_tonu}.",
    "Mert 🎙️": f"Sen Mert'sin. Ağırbaşlı, samimi, beyefendi bir sunucusun. Hitabın: 'Üstadım' veya 'Patron'. Modun: {yayin_tonu}."
}

# Ses Dosyaları (Applio'dan gelen klonlar)
ses_dosyalari = {
    "Dilay 💖": "dilay_klon_sesim.wav",
    "Mert 🎙️": "mert_klon_sesim.wav"
}

if prompt := st.chat_input("Patron, yayına bir not bırak..."):
    # Geçmişe ekle
    st.session_state.chat_history.append({"role": "user", "content": prompt})
    
    # AI Yanıtı
    with st.spinner(f"{secilen_sunucu} hazırlanıyor..."):
        messages = [{"role": "system", "content": personalar[secilen_sunucu]}] + \
                   [{"role": m["role"], "content": m["content"]} for m in st.session_state.chat_history[-8:]]
        
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=messages,
            temperature=0.8
        ).choices[0].message.content

        # Ses Verisi Hazırlama
        audio_data = None
        target_audio = ses_dosyalari[secilen_sunucu]
        if os.path.exists(target_audio):
            with open(target_audio, "rb") as f:
                audio_data = f.read()
        
        # Geçmişe Yanıtı ve Sesi Ekle
        st.session_state.chat_history.append({
            "role": "assistant",
            "host": secilen_sunucu,
            "content": response,
            "audio": audio_data
        })
        
        st.rerun()
