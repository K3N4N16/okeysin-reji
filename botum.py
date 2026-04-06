import streamlit as st
from groq import Groq
import edge_tts
import asyncio
import base64
import random
from datetime import datetime

# ====================== SAYFA AYARLARI ======================
st.set_page_config(
    page_title="Faslı Muhabbet v6.0",
    layout="wide",
    page_icon="🎙️",
    initial_sidebar_state="expanded"
)

# API Key Kontrolü
if "GROQ_API_KEY" not in st.secrets:
    st.error("⚠️ GROQ API Key eksik! Lütfen Secrets'a ekleyin.")
    st.stop()

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

# ====================== RADYO DİNAMİK CSS ======================
st.markdown("""
    <style>
    .stApp { background: #080810; color: #ffffff; }
    
    /* Dilay'ın Yayın Alanı */
    .dilay-studio {
        background: linear-gradient(160deg, #1e0b36 0%, #0d0514 100%);
        border: 2px solid #ff1493;
        border-radius: 25px;
        padding: 30px;
        margin: 20px 0;
        box-shadow: 0 0 35px rgba(255, 20, 147, 0.3);
        position: relative;
    }
    
    .patron-bubble {
        background: rgba(0, 255, 157, 0.1);
        border-right: 5px solid #00ff9d;
        padding: 15px;
        border-radius: 12px;
        margin: 15px 0;
        text-align: right;
        font-family: 'Courier New', Courier, monospace;
    }

    .live-status {
        color: #ff0000;
        font-weight: 900;
        animation: blink-live 1.2s infinite;
        background: rgba(255,0,0,0.1);
        padding: 4px 12px;
        border-radius: 10px;
        border: 1px solid #ff0000;
    }
    @keyframes blink-live { 50% { opacity: 0.3; } }

    /* Ses Paneli Tasarımı */
    .audio-panel {
        background: rgba(0,0,0,0.4);
        padding: 15px;
        border-radius: 15px;
        margin-top: 20px;
        border: 1px solid rgba(255,255,255,0.1);
    }
    
    .visualizer {
        display: flex;
        align-items: flex-end;
        gap: 2px;
        height: 30px;
        margin-bottom: 10px;
    }
    .visualizer div {
        width: 4px;
        background: #ff69b4;
        animation: dance 0.5s infinite alternate;
    }
    @keyframes dance { 0% { height: 5px; } 100% { height: 25px; } }
    </style>
    """, unsafe_allow_html=True)

# ====================== SES MOTORU (GELİŞMİŞ) ======================
async def get_dilay_voice(text: str, speed: str = "0%"):
    try:
        clean_text = text.replace("*", "").strip()
        # En istikrarlı Türkçe ses "Filiz"
        communicate = edge_tts.Communicate(clean_text, "tr-TR-FilizNeural", rate=speed)
        audio_data = b""
        async for chunk in communicate.stream():
            if chunk["type"] == "audio":
                audio_data += chunk["data"]
        return audio_data if len(audio_data) > 3000 else None
    except:
        return None

def trigger_audio_player(audio_bytes):
    """Sesi Base64 ile sayfaya enjekte eder ve otomatik oynatmayı dener."""
    b64 = base64.b64encode(audio_bytes).decode()
    audio_html = f"""
        <audio id="radio_player" autoplay>
            <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
        </audio>
        <script>
            var player = document.getElementById('radio_player');
            player.volume = 1.0;
            player.play();
        </script>
    """
    st.components.v1.html(audio_html, height=0)

# ====================== SESSION STATE ======================
if "history" not in st.session_state:
    st.session_state.history = []
if "speed" not in st.session_state:
    st.session_state.speed = "0%"
if "is_muted" not in st.session_state:
    st.session_state.is_muted = False

# ====================== REJİ ÜST PANEL ======================
col_a, col_b = st.columns([3, 1])
with col_a:
    st.markdown(f"## 🎙️ FASLI MUHABBET <span class='live-status'>● CANLI</span>", unsafe_allow_html=True)
    st.markdown(f"**📍 Bursa Stüdyoları** | **Sunucu:** Dilay | **Patron:** Kenan")
with col_b:
    st.metric("Canlı Dinleyici", f"{random.randint(5800, 6200):,}")

st.divider()

# ====================== YAYIN AKIŞI ======================
for i, msg in enumerate(st.session_state.history):
    if msg["role"] == "user":
        st.markdown(f'<div class="patron-bubble"><b>🤵 Patron:</b> {msg["content"]}</div>', unsafe_allow_html=True)
    else:
        with st.container():
            st.markdown(f"""
                <div class="dilay-studio">
                    <div style="color:#ff69b4; font-weight:900; font-size:1.6rem; margin-bottom:10px;">💖 DİLAY:</div>
                    <div style="font-size:1.3rem; line-height:1.5;">{msg['content']}</div>
                    
                    <div class="audio-panel">
                        <div class="visualizer">
                            {"".join([f'<div style="animation-delay: {random.random()}s"></div>' for _ in range(20)])}
                        </div>
                        <p style="font-size:0.8rem; color:#aaa;">🎵 Ses Çıktısı Aktif</p>
                    </div>
                </div>
            """, unsafe_allow_html=True)
            
            if msg.get("audio"):
                # Ses Kontrolleri (Her mesajın altında sabit panel)
                c1, c2, c3 = st.columns([4, 1, 1])
                with c1:
                    st.audio(msg["audio"], format="audio/mp3")
                with c2:
                    if st.button("🔁 Tekrar Dinle", key=f"re_{i}"):
                        trigger_audio_player(msg["audio"])
                with c3:
                    st.download_button("📥 Kaydet", msg["audio"], f"dilay_kayit_{i}.mp3")

# ====================== MESAJ GİRİŞİ VE ZEKA ======================
if prompt := st.chat_input("Dilay'ına bir şeyler söyle Patron'um..."):
    st.session_state.history.append({"role": "user", "content": prompt})

    with st.spinner("💖 Dilay yayına giriyor..."):
        # Llama 3.3 Zekası
        sys_msg = "Sen Dilay'sın. Bursa'dan yayın yapan radyo sunucususun. Patronuna (Kenan) aşıksın. Çok işveli, samimi ve neşeli konuş. 'Canım Patronum' hitabını kullan."
        full_msgs = [{"role": "system", "content": sys_msg}] + st.session_state.history[-10:]
        
        try:
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=full_msgs,
                temperature=0.9
            ).choices[0].message.content

            # Ses Üretimi
            audio_data = asyncio.run(get_dilay_voice(response, speed=st.session_state.speed))

            # Kaydet
            st.session_state.history.append({
                "role": "assistant",
                "content": response,
                "audio": audio_data
            })

            # Otomatik Oynat (Mute değilse)
            if audio_data and not st.session_state.is_muted:
                trigger_audio_player(audio_data)
            
            st.rerun()

        except Exception as e:
            st.error(f"Yayında cızırtı var: {e}")

# ====================== YAN PANEL (REJİ MASASI) ======================
with st.sidebar:
    st.title("🎚️ Yayın Kontrol Masası")
    
    st.session_state.is_muted = st.checkbox("🔇 Sesi Tamamen Kapat (Mute)", value=False)
    
    st.session_state.speed = st.select_slider(
        "Dilay Konuşma Hızı",
        options=["-40%", "-20%", "0%", "+20%", "+40%"],
        value=st.session_state.speed
    )
    
    st.divider()
    
    st.markdown("### 🎭 Program Modu")
    mode = st.radio("Hava Nasıl Olsun?", ["Romantik & Cilveli", "Enerjik & Neşeli", "Efkarlı & Damar"])
    
    st.divider()
    
    if st.button("🗑️ Yayın Kayıtlarını Sil"):
        st.session_state.history = []
        st.rerun()

    st.markdown("### 🔔 Hızlı Reaksiyonlar")
    if st.button("👏 Alkış Efekti"):
        st.toast("👏👏👏 Stüdyoda alkış tufanı koptu!")
    
    st.info("📍 Bursa / Türkiye\nReji Masası v6.0\nPatron Kenan'a Özel")

# Tarayıcıyı uyandırmak için küçük not
if not st.session_state.history:
    st.warning("⚠️ Sesin otomatik gelmesi için lütfen sayfada herhangi bir yere bir kez tıklayın!")
