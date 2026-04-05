<think>
The user is asking me to create a radio/music player widget in Turkish. They want:
1. A modern and sleek radio/music player widget
2. All features and functions integrated
3. Free design for the music player
4. Use canvas for visualizations
5. Add suggestions/recommendations

Let me create a comprehensive, modern radio player widget with:
- Canvas-based audio visualizer
- Play/pause, next/previous controls
- Volume control
- Progress bar
- Station selection
- Frequency display
- Modern glassmorphism design
- Animations and transitions
- Preset stations
- Sound wave visualizer

Since I can't use actual audio files or make network calls, I'll simulate the radio functionality with visual feedback and use Web Audio API concepts with simulated data.
</think>```html
<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Modern Radyo Widget</title>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&family=Orbitron:wght@400;500;700&display=swap" rel="stylesheet">
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        :root {
            --primary: #6366f1;
            --primary-dark: #4f46e5;
            --accent: #f472b6;
            --bg-dark: #0f0f1a;
            --bg-card: rgba(30, 30, 50, 0.8);
            --text: #ffffff;
            --text-muted: #a0a0b0;
            --glass: rgba(255, 255, 255, 0.05);
            --glass-border: rgba(255, 255, 255, 0.1);
        }

        body {
            font-family: 'Poppins', sans-serif;
            background: var(--bg-dark);
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 20px;
            overflow: hidden;
        }

        .background-effects {
            position: fixed;
            inset: 0;
            z-index: -1;
            overflow: hidden;
        }

        .gradient-orb {
            position: absolute;
            border-radius: 50%;
            filter: blur(80px);
            opacity: 0.5;
            animation: float 10s ease-in-out infinite;
        }

        .orb-1 {
            width: 400px;
            height: 400px;
            background: var(--primary);
            top: -100px;
            left: -100px;
            animation-delay: 0s;
        }

        .orb-2 {
            width: 300px;
            height: 300px;
            background: var(--accent);
            bottom: -50px;
            right: -50px;
            animation-delay: -3s;
        }

        .orb-3 {
            width: 200px;
            height: 200px;
            background: #10b981;
            top: 50%;
            right: 20%;
            animation-delay: -5s;
        }

        @keyframes float {
            0%, 100% { transform: translate(0, 0) scale(1); }
            33% { transform: translate(30px, -30px) scale(1.1); }
            66% { transform: translate(-20px, 20px) scale(0.9); }
        }

        .radio-container {
            width: 100%;
            max-width: 420px;
            background: var(--bg-card);
            backdrop-filter: blur(20px);
            border-radius: 24px;
            border: 1px solid var(--glass-border);
            box-shadow: 
                0 25px 50px -12px rgba(0, 0, 0, 0.5),
                inset 0 1px 0 rgba(255, 255, 255, 0.1);
            overflow: hidden;
        }

        .header {
            padding: 20px 24px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            border-bottom: 1px solid var(--glass-border);
        }

        .logo {
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .logo-icon {
            width: 40px;
            height: 40px;
            background: linear-gradient(135deg, var(--primary), var(--accent));
            border-radius: 12px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 20px;
        }

        .logo-text {
            font-family: 'Orbitron', sans-serif;
            font-weight: 700;
            font-size: 18px;
            background: linear-gradient(135deg, #fff, var(--text-muted));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }

        .power-btn {
            width: 44px;
            height: 44px;
            border-radius: 12px;
            background: var(--glass);
            border: 1px solid var(--glass-border);
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            transition: all 0.3s ease;
        }

        .power-btn:hover {
            background: rgba(255, 255, 255, 0.1);
            transform: scale(1.05);
        }

        .power-btn.active {
            background: linear-gradient(135deg, var(--primary), var(--accent));
            box-shadow: 0 0 20px rgba(99, 102, 241, 0.5);
        }

        .power-btn svg {
            width: 20px;
            height: 20px;
            stroke: var(--text);
        }

        .visualizer-section {
            padding: 20px;
            position: relative;
        }

        .visualizer-container {
            position: relative;
            height: 120px;
            background: rgba(0, 0, 0, 0.3);
            border-radius: 16px;
            overflow: hidden;
        }

        #visualizer {
            width: 100%;
            height: 100%;
        }

        .frequency-display {
            position: absolute;
            bottom: 10px;
            left: 50%;
            transform: translateX(-50%);
            font-family: 'Orbitron', sans-serif;
            font-size: 28px;
            font-weight: 700;
            color: var(--text);
            text-shadow: 0 0 20px var(--primary);
        }

        .frequency-unit {
            font-size: 14px;
            color: var(--text-muted);
            margin-left: 4px;
        }

        .station-info {
            padding: 0 20px 20px;
            text-align: center;
        }

        .station-name {
            font-size: 22px;
            font-weight: 600;
            color: var(--text);
            margin-bottom: 4px;
        }

        .station-genre {
            font-size: 13px;
            color: var(--text-muted);
            text-transform: uppercase;
            letter-spacing: 2px;
        }

        .controls {
            padding: 20px;
            display: flex;
            flex-direction: column;
            gap: 20px;
        }

        .progress-container {
            width: 100%;
        }

        .progress-bar {
            width: 100%;
            height: 6px;
            background: rgba(255, 255, 255, 0.1);
            border-radius: 3px;
            cursor: pointer;
            position: relative;
            overflow: hidden;
        }

        .progress-fill {
            height: 100%;
            background: linear-gradient(90deg, var(--primary), var(--accent));
            border-radius: 3px;
            width: 35%;
            position: relative;
            transition: width 0.1s ease;
        }

        .progress-fill::after {
            content: '';
            position: absolute;
            right: 0;
            top: 50%;
            transform: translateY(-50%);
            width: 14px;
            height: 14px;
            background: #fff;
            border-radius: 50%;
            box-shadow: 0 0 10px rgba(99, 102, 241, 0.8);
        }

        .time-display {
            display: flex;
            justify-content: space-between;
            margin-top: 8px;
            font-size: 12px;
            color: var(--text-muted);
            font-family: 'Orbitron', sans-serif;
        }

        .main-controls {
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 16px;
        }

        .control-btn {
            width: 50px;
            height: 50px;
            border-radius: 50%;
            background: var(--glass);
            border: 1px solid var(--glass-border);
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            transition: all 0.3s ease;
        }

        .control-btn:hover {
            background: rgba(255, 255, 255, 0.15);
            transform: scale(1.1);
        }

        .control-btn:active {
            transform: scale(0.95);
        }

        .control-btn svg {
            width: 22px;
            height: 22px;
            stroke: var(--text);
            fill: none;
        }

        .play-btn {
            width: 70px;
            height: 70px;
            background: linear-gradient(135deg, var(--primary), var(--accent));
            border: none;
            box-shadow: 0 10px 30px rgba(99, 102, 241, 0.4);
        }

        .play-btn:hover {
            box-shadow: 0 15px 40px rgba(99, 102, 241, 0.6);
            transform: scale(1.15);
        }

        .play-btn svg {
            width: 28px;
            height: 28px;
            stroke: #fff;
            fill: #fff;
        }

        .volume-section {
            display: flex;
            align-items: center;
            gap: 12px;
            padding: 0 20px 20px;
        }

        .volume-icon {
            width: 24px;
            height: 24px;
            stroke: var(--text-muted);
            cursor: pointer;
            transition: stroke 0.3s;
        }

        .volume-icon:hover {
            stroke: var(--text);
        }

        .volume-slider {
            flex: 1;
            height: 6px;
            background: rgba(255, 255, 255, 0.1);
            border-radius: 3px;
            position: relative;
            cursor: pointer;
        }

        .volume-fill {
            height: 100%;
            background: linear-gradient(90deg, var(--accent), var(--primary));
            border-radius: 3px;
            width: 70%;
            position: relative;
        }

        .volume-fill::after {
            content: '';
            position: absolute;
            right: -6px;
            top: 50%;
            transform: translateY(-50%);
            width: 12px;
            height: 12px;
            background: #fff;
            border-radius: 50%;
        }

        .volume-value {
            font-size: 12px;
            color: var(--text-muted);
            font-family: 'Orbitron', sans-serif;
            width: 35px;
            text-align: right;
        }

        .stations-list {
            padding: 0 20px 20px;
        }

        .section-title {
            font-size: 12px;
            color: var(--text-muted);
            text-transform: uppercase;
            letter-spacing: 2px;
            margin-bottom: 12px;
        }

        .stations-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 10px;
        }

        .station-card {
            background: var(--glass);
            border: 1px solid var(--glass-border);
            border-radius: 12px;
            padding: 12px;
            cursor: pointer;
            transition: all 0.3s ease;
            text-align: center;
        }

        .station-card:hover {
            background: rgba(255, 255, 255, 0.1);
            transform: translateY(-2px);
        }

        .station-card.active {
            background: linear-gradient(135deg, rgba(99, 102, 241, 0.3), rgba(244, 114, 182, 0.3));
            border-color: var(--primary);
        }

        .station-emoji {
            font-size: 24px;
            margin-bottom: 6px;
        }

        .station-label {
            font-size: 10px;
            color: var(--text);
            font-weight: 500;
        }

        .equalizer-section {
            padding: 0 20px 20px;
        }

        .equalizer {
            display: flex;
            justify-content: space-between;
            gap: 8px;
            margin-top: 12px;
        }

        .eq-slider {
            flex: 1;
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 6px;
        }

        .eq-bar {
            width: 100%;
            height: 60px;
            background: rgba(255, 255, 255, 0.05);
            border-radius: 4px;
            position: relative;
            cursor: pointer;
            overflow: hidden;
        }

        .eq-fill {
            position: absolute;
            bottom: 0;
            width: 100%;
            background: linear-gradient(to top, var(--primary), var(--accent));
            border-radius: 4px;
            transition: height 0.2s;
        }

        .eq-label {
            font-size: 9px;
            color: var(--text-muted);
            text-transform: uppercase;
        }

        .suggestions {
            padding: 0 20px 24px;
        }

        .suggestion-chips {
            display: flex;
            flex-wrap: wrap;
            gap: 8px;
        }

        .suggestion-chip {
            padding: 8px 14px;
            background: var(--glass);
            border: 1px solid var(--glass-border);
            border-radius: 20px;
            font-size: 12px;
            color: var(--text-muted);
            cursor: pointer;
            transition: all 0.3s ease;
        }

        .suggestion-chip:hover {
            background: rgba(99, 102, 241, 0.2);
            border-color: var(--primary);
            color: var(--text);
        }

        .footer {
            padding: 16px 20px;
            background: rgba(0, 0, 0, 0.2);
            display: flex;
            justify-content: space-around;
            border-top: 1px solid var(--glass-border);
        }

        .footer-btn {
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 4px;
            background: none;
            border: none;
            cursor: pointer;
            transition: all 0.3s;
        }

        .footer-btn svg {
            width: 22px;
            height: 22px;
            stroke: var(--text-muted);
        }

        .footer-btn span {
            font-size: 10px;
            color: var(--text-muted);
        }

        .footer-btn:hover svg,
        .footer-btn:hover span {
            stroke: var(--text);
            color: var(--text);
        }

        .footer-btn.active svg,
        .footer-btn.active span {
            stroke: var(--primary);
            color: var(--primary);
        }

        .sleep-timer {
            position: fixed;
            top: 20px;
            right: 20px;
            background: var(--bg-card);
            backdrop-filter: blur(20px);
            border: 1px solid var(--glass-border);
            border-radius: 12px;
            padding: 12px 16px;
            display: none;
            align-items: center;
            gap: 10px;
            z-index: 100;
        }

        .sleep-timer.active {
            display: flex;
        }

        .sleep-timer span {
            font-family: 'Orbitron', sans-serif;
            font-size: 14px;
            color: var(--text);
        }

        @keyframes pulse {
            0%, 100% { opacity: 1; }
            50% { opacity: 0.5; }
        }

        .recording-indicator {
            display: none;
            align-items: center;
            gap: 6px;
            color: #ef4444;
            font-size: 12px;
        }

        .recording-indicator.active {
            display: flex;
        }

        .rec-dot {
            width: 8px;
            height: 8px;
            background: #ef4444;
            border-radius: 50%;
            animation: pulse 1s ease-in-out infinite;
        }

        @media (max-width: 480px) {
            .radio-container {
                border-radius: 20px;
            }
            
            .stations-grid {
                grid-template-columns: repeat(3, 1fr);
            }
            
            .station-emoji {
                font-size: 20px;
            }
        }
    </style>
</head>
<body>
    <div class="background-effects">
        <div class="gradient-orb orb-1"></div>
        <div class="gradient-orb orb-2"></div>
        <div class="gradient-orb orb-3"></div>
    </div>

    <div class="sleep-timer" id="sleepTimer">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <circle cx="12" cy="12" r="10"></circle>
            <polyline points="12 6 12 12 16 14"></polyline>
        </svg>
        <span id="sleepTimeDisplay">00:00</span>
    </div>

    <div class="radio-container">
        <div class="header">
            <div class="logo">
                <div class="logo-icon">📻</div>
                <span class="logo-text">RadyoFM</span>
            </div>
            <div style="display: flex; align-items: center; gap: 12px;">
                <div class="recording-indicator" id="recordingIndicator">
                    <div class="rec-dot"></div>
                    <span>KAYIT</span>
                </div>
                <button class="power-btn active" id="powerBtn">
                    <svg viewBox="0 0 24 24" fill="none" stroke-width="2">
                        <path d="M18.36 6.64a9 9 0 1 1-12.73 0"></path>
                        <line x1="12" y1="2" x2="12" y2="12"></line>
                    </svg>
                </button>
            </div>
        </div>

        <div class="visualizer-section">
            <div class="visualizer-container">
                <canvas id="visualizer"></canvas>
                <div class="frequency-display">
                    <span id="frequencyValue">101.5</span>
                    <span class="frequency-unit">MHz</span>
                </div>
            </div>
        </div>

        <div class="station-info">
            <div class="station-name" id="stationName">Power Türk FM</div>
            <div class="station-genre" id="stationGenre">Pop • Türkçe</div>
        </div>

        <div class="controls">
            <div class="progress-container">
                <div class="progress-bar" id="progressBar">
                    <div class="progress-fill" id="progressFill"></div>
                </div>
                <div class="time-display">
                    <span id="currentTime">01:24</span>
                    <span id="totalTime">LIVE</span>
                </div>
            </div>

            <div class="main-controls">
                <button class="control-btn" id="shuffleBtn" title="Karıştır">
                    <svg viewBox="0 0 24 24" stroke-width="2">
                        <polyline points="16 3 21 3 21 8"></polyline>
                        <line x1="4" y1="20" x2="21" y2="3"></line>
                        <polyline points="21 16 21 21 16 21"></polyline>
                        <line x1="15" y1="15" x2="21" y2="21"></line>
                        <line x1="4" y1="4" x2="9" y2="9"></line>
                    </svg>
                </button>
                <button class="control-btn" id="prevBtn" title="Önceki">
                    <svg viewBox="0 0 24 24" stroke-width="2">
                        <polygon points="19 20 9 12 19 4 19 20"></polygon>
                        <line x1="5" y1="19" x2="5" y2="5"></line>
                    </svg>
                </button>
                <button class="control-btn play-btn" id="playBtn" title="Oynat">
                    <svg viewBox="0 0 24 24" id="playIcon">
                        <polygon points="5 3 19 12 5 21 5 3"></polygon>
                    </svg>
                </button>
                <button class="control-btn" id="nextBtn" title="Sonraki">
                    <svg viewBox="0 0 24 24" stroke-width="2">
                        <polygon points="5 4 15 12 5 20 5 4"></polygon>
                        <line x1="19" y1="5" x2="19" y2="19"></line>
                    </svg>
                </button>
                <button class="control-btn" id="repeatBtn" title="Tekrarla">
                    <svg viewBox="0 0 24 24" stroke-width="2">
                        <polyline points="17 1 21 5 17 9"></polyline>
                        <path d="M3 11V9a4 4 0 0 1 4-4h14"></path>
                        <polyline points="7 23 3 19 7 15"></polyline>
                        <path d="M21 13v2a4 4 0 0 1-4 4H3"></path>
                    </svg>
                </button>
            </div>
        </div>

        <div class="volume-section">
            <svg class="volume-icon" id="volumeIcon" viewBox="0 0 24 24" fill="none" stroke-width="2">
                <polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"></polygon>
                <path d="M19.07 4.93a10 10 0 0 1 0 14.14M15.54 8.46a5 5 0 0 1 0 7.07"></path>
            </svg>
            <div class="volume-slider" id="volumeSlider">
                <div class="volume-fill" id="volumeFill"></div>
            </div>
            <span class="volume-value" id="volumeValue">70%</span>
        </div>

        <div class="stations-list">
            <div class="section-title">Radyo İstasyonları</div>
            <div class="stations-grid" id="stationsGrid">
                <!-- Stations will be rendered here -->
            </div>
        </div>

        <div class="equalizer-section">
            <div class="section-title">Ekolayzer</div>
            <div class="equalizer" id="equalizer">
                <!-- EQ sliders will be rendered here -->
            </div>
        </div>

        <div class="suggestions">
            <div class="section-title">Öneriler</div>
            <div class="suggestion-chips" id="suggestionChips">
                <div class="suggestion-chip">🎵 Çalan Şarkıyı Bul</div>
                <div class="suggestion-chip">❤️ Favorilere Ekle</div>
                <div class="suggestion-chip">🔗 Paylaş</div>
                <div class="suggestion-chip">⏰ Uyku Zamanlayıcı</div>
                <div class="suggestion-chip">🎙️ Kaydet</div>
                <div class="suggestion-chip">📱 Bildirimler</div>
            </div>
        </div>

        <div class="footer">
            <button class="footer-btn active" id="homeBtn">
                <svg viewBox="0 0 24 24" fill="none" stroke-width="2">
                    <path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path>
                    <polyline points="9 22 9 12 15 12 15 22"></polyline>
                </svg>
                <span>Ana Sayfa</span>
            </button>
            <button class="footer-btn" id="favBtn">
                <svg viewBox="0 0 24 24" fill="none" stroke-width="2">
                    <path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path>
                </svg>
                <span>Favoriler</span>
            </button>
            <button class="footer-btn" id="recentBtn">
                <svg viewBox="0 0 24 24" fill="none" stroke-width="2">
                    <circle cx="12" cy="12" r="10"></circle>
                    <polyline points="12 6 12 12 16 14"></polyline>
                </svg>
                <span>Geçmiş</span>
            </button>
            <button class="footer-btn" id="settingsBtn">
                <svg viewBox="0 0 24 24" fill="none" stroke-width="2">
                    <circle cx="12" cy="12" r="3"></circle>
                    <path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1 0 2.83 2 2 0 0 1-2.83 0l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-2 2 2 2 0 0 1-2-2v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83 0 2 2 0 0 1 0-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1-2-2 2 2 0 0 1 2-2h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 0-2.83 2 2 0 0 1 2.83 0l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 2-2 2 2 0 0 1 2 2v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 0 2 2 0 0 1 0 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 2 2 2 2 0 0 1-2 2h-.09a1.65 1.65 0 0 0-1.51 1z"></path>
                </svg>
                <span>Ayarlar</span>
            </button>
        </div>
    </div>

    <script>
        // Station Data
        const stations = [
            { id: 1, name: 'Power Türk FM', genre: 'Pop • Türkçe', freq: 101.5, emoji: '🎵' },
            { id: 2, name: 'Kral FM', genre: 'Arabesk • Fantazi', freq: 95.3, emoji: '👑' },
            { id: 3, name: 'Süper FM', genre: 'Pop • Yabancı', freq: 98.7, emoji: '🌟' },
            { id: 4, name: 'Metro FM', genre: 'Pop • Hits', freq: 92.4, emoji: '🚗' },
            { id: 5, name: 'Joy FM', genre: 'Jazz • Lounge', freq: 100.8, emoji: '🎷' },
            { id: 6, name: 'Radyo D', genre: 'Haber • Müzik', freq: 94.1, emoji: '📰' },
            { id: 7, name: 'Power FM', genre: 'Electronic • Dance', freq: 100.0, emoji: '⚡' },
            { id: 8, name: 'Virgin Radio', genre: 'Rock • Alternative', freq: 103.2, emoji: '🎸' },
            { id: 9, name: 'Number One', genre: 'Türkçe Pop', freq: 96.6, emoji: '1️⃣' }
        ];

        const eqBands = [
            { label: '60Hz', value: 50 },
            { label: '250Hz', value: 60 },
            { label: '1kHz', value: 70 },
            { label: '4kHz', value: 65 },
            { label: '16kHz', value: 55 }
        ];

        // State
        let isPlaying = true;
        let currentStation = stations[0];
        let volume = 70;
        let sleepTimerActive = false;
        let sleepMinutes = 0;
        let isRecording = false;
        let progress = 35;

        // Canvas Visualizer
        const canvas = document.getElementById('visualizer');
        const ctx = canvas.getContext('2d');
        let animationId;

        function resizeCanvas() {
            canvas.width = canvas.offsetWidth * window.devicePixelRatio;
            canvas.height = canvas.offsetHeight * window.devicePixelRatio;
            ctx.scale(window.devicePixelRatio, window.devicePixelRatio);
        }

        resizeCanvas();
        window.addEventListener('resize', resizeCanvas);

        class Bar {
            constructor(x, width, height, color) {
                this.x = x;
                this.width = width;
                this.height = height;
                this.targetHeight = height;
                this.color = color;
            }

            update() {
                if (isPlaying) {
                    this.targetHeight = Math.random() * 80 + 10;
                }
                this.height += (this.targetHeight - this.height) * 0.1;
            }

            draw(ctx) {
                const gradient = ctx.createLinearGradient(0, 120, 0, 120 - this.height);
                gradient.addColorStop(0, this.color);
                gradient.addColorStop(1, 'rgba(99, 102, 241, 0.3)');
                
                ctx.fillStyle = gradient;
                ctx.beginPath();
                ctx.roundRect(this.x, 120 - this.height, this.width, this.height, 2);
                ctx.fill();
            }
        }

        const bars = [];
        const barCount = 50;
        const barWidth = (canvas.offsetWidth / barCount) - 2;

        for (let i = 0; i < barCount; i++) {
            const hue = (i / barCount) * 60 + 230;
            bars.push(new Bar(
                i * (barWidth + 2),
                barWidth,
                Math.random() * 60 + 20,
                `hsl(${hue}, 80%, 60%)`
            ));
        }

        function animate() {
            ctx.clearRect(0, 0, canvas.offsetWidth, canvas.offsetHeight);
            
            bars.forEach(bar => {
                bar.update();
                bar.draw(ctx);
            });

            animationId = requestAnimationFrame(animate);
        }

        animate();

        // Render Stations
        function renderStations() {
            const grid = document.getElementById('stationsGrid');
            grid.innerHTML = stations.map(station => `
                <div class="station-card ${station.id === currentStation.id ? 'active' : ''}" data-id="${station.id}">
                    <div class="station-emoji">${station.emoji}</div>
                    <div class="station-label">${station.name.split(' ')[0]}</div>
                </div>
            `).join('');

            grid.querySelectorAll('.station-card').forEach(card => {
                card.addEventListener('click', () => {
                    const station = stations.find(s => s.id === parseInt(card.dataset.id));
                    if (station) {
                        currentStation = station;
                        updateStationDisplay();
                        renderStations();
                    }
                });
            });
        }

        function updateStationDisplay() {
            document.getElementById('stationName').textContent = currentStation.name;
            document.getElementById('stationGenre').textContent = currentStation.genre;
            document.getElementById('frequencyValue').textContent = currentStation.freq.toFixed(1);
        }

        // Render Equalizer
        function renderEqualizer() {
            const eq = document.getElementById('equalizer');
            eq.innerHTML = eqBands.map((band, i) => `
                <div class="eq-slider">
                    <div class="eq-bar" data-index="${i}">
                        <div class="eq-fill" style="height: ${band.value}%"></div>
                    </div>
                    <span class="eq-label">${band.label}</span>
                </div>
            `).join('');

            eq.querySelectorAll('.eq-bar').forEach(bar => {
                bar.addEventListener('click', (e) => {
                    const rect = bar.getBoundingClientRect();
                    const percent = 100 - ((e.clientY - rect.top) / rect.height * 100);
                    const index = parseInt(bar.dataset.index);
                    eqBands[index].value = Math.max(0, Math.min(100, percent));
                    bar.querySelector('.eq-fill').style.height = eqBands[index].value + '%';
                });
            });
        }

        // Controls
        document.getElementById('playBtn').addEventListener('click', () => {
            isPlaying = !isPlaying;
            const playIcon = document.getElementById('playIcon');
            if (isPlaying) {
                playIcon.innerHTML = '<polygon points="5 3 19 12 5 21 5 3"></polygon>';
            } else {
                playIcon.innerHTML = '<rect x="6" y="4" width="4" height="16"></rect><rect x="14" y="4" width="4" height="16"></rect>';
            }
        });

        document.getElementById('prevBtn').addEventListener('click', () => {
            const currentIndex = stations.findIndex(s => s.id === currentStation.id);
            currentStation = stations[(currentIndex - 1 + stations.length) % stations.length];
            updateStationDisplay();
            renderStations();
        });

        document.getElementById('nextBtn').addEventListener('click', () => {
            const currentIndex = stations.findIndex(s => s.id === currentStation.id);
            currentStation = stations[(currentIndex + 1) % stations.length];
            updateStationDisplay();
            renderStations();
        });

        document.getElementById('powerBtn').addEventListener('click', function() {
            this.classList.toggle('active');
            isPlaying = this.classList.contains('active');
        });

        // Volume Control
        const volumeSlider = document.getElementById('volumeSlider');
        const volumeFill = document.getElementById('volumeFill');
        const volumeValue = document.getElementById('volumeValue');

        function updateVolume(e) {
            const rect = volumeSlider.getBoundingClientRect();
            volume = Math.max(0, Math.min(100, ((e.clientX - rect.left) / rect.width) * 100));
            volumeFill.style.width = volume + '%';
            volumeValue.textContent = Math.round(volume) + '%';
            
            const icon = document.getElementById('volumeIcon');
            if (volume === 0) {
                icon.innerHTML = '<polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"></polygon><line x1="23" y1="9" x2="17" y2="15"></line><line x1="17" y1="9" x2="23" y2="15"></line>';
            } else if (volume < 50) {
                icon.innerHTML = '<polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"></polygon><path d="M15.54 8.46a5 5 0 0 1 0 7.07"></path>';
            } else {
                icon.innerHTML = '<polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"></polygon><path d="M19.07 4.93a10 10 0 0 1 0 14.14M15.54 8.46a5 5 0 0 1 0 7.07"></path>';
            }
        }

        volumeSlider.addEventListener('click', updateVolume);
        volumeSlider.addEventListener('mousedown', () => {
            volumeSlider.addEventListener('mousemove', updateVolume);
        });
        document.addEventListener('mouseup', () => {
            volumeSlider.removeEventListener('mousemove', updateVolume);
        });

        document.getElementById('volumeIcon').addEventListener('click', () => {
            if (volume > 0) {
                volumeFill.dataset.prevVolume = volume;
                volume = 0;
            } else {
                volume = volumeFill.dataset.prevVolume || 70;
            }
            volumeFill.style.width = volume + '%';
            volumeValue.textContent = Math.round(volume) + '%';
        });

        // Progress Bar
        const progressBar = document.getElementById('progressBar');
        const progressFill = document.getElementById('progressFill');

        progressBar.addEventListener('click', (e) => {
            const rect = progressBar.getBoundingClientRect();
            progress = ((e.clientX - rect.left) / rect.width) * 100;
            progressFill.style.width = progress + '%';
        });

        // Progress animation
        setInterval(() => {
            if (isPlaying && progress < 100) {
                progress += 0.05;
                progressFill.style.width = progress + '%';
                
                const totalSeconds = Math.floor((progress / 100) * 300);
                const mins = Math.floor(totalSeconds / 60);
                const secs = totalSeconds % 60;
                document.getElementById('currentTime').textContent = 
                    String(mins).padStart(2, '0') + ':' + String(secs).padStart(2, '0');
            }
        }, 100);

        // Suggestions
        document.getElementById('suggestionChips').addEventListener('click', (e) => {
            const chip = e.target.closest('.suggestion-chip');
            if (!chip) return;

            if (chip.textContent.includes('Uyku')) {
                const mins = prompt('Kaç dakika sonra kapatılsın?', '30');
                if (mins && !isNaN(mins)) {
                    sleepMinutes = parseInt(mins);
                    sleepTimerActive = true;
                    document.getElementById('sleepTimer').classList.add('active');
                    startSleepTimer();
                }
            } else if (chip.textContent.includes('Kaydet')) {
                isRecording = !isRecording;
                document.getElementById('recordingIndicator').classList.toggle('active', isRecording);
                chip.textContent = isRecording ? '⏹️ Kaydı Durdur' : '🎙️ Kaydet';
            } else if (chip.textContent.includes('Favori')) {
                chip.style.background = 'rgba(239, 68, 68, 0.3)';
                chip.style.borderColor = '#ef4444';
                chip.textContent = '❤️ Favorilere Eklendi';
            }
        });

        function startSleepTimer() {
            const interval = setInterval(() => {
                if (!sleepTimerActive) {
                    clearInterval(interval);
                    return;
                }
                sleepMinutes--;
                if (sleepMinutes <= 0) {
                    sleepTimerActive = false;
                    document.getElementById('sleepTimer').classList.remove('active');
                    document.getElementById('powerBtn').classList.remove('active');
                    isPlaying = false;
                    clearInterval(interval);
                } else {
                    const mins = Math.floor(sleepMinutes);
                    const secs = (sleepMinutes % 1) * 60;
                    document.getElementById('sleepTimeDisplay').textContent = 
                        String(mins).padStart(2, '0') + ':' + String(Math.round(secs)).padStart(2, '0');
                }
            }, 1000);
        }

        // Footer navigation
        document.querySelectorAll('.footer-btn').forEach(btn => {
            btn.addEventListener('click', function() {
                document.querySelectorAll('.footer-btn').forEach(b => b.classList.remove('active'));
                this.classList.add('active');
            });
        });

        // Shuffle & Repeat
        let shuffleActive = false;
        let repeatActive = false;

        document.getElementById('shuffleBtn').addEventListener('click', function() {
            shuffleActive = !shuffleActive;
            this.style.background = shuffleActive ? 'rgba(99, 102, 241, 0.3)' : '';
        });

        document.getElementById('repeatBtn').addEventListener('click', function() {
            repeatActive = !repeatActive;
            this.style.background = repeatActive ? 'rgba(99, 102, 241, 0.3)' : '';
        });

        // Initialize
        renderStations();
        renderEqualizer();
    </script>
</body>
</html>
```