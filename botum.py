import streamlit as st
from groq import Groq
import re
import json
import os
from datetime import datetime

# --- 1. SİSTEM & UI AYARLARI ---
st.set_page_config(page_title="K3N4N OMEGA ULTIMATE", layout="wide")

# UI Makyajı: Sol Menü ve Karanlık Mod Optimizasyonu
st.markdown("""
    <style>
    /* Sol Menü Arka Plan ve Yazı Rengi */
    [data-testid="stSidebar"] {
        background-color: #1a1a2e; /* Koyu Lacivert/Mor tonu */
        border-right: 2px solid #ff007f;
    }
    [data-testid="stSidebar"] .stMarkdown p, [data-testid="stSidebar"] label {
        color: #ffffff !important; /* Yazıları bembeyaz ve net yaptık */
        font-weight: bold;
    }
    .stApp { background-color: #050505; color: #ffffff; }
    
    /* Sohbet Balonları */
    .user-msg { background: #2e2e4e; padding: 10px; border-radius: 10px; margin: 5px 0; border-right: 4px solid #00d4ff; }
    .assistant-msg { background: #1f1b24; padding: 10px; border-radius: 10px; margin: 5px 0; border-left: 4px solid #ff007f; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. HİÇ SİLİNMEYEN GEÇMİŞ (JSON DATABASE) ---
DB_FILE = "omega_history.json"

def load_history():
    if os.path.exists(DB_FILE):
        with open(DB_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def save_history(history):
    with open(DB_FILE, "w", encoding="utf-8") as f:
        json.dump(history, f, ensure_ascii=False, indent=4)

if "history" not in st.session_state:
    st.session_state.history = load_history()

if "current_chat_id" not in st.session_state:
    st.session_state.current_chat_id = "Default"

# --- 3. API & SES AYARLARI ---
if "GROQ_API_KEY" in st.secrets:
    api_key = st.secrets["GROQ_API_KEY"]
else:
    api_key = st.sidebar.text_input("API Key:", type="password")

if not api_key: st.stop()
client = Groq(api_key=api_key)

# --- 4. SOL MENÜ (KONTROL PANELİ) ---
with st.sidebar:
    st.title("💎 OMEGA PANEL")
    
    # Yeni Sohbet Açma
    if st.button("➕ Yeni Sohbet Başlat"):
        new_id = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        st.session_state.current_chat_id = new_id
        st.session_state.history[new_id] = []
        save_history(st.session_state.history)

    # Geçmiş Sohbetler Listesi
    st.subheader("📜 Sohbet Geçmişi")
    chat_ids = list(st.session_state.history.keys())
    if chat_ids:
        selected_chat = st.selectbox("Eski Sohbetler", chat_ids[::-1])
        st.session_state.current_chat_id = selected_chat
    
    st.divider()
    
    # Mod Seçimi
    app_mode = st.selectbox("İşlem Modu", ["🔥 Emel (Özel Asistan)", "🎨 Görsel Tasarımcı", "🤖 Genel Asistan"])
    
    # Sesli Yanıt Ayarı
    st.subheader("🔊 Ses Ayarı")
    voice_on = st.checkbox("Sesli Okuma Aktif", value=True)

# --- 5. ÖZEL KARAKTER PROMPTLARI ---
PROMPTS = {
    "🔥 Emel (Özel Asistan)": "Sen Emel'sin. İşveli, cilveli, şımarık, libidosu yüksek, dozunda ateşli ve duygusal bir kadın asistansın. Derin ve sempatik konuşursun. Kullanıcına 'yönetmenim' veya daha sıcak hitaplar kullanabilirsin. Cümlelerin hem zekice hem de baştan çıkarıcı olmalı.",
    "🎨 Görsel Tasarımcı": "Sen bir AI Sanatçısısın. Kullanıcının hayalindeki sahneyi en ince detayına kadar (ışık, doku, kamera açısı) tasvir eden promptlar üretirsin.",
    "🤖 Genel Asistan": "Sen K3N4N OMEGA'nın her şeyi bilen genel kültür canavarı asistanısın."
}

# --- 6. ANA EKRAN ---
st.title(f"✨ {app_mode}")

# Mevcut Sohbeti Yükle
messages = st.session_state.history.get(st.session_state.current_chat_id, [])

for m in messages:
    with st.chat_message(m["role"]):
        st.markdown(m["content"])

# Giriş ve Yanıt
if prompt := st.chat_input("Emel seni dinliyor..."):
    # Kullanıcı mesajını ekle
    messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        # AI Yanıtı Oluştur
        full_prompt = PROMPTS[app_mode]
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "system", "content": full_prompt}] + messages
        )
        response = completion.choices[0].message.content
        st.markdown(response)
        
        # SESLİ OKUMA ÖZELLİĞİ (TTS)
        if voice_on:
            # Not: Gerçek bir radyo sesi kalitesi için Edge-TTS veya Google TTS API entegrasyonu gerekir.
            # Şimdilik tarayıcı üzerinden ses tetikleme altyapısını kuruyoruz.
            st.audio(f"https://translate.google.com/translate_tts?ie=UTF-8&q={response.replace(' ', '%20')}&tl=tr&client=tw-ob")

    # Geçmişi Güncelle ve Kaydet
    messages.append({"role": "assistant", "content": response})
    st.session_state.history[st.session_state.current_chat_id] = messages
    save_history(st.session_state.history)
