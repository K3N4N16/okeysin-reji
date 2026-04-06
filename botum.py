import streamlit as st
from groq import Groq
import edge_tts
import asyncio
import base64
import random
from datetime import datetime

# --- 1. GLOBAL KONFİGÜRASYON ---
st.set_page_config(page_title="OKEYSIN GLOBAL V18", layout="wide", page_icon="📡")

if "GROQ_API_KEY" not in st.secrets:
    st.error("⚠️ API Key Eksik!")
    st.stop()

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

# --- 2. PROFESYONEL REJİ TASARIMI (QUANTUM V3) ---
st.markdown("""
    <style>
    .stApp { background: #020205; color: #e0e0e0; }
    .broadcast-card {
        background: rgba(10, 10, 35, 0.6);
        border-left: 4px solid #00f2ff;
        border-radius: 10px;
        padding: 20px;
        margin-bottom: 15px;
        backdrop-filter: blur(5px);
    }
    .playlist-card {
        background: linear-gradient(90deg, #1a1a1a 0%, #000 100%);
        border: 1px dashed #00f2ff55;
        border-radius: 10px;
        padding: 15px;
        margin: 10px 0;
    }
    .on-air-blink {
        color: #ff0000;
        font-weight: bold;
        animation: blink 1s infinite;
    }
    @keyframes blink { 50% { opacity: 0; } }
    </style>
    """, unsafe_allow_html=True)

# --- 3. AKILLI SES & MÜZİK MOTORU ---
async def generate_voice(text, char):
    voice = "tr-TR-EmelNeural" if char == "Okeysin" else "tr-TR-AhmetNeural"
    try:
        comm = edge_tts.Communicate(text, voice)
        data = b""
        async for chunk in comm.stream():
            if chunk["type"] == "audio":
                data += chunk["data"]
        return data
    except: return None

# --- 4. HAFIZA & YAYIN AKIŞI ---
if "messages" not in st.session_state:
    st.session_state.messages = []

# --- 5. ANA EKRAN ---
st.markdown('### 📡 <span class="on-air-blink">● LIVE:</span> BURSA GLOBAL HUB V18', unsafe_allow_html=True)

for i, msg in enumerate(st.session_state.messages):
    with st.container():
        if msg["role"] == "user":
            st.info(f"🎤 Yönetmen: {msg['content']}")
        else:
            name_color = "#00f2ff" if "Okeysin" in msg["name"] else "#ffaa00"
            st.markdown(f"""
                <div class="broadcast-card">
                    <b style="color:{name_color}; letter-spacing:1px;">{msg['name']}</b><br>
                    {msg['content']}
                </div>
            """, unsafe_allow_html=True)
            
            # Araç Paneli
            with st.expander("🛠️ Reji Araçları"):
                c1, c2, c3 = st.columns([2, 2, 4])
                with c1: 
                    if "audio" in msg: st.audio(msg["audio"], format="audio/mp3")
                with c2: st.download_button("📥 Kayıt", msg["content"], file_name=f"yayin_{i}.txt", key=f"dl_{i}")
                with c3: st.text_area("📋 Kopyala", value=msg["content"], key=f"cp_{i}", label_visibility="collapsed")

# --- 6. YAYIN TETİKLEYİCİ ---
if prompt := st.chat_input("Yönetmenim, yayına yeni bir yön verin..."):
    st.session_state.messages.append({"role": "user", "name": "YÖNETMEN", "content": prompt})
    
    sys_instruction = """
    Sen dünyanın en donanımlı radyo istasyonusun. 
    [OKEYSIN]: Bursa'dan dünyaya seslenen bilge, nazik kadın sunucu. Dünya edebiyatı, şairler ve klasikleşmiş müzikler onun uzmanlığı.
    [KEREM]: Global gazete manşetleri, sosyal medya gündemi ve teknik reji adamı. 
    
    YAYIN AKIŞI KURALLARI:
    1. Önce birbirinizi selamlayın (eğer yayın yeni başlıyorsa).
    2. Yönetmenin konusunu dünya kültürüyle harmanlayarak tartışın.
    3. HER YAYINDA mutlaka o anki konuya uygun bir "Playlist Önerisi" (3 şarkı: Sanatçı - Şarkı) sunun.
    4. Cevabın sonunda mutlaka birbirinize bir soru sorarak veya 'Sıradaki haberimize geçelim mi?' diyerek akışı canlı tutun.
    FORMAT: [OKEYSIN] ... [KEREM] ...
    """

    with st.spinner("Stüdyo hazırlanıyor, plaklar dönüyor..."):
        try:
            res = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[{"role": "system", "content": sys_instruction}] + 
                         [{"role": m["role"], "content": m["content"]} for m in st.session_state.messages]
            ).choices[0].message.content

            if "[OKEYSIN]" in res and "[KEREM]" in res:
                o_text = res.split("[OKEYSIN]")[1].split("[KEREM]")[0].strip()
                k_text = res.split("[KEREM]")[1].strip()

                audio_o = asyncio.run(generate_voice(o_text, "Okeysin"))
                audio_k = asyncio.run(generate_voice(k_text, "Kerem"))

                st.session_state.messages.append({"role": "assistant", "name": "🎙️ OKEYSİN", "content": o_text, "audio": audio_o})
                st.session_state.messages.append({"role": "assistant", "name": "🎧 KEREM", "content": k_text, "audio": audio_k})
                
                st.rerun()
        except Exception as e:
            st.error(f"📡 Kesinti: {e}")

# Sidebar
with st.sidebar:
    st.image("https://img.icons8.com/neon/96/microphone.png", width=80)
    st.markdown("### 🎚️ MIXER")
    if st.button("🗑️ Arşivi Sıfırla"):
        st.session_state.messages = []
        st.rerun()
    st.divider()
    st.markdown("🌍 **Mod:** Global Broadcast")
    st.markdown("🎶 **Playlist:** Otomatik Kürasyon Aktif")
