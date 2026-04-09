import streamlit as st
from groq import Groq
import json
import os
from datetime import datetime
import urllib.parse

# --- 1. ARAYÜZ TASARIMI (NEON & MODERN) ---
st.set_page_config(page_title="OMEGA v41 - EMEL VOICE", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #020205; color: #00f2ff; }
    [data-testid="stSidebar"] { background-color: #080810; border-right: 2px solid #ff007f; }
    
    .chat-card {
        background: rgba(15, 15, 25, 0.9); border: 1px solid #333;
        border-radius: 15px; padding: 20px; margin-bottom: 20px;
        box-shadow: 0 0 15px rgba(255, 0, 127, 0.2);
    }
    .assistant-header { color: #ff007f; font-weight: bold; font-family: 'Orbitron'; margin-bottom: 10px; }
    .assistant-msg { color: #ffffff; line-height: 1.6; }
    
    .action-bar { display: flex; gap: 15px; margin-top: 15px; border-top: 1px solid #222; padding-top: 10px; }
    .btn-style { 
        cursor: pointer; color: #ff007f; background: none; border: 1px solid #ff007f; 
        border-radius: 8px; padding: 5px 12px; transition: 0.3s;
    }
    .btn-style:hover { background: #ff007f; color: white; box-shadow: 0 0 10px #ff007f; }
    </style>
""", unsafe_allow_html=True)

# --- 2. EMEL SESİ (KALİTELİ TTS MOTORU) ---
def play_emel_voice(text):
    # Microsoft Edge-TTS tabanlı kaliteli ses köprüsü
    # Metni temizle ve URL formatına getir
    clean_text = urllib.parse.quote(text.replace('\n', ' '))
    # Kaliteli Türkçe Bayan Sesi (Emel benzeri tonlama)
    audio_url = f"https://translate.google.com/translate_tts?ie=UTF-8&q={clean_text}&tl=tr&client=tw-ob"
    
    js_code = f"""
    <script>
        var audio = new Audio('{audio_url}');
        audio.play().catch(e => console.log("Ses tetikleme bekleniyor..."));
    </script>
    """
    st.components.v1.html(js_code, height=0)

# --- 3. ARŞİV VE VERİ YÖNETİMİ ---
DB_FILE = "omega_v41_data.json"
def load_db(): return json.load(open(DB_FILE, "r", encoding="utf-8")) if os.path.exists(DB_FILE) else {}
def save_db(db): json.dump(db, open(DB_FILE, "w", encoding="utf-8"), ensure_ascii=False, indent=4)

if "db" not in st.session_state: st.session_state.db = load_db()
if "active_id" not in st.session_state: st.session_state.active_id = "Stüdyo Canlı"

# --- 4. REJİ SIDEBAR (UPLOAD FONKSİYONU) ---
with st.sidebar:
    st.title("🎛️ REJİ MASASI")
    
    # KİŞİLİK SEÇİMİ (Emel Modu Aktif)
    persona = st.selectbox("Ses Karakteri", ["🌸 Emel (Cilveli & Kaliteli)", "🎙️ Can (Erkek Radyocu)"])
    
    st.divider()
    
    # UPLOAD ALANI NEDİR?
    # Buraya yüklediğin dosya AI'nın 'Kısa Süreli Hafızası' olur.
    # Örneğin: 'okey_kuralları.txt' yüklersen, asistan o kuralları bilerek cevap verir.
    st.subheader("📁 Veri Yükleme (Hafıza)")
    up_file = st.file_uploader("Dosya Seç (TXT/JSON)", type=['txt', 'json'], help="Asistana özel bilgi öğretmek için kullanın.")
    
    extra_knowledge = ""
    if up_file:
        extra_knowledge = up_file.read().decode("utf-8")
        st.success(f"✅ {up_file.name} Hafızaya Alındı.")

    st.divider()
    if st.button("➕ Yeni Sohbet Başlat"):
        cid = f"{persona.split()[1]} | {datetime.now().strftime('%H:%M')}"
        st.session_state.db[cid] = []
        st.session_state.active_id = cid
        save_db(st.session_state.db)

    history = list(st.session_state.db.keys())
    if history:
        st.session_state.active_id = st.selectbox("📜 Sohbet Arşivi", history[::-1])

# --- 5. ANA PANEL VE AI İŞLEYİŞİ ---
client = Groq(api_key=st.secrets["GROQ_API_KEY"])
st.title(f"✨ {st.session_state.active_id}")

chat_data = st.session_state.db.get(st.session_state.active_id, [])

# Sohbet Akışını Görüntüle
for m in chat_data:
    with st.container():
        if m["role"] == "user":
            st.markdown(f'<div style="text-align:right; margin-bottom:10px;"><b>Yönetmenim:</b><br>{m["content"]}</div>', unsafe_allow_html=True)
        else:
            txt = m["content"]
            st.markdown(f"""
                <div class="chat-card">
                    <div class="assistant-header">{persona.split()[1]} Diyor ki:</div>
                    <div class="assistant-msg">{txt}</div>
                    <div class="action-bar">
                        <button class="btn-style" onclick="new Audio('https://translate.google.com/translate_tts?ie=UTF-8&q={urllib.parse.quote(txt[:300])}&tl=tr&client=tw-ob').play()">🔊 Tekrar Dinle</button>
                    </div>
                </div>
            """, unsafe_allow_html=True)

# Yeni Mesaj Girişi
if prompt := st.chat_input("Mesajınızı buraya bırakın yönetmenim..."):
    chat_data.append({"role": "user", "content": prompt})
    
    with st.spinner("Emel sesini hazırlıyor..."):
        # Sistem Talimatı (Hafıza Entegrasyonu)
        sys_msg = f"Sen {persona} modundasın. Yönetmenin Kenan'a çok sadık, cilveli ve zeki bir asistsansın."
        if extra_knowledge:
            sys_msg += f"\n\nÖNEMLİ BİLGİ (HAFIZA): {extra_knowledge}"
        
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "system", "content": sys_msg}] + chat_data
        ).choices[0].message.content
        
        chat_data.append({"role": "assistant", "content": response})
        st.session_state.db[st.session_state.active_id] = chat_data
        save_db(st.session_state.db)
        
        # SESİ OTOMATİK ÇAL
        play_emel_voice(response)
        st.rerun()
