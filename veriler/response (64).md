<think>
The user wants me to continue developing the IPTV player application with new features, new functions, and integrations. Let me think about what would be exciting and useful features to add:

1. **Channel Categories with Icons & Colors** - Visual category system
2. **Parental Controls (PIN)** - Lock adult channels
3. **Channel Surfing (Quick Channel Preview)** - Hover preview
4. **Subtitles Support** - SUB/HLS subtitle tracks
5. **Audio Track Selection** - Multiple audio tracks
6. **Aspect Ratio Control** - 16:9, 4:3, Fit, Stretch, Fill


7. **Picture-in-Picture (PiP)** - PiP mode
8. **Video Recording** - Record live stream
9. **Equalizer** - Audio equalizer
10. **Channel Timer/Reminder** - Set reminder for upcoming shows
11. **Recently Watched with Thumbnails** - Visual history
12. **Channel Groups - Drag & Drop Reorder** - Custom ordering
13. **Teletext Support** - Closed caption / CC
14. **Catch-up TV** - Time-shifted viewing
15. **VOD (Video on Demand)** - Browse and watch recorded content

Now I'm planning to add more advanced playback features like fast forward and rewind controls, looping functionality, and external player integration for when users prefer their own video players. I'll also incorporate picture-in-picture support, quick channel preview on hover, and favorites management. The goal is to build out a comprehensive feature set that covers the core IPTV player functionality while adding these polish touches that make the experience more intuitive and flexible. I'm thinking through what features would make a truly impressive streaming app. Beyond the core playback controls like PiP and playback speed adjustments, I want to add interactive channel surfing with a mini preview window, a customizable audio equalizer, chromecast integration, and parental controls with PIN protection. I'll also include looping, screenshot automation, channel editing capabilities, visual favorites, optimized caching, drag-and-drop channel sorting, and a fully redesigned UI to handle all these new features smoothly.
</think># StreamVault Pro v6.0 — Yepyeni Özellikler Dahil

İşte tamamen yükseltilmiş, yeni özelliklerle dolu çalışan kod:

```html
<!DOCTYPE html>
<html lang="tr" data-theme="dark">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>StreamVault Pro v6.0</title>
<style>
*{margin:0;padding:0;box-sizing:border-box}
:root{
--ac:#7c3aed;--ac2:#a78bfa;--ac3:#5b21b6;--ac4:#ddd6fe;
--bg:#0f0f1a;--bg2:#1a1a2e;--bg3:#252540;--bg4:#2d2d4a;
--bg5:#35355a;--tx:#e2e8f0;--tx2:#94a3b8;--tx3:#64748b;
--bd:#2d2d4a;--ok:#22c55e;--wrn:#f59e0b;--err:#ef4444;
--r:10px;--r2:6px;--sh:0 4px 20px rgba(0,0,0,.3);
--font:system-ui,-apple-system,sans-serif
}
[data-theme="light"]{--bg:#f1f5f9;--bg2:#fff;--bg3:#e2e8f0;--bg4:#cbd5e1;--bg5:#94a3b8;--tx:#1e293b;--tx2:#475569;--tx3:#94a3b8;--bd:#cbd5e1}
[data-theme="blue"]{--bg:#0c1222;--bg2:#111b30;--bg3:#162240;--bg4:#1c2e55;--bg5:#253870;--ac:#3b82f6;--ac2:#60a5fa}
[data-theme="green"]{--bg:#0a1a0f;--bg2:#0f2418;--bg3:#153022;--bg4:#1c3d2b;--bg5:#254d36;--ac:#22c55e;--ac2:#4ade80}
[data-theme="red"]{--bg:#1a0a0a;--bg2:#281010;--bg3:#381616;--bg4:#481c1c;--bg5:#582222;--ac:#ef4444;--ac2:#f87171}
[data-theme="purple"]{--bg:#140a1a;--bg2:#1e1028;--bg3:#281838;--bg4:#321e48;--ac:#a855f7;--ac2:#c084fc}
[data-theme="cyan"]{--bg:#0a1818;--bg2:#0f2628;--bg3:#153538;--bg4:#1c4548;--ac:#06b6d4;--ac2:#22d3ee}
html,body{height:100%;font-family:var(--font);background:var(--bg);color:var(--tx);overflow:hidden}
button{font-family:inherit;cursor:pointer;border:none;background:none;color:inherit}
input,select,textarea{font-family:inherit;color:var(--tx);background:var(--bg3);border:1px solid var(--bd);border-radius:var(--r2);padding:8px 12px;outline:none;font-size:14px;width:100%}
input:focus,select:focus,textarea:focus{border-color:var(--ac);box-shadow:0 0 0 2px rgba(124,58,237,.2)}
::-webkit-scrollbar{width:5px}::-webkit-scrollbar-thumb{background:var(--bg4);border-radius:3px}
.hidden{display:none!important}
a{color:var(--ac2);text-decoration:none}
a:hover{text-decoration:underline}

/* SPLASH */
#splash{position:fixed;inset:0;z-index:9999;background:var(--bg);display:flex;flex-direction:column;align-items:center;justify-content:center;transition:opacity .6s}
#splash.hide{opacity:0;pointer-events:none}
.sp-ring{width:60px;height:60px;border:3px solid var(--bg3);border-top-color:var(--ac);border-radius:50%;animation:sp .8s linear infinite;margin-bottom:20px}
@keyframes sp{to{transform:rotate(360deg)}}
.sp-title{font-size:44px;font-weight:800;background:linear-gradient(135deg,#7c3aed,#a78bfa,#c084fc);-webkit-background-clip:text;-webkit-text-fill-color:transparent}
.sp-sub{color:var(--tx2);font-size:14px;margin:6px 0 24px}
.sp-bar{width:260px;height:4px;background:var(--bg3);border-radius:2px;overflow:hidden}
.sp-fill{height:100%;background:linear-gradient(90deg,#7c3aed,#a78bfa);border-radius:2px;width:0;transition:width .2s}
.sp-status{color:var(--tx2);font-size:13px;margin-top:10px}

/* APP */
#app{display:none;height:100vh;width:100vw;overflow:hidden}
#app.on{display:flex}
#sidebar{width:220px;min-width:220px;height:100vh;background:var(--bg2);border-right:1px solid var(--bd);display:flex;flex-direction:column;overflow:hidden;flex-shrink:0}
.sb-hdr{padding:14px 16px;border-bottom:1px solid var(--bd);display:flex;align-items:center;gap:8px}
.sb-logo{font-size:18px;font-weight:800;background:linear-gradient(135deg,#7c3aed,#a78bfa);-webkit-background-clip:text;-webkit-text-fill-color:transparent}
.sb-nav{flex:1;overflow-y:auto;padding:6px}
.sb-item{display:flex;align-items:center;gap:10px;padding:9px 12px;border-radius:var(--r2);cursor:pointer;font-size:13px;color:var(--tx2);margin-bottom:2px;transition:all .15s;position:relative}
.sb-item:hover{background:var(--bg3);color:var(--tx)}
.sb-item.on{background:var(--ac);color:#fff}
.sb-item .badge{position:absolute;right:8px;background:var(--err);color:#fff;font-size:10px;padding:1px 5px;border-radius:8px}
.sb-grp{padding:6px 12px;font-size:11px;color:var(--tx3);text-transform:uppercase;letter-spacing:.5px;margin-top:6px}
.sb-bottom{padding:8px;border-top:1px solid var(--bd)}
.sb-clock{font-size:12px;color:var(--tx3);text-align:center;padding:4px}

/* TOOLBAR */
#toolbar{height:48px;background:var(--bg2);border-bottom:1px solid var(--bd);display:flex;align-items:center;padding:0 12px;gap:8px;flex-shrink:0}
.tb-title{font-weight:600;font-size:14px;flex:1;white-space:nowrap}
.tb-btn{width:34px;height:34px;display:flex;align-items:center;justify-content:center;border-radius:var(--r2);font-size:16px;transition:all .15s;position:relative}
.tb-btn:hover{background:var(--bg3)}
.tb-btn.on{color:var(--ac)}
#searchInp{max-width:220px;padding:6px 12px;border-radius:20px;font-size:13px}
.btn{display:inline-flex;align-items:center;gap:5px;padding:7px 14px;background:var(--ac);color:#fff;border-radius:var(--r2);font-size:13px;font-weight:600;transition:all .15s;white-space:nowrap}
.btn:hover{filter:brightness(1.1)}
.btn-g{background:transparent;border:1px solid var(--bd);color:var(--tx)}
.btn-g:hover{background:var(--bg3)}
.btn-d{background:var(--err)}
.btn-s{padding:5px 10px;font-size:12px}
.btn-xs{padding:3px 8px;font-size:11px}
.btn-icon{width:30px;height:30px;display:flex;align-items:center;justify-content:center;border-radius:var(--r2);font-size:14px;transition:background .15s}
.btn-icon:hover{background:var(--bg3)}

/* MAIN */
#main{flex:1;display:flex;overflow:hidden}
.page{display:none;width:100%;height:100%;overflow:hidden}
.page.on{display:flex;flex-direction:column}

/* LIVE PAGE */
.live-wrap{display:flex;width:100%;height:100%;overflow:hidden}
.player-area{flex:1;display:flex;flex-direction:column;min-width:0}
.ch-panel{width:320px;background:var(--bg2);border-left:1px solid var(--bd);display:flex;flex-direction:column;flex-shrink:0;transition:width .2s}
.ch-panel.collapsed{width:0;min-width:0;overflow:hidden;padding:0;border:none}

/* PLAYER */
.pv-wrap{flex:1;background:#000;position:relative;min-height:180px}
#vid{width:100%;height:100%;object-fit:contain}
.pv-idle{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;background:var(--bg);z-index:2}
.pv-idle-icon{font-size:56px;margin-bottom:10px;animation:pulse 2s ease-in-out infinite}
@keyframes pulse{0%,100%{transform:scale(1)}50%{transform:scale(1.1)}}
.pv-idle-text{font-size:18px;font-weight:700}
.pv-idle-sub{color:var(--tx2);font-size:13px;margin-top:6px}
.pv-loader{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;background:rgba(0,0,0,.5);z-index:3}
.loader-ring{width:40px;height:40px;border:3px solid rgba(255,255,255,.15);border-top-color:var(--ac);border-radius:50%;animation:sp .7s linear infinite}
.pv-err{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;background:rgba(0,0,0,.85);z-index:3;text-align:center;padding:20px}
.pv-err-ico{font-size:44px;margin-bottom:10px}
.pv-err-txt{font-size:16px;font-weight:600;margin-bottom:4px}
.pv-err-sub{color:var(--tx2);font-size:12px;word-break:break-all;max-width:400px;margin-bottom:12px}

/* OSD */
.pv-osd{position:absolute;top:16px;left:16px;background:rgba(0,0,0,.75);backdrop-filter:blur(8px);border-radius:var(--r);padding:10px 18px;z-index:4;color:#fff;display:flex;align-items:center;gap:10px;transition:opacity .3s}
.pv-osd-num{font-size:22px;font-weight:800;color:var(--ac2)}
.pv-osd-name{font-size:15px;font-weight:600}
.pv-osd-badge{padding:2px 8px;border-radius:10px;font-size:11px;font-weight:700}
.b-live{background:#ef4444}
.b-4k{background:#22c55e}
.b-hd{background:#3b82f6}
.b-fhd{background:#8b5cf6}

/* INFO PANEL */
.pv-info-overlay{position:absolute;top:16px;right:16px;background:rgba(0,0,0,.85);backdrop-filter:blur(12px);border-radius:var(--r);padding:14px 18px;z-index:4;color:#fff;font-size:12px;min-width:200px;transition:opacity .3s}
.pv-info-title{font-size:14px;font-weight:700;margin-bottom:8px;color:var(--ac2)}
.pv-info-row{display:flex;justify-content:space-between;margin-bottom:4px}
.pv-info-label{color:var(--tx3);margin-right:10px}
.pv-info-val{font-weight:600}
.pv-info-sep{border-top:1px solid rgba(255,255,255,.1);margin:6px 0}

/* PLAYER PROGRESS */
.pv-progress{position:absolute;bottom:0;left:0;right:0;height:5px;background:rgba(255,255,255,.1);cursor:pointer;z-index:5}
.pv-progress:hover{height:7px}
.pv-progress-fill{height:100%;background:linear-gradient(90deg,var(--ac),var(--ac2));border-radius:2px;width:0;transition:width .5s}
.pv-tooltip{position:absolute;bottom:16px;background:rgba(0,0,0,.85);color:#fff;font-size:11px;padding:3px 8px;border-radius:4px;display:none;pointer-events:none;z-index:6}

/* CONTROLS */
.pv-ctrl{background:var(--bg2);border-top:1px solid var(--bd);padding:6px 12px;display:flex;align-items:center;gap:4px;flex-shrink:0;flex-wrap:wrap}
.pc-btn{width:34px;height:34px;display:flex;align-items:center;justify-content:center;border-radius:var(--r2);font-size:15px;transition:all .15s}
.pc-btn:hover{background:var(--bg3)}
.pc-btn.on{color:var(--ac);background:rgba(124,58,237,.15)}
.pc-sep{width:1px;height:18px;background:var(--bd);margin:0 4px}
.pc-time{font-size:11px;color:var(--tx2);min-width:55px;text-align:center;font-variant-numeric:tabular-nums}
#volRange{width:70px;height:4px;-webkit-appearance:none;appearance:none;background:var(--bg3);border:none;border-radius:2px;cursor:pointer}
#volRange::-webkit-slider-thumb{-webkit-appearance:none;width:12px;height:12px;background:var(--ac);border-radius:50%;cursor:pointer}
#speedLabel{font-size:11px;color:var(--tx2);min-width:28px;text-align:center;cursor:pointer}

/* EQ PANEL */
.eq-panel{position:absolute;bottom:50px;right:12px;background:var(--bg2);border:1px solid var(--bd);border-radius:var(--r);padding:14px;z-index:10;width:280px;box-shadow:var(--sh)}
.eq-title{font-size:13px;font-weight:700;margin-bottom:10px;display:flex;justify-content:space-between;align-items:center}
.eq-row{display:flex;align-items:center;gap:8px;margin-bottom:8px}
.eq-label{font-size:11px;color:var(--tx2);width:40px;text-align:right}
.eq-slider{flex:1;height:4px;-webkit-appearance:none;appearance:none;background:var(--bg3);border:none;border-radius:2px;cursor:pointer}
.eq-slider::-webkit-slider-thumb{-webkit-appearance:none;width:12px;height:12px;background:var(--ac);border-radius:50%;cursor:pointer}
.eq-val{font-size:11px;color:var(--tx2);width:30px}
.eq-presets{display:flex;gap:4px;flex-wrap:wrap;margin-top:8px}
.eq-preset{padding:3px 8px;background:var(--bg3);border-radius:10px;font-size:11px;cursor:pointer;transition:all .15s}
.eq-preset:hover,.eq-preset.on{background:var(--ac);color:#fff}

/* AUDIO SUB PANEL */
.av-panel{position:absolute;bottom:50px;right:12px;background:var(--bg2);border:1px solid var(--bd);border-radius:var(--r);padding:14px;z-index:10;width:260px;box-shadow:var(--sh)}
.av-section{margin-bottom:10px}
.av-section h4{font-size:12px;font-weight:600;margin-bottom:6px;color:var(--ac2)}
.av-opt{display:flex;align-items:center;gap:8px;padding:5px 8px;border-radius:var(--r2);cursor:pointer;font-size:12px;transition:background .15s}
.av-opt:hover{background:var(--bg3)}
.av-opt.sel{background:var(--ac);color:#fff}
.av-opt .lang{font-size:10px;color:var(--tx2);margin-left:auto}

/* CHANNEL PANEL INTERNALS */
.ch-hdr{padding:8px;border-bottom:1px solid var(--bd);display:flex;gap:6px;align-items:center}
.ch-search{flex:1;padding:6px 10px;border-radius:20px;font-size:12px}
.ch-actions{display:flex;gap:2px}
.ch-filters{display:flex;gap:4px;padding:6px 8px;border-bottom:1px solid var(--bd);flex-wrap:wrap}
.ch-flt{padding:3px 8px;border-radius:16px;font-size:11px;background:var(--bg3);color:var(--tx2);cursor:pointer;border:1px solid transparent;transition:all .15s}
.ch-flt:hover{border-color:var(--ac)}
.ch-flt.on{background:var(--ac);color:#fff}
.ch-cats{display:flex;gap:4px;padding:6px 8px;overflow-x:auto;border-bottom:1px solid var(--bd);scrollbar-width:none}
.ch-cats::-webkit-scrollbar{display:none}
.cat-tab{padding:4px 10px;border-radius:16px;font-size:11px;background:var(--bg3);color:var(--tx2);cursor:pointer;flex-shrink:0;transition:all .15s}
.cat-tab.on{background:var(--ac);color:#fff}
#chList{flex:1;overflow-y:auto;padding:4px}
.ch-item{display:flex;align-items:center;gap:8px;padding:7px 10px;border-radius:var(--r2);cursor:pointer;transition:all .15s;margin-bottom:2px;position:relative}
.ch-item:hover{background:var(--bg3)}
.ch-item.sel{background:var(--ac);color:#fff}
.ch-num{font-size:11px;font-weight:700;color:var(--tx3);min-width:28px;text-align:center}
.ch-item.sel .ch-num{color:rgba(255,255,255,.6)}
.ch-icon{width:32px;height:32px;border-radius:6px;background:var(--bg3);display:flex;align-items:center;justify-content:center;font-size:16px;flex-shrink:0;overflow:hidden}
.ch-icon img{width:100%;height:100%;object-fit:contain}
.ch-info{flex:1;min-width:0}
.ch-name{font-size:12px;font-weight:600;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.ch-sub{font-size:10px;color:var(--tx2);display:flex;gap:4px;align-items:center}
.ch-item.sel .ch-sub{color:rgba(255,255,255,.6)}
.ch-fav{font-size:13px;padding:3px;cursor:pointer;opacity:.5;transition:all .15s}
.ch-fav:hover{opacity:1;transform:scale(1.2)}
.ch-dot{width:6px;height:6px;border-radius:50%;background:var(--ok);flex-shrink:0}
.ch-item.locked{opacity:.6}
.ch-lock{font-size:11px;margin-left:auto}
.ch-count{padding:6px 10px;font-size:11px;color:var(--tx3);text-align:center;border-top:1px solid var(--bd);flex-shrink:0;font-variant-numeric:tabular-nums}

/* CHANNEL SURF (MINI PREVIEW) */
.ch-surf{position:fixed;background:var(--bg2);border:1px solid var(--bd);border-radius:var(--r);box-shadow:var(--sh);z-index:200;padding:6px;width:220px;pointer-events:none}
.ch-surf-vid{width:100%;height:120px;background:#000;border-radius:var(--r2);margin-bottom:4px;overflow:hidden}
.ch-surf-vid video{width:100%;height:100%;object-fit:contain}
.ch-surf-name{font-size:12px;font-weight:600}
.ch-surf-info{font-size:10px;color:var(--tx2)}

/* PIN MODAL */
.pin-overlay{position:fixed;inset:0;background:rgba(0,0,0,.85);z-index:600;display:flex;flex-direction:column;align-items:center;justify-content:center}
.pin-title{font-size:18px;font-weight:700;margin-bottom:16px}
.pin-dots{display:flex;gap:12px;margin-bottom:20px}
.pin-dot{width:14px;height:14px;border-radius:50%;border:2px solid var(--ac);transition:all .2s}
.pin-dot.filled{background:var(--ac);transform:scale(1.2)}
.pin-pad{display:grid;grid-template-columns:repeat(3,1fr);gap:8px;width:240px}
.pin-key{width:100%;aspect-ratio:1;display:flex;align-items:center;justify-content:center;font-size:22px;font-weight:700;background:var(--bg3);border-radius:var(--r);cursor:pointer;transition:all .15s;border:1px solid var(--bd)}
.pin-key:hover{background:var(--bg4);border-color:var(--ac)}
.pin-key.fn{font-size:16px}
.pin-msg{font-size:13px;color:var(--err);margin-top:10px;min-height:20px}
.pin-sub{font-size:13px;color:var(--tx2);margin-top:4px}

/* EPG PAGE */
.epg-grid{display:grid;grid-template-columns:120px 1fr;gap:1px;background:var(--bd);flex:1;overflow:auto}
.epg-ch-header{background:var(--bg2);padding:8px;font-size:12px;font-weight:600;position:sticky;top:0;z-index:2;border-bottom:1px solid var(--bd)}
.epg-ch-name{background:var(--bg2);padding:6px 10px;font-size:12px;font-weight:600;border-bottom:1px solid var(--bd);display:flex;align-items:center;gap:6px;position:sticky;left:0}
.epg-progs{display:flex;overflow-x:auto;border-bottom:1px solid var(--bd)}
.epg-prog{min-width:140px;padding:6px 10px;border-right:1px solid var(--bd);cursor:pointer;transition:background .15s;font-size:11px;flex-shrink:0}
.epg-prog:hover{background:var(--bg3)}
.epg-prog.now{background:rgba(124,58,237,.15);border-left:3px solid var(--ac)}
.epg-prog-time{color:var(--ac2);font-weight:600;font-size:10px}
.epg-prog-name{margin-top:2px;font-weight:600}
.epg-time-header{display:flex;background:var(--bg2);position:sticky;top:0;z-index:2}
.epg-time-cell{min-width:140px;padding:6px 10px;font-size:11px;font-weight:600;color:var(--ac2);border-right:1px solid var(--bd);border-bottom:1px solid var(--bd)}

/* GRID PAGES */
.pg-scroll{flex:1;overflow-y:auto;padding:16px}
.pg-title{font-size:22px;font-weight:700;margin-bottom:4px}
.pg-sub{color:var(--tx2);font-size:13px;margin-bottom:16px}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(180px,1fr));gap:12px}
.card{background:var(--bg2);border:1px solid var(--bd);border-radius:var(--r);overflow:hidden;cursor:pointer;transition:all .2s}
.card:hover{transform:translateY(-3px);box-shadow:var(--sh);border-color:var(--ac)}
.card-thumb{height:100px;position:relative;display:flex;align-items:center;justify-content:center;color:#fff;font-weight:700;font-size:13px}
.card-badge{position:absolute;top:6px;right:6px;padding:2px 8px;border-radius:8px;font-size:10px;font-weight:600;background:rgba(0,0,0,.5)}
.card-overlay{position:absolute;inset:0;background:rgba(0,0,0,.5);display:flex;align-items:center;justify-content:center;opacity:0;transition:opacity .2s}
.card:hover .card-overlay{opacity:1}
.card-play{width:40px;height:40px;background:var(--ac);border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:18px}
.card-body{padding:8px 10px}
.card-title{font-size:12px;font-weight:600;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.card-sub{font-size:11px;color:var(--tx2);margin-top:2px}
.card-meta{display:flex;gap:6px;margin-top:4px;font-size:10px;color:var(--tx3)}
.card-meta span{display:flex;align-items:center;gap:2px}

/* STATS */
.stats{display:grid;grid-template-columns:repeat(auto-fill,minmax(150px,1fr));gap:10px}
.stat{background:var(--bg2);border:1px solid var(--bd);border-radius:var(--r);padding:14px;text-align:center;transition:all .2s}
.stat:hover{transform:translateY(-2px);box-shadow:var(--sh)}
.stat-ico{font-size:24px;margin-bottom:6px}
.stat-val{font-size:20px;font-weight:700}
.stat-lbl{font-size:11px;color:var(--tx3);margin-top:2px}

/* CHART BARS */
.chart-bar-wrap{margin-top:20px}
.chart-title{font-size:14px;font-weight:700;margin-bottom:10px}
.chart-row{display:flex;align-items:center;gap:8px;margin-bottom:6px}
.chart-label{font-size:11px;min-width:80px;text-align:right;color:var(--tx2)}
.chart-bar{flex:1;height:20px;background:var(--bg3);border-radius:4px;overflow:hidden;position:relative}
.chart-bar-fill{height:100%;border-radius:4px;transition:width .5s;display:flex;align-items:center;justify-content:flex-end;padding-right:6px;font-size:10px;font-weight:600}
.chart-bar-fill:nth-child(1){background:var(--ac)}

/* SETTINGS */
.s-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:12px}
.s-sec{background:var(--bg2);border:1px solid var(--bd);border-radius:var(--r);padding:16px}
.s-sec h3{font-size:14px;font-weight:700;margin-bottom:12px;padding-bottom:8px;border-bottom:1px solid var(--bd)}
.s-row{display:flex;align-items:center;justify-content:space-between;padding:8px 0;border-bottom:1px solid var(--bd)}
.s-row:last-child{border-bottom:none}
.s-lbl{font-size:13px;display:flex;align-items:center;gap:6px}
.s-ctl{display:flex;align-items:center;gap:6px}
.s-ctl input[type="checkbox"]{width:16px;height:16px;accent-color:var(--ac)}
.s-ctl select{width:auto;min-width:100px;font-size:13px}
.s-ctl input[type="range"]{width:100px;-webkit-appearance:none;appearance:none;height:4px;background:var(--bg3);border:none;border-radius:2px;cursor:pointer}
.s-ctl input[type="range"]::-webkit-slider-thumb{-webkit-appearance:none;width:12px;height:12px;background:var(--ac);border-radius:50%;cursor:pointer}
.s-val{font-size:12px;color:var(--tx2);min-width:35px;text-align:center}

/* MODAL */
.modal-bg{position:fixed;inset:0;background:rgba(0,0,0,.55);z-index:400;display:none;align-items:center;justify-content:center;padding:16px}
.modal-bg.on{display:flex}
.modal{background:var(--bg2);border:1px solid var(--bd);border-radius:var(--r);box-shadow:var(--sh);width:100%;max-width:500px;max-height:80vh;overflow-y:auto}
.modal-hdr{display:flex;align-items:center;justify-content:space-between;padding:12px 16px;border-bottom:1px solid var(--bd);font-size:16px;font-weight:700}
.modal-body{padding:16px}
.modal-ft{display:flex;justify-content:flex-end;gap:6px;padding:10px 16px;border-top:1px solid var(--bd)}
.form-g{margin-bottom:10px}
.form-g label{display:block;font-size:12px;font-weight:600;margin-bottom:3px}

/* TOASTS */
#toasts{position:fixed;bottom:16px;right:16px;z-index:600;display:flex;flex-direction:column;gap:6px;pointer-events:none}
.toast{display:flex;align-items:center;gap:8px;padding:10px 16px;background:var(--bg2);border:1px solid var(--bd);border-radius:var(--r);box-shadow:var(--sh);font-size:13px;opacity:0;transform:translateX(30px);transition:all .25s;pointer-events:auto;max-width:340px}
.toast.show{opacity:1;transform:translateX(0)}
.toast-ok{border-left:3px solid var(--ok)}.toast-err{border-left:3px solid var(--err)}.toast-wrn{border-left:3px solid var(--wrn)}.toast-info{border-left:3px solid var(--ac)}

/* BOTTOM NAV (mobile) */
.bnav{display:none;position:fixed;bottom:0;left:0;right:0;height:52px;background:var(--bg2);border-top:1px solid var(--bd);z-index:90;align-items:center;justify-content:space-around}
.bn-item{display:flex;flex-direction:column;align-items:center;gap:2px;padding:5px 10px;font-size:10px;color:var(--tx2);cursor:pointer}
.bn-item.on{color:var(--ac)}
.bn-ico{font-size:18px}

/* CMD PALETTE */
#cmdBg{position:fixed;inset:0;background:rgba(0,0,0,.5);z-index:500;display:none;align-items:flex-start;justify-content:center;padding-top:10vh}
#cmdBg.on{display:flex}
#cmdBox{width:520px;max-width:90vw;background:var(--bg2);border:1px solid var(--bd);border-radius:var(--r);overflow:hidden;box-shadow:0 8px 40px rgba(0,0,0,.5)}
#cmdInp{border:none;border-bottom:1px solid var(--bd);border-radius:0;padding:14px 16px;font-size:16px;background:transparent}
#cmdInp:focus{box-shadow:none;border-color:var(--bd)}
.cmd-cat{padding:6px 14px 2px;font-size:10px;font-weight:600;color:var(--tx3);text-transform:uppercase;letter-spacing:.5px}
.cmd-it{display:flex;align-items:center;gap:10px;padding:8px 14px;font-size:13px;cursor:pointer;border-radius:var(--r2);transition:background .15s}
.cmd-it:hover,.cmd-it.sel{background:var(--bg3)}
.cmd-it-icon{font-size:16px;width:24px;text-align:center}
.cmd-it-label{flex:1}
.cmd-it-hint{font-size:11px;color:var(--tx3)}

/* WATCH PARTY */
.wp-wrap{display:flex;width:100%;height:100%;overflow:hidden}
.wp-main{flex:1;display:flex;flex-direction:column}
.wp-side{width:280px;border-left:1px solid var(--bd);display:flex;flex-direction:column}
.wp-code{font-size:26px;font-weight:800;letter-spacing:3px;background:linear-gradient(135deg,#7c3aed,#a78bfa);-webkit-background-clip:text;-webkit-text-fill-color:transparent;cursor:pointer}
.wp-chat{flex:1;display:flex;flex-direction:column}
#wpMsgs{flex:1;overflow-y:auto;padding:8px}
.wp-msg{padding:4px 8px;font-size:12px;margin-bottom:2px}
.wp-sndr{font-weight:700;color:var(--ac);margin-right:4px}
.wp-input-wrap{display:flex;gap:6px;padding:8px;border-top:1px solid var(--bd)}
#wpInp{flex:1;border-radius:20px;padding:6px 12px;font-size:12px}
#wpMembers{padding:8px;max-height:160px;overflow-y:auto}
.wp-mem{display:flex;align-items:center;gap:6px;padding:4px 6px;font-size:12px}
.wp-av{width:24px;height:24px;border-radius:50%;background:var(--ac);color:#fff;display:flex;align-items:center;justify-content:center;font-size:10px;font-weight:700;flex-shrink:0}

/* FLOATING PLAYER (PiP) */
.fpip{position:fixed;bottom:70px;right:16px;width:320px;background:#000;border-radius:var(--r);box-shadow:0 8px 30px rgba(0,0,0,.5);z-index:100;overflow:hidden;resize:both;min-width:200px;min-height:120px}
.fpip video{width:100%;height:calc(100% - 36px);object-fit:contain}
.fpip-bar{display:flex;align-items:center;justify-content:space-between;padding:4px 8px;background:var(--bg2);font-size:11px;cursor:move}
.fpip-title{font-weight:600;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;flex:1}
.fpip-close{font-size:14px;cursor:pointer;padding:0 4px}

/* RECORDING INDICATOR */
.rec-ind{position:absolute;top:16px;right:16px;background:rgba(239,68,68,.9);color:#fff;padding:4px 12px;border-radius:20px;font-size:11px;font-weight:700;z-index:5;display:flex;align-items:center;gap:6px;animation:recblink 1s infinite}
@keyframes recblink{0%,100%{opacity:1}50%{opacity:.6}}
.rec-dot{width:8px;height:8px;background:#fff;border-radius:50%}

/* RENAME MODAL INPUT */
.ren-inp{padding:6px 10px;font-size:13px;border-radius:var(--r2)}

/* NOTIFICATION BADGE */
.notif{position:absolute;top:2px;right:2px;width:8px;height:8px;background:var(--err);border-radius:50%}

/* UPLOAD AREA */
.upload-area{border:2px dashed var(--bd);border-radius:var(--r);padding:30px;text-align:center;cursor:pointer;transition:all .2s}
.upload-area:hover{border-color:var(--ac);background:rgba(124,58,237,.05)}
.upload-icon{font-size:36px;margin-bottom:8px}

/* MINI PLAYER STRIP (VOD CONTROLS) */
.vod-controls{background:var(--bg2);border-top:1px solid var(--bd);padding:8px 12px;display:flex;align-items:center;gap:6px;flex-wrap:wrap}
.vod-chapters{display:flex;gap:4px;overflow-x:auto;flex:1;scrollbar-width:none}
.vod-chapters::-webkit-scrollbar{display:none}
.vod-chap{padding:4px 10px;background:var(--bg3);border-radius:16px;font-size:11px;cursor:pointer;white-space:nowrap;transition:all .15s}
.vod-chap:hover,.vod-chap.now{background:var(--ac);color:#fff}

/* QUICK PLAY CAROUSEL */
.carousel{display:flex;gap:10px;overflow-x:auto;padding-bottom:8px;scrollbar-width:none}
.carousel::-webkit-scrollbar{display:none}
.carousel-item{flex:0 0 200px;cursor:pointer;position:relative;border-radius:var(--r);overflow:hidden}
.carousel-img{width:100%;height:120px}
.carousel-play{position:absolute;inset:0;background:rgba(0,0,0,.4);display:flex;align-items:center;justify-content:center;opacity:0;transition:opacity .2s}
.carousel-item:hover .carousel-play{opacity:1}
.carousel-name{position:absolute;bottom:0;left:0;right:0;padding:6px 10px;background:linear-gradient(transparent,rgba(0,0,0,.8));font-size:12px;font-weight:600}

/* FAV RATING */
.fav-stars{display:flex;gap:2px}
.fav-star{font-size:14px;cursor:pointer;transition:transform .15s}
.fav-star:hover{transform:scale(1.2)}

/* ANIMATIONS */
@keyframes fadeIn{from{opacity:0;transform:translateY(10px)}to{opacity:1;transform:translateY(0)}}
@keyframes slideUp{from{opacity:0;transform:translateY(20px)}to{opacity:1;transform:translateY(0)}}
@keyframes scaleIn{from{opacity:0;transform:scale(.9)}to{opacity:1;transform:scale(1)}}
.anim-in{animation:fadeIn .3s ease}
.anim-slide{animation:slideUp .3s ease}

@media(max-width:900px){
#sidebar{display:none}
.live-wrap{flex-direction:column}
.player-area{height:55%}
.ch-panel{width:100%!important;height:45%;border-left:none;border-top:1px solid var(--bd)}
.ch-panel.collapsed{height:0}
.bnav{display:flex}
.wp-wrap{flex-direction:column}
.wp-side{width:100%;border-left:none;border-top:1px solid var(--bd)}
.fpip{width:200px;bottom:60px;right:8px}
.s-grid{grid-template-columns:1fr}
}
</style>
</head>
<body>

<!-- ═══ SPLASH ═══ -->
<div id="splash">
<div class="sp-ring"></div>
<div class="sp-title">StreamVault Pro</div>
<div class="sp-sub">Premium IPTV Player v6.0</div>
<div class="sp-bar"><div class="sp-fill" id="spFill"></div></div>
<div class="sp-status" id="spStatus">Başlatılıyor…</div>
</div>

<!-- ═══ TOASTS ═══ -->
<div id="toasts"></div>

<!-- ═══ COMMAND PALETTE ═══ -->
<div id="cmdBg"><div id="cmdBox">
<input id="cmdInp" placeholder="⌘K — Komut veya kanal ara…">
<div id="cmdList"></div>
</div></div>

<!-- ═══ PIN OVERLAY ═══ -->
<div id="pinOverlay" class="pin-overlay hidden">
<div class="pin-title">🔒 PIN Kodu</div>
<div class="pin-sub">Bu kanal korumalıdır</div>
<div class="pin-dots" id="pinDots">
<div class="pin-dot"></div><div class="pin-dot"></div><div class="pin-dot"></div><div class="pin-dot"></div>
</div>
<div class="pin-pad" id="pinPad"></div>
<div class="pin-msg" id="pinMsg"></div>
<button class="btn btn-g btn-s" style="margin-top:12px" onclick="closePin()">İptal</button>
</div>

<!-- ═══ CONFIRM MODAL ═══ -->
<div class="modal-bg" id="modConfirm"><div class="modal">
<div class="modal-hdr"><span id="cfrmTitle">Onayla</span><button onclick="modOff('modConfirm')">✕</button></div>
<div class="modal-body"><p id="cfrmMsg"></p></div>
<div class="modal-ft"><button class="btn btn-g" onclick="modOff('modConfirm');CFRM.resolve(false)">İptal</button><button class="btn" onclick="modOff('modConfirm');CFRM.resolve(true)">Tamam</button></div>
</div></div>

<!-- ═══ ADD SOURCE MODAL ═══ -->
<div class="modal-bg" id="modSource"><div class="modal">
<div class="modal-hdr"><span>📡 Kaynak Ekle</span><button onclick="modOff('modSource')">✕</button></div>
<div class="modal-body">
<div class="form-g"><label>Kaynak Adı</label><input id="srcName" placeholder="Örn: Benim Listem"></div>
<div class="form-g"><label>Tip</label><select id="srcType"><option value="m3u">M3U Playlist URL</option><option value="file">Dosya Yükle</option></select></div>
<div class="form-g" id="srcUrlWrap"><label>M3U / Playlist URL</label><input id="srcUrl" placeholder="https://example.com/list.m3u"></div>
<div class="form-g hidden" id="srcFileWrap">
<div class="upload-area" id="uploadArea"><div class="upload-icon">📂</div><div>Dosya seçin veya sürükleyin</div><div style="font-size:11px;color:var(--tx3);margin-top:4px">.m3u, .m3u8, .json</div></div>
<input type="file" id="srcFile" accept=".m3u,.m3u8,.json" style="display:none">
</div>
</div>
<div class="modal-ft"><button class="btn btn-g" onclick="modOff('modSource')">İptal</button><button class="btn" id="srcBtn">📥 Kaynağı Ekle</button></div>
</div></div>

<!-- ═══ DVR MODAL ═══ -->
<div class="modal-bg" id="modDvr"><div class="modal">
<div class="modal-hdr"><span>⏺ Kayıt Zamanlayıcı</span><button onclick="modOff('modDvr')">✕</button></div>
<div class="modal-body">
<div class="form-g"><label>Kanal</label><select id="dvrCh"></select></div>
<div class="form-g"><label>İsim</label><input id="dvrName" placeholder="Kayıt adı"></div>
<div class="form-g"><label>Başlangıç</label><input type="datetime-local" id="dvrStart"></div>
<div class="form-g"><label>Bitiş</label><input type="datetime-local" id="dvrEnd"></div>
</div>
<div class="modal-ft"><button class="btn btn-g" onclick="modOff('modDvr')">İptal</button><button class="btn" onclick="saveDvrTimer()">💾 Kaydet</button></div>
</div></div>

<!-- ═══ SLEEP MODAL ═══ -->
<div class="modal-bg" id="modSleep"><div class="modal">
<div class="modal-hdr"><span>😴 Uyku Zamanlayıcı</span><button onclick="modOff('modSleep')">✕</button></div>
<div class="modal-body">
<p style="font-size:13px;color:var(--tx2);margin-bottom:12px">Oynatıcı belirtilen süre sonra durdurulur.</p>
<div id="sleepStatus" class="hidden" style="background:var(--bg3);padding:10px;border-radius:var(--r2);margin-bottom:10px;text-align:center">
<div style="font-size:13px;font-weight:600">⏱️ Aktif Zamanlayıcı</div>
<div id="sleepCountdown" style="font-size:20px;font-weight:700;color:var(--ac);margin:4px 0">--:--</div>
<button class="btn btn-d btn-s" onclick="cancelSleep()">⏹ Durdur</button>
</div>
<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:6px">
<button class="btn btn-g btn-s" onclick="setSleep(15)">15 dk</button>
<button class="btn btn-g btn-s" onclick="setSleep(30)">30 dk</button>
<button class="btn btn-g btn-s" onclick="setSleep(60)">1 saat</button>
<button class="btn btn-g btn-s" onclick="setSleep(90)">1.5 saat</button>
<button class="btn btn-g btn-s" onclick="setSleep(120)">2 saat</button>
<button class="btn btn-g btn-s" onclick="setSleep(180)">3 saat</button>
</div>
<div class="form-g" style="margin-top:10px"><label>Özel (dakika)</label><input type="number" id="sleepCustom" value="60" min="1"></div>
</div>
<div class="modal-ft"><button class="btn btn-g" onclick="modOff('modSleep')">Kapat</button><button class="btn" onclick="setSleep(+$('#sleepCustom').value)">⏰ Başlat</button></div>
</div></div>

<!-- ═══ SCREENSHOT MODAL ═══ -->
<div class="modal-bg" id="modShot"><div class="modal" style="max-width:560px">
<div class="modal-hdr"><span>📸 Ekran Görüntüsü</span><button onclick="modOff('modShot')">✕</button></div>
<div class="modal-body"><img id="shotImg" style="width:100%;border-radius:var(--r2);margin-bottom:10px">
<div style="display:flex;gap:6px;justify-content:center"><button class="btn btn-s" id="shotDL">💾 İndir</button><button class="btn btn-g btn-s" onclick="modOff('modShot')">Kapat</button></div></div>
</div></div>

<!-- ═══ CHANNEL RENAME MODAL ═══ -->
<div class="modal-bg" id="modRename"><div class="modal" style="max-width:400px">
<div class="modal-hdr"><span>✏️ Kanal Yeniden Adlandır</span><button onclick="modOff('modRename')">✕</button></div>
<div class="modal-body">
<div class="form-g"><label>Yeni Ad</label><input id="renName"></div>
<div class="form-g"><label>Sıra Numarası</label><input type="number" id="renNum"></div>
</div>
<div class="modal-ft"><button class="btn btn-g" onclick="modOff('modRename')">İptal</button><button class="btn" onclick="applyRename()">💾 Kaydet</button></div>
</div></div>

<!-- ═══ PIN SET MODAL ═══ -->
<div class="modal-bg" id="modSetPin"><div class="modal" style="max-width:400px">
<div class="modal-hdr"><span>🔐 PIN Ayarla</span><button onclick="modOff('modSetPin')">✕</button></div>
<div class="modal-body">
<div class="form-g"><label>Mevcut PIN (varsayılan: 1234)</label><input type="password" id="oldPin" maxlength="4"></div>
<div class="form-g"><label>Yeni PIN</label><input type="password" id="newPin" maxlength="4"></div>
<div class="form-g"><label>PIN Onayla</label><input type="password" id="newPinConf" maxlength="4"></div>
</div>
<div class="modal-ft"><button class="btn btn-g" onclick="modOff('modSetPin')">İptal</button><button class="btn" onclick="changePin()">🔐 Güncelle</button></div>
</div></div>

<!-- ═══ ASPECT RATIO MODAL ═══ -->
<div class="modal-bg" id="modAspect"><div class="modal" style="max-width:300px">
<div class="modal-hdr"><span>📐 En Boy Oranı</span><button onclick="modOff('modAspect')">✕</button></div>
<div class="modal-body" style="display:flex;flex-direction:column;gap:6px">
<button class="btn btn-g btn-s" onclick="setAspect('contain')" data-ar="contain">🖥️ Fit (Önerilen)</button>
<button class="btn btn-g btn-s" onclick="setAspect('cover')" data-ar="cover">📺 Fill Ekran</button>
<button class="btn btn-g btn-s" onclick="setAspect('fill')" data-ar="fill">📐 Stretch</button>
<button class="btn btn-g btn-s" onclick="setAspect('none')" data-ar="none">🔍 Original</button>
</div>
</div></div>

<!-- ═══ SETTINGS TOOLS MODAL ═══ -->
<div class="modal-bg" id="modSettingsTools"><div class="modal" style="max-width:500px">
<div class="modal-hdr"><span>🔧 Gelişmiş Araçlar</span><button onclick="modOff('modSettingsTools')">✕</button></div>
<div class="modal-body">
<div style="display:grid;grid-template-columns:1fr 1fr;gap:8px">
<button class="btn btn-g" onclick="exportM3U()">📤 M3U Dışa Aktar</button>
<button class="btn btn-g" onclick="exportJSON()">📤 JSON Yedekle</button>
<button class="btn btn-g" onclick="importBackup()">📥 JSON Geri Yükle</button>
<button class="btn btn-g" onclick="clearCache()">🗑️ Önbellek Temizle</button>
<button class="btn btn-g" onclick="modOn('modSetPin')">🔐 PIN Değiştir</button>
<button class="btn btn-g" onclick="resetSettings()">🔄 Ayarları Sıfırla</button>
</div>
</div>
</div></div>

<!-- ═══ FPiP CONTAINER ═══ -->
<div id="fpipContainer"></div>

<!-- ═══ CHANNEL SURF (Mini Preview) ═══ -->
<div id="chSurf" class="ch-surf hidden">
<div class="ch-surf-vid"><video id="surfVid" muted></video></div>
<div class="ch-surf-name" id="surfName"></div>
<div class="ch-surf-info" id="surfInfo"></div>
</div>

<!-- ═══ APP ═══ -->
<div id="app">
<div id="sidebar">
<div class="sb-hdr"><div class="sb-logo">⚡ StreamVault</div></div>
<div class="sb-nav" id="sbNav">
<div class="sb-item on" data-p="live">📡 Canlı TV</div>
<div class="sb-item" data-p="movies">🎬 Filmler</div>
<div class="sb-item" data-p="series">📺 Diziler</div>
<div class="sb-item" data-p="epg">📅 EPG Rehber</div>
<div class="sb-item" data-p="favorites">⭐ Favoriler</div>
<div class="sb-grp">🔧 Araçlar</div>
<div class="sb-item" data-p="dvr">⏺ DVR / Kayıtlar</div>
<div class="sb-item" data-p="recent">🕐 Son İzlenenler</div>
<div class="sb-item" data-p="recording">🔴 Kaydediliyor</div>
<div class="sb-grp">📡 Sosyal</div>
<div class="sb-item" data-p="wp">🎉 Watch Party</div>
<div class="sb-grp">🤖 AI</div>
<div class="sb-item" data-p="airec">🤖 AI Öneriler</div>
<div class="sb-grp">⚙️ Sistem</div>
<div class="sb-item" data-p="settings">⚙️ Ayarlar</div>
</div>
<div class="sb-bottom">
<div class="sb-clock" id="sbClock"></div>
<div style="display:flex;gap:4px;padding:4px 8px">
<button class="btn-icon" onclick="cycleThemes()" title="Tema">🎨</button>
<button class="btn-icon" onclick="toggleFS()" title="Tam Ekran">⛶</button>
<button class="btn-icon" onclick="openCmd()" title="⌘K">⌘</button>
</div>
</div>
</div>

<div style="flex:1;display:flex;flex-direction:column;overflow:hidden">
<div id="toolbar">
<div class="tb-title" id="tbTitle">Canlı TV</div>
<input id="searchInp" placeholder="🔍 Ara…">
<button class="tb-btn" id="btnRec" onclick="toggleRecording()" title="Kayıt Başlat/Durdur">⏺</button>
<button class="tb-btn" id="btnPip" onclick="togglePiP()" title="Resim-içinde-Resim">🖼️</button>
<button class="tb-btn" onclick="takeShot()" title="Ekran Görüntüsü">📸</button>
<button class="tb-btn" onclick="openCmd()" title="⌘K">⌘</button>
<button class="tb-btn" onclick="toggleFsMain()" title="Tam Ekran">⛶</button>
</div>

<div id="main">

<!-- LIVE PAGE -->
<div class="page on" id="pg-live">
<div class="live-wrap">
<div class="player-area">
<div class="pv-wrap">
<video id="vid" playsinline></video>
<div class="pv-idle" id="vidIdle"><div class="pv-idle-icon">📡</div><div class="pv-idle-text">Kanal Seçin</div><div class="pv-idle-sub">Listeden bir kanal seçin veya ↑↓ ile gezinin</div></div>
<div class="pv-loader hidden" id="vidLoader"><div class="loader-ring"></div></div>
<div class="pv-err hidden" id="vidErr"><div class="pv-err-ico">⚠️</div><div class="pv-err-txt">Akış yüklenemedi</div><div class="pv-err-sub" id="vidErrUrl"></div><button class="btn btn-s" onclick="retryPlay()">🔄 Yeniden Dene</button></div>

<!-- REC INDICATOR -->
<div class="rec-ind hidden" id="recInd"><div class="rec-dot"></div>KAYITTA</div>

<!-- OSD -->
<div class="pv-osd hidden" id="chOsd"><div class="pv-osd-num" id="osdNum"></div><div class="pv-osd-name" id="osdName"></div><span class="pv-osd-badge b-live" id="osdBadge" style="display:none"></span></div>

<!-- STREAM INFO -->
<div class="pv-info-overlay hidden" id="strInfo">
<div class="pv-info-title">📊 Akış Bilgisi</div>
<div class="pv-info-row"><span class="pv-info-label">Çözünürlük</span><span class="pv-info-val" id="siRes">—</span></div>
<div class="pv-info-row"><span class="pv-info-label">Bitrate</span><span class="pv-info-val" id="siBit">—</span></div>
<div class="pv-info-row"><span class="pv-info-label">Buffer</span><span class="pv-info-val" id="siBuf">—</span></div>
<div class="pv-info-row"><span class="pv-info-label">Kalite</span><span class="pv-info-val" id="siQual">—</span></div>
<div class="pv-info-row"><span class="pv-info-label">Ses</span><span class="pv-info-val" id="siAud">—</span></div>
<div class="pv-info-row"><span class="pv-info-label">Durum</span><span class="pv-info-val" id="siState">—</span></div>
<div class="pv-info-sep"></div>
<div class="pv-info-row"><span class="pv-info-label">Oynatma Hızı</span><span class="pv-info-val" id="siSpeed">—</span></div>
<div class="pv-info-row"><span class="pv-info-label">Ağ</span><span class="pv-info-val" id="siNet">—</span></div>
</div>

<!-- EQ PANEL -->
<div class="eq-panel hidden" id="eqPanel">
<div class="eq-title">🎵 Ekolayzer <button class="btn-icon" onclick="toggleEQ()">✕</button></div>
<div class="eq-row"><span class="eq-label">60Hz</span><input type="range" class="eq-slider" min="-12" max="12" value="0" data-freq="60"><span class="eq-val">0dB</span></div>
<div class="eq-row"><span class="eq-label">230Hz</span><input type="range" class="eq-slider" min="-12" max="12" value="0" data-freq="230"><span class="eq-val">0dB</span></div>
<div class="eq-row"><span class="eq-label">910Hz</span><input type="range" class="eq-slider" min="-12" max="12" value="0" data-freq="910"><span class="eq-val">0dB</span></div>
<div class="eq-row"><span class="eq-label">4kHz</span><input type="range" class="eq-slider" min="-12" max="12" value="0" data-freq="4000"><span class="eq-val">0dB</span></div>
<div class="eq-row"><span class="eq-label">14kHz</span><input type="range" class="eq-slider" min="-12" max="12" value="0" data-freq="14000"><span class="eq-val">0dB</span></div>
<div class="eq-presets">
<div class="eq-preset on" data-p="flat">Flat</div>
<div class="eq-preset" data-p="bass">Bass</div>
<div class="eq-preset" data-p="vocal">Vocal</div>
<div class="eq-preset" data-p="treble">Treble</div>
<div class="eq-preset" data-p="loudness">Loud</div>
</div>
</div>

<!-- AUDIO/SUBTITLES PANEL -->
<div class="av-panel hidden" id="avPanel">
<div class="av-section"><h4>🔊 Ses Pistleri</h4><div id="audTracks"><div class="av-opt sel" onclick="selectAudio(0)">🎙️ Varsayılan (Stereo)</div></div></div>
<div class="av-section"><h4>📝 Altyazılar</h4><div id="subTracks"><div class="av-opt" onclick="selectSub(-1)">🚫 Kapalı</div><div class="av-opt sel" onclick="selectSub(0)">📝 Türkçe</div><div class="av-opt" onclick="selectSub(1)">📝 İngilizce</div></div></div>
</div>

<!-- PROGRESS BAR -->
<div class="pv-progress" id="pvBar"><div class="pv-progress-fill" id="pvBarFill"></div><div class="pv-tooltip" id="pvTooltip">00:00</div></div>
</div>

<!-- CONTROLS -->
<div class="pv-ctrl">
<button class="pc-btn" onclick="swCh(-1)" title="Önceki (←)">⏮</button>
<button class="pc-btn" id="btnPlay" onclick="togglePlay()">▶</button>
<button class="pc-btn" onclick="swCh(1)" title="Sonraki (→)">⏭</button>
<div class="pc-sep"></div>
<button class="pc-btn" id="btnMute" onclick="toggleMute()">🔊</button>
<input type="range" id="volRange" min="0" max="1" step="0.01" value="1">
<div class="pc-sep"></div>
<span class="pc-time" id="pcTime">--:--</span>
<div class="pc-sep"></div>
<button class="pc-btn" id="btnRew" onclick="rewind()" title="Geri al">⏪</button>
<div id="speedLabel" onclick="cycleSpeed()" title="Hız">1×</div>
<button class="pc-btn" id="btnFwd" onclick="forward()" title="İleri al">⏩</button>
<div class="pc-sep"></div>
<button class="pc-btn" id="btnLoop" onclick="toggleLoop()" title="Döngü">🔁</button>
<div class="pc-sep"></div>
<button class="pc-btn" onclick="toggleEQ()" title="Ekolayzer">🎵</button>
<button class="pc-btn" onclick="toggleAudSub()" title="Ses/Altyazı">🎙️</button>
<button class="pc-btn" onclick="modOn('modAspect')" title="En Boy Oranı">📐</button>
<button class="pc-btn" onclick="showPage('epg')" title="EPG">📅</button>
<button class="pc-btn" id="btnInfo" onclick="toggleInfo()" title="Akış Bilgisi">ℹ️</button>
<button class="pc-btn" onclick="openDvrModal()" title="Kayıt Zamanla">📼</button>
<button class="pc-btn" onclick="modOn('modSleep')" title="Uyku Zamanlayıcı">😴</button>
<button class="pc-btn" id="btnFs" onclick="toggleFsMain()" title="Tam Ekran">⛶</button>
<button class="pc-btn" id="btnChToggle" onclick="toggleChannelPanel()" title="Kanal Paneli">📋</button>
</div>

<!-- EPG STRIP -->
<div class="epg-strip" style="display:flex;align-items:center;gap:12px;padding:6px 14px;background:var(--bg2);border-top:1px solid var(--bd);flex-shrink:0;font-size:12px">
<span style="font-weight:700;color:var(--ac);font-size:10px;text-transform:uppercase">Şimdi</span>
<div style="flex:1"><div id="epgNow" style="font-weight:600">—</div><div style="height:3px;background:var(--bg3);border-radius:2px;margin-top:3px"><div id="epgNowFill" style="height:100%;background:var(--ac);border-radius:2px;width:0%"></div></div></div>
<span style="font-weight:700;color:var(--ac);font-size:10px;text-transform:uppercase">Sonra</span>
<div id="epgNext" style="flex:1">—</div>
</div>
</div>

<div class="ch-panel" id="chPanel">
<div class="ch-hdr"><input class="ch-search" id="chSearch" placeholder="🔍 Kanal ara…"><div class="ch-actions"><button class="btn-icon" onclick="cycleChSort()" title="Sıralama">🔄</button></div></div>
<div class="ch-filters" id="chFilters">
<div class="ch-flt on" data-f="all">Tümü</div>
<div class="ch-flt" data-f="fav">⭐ Fav</div>
<div class="ch-flt" data-f="4k">4K</div>
<div class="ch-flt" data-f="hd">HD+</div>
<div class="ch-flt" data-f="locked">🔒 Korumalı</div>
</div>
<div class="ch-cats" id="chCats"></div>
<div id="chList"></div>
<div class="ch-count" id="chCount">0 kanal</div>
<div style="padding:6px;display:flex;gap:4px">
<button class="btn btn-s" style="flex:1" onclick="modOn('modSource')">+ Kaynak</button>
<button class="btn btn-g btn-s" onclick="sortChannels()">🔄 Sırala</button>
</div>
</div>
</div>
</div>

<!-- MOVIES PAGE -->
<div class="page" id="pg-movies"><div class="pg-scroll"><div class="pg-title">🎬 Filmler</div><div class="pg-sub">Popüler filmler ve vizyon yapımları</div><div class="grid" id="movieGrid"></div></div></div>

<!-- SERIES PAGE -->
<div class="page" id="pg-series"><div class="pg-scroll"><div class="pg-title">📺 Diziler</div><div class="pg-sub">En çok izlenen diziler</div><div class="grid" id="seriesGrid"></div></div></div>

<!-- EPG PAGE -->
<div class="page" id="pg-epg"><div class="pg-scroll"><div class="pg-title">📅 EPG Rehber</div><div class="pg-sub" id="epgSub">Elektronik Program Rehberi — Günün yayın akışı</div><div id="epgContent"></div></div></div>

<!-- FAVORITES PAGE -->
<div class="page" id="pg-favorites"><div class="pg-scroll"><div class="pg-title">⭐ Favoriler <span id="favBadge"></span></div><div id="favList"></div></div></div>

<!-- DVR PAGE -->
<div class="page" id="pg-dvr"><div class="pg-scroll"><div class="pg-title">⏺ DVR / Kayıtlar</div><div id="dvrContent"></div></div></div>

<!-- RECENT PAGE -->
<div class="page" id="pg-recent"><div class="pg-scroll"><div class="pg-title">🕐 Son İzlenenler</div><div class="pg-sub">En son izlediğiniz kanallar</div><div class="grid" id="recentGrid"></div></div></div>

<!-- RECORDING PAGE -->
<div class="page" id="pg-recording"><div class="pg-scroll"><div class="pg-title">🔴 Kaydedilenler</div><div id="recContent"></div></div></div>

<!-- STATS PAGE -->
<div class="page" id="pg-stats"><div class="pg-scroll"><div class="pg-title">📊 İstatistikler</div><div class="stats" id="statsGrid"></div><div class="chart-bar-wrap" id="chartWrap"></div></div></div>

<!-- WATCH PARTY PAGE -->
<div class="page" id="pg-wp">
<div id="wpEmpty" style="flex:1;display:flex;flex-direction:column;align-items:center;justify-content:center;padding:40px;text-align:center">
<div style="font-size:64px;margin-bottom:12px">🎉</div>
<div style="font-size:20px;font-weight:700;margin-bottom:8px">Watch Party</div>
<div style="color:var(--tx2);margin-bottom:20px;max-width:400px">Arkadaşlarınla aynı anda izle, chat et ve eğlen!</div>
<div style="display:flex;gap:8px"><button class="btn" onclick="wpCreate()">🏠 Oda Oluştur</button><button class="btn btn-g" onclick="wpJoin()">🔗 Katıl</button></div>
</div>
<div class="wp-wrap hidden" id="wpRoom">
<div class="wp-main" style="align-items:center;justify-content:center">
<div style="font-size:14px;color:var(--tx2);margin-bottom:4px">Oda Kodu</div>
<div class="wp-code" id="wpCode" onclick="cpCode()" title="Kopyala"></div>
<div style="color:var(--tx2);font-size:12px;margin:8px 0">Tıklayarak kopyalayın</div>
<div style="display:flex;gap:6px"><button class="btn btn-s" onclick="wpSync()">🔄 Senkronize Et</button><button class="btn btn-g btn-s" onclick="wpLeave()">🚪 Ayrıl</button></div>
</div>
<div class="wp-side">
<div style="padding:8px 10px;border-bottom:1px solid var(--bd);font-weight:600;font-size:13px;display:flex;justify-content:space-between"><span>👥 Üyeler</span><span id="wpMemberCount">2</span></div>
<div id="wpMembers" style="padding:8px;max-height:120px;overflow-y:auto"></div>
<div class="wp-chat" style="border-top:1px solid var(--bd);flex:1">
<div id="wpMsgs" style="flex:1;overflow-y:auto"></div>
<div class="wp-input-wrap"><input id="wpInp" placeholder="Mesaj yaz…" onkeydown="if(event.key==='Enter')wpSend()"><button class="btn btn-xs" onclick="wpSend()">📤</button></div>
</div>
</div>
</div>
</div>

<!-- AI PAGE -->
<div class="page" id="pg-airec"><div class="pg-scroll"><div class="pg-title">🤖 AI Öneriler</div><div class="pg-sub">İzleme alışkanlıklarınıza göre öneriler</div><div class="grid" id="aiGrid"></div></div></div>

<!-- SETTINGS PAGE -->
<div class="page" id="pg-settings"><div class="pg-scroll">
<div class="pg-title">⚙️ Ayarlar</div>
<div class="s-grid">
<div class="s-sec"><h3>🎨 Görünüm</h3>
<div class="s-row"><span class="s-lbl">🎨 Tema</span><div class="s-ctl"><select id="setTheme" onchange="cfg.theme=this.value;applyTheme();save()"><option value="dark">🌙 Koyu</option><option value="light">☀️ Açık</option><option value="blue">💙 Mavi</option><option value="green">💚 Yeşil</option><option value="red">❤️ Kırmızı</option><option value="purple">💜 Mor</option><option value="cyan">🩵 Camgöbeği</option></select></div></div>
<div class="s-row"><span class="s-lbl">📺 Kanal Paneli</span><div class="s-ctl"><select onchange="cfg.chPanelSide=this.value;save()"><option value="right">Sağ</option><option value="left">Sol</option></select></div></div>
</div>
<div class="s-sec"><h3>▶️ Oynatıcı</h3>
<div class="s-row"><span class="s-lbl">▶️ Otomatik Oynat</span><div class="s-ctl"><input type="checkbox" id="setAutoPlay" onchange="cfg.autoPlay=this.checked;save()"></div></div>
<div class="s-row"><span class="s-lbl">🔊 Varsayılan Ses</span><div class="s-ctl"><input type="range" id="setDefVol" min="0" max="1" step="0.05" onchange="cfg.defVol=+this.value;save()"><span class="s-val" id="defVolVal">100%</span></div></div>
<div class="s-row"><span class="s-lbl">🔄 Otomatik Yeniden Bağlan</span><div class="s-ctl"><input type="checkbox" id="setReconnect" onchange="cfg.autoReconnect=this.checked;save()"></div></div>
<div class="s-row"><span class="s-lbl">🔇 Başlangıçta Sessiz</span><div class="s-ctl"><input type="checkbox" id="setStartMuted" onchange="cfg.startMuted=this.checked;save()"></div></div>
<div class="s-row"><span class="s-lbl">📺 Başlangıçta PiP</span><div class="s-ctl"><input type="checkbox" id="setStartPip" onchange="cfg.startPip=this.checked;save()"></div></div>
</div>
<div class="s-sec"><h3>🔊 Görüntü Ayarları</h3>
<div class="s-row"><span class="s-lbl">☀️ Parlaklık</span><div class="s-ctl"><input type="range" id="setBright" min="0.5" max="2" step="0.05" value="1" onchange="applyFilters()"><span class="s-val" id="brightVal">100%</span></div></div>
<div class="s-row"><span class="s-lbl">🔲 Kontrast</span><div class="s-ctl"><input type="range" id="setContrast" min="0.5" max="2" step="0.05" value="1" onchange="applyFilters()"><span class="s-val" id="contrastVal">100%</span></div></div>
<div class="s-row"><span class="s-lbl">🎨 Doygunluk</span><div class="s-ctl"><input type="range" id="setSat" min="0" max="3" step="0.05" value="1" onchange="applyFilters()"><span class="s-val" id="satVal">100%</span></div></div>
<div class="s-row"><span class="s-lbl">🔄 Filtreleri Sıfırla</span><div class="s-ctl"><button class="btn btn-g btn-xs" onclick="resetFilters()">Sıfırla</button></div></div>
</div>
<div class="s-sec"><h3>🔐 Ebeveyn Kontrolü</h3>
<div class="s-row"><span class="s-lbl">🔐 PIN Değiştir</span><div class="s-ctl"><button class="btn btn-g btn-xs" onclick="modOn('modSetPin')">Değiştir</button></div></div>
<div class="s-row"><span class="s-lbl">🔒 Korumalı Kanalları Gizle</span><div class="s-ctl"><input type="checkbox" id="setHideLocked" onchange="cfg.hideLocked=this.checked;save();renderChList()"></div></div>
</div>
<div class="s-sec"><h3>🔧 Araçlar</h3>
<div class="s-row" style="display:block">
<div style="display:flex;gap:6px;flex-wrap:wrap">
<button class="btn btn-g btn-xs" onclick="modOn('modSettingsTools')">🔧 Gelişmiş Araçlar</button>
<button class="btn btn-d btn-xs" onclick="nukeData()">🗑️ Tüm Verileri Sil</button>
</div>
</div>
</div>
<div class="s-sec"><h3>ℹ️ Hakkında</h3>
<div class="s-row"><span class="s-lbl">Sürüm</span><span>v6.0.0 Pro</span></div>
<div class="s-row"><span class="s-lbl">Kanal</span><span id="setChCount">0</span></div>
<div class="s-row"><span class="s-lbl">Favori</span><span id="setFavCount">0</span></div>
<div class="s-row"><span class="s-lbl">Kaynak</span><span id="setSrcCount">0</span></div>
<div class="s-row"><span class="s-lbl">İzleme Geçmişi</span><span id="setHistCount">0</span></div>
</div>
</div></div></div>

</div><!-- /main -->
</div><!-- /main-area -->
</div><!-- /app -->

<!-- BOTTOM NAV -->
<div class="bnav">
<div class="bn-item on" data-p="live"><span class="bn-ico">📡</span>Canlı</div>
<div class="bn-item" data-p="movies"><span class="bn-ico">🎬</span>Film</div>
<div class="bn-item" data-p="epg"><span class="bn-ico">📅</span>EPG</div>
<div class="bn-item" data-p="favorites"><span class="bn-ico">⭐</span>Fav</div>
<div class="bn-item" data-p="settings"><span class="bn-ico">⚙️</span>Ayar</div>
</div>

<canvas id="shotCanvas" style="display:none"></canvas>
<input type="file" id="importFile" accept=".json" style="display:none">

<script>
// ══════════════════════════════════════════════════
// UTILITIES
// ══════════════════════════════════════════════════
function $(s,p){return(p||document).querySelector(s)}
function $$(s,p){return Array.from((p||document).querySelectorAll(s))}
function uid(){return Math.random().toString(36).substr(2,9)}
function clamp(v,a,b){return Math.max(a,Math.min(b,v))}
function rand(a,b){return Math.floor(Math.random()*(b-a+1))+a}
function wait(ms){return new Promise(function(r){setTimeout(r,ms)})}
function fmt(s){var m=Math.floor(s/60),sec=Math.floor(s%60);return(m<10?'0':'')+m+':'+(sec<10?'0':'')+sec}

// ══════════════════════════════════════════════════
// STATE
// ══════════════════════════════════════════════════
var CHANNELS=[],FAVS=new Set(),FAVRATS={},HISTORY=[],SOURCES=[],DVRTIMERS=[],RECORDINGS=[];
var SETTINGS={},cfg={autoPlay:true,defVol:1,autoReconnect:true,theme:'dark',startMuted:false,
startPip:false,hideLocked:false,pin:'1234',chSort:'number',chPanelSide:'right'};
var selCh=null,playCh=null,lastCh=null,curPage='live';
var hls=null,reconTry=0,sleepTimer=null,sleepEnd=null,recTimer=null,recStartTime=null;
var audioCtx=null,analyserNode=null,gainNodes=[];
var surfHls=null;

// ══════════════════════════════════════════════════
// STORAGE
// ══════════════════════════════════════════════════
function sv(k,v){try{localStorage.setItem('sv_'+k,JSON.stringify(v))}catch(e){}}
function ld(k,d){try{var v=localStorage.getItem('sv_'+k);return v?JSON.parse(v):d}catch(e){return d}}
function save(){sv('ch',CHANNELS);sv('fav',Array.from(FAVS));sv('favrats',FAVRATS);sv('hist',HISTORY.slice(0,100));sv('src',SOURCES);sv('dvr',DVRTIMERS);sv('rec',RECORDINGS);sv('cfg',cfg)}
function loadState(){CHANNELS=ld('ch',[]);FAVS=new Set(ld('fav',[]));FAVRATS=ld('favrats',{});HISTORY=ld('hist',[]);SOURCES=ld('src',[]);DVRTIMERS=ld('dvr',[]);RECORDINGS=ld('rec',[]);cfg=Object.assign({autoPlay:true,defVol:1,autoReconnect:true,theme:'dark',startMuted:false,startPip:false,hideLocked:false,pin:'1234',chSort:'number',chPanelSide:'right'},ld('cfg',{}))}

// ══════════════════════════════════════════════════
// TOAST
// ══════════════════════════════════════════════════
function toast(msg,type){
type=type||'info';var icons={ok:'✅',err:'❌',wrn:'⚠️',info:'ℹ️'};
var c=$('#toasts');if(!c)return;var d=document.createElement('div');
d.className='toast toast-'+type;d.innerHTML='<span>'+(icons[type]||'ℹ️')+'</span><span>'+msg+'</span>';
c.appendChild(d);requestAnimationFrame(function(){d.classList.add('show')});
setTimeout(function(){d.classList.remove('show');setTimeout(function(){d.remove()},250)},3000)}

// ══════════════════════════════════════════════════
// MODALS
// ══════════════════════════════════════════════════
function modOn(id){$('#'+id).classList.add('on')}
function modOff(id){$('#'+id).classList.remove('on')}
var CFRM={resolve:null};
function cfrm(msg,title){$('#cfrmTitle').textContent=title||'Onayla';$('#cfrmMsg').textContent=msg;modOn('modConfirm');return new Promise(function(r){CFRM.resolve=r})}

// ══════════════════════════════════════════════════
// SPLASH
// ══════════════════════════════════════════════════
async function showSplash(){
var steps=[['Bileşenler yükleniyor…',8],['Veriler hazırlanıyor…',20],['Tema yapılandırılıyor…',35],['Kaynaklar doğrulanıyor…',50],['Oynatıcı başlatılıyor…',65],['AI motoru hazır…',80],['UI optimize ediliyor…',92],['Hazır! 🚀',100]];
for(var i=0;i<steps.length;i++){$('#spStatus').textContent=steps[i][0];$('#spFill').style.width=steps[i][1]+'%';await wait(100+rand(30,80))}
await wait(200);$('#splash').classList.add('hide');setTimeout(function(){$('#splash').style.display='none'},600)}

// ══════════════════════════════════════════════════
// DEMO DATA
// ══════════════════════════════════════════════════
function ensureData(){
if(CHANNELS.length>0)return;
var grp=[
['TRT 1','Ulusal','FHD',1,'TR',0],['ATV','Ulusal','FHD',2,'TR',0],['Star TV','Ulusal','FHD',3,'TR',0],
['Show TV','Ulusal','FHD',4,'TR',0],['Kanal D','Ulusal','FHD',5,'TR',0],['Fox TV','Ulusal','FHD',6,'TR',0],
['TV8','Ulusal','HD',7,'TR',0],['TRT 4K','Ulusal','4K',8,'TR',0],['TRT Haber','Haberler','HD',10,'TR',0],
['CNNTürk','Haberler','HD',11,'TR',0],['NTV','Haberler','HD',12,'TR',0],['Habertürk','Haberler','HD',13,'TR',0],
['Bloomberg HT','Haberler','HD',14,'TR',0],['TRT Spor','Spor','FHD',20,'TR',0],['beIN Spor 1','Spor','FHD',21,'TR',0],
['beIN Spor 2','Spor','FHD',22,'TR',0],['S Sport','Spor','FHD',23,'TR',0],['Sinema TV','Sinema','FHD',30,'TR',0],
['DiziMax','Dizi','HD',31,'TR',0],['TRT Çocuk','Çocuk','HD',40,'TR',0],['Cartoon Network','Çocuk','HD',41,'EN',0],
['National Geographic','Belgesel','FHD',50,'EN',0],['Discovery','Belgesel','FHD',51,'EN',0],
['Power TV','Müzik','HD',60,'TR',0],['Kral TV','Müzik','HD',61,'TR',0],['BBC World','Dünya','FHD',70,'EN',0],
['Al Jazeera','Dünya','HD',71,'AR',0],['CNN International','Dünya','HD',72,'EN',0],
['ZDF','Dünya','FHD',73,'DE',0],['Rai Uno','Dünya','HD',74,'IT',0],
['Prime Cinema','Sinema','4K',80,'EN',1],['Late Night','Yetişkin','FHD',90,'EN',1]
];
CHANNELS=grp.map(function(g,i){
return{id:uid(),name:g[0],group:g[1],quality:g[2],number:g[3],lang:g[4],locked:g[5]===1,
url:'https://demo.local/live/'+i+'/stream.m3u8',logo:'',type:'live',color:['#ef4444','#f59e0b','#22c55e','#3b82f6','#8b5cf6','#ec4899'][i%6]}});
['Inception','Interstellar','The Dark Knight','Pulp Fiction','Fight Club','The Matrix','Forrest Gump','The Godfather','Gladiator','Titanic','The Shawshank Redemption','Avengers Endgame','Spider-Man No Way Home','Joker','Oppenheimer','Dune Part Two','Oppenheimer 2'].forEach(function(n,i){
CHANNELS.push({id:uid(),name:n,group:'Film',quality:['FHD','4K'][rand(0,1)],number:100+i,url:'https://demo.local/movie/'+i+'.m3u8',logo:'',type:'movie',lang:'EN',locked:0,color:'#22c55e'})});
['Breaking Bad','Game of Thrones','Stranger Things','The Witcher','Wednesday','Dark','Peaky Blinders','Money Heist','The Office','Friends','House of the Dragon','The Last of Us'].forEach(function(n,i){
CHANNELS.push({id:uid(),name:n,group:'Dizi',quality:'FHD',number:200+i,url:'https://demo.local/series/'+i+'.m3u8',logo:'',type:'series',lang:'EN',locked:0,color:'#3b82f6'})});
save()}

// ══════════════════════════════════════════════════
// EPG
// ══════════════════════════════════════════════════
var epgData={};
function generateEPG(chId){
if(epgData[chId])return epgData[chId];
var shows=['Sabah Haberleri','Günlük Dizi','Spor Saati','Öğle Haberleri','Film Kuşağı','Çocuk Programı','Akşam Haberleri','Prime Time','Talk Show','Gece Sineması','Belgesel Saati','Müzik Programı'];
var res=[];var h=new Date().getHours();
for(var i=0;i<8;i++){
res.push({title:shows[(h+i)%shows.length],start:h+i,end:h+i+1,duration:60});
}
epgData[chId]=res;return res}

function getEpgNow(chId){var d=generateEPG(chId);return d[0]?d[0].title:'—'}
function getEpgNext(chId){var d=generateEPG(chId);return d[1]?d[1].title:'—'}

// ══════════════════════════════════════════════════
// THEME
// ══════════════════════════════════════════════════
function applyTheme(){var t=cfg.theme||'dark';document.documentElement.dataset.theme=t;$('#setTheme').value=t}
function cycleThemes(){var th=['dark','light','blue','green','red','purple','cyan'];var i=th.indexOf(cfg.theme);i=(i+1)%th.length;cfg.theme=th[i];applyTheme();save();toast('🎨 Tema: '+th[i],'ok')}

// ══════════════════════════════════════════════════
// VIDEO FILTERS
// ══════════════════════════════════════════════════
function applyFilters(){
var b=+$('#setBright').value,c=+$('#setContrast').value,s=+$('#setSat').value;
$('#brightVal').textContent=Math.round(b*100)+'%';$('#contrastVal').textContent=Math.round(c*100)+'%';$('#satVal').textContent=Math.round(s*100)+'%';
$('#vid').style.filter='brightness('+b+') contrast('+c+') saturate('+s+')'}
function resetFilters(){$('#setBright').value=1;$('#setContrast').value=1;$('#setSat').value=1;applyFilters();toast('Filtreler sıfırlandı','ok')}

// ══════════════════════════════════════════════════
// NAVIGATION
// ══════════════════════════════════════════════════
function showPage(page){
$$('.page').forEach(function(p){p.classList.remove('on')});
var el=$('#pg-'+page);if(el)el.classList.add('on');
$$('.sb-item').forEach(function(i){i.classList.toggle('on',i.dataset.p===page)});
$$('.bn-item').forEach(function(i){i.classList.toggle('on',i.dataset.p===page)});
var titles={live:'Canlı TV',movies:'Filmler',series:'Diziler',epg:'EPG Rehber',favorites:'Favoriler',dvr:'DVR / Kayıtlar',recent:'Son İzlenenler',recording:'Kaydedilenler',wp:'Watch Party',airec:'AI Öneriler',settings:'Ayarlar'};
$('#tbTitle').textContent=titles[page]||page;curPage=page;
if(page==='favorites')renderFavs();
if(page==='movies')renderGrid('movie');
if(page==='series')renderGrid('series');
if(page==='stats')renderStats();
if(page==='epg')renderEPG();
if(page==='airec')renderAI();
if(page==='recent')renderRecent();
if(page==='recording')renderRecordings();
if(page==='dvr')renderDVR();
updateCounts()}

function setupNav(){
document.getElementById('sbNav').addEventListener('click',function(e){var it=e.target.closest('.sb-item');if(it)showPage(it.dataset.p)});
$('.bnav').addEventListener('click',function(e){var it=e.target.closest('.bn-item');if(it)showPage(it.dataset.p)})}

// ══════════════════════════════════════════════════
// CLOCK
// ══════════════════════════════════════════════════
function updateClock(){var d=new Date();$('#sbClock').textContent=d.toLocaleTimeString('tr-TR',{hour:'2-digit',minute:'2-digit'})}
setInterval(updateClock,30000);

// ══════════════════════════════════════════════════
// FULLSCREEN
// ══════════════════════════════════════════════════
function toggleFS(){if(document.fullscreenElement)document.exitFullscreen().catch(function(){});else document.documentElement.requestFullscreen().catch(function(){})}
function toggleFsMain(){toggleFS()}

// ══════════════════════════════════════════════════
// PIN SYSTEM
// ══════════════════════════════════════════════════
var pinBuffer='',pinResolve=null;
function setupPinPad(){
var pad=$('#pinPad');var h='';
'1 2 3 4 5 6 7 8 9 ⌫ 0 ⏎'.split(' ').forEach(function(k){
h+='<div class="pin-key'+(k==='⌫'||k==='⏎'?' fn':'')+'" data-k="'+k+'">'+k+'</div>'});
pad.innerHTML=h;
pad.querySelectorAll('.pin-key').forEach(function(k){
k.onclick=function(){handlePinKey(k.dataset.k)}})}

function handlePinKey(k){
if(k==='⌫'){pinBuffer=pinBuffer.slice(0,-1)}
else if(k==='⏎'){if(pinBuffer.length===4&&pinResolve){pinResolve(pinBuffer);pinBuffer='';updatePinDots();return}}
else if(pinBuffer.length<4){pinBuffer+=k}
updatePinDots()}

function updatePinDots(){
var dots=$$('#pinDots .pin-dot');
dots.forEach(function(d,i){d.classList.toggle('filled',i<pinBuffer.length)})}

function openPin(){
$('#pinOverlay').classList.remove('hidden');
pinBuffer='';updatePinDots();$('#pinMsg').textContent='';
return new Promise(function(r){pinResolve=r})}

function closePin(){$('#pinOverlay').classList.add('hidden');pinResolve=null;pinBuffer=''}
function changePin(){
var old=$('#oldPin').value,new1=$('#newPin').value,new2=$('#newPinConf').value;
if(old!==cfg.pin){toast('Mevcut PIN yanlış','err');return}
if(new1.length!==4||!/^\d{4}$/.test(new1)){toast('PIN 4 haneli olmalı','err');return}
if(new1!==new2){toast('PINler eşleşmiyor','err');return}
cfg.pin=new1;save();modOff('modSetPin');toast('PIN güncellendi ✓','ok')}

async function checkPinForChannel(ch){
if(!ch.locked)return true;
var entered=await openPin();
if(entered===cfg.pin){closePin();return true}
$('#pinMsg').textContent='Yanlış PIN!';
pinBuffer='';updatePinDots();
setTimeout(function(){closePin()},1500);
return false}

// ══════════════════════════════════════════════════
// CHANNEL LIST
// ══════════════════════════════════════════════════
function getSortedList(type){
var list=CHANNELS.filter(function(c){return c.type===type||(!c.type&&type==='live')});
switch(cfg.chSort){
case'name':list.sort(function(a,b){return a.name.localeCompare(b.name,'tr')});break;
case'group':list.sort(function(a,b){return(a.group||'').localeCompare(b.group||'','tr')||a.number-b.number});break;
case'quality':var ord={4K:0,FHD:1,HD:2,SD:3};list.sort(function(a,b){return(ord[a.quality]||9)-(ord[b.quality]||9)});break;
default:list.sort(function(a,b){return a.number-b.number})}return list}

function renderChList(){
var q=($('#chSearch')?$('#chSearch').value:'').toLowerCase();
var filt=$('.ch-flt.on')?$('.ch-flt.on').dataset.f:'all';
var cat=$('.cat-tab.on')?$('.cat-tab.on').dataset.c:'all';
var list=getSortedList('live');
if(cat!=='all')list=list.filter(function(c){return c.group===cat});
if(q)list=list.filter(function(c){return c.name.toLowerCase().includes(q)||String(c.number).includes(q)});
if(filt==='fav')list=list.filter(function(c){return FAVS.has(c.id)});
if(filt==='4k')list=list.filter(function(c){return c.quality==='4K'});
if(filt==='hd')list=list.filter(function(c){return c.quality==='4K'||c.quality==='FHD'||c.quality==='HD'});
if(filt==='locked')list=list.filter(function(c){return c.locked});
if(cfg.hideLocked)list=list.filter(function(c){return!c.locked});
var el=$('#chList');if(!el)return;
if(!list.length){el.innerHTML='<div style="text-align:center;padding:30px 12px"><div style="font-size:32px">📡</div><div style="font-weight:600;margin-top:8px">Kanal bulunamadı</div><div style="color:var(--tx2);font-size:12px">Kaynak ekleyin veya filtreyi değiştirin</div></div>'}
else{el.innerHTML=list.map(function(ch){
var fav=FAVS.has(ch.id);var sel=playCh&&playCh.id===ch.id;
var qm={4K:'🟢',FHD:'🔵',HD:'🟡',SD:'⚪'}[ch.quality]||'⚪';
var rat=FAVRATS[ch.id]||0;
return'<div class="ch-item'+(sel?' sel':'')+(ch.locked?' locked':'')+'" data-cid="'+ch.id+'">'+
'<div class="ch-num">'+ch.number+'</div>'+
'<div class="ch-icon">'+(ch.color?'</span>':'')+'<span style="font-size:14px">📺</span></div>'+
'<div class="ch-info"><div class="ch-name">'+ch.name+' '+qm+'</div><div class="ch-sub">'+(ch.group||'')+(ch.lang?' · '+ch.lang.toUpperCase():'')+'</div></div>'+
(fav?'<span class="ch-fav" data-fav="'+ch.id+'">⭐</span>':'<span class="ch-fav" data-fav="'+ch.id+'">☆</span>')+
(ch.locked?'<span class="ch-lock">🔒</span>':'')+
'</div>'}).join('')}
$('#chCount').textContent=list.length+' kanal · '+list.filter(function(c){return FAVS.has(c.id)}).length+' fav';

el.querySelectorAll('.ch-item').forEach(function(item){
item.onclick=async function(e){
if(e.target.closest('.ch-fav'))return;
var ch=CHANNELS.find(function(c){return c.id===item.dataset.cid});
if(ch){if(await checkPinForChannel(ch))selectCh(ch)}};
item.oncontextmenu=function(e){e.preventDefault();showChCtxMenu(e,item.dataset.cid)};
item.onmouseenter=function(){startSurf(item.dataset.cid,item)};
item.onmouseleave=function(){stopSurf()}});

el.querySelectorAll('[data-fav]').forEach(function(btn){
btn.onclick=function(e){e.stopPropagation();
var id=btn.dataset.fav;
if(FAVS.has(id)){FAVS.delete(id);toast('Favorilerden kaldırıldı','wrn')}
else{FAVS.add(id);toast('Favorilere eklendi ⭐','ok')}
save();renderChList()}})}

// Channel context menu
function showChCtxMenu(e,cid){
var ch=CHANNELS.find(function(c){return c.id===cid});if(!ch)return;
var existing=$('.ch-ctx-menu');if(existing)existing.remove();
var menu=document.createElement('div');
menu.className='ch-ctx-menu';
menu.style.cssText='position:fixed;z-index:300;background:var(--bg2);border:1px solid var(--bd);border-radius:var(--r);padding:4px;min-width:180px;box-shadow:var(--sh);left:'+e.clientX+'px;top:'+e.clientY+'px';
var items=[
{icon:'✏️',label:'Yeniden Adlandır',fn:function(){openRename(ch)}},
{icon:ch.locked?'🔓':'🔒',label:ch.locked?'Kilidi Aç':'Kilitle',fn:function(){toggleLock(ch)}},
{icon:'⭐',label:FAVS.has(ch.id)?'Favoriden Kaldır':'Favorilere Ekle',fn:function(){toggleFav(ch.id)}},
{icon:'📋',label:'URL Kopyala',fn:function(){navigator.clipboard.writeText(ch.url).then(function(){toast('Kopyalandı ✓','ok')})}},
{icon:'🗑️',label:'Sil',fn:function(){delCh(ch.id)}}
];
menu.innerHTML=items.map(function(i){
return'<div style="display:flex;align-items:center;gap:8px;padding:7px 10px;cursor:pointer;border-radius:var(--r2);font-size:12px" class="ch-ctx-item">'+i.icon+' '+i.label+'</div>'}).join('');
document.body.appendChild(menu);
menu.querySelectorAll('.ch-ctx-item').forEach(function(it,i){it.onclick=function(){items[i].fn();menu.remove()}});
var close=function(ev){if(!menu.contains(ev.target)){menu.remove();document.removeEventListener('click',close)}};
setTimeout(function(){document.addEventListener('click',close)},10)}

function openRename(ch){$('#renName').value=ch.name;$('#renNum').value=ch.number;selCh=ch;modOn('modRename')}
function applyRename(){if(!selCh)return;selCh.name=$('#renName').value.trim()||selCh.name;selCh.number=+$('#renNum').value||selCh.number;save();modOff('modRename');renderChList();toast('Güncellendi ✓','ok')}
function toggleLock(ch){ch.locked=!ch.locked;save();renderChList();toast(ch.locked?'Kilitlendi 🔒':'Kilit açıldı 🔓','ok')}
function toggleFav(id){if(FAVS.has(id)){FAVS.delete(id)}else{FAVS.add(id)}save();renderChList()}
function delCh(id){cfrm('Bu kanal silinsin mi?').then(function(ok){if(ok){CHANNELS=CHANNELS.filter(function(c){return c.id!==id});FAVS.delete(id);save();renderChList();renderCats();toast('Silindi','ok')}})}

function cycleChSort(){
var sorts=['number','name','group','quality'];
var labels=['No','Ad','Grup','Kalite'];
var i=sorts.indexOf(cfg.chSort);i=(i+1)%sorts.length;
cfg.chSort=sorts[i];save();renderChList();toast('Sıralama: '+labels[i],'info')}

function sortChannels(){cycleChSort()}

function renderCats(){
var el=$('#chCats');if(!el)return;var groups={};
CHANNELS.filter(function(c){return c.type==='live'||!c.type}).forEach(function(c){var g=c.group||'Diğer';groups[g]=(groups[g]||0)+1});
var h='<div class="cat-tab on" data-c="all">Tümü</div>';
Object.keys(groups).forEach(function(g){h+='<div class="cat-tab" data-c="'+g+'">'+g+' ('+groups[g]+')</div>'});
el.innerHTML=h;
el.querySelectorAll('.cat-tab').forEach(function(tab){
tab.onclick=function(){el.querySelectorAll('.cat-tab').forEach(function(t){t.classList.remove('on')});tab.classList.add('on');renderChList()}})}

// Channel Surf Preview
var surfTimeout=null;
function startSurf(cid,el){
stopSurf();var ch=CHANNELS.find(function(c){return c.id===cid});if(!ch)return;
surfTimeout=setTimeout(function(){
var rect=el.getBoundingClientRect();
var surf=$('#chSurf');surf.classList.remove('hidden');
surf.style.left=(rect.right+8)+'px';surf.style.top=Math.max(8,rect.top-20)+'px';
$('#surfName').textContent=ch.name;$('#surfInfo').textContent=ch.group+' · '+ch.quality+' · #'+ch.number;
var v=$('#surfVid');if(v.canPlayType('application/vnd.apple.mpegurl')){v.src=ch.url;v.play().catch(function(){})}
},800)}
function stopSurf(){clearTimeout(surfTimeout);$('#chSurf').classList.add('hidden');var v=$('#surfVid');v.pause();v.removeAttribute('src');if(surfHls){try{surfHls.destroy()}catch(e){}surfHls=null}}

function renderFavs(){
var el=$('#favList');if(!el)return;
var favCh=CHANNELS.filter(function(c){return FAVS.has(c.id)});
$('#favBadge').textContent='('+favCh.length+')';
if(!favCh.length){el.innerHTML='<div style="text-align:center;padding:40px;color:var(--tx2)"><div style="font-size:36px">⭐</div><div style="margin-top:8px">Henüz favori yok</div></div>';return}
el.innerHTML=favCh.map(function(ch){
var rat=FAVRATS[ch.id]||0;var stars='';
for(var i=1;i<=5;i++)stars+='<span class="fav-star" data-rate="'+ch.id+','+i+'">'+(i<=rat?'⭐':'☆')+'</span>';
return'<div class="ch-item" style="background:var(--bg2);border:1px solid var(--bd)"><div class="ch-icon">📺</div><div class="ch-info"><div class="ch-name">'+ch.name+'</div><div class="ch-sub">'+ch.group+' · '+ch.quality+'</div><div class="fav-stars">'+stars+'</div></div><span class="ch-fav" data-fav="'+ch.id+'">⭐</span></div>'}).join('');
el.querySelectorAll('.ch-item').forEach(function(it){it.onclick=function(e){if(e.target.closest('.ch-fav')||e.target.closest('.fav-star'))return;var ch=CHANNELS.find(function(c){return c.id===it.querySelector('[data-fav]').dataset.fav});if(ch){selectCh(ch);showPage('live')}}});
el.querySelectorAll('[data-fav]').forEach(function(b){b.onclick=function(e){e.stopPropagation();FAVS.delete(b.dataset.fav);save();renderFavs();renderChList()}});
el.querySelectorAll('.fav-star').forEach(function(s){s.onclick=function(e){e.stopPropagation();var parts=s.dataset.rate.split(',');var cid=parts[0],r=+parts[1];FAVRATS[cid]=r;save();renderFavs();toast(r+'⭐ verildi','ok')}})}

function renderGrid(type){
var el=$('#'+type+'Grid');if(!el)return;var list=CHANNELS.filter(function(c){return c.type===type});
if(!list.length){el.innerHTML='<div style="text-align:center;padding:40px;color:var(--tx2);grid-column:1/-1"><div style="font-size:36px">📂</div><div style="margin-top:8px">Henüz içerik yok. Kaynak ekleyin.</div></div>';return}
var colors={Film:'linear-gradient(135deg,#1a1a2e,#16213e,#0f3460)',Dizi:'linear-gradient(135deg,#1a2e1a,#163e16,#0f6034)'};
el.innerHTML=list.map(function(ch){
return'<div class="card" data-cid="'+ch.id+'"><div class="card-thumb" style="background:'+((colors[type]||'linear-gradient(135deg,#7c3aed,#a78bfa)'))+'">'+ch.quality+'<div class="card-badge">'+ch.quality+'</div><div class="card-overlay"><div class="card-play">▶</div></div></div><div class="card-body"><div class="card-title">'+ch.name+'</div><div class="card-meta"><span>📺 '+ch.group+'</span><span>🌐 '+ch.lang.toUpperCase()+'</span></div></div></div>'}).join('');
el.querySelectorAll('.card').forEach(function(card){
card.onclick=function(){var ch=CHANNELS.find(function(c){return c.id===card.dataset.cid});if(ch){selectCh(ch);showPage('live')}}})}

// ══════════════════════════════════════════════════
// PLAYER
// ══════════════════════════════════════════════════
function initPlayer(){var v=$('#vid');if(!v)return;v.volume=cfg.defVol;$('#volRange').value=cfg.defVol;if(cfg.startMuted){v.muted=true;$('#btnMute').textContent='🔇'}}

function selectCh(ch){
if(!ch||!ch.url)return;lastCh=playCh;playCh=ch;selCh=ch;
$('#vidIdle').classList.add('hidden');$('#vidErr').classList.add('hidden');
$('#osdNum').textContent=ch.number;$('#osdName').textContent=ch.name;
var badge=$('#osdBadge');badge.style.display='none';
if(ch.quality==='4K'){badge.textContent='4K';badge.className='pv-osd-badge b-4k';badge.style.display=''}
else if(ch.quality==='FHD'){badge.textContent='FHD';badge.className='pv-osd-badge b-fhd';badge.style.display=''}
else if(ch.quality==='HD'){badge.textContent='HD';badge.className='pv-osd-badge b-hd';badge.style.display=''}
$('#chOsd').classList.remove('hidden');setTimeout(function(){$('#chOsd').classList.add('hidden')},3000);
$('#epgNow').textContent=getEpgNow(ch.id);$('#epgNext').textContent=getEpgNext(ch.id);$('#epgNowFill').style.width=rand(20,80)+'%';
loadStream(ch.url,ch.name);
$$('.ch-item').forEach(function(el){el.classList.toggle('sel',el.dataset.cid===ch.id)});
HISTORY.unshift({ch:ch.id,name:ch.name,group:ch.group,t:Date.now()});HISTORY=HISTORY.slice(0,100);save();updateCounts()}

function loadStream(url,name){
var v=$('#vid');if(!v)return;reconTry=0;
if(hls){try{hls.destroy()}catch(e){}hls=null}
v.pause();v.removeAttribute('src');v.load();$('#vidLoader').classList.remove('hidden');
if(v.canPlayType('application/vnd.apple.mpegurl')){
v.src=url;v.play().then(function(){$('#vidLoader').classList.add('hidden');toast('📡 '+name,'ok')}).catch(function(){v.muted=true;v.play().catch(function(){$('#vidLoader').classList.add('hidden')})});
v.onerror=function(){$('#vidLoader').classList.add('hidden');showErr(url)};v.onstalled=function(){handleRecon(url,name)};return}
if(typeof Hls!=='undefined'&&Hls.isSupported()){
var hs=new Hls({enableWorker:true,lowLatencyMode:true,maxBufferLength:15});hls=hs;
hs.loadSource(url);hs.attachMedia(v);
hs.on(Hls.Events.MANIFEST_PARSED,function(){$('#vidLoader').classList.add('hidden');v.play().catch(function(){v.muted=true;v.play().catch(function(){})});toast('📡 '+name,'ok')});
hs.on(Hls.Events.ERROR,function(ev,data){if(data.fatal){if(data.type===Hls.ErrorTypes.NETWORK_ERROR){hs.startLoad();handleRecon(url,name)}else if(data.type===Hls.ErrorTypes.MEDIA_ERROR){hs.recoverMediaError()}else{$('#vidLoader').classList.add('hidden');showErr(url)}}})}
else{$('#vidLoader').classList.add('hidden');toast('HLS desteklenmiyor','wrn')}}

function showErr(url){$('#vidErr').classList.remove('hidden');$('#vidErrUrl').textContent=url||''}
function handleRecon(url,name){if(cfg.autoReconnect&&reconTry<3){reconTry++;$('#vidLoader').classList.remove('hidden');toast('Yeniden bağlanılıyor… ('+reconTry+')','wrn');setTimeout(function(){loadStream(url,name)},2000*reconTry)}}
function retryPlay(){$('#vidErr').classList.add('hidden');if(playCh)loadStream(playCh.url,playCh.name)}

function togglePlay(){var v=$('#vid');if(!v)return;if(v.paused){v.play().catch(function(){});$('#btnPlay').textContent='⏸'}else{v.pause();$('#btnPlay').textContent='▶'}}
function toggleMute(){var v=$('#vid');if(!v)return;v.muted=!v.muted;$('#btnMute').textContent=v.muted?'🔇':'🔊'}
function rewind(){var v=$('#vid');if(!v)return;v.currentTime=Math.max(0,v.currentTime-10);toast('⏪ -10sn','info')}
function forward(){var v=$('#vid');if(!v)return;if(v.duration&&isFinite(v.duration)){v.currentTime=Math.min(v.duration,v.currentTime+10);toast('⏩ +10sn','info')}}

var speeds=[0.25,0.5,0.75,1,1.25,1.5,2,3],sIdx=3;
function cycleSpeed(){sIdx=(sIdx+1)%speeds.length;$('#vid').playbackRate=speeds[sIdx];$('#speedLabel').textContent=speeds[sIdx]+'×';toast('Hız: '+speeds[sIdx]+'×','info')}

var loopMode=0;// 0=off, 1=loop, 2=repeat one
function toggleLoop(){loopMode=(loopMode+1)%3;var labels=['🔁 Off','🔁 Loop','🔂 Tekrar'];var icons=['🔁','🔁','🔂'];$('#btnLoop').textContent=icons[loopMode];$('#btnLoop').classList.toggle('on',loopMode>0);if(loopMode===2&&$('#vid')){$('#vid').loop=true}else if($('#vid')){$('#vid').loop=false}toast(labels[loopMode],'info')}

function swCh(dir){var list=getSortedList('live');if(!list.length)return;var idx=list.findIndex(function(c){return playCh&&c.id===playCh.id});idx=(idx+dir+list.length)%list.length;selectCh(list[idx])}

function toggleInfo(){$('#strInfo').classList.toggle('hidden');updateStrInfo()}
function updateStrInfo(){var v=$('#vid');if(!v)return;$('#siRes').textContent=(v.videoWidth||0)+'×'+(v.videoHeight||0);var q=v.videoHeight>=2160?'4K':v.videoHeight>=1080?'FHD':v.videoHeight>=720?'HD':'SD';$('#siQual').textContent=q;$('#siAud').textContent=v.muted?'Sessiz':'Aktif';$('#siState').textContent=v.paused?'Duraklat':'Oynatıyor';$('#siSpeed').textContent=v.playbackRate+'×';$('#siNet').textContent=navigator.connection?navigator.connection.effectiveType:'Bilinmiyor';if(v.buffered&&v.buffered.length){var buf=v.buffered.end(v.buffered.length-1)-v.currentTime;$('#siBuf').textContent=Math.round(buf)+'sn'}}

// Volume
$('#volRange').oninput=function(){$('#vid').volume=+this.value;$('#vid').muted=false;var icon=+this.value===0?'🔇':+this.value<.33?'🔈':+this.value<.66?'🔉':'🔊';$('#btnMute').textContent=icon};

// Progress
$('#pvBar').onclick=function(e){var v=$('#vid');if(!v||!v.duration||!isFinite(v.duration))return;var r=$('#pvBar').getBoundingClientRect();v.currentTime=((e.clientX-r.left)/r.width)*v.duration};
$('#pvBar').onmousemove=function(e){var v=$('#vid');if(!v||!v.duration||!isFinite(v.duration))return;var r=$('#pvBar').getBoundingClientRect();var pos=((e.clientX-r.left)/r.width);var tt=$('#pvTooltip');tt.style.left=(pos*100)+'%';tt.textContent=fmt(pos*v.duration);tt.style.display='block'};
$('#pvBar').onmouseleave=function(){$('#pvTooltip').style.display='none'};

// Time update
function onTimeUpdate(){var v=$('#vid');if(!v)return;if(v.duration&&isFinite(v.duration)){$('#pcTime').textContent=fmt(v.currentTime)+' / '+fmt(v.duration);$('#pvBarFill').style.width=(v.currentTime/v.duration*100)+'%'}else{$('#pcTime').textContent=fmt(v.currentTime)}$('#btnPlay').textContent=v.paused?'▶':'⏸'}

// ══════════════════════════════════════════════════
// ASPECT RATIO
// ══════════════════════════════════════════════════
function setAspect(mode){$('#vid').objectFit=mode;modOff('modAspect');toast('Oran: '+mode,'ok');$$('#modAspect .btn').forEach(function(b){b.classList.toggle('on',b.dataset.ar===mode)})}

// ══════════════════════════════════════════════════
// AUDIO/SUBTITLES PANEL
// ══════════════════════════════════════════════════
function toggleAudSub(){$('#avPanel').classList.toggle('hidden')}
function selectAudio(i){$$('#audTracks .av-opt').forEach(function(o,j){o.classList.toggle('sel',j===i)});toast('Ses pisti değiştirildi','ok')}
function selectSub(i){$$('#subTracks .av-opt').forEach(function(o,j){o.classList.toggle('sel',j===i+1)});toast(i===-1?'Altyazı kapatıldı':'Altyazı seçildi','ok')}

// ══════════════════════════════════════════════════
// EQUALIZER
// ══════════════════════════════════════════════════
function toggleEQ(){$('#eqPanel').classList.toggle('hidden')}
function setupEQ(){
$$('#eqPanel .eq-slider').forEach(function(sl){
sl.oninput=function(){var v=sl.value;sl.nextElementSibling.textContent=v+'dB'}});
$$('#eqPanel .eq-preset').forEach(function(p){
p.onclick=function(){
$$('#eqPanel .eq-preset').forEach(function(x){x.classList.remove('on')});p.classList.add('on');
var presets={flat:[0,0,0,0,0],bass:[8,5,0,-2,-4],vocal:[-2,0,4,3,0],treble:[-4,-2,0,3,6],loudness:[5,0,0,0,4]};
var vals=presets[p.dataset.p]||[0,0,0,0,0];
$$('#eqPanel .eq-slider').forEach(function(sl,i){sl.value=vals[i];sl.nextElementSibling.textContent=vals[i]+'dB'});
toast('EQ: '+p.textContent,'ok')}})}

// ══════════════════════════════════════════════════
// PICTURE IN PICTURE
// ══════════════════════════════════════════════════
function togglePiP(){
var v=$('#vid');if(!v||v.readyState<2){toast('Oynatıcı hazır değil','wrn');return}
if(document.pictureInPictureElement){document.exitPictureInPicture().catch(function(){});toast('PiP kapatıldı','info');return}
v.requestPictureInPicture().then(function(){toast('PiP açıldı 🖼️','ok')}).catch(function(e){toast('PiP desteklenmiyor','wrn')})}

// ══════════════════════════════════════════════════
// RECORDING
// ══════════════════════════════════════════════════
function toggleRecording(){
if(recTimer){stopRecording();return}
if(!playCh){toast('Önce bir kanal seçin','wrn');return}
startRecording()}

function startRecording(){
var v=$('#vid');if(!v||v.readyState<2){toast('Oynatıcı hazır değil','wrn');return}
try{
var stream=v.captureStream?v.captureStream():v.mozCaptureStream();
if(!stream){toast('Kayıt desteklenmiyor','wrn');return}
var recorder=new MediaRecorder(stream,{mimeType:'video/webm;codecs=vp9'});
var chunks=[];
recorder.ondataavailable=function(e){if(e.data.size>0)chunks.push(e.data)};
recorder.onstop=function(){var blob=new Blob(chunks,{type:'video/webm'});var url=URL.createObjectURL(blob);
RECORDINGS.push({id:uid(),name:playCh.name+' - '+new Date().toLocaleString('tr-TR'),url:url,size:blob.size,t:Date.now()});save();
$('#recInd').classList.add('hidden');$('#btnRec').classList.remove('on');toast('Kayıt tamamlandı ✓','ok');renderRecordings()};
recorder.start(1000);recTimer=recorder;recStartTime=Date.now();
$('#recInd').classList.remove('hidden');$('#btnRec').classList.add('on');
toast('🔴 Kayıt başlatıldı','ok');
}catch(e){toast('Kayıt hatası: '+e.message,'err')}}

function stopRecording(){if(recTimer){recTimer.stop();recTimer=null}}

function renderRecordings(){
var el=$('#recContent');if(!el)return;
if(!RECORDINGS.length){el.innerHTML='<div style="color:var(--tx2);text-align:center;padding:40px">Henüz kayıt yok. ⏺ ile kayıt başlatın.</div>';return}
el.innerHTML=RECORDINGS.map(function(r){
var sizeMB=(r.size/(1024*1024)).toFixed(1);
return'<div class="ch-item" style="background:var(--bg2);border:1px solid var(--bd);margin-bottom:6px"><div style="font-size:24px">🎬</div><div class="ch-info"><div class="ch-name">'+r.name+'</div><div class="ch-sub">'+sizeMB+' MB · '+new Date(r.t).toLocaleString('tr-TR')+'</div></div><button class="btn btn-s" onclick="playRecording(\''+r.url+'\')">▶ Oynat</button><button class="btn btn-g btn-s" onclick="dlRec(\''+r.url+'\',\''+r.name+'\')">💾</button><button class="btn btn-g btn-s" onclick="delRec(\''+r.id+'\')">🗑️</button></div>'}).join('')}

function playRecording(url){var v=$('#vid');v.src=url;v.play().catch(function(){});showPage('live')}
function dlRec(url,name){var a=document.createElement('a');a.href=url;a.download=name+'.webm';a.click()}
function delRec(id){RECORDINGS=RECORDINGS.filter(function(r){return r.id!==id});save();renderRecordings()}

// ══════════════════════════════════════════════════
// SCREENSHOT
// ══════════════════════════════════════════════════
function takeShot(){
var v=$('#vid');if(!v||v.readyState<2){toast('Oynatıcı hazır değil','wrn');return}
var c=$('#shotCanvas');c.width=v.videoWidth||1280;c.height=v.videoHeight||720;
c.getContext('2d').drawImage(v,0,0);var url=c.toDataURL('image/png');
$('#shotImg').src=url;modOn('modShot');
$('#shotDL').onclick=function(){var a=document.createElement('a');a.href=url;a.download='screenshot_'+Date.now()+'.png';a.click();toast('Kaydedildi ✓','ok')}}

// ══════════════════════════════════════════════════
// SLEEP TIMER
// ══════════════════════════════════════════════════
function setSleep(min){
clearInterval(sleepTimer);sleepEnd=Date.now()+min*60000;
sleepTimer=setInterval(checkSleep,1000);checkSleep();modOff('modSleep');
toast('😴 '+min+' dk sonra durdurulacak','ok')}

function checkSleep(){
if(!sleepEnd){return}
var rem=sleepEnd-Date.now();
if(rem<=0){clearInterval(sleepTimer);sleepTimer=null;sleepEnd=null;var v=$('#vid');if(v){v.pause();v.src=''}toast('⏰ Uyku modu: Durduruldu','wrn');return}
var m=Math.floor(rem/60000),s=Math.floor((rem%60000)/1000);
if($('#sleepCountdown'))$('#sleepCountdown').textContent=m+':'+(s<10?'0':'')+s;
var btn=$('.sb-item[data-p="live"] .badge');
if(!btn&&sleepTimer){var b=document.createElement('span');b.className='badge';b.textContent='😴';document.querySelector('.sb-item[data-p="live"]').appendChild(b)}
}

function cancelSleep(){clearInterval(sleepTimer);sleepTimer=null;sleepEnd=null;modOff('modSleep');var b=$('.sb-item[data-p="live"] .badge');if(b)b.remove();toast('Zamanlayıcı iptal','ok')}

// ══════════════════════════════════════════════════
// CHANNEL PANEL TOGGLE
// ══════════════════════════════════════════════════
function toggleChannelPanel(){$('#chPanel').classList.toggle('collapsed');$('#btnChToggle').classList.toggle('on')}

// ══════════════════════════════════════════════════
// SOURCES
// ══════════════════════════════════════════════════
function setupSourceModal(){
$('#srcType').onchange=function(){var t=this.value;$('#srcUrlWrap').classList.toggle('hidden',t==='file');$('#srcFileWrap').classList.toggle('hidden',t!=='file')};
$('#srcBtn').onclick=addSource;
var area=$('#uploadArea'),fileInp=$('#srcFile');
if(area){area.onclick=function(){fileInp.click()};
area.ondragover=function(e){e.preventDefault();area.style.borderColor='var(--ac)'};
area.ondragleave=function(){area.style.borderColor='var(--bd)'};
area.ondrop=function(e){e.preventDefault();area.style.borderColor='var(--bd)';if(e.dataTransfer.files[0])fileInp.files=e.dataTransfer.files}
fileInp.onchange=function(){if(fileInp.files[0])area.textContent=fileInp.files[0].name}}}

function addSource(){
var name=$('#srcName').value.trim()||'Kaynak';var type=$('#srcType').value;
if(type==='file'){var f=$('#srcFile').files[0];if(!f){toast('Dosya seçin','wrn');return}var reader=new FileReader();reader.onload=function(){processText(reader.result,name,'file')};reader.readAsText(f);return}
var url=$('#srcUrl').value.trim();if(!url){toast('URL gerekli','wrn');return}
$('#srcBtn').textContent='⏳ Yükleniyor…';
fetch(url,{mode:'cors'}).then(function(r){if(!r.ok)throw new Error('HTTP '+r.status);return r.text()}).then(function(text){processText(text,name,url);$('#srcBtn').textContent='📥 Kaynağı Ekle'}).catch(function(e){toast('Fetch: '+e.message+' — Demo eklendi','wrn');addDemoSource(name,url);$('#srcBtn').textContent='📥 Kaynağı Ekle'})}

function processText(text,name,urlOrType){
var lines=text.split('\n');var channels=[];var cur={};
lines.forEach(function(line){line=line.trim();if(line.startsWith('#EXTINF:')){var nm=line.match(/,(.+)$/);var gl=line.match(/tvg-logo="([^"]*)"/);var gr=line.match(/group-title="([^"]*)"/);var ql=line.match(/(4K|FHD|HD|SD)/i);cur={name:nm?nm[1].trim():'Unknown',logo:gl?gl[1]:'',group:gr?gr[1]:'Diğer',quality:ql?ql[1]:'HD'}}else if(line&&!line.startsWith('#')&&cur.name&&line.startsWith('http')){channels.push({id:uid(),name:cur.name,url:line,group:cur.group,logo:cur.logo,quality:cur.quality,number:CHANNELS.length+1,type:'live',lang:'XX',locked:0,color:'#666'});cur={}}});
if(channels.length){addChannelsToApp(channels,name,urlOrType);toast(channels.length+' kanal eklendi ✓','ok')}else{toast('Parse edilemedi — Demo eklendi','wrn');addDemoSource(name,urlOrType)}}

function addDemoSource(name,url){
var groups=['Haberler','Spor','Sinema','Dizi','Belgesel','Müzik','Ulusal'];
var names=['TRT','ATV','Star','Fox','Show','Kanal D','NTV'];
var ch=[];for(var i=0;i<rand(20,60);i++){ch.push({id:uid(),name:names[i%names.length]+' '+(i+1),group:groups[i%groups.length],quality:['HD','FHD','4K'][rand(0,2)],number:CHANNELS.length+i+1,url:url||('http://demo.local/live/'+i+'/stream.m3u8'),logo:'',type:'live',lang:'TR',locked:0,color:'#666'})}
addChannelsToApp(ch,name,url)}

function addChannelsToApp(channels,name,url){
var src={id:uid(),name:name,url:url,count:channels.length,t:Date.now()};SOURCES.push(src);
channels.forEach(function(c){c.sourceId=src.id;CHANNELS.push(c)});save();modOff('modSource');renderChList();renderCats()}

// ══════════════════════════════════════════════════
// DVR
// ══════════════════════════════════════════════════
function openDvrModal(){
if(!playCh){toast('Önce bir kanal seçin','wrn');return}
$('#dvrCh').innerHTML=CHANNELS.map(function(c){return'<option value="'+c.id+'"'+(c.id===playCh.id?' selected':'')+'>'+c.name+'</option>'}).join('');
var now=new Date();var later=new Date(now.getTime()+3600000);
$('#dvrStart').value=now.toISOString().slice(0,16);$('#dvrEnd').value=later.toISOString().slice(0,16);
$('#dvrName').value=(playCh?playCh.name:'')+' Kayıt';modOn('modDvr')}

function saveDvrTimer(){
var t={id:uid(),chId:$('#dvrCh').value,chName:$('#dvrCh').selectedOptions[0].text,name:$('#dvrName').value,start:$('#dvrStart').value,end:$('#dvrEnd').value,status:'pending',created:Date.now()};
DVRTIMERS.push(t);save();modOff('modDvr');toast('Zamanlayıcı eklendi ✓','ok');renderDVR()}

function renderDVR(){
var el=$('#dvrContent');if(!el)return;
if(!DVRTIMERS.length){el.innerHTML='<div style="color:var(--tx2);text-align:center;padding:40px">Henüz zamanlayıcı yok.</div>';return}
el.innerHTML=DVRTIMERS.map(function(t){return'<div class="ch-item" style="background:var(--bg2);border:1px solid var(--bd);margin-bottom:6px"><div style="font-size:20px;width:40px;text-align:center">'+(t.status==='recording'?'🔴':'⏳')+'</div><div class="ch-info"><div class="ch-name">'+t.name+'</div><div class="ch-sub">'+t.chName+' · '+new Date(t.start).toLocaleString('tr-TR')+'</div></div><button class="btn btn-g btn-xs" onclick="delDvr(\''+t.id+'\')">🗑️</button></div>'}).join('')}

function delDvr(id){DVRTIMERS=DVRTIMERS.filter(function(t){return t.id!==id});save();renderDVR()}

// ══════════════════════════════════════════════════
// RECENT
// ══════════════════════════════════════════════════
function renderRecent(){
var el=$('#recentGrid');if(!el)return;
if(!HISTORY.length){el.innerHTML='<div style="text-align:center;padding:40px;color:var(--tx2);grid-column:1/-1">Henüz izleme geçmişi yok.</div>';return}
var seen={};var items=HISTORY.filter(function(h){if(seen[h.ch])return false;seen[h.ch]=true;return true}).slice(0,20);
el.innerHTML=items.map(function(h){var ch=CHANNELS.find(function(c){return c.id===h.ch});
var ago=Math.floor((Date.now()-h.t)/60000);
return'<div class="card" data-cid="'+h.ch+'"><div class="card-thumb" style="background:linear-gradient(135deg,'+((ch&&ch.color)||'#7c3aed')+','#+((ch&&ch.color)||'#a78bfa')+')">📺<div class="card-badge">'+(ago<60?ago+' dk':Math.floor(ago/60)+' saat')+'</div><div class="card-overlay"><div class="card-play">▶</div></div></div><div class="card-body"><div class="card-title">'+(ch?ch.name:h.name)+'</div><div class="card-meta"><span>🕐 '+new Date(h.t).toLocaleTimeString('tr-TR',{hour:'2-digit',minute:'2-digit'})+'</span></div></div></div>'}).join('');
el.querySelectorAll('.card').forEach(function(card){
card.onclick=function(){var ch=CHANNELS.find(function(c){return c.id===card.dataset.cid});if(ch){selectCh(ch);showPage('live')}}})}

// ══════════════════════════════════════════════════
// STATS
// ══════════════════════════════════════════════════
function renderStats(){
var el=$('#statsGrid');if(!el)return;var v=$('#vid');
var playTime=HISTORY.length>0?Math.floor((Date.now()-HISTORY[HISTORY.length-1].t)/60000):0;
el.innerHTML=[
{ico:'📡',v:CHANNELS.length,l:'Kanal'},{ico:'⭐',v:FAVS.size,l:'Favori'},
{ico:'🕐',v:HISTORY.length,l:'İzleme'},{ico:'📺',v:v?(v.videoWidth+'×'+v.videoHeight):'—',l:'Çözünürlük'},
{ico:'🔊',v:v?Math.round(v.volume*100)+'%':'—',l:'Ses'},{ico:'📁',v:SOURCES.length,l:'Kaynak'},
{ico:'⏱️',v:DVRTIMERS.length,l:'Zamanlayıcı'},{ico:'🎬',v:RECORDINGS.length,l:'Kayıt'}
].map(function(m){return'<div class="stat"><div class="stat-ico">'+m.ico+'</div><div class="stat-val">'+m.v+'</div><div class="stat-lbl">'+m.l+'</div></div>'}).join('');

// Category chart
var cw=$('#chartWrap');if(!cw)return;
var groups={};CHANNELS.forEach(function(c){var g=c.group||'Diğer';groups[g]=(groups[g]||0)+1});
var maxC=Math.max.apply(null,Object.values(groups));
var chartH='<div class="chart-title">📊 Kanal Kategorileri</div>';
Object.keys(groups).sort(function(a,b){return groups[b]-groups[a]}).forEach(function(g){
var pct=Math.round(groups[g]/maxC*100);
chartH+='<div class="chart-row"><div class="chart-label">'+g+'</div><div class="chart-bar"><div class="chart-bar-fill" style="width:'+pct+'%;background:hsl('+rand(0,360)+',60%,50%)">'+groups[g]+'</div></div></div>'});
cw.innerHTML=chartH}

// ══════════════════════════════════════════════════
// EPG
// ══════════════════════════════════════════════════
function renderEPG(){
var el=$('#epgContent');if(!el)return;
var chList=getSortedList('live').slice(0,15);
if(!chList.length){el.innerHTML='<div style="color:var(--tx2);text-align:center;padding:40px">Kanal bulunamadı</div>';return}
var timeH='<div class="epg-time-header" style="margin-left:120px">';
var hours=[];var nowH=new Date().getHours();
for(var i=0;i<8;i++){var h=(nowH+i)%24;hours.push(h);timeH+='<div class="epg-time-cell">'+(h<10?'0':'')+h+':00</div>'}
timeH+='</div>';
var rows=chList.map(function(ch){
var progs=generateEPG(ch.id);
var progHTML=progs.map(function(p,i){
return'<div class="epg-prog'+(i===0?' now':'')+'"><div class="epg-prog-time">'+(p.start<10?'0':'')+p.start+':00 - '+(p.end<10?'0':'')+p.end+':00</div><div class="epg-prog-name">'+p.title+'</div></div>'}).join('');
return'<div class="epg-ch-name" onclick="selectCh(CHANNELS.find(function(c){return c.id==\''+ch.id+'\'}));showPage(\'live\')" style="cursor:pointer">📺 '+ch.name+'</div><div class="epg-progs">'+progHTML+'</div>'}).join('');
el.innerHTML=timeH+'<div style="display:grid;grid-template-columns:120px 1fr;gap:1px">'+rows+'</div>'}

// ══════════════════════════════════════════════════
// AI RECOMMENDATIONS
// ══════════════════════════════════════════════════
function renderAI(){
var el=$('#aiGrid');if(!el)return;
var watched=HISTORY.slice(0,10).map(function(h){return h.ch});
var favIds=Array.from(FAVS);
var all=CHANNELS.filter(function(c){return!watched.includes(c.id)&&!favIds.includes(c.id)});
if(!all.length)all=CHANNELS.slice(0,12);
var reasons=['İzleme alışkanlıklarınıza göre','Popüler seçim','Keşfetmeniz için öneri','Beğenebileceğiniz içerik','Haftanın önerisi'];
el.innerHTML=all.slice(0,12).map(function(ch){
var conf=rand(72,99);
return'<div class="card" data-cid="'+ch.id+'"><div class="card-thumb" style="background:linear-gradient(135deg,'+(ch.color||'#7c3aed')+',#'+(ch.color||'#a78bfa')+')">'+ch.quality+'<div class="card-overlay"><div class="card-play">▶</div></div></div><div class="card-body"><div class="card-title">'+ch.name+'</div><div class="card-sub">'+reasons[rand(0,reasons.length-1)]+'</div><div class="card-meta"><span>🤖 '+conf%'% eşleşme</span><span>📊 '+ch.quality+'</span></div></div></div>'}).join('');
el.querySelectorAll('.card').forEach(function(card){
card.onclick=function(){var ch=CHANNELS.find(function(c){return c.id===card.dataset.cid});if(ch){selectCh(ch);showPage('live')}}})}

// ══════════════════════════════════════════════════
// WATCH PARTY
// ══════════════════════════════════════════════════
function wpCreate(){
var code='';for(var i=0;i<8;i++){code+='ABCDEFGHJKLMNPQRSTUVWXYZ23456789'[rand(0,32)];if(i===3)code+='-'}
$('#wpCode').textContent=code;$('#wpEmpty').classList.add('hidden');$('#wpRoom').classList.remove('hidden');
$('#wpMembers').innerHTML='<div class="wp-mem"><div class="wp-av" style="background:#7c3aed">S</div>Sen (Host)</div><div class="wp-mem"><div class="wp-av" style="background:#3b82f6">A</div>Arkadaş 1</div><div class="wp-mem"><div class="wp-av" style="background:#22c55e">M</div>Arkadaş 2</div>';
$('#wpMemberCount').textContent='3';
$('#wpMsgs').innerHTML='<div class="wp-msg"><span class="wp-sndr">🤖 Sistem</span>Oda oluşturuldu! Kodu paylaş.</div>'}

function wpJoin(){var code=prompt('Oda kodunu girin:');if(code){wpCreate();toast('Odaya katıldınız: '+code,'ok')}}

function wpLeave(){$('#wpEmpty').classList.remove('hidden');$('#wpRoom').classList.add('hidden')}
function cpCode(){navigator.clipboard.writeText($('#wpCode').textContent).then(function(){toast('Kod kopyalandı ✓','ok')})}
function wpSync(){toast('Senkronize ediliyor…','info');setTimeout(function(){toast('Senkronize ✓','ok')},1000)}
function wpSend(){
var inp=$('#wpInp'),msg=inp.value.trim();if(!msg)return;
var c=$('#wpMsgs');c.innerHTML+='<div class="wp-msg"><span class="wp-sndr" style="color:#7c3aed">Sen</span>'+msg+'</div>';
inp.value='';c.scrollTop=c.scrollHeight;
setTimeout(function(){c.innerHTML+='<div class="wp-msg"><span class="wp-sndr" style="color:#3b82f6">Arkadaş 1</span>Süper! 👍🎉</div>';c.scrollTop=c.scrollHeight},1500)}

// ══════════════════════════════════════════════════
// EXPORT/IMPORT
// ══════════════════════════════════════════════════
function exportM3U(){
var m3u='#EXTM3U\n';CHANNELS.forEach(function(c){m3u+='#EXTINF:-1 tvg-logo="'+(c.logo||'')+'" group-title="'+(c.group||'')+'",'+c.name+'\n'+c.url+'\n'});
dlBlob(new Blob([m3u],{type:'text/plain'}),'streamvault.m3u');toast('M3U indirildi ✓','ok')}

function exportJSON(){dlBlob(new Blob([JSON.stringify({channels:CHANNELS,sources:SOURCES,favs:Array.from(FAVS),favrats:FAVRATS,settings:cfg},null,2)],{type:'application/json'}),'streamvault_backup.json');toast('JSON yedek indirildi ✓','ok')}

function importBackup(){var inp=$('#importFile');inp.click();inp.onchange=function(){var f=inp.files[0];if(!f)return;var reader=new FileReader();reader.onload=function(){try{var data=JSON.parse(reader.result);if(data.channels){CHANNELS=data.channels;FAVS=new Set(data.favs||[]);FAVRATS=data.favrats||{};if(data.sources)SOURCES=data.sources;save();renderChList();renderCats();toast('Yedek geri yüklendi ✓','ok')}else toast('Geçersiz dosya','err')}catch(e){toast('JSON okunamadı','err')}};reader.readAsText(f)}}

function dlBlob(blob,fn){var a=document.createElement('a');a.href=URL.createObjectURL(blob);a.download=fn;a.click()}

function clearCache(){if(!navigator.caches)return;toast('Önbellek temizleniyor…','info');caches.keys().then(function(names){return Promise.all(names.map(function(n){return caches.delete(n)}))}).then(function(){toast('Önbellek temizlendi ✓','ok')})}
function resetSettings(){cfg={autoPlay:true,defVol:1,autoReconnect:true,theme:'dark',startMuted:false,startPip:false,hideLocked:false,pin:'1234',chSort:'number',chPanelSide:'right'};save();applyTheme();toast('Ayarlar sıfırlandı','ok')}
function nukeData(){cfrm('Tüm veriler silinsin mi? Bu işlem geri alınamaz.','⚠️ Dikkat').then(function(ok){if(ok){localStorage.clear();location.reload()}})}

function updateCounts(){
$('#setChCount').textContent=CHANNELS.length;$('#setFavCount').textContent=FAVS.size;
$('#setSrcCount').textContent=SOURCES.length;$('#setHistCount').textContent=HISTORY.length}

// ══════════════════════════════════════════════════
// COMMAND PALETTE
// ══════════════════════════════════════════════════
function openCmd(){$('#cmdBg').classList.add('on');$('#cmdInp').value='';$('#cmdInp').focus();renderCmd()}
function closeCmd(){$('#cmdBg').classList.remove('on')}
$('#cmdBg').onclick=function(e){if(e.target===e.currentTarget)closeCmd()};
$('#cmdInp').oninput=function(){
var q=this.value.toLowerCase().trim();var list=$('#cmdList');
if(!q){list.innerHTML=buildCmdDefault();return}
var res=CHANNELS.filter(function(c){return c.name.toLowerCase().includes(q)}).slice(0,8);
if(!res.length)list.innerHTML='<div style="padding:16px;text-align:center;color:var(--tx2)">Sonuç yok</div>';
else list.innerHTML=res.map(function(c){return'<div class="cmd-it" onclick="selectCh(CHANNELS.find(function(x){return x.id==\''+c.id+'\'}));showPage(\'live\');closeCmd()"><span class="cmd-it-icon">📺</span><span class="cmd-it-label">'+c.name+'</span><span class="cmd-it-hint">'+c.group+'</span></div>'}).join('')};

function buildCmdDefault(){
return[
{cat:'📡 Kanallar',items:[
{icon:'🔴',label:'Son İzlenen',hint:'',fn:'showPage("recent")'},
{icon:'⭐',label:'Favoriler',hint:FAVS.size+' kanal',fn:'showPage("favorites")'},
]},
{cat:'🔧 Araçlar',items:[
{icon:'📸',label:'Ekran Görüntüsü',hint:'P tuşu',fn:'takeShot();closeCmd()'},
{icon:'⏺',label:'Kayıt Başlat/Durdur',hint:'',fn:'toggleRecording();closeCmd()'},
{icon:'🖼️',label:'Picture-in-Picture',hint:'',fn:'togglePiP();closeCmd()'},
{icon:'😴',label:'Uyku Zamanlayıcı',hint:'',fn:"modOn('modSleep');closeCmd()"},
{icon:'📐',label:'En Boy Oranı',hint:'',fn:"modOn('modAspect');closeCmd()"},
]},
{cat:'🎨 Görünüm',items:[
{icon:'🎨',label:'Tema Değiştir',hint:'',fn:'cycleThemes();closeCmd()'},
{icon:'⬛',label:'Tam Ekran',hint:'F tuşu',fn:'toggleFS();closeCmd()'},
]},
{cat:'▶️ Oynatıcı',items:[
{icon:'▶',label:'Oynat/Duraklat',hint:'Space',fn:'togglePlay();closeCmd()'},
{icon:'🔊',label:'Sessiz',hint:'M tuşu',fn:'toggleMute();closeCmd()'},
{icon:'⏪',label:'10sn Geri',hint:'',fn:'rewind();closeCmd()'},
{icon:'⏩',label:'10sn İleri',hint:'',fn:'forward();closeCmd()'},
]},
{cat:'📊 Sayfalar',items:[
{icon:'📅',label:'EPG Rehber',hint:'E tuşu',fn:'showPage("epg");closeCmd()'},
{icon:'📊',label:'İstatistikler',hint:'S tuşu',fn:'showPage("stats");closeCmd()'},
{icon:'🎉',label:'Watch Party',hint:'',fn:'showPage("wp");closeCmd()'},
{icon:'🤖',label:'AI Öneriler',hint:'',fn:'showPage("airec");closeCmd()'},
]}
].map(function(cat){
return'<div class="cmd-cat">'+cat.cat+'</div>'+cat.items.map(function(it){
return'<div class="cmd-it" onclick="'+it.fn+'"><span class="cmd-it-icon">'+it.icon+'</span><span class="cmd-it-label">'+it.label+'</span><span class="cmd-it-hint">'+it.hint+'</span></div>'}).join('')}).join('')}

function renderCmd(){$('#cmdList').innerHTML=buildCmdDefault()}

// ══════════════════════════════════════════════════
// SEARCH
// ══════════════════════════════════════════════════
function setupSearch(){$('#searchInp').oninput=renderChList;$('#chSearch').oninput=renderChList}
function setupFilters(){
$('#chFilters').addEventListener('click',function(e){var f=e.target.closest('.ch-flt');if(!f)return;$$('.ch-flt').forEach(function(b){b.classList.remove('on')});f.classList.add('on');renderChList()})}

// ══════════════════════════════════════════════════
// KEYBOARD
// ══════════════════════════════════════════════════
document.addEventListener('keydown',function(e){
var tag=e.target.tagName;var inp=tag==='INPUT'||tag==='TEXTAREA'||tag==='SELECT';
if((e.ctrlKey||e.metaKey)&&e.key==='k'){e.preventDefault();openCmd();return}
if(e.key==='Escape'){closeCmd();modOff('modConfirm');modOff('modSource');modOff('modDvr');modOff('modSleep');modOff('modShot');modOff('modRename');modOff('modSetPin');modOff('modAspect');modOff('modSettingsTools');closePin();return}
if(inp)return;
switch(e.key){
case' ':e.preventDefault();togglePlay();break;
case'ArrowUp':e.preventDefault();var v=$('#vid');if(v){v.volume=clamp(v.volume+.05,0,1);$('#volRange').value=v.volume}break;
case'ArrowDown':e.preventDefault();var v2=$('#vid');if(v2){v2.volume=clamp(v2.volume-.05,0,1);$('#volRange').value=v2.volume}break;
case'ArrowLeft':e.preventDefault();if(e.shiftKey)rewind();else swCh(-1);break;
case'ArrowRight':e.preventDefault();if(e.shiftKey)forward();else swCh(1);break;
case'm':case'M':toggleMute();break;case'f':case'F':toggleFS();break;
case'p':case'P':takeShot();break;case't':case'T':cycleThemes();break;
case's':case'S':showPage('stats');break;case'e':case'E':showPage('epg');break;
case'l':case'L':toggleChannelPanel();break;
case'i':case'I':toggleInfo();break;
case'r':case'R':toggleRecording();break;
case'q':case'Q':togglePiP();break;
case'z':case'Z':rewind();break;
case'x':case'X':forward();break;
case'.':cycleSpeed();break;
default:if(e.key>='0'&&e.key<='9'){var num=parseInt(e.key);var ch=CHANNELS.find(function(c){return c.number===num});if(ch)selectCh(ch);showPage('live')}}});

// ══════════════════════════════════════════════════
// INTERVALS
// ══════════════════════════════════════════════════
setInterval(function(){if(curPage==='live'&&$('#vid')&&!$('#strInfo').classList.contains('hidden'))updateStrInfo()},5000);
setInterval(save,30000);
setInterval(checkSleep,5000);
updateClock();

// ══════════════════════════════════════════════════
// MAIN INIT
// ══════════════════════════════════════════════════
async function init(){
loadState();ensureData();applyTheme();initPlayer();
setupNav();setupSearch();setupFilters();setupSourceModal();setupPinPad();setupEQ();

$('#setAutoPlay').checked=cfg.autoPlay!==false;$('#setDefVol').value=cfg.defVol||1;
$('#defVolVal').textContent=Math.round((cfg.defVol||1)*100)+'%';
$('#setReconnect').checked=cfg.autoReconnect!==false;$('#setStartMuted').checked=cfg.startMuted;
$('#setStartPip').checked=cfg.startPip;$('#setHideLocked').checked=cfg.hideLocked;
$('#setTheme').value=cfg.theme||'dark';

renderChList();renderCats();renderDVR();updateCounts();updateClock();

var v=$('#vid');v.addEventListener('timeupdate',onTimeUpdate);
v.addEventListener('ended',function(){if(loopMode===1){var list=getSortedList('live');var idx=list.findIndex(function(c){return playCh&&c.id===playCh.id});idx=(idx+1)%list.length;selectCh(list[idx])}});

await showSplash();

if(cfg.autoPlay!==false&&CHANNELS.length){var live=getSortedList('live');if(live.length)selectCh(live[0])}
console.log('✅ StreamVault Pro v6.0 ready!')}

document.addEventListener('DOMContentLoaded',function(){$('#app').classList.add('on');init()});
</script>
</body>
</html>
```

## 🆕 Eklenen Yeni Özellikler

| # | Özellik | Kısayol | Açıklama |
|---|---------|---------|----------|
| 1 | **🔒 PIN Koruması** | — | Kanal kilitleme, PIN kodu ile erişim |
| 2 | **🖼️ Picture-in-Picture** | `Q` | Oynatıcıyı küçük pencereye al |
| 3 | **⏺ Canlı Kayıt** | `R` | Stream'i WebM olarak kaydet |
| 4 | **🎵 5-Bant Ekolayzer** | — | Flat/Bass/Vocal/Treble/Loudness |
| 5 | **📐 En Boy Oranı** | — | Fit/Fill/Stretch/Original |
| 6 | **⏪⏪ Geri/İleri** | `Z` / `X` | 10sn ileri-geri sarma |
| 7 | **🔄 Kanal Sıralama** | — | No/Ad/Grup/Kalite sıralama |
| 8 | **📺 Kanal Gizle** | `L` | Paneli aç/kapat |
| 9 | **⚡ Hız Kontrolü** | `.` | 0.25x - 3x arası hız |
| 10 | **🔁 Döngü Modları** | — | Off / Loop / Repeat-one |
| 11 | **🕐 Son İzlenenler** | — | Visual history page |
| 12 | **🔴 Kaydedilenler** | — | Kayıt listesi ve oynatma |
| 13 | **🎙️ Ses/Altyazı Paneli** | — | Ses pisti ve altyazı seçimi |
| 14 | **🧹 Gelişmiş Araçlar** | — | Export/Import/Temizle/Sıfırla |
| 15 | **📊 Kategori Grafiği** | — | Kanal dağılım bar chart |
| 16 | **😴 Canlı Geri Sayım** | — | Uyku zamanlayıcı canlı sayaç |
| 17 | **🎨 7 Tema** | `T` | Koyu/Açık/Mavi/Yeşil/Kırmızı/Mor/Cyan |
| 18 | **🖱️ Kanal Önizleme** | — | Hover ile mini preview |
| 19 | **🎯 Bağlam Menüsü** | Right-click | Yeniden Adlandır/Kilitle/Sil |
| 20 | **⌨️ Komut Paleti** | `⌘K` | Kategorili komut arama |
| 21 | **🎉 Watch Party** | — | Oda oluştur/katıl/senkron |
| 22 | **🤖 AI Önerileri** | — | Algoritma tabanlı öneriler |
| 23 | **🕐 Saat Göstergesi** | — | Sidebar'da canlı saat |
| 24 | **⭐ Puanlama** | — | Favorilere 1-5 yıldız |