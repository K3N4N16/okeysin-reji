import streamlit as st
import time

# Sayfa yapılandırması
st.set_page_config(
    page_title="Aşk-ı Muhabbet v46.0 BLACK | Bursa Stüdyosu 🎙️",
    page_icon="🎙️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS - Gerçek BLACK & Neon stüdyo havası
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Playfair+Display:wght@700&display=swap');
    
    .stApp {
        background: #0a0a0a;
    }
    
    .main {
        background: linear-gradient(135deg, #0f0f0f 0%, #1a0f1f 50%, #0f0a14 100%);
    }
    
    .live-badge {
        position: fixed;
        top: 25px;
        left: 40px;
        background: #dc143c;
        color: white;
        padding: 12px 32px;
        border-radius: 50px;
        font-size: 16px;
        font-weight: 700;
        letter-spacing: 2px;
        z-index: 9999;
        box-shadow: 0 0 30px rgba(220, 20, 60, 0.9);
        animation: pulse 2s infinite;
        display: flex;
        align-items: center;
        gap: 10px;
    }
    
    @keyframes pulse {
        0%, 100% { box-shadow: 0 0 30px rgba(220, 20, 60, 0.9); }
        50% { box-shadow: 0 0 45px rgba(220, 20, 60, 1); }
    }
    
    .floating-banner {
        position: fixed;
        bottom: 40px;
        right: 40px;
        background: rgba(15, 15, 22, 0.95);
        backdrop-filter: blur(25px);
        border: 1px solid rgba(255,255,255,0.15);
        border-radius: 24px;
        padding: 20px 32px;
        display: flex;
        align-items: center;
        gap: 20px;
        box-shadow: 0 25px 60px rgba(0,0,0,0.8);
        z-index: 9999;
        transition: all 0.7s cubic-bezier(0.34, 1.56, 0.64, 1);
    }
    
    .floating-banner:hover {
        transform: translateY(-8px) scale(1.04);
        box-shadow: 0 35px 70px rgba(192, 38, 211, 0.35);
    }
    
    .banner-logo {
        font-size: 42px;
        animation: mic-pulse 3s infinite ease-in-out;
    }
    
    @keyframes mic-pulse {
        0%, 100% { transform: scale(1); }
        50% { transform: scale(1.12); }
    }
    
    .banner-text .upper {
        font-size: 19px;
        font-weight: 700;
        color: #f0f0f0;
        letter-spacing: 1px;
    }
    
    .banner-text .lower {
        font-size: 13.5px;
        color: #a0a0aa;
    }
    
    .close-btn {
        background: none;
        border: none;
        color: #888;
        font-size: 28px;
        cursor: pointer;
        padding: 8px 12px;
        border-radius: 50%;
        transition: all 0.4s;
    }
    
    .close-btn:hover {
        color: #ff4d4d;
        background: rgba(255,77,77,0.15);
        transform: rotate(90deg);
    }
    
    iframe {
        border-radius: 12px;
        box-shadow: 0 0 40px rgba(0,0,0,0.6);
    }
</style>
""", unsafe_allow_html=True)

# Live Badge
st.markdown('<div class="live-badge">● CANLI YAYINDA - BURSA STÜDYOSU</div>', unsafe_allow_html=True)

# Ana başlık (güzel görünüm için)
st.markdown("""
<h1 style='text-align: center; color: #e0e0e0; font-family: "Playfair Display", serif; 
           margin-bottom: 10px; letter-spacing: 2px;'>
    Aşk-ı Muhabbet <span style='color:#c026d3;'>v46.0 BLACK</span>
</h1>
""", unsafe_allow_html=True)

st.markdown("<p style='text-align:center; color:#888; margin-bottom:30px;'>Bursa Stüdyosu 🎙️</p>", unsafe_allow_html=True)

# Iframe (orijinal Arena sayfan)
st.components.v1.iframe(
    src="https://019d8437-ab33-7da5-ae38-4f6524d037ed.arena.site/?embed=true",
    height=800,
    scrolling=True
)

# Şık Floating Banner
banner_html = """
<div class="floating-banner" id="banner">
    <div style="display:flex; align-items:center; gap:20px;">
        <div class="banner-logo">🎙️</div>
        <div class="banner-text">
            <div class="upper">Aşk-ı Muhabbet</div>
            <div class="lower">v46.0 BLACK • Bursa Stüdyosu</div>
        </div>
    </div>
    <button class="close-btn" onclick="document.getElementById('banner').style.display='none'">✕</button>
</div>
"""
st.markdown(banner_html, unsafe_allow_html=True)

# Küçük bir hoş geldin mesajı
st.markdown("""
<div style='text-align:center; margin-top:40px; color:#777; font-size:14px;'>
    Hoş geldin sevgili dinleyicimiz... Çaylar demlendi, mikrofonlar açıldı.<br>
    Keyifli muhabbetler dileriz ❤️
</div>
""", unsafe_allow_html=True)

# Otomatik banner kapatma animasyonu için ufak JS
st.markdown("""
<script>
    setTimeout(() => {
        const banner = document.getElementById('banner');
        if (banner) {
            banner.style.transition = 'all 0.8s ease';
        }
    }, 8000);
</script>
""", unsafe_allow_html=True)