import streamlit as st
from groq import Groq
import os
import random

# ====================== KONFİGÜRASYON ======================
st.set_page_config(
    page_title="Aşk-ı Muhabbet v10.0",
    layout="wide",
    page_icon="📻",
    initial_sidebar_state="expanded"
)

# API Anahtarı Kontrolü
if "GROQ_API_KEY" not in st.secrets:
    st.error("⚠️ GROQ API Key eksik! Lütfen secrets.toml dosyasını kontrol et.")
    st.stop()

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

# ====================== SES DOSYALARI YOLU ======================
# Applio ile eğittiğin sesleri bu isimlerle kök dizine koyabilirsin
SESLER = {
    "💖 Dilay": "dilay_klon_sesim.wav",
    "🎙️ Mert": "mert_klon_sesim.wav"
}

# ====================== TASARIM (CSS) ======================
st.markdown("""
    <style>
    .stApp { background: #0a0a12; color: #e0e0e0; }
    /* Dilay Kartı (Pembe/Mor Neon) */
    .dilay-card { 
        background: linear-gradient(135deg, #2d0b3d 0%, #1a0525 100%); 
        border-left: 10px solid #ff1493; 
        border-radius: 15px; padding: 25px; margin: 15px 0;
        box-shadow: 0 10px 30px rgba(255,20,147,0.2);
    }
    /* Mert Kartı (Mavi/Turkuaz Neon) */
    .mert-card { 
        background: linear-gradient(135deg, #0b2d3d 0%, #051a25 100%); 
        border-left: 10px solid #00d4ff; 
        border-radius: 15px; padding: 25px; margin: 15px 0;
        box-shadow: 0 10px 30px rgba(0,212,255,0.2);
    }
    .patron-card { 
        background: rgba(255, 255, 255, 0.05); 
        border-right: 4px solid #00ff9d; 
        padding: 15px; border-radius: 12px; margin: 10px 0; text-align: right; 
    }
    .live-indicator { color: #ff0000; font-weight: bold; animation: blink 1s infinite; }
    @keyframes blink { 50% { opacity: 0.2; } }
    </style>
    """, unsafe_allow_html=True)

# ====================== SESSION STATE ======================
if "history" not in st.session_state:
    st.session_state.history = []

# ====================== YAN PANEL (REJİ MASASI) ======================
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3058/3058983.png", width=100)
    st.title("🎚️ Reji Masası")
    
    selected_host = st.radio("Yayındaki Sunucu", ["💖 Dilay", "🎙️ Mert"])
    
    st.divider()
    mood = st.select_slider("Yayın Modu", options=["Duygusal", "Normal", "Enerjik", "Cilveli/Esprili"])
    
    st.divider()
    if st.button("🧹 Yayını Sıfırla"):
        st.session_state.history = []
        st.rerun()

# ====================== ANA EKRAN ======================
col1, col2 = st.columns([3, 1])
with col1:
    st.markdown(f"# 📻 AŞK-I MUHABBET <span class='live-indicator'>● CANLI YAYIN</span>", unsafe_allow_html=True)
    st.caption(f"Şu an mikrofon başında: **{selected_host}** | Mod: **{mood}**")
with col2:
    st.metric("Anlık Dinleyici", f"{random.randint(12000, 15500):,}", "+452")

# Sohbet Geçmişini Görüntüle
for msg in st.session_state.history:
    if msg["role"] == "user":
        st.markdown(f'<div class="patron-card"><b>🤵 Patron:</b> {msg["content"]}</div>', unsafe_allow_html=True)
    else:
        card_class = "dilay-card" if msg["host"] == "💖 Dilay" else "mert-card"
        st.markdown(f"""
            <div class="{card_class}">
                <b style="font-size:1.2rem;">{msg['host']}:</b><br>
                <div style="margin-top:10px;">{msg['content']}</div>
            </div>
        """, unsafe_allow_html=True)
        if msg.get("audio"):
            st.audio(msg["audio"], format="audio/wav", autoplay=True)

# ====================== AI VE SES MANTIĞI ======================
# Karakter ayarları
prompts = {
    "💖 Dilay": f"Sen Dilay'sın. Aşk-ı Muhabbet'in neşeli, samimi, biraz cilveli kadın sunucususun. Patronuna 'Canım Patronum' diye hitap et. Şu an {mood} bir ruh halindesin.",
    "🎙️ Mert": f"Sen Mert'sin. Aşk-ı Muhabbet'in ağırbaşlı, tok sesli, beyefendi erkek sunucususun. Patronuna 'Üstadım' veya 'Patron' diye hitap et. Şu an {mood} bir ruh halindesin."
}

if prompt := st.chat_input("Yayına bağlan, Patron..."):
    # Patron mesajını ekle
    st.session_state.history.append({"role": "user", "content": prompt})
    
    with st.spinner(f"🎙️ {selected_host} hazırlanıyor..."):
        # Groq'tan yanıt al
        messages = [{"role": "system", "content": prompts[selected_host]}] + \
                   [{"role": h["role"], "content": h["content"]} for h in st.session_state.history[-10:]]
        
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=messages,
            temperature=0.9 if mood == "Enerjik" else 0.7
        )
        response_text = completion.choices[0].message.content

        # Applio klon ses dosyasını oku
        audio_path = SESLER[selected_host]
        audio_data = None
        if os.path.exists(audio_path):
            with open(audio_path, "rb") as f:
                audio_data = f.read()
        else:
            st.warning(f"⚠️ {audio_path} bulunamadı. Lütfen Applio'dan aldığın klon sesi klasöre ekle.")

        # Geçmişe ekle
        st.session_state.history.append({
            "role": "assistant",
            "host": selected_host,
            "content": response_text,
            "audio": audio_data
        })
        
        st.rerun()

st.divider()
st.markdown("<center style='opacity:0.5'>Aşk-ı Muhabbet v10.0 | Tasarım ve Kod: K3N4N</center>", unsafe_allow_html=True)
