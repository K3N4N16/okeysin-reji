<think>
 Kullanıcı, modern ve gelişmiş bir radyo widget'ı istiyor. İstekler:

1. **Modern ve gelişmiş tasarım** - Canvas kullanımı, modern UI
2. **Tüm özellikler ve fonksiyonlar** - Play/Pause, Ses kontrolü, İstasyon değiştirme, Favoriler, vb.
3. **Entegre yapı** - Her şey tek bir HTML dosyasında
4. **Özgür müzik player tasarımı** - Yaratıcı, özgür bir tasarım
5. **Canvas kullanımı** - Görsel efektler, animasyonlar, visualizer
6. **Öneriler** - İstasyon önerileri, kategoriler
7. **Responsive** - İframe içinde çalışacak, genişleyebilir/daralabilir

Tasarım stratejisi:
- Glassmorphism (cam efekti) modern UI
- Canvas ile audio visualizer (ses dalgaları)
- Emoji kullanımı (harici assetler yasak)
- Gradient arka planlar, animasyonlar
- Çoklu radyo istasyonları (mock data)
- Favoriler sistemi (session based, localStorage yasak değil mi? Kontrol et... Evet, sandboxed iframe ve localStorage yasak)
- Playlist/History
- Arama özelliği
- Kategoriler (Pop, Rock, Jazz, vb.)
- Sleep timer
- Ses seviyesi kontrolü
- Bilgi ekranı (şarkı adı, sanatçı)

Teknik detaylar:
- Vanilla JS, HTML, CSS (inline)
- Canvas API for audio visualization
- Web Audio API (simulated since we can't load real audio in sandbox easily, but I'll create a visual simulation that looks like it's analyzing audio)
- Responsive CSS Grid/Flexbox
- CSS animations and transitions
- Mock data for radio stations

Özellikler listesi:
1. **Playback Controls**: Play/Pause, Stop, Next/Previous station
2. **Volume Control**: Slider with mute toggle
3. **Visualizer**: Canvas-based audio visualization bars/waves
4. **Station List**: Scrollable list with categories
5. **Favorites**: Add/remove favorites (memory-only due to restrictions)
6. **Search**: Search stations by name/genre
7. **Sleep Timer**: Auto-stop after X minutes
8. **Now Playing**: Display current track info (simulated)
9. **Categories**: Filter by genre
10. **Responsive**: Fluid layout

Canvas kullanımı:
- Audio frequency visualizer (bars or circular)
- Animated background particles or waves
- Equalizer effect

Kod yapısı:
- HTML: Container, canvas, controls, lists
- CSS: Modern styling, glassmorphism, animations, responsive queries
- JS: 
  - RadioStation class/data
  - AudioVisualizer class (canvas)
  - Player controller
  - UI interactions
  - State management

Örnek istasyonlar (mock):
- 🎵 Pop FM
- 🎸 Rock Station
- 🎷 Jazz Lounge
- 🎹 Classical Radio
- 🎧 Electronic Beats
- 📻 Talk Radio

Özellikler detaylı:
- **Canvas Visualizer**: Animate bars based on simulated frequency data (since we can't access real audio data easily in a static HTML without external files, I'll create a simulation that looks real)
- **Modern UI**: Dark theme with neon accents, glass cards
- **Entegre**: Everything self-contained in one HTML file

Önemli not: Kullanıcı "sandboxed iframe" ve "no localStorage" dediği için, veriler sadece memory'de tutulacak, sayfa yenilendiğinde kaybolacak. Ama bu normal, widget mantığında çalışacak.

Tasarım detayları:
- Ortada büyük canvas visualizer
- Altta playback kontrolleri
- Sol tarafta istasyon listesi
- Sağ tarafta now playing ve favorites
- Responsive: Mobilde alt alta dizilecek

Hadi kodu yazalım.
</think> ```html
<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Modern Radyo Widget</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        :root {
            --primary: #6366f1;
            --secondary: #ec4899;
            --accent: #06b6d4;
            --dark: #0f172a;
            --glass: rgba(255, 255, 255, 0.05);
            --border: rgba(255, 255, 255, 0.1);
            --text: #e2e8f0;
            --text-muted: #94a3b8;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 50%, #312e81 100%);
            color: var(--text);
            height: 100vh;
            overflow: hidden;
            display: flex;
            justify-content: center;
            align-items: center;
        }

        .radio-container {
            width: 95%;
            max-width: 1200px;
            height: 90vh;
            background: linear-gradient(145deg, rgba(30, 41, 59, 0.9), rgba(15, 23, 42, 0.95));
            border-radius: 24px;
            box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5);
            border: 1px solid var(--border);
            display: grid;
            grid-template-columns: 300px 1fr 300px;
            grid-template-rows: 1fr auto;
            overflow: hidden;
            position: relative;
        }

        .radio-container::before {
            content: '';
            position: absolute;
            top: -50%;
            left: -50%;
            width: 200%;
            height: 200%;
            background: radial-gradient(circle, rgba(99, 102, 241, 0.1) 0%, transparent 70%);
            pointer-events: none;
            animation: rotate 20s linear infinite;
        }

        @keyframes rotate {
            from { transform: rotate(0deg); }
            to { transform: rotate(360deg); }
        }

        /* Sidebar - Stations */
        .sidebar {
            background: var(--glass);
            border-right: 1px solid var(--border);
            display: flex;
            flex-direction: column;
            backdrop-filter: blur(10px);
            z-index: 10;
        }

        .sidebar-header {
            padding: 20px;
            border-bottom: 1px solid var(--border);
        }

        .search-box {
            position: relative;
            margin-top: 12px;
        }

        .search-box input {
            width: 100%;
            padding: 10px 35px 10px 15px;
            background: rgba(15, 23, 42, 0.5);
            border: 1px solid var(--border);
            border-radius: 12px;
            color: var(--text);
            font-size: 14px;
            outline: none;
            transition: all 0.3s;
        }

        .search-box input:focus {
            border-color: var(--primary);
            box-shadow: 0 0 0 3px rgba(99, 102, 241, 0.1);
        }

        .search-box::after {
            content: '🔍';
            position: absolute;
            right: 12px;
            top: 50%;
            transform: translateY(-50%);
            opacity: 0.5;
        }

        .categories {
            padding: 15px 20px;
            display: flex;
            gap: 8px;
            flex-wrap: wrap;
            border-bottom: 1px solid var(--border);
        }

        .category-btn {
            padding: 6px 12px;
            background: rgba(99, 102, 241, 0.1);
            border: 1px solid rgba(99, 102, 241, 0.3);
            border-radius: 20px;
            color: var(--text);
            font-size: 12px;
            cursor: pointer;
            transition: all 0.3s;
            white-space: nowrap;
        }

        .category-btn:hover, .category-btn.active {
            background: var(--primary);
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(99, 102, 241, 0.3);
        }

        .stations-list {
            flex: 1;
            overflow-y: auto;
            padding: 10px;
        }

        .stations-list::-webkit-scrollbar {
            width: 6px;
        }

        .stations-list::-webkit-scrollbar-track {
            background: transparent;
        }

        .stations-list::-webkit-scrollbar-thumb {
            background: var(--border);
            border-radius: 3px;
        }

        .station-item {
            padding: 15px;
            margin-bottom: 8px;
            background: rgba(255, 255, 255, 0.03);
            border: 1px solid var(--border);
            border-radius: 12px;
            cursor: pointer;
            transition: all 0.3s;
            display: flex;
            align-items: center;
            gap: 12px;
            position: relative;
            overflow: hidden;
        }

        .station-item::before {
            content: '';
            position: absolute;
            left: 0;
            top: 0;
            height: 100%;
            width: 3px;
            background: linear-gradient(to bottom, var(--primary), var(--secondary));
            opacity: 0;
            transition: opacity 0.3s;
        }

        .station-item:hover {
            background: rgba(255, 255, 255, 0.08);
            transform: translateX(5px);
        }

        .station-item.active {
            background: rgba(99, 102, 241, 0.15);
            border-color: rgba(99, 102, 241, 0.5);
        }

        .station-item.active::before {
            opacity: 1;
        }

        .station-icon {
            width: 40px;
            height: 40px;
            border-radius: 10px;
            background: linear-gradient(135deg, var(--primary), var(--secondary));
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 20px;
            flex-shrink: 0;
        }

        .station-info {
            flex: 1;
            min-width: 0;
        }

        .station-name {
            font-weight: 600;
            font-size: 14px;
            margin-bottom: 4px;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
        }

        .station-genre {
            font-size: 12px;
            color: var(--text-muted);
        }

        .favorite-btn {
            background: none;
            border: none;
            cursor: pointer;
            font-size: 18px;
            opacity: 0.5;
            transition: all 0.3s;
            padding: 5px;
        }

        .favorite-btn:hover, .favorite-btn.active {
            opacity: 1;
            transform: scale(1.2);
        }

        .favorite-btn.active {
            filter: drop-shadow(0 0 8px rgba(236, 72, 153, 0.5));
        }

        /* Main Player */
        .main-player {
            display: flex;
            flex-direction: column;
            position: relative;
            overflow: hidden;
            z-index: 10;
        }

        .visualizer-container {
            flex: 1;
            position: relative;
            display: flex;
            justify-content: center;
            align-items: center;
            background: radial-gradient(circle at center, rgba(99, 102, 241, 0.05) 0%, transparent 70%);
        }

        #visualizer {
            width: 100%;
            height: 100%;
        }

        .now-playing-overlay {
            position: absolute;
            text-align: center;
            pointer-events: none;
            z-index: 20;
        }

        .track-art {
            width: 180px;
            height: 180px;
            margin: 0 auto 20px;
            border-radius: 50%;
            background: linear-gradient(135deg, var(--primary), var(--secondary), var(--accent));
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 80px;
            box-shadow: 0 20px 60px rgba(99, 102, 241, 0.4);
            position: relative;
            animation: pulse 4s ease-in-out infinite;
        }

        @keyframes pulse {
            0%, 100% { transform: scale(1); box-shadow: 0 20px 60px rgba(99, 102, 241, 0.4); }
            50% { transform: scale(1.05); box-shadow: 0 30px 80px rgba(236, 72, 153, 0.5); }
        }

        .track-art::before {
            content: '';
            position: absolute;
            inset: 10px;
            border-radius: 50%;
            border: 2px solid rgba(255, 255, 255, 0.3);
            animation: spin 10s linear infinite;
        }

        @keyframes spin {
            from { transform: rotate(0deg); }
            to { transform: rotate(360deg); }
        }

        .track-name {
            font-size: 24px;
            font-weight: 700;
            margin-bottom: 8px;
            background: linear-gradient(to right, var(--text), var(--primary));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }

        .artist-name {
            font-size: 16px;
            color: var(--text-muted);
            margin-bottom: 5px;
        }

        .station-badge {
            display: inline-block;
            padding: 5px 15px;
            background: rgba(99, 102, 241, 0.2);
            border: 1px solid rgba(99, 102, 241, 0.4);
            border-radius: 20px;
            font-size: 12px;
            color: var(--primary);
        }

        /* Controls */
        .controls-section {
            padding: 30px;
            background: linear-gradient(to top, rgba(15, 23, 42, 0.95), transparent);
            border-top: 1px solid var(--border);
        }

        .progress-container {
            margin-bottom: 25px;
        }

        .progress-bar {
            width: 100%;
            height: 6px;
            background: rgba(255, 255, 255, 0.1);
            border-radius: 3px;
            overflow: hidden;
            cursor: pointer;
            position: relative;
        }

        .progress-fill {
            height: 100%;
            background: linear-gradient(90deg, var(--primary), var(--secondary));
            width: 35%;
            position: relative;
            transition: width 0.3s;
        }

        .progress-fill::after {
            content: '';
            position: absolute;
            right: -6px;
            top: 50%;
            transform: translateY(-50%);
            width: 12px;
            height: 12px;
            background: white;
            border-radius: 50%;
            box-shadow: 0 0 10px rgba(99, 102, 241, 0.5);
            opacity: 0;
            transition: opacity 0.3s;
        }

        .progress-bar:hover .progress-fill::after {
            opacity: 1;
        }

        .time-display {
            display: flex;
            justify-content: space-between;
            font-size: 12px;
            color: var(--text-muted);
            margin-top: 8px;
        }

        .main-controls {
            display: flex;
            justify-content: center;
            align-items: center;
            gap: 20px;
            margin-bottom: 25px;
        }

        .control-btn {
            background: none;
            border: none;
            color: var(--text);
            cursor: pointer;
            transition: all 0.3s;
            display: flex;
            align-items: center;
            justify-content: center;
        }

        .control-btn:hover {
            transform: scale(1.1);
            color: var(--primary);
        }

        .control-btn.small {
            font-size: 20px;
            width: 40px;
            height: 40px;
            border-radius: 50%;
            background: rgba(255, 255, 255, 0.05);
        }

        .control-btn.large {
            font-size: 28px;
            width: 70px;
            height: 70px;
            border-radius: 50%;
            background: linear-gradient(135deg, var(--primary), var(--secondary));
            box-shadow: 0 10px 30px rgba(99, 102, 241, 0.4);
        }

        .control-btn.large:hover {
            transform: scale(1.05);
            box-shadow: 0 15px 40px rgba(236, 72, 153, 0.5);
        }

        .secondary-controls {
            display: flex;
            justify-content: center;
            align-items: center;
            gap: 30px;
        }

        .volume-control {
            display: flex;
            align-items: center;
            gap: 10px;
            flex: 1;
            max-width: 200px;
        }

        .volume-slider {
            flex: 1;
            height: 4px;
            background: rgba(255, 255, 255, 0.1);
            border-radius: 2px;
            cursor: pointer;
            position: relative;
        }

        .volume-fill {
            height: 100%;
            background: var(--accent);
            border-radius: 2px;
            width: 70%;
        }

        .extra-controls {
            display: flex;
            gap: 15px;
        }

        .icon-btn {
            background: none;
            border: none;
            color: var(--text-muted);
            cursor: pointer;
            font-size: 18px;
            transition: all 0.3s;
            position: relative;
        }

        .icon-btn:hover {
            color: var(--text);
            transform: translateY(-2px);
        }

        .icon-btn.active {
            color: var(--secondary);
        }

        /* Right Panel */
        .right-panel {
            background: var(--glass);
            border-left: 1px solid var(--border);
            display: flex;
            flex-direction: column;
            backdrop-filter: blur(10px);
            z-index: 10;
        }

        .panel-section {
            padding: 20px;
            border-bottom: 1px solid var(--border);
        }

        .section-title {
            font-size: 14px;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 1px;
            color: var(--text-muted);
            margin-bottom: 15px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .favorites-list, .history-list {
            display: flex;
            flex-direction: column;
            gap: 10px;
        }

        .mini-item {
            display: flex;
            align-items: center;
            gap: 10px;
            padding: 10px;
            background: rgba(255, 255, 255, 0.03);
            border-radius: 8px;
            cursor: pointer;
            transition: all 0.3s;
            font-size: 13px;
        }

        .mini-item:hover {
            background: rgba(255, 255, 255, 0.08);
            transform: translateX(5px);
        }

        .mini-icon {
            width: 32px;
            height: 32px;
            border-radius: 8px;
            background: linear-gradient(135deg, var(--primary), var(--secondary));
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 14px;
        }

        .mini-info {
            flex: 1;
        }

        .mini-name {
            font-weight: 500;
            margin-bottom: 2px;
        }

        .mini-meta {
            font-size: 11px;
            color: var(--text-muted);
        }

        /* Sleep Timer */
        .timer-section {
            margin-top: auto;
            border-top: 1px solid var(--border);
        }

        .timer-display {
            display: flex;
            justify-content: space-around;
            margin-bottom: 15px;
        }

        .timer-option {
            padding: 5px 10px;
            background: rgba(6, 182, 212, 0.1);
            border: 1px solid rgba(6, 182, 212, 0.3);
            border-radius: 15px;
            font-size: 12px;
            cursor: pointer;
            transition: all 0.3s;
        }

        .timer-option:hover, .timer-option.active {
            background: var(--accent);
            color: var(--dark);
        }

        /* Responsive */
        @media (max-width: 1024px) {
            .radio-container {
                grid-template-columns: 250px 1fr;
                grid-template-rows: auto 1fr auto;
            }
            
            .right-panel {
                display: none;
            }
        }

        @media (max-width: 768px) {
            .radio-container {
                grid-template-columns: 1fr;
                grid-template-rows: auto 1fr auto;
                height: 100vh;
                width: 100%;
                border-radius: 0;
            }
            
            .sidebar {
                max-height: 30vh;
                border-right: none;
                border-bottom: 1px solid var(--border);
            }
            
            .track-art {
                width: 120px;
                height: 120px;
                font-size: 50px;
            }
            
            .track-name {
                font-size: 18px;
            }
        }

        /* Notification */
        .notification {
            position: fixed;
            top: 20px;
            right: 20px;
            background: var(--glass);
            border: 1px solid var(--border);
            backdrop-filter: blur(10px);
            padding: 15px 20px;
            border-radius: 12px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.3);
            transform: translateX(400px);
            transition: transform 0.3s;
            z-index: 1000;
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .notification.show {
            transform: translateX(0);
        }

        /* Loading Animation */
        .loading {
            display: inline-block;
            width: 20px;
            height: 20px;
            border: 3px solid rgba(255,255,255,.3);
            border-radius: 50%;
            border-top-color: white;
            animation: spin 1s ease-in-out infinite;
        }
    </style>
</head>
<body>
    <div class="radio-container">
        <!-- Sol Panel - İstasyonlar -->
        <aside class="sidebar">
            <div class="sidebar-header">
                <h2>📻 Radyo Aktif</h2>
                <div class="search-box">
                    <input type="text" id="searchInput" placeholder="İstasyon ara...">
                </div>
            </div>
            
            <div class="categories">
                <button class="category-btn active" data-category="all">Tümü</button>
                <button class="category-btn" data-category="pop">Pop</button>
                <button class="category-btn" data-category="rock">Rock</button>
                <button class="category-btn" data-category="jazz">Jazz</button>
                <button class="category-btn" data-category="electronic">Electronic</button>
                <button class="category-btn" data-category="classical">Klasik</button>
            </div>
            
            <div class="stations-list" id="stationsList">
                <!-- İstasyonlar JS ile doldurulacak -->
            </div>
        </aside>

        <!-- Ana Panel - Player -->
        <main class="main-player">
            <div class="visualizer-container">
                <canvas id="visualizer"></canvas>
                <div class="now-playing-overlay">
                    <div class="track-art" id="trackArt">🎵</div>
                    <div class="track-name" id="trackName">Radyo Dinlemeyi Başlat</div>
                    <div class="artist-name" id="artistName">Bir istasyon seçin</div>
                    <div class="station-badge" id="stationBadge">Hazır</div>
                </div>
            </div>

            <div class="controls-section">
                <div class="progress-container">
                    <div class="progress-bar" id="progressBar">
                        <div class="progress-fill" id="progressFill"></div>
                    </div>
                    <div class="time-display">
                        <span id="currentTime">00:00</span>
                        <span id="totalTime">00:00</span>
                    </div>
                </div>

                <div class="main-controls">
                    <button class="control-btn small" id="prevBtn" title="Önceki">⏮</button>
                    <button class="control-btn large" id="playBtn" title="Oynat/Duraklat">▶</button>
                    <button class="control-btn small" id="nextBtn" title="Sonraki">⏭</button>
                </div>

                <div class="secondary-controls">
                    <div class="volume-control">
                        <button class="icon-btn" id="muteBtn">🔊</button>
                        <div class="volume-slider" id="volumeSlider">
                            <div class="volume-fill" id="volumeFill"></div>
                        </div>
                    </div>
                    
                    <div class="extra-controls">
                        <button class="icon-btn" id="shuffleBtn" title="Karıştır">🔀</button>
                        <button class="icon-btn" id="repeatBtn" title="Tekrarla">🔁</button>
                        <button class="icon-btn" id="sleepBtn" title="Zamanlayıcı">⏰</button>
                        <button class="icon-btn" id="lyricsBtn" title="Şarkı Sözleri">📃</button>
                    </div>
                </div>
            </div>
        </main>

        <!-- Sağ Panel - Favoriler ve Geçmiş -->
        <aside class="right-panel">
            <div class="panel-section">
                <div class="section-title">
                    <span>❤️ Favoriler</span>
                    <span id="favCount">0</span>
                </div>
                <div class="favorites-list" id="favoritesList">
                    <div class="mini-item" style="opacity: 0.5; pointer-events: none;">
                        Henüz favori yok
                    </div>
                </div>
            </div>

            <div class="panel-section">
                <div class="section-title">
                    <span>🕐 Son Dinlenenler</span>
                    <button class="icon-btn" style="font-size: 12px;" onclick="clearHistory()">🗑</button>
                </div>
                <div class="history-list" id="historyList">
                    <!-- Geçmiş JS ile doldurulacak -->
                </div>
            </div>

            <div class="panel-section timer-section">
                <div class="section-title">
                    <span>⏲️ Uyku Zamanlayıcı</span>
                    <span id="timerDisplay" style="font-size: 12px; color: var(--accent);">Kapalı</span>
                </div>
                <div class="timer-display">
                    <button class="timer-option" data-time="15">15dk</button>
                    <button class="timer-option" data-time="30">30dk</button>
                    <button class="timer-option" data-time="60">60dk</button>
                    <button class="timer-option active" data-time="0">Kapalı</button>
                </div>
            </div>
        </aside>
    </div>

    <!-- Bildirim -->
    <div class="notification" id="notification">
        <span id="notifIcon">🔔</span>
        <span id="notifText">Bildirim</span>
    </div>

    <script>
        // Veri Modelleri
        const stations = [
            { id: 1, name: "Pop FM 104.2", genre: "pop", icon: "🎵", color: "#ec4899", desc: "Hit Müzik" },
            { id: 2, name: "Rock Station", genre: "rock", icon: "🎸", color: "#ef4444", desc: "Kaya Gibi" },
            { id: 3, name: "Jazz Lounge", genre: "jazz", icon: "🎷", color: "#f59e0b", desc: "Rahatlatıcı" },
            { id: 4, name: "Electronic Beats", genre: "electronic", icon: "🎧", color: "#06b6d4", desc: "Dance & House" },
            { id: 5, name: "Classical Radio", genre: "classical", icon: "🎹", color: "#8b5cf6", desc: "Klasikler" },
            { id: 6, name: "Hip Hop Zone", genre: "hiphop", icon: "🎤", color: "#6366f1", desc: "Rap & HipHop" },
            { id: 7, name: "Chill Out", genre: "chill", icon: "🌊", color: "#10b981", desc: "Dinlenme" },
            { id: 8, name: "Metal Head", genre: "rock", icon: "🤘", color: "#dc2626", desc: "Ağır Metal" },
            { id: 9, name: "Blues Club", genre: "jazz", icon: "🎺", color: "#3b82f6", desc: "Mavi Notalar" },
            { id: 10, name: "Techno Night", genre: "electronic", icon: "🌃", color: "#a855f7", desc: "Gece Modu" },
            { id: 11, name: "Acoustic Sessions", genre: "pop", icon: "🎸", color: "#f97316", desc: "Akustik" },
            { id: 12, name: "World Music", genre: "world", icon: "🌍", color: "#84cc16", desc: "Evrensel" }
        ];

        // State
        let currentStation = null;
        let isPlaying = false;
        let favorites = new Set();
        let history = [];
        let currentCategory = 'all';
        let volume = 70;
        let isMuted = false;
        let sleepTimer = null;
        let timerInterval = null;
        let visualizerAnimation = null;
        let shuffleMode = false;
        let repeatMode = false;
        let progress = 0;
        let progressInterval = null;

        // Canvas Visualizer
        class AudioVisualizer {
            constructor(canvas) {
                this.canvas = canvas;
                this.ctx = canvas.getContext('2d');
                this.bars = 60;
                this.dataArray = new Array(this.bars).fill(0);
                this.resize();
                window.addEventListener('resize', () => this.resize());
            }

            resize() {
                this.canvas.width = this.canvas.offsetWidth;
                this.canvas.height = this.canvas.offsetHeight;
            }

            generateData() {
                for (let i = 0; i < this.bars; i++) {
                    const target = Math.random() * (isPlaying ? 200 : 20);
                    this.dataArray[i] += (target - this.dataArray[i]) * 0.1;
                }
            }

            draw() {
                this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);
                
                const barWidth = this.canvas.width / this.bars;
                const centerY = this.canvas.height / 2;

                // Dalga efekti
                this.ctx.beginPath();
                this.ctx.moveTo(0, centerY);
                
                for (let i = 0; i < this.bars; i++) {
                    const x = i * barWidth;
                    const height = this.dataArray[i];
                    const y = centerY - height / 2;
                    
                    // Gradient bar
                    const gradient = this.ctx.createLinearGradient(0, y, 0, y + height);
                    gradient.addColorStop(0, '#6366f1');
                    gradient.addColorStop(0.5, '#ec4899');
                    gradient.addColorStop(1, '#06b6d4');
                    
                    this.ctx.fillStyle = gradient;
                    this.ctx.globalAlpha = 0.6;
                    this.ctx.fillRect(x + 1, y, barWidth - 2, height);
                    
                    // Parlama efekti
                    if (height > 100) {
                        this.ctx.shadowBlur = 20;
                        this.ctx.shadowColor = '#ec4899';
                    }
                }
                
                this.ctx.shadowBlur = 0;
                this.ctx.globalAlpha = 1;
                
                // Orta daire
                if (isPlaying) {
                    this.ctx.beginPath();
                    this.ctx.arc(this.canvas.width / 2, this.canvas.height / 2, 80 + Math.sin(Date.now() / 200) * 5, 0, Math.PI * 2);
                    this.ctx.strokeStyle = 'rgba(99, 102, 241, 0.3)';
                    this.ctx.lineWidth = 2;
                    this.ctx.stroke();
                }

                this.generateData();
                visualizerAnimation = requestAnimationFrame(() => this.draw());
            }

            start() {
                if (!visualizerAnimation) this.draw();
            }

            stop() {
                cancelAnimationFrame(visualizerAnimation);
                visualizerAnimation = null;
            }
        }

        // Uygulama Mantığı
        const visualizer = new AudioVisualizer(document.getElementById('visualizer'));
        visualizer.start();

        function renderStations() {
            const list = document.getElementById('stationsList');
            const filtered = currentCategory === 'all' 
                ? stations 
                : stations.filter(s => s.genre === currentCategory);
            
            const searchTerm = document.getElementById('searchInput').value.toLowerCase();
            const finalList = filtered.filter(s => s.name.toLowerCase().includes(searchTerm));
            
            list.innerHTML = finalList.map(station => `
                <div class="station-item ${currentStation?.id === station.id ? 'active' : ''}" 
                     data-id="${station.id}" onclick="playStation(${station.id})">
                    <div class="station-icon" style="background: ${station.color}">${station.icon}</div>
                    <div class="station-info">
                        <div class="station-name">${station.name}</div>
                        <div class="station-genre">${station.desc}</div>
                    </div>
                    <button class="favorite-btn ${favorites.has(station.id) ? 'active' : ''}" 
                            onclick="toggleFavorite(event, ${station.id})">
                        ${favorites.has(station.id) ? '💖' : '🤍'}
                    </button>
                </div>
            `).join('');
        }

        function playStation(id) {
            const station = stations.find(s => s.id === id);
            if (!station) return;
            
            currentStation = station;
            isPlaying = true;
            
            // UI Güncelle
            document.getElementById('trackArt').textContent = station.icon;
            document.getElementById('trackName').textContent = getRandomTrack();
            document.getElementById('artistName').textContent = getRandomArtist();
            document.getElementById('stationBadge').textContent = station.name;
            document.getElementById('playBtn').textContent = '⏸';
            
            // Progress sıfırla
            progress = 0;
            updateProgress();
            
            // Geçmiş ekle
            addToHistory(station);
            
            // Listeyi güncelle
            renderStations();
            
            // Bildirim
            showNotification('▶️ Oynatılıyor', `${station.name} - ${station.desc}`);
        }

        function getRandomTrack() {
            const tracks = [
                "Summer Vibes", "Midnight Dreams", "Electric Soul", "Golden Hour",
                "Neon Lights", "Ocean Drive", "Mountain High", "City Lights",
                "Retro Wave", "Future Nostalgia", "Cosmic Love", "Urban Rhythm"
            ];
            return tracks[Math.floor(Math.random() * tracks.length)];
        }

        function getRandomArtist() {
            const artists = [
                "The Weeknd", "Dua Lipa", "Arctic Monkeys", "Daft Punk",
                "Coldplay", "Imagine Dragons", "Tame Impala", "The xx",
                "Bonobo", "Fred again..", "Calvin Harris", "Disclosure"
            ];
            return artists[Math.floor(Math.random() * artists.length)];
        }

        function togglePlay() {
            if (!currentStation) {
                playStation(1);
                return;
            }
            isPlaying = !isPlaying;
            document.getElementById('playBtn').textContent = isPlaying ? '⏸' : '▶';
            showNotification(isPlaying ? '▶️ Devam Ediyor' : '⏸ Duraklatıldı', currentStation.name);
        }

        function nextStation() {
            if (!currentStation) {
                playStation(1);
                return;
            }
            const currentIdx = stations.findIndex(s => s.id === currentStation.id);
            const nextIdx = (currentIdx + 1) % stations.length;
            playStation(stations[nextIdx].id);
        }

        function prevStation() {
            if (!currentStation) return;
            const currentIdx = stations.findIndex(s => s.id === currentStation.id);
            const prevIdx = (currentIdx - 1 + stations.length) % stations.length;
            playStation(stations[prevIdx].id);
        }

        function toggleFavorite(event, id) {
            event.stopPropagation();
            if (favorites.has(id)) {
                favorites.delete(id);
            } else {
                favorites.add(id);
                showNotification('💖 Favorilere Eklendi', stations.find(s => s.id === id).name);
            }
            renderStations();
            renderFavorites();
        }

        function renderFavorites() {
            const list = document.getElementById('favoritesList');
            const favs = stations.filter(s => favorites.has(s.id));
            
            document.getElementById('favCount').textContent = favs.length;
            
            if (favs.length === 0) {
                list.innerHTML = '<div class="mini-item" style="opacity: 0.5;">Henüz favori yok</div>';
                return;
            }
            
            list.innerHTML = favs.map(station => `
                <div class="mini-item" onclick="playStation(${station.id})">
                    <div class="mini-icon" style="background: ${station.color}">${station.icon}</div>
                    <div class="mini-info">
                        <div class="mini-name">${station.name}</div>
                        <div class="mini-meta">${station.desc}</div>
                    </div>
                    <button class="icon-btn" onclick="event.stopPropagation(); toggleFavorite(event, ${station.id})">🗑</button>
                </div>
            `).join('');
        }

        function addToHistory(station) {
            history = history.filter(s => s.id !== station.id);
            history.unshift(station);
            if (history.length > 5) history.pop();
            renderHistory();
        }

        function renderHistory() {
            const list = document.getElementById('historyList');
            if (history.length === 0) {
                list.innerHTML = '<div class="mini-item" style="opacity: 0.5;">Henüz geçmiş yok</div>';
                return;
            }
            
            list.innerHTML = history.map(station => `
                <div class="mini-item" onclick="playStation(${station.id})">
                    <div class="mini-icon" style="background: ${station.color}">${station.icon}</div>
                    <div class="mini-info">
                        <div class="mini-name">${station.name}</div>
                        <div class="mini-meta">Son dinlenen</div>
                    </div>
                </div>
            `).join('');
        }

        function clearHistory() {
            history = [];
            renderHistory();
            showNotification('🗑️ Geçmiş Temizlendi');
        }

        function updateProgress() {
            if (progressInterval) clearInterval(progressInterval);
            if (!isPlaying) return;
            
            progressInterval = setInterval(() => {
                if (!isPlaying) return;
                progress += 0.1;
                if (progress > 100) {
                    progress = 0;
                    if (repeatMode) {
                        // Tekrar çal
                    } else if (shuffleMode) {
                        const randomId = Math.floor(Math.random() * stations.length) + 1;
                        playStation(randomId);
                    } else {
                        nextStation();
                    }
                }
                
                document.getElementById('progressFill').style.width = progress + '%';
                document.getElementById('currentTime').textContent = formatTime(progress * 2.4);
                document.getElementById('totalTime').textContent = '04:00';
            }, 100);
        }

        function formatTime(seconds) {
            const mins = Math.floor(seconds / 60);
            const secs = Math.floor(seconds % 60);
            return `${mins.toString().padStart(2, '0')}:${secs.toString().padStart(2, '0')}`;
        }

        function setVolume(val) {
            volume = Math.max(0, Math.min(100, val));
            document.getElementById('volumeFill').style.width = volume + '%';
            updateMuteIcon();
        }

        function updateMuteIcon() {
            const btn = document.getElementById('muteBtn');
            if (volume === 0 || isMuted) {
                btn.textContent = '🔇';
            } else if (volume < 50) {
                btn.textContent = '🔉';
            } else {
                btn.textContent = '🔊';
            }
        }

        function toggleMute() {
            isMuted = !isMuted;
            updateMuteIcon();
            showNotification(isMuted ? '🔇 Sessiz' : '🔊 Ses Açık', `Ses: ${volume}%`);
        }

        function showNotification(title, text = '') {
            const notif = document.getElementById('notification');
            document.getElementById('notifIcon').textContent = title.split(' ')[0];
            document.getElementById('notifText').textContent = title.replace(/^\S+\s/, '') + (text ? ` - ${text}` : '');
            notif.classList.add('show');
            setTimeout(() => notif.classList.remove('show'), 3000);
        }

        // Event Listeners
        document.getElementById('playBtn').addEventListener('click', togglePlay);
        document.getElementById('nextBtn').addEventListener('click', nextStation);
        document.getElementById('prevBtn').addEventListener('click', prevStation);
        
        document.getElementById('muteBtn').addEventListener('click', toggleMute);
        
        document.getElementById('volumeSlider').addEventListener('click', (e) => {
            const rect = e.currentTarget.getBoundingClientRect();
            const percent = ((e.clientX - rect.left) / rect.width) * 100;
            setVolume(percent);
        });

        document.getElementById('progressBar').addEventListener('click', (e) => {
            const rect = e.currentTarget.getBoundingClientRect();
            progress = ((e.clientX - rect.left) / rect.width) * 100;
            document.getElementById('progressFill').style.width = progress + '%';
        });

        document.getElementById('searchInput').addEventListener('input', renderStations);

        document.querySelectorAll('.category-btn').forEach(btn => {
            btn.addEventListener('click', (e) => {
                document.querySelectorAll('.category-btn').forEach(b => b.classList.remove('active'));
                e.target.classList.add('active');
                currentCategory = e.target.dataset.category;
                renderStations();
            });
        });

        document.getElementById('shuffleBtn').addEventListener('click', function() {
            shuffleMode = !shuffleMode;
            this.classList.toggle('active');
            showNotification(shuffleMode ? '🔀 Karıştırma Açık' : '🔀 Karıştırma Kapalı');
        });

        document.getElementById('repeatBtn').addEventListener('click', function() {
            repeatMode = !repeatMode;
            this.classList.toggle('active');
            showNotification(repeatMode ? '🔁 Tekrarlama Açık' : '🔁 Tekrarlama Kapalı');
        });

        document.getElementById('sleepBtn').addEventListener('click', function() {
            document.querySelector('.timer-section').scrollIntoView({ behavior: 'smooth' });
            showNotification('⏰ Zamanlayıcı Ayarları');
        });

        document.getElementById('lyricsBtn').addEventListener('click', function() {
            if (!currentStation) {
                showNotification('⚠️ Önce bir istasyon seçin');
                return;
            }
            showNotification('📝 Şarkı Sözleri', 'Bu özellik demo versiyonda mevcut değil');
        });

        document.querySelectorAll('.timer-option').forEach(btn => {
            btn.addEventListener('click', function() {
                document.querySelectorAll('.timer-option').forEach(b => b.classList.remove('active'));
                this.classList.add('active');
                
                const minutes = parseInt(this.dataset.time);
                if (minutes > 0) {
                    startSleepTimer(minutes);
                } else {
                    clearSleepTimer();
                }
            });
        });

        function startSleepTimer(minutes) {
            clearInterval(timerInterval);
            let seconds = minutes * 60;
            
            document.getElementById('timerDisplay').textContent = `${minutes}dk`;
            
            timerInterval = setInterval(() => {
                seconds--;
                const mins = Math.floor(seconds / 60);
                document.getElementById('timerDisplay').textContent = `${mins}dk`;
                
                if (seconds <= 0) {
                    isPlaying = false;
                    document.getElementById('playBtn').textContent = '▶';
                    clearInterval(timerInterval);
                    showNotification('😴 Zamanlayıcı', 'Radyo durduruldu');
                    document.getElementById('timerDisplay').textContent = 'Kapalı';
                }
            }, 1000);
            
            showNotification('⏲️ Zamanlayıcı Ayarlandı', `${minutes} dakika sonra duracak`);
        }

        function clearSleepTimer() {
            clearInterval(timerInterval);
            document.getElementById('timerDisplay').textContent = 'Kapalı';
            showNotification('⏲️ Zamanlayıcı Kapalı');
        }

        // Başlangıç
        renderStations();
        renderFavorites();
        renderHistory();
        setVolume(70);

        // Demo: Otomatik ilk istasyonu seç
        setTimeout(() => {
            document.querySelector('.station-item')?.click();
        }, 500);
    </script>
</body>
</html>
```