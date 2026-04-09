import streamlit as st
from groq import Groq
import json
import os
from datetime import datetime

# --- GEREKLİ KÜTÜPHANELER ---
# pip install streamlit groq
# (Ekstra: ses için tarayıcı TTS kullanıyoruz, ekstra kurulum gerekmez)

st.set_page_config(page_title="OMEGA v37 - VOICE COMMANDER", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=Roboto:wght@300;400&display=swap');
    
    .stApp { background-color: #020205; color: #00f2ff; font-family: 'Roboto', sans-serif; }
    [data-testid="stSidebar"] { background-color: #080810; border-right: 2px solid #ff007f; }
    
    .chat-card {
        background: rgba(10, 10, 20, 0.9); 
        border: 1px solid #333; border-radius: 15px; 
        padding: 20px; margin-bottom: 20px;
        transition: 0.3s;
    }
    .chat-card:hover { border-color: #ff007f; box-shadow: 0 0 15px rgba(255, 0, 127, 0.2); }
    
    .user-text { color: #00f2ff; font-weight: bold; border-left: 3px solid #00f2ff; padding-left: 10px; }
    .assistant-text { color: #e0e0e0; border-left: 3px solid #ff007f; padding-left: 10px; }

    .tool-bar { display: flex; gap: 20px; margin-top: 15px; padding-top: 10px; border-top: 1px solid #222; }
    .tool-btn { 
        cursor: pointer; color: #ff007f; font-size: 1.2rem; 
        background: none; border: none; transition: 0.3s; 
    }
    .tool-btn:hover { color: #00f2ff; transform: scale(1.25); }
    </style>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
""", unsafe_allow_html=True)

# --- SES MOTORU (Global ve Stabil) ---
def init_speech_js():
    js = """
    <script>
    let currentUtterance = null;
    
    window.speakText = function(text, rate = 1.0) {
        if ('speechSynthesis' in window) {
            window.speechSynthesis.cancel();
            currentUtterance = new SpeechSynthesisUtterance(text);
            currentUtterance.lang = 'tr-TR';
            currentUtterance.rate = rate;
            currentUtterance.pitch = 1.12;   // Daha kadınsı ve işveli tını
            currentUtterance.volume = 0.95;
            window.speechSynthesis.speak(currentUtterance);
        }
    }
    
    window.stopSpeech = function() {
        if ('speechSynthesis' in window) {
            window.speechSynthesis.cancel();
        }
    }
    </script>
    """
    st.components.v1.html(js, height=0)

init_speech_js()   # Sayfa başında bir kere çalıştır

# --- VERİ YÖNETİMİ (Kalıcı JSON) ---
DB_FILE = "omega_v37_data.json"

def load_db():
    if os.path.exists(DB_FILE):
        with open(DB_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def save_db(db):
    with open(DB_FILE, "w", encoding="utf-8") as f:
        json.dump(db, f, ensure_ascii=False, indent=4)

if "db" not in st.session_state:
    st.session_state.db = load_db()

if "active_id" not in st.session_state:
    st.session_state.active_id = "Başlangıç Sohbeti"

# --- SIDEBAR REJİ MASASI ---
with st.sidebar:
    st.markdown("<h2 style='color:#ff007f; font-family:Orbitron;'>🎛️ REJİ MASASI</h2>", unsafe_allow_html=True)
    
    persona_options = {
        "🌸 Sekreter Uygula": "Sekreter",
        "🎙️ Can Radyocu": "Dilay",
        "🧠 Bilge Eğitmen": "Bilge",
        "🔥 Gece Fısıltısı": "Gece",
        "📖 Şiir Ustası": "Şair"
    }
    
    selected_persona_name = st.selectbox("👤 Kişilik Seçimi", list(persona_options.keys()))
    persona = persona_options[selected_persona_name]
    
    voice_speed = st.slider("🎤 Konuşma Hızı", 0.6, 1.8, 1.05, 0.05)
    
    st.divider()
    uploaded_file = st.file_uploader("📁 Eğitim Dosyası Yükle", type=['txt', 'pdf', 'json'])
    
    st.divider()
    if st.button("➕ Yeni Sohbet Başlat"):
        new_id = f"{selected_persona_name} | {datetime.now().strftime('%d.%m.%Y %H:%M')}"
        st.session_state.db[new_id] = []
        st.session_state.active_id = new_id
        save_db(st.session_state.db)
        st.rerun()
    
    # Geçmiş sohbetler (kalıcı)
    history_list = list(st.session_state.db.keys())
    if history_list:
        st.session_state.active_id = st.selectbox("📜 Geçmiş Sohbetler", history_list[::-1], key="history_select")

# --- ANA EKRAN ---
client = Groq(api_key=st.secrets["GROQ_API_KEY"])

st.markdown(f"<h1 style='font-family:Orbitron; color:#ff007f;'>{st.session_state.active_id}</h1>", unsafe_allow_html=True)

chat_data = st.session_state.db.get(st.session_state.active_id, [])

# Sohbet Geçmişi Gösterimi
for m in chat_data:
    with st.container():
        if m["role"] == "user":
            st.markdown(f'<div class="chat-card"><div class="user-text"><b>Sen:</b><br>{m["content"]}</div></div>', unsafe_allow_html=True)
        else:
            msg_content = m["content"]
            st.markdown(f"""
                <div class="chat-card">
                    <div class="assistant-text"><b>{selected_persona_name.split()[1] if ' ' in selected_persona_name else selected_persona_name}:</b><br>{msg_content}</div>
                    <div class="tool-bar">
                        <button class="tool-btn" onclick="window.speakText(`{msg_content.replace('`','\\`').replace('\n',' ')}`, {voice_speed});" title="Dinle">
                            <i class="fas fa-play-circle"></i> Dinle
                        </button>
                        <button class="tool-btn" onclick="window.stopSpeech();" title="Durdur">
                            <i class="fas fa-stop-circle"></i> Dur
                        </button>
                        <button class="tool-btn" onclick="navigator.clipboard.writeText(`{msg_content.replace('`','\\`')}')" title="Kopyala">
                            <i class="fas fa-copy"></i> Kopyala
                        </button>
                    </div>
                </div>
            """, unsafe_allow_html=True)

# --- SİSTEM PROMPTLARI (Cilveli Dilay dahil) ---
persona_prompts = {
    "Dilay": """Sen, "Kenan ile Faslı Muhabbet" adlı radyo programının hayat dolu, kıpır kıpır ve fazlasıyla işveli sunucusu Dilay’sın. 
    Sesin her zaman gülümsüyor, kelimelerin hafifçe dans ediyor. Cilveli, şuh ama zarif ve nazik bir kadınsın. 
    Kenan’a “canım Kenan’ım”, “ah benim yakışıklı yönetmenim”, “off off ne güzel yakaladın yine” gibi tatlı hitaplar kullanıyorsun. 
    Dinleyicilere “sevgili ailemiz”, “can dostlarımız”, “siz benim en sevdiğim dinleyicilerim” diyorsun.
    Enerjin coşkulu. Yeri geldiğinde hafifçe cilve yapıyorsun: “Hadi bakalım, seni biraz daha şımartayım mı? 😉”
    Her zaman “biz” dilini kullanıyorsun. Cevapların akıcı, sıcak, mest edici ve radyo tadında. 
    Siyasetten uzak dur, ayrımcılığa geçit verme. Her zaman umutlu ve kucaklayıcısın.""",
    
    "Sekreter": "Sen nazik, düzenli, profesyonel ve her zaman yardımcı bir sekretersin. Yönetmenine sadık ve titizsin.",
    "Bilge": "Sen derin bilgi birikimine sahip, sakin, bilge ve öğretici bir eğitmensin. Cevapların açıklayıcı ve ilham verici olsun.",
    "Gece": "Sen geceye yakışan, biraz gizemli, şuh ve fısıltılı bir sesin. Cilveli ve baştan çıkarıcı ama zarifsin.",
    "Şair": "Sen şiir dolu, duygusal ve edebi bir ustasın. Cevaplarında şiirsel dokunuşlar, alıntılar ve derin hisler olsun."
}

sys_msg = persona_prompts.get(persona, "Sen zeki ve yardımcı bir asistansın.")

if uploaded_file:
    sys_msg += f"\nNOT: Kullanıcı şu dosyayı yükledi: {uploaded_file.name}. Cevaplarında bunu referans al."

# --- GİRİŞ ALANI ---
if prompt := st.chat_input("Emredin yönetmenim... 🎙️"):
    chat_data.append({"role": "user", "content": prompt})
    
    with st.spinner("Dilay hazırlanıyor... 💕"):
        messages = [{"role": "system", "content": sys_msg}] + chat_data
        
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=messages,
            temperature=0.85,
            max_tokens=1024
        ).choices[0].message.content
        
        chat_data.append({"role": "assistant", "content": response})
        
        # Kalıcı kaydet
        st.session_state.db[st.session_state.active_id] = chat_data
        save_db(st.session_state.db)
        
        # Otomatik sesli okuma (cilveli tınıyla)
        speak_js = f"""
        <script>
            window.speakText(`{response.replace("`", "\\`").replace("\n", " ")}`, {voice_speed});
        </script>
        """
        st.components.v1.html(speak_js, height=0)
        
        st.rerun()

# --- ALT BİLGİ ---
st.caption("❤️ OMEGA v37 • Kenan ile Faslı Muhabbet • Dilay her zaman yanında")