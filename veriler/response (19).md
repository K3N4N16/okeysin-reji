Anladım—“en gelişmiş profesyonel IP TV player + URL ekleme + Türkiye kanalları + içe/dışa aktarma + webhost TV IP modülü + mobil tam uyumlu” gibi kapsamlı bir proje istiyorsun. Ancak burada **önemli bir sınır** var: “Türkiye kanalları” ve “IP TV URL’leri” çoğu zaman **telif/içerik lisansı gerektiren** akışlar veya yasadışı kaynaklar olabilir. Ben sana **pirate/kaçak içerik listeleri**, “çalışan hazır URL’ler” veya bu amaçla kanal dağıtan içerikler veremem.

Yine de seni yarı yolda bırakmayacağım 😄: Sana **tam teşekküllü, modern, şık, mobil uyumlu** bir IP TV player uygulaması mimarisini ve **çalışır kod iskeletini** verebilirim. Bu altyapıda:
- Kullanıcı kendi **yasal playlist/kanal URL’lerini** ekleyebilir (m3u/m3u8, xspf vb.)
- **Kendi kanallarını** içe aktar/ dışa aktar
- Kullanıcı arayüzü, EPG/arama/etiketler/favoriler gibi modüller
- TV için web “host” modülü (liste yönetimi) — ama **içerik sağlayıcı değil**, sadece playlist yönetir
- Uygulama tarafında player (Web’de HTML5 video + HLS/DASH destek mantığı; mobilde PWA/React Native opsiyonu)

Aşağıda “en modern ve gösterişli” bir başlangıç sunuyorum: **Web tabanlı (PWA) modern IP TV player** + **kanal yönetimi (içe/dışa aktarma)** + örnek kanal formatları. İstersen bunu sonra React Native’ye de taşırız.

---

## 1) Mimari (Önerilen “Profesyonel” Yapı)

**Tek repo:**
- `/apps/web` → Mobil uyumlu PWA (player + kanal arama + favoriler + EPG slot)
- `/apps/server` → Node.js/Express API + JSON/Playlist yönetimi
- `/packages/shared` → kanal şemaları (types) + doğrulama

**Özellikler**
- Playlist import:
  - M3U (genel IP TV standardı)
  - JSON export/import (kendi formatımız)
- Export:
  - JSON ile kanal listesini dışa aktar
  - İstersen tekrar M3U olarak da dışa çıkar (ekleyebiliriz)
- Güvenlik:
  - CORS
  - URL doğrulama (format + HEAD ile kontrol opsiyonel)
  - Rate limit
- Player:
  - Web’de `video` etiketi + HLS için istemci tarafı (hls.js)
  - DASH varsa (dash.js) opsiyonel
- UI:
  - Dark mode, animasyonlar, modern kartlar
  - Kategoriler, arama, “son izlenenler”

---

## 2) Kanal Formatı (Lisanslı Kaynaklarla Kullan)

Kullanıcıların ekleyeceği playlist URL’lerini ben sağlayamam; ama **sen eklediğinde çalışacak** şekilde formatı standardize ediyorum.

### Kanal modeli (JSON)
```json
{
  "id": "tr-1",
  "name": "Kanal Adı",
  "logo": "https://.../logo.png",
  "group": "Haber",
  "stream": {
    "url": "https://.../stream.m3u8",
    "type": "hls"
  },
  "catchup": null,
  "epg": null
}
```

---

## 3) Uygulama: Web (PWA) + Player + İç/Dış Aktarım

### 3.1 Kurulum (Örnek)
```bash
mkdir iptv-modern
cd iptv-modern
npm init -y

# Server
mkdir -p apps/server apps/web packages/shared
npm i express cors helmet zod node-fetch express-rate-limit

# Web tarafı (Vite + React örnek)
# (Burayı proje kurulumuna göre güncelleyebilirsin)
```

İstersen tek komutla iskeleti üretmek için daha sonra CLI tasarlayabilirim; ama direkt kodu veriyorum.

---

## 4) Server: Kanal Yönetimi (Import/Export API)

### `apps/server/index.js`
```javascript
import express from "express";
import cors from "cors";
import helmet from "helmet";
import rateLimit from "express-rate-limit";
import { z } from "zod";

const app = express();
app.use(helmet());
app.use(cors({ origin: true }));
app.use(express.json({ limit: "1mb" }));

const limiter = rateLimit({ windowMs: 60_000, max: 200 });
app.use(limiter);

const ChannelSchema = z.object({
  id: z.string().min(1),
  name: z.string().min(1),
  logo: z.string().url().optional(),
  group: z.string().optional(),
  stream: z.object({
    url: z.string().min(1),
    type: z.enum(["hls", "mp4", "dash"]).default("hls")
  }),
  catchup: z.any().nullable().optional(),
  epg: z.any().nullable().optional()
});

const ImportChannelsSchema = z.object({
  source: z.enum(["json", "m3u"]).default("json"),
  channels: z.array(ChannelSchema)
});

let CHANNELS_DB = []; // Demo: gerçek projede DB (Postgres/SQLite) kullanılır

app.get("/api/health", (req, res) => res.json({ ok: true }));

app.get("/api/channels", (req, res) => {
  const q = (req.query.q || "").toString().toLowerCase();
  const group = (req.query.group || "").toString();
  let list = [...CHANNELS_DB];

  if (group) list = list.filter(c => c.group === group);
  if (q) list = list.filter(c =>
    c.name.toLowerCase().includes(q) ||
    (c.group || "").toLowerCase().includes(q)
  );

  res.json({ channels: list });
});

app.post("/api/channels/import", (req, res) => {
  const payload = ImportChannelsSchema.safeParse(req.body);
  if (!payload.success) {
    return res.status(400).json({ error: payload.error.flatten() });
  }

  // Merge by id (basit strateji)
  const incoming = payload.data.channels;
  const map = new Map(CHANNELS_DB.map(c => [c.id, c]));
  for (const ch of incoming) map.set(ch.id, ch);

  CHANNELS_DB = [...map.values()];
  res.json({ ok: true, count: incoming.length, total: CHANNELS_DB.length });
});

app.get("/api/channels/export", (req, res) => {
  res.json({ channels: CHANNELS_DB });
});

// Basit demo seed
app.post("/api/channels/seed-demo", (req, res) => {
  const demo = [
    {
      id: "demo-1",
      name: "Demo Haber",
      logo: "https://dummyimage.com/96x96/111/fff.png&text=NH",
      group: "Haber",
      stream: { url: "https://test-streams.mux.dev/x36xhzz/x36xhzz.m3u8", type: "hls" }
    },
    {
      id: "demo-2",
      name: "Demo Spor",
      logo: "https://dummyimage.com/96x96/111/fff.png&text=SP",
      group: "Spor",
      stream: { url: "https://test-streams.mux.dev/test_001/stream.m3u8", type: "hls" }
    }
  ];
  CHANNELS_DB = demo;
  res.json({ ok: true, total: CHANNELS_DB.length });
});

app.listen(3001, () => {
  console.log("Server running on http://localhost:3001");
});
```

> Not: “Demo URL’ler” test amaçlıdır. Gerçek TV kanalı URL’lerini sen yasal olarak sağlarsın.

---

## 5) Web Player: HLS Çal (hls.js) + Mobil UI

### `apps/web/src/components/Player.jsx` (özet)
```jsx
import React, { useEffect, useRef } from "react";
import Hls from "hls.js";

export default function Player({ streamUrl, streamType }) {
  const videoRef = useRef(null);
  const hlsRef = useRef(null);

  useEffect(() => {
    const video = videoRef.current;
    if (!video) return;

    // Temizle
    if (hlsRef.current) {
      hlsRef.current.destroy();
      hlsRef.current = null;
    }

    if (streamType === "hls") {
      if (Hls.isSupported()) {
        const hls = new Hls({
          enableWorker: true,
          lowLatencyMode: true,
        });
        hlsRef.current = hls;
        hls.loadSource(streamUrl);
        hls.attachMedia(video);
      } else if (video.canPlayType("application/vnd.apple.mpegurl")) {
        video.src = streamUrl; // Safari gibi
      } else {
        // fallback
        video.src = "";
      }
    } else {
      // mp4/dash opsiyonları
      video.src = streamUrl;
    }
  }, [streamUrl, streamType]);

  return (
    <div className="playerWrap">
      <video
        ref={videoRef}
        controls
        playsInline
        style={{ width: "100%", height: "auto", borderRadius: 16 }}
      />
    </div>
  );
}
```

### Mobil şık tasarım (CSS mini örnek)
```css
.playerWrap {
  padding: 12px;
  background: rgba(255,255,255,0.04);
  border: 1px solid rgba(255,255,255,0.08);
  backdrop-filter: blur(10px);
  border-radius: 18px;
}
```

---

## 6) İçe/Dışa Aktarma UI (JSON)

### İçe aktar (JSON)
- Kullanıcı bir JSON dosyasını seçer
- `channels/import` endpointine gönderir
- Liste yenilenir

### Dışa aktar
- `channels/export` çağrılır
- JSON dosya olarak indirilir

Bu kısmı istersen tek tek dosya haline getirip “çalışır React sayfaları” şeklinde de yazabilirim.

---

## 7) M3U İçe Aktarma (Ekleyelim Mi?)
Bu kısmı da yapabilirim ama burada kritik konu var:
- M3U içindeki URL’ler **kullanıcı tarafından sağlanmalı**.
- Ben “Türkiye kanalları için hazır m3u” üretmem/dağıtmam.
- Ama **M3U’yu parse edip** kendi sistemine dönüştüren kodu yazacağım.

İstersen bir sonraki adımda sana **tam M3U parser** (EXTINF metadata çıkarma + stream URL yakalama) kodunu ekleyebilirim.

---

## 8) “Webhost TV IP Modülü” Nasıl Olmalı?
“Host modülü” ile kastın genelde:
- Yönetim paneli: kanalları ekle/sil/güncelle
- Yetkilendirme (Admin login)
- Playlist export
- (Opsiyonel) kullanıcı bazlı listeler

Bu modülü güvenli yapmak için:
- Basit admin token (JWT) veya şifreli erişim
- URL’leri kaydetmeden önce doğrulama
- Rate limit

Ben sana bunun da API + UI iskeletini hazırlayacak şekilde genişletebilirim.

---

## Devam etmek için (netleştirmeden en iyi ilerleme)
Şu an en doğru ilerleme: Sana **tam bir “proje dosya yapısı” + çalışır web ekranları + import/export + kanal seçimi + player** bileşenlerini “uçtan uca” tek mesajda koymak zor; çok uzun olur.

Buna rağmen bugün başlayalım diye:
1) Server API iskeletini verdim (import/export dahil)
2) Player tarafında HLS mantığını verdim
3) Kanal JSON şemasını standardize ettim

### Bir sonraki mesajımda şunlardan birini **hemen** yazabilirim (içerik lisansına aykırı şeyler olmadan):
- **A)** Web için “Admin Panel” (kanal ekle/sil + JSON import + export)  
- **B)** Web için “Kullanıcı Player UI” (arama, gruplar, favoriler, son izlenenler)  
- **C)** Tam M3U parser (kendi formatına dönüştürme)  

Hangisini en çok istiyorsun? (A/B/C diye yazman yeterli.)