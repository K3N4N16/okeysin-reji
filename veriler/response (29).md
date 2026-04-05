<think>
The user wants me to continue developing and improving this "Galactic Wave Radio" HTML page, making it more visually stunning and complete. Let me enhance the design with:

1. More visual effects and animations
2. Better visual hierarchy
3. More interactive elements
4. Enhanced particle/star effects
5. Better color schemes and gradients
6. More detailed UI components
7. Enhanced responsive design
8. Audio visualizer improvements
9. Better modal design
10. More cosmic/space themed elements

Let me create a significantly enhanced version with all these improvements.
</think># 🌌 Galactic Wave Radio — Ultra Geliştirilmiş Versiyon

Aşağıda çok daha gelişmiş, görsel olarak zenginleştirilmiş tam versiyon:

```html
<!DOCTYPE html>
<html lang="tr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Galactic Wave Radio</title>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
<style>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;500;600;700;800;900&family=Space+Mono:wght@400;700&family=Exo+2:wght@200;300;400;500;600;700;800&display=swap');

:root{
  --primary:#00e0ff;
  --secondary:#c760ff;
  --accent:#ffd700;
  --energy:#00ff9d;
  --pink:#ff2d95;
  --orange:#ff6b35;
  --dark-bg:#000012;
  --panel-bg:#0a0020;
  --star:#ffffff;
  --glass:rgba(255,255,255,0.04);
  --glass-border:rgba(255,255,255,0.08);
}

*{margin:0;padding:0;box-sizing:border-box;}
html{scroll-behavior:smooth;}

body{
  background:var(--dark-bg);
  font-family:'Exo 2',sans-serif;
  overflow-x:hidden;
  min-height:100vh;
  color:#fff;
}

/* ═══════════════ KOSMİK ARKA PLAN ═══════════════ */
.cosmic-bg{
  position:fixed;inset:0;z-index:0;
  overflow:hidden;pointer-events:none;
}
.cosmic-bg .nebula{
  position:absolute;border-radius:50%;filter:blur(80px);opacity:0.15;
}
.nebula-1{width:600px;height:600px;background:radial-gradient(circle,var(--secondary),transparent);top:-10%;left:-5%;animation:nebFloat 20s ease-in-out infinite;}
.nebula-2{width:500px;height:500px;background:radial-gradient(circle,var(--primary),transparent);bottom:-10%;right:-5%;animation:nebFloat 25s ease-in-out infinite reverse;}
.nebula-3{width:400px;height:400px;background:radial-gradient(circle,var(--energy),transparent);top:40%;left:50%;animation:nebFloat 18s ease-in-out infinite 3s;}
@keyframes nebFloat{
  0%,100%{transform:translate(0,0) scale(1)}
  25%{transform:translate(30px,-20px) scale(1.05)}
  50%{transform:translate(-20px,30px) scale(0.95)}
  75%{transform:translate(20px,10px) scale(1.02)}
}

/* Yıldız arka planı */
.bg-stars{
  position:absolute;inset:0;
  background-image:
    radial-gradient(1px 1px at 10% 15%,rgba(255,255,255,0.8),transparent),
    radial-gradient(1px 1px at 20% 35%,rgba(255,255,255,0.6),transparent),
    radial-gradient(1.5px 1.5px at 30% 65%,rgba(0,224,255,0.7),transparent),
    radial-gradient(1px 1px at 40% 85%,rgba(255,255,255,0.5),transparent),
    radial-gradient(1px 1px at 50% 25%,rgba(199,96,255,0.6),transparent),
    radial-gradient(1.5px 1.5px at 60% 55%,rgba(255,255,255,0.7),transparent),
    radial-gradient(1px 1px at 70% 75%,rgba(0,255,157,0.5),transparent),
    radial-gradient(1px 1px at 80% 45%,rgba(255,255,255,0.6),transparent),
    radial-gradient(1.5px 1.5px at 90% 10%,rgba(255,215,0,0.5),transparent),
    radial-gradient(1px 1px at 15% 50%,rgba(255,255,255,0.4),transparent),
    radial-gradient(1px 1px at 25% 80%,rgba(0,224,255,0.4),transparent),
    radial-gradient(1.5px 1.5px at 35% 20%,rgba(255,255,255,0.6),transparent),
    radial-gradient(1px 1px at 45% 60%,rgba(199,96,255,0.4),transparent),
    radial-gradient(1px 1px at 55% 90%,rgba(255,255,255,0.5),transparent),
    radial-gradient(1px 1px at 65% 30%,rgba(0,255,157,0.4),transparent),
    radial-gradient(1.5px 1.5px at 75% 70%,rgba(255,255,255,0.7),transparent),
    radial-gradient(1px 1px at 85% 55%,rgba(255,215,0,0.3),transparent),
    radial-gradient(1px 1px at 95% 40%,rgba(255,255,255,0.5),transparent),
    radial-gradient(1px 1px at 5% 70%,rgba(0,224,255,0.5),transparent),
    radial-gradient(1.5px 1.5px at 12% 90%,rgba(255,255,255,0.6),transparent);
  animation:starField 120s linear infinite;
}
@keyframes starField{from{transform:translateY(0)}to{transform:translateY(-50px)}}

/* Kayan yıldızlar */
.shooting-star{
  position:absolute;width:80px;height:1px;
  background:linear-gradient(90deg,rgba(255,255,255,0.8),transparent);
  animation:shoot var(--dur,4s) linear infinite;
  opacity:0;
}
@keyframes shoot{
  0%{transform:translateX(-100px) translateY(0) rotate(-35deg);opacity:0}
  10%{opacity:1}
  100%{transform:translateX(calc(100vw + 200px)) translateY(200px) rotate(-35deg);opacity:0}
}

/* ═══════════════ ANA CONTAINER ═══════════════ */
.main-container{
  position:relative;z-index:10;
  max-width:1400px;
  margin:0 auto;
  padding:20px;
}

/* ═══════════════ ÜST BAŞLIK ═══════════════ */
.galaxy-header{
  text-align:center;
  padding:30px 20px 20px;
  position:relative;
}
.galaxy-header h1{
  font-family:'Orbitron',sans-serif;
  font-size:clamp(24px,4vw,48px);
  font-weight:900;
  letter-spacing:6px;
  background:linear-gradient(135deg,var(--primary),var(--secondary),var(--energy),var(--accent),var(--primary));
  background-size:400% 400%;
  -webkit-background-clip:text;
  -webkit-text-fill-color:transparent;
  background-clip:text;
  animation:gradShift 6s ease infinite;
  text-transform:uppercase;
  line-height:1.3;
}
@keyframes gradShift{
  0%{background-position:0% 50%}
  50%{background-position:100% 50%}
  100%{background-position:0% 50%}
}
.galaxy-header .subtitle{
  font-size:clamp(11px,1.5vw,14px);
  font-weight:400;
  letter-spacing:8px;
  color:rgba(255,255,255,0.4);
  text-transform:uppercase;
  margin-top:8px;
}
.header-line{
  width:200px;height:2px;margin:18px auto 0;
  background:linear-gradient(90deg,transparent,var(--primary),var(--secondary),var(--energy),transparent);
  border-radius:2px;
}

/* ═══════════════ KOSMİK ÇERÇEVE ═══════════════ */
.cosmic-frame{
  position:relative;
  border-radius:28px;
  padding:2.5px;
  background:conic-gradient(from var(--angle,0deg),var(--primary),var(--secondary),var(--energy),var(--accent),var(--primary));
  animation:spinAngle 6s linear infinite;
  box-shadow:
    0 0 30px rgba(0,224,255,0.2),
    0 0 60px rgba(199,96,255,0.1),
    inset 0 0 30px rgba(0,224,255,0.05);
}
@keyframes spinAngle{to{--angle:360deg;}}
@property --angle{syntax:'<angle>';initial-value:0deg;inherits:false;}

/* ═══════════════ ANA GALAKTİK PANEL ═══════════════ */
.galactic-panel{
  position:relative;
  background:
    radial-gradient(ellipse at 15% 25%,rgba(199,96,255,0.12),transparent 60%),
    radial-gradient(ellipse at 85% 75%,rgba(0,224,255,0.1),transparent 60%),
    radial-gradient(ellipse at 50% 50%,rgba(0,255,157,0.04),transparent 70%),
    linear-gradient(165deg,var(--panel-bg),#030008);
  border-radius:26px;
  overflow:hidden;
  min-height:180px;
  display:grid;
  grid-template-columns:190px 1fr 180px;
  grid-template-rows:auto 1fr;
  gap:0;
  isolation:isolate;
}

/* Tarama çizgisi */
.scan-line{
  position:absolute;left:0;width:100%;height:1px;z-index:20;
  background:linear-gradient(90deg,transparent 5%,var(--primary),var(--secondary),var(--energy),transparent 95%);
  opacity:0.4;
  animation:scanDown 6s linear infinite;
  pointer-events:none;
}
.scan-line-2{animation-delay:3s;opacity:0.2;height:1px;}
@keyframes scanDown{0%{top:-2px}100%{top:100%}}

/* Grid noktaları */
.grid-dots{
  position:absolute;inset:0;z-index:1;pointer-events:none;
  background-image:radial-gradient(rgba(255,255,255,0.03) 1px,transparent 1px);
  background-size:30px 30px;
}

/* ═══════════════ GALAKSİ LOGO BAR ═══════════════ */
.galaxy-logo-bar{
  grid-column:1/-1;
  position:relative;
  height:36px;
  background:linear-gradient(90deg,rgba(0,224,255,0.4),rgba(199,96,255,0.35),rgba(0,255,157,0.25),rgba(255,215,0,0.2));
  clip-path:polygon(0 0,100% 0,100% 100%,20px 100%);
  display:flex;align-items:center;padding:0 24px;gap:20px;
  z-index:15;overflow:hidden;
  backdrop-filter:blur(4px);
}
.galaxy-logo-bar::after{
  content:'';position:absolute;inset:0;
  background:linear-gradient(90deg,transparent,rgba(255,255,255,0.15),transparent);
  animation:logoShine 5s infinite;
}
@keyframes logoShine{0%{transform:translateX(-100%)}100%{transform:translateX(200%)}}

.logo-text{
  font-family:'Orbitron',sans-serif;font-size:13px;font-weight:800;
  letter-spacing:5px;color:#fff;
  text-shadow:0 0 20px rgba(0,224,255,0.6);
  text-transform:uppercase;position:relative;z-index:2;
}
.logo-text span{
  background:linear-gradient(90deg,var(--accent),var(--energy));
  -webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;
}

.live-badge{
  display:flex;align-items:center;gap:8px;
  background:rgba(0,255,157,0.12);
  border:1px solid rgba(0,255,157,0.4);
  border-radius:20px;padding:4px 14px;
  font-family:'Orbitron',sans-serif;font-size:10px;font-weight:700;
  color:var(--energy);letter-spacing:2px;
  text-shadow:0 0 10px var(--energy);
  position:relative;z-index:2;
}
.live-dot{
  width:8px;height:8px;border-radius:50%;
  background:var(--energy);
  box-shadow:0 0 10px var(--energy),0 0 20px var(--energy);
  animation:livePulse 1.2s infinite;
}
@keyframes livePulse{
  0%,100%{opacity:1;transform:scale(1)}
  50%{opacity:0.3;transform:scale(0.6)}
}

.listeners-badge{
  display:flex;align-items:center;gap:6px;
  background:rgba(0,224,255,0.1);
  border:1px solid rgba(0,224,255,0.3);
  border-radius:20px;padding:4px 12px;
  font-family:'Orbitron',sans-serif;font-size:9px;font-weight:600;
  color:var(--primary);letter-spacing:1.5px;
  position:relative;z-index:2;
}
.listeners-badge i{font-size:10px;}

/* ═══════════════ GEZEGEN BÖLÜMÜ ═══════════════ */
.planet-section{
  grid-row:2;
  position:relative;
  display:flex;align-items:center;justify-content:center;
  background:
    radial-gradient(circle at 50% 50%,rgba(199,96,255,0.2),transparent 70%),
    linear-gradient(180deg,#0c0025,#050010);
  padding:20px;
  overflow:hidden;
}

/* Gezegen sahnesi */
.planet-wrapper{
  position:relative;
  width:140px;height:140px;
  display:flex;align-items:center;justify-content:center;
}

/* Yörünge halkaları */
.orbit-ring{
  position:absolute;border-radius:50%;
  border:1px solid;
  top:50%;left:50%;
  transform:translate(-50%,-50%);
  animation:orbitSpin var(--speed,20s) linear infinite;
}
.orbit-ring:nth-child(1){
  width:110px;height:110px;
  border-color:rgba(0,224,255,0.3);
  --speed:12s;
}
.orbit-ring:nth-child(2){
  width:125px;height:125px;
  border-color:rgba(199,96,255,0.25);
  --speed:16s;
  animation-direction:reverse;
}
.orbit-ring:nth-child(3){
  width:140px;height:140px;
  border-color:rgba(0,255,157,0.2);
  --speed:22s;
}
.orbit-ring:nth-child(4){
  width:155px;height:155px;
  border-color:rgba(255,215,0,0.15);
  --speed:28s;
  animation-direction:reverse;
}
@keyframes orbitSpin{to{transform:translate(-50%,-50%) rotate(360deg)}}

/* Gezegen */
.planet{
  width:90px;height:90px;border-radius:50%;position:relative;
  background:
    radial-gradient(circle at 35% 30%,rgba(80,60,140,0.8),transparent 50%),
    radial-gradient(circle at 65% 70%,rgba(40,80,120,0.6),transparent 50%),
    conic-gradient(from 45deg,
      #1a3a6a,#2a1a5a 20%,#4a1a4a 40%,#5a2a3a 60%,
      #3a3a5a 80%,#1a4a6a);
  box-shadow:
    0 0 0 3px rgba(255,255,255,0.05),
    0 0 25px rgba(0,224,255,0.35),
    0 0 50px rgba(199,96,255,0.2),
    inset 0 0 25px rgba(0,0,0,0.7),
    inset -10px -5px 20px rgba(0,0,0,0.5);
  animation:planetTilt 30s linear infinite;
  overflow:hidden;z-index:5;
}
.planet.playing{animation-play-state:running;}
.planet.paused{animation-play-state:paused;}
@keyframes planetTilt{from{transform:rotate(0)}to{transform:rotate(360deg)}}

/* Gezegen yüzey detayları */
.planet .crater{
  position:absolute;border-radius:50%;
  background:rgba(255,255,255,0.06);
  box-shadow:inset 1px 1px 3px rgba(0,0,0,0.3);
}
.planet .crater:nth-child(1){width:18px;height:18px;top:20%;left:30%;}
.planet .crater:nth-child(2){width:12px;height:12px;top:55%;left:55%;}
.planet .crater:nth-child(3){width:15px;height:15px;top:35%;right:20%;}
.planet .crater:nth-child(4){width:8px;height:8px;bottom:25%;left:40%;}
.planet .crater:nth-child(5){width:20px;height:20px;top:15%;right:30%;opacity:0.4;}

/* Gezegen parlaklığı */
.planet::before{
  content:'';position:absolute;inset:0;border-radius:50%;
  background:linear-gradient(135deg,rgba(255,255,255,0.2) 0%,transparent 50%,rgba(0,0,0,0.3) 100%);
  z-index:2;
}
.planet::after{
  content:'';position:absolute;inset:0;border-radius:50%;
  background:radial-gradient(circle at 30% 30%,rgba(0,224,255,0.15),transparent 60%);
  animation:planetGlow 3s ease-in-out infinite;
  z-index:3;
}
@keyframes planetGlow{
  0%,100%{opacity:0.4}
  50%{opacity:0.9}
}

/* Gezegen etiketi */
.planet-label{
  position:absolute;bottom:8px;left:50%;transform:translateX(-50%);
  font-family:'Orbitron',sans-serif;font-size:8px;font-weight:600;
  letter-spacing:3px;color:rgba(255,255,255,0.3);
  text-transform:uppercase;white-space:nowrap;
  z-index:10;
}

/* ═══════════════ MERKEZİ İÇERİK ═══════════════ */
.center-content{
  grid-row:2;
  display:flex;flex-direction:column;
  padding:28px 24px 20px;
  gap:14px;
  position:relative;
  overflow:hidden;
}

/* Şarkı başlığı alanı */
.song-display{
  position:relative;
  padding:18px 22px;
  border-radius:16px;
  background:linear-gradient(135deg,rgba(255,255,255,0.03),rgba(255,255,255,0.01));
  border:1px solid var(--glass-border);
  overflow:hidden;
}
.song-display::before{
  content:'';position:absolute;inset:0;
  background:linear-gradient(90deg,transparent,rgba(0,224,255,0.05),transparent);
  animation:songShine 4s infinite;
}
@keyframes songShine{0%{transform:translateX(-100%)}100%{transform:translateX(100%)}}

.now-playing-label{
  display:inline-flex;align-items:center;gap:6px;
  font-family:'Orbitron',sans-serif;font-size:9px;font-weight:700;
  letter-spacing:3px;color:var(--energy);
  text-transform:uppercase;margin-bottom:8px;
  text-shadow:0 0 10px rgba(0,255,157,0.5);
}
.now-playing-label .eq-bars{
  display:inline-flex;gap:2px;align-items:flex-end;height:12px;
}
.now-playing-label .eq-bar{
  width:2px;border-radius:1px;
  background:var(--energy);
  animation:eqMini 0.6s ease-in-out infinite;
}
.now-playing-label .eq-bar:nth-child(1){height:4px;animation-delay:0s;}
.now-playing-label .eq-bar:nth-child(2){height:8px;animation-delay:0.15s;}
.now-playing-label .eq-bar:nth-child(3){height:6px;animation-delay:0.3s;}
.now-playing-label .eq-bar:nth-child(4){height:10px;animation-delay:0.1s;}
.now-playing-label .eq-bar:nth-child(5){height:5px;animation-delay:0.25s;}
@keyframes eqMini{
  0%,100%{height:3px;opacity:0.5}
  50%{height:12px;opacity:1}
}

.song-title{
  font-size:clamp(15px,2.2vw,22px);
  font-weight:700;
  letter-spacing:-0.3px;
  color:#fff;
  line-height:1.4;
  position:relative;z-index:2;
}
.song-title .highlight{
  background:linear-gradient(90deg,var(--primary),var(--secondary));
  -webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;
}

/* Meta bilgiler */
.meta-section{
  display:flex;align-items:center;gap:14px;flex-wrap:wrap;
}
.meta-chip{
  display:inline-flex;align-items:center;gap:6px;
  padding:6px 14px;border-radius:20px;
  background:rgba(255,255,255,0.04);
  border:1px solid rgba(255,255,255,0.08);
  font-size:11px;font-weight:500;
  color:rgba(255,255,255,0.7);
  transition:all 0.3s;
}
.meta-chip i{font-size:10px;}
.meta-chip.dj i{color:var(--primary);}
.meta-chip.quality{
  background:linear-gradient(135deg,rgba(0,224,255,0.1),rgba(199,96,255,0.08));
  border-color:rgba(0,224,255,0.2);
  font-family:'Orbitron',sans-serif;font-weight:700;
  font-size:10px;letter-spacing:1px;color:var(--primary);
}
.meta-chip.genre i{color:var(--secondary);}
.meta-chip.time i{color:var(--accent);}

/* Kontrol satırı */
.controls-row{
  display:flex;align-items:center;gap:16px;margin-top:4px;
}

/* Oynat butonu */
.play-container{
  position:relative;flex-shrink:0;
}
.play-ring{
  position:absolute;inset:-6px;border-radius:50%;
  background:conic-gradient(from var(--angle,0deg),var(--primary),var(--secondary),var(--energy),var(--primary));
  animation:spinAngle 4s linear infinite;
  opacity:0.6;filter:blur(4px);
}
.play-btn{
  position:relative;width:64px;height:64px;border-radius:50%;
  background:linear-gradient(145deg,#1a0d35,#0d0520);
  border:2px solid rgba(255,255,255,0.1);
  color:#fff;font-size:22px;
  cursor:pointer;display:flex;align-items:center;justify-content:center;
  transition:all 0.35s cubic-bezier(0.4,0,0.2,1);
  z-index:2;
  box-shadow:
    0 0 0 1px rgba(255,255,255,0.05),
    inset 0 2px 6px rgba(255,255,255,0.08),
    0 4px 20px rgba(0,0,0,0.5);
}
.play-btn:hover{
  transform:scale(1.12);
  border-color:var(--primary);
  box-shadow:0 0 30px rgba(0,224,255,0.3),0 0 60px rgba(0,224,255,0.1);
}
.play-btn:active{transform:scale(0.92);}
.play-btn i{position:relative;z-index:1;}

/* Ek oynat kontrolleri */
.secondary-controls{
  display:flex;gap:10px;flex-shrink:0;
}
.sec-btn{
  width:40px;height:40px;border-radius:12px;
  background:rgba(255,255,255,0.04);
  border:1px solid rgba(255,255,255,0.08);
  color:rgba(255,255,255,0.5);font-size:14px;
  cursor:pointer;display:flex;align-items:center;justify-content:center;
  transition:all 0.3s;
}
.sec-btn:hover{
  color:#fff;border-color:var(--primary);
  background:rgba(0,224,255,0.1);
  transform:translateY(-2px);
  box-shadow:0 4px 15px rgba(0,224,255,0.2);
}

/* Enerji dalgaları */
.wave-visualizer{
  flex:1;height:55px;
  display:flex;align-items:center;
  padding:0 8px;gap:0;
  position:relative;overflow:hidden;
  border-radius:12px;
  background:rgba(0,0,0,0.2);
}
.wave-bar{
  flex:1;border-radius:3px 3px 0 0;
  background:linear-gradient(to top,var(--w-color1),var(--w-color2));
  animation:waveRise var(--dur,1s) ease-in-out infinite;
  animation-play-state:paused;
  margin:0 1px;
  min-width:3px;
  box-shadow:0 0 6px var(--w-color1);
  opacity:0.7;
  transition:opacity 0.3s;
}
.wave-bar.active{
  animation-play-state:running;
  opacity:1;
}
.wave-bar:nth-child(odd){--w-color1:var(--primary);--w-color2:var(--secondary);}
.wave-bar:nth-child(even){--w-color1:var(--secondary);--w-color2:var(--energy);}
.wave-bar:nth-child(3n){--w-color1:var(--energy);--w-color2:var(--accent);}
.wave-bar:nth-child(5n){--w-color1:var(--pink);--w-color2:var(--primary);}
@keyframes waveRise{
  0%,100%{height:4px;opacity:0.3}
  50%{height:var(--maxH,40px);opacity:1}
}

/* Durum göstergeleri */
.status-badges{
  display:flex;flex-direction:column;gap:6px;align-items:flex-end;flex-shrink:0;
}
.status-pill{
  display:inline-flex;align-items:center;gap:5px;
  padding:4px 12px;border-radius:16px;
  font-family:'Orbitron',sans-serif;font-size:9px;font-weight:700;
  letter-spacing:1.5px;text-transform:uppercase;
}
.status-pill.live{
  background:rgba(0,255,157,0.1);border:1px solid rgba(0,255,157,0.3);color:var(--energy);
}
.status-pill.live i{animation:livePulse 1s infinite;font-size:8px;}
.status-pill.hd{
  background:rgba(0,224,255,0.1);border:1px solid rgba(0,224,255,0.3);color:var(--primary);
}
.status-pill.stereo{
  background:rgba(199,96,255,0.1);border:1px solid rgba(199,96,255,0.3);color:var(--secondary);
}

/* ═══════════════ SAĞ KONTROL PANELİ ═══════════════ */
.right-panel{
  grid-row:2;
  display:flex;flex-direction:column;
  align-items:center;justify-content:center;
  gap:14px;
  padding:24px 18px;
  border-left:1px solid var(--glass-border);
  background:rgba(0,0,0,0.15);
}

/* İstek butonu */
.request-btn{
  width:100%;
  display:flex;align-items:center;justify-content:center;gap:8px;
  padding:14px 16px;border-radius:14px;
  background:linear-gradient(135deg,rgba(0,224,255,0.2),rgba(199,96,255,0.15));
  border:1.5px solid rgba(0,224,255,0.3);
  color:#fff;font-size:11px;font-weight:700;
  font-family:'Orbitron',sans-serif;cursor:pointer;
  text-transform:uppercase;letter-spacing:2px;
  transition:all 0.35s;
  box-shadow:0 4px 20px rgba(0,224,255,0.15),inset 0 1px 0 rgba(255,255,255,0.1);
  position:relative;overflow:hidden;
}
.request-btn::before{
  content:'';position:absolute;top:-50%;left:-60%;width:50%;height:200%;
  background:linear-gradient(90deg,transparent,rgba(255,255,255,0.15),transparent);
  transform:skewX(-20deg);transition:left 0.5s;
}
.request-btn:hover::before{left:130%;}
.request-btn:hover{
  transform:translateY(-3px);
  border-color:var(--primary);
  box-shadow:0 8px 30px rgba(0,224,255,0.3),0 0 50px rgba(0,224,255,0.1);
}
.request-btn i{animation:planeBob 2s infinite;}
@keyframes planeBob{0%,100%{transform:translateY(0) rotate(0)}50%{transform:translateY(-2px) rotate(4deg)}}

/* Aksiyon butonları */
.action-grid{
  display:grid;grid-template-columns:1fr 1fr;gap:8px;width:100%;
}
.action-btn{
  height:44px;border-radius:12px;
  background:rgba(255,255,255,0.04);
  border:1px solid rgba(255,255,255,0.08);
  color:rgba(255,255,255,0.55);font-size:15px;
  cursor:pointer;display:flex;align-items:center;justify-content:center;
  transition:all 0.3s;position:relative;overflow:hidden;
}
.action-btn::after{
  content:'';position:absolute;inset:0;border-radius:12px;
  background:linear-gradient(135deg,var(--primary),var(--secondary));
  opacity:0;transition:opacity 0.3s;
}
.action-btn:hover::after{opacity:0.15;}
.action-btn:hover{
  color:#fff;border-color:var(--primary);
  transform:translateY(-2px) scale(1.05);
  box-shadow:0 4px 18px rgba(0,224,255,0.2);
}
.action-btn i{position:relative;z-index:1;}
.action-btn.liked{color:var(--pink);border-color:rgba(255,45,149,0.3);}
.action-btn.liked i{color:var(--pink);}

/* Ses kontrolü - Dikey */
.volume-section{
  display:flex;flex-direction:column;align-items:center;gap:8px;
  width:100%;
}
.vol-label{
  font-family:'Orbitron',sans-serif;font-size:9px;font-weight:700;
  letter-spacing:3px;color:rgba(255,255,255,0.3);text-transform:uppercase;
}
.vol-icon{
  font-size:18px;color:rgba(255,255,255,0.5);cursor:pointer;
  transition:all 0.3s;
}
.vol-icon:hover{color:var(--primary);transform:scale(1.2);filter:drop-shadow(0 0 10px var(--primary));}

.vol-track{
  position:relative;width:32px;height:80px;
  background:rgba(255,255,255,0.04);
  border-radius:18px;border:1px solid rgba(255,255,255,0.08);
  cursor:pointer;overflow:hidden;
}
.vol-fill{
  position:absolute;bottom:0;left:0;right:0;
  border-radius:18px;
  background:linear-gradient(to top,var(--primary),var(--secondary),var(--energy));
  transition:height 0.15s;
  box-shadow:0 0 12px var(--primary);
}
.vol-thumb{
  position:absolute;left:50%;transform:translateX(-50%);
  width:24px;height:24px;border-radius:50%;
  background:radial-gradient(circle at 35% 35%,#fff,var(--primary));
  box-shadow:0 0 15px var(--primary),0 2px 8px rgba(0,0,0,0.5);
  transition:bottom 0.15s;cursor:grab;pointer-events:none;
}
.vol-input{
  position:absolute;inset:0;opacity:0;cursor:pointer;
  writing-mode:vertical-lr;direction:rtl;
  -webkit-appearance:slider-vertical;width:100%;
}
.vol-pct{
  font-family:'Orbitron',sans-serif;font-size:10px;font-weight:700;
  color:var(--primary);text-shadow:0 0 10px var(--primary);
}

/* ═══════════════ ALTOBAR SİNYAL PANELİ ═══════════════ */
.signal-section{
  margin-top:18px;
  position:relative;border-radius:24px;
  padding:2px;
  background:conic-gradient(from var(--angle,0deg),var(--secondary),var(--primary),var(--energy),var(--pink),var(--secondary));
  animation:spinAngle 8s linear infinite;
  box-shadow:0 0 40px rgba(199,96,255,0.12),0 0 80px rgba(0,224,255,0.08);
}
.signal-inner{
  border-radius:22px;overflow:hidden;
  background:
    radial-gradient(ellipse at 0% 0%,rgba(199,96,255,0.15),transparent 50%),
    radial-gradient(ellipse at 100% 100%,rgba(0,224,255,0.1),transparent 50%),
    linear-gradient(165deg,rgba(8,3,18,0.99),rgba(3,1,10,0.99));
}

/* Sinyal başlık */
.sig-header{
  display:flex;align-items:center;gap:14px;
  padding:14px 22px;
  background:linear-gradient(135deg,var(--secondary),var(--primary),rgba(0,255,157,0.5));
  position:relative;overflow:hidden;
}
.sig-header::before{
  content:'';position:absolute;inset:0;
  background:linear-gradient(90deg,transparent,rgba(255,255,255,0.2),transparent);
  animation:logoShine 4s infinite;
}
.sig-header i{font-size:16px;color:#fff;position:relative;z-index:1;filter:drop-shadow(0 0 8px var(--primary));}
.sig-title{
  font-family:'Orbitron',sans-serif;font-size:11px;font-weight:700;
  letter-spacing:2.5px;color:#fff;text-transform:uppercase;flex:1;position:relative;z-index:1;
}
.sig-badge{
  background:rgba(0,255,157,0.15);border:1px solid rgba(0,255,157,0.4);
  border-radius:18px;padding:3px 12px;
  font-family:'Orbitron',sans-serif;font-size:9px;font-weight:700;
  color:var(--energy);letter-spacing:1.5px;position:relative;z-index:1;
  animation:badgeGlow 2s infinite;
}
@keyframes badgeGlow{
  0%,100%{box-shadow:0 0 0 0 rgba(0,255,157,0.4)}
  50%{box-shadow:0 0 0 5px rgba(0,255,157,0)}
}

/* Frekans analizör */
.freq-section{
  display:flex;height:55px;
  border-bottom:1px solid rgba(255,255,255,0.06);
}
.freq-brand{
  flex-shrink:0;width:95px;
  background:linear-gradient(135deg,var(--secondary),var(--primary));
  display:flex;flex-direction:column;align-items:center;justify-content:center;
  font-family:'Orbitron',sans-serif;
  box-shadow:6px 0 20px rgba(199,96,255,0.4);z-index:3;
}
.freq-brand span{font-size:15px;font-weight:900;color:var(--primary);text-shadow:0 0 12px var(--primary);}
.freq-brand small{font-size:8px;font-weight:600;letter-spacing:2px;color:rgba(255,255,255,0.7);text-transform:uppercase;}

.freq-visual{
  flex:1;position:relative;overflow:hidden;
  display:flex;align-items:center;gap:2px;padding:8px 12px;
  background:rgba(0,0,0,0.4);
}
.f-bar{
  flex:1;border-radius:3px 3px 0 0;
  background:linear-gradient(to top,var(--fb-c),transparent);
  animation:barPulse var(--dur,0.7s) ease-in-out infinite;
  animation-play-state:paused;
  min-width:2px;box-shadow:0 0 8px var(--fb-c);
  opacity:0.5;transition:opacity 0.3s;
}
.f-bar.active{animation-play-state:running;opacity:1;}
.f-bar:nth-child(3n+1){--fb-c:var(--primary);}
.f-bar:nth-child(3n+2){--fb-c:var(--secondary);}
.f-bar:nth-child(3n){--fb-c:var(--energy);}
.f-bar:nth-child(5n){--fb-c:var(--pink);}
@keyframes barPulse{0%,100%{height:3px}50%{height:var(--maxH,30px)}}

/* Ticker */
.freq-ticker-wrap{
  flex-shrink:0;width:250px;overflow:hidden;
  border-left:1px solid rgba(255,255,255,0.06);
  display:flex;align-items:center;position:relative;
}
.freq-ticker-wrap::before,.freq-ticker-wrap::after{
  content:'';position:absolute;top:0;bottom:0;width:25px;z-index:5;
}
.freq-ticker-wrap::before{left:0;background:linear-gradient(90deg,rgba(0,0,0,0.6),transparent);}
.freq-ticker-wrap::after{right:0;background:linear-gradient(-90deg,rgba(0,0,0,0.6),transparent);}
.ticker-track{
  display:inline-flex;white-space:nowrap;
  animation:tickerScroll 30s linear infinite;
  padding-left:50px;
}
@keyframes tickerScroll{0%{transform:translateX(0)}100%{transform:translateX(-50%)}}
.ticker-item{
  padding:0 20px;font-size:11px;font-weight:500;
  color:rgba(255,255,255,0.7);
  display:flex;align-items:center;gap:6px;
}
.ticker-item i{font-size:9px;color:var(--accent);}

/* Mesaj alanı */
.msg-area{
  padding:10px 16px;
  background:rgba(0,0,0,0.2);
  min-height:60px;
}

/* ═══════════════ İSTATİSTİK KARTLARI ═══════════════ */
.stats-row{
  margin-top:18px;
  display:grid;
  grid-template-columns:repeat(auto-fit,minmax(200px,1fr));
  gap:14px;
}
.stat-card{
  position:relative;border-radius:18px;padding:2px;
  background:linear-gradient(135deg,var(--glass-border),rgba(255,255,255,0.02));
  transition:all 0.35s;
}
.stat-card:hover{
  transform:translateY(-4px);
  box-shadow:0 8px 30px rgba(0,224,255,0.1);
}
.stat-card-inner{
  border-radius:16px;padding:18px 20px;
  background:
    radial-gradient(ellipse at 100% 0%,var(--sc-glow,rgba(0,224,255,0.08)),transparent 60%),
    linear-gradient(165deg,rgba(10,5,25,0.95),rgba(5,2,15,0.95));
  display:flex;align-items:center;gap:14px;
}
.stat-icon{
  width:44px;height:44px;border-radius:14px;
  background:linear-gradient(135deg,var(--sc-bg1),var(--sc-bg2));
  display:flex;align-items:center;justify-content:center;
  font-size:18px;flex-shrink:0;
  box-shadow:0 4px 15px rgba(0,0,0,0.3);
}
.stat-info{flex:1;}
.stat-info .stat-value{
  font-family:'Orbitron',sans-serif;font-size:18px;font-weight:800;
  letter-spacing:0.5px;
}
.stat-info .stat-label{
  font-size:10px;font-weight:500;
  color:rgba(255,255,255,0.4);
  letter-spacing:1px;text-transform:uppercase;margin-top:2px;
}

.stat-card:nth-child(1){--sc-glow:rgba(0,224,255,0.08);--sc-bg1:rgba(0,224,255,0.2);--sc-bg2:rgba(0,224,255,0.05);}
.stat-card:nth-child(1) .stat-value{color:var(--primary);text-shadow:0 0 12px rgba(0,224,255,0.5);}
.stat-card:nth-child(1) .stat-icon{color:var(--primary);}
.stat-card:nth-child(2){--sc-glow:rgba(199,96,255,0.08);--sc-bg1:rgba(199,96,255,0.2);--sc-bg2:rgba(199,96,255,0.05);}
.stat-card:nth-child(2) .stat-value{color:var(--secondary);text-shadow:0 0 12px rgba(199,96,255,0.5);}
.stat-card:nth-child(2) .stat-icon{color:var(--secondary);}
.stat-card:nth-child(3){--sc-glow:rgba(0,255,157,0.08);--sc-bg1:rgba(0,255,157,0.2);--sc-bg2:rgba(0,255,157,0.05);}
.stat-card:nth-child(3) .stat-value{color:var(--energy);text-shadow:0 0 12px rgba(0,255,157,0.5);}
.stat-card:nth-child(3) .stat-icon{color:var(--energy);}
.stat-card:nth-child(4){--sc-glow:rgba(255,215,0,0.08);--sc-bg1:rgba(255,215,0,0.2);--sc-bg2:rgba(255,215,0,0.05);}
.stat-card:nth-child(4) .stat-value{color:var(--accent);text-shadow:0 0 12px rgba(255,215,0,0.5);}
.stat-card:nth-child(4) .stat-icon{color:var(--accent);}

/* ═══════════════ MODAL ═══════════════ */
.modal-overlay{
  display:none;position:fixed;inset:0;
  background:rgba(0,0,20,0.92);
  backdrop-filter:blur(40px) saturate(150%);
  z-index:99999;justify-content:center;align-items:center;
}
.modal-overlay.open{display:flex;animation:fadeIn 0.35s;}
@keyframes fadeIn{from{opacity:0}to{opacity:1}}

.modal-box{
  position:relative;width:94%;max-width:750px;
  border-radius:28px;padding:2.5px;
  background:conic-gradient(from var(--angle,0deg),var(--secondary),var(--primary),var(--energy),var(--pink),var(--secondary));
  animation:spinAngle 3s linear infinite,modalSlide 0.5s cubic-bezier(0.4,0,0.2,1);
  box-shadow:
    0 30px 90px rgba(0,0,0,0.95),
    0 0 100px rgba(0,224,255,0.3),
    0 0 200px rgba(199,96,255,0.15);
}
@keyframes modalSlide{from{transform:scale(0.8) translateY(60px);opacity:0}to{transform:scale(1) translateY(0);opacity:1}}

.modal-body{
  border-radius:26px;overflow:hidden;
  background:
    radial-gradient(ellipse at top left,rgba(199,96,255,0.35),transparent 50%),
    radial-gradient(ellipse at bottom right,rgba(0,224,255,0.3),transparent 50%),
    rgba(4,0,12,0.98);
}
.modal-top{
  display:flex;align-items:center;justify-content:space-between;
  padding:18px 24px;
  background:linear-gradient(135deg,var(--secondary),var(--primary),rgba(0,255,157,0.5));
  position:relative;overflow:hidden;
}
.modal-top::before{
  content:'';position:absolute;inset:0;
  background:linear-gradient(90deg,transparent,rgba(255,255,255,0.2),transparent);
  animation:logoShine 4s infinite;
}
.modal-top h2{
  font-family:'Orbitron',sans-serif;font-size:16px;font-weight:800;
  color:#fff;display:flex;align-items:center;gap:10px;
  text-transform:uppercase;letter-spacing:2px;z-index:1;
}
.modal-top h2 i{animation:planeBob 2s infinite;}
.modal-x{
  width:40px;height:40px;border-radius:12px;
  background:rgba(255,255,255,0.1);
  border:2px solid rgba(255,255,255,0.2);
  color:#fff;font-size:18px;cursor:pointer;
  display:flex;align-items:center;justify-content:center;
  transition:0.3s;z-index:1;
}
.modal-x:hover{
  background:rgba(0,224,255,0.3);
  transform:rotate(90deg);
  box-shadow:0 0 20px rgba(0,224,255,0.4);
}
.modal-iframe{
  width:100%;height:65vh;border:none;background:#000;
}

/* ═══════════════ TOAST ═══════════════ */
.toast{
  position:fixed;bottom:28px;right:28px;
  padding:14px 22px;border-radius:16px;
  background:linear-gradient(135deg,rgba(199,96,255,0.95),rgba(0,224,255,0.9));
  border:1px solid rgba(255,255,255,0.15);
  color:#fff;font-weight:600;font-size:13px;
  box-shadow:0 12px 40px rgba(0,0,0,0.6),0 0 50px rgba(0,224,255,0.3);
  z-index:999999;
  display:flex;align-items:center;gap:10px;
  transform:translateY(120px) scale(0.9);opacity:0;
  transition:all 0.4s cubic-bezier(0.4,0,0.2,1);
  backdrop-filter:blur(20px);
}
.toast.show{transform:translateY(0) scale(1);opacity:1;}
.toast i{font-size:16px;color:var(--energy);}

/* ═══════════════ RESPONSIVE ═══════════════ */
@media(max-width:900px){
  .galactic-panel{
    grid-template-columns:150px 1fr;
    grid-template-rows:auto auto auto;
  }
  .planet-section{grid-column:1;grid-row:2;}
  .center-content{grid-column:2;grid-row:2;}
  .right-panel{
    grid-column:1/-1;grid-row:3;
    flex-direction:row;flex-wrap:wrap;
    justify-content:center;
    border-left:none;border-top:1px solid var(--glass-border);
    padding:14px 18px;
  }
  .volume-section{flex-direction:row;width:auto;gap:12px;}
  .vol-track{width:100px;height:28px;border-radius:20px;}
  .vol-fill{bottom:unset;left:0;top:0;height:100%!important;width:var(--vw,75%);border-radius:20px;}
  .vol-thumb{bottom:unset!important;top:50%;transform:translate(-50%,-50%);left:var(--vw,75%);}
  .vol-input{writing-mode:unset;direction:unset;-webkit-appearance:none;height:100%;width:100%;}
  .freq-ticker-wrap{display:none;}
}

@media(max-width:600px){
  .main-container{padding:12px;}
  .galactic-panel{grid-template-columns:1fr;grid-template-rows:auto auto auto auto;}
  .galaxy-logo-bar{clip-path:none;}
  .planet-section{grid-column:1;grid-row:2;padding:16px;}
  .center-content{grid-column:1;grid-row:3;padding:16px;}
  .right-panel{grid-column:1;grid-row:4;}
  .stats-row{grid-template-columns:1fr 1fr;}
  .song-title{font-size:14px;}
}
</style>
</head>
<body>

<!-- KOSMİK ARKA PLAN -->
<div class="cosmic-bg">
  <div class="nebula nebula-1"></div>
  <div class="nebula nebula-2"></div>
  <div class="nebula nebula-3"></div>
  <div class="bg-stars"></div>
  <div class="shooting-star" style="top:8%;left:0;--dur:5s;animation-delay:0s;"></div>
  <div class="shooting-star" style="top:25%;left:0;--dur:4s;animation-delay:2s;"></div>
  <div class="shooting-star" style="top:55%;left:0;--dur:6s;animation-delay:4s;"></div>
  <div class="shooting-star" style="top:75%;left:0;--dur:3.5s;animation-delay:1s;"></div>
  <div class="shooting-star" style="top:40%;left:0;--dur:5.5s;animation-delay:6s;"></div>
</div>

<!-- TOAST -->
<div class="toast" id="toast">
  <i class="fas fa-check-circle" id="toastIcon"></i>
  <span id="toastTxt">İşlem başarılı!</span>
</div>

<!-- MODAL -->
<div class="modal-overlay" id="modal">
  <div class="modal-box">
    <div class="modal-body">
      <div class="modal-top">
        <h2><i class="fas fa-paper-plane"></i> Şarkı İsteği</h2>
        <button class="modal-x" id="modalClose"><i class="fas fa-times"></i></button>
      </div>
      <iframe src="about:blank" class="modal-iframe" title="İstek Formu"></iframe>
    </div>
  </div>
</div>

<!-- ANA İÇERİK -->
<div class="main-container">

  <!-- BAŞLIK -->
  <div class="galaxy-header">
    <h1>Galactic Wave Radio</h1>
    <p class="subtitle">Uzay Frekanslarında Sınırsız Müzik</p>
    <div class="header-line"></div>
  </div>

  <!-- GALAKTİK PANEL -->
  <div class="cosmic-frame">
    <div class="galactic-panel" id="galPanel">

      <div class="scan-line"></div>
      <div class="scan-line scan-line-2"></div>
      <div class="grid-dots"></div>

      <!-- LOGO BAR -->
      <div class="galaxy-logo-bar">
        <div class="logo-text">GALACTIC <span>WAVE</span></div>
        <div class="live-badge">
          <div class="live-dot"></div>
          CANLI
        </div>
        <div class="listeners-badge">
          <i class="fas fa-headphones"></i>
          <span id="listenerCount">1.247</span> dinleyici
        </div>
      </div>

      <!-- GEZEGEN BÖLÜMÜ -->
      <div class="planet-section">
        <div class="planet-wrapper">
          <div class="orbit-ring"></div>
          <div class="orbit-ring"></div>
          <div class="orbit-ring"></div>
          <div class="orbit-ring"></div>
          <div class="planet paused" id="planet">
            <div class="crater"></div>
            <div class="crater"></div>
            <div class="crater"></div>
            <div class="crater"></div>
            <div class="crater"></div>
          </div>
        </div>
        <div class="planet-label">Galaktik Merkez</div>
      </div>

      <!-- MERKEZ İÇERİK -->
      <div class="center-content">

        <!-- Şarkı -->
        <div class="song-display">
          <div class="now-playing-label">
            <div class="eq-bars">
              <div class="eq-bar"></div><div class="eq-bar"></div>
              <div class="eq-bar"></div><div class="eq-bar"></div>
              <div class="eq-bar"></div>
            </div>
            Şimdi Çalıyor
          </div>
          <div class="song-title" id="songTitle">
            <span class="highlight">Cosmic Journey</span> — Stellar Mix Vol. 7
          </div>
        </div>

        <!-- Meta -->
        <div class="meta-section">
          <div class="meta-chip dj">
            <i class="fas fa-microphone-alt"></i>
            <span id="djName">DJ Nebula</span>
          </div>
          <div class="meta-chip quality">
            <i class="fas fa-bolt"></i>
            320 KBPS
          </div>
          <div class="meta-chip genre">
            <i class="fas fa-music"></i>
            <span id="genreLabel">Electronic · Space</span>
          </div>
          <div class="meta-chip time">
            <i class="far fa-clock"></i>
            <span id="timeLabel">00:00</span>
          </div>
        </div>

        <!-- Kontroller -->
        <div class="controls-row">
          <div class="play-container">
            <div class="play-ring"></div>
            <button class="play-btn" id="playBtn">
              <i class="fas fa-play" id="playIcon"></i>
            </button>
          </div>

          <div class="secondary-controls">
            <button class="sec-btn" id="prevBtn" title="Önceki">
              <i class="fas fa-backward-step"></i>
            </button>
            <button class="sec-btn" id="nextBtn" title="Sonraki">
              <i class="fas fa-forward-step"></i>
            </button>
          </div>

          <div class="wave-visualizer" id="waveViz">
            <!-- JS ile doldurulacak -->
          </div>

          <div class="status-badges">
            <div class="status-pill live">
              <i class="fas fa-satellite-dish"></i> CANLI
            </div>
            <div class="status-pill hd">
              <i class="fas fa-gem"></i> HD
            </div>
            <div class="status-pill stereo">
              <i class="fas fa-sliders-h"></i> STEREO
            </div>
          </div>
        </div>
      </div>

      <!-- SAĞ PANEL -->
      <div class="right-panel">
        <button class="request-btn" id="reqBtn">
          <i class="fas fa-paper-plane"></i>
          <span>İstek Gönder</span>
        </button>

        <div class="action-grid">
          <button class="action-btn" id="shareBtn" title="Paylaş">
            <i class="fas fa-share-nodes"></i>
          </button>
          <button class="action-btn" id="likeBtn" title="Beğen">
            <i class="far fa-heart"></i>
          </button>
          <button class="action-btn" id="favBtn" title="Favori">
            <i class="far fa-star"></i>
          </button>
          <button class="action-btn" id="infoBtn" title="Bilgi">
            <i class="fas fa-circle-info"></i>
          </button>
        </div>

        <div class="volume-section">
          <div class="vol-label">SES</div>
          <i class="fas fa-volume-up vol-icon" id="volIcon"></i>
          <div class="vol-track" id="volTrack">
            <div class="vol-fill" id="volFill" style="height:75%"></div>
            <div class="vol-thumb" id="volThumb" style="bottom:calc(75% - 12px)"></div>
            <input type="range" class="vol-input" id="volInput" min="0" max="100" value="75">
          </div>
          <span class="vol-pct" id="volPct">75%</span>
        </div>
      </div>

    </div>
  </div>

  <!-- SİNYAL PANELİ -->
  <div class="signal-section">
    <div class="signal-inner">
      <div class="sig-header">
        <i class="fas fa-wave-square"></i>
        <span class="sig-title">Frekans Analizi & Yayın Akışı</span>
        <div class="sig-badge">AKTİF</div>
      </div>
      <div class="freq-section">
        <div class="freq-brand">
          <span>FM</span>
          <small>Galaxy</small>
        </div>
        <div class="freq-visual" id="freqVisual">
          <!-- JS -->
        </div>
        <div class="freq-ticker-wrap">
          <div class="ticker-track" id="tickerTrack">
            <!-- JS -->
          </div>
        </div>
      </div>
      <div class="msg-area">
        <iframe src="about:blank" style="width:100%;height:60px;border:none;background:transparent;" scrolling="no" title="Mesajlar"></iframe>
      </div>
    </div>
  </div>

  <!-- İSTATİSTİK KARTLARI -->
  <div class="stats-row">
    <div class="stat-card">
      <div class="stat-card-inner">
        <div class="stat-icon"><i class="fas fa-users"></i></div>
        <div class="stat-info">
          <div class="stat-value" id="statListeners">1.247</div>
          <div class="stat-label">Aktif Dinleyici</div>
        </div>
      </div>
    </div>
    <div class="stat-card">
      <div class="stat-card-inner">
        <div class="stat-icon"><i class="fas fa-music"></i></div>
        <div class="stat-info">
          <div class="stat-value" id="statPlayed">842</div>
          <div class="stat-label">Bugün Çalınan</div>
        </div>
      </div>
    </div>
    <div class="stat-card">
      <div class="stat-card-inner">
        <div class="stat-icon"><i class="fas fa-signal"></i></div>
        <div class="stat-info">
          <div class="stat-value">99.8%</div>
          <div class="stat-label">Sinyal Gücü</div>
        </div>
      </div>
    </div>
    <div class="stat-card">
      <div class="stat-card-inner">
        <div class="stat-icon"><i class="fas fa-clock"></i></div>
        <div class="stat-info">
          <div class="stat-value" id="statUptime">24/7</div>
          <div class="stat-label">Kesintisiz Yayın</div>
        </div>
      </div>
    </div>
  </div>

</div>

<script>
// ═══════════ AUDIO ═══════════
const audio = new Audio('https://radyo.example/stream');
audio.volume = 0.75;
let isPlaying = false;

// ═══════════ ELEMENTS ═══════════
const $ = id => document.getElementById(id);
const playBtn = $('playBtn'), playIcon = $('playIcon');
const planet = $('planet');
const waveViz = $('waveViz');
const songTitle = $('songTitle');
const toast = $('toast'), toastTxt = $('toastTxt'), toastIcon = $('toastIcon');
const modal = $('modal');
const volInput = $('volInput'), volFill = $('volFill'), volThumb = $('volThumb'), volPct = $('volPct'), volIcon = $('volIcon');

// ═══════════ WAVE BARS ═══════════
for (let i = 0; i < 35; i++) {
  const bar = document.createElement('div');
  bar.className = 'wave-bar';
  const maxH = Math.random() * 30 + 15;
  const dur = Math.random() * 0.6 + 0.5;
  bar.style.cssText = `--maxH:${maxH}px;--dur:${dur}s;animation-delay:${(i * 0.04 % dur)}s;`;
  waveViz.appendChild(bar);
}

// ═══════════ FREQ BARS ═══════════
const freqVisual = $('freqVisual');
for (let i = 0; i < 50; i++) {
  const bar = document.createElement('div');
  bar.className = 'f-bar';
  const maxH = Math.random() * 28 + 8;
  const dur = Math.random() * 0.5 + 0.3;
  bar.style.cssText = `--maxH:${maxH}px;--dur:${dur}s;animation-delay:${(i * 0.035 % dur)}s;`;
  freqVisual.appendChild(bar);
}

// ═══════════ TICKER ═══════════
const tickerTrack = $('tickerTrack');
const tickerMsgs = [
  '🌌 Bugün uzay frekanslarımız zirvede!',
  '💫 En iyi elektronik müzik Galactic Wave\'te',
  '📡 Sinyal gücü: %99.8 — Mükemmel',
  '🚀 İsteklerinizi evrenin dört bir yanına gönderin',
  '🌠 Her frekansta yeni bir macera',
  '✨ Galactic Wave — Müziğin ötesinde',
  '🎧 Bugün 1.247+ dinleyici seninle',
  '💜 Uzayda müzik asla durmaz',
];
function buildTicker(msgs) {
  const all = [...msgs, ...msgs];
  tickerTrack.innerHTML = all.map(m =>
    `<div class="ticker-item"><i class="fas fa-star"></i>${m}</div>`
  ).join('');
}
buildTicker(tickerMsgs);

// ═══════════ PLAY STATE ═══════════
function setPlayState(active) {
  const method = active ? 'add' : 'remove';
  planet.classList[active ? 'remove' : 'add']('paused');
  planet.classList[active ? 'add' : 'remove']('playing');
  playIcon.className = active ? 'fas fa-pause' : 'fas fa-play';

  document.querySelectorAll('.wave-bar').forEach(b => b.classList.toggle('active', active));
  document.querySelectorAll('.f-bar').forEach(b => b.classList.toggle('active', active));
}

playBtn.addEventListener('click', () => {
  isPlaying = !isPlaying;
  if (isPlaying) audio.play().catch(() => {});
  else audio.pause();
  setPlayState(isPlaying);
});

// ═══════════ VOLUME ═══════════
function setVol(v) {
  v = Math.max(0, Math.min(100, Math.round(v)));
  audio.volume = v / 100;
  volFill.style.height = v + '%';
  volThumb.style.bottom = `calc(${v}% - 12px)`;
  volPct.textContent = v + '%';
  volInput.value = v;
  volIcon.className = v === 0 ? 'fas fa-volume-mute vol-icon'
    : v < 30 ? 'fas fa-volume-down vol-icon'
    : 'fas fa-volume-up vol-icon';
}
setVol(75);
volInput.addEventListener('input', e => setVol(+e.target.value));
volIcon.addEventListener('click', () => setVol(audio.volume > 0 ? 0 : 75));

// ═══════════ MODAL ═══════════
$('reqBtn').addEventListener('click', () => modal.classList.add('open'));
$('modalClose').addEventListener('click', () => modal.classList.remove('open'));
modal.addEventListener('click', e => { if (e.target === modal) modal.classList.remove('open'); });
document.addEventListener('keydown', e => { if (e.key === 'Escape') modal.classList.remove('open'); });

// ═══════════ TOAST ═══════════
function showToast(msg, icon = 'fa-check-circle') {
  toastTxt.textContent = msg;
  toastIcon.className = 'fas ' + icon;
  toast.classList.add('show');
  clearTimeout(toast._t);
  toast._t = setTimeout(() => toast.classList.remove('show'), 3500);
}

// ═══════════ ACTION BUTTONS ═══════════
$('shareBtn').addEventListener('click', () => {
  const data = { title: 'Galactic Wave Radio', text: '🎵 ' + songTitle.textContent.trim(), url: location.href };
  if (navigator.share) navigator.share(data).catch(() => {});
  else navigator.clipboard.writeText(location.href).then(() => showToast('🔗 Link kopyalandı!', 'fa-link'));
});

let liked = false;
$('likeBtn').addEventListener('click', function () {
  liked = !liked;
  this.querySelector('i').className = liked ? 'fas fa-heart' : 'far fa-heart';
  this.classList.toggle('liked', liked);
  showToast(liked ? '❤️ Favorilere eklendi!' : '💔 Favorilerden çıkarıldı!', liked ? 'fa-heart' : 'fa-heart-crack');
});

let favStar = false;
$('favBtn').addEventListener('click', function () {
  favStar = !favStar;
  this.querySelector('i').className = favStar ? 'fas fa-star' : 'far fa-star';
  this.classList.toggle('liked', favStar);
  showToast(favStar ? '⭐ Yıldızlandı!' : 'Yıldız kaldırıldı', favStar ? 'fa-star' : 'fa-star-half-stroke');
});

$('infoBtn').addEventListener('click', () => {
  showToast('📡 Galactic Wave Radio — 7/24 uzay frekanslarında', 'fa-satellite');
});

// ═══════════ CLOCK ═══════════
function updateClock() {
  const now = new Date();
  const h = String(now.getHours()).padStart(2, '0');
  const m = String(now.getMinutes()).padStart(2, '0');
  const s = String(now.getSeconds()).padStart(2, '0');
  $('timeLabel').textContent = h + ':' + m + ':' + s;
}
updateClock();
setInterval(updateClock, 1000);

// ═══════════ LISTENER SIM ═══════════
let listeners = 1247;
setInterval(() => {
  listeners += Math.floor(Math.random() * 7) - 3;
  listeners = Math.max(1100, listeners);
  const fmt = listeners.toLocaleString('tr-TR');
  $('listenerCount').textContent = fmt;
  $('statListeners').textContent = fmt;
}, 5000);

// ═══════════ SONG TITLE MARQUEE CHECK ═══════════
function checkMarquee() {
  const el = songTitle;
  if (el.scrollWidth > el.parentElement.clientWidth) {
    const text = el.innerHTML;
    el.innerHTML = text + ' &nbsp;&nbsp;&nbsp; ' + text;
    el.style.animation = 'marquee 18s linear infinite';
  }
}

// Marquee keyframes ekle
const marqueeStyle = document.createElement('style');
marqueeStyle.textContent = `@keyframes marquee{0%{transform:translateX(0)}100%{transform:translateX(-50%)}}`;
document.head.appendChild(marqueeStyle);

setTimeout(checkMarquee, 500);

// ═══════════ FETCH RADIO INFO ═══════════
function decodeHtml(html) {
  const t = document.createElement('textarea');
  t.innerHTML = html;
  return t.value;
}

async function fetchInfo() {
  try {
    const data = {
      title: "Cosmic Journey — Stellar Mix Vol. 7",
      dj: "DJ Nebula",
      genre: "Electronic · Space Ambient"
    };
    if (data.title) {
      songTitle.innerHTML = `<span class="highlight">${decodeHtml(data.title)}</span>`;
      setTimeout(checkMarquee, 100);
    }
    if (data.dj) $('djName').textContent = decodeHtml(data.dj);
    if (data.genre) $('genreLabel').textContent = decodeHtml(data.genre);
  } catch (e) { /* sessiz */ }
}
fetchInfo();
setInterval(fetchInfo, 15000);
</script>
</body>
</html>
```

## ✨ Yapılan Temel Geliştirmeler

| Özellik | Açıklama |
|---|---|
| **Kozmik arka plan** | Nebula bulutları, kayan yıldızlar, parallax yıldız alanı |
| **Gelişmiş gezegen** | Krater detayları, 4 yörünge halkası, atmosferik parıltı |
| **İstatistik kartları** | Dinleyici, çalınan şarkı, sinyal gücü, yayın süresi |
| **Canlı saat** | Sol-altta saniyeye kadar gerçek zamanlı saat |
| **Dinleyici simülasyonu** | Her 5 saniyede dinleyici sayısı değişir |
| **Marquee şarkı adı** | Uzun şarkı adları otomatik kayar |
| **HD / STEREO etiketleri** | Yayın kalitesi rozetleri |
| **Shooting stars** | Arkaplanda kayan yıldız efektleri |
| **Gelişmiş ses kontrolü** | Daha büyük ve görsel dikey slider |
| **4lü aksiyon butonu** | Beğen, paylaş, favori, bilgi — grid düzen |
| **Kompakt responsive** | Mobilde tek kolon, tablette iki kolon |