__import__('pysqlite3')
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')
# --- BURADAN SONRA SENİN IMPORTLARIN BAŞLAR ---
import os
import sys
# ... devamı aynı ...
import os
import sys
import base64
import shutil
import asyncio
import edge_tts
from groq import Groq

# --- WINDOWS YAMASI ---
try:
    import pywintypes
except ImportError:
    pass

import streamlit as st
from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
import streamlit as st
from groq import Groq
import os

# --- KONFİGÜRASYON (BULUT UYUMLU) ---
# Streamlit Secrets üzerinden anahtarı güvenli bir şekilde çeker
if "GROQ_API_KEY" in st.secrets:
    GROQ_API_KEY = st.secrets["GROQ_API_KEY"]
else:
    # Eğer bulutta değil de yereldeysen hata almamak için boş bırakır
    GROQ_API_KEY = "" 

client = Groq(api_key=GROQ_API_KEY)
MODEL_NAME = "llama-3.3-70b-versatile"
DATA_PATH = "veriler"
DB_PATH = "vektor_db"

# --- AZURE (EDGE-TTS) SESLENDİRME FONKSİYONU ---
async def ses_uret(text, filename):
    # 'tr-TR-EmelNeural' en doğal ve zarif Türkçe kadın sesidir
    communicate = edge_tts.Communicate(text, "tr-TR-EmelNeural")
    await communicate.save(filename)

def metni_seslendir(text):
    try:
        audio_file = "response.mp3"
        # Eski dosyayı temizle
        if os.path.exists(audio_file):
            os.remove(audio_file)
            
        # Ses üretimini başlat
        asyncio.run(ses_uret(text, audio_file))
        
        with open(audio_file, "rb") as f:
            data = f.read()
            b64 = base64.b64encode(data).decode()
            st.markdown(f'<audio controls autoplay src="data:audio/mp3;base64,{b64}"></audio>', unsafe_allow_html=True)
    except Exception as e:
        st.sidebar.error(f"Ses Hatası: {e}")

# --- DİĞER FONKSİYONLAR VE RAG ---
@st.cache_resource
def verileri_yukle():
    if not os.path.exists(DATA_PATH) or not os.listdir(DATA_PATH): return None
    documents = []
    for file in os.listdir(DATA_PATH):
        f_path = os.path.join(DATA_PATH, file)
        if file.endswith(".pdf"): documents.extend(PyPDFLoader(f_path).load())
        elif file.endswith(".txt"): documents.extend(TextLoader(f_path, encoding="utf-8").load())
    
    splits = RecursiveCharacterTextSplitter(chunk_size=400, chunk_overlap=40).split_documents(documents)
    return Chroma.from_documents(documents=splits, embedding=HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2"), persist_directory=DB_PATH)

# --- ARAYÜZ ---
st.set_page_config(page_title="Okeysin Live - Azure Voice", layout="wide")
st.title("🎙️ Okeysin Live (Azure & Groq)")
st.sidebar.header("⚙️ Reji Paneli")
ses_acik = st.sidebar.toggle("Canlı Mikrofon", value=True)

vector_db = verileri_yukle()

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]): st.markdown(message["content"])

if prompt := st.chat_input("Yönetmenim, yayındayız..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"): st.markdown(prompt)

    context = ""
    if vector_db:
        docs = vector_db.similarity_search(prompt, k=3)
        context = "\n".join([d.page_content for d in docs])

    sys_instruction = f"""
    KİMLİK: Adın Okeysin. Entelektüel, zarif, bayan bir radyo fenomenisin.
    PROTOKOL: Kullanıcı senin Yönetmenindir. Asla "Tamam", "Anladım" deme. Doğrudan yayına gir. 
    Parantez içi betimleme yapma. Saatleri edebi söyle.
    YAYIN ARŞİVİ: {context}
    """

    with st.chat_message("assistant"):
        res_placeholder = st.empty()
        full_res = ""
        completion = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[{"role": "system", "content": sys_instruction}] + st.session_state.messages,
            stream=True,
        )
        for chunk in completion:
            content = chunk.choices[0].delta.content
            if content:
                full_res += content
                res_placeholder.markdown(full_res + "▌")
        
        res_placeholder.markdown(full_res)
        st.session_state.messages.append({"role": "assistant", "content": full_res})
        if ses_acik:
            metni_seslendir(full_res)