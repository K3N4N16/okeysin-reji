# Okeysin İmaj FM Player V2

## Prompt 1

### You
*2026-03-15 14:43:28 +03*

<!DOCTYPE html>
<html lang="tr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>okeysin İmaj FM</title>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
<style>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Space+Grotesk:wght@300;400;500;600;700;800&display=swap');

:root{
  --pk:#ff006e;--cy:#00f5ff;--pu:#8338ec;
  --gn:#39ff14;--gd:#ffd700;--or:#ff6b35;
  --bg:#05050d;
}
/* TEMA DEĞİŞKENLERİ */
[data-theme="neon"]{--pk:#ff006e;--cy:#00f5ff;--pu:#8338ec;--gn:#39ff14;--gd:#ffd700;--or:#ff6b35;}
[data-theme="sunset"]{--pk:#ff4500;--cy:#ff8c00;--pu:#dc143c;--gn:#ff6347;--gd:#ffa500;--or:#ff7f50;}
[data-theme="ocean"]{--pk:#0077b6;--cy:#00b4d8;--pu:#023e8a;--gn:#48cae4;--gd:#90e0ef;--or:#0096c7;}
[data-theme="forest"]{--pk:#2d6a4f;--cy:#52b788;--pu:#1b4332;--gn:#95d5b2;--gd:#b7e4c7;--or:#40916c;}
[data-theme="purple"]{--pk:#e040fb;--cy:#d500f9;--pu:#aa00ff;--gn:#ea80fc;--gd:#ce93d8;--or:#ba68c8;}
[data-theme="retro"]{--pk:#f72585;--cy:#4cc9f0;--pu:#7209b7;--gn:#4895ef;--gd:#f3722c;--or:#f94144;}

*{margin:0;padding:0;box-sizing:border-box;}
body{background:transparent;font-family:'Space Grotesk',sans-serif;}

@property --angle{syntax:'<angle>';initial-value:0deg;inherits:false;}
@keyframes spinAngle{to{--angle:360deg;}}

/* ══════ HOLO ÇERÇEVE ══════ */
.holo-frame{
  position:relative;border-radius:28px;padding:1.5px;
  background:conic-gradient(from var(--angle),
    var(--pu),var(--pk),var(--cy),var(--gd),var(--pk),var(--pu));
  animation:spinAngle 4s linear infinite;
  box-shadow:0 0 60px rgba(255,0,110,.35),0 0 120px rgba(131,56,236,.2);
  transition: all 0.5s;
}

/* ══════ ANA PLAYER ══════ */
.player{
  position:relative;
  background:
    radial-gradient(ellipse 70% 120% at 15% 50%,rgba(131,56,236,.25) 0%,transparent 60%),
    radial-gradient(ellipse 60% 120% at 85% 50%,rgba(255,0,110,.22) 0%,transparent 60%),
    radial-gradient(ellipse 100% 70% at 50% -5%,rgba(0,245,255,.15) 0%,transparent 55%),
    linear-gradient(160deg,rgba(14,10,28,.99) 0%,rgba(6,4,14,.99) 100%);
  border-radius:27px;
  overflow:hidden;
  display:grid;
  grid-template-columns:138px 1fr auto auto;
  align-items:stretch;
  min-height:130px;
  isolation:isolate;
  transition: all 0.5s;
}

.player::before{
  content:'';position:absolute;inset:0;border-radius:27px;pointer-events:none;z-index:1;
  background:repeating-linear-gradient(0deg,transparent 0,transparent 3px,rgba(0,245,255,.014) 3px,rgba(0,245,255,.014) 4px);
}
.sweep{
  position:absolute;top:0;left:-100%;width:55%;height:100%;
  background:linear-gradient(90deg,transparent,rgba(255,255,255,.035),transparent);
  animation:sweepAn 9s infinite ease-in-out;pointer-events:none;z-index:2;
}
@keyframes sweepAn{0%,100%{left:-100%}55%{left:160%}}

/* ══════ LOGO ŞERİDİ ══════ */
.logo-strip{
  position:absolute;top:0;left:136px;right:0;height:27px;z-index:10;
  background:linear-gradient(90deg,rgba(131,56,236,.6),rgba(255,0,110,.45),rgba(0,245,255,.35));
  clip-path:polygon(0 0,100% 0,100% 100%,14px 100%);
  display:flex;align-items:center;padding:0 20px;gap:10px;overflow:hidden;
}
.logo-strip::after{
  content:'';position:absolute;inset:0;
  background:linear-gradient(90deg,transparent,rgba(255,255,255,.18),transparent);
  animation:lsShine 3.5s infinite;
}
@keyframes lsShine{0%{transform:translateX(-100%)}100%{transform:translateX(220%)}}
.logo-name{
  font-family:'Orbitron',sans-serif;font-size:10px;font-weight:900;
  letter-spacing:3px;color:#fff;text-transform:uppercase;
  text-shadow:0 0 18px rgba(0,245,255,.9);position:relative;z-index:1;
}
.live-badge{
  display:flex;align-items:center;gap:5px;
  background:rgba(57,255,20,.15);border:1px solid rgba(57,255,20,.55);
  border-radius:20px;padding:2px 9px;
  font-size:8px;font-weight:700;font-family:'Orbitron',sans-serif;
  color:var(--gn);letter-spacing:1.5px;text-shadow:0 0 10px var(--gn);
  position:relative;z-index:1;
}
.live-dot{width:6px;height:6px;border-radius:50%;background:var(--gn);box-shadow:0 0 10px var(--gn);animation:ldot .7s infinite;}
@keyframes ldot{0%,100%{opacity:1;transform:scale(1)}50%{opacity:.25;transform:scale(.45)}}

/* ═══ ÜST BAR EKSTRA ═══ */
.top-extras{
  display:flex;align-items:center;gap:6px;margin-left:auto;position:relative;z-index:2;
}
.top-xbtn{
  background:rgba(255,255,255,.08);border:1px solid rgba(255,255,255,.15);
  border-radius:14px;padding:2px 8px;font-size:8px;font-weight:700;
  font-family:'Orbitron',sans-serif;color:rgba(255,255,255,.7);
  cursor:pointer;transition:all .3s;letter-spacing:1px;display:flex;align-items:center;gap:4px;
}
.top-xbtn:hover{background:rgba(0,245,255,.2);border-color:var(--cy);color:#fff;transform:scale(1.08);}
.top-xbtn i{font-size:8px;}
.sleep-active{background:rgba(255,0,110,.25)!important;border-color:var(--pk)!important;color:var(--pk)!important;animation:sleepPulse 2s infinite;}
@keyframes sleepPulse{0%,100%{box-shadow:0 0 0 0 rgba(255,0,110,.4)}50%{box-shadow:0 0 0 4px rgba(255,0,110,0)}}

/* ══════ ALBÜM BÖLÜMÜ ══════ */
.album-col{
  position:relative;width:138px;min-height:130px;flex-shrink:0;
  display:flex;align-items:center;justify-content:center;
  background:radial-gradient(circle at 30% 40%,rgba(131,56,236,.7),transparent 65%),
    linear-gradient(145deg,#1c0838 0%,#090318 100%);
  overflow:hidden;
}
.album-col::before{
  content:'';position:absolute;inset:0;
  background-image:linear-gradient(rgba(131,56,236,.18) 1px,transparent 1px),
    linear-gradient(90deg,rgba(131,56,236,.18) 1px,transparent 1px);
  background-size:20px 20px;animation:gridScroll 10s linear infinite;
}
@keyframes gridScroll{0%{background-position:0 0}100%{background-position:0 20px}}
.album-col::after{
  content:'';position:absolute;bottom:0;right:0;
  width:38px;height:38px;
  border-right:2px solid var(--cy);border-bottom:2px solid var(--cy);
  box-shadow:2px 2px 14px var(--cy),inset -2px -2px 14px rgba(0,245,255,.25);
  opacity:.75;
}
.corner-tl{
  position:absolute;top:0;left:0;width:38px;height:38px;
  border-left:2px solid var(--pk);border-top:2px solid var(--pk);
  box-shadow:-2px -2px 14px var(--pk),inset 2px 2px 14px rgba(255,0,110,.25);
  opacity:.75;z-index:5;
}

/* VINYL */
.vinyl-scene{position:relative;width:90px;height:90px;z-index:5;}
.bass-halo{
  position:absolute;top:50%;left:50%;border-radius:50%;opacity:0;
  transform:translate(-50%,-50%);
  animation:haloAn 2.2s infinite;animation-play-state:paused;pointer-events:none;
}
.bass-halo:nth-child(1){width:98px;height:98px;border:1.5px solid var(--cy);box-shadow:0 0 12px var(--cy);animation-delay:0s;}
.bass-halo:nth-child(2){width:112px;height:112px;border:1.5px solid var(--pk);box-shadow:0 0 12px var(--pk);animation-delay:.75s;}
.bass-halo:nth-child(3){width:126px;height:126px;border:1.5px solid var(--pu);box-shadow:0 0 12px var(--pu);animation-delay:1.5s;}
.bass-halo.on{animation-play-state:running;}
@keyframes haloAn{
  0%{transform:translate(-50%,-50%) scale(.55);opacity:0}
  25%{opacity:.9}
  100%{transform:translate(-50%,-50%) scale(1.25);opacity:0}
}
.tonearm{
  position:absolute;top:-14px;right:-18px;width:56px;height:56px;
  transform-origin:88% 8%;transform:rotate(-34deg);
  transition:transform 1.4s cubic-bezier(.4,0,.2,1);
  z-index:10;pointer-events:none;
}
.tonearm.on{transform:rotate(-9deg);}
.vinyl{
  width:90px;height:90px;border-radius:50%;
  background:
    radial-gradient(circle at center,#0d0d0d 0%,#0d0d0d 20%,transparent 20%,transparent 26%,#080808 26%),
    conic-gradient(from 0deg,#0f0f0f,#1c1c1c 5%,#090909 10%,#191919 15%,
      #0f0f0f 20%,#1c1c1c 25%,#090909 30%,#191919 35%,
      #0f0f0f 40%,#1c1c1c 45%,#090909 50%,#191919 55%,
      #0f0f0f 60%,#1c1c1c 65%,#090909 70%,#191919 75%,
      #0f0f0f 80%,#1c1c1c 85%,#090909 90%,#191919 95%,#0f0f0f);
  animation:vSpin 7s linear infinite paused;
  box-shadow:0 0 0 1px rgba(255,255,255,.06),0 0 30px rgba(255,0,110,.5),inset 0 0 50px rgba(0,0,0,.95);
}
.vinyl.spin{
  animation-play-state:running;
  box-shadow:0 0 0 1px rgba(255,255,255,.1),0 0 45px rgba(255,0,110,.85),0 0 80px rgba(0,245,255,.35),inset 0 0 50px rgba(0,0,0,.95);
}
.vinyl::before{
  content:'';position:absolute;inset:4px;border-radius:50%;
  background:repeating-radial-gradient(circle at center,
    transparent 0,transparent 1.8px,rgba(255,255,255,.02) 1.8px,rgba(255,255,255,.02) 3px);
}
.vinyl::after{
  content:'';position:absolute;inset:0;border-radius:50%;
  background:linear-gradient(125deg,transparent 35%,rgba(255,255,255,.22) 50%,transparent 65%);
  animation:vSpin 2s linear infinite paused;
}
.vinyl.spin::after{animation-play-state:running;}
@keyframes vSpin{from{transform:rotate(0)}to{transform:rotate(360deg)}}
.vinyl-img{
  position:absolute;top:50%;left:50%;width:46px;height:46px;
  transform:translate(-50%,-50%);border-radius:50%;object-fit:cover;
  border:2.5px solid rgba(255,255,255,.2);
  box-shadow:0 0 18px rgba(0,0,0,.95);z-index:2;
  transition: all 0.5s;
}

/* ══════ MERKEZ ══════ */
.center-col{
  display:flex;flex-direction:column;justify-content:center;
  padding:32px 22px 14px 28px;gap:10px;
  position:relative;z-index:5;overflow:hidden;
}
.title-wrap{overflow:hidden;position:relative;}
.title-wrap::before,.title-wrap::after{
  content:'';position:absolute;top:0;bottom:0;width:18px;z-index:3;
}
.title-wrap::before{left:0;background:linear-gradient(90deg,rgba(6,4,14,.99),transparent);}
.title-wrap::after{right:0;background:linear-gradient(-90deg,rgba(6,4,14,.99),transparent);}
.track-name{
  display:inline-block;white-space:nowrap;
  font-size:16px;font-weight:800;letter-spacing:-.3px;
  background:linear-gradient(90deg,#fff 0%,var(--cy) 30%,var(--pk) 65%,#fff 100%);
  background-size:400% 100%;
  -webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;
  animation:nameGrad 5s linear infinite;
  filter:drop-shadow(0 0 8px rgba(0,245,255,.3));
}
@keyframes nameGrad{0%{background-position:0%}100%{background-position:400%}}
.track-name.marquee{animation:nameGrad 5s linear infinite,mqAn var(--mqd,13s) linear infinite;}
@keyframes mqAn{0%,15%{transform:translateX(0)}60%,82%{transform:translateX(var(--mqx,-80px))}100%{transform:translateX(0)}}
.meta-row{display:flex;align-items:center;gap:9px;flex-wrap:wrap;}
.dj-name{display:flex;align-items:center;gap:5px;font-size:11px;font-weight:600;color:rgba(255,255,255,.6);}
.dj-name i{color:var(--cy);font-size:10px;}
.quality-tag{
  font-size:9px;font-weight:700;font-family:'Orbitron',sans-serif;
  padding:3px 9px;border-radius:20px;letter-spacing:.8px;
  background:linear-gradient(135deg,rgba(131,56,236,.35),rgba(0,245,255,.2));
  border:1px solid rgba(0,245,255,.3);color:rgba(255,255,255,.85);
}

/* DINLEYICI SAYACI */
.listener-tag{
  font-size:9px;font-weight:700;font-family:'Orbitron',sans-serif;
  padding:3px 9px;border-radius:20px;letter-spacing:.8px;
  background:linear-gradient(135deg,rgba(255,0,110,.2),rgba(255,215,0,.15));
  border:1px solid rgba(255,215,0,.3);color:var(--gd);
  display:flex;align-items:center;gap:4px;
  animation:listPulse 3s infinite;
}
@keyframes listPulse{0%,100%{opacity:.8}50%{opacity:1}}

/* SÜRE SAYACI */
.listen-timer{
  font-size:9px;font-weight:700;font-family:'Orbitron',sans-serif;
  padding:3px 9px;border-radius:20px;letter-spacing:.8px;
  background:linear-gradient(135deg,rgba(57,255,20,.1),rgba(0,245,255,.1));
  border:1px solid rgba(57,255,20,.25);color:var(--gn);
  display:flex;align-items:center;gap:4px;
}

.ctrl-row{display:flex;align-items:center;gap:14px;}
.play-ring{position:relative;width:52px;height:52px;flex-shrink:0;}
.play-ring::before{
  content:'';position:absolute;inset:-3px;border-radius:50%;
  background:conic-gradient(from var(--angle),var(--pk),var(--cy),var(--pu),var(--pk));
  animation:spinAngle 2.5s linear infinite;filter:blur(4px);opacity:.95;
}
.play-btn{
  position:absolute;inset:0;border-radius:50%;
  background:linear-gradient(145deg,#2e0b42,#190625);
  border:none;color:#fff;font-size:18px;cursor:pointer;
  display:flex;align-items:center;justify-content:center;
  transition:all .25s;z-index:1;
  box-shadow:inset 0 1px 0 rgba(255,255,255,.18);
}
.play-btn:hover{transform:scale(1.12);background:linear-gradient(145deg,#420e5e,#26083a);}
.play-btn:active{transform:scale(.93);}

/* ══════ NEON EQ DALGALAR ══════ */
.eq-canvas-wrap{
  position:relative;
  display:flex;align-items:center;
  gap:0;flex:1;height:44px;overflow:hidden;
}
.eq-glow-layer{
  position:absolute;inset:0;filter:blur(8px);opacity:.55;pointer-events:none;
}
.eq-bars-wrap{
  display:flex;align-items:flex-end;gap:3px;height:44px;position:relative;z-index:2;
}
.eq-b{
  border-radius:4px 4px 2px 2px;min-height:4px;
  animation:eqB var(--spd) infinite ease-in-out var(--dly);
  animation-play-state:paused;position:relative;flex-shrink:0;
}
.eq-b:nth-child(1){width:5px;--c1:#00f5ff;--c2:#8338ec;--spd:.58s;--dly:.00s;--ph:38px;}
.eq-b:nth-child(2){width:5px;--c1:#ff006e;--c2:#ff6b35;--spd:.65s;--dly:.06s;--ph:44px;}
.eq-b:nth-child(3){width:5px;--c1:#8338ec;--c2:#00f5ff;--spd:.52s;--dly:.12s;--ph:32px;}
.eq-b:nth-child(4){width:5px;--c1:#ffd700;--c2:#ff006e;--spd:.72s;--dly:.04s;--ph:40px;}
.eq-b:nth-child(5){width:5px;--c1:#00f5ff;--c2:#39ff14;--spd:.60s;--dly:.18s;--ph:36px;}
.eq-b:nth-child(6){width:5px;--c1:#ff006e;--c2:#8338ec;--spd:.68s;--dly:.10s;--ph:44px;}
.eq-b:nth-child(7){width:5px;--c1:#39ff14;--c2:#00f5ff;--spd:.55s;--dly:.22s;--ph:30px;}
.eq-b:nth-child(8){width:5px;--c1:#8338ec;--c2:#ff006e;--spd:.75s;--dly:.08s;--ph:42px;}
.eq-b:nth-child(9){width:5px;--c1:#ff6b35;--c2:#ffd700;--spd:.62s;--dly:.16s;--ph:34px;}
.eq-b:nth-child(10){width:5px;--c1:#00f5ff;--c2:#ff006e;--spd:.70s;--dly:.14s;--ph:40px;}
.eq-b:nth-child(11){width:5px;--c1:#ff006e;--c2:#ffd700;--spd:.58s;--dly:.20s;--ph:28px;}
.eq-b:nth-child(12){width:5px;--c1:#8338ec;--c2:#39ff14;--spd:.66s;--dly:.02s;--ph:44px;}
.eq-b:nth-child(13){width:5px;--c1:#ffd700;--c2:#8338ec;--spd:.53s;--dly:.24s;--ph:32px;}
.eq-b:nth-child(14){width:5px;--c1:#39ff14;--c2:#ff006e;--spd:.78s;--dly:.07s;--ph:42px;}
.eq-b:nth-child(15){width:5px;--c1:#00f5ff;--c2:#8338ec;--spd:.61s;--dly:.28s;--ph:26px;}
.eq-b:nth-child(16){width:5px;--c1:#ff006e;--c2:#00f5ff;--spd:.69s;--dly:.11s;--ph:38px;}
.eq-b:nth-child(17){width:5px;--c1:#8338ec;--c2:#ffd700;--spd:.57s;--dly:.15s;--ph:44px;}
.eq-b:nth-child(18){width:5px;--c1:#00f5ff;--c2:#ff6b35;--spd:.74s;--dly:.19s;--ph:30px;}

.eq-b{background:linear-gradient(to top,var(--c1),var(--c2));box-shadow:0 0 10px var(--c1),0 0 22px rgba(0,245,255,.25);}
.eq-b.playing{animation-play-state:running;}

@keyframes eqB{
  0%,100%{height:4px;opacity:.45;filter:brightness(.8);}
  50%{height:var(--ph,30px);opacity:1;filter:brightness(2.2) saturate(1.5);}
}

.eq-glow-bars{display:flex;align-items:flex-end;gap:3px;height:44px;}
.eq-g{
  border-radius:4px;min-height:4px;
  animation:eqB var(--spd) infinite ease-in-out var(--dly);animation-play-state:paused;
}
.eq-g.playing{animation-play-state:running;}

/* Status */
.status-row{display:flex;align-items:center;gap:7px;}
.s-chip{
  display:flex;align-items:center;gap:4px;
  padding:4px 10px;border-radius:20px;
  font-size:9px;font-weight:700;font-family:'Orbitron',sans-serif;
  letter-spacing:.8px;transition:all .3s;
}
.chip-live{background:rgba(57,255,20,.1);border:1px solid rgba(57,255,20,.4);color:var(--gn);}
.chip-live i{animation:ldot .7s infinite;}
.chip-hd{background:rgba(0,245,255,.08);border:1px solid rgba(0,245,255,.3);color:var(--cy);}

/* Yüzen notalar */
.fnotes{position:absolute;inset:0;pointer-events:none;overflow:hidden;z-index:3;}
.fn{position:absolute;bottom:5px;opacity:0;font-size:13px;animation:fnUp 5s infinite ease-out;animation-play-state:paused;filter:drop-shadow(0 0 6px currentColor);}
.fn.on{animation-play-state:running;}
.fn:nth-child(1){left:5%;color:var(--cy);animation-delay:0s;animation-duration:4.8s;}
.fn:nth-child(2){left:20%;color:var(--pk);animation-delay:1s;animation-duration:5.6s;}
.fn:nth-child(3){left:40%;color:var(--pu);animation-delay:2s;animation-duration:4.2s;}
.fn:nth-child(4){left:58%;color:var(--gd);animation-delay:3s;animation-duration:6.2s;}
.fn:nth-child(5){left:75%;color:var(--gn);animation-delay:4s;animation-duration:5s;}
.fn:nth-child(6){left:90%;color:var(--or);animation-delay:1.5s;animation-duration:4.5s;}
@keyframes fnUp{
  0%{transform:translateY(0) rotate(-18deg) scale(.4);opacity:0}
  10%{opacity:1}
  85%{opacity:.5}
  100%{transform:translateY(-90px) rotate(22deg) scale(1.2);opacity:0}
}

/* Parçacıklar */
.pts-layer{position:absolute;inset:0;pointer-events:none;overflow:hidden;z-index:2;}
.pt{position:absolute;border-radius:50%;opacity:0;animation:ptRise var(--d) infinite var(--dl);animation-play-state:paused;}
.pt.on{animation-play-state:running;}
@keyframes ptRise{
  0%{transform:translateY(140px) translateX(0) scale(0);opacity:0}
  8%{opacity:1}
  92%{opacity:.8}
  100%{transform:translateY(-20px) translateX(var(--tx)) scale(1.4);opacity:0}
}

/* ══════ AKSİYON SÜTUNU ══════ */
.actions-col{
  display:flex;flex-direction:column;align-items:center;justify-content:center;
  gap:10px;padding:30px 18px 14px 16px;
  border-left:1px solid rgba(255,255,255,.05);
  min-width:148px;position:relative;z-index:5;
}
.req-btn{
  width:100%;display:flex;align-items:center;justify-content:center;gap:7px;
  padding:12px 16px;border-radius:14px;
  background:linear-gradient(135deg,rgba(131,56,236,.65),rgba(255,0,110,.6));
  border:1.5px solid rgba(255,0,110,.55);
  color:#fff;font-size:11px;font-weight:700;
  font-family:'Orbitron',sans-serif;cursor:pointer;
  transition:all .3s cubic-bezier(.4,0,.2,1);
  text-transform:uppercase;letter-spacing:1.5px;
  box-shadow:0 4px 22px rgba(255,0,110,.35),inset 0 1px 0 rgba(255,255,255,.12);
  position:relative;overflow:hidden;
}
.req-btn::before{
  content:'';position:absolute;top:-50%;left:-60%;width:55%;height:200%;
  background:linear-gradient(90deg,transparent,rgba(255,255,255,.28),transparent);
  transform:skewX(-20deg);transition:left .55s;
}
.req-btn:hover::before{left:130%;}
.req-btn:hover{transform:translateY(-3px);box-shadow:0 8px 32px rgba(255,0,110,.6),0 0 50px rgba(255,0,110,.3);}
.req-btn i{font-size:12px;animation:planeGo 2s infinite;}
@keyframes planeGo{
  0%,100%{transform:translateX(0) rotate(0)}
  30%{transform:translateX(3px) rotate(14deg)}
  70%{transform:translateX(-2px) rotate(-9deg)}
}
.side-btns{display:flex;gap:7px;flex-wrap:wrap;justify-content:center;}
.s-btn{
  width:37px;height:37px;border-radius:10px;
  background:rgba(255,255,255,.04);
  border:1px solid rgba(255,255,255,.1);
  color:rgba(255,255,255,.65);font-size:13px;cursor:pointer;
  display:flex;align-items:center;justify-content:center;
  transition:all .3s;position:relative;overflow:hidden;
}
.s-btn::after{content:'';position:absolute;inset:0;border-radius:10px;background:linear-gradient(135deg,var(--cy),var(--pu));opacity:0;transition:opacity .3s;}
.s-btn:hover::after{opacity:.28;}
.s-btn:hover{color:#fff;border-color:var(--cy);transform:translateY(-3px) scale(1.12);box-shadow:0 6px 20px rgba(0,245,255,.35);}
.s-btn i{position:relative;z-index:1;}
.s-btn.liked i{color:var(--pk);}
.s-btn.liked{border-color:var(--pk);box-shadow:0 0 16px rgba(255,0,110,.35);}
.s-btn.active-feature{border-color:var(--gn);box-shadow:0 0 12px rgba(57,255,20,.3);}
.s-btn.active-feature i{color:var(--gn);}

/* ══════ DİKEY SES KONTROLÜ ══════ */
.vol-col{
  display:flex;flex-direction:column;align-items:center;justify-content:center;
  gap:10px;padding:30px 22px 14px 18px;
  border-left:1px solid rgba(255,255,255,.05);
  position:relative;z-index:5;
}
.vol-lbl{font-family:'Orbitron',sans-serif;font-size:9px;font-weight:700;letter-spacing:2.5px;color:rgba(255,255,255,.3);text-transform:uppercase;}
.vol-ico{color:rgba(255,255,255,.6);font-size:18px;cursor:pointer;transition:all .3s;}
.vol-ico:hover{color:var(--cy);transform:scale(1.25);filter:drop-shadow(0 0 10px var(--cy));}
.vol-track{
  position:relative;width:30px;height:82px;
  background:rgba(255,255,255,.05);border-radius:20px;cursor:pointer;
  border:1px solid rgba(255,255,255,.08);overflow:hidden;
}
.vol-fill{
  position:absolute;bottom:0;left:0;right:0;
  background:linear-gradient(to top,var(--cy),var(--pu),var(--pk));
  border-radius:20px;transition:height .12s;
  box-shadow:0 0 14px var(--cy);
}
.vol-thumb{
  position:absolute;left:50%;transform:translateX(-50%);
  width:24px;height:24px;border-radius:50%;
  background:linear-gradient(135deg,#fff,var(--cy));
  box-shadow:0 0 18px var(--cy),0 2px 10px rgba(0,0,0,.6);
  transition:bottom .12s;cursor:grab;pointer-events:none;
}
.vol-range{
  position:absolute;inset:0;opacity:0;cursor:pointer;
  writing-mode:vertical-lr;direction:rtl;
  -webkit-appearance:slider-vertical;width:100%;
}
.vol-pct{font-family:'Orbitron',sans-serif;font-size:10px;font-weight:700;color:var(--cy);text-shadow:0 0 10px var(--cy);letter-spacing:.5px;}

/* ══════ SPECTRUM CANVAS ══════ */
.spectrum-wrap{
  position:absolute;bottom:0;left:0;right:0;
  height:28px;pointer-events:none;z-index:4;overflow:hidden;
}
.spectrum-canvas{width:100%;height:100%;display:block;}

/* ══════ ALT MESAJ WIDGET ══════ */
.msg-wrap{
  margin-top:12px;position:relative;
  border-radius:24px;padding:1.5px;
  background:conic-gradient(from var(--angle),var(--pu),var(--pk),var(--cy),var(--gd),var(--pu));
  animation:spinAngle 6s linear infinite;
  box-shadow:0 0 55px rgba(255,0,110,.2),0 0 90px rgba(131,56,236,.12);
}
.msg-card{
  background:
    radial-gradient(ellipse at 0% 0%,rgba(131,56,236,.22),transparent 55%),
    radial-gradient(ellipse at 100% 100%,rgba(255,0,110,.18),transparent 55%),
    linear-gradient(160deg,rgba(12,8,24,.99),rgba(6,4,14,.99));
  border-radius:22.5px;overflow:hidden;
}

.msg-top{
  background:linear-gradient(135deg,rgba(131,56,236,.75) 0%,rgba(255,0,110,.65) 60%,rgba(0,245,255,.45) 100%);
  padding:13px 22px;display:flex;align-items:center;gap:10px;
  position:relative;overflow:hidden;
}
.msg-top::before{
  content:'';position:absolute;inset:0;
  background:linear-gradient(90deg,transparent,rgba(255,255,255,.2),transparent);
  animation:lsShine 4s infinite;
}
.msg-top-ico{font-size:16px;color:#fff;position:relative;z-index:1;filter:drop-shadow(0 0 10px var(--cy));}
.msg-top-txt{font-family:'Orbitron',sans-serif;font-size:11px;font-weight:700;letter-spacing:2px;color:#fff;flex:1;text-transform:uppercase;position:relative;z-index:1;}
.msg-top-badge{
  background:rgba(0,245,255,.15);border:1px solid rgba(0,245,255,.45);
  border-radius:20px;padding:3px 10px;
  font-size:9px;font-weight:700;font-family:'Orbitron',sans-serif;
  color:var(--cy);letter-spacing:1px;position:relative;z-index:1;
  animation:bdgPulse 2s infinite;
}
@keyframes bdgPulse{0%,100%{box-shadow:0 0 0 0 rgba(0,245,255,.4)}50%{box-shadow:0 0 0 5px rgba(0,245,255,0)}}

/* ══════ FREKANS GÖRSELİ ══════ */
.freq-band{
  background:rgba(0,0,0,.55);
  height:42px;display:flex;align-items:center;
  border-bottom:1px solid rgba(255,255,255,.06);
  overflow:hidden;position:relative;gap:0;
}
.freq-label{
  flex-shrink:0;
  background:linear-gradient(135deg,var(--pu),var(--pk));
  height:100%;width:80px;
  display:flex;flex-direction:column;align-items:center;justify-content:center;
  font-family:'Orbitron',sans-serif;font-size:9px;font-weight:700;
  color:#fff;letter-spacing:1.5px;text-transform:uppercase;
  box-shadow:6px 0 18px rgba(131,56,236,.55);z-index:3;
}
.freq-label span{font-size:13px;font-weight:900;color:var(--cy);text-shadow:0 0 12px var(--cy);}
.freq-vis{flex:1;height:100%;position:relative;overflow:hidden;}
.freq-bars{
  position:absolute;inset:0;
  display:flex;align-items:center;gap:2px;padding:4px 12px;
}
.fb{
  flex:1;border-radius:3px;
  animation:fbAn var(--fs) infinite ease-in-out var(--fd);
  animation-play-state:paused;
}
.fb.on{animation-play-state:running;}
@keyframes fbAn{
  0%,100%{height:3px;opacity:.4;filter:brightness(.7);}
  50%{height:var(--fh,20px);opacity:1;filter:brightness(2.5);}
}
.fb:nth-child(3n+1){background:linear-gradient(to top,var(--cy),rgba(0,245,255,.3));box-shadow:0 0 8px var(--cy);}
.fb:nth-child(3n+2){background:linear-gradient(to top,var(--pk),rgba(255,0,110,.3));box-shadow:0 0 8px var(--pk);}
.fb:nth-child(3n){background:linear-gradient(to top,var(--pu),rgba(131,56,236,.3));box-shadow:0 0 8px var(--pu);}
.freq-vis::after{
  content:'';position:absolute;inset:0;
  background:linear-gradient(90deg,rgba(0,0,0,.7),transparent 15%,transparent 85%,rgba(0,0,0,.7));
  pointer-events:none;z-index:2;
}

.msg-ticker{
  flex-shrink:0;overflow:hidden;
  border-left:1px solid rgba(255,255,255,.08);
  width:220px;height:100%;
  display:flex;align-items:center;position:relative;
}
.msg-ticker::before,.msg-ticker::after{
  content:'';position:absolute;top:0;bottom:0;width:28px;z-index:5;
}
.msg-ticker::before{left:0;background:linear-gradient(90deg,rgba(0,0,0,.6),transparent);}
.msg-ticker::after{right:0;background:linear-gradient(-90deg,rgba(0,0,0,.6),transparent);}
.msg-scroll{
  display:inline-flex;white-space:nowrap;
  animation:msgScroll 22s linear infinite;padding-left:50px;
}
@keyframes msgScroll{0%{transform:translateX(0)}100%{transform:translateX(-50%)}}
.msg-item{
  padding:0 20px;font-size:10.5px;font-weight:600;
  color:rgba(255,255,255,.75);display:flex;align-items:center;gap:6px;
}
.msg-item i{font-size:9px;color:var(--gd);}

.req-frame{width:100%;height:60px;border:none;background:transparent;display:block;}

/* ══════ MODAL ══════ */
.modal-bg{
  display:none;position:fixed;inset:0;
  background:rgba(0,0,0,.93);backdrop-filter:blur(30px) saturate(130%);
  z-index:99999;justify-content:center;align-items:center;
}
.modal-bg.open{display:flex;animation:mFade .35s;}
@keyframes mFade{from{opacity:0}to{opacity:1}}
.modal-shell{
  position:relative;width:95%;max-width:800px;height:88vh;
  border-radius:30px;padding:2px;
  background:conic-gradient(from var(--angle),var(--pu),var(--pk),var(--cy),var(--pu));
  animation:spinAngle 3s linear infinite,mPop .5s cubic-bezier(.4,0,.2,1);
  box-shadow:0 30px 90px rgba(0,0,0,.96),0 0 120px rgba(255,0,110,.4),0 0 220px rgba(131,56,236,.22);
}
@keyframes mPop{from{transform:scale(.8) translateY(60px);opacity:0}to{transform:scale(1) translateY(0);opacity:1}}
.modal-body{
  width:100%;height:100%;border-radius:28px;overflow:hidden;
  background:radial-gradient(ellipse at top left,rgba(131,56,236,.38),transparent 55%),
    radial-gradient(ellipse at bottom right,rgba(255,0,110,.32),transparent 55%),rgba(8,5,18,.98);
  display:flex;flex-direction:column;
}
.modal-hdr{
  background:linear-gradient(135deg,var(--pu) 0%,var(--pk) 60%,rgba(0,245,255,.65) 100%);
  padding:18px 26px;display:flex;justify-content:space-between;align-items:center;
  position:relative;overflow:hidden;flex-shrink:0;
}
.modal-hdr::before{content:'';position:absolute;inset:0;background:linear-gradient(90deg,transparent,rgba(255,255,255,.22),transparent);animation:lsShine 4s infinite;}
.modal-ttl{
  font-family:'Orbitron',sans-serif;font-size:16px;font-weight:900;
  color:#fff;display:flex;align-items:center;gap:12px;
  text-transform:uppercase;letter-spacing:1.5px;z-index:1;
}
.modal-ttl i{animation:planeGo 2s infinite;}
.modal-close{
  width:42px;height:42px;border-radius:12px;
  background:rgba(255,255,255,.1);border:2px solid rgba(255,255,255,.22);
  color:#fff;cursor:pointer;font-size:18px;
  display:flex;align-items:center;justify-content:center;
  transition:.3s;z-index:1;
}
.modal-close:hover{background:rgba(255,0,110,.45);transform:rotate(90deg);box-shadow:0 0 24px rgba(255,0,110,.65);}
.modal-iframe{width:100%;flex:1;border:none;background:#fff;}

/* ══════ TOAST ══════ */
.toast{
  position:fixed;bottom:28px;right:28px;
  padding:14px 22px;border-radius:16px;
  background:linear-gradient(135deg,rgba(131,56,236,.94),rgba(255,0,110,.9));
  border:1px solid rgba(255,255,255,.18);color:#fff;font-weight:700;font-size:13px;
  box-shadow:0 12px 45px rgba(0,0,0,.65),0 0 55px rgba(255,0,110,.4);
  z-index:999999;backdrop-filter:blur(22px);
  display:flex;align-items:center;gap:10px;
  transform:translateY(120px) scale(.88);opacity:0;
  transition:all .4s cubic-bezier(.4,0,.2,1);pointer-events:none;
}
.toast.show{transform:translateY(0) scale(1);opacity:1;}
.toast i{font-size:16px;color:var(--cy);}

/* ══════════════════════════════════════════
   YENİ: ŞARKI GEÇMİŞİ PANELİ
══════════════════════════════════════════ */
.history-panel{
  position:fixed;top:0;right:-380px;width:360px;height:100vh;
  background:linear-gradient(180deg,rgba(12,8,26,.98),rgba(6,4,14,.99));
  border-left:2px solid rgba(131,56,236,.4);
  z-index:99998;transition:right .5s cubic-bezier(.4,0,.2,1);
  display:flex;flex-direction:column;
  box-shadow:-20px 0 60px rgba(0,0,0,.7);
  backdrop-filter:blur(30px);
}
.history-panel.open{right:0;}
.hp-hdr{
  padding:22px;display:flex;align-items:center;gap:12px;
  background:linear-gradient(135deg,rgba(131,56,236,.5),rgba(255,0,110,.4));
  flex-shrink:0;
}
.hp-hdr i{font-size:18px;color:var(--cy);}
.hp-hdr span{font-family:'Orbitron',sans-serif;font-size:13px;font-weight:700;color:#fff;letter-spacing:2px;flex:1;}
.hp-close{
  width:34px;height:34px;border-radius:10px;background:rgba(255,255,255,.1);
  border:1px solid rgba(255,255,255,.2);color:#fff;cursor:pointer;
  display:flex;align-items:center;justify-content:center;font-size:14px;
  transition:.3s;
}
.hp-close:hover{background:rgba(255,0,110,.4);transform:rotate(90deg);}
.hp-list{flex:1;overflow-y:auto;padding:12px;}
.hp-list::-webkit-scrollbar{width:4px;}
.hp-list::-webkit-scrollbar-thumb{background:var(--pu);border-radius:4px;}
.hp-item{
  display:flex;align-items:center;gap:12px;
  padding:12px;border-radius:14px;margin-bottom:8px;
  background:rgba(255,255,255,.03);border:1px solid rgba(255,255,255,.06);
  transition:all .3s;
}
.hp-item:hover{background:rgba(131,56,236,.15);border-color:rgba(131,56,236,.3);transform:translateX(-4px);}
.hp-num{
  font-family:'Orbitron',sans-serif;font-size:10px;font-weight:900;
  color:var(--pu);min-width:22px;text-align:center;
}
.hp-info{flex:1;min-width:0;}
.hp-title{font-size:12px;font-weight:700;color:rgba(255,255,255,.9);white-space:nowrap;overflow:hidden;text-overflow:ellipsis;}
.hp-time{font-size:9px;color:rgba(255,255,255,.4);font-family:'Orbitron',sans-serif;margin-top:2px;}
.hp-empty{text-align:center;padding:40px;color:rgba(255,255,255,.3);font-size:12px;}

/* ══════════════════════════════════════════
   YENİ: SLEEP TIMER PANELİ
══════════════════════════════════════════ */
.sleep-panel{
  position:fixed;bottom:80px;right:28px;
  width:280px;padding:2px;border-radius:22px;
  background:conic-gradient(from var(--angle),var(--pu),var(--pk),var(--cy),var(--pu));
  animation:spinAngle 4s linear infinite;
  z-index:99997;
  transform:scale(.8) translateY(20px);opacity:0;
  pointer-events:none;transition:all .35s cubic-bezier(.4,0,.2,1);
}
.sleep-panel.open{transform:scale(1) translateY(0);opacity:1;pointer-events:all;}
.sleep-inner{
  background:linear-gradient(160deg,rgba(12,8,24,.98),rgba(6,4,14,.99));
  border-radius:20px;padding:20px;
}
.sleep-title{
  font-family:'Orbitron',sans-serif;font-size:11px;font-weight:700;
  color:#fff;margin-bottom:14px;display:flex;align-items:center;gap:8px;letter-spacing:1.5px;
}
.sleep-title i{color:var(--cy);}
.sleep-options{display:flex;flex-wrap:wrap;gap:8px;}
.sleep-opt{
  padding:8px 14px;border-radius:12px;
  background:rgba(255,255,255,.05);border:1px solid rgba(255,255,255,.12);
  color:rgba(255,255,255,.7);font-size:11px;font-weight:700;
  font-family:'Orbitron',sans-serif;cursor:pointer;transition:all .3s;
}
.sleep-opt:hover{background:rgba(131,56,236,.3);border-color:var(--pu);color:#fff;transform:scale(1.06);}
.sleep-opt.active{background:linear-gradient(135deg,var(--pu),var(--pk));border-color:var(--pk);color:#fff;box-shadow:0 4px 20px rgba(255,0,110,.4);}
.sleep-countdown{
  margin-top:14px;text-align:center;
  font-family:'Orbitron',sans-serif;font-size:20px;font-weight:900;
  color:var(--cy);text-shadow:0 0 20px var(--cy);
  display:none;
}
.sleep-countdown.show{display:block;animation:countPulse 1s infinite;}
@keyframes countPulse{0%,100%{opacity:1}50%{opacity:.6}}
.sleep-cancel{
  margin-top:10px;width:100%;padding:8px;border-radius:10px;
  background:rgba(255,0,110,.2);border:1px solid rgba(255,0,110,.4);
  color:var(--pk);font-size:10px;font-weight:700;font-family:'Orbitron',sans-serif;
  cursor:pointer;display:none;transition:.3s;
}
.sleep-cancel.show{display:block;}
.sleep-cancel:hover{background:rgba(255,0,110,.4);}

/* ══════════════════════════════════════════
   YENİ: TEMA SEÇİCİ
══════════════════════════════════════════ */
.theme-panel{
  position:fixed;bottom:80px;left:28px;
  width:220px;padding:2px;border-radius:22px;
  background:conic-gradient(from var(--angle),var(--pu),var(--pk),var(--cy),var(--pu));
  animation:spinAngle 4s linear infinite;
  z-index:99997;
  transform:scale(.8) translateY(20px);opacity:0;
  pointer-events:none;transition:all .35s cubic-bezier(.4,0,.2,1);
}
.theme-panel.open{transform:scale(1) translateY(0);opacity:1;pointer-events:all;}
.theme-inner{
  background:linear-gradient(160deg,rgba(12,8,24,.98),rgba(6,4,14,.99));
  border-radius:20px;padding:18px;
}
.theme-title{
  font-family:'Orbitron',sans-serif;font-size:11px;font-weight:700;
  color:#fff;margin-bottom:12px;display:flex;align-items:center;gap:8px;letter-spacing:1.5px;
}
.theme-title i{color:var(--gd);}
.theme-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:8px;}
.theme-dot{
  width:100%;aspect-ratio:1;border-radius:14px;cursor:pointer;
  border:2px solid rgba(255,255,255,.12);transition:all .3s;
  position:relative;overflow:hidden;
  display:flex;align-items:center;justify-content:center;
}
.theme-dot::after{
  content:attr(data-label);font-size:7px;font-family:'Orbitron',sans-serif;
  font-weight:700;color:#fff;text-shadow:0 1px 4px rgba(0,0,0,.8);
  letter-spacing:.5px;
}
.theme-dot:hover{transform:scale(1.1);border-color:#fff;box-shadow:0 0 20px rgba(255,255,255,.3);}
.theme-dot.active{border-color:var(--cy);box-shadow:0 0 20px var(--cy);}
.td-neon{background:linear-gradient(135deg,#ff006e,#00f5ff,#8338ec);}
.td-sunset{background:linear-gradient(135deg,#ff4500,#ff8c00,#dc143c);}
.td-ocean{background:linear-gradient(135deg,#0077b6,#00b4d8,#023e8a);}
.td-forest{background:linear-gradient(135deg,#2d6a4f,#52b788,#1b4332);}
.td-purple{background:linear-gradient(135deg,#e040fb,#d500f9,#aa00ff);}
.td-retro{background:linear-gradient(135deg,#f72585,#4cc9f0,#7209b7);}

/* ══════════════════════════════════════════
   YENİ: EQ PRESET PANELİ
══════════════════════════════════════════ */
.eq-panel{
  position:fixed;top:50%;left:50%;transform:translate(-50%,-50%) scale(.8);
  width:340px;padding:2px;border-radius:24px;
  background:conic-gradient(from var(--angle),var(--pu),var(--pk),var(--cy),var(--pu));
  animation:spinAngle 4s linear infinite;
  z-index:99998;opacity:0;pointer-events:none;
  transition:all .4s cubic-bezier(.4,0,.2,1);
}
.eq-panel.open{transform:translate(-50%,-50%) scale(1);opacity:1;pointer-events:all;}
.eq-inner{
  background:linear-gradient(160deg,rgba(12,8,24,.99),rgba(6,4,14,.99));
  border-radius:22px;padding:24px;
}
.eq-head{display:flex;align-items:center;justify-content:space-between;margin-bottom:18px;}
.eq-head-title{font-family:'Orbitron',sans-serif;font-size:12px;font-weight:700;color:#fff;display:flex;align-items:center;gap:8px;letter-spacing:1.5px;}
.eq-head-title i{color:var(--gd);}
.eq-close{
  width:30px;height:30px;border-radius:8px;background:rgba(255,255,255,.08);
  border:1px solid rgba(255,255,255,.15);color:#fff;cursor:pointer;
  display:flex;align-items:center;justify-content:center;font-size:12px;transition:.3s;
}
.eq-close:hover{background:rgba(255,0,110,.4);transform:rotate(90deg);}
.eq-presets{display:grid;grid-template-columns:repeat(2,1fr);gap:8px;margin-bottom:18px;}
.eq-preset{
  padding:10px;border-radius:12px;
  background:rgba(255,255,255,.04);border:1px solid rgba(255,255,255,.1);
  cursor:pointer;transition:all .3s;text-align:center;
}
.eq-preset:hover{background:rgba(131,56,236,.2);border-color:var(--pu);transform:scale(1.04);}
.eq-preset.active{background:linear-gradient(135deg,rgba(131,56,236,.4),rgba(255,0,110,.3));border-color:var(--pk);box-shadow:0 4px 20px rgba(255,0,110,.3);}
.eq-preset-name{font-family:'Orbitron',sans-serif;font-size:10px;font-weight:700;color:#fff;letter-spacing:1px;}
.eq-preset-desc{font-size:9px;color:rgba(255,255,255,.5);margin-top:3px;}
.eq-sliders{display:flex;gap:10px;justify-content:center;align-items:flex-end;height:100px;}
.eq-sl{
  display:flex;flex-direction:column;align-items:center;gap:6px;
}
.eq-sl label{font-size:7px;font-family:'Orbitron',sans-serif;font-weight:700;color:rgba(255,255,255,.4);}
.eq-sl input[type="range"]{
  writing-mode:vertical-lr;direction:rtl;
  -webkit-appearance:slider-vertical;
  width:20px;height:70px;
  accent-color:var(--cy);
}
.eq-sl .eq-val{font-size:8px;font-family:'Orbitron',sans-serif;color:var(--cy);font-weight:700;}

/* ══════════════════════════════════════════
   YENİ: KLAVYE KISAYOL POPUP
══════════════════════════════════════════ */
.shortcut-panel{
  position:fixed;top:50%;left:50%;transform:translate(-50%,-50%) scale(.8);
  width:320px;padding:2px;border-radius:24px;
  background:conic-gradient(from var(--angle),var(--pu),var(--pk),var(--cy),var(--pu));
  animation:spinAngle 4s linear infinite;
  z-index:99998;opacity:0;pointer-events:none;
  transition:all .4s cubic-bezier(.4,0,.2,1);
}
.shortcut-panel.open{transform:translate(-50%,-50%) scale(1);opacity:1;pointer-events:all;}
.sc-inner{
  background:linear-gradient(160deg,rgba(12,8,24,.99),rgba(6,4,14,.99));
  border-radius:22px;padding:24px;
}
.sc-head{display:flex;align-items:center;justify-content:space-between;margin-bottom:16px;}
.sc-title{font-family:'Orbitron',sans-serif;font-size:12px;font-weight:700;color:#fff;display:flex;align-items:center;gap:8px;letter-spacing:1px;}
.sc-title i{color:var(--gn);}
.sc-close{
  width:30px;height:30px;border-radius:8px;background:rgba(255,255,255,.08);
  border:1px solid rgba(255,255,255,.15);color:#fff;cursor:pointer;
  display:flex;align-items:center;justify-content:center;font-size:12px;transition:.3s;
}
.sc-close:hover{background:rgba(255,0,110,.4);transform:rotate(90deg);}
.sc-list{display:flex;flex-direction:column;gap:8px;}
.sc-row{display:flex;align-items:center;gap:12px;}
.sc-key{
  display:inline-flex;align-items:center;justify-content:center;
  min-width:42px;padding:5px 10px;border-radius:8px;
  background:rgba(255,255,255,.08);border:1px solid rgba(255,255,255,.2);
  font-family:'Orbitron',sans-serif;font-size:9px;font-weight:700;color:var(--cy);
}
.sc-desc{font-size:11px;color:rgba(255,255,255,.7);}

/* ══════ BAĞLANTI DURUMU ÇUBUĞU ══════ */
.conn-bar{
  position:fixed;top:0;left:0;right:0;height:3px;z-index:999999;
  transition:all .3s;
}
.conn-bar.connected{background:linear-gradient(90deg,var(--gn),var(--cy),var(--gn));box-shadow:0 0 10px var(--gn);opacity:.6;}
.conn-bar.disconnected{background:linear-gradient(90deg,#ff0000,#ff4444,#ff0000);box-shadow:0 0 10px #ff0000;opacity:1;animation:connPulse 1s infinite;}
.conn-bar.buffering{background:linear-gradient(90deg,var(--gd),var(--or),var(--gd));box-shadow:0 0 10px var(--gd);animation:connSlide 1s linear infinite;background-size:200% 100%;}
@keyframes connPulse{0%,100%{opacity:1}50%{opacity:.3}}
@keyframes connSlide{0%{background-position:0% 0}100%{background-position:200% 0}}

/* ══════ MINI PLAYER ══════ */
.mini-player{
  position:fixed;bottom:20px;left:50%;transform:translateX(-50%) translateY(120px);
  width:350px;height:60px;
  border-radius:30px;padding:1.5px;
  background:conic-gradient(from var(--angle),var(--pu),var(--pk),var(--cy),var(--pu));
  animation:spinAngle 4s linear infinite;
  z-index:99996;
  transition:transform .5s cubic-bezier(.4,0,.2,1);
  pointer-events:none;opacity:0;
}
.mini-player.show{transform:translateX(-50%) translateY(0);pointer-events:all;opacity:1;}
.mini-inner{
  width:100%;height:100%;border-radius:28.5px;
  background:linear-gradient(160deg,rgba(12,8,24,.98),rgba(6,4,14,.98));
  display:flex;align-items:center;padding:0 8px;gap:10px;
}
.mini-art{
  width:44px;height:44px;border-radius:50%;object-fit:cover;
  border:2px solid rgba(131,56,236,.5);
  animation:vSpin 7s linear infinite paused;
}
.mini-art.spin{animation-play-state:running;}
.mini-info{flex:1;min-width:0;}
.mini-title{font-size:11px;font-weight:700;color:#fff;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;}
.mini-sub{font-size:9px;color:rgba(255,255,255,.4);font-family:'Orbitron',sans-serif;}
.mini-play{
  width:40px;height:40px;border-radius:50%;
  background:linear-gradient(135deg,var(--pu),var(--pk));
  border:none;color:#fff;font-size:14px;cursor:pointer;
  display:flex;align-items:center;justify-content:center;
  transition:.3s;flex-shrink:0;
}
.mini-play:hover{transform:scale(1.15);}
.mini-close{
  width:28px;height:28px;border-radius:50%;
  background:rgba(255,255,255,.08);border:1px solid rgba(255,255,255,.15);
  color:rgba(255,255,255,.6);font-size:10px;cursor:pointer;
  display:flex;align-items:center;justify-content:center;
  transition:.3s;flex-shrink:0;
}
.mini-close:hover{background:rgba(255,0,110,.3);color:#fff;}

/* ══════ RESPONSIVE ══════ */
@media(max-width:860px){
  .player{grid-template-columns:120px 1fr auto;grid-template-rows:auto auto;}
  .vol-col{grid-column:1/-1;flex-direction:row;border-left:none;border-top:1px solid rgba(255,255,255,.05);padding:10px 22px;justify-content:center;gap:14px;}
  .vol-track{width:110px;height:24px;border-radius:20px;}
  .vol-fill{bottom:unset;left:0;top:0;height:100% !important;width:var(--vw,70%);border-radius:20px;}
  .vol-thumb{bottom:unset !important;top:50%;transform:translate(-50%,-50%);left:var(--vw,70%);}
  .vol-range{writing-mode:unset;direction:unset;-webkit-appearance:none;height:100%;width:100%;padding:0;}
  .logo-strip{left:118px;}
  .history-panel{width:300px;}
}
@media(max-width:560px){
  .player{grid-template-columns:108px 1fr;}
  .actions-col{grid-column:1/-1;flex-direction:row;flex-wrap:wrap;justify-content:center;border-left:none;border-top:1px solid rgba(255,255,255,.05);padding:10px 16px;}
  .vol-col{grid-column:1/-1;}
  .album-col{width:108px;}
  .track-name{font-size:14px;}
  .msg-ticker{display:none;}
  .history-panel{width:100%;}
  .mini-player{width:300px;}
}
</style>
</head>
<body>

<!-- BAĞLANTI DURUMU ÇUBUĞU -->
<div class="conn-bar connected" id="connBar"></div>

<div class="toast" id="toast"><i class="fas fa-check-circle"></i><span id="toastTxt"></span></div>

<!-- ANA MODAL -->
<div class="modal-bg" id="modal">
  <div class="modal-shell">
    <div class="modal-body">
      <div class="modal-hdr">
        <div class="modal-ttl"><i class="fas fa-paper-plane"></i>Şarkı İsteği Gönder</div>
        <button class="modal-close" id="modalClose"><i class="fas fa-times"></i></button>
      </div>
      <iframe src="https://okeysin.com/istekgonder.php" class="modal-iframe" title="İstek"></iframe>
    </div>
  </div>
</div>

<!-- ŞARKI GEÇMİŞİ PANELİ -->
<div class="history-panel" id="historyPanel">
  <div class="hp-hdr">
    <i class="fas fa-clock-rotate-left"></i>
    <span>ŞARKI GEÇMİŞİ</span>
    <button class="hp-close" id="historyClose"><i class="fas fa-times"></i></button>
  </div>
  <div class="hp-list" id="historyList">
    <div class="hp-empty"><i class="fas fa-music" style="font-size:24px;margin-bottom:10px;display:block;color:var(--pu);"></i>Henüz şarkı geçmişi yok<br><small>Yayın başladığında burada görünecek</small></div>
  </div>
</div>

<!-- SLEEP TIMER PANELİ -->
<div class="sleep-panel" id="sleepPanel">
  <div class="sleep-inner">
    <div class="sleep-title"><i class="fas fa-moon"></i>UYKU ZAMANLAYICISI</div>
    <div class="sleep-options" id="sleepOptions">
      <div class="sleep-opt" data-min="5">5 dk</div>
      <div class="sleep-opt" data-min="15">15 dk</div>
      <div class="sleep-opt" data-min="30">30 dk</div>
      <div class="sleep-opt" data-min="45">45 dk</div>
      <div class="sleep-opt" data-min="60">1 saat</div>
      <div class="sleep-opt" data-min="120">2 saat</div>
    </div>
    <div class="sleep-countdown" id="sleepCountdown">00:00</div>
    <button class="sleep-cancel" id="sleepCancel">İPTAL ET</button>
  </div>
</div>

<!-- TEMA SEÇİCİ -->
<div class="theme-panel" id="themePanel">
  <div class="theme-inner">
    <div class="theme-title"><i class="fas fa-palette"></i>TEMA SEÇ</div>
    <div class="theme-grid">
      <div class="theme-dot td-neon active" data-theme="neon" data-label="NEON"></div>
      <div class="theme-dot td-sunset" data-theme="sunset" data-label="SUNSET"></div>
      <div class="theme-dot td-ocean" data-theme="ocean" data-label="OCEAN"></div>
      <div class="theme-dot td-forest" data-theme="forest" data-label="FOREST"></div>
      <div class="theme-dot td-purple" data-theme="purple" data-label="PURPLE"></div>
      <div class="theme-dot td-retro" data-theme="retro" data-label="RETRO"></div>
    </div>
  </div>
</div>

<!-- EQ PRESET PANELİ -->
<div class="eq-panel" id="eqPanel">
  <div class="eq-inner">
    <div class="eq-head">
      <div class="eq-head-title"><i class="fas fa-sliders"></i>EQUALİZER</div>
      <button class="eq-close" id="eqClose"><i class="fas fa-times"></i></button>
    </div>
    <div class="eq-presets" id="eqPresets">
      <div class="eq-preset active" data-preset="flat">
        <div class="eq-preset-name">FLAT</div>
        <div class="eq-preset-desc">Doğal ses</div>
      </div>
      <div class="eq-preset" data-preset="bass">
        <div class="eq-preset-name">BASS BOOST</div>
        <div class="eq-preset-desc">Güçlü bas</div>
      </div>
      <div class="eq-preset" data-preset="vocal">
        <div class="eq-preset-name">VOCAL</div>
        <div class="eq-preset-desc">Vokal öne çıkar</div>
      </div>
      <div class="eq-preset" data-preset="rock">
        <div class="eq-preset-name">ROCK</div>
        <div class="eq-preset-desc">Enerjik sound</div>
      </div>
      <div class="eq-preset" data-preset="pop">
        <div class="eq-preset-name">POP</div>
        <div class="eq-preset-desc">Balanced pop</div>
      </div>
      <div class="eq-preset" data-preset="jazz">
        <div class="eq-preset-name">JAZZ</div>
        <div class="eq-preset-desc">Sıcak tonlar</div>
      </div>
    </div>
    <div class="eq-sliders" id="eqSliders">
      <div class="eq-sl"><span class="eq-val" id="eqv0">0</span><input type="range" min="-12" max="12" value="0" data-band="0"><label>60</label></div>
      <div class="eq-sl"><span class="eq-val" id="eqv1">0</span><input type="range" min="-12" max="12" value="0" data-band="1"><label>250</label></div>
      <div class="eq-sl"><span class="eq-val" id="eqv2">0</span><input type="range" min="-12" max="12" value="0" data-band="2"><label>1K</label></div>
      <div class="eq-sl"><span class="eq-val" id="eqv3">0</span><input type="range" min="-12" max="12" value="0" data-band="3"><label>4K</label></div>
      <div class="eq-sl"><span class="eq-val" id="eqv4">0</span><input type="range" min="-12" max="12" value="0" data-band="4"><label>16K</label></div>
    </div>
  </div>
</div>

<!-- KLAVYE KISAYOLLARI PANELİ -->
<div class="shortcut-panel" id="shortcutPanel">
  <div class="sc-inner">
    <div class="sc-head">
      <div class="sc-title"><i class="fas fa-keyboard"></i>KISAYOLLAR</div>
      <button class="sc-close" id="scClose"><i class="fas fa-times"></i></button>
    </div>
    <div class="sc-list">
      <div class="sc-row"><span class="sc-key">SPACE</span><span class="sc-desc">Oynat / Duraklat</span></div>
      <div class="sc-row"><span class="sc-key">↑</span><span class="sc-desc">Ses Aç</span></div>
      <div class="sc-row"><span class="sc-key">↓</span><span class="sc-desc">Ses Kıs</span></div>
      <div class="sc-row"><span class="sc-key">M</span><span class="sc-desc">Sessiz / Sesli</span></div>
      <div class="sc-row"><span class="sc-key">H</span><span class="sc-desc">Şarkı Geçmişi</span></div>
      <div class="sc-row"><span class="sc-key">T</span><span class="sc-desc">Tema Değiştir</span></div>
      <div class="sc-row"><span class="sc-key">E</span><span class="sc-desc">Equalizer</span></div>
      <div class="sc-row"><span class="sc-key">F</span><span class="sc-desc">Tam Ekran</span></div>
      <div class="sc-row"><span class="sc-key">?</span><span class="sc-desc">Bu Pencere</span></div>
    </div>
  </div>
</div>

<!-- MİNİ PLAYER -->
<div class="mini-player" id="miniPlayer">
  <div class="mini-inner">
    <img src="https://images.unsplash.com/photo-1470225620780-dba8ba36b745?w=100" class="mini-art" id="miniArt" alt="">
    <div class="mini-info">
      <div class="mini-title" id="miniTitle">okeysin İmaj FM</div>
      <div class="mini-sub">CANLI YAYIN</div>
    </div>
    <button class="mini-play" id="miniPlay"><i class="fas fa-play" id="miniPlayIco"></i></button>
    <button class="mini-close" id="miniClose"><i class="fas fa-arrow-up"></i></button>
  </div>
</div>

<div style="position:relative;z-index:10;width:100%;" id="mainContainer">

  <!-- PLAYER -->
  <div class="holo-frame" id="holoFrame">
    <div class="player" id="player">

      <div class="sweep"></div>

      <div class="logo-strip">
        <div class="logo-name">okeysin İmaj FM</div>
        <div class="live-badge"><div class="live-dot"></div>CANLI</div>
        <!-- ÜST BAR EKSTRALAR -->
        <div class="top-extras">
          <button class="top-xbtn" id="sleepBtn" title="Uyku Zamanlayıcı"><i class="fas fa-moon"></i>UYKU</button>
          <button class="top-xbtn" id="themeBtn" title="Tema Seç"><i class="fas fa-palette"></i>TEMA</button>
          <button class="top-xbtn" id="eqBtn" title="Equalizer"><i class="fas fa-sliders"></i>EQ</button>
          <button class="top-xbtn" id="kbBtn" title="Kısayollar"><i class="fas fa-keyboard"></i></button>
          <button class="top-xbtn" id="fsBtn" title="Tam Ekran"><i class="fas fa-expand"></i></button>
        </div>
      </div>

      <!-- ALBÜM -->
      <div class="album-col">
        <div class="corner-tl"></div>
        <div class="vinyl-scene">
          <div class="bass-halo" id="bh1"></div>
          <div class="bass-halo" id="bh2"></div>
          <div class="bass-halo" id="bh3"></div>
          <div class="tonearm" id="tonearm">
            <svg viewBox="0 0 56 56" fill="none">
              <circle cx="50" cy="6" r="5.5" fill="#b0b0b0" stroke="rgba(255,255,255,.25)" stroke-width="1.2"/>
              <line x1="50" y1="11.5" x2="8" y2="52" stroke="#c8c8c8" stroke-width="2.8" stroke-linecap="round"/>
              <circle cx="8" cy="52" r="4.5" fill="#0d0d0d" stroke="var(--cy)" stroke-width="1.6"/>
              <circle cx="8" cy="52" r="2.2" fill="var(--cy)" opacity=".95"/>
            </svg>
          </div>
          <div class="vinyl" id="vinyl">
            <img src="https://images.unsplash.com/photo-1470225620780-dba8ba36b745?w=400"
                 id="coverImg" alt="Kapak" class="vinyl-img">
          </div>
        </div>
        <div class="spectrum-wrap">
          <canvas class="spectrum-canvas" id="specCanvas"></canvas>
        </div>
      </div>

      <!-- MERKEZ -->
      <div class="center-col">
        <div class="fnotes" id="fnotes">
          <i class="fas fa-music fn"></i><i class="fas fa-music fn"></i>
          <i class="fas fa-music fn"></i><i class="fas fa-music fn"></i>
          <i class="fas fa-music fn"></i><i class="fas fa-music fn"></i>
        </div>
        <div class="pts-layer" id="ptsLayer"></div>

        <div class="title-wrap">
          <span class="track-name" id="trackName">okeysin İmaj FM — Bağlanıyor...</span>
        </div>
        <div class="meta-row">
          <div class="dj-name"><i class="fas fa-microphone-lines"></i><span id="djLabel">Canlı Yayın</span></div>
          <div class="quality-tag">320 kbps · HD</div>
          <div class="listener-tag" id="listenerTag"><i class="fas fa-users"></i><span id="listenerCount">0</span> dinleyici</div>
          <div class="listen-timer" id="listenTimer"><i class="fas fa-stopwatch"></i><span id="listenTime">00:00:00</span></div>
        </div>
        <div class="ctrl-row">
          <div class="play-ring">
            <button class="play-btn" id="playBtn"><i class="fas fa-play" id="playIco"></i></button>
          </div>

          <div class="eq-canvas-wrap">
            <div class="eq-glow-layer">
              <div class="eq-glow-bars" id="eqGlow"></div>
            </div>
            <div class="eq-bars-wrap" id="eqWrap">
              <div class="eq-b"></div><div class="eq-b"></div><div class="eq-b"></div>
              <div class="eq-b"></div><div class="eq-b"></div><div class="eq-b"></div>
              <div class="eq-b"></div><div class="eq-b"></div><div class="eq-b"></div>
              <div class="eq-b"></div><div class="eq-b"></div><div class="eq-b"></div>
              <div class="eq-b"></div><div class="eq-b"></div><div class="eq-b"></div>
              <div class="eq-b"></div><div class="eq-b"></div><div class="eq-b"></div>
            </div>
          </div>

          <div class="status-row">
            <div class="s-chip chip-live"><i class="fas fa-tower-broadcast"></i>CANLI</div>
            <div class="s-chip chip-hd"><i class="fas fa-signal"></i>HD</div>
          </div>
        </div>
      </div>

      <!-- AKSİYONLAR -->
      <div class="actions-col">
        <button class="req-btn" id="reqBtn"><i class="fas fa-paper-plane"></i><span>İstek Yap</span></button>
        <div class="side-btns">
          <button class="s-btn" id="shareBtn" title="Paylaş"><i class="fas fa-share-nodes"></i></button>
          <button class="s-btn" id="heartBtn" title="Beğen"><i class="far fa-heart"></i></button>
          <button class="s-btn" id="historyBtn" title="Geçmiş"><i class="fas fa-clock-rotate-left"></i></button>
          <button class="s-btn" id="infoBtn" title="Bilgi"><i class="fas fa-circle-info"></i></button>
        </div>
      </div>

      <!-- SES -->
      <div class="vol-col">
        <div class="vol-lbl">Ses</div>
        <i class="fas fa-volume-high vol-ico" id="volIco"></i>
        <div class="vol-track" id="volTrack">
          <div class="vol-fill" id="volFill" style="height:70%"></div>
          <div class="vol-thumb" id="volThumb" style="bottom:calc(70% - 12px)"></div>
          <input type="range" class="vol-range" id="volRange" min="0" max="100" value="70">
        </div>
        <span class="vol-pct" id="volDisp">70%</span>
      </div>

    </div>
  </div>

  <!-- MESAJ WIDGET -->
  <div class="msg-wrap">
    <div class="msg-card">
      <div class="msg-top">
        <i class="fas fa-headphones-simple msg-top-ico"></i>
        <span class="msg-top-txt">Canlı Yayın &amp; Mesajlar</span>
        <div class="msg-top-badge">CANLI</div>
      </div>

      <div class="freq-band">
        <div class="freq-label">
          <span>FM</span>
          YAYINDA
        </div>
        <div class="freq-vis">
          <div class="freq-bars" id="freqBars"></div>
        </div>
        <div class="msg-ticker">
          <div class="msg-scroll" id="msgScroll"></div>
        </div>
      </div>

      <iframe src="https://okeysin.com/dj_panel/frame.php" class="req-frame" scrolling="no" title="Mesajlar"></iframe>
    </div>
  </div>

</div>

<script>
/* ════════════════════════════════════════════════════════
   CORE: AUDIO & ELEMENTS
════════════════════════════════════════════════════════ */
const aud = new Audio('https://radyocast.com/8028/Stream');
aud.volume = 0.7;
aud.crossOrigin = 'anonymous';
let playing = false;

const $ = id => document.getElementById(id);
const playBtn=$('playBtn'),playIco=$('playIco'),vinyl=$('vinyl'),tonearm=$('tonearm');
const eqWrap=$('eqWrap'),eqGlow=$('eqGlow'),trackName=$('trackName');
const djLabel=$('djLabel'),coverImg=$('coverImg');
const volRange=$('volRange'),volFill=$('volFill'),volThumb=$('volThumb');
const volDisp=$('volDisp'),volIco=$('volIco');
const toast=$('toast'),toastTxt=$('toastTxt');
const modal=$('modal'),connBar=$('connBar');
const bhalos=[$('bh1'),$('bh2'),$('bh3')];

/* ════════════════════════════════════════════════════════
   WEB AUDIO API — GERÇEK GÖRSELLEŞTIRME
════════════════════════════════════════════════════════ */
let audioCtx, analyser, sourceNode, dataArray;
function initAudioContext(){
  if(audioCtx) return;
  try{
    audioCtx = new (window.AudioContext || window.webkitAudioContext)();
    analyser = audioCtx.createAnalyser();
    analyser.fftSize = 256;
    analyser.smoothingTimeConstant = 0.8;
    dataArray = new Uint8Array(analyser.frequencyBinCount);
    sourceNode = audioCtx.createMediaElementSource(aud);

    // EQ Filtreleri oluştur
    createEQFilters();

    sourceNode.connect(eqFilters[0]);
    eqFilters[eqFilters.length-1].connect(analyser);
    analyser.connect(audioCtx.destination);
  } catch(e){
    console.log('Web Audio API hata:', e);
  }
}

/* ════════════════════════════════════════════════════════
   EQ FİLTRELERİ (Web Audio API)
════════════════════════════════════════════════════════ */
let eqFilters = [];
const eqFreqs = [60, 250, 1000, 4000, 16000];
const eqPresetValues = {
  flat:  [0, 0, 0, 0, 0],
  bass:  [10, 6, 0, -2, -4],
  vocal: [-2, 0, 6, 4, 0],
  rock:  [6, 2, -2, 4, 6],
  pop:   [2, 4, 6, 4, 2],
  jazz:  [4, 2, -2, 2, 6]
};

function createEQFilters(){
  if(!audioCtx) return;
  eqFilters = eqFreqs.map((freq, i) => {
    const filter = audioCtx.createBiquadFilter();
    filter.type = i === 0 ? 'lowshelf' : i === eqFreqs.length-1 ? 'highshelf' : 'peaking';
    filter.frequency.value = freq;
    filter.gain.value = 0;
    filter.Q.value = 1;
    return filter;
  });
  // Chain
  for(let i = 0; i < eqFilters.length - 1; i++){
    eqFilters[i].connect(eqFilters[i+1]);
  }
}

function applyEQPreset(name){
  const vals = eqPresetValues[name] || eqPresetValues.flat;
  eqFilters.forEach((f, i) => {
    f.gain.value = vals[i];
    const slider = document.querySelector(`#eqSliders input[data-band="${i}"]`);
    if(slider) slider.value = vals[i];
    const lbl = $('eqv'+i);
    if(lbl) lbl.textContent = vals[i] > 0 ? '+'+vals[i] : vals[i];
  });
}

// EQ Preset tıklamaları
document.querySelectorAll('.eq-preset').forEach(el => {
  el.addEventListener('click', () => {
    document.querySelectorAll('.eq-preset').forEach(e => e.classList.remove('active'));
    el.classList.add('active');
    const preset = el.dataset.preset;
    if(eqFilters.length) applyEQPreset(preset);
    showToast(`🎛️ EQ: ${el.querySelector('.eq-preset-name').textContent}`, 'fa-sliders');
  });
});

// EQ Slider değişimleri
document.querySelectorAll('#eqSliders input').forEach(sl => {
  sl.addEventListener('input', () => {
    const band = +sl.dataset.band;
    const val = +sl.value;
    if(eqFilters[band]) eqFilters[band].gain.value = val;
    const lbl = $('eqv'+band);
    if(lbl) lbl.textContent = val > 0 ? '+'+val : val;
    document.querySelectorAll('.eq-preset').forEach(e => e.classList.remove('active'));
  });
});

/* ════════════════════════════════════════════════════════
   GLOW EQ BARS
════════════════════════════════════════════════════════ */
const eqColors=[
  ['#00f5ff','#8338ec'],['#ff006e','#ff6b35'],['#8338ec','#00f5ff'],
  ['#ffd700','#ff006e'],['#00f5ff','#39ff14'],['#ff006e','#8338ec'],
  ['#39ff14','#00f5ff'],['#8338ec','#ff006e'],['#ff6b35','#ffd700'],
  ['#00f5ff','#ff006e'],['#ff006e','#ffd700'],['#8338ec','#39ff14'],
  ['#ffd700','#8338ec'],['#39ff14','#ff006e'],['#00f5ff','#8338ec'],
  ['#ff006e','#00f5ff'],['#8338ec','#ffd700'],['#00f5ff','#ff6b35']
];
const phArr=[38,44,32,40,36,44,30,42,34,40,28,44,32,42,26,38,44,30];
const spdArr=['0.58s','0.65s','0.52s','0.72s','0.60s','0.68s','0.55s','0.75s','0.62s','0.70s','0.58s','0.66s','0.53s','0.78s','0.61s','0.69s','0.57s','0.74s'];
const dlyArr=['0.00s','0.06s','0.12s','0.04s','0.18s','0.10s','0.22s','0.08s','0.16s','0.14s','0.20s','0.02s','0.24s','0.07s','0.28s','0.11s','0.15s','0.19s'];

for(let i=0;i<18;i++){
  const g=document.createElement('div');
  g.className='eq-g';
  g.style.cssText=`width:5px;min-height:4px;border-radius:4px;flex-shrink:0;background:linear-gradient(to top,${eqColors[i][0]},${eqColors[i][1]});box-shadow:0 0 16px ${eqColors[i][0]},0 0 32px ${eqColors[i][0]};--spd:${spdArr[i]};--dly:${dlyArr[i]};--ph:${phArr[i]}px;`;
  eqGlow.appendChild(g);
}

/* ════════════════════════════════════════════════════════
   PARÇACIKLAR
════════════════════════════════════════════════════════ */
const ptColors=['var(--cy)','var(--pk)','var(--pu)','var(--gd)','var(--or)','var(--gn)'];
const ptsLayer=$('ptsLayer');
for(let i=0;i<36;i++){
  const p=document.createElement('div');
  p.className='pt';
  const sz=Math.random()*4+2;
  p.style.cssText=`left:${Math.random()*100}%;width:${sz}px;height:${sz}px;background:${ptColors[i%ptColors.length]};box-shadow:0 0 12px ${ptColors[i%ptColors.length]};--tx:${(Math.random()*160-80).toFixed(0)}px;--d:${(3+Math.random()*3.5).toFixed(2)}s;--dl:${(Math.random()*5.5).toFixed(2)}s;`;
  ptsLayer.appendChild(p);
}

/* ════════════════════════════════════════════════════════
   FREKANS BARLARI
════════════════════════════════════════════════════════ */
const freqBars=$('freqBars');
const fhArr=[12,20,28,16,32,24,36,14,28,22,34,18,26,30,16,38,20,28,14,32,24,18,36,22,16,30,26,20,34,12,28,22,18,36,24,16,30,28,20,32,14,26,22,18,36,24,16,30];
for(let i=0;i<48;i++){
  const fb=document.createElement('div');
  fb.className='fb';
  const sp=(0.4+Math.random()*0.5).toFixed(2)+'s';
  const dl=(Math.random()*0.4).toFixed(2)+'s';
  fb.style.cssText=`--fs:${sp};--fd:${dl};--fh:${fhArr[i%fhArr.length]}px;`;
  freqBars.appendChild(fb);
}

/* ════════════════════════════════════════════════════════
   PLAY / PAUSE
════════════════════════════════════════════════════════ */
function setPlayState(on){
  const action = on ? 'add' : 'remove';
  vinyl.classList[action]('spin');
  tonearm.classList[action]('on');
  eqWrap.querySelectorAll('.eq-b').forEach(b=>b.classList[action]('playing'));
  eqGlow.querySelectorAll('.eq-g').forEach(g=>g.classList[action]('playing'));
  $('fnotes').querySelectorAll('.fn').forEach(n=>n.classList[action]('on'));
  ptsLayer.querySelectorAll('.pt').forEach(p=>p.classList[action]('on'));
  bhalos.forEach(b=>b.classList[action]('on'));
  freqBars.querySelectorAll('.fb').forEach(f=>f.classList[action]('on'));

  if(on){
    startSpecCanvas();
    startListenTimer();
    playIco.className='fas fa-pause';
    $('miniPlayIco').className='fas fa-pause';
    $('miniArt').classList.add('spin');
    updateMediaSession();
  } else {
    stopSpecCanvas();
    stopListenTimer();
    playIco.className='fas fa-play';
    $('miniPlayIco').className='fas fa-play';
    $('miniArt').classList.remove('spin');
  }
}

function togglePlay(){
  if(playing){
    aud.pause();
    playing=false;
    setPlayState(false);
  } else {
    initAudioContext();
    aud.play().catch(()=>{});
    playing=true;
    setPlayState(true);
  }
}

playBtn.addEventListener('click', togglePlay);
$('miniPlay').addEventListener('click', togglePlay);

/* ════════════════════════════════════════════════════════
   SPECTRUM CANVAS — GERÇEK VERİ
════════════════════════════════════════════════════════ */
const specCanvas=$('specCanvas');
const sCtx=specCanvas.getContext('2d');
let specRaf=null;
const specH=[];
const specN=40;
for(let i=0;i<specN;i++) specH.push(Math.random()*10+2);

function drawSpec(){
  const W=specCanvas.offsetWidth;
  const H=specCanvas.offsetHeight;
  specCanvas.width=W;specCanvas.height=H;
  sCtx.clearRect(0,0,W,H);

  // Gerçek ses verisini kullan
  if(analyser && dataArray){
    analyser.getByteFrequencyData(dataArray);
  }

  const bw=(W/specN)-1;
  for(let i=0;i<specN;i++){
    let h;
    if(analyser && dataArray && playing){
      const idx = Math.floor(i * dataArray.length / specN);
      h = (dataArray[idx] / 255) * (H - 2);
      h = Math.max(2, h);
    } else {
      specH[i]+=(Math.random()*12-6);
      specH[i]=Math.max(2,Math.min(H-2,specH[i]));
      h = specH[i];
    }
    const x=i*(bw+1);
    const grd=sCtx.createLinearGradient(0,H,0,H-h);
    const hue=200+i*4;
    grd.addColorStop(0,`hsl(${hue},100%,55%)`);
    grd.addColorStop(1,`hsl(${(hue+80)%360},100%,70%)`);
    sCtx.fillStyle=grd;
    sCtx.shadowColor=`hsl(${hue},100%,60%)`;
    sCtx.shadowBlur=8;
    sCtx.fillRect(x,H-h,bw,h);
  }
  specRaf=requestAnimationFrame(drawSpec);
}
function startSpecCanvas(){if(!specRaf) drawSpec();}
function stopSpecCanvas(){if(specRaf){cancelAnimationFrame(specRaf);specRaf=null;sCtx.clearRect(0,0,specCanvas.width,specCanvas.height);}}

/* ════════════════════════════════════════════════════════
   SES KONTROLÜ
════════════════════════════════════════════════════════ */
let prevVol = 70;
function setVol(v){
  v=Math.max(0,Math.min(100,v));
  aud.volume=v/100;
  volFill.style.height=v+'%';
  volThumb.style.bottom='calc('+v+'% - 12px)';
  volDisp.textContent=v+'%';
  volRange.value=v;
  volIco.className=v===0?'fas fa-volume-xmark vol-ico':v<40?'fas fa-volume-low vol-ico':'fas fa-volume-high vol-ico';
  localStorage.setItem('imajfm_vol', v);
}
// Kayıtlı ses seviyesi
const savedVol = localStorage.getItem('imajfm_vol');
setVol(savedVol !== null ? +savedVol : 70);

volRange.addEventListener('input',e=>setVol(+e.target.value));
volIco.addEventListener('click',()=>{
  if(aud.volume>0){prevVol=Math.round(aud.volume*100);setVol(0);}
  else setVol(prevVol||70);
});

/* ════════════════════════════════════════════════════════
   BAĞLANTI DURUMU İZLEME
════════════════════════════════════════════════════════ */
aud.addEventListener('waiting', () => {
  connBar.className = 'conn-bar buffering';
});
aud.addEventListener('playing', () => {
  connBar.className = 'conn-bar connected';
});
aud.addEventListener('error', () => {
  connBar.className = 'conn-bar disconnected';
  showToast('⚠️ Bağlantı hatası! Tekrar deneniyor...', 'fa-exclamation-triangle');
  // Otomatik yeniden bağlan
  setTimeout(() => {
    if(playing){
      aud.load();
      aud.play().catch(()=>{});
    }
  }, 3000);
});
aud.addEventListener('stalled', () => {
  connBar.className = 'conn-bar buffering';
});

// Network durumu izleme
window.addEventListener('online', () => {
  showToast('✅ İnternet bağlantısı geri geldi', 'fa-wifi');
  connBar.className = 'conn-bar connected';
  if(playing){aud.load();aud.play().catch(()=>{});}
});
window.addEventListener('offline', () => {
  showToast('❌ İnternet bağlantısı kesildi', 'fa-wifi');
  connBar.className = 'conn-bar disconnected';
});

/* ════════════════════════════════════════════════════════
   MODAL
════════════════════════════════════════════════════════ */
$('reqBtn').addEventListener('click',()=>modal.classList.add('open'));
$('modalClose').addEventListener('click',()=>modal.classList.remove('open'));
modal.addEventListener('click',e=>{if(e.target===modal)modal.classList.remove('open');});

/* ════════════════════════════════════════════════════════
   TOAST
════════════════════════════════════════════════════════ */
function showToast(msg,ico='fa-check-circle'){
  toastTxt.textContent=msg;
  toast.querySelector('i').className=`fas ${ico}`;
  toast.classList.add('show');
  clearTimeout(toast._t);
  toast._t=setTimeout(()=>toast.classList.remove('show'),3200);
}

/* ════════════════════════════════════════════════════════
   YENİ: DİNLEME SÜRESİ SAYACI
════════════════════════════════════════════════════════ */
let listenSeconds = 0;
let listenInterval = null;
function startListenTimer(){
  if(listenInterval) return;
  listenInterval = setInterval(() => {
    listenSeconds++;
    const h = String(Math.floor(listenSeconds/3600)).padStart(2,'0');
    const m = String(Math.floor((listenSeconds%3600)/60)).padStart(2,'0');
    const s = String(listenSeconds%60).padStart(2,'0');
    $('listenTime').textContent = `${h}:${m}:${s}`;
  }, 1000);
}
function stopListenTimer(){
  if(listenInterval){clearInterval(listenInterval);listenInterval=null;}
}

/* ════════════════════════════════════════════════════════
   YENİ: ŞARKI GEÇMİŞİ
════════════════════════════════════════════════════════ */
let trackHistory = JSON.parse(localStorage.getItem('imajfm_history') || '[]');
let lastTrackTitle = '';

function addToHistory(title){
  if(!title || title === lastTrackTitle || title.includes('Bağlanıyor')) return;
  lastTrackTitle = title;
  const item = {title, time: new Date().toLocaleTimeString('tr-TR')};
  trackHistory.unshift(item);
  if(trackHistory.length > 50) trackHistory.pop();
  localStorage.setItem('imajfm_history', JSON.stringify(trackHistory));
  renderHistory();
}

function renderHistory(){
  const list = $('historyList');
  if(trackHistory.length === 0){
    list.innerHTML = '<div class="hp-empty"><i class="fas fa-music" style="font-size:24px;margin-bottom:10px;display:block;color:var(--pu);"></i>Henüz şarkı geçmişi yok</div>';
    return;
  }
  list.innerHTML = trackHistory.map((h, i) =>
    `<div class="hp-item">
      <div class="hp-num">${i+1}</div>
      <div class="hp-info">
        <div class="hp-title">${h.title}</div>
        <div class="hp-time">${h.time}</div>
      </div>
    </div>`
  ).join('');
}
renderHistory();

$('historyBtn').addEventListener('click', () => {
  $('historyPanel').classList.toggle('open');
});
$('historyClose').addEventListener('click', () => {
  $('historyPanel').classList.remove('open');
});

/* ════════════════════════════════════════════════════════
   YENİ: SLEEP TIMER
════════════════════════════════════════════════════════ */
let sleepTimer = null;
let sleepRemaining = 0;
let sleepInterval = null;

$('sleepBtn').addEventListener('click', (e) => {
  e.stopPropagation();
  $('sleepPanel').classList.toggle('open');
  $('themePanel').classList.remove('open');
});

document.querySelectorAll('.sleep-opt').forEach(el => {
  el.addEventListener('click', () => {
    const min = +el.dataset.min;
    document.querySelectorAll('.sleep-opt').forEach(e => e.classList.remove('active'));
    el.classList.add('active');
    startSleepTimer(min);
  });
});

function startSleepTimer(minutes){
  clearTimeout(sleepTimer);
  clearInterval(sleepInterval);
  sleepRemaining = minutes * 60;
  $('sleepCountdown').classList.add('show');
  $('sleepCancel').classList.add('show');
  $('sleepBtn').classList.add('sleep-active');

  sleepInterval = setInterval(() => {
    sleepRemaining--;
    const m = String(Math.floor(sleepRemaining/60)).padStart(2,'0');
    const s = String(sleepRemaining%60).padStart(2,'0');
    $('sleepCountdown').textContent = `${m}:${s}`;
    // Son 30 saniye — volume fade
    if(sleepRemaining <= 30 && sleepRemaining > 0 && playing){
      const fadeVol = Math.round((sleepRemaining / 30) * aud.volume * 100);
      setVol(Math.max(0, fadeVol));
    }
    if(sleepRemaining <= 0){
      clearInterval(sleepInterval);
      if(playing) togglePlay();
      showToast('😴 Uyku zamanlayıcısı — İyi geceler!', 'fa-moon');
      cancelSleepTimer();
    }
  }, 1000);

  showToast(`⏰ ${minutes} dakika sonra kapanacak`, 'fa-moon');
}

function cancelSleepTimer(){
  clearTimeout(sleepTimer);
  clearInterval(sleepInterval);
  sleepRemaining = 0;
  $('sleepCountdown').classList.remove('show');
  $('sleepCancel').classList.remove('show');
  $('sleepBtn').classList.remove('sleep-active');
  document.querySelectorAll('.sleep-opt').forEach(e => e.classList.remove('active'));
}

$('sleepCancel').addEventListener('click', () => {
  cancelSleepTimer();
  showToast('⏰ Zamanlayıcı iptal edildi', 'fa-times-circle');
});

/* ════════════════════════════════════════════════════════
   YENİ: TEMA SİSTEMİ
════════════════════════════════════════════════════════ */
let currentTheme = localStorage.getItem('imajfm_theme') || 'neon';
document.documentElement.setAttribute('data-theme', currentTheme);
document.querySelector(`.theme-dot[data-theme="${currentTheme}"]`)?.classList.add('active');

$('themeBtn').addEventListener('click', (e) => {
  e.stopPropagation();
  $('themePanel').classList.toggle('open');
  $('sleepPanel').classList.remove('open');
});

document.querySelectorAll('.theme-dot').forEach(el => {
  el.addEventListener('click', () => {
    document.querySelectorAll('.theme-dot').forEach(e => e.classList.remove('active'));
    el.classList.add('active');
    currentTheme = el.dataset.theme;
    document.documentElement.setAttribute('data-theme', currentTheme);
    localStorage.setItem('imajfm_theme', currentTheme);
    showToast(`🎨 Tema: ${currentTheme.toUpperCase()}`, 'fa-palette');
  });
});

/* ════════════════════════════════════════════════════════
   YENİ: EQ PANELİ AÇMA/KAPAMA
════════════════════════════════════════════════════════ */
$('eqBtn').addEventListener('click', () => {
  $('eqPanel').classList.toggle('open');
});
$('eqClose').addEventListener('click', () => {
  $('eqPanel').classList.remove('open');
});

/* ════════════════════════════════════════════════════════
   YENİ: KLAVYE KISAYOLLARI
════════════════════════════════════════════════════════ */
$('kbBtn').addEventListener('click', () => {
  $('shortcutPanel').classList.toggle('open');
});
$('scClose').addEventListener('click', () => {
  $('shortcutPanel').classList.remove('open');
});

const themeList = ['neon','sunset','ocean','forest','purple','retro'];

document.addEventListener('keydown', e => {
  // Modal açıkken ESC tuşu
  if(e.key === 'Escape'){
    modal.classList.remove('open');
    $('historyPanel').classList.remove('open');
    $('sleepPanel').classList.remove('open');
    $('themePanel').classList.remove('open');
    $('eqPanel').classList.remove('open');
    $('shortcutPanel').classList.remove('open');
    return;
  }
  // Input/textarea içinde kısayolları devre dışı bırak
  if(['INPUT','TEXTAREA','SELECT'].includes(document.activeElement.tagName)) return;

  switch(e.key.toLowerCase()){
    case ' ':
      e.preventDefault();
      togglePlay();
      break;
    case 'arrowup':
      e.preventDefault();
      setVol(Math.round(aud.volume*100)+5);
      break;
    case 'arrowdown':
      e.preventDefault();
      setVol(Math.round(aud.volume*100)-5);
      break;
    case 'm':
      if(aud.volume>0){prevVol=Math.round(aud.volume*100);setVol(0);}
      else setVol(prevVol||70);
      break;
    case 'h':
      $('historyPanel').classList.toggle('open');
      break;
    case 't':
      // Sonraki tema
      const cIdx = themeList.indexOf(currentTheme);
      const nIdx = (cIdx + 1) % themeList.length;
      document.querySelectorAll('.theme-dot').forEach(e => e.classList.remove('active'));
      document.querySelector(`.theme-dot[data-theme="${themeList[nIdx]}"]`).classList.add('active');
      currentTheme = themeList[nIdx];
      document.documentElement.setAttribute('data-theme', currentTheme);
      localStorage.setItem('imajfm_theme', currentTheme);
      showToast(`🎨 Tema: ${currentTheme.toUpperCase()}`, 'fa-palette');
      break;
    case 'e':
      $('eqPanel').classList.toggle('open');
      break;
    case 'f':
      toggleFullscreen();
      break;
    case '?':
      $('shortcutPanel').classList.toggle('open');
      break;
  }
});

/* ════════════════════════════════════════════════════════
   YENİ: TAM EKRAN
════════════════════════════════════════════════════════ */
function toggleFullscreen(){
  if(!document.fullscreenElement){
    document.documentElement.requestFullscreen().catch(()=>{});
    $('fsBtn').querySelector('i').className = 'fas fa-compress';
    showToast('🖥️ Tam Ekran Modu', 'fa-expand');
  } else {
    document.exitFullscreen();
    $('fsBtn').querySelector('i').className = 'fas fa-expand';
  }
}
$('fsBtn').addEventListener('click', toggleFullscreen);
document.addEventListener('fullscreenchange', () => {
  if(!document.fullscreenElement){
    $('fsBtn').querySelector('i').className = 'fas fa-expand';
  }
});

/* ════════════════════════════════════════════════════════
   YENİ: MİNİ PLAYER (Scroll ile)
════════════════════════════════════════════════════════ */
let miniMode = false;
const mainContainer = $('mainContainer');
const holoFrame = $('holoFrame');

function checkMiniPlayer(){
  if(!mainContainer) return;
  const rect = holoFrame.getBoundingClientRect();
  const isOut = rect.bottom < -50;
  if(isOut && !miniMode){
    miniMode = true;
    $('miniPlayer').classList.add('show');
  } else if(!isOut && miniMode){
    miniMode = false;
    $('miniPlayer').classList.remove('show');
  }
}

window.addEventListener('scroll', checkMiniPlayer, {passive: true});

$('miniClose').addEventListener('click', () => {
  $('miniPlayer').classList.remove('show');
  holoFrame.scrollIntoView({behavior: 'smooth', block: 'center'});
});

/* ════════════════════════════════════════════════════════
   YENİ: MEDIA SESSION API (OS Kontrolleri)
════════════════════════════════════════════════════════ */
function updateMediaSession(){
  if(!('mediaSession' in navigator)) return;
  navigator.mediaSession.metadata = new MediaMetadata({
    title: trackName.textContent || 'okeysin İmaj FM',
    artist: djLabel.textContent || 'Canlı Yayın',
    album: 'okeysin İmaj FM',
    artwork: [
      {src: coverImg.src, sizes: '400x400', type: 'image/jpeg'}
    ]
  });
  navigator.mediaSession.setActionHandler('play', () => {if(!playing) togglePlay();});
  navigator.mediaSession.setActionHandler('pause', () => {if(playing) togglePlay();});
}

/* ════════════════════════════════════════════════════════
   YENİ: SCREEN WAKE LOCK
════════════════════════════════════════════════════════ */
let wakeLock = null;
async function requestWakeLock(){
  if('wakeLock' in navigator && playing){
    try{
      wakeLock = await navigator.wakeLock.request('screen');
      wakeLock.addEventListener('release', () => {wakeLock = null;});
    }catch(e){}
  }
}
function releaseWakeLock(){
  if(wakeLock){wakeLock.release();wakeLock=null;}
}
// Play/pause ile otomatik
const origToggle = togglePlay;

/* ════════════════════════════════════════════════════════
   BUTONLAR
════════════════════════════════════════════════════════ */
$('shareBtn').addEventListener('click',()=>{
  if(navigator.share){navigator.share({title:'okeysin İmaj FM',text:`🎵 ${trackName.textContent}`,url:location.href}).catch(()=>{});}
  else {navigator.clipboard.writeText(location.href).then(()=>showToast('🔗 Link kopyalandı!','fa-link'));}
});

let liked = localStorage.getItem('imajfm_liked') === 'true';
const heartBtn = $('heartBtn');
function updateHeartUI(){
  heartBtn.querySelector('i').className = liked ? 'fas fa-heart' : 'far fa-heart';
  heartBtn.classList.toggle('liked', liked);
}
updateHeartUI();

heartBtn.addEventListener('click',function(){
  liked = !liked;
  localStorage.setItem('imajfm_liked', liked);
  updateHeartUI();
  if(liked) showToast('❤️ Beğendiniz!','fa-heart');
});

$('infoBtn').addEventListener('click',()=>showToast('📡 okeysin İmaj FM — 7/24 Kesintisiz','fa-circle-info'));

/* ════════════════════════════════════════════════════════
   MESAJ ŞERİDİ
════════════════════════════════════════════════════════ */
const defaultMsgs=['🎵 Bugün harika bir yayın!','❤️ Sizi çok seviyoruz','🎤 İstek şarkınızı gönderin','🌟 En iyi müzik burada','🎧 Sesinizin adresi','💫 okeysin.com ile müzik'];
function buildMsgScroll(arr){
  const all=[...arr,...arr];
  $('msgScroll').innerHTML=all.map(m=>
    `<span class="msg-item"><i class="fas fa-star"></i>${m}</span>`
  ).join('');
}
buildMsgScroll(defaultMsgs);

/* ════════════════════════════════════════════════════════
   RADYO BİLGİSİ ÇEKME
════════════════════════════════════════════════════════ */
function decHtml(h){const t=document.createElement('textarea');t.innerHTML=h;return t.value;}

async function fetchInfo(){
  try{
    const r=await fetch('https://radyocast.com/cp/get_info.php?p=8028');
    const d=await r.json();
    if(d.title){
      const t=decHtml(d.title);
      trackName.textContent=t;
      $('miniTitle').textContent=t;

      // Geçmişe ekle
      addToHistory(t);

      // Media Session güncelle
      updateMediaSession();

      requestAnimationFrame(()=>{
        const wrap=trackName.closest('.title-wrap');
        if(wrap&&trackName.scrollWidth>wrap.clientWidth){
          const diff=-(trackName.scrollWidth-wrap.clientWidth+30);
          trackName.style.setProperty('--mqx',diff+'px');
          trackName.classList.add('marquee');
        } else trackName.classList.remove('marquee');
      });
    }
    if(d.dj) djLabel.textContent=decHtml(d.dj);
    if(d.art){
      coverImg.src=d.art;
      $('miniArt').src=d.art;
    }
    // Dinleyici sayısı
    if(d.listeners !== undefined){
      $('listenerCount').textContent = d.listeners;
    } else if(d.uniquelisteners !== undefined){
      $('listenerCount').textContent = d.uniquelisteners;
    }
  } catch(e){
    console.log('Bilgi çekme hatası:', e);
  }
}

// Dinleyici sayısını ayrı endpoint'ten çekmeyi dene
async function fetchListeners(){
  try{
    const r = await fetch('https://radyocast.com/cp/get_info.php?p=8028');
    const d = await r.json();
    if(d.listeners !== undefined){
      $('listenerCount').textContent = d.listeners;
    } else if(d.currentlisteners !== undefined){
      $('listenerCount').textContent = d.currentlisteners;
    }
  } catch(e){}
}

fetchInfo();
setInterval(fetchInfo, 12000);
setInterval(fetchListeners, 20000);

/* ════════════════════════════════════════════════════════
   PANEL DIŞ TIKLAMA İLE KAPATMA
════════════════════════════════════════════════════════ */
document.addEventListener('click', (e) => {
  // Sleep panel
  if(!$('sleepPanel').contains(e.target) && !$('sleepBtn').contains(e.target)){
    $('sleepPanel').classList.remove('open');
  }
  // Theme panel
  if(!$('themePanel').contains(e.target) && !$('themeBtn').contains(e.target)){
    $('themePanel').classList.remove('open');
  }
  // EQ panel
  if(!$('eqPanel').contains(e.target) && !$('eqBtn').contains(e.target)){
    $('eqPanel').classList.remove('open');
  }
  // Shortcut panel
  if(!$('shortcutPanel').contains(e.target) && !$('kbBtn').contains(e.target)){
    $('shortcutPanel').classList.remove('open');
  }
});

/* ════════════════════════════════════════════════════════
   WAKE LOCK ENTEGRASYONu
════════════════════════════════════════════════════════ */
// Oynama durumuna göre wake lock al/bırak
aud.addEventListener('play', () => {
  requestWakeLock();
});
aud.addEventListener('pause', () => {
  releaseWakeLock();
});
// Sekme tekrar görünür olunca wake lock yenile
document.addEventListener('visibilitychange', () => {
  if(document.visibilityState === 'visible' && playing){
    requestWakeLock();
  }
});

/* ════════════════════════════════════════════════════════
   YENİ: SAYFA BAŞLIĞINDA ŞARKI ADI GÖSTERİMİ
════════════════════════════════════════════════════════ */
let titleRotateInterval = null;
let titleIndex = 0;
const originalTitle = document.title;

function startTitleRotation(){
  if(titleRotateInterval) return;
  titleRotateInterval = setInterval(() => {
    const current = trackName.textContent || 'okeysin İmaj FM';
    if(titleIndex % 2 === 0){
      document.title = `🎵 ${current}`;
    } else {
      document.title = `▶ okeysin İmaj FM — Canlı`;
    }
    titleIndex++;
  }, 3000);
}

function stopTitleRotation(){
  if(titleRotateInterval){
    clearInterval(titleRotateInterval);
    titleRotateInterval = null;
  }
  document.title = originalTitle;
}

aud.addEventListener('play', startTitleRotation);
aud.addEventListener('pause', stopTitleRotation);

/* ════════════════════════════════════════════════════════
   YENİ: SES SEVİYESİ FARE TEKERLEĞİ
════════════════════════════════════════════════════════ */
$('volTrack').addEventListener('wheel', (e) => {
  e.preventDefault();
  const delta = e.deltaY < 0 ? 5 : -5;
  setVol(Math.round(aud.volume * 100) + delta);
}, {passive: false});

// Ana player üzerinde de çalışsın
$('player').addEventListener('wheel', (e) => {
  if(e.target.closest('.vol-col')) return; // zaten volTrack handle ediyor
  e.preventDefault();
  const delta = e.deltaY < 0 ? 3 : -3;
  setVol(Math.round(aud.volume * 100) + delta);
}, {passive: false});

/* ════════════════════════════════════════════════════════
   YENİ: ÇİFT TIKLAMA İLE TAM EKRAN
════════════════════════════════════════════════════════ */
$('player').addEventListener('dblclick', (e) => {
  // Butonlara çift tıklama durumunda tam ekran açılmasın
  if(e.target.closest('button') || e.target.closest('.s-btn') || e.target.closest('.vol-col')) return;
  toggleFullscreen();
});

/* ════════════════════════════════════════════════════════
   YENİ: OTOMATİK YENİDEN BAĞLANMA
════════════════════════════════════════════════════════ */
let reconnectAttempts = 0;
const maxReconnect = 5;
let reconnectTimeout = null;

aud.addEventListener('error', () => {
  if(!playing) return;
  reconnectAttempts++;
  if(reconnectAttempts <= maxReconnect){
    const delay = Math.min(reconnectAttempts * 3000, 15000);
    showToast(`🔄 Yeniden bağlanılıyor... (${reconnectAttempts}/${maxReconnect})`, 'fa-rotate');
    connBar.className = 'conn-bar disconnected';
    reconnectTimeout = setTimeout(() => {
      aud.src = 'https://radyocast.com/8028/Stream';
      aud.load();
      aud.play().then(() => {
        reconnectAttempts = 0;
        connBar.className = 'conn-bar connected';
        showToast('✅ Yeniden bağlandı!', 'fa-check-circle');
      }).catch(() => {});
    }, delay);
  } else {
    showToast('❌ Bağlantı kurulamadı. Lütfen tekrar deneyin.', 'fa-times-circle');
    playing = false;
    setPlayState(false);
    reconnectAttempts = 0;
  }
});

aud.addEventListener('playing', () => {
  reconnectAttempts = 0;
  if(reconnectTimeout){clearTimeout(reconnectTimeout);reconnectTimeout=null;}
});

/* ════════════════════════════════════════════════════════
   YENİ: HATIRLATMA — SON OTURUM BİLGİSİ
════════════════════════════════════════════════════════ */
(function showWelcome(){
  const lastVisit = localStorage.getItem('imajfm_lastvisit');
  const now = Date.now();
  localStorage.setItem('imajfm_lastvisit', now);

  if(lastVisit){
    const diff = now - (+lastVisit);
    const hours = Math.floor(diff / 3600000);
    if(hours >= 1 && hours < 24){
      setTimeout(() => showToast(`👋 Tekrar hoş geldiniz! (${hours} saat önce buraydınız)`, 'fa-hand-wave'), 1500);
    } else if(hours >= 24){
      const days = Math.floor(hours / 24);
      setTimeout(() => showToast(`👋 ${days} gündür görüşmüyorduk! Hoş geldiniz`, 'fa-hand-wave'), 1500);
    }
  } else {
    setTimeout(() => showToast('🎉 okeysin İmaj FM\'e hoş geldiniz!', 'fa-star'), 1500);
  }
})();

/* ════════════════════════════════════════════════════════
   YENİ: KAYIT/PAYLAŞ — ŞU AN ÇALANI KOPYALA
════════════════════════════════════════════════════════ */
trackName.addEventListener('click', () => {
  const text = trackName.textContent;
  if(!text || text.includes('Bağlanıyor')) return;
  navigator.clipboard.writeText(text).then(() => {
    showToast('📋 Şarkı adı kopyalandı!', 'fa-copy');
  }).catch(()=>{});
});
trackName.style.cursor = 'pointer';
trackName.title = 'Tıklayarak şarkı adını kopyala';

/* ════════════════════════════════════════════════════════
   YENİ: PERFORMANS — SAYFA GİZLİYKEN ANİMASYON DURDUR
════════════════════════════════════════════════════════ */
document.addEventListener('visibilitychange', () => {
  if(document.hidden){
    // Spectrum canvas durdur (ses devam eder)
    if(specRaf){cancelAnimationFrame(specRaf);specRaf=null;}
  } else {
    // Sayfa görünür olduğunda animasyonu tekrar başlat
    if(playing) startSpecCanvas();
  }
});

/* ════════════════════════════════════════════════════════
   İLK YÜKLEMEDEKİ FADE-IN
════════════════════════════════════════════════════════ */
window.addEventListener('load', () => {
  document.body.style.opacity = '0';
  document.body.style.transition = 'opacity 0.8s ease';
  requestAnimationFrame(() => {
    document.body.style.opacity = '1';
  });
});
</script>
</body>
</html>. Yeni görsel modern player oluştur daha görsel yaratıcı renkler tasarım la geliştirmeye devam edelim özgür gelişmiş tam kodu yaz 

### Concord Grape 2
*2026-03-15 14:43:29 +03*



# 🎵 okeysin İmaj FM — Ultra Modern Player V2

Tamamen yeniden tasarlanmış, görsel olarak çok daha yaratıcı ve modern bir player oluşturdum. İşte öne çıkan yenilikler:

```html
<!DOCTYPE html>
<html lang="tr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>okeysin İmaj FM</title>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
<style>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Rajdhani:wght@300;400;500;600;700&family=Audiowide&display=swap');

:root{
  --pk:#ff2d75;--cy:#00e5ff;--pu:#b026ff;
  --gn:#00ff87;--gd:#ffbe0b;--or:#ff6d00;
  --bg:#030108;--glass:rgba(255,255,255,.04);
  --neon-pink:0 0 20px #ff2d75,0 0 40px #ff2d7566;
  --neon-cyan:0 0 20px #00e5ff,0 0 40px #00e5ff66;
  --neon-purple:0 0 20px #b026ff,0 0 40px #b026ff66;
}

[data-theme="neon"]{--pk:#ff2d75;--cy:#00e5ff;--pu:#b026ff;--gn:#00ff87;--gd:#ffbe0b;--or:#ff6d00;}
[data-theme="cyberpunk"]{--pk:#f7e018;--cy:#e92efb;--pu:#1b1b2f;--gn:#ff2a6d;--gd:#05d9e8;--or:#d1f7ff;}
[data-theme="aurora"]{--pk:#43e97b;--cy:#38f9d7;--pu:#667eea;--gn:#764ba2;--gd:#f093fb;--or:#4facfe;}
[data-theme="lava"]{--pk:#ff0844;--cy:#ffb199;--pu:#ff3d00;--gn:#ff6e40;--gd:#ffd740;--or:#ff9100;}
[data-theme="midnight"]{--pk:#667eea;--cy:#764ba2;--pu:#f093fb;--gn:#4facfe;--gd:#00f2fe;--or:#43e97b;}
[data-theme="vapor"]{--pk:#ff71ce;--cy:#01cdfe;--pu:#b967ff;--gn:#05ffa1;--gd:#fffb96;--or:#ff6e6e;}

*{margin:0;padding:0;box-sizing:border-box;}
html{scroll-behavior:smooth;}
body{
  background:var(--bg);
  font-family:'Rajdhani',sans-serif;
  min-height:100vh;
  overflow-x:hidden;
  color:#fff;
}

/* ═══════ ANIMATED BG ═══════ */
.bg-scene{
  position:fixed;inset:0;z-index:0;pointer-events:none;
  overflow:hidden;
}
.bg-orb{
  position:absolute;border-radius:50%;filter:blur(80px);opacity:.18;
  animation:orbFloat 20s ease-in-out infinite;
}
.bg-orb:nth-child(1){width:600px;height:600px;background:var(--pk);top:-20%;left:-10%;animation-duration:25s;}
.bg-orb:nth-child(2){width:500px;height:500px;background:var(--cy);bottom:-15%;right:-8%;animation-duration:30s;animation-delay:-5s;}
.bg-orb:nth-child(3){width:400px;height:400px;background:var(--pu);top:40%;left:50%;animation-duration:22s;animation-delay:-10s;}
.bg-orb:nth-child(4){width:300px;height:300px;background:var(--gn);bottom:20%;left:20%;animation-duration:28s;animation-delay:-7s;}
@keyframes orbFloat{
  0%,100%{transform:translate(0,0) scale(1);}
  25%{transform:translate(80px,-60px) scale(1.15);}
  50%{transform:translate(-40px,80px) scale(.9);}
  75%{transform:translate(60px,40px) scale(1.1);}
}

/* Grid overlay */
.bg-grid{
  position:fixed;inset:0;z-index:0;pointer-events:none;
  background-image:
    linear-gradient(rgba(255,255,255,.015) 1px,transparent 1px),
    linear-gradient(90deg,rgba(255,255,255,.015) 1px,transparent 1px);
  background-size:60px 60px;
  animation:gridDrift 30s linear infinite;
}
@keyframes gridDrift{0%{background-position:0 0}100%{background-position:60px 60px}}

/* Scanlines */
.scanlines{
  position:fixed;inset:0;z-index:1;pointer-events:none;
  background:repeating-linear-gradient(0deg,transparent,transparent 2px,rgba(0,0,0,.06) 2px,rgba(0,0,0,.06) 4px);
}

/* ═══════ MAIN CONTAINER ═══════ */
.main-wrap{
  position:relative;z-index:10;
  max-width:1100px;margin:30px auto;padding:0 16px;
}

/* ═══════ GLASSMORPHIC FRAME ═══════ */
@property --border-angle{syntax:'<angle>';initial-value:0deg;inherits:false;}
@keyframes borderSpin{to{--border-angle:360deg;}}

.player-frame{
  position:relative;
  border-radius:32px;
  padding:2px;
  background:conic-gradient(from var(--border-angle),
    var(--pu),var(--pk),var(--cy),var(--gn),var(--gd),var(--pk),var(--pu));
  animation:borderSpin 6s linear infinite;
  box-shadow:
    0 0 80px rgba(176,38,255,.25),
    0 0 160px rgba(255,45,117,.12),
    0 30px 60px rgba(0,0,0,.5);
  transition:all .6s;
}
.player-frame:hover{
  box-shadow:
    0 0 100px rgba(176,38,255,.35),
    0 0 200px rgba(255,45,117,.2),
    0 40px 80px rgba(0,0,0,.6);
}

.player-core{
  position:relative;
  border-radius:30px;
  overflow:hidden;
  background:
    radial-gradient(ellipse 80% 60% at 20% 0%,rgba(176,38,255,.2),transparent 60%),
    radial-gradient(ellipse 70% 60% at 80% 100%,rgba(255,45,117,.15),transparent 60%),
    radial-gradient(ellipse 50% 80% at 50% 50%,rgba(0,229,255,.06),transparent 60%),
    linear-gradient(180deg,rgba(8,4,20,.97),rgba(3,1,8,.98));
  backdrop-filter:blur(40px) saturate(150%);
}

/* ═══════ TOP NAV BAR ═══════ */
.top-bar{
  display:flex;align-items:center;
  padding:14px 24px;
  background:linear-gradient(90deg,
    rgba(176,38,255,.5),rgba(255,45,117,.4),rgba(0,229,255,.3),rgba(176,38,255,.5));
  background-size:300% 100%;
  animation:topBarShift 8s linear infinite;
  position:relative;overflow:hidden;
}
@keyframes topBarShift{0%{background-position:0% 0}100%{background-position:300% 0}}
.top-bar::after{
  content:'';position:absolute;inset:0;
  background:linear-gradient(90deg,transparent,rgba(255,255,255,.15),transparent);
  animation:shineSlide 4s infinite;
}
@keyframes shineSlide{0%{transform:translateX(-100%)}100%{transform:translateX(200%)}}

.brand{
  display:flex;align-items:center;gap:10px;z-index:2;
}
.brand-logo{
  width:36px;height:36px;border-radius:10px;
  background:linear-gradient(135deg,#fff,var(--cy));
  display:flex;align-items:center;justify-content:center;
  font-size:16px;color:var(--bg);
  box-shadow:0 0 20px rgba(0,229,255,.5);
  animation:logoPulse 3s infinite;
}
@keyframes logoPulse{0%,100%{transform:scale(1)}50%{transform:scale(1.08);}}
.brand-name{
  font-family:'Audiowide',sans-serif;font-size:14px;font-weight:400;
  color:#fff;letter-spacing:2px;
  text-shadow:0 0 20px rgba(0,229,255,.6);
}

.live-pill{
  display:flex;align-items:center;gap:6px;
  background:rgba(0,255,135,.12);border:1px solid rgba(0,255,135,.5);
  border-radius:20px;padding:4px 14px;margin-left:12px;
  font-family:'Orbitron',sans-serif;font-size:9px;font-weight:700;
  color:var(--gn);letter-spacing:2px;z-index:2;
}
.live-pulse{
  width:8px;height:8px;border-radius:50%;
  background:var(--gn);
  box-shadow:0 0 10px var(--gn);
  animation:liveDot .8s infinite alternate;
}
@keyframes liveDot{0%{opacity:1;transform:scale(1)}100%{opacity:.3;transform:scale(.5)}}

.top-actions{
  display:flex;align-items:center;gap:6px;margin-left:auto;z-index:2;
}
.top-btn{
  background:rgba(255,255,255,.08);
  border:1px solid rgba(255,255,255,.12);
  border-radius:10px;padding:5px 10px;
  font-family:'Orbitron',sans-serif;font-size:8px;font-weight:700;
  color:rgba(255,255,255,.75);letter-spacing:1px;
  cursor:pointer;transition:all .3s;display:flex;align-items:center;gap:4px;
}
.top-btn:hover{background:rgba(0,229,255,.2);border-color:var(--cy);color:#fff;transform:translateY(-2px);}
.top-btn i{font-size:9px;}
.sleep-on{background:rgba(255,45,117,.2)!important;border-color:var(--pk)!important;color:var(--pk)!important;}

/* ═══════ HERO SECTION ═══════ */
.hero{
  display:grid;
  grid-template-columns:280px 1fr;
  min-height:320px;
  position:relative;
}

/* ─── VISUAL COLUMN ─── */
.visual-col{
  position:relative;
  display:flex;align-items:center;justify-content:center;
  background:
    radial-gradient(circle at 50% 50%,rgba(176,38,255,.25),transparent 70%),
    linear-gradient(180deg,rgba(0,0,0,.3),rgba(0,0,0,.1));
  overflow:hidden;
  padding:30px;
}

/* Hexagonal pattern bg */
.hex-pattern{
  position:absolute;inset:0;opacity:.06;
  background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='28' height='49' viewBox='0 0 28 49'%3E%3Cg fill-rule='evenodd'%3E%3Cg fill='%23ffffff' fill-opacity='1'%3E%3Cpath d='M13.99 9.25l13 7.5v15l-13 7.5L1 31.75v-15l12.99-7.5zM3 17.9v12.7l10.99 6.34 11-6.35V17.9l-11-6.34L3 17.9zM0 15l12.98-7.5V0h-2v6.35L0 12.69v2.3zm0 18.5L12.98 41v8h-2v-6.85L0 35.81v-2.3zM15 0v7.5L27.99 15H28v-2.31h-.01L17 6.35V0h-2zm0 49v-8l12.99-7.5H28v2.31h-.01L17 42.15V49h-2z'/%3E%3C/g%3E%3C/g%3E%3C/svg%3E");
  animation:hexMove 20s linear infinite;
}
@keyframes hexMove{0%{background-position:0 0}100%{background-position:28px 49px}}

/* 3D Disc */
.disc-container{
  position:relative;
  width:200px;height:200px;
  perspective:600px;
}
.disc-3d{
  width:200px;height:200px;
  border-radius:50%;
  position:relative;
  transform-style:preserve-3d;
  animation:discIdle 8s ease-in-out infinite;
}
.disc-3d.spinning{animation:discSpin 4s linear infinite;}
@keyframes discIdle{
  0%,100%{transform:rotateX(12deg) rotateY(0deg);}
  50%{transform:rotateX(12deg) rotateY(15deg);}
}
@keyframes discSpin{
  0%{transform:rotateX(12deg) rotateZ(0deg);}
  100%{transform:rotateX(12deg) rotateZ(360deg);}
}

.disc-vinyl{
  width:100%;height:100%;border-radius:50%;position:absolute;
  background:
    radial-gradient(circle,#111 0%,#111 18%,transparent 18.5%),
    radial-gradient(circle,transparent 18.5%,#0a0a0a 19%,#0a0a0a 22%,transparent 22.5%),
    repeating-radial-gradient(circle,
      rgba(255,255,255,.03) 0px,rgba(255,255,255,.03) 1px,
      transparent 1px,transparent 4px),
    conic-gradient(from 0deg,#0e0e0e,#1a1a1a 5%,#0a0a0a 10%,#181818 15%,
      #0e0e0e 20%,#1a1a1a 25%,#0a0a0a 30%,#181818 35%,
      #0e0e0e 40%,#1a1a1a 45%,#0a0a0a 50%,#181818 55%,
      #0e0e0e 60%,#1a1a1a 65%,#0a0a0a 70%,#181818 75%,
      #0e0e0e 80%,#1a1a1a 85%,#0a0a0a 90%,#181818 95%,#0e0e0e);
  box-shadow:
    0 0 0 3px rgba(255,255,255,.06),
    0 20px 50px rgba(0,0,0,.8),
    inset 0 0 60px rgba(0,0,0,.9);
}
.disc-vinyl::after{
  content:'';position:absolute;inset:0;border-radius:50%;
  background:linear-gradient(135deg,transparent 30%,rgba(255,255,255,.15) 50%,transparent 70%);
}
.disc-vinyl.glow{
  box-shadow:
    0 0 0 3px rgba(255,255,255,.1),
    0 0 40px var(--pk),0 0 80px var(--cy),
    0 20px 50px rgba(0,0,0,.8),
    inset 0 0 60px rgba(0,0,0,.9);
}
.disc-art{
  position:absolute;top:50%;left:50%;width:80px;height:80px;
  transform:translate(-50%,-50%);border-radius:50%;
  object-fit:cover;
  border:3px solid rgba(255,255,255,.15);
  box-shadow:0 0 30px rgba(0,0,0,.9);
  z-index:3;
  transition:all .5s;
}

/* Tonearm */
.tonearm-wrap{
  position:absolute;top:-10px;right:-25px;
  width:70px;height:70px;
  transform-origin:85% 10%;
  transform:rotate(-38deg);
  transition:transform 1.2s cubic-bezier(.4,0,.2,1);
  z-index:10;
}
.tonearm-wrap.on{transform:rotate(-12deg);}

/* Orbit Rings */
.orbit-ring{
  position:absolute;top:50%;left:50%;
  border-radius:50%;border:1px solid;
  transform:translate(-50%,-50%);
  opacity:0;animation:orbitPulse 3s infinite;
  animation-play-state:paused;
}
.orbit-ring.on{animation-play-state:running;}
.orbit-ring:nth-child(1){width:220px;height:220px;border-color:var(--cy);animation-delay:0s;}
.orbit-ring:nth-child(2){width:240px;height:240px;border-color:var(--pk);animation-delay:1s;}
.orbit-ring:nth-child(3){width:260px;height:260px;border-color:var(--pu);animation-delay:2s;}
@keyframes orbitPulse{
  0%{transform:translate(-50%,-50%) scale(.8);opacity:0}
  30%{opacity:.7}
  100%{transform:translate(-50%,-50%) scale(1.2);opacity:0}
}

/* Waveform canvas under disc */
.wave-canvas{
  position:absolute;bottom:0;left:0;right:0;height:50px;z-index:5;
}

/* ─── INFO COLUMN ─── */
.info-col{
  display:flex;flex-direction:column;
  padding:40px 30px 24px 30px;
  position:relative;z-index:5;
  justify-content:center;gap:16px;
}

/* Track Info */
.now-playing-label{
  font-family:'Orbitron',sans-serif;font-size:9px;font-weight:700;
  color:var(--cy);letter-spacing:3px;
  display:flex;align-items:center;gap:8px;
  opacity:.8;
}
.now-playing-label::before{
  content:'';width:20px;height:1px;
  background:linear-gradient(90deg,var(--cy),transparent);
}

.track-title-wrap{
  overflow:hidden;position:relative;max-width:100%;
}
.track-title-wrap::before,.track-title-wrap::after{
  content:'';position:absolute;top:0;bottom:0;width:30px;z-index:3;
}
.track-title-wrap::before{left:0;background:linear-gradient(90deg,rgba(8,4,20,.97),transparent);}
.track-title-wrap::after{right:0;background:linear-gradient(-90deg,rgba(8,4,20,.97),transparent);}

.track-title{
  display:inline-block;white-space:nowrap;
  font-family:'Audiowide',sans-serif;
  font-size:22px;font-weight:400;
  background:linear-gradient(90deg,#fff,var(--cy),var(--pk),var(--gd),#fff);
  background-size:500% 100%;
  -webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;
  animation:titleShimmer 6s linear infinite;
  filter:drop-shadow(0 0 12px rgba(0,229,255,.4));
}
@keyframes titleShimmer{0%{background-position:0%}100%{background-position:500%}}
.track-title.marquee{animation:titleShimmer 6s linear infinite,marqueeScroll var(--mqd,14s) linear infinite;}
@keyframes marqueeScroll{0%,12%{transform:translateX(0)}55%,78%{transform:translateX(var(--mqx,-100px))}100%{transform:translateX(0)}}

/* Meta chips */
.meta-chips{display:flex;flex-wrap:wrap;gap:8px;align-items:center;}
.chip{
  display:inline-flex;align-items:center;gap:5px;
  padding:5px 12px;border-radius:20px;
  font-family:'Orbitron',sans-serif;font-size:9px;font-weight:700;
  letter-spacing:1px;transition:all .3s;
}
.chip-dj{background:rgba(176,38,255,.12);border:1px solid rgba(176,38,255,.35);color:var(--pu);}
.chip-quality{background:rgba(0,229,255,.08);border:1px solid rgba(0,229,255,.3);color:var(--cy);}
.chip-listeners{
  background:rgba(255,190,11,.08);border:1px solid rgba(255,190,11,.3);color:var(--gd);
  animation:chipGlow 3s infinite;
}
@keyframes chipGlow{0%,100%{box-shadow:none}50%{box-shadow:0 0 12px rgba(255,190,11,.2)}}
.chip-timer{background:rgba(0,255,135,.06);border:1px solid rgba(0,255,135,.25);color:var(--gn);}

/* ─── CONTROL BAR ─── */
.ctrl-bar{
  display:flex;align-items:center;gap:16px;
  margin-top:4px;
}

/* Play Button — Morphing */
.play-morph{
  position:relative;width:62px;height:62px;flex-shrink:0;
}
.play-morph::before{
  content:'';position:absolute;inset:-4px;border-radius:50%;
  background:conic-gradient(from var(--border-angle),var(--pk),var(--cy),var(--pu),var(--pk));
  animation:borderSpin 3s linear infinite;
  filter:blur(6px);opacity:.8;
}
.play-morph-btn{
  position:absolute;inset:0;border-radius:50%;
  background:linear-gradient(145deg,rgba(30,10,50,.95),rgba(10,5,25,.98));
  border:none;color:#fff;font-size:22px;cursor:pointer;
  display:flex;align-items:center;justify-content:center;
  transition:all .3s;z-index:1;
  box-shadow:inset 0 2px 0 rgba(255,255,255,.1),0 8px 30px rgba(0,0,0,.5);
}
.play-morph-btn:hover{transform:scale(1.1);background:linear-gradient(145deg,rgba(50,15,80,.95),rgba(20,8,40,.98));}
.play-morph-btn:active{transform:scale(.92);}
.play-morph-btn .fa-pause{font-size:20px;}

/* EQ Visualizer — Circular Style */
.eq-circle-wrap{
  flex:1;height:52px;display:flex;align-items:flex-end;gap:2.5px;
  overflow:hidden;position:relative;
}
.eq-stick{
  flex:1;min-width:3px;max-width:6px;
  border-radius:3px;
  min-height:3px;
  transition:height .1s;
  animation:eqStick var(--sp,.6s) ease-in-out infinite var(--dl,0s);
  animation-play-state:paused;
}
.eq-stick.on{animation-play-state:running;}
@keyframes eqStick{
  0%,100%{height:3px;opacity:.3;}
  50%{height:var(--h,30px);opacity:1;filter:brightness(2);}
}

/* Status indicators */
.status-pills{
  display:flex;gap:6px;flex-shrink:0;
}
.s-pill{
  padding:5px 10px;border-radius:16px;
  font-family:'Orbitron',sans-serif;font-size:8px;font-weight:700;
  letter-spacing:1px;display:flex;align-items:center;gap:4px;
}
.pill-live{background:rgba(0,255,135,.1);border:1px solid rgba(0,255,135,.4);color:var(--gn);}
.pill-live .dot{width:5px;height:5px;border-radius:50%;background:var(--gn);animation:liveDot .8s infinite alternate;}
.pill-hd{background:rgba(0,229,255,.06);border:1px solid rgba(0,229,255,.3);color:var(--cy);}

/* ═══════ ACTION SIDEBAR ═══════ */
.actions-strip{
  display:flex;align-items:center;justify-content:space-between;
  padding:16px 28px;
  border-top:1px solid rgba(255,255,255,.04);
  background:rgba(0,0,0,.2);
  gap:10px;flex-wrap:wrap;
}
.req-mega-btn{
  display:flex;align-items:center;gap:8px;
  padding:12px 28px;border-radius:16px;
  background:linear-gradient(135deg,var(--pu),var(--pk));
  border:none;color:#fff;
  font-family:'Audiowide',sans-serif;font-size:12px;
  cursor:pointer;letter-spacing:1px;
  position:relative;overflow:hidden;
  box-shadow:0 6px 30px rgba(255,45,117,.4);
  transition:all .3s;
}
.req-mega-btn::before{
  content:'';position:absolute;top:-50%;left:-60%;width:50%;height:200%;
  background:linear-gradient(90deg,transparent,rgba(255,255,255,.25),transparent);
  transform:skewX(-20deg);transition:left .5s;
}
.req-mega-btn:hover::before{left:140%;}
.req-mega-btn:hover{transform:translateY(-3px) scale(1.03);box-shadow:0 10px 45px rgba(255,45,117,.55);}
.req-mega-btn i{animation:planeDance 2.5s infinite;}
@keyframes planeDance{
  0%,100%{transform:translate(0,0) rotate(0)}
  25%{transform:translate(3px,-2px) rotate(12deg)}
  75%{transform:translate(-2px,1px) rotate(-8deg)}
}

.action-btns{display:flex;gap:8px;}
.act-btn{
  width:42px;height:42px;border-radius:12px;
  background:rgba(255,255,255,.04);
  border:1px solid rgba(255,255,255,.08);
  color:rgba(255,255,255,.6);font-size:15px;cursor:pointer;
  display:flex;align-items:center;justify-content:center;
  transition:all .3s;position:relative;overflow:hidden;
}
.act-btn::after{
  content:'';position:absolute;inset:0;border-radius:12px;
  background:linear-gradient(135deg,var(--cy),var(--pu));
  opacity:0;transition:opacity .3s;
}
.act-btn:hover{color:#fff;border-color:var(--cy);transform:translateY(-3px);box-shadow:0 8px 24px rgba(0,229,255,.3);}
.act-btn:hover::after{opacity:.2;}
.act-btn i{position:relative;z-index:1;}
.act-btn.liked{border-color:var(--pk);box-shadow:0 0 16px rgba(255,45,117,.3);}
.act-btn.liked i{color:var(--pk);}

/* ─── Volume — Horizontal Neon Bar ─── */
.vol-bar{
  display:flex;align-items:center;gap:10px;
  padding:0 12px;
}
.vol-icon{
  color:rgba(255,255,255,.6);font-size:16px;cursor:pointer;
  transition:all .3s;min-width:20px;text-align:center;
}
.vol-icon:hover{color:var(--cy);transform:scale(1.2);filter:drop-shadow(0 0 8px var(--cy));}
.vol-slider-wrap{
  position:relative;width:120px;height:6px;
  background:rgba(255,255,255,.08);border-radius:6px;
  cursor:pointer;overflow:visible;
}
.vol-slider-fill{
  position:absolute;left:0;top:0;height:100%;
  background:linear-gradient(90deg,var(--cy),var(--pu),var(--pk));
  border-radius:6px;
  box-shadow:0 0 12px var(--cy);
  transition:width .1s;
}
.vol-slider-knob{
  position:absolute;top:50%;transform:translate(-50%,-50%);
  width:18px;height:18px;border-radius:50%;
  background:linear-gradient(135deg,#fff,var(--cy));
  box-shadow:0 0 16px var(--cy),0 2px 8px rgba(0,0,0,.5);
  transition:left .1s;
  pointer-events:none;
}
.vol-slider-input{
  position:absolute;inset:0;width:100%;height:100%;
  opacity:0;cursor:pointer;margin:0;
  -webkit-appearance:none;
}
.vol-pct-label{
  font-family:'Orbitron',sans-serif;font-size:10px;font-weight:700;
  color:var(--cy);text-shadow:0 0 8px var(--cy);min-width:30px;
}

/* ═══════ BOTTOM WIDGET ═══════ */
.bottom-widget{
  margin-top:16px;
  border-radius:24px;padding:2px;
  background:conic-gradient(from var(--border-angle),var(--pu),var(--pk),var(--cy),var(--gd),var(--pu));
  animation:borderSpin 8s linear infinite;
  box-shadow:0 0 60px rgba(176,38,255,.15),0 30px 60px rgba(0,0,0,.4);
}
.bw-inner{
  border-radius:22px;overflow:hidden;
  background:
    radial-gradient(ellipse at 0% 0%,rgba(176,38,255,.15),transparent 50%),
    radial-gradient(ellipse at 100% 100%,rgba(255,45,117,.1),transparent 50%),
    linear-gradient(160deg,rgba(8,4,20,.98),rgba(3,1,8,.99));
}
.bw-header{
  display:flex;align-items:center;gap:12px;
  padding:14px 24px;
  background:linear-gradient(135deg,rgba(176,38,255,.6),rgba(255,45,117,.5),rgba(0,229,255,.35));
  position:relative;overflow:hidden;
}
.bw-header::after{
  content:'';position:absolute;inset:0;
  background:linear-gradient(90deg,transparent,rgba(255,255,255,.18),transparent);
  animation:shineSlide 5s infinite;
}
.bw-header i{font-size:18px;color:#fff;z-index:1;filter:drop-shadow(0 0 10px var(--cy));}
.bw-header-text{
  font-family:'Audiowide',sans-serif;font-size:12px;color:#fff;
  letter-spacing:2px;z-index:1;flex:1;
}
.bw-header-badge{
  background:rgba(0,229,255,.15);border:1px solid rgba(0,229,255,.45);
  border-radius:16px;padding:3px 12px;
  font-family:'Orbitron',sans-serif;font-size:9px;font-weight:700;
  color:var(--cy);letter-spacing:1px;z-index:1;
  animation:badgePop 2.5s infinite;
}
@keyframes badgePop{0%,100%{box-shadow:0 0 0 0 rgba(0,229,255,.4)}50%{box-shadow:0 0 0 6px rgba(0,229,255,0)}}

/* Frequency Visualizer */
.freq-row{
  display:flex;height:48px;
  background:rgba(0,0,0,.4);
  border-bottom:1px solid rgba(255,255,255,.04);
  overflow:hidden;
}
.freq-tag{
  width:80px;display:flex;flex-direction:column;
  align-items:center;justify-content:center;flex-shrink:0;
  background:linear-gradient(135deg,var(--pu),var(--pk));
  font-family:'Orbitron',sans-serif;font-size:9px;font-weight:700;
  color:#fff;letter-spacing:1.5px;
  box-shadow:8px 0 20px rgba(176,38,255,.5);z-index:2;
}
.freq-tag span{font-size:14px;font-weight:900;color:var(--cy);text-shadow:0 0 10px var(--cy);}
.freq-visual{flex:1;display:flex;align-items:center;gap:2px;padding:6px 14px;position:relative;}
.freq-visual::after{
  content:'';position:absolute;inset:0;
  background:linear-gradient(90deg,rgba(0,0,0,.6),transparent 12%,transparent 88%,rgba(0,0,0,.6));
  pointer-events:none;z-index:2;
}
.fbar{
  flex:1;border-radius:3px;min-height:3px;
  animation:fbarAn var(--fs,.5s) ease-in-out infinite var(--fd,0s);
  animation-play-state:paused;
}
.fbar.on{animation-play-state:running;}
@keyframes fbarAn{
  0%,100%{height:3px;opacity:.3;filter:brightness(.6);}
  50%{height:var(--fh,20px);opacity:1;filter:brightness(2.5);}
}
.fbar:nth-child(3n+1){background:linear-gradient(to top,var(--cy),rgba(0,229,255,.2));box-shadow:0 0 6px var(--cy);}
.fbar:nth-child(3n+2){background:linear-gradient(to top,var(--pk),rgba(255,45,117,.2));box-shadow:0 0 6px var(--pk);}
.fbar:nth-child(3n){background:linear-gradient(to top,var(--pu),rgba(176,38,255,.2));box-shadow:0 0 6px var(--pu);}

.msg-ticker-area{
  width:240px;flex-shrink:0;overflow:hidden;
  border-left:1px solid rgba(255,255,255,.06);
  display:flex;align-items:center;position:relative;
}
.msg-ticker-area::before,.msg-ticker-area::after{
  content:'';position:absolute;top:0;bottom:0;width:24px;z-index:3;
}
.msg-ticker-area::before{left:0;background:linear-gradient(90deg,rgba(0,0,0,.5),transparent);}
.msg-ticker-area::after{right:0;background:linear-gradient(-90deg,rgba(0,0,0,.5),transparent);}
.msg-scroll-track{
  display:inline-flex;white-space:nowrap;
  animation:msgDrift 24s linear infinite;
  padding-left:60px;
}
@keyframes msgDrift{0%{transform:translateX(0)}100%{transform:translateX(-50%)}}
.msg-item{
  padding:0 18px;font-size:11px;font-weight:600;
  color:rgba(255,255,255,.7);display:flex;align-items:center;gap:6px;
}
.msg-item i{font-size:9px;color:var(--gd);}

.iframe-slot{width:100%;height:65px;border:none;display:block;background:transparent;}

/* ═══════ FLOATING NOTES ═══════ */
.float-notes{position:absolute;inset:0;pointer-events:none;overflow:hidden;z-index:3;}
.fnote{
  position:absolute;bottom:10%;opacity:0;font-size:14px;
  animation:noteFloat 5.5s infinite ease-out;
  animation-play-state:paused;
  filter:drop-shadow(0 0 8px currentColor);
}
.fnote.on{animation-play-state:running;}
.fnote:nth-child(1){left:8%;color:var(--cy);animation-delay:0s;animation-duration:5s;}
.fnote:nth-child(2){left:22%;color:var(--pk);animation-delay:1.2s;animation-duration:6s;}
.fnote:nth-child(3){left:45%;color:var(--pu);animation-delay:2.4s;animation-duration:4.5s;}
.fnote:nth-child(4){left:65%;color:var(--gd);animation-delay:3.6s;animation-duration:5.8s;}
.fnote:nth-child(5){left:82%;color:var(--gn);animation-delay:4.2s;animation-duration:4.8s;}
@keyframes noteFloat{
  0%{transform:translateY(0) rotate(-15deg) scale(.4);opacity:0}
  12%{opacity:1}
  80%{opacity:.4}
  100%{transform:translateY(-100px) rotate(20deg) scale(1.3);opacity:0}
}

/* Particle layer */
.particles{position:absolute;inset:0;pointer-events:none;overflow:hidden;z-index:2;}
.particle{
  position:absolute;border-radius:50%;opacity:0;
  animation:pRise var(--d,4s) infinite var(--dl,0s);
  animation-play-state:paused;
}
.particle.on{animation-play-state:running;}
@keyframes pRise{
  0%{transform:translateY(200px) translateX(0) scale(0);opacity:0}
  10%{opacity:1}
  90%{opacity:.6}
  100%{transform:translateY(-30px) translateX(var(--tx,0px)) scale(1.5);opacity:0}
}

/* ═══════ MODALS & PANELS ═══════ */
.modal-overlay{
  display:none;position:fixed;inset:0;
  background:rgba(0,0,0,.92);backdrop-filter:blur(30px);
  z-index:99999;justify-content:center;align-items:center;
}
.modal-overlay.open{display:flex;animation:fadeIn .35s;}
@keyframes fadeIn{from{opacity:0}to{opacity:1}}
.modal-box{
  position:relative;width:95%;max-width:820px;height:88vh;
  border-radius:28px;padding:2px;
  background:conic-gradient(from var(--border-angle),var(--pu),var(--pk),var(--cy),var(--pu));
  animation:borderSpin 3s linear infinite,popIn .5s cubic-bezier(.4,0,.2,1);
  box-shadow:0 40px 100px rgba(0,0,0,.9),0 0 150px rgba(255,45,117,.3);
}
@keyframes popIn{from{transform:scale(.75) translateY(60px);opacity:0}to{transform:scale(1) translateY(0);opacity:1}}
.modal-content{
  width:100%;height:100%;border-radius:26px;overflow:hidden;
  background:radial-gradient(ellipse at top left,rgba(176,38,255,.3),transparent 55%),
    radial-gradient(ellipse at bottom right,rgba(255,45,117,.25),transparent 55%),rgba(6,3,14,.98);
  display:flex;flex-direction:column;
}
.modal-top{
  background:linear-gradient(135deg,var(--pu),var(--pk),rgba(0,229,255,.6));
  padding:18px 28px;display:flex;justify-content:space-between;align-items:center;
  position:relative;overflow:hidden;flex-shrink:0;
}
.modal-top::after{content:'';position:absolute;inset:0;background:linear-gradient(90deg,transparent,rgba(255,255,255,.2),transparent);animation:shineSlide 4s infinite;}
.modal-top-title{
  font-family:'Audiowide',sans-serif;font-size:15px;
  color:#fff;display:flex;align-items:center;gap:12px;
  letter-spacing:1.5px;z-index:1;
}
.modal-x{
  width:44px;height:44px;border-radius:12px;
  background:rgba(255,255,255,.1);border:2px solid rgba(255,255,255,.2);
  color:#fff;cursor:pointer;font-size:18px;
  display:flex;align-items:center;justify-content:center;
  transition:.3s;z-index:1;
}
.modal-x:hover{background:rgba(255,45,117,.4);transform:rotate(90deg);box-shadow:0 0 25px rgba(255,45,117,.6);}
.modal-iframe{width:100%;flex:1;border:none;background:#fff;}

/* ═══════ HISTORY PANEL ═══════ */
.hist-panel{
  position:fixed;top:0;right:-400px;width:380px;height:100vh;
  background:linear-gradient(180deg,rgba(8,4,20,.98),rgba(3,1,8,.99));
  border-left:2px solid rgba(176,38,255,.4);
  z-index:99998;transition:right .5s cubic-bezier(.4,0,.2,1);
  display:flex;flex-direction:column;
  box-shadow:-30px 0 80px rgba(0,0,0,.7);
  backdrop-filter:blur(30px);
}
.hist-panel.open{right:0;}
.hist-head{
  padding:24px;display:flex;align-items:center;gap:14px;
  background:linear-gradient(135deg,rgba(176,38,255,.45),rgba(255,45,117,.35));
  flex-shrink:0;
}
.hist-head i{font-size:20px;color:var(--cy);}
.hist-head span{font-family:'Audiowide',sans-serif;font-size:13px;color:#fff;letter-spacing:2px;flex:1;}
.hist-close{
  width:36px;height:36px;border-radius:10px;background:rgba(255,255,255,.1);
  border:1px solid rgba(255,255,255,.2);color:#fff;cursor:pointer;
  display:flex;align-items:center;justify-content:center;font-size:14px;transition:.3s;
}
.hist-close:hover{background:rgba(255,45,117,.4);transform:rotate(90deg);}
.hist-list{flex:1;overflow-y:auto;padding:14px;}
.hist-list::-webkit-scrollbar{width:4px;}
.hist-list::-webkit-scrollbar-thumb{background:var(--pu);border-radius:4px;}
.hist-item{
  display:flex;align-items:center;gap:14px;
  padding:14px;border-radius:14px;margin-bottom:8px;
  background:rgba(255,255,255,.02);border:1px solid rgba(255,255,255,.05);
  transition:all .3s;
}
.hist-item:hover{background:rgba(176,38,255,.12);border-color:rgba(176,38,255,.3);transform:translateX(-4px);}
.hist-num{font-family:'Orbitron',sans-serif;font-size:10px;font-weight:900;color:var(--pu);min-width:24px;text-align:center;}
.hist-info{flex:1;min-width:0;}
.hist-title{font-size:13px;font-weight:700;color:rgba(255,255,255,.9);white-space:nowrap;overflow:hidden;text-overflow:ellipsis;}
.hist-time{font-size:9px;color:rgba(255,255,255,.4);font-family:'Orbitron',sans-serif;margin-top:3px;}
.hist-empty{text-align:center;padding:50px 20px;color:rgba(255,255,255,.25);font-size:13px;}

/* ═══════ SLEEP PANEL ═══════ */
.sleep-fly{
  position:fixed;bottom:80px;right:28px;
  width:290px;padding:2px;border-radius:22px;
  background:conic-gradient(from var(--border-angle),var(--pu),var(--pk),var(--cy),var(--pu));
  animation:borderSpin 4s linear infinite;
  z-index:99997;
  transform:scale(.8) translateY(20px);opacity:0;
  pointer-events:none;transition:all .4s cubic-bezier(.4,0,.2,1);
}
.sleep-fly.open{transform:scale(1) translateY(0);opacity:1;pointer-events:all;}
.sleep-body{
  background:linear-gradient(160deg,rgba(8,4,20,.98),rgba(3,1,8,.99));
  border-radius:20px;padding:22px;
}
.sleep-label{
  font-family:'Audiowide',sans-serif;font-size:11px;
  color:#fff;margin-bottom:14px;display:flex;align-items:center;gap:8px;letter-spacing:1.5px;
}
.sleep-label i{color:var(--cy);}
.sleep-opts{display:flex;flex-wrap:wrap;gap:8px;}
.sleep-opt{
  padding:8px 14px;border-radius:12px;
  background:rgba(255,255,255,.04);border:1px solid rgba(255,255,255,.1);
  color:rgba(255,255,255,.7);font-size:11px;font-weight:700;
  font-family:'Orbitron',sans-serif;cursor:pointer;transition:all .3s;
}
.sleep-opt:hover{background:rgba(176,38,255,.25);border-color:var(--pu);color:#fff;transform:scale(1.05);}
.sleep-opt.picked{background:linear-gradient(135deg,var(--pu),var(--pk));border-color:var(--pk);color:#fff;box-shadow:0 4px 20px rgba(255,45,117,.4);}
.sleep-count{
  margin-top:14px;text-align:center;
  font-family:'Orbitron',sans-serif;font-size:22px;font-weight:900;
  color:var(--cy);text-shadow:0 0 24px var(--cy);
  display:none;
}
.sleep-count.show{display:block;animation:countTick 1s infinite;}
@keyframes countTick{0%,100%{opacity:1}50%{opacity:.5}}
.sleep-stop{
  margin-top:10px;width:100%;padding:9px;border-radius:10px;
  background:rgba(255,45,117,.15);border:1px solid rgba(255,45,117,.4);
  color:var(--pk);font-size:10px;font-weight:700;font-family:'Orbitron',sans-serif;
  cursor:pointer;display:none;transition:.3s;
}
.sleep-stop.show{display:block;}
.sleep-stop:hover{background:rgba(255,45,117,.35);}

/* ═══════ THEME PANEL ═══════ */
.theme-fly{
  position:fixed;bottom:80px;left:28px;
  width:240px;padding:2px;border-radius:22px;
  background:conic-gradient(from var(--border-angle),var(--pu),var(--pk),var(--cy),var(--pu));
  animation:borderSpin 4s linear infinite;
  z-index:99997;
  transform:scale(.8) translateY(20px);opacity:0;
  pointer-events:none;transition:all .4s cubic-bezier(.4,0,.2,1);
}
.theme-fly.open{transform:scale(1) translateY(0);opacity:1;pointer-events:all;}
.theme-body{
  background:linear-gradient(160deg,rgba(8,4,20,.98),rgba(3,1,8,.99));
  border-radius:20px;padding:20px;
}
.theme-heading{
  font-family:'Audiowide',sans-serif;font-size:11px;
  color:#fff;margin-bottom:14px;display:flex;align-items:center;gap:8px;letter-spacing:1.5px;
}
.theme-heading i{color:var(--gd);}
.theme-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;}
.theme-card{
  aspect-ratio:1;border-radius:14px;cursor:pointer;
  border:2px solid rgba(255,255,255,.1);transition:all .3s;
  display:flex;align-items:center;justify-content:center;
  position:relative;overflow:hidden;
}
.theme-card::after{
  content:attr(data-name);font-size:7px;font-family:'Orbitron',sans-serif;
  font-weight:700;color:#fff;text-shadow:0 1px 6px rgba(0,0,0,.9);letter-spacing:.5px;
}
.theme-card:hover{transform:scale(1.1);border-color:#fff;box-shadow:0 0 24px rgba(255,255,255,.25);}
.theme-card.sel{border-color:var(--cy);box-shadow:0 0 24px var(--cy);}
.tc-neon{background:linear-gradient(135deg,#ff2d75,#00e5ff,#b026ff);}
.tc-cyberpunk{background:linear-gradient(135deg,#f7e018,#e92efb,#1b1b2f);}
.tc-aurora{background:linear-gradient(135deg,#43e97b,#38f9d7,#667eea);}
.tc-lava{background:linear-gradient(135deg,#ff0844,#ffb199,#ff3d00);}
.tc-midnight{background:linear-gradient(135deg,#667eea,#764ba2,#f093fb);}
.tc-vapor{background:linear-gradient(135deg,#ff71ce,#01cdfe,#b967ff);}

/* ═══════ EQ PANEL ═══════ */
.eq-fly{
  position:fixed;top:50%;left:50%;transform:translate(-50%,-50%) scale(.8);
  width:360px;padding:2px;border-radius:24px;
  background:conic-gradient(from var(--border-angle),var(--pu),var(--pk),var(--cy),var(--pu));
  animation:borderSpin 4s linear infinite;
  z-index:99998;opacity:0;pointer-events:none;
  transition:all .4s cubic-bezier(.4,0,.2,1);
}
.eq-fly.open{transform:translate(-50%,-50%) scale(1);opacity:1;pointer-events:all;}
.eq-body{
  background:linear-gradient(160deg,rgba(8,4,20,.99),rgba(3,1,8,.99));
  border-radius:22px;padding:26px;
}
.eq-top{display:flex;align-items:center;justify-content:space-between;margin-bottom:20px;}
.eq-top-title{font-family:'Audiowide',sans-serif;font-size:13px;color:#fff;display:flex;align-items:center;gap:10px;letter-spacing:1.5px;}
.eq-top-title i{color:var(--gd);}
.eq-x{
  width:32px;height:32px;border-radius:8px;background:rgba(255,255,255,.08);
  border:1px solid rgba(255,255,255,.15);color:#fff;cursor:pointer;
  display:flex;align-items:center;justify-content:center;font-size:13px;transition:.3s;
}
.eq-x:hover{background:rgba(255,45,117,.4);transform:rotate(90deg);}
.eq-presets-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:8px;margin-bottom:20px;}
.eq-pre{
  padding:10px 6px;border-radius:12px;
  background:rgba(255,255,255,.03);border:1px solid rgba(255,255,255,.08);
  cursor:pointer;transition:all .3s;text-align:center;
}
.eq-pre:hover{background:rgba(176,38,255,.15);border-color:var(--pu);transform:scale(1.04);}
.eq-pre.sel{background:linear-gradient(135deg,rgba(176,38,255,.35),rgba(255,45,117,.25));border-color:var(--pk);box-shadow:0 4px 20px rgba(255,45,117,.25);}
.eq-pre-name{font-family:'Orbitron',sans-serif;font-size:10px;font-weight:700;color:#fff;letter-spacing:.8px;}
.eq-pre-sub{font-size:8px;color:rgba(255,255,255,.45);margin-top:2px;}
.eq-sliders-row{display:flex;gap:12px;justify-content:center;align-items:flex-end;height:110px;}
.eq-band{display:flex;flex-direction:column;align-items:center;gap:6px;}
.eq-band label{font-size:7px;font-family:'Orbitron',sans-serif;font-weight:700;color:rgba(255,255,255,.35);}
.eq-band input[type="range"]{
  writing-mode:vertical-lr;direction:rtl;
  -webkit-appearance:slider-vertical;width:22px;height:75px;
  accent-color:var(--cy);
}
.eq-band .eq-val{font-size:8px;font-family:'Orbitron',sans-serif;color:var(--cy);font-weight:700;}

/* ═══════ SHORTCUTS PANEL ═══════ */
.sc-fly{
  position:fixed;top:50%;left:50%;transform:translate(-50%,-50%) scale(.8);
  width:340px;padding:2px;border-radius:24px;
  background:conic-gradient(from var(--border-angle),var(--pu),var(--pk),var(--cy),var(--pu));
  animation:borderSpin 4s linear infinite;
  z-index:99998;opacity:0;pointer-events:none;
  transition:all .4s cubic-bezier(.4,0,.2,1);
}
.sc-fly.open{transform:translate(-50%,-50%) scale(1);opacity:1;pointer-events:all;}
.sc-body{
  background:linear-gradient(160deg,rgba(8,4,20,.99),rgba(3,1,8,.99));
  border-radius:22px;padding:26px;
}
.sc-top{display:flex;align-items:center;justify-content:space-between;margin-bottom:18px;}
.sc-top-title{font-family:'Audiowide',sans-serif;font-size:13px;color:#fff;display:flex;align-items:center;gap:8px;letter-spacing:1px;}
.sc-top-title i{color:var(--gn);}
.sc-x{
  width:32px;height:32px;border-radius:8px;background:rgba(255,255,255,.08);
  border:1px solid rgba(255,255,255,.15);color:#fff;cursor:pointer;
  display:flex;align-items:center;justify-content:center;font-size:13px;transition:.3s;
}
.sc-x:hover{background:rgba(255,45,117,.4);transform:rotate(90deg);}
.sc-rows{display:flex;flex-direction:column;gap:8px;}
.sc-row{display:flex;align-items:center;gap:14px;}
.sc-key{
  min-width:46px;padding:5px 10px;border-radius:8px;
  background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.18);
  font-family:'Orbitron',sans-serif;font-size:9px;font-weight:700;color:var(--cy);
  text-align:center;
}
.sc-desc{font-size:11px;color:rgba(255,255,255,.65);}

/* ═══════ CONN BAR ═══════ */
.conn-line{
  position:fixed;top:0;left:0;right:0;height:3px;z-index:999999;transition:all .3s;
}
.conn-line.ok{background:linear-gradient(90deg,var(--gn),var(--cy),var(--gn));box-shadow:0 0 10px var(--gn);opacity:.5;}
.conn-line.err{background:linear-gradient(90deg,#f00,#f44,#f00);box-shadow:0 0 10px #f00;opacity:1;animation:connFlash 1s infinite;}
.conn-line.buf{background:linear-gradient(90deg,var(--gd),var(--or),var(--gd));box-shadow:0 0 10px var(--gd);animation:connMove 1s linear infinite;background-size:200%;}
@keyframes connFlash{0%,100%{opacity:1}50%{opacity:.3}}
@keyframes connMove{0%{background-position:0%}100%{background-position:200%}}

/* ═══════ TOAST ═══════ */
.toast-msg{
  position:fixed;bottom:28px;right:28px;
  padding:14px 24px;border-radius:16px;
  background:linear-gradient(135deg,rgba(176,38,255,.92),rgba(255,45,117,.88));
  border:1px solid rgba(255,255,255,.15);color:#fff;font-weight:700;font-size:13px;
  box-shadow:0 14px 50px rgba(0,0,0,.6),0 0 60px rgba(255,45,117,.35);
  z-index:999999;backdrop-filter:blur(20px);
  display:flex;align-items:center;gap:10px;
  transform:translateY(120px) scale(.85);opacity:0;
  transition:all .4s cubic-bezier(.4,0,.2,1);pointer-events:none;
}
.toast-msg.show{transform:translateY(0) scale(1);opacity:1;}
.toast-msg i{font-size:16px;color:var(--cy);}

/* ═══════ MINI PLAYER ═══════ */
.mini-bar{
  position:fixed;bottom:16px;left:50%;transform:translateX(-50%) translateY(120px);
  width:380px;height:64px;
  border-radius:32px;padding:1.5px;
  background:conic-gradient(from var(--border-angle),var(--pu),var(--pk),var(--cy),var(--pu));
  animation:borderSpin 4s linear infinite;
  z-index:99996;opacity:0;pointer-events:none;
  transition:all .5s cubic-bezier(.4,0,.2,1);
}
.mini-bar.show{transform:translateX(-50%) translateY(0);pointer-events:all;opacity:1;}
.mini-body{
  width:100%;height:100%;border-radius:31px;
  background:linear-gradient(160deg,rgba(8,4,20,.97),rgba(3,1,8,.98));
  display:flex;align-items:center;padding:0 10px;gap:10px;
}
.mini-cover{
  width:46px;height:46px;border-radius:50%;object-fit:cover;
  border:2px solid rgba(176,38,255,.5);
  animation:discSpin 7s linear infinite paused;
}
.mini-cover.spin{animation-play-state:running;}
.mini-meta{flex:1;min-width:0;}
.mini-meta-title{font-size:12px;font-weight:700;color:#fff;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;}
.mini-meta-sub{font-size:9px;color:rgba(255,255,255,.4);font-family:'Orbitron',sans-serif;}
.mini-play-btn{
  width:42px;height:42px;border-radius:50%;
  background:linear-gradient(135deg,var(--pu),var(--pk));
  border:none;color:#fff;font-size:15px;cursor:pointer;
  display:flex;align-items:center;justify-content:center;
  transition:.3s;flex-shrink:0;
}
.mini-play-btn:hover{transform:scale(1.12);}
.mini-up{
  width:30px;height:30px;border-radius:50%;
  background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.12);
  color:rgba(255,255,255,.5);font-size:10px;cursor:pointer;
  display:flex;align-items:center;justify-content:center;transition:.3s;flex-shrink:0;
}
.mini-up:hover{background:rgba(255,45,117,.25);color:#fff;}

/* ═══════ RESPONSIVE ═══════ */
@media(max-width:768px){
  .hero{grid-template-columns:1fr;min-height:auto;}
  .visual-col{height:260px;}
  .info-col{padding:20px;}
  .actions-strip{flex-direction:column;gap:12px;}
  .vol-bar{width:100%;justify-content:center;}
  .msg-ticker-area{display:none;}
  .hist-panel{width:100%;}
  .mini-bar{width:320px;}
  .top-actions{gap:4px;}
  .top-btn span{display:none;}
}
@media(max-width:480px){
  .disc-container{width:150px;height:150px;}
  .disc-3d{width:150px;height:150px;}
  .disc-art{width:60px;height:60px;}
  .track-title{font-size:17px;}
  .ctrl-bar{gap:10px;}
  .action-btns{gap:6px;}
  .act-btn{width:38px;height:38px;}
}
</style>
</head>
<body>

<!-- ANIMATED BACKGROUND -->
<div class="bg-scene">
  <div class="bg-orb"></div>
  <div class="bg-orb"></div>
  <div class="bg-orb"></div>
  <div class="bg-orb"></div>
</div>
<div class="bg-grid"></div>
<div class="scanlines"></div>

<!-- CONNECTION BAR -->
<div class="conn-line ok" id="connBar"></div>

<!-- TOAST -->
<div class="toast-msg" id="toast"><i class="fas fa-check-circle"></i><span id="toastTxt"></span></div>

<!-- MODAL -->
<div class="modal-overlay" id="modal">
  <div class="modal-box">
    <div class="modal-content">
      <div class="modal-top">
        <div class="modal-top-title"><i class="fas fa-paper-plane"></i>Şarkı İsteği Gönder</div>
        <button class="modal-x" id="modalClose"><i class="fas fa-times"></i></button>
      </div>
      <iframe src="https://okeysin.com/istekgonder.php" class="modal-iframe" title="İstek"></iframe>
    </div>
  </div>
</div>

<!-- HISTORY PANEL -->
<div class="hist-panel" id="histPanel">
  <div class="hist-head">
    <i class="fas fa-clock-rotate-left"></i>
    <span>ŞARKI GEÇMİŞİ</span>
    <button class="hist-close" id="histClose"><i class="fas fa-times"></i></button>
  </div>
  <div class="hist-list" id="histList">
    <div class="hist-empty"><i class="fas fa-music" style="font-size:28px;margin-bottom:12px;display:block;color:var(--pu);"></i>Henüz şarkı geçmişi yok<br><small style="opacity:.5;">Yayın başladığında burada görünecek</small></div>
  </div>
</div>

<!-- SLEEP PANEL -->
<div class="sleep-fly" id="sleepPanel">
  <div class="sleep-body">
    <div class="sleep-label"><i class="fas fa-moon"></i>UYKU ZAMANLAYICISI</div>
    <div class="sleep-opts" id="sleepOpts">
      <div class="sleep-opt" data-min="5">5 dk</div>
      <div class="sleep-opt" data-min="15">15 dk</div>
      <div class="sleep-opt" data-min="30">30 dk</div>
      <div class="sleep-opt" data-min="45">45 dk</div>
      <div class="sleep-opt" data-min="60">1 saat</div>
      <div class="sleep-opt" data-min="120">2 saat</div>
    </div>
    <div class="sleep-count" id="sleepCount">00:00</div>
    <button class="sleep-stop" id="sleepStop">İPTAL ET</button>
  </div>
</div>

<!-- THEME PANEL -->
<div class="theme-fly" id="themePanel">
  <div class="theme-body">
    <div class="theme-heading"><i class="fas fa-palette"></i>TEMA SEÇ</div>
    <div class="theme-grid">
      <div class="theme-card tc-neon sel" data-theme="neon" data-name="NEON"></div>
      <div class="theme-card tc-cyberpunk" data-theme="cyberpunk" data-name="CYBER"></div>
      <div class="theme-card tc-aurora" data-theme="aurora" data-name="AURORA"></div>
      <div class="theme-card tc-lava" data-theme="lava" data-name="LAVA"></div>
      <div class="theme-card tc-midnight" data-theme="midnight" data-name="NIGHT"></div>
      <div class="theme-card tc-vapor" data-theme="vapor" data-name="VAPOR"></div>
    </div>
  </div>
</div>

<!-- EQ PANEL -->
<div class="eq-fly" id="eqPanel">
  <div class="eq-body">
    <div class="eq-top">
      <div class="eq-top-title"><i class="fas fa-sliders"></i>EQUALIZER</div>
      <button class="eq-x" id="eqClose"><i class="fas fa-times"></i></button>
    </div>
    <div class="eq-presets-grid" id="eqPresets">
      <div class="eq-pre sel" data-preset="flat"><div class="eq-pre-name">FLAT</div><div class="eq-pre-sub">Doğal</div></div>
      <div class="eq-pre" data-preset="bass"><div class="eq-pre-name">BASS</div><div class="eq-pre-sub">Güçlü bas</div></div>
      <div class="eq-pre" data-preset="vocal"><div class="eq-pre-name">VOCAL</div><div class="eq-pre-sub">Vokal</div></div>
      <div class="eq-pre" data-preset="rock"><div class="eq-pre-name">ROCK</div><div class="eq-pre-sub">Enerji</div></div>
      <div class="eq-pre" data-preset="pop"><div class="eq-pre-name">POP</div><div class="eq-pre-sub">Balanced</div></div>
      <div class="eq-pre" data-preset="jazz"><div class="eq-pre-name">JAZZ</div><div class="eq-pre-sub">Sıcak</div></div>
    </div>
    <div class="eq-sliders-row" id="eqSliders">
      <div class="eq-band"><span class="eq-val" id="eqv0">0</span><input type="range" min="-12" max="12" value="0" data-band="0"><label>60</label></div>
      <div class="eq-band"><span class="eq-val" id="eqv1">0</span><input type="range" min="-12" max="12" value="0" data-band="1"><label>250</label></div>
      <div class="eq-band"><span class="eq-val" id="eqv2">0</span><input type="range" min="-12" max="12" value="0" data-band="2"><label>1K</label></div>
      <div class="eq-band"><span class="eq-val" id="eqv3">0</span><input type="range" min="-12" max="12" value="0" data-band="3"><label>4K</label></div>
      <div class="eq-band"><span class="eq-val" id="eqv4">0</span><input type="range" min="-12" max="12" value="0" data-band="4"><label>16K</label></div>
    </div>
  </div>
</div>

<!-- SHORTCUTS PANEL -->
<div class="sc-fly" id="scPanel">
  <div class="sc-body">
    <div class="sc-top">
      <div class="sc-top-title"><i class="fas fa-keyboard"></i>KISAYOLLAR</div>
      <button class="sc-x" id="scClose"><i class="fas fa-times"></i></button>
    </div>
    <div class="sc-rows">
      <div class="sc-row"><span class="sc-key">SPACE</span><span class="sc-desc">Oynat / Duraklat</span></div>
      <div class="sc-row"><span class="sc-key">↑ ↓</span><span class="sc-desc">Ses Aç / Kıs</span></div>
      <div class="sc-row"><span class="sc-key">M</span><span class="sc-desc">Sessiz / Sesli</span></div>
      <div class="sc-row"><span class="sc-key">H</span><span class="sc-desc">Şarkı Geçmişi</span></div>
      <div class="sc-row"><span class="sc-key">T</span><span class="sc-desc">Tema Değiştir</span></div>
      <div class="sc-row"><span class="sc-key">E</span><span class="sc-desc">Equalizer</span></div>
      <div class="sc-row"><span class="sc-key">F</span><span class="sc-desc">Tam Ekran</span></div>
      <div class="sc-row"><span class="sc-key">?</span><span class="sc-desc">Bu Pencere</span></div>
    </div>
  </div>
</div>

<!-- MINI PLAYER -->
<div class="mini-bar" id="miniBar">
  <div class="mini-body">
    <img src="https://images.unsplash.com/photo-1470225620780-dba8ba36b745?w=100" class="mini-cover" id="miniCover" alt="">
    <div class="mini-meta">
      <div class="mini-meta-title" id="miniTitle">okeysin İmaj FM</div>
      <div class="mini-meta-sub">CANLI YAYIN</div>
    </div>
    <button class="mini-play-btn" id="miniPlay"><i class="fas fa-play" id="miniPlayIco"></i></button>
    <button class="mini-up" id="miniUp"><i class="fas fa-arrow-up"></i></button>
  </div>
</div>

<!-- ═══════ MAIN PLAYER ═══════ -->
<div class="main-wrap" id="mainWrap">

  <div class="player-frame" id="playerFrame">
    <div class="player-core">

      <!-- TOP BAR -->
      <div class="top-bar">
        <div class="brand">
          <div class="brand-logo"><i class="fas fa-broadcast-tower"></i></div>
          <div class="brand-name">okeysin İmaj FM</div>
        </div>
        <div class="live-pill"><div class="live-pulse"></div>CANLI YAYIN</div>
        <div class="top-actions">
          <button class="top-btn" id="sleepBtn"><i class="fas fa-moon"></i><span>UYKU</span></button>
          <button class="top-btn" id="themeBtn"><i class="fas fa-palette"></i><span>TEMA</span></button>
          <button class="top-btn" id="eqBtn"><i class="fas fa-sliders"></i><span>EQ</span></button>
          <button class="top-btn" id="kbBtn"><i class="fas fa-keyboard"></i></button>
          <button class="top-btn" id="fsBtn"><i class="fas fa-expand"></i></button>
        </div>
      </div>

      <!-- HERO -->
      <div class="hero">

        <!-- VISUAL -->
        <div class="visual-col">
          <div class="hex-pattern"></div>
          <div class="disc-container">
            <div class="orbit-ring" id="orb1"></div>
            <div class="orbit-ring" id="orb2"></div>
            <div class="orbit-ring" id="orb3"></div>
            <div class="disc-3d" id="disc3d">
              <div class="disc-vinyl" id="discVinyl">
                <img src="https://images.unsplash.com/photo-1470225620780-dba8ba36b745?w=400"
                     id="coverImg" alt="Kapak" class="disc-art">
              </div>
            </div>
            <div class="tonearm-wrap" id="tonearm">
              <svg viewBox="0 0 70 70" fill="none">
                <circle cx="62" cy="8" r="6" fill="#b0b0b0" stroke="rgba(255,255,255,.2)" stroke-width="1.2"/>
                <line x1="62" y1="14" x2="10" y2="64" stroke="#ccc" stroke-width="3" stroke-linecap="round"/>
                <circle cx="10" cy="64" r="5" fill="#0d0d0d" stroke="var(--cy)" stroke-width="1.8"/>
                <circle cx="10" cy="64" r="2.5" fill="var(--cy)" opacity=".9"/>
              </svg>
            </div>
          </div>
          <canvas class="wave-canvas" id="waveCanvas"></canvas>
        </div>

        <!-- INFO -->
        <div class="info-col">
          <div class="float-notes" id="floatNotes">
            <i class="fas fa-music fnote"></i>
            <i class="fas fa-music fnote"></i>
            <i class="fas fa-music fnote"></i>
            <i class="fas fa-music fnote"></i>
            <i class="fas fa-music fnote"></i>
          </div>
          <div class="particles" id="particles"></div>

          <div class="now-playing-label">ŞU AN ÇALIYOR</div>

          <div class="track-title-wrap">
            <span class="track-title" id="trackTitle">okeysin İmaj FM — Bağlanıyor...</span>
          </div>

          <div class="meta-chips">
            <div class="chip chip-dj"><i class="fas fa-microphone-lines"></i><span id="djLabel">Canlı Yayın</span></div>
            <div class="chip chip-quality"><i class="fas fa-signal"></i>320 kbps · HD</div>
            <div class="chip chip-listeners"><i class="fas fa-users"></i><span id="listenerCount">0</span> dinleyici</div>
            <div class="chip chip-timer"><i class="fas fa-stopwatch"></i><span id="listenTime">00:00:00</span></div>
          </div>

          <div class="ctrl-bar">
            <div class="play-morph">
              <button class="play-morph-btn" id="playBtn"><i class="fas fa-play" id="playIco"></i></button>
            </div>

            <div class="eq-circle-wrap" id="eqWrap"></div>

            <div class="status-pills">
              <div class="s-pill pill-live"><div class="dot"></div>CANLI</div>
              <div class="s-pill pill-hd"><i class="fas fa-gem"></i>HD</div>
            </div>
          </div>
        </div>

      </div>

      <!-- ACTIONS STRIP -->
      <div class="actions-strip">
        <button class="req-mega-btn" id="reqBtn"><i class="fas fa-paper-plane"></i><span>İstek Yap</span></button>

        <div class="action-btns">
          <button class="act-btn" id="shareBtn" title="Paylaş"><i class="fas fa-share-nodes"></i></button>
          <button class="act-btn" id="heartBtn" title="Beğen"><i class="far fa-heart"></i></button>
          <button class="act-btn" id="histBtn" title="Geçmiş"><i class="fas fa-clock-rotate-left"></i></button>
          <button class="act-btn" id="infoBtn" title="Bilgi"><i class="fas fa-circle-info"></i></button>
        </div>

        <div class="vol-bar">
          <i class="fas fa-volume-high vol-icon" id="volIco"></i>
          <div class="vol-slider-wrap" id="volWrap">
            <div class="vol-slider-fill" id="volFill" style="width:70%"></div>
            <div class="vol-slider-knob" id="volKnob" style="left:70%"></div>
            <input type="range" class="vol-slider-input" id="volRange" min="0" max="100" value="70">
          </div>
          <span class="vol-pct-label" id="volDisp">70%</span>
        </div>
      </div>

    </div>
  </div>

  <!-- BOTTOM WIDGET -->
  <div class="bottom-widget">
    <div class="bw-inner">
      <div class="bw-header">
        <i class="fas fa-headphones-simple"></i>
        <span class="bw-header-text">Canlı Yayın & Mesajlar</span>
        <div class="bw-header-badge">CANLI</div>
      </div>
      <div class="freq-row">
        <div class="freq-tag"><span>FM</span>YAYINDA</div>
        <div class="freq-visual" id="freqVisual"></div>
        <div class="msg-ticker-area">
          <div class="msg-scroll-track" id="msgScroll"></div>
        </div>
      </div>
      <iframe src="https://okeysin.com/dj_panel/frame.php" class="iframe-slot" scrolling="no" title="Mesajlar"></iframe>
    </div>
  </div>

</div>

<script>
/* ═══════════════════════════════════════════
   CORE
═══════════════════════════════════════════ */
const aud = new Audio('https://radyocast.com/8028/Stream');
aud.volume = 0.7;
aud.crossOrigin = 'anonymous';
let playing = false;

const $ = id => document.getElementById(id);
const playBtn=$('playBtn'),playIco=$('playIco'),disc3d=$('disc3d'),discVinyl=$('discVinyl');
const tonearm=$('tonearm'),eqWrap=$('eqWrap'),trackTitle=$('trackTitle');
const djLabel=$('djLabel'),coverImg=$('coverImg');
const volRange=$('volRange'),volFill=$('volFill'),volKnob=$('volKnob');
const volDisp=$('volDisp'),volIco=$('volIco');
const toast=$('toast'),toastTxt=$('toastTxt');
const modal=$('modal'),connBar=$('connBar');
const orbs=[$('orb1'),$('orb2'),$('orb3')];

/* ═══════════════════════════════════════════
   WEB AUDIO API
═══════════════════════════════════════════ */
let audioCtx,analyser,sourceNode,dataArray;
function initAudio(){
  if(audioCtx) return;
  try{
    audioCtx=new(window.AudioContext||window.webkitAudioContext)();
    analyser=audioCtx.createAnalyser();
    analyser.fftSize=256;
    analyser.smoothingTimeConstant=0.82;
    dataArray=new Uint8Array(analyser.frequencyBinCount);
    sourceNode=audioCtx.createMediaElementSource(aud);
    createEQ();
    sourceNode.connect(eqFilters[0]);
    eqFilters[eqFilters.length-1].connect(analyser);
    analyser.connect(audioCtx.destination);
  }catch(e){console.log('Audio ctx error:',e);}
}

/* ═══════════════════════════════════════════
   EQ
═══════════════════════════════════════════ */
let eqFilters=[];
const eqFreqs=[60,250,1000,4000,16000];
const eqPresetVals={
  flat:[0,0,0,0,0],bass:[10,6,0,-2,-4],vocal:[-2,0,6,4,0],
  rock:[6,2,-2,4,6],pop:[2,4,6,4,2],jazz:[4,2,-2,2,6]
};
function createEQ(){
  if(!audioCtx)return;
  eqFilters=eqFreqs.map((f,i)=>{
    const fl=audioCtx.createBiquadFilter();
    fl.type=i===0?'lowshelf':i===eqFreqs.length-1?'highshelf':'peaking';
    fl.frequency.value=f;fl.gain.value=0;fl.Q.value=1;return fl;
  });
  for(let i=0;i<eqFilters.length-1;i++) eqFilters[i].connect(eqFilters[i+1]);
}
function applyPreset(name){
  const v=eqPresetVals[name]||eqPresetVals.flat;
  eqFilters.forEach((f,i)=>{
    f.gain.value=v[i];
    const sl=document.querySelector(`#eqSliders input[data-band="${i}"]`);
    if(sl) sl.value=v[i];
    const lb=$('eqv'+i);
    if(lb) lb.textContent=v[i]>0?'+'+v[i]:v[i];
  });
}
document.querySelectorAll('.eq-pre').forEach(el=>{
  el.addEventListener('click',()=>{
    document.querySelectorAll('.eq-pre').forEach(e=>e.classList.remove('sel'));
    el.classList.add('sel');
    if(eqFilters.length) applyPreset(el.dataset.preset);
    showToast('🎛️ EQ: '+el.querySelector('.eq-pre-name').textContent,'fa-sliders');
  });
});
document.querySelectorAll('#eqSliders input').forEach(sl=>{
  sl.addEventListener('input',()=>{
    const b=+sl.dataset.band,v=+sl.value;
    if(eqFilters[b]) eqFilters[b].gain.value=v;
    const lb=$('eqv'+b);
    if(lb) lb.textContent=v>0?'+'+v:v;
    document.querySelectorAll('.eq-pre').forEach(e=>e.classList.remove('sel'));
  });
});

/* ═══════════════════════════════════════════
   EQ BARS — Generate
═══════════════════════════════════════════ */
const stickCount=30;
const hues=['#00e5ff','#ff2d75','#b026ff','#ffbe0b','#00ff87','#ff6d00'];
for(let i=0;i<stickCount;i++){
  const s=document.createElement('div');
  s.className='eq-stick';
  const h=Math.floor(Math.random()*42+8);
  const sp=(0.35+Math.random()*0.5).toFixed(2);
  const dl=(Math.random()*0.4).toFixed(2);
  const c=hues[i%hues.length];
  s.style.cssText=`--h:${h}px;--sp:${sp}s;--dl:${dl}s;background:linear-gradient(to top,${c},${c}44);box-shadow:0 0 8px ${c};`;
  eqWrap.appendChild(s);
}

/* ═══════════════════════════════════════════
   PARTICLES
═══════════════════════════════════════════ */
const ptColors=['var(--cy)','var(--pk)','var(--pu)','var(--gd)','var(--or)','var(--gn)'];
const ptLayer=$('particles');
for(let i=0;i<40;i++){
  const p=document.createElement('div');
  p.className='particle';
  const sz=Math.random()*4+2;
  p.style.cssText=`left:${Math.random()*100}%;width:${sz}px;height:${sz}px;background:${ptColors[i%ptColors.length]};box-shadow:0 0 10px ${ptColors[i%ptColors.length]};--tx:${(Math.random()*160-80).toFixed(0)}px;--d:${(3+Math.random()*4).toFixed(2)}s;--dl:${(Math.random()*6).toFixed(2)}s;`;
  ptLayer.appendChild(p);
}

/* ═══════════════════════════════════════════
   FREQ BARS
═══════════════════════════════════════════ */
const freqVis=$('freqVisual');
for(let i=0;i<50;i++){
  const fb=document.createElement('div');
  fb.className='fbar';
  const fh=Math.floor(Math.random()*32+8);
  fb.style.cssText=`--fs:${(0.35+Math.random()*0.5).toFixed(2)}s;--fd:${(Math.random()*0.4).toFixed(2)}s;--fh:${fh}px;`;
  freqVis.appendChild(fb);
}

/* ═══════════════════════════════════════════
   PLAY/PAUSE
═══════════════════════════════════════════ */
function setPlayUI(on){
  const a=on?'add':'remove';
  disc3d.classList[a]('spinning');
  discVinyl.classList[a]('glow');
  tonearm.classList[a]('on');
  eqWrap.querySelectorAll('.eq-stick').forEach(s=>s.classList[a]('on'));
  $('floatNotes').querySelectorAll('.fnote').forEach(n=>n.classList[a]('on'));
  ptLayer.querySelectorAll('.particle').forEach(p=>p.classList[a]('on'));
  orbs.forEach(o=>o.classList[a]('on'));
  freqVis.querySelectorAll('.fbar').forEach(f=>f.classList[a]('on'));
  if(on){
    startWaveCanvas();
    startTimer();
    playIco.className='fas fa-pause';
    $('miniPlayIco').className='fas fa-pause';
    $('miniCover').classList.add('spin');
    updateMedia();
  }else{
    stopWaveCanvas();
    stopTimer();
    playIco.className='fas fa-play';
    $('miniPlayIco').className='fas fa-play';
    $('miniCover').classList.remove('spin');
  }
}

function togglePlay(){
  if(playing){aud.pause();playing=false;setPlayUI(false);}
  else{initAudio();aud.play().catch(()=>{});playing=true;setPlayUI(true);}
}
playBtn.addEventListener('click',togglePlay);
$('miniPlay').addEventListener('click',togglePlay);

/* ═══════════════════════════════════════════
   WAVE CANVAS
═══════════════════════════════════════════ */
const wCanvas=$('waveCanvas');
const wCtx=wCanvas.getContext('2d');
let wRaf=null;
function drawWave(){
  const W=wCanvas.offsetWidth,H=wCanvas.offsetHeight;
  wCanvas.width=W;wCanvas.height=H;
  wCtx.clearRect(0,0,W,H);
  if(analyser&&dataArray&&playing) analyser.getByteFrequencyData(dataArray);
  const n=50,bw=W/n;
  for(let i=0;i<n;i++){
    let h;
    if(analyser&&dataArray&&playing){
      const idx=Math.floor(i*dataArray.length/n);
      h=(dataArray[idx]/255)*(H-4);h=Math.max(2,h);
    }else h=Math.random()*H*.3+2;
    const x=i*bw;
    const grd=wCtx.createLinearGradient(0,H,0,H-h);
    const hue=180+i*3.5;
    grd.addColorStop(0,`hsla(${hue},100%,55%,.9)`);
    grd.addColorStop(1,`hsla(${(hue+60)%360},100%,70%,.4)`);
    wCtx.fillStyle=grd;
    wCtx.shadowColor=`hsl(${hue},100%,60%)`;
    wCtx.shadowBlur=6;
    wCtx.fillRect(x,H-h,bw-.5,h);
  }
  wRaf=requestAnimationFrame(drawWave);
}
function startWaveCanvas(){if(!wRaf) drawWave();}
function stopWaveCanvas(){if(wRaf){cancelAnimationFrame(wRaf);wRaf=null;wCtx.clearRect(0,0,wCanvas.width,wCanvas.height);}}

/* ═══════════════════════════════════════════
   VOLUME
═══════════════════════════════════════════ */
let prevVol=70;
function setVol(v){
  v=Math.max(0,Math.min(100,v));
  aud.volume=v/100;
  volFill.style.width=v+'%';
  volKnob.style.left=v+'%';
  volDisp.textContent=v+'%';
  volRange.value=v;
  volIco.className=v===0?'fas fa-volume-xmark vol-icon':v<40?'fas fa-volume-low vol-icon':'fas fa-volume-high vol-icon';
  localStorage.setItem('imajfm_vol',v);
}
const savedVol=localStorage.getItem('imajfm_vol');
setVol(savedVol!==null?+savedVol:70);
volRange.addEventListener('input',e=>setVol(+e.target.value));
volIco.addEventListener('click',()=>{
  if(aud.volume>0){prevVol=Math.round(aud.volume*100);setVol(0);}
  else setVol(prevVol||70);
});

/* ═══════════════════════════════════════════
   CONNECTION
═══════════════════════════════════════════ */
aud.addEventListener('waiting',()=>{connBar.className='conn-line buf';});
aud.addEventListener('playing',()=>{connBar.className='conn-line ok';});
aud.addEventListener('stalled',()=>{connBar.className='conn-line buf';});
window.addEventListener('online',()=>{showToast('✅ Bağlantı geri geldi','fa-wifi');connBar.className='conn-line ok';if(playing){aud.load();aud.play().catch(()=>{});}});
window.addEventListener('offline',()=>{showToast('❌ Bağlantı kesildi','fa-wifi');connBar.className='conn-line err';});

let reconAttempts=0;
aud.addEventListener('error',()=>{
  connBar.className='conn-line err';
  if(!playing)return;
  reconAttempts++;
  if(reconAttempts<=5){
    showToast(`🔄 Yeniden bağlanılıyor (${reconAttempts}/5)`,'fa-rotate');
    setTimeout(()=>{aud.src='https://radyocast.com/8028/Stream';aud.load();aud.play().then(()=>{reconAttempts=0;connBar.className='conn-line ok';showToast('✅ Bağlandı!','fa-check-circle');}).catch(()=>{});},reconAttempts*3000);
  }else{showToast('❌ Bağlantı kurulamadı','fa-times-circle');playing=false;setPlayUI(false);reconAttempts=0;}
});
aud.addEventListener('playing',()=>{reconAttempts=0;});

/* ═══════════════════════════════════════════
   TOAST
═══════════════════════════════════════════ */
function showToast(msg,ico='fa-check-circle'){
  toastTxt.textContent=msg;
  toast.querySelector('i').className='fas '+ico;
  toast.classList.add('show');
  clearTimeout(toast._t);
  toast._t=setTimeout(()=>toast.classList.remove('show'),3200);
}

/* ═══════════════════════════════════════════
   TIMER
═══════════════════════════════════════════ */
let tSec=0,tInt=null;
function startTimer(){
  if(tInt)return;
  tInt=setInterval(()=>{
    tSec++;
    const h=String(Math.floor(tSec/3600)).padStart(2,'0');
    const m=String(Math.floor((tSec%3600)/60)).padStart(2,'0');
    const s=String(tSec%60).padStart(2,'0');
    $('listenTime').textContent=`${h}:${m}:${s}`;
  },1000);
}
function stopTimer(){if(tInt){clearInterval(tInt);tInt=null;}}

/* ═══════════════════════════════════════════
   HISTORY
═══════════════════════════════════════════ */
let history=JSON.parse(localStorage.getItem('imajfm_history')||'[]');
let lastTrack='';
function addHist(t){
  if(!t||t===lastTrack||t.includes('Bağlanıyor'))return;
  lastTrack=t;
  history.unshift({title:t,time:new Date().toLocaleTimeString('tr-TR')});
  if(history.length>50)history.pop();
  localStorage.setItem('imajfm_history',JSON.stringify(history));
  renderHist();
}
function renderHist(){
  const l=$('histList');
  if(!history.length){l.innerHTML='<div class="hist-empty"><i class="fas fa-music" style="font-size:28px;margin-bottom:12px;display:block;color:var(--pu);"></i>Henüz geçmiş yok</div>';return;}
  l.innerHTML=history.map((h,i)=>`<div class="hist-item"><div class="hist-num">${i+1}</div><div class="hist-info"><div class="hist-title">${h.title}</div><div class="hist-time">${h.time}</div></div></div>`).join('');
}
renderHist();
$('histBtn').addEventListener('click',()=>$('histPanel').classList.toggle('open'));
$('histClose').addEventListener('click',()=>$('histPanel').classList.remove('open'));

/* ═══════════════════════════════════════════
   MODAL
═══════════════════════════════════════════ */
$('reqBtn').addEventListener('click',()=>modal.classList.add('open'));
$('modalClose').addEventListener('click',()=>modal.classList.remove('open'));
modal.addEventListener('click',e=>{if(e.target===modal)modal.classList.remove('open');});

/* ═══════════════════════════════════════════
   SLEEP TIMER
═══════════════════════════════════════════ */
let sleepRem=0,sleepInt=null;
$('sleepBtn').addEventListener('click',e=>{e.stopPropagation();$('sleepPanel').classList.toggle('open');$('themePanel').classList.remove('open');});
document.querySelectorAll('.sleep-opt').forEach(el=>{
  el.addEventListener('click',()=>{
    document.querySelectorAll('.sleep-opt').forEach(e=>e.classList.remove('picked'));
    el.classList.add('picked');
    startSleep(+el.dataset.min);
  });
});
function startSleep(min){
  clearInterval(sleepInt);sleepRem=min*60;
  $('sleepCount').classList.add('show');$('sleepStop').classList.add('show');
  $('sleepBtn').classList.add('sleep-on');
  sleepInt=setInterval(()=>{
    sleepRem--;
    $('sleepCount').textContent=String(Math.floor(sleepRem/60)).padStart(2,'0')+':'+String(sleepRem%60).padStart(2,'0');
    if(sleepRem<=30&&sleepRem>0&&playing) setVol(Math.max(0,Math.round((sleepRem/30)*aud.volume*100)));
    if(sleepRem<=0){clearInterval(sleepInt);if(playing)togglePlay();showToast('😴 İyi geceler!','fa-moon');cancelSleep();}
  },1000);
  showToast(`⏰ ${min} dk sonra kapanacak`,'fa-moon');
}
function cancelSleep(){
  clearInterval(sleepInt);sleepRem=0;
  $('sleepCount').classList.remove('show');$('sleepStop').classList.remove('show');
  $('sleepBtn').classList.remove('sleep-on');
  document.querySelectorAll('.sleep-opt').forEach(e=>e.classList.remove('picked'));
}
$('sleepStop').addEventListener('click',()=>{cancelSleep();showToast('⏰ İptal edildi','fa-times-circle');});

/* ═══════════════════════════════════════════
   THEME
═══════════════════════════════════════════ */
let curTheme=localStorage.getItem('imajfm_theme')||'neon';
document.documentElement.setAttribute('data-theme',curTheme);
document.querySelector(`.theme-card[data-theme="${curTheme}"]`)?.classList.add('sel');

$('themeBtn').addEventListener('click',e=>{e.stopPropagation();$('themePanel').classList.toggle('open');$('sleepPanel').classList.remove('open');});
document.querySelectorAll('.theme-card').forEach(el=>{
  el.addEventListener('click',()=>{
    document.querySelectorAll('.theme-card').forEach(e=>e.classList.remove('sel'));
    el.classList.add('sel');
    curTheme=el.dataset.theme;
    document.documentElement.setAttribute('data-theme',curTheme);
    localStorage.setItem('imajfm_theme',curTheme);
    showToast('🎨 Tema: '+curTheme.toUpperCase(),'fa-palette');
  });
});

/* ═══════════════════════════════════════════
   PANELS OPEN/CLOSE
═══════════════════════════════════════════ */
$('eqBtn').addEventListener('click',()=>$('eqPanel').classList.toggle('open'));
$('eqClose').addEventListener('click',()=>$('eqPanel').classList.remove('open'));
$('kbBtn').addEventListener('click',()=>$('scPanel').classList.toggle('open'));
$('scClose').addEventListener('click',()=>$('scPanel').classList.remove('open'));

function toggleFS(){
  if(!document.fullscreenElement){document.documentElement.requestFullscreen().catch(()=>{});$('fsBtn').querySelector('i').className='fas fa-compress';showToast('🖥️ Tam Ekran','fa-expand');}
  else{document.exitFullscreen();$('fsBtn').querySelector('i').className='fas fa-expand';}
}
$('fsBtn').addEventListener('click',toggleFS);
document.addEventListener('fullscreenchange',()=>{if(!document.fullscreenElement)$('fsBtn').querySelector('i').className='fas fa-expand';});

/* Outside click close */
document.addEventListener('click',e=>{
  if(!$('sleepPanel').contains(e.target)&&!$('sleepBtn').contains(e.target))$('sleepPanel').classList.remove('open');
  if(!$('themePanel').contains(e.target)&&!$('themeBtn').contains(e.target))$('themePanel').classList.remove('open');
  if(!$('eqPanel').contains(e.target)&&!$('eqBtn').contains(e.target))$('eqPanel').classList.remove('open');
  if(!$('scPanel').contains(e.target)&&!$('kbBtn').contains(e.target))$('scPanel').classList.remove('open');
});

/* ═══════════════════════════════════════════
   KEYBOARD SHORTCUTS
═══════════════════════════════════════════ */
const themes=['neon','cyberpunk','aurora','lava','midnight','vapor'];
document.addEventListener('keydown',e=>{
  if(e.key==='Escape'){modal.classList.remove('open');$('histPanel').classList.remove('open');$('sleepPanel').classList.remove('open');$('themePanel').classList.remove('open');$('eqPanel').classList.remove('open');$('scPanel').classList.remove('open');return;}
  if(['INPUT','TEXTAREA','SELECT'].includes(document.activeElement.tagName))return;
  switch(e.key.toLowerCase()){
    case' ':e.preventDefault();togglePlay();break;
    case'arrowup':e.preventDefault();setVol(Math.round(aud.volume*100)+5);break;
    case'arrowdown':e.preventDefault();setVol(Math.round(aud.volume*100)-5);break;
    case'm':if(aud.volume>0){prevVol=Math.round(aud.volume*100);setVol(0);}else setVol(prevVol||70);break;
    case'h':$('histPanel').classList.toggle('open');break;
    case't':
      const ci=themes.indexOf(curTheme),ni=(ci+1)%themes.length;
      document.querySelectorAll('.theme-card').forEach(e=>e.classList.remove('sel'));
      document.querySelector(`.theme-card[data-theme="${themes[ni]}"]`).classList.add('sel');
      curTheme=themes[ni];document.documentElement.setAttribute('data-theme',curTheme);
      localStorage.setItem('imajfm_theme',curTheme);
      showToast('🎨 Tema: '+curTheme.toUpperCase(),'fa-palette');break;
    case'e':$('eqPanel').classList.toggle('open');break;
    case'f':toggleFS();break;
    case'?':$('scPanel').classList.toggle('open');break;
  }
});

/* ═══════════════════════════════════════════
   BUTTONS
═══════════════════════════════════════════ */
$('shareBtn').addEventListener('click',()=>{
  if(navigator.share)navigator.share({title:'okeysin İmaj FM',text:'🎵 '+trackTitle.textContent,url:location.href}).catch(()=>{});
  else navigator.clipboard.writeText(location.href).then(()=>showToast('🔗 Link kopyalandı!','fa-link'));
});
let liked=localStorage.getItem('imajfm_liked')==='true';
const heartBtn=$('heartBtn');
function updHeart(){heartBtn.querySelector('i').className=liked?'fas fa-heart':'far fa-heart';heartBtn.classList.toggle('liked',liked);}
updHeart();
heartBtn.addEventListener('click',()=>{liked=!liked;localStorage.setItem('imajfm_liked',liked);updHeart();if(liked)showToast('❤️ Beğendiniz!','fa-heart');});
$('infoBtn').addEventListener('click',()=>showToast('📡 okeysin İmaj FM — 7/24 Kesintisiz','fa-circle-info'));

trackTitle.addEventListener('click',()=>{
  const t=trackTitle.textContent;
  if(!t||t.includes('Bağlanıyor'))return;
  navigator.clipboard.writeText(t).then(()=>showToast('📋 Şarkı adı kopyalandı!','fa-copy'));
});
trackTitle.style.cursor='pointer';trackTitle.title='Tıklayarak kopyala';

/* ═══════════════════════════════════════════
   MESSAGES
═══════════════════════════════════════════ */
const defMsgs=['🎵 Harika bir yayın!','❤️ Sizi çok seviyoruz','🎤 İstek gönderin','🌟 En iyi müzik','🎧 Sesin adresi','💫 okeysin.com'];
function buildMsgs(arr){
  const all=[...arr,...arr];
  $('msgScroll').innerHTML=all.map(m=>`<span class="msg-item"><i class="fas fa-star"></i>${m}</span>`).join('');
}
buildMsgs(defMsgs);

/* ═══════════════════════════════════════════
   RADIO INFO FETCH
═══════════════════════════════════════════ */
function decHtml(h){const t=document.createElement('textarea');t.innerHTML=h;return t.value;}
async function fetchInfo(){
  try{
    const r=await fetch('https://radyocast.com/cp/get_info.php?p=8028');
    const d=await r.json();
    if(d.title){
      const t=decHtml(d.title);
      trackTitle.textContent=t;$('miniTitle').textContent=t;
      addHist(t);updateMedia();
      requestAnimationFrame(()=>{
        const w=trackTitle.closest('.track-title-wrap');
        if(w&&trackTitle.scrollWidth>w.clientWidth){
          trackTitle.style.setProperty('--mqx',-(trackTitle.scrollWidth-w.clientWidth+30)+'px');
          trackTitle.classList.add('marquee');
        }else trackTitle.classList.remove('marquee');
      });
    }
    if(d.dj)djLabel.textContent=decHtml(d.dj);
    if(d.art){coverImg.src=d.art;$('miniCover').src=d.art;}
    if(d.listeners!==undefined)$('listenerCount').textContent=d.listeners;
    else if(d.uniquelisteners!==undefined)$('listenerCount').textContent=d.uniquelisteners;
  }catch(e){}
}
fetchInfo();setInterval(fetchInfo,12000);

/* ═══════════════════════════════════════════
   MINI PLAYER
═══════════════════════════════════════════ */
let miniMode=false;
const playerFrame=$('playerFrame');
function checkMini(){
  const r=playerFrame.getBoundingClientRect();
  const out=r.bottom<-50;
  if(out&&!miniMode){miniMode=true;$('miniBar').classList.add('show');}
  else if(!out&&miniMode){miniMode=false;$('miniBar').classList.remove('show');}
}
window.addEventListener('scroll',checkMini,{passive:true});
$('miniUp').addEventListener('click',()=>{$('miniBar').classList.remove('show');playerFrame.scrollIntoView({behavior:'smooth',block:'center'});});

/* ═══════════════════════════════════════════
   MEDIA SESSION
═══════════════════════════════════════════ */
function updateMedia(){
  if(!('mediaSession'in navigator))return;
  navigator.mediaSession.metadata=new MediaMetadata({
    title:trackTitle.textContent||'okeysin İmaj FM',
    artist:djLabel.textContent||'Canlı Yayın',
    album:'okeysin İmaj FM',
    artwork:[{src:coverImg.src,sizes:'400x400',type:'image/jpeg'}]
  });
  navigator.mediaSession.setActionHandler('play',()=>{if(!playing)togglePlay();});
  navigator.mediaSession.setActionHandler('pause',()=>{if(playing)togglePlay();});
}

/* ═══════════════════════════════════════════
   WAKE LOCK
═══════════════════════════════════════════ */
let wakeLock=null;
async function reqWake(){if('wakeLock'in navigator&&playing)try{wakeLock=await navigator.wakeLock.request('screen');}catch(e){}}
aud.addEventListener('play',reqWake);
aud.addEventListener('pause',()=>{if(wakeLock){wakeLock.release();wakeLock=null;}});
document.addEventListener('visibilitychange',()=>{if(document.visibilityState==='visible'&&playing)reqWake();});

/* ═══════════════════════════════════════════
   TITLE ROTATION
═══════════════════════════════════════════ */
let titleInt=null,titleIdx=0;
const origTitle=document.title;
aud.addEventListener('play',()=>{
  if(titleInt)return;
  titleInt=setInterval(()=>{
    document.title=titleIdx%2===0?'🎵 '+(trackTitle.textContent||'okeysin İmaj FM'):'▶ okeysin İmaj FM — Canlı';
    titleIdx++;
  },3000);
});
aud.addEventListener('pause',()=>{if(titleInt){clearInterval(titleInt);titleInt=null;}document.title=origTitle;});

/* Volume Wheel */
$('volWrap').addEventListener('wheel',e=>{e.preventDefault();setVol(Math.round(aud.volume*100)+(e.deltaY<0?5:-5));},{passive:false});

/* Double-click fullscreen */
document.querySelector('.player-core').addEventListener('dblclick',e=>{if(e.target.closest('button')||e.target.closest('.act-btn')||e.target.closest('.vol-bar'))return;toggleFS();});

/* Performance — hide animations when tab not visible */
document.addEventListener('visibilitychange',()=>{
  if(document.hidden){if(wRaf){cancelAnimationFrame(wRaf);wRaf=null;}}
  else{if(playing)startWaveCanvas();}
});

/* Welcome */
(function(){
  const lv=localStorage.getItem('imajfm_lastvisit');
  const now=Date.now();localStorage.setItem('imajfm_lastvisit',now);
  if(lv){
    const hrs=Math.floor((now-(+lv))/3600000);
    if(hrs>=1&&hrs<24)setTimeout(()=>showToast(`👋 Tekrar hoş geldiniz! (${hrs} saat önce)`,'fa-hand'),1500);
    else if(hrs>=24)setTimeout(()=>showToast(`👋 ${Math.floor(hrs/24)} gündür görüşmüyorduk!`,'fa-hand'),1500);
  }else setTimeout(()=>showToast('🎉 okeysin İmaj FM\'e hoş geldiniz!','fa-star'),1500);
})();

/* Fade-in */
window.addEventListener('load',()=>{
  document.body.style.opacity='0';document.body.style.transition='opacity .8s ease';
  requestAnimationFrame(()=>{document.body.style.opacity='1';});
});
</script>
</body>
</html>
```

Bu yeni versiyonda şu büyük geliştirmeler var:

**Görsel Yenilikler:**
- Animasyonlu floating orb arka plan (4 renkli küre sürekli hareket ediyor)
- Hex grid pattern overlay ile derinlik hissi
- Scanline efekti (retro CRT tarzı)
- 3D perspektifli dönen plak (CSS 3D transform ile)
- Conic gradient dönen sınır animasyonu
- Glassmorphism efektli panel tasarımı

**Tasarım Değişiklikleri:**
- Yatay hacim kontrolü (modern slider)
- "Audiowide" ve "Rajdhani" font ailesi ile daha modern tipografi
- 6 yeni tema: Neon, Cyberpunk, Aurora, Lava, Midnight, Vaporwave
- 30 adet EQ çubuğu (daha akıcı görselleştirme)
- Daha büyük ve etkileyici play butonu

**Yapısal İyileştirmeler:**
- Grid tabanlı hero layout (plak + bilgi yan yana)
- Daha temiz aksiyon çubuğu
- Tüm mevcut işlevsellik korundu (EQ, Sleep Timer, Geçmiş, Kısayollar vs.)

### Claude Sonnet 4.6 (Thinking)
*2026-03-15 14:43:29 +03*



<think>

The user wants me to create a new, more visually creative and modern radio player based on the existing code. They want it to be more visually impressive, creative with colors, and fully developed. Let me create an enhanced version with:

1. More creative visual effects
2. Better color schemes and gradients
3. More animations
4. Enhanced UI elements
5. Better overall design

Let me design a completely revamped player with:
- A more immersive design
- Glassmorphism effects
- 3D-like elements
- Better particle effects
- More creative EQ visualizer
- Enhanced album art section
- Better typography


- More sophisticated animations and improved layout

I'm going to build this with a cosmic galaxy theme, animated starfield background, vibrant color gradients, a 3D vinyl record effect, holographic visual elements, and an aurora-like animated backdrop. I'll also create a more sophisticated waveform visualization with an enhanced particle system and refined glassmorphism effects throughout.

Building the complete player... Writing the complete HTML structure... Setting up the CSS variables and font imports... Defining more theme color palettes... Writing the aurora background styles... Still writing styles... Still writing styles... Still writing styles... Still writing styles... Still writing styles... Still writing styles... Still writing styles... Writing the halo animations... Still writing vinyl styles... Still writing styles... Still writing styles... Still writing styles... Writing component styles... Still writing styles... Still writing styles... Still writing styles... Still writing the play button styles... Still writing styles... Writing component styles... Still writing button styles... Still writing styles... Still writing styles... Still writing styles... Writing component styles... Still writing styles... Still writing styles... Still writing styles... Still writing styles... Still writing modal styles... Still writing modal styles... Still writing styles... Still writing styles... Still writing styles... Still writing styles... Still writing styles... Still writing styles... Writing theme panel styles... Still writing theme styles... Still writing styles... Still writing styles... Still writing styles... Writing panel styles... Still writing styles... Writing the mini player styles... Still writing styles... Still writing styles... Building the HTML structure... Building the sleep timer interface... Building the theme selector... Building the equalizer presets... Building the equalizer interface... Building the shortcuts menu... Building the mini player and main wrapper... Building the player interface... Writing the vinyl player markup... Adding floating music notes... Building the player interface... Building the action bar... Building the message widget... Writing the star animation...

Now I'm setting up the Web Audio API to analyze the audio from the player, configuring the frequency analyzer and connecting it through an equalizer chain.

Defining the EQ frequency bands and preset configurations... Writing the preset system... Setting up the EQ visualizer with a vibrant color palette for each frequency band... Setting up the equalizer bars... Writing the frequency visualizer... Setting up particle animations...

Now I'm creating a function to toggle the play state, which adds or removes the 'spinning' class on the vinyl disk and 'playing' class on the tonearm, while also updating visual states across the equalizer bars, frequency visualizer bars, vinyl halos, musical notes, and particle elements.

Updating the play/pause icon in both the main player and mini player, then starting or stopping the spectrum canvas and listen timer based on whether audio is playing.

Setting up click listeners on both the main and mini play buttons to handle the toggle functionality.

Now I'm setting up the spectrum canvas visualization that will display frequency data from the audio analyser.

Writing spectrum bars... Writing volume control logic... Adding volume control with scroll wheel support...

Now I'm setting up connection status monitoring—tracking when the audio is buffering, playing, or encounters errors, with automatic reconnection logic that backs off exponentially after failed attempts. Writing connection and toast handlers...

Now I'm setting up a timer to track listening duration, converting elapsed seconds into a formatted hours:minutes:seconds display that updates every second.

Finishing the stop function to clear the interval, then moving on to build a history system that stores station titles with timestamps in localStorage, keeping only the 50 most recent entries and preventing duplicates. Writing the sleep timer functionality... Writing the sleep timer logic...
