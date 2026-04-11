import streamlit as st
from groq import Groq
import json
import os
from datetime import datetime

st.set_page_config(page_title="K-QUANTUM RADAR", layout="wide", page_icon="🌌")

# ====================== GROQ ======================
GROQ_KEY = os.getenv("GROQ_API_KEY") or st.secrets.get("GROQ_API_KEY")
if not GROQ_KEY:
    st.error("❌ GROQ_API_KEY eksik!")
    st.stop()

client = Groq(api_key=GROQ_KEY)

# ====================== BAŞLIK ======================
st.markdown("<h1 style='text-align:center; color:#a855f7;'>🌌 K-QUANTUM MULTIVERSE RADAR</h1>", unsafe_allow_html=True)

query = st.text_input("🔍 Ne arıyorsun?", placeholder="Beşiktaş maçı, nostaljik türkü, Matrix, Bursa canlı kamera...")

if st.button("🌌 RADAR TARASIN", type="primary"):
    if query:
        with st.spinner("🌌 Radar taranıyor..."):
            try:
                prompt = f'Kullanıcı "{query}" arıyor. 4-5 tane kesin çalışan kaynak bul. JSON formatı: {{"intro": "...", "results": [{{"title":"..", "url":"..", "mode":"youtube/hls/iframe", "info":".."}}]}}'

                response = client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=[{"role": "user", "content": prompt}],
                    response_format={"type": "json_object"}
                )

                data = json.loads(response.choices[0].message.content)

                st.success(data.get("intro", "Kaynaklar bulundu!"))

                for idx, item in enumerate(data.get("results", [])):
                    col1, col2 = st.columns([5, 1])
                    with col1:
                        st.markdown(f"**{item.get('title', 'İsimsiz')}**")
                        st.caption(f"{item.get('mode','hls').upper()} • {item.get('info','')}")
                    with col2:
                        if st.button("▶️ Oynat", key=f"play_btn_{idx}"):
                            st.session_state.play_url = item.get('url')
                            st.session_state.play_mode = item.get('mode', 'hls').lower()
                            st.session_state.play_title = item.get('title', 'Yayın')
                            st.rerun()
            except Exception as e:
                st.error(f"Radar hatası: {e}")

# ====================== GÜÇLÜ PLAYER (Televizyon Ekranı) ======================
if 'play_url' in st.session_state:
    st.divider()
    st.subheader(f"📺 {st.session_state.play_title}")

    url = st.session_state.play_url
    mode = st.session_state.play_mode

    st.info(f"Mod: **{mode.upper()}** | URL: {url[:100]}...")

    if mode == "youtube":
        if "watch?v=" in url:
            vid = url.split("watch?v=")[1].split("&")[0]
        elif "youtu.be/" in url:
            vid = url.split("youtu.be/")[1].split("?")[0]
        else:
            vid = url.split("/")[-1]
        st.components.v1.iframe(f"https://www.youtube.com/embed/{vid}?autoplay=1", height=560)

    elif mode == "iframe":
        st.components.v1.iframe(url, height=560, scrolling=True)

    else:
        # HLS ve diğer streamler için en güçlü player
        player_code = f"""
        <video id="player" controls autoplay style="width:100%; background:#000; max-height:560px;">
            Tarayıcınız video oynatmayı desteklemiyor.
        </video>
        <script src="https://cdn.jsdelivr.net/npm/hls.js@latest"></script>
        <script>
            var video = document.getElementById('player');
            var url = "{url}";
            if (Hls.isSupported()) {{
                var hls = new Hls();
                hls.loadSource(url);
                hls.attachMedia(video);
                hls.on(Hls.Events.MANIFEST_PARSED, function() {{ video.play(); }});
            }} else if (video.canPlayType('application/vnd.apple.mpegurl')) {{
                video.src = url;
                video.addEventListener('loadedmetadata', function() {{ video.play(); }});
            }} else {{
                video.src = url;
                video.play();
            }}
        </script>
        """
        st.components.v1.html(player_code, height=600)

    # Kontrol butonları
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🔄 Başka Kaynak Dene"):
            for key in list(st.session_state.keys()):
                if key.startswith('play_'):
                    del st.session_state[key]
            st.rerun()
    with col2:
        if st.button("🗑️ Player'ı Kapat"):
            for key in list(st.session_state.keys()):
                if key.startswith('play_'):
                    del st.session_state[key]
            st.rerun()

st.caption(f"🕒 {datetime.now().strftime('%H:%M:%S')} | K-QUANTUM RADAR")
