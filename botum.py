import streamlit as st
from gtts import gTTS
from io import BytesIO
import base64
import time

st.set_page_config(page_title="Aşk-ı Muhabbet v46.0 BLACK | Bursa Stüdyosu 🎙️", page_icon="🎙️", layout="wide")

st.markdown("""
<style>
    .stApp { background: #0a0a0a; }
    .main { background: linear-gradient(135deg, #0f0f0f 0%, #1a0f1f 50%, #0f0a14 100%); }
    .live-badge { position: fixed; top: 25px; left: 40px; background: #dc143c; color: white; padding: 12px 32px; border-radius: 50px; font-size: 16px; font-weight: 700; letter-spacing: 2px; z-index: 9999; box-shadow: 0 0 30px rgba(220,20,60,0.9); animation: pulse 2s infinite; }
    @keyframes pulse { 0%,100% { box-shadow: 0 0 30px rgba(220,20,60,0.9); } 50% { box-shadow: 0 0 45px rgba(220,20,60,1); } }
    .tts-box { background: rgba(20,20,30,0.95); padding: 28px; border-radius: 22px; border: 1px solid rgba(192,38,211,0.4); margin: 25px 0; }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="live-badge">● CANLI YAYINDA - BURSA STÜDYOSU</div>', unsafe_allow_html=True)

st.markdown("""
<h1 style='text-align: center; color: #e0e0e0; font-family: "Playfair Display", serif; letter-spacing: 2px;'>
    Aşk-ı Muhabbet <span style='color:#c026d3;'>v46.0 BLACK</span>
</h1>
""", unsafe_allow_html=True)

st.components.v1.iframe(src="https://019d8437-ab33-7da5-ae38-4f6524d037ed.arena.site/?embed=true", height=720, scrolling=True)

# ====================== YENİ VE DAHA DUYGUSAL TTS ======================
st.markdown("### 🎙️ Dilay'ın Daha Derin, Daha Akışkan Sesi", unsafe_allow_html=True)

with st.container():
    st.markdown('<div class="tts-box">', unsafe_allow_html=True)
    
    metin = st.text_area(
        "Radyo metnini buraya yaz canım… (daha doğal okuması için virgül ve nokta kullan)",
        placeholder="Sevgili dinleyicilerim… Bu akşam Bursa’dan size biraz hüzün, biraz da sıcak bir umut getirdim… Kalbinizden kalbine…",
        height=160
    )
    
    col1, col2, col3 = st.columns([2, 2, 1])
    with col1:
        slow_mode = st.checkbox("Daha yavaş ve duygusal oku (önerilen)", value=True)
    with col2:
        speed_hint = st.slider("Konuşma hızı ayarı (düşük = daha derin)", 0.7, 1.3, 0.9, 0.05)
    
    if st.button("🎤 Şimdi Daha Derin ve İçten Söyle Dilay!", type="primary", use_container_width=True):
        if metin.strip():
            with st.spinner("Sesimi derinleştiriyorum… Biraz sabır, bu sefer daha güzel olacak 🎙️"):
                try:
                    # Metni radyo tarzı temizle (daha akışkan olsun)
                    cleaned_text = metin.replace("...", "…").replace("..", "…")
                    
                    tts = gTTS(
                        text=cleaned_text, 
                        lang='tr', 
                        slow=slow_mode
                    )
                    
                    audio_bytes = BytesIO()
                    tts.write_to_fp(audio_bytes)
                    audio_bytes.seek(0)
                    
                    audio_b64 = base64.b64encode(audio_bytes.read()).decode()
                    audio_html = f"""
                    <audio autoplay controls style="width:100%; margin-top:10px;">
                        <source src="data:audio/mp3;base64,{audio_b64}" type="audio/mp3">
                        Tarayıcın ses çalamıyor gibi.
                    </audio>
                    """
                    st.markdown(audio_html, unsafe_allow_html=True)
                    
                    st.success("İşte bu sefer daha derin, daha kadife sesim… Nasıl buldun canım? ❤️")
                except Exception as e:
                    st.error(f"Bir şey oldu: {str(e)}")
        else:
            st.warning("Metin boş kalmasın ki sesimi duyabilesin 😉")
    
    st.markdown('</div>', unsafe_allow_html=True)

# Floating banner
st.markdown("""
<div style="position:fixed;bottom:40px;right:40px;background:rgba(15,15,22,0.95);backdrop-filter:blur(25px);border:1px solid rgba(255,255,