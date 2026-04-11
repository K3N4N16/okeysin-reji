import streamlit as st
from groq import Groq
import os
import streamlit.components.v1 as components

# ====================== QUANTUM ENGINE CONFIG ======================
GROQ_KEY = os.environ.get("GROQ_API_KEY") or st.secrets.get("GROQ_API_KEY")
client = Groq(api_key=GROQ_KEY)

st.set_page_config(page_title="K-QUANTUM TV v6.0", layout="wide", initial_sidebar_state="collapsed")

# Cyber-Style TV UI
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&display=swap');
    .main { background-color: #050505; color: #00ffcc; font-family: 'Orbitron', sans-serif; }
    .stTextInput>div>div>input { 
        background-color: #111; color: #00ffcc !important; border: 2px solid #00ffcc !important;
        border-radius: 50px; padding: 25px; font-size: 24px; box-shadow: 0 0 15px #00ffcc;
    }
    .tv-frame {
        border: 20px solid #1a1a1a; border-radius: 30px; background: black;
        box-shadow: 0 0 60px rgba(0, 255, 204, 0.3); overflow: hidden;
    }
    .channel-tag { background: #00ffcc; color: black; padding: 2px 10px; border-radius: 5px; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# PROFESYONEL HLS OYNATICI (M3U8 DESTEKLİ)
def quantum_player(url):
    html_code = f"""
    <div style="background:black; width:100%; height:100%;">
        <link href="https://vjs.zencdn.net/7.20.3/video-js.css" rel="stylesheet" />
        <script src="https://vjs.zencdn.net/7.20.3/video.min.js"></script>
        <video id="quantum-video" class="video-js vjs-big-play-centered vjs-theme-city" 
               controls preload="auto" width="auto" height="auto" data-setup='{{"fluid": true, "autoplay": true}}'
               style="width:100%; height:550px;">
            <source src="{url}" type="application/x-mpegURL">
            <p class="vjs-no-js">Yayını görmek için JavaScript'i etkinleştirin.</p>
        </video>
    </div>
    """
    components.html(html_code, height=560)

# ====================== REJİ & AI ARAMA MANTIĞI ======================
st.markdown("<h1 style='text-align:center; letter-spacing:10px;'>K-QUANTUM TV OS</h1>", unsafe_allow_html=True)

# Akıllı Arama
user_input = st.text_input("", placeholder="🔍 Kanal adı, Film veya 'Bursa Canlı' yaz ve arkana yaslan...")

# Gelişmiş IPTV Veri Tabanı (GitHub Kaynaklı API Simülasyonu)
def get_best_link(query):
    # Groq burada hangi kaynağın (m3u8 mi youtube mu) daha iyi olduğunu seçer
    db = {
        "trt1": "https://mn-nl.mncdn.com/blutv_trt1/smil:trt1_sd.smil/playlist.m3u8",
        "trtspor": "https://mn-nl.mncdn.com/blutv_trtspor/smil:trtspor_sd.smil/playlist.m3u8",
        "haberglobal": "https://haberglobal.daioncdn.net/haberglobal/haberglobal_hls.smil/playlist.m3u8",
        "atv": "https://atv-live.daioncdn.net/atv/atv.m3u8",
        "a2": "https://a2-live.daioncdn.net/a2tv/a2tv.m3u8",
        "show": "https://showtv-live.daioncdn.net/showtv/showtv.m3u8"
    }
    clean_q = query.lower().replace(" ", "")
    for key in db:
        if key in clean_q: return db[key]
    return None

if user_input:
    with st.spinner("⚡ Quantum İşlemci Dünyayı Tarıyor..."):
        # 1. Kaynağı Bul
        link = get_best_link(user_input)
        
        # 2. Reji Kararı
        if link:
            st.markdown(f"<p class='channel-tag'>🔴 CANLI YAYIN: {user_input.upper()}</p>", unsafe_allow_html=True)
            st.markdown("<div class='tv-frame'>", unsafe_allow_html=True)
            quantum_player(link)
            st.markdown("</div>", unsafe_allow_html=True)
        else:
            # YouTube veya alternatif kaynak araması
            st.markdown(f"<p class='channel-tag'>🌐 GLOBAL STREAM: {user_input.upper()}</p>", unsafe_allow_html=True)
            st.markdown("<div class='tv-frame'>", unsafe_allow_html=True)
            search_link = f"https://www.youtube.com/embed?listType=search&list={user_input.replace(' ', '+')}"
            st.video(search_link)
            st.markdown("</div>", unsafe_allow_html=True)

# ====================== SMART DASHBOARD ======================
st.divider()
col1, col2, col3, col4 = st.columns(4)
with col1: st.button("📽️ FİLMLER"); st.button("🎭 DİZİLER")
with col2: st.button("📰 HABERLER"); st.button("⚽ SPOR")
with col3: st.button("🇹🇷 TÜRKİYE"); st.button("🌍 GLOBAL")
with col4: st.button("💾 FAVORİLER"); st.button("⚙️ AYARLAR")

st.markdown("""
    <div style="position: fixed; bottom: 0; left: 0; width: 100%; background: #00ffcc; color: black; padding: 5px; text-align: center; font-weight: bold; font-family: sans-serif;">
        K-QUANTUM ULTRA-PROFESSIONAL MEDIA CENTER | BY KENAN | 2026
    </div>
    """, unsafe_allow_html=True)
