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
DB_FILE = "okeysin_v7.db"

# --- VERİTABANI İŞLEMLERİ ---
def init_db():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS chat (id INTEGER PRIMARY KEY AUTOINCREMENT, char TEXT, msg TEXT)''')
    conn.commit()
    conn.close()

def save_msg(char, msg):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("INSERT INTO chat (char, msg) VALUES (?, ?)", (char, msg))
    conn.commit()
    conn.close()

# --- SES ÜRETİMİ VE OYNATMA ---
async def make_audio(text, char):
    voice = "tr-TR-EmelNeural" if char == "Okeysin" else "tr-TR-AhmetNeural"
    comm = edge_tts.Communicate(text, voice)
    b_data = b""
    async for chunk in comm.stream():
        if chunk["type"] == "audio":
            b_data += chunk["data"]
    return base64.b64encode(b_data).decode()

def play_audio_js(b64_1, b64_2):
    # JavaScript ile sesleri sırayla çaldırma (Kesilme olmaz)
    js = f"""
        <script>
        var a1 = new Audio("data:audio/mp3;base64,{b64_1}");
        var a2 = new Audio("data:audio/mp3;base64,{b64_2}");
        a1.play();
        a1.onended = function() {{ setTimeout(() => {{ a2.play(); }}, 500); }};
        </script>
    """
    st.components.v1.html(js, height=0)

# --- TASARIM VE SAYFA YAPISI ---
st.set_page_config(page_title="OKEYSIN GLOBAL V7", layout="wide")
init_db()

st.markdown("""
    <style>
    .stApp { background: #050505; color: #00f2ff; }
    [data-testid="stChatMessage"] { background: rgba(0,242,255,0.05); border: 1px solid #00f2ff33; border-radius: 15px; }
    .stButton button { border-radius: 10px; border: 1px solid #00f2ff; background: transparent; color: #00f2ff; }
    </style>
    """, unsafe_allow_html=True)

# --- SİDEBAR ---
with st.sidebar:
    st.title("🎙️ GLOBAL V7")
    st.success("🟢 ON AIR")
    if st.button("🗑️ Sohbeti Sıfırla"):
        conn = sqlite3.connect(DB_FILE); conn.cursor().execute("DELETE FROM chat"); conn.commit()
        st.session_state.messages = []
        st.rerun()

# --- MESAJLAŞMA SİSTEMİ ---
if "messages" not in st.session_state:
    conn = sqlite3.connect(DB_FILE); c = conn.cursor()
    c.execute("SELECT char, msg FROM chat")
    st.session_state.messages = [{"role": r, "content": m} for r, m in c.fetchall()]
    conn.close()

# Geçmiş Mesajları Ekrana Bas (Anlık Gözükmesi İçin)
for i, m in enumerate(st.session_state.messages):
    with st.chat_message(m["role"]):
        st.write(m["content"])
        if m["role"] != "user":
            col1, col2 = st.columns([1, 4])
            col1.download_button("📥 İndir", m["content"], file_name=f"yayin_{i}.txt", key=f"dl_{i}")
            with col2:
                st.text_area("📋 Kopyala:", value=m["content"], height=70, key=f"cp_{i}", label_visibility="collapsed")

# --- GİRİŞ VE CEVAP DÖNGÜSÜ ---
if prompt := st.chat_input("Yönetmenim, konu nedir?"):
    # 1. Kullanıcı mesajını anında göster ve kaydet
    st.chat_message("user").write(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})
    save_msg("user", prompt)

    # 2. Groq'tan cevap al (Okeysin ve Kerem Ortak)
    sys = "OKEYSİN (zarif bayan sunucu) ve KEREM (esprili reji) olarak podcast formatında, [OKEYSIN] ... [KEREM] ... şeklinde yanıtla. Bursa'dan dünyaya açılan global bir vizyon kullan."
    
    res = client.chat.completions.create(
        model=MODEL_NAME, 
        messages=[{"role": "system", "content": sys}] + st.session_state.messages
    ).choices[0].message.content

    if "[OKEYSIN]" in res and "[KEREM]" in res:
        o_txt = res.split("[OKEYSIN]")[1].split("[KEREM]")[0].strip()
        k_txt = res.split("[KEREM]")[1].strip()

        # Kaydet ve Ekrana Bas
        for char, txt in [("Okeysin", o_txt), ("Kerem", k_txt)]:
            st.session_state.messages.append({"role": char, "content": txt})
            save_msg(char, txt)
        
        # Sesleri Üret ve Oynat
        b64_o = asyncio.run(make_audio(o_txt, "Okeysin"))
        b64_k = asyncio.run(make_audio(k_txt, "Kerem"))
        play_audio_js(b64_o, b64_k)
        
        st.rerun() # Yeni mesajların butonlarla birlikte yüklenmesi için
