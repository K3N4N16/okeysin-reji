import streamlit as st
from groq import Groq
import os

# ====================== SMART TV ENGINE ======================
GROQ_KEY = os.environ.get("GROQ_API_KEY") or st.secrets.get("GROQ_API_KEY")
client = Groq(api_key=GROQ_KEY)

st.set_page_config(page_title="K-QUANTUM TV", layout="wide", initial_sidebar_state="collapsed")

# TV Teması ve Gelişmiş Stil
st.markdown("""
    <style>
    .main { background-color: #000000; color: #e0e0e0; }
    .stTextInput>div>div>input { 
        background-color: #111; 
        color: #00ffcc !important; 
        border: 2px solid #222 !important;
        border-radius: 10px;
        font-size: 20px;
    }
    .stTextInput>div>div>input:focus { border: 2px solid #00ffcc !important; }
    .ai-box {
        background: rgba(0, 255, 204, 0.05);
        border-left: 5px solid #00ffcc;
        padding: 15px;
        border-radius: 5px;
        margin-bottom: 20 inline;
    }
    .status-bar {
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
        background: rgba(0,0,0,0.8);
        border-top: 1px solid #333;
        color: #00ffcc;
        padding: 5px 20px;
        font-family: monospace;
        z-index: 999;
    }
    </style>
    """, unsafe_allow_html=True)

# Üst Header
st.markdown("<h1 style='text-align: center; color: #00ffcc; letter-spacing: 5px;'>K-QUANTUM TV SYSTEM</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #666;'>Ultra Pro AI Media Center v2.0</p>", unsafe_allow_html=True)

# ====================== REJİ MERKEZİ ======================
col_search, col_info = st.columns([3, 1])

with col_search:
    target_source = st.text_input("", placeholder="🔍 İzlemek istediğin kaynağı, kanalı veya URL'yi buraya gir...", key="tv_input")

# Hata Yönetimli Oynatıcı
if target_source:
    try:
        # AI Analiz Paneli
        with st.expander("🤖 K-QUANTUM AI ANALİZİ", expanded=True):
            with st.spinner("Sistem analiz ediliyor..."):
                ai_analysis = client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=[{"role": "system", "content": "Sen bir teknoloji asistanısın. Kullanıcının girdiği medya kaynağını (link veya isim) profesyonelce yorumla. Eğer K3N4N veya QUANTUM ifadeleri geçerse, bunun Kenan'ın özel sistemi olduğunu vurgula."} ,
                             {"role": "user", "content": f"Kaynak: {target_source}"}],
                    max_tokens=150
                )
                st.markdown(f"<div class='ai-box'>{ai_analysis.choices[0].message.content}</div>", unsafe_allow_html=True)

        # Video Oynatma Alanı
        st.video(target_source)
        st.success(f"✅ Yayın Bağlandı: {target_source}")

    except Exception as e:
        st.error(f"❌ Kaynak Hatası: Girilen URL formatı TV motoru tarafından desteklenmiyor. Lütfen geçerli bir YouTube veya m3u8 linki girin.")
        st.info("İpucu: Linkin başında http:// veya https:// olduğundan emin olun.")
else:
    # Boş Ekran Görseli (TV Kapalı Modu)
    st.image("https://images.unsplash.com/photo-1550745165-9bc0b252726f?w=1200", caption="K-QUANTUM Bekleme Modunda... Lütfen bir kaynak girin.")

# ====================== ALT DURUM ÇUBUĞU ======================
st.markdown(f"""
    <div class="status-bar">
        ● SYSTEM: ONLINE | ● SIGNAL: OPTIMAL | ● ENGINE: GROQ-LLAMA3 | ● OPERATOR: KENAN | ● DATE: 11-04-2026
    </div>
    """, unsafe_allow_html=True)

# Kanal Favorileri (Yan panel yerine butonlarla aşağıda)
st.markdown("### 📡 HIZLI ERİŞİM KANALLARI")
c1, c2, c3, c4 = st.columns(4)
with c1: 
    if st.button("📽️ Bursa Canlı"): st.info("Link girilmedi")
with c2:
    if st.button("🌐 Uzay İstasyonu (Live)"): st.info("https://www.youtube.com/watch?v=EEIk7gwjgIM")
with c3:
    if st.button("🎮 Gaming Stream"): st.info("Twitch URL")
with c4:
    if st.button("🎵 Quantum Music"): st.info("YouTube Lofi URL")
