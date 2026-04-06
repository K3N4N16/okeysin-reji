import os
import sqlite3
import base64
import asyncio
import edge_tts
import streamlit as st
from groq import Groq
from datetime import datetime

# --- KRİTİK AYARLAR --- 
client = Groq(api_key=GROQ_API_KEY)
MODEL_NAME = "llama-3.3-70b-versatile"
DB_FILE = "okeysin_god_mode.db"

# --- VERİTABANI MİMARİSİ ---
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

# --- SES MOTORU (ÇİFT KARAKTER) ---
async def generate_audio(text, char_type, filename):
    # Okeysin: Emel (Zarif), Kerem: Ahmet (Sert/Teknik)
    voice = "tr-TR-EmelNeural" if char_type == "Okeysin" else "tr-TR-AhmetNeural"
    communicate = edge_tts.Communicate(text, voice)
    await communicate.save(filename)

def play_on_air(text, char):
    audio_file = f"on_air_{char}.mp3"
    asyncio.run(generate_audio(text, char, audio_file))
    with open(audio_file, "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
        st.markdown(f'<audio autoplay src="data:audio/mp3;base64,{b64}"></audio>', unsafe_allow_html=True)
    return data

# --- SAYFA TASARIMI (QUANTUM DASHBOARD) ---
st.set_page_config(page_title="OKEYSIN GLOBAL REJİ V4", layout="wide")
init_db()

st.markdown("""
    <style>
    .stApp { background: #020205; color: #e0e0e0; }
    .reji-card { background: rgba(0, 242, 255, 0.05); border: 1px solid #00f2ff44; border-radius: 15px; padding: 20px; margin-bottom: 15px; box-shadow: 0 0 20px #00f2ff11; }
    .status-on-air { color: #ff0000; font-weight: bold; animation: blinker 1.5s linear infinite; }
    @keyframes blinker { 50% { opacity: 0; } }
    .chat-okeysin { border-left: 5px solid #00f2ff; background: rgba(0,242,255,0.05); padding: 15px; border-radius: 10px; }
    .chat-kerem { border-left: 5px solid #ffaa00; background: rgba(255,170,0,0.05); padding: 15px; border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

# --- REJİ MASASI (SIDEBAR) ---
with st.sidebar:
    st.image("https://img.icons8.com/neon/96/experimental-radio-tower-neon.png", width=100)
    st.title("🎙️ GLOBAL REJİ V4")
    st.markdown('<p class="status-on-air">● CANLI YAYINDA</p>', unsafe_allow_html=True)
    
    with st.expander("📊 SİSTEM VERİLERİ", expanded=True):
        st.write("📍 Konum: Bursa Stüdyo")
        st.write("🧠 İşlemci: Groq LPU (Cloud)")
        st.write("👥 Aktif Oyuncu: 1.240 (Okeysin.com)")
    
    st.divider()
    podcast_modu = st.toggle("Podcast Modu (Çift Sunucu)", value=True)
    ses_aktif = st.toggle("Sesli Anons", value=True)
    
    if st.button("🗑️ TÜM ARŞİVİ SIFIRLA"):
        conn = sqlite3.connect(DB_FILE); conn.cursor().execute("DELETE FROM broadcast_logs"); conn.commit(); st.rerun()

# --- YAYIN AKIŞI (ANA EKRAN) ---
col_main, col_stats = st.columns([3, 1])

with col_main:
    # Geçmişi Yükle
    if "chat_history" not in st.session_state:
        conn = sqlite3.connect(DB_FILE); c = conn.cursor(); c.execute("SELECT character, message FROM broadcast_logs")
        st.session_state.chat_history = [{"char": r, "msg": m} for r, m in c.fetchall()]; conn.close()

    for entry in st.session_state.chat_history:
        css_class = "chat-okeysin" if entry["char"] == "Okeysin" else "chat-kerem"
        st.markdown(f'<div class="{css_class}"><b>{entry["char"]}:</b><br>{entry["msg"]}</div><br>', unsafe_allow_html=True)

# --- YÖNETMEN KOMUT GİRİŞİ ---
if prompt := st.chat_input("Yönetmenim, yayına komut verin..."):
    # 1. Yönetmen Mesajı
    st.session_state.chat_history.append({"char": "Yönetmen", "msg": prompt})
    
    # 2. Groq Üretimi (Çift Karakter Mantığı)
    sys_prompt = f"""
    Sen dünyanın en gelişmiş radyo reji yazılımısın. İki karakteri yönetiyorsun:
    1. OKEYSİN: Bursa'lı, elit, zarif, entelektüel kadın sunucu.
    2. KEREM: Şakacı, teknikten anlayan, Okeysin'e 'Hocam' diye hitap eden erkek teknisyen.
    
    Yönetmen şunu dedi: "{prompt}"
    
    GÖREV: Önce Okeysin konuşsun, ardından Kerem ona teknik bir detayla veya bir şakayla cevap versin. 
    İkisinin konuşmasını [OKEYSIN] ... [KEREM] ... şeklinde ayır. 
    Bursa havasından, Okeysin.com turnuvalarından ve güncel popülerlikten bahset.
    """

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[{"role": "system", "content": sys_prompt}],
    ).choices[0].message.content

    # Yanıtı Parçala ve Yayına Ver
    if "[OKEYSIN]" in response and "[KEREM]" in response:
        okey_text = response.split("[OKEYSIN]")[1].split("[KEREM]")[0].strip()
        kerem_text = response.split("[KEREM]")[1].strip()
        
        # Okeysin Anonsu
        st.session_state.chat_history.append({"char": "Okeysin", "msg": okey_text})
        log_broadcast("Okeysin", okey_text)
        if ses_aktif: play_on_air(okey_text, "Okeysin")
        
        # Kerem Cevabı (Podcast tadında)
        if podcast_modu:
            st.session_state.chat_history.append({"char": "Kerem", "msg": kerem_text})
            log_broadcast("Kerem", kerem_text)
            if ses_aktif: asyncio.run(asyncio.sleep(1)); play_on_air(kerem_text, "Kerem")
    
    st.rerun()

with col_stats:
    st.markdown('<div class="reji-card"><b>⭐ FAVORİ ANONS</b><br><small>Bursa ipeği gibi zarif bir yayın dileriz.</small></div>', unsafe_allow_html=True)
    st.download_button("📥 YAYIN KAYDINI AL (TXT)", "\n".join([f"{m['char']}: {m['msg']}" for m in st.session_state.chat_history]), file_name="yayin_arsivi.txt")
    st.info("💡 Not: Groq Cloud üzerinden 0.2ms hızla işlem yapılıyor.")
