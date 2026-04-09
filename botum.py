import streamlit as st
from groq import Groq
import json
import os
from datetime import datetime

# --- 1. SİSTEM & PREMİUM TASARIM ---
st.set_page_config(page_title="OMEGA v43 - KESİN SES", layout="wide")

# ResponsiveVoice API - Kaliteli Ses İçin Gerekli Köprü
st.markdown("""
    <script src="https://code.responsivevoice.org/responsivevoice.js?key=YOUR_FREE_KEY"></script>
    <style>
    .stApp { background-color: #020205; color: #00f2ff; }
    [data-testid="stSidebar"] { background-color: #080810; border-right: 2px solid #ff007f; }
    .chat-card {
        background: rgba(15, 15, 25, 0.95); border: 1px solid #333;
        border-radius: 15px; padding: 20px; margin-bottom: 20px;
        box-shadow: 0 0 15px rgba(255, 0, 127, 0.2);
    }
    .assistant-msg { color: #ffffff; line-height: 1.6; }
    .play-btn { 
        cursor: pointer; background: #ff007f; color: white; border: none;
        padding: 8px 15px; border-radius: 10px; font-weight: bold; margin-top: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# --- 2. SESİ ZORLAYAN MASTER FONKSİYON ---
def play_voice_js(text):
    # Bu JS kodu ResponsiveVoice kullanarak en kaliteli Türkçe kadın sesini tetikler
    clean_text = text.replace('"', '').replace("'", "").replace('\n', ' ')
    js_code = f"""
    <script>
    if (window.responsiveVoice) {{
        responsiveVoice.speak("{clean_text}", "Turkish Female", {{pitch: 1.1, rate: 1.05}});
    }} else {{
        // Yedek Motor: Browser TTS
        var msg = new SpeechSynthesisUtterance("{clean_text}");
        msg.lang = "tr-TR";
        window.speechSynthesis.speak(msg);
    }}
    </script>
    """
    st.components.v1.html(js_code, height=0)

# --- 3. VERİ YÖNETİMİ ---
DB_FILE = "omega_v43_master.json"
def load_db(): return json.load(open(DB_FILE, "r", encoding="utf-8")) if os.path.exists(DB_FILE) else {}
def save_db(db): json.dump(db, open(DB_FILE, "w", encoding="utf-8"), ensure_ascii=False, indent=4)

if "db" not in st.session_state: st.session_state.db = load_db()
if "active_id" not in st.session_state: st.session_state.active_id = "Stüdyo Ana Yayın"

# --- 4. REJİ PANELİ ---
with st.sidebar:
    st.markdown("<h2 style='color:#ff007f;'>🎙️ REJİ v43</h2>", unsafe_allow_html=True)
    persona = st.selectbox("Kişilik Seçimi", ["🌸 Emel (Cilveli)", "🎙️ Can (Erkek)", "💼 Uygula (Sekreter)"])
    
    st.divider()
    up_file = st.file_uploader("📁 Hafıza Dosyası Yükle", type=['txt'])
    training_data = ""
    if up_file:
        training_data = up_file.read().decode("utf-8")
        st.success("Hafıza Dosyası Hazır.")

    if st.button("➕ Yeni Proje"):
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

chat_history = st.session_state.db.get(st.session_state.active_id, [])

# Mesaj Listeleme
for i, m in enumerate(chat_history):
    if m["role"] == "user":
        st.markdown(f'<div style="text-align:right; color:#00f2ff; margin-bottom:10px;"><b>Yönetmenim:</b><br>{m["content"]}</div>', unsafe_allow_html=True)
    else:
        txt = m["content"]
        st.markdown(f"""
            <div class="chat-card">
                <div class="assistant-msg"><b>{persona.split()[1]}:</b><br>{txt}</div>
                <button class="play-btn" onclick="responsiveVoice.speak('{txt.replace("'","").replace('"','')}', 'Turkish Female', {{pitch: 1.1, rate: 1.05}})">🔊 Sesi Duy</button>
            </div>
        """, unsafe_allow_html=True)

# Mesaj Girişi
if prompt := st.chat_input("Yayındayız yönetmenim..."):
    chat_history.append({"role": "user", "content": prompt})
    
    with st.spinner("Emel mikrofona geliyor..."):
        sys_msg = f"Sen {persona} modundasın. Yönetmenin Kenan'a karşı cilveli, zeki ve radyocu dilinde cevaplar ver."
        if training_data: sys_msg += f"\n\nHAFIZA: {training_data}"
        
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "system", "content": sys_msg}] + chat_history
        ).choices[0].message.content
        
        chat_history.append({"role": "assistant", "content": response})
        st.session_state.db[st.session_state.active_id] = chat_history
        save_db(st.session_state.db)
        
        # SESİ OTOMATİK ÇALDIRMA DENEMESİ
        play_voice_js(response)
        st.rerun()

