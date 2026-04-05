<think>
The user says "Let's continue to develop with new features" in Turkish. I need to enhance the existing radio player widget with additional features. The previous implementation already had:
-, Music visualization canvas
-, Station selection
-, Play/pause controls
-, Volume and progress
-, Equalizer
-, Suggestions like sleep timer and recording

Now they want more features. I can add:
-, More visualizations (spectrum analyzer, waveform)
-, Presets for equalizer
-, Playlist management
-, Song history
-, Alarm clock feature
-, Audio effects (reverb, bass boost)
-, Lyrics display (simulated)
-, Share functionality
-, Themes/dark mode toggle
-, Advanced settings
-, Station search/filter
-, Favorites system
-, Social features (like/dislike)
-, Sleep timer with fade-out
-, Crossfade between stations
-, Metadata display (song title, artist)
-, Bitrate/quality selector
-, Recording playback
-, Import/export settings
-, Keyboard shortcuts
-, Mobile gesture controls

But I must keep it within a single HTML page, all inline, no external assets, and responsive. I'll extend the existing code.

I'll enhance the visualizer with multiple modes (bars, wave, circles). Add an alarm feature. Add a playlist queue. Add lyrics panel. Add more stations. Add station search. Add favorites. Add theme toggle. Add keyboard shortcuts. Add gesture info for mobile. Add recording playback.

Since no actual network/audio, I'll simulate these with UI updates.

Plan:
1. Add visualization mode selector (bar, wave, circle)
2. Add alarm clock setup panel
3. Add playlist queue (simulated songs)
4. Add lyrics display panel
5. Add station search/filter
6. Extend favorites functionality
7. Add theme toggle (light/dark)
8. Add keyboard shortcuts guide
9. Add gesture controls guide for mobile
10. Add recording playback list
11. Add audio effects (bass boost, reverb)
12. Add preset equalizer settings
13. Add crossfade control
14. Add bitrate selector
15. Add song history list

I'll keep the same design language and make sure it's responsive.

Let's produce the updated HTML page.
</think>```html
<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Gelişmiş Radyo Widget</title>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&family=Orbitron:wght@400;500;700&display=swap" rel="stylesheet">
    <style>
        * {
            margin:身份证;
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
            --success: #10b981;
            --warning: #f59e0b;
            --danger: #ef4444;
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
            transition: background 0.3s ease;
        }

        body.light-theme {
            --primary: #4f46e5;
            --primary-dark: #4338ca;
            --accent: #db2777;
            --bg-dark: #f9fafb;
            --bg-card: rgba(255, 255, 255, 0.9);
            --text: #111827;
            --text-muted: #6b7280;
            --glass: rgba(0, 0, 0, 0.05);
            --glass-border: rgba(0, 0, 0, 0.1);
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
            background: var(--success);
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
            max-width: entrance;
            background: var(--bg-card);
            backdrop-filter: blur(20px);
            border-radius: 24px;
            border: 1px solid var(--glass-border);
            box-shadow: 
                0 25px 50px -12px rgba(0, 0, 0, 0.5),
                inset 0 1px 0 rgba(255, 255, 255, 0.1);
            overflow: hidden;
            transition: all 0.3s ease;
        }

        .light-theme .radio-container {
            box-shadow: 
                0 10px 25px -5px rgba(0, 0, 0, 0.1),
                inset 0 1px 0 rgba(255, 255, 255, 0.5);
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
            background: linear-gradient(135deg, var(--text), var(--primary));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }

        .header-controls {
            display: flex;
            align-items: center;
            gap: 10px;
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

        .light-theme .icon-btn:hover {
            background: rgba(0, 0, 0, 0.05);
        }

        .icon-btn.active {
            background: linear-gradient(135deg, var(--primary), var(--accent));
            box-shadow: 0 0 20px rgba(99, 102, 241, 0.5);
        }

        .icon-btn svg {
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

        .light-theme .visualizer-container {
            background: rgba(0, 0, 0, 0.05);
        }

        .visualizer-toolbar {
            position: absolute;
            top: 10px;
            right: 10px;
            display: flex;
            gap: 5px;
            z-index: 2;
        }

        .viz-mode-btn {
            width: 28px;
            height: 28px;
            background: rgba(0, 0, 0, 0.5);
            border-radius: BMI;
            border: none;
            color: white;
            font-size: 12px;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
        }

        .viz-mode-btn.active {
            background: var(--primary);
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

        .current-song {
            font-size: 14px;
            color: var(--text-muted);
            margin-top: 8px;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 8px;
        }

        .song-icon {
            font-size: 16px;
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

        .light-theme .progress-bar {
            background: rgba(0, 0, 0, 0.1);
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
            background: var(--text);
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

        .light-theme .control-btn:hover {
            background: rgba(0, 0, 0, 0.05);
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

        .light-theme .volume-slider {
            background: rgba(0, 0, 0, 0.1);
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
            background: var(--text);
            border-radius: 50%;
        }

        .volume-value {
            font-size: 12px;
            color: var(--text-muted);
            font-family: 'Orbitron', sans-serif;
            width: 35px;
            text-align: right;
        }

        .extra-features {
            padding: 0 20px 20px;
            display: flex;
            flex-wrap: wrap;
            gap: 12px;
        }

        .feature-chip {
            padding: 8px 16px;
            background: var(--glass);
            border: 1px solid var(--glass-border);
            border-radius: 20px;
            font-size: 12px;
            color: var(--text-muted);
            cursor: pointer;
            transition: all 0.3s ease;
            display: flex;
            align-items: center;
            gap: 6px;
        }

        .feature-chip:hover {
            background: rgba(99, 102, 241, 0.2);
            border-color: var(--primary);
            color: var(--text);
        }

        .feature-chip.active {
            background: linear-gradient(135deg, var(--primary), var(--accent));
            color: white;
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
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .search-box {
            background: var(--glass);
            border: 1px solid var(--glass-border);
            border-radius: 20px;
            padding: 6px 12px;
            font-size: 12px;
            color: var(--text);
            width: 120px;
            outline: none;
        }

        .search-box::placeholder {
            color: var(--text-muted);
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
            position: relative;
        }

        .station-card:hover {
            background: rgba(255, 255, 255, 0.1);
            transform: translateY(-2px);
        }

        .light-theme .station-card:hover {
            background: rgba(0, 0, 0, 0.05);
        }

        .station-card.active {
            background: linear-gradient(135deg, rgba(99, 102, 241, 0.3), rgba(244, 114, 182, 0.3));
            border-color: var(--primary);
        }

        .station-fav {
            position: absolute;
            top: 8px;
            right: 8px;
            width: 18px;
            height: 18px;
            background: none;
            border: none;
            color: var(--text-muted);
            font-size: 14px;
            cursor: pointer;
            transition: all 0.3s;
        }

        .station-fav.active {
            color: var(--danger);
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

        .light-theme .eq-bar {
            background: rgba(0, 0, 0, 0.05);
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

        .eq-presets {
            display: flex;
            gap: 8px;
            margin-top: 12px;
            flex-wrap: wrap;
        }

        .eq-preset-btn {
            padding: 6px 12px;
            background: var(--glass);
            border: 1px solid var(--glass-border);
            border-radius: 16px;
            font-size: 10px;
            color: var(--text-muted);
            cursor: pointer;
            transition: all 0.3s;
        }

        .eq-preset-btn:hover {
            background: rgba(99, 102, 241, 0.2);
            color: var(--text);
        }

        .eq-preset-btn.active {
            background: var(--primary);
            color: white;
        }

        .audio-effects {
            padding: 0 20px 20px;
            display: flex;
            flex-wrap: wrap;
            gap:三项;
        }

        .effect-toggle {
            padding: 8px 16px;
            background: var(--glass);
            border: 1px solid var(--glass-border);
            border-radius: 16px;
            font-size: 11px;
            color: var(--text-muted);
            cursor: pointer;
            transition: all 0.3s;
            display: flex;
            align-items: center;
            gap: 6px;
        }

        .effect-toggle.active {
            background: var(--primary);
            color: white;
        }

        .effect-toggle span {
            font-family: 'Orbitron', sans-serif;
            font-size: 10px;
        }

        .side-panels {
            display: none;
            position: fixed;
            top: 0;
            right: 0;
            width: 300px;
            height: 100%;
            background: var(--bg-card);
            backdrop-filter: blur(20px);
            border-left: 1px solid var(--glass-border);
            padding: 24px;
            overflow-y: auto;
            z-index: 10;
            transition: transform 0.3s ease;
        }

        .side-panels.active {
            display: block;
        }

        .panel-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 24px;
        }

        .panel-title {
            font-family: 'Orbitron', sans-serif;
            font-size: 18px;
            color: var(--text);
        }

        .close-panel {
            width: 32px;
            height: 32px;
            background: var(--glass);
            border: 1px solid var(--glass-border);
            border-radius: 8px;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
        }

        .song-list {
            display: flex;
            flex-direction: column;
            gap: 8px;
        }

        .song-item {
            padding: 12px;
            background: var(--glass);
            border: 1px solid var(--glass-border);
            border-radius: 12px;
            display: flex;
            align-items: center;
            gap: 12px;
            cursor: pointer;
            transition: all 0.3s;
        }

        .song-item:hover {
            background: rgba(255, 255, 255, 0.1);
        }

        .light-theme .song-item:hover {
            background: rgba(0, 0, 0, 0.05);
        }

        .song-item.active {
            background: rgba(99, 102, 241, 0.2);
            border-color: var(--primary);
        }

        .song-emoji {
            font-size: 20px;
        }

        .song-details {
            flex: 1;
        }

        .song-title {
            font-size: 14px;
            color: var(--text);
        }

        .song-artist {
            font-size: 11px;
            color: var(--text-muted);
        }

        .alarm-settings {
            display: flex;
            flex-direction: column;
            gap: 16px;
        }

        .time-picker {
            display: flex;
            align-items: center;
            gap: 8px;
            justify-content: center;
        }

        .time-input {
            width: 60px;
            padding: 8px;
            background: var(--glass);
            border: 1px solid var(--glass-border);
            border-radius: 8px;
            text-align: center;
            font-family: 'Orbitron', sans-serif;
            color: var(--text);
            outline: none;
        }

        .time-separator {
            font-size: 20px;
            color: var(--text);
        }

        .alarm-days {
            display: flex;
            justify-content: space-between;
        }

        .alarm-day {
            width: 36px;
            height: 36px;
            border-radius: 50%;
            background: var(--glass);
            border: 1px solid var(--glass-border);
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 12px;
            color: var(--text-muted);
            cursor: pointer;
        }

        .alarm-day.active {
            background: var(--primary);
            color: white;
        }

        .set-alarm-btn {
            padding: 12px;
            background: linear-gradient(135deg, var(--primary), var(--accent));
            border: none;
            border-radius: 12px;
            color: white;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s;
        }

        .set-alarm-btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 10px 20px rgba(99, 102, 241, 0.4);
        }

        .footer {
            padding: 16px 20px;
            background: rgba(0, 0, 0, 0.2);
            display: flex;
            justify-content: space-around;
            border-top: 1px solid var(--glass-border);
        }

        .light-theme .footer {
            background: rgba(0, 0, 0, 0.05);
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
            color: var(--danger);
            font-size: 12px;
        }

        .recording-indicator.active {
            display: flex;
        }

        .rec-dot {
            width: 8px;
            height: 8px;
            background: var(--danger);
            border-radius: 50%;
            animation: pulse 1s ease-in-out infinite;
        }

        .lyrics-container {
            background: rgba(0, 0, 0, 0.3);
            border-radius: 12px;
            padding: 16px;
            margin-top: 20px;
            max-height: 200px;
            overflow-y: auto;
        }

        .light-theme .lyrics-container {
            background: rgba(0, 0, 0, 0.05);
        }

        .lyric-line {
            color: var(--text-muted);
            font-size: 14px;
            margin-bottom: 8px;
            text-align: center;
        }

        .lyric-line.active {
            color: var(--text);
            font-weight: 600;
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

            .side-panels {
                width: 100%;
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

    <div class="side-panels" id="playlistPanel">
        <div class="panel-header">
            <div class="panel-title">🎵 Çalma Listesi</div>
            <button class="close-panel" data-panel="playlistPanel">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <line x1="18" y1="6" x2="6" y2="18"></line>
                    <line x1="6" y1="6" x2="18" y2="18"></line>
                </svg>
            </button>
        </div>
        <div class="song-list" id="playlistSongs">
            <!-- Playlist songs will be rendered here -->
        </div>
    </div>

    <div class="side-panels" id="alarmPanel">
        <div class="panel-header">
            <div class="panel-title">⏰ Alarm</div>
            <button class="close-panel" data-panel="alarmPanel">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <line x1="18" y1="6" x2="6" y2="18"></line>
                    <line x1="6" y1="6" x2="18" y2="18"></line>
                </svg>
            </button>
        </div>
        <div class="alarm-settings">
            <div class="time-picker">
                <input type="number" min="0" max="23" value="7" class="time-input" id="alarmHour">
                <span class="time-separator">:</span>
                <input type="number" min="0" max="59" value="30" class="time-input" id="alarmMinute">
            </div>
            <div class="alarm-days">
                <div class="alarm-day" data-day="0">P</div>
                <div class="alarm-day" data-day="1">S</div>
                <div class="alarm-day" data-day="2">Ç</div>
                <div class="alarm-day" data-day="3">P</div>
                <div class="alarm-day" data-day="4">C</div>
                <div class="alarm-day" data-day="5">C</div>
                <div class="alarm-day" data-day="6">P</div>
            </div>
            <button class="set-alarm-btn" id="setAlarmBtn">Alarmı Kur</button>
        </div>
    </div>

    <div class="side-panels" id="lyricsPanel">
        <div class="panel-header">
            <div class="panel-title">📝 Şarkı Sözleri</div>
            <button class="close-panel" data-panel="lyricsPanel">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <line x1="18" y1="6" x2="6" y2="18"></line>
                    <line x1="6" y1="6" x2="18" y2="18"></line>
                </svg>
            </button>
        </div>
        <div class="lyrics-container" id="lyricsContent">
            <!-- Lyrics will be rendered here -->
        </div>
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
                <span class="logo-text">RadyoFM Pro</span>
            </div>
            <div class="header-controls">
                <div class="recording-indicator" id="recordingIndicator">
                    <div class="rec-dot"></div>
                    <span>KAYIT</span>
                </div>
                <button class="icon-btn" id="themeToggle" title="Tema Değiştir">
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
                <button class="icon-btn active" id="powerBtn" title="Aç/Kapat">
                    <svg viewBox="0 0 24 24" fill="none" stroke-width="2">
                        <path d="M18.36 6.64a9 9 0 1 1-12.73 0"></path>
                        <line x1="12" y1="2" x2="12" y2="12"></line>
                    </svg>
                </button>
            </div>
        </div>

        <div class="visualizer-section">
            <div class="visualizer-container">
                <div class="visualizer-toolbar">
                    <button class="viz-mode-btn active" data-mode="bars">📊</button>
                    <button class="viz-mode-btn" data-mode="wave">🌊</button>
                    <button class="viz-mode-btn" data-mode="circles">⚪</button>
                </div>
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
            <div class="current-song">
                <span class="song-icon">🎵</span>
                <span id="songTitle">Sezen Aksu - Gidiyorum</span>
            </div>
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

        <div class="extra-features">
            <div class="feature-chip" id="alarmFeature">
                <span>⏰</span>
                <span>Alarm</span>
            </div>
            <div class="feature-chip" id="playlistFeature">
                <span>🎵</span>
                <span>Çalma Listesi</span>
            </div>
            <div class="feature-chip" id="lyricsFeature">
                <span>📝</span>
                <span>Sözler</span>
            </div>
            <div class="feature-chip" id="crossfadeFeature">
                <span>↔️</span>
                <span>Crossfade</span>
            </div>
            <div class="feature-chip active" id="sleepTimerFeature">
                <span>⏱️</span>
                <span>Uyku Zamanlayıcı</span>
            </div>
            <div class="feature-chip" id="recordingFeature">
                <span>🎙️</span>
                <span>Kayıt</span>
            </div>
        </div>

        <div class="stations-list">
            <div class="section-title">
                <span>Radyo İstasyonları</span>
                <input type="text" class="search-box" placeholder="Ara..." id="stationSearch">
            </div>
            <div class="stations-grid" id="stationsGrid">
                <!-- Stations will be rendered here -->
            </div>
        </div>

        <div class="equalizer-section">
            <div class="section-title">Ekolayzer</div>
            <div class="equalizer" id="equalizer">
                <!-- EQ sliders will be rendered here -->
            </div>
            <div class="eq-presets">
                <button class="eq-preset-btn" data-preset="flat">Düz</button>
                <button class="eq-preset-btn" data-preset="pop">Pop</button>
                <button class="eq-preset-btn" data-preset="rock">Rock</button>
                <button class="eq-preset-btn" data-preset="jazz">Caz</button>
                <button class="eq-preset-btn active" data-preset="bass">Bas</button>
                <button class="eq-preset-btn" data-preset="vocal">Vokal</button>
            </div>
        </div>

        <div class="audio-effects">
            <div class="effect-toggle" id="bassBoostEffect">
                <span>🎵</span>
                <span>Bas Güçlendirici</span>
                <span>+12dB</span>
            </div>
            <div class="effect-toggle" id="reverbEffect">
                <span>🏛️</span>
                <span>Yankı</span>
                <span>Orta</span>
            </div>
            <div class="effect-toggle active" id="normalizeEffect">
                <span>⚖️</span>
                <span>Normalize</span>
                <span>Açık</span>
            </div>
            <div class="effect-toggle" id="karaokeEffect">
                <span>🎤</span>
                <span>Karaoke</span>
                <span>Kapalı</span>
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
                    <path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0 -7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path>
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
                    <path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1 0 2.83 2 2 0 0 1-2.83 0l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-2 2 2 2 0 0 1-2-2v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83 0 2 2 0 0 1 0-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1-2-2 2 2 0 0 1 2-2h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-
                        1.82l-.06-.06a2 2 0 0 1 0-2.83 2 2 0 0 1 2.83 0l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 2-2 2 2 0 0 1 2 2v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 0 2 2 0 0 1 0 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 2 2 2 2 0 0 1-2 2h-.09a1.65 1.65 0 0 0-1.51 1z"></path>
                </svg>
                <span>Ayarlar</span>
            </button>
        </div>
    </div>

    <script>
        // Enhanced Station Data
        const stations = [
            { id: 1, name: 'Power Türk FM', genre: 'Pop • Türkçe', freq: 101.5, emoji: '🎵', favorite: true },
            { id: 2, name: 'Kral FM', genre: 'Arabesk • Fantazi', freq: 95.3, emoji: '👑', favorite: false },
            { id: 3, name: 'Süper FM', genre: 'Pop • Yabancı', freq: 98.7, emoji: '🌟', favorite: true },
            { id: 4, name: 'Metro FM', genre: 'Pop • Hits', freq: 92.4, emoji: '🚗', favorite: false },
            { id: 5, name: 'Joy FM', genre: 'Jazz • Lounge', freq: 100.8, emoji: '🎷', favorite: true },
            { id: 6, name: 'Radyo D', genre: 'Haber • Müzik', freq: 94.1, emoji: '📰', favorite: false },
            { id: 7, name: 'Power FM', genre: 'Electronic • Dance', freq: 100.0, emoji: '⚡', favorite: false },
            { id: 8, name: 'Virgin Radio', genre: 'Rock • Alternative', freq: 103.2, emoji: '🎸', favorite: true },
            { id: 9, name: 'Number One', genre: 'Türkçe Pop', freq: 96.6, emoji: '1️⃣', favorite: false },
            { id: 10, name: 'Best FM', genre: '80s • 90s', freq: 97.8, emoji: '✨', favorite: false },
            { id: 11, name: 'Alem FM', genre: 'Türkü • Folk', freq: 89.0, emoji: '🌹', favorite: true },
            { id: 12, name: 'Radyo Fenomen', genre: 'Rock • Metal', freq: 102.4, emoji: '🔥', favorite: false }
        ];

        const eqBands = [
            { label: '60Hz', value: 50 },
            { label: '250Hz', value: 60 },
            { label: '1kHz', value: 70 },
            { label: '4kHz', value: 65 },
            { label: '16kHz', value: 55 }
        ];

        const eqPresets = {
            flat: [50, 50, 50, 50, 50],
            pop: [55, 60, detailed, 65, 55],
            rock: [60, 65, 70, 65, 60],
            jazz: [45, 55, 70, 65, 60],
            bass: [80, 70, 50, 40, 30],
            vocal: [40, 55, 75, 70, 45]
        };

        const playlistSongs = [
            { id: 1, title: 'Gidiyorum', artist: 'Sezen Aksu', emoji: '🎤' },
            { id: 2, title: 'Beni Benimle Bırak', artist: 'Mabel Matiz', emoji: '🎸' },
            { id: 3, title: 'Rüya', artist: 'Müslüm Gürses', emoji: '🌟' },
            { id: 4, title: 'Kime Ne', artist: 'İrem Derici', emoji: '💃' },
            { id: 5, title: 'Unutulmayanlar', artist: 'MFÖ', emoji: '🎵' },
            { id: 6, title: 'Yolla', artist: 'Tarkan', emoji: '🎶' },
            { id: 7, title: 'Altüst', artist: 'Duman', emoji: '🔥' },
            { id: 8, title: 'Seni Kendime Sakladım', artist: 'Yalın', emoji: '💖' }
        ];

        const lyrics = [
            "Gidiyorum, buralardan",
            "Gözlerimde yaş, yüreğimde yara",
            "Seni unutmak ne mümkün",
            "Aşkımız bir rüya, şimdi uyanma zamanı",
            "Her gece yıldızları sayarım",
            "Belki bir gün geri dönersin",
            "Yollar uzun, yalnızlık derin",
            "Gidiyorum, buralardan..."
        ];

        // State
        let isPlaying = true;
        let currentStation = stations[0];
        let volume = 70;
        let sleepTimerActive = false;
        let sleepMinutes = 0;
        let isRecording = false;
        let progress = 35;
        let visualizationMode = 'bars';
        let isLightTheme = false;
        let crossfade = 5;
        let bassBoost = false;
        let reverb = false;
        let normalize = true;
        let karaoke = false;
        let currentSongIndex = 0;
        let favoriteStations = stations.filter(s => s.favorite);

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

        class BarVisualizer {
            constructor() {
                this.bars = [];
                this.barCount = 50;
                this.barWidth = (canvas.offsetWidth / this.barCount) - 2;
                this.init();
            }

            init() {
                for (let i = 0; i < this.barCount; i++) {
                    const hue = (i / this.barCount) * 60 + 230;
                    this.bars.push({
                        x: i * (this.barWidth + 2),
                        width: this.barWidth,
                        height: Math.random() * 60 + 20,
                        targetHeight: Math.random() * 60 + 20,
                        color: `hsl(${hue}, 80%, 60%)`
                    });
                }
            }

            update() {
                this.bars.forEach(bar => {
                    if (isPlaying) {
                        bar.targetHeight = Math.random() * 80 + 10;
                    }
                    bar.height += (bar.targetHeight - bar.height) * 0.1;
                });
            }

            draw(ctx) {
                this.bars.forEach(bar => {
                    const gradient = ctx.createLinearGradient(0, 120, 0, 120 - bar.height);
                    gradient.addColorStop(0, bar.color);
                    gradient.addColorStop(1, 'rgba(99, 102, 241, 0.3)');
                    
                    ctx.fillStyle = gradient;
                    ctx.beginPath();
                    ctx.roundRect(bar.x, 120 - bar.height, bar.width, bar.height, 2);
                    ctx.fill();
                });
            }
        }

        class WaveVisualizer {
            constructor() {
                this.points = [];
                this.pointCount = 100;
                this.init();
            }

            init() {
                for (let i = 0; i < this.pointCount; i++) {
                    this.points.push({
                        x: (i / this.pointCount) * canvas.offsetWidth,
                        y: 60 + Math.sin(i * 0.2) * 30,
                        targetY: 60 + Math.sin(i * 0.2) * 30
                    });
                }
            }

            update() {
                if (isPlaying) {
                    this.points.forEach((point, i) => {
                        point.targetY = 60 + Math.sin(i * 0.2 + Date.now() * 0.002) * 40 + Math.random() * 10;
                    });
                }
                this.points.forEach(point => {
                    point.y += (point.targetY - point.y) * 0.1;
                });
            }

            draw(ctx) {
                ctx.beginPath();
                ctx.moveTo(this.points[0].x, this.points[0].y);
                
                for (let i = 1; i < this.points.length; i++) {
                    ctx.lineTo(this.points[i].x, this.points[i].y);
                }
                
                ctx.strokeStyle = getComputedStyle(document.documentElement).getPropertyValue('--primary');
                ctx.lineWidth = 3;
                ctx.stroke();
                
                // Fill under wave
                ctx.lineTo(canvas.offsetWidth, 120);
                ctx.lineTo(0, 120);
                ctx.closePath();
                ctx.fillStyle = 'rgba(99, 102, 241, 0.2)';
                ctx.fill();
            }
        }

        class CircleVisualizer {
            constructor() {
                this.circles = [];
                this.circleCount = 15;
                this.init();
            }

            init() {
                for (let i = 0; i < this.circleCount; i++) {
                    this.circles.push({
                        x: Math.random() * canvas.offsetWidth,
                        y: Math.random() * 120,
                        radius: Math.random() * 10 + 5,
                        targetRadius: Math.random() * 10 + 5,
                        color: `hsl(${Math.random() * 60 + 200}, 80%, 60%)`
                    });
                }
            }

            update() {
                if (isPlaying) {
                    this.circles.forEach(circle => {
                        circle.targetRadius = Math.random() * 15 + 5;
                        circle.x += (Math.random() - 0.5) * 2;
                        circle.y += (Math.random() - 0.5) * 2;
                        
                        // Keep within bounds
                        circle.x = Math.max(5, Math.min(canvas.offsetWidth - 5, circle.x));
                        circle.y = Math.max(5, Math.min(115, circle.y));
                    });
                }
                this.circles.forEach(circle => {
                    circle.radius += (circle.targetRadius - circle.radius) * 0.1;
                });
            }

            draw(ctx) {
                this.circles.forEach(circle => {
                    ctx.beginPath();
                    ctx.arc(circle.x, circle.y, circle.radius, 0, Math.PI * 2);
                    ctx.fillStyle = circle.color;
                    ctx.fill();
                    
                    // Glow effect
                    ctx.beginPath();
                    ctx.arc(circle.x, circle.y, circle.radius + 3, 0, Math.PI * 2);
                    ctx.fillStyle = 'rgba(99, 102, 241, 0.3)';
                    ctx.fill();
                });
            }
        }

        let barViz = new BarVisualizer();
        let waveViz = new WaveVisualizer();
        let circleViz = new CircleVisualizer();

        function animate() {
            ctx.clearRect(0, 0, canvas.offsetWidth, canvas.offsetHeight);
            
            switch (visualizationMode) {
                case 'bars':
                    barViz.update();
                    barViz.draw(ctx);
                    break;
                case 'wave':
                    waveViz.update();
                    waveViz.draw(ctx);
                    break;
                case 'circles':
                    circleViz.update();
                    circleViz.draw(ctx);
                    break;
            }

            animationId = requestAnimationFrame(animate);
        }

        animate();

        // Visualization mode switching
        document.querySelectorAll('.viz-mode-btn').forEach(btn => {
            btn.addEventListener('click', function() {
                document.querySelectorAll('.viz-mode-btn').forEach(b => b.classList.remove('active'));
                this.classList.add('active');
                visualizationMode = this.dataset.mode;
                
                // Reinitialize visualizers
                barViz = new BarVisualizer();
                waveViz = new WaveVisualizer();
                circleViz = new CircleVisualizer();
            });
        });

        // Render Stations
        function renderStations(filter = '') {
            const grid = document.getElementById('stationsGrid');
            const filteredStations = stations.filter(station => 
                station.name.toLowerCase().includes(filter.toLowerCase()) ||
                station.genre.toLowerCase().includes(filter.toLowerCase())
            );
            
            grid.innerHTML = filteredStations.map(station => `
                <div class="station-card ${station.id === currentStation.id ? 'active' : ''}" data-id="${station.id}">
                    <button class="station-fav ${station.favorite ? 'active' : ''}" data-id="${station.id}">${station.favorite ? '❤️' : '🤍'}</button>
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
                        renderStations(document.getElementById('stationSearch').value);
                    }
                });
            });

            grid.querySelectorAll('.station-fav').forEach(btn => {
                btn.addEventListener('click', function(e) {
                    e.stopPropagation();
                    const station = stations.find(s => s.id === parseInt(this.dataset.id));
                    if (station) {
                        station.favorite = !station.favorite;
                        this.classList.toggle('active');
                        this.textContent = station.favorite ? '❤️' : '🤍';
                        favoriteStations = stations.filter(s => s.favorite);
                    }
                });
            });
        }

        function updateStationDisplay() {
            document.getElementById('stationName').textContent = currentStation.name;
            document.getElementById('stationGenre').textContent = currentStation.genre;
            document.getElementById('frequencyValue').textContent = currentStation.freq.toFixed(1);
            
            // Update current song
            const song = playlistSongs[currentSongIndex];
            document.getElementById('songTitle').textContent = `${song.artist} - ${song.title}`;
        }

        // Station search
        document.getElementById('stationSearch').addEventListener('input', function() {
            renderStations(this.value);
        });

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

        // EQ Presets
        document.querySelectorAll('.eq-preset-btn').forEach(btn => {
            btn.addEventListener('click', function() {
                document.querySelectorAll('.eq-preset-btn').forEach(b => b.classList.remove('active'));
                this.classList.add('active');
                
                const preset = eqPresets[this.dataset.preset];
                eqBands.forEach((band, i) => {
                    band.value = preset[i];
                });
                renderEqualizer();
            });
        });

        // Render Playlist
        function renderPlaylist() {
            const list = document.getElementById('playlistSongs');
            list.innerHTML = playlistSongs.map((song, i) => `
                <div class="song-item ${i === currentSongIndex ? 'active' : ''}" data-index="${i}">
                    <div class="song-emoji">${song.emoji}</div>
                    <div class="song-details">
                        <div class="song-title">${song.title}</div>
                        <div class="song-artist">${song.artist}</div>
                    </div>
                </div>
            `).join('');

            list.querySelectorAll('.song-item').forEach(item => {
                item.addEventListener('click', function() {
                    currentSongIndex = parseInt(this.dataset.index);
                    renderPlaylist();
                    updateStationDisplay();
                });
            });
        }

        // Render Lyrics
        function renderLyrics() {
            const container = document.getElementById('lyricsContent');
            container.innerHTML = lyrics.map((line, i) => `
                <div class="lyric-line ${i === 2 ? 'active' : ''}">${line}</div>
            `).join('');
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
            currentSongIndex = (currentSongIndex - 1 + playlistSongs.length) % playlistSongs.length;
            updateStationDisplay();
            renderPlaylist();
        });

        document.getElementById('nextBtn').addEventListener('click', () => {
            currentSongIndex = (currentSongIndex + 1) % playlistSongs.length;
            updateStationDisplay();
            renderPlaylist();
        });

        document.getElementById('powerBtn').addEventListener('click', function() {
            this.classList.toggle('active');
            isPlaying = this.classList.contains('active');
        });

        // Theme Toggle
        document.getElementById('themeToggle').addEventListener('click', function() {
            isLightTheme = !isLightTheme;
            document.body.classList.toggle('light-theme', isLightTheme);
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

        // Feature panels
        document.querySelectorAll('.feature-chip').forEach(chip => {
            chip.addEventListener('click', function() {
                const id = this.id;
                
                if (id === 'alarmFeature') {
                    document.getElementById('alarmPanel').classList.add('active');
                } else if (id === 'playlistFeature') {
                    document.getElementById('playlistPanel').classList.add('active');
                } else if (id === 'lyricsFeature') {
                    document.getElementById('lyricsPanel').classList.add('active');
                } else if (id === 'sleepTimerFeature') {
                    const mins = prompt('Kaç dakika sonra kapatılsın?', '30');
                    if (mins && !isNaN(mins)) {
                        sleepMinutes = parseInt(mins);
                        sleepTimerActive = true;
                        document.getElementById('sleepTimer').classList.add('active');
                        startSleepTimer();
                    }
                } else if (id === 'recordingFeature') {
                    isRecording = !isRecording;
                    document.getElementById('recordingIndicator').classList.toggle('active', isRecording);
                    this.textContent = isRecording ? '🎙️ Kayıt Duruyor' : '🎙️ Kayıt';
                }
            });
        });

        // Close panels
        document.querySelectorAll('.close-panel').forEach(btn => {
            btn.addEventListener('click', function() {
                const panelId = this.dataset.panel;
                document.getElementById(panelId).classList.remove('active');
            });
        });

        // Alarm
        document.querySelectorAll('.alarm-day').forEach(day => {
            day.addEventListener('click', function() {
                this.classList.toggle('active');
            });
        });

        document.getElementById('setAlarmBtn').addEventListener('click', function() {
            const hour = document.getElementById('alarmHour').value.padStart(2, '0');
            const minute = document.getElementById('alarmMinute').value.padStart(2, '0');
            alert(`Alarm ${hour}:${minute} saatine kuruldu!`);
            document.getElementById('alarmPanel').classList.remove('active');
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

        // Audio Effects
        document.querySelectorAll('.effect-toggle').forEach(effect => {
            effect.addEventListener('click', function() {
                this.classList.toggle('active');
                
                const id = this.id;
                if (id === 'bassBoostEffect') {
                    bassBoost = !bassBoost;
                    this.querySelector('span:last-child').textContent = bassBoost ? '+12dB' : '0dB';
                } else if (id === 'reverbEffect') {
                    reverb = !reverb;
                    this.querySelector('span:last-child').textContent = reverb ? 'Açık' : 'Kapalı';
                } else if (id === 'normalizeEffect') {
                    normalize = !normalize;
                    this.querySelector('span:last-child').textContent = normalize ? 'Açık' : 'Kapalı';
                } else if (id === 'karaokeEffect') {
                    karaoke = !karaoke;
                    this.querySelector('span:last-child').textContent = karaoke ? 'Açık' : 'Kapalı';
                }
            });
        });

        // Footer navigation
        document.querySelectorAll('.footer-btn').forEach(btn => {
            btn.addEventListener('click', function() {
                document.querySelectorAll('.footer-btn').forEach(b => b.classList.remove('active'));
                this.classList.add('active');
                
                const id = this.id;
                if (id === 'favBtn') {
                    const favStations = stations.filter(s => s.favorite);
                    if (favStations.length > 0) {
                        currentStation = favStations[0];
                        updateStationDisplay();
                        renderStations();
                    }
                }
            });
        });

        // Shuffle & Repeat
        let shuffleActive = false;
        let repeatActive = false;

        document.getElementById('shuffleBtn').addEventListener('click', function() {
            shuffleActive = !shuffleActive;
            this.style.background = shuffleActive ? 'rgba(99, 102, 241, 0.3)' : '';
            if (shuffleActive) {
                // Shuffle playlist
                for (let i = playlistSongs.length - 1; i > 0; i--) {
                    const j = Math.floor(Math.random() * (i + 1));
                    [playlistSongs[i], playlistSongs[j]] = [playlistSongs[j], playlistSongs[i]];
                }
                renderPlaylist();
            }
        });

        document.getElementById('repeatBtn').addEventListener('click', function() {
            repeatActive = !repeatActive;
            this.style.background = repeatActive ? 'rgba(99, 102, 241, 0.3)' : '';
        });

        // Keyboard shortcuts
        document.addEventListener('keydown', (e) => {
            switch(e.key) {
                case ' ':
                    e.preventDefault();
                    document.getElementById('playBtn').click();
                    break;
                case 'ArrowLeft':
                    document.getElementById('prevBtn').click();
                    break;
                case 'ArrowRight':
                    document.getElementById('nextBtn').click();
                    break;
                case '+':
                case '=':
                    volume = Math.min(100, volume + 5);
                    volumeFill.style.width = volume + '%';
                    volumeValue.textContent = Math.round(volume) + '%';
                    break;
                case '-':
                    volume = Math.max(0, volume - 5);
                    volumeFill.style.width = volume + '%';
                    volumeValue.textContent = Math.round(volume) + '%';
                    break;
                case 'm':
                    document.getElementById('volumeIcon').click();
                    break;
            }
        });

        // Initialize
        renderStations();
        renderEqualizer();
        renderPlaylist();
        renderLyrics();
    </script>
</body>
</html>
```