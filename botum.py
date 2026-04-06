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
except:
    st.error("⚠️ GROQ_API_KEY bulunamadı! Secrets kısmına ekleyin.")
    st.stop()

client = Groq(api_key=GROQ_API_KEY)
MODEL_NAME = "llama-3.3-70b-versatile"
DB_FILE = "okeysin_global_v6.db"

# --- VERİTABANI ---
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

# --- KESİNTİSİZ SES KUYRUĞU (PLAYLIST) ---
async def generate_audio(text, char_type):
    voice = "tr-TR-EmelNeural" if char_type == "Okeysin" else "tr-TR-AhmetNeural"
    communicate = edge_tts.Communicate(text, voice)
    filename = f"voice_{char_type}_{datetime.now().strftime('%M%S')}.mp3"
    await communicate.save(filename)
    with open(filename, "rb") as f:
        data = f.read()
    os.remove(filename)
    return base64.b64encode(data).decode()

def play_dual_voices(text1, text2):
    b64_1 = asyncio.run(generate_audio(text1, "Okeysin"))
    b64_2 = asyncio.run(generate_audio(text2, "Kerem"))
    
    st.markdown(f"""
        <script>
        var audio1 = new Audio("data:audio/mp3;base64,{b64_1}");
        var audio2 = new Audio("data:audio/mp3;base64,{b64_2}");
        audio1.play();
        audio1.onended = function() {{
            setTimeout(function() {{ audio2.play(); }}, 600);
        }};
        </script>
    """, unsafe_allow_html=True)

# --- TASARIM (GLOBAL REJİ UI) ---
st.set_page_config(page_title="OKEYSIN GLOBAL V6", layout="wide")
init_db()

st.markdown("""
    <style>
    .stApp { background: linear-gradient(135deg, #020205 0%, #050515 100%); color: #e0e0e0; }
    .chat-card { background: rgba(255, 255, 255, 0.02); border: 1px solid rgba(0, 242, 255, 0.15); border-radius: 15px; padding: 20px; margin-bottom: 20px; box-shadow: 0 4px 15px rgba(0,0,0,0.5); }
    .label-okey { color: #00f2ff; font-weight: 800; letter-spacing: 1px; text-transform: uppercase; font-size: 0.8rem; margin-bottom: 10px; display: block; }
    .label-kerem { color: #ffaa00; font-weight: 800; letter-spacing: 1px; text-transform: uppercase; font-size: 0.8rem; margin-bottom: 10px; display: block; }
    .copy-area { background: #000 !important; color: #00f2ff !important; font-family: monospace !important; border: 1px solid #333 !important; }
    .on-air-pulse { color: #ff0000; font-weight: bold; animation: pulse 2s infinite; }
    @keyframes pulse { 0% { opacity: 1; } 50% { opacity: 0.3; } 100% { opacity: 1; } }
    </style>
    """, unsafe_allow_html=True)

# --- SİDEBAR ---
with st.sidebar:
    st.title("🌍 GLOBAL BROADCAST")
    st.markdown('<p class="on-air-pulse">● LIVE FROM EARTH</p>', unsafe_allow_html=True)
    st.divider()
    st.write("🌐 **Kapsam:** Dünya Geneli")
    st.write("📡 **Yayın:** Okeysin.com / Bot")
    st.divider()
    if st.button("🗑️ Yayın Akışını Sıfırla"):
        conn = sqlite3.connect(DB_FILE); conn.cursor().execute("DELETE FROM broadcast_logs"); conn.commit(); st.rerun()

# --- YAYIN AKIŞI ---
if "chat_history" not in st.session_state:
    conn = sqlite3.connect(DB_FILE); c = conn.cursor(); c.execute("SELECT character, message FROM broadcast_logs")
    st.session_state.chat_history = [{"char": r, "msg": m} for r, m in c.fetchall()]; conn.close()

col_left, col_right = st.columns([3, 1])

with col_left:
    for i, entry in enumerate(st.session_state.chat_history):
        if entry["char"] in ["Okeysin", "Kerem"]:
            lbl = "label-okey" if entry["char"] == "Okeysin" else "label-kerem"
            st.markdown(f'<div class="chat-card"><span class="{lbl}">{entry["char"]}</span>{entry["msg"]}</div>', unsafe_allow_html=True)
            # Kopyalama ve İndirme Paneli
            with st.expander(f"📥 Arşivle & Kopyala ({entry['char']})"):
                st.text_area("Metni Seç ve Kopyala:", value=entry["msg"], height=100, key=f"cp_{i}", label_visibility="collapsed")
                st.download_button("📄 Dosya Olarak İndir", entry["msg"], file_name=f"yayin_{i}.txt", key=f"dl_{i}")

# --- YÖNETMEN KOMUTU ---
if prompt := st.chat_input("Dünyaya ne söylemek istersiniz yönetmenim?"):
    st.session_state.chat_history.append({"char": "Yönetmen", "msg": prompt})
    
    sys_prompt = f"""
    Sen Okeysin.com'un küresel yayın ekibisin. 
    KİMLİKLER:
    1. OKEYSİN: Bursa kökenli ama dünya vatandaşı, son derece entelektüel, zarif ve bilge bir kadın sunucu. Sinema, sanat ve felsefe aşığı.
    2. KEREM: Okeysin'in reji ortağı. Esprili, samimi, bazen 'Hocam amma derinlere daldık yine' diyen ama işine aşık bir teknik adam.
    
    YÖNERGE: Konuyu yerel sınırlardan çıkar. Evrensel bir dil kullan. 
    Yönetmen Komutu: "{prompt}"
    FORMAT: [OKEYSIN] ... [KEREM] ... şeklinde yanıtla. Podcast akışında olsun.
    """

    res = client.chat.completions.create(model=MODEL_NAME, messages=[{"role": "system", "content": sys_prompt}]).choices[0].message.content

    if "[OKEYSIN]" in res and "[KEREM]" in res:
        o_msg = res.split("[OKEYSIN]")[1].split("[KEREM]")[0].strip()
        k_msg = res.split("[KEREM]")[1].strip()
        
        st.session_state.chat_history.append({"char": "Okeysin", "msg": o_msg})
        log_broadcast("Okeysin", o_msg)
        st.session_state.chat_history.append({"char": "Kerem", "msg": k_msg})
        log_broadcast("Kerem", k_msg)
        
        play_dual_voices(o_msg, k_msg)
            
    st.rerun()
