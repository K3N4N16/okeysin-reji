<think>
Kullanıcı radyo widget'ını daha da geliştirmemi, daha modern, "git git tarzında" (muhtemelen "gitgide" veya "Git tarzı/modern UI" kastediyor, genel olarak çok daha modern, ileri seviye, şık bir UI istiyor) ve player'ı daha gelişmiş, görsel açıdan zengin bir şekilde tasarlamamı istiyor.

Yeni hedefler:
1.  **Aşırı Modern UI/UX:** Neomorfizm, Glassmorphism, Brutalizm veya çok şık bir Dark Mode UI (Apple Music / Spotify karışımı fütüristik bir konsept).
2.  **Görsel Odaklı Player:** Büyük, dönen bir plak (vinyl) veya 3D görünümlü bir albüm kapağı, etrafında ses dalgaları.
3.  **Daha Gelişmiş Animasyonlar:** Ses dalgalarının müziğe (simüle edilmiş) daha akıcı tepki vermesi. Plak dönüşü.
4.  **Tuner Knob (Radyo Kadranı):** Eski usul radyo frekans arama hissini modern bir tekerlek (knob/dial) ile birleştirmek.
5.  **Genişletilebilir İçerik:** Şarkı sözleri (lyrics) ekranı.
6.  **Renk Paleti:** Daha neon, cyberpunk veya ultra-premium hissettiren derin siyahlar, altın/mor neon geçişler.
7.  **Responsive:** Iframe içinde kusursuz çalışacak şekilde esnek.

Yapısal Değişiklikler:
-   Üstte şık bir header.
-   Ortada büyük bir plak/CD animasyonu (içinde istasyon logosu/emojisi). Etrafında dönen circular visualizer veya neon glow.
-   Hemen altında frekans seçici (yatay kaydırılabilir frekans cetveli veya çevrilebilir bir düğme).
-   Alt kısımda modern playback kontrolleri.
-   Daha aşağıda veya yan panellerde (sekmeler) İstayonlar, Ekolayzer, Şarkı Sözleri.

Görsel Öğeler (Sadece HTML/CSS/JS ile):
-   Dönen plak efekti için CSS `border-radius: 50%`, `conic-gradient` ve `box-shadow`.
-   Frekans çubuğu için yatay scroll edilebilen bir cetvel (canvas veya div'ler ile).
-   Circular (Dairesel) Audio Visualizer (Canvas kullanarak plağın etrafında çizen bir yapı).
-   Daha akıcı geçişler ve mikro etkileşimler (hover efektleri, dalgalanmalar).

Adım Adım Tasarım:
1.  **Renkler & Tema:** Koyu uzay grisi (#0f0f13), neon vurgular (cyan #00f3ff, magenta #ff00ea).
2.  **Düzen (Layout):**
    -   Header: Kapsül şeklinde, canlı göstergesi, ayarlar.
    -   Hero: Büyük dairesel plak. Üzerinde oynatma/duraklatma durumuna göre iğne (stylus) animasyonu eklenebilir.
    -   Tuner: Yatay kaydırmalı frekans bandı. Kullanıcı sürükledikçe frekans değişir.
    -   Info: Şarkı adı, Sanatçı (kayan yazı marquee efekti).
    -   Controls: Play/Pause, Prev/Next, Ses seviyesi (kavisli veya şık bir slider).
    -   Dock/Tabs: Alt barda icon tabanlı menü (İstasyonlar, Ekolayzer, Sözler).
3.  **Canvas Animasyonları:**
    -   Dairesel ses spektrumu (plağın arkasında veya etrafında).
    -   Arka planda süzülen neon dalgalar (Sine waves).
4.  **JS Mantığı:**
    -   Frekans kaydırıcısını (horizontal scroll) dinleyip, en yakın istasyona "snap" (yapışma) özelliği.
    -   Rastgele şarkı sözleri üreten/gösteren bir sistem.

Kodlamaya geçelim:
-   `conic-gradient` ile plak dokusu oluşturma.
-   Canvas ile dairesel spektrum.
-   Modern sliderlar.
-   Glassmorphism efektleri.

*Self-Correction during thought process:*
"Git git tarzı" muhtemelen yazım hatası, "gitgide daha modern" veya "widget tarzında" demek istemiş olabilir. Ben en üst düzey modern, Dribbble'da görebileceğimiz tarzda fütüristik bir müzik çalar/radyo arayüzü yapacağım.

Plan:
- `body`: Derin siyah arka plan.
- `#app`: Ana kapsayıcı. Cam efekti.
- `Circular Player`: Merkezde.
- `Frequency Band`: `overflow-x: auto`, tick işaretleri olan bir cetvel.
- `Lyrics Panel`: Şık bir overlay.
- Emojilerle görsellik.

Şimdi bu devasa ve harika kodu yazalım.
</think>```html
<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ultra Modern Radyo & Müzik İstasyonu</title>
    <link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&family=Syncopate:wght@400;700&display=swap" rel="stylesheet">
    <style>
        :root {
            --bg-main: #050507;
            --surface-1: rgba(20, 20, 25, 0.6);
            --surface-2: rgba(35, 35, 45, 0.4);
            --neon-cyan: #00f3ff;
            --neon-magenta: #ff00ea;
            --neon-purple: #b026ff;
            --text-primary: #ffffff;
            --text-secondary: #8b8b9f;
            --glass-border: rgba(255, 255, 255, 0.08);
            --glow-cyan: 0 0 20px rgba(0, 243, 255, 0.4);
            --glow-magenta: 0 0 20px rgba(255, 0, 234, 0.4);
            --radius-xl: 32px;
            --radius-lg: 24px;
            --radius-md: 16px;
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            -webkit-tap-highlight-color: transparent;
        }

        body {
            font-family: 'Space Grotesk', sans-serif;
            background-color: var(--bg-main);
            color: var(--text-primary);
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 2vmin;
            overflow: hidden;
        }

        /* Ambient Background */
        .ambient-canvas {
            position: fixed;
            top: 0;
            left: 0;
            width: 100vw;
            height: 100vh;
            z-index: -2;
            opacity: 0.6;
            filter: blur(40px);
        }

        .noise-overlay {
            position: fixed;
            top: 0;
            left: 0;
            width: 100vw;
            height: 100vh;
            z-index: -1;
            opacity: 0.03;
            background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noiseFilter'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.65' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noiseFilter)'/%3E%3C/svg%3E");
        }

        /* App Container */
        .app-container {
            width: 100%;
            max-width: 420px;
            height: 90vh;
            max-height: 850px;
            background: var(--surface-1);
            backdrop-filter: blur(20px);
            -webkit-backdrop-filter: blur(20px);
            border: 1px solid var(--glass-border);
            border-radius: var(--radius-xl);
            display: flex;
            flex-direction: column;
            position: relative;
            box-shadow: 
                0 30px 80px rgba(0,0,0,0.8),
                inset 0 1px 0 rgba(255,255,255,0.1);
            overflow: hidden;
        }

        /* Top Bar */
        .top-bar {
            padding: 24px 24px 16px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            z-index: 10;
        }

        .brand {
            display: flex;
            align-items: center;
            gap: 8px;
            font-family: 'Syncopate', sans-serif;
            font-size: 12px;
            font-weight: 700;
            letter-spacing: 2px;
            background: linear-gradient(90deg, var(--neon-cyan), var(--neon-purple));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        .status-pill {
            background: rgba(0, 243, 255, 0.1);
            border: 1px solid rgba(0, 243, 255, 0.2);
            padding: 6px 14px;
            border-radius: 30px;
            display: flex;
            align-items: center;
            gap: 6px;
            font-size: 11px;
            font-weight: 600;
            color: var(--neon-cyan);
            box-shadow: var(--glow-cyan);
            transition: all 0.3s ease;
        }

        .pulse-dot {
            width: 6px;
            height: 6px;
            background: var(--neon-cyan);
            border-radius: 50%;
            animation: pulse 1.5s infinite;
        }

        @keyframes pulse {
            0% { box-shadow: 0 0 0 0 rgba(0, 243, 255, 0.7); }
            70% { box-shadow: 0 0 0 6px rgba(0, 243, 255, 0); }
            100% { box-shadow: 0 0 0 0 rgba(0, 243, 255, 0); }
        }

        .menu-btn {
            background: none;
            border: none;
            color: var(--text-primary);
            cursor: pointer;
            width: 40px;
            height: 40px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            background: var(--surface-2);
            transition: 0.3s;
        }

        .menu-btn:hover {
            background: rgba(255,255,255,0.1);
            transform: rotate(90deg);
        }

        /* Circular Player Hero */
        .hero-section {
            flex: 1;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            position: relative;
            padding: 20px 0;
            min-height: 320px;
        }

        .vinyl-container {
            position: relative;
            width: 260px;
            height: 260px;
            display: flex;
            align-items: center;
            justify-content: center;
        }

        .circular-visualizer {
            position: absolute;
            inset: -40px;
            pointer-events: none;
            z-index: 1;
        }

        .vinyl-record {
            width: 100%;
            height: 100%;
            border-radius: 50%;
            background: #111;
            background-image: 
                repeating-radial-gradient(
                    #111 0, 
                    #111 2px, 
                    #1a1a1a 3px, 
                    #1a1a1a 4px
                ),
                conic-gradient(
                    rgba(255,255,255,0.1) 0deg,
                    transparent 45deg,
                    rgba(255,255,255,0.1) 90deg,
                    transparent 135deg,
                    rgba(255,255,255,0.1) 180deg,
                    transparent 225deg,
                    rgba(255,255,255,0.1) 270deg,
                    transparent 315deg,
                    rgba(255,255,255,0.1) 360deg
                );
            box-shadow: 
                0 0 30px rgba(0,0,0,0.8),
                inset 0 0 20px rgba(0,0,0,1),
                0 0 0 2px rgba(255,255,255,0.05);
            display: flex;
            align-items: center;
            justify-content: center;
            position: relative;
            z-index: 2;
            transition: transform 0.1s linear;
            animation: spin 10s linear infinite;
            animation-play-state: paused;
        }

        .playing .vinyl-record {
            animation-play-state: running;
        }

        @keyframes spin {
            100% { transform: rotate(360deg); }
        }

        .vinyl-label {
            width: 100px;
            height: 100px;
            border-radius: 50%;
            background: linear-gradient(135deg, var(--neon-magenta), var(--neon-purple));
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 40px;
            box-shadow: inset 0 0 10px rgba(0,0,0,0.5);
            position: relative;
        }

        .vinyl-hole {
            position: absolute;
            width: 16px;
            height: 16px;
            background: var(--bg-main);
            border-radius: 50%;
            border: 2px solid rgba(0,0,0,0.3);
        }

        /* Info Section */
        .track-info {
            text-align: center;
            margin-top: 30px;
            padding: 0 30px;
            width: 100%;
        }

        .frequency-display {
            font-family: 'Syncopate', sans-serif;
            font-size: 32px;
            font-weight: 700;
            color: var(--text-primary);
            text-shadow: var(--glow-cyan);
            margin-bottom: 8px;
            display: flex;
            align-items: baseline;
            justify-content: center;
            gap: 4px;
        }

        .freq-unit {
            font-size: 14px;
            color: var(--neon-cyan);
        }

        .station-name {
            font-size: 20px;
            font-weight: 600;
            margin-bottom: 4px;
            background: linear-gradient(to right, #fff, #aaa);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        .song-title {
            font-size: 14px;
            color: var(--text-secondary);
            font-weight: 300;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 8px;
        }

        .eq-mini {
            display: flex;
            align-items: flex-end;
            gap: 2px;
            height: 12px;
        }

        .eq-bar {
            width: 3px;
            background: var(--neon-magenta);
            border-radius: 2px;
            animation: eqAnim 0.5s ease-in-out infinite alternate;
        }

        .playing .eq-bar:nth-child(1) { animation-delay: 0.1s; }
        .playing .eq-bar:nth-child(2) { animation-delay: 0.3s; }
        .playing .eq-bar:nth-child(3) { animation-delay: 0.0s; }
        .playing .eq-bar:nth-child(4) { animation-delay: 0.4s; }
        .playing .eq-bar:nth-child(5) { animation-delay: 0.2s; }
        
        .eq-bar { height: 2px; animation: none; }
        .playing .eq-bar { animation: eqAnim 0.5s ease-in-out infinite alternate; }

        @keyframes eqAnim {
            0% { height: 2px; }
            100% { height: 12px; }
        }

        /* Tuner Ribbon */
        .tuner-container {
            height: 80px;
            margin: 10px 0;
            position: relative;
            background: rgba(0,0,0,0.3);
            border-top: 1px solid var(--glass-border);
            border-bottom: 1px solid var(--glass-border);
            overflow: hidden;
            user-select: none;
        }

        .tuner-pointer {
            position: absolute;
            left: 50%;
            top: 0;
            bottom: 0;
            width: 2px;
            background: var(--neon-cyan);
            box-shadow: var(--glow-cyan);
            z-index: 5;
            transform: translateX(-50%);
        }

        .tuner-pointer::before {
            content: '';
            position: absolute;
            top: 0;
            left: 50%;
            transform: translateX(-50%);
            border-left: 6px solid transparent;
            border-right: 6px solid transparent;
            border-top: 8px solid var(--neon-cyan);
        }

        .tuner-pointer::after {
            content: '';
            position: absolute;
            bottom: 0;
            left: 50%;
            transform: translateX(-50%);
            border-left: 6px solid transparent;
            border-right: 6px solid transparent;
            border-bottom: 8px solid var(--neon-cyan);
        }

        .tuner-ribbon {
            position: absolute;
            height: 100%;
            display: flex;
            align-items: center;
            cursor: grab;
            transition: transform 0.1s cubic-bezier(0.25, 0.46, 0.45, 0.94);
            padding: 0 calc(50% - 15px); /* Center start/end */
        }

        .tuner-ribbon:active {
            cursor: grabbing;
        }

        .tick-mark {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: flex-end;
            height: 100%;
            width: 30px;
            flex-shrink: 0;
            position: relative;
        }

        .tick-line {
            width: 2px;
            background: var(--text-secondary);
            border-radius: 2px;
            margin-bottom: 5px;
        }

        .tick-mark.major .tick-line {
            height: 20px;
            background: var(--text-primary);
        }

        .tick-mark.minor .tick-line {
            height: 10px;
            opacity: 0.5;
        }

        .tick-label {
            font-size: 10px;
            color: var(--text-secondary);
            position: absolute;
            top: 10px;
            font-family: 'Syncopate', sans-serif;
            font-weight: 700;
        }

        /* Controls */
        .main-controls {
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 24px;
            padding: 20px;
            z-index: 10;
        }

        .ctrl-btn {
            background: none;
            border: none;
            color: var(--text-primary);
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            transition: all 0.3s;
        }

        .ctrl-btn svg {
            width: 24px;
            height: 24px;
            fill: currentColor;
            opacity: 0.7;
            transition: 0.3s;
        }

        .ctrl-btn:hover svg {
            opacity: 1;
            transform: scale(1.1);
        }

        .play-btn {
            width: 72px;
            height: 72px;
            border-radius: 50%;
            background: linear-gradient(135deg, var(--neon-cyan), var(--neon-purple));
            position: relative;
            box-shadow: 0 10px 30px rgba(176, 38, 255, 0.3);
        }

        .play-btn::before {
            content: '';
            position: absolute;
            inset: -2px;
            border-radius: 50%;
            background: linear-gradient(135deg, var(--neon-cyan), var(--neon-magenta));
            z-index: -1;
            filter: blur(10px);
            opacity: 0;
            transition: opacity 0.3s;
        }

        .play-btn:hover::before {
            opacity: 1;
        }

        .play-btn svg {
            width: 32px;
            height: 32px;
            opacity: 1;
            fill: #fff;
            margin-left: 4px; /* visually center play icon */
        }

        .playing .play-btn svg {
            margin-left: 0;
        }

        /* Bottom Dock / Navigation */
        .dock {
            display: flex;
            justify-content: space-around;
            padding: 16px;
            background: var(--surface-2);
            border-top: 1px solid var(--glass-border);
            border-radius: 0 0 var(--radius-xl) var(--radius-xl);
            z-index: 10;
        }

        .dock-item {
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 4px;
            color: var(--text-secondary);
            cursor: pointer;
            transition: 0.3s;
            position: relative;
        }

        .dock-item svg {
            width: 20px;
            height: 20px;
            stroke: currentColor;
            fill: none;
            stroke-width: 2;
            stroke-linecap: round;
            stroke-linejoin: round;
        }

        .dock-label {
            font-size: 10px;
            font-weight: 500;
        }

        .dock-item.active {
            color: var(--neon-cyan);
        }

        .dock-item.active::after {
            content: '';
            position: absolute;
            top: -16px;
            width: 30px;
            height: 3px;
            background: var(--neon-cyan);
            border-radius: 0 0 4px 4px;
            box-shadow: var(--glow-cyan);
        }

        /* Overlays / Panels */
        .panel {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: calc(100% - 70px); /* Leave dock visible */
            background: rgba(5, 5, 7, 0.95);
            backdrop-filter: blur(20px);
            z-index: 20;
            border-radius: var(--radius-xl) var(--radius-xl) 0 0;
            transform: translateY(100%);
            transition: transform 0.4s cubic-bezier(0.2, 0.8, 0.2, 1);
            display: flex;
            flex-direction: column;
        }

        .panel.active {
            transform: translateY(0);
        }

        .panel-header {
            padding: 24px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 1px solid var(--glass-border);
        }

        .panel-title {
            font-family: 'Syncopate', sans-serif;
            font-size: 14px;
            color: #fff;
            text-transform: uppercase;
            letter-spacing: 1px;
        }

        .close-panel {
            background: var(--surface-2);
            border: none;
            width: 32px;
            height: 32px;
            border-radius: 50%;
            color: #fff;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
        }

        .panel-content {
            flex: 1;
            overflow-y: auto;
            padding: 20px;
        }

        .panel-content::-webkit-scrollbar {
            width: 4px;
        }
        .panel-content::-webkit-scrollbar-thumb {
            background: var(--surface-2);
            border-radius: 4px;
        }

        /* Stations Grid in Panel */
        .station-grid {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 12px;
        }

        .station-card {
            background: var(--surface-2);
            border: 1px solid var(--glass-border);
            border-radius: var(--radius-md);
            padding: 16px;
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 10px;
            cursor: pointer;
            transition: 0.3s;
            position: relative;
            overflow: hidden;
        }

        .station-card:hover {
            border-color: rgba(255,255,255,0.2);
            transform: translateY(-2px);
        }

        .station-card.active {
            border-color: var(--neon-cyan);
            background: rgba(0, 243, 255, 0.05);
        }

        .station-card.active::before {
            content: '';
            position: absolute;
            inset: 0;
            background: radial-gradient(circle at center, rgba(0, 243, 255, 0.1) 0%, transparent 70%);
            pointer-events: none;
        }

        .station-card .icon {
            font-size: 32px;
            filter: drop-shadow(0 4px 8px rgba(0,0,0,0.5));
        }

        .station-card .freq {
            font-family: 'Syncopate', sans-serif;
            font-size: 12px;
            color: var(--neon-cyan);
            font-weight: 700;
        }

        .station-card .name {
            font-size: 14px;
            font-weight: 500;
            text-align: center;
        }

        /* Lyrics Panel */
        .lyrics-container {
            text-align: center;
            display: flex;
            flex-direction: column;
            gap: 20px;
            padding: 20px 0;
        }

        .lyric-line {
            font-size: 18px;
            color: var(--text-secondary);
            transition: 0.3s;
            filter: blur(1px);
        }

        .lyric-line.active {
            font-size: 24px;
            color: #fff;
            font-weight: 700;
            filter: blur(0);
            text-shadow: 0 0 20px rgba(255,255,255,0.3);
            transform: scale(1.05);
        }

        /* Volume Slider Horizontal */
        .volume-wrapper {
            position: absolute;
            right: 20px;
            top: 50%;
            transform: translateY(-50%);
            height: 100px;
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 10px;
            z-index: 10;
        }

        .vol-slider {
            -webkit-appearance: none;
            width: 80px;
            height: 4px;
            background: var(--surface-2);
            border-radius: 2px;
            transform: rotate(-90deg);
            outline: none;
        }

        .vol-slider::-webkit-slider-thumb {
            -webkit-appearance: none;
            width: 12px;
            height: 12px;
            border-radius: 50%;
            background: #fff;
            box-shadow: 0 0 10px rgba(255,255,255,0.5);
            cursor: pointer;
        }

        .vol-icon {
            margin-top: 40px;
            color: var(--text-secondary);
        }

        /* Responsive adjustments for iframe */
        @media (max-width: 360px) {
            .vinyl-container { width: 200px; height: 200px; }
            .frequency-display { font-size: 26px; }
            .play-btn { width: 60px; height: 60px; }
        }
        @media (max-height: 600px) {
            .hero-section { min-height: 240px; }
            .vinyl-container { width: 180px; height: 180px; }
            .tuner-container { height: 60px; }
            .track-info { margin-top: 10px; }
        }
    </style>
</head>
<body>

    <!-- Ambient WebGL-like Background -->
    <canvas class="ambient-canvas" id="ambientCanvas"></canvas>
    <div class="noise-overlay"></div>

    <div class="app-container" id="app">
        
        <!-- Top Header -->
        <header class="top-bar">
            <div class="brand">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="M12 2a10 10 0 1 0 10 10H12V2z"></path>
                    <path d="M12 12 2.1 7.1"></path>
                    <path d="M12 12l9.9 4.9"></path>
                </svg>
                NEXUS FM
            </div>
            <div class="status-pill" id="statusPill">
                <div class="pulse-dot"></div>
                <span id="statusText">CANLI</span>
            </div>
            <button class="menu-btn" onclick="toggleTheme()">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <circle cx="12" cy="12" r="3"></circle>
                    <path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1 0 2.83 2 2 0 0 1-2.83 0l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-2 2 2 2 0 0 1-2-2v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83 0 2 2 0 0 1 0-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1-2-2 2 2 0 0 1 2-2h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 0-2.83 2 2 0 0 1 2.83 0l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 2-2 2 2 0 0 1 2 2v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 0 2 2 0 0 1 0 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 2 2 2 2 0 0 1-2 2h-.09a1.65 1.65 0 0 0-1.51 1z"></path>
                </svg>
            </button>
        </header>

        <!-- Main Visual Area -->
        <main class="hero-section">
            <canvas class="circular-visualizer" id="circleViz"></canvas>
            <div class="vinyl-container">
                <div class="vinyl-record" id="vinyl">
                    <div class="vinyl-label" id="vinylLabel">
                        🎵
                        <div class="vinyl-hole"></div>
                    </div>
                </div>
            </div>

            <!-- Vertical Volume -->
            <div class="volume-wrapper">
                <input type="range" class="vol-slider" id="volSlider" min="0" max="100" value="80">
                <svg class="vol-icon" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"></polygon>
                    <path d="M19.07 4.93a10 10 0 0 1 0 14.14M15.54 8.46a5 5 0 0 1 0 7.07"></path>
                </svg>
            </div>

            <div class="track-info">
                <div class="frequency-display">
                    <span id="displayFreq">102.5</span>
                    <span class="freq-unit">FM</span>
                </div>
                <div class="station-name" id="displayStation">Cosmic Radio</div>
                <div class="song-title">
                    <div class="eq-mini">
                        <div class="eq-bar"></div><div class="eq-bar"></div><div class="eq-bar"></div><div class="eq-bar"></div><div class="eq-bar"></div>
                    </div>
                    <span id="displaySong">Daft Punk - Interstella 5555</span>
                </div>
            </div>
        </main>

        <!-- Interactive Tuner Ribbon -->
        <div class="tuner-container" id="tunerContainer">
            <div class="tuner-pointer"></div>
            <div class="tuner-ribbon" id="tunerRibbon">
                <!-- Ticks injected by JS -->
            </div>
        </div>

        <!-- Controls -->
        <div class="main-controls">
            <button class="ctrl-btn" id="btnPrev">
                <svg viewBox="0 0 24 24"><path d="M6 6h2v12H6zm3.5 6l8.5 6V6z"/></svg>
            </button>
            <button class="ctrl-btn play-btn" id="btnPlay">
                <svg viewBox="0 0 24 24" id="playIcon">
                    <path d="M8 5v14l11-7z"/>
                </svg>
            </button>
            <button class="ctrl-btn" id="btnNext">
                <svg viewBox="0 0 24 24"><path d="M6 18l8.5-6L6 6v12zM16 6v12h2V6h-2z"/></svg>
            </button>
        </div>

        <!-- Dock Navigation -->
        <nav class="dock">
            <div class="dock-item active" data-target="home">
                <svg viewBox="0 0 24 24"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path><polyline points="9 22 9 12 15 12 15 22"></polyline></svg>
                <span class="dock-label">Oynatıcı</span>
            </div>
            <div class="dock-item" data-target="stationsPanel">
                <svg viewBox="0 0 24 24"><rect x="2" y="2" width="20" height="8" rx="2" ry="2"></rect><rect x="2" y="14" width="20" height="8" rx="2" ry="2"></rect><line x1="6" y1="6" x2="6.01" y2="6"></line><line x1="6" y1="18" x2="6.01" y2="18"></line></svg>
                <span class="dock-label">İstasyonlar</span>
            </div>
            <div class="dock-item" data-target="lyricsPanel">
                <svg viewBox="0 0 24 24"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path></svg>
                <span class="dock-label">Sözler</span>
            </div>
        </nav>

        <!-- PANELS -->
        
        <!-- Stations Panel -->
        <div class="panel" id="stationsPanel">
            <div class="panel-header">
                <div class="panel-title">Tüm İstasyonlar</div>
                <button class="close-panel" onclick="closePanels()">×</button>
            </div>
            <div class="panel-content">
                <div class="station-grid" id="stationGrid">
                    <!-- Injected by JS -->
                </div>
            </div>
        </div>

        <!-- Lyrics Panel -->
        <div class="panel" id="lyricsPanel">
            <div class="panel-header">
                <div class="panel-title">Canlı Sözler</div>
                <button class="close-panel" onclick="closePanels()">×</button>
            </div>
            <div class="panel-content">
                <div class="lyrics-container" id="lyricsContainer">
                    <div class="lyric-line">Uzayın derinliklerinde...</div>
                    <div class="lyric-line">Sinyal aranıyor...</div>
                    <div class="lyric-line active">Kozmik frekans bulundu</div>
                    <div class="lyric-line">Yıldız tozları arasında uçuyoruz</div>
                    <div class="lyric-line">Neon ışıklar yolumuzu aydınlatıyor</div>
                    <div class="lyric-line">Bu frekans hiç bitmesin</div>
                </div>
            </div>
        </div>

    </div>

    <script>
        // --- DATA ---
        const stations = [
            { id: 1, freq: 88.2, name: 'Synthwave FM', icon: '🌃', song: 'Kavinsky - Nightcall', color1: '#ff00ea', color2: '#00f3ff' },
            { id: 2, freq: 92.4, name: 'Cyber Rock', icon: '🎸', song: 'Muse - Supermassive', color1: '#ff3366', color2: '#ff9933' },
            { id: 3, freq: 96.0, name: 'Lo-Fi Chill', icon: '☕', song: 'ChilledCow - 1AM Study', color1: '#a8ff78', color2: '#78ffd6' },
            { id: 4, freq: 100.5, name: 'Deep Space', icon: '🚀', song: 'Hans Zimmer - Time', color1: '#4facfe', color2: '#00f2fe' },
            { id: 5, freq: 102.5, name: 'Cosmic Radio', icon: '🌌', song: 'Daft Punk - Contact', color1: '#b026ff', color2: '#00f3ff' },
            { id: 6, freq: 106.8, name: 'Neon Pop', icon: '✨', song: 'The Weeknd - Blinding Lights', color1: '#f83600', color2: '#f9d423' },
            { id: 7, freq: 108.0, name: 'Classic Static', icon: '📻', song: 'White Noise', color1: '#8e9eab', color2: '#eef2f3' }
        ];

        // --- STATE ---
        let state = {
            isPlaying: false,
            currentFreq: 102.5,
            currentStation: stations[4],
            isDragging: false,
            startX: 0,
            scrollLeft: 0,
            ribbonPos: 0,
            pixelsPerFreq: 10 // 10px per 0.1 MHz
        };

        const minFreq = 87.5;
        const maxFreq = 108.0;

        // --- DOM ELEMENTS ---
        const app = document.getElementById('app');
        const btnPlay = document.getElementById('btnPlay');
        const playIcon = document.getElementById('playIcon');
        const displayFreq = document.getElementById('displayFreq');
        const displayStation = document.getElementById('displayStation');
        const displaySong = document.getElementById('displaySong');
        const vinylLabel = document.getElementById('vinylLabel');
        const tunerRibbon = document.getElementById('tunerRibbon');
        const stationGrid = document.getElementById('stationGrid');

        // --- INIT ---
        function init() {
            buildTuner();
            buildStationGrid();
            updateUI(state.currentStation);
            centerTunerOnFreq(state.currentFreq);
            setupCanvasViz();
            setupAmbientBg();
        }

        // --- TUNER LOGIC ---
        function buildTuner() {
            let html = '';
            for (let f = minFreq; f <= maxFreq; f += 0.1) {
                let freqNum = parseFloat(f.toFixed(1));
                let isMajor = freqNum % 1 === 0 || freqNum % 1 === 0.0;
                html += `
                    <div class="tick-mark ${isMajor ? 'major' : 'minor'}" data-freq="${freqNum}">
                        ${isMajor ? `<div class="tick-label">${Math.floor(freqNum)}</div>` : ''}
                        <div class="tick-line"></div>
                    </div>
                `;
            }
            tunerRibbon.innerHTML = html;
        }

        function centerTunerOnFreq(freq) {
            // Calculate position
            // Total ticks = (max - min) * 10
            // Tick width = 30px
            const totalTicks = (freq - minFreq) * 10;
            const targetX = -(totalTicks * 30);
            state.ribbonPos = targetX;
            tunerRibbon.style.transform = `translateX(${targetX}px)`;
        }

        function getFreqFromPosition(pos) {
            // Pos is negative
            let ticks = Math.abs(pos) / 30;
            let freq = minFreq + (ticks / 10);
            return Math.max(minFreq, Math.min(maxFreq, freq));
        }

        function findNearestStation(freq) {
            return stations.reduce((prev, curr) => 
                Math.abs(curr.freq - freq) < Math.abs(prev.freq - freq) ? curr : prev
            );
        }

        // Drag Logic for Tuner
        tunerRibbon.addEventListener('mousedown', e => {
            state.isDragging = true;
            state.startX = e.pageX - state.ribbonPos;
            tunerRibbon.style.transition = 'none';
        });

        window.addEventListener('mouseup', () => {
            if (!state.isDragging) return;
            state.isDragging = false;
            tunerRibbon.style.transition = 'transform 0.3s cubic-bezier(0.25, 0.46, 0.45, 0.94)';
            
            // Snap to nearest station or tick
            let currentF = getFreqFromPosition(state.ribbonPos);
            let nearest = findNearestStation(currentF);
            
            // If close enough to a station, snap to it
            if (Math.abs(nearest.freq - currentF) < 0.3) {
                changeStation(nearest);
            } else {
                // Just snap to nearest 0.1
                let snapFreq = parseFloat(currentF.toFixed(1));
                centerTunerOnFreq(snapFreq);
                updateStaticUI(snapFreq);
            }
        });

        window.addEventListener('mousemove', e => {
            if (!state.isDragging) return;
            e.preventDefault();
            const x = e.pageX;
            let newPos = x - state.startX;
            
            // Boundaries
            const maxPos = 0;
            const minPos = -(((maxFreq - minFreq) * 10) * 30);
            
            if (newPos > maxPos) newPos = maxPos;
            if (newPos < minPos) newPos = minPos;
            
            state.ribbonPos = newPos;
            tunerRibbon.style.transform = `translateX(${newPos}px)`;
            
            let currentF = getFreqFromPosition(newPos);
            displayFreq.textContent = currentF.toFixed(1);
            
            // Add static effect if playing and not on station
            if(state.isPlaying) {
                 const near = findNearestStation(currentF);
                 if(Math.abs(near.freq - currentF) > 0.1) {
                     document.querySelector('.noise-overlay').style.opacity = 0.15;
                     displayStation.textContent = "Sinyal Aranıyor...";
                 } else {
                     document.querySelector('.noise-overlay').style.opacity = 0.03;
                     displayStation.textContent = near.name;
                 }
            }
        });

        // Touch support for tuner
        tunerRibbon.addEventListener('touchstart', e => {
            state.isDragging = true;
            state.startX = e.touches[0].pageX - state.ribbonPos;
            tunerRibbon.style.transition = 'none';
        });
        window.addEventListener('touchend', () => {
            if (!state.isDragging) return;
            window.dispatchEvent(new Event('mouseup'));
        });
        window.addEventListener('touchmove', e => {
            if (!state.isDragging) return;
            const touch = e.touches[0];
            const mouseEvent = new MouseEvent("mousemove", {
                clientX: touch.clientX,
                clientY: touch.clientY,
                pageX: touch.pageX,
                pageY: touch.pageY
            });
            window.dispatchEvent(mouseEvent);
        }, {passive: false});

        // --- CONTROLS LOGIC ---
        function changeStation(station) {
            state.currentStation = station;
            state.currentFreq = station.freq;
            centerTunerOnFreq(station.freq);
            updateUI(station);
            highlightGrid(station.id);
            document.querySelector('.noise-overlay').style.opacity = 0.03;
            triggerGlitchEffect();
        }

        function updateUI(station) {
            displayFreq.textContent = station.freq.toFixed(1);
            displayStation.textContent = station.name;
            displaySong.textContent = station.song;
            vinylLabel.innerHTML = `${station.icon}<div class="vinyl-hole"></div>`;
            vinylLabel.style.background = `linear-gradient(135deg, ${station.color1}, ${station.color2})`;
            
            // Update app glow colors based on station
            document.documentElement.style.setProperty('--neon-cyan', station.color2);
            document.documentElement.style.setProperty('--neon-magenta', station.color1);
            document.documentElement.style.setProperty('--glow-cyan', `0 0 20px ${station.color2}66`);
        }

        function updateStaticUI(freq) {
            displayStation.textContent = "Statik / Gürültü";
            displaySong.textContent = "Sinyal Yok";
            vinylLabel.innerHTML = `📻<div class="vinyl-hole"></div>`;
            vinylLabel.style.background = `#333`;
        }

        btnPlay.addEventListener('click', () => {
            state.isPlaying = !state.isPlaying;
            if (state.isPlaying) {
                app.classList.add('playing');
                playIcon.innerHTML = `<path d="M6 19h4V5H6v14zm8-14v14h4V5h-4z"/>`;
                document.getElementById('statusText').textContent = "CANLI";
            } else {
                app.classList.remove('playing');
                playIcon.innerHTML = `<path d="M8 5v14l11-7z"/>`;
                document.getElementById('statusText').textContent = "DURAKLATILDI";
            }
        });

        document.getElementById('btnPrev').addEventListener('click', () => {
            let idx = stations.findIndex(s => s.id === state.currentStation.id);
            idx = idx - 1 < 0 ? stations.length - 1 : idx - 1;
            changeStation(stations[idx]);
        });

        document.getElementById('btnNext').addEventListener('click', () => {
            let idx = stations.findIndex(s => s.id === state.currentStation.id);
            idx = (idx + 1) % stations.length;
            changeStation(stations[idx]);
        });

        function triggerGlitchEffect() {
            app.style.transform = `translate(${Math.random()*4-2}px, ${Math.random()*4-2}px)`;
            setTimeout(() => app.style.transform = 'none', 50);
        }

        // --- PANELS & DOCK ---
        const panels = document.querySelectorAll('.panel');
        const dockItems = document.querySelectorAll('.dock-item');

        dockItems.forEach(item => {
            item.addEventListener('click', () => {
                const target = item.dataset.target;
                
                dockItems.forEach(d => d.classList.remove('active'));
                item.classList.add('active');

                if (target === 'home') {
                    closePanels();
                } else {
                    openPanel(target);
                }
            });
        });

        function openPanel(id) {
            panels.forEach(p => p.classList.remove('active'));
            document.getElementById(id).classList.add('active');
        }

        function closePanels() {
            panels.forEach(p => p.classList.remove('active'));
            dockItems.forEach(d => d.classList.remove('active'));
            dockItems[0].classList.add('active'); // Set Home active
        }

        function buildStationGrid() {
            stationGrid.innerHTML = stations.map(s => `
                <div class="station-card ${s.id === state.currentStation.id ? 'active' : ''}" data-id="${s.id}">
                    <div class="icon">${s.icon}</div>
                    <div class="freq">${s.freq.toFixed(1)} FM</div>
                    <div class="name">${s.name}</div>
                </div>
            `).join('');

            document.querySelectorAll('.station-card').forEach(card => {
                card.addEventListener('click', () => {
                    const st = stations.find(s => s.id === parseInt(card.dataset.id));
                    changeStation(st);
                    closePanels();
                });
            });
        }

        function highlightGrid(id) {
            document.querySelectorAll('.station-card').forEach(c => c.classList.remove('active'));
            const activeCard = document.querySelector(`.station-card[data-id="${id}"]`);
            if(activeCard) activeCard.classList.add('active');
        }

        // --- LYRICS ANIMATION ---
        setInterval(() => {
            if(!state.isPlaying) return;
            const lines = document.querySelectorAll('.lyric-line');
            let activeIdx = Array.from(lines).findIndex(l => l.classList.contains('active'));
            lines[activeIdx].classList.remove('active');
            
            activeIdx = (activeIdx + 1) % lines.length;
            lines[activeIdx].classList.add('active');
        }, 3000);

        // --- CANVAS VISUALIZER (CIRCULAR) ---
        const cvCanvas = document.getElementById('circleViz');
        const cvCtx = cvCanvas.getContext('2d');
        
        function setupCanvasViz() {
            const size = 340;
            cvCanvas.width = size;
            cvCanvas.height = size;
            cvCanvas.style.width = size + 'px';
            cvCanvas.style.height = size + 'px';
            requestAnimationFrame(drawCircleViz);
        }

        let angles = Array.from({length: 64}, (_, i) => (Math.PI * 2 * i) / 64);
        let radii = Array(64).fill(130); // Base radius outside vinyl

        function drawCircleViz() {
            cvCtx.clearRect(0, 0, cvCanvas.width, cvCanvas.height);
            const cx = cvCanvas.width / 2;
            const cy = cvCanvas.height / 2;

            cvCtx.beginPath();
            for (let i = 0; i < angles.length; i++) {
                // Animate radius if playing
                let targetR = 135;
                if (state.isPlaying) {
                    targetR = 135 + Math.random() * 30; // Random bump
                }
                
                // Smooth transition
                radii[i] += (targetR - radii[i]) * 0.1;

                let x = cx + Math.cos(angles[i]) * radii[i];
                let y = cy + Math.sin(angles[i]) * radii[i];

                if (i === 0) cvCtx.moveTo(x, y);
                else cvCtx.lineTo(x, y);
            }
            cvCtx.closePath();

            // Glow styling
            cvCtx.lineWidth = 2;
            const gradient = cvCtx.createLinearGradient(0, 0, cvCanvas.width, cvCanvas.height);
            gradient.addColorStop(0, getComputedStyle(document.documentElement).getPropertyValue('--neon-cyan').trim());
            gradient.addColorStop(1, getComputedStyle(document.documentElement).getPropertyValue('--neon-magenta').trim());
            
            cvCtx.strokeStyle = gradient;
            cvCtx.shadowBlur = 15;
            cvCtx.shadowColor = cvCtx.strokeStyle;
            cvCtx.stroke();
            
            // Inner fill transparent
            cvCtx.fillStyle = 'rgba(0,0,0,0)';
            cvCtx.fill();

            requestAnimationFrame(drawCircleViz);
        }

        // --- AMBIENT BACKGROUND CANVAS ---
        const bgCanvas = document.getElementById('ambientCanvas');
        const bgCtx = bgCanvas.getContext('2d');
        let t = 0;

        function setupAmbientBg() {
            resizeBg();
            window.addEventListener('resize', resizeBg);
            requestAnimationFrame(drawAmbientBg);
        }

        function resizeBg() {
            bgCanvas.width = window.innerWidth;
            bgCanvas.height = window.innerHeight;
        }

        function drawAmbientBg() {
            bgCtx.clearRect(0, 0, bgCanvas.width, bgCanvas.height);
            
            let color1 = getComputedStyle(document.documentElement).getPropertyValue('--neon-cyan').trim();
            let color2 = getComputedStyle(document.documentElement).getPropertyValue('--neon-magenta').trim();

            const cx = bgCanvas.width / 2;
            const cy = bgCanvas.height / 2;

            // Draw large slowly moving blobs
            let r1 = 300 + Math.sin(t * 0.01) * 100;
            let x1 = cx + Math.cos(t * 0.005) * 200;
            let y1 = cy + Math.sin(t * 0.007) * 200;

            const grd1 = bgCtx.createRadialGradient(x1, y1, 0, x1, y1, r1);
            grd1.addColorStop(0, color1 + '33'); // 20% opacity
            grd1.addColorStop(1, 'transparent');
            bgCtx.fillStyle = grd1;
            bgCtx.fillRect(0, 0, bgCanvas.width, bgCanvas.height);

            let r2 = 400 + Math.cos(t * 0.012) * 150;
            let x2 = cx + Math.sin(t * 0.004) * 300;
            let y2 = cy + Math.cos(t * 0.006) * 300;

            const grd2 = bgCtx.createRadialGradient(x2, y2, 0, x2, y2, r2);
            grd2.addColorStop(0, color2 + '22');
            grd2.addColorStop(1, 'transparent');
            bgCtx.fillStyle = grd2;
            bgCtx.fillRect(0, 0, bgCanvas.width, bgCanvas.height);

            t++;
            requestAnimationFrame(drawAmbientBg);
        }

        // --- THEME TOGGLE (Easter Egg) ---
        let isLight = false;
        function toggleTheme() {
            isLight = !isLight;
            if(isLight) {
                document.documentElement.style.setProperty('--bg-main', '#f0f0f5');
                document.documentElement.style.setProperty('--surface-1', 'rgba(255, 255, 255, 0.7)');
                document.documentElement.style.setProperty('--surface-2', 'rgba(240, 240, 245, 0.8)');
                document.documentElement.style.setProperty('--text-primary', '#111');
                document.documentElement.style.setProperty('--text-secondary', '#666');
            } else {
                document.documentElement.style.setProperty('--bg-main', '#050507');
                document.documentElement.style.setProperty('--surface-1', 'rgba(20, 20, 25, 0.6)');
                document.documentElement.style.setProperty('--surface-2', 'rgba(35, 35, 45, 0.4)');
                document.documentElement.style.setProperty('--text-primary', '#ffffff');
                document.documentElement.style.setProperty('--text-secondary', '#8b8b9f');
            }
        }

        // Run
        init();

    </script>
</body>
</html>
```