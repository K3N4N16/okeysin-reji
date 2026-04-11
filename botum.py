import streamlit as st
from groq import Groq
import os
import streamlit.components.v1 as components

# ====================== QUANTUM OS CONFIGURATION ======================
GROQ_KEY = os.environ.get("GROQ_API_KEY") or st.secrets.get("GROQ_API_KEY")
client = Groq(api_key=GROQ_KEY)

st.set_page_config(
    page_title="K-QUANTUM TV v7.0",
    layout="wide",
    initial_sidebar_state="collapsed",
    page_icon="📺"
)

# ====================== CYBER-TV THEME (Görsel Kalıp) ======================
# Görseldeki neon çizgileri, metalik dokuyu ve butonları simüle eden gelişmiş CSS
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&display=swap');
    .main { background-color: #050505; color: #00ffcc; font-family: 'Orbitron', sans-serif; }
    
    /* TV Kasa (TV FRAME) Tasarımı */
    .tv-frame {
        border: 20px solid #1a1a1a;
        border-radius: 30px;
        background: #000;
        box-shadow: 0 0 60px rgba(0, 255, 204, 0.3);
        overflow: hidden;
        padding: 5px;
        margin-bottom: 20px;
    }
    .tv-header {
        text-align: center;
        border-bottom: 1px solid #333;
        padding-bottom: 10px;
        margin-bottom: 10px;
    }
    
    /* Gelişmiş Neon Input (Görseldeki Search Bar) */
    .stTextInput>div>div>input { 
        background-color: #111; 
        color: #00ffcc !important; 
        border: 2px solid #00ffcc !important;
        border-radius: 50px; 
        padding: 25px; 
        font-size: 20px;
        box-shadow: 0 0 15px rgba(0, 255, 204, 0.5);
        text-align: center;
    }
    
    /* Kanal Butonları (Görseldeki Alt Bant) */
    .channel-tag {
        background: rgba(0, 255, 204, 0.1);
        color: #00ffcc;
        padding: 5px 15px;
        border-radius: 5px;
        font-weight: bold;
        border: 1px solid #00ffcc;
    }
    
    /* Alt Durum Çubuğu (Görseldeki Ticker) */
    .status-ticker {
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
        background: #00ffcc;
        color: black;
        padding: 5px 20px;
        font-weight: bold;
        font-family: sans-serif;
        font-size: 14px;
        z-index: 999;
    }
    </style>
    """, unsafe_allow_html=True)

# ====================== PROFESYONEL OYNATICI (Video.js/HLS.js) ======================
def quantum_player(url):
    # Görseldeki ekranın içinde çalışacak profesyonel HTML5/HLS oynatıcı
    html_code = f"""
    <div style="background:black; width:100%; height:100%;">
        <link href="https://vjs.zencdn.net/7.20.3/video-js.css" rel="stylesheet" />
        <script src="https://vjs.zencdn.net/7.20.3/video.min.js"></script>
        <video id="quantum-video" class="video-js vjs-big-play-centered vjs-theme-city" 
               controls preload="auto" width="auto" height="auto" data-setup='{{"fluid": true, "autoplay": true}}'
               style="width:100%; height:550px;">
            <source src="{url}" type="application/x-mpegURL">
            <source src="{url}" type="video/mp4">
            <p class="vjs-no-js">Yayını görmek için JavaScript'i etkinleştirin.</p>
        </video>
    </div>
    """
    components.html(html_code, height=560)

# ====================== SMART REJİ (AI ARAMA MANTIĞI) ======================
st.markdown("<div class='tv-header'><h1 style='letter-spacing:8px;'>K-QUANTUM TV</h1><p style='color:#666;'>AI MEDIA OS v7.0</p></div>", unsafe_allow_html=True)

# Akıllı Arama Çubuğu (Görseldeki Panel)
with st.expander("🤖 K-QUANTUM AI SORGULAMA PANELİ", expanded=True):
    query = st.text_input("", placeholder="🔍 Ne izlemek istersin Patron? (Örn: 'TRT 1 Canlı', 'Bursa Haber', 'Quantum Belgeseli')...")

# Gelişmiş IPTV Veri Tabanı (Gerçek Raw Linkleri)
def get_best_link(q):
    q_clean = q.lower().replace(" ", "")
    # Popüler TR IPTV Kanalları (m3u8 Listeleri)
    iptv_db = {
        "trt1": "https://mn-nl.mncdn.com/blutv_trt1/smil:trt1_sd.smil/playlist.m3u8",
        "haberglobal": "https://haberglobal.daioncdn.net/haberglobal/haberglobal_hls.smil/playlist.m3u8",
        "atv": "https://atv-live.daioncdn.net/atv/atv.m3u8",
        "show": "https://showtv-live.daioncdn.net/showtv/showtv.m3u8",
        "startv": "https://startv-live.daioncdn.net/startv/startv.m3u8",
        "bursa": "https://www.youtube.com/watch?v=EEIk7gwjgIM" # Örnek Bursa Live
    }
    for key in iptv_db:
        if key in q_clean: return iptv_db[key]
    
    # Özel link analizi
    if "http" in q: return q
    
    return None

# ====================== ANA EKRAN & OYNATICI DÖNGÜSÜ ======================
if query:
    with st.spinner("⚡ Quantum İşlemci Dünyayı Tarıyor..."):
        # 1. Kaynağı Bul
        link = get_best_link(query)
        
        # 2. Reji Paneli ve TV Ekranı
        st.markdown(f"<p class='channel-tag'>🔴 CANLI YAYIN: {query.upper()}</p>", unsafe_allow_html=True)
        st.markdown("<div class='tv-frame'>", unsafe_allow_html=True)
        
        if link:
            if ".m3u8" in link or "blutv" in link: # IPTV Formatları
                quantum_player(link)
            else: # YouTube veya Genel Linkler
                st.video(link)
        else:
            # Otomatik YouTube Arama Entegrasyonu
            search_url = f"https://www.youtube.com/embed?listType=search&list={query.replace(' ', '+')}"
            st.video(search_url)
            st.info("İpucu: Eğer kanal açılmadıysa, YouTube arama sonuçları gösteriliyor.")

        st.markdown("</div>", unsafe_allow_html=True)

# ====================== KANAL FAVORİLERİ (Görseldeki Alt Bant) ======================
st.divider()
st.markdown("### 📡 HIZLI KANAL REHBERİ")
c1, c2, c3, c4, c5 = st.columns(5)
with c1: st.button("🔴 TRT 1", use_container_width=True, key="trt1_btn")
with c2: st.button("🌐 HABER GLOBAL", use_container_width=True, key="hg_btn")
with c3: st.button("🔵 SPOR", use_container_width=True, key="spor_btn")
with c4: st.button("🎬 SİNEMA HD", use_container_width=True, key="sinema_btn")
with c5: st.button("🎵 MUSIC MIX", use_container_width=True, key="music_btn")

# ====================== ALT DURUM ÇUBUĞU (Görseldeki Ticker) ======================
st.markdown(f"""
    <div class="status-ticker">
        ● LIVE: K-QUANTUM GLOBAL MEDIA OS | ENGINES: GROQ-LLAMA3, VIDEO.JS, HLS.JS | OWNER: PATRON KENAN | 📍 BURSA AI HUB
    </div>
    """, unsafe_allow_html=True)
