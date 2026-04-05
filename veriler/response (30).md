<think>

Kullanıcı, bu HTML/CSS/JavaScript radyo sitesini daha da geliştirmemi ve özellikler eklememi, görselliği artırmamı istiyor. Mevcut kodu inceleyip şunları ekleyebilirim:

1. Daha fazla animasyon efekti
2. Yeni görsel elementler
3. Ek özellikler (playlist, equalizer, vs.)
4. Daha iyi responsive tasarım
5. Yeni renk şemaları ve efektler
6. Daha fazla interaktif element

Kodu önemli ölçüde genişletip geliştireceğim.

</think>

# Galactic Wave Radio - Gelişmiş Versiyon

Tamam! Radyo sitesini çok daha zengin görsellik, yeni özellikler ve gelişmiş animasyonlarla tamamen yeniden yapılandırıyorum.

```html
<!DOCTYPE html>
<html lang="tr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Galactic Wave Radio - Premium</title>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
<style>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;500;600;700;800;900&family=Space+Mono:wght@400;700&family=Exo+2:wght@300;400;500;600;700&display=swap');

:root {
  --primary: #00e0ff;
  --secondary: #c760ff;
  --accent: #ffd700;
  --energy: #00ff9d;
  --plasma: #ff3366;
  --cosmic: #7b2fff;
  --dark-bg: #000015;
  --panel-bg: #0d0024;
  --star: #ffffff;
  --glow-primary: 0 0 30px rgba(0, 224, 255, 0.6);
  --glow-secondary: 0 0 30px rgba(199, 96, 255, 0.6);
  --glow-energy: 0 0 30px rgba(0, 255, 157, 0.6);
}

* { margin: 0; padding: 0; box-sizing: border-box; }

body {
  background: var(--dark-bg);
  font-family: 'Exo 2', sans-serif;
  overflow-x: hidden;
  min-height: 100vh;
}

/* === ANİMASYONLU ARKA PLAN === */
.cosmic-bg {
  position: fixed;
  inset: 0;
  z-index: 0;
  overflow: hidden;
  background: 
    radial-gradient(ellipse at 20% 20%, rgba(199, 96, 255, 0.15) 0%, transparent 50%),
    radial-gradient(ellipse at 80% 80%, rgba(0, 224, 255, 0.12) 0%, transparent 50%),
    radial-gradient(ellipse at 50% 50%, rgba(123, 47, 255, 0.08) 0%, transparent 60%),
    var(--dark-bg);
}

.nebula {
  position: absolute;
  border-radius: 50%;
  filter: blur(80px);
  opacity: 0.4;
  animation: nebulaFloat 20s ease-in-out infinite;
}

.nebula-1 {
  width: 600px;
  height: 600px;
  background: radial-gradient(circle, var(--secondary), transparent 70%);
  top: -200px;
  left: -200px;
  animation-delay: 0s;
}

.nebula-2 {
  width: 500px;
  height: 500px;
  background: radial-gradient(circle, var(--primary), transparent 70%);
  bottom: -150px;
  right: -150px;
  animation-delay: -7s;
}

.nebula-3 {
  width: 400px;
  height: 400px;
  background: radial-gradient(circle, var(--cosmic), transparent 70%);
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  animation-delay: -14s;
}

@keyframes nebulaFloat {
  0%, 100% { transform: translate(0, 0) scale(1); }
  25% { transform: translate(30px, -20px) scale(1.1); }
  50% { transform: translate(-20px, 30px) scale(0.95); }
  75% { transform: translate(20px, 20px) scale(1.05); }
}

.stars-field {
  position: absolute;
  inset: 0;
}

.stars-field .star {
  position: absolute;
  background: white;
  border-radius: 50%;
  animation: starTwinkle var(--dur, 3s) infinite var(--delay, 0s);
}

@keyframes starTwinkle {
  0%, 100% { opacity: 0.2; transform: scale(0.8); }
  50% { opacity: 1; transform: scale(1.2); }
}

/* === SÜPERNOVSA EFEKTİ === */
.supernova {
  position: absolute;
  width: 800px;
  height: 800px;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  background: conic-gradient(
    from 0deg,
    transparent 0deg,
    rgba(199, 96, 255, 0.1) 60deg,
    transparent 120deg,
    rgba(0, 224, 255, 0.1) 180deg,
    transparent 240deg,
    rgba(123, 47, 255, 0.1) 300deg,
    transparent 360deg
  );
  border-radius: 50%;
  animation: supernovaSpin 60s linear infinite;
  pointer-events: none;
}

@keyframes supernovaSpin { to { transform: translate(-50%, -50%) rotate(360deg); } }

/* === ANA KONTEYNER === */
.main-container {
  position: relative;
  z-index: 10;
  max-width: 1400px;
  margin: 0 auto;
  padding: 20px;
  display: flex;
  flex-direction: column;
  gap: 25px;
}

/* === KOSMİK ÇERÇEVE === */
.cosmic-frame {
  position: relative;
  border-radius: 30px;
  padding: 3px;
  background: conic-gradient(
    from var(--angle),
    var(--primary),
    var(--secondary),
    var(--energy),
    var(--cosmic),
    var(--plasma),
    var(--primary)
  );
  animation: spinAngle 8s linear infinite;
  box-shadow:
    0 0 60px rgba(0, 224, 255, 0.3),
    0 0 120px rgba(199, 96, 255, 0.2),
    inset 0 0 60px rgba(0, 224, 255, 0.1);
}

@keyframes spinAngle { to { --angle: 360deg; } }
@property --angle { syntax: '<angle>'; initial-value: 0deg; inherits: false; }

.cosmic-frame::before {
  content: '';
  position: absolute;
  inset: -2px;
  border-radius: 32px;
  background: conic-gradient(
    from calc(var(--angle) * 2),
    var(--accent),
    var(--plasma),
    var(--energy),
    var(--accent)
  );
  filter: blur(20px);
  opacity: 0.5;
  z-index: -1;
  animation: spinAngle 12s linear infinite reverse;
}

/* === ANA PANEL === */
.galactic-panel {
  position: relative;
  background:
    radial-gradient(ellipse at 30% 20%, rgba(199, 96, 255, 0.2), transparent 50%),
    radial-gradient(ellipse at 70% 80%, rgba(0, 224, 255, 0.15), transparent 50%),
    radial-gradient(ellipse at 50% 50%, rgba(123, 47, 255, 0.1), transparent 60%),
    linear-gradient(165deg, var(--panel-bg) 0%, #050010 100%);
  border-radius: 28px;
  overflow: hidden;
  display: grid;
  grid-template-columns: 220px 1fr auto auto;
  align-items: stretch;
  min-height: 180px;
  isolation: isolate;
}

/* Tarama çizgisi */
.scan-line {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 3px;
  background: linear-gradient(90deg, 
    transparent 0%, 
    var(--primary) 20%, 
    var(--secondary) 50%, 
    var(--energy) 80%, 
    transparent 100%);
  animation: scanMove 6s linear infinite;
  z-index: 100;
  pointer-events: none;
  box-shadow: 
    0 0 20px var(--primary),
    0 0 40px var(--secondary);
}

@keyframes scanMove {
  0% { top: -3px; opacity: 0; }
  5% { opacity: 1; }
  95% { opacity: 1; }
  100% { top: 100%; opacity: 0; }
}

/* Grid arka plan efekti */
.grid-overlay {
  position: absolute;
  inset: 0;
  background-image: 
    linear-gradient(rgba(0, 224, 255, 0.03) 1px, transparent 1px),
    linear-gradient(90deg, rgba(0, 224, 255, 0.03) 1px, transparent 1px);
  background-size: 50px 50px;
  pointer-events: none;
  opacity: 0.5;
}

/* === ÜST LOGO BANNER === */
.galaxy-banner {
  position: absolute;
  top: 0;
  left: 218px;
  right: 0;
  height: 45px;
  z-index: 50;
  background: linear-gradient(
    90deg,
    rgba(0, 224, 255, 0.6) 0%,
    rgba(199, 96, 255, 0.5) 30%,
    rgba(123, 47, 255, 0.4) 50%,
    rgba(0, 255, 157, 0.3) 70%,
    rgba(255, 215, 0, 0.2) 100%
  );
  clip-path: polygon(0 0, 100% 0, 100% 100%, 20px 100%);
  display: flex;
  align-items: center;
  padding: 0 35px;
  gap: 20px;
  overflow: hidden;
}

.galaxy-banner::before {
  content: '';
  position: absolute;
  inset: 0;
  background: linear-gradient(
    90deg,
    transparent 0%,
    rgba(255, 255, 255, 0.3) 50%,
    transparent 100%
  );
  animation: bannerShine 4s linear infinite;
}

@keyframes bannerShine {
  0% { transform: translateX(-100%); }
  100% { transform: translateX(200%); }
}

.banner-text {
  font-family: 'Orbitron', sans-serif;
  font-size: 14px;
  font-weight: 900;
  letter-spacing: 5px;
  color: #fff;
  text-transform: uppercase;
  text-shadow: 0 0 20px var(--primary);
  position: relative;
  z-index: 1;
}

.banner-text span {
  color: var(--accent);
  text-shadow: 0 0 20px var(--accent);
}

.live-badge {
  display: flex;
  align-items: center;
  gap: 8px;
  background: rgba(0, 255, 157, 0.2);
  border: 1px solid rgba(0, 255, 157, 0.6);
  border-radius: 25px;
  padding: 5px 16px;
  font-size: 10px;
  font-weight: 700;
  font-family: 'Orbitron', sans-serif;
  color: var(--energy);
  letter-spacing: 2px;
  text-transform: uppercase;
  position: relative;
  z-index: 1;
  animation: livePulse 2s ease-in-out infinite;
}

@keyframes livePulse {
  0%, 100% { box-shadow: 0 0 0 0 rgba(0, 255, 157, 0.5); }
  50% { box-shadow: 0 0 0 8px rgba(0, 255, 157, 0); }
}

.live-dot {
  width: 10px;
  height: 10px;
  border-radius: 50%;
  background: var(--energy);
  box-shadow: 
    0 0 15px var(--energy),
    0 0 30px var(--energy);
  animation: liveDot 1s ease-in-out infinite;
}

@keyframes liveDot {
  0%, 100% { transform: scale(1); opacity: 1; }
  50% { transform: scale(0.6); opacity: 0.5; }
}

.listener-count {
  font-family: 'Orbitron', sans-serif;
  font-size: 11px;
  color: rgba(255, 255, 255, 0.8);
  display: flex;
  align-items: center;
  gap: 6px;
  position: relative;
  z-index: 1;
}

.listener-count i {
  color: var(--accent);
}

/* === GEZEGEN BÖLÜMÜ === */
.planet-section {
  position: relative;
  width: 220px;
  min-height: 180px;
  flex-shrink: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  background:
    radial-gradient(circle at 40% 50%, rgba(199, 96, 255, 0.3), transparent 60%),
    linear-gradient(150deg, #120033 0%, #080018 100%);
  overflow: hidden;
  z-index: 10;
}

.planet-section::after {
  content: '';
  position: absolute;
  right: 0;
  top: 0;
  bottom: 0;
  width: 30px;
  background: linear-gradient(90deg, transparent, var(--panel-bg));
  z-index: 5;
}

.planet-container {
  position: relative;
  width: 150px;
  height: 150px;
  z-index: 5;
}

/* Atmosferik halkalar */
.atmosphere-ring {
  position: absolute;
  top: 50%;
  left: 50%;
  border-radius: 50%;
  transform: translate(-50%, -50%);
  border: 1px solid;
  opacity: 0.5;
  animation: ringRotate var(--dur, 20s) linear infinite;
}

.atmosphere-ring:nth-child(1) {
  width: 160px;
  height: 160px;
  border-color: rgba(0, 224, 255, 0.5);
  animation-duration: 25s;
}

.atmosphere-ring:nth-child(2) {
  width: 180px;
  height: 180px;
  border-color: rgba(199, 96, 255, 0.4);
  animation-duration: 30s;
  animation-direction: reverse;
}

.atmosphere-ring:nth-child(3) {
  width: 200px;
  height: 200px;
  border-color: rgba(0, 255, 157, 0.3);
  animation-duration: 35s;
  border-style: dashed;
}

@keyframes ringRotate { to { transform: translate(-50%, -50%) rotate(360deg); } }

/* Gezegen gövdesi */
.planet-body {
  width: 130px;
  height: 130px;
  border-radius: 50%;
  position: relative;
  background:
    radial-gradient(circle at 35% 35%, #2a3a6a, #1a1a3a 50%, #0d0d24),
    conic-gradient(
      from 0deg at 50% 50%,
      #1a3a5a 0deg,
      #2a2a7a 60deg,
      #3a1a6a 120deg,
      #4a1a5a 180deg,
      #5a2a4a 240deg,
      #6a1a3a 300deg,
      #1a3a5a 360deg
    );
  box-shadow:
    0 0 0 3px rgba(255, 255, 255, 0.05),
    0 0 50px rgba(0, 224, 255, 0.5),
    0 0 100px rgba(199, 96, 255, 0.3),
    inset 0 0 50px rgba(0, 0, 0, 0.8),
    inset -30px -30px 60px rgba(0, 0, 0, 0.5),
    inset 20px 20px 40px rgba(255, 255, 255, 0.05);
  animation: planetRotation 30s linear infinite paused;
  overflow: hidden;
  z-index: 3;
}

.planet-body.playing {
  animation-play-state: running;
}

.planet-body::before {
  content: '';
  position: absolute;
  inset: 8px;
  border-radius: 50%;
  background: 
    repeating-radial-gradient(
      circle at center,
      transparent 0px,
      transparent 4px,
      rgba(255, 255, 255, 0.02) 4px,
      rgba(255, 255, 255, 0.02) 5px
    );
}

.planet-body::after {
  content: '';
  position: absolute;
  inset: 0;
  border-radius: 50%;
  background: linear-gradient(
    135deg,
    transparent 40%,
    rgba(255, 255, 255, 0.2) 60%,
    rgba(255, 255, 255, 0.4) 70%,
    transparent 80%
  );
  animation: planetShine 5s ease-in-out infinite paused;
}

.planet-body.playing::after {
  animation-play-state: running;
}

@keyframes planetShine {
  0%, 100% { opacity: 0.5; }
  50% { opacity: 1; }
}

@keyframes planetRotation { to { transform: rotate(360deg); } }

/* Gezegen yüzey detayları */
.surface-crater {
  position: absolute;
  border-radius: 50%;
  background: radial-gradient(circle, rgba(0, 0, 0, 0.3), transparent 70%);
  animation: craterFloat 6s ease-in-out infinite;
}

.crater-1 { width: 25px; height: 25px; top: 25%; left: 20%; animation-delay: 0s; }
.crater-2 { width: 18px; height: 18px; top: 55%; left: 45%; animation-delay: -2s; }
.crater-3 { width: 22px; height: 22px; top: 35%; right: 20%; animation-delay: -4s; }
.crater-4 { width: 15px; height: 15px; bottom: 25%; left: 35%; animation-delay: -1s; }
.crater-5 { width: 12px; height: 12px; top: 65%; right: 30%; animation-delay: -3s; }

@keyframes craterFloat {
  0%, 100% { transform: translate(0, 0); }
  25% { transform: translate(3px, -2px); }
  50% { transform: translate(-2px, 3px); }
  75% { transform: translate(-3px, -1px); }
}

/* Işın demeti */
.energy-beam {
  position: absolute;
  top: 50%;
  left: 50%;
  width: 150px;
  height: 3px;
  background: linear-gradient(
    90deg,
    transparent,
    var(--primary),
    var(--secondary),
    var(--energy),
    transparent
  );
  transform-origin: left;
  transform: translate(-50%, -50%) rotate(var(--angle, 0deg));
  opacity: 0.7;
  z-index: 2;
  filter: blur(1px);
}

.energy-beam.playing {
  animation: beamPulse 1.5s ease-in-out infinite;
}

@keyframes beamPulse {
  0%, 100% { opacity: 0.5; }
  50% { opacity: 1; filter: blur(1px) brightness(1.5); }
}

.beam-1 { --angle: 0deg; }
.beam-2 { --angle: 45deg; }
.beam-3 { --angle: 90deg; }
.beam-4 { --angle: 135deg; }
.beam-5 { --angle: 180deg; }
.beam-6 { --angle: 225deg; }
.beam-7 { --angle: 270deg; }
.beam-8 { --angle: 315deg; }

/* Parçacık alanı */
.particles-zone {
  position: absolute;
  inset: 0;
  pointer-events: none;
  z-index: 4;
}

.cosmic-particle {
  position: absolute;
  border-radius: 50%;
  opacity: 0;
  animation: particleDrift var(--dur, 6s) linear infinite;
}

.cosmic-particle.playing {
  animation-play-state: running;
}

@keyframes particleDrift {
  0% {
    transform: translate(0, 0) scale(0);
    opacity: 0.8;
  }
  50% {
    opacity: 1;
  }
  100% {
    transform: translate(var(--tx), var(--ty)) scale(1);
    opacity: 0;
  }
}

/* === MERKEZ PANEL === */
.center-zone {
  display: flex;
  flex-direction: column;
  justify-content: center;
  padding: 50px 30px 20px 40px;
  gap: 15px;
  position: relative;
  z-index: 10;
}

/* Korniş efekti */
.center-zone::before {
  content: '';
  position: absolute;
  top: 0;
  bottom: 0;
  left: 0;
  width: 35px;
  background: linear-gradient(90deg, var(--panel-bg), transparent);
  z-index: 10;
}

.center-zone::after {
  content: '';
  position: absolute;
  top: 0;
  bottom: 0;
  right: 0;
  width: 35px;
  background: linear-gradient(-90deg, var(--panel-bg), transparent);
  z-index: 10;
}

/* Şarkı bilgileri */
.song-info {
  position: relative;
  z-index: 5;
}

.song-title {
  display: inline-block;
  font-size: 22px;
  font-weight: 700;
  color: #fff;
  text-shadow: 
    0 0 20px rgba(0, 224, 255, 0.6),
    0 0 40px rgba(199, 96, 255, 0.3);
  position: relative;
  max-width: 100%;
  overflow: hidden;
}

.song-title span {
  background: linear-gradient(
    90deg,
    var(--primary),
    var(--secondary),
    var(--energy),
    var(--accent)
  );
  background-size: 200% auto;
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  animation: gradientFlow 3s linear infinite paused;
}

.song-title.playing span {
  animation: gradientFlow 3s linear infinite;
}

@keyframes gradientFlow {
  0% { background-position: 0% center; }
  100% { background-position: 200% center; }
}

.song-title.marquee {
  animation: marqueeScroll 15s linear infinite;
}

@keyframes marqueeScroll {
  0% { transform: translateX(0); }
  100% { transform: translateX(-50%); }
}

/* Sanatçı bilgisi */
.artist-row {
  display: flex;
  align-items: center;
  gap: 15px;
  flex-wrap: wrap;
}

.dj-badge {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 13px;
  font-weight: 500;
  color: rgba(255, 255, 255, 0.8);
  background: rgba(0, 224, 255, 0.1);
  padding: 6px 14px;
  border-radius: 20px;
  border: 1px solid rgba(0, 224, 255, 0.2);
}

.dj-badge i {
  color: var(--primary);
  font-size: 12px;
}

.quality-tag {
  font-size: 10px;
  font-weight: 700;
  font-family: 'Orbitron', sans-serif;
  padding: 5px 14px;
  border-radius: 22px;
  letter-spacing: 1.5px;
  background: linear-gradient(
    135deg,
    rgba(199, 96, 255, 0.2),
    rgba(0, 224, 255, 0.15)
  );
  border: 1px solid rgba(199, 96, 255, 0.3);
  color: rgba(255, 255, 255, 0.9);
  display: flex;
  align-items: center;
  gap: 6px;
}

.quality-tag i {
  color: var(--accent);
  font-size: 9px;
}

/* Albüm kapağı */
.album-art {
  width: 55px;
  height: 55px;
  border-radius: 12px;
  background: linear-gradient(135deg, var(--secondary), var(--primary));
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 
    0 0 25px rgba(199, 96, 255, 0.4),
    inset 0 0 15px rgba(255, 255, 255, 0.1);
  overflow: hidden;
  position: relative;
}

.album-art::before {
  content: '';
  position: absolute;
  inset: 0;
  background: url('https://images.unsplash.com/photo-1614613535308-eb5fbd3d2c17?w=100') center/cover;
  opacity: 0.8;
}

.album-art i {
  position: relative;
  z-index: 1;
  font-size: 22px;
  color: #fff;
  text-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
}

/* Kontrol butonları */
.control-zone {
  display: flex;
  align-items: center;
  gap: 20px;
  margin-top: 5px;
  position: relative;
  z-index: 5;
}

/* Ana oynatma butonu */
.play-hub {
  position: relative;
  width: 70px;
  height: 70px;
  flex-shrink: 0;
}

.play-hub::before {
  content: '';
  position: absolute;
  inset: -5px;
  border-radius: 50%;
  background: conic-gradient(
    from var(--angle),
    var(--primary),
    var(--secondary),
    var(--energy),
    var(--cosmic),
    var(--primary)
  );
  animation: spinAngle 3s linear infinite;
  opacity: 0.7;
  filter: blur(4px);
}

.play-hub::after {
  content: '';
  position: absolute;
  inset: -15px;
  border-radius: 50%;
  background: radial-gradient(circle, rgba(0, 224, 255, 0.2), transparent 70%);
  animation: hubGlow 2s ease-in-out infinite;
}

@keyframes hubGlow {
  0%, 100% { transform: scale(1); opacity: 0.5; }
  50% { transform: scale(1.2); opacity: 0.8; }
}

.play-button {
  position: absolute;
  inset: 0;
  border-radius: 50%;
  background: linear-gradient(145deg, #1a0d33, #0d051a);
  border: 2px solid rgba(255, 255, 255, 0.1);
  color: #fff;
  font-size: 24px;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.3s ease;
  z-index: 1;
  box-shadow:
    0 0 0 2px rgba(255, 255, 255, 0.05),
    inset 0 3px 6px rgba(255, 255, 255, 0.15),
    0 5px 20px rgba(0, 0, 0, 0.5);
}

.play-button:hover {
  transform: scale(1.12);
  background: linear-gradient(145deg, #2a124a, #15082a);
  box-shadow:
    0 0 30px rgba(0, 224, 255, 0.5),
    0 0 60px rgba(199, 96, 255, 0.3);
}

.play-button:active {
  transform: scale(0.95);
}

/* İkincil kontroller */
.secondary-controls {
  display: flex;
  gap: 12px;
}

.ctrl-btn {
  width: 48px;
  height: 48px;
  border-radius: 14px;
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid rgba(255, 255, 255, 0.1);
  color: rgba(255, 255, 255, 0.7);
  font-size: 16px;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.3s ease;
  position: relative;
  overflow: hidden;
}

.ctrl-btn::before {
  content: '';
  position: absolute;
  inset: 0;
  background: linear-gradient(135deg, var(--primary), var(--secondary));
  opacity: 0;
  transition: opacity 0.3s;
}

.ctrl-btn:hover::before { opacity: 0.25; }

.ctrl-btn:hover {
  color: #fff;
  border-color: var(--primary);
  transform: translateY(-3px) scale(1.08);
  box-shadow: 0 8px 25px rgba(0, 224, 255, 0.3);
}

.ctrl-btn i { position: relative; z-index: 1; }
.ctrl-btn.active { color: var(--energy); border-color: var(--energy); }
.ctrl-btn.active::before { opacity: 0.2; }

/* Ses dalgaları */
.wave-display {
  flex: 1;
  height: 60px;
  display: flex;
  align-items: center;
  gap: 3px;
  padding: 0 15px;
  position: relative;
}

.sound-wave {
  flex: 1;
  border-radius: 4px 4px 0 0;
  background: linear-gradient(to top, var(--primary), var(--secondary));
  animation: waveBounce var(--dur, 0.8s) ease-in-out infinite;
  animation-play-state: paused;
  box-shadow: 0 0 10px var(--primary);
}

.sound-wave.playing { animation-play-state: running; }

@keyframes waveBounce {
  0%, 100% { height: 8px; opacity: 0.4; }
  50% { height: var(--max, 40px); opacity: 1; }
}

.wave:nth-child(4n+1) { --primary: #00e0ff; --secondary: #c760ff; }
.wave:nth-child(4n+2) { --primary: #c760ff; --secondary: #00ff9d; }
.wave:nth-child(4n+3) { --primary: #00ff9d; --secondary: #ffd700; }
.wave:nth-child(4n) { --primary: #ffd700; --secondary: #00e0ff; }

/* Durum panosu */
.status-board {
  display: flex;
  flex-direction: column;
  align-items: flex-end;
  gap: 10px;
}

.status-row {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 11px;
  font-weight: 700;
  font-family: 'Orbitron', sans-serif;
  text-transform: uppercase;
  letter-spacing: 2px;
}

.status-row i {
  font-size: 13px;
  animation: statusBlink 1s ease-in-out infinite;
}

@keyframes statusBlink {
  0%, 100% { opacity: 1; }
  50% { opacity: 0.4; }
}

.status-live { color: var(--energy); }
.status-hd { color: var(--primary); }
.status-signal { color: var(--accent); }

/* === EŞİZLEYİCİ (EQUALIZER) === */
.eq-section {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 12px;
  padding: 45px 25px 20px 20px;
  border-left: 1px solid rgba(255, 255, 255, 0.06);
  min-width: 200px;
}

.eq-title {
  font-family: 'Orbitron', sans-serif;
  font-size: 10px;
  font-weight: 700;
  letter-spacing: 3px;
  color: rgba(255, 255, 255, 0.5);
  text-transform: uppercase;
}

.eq-display {
  display: flex;
  align-items: flex-end;
  gap: 4px;
  height: 70px;
  padding: 10px 15px;
  background: rgba(0, 0, 0, 0.4);
  border-radius: 15px;
  border: 1px solid rgba(255, 255, 255, 0.08);
}

.eq-bar {
  width: 8px;
  border-radius: 4px;
  background: linear-gradient(to top, var(--bar-color), transparent);
  animation: eqBounce var(--dur, 0.5s) ease-in-out infinite;
  animation-play-state: paused;
  box-shadow: 0 0 12px var(--bar-color);
}

.eq-bar.playing { animation-play-state: running; }

@keyframes eqBounce {
  0%, 100% { height: 10px; }
  50% { height: var(--max, 50px); }
}

.eq-bar:nth-child(1) { --bar-color: var(--primary); --max: 55px; --dur: 0.45s; }
.eq-bar:nth-child(2) { --bar-color: var(--secondary); --max: 40px; --dur: 0.5s; }
.eq-bar:nth-child(3) { --bar-color: var(--energy); --max: 65px; --dur: 0.4s; }
.eq-bar:nth-child(4) { --bar-color: var(--accent); --max: 45px; --dur: 0.55s; }
.eq-bar:nth-child(5) { --bar-color: var(--plasma); --max: 50px; --dur: 0.48s; }
.eq-bar:nth-child(6) { --bar-color: var(--cosmic); --max: 60px; --dur: 0.42s; }
.eq-bar:nth-child(7) { --bar-color: var(--primary); --max: 35px; --dur: 0.52s; }

.eq-modes {
  display: flex;
  gap: 8px;
}

.eq-mode {
  padding: 6px 12px;
  border-radius: 10px;
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid rgba(255, 255, 255, 0.1);
  color: rgba(255, 255, 255, 0.6);
  font-size: 9px;
  font-weight: 600;
  font-family: 'Orbitron', sans-serif;
  cursor: pointer;
  transition: all 0.3s;
  text-transform: uppercase;
  letter-spacing: 1px;
}

.eq-mode:hover {
  background: rgba(0, 224, 255, 0.15);
  border-color: var(--primary);
  color: #fff;
}

.eq-mode.active {
  background: linear-gradient(135deg, var(--primary), var(--secondary));
  border-color: transparent;
  color: #fff;
  box-shadow: 0 0 15px rgba(0, 224, 255, 0.4);
}

/* === SES KONTROLÜ === */
.volume-section {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 14px;
  padding: 45px 28px 20px 22px;
  border-left: 1px solid rgba(255, 255, 255, 0.06);
}

.volume-label {
  font-family: 'Orbitron', sans-serif;
  font-size: 10px;
  font-weight: 700;
  letter-spacing: 3px;
  color: rgba(255, 255, 255, 0.4);
  text-transform: uppercase;
}

.volume-icon {
  color: rgba(255, 255, 255, 0.7);
  font-size: 22px;
  cursor: pointer;
  transition: all 0.3s;
  padding: 8px;
}

.volume-icon:hover {
  color: var(--primary);
  transform: scale(1.2);
  filter: drop-shadow(0 0 15px var(--primary));
}

.volume-slider-container {
  position: relative;
  width: 40px;
  height: 100px;
  background: rgba(255, 255, 255, 0.06);
  border-radius: 25px;
  cursor: pointer;
  border: 1px solid rgba(255, 255, 255, 0.1);
  overflow: hidden;
}

.volume-track {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  border-radius: 25px;
  background: linear-gradient(
    to top,
    var(--primary),
    var(--secondary),
    var(--energy)
  );
  transition: height 0.15s;
  box-shadow: 0 0 20px var(--primary);
}

.volume-handle {
  position: absolute;
  left: 50%;
  transform: translateX(-50%);
  width: 32px;
  height: 32px;
  border-radius: 50%;
  background: linear-gradient(135deg, #fff, var(--primary));
  box-shadow:
    0 0 25px var(--primary),
    0 4px 15px rgba(0, 0, 0, 0.6);
  transition: bottom 0.15s;
  cursor: grab;
  pointer-events: none;
}

.volume-handle::before {
  content: '';
  position: absolute;
  inset: 3px;
  border-radius: 50%;
  background: linear-gradient(135deg, var(--primary), var(--secondary));
}

.volume-input {
  position: absolute;
  inset: 0;
  opacity: 0;
  cursor: pointer;
  writing-mode: vertical-lr;
  direction: rtl;
  -webkit-appearance: slider-vertical;
  width: 100%;
}

.volume-percent {
  font-family: 'Orbitron', sans-serif;
  font-size: 12px;
  font-weight: 700;
  color: var(--primary);
  text-shadow: 0 0 15px var(--primary);
}

/* === ALT PANEL: ŞARKI LİSTESİ === */
.bottom-section {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 20px;
}

/* Sinyal paneli */
.signal-container {
  position: relative;
  border-radius: 26px;
  padding: 3px;
  background: conic-gradient(
    from var(--angle),
    var(--secondary),
    var(--primary),
    var(--energy),
    var(--cosmic),
    var(--secondary)
  );
  animation: spinAngle 7s linear infinite;
  box-shadow:
    0 0 50px rgba(199, 96, 255, 0.2),
    0 0 100px rgba(0, 224, 255, 0.15);
}

.signal-card {
  background:
    radial-gradient(ellipse at 0% 0%, rgba(199, 96, 255, 0.25), transparent 50%),
    radial-gradient(ellipse at 100% 100%, rgba(0, 224, 255, 0.2), transparent 50%),
    rgba(8, 3, 20, 0.98);
  border-radius: 24px;
  overflow: hidden;
}

.signal-header {
  background: linear-gradient(
    135deg,
    var(--secondary) 0%,
    var(--primary) 50%,
    rgba(0, 255, 157, 0.6) 100%
  );
  padding: 16px 24px;
  display: flex;
  align-items: center;
  gap: 14px;
  position: relative;
  overflow: hidden;
}

.signal-header::before {
  content: '';
  position: absolute;
  inset: 0;
  background: linear-gradient(
    90deg,
    transparent,
    rgba(255, 255, 255, 0.3),
    transparent
  );
  animation: headerSweep 4s linear infinite;
}

@keyframes headerSweep {
  0% { transform: translateX(-100%); }
  100% { transform: translateX(200%); }
}

.signal-icon {
  font-size: 20px;
  color: #fff;
  position: relative;
  z-index: 1;
  filter: drop-shadow(0 0 15px var(--primary));
}

.signal-title {
  font-family: 'Orbitron', sans-serif;
  font-size: 13px;
  font-weight: 700;
  letter-spacing: 2.5px;
  color: #fff;
  flex: 1;
  text-transform: uppercase;
  position: relative;
  z-index: 1;
}

.signal-badge {
  background: rgba(0, 255, 157, 0.2);
  border: 1px solid rgba(0, 255, 157, 0.5);
  border-radius: 22px;
  padding: 5px 14px;
  font-size: 10px;
  font-weight: 700;
  font-family: 'Orbitron', sans-serif;
  color: var(--energy);
  letter-spacing: 1.5px;
  position: relative;
  z-index: 1;
  animation: badgePulse 2s ease-in-out infinite;
}

@keyframes badgePulse {
  0%, 100% { box-shadow: 0 0 0 0 rgba(0, 255, 157, 0.5); }
  50% { box-shadow: 0 0 0 8px rgba(0, 255, 157, 0); }
}

/* Frekans analizörü */
.freq-analyzer {
  height: 55px;
  display: flex;
  align-items: center;
  border-bottom: 1px solid rgba(255, 255, 255, 0.07);
  position: relative;
  overflow: hidden;
}

.freq-label {
  flex-shrink: 0;
  background: linear-gradient(135deg, var(--secondary), var(--primary));
  height: 100%;
  width: 100px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  font-family: 'Orbitron', sans-serif;
  font-size: 11px;
  font-weight: 700;
  color: #fff;
  letter-spacing: 2px;
  text-transform: uppercase;
  box-shadow: 8px 0 25px rgba(199, 96, 255, 0.6);
  z-index: 2;
}

.freq-label span {
  font-size: 16px;
  font-weight: 900;
  color: var(--primary);
  text-shadow: 0 0 20px var(--primary);
}

.freq-visualizer {
  flex: 1;
  height: 100%;
  display: flex;
  align-items: center;
  gap: 3px;
  padding: 5px 15px;
}

.freq-bar {
  flex: 1;
  border-radius: 4px 4px 0 0;
  background: linear-gradient(to top, var(--bar-color), transparent);
  animation: freqBounce var(--dur, 0.6s) ease-in-out infinite;
  animation-play-state: paused;
  box-shadow: 0 0 12px var(--bar-color);
}

.freq-bar.playing { animation-play-state: running; }

@keyframes freqBounce {
  0%, 100% { height: 6px; opacity: 0.4; }
  50% { height: var(--max, 40px); opacity: 1; }
}

.freq-bar:nth-child(3n+1) { --bar-color: var(--primary); }
.freq-bar:nth-child(3n+2) { --bar-color: var(--secondary); }
.freq-bar:nth-child(3n) { --bar-color: var(--energy); }

/* Frekans kayan mesaj */
.freq-ticker {
  flex-shrink: 0;
  overflow: hidden;
  border-left: 1px solid rgba(255, 255, 255, 0.1);
  width: 260px;
  height: 100%;
  display: flex;
  align-items: center;
  position: relative;
}

.freq-ticker::before,
.freq-ticker::after {
  content: '';
  position: absolute;
  top: 0;
  bottom: 0;
  width: 35px;
  z-index: 5;
}

.freq-ticker::before {
  left: 0;
  background: linear-gradient(90deg, rgba(8, 3, 20, 0.9), transparent);
}

.freq-ticker::after {
  right: 0;
  background: linear-gradient(-90deg, rgba(8, 3, 20, 0.9), transparent);
}

.ticker-scroll {
  display: inline-flex;
  white-space: nowrap;
  animation: tickerScroll 30s linear infinite;
  padding-left: 50px;
}

@keyframes tickerScroll {
  0% { transform: translateX(0); }
  100% { transform: translateX(-50%); }
}

.ticker-item {
  padding: 0 25px;
  font-size: 12px;
  font-weight: 600;
  color: rgba(255, 255, 255, 0.85);
  display: flex;
  align-items: center;
  gap: 8px;
}

.ticker-item i {
  font-size: 11px;
  color: var(--accent);
}

/* Mesaj iframe */
.message-container {
  width: 100%;
  height: 80px;
  border: none;
  background: transparent;
}

/* === ÇALMA LİSTESİ === */
.playlist-container {
  position: relative;
  border-radius: 26px;
  padding: 3px;
  background: conic-gradient(
    from var(--angle),
    var(--primary),
    var(--energy),
    var(--accent),
    var(--plasma),
    var(--primary)
  );
  animation: spinAngle 7s linear infinite reverse;
  box-shadow:
    0 0 50px rgba(0, 224, 255, 0.2),
    0 0 100px rgba(0, 255, 157, 0.15);
}

.playlist-card {
  background:
    radial-gradient(ellipse at 100% 0%, rgba(0, 224, 255, 0.2), transparent 50%),
    radial-gradient(ellipse at 0% 100%, rgba(255, 215, 0, 0.15), transparent 50%),
    rgba(8, 3, 20, 0.98);
  border-radius: 24px;
  overflow: hidden;
}

.playlist-header {
  background: linear-gradient(
    135deg,
    var(--primary) 0%,
    var(--energy) 50%,
    rgba(255, 215, 0, 0.6) 100%
  );
  padding: 16px 24px;
  display: flex;
  align-items: center;
  gap: 14px;
}

.playlist-icon {
  font-size: 20px;
  color: #fff;
  filter: drop-shadow(0 0 15px var(--primary));
}

.playlist-title {
  font-family: 'Orbitron', sans-serif;
  font-size: 13px;
  font-weight: 700;
  letter-spacing: 2.5px;
  color: #fff;
  flex: 1;
  text-transform: uppercase;
}

.playlist-count {
  background: rgba(0, 0, 0, 0.3);
  border-radius: 20px;
  padding: 5px 14px;
  font-size: 10px;
  font-weight: 700;
  font-family: 'Orbitron', sans-serif;
  color: #fff;
}

.playlist-items {
  max-height: 160px;
  overflow-y: auto;
  padding: 8px;
}

.playlist-items::-webkit-scrollbar {
  width: 6px;
}

.playlist-items::-webkit-scrollbar-track {
  background: rgba(255, 255, 255, 0.05);
  border-radius: 3px;
}

.playlist-items::-webkit-scrollbar-thumb {
  background: linear-gradient(var(--primary), var(--secondary));
  border-radius: 3px;
}

.playlist-item {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 10px 14px;
  border-radius: 12px;
  cursor: pointer;
  transition: all 0.3s;
  border: 1px solid transparent;
}

.playlist-item:hover {
  background: rgba(0, 224, 255, 0.1);
  border-color: rgba(0, 224, 255, 0.2);
}

.playlist-item.active {
  background: linear-gradient(90deg, rgba(0, 224, 255, 0.2), rgba(199, 96, 255, 0.15));
  border-color: rgba(0, 224, 255, 0.3);
}

.playlist-item-thumb {
  width: 40px;
  height: 40px;
  border-radius: 8px;
  background: linear-gradient(135deg, var(--secondary), var(--primary));
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
  overflow: hidden;
}

.playlist-item-thumb img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.playlist-item-thumb i {
  color: #fff;
  font-size: 14px;
}

.playlist-item-info {
  flex: 1;
  min-width: 0;
}

.playlist-item-title {
  font-size: 13px;
  font-weight: 600;
  color: #fff;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.playlist-item-artist {
  font-size: 11px;
  color: rgba(255, 255, 255, 0.6);
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.playlist-item-duration {
  font-family: 'Orbitron', sans-serif;
  font-size: 11px;
  color: var(--primary);
  flex-shrink: 0;
}

.playlist-item-play {
  width: 32px;
  height: 32px;
  border-radius: 50%;
  background: rgba(0, 224, 255, 0.2);
  border: 1px solid rgba(0, 224, 255, 0.4);
  color: var(--primary);
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
  opacity: 0;
  transition: all 0.3s;
}

.playlist-item:hover .playlist-item-play {
  opacity: 1;
}

.playlist-item-play:hover {
  background: var(--primary);
  color: #000;
  transform: scale(1.1);
}

/* === MODAL === */
.modal-overlay {
  display: none;
  position: fixed;
  inset: 0;
  background: rgba(0, 0, 20, 0.95);
  backdrop-filter: blur(40px) saturate(150%);
  z-index: 99999;
  justify-content: center;
  align-items: center;
  padding: 20px;
}

.modal-overlay.open { display: flex; animation: modalFadeIn 0.4s; }

@keyframes modalFadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}

.modal-wrapper {
  position: relative;
  width: 100%;
  max-width: 900px;
  height: 90vh;
  border-radius: 32px;
  padding: 3px;
  background: conic-gradient(
    from var(--angle),
    var(--secondary),
    var(--primary),
    var(--energy),
    var(--accent),
    var(--secondary)
  );
  animation: spinAngle 3s linear infinite, modalPopIn 0.5s cubic-bezier(0.4, 0, 0.2, 1);
  box-shadow:
    0 40px 120px rgba(0, 0, 0, 0.98),
    0 0 150px rgba(0, 224, 255, 0.4),
    0 0 280px rgba(199, 96, 255, 0.25);
}

@keyframes modalPopIn {
  from { transform: scale(0.7) translateY(80px); opacity: 0; }
  to { transform: scale(1) translateY(0); opacity: 1; }
}

.modal-body {
  width: 100%;
  height: 100%;
  border-radius: 30px;
  overflow: hidden;
  background:
    radial-gradient(ellipse at top left, rgba(199, 96, 255, 0.4), transparent 50%),
    radial-gradient(ellipse at bottom right, rgba(0, 224, 255, 0.35), transparent 50%),
    rgba(5, 0, 15, 0.98);
  display: flex;
  flex-direction: column;
}

.modal-header {
  background: linear-gradient(
    135deg,
    var(--secondary) 0%,
    var(--primary) 50%,
    rgba(0, 255, 157, 0.7) 100%
  );
  padding: 22px 30px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  position: relative;
  overflow: hidden;
  flex-shrink: 0;
}

.modal-header::before {
  content: '';
  position: absolute;
  inset: 0;
  background: linear-gradient(
    90deg,
    transparent,
    rgba(255, 255, 255, 0.3),
    transparent
  );
  animation: headerSweep 4s linear infinite;
}

.modal-heading {
  font-family: 'Orbitron', sans-serif;
  font-size: 20px;
  font-weight: 900;
  color: #fff;
  display: flex;
  align-items: center;
  gap: 16px;
  text-transform: uppercase;
  letter-spacing: 2px;
  z-index: 1;
}

.modal-heading i {
  animation: iconBounce 2s ease-in-out infinite;
}

@keyframes iconBounce {
  0%, 100% { transform: translateY(0) rotate(0); }
  50% { transform: translateY(-5px) rotate(5deg); }
}

.modal-close-btn {
  width: 50px;
  height: 50px;
  border-radius: 15px;
  background: rgba(255, 255, 255, 0.15);
  border: 2px solid rgba(255, 255, 255, 0.3);
  color: #fff;
  cursor: pointer;
  font-size: 22px;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.35s;
  z-index: 1;
}

.modal-close-btn:hover {
  background: rgba(0, 224, 255, 0.4);
  transform: rotate(90deg) scale(1.1);
  box-shadow: 0 0 35px rgba(0, 224, 255, 0.6);
}

.modal-iframe {
  width: 100%;
  flex: 1;
  border: none;
  background: #000;
}

/* === TOAST === */
.toast-message {
  position: fixed;
  bottom: 35px;
  right: 35px;
  padding: 18px 28px;
  border-radius: 20px;
  background: linear-gradient(135deg, rgba(199, 96, 255, 0.95), rgba(0, 224, 255, 0.92));
  border: 1px solid rgba(255, 255, 255, 0.25);
  color: #fff;
  font-weight: 700;
  font-size: 15px;
  box-shadow:
    0 15px 60px rgba(0, 0, 0, 0.7),
    0 0 70px rgba(0, 224, 255, 0.5);
  z-index: 999999;
  backdrop-filter: blur(30px);
  display: flex;
  align-items: center;
  gap: 14px;
  transform: translateY(150px) scale(0.8);
  opacity: 0;
  transition: all 0.5s cubic-bezier(0.4, 0, 0.2, 1);
  pointer-events: none;
}

.toast-message.show {
  transform: translateY(0) scale(1);
  opacity: 1;
}

.toast-message i {
  font-size: 20px;
  color: var(--energy);
}

/* === İLERLEME ÇUBUĞU === */
.progress-container {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-top: 5px;
}

.progress-time {
  font-family: 'Orbitron', sans-serif;
  font-size: 11px;
  color: rgba(255, 255, 255, 0.6);
  min-width: 45px;
}

.progress-bar {
  flex: 1;
  height: 6px;
  background: rgba(255, 255, 255, 0.1);
  border-radius: 3px;
  overflow: hidden;
  cursor: pointer;
  position: relative;
}

.progress-fill {
  height: 100%;
  width: 0%;
  background: linear-gradient(90deg, var(--primary), var(--secondary));
  border-radius: 3px;
  transition: width 0.1s linear;
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
  border-radius: 50%;
  background: var(--primary);
  box-shadow: 0 0 15px var(--primary);
  opacity: 0;
  transition: opacity 0.3s;
}

.progress-bar:hover .progress-fill::after {
  opacity: 1;
}

/* === ARAÇ ÇUBUĞU === */
.toolbar {
  position: fixed;
  bottom: 20px;
  left: 50%;
  transform: translateX(-50%);
  display: flex;
  gap: 8px;
  padding: 10px 20px;
  background: rgba(13, 0, 36, 0.95);
  backdrop-filter: blur(20px);
  border-radius: 50px;
  border: 1px solid rgba(255, 255, 255, 0.1);
  box-shadow: 0 10px 50px rgba(0, 0, 0, 0.5);
  z-index: 1000;
}

.toolbar-btn {
  width: 45px;
  height: 45px;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid rgba(255, 255, 255, 0.1);
  color: rgba(255, 255, 255, 0.7);
  font-size: 16px;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.3s;
}

.toolbar-btn:hover {
  background: rgba(0, 224, 255, 0.2);
  border-color: var(--primary);
  color: var(--primary);
  transform: translateY(-3px);
  box-shadow: 0 5px 20px rgba(0, 224, 255, 0.3);
}

/* === DÖKÜMAN === */
.docs-section {
  position: relative;
  border-radius: 26px;
  padding: 3px;
  background: conic-gradient(
    from var(--angle),
    var(--accent),
    var(--plasma),
    var(--primary),
    var(--accent)
  );
  animation: spinAngle 9s linear infinite;
  box-shadow: 0 0 50px rgba(255, 215, 0, 0.2);
}

.docs-card {
  background:
    radial-gradient(ellipse at top, rgba(255, 215, 0, 0.15), transparent 50%),
    rgba(8, 3, 20, 0.98);
  border-radius: 24px;
  overflow: hidden;
  padding: 20px;
}

.docs-tabs {
  display: flex;
  gap: 8px;
  margin-bottom: 15px;
  flex-wrap: wrap;
}

.docs-tab {
  padding: 10px 20px;
  border-radius: 12px;
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid rgba(255, 255, 255, 0.1);
  color: rgba(255, 255, 255, 0.7);
  font-size: 12px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s;
}

.docs-tab:hover {
  background: rgba(0, 224, 255, 0.15);
  border-color: var(--primary);
}

.docs-tab.active {
  background: linear-gradient(135deg, var(--accent), var(--plasma));
  border-color: transparent;
  color: #fff;
}

.docs-content {
  display: none;
}

.docs-content.active { display: block; }

.docs-content h4 {
  font-family: 'Orbitron', sans-serif;
  font-size: 14px;
  color: var(--accent);
  margin-bottom: 12px;
}

.docs-content p {
  font-size: 13px;
  color: rgba(255, 255, 255, 0.7);
  line-height: 1.7;
}

.docs-content ul {
  list-style: none;
  padding: 0;
}

.docs-content li {
  font-size: 12px;
  color: rgba(255, 255, 255, 0.7);
  padding: 6px 0;
  display: flex;
  align-items: center;
  gap: 8px;
}

.docs-content li::before {
  content: '›';
  color: var(--primary);
  font-size: 16px;
}

/* === RESPONSIVE === */
@media (max-width: 1100px) {
  .galactic-panel {
    grid-template-columns: 180px 1fr auto;
    grid-template-rows: auto auto;
  }
  
  .eq-section {
    grid-column: 1 / -1;
    flex-direction: row;
    justify-content: center;
    border-left: none;
    border-top: 1px solid rgba(255, 255, 255, 0.06);
    padding: 15px 20px;
  }
  
  .bottom-section {
    grid-template-columns: 1fr;
  }
}

@media (max-width: 850px) {
  .galactic-panel {
    grid-template-columns: 150px 1fr;
  }
  
  .volume-section {
    grid-column: 1 / -1;
    flex-direction: row;
    border-left: none;
    border-top: 1px solid rgba(255, 255, 255, 0.06);
    padding: 15px 24px;
    justify-content: center;
  }
  
  .volume-slider-container {
    width: 120px;
    height: 30px;
    border-radius: 20px;
  }
  
  .volume-track {
    left: 0;
    top: 0;
    bottom: 0;
    width: var(--vw, 75%);
    height: 100% !important;
    border-radius: 20px;
  }
  
  .volume-handle {
    bottom: unset !important;
    top: 50%;
    transform: translate(-50%, -50%);
    left: var(--vw, 75%);
  }
  
  .volume-input {
    writing-mode: unset;
    direction: unset;
    -webkit-appearance: none;
    width: 100%;
    height: 100%;
  }
  
  .galaxy-banner {
    left: 148px;
  }
}

@media (max-width: 600px) {
  .main-container {
    padding: 12px;
  }
  
  .galactic-panel {
    grid-template-columns: 120px 1fr;
  }
  
  .planet-container {
    width: 100px;
    height: 100px;
  }
  
  .planet-body {
    width: 80px;
    height: 80px;
  }
  
  .center-zone {
    padding: 45px 15px 15px 20px;
  }
  
  .song-title {
    font-size: 16px;
  }
  
  .play-hub {
    width: 55px;
    height: 55px;
  }
  
  .play-button {
    font-size: 18px;
  }
  
  .freq-ticker {
    display: none;
  }
  
  .toolbar {
    bottom: 10px;
    padding: 8px 15px;
  }
  
  .toolbar-btn {
    width: 38px;
    height: 38px;
    font-size: 14px;
  }
}
</style>
</head>
<body>

<!-- ANİMASYONLU ARKA PLAN -->
<div class="cosmic-bg">
  <div class="nebula nebula-1"></div>
  <div class="nebula nebula-2"></div>
  <div class="nebula nebula-3"></div>
  <div class="supernova"></div>
  <div class="stars-field" id="bgStars"></div>
</div>

<!-- TOAST -->
<div class="toast-message" id="toast">
  <i class="fas fa-check-circle"></i>
  <span id="toastText">İşlem başarılı!</span>
</div>

<!-- MODAL -->
<div class="modal-overlay" id="modal">
  <div class="modal-wrapper">
    <div class="modal-body">
      <div class="modal-header">
        <div class="modal-heading">
          <i class="fas fa-paper-plane"></i>
          Şarkı İsteği Gönder
        </div>
        <button class="modal-close-btn" id="modalClose">
          <i class="fas fa-times"></i>
        </button>
      </div>
      <iframe src="https://radyo.example/istek" class="modal-iframe" title="İstek"></iframe>
    </div>
  </div>
</div>

<!-- ARAÇ ÇUBUĞU -->
<div class="toolbar">
  <button class="toolbar-btn" id="toolHome" title="Ana Sayfa">
    <i class="fas fa-home"></i>
  </button>
  <button class="toolbar-btn" id="toolPlaylist" title="Çalma Listesi">
    <i class="fas fa-list"></i>
  </button>
  <button class="toolbar-btn" id="toolSearch" title="Ara">
    <i class="fas fa-search"></i>
  </button>
  <button class="toolbar-btn" id="toolSettings" title="Ayarlar">
    <i class="fas fa-cog"></i>
  </button>
</div>

<!-- ANA İÇERİK -->
<div class="main-container">

  <!-- ANA GALAKTİK PANEL -->
  <div class="cosmic-frame">
    <div class="galactic-panel" id="mainPanel">
      
      <div class="scan-line"></div>
      <div class="grid-overlay"></div>
      
      <!-- ÜST BANNER -->
      <div class="galaxy-banner">
        <div class="banner-text">GALACTIC<span>WAVE</span></div>
        <div class="live-badge">
          <div class="live-dot"></div>
          CANLI YAYIN
        </div>
        <div class="listener-count">
          <i class="fas fa-users"></i>
          <span id="listenerCount">1,247</span>
        </div>
      </div>

      <!-- GEZEGEN BÖLÜMÜ -->
      <div class="planet-section">
        <div class="planet-container">
          <div class="atmosphere-ring"></div>
          <div class="atmosphere-ring"></div>
          <div class="atmosphere-ring"></div>
          
          <div class="energy-beam beam-1" id="beam1"></div>
          <div class="energy-beam beam-2" id="beam2"></div>
          <div class="energy-beam beam-3" id="beam3"></div>
          <div class="energy-beam beam-4" id="beam4"></div>
          <div class="energy-beam beam-5" id="beam5"></div>
          <div class="energy-beam beam-6" id="beam6"></div>
          <div class="energy-beam beam-7" id="beam7"></div>
          <div class="energy-beam beam-8" id="beam8"></div>
          
          <div class="planet-body" id="planetBody">
            <div class="surface-crater crater-1"></div>
            <div class="surface-crater crater-2"></div>
            <div class="surface-crater crater-3"></div>
            <div class="surface-crater crater-4"></div>
            <div class="surface-crater crater-5"></div>
          </div>
        </div>
        
        <div class="particles-zone" id="particlesZone"></div>
      </div>

      <!-- MERKEZ PANEL -->
      <div class="center-zone">
        
        <div class="song-info">
          <div class="song-title" id="songTitle">
            <span>Galactic Wave Radio — Bağlanılıyor...</span>
          </div>
        </div>
        
        <div class="artist-row">
          <div class="album-art">
            <i class="fas fa-moon"></i>
          </div>
          <div class="dj-badge">
            <i class="fas fa-microphone-alt"></i>
            <span id="djName">Uzay Frekansları</span>
          </div>
          <div class="quality-tag">
            <i class="fas fa-bolt"></i>
            320 kbps · HD
          </div>
        </div>
        
        <div class="progress-container">
          <span class="progress-time" id="currentTime">0:00</span>
          <div class="progress-bar" id="progressBar">
            <div class="progress-fill" id="progressFill"></div>
          </div>
          <span class="progress-time" id="totalTime">0:00</span>
        </div>
        
        <div class="control-zone">
          <div class="play-hub">
            <button class="play-button" id="playBtn">
              <i class="fas fa-play" id="playIcon"></i>
            </button>
          </div>
          
          <div class="secondary-controls">
            <button class="ctrl-btn" id="prevBtn" title="Önceki">
              <i class="fas fa-backward"></i>
            </button>
            <button class="ctrl-btn" id="nextBtn" title="Sonraki">
              <i class="fas fa-forward"></i>
            </button>
            <button class="ctrl-btn" id="shuffleBtn" title="Karıştır">
              <i class="fas fa-random"></i>
            </button>
            <button class="ctrl-btn" id="repeatBtn" title="Tekrarla">
              <i class="fas fa-redo"></i>
            </button>
          </div>
          
          <div class="wave-display" id="waveDisplay"></div>
          
          <div class="status-board">
            <div class="status-row status-live">
              <i class="fas fa-satellite-dish"></i>
              CANLI
            </div>
            <div class="status-row status-hd">
              <i class="fas fa-shield-alt"></i>
              HD
            </div>
            <div class="status-row status-signal">
              <i class="fas fa-signal"></i>
              <span id="signalStrength">MÜKEMMEL</span>
            </div>
          </div>
        </div>
      </div>

      <!-- EŞİZLEYİCİ -->
      <div class="eq-section">
        <div class="eq-title">Eşizleyici</div>
        <div class="eq-display" id="eqDisplay"></div>
        <div class="eq-modes">
          <button class="eq-mode active" data-mode="normal">Normal</button>
          <button class="eq-mode" data-mode="rock">Rock</button>
          <button class="eq-mode" data-mode="jazz">Jazz</button>
          <button class="eq-mode" data-mode="pop">Pop</button>
        </div>
      </div>

      <!-- SES KONTROLÜ -->
      <div class="volume-section">
        <div class="volume-label">SES</div>
        <i class="fas fa-volume-up volume-icon" id="volIcon"></i>
        <div class="volume-slider-container" id="volContainer">
          <div class="volume-track" id="volTrack"></div>
          <div class="volume-handle" id="volHandle"></div>
          <input type="range" class="volume-input