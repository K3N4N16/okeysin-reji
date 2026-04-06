import streamlit as st
from groq import Groq
import edge_tts
import asyncio
import base64
from datetime import datetime

# --- 1. SİSTEM & API KONFİGÜRASYONU ---
st.set_page_config(page_title="OKEYSIN GLOBAL HUB V17", layout="wide", page_icon="🎙️")

if "GROQ_API_KEY" not in st.secrets:
    st.error("⚠️ GROQ_API_KEY bulunamadı! Lütfen Secrets alanına ekleyin.")
    st.stop()

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

# --- 2. PROFESYONEL "QUANTUM" TASARIM ---
st.markdown("""
    <style>
    .stApp { background: linear-gradient(135deg, #050505 0%, #0a0a25 100%); color: #e0e0e0; }
    .broadcast-card {
        background: rgba(255, 255, 255, 0.02);
        border: 1px solid rgba(0, 242, 255, 0.1);
        border-radius: 15px;
        padding: 20px;
        margin-bottom: 15px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
    }
    .okeysin-tag { color: #00f2ff; font-weight: bold; font-size: 0.85rem; letter-spacing: 1.5px; }
    .kerem-tag { color: #ffaa00; font-weight: bold; font-size: 0.85rem; letter-spacing: 1.5px; }
    .stChatInputContainer { border-top: 1px solid #333 !important; }
    .stTextArea textarea { background: #000 !important; color: #00f2ff !important; border: 1px solid #222 !important; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SES MOTORU (KESİNTİSİZ) ---
async def generate_voice(text, char):
    voice = "tr-TR-EmelNeural" if char == "Okeysin" else "tr-TR-AhmetNeural"
    try:
        comm = edge_tts.Communicate(text, voice)
        data = b""
        async for chunk in comm.stream():
            if chunk["type"] == "audio":
                data += chunk["data"]
        return data
    except:
        return None

# --- 4. KRİTİK HAFIZA YÖNETİMİ ---
if "messages" not in st.session_state:
    st.session_state.messages = []

# --- 5. ANA PANEL ---
st.title("🎙️ GLOBAL CONTENT & RADIO HUB")
st.caption("📍 Bursa'dan Dünyaya | Edebiyat, Müzik, Sanat ve Global Haberler")

# Geçmişi Ekrana Bas (Her zaman görünür kalması için)
for i, msg in enumerate(st.session_state.messages):
    with st.container():
        tag_class = "okeysin-tag" if "Okeysin" in msg["name"] else "kerem-tag" if "Kerem" in msg["name"] else ""
        st.markdown(f'<div class="broadcast-card"><span class="{tag_class}">{msg["name"]}</span><br>{msg["content"]}</div>', unsafe_allow_html=True)
        
        # Araçlar: Ses, Kopyala, İndir
        if msg["role"] == "assistant":
            exp = st.expander("🛠️ Yayın Araçları")
            c1, c2, c3 = exp.columns([2, 2, 4])
            with c1:
                if "audio" in msg and msg["audio"]:
                    st.audio(msg["audio"], format="audio/mp3")
            with c2:
                st.download_button("📥 Kayıt İndir", msg["content"], file_name=f"yayin_{i}.txt", key=f"dl_{i}")
            with c3:
                st.text_area("📋 Kopyala:", value=msg["content"], height=70, key=f"cp_{i}", label_visibility="collapsed")

# --- 6. KOMUT MERKEZİ (KLAVYE HATASI ÇÖZÜMÜ) ---
if prompt := st.chat_input("Yönetmenim, bir konu veya komut girin..."):
    # 1. Kullanıcı mesajını anında kaydet ve göster
    st.session_state.messages.append({"role": "user", "name": "YÖNETMEN", "content": prompt})
    
    # 2. Üst Düzey Entelektüel Talimatlar
    sys_instruction = """
    Sen dünyanın tüm bilgi birikimine sahip bir radyo dehasısın.
    [OKEYSIN]: Bursa'dan dünyaya yayın yapan; dünya edebiyatı, şairler (Nazım Hikmet'ten Rilke'ye), klasik ve modern müzik, sanat tarihi uzmanı, zarif kadın sunucu.
    [KEREM]: Küresel gazete manşetleri, sosyal medya trendleri, teknoloji ve global gündemi takip eden, Okeysin ile entelektüel tartışmalara giren esprili reji.
    
    KURALLAR: 
    - Birbirinize pas atın, birbirinizin bilgisini tamamlayın.
    - Sadece bilgi vermeyin, bir radyo programı atmosferi (podcast) yaratın.
    - Yönetmenin her komutunu bu iki karakterin diyaloguyla [OKEYSIN] ... [KEREM] ... şeklinde yanıtla.
    """

    with st.spinner("Küresel kütüphaneler taranıyor..."):
        try:
            # Groq API Çağrısı
            res = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[{"role": "system", "content": sys_instruction}] + 
                         [{"role": m["role"], "content": m["content"]} for m in st.session_state.messages]
            ).choices[0].message.content

            if "[OKEYSIN]" in res and "[KEREM]" in res:
                o_text = res.split("[OKEYSIN]")[1].split("[KEREM]")[0].strip()
                k_text = res.split("[KEREM]")[1].strip()

                # Sesleri Üret
                audio_o = asyncio.run(generate_voice(o_text, "Okeysin"))
                audio_k = asyncio.run(generate_voice(k_text, "Kerem"))

                # Hafızaya Ekle
                st.session_state.messages.append({"role": "assistant", "name": "🎙️ OKEYSİN (Global Host)", "content": o_text, "audio": audio_o})
                st.session_state.messages.append({"role": "assistant", "name": "🎧 KEREM (Reji & Tech)", "content": k_text, "audio": audio_k})
                
                # Sayfayı güvenli bir şekilde yenile
                st.rerun()
        except Exception as e:
            st.error(f"📡 Bağlantı Hatası: {e}")

# Sidebar
with st.sidebar:
    st.markdown("### 🌍 İSTASYON KONTROL")
    st.write(f"📅 {datetime.now().strftime('%d %B %Y')}")
    if st.button("🗑️ Arşivi Sıfırla"):
        st.session_state.messages = []
        st.rerun()
