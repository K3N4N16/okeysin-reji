<think>
The user wants me to integrate a real API from radyocast.com into the radio player, and continue developing it with new features. The API provides:
- Now Playing Song Title
- Album Image URL
- Online Listeners
- Unique Listeners
- Bitrate
- DJ Username
- DJ Profile Picture
- Last played 5 songs

Let me create a comprehensive, fully functional radio player that fetches data from this API and displays it beautifully. I'll use JavaScript fetch instead of PHP since this is a client-side application.

Let me build a complete, enhanced radio player with:


I need to make the API calls work from the frontend, but since this is a cross-origin request, I'll need to set up either a PHP proxy or use CORS-friendly endpoints. I'll create a proxy approach where the backend fetches from the Radyocast API and returns the data to the frontend. I'm going to put together a complete PHP backend with a proxy endpoint and a beautifully designed HTML radio player that dynamically pulls real-time data from the API.
</think># 🎵 Galactic Wave Radio - Tam Entegre Sürüm

İşte API entegrasyonlu, gerçek veriyle çalışan tam sürüm:

## 📁 Dosya Yapısı

```
📁 radyo/
├── 📄 index.html          ← Ana sayfa
├── 📄 api.php             ← API Proxy
├── 📄 script.js           ← JavaScript
└── 📄 style.css           ← Stiller (opsiyonel)
```

---

## 📄 api.php - API Proxy

```php
<?php
// ═══════════════════════════════════════════════
// GALACTIC WAVE RADIO - API PROXY
// ═══════════════════════════════════════════════

header('Content-Type: application/json; charset=utf-8');
header('Access-Control-Allow-Origin: *');
header('Cache-Control: no-cache, no-store, must-revalidate');

// API Anahtarı ve Ayarlar
define('STATION_ID', '8028');
define('API_URL', 'https://radyocast.com/cp/get_info.php?p=' . STATION_ID);

// Akış URL'si (kendi stream URL'nizi buraya yazın)
define('STREAM_URL', 'https://stream.radyocast.com/' . STATION_ID);

// CORS Preflight
if ($_SERVER['REQUEST_METHOD'] === 'OPTIONS') {
    http_response_code(200);
    exit;
}

$action = isset($_GET['action']) ? $_GET['action'] : 'info';

switch ($action) {

    case 'info':
        fetchStationInfo();
        break;

    case 'stream':
        getStreamUrl();
        break;

    case 'history':
        getPlayHistory();
        break;

    default:
        fetchStationInfo();
        break;
}

// ═══════════════════════════════════════════════
// İSTASYON BİLGİLERİNİ GETİR
// ═══════════════════════════════════════════════
function fetchStationInfo() {
    try {
        $ch = curl_init();
        curl_setopt_array($ch, [
            CURLOPT_URL            => API_URL,
            CURLOPT_POST           => false,
            CURLOPT_RETURNTRANSFER => true,
            CURLOPT_TIMEOUT        => 15,
            CURLOPT_CONNECTTIMEOUT => 10,
            CURLOPT_SSL_VERIFYHOST => false,
            CURLOPT_SSL_VERIFYPEER => false,
            CURLOPT_FOLLOWLOCATION => true,
            CURLOPT_HTTPHEADER     => [
                'User-Agent: GalacticWaveRadio/2.0',
                'Accept: application/json'
            ]
        ]);

        $response = curl_exec($ch);
        $httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
        $error    = curl_error($ch);
        curl_close($ch);

        // Hata kontrolü
        if ($error) {
            sendError('Bağlantı hatası: ' . $error, 503);
            return;
        }

        if ($httpCode !== 200) {
            sendError('API hatası: HTTP ' . $httpCode, 502);
            return;
        }

        // JSON parse
        $data = json_decode($response, true);

        if (json_last_error() !== JSON_ERROR_NONE) {
            // Objeyi dene
            $data = json_decode($response);
            if (!$data) {
                sendError('JSON parse hatası', 500);
                return;
            }
            $data = (array) $data;
        }

        // Veriyi temizle ve düzenle
        $result = [
            'status'   => 'success',
            'timestamp' => date('c'),
            'station'  => [
                'name'     => 'Galactic Wave Radio',
                'id'       => STATION_ID,
                'stream'   => STREAM_URL
            ],
            'now_playing' => [
                'title'   => sanitize($data['title'] ?? 'Bilinmiyor'),
                'art'     => sanitize($data['art'] ?? ''),
                'bitrate' => sanitize($data['bitrate'] ?? '128')
            ],
            'listeners' => [
                'online' => intval($data['listeners'] ?? 0),
                'unique' => intval($data['ulistener'] ?? 0)
            ],
            'dj' => [
                'username' => sanitize($data['djusername'] ?? ''),
                'profile'  => sanitize($data['djprofile'] ?? ''),
                'is_live'  => !empty($data['djusername'])
            ],
            'history' => parseHistory($data['history'] ?? [])
        ];

        echo json_encode($result, JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT);

    } catch (Exception $e) {
        sendError('Sunucu hatası: ' . $e->getMessage(), 500);
    }
}

// ═══════════════════════════════════════════════
// AKIŞ URL'SİNİ GETİR
// ═══════════════════════════════════════════════
function getStreamUrl() {
    echo json_encode([
        'status' => 'success',
        'url'    => STREAM_URL,
        'format' => 'mp3',
        'type'   => 'audio/mpeg'
    ]);
}

// ═══════════════════════════════════════════════
// ÇALMA GEÇMİŞİNİ GETİR
// ═══════════════════════════════════════════════
function getPlayHistory() {
    try {
        $ch = curl_init();
        curl_setopt_array($ch, [
            CURLOPT_URL            => API_URL,
            CURLOPT_RETURNTRANSFER => true,
            CURLOPT_TIMEOUT        => 15,
            CURLOPT_SSL_VERIFYHOST => false,
            CURLOPT_SSL_VERIFYPEER => false
        ]);

        $response = curl_exec($ch);
        curl_close($ch);

        $data = json_decode($response, true);
        if (!$data) {
            $data = (array) json_decode($response);
        }

        $history = parseHistory($data['history'] ?? []);

        echo json_encode([
            'status'  => 'success',
            'history' => $history,
            'count'   => count($history)
        ], JSON_UNESCAPED_UNICODE);

    } catch (Exception $e) {
        sendError('Geçmiş alınamadı', 500);
    }
}

// ═══════════════════════════════════════════════
// YARDIMCI FONKSİYONLAR
// ═══════════════════════════════════════════════
function sanitize($input) {
    if (is_array($input)) {
        return array_map('sanitize', $input);
    }
    return htmlspecialchars(trim($input), ENT_QUOTES, 'UTF-8');
}

function parseHistory($history) {
    $parsed = [];

    if (is_array($history)) {
        foreach ($history as $index => $track) {
            if (is_string($track)) {
                $parsed[] = [
                    'id'    => $index + 1,
                    'title' => sanitize($track),
                    'time'  => date('H:i', strtotime("-{$index} minutes"))
                ];
            } elseif (is_object($track) || is_array($track)) {
                $track = (array) $track;
                $parsed[] = [
                    'id'    => $index + 1,
                    'title' => sanitize($track['title'] ?? $track['name'] ?? 'Bilinmiyor'),
                    'artist'=> sanitize($track['artist'] ?? ''),
                    'art'   => sanitize($track['art'] ?? ''),
                    'time'  => sanitize($track['time'] ?? date('H:i'))
                ];
            }
        }
    }

    return $parsed;
}

function sendError($message, $code = 400) {
    http_response_code($code);
    echo json_encode([
        'status'  => 'error',
        'message' => $message,
        'code'    => $code,
        'timestamp' => date('c')
    ], JSON_UNESCAPED_UNICODE);
}
?>
```

---

## 📄 index.html - Ana Sayfa

```html
<!DOCTYPE html>
<html lang="tr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>🌌 Galactic Wave Radio</title>

  <!-- Font Awesome -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">

  <!-- Google Fonts -->
  <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;500;600;700;800;900&family=Rajdhani:wght@300;400;500;600;700&family=Space+Grotesk:wght@300;400;500;600;700&display=swap" rel="stylesheet">

  <style>
    /* ═══════════════════════════════════════════════
       CSS VARIABLES - GALAKTİK TEMA
    ═══════════════════════════════════════════════ */
    :root {
      --bg-deep:      #020010;
      --bg-dark:      #050520;
      --bg-card:      rgba(8, 8, 40, 0.85);
      --bg-glass:     rgba(15, 15, 60, 0.45);

      --primary:      #00e0ff;
      --secondary:    #c760ff;
      --accent:       #ff6b9d;
      --energy:       #ffe04b;
      --success:      #00ff88;
      --danger:       #ff4466;

      --glow-pri:     rgba(0, 224, 255, 0.35);
      --glow-sec:     rgba(199, 96, 255, 0.35);
      --glow-acc:     rgba(255, 107, 157, 0.35);

      --text:         #e0e0ff;
      --text-dim:     #7070a0;
      --text-bright:  #ffffff;

      --radius:       16px;
      --radius-sm:    10px;
      --radius-xs:    6px;

      --font-display: 'Orbitron', monospace;
      --font-body:    'Space Grotesk', sans-serif;
      --font-ui:      'Rajdhani', sans-serif;
    }

    /* ═══════════════════════════════════════════════
       RESET & BASE
    ═══════════════════════════════════════════════ */
    *, *::before, *::after {
      margin: 0; padding: 0; box-sizing: border-box;
    }

    html {
      scroll-behavior: smooth;
      overflow-x: hidden;
    }

    body {
      font-family: var(--font-body);
      background: var(--bg-deep);
      color: var(--text);
      min-height: 100vh;
      overflow-x: hidden;
      position: relative;
    }

    /* ═══════════════════════════════════════════════
       SCROLLBAR
    ═══════════════════════════════════════════════ */
    ::-webkit-scrollbar { width: 6px; }
    ::-webkit-scrollbar-track { background: var(--bg-deep); }
    ::-webkit-scrollbar-thumb {
      background: linear-gradient(180deg, var(--primary), var(--secondary));
      border-radius: 3px;
    }

    /* ═══════════════════════════════════════════════
       ANIMATED BACKGROUND
    ═══════════════════════════════════════════════ */
    .cosmic-bg {
      position: fixed;
      inset: 0;
      z-index: 0;
      overflow: hidden;
    }

    .cosmic-bg .nebula {
      position: absolute;
      border-radius: 50%;
      filter: blur(100px);
      opacity: 0.15;
      animation: nebula-drift 25s ease-in-out infinite alternate;
    }

    .cosmic-bg .nebula:nth-child(1) {
      width: 600px; height: 600px;
      background: var(--primary);
      top: -10%; left: -10%;
    }

    .cosmic-bg .nebula:nth-child(2) {
      width: 500px; height: 500px;
      background: var(--secondary);
      bottom: -10%; right: -10%;
      animation-delay: -8s;
      animation-direction: alternate-reverse;
    }

    .cosmic-bg .nebula:nth-child(3) {
      width: 400px; height: 400px;
      background: var(--accent);
      top: 40%; left: 50%;
      animation-delay: -15s;
    }

    .cosmic-bg .nebula:nth-child(4) {
      width: 350px; height: 350px;
      background: var(--energy);
      top: 20%; right: 20%;
      opacity: 0.08;
      animation-delay: -20s;
    }

    @keyframes nebula-drift {
      0%   { transform: translate(0, 0) scale(1); }
      33%  { transform: translate(60px, -40px) scale(1.15); }
      66%  { transform: translate(-30px, 50px) scale(0.9); }
      100% { transform: translate(20px, -20px) scale(1.05); }
    }

    /* Stars */
    .star-field {
      position: fixed;
      inset: 0;
      z-index: 0;
    }

    .star {
      position: absolute;
      background: white;
      border-radius: 50%;
      animation: twinkle var(--dur, 3s) ease-in-out infinite var(--delay, 0s);
    }

    @keyframes twinkle {
      0%, 100% { opacity: 0.2; transform: scale(0.8); }
      50%      { opacity: 1;   transform: scale(1.2); }
    }

    /* ═══════════════════════════════════════════════
       MAIN LAYOUT
    ═══════════════════════════════════════════════ */
    .app-container {
      position: relative;
      z-index: 1;
      max-width: 1400px;
      margin: 0 auto;
      padding: 15px;
      padding-bottom: 80px;
    }

    /* ═══════════════════════════════════════════════
       HEADER
    ═══════════════════════════════════════════════ */
    .header {
      text-align: center;
      padding: 20px 0 15px;
      position: relative;
    }

    .header h1 {
      font-family: var(--font-display);
      font-size: clamp(1.6rem, 4vw, 2.6rem);
      font-weight: 800;
      background: linear-gradient(135deg, var(--primary), var(--secondary), var(--accent));
      background-size: 200% 200%;
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      background-clip: text;
      animation: gradient-shift 4s ease infinite;
      letter-spacing: 3px;
      text-transform: uppercase;
    }

    .header .subtitle {
      font-family: var(--font-ui);
      font-size: 1rem;
      color: var(--text-dim);
      letter-spacing: 6px;
      text-transform: uppercase;
      margin-top: 5px;
    }

    @keyframes gradient-shift {
      0%, 100% { background-position: 0% 50%; }
      50%      { background-position: 100% 50%; }
    }

    /* Status Bar */
    .status-bar {
      display: flex;
      justify-content: center;
      gap: 25px;
      margin-top: 12px;
      flex-wrap: wrap;
    }

    .status-item {
      display: flex;
      align-items: center;
      gap: 8px;
      font-family: var(--font-ui);
      font-size: 0.85rem;
      color: var(--text-dim);
      padding: 6px 14px;
      background: var(--bg-glass);
      border-radius: 20px;
      border: 1px solid rgba(255,255,255,0.06);
    }

    .status-item i {
      color: var(--primary);
      font-size: 0.75rem;
    }

    .status-item.live i {
      color: var(--success);
      animation: pulse-dot 1.5s infinite;
    }

    .status-item.dj-live i {
      color: var(--accent);
    }

    @keyframes pulse-dot {
      0%, 100% { opacity: 1; }
      50%      { opacity: 0.3; }
    }

    .status-item strong {
      color: var(--text);
      font-weight: 600;
    }

    /* ═══════════════════════════════════════════════
       GRID LAYOUT
    ═══════════════════════════════════════════════ */
    .main-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 20px;
      margin-top: 20px;
    }

    @media (max-width: 900px) {
      .main-grid {
        grid-template-columns: 1fr;
      }
    }

    /* ═══════════════════════════════════════════════
       CARD BASE
    ═══════════════════════════════════════════════ */
    .card {
      background: var(--bg-card);
      border: 1px solid rgba(255, 255, 255, 0.06);
      border-radius: var(--radius);
      padding: 25px;
      backdrop-filter: blur(20px);
      transition: border-color 0.3s, box-shadow 0.3s;
    }

    .card:hover {
      border-color: rgba(0, 224, 255, 0.15);
      box-shadow: 0 0 30px rgba(0, 224, 255, 0.05);
    }

    .card-header {
      display: flex;
      align-items: center;
      gap: 10px;
      margin-bottom: 20px;
    }

    .card-header i {
      font-size: 1.1rem;
      color: var(--primary);
    }

    .card-header h3 {
      font-family: var(--font-display);
      font-size: 0.85rem;
      letter-spacing: 2px;
      text-transform: uppercase;
      color: var(--text);
    }

    .card-header .badge {
      margin-left: auto;
      padding: 3px 12px;
      border-radius: 12px;
      font-family: var(--font-ui);
      font-size: 0.7rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 1px;
    }

    .badge-live {
      background: rgba(0, 255, 136, 0.12);
      color: var(--success);
      border: 1px solid rgba(0, 255, 136, 0.25);
      animation: badge-pulse 2s infinite;
    }

    @keyframes badge-pulse {
      0%, 100% { box-shadow: 0 0 0 0 rgba(0, 255, 136, 0.3); }
      50%      { box-shadow: 0 0 12px 3px rgba(0, 255, 136, 0.15); }
    }

    .badge-dj {
      background: rgba(255, 107, 157, 0.12);
      color: var(--accent);
      border: 1px solid rgba(255, 107, 157, 0.25);
    }

    /* ═══════════════════════════════════════════════
       PLAYER CARD
    ═══════════════════════════════════════════════ */
    .player-card {
      grid-column: 1 / -1;
    }

    .player-layout {
      display: grid;
      grid-template-columns: 280px 1fr;
      gap: 30px;
      align-items: start;
    }

    @media (max-width: 700px) {
      .player-layout {
        grid-template-columns: 1fr;
      }
    }

    /* Album Art */
    .album-section {
      position: relative;
    }

    .album-art-wrapper {
      position: relative;
      width: 100%;
      aspect-ratio: 1;
      border-radius: var(--radius);
      overflow: hidden;
      cursor: pointer;
      group: album;
    }

    .album-art {
      width: 100%;
      height: 100%;
      object-fit: cover;
      transition: transform 0.5s ease;
    }

    .album-art-wrapper:hover .album-art {
      transform: scale(1.05);
    }

    .album-overlay {
      position: absolute;
      inset: 0;
      background: linear-gradient(
        180deg,
        transparent 30%,
        rgba(0, 0, 0, 0.7) 100%
      );
      display: flex;
      align-items: center;
      justify-content: center;
      opacity: 0;
      transition: opacity 0.3s;
    }

    .album-art-wrapper:hover .album-overlay {
      opacity: 1;
    }

    .album-play-btn {
      width: 60px;
      height: 60px;
      border-radius: 50%;
      background: rgba(0, 224, 255, 0.9);
      border: none;
      color: var(--bg-deep);
      font-size: 1.4rem;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      transition: transform 0.2s, box-shadow 0.2s;
    }

    .album-play-btn:hover {
      transform: scale(1.1);
      box-shadow: 0 0 30px var(--glow-pri);
    }

    /* Playing indicator on album */
    .album-playing-bars {
      position: absolute;
      bottom: 12px;
      left: 12px;
      display: flex;
      gap: 3px;
      align-items: flex-end;
      height: 20px;
    }

    .album-playing-bars span {
      width: 4px;
      background: var(--primary);
      border-radius: 2px;
      animation: album-bar 0.6s ease-in-out infinite;
    }

    .album-playing-bars span:nth-child(1) { height: 8px;  animation-delay: 0s; }
    .album-playing-bars span:nth-child(2) { height: 16px; animation-delay: 0.1s; }
    .album-playing-bars span:nth-child(3) { height: 10px; animation-delay: 0.2s; }
    .album-playing-bars span:nth-child(4) { height: 18px; animation-delay: 0.3s; }

    @keyframes album-bar {
      0%, 100% { transform: scaleY(0.4); }
      50%      { transform: scaleY(1); }
    }

    /* Bitrate badge */
    .bitrate-badge {
      position: absolute;
      top: 10px;
      right: 10px;
      padding: 4px 10px;
      background: rgba(0, 0, 0, 0.7);
      border: 1px solid var(--primary);
      border-radius: 12px;
      font-family: var(--font-display);
      font-size: 0.65rem;
      color: var(--primary);
      letter-spacing: 1px;
    }

    /* Song Info */
    .song-info-section {
      display: flex;
      flex-direction: column;
      gap: 20px;
    }

    .now-playing-info {
      display: flex;
      flex-direction: column;
      gap: 6px;
    }

    .now-playing-label {
      font-family: var(--font-ui);
      font-size: 0.75rem;
      color: var(--primary);
      letter-spacing: 3px;
      text-transform: uppercase;
    }

    .song-title {
      font-family: var(--font-display);
      font-size: clamp(1.1rem, 2.5vw, 1.6rem);
      font-weight: 700;
      color: var(--text-bright);
      line-height: 1.3;
      min-height: 2.6em;
    }

    .song-title.ticker {
      overflow: hidden;
      position: relative;
    }

    .song-title.ticker span {
      display: inline-block;
      animation: title-scroll 8s linear infinite;
      white-space: nowrap;
    }

    @keyframes title-scroll {
      0%   { transform: translateX(0); }
      40%  { transform: translateX(0); }
      60%  { transform: translateX(-50%); }
      100% { transform: translateX(-50%); }
    }

    .song-artist {
      font-family: var(--font-body);
      font-size: 1rem;
      color: var(--text-dim);
    }

    /* DJ Section */
    .dj-section {
      display: flex;
      align-items: center;
      gap: 14px;
      padding: 14px 18px;
      background: linear-gradient(135deg, rgba(255, 107, 157, 0.08), rgba(199, 96, 255, 0.08));
      border: 1px solid rgba(255, 107, 157, 0.15);
      border-radius: var(--radius-sm);
    }

    .dj-avatar {
      width: 48px;
      height: 48px;
      border-radius: 50%;
      object-fit: cover;
      border: 2px solid var(--accent);
      flex-shrink: 0;
    }

    .dj-avatar-placeholder {
      width: 48px;
      height: 48px;
      border-radius: 50%;
      background: linear-gradient(135deg, var(--accent), var(--secondary));
      display: flex;
      align-items: center;
      justify-content: center;
      color: white;
      font-size: 1.2rem;
      flex-shrink: 0;
    }

    .dj-info {
      flex: 1;
    }

    .dj-label {
      font-family: var(--font-ui);
      font-size: 0.7rem;
      color: var(--accent);
      letter-spacing: 2px;
      text-transform: uppercase;
    }

    .dj-name {
      font-family: var(--font-display);
      font-size: 0.95rem;
      font-weight: 600;
      color: var(--text-bright);
    }

    .dj-live-indicator {
      display: flex;
      align-items: center;
      gap: 6px;
      padding: 4px 12px;
      background: rgba(0, 255, 136, 0.1);
      border: 1px solid rgba(0, 255, 136, 0.25);
      border-radius: 20px;
      font-family: var(--font-ui);
      font-size: 0.7rem;
      color: var(--success);
      font-weight: 700;
      letter-spacing: 1px;
    }

    .dj-live-indicator .dot {
      width: 6px;
      height: 6px;
      background: var(--success);
      border-radius: 50%;
      animation: pulse-dot 1s infinite;
    }

    /* Progress Bar */
    .progress-section {
      width: 100%;
    }

    .progress-bar {
      width: 100%;
      height: 5px;
      background: rgba(255, 255, 255, 0.08);
      border-radius: 3px;
      cursor: pointer;
      position: relative;
      overflow: hidden;
    }

    .progress-fill {
      height: 100%;
      background: linear-gradient(90deg, var(--primary), var(--secondary));
      border-radius: 3px;
      width: 0%;
      transition: width 0.3s;
      position: relative;
    }

    .progress-fill::after {
      content: '';
      position: absolute;
      right: 0;
      top: 50%;
      transform: translateY(-50%);
      width: 14px;
      height: 14px;
      background: var(--primary);
      border-radius: 50%;
      box-shadow: 0 0 10px var(--glow-pri);
      opacity: 0;
      transition: opacity 0.2s;
    }

    .progress-bar:hover .progress-fill::after {
      opacity: 1;
    }

    .progress-time {
      display: flex;
      justify-content: space-between;
      margin-top: 6px;
      font-family: var(--font-ui);
      font-size: 0.75rem;
      color: var(--text-dim);
    }

    /* Controls */
    .controls-section {
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 18px;
      flex-wrap: wrap;
    }

    .ctrl-btn {
      width: 48px;
      height: 48px;
      border-radius: 50%;
      border: 1px solid rgba(255, 255, 255, 0.1);
      background: var(--bg-glass);
      color: var(--text);
      font-size: 1rem;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      transition: all 0.25s;
    }

    .ctrl-btn:hover {
      border-color: var(--primary);
      color: var(--primary);
      background: rgba(0, 224, 255, 0.08);
      transform: scale(1.08);
    }

    .ctrl-btn.active {
      border-color: var(--primary);
      color: var(--primary);
      background: rgba(0, 224, 255, 0.15);
    }

    .ctrl-btn.main-play {
      width: 64px;
      height: 64px;
      font-size: 1.4rem;
      background: linear-gradient(135deg, var(--primary), var(--secondary));
      border: none;
      color: var(--bg-deep);
      box-shadow: 0 0 30px var(--glow-pri);
    }

    .ctrl-btn.main-play:hover {
      transform: scale(1.12);
      box-shadow: 0 0 50px var(--glow-pri);
      color: var(--bg-deep);
    }

    .ctrl-btn.main-play.is-playing {
      animation: play-glow 2s ease-in-out infinite;
    }

    @keyframes play-glow {
      0%, 100% { box-shadow: 0 0 20px var(--glow-pri); }
      50%      { box-shadow: 0 0 50px var(--glow-pri), 0 0 80px rgba(199, 96, 255, 0.2); }
    }

    /* Volume */
    .volume-section {
      display: flex;
      align-items: center;
      gap: 12px;
      margin-top: 15px;
      padding-top: 15px;
      border-top: 1px solid rgba(255, 255, 255, 0.04);
    }

    .volume-section i {
      color: var(--text-dim);
      font-size: 0.95rem;
      cursor: pointer;
      width: 20px;
      text-align: center;
      transition: color 0.2s;
    }

    .volume-section i:hover {
      color: var(--primary);
    }

    .volume-slider {
      flex: 1;
      -webkit-appearance: none;
      appearance: none;
      height: 4px;
      background: rgba(255, 255, 255, 0.1);
      border-radius: 2px;
      outline: none;
      cursor: pointer;
    }

    .volume-slider::-webkit-slider-thumb {
      -webkit-appearance: none;
      width: 16px;
      height: 16px;
      border-radius: 50%;
      background: var(--primary);
      cursor: pointer;
      box-shadow: 0 0 8px var(--glow-pri);
      transition: transform 0.15s;
    }

    .volume-slider::-webkit-slider-thumb:hover {
      transform: scale(1.3);
    }

    .volume-slider::-moz-range-thumb {
      width: 16px;
      height: 16px;
      border-radius: 50%;
      background: var(--primary);
      cursor: pointer;
      border: none;
    }

    .volume-val {
      font-family: var(--font-display);
      font-size: 0.75rem;
      color: var(--text-dim);
      min-width: 36px;
      text-align: right;
    }

    /* ═══════════════════════════════════════════════
       PLAYLIST CARD
    ═══════════════════════════════════════════════ */
    .playlist-card {
      max-height: 500px;
      display: flex;
      flex-direction: column;
    }

    .playlist-list {
      flex: 1;
      overflow-y: auto;
      display: flex;
      flex-direction: column;
      gap: 6px;
      padding-right: 5px;
    }

    .playlist-track {
      display: flex;
      align-items: center;
      gap: 12px;
      padding: 10px 14px;
      background: rgba(255, 255, 255, 0.02);
      border-radius: var(--radius-xs);
      cursor: pointer;
      transition: all 0.2s;
      border: 1px solid transparent;
    }

    .playlist-track:hover {
      background: rgba(0, 224, 255, 0.05);
      border-color: rgba(0, 224, 255, 0.1);
    }

    .playlist-track.current {
      background: rgba(0, 224, 255, 0.08);
      border-color: rgba(0, 224, 255, 0.2);
    }

    .track-number {
      font-family: var(--font-display);
      font-size: 0.7rem;
      color: var(--text-dim);
      min-width: 20px;
      text-align: center;
    }

    .playlist-track.current .track-number {
      color: var(--primary);
    }

    .track-art {
      width: 40px;
      height: 40px;
      border-radius: 6px;
      object-fit: cover;
      flex-shrink: 0;
    }

    .track-art-placeholder {
      width: 40px;
      height: 40px;
      border-radius: 6px;
      background: linear-gradient(135deg, rgba(0, 224, 255, 0.2), rgba(199, 96, 255, 0.2));
      display: flex;
      align-items: center;
      justify-content: center;
      color: var(--primary);
      font-size: 0.8rem;
      flex-shrink: 0;
    }

    .track-info {
      flex: 1;
      min-width: 0;
    }

    .track-title {
      font-family: var(--font-body);
      font-size: 0.85rem;
      color: var(--text);
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }

    .track-artist {
      font-family: var(--font-ui);
      font-size: 0.7rem;
      color: var(--text-dim);
    }

    .track-time {
      font-family: var(--font-ui);
      font-size: 0.7rem;
      color: var(--text-dim);
      flex-shrink: 0;
    }

    /* ═══════════════════════════════════════════════
       VISUALIZER CARD
    ═══════════════════════════════════════════════ */
    .visualizer-card .bars-container {
      display: flex;
      align-items: flex-end;
      justify-content: center;
      gap: 3px;
      height: 120px;
      padding: 15px 0;
    }

    .freq-bar {
      width: 6px;
      min-height: 4px;
      background: linear-gradient(180deg, var(--primary), var(--secondary));
      border-radius: 3px 3px 0 0;
      transition: height 0.15s ease;
    }

    .freq-bar.odd {
      background: linear-gradient(180deg, var(--secondary), var(--accent));
    }

    /* EQ Section */
    .eq-section {
      margin-top: 20px;
    }

    .eq-modes {
      display: flex;
      gap: 8px;
      margin-bottom: 15px;
      flex-wrap: wrap;
    }

    .eq-mode-btn {
      padding: 6px 16px;
      border: 1px solid rgba(255, 255, 255, 0.08);
      background: rgba(255, 255, 255, 0.03);
      color: var(--text-dim);
      font-family: var(--font-ui);
      font-size: 0.75rem;
      border-radius: 20px;
      cursor: pointer;
      transition: all 0.2s;
      letter-spacing: 1px;
      text-transform: uppercase;
    }

    .eq-mode-btn:hover {
      border-color: var(--primary);
      color: var(--primary);
    }

    .eq-mode-btn.active {
      background: rgba(0, 224, 255, 0.12);
      border-color: var(--primary);
      color: var(--primary);
    }

    .eq-bands {
      display: flex;
      justify-content: space-between;
      gap: 8px;
    }

    .eq-band {
      flex: 1;
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 8px;
    }

    .eq-slider {
      -webkit-appearance: none;
      appearance: none;
      width: 4px;
      height: 80px;
      background: rgba(255, 255, 255, 0.1);
      border-radius: 2px;
      outline: none;
      writing-mode: vertical-lr;
      direction: rtl;
      cursor: pointer;
    }

    .eq-slider::-webkit-slider-thumb {
      -webkit-appearance: none;
      width: 14px;
      height: 14px;
      border-radius: 50%;
      background: var(--primary);
      cursor: pointer;
    }

    .eq-label {
      font-family: var(--font-ui);
      font-size: 0.65rem;
      color: var(--text-dim);
    }

    /* ═══════════════════════════════════════════════
       DJ CARD
    ═══════════════════════════════════════════════ */
    .dj-card {
      background: linear-gradient(135deg, 
        rgba(255, 107, 157, 0.06),
        rgba(199, 96, 255, 0.06)
      );
      border-color: rgba(255, 107, 157, 0.12);
    }

    .dj-profile-section {
      display: flex;
      align-items: center;
      gap: 18px;
      margin-bottom: 20px;
    }

    .dj-profile-avatar {
      width: 70px;
      height: 70px;
      border-radius: 50%;
      object-fit: cover;
      border: 3px solid var(--accent);
      box-shadow: 0 0 20px rgba(255, 107, 157, 0.3);
    }

    .dj-profile-placeholder {
      width: 70px;
      height: 70px;
      border-radius: 50%;
      background: linear-gradient(135deg, var(--accent), var(--secondary));
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1.8rem;
      color: white;
      border: 3px solid var(--accent);
      box-shadow: 0 0 20px rgba(255, 107, 157, 0.3);
    }

    .dj-profile-info h4 {
      font-family: var(--font-display);
      font-size: 1.1rem;
      color: var(--text-bright);
      font-weight: 600;
    }

    .dj-profile-info p {
      font-family: var(--font-ui);
      font-size: 0.8rem;
      color: var(--text-dim);
      margin-top: 4px;
    }

    .dj-stats {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 12px;
    }

    .dj-stat {
      text-align: center;
      padding: 14px 10px;
      background: rgba(255, 255, 255, 0.03);
      border-radius: var(--radius-xs);
      border: 1px solid rgba(255, 255, 255, 0.04);
    }

    .dj-stat .value {
      font-family: var(--font-display);
      font-size: 1.3rem;
      font-weight: 700;
      color: var(--primary);
    }

    .dj-stat .label {
      font-family: var(--font-ui);
      font-size: 0.7rem;
      color: var(--text-dim);
      margin-top: 4px;
      text-transform: uppercase;
      letter-spacing: 1px;
    }

    /* ═══════════════════════════════════════════════
       MESSAGE WALL
    ═══════════════════════════════════════════════ */
    .message-wall {
      max-height: 350px;
      display: flex;
      flex-direction: column;
    }

    .message-input-area {
      display: flex;
      gap: 10px;
      margin-bottom: 15px;
    }

    .message-input {
      flex: 1;
      padding: 10px 16px;
      background: rgba(255, 255, 255, 0.04);
      border: 1px solid rgba(255, 255, 255, 0.08);
      border-radius: var(--radius-xs);
      color: var(--text);
      font-family: var(--font-body);
      font-size: 0.85rem;
      outline: none;
      transition: border-color 0.2s;
    }

    .message-input::placeholder {
      color: var(--text-dim);
    }

    .message-input:focus {
      border-color: var(--primary);
    }

    .message-send-btn {
      padding: 10px 20px;
      background: linear-gradient(135deg, var(--primary), var(--secondary));
      border: none;
      border-radius: var(--radius-xs);
      color: var(--bg-deep);
      font-family: var(--font-display);
      font-size: 0.75rem;
      font-weight: 700;
      cursor: pointer;
      letter-spacing: 1px;
      transition: transform 0.2s, box-shadow 0.2s;
    }

    .message-send-btn:hover {
      transform: scale(1.05);
      box-shadow: 0 0 20px var(--glow-pri);
    }

    .message-list {
      flex: 1;
      overflow-y: auto;
      display: flex;
      flex-direction: column;
      gap: 10px;
    }

    .message-item {
      display: flex;
      gap: 10px;
      padding: 10px;
      background: rgba(255, 255, 255, 0.02);
      border-radius: var(--radius-xs);
    }

    .message-avatar {
      width: 32px;
      height: 32px;
      border-radius: 50%;
      background: linear-gradient(135deg, var(--primary), var(--secondary));
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 0.7rem;
      color: white;
      flex-shrink: 0;
    }

    .message-body {
      flex: 1;
    }

    .message-author {
      font-family: var(--font-ui);
      font-size: 0.75rem;
      color: var(--primary);
      font-weight: 600;
    }

    .message-text {
      font-size: 0.82rem;
      color: var(--text);
      margin-top: 3px;
      line-height: 1.4;
    }

    .message-time {
      font-family: var(--font-ui);
      font-size: 0.65rem;
      color: var(--text-dim);
      margin-top: 4px;
    }

    /* ═══════════════════════════════════════════════
       INFO GRID
    ═══════════════════════════════════════════════ */
    .info-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
      gap: 20px;
      margin-top: 20px;
    }

    /* ═══════════════════════════════════════════════
       BOTTOM TOOLBAR
    ═══════════════════════════════════════════════ */
    .bottom-toolbar {
      position: fixed;
      bottom: 0;
      left: 0;
      right: 0;
      z-index: 100;
      background: rgba(5, 5, 32, 0.92);
      backdrop-filter: blur(20px);
      border-top: 1px solid rgba(255, 255, 255, 0.06);
      padding: 8px 20px;
      display: flex;
      align-items: center;
      justify-content: space-between;
    }

    .toolbar-brand {
      font-family: var(--font-display);
      font-size: 0.7rem;
      color: var(--primary);
      letter-spacing: 2px;
    }

    .toolbar-nav {
      display: flex;
      gap: 6px;
    }

    .toolbar-btn {
      width: 42px;
      height: 42px;
      border-radius: 50%;
      border: 1px solid rgba(255, 255, 255, 0.08);
      background: rgba(255, 255, 255, 0.03);
      color: var(--text-dim);
      font-size: 0.9rem;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      transition: all 0.2s;
    }

    .toolbar-btn:hover {
      border-color: var(--primary);
      color: var(--primary);
      background: rgba(0, 224, 255, 0.08);
    }

    .toolbar-btn.active {
      color: var(--primary);
      border-color: var(--primary);
    }

    /* ═══════════════════════════════════════════════
       TOAST NOTIFICATION
    ═══════════════════════════════════════════════ */
    .toast {
      position: fixed;
      bottom: 80px;
      left: 50%;
      transform: translateX(-50%) translateY(30px);
      padding: 12px 24px;
      background: rgba(0, 224, 255, 0.12);
      border: 1px solid rgba(0, 224, 255, 0.25);
      backdrop-filter: blur(20px);
      border-radius: 30px;
      font-family: var(--font-ui);
      font-size: 0.82rem;
      color: var(--primary);
      z-index: 200;
      opacity: 0;
      pointer-events: none;
      transition: all 0.35s cubic-bezier(0.4, 0, 0.2, 1);
      white-space: nowrap;
    }

    .toast.show {
      opacity: 1;
      transform: translateX(-50%) translateY(0);
    }

    /* ═══════════════════════════════════════════════
       LOADING
    ═══════════════════════════════════════════════ */
    .loading-skeleton {
      background: linear-gradient(90deg, 
        rgba(255,255,255,0.03) 25%,
        rgba(255,255,255,0.06) 50%,
        rgba(255,255,255,0.03) 75%
      );
      background-size: 200% 100%;
      animation: skeleton-shimmer 1.5s infinite;
      border-radius: 6px;
    }

    @keyframes skeleton-shimmer {
      0%   { background-position: 200% 0; }
      100% { background-position: -200% 0; }
    }

    /* ═══════════════════════════════════════════════
       RESPONSIVE
    ═══════════════════════════════════════════════ */
    @media (max-width: 600px) {
      .app-container { padding: 10px; }
      .card { padding: 18px; }
      .player-layout { grid-template-columns: 1fr; }
      .album-section { max-width: 250px; margin: 0 auto; }
      .dj-stats { grid-template-columns: repeat(3, 1fr); }
      .controls-section { gap: 12px; }
      .status-bar { gap: 10px; }
      .status-item { padding: 5px 10px; font-size: 0.75rem; }
    }
  </style>
</head>
<body>

  <!-- ANİMASYONLU ARKA PLAN -->
  <div class="cosmic-bg">
    <div class="nebula"></div>
    <div class="nebula"></div>
    <div class="nebula"></div>
    <div class="nebula"></div>
  </div>
  <div class="star-field" id="starField"></div>

  <!-- ANA UYGULAMA -->
  <div class="app-container">

    <!-- HEADER -->
    <header class="header">
      <h1>🌌 Galactic Wave</h1>
      <div class="subtitle">Premium Radio Experience</div>

      <div class="status-bar">
        <div class="status-item live">
          <i class="fas fa-circle"></i>
          <span>YAYINDA</span>
        </div>
        <div class="status-item" id="statusListeners">
          <i class="fas fa-users"></i>
          <span><strong id="listenerCount">0</strong> Dinleyici</span>
        </div>
        <div class="status-item" id="statusBitrate">
          <i class="fas fa-tachometer-alt"></i>
          <span><strong id="bitrateVal">--</strong> kbps</span>
        </div>
        <div class="status-item dj-live" id="statusDj" style="display:none;">
          <i class="fas fa-microphone-alt"></i>
          <span>Canlı DJ: <strong id="statusDjName">--</strong></span>
        </div>
      </div>
    </header>

    <!-- PLAYER KARTI -->
    <div class="main-grid">
      <div class="card player-card">
        <div class="card-header">
          <i class="fas fa-satellite-dish"></i>
          <h3>Çalıyor</h3>
          <div class="badge badge-live" id="liveBadge">
            <i class="fas fa-circle" style="font-size:6px; margin-right:4px;"></i> CANLI
          </div>
        </div>

        <div class="player-layout">
          <!-- ALBÜM KAPAĞI -->
          <div class="album-section">
            <div class="album-art-wrapper" id="albumWrapper">
              <img src="https://via.placeholder.com/300/050520/00e0ff?text=🌌" 
                   alt="Albüm Kapağı" 
                   class="album-art" 
                   id="albumArt"
                   onerror="this.src='data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 300 300%22><rect fill=%22%23050520%22 width=%22300%22 height=%22300%22/><text fill=%22%2300e0ff%22 x=%2250%%22 y=%2250%%22 text-anchor=%22middle%22 font-size=%2260%22>🌌</text></svg>'">
              <div class="album-overlay">
                <button class="album-play-btn" id="albumPlayBtn">
                  <i class="fas fa-play"></i>
                </button>
              </div>
              <div class="album-playing-bars" id="albumBars">
                <span></span><span></span><span></span><span></span>
              </div>
              <div class="bitrate-badge" id="bitrateBadge">128 kbps</div>
            </div>
          </div>

          <!-- ŞARKI BİLGİLERİ -->
          <div class="song-info-section">
            <div class="now-playing-info">
              <span class="now-playing-label">🎵 Şimdi Çalıyor</span>
              <h2 class="song-title" id="songTitle">
                <span>Yükleniyor...</span>
              </h2>
              <p class="song-artist" id="songArtist">Galactic Wave Radio</p>
            </div>

            <!-- DJ BİLGİSİ -->
            <div class="dj-section" id="djSection" style="display:none;">
              <img src="" alt="DJ" class="dj-avatar" id="djAvatar"
                   onerror="this.style.display='none'; this.nextElementSibling.style.display='flex';">
              <div class="dj-avatar-placeholder" id="djAvatarPlaceholder" style="display:none;">
                <i class="fas fa-headphones"></i>
              </div>
              <div class="dj-info">
                <div class="dj-label">Canlı DJ</div>
                <div class="dj-name" id="djNameDisplay">--</div>
              </div>
              <div class="dj-live-indicator">
                <div class="dot"></div>
                CANLI
              </div>
            </div>

            <!-- İLERLEME -->
            <div class="progress-section">
              <div class="progress-bar" id="progressBar">
                <div class="progress-fill" id="progressFill"></div>
              </div>
              <div class="progress-time">
                <span id="timeElapsed">0:00</span>
                <span id="timeTotal">--:--</span>
              </div>
            </div>

            <!-- KONTROL BUTONLARI -->
            <div class="controls-section">
              <button class="ctrl-btn" id="btnShuffle" title="Karıştır">
                <i class="fas fa-random"></i>
              </button>
              <button class="ctrl-btn" id="btnPrev" title="Önceki">
                <i class="fas fa-step-backward"></i>
              </button>
              <button class="ctrl-btn main-play" id="btnPlay" title="Oynat/Duraklat">
                <i class="fas fa-play" id="playIcon"></i>
              </button>
              <button class="ctrl-btn" id="btnNext" title="Sonraki">
                <i class="fas fa-step-forward"></i>
              </button>
              <button class="ctrl-btn" id="btnRepeat" title="Tekrarla">
                <i class="fas fa-redo"></i>
              </button>
              <button class="ctrl-btn" id="btnLike" title="Beğen">
                <i class="far fa-heart"></i>
              </button>
              <button class="ctrl-btn" id="btnShare" title="Paylaş">
                <i class="fas fa-share-alt"></i>
              </button>
            </div>

            <!-- SES KONTROLÜ -->
            <div class="volume-section">
              <i class="fas fa-volume-up" id="volumeIcon"></i>
              <input type="range" class="volume-slider" id="volumeSlider" 
                     min="0" max="100" value="75">
              <span class="volume-val" id="volumeVal">75%</span>
            </div>
          </div>
        </div>
      </div>

      <!-- FREQ VISUALIZER -->
      <div class="card visualizer-card">
        <div class="card-header">
          <i class="fas fa-wave-square"></i>
          <h3>Frekans Analizörü</h3>
        </div>
        <div class="bars-container" id="freqBars"></div>

        <div class="eq-section">
          <div class="eq-modes">
            <button class="eq-mode-btn active" data-mode="normal">Normal</button>
            <button class="eq-mode-btn" data-mode="rock">Rock</button>
            <button class="eq-mode-btn" data-mode="jazz">Jazz</button>
            <button class="eq-mode-btn" data-mode="pop">Pop</button>
            <button class="eq-mode-btn" data-mode="electronic">Electronic</button>
          </div>
          <div class="eq-bands" id="eqBands"></div>
        </div>
      </div>

      <!-- ÇALMA LİSTESİ -->
      <div class="card playlist-card">
        <div class="card-header">
          <i class="fas fa-list-ul"></i>
          <h3>Çalma Listesi</h3>
          <div class="badge badge-live" id="historyCount">0 şarkı</div>
        </div>
        <div class="playlist-list" id="playlistList">
          <div class="loading-skeleton" style="height:50px; margin-bottom:8px;"></div>
          <div class="loading-skeleton" style="height:50px; margin-bottom:8px;"></div>
          <div class="loading-skeleton" style="height:50px; margin-bottom:8px;"></div>
          <div class="loading-skeleton" style="height:50px; margin-bottom:8px;"></div>
          <div class="loading-skeleton" style="height:50px;"></div>
        </div>
      </div>

      <!-- DJ PROFİLİ -->
      <div class="card dj-card">
        <div class="card-header">
          <i class="fas fa-headphones-alt"></i>
          <h3>DJ Profili</h3>
          <div class="badge badge-dj" id="djStatusBadge" style="display:none;">
            <i class="fas fa-circle" style="font-size:6px; margin-right:4px;"></i> CANLI
          </div>
        </div>
        <div class="dj-profile-section">
          <div class="dj-profile-placeholder" id="djProfilePlaceholder">
            <i class="fas fa-headphones"></i>
          </div>
          <img src="" alt="DJ" class="dj-profile-avatar" id="djProfileAvatar" 
               style="display:none;"
               onerror="this.style.display='none'; document.getElementById('djProfilePlaceholder').style.display='flex';">
          <div class="dj-profile-info">
            <h4 id="djProfileName">Otomatik Çalma</h4>
            <p id="djProfileDesc">Sanal DJ - Otomatik Playlist</p>
          </div>
        </div>
        <div class="dj-stats">
          <div class="dj-stat">
            <div class="value" id="statOnline">0</div>
            <div class="label">Online</div>
          </div>
          <div class="dj-stat">
            <div class="value" id="statUnique">0</div>
            <div class="label">Tekil</div>
          </div>
          <div class="dj-stat">
            <div class="value" id="statBitrate">--</div>
            <div class="label">kbps</div>
          </div>
        </div>
      </div>

      <!-- MESAJ DUVARI -->
      <div class="card message-wall">
        <div class="card-header">
          <i class="fas fa-comment-dots"></i>
          <h3>Mesajlar</h3>
        </div>
        <div class="message-input-area">
          <input type="text" class="message-input" id="messageInput" 
                 placeholder="Mesajınızı yazın..." maxlength="200">
          <button class="message-send-btn" id="messageSendBtn">GÖNDER</button>
        </div>
        <div class="message-list" id="messageList">
          <div class="message-item">
            <div class="message-avatar">🤖</div>
            <div class="message-body">
              <div class="message-author">Sistem</div>
              <div class="message-text">Galactic Wave Radio'ya hoş geldiniz! Şarkı isteklerinizi ve mesajlarınızı buraya yazabilirsiniz. 🌌</div>
              <div class="message-time">Şimdi</div>
            </div>
          </div>
        </div>
      </div>
    </div>

  </div>

  <!-- BOTTOM TOOLBAR -->
  <nav class="bottom-toolbar">
    <span class="toolbar-brand">GALACTIC WAVE</span>
    <div class="toolbar-nav">
      <button class="toolbar-btn" id="tbHome" title="Ana Sayfa">
        <i class="fas fa-home"></i>
      </button>
      <button class="toolbar-btn" id="tbSearch" title="Ara">
        <i class="fas fa-search"></i>
      </button>
      <button class="toolbar-btn" id="tbRadio" title="Radyo">
        <i class="fas fa-broadcast-tower"></i>
      </button>
      <button class="toolbar-btn" id="tbPlaylist" title="Liste">
        <i class="fas fa-stream"></i>
      </button>
      <button class="toolbar-btn" id="tbSettings" title="Ayarlar">
        <i class="fas fa-cog"></i>
      </button>
    </div>
  </nav>

  <!-- TOAST -->
  <div class="toast" id="toast">
    <i class="fas fa-check-circle"></i>
    <span id="toastText"></span>
  </div>

  <script>
    // ═══════════════════════════════════════════════════════════
    // GALACTIC WAVE RADIO - COMPLETE JAVASCRIPT ENGINE
    // ═══════════════════════════════════════════════════════════

    const CONFIG = {
      API_URL: 'api.php',
      REFRESH_INTERVAL: 10000,   // 10 saniye
      STREAM_URL: 'https://stream.radyocast.com/8028',
      FREQ_BARS_COUNT: 45,
      EQ_BANDS: [
        { label: '60Hz',   freq: 60 },
        { label: '170Hz',  freq: 170 },
        { label: '310Hz',  freq: 310 },
        { label: '600Hz',  freq: 600 },
        { label: '1kHz',   freq: 1000 },
        { label: '3kHz',   freq: 3000 },
        { label: '6kHz',   freq: 6000 },
        { label: '12kHz',  freq: 12000 },
        { label: '14kHz',  freq: 14000 },
        { label: '16kHz',  freq: 16000 }
      ],
      EQ_PRESETS: {
        normal:     [50, 50, 50, 50, 50, 50, 50, 50, 50, 50],
        rock:       [70, 65, 55, 45, 55, 65, 70, 70, 70, 65],
        jazz:       [55, 50, 45, 55, 60, 60, 55, 50, 55, 60],
        pop:        [45, 55, 65, 70, 65, 55, 50, 55, 60, 55],
        electronic: [70, 75, 60, 45, 50, 65, 75, 80, 75, 70]
      }
    };

    // ═══════════════════════════════════════════════════════════
    // STATE
    // ═══════════════════════════════════════════════════════════
    const state = {
      isPlaying: false,
      volume: 75,
      shuffle: false,
      repeat: false,
      liked: false,
      eqMode: 'normal',
      currentTrack: null,
      stationData: null,
      refreshTimer: null,
      progressTimer: null,
      elapsed: 0,
      trackDuration: 240,
      audioContext: null,
      analyser: null
    };

    // ═══════════════════════════════════════════════════════════
    // DOM REFS
    // ═══════════════════════════════════════════════════════════
    const $ = (sel) => document.querySelector(sel);
    const $$ = (sel) => document.querySelectorAll(sel);

    const DOM = {
      albumArt:       $('#albumArt'),
      songTitle:      $('#songTitle'),
      songArtist:     $('#songArtist'),
      djSection:      $('#djSection'),
      djAvatar:       $('#djAvatar'),
      djAvatarPh:     $('#djAvatarPlaceholder'),
      djNameDisplay:  $('#djNameDisplay'),
      djProfileAvatar:$('#djProfileAvatar'),
      djProfilePh:    $('#djProfilePlaceholder'),
      djProfileName:  $('#djProfileName'),
      djProfileDesc:  $('#djProfileDesc'),
      djStatusBadge:  $('#djStatusBadge'),
      statusDj:       $('#statusDj'),
      statusDjName:   $('#statusDjName'),
      btnPlay:        $('#btnPlay'),
      playIcon:       $('#playIcon'),
      albumPlayBtn:   $('#albumPlayBtn'),
      albumBars:      $('#albumBars'),
      btnPrev:        $('#btnPrev'),
      btnNext:        $('#btnNext'),
      btnShuffle:     $('#btnShuffle'),
      btnRepeat:      $('#btnRepeat'),
      btnLike:        $('#btnLike'),
      btnShare:       $('#btnShare'),
      volumeSlider:   $('#volumeSlider'),
      volumeIcon:     $('#volumeIcon'),
      volumeVal:      $('#volumeVal'),
      progressBar:    $('#progressBar'),
      progressFill:   $('#progressFill'),
      timeElapsed:    $('#timeElapsed'),
      timeTotal:      $('#timeTotal'),
      listenerCount:  $('#listenerCount'),
      bitrateVal:     $('#bitrateVal'),
      bitrateBadge:   $('#bitrateBadge'),
      statOnline:     $('#statOnline'),
      statUnique:     $('#statUnique'),
      statBitrate:    $('#statBitrate'),
      freqBars:       $('#freqBars'),
      eqBands:        $('#eqBands'),
      playlistList:   $('#playlistList'),
      historyCount:   $('#historyCount'),
      messageInput:   $('#messageInput'),
      messageSendBtn: $('#messageSendBtn'),
      messageList:    $('#messageList'),
      toast:          $('#toast'),
      toastText:      $('#toastText'),
      starField:      $('#starField')
    };

    // ═══════════════════════════════════════════════════════════
    // YILDIZ ARKA PLAN
    // ═══════════════════════════════════════════════════════════
    function createStars() {
      for (let i = 0; i < 200; i++) {
        const star = document.createElement('div');
        star.className = 'star';
        const size = Math.random() * 2.5 + 0.5;
        star.style.cssText = `
          width: ${size}px;
          height: ${size}px;
          top: ${Math.random() * 100}%;
          left: ${Math.random() * 100}%;
          --dur: ${Math.random() * 4 + 2}s;
          --delay: ${Math.random() * 5}s;
          opacity: ${Math.random() * 0.8 + 0.2};
        `;
        DOM.starField.appendChild(star);
      }
    }

    // ═══════════════════════════════════════════════════════════
    // FREKANS ÇUBUKLARI
    // ═══════════════════════════════════════════════════════════
    function createFreqBars() {
      DOM.freqBars.innerHTML = '';
      for (let i = 0; i < CONFIG.FREQ_BARS_COUNT; i++) {
        const bar = document.createElement('div');
        bar.className = `freq-bar${i % 2 === 0 ? '' : ' odd'}`;
        bar.style.height = '4px';
        DOM.freqBars.appendChild(bar);
      }
    }

    // ═══════════════════════════════════════════════════════════
    // EQ BANTLARI
    // ═══════════════════════════════════════════════════════════
    function createEQBands() {
      DOM.eqBands.innerHTML = '';
      CONFIG.EQ_BANDS.forEach((band, i) => {
        const div = document.createElement('div');
        div.className = 'eq-band';
        div.innerHTML = `
          <input type="range" class="eq-slider" id="eqSlider${i}" 
                 min="0" max="100" value="50" data-band="${i}">
          <span class="eq-label">${band.label}</span>
        `;
        DOM.eqBands.appendChild(div);
      });

      // Event listeners
      $$('.eq-slider').forEach(slider => {
        slider.addEventListener('input', () => {
          state.eqMode = 'custom';
          $$('.eq-mode-btn').forEach(b => b.classList.remove('active'));
        });
      });
    }

    // ═══════════════════════════════════════════════════════════
    // API VERİ ÇEKME
    // ═══════════════════════════════════════════════════════════
    async function fetchStationData() {
      try {
        const res = await fetch(`${CONFIG.API_URL}?action=info&t=${Date.now()}`);

        if (!res.ok) {
          throw new Error(`HTTP ${res.status}`);
        }

        const data = await res.json();

        if (data.status === 'success') {
          state.stationData = data;
          updateUI(data);
        } else {
          console.warn('API hata:', data.message);
          showToast('⚠ Veri alınamadı', 'fa-exclamation-triangle');
        }
      } catch (err) {
        console.error('API bağlantı hatası:', err);
        showToast('📡 Bağlantı sorunu', 'fa-wifi');
      }
    }

    // ═══════════════════════════════════════════════════════════
    // UI GÜNCELLEME
    // ═══════════════════════════════════════════════════════════
    function updateUI(data) {
      const { now_playing, listeners, dj, history, station } = data;

      // ─── Albüm Kapağı ───
      if (now_playing.art) {
        DOM.albumArt.src = now_playing.art;
      }

      // ─── Şarkı Bilgisi ───
      DOM.songTitle.innerHTML = `<span>${escapeHtml(now_playing.title)}</span>`;
      state.currentTrack = now_playing.title;

      // Artist çıkar (genellikle "Sanatçı - Şarkı" formatında)
      const titleParts = now_playing.title.split(' - ');
      if (titleParts.length >= 2) {
        DOM.songArtist.textContent = titleParts[0].trim();
        DOM.songTitle.innerHTML = `<span>${escapeHtml(titleParts.slice(1).join(' - ').trim())}</span>`;
      } else {
        DOM.songArtist.textContent = 'Galactic Wave Radio';
      }

      // ─── Bitrate ───
      if (now_playing.bitrate) {
        DOM.bitrateVal.textContent = now_playing.bitrate;
        DOM.bitrateBadge.textContent = `${now_playing.bitrate} kbps`;
        DOM.statBitrate.textContent = now_playing.bitrate;
      }

      // ─── Dinleyici Sayısı ───
      animateNumber(DOM.listenerCount, listeners.online);
      animateNumber(DOM.statOnline, listeners.online);
      animateNumber(DOM.statUnique, listeners.unique);

      // ─── DJ Bilgisi ───
      if (dj.is_live && dj.username) {
        // DJ varsa göster
        DOM.djSection.style.display = 'flex';
        DOM.statusDj.style.display = 'flex';
        DOM.djStatusBadge.style.display = 'block';

        DOM.djNameDisplay.textContent = dj.username;
        DOM.statusDjName.textContent = dj.username;
        DOM.djProfileName.textContent = dj.username;
        DOM.djProfileDesc.textContent = 'Canlı Yayın DJ';

        // DJ Avatar
        if (dj.profile) {
          DOM.djAvatar.src = dj.profile;
          DOM.djAvatar.style.display = 'block';
          DOM.djAvatarPh.style.display = 'none';

          DOM.djProfileAvatar.src = dj.profile;
          DOM.djProfileAvatar.style.display = 'block';
          DOM.djProfilePh.style.display = 'none';
        } else {
          DOM.djAvatar.style.display = 'none';
          DOM.djAvatarPh.style.display = 'flex';
          DOM.djProfileAvatar.style.display = 'none';
          DOM.djProfilePh.style.display = 'flex';
        }
      } else {
        // DJ yoksa gizle
        DOM.djSection.style.display = 'none';
        DOM.statusDj.style.display = 'none';
        DOM.djStatusBadge.style.display = 'none';
        DOM.djProfileName.textContent = 'Otomatik Çalma';
        DOM.djProfileDesc.textContent = 'Sanal DJ - Otomatik Playlist';
        DOM.djProfileAvatar.style.display = 'none';
        DOM.djProfilePh.style.display = 'flex';
      }

      // ─── Çalma Listesi ───
      if (history && history.length > 0) {
        DOM.historyCount.textContent = `${history.length} şarkı`;
        DOM.playlistList.innerHTML = history.map((track, i) => `
          <div class="playlist-track ${i === 0 ? 'current' : ''}" data-index="${i}">
            <span class="track-number">${i === 0 ? '▶' : (i + 1)}</span>
            <div class="track-art-placeholder">
              <i class="fas fa-music"></i>
            </div>
            <div class="track-info">
              <div class="track-title">${escapeHtml(track.title)}</div>
              <div class="track-artist">${escapeHtml(track.artist || 'Bilinmiyor')}</div>
            </div>
            <span class="track-time">${track.time || ''}</span>
          </div>
        `).join('');
      }
    }

    // ═══════════════════════════════════════════════════════════
    // SAYI ANİMASYONU
    // ═══════════════════════════════════════════════════════════
    function animateNumber(element, target) {
      const current = parseInt(element.textContent.replace(/\D/g, '')) || 0;
      const diff = target - current;
      const steps = 20;
      const stepValue = diff / steps;
      let step = 0;

      const timer = setInterval(() => {
        step++;
        const val = Math.round(current + stepValue * step);
        element.textContent = val.toLocaleString('tr-TR');
        if (step >= steps) {
          element.textContent = target.toLocaleString('tr-TR');
          clearInterval(timer);
        }
      }, 30);
    }

    // ═══════════════════════════════════════════════════════════
    // OYNATMA KONTROLÜ
    // ═══════════════════════════════════════════════════════════
    function togglePlay() {
      state.isPlaying = !state.isPlaying;

      if (state.isPlaying) {
        DOM.playIcon.className = 'fas fa-pause';
        DOM.albumPlayBtn.innerHTML = '<i class="fas fa-pause"></i>';
        DOM.btnPlay.classList.add('is-playing');
        startVisualizer();
        startProgress();
        showToast('▶ Radyo başlatıldı!', 'fa-play');
      } else {
        DOM.playIcon.className = 'fas fa-play';
        DOM.albumPlayBtn.innerHTML = '<i class="fas fa-play"></i>';
        DOM.btnPlay.classList.remove('is-playing');
        stopVisualizer();
        stopProgress();
        showToast('⏸ Duraklatıldı', 'fa-pause');
      }
    }

    // ═══════════════════════════════════════════════════════════
    // İLERLEME ÇUBUĞU
    // ═══════════════════════════════════════════════════════════
    function startProgress() {
      state.elapsed = 0;
      clearInterval(state.progressTimer);

      state.progressTimer = setInterval(() => {
        if (!state.isPlaying) return;
        state.elapsed++;
        const pct = (state.elapsed / state.trackDuration) * 100;
        DOM.progressFill.style.width = `${Math.min(pct, 100)}%`;
        DOM.timeElapsed.textContent = formatTime(state.elapsed);

        // Her şarkıda sıfırla (simüle)
        if (state.elapsed >= state.trackDuration) {
          state.elapsed = 0;
          DOM.progressFill.style.width = '0%';
        }
      }, 1000);
    }

    function stopProgress() {
      clearInterval(state.progressTimer);
    }

    function formatTime(sec) {
      const m = Math.floor(sec / 60);
      const s = Math.floor(sec % 60);
      return `${m}:${s.toString().padStart(2, '0')}`;
    }

    // ═══════════════════════════════════════════════════════════
    // FREKANS GÖRSELLEŞTİRİCİ
    // ═══════════════════════════════════════════════════════════
    let visInterval = null;

    function startVisualizer() {
      const bars = $$('.freq-bar');
      visInterval = setInterval(() => {
        bars.forEach((bar, i) => {
          const h = Math.random() * 90 + 10;
          bar.style.height = `${h}px`;
        });
      }, 120);
    }

    function stopVisualizer() {
      clearInterval(visInterval);
      $$('.freq-bar').forEach(bar => {
        bar.style.height = '4px';
      });
    }

    // ═══════════════════════════════════════════════════════════
    // SES KONTROLÜ
    // ═══════════════════════════════════════════════════════════
    function setVolume(val) {
      val = Math.max(0, Math.min(100, parseInt(val)));
      state.volume = val;
      DOM.volumeSlider.value = val;
      DOM.volumeVal.textContent = `${val}%`;

      if (val === 0) {
        DOM.volumeIcon.className = 'fas fa-volume-mute';
      } else if (val < 30) {
        DOM.volumeIcon.className = 'fas fa-volume-off';
      } else if (val < 70) {
        DOM.volumeIcon.className = 'fas fa-volume-down';
      } else {
        DOM.volumeIcon.className = 'fas fa-volume-up';
      }
    }

    // ═══════════════════════════════════════════════════════════
    // EQ MODU
    // ═══════════════════════════════════════════════════════════
    function setEQMode(mode) {
      state.eqMode = mode;
      $$('.eq-mode-btn').forEach(btn => btn.classList.remove('active'));
      document.querySelector(`.eq-mode-btn[data-mode="${mode}"]`)?.classList.add('active');

      const preset = CONFIG.EQ_PRESETS[mode];
      if (preset) {
        preset.forEach((val, i) => {
          const slider = $(`#eqSlider${i}`);
          if (slider) slider.value = val;
        });
      }
      showToast(`🎛 EQ: ${mode.toUpperCase()}`, 'fa-sliders-h');
    }

    // ═══════════════════════════════════════════════════════════
    // MESAJ GÖNDERME
    // ═══════════════════════════════════════════════════════════
    function sendMessage() {
      const text = DOM.messageInput.value.trim();
      if (!text) return;

      const messageHTML = `
        <div class="message-item">
          <div class="message-avatar">👤</div>
          <div class="message-body">
            <div class="message-author">Sen</div>
            <div class="message-text">${escapeHtml(text)}</div>
            <div class="message-time">Şimdi</div>
          </div>
        </div>
      `;

      DOM.messageList.insertAdjacentHTML('afterbegin', messageHTML);
      DOM.messageInput.value = '';
      showToast('💬 Mesaj gönderildi!', 'fa-paper-plane');
    }

    // ═══════════════════════════════════════════════════════════
    // BEĞEN
    // ═══════════════════════════════════════════════════════════
    function toggleLike() {
      state.liked = !state.liked;
      const icon = DOM.btnLike.querySelector('i');

      if (state.liked) {
        icon.className = 'fas fa-heart';
        DOM.btnLike.classList.add('active');
        icon.style.color = 'var(--accent)';
        showToast('❤️ Beğenildi!', 'fa-heart');
      } else {
        icon.className = 'far fa-heart';
        DOM.btnLike.classList.remove('active');
        icon.style.color = '';
        showToast('💔 Beğeni kaldırıldı', 'fa-heart-broken');
      }
    }

    // ═══════════════════════════════════════════════════════════
    // PAYLAŞ
    // ═══════════════════════════════════════════════════════════
    function shareTrack() {
      const text = `🎵 Şu an dinliyorum: ${state.currentTrack || 'Galactic Wave Radio'} 🌌\n🎧 Galactic Wave Radio`;
      if (navigator.share) {
        navigator.share({ title: 'Galactic Wave Radio', text: text });
      } else {
        navigator.clipboard?.writeText(text);
        showToast('📋 Panoya kopyalandı!', 'fa-clipboard');
      }
    }

    // ═══════════════════════════════════════════════════════════
    // TOAST BİLDİRİM
    // ═══════════════════════════════════════════════════════════
    function showToast(msg, icon = 'fa-check-circle') {
      DOM.toastText.textContent = msg;
      DOM.toast.querySelector('i').className = `fas ${icon}`;
      DOM.toast.classList.add('show');

      clearTimeout(DOM.toast._t);
      DOM.toast._t = setTimeout(() => {
        DOM.toast.classList.remove('show');
      }, 3000);
    }

    // ═══════════════════════════════════════════════════════════
    // ESCAPE HTML
    // ═══════════════════════════════════════════════════════════
    function escapeHtml(str) {
      if (!str) return '';
      const div = document.createElement('div');
      div.textContent = str;
      return div.innerHTML;
    }

    // ═══════════════════════════════════════════════════════════
    // EVENT LISTENERS
    // ═══════════════════════════════════════════════════════════
    function bindEvents() {
      // Oynatma
      DOM.btnPlay.addEventListener('click', togglePlay);
      DOM.albumPlayBtn.addEventListener('click', togglePlay);

      // Ses
      DOM.volumeSlider.addEventListener('input', (e) => setVolume(e.target.value));
      DOM.volumeIcon.addEventListener('click', () => {
        setVolume(state.volume > 0 ? 0 : 75);
      });

      // Shuffle / Repeat
      DOM.btnShuffle.addEventListener('click', () => {
        state.shuffle = !state.shuffle;
        DOM.btnShuffle.classList.toggle('active', state.shuffle);
        showToast(state.shuffle ? '🔀 Karıştırma açık' : '🔀 Karıştırma kapalı', 'fa-random');
      });

      DOM.btnRepeat.addEventListener('click', () => {
        state.repeat = !state.repeat;
        DOM.btnRepeat.classList.toggle('active', state.repeat);
        showToast(state.repeat ? '🔁 Tekrar açık' : '🔁 Tekrar kapalı', 'fa-redo');
      });

      // Beğen / Paylaş
      DOM.btnLike.addEventListener('click', toggleLike);
      DOM.btnShare.addEventListener('click', shareTrack);

      // İleri / Geri
      DOM.btnPrev.addEventListener('click', () => {
        showToast('⏮ Önceki şarkı', 'fa-backward');
        state.elapsed = 0;
      });

      DOM.btnNext.addEventListener('click', () => {
        showToast('⏭ Sonraki şarkı', 'fa-forward');
        state.elapsed = 0;
      });

      // EQ Modları
      $$('.eq-mode-btn').forEach(btn => {
        btn.addEventListener('click', () => setEQMode(btn.dataset.mode));
      });

      // Mesaj gönderme
      DOM.messageSendBtn.addEventListener('click', sendMessage);
      DOM.messageInput.addEventListener('keydown', (e) => {
        if (e.key === 'Enter') sendMessage();
      });

      // Toolbar
      $('#tbHome')?.addEventListener('click', () => {
        window.scrollTo({ top: 0, behavior: 'smooth' });
      });

      $('#tbRadio')?.addEventListener('click', () => {
        togglePlay();
      });

      $('#tbPlaylist')?.addEventListener('click', () => {
        document.querySelector('.playlist-card')?.scrollIntoView({ behavior: 'smooth' });
      });

      $('#tbSettings')?.addEventListener('click', () => {
        showToast('⚙ Ayarlar menüsü', 'fa-cog');
      });

      $('#tbSearch')?.addEventListener('click', () => {
        showToast('🔍 Arama yakında!', 'fa-search');
      });

      // İlerleme çubuğu tıklama
      DOM.progressBar.addEventListener('click', (e) => {
        const rect = DOM.progressBar.getBoundingClientRect();
        const pct = ((e.clientX - rect.left) / rect.width) * 100;
        DOM.progressFill.style.width = `${pct}%`;
        state.elapsed = (pct / 100) * state.trackDuration;
        DOM.timeElapsed.textContent = formatTime(state.elapsed);
      });

      // Klavye kısayolları
      document.addEventListener('keydown', (e) => {
        if (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA') return;
        switch (e.key.toLowerCase()) {
          case ' ':       e.preventDefault(); togglePlay(); break;
          case 'arrowup':   e.preventDefault(); setVolume(state.volume + 5); break;
          case 'arrowdown': e.preventDefault(); setVolume(state.volume - 5); break;
          case 'm':       DOM.volumeIcon.click(); break;
          case 'l':       toggleLike(); break;
          case 'n':       DOM.btnNext.click(); break;
          case 'p':       DOM.btnPrev.click(); break;
        }
      });
    }

    // ═══════════════════════════════════════════════════════════
    // BAŞLATMA
    // ═══════════════════════════════════════════════════════════
    function init() {
      console.log('%c🌌 Galactic Wave Radio - Loading...', 
        'color:#00e0ff; font-size:18px; font-weight:bold;');

      // Yaratıcıları oluştur
      createStars();
      createFreqBars();
      createEQBands();

      // Event'leri bağla
      bindEvents();

      // Ses ayarla
      setVolume(75);

      // İlk veri çekme
      fetchStationData();

      // Periyodik güncelleme
      state.refreshTimer = setInterval(fetchStationData, CONFIG.REFRESH_INTERVAL);

      // Zaman göstergesi
      DOM.timeTotal.textContent = '~4:00';

      console.log('%c🚀 Galactic Wave Radio Ready!', 
        'color:#00ff88; font-size:14px;');
    }

    // Sayfa yüklenince başlat
    document.addEventListener('DOMContentLoaded', init);
  </script>

</body>
</html>
```

---

## 🔄 Yeni Eklenen Özellikler

| # | Özellik | Açıklama |
|---|---------|----------|
| 1 | **🔄 Gerçek API Entegrasyonu** | Radyocast API'den 10 saniyede bir otomatik veri çekme |
| 2 | **🎵 Dinamik Albüm Kapağı** | API'den gelen `art` URL'si ile gerçek kapak gösterimi |
| 3 | **📡 Canlı Şarkı Bilgisi** | `title` alanından sanatçı ve şarkı ayrıştırma |
| 4 | **👥 Gerçek Dinleyici Sayacı** | Online + Tekil dinleyici animasyonlu gösterim |
| 5 | **🎧 DJ Profil Kartı** | API'den DJ adı ve profil fotoğrafı |
| 6 | **📋 Çalma Geçmişi** | API'den gelen `history` ile son çalınan şarkılar |
| 7 | **📊 Bitrate Göstergesi** | Gerçek bitrate bilgisi (badge + stat) |
| 8 | **🎛 10 Bant EQ** | Görsel equalizer + 5 önayar modu |
| 9 | **💬 Mesaj Duvarı** | Kullanıcı mesaj gönderme sistemi |
| 10 | **🔀 Shuffle / Repeat** | Karıştır ve tekrarla kontrolleri |
| 11 | **❤️ Beğen Sistemi** | Animasyonlu kalp beğenisi |
| 12 | **📤 Paylaş** | Web Share API + Panoya kopyalama |
| 13 | **⌨️ Klavye Kısayolları** | Space, ↑↓, M, L, N, P |
| 14 | **📱 Responsive Tasarım** | Mobil uyumlu grid sistemi |
| 15 | **🌌 Animasyonlu Arka Plan** | 200 yıldız + 4 nebula animasyonu |
| 16 | **📡 API Proxy (api.php)** | CORS sorunlarını aşmak için PHP proxy |

> **Not:** Akış URL'sini `api.php` dosyasındaki `STREAM_URL` sabitine kendi stream adresinizi yazarak gerçek ses akışını bağlamanız gerekir.