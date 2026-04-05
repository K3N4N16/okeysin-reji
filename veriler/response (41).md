<think>
We are going to enhance the existing webpage with more features and creativity.
 The user wants more visual appeal, more functions, and creative details.

 Ideas for enhancement:
 1. Add a dynamic particle background.
 2. Add a music visualizer that reacts to simulated audio (since we cannot access real audio, we'll simulate with animations).
 3. Add a dark/light mode toggle.
 4. Add more interactive elements in the music cards (like a progress bar and time indicator).
 5. Add a section for blog or thoughts (with a mini-blog slider).
 6. Add a clock or date display that is styled creatively.
 7. Add a floating action button for quick actions (like scroll to top, change theme, etc.).
 8. Make the music player more realistic with play/pause, next, previous.
 9. Add a section for projects or works with a creative gallery.

 However, note the constraints: no network calls, no localStorage. So we cannot store theme preference persistently.

 Let's break down:

 1. Particle Background: We can create a canvas with particles that move and interact with the mouse.

 2. Music Visualizer: We can create a canvas-based visualizer that shows random bars or circles moving (simulating music).

 3. Dark/Light Mode: We can toggle a class on the body and adjust colors accordingly.

 4. Music Player: We can simulate a music player with a list of songs. We can have play, pause, next, previous buttons and update the currently playing song.

 5. Blog Section: We can create a slider for short blog posts or thoughts.

 6. Clock: A digital/analog clock that shows current time.

 7. Floating Action Button: A button that floats and has options for theme, scroll to top, etc.

 8. Projects Gallery: A grid or slider of projects with emojis as icons.

 Since the code is already long, we need to integrate these features without making the code too messy.

 We'll restructure a bit:

 We'll add:
  - A canvas for particles and a canvas for visualizer (if not playing, we can show particles, else visualizer?).
  - We'll add a music player bar at the bottom that is fixed and shows the current song and controls.
  - We'll change the music cards to be part of a player system.

 Steps:

 1. Add canvas for particles (background) and style it to cover the whole page.

 2. Modify the music section to have a player that controls a simulated playlist.

 3. Add a visualizer that appears when music is playing.

 4. Add a theme toggle (dark/light) and adjust colors.

 5. Add a clock in the hero section or contact section.

 6. Add a projects section (maybe replace one of the existing sections or add a new slide).

 7. Add a floating action button for theme and scroll to top.

 8. Add a blog section (or combine with projects).

 However, note we have 4 slides already. We can add a 5th slide or replace one.

 Let's add a 5th slide for projects and a 6th for blog? But then the user might have to scroll more. Alternatively, we can make the page longer and have vertical scrolling with horizontal slides? But the current design is horizontal.

 We are already using horizontal slides. We can add more dots and slides.

 Let's plan for 6 slides:

 Slide 1: Hero
 Slide 2: Music Player & Visualizer
 Slide 3: Skills
 Slide 4: Projects Gallery
 Slide 5: Blog/Thoughts
 Slide 6: Contact

 We'll need to adjust the dots and navigation.

 Alternatively, we can keep the current 4 slides and enhance each one.

 Given the complexity, let's stick to 4 slides but enhance them:

 Slide 1: Hero (add clock and particle background)
 Slide 2: Music (add visualizer and player controls)
 Slide 3: Skills & Projects (combine)
 Slide 4: Contact & Blog (combine)

 We'll do:

 1. Particle Background: We'll add a canvas that covers the entire background and remove the ambient-bg div.

 2. Music Player: We'll create a fixed player at the bottom that is always visible and controls the music.

 3. Visualizer: We'll show the visualizer in the music slide when a song is playing.

 4. Theme Toggle: A button in the top right to toggle dark/light.

 5. Clock: In the hero slide, add a stylish clock.

 6. Projects: Add a grid of projects in the skills slide.

 7. Blog: Add a carousel of blog posts in the contact slide.

 8. Floating Action Button: Maybe not needed if we have fixed player and theme toggle.

 Let's code step by step.

 We'll start by adding the particle background.

 Note: We cannot use external images, so we'll use emojis for projects and blog.

 Due to the complexity, we'll focus on the most important enhancements:

 1. Particle background.
 2. Music player with visualizer.
 3. Theme toggle.

 If time and space permit, we'll add more.

 Let's code the particle background first.

 We'll create a canvas and draw particles that move and connect with lines.

 We'll also make the particles interact with the mouse.

 We'll adjust the colors for light and dark mode.

 We'll add the theme toggle and clock in the hero section.

 We'll also make the music player more functional.

 However, note that we are in a single HTML file and we have to be mindful of the length.

 Let's start by adding the canvas and removing the ambient-bg.

 We'll adjust the z-index so that the canvas is behind everything.

 We'll also add the theme toggle and clock in the hero section.

 We'll then update the music player to have a fixed bar and visualizer.

 We'll simulate playing a song with a setInterval for the visualizer.

 We'll create an array of songs and let the user navigate.

 We'll update the music cards to set the current song.

 We'll also add a play/pause button in the fixed player.

 Let's do it.

 IMPORTANT: We are not allowed to use localStorage, so theme will reset on refresh.

 We'll write the code accordingly.

 Let's begin by modifying the HTML structure.

 Due to the length, we'll only show the modified parts and the new JavaScript.

 We'll try to keep the existing style and just enhance.

 We'll break the code into parts:

 1. Add canvas for particles.
 2. Add theme toggle button.
 3. Add clock in hero.
 4. Modify music section to have a visualizer and fixed player.
 5. Add new sections if needed.

 Since we are already at the limit of the response, we'll focus on:

  - Particle background
  - Theme toggle
  - Clock
  - Music player with visualizer

 We'll leave out projects and blog for now, or we can replace the skills and contact with projects and blog.

 Let's decide:

 We'll change:

 Slide 1: Hero (with clock and particle background)
 Slide 2: Music (with visualizer and player)
 Slide 3: Projects (grid of projects with emojis)
 Slide 4: Blog (carousel of blog posts)

 We'll remove the skills and contact, or we can combine.

 Alternatively, we can have 6 slides and adjust the slider to handle 6.

 We'll adjust the slider to 6 slides and update the dots.

 Let's do 6 slides:

 1. Hero
 2. Music
 3. Projects
 4. Blog
 5. Skills
 6. Contact

 But the user said "daha yaratıcı daha görsel", so we'll focus on visual and creative.

 We'll create:

 1. Hero: with particle background, clock, theme toggle, and a creative title.
 2. Music: with a visualizer and advanced player.
 3. Projects: with a creative grid or masonry of project cards.
 4. Blog: with a creative blog post slider.
 5. Skills: with animated skill bars or circles.
 6. Contact: with a creative contact form (but we cannot submit, so just visual) and social links.

 We'll adjust the code accordingly.

 However, note the constraint of the response length. We'll try to keep it as minimal as possible but add these features.

 We'll start by adding the canvas for particles and the theme toggle.

 We'll then add the clock in the hero.

 We'll then change the music slide to have a visualizer and a fixed player.

 We'll then add new slides for projects, blog, skills, and contact.

 We'll update the navigation dots and the slider to have 6 slides.

 We'll also update the styles for the new theme (light mode).

 Let's code step by step.

 Due to the complexity, we'll show the entire code with the enhancements.

 We'll structure the code with:

  - HTML: with 6 slides and the new elements.
  - CSS: updated for the new slides and theme.
  - JavaScript: for particles, theme toggle, clock, music player, visualizer, and slider.

 We'll try to keep the code efficient.

 Let's start.

 Note: This will be a very long code. We'll have to be concise.

 We'll write the code in the following order:

  1. HTML structure with 6 slides.
  2. CSS for the new slides and theme.
  3. JavaScript for the new functionalities.

 We'll keep the existing code and modify.

 Due to the length, we might not be able to write the entire code here, but we'll try to cover the key parts.

 We'll start by replacing the entire code with the new structure.

 IMPORTANT: We are not allowed to use localStorage, so theme will not persist.

 Let's go.
</think>```html
<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Nebula | Yaratıcı Portfolyo</title>
    <style>
        :root {
            --neon-pink: #ff00ff;
            --neon-cyan: #00ffff;
            --neon-green: #00ff88;
            --neon-purple: #aa00ff;
            --deep-space: #050510;
            --star-dust: #1a1a2e;
            --comet-tail: rgba(255,255,255,0.1);
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Segoe UI', system-ui, sans-serif;
            background: var(--deep-space);
            color: #fff;
            overflow-x: hidden;
            min-height: 100vh;
            width: 100%;
            position: relative;
        }

        /* 🌌 Nebula Background Effect */
        .nebula-container {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            z-index: -2;
            filter: blur(40px);
            opacity: 0.6;
        }

        .nebula {
            position: absolute;
            border-radius: 50%;
            animation: nebulaFloat 20s infinite ease-in-out;
        }

        .nebula-1 {
            width: 60vw;
            height: 60vh;
            top: 10%;
            left: 10%;
            background: radial-gradient(circle, var(--neon-pink), transparent 70%);
            animation-delay: 0s;
        }

        .nebula-2 {
            width: 50vw;
            height: 50vh;
            bottom: 10%;
            right: 10%;
            background: radial-gradient(circle, var(--neon-cyan), transparent 70%);
            animation-delay: 5s;
        }

        .nebula-3 {
            width: 40vw;
            height: 40vh;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            background: radial-gradient(circle, var(--neon-purple), transparent 70%);
            animation-delay: 10s;
        }

        @keyframes nebulaFloat {
            0%, 100% { transform: translate(0, 0) scale(1); }
            33% { transform: translate(30px, -20px) scale(1.1); }
            66% { transform: translate(-20px, 30px) scale(0.9); }
        }

        /* ✨ Particle Field */
        .particles {
            position: fixed;
            width: 100%;
            height: 100%;
            z-index: -1;
        }

        .particle {
            position: absolute;
            width: 2px;
            height: 2px;
            background: white;
            border-radius: 50%;
            animation: particleTwinkle 2s infinite;
        }

        @keyframes particleTwinkle {
            0%, 100% { opacity: 0.1; }
            50% { opacity: 1; }
        }

        /* 🚀 Main Container */
        .main-container {
            max-width: 1400px;
            margin: 0 auto;
            padding: 2rem;
        }

        /* 🌟 Header with Holographic Effect */
        .holographic-header {
            text-align: center;
            margin-bottom: 3rem;
            position: relative;
            padding: 2rem;
            background: rgba(255, 255, 255, 0.02);
            backdrop-filter: blur(10px);
            border-radius: 30px;
            border: 1px solid var(--comet-tail);
            overflow: hidden;
        }

        .holographic-header::before {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, 
                transparent, 
                rgba(255, 255, 255, 0.1), 
                transparent);
            animation: hologramScan 3s infinite;
        }

        @keyframes hologramScan {
            0% { left: -100%; }
            100% { left: 100%; }
        }

        .main-title {
            font-size: clamp(3rem, 8vw, 5rem);
            font-weight: 900;
            background: linear-gradient(45deg, 
                var(--neon-pink), 
                var(--neon-cyan), 
                var(--neon-green));
            background-size: 300% 300%;
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            animation: titleGradient 5s ease infinite;
            margin-bottom: 1rem;
            letter-spacing: -2px;
        }

        @keyframes titleGradient {
            0%, 100% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
        }

        .tagline {
            font-size: 1.3rem;
            color: rgba(255, 255, 255, 0.7);
            margin-bottom: 2rem;
            font-weight: 300;
        }

        /* 🎮 Interactive Dashboard Grid */
        .dashboard-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
            gap: 2rem;
            margin-bottom: 3rem;
        }

        /* 📊 Dashboard Card */
        .dashboard-card {
            background: rgba(255, 255, 255, 0.03);
            backdrop-filter: blur(20px);
            border: 1px solid var(--comet-tail);
            border-radius: 25px;
            padding: 2rem;
            transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            position: relative;
            overflow: hidden;
            min-height: 300px;
        }

        .dashboard-card:hover {
            transform: translateY(-10px) scale(1.02);
            border-color: var(--neon-cyan);
            box-shadow: 
                0 20px 40px rgba(0, 255, 255, 0.1),
                0 0 60px rgba(0, 255, 255, 0.05);
        }

        .card-header {
            display: flex;
            align-items: center;
            gap: 1rem;
            margin-bottom: 1.5rem;
        }

        .card-icon {
            font-size: 2.5rem;
            filter: drop-shadow(0 0 10px currentColor);
        }

        .card-title {
            font-size: 1.5rem;
            font-weight: 700;
            color: var(--neon-cyan);
        }

        /* 🎵 Advanced Music Player */
        .music-player {
            grid-column: span 2;
        }

        .player-controls {
            display: flex;
            align-items: center;
            gap: 1rem;
            margin-bottom: 2rem;
            padding: 1rem;
            background: rgba(0, 0, 0, 0.3);
            border-radius: 20px;
        }

        .control-btn {
            width: 50px;
            height: 50px;
            border-radius: 50%;
            border: none;
            background: linear-gradient(135deg, var(--neon-pink), var(--neon-purple));
            color: white;
            font-size: 1.2rem;
            cursor: pointer;
            transition: all 0.3s;
            display: flex;
            align-items: center;
            justify-content: center;
        }

        .control-btn:hover {
            transform: scale(1.1);
            box-shadow: 0 0 20px var(--neon-pink);
        }

        .progress-container {
            flex: 1;
            height: 6px;
            background: rgba(255, 255, 255, 0.1);
            border-radius: 3px;
            cursor: pointer;
            position: relative;
        }

        .progress-bar {
            height: 100%;
            width: 30%;
            background: linear-gradient(90deg, var(--neon-pink), var(--neon-cyan));
            border-radius: 3px;
            position: relative;
        }

        .progress-bar::after {
            content: '';
            position: absolute;
            right: -5px;
            top: 50%;
            transform: translateY(-50%);
            width: 12px;
            height: 12px;
            background: white;
            border-radius: 50%;
            box-shadow: 0 0 10px var(--neon-cyan);
        }

        .music-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
            gap: 1rem;
        }

        .music-item {
            background: rgba(255, 255, 255, 0.05);
            border-radius: 15px;
            padding: 1.2rem;
            display: flex;
            align-items: center;
            gap: 1rem;
            cursor: pointer;
            transition: all 0.3s;
        }

        .music-item:hover {
            background: rgba(255, 255, 255, 0.1);
            transform: translateX(5px);
        }

        .music-item.active {
            background: linear-gradient(90deg, rgba(255,0,255,0.2), rgba(0,255,255,0.1));
            border-left: 3px solid var(--neon-pink);
        }

        .music-emoji {
            font-size: 1.8rem;
        }

        /* 🎨 Creative Studio */
        .creative-studio {
            position: relative;
            overflow: hidden;
        }

        .color-picker {
            display: flex;
            gap: 1rem;
            margin-bottom: 2rem;
        }

        .color-option {
            width: 40px;
            height: 40px;
            border-radius: 50%;
            cursor: pointer;
            border: 3px solid transparent;
            transition: all 0.3s;
        }

        .color-option:hover {
            transform: scale(1.2);
            border-color: white;
        }

        .color-option.active {
            transform: scale(1.2);
            border-color: white;
            box-shadow: 0 0 20px currentColor;
        }

        .art-canvas {
            width: 100%;
            height: 200px;
            background: rgba(0, 0, 0, 0.3);
            border-radius: 15px;
            position: relative;
            overflow: hidden;
            border: 2px dashed var(--comet-tail);
        }

        .floating-shape {
            position: absolute;
            animation: floatShape 8s infinite ease-in-out;
        }

        @keyframes floatShape {
            0%, 100% { transform: translate(0, 0) rotate(0deg); }
            25% { transform: translate(30px, 20px) rotate(90deg); }
            50% { transform: translate(20px, -20px) rotate(180deg); }
            75% { transform: translate(-20px, 30px) rotate(270deg); }
        }

        /* 🔮 Mood Generator */
        .mood-generator {
            text-align: center;
        }

        .mood-wheel {
            width: 200px;
            height: 200px;
            margin: 2rem auto;
            position: relative;
            animation: wheelSpin 20s infinite linear;
        }

        .mood-sector {
            position: absolute;
            width: 100%;
            height: 100%;
            clip-path: polygon(50% 50%, 50% 0, 100% 0, 100% 100%, 50% 50%);
            transform-origin: 50% 50%;
        }

        @keyframes wheelSpin {
            from { transform: rotate(0deg); }
            to { transform: rotate(360deg); }
        }

        .current-mood {
            font-size: 2rem;
            margin-top: 1rem;
            animation: moodPulse 2s infinite;
        }

        @keyframes moodPulse {
            0%, 100% { opacity: 1; transform: scale(1); }
            50% { opacity: 0.7; transform: scale(1.1); }
        }

        /* 📱 AI Assistant */
        .ai-assistant {
            position: fixed;
            bottom: 2rem;
            right: 2rem;
            z-index: 1000;
        }

        .ai-avatar {
            width: 60px;
            height: 60px;
            background: linear-gradient(135deg, var(--neon-cyan), var(--neon-green));
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 2rem;
            cursor: pointer;
            animation: aiBreathe 3s infinite;
            box-shadow: 0 0 30px rgba(0, 255, 255, 0.5);
            position: relative;
        }

        .ai-avatar::before {
            content: '';
            position: absolute;
            top: -5px;
            left: -5px;
            right: -5px;
            bottom: -5px;
            background: linear-gradient(135deg, var(--neon-cyan), var(--neon-green));
            border-radius: 50%;
            z-index: -1;
            filter: blur(10px);
            opacity: 0.5;
        }

        @keyframes aiBreathe {
            0%, 100% { transform: scale(1); }
            50% { transform: scale(1.1); }
        }

        .ai-panel {
            position: absolute;
            bottom: 70px;
            right: 0;
            width: 300px;
            background: rgba(10, 10, 25, 0.95);
            backdrop-filter: blur(20px);
            border: 1px solid var(--neon-cyan);
            border-radius: 20px;
            padding: 1.5rem;
            display: none;
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.5);
        }

        .ai-message {
            background: rgba(0, 255, 255, 0.1);
            padding: 1rem;
            border-radius: 15px;
            margin-bottom: 1rem;
            border-left: 3px solid var(--neon-cyan);
        }

        /* 🌈 Gradient Slider */
        .gradient-slider {
            grid-column: span 2;
            margin-top: 2rem;
        }

        .gradient-preview {
            width: 100%;
            height: 100px;
            background: linear-gradient(90deg, var(--neon-pink), var(--neon-cyan), var(--neon-green));
            border-radius: 20px;
            margin-bottom: 2rem;
            animation: gradientShift 5s infinite alternate;
        }

        .slider-controls {
            display: flex;
            gap: 2rem;
            align-items: center;
        }

        .slider-container {
            flex: 1;
        }

        .slider-label {
            display: flex;
            justify-content: space-between;
            margin-bottom: 0.5rem;
            color: var(--neon-cyan);
        }

        input[type="range"] {
            width: 100%;
            height: 8px;
            -webkit-appearance: none;
            background: linear-gradient(90deg, var(--neon-pink), var(--neon-cyan), var(--neon-green));
            border-radius: 4px;
            outline: none;
        }

        input[type="range"]::-webkit-slider-thumb {
            -webkit-appearance: none;
            width: 20px;
            height: 20px;
            background: white;
            border-radius: 50%;
            cursor: pointer;
            box-shadow: 0 0 10px var(--neon-pink);
        }

        /* 📈 Stats Dashboard */
        .stats-grid {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 1rem;
            margin-top: 2rem;
        }

        .stat-card {
            background: rgba(255, 255, 255, 0.05);
            border-radius: 15px;
            padding: 1.5rem;
            text-align: center;
            transition: all 0.3s;
        }

        .stat-card:hover {
            background: rgba(255, 255, 255, 0.1);
            transform: translateY(-5px);
        }

        .stat-value {
            font-size: 2.5rem;
            font-weight: 700;
            background: linear-gradient(45deg, var(--neon-cyan), var(--neon-green));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 0.5rem;
        }

        .stat-label {
            color: rgba(255, 255, 255, 0.7);
            font-size: 0.9rem;
        }

        /* 🎆 Interactive Footer */
        .interactive-footer {
            margin-top: 4rem;
            padding: 2rem;
            text-align: center;
            background: rgba(255, 255, 255, 0.02);
            border-radius: 30px;
            border: 1px solid var(--comet-tail);
            position: relative;
            overflow: hidden;
        }

        .sparkle {
            position: absolute;
            width: 4px;
            height: 4px;
            background: white;
            border-radius: 50%;
            animation: sparkle 2s infinite;
        }

        @keyframes sparkle {
            0%, 100% { opacity: 0; transform: scale(0); }
            50% { opacity: 1; transform: scale(1); }
        }

        /* 📱 Responsive Design */
        @media (max-width: 1024px) {
            .dashboard-grid {
                grid-template-columns: 1fr;
            }
            
            .music-player {
                grid-column: 1;
            }
            
            .gradient-slider {
                grid-column: 1;
            }
            
            .stats-grid {
                grid-template-columns: repeat(2, 1fr);
            }
        }

        @media (max-width: 768px) {
            .main-container {
                padding: 1rem;
            }
            
            .dashboard-card {
                padding: 1.5rem;
            }
            
            .stats-grid {
                grid-template-columns: 1fr;
            }
            
            .ai-assistant {
                bottom: 1rem;
                right: 1rem;
            }
        }

        /* ✨ Custom Scrollbar */
        ::-webkit-scrollbar {
            width: 10px;
        }

        ::-webkit-scrollbar-track {
            background: rgba(255, 255, 255, 0.05);
            border-radius: 5px;
        }

        ::-webkit-scrollbar-thumb {
            background: linear-gradient(45deg, var(--neon-pink), var(--neon-cyan));
            border-radius: 5px;
        }

        ::-webkit-scrollbar-thumb:hover {
            background: linear-gradient(45deg, var(--neon-cyan), var(--neon-green));
        }
    </style>
</head>
<body>
    <!-- 🌌 Nebula Background -->
    <div class="nebula-container">
        <div class="nebula nebula-1"></div>
        <div class="nebula nebula-2"></div>
        <div class="nebula nebula-3"></div>
    </div>

    <!-- ✨ Particle Field -->
    <div class="particles" id="particles"></div>

    <!-- 📱 AI Assistant -->
    <div class="ai-assistant">
        <div class="ai-avatar" onclick="toggleAIPanel()">🤖</div>
        <div class="ai-panel" id="aiPanel">
            <div class="ai-message">
                Merhaba! Ben Nebula AI. Size nasıl yardımcı olabilirim? 🚀
            </div>
            <div class="ai-message">
                🎵 Müzik önerisi: "Starlight" - The Midnight
            </div>
            <div class="ai-message">
                💡 Öneri: Renkleri değiştirerek temanızı kişiselleştirin!
            </div>
        </div>
    </div>

    <!-- 🚀 Main Content -->
    <div class="main-container">
        <!-- 🌟 Holographic Header -->
        <header class="holographic-header">
            <h1 class="main-title">NEBULA STUDIO</h1>
            <p class="tagline">🎨 Yaratıcılığın ve Teknolojinin Buluşma Noktası</p>
            
            <div class="stats-grid">
                <div class="stat-card">
                    <div class="stat-value" id="creativityScore">87%</div>
                    <div class="stat-label">Yaratıcılık</div>
                </div>
                <div class="stat-card">
                    <div class="stat-value" id="energyLevel">⚡92</div>
                    <div class="stat-label">Enerji</div>
                </div>
                <div class="stat-card">
                    <div class="stat-value" id="musicCount">🎵24</div>
                    <div class="stat-label">Parça</div>
                </div>
                <div class="stat-card">
                    <div class="stat-value" id="inspiration">💫∞</div>
                    <div class="stat-label">İlham</div>
                </div>
            </div>
        </header>

        <!-- 🎮 Interactive Dashboard -->
        <main class="dashboard-grid">
            <!-- 🎵 Advanced Music Player -->
            <div class="dashboard-card music-player">
                <div class="card-header">
                    <div class="card-icon">🎵</div>
                    <h2 class="card-title">Kuantum Çalar</h2>
                </div>
                
                <div class="player-controls">
                    <button class="control-btn" onclick="playMusic()">⏯️</button>
                    <button class="control-btn" onclick="nextTrack()">⏭️</button>
                    <div class="progress-container">
                        <div class="progress-bar"></div>
                    </div>
                    <div class="current-time">1:24 / 3:45</div>
                </div>

                <div class="music-grid">
                    <div class="music-item active" onclick="selectTrack(this)">
                        <span class="music-emoji">🌟</span>
                        <div>
                            <div class="track-name">Starlight Symphony</div>
                            <div class="artist-name">Nebula Orchestra</div>
                        </div>
                    </div>
                    
                    <div class="music-item" onclick="selectTrack(this)">
                        <span class="music-emoji">🌌</span>
                        <div>
                            <div class="track-name">Cosmic Dreams</div>
                            <div class="artist-name">Orion Beats</div>
                        </div>
                    </div>
                    
                    <div class="music-item" onclick="selectTrack(this)">
                        <span class="music-emoji">⚡</span>
                        <div>
                            <div class="track-name">Neon Pulse</div>
                            <div class="artist-name">Cyber Wave</div>
                        </div>
                    </div>
                    
                    <div class="music-item" onclick="selectTrack(this)">
                        <span class="music-emoji">🌙</span>
                        <div>
                            <div class="track-name">Lunar Echoes</div>
                            <div class="artist-name">Moonlight</div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- 🎨 Creative Studio -->
            <div class="dashboard-card creative-studio">
                <div class="card-header">
                    <div class="card-icon">🎨</div>
                    <h2 class="card-title">Yaratıcı Stüdyo</h2>
                </div>
                
                <div class="color-picker">
                    <div class="color-option active" style="background: var(--neon-pink);" onclick="changeTheme('pink')"></div>
                    <div class="color-option" style="background: var(--neon-cyan);" onclick="changeTheme('cyan')"></div>
                    <div class="color-option" style="background: var(--neon-green);" onclick="changeTheme('green')"></div>
                    <div class="color-option" style="background: var(--neon-purple);" onclick="changeTheme('purple')"></div>
                </div>

                <div class="art-canvas" id="artCanvas">
                    <!-- Floating shapes will be generated here -->
                </div>
            </div>

            <!-- 🔮 Mood Generator -->
            <div class="dashboard-card mood-generator">
                <div class="card-header">
                    <div class="card-icon">🔮</div>
                    <h2 class="card-title">Ruh Hali Jeneratörü</h2>
                </div>
                
                <div class="mood-wheel">
                    <!-- Mood sectors will be generated by JS -->
                </div>
                
                <div class="current-mood" id="currentMood">💫 İlham Verici</div>
                <button class="control-btn" style="margin-top: 1rem;" onclick="generateMood()">Yeni Ruh Hali</button>
            </div>

            <!-- 🌈 Gradient Slider -->
            <div class="dashboard-card gradient-slider">
                <div class="card-header">
                    <div class="card-icon">🌈</div>
                    <h2 class="card-title">Gradient Kontrol Paneli</h2>
                </div>
                
                <div class="gradient-preview" id="gradientPreview"></div>
                
                <div class="slider-controls">
                    <div class="slider-container">
                        <div class="slider-label">
                            <span>Parlaklık</span>
                            <span id="brightnessValue">75%</span>
                        </div>
                        <input type="range" min="0" max="100" value="75" oninput="updateBrightness(this.value)">
                    </div>
                    
                    <div class="slider-container">
                        <div class="slider-label">
                            <span>Doygunluk</span>
                            <span id="saturationValue">85%</span>
                        </div>
                        <input type="range" min="0" max="100" value="85" oninput="updateSaturation(this.value)">
                    </div>
                </div>
            </div>
        </main>

        <!-- 🎆 Interactive Footer -->
        <footer class="interactive-footer">
            <div class="card-header">
                <div class="card-icon">🚀</div>
                <h2 class="card-title">Yaratıcılık Sonsuzluğa Uzanır</h2>
            </div>
            <p style="margin: 1rem 0; color: rgba(255,255,255,0.7);">
                Bu sayfa tamamen dinamik ve interaktif deneyim için tasarlanmıştır.<br>
                Her element canlı ve tepki verir. Keyfini çıkarın! ✨
            </p>
            <div style="display: flex; gap: 1rem; justify-content: center; margin-top: 2rem;">
                <button class="control-btn" onclick="resetAll()">🔄 Sıfırla</button>
                <button class="control-btn" onclick="surpriseMe()">🎁 Sürpriz</button>
                <button class="control-btn" onclick="toggleEffects()">✨ Efektler</button>
            </div>
        </footer>
    </div>

    <script>
        // 🌌 Initialize Nebula
        document.addEventListener('DOMContentLoaded', function() {
            createParticles();
            initializeMoodWheel();
            createFloatingShapes();
            createSparkles();
            updateStats();
        });

        // ✨ Create Particle Field
        function createParticles() {
            const container = document.getElementById('particles');
            for (let i = 0; i < 100; i++) {
                const particle = document.createElement('div');
                particle.className = 'particle';
                particle.style.left = `${Math.random() * 100}vw`;
                particle.style.top = `${Math.random() * 100}vh`;
                particle.style.animationDelay = `${Math.random() * 2}s`;
                particle.style.opacity = Math.random() * 0.5 + 0.1;
                container.appendChild(particle);
            }
        }

        // 🎨 Create Floating Shapes
        function createFloatingShapes() {
            const canvas = document.getElementById('artCanvas');
            const shapes = ['🔺', '🔶', '🔵', '⭐', '🟣', '🔸'];
            
            for (let i = 0; i < 6; i++) {
                const shape = document.createElement('div');
                shape.className = 'floating-shape';
                shape.textContent = shapes[i];
                shape.style.fontSize = `${Math.random() * 2 + 1}rem`;
                shape.style.left = `${Math.random() * 80}%`;
                shape.style.top = `${Math.random() * 70}%`;
                shape.style.animationDelay = `${Math.random() * 5}s`;
                canvas.appendChild(shape);
            }
        }

        // 🎡 Initialize Mood Wheel
        function initializeMoodWheel() {
            const wheel = document.querySelector('.mood-wheel');
            const moods = ['🎨', '🎵', '💡', '⚡', '🌙', '🌟', '🚀', '🌈'];
            const colors = ['#ff00ff', '#00ffff', '#00ff88', '#aa00ff', '#ffaa00', '#ff0066', '#0099ff', '#88ff00'];
            
            moods.forEach((mood, i) => {
                const sector = document.createElement('div');
                sector.className = 'mood-sector';
                sector.style.backgroundColor = colors[i];
                sector.style.transform = `rotate(${i * 45}deg)`;
                sector.innerHTML = `<div style="transform: rotate(45deg); position: absolute; top: 20px; left: 70px; font-size: 1.5rem;">${mood}</div>`;
                wheel.appendChild(sector);
            });
        }

        // 🔮 Generate Random Mood
        function generateMood() {
            const moods = [
                { emoji: '🎨', text: 'Yaratıcı' },
                { emoji: '🎵', text: 'Müzikal' },
                { emoji: '💡', text: 'İlham Verici' },
                { emoji: '⚡', text: 'Enerjik' },
                { emoji: '🌙', text: 'Sakin' },
                { emoji: '🌟', text: 'Parlak' },
                { emoji: '🚀', text: 'Heyecanlı' },
                { emoji: '🌈', text: 'Renkli' }
            ];
            
            const randomMood = moods[Math.floor(Math.random() * moods.length)];
            document.getElementById('currentMood').innerHTML = `${randomMood.emoji} ${randomMood.text}`;
            
            // Add particle effect
            createMoodParticles(randomMood.emoji);
        }

        // ✨ Create Mood Particles
        function createMoodParticles(emoji) {
            for (let i = 0; i < 20; i++) {
                const particle = document.createElement('div');
                particle.textContent = emoji;
                particle.style.position = 'fixed';
                particle.style.fontSize = '1.5rem';
                particle.style.left = `${Math.random() * 100}vw`;
                particle.style.top = `${Math.random() * 100}vh`;
                particle.style.zIndex = '9999';
                particle.style.animation = 'floatUp 1s ease-out forwards';
                document.body.appendChild(particle);
                
                setTimeout(() => particle.remove(), 1000);
            }
        }

        // 🎵 Music Player Functions
        let isPlaying = false;
        
        function playMusic() {
            isPlaying = !isPlaying;
            const btn = document.querySelector('.player-controls .control-btn');
            btn.textContent = isPlaying ? '⏸️' : '⏯️';
            
            // Animate progress bar
            if (isPlaying) {
                animateProgressBar();
            }
        }
        
        function animateProgressBar() {
            const bar = document.querySelector('.progress-bar');
            let width = 30;
            
            const interval = setInterval(() => {
                if (!isPlaying) {
                    clearInterval(interval);
                    return;
                }
                
                width += 0.5;
                if (width > 100) width = 0;
                bar.style.width = `${width}%`;
                
                // Update time display
                const minutes = Math.floor(width * 3.45 / 100);
                const seconds = Math.floor((width * 3.45 / 100 - minutes) * 60);
                document.querySelector('.current-time').textContent = 
                    `${minutes}:${seconds.toString().padStart(2, '0')} / 3:45`;
            }, 500);
        }
        
        function nextTrack() {
            const items = document.querySelectorAll('.music-item');
            let currentIndex = 0;
            
            items.forEach((item, index) => {
                if (item.classList.contains('active')) {
                    currentIndex = index;
                    item.classList.remove('active');
                }
            });
            
            const nextIndex = (currentIndex + 1) % items.length;
            items[nextIndex].classList.add('active');
            
            // Reset progress
            document.querySelector('.progress-bar').style.width = '30%';
        }
        
        function selectTrack(element) {
            document.querySelectorAll('.music-item').forEach(item => {
                item.classList.remove('active');
            });
            element.classList.add('active');
            document.querySelector('.progress-bar').style.width = '30%';
        }

        // 🎨 Theme Changer
        function changeTheme(color) {
            const root = document.documentElement;
            document.querySelectorAll('.color-option').forEach(opt => {
                opt.classList.remove('active');
            });
            event.target.classList.add('active');
            
            switch(color) {
                case 'pink':
                    root.style.setProperty('--neon-pink', '#ff00ff');
                    root.style.setProperty('--neon-cyan', '#00ffff');
                    break;
                case 'cyan':
                    root.style.setProperty('--neon-pink', '#00ffff');
                    root.style.setProperty('--neon-cyan', '#00ff88');
                    break;
                case 'green':
                    root.style.setProperty('--neon-pink', '#00ff88');
                    root.style.setProperty('--neon-cyan', '#ff00ff');
                    break;
                case 'purple':
                    root.style.setProperty('--neon-pink', '#aa00ff');
                    root.style.setProperty('--neon-cyan', '#ff00aa');
                    break;
            }
            
            // Update gradient preview
            updateGradientPreview();
        }

        // 🌈 Gradient Controls
        function updateBrightness(value) {
            document.getElementById('brightnessValue').textContent = `${value}%`;
            updateGradientPreview();
        }
        
        function updateSaturation(value) {
            document.getElementById('saturationValue').textContent = `${value}%`;
            updateGradientPreview();
        }
        
        function updateGradientPreview() {
            const preview = document.getElementById('gradientPreview');
            const root = getComputedStyle(document.documentElement);
            const pink = root.getPropertyValue('--neon-pink').trim();
            const cyan = root.getPropertyValue('--neon-cyan').trim();
            
            preview.style.background = `linear-gradient(90deg, ${pink}, ${cyan}, var(--neon-green))`;
        }

        // 📊 Update Stats
        function updateStats() {
            // Animate stats
            const stats = {
                creativity: 87,
                energy: 92,
                music: 24
            };
            
            Object.keys(stats).forEach((stat, index) => {
                let value = 0;
                const interval = setInterval(() => {
                    value++;
                    switch(stat) {
                        case 'creativity':
                            document.getElementById('creativityScore').textContent = `${value}%`;
                            break;
                        case 'energy':
                            document.getElementById('energyLevel').textContent = `⚡${value}`;
                            break;
                        case 'music':
                            document.getElementById('musicCount').textContent = `🎵${value}`;
                            break;
                    }
                    
                    if (value >= stats[stat]) {
                        clearInterval(interval);
                    }
                }, 30 * (index + 1));
            });
        }

        // 🤖 AI Assistant
        function toggleAIPanel() {
            const panel = document.getElementById('aiPanel');
            panel.style.display = panel.style.display === 'block' ? 'none' : 'block';
        }

        // ✨ Create Sparkles
        function createSparkles() {
            const footer = document.querySelector('.interactive-footer');
            for (let i = 0; i < 20; i++) {
                const sparkle = document.createElement('div');
                sparkle.className = 'sparkle';
                sparkle.style.left = `${Math.random() * 100}%`;
                sparkle.style.top = `${Math.random() * 100}%`;
                sparkle.style.animationDelay = `${Math.random() * 2}s`;
                footer.appendChild(sparkle);
            }
        }

        // 🎁 Surprise Function
        function surpriseMe() {
            // Random color change
            const colors = ['pink', 'cyan', 'green', 'purple'];
            changeTheme(colors[Math.floor(Math.random() * colors.length)]);
            
            // Random mood
            generateMood();
            
            // Fireworks effect
            for (let i = 0; i < 30; i++) {
                setTimeout(() => {
                    createMoodParticles(['🎉', '✨', '🎊', '🥳'][Math.floor(Math.random() * 4)]);
                }, i * 50);
            }
        }

        // 🔄 Reset All
        function resetAll() {
            changeTheme('pink');
            document.getElementById('brightnessValue').textContent = '75%';
            document.getElementById('saturationValue').textContent = '85%';
            document.querySelector('input[type="range"]').value = 75;
            document.querySelectorAll('input[type="range"]')[1].value = 85;
            document.querySelector('.progress-bar').style.width = '30%';
            isPlaying = false;
            document.querySelector('.player-controls .control-btn').textContent = '⏯️';
            document.getElementById('currentMood').innerHTML = '💫 İlham Verici';
        }

        // ✨ Toggle Effects
        let effectsEnabled = true;
        function toggleEffects() {
            effectsEnabled = !effectsEnabled;
            const elements = document.querySelectorAll('.nebula, .particle, .floating-shape, .sparkle');
            elements.forEach(el => {
                el.style.animationPlayState = effectsEnabled ? 'running' : 'paused';
                el.style.opacity = effectsEnabled ? '' : '0.3';
            });
        }

        // Add floatUp animation for particles
        const style = document.createElement('style');
        style.textContent = `
            @keyframes floatUp {
                0% { transform: translateY(0) scale(1); opacity: 1; }
                100% { transform: translateY(-100px) scale(0); opacity: 0; }
            }
        `;
        document.head.appendChild(style);
    </script>
</body>
</html>
```