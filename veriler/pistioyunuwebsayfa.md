# Pişti Oyunu Web Sayfası Tasarımı

## Prompt 1

### You
*2025-12-09 10:07:13 +03*

Pişti oyunu Web sayfası tasarımı modern gösterişli html yaz 

### gpt-oss-120b
*2025-12-09 10:10:44 +03*

<think>
The user writes in Turkish: "Pişti oyunu Web sayfası tasarımı modern gösterişli html yaz". They want a modern, flashy HTML design for a Pişti game web page. So we need to provide HTML code (and possibly CSS/JS) that creates a modern, visually appealing page for a Pişti game. Should include maybe a header, game area, cards, controls, responsive design. Provide code blocks with HTML, CSS, maybe minimal JavaScript placeholders.

User didn't ask for explanation beyond that, but we can give a brief description. They asked "write html". Provide a full page with CSS (maybe internal style) and some placeholder assets (like images). Use modern techniques (Flexbox, CSS Grid, animations). Show sections: title, player names, scores, deck, hand, discard pile, buttons (New Game, Reset). Use modern fonts, colors.

We need to output code with markdown fences, language html, css, js.

Ensure inline math not needed.

Let's craft:

- HTML skeleton- CSS: using variables, dark theme or bright.
- JS: placeholder for functions to start game, deal cards, handle click.

Add comments for where to add assets.

We should not include extraneous explanation but a small intro is okay.

Let's produce.
</think>Below is a **complete, ready‑to‑use** HTML page for a modern, flashy Pişti game interface.  
It contains:

* HTML5 markup with semantic sections.  
* CSS (inside a `<style>` tag) that uses CSS‑Grid, Flexbox, CSS variables, smooth hover/flip animations and a responsive layout.  
* Minimal JavaScript (inside a `<script>` tag) with placeholders where you can hook your game‑logic.  

You can copy the whole block into a file called **`pisiti.html`** and open it in any modern browser.

```html
<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Pişti Oyunu</title>

    <!-- Google Font for a modern look -->
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600&display=swap" rel="stylesheet">

    <style>
        :root {
            --bg-primary: #1e1e2f;
            --bg-card: #fff;
            --bg-table: #2b2b40;
            --accent: #ff6b6b;
            --accent-light: #ff8787;
            --text-primary: #f0f0f5;
            --text-dark: #2c2c3e;
            --shadow: rgba(0,0,0,0.3);
        }

        * { box-sizing: border-box; margin:0; padding:0; }
        body {
            font-family: 'Montserrat', sans-serif;
            background: var(--bg-primary);
            color: var(--text-primary);
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            align-items: center;
            padding: 1rem;
        }

        h1 {
            margin: 0.5rem 0 1rem;
            font-weight: 600;
            font-size: 2.5rem;
            text-shadow: 0 2px 4px var(--shadow);
            color: var(--accent);
        }

        .game-wrapper {
            width: 100%;
            max-width: 1100px;
            background: var(--bg-table);
            border-radius: 12px;
            padding: 1.5rem;
            box-shadow: 0 8px 24px var(--shadow);
            display: grid;
            grid-template-rows: auto 1fr auto;
            gap: 1rem;
        }

        /* Top bar – player names & scores */
        .top-bar {
            display: flex;
            justify-content: space-between;
            align-items: center;
            font-size: 1.2rem;
        }
        .player {
            display: flex;
            flex-direction: column;
            align-items: center;
        }
        .player span {
            font-weight: 600;
            margin-top: 0.2rem;
        }

        /* Main play area */
        .play-area {
            display: grid;
            grid-template-columns: 1fr 2fr 1fr;
            align-items: center;
            gap: 0.8rem;
        }

        .hand, .opponent-hand {
            display: flex;
            justify-content: center;
            gap: 0.4rem;
            flex-wrap: wrap;
        }

        .card {
            width: 80px;
            height: 120px;
            perspective: 600px;
            cursor: pointer;
        }
        .card-inner {
            position: relative;
            width: 100%;
            height: 100%;
            transition: transform 0.6s;
            transform-style: preserve-3d;
        }
        .card:hover .card-inner { transform: rotateY(180deg); }

        .card-front, .card-back {
            position: absolute;
            width: 100%;
            height: 100%;
            border-radius: 8px;
            backface-visibility: hidden;
            border: 2px solid var(--accent);
        }
        .card-front {
            background: var(--bg-card);
            display: flex;
            justify-content: center;
            align-items: center;
            font-size: 1.6rem;
            color: var(--text-dark);
        }
        .card-back {
            background: var(--accent);
            transform: rotateY(180deg);
        }

        /* Center pile */
        .table-pile {
            position: relative;
            height: 150px;
            display: flex;
            justify-content: center;
            align-items: flex-end;
        }
        .table-pile .card {
            position: absolute;
            top: 0;
        }
        .table-pile .card:not(:last-child) { left: -10px; }

        /* Bottom controls */
        .bottom-bar {
            display: flex;
            justify-content: center;
            gap: 1rem;
        }
        .btn {
            background: var(--accent);
            color: #fff;
            border: none;
            border-radius: 6px;
            padding: 0.6rem 1.4rem;
            font-size: 1rem;
            cursor: pointer;
            transition: background 0.3s, transform 0.1s;
        }
        .btn:hover { background: var(--accent-light); }
        .btn:active { transform: scale(0.96); }

        /* Responsive */
        @media (max-width: 768px) {
            .play-area { grid-template-columns: 1fr; }
            .hand, .opponent-hand { justify-content: flex-start; }
            .card { width: 60px; height: 90px; }
        }
    </style>
</head>
<body>

    <h1>PİŞTİ</h1>

    <div class="game-wrapper">

        <!-- Top bar: players & scores -->
        <div class="top-bar">
            <div class="player" id="player1">
                <strong>Sen</strong>
                <span id="score1">0</span>
            </div>
            <div class="player" id="player2">
                <strong>Rakip</strong>
                <span id="score2">0</span>
            </div>
        </div>

        <!-- Main play area -->
        <div class="play-area">

            <!-- Opponent hand (face‑down) -->
            <div class="opponent-hand" id="opponentHand">
                <!-- Example placeholders – replace with dynamic cards -->
                <div class="card"><div class="card-inner"><div class="card-front"></div><div class="card-back"></div></div></div>
                <div class="card"><div class="card-inner"><div class="card-front"></div><div class="card-back"></div></div></div>
                <div class="card"><div class="card-inner"><div class="card-front"></div><div class="card-back"></div></div></div>
                <div class="card"><div class="card-inner"><div class="card-front"></div><div class="card-back"></div></div></div>
                <div class="card"><div class="card-inner"><div class="card-front"></div><div class="card-back"></div></div></div>
            </div>

            <!-- Table pile -->
            <div class="table-pile" id="tablePile">
                <!-- The central card (if any) will be inserted here by JS -->
            </div>

            <!-- Your hand (clickable) -->
            <div class="hand" id="playerHand">
                <!-- Example placeholders – replace with dynamic cards -->
                <!-- Cards will be generated by JavaScript -->
            </div>
        </div>

        <!-- Bottom controls -->
        <div class="bottom-bar">
            <button class="btn" id="newGameBtn">Yeni Oyun</button>
            <button class="btn" id="resetBtn">Sıfırla</button>
        </div>

    </div>

    <script>
        // -------------------------------------------------
        //  Simple placeholder logic – replace with real game
        // -------------------------------------------------
        const suits = ['♠','♥','♦','♣'];
        const ranks = ['A','2','3','4','5','6','7','8','9','10','J','Q','K'];
        let deck = [];

        const playerHandEl = document.getElementById('playerHand');
        const opponentHandEl = document.getElementById('opponentHand');
        const tablePileEl = document.getElementById('tablePile');
        const score1El = document.getElementById('score1');
        const score2El = document.getElementById('score2');

        function createDeck() {
            deck = [];
            for (let s of suits) {
                for (let r of ranks) {
                    deck.push({suit:s, rank:r});
                }
            }
            // Shuffle
            for (let i = deck.length-1; i>0; i--) {
                const j = Math.floor(Math.random() * (i+1));
                [deck[i], deck[j]] = [deck[j], deck[i]];
            }
        }

        function cardToString(card) {
            return `${card.rank}${card.suit}`;
        }

        function renderCard(card, clickable=false) {
            const cardEl = document.createElement('div');
            cardEl.className = 'card';
            const inner = document.createElement('div');
            inner.className = 'card-inner';

            const front = document.createElement('div');
            front.className = 'card-front';
            front.textContent = cardToString(card);

            const back = document.createElement('div');
            back.className = 'card-back';

            inner.appendChild(front);
            inner.appendChild(back);
            cardEl.appendChild(inner);

            if (clickable) {
                cardEl.addEventListener('click', () => playCard(card));
            } else {
                // hide front for opponent
                front.style.visibility = 'hidden';
            }
            return cardEl;
        }

        function dealInitial() {
            // 4 cards each
            playerHandEl.innerHTML = '';
            opponentHandEl.innerHTML = '';
            for (let i=0;i<4;i++) {
                const pCard = deck.pop();
                playerHandEl.appendChild(renderCard(pCard, true));

                const oCard = deck.pop();
                opponentHandEl.appendChild(renderCard(oCard));
            }

            // start pile with one card
            tablePileEl.innerHTML = '';
            const startCard = deck.pop();
            tablePileEl.appendChild(renderCard(startCard));
        }

        function playCard(card) {
            // Simple visual: move the card to the table pile
            const cardEl = renderCard(card);
            tablePileEl.appendChild(cardEl);
            // Remove from player's hand (re‑render)
            playerHandEl.innerHTML = '';
            // Re‑fill hand with next 4 cards (or less if deck empty)
            for (let i=0;i<4 && deck.length>0;i++) {
                const newCard = deck.pop();
                playerHandEl.appendChild(renderCard(newCard, true));
            }

            // Update scores placeholder
            // (Here you would implement real Pişti scoring)
            score1El.textContent = parseInt(score1El.textContent) + 1;
        }

        document.getElementById('newGameBtn').addEventListener('click', () => {
            createDeck();
            dealInitial();
            score1El.textContent = '0';
            score2El.textContent = '0';
        });

        document.getElementById('resetBtn').addEventListener('click', () => {
            location.reload();
        });

        // Auto‑start a game on load
        createDeck();
        dealInitial();
    </script>
</body>
</html>
```

### How to use

1. **Save** the code above as `pisiti.html`.  
2. Open it in any browser (Chrome, Edge, Firefox, Safari).  
3. Click **“Yeni Oyun”** to shuffle a fresh deck.  
4. Click a card in your hand to play it – the placeholder script simply moves the card to the table and increments your score; replace the `playCard` function with the full Pişti rules.  

Feel free to swap the colors, fonts, or card graphics, add sound effects, or integrate a full game‑engine – the layout and CSS are already set up for a modern, eye‑catching look. Enjoy!

### Qwen3 Max Instruct Preview
*2025-12-09 10:07:14 +03*

İşte modern ve gösterişli bir **Pişti oyunu** web sayfası tasarımı için HTML + CSS + JavaScript örneği. Bu örnek, temel arayüzü içerir; oyun mantığı basitçe simüle edilmiştir (gerçek kart mekaniği için daha fazla geliştirme gerekir).

```html
<!DOCTYPE html>
<html lang="tr">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Pişti Oyunu</title>
  <style>
    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
      font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }

    body {
      background: linear-gradient(135deg, #1a2a6c, #b21f1f, #1a2a6c);
      color: white;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      align-items: center;
      padding: 2rem;
    }

    header {
      text-align: center;
      margin-bottom: 2rem;
    }

    h1 {
      font-size: 2.8rem;
      text-shadow: 0 0 10px rgba(255,255,255,0.7);
      margin-bottom: 0.5rem;
    }

    .scoreboard {
      display: flex;
      justify-content: space-around;
      width: 80%;
      max-width: 600px;
      background: rgba(0,0,0,0.4);
      padding: 1rem;
      border-radius: 12px;
      margin-bottom: 2rem;
    }

    .player-score {
      text-align: center;
    }

    .player-score h2 {
      font-size: 1.4rem;
    }

    .player-score p {
      font-size: 1.8rem;
      font-weight: bold;
    }

    .game-area {
      width: 90%;
      max-width: 700px;
      background: rgba(0,0,0,0.5);
      border-radius: 16px;
      padding: 1.5rem;
      text-align: center;
    }

    .center-pile {
      width: 120px;
      height: 160px;
      background: #fff;
      border: 2px dashed #ffcc00;
      margin: 0 auto 2rem;
      border-radius: 8px;
      display: flex;
      align-items: center;
      justify-content: center;
      color: #333;
      font-weight: bold;
      box-shadow: 0 6px 12px rgba(0,0,0,0.4);
    }

    .hand {
      display: flex;
      justify-content: center;
      gap: 1rem;
      margin-top: 1rem;
    }

    .card {
      width: 70px;
      height: 100px;
      background: white;
      border-radius: 8px;
      display: flex;
      align-items: center;
      justify-content: center;
      color: #d32f2f;
      font-weight: bold;
      cursor: pointer;
      transition: transform 0.2s;
      box-shadow: 0 4px 8px rgba(0,0,0,0.3);
    }

    .card:hover {
      transform: translateY(-10px);
    }

    .controls {
      margin-top: 2rem;
    }

    button {
      background: #ffcc00;
      color: #1a2a6c;
      border: none;
      padding: 0.8rem 1.5rem;
      font-size: 1.1rem;
      font-weight: bold;
      border-radius: 50px;
      cursor: pointer;
      transition: background 0.3s;
    }

    button:hover {
      background: #ffd740;
    }

    footer {
      margin-top: 2rem;
      text-align: center;
      font-size: 0.9rem;
      opacity: 0.8;
    }
  </style>
</head>
<body>
  <header>
    <h1>♠️ Pişti ♣️</h1>
    <p>Klasik Türk iskambil oyunu</p>
  </header>

  <div class="scoreboard">
    <div class="player-score">
      <h2>Oyuncu</h2>
      <p id="player-score">0</p>
    </div>
    <div class="player-score">
      <h2>Bilgisayar</h2>
      <p id="computer-score">0</p>
    </div>
  </div>

  <div class="game-area">
    <div class="center-pile" id="center-pile">Orta</div>
    <div class="hand" id="player-hand">
      <!-- Kartlar JavaScript ile eklenecek -->
    </div>
    <div class="controls">
      <button id="new-game">Yeni Oyun</button>
    </div>
  </div>

  <footer>
    <p>© 2025 Pişti Oyunu | Eğlenceli ve Stratejik</p>
  </footer>

  <script>
    // Basit demo için kartları simüle edelim
    const suits = ['♠', '♥', '♦', '♣'];
    const ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'];
    
    function getRandomCard() {
      const suit = suits[Math.floor(Math.random() * suits.length)];
      const rank = ranks[Math.floor(Math.random() * ranks.length)];
      return `${rank}${suit}`;
    }

    function renderHand() {
      const handEl = document.getElementById('player-hand');
      handEl.innerHTML = '';
      for (let i = 0; i < 4; i++) {
        const card = document.createElement('div');
        card.className = 'card';
        card.textContent = getRandomCard();
        card.addEventListener('click', () => {
          alert('Kart oynandı! (Demo)');
        });
        handEl.appendChild(card);
      }
    }

    document.getElementById('new-game').addEventListener('click', () => {
      renderHand();
      document.getElementById('center-pile').textContent = getRandomCard();
      // Skor sıfırlama (demo)
      document.getElementById('player-score').textContent = '0';
      document.getElementById('computer-score').textContent = '0';
    });

    // İlk yüklemede el oluştur
    renderHand();
  </script>
</body>
</html>
```

### Özellikler:
- **Modern gradient arka plan**
- **Responsive tasarım**
- **Kartlar hover efektiyle**
- **Skor tablosu**
- **Yeni oyun butonu**
- **Basit interaktif demo**

> ⚠️ Not: Bu sadece **görsel ve temel etkileşim** içindir. Gerçek Pişti kurallarını uygulamak için tam bir oyun motoru (kart dağıtma, pişti kontrolü, skorlama mantığı vs.) gerekir. İstersen bu mantığı da ekleyebilirim.

## Prompt 2

### You
*2025-12-09 10:14:14 +03*

Oyun sayfası yapacağız oyun yapmayacağım 

### gpt-oss-120b
*2025-12-09 10:14:14 +03*

<think>
The user says: "Oyun sayfası yapacağız oyun yapmayacağım" which means "We will make a game page, we will not make the game." So they want a page layout for a game perhaps but not the game logic. They previously asked for a modern flashy HTML design for the Pişti game; now they clarify they only need the page layout, not the actual game functionality. So we should provide HTML/CSS (maybe minimal JS for UI) without game logic. Provide placeholders for game area, scores, etc. Keep it modern. Possibly remove the placeholder JavaScript for game logic, but we can keep minimal interactivity like button clicks that do nothing.

We should create a clean page, responsive, with sections: header, scoreboard, player hands visual placeholders (cards as images maybe blank). Provide CSS with modern styles. Provide placeholder images with unsplash or base64 color boxes.

We'll supply HTML and CSS (maybe a minimal JS to swap placeholder cards). Emphasize that the code is only UI, not game.

Let's respond in Turkish, give explanation brief, then provide code.


</think>Aşağıda **“Pişti – Oyun Sayfası”** için yalnızca görsel tasarımı (HTML + CSS) yer alıyor.  
Sayfa tamamen **statik**; oyun mantığı, kart dağıtımı vb. altyapı eklenmemiştir.  
İsterseniz JavaScript ile etkileşim ekleyebilir, kart görsellerini değiştirebilir ya da puanları güncelleyebilirsiniz.

---

## 1. Dosya Yapısı

```
pisiti/
│─ index.html
│─ style.css          (isteğe bağlı; burada aynı dosyada da tutabilirsiniz)
│─ img/
│   └─ back.png       (kart arka planı – örnek bir görsel)
│   └─ placeholder.png (boş kart resmi)
```

> **Not:** `style.css` içeriğini doğrudan `<style>` etiketi içinde de ekleyebilirsiniz. Aşağıdaki örnekte tek dosya (`index.html`) kullanılmıştır.

---

## 2. `index.html`

```html
<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <title>Pişti – Oyun Sayfası</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <!-- Google Font -->
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600&display=swap"
          rel="stylesheet">

    <style>
        /* ---------- Temel Renk ve Değişkenler ---------- */
        :root {
            --bg-primary:   #1e1e2f;
            --bg-card:      #ffffff;
            --bg-table:     #2b2b40;
            --accent:       #ff6b6b;
            --accent-light: #ff8787;
            --text-primary: #f0f0f5;
            --text-dark:    #2c2c3e;
            --shadow:       rgba(0,0,0,0.3);
        }

        * { box-sizing: border-box; margin:0; padding:0; }
        body{
            font-family: 'Montserrat', sans-serif;
            background: var(--bg-primary);
            color: var(--text-primary);
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            align-items: center;
            padding: 1rem;
        }

        h1{
            margin: .5rem 0 1rem;
            font-weight: 600;
            font-size: 2.5rem;
            color: var(--accent);
            text-shadow: 0 2px 4px var(--shadow);
        }

        /* ---------- Ana Kapsayıcı ---------- */
        .game-wrapper{
            width: 100%;
            max-width: 1100px;
            background: var(--bg-table);
            border-radius: 12px;
            padding: 1.5rem;
            box-shadow: 0 8px 24px var(--shadow);
            display: grid;
            grid-template-rows: auto 1fr auto;
            gap: 1rem;
        }

        .top-bar{
            display: flex;
            justify-content: space-between;
            font-size: 1.2rem;
        }
        .player{
            display: flex;
            flex-direction: column;
            align-items: center;
        }
        .player span{font-weight:600;margin-top:.2rem;}

        /* ---------- Oyun Alanı ---------- */
        .play-area{
            display: grid;
            grid-template-columns: 1fr 2fr 1fr;
            align-items: center;
            gap: .8rem;
        }
        .hand, .opponent-hand{
            display: flex;
            justify-content: center;
            gap: .4rem;
            flex-wrap: wrap;
        }

        /* Kart Stili */
        .card{
            width: 80px;
            height: 120px;
            perspective: 600px;
            cursor: default;
        }
        .card-inner{
            width: 100%; height:100%;
            transition: transform .6s;
            transform-style: preserve-3d;
        }
        .card:hover .card-inner{transform: rotateY(180deg);}
        .card-front,
        .card-back{
            position: absolute;
            width:100%; height:100%;
            border-radius:8px;
            backface-visibility:hidden;
            border:2px solid var(--accent);
        }
        .card-front{
            background: var(--bg-card);
            display:flex;
            justify-content:center;
            align-items:center;
            font-size:1.6rem;
            color: var(--text-dark);
        }
        .card-back{
            background: var(--accent);
            transform: rotateY(180deg);
        }

        /* Merkez Pile */
        .table-pile{
            position:relative;
            height:150px;
            display:flex;
            justify-content:center;
            align-items:flex-end;
        }
        .table-pile .card{position:absolute;top:0;}
        .table-pile .card:not(:last-child){left:-10px;}

        /* ---------- Alt Kontroller ---------- */
        .bottom-bar{
            display:flex;
            justify-content:center;
            gap:1rem;
        }
        .btn{
            background: var(--accent);
            color:#fff;
            border:none;
            border-radius:6px;
            padding:.6rem 1.4rem;
            font-size:1rem;
            cursor:pointer;
            transition:background .3s,transform .1s;
        }
        .btn:hover{background:var(--accent-light);}
        .btn:active{transform:scale(.96);}

        /* ---------- Responsiveness ---------- */
        @media (max-width:768px){
            .play-area{grid-template-columns:1fr;}
            .hand,.opponent-hand{justify-content:flex-start;}
            .card{width:60px;height:90px;}
        }
    </style>
</head>
<body>

<h1>PİŞTİ</h1>

<div class="game-wrapper">

    <!-- 1️⃣ Üst Çubuk: Oyuncu İsimleri & Puanlar -->
    <div class="top-bar">
        <div class="player" id="you">
            <strong>Sen</strong>
            <span id="score-you">0</span>
        </div>
        <div class="player" id="opponent">
            <strong>Rakip</strong>
            <span id="score-opponent">0</span>
        </div>
    </div>

    <!-- 2️⃣ Oyun Alanı -->
    <div class="play-area">

        <!-- Rakip eli (geri tarafı kapalı) -->
        <div class="opponent-hand" id="opponent-hand">
            <!-- 5 adet kapalı kart örneği -->
            <div class="card"><div class="card-inner"><div class="card-front"></div><div class="card-back"></div></div></div>
            <div class="card"><div class="card-inner"><div class="card-front"></div><div class="card-back"></div></div></div>
            <div class="card"><div class="card-inner"><div class="card-front"></div><div class="card-back"></div></div></div>
            <div class="card"><div class="card-inner"><div class="card-front"></div><div class="card-back"></div></div></div>
            <div class="card"><div class="card-inner"><div class="card-front"></div><div class="card-back"></div></div></div>
        </div>

        <!-- Ortadaki masadaki kart yığını -->
        <div class="table-pile" id="table-pile">
            <!-- Buraya bir kart koyarak “başlangıç kartı” gösterebilirsiniz -->
            <div class="card">
                <div class="card-inner">
                    <div class="card-front">A♠</div>
                    <div class="card-back"></div>
                </div>
            </div>
        </div>

        <!-- Senin elin (ön tarafı görünür) -->
        <div class="hand" id="your-hand">
            <!-- 5 örnek kart – gerçek oyunda JS ile doldurulur -->
            <div class="card"><div class="card-inner"><div class="card-front">K♥</div><div class="card-back"></div></div></div>
            <div class="card"><div class="card-inner"><div class="card-front">7♦</div><div class="card-back"></div></div></div>
            <div class="card"><div class="card-inner"><div class="card-front">2♣</div><div class="card-back"></div></div></div>
            <div class="card"><div class="card-inner"><div class="card-front">J♠</div><div class="card-back"></div></div></div>
            <div class="card"><div class="card-inner"><div class="card-front">10♥</div><div class="card-back"></div></div></div>
        </div>
    </div>

    <!-- 3️⃣ Alt Kontroller -->
    <div class="bottom-bar">
        <button class="btn" id="new-game">Yeni Oyun</button>
        <button class="btn" id="settings">Ayarlar</button>
    </div>

</div>

<!-- ---------------------------------------------------------
     Buraya sadece UI’yı kontrol edecek basit bir demo JS konuldu.
     Gerçek oyun mantığını eklemek isterseniz bu bölümü genişletin.
---------------------------------------------------------- -->
<script>
    // Demo amaçlı sadece butonların aktif olduğunu göstermek
    document.getElementById('new-game').addEventListener('click', () => {
        alert('Yeni oyun başlatıldı – (burada oyun mantığını ekleyin)');
    });
    document.getElementById('settings').addEventListener('click', () => {
        alert('Ayarlar penceresi – (burada bir modal açabilirsiniz)');
    });
</script>

</body>
</html>
```

### Nasıl Kullanılır?

1. **Dosyayı kaydedin** – örneğin `pisiti/index.html`.  
2. Tarayıcıda açın. Görsel olarak modern bir “Pişti” oyun sayfası göreceksiniz.  
3. **Gerçek oyun mantığını** eklemek isterseniz:
   - `#your-hand`, `#opponent-hand` ve `#table-pile` içeriklerini JavaScript ile dinamik olarak doldurun.  
   - Kartları sürükleyip bırakma, puan güncelleme vb. etkileşimleri `script` bölümüne ekleyin.  

Bu sadece **tasarım**; işlevselliği ihtiyacınıza göre genişletebilirsiniz. İyi çalışmalar!

### Amazon Nova 2 Lite
*2025-12-09 10:14:14 +03*

<think>
Okay, the user previously asked for a modern, flashy HTML design for a Pişti game web page. I provided a complete HTML file with CSS and JavaScript placeholders. Now the user says: "Oyun sayfası yapacağız oyun yapmayacağım" which translates to "We will make a game page, I will not make a game." So they want the page design but not the actual game logic.

They probably want a static design without any gameplay functionality. The previous response included placeholder JavaScript for dealing cards and playing, but the user now clarifies they don't want the game logic—just the page structure.

So I need to adjust the response to remove any JavaScript that handles game logic. Provide only the HTML and CSS for the visual design, maybe with static placeholder cards, no interactivity beyond maybe hover effects.

The user might still want the visual elements: header, player scores, opponent hand (face-down cards), player hand (face-up cards), table pile, buttons that look nice but don't do anything. The design should be modern and flashy, using CSS animations/hovers.

I should ensure the code is clean, well-commented, and only includes design. Remove the JavaScript entirely or leave minimal code for UI elements like buttons that do nothing (or just console.log). But better to keep the JavaScript minimal, maybe just to attach event listeners that log to console, so the buttons are clickable but don't affect the game.

Alternatively, I could remove the script tag entirely, leaving only the HTML and CSS. The user said they won't make the game, so the page should be static.

Thus, I should provide HTML with embedded CSS, and maybe a small script that just logs button clicks, but no game logic. Or just omit script entirely.

The user might also want responsive design, modern fonts, animations on card hover, etc.

I should also include comments in the code explaining sections.

Make sure to use modern CSS features: CSS variables, flexbox/grid, transitions for card flip, maybe subtle shadows.

The page should have:

- Title "Pişti"
- Top bar with player names and scores (static numbers)
- Central area: opponent hand (face-down cards), table pile (maybe one card face-up), player hand (face-up cards)
- Buttons: "Yeni Oyun", "Sıfırla" (New Game, Reset) styled nicely.

The cards should have flip animation: when hovered, the card flips to show back (maybe just a solid color). That's purely visual.

I can keep the same CSS as before but remove the JavaScript that deals cards. Instead, hardcode some cards in HTML.

Thus, the final answer should be HTML with CSS and maybe minimal JS for UI interactions (like button clicks logging). But the user said they won't make the game, so perhaps no JS at all.

Better to provide HTML + CSS only, with static content. That meets the requirement: design only, no game logic.

Thus, the answer will be a complete HTML file with embedded CSS, static cards, and styled buttons. No JavaScript or minimal.

I will include comments in HTML to indicate where dynamic content would go.

Make sure to use proper indentation, and explain briefly that this is the design only.

Also, ensure the code is in a markdown code block with language html.

Potentially include a note that the design is responsive and uses modern CSS.

Thus, final answer: HTML with CSS, static placeholders.

Let's write that.
</think>Below is a **pure‑design** HTML page for a **Pişti** game interface.  
It contains only the visual layout (modern, flashy styling) – **no game logic**.  
You can copy the code, open it in a browser, and see how it looks.  

```html
<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Pişti – Modern Tasarım</title>

    <!-- Google Font for a sleek look -->
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600&display=swap" rel="stylesheet">

    <style>
        /* -------------------------------------------------
           CSS Variables – easy colour tweaks
        ------------------------------------------------- */
        :root {
            --bg-primary: #1e1e2f;      /* dark background */
            --bg-table: #2b2b40;        /* game table */
            --accent: #ff6b6b;          /* bright accent */
            --accent-light: #ff8787;    /* lighter accent for hover */
            --card-face: #fff;          /* card face colour */
            --text-primary: #f0f0f5;    /* light text */
           

## Prompt 3

### You
*2025-12-09 10:32:31 +03*

Ktml olarak üstü oyunu salonun için web sayfası tasarımı yapacağım modern ve gösterişli bir tema olarak başlayalım 

### Gemini 3 Pro
*2025-12-09 10:32:31 +03*

<think>
The user wants an HTML design for a "Pişti Oyunu Salonu" (Pişti Game Hall/Lobby).
This is slightly different from the game board itself. It's the "salon" (lobby/hall) where players might see tables, join a game, or see a landing page for the game hall.
They specified "Ktml" which is likely a typo for HTML.
Key words: "salonun için" (for the hall/salon), "web sayfası tasarımı" (web page design), "modern ve gösterişli" (modern and flashy/showy).

So, the requirement is a Landing Page or a Lobby Page for a Pişti game site.

Elements needed:
1.  **Header/Hero Section**: "Pişti Salonu" title, flashy background, "Play Now" button.
2.  **Rooms/Tables List**: A section showing available tables (e.g., "İstanbul Odası", "Ankara Odası", "VIP Salon").
3.  **User Profile/Stats**: Small section showing "Online Players", "Your Balance".
4.  **Footer**: Copyright, links.

Design style: Dark theme (popular for gaming), neon accents (flashy), responsive grid for tables.

I will provide a single HTML file containing CSS and HTML structure.
I will use a dark, gaming-inspired color palette (dark blue/purple background, neon pink/blue accents).
The structure will be:
- Navbar
- Hero Section (Welcome)
- Game Rooms Grid (Salon Lobby)
- Leaderboard/Stats sidebar or section.

Let's write the code.
</think>Harika bir fikir! Bir **"Pişti Oyun Salonu" (Lobby)** tasarımı, oyuncuların oyuna girmeden önce karşılandığı, masaları seçtiği veya skorlarını gördüğü şık bir karşılama ekranı olmalıdır.

Aşağıda, **modern, karanlık mod (dark mode) ve neon efektli** gösterişli bir "Oyun Salonu" giriş sayfası tasarımı yer alıyor. Bu sayfada:
1.  **Hero (Karşılama) Alanı**: Büyük başlık ve "Hemen Oyna" butonu.
2.  **Masalar (Rooms)**: Katılabileceğiniz farklı oyun odaları.
3.  **Liderlik Tablosu**: En iyi oyuncuların listesi.

Bu kodu `index.html` olarak kaydedip çalıştırabilirsiniz.

```html
<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Royal Pişti Salonu</title>
    
    <!-- Modern Fontlar -->
    <link href="https://fonts.googleapis.com/css2?family=Rajdhani:wght@500;700&family=Poppins:wght@300;400;600&display=swap" rel="stylesheet">
    
    <!-- İkon Seti (FontAwesome CDN) -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">

    <style>
        /* --- GENEL AYARLAR & DEĞİŞKENLER --- */
        :root {
            --bg-dark: #0f0f13;
            --bg-panel: #1a1a24;
            --primary: #6c5ce7;       /* Modern Mor */
            --accent: #00cec9;        /* Neon Turkuaz */
            --danger: #ff7675;        /* Soft Kırmızı */
            --text-main: #dfe6e9;
            --text-muted: #b2bec3;
            --neon-shadow: 0 0 10px rgba(108, 92, 231, 0.5);
            --card-radius: 16px;
        }

        * { margin: 0; padding: 0; box-sizing: border-box; }

        body {
            font-family: 'Poppins', sans-serif;
            background-color: var(--bg-dark);
            color: var(--text-main);
            overflow-x: hidden;
        }

        a { text-decoration: none; color: inherit; }
        ul { list-style: none; }

        /* --- NAVBAR --- */
        nav {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 1.5rem 5%;
            background: rgba(26, 26, 36, 0.8);
            backdrop-filter: blur(10px);
            position: sticky;
            top: 0;
            z-index: 100;
            border-bottom: 1px solid rgba(255,255,255,0.05);
        }

        .logo {
            font-family: 'Rajdhani', sans-serif;
            font-size: 1.8rem;
            font-weight: 700;
            color: var(--accent);
            text-transform: uppercase;
            letter-spacing: 2px;
            text-shadow: var(--neon-shadow);
        }

        .user-profile {
            display: flex;
            align-items: center;
            gap: 15px;
        }

        .user-avatar {
            width: 40px;
            height: 40px;
            border-radius: 50%;
            background: var(--primary);
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: bold;
        }

        .coin-balance {
            background: #2d3436;
            padding: 5px 15px;
            border-radius: 20px;
            font-size: 0.9rem;
            color: #fab1a0;
            display: flex;
            align-items: center;
            gap: 8px;
        }

        /* --- HERO (KARŞILAMA) --- */
        header.hero {
            height: 60vh;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            text-align: center;
            background: radial-gradient(circle at center, #2d2d44 0%, var(--bg-dark) 70%);
            position: relative;
        }

        header.hero h1 {
            font-family: 'Rajdhani', sans-serif;
            font-size: 4rem;
            line-height: 1.1;
            margin-bottom: 1rem;
            background: -webkit-linear-gradient(45deg, var(--accent), var(--primary));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        header.hero p {
            font-size: 1.2rem;
            color: var(--text-muted);
            max-width: 600px;
            margin-bottom: 2rem;
        }

        .cta-btn {
            background: linear-gradient(90deg, var(--primary), var(--accent));
            color: #fff;
            padding: 1rem 2.5rem;
            border-radius: 50px;
            font-weight: 600;
            font-size: 1.1rem;
            transition: transform 0.3s, box-shadow 0.3s;
            border: none;
            cursor: pointer;
        }

        .cta-btn:hover {
            transform: translateY(-3px);
            box-shadow: 0 10px 20px rgba(108, 92, 231, 0.4);
        }

        /* --- MAIN CONTENT GRID --- */
        .container {
            display: grid;
            grid-template-columns: 3fr 1fr;
            gap: 2rem;
            padding: 2rem 5%;
            max-width: 1400px;
            margin: 0 auto;
        }

        /* --- ROOMS (MASALAR) --- */
        .section-title {
            font-size: 1.5rem;
            margin-bottom: 1.5rem;
            border-left: 4px solid var(--accent);
            padding-left: 10px;
        }

        .rooms-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
            gap: 1.5rem;
        }

        .room-card {
            background: var(--bg-panel);
            border-radius: var(--card-radius);
            padding: 1.5rem;
            transition: all 0.3s ease;
            position: relative;
            overflow: hidden;
            border: 1px solid rgba(255,255,255,0.05);
        }

        .room-card:hover {
            transform: translateY(-5px);
            border-color: var(--primary);
            box-shadow: 0 5px 15px rgba(0,0,0,0.5);
        }

        .room-card::before {
            content: '';
            position: absolute;
            top: 0; left: 0; width: 100%; height: 4px;
            background: linear-gradient(90deg, var(--primary), var(--accent));
        }

        .room-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 1rem;
        }

        .room-name {
            font-weight: 600;
            font-size: 1.2rem;
        }

        .room-stake {
            font-size: 0.9rem;
            color: #fab1a0;
        }

        .room-info {
            display: flex;
            justify-content: space-between;
            font-size: 0.9rem;
            color: var(--text-muted);
            margin-bottom: 1.5rem;
        }

        .join-btn {
            width: 100%;
            padding: 0.8rem;
            background: transparent;
            border: 1px solid var(--primary);
            color: var(--primary);
            border-radius: 8px;
            cursor: pointer;
            transition: 0.3s;
        }

        .join-btn:hover {
            background: var(--primary);
            color: #fff;
        }

        /* --- SIDEBAR (LEADERBOARD) --- */
        .sidebar {
            background: var(--bg-panel);
            border-radius: var(--card-radius);
            padding: 1.5rem;
            height: fit-content;
        }

        .player-list li {
            display: flex;
            align-items: center;
            padding: 10px 0;
            border-bottom: 1px solid rgba(255,255,255,0.05);
        }
        .player-list li:last-child { border: none; }

        .rank {
            font-weight: bold;
            color: var(--accent);
            width: 30px;
        }

        .p-info {
            flex: 1;
            margin-left: 10px;
        }
        .p-name { font-size: 0.95rem; display: block; }
        .p-score { font-size: 0.8rem; color: var(--text-muted); }

        /* --- RESPONSIVE --- */
        @media (max-width: 900px) {
            .container { grid-template-columns: 1fr; }
            header.hero h1 { font-size: 2.5rem; }
        }
    </style>
</head>
<body>

    <!-- Üst Menü -->
    <nav>
        <div class="logo"><i class="fas fa-crown"></i> ROYAL PİŞTİ</div>
        <div class="user-profile">
            <div class="coin-balance">
                <i class="fas fa-coins"></i> 2,500
            </div>
            <div class="user-avatar">
                <i class="fas fa-user"></i>
            </div>
        </div>
    </nav>

    <!-- Karşılama Alanı -->
    <header class="hero">
        <h1>Efsaneler Masaya!</h1>
        <p>Türkiye'nin en hızlı ve en modern Pişti salonuna hoş geldin. Masanı seç, rakiplerini yen ve sıralamada yüksel.</p>
        <button class="cta-btn"><i class="fas fa-play"></i> Hızlı Oyna</button>
    </header>

    <!-- Ana İçerik -->
    <div class="container">
        
        <!-- Sol: Masalar -->
        <main>
            <h2 class="section-title">Aktif Salonlar</h2>
            <div class="rooms-grid">
                
                <!-- Masa 1 -->
                <div class="room-card">
                    <div class="room-header">
                        <span class="room-name">Acemi Odası</span>
                        <span class="room-stake"><i class="fas fa-coins"></i> 100</span>
                    </div>
                    <div class="room-info">
                        <span><i class="fas fa-users"></i> 124 Oyuncu</span>
                        <span>Normal Hız</span>
                    </div>
                    <button class="join-btn">Katıl</button>
                </div>

                <!-- Masa 2 -->
                <div class="room-card">
                    <div class="room-header">
                        <span class="room-name">İstanbul Salonu</span>
                        <span class="room-stake"><i class="fas fa-coins"></i> 500</span>
                    </div>
                    <div class="room-info">
                        <span><i class="fas fa-users"></i> 85 Oyuncu</span>
                        <span>Hızlı Oyun</span>
                    </div>
                    <button class="join-btn">Katıl</button>
                </div>

                <!-- Masa 3 -->
                <div class="room-card">
                    <div class="room-header">
                        <span class="room-name">VIP Lounge</span>
                        <span class="room-stake"><i class="fas fa-coins"></i> 5,000</span>
                    </div>
                    <div class="room-info">
                        <span><i class="fas fa-users"></i> 12 Oyuncu</span>
                        <span>2x Puan</span>
                    </div>
                    <button class="join-btn">Katıl</button>
                </div>

                <!-- Masa 4 -->
                <div class="room-card">
                    <div class="room-header">
                        <span class="room-name">Turnuva Masası</span>
                        <span class="room-stake"><i class="fas fa-trophy"></i> Ödüllü</span>
                    </div>
                    <div class="room-info">
                        <span><i class="fas fa-users"></i> 200+ Bekleyen</span>
                        <span>Başlıyor...</span>
                    </div>
                    <button class="join-btn">Kayıt Ol</button>
                </div>

            </div>
        </main>

        <!-- Sağ: Sıralama -->
        <aside class="sidebar">
            <h3 class="section-title" style="font-size: 1.2rem;">Haftanın Liderleri</h3>
            <ul class="player-list">
                <li>
                    <span class="rank">1</span>
                    <div class="user-avatar" style="width:30px;height:30px;font-size:0.8rem;">AH</div>
                    <div class="p-info">
                        <span class="p-name">Ahmet K.</span>
                        <span class="p-score">15,400 Puan</span>
                    </div>
                </li>
                <li>
                    <span class="rank">2</span>
                    <div class="user-avatar" style="width:30px;height:30px;font-size:0.8rem; background: var(--accent);">EL</div>
                    <div class="p-info">
                        <span class="p-name">Elif Y.</span>
                        <span class="p-score">14,250 Puan</span>
                    </div>
                </li>
                <li>
                    <span class="rank">3</span>
                    <div class="user-avatar" style="width:30px;height:30px;font-size:0.8rem; background: var(--danger);">MR</div>
                    <div class="p-info">
                        <span class="p-name">Murat B.</span>
                        <span class="p-score">12,100 Puan</span>
                    </div>
                </li>
                <li>
                    <span class="rank">4</span>
                    <div class="user-avatar" style="width:30px;height:30px;font-size:0.8rem; background: #555;">SE</div>
                    <div class="p-info">
                        <span class="p-name">Selin D.</span>
                        <span class="p-score">9,800 Puan</span>
                    </div>
                </li>
            </ul>
        </aside>

    </div>

</body>
</html>
```

### Tasarımın Özellikleri:
1.  **Gösterişli Renk Paleti:** Koyu arka plan (`#0f0f13`) üzerine Mor ve Turkuaz neon vurgular kullanılarak modern bir "Gaming" havası verildi.
2.  **Card (Kart) Yapısı:** Masalar (Rooms) birbirinden ayrılmış kartlar halindedir. Üzerine gelindiğinde (Hover) hafifçe yukarı kalkar ve gölgelendirme efektine sahiptir.
3.  **Hero Bölümü:** Sayfanın en üstünde dikkat çekici bir başlık ve "Hızlı Oyna" butonu ile kullanıcıyı doğrudan oyuna davet eder.
4.  **Responsive (Duyarlı):** Mobil cihazlarda masaüstü düzeninden tek sütuna sorunsuzca geçer.

Bu sayfayı projenizin **Giriş / Lobby** sayfası olarak kullanabilirsiniz.

### Gemini 3 Pro (Low)
*2025-12-09 10:32:31 +03*

<think>
The user is asking for a web page design for a "Pişti oyunu salonu" (Pişti game hall/lobby).
User says "Ktml olarak üstü oyunu salonun için web sayfası tasarımı yapacağım".
Correction: "Html olarak pişti oyunu salonu için..."
The goal: A modern and flashy theme for a game lobby (salon). This is not the game board itself, but the entry page or lobby where players see rooms, tables, chat, or a generic "Play Now" interface.

Key elements for a game hall/lobby:
1.  **Header/Hero Section:** Flashy title, perhaps a "Play Now" CTA.
2.  **Room/Table List:** A grid or list showing active tables (e.g., "Table #1 - 2/4 Players").
3.  **User Profile/Stats:** Sidebar or top section showing user avatar, coins/chips, rank.
4.  **Chat/Online Users:** Optional but common in game halls.
5.  **Modern Aesthetic:** Dark mode is usually preferred for gaming ("neon", "cyberpunk", or sleek dark UI). Glassmorphism (translucent backgrounds) is modern.

I will create a single HTML file with embedded CSS.
Theme: Dark background, neon accents (purple/pink/blue), sleek cards for tables.

Structure:
-   Navbar: Logo, User Profile, Coins.
-   Main Content:
    -   Filters (All Rooms, VIP, Tournament).
    -   Grid of Tables.
-   Sidebar (optional, maybe keep it simple for mobile compatibility).

Tech stack: HTML5, CSS3 (Flexbox, Grid, Variables). No external images needed (use CSS shapes or placeholders).

Let's refine the "flashy" aspect:
-   Gradient text for the logo.
-   Hover effects on table cards (scale up, glow).
-   "Pulse" animation for "Live" status.

Plan:
1.  Define CSS variables for the theme.
2.  Build the Layout.
3.  Add dummy data for tables.

I will write the code in Turkish comments and content as requested.
</think>Harika bir fikir! Bir oyun salonu (lobby) tasarımı, oyuncuları karşılayan, heyecanlandıran ve masalara yönlendiren **vitrin** gibidir. Modern ve "gösterişli" (flashy) olması için genellikle **koyu tema (dark mode)**, **neon vurgular**, **cam efekti (glassmorphism)** ve **yumuşak animasyonlar** tercih edilir.

Aşağıda, bir **Pişti Oyun Salonu (Lobby)** için hazırladığım modern HTML/CSS tasarımını bulabilirsin. Bu kod, oyuncuların masaları gördüğü, profilini incelediği şık bir giriş sayfasıdır.

### Özellikler:
*   **Neon & Dark Tema:** Mor ve turkuaz tonlarıyla modern oyun atmosferi.
*   **Glassmorphism:** Yarı saydam paneller.
*   **Responsive:** Telefondan bilgisayara uyumlu ızgara (grid) yapısı.
*   **Animasyonlar:** Butonlarda ve kartlarda yumuşak geçişler.

Bu kodu `lobby.html` olarak kaydedip çalıştırabilirsin.

```html
<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Pişti Arena - Oyun Salonu</title>
    
    <!-- Modern Font -->
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;500;700&display=swap" rel="stylesheet">
    
    <style>
        /* --- TEMEL AYARLAR & DEĞİŞKENLER --- */
        :root {
            --bg-dark: #0f172a;
            --bg-panel: rgba(30, 41, 59, 0.7);
            --primary: #8b5cf6; /* Mor */
            --secondary: #06b6d4; /* Turkuaz */
            --accent: #f43f5e; /* Kırmızı/Pembe */
            --text-main: #f8fafc;
            --text-muted: #94a3b8;
            --glass-border: 1px solid rgba(255, 255, 255, 0.1);
            --glow: 0 0 20px rgba(139, 92, 246, 0.5);
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }

        body {
            font-family: 'Outfit', sans-serif;
            background-color: var(--bg-dark);
            /* Arka plana hafif bir gradyan ekleyelim */
            background-image: radial-gradient(circle at 10% 20%, rgba(139, 92, 246, 0.15) 0%, transparent 40%),
                              radial-gradient(circle at 90% 80%, rgba(6, 182, 212, 0.15) 0%, transparent 40%);
            color: var(--text-main);
            min-height: 100vh;
            overflow-x: hidden;
        }

        /* --- NAVBAR --- */
        header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 1rem 2rem;
            background: rgba(15, 23, 42, 0.8);
            backdrop-filter: blur(10px);
            border-bottom: var(--glass-border);
            position: sticky;
            top: 0;
            z-index: 100;
        }

        .logo {
            font-size: 1.8rem;
            font-weight: 700;
            background: linear-gradient(135deg, var(--secondary), var(--primary));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            text-transform: uppercase;
            letter-spacing: 1px;
        }

        .user-panel {
            display: flex;
            align-items: center;
            gap: 1.5rem;
        }

        .chip-count {
            background: rgba(255, 255, 255, 0.1);
            padding: 0.5rem 1rem;
            border-radius: 20px;
            font-size: 0.9rem;
            display: flex;
            align-items: center;
            gap: 0.5rem;
            border: var(--glass-border);
        }
        .chip-icon { color: #fbbf24; } /* Altın rengi */

        .avatar {
            width: 40px;
            height: 40px;
            border-radius: 50%;
            background: linear-gradient(45deg, var(--primary), var(--secondary));
            border: 2px solid #fff;
        }

        /* --- ANA İÇERİK --- */
        main {
            padding: 2rem;
            max-width: 1200px;
            margin: 0 auto;
        }

        .hero-section {
            text-align: center;
            margin-bottom: 3rem;
            animation: fadeIn 1s ease;
        }

        .hero-title {
            font-size: 3rem;
            margin-bottom: 0.5rem;
        }
        .hero-subtitle {
            color: var(--text-muted);
            font-size: 1.1rem;
        }

        .play-btn {
            margin-top: 1.5rem;
            padding: 1rem 2.5rem;
            font-size: 1.2rem;
            font-weight: 600;
            background: linear-gradient(90deg, var(--primary), var(--secondary));
            border: none;
            border-radius: 50px;
            color: #fff;
            cursor: pointer;
            box-shadow: var(--glow);
            transition: transform 0.2s, box-shadow 0.2s;
        }
        .play-btn:hover {
            transform: scale(1.05);
            box-shadow: 0 0 30px rgba(139, 92, 246, 0.8);
        }

        /* --- FİLTRELER --- */
        .filters {
            display: flex;
            gap: 1rem;
            margin-bottom: 2rem;
            overflow-x: auto;
            padding-bottom: 0.5rem;
        }
        .filter-btn {
            background: var(--bg-panel);
            border: var(--glass-border);
            color: var(--text-muted);
            padding: 0.6rem 1.2rem;
            border-radius: 12px;
            cursor: pointer;
            transition: all 0.3s;
            white-space: nowrap;
        }
        .filter-btn.active, .filter-btn:hover {
            background: var(--primary);
            color: #fff;
            border-color: var(--primary);
        }

        /* --- MASALAR GRID --- */
        .tables-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
            gap: 1.5rem;
        }

        /* MASA KARTI */
        .table-card {
            background: var(--bg-panel);
            backdrop-filter: blur(12px);
            border: var(--glass-border);
            border-radius: 16px;
            padding: 1.5rem;
            position: relative;
            transition: transform 0.3s, border-color 0.3s;
            overflow: hidden;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            min-height: 200px;
        }

        .table-card:hover {
            transform: translateY(-5px);
            border-color: var(--secondary);
        }

        /* Parlama efekti (arka plan süslemesi) */
        .table-card::before {
            content: '';
            position: absolute;
            top: -50%; left: -50%;
            width: 200%; height: 200%;
            background: radial-gradient(circle, rgba(255,255,255,0.03) 0%, transparent 60%);
            transform: rotate(45deg);
            pointer-events: none;
        }

        .card-header {
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
            margin-bottom: 1rem;
        }
        .room-name {
            font-size: 1.2rem;
            font-weight: 700;
        }
        .room-type {
            font-size: 0.8rem;
            color: var(--secondary);
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }

        .stakes {
            font-size: 1.5rem;
            font-weight: 700;
            color: #fbbf24;
            margin-bottom: 0.5rem;
        }
        .stakes span { font-size: 0.9rem; color: var(--text-muted); font-weight: 400; }

        .players-bar {
            margin-top: auto;
        }
        .bar-bg {
            width: 100%;
            height: 6px;
            background: rgba(255,255,255,0.1);
            border-radius: 3px;
            overflow: hidden;
            margin-bottom: 0.5rem;
        }
        .bar-fill {
            height: 100%;
            background: var(--secondary);
            width: 50%; /* Dinamik olarak değişecek */
            border-radius: 3px;
        }
        .player-count {
            font-size: 0.85rem;
            color: var(--text-muted);
            display: flex;
            justify-content: space-between;
        }

        .join-btn {
            margin-top: 1rem;
            width: 100%;
            padding: 0.8rem;
            background: rgba(255,255,255,0.05);
            border: 1px solid rgba(255,255,255,0.1);
            color: #fff;
            border-radius: 8px;
            cursor: pointer;
            transition: background 0.3s;
        }
        .join-btn:hover {
            background: var(--primary);
            border-color: var(--primary);
        }

        /* Özel Masa Stili (VIP) */
        .table-card.vip {
            border: 1px solid rgba(244, 63, 94, 0.4);
            box-shadow: 0 0 15px rgba(244, 63, 94, 0.2);
        }
        .table-card.vip .room-type { color: var(--accent); }
        .table-card.vip .bar-fill { background: var(--accent); }

        /* Animation Keyframes */
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }

        /* Mobile */
        @media (max-width: 768px) {
            .hero-title { font-size: 2rem; }
            header { padding: 1rem; }
            .user-panel span { display: none; } /* Mobilde "Bakiye" yazısını gizle */
        }
    </style>
</head>
<body>

    <!-- ÜST MENÜ -->
    <header>
        <div class="logo">PİŞTİ<span style="color:#fff; font-weight:300;">ARENA</span></div>
        
        <div class="user-panel">
            <div class="chip-count">
                <span class="chip-icon">●</span>
                <span>12,500 ₺</span>
            </div>
            <div class="avatar" title="Kullanıcı Profili"></div>
        </div>
    </header>

    <!-- ANA ALAN -->
    <main>
        
        <!-- KARŞILAMA / HERO -->
        <div class="hero-section">
            <h1 class="hero-title">Rakiplerini Bekliyor!</h1>
            <p class="hero-subtitle">Hemen bir masaya otur veya kendi özel odanı kur.</p>
            <button class="play-btn">Hızlı Oyna</button>
        </div>

        <!-- FİLTRELER -->
        <div class="filters">
            <button class="filter-btn active">Tüm Odalar</button>
            <button class="filter-btn">VIP Masalar</button>
            <button class="filter-btn">Turnuva</button>
            <button class="filter-btn">Arkadaşların</button>
        </div>

        <!-- MASALAR LİSTESİ -->
        <div class="tables-grid">

            <!-- Masa 1 -->
            <div class="table-card">
                <div class="card-header">
                    <div>
                        <div class="room-type">Standart</div>
                        <div class="room-name">İstanbul Odası</div>
                    </div>
                    <div style="color:#22c55e;">● Canlı</div>
                </div>
                <div class="stakes">100 <span>Bahis</span></div>
                <div class="players-bar">
                    <div class="bar-bg"><div class="bar-fill" style="width: 75%;"></div></div>
                    <div class="player-count">
                        <span>Doluluk</span>
                        <span>3/4</span>
                    </div>
                </div>
                <button class="join-btn">Katıl</button>
            </div>

            <!-- Masa 2 (VIP) -->
            <div class="table-card vip">
                <div class="card-header">
                    <div>
                        <div class="room-type">VIP ELITE</div>
                        <div class="room-name">Kıbrıs Casinası</div>
                    </div>
                    <div style="color:#f43f5e;">● Sıcak</div>
                </div>
                <div class="stakes">5.000 <span>Bahis</span></div>
                <div class="players-bar">
                    <div class="bar-bg"><div class="bar-fill" style="width: 50%;"></div></div>
                    <div class="player-count">
                        <span>Doluluk</span>
                        <span>2/4</span>
                    </div>
                </div>
                <button class="join-btn">Katıl</button>
            </div>

            <!-- Masa 3 -->
            <div class="table-card">
                <div class="card-header">
                    <div>
                        <div class="room-type">Hızlı Oyun</div>
                        <div class="room-name">Ege Sahili</div>
                    </div>
                    <div style="color:#22c55e;">● Canlı</div>
                </div>
                <div class="stakes">500 <span>Bahis</span></div>
                <div class="players-bar">
                    <div class="bar-bg"><div class="bar-fill" style="width: 25%;"></div></div>
                    <div class="player-count">
                        <span>Doluluk</span>
                        <span>1/4</span>
                    </div>
                </div>
                <button class="join-btn">Katıl</button>
            </div>

            <!-- Masa 4 -->
            <div class="table-card">
                <div class="card-header">
                    <div>
                        <div class="room-type">Turnuva</div>
                        <div class="room-name">Haftalık Kupa</div>
                    </div>
                    <div style="color:#fbbf24;">● Başlıyor</div>
                </div>
                <div class="stakes">1.000 <span>Giriş</span></div>
                <div class="players-bar">
                    <div class="bar-bg"><div class="bar-fill" style="width: 90%;"></div></div>
                    <div class="player-count">
                        <span>Kayıtlı</span>
                        <span>18/20</span>
                    </div>
                </div>
                <button class="join-btn">Kayıt Ol</button>
            </div>

             <!-- Masa 5 -->
             <div class="table-card">
                <div class="card-header">
                    <div>
                        <div class="room-type">Standart</div>
                        <div class="room-name">Ankara Loş</div>
                    </div>
                    <div style="color:#22c55e;">● Canlı</div>
                </div>
                <div class="stakes">250 <span>Bahis</span></div>
                <div class="players-bar">
                    <div class="bar-bg"><div class="bar-fill" style="width: 50%;"></div></div>
                    <div class="player-count">
                        <span>Doluluk</span>
                        <span>2/4</span>
                    </div>
                </div>
                <button class="join-btn">Katıl</button>
            </div>

             <!-- Masa 6 Yeni Masa -->
             <div class="table-card" style="border-style: dashed; justify-content: center; align-items: center; cursor: pointer; opacity: 0.7;">
                <div style="font-size: 3rem; color: var(--secondary);">+</div>
                <div style="margin-top: 10px;">Masa Oluştur</div>
            </div>

        </div>
    </main>

    <script>
        // Basit etkileşim scripti
        const buttons = document.querySelectorAll('.join-btn');
        buttons.forEach(btn => {
            btn.addEventListener('click', function() {
                // Burada gerçek oyuna yönlendirme yapılır
                alert("Masaya bağlanılıyor...");
            });
        });

        const filters = document.querySelectorAll('.filter-btn');
        filters.forEach(filter => {
            filter.addEventListener('click', () => {
                document.querySelector('.filter-btn.active').classList.remove('active');
                filter.classList.add('active');
            });
        });
    </script>
</body>
</html>
```

### Tasarım İpuçları:
1.  **Arka Plan:** `radial-gradient` kullanılarak çok hafif mor ve mavi ışık huzmeleri eklendi. Bu, sayfaya derinlik katar.
2.  **Glassmorphism:** Masaların ve menünün arkasındaki `backdrop-filter: blur(12px)` özelliği, modern cam görünümünü sağlar.
3.  **Hiyerarşi:** "Hızlı Oyna" butonu en belirgin, VIP masalar parlak çerçeveli, standart masalar daha sade tasarlandı.
4.  **Renk Paleti:** Koyu lacivert arka plan üzerine Neon Mor (`#8b5cf6`) ve Turkuaz (`#06b6d4`) kullanılarak "Gaming" hissi verildi.

## Prompt 4

### You
*2025-12-09 10:41:32 +03*

Daha çok daha modern ve göz alıcı Ultra profesyonelce 2 sitesi oyun sitesi tasarlamaya devam edelim yeni fonksiyonlar da yeni özellikleri Hepsi de Sırlar ekle 

### Gemini 3 Pro
*2025-12-09 10:41:33 +03*

<think>
The user wants to take the previous "Pişti Game Hall" design to the next level: "Ultra professional," "more modern," "eye-catching," "add new functions," "new features," and "secrets/easter eggs."

Let's break down the requirements:
1.  **Ultra Modern & Eye-Catching**: Needs advanced CSS effects. Glassmorphism (blur backgrounds), animated gradients, glowing neon text, smooth transitions, maybe some particle effects or background animations.
2.  **Professional Layout**: A sidebar navigation, a refined dashboard look, notifications area, detailed stats.
3.  **New Functions/Features**:
    *   **Live Chat/Global Chat**: A chat widget.
    *   **Daily Rewards**: A visible countdown or claim button.
    *   **Settings/Preferences**: Toggle for sound/music.
    *   **Avatar Customization**: A hint of profile editing.
    *   **Matchmaking Status**: "Looking for game..." indicator.
4.  **Secrets/Easter Eggs**: A hidden interaction. For example, clicking the logo multiple times triggers a confetti effect or changes the theme color (I can add a JavaScript snippet for this).

**Plan:**
-   **Structure**: Sidebar (left), Main Content (center), Social/Chat (right).
-   **Visual Style**: "Cyberpunk/Futuristic Casino" vibe. Deep purple/black gradients, glass panels (`backdrop-filter: blur`), floating elements.
-   **CSS**: Keyframe animations for "live" indicators, gradient borders.
-   **JS**:
    -   Simple tab switching (Lobby vs Leaderboard vs Shop).
    -   A "Secret" konami code or click listener.
    -   Interactive buttons.

**Content to include:**
-   Sidebar: Dashboard, Games, Tournaments, Shop, Settings.
-   Header: User stats, Level progress bar, Notifications.
-   Main: Featured tables (Carousel style?), Active Tournaments.
-   Right Panel: Global Chat, Friends Online.

I will write a single file solution again for ease of use, but organized cleanly.

Let's refine the "Secret": Clicking the "Level" badge 5 times unlocks a "Rainbow Mode" or shows a hidden message.

Let's start coding.
</think>Harika! Çıtayı yükseltiyoruz. **"Ultra Profesyonel"**, **Glassmorphism (Buzlu Cam)** efektleri, **animasyonlu arka planlar**, **canlı sohbet**, **mağaza** ve içine gizlenmiş **sürpriz (easter egg)** özellikleriyle tam teşekküllü bir oyun platformu arayüzü tasarlayalım.

Bu tasarımda şunları bulacaksınız:
1.  **Glassmorphism Arayüz:** Yarı saydam paneller ve bulanık arka planlar.
2.  **Canlı Efektler:** Yanıp sönen "Canlı" göstergeleri, hareketli gradientler.
3.  **Sidebar Menü & Global Chat:** Sol tarafta profesyonel menü, sağda oyuncu sohbeti.
4.  **Gizli Sır (Easter Egg):** Logoya hızlıca **5 kez tıklarsanız** tüm sitenin teması "Parti Modu"na geçer! 🤫

Kodu `index.html` olarak kaydedin ve tarayıcıda tam ekran açın.

```html
<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>NEXUS Pişti Arena - Ultra Pro</title>
    
    <!-- İkonlar ve Fontlar -->
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;500;700;900&display=swap" rel="stylesheet">

    <style>
        /* --- ULTRA MODERN CSS DEĞİŞKENLERİ --- */
        :root {
            --bg-deep: #050510;
            --glass-bg: rgba(255, 255, 255, 0.05);
            --glass-border: rgba(255, 255, 255, 0.1);
            --neon-blue: #00f3ff;
            --neon-purple: #bc13fe;
            --neon-green: #0aff60;
            --text-glow: 0 0 15px rgba(188, 19, 254, 0.5);
            --font-main: 'Outfit', sans-serif;
            --sidebar-width: 260px;
        }

        * { margin:0; padding:0; box-sizing:border-box; outline:none; }
        
        body {
            background-color: var(--bg-deep);
            color: #fff;
            font-family: var(--font-main);
            height: 100vh;
            overflow: hidden;
            background-image: 
                radial-gradient(circle at 10% 20%, rgba(188, 19, 254, 0.15) 0%, transparent 40%),
                radial-gradient(circle at 90% 80%, rgba(0, 243, 255, 0.15) 0%, transparent 40%);
        }

        /* --- LAYOUT GRID --- */
        .app-container {
            display: grid;
            grid-template-columns: var(--sidebar-width) 1fr 300px;
            height: 100vh;
        }

        /* --- 1. SOL SIDEBAR --- */
        .sidebar {
            background: rgba(10, 10, 20, 0.6);
            backdrop-filter: blur(20px);
            border-right: 1px solid var(--glass-border);
            padding: 2rem;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
        }

        .logo-area {
            cursor: pointer;
            user-select: none;
        }
        .logo-area h1 {
            font-size: 1.8rem;
            font-weight: 900;
            background: linear-gradient(to right, #fff, var(--neon-blue));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            letter-spacing: -1px;
        }
        .logo-subtitle {
            font-size: 0.7rem;
            color: var(--neon-purple);
            letter-spacing: 4px;
            text-transform: uppercase;
        }

        .menu-items { margin-top: 3rem; }
        .menu-link {
            display: flex;
            align-items: center;
            padding: 1rem;
            color: #889;
            text-decoration: none;
            border-radius: 12px;
            margin-bottom: 0.5rem;
            transition: 0.3s;
            position: relative;
        }
        .menu-link i { width: 25px; font-size: 1.2rem; }
        .menu-link:hover, .menu-link.active {
            background: linear-gradient(90deg, rgba(188,19,254,0.1), transparent);
            color: #fff;
            border-left: 3px solid var(--neon-purple);
        }
        .badge {
            background: var(--neon-purple);
            font-size: 0.7rem;
            padding: 2px 6px;
            border-radius: 4px;
            margin-left: auto;
            box-shadow: 0 0 10px var(--neon-purple);
        }

        /* --- 2. ORTA ALAN (MAIN) --- */
        .main-content {
            overflow-y: auto;
            padding: 2rem;
            position: relative;
        }

        /* Header */
        .top-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 2rem;
        }
        .search-bar {
            background: var(--glass-bg);
            border: 1px solid var(--glass-border);
            padding: 0.8rem 1.5rem;
            border-radius: 30px;
            width: 300px;
            color: #fff;
            display: flex;
            align-items: center;
            gap: 10px;
        }
        .user-stats {
            display: flex;
            gap: 20px;
        }
        .stat-box {
            background: var(--glass-bg);
            padding: 0.5rem 1rem;
            border-radius: 12px;
            border: 1px solid var(--glass-border);
            display: flex;
            align-items: center;
            gap: 10px;
        }
        .stat-box i.gold { color: #ffd700; }
        .stat-box i.diamond { color: var(--neon-blue); }

        /* Banner */
        .hero-banner {
            background: linear-gradient(135deg, rgba(188,19,254,0.8), rgba(10,10,20,0.9)), url('https://images.unsplash.com/photo-1511193311914-0346f16efe90?auto=format&fit=crop&w=1000&q=80');
            background-size: cover;
            border-radius: 20px;
            padding: 3rem;
            margin-bottom: 2rem;
            position: relative;
            overflow: hidden;
            border: 1px solid rgba(255,255,255,0.1);
            box-shadow: 0 10px 40px rgba(0,0,0,0.5);
        }
        .hero-banner h2 { font-size: 2.5rem; margin-bottom: 1rem; }
        .hero-banner p { max-width: 500px; color: #ddd; margin-bottom: 1.5rem; }
        .play-btn {
            background: #fff;
            color: #000;
            padding: 1rem 2.5rem;
            border-radius: 30px;
            font-weight: 800;
            border: none;
            cursor: pointer;
            text-transform: uppercase;
            box-shadow: 0 0 20px rgba(255,255,255,0.4);
            transition: 0.3s;
        }
        .play-btn:hover { transform: scale(1.05); box-shadow: 0 0 30px rgba(255,255,255,0.6); }

        /* Game Grid */
        .section-title { font-size: 1.4rem; margin-bottom: 1rem; display: flex; align-items: center; gap: 10px; }
        .games-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 1.5rem;
        }
        .game-card {
            background: var(--glass-bg);
            border: 1px solid var(--glass-border);
            border-radius: 16px;
            padding: 15px;
            transition: 0.4s;
            position: relative;
            overflow: hidden;
            cursor: pointer;
        }
        .game-card:hover {
            transform: translateY(-10px);
            border-color: var(--neon-blue);
            box-shadow: 0 0 20px rgba(0, 243, 255, 0.2);
        }
        .card-img {
            height: 140px;
            background: #222;
            border-radius: 12px;
            margin-bottom: 1rem;
            background-size: cover;
            background-position: center;
        }
        .live-badge {
            position: absolute;
            top: 25px; left: 25px;
            background: red;
            color: white;
            font-size: 0.6rem;
            padding: 2px 8px;
            border-radius: 4px;
            animation: pulse 1.5s infinite;
        }

        /* --- 3. SAĞ PANEL (SOCIAL) --- */
        .right-panel {
            background: rgba(10, 10, 20, 0.4);
            border-left: 1px solid var(--glass-border);
            padding: 1.5rem;
            display: flex;
            flex-direction: column;
        }
        .panel-header { font-weight: 700; margin-bottom: 1.5rem; color: var(--text-muted); }
        
        .chat-box {
            flex: 1;
            background: rgba(0,0,0,0.3);
            border-radius: 12px;
            padding: 10px;
            overflow-y: auto;
            margin-bottom: 1rem;
            font-size: 0.85rem;
        }
        .chat-msg { margin-bottom: 8px; }
        .chat-user { color: var(--neon-blue); font-weight: bold; }
        .chat-text { color: #ccc; }

        .chat-input {
            display: flex;
            gap: 5px;
        }
        .chat-input input {
            flex: 1;
            background: #222;
            border: 1px solid #333;
            color: #fff;
            padding: 8px;
            border-radius: 6px;
        }

        /* ANIMASYONLAR */
        @keyframes pulse {
            0% { opacity: 1; }
            50% { opacity: 0.5; }
            100% { opacity: 1; }
        }
        
        /* GİZLİ PARTİ MODU */
        body.party-mode {
            background: linear-gradient(45deg, #ff0000, #00ff00, #0000ff);
            background-size: 400% 400%;
            animation: gradientBG 2s ease infinite;
        }
        @keyframes gradientBG {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }
    </style>
</head>
<body>

<div class="app-container">
    
    <!-- 1. SOL MENÜ -->
    <aside class="sidebar">
        <div class="logo-area" id="secretLogo">
            <h1>NEXUS</h1>
            <div class="logo-subtitle">PRO GAMING ARENA</div>
        </div>

        <div class="menu-items">
            <a href="#" class="menu-link active"><i class="fas fa-home"></i> Salon</a>
            <a href="#" class="menu-link"><i class="fas fa-gamepad"></i> Turnuvalar <span class="badge">YENİ</span></a>
            <a href="#" class="menu-link"><i class="fas fa-chart-line"></i> Sıralama</a>
            <a href="#" class="menu-link"><i class="fas fa-store"></i> Market</a>
            <a href="#" class="menu-link"><i class="fas fa-users"></i> Klanlar</a>
            <br>
            <a href="#" class="menu-link"><i class="fas fa-cog"></i> Ayarlar</a>
        </div>

        <div class="daily-reward" style="background: linear-gradient(45deg, var(--neon-purple), var(--primary)); padding: 15px; border-radius: 12px; margin-top: auto; text-align: center;">
            <div style="font-size: 0.8rem; margin-bottom: 5px;">Günlük Ödül</div>
            <div style="font-weight: bold; font-size: 1.1rem;">500 Çip</div>
            <button style="margin-top:5px; background:rgba(0,0,0,0.3); border:none; color:#fff; padding:5px 10px; border-radius:4px; cursor:pointer; font-size:0.8rem;">Topla</button>
        </div>
    </aside>

    <!-- 2. ORTA İÇERİK -->
    <main class="main-content">
        <!-- Üst Bar -->
        <div class="top-header">
            <div class="search-bar">
                <i class="fas fa-search"></i>
                <input type="text" placeholder="Masa veya arkadaş ara..." style="background:transparent; border:none; color:#fff; width:100%;">
            </div>
            <div class="user-stats">
                <div class="stat-box">
                    <i class="fas fa-coins gold"></i> <span>24.5K</span>
                </div>
                <div class="stat-box">
                    <i class="fas fa-gem diamond"></i> <span>150</span>
                </div>
                <div class="profile-pic" style="width:40px; height:40px; background:url('https://i.pravatar.cc/100?img=33'); background-size:cover; border-radius:50%; border:2px solid var(--neon-green);"></div>
            </div>
        </div>

        <!-- Banner -->
        <div class="hero-banner">
            <h2>Büyük Turnuva Başlıyor!</h2>
            <p>Sezonun en büyük Pişti turnuvası bu hafta sonu. Toplam ödül havuzu 1.000.000 Çip!</p>
            <button class="play-btn" onclick="alert('Turnuva Kaydı Başarılı!')">Kayıt Ol</button>
        </div>

        <!-- Masalar -->
        <h3 class="section-title"><i class="fas fa-fire" style="color:orange;"></i> Popüler Masalar</h3>
        <div class="games-grid">
            <!-- Kart 1 -->
            <div class="game-card">
                <div class="live-badge">CANLI</div>
                <div class="card-img" style="background-image: url('https://images.unsplash.com/photo-1605806616949-1e87b487bc2a?w=400&q=80');"></div>
                <h4>İstanbul Elite</h4>
                <div style="font-size:0.8rem; color:#aaa; margin-top:5px;">Giriş: 500 Çip</div>
                <div style="margin-top:10px; display:flex; justify-content:space-between; align-items:center;">
                    <span style="font-size:0.8rem;"><i class="fas fa-user"></i> 3/4</span>
                    <button style="background:var(--neon-blue); border:none; padding:5px 15px; border-radius:4px; cursor:pointer;">Katıl</button>
                </div>
            </div>

            <!-- Kart 2 -->
            <div class="game-card">
                <div class="card-img" style="background-image: url('https://images.unsplash.com/photo-1596838132731-3301c3fd4317?w=400&q=80');"></div>
                <h4>Hızlı Pişti 1v1</h4>
                <div style="font-size:0.8rem; color:#aaa; margin-top:5px;">Giriş: 100 Çip</div>
                <div style="margin-top:10px; display:flex; justify-content:space-between; align-items:center;">
                    <span style="font-size:0.8rem;"><i class="fas fa-user"></i> 1/2</span>
                    <button style="background:var(--neon-purple); color:#fff; border:none; padding:5px 15px; border-radius:4px; cursor:pointer;">Katıl</button>
                </div>
            </div>

            <!-- Kart 3 -->
            <div class="game-card">
                <div class="card-img" style="background-image: url('https://images.unsplash.com/photo-1541562232579-512a21360020?w=400&q=80');"></div>
                <h4>Efsaneler Ligi</h4>
                <div style="font-size:0.8rem; color:#aaa; margin-top:5px;">Giriş: 10K Çip</div>
                <div style="margin-top:10px; display:flex; justify-content:space-between; align-items:center;">
                    <span style="font-size:0.8rem;"><i class="fas fa-lock"></i> VIP</span>
                    <button style="background:#444; color:#aaa; border:none; padding:5px 15px; border-radius:4px; cursor:not-allowed;">Kilitli</button>
                </div>
            </div>
        </div>
    </main>

    <!-- 3. SAĞ CHAT PANELİ -->
    <aside class="right-panel">
        <div class="panel-header">GLOBAL CHAT <span style="font-size:0.7rem; color:green;">● 1,204 Online</span></div>
        
        <div class="chat-box" id="chatContainer">
            <div class="chat-msg"><span class="chat-user">Shadow_99:</span> <span class="chat-text">İstanbul masasına gelecek var mı?</span></div>
            <div class="chat-msg"><span class="chat-user">ProGamer:</span> <span class="chat-text">Turnuva ne zaman başlıyor?</span></div>
            <div class="chat-msg"><span class="chat-user">Admin:</span> <span class="chat-text">Hile yapan banlanır! 🚫</span></div>
        </div>

        <div class="chat-input">
            <input type="text" id="msgInput" placeholder="Mesaj yaz...">
            <button onclick="sendMsg()" style="background:var(--neon-blue); border:none; border-radius:6px; width:40px; cursor:pointer;"><i class="fas fa-paper-plane"></i></button>
        </div>

        <div style="margin-top: 2rem;">
            <div class="panel-header">ARKADAŞLAR</div>
            <div style="display:flex; align-items:center; gap:10px; margin-bottom:10px;">
                <div style="width:30px; height:30px; background:#555; border-radius:50%;"></div>
                <div style="font-size:0.9rem;">Ayşe Y. <span style="font-size:0.7rem; color:gray;">(Oyunda)</span></div>
            </div>
            <div style="display:flex; align-items:center; gap:10px;">
                <div style="width:30px; height:30px; background:#555; border-radius:50%;"></div>
                <div style="font-size:0.9rem;">Mehmet K. <span style="font-size:0.7rem; color:gray;">(Çevrimdışı)</span></div>
            </div>
        </div>
    </aside>

</div>

<!-- SÜRPRİZ & FONKSİYONLAR JS -->
<script>
    // 1. CHAT FONKSİYONU
    function sendMsg() {
        const input = document.getElementById('msgInput');
        const container = document.getElementById('chatContainer');
        if(input.value.trim() !== "") {
            const newMsg = document.createElement('div');
            newMsg.className = 'chat-msg';
            newMsg.innerHTML = `<span class="chat-user" style="color:var(--neon-green)">Ben:</span> <span class="chat-text">${input.value}</span>`;
            container.appendChild(newMsg);
            input.value = '';
            container.scrollTop = container.scrollHeight; // Auto scroll
        }
    }

    // Enter tuşu ile mesaj atma
    document.getElementById('msgInput').addEventListener('keypress', function (e) {
        if (e.key === 'Enter') sendMsg();
    });

    // 2. SECRET EASTER EGG (GİZLİ PARTİ MODU)
    // Logoya 5 saniye içinde 5 kez tıklanırsa çalışır
    let clickCount = 0;
    const logo = document.getElementById('secretLogo');
    
    logo.addEventListener('click', () => {
        clickCount++;
        if (clickCount === 5) {
            document.body.classList.add('party-mode');
            alert('🎉 GİZLİ PARTİ MODU AÇILDI! MÜZİK BAŞLASIN! 🎶');
            // Buraya isterseniz bir ses dosyası da ekleyebilirsiniz.
            clickCount = 0;
        }
        // 2 saniye içinde tekrar tıklanmazsa sayacı sıfırla
        setTimeout(() => { clickCount = 0; }, 2000);
    });

    // Sayfa açılışında animasyon
    console.log("Nexus System Loaded... Welcome Player 1.");
</script>

</body>
</html>
```

### Eklenen Yeni Özellikler ve Sırlar:

1.  **Gizli "Party Mode" (Easter Egg):**
    *   Sol üstteki **"NEXUS" logosuna hızlıca 5 kez tıklayın**.
    *   Arka plan disko ışıkları gibi yanıp sönmeye başlayacak ve bir uyarı mesajı çıkacaktır.
2.  **Global Chat Sistemi:**
    *   Sağ panelde gerçekten çalışıyormuş hissi veren bir sohbet kutusu var. Mesaj yazıp "Enter"a veya gönder butonuna basarsanız mesajınız listeye eklenir.
3.  **Neon & Glassmorphism Tasarım:**
    *   `backdrop-filter: blur(20px)` kullanılarak paneller buzlu cam gibi gösterildi.
    *   Kenarlarda ince beyaz parlamalar ve neon gölgeler (`box-shadow`) kullanıldı.
4.  **Günlük Ödül Sistemi:**
    *   Sol menünün en altına "Günlük Ödül" kutusu eklendi.
5.  **Akıllı Banner:**
    *   Sayfa ortasında devasa, görselli bir turnuva duyurusu var.

Bu kod ile bir web sitesinden çok, modern bir **masaüstü oyun uygulaması** gibi hissettiren bir tasarıma sahip oldunuz.

### GPT-5.1
*2025-12-09 10:41:33 +03*

Aşağıya, **çok daha modern, göz alıcı ve “ultra profesyonel”** bir *oyun salonu ana sayfası* tasarımı koyuyorum.  
Bu sürüm, önceki örneğe göre:

- Daha “AAA oyun sitesi” havasında
- Arka planda gradient + ışık efektleri
- Kart tabanlı salon listesi
- Sağda profil / görevler / bildirimler
- Alt tarafta kayan “canlı bildirim” barı
- Küçük “sürpriz” (sözde gizli) özellikler: günlük ödül butonu, karanlık cam efektler, ufak animasyonlar

Tamamı **tek HTML dosyası** içinde; sadece HTML + CSS, JS ise çok hafif ve isteğe bağlı.

---

## Ultra Modern Oyun Salonu Ana Sayfası (HTML)

```html
<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8" />
    <title>Nova Pişti Arena – Oyun Salonu</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />

    <!-- Modern fontlar -->
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700&display=swap" rel="stylesheet" />
    <!-- İkon seti -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css" />

    <style>
        :root {
            --bg-body: #050613;
            --bg-panel: rgba(13, 16, 40, 0.85);
            --bg-panel-strong: #151730;
            --primary: #9b5cff;     /* neon mor */
            --primary-soft: #b98aff;
            --accent: #00f5d4;      /* neon turkuaz */
            --accent-soft: #5af2d5;
            --danger: #ff4d6d;
            --gold: #facc15;
            --text-main: #f6f7ff;
            --text-muted: #8f9bb3;
            --border-subtle: rgba(255, 255, 255, 0.07);
            --radius-lg: 20px;
            --radius-md: 14px;
            --blur-bg: blur(18px);
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: "Outfit", system-ui, -apple-system, BlinkMacSystemFont, sans-serif;
            background: radial-gradient(circle at top, #181b3a 0, #050613 50%, #02020a 100%);
            color: var(--text-main);
            min-height: 100vh;
            overflow-x: hidden;
        }

        a {
            color: inherit;
            text-decoration: none;
        }

        /* -------- Arka plan dekoratif efektler -------- */
        .bg-orb {
            position: fixed;
            width: 420px;
            height: 420px;
            border-radius: 50%;
            filter: blur(55px);
            opacity: 0.35;
            z-index: -2;
            pointer-events: none;
        }

        .bg-orb.orb-1 {
            background: #9b5cff;
            top: -120px;
            left: -80px;
        }

        .bg-orb.orb-2 {
            background: #00f5d4;
            bottom: -160px;
            right: -40px;
        }

        .noise-layer {
            position: fixed;
            inset: 0;
            pointer-events: none;
            opacity: 0.08;
            z-index: -1;
            background-image: url("https://grainy-gradients.vercel.app/noise.svg");
            mix-blend-mode: soft-light;
        }

        /* -------- NAVBAR -------- */
        .nav {
            position: sticky;
            top: 0;
            z-index: 50;
            backdrop-filter: var(--blur-bg);
            background: linear-gradient(90deg, rgba(5, 6, 19, 0.88), rgba(14, 16, 37, 0.92));
            border-bottom: 1px solid var(--border-subtle);
            padding: 0.9rem 5vw;
            display: flex;
            align-items: center;
            justify-content: space-between;
        }

        .nav-left {
            display: flex;
            align-items: center;
            gap: 12px;
        }

        .brand-logo {
            width: 36px;
            height: 36px;
            border-radius: 14px;
            background: conic-gradient(from 160deg, #9b5cff, #00f5d4, #ff4d6d, #9b5cff);
            display: flex;
            align-items: center;
            justify-content: center;
            color: #050613;
            font-size: 1.1rem;
            font-weight: 700;
            box-shadow: 0 0 25px rgba(155, 92, 255, 0.8);
        }

        .brand-text {
            display: flex;
            flex-direction: column;
        }

        .brand-text span:first-child {
            letter-spacing: 0.16em;
            text-transform: uppercase;
            font-size: 0.65rem;
            color: var(--accent-soft);
        }

        .brand-text strong {
            font-weight: 600;
            font-size: 1.1rem;
        }

        .nav-links {
            display: flex;
            gap: 20px;
            font-size: 0.9rem;
            color: var(--text-muted);
        }

        .nav-links a {
            position: relative;
            padding-bottom: 0.2rem;
        }

        .nav-links a::after {
            content: "";
            position: absolute;
            left: 0;
            bottom: 0;
            height: 2px;
            width: 0;
            background: linear-gradient(90deg, var(--accent), var(--primary));
            transition: width 0.25s ease;
        }

        .nav-links a:hover::after {
            width: 100%;
        }

        .nav-right {
            display: flex;
            align-items: center;
            gap: 16px;
            font-size: 0.9rem;
        }

        .pill {
            padding: 0.35rem 0.85rem;
            border-radius: 999px;
            border: 1px solid var(--border-subtle);
            background: rgba(15, 17, 40, 0.85);
            display: inline-flex;
            align-items: center;
            gap: 6px;
        }

        .pill i {
            color: var(--accent-soft);
        }

        .avatar {
            width: 38px;
            height: 38px;
            border-radius: 999px;
            background: linear-gradient(145deg, #3a3f79, #141632);
            border: 1px solid rgba(255, 255, 255, 0.14);
            display: inline-flex;
            align-items: center;
            justify-content: center;
            font-size: 0.95rem;
            position: relative;
            cursor: pointer;
        }

        .avatar::after {
            content: "";
            position: absolute;
            bottom: -2px;
            right: -2px;
            width: 11px;
            height: 11px;
            border-radius: 50%;
            background: #19e68c;
            border: 2px solid #050613;
        }

        /* -------- HERO / ÜST PANEL -------- */
        .hero-wrapper {
            padding: 1.5rem 5vw 0;
        }

        .hero {
            border-radius: var(--radius-lg);
            padding: 1.8rem 1.8rem 1.6rem;
            background: radial-gradient(circle at top left, rgba(155, 92, 255, 0.32), transparent 60%),
                        radial-gradient(circle at top right, rgba(0, 245, 212, 0.26), transparent 55%),
                        rgba(10, 12, 30, 0.97);
            border: 1px solid rgba(255, 255, 255, 0.09);
            display: grid;
            grid-template-columns: 2.3fr 1.7fr;
            gap: 1.5rem;
            position: relative;
            overflow: hidden;
        }

        .hero::after {
            content: "";
            position: absolute;
            inset: 0;
            background: linear-gradient(120deg, rgba(255, 255, 255, 0.06), transparent 40%, transparent 60%, rgba(255, 255, 255, 0.04));
            mix-blend-mode: soft-light;
            opacity: 0.5;
            pointer-events: none;
        }

        .hero-left {
            position: relative;
            z-index: 1;
        }

        .hero-label {
            display: inline-flex;
            align-items: center;
            gap: 6px;
            padding: 0.25rem 0.7rem;
            border-radius: 999px;
            font-size: 0.72rem;
            letter-spacing: 0.08em;
            text-transform: uppercase;
            background: rgba(7, 255, 193, 0.1);
            color: var(--accent-soft);
            margin-bottom: 0.8rem;
        }

        .hero-label i {
            color: var(--gold);
        }

        .hero-title {
            font-size: 2.4rem;
            font-weight: 600;
            line-height: 1.1;
            margin-bottom: 0.6rem;
        }

        .hero-title span {
            background: linear-gradient(110deg, var(--accent), var(--primary-soft));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        .hero-sub {
            font-size: 0.98rem;
            color: var(--text-muted);
            max-width: 420px;
            margin-bottom: 1.3rem;
        }

        .hero-cta {
            display: flex;
            flex-wrap: wrap;
            gap: 0.8rem;
            align-items: center;
        }

        .btn-primary {
            border: none;
            border-radius: 999px;
            padding: 0.7rem 1.7rem;
            font-size: 0.95rem;
            font-weight: 500;
            letter-spacing: 0.03em;
            text-transform: uppercase;
            background: linear-gradient(120deg, var(--primary), var(--accent));
            color: #050613;
            cursor: pointer;
            box-shadow: 0 12px 30px rgba(72, 33, 140, 0.6);
            display: inline-flex;
            align-items: center;
            gap: 8px;
            transition: transform 0.18s ease, box-shadow 0.18s ease;
        }

        .btn-primary:hover {
            transform: translateY(-2px);
            box-shadow: 0 18px 36px rgba(75, 34, 143, 0.75);
        }

        .btn-ghost {
            border-radius: 999px;
            padding: 0.65rem 1.2rem;
            border: 1px dashed rgba(255, 255, 255, 0.25);
            background: rgba(8, 10, 28, 0.8);
            font-size: 0.85rem;
            color: var(--text-muted);
            cursor: pointer;
            display: inline-flex;
            align-items: center;
            gap: 7px;
        }

        .hero-stats {
            display: flex;
            flex-wrap: wrap;
            gap: 1.2rem;
            margin-top: 1.3rem;
            font-size: 0.86rem;
        }

        .hero-stat {
            display: flex;
            flex-direction: column;
            gap: 2px;
            color: var(--text-muted);
        }

        .hero-stat strong {
            font-size: 1.1rem;
            color: var(--text-main);
        }

        .hero-right {
            position: relative;
            z-index: 1;
            display: grid;
            grid-template-columns: 1.4fr 1.2fr;
            gap: 1rem;
            align-items: stretch;
        }

        .glass-card {
            background: radial-gradient(circle at top, rgba(180, 168, 255, 0.2), transparent 55%),
                        rgba(9, 10, 30, 0.92);
            border-radius: var(--radius-md);
            border: 1px solid rgba(255, 255, 255, 0.12);
            padding: 1rem;
            backdrop-filter: var(--blur-bg);
            position: relative;
            overflow: hidden;
        }

        .glass-card::after {
            content: "";
            position: absolute;
            right: -30%;
            top: -40%;
            width: 70%;
            height: 160%;
            background: radial-gradient(circle at left, rgba(0, 245, 212, 0.25), transparent 60%);
            opacity: 0.7;
            pointer-events: none;
        }

        .glass-header {
            font-size: 0.8rem;
            text-transform: uppercase;
            letter-spacing: 0.09em;
            color: var(--text-muted);
            margin-bottom: 0.7rem;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .table-tag {
            padding: 0.16rem 0.6rem;
            border-radius: 999px;
            font-size: 0.7rem;
            background: rgba(0, 245, 212, 0.12);
            color: var(--accent-soft);
        }

        .table-main {
            display: flex;
            flex-direction: column;
            gap: 0.6rem;
        }

        .table-name {
            font-size: 1.05rem;
            font-weight: 500;
        }

        .table-meta {
            font-size: 0.8rem;
            color: var(--text-muted);
            display: flex;
            justify-content: space-between;
        }

        .chip {
            display: inline-flex;
            align-items: center;
            gap: 4px;
            padding: 0.2rem 0.6rem;
            border-radius: 999px;
            font-size: 0.75rem;
            background: rgba(92, 225, 230, 0.1);
            color: var(--accent-soft);
        }

        .chip i {
            font-size: 0.75rem;
        }

        .mini-avatars {
            display: flex;
            align-items: center;
        }

        .mini-avatar {
            width: 22px;
            height: 22px;
            border-radius: 50%;
            border: 1px solid #050613;
            background: #2a2d54;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            font-size: 0.7rem;
            margin-left: -7px;
        }

        .mini-avatar:first-child {
            margin-left: 0;
        }

        .spot-indicator {
            font-size: 0.78rem;
            color: var(--accent-soft);
        }

        .glass-small {
            background: radial-gradient(circle at top, rgba(0, 245, 212, 0.25), transparent 62%),
                        rgba(6, 9, 26, 0.96);
            border-radius: var(--radius-md);
            border: 1px solid rgba(90, 242, 213, 0.45);
            padding: 0.85rem 0.9rem;
            font-size: 0.78rem;
            display: flex;
            flex-direction: column;
            gap: 0.4rem;
            backdrop-filter: var(--blur-bg);
        }

        .reward-row {
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .reward-amount {
            font-size: 1rem;
            color: var(--gold);
        }

        .btn-claim {
            border-radius: 999px;
            border: none;
            padding: 0.35rem 0.9rem;
            font-size: 0.75rem;
            cursor: pointer;
            background: linear-gradient(120deg, #facc15, #f97316);
            color: #050613;
            font-weight: 600;
        }

        /* -------- ANA GRID (SALONLAR + SAĞ PANEL) -------- */
        .layout {
            padding: 1.6rem 5vw 2.2rem;
            display: grid;
            grid-template-columns: 3fr 1.2fr;
            gap: 1.6rem;
            max-width: 1440px;
            margin: 0 auto;
        }

        .section-title {
            font-size: 0.95rem;
            letter-spacing: 0.12em;
            text-transform: uppercase;
            color: var(--text-muted);
            margin-bottom: 0.9rem;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .section-title span {
            font-size: 0.78rem;
            color: var(--accent-soft);
        }

        .rooms-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(240px, 1fr));
            gap: 1.1rem;
        }

        .room-card {
            background: var(--bg-panel);
            border-radius: var(--radius-md);
            padding: 1rem;
            border: 1px solid var(--border-subtle);
            display: flex;
            flex-direction: column;
            gap: 0.8rem;
            position: relative;
            overflow: hidden;
            transition: transform 0.16s ease, box-shadow 0.16s ease, border-color 0.16s ease;
        }

        .room-card::before {
            content: "";
            position: absolute;
            inset: 0;
            background: linear-gradient(135deg, rgba(155, 92, 255, 0.2), rgba(0, 245, 212, 0.03));
            opacity: 0;
            transition: opacity 0.25s ease;
        }

        .room-card:hover::before {
            opacity: 1;
        }

        .room-card:hover {
            transform: translateY(-3px);
            border-color: rgba(155, 92, 255, 0.7);
            box-shadow: 0 10px 28px rgba(0, 0, 0, 0.65);
        }

        .room-top {
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .room-name {
            font-size: 1rem;
            font-weight: 500;
        }

        .room-badge {
            font-size: 0.7rem;
            border-radius: 999px;
            padding: 0.15rem 0.55rem;
            border: 1px solid rgba(255, 255, 255, 0.12);
            background: rgba(5, 6, 19, 0.9);
        }

        .room-middle {
            display: flex;
            justify-content: space-between;
            font-size: 0.78rem;
            color: var(--text-muted);
        }

        .room-middle strong {
            color: var(--text-main);
            font-size: 0.86rem;
        }

        .room-footer {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-top: 0.4rem;
        }

        .latency {
            font-size: 0.74rem;
            display: inline-flex;
            align-items: center;
            gap: 4px;
            color: var(--accent-soft);
        }

        .latency-dot {
            width: 8px;
            height: 8px;
            border-radius: 50%;
            background: #22c55e;
        }

        .btn-join {
            border-radius: 999px;
            border: none;
            padding: 0.45rem 1.2rem;
            font-size: 0.8rem;
            cursor: pointer;
            background: linear-gradient(120deg, var(--accent), var(--primary));
            color: #050613;
            font-weight: 500;
        }

        /* ----- sağ panel ----- */
        .side-panel {
            display: flex;
            flex-direction: column;
            gap: 1rem;
        }

        .panel {
            background: var(--bg-panel-strong);
            border-radius: var(--radius-md);
            border: 1px solid var(--border-subtle);
            padding: 1rem 1rem 0.9rem;
        }

        .panel-header {
            font-size: 0.85rem;
            letter-spacing: 0.12em;
            text-transform: uppercase;
            color: var(--text-muted);
            margin-bottom: 0.7rem;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .panel-header i {
            color: var(--accent-soft);
        }

        .profile-row {
            display: flex;
            align-items: center;
            gap: 0.75rem;
            margin-bottom: 0.7rem;
        }

        .profile-info {
            display: flex;
            flex-direction: column;
            gap: 2px;
        }

        .profile-info strong {
            font-size: 0.95rem;
        }

        .profile-info span {
            font-size: 0.8rem;
            color: var(--text-muted);
        }

        .profile-progress {
            width: 100%;
            height: 6px;
            border-radius: 999px;
            background: #202341;
            overflow: hidden;
            margin-top: 0.3rem;
        }

        .profile-progress-fill {
            height: 100%;
            width: 52%;
            background: linear-gradient(90deg, var(--accent), var(--primary));
        }

        .stats-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 0.4rem;
            font-size: 0.75rem;
            margin-top: 0.7rem;
        }

        .stat-box {
            background: #111325;
            border-radius: 10px;
            padding: 0.35rem 0.45rem;
            text-align: center;
        }

        .stat-box strong {
            display: block;
            font-size: 0.9rem;
        }

        .quests-list {
            list-style: none;
            display: flex;
            flex-direction: column;
            gap: 0.45rem;
            font-size: 0.8rem;
        }

        .quests-list li {
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .quest-label {
            display: inline-flex;
            align-items: center;
            gap: 6px;
            color: var(--text-muted);
        }

        .quest-label i {
            font-size: 0.8rem;
            color: var(--accent-soft);
        }

        .quest-reward {
            color: var(--gold);
            font-size: 0.78rem;
        }

        .notif-list {
            list-style: none;
            display: flex;
            flex-direction: column;
            gap: 0.45rem;
            font-size: 0.78rem;
            color: var(--text-muted);
        }

        .notif-tag {
            font-size: 0.7rem;
            text-transform: uppercase;
            letter-spacing: 0.08em;
            color: var(--accent-soft);
        }

        /* ----- alt canlı bar ----- */
        .live-bar {
            position: fixed;
            left: 50%;
            transform: translateX(-50%);
            bottom: 14px;
            min-width: 280px;
            max-width: 540px;
            background: rgba(7, 9, 28, 0.95);
            border-radius: 999px;
            border: 1px solid rgba(148, 163, 255, 0.45);
            box-shadow: 0 18px 40px rgba(0, 0, 0, 0.85);
            padding: 0.45rem 0.9rem;
            display: flex;
            align-items: center;
            gap: 8px;
            font-size: 0.78rem;
            backdrop-filter: var(--blur-bg);
        }

        .live-dot {
            width: 8px;
            height: 8px;
            border-radius: 50%;
            background: #ef4444;
            box-shadow: 0 0 12px rgba(239, 68, 68, 0.9);
        }

        .live-text strong {
            color: var(--accent-soft);
        }

        .live-close {
            margin-left: auto;
            cursor: pointer;
            opacity: 0.6;
        }

        .live-close:hover {
            opacity: 1;
        }

        /* -------- RESPONSIVE -------- */
        @media (max-width: 1024px) {
            .hero {
                grid-template-columns: 1fr;
            }
            .hero-right {
                order: -1;
            }
            .layout {
                grid-template-columns: 1fr;
            }
        }

        @media (max-width: 768px) {
            .nav {
                padding-inline: 4vw;
            }
            .hero-wrapper {
                padding-inline: 4vw;
            }
            .layout {
                padding-inline: 4vw;
            }
            .nav-links {
                display: none;
            }
            .hero-title {
                font-size: 2rem;
            }
        }
    </style>
</head>
<body>
    <!-- Dekoratif arka plan -->
    <div class="bg-orb orb-1"></div>
    <div class="bg-orb orb-2"></div>
    <div class="noise-layer"></div>

    <!-- NAVBAR -->
    <nav class="nav">
        <div class="nav-left">
            <div class="brand-logo">
                <i class="fa-solid fa-spade"></i>
            </div>
            <div class="brand-text">
                <span>Nova Arena</span>
                <strong>Pişti Online</strong>
            </div>
        </div>

        <div class="nav-links">
            <a href="#">Salonlar</a>
            <a href="#">Turnuvalar</a>
            <a href="#">Mağaza</a>
            <a href="#">Destek</a>
        </div>

        <div class="nav-right">
            <div class="pill">
                <i class="fa-solid fa-coins"></i>
                <span>3.420 Jeton</span>
            </div>
            <div class="pill">
                <i class="fa-solid fa-signal"></i>
                <span>24.381 çevrimiçi</span>
            </div>
            <div class="avatar">
                <i class="fa-solid fa-user"></i>
            </div>
        </div>
    </nav>

    <!-- HERO / ÜST PANEL -->
    <section class="hero-wrapper">
        <div class="hero">
            <!-- Sol -->
            <div class="hero-left">
                <div class="hero-label">
                    <i class="fa-solid fa-bolt"></i>
                    CANLI PİŞTİ SALONU
                </div>
                <h1 class="hero-title">
                    Masaya <span>şimdi</span> otur,  
                    efsanelerle kapış.
                </h1>
                <p class="hero-sub">
                    Anlık eşleştirme, ultra hızlı sunucular ve zengin animasyonlarla 
                    Türkiye’nin en akıcı pişti deneyimi. Tek tıkla hızlı maça gir, 
                    dereceli odalarda rütbe atla.
                </p>

                <div class="hero-cta">
                    <button class="btn-primary">
                        <i class="fa-solid fa-play"></i>
                        Hızlı Oyun
                    </button>
                    <button class="btn-ghost">
                        <i class="fa-solid fa-chess-board"></i>
                        Tüm Salonları Gör
                    </button>
                </div>

                <div class="hero-stats">
                    <div class="hero-stat">
                        <strong>128</strong>
                        Aktif masa
                    </div>
                    <div class="hero-stat">
                        <strong>4.2M</strong>
                        Dağıtılan el
                    </div>
                    <div class="hero-stat">
                        <strong>Legend III</strong>
                        Mevcut lig
                    </div>
                </div>
            </div>

            <!-- Sağ: Canlı masa + günlük ödül kartı -->
            <div class="hero-right">
                <div class="glass-card">
                    <div class="glass-header">
                        CANLI MASA
                        <span class="table-tag">İstanbul VIP</span>
                    </div>
                    <div class="table-main">
                        <div class="table-name">“Boğaz Gecesi” Masası</div>
                        <div class="table-meta">
                            <span class="chip">
                                <i class="fa-solid fa-coins"></i>
                                1.000 Giriş
                            </span>
                            <span class="spot-indicator">2/4 oyuncu</span>
                        </div>
                        <div class="table-meta" style="margin-top:0.5rem;">
                            <span>Tempo: <strong>Hızlı</strong></span>
                            <span>Ödül x<strong>3</strong></span>
                        </div>
                        <div class="table-meta" style="margin-top:0.5rem;">
                            <div class="mini-avatars">
                                <div class="mini-avatar">AK</div>
                                <div class="mini-avatar">MZ</div>
                                <div class="mini-avatar">EL</div>
                            </div>
                            <span style="font-size:0.78rem;color:var(--text-muted);">
                                Kazanma oranı: <strong style="color:var(--accent-soft);">64%</strong>
                            </span>
                        </div>
                    </div>
                </div>

                <div class="glass-small">
                    <div class="reward-row">
                        <div>
                            <div style="font-size:0.8rem;color:var(--text-muted);">
                                Günlük giriş ödülün
                            </div>
                            <div class="reward-amount">
                                <i class="fa-solid fa-gift"></i> +250 Jeton
                            </div>
                        </div>
                        <button class="btn-claim" id="claimDailyBtn">
                            Al
                        </button>
                    </div>
                    <div style="font-size:0.75rem;color:var(--text-muted);">
                        İpucu: Üst üste 7 gün giriş yap, gizli “Nova” kart temasını aç.
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- ANA GRID: Salonlar + Sağ Panel -->
    <main class="layout">
        <!-- Sol: Salon listesi -->
        <section>
            <div class="section-title">
                AKTİF SALONLAR
                <span>Filtre: Tümü • Hızlı • VIP • Turnuva</span>
            </div>

            <div class="rooms-grid">
                <!-- Oda 1 -->
                <article class="room-card">
                    <div class="room-top">
                        <div class="room-name">Acemi Dostu</div>
                        <div class="room-badge">
                            <i class="fa-solid fa-seedling"></i> Eğitim
                        </div>
                    </div>
                    <div class="room-middle">
                        <div>
                            Giriş: <strong>Bedava</strong><br />
                            Oyuncu: <strong>56 / 120</strong>
                        </div>
                        <div>
                            Mod: <strong>Rahat</strong><br />
                            El süresi: <strong>20 sn</strong>
                        </div>
                    </div>
                    <div class="room-footer">
                        <div class="latency">
                            <span class="latency-dot"></span> 18 ms
                        </div>
                        <button class="btn-join">Katıl</button>
                    </div>
                </article>

                <!-- Oda 2 -->
                <article class="room-card">
                    <div class="room-top">
                        <div class="room-name">İstanbul Salonu</div>
                        <div class="room-badge">
                            <i class="fa-solid fa-bolt"></i> Hızlı
                        </div>
                    </div>
                    <div class="room-middle">
                        <div>
                            Giriş: <strong>250 Jeton</strong><br />
                            Oyuncu: <strong>102 / 140</strong>
                        </div>
                        <div>
                            Mod: <strong>Rekabetçi</strong><br />
                            El süresi: <strong>12 sn</strong>
                        </div>
                    </div>
                    <div class="room-footer">
                        <div class="latency">
                            <span class="latency-dot"></span> 24 ms
                        </div>
                        <button class="btn-join">Katıl</button>
                    </div>
                </article>

                <!-- Oda 3 -->
                <article class="room-card">
                    <div class="room-top">
                        <div class="room-name">Gece VIP Lounge</div>
                        <div class="room-badge">
                            <i class="fa-solid fa-crown"></i> VIP
                        </div>
                    </div>
                    <div class="room-middle">
                        <div>
                            Giriş: <strong>2.000 Jeton</strong><br />
                            Oyuncu: <strong>18 / 40</strong>
                        </div>
                        <div>
                            Mod: <strong>Yüksek Risk</strong><br />
                            Bonus: <strong>x2.5</strong>
                        </div>
                    </div>
                    <div class="room-footer">
                        <div class="latency">
                            <span class="latency-dot"></span> 32 ms
                        </div>
                        <button class="btn-join">Katıl</button>
                    </div>
                </article>

                <!-- Oda 4 -->
                <article class="room-card">
                    <div class="room-top">
                        <div class="room-name">Haftalık Turnuva</div>
                        <div class="room-badge">
                            <i class="fa-solid fa-trophy"></i> Ödüllü
                        </div>
                    </div>
                    <div class="room-middle">
                        <div>
                            Giriş: <strong>500 Jeton</strong><br />
                            Kayıtlı: <strong>230 Oyuncu</strong>
                        </div>
                        <div>
                            Ödül Havuzu:<br />
                            <strong>150.000 Jeton</strong>
                        </div>
                    </div>
                    <div class="room-footer">
                        <div class="latency">
                            <span class="latency-dot"></span> 29 ms
                        </div>
                        <button class="btn-join">Kayıt Ol</button>
                    </div>
                </article>

                <!-- Oda 5 -->
                <article class="room-card">
                    <div class="room-top">
                        <div class="room-name">Arkadaş Masası</div>
                        <div class="room-badge">
                            <i class="fa-solid fa-user-group"></i> Özel
                        </div>
                    </div>
                    <div class="room-middle">
                        <div>
                            Şifreli Oda<br />
                            Durum: <strong>Beklemede</strong>
                        </div>
                        <div>
                            Oyuncu: <strong>2 / 4</strong><br />
                            Sesli Sohbet: <strong>Açık</strong>
                        </div>
                    </div>
                    <div class="room-footer">
                        <div class="latency">
                            <span class="latency-dot"></span> 20 ms
                        </div>
                        <button class="btn-join">Katıl</button>
                    </div>
                </article>

            </div>
        </section>

        <!-- Sağ: Profil, görevler, bildirimler -->
        <aside class="side-panel">
            <!-- Profil Paneli -->
            <div class="panel">
                <div class="panel-header">
                    PROFİLİN
                    <i class="fa-solid fa-circle-user"></i>
                </div>
                <div class="profile-row">
                    <div class="avatar">
                        <i class="fa-solid fa-user-ninja"></i>
                    </div>
                    <div class="profile-info">
                        <strong>NovaPlayer</strong>
                        <span>Lig: <strong style="color:var(--accent-soft);">Elmas II</strong></span>
                    </div>
                </div>
                <div class="profile-progress">
                    <div class="profile-progress-fill"></div>
                </div>
                <div style="font-size:0.75rem;color:var(--text-muted);margin-top:0.3rem;">
                    Sonraki lige <strong>1.240</strong> XP kaldı.
                </div>

                <div class="stats-grid">
                    <div class="stat-box">
                        Galibiyet
                        <strong>61%</strong>
                    </div>
                    <div class="stat-box">
                        Maç
                        <strong>312</strong>
                    </div>
                    <div class="stat-box">
                        Serin
                        <strong>7W</strong>
                    </div>
                </div>
            </div>

            <!-- Günlük Görevler -->
            <div class="panel">
                <div class="panel-header">
                    GÜNLÜK GÖREVLER
                    <i class="fa-solid fa-list-check"></i>
                </div>
                <ul class="quests-list">
                    <li>
                        <span class="quest-label">
                            <i class="fa-solid fa-check"></i>
                            3 maç tamamla
                        </span>
                        <span class="quest-reward">+150</span>
                    </li>
                    <li>
                        <span class="quest-label">
                            <i class="fa-solid fa-check"></i>
                            1 pişti yap
                        </span>
                        <span class="quest-reward">+200</span>
                    </li>
                    <li>
                        <span class="quest-label">
                            <i class="fa-solid fa-check"></i>
                            Arkadaş davet et
                        </span>
                        <span class="quest-reward">+350</span>
                    </li>
                </ul>
            </div>

            <!-- Bildirimler -->
            <div class="panel">
                <div class="panel-header">
                    CANLI AKIŞ
                    <i class="fa-solid fa-bell"></i>
                </div>
                <ul class="notif-list">
                    <li>
                        <span class="notif-tag">TURNOVA</span><br />
                        “Haftalık Turnuva” 15 dk içinde başlıyor. Koltuk sayısı sınırlı.
                    </li>
                    <li>
                        <span class="notif-tag">ARKADAŞ</span><br />
                        Mert seni özel “Arkadaş Masası”na davet etti.
                    </li>
                    <li>
                        <span class="notif-tag">ÖDÜL</span><br />
                        Dünkü serin 5 galibiyete ulaştı; ekstra bonusu kasana aktarıldı.
                    </li>
                </ul>
            </div>
        </aside>
    </main>

    <!-- Alt canlı bildirim barı (küçük sürpriz) -->
    <div class="live-bar" id="liveBar">
        <div class="live-dot"></div>
        <div class="live-text">
            <strong>Canlı:</strong> Az önce <strong>ElifY</strong>, “Gece VIP Lounge” masasında  
            32 puanlık müthiş bir pişti yaptı!
        </div>
        <div class="live-close" id="liveClose">
            <i class="fa-solid fa-xmark"></i>
        </div>
    </div>

    <!-- Mini JS: canlı bar kapatma & “günlük ödül” butonu -->
    <script>
        document.getElementById("liveClose")?.addEventListener("click", () => {
            document.getElementById("liveBar").style.display = "none";
        });

        document.getElementById("claimDailyBtn")?.addEventListener("click", function () {
            this.textContent = "Alındı!";
            this.disabled = true;
            this.style.opacity = "0.7";
        });
    </script>
</body>
</html>
```

---

### Neler Ekledik? (Özet)

- **Ultra modern görünüm**  
  - Neon mor + turkuaz gradientler  
  - Cam (glassmorphism) paneller  
  - Arka planda bulanık renkli “orb” ışıklar + noise katmanı  

- **Yeni fonksiyonel bölümler**
  - Hero bölümünde: Hızlı oyun, tüm salonlara git butonları  
  - Sağ üstte: canlı masa kartı + günlük ödül kartı  
  - Ana grid: birden fazla salon kartı (farklı modlar, hızlar, VIP, turnuva, arkadaş odası)  
  - Sağ panelde:
    - Profil seviyesi + XP bar
    - İstatistikler (galibiyet, maç, seri)
    - Günlük görevler
    - Canlı bildirimler

- **Küçük “sırlar” / sürprizler**
  - Günlük ödül butonuna bastığında sadece UI olarak “Alındı!” oluyor (ileride backend’e bağlanabilir).
  - Alt tarafta canlı maçtan gelen “anlık highlight” barı (kapatılabilir).
  - 7 gün üst üste girişte gizli tema açacağına dair ipucu.

---

İstersen:

- Sonraki adımda bu tasarımı **gerçek sistem mimarisine** (ör. kullanıcı oturumu, gerçek oda listesi, API’den veri çekme vs.) uyarlayabiliriz.
- Ya da mobil odaklı **sadece telefon için** sadeleştirilmiş bir versiyon oluşturabiliriz.

Bundan sonraki adım için ne yapalım:  
1) Bu salon tasarımını **oyun masası sayfasına** bağlayalım mı,  
yoksa 2) Bu temayı kullanarak **ikinci bir alt sayfa** (örneğin “Turnuva Sayfası”) tasarlayalım mı?
