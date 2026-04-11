import streamlit as st
from groq import Groq
import os
import streamlit.components.v1 as components

# ====================== 1. K-QUANTUM CORE & AI CONFIG ======================
# Groq API anahtarını sistemden alıyoruz
GROQ_KEY = os.environ.get("GROQ_API_KEY") or st.secrets.get("GROQ_API_KEY")
client = Groq(api_key=GROQ_KEY)

st.set_page_config(
    page_title="K-QUANTUM TV v7.0 Ultra AI",
    layout="wide",
    initial_sidebar_state="collapsed",
    page_icon="📺"
)

# ====================== 2. THE REJI: NEON-CYBER THEME (CSS) ======================
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=Rajdhani:wght@300;500;700&display=swap');
    
    :root {
        --bg-primary: #050505;
        --bg-secondary: #0a0a0f;
        --bg-card: #11111b; 
        --accent: #00ffcc; /* Neon Turkuaz */
        --accent-glow: rgba(0, 255, 204, 0.4);
        --text-primary: #ffffff;
        --text-secondary: #00ffcc;
    }

    .main { background-color: var(--bg-primary); color: var(--text-primary); font-family: 'Rajdhani', sans-serif; }
    
    /* TV Kasa Tasarımı */
    .tv-frame {
        border: 15px solid #1a1a1a;
        border-radius: 40px;
        background: #000;
        box-shadow: 0 0 80px rgba(0, 255, 204, 0.2);
        overflow: hidden;
        padding: 5px;
        margin-top: 10px;
        position: relative;
    }

    /* Görseldeki Neon Arama Paneli */
    .stTextInput>div>div>input { 
        background-color: #0d0d0d !important; 
        color: #00ffcc !important; 
        border: 2px solid #00ffcc !important;
        border-radius: 50px !important; 
        padding: 25px !important; 
        font-size: 20px !important;
        font-family: 'Orbitron', sans-serif;
        box-shadow: 0 0 20px rgba(0, 255, 204, 0.3);
        text-align: center;
    }

    /* K-QUANTUM Ticker */
    .status-bar {
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
        background: linear-gradient(90deg, #00ffcc, #0088ff);
        color: black;
        padding: 6px 30px;
        font-weight: 800;
        font-size: 13px;
        text-transform: uppercase;
        letter-spacing: 2px;
        z-index: 9999;
    }

    .ai-badge {
        background: rgba(0, 255, 204, 0.15);
        border: 1px solid #00ffcc;
        padding: 10px 20px;
        border-radius: 10px;
        color: #00ffcc;
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# ====================== 3. AI MEDYA MOTORU (GROQ & LOCAL DB) ======================
def get_ai_stream_advice(query):
    try:
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{
                "role": "system", 
                "content": "Sen K-QUANTUM TV'nin AI Reji asistanısın. Kullanıcıya istediği kanal veya içerik hakkında kısa, teknik ve havalı bir bilgi ver. Eğer bir kanal ismiyse, onun için varsa bilinen m3u8 kaynaklarını analiz et."
            }, {"role": "user", "content": query}],
            max_tokens=150
        )
        return completion.choices[0].message.content
    except:
        return "Quantum Reji: Bağlantı stabil. Kaynak taranıyor..."

# ====================== 4. PROFESYONEL OYNATICI (HLS.js / Video.js) ======================
def quantum_player(url):
    html_code = f"""
    <div style="background:black; width:100%; height:100%; border-radius:20px; overflow:hidden;">
        <link href="https://vjs.zencdn.net/7.20.3/video-js.css" rel="stylesheet" />
        <script src="https://vjs.zencdn.net/7.20.3/video.min.js"></script>
        <video id="k-video" class="video-js vjs-big-play-centered vjs-theme-city" 
               controls preload="auto" width="auto" height="auto" 
               data-setup='{{"fluid": true, "autoplay": true, "liveui": true}}'
               style="width:100%; height:580px;">
            <source src="{url}" type="application/x-mpegURL">
            <source src="{url}" type="video/mp4">
        </video>
    </div>
    """
    components.html(html_code, height=600)

# ====================== 5. TV INTERFACE (ANA EKRAN) ======================
st.markdown("<h1 style='text-align:center; font-family:Orbitron; color:#00ffcc; letter-spacing:15px; margin-bottom:0;'>K-QUANTUM TV</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#555; margin-bottom:30px;'>AI-POWERED MEDIA CENTER v7.0 PRO</p>", unsafe_allow_html=True)

# Arama Paneli (Görseldeki Input alanı)
user_query = st.text_input("", placeholder="🔍 Ne izlemek istersin Patron? (Kanal, Film veya Konu yazın...)")

if user_query:
    col_play, col_ai = st.columns([3, 1])
    
    # Yerel Liste Simülasyonu (ktv.txt mantığı)
    iptv_map = {
        "trt1": "https://mn-nl.mncdn.com/blutv_trt1/smil:trt1_sd.smil/playlist.m3u8",
        "haberglobal": "https://haberglobal.daioncdn.net/haberglobal/haberglobal_hls.smil/playlist.m3u8",
        "atv": "https://atv-live.daioncdn.net/atv/atv.m3u8",
        "show": "https://showtv-live.daioncdn.net/showtv/showtv.m3u8"
    }
    
    # Link Belirleme
    final_url = ""
    clean_q = user_query.lower().replace(" ", "")
    for key in iptv_map:
        if key in clean_q: final_url = iptv_map[key]; break
    
    if not final_url:
        if "http" in user_query: final_url = user_query
        else: final_url = f"https://www.youtube.com/embed?listType=search&list={user_query.replace(' ', '+')}"

    with col_play:
        st.markdown("<div class='tv-frame'>", unsafe_allow_html=True)
        quantum_player(final_url)
        st.markdown("</div>", unsafe_allow_html=True)

    with col_ai:
        st.markdown("### 🤖 REJİ ANALİZİ")
        ai_msg = get_ai_stream_advice(user_query)
        st.markdown(f"<div class='ai-badge'>{ai_msg}</div>", unsafe_allow_html=True)
        
        st.markdown("### 📡 SİNYAL DURUMU")
        st.progress(98, text="Optimal Stream")
        st.write("📍 Kaynak: Global HLS Node")
        st.write("📺 Çözünürlük: Auto HD")

else:
    # Boş ekran - TV Bekleme Modu
    st.image("https://images.unsplash.com/photo-1550745165-9bc0b252726f?w=1200", caption="K-QUANTUM BEKLEME MODUNDA... KOMUT BEKLENİYOR.")

# ====================== 6. ALT BANT (GÖRSELDEKİ FAVORİLER) ======================
st.divider()
st.markdown("### ⚡ HIZLI ERİŞİM")
c1, c2, c3, c4, c5, c6 = st.columns(6)
with c1: st.button("🔴 TRT 1 (LIVE)")
with c2: st.button("🌐 HABER GLOBAL")
with c3: st.button("⚽ SPOR TV")
with c4: st.button("🎬 SINEMA")
with c5: st.button("🎵 MUSIC")
with c6: st.button("🧬 QUANTUM AI")

# ====================== 7. GLOBAL STATUS TICKER ======================
st.markdown(f"""
    <div class="status-bar">
        📡 LIVE: K-QUANTUM GLOBAL MEDIA OS | ENGINE: GROQ-LLAMA3 | STATUS: OPTIMAL | OPERATOR: KENAN | DATE: 11-04-2026
    </div>
    """, unsafe_allow_html=True)
