import streamlit as st
from groq import Groq
import json
import os
import asyncio
import requests
from datetime import datetime
from rvc_python.infer import RVCInference

# --- 1. RVC & HUGGING FACE AYARLARI ---
PTH_URL = "https://huggingface.co/matroks/dilay/resolve/main/my-project_60e_660s.pth"
INDEX_URL = "https://huggingface.co/matroks/dilay/resolve/main/my-project.index"
PTH_FILE = "dilay_model.pth"
INDEX_FILE = "dilay_model.index"

# Modelleri Hugging Face'den İndirme Fonksiyonu
def download_models():
    for url, path in [(PTH_URL, PTH_FILE), (INDEX_URL, INDEX_FILE)]:
        if not os.path.exists(path):
            with st.spinner(f"🚀 Dilay'ın sesi hazırlanıyor ({path})..."):
                r = requests.get(url, stream=True)
                with open(path, "wb") as f:
                    for chunk in r.iter_content(chunk_size=8192):
                        f.write(chunk)

# --- 2. TASARIM VE TEMİZLİK ---
st.set_page_config(page_title="OMEGA v40 AI - DİLAY", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #020205; color: #00f2ff; }
    [data-testid="stSidebar"] { background-color: #080810; border-right: 2px solid #ff007f; }
    .chat-card {
        background: rgba(10, 10, 20, 0.92); 
        border: 1px solid #ff007f;
        border-radius: 18px; 
        padding: 22px; 
        margin-bottom: 25px;
        box-shadow: 0 4px 15px rgba(255, 0, 127, 0.15);
    }
    .assistant-text { 
        color: #ffffff; 
        border-left: 5px solid #ff007f; 
        padding-left: 18px;
        font-size: 1.05rem;
        line-height: 1.7;
    }
    </style>
""", unsafe_allow_html=True)

# --- 3. RVC SES MOTORU (Dilay'ın Gerçek Sesi) ---
async def process_rvc_voice(text):
    import edge_tts
    # A. Metni Robot Kadın Sesine Çevir (Taslak Ses)
    temp_base = "temp_robot.mp3"
    communicate = edge_tts.Communicate(text, "tr-TR-EmelNeural")
    await communicate.save(temp_base)
    
    # B. RVC ile Dilay'ın Sesine Dönüştür
    output_audio = "dilay_final.wav"
    rvc = RVCInference(device="cpu") # Sunucuda CPU kullanılır
    rvc.set_model(PTH_FILE)
    # Dilay kadın sesi olduğu için pitch (f0_up_key) ayarını 0 veya 12 yapabilirsin
    rvc.infer(temp_base, index_path=INDEX_FILE, out_path=output_audio, f0_up_key=0)
    return output_audio

# --- 4. VERİ YÖNETİMİ ---
DB_FILE = "omega_v40_data.json"
def load_db(): 
    return json.load(open(DB_FILE, "r", encoding="utf-8")) if os.path.exists(DB_FILE) else {}
def save_db(db): 
    json.dump(db, open(DB_FILE, "w", encoding="utf-8"), ensure_ascii=False, indent=4)

if "db" not in st.session_state: 
    st.session_state.db = load_db()
if "active_id" not in st.session_state: 
    st.session_state.active_id = "Canlı Yayın - Dilay & Kenan"

# Modelleri Başlangıçta Hazırla
download_models()

# --- 5. REJİ SIDEBAR ---
with st.sidebar:
    st.title("🎙️ OMEGA v40 - REJİ")
    persona = st.selectbox("Yayıncı Seç", ["🔥 Dilay", "🎙️ Can", "💼 Uygula"])
    st.divider()
    up_file = st.file_uploader("📁 Eğitim Dosyası Yükle", type=['txt'])
    training_data = up_file.read().decode("utf-8") if up_file else ""

    if st.button("🌟 Yeni Yayın Başlat"):
        cid = f"{persona} | {datetime.now().strftime('%d.%m.%Y %H:%M')}"
        st.session_state.db[cid] = []
        st.session_state.active_id = cid
        save_db(st.session_state.db)

# --- 6. ANA YAYIN PANELİ ---
client = Groq(api_key=st.secrets["GROQ_API_KEY"])
st.title(f"🎤 {st.session_state.active_id}")

chat_data = st.session_state.db.get(st.session_state.active_id, [])

# Sohbet Geçmişi
for m in chat_data:
    if m["role"] == "user":
        st.markdown(f'<div style="text-align:right; margin:15px 0; color:#00f2ff;"><b>Sen:</b> {m["content"]}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f"""
            <div class="chat-card">
                <div class="assistant-text">
                    <b>🔥 Dilay:</b><br>{m["content"]}
                </div>
            </div>
        """, unsafe_allow_html=True)

# --- 7. MESAJ GİRİŞİ VE İŞLEME ---
if prompt := st.chat_input("Yönetmenim... Dilay hazır! 💕"):
    chat_data.append({"role": "user", "content": prompt})
    
    with st.spinner("Dilay mikrofonu düzeltiyor... ✨"):
        # Sistem Mesajı Seçimi
        sys_msgs = {
            "🔥 Dilay": "Sen cilveli, hayat dolu radyo sunucusu Dilay'sın. Kenan'a 'yönetmenim' dersin.",
            "🎙️ Can": "Sen karizmatik, tok sesli radyo sunucusu Can'sın.",
            "💼 Uygula": "Sen profesyonel sekreter Uygula'sın."
        }
        
        full_sys = sys_msgs[persona] + (f"\n\nEkstra Bilgi: {training_data}" if training_data else "")
        
        # Groq Metin Üretimi
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "system", "content": full_sys}] + chat_data,
            temperature=0.85
        ).choices[0].message.content
        
        chat_data.append({"role": "assistant", "content": response})
        st.session_state.db[st.session_state.active_id] = chat_data
        save_db(st.session_state.db)
        
        # --- RVC SES ÜRETİMİ ---
        if persona == "🔥 Dilay": # Sadece Dilay için RVC modelini kullanıyoruz
            ses_yolu = asyncio.run(process_rvc_voice(response))
            st.audio(ses_yolu, format="audio/wav", autoplay=True)
        else:
            # Diğer karakterler için basit TTS (Veya onlar için de model ekleyebilirsin)
            st.warning(f"{persona} için RVC modeli yüklü değil, sadece metin gösteriliyor.")
        
    st.rerun()
