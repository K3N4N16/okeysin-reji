<think>
 The user wants a web page design for an Okey game website. Okey is a Turkish tile-based game similar to Rummy. They want:
1. Advanced features (gelişmiş özellikler)
2. Modern theme design (modern tema tasarımı)
3. Responsive design that fits in an iframe
4. Vanilla JS/HTML/CSS only
5. Single HTML file with inline styles/scripts
6. No external assets (use emojis for graphics)
7. No localStorage or network calls
8. Turkish language (since they wrote in Turkish)

Features to include for an Okey site:
- Game table visualization
- Player avatars/seats
- Tile pieces (okey stones)
- Score board
- Chat feature
- Game controls
- Spectator mode indication
- Modern dark theme with glassmorphism/cards
- Responsive layout

I should create:
1. A landing/lobby view
2. A game table view
3. Player positions (4 players typical for Okey)
4. Tile representation using emojis or styled divs
5. Interactive elements (even if simulated)
6. Modern UI with gradients, shadows, animations

Since it's a single page without backend, I'll create a mock interface that simulates the game state with interactive buttons to switch views and simulate gameplay.

Design approach:
- Dark theme with blue/purple gradients (modern)
- Glassmorphism effects (backdrop-filter)
- Animated tiles
- Responsive grid/flexbox
- Emoji-based icons (🀄🎲🃏 etc. for tiles, though Okey uses specific tiles - I can use colored squares or circles to represent Okey tiles)
- Sidebar for chat/players
- Main area for the table

Structure:
- Header with logo and user info
- Main game area with 4 player slots
- Center area for tiles/stacks
- Bottom area for player's hand
- Right sidebar for chat and scores
- Mobile responsive (stack on small screens)

Okey tiles are typically colored and numbered (1-13 in 4 colors: red, blue, green, black) plus 2 false jokers. I'll create divs with CSS to represent these tiles rather than using images.

Let me write the HTML with embedded CSS and JS.
</think> ```html
<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>OkeyKing - Modern Okey Salonu</title>
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
            --darker: #020617;
            --glass: rgba(30, 41, 59, 0.7);
            --glass-border: rgba(255, 255, 255, 0.1);
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 50%, #312e81 100%);
            color: #e2e8f0;
            height: 100vh;
            overflow: hidden;
            position: relative;
        }

        body::before {
            content: '';
            position: absolute;
            top: -50%;
            left: -50%;
            width: 200%;
            height: 200%;
            background: radial-gradient(circle, rgba(99, 102, 241, 0.15) 0%, transparent 70%);
            animation: pulse 15s ease-in-out infinite;
            pointer-events: none;
        }

        @keyframes pulse {
            0%, 100% { transform: translate(0, 0) scale(1); }
            50% { transform: translate(-25px, -25px) scale(1.1); }
        }

        .container {
            display: flex;
            flex-direction: column;
            height: 100vh;
            position: relative;
            z-index: 1;
        }

        header {
            background: var(--glass);
            backdrop-filter: blur(10px);
            border-bottom: 1px solid var(--glass-border);
            padding: 1rem 2rem;
            display: flex;
            justify-content: space-between;
            align-items: center;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        }

        .logo {
            font-size: 1.8rem;
            font-weight: 800;
            background: linear-gradient(to right, #818cf8, #c084fc);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }

        .user-info {
            display: flex;
            align-items: center;
            gap: 1rem;
            background: rgba(15, 23, 42, 0.6);
            padding: 0.5rem 1rem;
            border-radius: 9999px;
            border: 1px solid var(--glass-border);
        }

        .avatar {
            width: 40px;
            height: 40px;
            border-radius: 50%;
            background: linear-gradient(135deg, var(--primary), var(--secondary));
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.2rem;
            box-shadow: 0 0 15px rgba(99, 102, 241, 0.5);
        }

        .balance {
            color: #fbbf24;
            font-weight: 600;
            display: flex;
            align-items: center;
            gap: 0.3rem;
        }

        .main-layout {
            display: flex;
            flex: 1;
            overflow: hidden;
            padding: 1rem;
            gap: 1rem;
        }

        .game-area {
            flex: 1;
            display: flex;
            flex-direction: column;
            gap: 1rem;
        }

        .table-container {
            flex: 1;
            background: var(--glass);
            backdrop-filter: blur(10px);
            border-radius: 24px;
            border: 1px solid var(--glass-border);
            position: relative;
            padding: 2rem;
            box-shadow: inset 0 0 50px rgba(0, 0, 0, 0.5);
            display: grid;
            grid-template-rows: auto 1fr auto;
            grid-template-columns: auto 1fr auto;
            gap: 1rem;
        }

        .player-slot {
            background: rgba(15, 23, 42, 0.8);
            border: 2px solid var(--glass-border);
            border-radius: 16px;
            padding: 1rem;
            display: flex;
            align-items: center;
            gap: 0.8rem;
            min-width: 180px;
            transition: all 0.3s ease;
        }

        .player-slot.active {
            border-color: var(--accent);
            box-shadow: 0 0 20px rgba(6, 182, 212, 0.3);
            animation: glow 2s ease-in-out infinite;
        }

        @keyframes glow {
            0%, 100% { box-shadow: 0 0 20px rgba(6, 182, 212, 0.3); }
            50% { box-shadow: 0 0 30px rgba(6, 182, 212, 0.5); }
        }

        .player-top { grid-column: 2; justify-self: center; }
        .player-left { grid-row: 2; grid-column: 1; align-self: center; flex-direction: column; }
        .player-right { grid-row: 2; grid-column: 3; align-self: center; flex-direction: column; }
        .player-bottom { grid-column: 2; grid-row: 3; justify-self: center; flex-direction: row-reverse; }

        .player-avatar {
            width: 50px;
            height: 50px;
            border-radius: 50%;
            background: linear-gradient(135deg, #64748b, #475569);
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.5rem;
            border: 3px solid rgba(255, 255, 255, 0.1);
        }

        .player-info h4 {
            font-size: 0.9rem;
            margin-bottom: 0.2rem;
        }

        .player-info span {
            font-size: 0.75rem;
            color: #94a3b8;
        }

        .center-area {
            grid-row: 2;
            grid-column: 2;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            gap: 2rem;
        }

        .tile-stack {
            display: flex;
            gap: -10px;
            position: relative;
        }

        .tile {
            width: 40px;
            height: 60px;
            background: linear-gradient(135deg, #f8fafc, #e2e8f0);
            border-radius: 6px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: 800;
            font-size: 1.2rem;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3), inset 0 1px 0 rgba(255, 255, 255, 0.8);
            border: 1px solid #cbd5e1;
            position: relative;
            margin-left: -20px;
            transition: transform 0.2s;
        }

        .tile:first-child { margin-left: 0; }
        .tile:hover { transform: translateY(-10px); z-index: 10; }

        .tile.red { color: #dc2626; }
        .tile.blue { color: #2563eb; }
        .tile.green { color: #16a34a; }
        .tile.black { color: #0f172a; }
        .tile.joker { 
            background: linear-gradient(135deg, #fbbf24, #f59e0b);
            color: #fff;
            border-color: #d97706;
        }

        .indicator-tile {
            width: 50px;
            height: 70px;
            background: linear-gradient(135deg, #ef4444, #dc2626);
            border-radius: 8px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.5rem;
            color: white;
            box-shadow: 0 10px 25px rgba(220, 38, 38, 0.4);
            border: 2px solid rgba(255, 255, 255, 0.3);
            animation: float 3s ease-in-out infinite;
        }

        @keyframes float {
            0%, 100% { transform: translateY(0); }
            50% { transform: translateY(-10px); }
        }

        .hand-area {
            background: rgba(15, 23, 42, 0.9);
            border-radius: 16px;
            padding: 1rem;
            display: flex;
            justify-content: center;
            gap: 0.5rem;
            border: 1px solid var(--glass-border);
            min-height: 100px;
            overflow-x: auto;
        }

        .hand-area .tile {
            cursor: pointer;
            margin-left: -15px;
        }

        .hand-area .tile:first-child { margin-left: 0; }

        .sidebar {
            width: 300px;
            display: flex;
            flex-direction: column;
            gap: 1rem;
        }

        .panel {
            background: var(--glass);
            backdrop-filter: blur(10px);
            border: 1px solid var(--glass-border);
            border-radius: 16px;
            padding: 1rem;
            flex: 1;
            display: flex;
            flex-direction: column;
        }

        .panel-header {
            font-weight: 700;
            margin-bottom: 1rem;
            padding-bottom: 0.5rem;
            border-bottom: 1px solid var(--glass-border);
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }

        .chat-messages {
            flex: 1;
            overflow-y: auto;
            display: flex;
            flex-direction: column;
            gap: 0.5rem;
            margin-bottom: 1rem;
            max-height: 200px;
        }

        .message {
            background: rgba(30, 41, 59, 0.5);
            padding: 0.5rem;
            border-radius: 8px;
            font-size: 0.85rem;
        }

        .message.system {
            color: #94a3b8;
            font-style: italic;
        }

        .chat-input {
            display: flex;
            gap: 0.5rem;
        }

        .chat-input input {
            flex: 1;
            background: rgba(15, 23, 42, 0.6);
            border: 1px solid var(--glass-border);
            border-radius: 8px;
            padding: 0.5rem;
            color: white;
            outline: none;
        }

        button {
            background: linear-gradient(135deg, var(--primary), var(--secondary));
            border: none;
            color: white;
            padding: 0.5rem 1rem;
            border-radius: 8px;
            cursor: pointer;
            font-weight: 600;
            transition: all 0.2s;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.2);
        }

        button:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 12px rgba(99, 102, 241, 0.4);
        }

        button:active {
            transform: translateY(0);
        }

        .controls {
            display: flex;
            gap: 0.5rem;
            justify-content: center;
            margin-top: 0.5rem;
        }

        .btn-secondary {
            background: rgba(30, 41, 59, 0.8);
            border: 1px solid var(--glass-border);
        }

        .btn-secondary:hover {
            background: rgba(51, 65, 85, 0.9);
        }

        .timer {
            position: absolute;
            top: 1rem;
            right: 1rem;
            background: rgba(239, 68, 68, 0.9);
            padding: 0.5rem 1rem;
            border-radius: 9999px;
            font-weight: 800;
            font-size: 1.2rem;
            color: white;
            animation: tick 1s linear infinite;
        }

        @keyframes tick {
            0% { transform: scale(1); }
            50% { transform: scale(1.05); }
            100% { transform: scale(1); }
        }

        .badges {
            display: flex;
            gap: 0.5rem;
            margin-top: 0.5rem;
        }

        .badge {
            background: rgba(251, 191, 36, 0.2);
            color: #fbbf24;
            padding: 0.2rem 0.5rem;
            border-radius: 4px;
            font-size: 0.7rem;
            font-weight: 700;
        }

        @media (max-width: 1024px) {
            .sidebar { display: none; }
            .main-layout { flex-direction: column; }
            .table-container { 
                grid-template-rows: auto auto 1fr auto;
                grid-template-columns: 1fr 1fr;
            }
            .player-top { grid-column: 1 / -1; }
            .player-bottom { grid-column: 1 / -1; grid-row: 4; }
            .center-area { grid-column: 1 / -1; grid-row: 3; }
        }

        @media (max-width: 640px) {
            .player-left, .player-right { display: none; }
            .hand-area { padding: 0.5rem; }
            .tile { width: 30px; height: 45px; font-size: 0.9rem; }
            header { padding: 1rem; }
            .logo { font-size: 1.2rem; }
        }

        .modal {
            display: none;
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0, 0, 0, 0.8);
            z-index: 1000;
            align-items: center;
            justify-content: center;
            backdrop-filter: blur(5px);
        }

        .modal.active { display: flex; }

        .modal-content {
            background: linear-gradient(135deg, #1e293b, #0f172a);
            border: 1px solid var(--glass-border);
            border-radius: 24px;
            padding: 2rem;
            max-width: 400px;
            width: 90%;
            text-align: center;
            box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5);
        }

        .modal-content h2 {
            font-size: 2rem;
            margin-bottom: 1rem;
            background: linear-gradient(to right, #fbbf24, #f59e0b);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        .stats {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 1rem;
            margin: 1.5rem 0;
        }

        .stat {
            background: rgba(30, 41, 59, 0.5);
            padding: 1rem;
            border-radius: 12px;
        }

        .stat-value {
            font-size: 1.5rem;
            font-weight: 800;
            color: var(--accent);
        }

        .stat-label {
            font-size: 0.8rem;
            color: #94a3b8;
        }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <div class="logo">
                🎲 OkeyKing
            </div>
            <div class="user-info">
                <div class="avatar">👤</div>
                <div>
                    <div style="font-weight: 600; font-size: 0.9rem;">Oyuncu_99</div>
                    <div class="balance">💰 12.450</div>
                </div>
            </div>
        </header>

        <div class="main-layout">
            <div class="game-area">
                <div class="table-container" id="gameTable">
                    <div class="timer" id="timer">15</div>
                    
                    <div class="player-slot player-top" id="p-top">
                        <div class="player-avatar">🤖</div>
                        <div class="player-info">
                            <h4>Bot_Ahmet</h4>
                            <span>Sırası bekliyor...</span>
                        </div>
                        <div class="badges">
                            <span class="badge">VIP</span>
                        </div>
                    </div>

                    <div class="player-slot player-left" id="p-left">
                        <div class="player-avatar">👩</div>
                        <div class="player-info">
                            <h4>Ayşe_Nur</h4>
                            <span>Çevrimiçi</span>
                        </div>
                    </div>

                    <div class="center-area">
                        <div style="display: flex; gap: 2rem; align-items: center;">
                            <div>
                                <div style="text-align: center; margin-bottom: 0.5rem; font-size: 0.8rem; opacity: 0.7;">Gösterge</div>
                                <div class="indicator-tile" id="indicator">10🔴</div>
                            </div>
                            <div>
                                <div style="text-align: center; margin-bottom: 0.5rem; font-size: 0.8rem; opacity: 0.7;">Kalan Taş</div>
                                <div style="font-size: 2rem; font-weight: 800;">42</div>
                            </div>
                        </div>
                        <div class="tile-stack" id="stack">
                            <div class="tile" style="background: #334155; border-color: #475569;">?</div>
                            <div class="tile" style="background: #334155; border-color: #475569; margin-left: -30px;">?</div>
                            <div class="tile" style="background: #334155; border-color: #475569; margin-left: -30px;">?</div>
                        </div>
                    </div>

                    <div class="player-slot player-right" id="p-right">
                        <div class="player-avatar">👨</div>
                        <div class="player-info">
                            <h4>Mehmet_53</h4>
                            <span>Oynuyor...</span>
                        </div>
                    </div>

                    <div class="player-slot player-bottom active" id="p-bottom">
                        <div class="player-avatar" style="background: linear-gradient(135deg, var(--primary), var(--secondary));">👤</div>
                        <div class="player-info">
                            <h4>Sen</h4>
                            <span>Sıra sende!</span>
                        </div>
                    </div>
                </div>

                <div class="hand-area" id="playerHand">
                    <div class="tile red" onclick="playTile(this)">1</div>
                    <div class="tile blue" onclick="playTile(this)">3</div>
                    <div class="tile green" onclick="playTile(this)">7</div>
                    <div class="tile black" onclick="playTile(this)">11</div>
                    <div class="tile red" onclick="playTile(this)">5</div>
                    <div class="tile joker" onclick="playTile(this)">🃏</div>
                    <div class="tile blue" onclick="playTile(this)">8</div>
                   div class="tile green" onclick="playTile(this)">12</div>
                    <div class="tile black" onclick="playTile(this)">2</div>
                    <div class="tile red" onclick="playTile(this)">9</div>
                    <div class="tile blue" onclick="playTile(this)">4</div>
                    <div class="tile green" onclick="playTile(this)">6</div>
                    <div class="tile black" onclick="playTile(this)">10</div>
                    <div class="tile red" onclick="playTile(this)">13</div>
                </div>

                <div class="controls">
                    <button class="btn-secondary" onclick="sortTiles()">🔄 Sırala</button>
                    <button onclick="drawTile()">🎯 Çek</button>
                    <button onclick="declareWin()">🏆 Okey</button>
                    <button class="btn-secondary" onclick="openChat()">💬 Sohbet</button>
                </div>
            </div>

            <div class="sidebar">
                <div class="panel">
                    <div class="panel-header">
                        💬 Sohbet
                    </div>
                    <div class="chat-messages" id="chatBox">
                        <div class="message system">Oyuna hoş geldiniz!</div>
                        <div class="message"><strong>Bot_Ahmet:</strong> İyi oyunlar!</div>
                        <div class="message"><strong>Ayşe_Nur:</strong> Bol şans 🍀</div>
                    </div>
                    <div class="chat-input">
                        <input type="text" placeholder="Mesaj yaz..." id="chatInput" onkeypress="handleChat(event)">
                        <button onclick="sendMessage()">➤</button>
                    </div>
                </div>

                <div class="panel">
                    <div class="panel-header">
                        📊 Skor Tablosu
                    </div>
                    <div style="display: flex; flex-direction: column; gap: 0.5rem;">
                        <div style="display: flex; justify-content: space-between; padding: 0.5rem; background: rgba(99, 102, 241, 0.2); border-radius: 8px; border-left: 3px solid var(--primary);">
                            <span>1. Oyuncu_99</span>
                            <strong>1,250</strong>
                        </div>
                        <div style="display: flex; justify-content: space-between; padding: 0.5rem; background: rgba(30, 41, 59, 0.5); border-radius: 8px;">
                            <span>2. Bot_Ahmet</span>
                            <span>980</span>
                        </div>
                        <div style="display: flex; justify-content: space-between; padding: 0.5rem; background: rgba(30, 41, 59, 0.5); border-radius: 8px;">
                            <span>3. Ayşe_Nur</span>
                            <span>750</span>
                        </div>
                        <div style="display: flex; justify-content: space-between; padding: 0.5rem; background: rgba(30, 41, 59, 0.5); border-radius: 8px;">
                            <span>4. Mehmet_53</span>
                            <span>620</span>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <div class="modal" id="winModal">
        <div class="modal-content">
            <h2>🎉 Tebrikler!</h2>
            <p>Okey yaptınız!</p>
            <div class="stats">
                <div class="stat">
                    <div class="stat-value">+500</div>
                    <div class="stat-label">Kazanç</div>
                </div>
                <div class="stat">
                    <div class="stat-value">15s</div>
                    <div class="stat-label">Süre</div>
                </div>
            </div>
            <button onclick="closeModal()" style="width: 100%; padding: 1rem;">Yeni Oyun</button>
        </div>
    </div>

    <script>
        let timeLeft = 15;
        let timerInterval;
        let currentPlayer = 'bottom';

        function startTimer() {
            clearInterval(timerInterval);
            timeLeft = 15;
            document.getElementById('timer').textContent = timeLeft;
            
            timerInterval = setInterval(() => {
                timeLeft--;
                document.getElementById('timer').textContent = timeLeft;
                
                if (timeLeft <= 5) {
                    document.getElementById('timer').style.background = 'rgba(239, 68, 68, 0.9)';
                } else {
                    document.getElementById('timer').style.background = 'rgba(99, 102, 241, 0.9)';
                }
                
                if (timeLeft <= 0) {
                    clearInterval(timerInterval);
                    switchTurn();
                }
            }, 1000);
        }

        function switchTurn() {
            const positions = ['top', 'left', 'right', 'bottom'];
            const currentIndex = positions.indexOf(currentPlayer);
            currentPlayer = positions[(currentIndex + 1) % 4];
            
            document.querySelectorAll('.player-slot').forEach(slot => {
                slot.classList.remove('active');
            });
            
            const nextPlayer = document.querySelector(`.player-${currentPlayer}`);
            if (nextPlayer) nextPlayer.classList.add('active');
            
            startTimer();
            
            if (currentPlayer !== 'bottom') {
                setTimeout(() => {
                    const messages = ['Düşünüyor...', 'Taş çekiyor...', 'Oynuyor...'];
                    const msg = messages[Math.floor(Math.random() * messages.length)];
                    updatePlayerStatus(currentPlayer, msg);
                }, 1000);
            } else {
                updatePlayerStatus('bottom', 'Sıra sende!');
            }
        }

        function updatePlayerStatus(position, text) {
            const slot = document.querySelector(`.player-${position}`);
            if (slot) {
                const statusSpan = slot.querySelector('.player-info span');
                if (statusSpan) statusSpan.textContent = text;
            }
        }

        function playTile(tile) {
            if (currentPlayer !== 'bottom') return;
            
            tile.style.transform = 'translateY(-50px) scale(1.1)';
            setTimeout(() => {
                tile.style.display = 'none';
                sortTiles();
            }, 300);
            
            switchTurn();
        }

        function drawTile() {
            if (currentPlayer !== 'bottom') return;
            
            const colors = ['red', 'blue', 'green', 'black'];
            const color = colors[Math.floor(Math.random() * colors.length)];
            const num = Math.floor(Math.random() * 13) + 1;
            
            const newTile = document.createElement('div');
            newTile.className = `tile ${color}`;
            newTile.textContent = num;
            newTile.onclick = function() { playTile(this); };
            
            const hand = document.getElementById('playerHand');
            hand.appendChild(newTile);
            
            setTimeout(() => {
                newTile.style.transform = 'translateX(0)';
            }, 50);
            
            sortTiles();
        }

        function sortTiles() {
            const hand = document.getElementById('playerHand');
            const tiles = Array.from(hand.children);
            
            tiles.sort((a, b) => {
                const aClass = a.className.split(' ')[1] || '';
                const bClass = b.className.split(' ')[1] || '';
                if (aClass !== bClass) return aClass.localeCompare(bClass);
                return parseInt(a.textContent) - parseInt(b.textContent);
            });
            
            tiles.forEach(tile => hand.appendChild(tile));
        }

        function declareWin() {
            document.getElementById('winModal').classList.add('active');
            clearInterval(timerInterval);
            
            addMessage('system', 'Tebrikler! Oyunu kazandınız!');
        }

        function closeModal() {
            document.getElementById('winModal').classList.remove('active');
            resetGame();
        }

        function resetGame() {
            location.reload();
        }

        function handleChat(e) {
            if (e.key === 'Enter') sendMessage();
        }

        function sendMessage() {
            const input = document.getElementById('chatInput');
            const text = input.value.trim();
            if (!text) return;
            
            addMessage('player', text, 'Sen');
            input.value = '';
            
            setTimeout(() => {
                const responses = ['İyi hamle!', 'Şanslısın 😊', 'Güzel oyun', '🤔'];
                const randomResponse = responses[Math.floor(Math.random() * responses.length)];
                const players = ['Bot_Ahmet', 'Ayşe_Nur', 'Mehmet_53'];
                const randomPlayer = players[Math.floor(Math.random() * players.length)];
                addMessage('other', randomResponse, randomPlayer);
            }, 2000);
        }

        function addMessage(type, text, user) {
            const chatBox = document.getElementById('chatBox');
            const msg = document.createElement('div');
            msg.className = 'message';
            
            if (type === 'system') {
                msg.className += ' system';
                msg.textContent = text;
            } else if (type === 'player') {
                msg.innerHTML = `<strong style="color: #818cf8">${user}:</strong> ${text}`;
            } else {
                msg.innerHTML = `<strong>${user}:</strong> ${text}`;
            }
            
            chatBox.appendChild(msg);
            chatBox.scrollTop = chatBox.scrollHeight;
        }

        function openChat() {
            document.getElementById('chatInput').focus();
        }

        document.addEventListener('DOMContentLoaded', () => {
            startTimer();
            
            document.querySelectorAll('.tile').forEach(tile => {
                tile.addEventListener('mouseenter', () => {
                    if (!tile.dataset.clicked) {
                        tile.style.transform = 'translateY(-5px) scale(1.05)';
                    }
                });
                
                tile.addEventListener('mouseleave', () => {
                    if (!tile.dataset.clicked) {
                        tile.style.transform = '';
                    }
                });
            });
        });
    </script>
</body>
</html>
```