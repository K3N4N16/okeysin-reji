import streamlit as st
from groq import Groq
import os

# ====================== SMART TV ENGINE ======================
GROQ_KEY = os.environ.get("GROQ_API_KEY") or st.secrets.get("GROQ_API_KEY")
client = Groq(api_key=GROQ_KEY)

st.set_page_config(page_title="Kenan Quantum AI TV", layout="wide", initial_sidebar_state="collapsed")

# TV Teması ve Stil Ayarları
st.markdown("""
    <style>
    .main { background-color: #050505; color: white; }
    .stTextInput>div>div>input { background-color: #1a1a1a; color: #00ffcc; border: 1px solid #00ffcc; }
    .video-card { border: 2px solid #333; border-radius: 15px; padding: 5px; background: #111; }
    .ai-badge { background: linear-gradient(45deg, #ff00ff, #00ffff); padding: 5px 10px; border-radius: 20px; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# ====================== REJİ & KAYNAK YÖNETİMİ ======================
if "playlist" not in st.session_state:
    st.session_state.playlist = [
        {"name": "Bursa Canlı Mobese", "url": "https://www.youtube.com/watch?v=L2G57e7N_9E"},
        {"name": "Global Haber (NASA TV)", "url": "https://www.youtube.com/watch?v=21X5lGlDOfg"}
    ]

# Üst Menü
col_logo, col_search = st.columns([1, 4])
with col_logo:
    st.markdown("<h2 style='color:#00ffcc;'>K-QUANTUM TV</h2>", unsafe_allow_html=True)

with col_search:
    target_source = st.text_input("🔍 İzlemek istediğin kaynağı veya YouTube linkini buraya yaz...", placeholder="Örn: Haberler, Belgeseller veya bir URL...")

# ====================== SMART OYNATICI (PLAYER) ======================
col_main, col_side = st.columns([3, 1])

with col_main:
    if target_source:
        # AI Analiz (Groq kaynağı yorumluyor)
        with st.spinner("AI Kaynağı Analiz Ediyor..."):
            ai_analysis = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[{"role": "system", "content": "Sen bir Smart TV asistanısın. Kullanıcının girdiği kaynağı analiz et ve kısa bir açıklama yap."} ,
                         {"role": "user", "content": f"Şu kaynağı açıyorum: {target_source}"}],
                max_tokens=100
            )
            st.markdown(f"<div class='ai-badge'>🤖 AI Analizi: {ai_analysis.choices[0].message.content}</div>", unsafe_allow_html=True)
        
        # Video Oynatıcı
        st.video(target_source)
    else:
        # Varsayılan Karşılama Ekranı
        st.image("https://images.unsplash.com/photo-1593784991095-a205039470b6?w=1200", caption="Kenan Quantum TV OS Yayına Hazır")

# ====================== KANAL LİSTESİ & KÜTÜPHANE ======================
with col_side:
    st.markdown("### 📋 Kanal Listesi")
    for item in st.session_state.playlist:
        if st.button(f"📺 {item['name']}", use_container_width=True):
            st.rerun()
    
    st.divider()
    st.markdown("### ⚙️ TV Özellikleri")
    st.checkbox("Otomatik Altyazı (AI)", value=True)
    st.checkbox("Görüntü İyileştirme", value=True)
    st.slider("AI Ses Düzeyi", 0, 100, 80)

# Alt Bilgi Bandı
st.markdown("""
    <div style="position: fixed; bottom: 0; left: 0; width: 100%; background: #ff0000; color: white; padding: 5px; text-align: center; font-weight: bold;">
        LIVE: Bursa Merkez Stüdyoları AI TV Aktif | Quantum İşlemci Devrede | Patron: KENAN
    </div>
    """, unsafe_allow_html=True)
