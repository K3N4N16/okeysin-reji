import streamlit as st
import os
from groq import Groq
from rvc_python.infer import RVCInference
import edge_tts
import asyncio
import tempfile

# --- SAYFA TASARIMI ---
st.set_page_config(page_title="Dilay v7.0 Ultra", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #000000; color: #ff0000; }
    .stButton>button { background-color: #ff0000; color: white; border-radius: 20px; border: 1px solid #ff0000; }
    .stTextInput>div>div>input { background-color: #111111; color: #ff0000; border: 1px solid #ff0000; }
    .stChatMessage { background-color: #111111; border-radius: 10px; border: 1px solid #330000; margin-bottom: 10px; }
    </style>
    """, unsafe_allow_html=True)

st.title("🎙️ Aşk-ı Muhabbet | Dilay v7.0")
st.subheader("Yönetmenim Kenan Bey, yayın için emrinizdeyim...")

# --- SECRET KONTROL ---
if "GROQ_API_KEY" in st.secrets:
    client = Groq(api_key=st.secrets["GROQ_API_KEY"])
else:
    st.error("Lütfen Hugging Face Settings -> Secrets kısmından GROQ_API_KEY ekleyin!")
    st.stop()

# --- MODEL LİNKLERİ ---
PTH_URL = "https://huggingface.co/matroks/dilay/resolve/main/my-project_60e_660s.pth"
INDEX_URL = "https://huggingface.co/matroks/dilay/resolve/main/added_IVF264_Flat_nprobe_1_my-project_v2.index"

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Yönetmenim, ne konuşalım?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Groq Zekası
    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{
            "role": "system", 
            "content": "Sen Dilay'sın. İşveli, cilveli, sempatik bir radyo asistanısın. Patronun Kenan'a karşı çok sıcak ve duygusalsın."
        }] + st.session_state.messages
    )
    response = completion.choices[0].message.content
    
    with st.chat_message("assistant"):
        st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})
    
    # SES SÜRECİ
    async def generate_voice():
        try:
            communicate = edge_tts.Communicate(response, "tr-TR-EmelNeural")
            with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_mp3:
                await communicate.save(temp_mp3.name)
                temp_path = temp_mp3.name
            
            rvc = RVCInference(device="cpu")
            rvc.set_model(PTH_URL, INDEX_URL)
            output_wav = "yayin_sesi.wav"
            rvc.infer(temp_path, output_wav)
            
            st.audio(output_wav, format="audio/wav", autoplay=True)
            if os.path.exists(temp_path): os.remove(temp_path)
        except Exception as e:
            st.error(f"Ses Hatası: {e}")

    asyncio.run(generate_voice())
