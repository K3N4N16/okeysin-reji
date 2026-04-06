import streamlit as st
from groq import Groq
import edge_tts
import asyncio
import base64
from datetime import datetime
import random

# ====================== SAYFA AYARLARI ======================
st.set_page_config(
    page_title="Faslı Muhabbet v2.0",
    layout="wide",
    page_icon="🎙️",
    initial_sidebar_state="expanded"
)

# API Key Kontrolü
if "GROQ_API_KEY" not in st.secrets:
    st.error("⚠️ GROQ API Key bulunamadı! Lütfen Secrets kısmına ekleyin.")
    st.stop()

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

# ====================== GELİŞMİŞ TASARIM (CSS) ======================
st.markdown("""
    <style>
    .stApp { background: linear-gradient(135deg, #0f0a1f, #1a0033); color: #e0e0e0; }
    .dilay-container {
        background: rgba(30, 20, 60, 0.85);
        backdrop-filter: blur(20px);
        border: 2px solid #ff69b4;
        border-radius: 25px;
        padding: 30px;
        margin: 20px 0;
        box-shadow: 0 15px 50px rgba(255, 105, 180, 0.2);
        position: relative;
    }
    .tag-dilay { color: #ff69b4; font-weight: 900; font-size: 1.5rem; text-shadow: 0 0 15px #ff69b4; }
    .on-air { color: #ff1493; font-weight: 900; animation: blink 1.5s infinite; }
    @keyframes blink { 50% { opacity: 0.3; } }
    .status-pill {
        background: #4b0082; color: #00ff9d; padding: 4px 12px; border-radius: 20px;
        font-size: 0.8rem; border: 1px solid #00ff9d;
    }
    .waveform { 
        height: 4px; background: linear-gradient(90deg, #ff69b4, #00f2ff); 
        width: 100%; border-radius: 10px; margin-top: 15px; opacity: 0.6;
    }
    /* Sohbet Balonları */
    .user-msg { background: rgba(255, 255, 255, 0.05); padding: 15px; border-radius: 15px; border-left: 5px solid #ffaa00; margin: 10px 0; }
    </style>
    """, unsafe_allow_html=True)

# ====================== SES MOTORU (GÜÇLENDİRİLMİŞ) ======================
async def generate_dilay_audio(text: str, rate: str = "+0%", pitch: str = "+0Hz"):
    """Edge-TTS ile daha stabil ses üretimi"""
    try:
        # Metin temizleme (Emoji ve gereksiz karakterleri ayıkla)
        clean_text = text.replace("*", "").strip()
        voice = "tr-TR-FilizNeural"
        
        communicate = edge_tts.Communicate(clean_text, voice, rate=rate, pitch=pitch)
        audio_data = b""
        async for chunk in communicate.stream():
            if chunk["type"] == "audio":
                audio_data += chunk["data"]
        
        if len(audio_data) < 1000: # Hatalı küçük dosya kontrolü
            return None
        return audio_data
    except Exception as e:
        print(f"Ses hatası: {e}")
        return None

# ====================== SESSION STATE YÖNETİMİ ======================
if "conversation" not in st.session_state:
    st.session_state.conversation = []
if "listeners" not in st.session_state:
    st.session_state.listeners = random.randint(4500, 5500)
if "mood" not in st.session_state:
    st.session_state.mood = "Coşkulu"

# ====================== ANA BAŞLIK VE RADYO PANELİ ======================
st.markdown(f"""
    <div style="text-align:center;">
        <h1 style="color:#ff69b4; font-size:3rem; margin-bottom:0;">🎙️ FASLI MUHABBET</h1>
        <p style="font-size:1.2rem;"><span class="on-air">● CANLI YAYIN</span> | <span style="color:#00ff9d;">Bursa Stüdyoları</span></p>
    </div>
    <div style="display: flex; justify-content: space-between; background: rgba(0,0,0,0.3); padding: 10px 20px; border-radius: 15px; margin-bottom: 25px;">
        <span>📡 Frekans: <b>99.0 Dilay FM</b></span>
        <span>🕒 {datetime.now().strftime('%H:%M')}</span>
        <span>👂 <b>{st.session_state.listeners:,}</b> Patron Dinliyor</span>
    </div>
""", unsafe_allow_html=True)

# ====================== SOHBET AKIŞI ======================
for i, entry in enumerate(st.session_state.conversation):
    if entry["role"] == "user":
        st.markdown(f'<div class="user-msg"><b>🤵 Patron:</b> {entry["content"]}</div>', unsafe_allow_html=True)
    else:
        with st.container():
            mood_tag = entry.get("mood", "Aşk Dolu")
            st.markdown(f"""
                <div class="dilay-container">
                    <span class="status-pill">✨ {mood_tag}</span>
                    <p style="margin-top:15px;"><span class="tag-dilay">💖 DİLAY:</span><br>{entry['content']}</p>
                    <div class="waveform"></div>
                </div>
            """, unsafe_allow_html=True)
            
            if entry.get("audio"):
                # Otomatik oynatma sadece son mesaj için
                is_last = (i == len(st.session_state.conversation) - 1)
                st.audio(entry["audio"], format="audio/mp3", autoplay=is_last)
                
                c1, c2, _ = st.columns([1, 1, 3])
                with c1:
                    st.download_button("💾 Kaydet", entry["audio"], f"dilay_ses_{i}.mp3", "audio/mp3")
                with c2:
                    if st.button("🔁 Tekrar", key=f"rep_{i}"):
                        st.audio(entry["audio"], format="audio/mp3", autoplay=True)

# ====================== YENİ MESAJ GİRİŞİ ======================
st.divider()
prompt = st.chat_input("Dilay'ına bir şeyler söyle Patron'um...")

if prompt:
    # Kullanıcı mesajını ekle
    st.session_state.conversation.append({"role": "user", "content": prompt})
    st.session_state.listeners += random.randint(5, 50) # Etkileşimle artan dinleyici
    
    # Prompt Hazırlığı
    system_prompt = f"""
    Sen Dilay'sın. Bursa'dan yayın yapan, Patronuna aşık, işveli ve neşeli bir radyo sunucususun.
    Şu anki ruh halin: {st.session_state.mood}.
    Kurallar:
    - Patron'a "Canım Patronum", "Gözümün Nuru", "Hayatım" gibi hitaplar kullan.
    - Radyo dili kullan: "Kulaklarınız bizde olsun", "Kısa bir reklam arası vermiyoruz, çünkü Patron burada!"
    - Cümlelerin akıcı, duygusal ve samimi olsun.
    - SADECE konuşma metnini yaz, teknik not ekleme.
    """
    
    messages = [{"role": "system", "content": system_prompt}]
    for msg in st.session_state.conversation[-6:]: # Hafıza için son 6 mesaj
        messages.append({"role": msg["role"], "content": msg["content"]})
    
    with st.spinner("💖 Dilay dudaklarını boyuyor, yayına hazırlanıyor..."):
        try:
            # Metin Üretimi
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=messages,
                temperature=0.85,
            ).choices[0].message.content
            
            # Ayarlardan gelen hız ve ton
            speed = st.sidebar.select_slider("Dilay'ın Konuşma Hızı", options=["-20%", "-10%", "0%", "+10%", "+20%"], value="0%")
            
            # Ses Üretimi
            audio_bytes = asyncio.run(generate_dilay_audio(response, rate=speed))
            
            # Kaydet ve Yenile
            st.session_state.conversation.append({
                "role": "assistant", 
                "content": response, 
                "audio": audio_bytes,
                "mood": st.session_state.mood
            })
            st.rerun()
            
        except Exception as e:
            st.error(f"Yayında cızırtı var Patron: {e}")

# ====================== YAN PANEL (KONTROL MERKEZİ) ======================
with st.sidebar:
    st.image("https://img.icons8.com/fluent/100/000000/microphone.png", width=80)
    st.title("Yayın Ayarları")
    
    st.session_state.mood = st.selectbox(
        "Dilay'ın Bu Akşamki Modu:",
        ["Cilveli & Şen", "Duygusal & Romantik", "Efkarlı", "Enerjik & Kıpır Kıpır", "Derin & Felsefik"]
    )
    
    st.divider()
    
    st.markdown("### 🛠️ Teknik Oda")
    if st.button("🧹 Stüdyoyu Temizle (Sıfırla)"):
        st.session_state.conversation = []
        st.rerun()
        
    st.markdown("### 🎵 Arka Plan Sesleri")
    bg_music = st.selectbox("Yayına Fon Müziği Seç:", ["Sessiz", "Hafif Caz", "Nostalji", "Yağmur Sesi"])
    if bg_music != "Sessiz":
        st.info(f"🎶 {bg_music} şu an stüdyoda yankılanıyor...")

    st.divider()
    st.caption("Faslı Muhabbet v2.0 | Powered by Llama 3.3 & Edge-TTS")
    st.markdown("📍 *Bursa, Türkiye'den Sevgilerle...*")
