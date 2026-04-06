import streamlit as st
from groq import Groq
import edge_tts
import base64
import asyncio

# --- REJİ AYARLARI ---
st.set_page_config(page_title="OKEYSIN GLOBAL V11", layout="wide")

try:
    client = Groq(api_key=st.secrets["GROQ_API_KEY"])
except:
    st.error("⚠️ API Anahtarı Bulunamadı!")
    st.stop()

# --- STİL (QUANTUM DARK) ---
st.markdown("""
    <style>
    .stApp { background-color: #050505; color: #00f2ff; }
    .stChatMessage { border-radius: 15px; border: 1px solid #00f2ff33; margin-bottom: 10px; }
    .stChatInputContainer { padding-bottom: 20px; }
    </style>
    """, unsafe_allow_html=True)

# --- SOHBET HAFIZASI ---
if "messages" not in st.session_state:
    st.session_state.messages = []

# --- SES ÜRETİCİ ---
async def text_to_speech(text, voice_type):
    voice = "tr-TR-EmelNeural" if voice_type == "Okeysin" else "tr-TR-AhmetNeural"
    communicate = edge_tts.Communicate(text, voice)
    audio_data = b""
    async for chunk in communicate.stream():
        if chunk["type"] == "audio":
            audio_data += chunk["data"]
    return audio_data

# --- EKRAN AKIŞI ---
st.title("🎙️ OKEYSIN GLOBAL REJİ")
st.caption("Bursa'dan Dünyaya Kesintisiz Yayın")

# Geçmiş mesajları göster
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])
        if "audio" in msg:
            st.audio(msg["audio"], format="audio/mp3")

# --- KOMUT GİRİŞİ ---
if prompt := st.chat_input("Yönetmenim, yayına komut verin..."):
    # 1. Yönetmen mesajını göster
    with st.chat_message("user"):
        st.write(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # 2. Karakterlerin Cevabını Hazırla
    sys_prompt = "Sen Okeysin.com reji ekibisin. [OKEYSIN] (zarif kadın sunucu) ve [KEREM] (esprili erkek reji) olarak podcast formatında konuşun. Global ve bilgece bir dil kullanın."
    
    with st.spinner("Okeysin ve Kerem yayına hazırlanıyor..."):
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "system", "content": sys_prompt}] + 
                     [{"role": m["role"], "content": m["content"]} for m in st.session_state.messages]
        ).choices[0].message.content

    # 3. Cevabı Parçala ve Seslendir
    if "[OKEYSIN]" in response and "[KEREM]" in response:
        o_txt = response.split("[OKEYSIN]")[1].split("[KEREM]")[0].strip()
        k_txt = response.split("[KEREM]")[1].strip()

        # Okeysin Yayını
        audio_o = asyncio.run(text_to_speech(o_txt, "Okeysin"))
        with st.chat_message("assistant", avatar="🎙️"):
            st.markdown(f"**Okeysin:** {o_txt}")
            st.audio(audio_o, format="audio/mp3", autoplay=True)
        st.session_state.messages.append({"role": "assistant", "content": f"Okeysin: {o_txt}", "audio": audio_o})

        # Kerem Yayını
        audio_k = asyncio.run(text_to_speech(k_txt, "Kerem"))
        with st.chat_message("assistant", avatar="🎧"):
            st.markdown(f"**Kerem:** {k_txt}")
            st.audio(audio_k, format="audio/mp3")
        st.session_state.messages.append({"role": "assistant", "content": f"Kerem: {k_txt}", "audio": audio_k})
        
        # İndirme/Kopyalama için metin alanı (Opsiyonel)
        st.info("💡 Not: Mesajları kopyalamak için üzerlerine basılı tutabilir veya sağ tık yapabilirsiniz.")
