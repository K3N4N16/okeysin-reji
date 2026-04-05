<think>
Kullanıcı kodun kesildiği yerden devam etmemi istiyor. `<input type="range" class="volume-input` satırından sonrasını tamamlayacağım.
</think>```html
<!-- Kalan HTML + JS -->
          <input type="range" class="volume-input" id="volRange" min="0" max="100" value="75">
        </div>
        <span class="volume-percent" id="volPercent">75%</span>
      </div>

    </div>
  </div>

  <!-- ALT İÇERİK -->
  <div class="bottom-section">
    
    <!-- SİNYAL PANELİ -->
    <div class="signal-container">
      <div class="signal-card">
        <div class="signal-header">
          <i class="fas fa-wave-square signal-icon"></i>
          <span class="signal-title">Frekans Sinyali</span>
          <div class="signal-badge">AKTİF</div>
        </div>
        <div class="freq-analyzer">
          <div class="freq-label">
            <span>FM</span>
            GALAXY
          </div>
          <div class="freq-visualizer" id="freqVisualizer"></div>
          <div class="freq-ticker">
            <div class="ticker-scroll" id="tickerScroll"></div>
          </div>
        </div>
        <iframe src="https://radyo.example/mesajlar" class="message-container" scrolling="no" title="Mesajlar"></iframe>
      </div>
    </div>

    <!-- ÇALMA LİSTESİ -->
    <div class="playlist-container">
      <div class="playlist-card">
        <div class="playlist-header">
          <i class="fas fa-compact-disc playlist-icon"></i>
          <span class="playlist-title">Çalma Listesi</span>
          <span class="playlist-count" id="playlistCount">12 Parça</span>
        </div>
        <div class="playlist-items" id="playlistItems"></div>
      </div>
    </div>

    <!-- DOKÜMANLAR -->
    <div class="docs-section">
      <div class="docs-card">
        <div class="docs-tabs">
          <button class="docs-tab active" data-tab="hakkimizda">Hakkımızda</button>
          <button class="docs-tab" data-tab="freq-info">Frekans Bilgisi</button>
          <button class="docs-tab" data-tab="kulup">Kulüp</button>
        </div>
        <div class="docs-content active" id="tab-hakkimizda">
          <h4>🌌 Galactic Wave Radio</h4>
          <p>
            Galactic Wave, 2021'den bu yana uzay temalı bir yayın akışı sunan bağımsız bir dijital radyo platformudur. 
            Uzay frekanslarını müzikle buluşturuyor, her dinleyiciye evrensel bir müzik deneyimi yaşatıyoruz.
          </p>
          <ul>
            <li>7/24 kesintisiz canlı yayın</li>
            <li>Uluslararası DJ kadrosu</li>
            <li>320 kbps HD ses kalitesi</li>
            <li>Etkileşimli şarkı istek sistemi</li>
          </ul>
        </div>
        <div class="docs-content" id="tab-freq-info">
          <h4>📡 Frekans Bilgisi</h4>
          <p>
            Dinleyicilerimiz dünya genelinde 50'den fazla ülkeden bağlanmaktadır.
            Yayınlarımız gerçek zamanlı olarak işlenmekte ve en yüksek kalitede iletilmektedir.
          </p>
          <ul>
            <li>Bit hızı: 320 kbps VBR</li>
            <li>Örnekleme hızı: 44.1 kHz Stereo</li>
            <li>Gecikme: ~200ms</li>
            <li>Uptime: %99.97</li>
          </ul>
        </div>
        <div class="docs-content" id="tab-kulup">
          <h4>🌟 Kulüp Üyeliği</h4>
          <p>
            Galactic Wave Kulübümüze katılın ve özel ayrıcalıklar kazanın:
          </p>
          <ul>
            <li>Reklamsız dinleme deneyimi</li>
            <li>Özel stüdyo içi canlı yayın erişimi</li>
            <li>Aylık özel mix setleri</li>
            <li>Canlı DJ etkinliklerinde öncelikli erişim</li>
          </ul>
        </div>
      </div>
    </div>

  </div>
</div>

<!-- JAVASCRIPT -->
<script>
(function() {
  "use strict";

  // ───── SES KAYNAĞI ─────
  const audio = new Audio();
  audio.volume = 0.75;
  let isPlaying = false;
  let currentTrack = 0;
  let progressInterval = null;
  let fakeProgress = 0;

  // ───── ELEMENTLER ─────
  const playBtn      = document.getElementById('playBtn');
  const playIcon     = document.getElementById('playIcon');
  const planetBody   = document.getElementById('planetBody');
  const waveDisplay  = document.getElementById('waveDisplay');
  const eqDisplay    = document.getElementById('eqDisplay');
  const songTitle    = document.getElementById('songTitle');
  const djName       = document.getElementById('djName');
  const volRange     = document.getElementById('volRange');
  const volTrack     = document.getElementById('volTrack');
  const volHandle    = document.getElementById('volHandle');
  const volPercent   = document.getElementById('volPercent');
  const volIcon      = document.getElementById('volIcon');
  const toastEl      = document.getElementById('toast');
  const toastText    = document.getElementById('toastText');
  const modalEl      = document.getElementById('modal');
  const modalClose   = document.getElementById('modalClose');
  const progressFill = document.getElementById('progressFill');
  const progressBar  = document.getElementById('progressBar');
  const currentTime  = document.getElementById('currentTime');
  const totalTime    = document.getElementById('totalTime');
  const listenerEl   = document.getElementById('listenerCount');
  const playlistEl   = document.getElementById('playlistItems');
  const playlistCount= document.getElementById('playlistCount');
  const bgStars      = document.getElementById('bgStars');
  const particlesZone= document.getElementById('particlesZone');
  const freqViz      = document.getElementById('freqVisualizer');
  const tickerScroll = document.getElementById('tickerScroll');
  const beams        = document.querySelectorAll('.energy-beam');
  const atmosphereRings = document.querySelectorAll('.atmosphere-ring');
  const eqBars       = [];

  // ───── ŞARKI VERİLERİ ─────
  const tracks = [
    { title: "Cosmic Journey — Stellar Mix",          artist: "DJ Nebula",    duration: "4:23", art: "https://images.unsplash.com/photo-1536819442624-498d2648b45d?w=80",  url: "" },
    { title: "Nebula Dreams — Ambient Voyage",         artist: "Aurora",       duration: "5:10", art: "https://images.unsplash.com/photo-1543722530-d2c3201371e7?w=80",  url: "" },
    { title: "Pulsar Beats — Deep Space",              artist: "Dr. Quasar",   duration: "3:48", art: "https://images.unsplash.com/photo-1614613535308-eb5fbd3d2c17?w=80",  url: "" },
    { title: "Solar Wind — Interstellar Frequency",    artist: "Zenith",       duration: "6:02", art: "https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=80",  url: "" },
    { title: "Dark Matter — Twilight Echo",            artist: "Eclipse",      duration: "4:55", art: "https://images.unsplash.com/photo-1516339901601-2e1b62dc0c45?w=80",  url: "" },
    { title: "Milky Way Groove — Funk in Space",       artist: "Stellar Band", duration: "3:33", art: "https://images.unsplash.com/photo-1507400492013-162706c8c05e?w=80",  url: "" },
    { title: "Quantum Leap — Future Bass",             artist: "Photon",       duration: "4:12", art: "https://images.unsplash.com/photo-1544899489-a083461d8f4a?w=80",  url: "" },
    { title: "Asteroid Belt — Tribal Ambient",         artist: "Astral",       duration: "5:40", art: "https://images.unsplash.com/photo-1462332420958-a05d1e002413?w=80",  url: "" },
    { title: "Andromeda Session — Chillwave",          artist: "Nova",         duration: "4:01", art: "https://images.unsplash.com/photo-1504384308090-c894fdcc538d?w=80",  url: "" },
    { title: "Satellite Drift — Lo-Fi Space",          artist: "Moonlight",    duration: "3:25", art: "https://images.unsplash.com/photo-1506477331477-33d5d8b3dc85?w=80",  url: "" },
    { title: "Black Hole Resonance — Dark Ambient",    artist: "Void Walker",  duration: "7:18", art: "https://images.unsplash.com/photo-1502085026219-229491c902e3?w=80",  url: "" },
    { title: "Supernova Pulse — Trance Edition",       artist: "Pulsar",       duration: "5:50", art: "https://images.unsplash.com/photo-1444703686981-a3abbc4d4fe3?w=80",  url: "" }
  ];

  const tickerMessages = [
    "🌌 Bugün uzay frekanslarımız mükemmel!",
    "💫 En iyi müzikler galaksinin ötesinde",
    "📡 Sinyal gücü maksimum seviyede",
    "🚀 İsteklerinizi uzaya gönderin",
    "🌠 Her frekansta bir gezegen var",
    "✨ Galactic Wave Radio her yerde",
    "🎵 Bir sonraki parça sizin seçiminiz olabilir",
    "🛸 Uzay müziği ruhun gıdasıdır"
  ];

  // ───── ARKA PLAN YILDIZLARI ─────
  function createBgStars() {
    for (let i = 0; i < 200; i++) {
      const star = document.createElement('div');
      star.className = 'star';
      const size = Math.random() * 2.5 + 0.5;
      star.style.cssText = `
        width: ${size}px;
        height: ${size}px;
        top: ${Math.random() * 100}%;
        left: ${Math.random() * 100}%;
        --delay: ${Math.random() * 6}s;
        --dur: ${Math.random() * 4 + 2}s;
      `;
      bgStars.appendChild(star);
    }
  }
  createBgStars();

  // ───── PARÇACIKLAR ─────
  const particleColors = ['#00e0ff','#c760ff','#00ff9d','#ffd700','#ff3366','#7b2fff'];
  function createParticles() {
    for (let i = 0; i < 50; i++) {
      const p = document.createElement('div');
      p.className = 'cosmic-particle';
      const size = Math.random() * 4 + 1;
      const dur = Math.random() * 6 + 3;
      const tx = (Math.random() * 160 - 80);
      const ty = (Math.random() * 160 - 80);
      p.style.cssText = `
        width: ${size}px;
        height: ${size}px;
        top: ${Math.random() * 100}%;
        left: ${Math.random() * 100}%;
        background: ${particleColors[i % particleColors.length]};
        --tx: ${tx}px;
        --ty: ${ty}px;
        --dur: ${dur}s;
        animation-delay: ${Math.random() * dur}s;
      `;
      particlesZone.appendChild(p);
    }
  }
  createParticles();

  // ───── DİNAMİK DALGA ÇUBUKLARI ─────
  function createWaves() {
    for (let i = 0; i < 35; i++) {
      const w = document.createElement('div');
      w.className = 'sound-wave';
      const max = Math.random() * 30 + 15;
      const dur = Math.random() * 0.7 + 0.5;
      w.style.cssText = `
        --max: ${max}px;
        --dur: ${dur}s;
        animation-delay: ${(i * 0.07) % dur}s;
      `;
      waveDisplay.appendChild(w);
    }
  }
  createWaves();

  // ───── EŞİZLEYİCİ BARLARI ─────
  function createEqBars() {
    for (let i = 0; i < 10; i++) {
      const b = document.createElement('div');
      b.className = 'eq-bar';
      eqDisplay.appendChild(b);
      eqBars.push(b);
    }
  }
  createEqBars();

  // ───── FREKANS BARLARI ─────
  function createFreqBars() {
    for (let i = 0; i < 50; i++) {
      const b = document.createElement('div');
      b.className = 'freq-bar';
      const max = Math.random() * 30 + 10;
      const dur = Math.random() * 0.6 + 0.35;
      b.style.cssText = `
        --max: ${max}px;
        --dur: ${dur}s;
        animation-delay: ${(i * 0.05) % dur}s;
      `;
      freqViz.appendChild(b);
    }
  }
  createFreqBars();

  // ───── FREKANS KAYAR MESAJLAR ─────
  function buildTicker() {
    const doubled = [...tickerMessages, ...tickerMessages];
    tickerScroll.innerHTML = doubled.map(m =>
      `<div class="ticker-item"><i class="fas fa-star"></i>${m}</div>`
    ).join('');
  }
  buildTicker();

  // ───── ÇALMA LİSTESİ OLUŞTUR ─────
  function renderPlaylist() {
    playlistEl.innerHTML = '';
    tracks.forEach((t, i) => {
      const item = document.createElement('div');
      item.className = 'playlist-item' + (i === currentTrack ? ' active' : '');
      item.innerHTML = `
        <div class="playlist-item-thumb">
          <img src="${t.art}" alt="${t.title}" onerror="this.parentElement.innerHTML='<i class=\\'fas fa-music\\'></i>'">
        </div>
        <div class="playlist-item-info">
          <div class="playlist-item-title">${t.title}</div>
          <div class="playlist-item-artist">${t.artist}</div>
        </div>
        <span class="playlist-item-duration">${t.duration}</span>
        <div class="playlist-item-play">
          <i class="fas fa-${i === currentTrack && isPlaying ? 'pause' : 'play'}"></i>
        </div>
      `;
      item.addEventListener('click', () => {
        currentTrack = i;
        applyTrack();
        if (!isPlaying) togglePlay();
        renderPlaylist();
      });
      playlistEl.appendChild(item);
    });
    playlistCount.textContent = `${tracks.length} Parça`;
  }
  renderPlaylist();

  // ───── PARÇAYI UYGULA ─────
  function applyTrack() {
    const t = tracks[currentTrack];
    const titleSpan = songTitle.querySelector('span');
    if (titleSpan) {
      titleSpan.textContent = t.title;
    } else {
      songTitle.textContent = t.title;
    }
    djName.textContent = t.artist;
    totalTime.textContent = t.duration;
    fakeProgress = 0;
    progressFill.style.width = '0%';
    currentTime.textContent = '0:00';

    // Marquee kontrolü
    requestAnimationFrame(() => {
      if (songTitle.scrollWidth > songTitle.parentElement.clientWidth) {
        songTitle.classList.add('marquee');
      } else {
        songTitle.classList.remove('marquee');
      }
    });
  }
  applyTrack();

  // ───── İLERİLEME ÇUBUĞU ─────
  function parseDuration(str) {
    const parts = str.split(':');
    return parseInt(parts[0]) * 60 + parseInt(parts[1]);
  }

  function formatTime(sec) {
    const m = Math.floor(sec / 60);
    const s = Math.floor(sec % 60);
    return `${m}:${s < 10 ? '0' : ''}${s}`;
  }

  function startProgress() {
    const totalSec = parseDuration(tracks[currentTrack].duration);
    if (progressInterval) clearInterval(progressInterval);
    progressInterval = setInterval(() => {
      if (!isPlaying) return;
      fakeProgress += 1;
      if (fakeProgress >= totalSec) {
        fakeProgress = 0;
        nextTrack();
        return;
      }
      const pct = (fakeProgress / totalSec) * 100;
      progressFill.style.width = pct + '%';
      currentTime.textContent = formatTime(fakeProgress);
    }, 1000);
  }

  // Tıklama ile ilerleme
  progressBar.addEventListener('click', (e) => {
    const rect = progressBar.getBoundingClientRect();
    const pct = (e.clientX - rect.left) / rect.width;
    const totalSec = parseDuration(tracks[currentTrack].duration);
    fakeProgress = Math.floor(pct * totalSec);
    progressFill.style.width = (pct * 100) + '%';
    currentTime.textContent = formatTime(fakeProgress);
  });

  // ───── OYNAT / DURDUR ─────
  function togglePlay() {
    isPlaying = !isPlaying;
    setVisualState(isPlaying);
    playIcon.className = 'fas fa-' + (isPlaying ? 'pause' : 'play');
    if (isPlaying) {
      audio.play().catch(() => {});
      startProgress();
      showToast('▶️ Yayın başlatıldı', 'fa-play-circle');
    } else {
      audio.pause();
      showToast('⏸ Yayın duraklatıldı', 'fa-pause-circle');
    }
    renderPlaylist();
  }

  function setVisualState(active) {
    // Gezegen
    planetBody.classList.toggle('playing', active);

    // Beams
    beams.forEach(b => b.classList.toggle('playing', active));

    // Atmosfer halkaları
    atmosphereRings.forEach(r => r.style.animationPlayState = active ? 'running' : 'paused');

    // Dalgalar
    document.querySelectorAll('.sound-wave').forEach(w => {
      w.classList.toggle('playing', active);
      w.style.animationPlayState = active ? 'running' : 'paused';
    });

    // Eşizleyici
    eqBars.forEach(b => {
      b.classList.toggle('playing', active);
      b.style.animationPlayState = active ? 'running' : 'paused';
    });

    // Frekans barları
    document.querySelectorAll('.freq-bar').forEach(b => {
      b.classList.toggle('playing', active);
      b.style.animationPlayState = active ? 'running' : 'paused';
    });

    // Parçacıklar
    document.querySelectorAll('.cosmic-particle').forEach(p => {
      p.classList.toggle('playing', active);
    });

    // Şarkı adı gradient
    const span = songTitle.querySelector('span');
    if (span) {
      span.style.animationPlayState = active ? 'running' : 'paused';
    }
  }

  playBtn.addEventListener('click', togglePlay);

  // ───── İLERİ / GERİ ─────
  function nextTrack() {
    currentTrack = (currentTrack + 1) % tracks.length;
    applyTrack();
    renderPlaylist();
    if (isPlaying) startProgress();
  }

  function prevTrack() {
    currentTrack = (currentTrack - 1 + tracks.length) % tracks.length;
    applyTrack();
    renderPlaylist();
    if (isPlaying) startProgress();
  }

  document.getElementById('nextBtn').addEventListener('click', () => {
    nextTrack();
    showToast('⏭ Sonraki parça', 'fa-forward');
  });

  document.getElementById('prevBtn').addEventListener('click', () => {
    prevTrack();
    showToast('⏮ Önceki parça', 'fa-backward');
  });

  // ───── KARIŞTIR / TEKRARLA ─────
  let shuffleOn = false;
  let repeatOn = false;

  document.getElementById('shuffleBtn').addEventListener('click', function() {
    shuffleOn = !shuffleOn;
    this.classList.toggle('active', shuffleOn);
    showToast(shuffleOn ? '🔀 Karıştırma açık' : '🔀 Karıştırma kapalı', 'fa-random');
  });

  document.getElementById('repeatBtn').addEventListener('click', function() {
    repeatOn = !repeatOn;
    this.classList.toggle('active', repeatOn);
    showToast(repeatOn ? '🔁 Tekrar açık' : '🔁 Tekrar kapalı', 'fa-redo');
  });

  // ───── SES KONTROLÜ ─────
  function setVolume(val) {
    val = Math.max(0, Math.min(100, val));
    audio.volume = val / 100;
    volTrack.style.height = val + '%';
    volHandle.style.bottom = 'calc(' + val + '% - 16px)';
    volPercent.textContent = val + '%';
    volRange.value = val;
    volTrack.style.setProperty('--vw', val + '%');

    if (val === 0) {
      volIcon.className = 'fas fa-volume-mute volume-icon';
    } else if (val < 30) {
      volIcon.className = 'fas fa-volume-down volume-icon';
    } else {
      volIcon.className = 'fas fa-volume-up volume-icon';
    }
  }

  setVolume(75);

  volRange.addEventListener('input', (e) => setVolume(+e.target.value));
  volIcon.addEventListener('click', () => {
    setVolume(audio.volume > 0 ? 0 : 75);
  });

  // ───── MODAL ─────
  document.querySelector('.request-btn')
    ? document.querySelector('.request-btn').addEventListener('click', openModal)
    : null;

  // Doğrudan buton bağla
  function openModal() { modalEl.classList.add('open'); }
  modalClose.addEventListener('click', () => modalEl.classList.remove('open'));
  modalEl.addEventListener('click', (e) => {
    if (e.target === modalEl) modalEl.classList.remove('open');
  });
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') modalEl.classList.remove('open');
  });

  // ───── TOAST ─────
  let toastTimer = null;
  function showToast(message, icon = 'fa-check-circle') {
    toastText.textContent = message;
    toastEl.querySelector('i').className = 'fas ' + icon;
    toastEl.classList.add('show');
    clearTimeout(toastTimer);
    toastTimer = setTimeout(() => toastEl.classList.remove('show'), 3500);
  }

  // ───── ARAÇ ÇUBUĞU ─────
  document.getElementById('toolHome').addEventListener('click', () => {
    showToast('🏠 Ana sayfadasınız', 'fa-home');
  });

  document.getElementById('toolPlaylist').addEventListener('click', () => {
    const pl = document.querySelector('.playlist-container');
    if (pl) pl.scrollIntoView({ behavior: 'smooth', block: 'center' });
    showToast('📋 Çalma listesi', 'fa-list');
  });

  document.getElementById('toolSearch').addEventListener('click', () => {
    openModal();
    showToast('🔍 Şarkı istekleri', 'fa-search');
  });

  document.getElementById('toolSettings').addEventListener('click', () => {
    showToast('⚙️ Ayarlar yakında!', 'fa-cog');
  });

  // ───── DOKÜMAN SEKMELERİ ─────
  document.querySelectorAll('.docs-tab').forEach(tab => {
    tab.addEventListener('click', function() {
      const target = this.dataset.tab;
      document.querySelectorAll('.docs-tab').forEach(t => t.classList.remove('active'));
      document.querySelectorAll('.docs-content').forEach(c => c.classList.remove('active'));
      this.classList.add('active');
      document.getElementById('tab-' + target).classList.add('active');
    });
  });

  // ───── EŞİZLEYİCİ MODLARI ─────
  document.querySelectorAll('.eq-mode').forEach(btn => {
    btn.addEventListener('click', function() {
      document.querySelectorAll('.eq-mode').forEach(b => b.classList.remove('active'));
      this.classList.add('active');

      const mode = this.dataset.mode;
      let heights;
      switch (mode) {
        case 'rock':
          heights = [55, 50, 60, 45, 55, 65, 40, 50, 55, 48];
          break;
        case 'jazz':
          heights = [35, 40, 30, 45, 38, 42, 36, 44, 32, 40];
          break;
        case 'pop':
          heights = [50, 48, 52, 55, 50, 45, 58, 47, 52, 49];
          break;
        default:
          heights = [50, 40, 60, 45, 55, 65, 35, 50, 48, 42];
      }
      eqBars.forEach((bar, i) => {
        bar.style.setProperty('--max', heights[i] + 'px');
      });
      showToast(`🎵 ${mode.charAt(0).toUpperCase() + mode.slice(1)} modu aktif`, 'fa-music');
    });
  });

  // ───── DİNLEYİCİ SAYACI ─────
  function updateListeners() {
    const base = 1247;
    const variation = Math.floor(Math.random() * 50 - 25);
    listenerEl.textContent = (base + variation).toLocaleString();
  }
  setInterval(updateListeners, 5000);

  // ───── SİNYAL GÜCÜ ─────
  function updateSignal() {
    const levels = ['MÜKEMMEL', 'GÜÇLÜ', 'İYİ', 'NORMAL'];
    const level = levels[Math.floor(Math.random() * levels.length)];
    document.getElementById('signalStrength').textContent = level;
  }
  setInterval(updateSignal, 8000);

  // ───── İLK BAĞLANTI SIMÜLASYONU ─────
  setTimeout(() => {
    showToast('📡 Galaktik sinyal yakalandı!', 'fa-satellite-dish');
  }, 2000);

  setTimeout(() => {
    applyTrack();
    if (!isPlaying) {
      isPlaying = true;
      setVisualState(true);
      playIcon.className = 'fas fa-pause';
      startProgress();
      renderPlaylist();
      showToast('▶️ Yayın otomatik başlatıldı', 'fa-play-circle');
    }
  }, 4000);

})();
</script>
</body>
</html>
```

Bu güncellenmiş versiyonda eklenen/kapsanan her şeyin özeti:

| Özellik | Açıklama |
|---|---|
| **Nebula arka plan** | Canlı mor/mavi/neon bulutsular animasyonlu |
| **Supernova dönen efekt** | Arka planda 60sn'de bir tur atan ışın |
| **Çalma listesi paneli** | 12 şarkı, tıklanabilir, albüm kapağı, ileri/geri senkronize |
| **İlerleme çubuğu** | Sahte ilerleme, tıklanabilir, şarkı geçişi otomatik |
| **Eşizleyici** | 10 bar + 4 mod (Normal/Rock/Jazz/Pop) |
| **Dokümanlar sekmesi** | 3 sekme — Hakkımızda, Frekans, Kulüp |
| **Araç çubuğu** | Alt sabit bar — Ev, Liste, Ara, Ayarlar |
| **Gerçek zamanlı sayaç** | Dinleyici sayısı her 5sn değişiyor |
| **Sinyal gücü dinamik** | MÜKEMMEL / GÜÇLÜ / İYİ / NORMAL |
| **Otomatik başlatma** | Sayfa açıldıktan 4sn sonra yayın otomatik başlar |
| **Toast bildirimleri** | Her etkileşimde açılır bildirim |
| **Responsive** | 1100px / 850px / 600px kırılımları |