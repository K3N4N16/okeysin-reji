import streamlit as st
from groq import Groq
import re
import json
import os
from datetime import datetime
import urllib.parse

# --- 1. SİSTEM & TASARIM ---
st.set_page_config(page_title="OMEGA v36 - SOUND", layout="wide")

if 'theme' not in st.session_state: st.session_state.theme = "Dark Neon"

# Neon CSS ve Buton Stilleri
st.markdown(f"""
    <style>
    .stApp {{ background-color: #050505; color: #00f2ff; }}
    [data-testid="stSidebar"] {{ background-color: #0a0a0a; border-right: 2px solid #ff007f; }}
    
    .assistant-bubble {{
        background: rgba(255, 0, 127, 0.05); border: 1px solid #ff007f;
        border-radius: 15px; padding: 20px; margin: 10px 0;
        box-shadow: 0 0 15px rgba(255, 0, 127, 0.2);
    }}
    
    .action-bar {{
        display: flex; gap: 15px; margin-top: 10px; padding-top: 10px; border-top: 1px solid #333;
    }}
    
    .icon-btn {{
        cursor: pointer; color: #ff007f; font-size: 1.2rem; transition: 0.3s;
        text-decoration: none; display: flex; align-items: center; gap: 5px;
    }}
    .icon-btn:hover {{ color: #00f2ff; text-shadow: 0 0 10px #00f2ff; }}
    </style>
    
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
""", unsafe_allow_html=True)

# --- 2. FONKSİYONLAR ---
def load_db():
    if os.path.exists("omega_v36.json"):
        with open("omega_v36.json", "r", encoding="utf-8") as f: return json.load(f)
    return {}

def save_db(db):
    with open("omega_v36.json", "w", encoding="utf-8") as f: json.dump(db, f, indent=4, ensure_ascii=False)

if "db" not in st.session_state: st.session_state.db = load_db()
if "active_id" not in st.session_state: st.session_state.active_id = "Genel Sohbet"

# --- 3. SIDEBAR ---
with st.sidebar:
    st.title("🎙️ OMEGA REJİ")
    persona = st.selectbox("Kişilik", ["🌸 Sekreter Uygula", "🎙️ Can Radyocu", "🧠 Bilge Eğitmen"])
    st.divider()
    if st.button("➕ Yeni Başlat"):
        new_id = f"{persona} | {datetime.now().strftime('%H:%M')}"
        st.session_state.db[new_id] = []
        st.session_state.active_id = new_id
    
    history = list(st.session_state.db.keys())
    if history:
        st.session_state.active_id = st.selectbox("Arşiv", history[::-1])

# --- 4. ANA EKRAN & AI ---
client = Groq(api_key=st.secrets["GROQ_API_KEY"])
st.title(f"✨ {persona}")

messages = st.session_state.db.get(st.session_state.active_id, [])

# Mesajları ve Fonksiyonel Butonları Listele
for i, m in enumerate(messages):
    if m["role"] == "user":
        st.markdown(f'<div style="text-align:right; color:#00f2ff; margin:10px;"><b>Siz:</b><br>{m["content"]}</div>', unsafe_allow_html=True)
    else:
        # Asistan Mesaj Kartı
        text = m["content"]
        safe_text = urllib.parse.quote(text[:300]) # Ses için metni hazırla
        
        # HTML Kart Yapısı
        st.markdown(f"""
            <div class="assistant-bubble">
                <b>Uygula:</b><br>{text}
                <div class="action-bar">
                    <a href="https://translate.google.com/translate_tts?ie=UTF-8&q={safe_text}&tl=tr&client=tw-ob" target="audio_frame" class="icon-btn" title="Dinle">
                        <i class="fas fa-volume-up"></i>
                    </a>
                    <span class="icon-btn" onclick="navigator.clipboard.writeText(`{text}`)" title="Kopyala">
                        <i class="fas fa-copy"></i>
                    </span>
                    <a href="data:text/plain;charset=utf-8,{safe_text}" download="omega_mesaj.txt" class="icon-btn" title="İndir">
                        <i class="fas fa-download"></i>
                    </a>
                </div>
            </div>
        """, unsafe_allow_html=True)

# Görünmez ses oynatıcı iframe
st.write('<iframe name="audio_frame" style="display:none;"></iframe>', unsafe_allow_html=True)

# Girdi Alanı
if prompt := st.chat_input("Emredin yönetmenim..."):
    messages.append({"role": "user", "content": prompt})
    st.rerun() # Arayüzü güncellemek için

# AI Yanıt Üretimi (Eğer son mesaj kullanıcıdansa)
if messages and messages[-1]["role"] == "user":
    with st.spinner("Uygula yanıtlıyor..."):
        behavior = "Sen Uygula'sın, işveli ve zeki sekretersin." if persona == "🌸 Sekreter Uygula" else "Sen Can'sın, karizmatik radyocusun."
        res = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "system", "content": behavior}] + messages
        ).choices[0].message.content
        
        messages.append({"role": "assistant", "content": res})
        st.session_state.db[st.session_state.active_id] = messages
        save_db(st.session_state.db)
        st.rerun()
