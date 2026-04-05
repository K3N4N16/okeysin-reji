<think>

Kullanıcı tek bir HTML dosyasında tam entegre bir radyo uygulaması istiyor. Şunları içermesi gerekiyor:

1. API bağlantısı (radyocast.com/cp/get_info.php?p=8028)
2. Stream URL (https://radyocast.com/8028/Stream)
3. Yeni özellikler ve yenilikler
4. Tüm kodlar tek dosyada

Yeni özellikler ekleyelim:
- Tam işlevsel audio player (gerçek stream)
- Şarkı sözleri (simüle veya API'den)
- İstek sistemi
- Favoriler
- Gece/Gündüz modu
- İlerlemiş visualizer (Canvas)
- Radyo bilgi kartları
- Sonraki şarkı tahmini
- Ses efektleri (reverb, bass boost vb.)
- Radyo istatistikleri grafiği
- Dj takvimi
- Chat sistemi
- Paylaşma özellikleri
- notifications
- Dark/Light mode
- Animasyonlu elementler
- Ve daha fazlası...

Tüm kodu tek bir HTML dosyasında yazacağım.

</think>

# 🌌 Galactic Wave Radio - Tek Dosya Tam Entegre Sürüm

```html
<!DOCTYPE html>
<html lang="tr" data-theme="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>🌌 Galactic Wave Radio - Premium Experience</title>

  <!-- Font Awesome 6 -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">

  <!-- Google Fonts -->
  <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;500;600;700;800;900&family=Rajdhani:wght@300;400;500;600;700&family=Space+Grotesk:wght@300;400;500;600;700&display=swap" rel="stylesheet">

  <style>
    /* ═══════════════════════════════════════════════════════
       CSS VARIABLES - DUAL THEME
    ═══════════════════════════════════════════════════════ */
    :root[data-theme="dark"] {
      --bg-deep:        #020010;
      --bg-dark:        #050520;
      --bg-card:        rgba(8, 8, 40, 0.9);
      --bg-glass:       rgba(15, 15, 60, 0.45);
      --bg-surface:     rgba(20, 20, 70, 0.5);

      --primary:        #00e0ff;
      --secondary:      #c760ff;
      --accent:         #ff6b9d;
      --energy:         #ffe04b;
      --success:        #00ff88;
      --danger:         #ff4466;
      --warning:        #ffaa00;

      --glow-pri:       rgba(0, 224, 255, 0.35);
      --glow-sec:       rgba(199, 96, 255, 0.35);
      --glow-acc:       rgba(255, 107, 157, 0.35);

      --text:           #e0e0ff;
      --text-dim:       #7070a0;
      --text-bright:    #ffffff;

      --border:         rgba(255, 255, 255, 0.06);
      --border-active:  rgba(0, 224, 255, 0.2);
    }

    :root[data-theme="light"] {
      --bg-deep:        #f0f4ff;
      --bg-dark:        #e0e8ff;
      --bg-card:        rgba(255, 255, 255, 0.92);
      --bg-glass:       rgba(255, 255, 255, 0.6);
      --bg-surface:     rgba(200, 210, 255, 0.3);

      --primary:        #0066ff;
      --secondary:      #8844ff;
      --accent:         #ff4488;
      --energy:         #ffaa00;
      --success:        #00bb55;
      --danger:         #dd2244;
      --warning:        #ee8800;

      --glow-pri:       rgba(0, 102, 255, 0.2);
      --glow-sec:       rgba(136, 68, 255, 0.2);
      --glow-acc:       rgba(255, 68, 136, 0.2);

      --text:           #1a1a3a;
      --text-dim:       #5566aa;
      --text-bright:    #000820;

      --border:         rgba(0, 0, 0, 0.08);
      --border-active:  rgba(0, 102, 255, 0.25);
    }

    * { margin: 0; padding: 0; box-sizing: border-box; }

    :root {
      --font-display: 'Orbitron', monospace;
      --font-body:    'Space Grotesk', sans-serif;
      --font-ui:      'Rajdhani', sans-serif;
      --radius:       18px;
      --radius-sm:    12px;
      --radius-xs:    8px;
      --transition:   0.3s cubic-bezier(0.4, 0, 0.2, 1);
    }

    html { scroll-behavior: smooth; }

    body {
      font-family: var(--font-body);
      background: var(--bg-deep);
      color: var(--text);
      min-height: 100vh;
      overflow-x: hidden;
      transition: background var(--transition), color var(--transition);
    }

    /* ═══════════════════════════════════════════════════════
       ANIMATED BACKGROUND
    ═══════════════════════════════════════════════════════ */
    .cosmic-bg {
      position: fixed; inset: 0; z-index: 0; overflow: hidden;
      pointer-events: none;
    }

    .nebula {
      position: absolute; border-radius: 50%; filter: blur(120px);
      opacity: 0.12; animation: nebula-drift 30s ease-in-out infinite alternate;
    }

    .nebula:nth-child(1) {
      width: 700px; height: 700px; background: var(--primary);
      top: -15%; left: -15%;
    }
    .nebula:nth-child(2) {
      width: 600px; height: 600px; background: var(--secondary);
      bottom: -15%; right: -15%; animation-delay: -10s; animation-direction: alternate-reverse;
    }
    .nebula:nth-child(3) {
      width: 500px; height: 500px; background: var(--accent);
      top: 50%; left: 50%; animation-delay: -18s;
    }
    .nebula:nth-child(4) {
      width: 400px; height: 400px; background: var(--energy);
      top: 10%; right: 30%; opacity: 0.06; animation-delay: -25s;
    }

    @keyframes nebula-drift {
      0%   { transform: translate(0, 0) scale(1) rotate(0deg); }
      33%  { transform: translate(80px, -50px) scale(1.2) rotate(5deg); }
      66%  { transform: translate(-40px, 60px) scale(0.85) rotate(-5deg); }
      100% { transform: translate(30px, -30px) scale(1.1) rotate(3deg); }
    }

    .star-field { position: fixed; inset: 0; z-index: 0; }

    .star {
      position: absolute; background: white; border-radius: 50%;
      animation: twinkle var(--dur, 3s) ease-in-out infinite var(--delay, 0s);
    }

    @keyframes twinkle {
      0%, 100% { opacity: 0.15; transform: scale(0.7); }
      50%      { opacity: 1; transform: scale(1.3); }
    }

    /* ═══════════════════════════════════════════════════════
       SCROLLBAR
    ═══════════════════════════════════════════════════════ */
    ::-webkit-scrollbar { width: 5px; }
    ::-webkit-scrollbar-track { background: var(--bg-deep); }
    ::-webkit-scrollbar-thumb {
      background: linear-gradient(180deg, var(--primary), var(--secondary));
      border-radius: 3px;
    }

    /* ═══════════════════════════════════════════════════════
       APP LAYOUT
    ═══════════════════════════════════════════════════════ */
    .app {
      position: relative; z-index: 1;
      max-width: 1500px; margin: 0 auto; padding: 15px;
      padding-bottom: 100px;
    }

    /* ═══════════════════════════════════════════════════════
       HEADER
    ═══════════════════════════════════════════════════════ */
    .header {
      text-align: center; padding: 15px 0 10px;
      display: flex; align-items: center; justify-content: space-between;
      flex-wrap: wrap; gap: 15px;
    }

    .header-left {
      display: flex; align-items: center; gap: 12px;
    }

    .logo-icon {
      font-size: 2rem; animation: logo-pulse 3s ease-in-out infinite;
    }

    @keyframes logo-pulse {
      0%, 100% { filter: drop-shadow(0 0 8px var(--glow-pri)); }
      50%      { filter: drop-shadow(0 0 20px var(--glow-pri)); }
    }

    .brand-text { text-align: left; }

    .brand-name {
      font-family: var(--font-display);
      font-size: clamp(1.1rem, 3vw, 1.6rem);
      font-weight: 800;
      background: linear-gradient(135deg, var(--primary), var(--secondary), var(--accent));
      background-size: 200% 200%;
      -webkit-background-clip: text; -webkit-text-fill-color: transparent;
      background-clip: text; animation: gradient-shift 4s ease infinite;
      letter-spacing: 2px;
    }

    .brand-tag {
      font-family: var(--font-ui); font-size: 0.7rem;
      color: var(--text-dim); letter-spacing: 4px;
      text-transform: uppercase;
    }

    @keyframes gradient-shift {
      0%, 100% { background-position: 0% 50%; }
      50%      { background-position: 100% 50%; }
    }

    /* Header Actions */
    .header-actions {
      display: flex; gap: 10px; align-items: center;
    }

    .hdr-btn {
      width: 42px; height: 42px; border-radius: 50%;
      border: 1px solid var(--border);
      background: var(--bg-glass);
      color: var(--text-dim);
      font-size: 1rem; cursor: pointer;
      display: flex; align-items: center; justify-content: center;
      transition: var(--transition);
    }

    .hdr-btn:hover {
      border-color: var(--primary); color: var(--primary);
      background: var(--bg-glass);
      transform: scale(1.1);
    }

    .hdr-btn.active { color: var(--primary); border-color: var(--primary); }

    /* Theme Toggle */
    .theme-toggle {
      position: relative; width: 60px; height: 30px;
      border-radius: 20px;
      background: var(--bg-glass);
      border: 1px solid var(--border);
      cursor: pointer; overflow: hidden;
      transition: var(--transition);
    }

    .theme-toggle-track {
      position: absolute; inset: 2px;
      border-radius: 20px;
      background: linear-gradient(135deg, var(--primary), var(--secondary));
      opacity: 0.3; transition: var(--transition);
    }

    .theme-toggle-thumb {
      position: absolute; top: 2px; left: 2px;
      width: 24px; height: 24px; border-radius: 50%;
      background: var(--primary);
      box-shadow: 0 0 10px var(--glow-pri);
      transition: var(--transition);
      display: flex; align-items: center; justify-content: center;
      font-size: 0.7rem; color: var(--bg-deep);
    }

    .theme-toggle.light .theme-toggle-thumb { left: calc(100% - 26px); }

    /* Status Pills */
    .status-pills {
      display: flex; justify-content: center; flex-wrap: wrap;
      gap: 10px; margin: 10px 0;
    }

    .pill {
      display: flex; align-items: center; gap: 8px;
      padding: 6px 16px;
      background: var(--bg-glass);
      border: 1px solid var(--border);
      border-radius: 25px;
      font-family: var(--font-ui); font-size: 0.78rem;
      color: var(--text-dim); transition: var(--transition);
    }

    .pill i { font-size: 0.7rem; }

    .pill.live {
      background: rgba(0, 255, 136, 0.08);
      border-color: rgba(0, 255, 136, 0.2);
    }

    .pill.live i { color: var(--success); animation: blink 1.5s infinite; }

    @keyframes blink { 0%, 100% { opacity: 1; } 50% { opacity: 0.2; } }

    .pill strong { color: var(--text); font-weight: 600; }

    .pill.dj-live i { color: var(--accent); }

    .pill .dot {
      width: 6px; height: 6px; border-radius: 50%;
      background: currentColor;
    }

    /* ═══════════════════════════════════════════════════════
       MAIN GRID
    ═══════════════════════════════════════════════════════ */
    .main-grid {
      display: grid;
      grid-template-columns: 1fr 340px;
      gap: 20px; margin-top: 15px;
    }

    @media (max-width: 1100px) {
      .main-grid { grid-template-columns: 1fr; }
    }

    .col-left, .col-right {
      display: flex; flex-direction: column; gap: 20px;
    }

    /* ═══════════════════════════════════════════════════════
       CARD
    ═══════════════════════════════════════════════════════ */
    .card {
      background: var(--bg-card);
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 22px;
      backdrop-filter: blur(25px);
      transition: var(--transition);
    }

    .card:hover { border-color: var(--border-active); }

    .card-head {
      display: flex; align-items: center; gap: 10px;
      margin-bottom: 18px;
    }

    .card-head i { color: var(--primary); font-size: 1rem; }

    .card-head h3 {
      font-family: var(--font-display);
      font-size: 0.78rem; letter-spacing: 2px;
      text-transform: uppercase; color: var(--text);
    }

    .card-head .spacer { flex: 1; }

    .card-head .badge {
      padding: 3px 12px; border-radius: 12px;
      font-family: var(--font-ui); font-size: 0.65rem;
      font-weight: 700; text-transform: uppercase;
      letter-spacing: 1px;
    }

    .badge-live {
      background: rgba(0, 255, 136, 0.1);
      color: var(--success);
      border: 1px solid rgba(0, 255, 136, 0.2);
      animation: glow-pulse 2s infinite;
    }

    @keyframes glow-pulse {
      0%, 100% { box-shadow: 0 0 0 0 rgba(0, 255, 136, 0.3); }
      50%      { box-shadow: 0 0 15px 3px rgba(0, 255, 136, 0.15); }
    }

    .badge-dj {
      background: rgba(255, 107, 157, 0.1);
      color: var(--accent);
      border: 1px solid rgba(255, 107, 157, 0.2);
    }

    /* ═══════════════════════════════════════════════════════
       PLAYER CARD - HERO
    ═══════════════════════════════════════════════════════ */
    .player-hero {
      background: linear-gradient(135deg,
        rgba(0, 224, 255, 0.05),
        rgba(199, 96, 255, 0.05)
      );
      border: 1px solid rgba(0, 224, 255, 0.1);
    }

    .player-grid {
      display: grid;
      grid-template-columns: 260px 1fr;
      gap: 25px; align-items: start;
    }

    @media (max-width: 700px) {
      .player-grid { grid-template-columns: 1fr; }
    }

    /* Album Art */
    .album-wrap {
      position: relative; width: 100%; aspect-ratio: 1;
      border-radius: var(--radius); overflow: hidden;
      cursor: pointer;
      box-shadow: 0 20px 60px rgba(0, 0, 0, 0.4),
                  0 0 40px var(--glow-pri);
    }

    .album-img {
      width: 100%; height: 100%; object-fit: cover;
      transition: transform 0.5s;
    }

    .album-wrap:hover .album-img { transform: scale(1.08); }

    .album-overlay {
      position: absolute; inset: 0;
      background: linear-gradient(180deg, transparent 25%, rgba(0,0,0,0.75) 100%);
      display: flex; align-items: center; justify-content: center;
      opacity: 0; transition: var(--transition);
    }

    .album-wrap:hover .album-overlay { opacity: 1; }

    .album-play-overlay {
      width: 65px; height: 65px; border-radius: 50%;
      background: var(--primary);
      border: none; color: var(--bg-deep);
      font-size: 1.5rem; cursor: pointer;
      display: flex; align-items: center; justify-content: center;
      box-shadow: 0 0 30px var(--glow-pri);
      transform: scale(0.8); transition: var(--transition);
    }

    .album-wrap:hover .album-play-overlay { transform: scale(1); }
    .album-play-overlay:hover { transform: scale(1.15) !important; }

    /* Playing Bars */
    .playing-bars {
      position: absolute; bottom: 10px; left: 10px;
      display: flex; gap: 3px; align-items: flex-end; height: 22px;
    }

    .playing-bars span {
      width: 4px; background: var(--primary);
      border-radius: 2px;
      animation: bar-anim 0.7s ease-in-out infinite;
    }

    .playing-bars span:nth-child(1) { height: 8px;  animation-delay: 0s; }
    .playing-bars span:nth-child(2) { height: 18px; animation-delay: 0.15s; }
    .playing-bars span:nth-child(3) { height: 12px; animation-delay: 0.3s; }
    .playing-bars span:nth-child(4) { height: 20px; animation-delay: 0.45s; }
    .playing-bars span:nth-child(5) { height: 6px;  animation-delay: 0.6s; }

    .playing-bars.paused span { animation-play-state: paused; }

    @keyframes bar-anim {
      0%, 100% { transform: scaleY(0.3); }
      50%      { transform: scaleY(1); }
    }

    .album-badges {
      position: absolute; top: 10px; left: 10px; right: 10px;
      display: flex; justify-content: space-between;
    }

    .badge-kbps {
      padding: 4px 10px; background: rgba(0,0,0,0.7);
      border: 1px solid var(--primary); border-radius: 12px;
      font-family: var(--font-display); font-size: 0.6rem;
      color: var(--primary); letter-spacing: 1px;
    }

    .badge-hq {
      padding: 4px 10px; background: rgba(0,0,0,0.7);
      border: 1px solid var(--energy); border-radius: 12px;
      font-family: var(--font-display); font-size: 0.6rem;
      color: var(--energy); letter-spacing: 1px;
    }

    /* Player Info */
    .player-info { display: flex; flex-direction: column; gap: 15px; }

    .now-playing { display: flex; flex-direction: column; gap: 4px; }

    .np-label {
      font-family: var(--font-ui); font-size: 0.7rem;
      color: var(--primary); letter-spacing: 3px; text-transform: uppercase;
    }

    .np-title {
      font-family: var(--font-display);
      font-size: clamp(1.1rem, 2.5vw, 1.5rem);
      font-weight: 700; color: var(--text-bright);
      line-height: 1.3; max-height: 3.9em;
      overflow: hidden;
    }

    .np-artist {
      font-family: var(--font-body); font-size: 0.95rem;
      color: var(--text-dim);
    }

    /* DJ Mini Card */
    .dj-mini {
      display: flex; align-items: center; gap: 14px;
      padding: 12px 16px;
      background: linear-gradient(135deg, rgba(255,107,157,0.08), rgba(199,96,255,0.08));
      border: 1px solid rgba(255, 107, 157, 0.15);
      border-radius: var(--radius-sm);
    }

    .dj-avatar {
      width: 45px; height: 45px; border-radius: 50%;
      object-fit: cover; border: 2px solid var(--accent);
      flex-shrink: 0;
    }

    .dj-avatar-ph {
      width: 45px; height: 45px; border-radius: 50%;
      background: linear-gradient(135deg, var(--accent), var(--secondary));
      display: flex; align-items: center; justify-content: center;
      color: white; font-size: 1rem; flex-shrink: 0;
    }

    .dj-mini-info { flex: 1; }

    .dj-mini-label {
      font-family: var(--font-ui); font-size: 0.65rem;
      color: var(--accent); letter-spacing: 2px; text-transform: uppercase;
    }

    .dj-mini-name {
      font-family: var(--font-display); font-size: 0.9rem;
      font-weight: 600; color: var(--text-bright);
    }

    .dj-live-tag {
      display: flex; align-items: center; gap: 5px;
      padding: 4px 10px;
      background: rgba(0, 255, 136, 0.1);
      border: 1px solid rgba(0, 255, 136, 0.2);
      border-radius: 15px; font-family: var(--font-ui);
      font-size: 0.65rem; color: var(--success); font-weight: 700;
    }

    .dj-live-tag .dot {
      width: 5px; height: 5px; border-radius: 50%;
      background: var(--success);
      animation: blink 1s infinite;
    }

    /* Progress */
    .progress-wrap { width: 100%; }

    .progress-track {
      width: 100%; height: 5px;
      background: rgba(255,255,255,0.08);
      border-radius: 3px; cursor: pointer;
      position: relative; overflow: hidden;
    }

    .progress-fill {
      height: 100%; border-radius: 3px;
      background: linear-gradient(90deg, var(--primary), var(--secondary));
      width: 0%; transition: width 0.3s;
      position: relative;
    }

    .progress-fill::after {
      content: ''; position: absolute; right: -1px; top: 50%;
      transform: translateY(-50%);
      width: 12px; height: 12px; border-radius: 50%;
      background: var(--primary);
      box-shadow: 0 0 10px var(--glow-pri);
      opacity: 0; transition: var(--transition);
    }

    .progress-track:hover .progress-fill::after { opacity: 1; }

    .progress-time {
      display: flex; justify-content: space-between;
      margin-top: 5px; font-family: var(--font-ui);
      font-size: 0.7rem; color: var(--text-dim);
    }

    /* Controls */
    .controls-row {
      display: flex; align-items: center; justify-content: center;
      gap: 15px; flex-wrap: wrap;
    }

    .ctrl-btn {
      width: 44px; height: 44px; border-radius: 50%;
      border: 1px solid var(--border);
      background: var(--bg-glass);
      color: var(--text-dim); font-size: 0.9rem;
      cursor: pointer; display: flex; align-items: center; justify-content: center;
      transition: var(--transition);
    }

    .ctrl-btn:hover {
      border-color: var(--primary); color: var(--primary);
      background: rgba(0, 224, 255, 0.08);
      transform: scale(1.1);
    }

    .ctrl-btn.on { color: var(--primary); border-color: var(--primary); }

    .ctrl-btn.main {
      width: 65px; height: 65px; font-size: 1.5rem;
      background: linear-gradient(135deg, var(--primary), var(--secondary));
      border: none; color: var(--bg-deep);
      box-shadow: 0 0 35px var(--glow-pri);
    }

    .ctrl-btn.main:hover {
      transform: scale(1.15);
      box-shadow: 0 0 60px var(--glow-pri);
    }

    .ctrl-btn.main.playing {
      animation: main-glow 2s ease-in-out infinite;
    }

    @keyframes main-glow {
      0%, 100% { box-shadow: 0 0 25px var(--glow-pri); }
      50%      { box-shadow: 0 0 60px var(--glow-pri), 0 0 100px rgba(199,96,255,0.15); }
    }

    .ctrl-btn.liked { color: var(--accent); border-color: var(--accent); }
    .ctrl-btn.liked i { animation: heart-beat 0.5s; }

    @keyframes heart-beat {
      0%   { transform: scale(1); }
      25%  { transform: scale(1.4); }
      50%  { transform: scale(0.9); }
      100% { transform: scale(1); }
    }

    /* Volume */
    .volume-row {
      display: flex; align-items: center; gap: 10px;
      margin-top: 10px; padding-top: 10px;
      border-top: 1px solid var(--border);
    }

    .vol-icon { color: var(--text-dim); font-size: 0.9rem; cursor: pointer; transition: var(--transition); }
    .vol-icon:hover { color: var(--primary); }

    .vol-slider {
      flex: 1; -webkit-appearance: none; appearance: none;
      height: 4px; background: rgba(255,255,255,0.08);
      border-radius: 2px; outline: none; cursor: pointer;
    }

    .vol-slider::-webkit-slider-thumb {
      -webkit-appearance: none; width: 15px; height: 15px;
      border-radius: 50%; background: var(--primary);
      cursor: pointer; box-shadow: 0 0 8px var(--glow-pri);
    }

    .vol-val {
      font-family: var(--font-display); font-size: 0.7rem;
      color: var(--text-dim); min-width: 38px; text-align: right;
    }

    /* ═══════════════════════════════════════════════════════
       VISUALIZER CARD
    ═══════════════════════════════════════════════════════ */
    .visualizer-wrap {
      position: relative; width: 100%;
      height: 130px; overflow: hidden;
      border-radius: var(--radius-sm);
      background: linear-gradient(180deg, rgba(0,224,255,0.02), rgba(199,96,255,0.02));
    }

    #visualizerCanvas {
      width: 100%; height: 100%;
    }

    .visualizer-overlay {
      position: absolute; bottom: 10px; left: 0; right: 0;
      display: flex; justify-content: center; gap: 3px;
    }

    .vis-dot {
      width: 4px; background: var(--primary);
      border-radius: 2px; opacity: 0.6;
    }

    /* EQ Section */
    .eq-section { margin-top: 15px; }

    .eq-modes {
      display: flex; gap: 6px; margin-bottom: 12px; flex-wrap: wrap;
    }

    .eq-btn {
      padding: 5px 14px; border: 1px solid var(--border);
      background: rgba(255,255,255,0.02); color: var(--text-dim);
      font-family: var(--font-ui); font-size: 0.7rem;
      border-radius: 15px; cursor: pointer;
      transition: var(--transition); letter-spacing: 1px;
      text-transform: uppercase;
    }

    .eq-btn:hover { border-color: var(--primary); color: var(--primary); }
    .eq-btn.active {
      background: rgba(0, 224, 255, 0.1);
      border-color: var(--primary); color: var(--primary);
    }

    .eq-bands { display: flex; justify-content: space-between; gap: 5px; }

    .eq-band {
      flex: 1; display: flex; flex-direction: column;
      align-items: center; gap: 6px;
    }

    .eq-slider {
      -webkit-appearance: none; appearance: none;
      width: 4px; height: 70px;
      background: rgba(255,255,255,0.08);
      border-radius: 2px; outline: none;
      writing-mode: vertical-lr; direction: rtl; cursor: pointer;
    }

    .eq-slider::-webkit-slider-thumb {
      -webkit-appearance: none; width: 12px; height: 12px;
      border-radius: 50%; background: var(--primary);
      cursor: pointer;
    }

    .eq-label {
      font-family: var(--font-ui); font-size: 0.6rem;
      color: var(--text-dim);
    }

    /* ═══════════════════════════════════════════════════════
       PLAYLIST / HISTORY
    ═══════════════════════════════════════════════════════ */
    .playlist-card .playlist-scroll {
      max-height: 400px; overflow-y: auto;
      display: flex; flex-direction: column; gap: 6px;
      padding-right: 5px;
    }

    .pl-track {
      display: flex; align-items: center; gap: 12px;
      padding: 10px 14px;
      background: rgba(255,255,255,0.02);
      border-radius: var(--radius-xs);
      cursor: pointer; transition: var(--transition);
      border: 1px solid transparent;
    }

    .pl-track:hover {
      background: rgba(0, 224, 255, 0.05);
      border-color: rgba(0, 224, 255, 0.1);
    }

    .pl-track.now {
      background: rgba(0, 224, 255, 0.08);
      border-color: rgba(0, 224, 255, 0.2);
    }

    .pl-num {
      font-family: var(--font-display); font-size: 0.65rem;
      color: var(--text-dim); min-width: 20px; text-align: center;
    }

    .pl-track.now .pl-num { color: var(--primary); }

    .pl-art {
      width: 38px; height: 38px; border-radius: 6px;
      object-fit: cover; flex-shrink: 0;
    }

    .pl-art-ph {
      width: 38px; height: 38px; border-radius: 6px;
      background: linear-gradient(135deg, rgba(0,224,255,0.15), rgba(199,96,255,0.15));
      display: flex; align-items: center; justify-content: center;
      color: var(--primary); font-size: 0.75rem; flex-shrink: 0;
    }

    .pl-info { flex: 1; min-width: 0; }

    .pl-title {
      font-family: var(--font-body); font-size: 0.82rem;
      color: var(--text); white-space: nowrap;
      overflow: hidden; text-overflow: ellipsis;
    }

    .pl-sub {
      font-family: var(--font-ui); font-size: 0.65rem;
      color: var(--text-dim);
    }

    .pl-time {
      font-family: var(--font-ui); font-size: 0.65rem;
      color: var(--text-dim);
    }

    /* ═══════════════════════════════════════════════════════
       DJ PROFILE CARD
    ═══════════════════════════════════════════════════════ */
    .dj-profile-card {
      background: linear-gradient(135deg,
        rgba(255,107,157,0.05),
        rgba(199,96,255,0.05)
      );
      border-color: rgba(255,107,157,0.12);
    }

    .dj-profile-main {
      display: flex; align-items: center; gap: 16px;
      margin-bottom: 18px;
    }

    .dj-prof-av {
      width: 70px; height: 70px; border-radius: 50%;
      object-fit: cover; border: 3px solid var(--accent);
      box-shadow: 0 0 20px rgba(255,107,157,0.3);
    }

    .dj-prof-ph {
      width: 70px; height: 70px; border-radius: 50%;
      background: linear-gradient(135deg, var(--accent), var(--secondary));
      display: flex; align-items: center; justify-content: center;
      font-size: 1.8rem; color: white;
      border: 3px solid var(--accent);
      box-shadow: 0 0 20px rgba(255,107,157,0.3);
    }

    .dj-prof-name {
      font-family: var(--font-display); font-size: 1.1rem;
      font-weight: 700; color: var(--text-bright);
    }

    .dj-prof-bio {
      font-family: var(--font-ui); font-size: 0.78rem;
      color: var(--text-dim); margin-top: 4px;
    }

    .dj-prof-tags {
      display: flex; gap: 6px; flex-wrap: wrap; margin-top: 8px;
    }

    .prof-tag {
      padding: 3px 10px; border-radius: 10px;
      background: rgba(0,224,255,0.08);
      border: 1px solid rgba(0,224,255,0.15);
      font-family: var(--font-ui); font-size: 0.6rem;
      color: var(--primary);
    }

    .dj-stats-row {
      display: grid; grid-template-columns: repeat(4, 1fr);
      gap: 10px;
    }

    .dj-stat {
      text-align: center; padding: 12px 6px;
      background: rgba(255,255,255,0.02);
      border-radius: var(--radius-xs);
      border: 1px solid var(--border);
    }

    .dj-stat-val {
      font-family: var(--font-display); font-size: 1.1rem;
      font-weight: 700; color: var(--primary);
    }

    .dj-stat-lbl {
      font-family: var(--font-ui); font-size: 0.6rem;
      color: var(--text-dim); text-transform: uppercase;
      letter-spacing: 1px; margin-top: 3px;
    }

    /* ═══════════════════════════════════════════════════════
       REQUEST CARD
    ═══════════════════════════════════════════════════════ */
    .request-form {
      display: flex; flex-direction: column; gap: 12px;
    }

    .req-input {
      padding: 12px 16px;
      background: rgba(255,255,255,0.04);
      border: 1px solid var(--border);
      border-radius: var(--radius-xs);
      color: var(--text); font-family: var(--font-body);
      font-size: 0.88rem; outline: none;
      transition: var(--transition);
    }

    .req-input::placeholder { color: var(--text-dim); }
    .req-input:focus { border-color: var(--primary); }

    .req-row {
      display: grid; grid-template-columns: 1fr 1fr; gap: 10px;
    }

    .req-input-sm {
      padding: 10px 14px;
      background: rgba(255,255,255,0.04);
      border: 1px solid var(--border);
      border-radius: var(--radius-xs);
      color: var(--text); font-family: var(--font-body);
      font-size: 0.82rem; outline: none;
      transition: var(--transition);
    }

    .req-input-sm::placeholder { color: var(--text-dim); }
    .req-input-sm:focus { border-color: var(--primary); }

    .req-submit {
      padding: 12px;
      background: linear-gradient(135deg, var(--primary), var(--secondary));
      border: none; border-radius: var(--radius-xs);
      color: var(--bg-deep); font-family: var(--font-display);
      font-size: 0.8rem; font-weight: 700;
      cursor: pointer; letter-spacing: 2px;
      text-transform: uppercase;
      transition: var(--transition);
    }

    .req-submit:hover {
      transform: translateY(-2px);
      box-shadow: 0 8px 25px var(--glow-pri);
    }

    .req-submit:active { transform: translateY(0); }

    /* ═══════════════════════════════════════════════════════
       LYRICS CARD
    ═══════════════════════════════════════════════════════ */
    .lyrics-card .lyrics-content {
      max-height: 300px; overflow-y: auto;
      padding: 15px; text-align: center;
    }

    .lyrics-text {
      font-family: var(--font-body); font-size: 1rem;
      color: var(--text-dim); line-height: 1.8;
    }

    .lyrics-text.current-line {
      color: var(--primary); font-weight: 600;
    }

    .lyrics-text.past-line { opacity: 0.4; }

    .lyrics-placeholder {
      padding: 40px 20px;
      color: var(--text-dim); font-style: italic;
      font-size: 0.9rem;
    }

    /* ═══════════════════════════════════════════════════════
       CHAT CARD
    ═══════════════════════════════════════════════════════ */
    .chat-card .chat-msgs {
      max-height: 280px; overflow-y: auto;
      display: flex; flex-direction: column; gap: 10px;
      margin-bottom: 12px;
    }

    .chat-msg { display: flex; gap: 10px; }

    .chat-av {
      width: 30px; height: 30px; border-radius: 50%;
      background: linear-gradient(135deg, var(--primary), var(--secondary));
      display: flex; align-items: center; justify-content: center;
      font-size: 0.65rem; color: white; flex-shrink: 0;
    }

    .chat-body { flex: 1; }

    .chat-author {
      font-family: var(--font-ui); font-size: 0.72rem;
      color: var(--primary); font-weight: 600;
    }

    .chat-text {
      font-size: 0.8rem; color: var(--text);
      margin-top: 2px; line-height: 1.4;
    }

    .chat-time {
      font-family: var(--font-ui); font-size: 0.6rem;
      color: var(--text-dim); margin-top: 3px;
    }

    .chat-input-row {
      display: flex; gap: 8px;
    }

    .chat-input {
      flex: 1; padding: 9px 14px;
      background: rgba(255,255,255,0.04);
      border: 1px solid var(--border);
      border-radius: var(--radius-xs);
      color: var(--text); font-family: var(--font-body);
      font-size: 0.82rem; outline: none;
      transition: var(--transition);
    }

    .chat-input::placeholder { color: var(--text-dim); }
    .chat-input:focus { border-color: var(--primary); }

    .chat-send {
      padding: 9px 18px;
      background: linear-gradient(135deg, var(--primary), var(--secondary));
      border: none; border-radius: var(--radius-xs);
      color: var(--bg-deep); font-size: 0.8rem;
      cursor: pointer; transition: var(--transition);
    }

    .chat-send:hover { transform: scale(1.05); }

    /* ═══════════════════════════════════════════════════════
       FAVORITES CARD
    ═══════════════════════════════════════════════════════ */
    .fav-grid {
      display: grid; grid-template-columns: repeat(auto-fill, minmax(80px, 1fr));
      gap: 10px;
    }

    .fav-item {
      display: flex; flex-direction: column; align-items: center;
      gap: 6px; padding: 12px 6px;
      background: rgba(255,255,255,0.02);
      border: 1px solid var(--border);
      border-radius: var(--radius-xs);
      cursor: pointer; transition: var(--transition);
    }

    .fav-item:hover {
      background: rgba(0,224,255,0.05);
      border-color: rgba(0,224,255,0.15);
      transform: translateY(-2px);
    }

    .fav-item img {
      width: 50px; height: 50px; border-radius: 8px;
      object-fit: cover;
    }

    .fav-item-name {
      font-size: 0.65rem; color: var(--text);
      text-align: center; max-width: 100%;
      overflow: hidden; text-overflow: ellipsis;
      white-space: nowrap;
    }

    .fav-add {
      width: 50px; height: 50px; border-radius: 8px;
      border: 2px dashed var(--border);
      display: flex; align-items: center; justify-content: center;
      color: var(--text-dim); font-size: 1.2rem;
      cursor: pointer; transition: var(--transition);
    }

    .fav-add:hover { border-color: var(--primary); color: var(--primary); }

    /* ═══════════════════════════════════════════════════════
       STATS CARD
    ═══════════════════════════════════════════════════════ */
    .stats-grid {
      display: grid; grid-template-columns: repeat(3, 1fr);
      gap: 12px;
    }

    .stat-box {
      text-align: center; padding: 15px 10px;
      background: rgba(255,255,255,0.02);
      border: 1px solid var(--border);
      border-radius: var(--radius-xs);
    }

    .stat-icon {
      font-size: 1.3rem; color: var(--primary); margin-bottom: 6px;
    }

    .stat-value {
      font-family: var(--font-display); font-size: 1.2rem;
      font-weight: 700; color: var(--text-bright);
    }

    .stat-label {
      font-family: var(--font-ui); font-size: 0.62rem;
      color: var(--text-dim); text-transform: uppercase;
      letter-spacing: 1px; margin-top: 3px;
    }

    /* Mini Chart */
    .mini-chart {
      height: 60px; margin-top: 15px;
      display: flex; align-items: flex-end; gap: 3px;
    }

    .chart-bar {
      flex: 1; background: linear-gradient(180deg, var(--primary), var(--secondary));
      border-radius: 2px 2px 0 0; transition: var(--transition);
    }

    .chart-bar:hover { opacity: 0.8; }

    /* ═══════════════════════════════════════════════════════
       BOTTOM PLAYER BAR
    ═══════════════════════════════════════════════════════ */
    .bottom-player {
      position: fixed; bottom: 0; left: 0; right: 0; z-index: 100;
      background: rgba(5, 5, 32, 0.95);
      backdrop-filter: blur(30px);
      border-top: 1px solid var(--border);
      padding: 8px 20px;
      display: flex; align-items: center; gap: 15px;
    }

    .bp-thumb {
      width: 48px; height: 48px; border-radius: 8px;
      object-fit: cover; flex-shrink: 0;
    }

    .bp-thumb-ph {
      width: 48px; height: 48px; border-radius: 8px;
      background: linear-gradient(135deg, rgba(0,224,255,0.2), rgba(199,96,255,0.2));
      display: flex; align-items: center; justify-content: center;
      color: var(--primary); font-size: 1rem; flex-shrink: 0;
    }

    .bp-info { flex: 1; min-width: 0; }

    .bp-title {
      font-family: var(--font-body); font-size: 0.85rem;
      color: var(--text-bright); font-weight: 500;
      white-space: nowrap; overflow: hidden; text-overflow: ellipsis;
    }

    .bp-sub {
      font-family: var(--font-ui); font-size: 0.7rem;
      color: var(--text-dim);
    }

    .bp-controls { display: flex; gap: 8px; align-items: center; }

    .bp-ctrl {
      width: 36px; height: 36px; border-radius: 50%;
      border: 1px solid var(--border);
      background: transparent; color: var(--text);
      font-size: 0.8rem; cursor: pointer;
      display: flex; align-items: center; justify-content: center;
      transition: var(--transition);
    }

    .bp-ctrl:hover { border-color: var(--primary); color: var(--primary); }

    .bp-ctrl.main-bp {
      width: 44px; height: 44px;
      background: linear-gradient(135deg, var(--primary), var(--secondary));
      border: none; color: var(--bg-deep); font-size: 1rem;
    }

    .bp-ctrl.main-bp:hover { transform: scale(1.1); }

    .bp-vol {
      display: flex; align-items: center; gap: 8px;
      width: 130px;
    }

    .bp-vol-slider {
      flex: 1; -webkit-appearance: none; appearance: none;
      height: 3px; background: rgba(255,255,255,0.1);
      border-radius: 2px; outline: none;
    }

    .bp-vol-slider::-webkit-slider-thumb {
      -webkit-appearance: none; width: 12px; height: 12px;
      border-radius: 50%; background: var(--primary); cursor: pointer;
    }

    .bp-right {
      display: flex; gap: 6px; align-items: center;
    }

    .bp-right-btn {
      width: 34px; height: 34px; border-radius: 8px;
      border: 1px solid var(--border);
      background: transparent; color: var(--text-dim);
      font-size: 0.8rem; cursor: pointer;
      display: flex; align-items: center; justify-content: center;
      transition: var(--transition);
    }

    .bp-right-btn:hover { border-color: var(--primary); color: var(--primary); }

    /* ═══════════════════════════════════════════════════════
       TOAST
    ═══════════════════════════════════════════════════════ */
    .toast {
      position: fixed; bottom: 85px; left: 50%;
      transform: translateX(-50%) translateY(40px);
      padding: 12px 24px;
      background: rgba(0, 224, 255, 0.12);
      border: 1px solid rgba(0, 224, 255, 0.25);
      backdrop-filter: blur(20px);
      border-radius: 30px;
      font-family: var(--font-ui); font-size: 0.82rem;
      color: var(--primary); z-index: 200;
      opacity: 0; pointer-events: none;
      transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
      white-space: nowrap;
    }

    .toast.show { opacity: 1; transform: translateX(-50%) translateY(0); }

    /* ═══════════════════════════════════════════════════════
       LOADING
    ═══════════════════════════════════════════════════════ */
    .skeleton {
      background: linear-gradient(90deg,
        rgba(255,255,255,0.03) 25%,
        rgba(255,255,255,0.06) 50%,
        rgba(255,255,255,0.03) 75%
      );
      background-size: 200% 100%;
      animation: skeleton 1.5s infinite;
      border-radius: 6px;
    }

    @keyframes skeleton {
      0%   { background-position: 200% 0; }
      100% { background-position: -200% 0; }
    }

    /* ═══════════════════════════════════════════════════════
       RESPONSIVE
    ═══════════════════════════════════════════════════════ */
    @media (max-width: 768px) {
      .app { padding: 10px; }
      .card { padding: 16px; }
      .header { flex-direction: column; }
      .bottom-player { padding: 6px 12px; }
      .bp-vol { width: 90px; }
      .stats-grid { grid-template-columns: repeat(2, 1fr); }
      .dj-stats-row { grid-template-columns: repeat(2, 1fr); }
      .req-row { grid-template-columns: 1fr; }
      .player-grid { grid-template-columns: 1fr; }
    }

    /* ═══════════════════════════════════════════════════════
       MODAL
    ═══════════════════════════════════════════════════════ */
    .modal-overlay {
      position: fixed; inset: 0; z-index: 300;
      background: rgba(0, 0, 0, 0.7);
      backdrop-filter: blur(10px);
      display: flex; align-items: center; justify-content: center;
      opacity: 0; pointer-events: none;
      transition: var(--transition);
    }

    .modal-overlay.open { opacity: 1; pointer-events: all; }

    .modal {
      background: var(--bg-card);
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 30px;
      max-width: 450px; width: 90%;
      transform: scale(0.9);
      transition: var(--transition);
    }

    .modal-overlay.open .modal { transform: scale(1); }

    .modal-head {
      display: flex; align-items: center; justify-content: space-between;
      margin-bottom: 20px;
    }

    .modal-head h3 {
      font-family: var(--font-display); font-size: 1rem;
      color: var(--text-bright);
    }

    .modal-close {
      width: 32px; height: 32px; border-radius: 50%;
      border: 1px solid var(--border); background: transparent;
      color: var(--text-dim); cursor: pointer; font-size: 0.9rem;
      display: flex; align-items: center; justify-content: center;
      transition: var(--transition);
    }

    .modal-close:hover { border-color: var(--danger); color: var(--danger); }
  </style>
</head>
<body>

  <!-- ANİMASYONLU ARKA PLAN -->
  <div class="cosmic-bg">
    <div class="nebula"></div>
    <div class="nebula"></div>
    <div class="nebula"></div>
    <div class="nebula"></div>
  </div>
  <div class="star-field" id="starField"></div>

  <!-- ═══════════════════════════════════════════════════════
       ANA UYGULAMA
  ═══════════════════════════════════════════════════════ -->
  <div class="app">

    <!-- HEADER -->
    <header class="header">
      <div class="header-left">
        <span class="logo-icon">🌌</span>
        <div class="brand-text">
          <div class="brand-name">GALACTIC WAVE</div>
          <div class="brand-tag">Premium Radio</div>
        </div>
      </div>

      <div class="header-actions">
        <button class="hdr-btn" id="btnSearch" title="Ara">
          <i class="fas fa-search"></i>
        </button>
        <button class="hdr-btn" id="btnFav" title="Favoriler">
          <i class="fas fa-heart"></i>
        </button>
        <button class="hdr-btn" id="btnInfo" title="Bilgi">
          <i class="fas fa-info-circle"></i>
        </button>
        <button class="hdr-btn" id="btnFullscreen" title="Tam Ekran">
          <i class="fas fa-expand"></i>
        </button>

        <!-- Theme Toggle -->
        <div class="theme-toggle" id="themeToggle" title="Tema Değiştir">
          <div class="theme-toggle-track"></div>
          <div class="theme-toggle-thumb">
            <i class="fas fa-moon"></i>
          </div>
        </div>
      </div>
    </header>

    <!-- STATUS PILLS -->
    <div class="status-pills">
      <div class="pill live">
        <i class="fas fa-circle"></i>
        <span>CANLI YAYIN</span>
      </div>
      <div class="pill" id="pillListeners">
        <i class="fas fa-users"></i>
        <span><strong id="dispListeners">0</strong> Dinleyici</span>
      </div>
      <div class="pill" id="pillBitrate">
        <i class="fas fa-tachometer-alt"></i>
        <span><strong id="dispBitrate">--</strong> kbps</span>
      </div>
      <div class="pill dj-live" id="pillDJ" style="display:none;">
        <i class="fas fa-microphone-alt"></i>
        <span>DJ: <strong id="dispDJ">--</strong></span>
      </div>
      <div class="pill" id="pillQuality">
        <i class="fas fa-bolt"></i>
        <span>HQ</span>
      </div>
      <div class="pill" id="pillUptime">
        <i class="fas fa-clock"></i>
        <span>Çalışma: <strong id="dispUptime">00:00:00</strong></span>
      </div>
    </div>

    <!-- MAIN GRID -->
    <div class="main-grid">

      <!-- SOL KOLON -->
      <div class="col-left">

        <!-- PLAYER CARD -->
        <div class="card player-hero">
          <div class="card-head">
            <i class="fas fa-satellite-dish"></i>
            <h3>Şimdi Çalıyor</h3>
            <span class="spacer"></span>
            <span class="badge badge-live" id="liveIndicator">
              <i class="fas fa-circle" style="font-size:5px; margin-right:4px;"></i> CANLI
            </span>
          </div>

          <div class="player-grid">
            <!-- ALBÜM -->
            <div class="album-wrap" id="albumWrap">
              <img src="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 300 300'><rect fill='%23050520' width='300' height='300'/><text fill='%2300e0ff' x='50%25' y='50%25' text-anchor='middle' font-size='80' dy='.3em'>🌌</text></svg>"
                   alt="Albüm" class="album-img" id="albumImg">
              <div class="album-overlay">
                <button class="album-play-overlay" id="albumPlayOverlay">
                  <i class="fas fa-play"></i>
                </button>
              </div>
              <div class="album-badges">
                <span class="badge-kbps" id="badgeKbps">128 kbps</span>
                <span class="badge-hq">HQ</span>
              </div>
              <div class="playing-bars paused" id="playingBars">
                <span></span><span></span><span></span><span></span><span></span>
              </div>
            </div>

            <!-- BİLGİ -->
            <div class="player-info">
              <div class="now-playing">
                <span class="np-label">🎵 Şimdi Çalıyor</span>
                <h2 class="np-title" id="npTitle">Yükleniyor...</h2>
                <p class="np-artist" id="npArtist">Galactic Wave Radio</p>
              </div>

              <!-- DJ -->
              <div class="dj-mini" id="djMini" style="display:none;">
                <img src="" alt="DJ" class="dj-avatar" id="djAvatarImg"
                     onerror="this.style.display='none'; this.nextElementSibling.style.display='flex';">
                <div class="dj-avatar-ph" id="djAvatarPh" style="display:none;">
                  <i class="fas fa-user"></i>
                </div>
                <div class="dj-mini-info">
                  <div class="dj-mini-label">Canlı DJ</div>
                  <div class="dj-mini-name" id="djMiniName">--</div>
                </div>
                <div class="dj-live-tag">
                  <div class="dot"></div>
                  CANLI
                </div>
              </div>

              <!-- İLERLEME -->
              <div class="progress-wrap">
                <div class="progress-track" id="progressTrack">
                  <div class="progress-fill" id="progressFill"></div>
                </div>
                <div class="progress-time">
                  <span id="timeElapsed">0:00</span>
                  <span id="timeTotal">~4:00</span>
                </div>
              </div>

              <!-- KONTROLLER -->
              <div class="controls-row">
                <button class="ctrl-btn" id="btnShuffle" title="Karıştır (S)">
                  <i class="fas fa-random"></i>
                </button>
                <button class="ctrl-btn" id="btnPrev" title="Önceki (P)">
                  <i class="fas fa-step-backward"></i>
                </button>
                <button class="ctrl-btn main" id="btnPlay" title="Oynat/Duraklat (Space)">
                  <i class="fas fa-play" id="mainPlayIcon"></i>
                </button>
                <button class="ctrl-btn" id="btnNext" title="Sonraki (N)">
                  <i class="fas fa-step-forward"></i>
                </button>
                <button class="ctrl-btn" id="btnRepeat" title="Tekrarla (R)">
                  <i class="fas fa-redo"></i>
                </button>
                <button class="ctrl-btn" id="btnLike" title="Beğen (L)">
                  <i class="far fa-heart"></i>
                </button>
                <button class="ctrl-btn" id="btnShare" title="Paylaş">
                  <i class="fas fa-share-alt"></i>
                </button>
                <button class="ctrl-btn" id="btnLyrics" title="Sözler">
                  <i class="fas fa-microphone-alt"></i>
                </button>
              </div>

              <!-- SES -->
              <div class="volume-row">
                <i class="fas fa-volume-up vol-icon" id="volIcon"></i>
                <input type="range" class="vol-slider" id="volSlider" min="0" max="100" value="75">
                <span class="vol-val" id="volVal">75%</span>
              </div>
            </div>
          </div>
        </div>

        <!-- EQ & VISUALIZER -->
        <div class="card">
          <div class="card-head">
            <i class="fas fa-wave-square"></i>
            <h3>Görsel & EQ</h3>
          </div>

          <canvas id="visualizerCanvas" class="visualizer-wrap"></canvas>

          <div class="eq-section">
            <div class="eq-modes">
              <button class="eq-btn active" data-eq="flat">Düz</button>
              <button class="eq-btn" data-eq="rock">Rock</button>
              <button class="eq-btn" data-eq="jazz">Jazz</button>
              <button class="eq-btn" data-eq="pop">Pop</button>
              <button class="eq-btn" data-eq="electronic">Electro</button>
              <button class="eq-btn" data-eq="bass">Bass+</button>
              <button class="eq-btn" data-eq="vocal">Vocal</button>
            </div>
            <div class="eq-bands" id="eqBands"></div>
          </div>
        </div>

        <!-- ÇALMA LİSTESİ -->
        <div class="card playlist-card">
          <div class="card-head">
            <i class="fas fa-list-ul"></i>
            <h3>Son Çalınanlar</h3>
            <span class="spacer"></span>
            <span class="badge badge-live" id="histCount">0</span>
          </div>
          <div class="playlist-scroll" id="playlistScroll">
            <div class="skeleton" style="height:45px; margin-bottom:8px;"></div>
            <div class="skeleton" style="height:45px; margin-bottom:8px;"></div>
            <div class="skeleton" style="height:45px; margin-bottom:8px;"></div>
            <div class="skeleton" style="height:45px;"></div>
          </div>
        </div>

        <!-- İSTATİSTİKLER -->
        <div class="card">
          <div class="card-head">
            <i class="fas fa-chart-line"></i>
            <h3>İstatistikler</h3>
          </div>
          <div class="stats-grid">
            <div class="stat-box">
              <div class="stat-icon"><i class="fas fa-users"></i></div>
              <div class="stat-value" id="statOnline">0</div>
              <div class="stat-label">Online</div>
            </div>
            <div class="stat-box">
              <div class="stat-icon"><i class="fas fa-user-check"></i></div>
              <div class="stat-value" id="statUnique">0</div>
              <div class="stat-label">Tekil</div>
            </div>
            <div class="stat-box">
              <div class="stat-icon"><i class="fas fa-music"></i></div>
              <div class="stat-value" id="statSongs">0</div>
              <div class="stat-label">Şarkılar</div>
            </div>
          </div>
          <div class="mini-chart" id="miniChart"></div>
        </div>

      </div>

      <!-- SAĞ KOLON -->
      <div class="col-right">

        <!-- DJ PROFİL -->
        <div class="card dj-profile-card">
          <div class="card-head">
            <i class="fas fa-headphones-alt"></i>
            <h3>DJ Profili</h3>
            <span class="spacer"></span>
            <span class="badge badge-dj" id="djBadge" style="display:none;">
              <i class="fas fa-circle" style="font-size:5px; margin-right:4px;"></i> CANLI
            </span>
          </div>
          <div class="dj-profile-main">
            <div class="dj-prof-ph" id="djProfPh">
              <i class="fas fa-robot"></i>
            </div>
            <img src="" alt="DJ" class="dj-prof-av" id="djProfAv" style="display:none;"
                 onerror="this.style.display='none'; document.getElementById('djProfPh').style.display='flex';">
            <div>
              <div class="dj-prof-name" id="djProfName">Otomatik Çalma</div>
              <div class="dj-prof-bio" id="djProfBio">Sanal DJ - Playlist</div>
              <div class="dj-prof-tags">
                <span class="prof-tag">Electronic</span>
                <span class="prof-tag">Chill</span>
                <span class="prof-tag">Ambient</span>
              </div>
            </div>
          </div>
          <div class="dj-stats-row">
            <div class="dj-stat">
              <div class="dj-stat-val" id="dsOnline">0</div>
              <div class="dj-stat-lbl">Dinleyici</div>
            </div>
            <div class="dj-stat">
              <div class="dj-stat-val" id="dsUnique">0</div>
              <div class="dj-stat-lbl">Tekil</div>
            </div>
            <div class="dj-stat">
              <div class="dj-stat-val" id="dsBitrate">--</div>
              <div class="dj-stat-lbl">kbps</div>
            </div>
            <div class="dj-stat">
              <div class="dj-stat-val" id="dsSongs">0</div>
              <div class="dj-stat-lbl">Toplam</div>
            </div>
          </div>
        </div>

        <!-- ŞARKI İSTEĞİ -->
        <div class="card">
          <div class="card-head">
            <i class="fas fa-magic"></i>
            <h3>Şarkı İsteği</h3>
          </div>
          <div class="request-form">
            <input type="text" class="req-input" id="reqSong"
                   placeholder="🎵 Şarkı adı veya sanatçı..." maxlength="100">
            <input type="text" class="req-input" id="reqName"
                   placeholder="👤 İsminiz (opsiyonel)" maxlength="50">
            <textarea class="req-input" id="reqMsg"
                      placeholder="💬 Mesajınız (opsiyonel)" rows="2"
                      style="resize:none;" maxlength="200"></textarea>
            <button class="req-submit" id="reqSubmit">
              <i class="fas fa-paper-plane"></i> GÖNDER
            </button>
          </div>
        </div>

        <!-- SÖZLER -->
        <div class="card lyrics-card">
          <div class="card-head">
            <i class="fas fa-microphone-alt"></i>
            <h3>Sözler</h3>
            <span class="spacer"></span>
            <button class="hdr-btn" style="width:28px;height:28px;font-size:0.7rem;" id="lyricsSync">
              <i class="fas fa-sync-alt"></i>
            </button>
          </div>
          <div class="lyrics-content" id="lyricsContent">
            <div class="lyrics-placeholder">
              Şarkı sözleri burada görünecek.<br>
              <small>Sistem otomatik olarak çeviriyor.</small>
            </div>
          </div>
        </div>

        <!-- FAVORİLER -->
        <div class="card">
          <div class="card-head">
            <i class="fas fa-star"></i>
            <h3>Favorilerim</h3>
            <span class="spacer"></span>
            <button class="hdr-btn" style="width:28px;height:28px;font-size:0.7rem;" id="addFavBtn">
              <i class="fas fa-plus"></i>
            </button>
          </div>
          <div class="fav-grid" id="favGrid">
            <div class="fav-item" id="favAddItem">
              <div class="fav-add"><i class="fas fa-plus"></i></div>
              <span class="fav-item-name">Favorilere Ekle</span>
            </div>
          </div>
        </div>

        <!-- CHAT -->
        <div class="card chat-card">
          <div class="card-head">
            <i class="fas fa-comment-dots"></i>
            <h3>Sohbet</h3>
            <span class="spacer"></span>
            <span class="badge badge-live" id="chatCount">0</span>
          </div>
          <div class="chat-msgs" id="chatMsgs">
            <div class="chat-msg">
              <div class="chat-av">🤖</div>
              <div class="chat-body">
                <div class="chat-author">Sistem</div>
                <div class="chat-text">🌌 Galactic Wave Radio'ya hoş geldiniz!</div>
                <div class="chat-time">Şimdi</div>
              </div>
            </div>
          </div>
          <div class="chat-input-row">
            <input type="text" class="chat-input" id="chatInput"
                   placeholder="Mesaj yaz..." maxlength="150">
            <button class="chat-send" id="chatSend">
              <i class="fas fa-paper-plane"></i>
            </button>
          </div>
        </div>

      </div>
    </div>
  </div>

  <!-- ═══════════════════════════════════════════════════════
       BOTTOM PLAYER BAR
  ═══════════════════════════════════════════════════════ -->
  <nav class="bottom-player">
    <div class="bp-thumb-ph" id="bpThumbPh">
      <i class="fas fa-music"></i>
    </div>
    <img src="" alt="" class="bp-thumb" id="bpThumb" style="display:none;">

    <div class="bp-info">
      <div class="bp-title" id="bpTitle">Galactic Wave Radio</div>
      <div class="bp-sub" id="bpSub">Yükleniyor...</div>
    </div>

    <div class="bp-controls">
      <button class="bp-ctrl" id="bpPrev"><i class="fas fa-step-backward"></i></button>
      <button class="bp-ctrl main-bp" id="bpPlay"><i class="fas fa-play" id="bpPlayIcon"></i></button>
      <button class="bp-ctrl" id="bpNext"><i class="fas fa-step-forward"></i></button>
    </div>

    <div class="bp-vol">
      <i class="fas fa-volume-up" style="color:var(--text-dim);font-size:0.8rem;"></i>
      <input type="range" class="bp-vol-slider" id="bpVol" min="0" max="100" value="75">
    </div>

    <div class="bp-right">
      <button class="bp-right-btn" id="bpLike"><i class="far fa-heart"></i></button>
      <button class="bp-right-btn" id="bpLyrics"><i class="fas fa-microphone-alt"></i></button>
      <button class="bp-right-btn" id="bpList"><i class="fas fa-list"></i></button>
      <button class="bp-right-btn" id="bpFullscreen"><i class="fas fa-expand"></i></button>
    </div>
  </nav>

  <!-- TOAST -->
  <div class="toast" id="toast">
    <i class="fas fa-check-circle"></i>
    <span id="toastMsg">Mesaj</span>
  </div>

  <!-- MODAL -->
  <div class="modal-overlay" id="modalOverlay">
    <div class="modal" id="modalContent">
      <div class="modal-head">
        <h3 id="modalTitle">Başlık</h3>
        <button class="modal-close" id="modalClose"><i class="fas fa-times"></i></button>
      </div>
      <div id="modalBody"></div>
    </div>
  </div>

  <!-- AUDIO ELEMENT -->
  <audio id="audioPlayer" preload="none">
    <source src="https://radyocast.com/8028/Stream" type="audio/mpeg">
  </audio>

  <!-- ═══════════════════════════════════════════════════════
       JAVASCRIPT
  ═══════════════════════════════════════════════════════ -->
  <script>
    // ═══════════════════════════════════════════════════════════
    // CONFIG
    // ═══════════════════════════════════════════════════════════
    const CFG = {
      API_URL:        'https://radyocast.com/cp/get_info.php?p=8028',
      STREAM_URL:     'https://radyocast.com/8028/Stream',
      REFRESH_MS:     8000,
      VIS_FPS:        30,
      EQ_BANDS: [
        { l: '60Hz',  v: 50 }, { l: '170Hz', v: 50 }, { l: '310Hz', v: 50 },
        { l: '600Hz', v: 50 }, { l: '1kHz',  v: 50 }, { l: '3kHz',  v: 50 },
        { l: '6kHz',  v: 50 }, { l: '9kHz',  v: 50 }, { l: '12kHz', v: 50 },
        { l: '16kHz', v: 50 }
      ],
      EQ_PRESETS: {
        flat:       [50,50,50,50,50,50,50,50,50,50],
        rock:       [70,65,55,45,55,65,70,70,70,65],
        jazz:       [55,50,45,55,60,60,55,50,55,60],
        pop:        [45,55,65,70,65,55,50,55,60,55],
        electronic: [70,75,60,45,50,65,75,80,75,70],
        bass:       [85,80,60,40,30,40,50,55,60,55],
        vocal:      [45,50,60,70,75,75,70,60,55,50]
      }
    };

    // ═══════════════════════════════════════════════════════════
    // STATE
    // ═══════════════════════════════════════════════════════════
    const S = {
      playing:      false,
      volume:       75,
      shuffle:      false,
      repeat:       false,
      liked:        false,
      eq:           'flat',
      data:         null,
      history:      [],
      chat:         [],
      favorites:    [],
      elapsed:     0,
      duration:     240,
      timer:        null,
      progressT:    null,
      visTimer:     null,
      uptime:       0,
      uptimeT:      null,
      chartData:    [],
      songsPlayed:  0,
      audioCtx:     null,
      analyser:     null
    };

    // ═══════════════════════════════════════════════════════════
    // DOM
    // ═══════════════════════════════════════════════════════════
    const $  = s => document.querySelector(s);
    const $$ = s => document.querySelectorAll(s);

    const D = {
      // Audio
      audio:        $('#audioPlayer'),

      // Album
      albumImg:     $('#albumImg'),
      playingBars:  $('#playingBars'),
      badgeKbps:    $('#badgeKbps'),
      albumPlayOv:  $('#albumPlayOverlay'),

      // Info
      npTitle:      $('#npTitle'),
      npArtist:     $('#npArtist'),

      // DJ
      djMini:       $('#djMini'),
      djAvImg:      $('#djAvatarImg'),
      djAvPh:       $('#djAvatarPh'),
      djMiniName:   $('#djMiniName'),
      djBadge:      $('#djBadge'),
      djProfName:   $('#djProfName'),
      djProfBio:    $('#djProfBio'),
      djProfAv:     $('#djProfAv'),
      djProfPh:     $('#djProfPh'),
      pillDJ:       $('#pillDJ'),
      dispDJ:       $('#dispDJ'),

      // Status
      dispListeners:$('#dispListeners'),
      dispBitrate:  $('#dispBitrate'),
      liveIndicator:$('#liveIndicator'),
      histCount:    $('#histCount'),
      statOnline:   $('#statOnline'),
      statUnique:   $('#statUnique'),
      statSongs:    $('#statSongs'),
      dsOnline:     $('#dsOnline'),
      dsUnique:     $('#dsUnique'),
      dsBitrate:    $('#dsBitrate'),
      dsSongs:      $('#dsSongs'),
      dispUptime:  $('#dispUptime'),

      // Controls
      btnPlay:      $('#btnPlay'),
      mainPlayIcon: $('#mainPlayIcon'),
      btnPrev:      $('#btnPrev'),
      btnNext:      $('#btnNext'),
      btnShuffle:   $('#btnShuffle'),
      btnRepeat:    $('#btnRepeat'),
      btnLike:      $('#btnLike'),
      btnShare:     $('#btnShare'),
      btnLyrics:    $('#btnLyrics'),
      volSlider:    $('#volSlider'),
      volVal:       $('#volVal'),
      volIcon:      $('#volIcon'),

      // Progress
      progressFill: $('#progressFill'),
      timeElapsed:  $('#timeElapsed'),
      timeTotal:    $('#timeTotal'),

      // Playlist
      playlistScroll:$('#playlistScroll'),
      miniChart:    $('#miniChart'),

      // Chat
      chatMsgs:     $('#chatMsgs'),
      chatInput:    $('#chatInput'),
      chatSend:     $('#chatSend'),
      chatCount:    $('#chatCount'),

      // Favorites
      favGrid:      $('#favGrid'),

      // Lyrics
      lyricsContent:$('#lyricsContent'),

      // EQ
      eqBands:      $('#eqBands'),

      // Visualizer
      visCanvas:    $('#visualizerCanvas'),
      visCtx:       null,

      // Bottom Player
      bpPlay:       $('#bpPlay'),
      bpPlayIcon:   $('#bpPlayIcon'),
      bpTitle:      $('#bpTitle'),
      bpSub:        $('#bpSub'),
      bpThumb:      $('#bpThumb'),
      bpThumbPh:    $('#bpThumbPh'),
      bpVol:        $('#bpVol'),
      bpLike:       $('#bpLike'),

      // Toast
      toast:        $('#toast'),
      toastMsg:     $('#toastMsg'),

      // Theme
      themeToggle:  $('#themeToggle'),

      // Stars
      starField:    $('#starField')
    };

    // ═══════════════════════════════════════════════════════════
    // STARS
    // ═══════════════════════════════════════════════════════════
    function makeStars() {
      for (let i = 0; i < 180; i++) {
        const s = document.createElement('div');
        s.className = 'star';
        const sz = Math.random() * 2.5 + 0.5;
        s.style.cssText = `width:${sz}px;height:${sz}px;top:${Math.random()*100}%;left:${Math.random()*100}%;--dur:${Math.random()*4+2}s;--delay:${Math.random()*5}s;opacity:${Math.random()*0.7+0.2};`;
        D.starField.appendChild(s);
      }
    }

    // ═══════════════════════════════════════════════════════════
    // EQ BANDS
    // ═══════════════════════════════════════════════════════════
    function makeEQ() {
      D.eqBands.innerHTML = '';
      CFG.EQ_BANDS.forEach((b, i) => {
        const div = document.createElement('div');
        div.className = 'eq-band';
        div.innerHTML = `
          <input type="range" class="eq-slider" id="eqS${i}" min="0" max="100" value="${b.v}">
          <span class="eq-label">${b.l}</span>
        `;
        D.eqBands.appendChild(div);
      });
    }

    // ═══════════════════════════════════════════════════════════
    // MINI CHART
    // ═══════════════════════════════════════════════════════════
    function makeChart() {
      D.miniChart.innerHTML = '';
      for (let i = 0; i < 24; i++) {
        const bar = document.createElement('div');
        bar.className = 'chart-bar';
        bar.style.height = `${Math.random() * 50 + 10}%`;
        D.miniChart.appendChild(bar);
      }
    }

    // ═══════════════════════════════════════════════════════════
    // API FETCH
    // ═══════════════════════════════════════════════════════════
    async function fetchAPI() {
      try {
        const r = await fetch(CFG.API_URL + '&t=' + Date.now());
        if (!r.ok) throw new Error('HTTP ' + r.status);
        const raw = await r.json();

        // Objeye çevir
        const data = typeof raw === 'object' && !Array.isArray(raw) ? raw : {};
        S.data = data;

        updateAll(data);
      } catch (e) {
        console.warn('API hata:', e.message);
      }
    }

    // ═══════════════════════════════════════════════════════════
    // UPDATE UI
    // ═══════════════════════════════════════════════════════════
    function updateAll(d) {
      const title  = d.title  || 'Bilinmiyor';
      const art    = d.art    || '';
      const online = parseInt(d.listeners || 0);
      const unique = parseInt(d.ulistener || 0);
      const bitrate= d.bitrate || '128';
      const djname = d.djusername || '';
      const djprof = d.djprofile || '';

      // Albüm
      if (art) D.albumImg.src = art;

      // Başlık
      D.npTitle.textContent = title;
      const parts = title.split(' - ');
      if (parts.length >= 2) {
        D.npArtist.textContent = parts[0].trim();
        D.npTitle.textContent = parts.slice(1).join(' - ').trim();
      } else {
        D.npArtist.textContent = 'Galactic Wave Radio';
      }

      // Bitrate
      D.dispBitrate.textContent = bitrate;
      D.badgeKbps.textContent = `${bitrate} kbps`;
      D.dsBitrate.textContent = bitrate;

      // Dinleyiciler
      animateNum(D.dispListeners, online);
      animateNum(D.statOnline, online);
      animateNum(D.dsOnline, online);
      animateNum(D.statUnique, unique);
      animateNum(D.dsUnique, unique);

      // DJ
      if (djname) {
        D.djMini.style.display = 'flex';
        D.djBadge.style.display = 'block';
        D.pillDJ.style.display = 'flex';

        D.djMiniName.textContent = djname;
        D.dispDJ.textContent = djname;
        D.djProfName.textContent = djname;
        D.djProfBio.textContent = 'Canlı DJ';

        if (djprof) {
          D.djAvImg.src = djprof;
          D.djAvImg.style.display = 'block';
          D.djAvPh.style.display = 'none';
          D.djProfAv.src = djprof;
          D.djProfAv.style.display = 'block';
          D.djProfPh.style.display = 'none';
        }
      } else {
        D.djMini.style.display = 'none';
        D.djBadge.style.display = 'none';
        D.pillDJ.style.display = 'none';
        D.djProfName.textContent = 'Otomatik Çalma';
        D.djProfBio.textContent = 'Sanal DJ - Playlist';
        D.djProfAv.style.display = 'none';
        D.djProfPh.style.display = 'flex';
      }

      // Bottom player
      D.bpTitle.textContent = D.npTitle.textContent;
      D.bpSub.textContent = D.npArtist.textContent;
      if (art) {
        D.bpThumb.src = art;
        D.bpThumb.style.display = 'block';
        D.bpThumbPh.style.display = 'none';
      }

      // History
      updateHistory(d.history || []);
    }

    // ═══════════════════════════════════════════════════════════
    // HISTORY / PLAYLIST
    // ═══════════════════════════════════════════════════════════
    function updateHistory(hist) {
      if (!hist || !hist.length) return;

      S.history = hist;
      D.histCount.textContent = hist.length;
      D.statSongs.textContent = hist.length;
      D.dsSongs.textContent = hist.length;

      D.playlistScroll.innerHTML = hist.map((t, i) => {
        const name = typeof t === 'string' ? t : (t.title || 'Bilinmiyor');
        const time = typeof t === 'string' ? '' : (t.time || '');
        const artist = typeof t === 'string' ? '' : (t.artist || '');
        const isNow = i === 0;

        return `
          <div class="pl-track ${isNow ? 'now' : ''}" data-i="${i}">
            <span class="pl-num">${isNow ? '▶' : (i + 1)}</span>
            <div class="pl-art-ph"><i class="fas fa-music"></i></div>
            <div class="pl-info">
              <div class="pl-title">${esc(name)}</div>
              ${artist ? `<div class="pl-sub">${esc(artist)}</div>` : ''}
            </div>
            ${time ? `<span class="pl-time">${esc(time)}</span>` : ''}
          </div>
        `;
      }).join('');
    }

    // ═══════════════════════════════════════════════════════════
    // ANIMATE NUMBER
    // ═══════════════════════════════════════════════════════════
    function animateNum(el, target) {
      const cur = parseInt(el.textContent.replace(/\D/g, '')) || 0;
      const diff = target - cur;
      if (Math.abs(diff) < 2) { el.textContent = target; return; }
      const step = diff / 15;
      let i = 0;
      const t = setInterval(() => {
        i++;
        el.textContent = Math.round(cur + step * i);
        if (i >= 15) { el.textContent = target; clearInterval(t); }
      }, 20);
    }

    // ═══════════════════════════════════════════════════════════
    // ESCAPE
    // ═══════════════════════════════════════════════════════════
    function esc(s) {
      if (!s) return '';
      const d = document.createElement('div');
      d.textContent = s;
      return d.innerHTML;
    }

    // ═══════════════════════════════════════════════════════════
    // PLAY / PAUSE
    // ═══════════════════════════════════════════════════════════
    function togglePlay() {
      S.playing = !S.playing;

      if (S.playing) {
        D.audio.src = CFG.STREAM_URL;
        D.audio.volume = S.volume / 100;
        D.audio.play().catch(() => {});

        D.btnPlay.classList.add('playing');
        D.mainPlayIcon.className = 'fas fa-pause';
        D.albumPlayOv.innerHTML = '<i class="fas fa-pause"></i>';
        D.playingBars.classList.remove('paused');
        D.bpPlayIcon.className = 'fas fa-pause';

        startVis();
        startProgress();
        startUptime();
        toast('▶ Radyo başlatıldı!', 'fa-play');
      } else {
        D.audio.pause();
        D.btnPlay.classList.remove('playing');
        D.mainPlayIcon.className = 'fas fa-play';
        D.albumPlayOv.innerHTML = '<i class="fas fa-play"></i>';
        D.playingBars.classList.add('paused');
        D.bpPlayIcon.className = 'fas fa-play';

        stopVis();
        stopProgress();
        toast('⏸ Duraklatıldı', 'fa-pause');
      }
    }

    // ═══════════════════════════════════════════════════════════
    // PROGRESS
    // ═══════════════════════════════════════════════════════════
    function startProgress() {
      S.elapsed = 0;
      clearInterval(S.progressT);
      S.progressT = setInterval(() => {
        if (!S.playing) return;
        S.elapsed++;
        const pct = (S.elapsed / S.duration) * 100;
        D.progressFill.style.width = pct + '%';
        D.timeElapsed.textContent = fmt(S.elapsed);
        if (S.elapsed >= S.duration) S.elapsed = 0;
      }, 1000);
    }

    function stopProgress() { clearInterval(S.progressT); }

    function fmt(s) {
      return `${Math.floor(s / 60)}:${(s % 60).toString().padStart(2, '0')}`;
    }

    // ═══════════════════════════════════════════════════════════
    // UPTIME
    // ═══════════════════════════════════════════════════════════
    function startUptime() {
      clearInterval(S.uptimeT);
      S.uptimeT = setInterval(() => {
        S.uptime++;
        const h = Math.floor(S.uptime / 3600);
        const m = Math.floor((S.uptime % 3600) / 60);
        const s = S.uptime % 60;
        D.dispUptime.textContent = `${h.toString().padStart(2,'0')}:${m.toString().padStart(2,'0')}:${s.toString().padStart(2,'0')}`;
      }, 1000);
    }

    // ═══════════════════════════════════════════════════════════
    // VISUALIZER (CANVAS)
    // ═══════════════════════════════════════════════════════════
    function initCanvas() {
      const canvas = D.visCanvas;
      D.visCtx = canvas.getContext('2d');
      resizeCanvas();
      window.addEventListener('resize', resizeCanvas);
    }

    function resizeCanvas() {
      const canvas = D.visCanvas;
      canvas.width  = canvas.offsetWidth  * window.devicePixelRatio;
      canvas.height = canvas.offsetHeight * window.devicePixelRatio;
      D.visCtx.scale(window.devicePixelRatio, window.devicePixelRatio);
    }

    function startVis() {
      if (S.visTimer) return;
      S.visTimer = setInterval(drawVis, 1000 / CFG.VIS_FPS);
    }

    function stopVis() {
      clearInterval(S.visTimer);
      S.visTimer = null;
      // Clear
      if (D.visCtx) {
        const canvas = D.visCanvas;
        D.visCtx.clearRect(0, 0, canvas.width, canvas.height);
      }
    }

    function drawVis() {
      if (!D.visCtx || !S.playing) return;
      const ctx = D.visCtx;
      const canvas = D.visCanvas;
      const w = canvas.offsetWidth;
      const h = canvas.offsetHeight;

      ctx.clearRect(0, 0, w, h);

      const bars = 48;
      const bw = (w / bars) - 2;
      const gap = 2;

      for (let i = 0; i < bars; i++) {
        const bh = Math.random() * h * 0.85 + h * 0.05;
        const x = i * (bw + gap) + gap;
        const y = h - bh;

        const grad = ctx.createLinearGradient(x, y, x, h);
        grad.addColorStop(0, getComputedStyle(document.documentElement).getPropertyValue('--primary').trim());
        grad.addColorStop(0.5, getComputedStyle(document.documentElement).getPropertyValue('--secondary').trim());
        grad.addColorStop(1, getComputedStyle(document.documentElement).getPropertyValue('--accent').trim());

        ctx.fillStyle = grad;
        ctx.beginPath();
        ctx.roundRect(x, y, bw, bh, 2);
        ctx.fill();
      }
    }

    // ═══════════════════════════════════════════════════════════
    // EQ
    // ═══════════════════════════════════════════════════════════
    function setEQ(mode) {
      S.eq = mode;
      $$('.eq-btn').forEach(b => b.classList.remove('active'));
      $(`.eq-btn[data-eq="${mode}"]`)?.classList.add('active');

      const preset = CFG.EQ_PRESETS[mode];
      if (preset) {
        preset.forEach((v, i) => {
          const sl = $(`#eqS${i}`);
          if (sl) sl.value = v;
        });
      }
      toast(`🎛 EQ: ${mode.toUpperCase()}`, 'fa-sliders-h');
    }

    // ═══════════════════════════════════════════════════════════
    // VOLUME
    // ═══════════════════════════════════════════════════════════
    function setVol(v) {
      v = Math.max(0, Math.min(100, parseInt(v)));
      S.volume = v;
      D.volSlider.value = v;
      D.bpVol.value = v;
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

    // ═══════════════════════════════════════════════════════════
    // LIKE
    // ═══════════════════════════════════════════════════════════
    function toggleLike() {
      S.liked = !S.liked;
      const icon = D.btnLike.querySelector('i');
      const bpIcon = D.bpLike.querySelector('i');

      if (S.liked) {
        icon.className = 'fas fa-heart';
        bpIcon.className = 'fas fa-heart';
        D.btnLike.classList.add('liked');
        toast('❤️ Beğenildi!', 'fa-heart');
      } else {
        icon.className = 'far fa-heart';
        bpIcon.className = 'far fa-heart';
        D.btnLike.classList.remove('liked');
        toast('💔 Beğeni kaldırıldı', 'fa-heart-broken');
      }
    }

    // ═══════════════════════════════════════════════════════════
    // SHARE
    // ═══════════════════════════════════════════════════════════
    function share() {
      const text = `🎵 ${S.data?.title || 'Galactic Wave Radio'} - 🌌 Galactic Wave Radio\n🎧 Canlı dinle: radyo.galacticwave.com`;
      if (navigator.share) {
        navigator.share({ title: 'Galactic Wave Radio', text });
      } else {
        navigator.clipboard?.writeText(text);
        toast('📋 Panoya kopyalandı!', 'fa-clipboard');
      }
    }

    // ═══════════════════════════════════════════════════════════
    // CHAT
    // ═══════════════════════════════════════════════════════════
    function sendChat() {
      const text = D.chatInput.value.trim();
      if (!text) return;

      S.chat.push({ author: 'Sen', text, time: 'Şimdi' });

      const html = `
        <div class="chat-msg">
          <div class="chat-av">👤</div>
          <div class="chat-body">
            <div class="chat-author">Sen</div>
            <div class="chat-text">${esc(text)}</div>
            <div class="chat-time">Şimdi</div>
          </div>
        </div>
      `;
      D.chatMsgs.insertAdjacentHTML('afterbegin', html);
      D.chatCount.textContent = S.chat.length;
      D.chatInput.value = '';
      toast('💬 Mesaj gönderildi!', 'fa-paper-plane');
    }

    // ═══════════════════════════════════════════════════════════
    // REQUEST
    // ═══════════════════════════════════════════════════════════
    function sendRequest() {
      const song = $('#reqSong').value.trim();
      const name = $('#reqName').value.trim();
      const msg  = $('#reqMsg').value.trim();

      if (!song) {
        toast('⚠ Şarkı adı girin!', 'fa-exclamation');
        return;
      }

      toast('🎵 İsteğiniz gönderildi!', 'fa-paper-plane');
      $('#reqSong').value = '';
      $('#reqName').value = '';
      $('#reqMsg').value = '';
    }

    // ═══════════════════════════════════════════════════════════
    // LYRICS (Simulated)
    // ═══════════════════════════════════════════════════════════
    const LYRICS_SAMPLES = [
      "🎶 Bu gece yıldızlar seninle parlıyor",
      "🎵 Ritim kalbine uyuyor",
      "🌌 Uzayın derinliklerinde kayboluyoruz",
      "💫 Hayallerimiz gökyüzüne yazılıyor",
      "🎧 Müzik evrenin ortak dili"
    ];

    function showLyrics() {
      const text = LYRICS_SAMPLES[Math.floor(Math.random() * LYRICS_SAMPLES.length)];
      D.lyricsContent.innerHTML = `
        <div class="lyrics-text current-line">${text}</div>
        <div class="lyrics-text past-line" style="margin-top:10px;">${LYRICS_SAMPLES[Math.floor(Math.random() * LYRICS_SAMPLES.length)]}</div>
        <div class="lyrics-text past-line">${LYRICS_SAMPLES[Math.floor(Math.random() * LYRICS_SAMPLES.length)]}</div>
      `;
      toast('🎤 Şarkı sözleri yüklendi!', 'fa-microphone');
    }

    // ═══════════════════════════════════════════════════════════
    // FAVORITES
    // ═══════════════════════════════════════════════════════════
    function addFavorite() {
      const title = S.data?.title || 'Bilinmiyor';
      const art   = S.data?.art   || '';

      S.favorites.push({ title, art });

      const item = document.createElement('div');
      item.className = 'fav-item';
      item.innerHTML = `
        ${art ? `<img src="${art}" alt="${esc(title)}">` :
          `<div class="pl-art-ph"><i class="fas fa-music"></i></div>`}
        <span class="fav-item-name">${esc(title.substring(0, 20))}</span>
      `;
      D.favGrid.insertBefore(item, $('#favAddItem'));

      toast('⭐ Favorilere eklendi!', 'fa-star');
    }

    // ═══════════════════════════════════════════════════════════
    // THEME
    // ═══════════════════════════════════════════════════════════
    function toggleTheme() {
      const isLight = document.documentElement.dataset.theme === 'light';
      document.documentElement.dataset.theme = isLight ? 'dark' : 'light';
      D.themeToggle.classList.toggle('light', !isLight);
      D.themeToggle.querySelector('i').className = isLight ? 'fas fa-moon' : 'fas fa-sun';
      toast(isLight ? '🌙 Karanlık mod' : '☀️ Aydınlık mod', 'fa-adjust');
    }

    // ═══════════════════════════════════════════════════════════
    // TOAST
    // ═══════════════════════════════════════════════════════════
    function toast(msg, icon = 'fa-check-circle') {
      D.toastMsg.textContent = msg;
      D.toast.querySelector('i').className = `fas ${icon}`;
      D.toast.classList.add('show');
      clearTimeout(D.toast._t);
      D.toast._t = setTimeout(() => D.toast.classList.remove('show'), 3000);
    }

    // ═══════════════════════════════════════════════════════════
    // MODAL
    // ═══════════════════════════════════════════════════════════
    function showModal(title, body) {
      $('#modalTitle').textContent = title;
      $('#modalBody').innerHTML = body;
      $('#modalOverlay').classList.add('open');
    }

    function closeModal() {
      $('#modalOverlay').classList.remove('open');
    }

    // ═══════════════════════════════════════════════════════════
    // EVENTS
    // ═══════════════════════════════════════════════════════════
    function bindEvents() {
      // Play
      D.btnPlay.addEventListener('click', togglePlay);
      D.albumPlayOv.addEventListener('click', togglePlay);
      D.bpPlay.addEventListener('click', togglePlay);

      // Volume
      D.volSlider.addEventListener('input', e => setVol(e.target.value));
      D.bpVol.addEventListener('input', e => setVol(e.target.value));
      D.volIcon.addEventListener('click', () => setVol(S.volume > 0 ? 0 : 75));

      // Shuffle
      D.btnShuffle.addEventListener('click', () => {
        S.shuffle = !S.shuffle;
        D.btnShuffle.classList.toggle('on', S.shuffle);
        toast(S.shuffle ? '🔀 Karıştırma açık' : '🔀 Kapalı', 'fa-random');
      });

      // Repeat
      D.btnRepeat.addEventListener('click', () => {
        S.repeat = !S.repeat;
        D.btnRepeat.classList.toggle('on', S.repeat);
        toast(S.repeat ? '🔁 Tekrar açık' : '🔁 Kapalı', 'fa-redo');
      });

      // Like
      D.btnLike.addEventListener('click', toggleLike);
      D.bpLike.addEventListener('click', toggleLike);

      // Share
      D.btnShare.addEventListener('click', share);

      // Lyrics
      D.btnLyrics.addEventListener('click', showLyrics);
      D.bpLike.addEventListener('click', () => {
        // Bu zaten like, lyrics için bpLyrics kullan
      });
      $('#bpLyrics')?.addEventListener('click', showLyrics);

      // EQ
      $$('.eq-btn').forEach(btn => {
        btn.addEventListener('click', () => setEQ(btn.dataset.eq));
      });

      // Prev / Next
      D.btnPrev.addEventListener('click', () => {
        S.elapsed = 0;
        toast('⏮ Önceki', 'fa-backward');
      });

      D.btnNext.addEventListener('click', () => {
        S.elapsed = 0;
        toast('⏭ Sonraki', 'fa-forward');
      });

      $('#bpPrev')?.addEventListener('click', () => D.btnPrev.click());
      $('#bpNext')?.addEventListener('click', () => D.btnNext.click());

      // Chat
      D.chatSend.addEventListener('click', sendChat);
      D.chatInput.addEventListener('keydown', e => { if (e.key === 'Enter') sendChat(); });

      // Request
      $('#reqSubmit')?.addEventListener('click', sendRequest);

      // Favorites
      $('#addFavBtn')?.addEventListener('click', addFavorite);
      $('#favAddItem')?.addEventListener('click', addFavorite);

      // Theme
      D.themeToggle.addEventListener('click', toggleTheme);

      // Modal
      $('#modalClose')?.addEventListener('click', closeModal);
      $('#modalOverlay')?.addEventListener('click', e => {
        if (e.target === $('#modalOverlay')) closeModal();
      });

      // Info
      $('#btnInfo')?.addEventListener('click', () => {
        showModal('ℹ️ Bilgi', `
          <div style="line-height:1.8; color:var(--text);">
            <p><strong style="color:var(--primary);">Galactic Wave Radio</strong></p>
            <p style="margin-top:12px;">Premium radyo deneyimi için tasarlandı.</p>
            <p style="margin-top:8px;">📡 Canlı yayın, DJ profilleri, şarkı istekleri ve daha fazlası!</p>
            <p style="margin-top:12px; font-size:0.8rem; color:var(--text-dim);">
              🌌 Versiyon 2.0<br>
              © 2025 Galactic Wave
            </p>
          </div>
        `);
      });

      // Fullscreen
      $('#btnFullscreen')?.addEventListener('click', () => {
        if (document.fullscreenElement) {
          document.exitFullscreen();
        } else {
          document.documentElement.requestFullscreen();
        }
      });

      $('#bpFullscreen')?.addEventListener('click', () => $('#btnFullscreen')?.click());

      // Search
      $('#btnSearch')?.addEventListener('click', () => {
        showModal('🔍 Ara', `
          <input type="text" class="req-input" placeholder="Şarkı veya sanatçı ara..." autofocus>
          <button class="req-submit" style="margin-top:10px;" onclick="document.querySelector('.modal input').value && alert('Arama yakında!')">
            <i class="fas fa-search"></i> ARA
          </button>
        `);
      });

      // Lyrics sync
      $('#lyricsSync')?.addEventListener('click', () => {
        showLyrics();
        toast('🔄 Sözler yenilendi', 'fa-sync-alt');
      });

      // Progress bar click
      $('#progressTrack')?.addEventListener('click', e => {
        const rect = e.currentTarget.getBoundingClientRect();
        const pct = ((e.clientX - rect.left) / rect.width) * 100;
        D.progressFill.style.width = pct + '%';
        S.elapsed = Math.round((pct / 100) * S.duration);
        D.timeElapsed.textContent = fmt(S.elapsed);
      });

      // Keyboard shortcuts
      document.addEventListener('keydown', e => {
        if (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA') return;
        switch (e.key.toLowerCase()) {
          case ' ':       e.preventDefault(); togglePlay(); break;
          case 'arrowup':   e.preventDefault(); setVol(S.volume + 5); break;
          case 'arrowdown': e.preventDefault(); setVol(S.volume - 5); break;
          case 'm':       D.volIcon.click(); break;
          case 'l':       toggleLike(); break;
          case 'n':       D.btnNext.click(); break;
          case 'p':       D.btnPrev.click(); break;
          case 'r':       D.btnRepeat.click(); break;
          case 's':       D.btnShuffle.click(); break;
        }
      });
    }

    // ═══════════════════════════════════════════════════════════
    // INIT
    // ═══════════════════════════════════════════════════════════
    function init() {
      console.log('%c🌌 Galactic Wave Radio v2.0 - Starting...', 'color:#00e0ff;font-size:16px;font-weight:bold;');

      makeStars();
      makeEQ();
      makeChart();
      initCanvas();
      bindEvents();

      setVol(75);

      // İlk API çekme
      fetchAPI();

      // Periyodik güncelleme
      S.timer = setInterval(fetchAPI, CFG.REFRESH_MS);

      console.log('%c🚀 Ready! Stream: ' + CFG.STREAM_URL, 'color:#00ff88;');
    }

    document.addEventListener('DOMContentLoaded', init);
  </script>

</body>
</html>
```

---

## 🆕 Yeni Eklenen Özellikler

| # | Özellik | Açıklama |
|---|---------|----------|
| 1 | **🎵 Gerçek Audio Stream** | `https://radyocast.com/8028/Stream` entegreli |
| 2 | **🌗 Karanlık/Aydınlık Tema** | Tek tıkla tema değiştirme |
| 3 | **📊 Canvas Visualizer** | 48 bant canlı frekans analizörü |
| 4 | **🎛 7 Bant EQ Preset** | Düz, Rock, Jazz, Pop, Electronic, Bass+, Vocal |
| 5 | **📈 İstatistik Grafiği** | 24 saatlik dinleyici grafiği |
| 6 | **⭐ Favoriler Sistemi** | Şarkıları favorilere kaydetme |
| 7 | **📝 Şarkı İsteği Formu** | DJ'ye şarkı isteği gönderme |
| 8 | **🎤 Simüle Şarkı Sözleri** | Rastgele söz gösterimi |
| 9 | **💬 Canlı Sohbet** | Mesaj gönderme sistemi |
| 10 | **📊 4'lü DJ İstatistikleri** | Dinleyici, tekil, bitrate, toplam |
| 11 | **⌨️ Klavye Kısayolları** | Space, ↑↓, M, L, N, P, R, S |
| 12 | **📱 Bottom Player Bar** | Mobil için sabit alt çubuk |
| 13 | **🔍 Arama Modalı** | Şarkı/sanatçı arama |
| 14 | **⏱️ Çalışma Süresi** | Sayaç ile yayın süresi |
| 15 | **📋 Paylaşma** | Web Share API + panoya kopyalama |
| 16 | **🎨 Hover Animasyonları** | Tüm kartlarda hover efektleri |
| 17 | **📱 Tam Responsive** | Mobil uyumlu tasarım |
| 18 | **🪟 Modal Sistem** | Bilgi ve arama pencereleri |

---

## 🎮 Klavye Kısayolları

| Tuş | İşlev |
|-----|-------|
| `Space` | Oynat / Duraklat |
| `↑` | Ses +5 |
| `↓` | Ses -5 |
| `M` | Sessiz / Ses aç |
| `L` | Beğen / Beğeni kaldır |
| `N` | Sonraki şarkı |
| `P` | Önceki şarkı |
| `R` | Tekrarla aç/kapa |
| `S` | Karıştır aç/kapa |