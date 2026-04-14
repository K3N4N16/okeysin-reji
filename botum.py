import streamlit as st
from gtts import gTTS
from io import BytesIO
import base64

# Sayfa ayarları
st.set_page_config(
    page_title="Aşk-ı Muhabbet v46.0 BLACK | Bursa Stüdyosu 🎙️",
    page_icon="🎙️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Şık BLACK Tema CSS (öncekiyle aynı + TTS için ekstra)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Playfair+Display:wght@700&display=swap');
    
    .stApp { background: #0a0a0a; }
    .main { background: linear-gradient(135deg, #0f0f0f 0%, #1a0f1f 50%, #0f0a14 100%); }
    
    .live-badge {
        position: fixed; top: 25px; left: 40px; background: #dc143c; color: white;
        padding: 12px 32px; border-radius: 50px; font-size: 16px; font-weight: 700;
        letter-spacing: 2px; z-index: 9999; box-shadow: 0 0 30px rgba(220,20,60,0.9);
        animation: pulse 2s infinite; display: flex; align-items: center; gap: 10px;
    }
    @keyframes pulse { 0%,100% { box-shadow: 0 0 30px rgba(220,20,60,0.9); } 50% { box-shadow: 0 0 45px rgba(220,20,60,1); } }
    
    .tts-box { background: rgba(20,20,30,0.9); padding: 25px; border-radius: 20px; border: 1px solid rgba(192,38,211,0.3); margin: 20px 0; }
    
    .floating-banner {
        position: fixed; bottom: 40px; right: 40px; background: rgba(15,15,22,0.95);
        backdrop-filter: blur(25px); border: 1px solid rgba(255,255,255,0.15);
        border-radius: 24px; padding: 20px 32px; display: flex; align-items: center; gap: 20px;
        box-shadow: 0 25px 60px rgba(0,0,0,0.8); z-index: 9999;
    }
    .floating-banner:hover { transform: translateY(-8px) scale(1.04); }
    
    .banner-logo { font-size: 42px; animation: mic-pulse 3s infinite ease-in-out; }
    @keyframes mic-pulse { 0%,100% { transform: scale(1); } 50% { transform: scale(1.12); } }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="live-badge">● CANLI YAYINDA - BURSA STÜDYOSU</div>', unsafe_allow_html=True)

st.markdown("""
<h1 style='text-align: center; color: #e0e0e0; font-family: "Playfair Display", serif; 
           margin-bottom: 10px; letter-spacing: 2px;'>
    Aşk-ı Muhabbet <span style='color:#c026d3;'>v46.0 BLACK</span>
</h1>
""", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#888; margin-bottom:30px;'>Bursa Stüdyosu 🎙️ • Dilay burada, sesimle yanınızdayım</p>", unsafe_allow_html=True)

# Ana Iframe (Arena sayfan)
st.components.v1.iframe(
    src="https://019d8437-ab33-7da5-ae38-4f6524d037ed.arena.site/?embed=true",
    height=750,
    scrolling=True
)

# ====================== TTS BÖLÜMÜ ======================
st.markdown("### 🎙️ Dilay'ın Sesiyle Konuşalım", unsafe_allow_html=True)

with st.container():
    st.markdown('<div class="tts-box">', unsafe_allow_html=True)
    
    col1, col2 = st.columns([3,1])
    with col1:
        metin = st.text_area(
            "Radyo metnini buraya yaz canım...",
            placeholder="Sevgili dinleyicilerim, bu akşam Bursa'dan sizlere sıcacık bir muhabbet getiriyorum...",
            height=150,
            key="tts_input"
        )
    
    with col2:
        slow = st.checkbox("Yavaş ve duygusal oku", value=False)
        if st.button("🎤 Söyle Dilay!", type="primary", use_container_width=True):
            if metin.strip():
                with st.spinner("Ses hazırlanıyor... 🎙️"):
                    try:
                        tts = gTTS(text=metin, lang='tr', slow=slow)
                        audio_bytes = BytesIO()
                        tts.write_to_fp(audio_bytes)
                        audio_bytes.seek(0)
                        
                        # Base64 ile direkt çal
                        audio_b64 = base64.b64encode(audio_bytes.read()).decode()
                        audio_html = f"""
                        <audio autoplay controls style="width:100%;">
                            <source src="data:audio/mp3;base64,{audio_b64}" type="audio/mp3">
                        </audio>
                        """
                        st.markdown(audio_html, unsafe_allow_html=True)
                        
                        st.success("Ses hazır! Otomatik çalıyor... ❤️")
                    except Exception as e:
                        st.error(f"Bir şey oldu canım: {str(e)}")
            else:
                st.warning("Önce bir şeyler yaz ki sesimi duyabilesin 😉")
    
    st.markdown('</div>', unsafe_allow_html=True)

# Şık Floating Banner (önceki gibi)
banner_html = """
<div class="floating-banner" id="banner">
    <div style="display:flex; align-items:center; gap:20px;">
        <div class="banner-logo">🎙️</div>
        <div>
            <div style="font-size:19px; font-weight:700; color:#f0f0f0;">Aşk-ı Muhabbet</div>
            <div style="font-size:13.5px; color:#a0a0aa;">v46.0 BLACK • Bursa Stüdyosu</div>
        </div>
    </div>
    <button onclick="document.getElementById('banner').style.display='none'" 
            style="background:none; border:none; color:#888; font-size:28px; cursor:pointer; padding:8px 12px; border-radius:50%;">✕</button>
</div>
"""
st.markdown(banner_html, unsafe_allow_html=True)

# Küçük not
st.markdown("""
<div style='text-align:center; margin-top:30px; color:#777; font-size:14px;'>
    Türkçe ses gTTS ile üretiliyor. Daha duygusal okumalar için "Yavaş ve duygusal oku" seçeneğini dene.<br>
    Uzun metinlerde biraz bekleyebilir, sabırlı ol canım ❤️
</div>
""", unsafe_allow_html=True)