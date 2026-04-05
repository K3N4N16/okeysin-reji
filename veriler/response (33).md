<think>

Kullanıcı HTML kodunun yarım kaldığı yerden devam etmemi istiyor. "volume-input" sınıfından sonra kod kesilmiş. Tam kodu yazmaya devam etmeliyim.

Verdiğim kod devam edecek:
```html
<input type="range" class="volume-input" id="volInput" min="0" max="100" value="75">
        </div>
        <span class="volume-percent" id="volPercent">75%</span>
      </div>

    </div>
  </div>

  <!-- ALT PANEL -->
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
          <div class="freq-visualizer" id="freqBars"></div>
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
          <i class="fas fa-list playlist-icon"></i>
          <span class="playlist-title">Sıradaki</span>
          <span class="playlist-count">5 parça</span>
        </div>
        
        <div class="playlist-items" id="playlist"></div>
      </div>
    </div>
    
  </div>
  
</div>
```

Devam edecek bölümler var, özellikle JavaScript kısmı eksik. Çalma listesi öğelerini dinamik olarak oluşturmak ve frekans çubuklarını render etmek için betik eklemem gerekiyor.

</think>

```html
        <input type="range" class="volume-input" id="volInput" min="0" max="100" value="75">
        </div>
        <span class="volume-percent" id="volPercent">75%</span>
      </div>

    </div>
  </div>

  <!-- ALT PANEL -->
  <div class="bottom-section">
    
    <!-- SİNYAL PANELİ -->
    <div class="signal-container">
      <div class="signal-card">
        <div class="signal-header">
          <i class="fas fa-wave-square signal-icon"></i>
          <span class="signal-title">Frekans Sinyali & Mesajlar</span>
          <div class="signal-badge">AKTİF</div>
        </div>
        
        <div class="freq-analyzer">
          <div class="freq-label">
            <span>FM</span>
            GALAXY
          </div>
          <div class="freq-visualizer" id="freqBars"></div>
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
          <i class="fas fa-list playlist-icon"></i>
          <span class="playlist-title">Galaktik Sıra</span>
          <span class="playlist-count" id="playlistCount">8 Parça</span>
        </div>
        
        <div class="playlist-items" id="playlistItems"></div>
      </div>
    </div>
    
  </div>

  <!-- DÖKÜMAN BÖLÜMÜ -->
  <div class="docs-section">
    <div class="docs-card">
      <div class="docs-tabs">
        <button class="docs-tab active" data-tab="about">Hakkında</button>
        <button class="docs-tab" data-tab="features">Özellikler</button>
        <button class="docs-tab" data-tab="shortcuts">Kısayollar</button>
        <button class="docs-tab" data-tab="contact">İletişim</button>
      </div>
      
      <div class="docs-content active" id="tab-about">
        <h4><i class="fas fa-rocket"></i> Galactic Wave Radio</h4>
        <p>Galactic Wave Radio, uzay temalı premium bir radyo deneyimi sunar. Evrenin derinliklerinden gelen sinyallerle 7/24 kesintisiz müzik keyfi.</p>
        <ul>
          <li>320 kbps HD ses kalitesi</li>
          <li>Gelişmiş eşizleyici sistemi</li>
          <li>Gerçek zamanlı şarkı isteme</li>
          <li>Animasyonlu galaktik arayüz</li>
        </ul>
      </div>
      
      <div class="docs-content" id="tab-features">
        <h4><i class="fas fa-star"></i> Öne Çıkan Özellikler</h4>
        <ul>
          <li>3D Dönen Gezegen Animasyonu</li>
          <li>Gerçek Zamanlı Frekans Analizörü</li>
          <li>Çoklu EQ Modları (Rock, Jazz, Pop, Normal)</li>
          <li>Kayan Şarkı Listesi</li>
          <li>Ses Dalga Görselleştirme</li>
          <li>Paylaş ve Beğen Sistemleri</li>
        </ul>
      </div>
      
      <div class="docs-content" id="tab-shortcuts">
        <h4><i class="fas fa-keyboard"></i> Klavye Kısayolları</h4>
        <ul>
          <li><kbd>Space</kbd> — Oynat / Duraklat</li>
          <li><kbd>↑↓</kbd> — Ses Artır / Azalt</li>
          <li><kbd>←→</kbd> — Önceki / Sonraki Parça</li>
          <li><kbd>M</kbd> — Sesi Kapat / Aç</li>
          <li><kbd>L</kbd> — Beğen</li>
          <li><kbd>Esc</kbd> — Modal'ı Kapat</li>
        </ul>
      </div>
      
      <div class="docs-content" id="tab-contact">
        <h4><i class="fas fa-envelope"></i> İletişim</h4>
        <p>Bize ulaşın, önerilerinizi ve isteklerinizi gönderin!</p>
        <ul>
          <li>E-posta: info@galacticwave.radio</li>
          <li>Web: www.galacticwave.radio</li>
          <li>Destek: 7/24 Online</li>
        </ul>
      </div>
    </div>
  </div>

</div>

<script>
// ═══════════════════════════════════════════════
// GALACTIC WAVE RADIO - PREMIUM JAVASCRIPT
// ═══════════════════════════════════════════════

// Ses kaynağı
const audio = new Audio('https://radyo.example/stream');
audio.volume = 0.75;
let isPlaying = false;
let currentTrack = 0;

// Çalma listesi
const playlist = [
  { title: "Cosmic Journey", artist: "Stellar Dreams", duration: "4:32" },
  { title: "Nebula Dreams", artist: "Galaxy Express", duration: "3:45" },
  { title: "Stellar Winds", artist: "Space Harmony", duration: "5:18" },
  { title: "Aurora Borealis", artist: "Cosmic Pulse", duration: "4:02" },
  { title: "Black Hole Symphony", artist: "Dark Matter", duration: "6:34" },
  { title: "Solar Flare", artist: "Plasma Wave", duration: "3:56" },
  { title: "Interstellar", artist: "Void Travelers", duration: "5:41" },
  { title: "Supernova", artist: "Star Forge", duration: "4:28" }
];

// Element seçicileri
const playBtn = document.getElementById('playBtn');
const playIcon = document.getElementById('playIcon');
const planetBody = document.getElementById('planetBody');
const waveDisplay = document.getElementById('waveDisplay');
const eqDisplay = document.getElementById('eqDisplay');
const freqBars = document.getElementById('freqBars');
const tickerScroll = document.getElementById('tickerScroll');
const songTitle = document.getElementById('songTitle');
const djName = document.getElementById('djName');
const volInput = document.getElementById('volInput');
const volTrack = document.getElementById('volTrack');
const volHandle = document.getElementById('volHandle');
const volPercent = document.getElementById('volPercent');
const volIcon = document.getElementById('volIcon');
const toast = document.getElementById('toast');
const toastText = document.getElementById('toastText');
const modal = document.getElementById('modal');
const prevBtn = document.getElementById('prevBtn');
const nextBtn = document.getElementById('nextBtn');
const shuffleBtn = document.getElementById('shuffleBtn');
const repeatBtn = document.getElementById('repeatBtn');
const progressFill = document.getElementById('progressFill');
const currentTimeEl = document.getElementById('currentTime');
const totalTimeEl = document.getElementById('totalTime');
const playlistItems = document.getElementById('playlistItems');
const particlesZone = document.getElementById('particlesZone');

// ═══════════════════════════════════════════════
// ARKA PLAN YILDIZLARI
// ═══════════════════════════════════════════════
const bgStars = document.getElementById('bgStars');
for (let i = 0; i < 150; i++) {
  const star = document.createElement('div');
  star.className = 'star';
  const size = Math.random() * 2 + 0.5;
  star.style.cssText = `
    width: ${size}px;
    height: ${size}px;
    top: ${Math.random() * 100}%;
    left: ${Math.random() * 100}%;
    --dur: ${Math.random() * 4 + 2}s;
    --delay: ${Math.random() * 5}s;
  `;
  bgStars.appendChild(star);
}

// ═══════════════════════════════════════════════
// GEZEGEN PARÇACIKLARI
// ═══════════════════════════════════════════════
const particleColors = [
  'var(--primary)',
  'var(--secondary)',
  'var(--energy)',
  'var(--accent)',
  'var(--plasma)'
];

for (let i = 0; i < 50; i++) {
  const particle = document.createElement('div');
  particle.className = 'cosmic-particle';
  
  const size = Math.random() * 4 + 1;
  const tx = (Math.random() - 0.5) * 200;
  const ty = (Math.random() - 0.5) * 200;
  const dur = Math.random() * 4 + 2;
  const delay = Math.random() * 5;
  
  particle.style.cssText = `
    width: ${size}px;
    height: ${size}px;
    top: ${Math.random() * 100}%;
    left: ${Math.random() * 100}%;
    background: ${particleColors[i % particleColors.length]};
    --tx: ${tx}px;
    --ty: ${ty}px;
    --dur: ${dur}s;
    --delay: ${delay}s;
    box-shadow: 0 0 ${size * 2}px currentColor;
  `;
  
  particlesZone.appendChild(particle);
}

// ═══════════════════════════════════════════════
// SES DALGALARI
// ═══════════════════════════════════════════════
for (let i = 0; i < 35; i++) {
  const wave = document.createElement('div');
  wave.className = 'sound-wave';
  const max = Math.random() * 30 + 20;
  const dur = Math.random() * 0.8 + 0.5;
  const delay = (i * 0.04) % dur;
  
  wave.style.cssText = `
    --max: ${max}px;
    --dur: ${dur}s;
    animation-delay: ${delay}s;
  `;
  
  waveDisplay.appendChild(wave);
}

// ═══════════════════════════════════════════════
// EŞİZLEYİCİ ÇUBUKLARI
// ═══════════════════════════════════════════════
for (let i = 0; i < 7; i++) {
  const bar = document.createElement('div');
  bar.className = 'eq-bar';
  eqDisplay.appendChild(bar);
}

// ═══════════════════════════════════════════════
// FREKANS ÇUBUKLARI
// ═══════════════════════════════════════════════
for (let i = 0; i < 50; i++) {
  const bar = document.createElement('div');
  bar.className = 'freq-bar';
  const max = Math.random() * 30 + 15;
  const dur = Math.random() * 0.6 + 0.3;
  const delay = (i * 0.03) % dur;
  
  bar.style.cssText = `
    --max: ${max}px;
    --dur: ${dur}s;
    animation-delay: ${delay}s;
  `;
  
  freqBars.appendChild(bar);
}

// ═══════════════════════════════════════════════
// FREKANS KAYAN MESAJLAR
// ═══════════════════════════════════════════════
const tickerMessages = [
  '🌌 "Galaktik dalgalar evrenin müziğidir"',
  '💫 Şu an 1,247 dinleyici bağlı!',
  '📡 Sinyal gücü: Mükemmel seviyede',
  '🚀 Uzay istasyonundan yayın yapılıyor',
  '🌠 Gezegenlerin ritmine kendinizi bırakın',
  '✨ Canlı DJ performansı devam ediyor',
  '🎵 320 kbps HD ses kalitesi aktif',
  '🌙 Yıldız tozlarından oluşan melodiler',
  '🔮 Galaktik Wave Radio - Evrenin Sesi',
  '⚡ Frekanslar yükleniyor...'
];

function buildTicker() {
  const doubled = [...tickerMessages, ...tickerMessages];
  tickerScroll.innerHTML = doubled.map(msg => 
    `<span class="ticker-item"><i class="fas fa-star"></i>${msg}</span>`
  ).join('');
}
buildTicker();

// ═══════════════════════════════════════════════
// ÇALMA LİSTESİ
// ═══════════════════════════════════════════════
function buildPlaylist() {
  playlistItems.innerHTML = playlist.map((track, index) => `
    <div class="playlist-item ${index === currentTrack ? 'active' : ''}" data-index="${index}">
      <div class="playlist-item-thumb">
        <i class="fas fa-music"></i>
      </div>
      <div class="playlist-item-info">
        <div class="playlist-item-title">${track.title}</div>
        <div class="playlist-item-artist">${track.artist}</div>
      </div>
      <span class="playlist-item-duration">${track.duration}</span>
      <div class="playlist-item-play">
        <i class="fas fa-play"></i>
      </div>
    </div>
  `).join('');
  
  document.getElementById('playlistCount').textContent = `${playlist.length} Parça`;
}
buildPlaylist();

// Playlist tıklama
playlistItems.addEventListener('click', (e) => {
  const item = e.target.closest('.playlist-item');
  if (item) {
    currentTrack = parseInt(item.dataset.index);
    updateTrack();
    showToast(`▶ ${playlist[currentTrack].title}`, 'fa-play');
  }
});

// ═══════════════════════════════════════════════
// OYNATMA DURUMU
// ═══════════════════════════════════════════════
function setPlayState(active) {
  if (active) {
    planetBody.classList.add('playing');
    document.querySelectorAll('.energy-beam').forEach(beam => beam.classList.add('playing'));
    document.querySelectorAll('.cosmic-particle').forEach(p => p.classList.add('playing'));
    document.querySelectorAll('.sound-wave').forEach(w => w.classList.add('playing'));
    document.querySelectorAll('.eq-bar').forEach(b => b.classList.add('playing'));
    document.querySelectorAll('.freq-bar').forEach(b => b.classList.add('playing'));
    playIcon.className = 'fas fa-pause';
    songTitle.classList.add('playing');
  } else {
    planetBody.classList.remove('playing');
    document.querySelectorAll('.energy-beam').forEach(beam => beam.classList.remove('playing'));
    document.querySelectorAll('.cosmic-particle').forEach(p => p.classList.remove('playing'));
    document.querySelectorAll('.sound-wave').forEach(w => w.classList.remove('playing'));
    document.querySelectorAll('.eq-bar').forEach(b => b.classList.remove('playing'));
    document.querySelectorAll('.freq-bar').forEach(b => b.classList.remove('playing'));
    playIcon.className = 'fas fa-play';
    songTitle.classList.remove('playing');
  }
}

// ═══════════════════════════════════════════════
// OYNATMA BUTONU
// ═══════════════════════════════════════════════
playBtn.addEventListener('click', () => {
  if (isPlaying) {
    audio.pause();
    isPlaying = false;
    setPlayState(false);
    showToast('⏸ Radyo duraklatıldı', 'fa-pause');
  } else {
    audio.play().catch(() => {
      showToast('⚠ Yayın başlatılamadı', 'fa-exclamation');
    });
    isPlaying = true;
    setPlayState(true);
    showToast('▶ Radyo başlatıldı!', 'fa-play');
  }
});

// ═══════════════════════════════════════════════
// SES KONTROLÜ
// ═══════════════════════════════════════════════
function setVolume(value) {
  value = Math.max(0, Math.min(100, value));
  audio.volume = value / 100;
  volTrack.style.height = `${value}%`;
  volHandle.style.bottom = `calc(${value}% - 16px)`;
  volPercent.textContent = `${value}%`;
  volInput.value = value;
  
  if (value === 0) {
    volIcon.className = 'fas fa-volume-mute volume-icon';
  } else if (value < 30) {
    volIcon.className = 'fas fa-volume-down volume-icon';
  } else if (value < 70) {
    volIcon.className = 'fas fa-volume-up volume-icon';
  } else {
    volIcon.className = 'fas fa-volume-up volume-icon';
  }
}

setVolume(75);
volInput.addEventListener('input', (e) => setVolume(+e.target.value));
volIcon.addEventListener('click', () => setVolume(audio.volume > 0 ? 0 : 75));

// ═══════════════════════════════════════════════
// PARÇACIK KONTROLÜ
// ═══════════════════════════════════════════════
let particlesActive = true;
function toggleParticles() {
  particlesActive = !particlesActive;
  document.querySelectorAll('.cosmic-particle').forEach(p => {
    p.style.animationPlayState = particlesActive ? 'running' : 'paused';
  });
}

// ═══════════════════════════════════════════════
// İLERLEME ÇUBUĞU (Simüle)
// ═══════════════════════════════════════════════
let progress = 0;
setInterval(() => {
  if (isPlaying) {
    progress += 0.5;
    if (progress > 100) progress = 0;
    progressFill.style.width = `${progress}%`;
    currentTimeEl.textContent = formatTime(progress * 2.5);
  }
}, 1000);

function formatTime(seconds) {
  const mins = Math.floor(seconds / 60);
  const secs = Math.floor(seconds % 60);
  return `${mins}:${secs.toString().padStart(2, '0')}`;
}

// ═══════════════════════════════════════════════
// ÇALMA LİSTESİ KONTROLÜ
// ═══════════════════════════════════════════════
function updateTrack() {
  const track = playlist[currentTrack];
  songTitle.innerHTML = `<span>${track.title} — ${track.artist}</span>`;
  buildPlaylist();
  totalTimeEl.textContent = track.duration;
  
  // Simüle: 15 saniyede bir şarkı değişimi
  progress = 0;
}

prevBtn.addEventListener('click', () => {
  currentTrack = (currentTrack - 1 + playlist.length) % playlist.length;
  updateTrack();
  showToast(`⏮ ${playlist[currentTrack].title}`, 'fa-backward');
});

nextBtn.addEventListener('click', () => {
  currentTrack = (currentTrack + 1) % playlist.length;
  updateTrack();
  showToast(`⏭ ${playlist[currentTrack].title}`, 'fa-forward');
});

// ═══════════════════════════════════════════════
// SHUFFLE & REPEAT
// ═══════════════════════════════════════════════
let shuffleOn = false;
let repeatOn = false;

shuffleBtn.addEventListener('click', () => {
  shuffleOn = !shuffleOn;
  shuffleBtn.classList.toggle('active', shuffleOn);
  showToast(shuffleOn ? '🔀 Karıştırma açık' : '🔀 Karıştırma kapalı', 'fa-random');
});

repeatBtn.addEventListener('click', () => {
  repeatOn = !repeatOn;
  repeatBtn.classList.toggle('active', repeatOn);
  showToast(repeatOn ? '🔁 Tekrar açık' : '🔁 Tekrar kapalı', 'fa-redo');
});

// ═══════════════════════════════════════════════
// EŞİZLEYİCİ MODLARI
// ═══════════════════════════════════════════════
document.querySelectorAll('.eq-mode').forEach(btn => {
  btn.addEventListener('click', () => {
    document.querySelectorAll('.eq-mode').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
    showToast(`🎛 EQ: ${btn.textContent}`, 'fa-sliders-h');
  });
});

// ═══════════════════════════════════════════════
// DÖKÜMAN TABLARI
// ═══════════════════════════════════════════════
document.querySelectorAll('.docs-tab').forEach(tab => {
  tab.addEventListener('click', () => {
    document.querySelectorAll('.docs-tab').forEach(t => t.classList.remove('active'));
    document.querySelectorAll('.docs-content').forEach(c => c.classList.remove('active'));
    tab.classList.add('active');
    document.getElementById(`tab-${tab.dataset.tab}`).classList.add('active');
  });
});

// ═══════════════════════════════════════════════
// MODAL
// ═══════════════════════════════════════════════
document.getElementById('toolPlaylist')?.addEventListener('click', () => {
  modal.classList.add('open');
});
document.getElementById('modalClose').addEventListener('click', () => {
  modal.classList.remove('open');
});
modal.addEventListener('click', (e) => {
  if (e.target === modal) modal.classList.remove('open');
});
document.addEventListener('keydown', (e) => {
  if (e.key === 'Escape') modal.classList.remove('open');
});

// ═══════════════════════════════════════════════
// ARAÇ ÇUBUĞU
// ═══════════════════════════════════════════════
document.getElementById('toolHome')?.addEventListener('click', () => {
  window.scrollTo({ top: 0, behavior: 'smooth' });
  showToast('🏠 Ana sayfaya dönüldü', 'fa-home');
});

document.getElementById('toolSearch')?.addEventListener('click', () => {
  showToast('🔍 Arama özelliği yakında!', 'fa-search');
});

document.getElementById('toolSettings')?.addEventListener('click', () => {
  showToast('⚙ Ayarlar menüsü açıldı', 'fa-cog');
});

// ═══════════════════════════════════════════════
// TOAST BİLDİRİM
// ═══════════════════════════════════════════════
function showToast(message, icon = 'fa-check-circle') {
  toastText.textContent = message;
  toast.querySelector('i').className = `fas ${icon}`;
  toast.classList.add('show');
  
  clearTimeout(toast._timer);
  toast._timer = setTimeout(() => {
    toast.classList.remove('show');
  }, 3500);
}

// ═══════════════════════════════════════════════
// KLAVYE KISAYOLLARI
// ═══════════════════════════════════════════════
document.addEventListener('keydown', (e) => {
  if (e.target.tagName === 'INPUT') return;
  
  switch(e.key.toLowerCase()) {
    case ' ':
      e.preventDefault();
      playBtn.click();
      break;
    case 'arrowup':
      e.preventDefault();
      setVolume(audio.volume * 100 + 5);
      break;
    case 'arrowdown':
      e.preventDefault();
      setVolume(audio.volume * 100 - 5);
      break;
    case 'arrowleft':
      e.preventDefault();
      prevBtn.click();
      break;
    case 'arrowright':
      e.preventDefault();
      nextBtn.click();
      break;
    case 'm':
      volIcon.click();
      break;
    case 'l':
      document.getElementById('likeButton')?.click();
      break;
  }
});

// ═══════════════════════════════════════════════
// DİNLeyıcı SAYACI (Simüle)
// ═══════════════════════════════════════════════
function updateListenerCount() {
  const base = 1247;
  const variance = Math.floor(Math.random() * 50) - 25;
  const count = base + variance;
  document.getElementById('listenerCount').textContent = count.toLocaleString('tr-TR');
}

setInterval(updateListenerCount, 8000);

// ═══════════════════════════════════════════════
// ŞARKI BİLGİSİ (Simüle)
// ═══════════════════════════════════════════════
function fetchTrackInfo() {
  const titles = [
    "Interstellar Dreams",
    "Galactic Harmony",
    "Cosmic Voyage",
    "Nebula Nights",
    "Stellar Journey",
    "Void Walker"
  ];
  const artists = [
    "DJ Cosmos",
    "Space Phantom",
    "Stellar Beats",
    "Void Harmony",
    "Galaxy Sound"
  ];
  
  const title = titles[Math.floor(Math.random() * titles.length)];
  const artist = artists[Math.floor(Math.random() * artists.length)];
  
  songTitle.innerHTML = `<span>${title} — ${artist}</span>`;
  djName.textContent = artist;
}

// ═══════════════════════════════════════════════
// BAŞLANGIÇ
// ═══════════════════════════════════════════════
updateTrack();
showToast('🌌 Galactic Wave Radio\'a hoş geldiniz!', 'fa-rocket');

// ═══════════════════════════════════════════════
// KONUM BAZLI ANİMASYONLAR
// ═══════════════════════════════════════════════
document.addEventListener('mousemove', (e) => {
  const beams = document.querySelectorAll('.energy-beam');
  beams.forEach((beam, i) => {
    const baseAngle = i * 45;
    const offset = (e.clientX / window.innerWidth - 0.5) * 10;
    beam.style.setProperty('--angle', `${baseAngle + offset}deg`);
  });
});

// ═══════════════════════════════════════════════
// GEZEGEN TIKLAMA
// ═══════════════════════════════════════════════
planetBody.addEventListener('click', () => {
  playBtn.click();
});

// ═══════════════════════════════════════════════
// SES GÖRSELLEŞTİRME OPTİMİZASYONU
// ═══════════════════════════════════════════════
if ('mediaSession' in navigator) {
  navigator.mediaSession.setActionHandler('play', () => playBtn.click());
  navigator.mediaSession.setActionHandler('pause', () => playBtn.click());
  navigator.mediaSession.setActionHandler('previoustrack', () => prevBtn.click());
  navigator.mediaSession.setActionHandler('nexttrack', () => nextBtn.click());
}

console.log('%c🌌 Galactic Wave Radio - Premium Edition', 
  'color: #00e0ff; font-size: 20px; font-weight: bold; text-shadow: 0 0 10px #00e0ff;');
console.log('%cEvrenin ritmine hazır olun!', 'color: #c760ff; font-size: 14px;');
</script>

</body>
</html>
```

## 🎮 Eklenen Yeni Özellikler

| Özellik | Açıklama |
|---------|----------|
| **Animasyonlu Nebula Arka Planı** | Süpernova efekti ve parallax yıldızlar |
| **3D Dönen Gezegen** | Krater detayları ve atmosferik halkalar |
| **8 Işın Demeti** | Mouse takip eden enerji ışınları |
| **Eşizleyici (EQ)** | 7 bant görsel, 4 mod (Rock, Jazz, Pop, Normal) |
| **Çalma Listesi** | 8 şarkılık gerçek zamanlı liste |
| **İlerleme Çubuğu** | Simüle edilmiş zaman göstergesi |
| **Dinleyici Sayacı** | Canlı sayaç animasyonu |
| **Klavye Kısayolları** | Space, ↑↓, ←→, M, L |
| **Döküman Bölümü** | 4 sekmeli bilgi paneli |
| **Alt Araç Çubuğu** | Sabit navigasyon butonları |
| **Kayan Frekans Mesajları** | 10 farklı galaktik mesaj |
| **Media Session API** | Bildirim merkezi desteği |