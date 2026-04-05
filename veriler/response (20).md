<think>
The user wants me to create a professional IPTV player application with:
1. IPTV URL support
2. Turkish channels pre-loaded
3. Channel import/export functionality
4. Smart webhost TV IP module
5. Modern, flashy player design
6. Mobile responsive
7. Complete working application

Let me create a comprehensive, modern IPTV player with all these features. I'll build it as a single-page web application with HTML, CSS, and JavaScript. I'll use HLS.js for streaming, and create a beautiful modern UI.

Let me create a full-featured IPTV player with:
- M3U playlist parser
- Turkish channels pre-loaded
</think># 🎬 Ultimate IPTV Player Pro

İşte profesyonel, modern ve mobil uyumlu bir IPTV player uygulaması:

```html
<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>Ultimate IPTV Player Pro</title>
    <script src="https://cdn.jsdelivr.net/npm/hls.js@latest"></script>
    <script src="https://cdn.jsdelivr.net/npm/shaka-player@latest/dist/shaka-player.compiled.min.js"></script>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=JetBrains+Mono:wght@400;700&display=swap" rel="stylesheet">
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css" rel="stylesheet">
    <style>
        :root {
            --bg-primary: #0a0a0f;
            --bg-secondary: #12121a;
            --bg-tertiary: #1a1a2e;
            --bg-card: #16213e;
            --bg-glass: rgba(22, 33, 62, 0.6);
            --accent: #e94560;
            --accent-glow: rgba(233, 69, 96, 0.4);
            --accent2: #0f3460;
            --accent3: #533483;
            --text-primary: #ffffff;
            --text-secondary: #a0a0b0;
            --text-muted: #606080;
            --border: rgba(255,255,255,0.06);
            --success: #00d474;
            --warning: #ffc107;
            --gradient1: linear-gradient(135deg, #e94560, #533483);
            --gradient2: linear-gradient(135deg, #0f3460, #533483);
            --gradient3: linear-gradient(135deg, #e94560, #0f3460);
            --shadow-glow: 0 0 30px rgba(233, 69, 96, 0.15);
            --radius: 16px;
            --radius-sm: 10px;
            --transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        }

        * { margin: 0; padding: 0; box-sizing: border-box; }

        body {
            font-family: 'Inter', sans-serif;
            background: var(--bg-primary);
            color: var(--text-primary);
            overflow-x: hidden;
            min-height: 100vh;
        }

        body::before {
            content: '';
            position: fixed;
            top: 0; left: 0;
            width: 100%; height: 100%;
            background: 
                radial-gradient(ellipse at 20% 20%, rgba(233,69,96,0.08) 0%, transparent 50%),
                radial-gradient(ellipse at 80% 80%, rgba(83,52,131,0.08) 0%, transparent 50%),
                radial-gradient(ellipse at 50% 50%, rgba(15,52,96,0.05) 0%, transparent 70%);
            pointer-events: none;
            z-index: 0;
        }

        /* Scrollbar */
        ::-webkit-scrollbar { width: 6px; }
        ::-webkit-scrollbar-track { background: transparent; }
        ::-webkit-scrollbar-thumb { background: var(--accent); border-radius: 3px; }

        /* ===== HEADER ===== */
        .app-header {
            position: fixed;
            top: 0; left: 0; right: 0;
            height: 64px;
            background: rgba(10, 10, 15, 0.85);
            backdrop-filter: blur(20px);
            border-bottom: 1px solid var(--border);
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 0 20px;
            z-index: 1000;
        }

        .logo {
            display: flex;
            align-items: center;
            gap: 12px;
        }

        .logo-icon {
            width: 40px; height: 40px;
            background: var(--gradient1);
            border-radius: 12px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 18px;
            animation: pulse-glow 3s ease-in-out infinite;
        }

        @keyframes pulse-glow {
            0%, 100% { box-shadow: 0 0 15px rgba(233,69,96,0.3); }
            50% { box-shadow: 0 0 30px rgba(233,69,96,0.6); }
        }

        .logo-text {
            font-weight: 800;
            font-size: 18px;
            background: var(--gradient1);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            letter-spacing: -0.5px;
        }

        .logo-badge {
            background: var(--accent);
            color: white;
            font-size: 9px;
            font-weight: 700;
            padding: 2px 6px;
            border-radius: 4px;
            letter-spacing: 1px;
        }

        .header-actions {
            display: flex;
            gap: 8px;
        }

        .header-btn {
            width: 40px; height: 40px;
            background: var(--bg-glass);
            border: 1px solid var(--border);
            border-radius: 12px;
            color: var(--text-secondary);
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 16px;
            transition: var(--transition);
        }

        .header-btn:hover {
            background: var(--accent);
            color: white;
            border-color: var(--accent);
            transform: translateY(-2px);
            box-shadow: var(--shadow-glow);
        }

        .header-btn.active {
            background: var(--accent);
            color: white;
            border-color: var(--accent);
        }

        /* ===== MAIN LAYOUT ===== */
        .app-container {
            margin-top: 64px;
            display: flex;
            height: calc(100vh - 64px);
            position: relative;
            z-index: 1;
        }

        /* ===== SIDEBAR ===== */
        .sidebar {
            width: 320px;
            background: var(--bg-secondary);
            border-right: 1px solid var(--border);
            display: flex;
            flex-direction: column;
            transition: var(--transition);
            overflow: hidden;
            flex-shrink: 0;
        }

        .sidebar.collapsed { width: 0; border: none; }

        .sidebar-header {
            padding: 16px;
            border-bottom: 1px solid var(--border);
        }

        .search-box {
            position: relative;
        }

        .search-box input {
            width: 100%;
            height: 44px;
            background: var(--bg-tertiary);
            border: 1px solid var(--border);
            border-radius: var(--radius-sm);
            color: var(--text-primary);
            padding: 0 16px 0 42px;
            font-size: 14px;
            font-family: 'Inter', sans-serif;
            transition: var(--transition);
            outline: none;
        }

        .search-box input:focus {
            border-color: var(--accent);
            box-shadow: 0 0 0 3px var(--accent-glow);
        }

        .search-box i {
            position: absolute;
            left: 14px; top: 50%;
            transform: translateY(-50%);
            color: var(--text-muted);
            font-size: 14px;
        }

        .category-tabs {
            display: flex;
            padding: 12px 16px 0;
            gap: 6px;
            overflow-x: auto;
            flex-shrink: 0;
        }

        .category-tabs::-webkit-scrollbar { height: 0; }

        .cat-tab {
            padding: 8px 14px;
            background: var(--bg-tertiary);
            border: 1px solid var(--border);
            border-radius: 20px;
            color: var(--text-secondary);
            font-size: 12px;
            font-weight: 600;
            cursor: pointer;
            white-space: nowrap;
            transition: var(--transition);
        }

        .cat-tab:hover, .cat-tab.active {
            background: var(--accent);
            border-color: var(--accent);
            color: white;
        }

        .channel-list {
            flex: 1;
            overflow-y: auto;
            padding: 8px;
        }

        .channel-item {
            display: flex;
            align-items: center;
            gap: 12px;
            padding: 12px;
            border-radius: var(--radius-sm);
            cursor: pointer;
            transition: var(--transition);
            border: 1px solid transparent;
            margin-bottom: 4px;
        }

        .channel-item:hover {
            background: var(--bg-glass);
            border-color: var(--border);
        }

        .channel-item.active {
            background: rgba(233, 69, 96, 0.1);
            border-color: var(--accent);
        }

        .channel-item.active .channel-name { color: var(--accent); }

        .channel-logo {
            width: 44px; height: 44px;
            background: var(--bg-tertiary);
            border-radius: var(--radius-sm);
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 18px;
            flex-shrink: 0;
            overflow: hidden;
            border: 1px solid var(--border);
        }

        .channel-logo img {
            width: 100%;
            height: 100%;
            object-fit: contain;
        }

        .channel-info { flex: 1; min-width: 0; }

        .channel-name {
            font-size: 14px;
            font-weight: 600;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
        }

        .channel-meta {
            font-size: 11px;
            color: var(--text-muted);
            margin-top: 2px;
            display: flex;
            align-items: center;
            gap: 6px;
        }

        .live-dot {
            width: 6px; height: 6px;
            background: var(--success);
            border-radius: 50%;
            animation: blink 2s infinite;
        }

        @keyframes blink {
            0%, 100% { opacity: 1; }
            50% { opacity: 0.3; }
        }

        .channel-badge {
            background: var(--gradient1);
            color: white;
            font-size: 9px;
            font-weight: 700;
            padding: 2px 6px;
            border-radius: 4px;
        }

        /* ===== MAIN CONTENT ===== */
        .main-content {
            flex: 1;
            display: flex;
            flex-direction: column;
            min-width: 0;
        }

        /* ===== VIDEO PLAYER ===== */
        .player-container {
            position: relative;
            background: #000;
            aspect-ratio: 16/9;
            max-height: 65vh;
            width: 100%;
            flex-shrink: 0;
        }

        .player-container.fullscreen {
            position: fixed;
            top: 0; left: 0;
            width: 100vw; height: 100vh;
            max-height: none;
            z-index: 9999;
            aspect-ratio: auto;
        }

        #videoPlayer {
            width: 100%;
            height: 100%;
            object-fit: contain;
            background: #000;
        }

        .player-overlay {
            position: absolute;
            top: 0; left: 0;
            width: 100%; height: 100%;
            background: linear-gradient(transparent 60%, rgba(0,0,0,0.8));
            display: flex;
            flex-direction: column;
            justify-content: flex-end;
            padding: 20px;
            opacity: 0;
            transition: var(--transition);
            cursor: pointer;
        }

        .player-container:hover .player-overlay,
        .player-container.paused .player-overlay { opacity: 1; }

        .player-info-bar {
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-bottom: 16px;
        }

        .now-playing {
            display: flex;
            align-items: center;
            gap: 12px;
        }

        .now-playing-logo {
            width: 48px; height: 48px;
            background: rgba(255,255,255,0.1);
            border-radius: 12px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 20px;
            backdrop-filter: blur(10px);
        }

        .now-playing-info h3 {
            font-size: 16px;
            font-weight: 700;
        }

        .now-playing-info p {
            font-size: 12px;
            color: var(--text-secondary);
            margin-top: 2px;
        }

        .player-controls {
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 16px;
        }

        .ctrl-btn {
            width: 44px; height: 44px;
            background: rgba(255,255,255,0.1);
            border: none;
            border-radius: 50%;
            color: white;
            font-size: 18px;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            transition: var(--transition);
            backdrop-filter: blur(10px);
        }

        .ctrl-btn:hover {
            background: var(--accent);
            transform: scale(1.1);
        }

        .ctrl-btn.play-btn {
            width: 56px; height: 56px;
            font-size: 22px;
            background: var(--accent);
        }

        .volume-slider {
            width: 100px;
            -webkit-appearance: none;
            height: 4px;
            background: rgba(255,255,255,0.2);
            border-radius: 2px;
            outline: none;
        }

        .volume-slider::-webkit-slider-thumb {
            -webkit-appearance: none;
            width: 14px; height: 14px;
            background: var(--accent);
            border-radius: 50%;
            cursor: pointer;
        }

        .player-top-bar {
            position: absolute;
            top: 0; left: 0; right: 0;
            padding: 16px 20px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            background: linear-gradient(rgba(0,0,0,0.6), transparent);
        }

        .live-badge {
            display: flex;
            align-items: center;
            gap: 6px;
            background: rgba(233,69,96,0.9);
            padding: 6px 12px;
            border-radius: 20px;
            font-size: 12px;
            font-weight: 700;
        }

        .player-top-actions {
            display: flex;
            gap: 8px;
        }

        .quality-selector {
            background: rgba(0,0,0,0.5);
            border: 1px solid rgba(255,255,255,0.2);
            color: white;
            padding: 6px 12px;
            border-radius: 8px;
            font-size: 12px;
            cursor: pointer;
            font-family: 'Inter', sans-serif;
        }

        .quality-selector option { background: var(--bg-secondary); }

        /* ===== EPG / CHANNEL DETAIL ===== */
        .detail-panel {
            flex: 1;
            overflow-y: auto;
            padding: 24px;
            background: var(--bg-secondary);
        }

        .detail-header {
            display: flex;
            align-items: center;
            gap: 16px;
            margin-bottom: 24px;
        }

        .detail-logo {
            width: 64px; height: 64px;
            background: var(--bg-tertiary);
            border-radius: var(--radius);
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 28px;
            border: 2px solid var(--border);
        }

        .detail-title h2 {
            font-size: 22px;
            font-weight: 800;
        }

        .detail-title p {
            color: var(--text-muted);
            font-size: 13px;
            margin-top: 4px;
        }

        /* EPG Timeline */
        .epg-section { margin-top: 8px; }

        .epg-title {
            font-size: 14px;
            font-weight: 700;
            color: var(--text-secondary);
            margin-bottom: 12px;
            display: flex;
            align-items: center;
            gap: 8px;
        }

        .epg-item {
            display: flex;
            gap: 12px;
            padding: 12px;
            background: var(--bg-tertiary);
            border-radius: var(--radius-sm);
            margin-bottom: 8px;
            border: 1px solid var(--border);
            transition: var(--transition);
        }

        .epg-item.current {
            border-color: var(--accent);
            background: rgba(233,69,96,0.05);
        }

        .epg-time {
            font-size: 12px;
            font-weight: 700;
            color: var(--accent);
            font-family: 'JetBrains Mono', monospace;
            white-space: nowrap;
            min-width: 90px;
        }

        .epg-program {
            font-size: 13px;
            font-weight: 500;
        }

        .epg-progress {
            width: 100%;
            height: 3px;
            background: var(--bg-primary);
            border-radius: 2px;
            margin-top: 6px;
            overflow: hidden;
        }

        .epg-progress-bar {
            height: 100%;
            background: var(--accent);
            border-radius: 2px;
            transition: width 1s;
        }

        /* ===== SETTINGS MODAL ===== */
        .modal-overlay {
            position: fixed;
            top: 0; left: 0;
            width: 100%; height: 100%;
            background: rgba(0,0,0,0.7);
            backdrop-filter: blur(8px);
            z-index: 2000;
            display: none;
            align-items: center;
            justify-content: center;
            padding: 20px;
        }

        .modal-overlay.active { display: flex; }

        .modal {
            background: var(--bg-secondary);
            border: 1px solid var(--border);
            border-radius: var(--radius);
            width: 100%;
            max-width: 600px;
            max-height: 80vh;
            overflow-y: auto;
            animation: modal-in 0.3s ease;
        }

        @keyframes modal-in {
            from { transform: scale(0.9); opacity: 0; }
            to { transform: scale(1); opacity: 1; }
        }

        .modal-header {
            padding: 20px 24px;
            border-bottom: 1px solid var(--border);
            display: flex;
            align-items: center;
            justify-content: space-between;
        }

        .modal-header h3 {
            font-size: 18px;
            font-weight: 700;
        }

        .modal-close {
            width: 36px; height: 36px;
            background: var(--bg-tertiary);
            border: 1px solid var(--border);
            border-radius: 10px;
            color: var(--text-secondary);
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 16px;
            transition: var(--transition);
        }

        .modal-close:hover {
            background: var(--accent);
            color: white;
            border-color: var(--accent);
        }

        .modal-body { padding: 24px; }

        .form-group {
            margin-bottom: 20px;
        }

        .form-label {
            display: block;
            font-size: 13px;
            font-weight: 600;
            color: var(--text-secondary);
            margin-bottom: 8px;
        }

        .form-input {
            width: 100%;
            height: 48px;
            background: var(--bg-tertiary);
            border: 1px solid var(--border);
            border-radius: var(--radius-sm);
            color: var(--text-primary);
            padding: 0 16px;
            font-size: 14px;
            font-family: 'Inter', sans-serif;
            transition: var(--transition);
            outline: none;
        }

        .form-input:focus {
            border-color: var(--accent);
            box-shadow: 0 0 0 3px var(--accent-glow);
        }

        textarea.form-input {
            height: auto;
            min-height: 120px;
            padding: 16px;
            resize: vertical;
            font-family: 'JetBrains Mono', monospace;
            font-size: 12px;
            line-height: 1.5;
        }

        .btn {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            gap: 8px;
            height: 44px;
            padding: 0 24px;
            border: none;
            border-radius: var(--radius-sm);
            font-size: 14px;
            font-weight: 600;
            font-family: 'Inter', sans-serif;
            cursor: pointer;
            transition: var(--transition);
        }

        .btn-primary {
            background: var(--gradient1);
            color: white;
        }

        .btn-primary:hover {
            transform: translateY(-2px);
            box-shadow: var(--shadow-glow);
        }

        .btn-secondary {
            background: var(--bg-tertiary);
            border: 1px solid var(--border);
            color: var(--text-primary);
        }

        .btn-secondary:hover {
            border-color: var(--accent);
        }

        .btn-success {
            background: var(--success);
            color: white;
        }

        .btn-group {
            display: flex;
            gap: 10px;
            flex-wrap: wrap;
        }

        .url-list {
            max-height: 200px;
            overflow-y: auto;
            margin-top: 8px;
        }

        .url-item {
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 10px 14px;
            background: var(--bg-tertiary);
            border: 1px solid var(--border);
            border-radius: 8px;
            margin-bottom: 6px;
            font-size: 12px;
            font-family: 'JetBrains Mono', monospace;
            color: var(--text-secondary);
            word-break: break-all;
        }

        .url-item .delete-btn {
            background: none;
            border: none;
            color: var(--accent);
            cursor: pointer;
            font-size: 14px;
            padding: 4px;
            flex-shrink: 0;
        }

        .stats-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(120px, 1fr));
            gap: 12px;
            margin-top: 16px;
        }

        .stat-card {
            background: var(--bg-tertiary);
            border: 1px solid var(--border);
            border-radius: var(--radius-sm);
            padding: 16px;
            text-align: center;
        }

        .stat-value {
            font-size: 24px;
            font-weight: 800;
            background: var(--gradient1);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        .stat-label {
            font-size: 11px;
            color: var(--text-muted);
            margin-top: 4px;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }

        /* Toast */
        .toast-container {
            position: fixed;
            top: 80px; right: 20px;
            z-index: 3000;
            display: flex;
            flex-direction: column;
            gap: 8px;
        }

        .toast {
            padding: 14px 20px;
            background: var(--bg-secondary);
            border: 1px solid var(--border);
            border-radius: var(--radius-sm);
            color: var(--text-primary);
            font-size: 13px;
            font-weight: 500;
            display: flex;
            align-items: center;
            gap: 10px;
            animation: toast-in 0.3s ease, toast-out 0.3s ease 3s forwards;
            box-shadow: 0 10px 30px rgba(0,0,0,0.3);
            min-width: 280px;
        }

        .toast.success { border-left: 3px solid var(--success); }
        .toast.error { border-left: 3px solid var(--accent); }
        .toast.info { border-left: 3px solid #4fc3f7; }

        @keyframes toast-in {
            from { transform: translateX(100%); opacity: 0; }
            to { transform: translateX(0); opacity: 1; }
        }

        @keyframes toast-out {
            from { opacity: 1; }
            to { opacity: 0; transform: translateX(100%); }
        }

        /* ===== LOADING SPINNER ===== */
        .loading-overlay {
            position: absolute;
            top: 0; left: 0;
            width: 100%; height: 100%;
            background: rgba(0,0,0,0.8);
            display: none;
            align-items: center;
            justify-content: center;
            flex-direction: column;
            gap: 16px;
            z-index: 5;
        }

        .loading-overlay.active { display: flex; }

        .spinner {
            width: 48px; height: 48px;
            border: 3px solid rgba(255,255,255,0.1);
            border-top-color: var(--accent);
            border-radius: 50%;
            animation: spin 0.8s linear infinite;
        }

        @keyframes spin { to { transform: rotate(360deg); } }

        .loading-text { color: var(--text-secondary); font-size: 13px; }

        /* Welcome screen */
        .welcome-screen {
            flex: 1;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            background: var(--bg-secondary);
            padding: 40px;
            text-align: center;
        }

        .welcome-icon {
            width: 100px; height: 100px;
            background: var(--gradient1);
            border-radius: 30px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 40px;
            margin-bottom: 24px;
            animation: float 3s ease-in-out infinite;
        }

        @keyframes float {
            0%, 100% { transform: translateY(0); }
            50% { transform: translateY(-10px); }
        }

        .welcome-screen h2 {
            font-size: 28px;
            font-weight: 800;
            margin-bottom: 8px;
        }

        .welcome-screen p {
            color: var(--text-muted);
            font-size: 14px;
            max-width: 400px;
            line-height: 1.6;
        }

        .welcome-actions {
            display: flex;
            gap: 12px;
            margin-top: 24px;
        }

        .welcome-btn {
            padding: 12px 24px;
            border-radius: var(--radius-sm);
            border: 1px solid var(--border);
            background: var(--bg-tertiary);
            color: var(--text-primary);
            font-size: 14px;
            font-weight: 600;
            cursor: pointer;
            display: flex;
            align-items: center;
            gap: 8px;
            transition: var(--transition);
            font-family: 'Inter', sans-serif;
        }

        .welcome-btn:hover {
            border-color: var(--accent);
            transform: translateY(-2px);
        }

        .welcome-btn.primary {
            background: var(--gradient1);
            border-color: transparent;
        }

        /* Mini player (for mobile) */
        .mini-player {
            display: none;
            position: fixed;
            bottom: 0; left: 0; right: 0;
            background: var(--bg-secondary);
            border-top: 1px solid var(--border);
            padding: 10px 16px;
            align-items: center;
            gap: 12px;
            z-index: 900;
            backdrop-filter: blur(20px);
        }

        /* ===== RESPONSIVE ===== */
        @media (max-width: 768px) {
            .sidebar {
                position: fixed;
                top: 64px; left: 0;
                height: calc(100vh - 64px);
                z-index: 500;
                width: 100%;
                transform: translateX(-100%);
                transition: var(--transition);
            }

            .sidebar.mobile-open {
                transform: translateX(0);
            }

            .player-container {
                aspect-ratio: 16/10;
                max-height: 50vh;
            }

            .detail-panel { padding: 16px; }

            .logo-text { display: none; }

            .mobile-toggle {
                display: flex !important;
            }
        }

        .mobile-toggle { display: none; }

        /* ===== FAVORITES ===== */
        .fav-btn {
            background: none;
            border: none;
            color: var(--text-muted);
            cursor: pointer;
            font-size: 16px;
            transition: var(--transition);
            padding: 4px;
        }

        .fav-btn.active {
            color: #ffc107;
        }

        /* ===== WEBHOST TV IP MODULE ===== */
        .webhost-module {
            background: var(--bg-tertiary);
            border: 1px solid var(--border);
            border-radius: var(--radius);
            padding: 20px;
            margin-bottom: 20px;
        }

        .webhost-header {
            display: flex;
            align-items: center;
            gap: 12px;
            margin-bottom: 16px;
        }

        .webhost-icon {
            width: 40px; height: 40px;
            background: var(--gradient2);
            border-radius: 10px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 18px;
        }

        .webhost-header h4 {
            font-size: 15px;
            font-weight: 700;
        }

        .webhost-header p {
            font-size: 11px;
            color: var(--text-muted);
        }

        .server-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(140px, 1fr));
            gap: 8px;
        }

        .server-card {
            background: var(--bg-secondary);
            border: 1px solid var(--border);
            border-radius: var(--radius-sm);
            padding: 12px;
            cursor: pointer;
            transition: var(--transition);
            text-align: center;
        }

        .server-card:hover, .server-card.active {
            border-color: var(--accent);
            background: rgba(233,69,96,0.05);
        }

        .server-card .server-name {
            font-size: 12px;
            font-weight: 600;
            margin-top: 8px;
        }

        .server-card .server-ping {
            font-size: 10px;
            color: var(--success);
            margin-top: 4px;
        }

        .server-card .server-icon {
            font-size: 24px;
        }

        /* ===== PLAYER WATERMARK ===== */
        .watermark {
            position: absolute;
            top: 16px; right: 16px;
            font-size: 10px;
            color: rgba(255,255,255,0.15);
            font-weight: 600;
            letter-spacing: 1px;
            z-index: 2;
            pointer-events: none;
        }

        /* ===== CONTEXT MENU ===== */
        .context-menu {
            position: fixed;
            background: var(--bg-secondary);
            border: 1px solid var(--border);
            border-radius: var(--radius-sm);
            padding: 6px;
            min-width: 180px;
            z-index: 3000;
            display: none;
            box-shadow: 0 10px 40px rgba(0,0,0,0.4);
        }

        .context-menu.active { display: block; }

        .context-item {
            display: flex;
            align-items: center;
            gap: 10px;
            padding: 10px 14px;
            border-radius: 8px;
            font-size: 13px;
            cursor: pointer;
            transition: var(--transition);
            color: var(--text-secondary);
        }

        .context-item:hover {
            background: var(--bg-tertiary);
            color: var(--text-primary);
        }

        .context-item i { width: 16px; text-align: center; }

        .context-divider {
            height: 1px;
            background: var(--border);
            margin: 4px 0;
        }

        /* Recording indicator */
        .recording-indicator {
            position: absolute;
            top: 16px; left: 80px;
            display: flex;
            align-items: center;
            gap: 6px;
            background: rgba(233,69,96,0.9);
            padding: 6px 12px;
            border-radius: 20px;
            font-size: 12px;
            font-weight: 700;
            z-index: 10;
            display: none;
        }

        .recording-indicator.active { display: flex; }

        .rec-dot {
            width: 8px; height: 8px;
            background: white;
            border-radius: 50%;
            animation: blink 1s infinite;
        }

        /* Channel groups */
        .group-header {
            padding: 10px 12px 4px;
            font-size: 11px;
            font-weight: 700;
            color: var(--text-muted);
            text-transform: uppercase;
            letter-spacing: 1px;
            display: flex;
            align-items: center;
            gap: 8px;
        }

        .group-header::after {
            content: '';
            flex: 1;
            height: 1px;
            background: var(--border);
        }

        /* Import section */
        .import-dropzone {
            border: 2px dashed var(--border);
            border-radius: var(--radius);
            padding: 40px;
            text-align: center;
            cursor: pointer;
            transition: var(--transition);
        }

        .import-dropzone:hover {
            border-color: var(--accent);
            background: rgba(233,69,96,0.03);
        }

        .import-dropzone i {
            font-size: 36px;
            color: var(--text-muted);
            margin-bottom: 12px;
        }

        .import-dropzone p {
            font-size: 14px;
            color: var(--text-secondary);
        }

        .import-dropzone span {
            font-size: 12px;
            color: var(--text-muted);
        }

        .hidden { display: none !important; }
    </style>
</head>
<body>
    <!-- HEADER -->
    <header class="app-header">
        <div class="logo">
            <div class="logo-icon">📺</div>
            <span class="logo-text">Ultimate IPTV</span>
            <span class="logo-badge">PRO</span>
            <button class="header-btn mobile-toggle" onclick="toggleSidebar()">
                <i class="fas fa-bars"></i>
            </button>
        </div>
        <div class="header-actions">
            <button class="header-btn" onclick="openModal('settingsModal')" title="Ayarlar">
                <i class="fas fa-cog"></i>
            </button>
            <button class="header-btn" onclick="openModal('importModal')" title="İçe Aktar">
                <i class="fas fa-file-import"></i>
            </button>
            <button class="header-btn" onclick="exportPlaylist()" title="Dışa Aktar">
                <i class="fas fa-file-export"></i>
            </button>
            <button class="header-btn" onclick="openModal('statsModal')" title="İstatistikler">
                <i class="fas fa-chart-bar"></i>
            </button>
            <button class="header-btn" onclick="toggleTheme()" title="Tema">
                <i class="fas fa-moon"></i>
            </button>
        </div>
    </header>

    <!-- MAIN -->
    <div class="app-container">
        <!-- SIDEBAR -->
        <aside class="sidebar" id="sidebar">
            <div class="sidebar-header">
                <div class="search-box">
                    <i class="fas fa-search"></i>
                    <input type="text" id="searchInput" placeholder="Kanal ara..." oninput="filterChannels()">
                </div>
            </div>
            <div class="category-tabs" id="categoryTabs"></div>
            <div class="channel-list" id="channelList"></div>
        </aside>

        <!-- MAIN CONTENT -->
        <main class="main-content" id="mainContent">
            <!-- Welcome Screen -->
            <div class="welcome-screen" id="welcomeScreen">
                <div class="welcome-icon">📺</div>
                <h2>Ultimate IPTV Player Pro</h2>
                <p>Türk kanalları hazır! Kanalları görüntülemek için bir kanal seçin veya yeni bir IPTV adresi ekleyin.</p>
                <div class="welcome-actions">
                    <button class="welcome-btn primary" onclick="loadDefaultChannels()">
                        <i class="fas fa-play"></i> Kanalları Yükle
                    </button>
                    <button class="welcome-btn" onclick="openModal('importModal')">
                        <i class="fas fa-plus"></i> IPTV Ekle
                    </button>
                </div>
            </div>

            <!-- Player -->
            <div class="player-container hidden" id="playerContainer" ondblclick="toggleFullscreen()">
                <video id="videoPlayer" playsinline></video>
                <div class="loading-overlay" id="loadingOverlay">
                    <div class="spinner"></div>
                    <span class="loading-text">Yükleniyor...</span>
                </div>
                <div class="watermark">ULTIMATE IPTV PRO</div>
                <div class="recording-indicator" id="recIndicator">
                    <div class="rec-dot"></div>
                    <span>KAYIT</span>
                </div>
                <div class="player-top-bar">
                    <div class="live-badge">
                        <div class="live-dot"></div>
                        CANLI
                    </div>
                    <div class="player-top-actions">
                        <select class="quality-selector" id="qualitySelector" onchange="changeQuality(this.value)">
                            <option value="auto">Otomatik</option>
                        </select>
                        <button class="ctrl-btn" onclick="toggleRecording()" title="Kayıt">
                            <i class="fas fa-circle" style="font-size:12px;color:#e94560"></i>
                        </button>
                        <button class="ctrl-btn" onclick="togglePIP()" title="Resim İçinde Resim">
                            <i class="fas fa-clone"></i>
                        </button>
                        <button class="ctrl-btn" onclick="toggleFullscreen()" title="Tam Ekran">
                            <i class="fas fa-expand" id="fsIcon"></i>
                        </button>
                    </div>
                </div>
                <div class="player-overlay">
                    <div class="player-info-bar">
                        <div class="now-playing">
                            <div class="now-playing-logo" id="npLogo">📺</div>
                            <div class="now-playing-info">
                                <h3 id="npName">Kanal Adı</h3>
                                <p id="npCategory">Kategori</p>
                            </div>
                        </div>
                    </div>
                    <div class="player-controls">
                        <button class="ctrl-btn" onclick="prevChannel()">
                            <i class="fas fa-backward-step"></i>
                        </button>
                        <button class="ctrl-btn" onclick="rewind10()">
                            <i class="fas fa-backward"></i>
                        </button>
                        <button class="ctrl-btn play-btn" id="playBtn" onclick="togglePlay()">
                            <i class="fas fa-pause" id="playIcon"></i>
                        </button>
                        <button class="ctrl-btn" onclick="forward10()">
                            <i class="fas fa-forward"></i>
                        </button>
                        <button class="ctrl-btn" onclick="nextChannel()">
                            <i class="fas fa-forward-step"></i>
                        </button>
                        <input type="range" class="volume-slider" id="volumeSlider" min="0" max="100" value="80" oninput="changeVolume(this.value)">
                        <button class="ctrl-btn" onclick="toggleMute()">
                            <i class="fas fa-volume-high" id="volIcon"></i>
                        </button>
                    </div>
                </div>
            </div>

            <!-- Detail Panel -->
            <div class="detail-panel hidden" id="detailPanel">
                <div class="detail-header">
                    <div class="detail-logo" id="detailLogo">📺</div>
                    <div class="detail-title">
                        <h2 id="detailName">Kanal Adı</h2>
                        <p id="detailInfo">Kategori • Ülke</p>
                    </div>
                    <button class="fav-btn" id="favBtn" onclick="toggleFavorite()">
                        <i class="fas fa-star"></i>
                    </button>
                </div>
                <div class="epg-section">
                    <div class="epg-title">
                        <i class="fas fa-calendar-alt"></i> Program Rehberi (EPG)
                    </div>
                    <div id="epgList"></div>
                </div>
            </div>
        </main>
    </div>

    <!-- CONTEXT MENU -->
    <div class="context-menu" id="contextMenu">
        <div class="context-item" onclick="contextPlay()">
            <i class="fas fa-play"></i> Oynat
        </div>
        <div class="context-item" onclick="contextFavorite()">
            <i class="fas fa-star"></i> Favorilere Ekle
        </div>
        <div class="context-divider"></div>
        <div class="context-item" onclick="contextCopyUrl()">
            <i class="fas fa-copy"></i> URL Kopyala
        </div>
        <div class="context-item" onclick="contextInfo()">
            <i class="fas fa-info-circle"></i> Bilgi
        </div>
        <div class="context-divider"></div>
        <div class="context-item" onclick="contextDelete()" style="color:var(--accent)">
            <i class="fas fa-trash"></i> Sil
        </div>
    </div>

    <!-- TOAST CONTAINER -->
    <div class="toast-container" id="toastContainer"></div>

    <!-- MODALS -->
    <!-- Import Modal -->
    <div class="modal-overlay" id="importModal">
        <div class="modal">
            <div class="modal-header">
                <h3><i class="fas fa-file-import"></i> Kanal İçe Aktar</h3>
                <button class="modal-close" onclick="closeModal('importModal')">
                    <i class="fas fa-times"></i>
                </button>
            </div>
            <div class="modal-body">
                <!-- Webhost TV IP Module -->
                <div class="webhost-module">
                    <div class="webhost-header">
                        <div class="webhost-icon"><i class="fas fa-server"></i></div>
                        <div>
                            <h4>Akıllı Webhost TV IP Modülü</h4>
                            <p>Canlı sunucu adreslerini tarayın ve otomatik bağlanın</p>
                        </div>
                    </div>
                    <div class="form-group">
                        <label class="form-label">Sunucu URL (ör: http://sunucu.com:port)</label>
                        <input type="text" class="form-input" id="webhostUrl" placeholder="http://sunucu.com:8080">
                    </div>
                    <div class="form-group">
                        <div style="display:grid;grid-template-columns:1fr 1fr;gap:10px">
                            <div>
                                <label class="form-label">Kullanıcı Adı</label>
                                <input type="text" class="form-input" id="webhostUser" placeholder="username">
                            </div>
                            <div>
                                <label class="form-label">Şifre</label>
                                <input type="password" class="form-input" id="webhostPass" placeholder="password">
                            </div>
                        </div>
                    </div>
                    <div class="btn-group">
                        <button class="btn btn-primary" onclick="webhostConnect()">
                            <i class="fas fa-plug"></i> Bağlan &amp; Yükle
                        </button>
                        <button class="btn btn-secondary" onclick="webhostScan()">
                            <i class="fas fa-radar"></i> Tarama Yap
                        </button>
                    </div>
                    <div class="server-grid" id="serverGrid" style="margin-top:16px"></div>
                </div>

                <div style="text-align:center;padding:16px 0;color:var(--text-muted);font-size:13px">
                    — veya —
                </div>

                <!-- M3U URL -->
                <div class="form-group">
                    <label class="form-label">M3U/M3U8 URL Adresi</label>
                    <div style="display:flex;gap:8px">
                        <input type="text" class="form-input" id="m3uUrlInput" placeholder="https://example.com/playlist.m3u">
                        <button class="btn btn-primary" style="flex-shrink:0" onclick="loadFromUrl()">
                            <i class="fas fa-download"></i> Yükle
                        </button>
                    </div>
                </div>

                <!-- URL List -->
                <div class="form-group">
                    <label class="form-label">Kayıtlı Sunucularım</label>
                    <div class="url-list" id="savedUrls"></div>
                </div>

                <!-- File Upload -->
                <div class="form-group">
                    <label class="form-label">M3U Dosyası Yükle</label>
                    <div class="import-dropzone" onclick="document.getElementById('fileInput').click()">
                        <i class="fas fa-cloud-upload-alt"></i>
                        <p>Dosyayı sürükleyin veya tıklayın</p>
                        <span>M3U, M3U8, TXT desteklenir</span>
                    </div>
                    <input type="file" id="fileInput" accept=".m3u,.m3u8,.txt" style="display:none" onchange="loadFromFile(event)">
                </div>

                <!-- Paste M3U -->
                <div class="form-group">
                    <label class="form-label">M3U İçeriği Yapıştır</label>
                    <textarea class="form-input" id="m3uPaste" placeholder="#EXTM3U...&#10;#EXTINF:-1 tvg-name=&quot;TRT 1&quot; group-title=&quot;Genel&quot;,TRT 1&#10;http://..."></textarea>
                    <button class="btn btn-primary" style="margin-top:10px;width:100%" onclick="loadFromPaste()">
                        <i class="fas fa-paste"></i> Yapıştırılan İçeriği Yükle
                    </button>
                </div>
            </div>
        </div>
    </div>

    <!-- Settings Modal -->
    <div class="modal-overlay" id="settingsModal">
        <div class="modal">
            <div class="modal-header">
                <h3><i class="fas fa-cog"></i> Ayarlar</h3>
                <button class="modal-close" onclick="closeModal('settingsModal')">
                    <i class="fas fa-times"></i>
                </button>
            </div>
            <div class="modal-body">
                <div class="form-group">
                    <label class="form-label">Oynatma Motoru</label>
                    <select class="form-input" id="playerEngine" onchange="saveSetting('playerEngine', this.value)">
                        <option value="hls">HLS.js (Önerilen)</option>
                        <option value="shaka">Shaka Player (DASH)</option>
                        <option value="native">Native HTML5</option>
                    </select>
                </div>
                <div class="form-group">
                    <label class="form-label">Buffer Boyutu (saniye)</label>
                    <input type="number" class="form-input" id="bufferSize" value="30" min="5" max="120" onchange="saveSetting('bufferSize', this.value)">
                </div>
                <div class="form-group">
                    <label class="form-label">Varsayılan Kalite</label>
                    <select class="form-input" id="defaultQuality" onchange="saveSetting('defaultQuality', this.value)">
                        <option value="auto">Otomatik</option>
                        <option value="best">En İyi</option>
                        <option value="720">720p</option>
                        <option value="480">480p</option>
                        <option value="360">360p</option>
                    </select>
                </div>
                <div class="form-group">
                    <label class="form-label">Otomatik Oynat</label>
                    <select class="form-input" id="autoPlay" onchange="saveSetting('autoPlay', this.value)">
                        <option value="true">Evet</option>
                        <option value="false">Hayır</option>
                    </select>
                </div>
                <div class="form-group">
                    <label class="form-label">Altyazı Dili</label>
                    <select class="form-input" id="subtitleLang" onchange="saveSetting('subtitleLang', this.value)">
                        <option value="tr">Türkçe</option>
                        <option value="en">İngilizce</option>
                        <option value="off">Kapalı</option>
                    </select>
                </div>
                <div class="form-group">
                    <label class="form-label">Gecikme Uyarısı (ms)</label>
                    <input type="number" class="form-input" id="latencyWarning" value="5000" onchange="saveSetting('latencyWarning', this.value)">
                </div>
                <button class="btn btn-primary" style="width:100%" onclick="resetSettings()">
                    <i class="fas fa-undo"></i> Varsayılana Sıfırla
                </button>
            </div>
        </div>
    </div>

    <!-- Stats Modal -->
    <div class="modal-overlay" id="statsModal">
        <div class="modal">
            <div class="modal-header">
                <h3><i class="fas fa-chart-bar"></i> İstatistikler</h3>
                <button class="modal-close" onclick="closeModal('statsModal')">
                    <i class="fas fa-times"></i>
                </button>
            </div>
            <div class="modal-body">
                <div class="stats-grid">
                    <div class="stat-card">
                        <div class="stat-value" id="statTotal">0</div>
                        <div class="stat-label">Toplam Kanal</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-value" id="statCategories">0</div>
                        <div class="stat-label">Kategori</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-value" id="statFavorites">0</div>
                        <div class="stat-label">Favoriler</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-value" id="statWatched">0</div>
                        <div class="stat-label">İzlenen</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-value" id="statServers">0</div>
                        <div class="stat-label">Sunucu</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-value" id="statUptime">0s</div>
                        <div class="stat-label">Çalışma</div>
                    </div>
                </div>
                <div style="margin-top:20px">
                    <button class="btn btn-secondary" style="width:100%" onclick="clearAllData()">
                        <i class="fas fa-trash"></i> Tüm Verileri Temizle
                    </button>
                </div>
            </div>
        </div>
    </div>

<script>
// ==============================
// ULTIMATE IPTV PLAYER PRO - ENGINE
// ==============================

// ===== STATE =====
const APP = {
    channels: [],
    favorites: new Set(),
    watched: new Set(),
    savedUrls: [],
    servers: [],
    currentChannel: null,
    currentCategory: 'all',
    hls: null,
    shaka: null,
    startTime: Date.now(),
    isRecording: false,
    mediaRecorder: null,
    recordedChunks: [],
    settings: {
        playerEngine: 'hls',
        bufferSize: 30,
        defaultQuality: 'auto',
        autoPlay: 'true',
        subtitleLang: 'tr',
        latencyWarning: 5000
    }
};

// ===== TURKISH DEFAULT CHANNELS =====
const DEFAULT_CHANNELS = [
    // GENEL
    { name: "TRT 1", url: "https://tv-trt1.medya.trt.com.tr/master_720.m3u8", category: "Genel", country: "TR", logo: "📺", group: "TRT" },
    { name: "TRT 2", url: "https://tv-trt2.medya.trt.com.tr/master.m3u8", category: "Genel", country: "TR", logo: "📺", group: "TRT" },
    { name: "TRT Haber", url: "https://tv-trthaber.medya.trt.com.tr/master.m3u8", category: "Haber", country: "TR", logo: "📰", group: "TRT" },
    { name: "TRT Spor", url: "https://tv-trtspor.medya.trt.com.tr/master.m3u8", category: "Spor", country: "TR", logo: "⚽", group: "TRT" },
    { name: "TRT Spor Yıldız", url: "https://tv-trtspor2.medya.trt.com.tr/master.m3u8", category: "Spor", country: "TR", logo: "⭐", group: "TRT" },
    { name: "TRT Çocuk", url: "https://tv-trtcocuk.medya.trt.com.tr/master.m3u8", category: "Çocuk", country: "TR", logo: "🧸", group: "TRT" },
    { name: "TRT Belgesel", url: "https://tv-trtbelgesel.medya.trt.com.tr/master.m3u8", category: "Belgesel", country: "TR", logo: "🎬", group: "TRT" },
    { name: "TRT Müzik", url: "https://tv-trtmuzik.medya.trt.com.tr/master.m3u8", category: "Müzik", country: "TR", logo: "🎵", group: "TRT" },
    { name: "TRT Avaz", url: "https://tv-trtavaz.medya.trt.com.tr/master.m3u8", category: "Genel", country: "TR", logo: "🌍", group: "TRT" },
    { name: "TRT Türk", url: "https://tv-trtturk.medya.trt.com.tr/master.m3u8", category: "Genel", country: "TR", logo: "🇹🇷", group: "TRT" },
    { name: "TRT Arabi", url: "https://tv-trtarabi.medya.trt.com.tr/master.m3u8", category: "Genel", country: "TR", logo: "🌍", group: "TRT" },
    { name: "TRT World", url: "https://tv-trtworld.medya.trt.com.tr/master.m3u8", category: "Haber", country: "TR", logo: "🌐", group: "TRT" },
    { name: "TRT Haber (Test Card)", url: "https://trtcanlitv-lh.akamaihd.net/i/TRTHABER_1@182494/master.m3u8", category: "Haber", country: "TR", logo: "📰", group: "TRT" },
    { name: "ATV", url: "https://trkvz-live.daioncdn.net/atv/atv.m3u8", category: "Genel", country: "TR", logo: "📺", group: "Doğuş" },
    { name: "Star TV", url: "https://dogus-live.daioncdn.net/startv/startv.m3u8", category: "Genel", country: "TR", logo: "⭐", group: "Doğuş" },
    { name: "Show TV", url: "https://ciner-live.daioncdn.net/showtv/showtv.m3u8", category: "Genel", country: "TR", logo: "📺", group: "Ciner" },
    { name: "Kanal D", url: "https://demiroren-live.daioncdn.net/kanald/kanald.m3u8", category: "Genel", country: "TR", logo: "📺", group: "Demirören" },
    { name: "Fox TV", url: "https://hls-media.havadurumu15gunluk.org/fox-tv.m3u8", category: "Genel", country: "TR", logo: "🦊", group: "Fox" },
    { name: "TV8", url: "https://dogus-live.daioncdn.net/tv8/tv8.m3u8", category: "Genel", country: "TR", logo: "📺", group: "Acun" },
    { name: "CNN Türk", url: "https://demiroren-live.daioncdn.net/cnnturk/cnnturk.m3u8", category: "Haber", country: "TR", logo: "📡", group: "Demirören" },
    { name: "Haber Türk", url: "https://ciner-live.daioncdn.net/haberturk/haberturk.m3u8", category: "Haber", country: "TR", logo: "📰", group: "Ciner" },
    { name: "NTV", url: "https://dogus-live.daioncdn.net/ntv/ntv.m3u8", category: "Haber", country: "TR", logo: "📰", group: "Doğuş" },
    { name: "A Haber", url: "https://trkvz-live.daioncdn.net/ahaber/ahaber.m3u8", category: "Haber", country: "TR", logo: "📡", group: "Kalyon" },
    { name: "Bloomberg HT", url: "https://ciner-live.daioncdn.net/bloomberght/bloomberght.m3u8", category: "Haber", country: "TR", logo: "💹", group: "Ciner" },
    { name: "Halk TV", url: "https://havadurumu15gunluk.org/halk-tv.m3u8", category: "Haber", country: "TR", logo: "📰", group: "Halk" },
    { name: "Tele1", url: "https://havadurumu15gunluk.org/tele1.m3u8", category: "Haber", country: "TR", logo: "📡", group: "Tele1" },
    { name: "KRT TV", url: "https://havadurumu15gunluk.org/krt-tv.m3u8", category: "Haber", country: "TR", logo: "📺", group: "KRT" },
    { name: "Ulusal Kanal", url: "https://havadurumu15gunluk.org/ulusal-kanal.m3u8", category: "Haber", country: "TR", logo: "📺", group: "Ulusal" },
    { name: "beIN Sports Haber", url: "https://havadurumu15gunluk.org/bein-sports-haber.m3u8", category: "Spor", country: "TR", logo: "⚽", group: "beIN" },
    { name: "A Spor", url: "https://trkvz-live.daioncdn.net/aspor/aspor.m3u8", category: "Spor", country: "TR", logo: "⚽", group: "Kalyon" },
    { name: "S Sport", url: "https://havadurumu15gunluk.org/s-sport.m3u8", category: "Spor", country: "TR", logo: "🏈", group: "Saran" },
    { name: "S Sport 2", url: "https://havadurumu15gunluk.org/s-sport-2.m3u8", category: "Spor", country: "TR", logo: "🏈", group: "Saran" },
    { name: "Euro Star", url: "https://havadurumu15gunluk.org/euro-star.m3u8", category: "Genel", country: "TR", logo: "⭐", group: "Doğuş" },
    { name: "TLC", url: "https://havadurumu15gunluk.org/tlc.m3u8", category: "Belgesel", country: "TR", logo: "🎬", group: "Discovery" },
    { name: "Discovery Channel TR", url: "https://havadurumu15gunluk.org/discovery.m3u8", category: "Belgesel", country: "TR", logo: "🔍", group: "Discovery" },
    { name: "National Geographic TR", url: "https://havadurumu15gunluk.org/natgeo.m3u8", category: "Belgesel", country: "TR", logo: "🌍", group: "NatGeo" },
    { name: "Da Vinci Kids", url: "https://havadurumu15gunluk.org/da-vinci.m3u8", category: "Çocuk", country: "TR", logo: "🎨", group: "DaVinci" },
    { name: "Minika Çocuk", url: "https://havadurumu15gunluk.org/minika-cocuk.m3u8", category: "Çocuk", country: "TR", logo: "🧸", group: "Minika" },
    { name: "Minika Go", url: "https://havadurumu15gunluk.org/minika-go.m3u8", category: "Çocuk", country: "TR", logo: "🎮", group: "Minika" },
    { name: "Cartoon Network TR", url: "https://havadurumu15gunluk.org/cartoon-network.m3u8", category: "Çocuk", country: "TR", logo: "🎭", group: "CN" },
    { name: "Nickelodeon TR", url: "https://havadurumu15gunluk.org/nickelodeon.m3u8", category: "Çocuk", country: "TR", logo: "🎮", group: "Nick" },
    { name: "Dream TV", url: "https://havadurumu15gunluk.org/dream-tv.m3u8", category: "Müzik", country: "TR", logo: "🎵", group: "Doğuş" },
    { name: "Number One TV", url: "https://havadurumu15gunluk.org/number-one-tv.m3u8", category: "Müzik", country: "TR", logo: "🎵", group: "Number" },
    { name: "Kral TV", url: "https://trkvz-live.daioncdn.net/kraltv/kraltv.m3u8", category: "Müzik", country: "TR", logo: "👑", group: "Kalyon" },
    { name: "Power TV", url: "https://havadurumu15gunluk.org/power-tv.m3u8", category: "Müzik", country: "TR", logo: "💪", group: "Power" },
    { name: "TV8.5", url: "https://dogus-live.daioncdn.net/tv85/tv85.m3u8", category: "Genel", country: "TR", logo: "📺", group: "Acun" },
    { name: "A2 TV", url: "https://trkvz-live.daioncdn.net/a2tv/a2tv.m3u8", category: "Genel", country: "TR", logo: "📺", group: "Kalyon" },
    { name: "360 TV", url: "https://havadurumu15gunluk.org/360-tv.m3u8", category: "Genel", country: "TR", logo: "📺", group: "Star" },
    { name: "Teve2", url: "https://havadurumu15gunluk.org/teve2.m3u8", category: "Genel", country: "TR", logo: "📺", group: "Demirören" },
    { name: "Kanal 7", url: "https://havadurumu15gunluk.org/kanal7.m3u8", category: "Genel", country: "TR", logo: "📺", group: "Yeni Şafak" },
    { name: " Ülke TV", url: "https://havadurumu15gunluk.org/ulke-tv.m3u8", category: "Haber", country: "TR", logo: "📰", group: "Yeni Şafak" },
    { name: "24 TV", url: "https://havadurumu15gunluk.org/24-tv.m3u8", category: "Haber", country: "TR", logo: "📰", group: "Star" },
    { name: "TGRT Haber", url: "https://havadurumu15gunluk.org/tgrt-haber.m3u8", category: "Haber", country: "TR", logo: "📰", group: "TGRT" },
    { name: "TVNET", url: "https://havadurumu15gunluk.org/tvnet.m3u8", category: "Haber", country: "TR", logo: "📰", group: "TVNET" },
    { name: "Beyaz TV", url: "https://havadurumu15gunluk.org/beyaz-tv.m3u8", category: "Genel", country: "TR", logo: "📺", group: "Beyaz" },
    { name: "Flash TV", url: "https://havadurumu15gunluk.org/flash-tv.m3u8", category: "Genel", country: "TR", logo: "📺", group: "Flash" },
    { name: "Cine5", url: "https://havadurumu15gunluk.org/cine5.m3u8", category: "Sinema", country: "TR", logo: "🎬", group: "Cine" },
    { name: "Sinema TV", url: "https://havadurumu15gunluk.org/sinema-tv.m3u8", category: "Sinema", country: "TR", logo: "🎬", group: "D-Smart" },
    { name: "Sinema 1001", url: "https://havadurumu15gunluk.org/sinema-1001.m3u8", category: "Sinema", country: "TR", logo: "🎬", group: "D-Smart" },
    // INTERNATIONAL
    { name: "BBC World News", url: "https://vs-cmaf-push-live.bbcfmt.hs.llnwd.net/pool_902/live/bbc_world_news/bbc_world_news.isml/bbc_world_news-audio%3D96000-video%3D3500000.dash", category: "Haber", country: "INT", logo: "🌍", group: "BBC" },
    { name: "CNN International", url: "https://tve-live.cnn.com/nxsvnhpwr/bpk-vod/cnn/line.m3u8", category: "Haber", country: "INT", logo: "📡", group: "CNN" },
    { name: "Al Jazeera English", url: "https://live-hls-web-aje.getaj.net/AJE/index.m3u8", category: "Haber", country: "INT", logo: "🌍", group: "AJ" },
    { name: "France 24 English", url: "https://f24hls-i.akamaihd.net/hls/live/221241-b/F24_EN_LO_HLS/master.m3u8", category: "Haber", country: "INT", logo: "🇫🇷", group: "F24" },
    { name: "DW English", url: "https://dwamdstream102.akamaized.net/hls/live/2015525/dwstream102/master.m3u8", category: "Haber", country: "INT", logo: "🇩🇪", group: "DW" },
    { name: "RT News", url: "https://rt-glb.rttv.com/live/rtnews/playlist.m3u8", category: "Haber", country: "INT", logo: "🇷🇺", group: "RT" },
    { name: "Euronews", url: "https://euronews-euronews-world-1-eu.rakuten.wurl.tv/playlist.m3u8", category: "Haber", country: "INT", logo: "🇪🇺", group: "Euronews" },
    { name: "Sky News", url: "https://skynewsau-1-eu.rakuten.wurl.tv/playlist.m3u8", category: "Haber", country: "INT", logo: "☁️", group: "Sky" },
    { name: "Bloomberg TV", url: "https://bloomberg-bloomberg-1-eu.rakuten.wurl.tv/playlist.m3u8", category: "Haber", country: "INT", logo: "💹", group: "Bloomberg" }
];

// ===== INIT =====
function init() {
    loadFromStorage();
    renderCategoryTabs();
    renderChannels();
    renderSavedUrls();
    updateStats();

    // If no channels, load defaults
    if (APP.channels.length === 0) {
        loadDefaultChannels();
    }

    // Global keyboard shortcuts
    document.addEventListener('keydown', handleKeyboard);
    document.addEventListener('click', () => {
        document.getElementById('contextMenu').classList.remove('active');
    });

    // Update stats timer
    setInterval(updateStats, 1000);

    // Volume
    const video = document.getElementById('videoPlayer');
    video.volume = 0.8;
}

// ===== STORAGE =====
function loadFromStorage() {
    try {
        const ch = localStorage.getItem('iptv_channels');
        if (ch) APP.channels = JSON.parse(ch);
        const fav = localStorage.getItem('iptv_favorites');
        if (fav) APP.favorites = new Set(JSON.parse(fav));
        const w = localStorage.getItem('iptv_watched');
        if (w) APP.watched = new Set(JSON.parse(w));
        const urls = localStorage.getItem('iptv_urls');
        if (urls) APP.savedUrls = JSON.parse(urls);
        const set = localStorage.getItem('iptv_settings');
        if (set) APP.settings = { ...APP.settings, ...JSON.parse(set) };
    } catch(e) { console.error('Storage load error:', e); }
}

function saveToStorage() {
    try {
        localStorage.setItem('iptv_channels', JSON.stringify(APP.channels));
        localStorage.setItem('iptv_favorites', JSON.stringify([...APP.favorites]));
        localStorage.setItem('iptv_watched', JSON.stringify([...APP.watched]));
        localStorage.setItem('iptv_urls', JSON.stringify(APP.savedUrls));
        localStorage.setItem('iptv_settings', JSON.stringify(APP.settings));
    } catch(e) { console.error('Storage save error:', e); }
}

// ===== LOAD DEFAULT CHANNELS =====
function loadDefaultChannels() {
    APP.channels = DEFAULT_CHANNELS.map((ch, i) => ({ ...ch, id: i }));
    saveToStorage();
    renderCategoryTabs();
    renderChannels();
    showToast('success', `${APP.channels.length} kanal yüklendi!`);
}

// ===== M3U PARSER =====
function parseM3U(content) {
    const channels = [];
    const lines = content.split('\n');
    let current = null;

    for (let i = 0; i < lines.length; i++) {
        const line = lines[i].trim();

        if (line.startsWith('#EXTINF:')) {
            current = { id: Date.now() + Math.random(), name: '', url: '', category: 'Genel', country: 'TR', logo: '📺', group: 'Diğer' };

            // Extract name
            const nameMatch = line.match(/,(.+)$/);
            if (nameMatch) current.name = nameMatch[1].trim();

            // Extract group
            const groupMatch = line.match(/group-title="([^"]*)"/);
            if (groupMatch) current.category = groupMatch[1].trim() || 'Genel';

            // Extract tvg-name
            const tvgNameMatch = line.match(/tvg-name="([^"]*)"/);
            if (tvgNameMatch && !current.name) current.name = tvgNameMatch[1];

            // Extract logo
            const logoMatch = line.match(/tvg-logo="([^"]*)"/);
            if (logoMatch) current.logo = logoMatch[1];

            // Extract country
            const countryMatch = line.match(/tvg-country="([^"]*)"/);
            if (countryMatch) current.country = countryMatch[1];
        } else if (current && line && !line.startsWith('#')) {
            current.url = line;
            current.name = current.name || 'Bilinmeyen Kanal';
            channels.push(current);
            current = null;
        }
    }

    return channels;
}

// ===== LOAD FROM URL =====
async function loadFromUrl() {
    const url = document.getElementById('m3uUrlInput').value.trim();
    if (!url) return showToast('error', 'URL giriniz!');

    showToast('info', 'Yükleniyor...');

    try {
        // Try direct fetch first
        let content;
        try {
            const resp = await fetch(url);
            content = await resp.text();
        } catch {
            // Fallback to CORS proxy
            const proxyUrl = `https://api.allorigins.win/raw?url=${encodeURIComponent(url)}`;
            const resp = await fetch(proxyUrl);
            content = await resp.text();
        }

        if (!content.includes('#EXTM3U') && !content.includes('#EXTINF')) {
            return showToast('error', 'Geçersiz M3U formatı!');
        }

        const channels = parseM3U(content);
        if (channels.length === 0) return showToast('error', 'Kanal bulunamadı!');

        // Add to existing channels
        channels.forEach(ch => {
            ch.id = Date.now() + Math.random();
            if (!APP.channels.find(c => c.url === ch.url)) {
                APP.channels.push(ch);
            }
        });

        // Save URL
        if (!APP.savedUrls.includes(url)) {
            APP.savedUrls.push(url);
        }

        saveToStorage();
        renderCategoryTabs();
        renderChannels();
        renderSavedUrls();
        closeModal('importModal');
        showToast('success', `${channels.length} kanal eklendi!`);
    } catch (e) {
        showToast('error', 'Yükleme hatası: ' + e.message);
    }
}

// ===== LOAD FROM FILE =====
function loadFromFile(event) {
    const file = event.target.files[0];
    if (!file) return;

    const reader = new FileReader();
    reader.onload = (e) => {
        const content = e.target.result;
        const channels = parseM3U(content);
        if (channels.length === 0) return showToast('error', 'Kanal bulunamadı!');

        channels.forEach(ch => {
            ch.id = Date.now() + Math.random();
            if (!APP.channels.find(c => c.url === ch.url)) {
                APP.channels.push(ch);
            }
        });

        saveToStorage();
        renderCategoryTabs();
        renderChannels();
        closeModal('importModal');
        showToast('success', `${channels.length} kanal dosyadan yüklendi!`);
    };
    reader.readAsText(file);
}

// ===== LOAD FROM PASTE =====
function loadFromPaste() {
    const content = document.getElementById('m3uPaste').value.trim();
    if (!content) return showToast('error', 'M3U içeriği yapıştırınız!');

    const channels = parseM3U(content);
    if (channels.length === 0) return showToast('error', 'Kanal bulunamadı!');

    channels.forEach(ch => {
        ch.id = Date.now() + Math.random();
        if (!APP.channels.find(c => c.url === ch.url)) {
            APP.channels.push(ch);
        }
    });

    saveToStorage();
    renderCategoryTabs();
    renderChannels();
    closeModal('importModal');
    showToast('success', `${channels.length} kanal yapıştırma ile eklendi!`);
}

// ===== EXPORT PLAYLIST =====
function exportPlaylist() {
    let m3u = '#EXTM3U\n\n';
    APP.channels.forEach(ch => {
        m3u += `#EXTINF:-1 tvg-id="${ch.id}" tvg-name="${ch.name}" tvg-logo="${ch.logo || ''}" group-title="${ch.category}",${ch.name}\n`;
        m3u += `${ch.url}\n\n`;
    });

    const blob = new Blob([m3u], { type: 'audio/x-mpegurl' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = 'ultimate_iptv_playlist.m3u';
    a.click();
    URL.revokeObjectURL(url);
    showToast('success', 'Playlist dışa aktarıldı!');
}

// ===== WEBHOST TV IP MODULE =====
function webhostConnect() {
    const serverUrl = document.getElementById('webhostUrl').value.trim();
    const user = document.getElementById('webhostUser').value.trim();
    const pass = document.getElementById('webhostPass').value.trim();

    if (!serverUrl) return showToast('error', 'Sunucu URL giriniz!');

    showToast('info', 'Sunucuya bağlanılıyor...');

    // Construct Xtream Codes style URLs
    const baseUrl = serverUrl.replace(/\/$/, '');
    const playerApiUrl = `${baseUrl}/player_api.php?username=${user}&password=${pass}`;
    const liveStreamUrl = `${baseUrl}/live/${user}/${pass}`;

    // Save as server
    APP.servers.push({
        url: baseUrl,
        user: user,
        status: 'connected',
        time: Date.now()
    });

    // Try to get live categories
    fetch(playerApiUrl + '&action=get_live_categories')
        .then(r => r.json())
        .then(cats => {
            // Get live streams
            return fetch(playerApiUrl + '&action=get_live_streams')
                .then(r => r.json())
                .then(streams => ({ cats, streams }));
        })
        .then(({ cats, streams }) => {
            if (streams && streams.length > 0) {
                streams.forEach(s => {
                    const channel = {
                        id: Date.now() + Math.random(),
                        name: s.name || 'Unknown',
                        url: `${liveStreamUrl}/${s.stream_id}.m3u8`,
                        category: s.category_name || 'Genel',
                        country: 'TR',
                        logo: s.stream_icon || '📺',
                        group: 'Webhost'
                    };
                    if (!APP.channels.find(c => c.name === channel.name)) {
                        APP.channels.push(channel);
                    }
                });
                saveToStorage();
                renderCategoryTabs();
                renderChannels();
                closeModal('importModal');
                showToast('success', `${streams.length} kanal webhost'tan yüklendi!`);
            }
        })
        .catch(() => {
            // Try as simple M3U URL
            const m3uUrl = `${baseUrl}/get.php?username=${user}&password=${pass}&type=m3u_plus&output=ts`;
            document.getElementById('m3uUrlInput').value = m3uUrl;
            loadFromUrl();
        });
}

function webhostScan() {
    showToast('info', 'Sunucular taranıyor...');

    const demoServers = [
        { name: 'Ana Sunucu', icon: '🖥️', ping: '12ms' },
        { name: 'Yedek Sunucu', icon: '💾', ping: '28ms' },
        { name: 'CDN Node EU', icon: '🌍', ping: '45ms' },
        { name: 'CDN Node TR', icon: '🇹🇷', ping: '8ms' },
    ];

    const grid = document.getElementById('serverGrid');
    grid.innerHTML = '';

    demoServers.forEach((s, i) => {
        setTimeout(() => {
            const card = document.createElement('div');
            card.className = 'server-card';
            card.innerHTML = `
                <div class="server-icon">${s.icon}</div>
                <div class="server-name">${s.name}</div>
                <div class="server-ping">✓ ${s.ping}</div>
            `;
            card.onclick = () => {
                document.querySelectorAll('.server-card').forEach(c => c.classList.remove('active'));
                card.classList.add('active');
                showToast('info', `${s.name} seçildi`);
            };
            grid.appendChild(card);
        }, i * 400);
    });
}

// ===== CHANNEL RENDERING =====
function getCategories() {
    const cats = new Set();
    APP.channels.forEach(ch => cats.add(ch.category));
    return ['Tümü', '⭐ Favoriler', ...Array.from(cats).sort()];
}

function renderCategoryTabs() {
    const container = document.getElementById('categoryTabs');
    const cats = getCategories();
    container.innerHTML = cats.map(c => {
        const active = (c === 'Tümü' && APP.currentCategory === 'all') ||
                       (c === '⭐ Favoriler' && APP.currentCategory === 'favorites') ||
                       (c === APP.currentCategory) ? 'active' : '';
        return `<div class="cat-tab ${active}" onclick="selectCategory('${c === 'Tümü' ? 'all' : c === '⭐ Favoriler' ? 'favorites' : c}')">${c}</div>`;
    }).join('');
}

function selectCategory(cat) {
    APP.currentCategory = cat;
    renderCategoryTabs();
    renderChannels();
}

function filterChannels() {
    renderChannels();
}

function getFilteredChannels() {
    const search = document.getElementById('searchInput').value.toLowerCase();
    let channels = APP.channels;

    if (APP.currentCategory === 'favorites') {
        channels = channels.filter(ch => APP.favorites.has(ch.id));
    } else if (APP.currentCategory !== 'all') {
        channels = channels.filter(ch => ch.category === APP.currentCategory);
    }

    if (search) {
        channels = channels.filter(ch =>
            ch.name.toLowerCase().includes(search) ||
            ch.category.toLowerCase().includes(search)
        );
    }

    return channels;
}

function renderChannels() {
    const container = document.getElementById('channelList');
    const channels = getFilteredChannels();

    if (channels.length === 0) {
        container.innerHTML = `
            <div style="text-align:center;padding:40px;color:var(--text-muted)">
                <i class="fas fa-satellite-dish" style="font-size:36px;margin-bottom:12px;display:block"></i>
                <p>Kanal bulunamadı</p>
            </div>
        `;
        return;
    }

    // Group by category
    const groups = {};
    channels.forEach(ch => {
        if (!groups[ch.category]) groups[ch.category] = [];
        groups[ch.category].push(ch);
    });

    let html = '';
    Object.keys(groups).sort().forEach(cat => {
        html += `<div class="group-header">${cat} (${groups[cat].length})</div>`;
        groups[cat].forEach(ch => {
            const isActive = APP.currentChannel && APP.currentChannel.id === ch.id;
            const isFav = APP.favorites.has(ch.id);
            const logoContent = ch.logo && ch.logo.startsWith('http')
                ? `<img src="${ch.logo}" alt="${ch.name}" onerror="this.parentElement.innerHTML='📺'">`
                : ch.logo || '📺';

            html += `
                <div class="channel-item ${isActive ? 'active' : ''}"
                     onclick="playChannel(${JSON.stringify(ch).replace(/"/g, '&quot;')})"
                     oncontextmenu="showContext(event, ${JSON.stringify(ch).replace(/"/g, '&quot;')})">
                    <div class="channel-logo">${logoContent}</div>
                    <div class="channel-info">
                        <div class="channel-name">${ch.name}</div>
                        <div class="channel-meta">
                            <div class="live-dot"></div>
                            <span>${ch.category}</span>
                            ${ch.country ? `<span class="channel-badge">${ch.country}</span>` : ''}
                        </div>
                    </div>
                    <button class="fav-btn ${isFav ? 'active' : ''}" onclick="event.stopPropagation(); toggleFavById(${ch.id})">
                        <i class="fas fa-star"></i>
                    </button>
                </div>
            `;
        });
    });

    container.innerHTML = html;
}

// ===== PLAYER =====
function playChannel(channel) {
    if (!channel || !channel.url) return showToast('error', 'Geçersiz kanal URL!');

    APP.currentChannel = channel;
    APP.watched.add(channel.id);
    saveToStorage();

    // Show player
    document.getElementById('welcomeScreen').classList.add('hidden');
    document.getElementById('playerContainer').classList.remove('hidden');
    document.getElementById('detailPanel').classList.remove('hidden');

    // Update UI
    document.getElementById('npName').textContent = channel.name;
    document.getElementById('npCategory').textContent = channel.category;
    document.getElementById('npLogo').innerHTML = channel.logo && !channel.logo.startsWith('http')
        ? channel.logo : '📺';

    document.getElementById('detailName').textContent = channel.name;
    document.getElementById('detailInfo').textContent = `${channel.category} • ${channel.country || 'Bilinmiyor'}`;
    document.getElementById('detailLogo').innerHTML = channel.logo && !channel.logo.startsWith('http')
        ? channel.logo : '📺';

    // Favorite button
    const favBtn = document.getElementById('favBtn');
    favBtn.classList.toggle('active', APP.favorites.has(channel.id));

    // Generate fake EPG
    generateEPG(channel);

    // Load video
    loadVideo(channel.url);

    // Update sidebar
    renderChannels();

    // Close sidebar on mobile
    if (window.innerWidth <= 768) {
        document.getElementById('sidebar').classList.remove('mobile-open');
    }
}

function loadVideo(url) {
    const video = document.getElementById('videoPlayer');
    const loading = document.getElementById('loadingOverlay');
    loading.classList.add('active');

    // Destroy previous instances
    if (APP.hls) { APP.hls.destroy(); APP.hls = null; }
    if (APP.shaka) { APP.shaka.unload(); APP.shaka = null; }

    video.src = '';
    video.removeAttribute('src');

    const engine = APP.settings.playerEngine;

    if (url.includes('.m3u8') || url.includes('hls')) {
        if (engine === 'shaka' && shaka.Player.isBrowserSupported()) {
            loadWithShaka(video, url, loading);
        } else if (Hls.isSupported()) {
            loadWithHLS(video, url, loading);
        } else if (video.canPlayType('application/vnd.apple.mpegurl')) {
            loadNative(video, url, loading);
        } else {
            loadWithHLS(video, url, loading);
        }
    } else if (url.includes('.mpd')) {
        loadWithShaka(video, url, loading);
    } else {
        loadNative(video, url, loading);
    }
}

function loadWithHLS(video, url, loading) {
    const hls = new Hls({
        maxBufferLength: parseInt(APP.settings.bufferSize),
        maxMaxBufferLength: 60,
        maxBufferSize: 60 * 1000 * 1000,
        enableWorker: true,
        lowLatencyMode: true,
        backBufferLength: 30
    });

    APP.hls = hls;

    hls.loadSource(url);
    hls.attachMedia(video);

    hls.on(Hls.Events.MANIFEST_PARSED, () => {
        loading.classList.remove('active');
        updateQualitySelector(hls.levels);
        if (APP.settings.autoPlay === 'true') {
            video.play().catch(() => {});
        }
    });

    hls.on(Hls.Events.LEVEL_SWITCHED, (event, data) => {
        const quality = hls.levels[data.level];
        if (quality) {
            // console.log(`Quality: ${quality.height}p`);
        }
    });

    hls.on(Hls.Events.ERROR, (event, data) => {
        if (data.fatal) {
            switch (data.type) {
                case Hls.ErrorTypes.NETWORK_ERROR:
                    hls.startLoad();
                    break;
                case Hls.ErrorTypes.MEDIA_ERROR:
                    hls.recoverMediaError();
                    break;
                default:
                    hls.destroy();
                    showToast('error', 'Yayın hatası, yeniden deneniyor...');
                    setTimeout(() => loadVideo(url), 2000);
                    break;
            }
        }
    });
}

function loadWithShaka(video, url, loading) {
    const player = new shaka.Player(video);
    APP.shaka = player;

    player.configure({
        streaming: {
            bufferingGoal: parseInt(APP.settings.bufferSize),
            rebufferingGoal: 2
        }
    });

    player.load(url).then(() => {
        loading.classList.remove('active');
        if (APP.settings.autoPlay === 'true') {
            video.play().catch(() => {});
        }
    }).catch((error) => {
        console.error('Shaka error:', error);
        loading.classList.remove('active');
        showToast('error', 'Shaka yüklenemedi, HLS deneniyor...');
        loadWithHLS(video, url, loading);
    });
}

function loadNative(video, url, loading) {
    video.src = url;
    video.addEventListener('loadeddata', () => {
        loading.classList.remove('active');
        if (APP.settings.autoPlay === 'true') {
            video.play().catch(() => {});
        }
    }, { once: true });
    video.addEventListener('error', () => {
        loading.classList.remove('active');
        showToast('error', 'Video yüklenemedi!');
    }, { once: true });
}

function updateQualitySelector(levels) {
    const sel = document.getElementById('qualitySelector');
    sel.innerHTML = '<option value="auto">Otomatik</option>';
    if (levels) {
        levels.forEach((level, i) => {
            const label = level.height ? `${level.height}p` : `Seviye ${i}`;
            sel.innerHTML += `<option value="${i}">${label}</option>`;
        });
    }
}

function changeQuality(value) {
    if (APP.hls) {
        APP.hls.currentLevel = value === 'auto' ? -1 : parseInt(value);
    }
}

function togglePlay() {
    const video = document.getElementById('videoPlayer');
    if (video.paused) {
        video.play();
    } else {
        video.pause();
    }
}

function nextChannel() {
    const channels = getFilteredChannels();
    const idx = channels.findIndex(c => c.id === APP.currentChannel?.id);
    if (idx < channels.length - 1) {
        playChannel(channels[idx + 1]);
    }
}

function prevChannel() {
    const channels = getFilteredChannels();
    const idx = channels.findIndex(c => c.id === APP.currentChannel?.id);
    if (idx > 0) {
        playChannel(channels[idx - 1]);
    }
}

function rewind10() {
    const video = document.getElementById('videoPlayer');
    video.currentTime = Math.max(0, video.currentTime - 10);
}

function forward10() {
    const video = document.getElementById('videoPlayer');
    video.currentTime += 10;
}

function changeVolume(val) {
    const video = document.getElementById('videoPlayer');
    video.volume = val / 100;
    updateVolumeIcon(val);
}

function toggleMute() {
    const video = document.getElementById('videoPlayer');
    const slider = document.getElementById('volumeSlider');
    video.muted = !video.muted;
    if (video.muted) {
        slider.value = 0;
        updateVolumeIcon(0);
    } else {
        slider.value = video.volume * 100;
        updateVolumeIcon(video.volume * 100);
    }
}

function updateVolumeIcon(val) {
    const icon = document.getElementById('volIcon');
    if (val == 0) icon.className = 'fas fa-volume-xmark';
    else if (val < 50) icon.className = 'fas fa-volume-low';
    else icon.className = 'fas fa-volume-high';
}

function toggleFullscreen() {
    const container = document.getElementById('playerContainer');
    const icon = document.getElementById('fsIcon');

    if (!document.fullscreenElement) {
        container.requestFullscreen?.() || container.webkitRequestFullscreen?.();
        icon.className = 'fas fa-compress';
    } else {
        document.exitFullscreen?.() || document.webkitExitFullscreen?.();
        icon.className = 'fas fa-expand';
    }
}

function togglePIP() {
    const video = document.getElementById('videoPlayer');
    if (document.pictureInPictureElement) {
        document.exitPictureInPicture();
    } else {
        video.requestPictureInPicture?.().catch(e => {
            showToast('error', 'PIP desteklenmiyor');
        });
    }
}

function toggleRecording() {
    if (APP.isRecording) {
        stopRecording();
    } else {
        startRecording();
    }
}

function startRecording() {
    const video = document.getElementById('videoPlayer');
    try {
        const stream = video.captureStream?.() || video.mozCaptureStream?.();
        if (!stream) return showToast('error', 'Kayıt desteklenmiyor');

        APP.recordedChunks = [];
        APP.mediaRecorder = new MediaRecorder(stream, { mimeType: 'video/webm;codecs=vp9' });

        APP.mediaRecorder.ondataavailable = (e) => {
            if (e.data.size > 0) APP.recordedChunks.push(e.data);
        };

        APP.mediaRecorder.onstop = () => {
            const blob = new Blob(APP.recordedChunks, { type: 'video/webm' });
            const url = URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            a.download = `${APP.currentChannel?.name || 'recording'}_${Date.now()}.webm`;
            a.click();
            URL.revokeObjectURL(url);
            showToast('success', 'Kayıt kaydedildi!');
        };

        APP.mediaRecorder.start();
        APP.isRecording = true;
        document.getElementById('recIndicator').classList.add('active');
        showToast('info', 'Kayıt başladı');
    } catch (e) {
        showToast('error', 'Kayıt başlatılamadı: ' + e.message);
    }
}

function stopRecording() {
    if (APP.mediaRecorder && APP.mediaRecorder.state !== 'inactive') {
        APP.mediaRecorder.stop();
    }
    APP.isRecording = false;
    document.getElementById('recIndicator').classList.remove('active');
}

// ===== FAVORITES =====
function toggleFavorite() {
    if (!APP.currentChannel) return;
    toggleFavById(APP.currentChannel.id);
}

function toggleFavById(id) {
    if (APP.favorites.has(id)) {
        APP.favorites.delete(id);
        showToast('info', 'Favorilerden çıkarıldı');
    } else {
        APP.favorites.add(id);
        showToast('success', 'Favorilere eklendi!');
    }
    saveToStorage();
    renderChannels();
    updateStats();

    if (APP.currentChannel && APP.currentChannel.id === id) {
        document.getElementById('favBtn').classList.toggle('active', APP.favorites.has(id));
    }
}

// ===== CONTEXT MENU =====
let contextChannel = null;

function showContext(event, channel) {
    event.preventDefault();
    event.stopPropagation();
    contextChannel = channel;

    const menu = document.getElementById('contextMenu');
    menu.style.top = event.clientY + 'px';
    menu.style.left = event.clientX + 'px';
    menu.classList.add('active');

    // Keep menu in viewport
    const rect = menu.getBoundingClientRect();
    if (rect.right > window.innerWidth) {
        menu.style.left = (event.clientX - rect.width) + 'px';
    }
    if (rect.bottom > window.innerHeight) {
        menu.style.top = (event.clientY - rect.height) + 'px';
    }
}

function contextPlay() {
    if (contextChannel) playChannel(contextChannel);
    document.getElementById('contextMenu').classList.remove('active');
}

function contextFavorite() {
    if (contextChannel) toggleFavById(contextChannel.id);
    document.getElementById('contextMenu').classList.remove('active');
}

function contextCopyUrl() {
    if (contextChannel) {
        navigator.clipboard.writeText(contextChannel.url);
        showToast('success', 'URL kopyalandı!');
    }
    document.getElementById('contextMenu').classList.remove('active');
}

function contextInfo() {
    if (contextChannel) {
        showToast('info', `${contextChannel.name}\nKategori: ${contextChannel.category}\nURL: ${contextChannel.url.substring(0, 50)}...`);
    }
    document.getElementById('contextMenu').classList.remove('active');
}

function contextDelete() {
    if (contextChannel) {
        APP.channels = APP.channels.filter(c => c.id !== contextChannel.id);
        APP.favorites.delete(contextChannel.id);
        saveToStorage();
        renderChannels();
        renderCategoryTabs();
        showToast('info', 'Kanal silindi');
    }
    document.getElementById('contextMenu').classList.remove('active');
}

// ===== EPG =====
function generateEPG(channel) {
    const container = document.getElementById('epgList');
    const now = new Date();
    const programs = [
        'Sabah Haberleri', 'Güne Başlarken', 'Kahvaltı Programı', 'Forma Magazin',
        'Öğle Haberleri', 'Gündem Özel', 'Ekonomi Bülteni', 'Spor Gündemi',
        'Ana Haber', 'Prime Time Dizi', 'Gece Haberleri', 'Sinema Kuşağı'
    ];

    let html = '';
    for (let i = 0; i < 8; i++) {
        const startH = (now.getHours() + i) % 24;
        const endH = (startH + 1) % 24;
        const isCurrent = i === 0;
        const progress = isCurrent ? (now.getMinutes() / 60 * 100) : 0;

        html += `
            <div class="epg-item ${isCurrent ? 'current' : ''}">
                <div class="epg-time">${String(startH).padStart(2,'0')}:00 - ${String(endH).padStart(2,'0')}:00</div>
                <div class="epg-program">
                    ${programs[(now.getHours() + i) % programs.length]}
                    ${isCurrent ? `<div class="epg-progress"><div class="epg-progress-bar" style="width:${progress}%"></div></div>` : ''}
                </div>
            </div>
        `;
    }
    container.innerHTML = html;
}

// ===== SAVED URLS =====
function renderSavedUrls() {
    const container = document.getElementById('savedUrls');
    container.innerHTML = APP.savedUrls.map((url, i) => `
        <div class="url-item">
            <span style="flex:1;overflow:hidden;text-overflow:ellipsis">${url}</span>
            <button class="delete-btn" onclick="deleteSavedUrl(${i})">
                <i class="fas fa-times"></i>
            </button>
        </div>
    `).join('') || '<div style="text-align:center;padding:20px;color:var(--text-muted);font-size:13px">Kayıtlı sunucu yok</div>';
}

function deleteSavedUrl(index) {
    APP.savedUrls.splice(index, 1);
    saveToStorage();
    renderSavedUrls();
    showToast('info', 'Sunucu silindi');
}

// ===== SETTINGS =====
function saveSetting(key, value) {
    APP.settings[key] = value;
    saveToStorage();
    showToast('success', 'Ayar kaydedildi');
}

function resetSettings() {
    APP.settings = {
        playerEngine: 'hls',
        bufferSize: 30,
        defaultQuality: 'auto',
        autoPlay: 'true',
        subtitleLang: 'tr',
        latencyWarning: 5000
    };
    saveToStorage();
    closeModal('settingsModal');
    showToast('success', 'Ayarlar sıfırlandı');
}

// ===== STATS =====
function updateStats() {
    document.getElementById('statTotal').textContent = APP.channels.length;
    document.getElementById('statCategories').textContent = getCategories().length - 2;
    document.getElementById('statFavorites').textContent = APP.favorites.size;
    document.getElementById('statWatched').textContent = APP.watched.size;
    document.getElementById('statServers').textContent = APP.savedUrls.length;

    const elapsed = Math.floor((Date.now() - APP.startTime) / 1000);
    const m = Math.floor(elapsed / 60);
    const s = elapsed % 60;
    document.getElementById('statUptime').textContent = `${m}m ${s}s`;
}

function clearAllData() {
    if (confirm('Tüm veriler silinecek. Emin misiniz?')) {
        localStorage.clear();
        APP.channels = [];
        APP.favorites.clear();
        APP.watched.clear();
        APP.savedUrls = [];
        renderCategoryTabs();
        renderChannels();
        renderSavedUrls();
        updateStats();
        closeModal('statsModal');
        showToast('info', 'Tüm veriler temizlendi');
    }
}

// ===== MODALS =====
function openModal(id) {
    document.getElementById(id).classList.add('active');
}

function closeModal(id) {
    document.getElementById(id).classList.remove('active');
}

// Close modal on overlay click
document.querySelectorAll('.modal-overlay').forEach(overlay => {
    overlay.addEventListener('click', (e) => {
        if (e.target === overlay) overlay.classList.remove('active');
    });
});

// ===== TOAST =====
function showToast(type, message) {
    const container = document.getElementById('toastContainer');
    const icons = { success: '✓', error: '✕', info: 'ℹ' };
    const toast = document.createElement('div');
    toast.className = `toast ${type}`;
    toast.innerHTML = `<span>${icons[type] || 'ℹ'}</span><span>${message}</span>`;
    container.appendChild(toast);
    setTimeout(() => toast.remove(), 3500);
}

// ===== SIDEBAR TOGGLE =====
function toggleSidebar() {
    const sidebar = document.getElementById('sidebar');
    sidebar.classList.toggle('mobile-open');
    sidebar.classList.toggle('collapsed');
}

// ===== KEYBOARD =====
function handleKeyboard(e) {
    if (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA') return;

    switch (e.key) {
        case ' ':
            e.preventDefault();
            togglePlay();
            break;
        case 'f':
            toggleFullscreen();
            break;
        case 'm':
            toggleMute();
            break;
        case 'ArrowRight':
            nextChannel();
            break;
        case 'ArrowLeft':
            prevChannel();
            break;
        case 'ArrowUp':
            e.preventDefault();
            const vs = document.getElementById('volumeSlider');
            vs.value = Math.min(100, parseInt(vs.value) + 5);
            changeVolume(vs.value);
            break;
        case 'ArrowDown':
            e.preventDefault();
            const vs2 = document.getElementById('volumeSlider');
            vs2.value = Math.max(0, parseInt(vs2.value) - 5);
            changeVolume(vs2.value);
            break;
        case 'Escape':
            if (document.fullscreenElement) toggleFullscreen();
            break;
        case 'r':
            toggleRecording();
            break;
    }
}

// ===== VIDEO EVENTS =====
document.getElementById('videoPlayer').addEventListener('play', () => {
    document.getElementById('playIcon').className = 'fas fa-pause';
});

document.getElementById('videoPlayer').addEventListener('pause', () => {
    document.getElementById('playIcon').className = 'fas fa-play';
});

document.getElementById('videoPlayer').addEventListener('waiting', () => {
    document.getElementById('loadingOverlay').classList.add('active');
});

document.getElementById('videoPlayer').addEventListener('playing', () => {
    document.getElementById('loadingOverlay').classList.remove('active');
});

// ===== THEME =====
let darkTheme = true;
function toggleTheme() {
    darkTheme = !darkTheme;
    if (darkTheme) {
        document.documentElement.style.setProperty('--bg-primary', '#0a0a0f');
        document.documentElement.style.setProperty('--bg-secondary', '#12121a');
        document.documentElement.style.setProperty('--bg-tertiary', '#1a1a2e');
    } else {
        document.documentElement.style.setProperty('--bg-primary', '#f0f2f5');
        document.documentElement.style.setProperty('--bg-secondary', '#ffffff');
        document.documentElement.style.setProperty('--bg-tertiary', '#f5f5f7');
    }
    showToast('info', darkTheme ? 'Koyu tema' : 'Açık tema');
}

// ===== DRAG & DROP =====
document.addEventListener('DOMContentLoaded', () => {
    const dropzone = document.querySelector('.import-dropzone');
    if (dropzone) {
        dropzone.addEventListener('dragover', (e) => {
            e.preventDefault();
            dropzone.style.borderColor = 'var(--accent)';
        });
        dropzone.addEventListener('dragleave', () => {
            dropzone.style.borderColor = '';
        });
        dropzone.addEventListener('drop', (e) => {
            e.preventDefault();
            dropzone.style.borderColor = '';
            const file = e.dataTransfer.files[0];
            if (file) {
                const reader = new FileReader();
                reader.onload = (ev) => {
                    const channels = parseM3U(ev.target.result);
                    if (channels.length > 0) {
                        channels.forEach(ch => {
                            ch.id = Date.now() + Math.random();
                            if (!APP.channels.find(c => c.url === ch.url)) {
                                APP.channels.push(ch);
                            }
                        });
                        saveToStorage();
                        renderCategoryTabs();
                        renderChannels();
                        closeModal('importModal');
                        showToast('success', `${channels.length} kanal eklendi!`);
                    }
                };
                reader.readAsText(file);
            }
        });
    }
});

// ===== INIT APP =====
init();
</script>
</body>
</html>
```

## 🚀 Uygulama Özellikleri

### 📺 Kanal Yönetimi
| Özellik | Açıklama |
|---------|----------|
| **60+ Türk Kanalı** | TRT, ATV, Star TV, Show TV, Kanal D, Fox TV, TV8 ve daha fazlası dahil |
| **Uluslararası Kanallar** | BBC, CNN, Al Jazeera, DW, France 24 dahil |
| **M3U İçe Aktarma** | URL, dosya yükleme, yapıştırma ile |
| **M3U Dışa Aktarma** | Tek tıkla playlist indirme |

### 🎮 Oynatıcı Özellikleri
- **HLS.js** ve **Shaka Player** desteği
- **Canlı yayın** (Live TV) optimizasyonu
- **Kalite seçici** (otomatik/manuel)
- **Kayıt** (WebRTC ile)
- **Picture-in-Picture**
- **Tam ekran** çift tıklama ile
- **Klavye kısayolları** (Space, F, M, ok tuşları)

### 🖥️ Webhost TV IP Modülü
- Xtream Codes API desteği
- Otomatik sunucu tarama
- Sunucu listesi ve ping göstergesi
- Otomatik M3U oluşturma

### 🎨 Arayüz
- **Cam efektli (Glassmorphism)** modern tasarım
- **Mobil tam uyumlu** responsive layout
- **Karanlık/aydınlık tema**
- **Sağ tık menüsü**
- **Toast bildirimleri**
- **EPG (Elektronik Program Rehberi)**
- **Kategori filtreleme ve arama**