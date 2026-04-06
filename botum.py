import streamlit as st
from groq import Groq
import edge_tts
import asyncio
import base64
from datetime import datetime

# --- 1. GLOBAL KONFİGÜRASYON & API ---
st.set_page_config(page_title="OKEYSIN GLOBAL HUB V16", layout="wide", page_icon="🎙️")

if "GROQ_API_KEY" not in st.secrets:
    st.error("⚠️ API KEY eksik! Streamlit Secrets alanına ekleyin.")
    st.stop()

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

# --- 2. PROFESYONEL QUANTUM UI (GÖRSEL TEMA) ---
st.markdown("""
    <style>
    /* Ana Tema */
    .stApp { 
        background: radial-gradient(circle at top right, #0a0a2e, #050505); 
        color: #e0e0e0; font-family: 'Inter', sans-serif;
    }
    /* Yayın Kartları */
    .broadcast-card {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(0, 242, 255, 0.2);
        border-radius: 20px;
        padding: 25px;
        margin-bottom: 20px;
        backdrop-filter: blur(10px);
        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
    }
    .okeysin-label { color: #00f2ff; font-weight: 800; text-transform: uppercase; letter-spacing: 2px; font-size: 0.9rem; }
    .kerem-label { color: #ffaa00; font-weight: 800; text-transform: uppercase; letter-spacing: 2px; font-size: 0.9rem; }
    /* Araçlar Bölümü */
    .tool-section { background: rgba(0,0,0,0.4); border-radius: 10px; padding: 15px; margin-top: 15px; border: 1px solid #333; }
    .stButton button { width: 100%; border-radius: 8px; border: 1px solid #00f2ff44; transition: 0.3s; }
    .stButton button:hover { background: #00f2ff22; border-color: #00f2ff; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SES MOTORU (PROFESYONEL) ---
async def generate_broadcast_audio(text, char):
    voice = "tr-TR-EmelNeural" if char == "Okeysin" else "tr-TR-AhmetNeural"
    try:
        communicate = edge_tts.Communicate(text, voice)
        audio_data = b""
        async for chunk in communicate.stream():
            if chunk["type"] == "audio":
                audio_data += chunk["data"]
        return audio_data
    except:
        return None

# --- 4. AKILLI HAFIZA SİSTEMİ ---
if "global_history" not in st.session_state:
    st.session_state.global_history = []

# --- 5. ANA PANEL (DASHBOARD) ---
st.title("🎙️ OKEYSIN GLOBAL CONTENT HUB")
st.markdown("#### *Bursa'dan Havalanan, Dünyayı Kucaklayan Dijital Frekans*")

# Yayın Akışını Göster
for i, entry in enumerate(st.session_state.global_history):
    char_class = "okeysin-label" if "Okeysin" in entry["char"] else "kerem-label"
    
    with st.container():
        st.markdown(f"""
            <div class="broadcast-card">
                <div class="{char_class}">{entry['char']}</div>
                <div style="margin-top:10px; line-height:1.6; font-size:1.1rem;">{entry['content']}</div>
            </div>
        """, unsafe_allow_html=True)
        
        # ARAÇLAR PANELI (Her anonsun altında)
        with st.expander("🛠️ YAYIN ARAÇLARI (Kopyala / İndir / Dinle)"):
            c1, c2, c3 = st.columns([2, 2, 4])
            with c1:
                if "audio" in entry:
                    st.audio(entry["audio"], format="audio/mp3")
            with c2:
                st.download_button("📥 Kaydı İndir (.txt)", entry["content"], file_name=f"broadcast_{i}.txt", key=f"dl_{i}")
            with c3:
                st.text_area("📋 Kopyalama Alanı", value=entry["content"], height=80, key=f"cp_{i}", label_visibility="collapsed")

# --- 6. YAYIN KOMUT MERKEZİ ---
if prompt := st.chat_input("Yönetmenim, küresel gündemi veya konuyu buraya yazın..."):
    # Yönetmen mesajını kaydet
    st.session_state.global_history.append({"char": "YÖNETMEN", "content": prompt, "role": "user"})
    
    # DEVASA GENEL KÜLTÜR TALİMATI (SYSTEM PROMPT)
    sys_prompt = """
    Sen dünyanın en bilgili radyo profesyonelisin. Karakterlerin:
    1. OKEYSİN: Bursa'dan dünyaya seslenen; edebiyat, tarih, sanat, dünya şairleri ve global müzik konusunda derin bilgiye sahip, zarif ve entelektüel bir kadın programcı.
    2. KEREM: Sosyal medya trendleri, dünya gazeteleri, teknoloji ve global sohbetleri takip eden, Okeysin ile felsefi tartışmalara girebilen esprili reji uzmanı.
    
    İki karakter birbirleriyle konuşmalı, birbirlerine atıfta bulunmalı ve yönetmenin konusunu dünya genel kültürü süzgecinden geçirerek profesyonel bir podcast akışı oluşturmalı.
    FORMAT: [OKEYSIN] ... [KEREM] ... şeklinde yanıtla.
    """

    with st.spinner("Küresel veriler taranıyor ve yayın hazırlanıyor..."):
        try:
            # Groq üzerinden hafızayı kullanarak cevap al
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[{"role": "system", "content": sys_prompt}] + 
                         [{"role": m["role"], "content": m["content"]} for m in st.session_state.global_history]
            ).choices[0].message.content

            if "[OKEYSIN]" in response and "[KEREM]" in response:
                o_text = response.split("[OKEYSIN]")[1].split("[KEREM]")[0].strip()
                k_text = response.split("[KEREM]")[1].strip()

                # Sesleri Üret
                audio_o = asyncio.run(generate_broadcast_audio(o_text, "Okeysin"))
                audio_k = asyncio.run(generate_broadcast_audio(k_text, "Kerem"))

                # Hafızaya Kaydet (Karakter bazlı)
                st.session_state.global_history.append({"char": "🎙️ OKEYSİN (Global Host)", "content": o_text, "role": "assistant", "audio": audio_o})
                st.session_state.global_history.append({"char": "🎧 KEREM (Reji & Tech)", "content": k_text, "role": "assistant", "audio": audio_k})
                
                st.rerun()
        except Exception as e:
            st.error(f"📡 Yayın Kesintisi: {str(e)}")

# --- 7. SIDEBAR (İSTATİSTİK & ARŞİV) ---
with st.sidebar:
    st.markdown("### 🌐 GLOBAL İSTASYON")
    st.write(f"📅 **Yayın Tarihi:** {datetime.now().strftime('%d.%m.%Y')}")
    st.write("🌍 **Kapsam:** Dünya Geneli / Global Culture")
    st.divider()
    if st.button("🗑️ Tüm Arşivi Temizle"):
        st.session_state.global_history = []
        st.rerun()
    st.info("💡 Not: Her yeni konuşmada geçmişiniz hatırlanır ve üzerine inşa edilir.")
