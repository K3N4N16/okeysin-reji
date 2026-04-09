# ... (Üst kısımdaki importlar ve CSS aynı kalabilir) ...

# ====================== REJİ İSTATİSTİKLERİ ======================
with st.sidebar:
    st.markdown("### 📊 Yayın Durumu")
    dinleyici = random.randint(18500, 21000)
    st.status(f"Yayında {dinleyici:,} kişi var", state="running")
    
    # Yeni Özellik: Fon Müziği Seçici
    st.divider()
    fon_muzigi = st.checkbox("🎶 Arka Plan Müziği")
    if fon_muzigi:
        # Buraya kendi fon müziği dosyanı koyabilirsin
        st.audio("radyo_fon.mp3", format="audio/mp3", loop=True)

# ====================== SOHBET ALANI GÜNCELLEMESİ ======================
# ... (Döngü kısmı aynı kalsın, sadece tasarım dokunuşu ekliyoruz) ...
for i, chat in enumerate(st.session_state.chat_history):
    # (Mevcut döngü kodun...)
    pass

# ====================== SES TETİKLEYİCİ GÜNCELLEMESİ ======================
# Mesaj gönderme kısmına küçük bir gecikme ve efekt ekleyebiliriz
if prompt := st.chat_input("Patron, yayına bir not bırak..."):
    # (Mevcut akış kodun...)
    # Küçük bir ipucu: AI cevabına göre 'yayin_tonu' değişkenini 
    # temperature değerine bağlayarak cevabın yaratıcılığını değiştirebilirsin.
    temp_val = 0.5 if yayin_tonu == "Sakin" else 0.9 if yayin_tonu == "Muzip" else 0.7
