import streamlit as st
from groq import Groq
import os
import streamlit.components.v1 as components
import json

# ====================== 1. MEDYA MÜHENDİSİ BEYNİ (GROQ) ======================
GROQ_KEY = os.environ.get("GROQ_API_KEY") or st.secrets.get("GROQ_API_KEY")
client = Groq(api_key=GROQ_KEY)

st.set_page_config(page_title="K-QUANTUM TV OS", layout="wide", initial_sidebar_state="collapsed")

# ====================== 2. CYBER-PUNK TV ARAYÜZÜ (GÖRSEL TASARIM) ======================
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=Rajdhani:wght@500;700&display=swap');
    
    .main { background: radial-gradient(circle, #101015 0%, #050505 100%); color: #00ffcc; font-family: 'Rajdhani', sans-serif; }
    
    /* TV Kasa Tasarımı */
    .tv-frame {
        border: 12px solid #1a1a1a;
        border-radius: 40px;
        background: #000;
        box-shadow: 0 0 50px rgba(0, 255, 204, 0.2), inset 0 0 20px #000;
        padding: 10px;
        margin-top: 10px;
    }

    /* Görseldeki Neon Arama Çubuğu */
    .stTextInput>div>div>input { 
        background-color: #0d0d0d !important; 
        color: #00ffcc !important; 
        border: 2px solid #00ffcc !important;
        border-radius: 50px !important; 
        padding: 20px !important; 
        font-size: 22px !important;
        font-family: 'Orbitron', sans-serif;
        box-shadow: 0 0 20px rgba(0, 255, 204, 0.4);
        text-align: center;
    }

    .ai-status {
        background: rgba(0, 255, 204, 0.1);
        border-left: 5px solid #00ffcc;
        padding: 15px;
        border-radius: 5px;
        margin: 10px 0;
        font-size: 14px;
    }

    .ticker-tape {
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
        background: #00ffcc;
        color: #000;
        font-weight: bold;
        padding: 5px;
        text-align: center;
        text-transform: uppercase;
        letter-spacing: 3px;
        z-index: 100;
    }
    </style>
    """, unsafe_allow_html=True)

# ====================== 3. AKILLI KAYNAK BULUCU (AI ENGINE) ======================
def ai_media_engineer(user_input):
    """Groq kullanarak internetteki IPTV/Stream linklerini analiz eder ve JSON döner."""
    try:
        prompt = f"""
        Sen bir Medya Mühendisisin. Kullanıcının isteği: '{user_input}'.
        Görevin: Bu kanal veya içerik için internetteki en güncel ve açık kaynaklı .m3u8 (HLS) yayın linkini bulmak.
        Eğer linki tam bilmiyorsan, en muhtemel çalışan resmi stream URL'sini tahmin et veya YouTube canlı yayınını hedefle.
        Yanıtını sadece şu JSON formatında ver:
        {{"channel_name": "Kanal Adı", "stream_url": "link", "analysis": "Neden bu linki seçtiğin hakkında kısa bilgi"}}
        """
        
        chat_completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}],
            response_format={ "type": "json_object" }
        )
        return json.loads(chat_completion.choices[0].message.content)
    except Exception as e:
        return {"channel_name": "Hata", "stream_url": "", "analysis": f"Sistem hatası: {str(e)}"}

# ====================== 4. PROFESYONEL HLS/IPTV PLAYER ======================
def render_player(url):
    html_code = f"""
    <div style="background:black; border-radius:25px; overflow:hidden;">
        <link href="https://vjs.zencdn.net/7.20.3/video-js.css" rel="stylesheet" />
        <script src="https://cdn.jsdelivr.net/npm/hls.js@latest"></script>
        <script src="https://vjs.zencdn.net/7.20.3/video.min.js"></script>
        <video id="k-player" class="video-js vjs-big-play-centered vjs-theme-city" 
               controls preload="auto" width="auto" height="auto" 
               data-setup='{{"fluid": true, "autoplay": true}}'
               style="width:100%; height:540px;">
            <source src="{url}" type="application/x-mpegURL">
            <source src="{url}" type="video/mp4">
        </video>
    </div>
    """
    components.html(html_code, height=560)

# ====================== 5. TV KONTROL PANELİ (REJİ) ======================
st.markdown("<h1 style='text-align:center; font-family:Orbitron; letter-spacing:10px;'>K-QUANTUM TV</h1>", unsafe_allow_html=True)

# Görseldeki Search Panel
search_query = st.text_input("", placeholder="🎙️ 'TRT 1 aç', 'Bursa Mobese bul' veya 'Bilim Kurgu filmi oynat'...")

if search_query:
    col_main, col_side = st.columns([3, 1])
    
    with st.spinner("🚀 Medya Mühendisi kaynakları tarıyor..."):
        ai_data = ai_media_engineer(search_query)
        stream_url = ai_data.get("stream_url")
        
    with col_main:
        st.markdown("<div class='tv-frame'>", unsafe_allow_html=True)
        if stream_url:
            render_player(stream_url)
        else:
            st.error("Kaynak bulunamadı. Lütfen başka bir komut verin.")
        st.markdown("</div>", unsafe_allow_html=True)
        
    with col_side:
        st.markdown("### 🤖 REJİ RAPORU")
        st.markdown(f"<div class='ai-status'><b>Kanal:</b> {ai_data.get('channel_name')}<br><br><b>Analiz:</b> {ai_data.get('analysis')}</div>", unsafe_allow_html=True)
        
        st.markdown("### ⚙️ SİSTEM")
        st.info("🛰️ HLS Engine: Aktif")
        st.info("🧠 AI Mode: Engineer v8")
        if st.button("🔄 Kaynağı Yenile"):
            st.rerun()

else:
    st.image("https://images.unsplash.com/photo-1461151304267-38535e770d79?w=1200", caption="PATRON KENAN İÇİN HAZIR. KOMUT BEKLENİYOR.")

# Alt Bant
st.markdown("""
    <div class="ticker-tape">
        ● K-QUANTUM MEDIA OS | OWNER: KENAN | AI ENGINEER ACTIVE | SIGNAL: 100% | LOCATION: BURSA HUB
    </div>
    """, unsafe_allow_html=True)
