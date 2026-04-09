import streamlit as st
from groq import Groq
import json
import os
from datetime import datetime

# --- 1. SİSTEM & TASARIM ---
st.set_page_config(page_title="OMEGA v37 - VOICE COMMANDER", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=Roboto:wght@300;400&display=swap');
    
    .stApp { background-color: #020205; color: #00f2ff; font-family: 'Roboto', sans-serif; }
    [data-testid="stSidebar"] { background-color: #080810; border-right: 2px solid #ff007f; }
    
    /* Neon Mesaj Kartları */
    .chat-card {
        background: rgba(10, 10, 20, 0.9); border: 1px solid #333;
        border-radius: 15px; padding: 20px; margin-bottom: 20px;
        transition: 0.3s;
    }
    .chat-card:hover { border-color: #ff007f; box-shadow: 0 0 15px rgba(255, 0, 127, 0.2); }
    
    .user-text { color: #00f2ff; font-weight: bold; border-left: 3px solid #00f2ff; padding-left: 10px; }
    .assistant-text { color: #e0e0e0; border-left: 3px solid #ff007f; padding-left: 10px; }

    /* Action Icons */
    .tool-bar { display: flex; gap: 20px; margin-top: 15px; padding-top: 10px; border-top: 1px solid #222; }
    .tool-btn { 
        cursor: pointer; color: #ff007f; font-size: 1.1rem; 
        background: none; border: none; transition: 0.3s; 
    }
    .tool-btn:hover { color: #00f2ff; transform: scale(1.2); }
    </style>
    
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
""", unsafe_allow_html=True)

# --- 2. SES MOTORU (JAVASCRIPT KÖPRÜSÜ) ---
def speak_js(text, rate=1.0):
    # Tarayıcıyı zorla konuşturan JS kodu
    clean_text = text.replace("'", "\\'").replace("\n", " ")
    js_code = f"""
    <script>
    var msg = new SpeechSynthesisUtterance('{clean_text}');
    msg.lang = 'tr-TR';
    msg.rate = {rate};
    window.speechSynthesis.speak(msg);
    </script>
    """
    st.components.v1.html(js_code, height=0)

# --- 3. VERİ YÖNETİMİ ---
DB_FILE = "omega_v37_data.json"
def load_db(): return json.load(open(DB_FILE, "r", encoding="utf-8")) if os.path.exists(DB_FILE) else {}
def save_db(db): json.dump(db, open(DB_FILE, "w", encoding="utf-8"), ensure_ascii=False, indent=4)

if "db" not in st.session_state: st.session_state.db = load_db()
if "active_id" not in st.session_state: st.session_state.active_id = "Başlangıç"

# --- 4. SIDEBAR REJİ PANELİ ---
with st.sidebar:
    st.markdown("<h2 style='color:#ff007f; font-family:Orbitron;'>REJİ MASASI</h2>", unsafe_allow_html=True)
    
    persona = st.selectbox("Kişilik Seçimi", ["🌸 Sekreter Uygula", "🎙️ Can Radyocu", "🧠 Bilge Eğitmen"])
    voice_speed = st.slider("Konuşma Hızı", 0.5, 2.0, 1.0)
    
    st.divider()
    uploaded_file = st.file_uploader("Eğitim Dosyası Yükle (Veri Analizi)", type=['txt', 'pdf', 'json'])
    
    st.divider()
    if st.button("➕ Yeni Proje Başlat"):
        new_id = f"{persona} | {datetime.now().strftime('%H:%M')}"
        st.session_state.db[new_id] = []
        st.session_state.active_id = new_id
    
    history_list = list(st.session_state.db.keys())
    if history_list:
        st.session_state.active_id = st.selectbox("Geçmiş Kayıtlar", history_list[::-1])

# --- 5. ANA EKRAN ---
client = Groq(api_key=st.secrets["GROQ_API_KEY"])
st.markdown(f"<h1 style='font-family:Orbitron; font-size:1.5rem;'>{st.session_state.active_id}</h1>", unsafe_allow_html=True)

chat_data = st.session_state.db.get(st.session_state.active_id, [])

# Sohbet Akışı
for i, m in enumerate(chat_data):
    with st.container():
        if m["role"] == "user":
            st.markdown(f'<div class="chat-card"><div class="user-text"><b>Siz:</b><br>{m["content"]}</div></div>', unsafe_allow_html=True)
        else:
            msg_content = m["content"]
            st.markdown(f"""
                <div class="chat-card">
                    <div class="assistant-text"><b>Uygula:</b><br>{msg_content}</div>
                    <div class="tool-bar">
                        <button class="tool-btn" onclick="const msg = new SpeechSynthesisUtterance(`{msg_content}`); msg.lang='tr-TR'; msg.rate={voice_speed}; window.speechSynthesis.speak(msg);" title="Dinle">
                            <i class="fas fa-play-circle"></i> Dinle
                        </button>
                        <button class="tool-btn" onclick="window.speechSynthesis.cancel();" title="Durdur">
                            <i class="fas fa-stop-circle"></i> Dur
                        </button>
                        <button class="tool-btn" onclick="navigator.clipboard.writeText(`{msg_content}`)" title="Kopyala">
                            <i class="fas fa-copy"></i>
                        </button>
                    </div>
                </div>
            """, unsafe_allow_html=True)

# Girdi
if prompt := st.chat_input("Emredin yönetmenim..."):
    chat_data.append({"role": "user", "content": prompt})
    
    with st.spinner("Uygula hazırlanıyor..."):
        # Karakter ayarı
        sys_msg = f"Sen {persona} modundasın. Yönetmenine sadık, zeki ve etkileyicisin."
        if uploaded_file: sys_msg += f"\nNOT: Şu dosyayı da referans al: {uploaded_file.name}"
        
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "system", "content": sys_msg}] + chat_data
        ).choices[0].message.content
        
        chat_data.append({"role": "assistant", "content": response})
        st.session_state.db[st.session_state.active_id] = chat_data
        save_db(st.session_state.db)
        
        # OTOMATIK SES (Opsiyonel tetikleyici)
        speak_js(response, rate=voice_speed)
        st.rerun()
