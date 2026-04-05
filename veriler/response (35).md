<think>
Kullanıcı, radyo widget'ını yeni özelliklerle geliştirmemi istiyor. Daha gelişmiş ve modern özellikler eklemeliyim. İşte ekleyebileceğim bazı özellikler:

1. Playlist/Şarkı listesi görünümü
2. Daha gelişmiş visualizer efektleri (dalga, dairesel, parçacık efektleri)
3. Tema değiştirici (dark/light/colorful)
4. Radyo kaydırma tuneri (dial knob)
5. Şarkı sözleri görüntüleme
6. Ses efektleri (reverb, bass boost, 3D ses)
7. Radyo tarzı tuner tekerleği
8. Animasyonlu arka plan partikülleri
9. Canlı dinleyici sayısı
10. Şarkı geçmişi
11. Favori istasyonlar yönetimi
12. Ses dalga formu göstergesi
13. Bluetooth/AirPlay cast simülasyonu
14. Uyku modu efektleri (fade out)
15. Daha gelişmiş ekolayzer (presets)
16. Mini player modu
17. Widget boyut değiştirme
18. Radyo sinyal gücü göstergesi
19. Frekans tuner slider
20. Animasyonlu geçişler

Tüm bunları tek bir geliştirilmiş widget'ta birleştireyim.
</think>```html
<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Gelişmiş Radyo Widget</title>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&family=Orbitron:wght@400;500;700;900&display=swap" rel="stylesheet">
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        :root {
            --primary: #8b5cf6;
            --primary-light: #a78bfa;
            --accent: #f472b6;
            --accent-alt: #06b6d4;
            --bg-dark: #0a0a12;
            --bg-card: rgba(20, 20, 35, 0.9);
            --text: #ffffff;
            --text-muted: #8888a0;
            --glass: rgba(255, 255, 255, 0.05);
            --glass-border: rgba(255, 255, 255, 0.08);
            --gradient-1: linear-gradient(135deg, #8b5cf6, #06b6d4);
            --gradient-2: linear-gradient(135deg, #f472b6, #fb923c);
        }

        body {
            font-family: 'Poppins', sans-serif;
            background: var(--bg-dark);
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 15px;
            overflow-x: hidden;
        }

        /* Animated Background */
        .bg-container {
            position: fixed;
            inset: 0;
            z-index: -1;
            overflow: hidden;
        }

        .bg-particles {
            position: absolute;
            inset: 0;
        }

        .particle {
            position: absolute;
            border-radius: 50%;
            pointer-events: none;
            animation: particleFloat 20s infinite;
        }

        @keyframes particleFloat {
            0%, 100% { transform: translateY(100vh) rotate(0deg); opacity: 0; }
            10% { opacity: 1; }
            90% { opacity: 1; }
            100% { transform: translateY(-100vh) rotate(720deg); opacity: 0; }
        }

        .gradient-sphere {
            position: absolute;
            border-radius: 50%;
            filter: blur(100px);
            animation: sphereMove 15s ease-in-out infinite;
        }

        @keyframes sphereMove {
            0%, 100% { transform: translate(0, 0) scale(1); }
            25% { transform: translate(50px, -30px) scale(1.1); }
            50% { transform: translate(-30px, 50px) scale(0.9); }
            75% { transform: translate(-50px, -20px) scale(1.05); }
        }

        /* Main Container */
        .radio-widget {
            width: 100%;
            max-width: 440px;
            background: var(--bg-card);
            backdrop-filter: blur(30px);
            border-radius: 28px;
            border: 1px solid var(--glass-border);
            box-shadow: 
                0 30px 60px -20px rgba(0, 0, 0, 0.7),
                0 0 0 1px rgba(255, 255, 255, 0.05) inset;
            overflow: hidden;
            position: relative;
        }

        /* Glow Effect */
        .glow-ring {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            width: 300px;
            height: 300px;
            border-radius: 50%;
            background: radial-gradient(circle, rgba(139, 92, 246, 0.15) 0%, transparent 70%);
            pointer-events: none;
            opacity: 0;
            transition: opacity 0.5s;
        }

        .radio-widget.playing .glow-ring {
            opacity: 1;
            animation: glowPulse 2s ease-in-out infinite;
        }

        @keyframes glowPulse {
            0%, 100% { transform: translate(-50%, -50%) scale(1); opacity: 0.5; }
            50% { transform: translate(-50%, -50%) scale(1.2); opacity: 0.8; }
        }

        /* Header */
        .header {
            padding: 16px 20px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            border-bottom: 1px solid var(--glass-border);
            position: relative;
            z-index: 10;
        }

        .logo-section {
            display: flex;
            align-items: center;
            gap: 12px;
        }

        .logo-icon {
            width: 44px;
            height: 44px;
            background: var(--gradient-1);
            border-radius: 14px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 22px;
            position: relative;
            overflow: hidden;
        }

        .logo-icon::after {
            content: '';
            position: absolute;
            inset: 0;
            background: linear-gradient(45deg, transparent 40%, rgba(255,255,255,0.3) 50%, transparent 60%);
            animation: shimmer 3s infinite;
        }

        @keyframes shimmer {
            0% { transform: translateX(-100%); }
            100% { transform: translateX(100%); }
        }

        .logo-text {
            font-family: 'Orbitron', sans-serif;
            font-weight: 700;
            font-size: 20px;
            background: linear-gradient(135deg, #fff, var(--text-muted));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }

        .header-actions {
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .status-badge {
            display: flex;
            align-items: center;
            gap: 6px;
            padding: 6px 12px;
            background: rgba(34, 197, 94, 0.15);
            border: 1px solid rgba(34, 197, 94, 0.3);
            border-radius: 20px;
            font-size: 11px;
            color: #22c55e;
            font-weight: 500;
        }

        .live-dot {
            width: 6px;
            height: 6px;
            background: #22c55e;
            border-radius: 50%;
            animation: livePulse 1.5s infinite;
        }

        @keyframes livePulse {
            0%, 100% { opacity: 1; box-shadow: 0 0 0 0 rgba(34, 197, 94, 0.5); }
            50% { opacity: 0.6; box-shadow: 0 0 0 6px rgba(34, 197, 94, 0); }
        }

        .icon-btn {
            width: 40px;
            height: 40px;
            border-radius: 12px;
            background: var(--glass);
            border: 1px solid var(--glass-border);
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            transition: all 0.3s ease;
        }

        .icon-btn:hover {
            background: rgba(255, 255, 255, 0.1);
            transform: scale(1.05);
        }

        .icon-btn svg {
            width: 18px;
            height: 18px;
            stroke: var(--text-muted);
            transition: stroke 0.3s;
        }

        .icon-btn:hover svg {
            stroke: var(--text);
        }

        .icon-btn.active {
            background: var(--gradient-1);
            border-color: transparent;
        }

        .icon-btn.active svg {
            stroke: white;
        }

        /* Visualizer Section */
        .visualizer-wrapper {
            padding: 20px;
            position: relative;
        }

        .visualizer-card {
            background: rgba(0, 0, 0, 0.4);
            border-radius: 20px;
            padding: 20px;
            position: relative;
            overflow: hidden;
        }

        .visualizer-card::before {
            content: '';
            position: absolute;
            inset: 0;
            background: linear-gradient(180deg, transparent 0%, rgba(139, 92, 246, 0.1) 100%);
            pointer-events: none;
        }

        #mainVisualizer {
            width: 100%;
            height: 140px;
            display: block;
        }

        .frequency-badge {
            position: absolute;
            top: 16px;
            right: 16px;
            font-family: 'Orbitron', sans-serif;
            font-size: 24px;
            font-weight: 900;
            color: white;
            text-shadow: 0 0 30px var(--primary);
        }

        .frequency-badge span {
            font-size: 12px;
            font-weight: 400;
            color: var(--text-muted);
            margin-left: 4px;
        }

        /* Signal Strength */
        .signal-meter {
            position: absolute;
            top: 16px;
            left: 16px;
            display: flex;
            align-items: flex-end;
            gap: 3px;
            height: 20px;
        }

        .signal-bar {
            width: 4px;
            background: var(--text-muted);
            border-radius: 2px;
            transition: all 0.3s;
        }

        .signal-bar.active {
            background: #22c55e;
            box-shadow: 0 0 8px rgba(34, 197, 94, 0.5);
        }

        /* Station Info */
        .station-display {
            padding: 0 20px;
            text-align: center;
        }

        .album-art {
            width: 100px;
            height: 100px;
            margin: 0 auto 16px;
            border-radius: 20px;
            background: var(--gradient-1);
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 42px;
            position: relative;
            box-shadow: 0 15px 30px rgba(139, 92, 246, 0.3);
            animation: albumFloat 4s ease-in-out infinite;
        }

        @keyframes albumFloat {
            0%, 100% { transform: translateY(0) rotate(0deg); }
            50% { transform: translateY(-8px) rotate(2deg); }
        }

        .album-art::before {
            content: '';
            position: absolute;
            inset: -3px;
            border-radius: 22px;
            background: var(--gradient-1);
            z-index: -1;
            opacity: 0.5;
            filter: blur(10px);
        }

        .now-playing-label {
            font-size: 10px;
            text-transform: uppercase;
            letter-spacing: 3px;
            color: var(--primary);
            font-weight: 600;
            margin-bottom: 8px;
        }

        .track-title {
            font-size: 20px;
            font-weight: 600;
            color: var(--text);
            margin-bottom: 4px;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
        }

        .track-artist {
            font-size: 14px;
            color: var(--text-muted);
        }

        /* Progress Section */
        .progress-section {
            padding: 20px;
        }

        .waveform-progress {
            position: relative;
            height: 40px;
            background: rgba(0, 0, 0, 0.3);
            border-radius: 10px;
            overflow: hidden;
            cursor: pointer;
        }

        #waveformCanvas {
            width: 100%;
            height: 100%;
        }

        .progress-overlay {
            position: absolute;
            top: 0;
            left: 0;
            height: 100%;
            background: linear-gradient(90deg, rgba(139, 92, 246, 0.4), rgba(6, 182, 212, 0.4));
            pointer-events: none;
            transition: width 0.1s;
        }

        .time-row {
            display: flex;
            justify-content: space-between;
            margin-top: 10px;
            font-family: 'Orbitron', sans-serif;
            font-size: 11px;
            color: var(--text-muted);
        }

        /* Main Controls */
        .controls-row {
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 14px;
            padding: 0 20px 20px;
        }

        .ctrl-btn {
            width: 48px;
            height: 48px;
            border-radius: 50%;
            background: var(--glass);
            border: 1px solid var(--glass-border);
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        }

        .ctrl-btn:hover {
            background: rgba(255, 255, 255, 0.12);
            transform: scale(1.1);
        }

        .ctrl-btn:active {
            transform: scale(0.95);
        }

        .ctrl-btn svg {
            width: 20px;
            height: 20px;
            stroke: var(--text);
            fill: none;
        }

        .ctrl-btn.active {
            background: var(--gradient-1);
            border-color: transparent;
            box-shadow: 0 8px 25px rgba(139, 92, 246, 0.4);
        }

        .play-ctrl {
            width: 72px;
            height: 72px;
            background: var(--gradient-1);
            border: none;
            box-shadow: 0 12px 35px rgba(139, 92, 246, 0.5);
        }

        .play-ctrl:hover {
            box-shadow: 0 16px 45px rgba(139, 92, 246, 0.6);
            transform: scale(1.15);
        }

        .play-ctrl svg {
            width: 28px;
            height: 28px;
            fill: white;
            stroke: white;
        }

        /* Volume Section */
        .volume-row {
            display: flex;
            align-items: center;
            gap: 12px;
            padding: 0 20px 20px;
        }

        .vol-icon {
            width: 22px;
            height: 22px;
            stroke: var(--text-muted);
            cursor: pointer;
            transition: all 0.3s;
        }

        .vol-icon:hover {
            stroke: var(--text);
        }

        .vol-slider-container {
            flex: 1;
            height: 8px;
            background: rgba(255, 255, 255, 0.1);
            border-radius: 4px;
            position: relative;
            cursor: pointer;
            overflow: hidden;
        }

        .vol-slider-fill {
            height: 100%;
            background: var(--gradient-1);
            border-radius: 4px;
            position: relative;
            transition: width 0.1s;
        }

        .vol-slider-handle {
            position: absolute;
            right: -7px;
            top: 50%;
            transform: translateY(-50%);
            width: 16px;
            height: 16px;
            background: white;
            border-radius: 50%;
            box-shadow: 0 2px 10px rgba(0,0,0,0.3);
        }

        .vol-value {
            font-family: 'Orbitron', sans-serif;
            font-size: 12px;
            color: var(--text-muted);
            width: 40px;
            text-align: right;
        }

        /* Tabs */
        .tabs-container {
            border-top: 1px solid var(--glass-border);
        }

        .tabs-header {
            display: flex;
            padding: 0 20px;
            border-bottom: 1px solid var(--glass-border);
        }

        .tab-btn {
            flex: 1;
            padding: 14px;
            background: none;
            border: none;
            color: var(--text-muted);
            font-size: 13px;
            font-weight: 500;
            cursor: pointer;
            position: relative;
            transition: all 0.3s;
        }

        .tab-btn.active {
            color: var(--text);
        }

        .tab-btn::after {
            content: '';
            position: absolute;
            bottom: 0;
            left: 50%;
            transform: translateX(-50%);
            width: 0;
            height: 2px;
            background: var(--gradient-1);
            border-radius: 2px;
            transition: width 0.3s;
        }

        .tab-btn.active::after {
            width: 50%;
        }

        .tab-content {
            display: none;
            padding: 16px 20px;
            max-height: 220px;
            overflow-y: auto;
        }

        .tab-content.active {
            display: block;
        }

        .tab-content::-webkit-scrollbar {
            width: 4px;
        }

        .tab-content::-webkit-scrollbar-track {
            background: transparent;
        }

        .tab-content::-webkit-scrollbar-thumb {
            background: var(--glass-border);
            border-radius: 2px;
        }

        /* Stations Grid */
        .stations-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 10px;
        }

        .station-item {
            background: var(--glass);
            border: 1px solid var(--glass-border);
            border-radius: 14px;
            padding: 14px 10px;
            text-align: center;
            cursor: pointer;
            transition: all 0.3s;
        }

        .station-item:hover {
            background: rgba(255, 255, 255, 0.08);
            transform: translateY(-3px);
        }

        .station-item.active {
            background: linear-gradient(135deg, rgba(139, 92, 246, 0.2), rgba(6, 182, 212, 0.2));
            border-color: var(--primary);
        }

        .station-item .emoji {
            font-size: 28px;
            margin-bottom: 8px;
            display: block;
        }

        .station-item .name {
            font-size: 11px;
            color: var(--text);
            font-weight: 500;
        }

        .station-item .freq {
            font-family: 'Orbitron', sans-serif;
            font-size: 9px;
            color: var(--text-muted);
            margin-top: 4px;
        }

        /* Equalizer */
        .eq-presets {
            display: flex;
            gap: 8px;
            margin-bottom: 16px;
            flex-wrap: wrap;
        }

        .eq-preset-btn {
            padding: 8px 14px;
            background: var(--glass);
            border: 1px solid var(--glass-border);
            border-radius: 20px;
            color: var(--text-muted);
            font-size: 11px;
            cursor: pointer;
            transition: all 0.3s;
        }

        .eq-preset-btn:hover,
        .eq-preset-btn.active {
            background: var(--gradient-1);
            border-color: transparent;
            color: white;
        }

        .eq-sliders {
            display: flex;
            justify-content: space-between;
            gap: 12px;
        }

        .eq-band {
            flex: 1;
            display: flex;
            flex-direction: column;
            align-items: center;
        }

        .eq-track {
            width: 100%;
            height: 80px;
            background: rgba(0, 0, 0, 0.3);
            border-radius: 6px;
            position: relative;
            cursor: pointer;
            overflow: hidden;
        }

        .eq-fill {
            position: absolute;
            bottom: 0;
            width: 100%;
            background: linear-gradient(to top, var(--primary), var(--accent-alt));
            border-radius: 6px;
            transition: height 0.2s;
        }

        .eq-label {
            font-size: 9px;
            color: var(--text-muted);
            margin-top: 6px;
            text-transform: uppercase;
        }

        .eq-value {
            font-family: 'Orbitron', sans-serif;
            font-size: 10px;
            color: var(--primary);
            margin-top: 2px;
        }

        /* Effects Section */
        .effects-grid {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 10px;
        }

        .effect-card {
            background: var(--glass);
            border: 1px solid var(--glass-border);
            border-radius: 14px;
            padding: 14px;
            display: flex;
            align-items: center;
            gap: 12px;
            cursor: pointer;
            transition: all 0.3s;
        }

        .effect-card:hover {
            background: rgba(255, 255, 255, 0.08);
        }

        .effect-card.active {
            background: linear-gradient(135deg, rgba(139, 92, 246, 0.2), rgba(244, 114, 182, 0.2));
            border-color: var(--primary);
        }

        .effect-icon {
            width: 36px;
            height: 36px;
            background: var(--gradient-1);
            border-radius: 10px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 16px;
        }

        .effect-info h4 {
            font-size: 13px;
            color: var(--text);
            font-weight: 500;
        }

        .effect-info p {
            font-size: 10px;
            color: var(--text-muted);
        }

        /* Settings */
        .settings-list {
            display: flex;
            flex-direction: column;
            gap: 10px;
        }

        .setting-row {
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 12px 14px;
            background: var(--glass);
            border: 1px solid var(--glass-border);
            border-radius: 12px;
        }

        .setting-label {
            display: flex;
            align-items: center;
            gap: 10px;
            color: var(--text);
            font-size: 13px;
        }

        .setting-label span {
            font-size: 18px;
        }

        /* Toggle Switch */
        .toggle-switch {
            width: 44px;
            height: 24px;
            background: rgba(255, 255, 255, 0.1);
            border-radius: 12px;
            position: relative;
            cursor: pointer;
            transition: all 0.3s;
        }

        .toggle-switch.active {
            background: var(--gradient-1);
        }

        .toggle-switch::after {
            content: '';
            position: absolute;
            top: 2px;
            left: 2px;
            width: 20px;
            height: 20px;
            background: white;
            border-radius: 50%;
            transition: transform 0.3s;
        }

        .toggle-switch.active::after {
            transform: translateX(20px);
        }

        /* Footer */
        .widget-footer {
            padding: 14px 20px;
            background: rgba(0, 0, 0, 0.3);
            border-top: 1px solid var(--glass-border);
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .listeners-count {
            display: flex;
            align-items: center;
            gap: 8px;
            font-size: 12px;
            color: var(--text-muted);
        }

        .listeners-avatars {
            display: flex;
        }

        .avatar {
            width: 24px;
            height: 24px;
            border-radius: 50%;
            background: var(--gradient-1);
            border: 2px solid var(--bg-card);
            margin-left: -8px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 10px;
        }

        .avatar:first-child {
            margin-left: 0;
        }

        .quick-actions {
            display: flex;
            gap: 8px;
        }

        .quick-btn {
            padding: 8px 14px;
            background: var(--glass);
            border: 1px solid var(--glass-border);
            border-radius: 20px;
            color: var(--text-muted);
            font-size: 11px;
            cursor: pointer;
            transition: all 0.3s;
            display: flex;
            align-items: center;
            gap: 6px;
        }

        .quick-btn:hover {
            background: rgba(139, 92, 246, 0.2);
            border-color: var(--primary);
            color: var(--text);
        }

        /* Modal */
        .modal-overlay {
            position: fixed;
            inset: 0;
            background: rgba(0, 0, 0, 0.7);
            backdrop-filter: blur(10px);
            display: flex;
            align-items: center;
            justify-content: center;
            z-index: 1000;
            opacity: 0;
            visibility: hidden;
            transition: all 0.3s;
        }

        .modal-overlay.active {
            opacity: 1;
            visibility: visible;
        }

        .modal-content {
            background: var(--bg-card);
            border: 1px solid var(--glass-border);
            border-radius: 24px;
            padding: 24px;
            max-width: 360px;
            width: 90%;
            transform: scale(0.9);
            transition: transform 0.3s;
        }

        .modal-overlay.active .modal-content {
            transform: scale(1);
        }

        .modal-header {
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-bottom: 20px;
        }

        .modal-title {
            font-size: 18px;
            font-weight: 600;
            color: var(--text);
        }

        .modal-close {
            width: 32px;
            height: 32px;
            background: var(--glass);
            border: none;
            border-radius: 8px;
            color: var(--text-muted);
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 18px;
        }

        .sleep-options {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 10px;
        }

        .sleep-option {
            padding: 16px;
            background: var(--glass);
            border: 1px solid var(--glass-border);
            border-radius: 12px;
            text-align: center;
            cursor: pointer;
            transition: all 0.3s;
        }

        .sleep-option:hover {
            background: rgba(139, 92, 246, 0.2);
            border-color: var(--primary);
        }

        .sleep-option .time {
            font-family: 'Orbitron', sans-serif;
            font-size: 18px;
            color: var(--text);
            font-weight: 600;
        }

        .sleep-option .unit {
            font-size: 11px;
            color: var(--text-muted);
        }

        /* Recording Indicator */
        .recording-status {
            position: absolute;
            top: 70px;
            left: 50%;
            transform: translateX(-50%);
            display: flex;
            align-items: center;
            gap: 8px;
            padding: 8px 16px;
            background: rgba(239, 68, 68, 0.2);
            border: 1px solid rgba(239, 68, 68, 0.4);
            border-radius: 20px;
            z-index: 20;
            opacity: 0;
            transition: opacity 0.3s;
        }

        .recording-status.active {
            opacity: 1;
        }

        .rec-dot {
            width: 8px;
            height: 8px;
            background: #ef4444;
            border-radius: 50%;
            animation: recBlink 1s infinite;
        }

        @keyframes recBlink {
            0%, 100% { opacity: 1; }
            50% { opacity: 0.3; }
        }

        .recording-status span {
            font-size: 12px;
            color: #ef4444;
            font-weight: 500;
        }

        /* Sleep Timer Badge */
        .sleep-badge {
            position: absolute;
            top: 70px;
            right: 20px;
            display: flex;
            align-items: center;
            gap: 6px;
            padding: 6px 12px;
            background: rgba(139, 92, 246, 0.2);
            border: 1px solid rgba(139, 92, 246, 0.4);
            border-radius: 20px;
            z-index: 20;
            opacity: 0;
            transition: opacity 0.3s;
        }

        .sleep-badge.active {
            opacity: 1;
        }

        .sleep-badge span {
            font-family: 'Orbitron', sans-serif;
            font-size: 12px;
            color: var(--primary);
        }

        /* Responsive */
        @media (max-width: 400px) {
            .radio-widget {
                border-radius: 24px;
            }
            
            .stations-grid {
                grid-template-columns: repeat(3, 1fr);
                gap: 8px;
            }
            
            .station-item .emoji {
                font-size: 24px;
            }
            
            .ctrl-btn {
                width: 44px;
                height: 44px;
            }
            
            .play-ctrl {
                width: 64px;
                height: 64px;
            }
        }
    </style>
</head>
<body>
    <!-- Background Effects -->
    <div class="bg-container">
        <div class="bg-particles" id="bgParticles"></div>
        <div class="gradient-sphere" style="width: 500px; height: 500px; background: rgba(139, 92, 246, 0.3); top: -200px; left: -200px;"></div>
        <div class="gradient-sphere" style="width: 400px; height: 400px; background: rgba(6, 182, 212, 0.2); bottom: -150px; right: -150px; animation-delay: -5s;"></div>
        <div class="gradient-sphere" style="width: 300px; height: 300px; background: rgba(244, 114, 182, 0.2); top: 50%; left: 50%; transform: translate(-50%, -50%); animation-delay: -10s;"></div>
    </div>

    <!-- Sleep Timer Modal -->
    <div class="modal-overlay" id="sleepModal">
        <div class="modal-content">
            <div class="modal-header">
                <h3 class="modal-title">Uyku Zamanlayıcı</h3>
                <button class="modal-close" onclick="closeSleepModal()">×</button>
            </div>
            <div class="sleep-options">
                <div class="sleep-option" data-minutes="15">
                    <div class="time">15</div>
                    <div class="unit">dakika</div>
                </div>
                <div class="sleep-option" data-minutes="30">
                    <div class="time">30</div>
                    <div class="unit">dakika</div>
                </div>
                <div class="sleep-option" data-minutes="45">
                    <div class="time">45</div>
                    <div class="unit">dakika</div>
                </div>
                <div class="sleep-option" data-minutes="60">
                    <div class="time">60</div>
                    <div class="unit">dakika</div>
                </div>
                <div class="sleep-option" data-minutes="90">
                    <div class="time">90</div>
                    <div class="unit">dakika</div>
                </div>
                <div class="sleep-option" data-minutes="0">
                    <div class="time">∞</div>
                    <div class="unit">kapat</div>
                </div>
            </div>
        </div>
    </div>

    <!-- Main Widget -->
    <div class="radio-widget playing" id="radioWidget">
        <div class="glow-ring"></div>
        
        <!-- Recording Status -->
        <div class="recording-status" id="recordingStatus">
            <div class="rec-dot"></div>
            <span>KAYDEDİYOR</span>
        </div>
        
        <!-- Sleep Timer Badge -->
        <div class="sleep-badge" id="sleepBadge">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <circle cx="12" cy="12" r="10"></circle>
                <polyline points="12 6 12 12 16 14"></polyline>
            </svg>
            <span id="sleepTimerDisplay">--:--</span>
        </div>

        <!-- Header -->
        <div class="header">
            <div class="logo-section">
                <div class="logo-icon">📻</div>
                <span class="logo-text">RadyoPro</span>
            </div>
            <div class="header-actions">
                <div class="status-badge">
                    <div class="live-dot"></div>
                    CANLI
                </div>
                <button class="icon-btn" id="themeBtn" title="Tema">
                    <svg viewBox="0 0 24 24" fill="none" stroke-width="2">
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
                <button class="icon-btn" id="powerBtn" title="Kapat">
                    <svg viewBox="0 0 24 24" fill="none" stroke-width="2">
                        <path d="M18.36 6.64a9 9 0 1 1-12.73 0"></path>
                        <line x1="12" y1="2" x2="12" y2="12"></line>
                    </svg>
                </button>
            </div>
        </div>

        <!-- Visualizer -->
        <div class="visualizer-wrapper">
            <div class="visualizer-card">
                <div class="signal-meter" id="signalMeter">
                    <div class="signal-bar" style="height: 4px;"></div>
                    <div class="signal-bar" style="height: 8px;"></div>
                    <div class="signal-bar" style="height: 12px;"></div>
                    <div class="signal-bar" style="height: 16px;"></div>
                    <div class="signal-bar" style="height: 20px;"></div>
                </div>
                <div class="frequency-badge">
                    <span id="freqValue">101.5</span><span>MHz</span>
                </div>
                <canvas id="mainVisualizer"></canvas>
            </div>
        </div>

        <!-- Station Display -->
        <div class="station-display">
            <div class="album-art" id="albumArt">🎵</div>
            <div class="now-playing-label">ŞU AN ÇALIYOR</div>
            <div class="track-title" id="trackTitle">Yıldız Tozu</div>
            <div class="track-artist" id="trackArtist">Power Türk FM</div>
        </div>

        <!-- Progress -->
        <div class="progress-section">
            <div class="waveform-progress" id="waveformProgress">
                <div class="progress-overlay" id="progressOverlay"></div>
                <canvas id="waveformCanvas"></canvas>
            </div>
            <div class="time-row">
                <span id="currentTime">02:34</span>
                <span>CANLI YAYIN</span>
            </div>
        </div>

        <!-- Main Controls -->
        <div class="controls-row">
            <button class="ctrl-btn" id="shuffleBtn" title="Karıştır">
                <svg viewBox="0 0 24 24" stroke-width="2">
                    <polyline points="16 3 21 3 21 8"></polyline>
                    <line x1="4" y1="20" x2="21" y2="3"></line>
                    <polyline points="21 16 21 21 16 21"></polyline>
                    <line x1="15" y1="15" x2="21" y2="21"></line>
                    <line x1="4" y1="4" x2="9" y2="9"></line>
                </svg>
            </button>
            <button class="ctrl-btn" id="prevBtn" title="Önceki">
                <svg viewBox="0 0 24 24" stroke-width="2">
                    <polygon points="19 20 9 12 19 4 19 20"></polygon>
                    <line x1="5" y1="19" x2="5" y2="5"></line>
                </svg>
            </button>
            <button class="ctrl-btn play-ctrl" id="playBtn" title="Oynat/Duraklat">
                <svg viewBox="0 0 24 24" id="playPauseIcon">
                    <rect x="6" y="4" width="4" height="16" rx="1"></rect>
                    <rect x="14" y="4" width="4" height="16" rx="1"></rect>
                </svg>
            </button>
            <button class="ctrl-btn" id="nextBtn" title="Sonraki">
                <svg viewBox="0 0 24 24" stroke-width="2">
                    <polygon points="5 4 15 12 5 20 5 4"></polygon>
                    <line x1="19" y1="5" x2="19" y2="19"></line>
                </svg>
            </button>
            <button class="ctrl-btn" id="repeatBtn" title="Tekrarla">
                <svg viewBox="0 0 24 24" stroke-width="2">
                    <polyline points="17 1 21 5 17 9"></polyline>
                    <path d="M3 11V9a4 4 0 0 1 4-4h14"></path>
                    <polyline points="7 23 3 19 7 15"></polyline>
                    <path d="M21 13v2a4 4 0 0 1-4 4H3"></path>
                </svg>
            </button>
        </div>

        <!-- Volume -->
        <div class="volume-row">
            <svg class="vol-icon" id="volIcon" viewBox="0 0 24 24" fill="none" stroke-width="2">
                <polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"></polygon>
                <path d="M19.07 4.93a10 10 0 0 1 0 14.14M15.54 8.46a5 5 0 0 1 0 7.07"></path>
            </svg>
            <div class="vol-slider-container" id="volSlider">
                <div class="vol-slider-fill" id="volFill" style="width: 75%;">
                    <div class="vol-slider-handle"></div>
                </div>
            </div>
            <span class="vol-value" id="volValue">75%</span>
        </div>

        <!-- Tabs -->
        <div class="tabs-container">
            <div class="tabs-header">
                <button class="tab-btn active" data-tab="stations">İstasyonlar</button>
                <button class="tab-btn" data-tab="equalizer">Ekolayzer</button>
                <button class="tab-btn" data-tab="effects">Efektler</button>
                <button class="tab-btn" data-tab="settings">Ayarlar</button>
            </div>

            <!-- Stations Tab -->
            <div class="tab-content active" id="tab-stations">
                <div class="stations-grid" id="stationsGrid"></div>
            </div>

            <!-- Equalizer Tab -->
            <div class="tab-content" id="tab-equalizer">
                <div class="eq-presets">
                    <button class="eq-preset-btn active" data-preset="normal">Normal</button>
                    <button class="eq-preset-btn" data-preset="pop">Pop</button>
                    <button class="eq-preset-btn" data-preset="rock">Rock</button>
                    <button class="eq-preset-btn" data-preset="jazz">Jazz</button>
                    <button class="eq-preset-btn" data-preset="classical">Klasik</button>
                    <button class="eq-preset-btn" data-preset="bass">Bass Boost</button>
                </div>
                <div class="eq-sliders" id="eqSliders"></div>
            </div>

            <!-- Effects Tab -->
            <div class="tab-content" id="tab-effects">
                <div class="effects-grid" id="effectsGrid"></div>
            </div>

            <!-- Settings Tab -->
            <div class="tab-content" id="tab-settings">
                <div class="settings-list" id="settingsList"></div>
            </div>
        </div>

        <!-- Footer -->
        <div class="widget-footer">
            <div class="listeners-count">
                <div class="listeners-avatars">
                    <div class="avatar">👨</div>
                    <div class="avatar">👩</div>
                    <div class="avatar">🧑</div>
                </div>
                <span><strong id="listenerCount">12.4K</strong> dinleyici</span>
            </div>
            <div class="quick-actions">
                <button class="quick-btn" id="sleepBtn">
                    <span>⏰</span> Uyku
                </button>
                <button class="quick-btn" id="recordBtn">
                    <span>⏺️</span> Kaydet
                </button>
                <button class="quick-btn" id="shareBtn">
                    <span>📤</span> Paylaş
                </button>
            </div>
        </div>
    </div>

    <script>
        // ========== DATA ==========
        const stations = [
            { id: 1, name: 'Power Türk', freq: 101.5, emoji: '🎵', genre: 'Pop' },
            { id: 2, name: 'Kral FM', freq: 95.3, emoji: '👑', genre: 'Arabesk' },
            { id: 3, name: 'Süper FM', freq: 98.7, emoji: '🌟', genre: 'Hits' },
            { id: 4, name: 'Metro FM', freq: 92.4, emoji: '🚗', genre: 'Pop' },
            { id: 5, name: 'Joy FM', freq: 100.8, emoji: '🎷', genre: 'Jazz' },
            { id: 6, name: 'Radyo D', freq: 94.1, emoji: '📰', genre: 'Haber' },
            { id: 7, name: 'Power FM', freq: 100.0, emoji: '⚡', genre: 'Dance' },
            { id: 8, name: 'Virgin Radio', freq: 103.2, emoji: '🎸', genre: 'Rock' },
            { id: 9, name: 'Number One', freq: 96.6, emoji: '1️⃣', genre: 'Türkçe' }
        ];

        const eqPresets = {
            normal: [50, 50, 50, 50, 50],
            pop: [40, 50, 60, 55, 45],
            rock: [60, 50, 40, 55, 60],
            jazz: [45, 55, 60, 50, 45],
            classical: [55, 50, 45, 50, 55],
            bass: [80, 70, 50, 40, 35]
        };

        const eqBands = [
            { label: '60Hz', value: 50 },
            { label: '250Hz', value: 50 },
            { label: '1kHz', value: 50 },
            { label: '4kHz', value: 50 },
            { label: '16kHz', value: 50 }
        ];

        const effects = [
            { id: 'reverb', name: 'Reverb', desc: 'Yankı efekti', icon: '🌊', active: false },
            { id: 'bass', name: 'Bass+', desc: 'Derin bas', icon: '🔊', active: false },
            { id: 'surround', name: '3D Surround', desc: 'Uzaysal ses', icon: '🌐', active: false },
            { id: 'vocal', name: 'Vocal+', desc: 'Vokal vurgusu', icon: '🎤', active: false }
        ];

        const settings = [
            { id: 'autoplay', name: 'Otomatik Başlat', icon: '▶️', active: true },
            { id: 'hd', name: 'HD Ses', icon: '🎧', active: true },
            { id: 'notify', name: 'Bildirimler', icon: '🔔', active: false },
            { id: 'dark', name: 'Karanlık Mod', icon: '🌙', active: true },
            { id: 'crossfade', name: 'Crossfade', icon: '🔀', active: false }
        ];

        // ========== STATE ==========
        let state = {
            isPlaying: true,
            currentStation: stations[0],
            volume: 75,
            progress: 35,
            shuffle: false,
            repeat: false,
            isRecording: false,
            sleepMinutes: 0,
            sleepInterval: null,
            currentPreset: 'normal'
        };

        // ========== BACKGROUND PARTICLES ==========
        function createParticles() {
            const container = document.getElementById('bgParticles');
            for (let i = 0; i < 30; i++) {
                const particle = document.createElement('div');
                particle.className = 'particle';
                const size = Math.random() * 4 + 2;
                particle.style.cssText = `
                    width: ${size}px;
                    height: ${size}px;
                    left: ${Math.random() * 100}%;
                    background: ${['#8b5cf6', '#06b6d4', '#f472b6'][Math.floor(Math.random() * 3)]};
                    animation-delay: ${Math.random() * 20}s;
                    animation-duration: ${15 + Math.random() * 15}s;
                `;
                container.appendChild(particle);
            }
        }
        createParticles();

        // ========== MAIN VISUALIZER ==========
        const mainCanvas = document.getElementById('mainVisualizer');
        const mainCtx = mainCanvas.getContext('2d');
        let mainBars = [];

        function resizeMainCanvas() {
            mainCanvas.width = mainCanvas.offsetWidth * 2;
            mainCanvas.height = mainCanvas.offsetHeight * 2;
            mainCtx.scale(2, 2);
            initMainBars();
        }

        function initMainBars() {
            mainBars = [];
            const barCount = 60;
            const barWidth = mainCanvas.offsetWidth / barCount - 1.5;
            for (let i = 0; i < barCount; i++) {
                mainBars.push({
                    x: i * (barWidth + 1.5),
                    width: barWidth,
                    height: Math.random() * 40 + 10,
                    targetHeight: Math.random() * 60 + 20,
                    hue: 260 + (i / barCount) * 60
                });
            }
        }

        function animateMainVisualizer() {
            mainCtx.clearRect(0, 0, mainCanvas.offsetWidth, mainCanvas.offsetHeight);
            
            mainBars.forEach((bar, i) => {
                if (state.isPlaying) {
                    bar.targetHeight = Math.random() * 80 + 15;
                }
                bar.height += (bar.targetHeight - bar.height) * 0.12;
                
                const gradient = mainCtx.createLinearGradient(0, 140, 0, 140 - bar.height);
                gradient.addColorStop(0, `hsla(${bar.hue}, 80%, 60%, 0.8)`);
                gradient.addColorStop(1, `hsla(${bar.hue}, 80%, 40%, 0.2)`);
                
                mainCtx.fillStyle = gradient;
                mainCtx.beginPath();
                mainCtx.roundRect(bar.x, 140 - bar.height, bar.width, bar.height, 2);
                mainCtx.fill();
            });

            requestAnimationFrame(animateMainVisualizer);
        }

        resizeMainCanvas();
        window.addEventListener('resize', resizeMainCanvas);
        animateMainVisualizer();

        // ========== WAVEFORM ==========
        const waveCanvas = document.getElementById('waveformCanvas');
        const waveCtx = waveCanvas.getContext('2d');

        function resizeWaveCanvas() {
            waveCanvas.width = waveCanvas.offsetWidth * 2;
            waveCanvas.height = waveCanvas.offsetHeight * 2;
            waveCtx.scale(2, 2);
        }

        function drawWaveform() {
            waveCtx.clearRect(0, 0, waveCanvas.offsetWidth, waveCanvas.offsetHeight);
            const centerY = waveCanvas.offsetHeight / 2;
            
            for (let x = 0; x < waveCanvas.offsetWidth; x += 3) {
                const height = Math.sin(x * 0.05 + Date.now() * 0.002) * 15 + Math.random() * 5;
                waveCtx.fillStyle = `rgba(139, 92, 246, ${0.3 + Math.random() * 0.3})`;
                waveCtx.fillRect(x, centerY - height, 2, height * 2);
            }
            
            requestAnimationFrame(drawWaveform);
        }

        resizeWaveCanvas();
        window.addEventListener('resize', resizeWaveCanvas);
        drawWaveform();

        // ========== SIGNAL METER ==========
        function updateSignal() {
            const bars = document.querySelectorAll('.signal-bar');
            const activeCount = state.isPlaying ? Math.floor(Math.random() * 2) + 3 : 1;
            bars.forEach((bar, i) => {
                bar.classList.toggle('active', i < activeCount);
            });
        }
        setInterval(updateSignal, 500);

        // ========== RENDER FUNCTIONS ==========
        function renderStations() {
            const grid = document.getElementById('stationsGrid');
            grid.innerHTML = stations.map(s => `
                <div class="station-item ${s.id === state.currentStation.id ? 'active' : ''}" data-id="${s.id}">
                    <span class="emoji">${s.emoji}</span>
                    <div class="name">${s.name}</div>
                    <div class="freq">${s.freq} MHz</div>
                </div>
            `).join('');

            grid.querySelectorAll('.station-item').forEach(item => {
                item.addEventListener('click', () => {
                    const station = stations.find(s => s.id === parseInt(item.dataset.id));
                    if (station) {
                        state.currentStation = station;
                        updateStationDisplay();
                        renderStations();
                    }
                });
            });
        }

        function updateStationDisplay() {
            document.getElementById('freqValue').textContent = state.currentStation.freq.toFixed(1);
            document.getElementById('trackArtist').textContent = state.currentStation.name;
            document.getElementById('albumArt').textContent = state.currentStation.emoji;
        }

        function renderEqualizer() {
            const container = document.getElementById('eqSliders');
            container.innerHTML = eqBands.map((band, i) => `
                <div class="eq-band">
                    <div class="eq-track" data-index="${i}">
                        <div class="eq-fill" style="height: ${band.value}%"></div>
                    </div>
                    <span class="eq-label">${band.label}</span>
                    <span class="eq-value">${band.value}%</span>
                </div>
            `).join('');

            container.querySelectorAll('.eq-track').forEach(track => {
                track.addEventListener('click', e => {
                    const rect = track.getBoundingClientRect();
                    const percent = 100 - ((e.clientY - rect.top) / rect.height * 100);
                    const index = parseInt(track.dataset.index);
                    eqBands[index].value = Math.round(Math.max(0, Math.min(100, percent)));
                    track.querySelector('.eq-fill').style.height = eqBands[index].value + '%';
                    track.closest('.eq-band').querySelector('.eq-value').textContent = eqBands[index].value + '%';
                });
            });

            // Preset buttons
            document.querySelectorAll('.eq-preset-btn').forEach(btn => {
                btn.addEventListener('click', () => {
                    const preset = btn.dataset.preset;
                    state.currentPreset = preset;
                    document.querySelectorAll('.eq-preset-btn').forEach(b => b.classList.remove('active'));
                    btn.classList.add('active');
                    
                    eqPresets[preset].forEach((val, i) => {
                        eqBands[i].value = val;
                    });
                    renderEqualizer();
                });
            });
        }

        function renderEffects() {
            const grid = document.getElementById('effectsGrid');
            grid.innerHTML = effects.map(e => `
                <div class="effect-card ${e.active ? 'active' : ''}" data-id="${e.id}">
                    <div class="effect-icon">${e.icon}</div>
                    <div class="effect-info">
                        <h4>${e.name}</h4>
                        <p>${e.desc}</p>
                    </div>
                </div>
            `).join('');

            grid.querySelectorAll('.effect-card').forEach(card => {
                card.addEventListener('click', () => {
                    const effect = effects.find(e => e.id === card.dataset.id);
                    if (effect) {
                        effect.active = !effect.active;
                        card.classList.toggle('active', effect.active);
                    }
                });
            });
        }

        function renderSettings() {
            const list = document.getElementById('settingsList');
            list.innerHTML = settings.map(s => `
                <div class="setting-row">
                    <div class="setting-label">
                        <span>${s.icon}</span>
                        ${s.name}
                    </div>
                    <div class="toggle-switch ${s.active ? 'active' : ''}" data-id="${s.id}"></div>
                </div>
            `).join('');

            list.querySelectorAll('.toggle-switch').forEach(toggle => {
                toggle.addEventListener('click', () => {
                    const setting = settings.find(s => s.id === toggle.dataset.id);
                    if (setting) {
                        setting.active = !setting.active;
                        toggle.classList.toggle('active', setting.active);
                    }
                });
            });
        }

        // ========== TABS ==========
        document.querySelectorAll('.tab-btn').forEach(btn => {
            btn.addEventListener('click', () => {
                document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
                document.querySelectorAll('.tab-content').forEach(c => c.classList.remove('active'));
                btn.classList.add('active');
                document.getElementById(`tab-${btn.dataset.tab}`).classList.add('active');
            });
        });

        // ========== CONTROLS ==========
        document.getElementById('playBtn').addEventListener('click', () => {
            state.isPlaying = !state.isPlaying;
            document.getElementById('radioWidget').classList.toggle('playing', state.isPlaying);
            
            const icon = document.getElementById('playPauseIcon');
            if (state.isPlaying) {
                icon.innerHTML = '<rect x="6" y="4" width="4" height="16" rx="1"></rect><rect x="14" y="4" width="4" height="16" rx="1"></rect>';
            } else {
                icon.innerHTML = '<polygon points="5 3 19 12 5 21 5 3"></polygon>';
            }
        });

        document.getElementById('prevBtn').addEventListener('click', () => {
            const idx = stations.findIndex(s => s.id === state.currentStation.id);
            state.currentStation = stations[(idx - 1 + stations.length) % stations.length];
            updateStationDisplay();
            renderStations();
        });

        document.getElementById('nextBtn').addEventListener('click', () => {
            const idx = stations.findIndex(s => s.id === state.currentStation.id);
            state.currentStation = stations[(idx + 1) % stations.length];
            updateStationDisplay();
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
            state.isPlaying = this.classList.contains('active');
            document.getElementById('radioWidget').classList.toggle('playing', state.isPlaying);
        });

        // ========== VOLUME ==========
        const volSlider = document.getElementById('volSlider');
        const volFill = document.getElementById('volFill');
        const volValue = document.getElementById('volValue');
        const volIcon = document.getElementById('volIcon');

        function setVolume(e) {
            const rect = volSlider.getBoundingClientRect();
            state.volume = Math.round(Math.max(0, Math.min(100, ((e.clientX - rect.left) / rect.width) * 100)));
            volFill.style.width = state.volume + '%';
            volValue.textContent = state.volume + '%';
            
            if (state.volume === 0) {
                volIcon.innerHTML = '<polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"></polygon><line x1="23" y1="9" x2="17" y2="15"></line><line x1="17" y1="9" x2="23" y2="15"></line>';
            } else if (state.volume < 50) {
                volIcon.innerHTML = '<polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"></polygon><path d="M15.54 8.46a5 5 0 0 1 0 7.07"></path>';
            } else {
                volIcon.innerHTML = '<polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"></polygon><path d="M19.07 4.93a10 10 0 0 1 0 14.14M15.54 8.46a5 5 0 0 1 0 7.07"></path>';
            }
        }

        volSlider.addEventListener('click', setVolume);
        let isDragging = false;
        volSlider.addEventListener('mousedown', () => isDragging = true);
        document.addEventListener('mousemove', e => { if (isDragging) setVolume(e); });
        document.addEventListener('mouseup', () => isDragging = false);

        volIcon.addEventListener('click', () => {
            if (state.volume > 0) {
                volFill.dataset.prev = state.volume;
                state.volume = 0;
            } else {
                state.volume = volFill.dataset.prev || 75;
            }
            volFill.style.width = state.volume + '%';
            volValue.textContent = state.volume + '%';
        });

        // ========== PROGRESS ==========
        const waveformProgress = document.getElementById('waveformProgress');
        const progressOverlay = document.getElementById('progressOverlay');

        waveformProgress.addEventListener('click', e => {
            const rect = waveformProgress.getBoundingClientRect();
            state.progress = ((e.clientX - rect.left) / rect.width) * 100;
            progressOverlay.style.width = state.progress + '%';
        });

        // Animate progress
        setInterval(() => {
            if (state.isPlaying) {
                const totalSecs = Math.floor((state.progress / 100) * 300);
                const mins = Math.floor(totalSecs / 60);
                const secs = totalSecs % 60;
                document.getElementById('currentTime').textContent = 
                    String(mins).padStart(2, '0') + ':' + String(secs).padStart(2, '0');
                
                if (state.progress < 100) state.progress += 0.03;
                progressOverlay.style.width = state.progress + '%';
            }
        }, 100);

        // ========== QUICK ACTIONS ==========
        document.getElementById('sleepBtn').addEventListener('click', () => {
            document.getElementById('sleepModal').classList.add('active');
        });

        function closeSleepModal() {
            document.getElementById('sleepModal').classList.remove('active');
        }

        document.querySelectorAll('.sleep-option').forEach(opt => {
            opt.addEventListener('click', () => {
                const mins = parseInt(opt.dataset.minutes);
                if (mins === 0) {
                    clearInterval(state.sleepInterval);
                    state.sleepMinutes = 0;
                    document.getElementById('sleepBadge').classList.remove('active');
                } else {
                    state.sleepMinutes = mins;
                    document.getElementById('sleepBadge').classList.add('active');
                    startSleepTimer();
                }
                closeSleepModal();
            });
        });

        function startSleepTimer() {
            clearInterval(state.sleepInterval);
            state.sleepInterval = setInterval(() => {
                if (state.sleepMinutes > 0) {
                    state.sleepMinutes--;
                    const m = Math.floor(state.sleepMinutes);
                    const s = (state.sleepMinutes % 1) * 60;
                    document.getElementById('sleepTimerDisplay').textContent = 
                        String(m).padStart(2, '0') + ':' + String(Math.round(s)).padStart(2, '0');
                    
                    if (state.sleepMinutes <= 0) {
                        state.isPlaying = false;
                        document.getElementById('radioWidget').classList.remove('playing');
                        document.getElementById('sleepBadge').classList.remove('active');
                        clearInterval(state.sleepInterval);
                    }
                }
            }, 60000);
        }

        document.getElementById('recordBtn').addEventListener('click', function() {
            state.isRecording = !state.isRecording;
            document.getElementById('recordingStatus').classList.toggle('active', state.isRecording);
            this.innerHTML = state.isRecording ? '<span>⏹️</span> Durdur' : '<span>⏺️</span> Kaydet';
        });

        document.getElementById('shareBtn').addEventListener('click', () => {
            alert('🔄 Paylaşım linki kopyalandı!\n\n' + state.currentStation.name + ' - ' + state.currentStation.freq + ' MHz');
        });

        // ========== LISTENER COUNT ==========
        setInterval(() => {
            const count = 12000 + Math.floor(Math.random() * 500);
            document.getElementById('listenerCount').textContent = (count / 1000).toFixed(1) + 'K';
        }, 5000);

        // ========== INIT ==========
        renderStations();
        renderEqualizer();
        renderEffects();
        renderSettings();
    </script>
</body>
</html>
```