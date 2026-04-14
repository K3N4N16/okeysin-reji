from flask import Flask, render_template_string
import webbrowser
import threading
import time

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Aşk-ı Muhabbet v46.0 BLACK | Bursa Stüdyosu 🎙️</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Playfair+Display:wght@700&display=swap');
        
        * { margin: 0; padding: 0; box-sizing: border-box; }
        
        body {
            background: #0a0a0a;
            color: #fff;
            font-family: 'Inter', sans-serif;
            overflow: hidden;
            height: 100vh;
            position: relative;
        }
        
        .studio-bg {
            position: absolute;
            inset: 0;
            background: linear-gradient(135deg, #0f0f0f 0%, #1a0f1f 50%, #0f0a14 100%);
            box-shadow: inset 0 0 120px rgba(139, 0, 0, 0.4);
            z-index: -1;
        }
        
        .live-badge {
            position: absolute;
            top: 30px;
            left: 40px;
            background: #dc143c;
            color: white;
            padding: 10px 28px;
            border-radius: 50px;
            font-size: 15px;
            font-weight: 700;
            letter-spacing: 1.5px;
            z-index: 100;
            box-shadow: 0 0 25px rgba(220, 20, 60, 0.8);
            animation: pulse 2s infinite;
            display: flex;
            align-items: center;
            gap: 8px;
        }
        
        @keyframes pulse {
            0%, 100% { box-shadow: 0 0 25px rgba(220, 20, 60, 0.8); }
            50% { box-shadow: 0 0 40px rgba(220, 20, 60, 1); }
        }
        
        .studio-iframe {
            position: absolute;
            top: 0; left: 0;
            width: 100%;
            height: 100%;
            border: none;
            opacity: 0.96;
            transition: opacity 1.5s ease;
            filter: contrast(1.08) saturate(1.15);
        }
        
        .floating-banner {
            position: fixed;
            bottom: 35px;
            right: 35px;
            background: rgba(15, 15, 20, 0.96);
            backdrop-filter: blur(25px);
            border: 1px solid rgba(255, 255, 255, 0.12);
            border-radius: 24px;
            padding: 18px 28px;
            display: flex;
            align-items: center;
            gap: 18px;
            box-shadow: 0 25px 50px rgba(0, 0, 0, 0.7);
            z-index: 1000;
            transition: all 0.7s cubic-bezier(0.34, 1.56, 0.64, 1);
        }
        
        .banner-content {
            display: flex;
            align-items: center;
            gap: 16px;
        }
        
        .banner-logo {
            font-size: 38px;
            filter: drop-shadow(0 0 12px #c026d3);
            animation: mic-pulse 3s infinite ease-in-out;
        }
        
        @keyframes mic-pulse {
            0%, 100% { transform: scale(1); }
            50% { transform: scale(1.08); }
        }
        
        .banner-text .upper {
            font-size: 18px;
            font-weight: 700;
            letter-spacing: 0.8px;
            color: #f1f1f1;
        }
        
        .banner-text .lower {
            font-size: 13px;
            color: #a1a1aa;
            margin-top: 3px;
        }
        
        .close-btn {
            background: none;
            border: none;
            color: #777;
            font-size: 26px;
            width: 42px;
            height: 42px;
            display: flex;
            align-items: center;
            justify-content: center;
            border-radius: 50%;
            cursor: pointer;
            transition: all 0.4s;
        }
        
        .close-btn:hover {
            background: rgba(255, 60, 60, 0.15);
            color: #ff4d4d;
            transform: rotate(90deg);
        }
        
        .floating-banner:hover {
            transform: translateY(-6px) scale(1.03);
            box-shadow: 0 30px 60px rgba(192, 38, 211, 0.3);
        }
        
        .neon-line {
            position: absolute;
            bottom: 0;
            left: 0;
            width: 100%;
            height: 3px;
            background: linear-gradient(90deg, transparent, #c026d3, #dc143c, transparent);
            box-shadow: 0 0 15px #c026d3;
            animation: neon-flow 8s linear infinite;
        }
        
        @keyframes neon-flow {
            0% { background-position: 0% 50%; }
            100% { background-position: 200% 50%; }
        }
    </style>
</head>
<body>
    <div class="studio-bg"></div>
    
    <div class="live-badge">● CANLI YAYINDA - BURSA STÜDYOSU</div>
    
    <iframe 
        src="https://019d8437-ab33-7da5-ae38-4f6524d037ed.arena.site/?embed=true" 
        class="studio-iframe"
        allowfullscreen>
    </iframe>
    
    <!-- Şık Floating Banner -->
    <div class="floating-banner" id="floating-banner">
        <div class="banner-content">
            <div class="banner-logo">🎙️</div>
            <div class="banner-text">
                <span class="upper">Aşk-ı Muhabbet</span>
                <span class="lower">v46.0 BLACK • Bursa Stüdyosu</span>
            </div>
        </div>
        <button class="close-btn" onclick="dismissBanner()">✕</button>
    </div>
    
    <div class="neon-line"></div>

    <script>
        function dismissBanner() {
            const banner = document.getElementById('floating-banner');
            banner.style.transition = 'all 0.8s cubic-bezier(0.4, 0, 0.2, 1)';
            banner.style.transform = 'translateY(150px) scale(0.9)';
            banner.style.opacity = '0';
            setTimeout(() => banner.style.display = 'none', 800);
        }
        
        // Sayfa açılırken güzel bir giriş
        window.onload = () => {
            document.querySelector('.studio-iframe').style.opacity = '1';
        };
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML)

def open_browser():
    time.sleep(1.5)
    webbrowser.open('http://127.0.0.1:5000')

if __name__ == '__main__':
    print("🎙️ Aşk-ı Muhabbet v46.0 BLACK | Bursa Stüdyosu açılıyor...")
    print("🌹 Daha şık, daha siyah, daha kadife...")
    print("http://127.0.0.1:5000 adresine gidiyor...")
    
    # Otomatik tarayıcı açsın
    threading.Thread(target=open_browser, daemon=True).start()
    
    app.run(host='0.0.0.0', port=5000, debug=False)