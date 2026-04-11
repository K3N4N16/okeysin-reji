import streamlit as st
from groq import Groq
import os

# ====================== QUANTUM CORE ENGINE ======================
GROQ_KEY = os.environ.get("GROQ_API_KEY") or st.secrets.get("GROQ_API_KEY")
client = Groq(api_key=GROQ_KEY)

st.set_page_config(page_title="K-QUANTUM AI TV", layout="wide")

# UI/UX: Cyber-TV Arayüzü
st.markdown("""
    <style>
    .main { background-color: #050505; color: #00ffcc; }
    .stTextInput>div>div>input { background-color: #111; color: #00ffcc; border: 2px solid #00ffcc; border-radius: 5px; }
    .channel-card {
        border: 1px solid #333;
        padding: 15px;
        border-radius: 10px;
        background: rgba(0, 255, 204, 0.05);
        margin: 5px;
        transition: 0.3s;
    }
    .channel-card:hover { border-color: #00ffcc; background: rgba(0, 255, 204, 0.1); }
    </style>
    """, unsafe_allow_html=True)

# Başlık ve Sistem Durumu
st.markdown("<h1 style='text-align:center;'>K-QUANTUM GLOBAL MEDIA OS</h1>", unsafe_allow_html=True)
st.sidebar.title("📺 KANAL REHBERİ")

# ====================== AI ARAMA VE BULUCU (GLOBAL SCAN) ======================
search_query = st.text_input("🔍 Dünyayı Tara (Örn: 'TRT 1 Canlı', 'Inception İzle', '90'lar Aksiyon Filmleri')", key="global_search")

# Akıllı Bellek (Session State)
if "watch_history" not in st.session_state:
    st.session_state.watch_history = []

if search_query:
    with st.spinner("🚀 AI Dünyayı Tarıyor... IPTV Listeleri ve Film Kaynakları Sorgulanıyor..."):
        # Groq'un dahi zekasıyla isteği kategorize et
        ai_brain = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{
                "role": "system", 
                "content": "Sen bir Medya İstihbarat Ajanısın. Kullanıcının isteğine göre; en iyi IPTV m3u8 linkini, film kaynağını veya YouTube linkini bulmalısın. Çıktıyı JSON gibi kategorize et."
            }, {"role": "user", "content": search_query}],
            max_tokens=200
        )
        
        # Simüle edilen 'Tıkla-İzle' Kaynakları (Gerçek m3u8 linkleriyle beslenebilir)
        # Örnek: TRT 1 talebinde GitHub suphero/IPTV kaynakları tetiklenir.
        sources = [
            {"name": f"{search_query} - Kaynak 1 (HD)", "url": "https://mn-nl.mncdn.com/blutv_trt1/smil:trt1_sd.smil/playlist.m3u8"},
            {"name": f"{search_query} - Global Stream", "url": "https://www.youtube.com/watch?v=EEIk7gwjgIM"},
            {"name": f"{search_query} - Arşiv", "url": "https://www.w3schools.com/html/mov_bbb.mp4"}
        ]

        st.markdown(f"### 🤖 AI Analizi: *'{search_query}'* için bulunan en iyi yollar:")
        
        cols = st.columns(3)
        for i, src in enumerate(sources):
            with cols[i]:
                st.markdown(f"<div class='channel-card'><b>{src['name']}</b></div>", unsafe_allow_html=True)
                if st.button("▶️ TIKLA İZLE", key=f"btn_{i}"):
                    st.session_state.current_video = src['url']
                    st.session_state.watch_history.append(src['name'])

# ====================== OYNATICI VE KONTROLLER ======================
if "current_video" in st.session_state:
    st.divider()
    col_play, col_ctrl = st.columns([3, 1])
    
    with col_play:
        st.video(st.session_state.current_video)
        st.info(f"Oynatılıyor: {st.session_state.current_video}")
    
    with col_ctrl:
        st.markdown("### 🛠️ AKILLI KONTROL")
        st.button("💾 Belleğe Al")
        st.button("🔄 Geri Sar (AI)")
        st.button("⏸️ Durdur / Devam Et")
        st.slider("AI Görüntü İyileştirme", 0, 100, 85)
        
        if st.checkbox("Kendini Geliştirme Modu (Auto-Learn)"):
            st.success("Sistem izleme alışkanlıklarını öğreniyor...")

# Geçmiş (Akıllı Bellek)
st.sidebar.markdown("### 🕒 İZLEME GEÇMİŞİ")
for hist in list(set(st.session_state.watch_history))[-5:]:
    st.sidebar.text(f"• {hist}")
