```html
<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Okey Pişti Batak - Gelişmiş Oyun Platformu</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Arial', sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            color: #333;
            overflow-x: hidden;
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
        }

        .header {
            text-align: center;
            background: rgba(255,255,255,0.95);
            padding: 30px;
            border-radius: 20px;
            box-shadow: 0 20px 40px rgba(0,0,0,0.2);
            margin-bottom: 30px;
            backdrop-filter: blur(10px);
        }

        .header h1 {
            font-size: 3em;
            background: linear-gradient(45deg, #ff6b6b, #4ecdc4, #45b7d1);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            margin-bottom: 10px;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
        }

        .header p {
            font-size: 1.3em;
            color: #666;
        }

        .games-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
            gap: 30px;
            margin-bottom: 40px;
        }

        .game-card {
            background: rgba(255,255,255,0.95);
            border-radius: 25px;
            padding: 30px;
            box-shadow: 0 25px 50px rgba(0,0,0,0.15);
            transition: all 0.4s ease;
            position: relative;
            overflow: hidden;
            backdrop-filter: blur(10px);
            border: 2px solid transparent;
        }

        .game-card:hover {
            transform: translateY(-15px) scale(1.02);
            box-shadow: 0 35px 70px rgba(0,0,0,0.25);
            border-color: #4ecdc4;
        }

        .game-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 5px;
            background: linear-gradient(90deg, #ff6b6b, #4ecdc4, #45b7d1);
        }

        .game-icon {
            font-size: 5em;
            text-align: center;
            margin-bottom: 20px;
            filter: drop-shadow(0 5px 10px rgba(0,0,0,0.2));
        }

        .okey .game-icon { color: #ff6b6b; }
        .pisti .game-icon { color: #4ecdc4; }
        .batak .game-icon { color: #45b7d1; }

        .game-title {
            font-size: 2.2em;
            text-align: center;
            margin-bottom: 15px;
            color: #333;
            font-weight: bold;
        }

        .game-description {
            line-height: 1.7;
            margin-bottom: 20px;
            color: #555;
        }

        .features {
            list-style: none;
        }

        .features li {
            padding: 10px 0;
            padding-left: 30px;
            position: relative;
            font-size: 1.1em;
        }

        .features li::before {
            content: '✨';
            position: absolute;
            left: 0;
            font-size: 1.2em;
        }

        .play-btn {
            display: block;
            width: 100%;
            background: linear-gradient(45deg, #ff6b6b, #ff8e8e);
            color: white;
            padding: 18px;
            border: none;
            border-radius: 50px;
            font-size: 1.3em;
            font-weight: bold;
            cursor: pointer;
            transition: all 0.3s ease;
            text-decoration: none;
            text-align: center;
            box-shadow: 0 10px 30px rgba(255,107,107,0.4);
        }

        .play-btn:hover {
            transform: translateY(-3px);
            box-shadow: 0 15px 40px rgba(255,107,107,0.6);
        }

        .okey .play-btn { background: linear-gradient(45deg, #ff6b6b, #ff8e8e); }
        .pisti .play-btn { background: linear-gradient(45deg, #4ecdc4, #6bd4cc); }
        .batak .play-btn { background: linear-gradient(45deg, #45b7d1, #6bc8e0); }

        .demo-area {
            background: rgba(0,0,0,0.05);
            border-radius: 20px;
            padding: 25px;
            margin-top: 30px;
            text-align: center;
        }

        .demo-cards {
            display: flex;
            justify-content: center;
            gap: 15px;
            flex-wrap: wrap;
            margin-top: 20px;
        }

        .card {
            width: 60px;
            height: 90px;
            background: white;
            border-radius: 12px;
            box-shadow: 0 8px 20px rgba(0,0,0,0.2);
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.6em;
            font-weight: bold;
            position: relative;
            transition: all 0.3s ease;
        }

        .card:hover {
            transform: translateY(-5px) rotate(5deg);
            box-shadow: 0 15px 35px rgba(0,0,0,0.3);
        }

        .card.suit-hearts { color: #ff4757; }
        .card.suit-diamonds { color: #ffa502; }
        .card.suit-clubs { color: #2f3542; }
        .card.suit-spades { color: #2f3542; }

        .okey-tiles {
            display: flex;
            gap: 10px;
            justify-content: center;
            margin-top: 15px;
        }

        .okey-tile {
            width: 50px;
            height: 70px;
            background: linear-gradient(145deg, #f8f9fa, #e9ecef);
            border-radius: 8px;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            font-weight: bold;
            font-size: 0.9em;
            box-shadow: 0 5px 15px rgba(0,0,0,0.2);
            position: relative;
        }

        .okey-tile::after {
            content: '🀄';
            font-size: 1.5em;
            position: absolute;
            top: 5px;
            right: 5px;
        }

        .stats {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
            margin-top: 40px;
        }

        .stat-card {
            background: rgba(255,255,255,0.9);
            padding: 25px;
            border-radius: 20px;
            text-align: center;
            box-shadow: 0 15px 35px rgba(0,0,0,0.1);
        }

        .stat-number {
            font-size: 2.5em;
            font-weight: bold;
            background: linear-gradient(45deg, #4ecdc4, #45b7d1);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        .footer {
            text-align: center;
            padding: 40px 20px;
            color: rgba(255,255,255,0.9);
            background: rgba(0,0,0,0.2);
            border-radius: 20px;
            margin-top: 40px;
            backdrop-filter: blur(10px);
        }

        @media (max-width: 768px) {
            .header h1 { font-size: 2em; }
            .games-grid { grid-template-columns: 1fr; }
            .game-card { padding: 20px; }
            .demo-cards .card { width: 50px; height: 75px; font-size: 1.2em; }
        }

        @keyframes glow {
            0%, 100% { box-shadow: 0 0 20px rgba(255,255,255,0.5); }
            50% { box-shadow: 0 0 40px rgba(255,255,255,0.8); }
        }

        .header:hover { animation: glow 2s infinite; }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🃏 OKey • Pişti • Batak 🂡</h1>
            <p>Gelişmiş modern tasarım ile Türkiye'nin en sevilen oyunları tek platformda!</p>
        </div>

        <div class="games-grid">
            <div class="game-card okey">
                <div class="game-icon">🀄</div>
                <div class="game-title">Okey Oyunu</div>
                <div class="game-description">
                    Geleneksel Türk Okey oyununun modern versiyonu. 106 taşla oynanan bu strateji oyunu, 
                    en hızlı serileri tamamlayarak kazanma heyecanı sunar. Renkli taşlar ve gelişmiş AI rakip.
                </div>
                <ul class="features">
                    <li>Gerçekçi taş animasyonları</li>
                    <li>Çevrimiçi çok oyunculu mod</li>
                    <li>Turnuva sistemi</li>
                    <li>Günlük bonuslar</li>
                </ul>
                <a href="#" class="play-btn">Okey Oyna ➤</a>
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
                <div class="game-title">Pişti Oyunu</div>
                <div class="game-description">
                    Efsanevi Pişti oyunu! Aynı sayıdaki kartları toplayarak en yüksek puanı hedefleyin. 
                    36 kartlık deste ile hızlı tempolu, zeka dolu bir kart oyunu deneyimi.
                </div>
                <ul class="features">
                    <li>Pişti bonusları</li>
                    <li>AI zorluk seviyeleri</li>
                    <li>Skor tabloları</li>
                    <li>Çift kişilik mod</li>
                </ul>
                <a href="#" class="play-btn">Pişti Oyna ➤</a>
                <div class="demo-area">
                    <div class="demo-cards">
                        <div class="card suit-hearts">10</div>
                        <div class="card suit-diamonds">♠</div>
                        <div class="card suit-hearts">10</div>
                    </div>
                </div>
            </div>

            <div class="game-card batak">
                <div class="game-icon">♠️</div>
                <div class="game-title">Batak Oyunu</div>
                <div class="game-description">
                    Klasik 4 kişilik ihale sistemi ile Batak! Koz belirleme, el alma ve stratejik hamleler. 
                    Klasik, Gömmeli ve Koz Maça modları ile zengin oyun deneyimi.[1][2][3]
                </div>
                <ul class="features">
                    <li>4 kişilik eşli oyun</li>
                    <li>Gömmeli Batak modu</li>
                    <li>Koz Maça seçeneği</li>
                    <li>Detaylı skor takibi</li>
                </ul>
                <a href="#" class="play-btn">Batak Oyna ➤</a>
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
                <div class="stat-number">1M+</div>
                <div>Aktif Oyuncu</div>
            </div>
            <div class="stat-card">
                <div class="stat-number">500K+</div>
                <div>Günlük Oyun</div>
            </div>
            <div class="stat-card">
                <div class="stat-number">24/7</div>
                <div>Canlı Maç</div>
            </div>
            <div class="stat-card">
                <div class="stat-number">100%</div>
                <div>Ücretsiz</div>
            </div>
        </div>

        <div class="footer">
            <h3>🎮 Hemen Oyna, Arkadaşlarınla Rekabet Et! 🎮</h3>
            <p>Mobil uyumlu • Hızlı • Ücretsiz • Eğlenceli</p>
        </div>
    </div>

    <script>
        // İnteraktif efektler
        document.querySelectorAll('.play-btn').forEach(btn => {
            btn.addEventListener('click', (e) => {
                e.preventDefault();
                btn.style.transform = 'scale(0.95)';
                setTimeout(() => {
                    btn.style.transform = 'translateY(-3px)';
                    alert('🎉 Oyun yükleniyor... Yakında aktif!');
                }, 150);
            });
        });

        // Kart hover efektleri
        document.querySelectorAll('.card, .okey-tile').forEach(card => {
            card.addEventListener('mouseenter', () => {
                card.style.transform = 'translateY(-10px) rotate(3deg)';
            });
            card.addEventListener('mouseleave', () => {
                card.style.transform = 'translateY(0) rotate(0deg)';
            });
        });

        // Responsive parallax efekti
        window.addEventListener('scroll', () => {
            const scrolled = window.pageYOffset;
            document.querySelector('.header').style.transform = `translateY(${scrolled * 0.5}px)`;
        });
    </script>
</body>
</html>
```

## Sources

1.https://www.hepsiburada.com/hayatburada/batak-oyunu-kolay-ve-eglenceli-ogrenme-rehberi-ile-hizli-baslangic/
2.https://www.youtube.com/watch?v=itppiZyyr84
3.https://www.dostlarokey.com/batak-oyunu-nedir/
