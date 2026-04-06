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
except Exception:
    st.error("⚠️ API Anahtarı Hatası! Lütfen Secrets ayarlarını yapın.")
    st.stop()

MODEL_NAME = "llama-3.3-70b-versatile"
DB_FILE = "okeysin_v9.db"

# --- VERİTABANI YÖNETİMİ ---
def init_db():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS chat (id INTEGER PRIMARY KEY AUTOINCREMENT, role TEXT, content TEXT)''')
    conn.commit()
    conn.close()

def save_msg(role, content):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("INSERT INTO chat (role, content) VALUES (?, ?)", (role, content))
    conn.commit()
    conn.close()

# --- SES ÜRETİMİ ---
async def get_voice_b64(text, char):
    voice = "tr-TR-EmelNeural" if char == "Okeysin" else "tr-TR-AhmetNeural"
    try:
        communicate = edge_tts.Communicate(text, voice)
        audio_data = b""
        async for chunk in communicate.stream():
            if chunk["type"] == "audio":
                audio_data += chunk["data"]
        return base64.b64encode(audio_data).decode()
    except:
        return None

# --- TASARIM VE UI ---
st.set_page_config(page_title="OKEYSIN GLOBAL REJİ V9", layout="wide")
init_db()

st.markdown("""
    <style>
    .stApp { background-color: #020205; color: #e0e0e0; }
    .chat-card { padding: 15px; border-radius: 12px; margin-bottom: 10px; border: 1px solid #333; }
    .okeysin-style { border-left: 5px solid #00f2ff; background: rgba(0,242,255,0.05); }
    .kerem-style { border-left: 5px solid #ffaa00; background: rgba(255,170,0,0.05); }
    .user-style { border-left: 5px solid #ffffff; background: rgba(255,255,255,0.05); }
    </style>
    """, unsafe_allow_html=True)

# --- SOHBET GEÇMİŞİ YÜKLEME ---
if "messages" not in st.session_state:
    conn = sqlite3.connect(DB_FILE); c = conn.cursor()
    c.execute("SELECT role, content FROM chat")
    # Groq için doğru format: role (user/assistant) ve content
    st.session_state.messages = [{"role": r if r in ["user", "assistant"] else "assistant", "content": c_val} for r, c_val in c.fetchall()]
    conn.close()

# --- REJİ PANELİ (SIDEBAR) ---
with st.sidebar:
    st.title("🎙️ GLOBAL REJİ V9")
    st.info("📍 Bursa'dan Tüm Dünyaya")
    if st.button("🗑️ Arşivi Sıfırla"):
        conn = sqlite3.connect(DB_FILE); conn.cursor().execute("DELETE FROM chat"); conn.commit()
        st.session_state.messages = []
        st.rerun()

# --- EKRAN AKIŞI ---
for i, m in enumerate(st.session_state.messages):
    style = "user-style" if m["role"] == "user" else "okeysin-style" # Basit ayrım
    # Karakter adını mesajın başından anlamaya çalışalım
    display_name = "Yönetmen" if m["role"] == "user" else ("Okeysin" if "Okeysin" in m["content"][:20] else "Kerem")
    
    with st.container():
        st.markdown(f'<div class="chat-card {style}"><b>{display_name}:</b><br>{m["content"]}</div>', unsafe_allow_html=True)
        if m["role"] == "assistant":
            c1, c2 = st.columns([1, 4])
            c1.download_button("📥 İndir", m["content"], file_name=f"yayin_{i}.txt", key=f"dl_{i}")
            with c2:
                st.text_area("📋 Kopyala:", value=m["content"], height=70, key=f"cp_{i}", label_visibility="collapsed")

# --- KOMUT GİRİŞİ ---
if prompt := st.chat_input("Yönetmenim, yayındayız..."):
    # Mesajı Kaydet (Format: user/assistant)
    save_msg("user", prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Podcast Talimatı
    sys_msg = "Sen Okeysin.com reji ekibisin. [OKEYSIN] (zarif sunucu) ve [KEREM] (esprili reji) karakterleriyle karşılıklı konuşma üret. Dünya olaylarını bilgece ve barışçıl bir dille analiz et."

    try:
        # Groq'a gönderirken sadece user/assistant rollerini gönderiyoruz
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[{"role": "system", "content": sys_msg}] + st.session_state.messages
        ).choices[0].message.content

        if "[OKEYSIN]" in response and "[KEREM]" in response:
            o_txt = response.split("[OKEYSIN]")[1].split("[KEREM]")[0].strip()
            k_txt = response.split("[KEREM]")[1].strip()

            # Sesleri Hazırla (B64)
            b64_o = asyncio.run(get_voice_b64(o_txt, "Okeysin"))
            b64_k = asyncio.run(get_voice_b64(k_txt, "Kerem"))

            # Kaydet (Assistant olarak)
            save_msg("assistant", f"Okeysin: {o_txt}")
            save_msg("assistant", f"Kerem: {k_txt}")
            st.session_state.messages.append({"role": "assistant", "content": f"Okeysin: {o_txt}"})
            st.session_state.messages.append({"role": "assistant", "content": f"Kerem: {k_txt}"})
            
            # JavaScript Ses Kuyruğu
            if b64_o and b64_k:
                js_code = f"""
                    <script>
                    var aO = new Audio("data:audio/mp3;base64,{b64_o}");
                    var aK = new Audio("data:audio/mp3;base64,{b64_k}");
                    aO.play();
                    aO.onended = function() {{ setTimeout(() => {{ aK.play(); }}, 600); }};
                    </script>
                """
                st.components.v1.html(js_code, height=0)
            
            st.rerun()
    except Exception as e:
        st.error(f"⚠️ Yayın Hatası: {str(e)}")
