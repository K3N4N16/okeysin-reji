import streamlit as st
from groq import Groq
import json
import os
from datetime import datetime

# --- 1. RADİKAL TEMİZLİK VE TASARIM ---
st.set_page_config(page_title="OMEGA v40 - KESİN ÇÖZÜM", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #020205; color: #00f2ff; }
    [data-testid="stSidebar"] { background-color: #080810; border-right: 2px solid #ff007f; }
    .chat-card {
        background: rgba(10, 10, 20, 0.9); border: 1px solid #333;
        border-radius: 15px; padding: 20px; margin-bottom: 20px;
    }
    .assistant-text { color: #ffffff; border-left: 4px solid #ff007f; padding-left: 15px; }
    .stButton>button { background-color: #ff007f; color: white; width: 100%; }
    </style>
""", unsafe_allow_html=True)

# --- 2. SESİ ZORLAYAN JAVASCRIPT MOTORU ---
# Bu fonksiyon tarayıcıyı "uyandırır" ve sesi çalar.
def force_speak_js(text):
    clean_text = text.replace('"', '').replace("'", "").replace('\n', ' ')
    js_code = f"""
    <script>
    (function() {{
        window.speechSynthesis.cancel();
        var msg = new SpeechSynthesisUtterance("{clean_text}");
        msg.lang = "tr-TR";
        msg.rate = 1.0;
        msg.pitch = 1.1;
        window.speechSynthesis.speak(msg);
    }})();
    </script>
    """
    st.components.v1.html(js_code, height=0)

# --- 3. VERİ YÖNETİMİ ---
DB_FILE = "omega_v40_data.json"
def load_db(): return json.load(open(DB_FILE, "r", encoding="utf-8")) if os.path.exists(DB_FILE) else {}
def save_db(db): json.dump(db, open(DB_FILE, "w", encoding="utf-8"), ensure_ascii=False, indent=4)

if "db" not in st.session_state: st.session_state.db = load_db()
if "active_id" not in st.session_state: st.session_state.active_id = "Canlı Yayın"

# --- 4. REJİ SIDEBAR ---
with st.sidebar:
    st.title("🎙️ OMEGA MASTER")
    persona = st.selectbox("Kişilik", ["🔥 Dilay", "🎙️ Can", "💼 Uygula"])
    
    st.divider()
    # Dosya okuma (Basit ve Hatasız)
    up_file = st.file_uploader("Eğitim Dosyası", type=['txt'])
    training_data = ""
    if up_file:
        training_data = up_file.read().decode("utf-8")
        st.success("Veri Yüklendi")

    if st.button("➕ Yeni Sohbet"):
        cid = f"{persona} | {datetime.now().strftime('%H:%M')}"
        st.session_state.db[cid] = []
        st.session_state.active_id = cid
        save_db(st.session_state.db)

    history = list(st.session_state.db.keys())
    if history:
        st.session_state.active_id = st.selectbox("Geçmiş", history[::-1])

# --- 5. ANA PANEL ---
client = Groq(api_key=st.secrets["GROQ_API_KEY"])
st.title(st.session_state.active_id)

chat_data = st.session_state.db.get(st.session_state.active_id, [])

# Mesajları Ekrana Bas
for m in chat_data:
    with st.container():
        if m["role"] == "user":
            st.markdown(f'**Siz:** {m["content"]}')
        else:
            txt = m["content"]
            st.markdown(f"""
                <div class="chat-card">
                    <div class="assistant-text"><b>{persona}:</b><br>{txt}</div>
                </div>
            """, unsafe_allow_html=True)
            # Her mesajın altına manuel "Dinle" butonu (JS Tetikleyici)
            if st.button(f"🔊 Oynat", key=hash(txt)):
                force_speak_js(txt)

# Girdi Alanı
if prompt := st.chat_input("Mesajınızı yazın yönetmenim..."):
    chat_data.append({"role": "user", "content": prompt})
    
    with st.spinner("Yanıt hazırlanıyor..."):
        # Persona Ayarları
        sys_msgs = {
            "🔥 Dilay": "Sen cilveli, işveli radyo asistanı Dilay'sın. Kenan'a 'yönetmenim' dersin.",
            "🎙️ Can": "Sen karizmatik, tok sesli radyo sunucusu Can'sın.",
            "💼 Uygula": "Sen zeki ve profesyonel sekreter Uygula'sın."
        }
        
        full_sys = sys_msgs[persona] + (f"\nVeri: {training_data}" if training_data else "")
        
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "system", "content": full_sys}] + chat_data
        ).choices[0].message.content
        
        chat_data.append({"role": "assistant", "content": response})
        st.session_state.db[st.session_state.active_id] = chat_data
        save_db(st.session_state.db)
        
        # Otomatik Ses Tetikleme
        force_speak_js(response)
        st.rerun()
