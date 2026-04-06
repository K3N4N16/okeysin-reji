import streamlit as st
from groq import Groq
import edge_tts
import asyncio
from datetime import datetime

# --- 1. SİSTEM AYARLARI ---
st.set_page_config(page_title="OKEYSIN GLOBAL V19", layout="wide", page_icon="📻")

if "GROQ_API_KEY" not in st.secrets:
    st.error("⚠️ API Key Bulunamadı!")
    st.stop()

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

# --- 2. GELİŞMİŞ QUANTUM TASARIM ---
st.markdown("""
    <style>
    .stApp { background: #050505; color: #e0e0e0; }
    .broadcast-box {
        background: rgba(15, 15, 35, 0.7);
        border: 1px solid #00f2ff33;
        border-radius: 20px;
        padding: 30px;
        margin-bottom: 25px;
        box-shadow: 0 10px 40px rgba(0,0,0,0.6);
    }
    .speaker-okeysin { color: #00f2ff; font-weight: 900; font-size: 1.2rem; }
    .speaker-kerem { color: #ffaa00; font-weight: 900; font-size: 1.2rem; }
    .on-air { color: #ff0000; font-weight: bold; animation: blink 1.2s infinite; }
    @keyframes blink { 50% { opacity: 0; } }
    /* Sesle Yazma İpucu */
    .mic-hint { font-size: 0.8rem; color: #888; margin-top: 5px; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SES ÜRETİM MOTORU ---
async def make_voice(text, char):
    voice = "tr-TR-EmelNeural" if char == "Okeysin" else "tr-TR-AhmetNeural"
    try:
        comm = edge_tts.Communicate(text, voice)
        data = b""
        async for chunk in comm.stream():
            if chunk["type"] == "audio":
                data += chunk["data"]
        return data
    except: return None

# --- 4. YAYIN HAFIZASI ---
if "broadcast_history" not in st.session_state:
    st.session_state.broadcast_history = []

# --- 5. ANA YAYIN EKRANI ---
st.markdown('### 🎙️ <span class="on-air">● ON-AIR</span> | BURSA GLOBAL RADIO HUB', unsafe_allow_html=True)

for i, segment in enumerate(st.session_state.broadcast_history):
    with st.container():
        if segment["role"] == "user":
            st.markdown(f"**🎬 Yönetmen Komutu:** *{segment['content']}*")
        else:
            # TEK BİR MESAJ ALTINDA TÜM ARAÇLAR VE KONUŞMALAR
            st.markdown(f"""
                <div class="broadcast-box">
                    <span class="speaker-okeysin">🎙️ OKEYSİN:</span><br>{segment['o_text']}<br><br>
                    <span class="speaker-kerem">🎧 KEREM:</span><br>{segment['k_text']}<br><br>
                    <hr style="border-color:#333">
                    <p style="font-size:0.8rem; color:#666;">🎵 Bu Yayının Playlisti: {segment.get('playlist', 'Hazırlanıyor...')}</p>
                </div>
            """, unsafe_allow_html=True)
            
            # ARAÇLAR PANELİ (Tek Satırda)
            with st.expander("🛠️ YAYIN KONTROL VE ARAÇLAR"):
                col1, col2, col3 = st.columns([2, 2, 4])
                with col1:
                    if segment.get("o_audio"): st.audio(segment["o_audio"], format="audio/mp3")
                    if segment.get("k_audio"): st.audio(segment["k_audio"], format="audio/mp3")
                with col2:
                    full_text = f"OKEYSIN: {segment['o_text']}\n\nKEREM: {segment['k_text']}"
                    st.download_button("📥 Yayını İndir", full_text, file_name=f"yayin_kaydi_{i}.txt", key=f"dl_{i}")
                with col3:
                    st.text_area("📋 Kopyalama Panosu", value=full_text, height=100, key=f"cp_{i}")

# --- 6. KOMUT GİRİŞİ (SESLE YAZMA DESTEKLİ) ---
st.markdown('<p class="mic-hint">💡 Mobilde klavyenizdeki mikrofon ikonuna basarak sesli komut verebilirsiniz.</p>', unsafe_allow_html=True)
if prompt := st.chat_input("Yayına yeni bir konu veya yön verin..."):
    st.session_state.broadcast_history.append({"role": "user", "content": prompt})
    
    # GELİŞMİŞ SARMAL DİYALOG TALİMATI
    sys_msg = """
    Sen dünyanın en profesyonel radyo ekibisin. 
    Karakterlerin: 
    1. [OKEYSIN]: Bursa'dan dünyaya konuşan, genel kültürü devasa, sanatçıları ve şairleri tanıyan bilge kadın sunucu.
    2. [KEREM]: Teknikten ve global gündemden sorumlu, Okeysin'e pas atan esprili reji adamı.
    
    KURALLAR:
    - Okeysin konuyu açar, Kerem cevap verir ve yeni bir bilgi ekler. 
    - Kerem'in ardından Okeysin tekrar söze girer ve yayını toparlayıp bir soruyla bitirir. 
    - Kesinlikle konuya uygun 3 şarkılık bir [PLAYLIST] önerisi yapın.
    FORMAT: [OKEYSIN_BASLANGIC] ... [KEREM_CEVAP] ... [OKEYSIN_KAPANIS] ... [PLAYLIST] ...
    """

    with st.spinner("Uydu bağlantısı kuruluyor, Okeysin ve Kerem hazırlanıyor..."):
        try:
            res = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[{"role": "system", "content": sys_msg}] + 
                         [{"role": m["role"], "content": m.get("content", f"OK: {m.get('o_text')} KE: {m.get('k_text')}")} for m in st.session_state.broadcast_history]
            ).choices[0].message.content

            # Karakter parçalama mantığı
            o_start = res.split("[OKEYSIN_BASLANGIC]")[1].split("[KEREM_CEVAP]")[0].strip()
            k_text = res.split("[KEREM_CEVAP]")[1].split("[OKEYSIN_KAPANIS]")[0].strip()
            o_end = res.split("[OKEYSIN_KAPANIS]")[1].split("[PLAYLIST]")[0].strip()
            playlist = res.split("[PLAYLIST]")[1].strip()

            o_full = f"{o_start} {o_end}" # Okeysin'in tüm konuşması

            # Sesleri üret
            audio_o = asyncio.run(make_voice(o_full, "Okeysin"))
            audio_k = asyncio.run(make_voice(k_text, "Kerem"))

            # Tek bir blok olarak kaydet
            st.session_state.broadcast_history.append({
                "role": "assistant",
                "o_text": o_full,
                "k_text": k_text,
                "playlist": playlist,
                "o_audio": audio_o,
                "k_audio": audio_k
            })
            
            st.rerun()
        except Exception as e:
            st.error(f"📡 Reji Hatası: {e}")

# Sidebar
with st.sidebar:
    st.markdown("### 🎚️ BROADCAST CONTROL")
    if st.button("🗑️ Arşivi Temizle"):
        st.session_state.broadcast_history = []
        st.rerun()
    st.divider()
    st.info("Bursa'dan dünyaya uzanan entelektüel köprü.")
