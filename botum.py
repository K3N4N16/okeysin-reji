import streamlit as st
from groq import Groq
import edge_tts
import base64
import asyncio
from datetime import datetime

# --- REJİ AYARLARI ---
st.set_page_config(page_title="OKEYSIN GLOBAL V12", layout="wide", page_icon="🎙️")

try:
    client = Groq(api_key=st.secrets["GROQ_API_KEY"])
except:
    st.error("⚠️ API Anahtarı Bulunamadı! Lütfen Streamlit Secrets ayarlarını yapın.")
    st.stop()

# --- ÖZEL TASARIM (GLOBAL DARK UI) ---
st.markdown("""
    <style>
    .stApp { background: linear-gradient(180deg, #050505 0%, #0a0a1a 100%); color: #e0e0e0; }
    .stChatMessage { border-radius: 20px; border: 1px solid #00f2ff22; background: rgba(0, 242, 255, 0.03); }
    .status-bar { padding: 10px; border-radius: 10px; background: rgba(0, 242, 255, 0.1); border: 1px solid #00f2ff44; margin-bottom: 20px; }
    .on-air { color: #ff0000; font-weight: bold; animation: blinker 1.5s linear infinite; }
    @keyframes blinker { 50% { opacity: 0; } }
    </style>
    """, unsafe_allow_html=True)

# --- SOHBET HAFIZASI ---
if "messages" not in st.session_state:
    st.session_state.messages = []

# --- SES ÜRETİCİ ---
async def text_to_speech(text, char):
    voice = "tr-TR-EmelNeural" if char == "Okeysin" else "tr-TR-AhmetNeural"
    try:
        communicate = edge_tts.Communicate(text, voice)
        audio_data = b""
        async for chunk in communicate.stream():
            if chunk["type"] == "audio":
                audio_data += chunk["data"]
        return audio_data
    except:
        return None

# --- REJİ PANELİ (ANA EKRAN) ---
st.markdown('<div class="status-bar">📡 <span class="on-air">● CANLI YAYIN:</span> Bursa Stüdyo ⮕ Global Uydu Bağlantısı</div>', unsafe_allow_html=True)

# Geçmiş mesajları ve araçları göster
for i, msg in enumerate(st.session_state.messages):
    with st.chat_message(msg["role"]):
        st.write(msg["content"])
        if "audio" in msg:
            st.audio(msg["audio"], format="audio/mp3")
            # İndirme ve Kopyalama Araçları
            col1, col2 = st.columns([1, 3])
            col1.download_button("📥 İndir", msg["content"], file_name=f"yayin_{i}.txt", key=f"dl_{i}")
            with col2:
                # Kopyalama için pratik alan
                st.text_area("📋 Metni Kopyala:", value=msg["content"], height=80, key=f"cp_{i}", label_visibility="collapsed")

# --- KOMUT GİRİŞİ ---
if prompt := st.chat_input("Yönetmenim, dünyaya ne söylemek istersiniz?"):
    # 1. Yönetmen Mesajı
    with st.chat_message("user"):
        st.write(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # 2. Global Podcast Kurgusu
    sys_prompt = """Sen Okeysin.com'un küresel reji ekibisin. 
    Karakterler: 
    1. OKEYSİN: Bilge, zarif, sanat ve dünya barışı aşığı bayan sunucu. 
    2. KEREM: Şakacı, teknikten anlayan, Okeysin'e 'Hocam' diye hitap eden reji adamı. 
    Her komutu karşılıklı diyalogla, [OKEYSIN] ... [KEREM] ... şeklinde yanıtla. 
    Konuları Bursa yerelliğinden çıkarıp evrensel bir boyuta taşı."""
    
    with st.spinner("Uydu bağlantısı kuruluyor..."):
        try:
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[{"role": "system", "content": sys_prompt}] + 
                         [{"role": m["role"], "content": m["content"]} for m in st.session_state.messages]
            ).choices[0].message.content

            if "[OKEYSIN]" in response and "[KEREM]" in response:
                o_txt = response.split("[OKEYSIN]")[1].split("[KEREM]")[0].strip()
                k_txt = response.split("[KEREM]")[1].strip()

                # Okeysin Yayını
                audio_o = asyncio.run(text_to_speech(o_txt, "Okeysin"))
                st.session_state.messages.append({"role": "assistant", "content": f"Okeysin: {o_txt}", "audio": audio_o})

                # Kerem Yayını
                audio_k = asyncio.run(text_to_speech(k_txt, "Kerem"))
                st.session_state.messages.append({"role": "assistant", "content": f"Kerem: {k_txt}", "audio": audio_k})
                
                st.rerun() # Yeni mesajları ve butonları yüklemek için
        except Exception as e:
            st.error(f"⚠️ Reji Hatası: {str(e)}")

# Sidebar Arşiv Yönetimi
with st.sidebar:
    st.title("🎙️ REJİ ARŞİVİ")
    if st.button("🗑️ Tüm Yayını Sıfırla"):
        st.session_state.messages = []
        st.rerun()
    st.divider()
    st.write(f"📅 Tarih: {datetime.now().strftime('%d.%m.%Y')}")
    st.write("🌍 Bölge: Global / Bursa")
