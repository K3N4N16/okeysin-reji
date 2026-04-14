import streamlit as st
import requests
from io import BytesIO
import base64

# Sayfa ayarları (aynı güzel BLACK tema)
st.set_page_config(page_title="Aşk-ı Muhabbet v46.0 BLACK | Bursa Stüdyosu 🎙️", page_icon="🎙️", layout="wide")

st.markdown("""
<style>
    .stApp { background: #0a0a0a; }
    .main { background: linear-gradient(135deg, #0f0f0f 0%, #1a0f1f 50%, #0f0a14 100%); }
    .live-badge { position: fixed; top: 25px; left: 40px; background: #dc143c; color: white; padding: 12px 32px; border-radius: 50px; font-size: 16px; font-weight: 700; letter-spacing: 2px; z-index: 9999; box-shadow: 0 0 30px rgba(220,20,60,0.9); animation: pulse 2s infinite; }
    @keyframes pulse { 0%,100% { box-shadow: 0 0 30px rgba(220,20,60,0.9); } 50% { box-shadow: 0 0 45px rgba(220,20,60,1); } }
    .tts-box { background: rgba(20,20,30,0.9); padding: 25px; border-radius: 20px; border: 1px solid rgba(192,38,211,0.3); margin: 20px 0; }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="live-badge">● CANLI YAYINDA - BURSA STÜDYOSU</div>', unsafe_allow_html=True)

st.markdown("""
<h1 style='text-align: center; color: #e0e0e0; font-family: "Playfair Display", serif; letter-spacing: 2px;'>
    Aşk-ı Muhabbet <span style='color:#c026d3;'>v46.0 BLACK</span>
</h1>
""", unsafe_allow_html=True)

st.components.v1.iframe(src="https://019d8437-ab33-7da5-ae38-4f6524d037ed.arena.site/?embed=true", height=750, scrolling=True)

# ====================== YENİ TTS BÖLÜMÜ ======================
st.markdown("### 🎙️ Dilay'ın Daha Derin ve Duygusal Sesi", unsafe_allow_html=True)

with st.container():
    st.markdown('<div class="tts-box">', unsafe_allow_html=True)
    
    metin = st.text_area("Radyo metnini buraya yaz canım…", 
                         placeholder="Sevgili dinleyicilerim… Bu akşam Bursa’dan size biraz hüzün, biraz da umut getirdim…", 
                         height=150)
    
    col1, col2 = st.columns([3,1])
    with col1:
        if st.button("🎤 Şimdi Daha Derin Söyle Dilay!", type="primary", use_container_width=True):
            if metin.strip():
                with st.spinner("Daha derin ve akışkan ses hazırlanıyor… Bu biraz zaman alabilir 🎙️"):
                    try:
                        API_URL = "https://api-inference.huggingface.co/models/facebook/mms-tts-tur"
                        headers = {"Authorization": "Bearer hf_..."}  # Buraya kendi ücretsiz HF token'ını koy (https://huggingface.co/settings/tokens)
                        
                        payload = {"inputs": metin}
                        response = requests.post(API_URL, headers=headers, json=payload)
                        
                        if response.status_code == 200:
                            audio_bytes = BytesIO(response.content)
                            audio_b64 = base64.b64encode(audio_bytes.read()).decode()
                            audio_html = f"""
                            <audio autoplay controls style="width:100%;">
                                <source src="data:audio/wav;base64,{audio_b64}" type="audio/wav">
                            </audio>
                            """
                            st.markdown(audio_html, unsafe_allow_html=True)
                            st.success("İşte daha derin, daha akışkan sesim… Nasıl buldun canım? ❤️")
                        else:
                            st.error(f"Model şu an meşgul, birazdan tekrar dene… ({response.status_code})")
                    except Exception as e:
                        st.error(f"Bir şey oldu: {str(e)}")
            else:
                st.warning("Metin boş olmasın ki sesimi duyabilesin 😉")
    
    st.markdown('</div>', unsafe_allow_html=True)

# Floating banner aynı kalsın
st.markdown("""
<div class="floating-banner" id="banner" style="position:fixed;bottom:40px;right:40px;background:rgba(15,15,22,0.95);backdrop-filter:blur(25px);border:1px solid rgba(255,255,255,0.15);border-radius:24px;padding:20px 32px;display:flex;align-items:center;gap:20px;box-shadow:0 25px 60px rgba(0,0,0,0.8);z-index:9999;">
    <div style="display:flex;align-items:center;gap:20px;">
        <div style="font-size:42px;">🎙️</div>
        <div><div style="font-size:19px;font-weight:700;color:#f0f0f0;">Aşk-ı Muhabbet</div><div style="font-size:13.5px;color:#a0a0aa;">v46.0 BLACK • Bursa Stüdyosu</div></div>
    </div>
    <button onclick="document.getElementById('banner').style.display='none'" style="background:none;border:none;color:#888;font-size:28px;cursor:pointer;">✕</button>
</div>
""", unsafe_allow_html=True)