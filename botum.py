import streamlit as st
from groq import Groq
import json
import os
from datetime import datetime
import base64

# --- 1. SİSTEM AYARLARI ---
st.set_page_config(page_title="OMEGA v39 - IRONCLAD", layout="wide", page_icon="🎙️")

# Ultra-Net CSS (Görünürlük Sorunu Çözüldü)
st.markdown("""
    <style>
    .stApp { background-color: #050505; color: #ffffff; }
    [data-testid="stSidebar"] { background-color: #0d0d15 !important; border-right: 2px solid #ff007f !important; }
    .stSidebar * { color: #00f2ff !important; }
    
    .chat-card {
        background: #11111b; border: 1px solid #333;
        border-radius: 12px; padding: 20px; margin-bottom: 20px;
        box-shadow: 5px 5px 15px rgba(0,0,0,0.5);
    }
    .user-text { color: #00f2ff; border-left: 4px solid #00f2ff; padding-left: 10px; font-weight: bold; }
    .assistant-text { color: #e0e0e0; border-left: 4px solid #ff007f; padding-left: 10px; }
    
    .action-bar { display: flex; gap: 15px; margin-top: 15px; border-top: 1px solid #222; padding-top: 10px; }
    .btn-icon { cursor: pointer; color: #ff007f; background: none; border: 1px solid #ff007f; border-radius: 5px; padding: 5px 10px; font-size: 0.9rem; }
    .btn-icon:hover { background: #ff007f; color: white; }
    </style>
""", unsafe_allow_html=True)

# --- 2. SES SİSTEMİ (JS & HTML5 HYBRID) ---
def get_audio_html(text):
    # Google TTS Bulut Kaynağı (Tarayıcı motoru yerine dış kaynak)
    encoded_text = base64.b64encode(text.encode('utf-8')).decode('utf-8')
    # JS ile sesi tetikleme
    js_code = f"""
    <script>
    function playOmega() {{
        var text = "{text.replace('"', '').replace("'", "").replace('\n', ' ')}";
        var msg = new SpeechSynthesisUtterance(text);
        msg.lang = 'tr-TR';
        msg.rate = 1.0;
        window.speechSynthesis.speak(msg);
    }}
    playOmega();
    </script>
    """
    return js_code

# --- 3. VERİTABANI ---
DB_FILE = "omega_ironclad_v39.json"
def load_db(): return json.load(open(DB_FILE, "r", encoding="utf-8")) if os.path.exists(DB_FILE) else {}
def save_db(db): json.dump(db, open(DB_FILE, "w", encoding="utf-8"), ensure_ascii=False, indent=4)

if "db" not in st.session_state: st.session_state.db = load_db()
if "active_id" not in st.session_state: st.session_state.active_id = "Ana Kumanda"

# --- 4. REJİ SIDEBAR ---
with st.sidebar:
    st.image("https://img.icons8.com/nolan/96/artificial-intelligence.png")
    st.header("OMEGA v39 REJİ")
    
    persona = st.selectbox("Kişilik", ["🔥 Dilay (Cilveli)", "💼 Uygula (Sekreter)", "🎙️ Can (Radyocu)"])
    
    st.divider()
    # DOSYA YÜKLEME (Çalışan Versiyon)
    up_file = st.file_uploader("📁 Veri Dosyası Yükle", type=['txt', 'json'])
    file_content = ""
    if up_file:
        file_content = up_file.read().decode("utf-8")
        st.success(f"Dosya Hazır: {up_file.name}")

    if st.button("➕ Yeni Sohbet"):
        cid = f"{persona.split()[1]} | {datetime.now().strftime('%H:%M')}"
        st.session_state.db[cid] = []
        st.session_state.active_id = cid
        save_db(st.session_state.db)

    history = list(st.session_state.db.keys())
    if history:
        st.session_state.active_id = st.selectbox("Arşiv", history[::-1])

# --- 5. AI & MESAJ MOTORU ---
client = Groq(api_key=st.secrets["GROQ_API_KEY"])
st.title(st.session_state.active_id)

chat_history = st.session_state.db.get(st.session_state.active_id, [])

# Sohbet Listeleme
for i, m in enumerate(chat_history):
    with st.container():
        if m["role"] == "user":
            st.markdown(f'<div class="chat-card"><div class="user-text">Siz: {m["content"]}</div></div>', unsafe_allow_html=True)
        else:
            t = m["content"]
            st.markdown(f"""
                <div class="chat-card">
                    <div class="assistant-text"><b>{persona.split()[1]}:</b><br>{t}</div>
                    <div class="action-bar">
                        <button class="btn-icon" onclick="window.speechSynthesis.cancel(); var u=new SpeechSynthesisUtterance(`{t.replace('`','')}`); u.lang='tr-TR'; window.speechSynthesis.speak(u);">🔊 Dinle</button>
                        <button class="btn-icon" onclick="navigator.clipboard.writeText(`{t.replace('`','')}`)">📋 Kopyala</button>
                    </div>
                </div>
            """, unsafe_allow_html=True)

# Girdi ve İşleme
if prompt := st.chat_input("Buraya yazın yönetmenim..."):
    chat_history.append({"role": "user", "content": prompt})
    
    with st.spinner("AI Yanıtlıyor..."):
        # Persona Promptları
        sys_prompts = {
            "🔥 Dilay (Cilveli)": "Sen Dilay'sın. Kenan'ın reji asistanısın. Çok cilveli, işveli ve Kenan'ı şımartan bir kadınsın. Radyo diliyle konuşursun.",
            "💼 Uygula (Sekreter)": "Sen Uygula'sın. Profesyonel, sadık ve çözüm odaklı bir sekretersin.",
            "🎙️ Can (Radyocu)": "Sen Can'sın. Karizmatik ve entelektüel bir radyo sunucususun."
        }
        
        full_sys = sys_prompts[persona]
        if file_content: full_sys += f"\n\nDOSYA VERİSİ: {file_content}"
        
        resp = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "system", "content": full_sys}] + chat_history
        ).choices[0].message.content
        
        chat_history.append({"role": "assistant", "content": resp})
        st.session_state.db[st.session_state.active_id] = chat_history
        save_db(st.session_state.db)
        
        # SESİ ZORLA OYNAT (JavaScript Bridge)
        st.components.v1.html(get_audio_html(resp), height=0)
        st.rerun()
