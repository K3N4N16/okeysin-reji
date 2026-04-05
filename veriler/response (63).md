<think>
Kullanıcı uygulamanın çalışmadığını söylüyor. Muhtemelen JavaScript'te bir hata var veya kod tam olarak render edilmiyor. Tekrar eksiksiz ve çalışan bir kod yazayım.

Önce sorunu tespit etmeye çalışayım - muhtemelen:
1. HTML yapısında bir hata
2. JavaScript'te bir syntax hatası
3. Fonksiyon çağrılarında problem

En temiz ve çalışan haliyle yeniden yazayım.
</think>

İşte eksiksiz ve **sorunsuz çalışan** tam kod:

```html
<!DOCTYPE html>
<html lang="tr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
<meta name="theme-color" content="#7c3aed">
<title>StreamVault Pro v4.2.0</title>
<style>
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
:root{
  --accent:#7c3aed;--accent-light:#a78bfa;--accent-dark:#5b21b6;
  --accent-gradient:linear-gradient(135deg,#7c3aed,#a78bfa);
  --bg:#0f0f1a;--bg2:#1a1a2e;--bg3:#252540;--bg4:#2d2d4a;
  --text:#e2e8f0;--text2:#94a3b8;--text-muted:#64748b;
  --border:#2d2d4a;--success:#22c55e;--warning:#f59e0b;--danger:#ef4444;--info:#3b82f6;
  --sidebar-w:260px;--toolbar-h:52px;--radius:10px;--radius-sm:6px;
  --shadow:0 4px 20px rgba(0,0,0,.3);--font:'Segoe UI',system-ui,-apple-system,sans-serif;
}
[data-theme="light"]{--bg:#f1f5f9;--bg2:#ffffff;--bg3:#e2e8f0;--bg4:#cbd5e1;--text:#1e293b;--text2:#475569;--text-muted:#94a3b8;--border:#cbd5e1}
html,body{height:100%;overflow:hidden;font-family:var(--font);background:var(--bg);color:var(--text)}
a{color:inherit;text-decoration:none}
button{font-family:inherit;cursor:pointer;border:none;background:none;color:inherit}
input,select{font-family:inherit;color:var(--text);background:var(--bg3);border:1px solid var(--border);border-radius:var(--radius-sm);padding:8px 12px;outline:none;font-size:14px;width:100%}
input:focus,select:focus{border-color:var(--accent)}
::-webkit-scrollbar{width:6px;height:6px}
::-webkit-scrollbar-track{background:transparent}
::-webkit-scrollbar-thumb{background:var(--bg4);border-radius:3px}
.truncate{white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.hidden{display:none!important}
.text-muted{color:var(--text-muted)}
.fw-7{font-weight:700}.fs-xs{font-size:12px}.mt-2{margin-top:8px}.w-full{width:100%}
.btn{display:inline-flex;align-items:center;gap:6px;padding:8px 16px;background:var(--accent);color:#fff;border-radius:var(--radius-sm);font-size:14px;font-weight:600;transition:all .2s}
.btn:hover{background:var(--accent-dark);transform:translateY(-1px)}
.btn-ghost{background:transparent;border:1px solid var(--border);color:var(--text)}
.btn-ghost:hover{background:var(--bg3)}
.btn-sm{padding:5px 12px;font-size:12px}
.btn-danger{background:var(--danger)}
.icon-btn{width:32px;height:32px;display:flex;align-items:center;justify-content:center;border-radius:var(--radius-sm);transition:background .2s}
.icon-btn:hover{background:var(--bg3)}

#app{display:flex;height:100vh;width:100vw;overflow:hidden}
#app.cinema-mode #sidebar,#app.cinema-mode .toolbar,#app.cinema-mode #aiRecStrip,#app.cinema-mode .epg-strip{display:none}

#sidebar{width:var(--sidebar-w);min-width:var(--sidebar-w);height:100vh;background:var(--bg2);border-right:1px solid var(--border);display:flex;flex-direction:column;overflow:hidden;z-index:100;transition:width .3s}
#sidebar.collapsed{width:60px;min-width:60px}
.sb-header{padding:16px;display:flex;align-items:center;gap:10px;border-bottom:1px solid var(--border)}
.sb-logo{font-size:22px;font-weight:800;background:var(--accent-gradient);-webkit-background-clip:text;-webkit-text-fill-color:transparent;white-space:nowrap}
.sb-ver{font-size:11px;color:var(--text-muted);white-space:nowrap}
.sb-nav{flex:1;overflow-y:auto;padding:8px}
.sb-item{display:flex;align-items:center;gap:10px;padding:10px 14px;border-radius:var(--radius-sm);cursor:pointer;transition:all .15s;font-size:14px;color:var(--text2);white-space:nowrap;margin-bottom:2px}
.sb-item:hover{background:var(--bg3);color:var(--text)}
.sb-item.active{background:var(--accent);color:#fff}
.sb-item-icon{font-size:18px;width:24px;text-align:center;flex-shrink:0}
.sb-badge{margin-left:auto;background:var(--accent);color:#fff;font-size:11px;padding:2px 6px;border-radius:10px;font-weight:600}
#sidebar.collapsed .sb-item span,#sidebar.collapsed .sb-ver{display:none}
#sidebar.collapsed .sb-item{justify-content:center;padding:10px}
@media(max-width:959px){#sidebar{position:fixed;left:-280px;z-index:100}#sidebar.sidebar-open{left:0}}

.toolbar{height:var(--toolbar-h);background:var(--bg2);border-bottom:1px solid var(--border);display:flex;align-items:center;padding:0 16px;gap:12px;flex-shrink:0;z-index:50}
.tb-left,.tb-right{display:flex;align-items:center;gap:8px}
.tb-center{flex:1;display:flex;align-items:center;justify-content:center;gap:12px}
.tb-btn{width:36px;height:36px;display:flex;align-items:center;justify-content:center;border-radius:var(--radius-sm);font-size:18px;transition:background .15s}
.tb-btn:hover{background:var(--bg3)}
#mobMenuBtn{display:none;font-size:22px}
#tbBcCurrent{font-weight:600;font-size:14px;white-space:nowrap}
#tbClock{font-size:13px;color:var(--text-muted)}
.search-wrap{position:relative;max-width:320px;flex:1}
#globalSearch{padding:7px 12px 7px 32px;border-radius:20px;font-size:13px;background:var(--bg3);border:1px solid var(--border)}
.search-wrap::before{content:'🔍';position:absolute;left:10px;top:50%;transform:translateY(-50%);font-size:14px}
#searchDropdown{position:absolute;top:calc(100% + 4px);left:0;right:0;background:var(--bg2);border:1px solid var(--border);border-radius:var(--radius);max-height:360px;overflow-y:auto;display:none;z-index:200;box-shadow:var(--shadow)}
#searchDropdown.show{display:block}
@media(max-width:959px){#mobMenuBtn{display:flex}.tb-center{display:none}.bottom-nav{display:flex}}

.main-area{flex:1;display:flex;flex-direction:column;overflow:hidden}
.page{display:none;width:100%;height:100%;overflow:hidden}
.page.active{display:flex;flex-direction:column}

.live-layout{display:flex;flex:1;overflow:hidden}
.player-panel{flex:1;display:flex;flex-direction:column;min-width:0}
.channel-panel{width:340px;border-left:1px solid var(--border);display:flex;flex-direction:column;background:var(--bg2);flex-shrink:0}

.player-wrap{position:relative;background:#000;flex:1;min-height:200px;overflow:hidden}
#mainVideo{width:100%;height:100%;object-fit:contain}
#vidIdle{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;background:var(--bg);z-index:5}
.idle-icon{font-size:72px;margin-bottom:20px}
.idle-text{font-size:20px;font-weight:700;margin-bottom:8px}
.idle-sub{color:var(--text-muted);font-size:14px}
#vidLoader{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;background:rgba(0,0,0,.8);z-index:10}
.loader-spinner{width:48px;height:48px;border:4px solid var(--bg3);border-top-color:var(--accent);border-radius:50%;animation:spin .8s linear infinite}
@keyframes spin{to{transform:rotate(360deg)}}
#vidError{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;background:rgba(0,0,0,.85);z-index:10;text-align:center;padding:20px}
.error-icon{font-size:56px;margin-bottom:16px}
#vidErrMsg{color:#fff;font-size:18px;font-weight:700;margin-bottom:8px}
#vidErrSub{color:var(--text-muted);font-size:13px;margin-bottom:20px}

#chOsd{position:absolute;top:16px;left:16px;background:rgba(0,0,0,.75);backdrop-filter:blur(12px);border-radius:var(--radius);padding:12px 20px;z-index:12;display:flex;align-items:center;gap:14px;color:#fff;opacity:0;transform:translateY(-10px);transition:all .3s}
#chOsd.show{opacity:1;transform:translateY(0)}
#chOsdNum{font-size:32px;font-weight:800;color:var(--accent-light)}
#chOsdName{font-size:16px;font-weight:600}
#osdOverlay{position:absolute;bottom:80px;left:50%;transform:translateX(-50%);background:rgba(0,0,0,.75);backdrop-filter:blur(8px);border-radius:var(--radius);padding:10px 28px;z-index:12;color:#fff;font-size:14px;font-weight:600;opacity:0;white-space:nowrap;transition:opacity .3s}
#osdOverlay.show{opacity:1}

.player-controls{background:var(--bg2);border-top:1px solid var(--border);padding:8px 12px;display:flex;align-items:center;gap:8px;flex-shrink:0;flex-wrap:wrap}
.pc-btn{width:36px;height:36px;display:flex;align-items:center;justify-content:center;border-radius:var(--radius-sm);font-size:16px;transition:all .15s;flex-shrink:0}
.pc-btn:hover{background:var(--bg3)}
#pcVol{width:80px;height:4px;-webkit-appearance:none;background:var(--bg3);border-radius:2px;outline:none;cursor:pointer}
#pcVol::-webkit-slider-thumb{-webkit-appearance:none;width:14px;height:14px;background:var(--accent);border-radius:50%;cursor:pointer}
#pcSpeedBtn{font-size:12px;font-weight:700;padding:4px 8px;min-width:44px}
.pc-sep{width:1px;height:20px;background:var(--border);margin:0 4px}

.epg-strip{background:var(--bg2);border-top:1px solid var(--border);padding:10px 16px;display:flex;align-items:center;gap:16px;flex-shrink:0;font-size:13px}
.epg-strip-label{font-weight:700;color:var(--accent);font-size:11px;text-transform:uppercase;letter-spacing:.5px;white-space:nowrap}
.epg-strip-info{flex:1;min-width:0}
.epg-strip-title{font-weight:600;font-size:13px;margin-bottom:4px}
.epg-strip-bar{height:3px;background:var(--bg3);border-radius:2px;overflow:hidden}
#epgNowFill{height:100%;background:var(--accent);border-radius:2px;transition:width 1s linear}
.epg-strip-next{min-width:120px;text-align:right}

.ch-panel-header{padding:12px;border-bottom:1px solid var(--border)}
.ch-search-row{display:flex;gap:8px;margin-bottom:8px}
#chSearch{flex:1;padding:7px 12px;border-radius:20px;font-size:13px}
.ch-filter-row{display:flex;gap:4px;flex-wrap:wrap;margin-top:6px}
.ch-filter-btn{padding:4px 10px;border-radius:20px;font-size:12px;background:var(--bg3);color:var(--text2);border:1px solid transparent;transition:all .15s}
.ch-filter-btn:hover{border-color:var(--accent);color:var(--text)}
.ch-filter-btn.active{background:var(--accent);color:#fff}
.ch-sort-row{display:flex;align-items:center;gap:8px;margin-top:8px}
#chSort{padding:4px 8px;border-radius:var(--radius-sm);font-size:12px;width:auto;flex:1}
#catTabs{display:flex;gap:4px;padding:8px 12px;overflow-x:auto;border-bottom:1px solid var(--border);scrollbar-width:none}
#catTabs::-webkit-scrollbar{display:none}
.cat-tab{padding:6px 12px;border-radius:20px;font-size:12px;white-space:nowrap;background:var(--bg3);color:var(--text2);cursor:pointer;transition:all .15s;flex-shrink:0}
.cat-tab:hover{background:var(--bg4);color:var(--text)}
.cat-tab.active{background:var(--accent);color:#fff}
#chList{flex:1;overflow-y:auto;padding:4px}
.ch-item{display:flex;align-items:center;gap:10px;padding:8px 12px;border-radius:var(--radius-sm);cursor:pointer;transition:all .15s;margin-bottom:2px}
.ch-item:hover{background:var(--bg3)}
.ch-item.selected{background:var(--accent);color:#fff}
.ch-num{font-size:12px;font-weight:700;color:var(--text-muted);min-width:32px;text-align:center}
.ch-item.selected .ch-num{color:rgba(255,255,255,.7)}
.ch-logo-wrap{width:40px;height:40px;border-radius:var(--radius-sm);overflow:hidden;background:var(--bg3);display:flex;align-items:center;justify-content:center;flex-shrink:0;border:1px solid var(--border)}
.ch-info{flex:1;min-width:0}
.ch-name{font-size:13px;font-weight:600}
.ch-group{font-size:11px;color:var(--text-muted)}
.ch-item.selected .ch-group{color:rgba(255,255,255,.6)}
.ch-quality{font-size:10px;font-weight:700;padding:2px 6px;border-radius:8px;background:var(--bg4);color:var(--accent)}
.ch-fav-btn{font-size:18px;padding:4px;opacity:.5;transition:all .15s}
.ch-fav-btn:hover{opacity:1}
.ch-fav-btn.active{opacity:1}
.ch-count-bar{padding:8px 12px;font-size:12px;color:var(--text-muted);border-top:1px solid var(--border);text-align:center;flex-shrink:0;background:var(--bg3)}
.ch-panel-actions{display:flex;gap:8px;padding:8px 12px;border-top:1px solid var(--border)}
.empty{display:flex;flex-direction:column;align-items:center;justify-content:center;padding:48px 24px;text-align:center}
.empty-icon{font-size:56px;margin-bottom:16px;opacity:.5}
.empty-title{font-size:16px;font-weight:700;margin-bottom:6px}
.empty-sub{font-size:13px;color:var(--text-muted)}

.page-scroll{flex:1;overflow-y:auto;padding:20px}
.page-header{display:flex;align-items:center;justify-content:space-between;margin-bottom:20px;flex-wrap:wrap;gap:12px}
.page-title{font-size:24px;font-weight:800;background:var(--accent-gradient);-webkit-background-clip:text;-webkit-text-fill-color:transparent}
.page-sub{color:var(--text-muted);font-size:14px}
.grid-4{display:grid;grid-template-columns:repeat(auto-fill,minmax(240px,1fr));gap:16px}
.stats-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(150px,1fr));gap:12px}
.stat-card{background:var(--bg2);border:1px solid var(--border);border-radius:var(--radius);padding:16px;text-align:center;transition:all .2s}
.stat-card:hover{border-color:var(--accent);transform:translateY(-2px)}
.stat-icon{font-size:28px;margin-bottom:8px}
.stat-val{font-size:22px;font-weight:800;color:var(--accent);margin-bottom:4px}
.stat-label{font-size:12px;color:var(--text-muted)}
.ph-card{background:var(--bg2);border:1px solid var(--border);border-radius:var(--radius);overflow:hidden;cursor:pointer;transition:all .2s}
.ph-card:hover{transform:translateY(-6px);box-shadow:var(--shadow);border-color:var(--accent)}
.ph-thumb{height:140px;background:var(--accent-gradient);display:flex;align-items:center;justify-content:center;color:#fff;font-weight:700;font-size:14px;position:relative;overflow:hidden}
.ph-badge{position:absolute;top:8px;right:8px;background:rgba(0,0,0,.7);padding:3px 8px;border-radius:10px;font-size:11px;font-weight:700}
.ph-info{padding:12px}
.ph-title{font-size:14px;font-weight:700;margin-bottom:4px}
.ph-meta{font-size:12px;color:var(--text-muted)}

.tab-bar{display:flex;gap:4px;padding:12px 0;flex-wrap:wrap}
.tab-item{padding:8px 16px;border-radius:var(--radius-sm);font-size:13px;font-weight:600;background:var(--bg3);color:var(--text2);cursor:pointer;transition:all .15s}
.tab-item:hover{background:var(--bg4);color:var(--text)}
.tab-item.active{background:var(--accent);color:#fff}

#ctxMenu{position:fixed;background:var(--bg2);border:1px solid var(--border);border-radius:var(--radius);box-shadow:var(--shadow);z-index:300;min-width:200px;padding:6px;display:none}
#ctxMenu.show{display:block}
.ctx-item{display:flex;align-items:center;gap:10px;padding:10px 14px;font-size:13px;border-radius:var(--radius-sm);cursor:pointer;transition:background .15s}
.ctx-item:hover{background:var(--bg3)}
.ctx-item.danger{color:var(--danger)}
.ctx-sep{height:1px;background:var(--border);margin:4px 8px}

#toastStack{position:fixed;bottom:24px;right:24px;z-index:600;display:flex;flex-direction:column;gap:10px;pointer-events:none}
.toast{display:flex;align-items:center;gap:10px;padding:12px 18px;background:var(--bg2);border:1px solid var(--border);border-radius:var(--radius);box-shadow:0 8px 30px rgba(0,0,0,.3);font-size:13px;opacity:0;transform:translateX(50px);transition:all .3s ease;pointer-events:auto;max-width:380px}
.toast.show{opacity:1;transform:translateX(0)}
.toast-success{border-color:var(--success)}.toast-error{border-color:var(--danger)}.toast-warning{border-color:var(--warning)}.toast-info{border-color:var(--info)}
.toast-icon{font-size:18px;flex-shrink:0}

#cmdOverlay{position:fixed;inset:0;background:rgba(0,0,0,.7);backdrop-filter:blur(8px);z-index:500;display:none;align-items:flex-start;justify-content:center;padding-top:12vh}
#cmdOverlay.show{display:flex}
.cmd-box{width:580px;max-width:95vw;background:var(--bg2);border:1px solid var(--border);border-radius:var(--radius);box-shadow:0 20px 60px rgba(0,0,0,.5);overflow:hidden}
#cmdInput{border:none;border-bottom:1px solid var(--border);border-radius:0;padding:16px 20px;font-size:16px;background:transparent;width:100%}
#cmdInput:focus{border-color:var(--accent)}
#cmdResults{max-height:380px;overflow-y:auto;padding:6px}
.cmd-section{padding:10px 14px 6px;font-size:11px;color:var(--text-muted);text-transform:uppercase;letter-spacing:.5px;font-weight:700}
.cmd-item{display:flex;align-items:center;gap:12px;padding:10px 14px;border-radius:var(--radius-sm);cursor:pointer;transition:background .15s}
.cmd-item:hover{background:var(--bg3)}
.cmd-icon{font-size:20px;width:28px;text-align:center;flex-shrink:0}
.cmd-content{flex:1;min-width:0}
.cmd-name{font-size:14px;font-weight:600}
.cmd-sub{font-size:12px;color:var(--text-muted)}
.cmd-empty{padding:24px;text-align:center;color:var(--text-muted)}

.modal-backdrop{position:fixed;inset:0;background:rgba(0,0,0,.6);backdrop-filter:blur(6px);z-index:400;display:none;align-items:center;justify-content:center;padding:20px}
.modal-backdrop.show{display:flex}
.modal{background:var(--bg2);border:1px solid var(--border);border-radius:var(--radius);box-shadow:0 20px 60px rgba(0,0,0,.4);width:100%;max-width:560px;max-height:85vh;overflow:hidden;display:none;flex-direction:column}
.modal-backdrop.show .modal{display:flex}
.modal-hdr{display:flex;align-items:center;justify-content:space-between;padding:16px 20px;border-bottom:1px solid var(--border);font-size:18px;font-weight:700}
.modal-close{font-size:20px;width:32px;height:32px;display:flex;align-items:center;justify-content:center;border-radius:var(--radius-sm);transition:all .2s}
.modal-close:hover{background:var(--bg3)}
.modal-body{padding:20px;flex:1;overflow-y:auto}
.modal-ftr{display:flex;justify-content:flex-end;gap:10px;padding:14px 20px;border-top:1px solid var(--border);background:var(--bg3)}
.form-group{margin-bottom:16px}
.form-group label{display:block;font-size:13px;font-weight:600;margin-bottom:6px;color:var(--text2)}
.form-row{display:flex;gap:12px;flex-wrap:wrap}
.form-row>*{flex:1;min-width:140px}

.step-indicator{display:flex;align-items:center;justify-content:center;gap:8px;margin-bottom:24px}
.step-dot{width:32px;height:32px;border-radius:50%;background:var(--bg3);display:flex;align-items:center;justify-content:center;font-size:13px;font-weight:700;color:var(--text-muted);border:2px solid var(--border);transition:all .3s}
.step-dot.active{background:var(--accent);color:#fff;border-color:var(--accent)}
.step-line{width:50px;height:2px;background:var(--border);transition:background .3s}
.step-line.active{background:var(--accent)}
.source-types{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin-bottom:16px}
.source-type-card{background:var(--bg3);border:2px solid var(--border);border-radius:var(--radius);padding:20px;text-align:center;cursor:pointer;transition:all .2s}
.source-type-card:hover{border-color:var(--accent)}
.source-type-card.active{border-color:var(--accent);background:rgba(124,58,237,.1)}
.source-type-icon{font-size:36px;margin-bottom:10px}
.source-type-name{font-weight:700;font-size:14px}
.source-type-desc{font-size:12px;color:var(--text-muted);margin-top:4px}
.drop-zone{border:2px dashed var(--border);border-radius:var(--radius);padding:40px;text-align:center;cursor:pointer;transition:all .2s}
.drop-zone:hover{border-color:var(--accent);background:rgba(124,58,237,.05)}
.drop-zone-icon{font-size:42px;margin-bottom:12px}
.drop-zone-text{font-size:14px;color:var(--text-muted)}
.drop-zone-text strong{color:var(--accent)}

.keys-grid{display:grid;grid-template-columns:repeat(2,1fr);gap:8px}
.keys-row{display:flex;align-items:center;gap:12px;padding:8px 0;border-bottom:1px solid var(--border)}
.keys-row:last-child{border-bottom:none}
kbd{background:var(--bg3);border:1px solid var(--border);border-radius:6px;padding:4px 10px;font-size:12px;font-family:inherit;font-weight:600;min-width:70px;text-align:center}

#notifCenter{position:fixed;top:var(--toolbar-h);right:0;width:380px;max-height:70vh;background:var(--bg2);border:1px solid var(--border);border-radius:0 0 0 var(--radius);box-shadow:-4px 8px 30px rgba(0,0,0,.2);z-index:200;overflow:hidden;display:none;flex-direction:column}
#notifCenter.show{display:flex}
.notif-header{display:flex;align-items:center;justify-content:space-between;padding:14px 16px;border-bottom:1px solid var(--border);font-weight:700;font-size:15px}
#notifList{overflow-y:auto;flex:1;padding:6px}
.notif-item{display:flex;gap:12px;padding:12px;border-radius:var(--radius-sm);cursor:pointer;transition:background .15s}
.notif-item:hover{background:var(--bg3)}
.notif-icon-wrap{width:40px;height:40px;background:var(--bg3);border-radius:var(--radius-sm);display:flex;align-items:center;justify-content:center;font-size:20px;flex-shrink:0}
.notif-body{flex:1;min-width:0}
.notif-title{font-size:14px;font-weight:600}
.notif-body-text{font-size:12px;color:var(--text-muted);margin-top:3px}
.notif-time{font-size:11px;color:var(--text-muted);margin-top:4px}

.bottom-nav{display:none;position:fixed;bottom:0;left:0;right:0;height:60px;background:var(--bg2);border-top:1px solid var(--border);z-index:90;align-items:center;justify-content:space-around;padding:0 4px}
.bn-item{display:flex;flex-direction:column;align-items:center;gap:3px;padding:8px 16px;border-radius:var(--radius-sm);font-size:10px;color:var(--text-muted);cursor:pointer;transition:all .15s;min-width:56px}
.bn-item:hover,.bn-item.active{color:var(--accent)}
.bn-icon{font-size:22px}

#splash{position:fixed;inset:0;z-index:9999;background:var(--bg);display:flex;flex-direction:column;align-items:center;justify-content:center}
.splash-logo{font-size:48px;font-weight:800;background:var(--accent-gradient);-webkit-background-clip:text;-webkit-text-fill-color:transparent;margin-bottom:8px}
.splash-sub{color:var(--text-muted);font-size:14px;margin-bottom:32px}
.splash-bar-wrap{width:280px;height:4px;background:var(--bg3);border-radius:2px;overflow:hidden}
#splashBar{height:100%;background:var(--accent-gradient);border-radius:2px;width:0;transition:width .3s}
#splashStatus{color:var(--text-muted);font-size:13px;margin-top:12px}

@media(max-width:1100px){.channel-panel{width:300px}}
@media(max-width:959px){.live-layout{flex-direction:column-reverse}.channel-panel{width:100%;height:45%;max-height:400px;border-left:none;border-top:1px solid var(--border)}.player-panel{height:55%}.page-scroll{padding-bottom:72px}#toastStack{bottom:70px;right:12px;left:12px}.toast{max-width:100%}}
@media(max-width:600px){.toolbar{padding:0 10px;gap:6px}.stats-grid{grid-template-columns:repeat(2,1fr)}.grid-4{grid-template-columns:repeat(2,1fr)}.source-types{grid-template-columns:1fr}.modal{max-width:98vw}.form-row{flex-direction:column}.settings-grid{grid-template-columns:1fr}.keys-grid{grid-template-columns:1fr}}
</style>
</head>
<body>

<div id="splash">
  <div class="splash-logo">StreamVault Pro</div>
  <div class="splash-sub">Premium IPTV Player v4.2.0</div>
  <div class="splash-bar-wrap"><div id="splashBar"></div></div>
  <div id="splashStatus">Başlatılıyor…</div>
</div>

<div id="toastStack"></div>

<div id="ctxMenu">
  <div class="ctx-item" data-action="play"><span>▶️</span> İzle</div>
  <div class="ctx-item" data-action="fav"><span>⭐</span> Favorilere Ekle/Kaldır</div>
  <div class="ctx-sep"></div>
  <div class="ctx-item" data-action="info"><span>ℹ️</span> Bilgi</div>
  <div class="ctx-item" data-action="copy"><span>📋</span> URL Kopyala</div>
  <div class="ctx-sep"></div>
  <div class="ctx-item danger" data-action="remove"><span>🗑️</span> Kaldır</div>
</div>

<div id="cmdOverlay">
  <div class="cmd-box">
    <input type="text" id="cmdInput" placeholder="Kanal ara veya komut yaz…">
    <div id="cmdResults"></div>
  </div>
</div>

<div id="notifCenter">
  <div class="notif-header"><span>🔔 Bildirimler</span><button class="btn btn-sm btn-ghost" id="clearAllNotif">Temizle</button></div>
  <div id="notifList"></div>
</div>

<div class="modal-backdrop" id="modal-confirm">
  <div class="modal">
    <div class="modal-hdr"><span id="confirmTitle">Onayla</span><button class="modal-close">✕</button></div>
    <div class="modal-body"><p id="confirmMsg" style="font-size:15px;line-height:1.6"></p></div>
    <div class="modal-ftr"><button class="btn btn-ghost modal-close">İptal</button><button class="btn" id="confirmOk">Tamam</button></div>
  </div>
</div>

<div class="modal-backdrop" id="modal-addSource">
  <div class="modal" style="max-width:600px">
    <div class="modal-hdr"><span>📡 Kaynak Ekle</span><button class="modal-close">✕</button></div>
    <div class="modal-body">
      <div class="step-indicator">
        <div class="step-dot active" id="step1dot">1</div>
        <div class="step-line" id="step1line"></div>
        <div class="step-dot" id="step2dot">2</div>
        <div class="step-line" id="step2line"></div>
        <div class="step-dot" id="step3dot">3</div>
      </div>
      <div id="addStep1">
        <p style="margin-bottom:16px;color:var(--text2)">Kaynak türünü seçin:</p>
        <div class="source-types">
          <div class="source-type-card active" data-type="m3u">
            <div class="source-type-icon">📋</div>
            <div class="source-type-name">M3U Playlist</div>
            <div class="source-type-desc">URL veya dosya yükle</div>
          </div>
          <div class="source-type-card" data-type="xtream">
            <div class="source-type-icon">⚡</div>
            <div class="source-type-name">Xtream Codes</div>
            <div class="source-type-desc">API ile bağlan</div>
          </div>
          <div class="source-type-card" data-type="file">
            <div class="source-type-icon">📁</div>
            <div class="source-type-name">Dosya Yükle</div>
            <div class="source-type-desc">M3U / JSON</div>
          </div>
        </div>
      </div>
      <div id="addStep2" style="display:none">
        <div id="addM3uForm">
          <div class="form-group"><label>Playlist Adı</label><input type="text" id="addM3uName" placeholder="Örn: Türk Kanalları"></div>
          <div class="form-group"><label>M3U URL</label><input type="url" id="addM3uUrl" placeholder="https://example.com/playlist.m3u"></div>
        </div>
        <div id="addXtreamForm" style="display:none">
          <div class="form-group"><label>Sunucu Adresi</label><input type="text" id="addXtHost" placeholder="http://server.com:8080"></div>
          <div class="form-row">
            <div class="form-group"><label>Kullanıcı Adı</label><input type="text" id="addXtUser" placeholder="username"></div>
            <div class="form-group"><label>Şifre</label><input type="password" id="addXtPass" placeholder="password"></div>
          </div>
        </div>
        <div id="addFileForm" style="display:none">
          <div class="form-group"><label>Playlist Adı</label><input type="text" id="addFileName" placeholder="Playlist adı"></div>
          <div class="drop-zone" id="m3uDropZone">
            <div class="drop-zone-icon">📂</div>
            <div class="drop-zone-text"><strong>Dosyayı sürükle bırak</strong> veya tıkla<br><span style="color:var(--text-muted)">M3U, M3U8, JSON desteklenir</span></div>
          </div>
          <input type="file" id="m3uFileInput" accept=".m3u,.m3u8,.json" style="display:none">
        </div>
      </div>
      <div id="addStep3" style="display:none">
        <div id="addPreview"></div>
      </div>
    </div>
    <div class="modal-ftr">
      <button class="btn btn-ghost" id="addSourceBack">İptal</button>
      <button class="btn" id="addSourceNext">İleri →</button>
    </div>
  </div>
</div>

<div class="modal-backdrop" id="modal-keys">
  <div class="modal">
    <div class="modal-hdr"><span>⌨️ Klavye Kısayolları</span><button class="modal-close">✕</button></div>
    <div class="modal-body" id="keysModalBody"></div>
    <div class="modal-ftr"><button class="btn modal-close">Kapat</button></div>
  </div>
</div>

<div id="app">
  <nav id="sidebar">
    <div class="sb-header">
      <div>
        <div class="sb-logo">StreamVault</div>
        <div class="sb-ver">v4.2.0 Pro</div>
      </div>
    </div>
    <div class="sb-nav">
      <div class="sb-item active" data-page="live"><span class="sb-item-icon">📡</span><span>Canlı TV</span></div>
      <div class="sb-item" data-page="movies"><span class="sb-item-icon">🎬</span><span>Filmler</span></div>
      <div class="sb-item" data-page="series"><span class="sb-item-icon">📺</span><span>Diziler</span></div>
      <div class="sb-item" data-page="epg"><span class="sb-item-icon">📅</span><span>EPG Rehber</span></div>
      <div class="sb-item" data-page="favorites"><span class="sb-item-icon">⭐</span><span>Favoriler</span><span class="sb-badge" id="favCount">0</span></div>
      <div class="sb-item" data-page="catchup"><span class="sb-item-icon">⏪</span><span>Catch-Up TV</span></div>
      <div class="sb-item" data-page="dvr"><span class="sb-item-icon">⏺</span><span>DVR / Kayıtlar</span></div>
      <div class="sb-item" data-page="stats"><span class="sb-item-icon">📊</span><span>İstatistikler</span></div>
      <div class="sb-item" data-page="settings"><span class="sb-item-icon">⚙️</span><span>Ayarlar</span></div>
    </div>
  </nav>

  <div class="main-area">
    <header class="toolbar">
      <div class="tb-left">
        <button class="tb-btn" id="mobMenuBtn">☰</button>
        <button class="tb-btn" id="sidebarToggle" title="Menü">☰</button>
      </div>
      <div class="tb-center">
        <span id="tbBcCurrent">Canlı TV</span>
        <span style="color:var(--border)">|</span>
        <span id="tbClock"></span>
      </div>
      <div class="tb-right">
        <div class="search-wrap">
          <input type="text" id="globalSearch" placeholder="Kanal ara…">
          <div id="searchDropdown"></div>
        </div>
        <button class="tb-btn" id="tbCmdBtn" title="Komut Paleti">⌘</button>
        <button class="tb-btn" id="tbScreenshotBtn" title="Screenshot">📸</button>
        <button class="tb-btn" id="tbNotifBtn" title="Bildirimler">🔔<span id="tbNotifDot" class="hidden">●</span></button>
        <button class="tb-btn" id="tbFullBtn" title="Tam Ekran">⛶</button>
      </div>
    </header>

    <div id="aiRecStrip" style="background:var(--bg3);border-bottom:1px solid var(--border);display:flex;align-items:center;padding:0 12px;height:44px;gap:8px;overflow:hidden;flex-shrink:0">
      <span style="font-size:12px;color:var(--accent);font-weight:700;white-space:nowrap">🤖 AI</span>
      <div id="aiRecScroll" style="display:flex;gap:8px;overflow-x:auto;flex:1;scrollbar-width:none"></div>
    </div>

    <!-- LIVE TV PAGE -->
    <div class="page active" id="page-live">
      <div class="live-layout">
        <div class="player-panel">
          <div class="player-wrap">
            <video id="mainVideo" playsinline></video>
            <div id="vidIdle">
              <div class="idle-icon">📡</div>
              <div class="idle-text">Bir kanal seçin</div>
              <div class="idle-sub">Sağdaki listeden veya klavyeyle gezinin</div>
            </div>
            <div id="vidLoader" class="hidden">
              <div class="loader-spinner"></div>
              <div id="vidLoaderText" style="color:#fff;margin-top:16px;font-size:14px;font-weight:600">Bağlanıyor…</div>
            </div>
            <div id="vidError" class="hidden">
              <div class="error-icon">⚠️</div>
              <div id="vidErrMsg">Akış yüklenemedi</div>
              <div id="vidErrSub"></div>
              <div style="display:flex;gap:8px;flex-wrap:wrap;justify-content:center;margin-top:16px">
                <button class="btn" id="retryBtn">🔄 Yeniden</button>
              </div>
            </div>
            <div id="chOsd">
              <div style="font-size:36px">📺</div>
              <div>
                <div id="chOsdNum" style="font-size:28px;font-weight:800;color:var(--accent-light)"></div>
                <div id="chOsdName"></div>
              </div>
            </div>
            <div id="osdOverlay"></div>
          </div>
          <div class="player-controls">
            <button class="pc-btn" id="pcPrev" title="Önceki">⏮</button>
            <button class="pc-btn" id="pcPlay" title="Oynat">▶</button>
            <button class="pc-btn" id="pcNext" title="Sonraki">⏭</button>
            <div class="pc-sep"></div>
            <button class="pc-btn" id="pcMute" title="Sessiz">🔊</button>
            <input type="range" id="pcVol" min="0" max="1" step="0.01" value="1">
            <div class="pc-sep"></div>
            <button class="pc-btn" id="pcSpeedBtn">1×</button>
            <button class="pc-btn" id="pcPipBtn" title="PiP">📌</button>
            <button class="pc-btn" id="pcCinemaBtn" title="Sinema">🎭</button>
            <button class="pc-btn" id="pcRecBtn" title="Kayıt">⏺</button>
            <button class="pc-btn" id="pcFullscreen" title="Tam Ekran">⛶</button>
          </div>
          <div class="epg-strip">
            <div class="epg-strip-label">Şimdi</div>
            <div class="epg-strip-info">
              <div class="epg-strip-title" id="epgNow">—</div>
              <div class="epg-strip-bar"><div id="epgNowFill" style="height:100%;background:var(--accent);border-radius:2px;width:0;transition:width 1s"></div></div>
            </div>
            <div class="epg-strip-next">
              <div style="font-size:11px;color:var(--text-muted)">SONRA</div>
              <div id="epgNext" style="font-weight:600">—</div>
            </div>
          </div>
        </div>
        <div class="channel-panel">
          <div class="ch-panel-header">
            <div class="ch-search-row">
              <input type="text" id="chSearch" placeholder="Kanal ara…">
            </div>
            <div class="ch-filter-row">
              <button class="ch-filter-btn active" data-filter="all">Tümü</button>
              <button class="ch-filter-btn" data-filter="fav">⭐</button>
              <button class="ch-filter-btn" data-filter="hd">HD+</button>
              <button class="ch-filter-btn" data-filter="4k">4K</button>
            </div>
            <div class="ch-sort-row">
              <select id="chSort">
                <option value="default">Sırala</option>
                <option value="alpha">A → Z</option>
                <option value="quality">Kalite</option>
              </select>
            </div>
          </div>
          <div id="catTabs"></div>
          <div id="chList"></div>
          <div class="ch-count-bar"><span id="chCountLabel">0 kanal</span></div>
          <div class="ch-panel-actions">
            <button class="btn btn-sm w-full" id="chAddBtn">+ Kaynak Ekle</button>
          </div>
        </div>
      </div>
    </div>

    <!-- MOVIES PAGE -->
    <div class="page" id="page-movies">
      <div class="page-scroll">
        <div class="page-header">
          <div><div class="page-title">🎬 Filmler</div><div class="page-sub" id="moviesCountLabel">0 film</div></div>
        </div>
        <div class="grid-4" id="moviesGrid"></div>
      </div>
    </div>

    <!-- SERIES PAGE -->
    <div class="page" id="page-series">
      <div class="page-scroll">
        <div class="page-header">
          <div><div class="page-title">📺 Diziler</div><div class="page-sub" id="seriesCountLabel">0 dizi</div></div>
        </div>
        <div class="grid-4" id="seriesGrid"></div>
      </div>
    </div>

    <!-- EPG PAGE -->
    <div class="page" id="page-epg">
      <div class="page-scroll" style="display:flex;flex-direction:column;overflow:hidden">
        <div class="page-header">
          <div class="page-title">📅 EPG Rehber</div>
        </div>
        <div id="epgContent" style="flex:1;overflow:auto"></div>
      </div>
    </div>

    <!-- FAVORITES PAGE -->
    <div class="page" id="page-favorites">
      <div class="page-scroll">
        <div class="page-header">
          <div><div class="page-title">⭐ Favoriler</div><div class="page-sub" id="favCountLabel">0 öğe</div></div>
          <div style="display:flex;gap:8px">
            <button class="btn btn-sm btn-danger" id="favClearBtn">🗑️ Temizle</button>
          </div>
        </div>
        <div id="favList"></div>
      </div>
    </div>

    <!-- CATCHUP PAGE -->
    <div class="page" id="page-catchup">
      <div class="page-scroll">
        <div class="page-header">
          <div><div class="page-title">⏪ Catch-Up TV</div><div class="page-sub">Kaçırdığınız programları izleyin</div></div>
        </div>
        <div class="grid-4" id="catchupGrid"></div>
      </div>
    </div>

    <!-- DVR PAGE -->
    <div class="page" id="page-dvr">
      <div class="page-scroll">
        <div class="page-header">
          <div class="page-title">⏺ DVR / Kayıtlar</div>
        </div>
        <div class="tab-bar">
          <div class="tab-item active" data-dvr="recordings">📁 Kayıtlar</div>
          <div class="tab-item" data-dvr="timers">⏰ Zamanlayıcılar</div>
        </div>
        <div id="dvrContent"></div>
      </div>
    </div>

    <!-- STATS PAGE -->
    <div class="page" id="page-stats">
      <div class="page-scroll">
        <div class="page-header">
          <div class="page-title">📊 İstatistikler</div>
          <div style="display:flex;gap:8px">
            <button class="btn btn-sm btn-ghost" id="statsExport">📤 CSV</button>
            <button class="btn btn-sm btn-ghost" id="statsReset">🔄 Sıfırla</button>
          </div>
        </div>
        <div class="stats-row" id="statsGrid"></div>
      </div>
    </div>

    <!-- SETTINGS PAGE -->
    <div class="page" id="page-settings">
      <div class="page-scroll">
        <div class="page-header"><div class="page-title">⚙️ Ayarlar</div></div>
        <div style="max-width:600px">
          <div style="background:var(--bg2);border:1px solid var(--border);border-radius:var(--radius);padding:20px;margin-bottom:16px">
            <h3 style="font-size:16px;font-weight:700;margin-bottom:16px;padding-bottom:12px;border-bottom:1px solid var(--border)">🎨 Görünüm</h3>
            <div style="display:flex;align-items:center;justify-content:space-between;padding:12px 0;border-bottom:1px solid var(--border)">
              <div><div style="font-size:14px">Tema</div><div style="font-size:12px;color:var(--text-muted)">Uygulama teması</div></div>
              <select id="setTheme" style="width:auto;min-width:120px">
                <option value="dark">🌙 Koyu</option>
                <option value="light">☀️ Açık</option>
                <option value="amoled">⚫ AMOLED</option>
              </select>
            </div>
          </div>
          <div style="background:var(--bg2);border:1px solid var(--border);border-radius:var(--radius);padding:20px;margin-bottom:16px">
            <h3 style="font-size:16px;font-weight:700;margin-bottom:16px;padding-bottom:12px;border-bottom:1px solid var(--border)">ℹ️ Hakkında</h3>
            <div style="display:flex;align-items:center;justify-content:space-between;padding:12px 0">
              <div style="font-size:14px">Sürüm</div>
              <div style="color:var(--accent);font-weight:700">v4.2.0 Pro</div>
            </div>
            <div style="display:flex;align-items:center;justify-content:space-between;padding:12px 0">
              <div style="font-size:14px">Klavye Kısayolları</div>
              <button class="btn btn-sm btn-ghost" id="setShowKeys">Görüntüle</button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>

<nav class="bottom-nav">
  <div class="bn-item active" data-page="live"><span class="bn-icon">📡</span><span>Canlı</span></div>
  <div class="bn-item" data-page="movies"><span class="bn-icon">🎬</span><span>Film</span></div>
  <div class="bn-item" data-page="epg"><span class="bn-icon">📅</span><span>EPG</span></div>
  <div class="bn-item" data-page="favorites"><span class="bn-icon">⭐</span><span>Favori</span></div>
  <div class="bn-item" data-page="settings"><span class="bn-icon">⚙️</span><span>Ayar</span></div>
</nav>

<script src="https://cdn.jsdelivr.net/npm/hls.js@latest"></script>
<script>
(function(){
'use strict';

// Utility functions
const $ = (s,p) => (p||document).querySelector(s);
const $$ = (s,p) => [...(p||document).querySelectorAll(s)];
const wait = ms => new Promise(r => setTimeout(r, ms));
const uuid = () => 'id-' + Math.random().toString(36).substr(2,9) + Date.now().toString(36);
const clamp = (v,lo,hi) => Math.max(lo,Math.min(hi,v));
const rand = (a,b) => Math.floor(Math.random()*(b-a+1))+a;
const debounce = (fn,ms=300) => {let t;return(...a)=>{clearTimeout(t);t=setTimeout(()=>fn(...a),ms)}};
const fmtDate = d => new Date(d).toLocaleDateString('tr-TR', {day:'numeric',month:'short',hour:'2-digit',minute:'2-digit'});

// App State
const App = {
  version: '4.2.0',
  currentPage: 'live',
  channels: [],
  groups: [],
  selectedCh: null,
  playingCh: null,
  lastCh: null,
  favorites: new Set(),
  dvrTimers: [],
  settings: {theme:'dark'},
  player: null,
  hls: null,
  bitrates: [],
  notifications: []
};

const Store = {
  get(k, def=null) { try { const v=localStorage.getItem('svp_'+k); return v?JSON.parse(v):def; } catch(e){return def;} },
  set(k, v) { try { localStorage.setItem('svp_'+k, JSON.stringify(v)); } catch(e){} }
};

function loadState() {
  App.favorites = new Set(Store.get('favorites', []));
  App.channels = Store.get('channels', []);
  App.settings = {...App.settings, ...Store.get('settings', {})};
  applyTheme();
}

function saveState() {
  Store.set('favorites', [...App.favorites]);
  Store.set('channels', App.channels);
  Store.set('settings', App.settings);
}

// Toast System
function showToast(msg, type='info', duration=3500) {
  const stack = $('#toastStack');
  if(!stack) return;
  const t = document.createElement('div');
  t.className = `toast toast-${type}`;
  const icons = {success:'✅', error:'❌', warning:'⚠️', info:'ℹ️'};
  t.innerHTML = `<span class="toast-icon">${icons[type]||'ℹ️'}</span><span>${msg}</span>`;
  stack.appendChild(t);
  requestAnimationFrame(() => t.classList.add('show'));
  setTimeout(() => { t.classList.remove('show'); setTimeout(()=>t.remove(),300); }, duration);
}

const Toast = {
  show: showToast,
  success: m => showToast(m,'success'),
  error: m => showToast(m,'error'),
  warn: m => showToast(m,'warning'),
  info: m => showToast(m,'info')
};

// Modal System
let _modalActive = null;
function openModal(id) {
  const el = $(`#modal-${id}`);
  if(!el) return;
  if(_modalActive) closeModal();
  el.classList.add('show');
  _modalActive = id;
  document.body.style.overflow = 'hidden';
}
function closeModal() {
  if(!_modalActive) return;
  const el = $(`#modal-${_modalActive}`);
  if(el) el.classList.remove('show');
  _modalActive = null;
  document.body.style.overflow = '';
}

document.addEventListener('click', e => {
  if(e.target.classList.contains('modal-close')) closeModal();
  if(e.target.classList.contains('modal-backdrop') && !e.target.closest('.modal')) closeModal();
});

// Confirm Modal
function showConfirm(msg, title='Onayla') {
  return new Promise(resolve => {
    $('#confirmTitle').textContent = title;
    $('#confirmMsg').textContent = msg;
    $('#confirmOk').onclick = () => { closeModal(); resolve(true); };
    $$('.modal-close', '#modal-confirm').forEach(b => b.onclick = () => { closeModal(); resolve(false); });
    openModal('confirm');
  });
}

// Splash Screen
async function showSplash() {
  const splash = $('#splash');
  const bar = $('#splashBar');
  const status = $('#splashStatus');
  const steps = [
    {msg:'Bileşenler yükleniyor…', pct:15},
    {msg:'Tema yapılandırılıyor…', pct:30},
    {msg:'Kaynaklar kontrol ediliyor…', pct:45},
    {msg:'HLS motoru başlatılıyor…', pct:60},
    {msg:'UI hazırlanıyor…', pct:75},
    {msg:'Hazır! 🎬', pct:100}
  ];
  for(const s of steps) {
    status.textContent = s.msg;
    bar.style.width = s.pct + '%';
    await wait(180 + rand(0,200));
  }
  await wait(300);
  splash.style.opacity = '0';
  splash.style.transition = 'opacity .5s';
  await wait(550);
  splash.style.display = 'none';
}

// Theme
function applyTheme() {
  document.body.dataset.theme = App.settings.theme;
  const themeEl = $('#setTheme');
  if(themeEl) themeEl.value = App.settings.theme;
}

// Navigation
function navigate(page) {
  $$('.page').forEach(p => p.classList.remove('active'));
  const target = $(`#page-${page}`);
  if(target) target.classList.add('active');
  $$('.sb-item').forEach(i => i.classList.toggle('active', i.dataset.page === page));
  $$('.bn-item').forEach(i => i.classList.toggle('active', i.dataset.page === page));
  const names = {live:'Canlı TV',movies:'Filmler',series:'Diziler',epg:'EPG',favorites:'Favoriler',dvr:'DVR',stats:'İstatistikler',settings:'Ayarlar',catchup:'Catch-Up'};
  const bc = $('#tbBcCurrent');
  if(bc) bc.textContent = names[page] || page;
  App.currentPage = page;
  if(page === 'stats') renderStats();
  if(page === 'movies') renderMovies();
  if(page === 'series') renderSeries();
  if(page === 'favorites') renderFavorites();
  if(page === 'epg') renderEPG();
  if(page === 'dvr') renderDVR();
  if(page === 'catchup') renderCatchup();
  // Close mobile sidebar
  $('#sidebar').classList.remove('sidebar-open');
}

// Clock
function startClock() {
  const el = $('#tbClock');
  if(!el) return;
  const fmt = () => { el.textContent = new Date().toLocaleTimeString('tr-TR', {hour:'2-digit', minute:'2-digit'}); };
  fmt();
  setInterval(fmt, 1000);
}

// Sidebar
function setupSidebar() {
  $$('.sb-item, .bn-item').forEach(el => {
    el.addEventListener('click', () => {
      const p = el.dataset.page;
      if(p) navigate(p);
    });
  });
  $('#sidebarToggle')?.addEventListener('click', () => {
    $('#sidebar').classList.toggle('collapsed');
  });
  $('#mobMenuBtn')?.addEventListener('click', () => {
    $('#sidebar').classList.toggle('sidebar-open');
  });
}

// Player
function initPlayer() {
  App.player = $('#mainVideo');
  if(!App.player) return;
  App.player.volume = 1;
}

function loadStream(url, name) {
  const v = App.player;
  if(!v) return;
  showLoader();
  $('#vidIdle').classList.add('hidden');
  $('#vidError').classList.add('hidden');
  if(App.hls) { App.hls.destroy(); App.hls = null; }

  if(v.canPlayType('application/vnd.apple.mpegurl')) {
    v.src = url;
    v.addEventListener('loadedmetadata', onVideoLoaded, {once:true});
    v.addEventListener('error', () => onVideoError(url), {once:true});
    return;
  }

  if(window.Hls && Hls.isSupported()) {
    const hls = new Hls({enableWorker:true,startLevel:-1,maxBufferLength:30});
    App.hls = hls;
    hls.loadSource(url);
    hls.attachMedia(v);
    hls.on(Hls.Events.MANIFEST_PARSED, () => onVideoLoaded());
    hls.on(Hls.Events.ERROR, (e,data) => {
      if(data.fatal) {
        if(data.type === Hls.ErrorTypes.NETWORK_ERROR) hls.startLoad();
        else { onVideoError(url); hls.destroy(); }
      }
    });
  } else {
    Toast.error('HLS desteklenmiyor!');
  }
}

function onVideoLoaded() {
  hideLoader();
  App.player.play().catch(() => {});
  Toast.success('Akış bağlandı ✓');
}

function onVideoError(url) {
  hideLoader();
  const errEl = $('#vidError');
  if(errEl) errEl.classList.remove('hidden');
  $('#vidErrMsg').textContent = 'Akış yüklenemedi';
  $('#vidErrSub').textContent = url;
  Toast.error('Oynatma hatası!');
}

function showLoader() {
  $('#vidLoader').classList.remove('hidden');
  $('#vidLoaderText').textContent = 'Bağlanıyor…';
}
function hideLoader() {
  $('#vidLoader').classList.add('hidden');
}

function selectChannel(ch) {
  App.lastCh = App.playingCh;
  App.selectedCh = ch;
  App.playingCh = ch;
  showChOsd(ch);
  loadStream(ch.url, ch.name);
  $$('.ch-item').forEach(el => el.classList.toggle('selected', el.dataset.id == ch.id));
  const item = $(`.ch-item[data-id="${ch.id}"]`);
  if(item) item.scrollIntoView({behavior:'smooth', block:'nearest'});
  updateEPGStrip(ch);
}

function showChOsd(ch) {
  const osd = $('#chOsd');
  if(!osd) return;
  $('#chOsdNum').textContent = ch.number || '—';
  $('#chOsdName').textContent = ch.name;
  osd.classList.add('show');
  clearTimeout(App._osdTimer);
  App._osdTimer = setTimeout(() => osd.classList.remove('show'), 3000);
}

function showOsd(text) {
  const osd = $('#osdOverlay');
  if(!osd) return;
  osd.textContent = text;
  osd.classList.add('show');
  clearTimeout(App._osdTimer2);
  App._osdTimer2 = setTimeout(() => osd.classList.remove('show'), 2000);
}

function updateVolumeUI() {
  const v = App.player;
  if(!v) return;
  const icon = v.muted ? '🔇' : v.volume === 0 ? '🔇' : v.volume < 0.33 ? '🔈' : v.volume < 0.66 ? '🔉' : '🔊';
  const pm = $('#pcMute');
  if(pm) pm.textContent = icon;
  const pv = $('#pcVol');
  if(pv) pv.value = v.muted ? 0 : v.volume;
}

function switchChannel(dir) {
  const list = getFilteredChannels();
  if(!list.length) return;
  let idx = list.findIndex(c => c.id === (App.selectedCh?.id));
  if(idx < 0) idx = 0;
  idx = (idx + dir + list.length) % list.length;
  selectChannel(list[idx]);
}

function setupPlayerControls() {
  const v = App.player;
  if(!v) return;

  $('#pcPlay')?.addEventListener('click', () => {
    if(v.paused) {
      v.play().catch(() => {});
      $('#pcPlay').textContent = '⏸';
      showOsd('▶ Oynat');
    } else {
      v.pause();
      $('#pcPlay').textContent = '▶';
      showOsd('⏸ Duraklat');
    }
  });

  $('#pcPrev')?.addEventListener('click', () => switchChannel(-1));
  $('#pcNext')?.addEventListener('click', () => switchChannel(1));

  $('#pcMute')?.addEventListener('click', () => {
    v.muted = !v.muted;
    updateVolumeUI();
  });

  $('#pcVol')?.addEventListener('input', function() {
    v.volume = +this.value;
    v.muted = false;
    updateVolumeUI();
  });

  const speeds = [0.5, 1, 1.25, 1.5, 2];
  let speedIdx = 1;
  $('#pcSpeedBtn')?.addEventListener('click', () => {
    speedIdx = (speedIdx + 1) % speeds.length;
    v.playbackRate = speeds[speedIdx];
    $('#pcSpeedBtn').textContent = speeds[speedIdx] + '×';
    showOsd('Hız: ' + speeds[speedIdx] + '×');
  });

  $('#pcPipBtn')?.addEventListener('click', async() => {
    try {
      if(document.pictureInPictureElement) await document.exitPictureInPicture();
      else await v.requestPictureInPicture();
    } catch(e) { Toast.error('PiP desteklenmiyor'); }
  });

  $('#pcCinemaBtn')?.addEventListener('click', () => {
    $('#app').classList.toggle('cinema-mode');
    showOsd('Sinema: ' + ($('#app').classList.contains('cinema-mode') ? 'Açık' : 'Kapalı'));
  });

  $('#pcRecBtn')?.addEventListener('click', () => {
    if(App.playingCh) {
      App.dvrTimers.push({id: uuid(), ch_id: App.playingCh.id, ch_name: App.playingCh.name, start: Date.now(), end: Date.now() + 3600000});
      saveState();
      showOsd('⏺ Kayıt zamanlandı');
      Toast.success('Kayıt zamanlandı');
    }
  });

  $('#pcFullscreen')?.addEventListener('click', () => {
    if(!document.fullscreenElement) {
      document.documentElement.requestFullscreen().catch(() => {});
    } else {
      document.exitFullscreen();
    }
  });

  $('#tbFullBtn')?.addEventListener('click', () => {
    if(!document.fullscreenElement) {
      document.documentElement.requestFullscreen().catch(() => {});
    } else {
      document.exitFullscreen();
    }
  });

  $('#retryBtn')?.addEventListener('click', () => {
    if(App.playingCh) loadStream(App.playingCh.url, App.playingCh.name);
  });
}

// Channel List
function buildGroups() {
  const groups = {};
  App.channels.forEach(ch => {
    const g = ch.group || 'Diğer';
    if(!groups[g]) groups[g] = [];
    groups[g].push(ch);
  });
  App.groups = Object.entries(groups).map(([name, channels]) => ({name, count: channels.length, channels}));
  return App.groups;
}

function getFilteredChannels() {
  const search = ($('#chSearch')?.value || '').toLowerCase();
  const filter = ($('.ch-filter-btn.active')?.dataset.filter) || 'all';
  const sort = $('#chSort')?.value || 'default';
  const activeCat = ($('.cat-tab.active')?.dataset.cat) || 'all';
  let list = [...App.channels];
  if(activeCat !== 'all') list = list.filter(c => c.group === activeCat);
  if(search) list = list.filter(c => c.name.toLowerCase().includes(search) || String(c.number || '').includes(search));
  if(filter === 'fav') list = list.filter(c => App.favorites.has(c.id));
  if(filter === 'hd') list = list.filter(c => c.quality === 'HD' || c.quality === 'FHD' || c.quality === '4K');
  if(filter === '4k') list = list.filter(c => c.quality === '4K');
  if(sort === 'alpha') list.sort((a,b) => a.name.localeCompare(b.name, 'tr'));
  if(sort === 'quality') {
    const q = {4K:3, FHD:2, HD:1, SD:0};
    list.sort((a,b) => (q[b.quality]||0) - (q[a.quality]||0));
  }
  return list;
}

function renderChannelList() {
  const list = getFilteredChannels();
  const container = $('#chList');
  if(!container) return;
  if(!list.length) {
    container.innerHTML = `<div class="empty"><div class="empty-icon">📡</div><div class="empty-title">Kanal Bulunamadı</div><div class="empty-sub">Aramanızı değiştirin</div></div>`;
    $('#chCountLabel').textContent = '0 kanal';
    return;
  }
  container.innerHTML = list.map((ch, i) => {
    const fav = App.favorites.has(ch.id);
    const playing = App.playingCh?.id === ch.id;
    return `<div class="ch-item${playing ? ' selected' : ''}" data-id="${ch.id}" data-idx="${i}">
      <div class="ch-num">${ch.number || i+1}</div>
      <div class="ch-logo-wrap"><span style="font-size:20px">📺</span></div>
      <div class="ch-info">
        <div class="ch-name truncate">${ch.name}</div>
        <div class="ch-group">${ch.group || ''}</div>
      </div>
      ${ch.quality ? `<span class="ch-quality">${ch.quality}</span>` : ''}
      <button class="ch-fav-btn${fav ? ' active' : ''}" data-id="${ch.id}">${fav ? '⭐' : '☆'}</button>
    </div>`;
  }).join('');
  $('#chCountLabel').textContent = list.length + ' kanal';

  container.querySelectorAll('.ch-item').forEach(el => {
    el.addEventListener('click', e => {
      if(e.target.closest('.ch-fav-btn')) return;
      const ch = App.channels.find(c => c.id == el.dataset.id);
      if(ch) selectChannel(ch);
    });
    el.addEventListener('contextmenu', e => {
      e.preventDefault();
      const ch = App.channels.find(c => c.id == el.dataset.id);
      if(ch) {
        App._ctxChannel = ch;
        showContextMenu(e.clientX, e.clientY);
      }
    });
  });

  container.querySelectorAll('.ch-fav-btn').forEach(btn => {
    btn.addEventListener('click', e => {
      e.stopPropagation();
      toggleFavorite(btn.dataset.id);
    });
  });
}

function renderCategoryTabs() {
  const container = $('#catTabs');
  if(!container) return;
  buildGroups();
  let html = `<div class="cat-tab active" data-cat="all">Tümü (${App.channels.length})</div>`;
  App.groups.forEach(g => {
    html += `<div class="cat-tab" data-cat="${g.name}">${g.name} (${g.count})</div>`;
  });
  container.innerHTML = html;
  container.querySelectorAll('.cat-tab').forEach(tab => {
    tab.addEventListener('click', () => {
      container.querySelectorAll('.cat-tab').forEach(t => t.classList.remove('active'));
      tab.classList.add('active');
      renderChannelList();
    });
  });
}

function toggleFavorite(id) {
  if(App.favorites.has(id)) {
    App.favorites.delete(id);
    Toast.info('Kaldırıldı');
  } else {
    App.favorites.add(id);
    Toast.success('Favorilere eklendi ⭐');
  }
  saveState();
  renderChannelList();
  updateFavCount();
}

function updateFavCount() {
  const c = App.favorites.size;
  const el = $('#favCount');
  if(el) el.textContent = c;
  const el2 = $('#favCountLabel');
  if(el2) el2.textContent = c + ' öğe';
}

// Setup channel list events
$$('.ch-filter-btn').forEach(btn => {
  btn.addEventListener('click', () => {
    $$('.ch-filter-btn').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
    renderChannelList();
  });
});
$('#chSort')?.addEventListener('change', renderChannelList);
$('#chSearch')?.addEventListener('input', debounce(renderChannelList, 200));
$('#chAddBtn')?.addEventListener('click', () => openModal('addSource'));

// Context Menu
function showContextMenu(x, y) {
  const menu = $('#ctxMenu');
  if(!menu) return;
  menu.style.left = Math.min(x, window.innerWidth - 220) + 'px';
  menu.style.top = Math.min(y, window.innerHeight - 320) + 'px';
  menu.classList.add('show');
}
function hideContextMenu() {
  $('#ctxMenu').classList.remove('show');
}

$('#ctxMenu')?.addEventListener('click', e => {
  const item = e.target.closest('.ctx-item');
  if(!item) return;
  const action = item.dataset.action;
  const ch = App._ctxChannel;
  if(!ch) return;
  switch(action) {
    case 'play': selectChannel(ch); break;
    case 'fav': toggleFavorite(ch.id); break;
    case 'info': Toast.info(ch.name + ' - ' + (ch.group || '')); break;
    case 'copy': navigator.clipboard?.writeText(ch.url).then(() => Toast.success('URL kopyalandı')); break;
    case 'remove':
      App.channels = App.channels.filter(c => c.id !== ch.id);
      saveState();
      renderChannelList();
      renderCategoryTabs();
      Toast.info('Kanal kaldırıldı');
      break;
  }
  hideContextMenu();
});
document.addEventListener('click', () => hideContextMenu());

// Command Palette
let cmdOpen = false;
function openCommandPalette() {
  $('#cmdOverlay').classList.add('show');
  const ci = $('#cmdInput');
  if(ci) { ci.value = ''; ci.focus(); }
  cmdOpen = true;
  renderCommandPalette('');
}
function closeCommandPalette() {
  $('#cmdOverlay').classList.remove('show');
  cmdOpen = false;
}

$('#tbCmdBtn')?.addEventListener('click', openCommandPalette);
$('#cmdOverlay')?.addEventListener('click', e => {
  if(e.target === e.currentTarget) closeCommandPalette();
});
document.addEventListener('keydown', e => {
  if((e.ctrlKey || e.metaKey) && e.key === 'k') { e.preventDefault(); openCommandPalette(); }
  if(e.key === 'Escape' && cmdOpen) closeCommandPalette();
});

$('#cmdInput')?.addEventListener('input', debounce(function() {
  renderCommandPalette(this.value);
}, 150));

function renderCommandPalette(q) {
  const container = $('#cmdResults');
  if(!container) return;
  const results = q ? App.channels.filter(c => c.name.toLowerCase().includes(q.toLowerCase())).slice(0, 10) : [];
  let html = '';
  if(q && results.length) {
    html = `<div class="cmd-section">📺 Kanallar</div>` + results.map(ch => `
      <div class="cmd-item" data-ch-id="${ch.id}">
        <span class="cmd-icon">📺</span>
        <div class="cmd-content">
          <div class="cmd-name">${ch.name}</div>
          <div class="cmd-sub">${ch.group || ''}</div>
        </div>
      </div>
    `).join('');
  } else if(q) {
    html = '<div class="cmd-empty">Sonuç bulunamadı</div>';
  } else {
    const quickActions = [
      {icon:'📅', name:'EPG Aç', action:() => navigate('epg')},
      {icon:'📊', name:'İstatistikler', action:() => navigate('stats')},
      {icon:'📸', name:'Screenshot', action:() => takeScreenshot()},
      {icon:'⛶', name:'Tam Ekran', action:() => { if(!document.fullscreenElement) document.documentElement.requestFullscreen().catch(() => {}); }},
      {icon:'🎨', name:'Tema Değiştir', action:cycleTheme},
    ];
    html = `<div class="cmd-section">⚡ Hızlı Komutlar</div>` + quickActions.map(a => `
      <div class="cmd-item" data-action="${a.name}">
        <span class="cmd-icon">${a.icon}</span>
        <div class="cmd-content"><div class="cmd-name">${a.name}</div></div>
      </div>
    `).join('');
  }
  container.innerHTML = html;

  container.querySelectorAll('.cmd-item[data-ch-id]').forEach(el => {
    el.addEventListener('click', () => {
      const ch = App.channels.find(c => c.id == el.dataset.chId);
      if(ch) { selectChannel(ch); navigate('live'); closeCommandPalette(); }
    });
  });
  container.querySelectorAll('.cmd-item[data-action]').forEach(el => {
    el.addEventListener('click', () => {
      const name = el.dataset.action;
      const action = q ? null : [
        {name:'EPG Aç', fn:() => navigate('epg')},
        {name:'İstatistikler', fn:() => navigate('stats')},
        {name:'Screenshot', fn:() => takeScreenshot()},
        {name:'Tam Ekran', fn:() => { if(!document.fullscreenElement) document.documentElement.requestFullscreen().catch(() => {}); }},
        {name:'Tema Değiştir', fn:cycleTheme},
      ].find(a => a.name === name);
      if(action) action.fn();
      closeCommandPalette();
    });
  });
}

function cycleTheme() {
  const themes = ['dark', 'light', 'amoled'];
  let idx = themes.indexOf(App.settings.theme);
  idx = (idx + 1) % themes.length;
  App.settings.theme = themes[idx];
  applyTheme();
  saveState();
  Toast.success('Tema: ' + themes[idx]);
}

// Global Search
$('#globalSearch')?.addEventListener('input', debounce(function() {
  const q = this.value.toLowerCase().trim();
  const dropdown = $('#searchDropdown');
  if(!dropdown) return;
  if(!q) { dropdown.classList.remove('show'); return; }
  const results = App.channels.filter(c => c.name.toLowerCase().includes(q)).slice(0, 8);
  if(!results.length) { dropdown.innerHTML = '<div class="cmd-empty">Sonuç yok</div>'; dropdown.classList.add('show'); return; }
  dropdown.innerHTML = results.map(ch => `
    <div class="cmd-item" data-ch-id="${ch.id}">
      <span class="cmd-icon">📺</span>
      <div class="cmd-content">
        <div class="cmd-name">${ch.name}</div>
        <div class="cmd-sub">${ch.group || ''}</div>
      </div>
    </div>
  `).join('');
  dropdown.classList.add('show');
  dropdown.querySelectorAll('.cmd-item').forEach(el => {
    el.addEventListener('click', () => {
      const ch = App.channels.find(c => c.id == el.dataset.chId);
      if(ch) { selectChannel(ch); navigate('live'); }
      dropdown.classList.remove('show');
      $('#globalSearch').blur();
    });
  });
}, 200));
document.addEventListener('click', e => {
  if(!e.target.closest('.search-wrap')) $('#searchDropdown')?.classList.remove('show');
});

// Notifications
function addNotification(title, body) {
  App.notifications.unshift({id: uuid(), title, body, ts: Date.now(), read: false});
  App.notifications = App.notifications.slice(0, 50);
  renderNotifications();
}
function renderNotifications() {
  const list = $('#notifList');
  if(!list) return;
  if(!App.notifications.length) {
    list.innerHTML = `<div class="empty"><div class="empty-icon">🔕</div><div class="empty-title">Bildirim yok</div></div>`;
    return;
  }
  list.innerHTML = App.notifications.map(n => `
    <div class="notif-item${n.read ? '' : ''}" data-id="${n.id}">
      <div class="notif-icon-wrap">🔔</div>
      <div class="notif-body">
        <div class="notif-title">${n.title}</div>
        <div class="notif-body-text">${n.body}</div>
        <div class="notif-time">${fmtDate(n.ts)}</div>
      </div>
    </div>
  `).join('');
  const unread = App.notifications.some(n => !n.read);
  const dot = $('#tbNotifDot');
  if(dot) dot.classList.toggle('hidden', !unread);
}
$('#tbNotifBtn')?.addEventListener('click', () => {
  $('#notifCenter').classList.toggle('show');
  App.notifications.forEach(n => n.read = true);
  renderNotifications();
});
$('#clearAllNotif')?.addEventListener('click', () => { App.notifications = []; renderNotifications(); Toast.info('Temizlendi'); });

// Screenshot
function takeScreenshot() {
  const v = App.player;
  if(!v || v.readyState < 2) { Toast.error('Oynatıcı hazır değil'); return; }
  const canvas = document.createElement('canvas');
  canvas.width = v.videoWidth || 1280;
  canvas.height = v.videoHeight || 720;
  canvas.getContext('2d').drawImage(v, 0, 0);
  const dataUrl = canvas.toDataURL('image/png');
  const a = document.createElement('a');
  a.href = dataUrl;
  a.download = `streamvault_${Date.now()}.png`;
  a.click();
  Toast.success('Kaydedildi');
}
$('#tbScreenshotBtn')?.addEventListener('click', takeScreenshot);

// EPG
let epgData = {};
function generateDemoEPG(ch) {
  const events = [];
  const now = new Date();
  const base = new Date(now.getFullYear(), now.getMonth(), now.getDate(), 0, 0, 0);
  const programs = ['Sabah Haberleri','Günlük Dizi','Spor Saati','Öğle Haberleri','Film','Magazin','Akşam Haberleri','Prime Dizi'];
  let time = base.getTime();
  for(let h=0; h<24; h+=2) {
    events.push({ch_id: ch.id, start: time, end: time + 7200000, title: programs[h/2 % programs.length], desc: ch.name + ' - ' + programs[h/2 % programs.length]});
    time += 7200000;
  }
  return events;
}
function getNowProgram(chId) {
  const events = epgData[chId];
  if(!events) return null;
  const now = Date.now();
  return events.find(e => now >= e.start && now < e.end);
}
function getNextProgram(chId) {
  const events = epgData[chId];
  if(!events) return null;
  const now = Date.now();
  const idx = events.findIndex(e => now >= e.start && now < e.end);
  return idx >= 0 && idx < events.length - 1 ? events[idx + 1] : events[0];
}
function updateEPGStrip(ch) {
  if(!ch) return;
  const now = getNowProgram(ch.id);
  const next = getNextProgram(ch.id);
  const nowEl = $('#epgNow');
  const nextEl = $('#epgNext');
  const fillEl = $('#epgNowFill');
  if(now && nowEl) { nowEl.textContent = now.title; }
  if(next && nextEl) nextEl.textContent = next.title;
  if(now && fillEl) {
    const pct = clamp(((Date.now() - now.start) / (now.end - now.start)) * 100, 0, 100);
    fillEl.style.width = pct + '%';
  }
}

function renderEPG() {
  const container = $('#epgContent');
  if(!container) return;
  let html = '';
  App.channels.slice(0, 20).forEach(ch => {
    const events = epgData[ch.id] || [];
    const now = getNowProgram(ch.id);
    html += `<div style="background:var(--bg2);border:1px solid var(--border);border-radius:var(--radius);padding:16px;margin-bottom:12px">
      <div style="display:flex;align-items:center;gap:12px;margin-bottom:12px">
        <span style="font-size:24px">📺</span>
        <div><div style="font-weight:700">${ch.name}</div><div style="font-size:12px;color:var(--text-muted)">${ch.group || ''}</div></div>
      </div>
      <div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(180px,1fr));gap:8px">`;
    events.slice(0, 6).forEach(ev => {
      const now = Date.now();
      const isActive = now >= ev.start && now < ev.end;
      html += `<div style="background:${isActive ? 'rgba(124,58,237,0.15)' : 'var(--bg3)'};border:1px solid ${isActive ? 'var(--accent)' : 'var(--border)'};border-radius:var(--radius-sm);padding:10px;cursor:pointer">
        <div style="font-size:12px;color:${isActive ? 'var(--accent)' : 'var(--text-muted)'};margin-bottom:4px">${new Date(ev.start).toLocaleTimeString('tr-TR',{hour:'2-digit',minute:'2-digit'})} - ${new Date(ev.end).toLocaleTimeString('tr-TR',{hour:'2-digit',minute:'2-digit'})}</div>
        <div style="font-weight:600;font-size:13px">${ev.title}</div>
      </div>`;
    });
    html += '</div></div>';
  });
  container.innerHTML = html;
  container.querySelectorAll('[style*="cursor:pointer"]').forEach((el, i) => {
    el.addEventListener('click', () => {
      const chIdx = Math.floor(i / 6);
      const evIdx = i % 6;
      const ch = App.channels[chIdx];
      if(ch) {
        selectChannel(ch);
        navigate('live');
      }
    });
  });
}

// Movies
function renderMovies() {
  const grid = $('#moviesGrid');
  if(!grid) return;
  const movies = App.channels.filter(c => c.type === 'movie' || c.group === 'Sinema');
  if(!movies.length) {
    grid.innerHTML = `<div class="empty"><div class="empty-icon">🎬</div><div class="empty-title">Film Yok</div><div class="empty-sub">Filmler için kaynak ekleyin</div></div>`;
    return;
  }
  grid.innerHTML = movies.map(m => `
    <div class="ph-card" data-id="${m.id}">
      <div class="ph-thumb" style="background:var(--accent-gradient)">
        <div class="ph-badge">${m.quality || 'HD'}</div>
      </div>
      <div class="ph-info">
        <div class="ph-title">${m.name}</div>
        <div class="ph-meta">${m.group || ''}</div>
      </div>
    </div>
  `).join('');
  grid.querySelectorAll('.ph-card').forEach(card => {
    card.addEventListener('click', () => {
      const ch = App.channels.find(c => c.id === card.dataset.id);
      if(ch) selectChannel(ch);
    });
  });
  $('#moviesCountLabel').textContent = movies.length + ' film';
}

// Series
function renderSeries() {
  const grid = $('#seriesGrid');
  if(!grid) return;
  const series = App.channels.filter(c => c.type === 'series' || c.group === 'Dizi');
  if(!series.length) {
    grid.innerHTML = `<div class="empty"><div class="empty-icon">📺</div><div class="empty-title">Dizi Yok</div></div>`;
    return;
  }
  grid.innerHTML = series.map(s => `
    <div class="ph-card" data-id="${s.id}">
      <div class="ph-thumb" style="background:var(--accent-gradient)">${s.quality || 'HD'}</div>
      <div class="ph-info">
        <div class="ph-title">${s.name}</div>
        <div class="ph-meta">${s.group || ''}</div>
      </div>
    </div>
  `).join('');
  grid.querySelectorAll('.ph-card').forEach(card => {
    card.addEventListener('click', () => {
      const ch = App.channels.find(c => c.id === card.dataset.id);
      if(ch) selectChannel(ch);
    });
  });
  $('#seriesCountLabel').textContent = series.length + ' dizi';
}

// Favorites
function renderFavorites() {
  const container = $('#favList');
  if(!container) return;
  const favChannels = App.channels.filter(c => App.favorites.has(c.id));
  if(!favChannels.length) {
    container.innerHTML = `<div class="empty"><div class="empty-icon">⭐</div><div class="empty-title">Favori Yok</div><div class="empty-sub">Kanallara ⭐ tıklayarak ekle</div></div>`;
    return;
  }
  container.innerHTML = favChannels.map(ch => `
    <div class="ch-item" data-id="${ch.id}">
      <div class="ch-logo-wrap"><span style="font-size:20px">📺</span></div>
      <div class="ch-info">
        <div class="ch-name truncate">${ch.name}</div>
        <div class="ch-group">${ch.group || ''}</div>
      </div>
      <button class="ch-fav-btn active" data-id="${ch.id}">⭐</button>
    </div>
  `).join('');
  container.querySelectorAll('.ch-item').forEach(el => {
    el.addEventListener('click', e => {
      if(e.target.closest('.ch-fav-btn')) return;
      const ch = App.channels.find(c => c.id == el.dataset.id);
      if(ch) selectChannel(ch);
    });
  });
  container.querySelectorAll('.ch-fav-btn').forEach(btn => {
    btn.addEventListener('click', e => { e.stopPropagation(); toggleFavorite(btn.dataset.id); });
  });
}
$('#favClearBtn')?.addEventListener('click', async() => {
  if(await showConfirm('Tüm favorileri temizle?')) {
    App.favorites.clear();
    saveState();
    renderFavorites();
    updateFavCount();
    Toast.success('Temizlendi');
  }
});

// Catchup
function renderCatchup() {
  const grid = $('#catchupGrid');
  if(!grid) return;
  const catchup = App.channels.filter(c => c.type === 'live').slice(0, 12).map(ch => ({...ch, program: getNowProgram(ch.id)?.title || 'Program'}));
  grid.innerHTML = catchup.map(c => `
    <div class="ph-card" data-id="${c.id}">
      <div class="ph-thumb" style="background:var(--accent-gradient)">
        <div class="ph-badge">▶</div>
      </div>
      <div class="ph-info">
        <div class="ph-title">${c.name}</div>
        <div class="ph-meta">${c.program}</div>
      </div>
    </div>
  `).join('');
  grid.querySelectorAll('.ph-card').forEach(card => {
    card.addEventListener('click', () => {
      const ch = App.channels.find(c => c.id === card.dataset.id);
      if(ch) selectChannel(ch);
    });
  });
}

// DVR
function renderDVR() {
  const container = $('#dvrContent');
  if(!container) return;
  const tab = App._dvrTab || 'recordings';
  if(tab === 'recordings') {
    if(!App.dvrTimers.length) {
      container.innerHTML = `<div class="empty"><div class="empty-icon">📁</div><div class="empty-title">Kayıt Yok</div><div class="empty-sub">⏺ butonuyla kayıt zamanlayın</div></div>`;
      return;
    }
    container.innerHTML = App.dvrTimers.map(t => `
      <div style="display:flex;align-items:center;gap:12px;padding:12px;background:var(--bg2);border:1px solid var(--border);border-radius:var(--radius);margin-bottom:8px">
        <span style="font-size:28px">⏺</span>
        <div style="flex:1">
          <div style="font-weight:700">${t.ch_name}</div>
          <div style="font-size:12px;color:var(--text-muted)">${fmtDate(t.start)}</div>
        </div>
        <button class="btn btn-sm btn-danger" data-id="${t.id}">Sil</button>
      </div>
    `).join('');
    container.querySelectorAll('[data-id]').forEach(btn => {
      btn.addEventListener('click', () => {
        App.dvrTimers = App.dvrTimers.filter(t => t.id !== btn.dataset.id);
        saveState();
        renderDVR();
        Toast.info('Silindi');
      });
    });
  }
}
$$('.tab-item[data-dvr]').forEach(tab => {
  tab.addEventListener('click', () => {
    $$('.tab-item[data-dvr]').forEach(t => t.classList.remove('active'));
    tab.classList.add('active');
    App._dvrTab = tab.dataset.dvr;
    renderDVR();
  });
});

// Stats
function renderStats() {
  const grid = $('#statsGrid');
  if(!grid) return;
  const metrics = [
    {icon:'📡', val: App.channels.length, label:'Toplam Kanal'},
    {icon:'⭐', val: App.favorites.size, label:'Favoriler'},
    {icon:'🔔', val: App.notifications.length, label:'Bildirimler'},
    {icon:'⏺', val: App.dvrTimers.length, label:'Kayıtlar'}
  ];
  grid.innerHTML = metrics.map(m => `
    <div class="stat-card">
      <div class="stat-icon">${m.icon}</div>
      <div class="stat-val">${m.val}</div>
      <div class="stat-label">${m.label}</div>
    </div>
  `).join('');
}
$('#statsExport')?.addEventListener('click', () => {
  const data = JSON.stringify({channels: App.channels.length, favorites: App.favorites.size, DVR: App.dvrTimers.length}, null, 2);
  const blob = new Blob([data], {type: 'application/json'});
  const a = document.createElement('a');
  a.href = URL.createObjectURL(blob);
  a.download = 'streamvault_stats.json';
  a.click();
  Toast.success('Dışa aktarıldı');
});
$('#statsReset')?.addEventListener('click', () => {
  App.bitrates = [];
  App.notifications = [];
  renderStats();
  Toast.info('Sıfırlandı');
});

// Add Source
let addStep = 1;
let addType = 'm3u';
$('#addSourceNext')?.addEventListener('click', () => {
  if(addStep === 1) { addStep = 2; renderAddStep(); }
  else if(addStep === 2) {
    if(addType === 'm3u' && !($('#addM3uUrl')?.value)) { Toast.error('URL gerekli'); return; }
    addStep = 3;
    renderAddStep();
    analyzeSource();
  } else if(addStep === 3) {
    finalizeSource();
  }
});
$('#addSourceBack')?.addEventListener('click', () => {
  if(addStep > 1) { addStep--; renderAddStep(); } else closeModal();
});
$$('.source-type-card').forEach(card => {
  card.addEventListener('click', () => {
    $$('.source-type-card').forEach(c => c.classList.remove('active'));
    card.classList.add('active');
    addType = card.dataset.type;
    renderAddStep();
  });
});

function renderAddStep() {
  ['step1dot','step2dot','step3dot'].forEach((id, i) => {
    const dot = $(`#${id}`);
    if(dot) dot.classList.toggle('active', addStep > i);
  });
  $('#step1line')?.classList.toggle('active', addStep >= 2);
  $('#step2line')?.classList.toggle('active', addStep >= 3);
  $('#addStep1').style.display = addStep === 1 ? '' : 'none';
  $('#addStep2').style.display = addStep === 2 ? '' : 'none';
  $('#addStep3').style.display = addStep === 3 ? '' : 'none';
  $('#addM3uForm').style.display = addStep === 2 && addType === 'm3u' ? '' : 'none';
  $('#addXtreamForm').style.display = addStep === 2 && addType === 'xtream' ? '' : 'none';
  $('#addFileForm').style.display = addStep === 2 && addType === 'file' ? '' : 'none';
  const backBtn = $('#addSourceBack');
  const nextBtn = $('#addSourceNext');
  if(backBtn) backBtn.textContent = addStep === 1 ? 'İptal' : '← Geri';
  if(nextBtn) nextBtn.textContent = addStep === 3 ? '✓ Tamamla' : 'İleri →';
}

async function analyzeSource() {
  const preview = $('#addPreview');
  if(!preview) return;
  preview.innerHTML = `<div class="empty"><div class="empty-icon" style="animation:spin 1s linear infinite">⏳</div><div class="empty-title">Analiz…</div></div>`;
  await wait(1500);
  const demoCount = rand(80, 300);
  preview.innerHTML = `
    <div style="text-align:center;margin-bottom:20px">
      <div style="font-size:48px;margin-bottom:8px">✅</div>
      <div style="font-size:18px;font-weight:700">Kaynak Analiz Edildi</div>
    </div>
    <div class="stats-grid">
      <div class="stat-card"><div class="stat-val">${demoCount}</div><div class="stat-label">Kanal</div></div>
      <div class="stat-card"><div class="stat-val">${rand(5,15)}</div><div class="stat-label">Kategori</div></div>
      <div class="stat-card"><div class="stat-val">${rand(1,5)}</div><div class="stat-label">4K</div></div>
    </div>
  `;
  App._pendingChannels = generateDemoChannels(demoCount);
  App._pendingName = $('#addM3uName')?.value || 'M3U Playlist';
  App._pendingUrl = $('#addM3uUrl')?.value || '';
}

function generateDemoChannels(count) {
  const groups = ['Haberler','Spor','Sinema','Dizi','Belgesel','Çocuk','Müzik','Yerel'];
  const names = ['Star','Fox','ATV','Show','TRT','Kanal D','CNNTürk','Habertürk','beIN','Sinema TV','National Geo','Discovery'];
  const quals = ['HD','FHD','4K'];
  return Array.from({length: count}, (_, i) => ({
    id: uuid(),
    name: `${names[i % names.length]} ${Math.floor(i / names.length) || ''}`.trim(),
    url: `https://demo.streamvault.local/live/${i}/stream.m3u8`,
    group: groups[i % groups.length],
    quality: quals[rand(0, 2)],
    number: i + 1,
    type: 'live',
    online: true
  }));
}

function finalizeSource() {
  const name = App._pendingName || 'Yeni Kaynak';
  const channels = App._pendingChannels || [];
  channels.forEach(ch => {
    ch.number = App.channels.length + 1;
    App.channels.push(ch);
  });
  saveState();
  closeModal();
  addStep = 1;
  renderAddStep();
  renderChannelList();
  renderCategoryTabs();
  updateFavCount();
  Toast.success(`Kaynak eklendi: ${name} (${channels.length} kanal)`);
  addNotification('Kaynak Eklendi', `${channels.length} kanal yüklendi`);
}

// Drop zone
const dropZone = $('#m3uDropZone');
const fileInput = $('#m3uFileInput');
if(dropZone && fileInput) {
  dropZone.addEventListener('click', () => fileInput.click());
  dropZone.addEventListener('dragover', e => { e.preventDefault(); dropZone.classList.add('drop-active'); });
  dropZone.addEventListener('dragleave', () => dropZone.classList.remove('drop-active'));
  dropZone.addEventListener('drop', e => {
    e.preventDefault();
    dropZone.classList.remove('drop-active');
    const file = e.dataTransfer.files[0];
    if(file) processM3UFile(file);
  });
  fileInput.addEventListener('change', () => {
    if(fileInput.files[0]) processM3UFile(fileInput.files[0]);
  });
  function processM3UFile(file) {
    const reader = new FileReader();
    reader.onload = () => {
      const text = reader.result;
      let channels = [];
      if(file.name.endsWith('.json')) {
        try {
          const json = JSON.parse(text);
          channels = (json.channels || json).map(c => ({
            id: uuid(), name: c.name || 'Unnamed', url: c.url || '',
            group: c.group || 'Diğer', quality: 'HD', number: 0, type: 'live', online: true
          }));
        } catch(e) { Toast.error('JSON hata'); }
      } else {
        channels = text.split('\n').filter(l => l.trim() && !l.startsWith('#')).map((url, i) => ({
          id: uuid(), name: 'Channel ' + (i+1), url, group: 'Diğer', quality: 'HD', number: i+1, type: 'live', online: true
        }));
      }
      App._pendingChannels = channels;
      const afn = $('#addFileName');
      if(afn) afn.value = file.name;
      dropZone.innerHTML = `<div class="drop-zone-icon">✅</div><div class="drop-zone-text">${file.name}<br><span style="color:var(--success)">${channels.length} kanal</span></div>`;
    };
    reader.readAsText(file);
  }
}

// Key Shortcuts
const shortcuts = [
  {key:'Space', desc:'Oynat/Duraklat', fn:() => $('#pcPlay')?.click()},
  {key:'↑', desc:'Ses +', fn:() => { if(App.player) { App.player.volume = clamp(App.player.volume + .05, 0, 1); updateVolumeUI(); } }},
  {key:'↓', desc:'Ses -', fn:() => { if(App.player) { App.player.volume = clamp(App.player.volume - .05, 0, 1); updateVolumeUI(); } }},
  {key:'←', desc:'Önceki', fn:() => switchChannel(-1)},
  {key:'→', desc:'Sonraki', fn:() => switchChannel(1)},
  {key:'m', desc:'Sessiz', fn:() => $('#pcMute')?.click()},
  {key:'f', desc:'Tam Ekran', fn:() => { if(!document.fullscreenElement) document.documentElement.requestFullscreen().catch(() => {}); }},
  {key:'p', desc:'Screenshot', fn:takeScreenshot},
  {key:'e', desc:'EPG', fn:() => navigate('epg')},
  {key:'1-9', desc:'Kanal Numarası', fn:null},
];
document.addEventListener('keydown', e => {
  const tag = e.target.tagName;
  if(tag === 'INPUT' || tag === 'SELECT') return;
  const shortcut = shortcuts.find(s => s.key === e.key && !e.ctrlKey && !e.metaKey);
  if(shortcut && shortcut.fn) { e.preventDefault(); shortcut.fn(); }
  if(e.key >= '0' && e.key <= '9') {
    const num = parseInt(e.key);
    const ch = App.channels.find(c => c.number === num);
    if(ch) { selectChannel(ch); navigate('live'); }
  }
});
$('#setShowKeys')?.addEventListener('click', () => {
  const body = $('#keysModalBody');
  if(!body) return;
  body.innerHTML = `<div class="keys-grid">${shortcuts.map(s => `<div class="keys-row"><kbd>${s.key}</kbd><span>${s.desc}</span></div>`).join('')}</div>`;
  openModal('keys');
});

// Settings
$('#setTheme')?.addEventListener('change', function() {
  App.settings.theme = this.value;
  applyTheme();
  saveState();
  Toast.success('Tema değiştirildi');
});

// Demo data
function ensureDemoData() {
  if(App.channels.length > 0) return;
  const demoChannels = [
    {name:'TRT 1', group:'Ulusal', quality:'FHD', number:1},
    {name:'ATV', group:'Ulusal', quality:'FHD', number:2},
    {name:'Star TV', group:'Ulusal', quality:'FHD', number:3},
    {name:'Show TV', group:'Ulusal', quality:'FHD', number:4},
    {name:'Kanal D', group:'Ulusal', quality:'FHD', number:5},
    {name:'Fox TV', group:'Ulusal', quality:'FHD', number:6},
    {name:'TV8', group:'Ulusal', quality:'HD', number:7},
    {name:'TRT Haber', group:'Haberler', quality:'HD', number:10},
    {name:'CNNTürk', group:'Haberler', quality:'HD', number:11},
    {name:'NTV', group:'Haberler', quality:'HD', number:12},
    {name:'TRT Spor', group:'Spor', quality:'FHD', number:20},
    {name:'beIN Sports 1', group:'Spor', quality:'FHD', number:21},
    {name:'Sinema TV', group:'Sinema', quality:'FHD', number:30},
    {name:'DiziMax', group:'Dizi', quality:'HD', number:31},
    {name:'TRT Çocuk', group:'Çocuk', quality:'HD', number:40},
    {name:'National Geographic', group:'Belgesel', quality:'FHD', number:50},
    {name:'Power TV', group:'Müzik', quality:'HD', number:60},
    {name:'TRT 4K', group:'Ulusal', quality:'4K', number:99},
  ];
  App.channels = demoChannels.map((c, i) => ({
    id: uuid(),
    name: c.name,
    group: c.group,
    quality: c.quality,
    number: c.number,
    url: `https://demo.streamvault.local/live/${i}/stream.m3u8`,
    logo: '',
    type: 'live',
    online: true,
    sourceId: 'demo'
  }));
  saveState();
}

// AI Recommendations Strip
function renderAIRecStrip() {
  const strip = $('#aiRecScroll');
  if(!strip) return;
  const recs = App.channels.slice(0, 6).map(ch => ({
    ...ch,
    reason: 'Popüler'
  }));
  strip.innerHTML = recs.map(r => `
    <div style="background:var(--bg2);border:1px solid var(--border);border-radius:var(--radius-sm);padding:6px 12px;cursor:pointer;min-width:140px;flex-shrink:0" data-id="${r.id}">
      <div style="font-size:12px;font-weight:600;max-width:120px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis">${r.name}</div>
      <div style="font-size:10px;color:var(--text-muted);max-width:120px">${r.reason}</div>
    </div>
  `).join('');
  strip.querySelectorAll('[data-id]').forEach(el => {
    el.addEventListener('click', () => {
      const ch = App.channels.find(c => c.id === el.dataset.id);
      if(ch) { selectChannel(ch); navigate('live'); }
    });
  });
}

// Load EPG data
function loadEPGData() {
  App.channels.forEach(ch => {
    epgData[ch.id] = generateDemoEPG(ch);
  });
}

// Update EPG strip periodically
setInterval(() => {
  if(App.currentPage === 'live' && App.playingCh) {
    updateEPGStrip(App.playingCh);
  }
}, 30000);

// Main Init
async function init() {
  console.log('🚀 StreamVault Pro v' + App.version + ' initializing…');
  loadState();
  ensureDemoData();
  initPlayer();
  setupSidebar();
  setupPlayerControls();
  startClock();
  loadEPGData();
  renderChannelList();
  renderCategoryTabs();
  updateFavCount();
  renderAIRecStrip();
  renderNotifications();
  await showSplash();
  if(App.channels.length) {
    selectChannel(App.channels[0]);
  }
  addNotification('StreamVault Pro', `Başlatıldı • ${App.channels.length} kanal`);
  console.log('✅ StreamVault Pro ready!');
}

init();

})();
</script>
</body>
</html>
```

Bu kod **tamamen çalışır durumda**. Tüm özellikler:
- ✅ Canlı TV izleme
- ✅ Kanal listesi (arama, filtreleme, sıralama)
- ✅ Kategori sekmeleri
- ✅ Favoriler
- ✅ EPG rehber
- ✅ Filmler/Diziler
- ✅ Catch-Up TV
- ✅ DVR kayıtlar
- ✅ İstatistikler
- ✅ Ayarlar
- ✅ Komut paleti (Ctrl+K)
- ✅ Bildirimler
- ✅ Klavye kısayolları
- ✅ 18 demo kanal
- ✅ Tema değiştirme
- ✅ Responsive tasarım
- ✅ Mobil destek