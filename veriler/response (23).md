```html
<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>🃏 OKEY • PİŞTİ • BATAK 🂡 - Ultra Modern Oyun Platformu</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700;800&display=swap');
        
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Poppins', sans-serif;
            background: linear-gradient(-45deg, #ee7752, #e73c7e, #23a6d5, #23d5ab);
            background-size: 400% 400%;
            animation: gradientBG 15s ease infinite;
            min-height: 100vh;
            color: #fff;
            overflow-x: hidden;
            position: relative;
        }

        @keyframes gradientBG {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
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
            0%, 100% { transform: translateY(0px) rotate(0deg); }
            50% { transform: translateY(-20px) rotate(1deg); }
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
            background: rgba(255,255,255,0.1);
            backdrop-filter: blur(25px);
            border-radius: 40px;
            padding: 60px 40px;
            box-shadow: 0 30px 80px rgba(0,0,0,0.3);
            margin-bottom: 50px;
            border: 1px solid rgba(255,255,255,0.2);
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
            background: conic-gradient(transparent, rgba(255,255,255,0.1), transparent);
            animation: rotate 20s linear infinite;
        }

        @keyframes rotate {
            100% { transform: rotate(360deg); }
        }

        .header h1 {
            font-size: clamp(2.5em, 8vw, 6em);
            font-weight: 800;
            background: linear-gradient(45deg, #fff, #f0f0f0, #e0e0e0);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            margin-bottom: 20px;
            text-shadow: 0 0 50px rgba(255,255,255,0.5);
            animation: glowText 3s ease-in-out infinite alternate;
        }

        @keyframes glowText {
            from { filter: drop-shadow(0 0 20px #fff) drop-shadow(0 0 40px #fff); }
            to { filter: drop-shadow(0 0 30px #fff) drop-shadow(0 0 60px #fff); }
        }

        .header p {
            font-size: clamp(1.1em, 3vw, 1.5em);
            font-weight: 300;
            opacity: 0.9;
            letter-spacing: 1px;
        }

        .games-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(380px, 1fr));
            gap: 40px;
            margin-bottom: 60px;
        }

        .game-card {
            background: rgba(255,255,255,0.15);
            backdrop-filter: blur(30px);
            border-radius: 30px;
            padding: 40px 30px;
            box-shadow: 0 35px 100px rgba(0,0,0,0.3);
            transition: all 0.5s cubic-bezier(0.25, 0.46, 0.45, 0.94);
            position: relative;
            border: 1px solid rgba(255,255,255,0.2);
            overflow: hidden;
        }

        .game-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 4px;
            background: linear-gradient(90deg, #ff6b6b, #4ecdc4, #45b7d1, #ffd93d);
            border-radius: 30px 30px 0 0;
        }

        .game-card:hover {
            transform: translateY(-25px) scale(1.05);
            box-shadow: 0 50px 150px rgba(0,0,0,0.4);
            border-color: rgba(255,255,255,0.4);
        }

        .game-icon {
            font-size: clamp(4em, 15vw, 7em);
            text-align: center;
            margin-bottom: 25px;
            filter: drop-shadow(0 15px 30px rgba(0,0,0,0.3));
            position: relative;
        }

        .game-icon::after {
            content: '';
            position: absolute;
            top: -20px;
            left: 50%;
            transform: translateX(-50%);
            width: 80px;
            height: 80px;
            background: radial-gradient(circle, rgba(255,255,255,0.3) 0%, transparent 70%);
            border-radius: 50%;
            animation: pulse 2s infinite;
        }

        @keyframes pulse {
            0% { transform: translateX(-50%) scale(0.8); opacity: 1; }
            100% { transform: translateX(-50%) scale(1.2); opacity: 0; }
        }

        .okey .game-icon { text-shadow: 0 0 40px #ff6b6b; }
        .pisti .game-icon { text-shadow: 0 0 40px #4ecdc4; }
        .batak .game-icon { text-shadow: 0 0 40px #45b7d1; }

        .game-title {
            font-size: clamp(1.8em, 5vw, 2.8em);
            text-align: center;
            margin-bottom: 20px;
            font-weight: 700;
            background: linear-gradient(45deg, #fff, rgba(255,255,255,0.8));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        .game-description {
            line-height: 1.8;
            margin-bottom: 30px;
            color: rgba(255,255,255,0.95);
            font-weight: 300;
            text-align: center;
        }

        .features {
            list-style: none;
            margin-bottom: 30px;
        }

        .features li {
            padding: 15px 0;
            padding-left: 45px;
            position: relative;
            font-size: 1.1em;
            opacity: 0.9;
            transition: all 0.3s ease;
        }

        .features li:hover {
            transform: translateX(10px);
            opacity: 1;
        }

        .features li::before {
            content: '✨';
            position: absolute;
            left: 0;
            font-size: 1.4em;
            animation: sparkle 2s infinite;
        }

        @keyframes sparkle {
            0%, 100% { transform: scale(1) rotate(0deg); }
            50% { transform: scale(1.2) rotate(180deg); }
        }

        .play-btn {
            display: block;
            width: 100%;
            background: linear-gradient(45deg, #fff, #f0f0f0);
            color: #333;
            padding: 22px;
            border: none;
            border-radius: 50px;
            font-size: 1.4em;
            font-weight: 700;
            cursor: pointer;
            transition: all 0.4s ease;
            text-decoration: none;
            text-align: center;
            box-shadow: 0 20px 50px rgba(255,255,255,0.3);
            position: relative;
            overflow: hidden;
            letter-spacing: 1px;
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
            transform: translateY(-5px) scale(1.02);
            box-shadow: 0 30px 70px rgba(255,255,255,0.4);
        }

        .demo-area {
            background: rgba(255,255,255,0.1);
            border-radius: 20px;
            padding: 30px;
            margin-top: 30px;
            border: 1px solid rgba(255,255,255,0.2);
        }

        .demo-title {
            text-align: center;
            font-size: 1.2em;
            margin-bottom: 20px;
            font-weight: 500;
        }

        .demo-cards {
            display: flex;
            justify-content: center;
            gap: 20px;
            flex-wrap: wrap;
        }

        .card {
            width: 70px;
            height: 100px;
            background: linear-gradient(145deg, #fff, #f8f9fa);
            border-radius: 15px;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            font-size: 1.8em;
            font-weight: 800;
            box-shadow: 0 15px 40px rgba(0,0,0,0.3);
            transition: all 0.4s ease;
            position: relative;
            border: 2px solid rgba(255,255,255,0.3);
        }

        .card:hover {
            transform: translateY(-15px) rotateY(15deg);
            box-shadow: 0 25px 60px rgba(0,0,0,0.4);
        }

        .suit-symbol {
            position: absolute;
            font-size: 0.8em;
            top: 5px;
            right: 5px;
        }

        .okey-tiles {
            display: flex;
            gap: 15px;
            justify-content: center;
            flex-wrap: wrap;
        }

        .okey-tile {
            width: 65px;
            height: 90px;
            background: linear-gradient(145deg, rgba(255,255,255,0.9), rgba(240,240,240,0.8));
            border-radius: 12px;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            font-weight: 700;
            font-size: 1.1em;
            box-shadow: 0 12px 35px rgba(0,0,0,0.3);
            position: relative;
            transition: all 0.4s ease;
            border: 2px solid rgba(255,255,255,0.5);
        }

        .okey-tile:hover {
            transform: translateY(-10px) scale(1.05);
        }

        .okey-tile::after {
            content: '🀄';
            font-size: 1.8em;
            position: absolute;
            top: 8px;
            right: 8px;
            opacity: 0.7;
        }

        .stats {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
            gap: 30px;
            margin: 60px 0;
        }

        .stat-card {
            background: rgba(255,255,255,0.15);
            backdrop-filter: blur(25px);
            padding: 35px 25px;
            border-radius: 25px;
            text-align: center;
            border: 1px solid rgba(255,255,255,0.2);
            transition: all 0.4s ease;
        }

        .stat-card:hover {
            transform: translateY(-10px);
            box-shadow: 0 30px 80px rgba(0,0,0,0.3);
        }

        .stat-number {
            font-size: clamp(2em, 6vw, 3.5em);
            font-weight: 800;
            background: linear-gradient(45deg, #fff, #f0f0f0);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 10px;
        }

        .particles {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            pointer-events: none;
            z-index: 0;
        }

        .particle {
            position: absolute;
            width: 4px;
            height: 4px;
            background: rgba(255,255,255,0.6);
            border-radius: 50%;
            animation: floatParticle 25s infinite linear;
        }

        @keyframes floatParticle {
            0% {
                transform: translateY(100vh) rotate(0deg);
                opacity: 0;
            }
            10% {
                opacity: 1;
            }
            90% {
                opacity: 1;
            }
            100% {
                transform: translateY(-100px) rotate(360deg);
                opacity: 0;
            }
        }

        .footer {
            text-align: center;
            padding: 60px 30px;
            background: rgba(0,0,0,0.2);
            backdrop-filter: blur(25px);
            border-radius: 30px;
            margin-top: 60px;
            border: 1px solid rgba(255,255,255,0.1);
            font-weight: 300;
        }

        .footer h3 {
            font-size: 2em;
            margin-bottom: 15px;
            font-weight: 700;
        }

        @media (max-width: 768px) {
            .games-grid { grid-template-columns: 1fr; gap: 30px; }
            .header { padding: 40px 20px; }
            .demo-cards .card { width: 55px; height: 80px; font-size: 1.3em; }
            .stats { grid-template-columns: repeat(2, 1fr); }
        }

        @media (max-width: 480px) {
            .stats { grid-template-columns: 1fr; }
        }
    </style>
</head>
<body>
    <div class="particles" id="particles"></div>
    
    <div class="container">
        <div class="header">
            <h1>🃏 OKEY • PİŞTİ • BATAK 🂡</h1>
            <p>🌟 2026'nın En Modern Oyun Platformu | Ultra Görsel Deneyim | Gerçek Zamanlı Rekabet</p>
        </div>

        <div class="games-grid">
            <div class="game-card okey">
                <div class="game-icon">🀄</div>
                <h2 class="game-title">Okey Ustası</h2>
                <p class="game-description">106 renkli taşla stratejik zeka oyunu. Gerçekçi fizik, gelişmiş AI ve canlı turnuvalar ile unutulmaz deneyim.</p>
                <ul class="features">
                    <li>4D taş animasyonları & fizik motoru</li>
                    <li>Global liderlik tablosu</li>
                    <li>Canlı ses efektleri</li>
                    <li>Özel oda sistemi</li>
                </ul>
                <a href="#" class="play-btn">🚀 OKEY OYNA</a>
                <div class="demo-area">
                    <div class="demo-title">Canlı Taşlar ✨</div>
                    <div class="okey-tiles">
                        <div class="okey-tile">1🔴</div>
                        <div class="okey-tile">7🔵</div>
                        <div class="okey-tile">12🟡</div>
                        <div class="okey-tile">4🟢</div>
                        <div class="okey-tile">🀄</div>
                    </div>
                </div>
            </div>

            <div class="game-card pisti">
                <div class="game-icon">♥️♦️</div>
                <h2 class="game-title">Pişti Efsanesi</h2>
                <p class="game-description">36 kartlık hızlı tempolu kağıt oyunu. Pişti bonusları, çift skorlar ve AI rakiple kesintisiz eğlence.</p>
                <ul class="features">
                    <li>Yüksek kaliteli kart grafikleri</li>
                    <li>3 zorluk seviyesi AI</li>
                    <li>Haftalık turnuvalar</li>
                    <li>Arkadaş daveti</li>
                </ul>
                <a href="#" class="play-btn">💎 PİŞTİ OYNA</a>
                <div class="demo-area">
                    <div class="demo-title">Pişti Anı 🔥</div>
                    <div class="demo-cards">
                        <div class="card suit-hearts">
                            <span class="suit-symbol">♥</span>10
                        </div>
                        <div class="card suit-diamonds">
                            <span class="suit-symbol">♦</span>♠
                        </div>
                        <div class="card suit-hearts">
                            <span class="suit-symbol">♥</span>10
                        </div>
                    </div>
                </div>
            </div>

            <div class="game-card batak">
                <div class="game-icon">♠️♣️</div>
                <h2 class="game-title">Batak İmparatoru</h2>
                <p class="game-description">4 kişilik ihale sistemi, gömmeli & koz maça modları. Profesyonel turnuva deneyimi ve detaylı istatistikler.</p>
                <ul class="features">
                    <li>Eşli 4 kişilik masa</li>
                    <li>3 farklı Batak modu</li>
                    <li>Canlı skor takibi</li>
                    <li>Turnuva şampiyonası</li>
                </ul>
                <a href="#" class="play-btn">👑 BATAK OYNA</a>
                <div class="demo-area">
                    <div class="demo-title">Koz Sırası ⚡</div>
                    <div class="demo-cards">
                        <div class="card suit-spades">
                            <span class="suit-symbol">♠</span>A
                        </div>
                        <div class="card suit-spades">
                            <span class="suit-symbol">♠</span>K
                        </div>
                        <div class="card suit-spades">
                            <span class="suit-symbol">♠</span>Q
                        </div>
                        <div class="card suit-spades">
                            <span class="suit-symbol">♠</span>J
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <div class="stats">
            <div class="stat-card">
                <div class="stat-number">2.5M+</div>
                <div>Mutlu Oyuncu</div>
            </div>
            <div class="stat-card">
                <div class="stat-number">1K+</div>
                <div>Günlük Turnuva</div>
            </div>
            <div class="stat-card">
                <div class="stat-number">99.9%</div>
                <div>Bağlantı Başarı</div>
            </div>
            <div class="stat-card">
                <div class="stat-number">🇹🇷 #1</div>
                <div>Oyun Platformu</div>
            </div>
        </div>

        <div class="footer">
            <h3>🎮 Anında Oyna • Hiç Durma • Zirveye Çık! 🎮</h3>
            <p>📱 Mobil Uyumlu | ⚡ Hızlı Yükleme | 🆓 Tamamen Ücretsiz | 🌍 Global Sunucular</p>
        </div>
    </div>

    <script>
        // Parçacık sistemi
        function createParticles() {
            const particlesContainer = document.getElementById('particles');
            for (let i = 0; i < 50; i++) {
                const particle = document.createElement('div');
                particle.className = 'particle';
                particle.style.left = Math.random() * 100 + '%';
                particle.style.animationDelay = Math.random() * 25 + 's';
                particle.style.animationDuration = (Math.random() * 10 + 15) + 's';
                particlesContainer.appendChild(particle);
            }
        }

        // Buton efektleri
        document.querySelectorAll('.play-btn').forEach(btn => {
            btn.addEventListener('click', (e) => {
                e.preventDefault();
                btn.innerHTML = '🎯 YÜKLENİYOR...';
                btn.style.background = 'linear-gradient(45deg, #4ecdc4, #45b7d1)';
                btn.style.color = '#fff';
                
                setTimeout(() => {
                    alert('🎉 Oyun başarıyla başlatıldı! Modern deneyim başlıyor... ✨');
                    location.reload();
                }, 1500);
            });
        });

        // Kart 3D hover efektleri
        document.querySelectorAll('.card, .okey-tile').forEach(card => {
            card.addEventListener('mousemove', (e) => {
                const rect = card.getBoundingClientRect();
                const x = e.clientX - rect.left;
                const y = e.clientY - rect.top;
                const centerX = rect.width / 2;
                const centerY = rect.height / 2;
                const rotateX = (y - centerY) / 10;
                const rotateY = (centerX - x) / 10;
                
                card.style.transform = `perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) translateY(-10px)`;
            });
            
            card.addEventListener('mouseleave', () => {
                card.style.transform = 'translateY(0) rotateX(0deg) rotateY(0deg)';
            });
        });

        // Scroll parallax
        window.addEventListener('scroll', () => {
            const scrolled = window.pageYOffset;
            document.querySelector('.header').style.transform = `translateY(${scrolled * 0.3}px)`;
            document.querySelectorAll('.game-card').forEach((card, index) => {
                const speed = 0.2 + (index * 0.1);
                card.style.transform += `translateY(${scrolled * speed}px)`;
            });
        });

        // Sayfa yüklendiğinde parçacıkları oluştur
        window.addEventListener('load', createParticles);

        // Mouse takip efekti
        document.addEventListener('mousemove', (e) => {
            const cursor = document.createElement('div');
            cursor.style.position = 'fixed';
            cursor.style.width = '6px';
            cursor.style.height = '6px';
            cursor.style.background = 'rgba(255,255,255,0.8)';
            cursor.style.borderRadius = '50%';
            cursor.style.pointerEvents = 'none';
            cursor.style.zIndex = '9999';
            cursor.style.left = e.clientX - 3 + 'px';
            cursor.style.top = e.clientY - 3 + 'px';
            cursor.style.transition = 'all 0.1s ease';
            document.body.appendChild(cursor);
            
            setTimeout(() => cursor.remove(), 100);
        });
    </script>
</body>
</html>
```

## Sources

1.https://ankarawebtasarim.net.tr/modern-tasarimli-web-sitesi-ornekleri-ilham-veren-10-tasarim/
2.https://iselbiselerifirmalari.com.tr/modern-web-sitesi-tasarim-ornekleri/
