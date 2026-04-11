import streamlit as st
from groq import Groq
import os
import requests

# ====================== SMART MEDIA ENGINE ======================
GROQ_KEY = os.environ.get("GROQ_API_KEY") or st.secrets.get("GROQ_API_KEY")
client = Groq(api_key=GROQ_KEY)

st.set_page_config(page_title="K-QUANTUM TV OS", layout="wide", initial_sidebar_state="collapsed")

# TV Teması (Quantum Neon Style)
st.markdown("""
    <style>
    .main { background-color: #000000; color: #e0e0e0; }
    .stTextInput>div>div>input { 
        background-color: #111; 
        color: #00ffcc !important; 
        border: 2px solid #00ffcc !important;
        border-radius: 30px;
        padding: 20px;
        font-size: 22px;
        text-align: center;
    }
    .tv-status { color: #00ffcc; font-family: 'Courier New', monospace; font-size: 14px; text-align: center; }
    .ai-bubble {
        background: rgba(0, 255, 204, 0.1);
        border: 1px solid #00ffcc;
        padding: 15px;
        border-radius: 15px;
        margin: 10px 0;
    }
    </style>
    """, unsafe_allow_html=True)

# Üst Bilgi
st.markdown("<h1 style='text-align: center; color: #00ffcc;'>K-QUANTUM MEDIA AGENT</h1>", unsafe_allow_html=True)
st.markdown("<div class='tv-status'>● SİSTEM ÇALIŞIYOR: EMEL AI ASİSTAN DEVREDE</div>", unsafe_allow_html=True)

# ====================== AI KOMUT MERKEZİ ======================
col_a, col_b, col_c = st.columns([1, 6, 1])
with col_b:
    user_command = st.text_input("", placeholder="🎙️ 'TRT 1 canlı izle', 'Bursa haberleri aç' veya '90lar pop çal'...", key="cmd_input")

if user_command:
    with st.spinner("🔍 Medya kaynakları taranıyor..."):
        # 1. Adım: Groq ile kullanıcının ne izlemek istediğini ve URL tipini belirle
        ai_decision = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{
                "role": "system", 
                "content": "Sen bir Media Center asistanısın. Kullanıcının isteğine göre en iyi YouTube arama terimini belirle. Yanıtın sadece aranacak kelime olsun."
            },
            {"role": "user", "content": f"Kullanıcı şunu izlemek istiyor: {user_command}"}],
            max_tokens=50
        )
        search_query = ai_decision.choices[0].message.content.strip()
        
        # 2. Adım: YouTube üzerinde arama yap (Link oluşturma)
        # Not: Profesyonel sürümde burada YouTube API kullanılır, 
        # şimdilik akıllı yönlendirme ile en popüler sonucu hedefliyoruz.
        formatted_query = search_query.replace(" ", "+")
        search_url = f"https://www.youtube.com/results?search_query={formatted_query}"
        
        # 3. Adım: Oynatıcıyı Başlat
        st.markdown(f"<div class='ai-bubble'>🤖 <b>Asistan:</b> '{user_command}' isteğini anladım. Senin için en uygun yayını buldum ve açıyorum Patron.</div>", unsafe_allow_html=True)
        
        # TRT 1 gibi spesifik canlı yayınlar için manuel yönlendirme (Opsiyonel)
        if "trt 1" in user_command.lower():
            final_link = "https://www.youtube.com/watch?v=68E6XG6y_v4" # Örnek Canlı TRT1
        else:
            # Genel arama sonuçları için YouTube'un 'en iyi eşleşme' algoritmasını tetikleyen embed yapı
            final_link = f"https://www.youtube.com/embed?listType=search&list={formatted_query}"

        st.video(final_link)
        st.caption(f"📺 Şu an oynatılıyor: {search_query}")

else:
    st.image("https://images.unsplash.com/photo-1461151304267-38535e770d79?w=1200", caption="Komut Bekleniyor...")

# ====================== SMART TV KONTROLLERİ ======================
st.divider()
c1, c2, c3 = st.columns(3)
with c1:
    if st.button("🔴 CANLI TV MODU"):
        st.info("Haber kanalları taranıyor...")
with c2:
    if st.button("🎬 SİNEMA MODU"):
        st.info("Film fragmanları ve açık kaynaklar listeleniyor...")
with c3:
    if st.button("📻 RADYO (AŞK-I MUHABBET)"):
        st.info("Emel v49.0 radyo yayınına bağlanıyor...")

st.markdown("""
    <div style="position: fixed; bottom: 0; left: 0; width: 100%; background: #00ffcc; color: black; padding: 3px; text-align: center; font-weight: bold; font-size: 12px;">
        K-QUANTUM OS | ULTRA-SPEED MEDIA AGENT | OPERATOR: KENAN
    </div>
    """, unsafe_allow_html=True)
