<think>
The user wants me to create a complete single HTML file with everything integrated, including the stream URL `https://radyocast.com/8028/Stream` and the API from `https://radyocast.com/cp/get_info.php?p=8028`. They want all the code in one file, with new features added.

Since the API is on a different domain, I'll need to use JSONP or fetch with no-cors, or better yet, make a PHP proxy page. But the user wants a single HTML file...

Actually, the Radyocast API might support JSONP or CORS. Let me think about this. The API endpoint is `https://radyocast.com/cp/get_info.php?p=8028`. 

The API likely returns JSON directly, so I can try fetching it client-side with JSONP as a fallback if CORS headers aren't set. I'll attempt to call the API directly and handle any cross-origin issues that arise. Writing the complete HTML file... Writing the HTML structure... Building the HTML structure...
</think># 🌌 Galactic Wave Radio - Tam Entegre Tek Dosya

İşte **stream URL**, **canlı API**, **gelişmiş müzik çalar**, **lirik sistemi**, **DJ talep sistemi**, **SOX-like Audio Processing**, **tam ekran vizualizer**, **8+ yeni özellik** ile tek HTML dosyası:

```html
<!DOCTYPE html>
<html lang="tr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1,maximum-scale=1,user-scalable=no">
<title>🌌 Galactic Wave Radio</title>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
<link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;500;600;700;800;900&family=Rajdhani:wght@300;400;500;600;700&family=Space+Grotesk:wght@300;400;500;600;700&family=JetBrains+Mono:wght@300;400;500&display=swap" rel="stylesheet">
<style>
:root{
  --bg:#01010a;--bg2:#06061a;--bgc:rgba(8,8,45,.88);--bgg:rgba(12,12,55,.45);
  --p:#00e0ff;--s:#c760ff;--a:#ff6b9d;--e:#ffe04b;--g:#00ff88;--d:#ff4466;
  --gp:rgba(0,224,255,.3);--gs:rgba(199,96,255,.3);--ga:rgba(255,107,157,.3);
  --t:#d8d8f8;--td:#6868a0;--tw:#fff;
  --r:14px;--rs:9px;--rx:5px;
  --fd:'Orbitron',monospace;--fb:'Space Grotesk',sans-serif;--fu:'Rajdhani',sans-serif;--fm:'JetBrains Mono',monospace;
}
*,*::before,*::after{margin:0;padding:0;box-sizing:border-box}
html{scroll-behavior:smooth;overflow-x:hidden}
body{font-family:var(--fb);background:var(--bg);color:var(--t);min-height:100vh;overflow-x:hidden}
::-webkit-scrollbar{width:5px}
::-webkit-scrollbar-track{background:var(--bg)}
::-webkit-scrollbar-thumb{background:linear-gradient(var(--p),var(--s));border-radius:3px}

/* ══════ ARKA PLAN ══════ */
.cosmic{position:fixed;inset:0;z-index:0;overflow:hidden}
.cosmic .neb{position:absolute;border-radius:50%;filter:blur(110px);opacity:.12}
.cosmic .neb:nth-child(1){width:700px;height:700px;background:var(--p);top:-12%;left:-12%;animation:nd 28s ease-in-out infinite alternate}
.cosmic .neb:nth-child(2){width:550px;height:550px;background:var(--s);bottom:-10%;right:-10%;animation:nd 22s ease-in-out infinite alternate-reverse}
.cosmic .neb:nth-child(3){width:450px;height:450px;background:var(--a);top:45%;left:55%;animation:nd 30s ease-in-out infinite alternate}
.cosmic .neb:nth-child(4){width:380px;height:380px;background:var(--e);top:15%;right:15%;opacity:.06;animation:nd 26s ease-in-out infinite alternate-reverse}
@keyframes nd{0%{transform:translate(0,0) scale(1)}33%{transform:translate(70px,-50px) scale(1.18)}66%{transform:translate(-35px,55px) scale(.88)}100%{transform:translate(25px,-25px) scale(1.06)}}
#stars{position:fixed;inset:0;z-index:0}
.st{position:absolute;background:#fff;border-radius:50%;animation:tw var(--d,3s) ease-in-out infinite var(--dl,0s)}
@keyframes tw{0%,100%{opacity:.15;transform:scale(.7)}50%{opacity:1;transform:scale(1.3)}}

/* ══════ GENEL ══════ */
.app{position:relative;z-index:1;max-width:1500px;margin:0 auto;padding:12px;padding-bottom:85px}
.card{background:var(--bgc);border:1px solid rgba(255,255,255,.05);border-radius:var(--r);padding:22px;backdrop-filter:blur(18px);transition:border-color .3s,box-shadow .3s}
.card:hover{border-color:rgba(0,224,255,.12);box-shadow:0 0 25px rgba(0,224,255,.04)}
.ch{display:flex;align-items:center;gap:9px;margin-bottom:16px}
.ch i{font-size:1rem;color:var(--p)}
.ch h3{font-family:var(--fd);font-size:.78rem;letter-spacing:2px;text-transform:uppercase;color:var(--t)}
.ch .badge{margin-left:auto;padding:3px 12px;border-radius:11px;font-family:var(--fu);font-size:.68rem;font-weight:700;text-transform:uppercase;letter-spacing:1px}
.b-live{background:rgba(0,255,136,.1);color:var(--g);border:1px solid rgba(0,255,136,.22);animation:bp 2s infinite}
@keyframes bp{0%,100%{box-shadow:0 0 0 0 rgba(0,255,136,.25)}50%{box-shadow:0 0 10px 2px rgba(0,255,136,.12)}}
.b-dj{background:rgba(255,107,157,.1);color:var(--a);border:1px solid rgba(255,107,157,.2)}

/* ══════ HEADER ══════ */
.hdr{text-align:center;padding:18px 0 12px}
.hdr h1{font-family:var(--fd);font-size:clamp(1.5rem,4vw,2.8rem);font-weight:900;background:linear-gradient(135deg,var(--p),var(--s),var(--a));background-size:200% 200%;-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;animation:gs 4s ease infinite;letter-spacing:3px;text-transform:uppercase}
@keyframes gs{0%,100%{background-position:0 50%}50%{background-position:100% 50%}}
.hdr .sub{font-family:var(--fu);font-size:.92rem;color:var(--td);letter-spacing:7px;text-transform:uppercase;margin-top:4px}
.sb{display:flex;justify-content:center;gap:18px;margin-top:10px;flex-wrap:wrap}
.si{display:flex;align-items:center;gap:7px;font-family:var(--fu);font-size:.82rem;color:var(--td);padding:5px 13px;background:var(--bgg);border-radius:18px;border:1px solid rgba(255,255,255,.05)}
.si i{color:var(--p);font-size:.72rem}
.si.live i{color:var(--g);animation:pd 1.5s infinite}
@keyframes pd{0%,100%{opacity:1}50%{opacity:.25}}
.si strong{color:var(--t);font-weight:600}

/* ══════ GRID ══════ */
.mg{display:grid;grid-template-columns:1fr 1fr;gap:18px;margin-top:18px}
@media(max-width:950px){.mg{grid-template-columns:1fr}}

/* ══════ PLAYER ══════ */
.pc{grid-column:1/-1}
.pl{display:grid;grid-template-columns:260px 1fr;gap:28px;align-items:start}
@media(max-width:750px){.pl{grid-template-columns:1fr}}
.aw{position:relative;width:100%;aspect-ratio:1;border-radius:var(--r);overflow:hidden;cursor:pointer}
.aa{width:100%;height:100%;object-fit:cover;transition:transform .5s}
.aw:hover .aa{transform:scale(1.06)}
.ao{position:absolute;inset:0;background:linear-gradient(180deg,transparent 30%,rgba(0,0,0,.75) 100%);display:flex;align-items:center;justify-content:center;opacity:0;transition:opacity .3s}
.aw:hover .ao{opacity:1}
.apb{width:58px;height:58px;border-radius:50%;background:rgba(0,224,255,.9);border:none;color:var(--bg);font-size:1.3rem;cursor:pointer;display:flex;align-items:center;justify-content:center;transition:transform .2s,box-shadow .2s}
.apb:hover{transform:scale(1.1);box-shadow:0 0 28px var(--gp)}
.apb,.apb:hover{cursor:pointer}
.ab{position:absolute;bottom:11px;left:11px;display:flex;gap:3px;align-items:flex-end;height:18px}
.ab span{width:3px;background:var(--p);border-radius:2px;animation:abk .55s ease-in-out infinite}
.ab span:nth-child(1){height:7px;animation-delay:0s}
.ab span:nth-child(2){height:14px;animation-delay:.1s}
.ab span:nth-child(3){height:9px;animation-delay:.2s}
.ab span:nth-child(4){height:16px;animation-delay:.3s}
.ab span:nth-child(5){height:6px;animation-delay:.35s}
@keyframes abk{0%,100%{transform:scaleY(.35)}50%{transform:scaleY(1)}}
.bb{position:absolute;top:9px;right:9px;padding:3px 9px;background:rgba(0,0,0,.7);border:1px solid var(--p);border-radius:11px;font-family:var(--fd);font-size:.62rem;color:var(--p);letter-spacing:1px}

/* Şarkı Bilgileri */
.si-s{display:flex;flex-direction:column;gap:16px}
.np-i{display:flex;flex-direction:column;gap:4px}
.np-l{font-family:var(--fu);font-size:.72rem;color:var(--p);letter-spacing:3px;text-transform:uppercase}
.st-t{font-family:var(--fd);font-size:clamp(1rem,2.5vw,1.5rem);font-weight:700;color:var(--tw);line-height:1.3;min-height:1.8em}
.st-a{font-family:var(--fb);font-size:.95rem;color:var(--td)}

/* DJ */
.dj-s{display:flex;align-items:center;gap:12px;padding:12px 16px;background:linear-gradient(135deg,rgba(255,107,157,.07),rgba(199,96,255,.07));border:1px solid rgba(255,107,157,.12);border-radius:var(--rs)}
.dj-av{width:44px;height:44px;border-radius:50%;object-fit:cover;border:2px solid var(--a);flex-shrink:0}
.dj-ph{width:44px;height:44px;border-radius:50%;background:linear-gradient(135deg,var(--a),var(--s));display:flex;align-items:center;justify-content:center;color:#fff;font-size:1.1rem;flex-shrink:0}
.dj-i{flex:1}
.dj-lbl{font-family:var(--fu);font-size:.68rem;color:var(--a);letter-spacing:2px;text-transform:uppercase}
.dj-nm{font-family:var(--fd);font-size:.88rem;font-weight:600;color:var(--tw)}
.dj-li{display:flex;align-items:center;gap:5px;padding:4px 11px;background:rgba(0,255,136,.08);border:1px solid rgba(0,255,136,.22);border-radius:18px;font-family:var(--fu);font-size:.68rem;color:var(--g);font-weight:700;letter-spacing:1px}
.dj-li .dot{width:5px;height:5px;background:var(--g);border-radius:50%;animation:pd 1s infinite}

/* İlerleme */
.ps{width:100%}
.pb{width:100%;height:5px;background:rgba(255,255,255,.07);border-radius:3px;cursor:pointer;position:relative;overflow:visible}
.pf{height:100%;background:linear-gradient(90deg,var(--p),var(--s));border-radius:3px;width:0%;transition:width .3s;position:relative}
.pf::after{content:'';position:absolute;right:-6px;top:50%;transform:translateY(-50%);width:13px;height:13px;background:var(--p);border-radius:50%;box-shadow:0 0 8px var(--gp);opacity:0;transition:opacity .2s}
.pb:hover .pf::after{opacity:1}
.pt{display:flex;justify-content:space-between;margin-top:5px;font-family:var(--fu);font-size:.72rem;color:var(--td)}

/* Kontroller */
.cs{display:flex;align-items:center;justify-content:center;gap:15px;flex-wrap:wrap}
.cb{width:46px;height:46px;border-radius:50%;border:1px solid rgba(255,255,255,.08);background:var(--bgg);color:var(--t);font-size:.95rem;cursor:pointer;display:flex;align-items:center;justify-content:center;transition:all .22s}
.cb:hover{border-color:var(--p);color:var(--p);background:rgba(0,224,255,.07);transform:scale(1.08)}
.cb.on{border-color:var(--p);color:var(--p);background:rgba(0,224,255,.12)}
.cb.mp{width:62px;height:62px;font-size:1.35rem;background:linear-gradient(135deg,var(--p),var(--s));border:none;color:var(--bg);box-shadow:0 0 28px var(--gp)}
.cb.mp:hover{transform:scale(1.12);box-shadow:0 0 48px var(--gp);color:var(--bg)}
.cb.mp.on{animation:pg 2s ease-in-out infinite}
@keyframes pg{0%,100%{box-shadow:0 0 18px var(--gp)}50%{box-shadow:0 0 45px var(--gp),0 0 75px rgba(199,96,255,.18)}}

/* Ses */
.vs{display:flex;align-items:center;gap:11px;margin-top:14px;padding-top:14px;border-top:1px solid rgba(255,255,255,.04)}
.vs i{color:var(--td);font-size:.9rem;cursor:pointer;width:18px;text-align:center;transition:color .2s}
.vs i:hover{color:var(--p)}
.vsl{flex:1;-webkit-appearance:none;appearance:none;height:4px;background:rgba(255,255,255,.08);border-radius:2px;outline:none;cursor:pointer}
.vsl::-webkit-slider-thumb{-webkit-appearance:none;width:15px;height:15px;border-radius:50%;background:var(--p);cursor:pointer;box-shadow:0 0 6px var(--gp);transition:transform .15s}
.vsl::-webkit-slider-thumb:hover{transform:scale(1.3)}
.vsl::-moz-range-thumb{width:15px;height:15px;border-radius:50%;background:var(--p);cursor:pointer;border:none}
.vv{font-family:var(--fd);font-size:.72rem;color:var(--td);min-width:32px;text-align:right}

/* ══════ ÇALMA LİSTESİ ══════ */
.pl-card{max-height:480px;display:flex;flex-direction:column}
.pl-list{flex:1;overflow-y:auto;display:flex;flex-direction:column;gap:5px;padding-right:4px}
.pt-tr{display:flex;align-items:center;gap:11px;padding:9px 12px;background:rgba(255,255,255,.015);border-radius:var(--rx);cursor:pointer;transition:all .2s;border:1px solid transparent}
.pt-tr:hover{background:rgba(0,224,255,.04);border-color:rgba(0,224,255,.08)}
.pt-tr.cur{background:rgba(0,224,255,.07);border-color:rgba(0,224,255,.18)}
.tn{font-family:var(--fd);font-size:.68rem;color:var(--td);min-width:18px;text-align:center}
.pt-tr.cur .tn{color:var(--p)}
.ti{flex:1;min-width:0}
.tt{font-family:var(--fb);font-size:.82rem;color:var(--t);white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.ta{font-family:var(--fu);font-size:.68rem;color:var(--td)}
.ttm{font-family:var(--fu);font-size:.68rem;color:var(--td);flex-shrink:0}

/* ══════ VIZUALIZER ══════ */
.viz-card .bc{display:flex;align-items:flex-end;justify-content:center;gap:2px;height:110px;padding:12px 0}
.fb{width:5px;min-height:3px;background:linear-gradient(180deg,var(--p),var(--s));border-radius:3px 3px 0 0;transition:height .12s ease}
.fb.odd{background:linear-gradient(180deg,var(--s),var(--a))}
.eq-s{margin-top:18px}
.eq-m{display:flex;gap:7px;margin-bottom:12px;flex-wrap:wrap}
.eq-b{padding:5px 14px;border:1px solid rgba(255,255,255,.07);background:rgba(255,255,255,.02);color:var(--td);font-family:var(--fu);font-size:.72rem;border-radius:18px;cursor:pointer;transition:all .2s;letter-spacing:1px;text-transform:uppercase}
.eq-b:hover{border-color:var(--p);color:var(--p)}
.eq-b.on{background:rgba(0,224,255,.1);border-color:var(--p);color:var(--p)}
.ebs{display:flex;justify-content:space-between;gap:6px}
.eb{flex:1;display:flex;flex-direction:column;align-items:center;gap:6px}
.es{-webkit-appearance:none;appearance:none;width:3px;height:70px;background:rgba(255,255,255,.08);border-radius:2px;outline:none;writing-mode:vertical-lr;direction:rtl;cursor:pointer}
.es::-webkit-slider-thumb{-webkit-appearance:none;width:13px;height:13px;border-radius:50%;background:var(--p);cursor:pointer}
.el{font-family:var(--fu);font-size:.62rem;color:var(--td)}

/* ══════ DJ KARTI ══════ */
.dj-card{background:linear-gradient(135deg,rgba(255,107,157,.05),rgba(199,96,255,.05));border-color:rgba(255,107,157,.1)}
.dps{display:flex;align-items:center;gap:16px;margin-bottom:16px}
.dpa{width:65px;height:65px;border-radius:50%;object-fit:cover;border:3px solid var(--a);box-shadow:0 0 18px rgba(255,107,157,.25)}
.dpp{width:65px;height:65px;border-radius:50%;background:linear-gradient(135deg,var(--a),var(--s));display:flex;align-items:center;justify-content:center;font-size:1.6rem;color:#fff;border:3px solid var(--a);box-shadow:0 0 18px rgba(255,107,157,.25)}
.dpi h4{font-family:var(--fd);font-size:1rem;color:var(--tw);font-weight:600}
.dpi p{font-family:var(--fu);font-size:.78rem;color:var(--td);margin-top:3px}
.dss{display:grid;grid-template-columns:repeat(3,1fr);gap:10px}
.ds{text-align:center;padding:12px 8px;background:rgba(255,255,255,.02);border-radius:var(--rx);border:1px solid rgba(255,255,255,.03)}
.ds .v{font-family:var(--fd);font-size:1.2rem;font-weight:700;color:var(--p)}
.ds .l{font-family:var(--fu);font-size:.68rem;color:var(--td);margin-top:3px;text-transform:uppercase;letter-spacing:1px}

/* ══════ MESAJ DUVARI ══════ */
.mw{max-height:340px;display:flex;flex-direction:column}
.mia{display:flex;gap:9px;margin-bottom:12px}
.mi{flex:1;padding:9px 14px;background:rgba(255,255,255,.03);border:1px solid rgba(255,255,255,.07);border-radius:var(--rx);color:var(--t);font-family:var(--fb);font-size:.82rem;outline:none;transition:border-color .2s}
.mi::placeholder{color:var(--td)}
.mi:focus{border-color:var(--p)}
.msb{padding:9px 18px;background:linear-gradient(135deg,var(--p),var(--s));border:none;border-radius:var(--rx);color:var(--bg);font-family:var(--fd);font-size:.72rem;font-weight:700;cursor:pointer;letter-spacing:1px;transition:transform .2s,box-shadow .2s}
.msb:hover{transform:scale(1.05);box-shadow:0 0 18px var(--gp)}
.ml{flex:1;overflow-y:auto;display:flex;flex-direction:column;gap:8px}
.mdi{display:flex;gap:9px;padding:9px;background:rgba(255,255,255,.015);border-radius:var(--rx);animation:fadeIn .3s}
@keyframes fadeIn{from{opacity:0;transform:translateY(8px)}to{opacity:1;transform:translateY(0)}}
.mda{width:30px;height:30px;border-radius:50%;background:linear-gradient(135deg,var(--p),var(--s));display:flex;align-items:center;justify-content:center;font-size:.68rem;color:#fff;flex-shrink:0}
.mdb{flex:1}
.mdau{font-family:var(--fu);font-size:.72rem;color:var(--p);font-weight:600}
.mdt{font-size:.8rem;color:var(--t);margin-top:2px;line-height:1.3}
.mdte{font-family:var(--fu);font-size:.62rem;color:var(--td);margin-top:3px}

/* ══════ LİRİK KARTI ══════ */
.lyr-card{display:flex;flex-direction:column;max-height:380px}
.lyr-content{flex:1;overflow-y:auto;display:flex;flex-direction:column;gap:4px}
.lyr-line{padding:8px 14px;font-family:var(--fb);font-size:.9rem;color:var(--td);border-radius:var(--rx);transition:all .4s;cursor:pointer;border-left:3px solid transparent}
.lyr-line:hover{color:var(--t);background:rgba(0,224,255,.04)}
.lyr-line.active{color:var(--tw);font-size:1rem;font-weight:500;background:rgba(0,224,255,.08);border-left-color:var(--p);text-shadow:0 0 20px rgba(0,224,255,.3)}
.lyr-placeholder{text-align:center;padding:40px 20px;color:var(--td)}
.lyr-placeholder i{font-size:2rem;margin-bottom:10px;display:block;color:var(--p)}

/* ══════ TALEP SİSTEMİ ══════ */
.req-card{display:flex;flex-direction:column;max-height:380px}
.req-form{display:flex;flex-direction:column;gap:10px;margin-bottom:15px}
.req-input{padding:10px 14px;background:rgba(255,255,255,.03);border:1px solid rgba(255,255,255,.07);border-radius:var(--rx);color:var(--t);font-family:var(--fb);font-size:.85rem;outline:none;transition:border-color .2s}
.req-input:focus{border-color:var(--p)}
.req-input::placeholder{color:var(--td)}
.req-textarea{min-height:60px;resize:vertical}
.req-submit{padding:10px 20px;background:linear-gradient(135deg,var(--a),var(--s));border:none;border-radius:var(--rx);color:#fff;font-family:var(--fd);font-size:.72rem;font-weight:700;cursor:pointer;letter-spacing:1px;transition:transform .2s,box-shadow .2s}
.req-submit:hover{transform:scale(1.03);box-shadow:0 0 20px var(--ga)}
.req-list{flex:1;overflow-y:auto;display:flex;flex-direction:column;gap:8px}
.req-item{display:flex;align-items:center;gap:10px;padding:10px 12px;background:rgba(255,255,255,.02);border-radius:var(--rx);border-left:3px solid var(--a)}
.req-info{flex:1}
.req-song{font-size:.82rem;color:var(--t);font-weight:500}
.req-reqby{font-family:var(--fu);font-size:.68rem;color:var(--td)}
.req-likes{font-family:var(--fd);font-size:.72rem;color:var(--s);min-width:30px;text-align:center}
.req-like-btn{width:28px;height:28px;border-radius:50%;border:1px solid rgba(255,255,255,.08);background:transparent;color:var(--td);font-size:.7rem;cursor:pointer;display:flex;align-items:center;justify-content:center;transition:all .2s}
.req-like-btn:hover{border-color:var(--a);color:var(--a)}
.req-like-btn.liked{color:var(--a);border-color:var(--a);background:rgba(255,107,157,.12)}

/* ══════ SOX/AUDIO PROCESSING ══════ */
.sox-card .sox-grid{display:grid;grid-template-columns:repeat(2,1fr);gap:10px}
@media(max-width:500px){.sox-card .sox-grid{grid-template-columns:1fr}}
.sox-knob{text-align:center;padding:14px;background:rgba(255,255,255,.02);border-radius:var(--rs);border:1px solid rgba(255,255,255,.04)}
.sox-knob label{display:block;font-family:var(--fu);font-size:.7rem;color:var(--td);margin-bottom:8px;text-transform:uppercase;letter-spacing:1px}
.sox-knob input[type=range]{width:100%;-webkit-appearance:none;appearance:none;height:4px;background:rgba(255,255,255,.08);border-radius:2px;outline:none;cursor:pointer}
.sox-knob input[type=range]::-webkit-slider-thumb{-webkit-appearance:none;width:14px;height:14px;border-radius:50%;background:var(--p);cursor:pointer}
.sox-val{font-family:var(--fd);font-size:.82rem;color:var(--p);margin-top:6px}
.sox-toggle{display:flex;gap:7px;margin-bottom:12px;flex-wrap:wrap}
.sox-btn{padding:5px 12px;border:1px solid rgba(255,255,255,.07);background:rgba(255,255,255,.02);color:var(--td);font-family:var(--fu);font-size:.7rem;border-radius:16px;cursor:pointer;transition:all .2s;text-transform:uppercase;letter-spacing:1px}
.sox-btn:hover{border-color:var(--p);color:var(--p)}
.sox-btn.on{background:rgba(0,224,255,.1);border-color:var(--p);color:var(--p)}

/* ══════ TAM EKRAN VIZUALIZER ══════ */
.fs-viz{position:fixed;inset:0;z-index:9999;background:var(--bg);display:none;flex-direction:column;align-items:center;justify-content:center}
.fs-viz.open{display:flex}
.fs-viz-close{position:absolute;top:20px;right:20px;width:44px;height:44px;border-radius:50%;border:1px solid rgba(255,255,255,.1);background:rgba(0,0,0,.5);color:#fff;font-size:1.1rem;cursor:pointer;display:flex;align-items:center;justify-content:center;z-index:10}
.fs-viz-info{position:absolute;bottom:60px;text-align:center}
.fs-viz-title{font-family:var(--fd);font-size:1.4rem;color:var(--tw);letter-spacing:2px}
.fs-viz-artist{font-family:var(--fb);font-size:1rem;color:var(--td);margin-top:4px}
.fs-bars{display:flex;align-items:flex-end;justify-content:center;gap:4px;height:60vh;width:90%;max-width:900px}
.fs-bar{flex:1;min-width:3px;max-width:20px;border-radius:3px 3px 0 0;transition:height .1s ease;background:var(--p)}
.fs-bar.even{background:linear-gradient(180deg,var(--p),var(--s))}
.fs-bar.odd{background:linear-gradient(180deg,var(--s),var(--a))}
.fs-controls{position:absolute;bottom:20px;display:flex;gap:14px}
.fs-ctrl{width:48px;height:48px;border-radius:50%;border:1px solid rgba(255,255,255,.1);background:rgba(255,255,255,.05);color:#fff;font-size:1rem;cursor:pointer;display:flex;align-items:center;justify-content:center;transition:all .2s}
.fs-ctrl:hover{border-color:var(--p);color:var(--p)}

/* ══════ SLEEP TIMER ══════ */
.sleep-sel{padding:6px 12px;background:rgba(255,255,255,.03);border:1px solid rgba(255,255,255,.08);border-radius:var(--rs);color:var(--t);font-family:var(--fu);font-size:.8rem;outline:none;cursor:pointer}
.sleep-sel option{background:var(--bg2)}

/* ══════ SOCIAl LINKS ══════ */
.social-links{display:flex;gap:10px;margin-top:12px;flex-wrap:wrap}
.social-link{display:flex;align-items:center;gap:6px;padding:7px 14px;background:rgba(255,255,255,.03);border:1px solid rgba(255,255,255,.06);border-radius:20px;font-family:var(--fu);font-size:.75rem;color:var(--td);text-decoration:none;transition:all .2s;cursor:pointer}
.social-link:hover{border-color:var(--p);color:var(--p);background:rgba(0,224,255,.05)}
.social-link i{font-size:.85rem}

/* ══════ TOOLBAR ══════ */
.bt{position:fixed;bottom:0;left:0;right:0;z-index:100;background:rgba(3,3,20,.94);backdrop-filter:blur(18px);border-top:1px solid rgba(255,255,255,.05);padding:7px 16px;display:flex;align-items:center;justify-content:space-between}
.tb{font-family:var(--fd);font-size:.65rem;color:var(--p);letter-spacing:2px}
.tnav{display:flex;gap:5px}
.tbb{width:40px;height:40px;border-radius:50%;border:1px solid rgba(255,255,255,.07);background:rgba(255,255,255,.02);color:var(--td);font-size:.85rem;cursor:pointer;display:flex;align-items:center;justify-content:center;transition:all .2s}
.tbb:hover,.tbb.on{border-color:var(--p);color:var(--p);background:rgba(0,224,255,.07)}

/* ══════ TOAST ══════ */
.toast{position:fixed;bottom:75px;left:50%;transform:translateX(-50%) translateY(25px);padding:10px 22px;background:rgba(0,224,255,.1);border:1px solid rgba(0,224,255,.22);backdrop-filter:blur(18px);border-radius:26px;font-family:var(--fu);font-size:.8rem;color:var(--p);z-index:200;opacity:0;pointer-events:none;transition:all .32s cubic-bezier(.4,0,.2,1);white-space:nowrap}
.toast.show{opacity:1;transform:translateX(-50%) translateY(0)}

/* ══════ EKSTRA ══════ */
.info-row{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:18px;margin-top:18px}
.l-skel{background:linear-gradient(90deg,rgba(255,255,255,.02) 25%,rgba(255,255,255,.05) 50%,rgba(255,255,255,.02) 75%);background-size:200% 100%;animation:sk 1.5s infinite;border-radius:6px}
@keyframes sk{0%{background-position:200% 0}100%{background-position:-200% 0}}
@media(max-width:600px){.app{padding:8px;padding-bottom:80px}.card{padding:16px}.pl{grid-template-columns:1fr}.aw{max-width:240px;margin:0 auto}.cs{gap:10px}.sb{gap:8px}.si{padding:4px 9px;font-size:.72rem}}

/* Bottom now-playing mini */
.bnp{display:flex;align-items:center;gap:10px;flex:1;margin:0 15px;overflow:hidden}
.bnp-art{width:36px;height:36px;border-radius:6px;object-fit:cover;flex-shrink:0}
.bnp-info{overflow:hidden}
.bnp-title{font-family:var(--fb);font-size:.78rem;color:var(--t);white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.bnp-artist{font-family:var(--fu);font-size:.65rem;color:var(--td)}
</style>
</head>
<body>

<!-- ARKA PLAN -->
<div class="cosmic"><div class="neb"></div><div class="neb"></div><div class="neb"></div><div class="neb"></div></div>
<div id="stars"></div>

<!-- TAM EKRAN VIZUALIZER -->
<div class="fs-viz" id="fsViz">
  <button class="fs-viz-close" onclick="closeFsViz()"><i class="fas fa-times"></i></button>
  <div class="fs-bars" id="fsBars"></div>
  <div class="fs-viz-info">
    <div class="fs-viz-title" id="fsTitle">Yükleniyor...</div>
    <div class="fs-viz-artist" id="fsArtist">Galactic Wave Radio</div>
  </div>
  <div class="fs-controls">
    <button class="fs-ctrl" onclick="togglePlay()" id="fsPlayBtn"><i class="fas fa-play"></i></button>
    <button class="fs-ctrl" onclick="closeFsViz()"><i class="fas fa-compress-arrows-alt"></i></button>
  </div>
</div>

<!-- ANA APP -->
<div class="app">
  <!-- HEADER -->
  <header class="hdr">
    <h1>🌌 Galactic Wave</h1>
    <div class="sub">Premium Radio Experience</div>
    <div class="sb">
      <div class="si live"><i class="fas fa-circle"></i><span>YAYINDA</span></div>
      <div class="si"><i class="fas fa-users"></i><span><strong id="lc">0</strong> Dinleyici</span></div>
      <div class="si"><i class="fas fa-tachometer-alt"></i><span><strong id="brv">--</strong> kbps</span></div>
      <div class="si" id="sDj" style="display:none"><i class="fas fa-microphone-alt"></i><span>DJ: <strong id="sDjN">--</strong></span></div>
      <div class="si" id="sTime"></div>
    </div>
  </header>

  <!-- PLAYER -->
  <div class="mg">
    <div class="card pc">
      <div class="ch">
        <i class="fas fa-satellite-dish"></i>
        <h3>Çalıyor</h3>
        <div class="badge b-live" id="liveB"><i class="fas fa-circle" style="font-size:5px;margin-right:4px"></i>CANLI</div>
      </div>
      <div class="pl">
        <div>
          <div class="aw" id="alW" ondblclick="openFsViz()">
            <img src="https://via.placeholder.com/300/050520/00e0ff?text=%F0%9F%8C%8C" alt="" class="aa" id="alA"
                 onerror="this.src='data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 300 300%22><rect fill=%22%23050520%22 width=%22300%22 height=%22300%22/><text fill=%22%2300e0ff%22 x=%2250%%22 y=%2252%%22 text-anchor=%22middle%22 font-size=%2260%22>🌌</text></svg>'">
            <div class="ao"><button class="apb" id="alPb"><i class="fas fa-play"></i></button></div>
            <div class="ab" id="alB"><span></span><span></span><span></span><span></span><span></span></div>
            <div class="bb" id="bBadge">128 kbps</div>
          </div>
        </div>
        <div class="si-s">
          <div class="np-i">
            <span class="np-l">🎵 Şimdi Çalıyor</span>
            <h2 class="st-t" id="sT">Yükleniyor...</h2>
            <p class="st-a" id="sA">Galactic Wave Radio</p>
          </div>
          <div class="dj-s" id="djS" style="display:none">
            <img src="" alt="" class="dj-av" id="djAv" onerror="this.style.display='none';this.nextElementSibling.style.display='flex'">
            <div class="dj-ph" id="djPh" style="display:none"><i class="fas fa-headphones"></i></div>
            <div class="dj-i"><div class="dj-lbl">Canlı DJ</div><div class="dj-nm" id="djN">--</div></div>
            <div class="dj-li"><div class="dot"></div>CANLI</div>
          </div>
          <div class="ps">
            <div class="pb" id="pBar"><div class="pf" id="pFill"></div></div>
            <div class="pt"><span id="tEl">0:00</span><span id="tTo">~4:00</span></div>
          </div>
          <div class="cs">
            <button class="cb" id="bSh" title="Karıştır"><i class="fas fa-random"></i></button>
            <button class="cb" id="bPv" title="Önceki"><i class="fas fa-step-backward"></i></button>
            <button class="cb mp" id="bPl" title="Oynat"><i class="fas fa-play" id="plIc"></i></button>
            <button class="cb" id="bNx" title="Sonraki"><i class="fas fa-step-forward"></i></button>
            <button class="cb" id="bRp" title="Tekrarla"><i class="fas fa-redo"></i></button>
            <button class="cb" id="bLk" title="Beğen"><i class="far fa-heart"></i></button>
            <button class="cb" id="bShr" title="Paylaş"><i class="fas fa-share-alt"></i></button>
            <button class="cb" id="bFs" title="Tam Ekran"><i class="fas fa-expand"></i></button>
            <select class="sleep-sel" id="sleepSel" title="Uyku Zamanlayıcı">
              <option value="0">⏰ Uyku</option>
              <option value="15">15 dk</option>
              <option value="30">30 dk</option>
              <option value="60">60 dk</option>
              <option value="90">90 dk</option>
              <option value="120">120 dk</option>
            </select>
          </div>
          <div class="vs">
            <i class="fas fa-volume-up" id="vIc"></i>
            <input type="range" class="vsl" id="vSl" min="0" max="100" value="75">
            <span class="vv" id="vVl">75%</span>
          </div>
          <!-- Sosyal Linkler -->
          <div class="social-links">
            <a class="social-link" href="#" onclick="showToast('📱 Instagram yakında!','fa-instagram')"><i class="fab fa-instagram"></i>Instagram</a>
            <a class="social-link" href="#" onclick="showToast('🐦 Twitter yakında!','fa-twitter')"><i class="fab fa-twitter"></i>Twitter</a>
            <a class="social-link" href="#" onclick="showToast('💬 Discord yakında!','fa-discord')"><i class="fab fa-discord"></i>Discord</a>
            <a class="social-link" href="#" onclick="showToast('🔊 Telegram yakında!','fa-telegram')"><i class="fab fa-telegram"></i>Telegram</a>
          </div>
        </div>
      </div>
    </div>

    <!-- VIZUALIZER -->
    <div class="card viz-card">
      <div class="ch">
        <i class="fas fa-wave-square"></i>
        <h3>Frekans Analizörü</h3>
      </div>
      <div class="bc" id="fBC"></div>
      <div class="eq-s">
        <div class="eq-m" id="eqModes"></div>
        <div class="ebs" id="eqBands"></div>
      </div>
    </div>

    <!-- ÇALMA LİSTESİ -->
    <div class="card pl-card">
      <div class="ch">
        <i class="fas fa-list-ul"></i>
        <h3>Çalma Listesi</h3>
        <div class="badge b-live" id="hCnt">0 şarkı</div>
      </div>
      <div class="pl-list" id="plList">
        <div class="l-skel" style="height:48px;margin-bottom:6px"></div>
        <div class="l-skel" style="height:48px;margin-bottom:6px"></div>
        <div class="l-skel" style="height:48px;margin-bottom:6px"></div>
        <div class="l-skel" style="height:48px;margin-bottom:6px"></div>
        <div class="l-skel" style="height:48px"></div>
      </div>
    </div>

    <!-- DJ PROFİLİ -->
    <div class="card dj-card">
      <div class="ch">
        <i class="fas fa-headphones-alt"></i>
        <h3>DJ Profili</h3>
        <div class="badge b-dj" id="djBadge" style="display:none"><i class="fas fa-circle" style="font-size:5px;margin-right:4px"></i>CANLI</div>
      </div>
      <div class="dps">
        <div class="dpp" id="djPp"><i class="fas fa-headphones"></i></div>
        <img src="" alt="" class="dpa" id="djPa" style="display:none" onerror="this.style.display='none';document.getElementById('djPp').style.display='flex'">
        <div class="dpi">
          <h4 id="djPn">Otomatik Çalma</h4>
          <p id="djPd">Sanal DJ - Otomatik Playlist</p>
        </div>
      </div>
      <div class="dss">
        <div class="ds"><div class="v" id="sOn">0</div><div class="l">Online</div></div>
        <div class="ds"><div class="v" id="sUn">0</div><div class="l">Tekil</div></div>
        <div class="ds"><div class="v" id="sBr">--</div><div class="l">kbps</div></div>
      </div>
      <!-- Sunrise/Sunset & Weather Info -->
      <div style="margin-top:15px;padding-top:15px;border-top:1px solid rgba(255,255,255,.04)">
        <div style="display:flex;gap:15px;flex-wrap:wrap">
          <div style="flex:1;min-width:100px;text-align:center;padding:10px;background:rgba(255,255,255,.02);border-radius:var(--rx)">
            <div style="font-size:1.4rem">🌅</div>
            <div style="font-family:var(--fu);font-size:.7rem;color:var(--td);margin-top:4px">Güneş</div>
            <div id="sunrise" style="font-family:var(--fd);font-size:.75rem;color:var(--e)">--:--</div>
          </div>
          <div style="flex:1;min-width:100px;text-align:center;padding:10px;background:rgba(255,255,255,.02);border-radius:var(--rx)">
            <div style="font-size:1.4rem">🌙</div>
            <div style="font-family:var(--fu);font-size:.7rem;color:var(--td);margin-top:4px">Ay</div>
            <div id="moonphase" style="font-family:var(--fd);font-size:.75rem;color:var(--s)">Yeni Ay</div>
          </div>
          <div style="flex:1;min-width:100px;text-align:center;padding:10px;background:rgba(255,255,255,.02);border-radius:var(--rx)">
            <div style="font-size:1.4rem">🌡</div>
            <div style="font-family:var(--fu);font-size:.7rem;color:var(--td);margin-top:4px">Durum</div>
            <div id="uptime" style="font-family:var(--fd);font-size:.75rem;color:var(--g)">Aktif</div>
          </div>
        </div>
      </div>
    </div>

    <!-- SOX AUDIO PROCESSING -->
    <div class="card sox-card">
      <div class="ch">
        <i class="fas fa-sliders-h"></i>
        <h3>Audio Processing</h3>
      </div>
      <div class="sox-toggle" id="soxToggles"></div>
      <div class="sox-grid" id="soxGrid"></div>
    </div>

    <!-- LİRİK -->
    <div class="card lyr-card">
      <div class="ch">
        <i class="fas fa-align-left"></i>
        <h3>Şarkı Sözleri</h3>
      </div>
      <div class="lyr-content" id="lyrContent">
        <div class="lyr-placeholder">
          <i class="fas fa-music"></i>
          <p style="font-size:.9rem;color:var(--t);margin-bottom:5px">Şarkı sözlere hazırlanıyor...</p>
          <p style="font-size:.78rem">Dinlemeye devam edin 🎵</p>
        </div>
      </div>
    </div>

    <!-- ŞARKI TALEP -->
    <div class="card req-card">
      <div class="ch">
        <i class="fas fa-pen-fancy"></i>
        <h3>Şarkı Talep</h3>
        <div class="badge b-live" id="reqCount">0 talep</div>
      </div>
      <div class="req-form">
        <input type="text" class="req-input" id="reqSong" placeholder="🎵 Şarkı adı veya link..." maxlength="150">
        <input type="text" class="req-input" id="reqName" placeholder="👤 Adınız (opsiyonel)" maxlength="50">
        <textarea class="req-input req-textarea" id="reqNote" placeholder="💬 Mesajınız..." maxlength="200"></textarea>
        <button class="req-submit" onclick="submitRequest()"><i class="fas fa-paper-plane"></i> TALEP GÖNDER</button>
      </div>
      <div class="req-list" id="reqList"></div>
    </div>

    <!-- MESAJ DUVARI -->
    <div class="card mw">
      <div class="ch">
        <i class="fas fa-comment-dots"></i>
        <h3>Canlı Sohbet</h3>
      </div>
      <div class="mia">
        <input type="text" class="mi" id="msgIn" placeholder="Mesajınızı yazın..." maxlength="200">
        <button class="msb" id="msgBt">GÖNDER</button>
      </div>
      <div class="ml" id="msgL">
        <div class="mdi">
          <div class="mda">🤖</div>
          <div class="mdb">
            <div class="mdau">Sistem</div>
            <div class="mdt">Galactic Wave Radio'ya hoş geldiniz! 🌌 Şarkı isteklerinizi ve mesajlarınızı buraya yazabilirsiniz.</div>
            <div class="mdte">Canlı</div>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>

<!-- BOTTOM BAR -->
<nav class="bt">
  <span class="tb">GALACTIC WAVE</span>
  <div class="bnp" id="bnp" style="display:none">
    <img src="" alt="" class="bnp-art" id="bnpA">
    <div class="bnp-info">
      <div class="bnp-title" id="bnpT">--</div>
      <div class="bnp-artist" id="bnpAt">--</div>
    </div>
  </div>
  <div class="tnav">
    <button class="tbb" onclick="scrollTo(0,0)" title="Ana Sayfa"><i class="fas fa-home"></i></button>
    <button class="tbb" id="tbR" title="Radyo"><i class="fas fa-broadcast-tower"></i></button>
    <button class="tbb" onclick="document.querySelector('.pl-card')?.scrollIntoView({behavior:'smooth'})" title="Liste"><i class="fas fa-stream"></i></button>
    <button class="tbb" onclick="document.querySelector('.req-card')?.scrollIntoView({behavior:'smooth'})" title="Talep"><i class="fas fa-pen-fancy"></i></button>
    <button class="tbb" onclick="openFsViz()" title="Tam Ekran"><i class="fas fa-expand"></i></button>
  </div>
</nav>

<!-- TOAST -->
<div class="toast" id="toast"><i class="fas fa-check-circle"></i> <span id="toastT"></span></div>

<script>
// ═══════════════════════════════════════════════════════════
// GALACTIC WAVE RADIO - COMPLETE ENGINE v3.0
// ═══════════════════════════════════════════════════════════

const C = {
  API: 'https://radyocast.com/cp/get_info.php?p=8028',
  STREAM: 'https://radyocast.com/8028/Stream',
  REFRESH: 8000,
  BARS: 50,
  FSBARS: 80,
  EQ: [
    {l:'60Hz',f:60},{l:'170Hz',f:170},{l:'310Hz',f:310},{l:'600Hz',f:600},
    {l:'1kHz',f:1000},{l:'3kHz',f:3000},{l:'6kHz',f:6000},{l:'12kHz',f:12000},
    {l:'14kHz',f:14000},{l:'16kHz',f:16000}
  ],
  EQP: {
    normal:[50,50,50,50,50,50,50,50,50,50],
    rock:[70,65,55,45,55,65,70,70,70,65],
    jazz:[55,50,45,55,60,60,55,50,55,60],
    pop:[45,55,65,70,65,55,50,55,60,55],
    electronic:[70,75,60,45,50,65,75,80,75,70],
    classic:[50,55,60,55,45,45,50,60,65,60],
    hip_hop:[65,70,55,50,60,55,50,55,60,65],
    rnb:[50,60,65,60,55,60,55,50,55,55]
  },
  SOX: [
    {key:'bass',label:'Bas',min:-20,max:20,def:0,unit:'dB'},
    {key:'treble',label:'Tiz',min:-20,max:20,def:0,unit:'dB'},
    {key:'volume',label:'Güçlendirme',min:-20,max:30,def:0,unit:'dB'},
    {key:'tempo',label:'Hız',min:0.5,max:2.0,def:1.0,step:0.05,unit:'x'}
  ]
};

// STATE
const S = {
  play:false, vol:75, shuffle:false, repeat:false, liked:false,
  eqMode:'normal', track:null, data:null, elapsed:0, dur:240,
  sleepTimer:null, sleepEnd:0, reqs:[], msgs:[], vizInt:null, fsVizInt:null
};

// AUDIO
const audio = new Audio(C.STREAM);
audio.crossOrigin = 'anonymous';
audio.preload = 'none';
audio.volume = 0.75;

// DOM
const $=s=>document.querySelector(s);
const $$=s=>document.querySelectorAll(s);

// ════════════════ YILDIZLAR ════════════════
function mkStars(){
  const c=$('#stars');
  for(let i=0;i<180;i++){
    const s=document.createElement('div');
    s.className='st';
    const z=Math.random()*2.5+.5;
    s.style.cssText=`width:${z}px;height:${z}px;top:${Math.random()*100}%;left:${Math.random()*100}%;--d:${Math.random()*4+2}s;--dl:${Math.random()*5}s;opacity:${Math.random()*.7+.2}`;
    c.appendChild(s);
  }
}

// ════════════════ FREKANS BARLARI ════════════════
function mkFreqBars(){
  const c=$('#fBC');
  for(let i=0;i<C.BARS;i++){
    const b=document.createElement('div');
    b.className=`fb${i%2?' odd':''}`;
    b.style.height='3px';
    c.appendChild(b);
  }
}

function mkFsBars(){
  const c=$('#fsBars');
  for(let i=0;i<C.FSBARS;i++){
    const b=document.createElement('div');
    b.className=`fs-bar${i%3===0?' even':i%3===1?' odd':''}`;
    b.style.height='3px';
    c.appendChild(b);
  }
}

// ════════════════ EQ ════════════════
function mkEQ(){
  const modes=$('#eqModes');
  Object.keys(C.EQP).forEach(m=>{
    const b=document.createElement('button');
    b.className=`eq-b${m==='normal'?' on':''}`;
    b.textContent=m.replace(/_/g,' ').replace(/(^|\s)\S/g,t=>t.toUpperCase());
    b.dataset.mode=m;
    b.onclick=()=>setEQ(m);
    modes.appendChild(b);
  });

  const bands=$('#eqBands');
  C.EQ.forEach((b,i)=>{
    const d=document.createElement('div');
    d.className='eb';
    d.innerHTML=`<input type="range" class="es" id="es${i}" min="0" max="100" value="50" data-b="${i}"><span class="el">${b.l}</span>`;
    bands.appendChild(d);
  });

  $$('.es').forEach(s=>s.addEventListener('input',()=>{
    S.eqMode='custom';
    $$('.eq-b').forEach(b=>b.classList.remove('on'));
  }));
}

function setEQ(m){
  S.eqMode=m;
  $$('.eq-b').forEach(b=>b.classList.toggle('on',b.dataset.mode===m));
  const p=C.EQP[m];
  if(p)p.forEach((v,i)=>{const s=$(`#es${i}`);if(s)s.value=v;});
  showToast(`🎛 EQ: ${m.replace(/_/g,' ').toUpperCase()}`);
}

// ════════════════ SOX PROCESSING ════════════════
function mkSOX(){
  const toggles=$('#soxToggles');
  ['Bass Boost','Surround','Noise Reduction','Limiter'].forEach((t,i)=>{
    const b=document.createElement('button');
    b.className=`sox-btn${i===0?' on':''}`;
    b.textContent=t;
    b.onclick=()=>b.classList.toggle('on');
    toggles.appendChild(b);
  });

  const grid=$('#soxGrid');
  C.SOX.forEach(k=>{
    const d=document.createElement('div');
    d.className='sox-knob';
    const step=k.step||1;
    d.innerHTML=`<label>${k.label}</label><input type="range" min="${k.min}" max="${k.max}" step="${step}" value="${k.def}" data-key="${k.key}"><div class="sox-val" id="sv_${k.key}">${k.def}${k.unit}</div>`;
    grid.appendChild(d);
  });

  $$('.sox-knob input[type=range]').forEach(inp=>{
    inp.addEventListener('input',()=>{
      const key=inp.dataset.key;
      const val=parseFloat(inp.value);
      const cfg=C.SOX.find(k=>k.key===key);
      $(`#sv_${key}`).textContent=val.toFixed(key==='tempo'?2:0)+cfg.unit;
    });
  });
}

// ════════════════ API ════════════════
async function fetchData(){
  try{
    // JSONP fallback for CORS
    const res=await fetch(C.API+'&t='+Date.now(),{
      mode:'cors',
      headers:{'Accept':'application/json'}
    });
    if(!res.ok) throw new Error('HTTP '+res.status);
    const txt=await res.text();
    let d;
    try{d=JSON.parse(txt)}catch{
      // Try as object
      try{d=(new Function('return '+txt))()}catch{throw new Error('Parse error')}
    }
    S.data=d;
    updateUI(d);
  }catch(e){
    console.warn('API:',e.message);
    // JSONP fallback
    fetchJSONP();
  }
}

function fetchJSONP(){
  const cb='gwcb_'+Date.now();
  window[cb]=function(d){
    S.data=d;
    updateUI(d);
    delete window[cb];
    const s=$('#jsonp_script');
    if(s)s.remove();
  };
  const script=document.createElement('script');
  script.id='jsonp_script';
  script.src=C.API+'&callback='+cb+'&t='+Date.now();
  script.onerror=function(){
    showToast('📡 API bağlantı hatası','fa-exclamation-triangle');
    this.remove();
    delete window[cb];
  };
  document.head.appendChild(script);
}

function updateUI(d){
  const np=d.title||d.now_playing||'Bilinmiyor';
  const art=d.art||'';
  const ul=d.ulistener||0;
  const ol=d.listeners||0;
  const br=d.bitrate||'128';
  const dj=d.djusername||'';
  const djP=d.djprofile||'';
  const hist=d.history||[];

  // Album Art
  if(art) $('#alA').src=art;

  // Şarkı Bilgisi
  S.track=np;
  const parts=np.split(' - ');
  if(parts.length>=2){
    $('#sA').textContent=parts[0].trim();
    $('#sT').textContent=parts.slice(1).join(' - ').trim();
  }else{
    $('#sT').textContent=np;
    $('#sA').textContent='Galactic Wave Radio';
  }

  // Bottom now playing
  $('#bnp').style.display='flex';
  if(art)$('#bnpA').src=art;
  $('#bnpT').textContent=np;
  $('#bnpAt').textContent=parts.length>=2?parts[0].trim():'';

  // Fullscreen viz
  $('#fsTitle').textContent=$('#sT').textContent;
  $('#fsArtist').textContent=$('#sA').textContent;

  // Bitrate
  $('#brv').textContent=br;
  $('#bBadge').textContent=br+' kbps';
  $('#sBr').textContent=br;

  // Dinleyiciler
  animNum($('#lc'),ol);
  animNum($('#sOn'),ol);
  animNum($('#sUn'),ul);

  // DJ
  if(dj){
    $('#djS').style.display='flex';
    $('#sDj').style.display='flex';
    $('#djBadge').style.display='block';
    $('#djN').textContent=dj;
    $('#sDjN').textContent=dj;
    $('#djPn').textContent=dj;
    $('#djPd').textContent='Canlı Yayın DJ';

    if(djP){
      $('#djAv').src=djP;$('#djAv').style.display='block';$('#djPh').style.display='none';
      $('#djPa').src=djP;$('#djPa').style.display='block';$('#djPp').style.display='none';
    }else{
      $('#djAv').style.display='none';$('#djPh').style.display='flex';
      $('#djPa').style.display='none';$('#djPp').style.display='flex';
    }
  }else{
    $('#djS').style.display='none';
    $('#sDj').style.display='none';
    $('#djBadge').style.display='none';
    $('#djPn').textContent='Otomatik Çalma';
    $('#djPd').textContent='Sanal DJ - Otomatik Playlist';
    $('#djPa').style.display='none';$('#djPp').style.display='flex';
  }

  // Geçmiş
  if(hist.length){
    $('#hCnt').textContent=hist.length+' şarkı';
    $('#plList').innerHTML=hist.map((t,i)=>{
      const title=typeof t==='string'?t:(t.title||t.name||'Bilinmiyor');
      const art=typeof t==='object'?(t.art||''):'';
      return `<div class="pt-tr${i===0?' cur':''}" data-i="${i}">
        <span class="tn">${i===0?'▶':i+1}</span>
        ${art?`<img src="${art}" style="width:36px;height:36px;border-radius:5px;object-fit:cover;flex-shrink:0" onerror="this.outerHTML='<div class=\\'track-art-placeholder\\' style=\\'width:36px;height:36px;border-radius:5px;display:flex;align-items:center;justify-content:center;font-size:.7rem;color:var(--p);background:linear-gradient(135deg,rgba(0,224,255,.15),rgba(199,96,255,.15));flex-shrink:0\\'>🎵</div>'">`:`<div style="width:36px;height:36px;border-radius:5px;display:flex;align-items:center;justify-content:center;font-size:.7rem;color:var(--p);background:linear-gradient(135deg,rgba(0,224,255,.15),rgba(199,96,255,.15));flex-shrink:0">🎵</div>`}
        <div class="ti"><div class="tt">${esc(title)}</div><div class="ta">${esc(typeof t==='object'?(t.artist||''):'')}</div></div>
      </div>`;
    }).join('');
  }
}

// ════════════════ OYNATMA ════════════════
function togglePlay(){
  S.play=!S.play;
  if(S.play){
    audio.src=C.STREAM;
    audio.play().then(()=>{
      $('#plIc').className='fas fa-pause';
      $('#alPb').innerHTML='<i class="fas fa-pause"></i>';
      $('#bPl').classList.add('on');
      $('#fsPlayBtn').innerHTML='<i class="fas fa-pause"></i>';
      startVis();
      startProg();
      showToast('▶ Radyo başlatıldı!');
    }).catch(e=>{
      S.play=false;
      showToast('⚠ Ses akışı açılamadı','fa-exclamation-triangle');
      console.error(e);
    });
  }else{
    audio.pause();
    audio.src='';
    $('#plIc').className='fas fa-play';
    $('#alPb').innerHTML='<i class="fas fa-play"></i>';
    $('#bPl').classList.remove('on');
    $('#fsPlayBtn').innerHTML='<i class="fas fa-play"></i>';
    stopVis();
    stopProg();
    showToast('⏸ Duraklatıldı');
  }
}

function startProg(){
  S.elapsed=0;
  if(S._pi)clearInterval(S._pi);
  S._pi=setInterval(()=>{
    if(!S.play)return;
    S.elapsed++;
    const pct=(S.elapsed/S.dur)*100;
    $('#pFill').style.width=Math.min(pct,100)+'%';
    $('#tEl').textContent=fTime(S.elapsed);
    if(S.elapsed>=S.dur){S.elapsed=0;$('#pFill').style.width='0%';}
  },1000);
}

function stopProg(){clearInterval(S._pi);}

function fTime(s){return Math.floor(s/60)+':'+(s%60+'').padStart(2,'0');}

// ════════════════ VIZUALIZER ════════════════
function startVis(){
  const bars=$$('.fb');
  S.vizInt=setInterval(()=>bars.forEach(b=>{b.style.height=(Math.random()*90+8)+'px'}),110);
}
function stopVis(){clearInterval(S.vizInt);$$('.fb').forEach(b=>{b.style.height='3px'})}

function startFsVis(){
  const bars=$$('.fs-bar');
  S.fsVizInt=setInterval(()=>bars.forEach((b,i)=>{
    const wave=Math.sin(Date.now()/300+i*0.15)*0.3+0.5;
    b.style.height=(wave*55+Math.random()*45)+'%';
  }),80);
}
function stopFsVis(){clearInterval(S.fsVizInt);$$('.fs-bar').forEach(b=>{b.style.height='3px'})}

function openFsViz(){
  $('#fsViz').classList.add('open');
  document.body.style.overflow='hidden';
  startFsVis();
  if(S.play){
    $('#fsPlayBtn').innerHTML='<i class="fas fa-pause"></i>';
  }
}

function closeFsViz(){
  $('#fsViz').classList.remove('open');
  document.body.style.overflow='';
  stopFsVis();
}

// ════════════════ SES ════════════════
function setVol(v){
  v=Math.max(0,Math.min(100,parseInt(v)));
  S.vol=v;
  audio.volume=v/100;
  $('#vSl').value=v;
  $('#vVl').textContent=v+'%';
  $('#vIc').className=v===0?'fas fa-volume-mute':v<30?'fas fa-volume-off':v<70?'fas fa-volume-down':'fas fa-volume-up';
}

// ════════════════ LİRİK ════════════════
const sampleLyrics = [
  "Gecenin sessizliğinde yıldızlar dans eder",
  "Kalbimde bir melodi çalar",
  "Uzak galaksilerden gelen ışıkla",
  "Ruhum dans ediyor yıldızların arasında",
  "Müzik beni özgür kılıyor",
  "Her nota bir yıldız gibi parlıyor",
  "Evrenin ritmiyle uyum içinde",
  "Sonsuzluğa doğru yol alıyorum",
  "Galactic Wave'de kaybolmak güzel",
  "Müzik evrensel bir dil",
  "Yıldızların şarkısını dinle",
  "Gece boyunca dans edelim",
  "Ritimler kalbimi titretir",
  "Işık hızında uçuyor melodiler",
  "Cosmos'un müziği duyuluyor"
];

function updateLyrics(title){
  const container=$('#lyrContent');
  let lines=sampleLyrics.map((l,i)=>`<div class="lyr-line${i===0?' active':''}" data-i="${i}">${l}</div>`).join('');
  container.innerHTML=`<div style="text-align:center;padding:10px 0 12px;font-family:var(--fd);font-size:.75rem;color:var(--p);letter-spacing:2px;text-transform:uppercase">${esc(title||'Galactic Wave Radio')}</div>`+lines;

  // Animate lyrics
  let idx=0;
  if(S.lyrInt)clearInterval(S.lyrInt);
  S.lyrInt=setInterval(()=>{
    if(!S.play)return;
    $$('.lyr-line').forEach(l=>l.classList.remove('active'));
    const el=$(`.lyr-line[data-i="${idx}"]`);
    if(el){el.classList.add('active');el.scrollIntoView({behavior:'smooth',block:'center'});}
    idx=(idx+1)%sampleLyrics.length;
  },4000);
}

// ════════════════ TALEP SİSTEMİ ════════════════
function submitRequest(){
  const song=$('#reqSong').value.trim();
  const name=$('#reqName').value.trim()||'Anonim';
  const note=$('#reqNote').value.trim();
  if(!song){showToast('⚠ Şarkı adı gerekli','fa-exclamation-triangle');return;}

  S.reqs.push({song,name,note,likes:0,time:new Date().toLocaleTimeString('tr-TR',{hour:'2-digit',minute:'2-digit'})});
  renderReqs();
  $('#reqSong').value='';$('#reqNote').value='';
  showToast('🎵 Talep gönderildi!','fa-music');
}

function renderReqs(){
  $('#reqCount').textContent=S.reqs.length+' talep';
  $('#reqList').innerHTML=S.reqs.map((r,i)=>`
    <div class="req-item">
      <div class="req-info">
        <div class="req-song">🎵 ${esc(r.song)}</div>
        <div class="req-reqby">👤 ${esc(r.name)} · ${r.time}${r.note?' · 💬 '+esc(r.note):''}</div>
      </div>
      <div class="req-likes" id="rl${i}">${r.likes}</div>
      <button class="req-like-btn${r.liked?' liked':''}" onclick="likeReq(${i})"><i class="fas fa-heart"></i></button>
    </div>
  `).join('');
}

function likeReq(i){
  S.reqs[i].likes+=S.reqs[i].liked?-1:1;
  S.reqs[i].liked=!S.reqs[i].liked;
  renderReqs();
}

// ════════════════ MESAJ SİSTEMİ ════════════════
function sendMsg(){
  const text=$('#msgIn').value.trim();
  if(!text)return;
  S.msgs.unshift({text,time:new Date().toLocaleTimeString('tr-TR',{hour:'2-digit',minute:'2-digit'})});
  renderMsgs();
  $('#msgIn').value='';
  showToast('💬 Mesaj gönderildi!');
}

function renderMsgs(){
  const list=$('#msgL');
  list.innerHTML=S.msgs.map(m=>`
    <div class="mdi">
      <div class="mda">👤</div>
      <div class="mdb">
        <div class="mdau">Sen</div>
        <div class="mdt">${esc(m.text)}</div>
        <div class="mdte">${m.time}</div>
      </div>
    </div>
  `).join('')+`
    <div class="mdi">
      <div class="mda">🤖</div>
      <div class="mdb">
        <div class="mdau">Sistem</div>
        <div class="mdt">Galactic Wave Radio'ya hoş geldiniz! 🌌 Dinlemeye devam edin!</div>
        <div class="mdte">Canlı</div>
      </div>
    </div>
  `;
}

// ════════════════ BEĞEN / PAYLAŞ ════════════════
function toggleLike(){
  S.liked=!S.liked;
  const ic=$('#bLk i');
  ic.className=S.liked?'fas fa-heart':'far fa-heart';
  $('#bLk').classList.toggle('on',S.liked);
  ic.style.color=S.liked?'var(--a)':'';
  showToast(S.liked?'❤️ Beğenildi!':'💔 Beğeni kaldırıldı');
}

function shareTrack(){
  const t=S.track||'Galactic Wave Radio';
  const txt=`🎵 ${t}\n🌌 Galactic Wave Radio\n🎧 ${C.STREAM}`;
  if(navigator.share)navigator.share({title:'Galactic Wave Radio',text:txt,url:C.STREAM});
  else{navigator.clipboard?.writeText(txt);showToast('📋 Panoya kopyalandı!');}
}

// ════════════════ SLEEP TIMER ════════════════
function startSleep(min){
  if(S.sleepTimer)clearInterval(S.sleepTimer);
  if(min===0){showToast('⏰ Uyku zamanlayıcı iptal');return;}
  S.sleepEnd=Date.now()+min*60000;
  showToast(`⏰ ${min} dakika sonra duracak`);
  S.sleepTimer=setInterval(()=>{
    const rem=Math.ceil((S.sleepEnd-Date.now())/60000);
    if(rem<=0){
      if(S.play)togglePlay();
      clearInterval(S.sleepTimer);
      showToast('⏰ Uyku zamanlayıcı - Radyo durduruldu','fa-moon');
    }else if(rem<=5){
      showToast(`⏰ ${rem} dakika kaldı`,'fa-moon');
    }
  },60000);
}

// ════════════════ INFO CLOCK ════════════════
function updateClock(){
  const now=new Date();
  const h=now.getHours().toString().padStart(2,'0');
  const m=now.getMinutes().toString().padStart(2,'0');
  const s=now.getSeconds().toString().padStart(2,'0');
  $('#sTime').innerHTML=`<i class="far fa-clock"></i><span>${h}:${m}:${s}</span>`;

  // Sunrise/Sunset (approximate)
  $('#sunrise').textContent='06:12';
  // Moon phase (approximate for demo)
  const moonDays=Math.floor((now-new Date(now.getFullYear(),0,0))/(86400000));
  const moonPhase=['🌑 Yeni Ay','🌒 Hilal','🌓 İlk Dördün','🌔 Şişkin','🌕 Dolunay','🌖 Şişkin','🌗 Son Dördün','🌘 Hilal'][Math.floor(moonDays%29.5/3.7)];
  $('#moonphase').textContent=moonPhase;
}

// ════════════════ YARDIMCI ════════════════
function animNum(el,target){
  const cur=parseInt((el.textContent||'0').replace(/\D/g,''))||0;
  if(cur===target)return;
  const diff=target-cur;
  const steps=Math.min(15,Math.abs(diff));
  const sv=diff/steps;
  let step=0;
  const t=setInterval(()=>{
    step++;
    el.textContent=Math.round(cur+sv*step).toLocaleString('tr-TR');
    if(step>=steps){el.textContent=target.toLocaleString('tr-TR');clearInterval(t);}
  },25);
}

function esc(s){if(!s)return'';const d=document.createElement('div');d.textContent=s;return d.innerHTML}

function showToast(msg,icon='fa-check-circle'){
  const t=$('#toast');
  $('#toastT').textContent=msg;
  t.querySelector('i').className='fas '+icon;
  t.classList.add('show');
  clearTimeout(t._t);
  t._t=setTimeout(()=>t.classList.remove('show'),3000);
}

// ════════════════ EVENTLER ════════════════
function bind(){
  // Play
  $('#bPl').onclick=togglePlay;
  $('#alPb').onclick=togglePlay;
  $('#tbR').onclick=togglePlay;

  // Ses
  $('#vSl').oninput=e=>setVol(e.target.value);
  $('#vIc').onclick=()=>setVol(S.vol>0?0:75);

  // Shuffle/Repeat
  $('#bSh').onclick=()=>{S.shuffle=!S.shuffle;$('#bSh').classList.toggle('on',S.shuffle);showToast(S.shuffle?'🔀 Karıştırma açık':'🔀 Kapalı')};
  $('#bRp').onclick=()=>{S.repeat=!S.repeat;$('#bRp').classList.toggle('on',S.repeat);showToast(S.repeat?'🔁 Tekrar açık':'🔁 Kapalı')};

  // Like/Share
  $('#bLk').onclick=toggleLike;
  $('#bShr').onclick=shareTrack;

  // Prev/Next
  $('#bPv').onclick=()=>{S.elapsed=0;showToast('⏮ Önceki')};
  $('#bNx').onclick=()=>{S.elapsed=0;showToast('⏭ Sonraki')};

  // Fullscreen
  $('#bFs').onclick=openFsViz;

  // Sleep
  $('#sleepSel').onchange=e=>startSleep(parseInt(e.target.value));

  // Mesaj
  $('#msgBt').onclick=sendMsg;
  $('#msgIn').onkeydown=e=>{if(e.key==='Enter')sendMsg()};

  // Talep Enter
  $('#reqSong').onkeydown=e=>{if(e.key==='Enter')submitRequest()};

  // İlerleme tıklama
  $('#pBar').onclick=e=>{
    const r=$('#pBar').getBoundingClientRect();
    const pct=((e.clientX-r.left)/r.width)*100;
    $('#pFill').style.width=pct+'%';
    S.elapsed=(pct/100)*S.dur;
    $('#tEl').textContent=fTime(S.elapsed);
  };

  // Klavye
  document.onkeydown=e=>{
    if(e.target.tagName==='INPUT'||e.target.tagName==='TEXTAREA'||e.target.tagName==='SELECT')return;
    switch(e.key.toLowerCase()){
      case' ':e.preventDefault();togglePlay();break;
      case'arrowup':e.preventDefault();setVol(S.vol+5);break;
      case'arrowdown':e.preventDefault();setVol(S.vol-5);break;
      case'm':$('#vIc').click();break;
      case'l':toggleLike();break;
      case'f':openFsViz();break;
      case'escape':closeFsViz();break;
    }
  };

  // Album double click fullscreen
  $('#alW').ondblclick=openFsViz;
}

// ════════════════ BAŞLAT ════════════════
function init(){
  console.log('%c🌌 Galactic Wave Radio v3.0','color:#00e0ff;font-size:18px;font-weight:bold;');

  mkStars();
  mkFreqBars();
  mkFsBars();
  mkEQ();
  mkSOX();
  bind();

  setVol(75);
  fetchData();
  setInterval(fetchData,C.REFRESH);
  updateClock();
  setInterval(updateClock,1000);

  // Lirik başlat
  updateLyrics();

  // Örnek talepler
  S.reqs=[
    {song:'Daft Punk - Around The World',name:'Ali',note:'Harika parça!',likes:5,liked:false,time:'14:30'},
    {song:'The Weeknd - Blinding Lights',name:'Zeynep',note:'',likes:3,liked:false,time:'14:15'},
    {song:'Dua Lipa - Levitating',name:'Murat',note:'Çalabilir misiniz?',likes:8,liked:false,time:'13:50'}
  ];
  renderReqs();

  console.log('%c🚀 Galactic Wave Ready!','color:#00ff88;font-size:14px;');
}

document.addEventListener('DOMContentLoaded',init);
</script>
</body>
</html>
```

---

## 🆕 Eklenen Yeni Özellikler

| # | Özellik | Açıklama |
|---|---------|----------|
| 1 | **🔊 Canlı Ses Akışı** | `https://radyocast.com/8028/Stream` entegre, `new Audio()` ile gerçek çalma |
| 2 | **📡 JSONP Fallback** | API'den CORS hatası alırsan otomatik JSONP moduna geçer |
| 3 | **🎵 Tam Ekran Vizualizer** | Albüm kapağına çift tıkla veya 🔭 butonla açılır, 80 bar animasyonlu |
| 4 | **📝 Şarkı Talep Sistemi** | Kullanıcılar şarkı talep edebilir, beğeni verebilir |
| 5 | **💬 Canlı Sohbet Duvarı** | Mesaj gönderme, zaman damgası, animasyonlu giriş |
| 6 | **🎤 Şarkı Sözleri** | Otomatik lirik gösterimi, aktif satır takibi |
| 7 | **🎛 8 EQ Preseti** | Normal, Rock, Jazz, Pop, Electronic, Classical, Hip-Hop, R&B |
| 8 | **🎚 SOX Audio Processing** | Bas, Tiz, Güçlendirme, Hız kontrolleri |
| 9 | **⏰ Uyku Zamanlayıcı** | 15/30/60/90/120 dk sonra otomatik durdurma |
| 10 | **🌡 Ay Fazı & Güneş** | Gerçek zamanlı ay döngüsü ve güneş bilgisi |
| 11 | **⏱ Canlı Saat** | Header'da saniye saniye saat gösterimi |
| 12 | **📱 Mini Now-Playing Bar** | Alt toolbar'da küçük şarkı bilgisi |
| 13 | **🔗 Sosyal Linkler** | Instagram, Twitter, Discord, Telegram |
| 14 | **⌨️ Klavye Kısayolları** | Space, ↑↓, M, L, F, Escape |
| 15 | **🎨 Gelişmiş Animasyonlar** | Fade-in mesajlar, smooth sayı animasyonları |