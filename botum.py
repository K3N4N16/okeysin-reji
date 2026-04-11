import streamlit as st
from groq import Groq
import json
import os
from datetime import datetime

# ====================== AYARLAR ======================
st.set_page_config(
    page_title="K-QUANTUM RADAR", 
    layout="wide", 
    page_icon="🌌"
)

# Groq Client
GROQ_KEY = os.getenv("GROQ_API_KEY") or st.secrets.get("GROQ_API_KEY")
if not GROQ_KEY:
    st.error("❌ GROQ_API_KEY bulunamadı. Streamlit secrets'a veya ortam değişkenlerine ekle.")
    st.stop()

client = Groq(api_key=GROQ_KEY)

# ====================== BAŞLIK ======================
st.markdown("""
    <h1 style='text-align:center; color:#a855f7; margin-bottom:8px;'>🌌 K-QUANTUM MULTIVERSE RADAR</h1>
    <p style='text-align:center; color:#888; font-size:1.1rem;'>Kendi IPTV listelerin + Yapay Zeka ile sınırsız arama</p>
    <hr>
""", unsafe_allow_html=True)

# ====================== KENDİ DOSYALARINI YÜKLE ======================
st.sidebar.header("📁 Kendi Listelerin")

uploaded_files = st.sidebar.file_uploader(
    "JSON veya M3U dosyası yükle", 
    type=['json', 'm3u', 'm3u8'], 
    accept_multiple_files=True
)

local_channels = []

if uploaded_files:
    for file in uploaded_files:
        try:
            if file.name.endswith('.json'):
                data = json.loads(file.read().decode('utf-8'))
                # JSON yapısına göre uyarla
                if isinstance(data, dict):
                    channels = data.get('channels', data.get('list', data))
                else:
                    channels = data
                local_channels.extend(channels if isinstance(channels, list) else [])
                
            elif file.name.endswith(('.m3u', '.m3u8')):
                content = file.read().decode('utf-8')
                lines = content.splitlines()
                i = 0
                while i < len(lines):
                    line = lines[i].strip()
                    if line.startswith('#EXTINF:'):
                        # Basit isim çıkarma
                        name = line.split(',')[-1].strip() if ',' in line else f"Kanal {len(local_channels)+1}"
                        i += 1
                        if i < len(lines):
                            url = lines[i].strip()
                            if url.startswith('http'):
                                local_channels.append({
                                    "name": name,
                                    "url": url,
                                    "source": "local_m3u",
                                    "mode": "hls"
                                })
                    i += 1
        except Exception as e:
            st.sidebar.warning(f"{file.name} okunurken hata: {str(e)}")

    st.sidebar.success(f"✅ {len(local_channels)} kanal yüklendi")

# ====================== ANA ARAMA ======================
query = st.text_input(
    "🔍 Ne aramak istiyorsun?", 
    placeholder="Matrix, Beşiktaş maçı, nostaljik türkü, Bursa canlı kamera, Sezen Aksu..."
)

col1, col2 = st.columns([1, 4])

with col1:
    if st.button("🌌 RADAR TARASIN", type="primary", use_container_width=True):
        if not query:
            st.error("Lütfen arama yapmak istediğin şeyi yaz")
        else:
            with st.spinner("🌌 Multiverse radarı taranıyor..."):
                try:
                    prompt = f"""
                    Kullanıcı şu an "{query}" arıyor.
                    Hem kendi yerel listelerinden hem de internetten kesin çalışan kaynaklar bul.
                    En az 4 tane sonuç ver.
                    JSON formatında cevap ver:
                    {{
                        "intro": "Havalı bir giriş cümlesi",
                        "results": [
                            {{"title": "Başlık", "url": "tam link", "mode": "youtube/hls/iframe", "info": "kalite veya açıklama"}}
                        ]
                    }}
                    """

                    response = client.chat.completions.create(
                        model="llama-3.3-70b-versatile",
                        messages=[{"role": "user", "content": prompt}],
                        response_format={"type": "json_object"},
                        temperature=0.7
                    )

                    data = json.loads(response.choices[0].message.content)

                    st.success(data.get("intro", "Kaynaklar bulundu!"))

                    # Sonuçları göster
                    for idx, item in enumerate(data.get("results", [])):
                        with st.container():
                            st.markdown(f"**{item.get('title', 'İsimsiz')}**")
                            st.caption(f"{item.get('mode','hls').upper()} • {item.get('info','')}")
                            if st.button(f"▶️ Oynat", key=f"play_{idx}"):
                                st.session_state.current_url = item.get('url')
                                st.session_state.current_mode = item.get('mode')
                                st.session_state.current_title = item.get('title')
                                st.rerun()

                except Exception as e:
                    st.error(f"Radar çalışırken hata: {str(e)}")

# ====================== OYNATICI ======================
if 'current_url' in st.session_state:
    st.divider()
    st.subheader(f"▶️ {st.session_state.current_title}")
    
    url = st.session_state.current_url
    mode = st.session_state.current_mode.lower()

    if mode == "youtube":
        if "watch?v=" in url:
            video_id = url.split("watch?v=")[1].split("&")[0]
        elif "youtu.be/" in url:
            video_id = url.split("youtu.be/")[1]
        else:
            video_id = url
        st.components.v1.iframe(f"https://www.youtube.com/embed/{video_id}?autoplay=1", height=500)
        
    elif mode == "hls":
        st.video(url)
        
    elif mode == "iframe":
        st.components.v1.iframe(url, height=500, scrolling=True)
        
    else:
        st.video(url)

# ====================== ALT BİLGİ ======================
st.caption(f"⏰ Son tarama: {datetime.now().strftime('%H:%M:%S')} | K-QUANTUM RADAR v1.0")
