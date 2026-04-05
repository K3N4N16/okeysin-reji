```html
<!DOCTYPE html>
<html lang="tr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Okeysin - Modern Okey, Pişti ve Batak</title>
  <style>
    :root {
      --primary: #289672;
      --secondary: #1d3557;
      --bg: #f4f9f4;
      --white: #fff;
      --gold: #ffd166;
      --shadow: 0 4px 16px rgba(44,62,80,0.07);
    }
    body {
      margin: 0;
      padding: 0;
      font-family: 'Segoe UI', Arial, sans-serif;
      background: var(--bg);
      color: var(--secondary);
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      justify-content: flex-start;
      align-items: center;
    }
    header {
      width: 100%;
      background: linear-gradient(90deg, var(--primary), var(--gold));
      color: var(--white);
      text-align: center;
      padding: 32px 10px 20px 10px;
      box-shadow: var(--shadow);
    }
    header h1 {
      font-size: 2.5rem;
      margin: 0;
      font-weight: 800;
      letter-spacing: 1px;
      display: flex;
      gap: 0.5em;
      align-items: center;
      justify-content: center;
    }
    header span {
      font-size: 2.4rem;
    }
    .subhead {
      margin-top: 6px;
      font-size: 1.15rem;
      opacity: 0.92;
      font-weight: 500;
    }
    main {
      width: 98%;
      max-width: 880px;
      margin: 34px auto 0 auto;
      display: flex;
      flex-wrap: wrap;
      gap: 28px;
      justify-content: center;
      align-items: flex-start;
    }
    .game-card {
      background: var(--white);
      box-shadow: var(--shadow);
      border-radius: 12px;
      padding: 26px 20px 18px 20px;
      flex-basis: 275px;
      flex-grow: 1;
      min-width: 220px;
      display: flex;
      flex-direction: column;
      align-items: center;
      transition: transform 0.15s, box-shadow 0.15s;
    }
    .game-card:hover {
      transform: translateY(-6px) scale(1.027);
      box-shadow: 0 8px 22px 0 rgba(80,80,80,0.12);
    }
    .game-icon {
      font-size: 2.4rem;
      margin-bottom: 12px;
    }
    .game-title {
      font-size: 1.33rem;
      font-weight: bold;
      color: var(--primary);
      margin-bottom: 10px;
      letter-spacing: 0.7px;
      text-align: center;
    }
    .game-desc {
      font-size: 1.02rem;
      opacity: 0.91;
      text-align: center;
      margin-bottom: 14px;
    }
    .game-visual {
      display: flex;
      gap: 1em;
      flex-wrap: wrap;
      margin-bottom: 8px;
      justify-content: center;
    }
    .tile, .card {
      display: inline-flex;
      justify-content: center;
      align-items: center;
      background: var(--bg);
      border-radius: 6px;
      box-shadow: 0 1.5px 5px 0 rgba(60,60,60,0.07);
      margin: 2px;
      font-weight: 700;
      font-size: 1.11em;
    }
    .tile {
      width: 36px;
      height: 46px;
      color: #c1121f;
      background: #f7ecde;
      border: 2.2px solid #e8c57a;
    }
    .card {
      width: 32px;
      height: 45px;
      color: #212529;
      border: 1.8px solid #999;
      background: #fffbe7;
    }
    .point {
      background: var(--gold);
      border-radius: 50%;
      width: 2em;
      height: 2em;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      color: #fff;
      font-size: 1.05em;
      font-weight: bold;
      margin-left: 5px;
    }
    .feature-list {
      margin: 18px 0 8px 0;
      padding: 0;
      list-style: none;
      text-align: left;
    }
    .feature-list li {
      font-size: .97rem;
      margin-bottom: 6px;
      position: relative;
      padding-left: 1.6em;
    }
    .feature-list li:before {
      content: "✨";
      position: absolute;
      left: 0.1em;
      font-size: 1.07em;
    }
    @media (max-width: 700px) {
      header h1 { font-size: 1.4rem; }
      main { gap: 17px; }
      .game-card { min-width: 155px; padding: 16px 5px 12px 5px; }
      .game-icon { font-size: 1.8rem; margin-bottom: 7px; }
      .game-visual { gap: 0.4em;}
    }
    @media (max-width: 450px) {
      .game-card { min-width: 114px; }
      .tile, .card { width: 22px; height: 27px; font-size: 0.69em; }
      .point { width: 1.3em; height: 1.3em; font-size: .79em; }
      main { margin-top: 14px; }
    }
  </style>
</head>
<body>
  <header>
    <h1>
      <span>🀄</span>
      Okeysin
    </h1>
    <div class="subhead">
      Modern, gelişmiş ve tasarımlı: Okey, Pişti ve Batak ile her elde keyif! 👑
    </div>
  </header>
  <main>
    <!-- OKEY CARD -->
    <section class="game-card">
      <div class="game-icon">🀄</div>
      <div class="game-title">Modern Okey</div>
      <div class="game-visual">
        <span class="tile" style="color: #c1121f;">7</span>
        <span class="tile" style="color: #0077b6;">12</span>
        <span class="tile" style="color: #f48c06;">J</span>
        <span class="tile" style="color: #212529;">🔶</span>
        <span class="point" style="background: var(--primary);">+101</span>
      </div>
      <div class="game-desc">
        4 kişilik geleneksel oyun yepyeni arayüz, kolay oynanış ve canlı animasyonlarla! <br>
          Çift okey, el açma, taş dizme ve çok daha fazlası...
      </div>
      <ul class="feature-list">
        <li>Otomatik taş dizilim ve öneri sistemi</li>
        <li>Animasyonlu, renkli masa tasarımları</li>
        <li>Gerçekçi efektlerle eşsiz oyun hissi</li>
      </ul>
    </section>
    <!-- PIŞTI CARD -->
    <section class="game-card">
      <div class="game-icon">🃏</div>
      <div class="game-title">Pişti</div>
      <div class="game-visual">
        <span class="card" style="color: #d90429;">A♥</span>
        <span class="card" style="color: #222;">7♣</span>
        <span class="card" style="color: #222;">10♠</span>
        <span class="point" style="background: #c1121f;">+20</span>
      </div>
      <div class="game-desc">
        Hızlı, eğlenceli ve rekabet dolu pişti deneyimi! <br> Otomatik kart dağıtımı, ses efektleri ve akıcı geçişlerle akıllı pişti keyfi.
      </div>
      <ul class="feature-list">
        <li>Açık ve kapalı kart gösterimi</li>
        <li>Anlık puan hesaplama ve lider tablosu</li>
        <li>Farklı arka plan temaları ve hızlı oyun</li>
      </ul>
    </section>
    <!-- BATAK CARD -->
    <section class="game-card">
      <div class="game-icon">🂡</div>
      <div class="game-title">Batak</div>
      <div class="game-visual">
        <span class="card" style="color: #212529;">2♠</span>
        <span class="card" style="color: #d90429;">Q♥</span>
        <span class="card" style="color: #222;">J♣</span>
        <span class="card" style="color: #212529;">A♠</span>
        <span class="point" style="background: var(--secondary);">0-13</span>
      </div>
      <div class="game-desc">
        İhale usulü, kozlu veya kozsuz: <br>
        Modern scorboard, akıcı dizayn ve stratejik oynanış ile Batak'ın en yeni hali!
      </div>
      <ul class="feature-list">
        <li>Dört farklı batak türü (Koz/Maka)</li>
        <li>Dinamik ihale ve sıralı kart/puan paneli</li>
        <li>Renkli, minimal masa ve hızlı geçişler</li>
      </ul>
    </section>
  </main>
  <footer style="margin:36px 0 19px 0; text-align:center; font-size:.94rem; color:#999; width:100%;">
    © 2026 Okeysin — Tüm hakları saklıdır.
  </footer>
</body>
</html>
```
