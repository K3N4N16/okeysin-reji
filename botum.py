import streamlit as st
from groq import Groq
import json
import os
from datetime import datetime
import urllib.parse

# --- 1. PREMİUM NEON ARAYÜZ ---
st.set_page_config(page_title="OMEGA v42 - EMEL SESİ", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #020205; color: #00f2ff; }
    [data-testid="stSidebar"] { background-color: #080810; border-right: 2px solid #ff007f; }
    
    .chat-card {
        background: rgba(10, 10, 20, 0.95); border: 1px solid #333;
        border-radius: 15px; padding: 20px; margin-bottom: 20px;
        box-shadow: 0 0 20px rgba(255, 0, 127, 0.2);
    }
    .assistant-msg { color: #ffffff; line-height: 1.6; font-size: 1.1rem; }
    .tool-btn { 
        cursor: pointer; color: #ff007f; background: none; border: 1px solid #ff007f; 
        border-radius: 10px; padding: 8px 15px; margin-top: 10px; transition: 0.3s;
    }
    .tool-btn:hover { background: #ff007f; color: white; box-shadow: 0 0 15px #ff007f; }
    </style>
""", unsafe_allow_html=True)

# --- 2. SES MOTORU (EMEL - KALİTELİ) ---
def play_voice(text):
    # Temizleme ve Encode
    safe_text = urllib.parse.quote(text.replace('\n', ' ').replace('"', '').replace("'", ""))
    audio_url = f"https://translate.google.com/translate_tts?ie=UTF-8&q={safe_text}&tl=tr&client=tw-ob"
    
    # JS Köprüsü (Zorlayıcı Tetikleme)
    js_code = f"""
    <script>
        var audio = new Audio('{audio_url}');
        audio.play().catch(function(error) {{
            console.log("Tarayıcı engeli: Bir kez sayfaya tıklamanız gerekiyor.");
        }});
    </script>
    """
    st.components.v1.html(js_code, height=0)

# --- 3. VERİ YÖNETİMİ ---
DB_FILE = "omega_v42_data.json"
def load_db(): return json.load(open(DB_FILE, "r", encoding="utf-8")) if os.path.exists(DB_FILE) else {}
def save_db(db): json.dump(db, open(DB_FILE, "w", encoding="utf-8"), ensure_ascii=False, indent=4)

if "db" not in st.session_state: st.session_state.db = load_db()
if "active_id" not in st.session_state: st.session_state.active_id = "Ana Stüdyo"

# --- 4. REJİ PANELİ (SIDEBAR) ---
with st.sidebar:
    st.markdown("<h2 style='color:#ff007f;'>🎙️ OMEGA REJİ</h2>", unsafe_allow_html=True)
    persona = st.selectbox("Kişilik Seçimi", ["🌸 Emel (Cilveli)", "🎙️ Can (Erkek)", "💼 Uygula (Sekreter)"])
    
    st.divider()
    # UPLOAD FONKSİYONU: Bilgi Bankası
    st.subheader("📁 Hafıza Yükleme")
    up_file = st.file_uploader("Dosya Yükle (.txt)", type=['txt'], help="Asistana özel bilgiler öğretir.")
    file_data = ""
    if up_file:
        file_data = up_file.read().decode("utf-8")
        st.success(f"✅ {up_file.name} belleğe alındı.")

    if st.button("➕ Yeni Sohbet"):
        cid = f"{persona.split()[1]} | {datetime.now().strftime('%H:%M')}"
        st.session_state.db[cid] = []
        st.session_state.active_id = cid
        save_db(st.session_state.db)

    history = list(st.session_state.db.keys())
    if history:
        st.session_state.active_id = st.selectbox("📜 Arşiv", history[::-1])

# --- 5. ANA EKRAN ---
client = Groq(api_key=st.secrets["GROQ_API_KEY"])
st.title(st.session_state.active_id)

messages = st.session_state.db.get(st.session_state.active_id, [])

# Sohbet Akışı
for i, m in enumerate(messages):
    with st.container():
        if m["role"] == "user":
            st.markdown(f'<div style="text-align:right; color:#00f2ff;"><b>Yönetmenim:</b><br>{m["content"]}</div>', unsafe_allow_html=True)
        else:
            txt = m["content"]
            st.markdown(f"""
                <div class="chat-card">
                    <div class="assistant-msg"><b>{persona.split()[1]}:</b><br>{txt}</div>
                    <button class="tool-btn" onclick="new Audio('https://translate.google.com/translate_tts?ie=UTF-8&q={urllib.parse.quote(txt[:300])}&tl=tr&client=tw-ob').play()">🔊 Sesi Tekrar Oynat</button>
                </div>
            """, unsafe_allow_html=True)

# Girdi
if prompt := st.chat_input("Emredin yönetmenim..."):
    messages.append({"role": "user", "content": prompt})
    
    with st.spinner("Emel hazırlanıyor..."):
        sys_prompt = f"Sen {persona} modundasın. Yönetmenin Kenan'a karşı çok saygılı, cilveli ve zekisin."
        if file_data: sys_prompt += f"\n\nHAFIZA VERİSİ: {file_data}"
        
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "system", "content": sys_prompt}] + messages
        ).choices[0].message.content
        
        messages.append({"role": "assistant", "content": response})
        st.session_state.db[st.session_state.active_id] = messages
        save_db(st.session_state.db)
        
        # SESİ TETİKLE
        play_voice(response)
        st.rerun()
