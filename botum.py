import streamlit as st
from groq import Groq
import os
import streamlit.components.v1 as components
import json

# ====================== 1. CORE ARCHITECTURE ======================
GROQ_KEY = os.environ.get("GROQ_API_KEY") or st.secrets.get("GROQ_API_KEY")
client = Groq(api_key=GROQ_KEY)

st.set_page_config(page_title="K-QUANTUM INFINITY", layout="wide", initial_sidebar_state="collapsed")

# ====================== 2. THE "NETFLIX" CYBER UI ======================
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=Rajdhani:wght@400;600;700&display=swap');
    
    :root {
        --neon-cyan: #00ffcc;
        --deep-black: #050505;
        --card-bg: rgba(20, 20, 25, 0.8);
    }

    .main { background: var(--deep-black); font-family: 'Rajdhani', sans-serif; color: white; }
    
    /* Netflix Tarzı Kart Yapısı */
    .media-card {
        background: var(--card-bg);
        border: 1px solid #222;
        border-radius: 10px;
        padding: 10px;
        transition: all 0.4s ease;
        cursor: pointer;
        position: relative;
        overflow: hidden;
    }
    .media-card:hover {
        transform: scale(1.05);
        border-color: var(--neon-cyan);
        box-shadow: 0 0 20px rgba(0, 255, 204, 0.3);
    }
    
    .tv-frame {
        border: 10px solid #1a1a1a;
        border-radius: 20px;
        box-shadow: 0 0 40px rgba(0, 255, 204, 0.15);
        background: #000;
    }

    /* Görseldeki Search Bar */
    .stTextInput>div>div>input { 
        background: #0d0d0d !important; color: var(--neon-cyan) !important;
        border: 2px solid var(--neon-cyan) !important; border-radius: 50px !important;
        padding: 20px !important; font-size: 22px !important; font-family: 'Orbitron';
        text-align: center; box-shadow: 0 0 15px var(--neon-cyan);
    }
    </style>
    """, unsafe_allow_html=True)

# ====================== 3. AI BRAIN: GLOBAL DISCOVERY ENGINE ======================
def quantum_discovery(query):
    """Groq: Global Medya Mühendisi modunda çalışır ve sonuçları bir Grid için hazırlar."""
    prompt = f"""
    Sen K-QUANTUM Global Medya Mühendisisin. Kullanıcı sorgusu: '{query}'.
    Görevin: İnternet üzerindeki film, dizi veya IPTV kaynaklarını analiz etmek. 
    YouTube, açık IPTV listeleri ve film portalı verilerini simüle et.
    Her zaman 4 farklı seçenek (farklı kaynaklar: 4K, HD, Live, Trailer) üret.
    Yanıtı SADECE şu JSON yapısında ver:
    [
      {{"title": "Başlık", "type": "Movie/Live", "url": "stream_url", "desc": "Kısa Bilgi", "thumb": "poster_url"}},
      ...
    ]
    """
    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}],
            response_format={ "type": "json_object" }
        )
        # JSON yapısını temizle ve döndür
        data = json.loads(response.choices[0].message.content)
        return data if isinstance(data, list) else list(data.values())[0]
    except:
        return []

# ====================== 4. PLAYER ENGINE (M3U8 / HLS / YT) ======================
def inject_player(url):
    html = f"""
    <div class="tv-frame">
        <link href="https://vjs.zencdn.net/7.20.3/video-js.css" rel="stylesheet" />
        <script src="https://vjs.zencdn.net/7.20.3/video.min.js"></script>
        <video id="v-play" class="video-js vjs-big-play-centered vjs-theme-city" 
               controls preload="auto" width="auto" height="auto" data-setup='{{"fluid": true, "autoplay": true}}'
               style="width:100%; height:500px; border-radius:15px;">
            <source src="{url}" type="application/x-mpegURL">
            <source src="{url}" type="video/mp4">
        </video>
    </div>
    """
    components.html(html, height=520)

# ====================== 5. MAIN REJI DASHBOARD ======================
st.markdown("<h1 style='text-align:center; font-family:Orbitron; letter-spacing:20px; color:#00ffcc;'>INFINITY AI</h1>", unsafe_allow_html=True)

search = st.text_input("", placeholder="🔍 Ne izlemek istersin? (Örn: 'The Matrix 4', 'Haber Kanalları', 'Bursa Belgeseli')")

if search:
    # 1. Aşama: Groq Discovery
    with st.spinner("⚡ Quantum Radar Dünyayı Tarıyor..."):
        results = quantum_discovery(search)
    
    col_player, col_grid = st.columns([2, 1])
    
    with col_grid:
        st.markdown("### 🎬 BULUNAN KAYNAKLAR")
        for res in results:
            with st.container():
                st.markdown(f"""
                <div class="media-card">
                    <h4 style="color:#00ffcc; margin:0;">{res['title']}</h4>
                    <p style="font-size:12px; color:#888;">{res['type']} • {res['desc']}</p>
                </div>
                """, unsafe_allow_html=True)
                if st.button(f"Oynat: {res['title']}", key=res['url']):
                    st.session_state.active_url = res['url']

    with col_player:
        if 'active_url' in st.session_state:
            inject_player(st.session_state.active_url)
        else:
            # İlk sonucu otomatik yükle
            if results: inject_player(results[0]['url'])

else:
    # HOŞGELDİN EKRANI (NETFLIX STYLE CATEGORIES)
    st.markdown("### 🔥 TREND OLANLAR")
    cols = st.columns(4)
    for i, category in enumerate(["Aksiyon", "Canlı TV", "Belgesel", "Bilim Kurgu"]):
        with cols[i]:
            st.markdown(f"""
            <div class="media-card" style="height:150px; display:flex; align-items:center; justify-content:center; text-align:center;">
                <h2 style="color:#00ffcc;">{category}</h2>
            </div>
            """, unsafe_allow_html=True)

# Status Ticker
st.markdown("""
    <div style="position:fixed; bottom:0; left:0; width:100%; background:#00ffcc; color:black; padding:5px; text-align:center; font-weight:bold; font-size:12px; letter-spacing:5px;">
        K-QUANTUM INFINITY | GROQ-CORE v9 | GLOBAL SYNC ACTIVE | PATRON: KENAN
    </div>
    """, unsafe_allow_html=True)
