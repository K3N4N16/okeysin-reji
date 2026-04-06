import streamlit as st
from groq import Groq
import edge_tts
import asyncio
import base64
import random
from datetime import datetime

# ====================== SAYFA AYARLARI ======================
st.set_page_config(
    page_title="Faslı Muhabbet v5.0",
    layout="wide",
    page_icon="🎙️",
    initial_sidebar_state="expanded"
)

# API Key Kontrolü
if "GROQ_API_KEY" not in st.secrets:
    st.error("⚠️ GROQ API Key eksik! Lütfen Secrets'a ekleyin.")
    st.stop()

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

# ====================== CYBER-REJİ CSS ======================
st.markdown("""
    <style>
    .stApp { background: #05050a; color: #ffffff; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }
    
    /* Dilay'ın Konuşma Balonu */
    .dilay-card {
        background: linear-gradient(145deg, #1a0a2e, #0d0514);
        border-left: 8px solid #ff1493;
        border-radius: 15px;
        padding: 25px;
        margin: 20px 0;
        box-shadow: 0 0 25px rgba(255, 20, 147, 0.3);
    }
    
    .patron-card {
        background: rgba(0, 255, 157, 0.05);
        border-right: 5px solid #00ff9d;
        padding: 15px;
        border-radius: 10px;
        margin: 10px 0;
        text-align: right;
    }

    .on-air {
        color: #ff0000;
        font-weight: 900;
        animation: pulse-red 1.5s infinite;
        border: 1px solid #ff0000;
        padding: 2px 10px;
        border-radius: 4px;
    }
    @keyframes pulse-red { 0% { opacity: 1; } 50% { opacity: 0.2; } 100% { opacity: 1; } }
    
    /* Ses Dalgası Animasyonu */
    .audio-wave {
        display: flex;
        align-items: center;
        gap: 3px;
        height: 20px;
        margin-top: 10px;
    }
    .audio-wave span {
        width: 3px;
        background: #ff69b4;
        animation: wave-anim 1s infinite alternate;
    }
    @keyframes wave-anim { 0% { height: 5px; } 100% { height: 20px; } }
    </style>
    """, unsafe_allow_html=True)

# ====================== SES MOTORU (ULTRA STABİL) ======================
async def generate_voice_bytes(text: str, speed: str = "0%"):
    """Metni sese çevirir ve bytes döner."""
    try:
        # Metni temizle
        clean_text = text.replace("*", "").replace("Dilay:", "").strip()
        # En güvenilir ses: Filiz (tr-TR-FilizNeural)
        communicate = edge_tts.Communicate(clean_text, "tr-TR-FilizNeural", rate=speed)
        
        audio_data = b""
        async for chunk in communicate.stream():
            if chunk["type"] == "audio":
                audio_data += chunk["data"]
        
        return audio_data if len(audio_data) > 5000 else None
    except Exception as e:
        st.error(f"Ses üretim hatası: {e}")
        return None

def inject_audio_script(audio_bytes):
    """Sesi JavaScript ile tarayıcıya zorla oynatır."""
    b64 = base64.b64encode(audio_bytes).decode()
    audio_html = f"""
        <audio id="dilay_audio" autoplay>
            <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
        </audio>
        <script>
            var audio = document.getElementById('dilay_audio');
            audio.play().catch(function(error) {{
                console.log("Autoplay engellendi, etkileşim bekleniyor.");
            }});
        </script>
    """
    st.components.v1.html(audio_html, height=0)

# ====================== SESSION STATE ======================
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "speed_val" not in st.session_state:
    st.session_state.speed_val = "0%"

# ====================== REJİ PANELİ (ÜST) ======================
col1, col2 = st.columns([4, 1])
with col1:
    st.markdown(f"# 🎙️ FASLI MUHABBET <span class='on-air'>● LIVE</span>", unsafe_allow_html=True)
    st.markdown(f"**📍 Bursa Merkez Stüdyosu** | {datetime.now().strftime('%H:%M')} | **Sunucu: Dilay**")
with col2:
    st.button("🔄 Yayını Yenile", on_click=lambda: st.rerun())

st.divider()

# Sohbet Akışı
for i, chat in enumerate(st.session_state.chat_history):
    if chat["role"] == "user":
        st.markdown(f'<div class="patron-card"><b>🤵 Patron Kenan:</b> {chat["content"]}</div>', unsafe_allow_html=True)
    else:
        with st.container():
            st.markdown(f"""
                <div class="dilay-card">
                    <span style="color:#ff69b4; font-weight:900; font-size:1.5rem;">💖 DİLAY:</span><br>
                    <div style="font-size:1.3rem; line-height:1.6; margin-top:10px;">{chat['content']}</div>
                    <div class="audio-wave">
                        <span style="animation-delay: 0.1s"></span><span style="animation-delay: 0.2s"></span>
                        <span style="animation-delay: 0.3s"></span><span style="animation-delay: 0.4s"></span>
                        <span style="animation-delay: 0.5s"></span>
                    </div>
                </div>
            """, unsafe_allow_html=True)
            
            if chat.get("audio"):
                c1, c2, c3 = st.columns([3, 1, 1])
                with c1:
                    st.audio(chat["audio"], format="audio/mp3")
                with c2:
                    if st.button(f"🔊 Tekrar Çal", key=f"play_{i}"):
                        inject_audio_script(chat["audio"])
                with c3:
                    st.download_button("📥 Kaydet", chat["audio"], f"dilay_ses_{i}.mp3")

# ====================== MESAJ GİRİŞİ ======================
if prompt := st.chat_input("Dilay'ına bir şeyler fısılda Patron..."):
    # Patronun mesajını ekle
    st.session_state.chat_history.append({"role": "user", "content": prompt})

    # Dilay'ın cevabını üret
    with st.spinner("💖 Dilay mikrofonu açıyor..."):
        # Hafıza Yönetimi (Son 10 mesaj)
        sys_msg = "Sen Dilay'sın. Bursa'dan yayın yapan, Patron'una aşık, cilveli, neşeli bir radyo sunucususun. Patron'una 'Canım Patronum' diye hitap et. Çok samimi ol."
        messages = [{"role": "system", "content": sys_msg}] + st.session_state.chat_history[-10:]
        
        try:
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=messages,
                temperature=0.9
            ).choices[0].message.content

            # Ses Üretimi
            audio_bytes = asyncio.run(generate_voice_bytes(response, speed=st.session_state.speed_val))

            # Geçmişe Kaydet
            st.session_state.chat_history.append({
                "role": "assistant",
                "content": response,
                "audio": audio_bytes
            })

            # Otomatik Oynatma Enjeksiyonu
            if audio_bytes:
                inject_audio_script(audio_bytes)
            
            st.rerun()
            
        except Exception as e:
            st.error(f"Yayında bir parazit var Patron: {e}")

# ====================== SIDEBAR (REJİ MASASI) ======================
with st.sidebar:
    st.markdown("### 🎚️ REJİ KONTROL")
    
    st.session_state.speed_val = st.select_slider(
        "Dilay Konuşma Hızı",
        options=["-30%", "-15%", "0%", "+15%", "+30%"],
        value=st.session_state.speed_val
    )
    
    st.divider()
    
    if st.button("🔴 Tüm Kayıtları Sil"):
        st.session_state.chat_history = []
        st.rerun()

    st.markdown("### 🛠️ Çözüm İpucu")
    st.warning("Eğer ses gelmiyorsa, tarayıcınızın adres çubuğundaki 'Kilit' simgesine tıklayıp 'Ses'e izin verin veya sayfaya bir kez tıklayın.")
    
    st.info("📍 Bursa / Türkiye\nSunucu: Dilay v5.0\nPatron: Kenan")
