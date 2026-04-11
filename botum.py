import streamlit as st
from groq import Groq
import os
import streamlit.components.v1 as components
import json

# ====================== 1. K-QUANTUM CORE ======================
GROQ_KEY = os.environ.get("GROQ_API_KEY") or st.secrets.get("GROQ_API_KEY")
client = Groq(api_key=GROQ_KEY)

st.set_page_config(page_title="K-QUANTUM MULTI-ENGINE", layout="wide", initial_sidebar_state="collapsed")

# ====================== 2. GÖRSEL MİMARİ (PROFESYONEL REJİ) ======================
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=Rajdhani:wght@500;700&display=swap');
    
    .main { background: #020205; color: #00ffcc; font-family: 'Rajdhani', sans-serif; }
    
    /* Gelişmiş TV Çerçevesi */
    .tv-bezel {
        border: 10px solid #1a1a1a;
        border-radius: 30px;
        background: #000;
        box-shadow: 0 0 40px rgba(0, 255, 204, 0.2);
        overflow: hidden;
        position: relative;
    }

    /* "İkramiye" Panel (Gelişmiş Kartlar) */
    .bonus-card {
        background: linear-gradient(145deg, #0d0d18, #151528);
        border: 1px solid #222;
        border-radius: 15px;
        padding: 15px;
        margin-bottom: 15px;
        transition: 0.3s;
        cursor: pointer;
    }
    .bonus-card:hover {
        border-color: #00ffcc;
        box-shadow: 0 0 20px rgba(0, 255, 204, 0.4);
        transform: scale(1.02);
    }

    .stTextInput>div>div>input { 
        background: #080808 !important; color: #00ffcc !important;
        border: 2px solid #00ffcc !important; border-radius: 50px !important;
        font-family: 'Orbitron'; text-align: center; font-size: 18px !important;
    }
    </style>
    """, unsafe_allow_html=True)

# ====================== 3. AI MEDYA MÜHENDİSİ (IFRAME & STREAM ANALİZ) ======================

def ai_resource_scanner(user_mood):
    """Groq: Moduna göre interneti tarar ve doğru 'Oynatma Modu'nu seçer."""
    prompt = f"""
    Sen bir Medya Mühendisisin. Kullanıcının isteği/modu: '{user_mood}'.
    Lütfen internetteki en iyi 4 içeriği bul. 
    İçerik tipine göre 'iframe', 'hls' veya 'youtube' modunu belirle.
    Yanıtı SADECE bu JSON formatında ver:
    {{
        "ai_speech": "Patron için kısa bir sunum mesajı",
        "playlist": [
            {{"title": "Kanal/Video Adı", "url": "URL", "mode": "iframe/hls/youtube", "info": "Kalite/Tür"}},
            ...
        ]
    }}
    """
    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}],
            response_format={"type": "json_object"}
        )
        return json.loads(response.choices[0].message.content)
    except:
        return {"ai_speech": "Reji masasında sinyal kaybı.", "playlist": []}

# ====================== 4. ÇOKLU OYNATICI MOTORU (THE ENGINE) ======================

def multi_player(url, mode):
    """İçerik tipine göre en iyi oynatıcıyı (IFrame veya HLS) tetikler."""
    if mode == "youtube":
        # YouTube linkini IFrame dostu yap
        if "watch?v=" in url: url = url.replace("watch?v=", "embed/")
        st.video(url)
    
    elif mode == "iframe":
        # Harici bir web platformunu veya portalı "ikramiye" olarak sığdırır
        components.iframe(url, height=550, scrolling=True)
        
    else: # HLS / IPTV Modu
        html_hls = f"""
        <div class="tv-bezel">
            <link href="https://vjs.zencdn.net/7.20.3/video-js.css" rel="stylesheet" />
            <script src="https://vjs.zencdn.net/7.20.3/video.min.js"></script>
            <video id="k-pro" class="video-js vjs-big-play-centered" 
                   controls preload="auto" width="auto" height="auto" data-setup='{{"fluid": true, "autoplay": true}}'
                   style="width:100%; height:540px;">
                <source src="{url}" type="application/x-mpegURL">
            </video>
        </div>
        """
        components.html(html_hls, height=560)

# ====================== 5. REJİ DASHBOARD ======================
st.markdown("<h1 style='text-align:center; font-family:Orbitron; letter-spacing:10px; color:#00ffcc;'>K-QUANTUM REJI</h1>", unsafe_allow_html=True)

# ARAMA VE MOD PANELİ
q = st.text_input("", placeholder="🎙️ Patron, bugün nasıl bir yayın yapalım? Modunu veya istediğin içeriği yaz...")

if q:
    with st.spinner("⚡ Quantum AI kaynakları ve ikramiyeleri topluyor..."):
        data = ai_resource_scanner(q)
    
    st.write(f"🎙️ **Sunucu:** {data['ai_speech']}")
    
    col_play, col_side = st.columns([2.5, 1])
    
    with col_side:
        st.markdown("### 🎁 YAYIN İKRAMİYELERİ")
        for idx, item in enumerate(data['playlist']):
            with st.container():
                st.markdown(f"""
                <div class="bonus-card">
                    <b style="color:#00ffcc;">{item['title']}</b><br>
                    <small>{item['mode'].upper()} | {item['info']}</small>
                </div>
                """, unsafe_allow_html=True)
                if st.button(f"YAYINA VER: {item['title']}", key=f"btn_{idx}"):
                    st.session_state.active_res = item

    with col_play:
        if 'active_res' in st.session_state:
            res = st.session_state.active_res
            multi_player(res['url'], res['mode'])
        elif data['playlist']:
            res = data['playlist'][0]
            multi_player(res['url'], res['mode'])

else:
    st.image("https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=1200", caption="REJİ MASASI AKTİF. EMREDİN YÖNETMENİM.")

st.markdown("<div style='position:fixed; bottom:0; left:0; width:100%; background:#00ffcc; color:000; text-align:center; font-weight:bold; padding:5px; font-size:10px; letter-spacing:5px;'>● K-QUANTUM INFINITY ENGINE v13 | BURSA HUB | OPERATOR: KENAN</div>", unsafe_allow_html=True)
