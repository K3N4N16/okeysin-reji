import streamlit as st
from groq import Groq
import json
import os

st.set_page_config(page_title="K-QUANTUM TV", layout="wide", page_icon="📺")

# Groq
GROQ_KEY = os.getenv("GROQ_API_KEY") or st.secrets.get("GROQ_API_KEY")
client = Groq(api_key=GROQ_KEY)

st.title("📺 K-QUANTUM TELEVİZYON")
st.markdown("**Kenan ile Faslı Muhabbet** Rejisi - Radar + Televizyon")

query = st.text_input("Ne izlemek istiyorsun?", placeholder="Beşiktaş maçı, nostaljik türkü, Matrix, canlı kamera...")

if st.button("🌌 RADAR TARASIN", type="primary"):
    if query:
        with st.spinner("Radar taranıyor..."):
            try:
                prompt = f'Kullanıcı "{query}" arıyor. 4 tane kesin çalışan kaynak bul. JSON formatı: {{"intro": "...", "results": [{{"title":"..", "url":"..", "mode":"youtube/hls/iframe", "info":".."}}]}}'

                resp = client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=[{"role": "user", "content": prompt}],
                    response_format={"type": "json_object"}
                )

                data = json.loads(resp.choices[0].message.content)

                st.success(data.get("intro", "Kaynaklar bulundu"))

                for idx, item in enumerate(data.get("results", [])):
                    col1, col2 = st.columns([4,1])
                    with col1:
                        st.write(f"**{item.get('title')}**")
                        st.caption(f"{item.get('mode','hls').upper()} - {item.get('info','')}")
                    with col2:
                        if st.button("📺 OYNAT", key=f"btn_{idx}"):
                            st.session_state.tv_url = item.get('url')
                            st.session_state.tv_mode = item.get('mode', 'hls').lower()
                            st.session_state.tv_title = item.get('title')
                            st.rerun()
            except:
                st.error("Radar şu anda çalışmıyor.")

# ====================== TELEVİZYON EKRANI ======================
if 'tv_url' in st.session_state:
    st.divider()
    st.subheader(f"📺 {st.session_state.tv_title}")

    url = st.session_state.tv_url
    mode = st.session_state.tv_mode

    if mode == "youtube":
        vid = url.split("v=")[-1].split("&")[0] if "v=" in url else url.split("/")[-1]
        st.components.v1.iframe(f"https://www.youtube.com/embed/{vid}?autoplay=1", height=600)
    elif mode == "iframe":
        st.components.v1.iframe(url, height=600, scrolling=True)
    else:
        # HLS ve diğer linkler için
        html_code = f"""
        <video id="tvplayer" controls autoplay style="width:100%; height:600px; background:black;">
            <source src="{url}" type="application/x-mpegURL">
        </video>
        <script src="https://cdn.jsdelivr.net/npm/hls.js@latest"></script>
        <script>
            var video = document.getElementById('tvplayer');
            if (Hls.isSupported()) {{
                var hls = new Hls();
                hls.loadSource('{url}');
                hls.attachMedia(video);
            }} else {{
                video.src = '{url}';
            }}
            video.play();
        </script>
        """
        st.components.v1.html(html_code, height=650)

    if st.button("🗑️ Televizyonu Kapat"):
        for key in ['tv_url', 'tv_mode', 'tv_title']:
            if key in st.session_state:
                del st.session_state[key]
        st.rerun()

st.caption("K-QUANTUM TELEVİZYON • Kenan ile Faslı Muhabbet")
