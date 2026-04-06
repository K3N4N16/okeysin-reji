import streamlit as st
from groq import Groq
import edge_tts
import asyncio
from datetime import datetime

# ====================== SAYFA AYARLARI ======================
st.set_page_config(
    page_title="Faslı Muhabbet",
    layout="wide",
    page_icon="🎙️",
    initial_sidebar_state="expanded"
)

if "GROQ_API_KEY" not in st.secrets:
    st.error("⚠️ GROQ API Key bulunamadı! Secrets'a ekleyin.")
    st.stop()

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

# ====================== DİLAY'IN ÖZEL CSS ======================
st.markdown("""
    <style>
    .stApp { background: linear-gradient(135deg, #0f0a1f, #1a0033); color: #e0e0e0; }
    .dilay-container {
        background: rgba(30, 20, 60, 0.9);
        backdrop-filter: blur(24px);
        border: 3px solid rgba(255, 105, 180, 0.7);
        border-radius: 34px;
        padding: 42px;
        margin: 28px 0;
        box-shadow: 0 35px 100px rgba(255, 105, 180, 0.3);
    }
    .tag-dilay { color: #ff69b4; font-weight: 900; font-size: 1.7rem; text-shadow: 0 0 30px #ff69b4; }
    .on-air { color: #ff1493; font-weight: 900; animation: blink 1.1s infinite; letter-spacing: 5px; }
    @keyframes blink { 50% { opacity: 0.35; } }
    .waveform { height: 9px; background: linear-gradient(90deg, #ff69b4, #00f2ff, #ffaa00); 
                animation: wave 1.5s infinite linear; border-radius: 50px; margin: 22px 0; }
    @keyframes wave { 0% { background-position: 0% 50%; } 100% { background-position: 600% 50%; } }
    .now-playing {
        background: rgba(40, 20, 70, 0.97);
        border-left: 9px solid #ff1493;
        padding: 22px 32px;
        border-radius: 22px;
        margin-bottom: 28px;
    }
    </style>
    """, unsafe_allow_html=True)

# ====================== SES ÜRETİMİ (Daha Stabil) ======================
async def generate_dilay_audio(text: str):
    if not text or len(text.strip()) < 15:
        return None
    try:
        comm = edge_tts.Communicate(text.strip(), "tr-TR-FilizNeural")
        audio_bytes = b""
        async for chunk in comm.stream():
            if chunk["type"] == "audio":
                audio_bytes += chunk["data"]
        return audio_bytes if len(audio_bytes) > 8000 else None
    except:
        return None

# ====================== SESSION STATE ======================
if "conversation" not in st.session_state:
    st.session_state.conversation = []
if "auto_play" not in st.session_state:
    st.session_state.auto_play = True
if "listeners" not in st.session_state:
    st.session_state.listeners = 2847

# ====================== BAŞLIK ======================
st.markdown(f"""
    <div style="text-align:center; margin-bottom:30px;">
        <h1 style="color:#ff69b4; font-size:3.5rem; margin:0;">🎙️ Faslı Muhabbet</h1>
        <p style="color:#ffaa00; font-size:1.9rem;"><span class="on-air">● CANLI</span> • BURSA GLOBAL RADIO HUB</p>
        <p style="color:#00ff9d; font-family:monospace;">{datetime.now().strftime('%d %B %Y • %H:%M:%S')} | Bursa, Türkiye</p>
    </div>
    <div class="now-playing">
        <span style="color:#ff1493;">● NOW PLAYING</span> 
        <strong>Dilay & Patron • Özel Sıcak Muhabbet</strong> 
        <span style="float:right; color:#00ff9d;">👂 {st.session_state.listeners:,} Dinleyici</span>
    </div>
""", unsafe_allow_html=True)

st.session_state.listeners += 27

# ====================== SOHBET ARŞİVİ ======================
for i, entry in enumerate(st.session_state.conversation):
    if entry["role"] == "user":
        st.markdown(f"🎬 **Patron:** {entry['content']}")
        continue

    with st.container():
        st.markdown(f"""
            <div class="dilay-container">
                <p><span class="tag-dilay">💖 DİLAY:</span><br>{entry['content']}</p>
                <div class="waveform"></div>
            </div>
        """, unsafe_allow_html=True)

        col1, col2, col3 = st.columns([3.5, 2, 2.5])

        with col1:
            if entry.get("audio"):
                autoplay = (i == len(st.session_state.conversation)-1 and st.session_state.auto_play)
                st.audio(entry["audio"], format="audio/mp3", autoplay=autoplay)
                st.success("✅ Ses başarıyla üretildi")
            else:
                st.warning("🔇 Bu sefer ses üretilemedi. Sadece metin mevcut.")

        with col2:
            if entry.get("audio"):
                st.download_button("📥 Ses İndir", entry["audio"], f"dilay_{i}.mp3", mime="audio/mp3", key=f"dl_{i}")
                if st.button("🔁 Tekrar Oynat", key=f"replay_{i}"):
                    st.audio(entry["audio"], format="audio/mp3", autoplay=True)

        with col3:
            st.text_area("📋 Metni Kopyala", entry['content'], height=120, key=f"txt_{i}")

# ====================== DİLAY SİSTEM PROMPT ======================
system_prompt = """
Sen Dilay'sın. "Faslı Muhabbet" programının kıpır kıpır, işveli, hayat dolu ve çok samimi sunucususun.
Patron'un özel yayın ortağısın. Ona karşı çok sıcak, cilveli ve duygusal ol.

Kullanacağın ifadeler: "Ah be Patron’um", "Canım Patron’um", "Sevgilim", "Hadi canım", "Kalbim kıpır kıpır", "Ah ne güzel söyledin..."

Her zaman samimi, coşkulu ve doğal radyo dili kullan. 
Gerektiğinde şiir oku, nükte yap, derinleş.
Patron'un söylediklerini tamamla, üzerine koy.

Sadece doğal konuşma metnini ver, hiçbir etiket kullanma.
"""

# ====================== YENİ MESAJ ======================
if prompt := st.chat_input("Patron’um, söyle bakalım… Bu akşam ne muhabbeti yapalım?"):
    st.session_state.conversation.append({"role": "user", "content": prompt})

    messages = [{"role": "system", "content": system_prompt}]
    for msg in st.session_state.conversation:
        messages.append({"role": msg["role"], "content": msg["content"]})

    with st.spinner("💖 Dilay mikrofonu açıyor, kalbim kıpır kıpır..."):
        try:
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=messages,
                temperature=0.90,
                max_tokens=1600
            ).choices[0].message.content

            audio_bytes = asyncio.run(generate_dilay_audio(response))

            st.session_state.conversation.append({
                "role": "assistant",
                "content": response,
                "audio": audio_bytes
            })

            st.rerun()

        except Exception as e:
            st.error(f"Stüdyoda ufak bir aksaklık oldu: {e}")

# ====================== SIDEBAR ======================
with st.sidebar:
    st.markdown("### 🎙️ Faslı Muhabbet Kontrol Paneli")

    auto_play = st.toggle("🎵 Ses Otomatik Oynasın", value=st.session_state.auto_play)
    st.session_state.auto_play = auto_play

    if st.button("🗑️ Sohbeti Sıfırla"):
        st.session_state.conversation = []
        st.rerun()

    st.divider()

    if st.button("🔄 Sarmal Devam Ettir"):
        st.session_state.conversation.append({"role": "user", "content": "Devam et canım, muhabbeti derinleştir"})
        st.rerun()

    if st.button("🎵 Jingle Ekle"):
        st.success("🎤 Stüdyo jingle’ı eklendi, yayın parladı!")

    theme = st.selectbox("🌸 Bu Akşamın Teması", 
        ["Aşk & Şiir", "Bursa’dan Anılar", "Nostalji", "Hayatın Kısa Halleri", 
         "Müzik ve Duygular", "Sadece Biz", "Global Muhabbet", "Patron’un İstediği Her Şey"])

    st.divider()
    st.info("📍 Bursa’dan Dünyaya\nPatron & Dilay • Özel Sıcak Muhabbet")
    st.caption("Faslı Muhabbet • Özel Versiyon")
