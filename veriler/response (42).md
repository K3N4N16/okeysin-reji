<think>
 The user wants me to continue developing the personal webpage with new features, functions, and suggestions. They want it integrated, more creative, more visual, super detailed, with my own suggestions and creativity, and visually themed. 

Key requests:
1. New features and functions
2. Continue development (integrate new things)
3. More creative and visual
4. Super detailed page
5. My own suggestions and creativity
6. Visual theme development

I should create an enhanced version with:
- Advanced visual effects (particle systems, animated backgrounds, 3D transforms)
- Interactive elements (mouse tracking, parallax effects, dynamic lighting)
- New functional features (music visualizer simulation, interactive timeline, skill animations)
- Better UX (smooth page transitions, loading animations, context menus or interactive widgets)
- Creative additions: 
  - Animated cursor
  - Glitch effects
  - Neumorphism + Glassmorphism combo
  - Interactive music player interface (not just cards)
  - Dark/light mode toggle
  - Text scramble effects
  - Magnetic buttons
  - Scroll-triggered animations
  - 3D card tilts
  - Particle network background
  - Dynamic color themes based on "mood" or music

Since it's a personal page with music theme, I can make it like a "Cyberpunk/Neon Music Producer Portfolio" style.

Specific features to add:
1. **Interactive Particle Background**: Connected particles that react to mouse
2. **3D Tilt Cards**: Cards that tilt based on mouse position
3. **Music Visualizer Bars**: Animated equalizer that actually moves
4. **Glitch Text Effect**: For the main heading
5. **Cursor Follower**: Custom glowing cursor
6. **Dynamic Theme Switcher**: Change color schemes (Neon Pink, Cyber Blue, Sunset Orange)
7. **Typewriter Effect**: For subtitles
8. **Scroll Progress Indicator**: Visual indicator on the side
9. **Interactive Skill Bars**: Animated progress bars
10. **Floating Chat Widget**: Simulated contact widget
11. **Parallax Layers**: Different scroll speeds for depth
12. **Hover Spotlight Effect**: Light follows mouse on cards

Make sure:
- Still responsive
- No external assets (emojis only)
- Single file HTML
- No localStorage (use variables)
- Turkish text
- Modern, sleek, flashy ("sık ve gösterişli")

Let's build this step by step:

Structure:
- Preloader animation
- Custom cursor
- Particle canvas background
- Navigation with progress indicator
- Sections:
  1. Hero: Glitch text, typewriter subtitle, 3D tilt profile card
  2. Music: Interactive player UI with working visualizer, playlist, theme switcher
  3. Skills: Animated progress bars with hover details
  4. Gallery/Projects: 3D carousel for projects
  5. Contact: Magnetic buttons, form simulation

Technical implementation:
- Canvas for particles
- CSS 3D transforms for tilts
- requestAnimationFrame for smooth animations
- CSS variables for theming
- Intersection Observer for scroll animations

Let's write the code.
</think> ```html
<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Alex | Creative Developer & Music Curator</title>
    <style>
        :root {
            --primary: #ff00cc;
            --secondary: #3333ff;
            --accent: #00ffff;
            --bg: #050505;
            --glass: rgba(255, 255, 255, 0.03);
            --border: rgba(255, 255, 255, 0.1);
            --theme-1: linear-gradient(135deg, #ff00cc, #3333ff);
            --theme-2: linear-gradient(135deg, #00ff88, #00ccff);
            --theme-3: linear-gradient(135deg, #ff6600, #ff0066);
            --current-theme: var(--theme-1);
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            cursor: none;
        }

        body {
            font-family: 'Segoe UI', system-ui, sans-serif;
            background: var(--bg);
            color: #fff;
            overflow-x: hidden;
            transition: all 0.5s ease;
        }

        /* Custom Cursor */
        .cursor {
            width: 20px;
            height: 20px;
            border: 2px solid var(--primary);
            border-radius: 50%;
            position: fixed;
            pointer-events: none;
            z-index: 9999;
            transition: transform 0.1s, background 0.2s;
            mix-blend-mode: difference;
        }

        .cursor-follower {
            width: 40px;
            height: 40px;
            background: radial-gradient(circle, var(--primary) 0%, transparent 70%);
            border-radius: 50%;
            position: fixed;
            pointer-events: none;
            z-index: 9998;
            opacity: 0.3;
            transition: transform 0.3s ease-out;
        }

        .cursor.hover {
            transform: scale(2);
            background: var(--primary);
            border-color: transparent;
        }

        /* Preloader */
        .preloader {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: #000;
            z-index: 10000;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            transition: opacity 0.5s;
        }

        .preloader-text {
            font-size: 2rem;
            font-weight: bold;
            background: var(--current-theme);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 2rem;
            animation: glitch 2s infinite;
        }

        .loading-bar {
            width: 200px;
            height: 3px;
            background: rgba(255,255,255,0.1);
            border-radius: 3px;
            overflow: hidden;
        }

        .loading-progress {
            height: 100%;
            width: 0%;
            background: var(--current-theme);
            animation: loadProgress 2s ease-in-out forwards;
        }

        @keyframes loadProgress {
            to { width: 100%; }
        }

        /* Particle Canvas */
        #particles {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            z-index: -1;
        }

        /* Scroll Progress */
        .scroll-progress {
            position: fixed;
            right: 0;
            top: 0;
            width: 4px;
            height: 0%;
            background: var(--current-theme);
            z-index: 1000;
            transition: height 0.1s;
        }

        /* Navigation */
        .nav-container {
            position: fixed;
            left: 2rem;
            top: 50%;
            transform: translateY(-50%);
            z-index: 100;
            display: flex;
            flex-direction: column;
            gap: 1.5rem;
        }

        .nav-item {
            width: 50px;
            height: 50px;
            border-radius: 15px;
            background: rgba(255,255,255,0.05);
            border: 1px solid rgba(255,255,255,0.1);
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.3rem;
            transition: all 0.3s;
            position: relative;
            overflow: hidden;
        }

        .nav-item:hover, .nav-item.active {
            background: var(--current-theme);
            transform: scale(1.1);
            border-color: transparent;
            box-shadow: 0 0 30px rgba(255,0,204,0.4);
        }

        .nav-item::after {
            content: attr(data-label);
            position: absolute;
            left: 60px;
            font-size: 0.8rem;
            white-space: nowrap;
            opacity: 0;
            transform: translateX(-10px);
            transition: all 0.3s;
            color: #fff;
            font-weight: 600;
            letter-spacing: 1px;
        }

        .nav-item:hover::after {
            opacity: 1;
            transform: translateX(0);
        }

        /* Theme Switcher */
        .theme-switcher {
            position: fixed;
            bottom: 2rem;
            left: 2rem;
            display: flex;
            gap: 1rem;
            z-index: 100;
        }

        .theme-btn {
            width: 40px;
            height: 40px;
            border-radius: 50%;
            border: 2px solid rgba(255,255,255,0.2);
            cursor: pointer;
            transition: all 0.3s;
        }

        .theme-btn:hover {
            transform: scale(1.2);
            border-color: #fff;
        }

        .theme-1 { background: linear-gradient(135deg, #ff00cc, #3333ff); }
        .theme-2 { background: linear-gradient(135deg, #00ff88, #00ccff); }
        .theme-3 { background: linear-gradient(135deg, #ff6600, #ff0066); }

        /* Main Container */
        .container {
            scroll-snap-type: y mandatory;
            overflow-y: scroll;
            height: 100vh;
            scroll-behavior: smooth;
        }

        .section {
            min-height: 100vh;
            scroll-snap-align: start;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 2rem;
            position: relative;
            perspective: 1000px;
        }

        /* Glass Cards with 3D Tilt */
        .glass-card {
            background: var(--glass);
            backdrop-filter: blur(20px);
            border: 1px solid var(--border);
            border-radius: 30px;
            padding: 3rem;
            max-width: 1000px;
            width: 90%;
            position: relative;
            overflow: hidden;
            transform-style: preserve-3d;
            transition: transform 0.1s;
        }

        .glass-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255,255,255,0.1), transparent);
            transition: left 0.7s;
        }

        .glass-card:hover::before {
            left: 100%;
        }

        /* Glitch Text */
        .glitch {
            font-size: clamp(3rem, 8vw, 6rem);
            font-weight: 900;
            position: relative;
            text-transform: uppercase;
            letter-spacing: -3px;
            background: var(--current-theme);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            animation: glitch 3s infinite;
        }

        @keyframes glitch {
            0%, 100% { transform: translate(0); }
            20% { transform: translate(-2px, 2px); }
            40% { transform: translate(-2px, -2px); }
            60% { transform: translate(2px, 2px); }
            80% { transform: translate(2px, -2px); }
        }

        /* Typewriter */
        .typewriter {
            font-size: 1.5rem;
            color: #888;
            margin: 1.5rem 0;
            height: 2rem;
            overflow: hidden;
            border-right: 2px solid var(--primary);
            white-space: nowrap;
            animation: typing 3.5s steps(40, end), blink-caret 0.75s step-end infinite;
            display: inline-block;
        }

        @keyframes typing {
            from { width: 0 }
            to { width: 100% }
        }

        @keyframes blink-caret {
            from, to { border-color: transparent }
            50% { border-color: var(--primary); }
        }

        /* 3D Profile */
        .profile-3d {
            width: 200px;
            height: 200px;
            margin: 2rem auto;
            position: relative;
            transform-style: preserve-3d;
            animation: float 6s ease-in-out infinite;
        }

        .profile-ring {
            position: absolute;
            width: 100%;
            height: 100%;
            border: 3px solid transparent;
            border-radius: 50%;
            animation: rotate 10s linear infinite;
        }

        .ring-1 {
            border-top-color: var(--primary);
            animation-delay: 0s;
        }

        .ring-2 {
            border-right-color: var(--secondary);
            width: 80%;
            height: 80%;
            top: 10%;
            left: 10%;
            animation-direction: reverse;
        }

        .ring-3 {
            border-bottom-color: var(--accent);
            width: 60%;
            height: 60%;
            top: 20%;
            left: 20%;
        }

        .profile-center {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            font-size: 4rem;
            filter: drop-shadow(0 0 20px var(--primary));
        }

        @keyframes rotate {
            from { transform: rotate(0deg); }
            to { transform: rotate(360deg); }
        }

        @keyframes float {
            0%, 100% { transform: translateY(0px); }
            50% { transform: translateY(-20px); }
        }

        /* Magnetic Buttons */
        .magnetic-btn {
            display: inline-block;
            padding: 1.2rem 3rem;
            margin: 0.5rem;
            background: transparent;
            border: 2px solid var(--primary);
            color: #fff;
            border-radius: 50px;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 2px;
            transition: all 0.3s;
            position: relative;
            overflow: hidden;
            transform-style: preserve-3d;
        }

        .magnetic-btn::before {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: var(--current-theme);
            transition: left 0.5s;
            z-index: -1;
        }

        .magnetic-btn:hover::before {
            left: 0;
        }

        .magnetic-btn:hover {
            transform: translateZ(20px);
            box-shadow: 0 10px 30px rgba(255,0,204,0.3);
            border-color: transparent;
        }

        /* Music Player UI */
        .music-player {
            background: rgba(0,0,0,0.3);
            border-radius: 20px;
            padding: 2rem;
            margin-top: 2rem;
            border: 1px solid rgba(255,255,255,0.1);
        }

        .player-header {
            display: flex;
            align-items: center;
            gap: 2rem;
            margin-bottom: 2rem;
            flex-wrap: wrap;
        }

        .album-art {
            width: 150px;
            height: 150px;
            border-radius: 20px;
            background: var(--current-theme);
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 4rem;
            position: relative;
            overflow: hidden;
            animation: pulse-glow 2s infinite;
            box-shadow: 0 0 30px rgba(255,0,204,0.3);
        }

        @keyframes pulse-glow {
            0%, 100% { box-shadow: 0 0 30px rgba(255,0,204,0.3); }
            50% { box-shadow: 0 0 50px rgba(255,0,204,0.6); }
        }

        .track-info h3 {
            font-size: 1.8rem;
            margin-bottom: 0.5rem;
        }

        .track-info p {
            color: #888;
        }

        /* Visualizer */
        .visualizer {
            display: flex;
            align-items: flex-end;
            gap: 4px;
            height: 60px;
            margin: 2rem 0;
            justify-content: center;
        }

        .bar {
            width: 6px;
            background: var(--current-theme);
            border-radius: 3px;
            transition: height 0.1s ease;
            box-shadow: 0 0 10px currentColor;
        }

        .playlist {
            max-height: 300px;
            overflow-y: auto;
            margin-top: 1rem;
        }

        .playlist-item {
            display: flex;
            align-items: center;
            padding: 1rem;
            border-radius: 10px;
            cursor: pointer;
            transition: all 0.3s;
            margin-bottom: 0.5rem;
            background: rgba(255,255,255,0.02);
            border: 1px solid transparent;
        }

        .playlist-item:hover, .playlist-item.active {
            background: rgba(255,255,255,0.08);
            border-color: rgba(255,255,255,0.1);
            transform: translateX(10px);
        }

        .playlist-item.active {
            border-left: 3px solid var(--primary);
        }

        .playlist-icon {
            font-size: 1.5rem;
            margin-right: 1rem;
            opacity: 0.7;
        }

        .playlist-info {
            flex: 1;
        }

        .playlist-title {
            font-weight: 600;
            margin-bottom: 0.2rem;
        }

        .playlist-artist {
            font-size: 0.85rem;
            color: #666;
        }

        .playlist-duration {
            color: #666;
            font-size: 0.9rem;
        }

        /* Skills with Progress */
        .skills-container {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 2rem;
            margin-top: 2rem;
        }

        .skill-box {
            background: rgba(255,255,255,0.03);
            border: 1px solid rgba(255,255,255,0.05);
            border-radius: 20px;
            padding: 1.5rem;
            transition: all 0.3s;
            position: relative;
            overflow: hidden;
        }

        .skill-box:hover {
            transform: translateY(-5px);
            background: rgba(255,255,255,0.06);
            border-color: rgba(255,255,255,0.2);
        }

        .skill-header {
            display: flex;
            justify-content: space-between;
            margin-bottom: 1rem;
            align-items: center;
        }

        .skill-name {
            font-weight: 700;
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }

        .skill-percent {
            color: var(--primary);
            font-weight: bold;
            font-size: 1.2rem;
        }

        .progress-bar {
            height: 8px;
            background: rgba(255,255,255,0.1);
            border-radius: 4px;
            overflow: hidden;
            position: relative;
        }

        .progress-fill {
            height: 100%;
            background: var(--current-theme);
            border-radius: 4px;
            width: 0%;
            transition: width 1.5s cubic-bezier(0.22, 1, 0.36, 1);
            position: relative;
            overflow: hidden;
        }

        .progress-fill::after {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: linear-gradient(90deg, transparent, rgba(255,255,255,0.3), transparent);
            animation: shimmer 2s infinite;
        }

        @keyframes shimmer {
            0% { transform: translateX(-100%); }
            100% { transform: translateX(100%); }
        }

        /* Contact Form */
        .contact-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 1.5rem;
            margin-top: 2rem;
        }

        .contact-card {
            background: rgba(255,255,255,0.05);
            border: 1px solid rgba(255,255,255,0.1);
            border-radius: 20px;
            padding: 2rem;
            text-align: center;
            transition: all 0.3s;
            cursor: pointer;
            position: relative;
            overflow: hidden;
        }

        .contact-card::before {
            content: '';
            position: absolute;
            top: 50%;
            left: 50%;
            width: 0;
            height: 0;
            background: var(--current-theme);
            border-radius: 50%;
            transform: translate(-50%, -50%);
            transition: width 0.6s, height 0.6s;
            z-index: -1;
            opacity: 0.2;
        }

        .contact-card:hover::before {
            width: 300px;
            height: 300px;
        }

        .contact-card:hover {
            transform: translateY(-10px) rotate(5deg);
            border-color: transparent;
        }

        .contact-icon {
            font-size: 3rem;
            margin-bottom: 1rem;
            display: block;
            transition: transform 0.3s;
        }

        .contact-card:hover .contact-icon {
            transform: scale(1.2) rotate(-5deg);
        }

        /* Spotlight Effect */
        .spotlight {
            position: absolute;
            width: 200px;
            height: 200px;
            background: radial-gradient(circle, rgba(255,0,204,0.15) 0%, transparent 70%);
            pointer-events: none;
            opacity: 0;
            transition: opacity 0.3s;
            z-index: 0;
        }

        .glass-card:hover .spotlight {
            opacity: 1;
        }

        /* Responsive */
        @media (max-width: 768px) {
            .cursor, .cursor-follower { display: none; }
            .nav-container { left: 1rem; }
            .nav-item { width: 40px; height: 40px; font-size: 1rem; }
            .glass-card { padding: 2rem 1.5rem; }
            .theme-switcher { bottom: 1rem; left: 1rem; }
            .typewriter { font-size: 1.1rem; }
        }
    </style>
</head>
<body>

    <!-- Preloader -->
    <div class="preloader" id="preloader">
        <div class="preloader-text">SYSTEM BOOT</div>
        <div class="loading-bar">
            <div class="loading-progress"></div>
        </div>
    </div>

    <!-- Custom Cursor -->
    <div class="cursor"></div>
    <div class="cursor-follower"></div>

    <!-- Particle Canvas -->
    <canvas id="particles"></canvas>

    <!-- Scroll Progress -->
    <div class="scroll-progress" id="scrollProgress"></div>

    <!-- Navigation -->
    <nav class="nav-container">
        <div class="nav-item active" data-label="GİRİŞ" onclick="scrollToSection(0)">🏠</div>
        <div class="nav-item" data-label="MÜZİK" onclick="scrollToSection(1)">🎵</div>
        <div class="nav-item" data-label="YETENEK" onclick="scrollToSection(2)">⚡</div>
        <div class="nav-item" data-label="İLETİŞİM" onclick="scrollToSection(3)">📡</div>
    </nav>

    <!-- Theme Switcher -->
    <div class="theme-switcher">
        <div class="theme-btn theme-1" onclick="changeTheme('theme-1')"></div>
        <div class="theme-btn theme-2" onclick="changeTheme('theme-2')"></div>
        <div class="theme-btn theme-3" onclick="changeTheme('theme-3')"></div>
    </div>

    <div class="container" id="container">
        <!-- Section 1: Hero -->
        <section class="section" id="section-0">
            <div class="glass-card" data-tilt>
                <div class="spotlight"></div>
                <div class="profile-3d">
                    <div class="profile-ring ring-1"></div>
                    <div class="profile-ring ring-2"></div>
                    <div class="profile-ring ring-3"></div>
                    <div class="profile-center">👨‍🚀</div>
                </div>
                
                <h1 class="glitch" data-text="CREATIVE DEV">CREATIVE DEV</h1>
                <div class="typewriter" id="typewriter">Dijital evrenleri kodluyorum...</div>
                
                <p style="text-align: center; color: #888; max-width: 600px; margin: 0 auto; line-height: 1.8;">
                    Modern web teknolojileri, 3D deneyimler ve elektronik müzik tutkusu. 
                    Her pikseli dans ettiren, her kodu ritme dönüştüren yaklaşım. 🎧✨
                </p>
                
                <div style="text-align: center; margin-top: 3rem;">
                    <button class="magnetic-btn" data-magnetic onclick="scrollToSection(1)">Projeleri İncele 🚀</button>
                    <button class="magnetic-btn" data-magnetic onclick="scrollToSection(3)">İletişime Geç 📩</button>
                </div>
            </div>
        </section>

        <!-- Section 2: Music -->
        <section class="section" id="section-1">
            <div class="glass-card" data-tilt>
                <div class="spotlight"></div>
                <h2 style="text-align: center; margin-bottom: 0.5rem;">🎧 Ses Laboratuvarı</h2>
                <p style="text-align: center; color: #666; margin-bottom: 2rem;">Kod yazarken dinlediklerim & önerilerim</p>
                
                <div class="music-player">
                    <div class="player-header">
                        <div class="album-art" id="albumArt">🎵</div>
                        <div class="track-info">
                            <h3 id="currentTrack">Midnight City</h3>
                            <p id="currentArtist">M83</p>
                            <div class="visualizer" id="visualizer">
                                <!-- Bars generated by JS -->
                            </div>
                        </div>
                    </div>
                    
                    <div class="progress-bar" style="margin-bottom: 2rem;">
                        <div class="progress-fill" style="width: 45%;"></div>
                    </div>
                    
                    <div class="playlist" id="playlist">
                        <!-- Playlist items generated by JS -->
                    </div>
                </div>
            </div>
        </section>

        <!-- Section 3: Skills -->
        <section class="section" id="section-2">
            <div class="glass-card" data-tilt>
                <div class="spotlight"></div>
                <h2 style="text-align: center; margin-bottom: 0.5rem;">⚡ Yetenek Matrisi</h2>
                <p style="text-align: center; color: #666; margin-bottom: 2rem;">Teknik stack ve uzmanlık alanları</p>
                
                <div class="skills-container" id="skillsContainer">
                    <!-- Skills generated by JS -->
                </div>
            </div>
        </section>

        <!-- Section 4: Contact -->
        <section class="section" id="section-3">
            <div class="glass-card" data-tilt>
                <div class="spotlight"></div>
                <h2 style="text-align: center; margin-bottom: 0.5rem;">📡 Sinyal Gönder</h2>
                <p style="text-align: center; color: #666; margin-bottom: 2rem;">Projeler, iş birlikleri veya sadece selam için 👋</p>
                
                <div class="contact-grid">
                    <div class="contact-card" onclick="createRipple(this)">
                        <span class="contact-icon">📧</span>
                        <div style="font-weight: 700;">Email</div>
                        <div style="font-size: 0.85rem; color: #666; margin-top: 0.5rem;">hello@alex.dev</div>
                    </div>
                    <div class="contact-card" onclick="createRipple(this)">
                        <span class="contact-icon">🐦</span>
                        <div style="font-weight: 700;">Twitter</div>
                        <div style="font-size: 0.85rem; color: #666; margin-top: 0.5rem;">@alexcode</div>
                    </div>
                    <div class="contact-card" onclick="createRipple(this)">
                        <span class="contact-icon">💻</span>
                        <div style="font-weight: 700;">GitHub</div>
                        <div style="font-size: 0.85rem; color: #666; margin-top: 0.5rem;">@alexgithub</div>
                    </div>
                    <div class="contact-card" onclick="createRipple(this)">
                        <span class="contact-icon">🎵</span>
                        <div style="font-weight: 700;">Spotify</div>
                        <div style="font-size: 0.85rem; color: #666; margin-top: 0.5rem;">Alex Playlist</div>
                    </div>
                </div>
                
                <div style="text-align: center; margin-top: 3rem; padding-top: 2rem; border-top: 1px solid rgba(255,255,255,0.1);">
                    <p style="font-size: 1.2rem; margin-bottom: 0.5rem;">🚀 Haydi birlikte çalışalım!</p>
                    <p style="color: #555; font-size: 0.9rem;">© 2026 Alex Creative. Tüm hakları saklıdır.</p>
                </div>
            </div>
        </section>
    </div>

    <script>
        // Remove preloader
        window.addEventListener('load', () => {
            setTimeout(() => {
                document.getElementById('preloader').style.opacity = '0';
                setTimeout(() => {
                    document.getElementById('preloader').style.display = 'none';
                    initTypewriter();
                }, 500);
            }, 2000);
        });

        // Custom Cursor
        const cursor = document.querySelector('.cursor');
        const follower = document.querySelector('.cursor-follower');
        
        document.addEventListener('mousemove', (e) => {
            cursor.style.left = e.clientX + 'px';
            cursor.style.top = e.clientY + 'px';
            
            setTimeout(() => {
                follower.style.left = e.clientX - 10 + 'px';
                follower.style.top = e.clientY - 10 + 'px';
            }, 100);
        });

        document.querySelectorAll('button, .nav-item, .music-card, .contact-card, .playlist-item').forEach(el => {
            el.addEventListener('mouseenter', () => cursor.classList.add('hover'));
            el.addEventListener('mouseleave', () => cursor.classList.remove('hover'));
        });

        // Particle System
        const canvas = document.getElementById('particles');
        const ctx = canvas.getContext('2d');
        let particles = [];
        
        function resizeCanvas() {
            canvas.width = window.innerWidth;
            canvas.height = window.innerHeight;
        }
        resizeCanvas();
        window.addEventListener('resize', resizeCanvas);

        class Particle {
            constructor() {
                this.x = Math.random() * canvas.width;
                this.y = Math.random() * canvas.height;
                this.size = Math.random() * 2 + 0.5;
                this.speedX = Math.random() * 1 - 0.5;
                this.speedY = Math.random() * 1 - 0.5;
                this.color = `rgba(${Math.random() > 0.5 ? '255, 0, 204' : '0, 255, 255'}, ${Math.random() * 0.5})`;
            }
            
            update() {
                this.x += this.speedX;
                this.y += this.speedY;
                
                if (this.x > canvas.width) this.x = 0;
                if (this.x < 0) this.x = canvas.width;
                if (this.y > canvas.height) this.y = 0;
                if (this.y < 0) this.y = canvas.height;
            }
            
            draw() {
                ctx.fillStyle = this.color;
                ctx.beginPath();
                ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
                ctx.fill();
            }
        }

        function initParticles() {
            particles = [];
            for (let i = 0; i < 100; i++) {
                particles.push(new Particle());
            }
        }

        function connectParticles() {
            for (let i = 0; i < particles.length; i++) {
                for (let j = i; j < particles.length; j++) {
                    const dx = particles[i].x - particles[j].x;
                    const dy = particles[i].y - particles[j].y;
                    const distance = Math.sqrt(dx * dx + dy * dy);
                    
                    if (distance < 100) {
                        ctx.beginPath();
                        ctx.strokeStyle = `rgba(255, 255, 255, ${0.1 - distance/1000})`;
                        ctx.lineWidth = 0.5;
                        ctx.moveTo(particles[i].x, particles[i].y);
                        ctx.lineTo(particles[j].x, particles[j].y);
                        ctx.stroke();
                    }
                }
            }
        }

        function animateParticles() {
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            
            particles.forEach(p => {
                p.update();
                p.draw();
            });
            
            connectParticles();
            requestAnimationFrame(animateParticles);
        }

        initParticles();
        animateParticles();

        // Scroll Progress & Sections
        const container = document.getElementById('container');
        const sections = document.querySelectorAll('.section');
        const navItems = document.querySelectorAll('.nav-item');
        let currentSection = 0;

        container.addEventListener('scroll', () => {
            const scrollTop = container.scrollTop;
            const docHeight = container.scrollHeight - container.clientHeight;
            const scrollPercent = (scrollTop / docHeight) * 100;
            
            document.getElementById('scrollProgress').style.height = scrollPercent + '%';
            
            // Update active section
            const index = Math.round(scrollTop / window.innerHeight);
            if (index !== currentSection) {
                currentSection = index;
                updateNav();
                
                // Animate skills when visible
                if (index === 2) animateSkills();
            }
        });

        function scrollToSection(index) {
            document.getElementById(`section-${index}`).scrollIntoView({ behavior: 'smooth' });
        }

        function updateNav() {
            navItems.forEach((item, idx) => {
                item.classList.toggle('active', idx === currentSection);
            });
        }

        // 3D Tilt Effect
        document.querySelectorAll('[data-tilt]').forEach(card => {
            card.addEventListener('mousemove', (e) => {
                const rect = card.getBoundingClientRect();
                const x = e.clientX - rect.left;
                const y = e.clientY - rect.top;
                
                const centerX = rect.width / 2;
                const centerY = rect.height / 2;
                
                const rotateX = (y - centerY) / 20;
                const rotateY = (centerX - x) / 20;
                
                card.style.transform = `perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg)`;
                
                // Spotlight effect
                const spotlight = card.querySelector('.spotlight');
                if (spotlight) {
                    spotlight.style.left = x - 100 + 'px';
                    spotlight.style.top = y - 100 + 'px';
                }
            });
            
            card.addEventListener('mouseleave', () => {
                card.style.transform = 'perspective(1000px) rotateX(0) rotateY(0)';
            });
        });

        // Magnetic Buttons
        document.querySelectorAll('[data-magnetic]').forEach(btn => {
            btn.addEventListener('mousemove', (e) => {
                const rect = btn.getBoundingClientRect();
                const x = e.clientX - rect.left - rect.width / 2;
                const y = e.clientY - rect.top - rect.height / 2;
                
                btn.style.transform = `translate(${x * 0.3}px, ${y * 0.3}px)`;
            });
            
            btn.addEventListener('mouseleave', () => {
                btn.style.transform = 'translate(0, 0)';
            });
        });

        // Typewriter Effect
        const phrases = [
            "Dijital evrenleri kodluyorum...",
            "Elektronik ritimler üretiyorum...",
            "3D deneyimler tasarlıyorum...",
            "Geleceği şekillendiriyorum..."
        ];
        let phraseIndex = 0;
        let charIndex = 0;
        let isDeleting = false;
        
        function initTypewriter() {
            const element = document.getElementById('typewriter');
            const currentPhrase = phrases[phraseIndex];
            
            if (isDeleting) {
                element.textContent = currentPhrase.substring(0, charIndex - 1);
                charIndex--;
            } else {
                element.textContent = currentPhrase.substring(0, charIndex + 1);
                charIndex++;
            }
            
            let typeSpeed = isDeleting ? 50 : 100;
            
            if (!isDeleting && charIndex === currentPhrase.length) {
                typeSpeed = 2000;
                isDeleting = true;
            } else if (isDeleting && charIndex === 0) {
                isDeleting = false;
                phraseIndex = (phraseIndex + 1) % phrases.length;
                typeSpeed = 500;
            }
            
            setTimeout(initTypewriter, typeSpeed);
        }

        // Theme Switcher
        function changeTheme(theme) {
            const root = document.documentElement;
            const gradients = {
                'theme-1': 'linear-gradient(135deg, #ff00cc, #3333ff)',
                'theme-2': 'linear-gradient(135deg, #00ff88, #00ccff)',
                'theme-3': 'linear-gradient(135deg, #ff6600, #ff0066)'
            };
            
            root.style.setProperty('--current-theme', gradients[theme]);
            
            // Update CSS variables for specific themes
            if (theme === 'theme-1') {
                root.style.setProperty('--primary', '#ff00cc');
                root.style.setProperty('--secondary', '#3333ff');
            } else if (theme === 'theme-2') {
                root.style.setProperty('--primary', '#00ff88');
                root.style.setProperty('--secondary', '#00ccff');
            } else {
                root.style.setProperty('--primary', '#ff6600');
                root.style.setProperty('--secondary', '#ff0066');
            }
            
            // Recreate particles with new colors
            initParticles();
        }

        // Music Player Logic
        const tracks = [
            { icon: '🌙', title: 'Midnight City', artist: 'M83', duration: '4:03' },
            { icon: '⚡', title: 'Instant Crush', artist: 'Daft Punk', duration: '5:37' },
            { icon: '🌌', title: 'Starboy', artist: 'The Weeknd', duration: '3:50' },
            { icon: '🔥', title: 'One More Time', artist: 'Daft Punk', duration: '5:20' },
            { icon: '💎', title: 'Get Lucky', artist: 'Pharrell Williams', duration: '4:07' },
            { icon: '🚀', title: 'Interstellar', artist: 'Hans Zimmer', duration: '4:47' }
        ];

        let currentTrackIndex = 0;
        const visualizer = document.getElementById('visualizer');

        // Create visualizer bars
        for (let i = 0; i < 20; i++) {
            const bar = document.createElement('div');
            bar.className = 'bar';
            bar.style.height = '20%';
            visualizer.appendChild(bar);
        }

        // Populate playlist
        const playlistEl = document.getElementById('playlist');
        tracks.forEach((track, index) => {
            const item = document.createElement('div');
            item.className = `playlist-item ${index === 0 ? 'active' : ''}`;
            item.innerHTML = `
                <span class="playlist-icon">${track.icon}</span>
                <div class="playlist-info">
                    <div class="playlist-title">${track.title}</div>
                    <div class="playlist-artist">${track.artist}</div>
                </div>
                <div class="playlist-duration">${track.duration}</div>
            `;
            item.onclick = () => selectTrack(index);
            playlistEl.appendChild(item);
        });

        function selectTrack(index) {
            currentTrackIndex = index;
            const track = tracks[index];
            
            document.getElementById('albumArt').textContent = track.icon;
            document.getElementById('currentTrack').textContent = track.title;
            document.getElementById('currentArtist').textContent = track.artist;
            
            // Update active state in playlist
            document.querySelectorAll('.playlist-item').forEach((item, idx) => {
                item.classList.toggle('active', idx === index);
            });
        }

        // Animate visualizer
        function animateVisualizer() {
            const bars = visualizer.querySelectorAll('.bar');
            bars.forEach((bar, i) => {
                const height = Math.random() * 80 + 20;
                bar.style.height = height + '%';
                bar.style.opacity = 0.5 + (height / 200);
            });
            
            if (currentSection === 1) { // Only animate when music section is visible
                requestAnimationFrame(animateVisualizer);
            }
        }
        
        // Start visualizer when music section visible
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting && entry.target.id === 'section-1') {
                    animateVisualizer();
                }
            });
        }, { threshold: 0.5 });
        
        observer.observe(document.getElementById('section-1'));

        // Skills Data with Animation
        const skills = [
            { name: 'React/Next.js', icon: '⚛️', percent: 95 },
            { name: 'Three.js/WebGL', icon: '🧊', percent: 88 },
            { name: 'Node.js', icon: '🟢', percent: 85 },
            { name: 'UI/UX Design', icon: '🎨', percent: 92 },
            { name: 'Electronik Müzik', icon: '🎹', percent: 78 },
            { name: 'Python/AI', icon: '🐍', percent: 75 }
        ];

        // Populate skills
        const skillsContainer = document.getElementById('skillsContainer');
        skills.forEach(skill => {
            const div = document.createElement('div');
            div.className = 'skill-box';
            div.innerHTML = `
                <div class="skill-header">
                    <div class="skill-name">
                        <span style="margin-right: 0.5rem;">${skill.icon}</span>
                        ${skill.name}
                    </div>
                    <div class="skill-percent">0%</div>
                </div>
                <div class="progress-bar">
                    <div class="progress-fill" data-width="${skill.percent}"></div>
                </div>
            `;
            skillsContainer.appendChild(div);
        });

        function animateSkills() {
            const progressBars = document.querySelectorAll('.skill-box .progress-fill');
            const counters = document.querySelectorAll('.skill-percent');
            
            progressBars.forEach((bar, index) => {
                setTimeout(() => {
                    const width = bar.getAttribute('data-width');
                    bar.style.width = width + '%';
                    
                    // Animate counter
                    let count = 0;
                    const interval = setInterval(() => {
                        if (count >= width) {
                            clearInterval(interval);
                        } else {
                            count++;
                            counters[index].textContent = count + '%';
                        }
                    }, 15);
                    
                }, index * 100);
            });
        }

        // Ripple Effect for Contact Cards
        function createRipple(element) {
            const ripple = document.createElement('span');
            ripple.style.position = 'absolute';
            ripple.style.width = '20px';
            ripple.style.height = '20px';
            ripple.style.background = 'rgba(255,255,255,0.5)';
            ripple.style.borderRadius = '50%';
            ripple.style.transform = 'translate(-50%, -50%)';
            ripple.style.animation = 'ripple 0.6s ease-out';
            ripple.style.left = '50%';
            ripple.style.top = '50%';
            
            element.appendChild(ripple);
            setTimeout(() => ripple.remove(), 600);
            
            // Wiggle animation
            element.style.animation = 'wiggle 0.5s';
            setTimeout(() => element.style.animation = '', 500);
        }

        // Add ripple animation
        const style = document.createElement('style');
        style.textContent = `
            @keyframes ripple {
                to {
                    width: 200px;
                    height: 200px;
                    opacity: 0;
                }
            }
            @keyframes wiggle {
                0%, 100% { transform: rotate(0deg) translateY(-10px); }
                25% { transform: rotate(-5deg) translateY(-10px); }
                75% { transform: rotate(5deg) translateY(-10px); }
            }
        `;
        document.head.appendChild(style);

        // Parallax Effect for Sections
        document.addEventListener('mousemove', (e) => {
            const mouseX = e.clientX / window.innerWidth;
            const mouseY = e.clientY / window.innerHeight;
            
            document.querySelectorAll('.profile-ring').forEach((ring, index) => {
                const speed = (index + 1) * 20;
                const x = (window.innerWidth - e.pageX * speed) / 100;
                const y = (window.innerHeight - e.pageY * speed) / 100;
                ring.style.transform = `translateX(${x}px) translateY(${y}px)`;
            });
        });

        // Glitch text randomizer
        setInterval(() => {
            const glitch = document.querySelector('.glitch');
            if (Math.random() > 0.95) {
                glitch.style.textShadow = `${Math.random() * 10 - 5}px ${Math.random() * 10 - 5}px rgba(255,0,204,0.5)`;
                setTimeout(() => {
                    glitch.style.textShadow = 'none';
                }, 100);
            }
        }, 2000);

        // Keyboard Navigation
        document.addEventListener('keydown', (e) => {
            if (e.key === 'ArrowDown' && currentSection < 3) {
                scrollToSection(currentSection + 1);
            } else if (e.key === 'ArrowUp' && currentSection > 0) {
                scrollToSection(currentSection - 1);
            }
        });
    </script>
</body>
</html>
```