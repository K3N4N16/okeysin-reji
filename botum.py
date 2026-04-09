import streamlit as st
from groq import Groq
import asyncio
import edge_tts
import time

# --- REJİ AYARLARI ---
st.set_page_config(page_title="Faslı Muhabbet v11.0 - Sarmal Yayın", layout="wide")

if "GROQ_API_KEY" not in st.secrets:
    st.error("⚠️ GROQ API Key Eksik!")
    st.stop()

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

# Session State: Yayın akışını ve tur sayısını kontrol eder
if "history" not in st.session_state:
    st.session_state.history = []
if "loop_counter" not in st.session_state:
    st.session_state.loop_counter = 0

# --- SES VE KARAKTER TANIMLARI ---
HOSTS = [
    {"name": "Dilay 💖", "voice": "tr-TR-EmelNeural", "persona": "İşveli, neşeli, Mert'e laf atan kadın sunucu."},
    {"name": "Mert 🎙️", "voice": "tr-TR-AhmetNeural", "persona": "Ağırbaşlı, esprili, Dilay'ın paslarını gole çeviren erkek sunucu."}
]

async def generate_audio(text, voice):
    communicate = edge_tts.Communicate(text, voice, rate="+5%")
    audio_bytes = b""
    async for chunk in communicate.stream():
        if chunk["type"] == "audio":
            audio_bytes += chunk["data"]
    return audio_bytes

# --- ARAYÜZ ---
st.markdown("<h1 style='text-align: center; color: #ff1493;'>🎙️ FASLI MUHABBET: SARMAL CANLI YAYIN</h1>", unsafe_allow_html=True)

# Yayın Geçmişini Görüntüle
for msg in st.session_state.history:
    if msg["role"] == "user":
        st.markdown(f"🤵 **Patron:** {msg['content']}")
    else:
        role_color = "#ff69b4" if "Dilay" in msg["host"] else "#00d4ff"
        with st.chat_message("assistant", avatar="🎙️"):
            st.markdown(f"<span style='color:{role_color}; font-weight:bold;'>{msg['host']}</span>", unsafe_allow_html=True)
            st.write(msg["content"])
            if msg.get("audio"):
                st.audio(msg["audio"], format="audio/mp3", autoplay=True)

# --- SARMAL DÖNGÜ MANTIĞI ---
def start_broadcast(topic):
    # Eğer yeni bir konu geldiyse geçmişi temizlemeden ekle
    if not st.session_state.history or st.session_state.history[-1]["role"] == "user":
        # Döngüyü başlat (Örn: Her turda 4 paslaşma olsun)
        for i in range(4): 
            speaker_data = HOSTS[i % 2] # 0, 1, 0, 1 şeklinde sırayla seçer
            partner_data = HOSTS[(i + 1) % 2]
            
            with st.spinner(f"🎙️ {speaker_data['name']} yayında..."):
                # Sistem Prompt'u: Partnerini ve konuyu bilmesini sağlar
                messages = [{
                    "role": "system", 
                    "content": f"Sen {speaker_data['name']}. {speaker_data['persona']} "
                               f"Partnerin {partner_data['name']} ile sarmal bir sohbettesin. "
                               f"Ona sorular sor, pas at ve muhabbeti asla koparma. "
                               f"Radyo akıcılığında kısa cümleler kur."
                }]
                
                # Son 5 mesajı hafızaya ekle (Birbirlerini duymaları için)
                for h in st.session_state.history[-5:]:
                    messages.append({"role": h.get("role"), "content": h.get("content")})

                # Groq'tan yanıt al
                response = client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=messages,
                    temperature=0.9
                ).choices[0].message.content

                # Ses üret
                audio = asyncio.run(generate_audio(response, speaker_data["voice"]))

                # Kaydet
                st.session_state.history.append({
                    "role": "assistant",
                    "host": speaker_data["name"],
                    "content": response,
                    "audio": audio
                })
                
                # Anlık güncelleme için rerun
                st.rerun()

# Giriş Alanı
if prompt := st.chat_input("Patronum konuyu ver, onlar kendi aralarında aksın gitsin..."):
    st.session_state.history.append({"role": "user", "content": prompt})
    start_broadcast(prompt)

# --- REJİ KONTROL ---
with st.sidebar:
    st.title("🎚️ Reji Odası")
    if st.button("🔴 YAYINI DURDUR VE TEMİZLE"):
        st.session_state.history = []
        st.rerun()
    st.info("Bu modda sunucular 4 tur boyunca (2 Dilay, 2 Mert) birbirlerine pas atarak konuşur.")
