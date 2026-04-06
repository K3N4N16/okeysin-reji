import streamlit as st
from groq import Groq
import edge_tts
import asyncio
from datetime import datetime

# ====================== SAYFA AYARLARI ======================
st.set_page_config(
    page_title="Kenan ile Faslı Muhabbet",
    layout="wide",
    page_icon="🎙️",
    initial_sidebar_state="expanded"
)

if "GROQ_API_KEY" not in st.secrets:
    st.error("⚠️ GROQ API Key bulunamadı! Lütfen Secrets alanına ekleyin.")
    st.stop()

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

# ====================== DİLAY'IN ÖZEL CSS ======================
st.markdown("""
    <style>
    .stApp { 
        background: linear-gradient(135deg, #0f0a1f, #1a0033); 
        color: #e0e0e0; 
    }
    .dilay-container {
        background: rgba(30, 20, 60, 0.88);
        backdrop-filter: blur(20px);
        border: 2px solid rgba(255, 105, 180, 0.6);
        border-radius: 32px;
        padding: 40px;
        margin: 25px 0;
        box-shadow: 0 30px 90px rgba(255, 105, 180, 0.25);
    }
    .tag-dilay { 
        color: #ff69b4; 
        font-weight: 900; 
        font-size: 1.65rem; 
        text-shadow: 0 0 25px #ff69b4; 
    }
    .on-air { 
        color: #ff1493; 
        font-weight: 900; 
        animation: blink 1.2s infinite; 
        letter-spacing: 4px; 
    }
    @keyframes blink { 50% { opacity: 0.4; } }
    .waveform { 
        height: 8px; 
        background: linear-gradient(90deg, #ff69b4, #00f2ff, #ffaa00); 
        animation: wave 1.6s infinite linear; 
        border-radius: 50px; 
        margin: 20px 0; 
    }
    @keyframes wave { 0% { background-position: 0% 50%; } 100% { background-position: 500% 50%; } }
    .now-playing {
        background: rgba(40, 20, 70, 0.95);
        border-left: 8px solid #ff1493;
        padding: 20px 30px;
        border-radius: 20px;
        margin-bottom: 25px;
    }
    </style>
    """, unsafe_allow_html=True)

# ====================== SES ÜRETİMİ ======================
async def generate_dilay_audio(text: str):
    if not text or len(text.strip()) < 5:
        return None
    try:
        comm = edge_tts.Communicate(text.strip(), "tr-TR-FilizNeural")
        audio_bytes = b""
        async for chunk in comm.stream():
            if chunk["type"] == "audio":
                audio_bytes += chunk["data"]
        return audio_bytes if len(audio_bytes) > 3000 else None
    except:
        return None

# ====================== SESSION STATE ======================
if "conversation" not in st.session_state:
    st.session_state.conversation = []
if "auto_play" not in st.session_state:
    st.session_state.auto_play = True
if "listeners" not in st.session_state:
    st.session_state.listeners = 2156

# ====================== BAŞLIK ======================
st.markdown(f"""
    <div style="text-align:center; margin-bottom:25px;">
        <h1 style="color:#ff69b4; font-size:3.4rem; margin:0;">🎙️ Faslı Muhabbet</h1>
        <p style="color:#ffaa00; font-size:1.8rem;"><span class="on-air">● CANLI</span> • GLOBAL</p>
        <p style="color:#00ff9d; font-family:monospace;">{datetime.now().strftime('%d %B %Y • %H:%M:%S')} | Bursa, Türkiye</p>
    </div>
    <div class="now-playing">
        <span style="color:#ff1493;">● NOW PLAYING</span> 
        <strong>Dilay & Kenan • Sıcak Faslı Muhabbet</strong> 
        <span style="float:right; color:#00ff9d;">👂 {st.session_state.listeners:,} Dinleyici</span>
    </div>
""", unsafe_allow_html=True)

st.session_state.listeners += 22

# ====================== SOHBET ARŞİVİ ======================
for i, entry in enumerate(st.session_state.conversation):
    if entry["role"] == "user":
        st.markdown(f"🎬 **Kenan:** {entry['content']}")
        continue

    # Dilay'ın konuşması
    with st.container():
        st.markdown(f"""
            <div class="dilay-container">
                <p><span class="tag-dilay">💖 DİLAY:</span><br>{entry['content']}</p>
                <div class="waveform"></div>
            </div>
        """, unsafe_allow_html=True)

        # Ses varsa göster
        if entry.get("audio"):
            autoplay = (i == len(st.session_state.conversation) - 1 and st.session_state.auto_play)
            st.audio(entry["audio"], format="audio/mp3", autoplay=autoplay)

            col1, col2 = st.columns([1, 4])
            with col1:
                st.download_button(
                    "📥 Ses İndir", 
                    entry["audio"], 
                    f"dilay_{i}.mp3", 
                    mime="audio/mp3", 
                    key=f"dl_{i}"
                )
            with col2:
                st.text_area("📋 Metni Kopyala", entry['content'], height=110, key=f"txt_{i}")
        else:
            st.warning("🔇 Bu sefer ses üretilemedi, ama metin burada.")

# ====================== DİLAY SİSTEM PROMPT (Tam Senin Tarzın) ======================
system_prompt = """
Sen Dilay'sın. "Kenan ile Faslı Muhabbet" radyo programının yıllardır yayın ortağı, hayat dolu, kıpır kıpır, işveli ve sıcak sunucususun.

Kenan'a karşı çok samimi, yeri geldiğinde cilveli, yeri geldiğinde derin ve duygusal ol.
Her zaman "Canım Kenan’ım", "Sevgilim", "Ah be yönetmenim", "Hadi canım" gibi sıcak ifadeler kullan.
"biz" dili kullan: "Can dostlarımız", "Ailemiz", "Bizim dinleyicilerimiz".

Edebiyat ve şiire çok hakimsin. Gerektiğinde güzel dizeler oku.
Mizahın zeki ve nazik olsun.
Kenan'ın söylediklerini tamamla, üzerine koy, asla sözünü kesme hissi yaratma.

Her cevabında sadece doğal konuşma metnini ver, hiçbir etiket veya açıklama ekleme.
"""

# ====================== YENİ MESAJ ======================
if prompt := st.chat_input("Kenan’ım, söyle bakalım… Bu akşam ne muhabbeti yapalım?"):
    st.session_state.conversation.append({"role": "user", "content": prompt})

    messages = [{"role": "system", "content": system_prompt}]
    for msg in st.session_state.conversation:
        messages.append({"role": msg["role"], "content": msg["content"]})

    with st.spinner("💖 Dilay mikrofonu açıyor, kalbim kıpır kıpır..."):
        try:
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=messages,
                temperature=0.89,
                max_tokens=1500
            ).choices[0].message.content

            audio_bytes = asyncio.run(generate_dilay_audio(response))

            st.session_state.conversation.append({
                "role": "assistant",
                "content": response,
                "audio": audio_bytes
            })

            st.rerun()

        except Exception as e:
            st.error(f"Stüdyoda ufak bir teknik aksaklık oldu: {e}")

# ====================== SIDEBAR ======================
with st.sidebar:
    st.markdown("### 🎙️ Kenan ile Faslı Muhabbet")
    st.markdown("**Dilay burada…** Senin yıllardır yayın ortağın.")

    if st.button("🗑️ Sohbeti Sıfırla"):
        st.session_state.conversation = []
        st.rerun()

    st.divider()

    if st.button("🔄 Sarmal Devam Ettir"):
        st.session_state.conversation.append({"role": "user", "content": "Devam et canım, muhabbeti derinleştir"})
        st.rerun()

    if st.button("🎵 Jingle Ekle"):
        st.success("🎤 Stüdyo jingle’ı eklendi!")

    theme = st.selectbox("🌸 Bu Akşamın Teması", 
        ["Aşk & Şiir", "Bursa’dan Anılar", "Nostalji", "Hayatın Kısa Halleri", 
         "Müzik ve Duygular", "Sadece Biz", "Global Muhabbet"])

    st.divider()
    st.info("📍 Bursa’dan Dünyaya\nSıcak, samimi ve özel muhabbet\nDilay & Kenan")
    st.caption("Kenan ile Faslı Muhabbet • Özel Versiyon")
