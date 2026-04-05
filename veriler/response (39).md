<think>
 The user wants a personal webpage that is:
1. "Sliderke olsun" - I interpret this as "with sliders" or "slider-based"
2. "Modern olsun" - Modern design
3. "Sık ve gösterişli" - Sleek and flashy/showy
4. "Eğlence müzik önerilerin varsa ekleyebilirsin" - Can add entertainment/music recommendations if I have any
5. "Başlayalım" - Let's start

Since the user is writing in Turkish, I should respond in Turkish. But the system prompt says "Communicate in the same language the user is using" - so Turkish it is.

However, looking at the instructions again: "Return ONLY the HTML page, nothing else, no commentary." This is a constraint from the system prompt. So I should not add any Turkish commentary outside the HTML, or if I do, it should be minimal or inside the HTML. But the system says "nothing else, no commentary" and "The code should be inside a single markdown HTML code block."

So I need to:
1. Create a full HTML page with inline CSS and JS
2. Make it responsive for iframe container
3. No external assets (use emojis)
4. Modern, sleek, flashy design with sliders
5. Include music recommendations (entertainment)
6. Single file, vanilla JS/CSS
7. No localStorage, no network calls
8. No images/videos imports (use emojis)

Design ideas:
- Dark theme with neon accents (modern & flashy)
- Horizontal slider/carousel for sections or music recommendations
- Smooth animations and transitions
- Glass morphism effects (modern trend)
- Music player interface or music recommendation cards with slider functionality

Structure:
- Header with name and title
- Main content with slider for different sections (About, Music, Projects, Contact)
- Or a full-page slider with snap scrolling
- Music section with recommendations (Turkish or international pop, electronic, etc.)
- Visual effects: gradients, shadows, animations

Since it's a personal page, I'll create a fictional persona or a template that can be customized.

Features:
- Slider navigation between sections (full page slides)
- Music recommendation cards with play buttons (visual only)
- Modern typography (system fonts)
- Particle effects or animated background
- Glass morphism cards

Music recommendations (since user asked):
- Electronic/Dance: The Weeknd, Dua Lipa, Calvin Harris
- Turkish pop: Might not be recognizable emojis, so I'll use international well-known ones
- Or generic "Recommended Tracks" with emojis

Technical implementation:
- Use CSS scroll-snap for slider effect
- Or JavaScript carousel
- Responsive design with flexbox/grid
- Neon color scheme: purple, cyan, pink gradients

Let's code:
- Full viewport sections with scroll-snap-type: x mandatory
- Horizontal scrolling container
- Sections: Home, About, Music, Contact
- Music section with card slider
- Animated background with CSS gradients
- Emoji icons for everything

Wait, the user said "Kişisel bir Web sayfası" (Personal webpage), so I should make it feel like a portfolio/personal site with the user's name, but since I don't know their name, I'll use a placeholder like "JS" or "Developer" or "Your Name".

Actually, looking at "sliderke olsun" - this might mean "with a slider" or "slider-like". In Turkish, "slider" is used as is. So a page with slider functionality.

I'll create:
1. A hero section with a large slider/carousel for featured content
2. Below that, a music recommendation section with horizontal scrollable cards
3. Modern dark theme with gradient text and glowing effects

Let me refine the design:
- Background: Dark navy/black with animated gradient orbs
- Glassmorphism cards (backdrop-filter)
- Horizontal scroll snap for the main navigation between sections
- Music cards with hover effects
- No images, only emojis: 🎵 🎧 🎸 🎹 🎤 etc.

Sections in the slider:
1. Hero/Intro - Name, title, brief description
2. Music Recommendations - Cards with song suggestions
3. Skills/Interests - What the person does
4. Contact - Social links using emojis

Implementation:
```html
<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Kişisel Sayfa</title>
    <style>
        /* Reset and base styles */
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background: #0a0a0a;
            color: #fff;
            overflow-x: hidden;
            height: 100vh;
            width: 100vw;
        }
        
        /* Animated background */
        .bg-animation {
            position: fixed;
            top: 0; left: 0; width: 100%; height: 100%;
            z-index: -1;
            background: radial-gradient(circle at 20% 50%, #1a0033 0%, transparent 50%),
                        radial-gradient(circle at 80% 80%, #001a33 0%, transparent 50%),
                        radial-gradient(circle at 40% 20%, #330019 0%, transparent 50%);
            animation: bgMove 20s ease-in-out infinite;
        }
        
        @keyframes bgMove {
            0%, 100% { transform: translate(0, 0) scale(1); }
            33% { transform: translate(30px, -30px) scale(1.1); }
            66% { transform: translate(-20px, 20px) scale(0.9); }
        }
        
        /* Main slider container */
        .slider-container {
            display: flex;
            height: 100vh;
            overflow-x: auto;
            scroll-snap-type: x mandatory;
            scroll-behavior: smooth;
            -webkit-overflow-scrolling: touch;
        }
        
        .slide {
            min-width: 100vw;
            height: 100vh;
            scroll-snap-align: start;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            padding: 2rem;
            position: relative;
        }
        
        /* Glass card effect */
        .glass-card {
            background: rgba(255, 255, 255, 0.05);
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 20px;
            padding: 2rem;
            box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
            max-width: 800px;
            width: 90%;
        }
        
        /* Typography */
        h1 {
            font-size: clamp(2rem, 5vw, 4rem);
            background: linear-gradient(45deg, #ff00cc, #3333ff);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 1rem;
            text-align: center;
        }
        
        h2 {
            font-size: clamp(1.5rem, 3vw, 2.5rem);
            margin-bottom: 1rem;
            color: #00ffff;
            text-shadow: 0 0 10px rgba(0, 255, 255, 0.5);
        }
        
        p {
            font-size: 1.1rem;
            line-height: 1.6;
            color: #cccccc;
            text-align: center;
        }
        
        /* Music cards slider */
        .music-slider {
            display: flex;
            gap: 1.5rem;
            overflow-x: auto;
            padding: 1rem;
            max-width: 100%;
            scrollbar-width: none;
        }
        
        .music-slider::-webkit-scrollbar { display: none; }
        
        .music-card {
            min-width: 250px;
            background: linear-gradient(135deg, rgba(255,0,204,0.1), rgba(51,51,255,0.1));
            border: 1px solid rgba(255,255,255,0.1);
            border-radius: 15px;
            padding: 1.5rem;
            text-align: center;
            transition: transform 0.3s, box-shadow 0.3s;
            cursor: pointer;
        }
        
        .music-card:hover {
            transform: translateY(-10px) scale(1.05);
            box-shadow: 0 10px 30px rgba(255,0,204,0.3);
            border-color: rgba(255,0,204,0.5);
        }
        
        .music-emoji {
            font-size: 3rem;
            margin-bottom: 1rem;
            display: block;
        }
        
        .music-title {
            font-weight: bold;
            color: #fff;
            margin-bottom: 0.5rem;
        }
        
        .music-artist {
            color: #888;
            font-size: 0.9rem;
        }
        
        /* Navigation dots */
        .nav-dots {
            position: fixed;
            right: 2rem;
            top: 50%;
            transform: translateY(-50%);
            display: flex;
            flex-direction: column;
            gap: 1rem;
            z-index: 100;
        }
        
        .dot {
            width: 12px;
            height: 12px;
            border-radius: 50%;
            background: rgba(255,255,255,0.3);
            cursor: pointer;
            transition: all 0.3s;
            border: 2px solid transparent;
        }
        
        .dot:hover, .dot.active {
            background: #ff00cc;
            box-shadow: 0 0 10px #ff00cc;
            transform: scale(1.2);
        }
        
        /* Decorative elements */
        .glow-text {
            animation: glow 2s ease-in-out infinite alternate;
        }
        
        @keyframes glow {
            from { text-shadow: 0 0 5px #fff, 0 0 10px #ff00cc; }
            to { text-shadow: 0 0 20px #fff, 0 0 30px #ff00cc; }
        }
        
        .floating {
            animation: float 3s ease-in-out infinite;
        }
        
        @keyframes float {
            0%, 100% { transform: translateY(0); }
            50% { transform: translateY(-20px); }
        }
        
        /* Button styles */
        .btn {
            background: linear-gradient(45deg, #ff00cc, #3333ff);
            border: none;
            padding: 1rem 2rem;
            color: white;
            border-radius: 50px;
            font-size: 1rem;
            cursor: pointer;
            margin-top: 1rem;
            transition: transform 0.3s, box-shadow 0.3s;
            text-transform: uppercase;
            letter-spacing: 1px;
            font-weight: bold;
        }
        
        .btn:hover {
            transform: scale(1.05);
            box-shadow: 0 5px 20px rgba(255,0,204,0.4);
        }
        
        /* Responsive */
        @media (max-width: 768px) {
            .glass-card { padding: 1.5rem; }
            .nav-dots { right: 1rem; }
            .music-card { min-width: 200px; }
        }
    </style>
</head>
<body>
    <div class="bg-animation"></div>
    
    <div class="nav-dots">
        <div class="dot active" onclick="goToSlide(0)"></div>
        <div class="dot" onclick="goToSlide(1)"></div>
        <div class="dot" onclick="goToSlide(2)"></div>
        <div class="dot" onclick="goToSlide(3)"></div>
    </div>
    
    <div class="slider-container" id="slider">
        <!-- Slide 1: Hero -->
        <section class="slide">
            <div class="glass-card floating">
                <h1 class="glow-text">Merhaba, Ben JS 👋</h1>
                <p>Yaratıcı kod yazarı, müzik tutkunu ve dijital sanatçı. Modern teknolojiler ve sık tasarımlarla dijital deneyimler yaratıyorum.</p>
                <button class="btn" onclick="goToSlide(1)">Keşfet 🚀</button>
            </div>
        </section>
        
        <!-- Slide 2: Music Recommendations -->
        <section class="slide">
            <div class="glass-card" style="max-width: 900px;">
                <h2>🎵 Müzik Önerilerim</h2>
                <p style="margin-bottom: 2rem;">Günlük eğlence ve enerji için en sevdiğim parçalar</p>
                
                <div class="music-slider">
                    <div class="music-card" onclick="playAnimation(this)">
                        <span class="music-emoji">🌟</span>
                        <div class="music-title">Blinding Lights</div>
                        <div class="music-artist">The Weeknd</div>
                    </div>
                    
                    <div class="music-card" onclick="playAnimation(this)">
                        <span class="music-emoji">🌊</span>
                        <div class="music-title">Levitating</div>
                        <div class="music-artist">Dua Lipa</div>
                    </div>
                    
                    <div class="music-card" onclick="playAnimation(this)">
                        <span class="music-emoji">🎸</span>
                        <div class="music-title">Heat Waves</div>
                        <div class="music-artist">Glass Animals</div>
                    </div>
                    
                    <div class="music-card" onclick="playAnimation(this)">
                        <span class="music-emoji">⚡</span>
                        <div class="music-title">Stay</div>
                        <div class="music-artist">Justin Bieber</div>
                    </div>
                    
                    <div class="music-card" onclick="playAnimation(this)">
                        <span class="music-emoji">🌙</span>
                        <div class="music-title">Midnight City</div>
                        <div class="music-artist">M83</div>
                    </div>
                </div>
            </div>
        </section>
        
        <!-- Slide 3: Skills -->
        <section class="slide">
            <div class="glass-card">
                <h2>💫 Yetenekler & İlgi Alanları</h2>
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); gap: 1rem; margin-top: 2rem;">
                    <div class="music-card" style="min-width: auto;">
                        <span style="font-size: 2rem;">💻</span>
                        <div style="margin-top: 0.5rem; font-weight: bold;">Web Dev</div>
                    </div>
                    <div class="music-card" style="min-width: auto;">
                        <span style="font-size: 2rem;">🎨</span>
                        <div style="margin-top: 0.5rem; font-weight: bold;">UI/UX</div>
                    </div>
                    <div class="music-card" style="min-width: auto;">
                        <span style="font-size: 2rem;">📱</span>
                        <div style="margin-top: 0.5rem; font-weight: bold;">Mobil</div>
                    </div>
                    <div class="music-card" style="min-width: auto;">
                        <span style="font-size: 2rem;">🎧</span>
                        <div style="margin-top: 0.5rem; font-weight: bold;">Müzik</div>
                    </div>
                </div>
            </div>
        </section>
        
        <!-- Slide 4: Contact -->
        <section class="slide">
            <div class="glass-card" style="text-align: center;">
                <h2>📬 İletişim</h2>
                <p style="margin: 2rem 0;">Benimle iletişime geçmek için aşağıdaki kanalları kullanabilirsiniz</p>
                
                <div style="display: flex; justify-content: center; gap: 2rem; flex-wrap: wrap;">
                    <div class="music-card" style="min-width: auto; cursor: pointer;">
                        <span style="font-size: 2.5rem;">📧</span>
                        <div style="margin-top: 0.5rem;">Email</div>
                    </div>
                    <div class="music-card" style="min-width: auto; cursor: pointer;">
                        <span style="font-size: 2.5rem;">🐦</span>
                        <div style="margin-top: 0.5rem;">Twitter</div>
                    </div>
                    <div class="music-card" style="min-width: auto; cursor: pointer;">
                        <span style="font-size: 2.5rem;">💼</span>
                        <div style="margin-top: 0.5rem;">LinkedIn</div>
                    </div>
                </div>
                
                <p style="margin-top: 2rem; font-size: 0.9rem; opacity: 0.7;">✨ 2026 Kişisel Web Sayfası ✨</p>
            </div>
        </section>
    </div>
    
    <script>
        const slider = document.getElementById('slider');
        const dots = document.querySelectorAll('.dot');
        let currentSlide = 0;
        const totalSlides = 4;
        
        function goToSlide(index) {
            currentSlide = index;
            const slideWidth = window.innerWidth;
            slider.scrollTo({
                left: slideWidth * index,
                behavior: 'smooth'
            });
            updateDots();
        }
        
        function updateDots() {
            dots.forEach((dot, index) => {
                if (index === currentSlide) {
                    dot.classList.add('active');
                } else {
                    dot.classList.remove('active');
                }
            });
        }
        
        // Update current slide on scroll
        slider.addEventListener('scroll', () => {
            const slideWidth = window.innerWidth;
            const newSlide = Math.round(slider.scrollLeft / slideWidth);
            if (newSlide !== currentSlide) {
                currentSlide = newSlide;
                updateDots();
            }
        });
        
        // Keyboard navigation
        document.addEventListener('keydown', (e) => {
            if (e.key === 'ArrowRight' && currentSlide < totalSlides - 1) {
                goToSlide(currentSlide + 1);
            } else if (e.key === 'ArrowLeft' && currentSlide > 0) {
                goToSlide(currentSlide - 1);
            }
        });
        
        // Play animation for music cards
        function playAnimation(element) {
            element.style.transform = 'scale(0.95)';
            setTimeout(() => {
                element.style.transform = '';
            }, 200);
            
            // Create floating notes
            const note = document.createElement('div');
            note.textContent = '♪';
            note.style.position = 'absolute';
            note.style.fontSize = '2rem';
            note.style.color = '#ff00cc';
            note.style.left = '50%';
            note.style.top = '50%';
            note.style.transform = 'translate(-50%, -50%)';
            note.style.pointerEvents = 'none';
            note.style.animation = 'floatUp 1s ease-out forwards';
            element.style.position = 'relative';
            element.appendChild(note);
            
            setTimeout(() => note.remove(), 1000);
        }
        
        // Add floatUp animation dynamically
        const style = document.createElement('style');
        style.textContent = `
            @keyframes floatUp {
                0% { transform: translate(-50%, -50%) scale(0); opacity: 1; }
                100% { transform: translate(-50%, -150%) scale(1.5); opacity: 0; }
            }
        `;
        document.head.appendChild(style);
        
        // Touch swipe support
        let touchStartX = 0;
        let touchEndX = 0;
        
        slider.addEventListener('touchstart', (e) => {
            touchStartX = e.changedTouches[0].screenX;
        });
        
        slider.addEventListener('touchend', (e) => {
            touchEndX = e.changedTouches[0].screenX;
            handleSwipe();
        });
        
        function handleSwipe() {
            const threshold = 50;
            if (touchEndX < touchStartX - threshold && currentSlide < totalSlides - 1) {
                goToSlide(currentSlide + 1);
            }
            if (touchEndX > touchStartX + threshold && currentSlide > 0) {
                goToSlide(currentSlide - 1);
            }
        }
    </script>
</body>
</html>
```

This creates:
1. A full-screen horizontal slider with 4 sections (Hero, Music, Skills, Contact)
2. Modern dark theme with neon gradients and glassmorphism
3. Music recommendations with The Weeknd, Dua Lipa, etc. (popular entertainment music)
4. Responsive design that works in iframe
5. Touch/swipe support for mobile
6. Visual effects and animations
7. No external dependencies or images (uses emojis)

The text is in Turkish as requested.
</think> ```html
<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Kişisel Portfolyo</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Segoe UI', system-ui, -apple-system, sans-serif;
            background: #050505;
            color: #ffffff;
            overflow: hidden;
            height: 100vh;
            width: 100vw;
        }

        .ambient-bg {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            z-index: -1;
            background: 
                radial-gradient(circle at 20% 30%, rgba(120, 0, 255, 0.15) 0%, transparent 40%),
                radial-gradient(circle at 80% 70%, rgba(255, 0, 128, 0.15) 0%, transparent 40%),
                radial-gradient(circle at 50% 50%, rgba(0, 200, 255, 0.1) 0%, transparent 50%);
            animation: ambientMove 15s ease-in-out infinite;
        }

        @keyframes ambientMove {
            0%, 100% { transform: scale(1) rotate(0deg); }
            50% { transform: scale(1.1) rotate(5deg); }
        }

        .slider-container {
            display: flex;
            height: 100vh;
            width: 100vw;
            overflow-x: auto;
            scroll-snap-type: x mandatory;
            scroll-behavior: smooth;
            -webkit-overflow-scrolling: touch;
            scrollbar-width: none;
        }

        .slider-container::-webkit-scrollbar {
            display: none;
        }

        .slide {
            min-width: 100vw;
            height: 100vh;
            scroll-snap-align: start;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            padding: 2rem;
            position: relative;
        }

        .glass-panel {
            background: rgba(255, 255, 255, 0.03);
            backdrop-filter: blur(20px);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 30px;
            padding: 3rem;
            max-width: 850px;
            width: 90%;
            box-shadow: 
                0 25px 50px -12px rgba(0, 0, 0, 0.5),
                inset 0 1px 0 rgba(255, 255, 255, 0.05);
            position: relative;
            overflow: hidden;
        }

        .glass-panel::before {
            content: '';
            position: absolute;
            top: -50%;
            left: -50%;
            width: 200%;
            height: 200%;
            background: linear-gradient(45deg, transparent, rgba(255,255,255,0.03), transparent);
            transform: rotate(45deg);
        }

        h1 {
            font-size: clamp(2.5rem, 6vw, 4.5rem);
            font-weight: 800;
            background: linear-gradient(135deg, #ff00cc, #3333ff, #00ccff);
            background-size: 200% 200%;
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            animation: gradientShift 3s ease infinite;
            margin-bottom: 1rem;
            text-align: center;
            letter-spacing: -2px;
        }

        h2 {
            font-size: clamp(1.8rem, 4vw, 3rem);
            margin-bottom: 1.5rem;
            background: linear-gradient(90deg, #00ffff, #ff00cc);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            text-align: center;
        }

        .subtitle {
            font-size: 1.3rem;
            color: #888;
            text-align: center;
            margin-bottom: 2rem;
            font-weight: 300;
        }

        @keyframes gradientShift {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }

        .neon-text {
            text-shadow: 0 0 10px rgba(255, 0, 204, 0.5), 0 0 20px rgba(255, 0, 204, 0.3);
        }

        .music-carousel {
            display: flex;
            gap: 1.5rem;
            overflow-x: auto;
            padding: 1.5rem 0.5rem;
            scrollbar-width: none;
            -webkit-overflow-scrolling: touch;
            cursor: grab;
        }

        .music-carousel:active {
            cursor: grabbing;
        }

        .music-carousel::-webkit-scrollbar {
            display: none;
        }

        .music-card {
            min-width: 220px;
            background: linear-gradient(145deg, rgba(255,255,255,0.05), rgba(255,255,255,0.01));
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 20px;
            padding: 1.8rem;
            text-align: center;
            transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            position: relative;
            overflow: hidden;
        }

        .music-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255,255,255,0.1), transparent);
            transition: left 0.5s;
        }

        .music-card:hover::before {
            left: 100%;
        }

        .music-card:hover {
            transform: translateY(-10px) scale(1.05);
            border-color: rgba(255, 0, 204, 0.5);
            box-shadow: 0 20px 40px rgba(255, 0, 204, 0.2);
        }

        .music-icon {
            font-size: 3.5rem;
            margin-bottom: 1rem;
            display: block;
            filter: drop-shadow(0 0 10px rgba(255,255,255,0.3));
        }

        .track-name {
            font-weight: 700;
            font-size: 1.1rem;
            margin-bottom: 0.5rem;
            color: #fff;
        }

        .artist-name {
            color: #888;
            font-size: 0.95rem;
        }

        .play-btn {
            margin-top: 1rem;
            width: 45px;
            height: 45px;
            border-radius: 50%;
            background: linear-gradient(135deg, #ff00cc, #3333ff);
            border: none;
            color: white;
            font-size: 1.2rem;
            cursor: pointer;
            opacity: 0;
            transform: scale(0);
            transition: all 0.3s;
            display: flex;
            align-items: center;
            justify-content: center;
            margin-left: auto;
            margin-right: auto;
        }

        .music-card:hover .play-btn {
            opacity: 1;
            transform: scale(1);
        }

        .nav-dots {
            position: fixed;
            right: 2.5rem;
            top: 50%;
            transform: translateY(-50%);
            display: flex;
            flex-direction: column;
            gap: 1.2rem;
            z-index: 1000;
        }

        .dot {
            width: 14px;
            height: 14px;
            border-radius: 50%;
            background: rgba(255, 255, 255, 0.2);
            cursor: pointer;
            transition: all 0.4s;
            border: 2px solid transparent;
            position: relative;
        }

        .dot::after {
            content: '';
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%) scale(0);
            width: 100%;
            height: 100%;
            border-radius: 50%;
            background: rgba(255, 0, 204, 0.3);
            transition: transform 0.3s;
        }

        .dot:hover {
            background: rgba(255, 0, 204, 0.6);
            transform: scale(1.2);
        }

        .dot.active {
            background: #ff00cc;
            box-shadow: 0 0 20px rgba(255, 0, 204, 0.8);
            transform: scale(1.3);
        }

        .dot.active::after {
            transform: translate(-50%, -50%) scale(2);
            opacity: 0;
            animation: pulse 2s infinite;
        }

        @keyframes pulse {
            0% { transform: translate(-50%, -50%) scale(1); opacity: 0.5; }
            100% { transform: translate(-50%, -50%) scale(2.5); opacity: 0; }
        }

        .cta-button {
            background: linear-gradient(135deg, #ff00cc, #3333ff);
            border: none;
            padding: 1.2rem 3rem;
            color: white;
            border-radius: 50px;
            font-size: 1.1rem;
            font-weight: 700;
            cursor: pointer;
            margin-top: 2rem;
            transition: all 0.3s;
            text-transform: uppercase;
            letter-spacing: 2px;
            position: relative;
            overflow: hidden;
            display: inline-block;
            text-decoration: none;
        }

        .cta-button:hover {
            transform: translateY(-3px);
            box-shadow: 0 15px 30px rgba(255, 0, 204, 0.4);
        }

        .cta-button::before {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255,255,255,0.4), transparent);
            transition: left 0.5s;
        }

        .cta-button:hover::before {
            left: 100%;
        }

        .floating {
            animation: float 6s ease-in-out infinite;
        }

        @keyframes float {
            0%, 100% { transform: translateY(0px); }
            50% { transform: translateY(-20px); }
        }

        .skills-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(130px, 1fr));
            gap: 1.2rem;
            margin-top: 2rem;
        }

        .skill-item {
            background: rgba(255, 255, 255, 0.03);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 16px;
            padding: 1.5rem;
            text-align: center;
            transition: all 0.3s;
            cursor: pointer;
        }

        .skill-item:hover {
            background: rgba(255, 255, 255, 0.08);
            transform: translateY(-5px);
            border-color: rgba(0, 255, 255, 0.3);
        }

        .skill-icon {
            font-size: 2.5rem;
            margin-bottom: 0.5rem;
            display: block;
        }

        .skill-label {
            font-size: 0.9rem;
            color: #aaa;
            font-weight: 500;
        }

        .contact-links {
            display: flex;
            justify-content: center;
            gap: 2rem;
            margin-top: 2.5rem;
            flex-wrap: wrap;
        }

        .contact-item {
            width: 70px;
            height: 70px;
            border-radius: 20px;
            background: rgba(255, 255, 255, 0.05);
            border: 1px solid rgba(255, 255, 255, 0.1);
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 2rem;
            cursor: pointer;
            transition: all 0.3s;
            position: relative;
            overflow: hidden;
        }

        .contact-item:hover {
            transform: translateY(-5px) rotate(5deg);
            background: rgba(255, 0, 204, 0.1);
            border-color: rgba(255, 0, 204, 0.5);
            box-shadow: 0 10px 30px rgba(255, 0, 204, 0.2);
        }

        .scroll-hint {
            position: absolute;
            bottom: 2rem;
            left: 50%;
            transform: translateX(-50%);
            animation: bounce 2s infinite;
            color: rgba(255, 255, 255, 0.4);
            font-size: 1.5rem;
        }

        @keyframes bounce {
            0%, 100% { transform: translateX(-50%) translateY(0); }
            50% { transform: translateX(-50%) translateY(-10px); }
        }

        .equalizer {
            display: flex;
            gap: 3px;
            height: 20px;
            align-items: flex-end;
            justify-content: center;
            margin-top: 1rem;
            opacity: 0;
            transition: opacity 0.3s;
        }

        .music-card:hover .equalizer {
            opacity: 1;
        }

        .bar {
            width: 4px;
            background: linear-gradient(to top, #ff00cc, #00ffff);
            animation: equalize 0.8s ease-in-out infinite;
        }

        .bar:nth-child(1) { height: 40%; animation-delay: 0.1s; }
        .bar:nth-child(2) { height: 70%; animation-delay: 0.2s; }
        .bar:nth-child(3) { height: 50%; animation-delay: 0.3s; }
        .bar:nth-child(4) { height: 80%; animation-delay: 0.4s; }

        @keyframes equalize {
            0%, 100% { height: 30%; }
            50% { height: 90%; }
        }

        @media (max-width: 768px) {
            .glass-panel { padding: 2rem 1.5rem; }
            .nav-dots { right: 1rem; gap: 0.8rem; }
            .dot { width: 10px; height: 10px; }
            .music-card { min-width: 180px; padding: 1.5rem; }
            .contact-item { width: 60px; height: 60px; font-size: 1.7rem; }
        }
    </style>
</head>
<body>
    <div class="ambient-bg"></div>
    
    <div class="nav-dots">
        <div class="dot active" onclick="scrollToSection(0)"></div>
        <div class="dot" onclick="scrollToSection(1)"></div>
        <div class="dot" onclick="scrollToSection(2)"></div>
        <div class="dot" onclick="scrollToSection(3)"></div>
    </div>

    <div class="slider-container" id="mainSlider">
        <!-- Slide 1: Hero -->
        <section class="slide">
            <div class="glass-panel floating">
                <h1>Merhaba, Ben Alex 👨‍💻</h1>
                <p class="subtitle">Dijital Deneyim Tasarımcısı & Müzik Tutkunu</p>
                <p style="text-align: center; color: #aaa; line-height: 1.8; font-size: 1.1rem;">
                    Modern, sık ve gösterişli web deneyimleri tasarlıyorum. 
                    Kod ve müzik arasında bir yerde yaşıyorum. 🎵✨
                </p>
                <div style="text-align: center;">
                    <button class="cta-button" onclick="scrollToSection(1)">Müzikleri Keşfet 🎧</button>
                </div>
            </div>
            <div class="scroll-hint">↓</div>
        </section>

        <!-- Slide 2: Music Recommendations -->
        <section class="slide">
            <div class="glass-panel">
                <h2>🎵 Günün Eğlence Listesi</h2>
                <p style="text-align: center; color: #888; margin-bottom: 1rem;">
                    Enerji dolu anlar için en sevdiğim parçalar
                </p>
                
                <div class="music-carousel" id="musicCarousel">
                    <div class="music-card" onclick="playEffect(this)">
                        <span class="music-icon">🌟</span>
                        <div class="track-name">Blinding Lights</div>
                        <div class="artist-name">The Weeknd</div>
                        <div class="equalizer">
                            <div class="bar"></div><div class="bar"></div><div class="bar"></div><div class="bar"></div>
                        </div>
                        <button class="play-btn">▶</button>
                    </div>

                    <div class="music-card" onclick="playEffect(this)">
                        <span class="music-icon">🌊</span>
                        <div class="track-name">Levitating</div>
                        <div class="artist-name">Dua Lipa</div>
                        <div class="equalizer">
                            <div class="bar"></div><div class="bar"></div><div class="bar"></div><div class="bar"></div>
                        </div>
                        <button class="play-btn">▶</button>
                    </div>

                    <div class="music-card" onclick="playEffect(this)">
                        <span class="music-icon">🎸</span>
                        <div class="track-name">Heat Waves</div>
                        <div class="artist-name">Glass Animals</div>
                        <div class="equalizer">
                            <div class="bar"></div><div class="bar"></div><div class="bar"></div><div class="bar"></div>
                        </div>
                        <button class="play-btn">▶</button>
                    </div>

                    <div class="music-card" onclick="playEffect(this)">
                        <span class="music-icon">⚡</span>
                        <div class="track-name">Stay</div>
                        <div class="artist-name">The Kid LAROI</div>
                        <div class="equalizer">
                            <div class="bar"></div><div class="bar"></div><div class="bar"></div><div class="bar"></div>
                        </div>
                        <button class="play-btn">▶</button>
                    </div>

                    <div class="music-card" onclick="playEffect(this)">
                        <span class="music-icon">🌙</span>
                        <div class="track-name">Midnight City</div>
                        <div class="artist-name">M83</div>
                        <div class="equalizer">
                            <div class="bar"></div><div class="bar"></div><div class="bar"></div><div class="bar"></div>
                        </div>
                        <button class="play-btn">▶</button>
                    </div>

                    <div class="music-card" onclick="playEffect(this)">
                        <span class="music-icon">🔥</span>
                        <div class="track-name">Titanium</div>
                        <div class="artist-name">David Guetta</div>
                        <div class="equalizer">
                            <div class="bar"></div><div class="bar"></div><div class="bar"></div><div class="bar"></div>
                        </div>
                        <button class="play-btn">▶</button>
                    </div>
                </div>
                
                <p style="text-align: center; color: #666; font-size: 0.9rem; margin-top: 1rem;">
                    🖱️ Sürükleyerek daha fazla müzik keşfedin
                </p>
            </div>
        </section>

        <!-- Slide 3: Skills -->
        <section class="slide">
            <div class="glass-panel">
                <h2>💫 Yetenekler</h2>
                <p style="text-align: center; color: #888; margin-bottom: 1rem;">
                    Teknoloji ve sanatın kesişiminde
                </p>
                
                <div class="skills-grid">
                    <div class="skill-item">
                        <span class="skill-icon">⚛️</span>
                        <div class="skill-label">React</div>
                    </div>
                    <div class="skill-item">
                        <span class="skill-icon">🎨</span>
                        <div class="skill-label">UI/UX</div>
                    </div>
                    <div class="skill-item">
                        <span class="skill-icon">📱</span>
                        <div class="skill-label">Mobile</div>
                    </div>
                    <div class="skill-item">
                        <span class="skill-icon">🎧</span>
                        <div class="skill-label">DJ'lik</div>
                    </div>
                    <div class="skill-item">
                        <span class="skill-icon">🎬</span>
                        <div class="skill-label">Motion</div>
                    </div>
                    <div class="skill-item">
                        <span class="skill-icon">🔮</span>
                        <div class="skill-label">3D Web</div>
                    </div>
                </div>
                
                <p style="text-align: center; color: #666; margin-top: 2rem; font-style: italic;">
                    "Müzik ve kod benim için aynı şey: Ritim ve mantık." 🎵💻
                </p>
            </div>
        </section>

        <!-- Slide 4: Contact -->
        <section class="slide">
            <div class="glass-panel" style="text-align: center;">
                <h2>📬 İletişim</h2>
                <p style="color: #888; margin-bottom: 2rem;">
                    Proje fikirleri veya müzik önerileri için ulaşın!
                </p>
                
                <div class="contact-links">
                    <div class="contact-item" onclick="wiggle(this)" title="Email">
                        📧
                    </div>
                    <div class="contact-item" onclick="wiggle(this)" title="Twitter">
                        🐦
                    </div>
                    <div class="contact-item" onclick="wiggle(this)" title="Instagram">
                        📷
                    </div>
                    <div class="contact-item" onclick="wiggle(this)" title="GitHub">
                        🔗
                    </div>
                    <div class="contact-item" onclick="wiggle(this)" title="Spotify">
                        🎵
                    </div>
                </div>
                
                <div style="margin-top: 3rem; padding-top: 2rem; border-top: 1px solid rgba(255,255,255,0.1);">
                    <p style="color: #555; font-size: 0.9rem;">
                        ✨ 2026 Kişisel Web Sayfası ✨<br>
                        <span style="font-size: 0.8rem;">Tüm hakları saklıdır. | İstanbul, Türkiye 📍</span>
                    </p>
                </div>
            </div>
        </section>
    </div>

    <script>
        const slider = document.getElementById('mainSlider');
        const dots = document.querySelectorAll('.dot');
        let currentIndex = 0;
        let isScrolling;

        function scrollToSection(index) {
            currentIndex = index;
            const slideWidth = window.innerWidth;
            slider.scrollTo({
                left: slideWidth * index,
                behavior: 'smooth'
            });
            updateDots();
        }

        function updateDots() {
            dots.forEach((dot, index) => {
                dot.classList.toggle('active', index === currentIndex);
            });
        }

        // Scroll detection
        slider.addEventListener('scroll', () => {
            clearTimeout(isScrolling);
            isScrolling = setTimeout(() => {
                const slideWidth = window.innerWidth;
                const newIndex = Math.round(slider.scrollLeft / slideWidth);
                if (newIndex !== currentIndex) {
                    currentIndex = newIndex;
                    updateDots();
                }
            }, 50);
        });

        // Keyboard navigation
        document.addEventListener('keydown', (e) => {
            if (e.key === 'ArrowRight' && currentIndex < 3) {
                scrollToSection(currentIndex + 1);
            } else if (e.key === 'ArrowLeft' && currentIndex > 0) {
                scrollToSection(currentIndex - 1);
            }
        });

        // Touch/Swipe support
        let touchStartX = 0;
        let touchEndX = 0;

        slider.addEventListener('touchstart', (e) => {
            touchStartX = e.changedTouches[0].screenX;
        });

        slider.addEventListener('touchend', (e) => {
            touchEndX = e.changedTouches[0].screenX;
            handleSwipe();
        });

        function handleSwipe() {
            const threshold = 50;
            if (touchEndX < touchStartX - threshold && currentIndex < 3) {
                scrollToSection(currentIndex + 1);
            }
            if (touchEndX > touchStartX + threshold && currentIndex > 0) {
                scrollToSection(currentIndex - 1);
            }
        }

        // Music card play effect
        function playEffect(element) {
            element.style.transform = 'scale(0.95)';
            setTimeout(() => {
                element.style.transform = '';
            }, 150);

            // Create floating musical notes
            for (let i = 0; i < 3; i++) {
                setTimeout(() => {
                    const note = document.createElement('div');
                    note.textContent = ['♪', '♫', '♬'][Math.floor(Math.random() * 3)];
                    note.style.position = 'absolute';
                    note.style.fontSize = (1.5 + Math.random()) + 'rem';
                    note.style.color = Math.random() > 0.5 ? '#ff00cc' : '#00ccff';
                    note.style.left = (20 + Math.random() * 60) + '%';
                    note.style.top = '50%';
                    note.style.pointerEvents = 'none';
                    note.style.animation = 'floatNote 1s ease-out forwards';
                    note.style.zIndex = '100';
                    element.style.position = 'relative';
                    element.appendChild(note);
                    setTimeout(() => note.remove(), 1000);
                }, i * 100);
            }
        }

        // Wiggle animation for contact icons
        function wiggle(element) {
            element.style.animation = 'wiggle 0.5s ease-in-out';
            setTimeout(() => {
                element.style.animation = '';
            }, 500);
        }

        // Add floatNote animation
        const style = document.createElement('style');
        style.textContent = `
            @keyframes floatNote {
                0% { transform: translateY(0) scale(0); opacity: 1; }
                100% { transform: translateY(-100px) scale(1.5) rotate(20deg); opacity: 0; }
            }
            @keyframes wiggle {
                0%, 100% { transform: rotate(0deg); }
                25% { transform: rotate(-10deg); }
                75% { transform: rotate(10deg); }
            }
        `;
        document.head.appendChild(style);

        // Drag scroll for music carousel
        const musicCarousel = document.getElementById('musicCarousel');
        let isDown = false;
        let startX;
        let scrollLeft;

        musicCarousel.addEventListener('mousedown', (e) => {
            isDown = true;
            startX = e.pageX - musicCarousel.offsetLeft;
            scrollLeft = musicCarousel.scrollLeft;
        });

        musicCarousel.addEventListener('mouseleave', () => {
            isDown = false;
        });

        musicCarousel.addEventListener('mouseup', () => {
            isDown = false;
        });

        musicCarousel.addEventListener('mousemove', (e) => {
            if (!isDown) return;
            e.preventDefault();
            const x = e.pageX - musicCarousel.offsetLeft;
            const walk = (x - startX) * 2;
            musicCarousel.scrollLeft = scrollLeft - walk;
        });
    </script>
</body>
</html>
```