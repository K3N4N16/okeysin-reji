```html
<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Okey Pişti Batak - Ultra Modern Oyun Platformu</title>
    <style>
        :root {
            --primary-gradient: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
            --accent-red: linear-gradient(45deg, #ff6b6b, #ff8e8e);
            --accent-teal: linear-gradient(45deg, #4ecdc4, #44a08d);
            --accent-blue: linear-gradient(45deg, #45b7d1, #96c93d);
            --glass-bg: rgba(255, 255, 255, 0.1);
            --glass-border: rgba(255, 255, 255, 0.2);
            --shadow-glow: 0 25px 50px rgba(0,0,0,0.25);
            --text-glow: 0 0 30px rgba(255,255,255,0.5);
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background: var(--primary-gradient);
            min-height: 100vh;
            color: #fff;
            overflow-x: hidden;
            position: relative;
        }

        body::before {
            content: '';
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: 
                radial-gradient(circle at 20% 80%, rgba(120,119,198,0.3) 0%, transparent 50%),
                radial-gradient(circle at 80% 20%, rgba(255,119,198,0.3) 0%, transparent 50%),
                radial-gradient(circle at 40% 40%, rgba(120,219,255,0.2) 0%, transparent 50%);
            z-index: -1;
            animation: float 20s ease-in-out infinite;
        }

        @keyframes float {
            0%, 100% { transform: translateY(0) rotate(0deg); }
            33% { transform: translateY(-20px) rotate(1deg); }
            66% { transform: translateY(10px) rotate(-1deg); }
        }

        .particles {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            pointer-events: none;
            z-index: -1;
        }

        .particle {
            position: absolute;
            width: 4px;
            height: 4px;
            background: rgba(255,255,255,0.6);
            border-radius: 50%;
            animation: drift 15s linear infinite;
        }

        @keyframes drift {
            0% { transform: translateY(100vh) scale(0); opacity: 0; }
            10% { opacity: 1; }
            90% { opacity: 1; }
            100% { transform: translateY(-100px) scale(1); opacity: 0; }
        }

        .container {
            max-width: 1400px;
            margin: 0 auto;
            padding: 20px;
            position: relative;
            z-index: 1;
        }

        .header {
            text-align: center;
            background: var(--glass-bg);
            backdrop-filter: blur(20px);
            border: 1px solid var(--glass-border);
            padding: 60px 40px;
            border-radius: 40px;
            box-shadow: var(--shadow-glow);
            margin-bottom: 50px;
            position: relative;
            overflow: hidden;
        }

        .header::before {
            content: '';
            position: absolute;
            top: -50%;
            left: -50%;
            width: 200%;
            height: 200%;
            background: conic-gradient(from 0deg, transparent, rgba(255,255,255,0.1), transparent);
            animation: rotate 4s linear infinite;
        }

        @keyframes rotate {
            100% { transform: rotate(360deg); }
        }

        .header h1 {
            font-size: clamp(2.5rem, 5vw, 4.5rem);
            background: linear-gradient(45deg, #ff6b6b, #4ecdc4, #45b7d1, #f093fb);
            background-size: 300% 300%;
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            margin-bottom: 20px;
            text-shadow: var(--text-glow);
            animation: shimmer 3s ease-in-out infinite;
            letter-spacing: 0.1em;
        }

        @keyframes shimmer {
            0%, 100% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
        }

        .header p {
            font-size: 1.4rem;
            opacity: 0.9;
            max-width: 600px;
            margin: 0 auto;
        }

        .games-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(380px, 1fr));
            gap: 40px;
            margin-bottom: 60px;
        }

        .game-card {
            background: var(--glass-bg);
            backdrop-filter: blur(25px);
            border: 1px solid var(--glass-border);
            border-radius: 30px;
            padding: 40px;
            box-shadow: var(--shadow-glow);
            transition: all 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            position: relative;
            overflow: hidden;
            transform-style: preserve-3d;
        }

        .game-card::before {
            content: '';
            position: absolute;
            inset: 0;
            background: var(--primary-gradient);
            opacity: 0;
            transition: opacity 0.5s;
            z-index: -1;
        }

        .game-card:hover::before {
            opacity: 0.1;
        }

        .game-card:hover {
            transform: translateY(-20px) rotateX(5deg) rotateY(5deg) scale(1.05);
            box-shadow: 0 50px 100px rgba(0,0,0,0.4);
            border-color: rgba(255,255,255,0.4);
        }

        .game-icon {
            font-size: 6rem;
            text-align: center;
            margin-bottom: 25px;
            filter: drop-shadow(0 10px 20px rgba(0,0,0,0.3));
            transition: all 0.4s ease;
        }

        .game-card:hover .game-icon {
            transform: scale(1.2) rotate(360deg);
            filter: drop-shadow(0 0 40px currentColor);
        }

        .okey .game-icon { color: #ff6b6b; }
        .pisti .game-icon { color: #4ecdc4; }
        .batak .game-icon { color: #45b7d1; }

        .game-title {
            font-size: 2.5rem;
            text-align: center;
            margin-bottom: 20px;
            background: linear-gradient(45deg, #fff, rgba(255,255,255,0.8));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-weight: 700;
        }

        .game-description {
            line-height: 1.8;
            margin-bottom: 25px;
            opacity: 0.9;
        }

        .features {
            list-style: none;
            margin-bottom: 30px;
        }

        .features li {
            padding: 12px 0;
            padding-left: 35px;
            position: relative;
            font-size: 1.15rem;
            opacity: 0.95;
            transition: color 0.3s;
        }

        .features li::before {
            content: '✨';
            position: absolute;
            left: 0;
            font-size: 1.4rem;
            animation: sparkle 2s infinite;
        }

        @keyframes sparkle {
            0%, 100% { transform: scale(1) rotate(0deg); opacity: 1; }
            50% { transform: scale(1.2) rotate(180deg); opacity: 0.7; }
        }

        .play-btn {
            display: block;
            width: 100%;
            background: var(--accent-red);
            color: white;
            padding: 20px;
            border: none;
            border-radius: 50px;
            font-size: 1.4rem;
            font-weight: 700;
            cursor: pointer;
            transition: all 0.4s ease;
            position: relative;
            overflow: hidden;
            box-shadow: 0 15px 35px rgba(255,107,107,0.4);
        }

        .play-btn::before {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255,255,255,0.4), transparent);
            transition: left 0.5s;
        }

        .play-btn:hover::before {
            left: 100%;
        }

        .play-btn:hover {
            transform: translateY(-5px) scale(1.05);
            box-shadow: 0 25px 50px rgba(255,107,107,0.6);
        }

        .okey .play-btn { background: var(--accent-red); }
        .pisti .play-btn { background: var(--accent-teal); }
        .batak .play-btn { background: var(--accent-blue); }

        .demo-area {
            background: rgba(0,0,0,0.1);
            border-radius: 25px;
            padding: 30px;
            margin-top: 30px;
            position: relative;
            overflow: hidden;
        }

        .demo-area::after {
            content: '';
            position: absolute;
            inset: 0;
            background: radial-gradient(circle, rgba(255,255,255,0.1) 0%, transparent 70%);
            animation: pulse 3s ease-in-out infinite;
        }

        @keyframes pulse {
            0%, 100% { opacity: 0.5; transform: scale(1); }
            50% { opacity: 1; transform: scale(1.05); }
        }

        .demo-cards, .okey-tiles {
            display: flex;
            justify-content: center;
            gap: 15px;
            flex-wrap: wrap;
            margin-top: 20px;
            perspective: 1000px;
        }

        .card, .okey-tile {
            transition: all 0.5s cubic-bezier(0.68, -0.55, 0.265, 1.55);
            cursor: pointer;
            position: relative;
        }

        .card {
            width: 70px;
            height: 100px;
            background: linear-gradient(145deg, #fff, #f0f0f0);
            border-radius: 15px;
            box-shadow: 0 10px 25px rgba(0,0,0,0.3);
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.8rem;
            font-weight: bold;
            transform-style: preserve-3d;
        }

        .card:hover {
            transform: translateY(-15px) rotateY(180deg) rotateX(10deg);
            box-shadow: 0 25px 50px rgba(0,0,0,0.4);
        }

        .card.suit-hearts { color: #ff4757; }
        .card.suit-diamonds { color: #ffa502; }
        .card.suit-clubs, .card.suit-spades { color: #2f3542; }

        .okey-tile {
            width: 60px;
            height: 85px;
            background: linear-gradient(145deg, #f8f9fa, #e9ecef);
            border-radius: 12px;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            font-weight: bold;
            font-size: 1rem;
            box-shadow: 0 8px 25px rgba(0,0,0,0.3);
            position: relative;
        }

        .okey-tile::after {
            content: '🀄';
            font-size: 1.8rem;
            position: absolute;
            top: 8px;
            right: 8px;
            opacity: 0.8;
        }

        .okey-tile:hover {
            transform: translateY(-12px) rotateZ(5deg);
        }

        .stats {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
            gap: 30px;
            margin-top: 60px;
            margin-bottom: 60px;
        }

        .stat-card {
            background: var(--glass-bg);
            backdrop-filter: blur(20px);
            border: 1px solid var(--glass-border);
            padding: 35px 25px;
            border-radius: 25px;
            text-align: center;
            box-shadow: var(--shadow-glow);
            transition: transform 0.4s ease;
        }

        .stat-card:hover {
            transform: translateY(-10px) scale(1.05);
        }

        .stat-number {
            font-size: 3rem;
            font-weight: 800;
            background: linear-gradient(45deg, #fff, #4ecdc4);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 10px;
        }

        .footer {
            text-align: center;
            padding: 50px 30px;
            background: var(--glass-bg);
            backdrop-filter: blur(20px);
            border: 1px solid var(--glass-border);
            border-radius: 30px;
            box-shadow: var(--shadow-glow);
        }

        .footer h3 {
            font-size: 2rem;
            margin-bottom: 15px;
            background: linear-gradient(45deg, #fff, rgba(255,255,255,0.8));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        @media (max-width: 768px) {
            .games-grid { grid-template-columns: 1fr; gap: 30px; }
            .game-card { padding: 30px 25px; }
            .header { padding: 40px 20px; }
            .card { width: 55px; height: 80px; font-size: 1.4rem; }
            .okey-tile { width: 50px; height: 70px; }
        }

        @media (max-width: 480px) {
            .container { padding: 15px; }
        }
    </style>
</head>
<body>
    <canvas class="particles" id="particles"></canvas>
    <div class="container">
        <div class="header">
            <h1>🃏 OKEY • PİŞTİ • BATAK 🂡</h1>
            <p>🔥 Ultra modern tasarım, gelişmiş grafikler ve sürükleyici oyun deneyimi! Türkiye'nin favori kart & taş oyunları tek tıkla!</p>
        </div>

        <div class="games-grid">
            <div class="game-card okey">
                <div class="game-icon">🀄</div>
                <div class="game-title">Okey</div>
                <div class="game-description">
                    106 taş, 4 renk, strateji dolu seriler! AI rakip, turnuvalar ve gerçekçi animasyonlar.
                </div>
                <ul class="features">
                    <li>3D taş animasyonları</li>
                    <li>Çevrimiçi multiplayer</li>
                    <li>Günlük challenge'lar</li>
                    <li>Custom masalar</li>
                </ul>
                <button class="play-btn">Okey Oyna 🚀</button>
                <div class="demo-area">
                    <div class="okey-tiles">
                        <div class="okey-tile">1🔴</div>
                        <div class="okey-tile">5🔵</div>
                        <div class="okey-tile">9🟡</div>
                        <div class="okey-tile">12🟢</div>
                    </div>
                </div>
            </div>

            <div class="game-card pisti">
                <div class="game-icon">♥️</div>
                <div class="game-title">Pişti</div>
                <div class="game-description">
                    Pişti yakala, bonus topla! 36 kartlık hızlı tempo, zorluk seviyeleriyle zeka testi.
                </div>
                <ul class="features">
                    <li>Triple Pişti x3 puan</li>
                    <li>AI & arkadaş modu</li>
                    <li>Lider tabloları</li>
                    <li>Kart efektleri</li>
                </ul>
                <button class="play-btn">Pişti Oyna 💥</button>
                <div class="demo-area">
                    <div class="demo-cards">
                        <div class="card suit-hearts">10</div>
                        <div class="card suit-diamonds">♠️</div>
                        <div class="card suit-hearts">10</div>
                    </div>
                </div>
            </div>

            <div class="game-card batak">
                <div class="game-icon">♠️</div>
                <div class="game-title">Batak</div>
                <div class="game-description">
                    İhale, koz, gömme! 4 kişilik eşli strateji, klasik & varyasyon modları.
                </div>
                <ul class="features">
                    <li>Gömmeli & Koz Maça</li>
                    <li>Eşli takım oyunu</li>
                    <li>Detaylı istatistik</li>
                    <li>Turnuva ligi</li>
                </ul>
                <button class="play-btn">Batak Oyna ⚡</button>
                <div class="demo-area">
                    <div class="demo-cards">
                        <div class="card suit-spades">A</div>
                        <div class="card suit-spades">K</div>
                        <div class="card suit-spades">Q</div>
                        <div class="card suit-spades">J</div>
                    </div>
                </div>
            </div>
        </div>

        <div class="stats">
            <div class="stat-card">
                <div class="stat-number">2M+</div>
                <div>Aktif Oyuncu</div>
            </div>
            <div class="stat-card">
                <div class="stat-number">1M+</div>
                <div>Günlük Parti</div>
            </div>
            <div class="stat-card">
                <div class="stat-number">99.9%</div>
                <div>Upscale Grafik</div>
            </div>
            <div class="stat-card">
                <div class="stat-number">100%</div>
                <div>Mobil Uyumlu</div>
            </div>
        </div>

        <div class="footer">
            <h3>🎮 Ultra HD, Gerçek Zamanlı, Sonsuz Eğlence! 🎮</h3>
            <p>PC • Mobil • Ücretsiz • Anında Oyna</p>
        </div>
    </div>

    <script>
        // Particle system
        const canvas = document.getElementById('particles');
        const ctx = canvas.getContext('2d');
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;

        window.addEventListener('resize', () => {
            canvas.width = window.innerWidth;
            canvas.height = window.innerHeight;
        });

        function createParticles() {
            const particles = [];
            for (let i = 0; i < 50; i++) {
                const particle = document.createElement('div');
                particle.className = 'particle';
                particle.style.left = Math.random() * 100 + '%';
                particle.style.animationDelay = Math.random() * 15 + 's';
                particle.style.animationDuration = (Math.random() * 10 + 10) + 's';
                document.body.appendChild(particle);
            }
        }
        createParticles();

        // Button interactions with confetti-like effect (canvas bursts)
        document.querySelectorAll('.play-btn').forEach((btn, index) => {
            btn.addEventListener('click', (e) => {
                e.preventDefault();
                btn.style.transform = 'scale(0.95)';
                setTimeout(() => {
                    btn.style.transform = '';
                    const gameNames = ['Okey', 'Pişti', 'Batak'];
                    alert(`🎉 ${gameNames[index]} yükleniyor... Ultra modern mod aktif! 🚀`);
                }, 200);

                // Simple burst effect
                for (let i = 0; i < 20; i++) {
                    const burst = document.createElement('div');
                    burst.style.position = 'fixed';
                    burst.style.left = e.clientX + 'px';
                    burst.style.top = e.clientY + 'px';
                    burst.style.width = '6px';
                    burst.style.height = '6px';
                    burst.style.background = ['#ff6b6b', '#4ecdc4', '#45b7d1'][index % 3];
                    burst.style.borderRadius = '50%';
                    burst.style.pointerEvents = 'none';
                    burst.style.zIndex = '9999';
                    document.body.appendChild(burst);

                    const angle = (i / 20) * Math.PI * 2;
                    const vel = 200 + Math.random() * 100;
                    burst.animate([
                        { transform: 'translate(0, 0) scale(1)', opacity: 1 },
                        { transform: `translate(${Math.cos(angle) * vel}px, ${Math.sin(angle) * vel}px) scale(0)`, opacity: 0 }
                    ], {
                        duration: 800,
                        easing: 'cubic-bezier(0.25, 0.46, 0.45, 0.94)'
                    }).onfinish = () => burst.remove();
                }
            });
        });

        // Enhanced card/tile interactions
        document.querySelectorAll('.card, .okey-tile').forEach(el => {
            el.addEventListener('mouseenter', () => {
                el.style.filter = 'brightness(1.3) drop-shadow(0 0 20px currentColor)';
            });
            el.addEventListener('mouseleave', () => {
                el.style.filter = '';
            });
        });

        // Parallax scroll
        window.addEventListener('scroll', () => {
            const scrolled = window.pageYOffset;
            document.querySelector('.header').style.transform = `translateY(${scrolled * 0.3}px)`;
            document.querySelectorAll('.game-card').forEach((card, i) => {
                card.style.transform += `translateY(${scrolled * 0.1 * (i + 1)}px)`;
            });
        });

        // Smooth reveal on load
        document.addEventListener('DOMContentLoaded', () => {
            document.body.style.opacity = '0';
            document.body.style.transition = 'opacity 1s ease';
            setTimeout(() => {
                document.body.style.opacity = '1';
            }, 100);
        });
    </script>
</body>
</html>
```