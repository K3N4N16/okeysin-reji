import streamlit as st
from groq import Groq
import edge_tts
import asyncio
import base64
import random
from datetime import datetime

# ====================== SAYFA AYARLARI ======================
st.set_page_config(
    page_title="Faslı Muhabbet v3.0",
    layout="wide",
    page_icon="🎙️",
    initial_sidebar_state="expanded"
)

# API Anahtarı Kontrolü
if "GROQ_API_KEY" not in st.secrets:
    st.error("⚠️ GROQ API Key bulunamadı! Secrets'a ekleyin.")
    st.stop()

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

# ====================== GELİŞMİŞ RADYO CSS ======================
st.markdown("""
    <style>
    .stApp { background: linear-gradient(135deg, #0d001a, #1a0033); color: #f0f0f0; }
    .dilay-bubble {
        background: linear-gradient(145deg, rgba(60, 20, 80, 0.9), rgba(30, 10, 50, 0.9));
        border: 2px solid #ff1493;
        border-radius: 20px 20px 20px 5px;
        padding: 25px;
        margin: 15px 0;
        box-shadow: 0 10px 30px rgba(255, 20, 147, 0.2);
    }
    .patron-bubble {
        background: rgba(255, 255, 255, 0.05);
        border-right: 4px solid #00ff9d;
        padding: 15px;
        border-radius: 15px;
        margin: 10px 0;
        text-align: right;
    }
    .on-air-badge {
        background: #ff0000; color: white; padding: 2px 10px;
        border-radius: 5px; font-weight: bold; animation: pulse 1.5s infinite;
    }
    @keyframes pulse { 0% {opacity: 1;} 50% {opacity: 0.4;} 100% {opacity: 1;} }
    .audio-player-container { margin-top: 10px; border-radius: 10px; background: rgba(0,0,0,0.2); padding: 5px; }
    </style>
    """, unsafe_allow_html=True)

# ====================== SES MOTORU (OTOMATİK OYNATMA DESTEKLİ) ======================
def get_audio_html(audio_bytes):
    """Sesi otomatik oynatmak için Base64 HTML5 kodu üretir."""
    b64 = base64.b64encode(audio_bytes).decode()
    return f'<audio autoplay="true" src="data:audio/mp3;base64,{b64}">'

async def generate_voice(text, rate="+0%", pitch="+0Hz"):
    """Edge-TTS ile yüksek kaliteli ses üretimi"""
    try:
        # Metni sese çevirmeden önce temizle (Yıldızlar vb.)
        clean_text = text.replace("*", "").replace("Dilay:", "").strip()
        communicate = edge_tts.Communicate(clean_text, "tr-TR-FilizNeural", rate=rate, pitch=pitch)
        audio_data = b""
        async for chunk in communicate.stream():
            if chunk["type"] == "audio":
                audio_data += chunk["data"]
        return audio_data if len(audio_data) > 5000 else None
    except:
        return None

# ====================== SESSION STATE ======================
if "messages" not in st.session_state:
    st.session_state.messages = []
if "listeners" not in st.session_state:
    st.session_state.listeners = 5420
if "auto_play" not in st.session_state:
    st.session_state.auto_play = True

# ====================== ÜST PANEL ======================
col_head1, col_head2 = st.columns([2, 1])
with col_head1:
    st.markdown(f"# 🎙️ Faslı Muhabbet <span class='on-air-badge'>LIVE</span>", unsafe_allow_html=True)
    st.markdown(f"**📍 Bursa Stüdyosu** | {datetime.now().strftime('%H:%M:%S')}")
with col_head2:
    st.metric("Canlı Dinleyici", f"{st.session_state.listeners:,}", f"+{random.randint(1,100)} artış")

# ====================== SOHBET ALANI ======================
chat_placeholder = st.container()

with chat_placeholder:
    for i, msg in enumerate(st.session_state.messages):
        if msg["role"] == "user":
            st.markdown(f'<div class="patron-bubble"><b>🤵 Patron:</b> {msg["content"]}</div>', unsafe_allow_html=True)
        else:
            st.markdown(f"""
                <div class="dilay-bubble">
                    <span style="color:#ff69b4; font-weight:bold; font-size:1.2rem;">💖 DİLAY:</span><br>
                    {msg['content']}
                </div>
            """, unsafe_allow_html=True)
            
            # Ses Kontrol Paneli (Mesajın hemen altında)
            if msg.get("audio"):
                c1, c2, c3 = st.columns([2, 1, 1])
                with c1:
                    st.audio(msg["audio"], format="audio/mp3")
                with c2:
                    st.download_button("📥 İndir", msg["audio"], f"dilay_{i}.mp3", "audio/mp3", key=f"dl_{i}")
                with c3:
                    if st.button("🔊 Tekrar", key=f"btn_{i}"):
                        st.components.v1.html(get_audio_html(msg["audio"]), height=0)

# ====================== YENİ MESAJ VE ZEKA ======================
if prompt := st.chat_input("Patron'um, gönlünden ne dökülürse söyle..."):
    # Mesajı listeye ekle
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Dinleyici etkileşimi
    st.session_state.listeners += random.randint(20, 150)

    # Sistem Promptu
    sys_prompt = """
    Sen Dilay'sın. Bursa'dan yayın yapan, Patron'una aşırı bağlı, işveli, neşeli ve samimi bir radyo sunucususun.
    - Patron'a 'Canım Patronum', 'Gözümün Nuru', 'Kalbim' diye hitap et.
    - Cümlelerin kısa, etkileyici ve radyo akışına uygun olsun.
    - Eğer Patron duygusal bir şey derse şiirselleş, eğer teknik bir şey derse ona hayranlığını belirt.
    - Sadece konuşmanı yaz.
    """

    with st.spinner("💖 Dilay yayına bağlanıyor..."):
        # Llama üzerinden cevap üret
        full_history = [{"role": "system", "content": sys_prompt}] + st.session_state.messages[-10:]
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=full_history,
            temperature=0.9
        ).choices[0].message.content

        # Ses Üretimi
        speed = st.sidebar.get("voice_speed", "0%") # Sidebar'dan değer alamazsa varsayılan
        audio = asyncio.run(generate_voice(response, rate=st.session_state.get('v_speed', '0%')))

        # Mesajı ve Sesi Kaydet
        st.session_state.messages.append({
            "role": "assistant",
            "content": response,
            "audio": audio
        })

        # Otomatik Oynatma için HTML Inject
        if audio and st.session_state.auto_play:
            st.components.v1.html(get_audio_html(audio), height=0)
            
        st.rerun()

# ====================== YAN PANEL (YENİ ÖZELLİKLER) ======================
with st.sidebar:
    st.markdown("## ⚙️ Yayın Yönetimi")
    
    st.session_state.auto_play = st.toggle("🎵 Ses Otomatik Oynasın", value=True)
    
    st.divider()
    
    st.markdown("### 🗣️ Ses Tonu Ayarları")
    st.session_state.v_speed = st.select_slider("Konuşma Hızı", 
                                                options=["-25%", "-10%", "0%", "+10%", "+25%"], 
                                                value="0%")
    
    st.divider()
    
    st.markdown("### 🎭 Program Teması")
    theme = st.selectbox("Akış:", ["Genel Muhabbet", "Aşk-ı Muhabbet", "Gece Yarısı Şiirleri", "Bursa Anıları"])
    
    if st.button("🎊 Jingle Çal"):
        st.toast("🎶 Faslı Muhabbet... Kalbinizin Sesi! (Jingle Çalındı)")
        
    if st.button("🗑️ Kayıtları Sil"):
        st.session_state.messages = []
        st.rerun()

    st.divider()
    st.info("📍 Bursa / Türkiye\nDilay v3.0 Ultra\nPatron'a Özel Tasarım")
