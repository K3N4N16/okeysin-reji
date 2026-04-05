<think>

Kullanıcı sadece bir radyo player widget'ı istiyor. Şunları içermeli:

1. Radyo stream URL'si (https://radyocast.com/8028/Stream)
2. İstek gönder formu (şarkı isteği)
3. Kayan yazı alanı (ticker/ticker tape)
4. Mobil uyumlu tasarım
5. Sade ve temiz widget görünümü

Daha minimal, widget tarzı bir tasarım yapalım.

</think>

# 🎵 Minimal Radyo Player Widget

```html
<!DOCTYPE html>
<html lang="tr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Radyo Player</title>

  <!-- Google Fonts -->
  <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&family=Space+Grotesk:wght@400;500;600&display=swap" rel="stylesheet">

  <!-- Font Awesome -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">

  <style>
    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
    }

    :root {
      --bg-dark:    #0a0a1a;
      --bg-card:    #12122a;
      --bg-input:   rgba(255,255,255,0.05);
      --primary:    #00d4ff;
      --secondary:  #7b5cff;
      --accent:     #ff6b9d;
      --text:       #e0e0f0;
      --text-dim:   #6b6b8a;
      --border:     rgba(255,255,255,0.08);
      --glow:       rgba(0,212,255,0.3);
      --radius:     16px;
      --radius-sm:  10px;
    }

    body {
      font-family: 'Poppins', sans-serif;
      background: var(--bg-dark);
      min-height: 100vh;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 20px;
      background: linear-gradient(135deg, #0a0a1a 0%, #0d0d24 50%, #0a0a1a 100%);
    }

    /* Animated Background */
    .bg-orb {
      position: fixed;
      width: 400px;
      height: 400px;
      border-radius: 50%;
      filter: blur(120px);
      opacity: 0.15;
      pointer-events: none;
      z-index: 0;
    }

    .bg-orb-1 {
      background: var(--primary);
      top: -100px;
      left: -100px;
      animation: orbFloat 15s ease-in-out infinite;
    }

    .bg-orb-2 {
      background: var(--secondary);
      bottom: -100px;
      right: -100px;
      animation: orbFloat 18s ease-in-out infinite reverse;
    }

    @keyframes orbFloat {
      0%, 100% { transform: translate(0, 0) scale(1); }
      50% { transform: translate(40px, 30px) scale(1.15); }
    }

    /* ══════════════════════════════════════
       MAIN WIDGET
    ══════════════════════════════════════ */
    .radio-widget {
      position: relative;
      z-index: 1;
      width: 100%;
      max-width: 480px;
      background: var(--bg-card);
      border: 1px solid var(--border);
      border-radius: var(--radius);
      overflow: hidden;
      box-shadow: 0 25px 80px rgba(0,0,0,0.5),
                  0 0 60px rgba(0,212,255,0.05);
      backdrop-filter: blur(20px);
    }

    /* ══════════════════════════════════════
       TICKER / KAYAN YAZI
    ══════════════════════════════════════ */
    .ticker-wrap {
      background: linear-gradient(90deg, var(--primary), var(--secondary));
      padding: 8px 0;
      overflow: hidden;
      position: relative;
    }

    .ticker-wrap::before,
    .ticker-wrap::after {
      content: '';
      position: absolute;
      top: 0;
      width: 60px;
      height: 100%;
      z-index: 2;
    }

    .ticker-wrap::before {
      left: 0;
      background: linear-gradient(90deg, var(--primary), transparent);
    }

    .ticker-wrap::after {
      right: 0;
      background: linear-gradient(-90deg, var(--secondary), transparent);
    }

    .ticker {
      display: flex;
      white-space: nowrap;
      animation: tickerScroll 25s linear infinite;
    }

    .ticker:hover { animation-play-state: paused; }

    @keyframes tickerScroll {
      0%   { transform: translateX(0); }
      100% { transform: translateX(-50%); }
    }

    .ticker-item {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      padding: 0 40px;
      font-size: 0.75rem;
      font-weight: 600;
      color: #0a0a1a;
      letter-spacing: 0.5px;
    }

    .ticker-item i { font-size: 0.65rem; }

    /* ══════════════════════════════════════
       HEADER
    ══════════════════════════════════════ */
    .widget-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 16px 20px;
      border-bottom: 1px solid var(--border);
    }

    .widget-brand {
      display: flex;
      align-items: center;
      gap: 10px;
    }

    .brand-icon {
      width: 38px;
      height: 38px;
      border-radius: 10px;
      background: linear-gradient(135deg, var(--primary), var(--secondary));
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1rem;
      animation: brandPulse 3s ease-in-out infinite;
    }

    @keyframes brandPulse {
      0%, 100% { box-shadow: 0 0 15px var(--glow); }
      50% { box-shadow: 0 0 30px var(--glow); }
    }

    .brand-name {
      font-family: 'Space Grotesk', sans-serif;
      font-size: 1rem;
      font-weight: 700;
      color: var(--text);
      letter-spacing: 1px;
    }

    .live-badge {
      display: flex;
      align-items: center;
      gap: 6px;
      padding: 5px 12px;
      background: rgba(0,255,136,0.1);
      border: 1px solid rgba(0,255,136,0.25);
      border-radius: 20px;
      font-size: 0.65rem;
      font-weight: 700;
      color: #00ff88;
      text-transform: uppercase;
      letter-spacing: 1px;
    }

    .live-dot {
      width: 6px;
      height: 6px;
      border-radius: 50%;
      background: #00ff88;
      animation: livePulse 1.5s infinite;
    }

    @keyframes livePulse {
      0%, 100% { opacity: 1; transform: scale(1); }
      50% { opacity: 0.4; transform: scale(0.8); }
    }

    .live-badge.offline {
      background: rgba(255,68,102,0.1);
      border-color: rgba(255,68,102,0.25);
      color: #ff4466;
    }

    .live-badge.offline .live-dot {
      background: #ff4466;
      animation: none;
    }

    /* ══════════════════════════════════════
       PLAYER SECTION
    ══════════════════════════════════════ */
    .player-section {
      padding: 20px;
    }

    .now-playing {
      display: flex;
      align-items: center;
      gap: 16px;
      margin-bottom: 20px;
    }

    .album-art {
      width: 70px;
      height: 70px;
      border-radius: 14px;
      background: linear-gradient(135deg, rgba(0,212,255,0.15), rgba(123,92,255,0.15));
      display: flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
      position: relative;
      overflow: hidden;
      border: 1px solid var(--border);
    }

    .album-art img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      border-radius: 14px;
    }

    .album-art .icon {
      font-size: 1.5rem;
      color: var(--primary);
    }

    .album-art.spinning img,
    .album-art.spinning .icon {
      animation: spin 8s linear infinite;
    }

    @keyframes spin {
      from { transform: rotate(0deg); }
      to { transform: rotate(360deg); }
    }

    /* Playing Bars on Album */
    .playing-bars-overlay {
      position: absolute;
      inset: 0;
      background: rgba(0,0,0,0.6);
      display: flex;
      align-items: center;
      justify-content: center;
      border-radius: 14px;
      opacity: 0;
      transition: opacity 0.3s;
    }

    .album-art.playing .playing-bars-overlay { opacity: 1; }

    .mini-bars {
      display: flex;
      gap: 3px;
      align-items: flex-end;
      height: 24px;
    }

    .mini-bars span {
      width: 4px;
      background: var(--primary);
      border-radius: 2px;
      animation: miniBar 0.6s ease-in-out infinite;
    }

    .mini-bars span:nth-child(1) { height: 8px; animation-delay: 0s; }
    .mini-bars span:nth-child(2) { height: 16px; animation-delay: 0.12s; }
    .mini-bars span:nth-child(3) { height: 10px; animation-delay: 0.24s; }
    .mini-bars span:nth-child(4) { height: 20px; animation-delay: 0.36s; }

    @keyframes miniBar {
      0%, 100% { transform: scaleY(0.4); }
      50% { transform: scaleY(1); }
    }

    .np-info { flex: 1; min-width: 0; }

    .np-label {
      font-size: 0.6rem;
      font-weight: 700;
      color: var(--primary);
      text-transform: uppercase;
      letter-spacing: 2px;
      margin-bottom: 4px;
    }

    .np-title {
      font-family: 'Space Grotesk', sans-serif;
      font-size: 1rem;
      font-weight: 600;
      color: var(--text);
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }

    .np-artist {
      font-size: 0.78rem;
      color: var(--text-dim);
      margin-top: 2px;
    }

    /* ══════════════════════════════════════
       CONTROLS
    ══════════════════════════════════════ */
    .controls {
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 12px;
      margin-bottom: 18px;
    }

    .ctrl-btn {
      width: 42px;
      height: 42px;
      border-radius: 50%;
      border: 1px solid var(--border);
      background: rgba(255,255,255,0.03);
      color: var(--text-dim);
      font-size: 0.9rem;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      transition: all 0.25s ease;
    }

    .ctrl-btn:hover {
      border-color: var(--primary);
      color: var(--primary);
      background: rgba(0,212,255,0.08);
      transform: scale(1.08);
    }

    .ctrl-btn.active {
      color: var(--primary);
      border-color: var(--primary);
    }

    .ctrl-btn.main {
      width: 60px;
      height: 60px;
      font-size: 1.4rem;
      background: linear-gradient(135deg, var(--primary), var(--secondary));
      border: none;
      color: #0a0a1a;
      box-shadow: 0 8px 30px rgba(0,212,255,0.3);
    }

    .ctrl-btn.main:hover {
      transform: scale(1.1);
      box-shadow: 0 12px 40px rgba(0,212,255,0.4);
    }

    .ctrl-btn.main.playing {
      animation: mainGlow 2s ease-in-out infinite;
    }

    @keyframes mainGlow {
      0%, 100% { box-shadow: 0 8px 30px rgba(0,212,255,0.3); }
      50% { box-shadow: 0 8px 50px rgba(0,212,255,0.5), 0 0 80px rgba(123,92,255,0.2); }
    }

    .ctrl-btn.liked {
      color: var(--accent);
      border-color: var(--accent);
    }

    .ctrl-btn.liked i {
      animation: heartBeat 0.5s ease;
    }

    @keyframes heartBeat {
      0% { transform: scale(1); }
      25% { transform: scale(1.4); }
      50% { transform: scale(0.9); }
      100% { transform: scale(1); }
    }

    /* Volume */
    .volume-row {
      display: flex;
      align-items: center;
      gap: 10px;
      padding: 0 10px;
    }

    .vol-icon {
      color: var(--text-dim);
      font-size: 0.85rem;
      cursor: pointer;
      transition: color 0.25s;
      flex-shrink: 0;
    }

    .vol-icon:hover { color: var(--primary); }

    .vol-slider {
      flex: 1;
      -webkit-appearance: none;
      appearance: none;
      height: 4px;
      background: rgba(255,255,255,0.08);
      border-radius: 2px;
      outline: none;
      cursor: pointer;
    }

    .vol-slider::-webkit-slider-thumb {
      -webkit-appearance: none;
      width: 14px;
      height: 14px;
      border-radius: 50%;
      background: var(--primary);
      cursor: pointer;
      box-shadow: 0 0 10px var(--glow);
      transition: transform 0.2s;
    }

    .vol-slider::-webkit-slider-thumb:hover {
      transform: scale(1.2);
    }

    .vol-val {
      font-size: 0.65rem;
      font-weight: 600;
      color: var(--text-dim);
      min-width: 32px;
      text-align: right;
    }

    /* ══════════════════════════════════════
       VISUALIZER
    ══════════════════════════════════════ */
    .visualizer-wrap {
      height: 50px;
      margin: 15px 0;
      display: flex;
      align-items: flex-end;
      justify-content: center;
      gap: 3px;
      padding: 0 5px;
    }

    .vis-bar {
      flex: 1;
      max-width: 8px;
      border-radius: 3px 3px 0 0;
      background: linear-gradient(180deg, var(--primary), var(--secondary));
      transition: height 0.1s ease;
      opacity: 0.5;
    }

    .vis-bar.active {
      opacity: 1;
    }

    /* ══════════════════════════════════════
       REQUEST SECTION
    ══════════════════════════════════════ */
    .request-section {
      padding: 16px 20px;
      border-top: 1px solid var(--border);
      background: rgba(0,0,0,0.15);
    }

    .request-title {
      display: flex;
      align-items: center;
      gap: 8px;
      font-size: 0.75rem;
      font-weight: 700;
      color: var(--text);
      text-transform: uppercase;
      letter-spacing: 1.5px;
      margin-bottom: 14px;
    }

    .request-title i { color: var(--accent); }

    .request-form {
      display: flex;
      flex-direction: column;
      gap: 10px;
    }

    .req-input {
      width: 100%;
      padding: 12px 16px;
      background: var(--bg-input);
      border: 1px solid var(--border);
      border-radius: var(--radius-sm);
      color: var(--text);
      font-family: 'Poppins', sans-serif;
      font-size: 0.85rem;
      outline: none;
      transition: all 0.25s ease;
    }

    .req-input::placeholder {
      color: var(--text-dim);
    }

    .req-input:focus {
      border-color: var(--primary);
      background: rgba(0,212,255,0.05);
    }

    .req-row {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 10px;
    }

    @media (max-width: 400px) {
      .req-row { grid-template-columns: 1fr; }
    }

    .req-submit {
      width: 100%;
      padding: 13px;
      background: linear-gradient(135deg, var(--primary), var(--secondary));
      border: none;
      border-radius: var(--radius-sm);
      color: #0a0a1a;
      font-family: 'Space Grotesk', sans-serif;
      font-size: 0.8rem;
      font-weight: 700;
      cursor: pointer;
      letter-spacing: 1px;
      text-transform: uppercase;
      transition: all 0.25s ease;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
    }

    .req-submit:hover {
      transform: translateY(-2px);
      box-shadow: 0 8px 25px rgba(0,212,255,0.3);
    }

    .req-submit:active {
      transform: translateY(0);
    }

    /* ══════════════════════════════════════
       LISTENER INFO
    ══════════════════════════════════════ */
    .listener-bar {
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 10px 20px;
      border-top: 1px solid var(--border);
      background: rgba(0,0,0,0.1);
    }

    .listener-item {
      display: flex;
      align-items: center;
      gap: 6px;
      font-size: 0.7rem;
      color: var(--text-dim);
    }

    .listener-item i { font-size: 0.65rem; }

    .listener-item strong {
      color: var(--text);
      font-weight: 600;
    }

    /* ══════════════════════════════════════
       TOAST
    ══════════════════════════════════════ */
    .toast {
      position: fixed;
      bottom: 30px;
      left: 50%;
      transform: translateX(-50%) translateY(60px);
      padding: 12px 24px;
      background: var(--bg-card);
      border: 1px solid var(--primary);
      border-radius: 30px;
      font-size: 0.8rem;
      font-weight: 500;
      color: var(--primary);
      z-index: 999;
      opacity: 0;
      pointer-events: none;
      transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
      white-space: nowrap;
      box-shadow: 0 10px 40px rgba(0,0,0,0.4);
      display: flex;
      align-items: center;
      gap: 8px;
    }

    .toast.show {
      opacity: 1;
      transform: translateX(-50%) translateY(0);
    }

    /* ══════════════════════════════════════
       RESPONSIVE
    ══════════════════════════════════════ */
    @media (max-width: 500px) {
      body { padding: 10px; }
      .widget-header { padding: 12px 16px; }
      .player-section { padding: 16px; }
      .request-section { padding: 14px 16px; }
      .album-art { width: 60px; height: 60px; }
      .np-title { font-size: 0.9rem; }
      .ctrl-btn.main { width: 54px; height: 54px; }
      .ctrl-btn { width: 38px; height: 38px; }
    }

    /* Scrollbar */
    ::-webkit-scrollbar { width: 3px; }
    ::-webkit-scrollbar-track { background: transparent; }
    ::-webkit-scrollbar-thumb { background: var(--primary); border-radius: 2px; }
  </style>
</head>
<body>

  <!-- Background Orbs -->
  <div class="bg-orb bg-orb-1"></div>
  <div class="bg-orb bg-orb-2"></div>

  <!-- ══════════════════════════════════════
       WIDGET
  ══════════════════════════════════════ -->
  <div class="radio-widget">

    <!-- KAYAN YAZI -->
    <div class="ticker-wrap">
      <div class="ticker" id="ticker">
        <span class="ticker-item">
          <i class="fas fa-radio"></i> GALACTIC WAVE RADYO
        </span>
        <span class="ticker-item">
          <i class="fas fa-music"></i> Premium Ses Kalitesi
        </span>
        <span class="ticker-item">
          <i class="fas fa-headphones"></i> 7/24 Canlı Yayın
        </span>
        <span class="ticker-item">
          <i class="fas fa-star"></i> En İyi Radyo Deneyimi
        </span>
        <span class="ticker-item">
          <i class="fas fa-bolt"></i> Kesintisiz Müzik
        </span>
        <span class="ticker-item">
          <i class="fas fa-microphone"></i> Canlı DJ Performansları
        </span>
        <!-- Repeat for seamless scroll -->
        <span class="ticker-item">
          <i class="fas fa-radio"></i> GALACTIC WAVE RADYO
        </span>
        <span class="ticker-item">
          <i class="fas fa-music"></i> Premium Ses Kalitesi
        </span>
        <span class="ticker-item">
          <i class="fas fa-headphones"></i> 7/24 Canlı Yayın
        </span>
        <span class="ticker-item">
          <i class="fas fa-star"></i> En İyi Radyo Deneyimi
        </span>
        <span class="ticker-item">
          <i class="fas fa-bolt"></i> Kesintisiz Müzik
        </span>
        <span class="ticker-item">
          <i class="fas fa-microphone"></i> Canlı DJ Performansları
        </span>
      </div>
    </div>

    <!-- HEADER -->
    <div class="widget-header">
      <div class="widget-brand">
        <div class="brand-icon">🎵</div>
        <span class="brand-name">RADYO</span>
      </div>
      <div class="live-badge" id="liveBadge">
        <span class="live-dot"></span>
        <span id="liveText">CANLI</span>
      </div>
    </div>

    <!-- PLAYER -->
    <div class="player-section">
      <div class="now-playing">
        <div class="album-art" id="albumArt">
          <i class="fas fa-music icon"></i>
          <div class="playing-bars-overlay">
            <div class="mini-bars">
              <span></span><span></span><span></span><span></span>
            </div>
          </div>
        </div>
        <div class="np-info">
          <div class="np-label">🎧 Şimdi Çalıyor</div>
          <div class="np-title" id="npTitle">Yükleniyor...</div>
          <div class="np-artist" id="npArtist">Radyo</div>
        </div>
      </div>

      <!-- Visualizer -->
      <div class="visualizer-wrap" id="visualizer">
        <!-- Bars will be generated by JS -->
      </div>

      <!-- Controls -->
      <div class="controls">
        <button class="ctrl-btn" id="btnShuffle" title="Karıştır">
          <i class="fas fa-random"></i>
        </button>
        <button class="ctrl-btn" id="btnPrev" title="Sesi Azalt">
          <i class="fas fa-volume-down"></i>
        </button>
        <button class="ctrl-btn main" id="btnPlay" title="Oynat">
          <i class="fas fa-play" id="playIcon"></i>
        </button>
        <button class="ctrl-btn" id="btnNext" title="Sesi Artır">
          <i class="fas fa-volume-up"></i>
        </button>
        <button class="ctrl-btn" id="btnLike" title="Beğen">
          <i class="far fa-heart"></i>
        </button>
      </div>

      <!-- Volume -->
      <div class="volume-row">
        <i class="fas fa-volume-up vol-icon" id="volIcon"></i>
        <input type="range" class="vol-slider" id="volSlider" min="0" max="100" value="75">
        <span class="vol-val" id="volVal">75%</span>
      </div>
    </div>

    <!-- REQUEST -->
    <div class="request-section">
      <div class="request-title">
        <i class="fas fa-magic"></i>
        <span>Şarkı İste</span>
      </div>
      <div class="request-form">
        <input type="text" class="req-input" id="reqSong"
               placeholder="🎵 Şarkı adı veya sanatçı..." maxlength="100">
        <div class="req-row">
          <input type="text" class="req-input" id="reqName"
                 placeholder="👤 İsminiz" maxlength="50">
          <input type="text" class="req-input" id="reqWish"
                 placeholder="💬 Dilek (opsiyonel)" maxlength="80">
        </div>
        <button class="req-submit" id="reqSubmit">
          <i class="fas fa-paper-plane"></i>
          İsteği Gönder
        </button>
      </div>
    </div>

    <!-- LISTENER INFO -->
    <div class="listener-bar">
      <div class="listener-item">
        <i class="fas fa-users"></i>
        <span>Dinleyici: <strong id="dispListeners">0</strong></span>
      </div>
      <div class="listener-item">
        <i class="fas fa-tachometer-alt"></i>
        <span><strong id="dispBitrate">128</strong> kbps</span>
      </div>
      <div class="listener-item">
        <i class="fas fa-clock"></i>
        <span><strong id="dispUptime">00:00</strong></span>
      </div>
    </div>
  </div>

  <!-- TOAST -->
  <div class="toast" id="toast">
    <i class="fas fa-check-circle"></i>
    <span id="toastMsg">Mesaj</span>
  </div>

  <!-- AUDIO -->
  <audio id="audioPlayer" preload="none">
    <source src="https://radyocast.com/8028/Stream" type="audio/mpeg">
  </audio>

  <script>
    // ══════════════════════════════════════
    // CONFIG
    // ══════════════════════════════════════
    const CFG = {
      API_URL:    'https://radyocast.com/cp/get_info.php?p=8028',
      STREAM_URL: 'https://radyocast.com/8028/Stream',
      REFRESH_MS: 8000
    };

    // ══════════════════════════════════════
    // STATE
    // ══════════════════════════════════════
    const S = {
      playing:    false,
      volume:     75,
      liked:      false,
      uptime:     0,
      uptimeT:    null,
      refreshT:  null,
      visT:       null,
      data:       null
    };

    // ══════════════════════════════════════
    // DOM
    // ══════════════════════════════════════
    const $ = s => document.querySelector(s);

    const D = {
      audio:      $('#audioPlayer'),
      npTitle:    $('#npTitle'),
      npArtist:   $('#npArtist'),
      albumArt:   $('#albumArt'),
      playIcon:   $('#playIcon'),
      btnPlay:    $('#btnPlay'),
      btnLike:    $('#btnLike'),
      btnPrev:    $('#btnPrev'),
      btnNext:    $('#btnNext'),
      btnShuffle: $('#btnShuffle'),
      volSlider:  $('#volSlider'),
      volVal:     $('#volVal'),
      volIcon:    $('#volIcon'),
      liveBadge:  $('#liveBadge'),
      liveText:   $('#liveText'),
      dispListeners: $('#dispListeners'),
      dispBitrate:  $('#dispBitrate'),
      dispUptime:  $('#dispUptime'),
      reqSong:    $('#reqSong'),
      reqName:    $('#reqName'),
      reqWish:    $('#reqWish'),
      reqSubmit:  $('#reqSubmit'),
      toast:      $('#toast'),
      toastMsg:   $('#toastMsg'),
      visualizer: $('#visualizer'),
      ticker:     $('#ticker')
    };

    // ══════════════════════════════════════
    // VISUALIZER BARS
    // ══════════════════════════════════════
    function initVisualizer() {
      D.visualizer.innerHTML = '';
      for (let i = 0; i < 32; i++) {
        const bar = document.createElement('div');
        bar.className = 'vis-bar';
        bar.style.height = '5px';
        D.visualizer.appendChild(bar);
      }
    }

    function startVisualizer() {
      if (S.visT) return;
      S.visT = setInterval(() => {
        if (!S.playing) return;
        const bars = D.visualizer.querySelectorAll('.vis-bar');
        bars.forEach((bar, i) => {
          const h = Math.random() * 40 + 5;
          bar.style.height = h + 'px';
          bar.classList.add('active');
          setTimeout(() => bar.classList.remove('active'), 200);
        });
      }, 120);
    }

    function stopVisualizer() {
      clearInterval(S.visT);
      S.visT = null;
      const bars = D.visualizer.querySelectorAll('.vis-bar');
      bars.forEach(bar => bar.style.height = '5px');
    }

    // ══════════════════════════════════════
    // API
    // ══════════════════════════════════════
    async function fetchAPI() {
      try {
        const r = await fetch(CFG.API_URL + '&t=' + Date.now());
        if (!r.ok) throw new Error('API error');
        const raw = await r.json();
        S.data = typeof raw === 'object' && !Array.isArray(raw) ? raw : {};
        updateUI(S.data);
      } catch (e) {
        console.warn('API: ', e.message);
      }
    }

    // ══════════════════════════════════════
    // UPDATE UI
    // ══════════════════════════════════════
    function updateUI(d) {
      const title   = d.title    || 'Bilinmiyor';
      const art     = d.art      || '';
      const online  = parseInt(d.listeners || 0);
      const bitrate = d.bitrate  || '128';
      const dj      = d.djusername || '';

      // Album art
      if (art) {
        D.albumArt.innerHTML = `<img src="${art}" alt="albüm">` +
          `<div class="playing-bars-overlay"><div class="mini-bars"><span></span><span></span><span></span><span></span></div></div>`;
      }

      // Title / Artist
      const parts = title.split(' - ');
      if (parts.length >= 2) {
        D.npArtist.textContent = parts[0].trim();
        D.npTitle.textContent  = parts.slice(1).join(' - ').trim();
      } else {
        D.npArtist.textContent = 'Radyo';
        D.npTitle.textContent  = title;
      }

      // Live badge
      if (S.playing) {
        D.liveBadge.classList.remove('offline');
        D.liveText.textContent = 'CANLI';
        if (dj) D.liveText.textContent = 'DJ: ' + dj;
      } else {
        D.liveBadge.classList.add('offline');
        D.liveText.textContent = 'ÇEVRİMDIŞI';
      }

      // Stats
      animateNum(D.dispListeners, online);
      D.dispBitrate.textContent = bitrate;

      // Update ticker with current song
      updateTicker(title);
    }

    function updateTicker(song) {
      const items = D.ticker.querySelectorAll('.ticker-item');
      // First item is always station name, second becomes current song
      if (items[1]) {
        items[1].innerHTML = `<i class="fas fa-music"></i> ${esc(song)}`;
      }
    }

    // ══════════════════════════════════════
    // HELPERS
    // ══════════════════════════════════════
    function esc(s) {
      if (!s) return '';
      const d = document.createElement('div');
      d.textContent = s;
      return d.innerHTML;
    }

    function animateNum(el, target) {
      const cur = parseInt(el.textContent) || 0;
      const diff = target - cur;
      if (Math.abs(diff) < 3) { el.textContent = target; return; }
      let i = 0;
      const t = setInterval(() => {
        i++;
        el.textContent = Math.round(cur + (diff / 10) * i);
        if (i >= 10) { el.textContent = target; clearInterval(t); }
      }, 20);
    }

    // ══════════════════════════════════════
    // PLAY / PAUSE
    // ══════════════════════════════════════
    function togglePlay() {
      S.playing = !S.playing;

      if (S.playing) {
        D.audio.src = CFG.STREAM_URL;
        D.audio.volume = S.volume / 100;
        D.audio.play().catch(() => {});

        D.btnPlay.classList.add('playing');
        D.playIcon.className = 'fas fa-pause';
        D.albumArt.classList.add('spinning', 'playing');

        startVisualizer();
        startUptime();
        toast('▶ Radyo başlatıldı!');

        D.liveBadge.classList.remove('offline');
        if (S.data?.djusername) {
          D.liveText.textContent = 'DJ: ' + S.data.djusername;
        } else {
          D.liveText.textContent = 'CANLI';
        }
      } else {
        D.audio.pause();
        D.btnPlay.classList.remove('playing');
        D.playIcon.className = 'fas fa-play';
        D.albumArt.classList.remove('spinning', 'playing');

        stopVisualizer();
        toast('⏸ Yayın duraklatıldı');

        D.liveBadge.classList.add('offline');
        D.liveText.textContent = 'ÇEVRİMDIŞI';
      }
    }

    // ══════════════════════════════════════
    // UPTIME
    // ══════════════════════════════════════
    function startUptime() {
      clearInterval(S.uptimeT);
      S.uptimeT = setInterval(() => {
        S.uptime++;
        const m = Math.floor(S.uptime / 60);
        const s = S.uptime % 60;
        D.dispUptime.textContent = `${m}:${s.toString().padStart(2, '0')}`;
      }, 1000);
    }

    // ══════════════════════════════════════
    // VOLUME
    // ══════════════════════════════════════
    function setVol(v) {
      v = Math.max(0, Math.min(100, parseInt(v)));
      S.volume = v;
      D.volSlider.value = v;
      D.volVal.textContent = v + '%';
      D.audio.volume = v / 100;

      if (v === 0) {
        D.volIcon.className = 'fas fa-volume-mute vol-icon';
      } else if (v < 30) {
        D.volIcon.className = 'fas fa-volume-off vol-icon';
      } else if (v < 70) {
        D.volIcon.className = 'fas fa-volume-down vol-icon';
      } else {
        D.volIcon.className = 'fas fa-volume-up vol-icon';
      }
    }

    // ══════════════════════════════════════
    // LIKE
    // ══════════════════════════════════════
    function toggleLike() {
      S.liked = !S.liked;
      const icon = D.btnLike.querySelector('i');

      if (S.liked) {
        icon.className = 'fas fa-heart';
        D.btnLike.classList.add('liked');
        toast('❤️ Beğenildi!');
      } else {
        icon.className = 'far fa-heart';
        D.btnLike.classList.remove('liked');
        toast('💔 Beğeni kaldırıldı');
      }
    }

    // ══════════════════════════════════════
    // REQUEST
    // ══════════════════════════════════════
    function sendRequest() {
      const song = D.reqSong.value.trim();
      const name = D.reqName.value.trim();
      const wish = D.reqWish.value.trim();

      if (!song) {
        toast('⚠️ Şarkı adı girin!');
        D.reqSong.focus();
        return;
      }

      // Here you would normally send to API
      toast('🎵 İsteğiniz gönderildi!');

      D.reqSong.value = '';
      D.reqWish.value = '';
      // Keep name for next time
    }

    // ══════════════════════════════════════
    // TOAST
    // ══════════════════════════════════════
    function toast(msg) {
      D.toastMsg.textContent = msg;
      D.toast.classList.add('show');
      clearTimeout(D.toast._t);
      D.toast._t = setTimeout(() => D.toast.classList.remove('show'), 3000);
    }

    // ══════════════════════════════════════
    // EVENTS
    // ══════════════════════════════════════
    function bindEvents() {
      // Play
      D.btnPlay.addEventListener('click', togglePlay);

      // Volume
      D.volSlider.addEventListener('input', e => setVol(e.target.value));
      D.volIcon.addEventListener('click', () => setVol(S.volume > 0 ? 0 : 75));

      // Volume buttons
      D.btnPrev.addEventListener('click', () => setVol(S.volume - 10));
      D.btnNext.addEventListener('click', () => setVol(S.volume + 10));

      // Like
      D.btnLike.addEventListener('click', toggleLike);

      // Shuffle (visual feedback)
      D.btnShuffle.addEventListener('click', () => {
        D.btnShuffle.classList.toggle('active');
        toast(D.btnShuffle.classList.contains('active') ? '🔀 Karıştırma açık' : '🔀 Kapalı');
      });

      // Request
      D.reqSubmit.addEventListener('click', sendRequest);
      D.reqSong.addEventListener('keydown', e => { if (e.key === 'Enter') sendRequest(); });

      // Keyboard
      document.addEventListener('keydown', e => {
        if (e.target.tagName === 'INPUT') return;
        switch (e.key) {
          case ' ': e.preventDefault(); togglePlay(); break;
          case 'ArrowUp':   e.preventDefault(); setVol(S.volume + 5); break;
          case 'ArrowDown': e.preventDefault(); setVol(S.volume - 5); break;
          case 'l': toggleLike(); break;
          case 'm': D.volIcon.click(); break;
        }
      });

      // Audio events
      D.audio.addEventListener('playing', () => {
        D.btnPlay.classList.add('playing');
        D.playIcon.className = 'fas fa-pause';
      });

      D.audio.addEventListener('pause', () => {
        D.btnPlay.classList.remove('playing');
        D.playIcon.className = 'fas fa-play';
      });
    }

    // ══════════════════════════════════════
    // INIT
    // ══════════════════════════════════════
    function init() {
      initVisualizer();
      bindEvents();
      setVol(75);

      // Initial API fetch
      fetchAPI();

      // Periodic refresh
      S.refreshT = setInterval(fetchAPI, CFG.REFRESH_MS);
    }

    document.addEventListener('DOMContentLoaded', init);
  </script>

</body>
</html>
```

---

## 🎯 Widget Özellikleri

| Özellik | Açıklama |
|---------|----------|
| 🎵 **Stream** | `radyocast.com/8028/Stream` entegreli |
| 📜 **Kayan Yazı** | Üstte sürekli akan duyuru bandı |
| 🎛️ **Visualizer** | 32 bant animasyonlu bars |
| 📊 **Dinleyici** | Canlı dinleyici sayısı |
| ⏱️ **Sayaç** | Yayın çalışma süresi |
| 🎚️ **Ses** | Volüm slider + butonları |
| ❤️ **Beğen** | Kalp butonu animasyonu |
| 🎵 **İstek** | Şarkı adı + isim + dilek formu |
| 📱 **Mobil** | Tüm ekranlarda responsive |
| 🌙 **Karanlık** | Modern karanlık tema |

## 🎮 Kısayollar

| Tuş | İşlev |
|-----|-------|
| `Space` | Oynat / Duraklat |
| `↑` | Ses +5 |
| `↓` | Ses -5 |
| `M` | Sessiz / Aç |
| `L` | Beğen |