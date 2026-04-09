# ... (Üst kısımdaki CSS ve Ayarlar aynı kalıyor) ...

# Sohbet Akışı
# i değişkenini döngüye ekleyerek her elemana benzersiz ID veriyoruz
for i, chat in enumerate(st.session_state.chat_history):
    if chat["role"] == "user":
        st.markdown(f'<div class="patron-bubble"><b>Patron:</b> {chat["content"]}</div>', unsafe_allow_html=True)
    else:
        tema = "dilay-theme" if chat["host"] == "Dilay 💖" else "mert-theme"
        st.markdown(f"""
            <div class="host-card {tema}">
                <b style="font-size: 1.2em;">{chat['host']}</b><br>
                <div style="margin-top: 10px;">{chat['content']}</div>
            </div>
        """, unsafe_allow_html=True)
        
        # SES OYNATICI DÜZELTMESİ
        if chat.get("audio"):
            # Sadece en son mesajın otomatik çalması için kontrol
            is_latest = (i == len(st.session_state.chat_history) - 1)
            
            # key=f"audio_{i}" hatayı çözen kritik kısımdır
            st.audio(
                chat["audio"], 
                format="audio/wav", 
                autoplay=is_latest, 
                key=f"audio_{i}_{random.randint(0,9999)}" 
            )

# ====================== AI VE SES TETİKLEME (ALT KISIM) ======================

if prompt := st.chat_input("Patron, yayına bir not bırak..."):
    st.session_state.chat_history.append({"role": "user", "content": prompt})
    
    with st.spinner(f"{secilen_sunucu} hazırlanıyor..."):
        # Mesajları sisteme gönderirken sunucu kimliğini ve modu koru
        messages = [{"role": "system", "content": personalar[secilen_sunucu]}] + \
                   [{"role": m["role"], "content": m["content"]} for m in st.session_state.chat_history[-8:]]
        
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=messages,
            temperature=0.8
        ).choices[0].message.content

        # Ses dosyasını oku (Hata payı bırakma)
        audio_data = None
        target_audio = ses_dosyalari[secilen_sunucu]
        try:
            if os.path.exists(target_audio):
                with open(target_audio, "rb") as f:
                    audio_data = f.read()
        except Exception as e:
            st.error(f"Ses okuma hatası: {e}")

        st.session_state.chat_history.append({
            "role": "assistant",
            "host": secilen_sunucu,
            "content": response,
            "audio": audio_data
        })
        
        st.rerun()
