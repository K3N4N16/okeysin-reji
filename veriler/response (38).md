<think>
Kullanıcı sadece bir player widget istiyor:

1. Sadece player widget - mobil uyumlu
2. Stream URL: https://radyocast.com/8028/Stream
3. API URL: https://radyocast.com/cp/get_info.php?p=8028
4. Şarkı isteği gönderme formu
5. İstek mesajları kayan yazı alanı (marquee)
6. Temiz, minimal kod

Sadeleştirilmiş bir player widget yapalım:

- Mini player widget (compact)
- Müzik kontrolü (play/pause, volume)


- Başlık ve istek formu ile birlikte istek mesajlarının kayan metin olarak gösterimi

Tek dosya halinde tüm widget'ı yazacağım.
</think>```html
<!DOCTYPE html>
<html lang="tr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>📻 Radio Player Widget</title>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
  <style>
    * { margin: 0; padding: 0; box-sizing: border-box; }

    body {
      font-family: 'Inter', sans-serif;
      background: #050510;
      min-height: 100vh;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 20px;
      overflow: hidden;
    }

    /* ── ANİMASYONLU ARKA PLAN ── */
    .bg-anim {
      position: fixed; inset: 0; z-index: 0;
      overflow: hidden; pointer-events: none;
    }

    .bg-anim .blob {
      position: absolute; border-radius: 50%;
      filter: blur(100px); opacity: 0.2;
      animation: blobMove 20s ease-in-out infinite alternate;
    }

    .bg-anim .blob:nth-child(1) {
      width: 500px; height: 500px;
      background: #00e0ff;
      top: -20%; left: -15%;
    }
    .bg-anim .blob:nth-child(2) {
      width: 400px; height: 400px;
      background: #c760ff;
      bottom: -20%; right: -15%;
      animation-delay: -7s;
    }
    .bg-anim .blob:nth-child(3) {
      width: 300px; height: 300px;
      background: #ff6b9d;
      top: 50%; left: 60%;
      animation-delay: -14s;
    }

    @keyframes blobMove {
      0%   { transform: translate(0,0) scale(1); }
      50%  { transform: translate(60px,-40px) scale(1.2); }
      100% { transform: translate(-30px,50px) scale(0.9); }
    }

    /* ── WIDGET CONTAINER ── */
    .widget {
      position: relative; z-index: 1;
      width: 100%; max-width: 460px;
      background: rgba(10, 10, 40, 0.85);
      border: 1px solid rgba(255,255,255,0.08);
      border-radius: 24px;
      overflow: hidden;
      backdrop-filter: blur(30px);
      box-shadow:
        0 30px 80px rgba(0,0,0,0.6),
        0 0 60px rgba(0,224,255,0.08);
    }

    /* ── LIVE BAR ── */
    .live-bar {
      display: flex; align-items: center; justify-content: center;
      gap: 8px; padding: 8px 0;
      background: linear-gradient(90deg, rgba(0,224,255,0.1), rgba(199,96,255,0.1));
      border-bottom: 1px solid rgba(255,255,255,0.05);
      font-size: 0.65rem; letter-spacing: 3px; font-weight: 700;
      color: #00e0ff; text-transform: uppercase;
    }

    .live-bar .dot {
      width: 7px; height: 7px; border-radius: 50%;
      background: #00ff88;
      animation: blink 1.2s infinite;
      box-shadow: 0 0 8px #00ff88;
    }

    @keyframes blink { 0%,100%{opacity:1} 50%{opacity:0.15} }

    .live-bar span.listeners {
      color: rgba(255,255,255,0.4);
      font-weight: 400; letter-spacing: 1px;
    }

    /* ── SCROLLING TEXT (KAYAN YAZI) ── */
    .scroll-strip {
      position: relative;
      width: 100%; height: 36px;
      overflow: hidden;
      border-bottom: 1px solid rgba(255,255,255,0.04);
    }

    .scroll-track {
      display: flex;
      width: max-content;
      animation: marquee var(--speed, 20s) linear infinite;
      height: 100%;
      align-items: center;
    }

    .scroll-track:hover { animation-play-state: paused; }

    .scroll-item {
      display: flex; align-items: center; gap: 8px;
      padding: 0 24px;
      white-space: nowrap;
      font-size: 0.78rem;
      color: rgba(255,255,255,0.5);
    }

    .scroll-item .si-icon {
      color: #00e0ff;
      font-size: 0.7rem;
    }

    .scroll-item .si-name {
      color: #ff6b9d;
      font-weight: 600;
    }

    .scroll-item .si-song {
      color: rgba(255,255,255,0.7);
    }

    .scroll-sep {
      padding: 0 6px;
      color: rgba(255,255,255,0.15);
    }

    @keyframes marquee {
      0%   { transform: translateX(0); }
      100% { transform: translateX(-50%); }
    }

    /* ── COVER ART ── */
    .cover-section {
      position: relative;
      width: 100%;
      aspect-ratio: 16/10;
      overflow: hidden;
    }

    .cover-bg {
      width: 100%; height: 100%;
      object-fit: cover;
      filter: brightness(0.5) blur(1px);
      transform: scale(1.05);
    }

    .cover-overlay {
      position: absolute; inset: 0;
      background: linear-gradient(180deg,
        rgba(5,5,16,0.3) 0%,
        rgba(5,5,16,0.85) 100%
      );
      display: flex; align-items: center; justify-content: center;
    }

    .cover-art {
      width: 140px; height: 140px;
      border-radius: 20px;
      object-fit: cover;
      box-shadow: 0 15px 50px rgba(0,0,0,0.7);
      transition: transform 0.5s;
    }

    .cover-section:hover .cover-art {
      transform: scale(1.08);
    }

    .cover-glow {
      position: absolute;
      width: 140px; height: 140px;
      border-radius: 20px;
      background: linear-gradient(135deg, #00e0ff, #c760ff);
      opacity: 0.3; filter: blur(30px);
      pointer-events: none;
    }

    /* Bars */
    .cover-bars {
      position: absolute; bottom: 12px; left: 50%;
      transform: translateX(-50%);
      display: flex; gap: 3px; align-items: flex-end; height: 20px;
    }

    .cover-bars span {
      width: 3px; background: #00e0ff;
      border-radius: 2px;
      animation: barAnim 0.7s ease-in-out infinite;
    }

    .cover-bars span:nth-child(1) { height: 6px;  animation-delay: 0s; }
    .cover-bars span:nth-child(2) { height: 16px; animation-delay: 0.12s; }
    .cover-bars span:nth-child(3) { height: 10px; animation-delay: 0.24s; }
    .cover-bars span:nth-child(4) { height: 18px; animation-delay: 0.36s; }
    .cover-bars span:nth-child(5) { height: 8px;  animation-delay: 0.48s; }

    .cover-bars.paused span { animation-play-state: paused; height: 4px; }

    @keyframes barAnim {
      0%,100% { transform: scaleY(0.3); }
      50%     { transform: scaleY(1); }
    }

    /* Quality badge */
    .q-badge {
      position: absolute; top: 12px; right: 12px;
      padding: 3px 10px;
      background: rgba(0,0,0,0.6);
      border: 1px solid rgba(0,224,255,0.3);
      border-radius: 10px;
      font-size: 0.58rem; font-weight: 700;
      letter-spacing: 1px; color: #00e0ff;
    }

    /* ── TRACK INFO ── */
    .track-info {
      padding: 18px 22px 6px;
      text-align: center;
    }

    .track-label {
      font-size: 0.62rem;
      color: #00e0ff; letter-spacing: 4px;
      text-transform: uppercase;
      font-weight: 600; margin-bottom: 6px;
    }

    .track-title {
      font-size: 1.15rem;
      font-weight: 700; color: #fff;
      line-height: 1.35;
      max-height: 2.7em;
      overflow: hidden;
    }

    .track-artist {
      font-size: 0.85rem;
      color: rgba(255,255,255,0.45);
      margin-top: 4px;
    }

    /* ── PROGRESS ── */
    .progress-area {
      padding: 14px 22px 0;
    }

    .prog-track {
      width: 100%; height: 4px;
      background: rgba(255,255,255,0.08);
      border-radius: 2px;
      cursor: pointer; position: relative;
      overflow: visible;
    }

    .prog-fill {
      height: 100%; border-radius: 2px;
      background: linear-gradient(90deg, #00e0ff, #c760ff);
      width: 0%; transition: width 0.4s;
      position: relative;
    }

    .prog-thumb {
      position: absolute; right: -5px; top: 50%;
      transform: translateY(-50%) scale(0);
      width: 10px; height: 10px; border-radius: 50%;
      background: #00e0ff;
      box-shadow: 0 0 10px rgba(0,224,255,0.5);
      transition: transform 0.2s;
    }

    .prog-track:hover .prog-thumb { transform: translateY(-50%) scale(1); }

    .prog-times {
      display: flex; justify-content: space-between;
      margin-top: 6px;
      font-size: 0.65rem; color: rgba(255,255,255,0.3);
      font-variant-numeric: tabular-nums;
    }

    /* ── CONTROLS ── */
    .controls {
      display: flex; align-items: center; justify-content: center;
      gap: 16px; padding: 16px 22px;
    }

    .c-btn {
      width: 42px; height: 42px; border-radius: 50%;
      border: 1px solid rgba(255,255,255,0.08);
      background: rgba(255,255,255,0.03);
      color: rgba(255,255,255,0.5);
      font-size: 0.85rem; cursor: pointer;
      display: flex; align-items: center; justify-content: center;
      transition: all 0.25s;
    }

    .c-btn:hover {
      border-color: rgba(0,224,255,0.3);
      color: #00e0ff;
      background: rgba(0,224,255,0.06);
      transform: scale(1.1);
    }

    .c-btn.active {
      color: #00e0ff;
      border-color: rgba(0,224,255,0.4);
      background: rgba(0,224,255,0.1);
    }

    .c-btn.like-active {
      color: #ff6b9d;
      border-color: rgba(255,107,157,0.4);
    }

    .c-btn-play {
      width: 60px; height: 60px; border-radius: 50%;
      border: none;
      background: linear-gradient(135deg, #00e0ff, #7b5fff);
      color: #fff; font-size: 1.4rem;
      cursor: pointer;
      display: flex; align-items: center; justify-content: center;
      box-shadow: 0 0 30px rgba(0,224,255,0.3);
      transition: all 0.25s;
    }

    .c-btn-play:hover {
      transform: scale(1.1);
      box-shadow: 0 0 50px rgba(0,224,255,0.4);
    }

    .c-btn-play.playing {
      animation: playGlow 2.5s ease-in-out infinite;
    }

    @keyframes playGlow {
      0%,100% { box-shadow: 0 0 25px rgba(0,224,255,0.25); }
      50%     { box-shadow: 0 0 55px rgba(0,224,255,0.45), 0 0 90px rgba(123,95,255,0.15); }
    }

    /* ── VOLUME ROW ── */
    .vol-row {
      display: flex; align-items: center; gap: 10px;
      padding: 0 22px 10px;
    }

    .vol-icon {
      color: rgba(255,255,255,0.35);
      font-size: 0.85rem; cursor: pointer;
      transition: color 0.2s;
      min-width: 18px; text-align: center;
    }

    .vol-icon:hover { color: #00e0ff; }

    .vol-slider {
      flex: 1; -webkit-appearance: none; appearance: none;
      height: 3px; background: rgba(255,255,255,0.08);
      border-radius: 2px; outline: none;
      cursor: pointer;
    }

    .vol-slider::-webkit-slider-thumb {
      -webkit-appearance: none;
      width: 13px; height: 13px; border-radius: 50%;
      background: #00e0ff;
      cursor: pointer;
      box-shadow: 0 0 8px rgba(0,224,255,0.4);
    }

    .vol-pct {
      font-size: 0.65rem; font-weight: 600;
      color: rgba(255,255,255,0.3);
      min-width: 32px; text-align: right;
    }

    /* ── TABS ── */
    .tabs {
      display: flex;
      border-top: 1px solid rgba(255,255,255,0.04);
    }

    .tab {
      flex: 1; padding: 12px 0;
      background: transparent; border: none;
      color: rgba(255,255,255,0.3);
      font-size: 0.72rem; font-weight: 600;
      cursor: pointer; transition: all 0.25s;
      display: flex; align-items: center; justify-content: center; gap: 6px;
      border-bottom: 2px solid transparent;
    }

    .tab:hover { color: rgba(255,255,255,0.5); }

    .tab.active {
      color: #00e0ff;
      border-bottom-color: #00e0ff;
      background: rgba(0,224,255,0.04);
    }

    .tab i { font-size: 0.8rem; }

    /* ── TAB PANELS ── */
    .tab-panels {
      min-height: 0;
      overflow: hidden;
      transition: max-height 0.4s ease;
    }

    .tab-panel {
      display: none; padding: 16px 22px;
    }

    .tab-panel.active { display: block; }

    /* ── HISTORY LIST ── */
    .hist-list {
      display: flex; flex-direction: column; gap: 6px;
      max-height: 220px; overflow-y: auto;
    }

    .hist-list::-webkit-scrollbar { width: 3px; }
    .hist-list::-webkit-scrollbar-thumb { background: rgba(0,224,255,0.3); border-radius: 2px; }

    .hist-item {
      display: flex; align-items: center; gap: 10px;
      padding: 8px 10px;
      border-radius: 10px;
      background: rgba(255,255,255,0.02);
      border: 1px solid transparent;
      transition: all 0.2s;
    }

    .hist-item:hover {
      background: rgba(0,224,255,0.04);
      border-color: rgba(0,224,255,0.08);
    }

    .hist-item.now {
      background: rgba(0,224,255,0.06);
      border-color: rgba(0,224,255,0.12);
    }

    .hist-num {
      font-size: 0.65rem; font-weight: 700;
      color: rgba(255,255,255,0.2);
      min-width: 18px; text-align: center;
      font-variant-numeric: tabular-nums;
    }

    .hist-item.now .hist-num { color: #00e0ff; }

    .hist-art {
      width: 32px; height: 32px; border-radius: 6px;
      background: linear-gradient(135deg, rgba(0,224,255,0.15), rgba(199,96,255,0.15));
      display: flex; align-items: center; justify-content: center;
      color: rgba(0,224,255,0.6); font-size: 0.65rem; flex-shrink: 0;
      overflow: hidden;
    }

    .hist-art img { width: 100%; height: 100%; object-fit: cover; }

    .hist-info { flex: 1; min-width: 0; }

    .hist-title {
      font-size: 0.78rem; color: rgba(255,255,255,0.75);
      white-space: nowrap; overflow: hidden; text-overflow: ellipsis;
    }

    .hist-item.now .hist-title { color: #fff; font-weight: 600; }

    .hist-time {
      font-size: 0.62rem; color: rgba(255,255,255,0.25);
      min-width: 40px; text-align: right;
    }

    /* ── REQUEST FORM ── */
    .req-form {
      display: flex; flex-direction: column; gap: 10px;
    }

    .req-row {
      display: flex; gap: 8px;
    }

    .req-input {
      flex: 1; padding: 11px 14px;
      background: rgba(255,255,255,0.04);
      border: 1px solid rgba(255,255,255,0.08);
      border-radius: 10px;
      color: #fff; font-family: 'Inter', sans-serif;
      font-size: 0.82rem; outline: none;
      transition: border-color 0.25s;
    }

    .req-input::placeholder { color: rgba(255,255,255,0.2); }
    .req-input:focus { border-color: rgba(0,224,255,0.4); }

    .req-submit {
      width: 100%; padding: 12px;
      background: linear-gradient(135deg, #00e0ff, #7b5fff);
      border: none; border-radius: 10px;
      color: #fff; font-family: 'Inter', sans-serif;
      font-size: 0.82rem; font-weight: 700;
      cursor: pointer; letter-spacing: 1px;
      text-transform: uppercase;
      transition: all 0.25s;
    }

    .req-submit:hover {
      transform: translateY(-2px);
      box-shadow: 0 8px 25px rgba(0,224,255,0.2);
    }

    .req-submit:active { transform: translateY(0); }

    .req-msg-list {
      display: flex; flex-direction: column; gap: 8px;
      margin-top: 10px; max-height: 160px; overflow-y: auto;
    }

    .req-msg-list::-webkit-scrollbar { width: 3px; }
    .req-msg-list::-webkit-scrollbar-thumb { background: rgba(0,224,255,0.2); border-radius: 2px; }

    .req-msg-item {
      padding: 10px 12px;
      background: rgba(0,224,255,0.04);
      border: 1px solid rgba(0,224,255,0.08);
      border-radius: 10px;
      animation: fadeInUp 0.3s ease;
    }

    .req-msg-item .rm-header {
      display: flex; align-items: center; justify-content: space-between;
      margin-bottom: 4px;
    }

    .req-msg-item .rm-name {
      font-size: 0.7rem; font-weight: 700; color: #00e0ff;
    }

    .req-msg-item .rm-time {
      font-size: 0.58rem; color: rgba(255,255,255,0.2);
    }

    .req-msg-item .rm-song {
      font-size: 0.78rem; color: rgba(255,255,255,0.7);
      font-weight: 500;
    }

    .req-msg-item .rm-note {
      font-size: 0.7rem; color: rgba(255,255,255,0.35);
      margin-top: 2px; font-style: italic;
    }

    @keyframes fadeInUp {
      from { opacity: 0; transform: translateY(8px); }
      to   { opacity: 1; transform: translateY(0); }
    }

    /* ── VISUALIZER ── */
    .vis-canvas {
      width: 100%; height: 60px;
      display: block;
    }

    /* ── EQUALIZER ── */
    .eq-row {
      display: flex; justify-content: space-between;
      padding: 12px 22px 16px;
      border-top: 1px solid rgba(255,255,255,0.03);
    }

    .eq-bar {
      flex: 1; display: flex; flex-direction: column;
      align-items: center; gap: 4px;
    }

    .eq-slider {
      -webkit-appearance: none; appearance: none;
      width: 3px; height: 50px;
      background: rgba(255,255,255,0.06);
      border-radius: 2px; outline: none;
      writing-mode: vertical-lr; direction: rtl; cursor: pointer;
    }

    .eq-slider::-webkit-slider-thumb {
      -webkit-appearance: none;
      width: 10px; height: 10px; border-radius: 50%;
      background: #00e0ff; cursor: pointer;
    }

    .eq-lbl {
      font-size: 0.52rem; color: rgba(255,255,255,0.2);
      font-weight: 500;
    }

    /* ── TOAST ── */
    .toast {
      position: fixed; bottom: 30px; left: 50%;
      transform: translateX(-50%) translateY(20px);
      padding: 10px 22px;
      background: rgba(0,224,255,0.12);
      border: 1px solid rgba(0,224,255,0.25);
      backdrop-filter: blur(20px);
      border-radius: 25px;
      font-size: 0.8rem; color: #00e0ff;
      z-index: 999;
      opacity: 0; pointer-events: none;
      transition: all 0.35s ease;
      white-space: nowrap;
    }

    .toast.show {
      opacity: 1;
      transform: translateX(-50%) translateY(0);
    }

    /* ── RESPONSIVE ── */
    @media (max-width: 480px) {
      body { padding: 10px; }
      .widget { border-radius: 18px; }
      .cover-art { width: 110px; height: 110px; }
      .track-title { font-size: 1rem; }
      .controls { gap: 12px; padding: 14px 16px; }
      .c-btn { width: 38px; height: 38px; font-size: 0.8rem; }
      .c-btn-play { width: 52px; height: 52px; font-size: 1.2rem; }
      .track-info { padding: 14px 16px 4px; }
      .vol-row { padding: 0 16px 10px; }
      .req-form { padding: 0; }
    }
  </style>
</head>
<body>

  <!-- Background -->
  <div class="bg-anim">
    <div class="blob"></div>
    <div class="blob"></div>
    <div class="blob"></div>
  </div>

  <!-- ══════════ WIDGET ══════════ -->
  <div class="widget" id="widget">

    <!-- LIVE BAR -->
    <div class="live-bar">
      <div class="dot"></div>
      CANLI YAYIN
      <span class="listeners" id="liveCount">• 0 dinleyici</span>
    </div>

    <!-- SCROLLING TEXT (Kayan Yazı) -->
    <div class="scroll-strip">
      <div class="scroll-track" id="scrollTrack">
        <!-- JS doldurur -->
      </div>
    </div>

    <!-- COVER ART -->
    <div class="cover-section">
      <img src="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 400 250'><rect fill='%23050510' width='400' height='250'/><text fill='%2300e0ff' x='50%25' y='50%25' text-anchor='middle' font-size='60' dy='.3em'>📡</text></svg>"
           class="cover-bg" id="coverBg">
      <div class="cover-overlay">
        <div class="cover-glow" id="coverGlow"></div>
        <img src="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 200 200'><rect fill='%23050520' width='200' height='200'/><text fill='%2300e0ff' x='50%25' y='50%25' text-anchor='middle' font-size='50' dy='.3em'>🎵</text></svg>"
             class="cover-art" id="coverArt">
      </div>
      <div class="cover-bars paused" id="coverBars">
        <span></span><span></span><span></span><span></span><span></span>
      </div>
      <div class="q-badge" id="qBadge">128kbps</div>
    </div>

    <!-- TRACK INFO -->
    <div class="track-info">
      <div class="track-label">🎵 Çalıyor</div>
      <div class="track-title" id="trackTitle">Yükleniyor...</div>
      <div class="track-artist" id="trackArtist">Galactic Wave Radio</div>
    </div>

    <!-- PROGRESS -->
    <div class="progress-area">
      <div class="prog-track" id="progTrack">
        <div class="prog-fill" id="progFill">
          <div class="prog-thumb"></div>
        </div>
      </div>
      <div class="prog-times">
        <span id="tElapsed">0:00</span>
        <span id="tTotal">~4:00</span>
      </div>
    </div>

    <!-- CONTROLS -->
    <div class="controls">
      <button class="c-btn" id="btnShuffle" title="Karıştır"><i class="fas fa-random"></i></button>
      <button class="c-btn" id="btnPrev" title="Önceki"><i class="fas fa-step-backward"></i></button>
      <button class="c-btn-play" id="btnPlay" title="Oynat / Duraklat">
        <i class="fas fa-play" id="playIcon"></i>
      </button>
      <button class="c-btn" id="btnNext" title="Sonraki"><i class="fas fa-step-forward"></i></button>
      <button class="c-btn" id="btnLike" title="Beğen"><i class="far fa-heart"></i></button>
    </div>

    <!-- VOLUME -->
    <div class="vol-row">
      <i class="fas fa-volume-up vol-icon" id="volIcon"></i>
      <input type="range" class="vol-slider" id="volSlider" min="0" max="100" value="75">
      <span class="vol-pct" id="volPct">75%</span>
    </div>

    <!-- VISUALIZER -->
    <canvas class="vis-canvas" id="visCanvas"></canvas>

    <!-- TABS -->
    <div class="tabs">
      <button class="tab active" data-tab="history">
        <i class="fas fa-history"></i> Son Çalınan
      </button>
      <button class="tab" data-tab="request">
        <i class="fas fa-magic"></i> İstek
      </button>
    </div>

    <!-- TAB PANELS -->
    <div class="tab-panels">

      <!-- History -->
      <div class="tab-panel active" id="panelHistory">
        <div class="hist-list" id="histList">
          <div style="text-align:center;padding:30px;color:rgba(255,255,255,0.15);font-size:0.8rem;">
            <i class="fas fa-spinner fa-spin" style="margin-right:8px;"></i> Yükleniyor...
          </div>
        </div>
      </div>

      <!-- Request -->
      <div class="tab-panel" id="panelRequest">
        <div class="req-form">
          <input type="text" class="req-input" id="reqSong"
                 placeholder="🎵 Şarkı adı veya sanatçı..." maxlength="120">
          <div class="req-row">
            <input type="text" class="req-input" id="reqName"
                   placeholder="👤 İsim (opsiyonel)" maxlength="40">
            <input type="text" class="req-input" id="reqMsg"
                   placeholder="💬 Mesaj" maxlength="150">
          </div>
          <button class="req-submit" id="reqSubmit">
            <i class="fas fa-paper-plane"></i> İSTEK GÖNDER
          </button>
        </div>
        <div class="req-msg-list" id="reqMsgList"></div>
      </div>

    </div>

  </div>

  <!-- Toast -->
  <div class="toast" id="toast"><i class="fas fa-check-circle" style="margin-right:6px;"></i><span id="toastText"></span></div>

  <!-- Audio -->
  <audio id="audio" preload="none" crossorigin="anonymous">
    <source src="https://radyocast.com/8028/Stream" type="audio/mpeg">
  </audio>

  <script>
    // ═══════════════════════════════════════════════════════
    // CONFIG
    // ═══════════════════════════════════════════════════════
    const CFG = {
      API:      'https://radyocast.com/cp/get_info.php?p=8028',
      STREAM:   'https://radyocast.com/8028/Stream',
      REFRESH:  8000,
      VIS_FPS:  25,
      DURATION: 240,
      EQ:       [128, 256, 512, 1024, 2048, 4096, 8192, 16384]
    };

    // ═══════════════════════════════════════════════════════
    // STATE
    // ═══════════════════════════════════════════════════════
    const S = {
      playing:    false,
      volume:     75,
      liked:      false,
      shuffle:    false,
      elapsed:    0,
      timer:      null,
      visT:       null,
      scrollMsgs: [],
      history:    [],
      requests:   []
    };

    // ═══════════════════════════════════════════════════════
    // DOM
    // ═══════════════════════════════════════════════════════
    const $ = s => document.querySelector(s);

    const D = {
      audio:       $('#audio'),
      coverBg:     $('#coverBg'),
      coverArt:    $('#coverArt'),
      coverBars:   $('#coverBars'),
      qBadge:      $('#qBadge'),
      trackTitle:  $('#trackTitle'),
      trackArtist: $('#trackArtist'),
      progFill:    $('#progFill'),
      tElapsed:    $('#tElapsed'),
      tTotal:      $('#tTotal'),
      btnPlay:     $('#btnPlay'),
      playIcon:    $('#playIcon'),
      btnShuffle:  $('#btnShuffle'),
      btnPrev:     $('#btnPrev'),
      btnNext:     $('#btnNext'),
      btnLike:     $('#btnLike'),
      volSlider:   $('#volSlider'),
      volPct:      $('#volPct'),
      volIcon:     $('#volIcon'),
      visCanvas:   $('#visCanvas'),
      visCtx:      null,
      liveCount:   $('#liveCount'),
      scrollTrack: $('#scrollTrack'),
      histList:    $('#histList'),
      reqSong:     $('#reqSong'),
      reqName:     $('#reqName'),
      reqMsg:      $('#reqMsg'),
      reqSubmit:   $('#reqSubmit'),
      reqMsgList:  $('#reqMsgList'),
      toast:       $('#toast'),
      toastText:   $('#toastText')
    };

    // ═══════════════════════════════════════════════════════
    // TOAST
    // ═══════════════════════════════════════════════════════
    function toast(msg) {
      D.toastText.textContent = msg;
      D.toast.classList.add('show');
      clearTimeout(D.toast._t);
      D.toast._t = setTimeout(() => D.toast.classList.remove('show'), 2800);
    }

    // ═══════════════════════════════════════════════════════
    // ESCAPE
    // ═══════════════════════════════════════════════════════
    function esc(s) {
      const d = document.createElement('div');
      d.textContent = s || '';
      return d.innerHTML;
    }

    // ═══════════════════════════════════════════════════════
    // API FETCH
    // ═══════════════════════════════════════════════════════
    async function fetchAPI() {
      try {
        const r = await fetch(CFG.API + '&t=' + Date.now());
        if (!r.ok) return;
        const data = await r.json();
        updateUI(data);
      } catch(e) { console.warn('API:', e.message); }
    }

    function updateUI(d) {
      const title   = d.title || 'Bilinmiyor';
      const art     = d.art || '';
      const online  = parseInt(d.listeners || 0);
      const bitrate = d.bitrate || '128';

      // Albüm resmi
      if (art) {
        D.coverArt.src = art;
        D.coverBg.src = art;
      }

      // Başlık
      const parts = title.split(' - ');
      if (parts.length >= 2) {
        D.trackArtist.textContent = parts[0].trim();
        D.trackTitle.textContent = parts.slice(1).join(' - ').trim();
      } else {
        D.trackTitle.textContent = title;
        D.trackArtist.textContent = 'Galactic Wave Radio';
      }

      // Bitrate
      D.qBadge.textContent = bitrate + 'kbps';

      // Dinleyici
      D.liveCount.textContent = '• ' + online + ' dinleyici';

      // History
      if (d.history && d.history.length) {
        updateHistory(d.history);
      }

      // Scrolling text güncelle
      if (d.history && d.history.length) {
        buildScrollText(d.history);
      }
    }

    // ═══════════════════════════════════════════════════════
    // HISTORY
    // ═══════════════════════════════════════════════════════
    function updateHistory(items) {
      S.history = items;
      D.histList.innerHTML = items.map((item, i) => {
        const name = typeof item === 'string' ? item : (item.title || 'Bilinmiyor');
        const time = typeof item === 'string' ? '' : (item.time || '');
        return `
          <div class="hist-item ${i===0 ? 'now' : ''}">
            <span class="hist-num">${i===0 ? '▶' : i+1}</span>
            <div class="hist-art"><i class="fas fa-music"></i></div>
            <div class="hist-info">
              <div class="hist-title">${esc(name)}</div>
            </div>
            ${time ? `<span class="hist-time">${esc(time)}</span>` : ''}
          </div>
        `;
      }).join('');
    }

    // ═══════════════════════════════════════════════════════
    // SCROLLING TEXT (Kayan Yazı Alanı)
    // ═══════════════════════════════════════════════════════
    function buildScrollText(items) {
      const msgs = [
        '🎧 Dinlediğiniz için teşekkürler',
        '💜 Şarkı isteklerinizi bekliyoruz',
        '📡 Canlı yayın 7/24',
        '🌟 Galactic Wave Radio',
        '🎵 Müzik evrenin ortak dili',
      ];

      // History şarkılarını ekle
      items.slice(0, 5).forEach(item => {
        const name = typeof item === 'string' ? item : item.title;
        if (name) msgs.push('🎵 ' + name);
      });

      // User mesajlarını ekle
      S.requests.forEach(r => {
        if (r.song) msgs.push('📨 ' + r.name + ': ' + r.song);
      });

      buildMarquee(msgs);
    }

    function buildMarquee(messages) {
      let itemsHTML = messages.map(m =>
        `<span class="scroll-item">${esc(m)}</span><span class="scroll-sep">✦</span>`
      ).join('');

      // Çift kez kopyala (sonsuz marquee için)
      D.scrollTrack.innerHTML = itemsHTML + itemsHTML;
      const dur = Math.max(15, messages.length * 5);
      D.scrollTrack.style.setProperty('--speed', dur + 's');
    }

    // ═══════════════════════════════════════════════════════
    // PLAY / PAUSE
    // ═══════════════════════════════════════════════════════
    function togglePlay() {
      S.playing = !S.playing;

      if (S.playing) {
        D.audio.src = CFG.STREAM;
        D.audio.volume = S.volume / 100;
        D.audio.play().catch(() => {});

        D.playIcon.className = 'fas fa-pause';
        D.btnPlay.classList.add('playing');
        D.coverBars.classList.remove('paused');

        startProgress();
        startVis();
        toast('▶ Yayına bağlanılıyor...');
      } else {
        D.audio.pause();
        D.playIcon.className = 'fas fa-play';
        D.btnPlay.classList.remove('playing');
        D.coverBars.classList.add('paused');

        stopProgress();
        stopVis();
        toast('⏸ Duraklatıldı');
      }
    }

    // ═══════════════════════════════════════════════════════
    // PROGRESS
    // ═══════════════════════════════════════════════════════
    function startProgress() {
      S.elapsed = 0;
      clearInterval(S.timer);
      S.timer = setInterval(() => {
        if (!S.playing) return;
        S.elapsed++;
        const pct = (S.elapsed / CFG.DURATION) * 100;
        D.progFill.style.width = pct + '%';
        D.tElapsed.textContent = fmt(S.elapsed);
        if (S.elapsed >= CFG.DURATION) S.elapsed = 0;
      }, 1000);
    }

    function stopProgress() { clearInterval(S.timer); }

    function fmt(s) {
      return Math.floor(s / 60) + ':' + String(s % 60).padStart(2, '0');
    }

    // ═══════════════════════════════════════════════════════
    // VISUALIZER
    // ═══════════════════════════════════════════════════════
    function initVis() {
      D.visCtx = D.visCanvas.getContext('2d');
      resizeVis();
      window.addEventListener('resize', resizeVis);
    }

    function resizeVis() {
      const c = D.visCanvas;
      c.width = c.offsetWidth * 2;
      c.height = c.offsetHeight * 2;
      D.visCtx.scale(2, 2);
    }

    function startVis() {
      if (S.visT) return;
      S.visT = setInterval(drawVis, 1000 / CFG.VIS_FPS);
    }

    function stopVis() {
      clearInterval(S.visT);
      S.visT = null;
      if (D.visCtx) {
        const c = D.visCanvas;
        D.visCtx.clearRect(0, 0, c.offsetWidth, c.offsetHeight);
      }
    }

    function drawVis() {
      if (!D.visCtx || !S.playing) return;
      const ctx = D.visCtx;
      const w = D.visCanvas.offsetWidth;
      const h = D.visCanvas.offsetHeight;
      ctx.clearRect(0, 0, w, h);

      const bars = 36;
      const bw = w / bars;

      for (let i = 0; i < bars; i++) {
        const bh = Math.random() * h * 0.85 + h * 0.05;
        const x = i * bw + 1;
        const y = h - bh;

        const g = ctx.createLinearGradient(x, y, x, h);
        g.addColorStop(0, '#00e0ff');
        g.addColorStop(0.6, '#7b5fff');
        g.addColorStop(1, 'rgba(123,95,255,0.2)');

        ctx.fillStyle = g;
        ctx.beginPath();
        ctx.roundRect(x, y, bw - 2, bh, 2);
        ctx.fill();
      }
    }

    // ═══════════════════════════════════════════════════════
    // VOLUME
    // ═══════════════════════════════════════════════════════
    function setVol(v) {
      v = Math.max(0, Math.min(100, parseInt(v)));
      S.volume = v;
      D.volSlider.value = v;
      D.volPct.textContent = v + '%';
      D.audio.volume = v / 100;

      if (v === 0) D.volIcon.className = 'fas fa-volume-mute vol-icon';
      else if (v < 30) D.volIcon.className = 'fas fa-volume-off vol-icon';
      else if (v < 70) D.volIcon.className = 'fas fa-volume-down vol-icon';
      else D.volIcon.className = 'fas fa-volume-up vol-icon';
    }

    // ═══════════════════════════════════════════════════════
    // LIKE
    // ═══════════════════════════════════════════════════════
    function toggleLike() {
      S.liked = !S.liked;
      const icon = D.btnLike.querySelector('i');
      if (S.liked) {
        icon.className = 'fas fa-heart';
        D.btnLike.classList.add('like-active');
        toast('❤️ Beğenildi!');
      } else {
        icon.className = 'far fa-heart';
        D.btnLike.classList.remove('like-active');
        toast('💔 Beğeni kaldırıldı');
      }
    }

    // ═══════════════════════════════════════════════════════
    // REQUEST
    // ═══════════════════════════════════════════════════════
    function sendRequest() {
      const song = D.reqSong.value.trim();
      if (!song) {
        toast('⚠ Şarkı adı girin!');
        D.reqSong.focus();
        return;
      }

      const name = D.reqName.value.trim() || 'Misafir';
      const msg  = D.reqMsg.value.trim();
      const now  = new Date();
      const time = now.getHours().toString().padStart(2,'0') + ':' + now.getMinutes().toString().padStart(2,'0');

      const req = { song, name, msg, time };
      S.requests.unshift(req);

      // Kayan metne ekle
      buildScrollText(S.history.length ? S.history : []);

      // Mesaj listesine ekle
      const html = `
        <div class="req-msg-item">
          <div class="rm-header">
            <span class="rm-name"><i class="fas fa-user" style="margin-right:5px;"></i>${esc(name)}</span>
            <span class="rm-time">${esc(time)}</span>
          </div>
          <div class="rm-song"><i class="fas fa-music" style="margin-right:6px;color:#00e0ff;font-size:0.7rem;"></i>${esc(song)}</div>
          ${msg ? `<div class="rm-note">"${esc(msg)}"</div>` : ''}
        </div>
      `;
      D.reqMsgList.insertAdjacentHTML('afterbegin', html);

      D.reqSong.value = '';
      D.reqName.value = '';
      D.reqMsg.value = '';

      toast('🎵 İsteğiniz gönderildi!');
    }

    // ═══════════════════════════════════════════════════════
    // TABS
    // ═══════════════════════════════════════════════════════
    function initTabs() {
      document.querySelectorAll('.tab').forEach(tab => {
        tab.addEventListener('click', () => {
          document.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));
          document.querySelectorAll('.tab-panel').forEach(p => p.classList.remove('active'));
          tab.classList.add('active');
          $('#panel' + tab.dataset.tab.charAt(0).toUpperCase() + tab.dataset.tab.slice(1))
            .classList.add('active');
        });
      });
    }

    // ═══════════════════════════════════════════════════════
    // PROGRESS BAR CLICK
    // ═══════════════════════════════════════════════════════
    function initProgressClick() {
      $('#progTrack').addEventListener('click', e => {
        const rect = e.currentTarget.getBoundingClientRect();
        const pct = ((e.clientX - rect.left) / rect.width) * 100;
        D.progFill.style.width = pct + '%';
        S.elapsed = Math.round((pct / 100) * CFG.DURATION);
        D.tElapsed.textContent = fmt(S.elapsed);
      });
    }

    // ═══════════════════════════════════════════════════════
    // KEYBOARD
    // ═══════════════════════════════════════════════════════
    function initKeys() {
      document.addEventListener('keydown', e => {
        if (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA') return;
        switch (e.key) {
          case ' ':
            e.preventDefault();
            togglePlay();
            break;
          case 'ArrowUp':
            e.preventDefault();
            setVol(S.volume + 5);
            break;
          case 'ArrowDown':
            e.preventDefault();
            setVol(S.volume - 5);
            break;
          case 'm': case 'M':
            D.volIcon.click();
            break;
          case 'l': case 'L':
            toggleLike();
            break;
        }
      });
    }

    // ═══════════════════════════════════════════════════════
    // EVENTS
    // ═══════════════════════════════════════════════════════
    function bindEvents() {
      D.btnPlay.addEventListener('click', togglePlay);

      D.volSlider.addEventListener('input', e => setVol(e.target.value));
      D.volIcon.addEventListener('click', () => setVol(S.volume > 0 ? 0 : 75));

      D.btnLike.addEventListener('click', toggleLike);

      D.btnShuffle.addEventListener('click', () => {
        S.shuffle = !S.shuffle;
        D.btnShuffle.classList.toggle('active', S.shuffle);
        toast(S.shuffle ? '🔀 Karıştırma açık' : '🔀 Karıştırma kapalı');
      });

      D.btnPrev.addEventListener('click', () => { S.elapsed = 0; toast('⏮ Önceki'); });
      D.btnNext.addEventListener('click', () => { S.elapsed = 0; toast('⏭ Sonraki'); });

      D.reqSubmit.addEventListener('click', sendRequest);
      D.reqSong.addEventListener('keydown', e => { if (e.key === 'Enter') sendRequest(); });

      D.audio.addEventListener('playing', () => {
        D.btnPlay.classList.add('playing');
      });

      D.audio.addEventListener('error', () => {
        if (S.playing) {
          toast('⚠ Bağlantı hatası, tekrar deneniyor...');
          setTimeout(() => {
            D.audio.src = CFG.STREAM + '?t=' + Date.now();
            D.audio.play().catch(() => {});
          }, 3000);
        }
      });
    }

    // ═══════════════════════════════════════════════════════
    // INIT
    // ═══════════════════════════════════════════════════════
    function init() {
      // Başlangıç kayan metni
      buildMarquee([
        '🎧 Dinlediğiniz için teşekkürler',
        '💜 Şarkı isteklerinizi bekliyoruz',
        '📡 Canlı yayın 7/24',
        '🌟 Galactic Wave Radio',
        '🎵 Müzik evrenin ortak dili'
      ]);

      initVis();
      initTabs();
      initProgressClick();
      initKeys();
      bindEvents();
      setVol(75);

      // API
      fetchAPI();
      setInterval(fetchAPI, CFG.REFRESH);
    }

    document.addEventListener('DOMContentLoaded', init);
  </script>
</body>
</html>
```

---

## ✅ Özellikler

| Özellik | Detay |
|---------|-------|
| **📻 Stream** | `https://radyocast.com/8028/Stream` doğrudan entegre |
| **📡 API** | Otomatik 8sn refresh ile şarkı bilgisi |
| **⏭ Kayan Yazı** | İstek mesajları + son çalınanlar + varsayılan mesajlar |
| **📨 İstek Formu** | Şarkı adı, isim, mesaj — anında kayan yazıya eklenir |
| **📊 Visualizer** | Canvas tabanlı 36 bant animasyon |
| **❤️ Beğen** | Tek dokunuşla şarkı beğenme |
| **🔀 Karıştır** | Shuffle modu |
| **📱 Mobil** | Tam responsive, max 460px widget |
| **⌨️ Kısayollar** | Space, ↑↓, M, L |

> **Tek dosya** — tüm CSS + JS + HTML dahil, harici bağımlılık yok (sadece Google Fonts + Font Awesome CDN).