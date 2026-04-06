import streamlit as st
from groq import Groq
import edge_tts
import base64
import asyncio

# --- 1. SAYFA VE API AYARLARI ---
st.set_page_config(page_title="OKEYSIN GLOBAL V14", layout="wide", page_icon="🎙️")

if "GROQ_API_KEY" not in st.secrets:
    st.error("⚠️ API Anahtarı Bulunamadı! Streamlit Secrets ayarlarını kontrol edin.")
    st.stop()

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

# --- 2. SES ÜRETİMİ ---
async def get_audio_data(text, char):
    voice = "tr-TR-EmelNeural" if char == "Okeysin" else "tr-TR-AhmetNeural"
    try:
        communicate = edge_tts.Communicate(text, voice)
        audio_bytes = b""
        async for chunk in communicate.stream():
            if chunk["type"] == "audio":
                audio_bytes += chunk["data"]
        return audio_bytes
    except:
        return None

# --- 3. HAFIZA (SESSION STATE) BAŞLATMA ---
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# --- 4. TASARIM ---
st.markdown("""
    <style>
    .stApp { background-color: #050505; color: #00f2ff; }
    .stChatMessage { border: 1px solid #00f2ff22; border-radius: 15px; background: rgba(0,242,255,0.02); }
    </style>
    """, unsafe_allow_html=True)

st.title("🎙️ GLOBAL REJİ V14")
st.caption("Bursa Stüdyolarından Dünyaya Kesintisiz Akış")

# --- 5. MESAJLARI GÖSTER ---
for i, chat in enumerate(st.session_state.chat_history):
    with st.chat_message(chat["role"]):
        st.write(chat["content"])
        
        if chat["role"] == "assistant":
            if "audio" in chat:
                st.audio(chat["audio"], format="audio/mp3")
            
            c1, c2 = st.columns([1, 4])
            c1.download_button("📥 İndir", chat["content"], file_name=f"yayin_{i}.txt", key=f"dl_{i}")
            with c2:
                st.text_area("📋 Kopyala:", value=chat["content"], height=70, key=f"cp_{i}", label_visibility="collapsed")

# --- 6. KOMUT VE CEVAP DÖNGÜSÜ ---
if prompt := st.chat_input("Yönetmenim, yayına komut verin..."):
    # Yönetmen mesajını ekle
    st.session_state.chat_history.append({"role": "user", "content": prompt})
    
    sys_prompt = "Sen Okeysin.com reji ekibisin. [OKEYSIN] (zarif sunucu) ve [KEREM] (esprili reji) karakterleriyle karşılıklı konuşun. Global vizyon kullanın."

    try:
        # Groq'tan Yanıt Al (Hata düzeltilen kısım burası)
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "system", "content": sys_prompt}] + 
                     [{"role": m["role"], "content": m["content"]} for m in st.session_state.chat_history]
        ).choices[0].message.content

        if "[OKEYSIN]" in response and "[KEREM]" in response:
            o_text = response.split("[OKEYSIN]")[1].split("[KEREM]")[0].strip()
            k_text = response.split("[KEREM]")[1].strip()

            # Sesleri Üret
            audio_o = asyncio.run(get_audio_data(o_text, "Okeysin"))
            audio_k = asyncio.run(get_audio_data(k_text, "Kerem"))

            # Hafızaya Kaydet
            st.session_state.chat_history.append({"role": "assistant", "content": f"Okeysin: {o_text}", "audio": audio_o})
            st.session_state.chat_history.append({"role": "assistant", "content": f"Kerem: {k_text}", "audio": audio_k})
            
            st.rerun()

    except Exception as e:
        st.error(f"⚠️ Reji Hatası: {str(e)}")

# --- 7. SIDEBAR ---
with st.sidebar:
    st.markdown("### 🎚️ KONTROL")
    if st.button("🗑️ Yayını Sıfırla"):
        st.session_state.chat_history = []
        st.rerun()
