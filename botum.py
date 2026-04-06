import os
import sqlite3
import base64
import asyncio
import edge_tts
import streamlit as st
from groq import Groq
from datetime import datetime

# --- GÜVENLİ API BAĞLANTISI (STREAMLIT SECRETS) ---
# GitHub'da şifrenin iptal olmaması için bu yöntemi kullanıyoruz.
try:
    GROQ_API_KEY = st.secrets["GROQ_API_KEY"]
except:
    st.error("⚠️ GROQ_API_KEY bulunamadı! Lütfen Streamlit Cloud ayarlarından Secrets kısmına ekleyin.")
    st.stop()

client = Groq(api_key=GROQ_API_KEY)
MODEL_NAME = "llama-3.3-70b-versatile"
DB_FILE = "okeysin_ultra_v4.db"

# --- VERİTABANI SİSTEMİ (GEÇMİŞİ UNUTMAZ) ---
def init_db():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS broadcast_logs 
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, character TEXT, message TEXT, timestamp TEXT)''')
    conn.commit()
    conn.close()

def log_broadcast(char, msg):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    ts = datetime.now().strftime("%H:%M:%S")
    c.execute("INSERT INTO broadcast_logs (character, message, timestamp) VALUES (?, ?, ?)", (char, msg, ts))
    conn.commit()
    conn.close()

# --- SES MOTORU (Okeysin & Kerem) ---
async def generate_audio(text, char_type, filename):
    # Okeysin: Zarif Bayan Sesi | Kerem: Teknik Erkek Sesi
    voice = "tr-TR-EmelNeural" if char_type == "Okeysin" else "tr-TR-AhmetNeural"
    communicate = edge_tts.Communicate(text, voice)
    await communicate.save(filename)

def play_on_air(text, char):
    audio_file = f"temp_voice_{char}.mp3"
    asyncio.run(generate_audio(text, char, audio_file))
    with open(audio_file, "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
        st.markdown(f'<audio autoplay src="data:audio/mp3;base64,{b64}"></audio>', unsafe_allow_html=True)

# --- TASARIM (QUANTUM NEON UI) ---
st.set_page_config(page_title="OKEYSIN GLOBAL REJİ V4", layout="wide")
init_db()

st.markdown("""
    <style>
    .stApp { background: #020205; color: #00f2ff; }
    .chat-card { background: rgba(0, 242, 255, 0.05); border: 1px solid #00f2ff33; border-radius: 15px; padding: 15px; margin-bottom: 10px; }
    .okeysin-text { color: #00f2ff; border-left: 4px solid #00f2ff; padding-left: 10px; }
    .kerem-text { color: #ffaa00; border-left: 4px solid #ffaa00; padding-left: 10px; }
    .on-air { color: red; font-weight: bold; animation: blinker 1.2s linear infinite; }
    @keyframes blinker { 50% { opacity: 0; } }
    </style>
    """, unsafe_allow_html=True)

# --- REJİ PANELİ (SIDEBAR) ---
with st.sidebar:
    st.image("https://img.icons8.com/neon/96/radio-tower.png", width=80)
    st.title("🎙️ GLOBAL REJİ")
    st.markdown('<p class="on-air">● CANLI YAYINDA</p>', unsafe_allow_html=True)
    
    st.divider()
    st.write("📍 Konum: Bursa Stüdyo")
    st.write("🧠 İşlemci: Groq Cloud")
    st.write("👥 Oyuncu: 1.240 (Okeysin.com)")
    
    st.divider()
    ses_aktif = st.toggle("Sesli Anons", value=True)
    if st.button("🗑️ Arşivi Temizle"):
        conn = sqlite3.connect(DB_FILE); conn.cursor().execute("DELETE FROM broadcast_logs"); conn.commit(); st.rerun()

# --- SOHBET AKIŞI ---
if "chat_history" not in st.session_state:
    conn = sqlite3.connect(DB_FILE); c = conn.cursor(); c.execute("SELECT character, message FROM broadcast_logs")
    st.session_state.chat_history = [{"char": r, "msg": m} for r, m in c.fetchall()]; conn.close()

# Ekranı ikiye böl (Sohbet ve İstatistik)
col_chat, col_stats = st.columns([3, 1])

with col_chat:
    for entry in st.session_state.chat_history:
        cls = "okeysin-text" if entry["char"] == "Okeysin" else "kerem-text"
        st.markdown(f'<div class="chat-card"><b class="{cls}">{entry["char"]}:</b><br>{entry["msg"]}</div>', unsafe_allow_html=True)

# --- YÖNETMEN KOMUTU ---
if prompt := st.chat_input("Yönetmenim, yayına komut verin..."):
    st.session_state.chat_history.append({"char": "Yönetmen", "msg": prompt})
    
    # Karakter Talimatları
    sys_prompt = f"""
    Sen dünyanın en gelişmiş radyo reji yazılımısın. İki karakteri yönetiyorsun:
    1. OKEYSİN: Bursa'lı, elit, zarif, entelektüel kadın sunucu.
    2. KEREM: Şakacı, teknikten anlayan, Okeysin'e saygılı ama espri yapan erkek teknisyen.
    
    Yönetmen şunu dedi: "{prompt}"
    
    GÖREV: Önce Okeysin konuyu açsın, ardından Kerem ona cevap versin. 
    Lütfen yanıtını tam olarak şu formatta yaz: 
    [OKEYSIN] (Mesaj buraya) [KEREM] (Mesaj buraya)
    Bursa havasından, Okeysin.com turnuvalarından ve sinema/müzik dünyasından bahset.
    """

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[{"role": "system", "content": sys_prompt}],
    ).choices[0].message.content

    # Yanıtı Parçala ve Yayına Ver
    if "[OKEYSIN]" in response and "[KEREM]" in response:
        okey_msg = response.split("[OKEYSIN]")[1].split("[KEREM]")[0].strip()
        kerem_msg = response.split("[KEREM]")[1].strip()
        
        # Okeysin Anonsu
        st.session_state.chat_history.append({"char": "Okeysin", "msg": okey_msg})
        log_broadcast("Okeysin", okey_msg)
        if ses_aktif: play_on_air(okey_msg, "Okeysin")
        
        # Kerem Cevabı
        st.session_state.chat_history.append({"char": "Kerem", "msg": kerem_msg})
        log_broadcast("Kerem", kerem_msg)
        if ses_aktif: play_on_air(kerem_msg, "Kerem")
    
    st.rerun()

with col_stats:
    st.subheader("📊 Reji Notları")
    st.success("Groq LPU: Aktif")
    st.warning("Azure Ses: Hazır")
    st.download_button("📥 Arşivi İndir", "\n".join([f"{m['char']}: {m['msg']}" for m in st.session_state.chat_history]), file_name="yayin_kaydi.txt")
