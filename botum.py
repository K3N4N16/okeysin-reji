import streamlit as st
from groq import Groq
import json
import os
from datetime import datetime

# ====================== AYARLAR ======================
st.set_page_config(page_title="K-QUANTUM RADAR", layout="wide", page_icon="🌌")

# Groq Client
GROQ_KEY = os.getenv("GROQ_API_KEY") or st.secrets.get("GROQ_API_KEY")
client = Groq(api_key=GROQ_KEY)

# ====================== BAŞLIK ======================
st.markdown("""
    <h1 style='text-align:center; color:#a855f7; margin-bottom:10px;'>🌌 K-QUANTUM MULTIVERSE RADAR</h1>
    <p style='text-align:center; color:#888;'>Kendi IPTV listelerin + Yapay Zeka ile sınırsız arama</p>
""", unsafe_allow_html=True)

# ====================== KENDİ DOSYALARINI YÜKLE ======================
st.sidebar.header("📁 Kendi Listelerin")
uploaded_files = st.sidebar.file_uploader(
    "JSON veya M3U dosyanı yükle", 
    type= , 
    accept_multiple_files=True
)

local_channels = []

if uploaded_files:
    for file in uploaded_files:
        if file.name.endswith('.json'):
            data = json.loads(file.read().decode())
            local_channels.extend(data.get('channels', data))
        elif file.name.endswith(('.m3u', '.m3u8')):
            content = file.read().decode()
            # Basit m3u parser (geliştirilebilir)
            lines = content.split('\n')
            for i, line in enumerate(lines):
                if line.startswith('#EXTINF:') and i+1 < len(lines):
                    name = line.split(',')[-1].strip()
                    url = lines .strip()
                    if url.startswith('http'):
                        local_channels.append({"name": name, "url": url, "source": "local"})

    st.sidebar.success(f"✅ {len(local_channels)} kanal yüklendi")

# ====================== ARAMA ALANI ======================
query = st.text_input("🔍 Ne aramak istiyorsun?", placeholder="Matrix 4, Beşiktaş maçı, nostaljik türkü, bursa canlı kamera...")

if st.button("🌌 RADAR TARASIN", type="primary"):
    if not query:
        st.error("Lütfen bir şey yaz")
    else:
        with st.spinner("Multiverse radarı taranıyor..."):
            try:
                prompt = f"""
                Kullanıcı şu an "{query}" arıyor.
                Hem kendi listelerinden hem internetten kesin çalışan kaynaklar bul.
                En az 4 tane sonuç ver.
                JSON formatında cevap ver:
                {{
                    "intro": "Havalı bir giriş cümlesi",
                    "results": [
                        {{"title": "Başlık", "url": "link", "mode": "youtube/hls/iframe/m3u", "info": "kalite veya açıklama"}}
                    ]
                }}
                """

                response = client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages= ,
                    response_format={"type": "json_object"}
                )

                data = json.loads(response.choices[0].message.content)

                st.success(data.get("intro", "Sonuçlar bulundu!"))

                for item in data.get("results", [ 4, 1])
                    with col1:
                        st.markdown(f"**{item }**")
                        st.caption(f"{item .upper()} | {item.get('info','')}")
                    with col2:
                        if st.button("Oynat", key=item ):
                            st.session_state.current_url = item st.session_state.current_mode = item st.session_state.current_title = item except Exception as e:
                st.error(f"Radar çalışırken hata oldu: {str(e)}")

# ====================== PLAYER ======================
if 'current_url' in st.session_state:
    st.markdown("### ▶️ Şu an oynatılıyor:")
    st.markdown(f"**{st.session_state.current_title}**")
    
    url = st.session_state.current_url
    mode = st.session_state.current_mode
    
    if mode == "youtube":
        video_id = url.split("v=")[-1 0] if "v=" in url else url.split("/")[-1]
        st.video(f"https://www.youtube.com/embed/{video_id}")
    elif mode in :
        st.video(url)
    else:
        st.components.v1.iframe(url, height=500)

# ====================== STATUS ======================
st.caption(f"⏰ Son tarama: {datetime.now().strftime('%H:%M:%S')}")
