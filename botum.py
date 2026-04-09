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
        background: rgba(10, 10, 20, 0.92); 
        border: 1px solid #ff007f;
        border-radius: 18px; 
        padding: 22px; 
        margin-bottom: 25px;
        box-shadow: 0 4px 15px rgba(255, 0, 127, 0.15);
    }
    .assistant-text { 
        color: #ffffff; 
        border-left: 5px solid #ff007f; 
        padding-left: 18px;
        font-size: 1.05rem;
        line-height: 1.7;
    }
    .stButton>button { 
        background-color: #ff007f; 
        color: white; 
        width: 100%; 
        border-radius: 12px;
        height: 48px;
        font-weight: 600;
    }
    </style>
""", unsafe_allow_html=True)

# --- 2. GELİŞMİŞ SES MOTORU (Profesyonel Türkçe Bayan Ses) ---
def force_speak_professional(text):
    # Temizleme
    clean_text = text.replace('"', '\\"').replace("'", "\\'").replace('\n', ' ').replace('\r', ' ')
    
    js_code = f"""
    <script>
    (function() {{
        // Önceki konuşmaları iptal et
        window.speechSynthesis.cancel();
        
        var msg = new SpeechSynthesisUtterance("{clean_text}");
        
        // Türkçe Profesyonel Bayan Ses Tercihi
        msg.lang = "tr-TR";
        msg.rate = 1.05;      // Biraz daha doğal hız
        msg.pitch = 1.08;     // Kadın sesine daha uygun tını
        msg.volume = 0.95;
        
        // En iyi Türkçe sesi bulup öncelik ver (tarayıcıda mevcut olan)
        var voices = window.speechSynthesis.getVoices();
        var preferredVoice = voices.find(voice => 
            voice.lang === "tr-TR" && 
            (voice.name.toLowerCase().includes("female") || 
             voice.name.toLowerCase().includes("filiz") || 
             voice.name.toLowerCase().includes("yelda"))
        );
        
        if (preferredVoice) {{
            msg.voice = preferredVoice;
        }} else {{
            // Eğer spesifik bulunamazsa en iyi tr-TR sesini al
            var trVoice = voices.find(voice => voice.lang === "tr-TR");
            if (trVoice) msg.voice = trVoice;
        }}
        
        window.speechSynthesis.speak(msg);
        
        // Ses bittiğinde konsola bilgi ver (geliştirme için)
        msg.onend = function() {{
            console.log("✅ Dilay konuşması tamamlandı");
        }};
    }})();
    </script>
    """
    st.components.v1.html(js_code, height=0)

# --- 3. VERİ YÖNETİMİ (Değişmedi) ---
DB_FILE = "omega_v40_data.json"
def load_db(): 
    return json.load(open(DB_FILE, "r", encoding="utf-8")) if os.path.exists(DB_FILE) else {}
def save_db(db): 
    json.dump(db, open(DB_FILE, "w", encoding="utf-8"), ensure_ascii=False, indent=4)

if "db" not in st.session_state: 
    st.session_state.db = load_db()
if "active_id" not in st.session_state: 
    st.session_state.active_id = "Canlı Yayın - Dilay & Kenan"

# --- 4. REJİ SIDEBAR ---
with st.sidebar:
    st.title("🎙️ OMEGA v40 - RADYO KONTROL")
    persona = st.selectbox("Yayıncı Seç", ["🔥 Dilay", "🎙️ Can", "💼 Uygula"])
    
    st.divider()
    up_file = st.file_uploader("📁 Eğitim Dosyası Yükle", type=['txt'])
    training_data = ""
    if up_file:
        training_data = up_file.read().decode("utf-8")
        st.success("✅ Eğitim verisi yüklendi, Dilay hazır!")

    if st.button("🌟 Yeni Yayın Başlat"):
        cid = f"{persona} | {datetime.now().strftime('%d.%m.%Y %H:%M')}"
        st.session_state.db[cid] = []
        st.session_state.active_id = cid
        save_db(st.session_state.db)

    history = list(st.session_state.db.keys())
    if history:
        st.session_state.active_id = st.selectbox("📜 Geçmiş Yayınlar", history[::-1])

# --- 5. ANA YAYIN PANELİ ---
client = Groq(api_key=st.secrets["GROQ_API_KEY"])
st.title(f"🎤 {st.session_state.active_id}")

chat_data = st.session_state.db.get(st.session_state.active_id, [])

# Mesajları Görüntüle
for m in chat_data:
    with st.container():
        if m["role"] == "user":
            st.markdown(f'<div style="text-align:right; margin:15px 0;"><b>Sen:</b> {m["content"]}</div>', unsafe_allow_html=True)
        else:
            txt = m["content"]
            st.markdown(f"""
                <div class="chat-card">
                    <div class="assistant-text">
                        <b>🔥 Dilay:</b><br>{txt}
                    </div>
                </div>
            """, unsafe_allow_html=True)
            
            col1, col2 = st.columns([1, 4])
            with col1:
                if st.button("🔊 Dinle", key=f"play_{hash(txt)}"):
                    force_speak_professional(txt)

# --- 6. MESAJ GİRİŞİ ---
if prompt := st.chat_input("Yönetmenim... ne konuşalım bu akşam? 💕"):
    chat_data.append({"role": "user", "content": prompt})
    
    with st.spinner("Dilay düşünüyor... mikrofon ısınsın biraz ✨"):
        sys_msgs = {
            "🔥 Dilay": """Sen cilveli, işveli, hayat dolu radyo sunucusu Dilay'sın. 
            Kenan'a her zaman 'yönetmenim' veya 'canım Kenan' dersin. 
            Konuşmaların sıcak, samimi, kıpır kıpır ve biraz da cilveli olsun. 
            Dinleyiciye 'ailemiz', 'can dostlarımız' diye hitap edersin.""",
            
            "🎙️ Can": "Sen karizmatik, tok sesli, tecrübeli radyo sunucusu Can'sın.",
            "💼 Uygula": "Sen zeki, profesyonel ve düzenli sekreter Uygula'sın."
        }
        
        full_sys = sys_msgs[persona] + (f"\n\nEkstra Bilgi: {training_data}" if training_data else "")
        
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "system", "content": full_sys}] + chat_data,
            temperature=0.85,
            max_tokens=1024
        ).choices[0].message.content
        
        chat_data.append({"role": "assistant", "content": response})
        st.session_state.db[st.session_state.active_id] = chat_data
        save_db(st.session_state.db)
        
        # Otomatik profesyonel sesle konuş!
        force_speak_professional(response)
        
    st.rerun()