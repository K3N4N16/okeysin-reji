import streamlit as st
from groq import Groq
import edge_tts
import asyncio
from datetime import datetime

# --- 1. SİSTEM VE GÖRSEL AYARLAR ---
st.set_page_config(page_title="OKEYSIN GLOBAL V20", layout="wide", page_icon="📻")

if "GROQ_API_KEY" not in st.secrets:
    st.error("⚠️ API Key Bulunamadı! Lütfen Secrets alanına ekleyin.")
    st.stop()

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

st.markdown("""
    <style>
    .stApp { background: #030308; color: #e0e0e0; }
    .broadcast-container {
        background: linear-gradient(145deg, #0a0a1a, #050505);
        border: 1px solid #00f2ff22;
        border-radius: 25px;
        padding: 35px;
        margin-bottom: 30px;
        box-shadow: 0 15px 50px rgba(0,0,0,0.8);
    }
    .tag-o { color: #00f2ff; font-weight: 800; font-size: 1.1rem; border-bottom: 1px solid #00f2ff33; }
    .tag-k { color: #ffaa00; font-weight: 800; font-size: 1.1rem; border-bottom: 1px solid #ffaa0033; }
    .on-air { color: #ff0000; font-weight: bold; animation: blink 1.5s infinite; }
    @keyframes blink { 50% { opacity: 0; } }
    </style>
    """, unsafe_allow_html=True)

# --- 2. SES ÜRETİMİ ---
async def process_audio(text, char):
    voice = "tr-TR-EmelNeural" if char == "Okeysin" else "tr-TR-AhmetNeural"
    try:
        comm = edge_tts.Communicate(text, voice)
        audio_bytes = b""
        async for chunk in comm.stream():
            if chunk["type"] == "audio":
                audio_bytes += chunk["data"]
        return audio_bytes
    except: return None

# --- 3. GÜVENLİ HAFIZA YÖNETİMİ ---
if "broadcast_archive" not in st.session_state:
    st.session_state.broadcast_archive = []

# --- 4. YAYIN PANELİ ---
st.markdown('### 🎙️ <span class="on-air">● CANLI YAYIN</span> | BURSA GLOBAL RADIO HUB V20', unsafe_allow_html=True)

for i, entry in enumerate(st.session_state.broadcast_archive):
    if entry["role"] == "user":
        st.markdown(f"🎬 **Yönetmen:** *{entry['content']}*")
    else:
        with st.container():
            st.markdown(f"""
                <div class="broadcast-container">
                    <p><span class="tag-o">🎙️ OKEYSİN:</span><br>{entry['o_text']}</p>
                    <p><span class="tag-k">🎧 KEREM:</span><br>{entry['k_text']}</p>
                    <hr style="border-color:#222">
                    <p style="font-size:0.9rem; color:#00f2ff; font-style:italic;">🎵 Playlist: {entry['playlist']}</p>
                </div>
            """, unsafe_allow_html=True)
            
            # TEK PANEL ARAÇ SETİ
            with st.expander("🛠️ YAYIN ARAÇLARI (Ses / Kayıt / Metin)"):
                c1, c2, c3 = st.columns([2, 2, 4])
                full_txt = f"OKEYSIN: {entry['o_text']}\n\nKEREM: {entry['k_text']}\n\nPLAYLIST: {entry['playlist']}"
                with c1:
                    if entry.get("o_audio"): st.audio(entry["o_audio"], format="audio/mp3")
                    if entry.get("k_audio"): st.audio(entry["k_audio"], format="audio/mp3")
                with c2:
                    st.download_button("📥 Kaydı İndir", full_txt, file_name=f"yayin_{i}.txt", key=f"dl_{i}")
                with c3:
                    st.text_area("📋 Kopyala", value=full_txt, height=80, key=f"cp_{i}")

# --- 5. YAYIN KOMUT MERKEZİ ---
if prompt := st.chat_input("Yönetmenim, yayını başlatın veya konuyu değiştirin..."):
    st.session_state.broadcast_archive.append({"role": "user", "content": prompt})
    
    # HATA KORUMALI SİSTEM TALİMATI
    sys_instruction = """
    Sen dünyanın en profesyonel radyo yayıncısısın.
    [OKEYSIN]: Bilge, sanatsever, dünya edebiyatına ve şairlere hakim sunucu.
    [KEREM]: Global manşetleri ve sosyal medyayı takip eden esprili reji.
    
    KURALLAR:
    1. Her zaman [OKEYSIN_START], [KEREM_REPLY], [OKEYSIN_END] ve [PLAYLIST] etiketlerini kullan.
    2. Okeysin konuyu açar, Kerem eklemeler yapar, Okeysin yayını bir soruyla veya playlistle bağlar.
    3. Geçmiş sohbetleri hatırla ve Bursa'dan dünyaya bir entelektüel köprü kur.
    """

    with st.spinner("Uydu bağlantısı kuruluyor..."):
        try:
            res = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[{"role": "system", "content": sys_instruction}] + 
                         [{"role": m["role"], "content": m.get("content", f"O: {m.get('o_text')} K: {m.get('k_text')}")} for m in st.session_state.broadcast_archive]
            ).choices[0].message.content

            # GÜVENLİ PARÇALAMA (ERROR PROTECTION)
            try:
                o_text = res.split("[OKEYSIN_START]")[1].split("[KEREM_REPLY]")[0].strip()
                k_part = res.split("[KEREM_REPLY]")[1].split("[OKEYSIN_END]")[0].strip()
                o_last = res.split("[OKEYSIN_END]")[1].split("[PLAYLIST]")[0].strip()
                playlist = res.split("[PLAYLIST]")[1].strip()
                
                o_full = f"{o_text} {o_last}"
            except:
                # Eğer etiketlerde hata varsa düz metin olarak al
                o_full = "Yayın akışında bir teknik aksaklık oldu ama devam ediyoruz."
                k_part = res
                playlist = "Radyo Klasikleri"

            audio_o = asyncio.run(process_audio(o_full, "Okeysin"))
            audio_k = asyncio.run(process_audio(k_part, "Kerem"))

            st.session_state.broadcast_archive.append({
                "role": "assistant",
                "o_text": o_full,
                "k_text": k_part,
                "playlist": playlist,
                "o_audio": audio_o,
                "k_audio": audio_k
            })
            st.rerun()
            
        except Exception as e:
            st.error(f"📡 Reji Hatası: {e}")

# Sidebar
with st.sidebar:
    st.markdown("### 🎚️ ANA KONTROL")
    if st.button("🗑️ Arşivi Sıfırla"):
        st.session_state.broadcast_archive = []
        st.rerun()
    st.divider()
    st.info("Bursa'dan Dünyaya: Global Kültür Köprüsü")
