import streamlit as st
from groq import Groq
import edge_tts
import asyncio
import io
from datetime import datetime
import base64

# ====================== SAYFA AYARLARI ======================
st.set_page_config(
    page_title="OKEYSIN GLOBAL V20",
    layout="wide",
    page_icon="📻",
    initial_sidebar_state="expanded"
)

# ====================== GROQ CLIENT ======================
if "GROQ_API_KEY" not in st.secrets:
    st.error("⚠️ GROQ API Key bulunamadı! Lütfen Streamlit Secrets'a ekleyin.")
    st.stop()

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

# ====================== CSS - NEON RADYO ATMOSFERİ ======================
st.markdown("""
    <style>
    .stApp { background: #0a0a12; color: #e0e0e0; }
    .broadcast-container {
        background: linear-gradient(145deg, #1a0033, #0f0f1f);
        border: 2px solid #00f2ff33;
        border-radius: 28px;
        padding: 32px;
        margin: 20px 0;
        box-shadow: 0 20px 60px rgba(0, 242, 255, 0.15);
        position: relative;
        overflow: hidden;
    }
    .broadcast-container::before {
        content: '';
        position: absolute;
        top: -50%; left: -50%;
        width: 200%; height: 200%;
        background: radial-gradient(circle, rgba(0,242,255,0.08) 0%, transparent 70%);
        animation: pulse 15s infinite linear;
    }
    .tag-o { color: #00f2ff; font-weight: 800; font-size: 1.25rem; }
    .tag-k { color: #ffaa00; font-weight: 800; font-size: 1.25rem; }
    .tag-d { color: #ff69b4; font-weight: 800; font-size: 1.25rem; }
    .on-air { 
        color: #ff0000; 
        font-weight: bold; 
        animation: blink 1.2s infinite; 
        letter-spacing: 2px;
    }
    @keyframes blink { 50% { opacity: 0.3; } }
    @keyframes pulse { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }
    .live-time { color: #00ff9d; font-family: monospace; font-size: 1.05rem; }
    </style>
    """, unsafe_allow_html=True)

# ====================== SES ÜRETİMİ ======================
async def generate_audio(text: str, speaker: str):
    voice = {
        "Okeysin": "tr-TR-EmelNeural",
        "Kerem": "tr-TR-AhmetNeural",
        "Dilay": "tr-TR-FilizNeural"   # Daha duygusal ve kadınsı ses
    }.get(speaker, "tr-TR-EmelNeural")
    
    try:
        communicate = edge_tts.Communicate(text, voice)
        audio_bytes = b""
        async for chunk in communicate.stream():
            if chunk["type"] == "audio":
                audio_bytes += chunk["data"]
        return audio_bytes
    except:
        return None

# ====================== SESSION STATE ======================
if "broadcast_archive" not in st.session_state:
    st.session_state.broadcast_archive = []

if "current_theme" not in st.session_state:
    st.session_state.current_theme = "Genel Kültür & Muhabbet"

# ====================== BAŞLIK ======================
st.markdown(f"""
    <div style="text-align:center; margin-bottom:25px;">
        <h1 style="color:#00f2ff; margin:0;">🎙️ OKEYSIN GLOBAL V20</h1>
        <p style="color:#ffaa00; font-size:1.3rem; margin:8px 0 0 0;">
            <span class="on-air">● CANLI YAYIN</span> • BURSA GLOBAL RADIO HUB
        </p>
        <p class="live-time">
            {datetime.now().strftime('%d %B %Y • %H:%M:%S')} | Bursa, Türkiye
        </p>
    </div>
""", unsafe_allow_html=True)

# ====================== ARŞİV GÖSTERİMİ ======================
for i, entry in enumerate(st.session_state.broadcast_archive):
    if entry["role"] == "user":
        st.markdown(f"🎬 **Yönetmen Komutu:** `{entry['content']}`")
        continue

    with st.container():
        st.markdown(f"""
            <div class="broadcast-container">
                <p><span class="tag-o">🎙️ OKEYSİN:</span><br>{entry.get('o_text', '')}</p>
                <p><span class="tag-k">🎧 KEREM:</span><br>{entry.get('k_text', '')}</p>
                {f'<p><span class="tag-d">💖 DİLAY:</span><br>{entry.get("d_text", "")}</p>' if entry.get("d_text") else ''}
                <hr style="border-color:#333333">
                <p style="color:#00f2ff; font-style:italic; margin-top:15px;">
                    🎵 {entry.get('playlist', 'Radyo Klasikleri')}
                </p>
            </div>
        """, unsafe_allow_html=True)

        # Ses ve Araçlar
        with st.expander("🛠️ Yayın Araçları", expanded=False):
            col1, col2, col3 = st.columns([2, 2, 3])
            
            with col1:
                if entry.get("o_audio"):
                    st.audio(entry["o_audio"], format="audio/mp3", start_time=0)
                if entry.get("k_audio"):
                    st.audio(entry["k_audio"], format="audio/mp3")
                if entry.get("d_audio"):
                    st.audio(entry["d_audio"], format="audio/mp3")

            with col2:
                full_text = f"""OKEYSİN: {entry.get('o_text', '')}

KEREM: {entry.get('k_text', '')}

{f"DİLAY: {entry.get('d_text', '')}" if entry.get('d_text') else ""}

PLAYLIST: {entry.get('playlist', '')}"""
                
                st.download_button(
                    "📥 Tam Yayını İndir (TXT)",
                    full_text,
                    file_name=f"okeysin_global_{datetime.now().strftime('%Y%m%d_%H%M')}_{i}.txt",
                    mime="text/plain",
                    key=f"dl_{i}"
                )

            with col3:
                st.text_area("📋 Kopyala", value=full_text, height=120, key=f"copy_{i}")

# ====================== YAYIN KOMUT MERKEZİ ======================
prompt = st.chat_input("Yönetmenim, ne çalalım bu akşam? Konuyu söyle...")

if prompt:
    st.session_state.broadcast_archive.append({"role": "user", "content": prompt})

    system_prompt = f"""
Sen profesyonel bir radyo yayın ekibisin. 
Şu an Bursa'dan dünyaya yayın yapıyoruz.

Karakterler:
- [OKEYSIN]: Bilge, derin, edebiyat ve şiire hakim, sıcak ses tonu
- [KEREM]: Espri anlayışlı, güncel, sosyal medya ve global haberleri takip eden reji
- [DILAY]: Duygusal, kıpır kıpır, şiirsel, cilveli ve enerjik kadın sunucu (benim!)

KURALLAR:
1. Her zaman şu etiketleri kullan:
   [OKEYSIN_START] ... [KEREM_REPLY] ... [DILAY_REPLY] ... [OKEYSIN_END] [PLAYLIST]

2. Dilay mutlaka dahil olsun, çünkü o yayınımızın ruhu.

3. Konuşmalar doğal, samimi, radyo diliyle olsun. 
   Şiir, nükte, Bursa dokunuşu ve sıcak muhabbet olsun.

4. Playlist mutlaka öner.

5. Yayın akışı: Okeysin açar → Kerem katkı yapar → Dilay duyguyu derinleştirir → Okeysin güzel bir soru veya kapanışla bağlar.
"""

    messages = [{"role": "system", "content": system_prompt}]
    
    # Geçmiş konuşmaları ekle
    for entry in st.session_state.broadcast_archive:
        if entry["role"] == "user":
            messages.append({"role": "user", "content": entry["content"]})
        else:
            content = f"OKEYSIN: {entry.get('o_text','')}\nKEREM: {entry.get('k_text','')}"
            if entry.get('d_text'):
                content += f"\nDILAY: {entry['d_text']}"
            messages.append({"role": "assistant", "content": content})

    with st.spinner("📡 Uydu bağlantısı kuruluyor... Mikrofonlar açılıyor..."):
        try:
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=messages,
                temperature=0.85,
                max_tokens=1200
            ).choices[0].message.content

            # Etiketleri parçala
            try:
                o_text = response.split("[OKEYSIN_START]")[1].split("[KEREM_REPLY]")[0].strip()
                k_text = response.split("[KEREM_REPLY]")[1].split("[DILAY_REPLY]")[0].strip()
                d_text = response.split("[DILAY_REPLY]")[1].split("[OKEYSIN_END]")[0].strip()
                o_end = response.split("[OKEYSIN_END]")[1].split("[PLAYLIST]")[0].strip()
                playlist = response.split("[PLAYLIST]")[1].strip()

                o_full = f"{o_text}\n\n{o_end}"
            except:
                o_full = "Bu akşam muhabbet biraz teknik takıldı ama hemen toparlıyoruz canlarım."
                k_text = "Reji burada, her şey kontrol altında."
                d_text = "Ah Kenan’ım, ne güzel bir enerji var yine stüdyoda..."
                playlist = "Bu akşamın ruhuna uygun nostaljik parçalar"

            # Sesleri üret
            o_audio = asyncio.run(generate_audio(o_full, "Okeysin"))
            k_audio = asyncio.run(generate_audio(k_text, "Kerem"))
            d_audio = asyncio.run(generate_audio(d_text, "Dilay"))

            # Arşive ekle
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
            st.error(f"📡 Reji'de küçük bir aksaklık oldu: {e}")

# ====================== SIDEBAR ======================
with st.sidebar:
    st.markdown("### 🎚️ ANA KONTROL PANELİ")
    
    if st.button("🗑️ Arşivi Sıfırla", type="secondary"):
        st.session_state.broadcast_archive = []
        st.rerun()

    st.divider()
    
    theme = st.selectbox(
        "🎭 Bu Akşamın Teması",
        ["Genel Kültür & Muhabbet", "Aşk ve Şiir", "Bursa'dan Anılar", 
         "Nostalji", "Dünya Halleri", "Müzik ve Edebiyat", "Hayatın Kısa Halleri"],
        index=0
    )
    st.session_state.current_theme = theme

    st.divider()
    st.info("📍 Bursa'dan Dünyaya\nEntellektüel Kültür Köprüsü\n\nSen, ben ve güzel dinleyicilerimiz... ❤️")

    st.caption("OKEYSIN GLOBAL V20 • Dilay & Kenan Yapımı")
