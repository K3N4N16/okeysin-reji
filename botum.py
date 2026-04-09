import streamlit as st
from groq import Groq
import json
import os
from datetime import datetime
import urllib.parse

# --- 1. SİSTEM & PREMİUM TASARIM ---
st.set_page_config(page_title="OMEGA v38 - NEXUS", layout="wide", page_icon="🎙️")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=Roboto:wght@300;400&display=swap');
    
    .stApp { background-color: #020205; color: #00f2ff; font-family: 'Roboto', sans-serif; }
    [data-testid="stSidebar"] { background-color: #080810; border-right: 2px solid #ff007f; min-width: 300px !important; }
    
    /* Neon Mesaj Kartları */
    .chat-card {
        background: rgba(15, 15, 25, 0.95); border: 1px solid #333;
        border-radius: 15px; padding: 25px; margin-bottom: 25px;
        transition: 0.3s ease-in-out;
    }
    .chat-card:hover { border-color: #ff007f; box-shadow: 0 0 20px rgba(255, 0, 127, 0.25); }
    
    .user-text { color: #00f2ff; font-weight: bold; border-left: 4px solid #00f2ff; padding-left: 15px; }
    .assistant-text { color: #f5f5f5; border-left: 4px solid #ff007f; padding-left: 15px; line-height: 1.6; }

    /* Action Toolbar */
    .tool-bar { display: flex; gap: 25px; margin-top: 20px; padding-top: 15px; border-top: 1px solid #222; }
    .tool-btn { 
        cursor: pointer; color: #ff007f; font-size: 1.1rem; 
        background: transparent; border: none; transition: 0.3s; 
        display: flex; align-items: center; gap: 8px;
    }
    .tool-btn:hover { color: #00f2ff; transform: translateY(-2px); text-shadow: 0 0 10px #00f2ff; }
    </style>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
""", unsafe_allow_html=True)

# --- 2. GLOBAL SES MOTORU (JS KÖPRÜSÜ) ---
def init_voice_engine():
    js = """
    <script>
    window.speakText = function(text, rate = 1.05) {
        if ('speechSynthesis' in window) {
            window.speechSynthesis.cancel(); // Mevcut sesi durdur
            var utter = new SpeechSynthesisUtterance(text);
            utter.lang = 'tr-TR';
            utter.rate = rate;
            utter.pitch = 1.1;
            window.speechSynthesis.speak(utter);
        }
    }
    window.stopSpeech = function() { window.speechSynthesis.cancel(); }
    </script>
    """
    st.components.v1.html(js, height=0)

init_voice_engine()

# --- 3. KALICI VERİ MOTORU ---
DB_FILE = "omega_nexus_v38.json"
def load_db(): return json.load(open(DB_FILE, "r", encoding="utf-8")) if os.path.exists(DB_FILE) else {}
def save_db(db): json.dump(db, open(DB_FILE, "w", encoding="utf-8"), ensure_ascii=False, indent=4)

if "db" not in st.session_state: st.session_state.db = load_db()
if "active_id" not in st.session_state: st.session_state.active_id = "Ana Reji"

# --- 4. REJİ SIDEBAR ---
with st.sidebar:
    st.markdown("<h2 style='color:#ff007f; font-family:Orbitron;'>🎛️ REJİ PANELİ</h2>", unsafe_allow_html=True)
    
    personalar = {
        "🌸 Sekreter Uygula": "Cilveli, iş bitirici ve zeki sekreter.",
        "🎙️ Can Radyocu": "Tok sesli, karizmatik ve genel kültür canavarı.",
        "🔥 Dilay (Radyo Yıldızı)": "İşveli, kıpır kıpır, Kenan'a hayran radyo sunucusu.",
        "🧠 Bilge Eğitmen": "Her konuda akademik ve derin bilgisi olan usta."
    }
    selected_persona = st.selectbox("👤 Aktif Karakter", list(personalar.keys()))
    speed = st.slider("🎤 Ses Hızı", 0.7, 1.5, 1.05)
    
    st.divider()
    up_file = st.file_uploader("📁 Veri Dosyası (Eğitim)", type=['txt', 'json', 'pdf'])
    
    if st.button("➕ Yeni Sohbet"):
        cid = f"{selected_persona.split()[-1]} | {datetime.now().strftime('%H:%M')}"
        st.session_state.db[cid] = []
        st.session_state.active_id = cid
        save_db(st.session_state.db)
        st.rerun()

    st.subheader("📜 Arşivlenenler")
    history = list(st.session_state.db.keys())
    if history:
        st.session_state.active_id = st.selectbox("Geçmiş", history[::-1])

# --- 5. ANA EKRAN & AI LOGIC ---
client = Groq(api_key=st.secrets["GROQ_API_KEY"])
st.markdown(f"<h1 style='font-family:Orbitron; color:#ff007f; font-size:1.4rem;'>{st.session_state.active_id}</h1>", unsafe_allow_html=True)

chat_history = st.session_state.db.get(st.session_state.active_id, [])

# Sohbet Görüntüleme
for msg in chat_history:
    if msg["role"] == "user":
        st.markdown(f'<div class="chat-card"><div class="user-text"><b>Siz:</b><br>{msg["content"]}</div></div>', unsafe_allow_html=True)
    else:
        txt = msg["content"]
        safe_txt = txt.replace("`", "'").replace("\n", " ")
        st.markdown(f"""
            <div class="chat-card">
                <div class="assistant-text"><b>{selected_persona.split()[-1]}:</b><br>{txt}</div>
                <div class="tool-bar">
                    <button class="tool-btn" onclick="window.speakText(`{safe_txt}`, {speed})">
                        <i class="fas fa-play-circle"></i> Dinle
                    </button>
                    <button class="tool-btn" onclick="window.stopSpeech()">
                        <i class="fas fa-stop-circle"></i> Dur
                    </button>
                    <button class="tool-btn" onclick="navigator.clipboard.writeText(`{txt}`)">
                        <i class="fas fa-copy"></i> Kopyala
                    </button>
                    <a href="data:text/plain;charset=utf-8,{urllib.parse.quote(txt)}" download="omega_not.txt" class="tool-btn" style="text-decoration:none;">
                        <i class="fas fa-download"></i> İndir
                    </a>
                </div>
            </div>
        """, unsafe_allow_html=True)

# Girdi ve Yanıt
if prompt := st.chat_input("Emredin yönetmenim... 🎙️"):
    chat_history.append({"role": "user", "content": prompt})
    st.session_state.db[st.session_state.active_id] = chat_history
    
    with st.spinner(f"{selected_persona.split()[-1]} hazırlanıyor..."):
        # Sistem Talimatı (Persona Entegrasyonu)
        sys_prompt = f"Sen {selected_persona} rolündesin. Yönetmenin Kenan'a sadık, zeki ve çok etkileyicisin."
        if up_file: sys_prompt += f" Şu dosyayı hafızana al: {up_file.name}"
        
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "system", "content": sys_prompt}] + chat_history
        ).choices[0].message.content
        
        chat_history.append({"role": "assistant", "content": response})
        st.session_state.db[st.session_state.active_id] = chat_history
        save_db(st.session_state.db)
        
        # Otomatik Ses Tetikleme
        st.components.v1.html(f"<script>window.speakText(`{response.replace('`','').replace('\\','').replace(chr(10), ' ')}`, {speed});</script>", height=0)
        st.rerun()

st.caption("🚀 OMEGA v38 Master Chassis | Tüm Sistemler Aktif")
