<think>
 The user wants me to continue developing the webpage further, making it "ultra professional" with more features and integrations. They want me to be free with suggestions and integrate all necessary features.

Looking at the current state, I have:
1. Nebula background with floating effects
2. Particle system
3. Interactive dashboard with cards
4. Music player with controls
5. Creative studio with color picker
6. Mood generator
7. Gradient slider
8. Stats dashboard
9. AI assistant
10. Interactive footer

To make it ULTRA professional and more advanced, I should add:

1. **Window/Modal System** - Draggable, resizable windows like an OS
2. **Terminal/Console** - A working command line interface
3. **File Explorer** - Visual file system
4. **3D Elements** - CSS 3D transforms for depth
5. **Advanced Visualizations** - Audio visualizer canvas, animated charts
6. **Multi-screen Support** - Split screen functionality
7. **Real-time Clock/Calendar** - Digital and analog clock
8. **Notification System** - Toast notifications
9. **Context Menu** - Right-click menu
10. **Keyboard Shortcuts** - Hotkeys
11. **Weather Widget** - Simulated weather
12. **Task Manager** - Showing "processes"
13. **Calculator** - Functional calculator
14. **Notes/Sticky Notes** - Draggable notes
15. **Matrix Rain Effect** - Background option
16. **Glitch Effects** - Cyberpunk aesthetics
17. **Loading/Splash Screen** - Initial boot sequence
18. **Settings Panel** - Comprehensive settings
19. **Minimap/Navigator** - Overview of sections
20. **Scroll-triggered Animations** - Intersection Observer

I'll create an "Operating System" like interface that is ultra-professional, with:
- Boot sequence
- Desktop environment with icons
- Multiple draggable windows
- Functional terminal
- Real calculator
- Sticky notes
- Advanced music visualizer using Canvas API
- System tray with time, weather, notifications
- Right-click context menu
- Keyboard shortcuts (Ctrl+T for terminal, etc.)
- Matrix rain background toggle
- Glitch text effects
- Parallax layers

This will be a single-page application that behaves like a futuristic OS.

Structure:
1. Boot screen with loading animation
2. Desktop with:
   - Wallpaper (animated gradient)
   - Desktop icons (Music, Terminal, Settings, Browser, Calculator, Notes)
   - Taskbar (Start menu, open apps, system tray with clock)
   - Context menu (right click on desktop)
3. Draggable windows:
   - Terminal (functional commands)
   - Music Player (with canvas visualizer)
   - File Explorer
   - Settings
   - Calculator
   - Notepad
4. Background effects:
   - Matrix rain option
   - Particle network (connecting lines)
   - Nebula clouds
5. Notifications system
6. Keyboard shortcuts overlay

I'll implement all of this with vanilla JS, no external dependencies, fully responsive, and visually stunning with glassmorphism, neon effects, and smooth animations.

Key technical implementations:
- Drag and drop API for windows
- Canvas API for audio visualizer and matrix rain
- CSS 3D transforms
- Intersection Observer for scroll animations
- Custom event system for notifications
- State management for the "OS"
- Command parser for terminal
- Calculator logic
- Local storage simulation (using variables since localStorage is blocked, but I'll simulate persistence within the session)

This will be a comprehensive, ultra-professional web experience.
</think> ```html
<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>NEBULA OS | Ultra Professional Dashboard</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=JetBrains+Mono:wght@400;700&display=swap');
        
        :root {
            --neon-pink: #ff00ff;
            --neon-cyan: #00ffff;
            --neon-green: #00ff88;
            --neon-purple: #aa00ff;
            --neon-orange: #ff8800;
            --bg-dark: #0a0a0f;
            --bg-card: rgba(20, 20, 30, 0.6);
            --glass: rgba(255, 255, 255, 0.03);
            --border: rgba(255, 255, 255, 0.1);
            --shadow: 0 8px 32px rgba(0, 0, 0, 0.4);
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            user-select: none;
        }

        body {
            font-family: 'Inter', sans-serif;
            background: var(--bg-dark);
            color: #fff;
            overflow: hidden;
            height: 100vh;
            width: 100vw;
        }

        /* Boot Sequence */
        #boot-screen {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: #000;
            z-index: 10000;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            font-family: 'JetBrains Mono', monospace;
        }

        .boot-text {
            color: var(--neon-cyan);
            font-size: 14px;
            max-width: 600px;
            width: 90%;
        }

        .boot-line {
            margin: 4px 0;
            opacity: 0;
            animation: fadeIn 0.1s forwards;
        }

        @keyframes fadeIn {
            to { opacity: 1; }
        }

        .boot-progress {
            width: 300px;
            height: 2px;
            background: rgba(255,255,255,0.1);
            margin-top: 30px;
            position: relative;
            overflow: hidden;
        }

        .boot-progress-bar {
            height: 100%;
            background: var(--neon-cyan);
            width: 0%;
            animation: bootProgress 3s ease-out forwards;
            box-shadow: 0 0 10px var(--neon-cyan);
        }

        @keyframes bootProgress {
            to { width: 100%; }
        }

        /* Desktop Environment */
        #desktop {
            width: 100%;
            height: 100vh;
            position: relative;
            background: radial-gradient(ellipse at center, #1a1a2e 0%, #0a0a0f 100%);
            overflow: hidden;
        }

        /* Animated Wallpaper */
        .wallpaper {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            z-index: 0;
        }

        .nebula-layer {
            position: absolute;
            border-radius: 50%;
            filter: blur(80px);
            opacity: 0.4;
            animation: nebulaFloat 30s infinite ease-in-out;
        }

        @keyframes nebulaFloat {
            0%, 100% { transform: translate(0, 0) scale(1); }
            25% { transform: translate(50px, -30px) scale(1.1); }
            50% { transform: translate(-30px, 50px) scale(0.9); }
            75% { transform: translate(30px, 30px) scale(1.05); }
        }

        /* Matrix Rain Canvas */
        #matrix-canvas {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            z-index: 1;
            opacity: 0;
            transition: opacity 1s;
        }

        /* Particle Network */
        #particle-canvas {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            z-index: 1;
        }

        /* Desktop Icons */
        .desktop-icons {
            position: absolute;
            top: 20px;
            left: 20px;
            z-index: 10;
            display: grid;
            grid-template-columns: 80px;
            gap: 20px;
        }

        .desktop-icon {
            display: flex;
            flex-direction: column;
            align-items: center;
            cursor: pointer;
            padding: 10px;
            border-radius: 12px;
            transition: all 0.3s;
            width: 80px;
        }

        .desktop-icon:hover {
            background: rgba(255,255,255,0.1);
            transform: translateY(-2px);
        }

        .desktop-icon.selected {
            background: rgba(0,255,255,0.2);
            border: 1px solid var(--neon-cyan);
        }

        .icon-emoji {
            font-size: 32px;
            margin-bottom: 5px;
            filter: drop-shadow(0 0 10px currentColor);
        }

        .icon-label {
            font-size: 11px;
            color: rgba(255,255,255,0.9);
            text-align: center;
            text-shadow: 0 1px 2px rgba(0,0,0,0.8);
        }

        /* Windows System */
        .window {
            position: absolute;
            background: var(--bg-card);
            backdrop-filter: blur(20px);
            border: 1px solid var(--border);
            border-radius: 16px;
            box-shadow: var(--shadow), 0 0 0 1px rgba(255,255,255,0.05);
            min-width: 300px;
            min-height: 200px;
            z-index: 100;
            overflow: hidden;
            resize: both;
            animation: windowOpen 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        }

        @keyframes windowOpen {
            from { transform: scale(0.8); opacity: 0; }
            to { transform: scale(1); opacity: 1; }
        }

        .window.minimized {
            display: none;
        }

        .window-header {
            background: rgba(0,0,0,0.3);
            padding: 12px 16px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            cursor: move;
            border-bottom: 1px solid var(--border);
        }

        .window-title {
            font-size: 13px;
            font-weight: 600;
            display: flex;
            align-items: center;
            gap: 8px;
        }

        .window-controls {
            display: flex;
            gap: 8px;
        }

        .window-btn {
            width: 12px;
            height: 12px;
            border-radius: 50%;
            border: none;
            cursor: pointer;
            transition: transform 0.2s;
        }

        .window-btn:hover {
            transform: scale(1.2);
        }

        .btn-close { background: #ff5f57; }
        .btn-minimize { background: #febc2e; }
        .btn-maximize { background: #28c840; }

        .window-content {
            padding: 20px;
            height: calc(100% - 45px);
            overflow: auto;
            position: relative;
        }

        /* Taskbar */
        #taskbar {
            position: fixed;
            bottom: 0;
            left: 0;
            right: 0;
            height: 50px;
            background: rgba(10, 10, 15, 0.8);
            backdrop-filter: blur(20px);
            border-top: 1px solid var(--border);
            z-index: 1000;
            display: flex;
            align-items: center;
            padding: 0 20px;
            gap: 15px;
        }

        .start-btn {
            width: 40px;
            height: 40px;
            border-radius: 10px;
            background: linear-gradient(135deg, var(--neon-pink), var(--neon-purple));
            border: none;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 20px;
            transition: transform 0.2s;
            box-shadow: 0 0 20px rgba(255,0,255,0.3);
        }

        .start-btn:hover {
            transform: scale(1.1);
        }

        .taskbar-apps {
            display: flex;
            gap: 10px;
            flex: 1;
        }

        .taskbar-item {
            padding: 8px 16px;
            background: rgba(255,255,255,0.05);
            border-radius: 8px;
            cursor: pointer;
            font-size: 13px;
            display: flex;
            align-items: center;
            gap: 8px;
            transition: all 0.3s;
            border: 1px solid transparent;
        }

        .taskbar-item:hover {
            background: rgba(255,255,255,0.1);
        }

        .taskbar-item.active {
            background: rgba(0,255,255,0.1);
            border-color: var(--neon-cyan);
            box-shadow: 0 0 10px rgba(0,255,255,0.2);
        }

        .system-tray {
            display: flex;
            align-items: center;
            gap: 15px;
            padding: 0 15px;
            border-left: 1px solid var(--border);
        }

        .tray-icon {
            cursor: pointer;
            font-size: 16px;
            transition: transform 0.2s;
        }

        .tray-icon:hover {
            transform: scale(1.2);
        }

        .clock {
            font-family: 'JetBrains Mono', monospace;
            font-size: 13px;
            color: rgba(255,255,255,0.9);
            text-align: right;
        }

        /* Terminal Styles */
        .terminal {
            background: #0c0c0c;
            font-family: 'JetBrains Mono', monospace;
            color: #00ff00;
            height: 100%;
            overflow-y: auto;
            padding: 10px;
            font-size: 13px;
            line-height: 1.5;
        }

        .terminal-line {
            margin: 4px 0;
        }

        .terminal-input-line {
            display: flex;
            align-items: center;
            gap: 8px;
        }

        .terminal-prompt {
            color: var(--neon-cyan);
        }

        .terminal-input {
            background: transparent;
            border: none;
            color: #fff;
            font-family: inherit;
            font-size: inherit;
            flex: 1;
            outline: none;
        }

        /* Music Visualizer */
        .visualizer-container {
            background: #000;
            border-radius: 12px;
            padding: 20px;
            margin-bottom: 20px;
        }

        #visualizer-canvas {
            width: 100%;
            height: 150px;
            background: radial-gradient(circle at center, #1a1a2e 0%, #000 100%);
            border-radius: 8px;
        }

        /* Calculator */
        .calculator {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 10px;
            max-width: 300px;
        }

        .calc-display {
            grid-column: span 4;
            background: rgba(0,0,0,0.5);
            padding: 20px;
            text-align: right;
            font-size: 24px;
            border-radius: 8px;
            margin-bottom: 10px;
            font-family: 'JetBrains Mono', monospace;
            border: 1px solid var(--border);
        }

        .calc-btn {
            padding: 20px;
            border: none;
            background: rgba(255,255,255,0.05);
            color: white;
            border-radius: 8px;
            cursor: pointer;
            font-size: 18px;
            transition: all 0.2s;
        }

        .calc-btn:hover {
            background: rgba(255,255,255,0.1);
            transform: translateY(-2px);
        }

        .calc-btn.operator {
            background: rgba(255,0,255,0.2);
            color: var(--neon-pink);
        }

        .calc-btn.equals {
            background: var(--neon-green);
            color: #000;
            grid-column: span 2;
        }

        /* File Explorer */
        .file-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(100px, 1fr));
            gap: 15px;
        }

        .file-item {
            display: flex;
            flex-direction: column;
            align-items: center;
            padding: 15px;
            border-radius: 10px;
            cursor: pointer;
            transition: all 0.2s;
        }

        .file-item:hover {
            background: rgba(255,255,255,0.05);
        }

        .file-icon {
            font-size: 40px;
            margin-bottom: 8px;
        }

        .file-name {
            font-size: 12px;
            text-align: center;
            color: rgba(255,255,255,0.8);
        }

        /* Context Menu */
        #context-menu {
            position: absolute;
            background: rgba(20, 20, 30, 0.95);
            backdrop-filter: blur(20px);
            border: 1px solid var(--border);
            border-radius: 8px;
            padding: 8px 0;
            z-index: 10000;
            display: none;
            min-width: 180px;
            box-shadow: 0 10px 40px rgba(0,0,0,0.5);
        }

        .context-item {
            padding: 10px 20px;
            cursor: pointer;
            font-size: 13px;
            display: flex;
            align-items: center;
            gap: 10px;
            transition: background 0.2s;
        }

        .context-item:hover {
            background: rgba(255,255,255,0.1);
        }

        .context-divider {
            height: 1px;
            background: var(--border);
            margin: 8px 0;
        }

        /* Notification System */
        #notification-area {
            position: fixed;
            top: 20px;
            right: 20px;
            z-index: 9999;
            display: flex;
            flex-direction: column;
            gap: 10px;
            max-width: 350px;
        }

        .notification {
            background: var(--bg-card);
            backdrop-filter: blur(20px);
            border: 1px solid var(--border);
            border-radius: 12px;
            padding: 16px;
            animation: slideIn 0.3s, fadeOut 0.3s 4.7s;
            box-shadow: 0 10px 40px rgba(0,0,0,0.3);
            display: flex;
            align-items: center;
            gap: 12px;
        }

        @keyframes slideIn {
            from { transform: translateX(100%); opacity: 0; }
            to { transform: translateX(0); opacity: 1; }
        }

        @keyframes fadeOut {
            to { opacity: 0; transform: translateX(100%); }
        }

        /* Start Menu */
        #start-menu {
            position: fixed;
            bottom: 60px;
            left: 20px;
            width: 400px;
            background: rgba(15, 15, 25, 0.95);
            backdrop-filter: blur(30px);
            border: 1px solid var(--border);
            border-radius: 16px;
            z-index: 999;
            display: none;
            box-shadow: 0 20px 60px rgba(0,0,0,0.5);
            overflow: hidden;
        }

        .start-header {
            padding: 20px;
            background: linear-gradient(135deg, rgba(255,0,255,0.1), rgba(0,255,255,0.1));
            border-bottom: 1px solid var(--border);
        }

        .start-user {
            display: flex;
            align-items: center;
            gap: 15px;
        }

        .user-avatar {
            width: 50px;
            height: 50px;
            border-radius: 50%;
            background: linear-gradient(135deg, var(--neon-pink), var(--neon-cyan));
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 24px;
        }

        .apps-grid {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 10px;
            padding: 20px;
        }

        .app-tile {
            aspect-ratio: 1;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            background: rgba(255,255,255,0.03);
            border-radius: 12px;
            cursor: pointer;
            transition: all 0.2s;
            font-size: 24px;
        }

        .app-tile:hover {
            background: rgba(255,255,255,0.1);
            transform: scale(1.05);
        }

        /* Glitch Effect */
        .glitch {
            position: relative;
            color: white;
        }

        .glitch::before,
        .glitch::after {
            content: attr(data-text);
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
        }

        .glitch::before {
            left: 2px;
            text-shadow: -2px 0 var(--neon-pink);
            animation: glitch-1 2s infinite linear alternate-reverse;
            clip-path: polygon(0 0, 100% 0, 100% 35%, 0 35%);
        }

        .glitch::after {
            left: -2px;
            text-shadow: 2px 0 var(--neon-cyan);
            animation: glitch-2 2s infinite linear alternate-reverse;
            clip-path: polygon(0 65%, 100% 65%, 100% 100%, 0 100%);
        }

        @keyframes glitch-1 {
            0% { transform: translateX(0); }
            20% { transform: translateX(-2px); }
            40% { transform: translateX(2px); }
            60% { transform: translateX(-1px); }
            80% { transform: translateX(1px); }
            100% { transform: translateX(0); }
        }

        @keyframes glitch-2 {
            0% { transform: translateX(0); }
            20% { transform: translateX(2px); }
            40% { transform: translateX(-2px); }
            60% { transform: translateX(1px); }
            80% { transform: translateX(-1px); }
            100% { transform: translateX(0); }
        }

        /* Responsive */
        @media (max-width: 768px) {
            .desktop-icons { left: 10px; top: 10px; }
            .window { width: 90vw !important; height: 70vh !important; left: 5vw !important; top: 15vh !important; }
            #start-menu { width: 90vw; left: 5vw; }
            .apps-grid { grid-template-columns: repeat(3, 1fr); }
        }

        /* Scrollbar */
        ::-webkit-scrollbar { width: 8px; height: 8px; }
        ::-webkit-scrollbar-track { background: rgba(0,0,0,0.2); }
        ::-webkit-scrollbar-thumb { background: var(--neon-cyan); border-radius: 4px; }
    </style>
</head>
<body>

    <!-- Boot Screen -->
    <div id="boot-screen">
        <div class="boot-text" id="boot-text"></div>
        <div class="boot-progress">
            <div class="boot-progress-bar"></div>
        </div>
    </div>

    <!-- Desktop Environment -->
    <div id="desktop" style="display: none;">
        <!-- Animated Wallpaper Layers -->
        <div class="wallpaper">
            <div class="nebula-layer" style="width: 600px; height: 600px; background: radial-gradient(circle, rgba(255,0,255,0.3), transparent 70%); top: -200px; left: -100px;"></div>
            <div class="nebula-layer" style="width: 500px; height: 500px; background: radial-gradient(circle, rgba(0,255,255,0.3), transparent 70%); bottom: -100px; right: -100px; animation-delay: -10s;"></div>
            <div class="nebula-layer" style="width: 400px; height: 400px; background: radial-gradient(circle, rgba(170,0,255,0.3), transparent 70%); top: 50%; left: 50%; animation-delay: -20s;"></div>
        </div>

        <!-- Canvas Effects -->
        <canvas id="matrix-canvas"></canvas>
        <canvas id="particle-canvas"></canvas>

        <!-- Desktop Icons -->
        <div class="desktop-icons">
            <div class="desktop-icon" ondblclick="openWindow('terminal')">
                <div class="icon-emoji">💻</div>
                <div class="icon-label">Terminal</div>
            </div>
            <div class="desktop-icon" ondblclick="openWindow('music')">
                <div class="icon-emoji">🎵</div>
                <div class="icon-label">Müzik</div>
            </div>
            <div class="desktop-icon" ondblclick="openWindow('files')">
                <div class="icon-emoji">📁</div>
                <div class="icon-label">Dosyalar</div>
            </div>
            <div class="desktop-icon" ondblclick="openWindow('calc')">
                <div class="icon-emoji">🧮</div>
                <div class="icon-label">Hesap Mak.</div>
            </div>
            <div class="desktop-icon" ondblclick="openWindow('settings')">
                <div class="icon-emoji">⚙️</div>
                <div class="icon-label">Ayarlar</div>
            </div>
            <div class="desktop-icon" ondblclick="openWindow('browser')">
                <div class="icon-emoji">🌐</div>
                <div class="icon-label">Browser</div>
            </div>
        </div>

        <!-- Windows Container -->
        <div id="windows-container"></div>

        <!-- Context Menu -->
        <div id="context-menu">
            <div class="context-item" onclick="createNewFolder()">📁 Yeni Klasör</div>
            <div class="context-item" onclick="changeWallpaper()">🖼️ Arka Plan Değiştir</div>
            <div class="context-item" onclick="toggleMatrix()">🌧️ Matrix Efekti</div>
            <div class="context-divider"></div>
            <div class="context-item" onclick="refreshDesktop()">🔄 Yenile</div>
            <div class="context-item" onclick="showSystemInfo()">ℹ️ Sistem Bilgisi</div>
        </div>

        <!-- Start Menu -->
        <div id="start-menu">
            <div class="start-header">
                <div class="start-user">
                    <div class="user-avatar">👤</div>
                    <div>
                        <div style="font-weight: 700;">Kullanıcı</div>
                        <div style="font-size: 12px; opacity: 0.7; margin-top: 4px;">Yönetici</div>
                    </div>
                </div>
            </div>
            <div class="apps-grid">
                <div class="app-tile" onclick="openWindow('terminal'); toggleStart()">💻</div>
                <div class="app-tile" onclick="openWindow('music'); toggleStart()">🎵</div>
                <div class="app-tile" onclick="openWindow('files'); toggleStart()">📁</div>
                <div class="app-tile" onclick="openWindow('calc'); toggleStart()">🧮</div>
                <div class="app-tile" onclick="openWindow('settings'); toggleStart()">⚙️</div>
                <div class="app-tile" onclick="openWindow('browser'); toggleStart()">🌐</div>
                <div class="app-tile" onclick="openWindow('notes'); toggleStart()">📝</div>
                <div class="app-tile" onclick="openWindow('weather'); toggleStart()">🌤️</div>
            </div>
        </div>

        <!-- Notification Area -->
        <div id="notification-area"></div>

        <!-- Taskbar -->
        <div id="taskbar">
            <button class="start-btn" onclick="toggleStart()">🚀</button>
            
            <div class="taskbar-apps" id="taskbar-apps"></div>
            
            <div class="system-tray">
                <span class="tray-icon" onclick="toggleMute()" id="volume-icon">🔊</span>
                <span class="tray-icon" onclick="toggleWifi()" id="wifi-icon">📶</span>
                <span class="tray-icon">🔋</span>
                <div class="clock" id="clock">
                    <div id="time">00:00</div>
                    <div id="date" style="font-size: 11px;">01.01.2024</div>
                </div>
            </div>
        </div>
    </div>

    <script>
        // System State
        const system = {
            windows: [],
            activeWindow: null,
            zIndex: 100,
            matrixEnabled: false,
            volume: 100,
            wifi: true,
            files: [
                { name: 'Proje', type: 'folder', icon: '📁' },
                { name: 'Müzikler', type: 'folder', icon: '🎵' },
                { name: 'Fotoğraflar', type: 'folder', icon: '📷' },
                { name: 'belge.txt', type: 'file', icon: '📄' },
                { name: 'rapor.pdf', type: 'file', icon: '📑' }
            ]
        };

        // Boot Sequence
        const bootLines = [
            "BIOS Version 3.14.159... OK",
            "RAM Test: 64GB... OK",
            "CPU: Quantum Core i9... OK",
            "GPU: Nebula RTX 9090... OK",
            "Loading Kernel...",
            "Mounting File Systems...",
            "Starting Nebula OS...",
            "Initializing GUI...",
            "Loading Desktop Environment...",
            "System Ready."
        ];

        function runBoot() {
            const bootText = document.getElementById('boot-text');
            let line = 0;
            
            const interval = setInterval(() => {
                if (line < bootLines.length) {
                    const div = document.createElement('div');
                    div.className = 'boot-line';
                    div.textContent = `[${new Date().toLocaleTimeString()}] ${bootLines[line]}`;
                    div.style.animationDelay = '0s';
                    bootText.appendChild(div);
                    line++;
                } else {
                    clearInterval(interval);
                    setTimeout(() => {
                        document.getElementById('boot-screen').style.display = 'none';
                        document.getElementById('desktop').style.display = 'block';
                        initDesktop();
                    }, 1000);
                }
            }, 200);
        }

        // Desktop Initialization
        function initDesktop() {
            updateClock();
            setInterval(updateClock, 1000);
            initParticles();
            showNotification('🚀', 'Nebula OS Başlatıldı', 'Hoş geldiniz!');
            
            // Global event listeners
            document.addEventListener('click', (e) => {
                const contextMenu = document.getElementById('context-menu');
                const startMenu = document.getElementById('start-menu');
                
                if (!e.target.closest('.desktop-icon')) {
                    document.querySelectorAll('.desktop-icon').forEach(icon => {
                        icon.classList.remove('selected');
                    });
                }
                
                if (!e.target.closest('#context-menu') && !e.target.closest('.desktop')) {
                    contextMenu.style.display = 'none';
                }
                
                if (!e.target.closest('#start-menu') && !e.target.closest('.start-btn')) {
                    startMenu.style.display = 'none';
                }
            });

            document.addEventListener('contextmenu', (e) => {
                if (e.target.closest('#desktop') && !e.target.closest('.window')) {
                    e.preventDefault();
                    const menu = document.getElementById('context-menu');
                    menu.style.display = 'block';
                    menu.style.left = e.pageX + 'px';
                    menu.style.top = e.pageY + 'px';
                }
            });

            // Keyboard shortcuts
            document.addEventListener('keydown', (e) => {
                if (e.key === 'Meta' || e.key === 'Control') {
                    if (e.key === 't') openWindow('terminal');
                    if (e.key === 'm') openWindow('music');
                }
            });
        }

        // Window Management
        function openWindow(type) {
            const id = 'win-' + Date.now();
            const win = document.createElement('div');
            win.className = 'window';
            win.id = id;
            win.style.left = (100 + system.windows.length * 30) + 'px';
            win.style.top = (50 + system.windows.length * 30) + 'px';
            win.style.width = type === 'browser' ? '800px' : '600px';
            win.style.height = type === 'calc' ? '500px' : '400px';
            
            const titles = {
                terminal: '💻 Terminal',
                music: '🎵 Kuantum Müzik Çalar',
                files: '📁 Dosya Yöneticisi',
                calc: '🧮 Hesap Makinesi',
                settings: '⚙️ Sistem Ayarları',
                browser: '🌐 Nebula Browser',
                notes: '📝 Not Defteri',
                weather: '🌤️ Hava Durumu'
            };
            
            win.innerHTML = `
                <div class="window-header" onmousedown="startDrag(event, '${id}')">
                    <div class="window-title">${titles[type]}</div>
                    <div class="window-controls">
                        <button class="window-btn btn-minimize" onclick="minimizeWindow('${id}')"></button>
                        <button class="window-btn btn-maximize" onclick="maximizeWindow('${id}')"></button>
                        <button class="window-btn btn-close" onclick="closeWindow('${id}')"></button>
                    </div>
                </div>
                <div class="window-content">
                    ${getWindowContent(type)}
                </div>
            `;
            
            document.getElementById('windows-container').appendChild(win);
            system.windows.push(id);
            system.activeWindow = id;
            updateZIndex(id);
            updateTaskbar();
            
            if (type === 'terminal') initTerminal();
            if (type === 'music') initVisualizer();
            if (type === 'calc') initCalculator();
        }

        function getWindowContent(type) {
            switch(type) {
                case 'terminal':
                    return `<div class="terminal" id="terminal-${Date.now()}">
                        <div class="terminal-line">Nebula OS Terminal v2.0</div>
                        <div class="terminal-line">Copyright (c) 2024 Nebula Corp. Tüm hakları saklıdır.</div>
                        <div class="terminal-line">&nbsp;</div>
                        <div class="terminal-input-line">
                            <span class="terminal-prompt">user@nebula:~$</span>
                            <input type="text" class="terminal-input" onkeypress="handleTerminal(event, this)" autofocus>
                        </div>
                    </div>`;
                
                case 'music':
                    return `
                        <div class="visualizer-container">
                            <canvas id="visualizer-canvas"></canvas>
                        </div>
                        <div style="display: flex; align-items: center; gap: 15px; margin-bottom: 20px;">
                            <button class="calc-btn" style="width: 50px; height: 50px; border-radius: 50%;" onclick="toggleMusic()">⏯️</button>
                            <button class="calc-btn" style="width: 40px; height: 40px; border-radius: 50%;" onclick="nextTrack()">⏭️</button>
                            <div style="flex: 1;">
                                <div style="font-weight: 600; margin-bottom: 5px;">Starlight Symphony</div>
                                <div style="font-size: 12px; opacity: 0.7;">Nebula Orchestra</div>
                            </div>
                            <div style="font-family: monospace;">3:45</div>
                        </div>
                        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px;">
                            <div class="file-item" style="flex-direction: row; gap: 10px;">
                                <span>🎵</span>
                                <div>
                                    <div style="font-weight: 600;">Cosmic Dreams</div>
                                    <div style="font-size: 11px; opacity: 0.7;">Orion Beats</div>
                                </div>
                            </div>
                            <div class="file-item" style="flex-direction: row; gap: 10px;">
                                <span>🎵</span>
                                <div>
                                    <div style="font-weight: 600;">Neon Pulse</div>
                                    <div style="font-size: 11px; opacity: 0.7;">Cyber Wave</div>
                                </div>
                            </div>
                        </div>
                    `;
                
                case 'files':
                    return `
                        <div style="margin-bottom: 15px; padding: 10px; background: rgba(0,0,0,0.3); border-radius: 8px; display: flex; gap: 10px;">
                            <span>📍</span>
                            <span style="opacity: 0.8;">Ana Dizin / Kullanıcı / Belgeler</span>
                        </div>
                        <div class="file-grid" id="file-grid">
                            ${system.files.map(f => `
                                <div class="file-item" ondblclick="openFile('${f.name}')">
                                    <div class="file-icon">${f.icon}</div>
                                    <div class="file-name">${f.name}</div>
                                </div>
                            `).join('')}
                        </div>
                    `;
                
                case 'calc':
                    return `
                        <div class="calculator">
                            <div class="calc-display" id="calc-display">0</div>
                            <button class="calc-btn" onclick="calcClear()">C</button>
                            <button class="calc-btn" onclick="calcOp('/')">/</button>
                            <button class="calc-btn" onclick="calcOp('*')">×</button>
                            <button class="calc-btn" onclick="calcDelete()">⌫</button>
                            <button class="calc-btn" onclick="calcNum('7')">7</button>
                            <button class="calc-btn" onclick="calcNum('8')">8</button>
                            <button class="calc-btn" onclick="calcNum('9')">9</button>
                            <button class="calc-btn operator" onclick="calcOp('-')">-</button>
                            <button class="calc-btn" onclick="calcNum('4')">4</button>
                            <button class="calc-btn" onclick="calcNum('5')">5</button>
                            <button class="calc-btn" onclick="calcNum('6')">6</button>
                            <button class="calc-btn operator" onclick="calcOp('+')">+</button>
                            <button class="calc-btn" onclick="calcNum('1')">1</button>
                            <button class="calc-btn" onclick="calcNum('2')">2</button>
                            <button class="calc-btn" onclick="calcNum('3')">3</button>
                            <button class="calc-btn equals" onclick="calcEquals()">=</button>
                            <button class="calc-btn" style="grid-column: span 2;" onclick="calcNum('0')">0</button>
                            <button class="calc-btn" onclick="calcNum('.')">.</button>
                        </div>
                    `;
                
                case 'settings':
                    return `
                        <div style="max-width: 500px;">
                            <h3 style="margin-bottom: 20px; color: var(--neon-cyan);">🎨 Görünüm Ayarları</h3>
                            <div style="margin-bottom: 20px;">
                                <label style="display: block; margin-bottom: 10px;">Tema Rengi</label>
                                <div style="display: flex; gap: 10px;">
                                    <div style="width: 40px; height: 40px; background: #ff00ff; border-radius: 8px; cursor: pointer; border: 2px solid white;" onclick="setAccent('#ff00ff')"></div>
                                    <div style="width: 40px; height: 40px; background: #00ffff; border-radius: 8px; cursor: pointer;" onclick="setAccent('#00ffff')"></div>
                                    <div style="width: 40px; height: 40px; background: #00ff88; border-radius: 8px; cursor: pointer;" onclick="setAccent('#00ff88')"></div>
                                    <div style="width: 40px; height: 40px; background: #aa00ff; border-radius: 8px; cursor: pointer;" onclick="setAccent('#aa00ff')"></div>
                                </div>
                            </div>
                            <div style="margin-bottom: 20px;">
                                <label style="display: block; margin-bottom: 10px;">Efektler</label>
                                <button class="calc-btn" onclick="toggleMatrix()" style="display: inline-block; margin-right: 10px;">🌧️ Matrix Efekti</button>
                                <button class="calc-btn" onclick="toggleParticles()" style="display: inline-block;">✨ Parçacıklar</button>
                            </div>
                            <h3 style="margin: 30px 0 20px; color: var(--neon-cyan);">🔊 Ses Ayarları</h3>
                            <input type="range" min="0" max="100" value="100" style="width: 100%;" oninput="setVolume(this.value)">
                        </div>
                    `;
                
                case 'browser':
                    return `
                        <div style="height: 100%; display: flex; flex-direction: column;">
                            <div style="display: flex; gap: 10px; margin-bottom: 15px;">
                                <button class="calc-btn" style="padding: 8px 12px;">⬅️</button>
                                <button class="calc-btn" style="padding: 8px 12px;">➡️</button>
                                <button class="calc-btn" style="padding: 8px 12px;">🔄</button>
                                <input type="text" value="https://nebula.os/anasayfa" style="flex: 1; background: rgba(0,0,0,0.3); border: 1px solid var(--border); border-radius: 8px; padding: 0 15px; color: white;" readonly>
                            </div>
                            <div style="flex: 1; background: rgba(0,0,0,0.2); border-radius: 12px; display: flex; align-items: center; justify-content: center; flex-direction: column; gap: 20px;">
                                <div style="font-size: 64px;">🌐</div>
                                <h2>Nebula Browser</h2>
                                <p style="opacity: 0.7;">İnternet bağlantısı simüle ediliyor...</p>
                                <button class="calc-btn" onclick="showNotification('🌐', 'Browser', 'Sayfa yüklenemedi!')">Yeniden Dene</button>
                            </div>
                        </div>
                    `;
                
                case 'notes':
                    return `
                        <textarea style="width: 100%; height: 100%; background: rgba(0,0,0,0.3); border: 1px solid var(--border); border-radius: 8px; padding: 15px; color: white; font-family: inherit; resize: none; outline: none;" placeholder="Notlarınızı buraya yazın..."></textarea>
                    `;
                
                case 'weather':
                    return `
                        <div style="text-align: center; padding: 40px;">
                            <div style="font-size: 80px; margin-bottom: 20px;">⛈️</div>
                            <div style="font-size: 48px; font-weight: 700; margin-bottom: 10px;">24°C</div>
                            <div style="font-size: 18px; opacity: 0.8; margin-bottom: 30px;">İstanbul, Türkiye</div>
                            <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 15px; margin-top: 30px;">
                                <div style="background: rgba(0,0,0,0.2); padding: 15px; border-radius: 12px;">
                                    <div style="opacity: 0.7; font-size: 12px;">Nem</div>
                                    <div style="font-size: 20px; font-weight: 600;">65%</div>
                                </div>
                                <div style="background: rgba(0,0,0,0.2); padding: 15px; border-radius: 12px;">
                                    <div style="opacity: 0.7; font-size: 12px;">Rüzgar</div>
                                    <div style="font-size: 20px; font-weight: 600;">12 km/s</div>
                                </div>
                                <div style="background: rgba(0,0,0,0.2); padding: 15px; border-radius: 12px;">
                                    <div style="opacity: 0.7; font-size: 12px;">UV</div>
                                    <div style="font-size: 20px; font-weight: 600;">Yüksek</div>
                                </div>
                            </div>
                        </div>
                    `;
                
                default:
                    return '<p>Pencere içeriği yüklenemedi.</p>';
            }
        }

        function closeWindow(id) {
            document.getElementById(id).remove();
            system.windows = system.windows.filter(w => w !== id);
            updateTaskbar();
        }

        function minimizeWindow(id) {
            document.getElementById(id).classList.add('minimized');
            updateTaskbar();
        }

        function maximizeWindow(id) {
            const win = document.getElementById(id);
            if (win.style.width === '100%') {
                win.style.width = '600px';
                win.style.height = '400px';
                win.style.left = '100px';
                win.style.top = '50px';
            } else {
                win.style.width = '100%';
                win.style.height = 'calc(100vh - 50px)';
                win.style.left = '0';
                win.style.top = '0';
            }
        }

        function startDrag(e, id) {
            const win = document.getElementById(id);
            system.activeWindow = id;
            updateZIndex(id);
            
            const startX = e.clientX - win.offsetLeft;
            const startY = e.clientY - win.offsetTop;
            
            function doDrag(e) {
                if (win.style.width === '100%') return;
                win.style.left = (e.clientX - startX) + 'px';
                win.style.top = (e.clientY - startY) + 'px';
            }
            
            function stopDrag() {
                document.removeEventListener('mousemove', doDrag);
                document.removeEventListener('mouseup', stopDrag);
            }
            
            document.addEventListener('mousemove', doDrag);
            document.addEventListener('mouseup', stopDrag);
        }

        function updateZIndex(id) {
            system.zIndex++;
            document.getElementById(id).style.zIndex = system.zIndex;
        }

        function updateTaskbar() {
            const container = document.getElementById('taskbar-apps');
            container.innerHTML = '';
            
            system.windows.forEach(id => {
                const win = document.getElementById(id);
                const isMinimized = win.classList.contains('minimized');
                
                const item = document.createElement('div');
                item.className = 'taskbar-item' + (system.activeWindow === id && !isMinimized ? ' active' : '');
                item.innerHTML = win.querySelector('.window-title').innerHTML;
                item.onclick = () => {
                    if (isMinimized) {
                        win.classList.remove('minimized');
                        updateZIndex(id);
                    } else if (system.activeWindow === id) {
                        minimizeWindow(id);
                    } else {
                        updateZIndex(id);
                    }
                    updateTaskbar();
                };
                container.appendChild(item);
            });
        }

        // Clock
        function updateClock() {
            const now = new Date();
            const timeStr = now.toLocaleTimeString('tr-TR', { hour: '2-digit', minute: '2-digit' });
            const dateStr = now.toLocaleDateString('tr-TR');
            document.getElementById('time').textContent = timeStr;
            document.getElementById('date').textContent = dateStr;
        }

        // Notifications
        function showNotification(icon, title, message) {
            const notif = document.createElement('div');
            notif.className = 'notification';
            notif.innerHTML = `
                <div style="font-size: 24px;">${icon}</div>
                <div>
                    <div style="font-weight: 600; margin-bottom: 4px;">${title}</div>
                    <div style="font-size: 13px; opacity: 0.8;">${message}</div>
                </div>
            `;
            document.getElementById('notification-area').appendChild(notif);
            setTimeout(() => notif.remove(), 5000);
        }

        // Start Menu
        function toggleStart() {
            const menu = document.getElementById('start-menu');
            menu.style.display = menu.style.display === 'block' ? 'none' : 'block';
        }

        // Terminal Functions
        function initTerminal() {
            const inputs = document.querySelectorAll('.terminal-input');
            inputs[inputs.length - 1]?.focus();
        }

        function handleTerminal(e, input) {
            if (e.key === 'Enter') {
                const command = input.value.trim();
                const terminal = input.closest('.terminal');
                
                // Add command to history
                const line = document.createElement('div');
                line.className = 'terminal-line';
                line.innerHTML = `<span class="terminal-prompt">user@nebula:~$</span> ${command}`;
                terminal.insertBefore(line, input.closest('.terminal-input-line'));
                
                // Process command
                let response = '';
                switch(command) {
                    case 'help':
                        response = 'Kullanılabilir komutlar: help, clear, date, echo, reboot, neofetch, whoami, ls';
                        break;
                    case 'clear':
                        terminal.innerHTML = '';
                        break;
                    case 'date':
                        response = new Date().toString();
                        break;
                    case 'reboot':
                        location.reload();
                        break;
                    case 'whoami':
                        response = 'user (Yönetici)';
                        break;
                    case 'neofetch':
                        response = `
OS: Nebula OS v2.0
Kernel: Quantum-Core 5.15
Shell: nebula-sh 1.0.0
CPU: Quantum Core i9 @ 5.0GHz
GPU: Nebula RTX 9090
RAM: 64GB Quantum RAM
Uptime: ${Math.floor(Math.random() * 24)} hours
                        `;
                        break;
                    case 'ls':
                        response = 'Belgeler  Müzikler  Projeler  Sistem';
                        break;
                    default:
                        if (command.startsWith('echo ')) {
                            response = command.slice(5);
                        } else if (command) {
                            response = `Komut bulunamadı: ${command}. 'help' yazarak kullanılabilir komutları görüntüleyin.`;
                        }
                }
                
                if (response) {
                    const respLine = document.createElement('div');
                    respLine.className = 'terminal-line';
                    respLine.style.color = '#aaa';
                    respLine.textContent = response;
                    terminal.insertBefore(respLine, input.closest('.terminal-input-line'));
                }
                
                // Clear input
                input.value = '';
                terminal.scrollTop = terminal.scrollHeight;
            }
        }

        // Calculator
        let calcExpression = '';
        
        function initCalculator() {
            calcExpression = '';
            updateCalcDisplay();
        }

        function calcNum(n) {
            calcExpression += n;
            updateCalcDisplay();
        }

        function calcOp(op) {
            calcExpression += ' ' + op + ' ';
            updateCalcDisplay();
        }

        function calcClear() {
            calcExpression = '';
            updateCalcDisplay();
        }

        function calcDelete() {
            calcExpression = calcExpression.trim();
            if (calcExpression.endsWith(' ')) {
                calcExpression = calcExpression.slice(0, -3);
            } else {
                calcExpression = calcExpression.slice(0, -1);
            }
            updateCalcDisplay();
        }

        function calcEquals() {
            try {
                // Safe evaluation
                const clean = calcExpression.replace(/[^0-9+\-*/. ]/g, '');
                calcExpression = eval(clean).toString();
            } catch {
                calcExpression = 'Error';
            }
            updateCalcDisplay();
        }

        function updateCalcDisplay() {
            const display = document.getElementById('calc-display');
            if (display) {
                display.textContent = calcExpression || '0';
            }
        }

        // Visualizer
        let musicPlaying = false;
        function initVisualizer() {
            const canvas = document.getElementById('visualizer-canvas');
            if (!canvas) return;
            
            const ctx = canvas.getContext('2d');
            canvas.width = canvas.offsetWidth;
            canvas.height = canvas.offsetHeight;
            
            const bars = 50;
            const barWidth = canvas.width / bars;
            
            function animate() {
                if (!document.getElementById('visualizer-canvas')) return;
                
                ctx.fillStyle = 'rgba(0, 0, 0, 0.1)';
                ctx.fillRect(0, 0, canvas.width, canvas.height);
                
                for (let i = 0; i < bars; i++) {
                    const height = musicPlaying ? 
                        Math.random() * canvas.height * 0.8 : 
                        Math.sin(Date.now() / 1000 + i) * 20 + 20;
                    
                    const hue = (i / bars) * 360;
                    ctx.fillStyle = `hsl(${hue}, 100%, 50%)`;
                    ctx.fillRect(
                        i * barWidth, 
                        canvas.height - height, 
                        barWidth - 2, 
                        height
                    );
                }
                
                requestAnimationFrame(animate);
            }
            animate();
        }

        function toggleMusic() {
            musicPlaying = !musicPlaying;
        }

        function nextTrack() {
            showNotification('🎵', 'Müzik', 'Sonraki parça çalınıyor...');
        }

        // Particles
        function initParticles() {
            const canvas = document.getElementById('particle-canvas');
            const ctx = canvas.getContext('2d');
            canvas.width = window.innerWidth;
            canvas.height = window.innerHeight;
            
            const particles = [];
            const particleCount = 100;
            
            for (let i = 0; i < particleCount; i++) {
                particles.push({
                    x: Math.random() * canvas.width,
                    y: Math.random() * canvas.height,
                    vx: (Math.random() - 0.5) * 0.5,
                    vy: (Math.random() - 0.5) * 0.5,
                    size: Math.random() * 2
                });
            }
            
            function animate() {
                if (!document.getElementById('particle-canvas')) return;
                
                ctx.clearRect(0, 0, canvas.width, canvas.height);
                
                particles.forEach((p, i) => {
                    p.x += p.vx;
                    p.y += p.vy;
                    
                    if (p.x < 0 || p.x > canvas.width) p.vx *= -1;
                    if (p.y < 0 || p.y > canvas.height) p vy *= -1;
                    
                    ctx.beginPath();
                    ctx.arc(p.x, p.y, p.size, 0, Math.PI * 2);
                    ctx.fillStyle = 'rgba(255, 255, 255, 0.5)';
                    ctx.fill();
                    
                    // Connect nearby particles
                    for (let j = i + 1; j < particles.length; j++) {
                        const dx = particles[j].x - p.x;
                        const dy = particles[j].y - p.y;
                        const dist = Math.sqrt(dx * dx + dy * dy);
                        
                        if (dist < 100) {
                            ctx.beginPath();
                            ctx.moveTo(p.x, p.y);
                            ctx.lineTo(particles[j].x, particles[j].y);
                            ctx.strokeStyle = `rgba(0, 255, 255, ${0.1 * (1 - dist / 100)})`;
                            ctx.stroke();
                        }
                    }
                });
                
                requestAnimationFrame(animate);
            }
            animate();
        }

        // Matrix Rain
        function toggleMatrix() {
            system.matrixEnabled = !system.matrixEnabled;
            const canvas = document.getElementById('matrix-canvas');
            canvas.style.opacity = system.matrixEnabled ? '0.1' : '0';
            
            if (system.matrixEnabled) {
                const ctx = canvas.getContext('2d');
                canvas.width = window.innerWidth;
                canvas.height = window.innerHeight;
                
                const chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@#$%^&*';
                const fontSize = 14;
                const columns = canvas.width / fontSize;
                const drops = [];
                
                for (let i = 0; i < columns; i++) {
                    drops[i] = 1;
                }
                
                function draw() {
                    if (!system.matrixEnabled) return;
                    
                    ctx.fillStyle = 'rgba(0, 0, 0, 0.05)';
                    ctx.fillRect(0, 0, canvas.width, canvas.height);
                    
                    ctx.fillStyle = '#0f0';
                    ctx.font = fontSize + 'px monospace';
                    
                    for (let i = 0; i < drops.length; i++) {
                        const text = chars[Math.floor(Math.random() * chars.length)];
                        ctx.fillText(text, i * fontSize, drops[i] * fontSize);
                        
                        if (drops[i] * fontSize > canvas.height && Math.random() > 0.975) {
                            drops[i] = 0;
                        }
                        drops[i]++;
                    }
                    requestAnimationFrame(draw);
                }
                draw();
            }
        }

        // Context Menu Actions
        function createNewFolder() {
            system.files.push({ name: 'Yeni Klasör', type: 'folder', icon: '📁' });
            showNotification('📁', 'Dosya Yöneticisi', 'Yeni klasör oluşturuldu');
            refreshFileGrid();
        }

        function changeWallpaper() {
            const colors = [
                'radial-gradient(ellipse at center, #1a1a2e 0%, #0a0a0f 100%)',
                'radial-gradient(ellipse at center, #2e1a1a 0%, #0f0a0a 100%)',
                'radial-gradient(ellipse at center, #1a2e1a 0%, #0a0f0a 100%)',
                'linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f0f23 100%)'
            ];
            const desktop = document.getElementById('desktop');
            desktop.style.background = colors[Math.floor(Math.random() * colors.length)];
            showNotification('🖼️', 'Arka Plan', 'Duvar kağıdı değiştirildi');
        }

        function refreshDesktop() {
            showNotification('🔄', 'Sistem', 'Masaüstü yenileniyor...');
            setTimeout(() => location.reload(), 1000);
        }

        function showSystemInfo() {
            showNotification('💻', 'Sistem Bilgisi', 'Nebula OS v2.0 | 64GB RAM | Quantum CPU');
        }

        function openFile(name) {
            showNotification('📄', 'Dosya', `${name} açılıyor...`);
        }

        function refreshFileGrid() {
            const grid = document.getElementById('file-grid');
            if (grid) {
                grid.innerHTML = system.files.map(f => `
                    <div class="file-item" ondblclick="openFile('${f.name}')">
                        <div class="file-icon">${f.icon}</div>
                        <div class="file-name">${f.name}</div>
                    </div>
                `).join('');
            }
        }

        // System Tray
        function toggleMute() {
            system.volume = system.volume > 0 ? 0 : 100;
            document.getElementById('volume-icon').textContent = system.volume ? '🔊' : '🔇';
            showNotification(system.volume ? '🔊' : '🔇', 'Ses', system.volume ? 'Ses açıldı' : 'Ses kapatıldı');
        }

        function toggleWifi() {
            system.wifi = !system.wifi;
            document.getElementById('wifi-icon').textContent = system.wifi ? '📶' : '📵';
            showNotification(system.wifi ? '📶' : '📵', 'Ağ', system.wifi ? 'Wi-Fi bağlandı' : 'Wi-Fi bağlantısı kesildi');
        }

        function setVolume(val) {
            system.volume = val;
        }

        function setAccent(color) {
            document.documentElement.style.setProperty('--neon-cyan', color);
            showNotification('🎨', 'Tema', 'Tema rengi güncellendi');
        }

        function toggleParticles() {
            const canvas = document.getElementById('particle-canvas');
            canvas.style.display = canvas.style.display === 'none' ? 'block' : 'none';
        }

        // Initialize
        runBoot();
    </script>
</body>
</html>
```