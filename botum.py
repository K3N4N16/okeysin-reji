import os
import sqlite3
import base64
import asyncio
import edge_tts
import streamlit as st
from groq import Groq
from datetime import datetime

# --- GÜVENLİ API SİSTEMİ ---
try:
    GROQ_API_KEY = st.secrets["GROQ_API_KEY"]
    client = Groq(api_key=GROQ_API_KEY)
except Exception as e:
    st.error("⚠️ API Anahtarı Hatası: Lütfen Streamlit Secrets ayarlarını kontrol edin.")
    st.stop()

MODEL_NAME = "llama-3.3-70b-versatile"
DB_FILE = "okeysin_v8.db"

# --- VERİTABANI ---
def init_db():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS chat (id INTEGER PRIMARY KEY AUTOINCREMENT, char TEXT, msg TEXT, ts TEXT)''')
    conn.commit()
    conn.close()

def save_msg(char, msg):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    ts = datetime.now().strftime("%H:%M:%S")
    c.execute("INSERT INTO chat (char, msg, ts) VALUES (?, ?, ?)", (char, msg, ts))
    conn.commit()
    conn.close()

# --- SES ÜRETİMİ (GELİŞMİŞ) ---
async def get_voice_b64(text, char):
    voice = "tr-TR-EmelNeural" if char == "Okeysin" else "tr-TR-AhmetNeural"
    communicate = edge_tts.Communicate(text, voice)
    audio_data = b""
    async for chunk in communicate.stream():
        if chunk["type"] == "audio":
            audio_data += chunk["data"]
    return base64.b64encode(audio_data).decode()

# --- TASARIM ---
st.set_page_config(page_title="OKEYSIN GLOBAL V8", layout="wide")
init_db()

st.markdown("""
    <style>
    .stApp { background-color: #020205; color: #e0e0e0; }
    .chat-box { padding: 15px; border-radius: 15px; margin-bottom: 10px; border: 1px solid #333; }
    .okeysin-style { border-left: 5px solid #00f2ff; background: rgba(0,242,255,0.05); }
    .kerem-style { border-left: 5px solid #ffaa00; background: rgba(255,170,0,0.05); }
    .user-style { border-left: 5px solid #ffffff; background: rgba(255,255,255,0.05); }
    </style>
    """, unsafe_allow_html=True)

# --- SİDEBAR ---
with st.sidebar:
    st.title("🎙️ GLOBAL REJİ V8")
    st.info("📍 Bursa'dan Dünyaya")
    if st.button("🗑️ Arşivi Temizle"):
        conn = sqlite3.connect(DB_FILE); conn.cursor().execute("DELETE FROM chat"); conn.commit()
        st.session_state.messages = []
        st.rerun()

# --- MESAJLARI YÜKLE ---
if "messages" not in st.session_state:
    conn = sqlite3.connect(DB_FILE); c = conn.cursor()
    c.execute("SELECT char, msg FROM chat")
    st.session_state.messages = [{"role": r, "content": m} for r, m in c.fetchall()]
    conn.close()

# --- EKRANA BASMA DÖNGÜSÜ ---
for i, m in enumerate(st.session_state.messages):
    style = "okeysin-style" if m["role"] == "Okeysin" else "kerem-style" if m["role"] == "Kerem" else "user-style"
    with st.container():
        st.markdown(f'<div class="chat-box {style}"><b>{m["role"]}:</b><br>{m["content"]}</div>', unsafe_allow_html=True)
        if m["role"] in ["Okeysin", "Kerem"]:
            c1, c2 = st.columns([1, 4])
            c1.download_button("📥 İndir", m["content"], file_name=f"anons_{i}.txt", key=f"dl_{i}")
            with c2:
                st.text_area("📋 Kopyala:", value=m["content"], height=70, key=f"cp_{i}", label_visibility="collapsed")

# --- KOMUT GİRİŞİ ---
if prompt := st.chat_input("Yönetmenim, yayındayız..."):
    # Kullanıcı mesajını kaydet
    save_msg("Yönetmen", prompt)
    st.session_state.messages.append({"role": "Yönetmen", "content": prompt})
    
    # Podcast Formatında Yanıt Üret
    sys_msg = """Sen Okeysin.com reji ekibisin. İki karakterin var:
    1. OKEYSİN: Zarif, entelektüel, global vizyonlu bayan sunucu.
    2. KEREM: Esprili, teknik reji adamı.
    Yönetmenin her komutuna [OKEYSIN] ... [KEREM] ... şeklinde karşılıklı diyalogla cevap ver. 
    Konuyu Bursa'dan alıp dünya gündemine, sanata veya okey masalarına taşı."""

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[{"role": "system", "content": sys_msg}] + st.session_state.messages
    ).choices[0].message.content

    if "[OKEYSIN]" in response and "[KEREM]" in response:
        o_txt = response.split("[OKEYSIN]")[1].split("[KEREM]")[0].strip()
        k_txt = response.split("[KEREM]")[1].strip()

        # Sesleri Hazırla
        b64_o = asyncio.run(get_voice_b64(o_txt, "Okeysin"))
        b64_k = asyncio.run(get_voice_b64(k_txt, "Kerem"))

        # Kaydet
        save_msg("Okeysin", o_txt)
        save_msg("Kerem", k_txt)
        
        # SES OYNATICI (JavaScript Playlist)
        js_code = f"""
            <script>
            var audioO = new Audio("data:audio/mp3;base64,{b64_o}");
            var audioK = new Audio("data:audio/mp3;base64,{b64_k}");
            audioO.play();
            audioO.onended = function() {{
                setTimeout(function() {{ audioK.play(); }}, 600);
            }};
            </script>
        """
        st.components.v1.html(js_code, height=0)
        
        # Sayfayı Yenile (Mesajlar ekrana düşsün)
        st.rerun()
