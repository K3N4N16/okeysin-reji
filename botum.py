import streamlit as st
from groq import Groq
import asyncio
import edge_tts
import time

# --- REJİ AYARLARI ---
st.set_page_config(page_title="Faslı Muhabbet v10.5", layout="wide")

if "GROQ_API_KEY" not in st.secrets:
    st.error("⚠️ GROQ API Key Eksik!")
    st.stop()

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

if "history" not in st.session_state:
    st.session_state.history = []

# --- SES KÜTÜPHANESİ ---
# Senin klon sesini entegre edene kadar en doğal kurumsal sesler:
VOICES = {
    "Dilay 💖": "tr-TR-EmelNeural", # Cilveli ve enerjik
    "Mert 🎙️": "tr-TR-AhmetNeural"  # Tok ve samimi erkek sesi
}

async def generate_audio(text, voice):
    communicate = edge_tts.Communicate(text, voice, rate="+5%")
    audio_bytes = b""
    async for chunk in communicate.stream():
        if chunk["type"] == "audio":
            audio_bytes += chunk["data"]
    return audio_bytes

# --- SİSTEM TALİMATLARI (PROMPT) ---
def get_persona(name, partner):
    if "Dilay" in name:
        return f"""Sen Dilay'sın. Faslı Muhabbet'in neşeli, işveli kadın sunucususun. 
        Yanında partnerin {partner} var. Onunla tatlı sert atış, şakalaş. 
        Patron'a (Kullanıcı) 'Canım Patronum' de. Radyo dilinde, kısa ve etkileyici konuş."""
    else:
        return f"""Sen Mert'sin. Programın ağırbaşlı ama hazırcevap erkek sunucususun. 
        Yanında {partner} var. Onun cilvelerine beyefendi bir tavırla ama esprili karşılıklar ver. 
        Programın akışını bozmadan muhabbeti sürdür."""

# --- ARAYÜZ ---
st.markdown("<h1 style='text-align: center; color: #ff1493;'>🎙️ FASLI MUHABBET CANLI YAYIN</h1>", unsafe_allow_html=True)

# Yayın Akışı Görüntüleme
for msg in st.session_state.history:
    role_color = "#ff69b4" if "Dilay" in msg.get("host", "") else "#00d4ff"
    if msg["role"] == "user":
        st.info(f"🤵 **Patron:** {msg['content']}")
    else:
        with st.chat_message("assistant", avatar="🎙️"):
            st.markdown(f"<span style='color:{role_color}; font-weight:bold;'>{msg['host']}</span>", unsafe_allow_html=True)
            st.write(msg["content"])
            if msg.get("audio"):
                st.audio(msg["audio"], format="audio/mp3")

# --- YAYIN TETİKLEME ---
if prompt := st.chat_input("Yayını başlatacak konuyu girin Patronum..."):
    # 1. Patron'un mesajını ekle
    st.session_state.history.append({"role": "user", "content": prompt})
    st.rerun()

# Eğer en son mesaj kullanıcıdansa, sırayla sunucuları konuştur
if len(st.session_state.history) > 0 and st.session_state.history[-1]["role"] == "user":
    
    current_topic = st.session_state.history[-1]["content"]
    
    # SIRA: Önce Dilay, Sonra Mert
    for speaker, partner in [("Dilay 💖", "Mert 🎙️"), ("Mert 🎙️", "Dilay 💖")]:
        with st.spinner(f"🎙️ {speaker} mikrofonda..."):
            
            # Groq'a gönderilecek mesaj geçmişini hazırla
            messages = [{"role": "system", "content": get_persona(speaker, partner)}]
            # Son diyalogları ekle ki birbirlerini duyabilsinler
            for h in st.session_state.history[-6:]:
                messages.append({"role": h["role"], "content": h["content"]})

            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=messages,
                temperature=0.9
            ).choices[0].message.content

            # Ses üret
            audio = asyncio.run(generate_audio(response, VOICES[speaker]))

            # Kaydet
            st.session_state.history.append({
                "role": "assistant",
                "host": speaker,
                "content": response,
                "audio": audio
            })
            st.rerun() # Her konuşmadan sonra ekranı tazele ki sırayla sesler çalsın
