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
    st.error("⚠️ API Anahtarı Hatası! Lütfen Secrets ayarlarını kontrol edin.")
    st.stop()

MODEL_NAME = "llama-3.3-70b-versatile"
DB_FILE = "okeysin_v10.db"

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

# --- SES ÜRETİMİ (DOĞRUDAN BYTES) ---
async def get_voice_bytes(text, char):
    voice = "tr-TR-EmelNeural" if char == "Okeysin" else "tr-TR-AhmetNeural"
    try:
        communicate = edge_tts.Communicate(text, voice)
        audio_data = b""
        async for chunk in communicate.stream():
            if chunk["type"] == "audio":
                audio_data += chunk["data"]
        return audio_data
    except Exception as e:
        return None

# --- TASARIM VE UI ---
st.set_page_config(page_title="OKEYSIN GLOBAL V10", layout="wide")
init_db()

st.markdown("""
    <style>
    .stApp { background-color: #020205; color: #e0e0e0; }
    .chat-card { padding: 15px; border-radius: 12px; margin-bottom: 10px; border: 1px solid #333; }
    .okeysin-style { border-left: 5px solid #00f2ff; background: rgba(0,242,255,0.05); }
    .kerem-style { border-left: 5px solid #ffaa00; background: rgba(255,170,0,0.05); }
    .user-style { border-left: 5px solid #ffffff; background: rgba(255,255,255,0.05); }
    audio { width: 100%; height: 30px; margin-top: 10px; }
    </style>
    """, unsafe_allow_html=True)

# --- SOHBET GEÇMİŞİ YÜKLEME ---
if "messages" not in st.session_state:
    conn = sqlite3.connect(DB_FILE); c = conn.cursor()
    c.execute("SELECT role, content FROM chat")
    st.session_state.messages = [{"role": r, "content": m} for r, m in c.fetchall()]
    conn.close()

# --- SIDEBAR ---
with st.sidebar:
    st.title("🎙️ GLOBAL REJİ V10")
    st.info("📍 Bursa'dan Tüm Dünyaya")
    st.warning("💡 Ses gelmiyorsa, tarayıcıda sayfa için 'Ses' izni verin.")
    if st.button("🗑️ Arşivi Sıfırla"):
        conn = sqlite3.connect(DB_FILE); conn.cursor().execute("DELETE FROM chat"); conn.commit()
        st.session_state.messages = []
        st.rerun()

# --- EKRAN AKIŞI ---
for i, m in enumerate(st.session_state.messages):
    style = "user-style" if m["role"] == "user" else "okeysin-style"
    is_asst = m["role"] == "assistant"
    display_name = "Yönetmen" if m["role"] == "user" else ("Okeysin" if "Okeysin:" in m["content"] else "Kerem")
    
    with st.container():
        st.markdown(f'<div class="chat-card {style}"><b>{display_name}:</b><br>{m["content"]}</div>', unsafe_allow_html=True)
        if is_asst:
            # Ses Dosyasını Her Seferinde Üretmek Yerine Sadece Buraya Bir Buton Koyuyoruz (Opsiyonel)
            c1, c2, c3 = st.columns([1, 2, 2])
            c1.download_button("📥 İndir", m["content"], file_name=f"yayin_{i}.txt", key=f"dl_{i}")
            with c2:
                st.text_area("📋 Kopyala:", value=m["content"], height=70, key=f"cp_{i}", label_visibility="collapsed")

# --- KOMUT GİRİŞİ ---
if prompt := st.chat_input("Yönetmenim, bir konu verin..."):
    save_msg("user", prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    sys_msg = "Sen Okeysin.com reji ekibisin. [OKEYSIN] (zarif) ve [KEREM] (esprili) olarak podcast yap. Bursa'dan dünyaya global vizyonla konuş."

    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[{"role": "system", "content": sys_msg}] + st.session_state.messages
        ).choices[0].message.content

        if "[OKEYSIN]" in response and "[KEREM]" in response:
            o_txt = response.split("[OKEYSIN]")[1].split("[KEREM]")[0].strip()
            k_txt = response.split("[KEREM]")[1].strip()

            # Sesleri Üret
            audio_o = asyncio.run(get_voice_bytes(o_txt, "Okeysin"))
            audio_k = asyncio.run(get_voice_bytes(k_txt, "Kerem"))

            # Kaydet
            save_msg("assistant", f"Okeysin: {o_txt}")
            save_msg("assistant", f"Kerem: {k_txt}")
            st.session_state.messages.append({"role": "assistant", "content": f"Okeysin: {o_txt}"})
            st.session_state.messages.append({"role": "assistant", "content": f"Kerem: {k_txt}"})
            
            # SESLERİ EKRANA BAS (KESİN ÇÖZÜM)
            if audio_o:
                st.audio(audio_o, format="audio/mp3", autoplay=True)
                st.write("🎵 Okeysin konuşuyor...")
            
            if audio_k:
                # Kerem'in sesini biraz bekletmek için (Simülasyon)
                st.audio(audio_k, format="audio/mp3")
                st.write("🎵 Kerem hazır (Oynat'a basabilir veya bekleyebilirsiniz)")
            
            st.rerun()
    except Exception as e:
        st.error(f"⚠️ Hata: {str(e)}")
