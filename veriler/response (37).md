<think>
Kullanıcı daha modern, daha görsel ve gelişmiş bir radyo player istiyor. "Git git tarzında" ifadesiyle muhtemelen git-github tarzı veya modern gradient/akıcı tasarımları kastediyor. Daha gelişmiş özellikler ve daha modern bir görünüm oluşturacağım.

Yeni özellikler ekleyeceğim:
1. Daha modern glassmorphism tasarımı
2. Animasyonlu gradientler
3. Daha gelişmiş visualizer (dalgalar, parçacıklar)
4. Spotify benzeri modern UI elementleri
5. Daha fazla etkileşimli element
6. 3D efektleri
7. Daha akıcı animasyonlar
8. Modern kart tasarımları
9. Gelişmiş ses efektleri görselleştirmesi
10. Dinamik renk geçişleri

Tasarım özellikleri:
- Neumorphism ve glassmorphism karışımı
- Daha canlı renkler
- Smooth animasyonlar
- Daha gelişmiş waveform
- Album art için dönen disk efekti
- Spotify tarzı progress bar
- Modern tipografi
- Hover efektleri
- Particle effects
</think>```html
<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>NeoRadio Pro</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=Space+Grotesk:wght@400;500;600;700&display=swap" rel="stylesheet">
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        :root {
            --primary: #6366f1;
            --primary-glow: rgba(99, 102, 241, 0.5);
            --secondary: #ec4899;
            --tertiary: #06b6d4;
            --accent: #f59e0b;
            --bg-deep: #030014;
            --bg-main: #0f0f1a;
            --bg-card: rgba(15, 15, 30, 0.8);
            --glass: rgba(255, 255, 255, 0.03);
            --glass-border: rgba(255, 255, 255, 0.06);
            --text-bright: #ffffff;
            --text-dim: #a1a1aa;
            --gradient-main: linear-gradient(135deg, #6366f1 0%, #ec4899 50%, #06b6d4 100%);
            --gradient-glow: linear-gradient(135deg, rgba(99, 102, 241, 0.3), rgba(236, 72, 153, 0.3));
        }

        body {
            font-family: 'Inter', sans-serif;
            background: var(--bg-deep);
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 20px;
            overflow-x: hidden;
            position: relative;
        }

        /* Ambient Background */
        .ambient-bg {
            position: fixed;
            inset: 0;
            overflow: hidden;
            z-index: 0;
        }

        .ambient-orb {
            position: absolute;
            border-radius: 50%;
            filter: blur(120px);
            animation: orbFloat 25s ease-in-out infinite;
        }

        .orb-1 {
            width: 600px;
            height: 600px;
            background: radial-gradient(circle, rgba(99, 102, 241, 0.4) 0%, transparent 70%);
            top: -200px;
            left: -200px;
        }

        .orb-2 {
            width: 500px;
            height: 500px;
            background: radial-gradient(circle, rgba(236, 72, 153, 0.3) 0%, transparent 70%);
            bottom: -150px;
            right: -150px;
            animation-delay: -8s;
        }

        .orb-3 {
            width: 400px;
            height: 400px;
            background: radial-gradient(circle, rgba(6, 182, 212, 0.25) 0%, transparent 70%);
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            animation-delay: -15s;
        }

        @keyframes orbFloat {
            0%, 100% { transform: translate(0, 0) scale(1); }
            25% { transform: translate(80px, -50px) scale(1.1); }
            50% { transform: translate(-40px, 80px) scale(0.95); }
            75% { transform: translate(60px, 40px) scale(1.05); }
        }

        /* Grid Pattern */
        .grid-overlay {
            position: fixed;
            inset: 0;
            background-image: 
                linear-gradient(rgba(255,255,255,0.02) 1px, transparent 1px),
                linear-gradient(90deg, rgba(255,255,255,0.02) 1px, transparent 1px);
            background-size: 60px 60px;
            z-index: 1;
            pointer-events: none;
        }

        /* Main Container */
        .player-container {
            position: relative;
            z-index: 10;
            width: 100%;
            max-width: 480px;
            perspective: 1000px;
        }

        .player-card {
            background: var(--bg-card);
            backdrop-filter: blur(40px);
            border-radius: 32px;
            border: 1px solid var(--glass-border);
            overflow: hidden;
            position: relative;
            box-shadow: 
                0 0 0 1px rgba(255, 255, 255, 0.05) inset,
                0 40px 80px -20px rgba(0, 0, 0, 0.8),
                0 0 100px -50px var(--primary-glow);
            transform-style: preserve-3d;
            transition: transform 0.3s ease;
        }

        .player-card:hover {
            transform: rotateX(2deg) rotateY(-2deg);
        }

        /* Glow Effect */
        .dynamic-glow {
            position: absolute;
            top: -50%;
            left: -50%;
            width: 200%;
            height: 200%;
            background: conic-gradient(
                from 0deg at 50% 50%,
                transparent 0deg,
                rgba(99, 102, 241, 0.1) 60deg,
                rgba(236, 72, 153, 0.1) 120deg,
                transparent 180deg,
                rgba(6, 182, 212, 0.1) 240deg,
                transparent 300deg,
                rgba(99, 102, 241, 0.1) 360deg
            );
            animation: glowRotate 15s linear infinite;
            pointer-events: none;
            opacity: 0;
            transition: opacity 0.5s;
        }

        .player-card.playing .dynamic-glow {
            opacity: 1;
        }

        @keyframes glowRotate {
            from { transform: rotate(0deg); }
            to { transform: rotate(360deg); }
        }

        /* Top Bar */
        .top-bar {
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 20px 24px;
            position: relative;
            z-index: 10;
        }

        .brand {
            display: flex;
            align-items: center;
            gap: 12px;
        }

        .brand-icon {
            width: 48px;
            height: 48px;
            background: var(--gradient-main);
            border-radius: 14px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 24px;
            position: relative;
            overflow: hidden;
        }

        .brand-icon::before {
            content: '';
            position: absolute;
            inset: 0;
            background: linear-gradient(135deg, rgba(255,255,255,0.4) 0%, transparent 50%);
        }

        .brand-text {
            font-family: 'Space Grotesk', sans-serif;
            font-size: 22px;
            font-weight: 700;
            background: linear-gradient(135deg, #fff 0%, #a1a1aa 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }

        .top-actions {
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .live-badge {
            display: flex;
            align-items: center;
            gap: 6px;
            padding: 8px 14px;
            background: rgba(34, 197, 94, 0.15);
            border: 1px solid rgba(34, 197, 94, 0.3);
            border-radius: 24px;
            font-size: 11px;
            font-weight: 600;
            color: #22c55e;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }

        .live-pulse {
            width: 8px;
            height: 8px;
            background: #22c55e;
            border-radius: 50%;
            position: relative;
        }

        .live-pulse::after {
            content: '';
            position: absolute;
            inset: -3px;
            border: 2px solid #22c55e;
            border-radius: 50%;
            animation: pulseRing 1.5s ease-out infinite;
        }

        @keyframes pulseRing {
            0% { transform: scale(1); opacity: 1; }
            100% { transform: scale(2); opacity: 0; }
        }

        .icon-button {
            width: 44px;
            height: 44px;
            background: var(--glass);
            border: 1px solid var(--glass-border);
            border-radius: 14px;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            transition: all 0.25s ease;
            position: relative;
            overflow: hidden;
        }

        .icon-button::before {
            content: '';
            position: absolute;
            inset: 0;
            background: linear-gradient(135deg, rgba(255,255,255,0.1) 0%, transparent 50%);
            opacity: 0;
            transition: opacity 0.25s;
        }

        .icon-button:hover {
            background: rgba(255, 255, 255, 0.08);
            transform: translateY(-2px);
        }

        .icon-button:hover::before {
            opacity: 1;
        }

        .icon-button svg {
            width: 20px;
            height: 20px;
            stroke: var(--text-dim);
            stroke-width: 2;
            fill: none;
            transition: all 0.25s;
        }

        .icon-button:hover svg {
            stroke: var(--text-bright);
        }

        .icon-button.active {
            background: var(--gradient-main);
            border-color: transparent;
        }

        .icon-button.active svg {
            stroke: white;
        }

        /* Visualizer Section */
        .visualizer-section {
            padding: 0 24px;
            position: relative;
        }

        .visualizer-container {
            background: rgba(0, 0, 0, 0.5);
            border-radius: 24px;
            padding: 24px;
            position: relative;
            overflow: hidden;
            border: 1px solid var(--glass-border);
        }

        .visualizer-container::before {
            content: '';
            position: absolute;
            inset: 0;
            background: linear-gradient(180deg, transparent 0%, rgba(99, 102, 241, 0.05) 100%);
        }

        #visualizerCanvas {
            width: 100%;
            height: 160px;
            display: block;
            position: relative;
            z-index: 2;
        }

        .freq-display {
            position: absolute;
            top: 20px;
            right: 20px;
            text-align: right;
            z-index: 5;
        }

        .freq-number {
            font-family: 'Space Grotesk', sans-serif;
            font-size: 36px;
            font-weight: 700;
            color: white;
            line-height: 1;
            text-shadow: 0 0 30px var(--primary-glow);
        }

        .freq-unit {
            font-size: 14px;
            color: var(--text-dim);
            font-weight: 500;
        }

        .signal-bars {
            position: absolute;
            top: 24px;
            left: 24px;
            display: flex;
            align-items: flex-end;
            gap: 4px;
            height: 28px;
            z-index: 5;
        }

        .sig-bar {
            width: 5px;
            background: rgba(255, 255, 255, 0.2);
            border-radius: 3px;
            transition: all 0.3s;
        }

        .sig-bar.active {
            background: linear-gradient(to top, #22c55e, #4ade80);
            box-shadow: 0 0 10px rgba(34, 197, 94, 0.5);
        }

        /* Album Section */
        .album-section {
            padding: 28px 24px;
            text-align: center;
            position: relative;
        }

        .album-wrapper {
            position: relative;
            width: 160px;
            height: 160px;
            margin: 0 auto 24px;
        }

        .album-glow {
            position: absolute;
            inset: -20px;
            background: var(--gradient-main);
            border-radius: 50%;
            filter: blur(40px);
            opacity: 0.4;
            animation: albumGlow 4s ease-in-out infinite;
        }

        @keyframes albumGlow {
            0%, 100% { transform: scale(1); opacity: 0.4; }
            50% { transform: scale(1.1); opacity: 0.6; }
        }

        .album-disc {
            position: relative;
            width: 160px;
            height: 160px;
            border-radius: 50%;
            background: 
                radial-gradient(circle at 30% 30%, rgba(255,255,255,0.2) 0%, transparent 50%),
                var(--gradient-main);
            display: flex;
            align-items: center;
            justify-content: center;
            box-shadow: 
                0 20px 40px rgba(99, 102, 241, 0.3),
                inset 0 0 0 4px rgba(255, 255, 255, 0.1);
            transition: transform 0.3s;
        }

        .player-card.playing .album-disc {
            animation: discSpin 8s linear infinite;
        }

        @keyframes discSpin {
            from { transform: rotate(0deg); }
            to { transform: rotate(360deg); }
        }

        .album-center {
            width: 60px;
            height: 60px;
            background: var(--bg-deep);
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 28px;
            box-shadow: inset 0 0 20px rgba(0, 0, 0, 0.5);
        }

        .album-ring {
            position: absolute;
            inset: 8px;
            border: 2px dashed rgba(255, 255, 255, 0.15);
            border-radius: 50%;
        }

        .now-playing-label {
            display: inline-flex;
            align-items: center;
            gap: 8px;
            padding: 6px 14px;
            background: var(--gradient-main);
            border-radius: 20px;
            font-size: 10px;
            font-weight: 700;
            color: white;
            text-transform: uppercase;
            letter-spacing: 1.5px;
            margin-bottom: 16px;
        }

        .track-name {
            font-size: 24px;
            font-weight: 700;
            color: var(--text-bright);
            margin-bottom: 6px;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
        }

        .artist-name {
            font-size: 15px;
            color: var(--text-dim);
            font-weight: 500;
        }

        /* Progress Section */
        .progress-section {
            padding: 0 24px 24px;
        }

        .waveform-container {
            position: relative;
            height: 48px;
            background: rgba(0, 0, 0, 0.4);
            border-radius: 16px;
            overflow: hidden;
            cursor: pointer;
            border: 1px solid var(--glass-border);
        }

        #waveformCanvas {
            width: 100%;
            height: 100%;
        }

        .wave-progress {
            position: absolute;
            top: 0;
            left: 0;
            height: 100%;
            background: linear-gradient(90deg, rgba(99, 102, 241, 0.4), rgba(236, 72, 153, 0.4));
            pointer-events: none;
            border-radius: 16px;
        }

        .wave-cursor {
            position: absolute;
            top: 0;
            width: 3px;
            height: 100%;
            background: white;
            border-radius: 2px;
            box-shadow: 0 0 10px white;
            pointer-events: none;
        }

        .time-display {
            display: flex;
            justify-content: space-between;
            margin-top: 12px;
            font-family: 'Space Grotesk', sans-serif;
            font-size: 12px;
            color: var(--text-dim);
        }

        .live-indicator {
            display: flex;
            align-items: center;
            gap: 6px;
            color: #22c55e;
        }

        .live-dot {
            width: 6px;
            height: 6px;
            background: #22c55e;
            border-radius: 50%;
            animation: blink 1s infinite;
        }

        @keyframes blink {
            0%, 100% { opacity: 1; }
            50% { opacity: 0.4; }
        }

        /* Main Controls */
        .controls-section {
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 16px;
            padding: 0 24px 24px;
        }

        .ctrl-btn {
            width: 52px;
            height: 52px;
            border-radius: 50%;
            background: var(--glass);
            border: 1px solid var(--glass-border);
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1);
            position: relative;
            overflow: hidden;
        }

        .ctrl-btn::before {
            content: '';
            position: absolute;
            inset: 0;
            background: linear-gradient(135deg, rgba(255,255,255,0.1) 0%, transparent 50%);
            opacity: 0;
            transition: opacity 0.25s;
        }

        .ctrl-btn:hover {
            background: rgba(255, 255, 255, 0.1);
            transform: scale(1.08);
        }

        .ctrl-btn:hover::before {
            opacity: 1;
        }

        .ctrl-btn:active {
            transform: scale(0.95);
        }

        .ctrl-btn svg {
            width: 22px;
            height: 22px;
            stroke: var(--text-bright);
            fill: none;
            stroke-width: 2;
            transition: all 0.25s;
        }

        .ctrl-btn.active {
            background: var(--gradient-main);
            border-color: transparent;
            box-shadow: 0 8px 30px rgba(99, 102, 241, 0.4);
        }

        .play-btn {
            width: 80px;
            height: 80px;
            background: var(--gradient-main);
            border: none;
            box-shadow: 
                0 15px 40px rgba(99, 102, 241, 0.5),
                0 0 0 8px rgba(99, 102, 241, 0.1);
            position: relative;
        }

        .play-btn::before {
            content: '';
            position: absolute;
            inset: -4px;
            border-radius: 50%;
            background: var(--gradient-main);
            filter: blur(15px);
            opacity: 0.5;
            z-index: -1;
        }

        .play-btn:hover {
            transform: scale(1.12);
            box-shadow: 
                0 20px 50px rgba(99, 102, 241, 0.6),
                0 0 0 12px rgba(99, 102, 241, 0.15);
        }

        .play-btn svg {
            width: 32px;
            height: 32px;
            fill: white;
            stroke: white;
        }

        /* Volume Section */
        .volume-section {
            display: flex;
            align-items: center;
            gap: 16px;
            padding: 0 24px 24px;
        }

        .vol-icon-wrap {
            width: 44px;
            height: 44px;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            border-radius: 12px;
            transition: background 0.25s;
        }

        .vol-icon-wrap:hover {
            background: var(--glass);
        }

        .vol-icon-wrap svg {
            width: 24px;
            height: 24px;
            stroke: var(--text-dim);
            fill: none;
            stroke-width: 2;
            transition: stroke 0.25s;
        }

        .vol-icon-wrap:hover svg {
            stroke: var(--text-bright);
        }

        .volume-slider-wrap {
            flex: 1;
            height: 10px;
            background: rgba(255, 255, 255, 0.08);
            border-radius: 5px;
            position: relative;
            cursor: pointer;
            overflow: hidden;
        }

        .volume-fill {
            height: 100%;
            background: var(--gradient-main);
            border-radius: 5px;
            position: relative;
            transition: width 0.1s;
        }

        .volume-fill::after {
            content: '';
            position: absolute;
            right: 0;
            top: 50%;
            transform: translateY(-50%);
            width: 18px;
            height: 18px;
            background: white;
            border-radius: 50%;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.3);
        }

        .vol-percent {
            font-family: 'Space Grotesk', sans-serif;
            font-size: 13px;
            color: var(--text-dim);
            min-width: 42px;
            text-align: right;
        }

        /* Tabs Section */
        .tabs-section {
            border-top: 1px solid var(--glass-border);
        }

        .tabs-header {
            display: flex;
            padding: 0 16px;
            border-bottom: 1px solid var(--glass-border);
            overflow-x: auto;
        }

        .tab-trigger {
            flex: 1;
            min-width: 80px;
            padding: 16px 8px;
            background: none;
            border: none;
            color: var(--text-dim);
            font-size: 13px;
            font-weight: 600;
            cursor: pointer;
            position: relative;
            transition: color 0.25s;
            white-space: nowrap;
        }

        .tab-trigger:hover {
            color: var(--text-bright);
        }

        .tab-trigger.active {
            color: var(--text-bright);
        }

        .tab-trigger::after {
            content: '';
            position: absolute;
            bottom: -1px;
            left: 50%;
            transform: translateX(-50%);
            width: 0;
            height: 3px;
            background: var(--gradient-main);
            border-radius: 3px 3px 0 0;
            transition: width 0.25s;
        }

        .tab-trigger.active::after {
            width: 60%;
        }

        .tab-panel {
            display: none;
            padding: 20px 24px;
            max-height: 240px;
            overflow-y: auto;
        }

        .tab-panel.active {
            display: block;
        }

        .tab-panel::-webkit-scrollbar {
            width: 5px;
        }

        .tab-panel::-webkit-scrollbar-track {
            background: transparent;
        }

        .tab-panel::-webkit-scrollbar-thumb {
            background: rgba(255, 255, 255, 0.1);
            border-radius: 3px;
        }

        /* Stations Grid */
        .stations-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 12px;
        }

        .station-card {
            background: var(--glass);
            border: 1px solid var(--glass-border);
            border-radius: 18px;
            padding: 16px 12px;
            text-align: center;
            cursor: pointer;
            transition: all 0.3s ease;
            position: relative;
            overflow: hidden;
        }

        .station-card::before {
            content: '';
            position: absolute;
            inset: 0;
            background: var(--gradient-main);
            opacity: 0;
            transition: opacity 0.3s;
        }

        .station-card:hover {
            transform: translateY(-4px);
            border-color: rgba(99, 102, 241, 0.3);
        }

        .station-card:hover::before {
            opacity: 0.1;
        }

        .station-card.active {
            border-color: var(--primary);
            background: linear-gradient(135deg, rgba(99, 102, 241, 0.15), rgba(236, 72, 153, 0.15));
        }

        .station-emoji {
            font-size: 32px;
            margin-bottom: 10px;
            display: block;
            position: relative;
            z-index: 1;
        }

        .station-name {
            font-size: 12px;
            font-weight: 600;
            color: var(--text-bright);
            position: relative;
            z-index: 1;
        }

        .station-freq {
            font-family: 'Space Grotesk', sans-serif;
            font-size: 11px;
            color: var(--text-dim);
            margin-top: 4px;
            position: relative;
            z-index: 1;
        }

        /* Equalizer */
        .eq-presets-wrap {
            display: flex;
            flex-wrap: wrap;
            gap: 8px;
            margin-bottom: 20px;
        }

        .eq-preset {
            padding: 10px 16px;
            background: var(--glass);
            border: 1px solid var(--glass-border);
            border-radius: 24px;
            font-size: 12px;
            font-weight: 600;
            color: var(--text-dim);
            cursor: pointer;
            transition: all 0.25s;
        }

        .eq-preset:hover {
            color: var(--text-bright);
            background: rgba(255, 255, 255, 0.08);
        }

        .eq-preset.active {
            background: var(--gradient-main);
            border-color: transparent;
            color: white;
        }

        .eq-bands {
            display: flex;
            justify-content: space-between;
            gap: 14px;
        }

        .eq-band {
            flex: 1;
            display: flex;
            flex-direction: column;
            align-items: center;
        }

        .eq-track {
            width: 100%;
            height: 100px;
            background: rgba(0, 0, 0, 0.4);
            border-radius: 10px;
            position: relative;
            cursor: pointer;
            overflow: hidden;
        }

        .eq-fill {
            position: absolute;
            bottom: 0;
            width: 100%;
            background: linear-gradient(to top, var(--primary), var(--secondary));
            border-radius: 10px;
            transition: height 0.15s;
        }

        .eq-label {
            font-size: 10px;
            color: var(--text-dim);
            margin-top: 8px;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }

        .eq-val {
            font-family: 'Space Grotesk', sans-serif;
            font-size: 11px;
            color: var(--primary);
            margin-top: 2px;
        }

        /* Effects Grid */
        .effects-grid {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 12px;
        }

        .effect-item {
            background: var(--glass);
            border: 1px solid var(--glass-border);
            border-radius: 18px;
            padding: 16px;
            display: flex;
            align-items: center;
            gap: 14px;
            cursor: pointer;
            transition: all 0.3s;
        }

        .effect-item:hover {
            background: rgba(255, 255, 255, 0.06);
            transform: translateY(-2px);
        }

        .effect-item.active {
            background: linear-gradient(135deg, rgba(99, 102, 241, 0.15), rgba(236, 72, 153, 0.15));
            border-color: var(--primary);
        }

        .effect-icon {
            width: 44px;
            height: 44px;
            background: var(--gradient-main);
            border-radius: 12px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 20px;
        }

        .effect-text h4 {
            font-size: 14px;
            font-weight: 600;
            color: var(--text-bright);
        }

        .effect-text p {
            font-size: 11px;
            color: var(--text-dim);
            margin-top: 2px;
        }

        /* Settings */
        .settings-list {
            display: flex;
            flex-direction: column;
            gap: 12px;
        }

        .setting-item {
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 14px 16px;
            background: var(--glass);
            border: 1px solid var(--glass-border);
            border-radius: 16px;
        }

        .setting-label {
            display: flex;
            align-items: center;
            gap: 12px;
            color: var(--text-bright);
            font-size: 14px;
            font-weight: 500;
        }

        .setting-label span {
            font-size: 20px;
        }

        .toggle {
            width: 50px;
            height: 28px;
            background: rgba(255, 255, 255, 0.1);
            border-radius: 14px;
            position: relative;
            cursor: pointer;
            transition: all 0.3s;
        }

        .toggle.active {
            background: var(--gradient-main);
        }

        .toggle::after {
            content: '';
            position: absolute;
            top: 3px;
            left: 3px;
            width: 22px;
            height: 22px;
            background: white;
            border-radius: 50%;
            transition: transform 0.3s;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.2);
        }

        .toggle.active::after {
            transform: translateX(22px);
        }

        /* Footer */
        .footer-section {
            padding: 16px 24px;
            background: rgba(0, 0, 0, 0.3);
            border-top: 1px solid var(--glass-border);
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .listeners-info {
            display: flex;
            align-items: center;
            gap: 10px;
            font-size: 13px;
            color: var(--text-dim);
        }

        .avatar-stack {
            display: flex;
        }

        .avatar-item {
            width: 28px;
            height: 28px;
            border-radius: 50%;
            background: var(--gradient-main);
            border: 2px solid var(--bg-card);
            margin-left: -8px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 12px;
        }

        .avatar-item:first-child {
            margin-left: 0;
        }

        .listener-count {
            font-weight: 700;
            color: var(--text-bright);
        }

        .action-buttons {
            display: flex;
            gap: 10px;
        }

        .action-btn {
            padding: 10px 16px;
            background: var(--glass);
            border: 1px solid var(--glass-border);
            border-radius: 24px;
            font-size: 12px;
            font-weight: 600;
            color: var(--text-dim);
            cursor: pointer;
            display: flex;
            align-items: center;
            gap: 6px;
            transition: all 0.25s;
        }

        .action-btn:hover {
            background: rgba(99, 102, 241, 0.2);
            border-color: var(--primary);
            color: var(--text-bright);
        }

        .action-btn.recording {
            background: rgba(239, 68, 68, 0.2);
            border-color: rgba(239, 68, 68, 0.5);
            color: #ef4444;
        }

        /* Recording Badge */
        .rec-badge {
            position: absolute;
            top: 80px;
            left: 50%;
            transform: translateX(-50%);
            display: flex;
            align-items: center;
            gap: 8px;
            padding: 8px 16px;
            background: rgba(239, 68, 68, 0.2);
            border: 1px solid rgba(239, 68, 68, 0.4);
            border-radius: 24px;
            z-index: 20;
            opacity: 0;
            transition: opacity 0.3s;
        }

        .rec-badge.active {
            opacity: 1;
        }

        .rec-dot {
            width: 10px;
            height: 10px;
            background: #ef4444;
            border-radius: 50%;
            animation: recPulse 1s infinite;
        }

        @keyframes recPulse {
            0%, 100% { opacity: 1; transform: scale(1); }
            50% { opacity: 0.5; transform: scale(0.8); }
        }

        .rec-badge span {
            font-size: 12px;
            font-weight: 600;
            color: #ef4444;
            text-transform: uppercase;
            letter-spacing: 1px;
        }

        /* Sleep Timer Badge */
        .sleep-badge {
            position: absolute;
            top: 80px;
            right: 24px;
            display: flex;
            align-items: center;
            gap: 6px;
            padding: 8px 14px;
            background: rgba(99, 102, 241, 0.2);
            border: 1px solid rgba(99, 102, 241, 0.4);
            border-radius: 24px;
            z-index: 20;
            opacity: 0;
            transition: opacity 0.3s;
        }

        .sleep-badge.active {
            opacity: 1;
        }

        .sleep-badge span {
            font-family: 'Space Grotesk', sans-serif;
            font-size: 13px;
            font-weight: 600;
            color: var(--primary);
        }

        /* Modal */
        .modal-backdrop {
            position: fixed;
            inset: 0;
            background: rgba(0, 0, 0, 0.8);
            backdrop-filter: blur(10px);
            display: flex;
            align-items: center;
            justify-content: center;
            z-index: 1000;
            opacity: 0;
            visibility: hidden;
            transition: all 0.3s;
        }

        .modal-backdrop.active {
            opacity: 1;
            visibility: visible;
        }

        .modal-box {
            background: var(--bg-card);
            border: 1px solid var(--glass-border);
            border-radius: 28px;
            padding: 28px;
            max-width: 380px;
            width: 90%;
            transform: scale(0.9) translateY(20px);
            transition: transform 0.3s;
        }

        .modal-backdrop.active .modal-box {
            transform: scale(1) translateY(0);
        }

        .modal-head {
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-bottom: 24px;
        }

        .modal-title {
            font-size: 20px;
            font-weight: 700;
            color: var(--text-bright);
        }

        .modal-close {
            width: 36px;
            height: 36px;
            background: var(--glass);
            border: none;
            border-radius: 10px;
            color: var(--text-dim);
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 24px;
            transition: all 0.25s;
        }

        .modal-close:hover {
            background: rgba(255, 255, 255, 0.1);
            color: var(--text-bright);
        }

        .sleep-options-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 12px;
        }

        .sleep-opt {
            padding: 20px 12px;
            background: var(--glass);
            border: 1px solid var(--glass-border);
            border-radius: 16px;
            text-align: center;
            cursor: pointer;
            transition: all 0.25s;
        }

        .sleep-opt:hover {
            background: rgba(99, 102, 241, 0.2);
            border-color: var(--primary);
        }

        .sleep-opt .time-val {
            font-family: 'Space Grotesk', sans-serif;
            font-size: 24px;
            font-weight: 700;
            color: var(--text-bright);
        }

        .sleep-opt .time-unit {
            font-size: 12px;
            color: var(--text-dim);
            margin-top: 4px;
        }

        /* Responsive */
        @media (max-width: 420px) {
            .player-card {
                border-radius: 28px;
            }

            .album-wrapper {
                width: 140px;
                height: 140px;
            }

            .album-disc {
                width: 140px;
                height: 140px;
            }

            .track-name {
                font-size: 20px;
            }

            .stations-grid {
                gap: 8px;
            }

            .station-card {
                padding: 12px 8px;
            }

            .station-emoji {
                font-size: 26px;
            }

            .play-btn {
                width: 70px;
                height: 70px;
            }

            .ctrl-btn {
                width: 46px;
                height: 46px;
            }
        }
    </style>
</head>
<body>
    <!-- Ambient Background -->
    <div class="ambient-bg">
        <div class="ambient-orb orb-1"></div>
        <div class="ambient-orb orb-2"></div>
        <div class="ambient-orb orb-3"></div>
    </div>
    <div class="grid-overlay"></div>

    <!-- Sleep Modal -->
    <div class="modal-backdrop" id="sleepModal">
        <div class="modal-box">
            <div class="modal-head">
                <h3 class="modal-title">Uyku Zamanlayıcısı</h3>
                <button class="modal-close" onclick="closeSleepModal()">×</button>
            </div>
            <div class="sleep-options-grid" id="sleepOptions"></div>
        </div>
    </div>

    <!-- Main Player -->
    <div class="player-container">
        <div class="player-card playing" id="playerCard">
            <div class="dynamic-glow"></div>
            
            <!-- Recording Badge -->
            <div class="rec-badge" id="recBadge">
                <div class="rec-dot"></div>
                <span>KAYIT</span>
            </div>
            
            <!-- Sleep Badge -->
            <div class="sleep-badge" id="sleepBadge">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <circle cx="12" cy="12" r="10"></circle>
                    <polyline points="12 6 12 12 16 14"></polyline>
                </svg>
                <span id="sleepTime">--:--</span>
            </div>

            <!-- Top Bar -->
            <div class="top-bar">
                <div class="brand">
                    <div class="brand-icon">📻</div>
                    <span class="brand-text">NeoRadio</span>
                </div>
                <div class="top-actions">
                    <div class="live-badge">
                        <div class="live-pulse"></div>
                        CANLI
                    </div>
                    <button class="icon-button" id="themeBtn" title="Tema">
                        <svg viewBox="0 0 24 24">
                            <circle cx="12" cy="12" r="5"></circle>
                            <line x1="12" y1="1" x2="12" y2="3"></line>
                            <line x1="12" y1="21" x2="12" y2="23"></line>
                            <line x1="4.22" y1="4.22" x2="5.64" y2="5.64"></line>
                            <line x1="18.36" y1="18.36" x2="19.78" y2="19.78"></line>
                            <line x1="1" y1="12" x2="3" y2="12"></line>
                            <line x1="21" y1="12" x2="23" y2="12"></line>
                            <line x1="4.22" y1="19.78" x2="5.64" y2="18.36"></line>
                            <line x1="18.36" y1="5.64" x2="19.78" y2="4.22"></line>
                        </svg>
                    </button>
                    <button class="icon-button" id="powerBtn" title="Kapat">
                        <svg viewBox="0 0 24 24">
                            <path d="M18.36 6.64a9 9 0 1 1-12.73 0"></path>
                            <line x1="12" y1="2" x2="12" y2="12"></line>
                        </svg>
                    </button>
                </div>
            </div>

            <!-- Visualizer -->
            <div class="visualizer-section">
                <div class="visualizer-container">
                    <div class="signal-bars" id="signalBars"></div>
                    <div class="freq-display">
                        <div class="freq-number" id="freqNum">101.5</div>
                        <div class="freq-unit">MHz</div>
                    </div>
                    <canvas id="visualizerCanvas"></canvas>
                </div>
            </div>

            <!-- Album Section -->
            <div class="album-section">
                <div class="album-wrapper">
                    <div class="album-glow"></div>
                    <div class="album-disc" id="albumDisc">
                        <div class="album-center" id="albumEmoji">🎵</div>
                        <div class="album-ring"></div>
                    </div>
                </div>
                <div class="now-playing-label">ŞU AN ÇALIYOR</div>
                <div class="track-name" id="trackName">Gece Yolculuğu</div>
                <div class="artist-name" id="artistName">Power Türk FM</div>
            </div>

            <!-- Progress -->
            <div class="progress-section">
                <div class="waveform-container" id="waveformContainer">
                    <div class="wave-progress" id="waveProgress"></div>
                    <div class="wave-cursor" id="waveCursor"></div>
                    <canvas id="waveformCanvas"></canvas>
                </div>
                <div class="time-display">
                    <span id="currentTime">02:45</span>
                    <div class="live-indicator">
                        <div class="live-dot"></div>
                        CANLI YAYIN
                    </div>
                </div>
            </div>

            <!-- Controls -->
            <div class="controls-section">
                <button class="ctrl-btn" id="shuffleBtn" title="Karıştır">
                    <svg viewBox="0 0 24 24">
                        <polyline points="16 3 21 3 21 8"></polyline>
                        <line x1="4" y1="20" x2="21" y2="3"></line>
                        <polyline points="21 16 21 21 16 21"></polyline>
                        <line x1="15" y1="15" x2="21" y2="21"></line>
                        <line x1="4" y1="4" x2="9" y2="9"></line>
                    </svg>
                </button>
                <button class="ctrl-btn" id="prevBtn" title="Önceki">
                    <svg viewBox="0 0 24 24">
                        <polygon points="19 20 9 12 19 4 19 20"></polygon>
                        <line x1="5" y1="19" x2="5" y2="5"></line>
                    </svg>
                </button>
                <button class="ctrl-btn play-btn" id="playBtn">
                    <svg viewBox="0 0 24 24" id="playIcon">
                        <rect x="6" y="4" width="4" height="16" rx="1" fill="white" stroke="none"></rect>
                        <rect x="14" y="4" width="4" height="16" rx="1" fill="white" stroke="none"></rect>
                    </svg>
                </button>
                <button class="ctrl-btn" id="nextBtn" title="Sonraki">
                    <svg viewBox="0 0 24 24">
                        <polygon points="5 4 15 12 5 20 5 4"></polygon>
                        <line x1="19" y1="5" x2="19" y2="19"></line>
                    </svg>
                </button>
                <button class="ctrl-btn" id="repeatBtn" title="Tekrarla">
                    <svg viewBox="0 0 24 24">
                        <polyline points="17 1 21 5 17 9"></polyline>
                        <path d="M3 11V9a4 4 0 0 1 4-4h14"></path>
                        <polyline points="7 23 3 19 7 15"></polyline>
                        <path d="M21 13v2a4 4 0 0 1-4 4H3"></path>
                    </svg>
                </button>
            </div>

            <!-- Volume -->
            <div class="volume-section">
                <div class="vol-icon-wrap" id="volIcon">
                    <svg viewBox="0 0 24 24">
                        <polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"></polygon>
                        <path d="M19.07 4.93a10 10 0 0 1 0 14.14M15.54 8.46a5 5 0 0 1 0 7.07"></path>
                    </svg>
                </div>
                <div class="volume-slider-wrap" id="volumeSlider">
                    <div class="volume-fill" id="volumeFill" style="width: 75%;"></div>
                </div>
                <span class="vol-percent" id="volPercent">75%</span>
            </div>

            <!-- Tabs -->
            <div class="tabs-section">
                <div class="tabs-header">
                    <button class="tab-trigger active" data-tab="stations">İstasyonlar</button>
                    <button class="tab-trigger" data-tab="equalizer">Ekolayzer</button>
                    <button class="tab-trigger" data-tab="effects">Efektler</button>
                    <button class="tab-trigger" data-tab="settings">Ayarlar</button>
                </div>

                <!-- Stations -->
                <div class="tab-panel active" id="panel-stations">
                    <div class="stations-grid" id="stationsGrid"></div>
                </div>

                <!-- Equalizer -->
                <div class="tab-panel" id="panel-equalizer">
                    <div class="eq-presets-wrap" id="eqPresets"></div>
                    <div class="eq-bands" id="eqBands"></div>
                </div>

                <!-- Effects -->
                <div class="tab-panel" id="panel-effects">
                    <div class="effects-grid" id="effectsGrid"></div>
                </div>

                <!-- Settings -->
                <div class="tab-panel" id="panel-settings">
                    <div class="settings-list" id="settingsList"></div>
                </div>
            </div>

            <!-- Footer -->
            <div class="footer-section">
                <div class="listeners-info">
                    <div class="avatar-stack">
                        <div class="avatar-item">👨</div>
                        <div class="avatar-item">👩</div>
                        <div class="avatar-item">🧑</div>
                    </div>
                    <span><span class="listener-count" id="listenerCount">15.2K</span> dinleyici</span>
                </div>
                <div class="action-buttons">
                    <button class="action-btn" id="sleepBtn">⏰ Uyku</button>
                    <button class="action-btn" id="recordBtn">⏺️ Kaydet</button>
                    <button class="action-btn" id="shareBtn">📤 Paylaş</button>
                </div>
            </div>
        </div>
    </div>

    <script>
        // ========== DATA ==========
        const stations = [
            { id: 1, name: 'Power Türk', freq: 101.5, emoji: '🎵', color: '#6366f1' },
            { id: 2, name: 'Kral FM', freq: 95.3, emoji: '👑', color: '#ec4899' },
            { id: 3, name: 'Süper FM', freq: 98.7, emoji: '🌟', color: '#f59e0b' },
            { id: 4, name: 'Metro FM', freq: 92.4, emoji: '🚗', color: '#06b6d4' },
            { id: 5, name: 'Joy FM', freq: 100.8, emoji: '🎷', color: '#8b5cf6' },
            { id: 6, name: 'Radyo D', freq: 94.1, emoji: '📰', color: '#22c55e' },
            { id: 7, name: 'Power FM', freq: 100.0, emoji: '⚡', color: '#ef4444' },
            { id: 8, name: 'Virgin Radio', freq: 103.2, emoji: '🎸', color: '#f97316' },
            { id: 9, name: 'Number One', freq: 96.6, emoji: '1️⃣', color: '#14b8a6' }
        ];

        const eqPresets = {
            normal: [50, 50, 50, 50, 50],
            pop: [35, 45, 60, 55, 40],
            rock: [65, 50, 40, 55, 60],
            jazz: [40, 55, 60, 50, 40],
            classical: [50, 45, 40, 50, 55],
            bass: [85, 75, 50, 35, 30]
        };

        const eqBandsData = [
            { label: '60Hz', value: 50 },
            { label: '250Hz', value: 50 },
            { label: '1kHz', value: 50 },
            { label: '4kHz', value: 50 },
            { label: '16kHz', value: 50 }
        ];

        const effectsData = [
            { id: 'reverb', name: 'Reverb', desc: 'Derin yankı', icon: '🌊', active: false },
            { id: 'bass', name: 'Bass Boost', desc: 'Güçlü bas', icon: '🔊', active: false },
            { id: 'spatial', name: '3D Audio', desc: 'Uzaysal ses', icon: '🌐', active: false },
            { id: 'vocal', name: 'Vocal Clear', desc: 'Net vokal', icon: '🎤', active: false }
        ];

        const settingsData = [
            { id: 'autoplay', name: 'Otomatik Başlat', icon: '▶️', active: true },
            { id: 'hd', name: 'HD Ses Kalitesi', icon: '🎧', active: true },
            { id: 'notify', name: 'Bildirimler', icon: '🔔', active: false },
            { id: 'dark', name: 'Karanlık Tema', icon: '🌙', active: true },
            { id: 'crossfade', name: 'Crossfade', icon: '🔀', active: true }
        ];

        // ========== STATE ==========
        let state = {
            playing: true,
            station: stations[0],
            volume: 75,
            progress: 45,
            shuffle: false,
            repeat: false,
            recording: false,
            sleepMinutes: 0,
            sleepTimer: null,
            preset: 'normal'
        };

        // ========== VISUALIZER ==========
        const visCanvas = document.getElementById('visualizerCanvas');
        const visCtx = visCanvas.getContext('2d');
        let bars = [];

        function initVisualizer() {
            visCanvas.width = visCanvas.offsetWidth * 2;
            visCanvas.height = visCanvas.offsetHeight * 2;
            visCtx.scale(2, 2);
            
            bars = [];
            const count = 80;
            const gap = 3;
            const width = (visCanvas.offsetWidth - gap * count) / count;
            
            for (let i = 0; i < count; i++) {
                bars.push({
                    x: i * (width + gap),
                    width: width,
                    height: Math.random() * 30 + 5,
                    target: Math.random() * 60 + 10,
                    hue: 250 + (i / count) * 80
                });
            }
        }

        function animateVisualizer() {
            visCtx.clearRect(0, 0, visCanvas.offsetWidth, visCanvas.offsetHeight);
            
            bars.forEach((bar, i) => {
                if (state.playing) {
                    bar.target = Math.random() * 100 + 20;
                } else {
                    bar.target = 15;
                }
                bar.height += (bar.target - bar.height) * 0.15;
                
                const grad = visCtx.createLinearGradient(0, 160, 0, 160 - bar.height);
                grad.addColorStop(0, `hsla(${bar.hue}, 85%, 55%, 0.9)`);
                grad.addColorStop(1, `hsla(${bar.hue}, 85%, 35%, 0.1)`);
                
                visCtx.fillStyle = grad;
                visCtx.beginPath();
                visCtx.roundRect(bar.x, 160 - bar.height, bar.width, bar.height, 2);
                visCtx.fill();
            });
            
            requestAnimationFrame(animateVisualizer);
        }

        initVisualizer();
        window.addEventListener('resize', initVisualizer);
        animateVisualizer();

        // ========== WAVEFORM ==========
        const waveCanvas = document.getElementById('waveformCanvas');
        const waveCtx = waveCanvas.getContext('2d');

        function initWaveform() {
            waveCanvas.width = waveCanvas.offsetWidth * 2;
            waveCanvas.height = waveCanvas.offsetHeight * 2;
            waveCtx.scale(2, 2);
        }

        function drawWaveform() {
            waveCtx.clearRect(0, 0, waveCanvas.offsetWidth, waveCanvas.offsetHeight);
            const h = waveCanvas.offsetHeight / 2;
            
            for (let x = 0; x < waveCanvas.offsetWidth; x += 3) {
                const amp = Math.sin(x * 0.04 + Date.now() * 0.003) * 12 + Math.random() * 4;
                waveCtx.fillStyle = `rgba(99, 102, 241, ${0.4 + Math.random() * 0.3})`;
                waveCtx.fillRect(x, h - amp, 2, amp * 2);
            }
            
            requestAnimationFrame(drawWaveform);
        }

        initWaveform();
        window.addEventListener('resize', initWaveform);
        drawWaveform();

        // Progress click
        document.getElementById('waveformContainer').addEventListener('click', e => {
            const rect = e.currentTarget.getBoundingClientRect();
            state.progress = ((e.clientX - rect.left) / rect.width) * 100;
            updateProgress();
        });

        function updateProgress() {
            document.getElementById('waveProgress').style.width = state.progress + '%';
            document.getElementById('waveCursor').style.left = state.progress + '%';
        }

        // Time update
        setInterval(() => {
            if (state.playing && state.progress < 100) {
                state.progress += 0.02;
                updateProgress();
                const secs = Math.floor((state.progress / 100) * 300);
                document.getElementById('currentTime').textContent = 
                    String(Math.floor(secs / 60)).padStart(2, '0') + ':' + String(secs % 60).padStart(2, '0');
            }
        }, 100);

        // ========== SIGNAL BARS ==========
        function initSignalBars() {
            const container = document.getElementById('signalBars');
            container.innerHTML = '';
            for (let i = 0; i < 5; i++) {
                const bar = document.createElement('div');
                bar.className = 'sig-bar';
                bar.style.height = (i + 1) * 5 + 'px';
                container.appendChild(bar);
            }
        }
        initSignalBars();

        setInterval(() => {
            const bars = document.querySelectorAll('.sig-bar');
            const active = state.playing ? Math.floor(Math.random() * 2) + 3 : 1;
            bars.forEach((b, i) => b.classList.toggle('active', i < active));
        }, 400);

        // ========== RENDER STATIONS ==========
        function renderStations() {
            const grid = document.getElementById('stationsGrid');
            grid.innerHTML = stations.map(s => `
                <div class="station-card ${s.id === state.station.id ? 'active' : ''}" data-id="${s.id}">
                    <span class="station-emoji">${s.emoji}</span>
                    <div class="station-name">${s.name}</div>
                    <div class="station-freq">${s.freq} MHz</div>
                </div>
            `).join('');

            grid.querySelectorAll('.station-card').forEach(card => {
                card.addEventListener('click', () => {
                    const id = parseInt(card.dataset.id);
                    state.station = stations.find(s => s.id === id);
                    updateStation();
                    renderStations();
                });
            });
        }

        function updateStation() {
            document.getElementById('freqNum').textContent = state.station.freq.toFixed(1);
            document.getElementById('artistName').textContent = state.station.name;
            document.getElementById('albumEmoji').textContent = state.station.emoji;
        }

        // ========== RENDER EQUALIZER ==========
        function renderEqualizer() {
            // Presets
            const presetsWrap = document.getElementById('eqPresets');
            presetsWrap.innerHTML = Object.keys(eqPresets).map(p => `
                <button class="eq-preset ${p === state.preset ? 'active' : ''}" data-preset="${p}">
                    ${p.charAt(0).toUpperCase() + p.slice(1)}
                </button>
            `).join('');

            presetsWrap.querySelectorAll('.eq-preset').forEach(btn => {
                btn.addEventListener('click', () => {
                    state.preset = btn.dataset.preset;
                    eqPresets[state.preset].forEach((v, i) => eqBandsData[i].value = v);
                    renderEqualizer();
                });
            });

            // Bands
            const bandsWrap = document.getElementById('eqBands');
            bandsWrap.innerHTML = eqBandsData.map((b, i) => `
                <div class="eq-band">
                    <div class="eq-track" data-idx="${i}">
                        <div class="eq-fill" style="height: ${b.value}%"></div>
                    </div>
                    <span class="eq-label">${b.label}</span>
                    <span class="eq-val">${b.value}%</span>
                </div>
            `).join('');

            bandsWrap.querySelectorAll('.eq-track').forEach(track => {
                track.addEventListener('click', e => {
                    const rect = track.getBoundingClientRect();
                    const pct = 100 - ((e.clientY - rect.top) / rect.height * 100);
                    const idx = parseInt(track.dataset.idx);
                    eqBandsData[idx].value = Math.round(Math.max(0, Math.min(100, pct)));
                    track.querySelector('.eq-fill').style.height = eqBandsData[idx].value + '%';
                    track.closest('.eq-band').querySelector('.eq-val').textContent = eqBandsData[idx].value + '%';
                });
            });
        }

        // ========== RENDER EFFECTS ==========
        function renderEffects() {
            const grid = document.getElementById('effectsGrid');
            grid.innerHTML = effectsData.map(e => `
                <div class="effect-item ${e.active ? 'active' : ''}" data-id="${e.id}">
                    <div class="effect-icon">${e.icon}</div>
                    <div class="effect-text">
                        <h4>${e.name}</h4>
                        <p>${e.desc}</p>
                    </div>
                </div>
            `).join('');

            grid.querySelectorAll('.effect-item').forEach(item => {
                item.addEventListener('click', () => {
                    const effect = effectsData.find(e => e.id === item.dataset.id);
                    effect.active = !effect.active;
                    item.classList.toggle('active', effect.active);
                });
            });
        }

        // ========== RENDER SETTINGS ==========
        function renderSettings() {
            const list = document.getElementById('settingsList');
            list.innerHTML = settingsData.map(s => `
                <div class="setting-item">
                    <div class="setting-label">
                        <span>${s.icon}</span>
                        ${s.name}
                    </div>
                    <div class="toggle ${s.active ? 'active' : ''}" data-id="${s.id}"></div>
                </div>
            `).join('');

            list.querySelectorAll('.toggle').forEach(toggle => {
                toggle.addEventListener('click', () => {
                    const setting = settingsData.find(s => s.id === toggle.dataset.id);
                    setting.active = !setting.active;
                    toggle.classList.toggle('active', setting.active);
                });
            });
        }

        // ========== TABS ==========
        document.querySelectorAll('.tab-trigger').forEach(trigger => {
            trigger.addEventListener('click', () => {
                document.querySelectorAll('.tab-trigger').forEach(t => t.classList.remove('active'));
                document.querySelectorAll('.tab-panel').forEach(p => p.classList.remove('active'));
                trigger.classList.add('active');
                document.getElementById(`panel-${trigger.dataset.tab}`).classList.add('active');
            });
        });

        // ========== CONTROLS ==========
        document.getElementById('playBtn').addEventListener('click', () => {
            state.playing = !state.playing;
            document.getElementById('playerCard').classList.toggle('playing', state.playing);
            
            const icon = document.getElementById('playIcon');
            if (state.playing) {
                icon.innerHTML = `
                    <rect x="6" y="4" width="4" height="16" rx="1" fill="white" stroke="none"></rect>
                    <rect x="14" y="4" width="4" height="16" rx="1" fill="white" stroke="none"></rect>
                `;
            } else {
                icon.innerHTML = '<polygon points="5 3 19 12 5 21" fill="white" stroke="none"></polygon>';
            }
        });

        document.getElementById('prevBtn').addEventListener('click', () => {
            const idx = stations.findIndex(s => s.id === state.station.id);
            state.station = stations[(idx - 1 + stations.length) % stations.length];
            updateStation();
            renderStations();
        });

        document.getElementById('nextBtn').addEventListener('click', () => {
            const idx = stations.findIndex(s => s.id === state.station.id);
            state.station = stations[(idx + 1) % stations.length];
            updateStation();
            renderStations();
        });

        document.getElementById('shuffleBtn').addEventListener('click', function() {
            state.shuffle = !state.shuffle;
            this.classList.toggle('active', state.shuffle);
        });

        document.getElementById('repeatBtn').addEventListener('click', function() {
            state.repeat = !state.repeat;
            this.classList.toggle('active', state.repeat);
        });

        document.getElementById('powerBtn').addEventListener('click', function() {
            this.classList.toggle('active');
            state.playing = !this.classList.contains('active');
            document.getElementById('playerCard').classList.toggle('playing', state.playing);
        });

        // ========== VOLUME ==========
        const volSlider = document.getElementById('volumeSlider');
        const volFill = document.getElementById('volumeFill');
        const volPercent = document.getElementById('volPercent');
        const volIconWrap = document.getElementById('volIcon');

        function setVolume(e) {
            const rect = volSlider.getBoundingClientRect();
            state.volume = Math.round(Math.max(0, Math.min(100, ((e.clientX - rect.left) / rect.width) * 100)));
            volFill.style.width = state.volume + '%';
            volPercent.textContent = state.volume + '%';
            updateVolIcon();
        }

        function updateVolIcon() {
            const svg = volIconWrap.querySelector('svg');
            if (state.volume === 0) {
                svg.innerHTML = `
                    <polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"></polygon>
                    <line x1="23" y1="9" x2="17" y2="15"></line>
                    <line x1="17" y1="9" x2="23" y2="15"></line>
                `;
            } else if (state.volume < 50) {
                svg.innerHTML = `
                    <polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"></polygon>
                    <path d="M15.54 8.46a5 5 0 0 1 0 7.07"></path>
                `;
            } else {
                svg.innerHTML = `
                    <polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"></polygon>
                    <path d="M19.07 4.93a10 10 0 0 1 0 14.14M15.54 8.46a5 5 0 0 1 0 7.07"></path>
                `;
            }
        }

        volSlider.addEventListener('click', setVolume);
        let dragging = false;
        volSlider.addEventListener('mousedown', () => dragging = true);
        document.addEventListener('mousemove', e => { if (dragging) setVolume(e); });
        document.addEventListener('mouseup', () => dragging = false);

        volIconWrap.addEventListener('click', () => {
            if (state.volume > 0) {
                volFill.dataset.prev = state.volume;
                state.volume = 0;
            } else {
                state.volume = volFill.dataset.prev || 75;
            }
            volFill.style.width = state.volume + '%';
            volPercent.textContent = state.volume + '%';
            updateVolIcon();
        });

        // ========== QUICK ACTIONS ==========
        document.getElementById('sleepBtn').addEventListener('click', () => {
            document.getElementById('sleepModal').classList.add('active');
        });

        function closeSleepModal() {
            document.getElementById('sleepModal').classList.remove('active');
        }

        // Sleep options
        function initSleepOptions() {
            const grid = document.getElementById('sleepOptions');
            const opts = [15, 30, 45, 60, 90, 0];
            grid.innerHTML = opts.map(m => `
                <div class="sleep-opt" data-mins="${m}">
                    <div class="time-val">${m === 0 ? '∞' : m}</div>
                    <div class="time-unit">${m === 0 ? 'Kapat' : 'dakika'}</div>
                </div>
            `).join('');

            grid.querySelectorAll('.sleep-opt').forEach(opt => {
                opt.addEventListener('click', () => {
                    const mins = parseInt(opt.dataset.mins);
                    if (mins === 0) {
                        clearInterval(state.sleepTimer);
                        state.sleepMinutes = 0;
                        document.getElementById('sleepBadge').classList.remove('active');
                    } else {
                        state.sleepMinutes = mins;
                        document.getElementById('sleepBadge').classList.add('active');
                        document.getElementById('sleepTime').textContent = mins + ':00';
                        startSleepCountdown();
                    }
                    closeSleepModal();
                });
            });
        }

        function startSleepCountdown() {
            clearInterval(state.sleepTimer);
            state.sleepTimer = setInterval(() => {
                if (state.sleepMinutes > 0) {
                    state.sleepMinutes--;
                    const m = Math.floor(state.sleepMinutes);
                    const s = (state.sleepMinutes % 1) * 60;
                    document.getElementById('sleepTime').textContent = 
                        String(m).padStart(2, '0') + ':' + String(Math.round(s)).padStart(2, '0');
                    
                    if (state.sleepMinutes <= 0) {
                        state.playing = false;
                        document.getElementById('playerCard').classList.remove('playing');
                        document.getElementById('sleepBadge').classList.remove('active');
                        clearInterval(state.sleepTimer);
                    }
                }
            }, 60000);
        }

        initSleepOptions();

        document.getElementById('recordBtn').addEventListener('click', function() {
            state.recording = !state.recording;
            document.getElementById('recBadge').classList.toggle('active', state.recording);
            this.classList.toggle('recording', state.recording);
            this.innerHTML = state.recording ? '⏹️ Durdur' : '⏺️ Kaydet';
        });

        document.getElementById('shareBtn').addEventListener('click', () => {
            const text = `${state.station.name} - ${state.station.freq} MHz dinliyorum! 📻`;
            alert('Link kopyalandı!\n\n' + text);
        });

        // ========== LISTENERS COUNT ==========
        setInterval(() => {
            const count = 14000 + Math.floor(Math.random() * 2000);
            document.getElementById('listenerCount').textContent = (count / 1000).toFixed(1) + 'K';
        }, 4000);

        // ========== INIT ==========
        renderStations();
        renderEqualizer();
        renderEffects();
        renderSettings();
    </script>
</body>
</html>
```