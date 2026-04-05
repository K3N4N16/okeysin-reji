```html
<!DOCTYPE html>
<html lang="tr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Okeysin | Modern Okey Masası</title>
<style>
:root {
  --bg: #0d0f1c;
  --fg: #f7f7ff;
  --accent: #ff7a18;
  --accent-2: #2ec4ff;
  --card: rgba(255,255,255,0.05);
  --shadow: 0 10px 30px rgba(0,0,0,0.4);
}
body.light {
  --bg: #f2f6ff;
  --fg: #101226;
  --card: rgba(16,18,38,0.05);
  --shadow: 0 12px 40px rgba(15,20,40,0.2);
}
* { box-sizing:border-box; }
body {
  margin:0;
  font-family: "Segoe UI", system-ui, sans-serif;
  background: radial-gradient(circle at top, #1c1f3b, var(--bg));
  color:var(--fg);
  min-height:100vh;
  display:flex;
  justify-content:center;
  align-items:center;
  padding:3vw;
}
main {
  width:min(1100px,100%);
  background:var(--card);
  border-radius:28px;
  box-shadow:var(--shadow);
  overflow:hidden;
  backdrop-filter: blur(16px);
  border:1px solid rgba(255,255,255,0.08);
}
header {
  padding:3rem clamp(1.5rem,4vw,3rem) 2rem;
  display:flex;
  flex-wrap:wrap;
  gap:2rem;
  justify-content:space-between;
  align-items:center;
}
.hero-text { max-width:540px; }
h1 {
  font-size:clamp(2.6rem,4.2vw,3.5rem);
  margin:0 0 1rem;
  line-height:1.1;
}
p { margin:0 0 1rem; color:rgba(247,247,255,0.8); }
.cta-group {
  display:flex;
  flex-wrap:wrap;
  gap:0.8rem;
  margin-top:1.2rem;
}
button {
  border:none;
  border-radius:999px;
  padding:0.9rem 1.4rem;
  font-size:0.95rem;
  font-weight:600;
  cursor:pointer;
  transition:transform 0.2s ease, box-shadow 0.2s ease;
}
button:active { transform:scale(0.96); }
.btn-primary {
  background:linear-gradient(120deg,var(--accent),var(--accent-2));
  color:#fff;
  box-shadow:0 10px 25px rgba(255,122,24,0.35);
}
.btn-ghost {
  background:transparent;
  border:1px solid rgba(255,255,255,0.4);
  color:var(--fg);
}
.theme-toggle {
  margin-left:auto;
  background:var(--card);
  color:var(--fg);
  border:1px solid rgba(255,255,255,0.3);
}
.dashboard {
  display:grid;
  grid-template-columns:repeat(auto-fit,minmax(240px,1fr));
  gap:1.5rem;
  padding:0 2.5rem 3rem;
}
.card {
  background:rgba(255,255,255,0.03);
  border-radius:22px;
  padding:1.6rem;
  border:1px solid rgba(255,255,255,0.06);
  min-height:180px;
  display:flex;
  flex-direction:column;
  gap:1rem;
}
.scoreboard ul {
  list-style:none;
  padding:0;
  margin:0;
  display:flex;
  flex-direction:column;
  gap:1rem;
}
.player-row {
  display:flex;
  align-items:center;
  justify-content:space-between;
  gap:1rem;
}
.player-info {
  display:flex;
  align-items:center;
  gap:0.8rem;
  font-weight:600;
}
.controls {
  display:flex;
  gap:0.4rem;
}
.controls button {
  width:38px;
  height:38px;
  border-radius:50%;
  font-size:1.1rem;
  background:rgba(255,255,255,0.08);
  color:var(--fg);
}
.badge {
  font-size:0.75rem;
  text-transform:uppercase;
  letter-spacing:0.08em;
  color:rgba(247,247,255,0.6);
}
.table-visual {
  position:relative;
  flex:1;
  display:grid;
  place-items:center;
}
.okey-table {
  width:100%;
  aspect-ratio:1/0.6;
  background:linear-gradient(145deg,#1c253f,#13182c);
  border-radius:32px;
  border:2px solid rgba(255,255,255,0.08);
  box-shadow:0 20px 50px rgba(0,0,0,0.35) inset;
  position:relative;
  padding:1rem;
}
.seat {
  position:absolute;
  display:flex;
  flex-direction:column;
  align-items:center;
  gap:0.3rem;
  font-size:0.9rem;
}
.seat span { background:rgba(0,0,0,0.35); padding:0.3rem 0.8rem; border-radius:999px; font-weight:600; }
.seat .tiles { font-size:1.5rem; }
.seat.top { top:10px; left:50%; transform:translateX(-50%); }
.seat.bottom { bottom:10px; left:50%; transform:translateX(-50%); }
.seat.left { left:10px; top:50%; transform:translateY(-50%) rotate(-90deg); }
.seat.right { right:10px; top:50%; transform:translateY(-50%) rotate(90deg); }
.center-pot {
  position:absolute;
  top:50%; left:50%;
  transform:translate(-50%,-50%);
  background:rgba(255,255,255,0.08);
  padding:1.2rem 2rem;
  border-radius:18px;
  text-align:center;
}
.stats-grid {
  display:grid;
  grid-template-columns:repeat(auto-fit,minmax(160px,1fr));
  gap:1rem;
}
.stat {
  padding:1rem;
  border-radius:18px;
  background:rgba(0,0,0,0.25);
}
.progress {
  height:6px;
  border-radius:999px;
  background:rgba(255,255,255,0.15);
  overflow:hidden;
}
.progress span {
  display:block;
  height:100%;
  border-radius:999px;
}
.features {
  display:grid;
  grid-template-columns:repeat(auto-fit,minmax(220px,1fr));
  gap:1rem;
}
.accordion-item {
  border:1px solid rgba(255,255,255,0.08);
  border-radius:18px;
  overflow:hidden;
}
.accordion-header {
  background:rgba(255,255,255,0.03);
  padding:1rem 1.2rem;
  display:flex;
  justify-content:space-between;
  cursor:pointer;
  font-weight:600;
}
.accordion-content {
  max-height:0;
  overflow:hidden;
  padding:0 1.2rem;
  transition:max-height 0.3s ease;
  color:rgba(247,247,255,0.8);
}
.accordion-item.active .accordion-content {
  max-height:200px;
  padding:0.8rem 1.2rem 1.2rem;
}
footer {
  padding:1.5rem 2.5rem 3rem;
  display:flex;
  flex-wrap:wrap;
  gap:1rem;
  align-items:center;
  justify-content:space-between;
  font-size:0.85rem;
  color:rgba(247,247,255,0.6);
}
@media (max-width:720px) {
  header { flex-direction:column; align-items:flex-start; }
  .table-visual, .scoreboard { min-height:auto; }
  .seat.left, .seat.right { display:none; }
}
</style>
</head>
<body>
<main>
  <header>
    <div class="hero-text">
      <p class="badge">Okeysin • Pro Masa</p>
      <h1>Modern Okey masasında hız, stil ve strateji bir arada.</h1>
      <p>Özel turnuva lobileri, gerçek zamanlı skor takibi, adaptif eşleştirme ve neon estetik aynı masada. Kulübünü kur, davet linki paylaş, anında oyna.</p>
      <div class="cta-group">
        <button class="btn-primary">⚡ Hızlı Eşleştirme</button>
        <button class="btn-ghost">👥 Özel Oda Aç</button>
      </div>
    </div>
    <button class="theme-toggle" id="themeToggle">🌗 Tema</button>
  </header>

  <section class="dashboard">
    <article class="card scoreboard">
      <p class="badge">Canlı Skor Tahtası</p>
      <ul>
        <li class="player-row" data-player="0">
          <div class="player-info">🧠 <span>Stratejist</span></div>
          <div class="controls">
            <button class="minus">−</button>
            <strong class="score">1320</strong>
            <button class="plus">+</button>
          </div>
        </li>
        <li class="player-row" data-player="1">
          <div class="player-info">🔥 <span>Blöf Ustası</span></div>
          <div class="controls">
            <button class="minus">−</button>
            <strong class="score">1180</strong>
            <button class="plus">+</button>
          </div>
        </li>
        <li class="player-row" data-player="2">
          <div class="player-info">🎯 <span>Hedefçi</span></div>
          <div class="controls">
            <button class="minus">−</button>
            <strong class="score">1040</strong>
            <button class="plus">+</button>
          </div>
        </li>
        <li class="player-row" data-player="3">
          <div class="player-info">🌪️ <span>Turbo Oyuncu</span></div>
          <div class="controls">
            <button class="minus">−</button>
            <strong class="score">960</strong>
            <button class="plus">+</button>
          </div>
        </li>
      </ul>
    </article>

    <article class="card table-visual">
      <p class="badge">Canlı Masa Görünümü</p>
      <div class="okey-table">
        <div class="seat top">
          <span>🎩 Kuzey</span>
          <div class="tiles">🀄🀅🀆🀇</div>
        </div>
        <div class="seat bottom">
          <span>🧿 Sen</span>
          <div class="tiles">🀈🀉🀊🀋</div>
        </div>
        <div class="seat left">
          <span>♟️ Batı</span>
          <div class="tiles">🀌🀍🀎🀏</div>
        </div>
        <div class="seat right">
          <span>⚙️ Doğu</span>
          <div class="tiles">🀐🀑🀒🀓</div>
        </div>
        <div class="center-pot">
          <p style="margin:0;font-weight:700;">Okey Taşı</p>
          <p style="margin:0.2rem 0 0;">🀚 • Tur: 17</p>
        </div>
      </div>
    </article>

    <article class="card">
      <p class="badge">Anlık İstatistikler</p>
      <div class="stats-grid">
        <div class="stat">
          <strong>%78 Win Rate</strong>
          <div class="progress"><span style="width:78%; background:var(--accent);"></span></div>
          <small>Son 40 maç</small>
        </div>
        <div class="stat">
          <strong>14 Serisi</strong>
          <div class="progress"><span style="width:60%; background:var(--accent-2);"></span></div>
          <small>Aktif galibiyet</small>
        </div>
        <div class="stat">
          <strong>03:12 dk</strong>
          <div class="progress"><span style="width:45%; background:#c7ff4d;"></span></div>
          <small>Tur başına süre</small>
        </div>
      </div>
    </article>
  </section>

  <section class="dashboard">
    <article class="card">
      <p class="badge">Öne Çıkan Araçlar</p>
      <div class="features">
        <div>
          <strong>🛰️ Adaptif Eşleştirme</strong>
          <p>MMR algoritması benzer tempo ve risk profiline sahip oyuncuları saniyeler içinde bulur.</p>
        </div>
        <div>
          <strong>🧭 Strateji Haritası</strong>
          <p>Seçilen serilere göre otomatik önerilen bekler, bloklar ve çift açma simülasyonları.</p>
        </div>
        <div>
          <strong>🔐 Kulüp Koruması</strong>
          <p>Şifreli oda + tek tık davet kodu, AI spam filtresi ve güvenli sohbet.</p>
        </div>
      </div>
    </article>

    <article class="card">
      <p class="badge">Pro İpuçları</p>
      <div class="accordion">
        <div class="accordion-item active">
          <div class="accordion-header">🎯 Seriye Öncelik Ver</div>
          <div class="accordion-content">Çift stoğunu erken erit, 3 renkli sıraları dengele. Tur başına minimum 2 taş geliştirmeye bak.</div>
        </div>
        <div class="accordion-item">
          <div class="accordion-header">🧊 Soğukkanlı Puanlama</div>
          <div class="accordion-content">Rakip payoff takibi yap: 40 üstü risk taşıyan oyuncuya temkinli at, taş bloklarını sakla.</div>
        </div>
        <div class="accordion-item">
          <div class="accordion-header">⚡ Turbo Hamle Modu</div>
          <div class="accordion-content">Sistem 25 saniye altı hamlelerde bonus MMR verir. Önceki tur verilerini kullanarak tahminli atış yap.</div>
        </div>
      </div>
    </article>
  </section>

  <footer>
    <span>© 2026 Okeysin • Neon masa, gerçek rekabet.</span>
    <span>Destek: destek@okeysin.com</span>
  </footer>
</main>

<script>
const body = document.body;
document.getElementById("themeToggle").addEventListener("click", () => {
  body.classList.toggle("light");
});
document.querySelectorAll(".player-row").forEach((row) => {
  const scoreEl = row.querySelector(".score");
  row.querySelector(".plus").addEventListener("click", () => {
    scoreEl.textContent = Number(scoreEl.textContent) + 10;
  });
  row.querySelector(".minus").addEventListener("click", () => {
    scoreEl.textContent = Math.max(0, Number(scoreEl.textContent) - 10);
  });
});
document.querySelectorAll(".accordion-item").forEach((item) => {
  item.querySelector(".accordion-header").addEventListener("click", () => {
    item.classList.toggle("active");
  });
});
</script>
</body>
</html>
```