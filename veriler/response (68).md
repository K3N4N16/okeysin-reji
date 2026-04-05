# Zamanlı Harf Açma Oyunu - Detaylı Örnek

Anladım! Yani botun şöyle çalışıyor:

> Soru gelir → `*****` şeklinde gizli cevap → her X saniyede bir harf açılır → kullanıcılar tahmin eder

Bu mantıkla çok eğlenceli bir şey yapalım:

---

## 🎬 Film Tahmin Oyunu

**Akış şöyle olur:**

```
⏱ 0. saniye  → 🎬 Bu hangi film? İpucu: 1994 yapımı efsane bir film
                Cevap: ********** (10 harf)

⏱ 5. saniye  → E********N

⏱ 10. saniye → ES*****EN  

⏱ 15. saniye → ESH***SEN

⏱ 20. saniye → ESHKı**SEN

⏱ 25. saniye → Süre doldu! Cevap: EŞKIYASEN → "Eşkıya"
```

Yanlış örnek verdim, daha temiz yazayım:

---

## 🎯 Tam Çalışma Örneği

Diyelim **"Ünlü Kişi Tahmin"** oyunu yapıyorsun:

```
📢 SORU: Bu ünlü kim?
🎤 İpucu: Türk müzik efsanesi, "Kralice" lakabı

⏱  0 sn  →  * * * * *   * * * * *
⏱  5 sn  →  A * * * *   * * * * *
⏱ 10 sn  →  A * * * N   * * * * *
⏱ 15 sn  →  A J * A N   * * * * *
⏱ 20 sn  →  A J D A N   P * K * *
⏱ 25 sn  →  Süre doldu! → AJDA PEKKAN ✅

🏆 İlk bilen: @kullanici123 → +50 puan!
```

---

## 🧩 Farklı Kategoriler Yapabilirsin

```
Pazartesi  → 🎬 Film Tahmin
Salı       → 🎵 Şarkı Sözünden Tahmin  
Çarşamba   → 🏙️ Şehir Tahmin (ipucu: ülke + özellik)
Perşembe   → ⚽ Futbolcu Tahmin
Cuma       → 🎭 Atasözü Tamamla
Cumartesi  → 😂 Emoji'den Film/Dizi Tahmin
Pazar      → 🧠 Genel Kültür
```

---

## ⚽ Futbolcu Tahmin Örneği

```
📢 SORU: Bu futbolcu kim?
🏟️ İpucu: Brezilyalı, 5 kez Ballon d'Or kazandı

⏱  0 sn  →  * * * * *
⏱  5 sn  →  * E * * *
⏱ 10 sn  →  M E * * İ
⏱ 15 sn  →  M E S * İ
⏱ 20 sn  →  Ooops! Arjantinli demiştik 😄
              Cevap: MESSİ ✅
```

---

## 🎵 Şarkı Sözünden Tahmin Örneği

```
📢 Bu şarkı hangisi?
🎶 "Yağmur yağıyor inceden..."

⏱  0 sn  →  * * * * * * *   * * * * *
⏱  5 sn  →  İ * * * * * *   * * * * *
⏱ 10 sn  →  İ N * E * E *   * E * * *
⏱ 15 sn  →  İ N C E D E N   * E L * R
⏱ 20 sn  →  Cevap: İNCEDEN GELİR ✅
```

---

## 💡 Puan Sistemi Önerisi

```
⚡ İlk harfte bildi     → 100 puan
⚡ 2. ipucunda bildi    → 75 puan  
⚡ 3. ipucunda bildi    → 50 puan
⚡ Son ipucunda bildi   → 25 puan
❌ Bilemedi             → 0 puan

🏆 Haftalık en yüksek puanlı → Özel rozet!
```

---

Hangi kategoriyle başlamak istiyorsun? Sana o kategoriye özel hazır soru-cevap listesi hazırlayabilirim, direkt bota yüklersin.