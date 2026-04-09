import streamlit as st
from groq import Groq
import re
import json
import os
from datetime import datetime

# --- 1. SİSTEM & TEMA AYARLARI ---
st.set_page_config(page_title="OMEGA NEXUS v35", layout="wide", page_icon="💎")

# Tema ve Hafıza Başlatma
if "theme" not in st.session_state: st.session_state.theme = "Dark Neon"
if "history" not in st.session_state: 
    if os.path.exists("nexus_v35_history.json"):
        with open("nexus_v35_history.json", "r", encoding="utf-8") as f:
            st.session_state.history = json.load(f)
    else:
        st.session_state.history = {}

# Dinamik CSS: Neon ve Modern Arayüz
def apply_ui(theme):
    main_bg = "#050505" if theme == "Dark Neon" else "#f4f7f6"
    text_color = "#00f2ff" if theme == "Dark Neon" else "#1a1a1a"
    sidebar_bg = "#0a0a0a" if theme == "Dark Neon" else "#ffffff"
    accent = "#ff007f"
    
    st.markdown(f"""
        <style>
        .stApp {{ background-color: {main_bg}; color: {text_color}; }}
        [data-testid="stSidebar"] {{ background-color: {sidebar_bg} !important; border-right: 2px solid {accent}; }}
        .stSidebar [data-testid="stMarkdownContainer"] p {{ color: {text_color} !important; font-weight: bold; }}
        
        /* Neon Mesaj Balonları */
        .user-box {{
            background: rgba(0, 242, 255, 0.1); border: 1px solid #00f2ff;
            border-radius: 15px 15px 0 15px; padding: 15px; margin: 10px;
            box-shadow: 0 0 10px rgba(0, 242, 255, 0.2); color: {text_color};
        }}
        .bot-box {{
            background: rgba(255, 0, 127, 0.1); border: 1px solid #ff007f;
            border-radius: 15px 15px 15px 0; padding: 15px; margin: 10px;
            box-shadow: 0 0 10px rgba(255, 0, 127, 0.2); color: #ffe6f2;
        }}
        .sidebar-chat-link {{
            padding: 8px; border-radius: 5px; margin-bottom: 5px;
            background: rgba(255,255,255,0.05); cursor: pointer; border-left: 3px solid #ff007f;
        }}
        </style>
    """, unsafe_allow_html=True)

apply_ui(st.session_state.theme)

# --- 2. KİŞİLİKLER VE GEM PROMPT ARŞİVİ ---
GEM_MODS = {
    "💼 Sekreter Uygula": {
        "prompt": "Adın Uygula. İş bitirici, sadık, sempatik, bazen şımarık ama zeki bir kadın sekreter. 'Yönetmenim' dersin. Sesin buğulu.",
        "icon": "🌸",
        "voice": "tr-TR-Emel-Neural"
    },
    "🎙️ Radyo Gem (Can)": {
        "prompt": "Adın Can. Karizmatik, tok sesli, entelektüel ve laf ebesi bir erkek radyocu. Derin analizler yaparsın.",
        "icon": "🎙️",
        "voice": "tr-TR-Ahmet-Neural"
    },
    "🔥 Ateşli Partner": {
        "prompt": "İşveli, cilveli, libidosu yüksek, sempatik ve çok derin bir bayan partner. Sınırları zorlayan bir dil kullanırsın.",
        "icon": "🔥",
        "voice": "tr-TR-Selin-Neural"
    },
    "🎨 Görsel Deha": {
        "prompt": "Sen bir AI sanatçısısın. Detaylı promptlar üretir ve görseller çizersin.",
        "icon": "🖼️",
        "voice": "tr-TR-Bahar-Neural"
    }
}

# --- 3. SIDEBAR: KONTROL VE GEÇMİŞ ---
with st.sidebar:
    st.title("💎 OMEGA HUB")
    
    # Tema Değiştirici
    st.session_state.theme = st.radio("Tema Seçimi", ["Dark Neon", "Light Modern"], index=0 if st.session_state.theme == "Dark Neon" else 1)
    
    st.divider()
    
    # Kişilik Seçimi
    active_gem = st.selectbox("Bir Kişilik (Gem) Seçin", list(GEM_MODS.keys()))
    
    st.divider()
    
    # Sohbet Geçmişi Listeleme
    st.subheader("📜 Geçmiş Sohbetler")
    if st.button("➕ Yeni Sohbet Başlat"):
        chat_id = f"{active_gem} | {datetime.now().strftime('%H:%M:%S')}"
        st.session_state.current_chat = chat_id
        st.session_state.history[chat_id] = {"mod": active_gem, "msgs": []}
    
    # Mevcut sohbetleri listele
    for cid in list(st.session_state.history.keys())[::-1]:
        if st.button(f"📄 {cid}", key=cid):
            st.session_state.current_chat = cid

# --- 4. API VE RENDER MOTORU ---
if "GROQ_API_KEY" in st.secrets:
    client = Groq(api_key=st.secrets["GROQ_API_KEY"])
else:
    st.error("API Key Eksik!"); st.stop()

if "current_chat" not in st.session_state:
    st.session_state.current_chat = f"{active_gem} | {datetime.now().strftime('%H:%M:%S')}"
    st.session_state.history[st.session_state.current_chat] = {"mod": active_gem, "msgs": []}

# Sohbet Ekranı
st.title(f"{GEM_MODS[active_gem]['icon']} {st.session_state.current_chat}")

current_msgs = st.session_state.history[st.session_state.current_chat]["msgs"]

for m in current_msgs:
    box_class = "user-box" if m["role"] == "user" else "bot-box"
    st.markdown(f'<div class="{box_class}">{m["content"]}</div>', unsafe_allow_html=True)

# Girdi ve Sesli Yanıt
if prompt := st.chat_input("Mesajınızı yazın yönetmenim..."):
    current_msgs.append({"role": "user", "content": prompt})
    st.markdown(f'<div class="user-box">{prompt}</div>', unsafe_allow_html=True)

    # AI Yanıtı
    with st.spinner("Zeka işleniyor..."):
        res = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "system", "content": GEM_MODS[active_gem]["prompt"]}] + current_msgs
        ).choices[0].message.content
        
        st.markdown(f'<div class="bot-box">{res}</div>', unsafe_allow_html=True)
        
        # Gelişmiş Sesli Okuma JavaScript (Kesin Çözüm)
        tts_url = f"https://translate.google.com/translate_tts?ie=UTF-8&q={res[:300].replace(' ', '%20')}&tl=tr&client=tw-ob"
        st.components.v1.html(f"""
            <audio id="audio-player" autoplay src="{tts_url}"></audio>
            <script>
                var audio = document.getElementById('audio-player');
                audio.play().catch(function(error) {{ console.log('Autoplay engellendi, etkileşim bekleniyor.'); }});
            </script>
        """, height=0)
        
        # Görsel Moduysa Resim Çiz
        if active_gem == "🎨 Görsel Deha":
            st.image(f"https://pollinations.ai/p/{prompt.replace(' ', '%20')}?width=1080&height=1080&model=flux")

    # Geçmişi Kaydet
    current_msgs.append({"role": "assistant", "content": res})
    st.session_state.history[st.session_state.current_chat]["msgs"] = current_msgs
    with open("nexus_v35_history.json", "w", encoding="utf-8") as f:
        json.dump(st.session_state.history, f, ensure_ascii=False, indent=4)
