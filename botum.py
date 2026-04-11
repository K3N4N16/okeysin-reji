import streamlit as st
from groq import Groq
import os
import streamlit.components.v1 as components
import json

# ====================== 1. REJİ MERKEZİ (GROQ CONFIG) ======================
GROQ_KEY = os.environ.get("GROQ_API_KEY") or st.secrets.get("GROQ_API_KEY")
client = Groq(api_key=GROQ_KEY)

st.set_page_config(page_title="K-QUANTUM INFINITY v12", layout="wide", initial_sidebar_state="collapsed")

# ====================== 2. GÖRSEL SUNUM (NEON CYBER UI) ======================
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=Rajdhani:wght@400;600;700&display=swap');
    
    .main { background: #050505; color: #fff; font-family: 'Rajdhani', sans-serif; }
    
    /* Radyo/TV Reji Kasası */
    .reji-frame {
        border: 15px solid #111;
        border-radius: 40px;
        background: #000;
        box-shadow: 0 0 70px rgba(0, 255, 204, 0.2);
        padding: 5px;
        position: relative;
    }

    /* Mod ve Seçim Kartları (Netflix Stil) */
    .media-card {
        background: rgba(20, 20, 30, 0.9);
        border: 1px solid #333;
        border-radius: 15px;
        padding: 20px;
        text-align: center;
        transition: 0.4s all ease;
        cursor: pointer;
        border-bottom: 4px solid transparent;
    }
    .media-card:hover {
        border-bottom: 4px solid #00ffcc;
        transform: translateY(-10px);
        box-shadow: 0 15px 30px rgba(0, 255, 204, 0.3);
    }

    /* Arama ve Mod Girişi */
    .stTextInput>div>div>input { 
        background: #0d0d0d !important; color: #00ffcc !important;
        border: 2px solid #00ffcc !important; border-radius: 100px !important;
        padding: 25px !important; font-size: 22px !important; font-family: 'Orbitron';
        text-align: center; box-shadow: 0 0 20px rgba(0, 255, 204, 0.4);
    }

    .status-ticker {
        position: fixed; bottom: 0; left: 0; width: 100%;
        background: linear-gradient(90deg, #00ffcc, #0088ff);
        color: black; font-weight: bold; padding: 5px;
        text-align: center; letter-spacing: 5px; font-size: 11px;
    }
    </style>
    """, unsafe_allow_html=True)

# ====================== 3. MEDYA MÜHENDİSİ BEYNİ (AI ENGINE) ======================

def ai_content_engine(mood_or_query):
    """Groq AI: Moduna göre interneti tarar ve OYNATILABİLİR linkler bulur."""
    prompt = f"""
    Sen bir Global Medya Mühendisi ve Radyo Sunucususun. Kullanıcının modu/isteği: '{mood_or_query}'.
    Görevin: İnternet üzerindeki (YouTube, IPTV, Film Portalları) en iyi 4 içeriği bulmak.
    Önemli: Linklerin m3u8 veya doğrudan izlenebilir URL olması için tahminde bulunma, gerçekçi ol.
    Yanıtı SADECE aşağıdaki JSON formatında ver:
    {{
        "presentation": "Kısa bir radyo sunucusu anonsu (Patron bu senin için... gibi)",
        "results": [
            {{"title": "Başlık", "url": "video_veya_stream_url", "type": "Live/Movie/Music", "desc": "Neden seçildi?"}},
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
        return {"presentation": "Bağlantı hatası, reji beklemede.", "results": []}

def inject_pro_player(url):
    """Profesyonel Video.js + HLS Engine"""
    html = f"""
    <div class="reji-frame">
        <link href="https://vjs.zencdn.net/7.20.3/video-js.css" rel="stylesheet" />
        <script src="https://vjs.zencdn.net/7.20.3/video.min.js"></script>
        <video id="k-player" class="video-js vjs-big-play-centered vjs-theme-city" 
               controls preload="auto" width="auto" height="auto" data-setup='{{"fluid": true, "autoplay": true}}'
               style="width:100%; height:550px; border-radius:25px;">
            <source src="{url}" type="application/x-mpegURL">
            <source src="{url}" type="video/mp4">
        </video>
    </div>
    """
    components.html(html, height=580)

# ====================== 4. ANA REJİ MASASI ======================
st.markdown("<h1 style='text-align:center; font-family:Orbitron; letter-spacing:15px; color:#00ffcc;'>K-QUANTUM INFINITY</h1>", unsafe_allow_html=True)

# Mod Girişi
user_input = st.text_input("", placeholder="🎙️ Modunu söyle veya ne izlemek istediğini yaz... (Örn: 'Bugün çok enerjiğim, hareketli konserler bul')")

if user_input:
    # 1. AI Sunumu Al
    with st.spinner("⚡ Reji Masası Hazırlanıyor..."):
        ai_data = ai_content_engine(user_input)
    
    st.markdown(f"### 🎙️ AI SUNUCU: *\"{ai_data['presentation']}\"*")
    
    col_play, col_menu = st.columns([2.5, 1])

    with col_menu:
        st.markdown("### 🎬 SANA ÖZEL SEÇİMLER")
        for idx, item in enumerate(ai_data['results']):
            with st.container():
                st.markdown(f"""
                <div class="media-card">
                    <strong style="color:#00ffcc;">{item['title']}</strong><br>
                    <small>{item['type']} • {item['desc']}</small>
                </div>
                """, unsafe_allow_html=True)
                if st.button(f"YAYINA AL: {item['title']}", key=f"btn_{idx}"):
                    st.session_state.current_url = item['url']

    with col_play:
        if 'current_url' in st.session_state:
            inject_pro_player(st.session_state.current_url)
        elif ai_data['results']:
            inject_pro_player(ai_data['results'][0]['url'])
else:
    # Bekleme Ekranı
    st.image("https://images.unsplash.com/photo-1478737270239-2fccd27ee086?w=1200", caption="REJİ SİNYAL BEKLİYOR. MODUNU SÖYLE, DÜNYAYI ÖNÜNE SEREYİM PATRON.")

# Ticker
st.markdown("<div class='status-ticker'>● GLOBAL MEDIA ARCHITECT v12 | MOOD-SYNC ACTIVE | OWNER: KENAN | 📍 BURSA HUB</div>", unsafe_allow_html=True)
