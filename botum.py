import streamlit as st
from groq import Groq
import re

# --- 1. SİSTEM AYARLARI ---
st.set_page_config(
    page_title="Aşk-ı Muhabbet | Pro Lady v28.2",
    layout="wide",
    page_icon="🌸"
)

# Multi-Profesyonel Arayüz ve Sesli Komut JS
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;900&family=Sofia&family=Dancing+Script&family=Nabla&display=swap');
    
    .stApp { background-color: #050005; color: #ffe6f2; }
    
    /* Profesyonel Ses Butonu */
    .mic-container { text-align: center; margin: 25px 0; }
    .mic-btn-pro {
        background: linear-gradient(135deg, #ff007f 0%, #800040 100%);
        color: white; border: none; padding: 22px 45px;
        border-radius: 50px; font-weight: bold; cursor: pointer;
        font-family: 'Orbitron', sans-serif;
        box-shadow: 0 0 30px rgba(255, 0, 127, 0.4);
        font-size: 1.2rem; transition: 0.4s;
    }
    .mic-btn-pro:hover { box-shadow: 0 0 50px #ff007f; transform: translateY(-3px); }
    .listening { animation: pulse-pink 1.2s infinite; background: #ff3399 !important; }
    
    @keyframes pulse-pink {
        0% { box-shadow: 0 0 0 0 rgba(255, 51, 153, 0.7); }
        70% { box-shadow: 0 0 0 20px rgba(255, 51, 153, 0); }
        100% { box-shadow: 0 0 0 0 rgba(255, 51, 153, 0); }
    }

    /* Beyaz Canvas Reji */
    iframe { background-color: #FFFFFF !important; border-radius: 25px; border: 5px solid #ff007f; }
    </style>

    <script>
    function startLadyVoice() {
        const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
        recognition.lang = 'tr-TR';
        const btn = document.getElementById('lady-mic');
        btn.innerHTML = "🔴 SİZİ DİNLİYORUM...";
        btn.classList.add('listening');

        recognition.onresult = function(event) {
            const transcript = event.results[0][0].transcript;
            const textareas = window.parent.document.querySelectorAll('textarea');
            textareas.forEach(t => {
                if(t.placeholder.includes("Tarif")) {
                    t.value = transcript;
                    t.dispatchEvent(new Event('input', { bubbles: true }));
                }
            });
            btn.innerHTML = "🎤 SESLİ KOMUT BAŞARILI";
            btn.classList.remove('listening');
            setTimeout(() => { btn.innerHTML = "🎤 SESLİ KOMUT VER (PRO)"; }, 2000);
        };
        
        recognition.onerror = () => {
            btn.innerHTML = "⚠️ TEKRAR DENEYİN";
            btn.classList.remove('listening');
        };
        recognition.start();
    }
    </script>
    """, unsafe_allow_html=True)

# --- 2. API KONFİGÜRASYONU ---
if "GROQ_API_KEY" in st.secrets:
    api_key = st.secrets["GROQ_API_KEY"]
else:
    with st.sidebar:
        api_key = st.text_input("Groq Cloud Key:", type="password")

if not api_key:
    st.info("Lütfen API Key girerek yayını başlatın.")
    st.stop()

client = Groq(api_key=api_key)

# --- 3. REJİ PANELİ ---
st.markdown("<h1 style='text-align: center; font-family: Sofia; color: #ff007f; font-size: 3rem;'>Aşk-ı Muhabbet <span style='color:#ffffff; font-family:Orbitron; font-size: 1.5rem;'>PRO LADY</span></h1>", unsafe_allow_html=True)

st.markdown('<div class="mic-container"><button id="lady-mic" class="mic-btn-pro" onclick="startLadyVoice()">🎤 SESLİ KOMUT VER (PRO)</button></div>', unsafe_allow_html=True)

with st.form("lady_pro_form"):
    c1, c2 = st.columns([1, 1])
    with c1:
        nick = st.text_input("Bayan Nick:", value="Papatya")
    with c2:
        font = st.selectbox("Zarif Fontlar:", ["Sofia", "Dancing Script", "Nabla", "Bungee Spice", "Righteous"])

    user_desc = st.text_area("Tasarım Tarifi (Sesli veya Manuel):", placeholder="Örn: Pembe yanan, Ken5 gibi parıltılı, Sofia fontunda zarif bir nick...", height=120)
    
    submit = st.form_submit_button("⚡ MULTI-PROFESYONEL RENDER")

# --- 4. OMEGA ENGINE RENDER ---
if submit:
    with st.spinner("Lady Pro motoru arşivdeki en zarif efektleri işliyor..."):
        # Bayan profil olduğu için sistem promptunu özelleştiriyoruz
        lady_prompt = f"""
        Sen profesyonel bir CSS tasarımcısısın. Bir BAYAN kullanıcı için tasarım yapıyorsun.
        - Arşiv: Ken1-Ken8, Colors, Nostalji dosyalarındaki en şık efektleri kullan.
        - Stil: Pembe tonları (#ff007f, #ff79fc), beyaz parıltılar, yumuşak geçişler (blur/glow).
        - Zorunlu: Zemin BEYAZ (#FFFFFF).
        - Metin: '{nick}', Font: {font}.
        Sadece HTML/CSS kodu ver. Açıklama yapma. Bytes hatası almamak için metni düzgün döndür.
        """

        try:
            res = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {"role": "system", "content": lady_prompt},
                    {"role": "user", "content": user_desc}
                ]
            )
            
            # bytes to string koruması
            raw_code = str(res.choices[0].message.content)
            clean_code = re.sub(r"```(html|css)?", "", raw_code).replace("```", "").strip()

            st.divider()
            p_col, s_col = st.columns([1.6, 1])
            
            with p_col:
                st.subheader("🖼️ Pro Lady Preview")
                f_link = font.replace(" ", "+")
                full_html = f"""
                <link href="https://fonts.googleapis.com/css2?family={f_link}&family=Sofia&family=Dancing+Script&display=swap" rel="stylesheet">
                <style>
                    body {{ 
                        margin: 0; background: #FFFFFF; 
                        display: flex; justify-content: center; align-items: center; 
                        height: 100vh; overflow: hidden; 
                    }}
                </style>
                {clean_code}
                """
                st.components.v1.html(full_html, height=550)
            
            with s_col:
                st.subheader("📄 Tasarım Kodları")
                st.code(clean_code, language="html")
                st.download_button("Kodları İndir", clean_code, file_name=f"lady_{nick}.html")

        except Exception as e:
            st.error(f"Reji Hatası: {str(e)}")
