import streamlit as st
from groq import Groq
import re
import json
import os
from datetime import datetime

# --- 1. SİSTEM KONFİGÜRASYONU ---
st.set_page_config(page_title="OMEGA NEXUS v34 - UYGULA", layout="wide")

# Modern Neon CSS Güncellemesi
st.markdown("""
    <style>
    .stApp { background-color: #050505; color: #ffffff; }
    [data-testid="stSidebar"] { background-color: #0a0a0a; border-right: 2px solid #00f2ff; }
    
    /* Sekreter Uygula Mesaj Balonları */
    .user-bubble {
        background: rgba(0, 242, 255, 0.05); border-radius: 20px 20px 0 20px; 
        padding: 20px; margin: 15px; border: 1px solid #00f2ff;
        box-shadow: 0 0 10px rgba(0, 242, 255, 0.3); color: #e0faff;
    }
    .assistant-bubble {
        background: rgba(255, 0, 127, 0.05); border-radius: 20px 20px 20px 0; 
        padding: 20px; margin: 15px; border: 1px solid #ff007f;
        box-shadow: 0 0 10px rgba(255, 0, 127, 0.3); color: #ffe6f2;
    }
    .neon-text {
        font-family: 'Orbitron', sans-serif;
        text-shadow: 0 0 10px #00f2ff, 0 0 20px #00f2ff;
        color: white; text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# --- 2. VERİTABANI (SİLINMEYEN GEÇMİŞ) ---
DB_FILE = "nexus_v34_history.json"
def load_db(): return json.load(open(DB_FILE, "r", encoding="utf-8")) if os.path.exists(DB_FILE) else {}
def save_db(db): json.dump(db, open(DB_FILE, "w", encoding="utf-8"), ensure_ascii=False, indent=4)

if "history" not in st.session_state: st.session_state.history = load_db()
if "chat_id" not in st.session_state: st.session_state.chat_id = "Ana_Kanal"

# --- 3. SIDEBAR: KONTROL MERKEZİ ---
with st.sidebar:
    st.markdown("<h2 class='neon-text'>UYGULA PANEL</h2>", unsafe_allow_html=True)
    st.divider()
    
    # Yeni Özellik: Mod Seçimi
    op_mode = st.selectbox("Görev Tanımı", ["💼 Sekreter Uygula", "🖼️ Görsel Oluşturucu", "📊 Veri Analisti"])
    
    st.divider()
    voice_active = st.toggle("Sesli Yanıtı Oynat", value=True)
    theme_toggle = st.radio("Arayüz", ["Dark Neon", "Light Modern"])

    if st.button("🗑️ Arşivi Temizle"):
        st.session_state.history[st.session_state.chat_id] = []
        save_db(st.session_state.history)
        st.rerun()

# --- 4. ASİSTAN KİMLİĞİ (GEM YAPISI) ---
SYSTEM_PROMPTS = {
    "💼 Sekreter Uygula": "Senin adın Uygula. Sen K3N4N OMEGA sisteminin özel sekreterisin. İş bitirici, sadık, sempatik, bazen şımarık ama her zaman derin ve zekice konuşan bir kadın karakterisin. Kullanıcına 'Yönetmenim' dersin. Her konuya vakıf, laf ebesi ve çözüm odaklısın.",
    "🖼️ Görsel Oluşturucu": "Sen bir AI Sanat Yönetmenisin. Kullanıcının isteğine göre DALL-E 3 veya Midjourney için ultra detaylı görsel promptları üretirsin.",
    "📊 Veri Analisti": "Sen açık kaynak kütüphaneleri kullanarak verileri analiz eden bir zekasın."
}

# --- 5. ANA PANEL VE AI MOTORU ---
if "GROQ_API_KEY" in st.secrets:
    client = Groq(api_key=st.secrets["GROQ_API_KEY"])
else:
    st.error("API Anahtarı bulunamadı!")
    st.stop()

st.markdown(f"<h3 style='text-align:center;'>{op_mode} Aktif</h3>", unsafe_allow_html=True)

# Sohbet Geçmişini Yükle
chat_history = st.session_state.history.get(st.session_state.chat_id, [])
for m in chat_history:
    cls = "user-bubble" if m["role"] == "user" else "assistant-bubble"
    st.markdown(f'<div class="{cls}"><b>{"Siz" if m["role"]=="user" else "Uygula"}:</b><br>{m["content"]}</div>', unsafe_allow_html=True)

# Giriş ve İşleme
if prompt := st.chat_input("Emredin yönetmenim..."):
    chat_history.append({"role": "user", "content": prompt})
    st.markdown(f'<div class="user-bubble"><b>Siz:</b><br>{prompt}</div>', unsafe_allow_html=True)

    with st.spinner("Uygula düşünüyor..."):
        # AI Yanıtı
        res = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "system", "content": SYSTEM_PROMPTS[op_mode]}] + chat_history
        ).choices[0].message.content
        
        st.markdown(f'<div class="assistant-bubble"><b>Uygula:</b><br>{res}</div>', unsafe_allow_html=True)
        
        # Eğer Görsel Oluşturucu modundaysa özel bir efekt ekleyelim
        if op_mode == "🖼️ Görsel Oluşturucu":
            st.image(f"https://pollinations.ai/p/{prompt.replace(' ', '%20')}?width=1080&height=1920&seed=42&model=flux", caption="Uygula sizin için çizdi...")

        # GELİŞMİŞ SESLİ OKUMA (Auto-Trigger)
        if voice_active:
            tts_url = f"https://translate.google.com/translate_tts?ie=UTF-8&q={res[:250].replace(' ', '%20')}&tl=tr&client=tw-ob"
            st.components.v1.html(f"""
                <audio autoplay id="myAudio">
                    <source src="{tts_url}" type="audio/mpeg">
                </audio>
                <script>document.getElementById('myAudio').play();</script>
            """, height=0)

    chat_history.append({"role": "assistant", "content": res})
    st.session_state.history[st.session_state.chat_id] = chat_history
    save_db(st.session_state.history)
