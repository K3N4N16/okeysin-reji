import streamlit as st
from groq import Groq
import os
import streamlit.components.v1 as components
import json

# ====================== 1. RADAR MERKEZİ (GROQ) ======================
GROQ_KEY = os.environ.get("GROQ_API_KEY") or st.secrets.get("GROQ_API_KEY")
client = Groq(api_key=GROQ_KEY)

st.set_page_config(page_title="K-QUANTUM MULTIVERSE", layout="wide", initial_sidebar_state="collapsed")

# ====================== 2. GÖRSEL REJİ TASARIMI (MASTER UI) ======================
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=Rajdhani:wght@500;700&display=swap');
    
    .main { background: #000; color: #00ffcc; font-family: 'Rajdhani', sans-serif; }
    
    /* Neon TV Kasası */
    .master-screen {
        border: 10px solid #111;
        border-radius: 25px;
        background: #000;
        box-shadow: 0 0 50px rgba(0, 255, 204, 0.3);
        overflow: hidden;
        position: relative;
    }

    /* Medya Kartları (Netflix Tarzı) */
    .media-shelf {
        background: rgba(10, 10, 20, 0.9);
        border: 1px solid #1a1a2e;
        border-radius: 15px;
        padding: 15px;
        margin: 10px 0;
        transition: 0.4s;
        cursor: pointer;
    }
    .media-shelf:hover {
        border-color: #00ffcc;
        box-shadow: 0 0 15px #00ffcc;
        transform: translateX(10px);
    }

    .stTextInput>div>div>input { 
        background: #0d0d0d !important; color: #00ffcc !important;
        border: 2px solid #00ffcc !important; border-radius: 50px !important;
        font-family: 'Orbitron'; text-align: center; font-size: 1.2rem !important;
    }
    </style>
    """, unsafe_allow_html=True)

# ====================== 3. MULTIVERSE SEARCH ENGINE ======================

def multiverse_radar(user_input):
    """Groq: İnterneti, YouTube'u ve Global Film Sunucularını tarar."""
    prompt = f"""
    Sen bir Medya Mimarı ve Global Reji Şefisin. Kullanıcının isteği: '{user_input}'.
    İnternetteki YouTube listelerini, m3u8 streamlerini, sosyal medya videolarını ve dizi/film klasörlerini tara.
    Bana 4 adet kesin çalışan kaynak bul. YouTube için 'youtube', web siteleri için 'iframe', direkt stream için 'hls' modunu seç.
    Yanıtı SADECE bu JSON formatında ver:
    {{
        "intro": "Patron için havalı bir sunum cümlesi",
        "library": [
            {{"title": "İçerik Adı", "url": "URL", "mode": "youtube/hls/iframe", "info": "Tür/Kalite"}},
            ...
        ]
    }}
    """
    try:
        res = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}],
            response_format={"type": "json_object"}
        )
        return json.loads(res.choices[0].message.content)
    except:
        return {"intro": "Sinyal zayıf, tekrar taranıyor...", "library": []}

# ====================== 4. THE ULTIMATE PLAYER (HIBRYD ENGINE) ======================

def render_multiverse_player(url, mode):
    """YouTube, IFrame ve HLS'yi tek bir ekranda birleştirir."""
    if mode == "youtube":
        # YouTube URL Dönüştürücü (Embed modu)
        if "watch?v=" in url: url = url.split("watch?v=")[1].split("&")[0]
        elif "youtu.be/" in url: url = url.split("youtu.be/")[1]
        embed_url = f"https://www.youtube.com/embed/{url}?autoplay=1&rel=0"
        components.iframe(embed_url, height=580)
        
    elif mode == "iframe":
        # Dizi siteleri, Portal veya Web içerikleri
        components.iframe(url, height=580, scrolling=True)
        
    else: # HLS / IPTV / Klasör Video (.m3u8, .mp4)
        html_code = f"""
        <div class="master-screen">
            <link href="https://vjs.zencdn.net/7.20.3/video-js.css" rel="stylesheet" />
            <script src="https://vjs.zencdn.net/7.20.3/video.min.js"></script>
            <video id="multiverse-v" class="video-js vjs-big-play-centered" 
                   controls preload="auto" width="auto" height="auto" data-setup='{{"fluid": true, "autoplay": true}}'
                   style="width:100%; height:570px;">
                <source src="{url}" type="application/x-mpegURL">
                <source src="{url}" type="video/mp4">
            </video>
        </div>
        """
        components.html(html_code, height=600)

# ====================== 5. MASTER REJI INTERFACE ======================
st.markdown("<h1 style='text-align:center; font-family:Orbitron; letter-spacing:10px; color:#00ffcc; text-shadow: 0 0 10px #00ffcc;'>K-QUANTUM MULTIVERSE</h1>", unsafe_allow_html=True)

# GİRİŞ PANELİ (MOD VEYA İSİM)
cmd = st.text_input("", placeholder="🎙️ 'Hakan Bey için nostaljik bir türkü listesi', 'Bursa canlı kamera' veya 'Matrix 4'...")

if cmd:
    with st.spinner("🌌 Multiverse Radarı Taranıyor..."):
        data = multiverse_radar(cmd)
    
    st.markdown(f"**🎙️ REJİ:** *\"{data['intro']}\"*")
    
    col_v, col_l = st.columns([3, 1])
    
    with col_l:
        st.markdown("### 📚 MEDYA KÜTÜPHANESİ")
        for idx, m in enumerate(data['library']):
            with st.container():
                st.markdown(f"""
                <div class="media-shelf">
                    <b style="color:#00ffcc;">{m['title']}</b><br>
                    <small style="color:#888;">{m['mode'].upper()} | {m['info']}</small>
                </div>
                """, unsafe_allow_html=True)
                if st.button(f"YÜKLE: {m['title']}", key=f"m_{idx}"):
                    st.session_state.target_res = m

    with col_v:
        if 'target_res' in st.session_state:
            sel = st.session_state.target_res
            render_multiverse_player(sel['url'], sel['mode'])
        elif data['library']:
            sel = data['library'][0]
            render_multiverse_player(sel['url'], sel['mode'])

else:
    st.image("https://images.unsplash.com/photo-1485846234645-a62644f84728?w=1200", caption="RADAR BEKLEMEDE. DÜNYAYI IŞINLAMAK İÇİN BİR ŞEYLER YAZ PATRON.")

# Status Bar
st.markdown("<div style='position:fixed; bottom:0; left:0; width:100%; background:linear-gradient(90deg, #00ffcc, #001111); color:white; text-align:center; font-weight:bold; padding:5px; font-size:10px; letter-spacing:5px;'>● K-QUANTUM MULTIVERSE ENGINE v14 | ALL-IN-ONE MEDIA HUB | OWNER: KENAN</div>", unsafe_allow_html=True)
