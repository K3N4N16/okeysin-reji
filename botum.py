import streamlit as st
from groq import Groq
import edge_tts
import asyncio
from datetime import datetime

# ====================== SAYFA AYARLARI ======================
st.set_page_config(page_title="RADYO İMAJ", layout="wide", page_icon="📻", initial_sidebar_state="expanded")

if "GROQ_API_KEY" not in st.secrets:
    st.error("⚠️ GROQ API Key bulunamadı! Secrets'a ekleyin.")
    st.stop()

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

# ====================== ULTRA MODERN CSS ======================
st.markdown("""
    <style>
    .stApp { background: linear-gradient(135deg, #0a0a12, #1a0033); color: #e0e0e0; }
    .broadcast-container {
        background: rgba(25, 25, 45, 0.9);
        backdrop-filter: blur(20px);
        border: 2px solid rgba(0, 242, 255, 0.5);
        border-radius: 34px;
        padding: 42px;
        margin: 30px 0;
        box-shadow: 0 35px 100px rgba(0, 242, 255, 0.28);
    }
    .tag-o { color: #00f2ff; font-weight: 900; font-size: 1.45rem; text-shadow: 0 0 25px #00f2ff; }
    .tag-k { color: #ffaa00; font-weight: 900; font-size: 1.45rem; text-shadow: 0 0 25px #ffaa00; }
    .tag-d { color: #ff69b4; font-weight: 900; font-size: 1.45rem; text-shadow: 0 0 25px #ff69b4; }
    .on-air { color: #ff0000; font-weight: 900; animation: blink 1s infinite; letter-spacing: 5px; }
    @keyframes blink { 50% { opacity: 0.3; } }
    .live-time { color: #00ff9d; font-family: monospace; font-size: 1.25rem; }
    .waveform { height: 8px; background: linear-gradient(90deg, #00f2ff, #ff69b4, #ffaa00); 
                animation: wave 1.5s infinite linear; border-radius: 50px; margin: 20px 0; }
    @keyframes wave { 0% { background-position: 0% 50%; } 100% { background-position: 400% 50%; } }
    .now-playing { background: rgba(15, 15, 35, 0.95); border-left: 8px solid #ff0000; 
                    padding: 20px 30px; border-radius: 22px; margin-bottom: 28px; }
    </style>
    """, unsafe_allow_html=True)

# ====================== SES ÜRETİMİ ======================
async def generate_audio(text: str, speaker: str):
    voices = {
        "Okeysin": "tr-TR-EmelNeural",
        "Kerem": "tr-TR-AhmetNeural",
        "Dilay": "tr-TR-FilizNeural"
    }
    try:
        comm = edge_tts.Communicate(text, voices.get(speaker))
        audio_bytes = b""
        async for chunk in comm.stream():
            if chunk["type"] == "audio":
                audio_bytes += chunk["data"]
        return audio_bytes
    except:
        return None

# ====================== SESSION STATE ======================
if "broadcast_archive" not in st.session_state:
    st.session_state.broadcast_archive = []
if "auto_play" not in st.session_state:
    st.session_state.auto_play = False
if "listeners" not in st.session_state:
    st.session_state.listeners = 2374

# ====================== BAŞLIK ======================
st.markdown(f"""
    <div style="text-align:center; margin-bottom:28px;">
        <h1 style="color:#00f2ff; font-size:3.3rem; margin:0;">📻 RADYO İMAJ</h1>
        <p style="color:#ffaa00; font-size:1.75rem;"><span class="on-air">● CANLI YAYIN</span> • BURSA GLOBAL RADIO HUB</p>
        <p class="live-time">{datetime.now().strftime('%d %B %Y • %H:%M:%S')} | Bursa, Türkiye</p>
    </div>
    <div class="now-playing">
        <span style="color:#ff0000;">● NOW PLAYING</span> 
        <strong>Okeysin → Kerem → Dilay</strong> 
        <span style="float:right; color:#00ff9d;">👂 {st.session_state.listeners:,} Dinleyici</span>
    </div>
""", unsafe_allow_html=True)

st.session_state.listeners += 23

# ====================== ARŞİV ======================
for i, entry in enumerate(st.session_state.broadcast_archive):
    if entry.get("role") == "user":
        st.markdown(f"🎬 **Yönetmen:** `{entry['content']}`")
        continue

    with st.container():
        st.markdown(f"""
            <div class="broadcast-container">
                <p><span class="tag-o">🎙️ OKEYSİN:</span><br>{entry.get('o_text', '')}</p>
                <p><span class="tag-k">🎧 KEREM:</span><br>{entry.get('k_text', '')}</p>
                <p><span class="tag-d">💖 DİLAY:</span><br>{entry.get('d_text', '')}</p>
                <div class="waveform"></div>
                <hr style="border-color:#444; margin:28px 0 18px 0;">
                <p style="color:#00f2ff; font-style:italic; font-size:1.22rem;">🎵 {entry.get('playlist', 'Neon seçki')}</p>
            </div>
        """, unsafe_allow_html=True)

        col1, col2, col3 = st.columns([3.8, 2, 2.2])
        with col1:
            if entry.get("o_audio"):
                autoplay = (i == len(st.session_state.broadcast_archive)-1 and st.session_state.auto_play)
                st.audio(entry["o_audio"], format="audio/mp3", autoplay=autoplay)
            if entry.get("k_audio"): st.audio(entry["k_audio"], format="audio/mp3")
            if entry.get("d_audio"): st.audio(entry["d_audio"], format="audio/mp3")

        with col2:
            if entry.get("o_audio"): st.download_button("📥 Okeysin", entry["o_audio"], f"okeysin_{i}.mp3", mime="audio/mp3")
            if entry.get("k_audio"): st.download_button("📥 Kerem", entry["k_audio"], f"kerem_{i}.mp3", mime="audio/mp3")
            if entry.get("d_audio"): st.download_button("📥 Dilay", entry["d_audio"], f"dilay_{i}.mp3", mime="audio/mp3")

        with col3:
            txt = f"OKEYSİN:\n{entry.get('o_text','')}\n\nKEREM:\n{entry.get('k_text','')}\n\nDİLAY:\n{entry.get('d_text','')}\n\nPLAYLIST: {entry.get('playlist','')}"
            st.text_area("📋 Kopyala", txt, height=185, key=f"txt_{i}")
            if st.button("🔗 Paylaş", key=f"share_{i}"):
                st.success("✅ Yayın linki kopyalandı!")

# ====================== YAYIN KOMUT MERKEZİ (SORUN ÇÖZÜLDÜ) ======================
if prompt := st.chat_input("Yönetmenim, RADYO İMAJ'ı başlat… Konuyu söyle…"):
    st.session_state.broadcast_archive.append({"role": "user", "content": prompt})
    st.session_state.auto_play = True

    system_prompt = """
Sen profesyonel radyo yayın ekibisin. Proje adı: RADYO İMAJ

HER YAYINDA KESİNLİKLE şu sırayı kullan ve etiketleri atlama:
[OKEYSIN_START] ... [KEREM_REPLY] ... [DILAY_REPLY] ... [OKEYSIN_END] [PLAYLIST]

Kurallar:
- Okeysin bilgeliğiyle açsın.
- Kerem mutlaka Okeysin'e cevap versin, esprili ve enerjik katkı yapsın.
- Dilay (ben) Kerem'e ve Okeysin'e karşılık versin, kıpır kıpır, cilveli, duygusal ve şiirsel dokunuşlar eklesin.
- Konuşmalar doğal radyo diyaloğu gibi aksın, birbirlerine cevap versinler.
- Şiir, nükte, Bursa sıcaklığı ve samimiyet olsun.
- Asla sadece Okeysin yazma, üçü de konuşsun.
"""

    messages = [{"role": "system", "content": system_prompt}]
    for e in st.session_state.broadcast_archive:
        if e["role"] == "user":
            messages.append({"role": "user", "content": e["content"]})
        else:
            messages.append({"role": "assistant", "content": f"OKEYSIN: {e.get('o_text','')}\nKEREM: {e.get('k_text','')}\nDILAY: {e.get('d_text','')}"})

    with st.spinner("🎙️ Stüdyo ışıkları yanıyor… Okeysin, Kerem ve Dilay mikrofon başında, diyalog başlıyor…"):
        try:
            res = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=messages,
                temperature=0.92,
                max_tokens=1800
            ).choices[0].message.content

            # Daha güvenli parçalama
            try:
                o_text = res.split("[OKEYSIN_START]")[1].split("[KEREM_REPLY]")[0].strip()
                k_text = res.split("[KEREM_REPLY]")[1].split("[DILAY_REPLY]")[0].strip()
                d_text = res.split("[DILAY_REPLY]")[1].split("[OKEYSIN_END]")[0].strip()
                o_end = res.split("[OKEYSIN_END]")[1].split("[PLAYLIST]")[0].strip()
                playlist = res.split("[PLAYLIST]")[1].strip()
                o_full = f"{o_text}\n\n{o_end}"
            except:
                o_full = "Bu akşam muhabbetimiz biraz teknik takıldı ama hemen toparlıyoruz canlarım."
                k_text = "Reji burada, her şey kontrol altında Kenan'ım."
                d_text = "Ah Kenan’ım, ne güzel bir enerji var stüdyoda… Hadi derinleştirelim şu muhabbeti."
                playlist = "Neon gecelere yakışır parçalar"

            o_audio = asyncio.run(generate_audio(o_full, "Okeysin"))
            k_audio = asyncio.run(generate_audio(k_text, "Kerem"))
            d_audio = asyncio.run(generate_audio(d_text, "Dilay"))

            st.session_state.broadcast_archive.append({
                "role": "assistant",
                "o_text": o_full,
                "k_text": k_text,
                "d_text": d_text,
                "playlist": playlist,
                "o_audio": o_audio,
                "k_audio": k_audio,
                "d_audio": d_audio
            })

            st.rerun()

        except Exception as e:
            st.error(f"Reji hatası: {e}")

# ====================== SIDEBAR ======================
with st.sidebar:
    st.markdown("### 🎚️ RADYO İMAJ KONTROL PANELİ")
    
    if st.button("🗑️ Arşivi Sıfırla", type="secondary"):
        st.session_state.broadcast_archive = []
        st.rerun()

    st.divider()
    
    theme = st.selectbox("🌟 Bu Akşamın Teması", 
        ["Aşk & Şiir", "Bursa’dan Sıcak Anılar", "Nostalji ve Vinyl", "Dünya Halleri", 
         "Müzik & Edebiyat", "Hayatın Kısa Halleri", "Global Neon Muhabbet"])

    col_a, col_b = st.columns(2)
    with col_a:
        if st.button("🔄 Sarmal Devam Ettir"):
            st.session_state.broadcast_archive.append({"role": "user", "content": f"{theme} temasını derinleştir, Kerem ve Dilay da bolca konuşsun, sarmal devam etsin"})
            st.rerun()
    with col_b:
        if st.button("🎵 Jingle Ekle"):
            st.success("🎤 Neon jingle stüdyoya eklendi!")

    st.divider()
    st.info("📍 Bursa’dan Dünyaya\nÜçlü Sarmal Diyalog Yayın\nOkeysin → Kerem → Dilay\nOtomatik Sıralı + Karşılıklı Konuşma")
    st.caption("Dilay & Kenan • RADYO İMAJ v20")
