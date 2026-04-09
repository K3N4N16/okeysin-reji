import streamlit as st
from groq import Groq
import re
import json
import os
from datetime import datetime

# --- 1. SİSTEM VE TEMA YÖNETİMİ ---
st.set_page_config(page_title="K3N4N OMEGA v35", layout="wide")

if 'theme' not in st.session_state:
    st.session_state.theme = "Dark Neon"

def get_theme_css(theme_name):
    if theme_name == "Dark Neon":
        return {
            "bg": "#050505", "sidebar": "#0a0a0a", "text": "#00f2ff",
            "bubble_u": "rgba(0, 242, 255, 0.1)", "bubble_a": "rgba(255, 0, 127, 0.1)",
            "border_u": "#00f2ff", "border_a": "#ff007f"
        }
    else:
        return {
            "bg": "#ffffff", "sidebar": "#f0f2f6", "text": "#1a1a1a",
            "bubble_u": "#e1f5fe", "bubble_a": "#fce4ec",
            "border_u": "#01579b", "border_a": "#c2185b"
        }

t = get_theme_css(st.session_state.theme)

st.markdown(f"""
    <style>
    .stApp {{ background-color: {t['bg']}; color: {t['text']}; }}
    [data-testid="stSidebar"] {{ background-color: {t['sidebar']}; border-right: 2px solid {t['border_a']}; }}
    .stSidebar [data-testid="stMarkdownContainer"] p {{ color: {t['text']} !important; font-weight: bold; }}
    
    .user-bubble {{
        background: {t['bubble_u']}; border: 1px solid {t['border_u']};
        border-radius: 15px 15px 0 15px; padding: 15px; margin: 10px;
        box-shadow: 0 0 10px {t['bubble_u']}; color: {t['text']};
    }}
    .assistant-bubble {{
        background: {t['bubble_a']}; border: 1px solid {t['border_a']};
        border-radius: 15px 15px 15px 0; padding: 15px; margin: 10px;
        box-shadow: 0 0 10px {t['bubble_a']}; color: {t['text']};
    }}
    </style>
""", unsafe_allow_html=True)

# --- 2. KALICI HAFIZA MOTORU (JSON DB) ---
DB_FILE = "omega_v35_master.json"

def load_db():
    if os.path.exists(DB_FILE):
        with open(DB_FILE, "r", encoding="utf-8") as f: return json.load(f)
    return {}

def save_db(db):
    with open(DB_FILE, "w", encoding="utf-8") as f: json.dump(db, f, indent=4, ensure_ascii=False)

if "db" not in st.session_state: st.session_state.db = load_db()
if "active_id" not in st.session_state: st.session_state.active_id = None

# --- 3. SIDEBAR (REJİ MASASI) ---
with st.sidebar:
    st.title("🕹️ OMEGA MASTER")
    
    st.session_state.theme = st.selectbox("Tema Seçimi", ["Dark Neon", "Light Modern"])
    
    st.divider()
    # Kişilik Gem'leri
    st.subheader("🎭 Karakter Gem'leri")
    persona = st.selectbox("Aktif Kişilik", [
        "🌸 Sekreter Uygula (Bayan)", 
        "🎙️ Can Radyocu (Erkek)", 
        "🧠 Bilge (Eğitmen)",
        "🖼️ Görsel Tasarımcı"
    ])
    
    voice_on = st.toggle("Sesli Okuma (Aktif)", value=True)
    
    st.divider()
    if st.button("➕ Yeni Sohbet"):
        chat_id = f"{persona} | {datetime.now().strftime('%H:%M:%S')}"
        st.session_state.db[chat_id] = []
        st.session_state.active_id = chat_id
        save_db(st.session_state.db)

    st.subheader("📜 Sohbet Arşivi")
    all_chats = list(st.session_state.db.keys())
    if all_chats:
        st.session_state.active_id = st.selectbox("Geçmiş Konuşmalar", all_chats[::-1])

# --- 4. KARAKTER DAVRANIŞLARI (PROMPT MERKEZİ) ---
BEHAVIORS = {
    "🌸 Sekreter Uygula (Bayan)": "Sen Uygula'sın. İşveli, cilveli, sempatik ve çok zeki bir sekreter/asistansın. Kullanıcına 'Yönetmenim' dersin. Sesin buğulu ve etkileyicidir.",
    "🎙️ Can Radyocu (Erkek)": "Sen Can'sın. Karizmatik, tok sesli, entelektüel bir radyo programcısısın. Genel kültür canavarısın.",
    "🧠 Bilge (Eğitmen)": "Sen her konuya vakıf, teknik ve akademik bilgisi çok yüksek bir eğitmensin. Soruları derinlemesine analiz edersin.",
    "🖼️ Görsel Tasarımcı": "Sen bir AI Sanatçısısın. Kullanıcının her isteğine uygun görsel promptları ve tasarımlar üretirsin."
}

# --- 5. ANA PANEL ---
if not st.session_state.active_id:
    st.info("Lütfen sol menüden 'Yeni Sohbet' başlatın veya bir arşiv seçin yönetmenim.")
    st.stop()

st.title(st.session_state.active_id)

# API Bağlantısı
client = Groq(api_key=st.secrets["GROQ_API_KEY"])

# Mesajları Çek
messages = st.session_state.db.get(st.session_state.active_id, [])

for m in messages:
    cls = "user-bubble" if m["role"] == "user" else "assistant-bubble"
    st.markdown(f'<div class="{cls}"><b>{"Siz" if m["role"]=="user" else "Uygula"}:</b><br>{m["content"]}</div>', unsafe_allow_html=True)

# Girdi ve AI Yanıtı
if prompt := st.chat_input("Emredin yönetmenim..."):
    messages.append({"role": "user", "content": prompt})
    st.markdown(f'<div class="user-bubble"><b>Siz:</b><br>{prompt}</div>', unsafe_allow_html=True)

    with st.spinner("İşleniyor..."):
        full_system = BEHAVIORS[persona]
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "system", "content": full_system}] + messages
        ).choices[0].message.content
        
        st.markdown(f'<div class="assistant-bubble"><b>Uygula:</b><br>{response}</div>', unsafe_allow_html=True)

        # SESLİ OKUMA KÖPRÜSÜ
        if voice_on:
            clean_text = re.sub(r'[^\w\s]', '', response[:300]) # Özel karakterleri temizle
            tts_url = f"https://translate.google.com/translate_tts?ie=UTF-8&q={clean_text.replace(' ', '%20')}&tl=tr&client=tw-ob"
            st.components.v1.html(f"""
                <audio autoplay><source src="{tts_url}" type="audio/mpeg"></audio>
            """, height=0)

    messages.append({"role": "assistant", "content": response})
    st.session_state.db[st.session_state.active_id] = messages
    save_db(st.session_state.db)
