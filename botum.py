import streamlit as st
from groq import Groq
import re

# --- 1. SAYFA VE PANEL AYARLARI ---
st.set_page_config(page_title="K3N4N OMEGA PANEL", layout="wide", page_icon="🕹️")

# Görsel Stil (Premium Dark Mode)
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stSidebar { background-color: #161b22; border-right: 1px solid #30363d; }
    .stButton>button { width: 100%; border-radius: 5px; height: 3em; background-color: #238636; color: white; }
    .chat-card { padding: 20px; border-radius: 15px; background: #161b22; border: 1px solid #30363d; margin-bottom: 10px; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. SIDEBAR (KONTROL PANELİ) ---
with st.sidebar:
    st.image("https://img.icons8.com/clouds/200/000000/artificial-intelligence.png")
    st.title("OMEGA CONTROL")
    st.divider()
    
    # 1. ARAÇ SEÇİMİ
    app_mode = st.selectbox("Modül Seçin", ["🤖 Gölge Asistan", "🎨 Nick Tasarımcısı", "⚙️ Sistem Ayarları"])
    
    st.divider()
    
    # 2. KARAKTER/ROL SEÇİMİ (Sadece Asistan Modunda Aktif)
    if app_mode == "🤖 Gölge Asistan":
        st.subheader("Karakter Seçimi")
        persona = st.radio("Asistan Kişiliği", ["Laf Ebesi (Genel Kültür)", "Bilge (Strateji)", "Yazılım Dehası", "Radyocu (Duygusal)"])
        
        st.divider()
        st.subheader("Ses Ayarları")
        voice_active = st.checkbox("Sesli Yanıtları Aç", value=False)
    
    st.divider()
    if st.button("🗑️ Sohbeti Temizle"):
        st.session_state.messages = []
        st.rerun()

# --- 3. API VE HAFIZA YÖNETİMİ ---
if "messages" not in st.session_state:
    st.session_state.messages = []

if "GROQ_API_KEY" in st.secrets:
    api_key = st.secrets["GROQ_API_KEY"]
else:
    api_key = st.text_input("Sistem Anahtarı (API Key):", type="password")

if not api_key:
    st.warning("Lütfen API anahtarını girin.")
    st.stop()

client = Groq(api_key=api_key)

# --- 4. MODÜL ÇALIŞTIRICILAR ---

# --- MODÜL A: GÖLGE ASİSTAN ---
if app_mode == "🤖 Gölge Asistan":
    st.title(f"🕶️ {persona} Modu")
    
    # Sohbet Geçmişini Görüntüle
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    # Giriş Alanı
    if prompt := st.chat_input("Mesajınızı yazın..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            # Persona'ya göre talimat belirle
            instruction = f"Sen {persona} rolündesin. K3N4N OMEGA sisteminin parçasısın. Çok hızlı ve zekice cevap ver."
            
            chat_completion = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[{"role": "system", "content": instruction}] + 
                         [{"role": m["role"], "content": m["content"]} for m in st.session_state.messages]
            )
            response = str(chat_completion.choices[0].message.content)
            st.markdown(response)
            
            # Eğer sesli yanıt açıksa (Basit bir uyarı mekanizması şimdilik)
            if voice_active:
                st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3") # Örnek ses tetikleyici
        
        st.session_state.messages.append({"role": "assistant", "content": response})

# --- MODÜL B: NİCK TASARIMCISI ---
elif app_mode == "🎨 Nick Tasarımcısı":
    st.title("🎨 OMEGA Nick Designer")
    with st.container():
        nick_name = st.text_input("Metin Girin", "K3N4N")
        design_desc = st.text_area("Tasarım Tarifi", "Ken7 gold sparkle tarzında olsun...")
        if st.button("Render Et"):
            st.info("AI Tasarım kodlarını oluşturuyor...")
            # Burada önceki projedeki tasarım kodlarını çalıştıran fonksiyonu çağırabiliriz.

# --- MODÜL C: SİSTEM AYARLARI ---
elif app_mode == "⚙️ Sistem Ayarları":
    st.title("⚙️ Sistem Konfigürasyonu")
    st.write("Buradan API limitlerini, tema renklerini ve kullanıcı tercihlerini yönetebilirsiniz.")
    st.color_picker("Panel Tema Rengi", "#58a6ff")
