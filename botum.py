import streamlit as st
from groq import Groq
import os
import streamlit.components.v1 as components
import json
import re

# ====================== 1. CORE & AI CONFIG ======================
GROQ_KEY = os.environ.get("GROQ_API_KEY") or st.secrets.get("GROQ_API_KEY")
client = Groq(api_key=GROQ_KEY)

st.set_page_config(page_title="K-QUANTUM INFINITY v10", layout="wide", initial_sidebar_state="collapsed")

# ====================== 2. CYBER-PUNK NETFLIX UI ======================
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=Rajdhani:wght@500;700&display=swap');
    
    body { background-color: #050505; }
    .main { background: transparent; color: #fff; font-family: 'Rajdhani', sans-serif; }
    
    /* GÖRSELDEKİ O NEON TV KASASI */
    .tv-container {
        border: 10px solid #1a1a1a;
        border-radius: 30px;
        background: #000;
        box-shadow: 0 0 50px rgba(0, 255, 204, 0.2);
        padding: 5px;
        margin-bottom: 20px;
    }

    /* NETFLIX TARZI KARTLAR */
    .media-card {
        background: rgba(20, 20, 25, 0.9);
        border: 1px solid #333;
        border-radius: 12px;
        padding: 15px;
        transition: 0.4s all;
        cursor: pointer;
        height: 100%;
        border-bottom: 3px solid transparent;
    }
    .media-card:hover {
        border-bottom: 3px solid #00ffcc;
        transform: translateY(-5px);
        box-shadow: 0 10px 20px rgba(0, 255, 204, 0.2);
    }

    /* GÖRSELDEKİ NEON INPUT */
    .stTextInput>div>div>input { 
        background: #0d0d0d !important; color: #00ffcc !important;
        border: 2px solid #00ffcc !important; border-radius: 50px !important;
        padding: 18px !important; font-size: 20px !important; font-family: 'Orbitron';
        text-align: center; box-shadow: 0 0 15px rgba(0, 255, 204, 0.3);
    }

    .status-ticker {
        position: fixed; bottom: 0; left: 0; width: 100%;
        background: #00ffcc; color: #000; padding: 5px;
        text-align: center; font-weight: bold; font-size: 11px;
        letter-spacing: 4px; z-index: 999;
    }
    </style>
    """, unsafe_allow_html=True)

# ====================== 3. MEDYA MÜHENDİSLİĞİ FONKSİYONLARI ======================

def get_local_channels(query):
    """Senin ktv.txt dosyanın içindeki kanalları simüle eder."""
    # Burada normalde ktv.txt okunur, şimdilik ana kanalları ekledim
    local_db = [
        {"name": "TRT 1", "url": "https://mn-nl.mncdn.com/blutv_trt1/smil:trt1_sd.smil/playlist.m3u8"},
        {"name": "Haber Global", "url": "https://haberglobal.daioncdn.net/haberglobal/haberglobal_hls.smil/playlist.m3u8"},
        {"name": "ATV HD", "url": "https://atv-live.daioncdn.net/atv/atv.m3u8"}
    ]
    return [ch for ch in local_db if query.lower() in ch['name'].lower()]

def ai_discovery_engine(query):
    """Groq API: Dünyadaki yayınları tarar ve Netflix kartları üretir."""
    prompt = f"""
    Sen bir AI Medya Mühendisisin. Kullanıcı '{query}' aratıyor. 
    İnternetteki en iyi m3u8, YouTube veya Film portalı linklerini bul. 
    Lütfen bana 4 adet sonuç döndür. Format kesinlikle şu JSON listesi olsun:
    [
        {{"title": "Başlık", "url": "çalışan_link", "type": "Canlı/Film", "info": "Kalite Bilgisi"}},
        ...
    ]
    """
    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}],
            response_format={"type": "json_object"}
        )
        data = json.loads(response.choices[0].message.content)
        return data.get("results", data) if isinstance(data, dict) else data
    except:
        return []

def play_media(url):
    """Profesyonel Video.js Oynatıcı Entegrasyonu"""
    html_player = f"""
    <div class="tv-container">
        <link href="https://vjs.zencdn.net/7.20.3/video-js.css" rel="stylesheet" />
        <script src="https://vjs.zencdn.net/7.20.3/video.min.js"></script>
        <video id="k-infinity-player" class="video-js vjs-big-play-centered vjs-theme-city" 
               controls preload="auto" width="auto" height="auto" data-setup='{{"fluid": true, "autoplay": true}}'
               style="width:100%; height:500px; border-radius:15px;">
            <source src="{url}" type="application/x-mpegURL">
            <source src="{url}" type="video/mp4">
        </video>
    </div>
    """
    components.html(html_player, height=520)

# ====================== 4. ANA REJİ EKRANI ======================
st.markdown("<h1 style='text-align:center; font-family:Orbitron; letter-spacing:10px; color:#00ffcc;'>K-QUANTUM INFINITY</h1>", unsafe_allow_html=True)

# ARAMA ÇUBUĞU
search_input = st.text_input("", placeholder="🔍 Bir kanal, film veya dizi ismi yazın...")

if search_input:
    # 1. Adım: Önce Yerel Listede Bak
    local_results = get_local_channels(search_input)
    
    # 2. Adım: Groq AI ile Dünyayı Tara
    with st.spinner("🚀 Quantum AI Medya Mühendisi Dünyayı Tarıyor..."):
        ai_results = ai_discovery_engine(search_input)
        if isinstance(ai_results, dict): # JSON temizleme
            ai_results = list(ai_results.values())[0] if len(ai_results) > 0 else []

    # EKRAN DÜZENİ
    col_play, col_results = st.columns([2, 1])

    with col_results:
        st.markdown("### 🎬 BULUNAN KAYNAKLAR")
        
        # Yerel Sonuçlar
        for ch in local_results:
            with st.container():
                st.markdown(f"<div class='media-card'><b>📡 {ch['name']}</b><br><small>Yerel Liste (Stabil)</small></div>", unsafe_allow_html=True)
                if st.button(f"Hemen İzle: {ch['name']}", key=ch['url']):
                    st.session_state.active_url = ch['url']

        # AI Sonuçları
        if isinstance(ai_results, list):
            for res in ai_results:
                title = res.get('title', 'Bilinmeyen İçerik')
                url = res.get('url', '')
                st.markdown(f"<div class='media-card'><b>🎬 {title}</b><br><small>{res.get('type')} • {res.get('info')}</small></div>", unsafe_allow_html=True)
                if st.button(f"AI Kaynağını Aç: {title}", key=url):
                    st.session_state.active_url = url

    with col_play:
        if 'active_url' in st.session_state:
            play_media(st.session_state.active_url)
        elif local_results:
            play_media(local_results[0]['url'])
        elif isinstance(ai_results, list) and len(ai_results) > 0:
            play_media(ai_results[0].get('url'))

else:
    # BOŞ EKRAN - HOŞGELDİNİZ
    st.image("https://images.unsplash.com/photo-1593784991095-a205069470b6?w=1200", caption="K-QUANTUM RADAR AKTİF. PATRON KENAN'DAN KOMUT BEKLENİYOR.")

# ALT BANT
st.markdown("<div class='status-ticker'>● GLOBAL SYNC ACTIVE | GROQ-LLAMA3 | REJI: BURSA HUB | OPERATOR: KENAN</div>", unsafe_allow_html=True)
