# CSS Generator Kod Yeniden Yapılandırma

## Prompt 1

### You
*2026-02-07 18:34:56 +03*

<!DOCTYPE html>
<html lang="tr" data-theme="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>K3N4N CSS Stil Generator V6.0 (Ultimate Pro Edition)</title>
    <link href="https://fonts.googleapis.com/css2?family=VT323&family=Press+Start+2P&family=Orbitron:wght@400;700&family=Roboto+Mono:wght@400;700&family=Lobster&family=Kaushan+Script&family=Poppins:wght@300;400;500;600;700&family=Fira+Code:wght@400;700&family=Inter:wght@400;500;600;700&family=Space+Grotesk:wght@400;500;700&family=JetBrains+Mono:wght@400;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/chroma-js/2.4.2/chroma.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/@jaames/iro@5/dist/iro.min.js"></script>
    <style>
       /* ===== RESET & BASE ===== */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

:root {
    --bg-dark: #0b0f1a;
    --bg-surface: #111827;
    --bg-card: #1a2234;
    --bg-elevated: #243049;
    --bg-input: #0f172a;
    --text-white: #f1f5f9;
    --text-light: #cbd5e1;
    --text-muted: #64748b;
    --text-dim: #475569;
    --accent-cyan: #22d3ee;
    --accent-cyan-dim: rgba(34, 211, 238, 0.1);
    --accent-cyan-mid: rgba(34, 211, 238, 0.25);
    --accent-violet: #a78bfa;
    --accent-violet-dim: rgba(167, 139, 250, 0.1);
    --accent-pink: #f472b6;
    --accent-pink-dim: rgba(244, 114, 182, 0.1);
    --accent-amber: #fbbf24;
    --accent-amber-dim: rgba(251, 191, 36, 0.1);
    --accent-green: #34d399;
    --accent-green-dim: rgba(52, 211, 153, 0.1);
    --accent-red: #f87171;
    --accent-red-dim: rgba(248, 113, 113, 0.1);
    --accent-blue: #60a5fa;
    --accent-blue-dim: rgba(96, 165, 250, 0.1);
    --accent-orange: #fb923c;
    --accent-orange-dim: rgba(251, 146, 60, 0.1);
    --border-color: rgba(148, 163, 184, 0.08);
    --border-light: rgba(148, 163, 184, 0.15);
    --border-focus: rgba(34, 211, 238, 0.5);
    --shadow-sm: 0 1px 3px rgba(0, 0, 0, 0.3);
    --shadow-md: 0 4px 16px rgba(0, 0, 0, 0.4);
    --shadow-lg: 0 8px 32px rgba(0, 0, 0, 0.5);
    --shadow-glow: 0 0 20px rgba(34, 211, 238, 0.15);
    --radius-xs: 6px;
    --radius-sm: 8px;
    --radius-md: 12px;
    --radius-lg: 16px;
    --speed-fast: 0.15s;
    --speed-normal: 0.25s;
    --speed-slow: 0.4s;
    --ease-out: cubic-bezier(0.16, 1, 0.3, 1);
    --ease-in-out: cubic-bezier(0.4, 0, 0.2, 1);
}

html {
    scroll-behavior: smooth;
    font-size: 16px;
}

body {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    background: var(--bg-dark);
    color: var(--text-white);
    line-height: 1.5;
    min-height: 100vh;
    overflow-x: hidden;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
}

/* ===== SCROLLBAR ===== */
::-webkit-scrollbar {
    width: 5px;
}

::-webkit-scrollbar-track {
    background: transparent;
}

::-webkit-scrollbar-thumb {
    background: var(--text-dim);
    border-radius: 10px;
}

::-webkit-scrollbar-thumb:hover {
    background: var(--text-muted);
}

/* ===== APP LAYOUT ===== */
.app-layout {
    display: flex;
    min-height: 100vh;
}

/* ========================================
   TOP BAR / HEADER
   ======================================== */
.top-bar {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    height: 54px;
    background: rgba(17, 24, 39, 0.85);
    backdrop-filter: blur(16px) saturate(1.5);
    -webkit-backdrop-filter: blur(16px) saturate(1.5);
    border-bottom: 1px solid var(--border-color);
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0 16px;
    z-index: 1000;
}

.top-bar .logo {
    display: flex;
    align-items: center;
    gap: 10px;
    font-weight: 700;
    font-size: 16px;
    color: var(--accent-cyan);
    text-decoration: none;
    letter-spacing: -0.3px;
}

.top-bar .logo i {
    font-size: 18px;
    filter: drop-shadow(0 0 6px rgba(34, 211, 238, 0.4));
}

.top-bar .logo span {
    background: linear-gradient(135deg, var(--accent-cyan), var(--accent-violet));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

.top-bar-actions {
    display: flex;
    align-items: center;
    gap: 6px;
}

.top-btn {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    width: 36px;
    height: 36px;
    background: var(--bg-card);
    border: 1px solid var(--border-color);
    border-radius: var(--radius-sm);
    color: var(--text-muted);
    font-size: 14px;
    cursor: pointer;
    transition: all var(--speed-normal) var(--ease-out);
}

.top-btn:hover {
    background: var(--bg-elevated);
    color: var(--accent-cyan);
    border-color: var(--border-light);
    transform: translateY(-1px);
}

.top-btn.accent-btn {
    background: linear-gradient(135deg, var(--accent-cyan), #06b6d4);
    color: var(--bg-dark);
    border: none;
    font-weight: 700;
    font-size: 12px;
    width: auto;
    padding: 0 14px;
    gap: 6px;
    font-family: inherit;
}

.top-btn.accent-btn:hover {
    filter: brightness(1.15);
    box-shadow: 0 4px 16px rgba(34, 211, 238, 0.3);
    transform: translateY(-1px);
}

/* HAMBURGER TOGGLE */
.sidebar-toggle-btn {
    display: none;
    align-items: center;
    justify-content: center;
    width: 36px;
    height: 36px;
    background: var(--bg-card);
    border: 1px solid var(--border-color);
    border-radius: var(--radius-sm);
    color: var(--text-light);
    font-size: 16px;
    cursor: pointer;
    transition: all var(--speed-normal) var(--ease-out);
}

.sidebar-toggle-btn:hover {
    color: var(--accent-cyan);
}

/* ========================================
   SIDEBAR
   ======================================== */
.sidebar {
    position: fixed;
    top: 54px;
    left: 0;
    bottom: 0;
    width: 370px;
    background: var(--bg-surface);
    border-right: 1px solid var(--border-color);
    overflow-y: auto;
    overflow-x: hidden;
    z-index: 900;
    padding: 12px;
    padding-bottom: 60px;
    transition: transform var(--speed-slow) var(--ease-out);
}

.sidebar-overlay {
    display: none;
    position: fixed;
    inset: 0;
    background: rgba(0, 0, 0, 0.65);
    backdrop-filter: blur(4px);
    z-index: 899;
}

/* ===== SEARCH ===== */
.search-box {
    position: relative;
    margin-bottom: 12px;
}

.search-box input {
    width: 100%;
    padding: 10px 12px 10px 36px;
    background: var(--bg-input);
    border: 1px solid var(--border-color);
    border-radius: var(--radius-sm);
    color: var(--text-white);
    font-size: 13px;
    font-family: inherit;
    outline: none;
    transition: all var(--speed-normal) var(--ease-out);
}

.search-box input::placeholder {
    color: var(--text-dim);
}

.search-box input:focus {
    border-color: var(--accent-cyan);
    box-shadow: 0 0 0 3px var(--accent-cyan-dim);
}

.search-box i {
    position: absolute;
    left: 12px;
    top: 50%;
    transform: translateY(-50%);
    color: var(--text-dim);
    font-size: 13px;
    pointer-events: none;
}

/* ========================================
   PANELS (ACCORDION)
   ======================================== */
.panel {
    background: var(--bg-card);
    border: 1px solid var(--border-color);
    border-radius: var(--radius-md);
    margin-bottom: 6px;
    transition: all var(--speed-normal) var(--ease-out);
    overflow: visible;
}

.panel:hover {
    border-color: var(--border-light);
}

/* --- PANEL HEADER --- */
.panel-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 12px 14px;
    cursor: pointer;
    user-select: none;
    border-radius: var(--radius-md);
    transition: background var(--speed-fast) var(--ease-in-out);
    -webkit-tap-highlight-color: transparent;
}

.panel-header:hover {
    background: rgba(255, 255, 255, 0.03);
}

.panel-header:active {
    background: rgba(255, 255, 255, 0.05);
}

.panel-header-left {
    display: flex;
    align-items: center;
    gap: 10px;
    min-width: 0;
}

.panel-icon {
    width: 34px;
    height: 34px;
    border-radius: var(--radius-sm);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 14px;
    flex-shrink: 0;
}

/* Panel icon colors */
.panel-icon.pi-font      { background: var(--accent-cyan-dim);    color: var(--accent-cyan); }
.panel-icon.pi-bg        { background: var(--accent-pink-dim);    color: var(--accent-pink); }
.panel-icon.pi-border    { background: var(--accent-amber-dim);   color: var(--accent-amber); }
.panel-icon.pi-radius    { background: var(--accent-blue-dim);    color: var(--accent-blue); }
.panel-icon.pi-shadow    { background: var(--accent-violet-dim);  color: var(--accent-violet); }
.panel-icon.pi-transform { background: var(--accent-orange-dim);  color: var(--accent-orange); }
.panel-icon.pi-animation { background: var(--accent-red-dim);     color: var(--accent-red); }
.panel-icon.pi-filter    { background: var(--accent-green-dim);   color: var(--accent-green); }
.panel-icon.pi-clip      { background: var(--accent-amber-dim);   color: var(--accent-amber); }
.panel-icon.pi-textfill  { background: var(--accent-violet-dim);  color: var(--accent-violet); }
.panel-icon.pi-effect    { background: var(--accent-blue-dim);    color: var(--accent-blue); }
.panel-icon.pi-palette   { background: var(--accent-pink-dim);    color: var(--accent-pink); }
.panel-icon.pi-chaos     { background: var(--accent-red-dim);     color: var(--accent-red); }
.panel-icon.pi-theme     { background: var(--accent-amber-dim);   color: var(--accent-amber); }

.panel-title {
    font-weight: 600;
    font-size: 13px;
    color: var(--text-white);
    line-height: 1.3;
}

.panel-subtitle {
    font-size: 11px;
    color: var(--text-dim);
    line-height: 1.2;
    margin-top: 1px;
}

/* --- PANEL ARROW --- */
.panel-arrow {
    font-size: 11px;
    color: var(--text-dim);
    transition: transform var(--speed-slow) var(--ease-out);
    flex-shrink: 0;
    margin-left: 8px;
}

/* ========================================
   PANEL BODY - AÇILMA / KAPANMA
   Kritik: overflow hidden + max-height
   ======================================== */
.panel-body {
    display: none;
    padding: 0 14px 14px 14px;
}

.panel.expanded > .panel-body {
    display: block;
    animation: panelSlideDown var(--speed-slow) var(--ease-out);
}

.panel.expanded > .panel-header .panel-arrow {
    transform: rotate(180deg);
}

.panel.expanded {
    border-color: var(--border-light);
    box-shadow: var(--shadow-sm), 0 0 0 1px rgba(34, 211, 238, 0.04);
}

.panel.expanded > .panel-header {
    border-bottom: 1px solid var(--border-color);
    border-radius: var(--radius-md) var(--radius-md) 0 0;
    margin-bottom: 2px;
}

@keyframes panelSlideDown {
    0% {
        opacity: 0;
        transform: translateY(-8px);
    }
    100% {
        opacity: 1;
        transform: translateY(0);
    }
}

/* ========================================
   FORM CONTROLS
   ======================================== */

/* --- Control Group --- */
.control-group {
    margin-bottom: 14px;
}

.control-group:last-child {
    margin-bottom: 0;
}

/* --- Label --- */
.control-label {
    display: flex;
    align-items: center;
    justify-content: space-between;
    font-size: 11.5px;
    color: var(--text-muted);
    margin-bottom: 6px;
    font-weight: 500;
}

.control-label .badge {
    background: var(--accent-cyan-dim);
    color: var(--accent-cyan);
    padding: 1px 7px;
    border-radius: 20px;
    font-size: 10.5px;
    font-weight: 700;
    font-family: 'JetBrains Mono', monospace;
}

/* --- Text Input --- */
.form-input {
    width: 100%;
    padding: 9px 12px;
    background: var(--bg-input);
    border: 1px solid var(--border-color);
    border-radius: var(--radius-xs);
    color: var(--text-white);
    font-size: 13px;
    font-family: inherit;
    outline: none;
    transition: all var(--speed-normal) var(--ease-out);
}

.form-input:hover {
    border-color: var(--border-light);
}

.form-input:focus {
    border-color: var(--accent-cyan);
    box-shadow: 0 0 0 3px var(--accent-cyan-dim);
}

/* --- Select --- */
.form-select {
    width: 100%;
    padding: 9px 32px 9px 12px;
    background: var(--bg-input);
    border: 1px solid var(--border-color);
    border-radius: var(--radius-xs);
    color: var(--text-white);
    font-size: 13px;
    font-family: inherit;
    outline: none;
    cursor: pointer;
    appearance: none;
    -webkit-appearance: none;
    background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='12' height='12' viewBox='0 0 24 24' fill='none' stroke='%2364748b' stroke-width='2.5' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpolyline points='6 9 12 15 18 9'%3E%3C/polyline%3E%3C/svg%3E");
    background-repeat: no-repeat;
    background-position: right 10px center;
    transition: all var(--speed-normal) var(--ease-out);
}

.form-select:hover {
    border-color: var(--border-light);
}

.form-select:focus {
    border-color: var(--accent-cyan);
    box-shadow: 0 0 0 3px var(--accent-cyan-dim);
}

.form-select option {
    background: var(--bg-card);
    color: var(--text-white);
}

/* --- Textarea --- */
.form-textarea {
    width: 100%;
    padding: 10px 12px;
    background: var(--bg-input);
    border: 1px solid var(--border-color);
    border-radius: var(--radius-xs);
    color: var(--accent-cyan);
    font-size: 12px;
    font-family: 'JetBrains Mono', 'Fira Code', monospace;
    outline: none;
    resize: vertical;
    min-height: 60px;
    line-height: 1.6;
    transition: all var(--speed-normal) var(--ease-out);
}

.form-textarea:focus {
    border-color: var(--accent-cyan);
    box-shadow: 0 0 0 3px var(--accent-cyan-dim);
}

/* --- Range Slider --- */
.range-group {
    display: flex;
    align-items: center;
    gap: 10px;
}

.range-group input[type="range"] {
    flex: 1;
    -webkit-appearance: none;
    appearance: none;
    height: 4px;
    background: var(--bg-elevated);
    border-radius: 2px;
    outline: none;
    cursor: pointer;
}

.range-group input[type="range"]::-webkit-slider-thumb {
    -webkit-appearance: none;
    width: 16px;
    height: 16px;
    border-radius: 50%;
    background: var(--accent-cyan);
    cursor: pointer;
    border: 2px solid var(--bg-dark);
    box-shadow: 0 0 8px rgba(34, 211, 238, 0.4);
    transition: all var(--speed-fast);
}

.range-group input[type="range"]::-webkit-slider-thumb:hover {
    transform: scale(1.2);
    box-shadow: 0 0 14px rgba(34, 211, 238, 0.6);
}

.range-group input[type="range"]::-moz-range-thumb {
    width: 16px;
    height: 16px;
    border-radius: 50%;
    background: var(--accent-cyan);
    cursor: pointer;
    border: 2px solid var(--bg-dark);
}

/* --- Input Row / Grid --- */
.input-row {
    display: flex;
    gap: 8px;
    align-items: center;
}

.input-row .form-input,
.input-row .form-select {
    flex: 1;
    min-width: 0;
}

.input-row-label {
    font-size: 10px;
    color: var(--text-dim);
    min-width: 16px;
    text-align: center;
    flex-shrink: 0;
}

.input-grid-2 { display: grid; grid-template-columns: 1fr 1fr; gap: 8px; }
.input-grid-3 { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 8px; }
.input-grid-4 { display: grid; grid-template-columns: 1fr 1fr 1fr 1fr; gap: 8px; }

.mini-label {
    display: block;
    font-size: 10px;
    color: var(--text-dim);
    margin-bottom: 3px;
    text-align: center;
}

/* --- Color Picker --- */
.color-picker-wrapper {
    display: flex;
    align-items: center;
    gap: 10px;
}

.color-picker-box {
    width: 42px;
    height: 42px;
    border-radius: var(--radius-sm);
    border: 2px solid var(--border-light);
    cursor: pointer;
    flex-shrink: 0;
    overflow: hidden;
    transition: all var(--speed-normal) var(--ease-out);
}

.color-picker-box:hover {
    border-color: var(--accent-cyan);
    transform: scale(1.08);
    box-shadow: var(--shadow-glow);
}

/* --- Toggle Switch --- */
.toggle-row {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 5px 0;
}

.toggle-row label {
    font-size: 12px;
    color: var(--text-light);
    cursor: pointer;
}

.toggle-switch {
    position: relative;
    width: 40px;
    height: 22px;
    flex-shrink: 0;
}

.toggle-switch input {
    opacity: 0;
    width: 0;
    height: 0;
    position: absolute;
}

.toggle-slider {
    position: absolute;
    inset: 0;
    background: var(--bg-elevated);
    border-radius: 11px;
    cursor: pointer;
    transition: all var(--speed-normal) var(--ease-out);
}

.toggle-slider::before {
    content: '';
    position: absolute;
    left: 3px;
    top: 3px;
    width: 16px;
    height: 16px;
    background: var(--text-dim);
    border-radius: 50%;
    transition: all var(--speed-normal) var(--ease-out);
}

.toggle-switch input:checked + .toggle-slider {
    background: var(--accent-cyan-mid);
}

.toggle-switch input:checked + .toggle-slider::before {
    transform: translateX(18px);
    background: var(--accent-cyan);
    box-shadow: 0 0 8px rgba(34, 211, 238, 0.4);
}

/* --- Small Number Input --- */
input[type="number"].small-input {
    width: 60px;
    padding: 6px 8px;
    background: var(--bg-input);
    border: 1px solid var(--border-color);
    border-radius: var(--radius-xs);
    color: var(--text-white);
    font-size: 12px;
    font-family: 'JetBrains Mono', monospace;
    text-align: center;
    outline: none;
    transition: all var(--speed-normal) var(--ease-out);
}

input[type="number"].small-input:focus {
    border-color: var(--accent-cyan);
    box-shadow: 0 0 0 2px var(--accent-cyan-dim);
}

input[type="number"]::-webkit-inner-spin-button,
input[type="number"]::-webkit-outer-spin-button {
    opacity: 0.3;
}

/* ========================================
   BUTTONS
   ======================================== */
.btn-row {
    display: flex;
    flex-wrap: wrap;
    gap: 6px;
    margin-top: 10px;
}

.btn {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    gap: 5px;
    padding: 7px 14px;
    font-size: 11.5px;
    font-weight: 600;
    font-family: inherit;
    border: 1px solid var(--border-color);
    border-radius: var(--radius-xs);
    cursor: pointer;
    transition: all var(--speed-normal) var(--ease-out);
    white-space: nowrap;
    line-height: 1;
}

.btn-sm { padding: 5px 10px; font-size: 11px; }
.btn-block { width: 100%; }
.btn-icon { width: 32px; height: 32px; padding: 0; }

.btn-default {
    background: var(--bg-elevated);
    color: var(--text-light);
}

.btn-default:hover {
    background: var(--bg-card);
    color: var(--text-white);
    border-color: var(--border-light);
    transform: translateY(-1px);
}

.btn-accent {
    background: var(--accent-cyan-dim);
    color: var(--accent-cyan);
    border-color: rgba(34, 211, 238, 0.2);
}

.btn-accent:hover {
    background: var(--accent-cyan-mid);
    border-color: var(--accent-cyan);
    transform: translateY(-1px);
    box-shadow: 0 4px 12px rgba(34, 211, 238, 0.15);
}

.btn-danger {
    background: var(--accent-red-dim);
    color: var(--accent-red);
    border-color: rgba(248, 113, 113, 0.2);
}

.btn-danger:hover {
    background: rgba(248, 113, 113, 0.2);
    border-color: var(--accent-red);
    transform: translateY(-1px);
}

.btn-pink {
    background: var(--accent-pink-dim);
    color: var(--accent-pink);
    border-color: rgba(244, 114, 182, 0.2);
}

.btn-pink:hover {
    background: rgba(244, 114, 182, 0.2);
    border-color: var(--accent-pink);
    transform: translateY(-1px);
}

.btn-gold {
    background: var(--accent-amber-dim);
    color: var(--accent-amber);
    border-color: rgba(251, 191, 36, 0.2);
}

.btn-gold:hover {
    background: rgba(251, 191, 36, 0.2);
    border-color: var(--accent-amber);
    transform: translateY(-1px);
}

/* ========================================
   MAIN CONTENT AREA
   ======================================== */
.main-content {
    margin-left: 370px;
    margin-top: 54px;
    flex: 1;
    padding: 20px;
    display: flex;
    flex-direction: column;
    gap: 20px;
    min-height: calc(100vh - 54px);
}

/* ===== PREVIEW SECTION ===== */
.preview-section {
    background: var(--bg-surface);
    border: 1px solid var(--border-color);
    border-radius: var(--radius-lg);
    padding: 20px;
    flex-shrink: 0;
}

.preview-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 16px;
}

.preview-title {
    font-size: 14px;
    font-weight: 600;
    color: var(--text-white);
    display: flex;
    align-items: center;
    gap: 8px;
}

.preview-title i {
    color: var(--accent-cyan);
}

.preview-dimensions {
    font-size: 11px;
    color: var(--text-dim);
    background: var(--bg-card);
    padding: 3px 10px;
    border-radius: 20px;
    font-family: 'JetBrains Mono', monospace;
}

.preview-container {
    background: var(--bg-card);
    border-radius: var(--radius-md);
    min-height: 280px;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 30px;
    position: relative;
    overflow: hidden;
    border: 1px solid var(--border-color);
}

.preview-container::before {
    content: '';
    position: absolute;
    inset: 0;
    background-image:
        linear-gradient(45deg, rgba(255,255,255,0.015) 25%, transparent 25%),
        linear-gradient(-45deg, rgba(255,255,255,0.015) 25%, transparent 25%),
        linear-gradient(45deg, transparent 75%, rgba(255,255,255,0.015) 75%),
        linear-gradient(-45deg, transparent 75%, rgba(255,255,255,0.015) 75%);
    background-size: 20px 20px;
    background-position: 0 0, 0 10px, 10px -10px, -10px 0px;
    pointer-events: none;
}

#preview-box {
    font-family: 'Poppins', sans-serif;
    font-size: 30px;
    color: var(--accent-cyan);
    padding: 25px 40px;
    position: relative;
    z-index: 1;
    word-break: break-word;
    text-align: center;
    min-width: 180px;
}

/* ===== TEXT INPUT ===== */
.text-input-section {
    display: flex;
    gap: 10px;
    align-items: center;
    margin-top: 12px;
}

.text-input-section input {
    flex: 1;
    padding: 10px 14px;
    background: var(--bg-input);
    border: 1px solid var(--border-color);
    border-radius: var(--radius-xs);
    color: var(--text-white);
    font-size: 13px;
    font-family: inherit;
    outline: none;
    transition: all var(--speed-normal) var(--ease-out);
}

.text-input-section input:focus {
    border-color: var(--accent-cyan);
    box-shadow: 0 0 0 3px var(--accent-cyan-dim);
}

.char-count {
    font-size: 11px;
    color: var(--text-dim);
    flex-shrink: 0;
    font-family: 'JetBrains Mono', monospace;
}

/* ===== OUTPUT SECTION ===== */
.output-section {
    background: var(--bg-surface);
    border: 1px solid var(--border-color);
    border-radius: var(--radius-lg);
    overflow: hidden;
    flex: 1;
}

.output-tabs {
    display: flex;
    border-bottom: 1px solid var(--border-color);
    background: rgba(0, 0, 0, 0.15);
}

.output-tab {
    padding: 11px 20px;
    font-size: 12.5px;
    font-weight: 600;
    color: var(--text-dim);
    cursor: pointer;
    border: none;
    background: none;
    transition: all var(--speed-normal) var(--ease-out);
    position: relative;
    font-family: inherit;
}

.output-tab:hover {
    color: var(--text-light);
    background: rgba(255, 255, 255, 0.03);
}

.output-tab.active {
    color: var(--accent-cyan);
}

.output-tab.active::after {
    content: '';
    position: absolute;
    bottom: 0;
    left: 8px;
    right: 8px;
    height: 2px;
    background: var(--accent-cyan);
    border-radius: 2px 2px 0 0;
}

.tab-content {
    display: none;
    padding: 16px;
}

.tab-content.active {
    display: block;
}

.output-textarea {
    width: 100%;
    min-height: 180px;
    padding: 14px;
    background: var(--bg-dark);
    border: 1px solid var(--border-color);
    border-radius: var(--radius-sm);
    color: var(--accent-cyan);
    font-family: 'JetBrains Mono', 'Fira Code', monospace;
    font-size: 12px;
    line-height: 1.7;
    resize: vertical;
    outline: none;
    transition: all var(--speed-normal) var(--ease-out);
}

.output-textarea:focus {
    border-color: var(--accent-cyan);
    box-shadow: 0 0 0 3px var(--accent-cyan-dim);
}

.output-actions {
    display: flex;
    gap: 6px;
    margin-top: 10px;
    flex-wrap: wrap;
}

/* ===== FEEDBACK MESSAGES ===== */
.feedback-msg {
    display: none;
    padding: 6px 12px;
    border-radius: var(--radius-xs);
    font-size: 12px;
    margin-top: 8px;
    font-weight: 500;
}

.feedback-msg.visible {
    display: inline-block;
}

.feedback-success {
    background: var(--accent-green-dim);
    color: var(--accent-green);
    border: 1px solid rgba(52, 211, 153, 0.2);
}

.feedback-error {
    background: var(--accent-red-dim);
    color: var(--accent-red);
    border: 1px solid rgba(248, 113, 113, 0.2);
}

/* ========================================
   GRADIENT EDITOR
   ======================================== */
.gradient-stops {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
    margin-top: 8px;
}

.gradient-stop {
    display: flex;
    align-items: center;
    gap: 6px;
    background: var(--bg-input);
    padding: 6px 10px;
    border-radius: var(--radius-xs);
    border: 1px solid var(--border-color);
}

.gradient-stop .color-dot {
    width: 24px;
    height: 24px;
    border-radius: var(--radius-xs);
    border: 2px solid var(--border-light);
    cursor: pointer;
}

.gradient-stop input[type="number"] {
    width: 50px;
    padding: 4px 6px;
    background: var(--bg-dark);
    border: 1px solid var(--border-color);
    border-radius: 4px;
    color: var(--text-white);
    font-size: 11px;
    text-align: center;
    outline: none;
    font-family: 'JetBrains Mono', monospace;
}

.gradient-stop input[type="number"]:focus {
    border-color: var(--accent-cyan);
}

.add-stop-btn {
    width: 28px;
    height: 28px;
    display: flex;
    align-items: center;
    justify-content: center;
    background: var(--accent-cyan-dim);
    color: var(--accent-cyan);
    border: 1px dashed rgba(34, 211, 238, 0.4);
    border-radius: var(--radius-xs);
    cursor: pointer;
    font-size: 14px;
    transition: all var(--speed-normal) var(--ease-out);
}

.add-stop-btn:hover {
    background: var(--accent-cyan-mid);
    border-style: solid;
}

/* ========================================
   THEME PRESETS GRID
   ======================================== */
.theme-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 6px;
}

.theme-btn {
    padding: 10px 8px;
    border-radius: var(--radius-sm);
    border: 1px solid var(--border-color);
    cursor: pointer;
    text-align: center;
    font-size: 11px;
    font-weight: 600;
    font-family: inherit;
    transition: all var(--speed-normal) var(--ease-out);
}

.theme-btn:hover {
    transform: translateY(-2px);
    box-shadow: var(--shadow-md);
}

.theme-btn:active {
    transform: translateY(0);
}

.theme-neon        { background: #0a0a2e; color: #0ff; border-color: rgba(0,255,255,0.2); }
.theme-minimal     { background: #fafafa; color: #333; border-color: #ddd; }
.theme-vintage     { background: #f4e9d8; color: #5c3317; border-color: #c49a6c; }
.theme-glass       { background: rgba(255,255,255,0.06); color: #fff; border-color: rgba(255,255,255,0.15); }
.theme-neumorphism { background: #e0e5ec; color: #6b7b99; border-color: #ccd3dd; }
.theme-cyberpunk   { background: #0d0221; color: #ff2d6a; border-color: rgba(255,45,106,0.25); }
.theme-nature      { background: #e8f5e9; color: #2d5016; border-color: #81c784; }
.theme-ocean       { background: linear-gradient(135deg, #0077b6, #023e8a); color: #fff; border-color: transparent; }
.theme-sunset      { background: linear-gradient(135deg, #ff512f, #f09819); color: #fff; border-color: transparent; }
.theme-elegant     { background: #1a1a2e; color: #d4af37; border-color: rgba(212,175,55,0.2); }

/* ========================================
   PALETTE PREVIEW
   ======================================== */
.palette-preview {
    display: flex;
    gap: 4px;
    margin-top: 10px;
    flex-wrap: wrap;
}

.palette-color {
    width: 44px;
    height: 44px;
    border-radius: var(--radius-sm);
    cursor: pointer;
    position: relative;
    transition: all var(--speed-normal) var(--ease-out);
    border: 2px solid transparent;
}

.palette-color:hover {
    transform: scale(1.15);
    border-color: var(--text-white);
    z-index: 1;
    box-shadow: var(--shadow-md);
}

.palette-color .tooltip {
    position: absolute;
    bottom: -24px;
    left: 50%;
    transform: translateX(-50%);
    background: var(--bg-dark);
    color: var(--text-white);
    padding: 2px 8px;
    border-radius: 4px;
    font-size: 10px;
    font-family: 'JetBrains Mono', monospace;
    white-space: nowrap;
    opacity: 0;
    pointer-events: none;
    transition: opacity var(--speed-fast);
    border: 1px solid var(--border-color);
}

.palette-color:hover .tooltip {
    opacity: 1;
}

/* ========================================
   CHAOS SECTION
   ======================================== */
.chaos-checks {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 6px;
    margin-bottom: 10px;
}

.chaos-check {
    display: flex;
    align-items: center;
    gap: 6px;
    font-size: 11px;
    color: var(--text-light);
    cursor: pointer;
}

.chaos-check input[type="checkbox"] {
    accent-color: var(--accent-cyan);
    width: 14px;
    height: 14px;
    cursor: pointer;
}

/* ========================================
   DIVIDER & SECTION DIVIDER
   ======================================== */
.divider {
    height: 1px;
    background: var(--border-color);
    margin: 12px 0;
}

.section-divider {
    display: flex;
    align-items: center;
    gap: 10px;
    margin: 14px 0 8px;
    font-size: 10px;
    color: var(--text-dim);
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 1px;
}

.section-divider::before,
.section-divider::after {
    content: '';
    flex: 1;
    height: 1px;
    background: var(--border-color);
}

/* ========================================
   TOAST NOTIFICATIONS
   ======================================== */
.toast-container {
    position: fixed;
    bottom: 20px;
    right: 20px;
    z-index: 9999;
    display: flex;
    flex-direction: column-reverse;
    gap: 8px;
    pointer-events: none;
}

.toast {
    padding: 10px 18px;
    background: var(--bg-card);
    border: 1px solid var(--border-color);
    border-radius: var(--radius-sm);
    color: var(--text-white);
    font-size: 13px;
    font-weight: 500;
    box-shadow: var(--shadow-lg);
    display: flex;
    align-items: center;
    gap: 8px;
    animation: toastIn 0.4s var(--ease-out);
    max-width: 340px;
    pointer-events: all;
    backdrop-filter: blur(12px);
}

.toast.toast-success { border-left: 3px solid var(--accent-green); }
.toast.toast-error   { border-left: 3px solid var(--accent-red); }
.toast.toast-info    { border-left: 3px solid var(--accent-blue); }

.toast.removing {
    animation: toastOut 0.3s var(--ease-out) forwards;
}

@keyframes toastIn {
    from { opacity: 0; transform: translateX(40px) scale(0.95); }
    to   { opacity: 1; transform: translateX(0) scale(1); }
}

@keyframes toastOut {
    from { opacity: 1; transform: translateX(0) scale(1); }
    to   { opacity: 0; transform: translateX(40px) scale(0.95); }
}

/* ========================================
   HIDDEN UTILITIES
   ======================================== */
input[type="file"].hidden-input {
    display: none;
}

/* ========================================
   RESPONSIVE - TABLET
   ======================================== */
@media (max-width: 1024px) {
    .sidebar {
        transform: translateX(-100%);
        width: 340px;
    }

    .sidebar.open {
        transform: translateX(0);
        box-shadow: var(--shadow-lg);
    }

    .sidebar-overlay.visible {
        display: block;
    }

    .sidebar-toggle-btn {
        display: flex;
    }

    .main-content {
        margin-left: 0;
    }
}

/* ========================================
   RESPONSIVE - MOBILE
   ======================================== */
@media (max-width: 640px) {
    .sidebar {
        width: 100%;
    }

    .top-bar {
        padding: 0 12px;
    }

    .top-btn.accent-btn span {
        display: none;
    }

    .main-content {
        padding: 12px;
    }

    .preview-container {
        min-height: 200px;
        padding: 20px;
    }

    #preview-box {
        font-size: 22px;
        padding: 20px 24px;
    }

    .theme-grid {
        grid-template-columns: 1fr;
    }

    .input-grid-4 {
        grid-template-columns: 1fr 1fr;
    }

    .output-tabs {
        overflow-x: auto;
    }

    .output-tab {
        padding: 10px 14px;
        font-size: 12px;
    }
}

/* ========================================
   PRINT
   ======================================== */
@media print {
    .sidebar,
    .top-bar,
    .toast-container {
        display: none !important;
    }
    .main-content {
        margin: 0;
        padding: 0;
    }
}
    </style>
</head>
<body>
    <!-- TOAST CONTAINER -->
    <div class="toast-container" id="toastContainer"></div>

    <!-- HEADER -->
    <header class="app-header">
        <a class="logo" href="#">
            <i class="fas fa-wand-magic-sparkles"></i>
            <span>K3N4N CSS Generator V6.0</span>
        </a>
        <div class="header-actions">
            <button class="header-btn" data-action="undo" disabled data-tooltip="Geri Al (Ctrl+Z)"><i class="fas fa-undo-alt"></i> Geri</button>
            <button class="header-btn" data-action="redo" disabled data-tooltip="İleri Al (Ctrl+Y)"><i class="fas fa-redo-alt"></i> İleri</button>
            <button class="header-btn theme-btn" data-action="toggle-theme" data-tooltip="Tema Değiştir"><i class="fas fa-moon"></i></button>
            <button class="header-btn reset-btn" data-action="reset-all" data-tooltip="Tümünü Sıfırla"><i class="fas fa-trash-restore"></i> Sıfırla</button>
        </div>
    </header>

    <!-- MOBILE SIDEBAR TOGGLE -->
    <button class="sidebar-toggle" id="sidebarToggle" aria-label="Menüyü aç/kapat"><i class="fas fa-sliders-h"></i></button>
    <div class="sidebar-overlay" id="sidebarOverlay"></div>

    <!-- MAIN LAYOUT -->
    <div class="app-container">
        <!-- SIDEBAR -->
        <aside class="sidebar" id="sidebar">
            <div class="sidebar-search">
                <i class="fas fa-search"></i>
                <input type="text" id="panelSearch" placeholder="Panel ara... (metin, arka plan, çerçeve...)" aria-label="Panel arama">
            </div>

            <!-- 1. METIN STİLLERİ -->
            <div class="panel expanded" data-panel="text">
                <div class="panel-header">
                    <div class="panel-icon text"><i class="fas fa-font"></i></div>
                    <span class="panel-title">Metin Stilleri</span>
                    <i class="fas fa-chevron-up panel-toggle"></i>
                </div>
                <div class="panel-body">
                    <div class="btn-grid">
                        <button class="style-btn" data-style-target="random-font"><i class="fas fa-dice"></i> Rnd Font</button>
                        <button class="style-btn" data-style-target="random-color"><i class="fas fa-palette"></i> Rnd Renk</button>
                        <button class="style-btn" data-style-target="random-text-shadow"><i class="fas fa-clone"></i> Rnd Gölge</button>
                        <button class="style-btn" data-style-target="random-text-decoration"><i class="fas fa-underline"></i> Rnd Dekor</button>
                        <button class="style-btn" data-style-target="random-spacing"><i class="fas fa-arrows-alt-h"></i> Rnd Boşluk</button>
                        <button class="style-btn" data-style-target="random-align"><i class="fas fa-align-center"></i> Rnd Hiza</button>
                        <button class="style-btn" data-style-target="random-line-height"><i class="fas fa-text-height"></i> Rnd Satır</button>
                        <button class="style-btn" data-style-target="random-text-transform"><i class="fas fa-text-width"></i> Rnd Dönüşüm</button>
                    </div>
                    <div class="separator"></div>
                    <div class="form-group">
                        <label for="fontFamily">Yazı Fontu</label>
                        <select id="fontFamily" data-style-prop="fontFamily">
                            <option value="'Poppins', sans-serif">Poppins</option>
                            <option value="'Inter', sans-serif">Inter</option>
                            <option value="'Space Grotesk', sans-serif">Space Grotesk</option>
                            <option value="'VT323', monospace">VT323</option>
                            <option value="'Press Start 2P', monospace">Press Start 2P</option>
                            <option value="'Orbitron', sans-serif">Orbitron</option>
                            <option value="'Roboto Mono', monospace">Roboto Mono</option>
                            <option value="'JetBrains Mono', monospace">JetBrains Mono</option>
                            <option value="'Lobster', cursive">Lobster</option>
                            <option value="'Kaushan Script', cursive">Kaushan Script</option>
                            <option value="'Fira Code', monospace">Fira Code</option>
                            <option value="Georgia, serif">Georgia</option>
                            <option value="'Courier New', monospace">Courier New</option>
                            <option value="Impact, sans-serif">Impact</option>
                        </select>
                    </div>
                    <div class="form-group">
                        <label>Yazı Boyutu <span class="value-badge" id="fontSizeVal">30px</span></label>
                        <input type="range" id="fontSizeRange" min="8" max="120" value="30">
                        <input type="number" id="fontSize" data-style-prop="fontSize" data-style-unit="px" value="30" min="1" max="200">
                    </div>
                    <div class="form-group">
                        <label>Font Weight <span class="value-badge" id="fontWeightVal">400</span></label>
                        <input type="range" id="fontWeightRange" min="100" max="900" step="100" value="400">
                        <select id="fontWeight" data-style-prop="fontWeight">
                            <option value="100">100 - Thin</option>
                            <option value="200">200 - Extra Light</option>
                            <option value="300">300 - Light</option>
                            <option value="400" selected>400 - Normal</option>
                            <option value="500">500 - Medium</option>
                            <option value="600">600 - Semi Bold</option>
                            <option value="700">700 - Bold</option>
                            <option value="800">800 - Extra Bold</option>
                            <option value="900">900 - Black</option>
                        </select>
                    </div>
                    <div class="form-group">
                        <label>Yazı Rengi</label>
                        <div id="textColorPicker" class="color-picker-container"></div>
                    </div>
                    <div class="form-group">
                        <label>Yazı Gölgesi</label>
                        <div class="form-row">
                            <label>X:</label><input type="number" id="textShadowX" value="0">
                            <label>Y:</label><input type="number" id="textShadowY" value="0">
                            <label>Blur:</label><input type="number" id="textShadowBlur" value="0" min="0">
                        </div>
                        <div id="textShadowColorPicker" class="color-picker-container"></div>
                    </div>
                    <div class="form-group">
                        <label>Dekorasyon</label>
                        <div class="form-row">
                            <select id="textDecorationLine" data-style-prop="textDecorationLine">
                                <option value="none" selected>Yok</option>
                                <option value="underline">Altı Çizili</option>
                                <option value="overline">Üstü Çizili</option>
                                <option value="line-through">Üzerinden</option>
                            </select>
                            <select id="textDecorationStyle" data-style-prop="textDecorationStyle">
                                <option value="solid" selected>Düz</option>
                                <option value="double">Çift</option>
                                <option value="dotted">Noktalı</option>
                                <option value="dashed">Kesikli</option>
                                <option value="wavy">Dalgalı</option>
                            </select>
                        </div>
                    </div>
                    <div class="form-group">
                        <label for="textAlign">Hizalama</label>
                        <select id="textAlign" data-style-prop="textAlign">
                            <option value="left">Sola</option>
                            <option value="center" selected>Ortala</option>
                            <option value="right">Sağa</option>
                            <option value="justify">İki Yana</option>
                        </select>
                    </div>
                    <div class="form-group">
                        <label>Satır Yüksekliği <span class="value-badge" id="lineHeightVal">1.5</span></label>
                        <input type="range" id="lineHeightRange" min="0.5" max="4" step="0.1" value="1.5">
                    </div>
                    <div class="form-group">
                        <label>Boşluklar</label>
                        <div class="form-row">
                            <label>Harf:</label><input type="number" id="letterSpacing" data-style-prop="letterSpacing" data-style-unit="px" value="0" step="0.5">
                            <label>Kelime:</label><input type="number" id="wordSpacing" data-style-prop="wordSpacing" data-style-unit="px" value="0" step="0.5">
                        </div>
                    </div>
                    <div class="form-group">
                        <label>Padding</label>
                        <div class="form-row">
                            <label>Sol:</label><input type="number" id="paddingLeft" value="0" min="0">
                            <label>Sağ:</label><input type="number" id="paddingRight" value="0" min="0">
                            <label>Üst:</label><input type="number" id="paddingTop" value="0" min="0">
                            <label>Alt:</label><input type="number" id="paddingBottom" value="0" min="0">
                        </div>
                        <select id="paddingUnit">
                            <option value="px" selected>px</option>
                            <option value="%">%</option>
                            <option value="rem">rem</option>
                            <option value="em">em</option>
                        </select>
                    </div>
                    <div class="form-group">
                        <label for="textTransform">Metin Dönüşümü</label>
                        <select id="textTransform" data-style-prop="textTransform">
                            <option value="none" selected>Yok</option>
                            <option value="uppercase">BÜYÜK HARF</option>
                            <option value="lowercase">küçük harf</option>
                            <option value="capitalize">Baş Harf Büyük</option>
                        </select>
                    </div>
                    <div class="form-group">
                        <label for="fontStyle">Font Stili</label>
                        <select id="fontStyle" data-style-prop="fontStyle">
                            <option value="normal" selected>Normal</option>
                            <option value="italic">İtalik</option>
                            <option value="oblique">Eğik</option>
                        </select>
                    </div>
                    <div class="form-group">
                        <label for="writingMode">Yazı Yönü</label>
                        <select id="writingMode" data-style-prop="writingMode">
                            <option value="horizontal-tb" selected>Yatay (Normal)</option>
                            <option value="vertical-rl">Dikey (Sağ-Sol)</option>
                            <option value="vertical-lr">Dikey (Sol-Sağ)</option>
                        </select>
                    </div>
                    <div class="form-group">
                        <label for="textOverflow">Taşma Davranışı</label>
                        <select id="textOverflow" data-style-prop="textOverflow">
                            <option value="clip" selected>Kes</option>
                            <option value="ellipsis">Üç Nokta (...)</option>
                        </select>
                    </div>
                </div>
            </div>

            <!-- 2. ARKA PLAN -->
            <div class="panel" data-panel="background">
                <div class="panel-header">
                    <div class="panel-icon bg"><i class="fas fa-fill-drip"></i></div>
                    <span class="panel-title">Arka Plan</span>
                    <i class="fas fa-chevron-up panel-toggle"></i>
                </div>
                <div class="panel-body">
                    <div class="btn-grid">
                        <button class="style-btn" data-style-target="random-bg-color"><i class="fas fa-fill"></i> Rnd Renk</button>
                        <button class="style-btn" data-style-target="random-gradient"><i class="fas fa-grip-lines"></i> Rnd Gradyan</button>
                        <button class="style-btn" data-style-target="random-bg-gif"><i class="fas fa-film"></i> Rnd GIF</button>
                        <button class="style-btn" data-style-target="random-bg-position"><i class="fas fa-arrows-alt"></i> Rnd Konum</button>
                        <button class="style-btn" data-style-target="random-bg-size"><i class="fas fa-expand"></i> Rnd Boyut</button>
                        <button class="style-btn" data-style-target="random-bg-opacity"><i class="fas fa-adjust"></i> Rnd Opaklık</button>
                        <button class="style-btn" data-style-target="random-bg-pattern"><i class="fas fa-th"></i> Rnd Desen</button>
                        <button class="style-btn" data-style-target="random-bg-blend"><i class="fas fa-layer-group"></i> Rnd Karıştırma</button>
                    </div>
                    <div class="separator"></div>
                    <div class="form-group">
                        <label>Arka Plan Rengi</label>
                        <div id="backgroundColorPicker" class="color-picker-container"></div>
                    </div>
                    <div class="form-group">
                        <label>Opaklık <span class="value-badge" id="bgOpacityVal">1</span></label>
                        <input type="range" id="backgroundOpacityRange" min="0" max="1" step="0.05" value="1">
                    </div>
                    <div class="form-group">
                        <label>GIF/Resim URL</label>
                        <input type="text" id="backgroundImageUrl" placeholder="URL girin...">
                    </div>
                    <div class="form-group">
                        <label>Konum</label>
                        <div class="form-row">
                            <label>X:</label><input type="text" id="backgroundPositionX" placeholder="center">
                            <label>Y:</label><input type="text" id="backgroundPositionY" placeholder="center">
                        </div>
                    </div>
                    <div class="form-group">
                        <label>Boyut</label>
                        <select id="backgroundSize" data-style-prop="backgroundSize">
                            <option value="auto" selected>Otomatik</option>
                            <option value="cover">Kapla</option>
                            <option value="contain">İçer</option>
                            <option value="100% 100%">100% 100%</option>
                            <option value="50% 50%">50% 50%</option>
                        </select>
                    </div>
                    <div class="form-group">
                        <label>Tekrar</label>
                        <select id="backgroundRepeat" data-style-prop="backgroundRepeat">
                            <option value="repeat" selected>Tekrarla</option>
                            <option value="no-repeat">Tekrarlama</option>
                            <option value="repeat-x">Yatay Tekrar</option>
                            <option value="repeat-y">Dikey Tekrar</option>
                        </select>
                    </div>
                    <div class="form-group">
                        <label>Karıştırma Modu</label>
                        <select id="backgroundBlendMode" data-style-prop="backgroundBlendMode">
                            <option value="normal" selected>Normal</option>
                            <option value="multiply">Çarpma</option>
                            <option value="screen">Ekran</option>
                            <option value="overlay">Kaplama</option>
                            <option value="darken">Koyulaştır</option>
                            <option value="lighten">Aydınlat</option>
                            <option value="color-dodge">Renk Etkisi</option>
                            <option value="difference">Fark</option>
                            <option value="hue">Ton</option>
                            <option value="saturation">Doygunluk</option>
                        </select>
                    </div>
                    <div class="separator"></div>
                    <div class="form-group">
                        <label>Gradyan Düzenleyici</label>
                        <div class="form-row">
                            <label>Yön:</label><input type="number" id="gradientAngle" value="90" min="0" max="360">
                            <label>Tür:</label>
                            <select id="gradientType">
                                <option value="linear" selected>Doğrusal</option>
                                <option value="radial">Radyal</option>
                                <option value="conic">Konik</option>
                            </select>
                        </div>
                        <div id="gradientColors" class="gradient-colors"></div>
                        <button class="add-color-btn" id="addGradientColor"><i class="fas fa-plus"></i> Renk Ekle</button>
                    </div>
                </div>
            </div>

            <!-- 3. ÇERÇEVE -->
            <div class="panel" data-panel="border">
                <div class="panel-header">
                    <div class="panel-icon border"><i class="fas fa-border-all"></i></div>
                    <span class="panel-title">Çerçeve & Kenarlar</span>
                    <i class="fas fa-chevron-up panel-toggle"></i>
                </div>
                <div class="panel-body">
                    <div class="btn-grid">
                        <button class="style-btn" data-style-target="random-multi-border"><i class="fas fa-border-style"></i> Rnd Çerçeve</button>
                        <button class="style-btn" data-style-target="random-outline"><i class="fas fa-square"></i> Rnd Dış Çizgi</button>
                        <button class="style-btn" data-style-target="random-border-radius"><i class="fas fa-circle"></i> Rnd Yuvarla</button>
                        <button class="style-btn" data-style-target="random-border-color"><i class="fas fa-palette"></i> Rnd Renk</button>
                    </div>
                    <div class="separator"></div>
                    <div class="form-group">
                        <label>Kenar Genişliği</label>
                        <div class="form-row">
                            <label>Üst:</label><input type="text" id="borderTop" data-style-prop="borderTop" placeholder="2px solid #000">
                            <label>Alt:</label><input type="text" id="borderBottom" data-style-prop="borderBottom" placeholder="2px solid #000">
                        </div>
                        <div class="form-row">
                            <label>Sol:</label><input type="text" id="borderLeft" data-style-prop="borderLeft" placeholder="2px solid #000">
                            <label>Sağ:</label><input type="text" id="borderRight" data-style-prop="borderRight" placeholder="2px solid #000">
                        </div>
                    </div>
                    <div class="form-group">
                        <label>Yuvarlak Kenarlar <span class="value-badge" id="borderRadiusVal">0px</span></label>
                        <input type="range" id="borderRadiusAll" min="0" max="200" value="0">
                        <div class="form-row">
                            <label>ÜS:</label><input type="number" id="borderRadiusTopLeft" data-style-prop="borderTopLeftRadius" data-style-unit="px" value="0" min="0">
                            <label>ÜSa:</label><input type="number" id="borderRadiusTopRight" data-style-prop="borderTopRightRadius" data-style-unit="px" value="0" min="0">
                        </div>
                        <div class="form-row">
                            <label>AS:</label><input type="number" id="borderRadiusBottomLeft" data-style-prop="borderBottomLeftRadius" data-style-unit="px" value="0" min="0">
                            <label>ASa:</label><input type="number" id="borderRadiusBottomRight" data-style-prop="borderBottomRightRadius" data-style-unit="px" value="0" min="0">
                        </div>
                    </div>
                    <div class="form-group">
                        <label>Dış Çizgi (Outline)</label>
                        <div class="form-row">
                            <label>Genişlik:</label><input type="number" id="outlineWidth" data-style-prop="outlineWidth" data-style-unit="px" value="0" min="0">
                            <label>Stil:</label>
                            <select id="outlineStyle" data-style-prop="outlineStyle">
                                <option value="none" selected>Yok</option>
                                <option value="solid">Düz</option>
                                <option value="dashed">Kesik</option>
                                <option value="dotted">Noktalı</option>
                                <option value="double">Çift</option>
                                <option value="groove">Oluk</option>
                                <option value="ridge">Çıkıntı</option>
                            </select>
                        </div>
                        <div id="outlineColorPicker" class="color-picker-container"></div>
                    </div>
                    <div class="form-group">
                        <label>Outline Offset</label>
                        <input type="number" id="outlineOffset" data-style-prop="outlineOffset" data-style-unit="px" value="0">
                    </div>
                </div>
            </div>

            <!-- 4. DÖNÜŞÜM -->
            <div class="panel" data-panel="transform">
                <div class="panel-header">
                    <div class="panel-icon transform"><i class="fas fa-cube"></i></div>
                    <span class="panel-title">Dönüşüm (Transform)</span>
                    <i class="fas fa-chevron-up panel-toggle"></i>
                </div>
                <div class="panel-body">
                    <div class="btn-grid">
                        <button class="style-btn" data-style-target="random-transform"><i class="fas fa-sync"></i> Rnd Dönüşüm</button>
                        <button class="style-btn" data-style-target="reset-transform"><i class="fas fa-undo"></i> Sıfırla</button>
                    </div>
                    <div class="separator"></div>
                    <div class="form-group">
                        <label>Döndür <span class="value-badge" id="rotateVal">0°</span></label>
                        <input type="range" id="rotateRange" min="-360" max="360" value="0">
                        <input type="number" id="rotate" value="0">
                    </div>
                    <div class="form-group">
                        <label>Ölçek <span class="value-badge" id="scaleVal">1</span></label>
                        <input type="range" id="scaleRange" min="0.1" max="3" step="0.05" value="1">
                    </div>
                    <div class="form-group">
                        <label>Eğme</label>
                        <div class="form-row">
                            <label>X:</label><input type="number" id="skewX" value="0">
                            <label>Y:</label><input type="number" id="skewY" value="0">
                        </div>
                    </div>
                    <div class="form-group">
                        <label>Taşıma (Translate)</label>
                        <div class="form-row">
                            <label>X:</label><input type="number" id="translateX" value="0">
                            <label>Y:</label><input type="number" id="translateY" value="0">
                        </div>
                    </div>
                    <div class="form-group">
                        <label>Transform Origin</label>
                        <select id="transformOrigin" data-style-prop="transformOrigin">
                            <option value="center center" selected>Orta</option>
                            <option value="top left">Üst Sol</option>
                            <option value="top right">Üst Sağ</option>
                            <option value="bottom left">Alt Sol</option>
                            <option value="bottom right">Alt Sağ</option>
                            <option value="top center">Üst Orta</option>
                            <option value="bottom center">Alt Orta</option>
                        </select>
                    </div>
                </div>
            </div>

            <!-- 5. KUTU GÖLGESİ -->
            <div class="panel" data-panel="shadow">
                <div class="panel-header">
                    <div class="panel-icon shadow"><i class="fas fa-clone"></i></div>
                    <span class="panel-title">Kutu Gölgesi</span>
                    <i class="fas fa-chevron-up panel-toggle"></i>
                </div>
                <div class="panel-body">
                    <div class="btn-grid">
                        <button class="style-btn" data-style-target="random-box-shadow"><i class="fas fa-clone"></i> Rnd Gölge</button>
                        <button class="style-btn" data-style-target="random-box-shadow-color"><i class="fas fa-palette"></i> Rnd Renk</button>
                        <button class="style-btn" data-style-target="random-multi-shadow"><i class="fas fa-layer-group"></i> Rnd Çoklu</button>
                        <button class="style-btn" data-style-target="random-inset-shadow"><i class="fas fa-compress-alt"></i> Rnd İç Gölge</button>
                    </div>
                    <div class="separator"></div>
                    <div class="form-group">
                        <label>Gölge Ayarları</label>
                        <div class="form-row">
                            <label>X:</label><input type="number" id="boxShadowX" value="0">
                            <label>Y:</label><input type="number" id="boxShadowY" value="4">
                            <label>Blur:</label><input type="number" id="boxShadowBlur" value="15" min="0">
                            <label>Spread:</label><input type="number" id="boxShadowSpread" value="0">
                        </div>
                        <label style="font-size:0.78em;color:var(--text-secondary);margin-top:4px;">
                            <input type="checkbox" id="boxShadowInset"> İç Gölge (inset)
                        </label>
                        <div id="boxShadowColorPicker" class="color-picker-container"></div>
                    </div>
                </div>
            </div>

            <!-- 6. ANİMASYON -->
            <div class="panel" data-panel="animation">
                <div class="panel-header">
                    <div class="panel-icon anim"><i class="fas fa-play"></i></div>
                    <span class="panel-title">Animasyon / Geçiş</span>
                    <i class="fas fa-chevron-up panel-toggle"></i>
                </div>
                <div class="panel-body">
                    <div class="btn-grid">
                        <button class="style-btn" data-style-target="random-animation"><i class="fas fa-random"></i> Rnd Anim</button>
                        <button class="style-btn" data-style-target="random-timing-function"><i class="fas fa-clock"></i> Rnd Zamanlama</button>
                        <button class="style-btn" data-style-target="random-iteration-count"><i class="fas fa-redo"></i> Rnd Tekrar</button>
                        <button class="style-btn" data-style-target="stop-animation"><i class="fas fa-stop"></i> Durdur</button>
                    </div>
                    <div class="separator"></div>
                    <div class="form-group">
                        <label>Hazır Animasyonlar</label>
                        <select id="presetAnimation">
                            <option value="">Seçin...</option>
                            <option value="bounce">Zıpla</option>
                            <option value="pulse">Nabız</option>
                            <option value="shake">Salla</option>
                            <option value="fadeIn">Belir</option>
                            <option value="fadeOut">Kaybol</option>
                            <option value="slideInLeft">Sol Kayış</option>
                            <option value="slideInRight">Sağ Kayış</option>
                            <option value="rotateIn">Dönerek Gel</option>
                            <option value="zoomIn">Büyüyerek Gel</option>
                            <option value="flip">Çevir</option>
                            <option value="swing">Sallan</option>
                            <option value="rubberBand">Lastik</option>
                            <option value="jello">Jöle</option>
                            <option value="heartBeat">Kalp Atışı</option>
                            <option value="float">Süzül</option>
                            <option value="glitch">Glitch</option>
                            <option value="neonPulse">Neon Nabız</option>
                            <option value="typewriter">Daktilo</option>
                        </select>
                    </div>
                    <div class="form-group">
                        <label>Süre <span class="value-badge" id="animDurationVal">1s</span></label>
                        <input type="range" id="animationDurationRange" min="0.1" max="10" step="0.1" value="1">
                    </div>
                    <div class="form-group">
                        <label>Zamanlama</label>
                        <select id="animationTimingFunction" data-style-prop="animationTimingFunction">
                            <option value="ease" selected>Ease</option>
                            <option value="linear">Linear</option>
                            <option value="ease-in">Ease-In</option>
                            <option value="ease-out">Ease-Out</option>
                            <option value="ease-in-out">Ease-In-Out</option>
                            <option value="cubic-bezier(0.68, -0.55, 0.265, 1.55)">Bounce</option>
                            <option value="cubic-bezier(0.25, 0.46, 0.45, 0.94)">Soft</option>
                            <option value="steps(10)">Steps(10)</option>
                        </select>
                    </div>
                    <div class="form-group">
                        <label>Tekrar</label>
                        <select id="animationIterationCount">
                            <option value="1" selected>1</option>
                            <option value="2">2</option>
                            <option value="3">3</option>
                            <option value="5">5</option>
                            <option value="infinite">Sonsuz</option>
                        </select>
                    </div>
                    <div class="form-group">
                        <label>Yön</label>
                        <select id="animationDirection" data-style-prop="animationDirection">
                            <option value="normal" selected>Normal</option>
                            <option value="reverse">Ters</option>
                            <option value="alternate">Alternatif</option>
                            <option value="alternate-reverse">Alternatif Ters</option>
                        </select>
                    </div>
                    <div class="form-group">
                        <label>Geçiş (Transition)</label>
                        <div class="form-row">
                            <select id="transitionProperty">
                                <option value="all" selected>Tümü</option>
                                <option value="transform">Transform</option>
                                <option value="opacity">Opaklık</option>
                                <option value="background-color">Arkaplan</option>
                                <option value="color">Renk</option>
                                <option value="box-shadow">Gölge</option>
                            </select>
                            <input type="number" id="transitionDuration" value="0.3" min="0" step="0.1" style="width:60px;">
                            <span style="font-size:0.78em;color:var(--text-secondary);">s</span>
                        </div>
                    </div>
                    <div class="form-group">
                        <label>Özel Keyframes</label>
                        <textarea id="animationKeyframes" placeholder="@keyframes myAnim { 0% { ... } 100% { ... } }"></textarea>
                        <button class="add-color-btn" id="applyKeyframesBtn" style="background:var(--accent-tertiary);"><i class="fas fa-play"></i> Keyframes Uygula</button>
                    </div>
                </div>
            </div>

            <!-- 7. KIRMA / CLİP PATH -->
            <div class="panel" data-panel="clip">
                <div class="panel-header">
                    <div class="panel-icon clip"><i class="fas fa-cut"></i></div>
                    <span class="panel-title">Kırma (Clip-Path)</span>
                    <i class="fas fa-chevron-up panel-toggle"></i>
                </div>
                <div class="panel-body">
                    <div class="btn-grid">
                        <button class="style-btn" data-style-target="random-clip-path"><i class="fas fa-cut"></i> Rnd Kırma</button>
                        <button class="style-btn" data-style-target="reset-clip"><i class="fas fa-undo"></i> Sıfırla</button>
                    </div>
                    <div class="separator"></div>
                    <div class="form-group">
                        <label>Hazır Şekiller</label>
                        <select id="presetClipPath">
                            <option value="">Seçin...</option>
                            <option value="none">Yok</option>
                            <option value="circle(50% at 50% 50%)">Daire</option>
                            <option value="ellipse(40% 50% at 50% 50%)">Elips</option>
                            <option value="polygon(50% 0%, 100% 50%, 50% 100%, 0% 50%)">Elmas</option>
                            <option value="polygon(50% 0%, 100% 100%, 0% 100%)">Üçgen</option>
                            <option value="polygon(25% 0%, 75% 0%, 100% 50%, 75% 100%, 25% 100%, 0% 50%)">Altıgen</option>
                            <option value="polygon(50% 0%, 61% 35%, 98% 35%, 68% 57%, 79% 91%, 50% 70%, 21% 91%, 32% 57%, 2% 35%, 39% 35%)">Yıldız</option>
                            <option value="polygon(0% 0%, 100% 0%, 100% 75%, 75% 75%, 75% 100%, 50% 75%, 0% 75%)">Konuşma Balonu</option>
                            <option value="polygon(20% 0%, 80% 0%, 100% 20%, 100% 80%, 80% 100%, 20% 100%, 0% 80%, 0% 20%)">Sekizgen</option>
                            <option value="inset(5% 5% 5% 5% round 10px)">Yuvarlak İç</option>
                            <option value="polygon(0% 15%, 15% 15%, 15% 0%, 85% 0%, 85% 15%, 100% 15%, 100% 85%, 85% 85%, 85% 100%, 15% 100%, 15% 85%, 0% 85%)">Artı</option>
                        </select>
                    </div>
                    <div class="form-group">
                        <label>Özel Clip-Path</label>
                        <input type="text" id="clipPath" data-style-prop="clipPath" placeholder="polygon(50% 0%, ...)">
                    </div>
                </div>
            </div>

            <!-- 8. TRANSPARAN YAZI -->
            <div class="panel" data-panel="transparent">
                <div class="panel-header">
                    <div class="panel-icon transparent"><i class="fas fa-eye-dropper"></i></div>
                    <span class="panel-title">Transparan / Gradyan Yazı</span>
                    <i class="fas fa-chevron-up panel-toggle"></i>
                </div>
                <div class="panel-body">
                    <div class="btn-grid">
                        <button class="style-btn" data-style-target="random-text-opacity"><i class="fas fa-adjust"></i> Rnd Opaklık</button>
                        <button class="style-btn" data-style-target="random-text-gradient"><i class="fas fa-grip-lines"></i> Rnd Gradyan</button>
                        <button class="style-btn" data-style-target="random-text-image-fill"><i class="fas fa-image"></i> Rnd Resim</button>
                        <button class="style-btn" data-style-target="reset-text-fill"><i class="fas fa-undo"></i> Sıfırla</button>
                    </div>
                    <div class="separator"></div>
                    <div class="form-group">
                        <label>Opaklık <span class="value-badge" id="textOpacityVal">1</span></label>
                        <input type="range" id="textOpacityRange" min="0" max="1" step="0.05" value="1">
                    </div>
                    <div class="form-group">
                        <label>Metin Gradyan</label>
                        <div class="form-row">
                            <label>Yön:</label><input type="number" id="textGradientAngle" value="90" min="0" max="360">
                            <label>Tür:</label>
                            <select id="textGradientType">
                                <option value="linear" selected>Doğrusal</option>
                                <option value="radial">Radyal</option>
                            </select>
                        </div>
                        <div id="textGradientColors" class="gradient-colors"></div>
                        <button class="add-color-btn" id="addTextGradientColor"><i class="fas fa-plus"></i> Renk Ekle</button>
                    </div>
                    <div class="form-group">
                        <label>Resim Dolgusu URL</label>
                        <input type="text" id="textImageFill" placeholder="Resim URL...">
                    </div>
                    <div class="form-group">
                        <label>Mix Blend Mode</label>
                        <select id="mixBlendMode" data-style-prop="mixBlendMode">
                            <option value="normal" selected>Normal</option>
                            <option value="multiply">Çarpma</option>
                            <option value="screen">Ekran</option>
                            <option value="overlay">Kaplama</option>
                            <option value="difference">Fark</option>
                            <option value="exclusion">Dışlama</option>
                            <option value="color-dodge">Renk Etkisi</option>
                        </select>
                    </div>
                </div>
            </div>

            <!-- 9. RENK PALETİ -->
            <div class="panel" data-panel="palette">
                <div class="panel-header">
                    <div class="panel-icon palette"><i class="fas fa-swatchbook"></i></div>
                    <span class="panel-title">Renk Paleti Oluşturucu</span>
                    <i class="fas fa-chevron-up panel-toggle"></i>
                </div>
                <div class="panel-body">
                    <div class="btn-grid">
                        <button class="style-btn" data-style-target="generate-palette"><i class="fas fa-swatchbook"></i> Oluştur</button>
                        <button class="style-btn" data-style-target="random-palette"><i class="fas fa-dice"></i> Rnd Palet</button>
                    </div>
                    <div class="separator"></div>
                    <div class="form-group">
                        <label>Temel Renk</label>
                        <div id="baseColorPicker" class="color-picker-container"></div>
                    </div>
                    <div class="form-group">
                        <label>Palet Tipi</label>
                        <select id="paletteType">
                            <option value="monochromatic">Monokromatik</option>
                            <option value="analogous">Analog</option>
                            <option value="complementary">Tamamlayıcı</option>
                            <option value="triadic">Triadik</option>
                            <option value="split-complementary">Bölünmüş Tamamlayıcı</option>
                            <option value="tetradic">Tetradik</option>
                        </select>
                    </div>
                    <div class="form-group">
                        <label>Renk Sayısı</label>
                        <input type="number" id="paletteSize" value="5" min="2" max="12">
                    </div>
                    <div class="form-group">
                        <label>Palet Önizleme</label>
                        <div id="palettePreview" class="palette-preview"></div>
                    </div>
                </div>
            </div>

            <!-- 10. EFEKTLER -->
            <div class="panel" data-panel="effects">
                <div class="panel-header">
                    <div class="panel-icon effects"><i class="fas fa-magic"></i></div>
                    <span class="panel-title">Filtre & Efektler</span>
                    <i class="fas fa-chevron-up panel-toggle"></i>
                </div>
                <div class="panel-body">
                    <div class="btn-grid">
                        <button class="style-btn" data-style-target="random-filter"><i class="fas fa-filter"></i> Rnd Filtre</button>
                        <button class="style-btn" data-style-target="random-cursor"><i class="fas fa-mouse-pointer"></i> Rnd İmleç</button>
                        <button class="style-btn" data-style-target="random-effect"><i class="fas fa-star"></i> Rnd Efekt</button>
                        <button class="style-btn" data-style-target="reset-filters"><i class="fas fa-undo"></i> Sıfırla</button>
                    </div>
                    <div class="separator"></div>
                    <div class="form-group">
                        <label>Bulanıklık <span class="value-badge" id="blurVal">0px</span></label>
                        <input type="range" id="filterBlurRange" min="0" max="30" value="0">
                    </div>
                    <div class="form-group">
                        <label>Parlaklık <span class="value-badge" id="brightnessVal">100%</span></label>
                        <input type="range" id="filterBrightnessRange" min="0" max="300" value="100">
                    </div>
                    <div class="form-group">
                        <label>Kontrast <span class="value-badge" id="contrastVal">100%</span></label>
                        <input type="range" id="filterContrastRange" min="0" max="300" value="100">
                    </div>
                    <div class="form-group">
                        <label>Doygunluk <span class="value-badge" id="saturateVal">100%</span></label>
                        <input type="range" id="filterSaturateRange" min="0" max="300" value="100">
                    </div>
                    <div class="form-group">
                        <label>Ton Döndürme <span class="value-badge" id="hueRotateVal">0°</span></label>
                        <input type="range" id="filterHueRotateRange" min="0" max="360" value="0">
                    </div>
                    <div class="form-group">
                        <label>Ters Çevir <span class="value-badge" id="invertVal">0%</span></label>
                        <input type="range" id="filterInvertRange" min="0" max="100" value="0">
                    </div>
                    <div class="form-group">
                        <label>Sepya <span class="value-badge" id="sepiaVal">0%</span></label>
                        <input type="range" id="filterSepiaRange" min="0" max="100" value="0">
                    </div>
                    <div class="form-group">
                        <label>Gri Tonlama <span class="value-badge" id="grayscaleVal">0%</span></label>
                        <input type="range" id="filterGrayscaleRange" min="0" max="100" value="0">
                    </div>
                    <div class="form-group">
                        <label>Backdrop Blur</label>
                        <input type="range" id="backdropBlurRange" min="0" max="30" value="0">
                    </div>
                    <div class="form-group">
                        <label>İmleç</label>
                        <select id="cursor" data-style-prop="cursor">
                            <option value="auto" selected>Otomatik</option>
                            <option value="pointer">İşaretçi</option>
                            <option value="crosshair">Artı</option>
                            <option value="move">Taşı</option>
                            <option value="text">Metin</option>
                            <option value="not-allowed">Yasak</option>
                            <option value="grab">Yakala</option>
                            <option value="zoom-in">Yakınlaştır</option>
                            <option value="zoom-out">Uzaklaştır</option>
                            <option value="wait">Bekle</option>
                            <option value="help">Yardım</option>
                            <option value="none">Gizle</option>
                        </select>
                    </div>
                </div>
            </div>

            <!-- 11. LAYOUT -->
            <div class="panel" data-panel="layout">
                <div class="panel-header">
                    <div class="panel-icon layout"><i class="fas fa-th-large"></i></div>
                    <span class="panel-title">Boyut & Düzen</span>
                    <i class="fas fa-chevron-up panel-toggle"></i>
                </div>
                <div class="panel-body">
                    <div class="form-group">
                        <label>Genişlik</label>
                        <div class="form-row">
                            <input type="text" id="boxWidth" placeholder="auto" data-style-prop="width">
                            <select id="widthUnit" style="width:60px;">
                                <option value="px">px</option>
                                <option value="%">%</option>
                                <option value="vw">vw</option>
                                <option value="rem">rem</option>
                            </select>
                        </div>
                    </div>
                    <div class="form-group">
                        <label>Yükseklik</label>
                        <div class="form-row">
                            <input type="text" id="boxHeight" placeholder="auto" data-style-prop="height">
                            <select id="heightUnit" style="width:60px;">
                                <option value="px">px</option>
                                <option value="%">%</option>
                                <option value="vh">vh</option>
                                <option value="rem">rem</option>
                            </select>
                        </div>
                    </div>
                    <div class="form-group">
                        <label>Min/Max Genişlik</label>
                        <div class="form-row">
                            <label>Min:</label><input type="text" id="minWidth" placeholder="auto" data-style-prop="minWidth">
                            <label>Max:</label><input type="text" id="maxWidth" placeholder="auto" data-style-prop="maxWidth">
                        </div>
                    </div>
                    <div class="form-group">
                        <label>Min/Max Yükseklik</label>
                        <div class="form-row">
                            <label>Min:</label><input type="text" id="minHeight" placeholder="auto" data-style-prop="minHeight">
                            <label>Max:</label><input type="text" id="maxHeight" placeholder="auto" data-style-prop="maxHeight">
                        </div>
                    </div>
                    <div class="form-group">
                        <label>Overflow</label>
                        <select id="overflow" data-style-prop="overflow">
                            <option value="hidden" selected>Gizle</option>
                            <option value="visible">Göster</option>
                            <option value="scroll">Kaydır</option>
                            <option value="auto">Otomatik</option>
                        </select>
                    </div>
                    <div class="form-group">
                        <label>Display</label>
                        <select id="display" data-style-prop="display">
                            <option value="flex" selected>Flex</option>
                            <option value="block">Block</option>
                            <option value="inline-block">Inline Block</option>
                            <option value="grid">Grid</option>
                            <option value="inline-flex">Inline Flex</option>
                        </select>
                    </div>
                    <div class="form-group">
                        <label>Flex Yönü</label>
                        <select id="flexDirection" data-style-prop="flexDirection">
                            <option value="row">Satır</option>
                            <option value="column">Sütun</option>
                            <option value="row-reverse">Satır Ters</option>
                            <option value="column-reverse">Sütun Ters</option>
                        </select>
                    </div>
                    <div class="form-group">
                        <label>Justify Content</label>
                        <select id="justifyContent" data-style-prop="justifyContent">
                            <option value="center" selected>Ortala</option>
                            <option value="flex-start">Başlangıç</option>
                            <option value="flex-end">Bitiş</option>
                            <option value="space-between">Arası Boşluk</option>
                            <option value="space-around">Etrafı Boşluk</option>
                            <option value="space-evenly">Eşit Boşluk</option>
                        </select>
                    </div>
                    <div class="form-group">
                        <label>Align Items</label>
                        <select id="alignItems" data-style-prop="alignItems">
                            <option value="center" selected>Ortala</option>
                            <option value="flex-start">Başlangıç</option>
                            <option value="flex-end">Bitiş</option>
                            <option value="stretch">Esnet</option>
                            <option value="baseline">Taban Çizgisi</option>
                        </select>
                    </div>
                    <div class="form-group">
                        <label>Gap</label>
                        <input type="text" id="gap" data-style-prop="gap" placeholder="0px">
                    </div>
                </div>
            </div>

            <!-- 12. HAZIR TEMALAR -->
            <div class="panel" data-panel="presets">
                <div class="panel-header">
                    <div class="panel-icon presets"><i class="fas fa-palette"></i></div>
                    <span class="panel-title">Hazır Temalar</span>
                    <i class="fas fa-chevron-up panel-toggle"></i>
                </div>
                <div class="panel-body">
                    <div class="preset-cards">
                        <button class="preset-card" data-style-target="auto-theme-neon">
                            <i class="fas fa-lightbulb"></i> Neon
                        </button>
                        <button class="preset-card" data-style-target="auto-theme-minimal">
                            <i class="fas fa-compress"></i> Minimal
                        </button>
                        <button class="preset-card" data-style-target="auto-theme-vintage">
                            <i class="fas fa-camera-retro"></i> Vintage
                        </button>
                        <button class="preset-card" data-style-target="auto-theme-glassmorphism">
                            <i class="fas fa-glass-whiskey"></i> Glass
                        </button>
                        <button class="preset-card" data-style-target="auto-theme-neumorphism">
                            <i class="fas fa-circle"></i> Neumorphism
                        </button>
                        <button class="preset-card" data-style-target="auto-theme-cyberpunk">
                            <i class="fas fa-robot"></i> Cyberpunk
                        </button>
                        <button class="preset-card" data-style-target="auto-theme-nature">
                            <i class="fas fa-leaf"></i> Doğa
                        </button>
                        <button class="preset-card" data-style-target="auto-theme-ocean">
                            <i class="fas fa-water"></i> Okyanus
                        </button>
                        <button class="preset-card" data-style-target="auto-theme-sunset">
                            <i class="fas fa-sun"></i> Gün Batımı
                        </button>
                        <button class="preset-card" data-style-target="auto-theme-dark-elegant">
                            <i class="fas fa-gem"></i> Zarif Karanlık
                        </button>
                    </div>
                </div>
            </div>

            <!-- 13. KAOS MOTORU -->
            <div class="panel" data-panel="chaos">
                <div class="panel-header">
                    <div class="panel-icon chaos"><i class="fas fa-explosion"></i></div>
                    <span class="panel-title">Kaos Motoru</span>
                    <i class="fas fa-chevron-up panel-toggle"></i>
                </div>
                <div class="panel-body">
                    <div class="btn-grid">
                        <button class="style-btn chaos-btn" data-style-target="auto-generate" style="grid-column:1/-1;padding:12px;font-size:0.9em;">
                            <i class="fas fa-wand-magic-sparkles"></i> Otomatik Stil Oluştur
                        </button>
                        <button class="style-btn chaos-btn" data-style-target="max-chaos" style="grid-column:1/-1;padding:12px;font-size:0.9em;">
                            <i class="fas fa-explosion"></i> MAKSİMUM KAOS!
                        </button>
                    </div>
                    <div class="separator"></div>
                    <div class="form-group">
                        <label>Kaos Kategorileri</label>
                        <div class="checkbox-row">
                            <label><input type="checkbox" id="chaosFont" checked> Yazı</label>
                            <label><input type="checkbox" id="chaosBackground" checked> Arka Plan</label>
                            <label><input type="checkbox" id="chaosBorder" checked> Çerçeve</label>
                        </div>
                        <div class="checkbox-row">
                            <label><input type="checkbox" id="chaosEffects" checked> Efektler</label>
                            <label><input type="checkbox" id="chaosAnimation" checked> Animasyon</label>
                            <label><input type="checkbox" id="chaosClip" checked> Kırma</label>
                        </div>
                        <div class="checkbox-row">
                            <label><input type="checkbox" id="chaosTransform" checked> Dönüşüm</label>
                            <label><input type="checkbox" id="chaosBoxShadow" checked> Gölge</label>
                            <label><input type="checkbox" id="chaosTextGradient" checked> Gradyan</label>
                        </div>
                        <div class="checkbox-row">
                            <label><input type="checkbox" id="chaosTextImage" checked> Resim Dolgusu</label>
                            <label><input type="checkbox" id="chaosOpacity" checked> Opaklık</label>
                            <label><input type="checkbox" id="chaosLayout" checked> Düzen</label>
                        </div>
                    </div>
                </div>
            </div>
        </aside>

        <!-- MAIN CONTENT -->
        <main class="main-content">
            <!-- PREVIEW -->
            <div class="preview-wrapper">
                <div class="preview-label">
                    <h3><i class="fas fa-eye"></i> Canlı Önizleme</h3>
                    <span class="preview-dimensions" id="previewDimensions">-- × --</span>
                </div>
                <div id="preview-box">K3N4N V6.0</div>
                <div class="preview-text-input">
                    <input type="text" id="customText" placeholder="Önizleme metnini değiştir...">
                    <span class="char-count" id="charCount">0/100</span>
                </div>
            </div>

            <!-- CSS OUTPUT -->
            <div class="output-card">
                <div class="output-tabs">
                    <button class="output-tab active" data-tab="css-tab">CSS Çıktısı</button>
                    <button class="output-tab" data-tab="html-tab">HTML Önizleme</button>
                    <button class="output-tab" data-tab="input-tab">Özel CSS</button>
                </div>

                <div class="tab-content active" id="css-tab">
                    <div class="output-card-body">
                        <textarea id="css-output" readonly></textarea>
                        <div class="output-actions">
                            <button class="output-btn primary" id="copy-css-btn"><i class="fas fa-copy"></i> Kopyala</button>
                            <button class="output-btn secondary" data-action="download-css"><i class="fas fa-download"></i> CSS İndir</button>
                            <button class="output-btn secondary" data-action="download-html"><i class="fas fa-file-code"></i> HTML İndir</button>
                            <button class="output-btn tertiary" data-action="export-styles"><i class="fas fa-file-export"></i> Dışa Aktar</button>
                            <button class="output-btn tertiary" data-action="import-styles"><i class="fas fa-file-import"></i> İçe Aktar</button>
                            <input type="file" id="import-styles" accept=".json">
                        </div>
                        <div class="msg success" id="copy-success"><i class="fas fa-check-circle"></i> CSS panoya kopyalandı!</div>
                        <div class="msg error" id="copy-error"><i class="fas fa-exclamation-circle"></i> Kopyalama başarısız.</div>
                    </div>
                </div>

                <div class="tab-content" id="html-tab">
                    <div class="output-card-body">
                        <div id="htmlPreviewArea"></div>
                    </div>
                </div>

                <div class="tab-content" id="input-tab">
                    <div class="output-card-body">
                        <textarea id="cssInputArea" placeholder="Özel CSS kodunuzu buraya girin..."></textarea>
                        <div class="output-actions">
                            <button class="output-btn primary" id="applyCustomCss"><i class="fas fa-check"></i> CSS Uygula</button>
                        </div>
                        <div class="msg success" id="css-success"><i class="fas fa-check-circle"></i> CSS başarıyla uygulandı!</div>
                        <div class="msg error" id="css-error"><i class="fas fa-exclamation-circle"></i> Geçersiz CSS.</div>
                    </div>
                </div>
            </div>
        </main>
    </div>

    <!-- FOOTER -->
    <footer class="app-footer">
        <p>K3N4N CSS Stil Generator V6.0 © 2025 — Tüm hakları saklıdır.</p>
    </footer>

    <script>
    (function() {
        'use strict';

        // ===== DOM =====
        const $ = id => document.getElementById(id);
        const $$ = sel => document.querySelectorAll(sel);

        const previewBox = $('preview-box');
        const cssOutput = $('css-output');
        const cssInputArea = $('cssInputArea');
        const customTextInput = $('customText');
        const htmlPreviewArea = $('htmlPreviewArea');
        const toastContainer = $('toastContainer');

        // ===== STATE =====
        let currentTheme = 'dark';
        let history = [];
        let historyIndex = -1;
        const MAX_HISTORY = 80;

        let currentStyles = getDefaultStyles();

        function getDefaultStyles() {
            return {
                fontFamily: "'Poppins', sans-serif",
                fontSize: '30px',
                fontWeight: '400',
                fontStyle: 'normal',
                color: '#222222',
                textShadow: 'none',
                textDecorationLine: 'none',
                textDecorationStyle: 'solid',
                textAlign: 'center',
                lineHeight: '1.5',
                letterSpacing: '0px',
                wordSpacing: '0px',
                textTransform: 'none',
                writingMode: 'horizontal-tb',
                textOverflow: 'clip',
                paddingLeft: '0px',
                paddingRight: '0px',
                paddingTop: '0px',
                paddingBottom: '0px',
                backgroundColor: '#ffffff',
                backgroundImage: 'none',
                backgroundPositionX: 'center',
                backgroundPositionY: 'center',
                backgroundSize: 'auto',
                backgroundRepeat: 'repeat',
                backgroundBlendMode: 'normal',
                opacity: '1',
                borderTop: '1px solid #cccccc',
                borderBottom: '1px solid #cccccc',
                borderLeft: '1px solid #cccccc',
                borderRight: '1px solid #cccccc',
                borderTopLeftRadius: '10px',
                borderTopRightRadius: '10px',
                borderBottomLeftRadius: '10px',
                borderBottomRightRadius: '10px',
                outlineWidth: '0px',
                outlineStyle: 'none',
                outlineColor: '#ffffff',
                outlineOffset: '0px',
                transform: 'none',
                transformOrigin: 'center center',
                boxShadow: '0 4px 15px rgba(0, 0, 0, 0.08)',
                animationName: 'none',
                animationDuration: '1s',
                animationTimingFunction: 'ease',
                animationIterationCount: '1',
                animationDirection: 'normal',
                clipPath: 'none',
                filter: 'none',
                backdropFilter: 'none',
                cursor: 'auto',
                backgroundClip: 'border-box',
                webkitTextFillColor: '',
                webkitBackgroundClip: '',
                mixBlendMode: 'normal',
                width: 'auto',
                height: 'auto',
                minWidth: 'auto',
                maxWidth: 'auto',
                minHeight: '280px',
                maxHeight: 'auto',
                overflow: 'hidden',
                display: 'flex',
                flexDirection: 'row',
                justifyContent: 'center',
                alignItems: 'center',
                gap: '0px',
                transition: 'none'
            };
        }

        // ===== TOAST =====
        function showToast(message, type = 'success') {
            const toast = document.createElement('div');
            toast.className = `toast ${type}`;
            toast.innerHTML = `<i class="fas fa-${type === 'success' ? 'check-circle' : type === 'error' ? 'exclamation-circle' : 'info-circle'}"></i> ${message}`;
            toastContainer.appendChild(toast);
            setTimeout(() => toast.remove(), 3000);
        }

        // ===== COLOR PICKERS =====
        const pickers = {};
        const pickerConfigs = [
            { id: 'textColorPicker', key: 'textColor', default: '#222222', onChange: c => updateStyle('color', c.hexString) },
            { id: 'textShadowColorPicker', key: 'textShadowColor', default: '#000000', onChange: c => updateComplexStyle('textShadowColor', c.hexString) },
            { id: 'backgroundColorPicker', key: 'bgColor', default: '#ffffff', onChange: c => updateStyle('backgroundColor', c.hexString) },
            { id: 'outlineColorPicker', key: 'outlineColor', default: '#ffffff', onChange: c => updateComplexStyle('outlineColor', c.hexString) },
            { id: 'boxShadowColorPicker', key: 'boxShadowColor', default: '#000000', onChange: c => updateComplexStyle('boxShadowColor', c.hexString) },
            { id: 'baseColorPicker', key: 'baseColor', default: '#64ffda', onChange: () => generatePalette() }
        ];

        pickerConfigs.forEach(cfg => {
            const el = $(cfg.id);
            if (!el) return;
            pickers[cfg.key] = new iro.ColorPicker(el, {
                width: 140,
                color: cfg.default,
                borderWidth: 1,
                borderColor: 'rgba(255,255,255,0.15)',
                layoutDirection: 'horizontal',
                layout: [
                    { component: iro.ui.Wheel, options: { wheelLightness: true } },
                    { component: iro.ui.Slider, options: { sliderType: 'value' } }
                ]
            });
            pickers[cfg.key].on('color:change', cfg.onChange);
        });

        // ===== GRADIENT COLORS =====
        let gradientColors = [{ color: '#64ffda', stop: 0 }, { color: '#c084fc', stop: 100 }];
        let textGradientColors = [{ color: '#64ffda', stop: 0 }, { color: '#ff6b9d', stop: 100 }];

        function initGradientPickers(container, colors, type) {
            const el = $(container);
            el.innerHTML = '';
            colors.forEach((gc, i) => {
                const row = document.createElement('div');
                row.className = 'gradient-color-row';
                const colorInput = document.createElement('input');
                colorInput.type = 'color';
                colorInput.value = gc.color;
                colorInput.style.cssText = 'width:40px;height:28px;border:1px solid var(--border-color);border-radius:4px;cursor:pointer;background:var(--bg-dark);padding:1px;';
                colorInput.addEventListener('input', e => {
                    colors[i].color = e.target.value;
                    type === 'bg' ? updateGradient() : updateTextGradient();
                });

                const stopInput = document.createElement('input');
                stopInput.type = 'number';
                stopInput.className = type === 'bg' ? 'gradientStop' : 'textGradientStop';
                stopInput.value = gc.stop;
                stopInput.min = 0;
                stopInput.max = 100;
                stopInput.style.width = '55px';
                stopInput.addEventListener('input', e => {
                    colors[i].stop = parseInt(e.target.value) || 0;
                    type === 'bg' ? updateGradient() : updateTextGradient();
                });

                const removeBtn = document.createElement('button');
                removeBtn.className = type === 'bg' ? 'removeGradientColor' : 'removeTextGradientColor';
                removeBtn.innerHTML = '<i class="fas fa-trash"></i>';
                removeBtn.addEventListener('click', () => {
                    if (colors.length > 1) {
                        colors.splice(i, 1);
                        initGradientPickers(container, colors, type);
                        type === 'bg' ? updateGradient() : updateTextGradient();
                    }
                });

                row.appendChild(colorInput);
                row.appendChild(stopInput);
                row.appendChild(removeBtn);
                el.appendChild(row);
            });
        }

        $('addGradientColor').addEventListener('click', () => {
            gradientColors.push({ color: '#' + Math.floor(Math.random()*16777215).toString(16).padStart(6,'0'), stop: 100 });
            initGradientPickers('gradientColors', gradientColors, 'bg');
            updateGradient();
        });

        $('addTextGradientColor').addEventListener('click', () => {
            textGradientColors.push({ color: '#' + Math.floor(Math.random()*16777215).toString(16).padStart(6,'0'), stop: 100 });
            initGradientPickers('textGradientColors', textGradientColors, 'text');
            updateTextGradient();
        });

        // ===== CORE FUNCTIONS =====
        function updateStyle(property, value, unit = '') {
            const finalVal = unit ? `${value}${unit}` : value;
            if (currentStyles[property] !== finalVal) {
                currentStyles[property] = finalVal;
                applyStyles();
                saveToHistory();
            }
        }

               function updateComplexStyle(property, value) {
            if (property === 'textShadowColor') {
                const x = $('textShadowX').value || 0;
                const y = $('textShadowY').value || 0;
                const blur = $('textShadowBlur').value || 0;
                currentStyles.textShadow = `${x}px ${y}px ${blur}px ${value}`;
            } else if (property === 'boxShadowColor') {
                const x = $('boxShadowX').value || 0;
                const y = $('boxShadowY').value || 0;
                const blur = $('boxShadowBlur').value || 0;
                const spread = $('boxShadowSpread').value || 0;
                const inset = $('boxShadowInset').checked ? 'inset ' : '';
                currentStyles.boxShadow = `${inset}${x}px ${y}px ${blur}px ${spread}px ${value}`;
            } else if (property === 'outlineColor') {
                currentStyles.outlineWidth = `${$('outlineWidth').value || 0}px`;
                currentStyles.outlineStyle = $('outlineStyle').value;
                currentStyles.outlineColor = value;
            }
            applyStyles();
            saveToHistory();
        }

        function updateGradient() {
            const type = $('gradientType').value;
            const angle = $('gradientAngle').value;
            const stops = gradientColors.map(gc => `${gc.color} ${gc.stop}%`).join(', ');
            let gradient;
            if (type === 'linear') gradient = `linear-gradient(${angle}deg, ${stops})`;
            else if (type === 'radial') gradient = `radial-gradient(circle, ${stops})`;
            else gradient = `conic-gradient(from ${angle}deg, ${stops})`;
            currentStyles.backgroundImage = gradient;
            currentStyles.webkitBackgroundClip = '';
            currentStyles.webkitTextFillColor = '';
            currentStyles.backgroundClip = 'border-box';
            applyStyles();
            saveToHistory();
        }

        function updateTextGradient() {
            const type = $('textGradientType').value;
            const angle = $('textGradientAngle').value;
            const stops = textGradientColors.map(gc => `${gc.color} ${gc.stop}%`).join(', ');
            let gradient;
            if (type === 'linear') gradient = `linear-gradient(${angle}deg, ${stops})`;
            else gradient = `radial-gradient(circle, ${stops})`;
            currentStyles.backgroundImage = gradient;
            currentStyles.webkitBackgroundClip = 'text';
            currentStyles.backgroundClip = 'text';
            currentStyles.webkitTextFillColor = 'transparent';
            applyStyles();
            saveToHistory();
        }

        function updateTextImageFill() {
            const url = $('textImageFill').value.trim();
            if (url) {
                currentStyles.backgroundImage = `url(${url})`;
                currentStyles.backgroundSize = 'cover';
                currentStyles.webkitBackgroundClip = 'text';
                currentStyles.backgroundClip = 'text';
                currentStyles.webkitTextFillColor = 'transparent';
            } else {
                currentStyles.backgroundImage = 'none';
                currentStyles.webkitBackgroundClip = '';
                currentStyles.backgroundClip = 'border-box';
                currentStyles.webkitTextFillColor = '';
            }
            applyStyles();
            saveToHistory();
        }

        function updateBackgroundImageUrl() {
            const url = $('backgroundImageUrl').value.trim();
            if (url) {
                currentStyles.backgroundImage = `url(${url})`;
                currentStyles.webkitBackgroundClip = '';
                currentStyles.webkitTextFillColor = '';
                currentStyles.backgroundClip = 'border-box';
            } else {
                currentStyles.backgroundImage = 'none';
            }
            applyStyles();
            saveToHistory();
        }

        function updateFilter() {
            const blur = $('filterBlurRange').value;
            const brightness = $('filterBrightnessRange').value;
            const contrast = $('filterContrastRange').value;
            const saturate = $('filterSaturateRange').value;
            const hueRotate = $('filterHueRotateRange').value;
            const invert = $('filterInvertRange').value;
            const sepia = $('filterSepiaRange').value;
            const grayscale = $('filterGrayscaleRange').value;
            let parts = [];
            if (parseFloat(blur) > 0) parts.push(`blur(${blur}px)`);
            if (parseFloat(brightness) !== 100) parts.push(`brightness(${brightness}%)`);
            if (parseFloat(contrast) !== 100) parts.push(`contrast(${contrast}%)`);
            if (parseFloat(saturate) !== 100) parts.push(`saturate(${saturate}%)`);
            if (parseFloat(hueRotate) > 0) parts.push(`hue-rotate(${hueRotate}deg)`);
            if (parseFloat(invert) > 0) parts.push(`invert(${invert}%)`);
            if (parseFloat(sepia) > 0) parts.push(`sepia(${sepia}%)`);
            if (parseFloat(grayscale) > 0) parts.push(`grayscale(${grayscale}%)`);
            currentStyles.filter = parts.length ? parts.join(' ') : 'none';

            const backdropBlur = $('backdropBlurRange').value;
            currentStyles.backdropFilter = parseFloat(backdropBlur) > 0 ? `blur(${backdropBlur}px)` : 'none';

            $('blurVal').textContent = blur + 'px';
            $('brightnessVal').textContent = brightness + '%';
            $('contrastVal').textContent = contrast + '%';
            $('saturateVal').textContent = saturate + '%';
            $('hueRotateVal').textContent = hueRotate + '°';
            $('invertVal').textContent = invert + '%';
            $('sepiaVal').textContent = sepia + '%';
            $('grayscaleVal').textContent = grayscale + '%';

            applyStyles();
            saveToHistory();
        }

        function updatePadding() {
            const unit = $('paddingUnit').value;
            currentStyles.paddingLeft = ($('paddingLeft').value || 0) + unit;
            currentStyles.paddingRight = ($('paddingRight').value || 0) + unit;
            currentStyles.paddingTop = ($('paddingTop').value || 0) + unit;
            currentStyles.paddingBottom = ($('paddingBottom').value || 0) + unit;
            applyStyles();
            saveToHistory();
        }

        function updateTransform() {
            const rotate = $('rotate') ? $('rotate').value : ($('rotateRange') ? $('rotateRange').value : 0);
            const scale = $('scaleRange').value;
            const skewX = $('skewX').value || 0;
            const skewY = $('skewY').value || 0;
            const translateX = $('translateX').value || 0;
            const translateY = $('translateY').value || 0;
            let parts = [];
            if (parseFloat(rotate) !== 0) parts.push(`rotate(${rotate}deg)`);
            if (parseFloat(scale) !== 1) parts.push(`scale(${scale})`);
            if (parseFloat(skewX) !== 0) parts.push(`skewX(${skewX}deg)`);
            if (parseFloat(skewY) !== 0) parts.push(`skewY(${skewY}deg)`);
            if (parseFloat(translateX) !== 0) parts.push(`translateX(${translateX}px)`);
            if (parseFloat(translateY) !== 0) parts.push(`translateY(${translateY}px)`);
            currentStyles.transform = parts.length ? parts.join(' ') : 'none';

            $('rotateVal').textContent = rotate + '°';
            $('scaleVal').textContent = scale;

            applyStyles();
            saveToHistory();
        }

        function updateBoxShadow() {
            const x = $('boxShadowX').value || 0;
            const y = $('boxShadowY').value || 0;
            const blur = $('boxShadowBlur').value || 0;
            const spread = $('boxShadowSpread').value || 0;
            const inset = $('boxShadowInset').checked ? 'inset ' : '';
            const color = pickers.boxShadowColor ? pickers.boxShadowColor.color.hexString : '#000000';
            currentStyles.boxShadow = `${inset}${x}px ${y}px ${blur}px ${spread}px ${color}`;
            applyStyles();
            saveToHistory();
        }

        function updateTransition() {
            const prop = $('transitionProperty').value;
            const dur = $('transitionDuration').value;
            currentStyles.transition = `${prop} ${dur}s ease`;
            applyStyles();
            saveToHistory();
        }

        // ===== APPLY STYLES =====
        function applyStyles() {
            const stylePropMap = {
                webkitTextFillColor: '-webkit-text-fill-color',
                webkitBackgroundClip: '-webkit-background-clip'
            };

            Object.keys(currentStyles).forEach(prop => {
                const val = currentStyles[prop];
                if (val === '' || val === undefined || val === null) return;

                if (prop === 'webkitTextFillColor') {
                    previewBox.style.setProperty('-webkit-text-fill-color', val);
                } else if (prop === 'webkitBackgroundClip') {
                    previewBox.style.setProperty('-webkit-background-clip', val);
                } else {
                    try { previewBox.style[prop] = val; } catch(e) {}
                }
            });

            updateCssOutput();
            updateHtmlPreview();
            updatePreviewDimensions();
        }

        function camelToKebab(str) {
            return str.replace(/[A-Z]/g, m => `-${m.toLowerCase()}`);
        }

        function updateCssOutput() {
            const defaults = getDefaultStyles();
            const lines = [];
            Object.entries(currentStyles).forEach(([key, value]) => {
                if (value === '' || value === undefined || value === null) return;
                let cssProp;
                if (key === 'webkitTextFillColor') cssProp = '-webkit-text-fill-color';
                else if (key === 'webkitBackgroundClip') cssProp = '-webkit-background-clip';
                else cssProp = camelToKebab(key);
                lines.push(`    ${cssProp}: ${value};`);
            });
            cssOutput.value = `#preview-box {\n${lines.join('\n')}\n}`;
        }

        function updateHtmlPreview() {
            const text = customTextInput.value || 'K3N4N V6.0';
            const inlineStyles = [];
            Object.entries(currentStyles).forEach(([key, value]) => {
                if (value === '' || value === undefined || value === null) return;
                let cssProp;
                if (key === 'webkitTextFillColor') cssProp = '-webkit-text-fill-color';
                else if (key === 'webkitBackgroundClip') cssProp = '-webkit-background-clip';
                else cssProp = camelToKebab(key);
                inlineStyles.push(`${cssProp}: ${value}`);
            });
            htmlPreviewArea.textContent = `<div id="preview-box" style="${inlineStyles.join('; ')}">\n  ${text}\n</div>`;
        }

        function updatePreviewDimensions() {
            const rect = previewBox.getBoundingClientRect();
            $('previewDimensions').textContent = `${Math.round(rect.width)} × ${Math.round(rect.height)}`;
        }

        // ===== HISTORY =====
        function saveToHistory() {
            history = history.slice(0, historyIndex + 1);
            history.push(JSON.parse(JSON.stringify(currentStyles)));
            if (history.length > MAX_HISTORY) history.shift();
            historyIndex = history.length - 1;
            updateHistoryButtons();
        }

        function updateHistoryButtons() {
            const undoBtn = document.querySelector('[data-action="undo"]');
            const redoBtn = document.querySelector('[data-action="redo"]');
            if (undoBtn) undoBtn.disabled = historyIndex <= 0;
            if (redoBtn) redoBtn.disabled = historyIndex >= history.length - 1;
        }

        function undo() {
            if (historyIndex > 0) {
                historyIndex--;
                currentStyles = JSON.parse(JSON.stringify(history[historyIndex]));
                applyStyles();
                updateHistoryButtons();
                showToast('Geri alındı', 'info');
            }
        }

        function redo() {
            if (historyIndex < history.length - 1) {
                historyIndex++;
                currentStyles = JSON.parse(JSON.stringify(history[historyIndex]));
                applyStyles();
                updateHistoryButtons();
                showToast('İleri alındı', 'info');
            }
        }

        // ===== RANDOM GENERATORS =====
        function rndHex() {
            return '#' + Math.floor(Math.random() * 16777215).toString(16).padStart(6, '0');
        }

        function rndInt(min, max) {
            return Math.floor(Math.random() * (max - min + 1)) + min;
        }

        function rndFloat(min, max, dec = 1) {
            return parseFloat((Math.random() * (max - min) + min).toFixed(dec));
        }

        function rndItem(arr) {
            return arr[Math.floor(Math.random() * arr.length)];
        }

        const allFonts = [
            "'Poppins', sans-serif", "'Inter', sans-serif", "'Space Grotesk', sans-serif",
            "'VT323', monospace", "'Press Start 2P', monospace", "'Orbitron', sans-serif",
            "'Roboto Mono', monospace", "'JetBrains Mono', monospace", "'Lobster', cursive",
            "'Kaushan Script', cursive", "'Fira Code', monospace", "Georgia, serif",
            "'Courier New', monospace", "Impact, sans-serif"
        ];

        function randomFont() {
            updateStyle('fontFamily', rndItem(allFonts));
            updateStyle('fontSize', rndItem([16, 20, 24, 28, 30, 36, 42, 48, 56, 64]), 'px');
            updateStyle('fontWeight', rndItem(['300', '400', '500', '600', '700', '800', '900']));
            showToast('Yazı tipi randomlandı');
        }

        function randomColor() {
            updateStyle('color', rndHex());
            showToast('Yazı rengi değişti');
        }

        function randomTextShadow() {
            const count = rndInt(1, 3);
            let shadows = [];
            for (let i = 0; i < count; i++) {
                shadows.push(`${rndInt(-8, 8)}px ${rndInt(-8, 8)}px ${rndInt(0, 15)}px ${rndHex()}`);
            }
            currentStyles.textShadow = shadows.join(', ');
            applyStyles();
            saveToHistory();
            showToast('Yazı gölgesi oluşturuldu');
        }

        function randomTextDecoration() {
            updateStyle('textDecorationLine', rndItem(['none', 'underline', 'overline', 'line-through']));
            updateStyle('textDecorationStyle', rndItem(['solid', 'double', 'dotted', 'dashed', 'wavy']));
        }

        function randomSpacing() {
            updateStyle('letterSpacing', rndFloat(-2, 8), 'px');
            updateStyle('wordSpacing', rndFloat(-2, 10), 'px');
        }

        function randomAlign() {
            updateStyle('textAlign', rndItem(['left', 'center', 'right', 'justify']));
        }

        function randomLineHeight() {
            const val = rndFloat(0.8, 3.0);
            currentStyles.lineHeight = val.toString();
            $('lineHeightRange').value = val;
            $('lineHeightVal').textContent = val;
            applyStyles();
            saveToHistory();
        }

        function randomTextTransform() {
            updateStyle('textTransform', rndItem(['none', 'uppercase', 'lowercase', 'capitalize']));
        }

        function randomBgColor() {
            updateStyle('backgroundColor', rndHex());
            currentStyles.backgroundImage = 'none';
            currentStyles.webkitBackgroundClip = '';
            currentStyles.webkitTextFillColor = '';
            currentStyles.backgroundClip = 'border-box';
            applyStyles();
            saveToHistory();
            showToast('Arka plan rengi değişti');
        }

        function randomGradient() {
            const count = rndInt(2, 4);
            gradientColors = [];
            for (let i = 0; i < count; i++) {
                gradientColors.push({ color: rndHex(), stop: Math.round(i / (count - 1) * 100) });
            }
            $('gradientAngle').value = rndInt(0, 360);
            $('gradientType').value = rndItem(['linear', 'radial', 'conic']);
            initGradientPickers('gradientColors', gradientColors, 'bg');
            updateGradient();
            showToast('Gradyan oluşturuldu');
        }

        function randomBgGif() {
            const gifs = [
                'https://media.giphy.com/media/l0MYt5jPR6QX5pnqM/giphy.gif',
                'https://media.giphy.com/media/3o7btPCcdNniyf0ArS/giphy.gif',
                'https://media.giphy.com/media/xT9IgzoKnwFNmISR8I/giphy.gif',
                'https://media.giphy.com/media/26tn33aiTi1jkl6H6/giphy.gif',
                'https://media.giphy.com/media/l378p60yRSCeVrd5e/giphy.gif'
            ];
            currentStyles.backgroundImage = `url(${rndItem(gifs)})`;
            currentStyles.backgroundSize = 'cover';
            currentStyles.webkitBackgroundClip = '';
            currentStyles.webkitTextFillColor = '';
            currentStyles.backgroundClip = 'border-box';
            applyStyles();
            saveToHistory();
        }

        function randomBgPosition() {
            const positions = ['center', 'top', 'bottom', 'left', 'right', '25%', '75%'];
            updateStyle('backgroundPositionX', rndItem(positions));
            updateStyle('backgroundPositionY', rndItem(positions));
        }

        function randomBgSize() {
            updateStyle('backgroundSize', rndItem(['auto', 'cover', 'contain', '100% 100%', '50% 50%', '200px 200px']));
        }

        function randomBgOpacity() {
            const val = rndFloat(0.2, 1.0);
            currentStyles.opacity = val.toString();
            $('backgroundOpacityRange').value = val;
            $('bgOpacityVal').textContent = val;
            applyStyles();
            saveToHistory();
        }

        function randomBgPattern() {
            const patterns = [
                `repeating-linear-gradient(45deg, transparent, transparent 10px, ${rndHex()} 10px, ${rndHex()} 20px)`,
                `repeating-radial-gradient(circle at 50% 50%, ${rndHex()}, ${rndHex()} 10px, ${rndHex()} 20px)`,
                `linear-gradient(45deg, ${rndHex()} 25%, transparent 25%), linear-gradient(-45deg, ${rndHex()} 25%, transparent 25%), linear-gradient(45deg, transparent 75%, ${rndHex()} 75%), linear-gradient(-45deg, transparent 75%, ${rndHex()} 75%)`,
                `radial-gradient(circle at 25% 25%, ${rndHex()} 2px, transparent 3px), radial-gradient(circle at 75% 75%, ${rndHex()} 2px, transparent 3px)`
            ];
            currentStyles.backgroundImage = rndItem(patterns);
            currentStyles.webkitBackgroundClip = '';
            currentStyles.webkitTextFillColor = '';
            currentStyles.backgroundClip = 'border-box';
            applyStyles();
            saveToHistory();
            showToast('Desen oluşturuldu');
        }

        function randomBgBlend() {
            updateStyle('backgroundBlendMode', rndItem(['multiply', 'screen', 'overlay', 'darken', 'lighten', 'color-dodge', 'difference', 'hue', 'saturation']));
        }

        function randomMultiBorder() {
            const styles = ['solid', 'dashed', 'dotted', 'double', 'groove', 'ridge'];
            ['borderTop', 'borderBottom', 'borderLeft', 'borderRight'].forEach(side => {
                currentStyles[side] = `${rndInt(1, 6)}px ${rndItem(styles)} ${rndHex()}`;
            });
            applyStyles();
            saveToHistory();
            showToast('Çerçeve oluşturuldu');
        }

        function randomBorderColor() {
            const color = rndHex();
            ['borderTop', 'borderBottom', 'borderLeft', 'borderRight'].forEach(side => {
                const parts = currentStyles[side].split(' ');
                if (parts.length >= 2) {
                    currentStyles[side] = `${parts[0]} ${parts[1]} ${color}`;
                }
            });
            applyStyles();
            saveToHistory();
        }

        function randomOutline() {
            currentStyles.outlineWidth = `${rndInt(1, 5)}px`;
            currentStyles.outlineStyle = rndItem(['solid', 'dashed', 'dotted', 'double', 'groove', 'ridge']);
            currentStyles.outlineColor = rndHex();
            currentStyles.outlineOffset = `${rndInt(0, 8)}px`;
            applyStyles();
            saveToHistory();
        }

        function randomBorderRadius() {
            const mode = rndItem(['uniform', 'crazy']);
            if (mode === 'uniform') {
                const r = rndInt(0, 50);
                ['borderTopLeftRadius', 'borderTopRightRadius', 'borderBottomLeftRadius', 'borderBottomRightRadius'].forEach(p => {
                    currentStyles[p] = r + 'px';
                });
                $('borderRadiusAll').value = r;
                $('borderRadiusVal').textContent = r + 'px';
            } else {
                ['borderTopLeftRadius', 'borderTopRightRadius', 'borderBottomLeftRadius', 'borderBottomRightRadius'].forEach(p => {
                    currentStyles[p] = rndInt(0, 80) + 'px';
                });
            }
            applyStyles();
            saveToHistory();
            showToast('Kenar yuvarlatması oluşturuldu');
        }

        function randomTransform() {
            $('rotateRange').value = $('rotate').value = rndInt(-30, 30);
            $('scaleRange').value = rndFloat(0.7, 1.5);
            $('skewX').value = rndInt(-15, 15);
            $('skewY').value = rndInt(-15, 15);
            $('translateX').value = rndInt(-20, 20);
            $('translateY').value = rndInt(-20, 20);
            updateTransform();
            showToast('Dönüşüm oluşturuldu');
        }

        function randomBoxShadow() {
            const count = rndInt(1, 3);
            let shadows = [];
            for (let i = 0; i < count; i++) {
                const inset = Math.random() > 0.7 ? 'inset ' : '';
                shadows.push(`${inset}${rndInt(-10, 10)}px ${rndInt(-10, 10)}px ${rndInt(5, 30)}px ${rndInt(-5, 10)}px ${rndHex()}`);
            }
            currentStyles.boxShadow = shadows.join(', ');
            applyStyles();
            saveToHistory();
            showToast('Kutu gölgesi oluşturuldu');
        }

        function randomBoxShadowColor() {
            const color = rndHex();
            const parts = currentStyles.boxShadow.split(')');
            if (parts.length > 1) {
                currentStyles.boxShadow = currentStyles.boxShadow.replace(/#[0-9a-fA-F]{3,8}/g, color);
            } else {
                currentStyles.boxShadow = currentStyles.boxShadow.replace(/#[0-9a-fA-F]{3,8}/g, color);
            }
            applyStyles();
            saveToHistory();
        }

        function randomMultiShadow() {
            let shadows = [];
            const count = rndInt(2, 5);
            for (let i = 0; i < count; i++) {
                shadows.push(`${rndInt(-15, 15)}px ${rndInt(-15, 15)}px ${rndInt(5, 40)}px ${rndInt(-5, 10)}px ${rndHex()}`);
            }
            currentStyles.boxShadow = shadows.join(', ');
            applyStyles();
            saveToHistory();
            showToast('Çoklu gölge oluşturuldu');
        }

        function randomInsetShadow() {
            currentStyles.boxShadow = `inset ${rndInt(-10, 10)}px ${rndInt(-10, 10)}px ${rndInt(10, 40)}px ${rndInt(0, 10)}px ${rndHex()}`;
            applyStyles();
            saveToHistory();
            showToast('İç gölge oluşturuldu');
        }

        // ===== ANIMATIONS =====
        const animationKeyframesMap = {
            bounce: `@keyframes bounce {
    0%, 20%, 50%, 80%, 100% { transform: translateY(0); }
    40% { transform: translateY(-30px); }
    60% { transform: translateY(-15px); }
}`,
            pulse: `@keyframes pulse {
    0% { transform: scale(1); }
    50% { transform: scale(1.08); }
    100% { transform: scale(1); }
}`,
            shake: `@keyframes shake {
    0%, 100% { transform: translateX(0); }
    10%, 30%, 50%, 70%, 90% { transform: translateX(-8px); }
    20%, 40%, 60%, 80% { transform: translateX(8px); }
}`,
            fadeIn: `@keyframes fadeIn {
    0% { opacity: 0; }
    100% { opacity: 1; }
}`,
            fadeOut: `@keyframes fadeOut {
    0% { opacity: 1; }
    100% { opacity: 0; }
}`,
            slideInLeft: `@keyframes slideInLeft {
    0% { transform: translateX(-100%); opacity: 0; }
    100% { transform: translateX(0); opacity: 1; }
}`,
            slideInRight: `@keyframes slideInRight {
    0% { transform: translateX(100%); opacity: 0; }
    100% { transform: translateX(0); opacity: 1; }
}`,
            rotateIn: `@keyframes rotateIn {
    0% { transform: rotate(-360deg) scale(0); opacity: 0; }
    100% { transform: rotate(0) scale(1); opacity: 1; }
}`,
            zoomIn: `@keyframes zoomIn {
    0% { transform: scale(0.3); opacity: 0; }
    50% { opacity: 1; }
    100% { transform: scale(1); }
}`,
            flip: `@keyframes flip {
    0% { transform: perspective(400px) rotateY(0); }
    50% { transform: perspective(400px) rotateY(180deg); }
    100% { transform: perspective(400px) rotateY(360deg); }
}`,
            swing: `@keyframes swing {
    20% { transform: rotate(15deg); }
    40% { transform: rotate(-10deg); }
    60% { transform: rotate(5deg); }
    80% { transform: rotate(-5deg); }
    100% { transform: rotate(0deg); }
}`,
            rubberBand: `@keyframes rubberBand {
    0% { transform: scaleX(1) scaleY(1); }
    30% { transform: scaleX(1.25) scaleY(0.75); }
    40% { transform: scaleX(0.75) scaleY(1.25); }
    50% { transform: scaleX(1.15) scaleY(0.85); }
    65% { transform: scaleX(0.95) scaleY(1.05); }
    75% { transform: scaleX(1.05) scaleY(0.95); }
    100% { transform: scaleX(1) scaleY(1); }
}`,
            jello: `@keyframes jello {
    0%, 100% { transform: skewX(0) skewY(0); }
    30% { transform: skewX(-12.5deg) skewY(-12.5deg); }
    40% { transform: skewX(6.25deg) skewY(6.25deg); }
    50% { transform: skewX(-3.125deg) skewY(-3.125deg); }
    65% { transform: skewX(1.5625deg) skewY(1.5625deg); }
    75% { transform: skewX(-0.78125deg) skewY(-0.78125deg); }
}`,
            heartBeat: `@keyframes heartBeat {
    0% { transform: scale(1); }
    14% { transform: scale(1.3); }
    28% { transform: scale(1); }
    42% { transform: scale(1.3); }
    70% { transform: scale(1); }
}`,
            float: `@keyframes float {
    0%, 100% { transform: translateY(0); }
    50% { transform: translateY(-20px); }
}`,
            glitch: `@keyframes glitch {
    0%, 100% { transform: translate(0); }
    20% { transform: translate(-3px, 3px); }
    40% { transform: translate(3px, -3px); }
    60% { transform: translate(-2px, -2px); }
    80% { transform: translate(2px, 2px); }
}`,
            neonPulse: `@keyframes neonPulse {
    0%, 100% { box-shadow: 0 0 5px #fff, 0 0 10px #fff, 0 0 20px #64ffda, 0 0 40px #64ffda; }
    50% { box-shadow: 0 0 10px #fff, 0 0 20px #fff, 0 0 40px #64ffda, 0 0 80px #64ffda; }
}`,
            typewriter: `@keyframes typewriter {
    0% { width: 0; }
    100% { width: 100%; }
}`
        };

        let injectedKeyframes = new Set();

        function injectKeyframes(name) {
            if (injectedKeyframes.has(name)) return;
            const kf = animationKeyframesMap[name];
            if (kf) {
                const style = document.createElement('style');
                style.textContent = kf;
                style.setAttribute('data-keyframe', name);
                document.head.appendChild(style);
                injectedKeyframes.add(name);
            }
        }

        function applyAnimation(name) {
            injectKeyframes(name);
            const duration = $('animationDurationRange').value;
            const timing = $('animationTimingFunction').value;
            const iteration = $('animationIterationCount').value;
            const direction = $('animationDirection').value;

            currentStyles.animationName = name;
            currentStyles.animationDuration = duration + 's';
            currentStyles.animationTimingFunction = timing;
            currentStyles.animationIterationCount = iteration;
            currentStyles.animationDirection = direction;

            // Force restart
            previewBox.style.animation = 'none';
            previewBox.offsetHeight; // trigger reflow
            applyStyles();
            saveToHistory();
        }

        function randomAnimation() {
            const names = Object.keys(animationKeyframesMap);
            const name = rndItem(names);
            $('presetAnimation').value = name;
            $('animationDurationRange').value = rndFloat(0.5, 3);
            $('animDurationVal').textContent = $('animationDurationRange').value + 's';
            $('animationTimingFunction').value = rndItem(['ease', 'linear', 'ease-in', 'ease-out', 'ease-in-out']);
            $('animationIterationCount').value = rndItem(['1', '2', '3', 'infinite']);
            applyAnimation(name);
            showToast(`Animasyon: ${name}`);
        }

        function randomTimingFunction() {
            const tf = rndItem(['ease', 'linear', 'ease-in', 'ease-out', 'ease-in-out', 'cubic-bezier(0.68, -0.55, 0.265, 1.55)']);
            $('animationTimingFunction').value = tf;
            currentStyles.animationTimingFunction = tf;
            applyStyles();
            saveToHistory();
        }

        function randomIterationCount() {
            const ic = rndItem(['1', '2', '3', '5', 'infinite']);
            $('animationIterationCount').value = ic;
            currentStyles.animationIterationCount = ic;
            applyStyles();
            saveToHistory();
        }

        function stopAnimation() {
            currentStyles.animationName = 'none';
            previewBox.style.animation = 'none';
            applyStyles();
            saveToHistory();
            showToast('Animasyon durduruldu', 'info');
        }

        function randomClipPath() {
            const paths = [
                'polygon(50% 0%, 100% 50%, 50% 100%, 0% 50%)',
                'circle(50% at 50% 50%)',
                'ellipse(40% 50% at 50% 50%)',
                'polygon(50% 0%, 100% 100%, 0% 100%)',
                'polygon(25% 0%, 75% 0%, 100% 50%, 75% 100%, 25% 100%, 0% 50%)',
                'polygon(50% 0%, 61% 35%, 98% 35%, 68% 57%, 79% 91%, 50% 70%, 21% 91%, 32% 57%, 2% 35%, 39% 35%)',
                'inset(5% 5% 5% 5% round 10px)',
                `polygon(${rndInt(10,40)}% 0%, ${rndInt(60,90)}% 0%, 100% ${rndInt(10,40)}%, 100% ${rndInt(60,90)}%, ${rndInt(60,90)}% 100%, ${rndInt(10,40)}% 100%, 0% ${rndInt(60,90)}%, 0% ${rndInt(10,40)}%)`
            ];
            updateStyle('clipPath', rndItem(paths));
            showToast('Clip-path oluşturuldu');
        }

        function randomTextOpacity() {
            const val = rndFloat(0.3, 1.0);
            currentStyles.opacity = val.toString();
            $('textOpacityRange').value = val;
            $('textOpacityVal').textContent = val;
            applyStyles();
            saveToHistory();
        }

        function randomTextGradient() {
            const count = rndInt(2, 4);
            textGradientColors = [];
            for (let i = 0; i < count; i++) {
                textGradientColors.push({ color: rndHex(), stop: Math.round(i / (count - 1) * 100) });
            }
            $('textGradientAngle').value = rndInt(0, 360);
            $('textGradientType').value = rndItem(['linear', 'radial']);
            initGradientPickers('textGradientColors', textGradientColors, 'text');
            updateTextGradient();
            showToast('Metin gradyanı oluşturuldu');
        }

        function randomTextImageFill() {
            const images = [
                'https://picsum.photos/seed/' + rndInt(1,1000) + '/400/300',
                'https://picsum.photos/seed/' + rndInt(1,1000) + '/500/400'
            ];
            currentStyles.backgroundImage = `url(${rndItem(images)})`;
            currentStyles.backgroundSize = 'cover';
            currentStyles.webkitBackgroundClip = 'text';
            currentStyles.backgroundClip = 'text';
            currentStyles.webkitTextFillColor = 'transparent';
            applyStyles();
            saveToHistory();
            showToast('Metin resim dolgusu oluşturuldu');
        }

        function randomFilter() {
            $('filterBlurRange').value = rndInt(0, 3);
            $('filterBrightnessRange').value = rndInt(70, 150);
            $('filterContrastRange').value = rndInt(80, 150);
            $('filterSaturateRange').value = rndInt(60, 200);
            $('filterHueRotateRange').value = rndInt(0, 360);
            $('filterInvertRange').value = rndInt(0, 30);
            $('filterSepiaRange').value = rndInt(0, 50);
            $('filterGrayscaleRange').value = rndInt(0, 40);
            updateFilter();
            showToast('Filtreler oluşturuldu');
        }

        function randomCursor() {
            const cursors = ['auto', 'pointer', 'crosshair', 'move', 'text', 'not-allowed', 'grab', 'zoom-in', 'zoom-out', 'wait', 'help'];
            updateStyle('cursor', rndItem(cursors));
        }

        function randomEffect() {
            randomFilter();
            randomCursor();
        }

        // ===== PALETTE =====
        function generatePalette() {
            const base = pickers.baseColor ? pickers.baseColor.color.hexString : '#64ffda';
            const type = $('paletteType').value;
            const size = parseInt($('paletteSize').value) || 5;
            let colors = [];

            try {
                const hsl = chroma(base).hsl();
                const baseHue = hsl[0] || 0;

                if (type === 'monochromatic') {
                    colors = chroma.scale([chroma(base).darken(2), base, chroma(base).brighten(2)]).colors(size);
                } else if (type === 'analogous') {
                    for (let i = 0; i < size; i++) {
                        colors.push(chroma.hsl((baseHue + i * 30) % 360, hsl[1] || 0.7, hsl[2] || 0.5).hex());
                    }
                } else if (type === 'complementary') {
                    colors.push(base);
                    colors.push(chroma.hsl((baseHue + 180) % 360, hsl[1] || 0.7, hsl[2] || 0.5).hex());
                    for (let i = 2; i < size; i++) {
                        colors.push(chroma(base).brighten(i * 0.4).hex());
                    }
                } else if (type === 'triadic') {
                    for (let i = 0; i < size; i++) {
                        colors.push(chroma.hsl((baseHue + i * 120) % 360, hsl[1] || 0.7, hsl[2] || 0.5).hex());
                    }
                } else if (type === 'split-complementary') {
                    colors.push(base);
                    colors.push(chroma.hsl((baseHue + 150) % 360, hsl[1] || 0.7, hsl[2] || 0.5).hex());
                    colors.push(chroma.hsl((baseHue + 210) % 360, hsl[1] || 0.7, hsl[2] || 0.5).hex());
                    for (let i = 3; i < size; i++) {
                        colors.push(chroma(base).brighten(i * 0.3).hex());
                    }
                } else if (type === 'tetradic') {
                    for (let i = 0; i < size; i++) {
                        colors.push(chroma.hsl((baseHue + i * 90) % 360, hsl[1] || 0.7, hsl[2] || 0.5).hex());
                    }
                }
            } catch(e) {
                colors = [base];
                for (let i = 1; i < size; i++) colors.push(rndHex());
            }

            const preview = $('palettePreview');
            preview.innerHTML = colors.map(c =>
                `<div class="palette-color" style="background-color:${c};" data-color="${c}" title="${c}">
                    <span class="tooltip">${c}</span>
                </div>`
            ).join('');

            // Click to copy color
            preview.querySelectorAll('.palette-color').forEach(el => {
                el.addEventListener('click', () => {
                    navigator.clipboard.writeText(el.dataset.color).then(() => {
                        showToast(`Renk kopyalandı: ${el.dataset.color}`);
                    }).catch(() => {});
                });
            });
        }

        // ===== THEME PRESETS =====
        function applyThemePreset(theme) {
            // Reset first
            currentStyles = getDefaultStyles();

            switch(theme) {
                case 'neon':
                    Object.assign(currentStyles, {
                        fontFamily: "'Orbitron', sans-serif",
                        fontSize: '36px',
                        fontWeight: '700',
                        color: '#0ff',
                        backgroundColor: '#0a0a2e',
                        textShadow: '0 0 10px #0ff, 0 0 20px #0ff, 0 0 40px #0ff, 0 0 80px #0ff',
                        borderTop: '2px solid #0ff',
                        borderBottom: '2px solid #0ff',
                        borderLeft: '2px solid #0ff',
                        borderRight: '2px solid #0ff',
                        boxShadow: '0 0 10px #0ff, inset 0 0 10px rgba(0,255,255,0.1)',
                        borderTopLeftRadius: '12px',
                        borderTopRightRadius: '12px',
                        borderBottomLeftRadius: '12px',
                        borderBottomRightRadius: '12px',
                        textTransform: 'uppercase',
                        letterSpacing: '4px'
                    });
                    break;

                case 'minimal':
                    Object.assign(currentStyles, {
                        fontFamily: "'Inter', sans-serif",
                        fontSize: '28px',
                        fontWeight: '300',
                        color: '#333333',
                        backgroundColor: '#fafafa',
                        textShadow: 'none',
                        borderTop: '1px solid #eee',
                        borderBottom: '1px solid #eee',
                        borderLeft: '1px solid #eee',
                        borderRight: '1px solid #eee',
                        boxShadow: '0 1px 3px rgba(0,0,0,0.04)',
                        borderTopLeftRadius: '8px',
                        borderTopRightRadius: '8px',
                        borderBottomLeftRadius: '8px',
                        borderBottomRightRadius: '8px',
                        letterSpacing: '1px'
                    });
                    break;

                case 'vintage':
                    Object.assign(currentStyles, {
                        fontFamily: "'Kaushan Script', cursive",
                        fontSize: '38px',
                        fontWeight: '400',
                        color: '#5c3317',
                        backgroundColor: '#f4e9d8',
                        textShadow: '2px 2px 0px #d4a574',
                        borderTop: '3px double #8b6914',
                        borderBottom: '3px double #8b6914',
                        borderLeft: '3px double #8b6914',
                        borderRight: '3px double #8b6914',
                        boxShadow: '0 4px 8px rgba(92,51,23,0.2)',
                        borderTopLeftRadius: '4px',
                        borderTopRightRadius: '4px',
                        borderBottomLeftRadius: '4px',
                        borderBottomRightRadius: '4px'
                    });
                    break;

                case 'glassmorphism':
                    Object.assign(currentStyles, {
                        fontFamily: "'Inter', sans-serif",
                        fontSize: '30px',
                        fontWeight: '500',
                        color: '#ffffff',
                        backgroundColor: 'rgba(255,255,255,0.1)',
                        backdropFilter: 'blur(12px)',
                        textShadow: '0 1px 2px rgba(0,0,0,0.1)',
                        borderTop: '1px solid rgba(255,255,255,0.2)',
                        borderBottom: '1px solid rgba(255,255,255,0.2)',
                        borderLeft: '1px solid rgba(255,255,255,0.2)',
                        borderRight: '1px solid rgba(255,255,255,0.2)',
                        boxShadow: '0 8px 32px rgba(0,0,0,0.12)',
                        borderTopLeftRadius: '20px',
                        borderTopRightRadius: '20px',
                        borderBottomLeftRadius: '20px',
                        borderBottomRightRadius: '20px'
                    });
                    break;

                case 'neumorphism':
                    Object.assign(currentStyles, {
                        fontFamily: "'Poppins', sans-serif",
                        fontSize: '28px',
                        fontWeight: '600',
                        color: '#6b7b99',
                        backgroundColor: '#e0e5ec',
                        textShadow: '1px 1px 2px rgba(255,255,255,0.8)',
                        borderTop: 'none',
                        borderBottom: 'none',
                        borderLeft: 'none',
                        borderRight: 'none',
                        boxShadow: '8px 8px 16px #b8bec7, -8px -8px 16px #ffffff',
                        borderTopLeftRadius: '20px',
                        borderTopRightRadius: '20px',
                        borderBottomLeftRadius: '20px',
                        borderBottomRightRadius: '20px'
                    });
                    break;

                case 'cyberpunk':
                    Object.assign(currentStyles, {
                        fontFamily: "'Press Start 2P', monospace",
                        fontSize: '22px',
                        fontWeight: '400',
                        color: '#ff2d6a',
                        backgroundColor: '#0d0221',
                        textShadow: '0 0 8px #ff2d6a, 0 0 20px #ff2d6a, 3px 3px 0px #00f0ff',
                        borderTop: '2px solid #ff2d6a',
                        borderBottom: '4px solid #00f0ff',
                        borderLeft: '2px solid #ff2d6a',
                        borderRight: '2px solid #00f0ff',
                        boxShadow: '0 0 15px rgba(255,45,106,0.4), inset 0 0 15px rgba(0,240,255,0.1)',
                        borderTopLeftRadius: '4px',
                        borderTopRightRadius: '4px',
                        borderBottomLeftRadius: '4px',
                        borderBottomRightRadius: '4px',
                        textTransform: 'uppercase',
                        letterSpacing: '3px'
                    });
                    break;

                case 'nature':
                    Object.assign(currentStyles, {
                        fontFamily: "'Space Grotesk', sans-serif",
                        fontSize: '32px',
                        fontWeight: '500',
                        color: '#2d5016',
                        backgroundColor: '#e8f5e9',
                        backgroundImage: 'linear-gradient(135deg, #e8f5e9 0%, #c8e6c9 100%)',
                        textShadow: '1px 1px 2px rgba(45,80,22,0.15)',
                        borderTop: '2px solid #81c784',
                        borderBottom: '2px solid #81c784',
                        borderLeft: '2px solid #81c784',
                        borderRight: '2px solid #81c784',
                        boxShadow: '0 4px 12px rgba(45,80,22,0.15)',
                        borderTopLeftRadius: '16px',
                        borderTopRightRadius: '16px',
                        borderBottomLeftRadius: '16px',
                        borderBottomRightRadius: '16px'
                    });
                    break;

                case 'ocean':
                    Object.assign(currentStyles, {
                        fontFamily: "'Poppins', sans-serif",
                        fontSize: '34px',
                        fontWeight: '600',
                        color: '#ffffff',
                        backgroundImage: 'linear-gradient(135deg, #0077b6, #023e8a, #0096c7)',
                        textShadow: '0 2px 4px rgba(0,0,0,0.3)',
                        borderTop: '2px solid rgba(255,255,255,0.3)',
                        borderBottom: '2px solid rgba(255,255,255,0.3)',
                        borderLeft: '2px solid rgba(255,255,255,0.3)',
                        borderRight: '2px solid rgba(255,255,255,0.3)',
                        boxShadow: '0 8px 24px rgba(0,119,182,0.4)',
                        borderTopLeftRadius: '16px',
                        borderTopRightRadius: '16px',
                        borderBottomLeftRadius: '16px',
                        borderBottomRightRadius: '16px'
                    });
                    break;

                case 'sunset':
                    Object.assign(currentStyles, {
                        fontFamily: "'Lobster', cursive",
                        fontSize: '40px',
                        fontWeight: '400',
                        color: '#fff',
                        backgroundImage: 'linear-gradient(135deg, #ff512f, #f09819, #dd2476)',
                        textShadow: '2px 2px 8px rgba(0,0,0,0.3)',
                        borderTop: 'none',
                        borderBottom: 'none',
                        borderLeft: 'none',
                        borderRight: 'none',
                        boxShadow: '0 10px 30px rgba(255,81,47,0.4)',
                        borderTopLeftRadius: '24px',
                        borderTopRightRadius: '24px',
                        borderBottomLeftRadius: '24px',
                        borderBottomRightRadius: '24px'
                    });
                    break;

                case 'dark-elegant':
                    Object.assign(currentStyles, {
                        fontFamily: "'Space Grotesk', sans-serif",
                        fontSize: '30px',
                        fontWeight: '500',
                        color: '#d4af37',
                        backgroundColor: '#1a1a2e',
                        textShadow: '0 0 6px rgba(212,175,55,0.3)',
                        borderTop: '1px solid rgba(212,175,55,0.3)',
                        borderBottom: '1px solid rgba(212,175,55,0.3)',
                        borderLeft: '1px solid rgba(212,175,55,0.3)',
                        borderRight: '1px solid rgba(212,175,55,0.3)',
                        boxShadow: '0 8px 24px rgba(0,0,0,0.4), inset 0 1px 0 rgba(212,175,55,0.1)',
                        borderTopLeftRadius: '12px',
                        borderTopRightRadius: '12px',
                        borderBottomLeftRadius: '12px',
                        borderBottomRightRadius: '12px',
                        letterSpacing: '2px'
                    });
                    break;
            }

            applyStyles();
            saveToHistory();
            showToast(`Tema uygulandı: ${theme}`);
        }

        // ===== CHAOS ENGINE =====
        function autoGenerateStyles(mode) {
            const checks = {
                font: $('chaosFont').checked,
                bg: $('chaosBackground').checked,
                border: $('chaosBorder').checked,
                effects: $('chaosEffects').checked,
                animation: $('chaosAnimation').checked,
                clip: $('chaosClip').checked,
                transform: $('chaosTransform').checked,
                shadow: $('chaosBoxShadow').checked,
                textGradient: $('chaosTextGradient').checked,
                textImage: $('chaosTextImage').checked,
                opacity: $('chaosOpacity').checked,
                layout: $('chaosLayout') ? $('chaosLayout').checked : false
            };

            if (mode === 'chaos' || mode === 'random') {
                if (checks.font) randomFont();
                if (checks.bg) { Math.random() > 0.5 ? randomGradient() : randomBgColor(); }
                if (checks.border) randomMultiBorder();
                if (checks.effects) randomFilter();
                if (checks.animation) randomAnimation();
                if (checks.clip && Math.random() > 0.6) randomClipPath();
                if (checks.transform) randomTransform();
                if (checks.shadow) randomBoxShadow();
                if (checks.textGradient && Math.random() > 0.5) randomTextGradient();
                if (checks.opacity && Math.random() > 0.6) randomTextOpacity();
                randomBorderRadius();
                randomTextShadow();
                randomColor();
            }

            if (mode === 'chaos') {
                showToast('🔥 KAOS MODU AKTİF!');
            } else if (mode === 'random') {
                showToast('✨ Otomatik stil oluşturuldu');
            }
        }

        // ===== KEYBOARD SHORTCUTS =====
        document.addEventListener('keydown', e => {
            if ((e.ctrlKey || e.metaKey) && e.key === 'z' && !e.shiftKey) {
                e.preventDefault();
                undo();
            } else if ((e.ctrlKey || e.metaKey) && (e.key === 'y' || (e.key === 'z' && e.shiftKey))) {
                e.preventDefault();
                redo();
            } else if ((e.ctrlKey || e.metaKey) && e.key === 's') {
                e.preventDefault();
                navigator.clipboard.writeText(cssOutput.value).then(() => showToast('CSS kopyalandı!')).catch(() => {});
            }
        });

        // ===== EVENT LISTENERS =====

        // Action buttons
        $$('[data-action]').forEach(btn => {
            btn.addEventListener('click', () => {
                const action = btn.dataset.action;
                switch(action) {
                    case 'undo': undo(); break;
                    case 'redo': redo(); break;
                    case 'toggle-theme':
                        currentTheme = currentTheme === 'dark' ? 'light' : 'dark';
                        document.documentElement.setAttribute('data-theme', currentTheme);
                        btn.querySelector('i').className = currentTheme === 'dark' ? 'fas fa-moon' : 'fas fa-sun';
                        showToast(`Tema: ${currentTheme === 'dark' ? 'Koyu' : 'Açık'}`, 'info');
                        break;
                    case 'reset-all':
                        currentStyles = getDefaultStyles();
                        // Reset all range sliders
                        if ($('fontSizeRange')) $('fontSizeRange').value = 30;
                        if ($('fontWeightRange')) $('fontWeightRange').value = 400;
                        if ($('lineHeightRange')) $('lineHeightRange').value = 1.5;
                        if ($('backgroundOpacityRange')) $('backgroundOpacityRange').value = 1;
                        if ($('textOpacityRange')) $('textOpacityRange').value = 1;
                        if ($('rotateRange')) $('rotateRange').value = 0;
                        if ($('scaleRange')) $('scaleRange').value = 1;
                        if ($('borderRadiusAll')) $('borderRadiusAll').value = 10;
                        if ($('filterBlurRange')) $('filterBlurRange').value = 0;
                        if ($('filterBrightnessRange')) $('filterBrightnessRange').value = 100;
                        if ($('filterContrastRange')) $('filterContrastRange').value = 100;
                        if ($('filterSaturateRange')) $('filterSaturateRange').value = 100;
                        if ($('filterHueRotateRange')) $('filterHueRotateRange').value = 0;
                        if ($('filterInvertRange')) $('filterInvertRange').value = 0;
                        if ($('filterSepiaRange')) $('filterSepiaRange').value = 0;
                        if ($('filterGrayscaleRange')) $('filterGrayscaleRange').value = 0;
                        if ($('backdropBlurRange')) $('backdropBlurRange').value = 0;
                        previewBox.style.animation = 'none';
                        applyStyles();
                        saveToHistory();
                        showToast('Tüm stiller sıfırlandı', 'info');
                        break;
                    case 'download-css': {
                        const blob = new Blob([cssOutput.value], { type: 'text/css' });
                        const url = URL.createObjectURL(blob);
                        const a = document.createElement('a');
                        a.href = url; a.download = 'k3n4n-styles.css'; a.click();
                        URL.revokeObjectURL(url);
                        showToast('CSS dosyası indirildi');
                        break;
                    }
                    case 'download-html': {
                        const html = `<!DOCTYPE html>\n<html lang="tr">\n<head>\n    <meta charset="UTF-8">\n    <title>K3N4N V6.0 Preview</title>\n    <style>\n${cssOutput.value}\n    </style>\n</head>\n<body style="display:flex;justify-content:center;align-items:center;min-height:100vh;margin:0;background:#1a1a2e;">\n    ${htmlPreviewArea.textContent}\n</body>\n</html>`;
                        const blob = new Blob([html], { type: 'text/html' });
                        const url = URL.createObjectURL(blob);
                        const a = document.createElement('a');
                        a.href = url; a.download = 'k3n4n-preview.html'; a.click();
                        URL.revokeObjectURL(url);
                        showToast('HTML dosyası indirildi');
                        break;
                    }
                    case 'export-styles': {
                        const data = JSON.stringify(currentStyles, null, 2);
                        const blob = new Blob([data], { type: 'application/json' });
                        const url = URL.createObjectURL(blob);
                        const a = document.createElement('a');
                        a.href = url; a.download = 'k3n4n-styles.json'; a.click();
                        URL.revokeObjectURL(url);
                        showToast('Stiller dışa aktarıldı');
                        break;
                    }
                    case 'import-styles':
                        $('import-styles').click();
                        break;
                }
            });
        });

        // Style target buttons
        $$('[data-style-target]').forEach(btn => {
            btn.addEventListener('click', () => {
                const target = btn.dataset.styleTarget;
                switch(target) {
                    case 'random-font': randomFont(); break;
                    case 'random-color': randomColor(); break;
                    case 'random-text-shadow': randomTextShadow(); break;
                    case 'random-text-decoration': randomTextDecoration(); break;
                    case 'random-spacing': randomSpacing(); break;
                    case 'random-align': randomAlign(); break;
                    case 'random-line-height': randomLineHeight(); break;
                    case 'random-text-transform': randomTextTransform(); break;
                    case 'random-bg-color': randomBgColor(); break;
                    case 'random-gradient': randomGradient(); break;
                    case 'random-bg-gif': randomBgGif(); break;
                    case 'random-bg-position': randomBgPosition(); break;
                    case 'random-bg-size': randomBgSize(); break;
                    case 'random-bg-opacity': randomBgOpacity(); break;
                    case 'random-bg-pattern': randomBgPattern(); break;
                    case 'random-bg-blend': randomBgBlend(); break;
                    case 'random-multi-border': randomMultiBorder(); break;
                    case 'random-border-color': randomBorderColor(); break;
                    case 'random-outline': randomOutline(); break;
                    case 'random-border-radius': randomBorderRadius(); break;
                    case 'random-transform': randomTransform(); break;
                    case 'reset-transform':
                        $('rotateRange').value = $('rotate').value = 0;
                        $('scaleRange').value = 1;
                        $('skewX').value = 0; $('skewY').value = 0;
                        $('translateX').value = 0; $('translateY').value = 0;
                        updateTransform();
                        showToast('Dönüşüm sıfırlandı', 'info');
                        break;
                    case 'random-box-shadow': randomBoxShadow(); break;
                    case 'random-box-shadow-color': randomBoxShadowColor(); break;
                    case 'random-multi-shadow': randomMultiShadow(); break;
                    case 'random-inset-shadow': randomInsetShadow(); break;
                    case 'random-animation': randomAnimation(); break;
                    case 'random-timing-function': randomTimingFunction(); break;
                    case 'random-iteration-count': randomIterationCount(); break;
                    case 'stop-animation': stopAnimation(); break;
                    case 'random-clip-path': randomClipPath(); break;
                    case 'reset-clip':
                        updateStyle('clipPath', 'none');
                        showToast('Clip-path sıfırlandı', 'info');
                        break;
                    case 'random-text-opacity': randomTextOpacity(); break;
                    case 'random-text-gradient': randomTextGradient(); break;
                    case 'random-text-image-fill': randomTextImageFill(); break;
                    case 'reset-text-fill':
                        currentStyles.backgroundImage = 'none';
                        currentStyles.webkitBackgroundClip = '';
                        currentStyles.webkitTextFillColor = '';
                        currentStyles.backgroundClip = 'border-box';
                        applyStyles(); saveToHistory();
                        showToast('Metin dolgusu sıfırlandı', 'info');
                        break;
                    case 'random-filter': randomFilter(); break;
                    case 'random-cursor': randomCursor(); break;
                    case 'random-effect': randomEffect(); break;
                    case 'reset-filters':
                        $('filterBlurRange').value = 0;
                        $('filterBrightnessRange').value = 100;
                        $('filterContrastRange').value = 100;
                        $('filterSaturateRange').value = 100;
                        $('filterHueRotateRange').value = 0;
                        $('filterInvertRange').value = 0;
                        $('filterSepiaRange').value = 0;
                        $('filterGrayscaleRange').value = 0;
                        $('backdropBlurRange').value = 0;
                        updateFilter();
                        showToast('Filtreler sıfırlandı', 'info');
                        break;
                    case 'generate-palette': generatePalette(); break;
                    case 'random-palette':
                        if (pickers.baseColor) pickers.baseColor.color.hexString = rndHex();
                        generatePalette();
                        showToast('Palet oluşturuldu');
                        break;
                    case 'auto-generate': autoGenerateStyles('random'); break;
                    case 'max-chaos': autoGenerateStyles('chaos'); break;
                    case 'auto-theme-neon': applyThemePreset('neon'); break;
                    case 'auto-theme-minimal': applyThemePreset('minimal'); break;
                    case 'auto-theme-vintage': applyThemePreset('vintage'); break;
                    case 'auto-theme-glassmorphism': applyThemePreset('glassmorphism'); break;
                    case 'auto-theme-neumorphism': applyThemePreset('neumorphism'); break;
                    case 'auto-theme-cyberpunk': applyThemePreset('cyberpunk'); break;
                    case 'auto-theme-nature': applyThemePreset('nature'); break;
                    case 'auto-theme-ocean': applyThemePreset('ocean'); break;
                    case 'auto-theme-sunset': applyThemePreset('sunset'); break;
                    case 'auto-theme-dark-elegant': applyThemePreset('dark-elegant'); break;
                }
            });
        });

        // Direct style prop inputs
        $$('[data-style-prop]').forEach(input => {
            const handler = () => {
                const prop = input.dataset.styleProp;
                const unit = input.dataset.styleUnit || '';
                if (prop === 'transform') {
                    updateTransform();
                } else if (prop === 'filter') {
                    updateFilter();
                } else {
                    updateStyle(prop, input.value, unit);
                }
            };
            input.addEventListener('input', handler);
            input.addEventListener('change', handler);
        });

        // Range slider sync
        function syncRange(rangeId, valueDisplay, callback) {
            const range = $(rangeId);
            if (!range) return;
            range.addEventListener('input', () => {
                if (valueDisplay) {
                    const el = $(valueDisplay);
                    if (el) el.textContent = range.value + (range.dataset.unit || '');
                }
                if (callback) callback(range.value);
            });
        }

        syncRange('fontSizeRange', 'fontSizeVal', v => {
            $('fontSize').value = v;
            $('fontSizeVal').textContent = v + 'px';
            updateStyle('fontSize', v, 'px');
        });

        syncRange('fontWeightRange', 'fontWeightVal', v => {
            $('fontWeight').value = v;
            $('fontWeightVal').textContent = v;
            updateStyle('fontWeight', v);
        });

        if ($('fontWeight')) {
            $('fontWeight').addEventListener('change', () => {
                const v = $('fontWeight').value;
                $('fontWeightRange').value = v;
                $('fontWeightVal').textContent = v;
                updateStyle('fontWeight', v);
            });
        }

        syncRange('lineHeightRange', 'lineHeightVal', v => {
            $('lineHeightVal').textContent = v;
            updateStyle('lineHeight', v);
        });

        syncRange('backgroundOpacityRange', 'bgOpacityVal', v => {
            $('bgOpacityVal').textContent = v;
            updateStyle('opacity', v);
        });

        syncRange('textOpacityRange', 'textOpacityVal', v => {
            $('textOpacityVal').textContent = v;
            updateStyle('opacity', v);
        });

        syncRange('rotateRange', 'rotateVal', v => {
            $('rotate').value = v;
            $('rotateVal').textContent = v + '°';
            updateTransform();
        });

        if ($('rotate')) {
            $('rotate').addEventListener('input', () => {
                $('rotateRange').value = $('rotate').value;
                $('rotateVal').textContent = $('rotate').value + '°';
                updateTransform();
            });
        }

        syncRange('scaleRange', 'scaleVal', v => {
            $('scaleVal').textContent = v;
            updateTransform();
        });

        syncRange('borderRadiusAll', 'borderRadiusVal', v => {
            $('borderRadiusVal').textContent = v + 'px';
            ['borderRadiusTopLeft', 'borderRadiusTopRight', 'borderRadiusBottomLeft', 'borderRadiusBottomRight'].forEach(id => {
                if ($(id)) $(id).value = v;
            });
            updateStyle('borderTopLeftRadius', v, 'px');
            updateStyle('borderTopRightRadius', v, 'px');
            updateStyle('borderBottomLeftRadius', v, 'px');
            updateStyle('borderBottomRightRadius', v, 'px');
        });

        syncRange('animationDurationRange', 'animDurationVal', v => {
            $('animDurationVal').textContent = v + 's';
            currentStyles.animationDuration = v + 's';
            applyStyles();
        });

        // Filter ranges
        ['filterBlurRange', 'filterBrightnessRange', 'filterContrastRange', 'filterSaturateRange',
         'filterHueRotateRange', 'filterInvertRange', 'filterSepiaRange', 'filterGrayscaleRange', 'backdropBlurRange'].forEach(id => {
            const el = $(id);
            if (el) el.addEventListener('input', updateFilter);
        });

        // Complex inputs
        ['textShadowX', 'textShadowY', 'textShadowBlur'].forEach(id => {
            const el = $(id);
            if (el) el.addEventListener('input', () => {
                const color = pickers.textShadowColor ? pickers.textShadowColor.color.hexString : '#000000';
                updateComplexStyle('textShadowColor', color);
            });
        });

        ['boxShadowX', 'boxShadowY', 'boxShadowBlur', 'boxShadowSpread'].forEach(id => {
            const el = $(id);
            if (el) el.addEventListener('input', updateBoxShadow);
        });

        if ($('boxShadowInset')) $('boxShadowInset').addEventListener('change', updateBoxShadow);

        ['outlineWidth', 'outlineStyle'].forEach(id => {
            const el = $(id);
            if (el) el.addEventListener('input', () => {
                const color = pickers.outlineColor ? pickers.outlineColor.color.hexString : '#ffffff';
                updateComplexStyle('outlineColor', color);
            });
        });

        ['skewX', 'skewY', 'translateX', 'translateY'].forEach(id => {
            const el = $(id);
            if (el) el.addEventListener('input', updateTransform);
        });

        ['gradientAngle', 'gradientType'].forEach(id => {
            const el = $(id);
            if (el) {
                el.addEventListener('input', updateGradient);
                el.addEventListener('change', updateGradient);
            }
        });

        ['textGradientAngle', 'textGradientType'].forEach(id => {
            const el = $(id);
            if (el) {
                el.addEventListener('input', updateTextGradient);
                el.addEventListener('change', updateTextGradient);
            }
        });

        if ($('backgroundImageUrl')) $('backgroundImageUrl').addEventListener('input', updateBackgroundImageUrl);
        if ($('textImageFill')) $('textImageFill').addEventListener('input', updateTextImageFill);

        ['paddingLeft', 'paddingRight', 'paddingTop', 'paddingBottom', 'paddingUnit'].forEach(id => {
            const el = $(id);
            if (el) el.addEventListener('input', updatePadding);
        });

        if ($('transitionProperty')) $('transitionProperty').addEventListener('change', updateTransition);
        if ($('transitionDuration')) $('transitionDuration').addEventListener('input', updateTransition);

        // Preset animation
        if ($('presetAnimation')) {
            $('presetAnimation').addEventListener('change', () => {
                const name = $('presetAnimation').value;
                if (name) applyAnimation(name);
            });
        }

        // Preset clip-path
        if ($('presetClipPath')) {
            $('presetClipPath').addEventListener('change', () => {
                const val = $('presetClipPath').value;
                if (val !== '') {
                    updateStyle('clipPath', val);
                    if ($('clipPath')) $('clipPath').value = val;
                }
            });
        }

        // Custom keyframes
        if ($('applyKeyframesBtn')) {
            $('applyKeyframesBtn').addEventListener('click', () => {
                const kf = $('animationKeyframes').value.trim();
                if (kf) {
                    const style = document.createElement('style');
                    style.textContent = kf;
                    document.head.appendChild(style);
                    // Extract name
                    const match = kf.match(/@keyframes\s+([a-zA-Z0-9_-]+)/);
                    if (match) {
                        applyAnimation(match[1]);
                        showToast(`Keyframes uygulandı: ${match[1]}`);
                    }
                }
            });
        }

        // Custom text input
        if (customTextInput) {
            customTextInput.addEventListener('input', () => {
                previewBox.textContent = customTextInput.value || 'K3N4N V6.0';
                $('charCount').textContent = `${customTextInput.value.length}/100`;
                updateHtmlPreview();
            });
        }

        // Custom CSS apply
        if ($('applyCustomCss')) {
            $('applyCustomCss').addEventListener('click', () => {
                try {
                    const css = cssInputArea.value.trim();
                    if (!css) return;
                    const style = document.createElement('style');
                    style.textContent = `#preview-box { ${css} }`;
                    document.head.appendChild(style);
                    $('css-success').classList.add('visible');
                    $('css-error').classList.remove('visible');
                    setTimeout(() => $('css-success').classList.remove('visible'), 2500);
                    showToast('Özel CSS uygulandı');
                } catch(e) {
                    $('css-error').classList.add('visible');
                    $('css-success').classList.remove('visible');
                    setTimeout(() => $('css-error').classList.remove('visible'), 2500);
                }
            });
        }

        // Copy CSS
        if ($('copy-css-btn')) {
            $('copy-css-btn').addEventListener('click', () => {
                navigator.clipboard.writeText(cssOutput.value).then(() => {
                    $('copy-success').classList.add('visible');
                    $('copy-error').classList.remove('visible');
                    setTimeout(() => $('copy-success').classList.remove('visible'), 2500);
                    showToast('CSS kopyalandı!');
                }).catch(() => {
                    $('copy-error').classList.add('visible');
                    setTimeout(() => $('copy-error').classList.remove('visible'), 2500);
                    showToast('Kopyalama başarısız', 'error');
                });
            });
        }

        // Import styles
        if ($('import-styles')) {
            $('import-styles').addEventListener('change', e => {
                const file = e.target.files[0];
                if (!file) return;
                const reader = new FileReader();
                reader.onload = event => {
                    try {
                        const imported = JSON.parse(event.target.result);
                        currentStyles = { ...getDefaultStyles(), ...imported };
                        applyStyles();
                        saveToHistory();
                        showToast('Stiller içe aktarıldı');
                    } catch(err) {
                        showToast('Geçersiz dosya!', 'error');
                    }
                };
                reader.readAsText(file);
                e.target.value = '';
            });
        }

        // ===== PANELS (Accordion) =====
        $$('.panel-header').forEach(header => {
            header.addEventListener('click', () => {
                const panel = header.closest('.panel');
                panel.classList.toggle('expanded');
            });
        });

        // ===== TABS =====
        $$('.output-tab').forEach(tab => {
            tab.addEventListener('click', () => {
                $$('.output-tab').forEach(t => t.classList.remove('active'));
                $$('.tab-content').forEach(c => c.classList.remove('active'));
                tab.classList.add('active');
                const target = $(tab.dataset.tab);
                if (target) target.classList.add('active');
            });
        });

        // ===== SIDEBAR TOGGLE (Mobile) =====
        if ($('sidebarToggle')) {
            $('sidebarToggle').addEventListener('click', () => {
                $('sidebar').classList.toggle('open');
                $('sidebarOverlay').classList.toggle('visible');
            });
        }

        if ($('sidebarOverlay')) {
            $('sidebarOverlay').addEventListener('click', () => {
                $('sidebar').classList.remove('open');
                $('sidebarOverlay').classList.remove('visible');
            });
        }

        // ===== PANEL SEARCH =====
        if ($('panelSearch')) {
            $('panelSearch').addEventListener('input', e => {
                const q = e.target.value.toLowerCase().trim();
                $$('.panel').forEach(panel => {
                    const title = panel.querySelector('.panel-title');
                    const text = (title ? title.textContent : '').toLowerCase();
                    const panelName = (panel.dataset.panel || '').toLowerCase();
                    if (!q || text.includes(q) || panelName.includes(q)) {
                        panel.style.display = '';
                    } else {
                        panel.style.display = 'none';
                    }
                });
            });
        }

        // ===== Font size input sync =====
        if ($('fontSize')) {
            $('fontSize').addEventListener('input', () => {
                const v = $('fontSize').value;
                $('fontSizeRange').value = v;
                $('fontSizeVal').textContent = v + 'px';
                updateStyle('fontSize', v, 'px');
            });
        }

        // ===== INITIALIZATION =====
        initGradientPickers('gradientColors', gradientColors, 'bg');
        initGradientPickers('textGradientColors', textGradientColors, 'text');
        applyStyles();
        saveToHistory();
        generatePalette();

        // Set initial badge values
        $('fontSizeVal').textContent = '30px';
        $('fontWeightVal').textContent = '400';
        $('lineHeightVal').textContent = '1.5';
        $('bgOpacityVal').textContent = '1';
        $('textOpacityVal').textContent = '1';
        $('rotateVal').textContent = '0°';
        $('scaleVal').textContent = '1';
        $('borderRadiusVal').textContent = '10px';
        $('animDurationVal').textContent = '1s';
        $('blurVal').textContent = '0px';
        $('brightnessVal').textContent = '100%';
        $('contrastVal').textContent = '100%';
        $('saturateVal').textContent = '100%';
        $('hueRotateVal').textContent = '0°';
        $('invertVal').textContent = '0%';
        $('sepiaVal').textContent = '0%';
        $('grayscaleVal').textContent = '0%';

        // Window resize observer for preview
        const resizeObserver = new ResizeObserver(() => updatePreviewDimensions());
        resizeObserver.observe(previewBox);

        console.log('K3N4N CSS Generator V6.0 initialized successfully! 🎨');

    })();
    </script>
</body>
</html>   tenayı uyumlu ve kodlamaay uygun olarak modern edıtor olarak kullancagım sekılde  tama yapılandır  sadece css  kodunu yazabılırsın yada tam  kodu yaz  nasıl ıstersen

### Claude Opus 4.6
*2026-02-07 18:34:58 +03*



# K3N4N CSS Stil Generator V6.0 — Tam Yeniden Yapılandırma

Kodunu baştan sona inceledim. HTML yapısı ile CSS arasında ciddi uyumsuzluklar var (class isimleri, yapısal hiyerarşi, eksik stiller). Aşağıda **tüm kodu tamamen uyumlu, modern editör kalitesinde** yeniden yazıyorum.

```html
<!DOCTYPE html>
<html lang="tr" data-theme="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>K3N4N CSS Stil Generator V6.0 (Ultimate Pro Edition)</title>
    <link href="https://fonts.googleapis.com/css2?family=VT323&family=Press+Start+2P&family=Orbitron:wght@400;700&family=Roboto+Mono:wght@400;700&family=Lobster&family=Kaushan+Script&family=Poppins:wght@300;400;500;600;700&family=Fira+Code:wght@400;700&family=Inter:wght@400;500;600;700&family=Space+Grotesk:wght@400;500;700&family=JetBrains+Mono:wght@400;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/chroma-js/2.4.2/chroma.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/@jaames/iro@5/dist/iro.min.js"></script>
    <style>
/* ============================================================
   K3N4N CSS GENERATOR V6.0 — COMPLETE STYLESHEET
   Tüm HTML yapısıyla %100 uyumlu, modern editör teması
   ============================================================ */

/* ===== RESET & BASE ===== */
*, *::before, *::after {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

:root {
    /* — Surface & Background — */
    --bg-dark: #0a0e1a;
    --bg-surface: #0f1629;
    --bg-card: #161d30;
    --bg-elevated: #1e2844;
    --bg-input: #0c1222;
    --bg-hover: rgba(255, 255, 255, 0.03);
    --bg-active: rgba(255, 255, 255, 0.05);

    /* — Text — */
    --text-white: #f0f4f8;
    --text-primary: #e2e8f0;
    --text-secondary: #94a3b8;
    --text-muted: #64748b;
    --text-dim: #475569;

    /* — Accent Colors — */
    --accent-primary: #22d3ee;
    --accent-primary-dim: rgba(34, 211, 238, 0.1);
    --accent-primary-mid: rgba(34, 211, 238, 0.25);
    --accent-primary-strong: rgba(34, 211, 238, 0.4);
    --accent-secondary: #a78bfa;
    --accent-secondary-dim: rgba(167, 139, 250, 0.1);
    --accent-tertiary: #f472b6;
    --accent-tertiary-dim: rgba(244, 114, 182, 0.1);
    --accent-amber: #fbbf24;
    --accent-amber-dim: rgba(251, 191, 36, 0.1);
    --accent-green: #34d399;
    --accent-green-dim: rgba(52, 211, 153, 0.1);
    --accent-red: #f87171;
    --accent-red-dim: rgba(248, 113, 113, 0.1);
    --accent-blue: #60a5fa;
    --accent-blue-dim: rgba(96, 165, 250, 0.1);
    --accent-orange: #fb923c;
    --accent-orange-dim: rgba(251, 146, 60, 0.1);

    /* — Borders — */
    --border-color: rgba(148, 163, 184, 0.08);
    --border-light: rgba(148, 163, 184, 0.15);
    --border-focus: rgba(34, 211, 238, 0.5);

    /* — Shadows — */
    --shadow-xs: 0 1px 2px rgba(0, 0, 0, 0.2);
    --shadow-sm: 0 2px 6px rgba(0, 0, 0, 0.3);
    --shadow-md: 0 4px 16px rgba(0, 0, 0, 0.35);
    --shadow-lg: 0 8px 32px rgba(0, 0, 0, 0.45);
    --shadow-xl: 0 16px 48px rgba(0, 0, 0, 0.5);
    --shadow-glow: 0 0 20px rgba(34, 211, 238, 0.12);
    --shadow-glow-strong: 0 0 30px rgba(34, 211, 238, 0.2);

    /* — Radii — */
    --radius-xs: 4px;
    --radius-sm: 6px;
    --radius-md: 10px;
    --radius-lg: 14px;
    --radius-xl: 20px;
    --radius-full: 9999px;

    /* — Animation — */
    --speed-instant: 0.08s;
    --speed-fast: 0.15s;
    --speed-normal: 0.25s;
    --speed-slow: 0.4s;
    --ease-out: cubic-bezier(0.16, 1, 0.3, 1);
    --ease-in-out: cubic-bezier(0.4, 0, 0.2, 1);
    --ease-bounce: cubic-bezier(0.34, 1.56, 0.64, 1);

    /* — Layout — */
    --header-h: 52px;
    --sidebar-w: 360px;

    /* — Z-Index — */
    --z-base: 1;
    --z-sticky: 100;
    --z-overlay: 800;
    --z-sidebar: 900;
    --z-header: 1000;
    --z-toast: 9999;
}

/* Light theme override */
[data-theme="light"] {
    --bg-dark: #f1f5f9;
    --bg-surface: #ffffff;
    --bg-card: #f8fafc;
    --bg-elevated: #e2e8f0;
    --bg-input: #ffffff;
    --bg-hover: rgba(0, 0, 0, 0.03);
    --bg-active: rgba(0, 0, 0, 0.06);
    --text-white: #0f172a;
    --text-primary: #1e293b;
    --text-secondary: #475569;
    --text-muted: #64748b;
    --text-dim: #94a3b8;
    --accent-primary: #0891b2;
    --accent-primary-dim: rgba(8, 145, 178, 0.08);
    --accent-primary-mid: rgba(8, 145, 178, 0.18);
    --border-color: rgba(0, 0, 0, 0.06);
    --border-light: rgba(0, 0, 0, 0.1);
    --shadow-xs: 0 1px 2px rgba(0, 0, 0, 0.05);
    --shadow-sm: 0 1px 3px rgba(0, 0, 0, 0.08);
    --shadow-md: 0 4px 12px rgba(0, 0, 0, 0.08);
    --shadow-lg: 0 8px 24px rgba(0, 0, 0, 0.1);
}

html {
    scroll-behavior: smooth;
    font-size: 16px;
    height: 100%;
}

body {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    background: var(--bg-dark);
    color: var(--text-primary);
    line-height: 1.55;
    min-height: 100vh;
    overflow-x: hidden;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
}

/* ===== SCROLLBAR ===== */
::-webkit-scrollbar { width: 5px; height: 5px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb { background: var(--text-dim); border-radius: 10px; }
::-webkit-scrollbar-thumb:hover { background: var(--text-muted); }


/* ================================================================
   HEADER / TOP BAR  — .app-header
   ================================================================ */
.app-header {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    height: var(--header-h);
    background: rgba(15, 22, 41, 0.88);
    backdrop-filter: blur(20px) saturate(1.6);
    -webkit-backdrop-filter: blur(20px) saturate(1.6);
    border-bottom: 1px solid var(--border-color);
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0 16px;
    z-index: var(--z-header);
    gap: 12px;
}

[data-theme="light"] .app-header {
    background: rgba(255, 255, 255, 0.9);
}

/* — Logo — */
.app-header .logo {
    display: flex;
    align-items: center;
    gap: 10px;
    text-decoration: none;
    font-weight: 700;
    font-size: 15px;
    color: var(--accent-primary);
    flex-shrink: 0;
    letter-spacing: -0.3px;
}

.app-header .logo i {
    font-size: 18px;
    filter: drop-shadow(0 0 8px rgba(34, 211, 238, 0.35));
}

.app-header .logo span {
    background: linear-gradient(135deg, var(--accent-primary), var(--accent-secondary));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

/* — Header Actions — */
.header-actions {
    display: flex;
    align-items: center;
    gap: 6px;
    flex-wrap: wrap;
}

.header-btn {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    gap: 6px;
    height: 34px;
    padding: 0 12px;
    background: var(--bg-card);
    border: 1px solid var(--border-color);
    border-radius: var(--radius-sm);
    color: var(--text-secondary);
    font-size: 12px;
    font-weight: 500;
    font-family: inherit;
    cursor: pointer;
    transition: all var(--speed-normal) var(--ease-out);
    white-space: nowrap;
}

.header-btn:hover:not(:disabled) {
    background: var(--bg-elevated);
    color: var(--text-white);
    border-color: var(--border-light);
    transform: translateY(-1px);
    box-shadow: var(--shadow-sm);
}

.header-btn:active:not(:disabled) {
    transform: translateY(0);
}

.header-btn:disabled {
    opacity: 0.35;
    cursor: not-allowed;
}

.header-btn i { font-size: 12px; }

.header-btn.theme-btn {
    width: 34px;
    padding: 0;
}

.header-btn.reset-btn {
    background: var(--accent-red-dim);
    color: var(--accent-red);
    border-color: rgba(248, 113, 113, 0.15);
}

.header-btn.reset-btn:hover {
    background: rgba(248, 113, 113, 0.18);
    border-color: var(--accent-red);
    color: var(--accent-red);
}

/* — Tooltip — */
.header-btn[data-tooltip] {
    position: relative;
}

.header-btn[data-tooltip]::after {
    content: attr(data-tooltip);
    position: absolute;
    bottom: -30px;
    left: 50%;
    transform: translateX(-50%) scale(0.92);
    background: var(--bg-dark);
    color: var(--text-primary);
    padding: 3px 10px;
    border-radius: var(--radius-xs);
    font-size: 10.5px;
    font-weight: 500;
    white-space: nowrap;
    opacity: 0;
    pointer-events: none;
    transition: all var(--speed-fast);
    border: 1px solid var(--border-color);
    z-index: 10;
}

.header-btn[data-tooltip]:hover::after {
    opacity: 1;
    transform: translateX(-50%) scale(1);
}


/* ================================================================
   SIDEBAR TOGGLE (Mobile)
   ================================================================ */
.sidebar-toggle {
    display: none;
    position: fixed;
    bottom: 20px;
    right: 20px;
    width: 48px;
    height: 48px;
    border-radius: 50%;
    background: linear-gradient(135deg, var(--accent-primary), #06b6d4);
    color: var(--bg-dark);
    border: none;
    font-size: 18px;
    cursor: pointer;
    z-index: calc(var(--z-sidebar) + 5);
    box-shadow: var(--shadow-lg), 0 0 20px rgba(34, 211, 238, 0.3);
    transition: all var(--speed-normal) var(--ease-out);
    align-items: center;
    justify-content: center;
}

.sidebar-toggle:hover {
    transform: scale(1.1);
    box-shadow: var(--shadow-xl), 0 0 30px rgba(34, 211, 238, 0.4);
}

.sidebar-overlay {
    display: none;
    position: fixed;
    inset: 0;
    background: rgba(0, 0, 0, 0.6);
    backdrop-filter: blur(4px);
    z-index: var(--z-overlay);
    opacity: 0;
    transition: opacity var(--speed-normal) var(--ease-out);
}

.sidebar-overlay.visible {
    display: block;
    opacity: 1;
}


/* ================================================================
   APP CONTAINER (Sidebar + Main)
   ================================================================ */
.app-container {
    display: flex;
    min-height: 100vh;
    padding-top: var(--header-h);
}


/* ================================================================
   SIDEBAR
   ================================================================ */
.sidebar {
    position: fixed;
    top: var(--header-h);
    left: 0;
    bottom: 0;
    width: var(--sidebar-w);
    background: var(--bg-surface);
    border-right: 1px solid var(--border-color);
    overflow-y: auto;
    overflow-x: hidden;
    z-index: var(--z-sidebar);
    padding: 12px;
    padding-bottom: 80px;
    transition: transform var(--speed-slow) var(--ease-out);
}

/* — Search — */
.sidebar-search {
    position: relative;
    margin-bottom: 12px;
}

.sidebar-search i {
    position: absolute;
    left: 12px;
    top: 50%;
    transform: translateY(-50%);
    color: var(--text-dim);
    font-size: 13px;
    pointer-events: none;
}

.sidebar-search input {
    width: 100%;
    padding: 10px 12px 10px 36px;
    background: var(--bg-input);
    border: 1px solid var(--border-color);
    border-radius: var(--radius-md);
    color: var(--text-white);
    font-size: 12.5px;
    font-family: inherit;
    outline: none;
    transition: all var(--speed-normal) var(--ease-out);
}

.sidebar-search input::placeholder {
    color: var(--text-dim);
}

.sidebar-search input:focus {
    border-color: var(--accent-primary);
    box-shadow: 0 0 0 3px var(--accent-primary-dim);
    background: var(--bg-card);
}


/* ================================================================
   PANELS (Accordion)
   ================================================================ */
.panel {
    background: var(--bg-card);
    border: 1px solid var(--border-color);
    border-radius: var(--radius-md);
    margin-bottom: 6px;
    transition: all var(--speed-normal) var(--ease-out);
    overflow: visible;
}

.panel:hover {
    border-color: var(--border-light);
}

.panel.expanded {
    border-color: var(--border-light);
    box-shadow: var(--shadow-sm), 0 0 0 1px rgba(34, 211, 238, 0.04);
}

/* — Panel Header — */
.panel-header {
    display: flex;
    align-items: center;
    gap: 10px;
    padding: 10px 12px;
    cursor: pointer;
    user-select: none;
    border-radius: var(--radius-md);
    transition: background var(--speed-fast) var(--ease-in-out);
    -webkit-tap-highlight-color: transparent;
}

.panel-header:hover {
    background: var(--bg-hover);
}

.panel-header:active {
    background: var(--bg-active);
}

.panel.expanded > .panel-header {
    border-bottom: 1px solid var(--border-color);
    border-radius: var(--radius-md) var(--radius-md) 0 0;
}

/* — Panel Icon — */
.panel-icon {
    width: 32px;
    height: 32px;
    border-radius: var(--radius-sm);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 13px;
    flex-shrink: 0;
}

.panel-icon.text        { background: var(--accent-primary-dim);    color: var(--accent-primary); }
.panel-icon.bg          { background: var(--accent-tertiary-dim);   color: var(--accent-tertiary); }
.panel-icon.border      { background: var(--accent-amber-dim);      color: var(--accent-amber); }
.panel-icon.transform   { background: var(--accent-orange-dim);     color: var(--accent-orange); }
.panel-icon.shadow      { background: var(--accent-secondary-dim);  color: var(--accent-secondary); }
.panel-icon.anim        { background: var(--accent-red-dim);        color: var(--accent-red); }
.panel-icon.clip        { background: var(--accent-amber-dim);      color: var(--accent-amber); }
.panel-icon.transparent { background: var(--accent-secondary-dim);  color: var(--accent-secondary); }
.panel-icon.palette     { background: var(--accent-tertiary-dim);   color: var(--accent-tertiary); }
.panel-icon.effects     { background: var(--accent-blue-dim);       color: var(--accent-blue); }
.panel-icon.layout      { background: var(--accent-green-dim);      color: var(--accent-green); }
.panel-icon.presets     { background: var(--accent-amber-dim);      color: var(--accent-amber); }
.panel-icon.chaos       { background: var(--accent-red-dim);        color: var(--accent-red); }

/* — Panel Title — */
.panel-title {
    flex: 1;
    font-weight: 600;
    font-size: 12.5px;
    color: var(--text-white);
    line-height: 1.35;
    min-width: 0;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
}

/* — Panel Toggle Arrow — */
.panel-toggle {
    font-size: 11px;
    color: var(--text-dim);
    transition: transform var(--speed-slow) var(--ease-out);
    flex-shrink: 0;
    transform: rotate(180deg);
}

.panel.expanded > .panel-header .panel-toggle {
    transform: rotate(0deg);
}

/* — Panel Body — */
.panel-body {
    display: none;
    padding: 12px;
    animation: panelSlideDown var(--speed-slow) var(--ease-out);
}

.panel.expanded > .panel-body {
    display: block;
}

@keyframes panelSlideDown {
    from { opacity: 0; transform: translateY(-6px); }
    to   { opacity: 1; transform: translateY(0); }
}


/* ================================================================
   BUTTON GRID (style-btn / action buttons in panels)
   ================================================================ */
.btn-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(105px, 1fr));
    gap: 5px;
    margin-bottom: 4px;
}

.style-btn {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    gap: 5px;
    padding: 7px 6px;
    font-size: 10.5px;
    font-weight: 600;
    font-family: inherit;
    background: var(--bg-elevated);
    border: 1px solid var(--border-color);
    border-radius: var(--radius-sm);
    color: var(--text-secondary);
    cursor: pointer;
    transition: all var(--speed-normal) var(--ease-out);
    white-space: nowrap;
    line-height: 1;
    text-align: center;
}

.style-btn i {
    font-size: 10px;
}

.style-btn:hover {
    background: var(--accent-primary-dim);
    color: var(--accent-primary);
    border-color: rgba(34, 211, 238, 0.2);
    transform: translateY(-1px);
    box-shadow: var(--shadow-xs);
}

.style-btn:active {
    transform: translateY(0);
}

.style-btn.chaos-btn {
    background: linear-gradient(135deg, rgba(248, 113, 113, 0.1), rgba(167, 139, 250, 0.1));
    color: var(--accent-red);
    border-color: rgba(248, 113, 113, 0.15);
}

.style-btn.chaos-btn:hover {
    background: linear-gradient(135deg, rgba(248, 113, 113, 0.2), rgba(167, 139, 250, 0.2));
    border-color: var(--accent-red);
    box-shadow: 0 0 12px rgba(248, 113, 113, 0.15);
}


/* ================================================================
   SEPARATOR
   ================================================================ */
.separator {
    height: 1px;
    background: var(--border-color);
    margin: 10px 0;
}


/* ================================================================
   FORM GROUPS & CONTROLS
   ================================================================ */
.form-group {
    margin-bottom: 12px;
}

.form-group:last-child {
    margin-bottom: 0;
}

.form-group > label {
    display: flex;
    align-items: center;
    justify-content: space-between;
    font-size: 11.5px;
    color: var(--text-muted);
    margin-bottom: 5px;
    font-weight: 500;
    gap: 6px;
}

/* — Value Badge — */
.value-badge {
    background: var(--accent-primary-dim);
    color: var(--accent-primary);
    padding: 1px 7px;
    border-radius: var(--radius-full);
    font-size: 10px;
    font-weight: 700;
    font-family: 'JetBrains Mono', monospace;
    flex-shrink: 0;
}

/* — Text Input — */
.form-group input[type="text"],
.form-group input[type="number"] {
    width: 100%;
    padding: 8px 10px;
    background: var(--bg-input);
    border: 1px solid var(--border-color);
    border-radius: var(--radius-sm);
    color: var(--text-white);
    font-size: 12.5px;
    font-family: inherit;
    outline: none;
    transition: all var(--speed-normal) var(--ease-out);
}

.form-group input[type="text"]:hover,
.form-group input[type="number"]:hover {
    border-color: var(--border-light);
}

.form-group input[type="text"]:focus,
.form-group input[type="number"]:focus {
    border-color: var(--accent-primary);
    box-shadow: 0 0 0 3px var(--accent-primary-dim);
    background: var(--bg-card);
}

.form-group input[type="text"]::placeholder {
    color: var(--text-dim);
}

/* — Select — */
.form-group select {
    width: 100%;
    padding: 8px 30px 8px 10px;
    background: var(--bg-input);
    border: 1px solid var(--border-color);
    border-radius: var(--radius-sm);
    color: var(--text-white);
    font-size: 12.5px;
    font-family: inherit;
    outline: none;
    cursor: pointer;
    appearance: none;
    -webkit-appearance: none;
    background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='12' height='12' viewBox='0 0 24 24' fill='none' stroke='%2364748b' stroke-width='2.5' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpolyline points='6 9 12 15 18 9'/%3E%3C/svg%3E");
    background-repeat: no-repeat;
    background-position: right 8px center;
    transition: all var(--speed-normal) var(--ease-out);
}

.form-group select:hover {
    border-color: var(--border-light);
}

.form-group select:focus {
    border-color: var(--accent-primary);
    box-shadow: 0 0 0 3px var(--accent-primary-dim);
}

.form-group select option {
    background: var(--bg-card);
    color: var(--text-white);
}

/* — Textarea — */
.form-group textarea {
    width: 100%;
    padding: 10px;
    background: var(--bg-input);
    border: 1px solid var(--border-color);
    border-radius: var(--radius-sm);
    color: var(--accent-primary);
    font-size: 11.5px;
    font-family: 'JetBrains Mono', 'Fira Code', monospace;
    outline: none;
    resize: vertical;
    min-height: 70px;
    line-height: 1.6;
    transition: all var(--speed-normal) var(--ease-out);
}

.form-group textarea:focus {
    border-color: var(--accent-primary);
    box-shadow: 0 0 0 3px var(--accent-primary-dim);
}

/* — Range Slider — */
.form-group input[type="range"] {
    width: 100%;
    -webkit-appearance: none;
    appearance: none;
    height: 4px;
    background: var(--bg-elevated);
    border-radius: 2px;
    outline: none;
    cursor: pointer;
    margin: 6px 0;
}

.form-group input[type="range"]::-webkit-slider-thumb {
    -webkit-appearance: none;
    width: 16px;
    height: 16px;
    border-radius: 50%;
    background: var(--accent-primary);
    cursor: pointer;
    border: 2px solid var(--bg-dark);
    box-shadow: 0 0 8px rgba(34, 211, 238, 0.35);
    transition: all var(--speed-fast);
}

.form-group input[type="range"]::-webkit-slider-thumb:hover {
    transform: scale(1.2);
    box-shadow: 0 0 14px rgba(34, 211, 238, 0.5);
}

.form-group input[type="range"]::-moz-range-thumb {
    width: 16px;
    height: 16px;
    border-radius: 50%;
    background: var(--accent-primary);
    cursor: pointer;
    border: 2px solid var(--bg-dark);
}

/* — Form Row (inline fields) — */
.form-row {
    display: flex;
    gap: 8px;
    align-items: center;
    flex-wrap: wrap;
    margin-bottom: 6px;
}

.form-row:last-child {
    margin-bottom: 0;
}

.form-row > label {
    font-size: 10px;
    color: var(--text-dim);
    min-width: 14px;
    flex-shrink: 0;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.3px;
}

.form-row > input[type="text"],
.form-row > input[type="number"] {
    flex: 1;
    min-width: 0;
    padding: 7px 8px;
    background: var(--bg-input);
    border: 1px solid var(--border-color);
    border-radius: var(--radius-sm);
    color: var(--text-white);
    font-size: 12px;
    font-family: inherit;
    outline: none;
    transition: all var(--speed-normal) var(--ease-out);
}

.form-row > input:focus {
    border-color: var(--accent-primary);
    box-shadow: 0 0 0 2px var(--accent-primary-dim);
}

.form-row > select {
    flex: 1;
    min-width: 0;
    padding: 7px 26px 7px 8px;
    background: var(--bg-input);
    border: 1px solid var(--border-color);
    border-radius: var(--radius-sm);
    color: var(--text-white);
    font-size: 12px;
    font-family: inherit;
    outline: none;
    cursor: pointer;
    appearance: none;
    -webkit-appearance: none;
    background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='10' height='10' viewBox='0 0 24 24' fill='none' stroke='%2364748b' stroke-width='2.5'%3E%3Cpolyline points='6 9 12 15 18 9'/%3E%3C/svg%3E");
    background-repeat: no-repeat;
    background-position: right 6px center;
    transition: all var(--speed-normal) var(--ease-out);
}

.form-row > select:focus {
    border-color: var(--accent-primary);
    box-shadow: 0 0 0 2px var(--accent-primary-dim);
}

.form-row > select option {
    background: var(--bg-card);
    color: var(--text-white);
}

/* Number input spin buttons */
input[type="number"]::-webkit-inner-spin-button,
input[type="number"]::-webkit-outer-spin-button {
    opacity: 0.3;
}

/* — Checkbox Row — */
.checkbox-row {
    display: flex;
    flex-wrap: wrap;
    gap: 4px 14px;
    margin-bottom: 6px;
}

.checkbox-row label {
    display: flex;
    align-items: center;
    gap: 5px;
    font-size: 11px;
    color: var(--text-secondary);
    cursor: pointer;
    white-space: nowrap;
    transition: color var(--speed-fast);
}

.checkbox-row label:hover {
    color: var(--text-white);
}

.checkbox-row input[type="checkbox"] {
    accent-color: var(--accent-primary);
    width: 13px;
    height: 13px;
    cursor: pointer;
    border-radius: 3px;
}

/* — Color Picker Container — */
.color-picker-container {
    margin-top: 6px;
    padding: 8px;
    background: var(--bg-input);
    border: 1px solid var(--border-color);
    border-radius: var(--radius-md);
    display: flex;
    justify-content: center;
}

/* — Gradient Colors — */
.gradient-colors {
    display: flex;
    flex-direction: column;
    gap: 6px;
    margin-top: 8px;
}

.gradient-color-row {
    display: flex;
    align-items: center;
    gap: 8px;
    background: var(--bg-input);
    padding: 6px 8px;
    border-radius: var(--radius-sm);
    border: 1px solid var(--border-color);
}

.gradient-color-row input[type="number"] {
    width: 50px;
    padding: 5px 6px;
    background: var(--bg-dark);
    border: 1px solid var(--border-color);
    border-radius: var(--radius-xs);
    color: var(--text-white);
    font-size: 11px;
    text-align: center;
    outline: none;
    font-family: 'JetBrains Mono', monospace;
}

.gradient-color-row input[type="number"]:focus {
    border-color: var(--accent-primary);
}

.gradient-color-row button {
    width: 26px;
    height: 26px;
    display: flex;
    align-items: center;
    justify-content: center;
    background: var(--accent-red-dim);
    color: var(--accent-red);
    border: 1px solid rgba(248, 113, 113, 0.15);
    border-radius: var(--radius-xs);
    cursor: pointer;
    font-size: 10px;
    transition: all var(--speed-fast);
    flex-shrink: 0;
    margin-left: auto;
}

.gradient-color-row button:hover {
    background: rgba(248, 113, 113, 0.2);
    border-color: var(--accent-red);
}

.add-color-btn {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    gap: 5px;
    padding: 7px 14px;
    background: var(--accent-primary-dim);
    color: var(--accent-primary);
    border: 1px dashed rgba(34, 211, 238, 0.35);
    border-radius: var(--radius-sm);
    cursor: pointer;
    font-size: 11px;
    font-weight: 600;
    font-family: inherit;
    transition: all var(--speed-normal) var(--ease-out);
    margin-top: 6px;
}

.add-color-btn:hover {
    background: var(--accent-primary-mid);
    border-style: solid;
    border-color: var(--accent-primary);
}


/* ================================================================
   PRESET CARDS (Theme Presets)
   ================================================================ */
.preset-cards {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 6px;
}

.preset-card {
    padding: 10px 8px;
    border-radius: var(--radius-sm);
    border: 1px solid var(--border-color);
    background: var(--bg-elevated);
    color: var(--text-secondary);
    cursor: pointer;
    text-align: center;
    font-size: 11px;
    font-weight: 600;
    font-family: inherit;
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 6px;
    transition: all var(--speed-normal) var(--ease-out);
}

.preset-card i {
    font-size: 12px;
}

.preset-card:hover {
    background: var(--accent-primary-dim);
    color: var(--accent-primary);
    border-color: rgba(34, 211, 238, 0.2);
    transform: translateY(-2px);
    box-shadow: var(--shadow-md);
}

.preset-card:active {
    transform: translateY(0);
}


/* ================================================================
   PALETTE PREVIEW
   ================================================================ */
.palette-preview {
    display: flex;
    gap: 5px;
    flex-wrap: wrap;
    margin-top: 8px;
}

.palette-color {
    width: 40px;
    height: 40px;
    border-radius: var(--radius-sm);
    cursor: pointer;
    position: relative;
    transition: all var(--speed-normal) var(--ease-out);
    border: 2px solid transparent;
    box-shadow: var(--shadow-xs);
}

.palette-color:hover {
    transform: scale(1.18);
    border-color: var(--text-white);
    z-index: 1;
    box-shadow: var(--shadow-md);
}

.palette-color .tooltip {
    position: absolute;
    bottom: -26px;
    left: 50%;
    transform: translateX(-50%);
    background: var(--bg-dark);
    color: var(--text-white);
    padding: 2px 8px;
    border-radius: var(--radius-xs);
    font-size: 9.5px;
    font-family: 'JetBrains Mono', monospace;
    white-space: nowrap;
    opacity: 0;
    pointer-events: none;
    transition: opacity var(--speed-fast);
    border: 1px solid var(--border-color);
}

.palette-color:hover .tooltip {
    opacity: 1;
}


/* ================================================================
   MAIN CONTENT
   ================================================================ */
.main-content {
    margin-left: var(--sidebar-w);
    flex: 1;
    padding: 20px;
    display: flex;
    flex-direction: column;
    gap: 20px;
    min-width: 0;
}


/* ================================================================
   PREVIEW SECTION
   ================================================================ */
.preview-wrapper {
    background: var(--bg-surface);
    border: 1px solid var(--border-color);
    border-radius: var(--radius-lg);
    padding: 20px;
    display: flex;
    flex-direction: column;
    gap: 14px;
}

.preview-label {
    display: flex;
    align-items: center;
    justify-content: space-between;
}

.preview-label h3 {
    font-size: 13.5px;
    font-weight: 600;
    color: var(--text-white);
    display: flex;
    align-items: center;
    gap: 8px;
}

.preview-label h3 i {
    color: var(--accent-primary);
    font-size: 14px;
}

.preview-dimensions {
    font-size: 11px;
    color: var(--text-dim);
    background: var(--bg-card);
    padding: 3px 10px;
    border-radius: var(--radius-full);
    font-family: 'JetBrains Mono', monospace;
    border: 1px solid var(--border-color);
}

/* — Preview Box — */
#preview-box {
    background: var(--bg-card);
    border-radius: var(--radius-md);
    min-height: 280px;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 30px;
    position: relative;
    overflow: hidden;
    border: 1px solid var(--border-color);
    font-family: 'Poppins', sans-serif;
    font-size: 30px;
    color: var(--accent-primary);
    word-break: break-word;
    text-align: center;
}

#preview-box::before {
    content: '';
    position: absolute;
    inset: 0;
    background-image:
        linear-gradient(45deg, rgba(255,255,255,0.012) 25%, transparent 25%),
        linear-gradient(-45deg, rgba(255,255,255,0.012) 25%, transparent 25%),
        linear-gradient(45deg, transparent 75%, rgba(255,255,255,0.012) 75%),
        linear-gradient(-45deg, transparent 75%, rgba(255,255,255,0.012) 75%);
    background-size: 20px 20px;
    background-position: 0 0, 0 10px, 10px -10px, -10px 0;
    pointer-events: none;
    z-index: 0;
}

/* — Text Input — */
.preview-text-input {
    display: flex;
    gap: 10px;
    align-items: center;
}

.preview-text-input input {
    flex: 1;
    padding: 10px 14px;
    background: var(--bg-input);
    border: 1px solid var(--border-color);
    border-radius: var(--radius-sm);
    color: var(--text-white);
    font-size: 13px;
    font-family: inherit;
    outline: none;
    transition: all var(--speed-normal) var(--ease-out);
}

.preview-text-input input::placeholder {
    color: var(--text-dim);
}

.preview-text-input input:focus {
    border-color: var(--accent-primary);
    box-shadow: 0 0 0 3px var(--accent-primary-dim);
}

.char-count {
    font-size: 11px;
    color: var(--text-dim);
    flex-shrink: 0;
    font-family: 'JetBrains Mono', monospace;
}


/* ================================================================
   OUTPUT SECTION
   ================================================================ */
.output-card {
    background: var(--bg-surface);
    border: 1px solid var(--border-color);
    border-radius: var(--radius-lg);
    overflow: hidden;
    flex: 1;
    display: flex;
    flex-direction: column;
}

/* — Tabs — */
.output-tabs {
    display: flex;
    border-bottom: 1px solid var(--border-color);
    background: rgba(0, 0, 0, 0.12);
    overflow-x: auto;
}

.output-tab {
    padding: 11px 18px;
    font-size: 12px;
    font-weight: 600;
    color: var(--text-dim);
    cursor: pointer;
    border: none;
    background: none;
    transition: all var(--speed-normal) var(--ease-out);
    position: relative;
    font-family: inherit;
    white-space: nowrap;
    flex-shrink: 0;
}

.output-tab:hover {
    color: var(--text-secondary);
    background: var(--bg-hover);
}

.output-tab.active {
    color: var(--accent-primary);
}

.output-tab.active::after {
    content: '';
    position: absolute;
    bottom: 0;
    left: 10px;
    right: 10px;
    height: 2px;
    background: var(--accent-primary);
    border-radius: 2px 2px 0 0;
}

/* — Tab Content — */
.tab-content {
    display: none;
    flex: 1;
}

.tab-content.active {
    display: flex;
    flex-direction: column;
}

.output-card-body {
    padding: 16px;
    display: flex;
    flex-direction: column;
    gap: 10px;
    flex: 1;
}

/* — Output Textarea — */
.output-card-body textarea {
    width: 100%;
    min-height: 180px;
    flex: 1;
    padding: 14px;
    background: var(--bg-dark);
    border: 1px solid var(--border-color);
    border-radius: var(--radius-sm);
    color: var(--accent-primary);
    font-family: 'JetBrains Mono', 'Fira Code', monospace;
    font-size: 12px;
    line-height: 1.7;
    resize: vertical;
    outline: none;
    transition: all var(--speed-normal) var(--ease-out);
}

.output-card-body textarea:focus {
    border-color: var(--accent-primary);
    box-shadow: 0 0 0 3px var(--accent-primary-dim);
}

.output-card-body textarea::placeholder {
    color: var(--text-dim);
}

/* — HTML Preview — */
#htmlPreviewArea {
    width: 100%;
    min-height: 160px;
    padding: 14px;
    background: var(--bg-dark);
    border: 1px solid var(--border-color);
    border-radius: var(--radius-sm);
    color: var(--accent-secondary);
    font-family: 'JetBrains Mono', 'Fira Code', monospace;
    font-size: 12px;
    line-height: 1.7;
    white-space: pre-wrap;
    word-break: break-all;
    overflow: auto;
}

/* — Output Actions — */
.output-actions {
    display: flex;
    gap: 6px;
    flex-wrap: wrap;
}

.output-btn {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    gap: 6px;
    padding: 8px 14px;
    font-size: 11.5px;
    font-weight: 600;
    font-family: inherit;
    border-radius: var(--radius-sm);
    cursor: pointer;
    transition: all var(--speed-normal) var(--ease-out);
    white-space: nowrap;
    line-height: 1;
    border: 1px solid;
}

.output-btn i { font-size: 11px; }

.output-btn.primary {
    background: linear-gradient(135deg, var(--accent-primary), #06b6d4);
    color: var(--bg-dark);
    border-color: transparent;
    font-weight: 700;
}

.output-btn.primary:hover {
    filter: brightness(1.12);
    box-shadow: 0 4px 16px rgba(34, 211, 238, 0.3);
    transform: translateY(-1px);
}

.output-btn.secondary {
    background: var(--bg-elevated);
    color: var(--text-secondary);
    border-color: var(--border-color);
}

.output-btn.secondary:hover {
    background: var(--bg-card);
    color: var(--text-white);
    border-color: var(--border-light);
    transform: translateY(-1px);
}

.output-btn.tertiary {
    background: var(--accent-secondary-dim);
    color: var(--accent-secondary);
    border-color: rgba(167, 139, 250, 0.15);
}

.output-btn.tertiary:hover {
    background: rgba(167, 139, 250, 0.2);
    border-color: var(--accent-secondary);
    transform: translateY(-1px);
}

/* — Hidden File Input — */
input[type="file"]#import-styles {
    display: none;
}

/* — Messages — */
.msg {
    display: none;
    padding: 7px 12px;
    border-radius: var(--radius-sm);
    font-size: 12px;
    font-weight: 500;
    align-items: center;
    gap: 6px;
}

.msg.visible {
    display: inline-flex;
}

.msg.success {
    background: var(--accent-green-dim);
    color: var(--accent-green);
    border: 1px solid rgba(52, 211, 153, 0.15);
}

.msg.error {
    background: var(--accent-red-dim);
    color: var(--accent-red);
    border: 1px solid rgba(248, 113, 113, 0.15);
}


/* ================================================================
   FOOTER
   ================================================================ */
.app-footer {
    margin-left: var(--sidebar-w);
    padding: 16px 20px;
    text-align: center;
    font-size: 11.5px;
    color: var(--text-dim);
    border-top: 1px solid var(--border-color);
}


/* ================================================================
   TOAST NOTIFICATIONS
   ================================================================ */
.toast-container {
    position: fixed;
    bottom: 20px;
    right: 20px;
    z-index: var(--z-toast);
    display: flex;
    flex-direction: column-reverse;
    gap: 8px;
    pointer-events: none;
}

.toast {
    padding: 10px 18px;
    background: var(--bg-card);
    border: 1px solid var(--border-color);
    border-radius: var(--radius-sm);
    color: var(--text-white);
    font-size: 12.5px;
    font-weight: 500;
    box-shadow: var(--shadow-lg);
    display: flex;
    align-items: center;
    gap: 8px;
    animation: toastIn 0.4s var(--ease-out);
    max-width: 340px;
    pointer-events: all;
    backdrop-filter: blur(16px);
}

.toast.success { border-left: 3px solid var(--accent-green); }
.toast.error   { border-left: 3px solid var(--accent-red); }
.toast.info    { border-left: 3px solid var(--accent-blue); }

@keyframes toastIn {
    from { opacity: 0; transform: translateX(40px) scale(0.95); }
    to   { opacity: 1; transform: translateX(0) scale(1); }
}


/* ================================================================
   RESPONSIVE — TABLET (≤1024px)
   ================================================================ */
@media (max-width: 1024px) {
    .sidebar {
        transform: translateX(-100%);
        width: 340px;
        box-shadow: none;
    }

    .sidebar.open {
        transform: translateX(0);
        box-shadow: var(--shadow-xl);
    }

    .sidebar-toggle {
        display: flex;
    }

    .main-content {
        margin-left: 0;
    }

    .app-footer {
        margin-left: 0;
    }
}


/* ================================================================
   RESPONSIVE — MOBILE (≤640px)
   ================================================================ */
@media (max-width: 640px) {
    :root {
        --header-h: 48px;
    }

    .sidebar {
        width: 100%;
    }

    .app-header {
        padding: 0 12px;
    }

    .app-header .logo span {
        font-size: 13px;
    }

    .header-actions {
        gap: 4px;
    }

    .header-btn {
        height: 32px;
        padding: 0 8px;
        font-size: 11px;
    }

    .header-btn span,
    .header-btn:not(.theme-btn):not(.reset-btn) {
        font-size: 0;
    }

    .header-btn i {
        font-size: 13px;
    }

    .header-btn:not(.theme-btn):not(.reset-btn) i {
        margin: 0;
    }

    .main-content {
        padding: 12px;
        gap: 14px;
    }

    .preview-wrapper {
        padding: 14px;
    }

    #preview-box {
        font-size: 22px;
        min-height: 200px;
        padding: 20px;
    }

    .preset-cards {
        grid-template-columns: 1fr;
    }

    .btn-grid {
        grid-template-columns: repeat(auto-fill, minmax(90px, 1fr));
    }

    .output-tab {
        padding: 10px 12px;
        font-size: 11.5px;
    }

    .output-card-body {
        padding: 12px;
    }

    .toast-container {
        left: 12px;
        right: 12px;
        bottom: 76px;
    }

    .toast {
        max-width: 100%;
    }
}

/* ================================================================
   RESPONSIVE — Small Mobile (≤400px)
   ================================================================ */
@media (max-width: 400px) {
    .app-header .logo i { display: none; }

    .header-btn.reset-btn span {
        display: none;
    }

    .form-row {
        flex-direction: column;
        gap: 4px;
    }

    .form-row > input,
    .form-row > select {
        width: 100%;
    }
}


/* ================================================================
   PRINT
   ================================================================ */
@media print {
    .sidebar,
    .app-header,
    .sidebar-toggle,
    .sidebar-overlay,
    .toast-container,
    .app-footer,
    .output-actions,
    .preview-text-input {
        display: none !important;
    }

    .main-content {
        margin: 0;
        padding: 20px;
    }

    .app-container {
        padding-top: 0;
    }
}


/* ================================================================
   UTILITY: iro.js color picker overrides
   ================================================================ */
.IroColorPicker {
    margin: 0 auto;
}

.IroSlider {
    margin-top: 8px !important;
}
    </style>
</head>
<body>
    <!-- TOAST CONTAINER -->
    <div class="toast-container" id="toastContainer"></div>

    <!-- HEADER -->
    <header class="app-header">
        <a class="logo" href="#">
            <i class="fas fa-wand-magic-sparkles"></i>
            <span>K3N4N CSS Generator V6.0</span>
        </a>
        <div class="header-actions">
            <button class="header-btn" data-action="undo" disabled data-tooltip="Geri Al (Ctrl+Z)"><i class="fas fa-undo-alt"></i> Geri</button>
            <button class="header-btn" data-action="redo" disabled data-tooltip="İleri Al (Ctrl+Y)"><i class="fas fa-redo-alt"></i> İleri</button>
            <button class="header-btn theme-btn" data-action="toggle-theme" data-tooltip="Tema Değiştir"><i class="fas fa-moon"></i></button>
            <button class="header-btn reset-btn" data-action="reset-all" data-tooltip="Tümünü Sıfırla"><i class="fas fa-trash-restore"></i> <span>Sıfırla</span></button>
        </div>
    </header>

    <!-- MOBILE SIDEBAR TOGGLE -->
    <button class="sidebar-toggle" id="sidebarToggle" aria-label="Menüyü aç/kapat"><i class="fas fa-sliders-h"></i></button>
    <div class="sidebar-overlay" id="sidebarOverlay"></div>

    <!-- MAIN LAYOUT -->
    <div class="app-container">
        <!-- SIDEBAR -->
        <aside class="sidebar" id="sidebar">
            <div class="sidebar-search">
                <i class="fas fa-search"></i>
                <input type="text" id="panelSearch" placeholder="Panel ara... (metin, arka plan, çerçeve...)" aria-label="Panel arama">
            </div>

            <!-- 1. METİN STİLLERİ -->
            <div class="panel expanded" data-panel="text">
                <div class="panel-header">
                    <div class="panel-icon text"><i class="fas fa-font"></i></div>
                    <span class="panel-title">Metin Stilleri</span>
                    <i class="fas fa-chevron-up panel-toggle"></i>
                </div>
                <div class="panel-body">
                    <div class="btn-grid">
                        <button class="style-btn" data-style-target="random-font"><i class="fas fa-dice"></i> Rnd Font</button>
                        <button class="style-btn" data-style-target="random-color"><i class="fas fa-palette"></i> Rnd Renk</button>
                        <button class="style-btn" data-style-target="random-text-shadow"><i class="fas fa-clone"></i> Rnd Gölge</button>
                        <button class="style-btn" data-style-target="random-text-decoration"><i class="fas fa-underline"></i> Rnd Dekor</button>
                        <button class="style-btn" data-style-target="random-spacing"><i class="fas fa-arrows-alt-h"></i> Rnd Boşluk</button>
                        <button class="style-btn" data-style-target="random-align"><i class="fas fa-align-center"></i> Rnd Hiza</button>
                        <button class="style-btn" data-style-target="random-line-height"><i class="fas fa-text-height"></i> Rnd Satır</button>
                        <button class="style-btn" data-style-target="random-text-transform"><i class="fas fa-text-width"></i> Rnd Dönüşüm</button>
                    </div>
                    <div class="separator"></div>
                    <div class="form-group">
                        <label for="fontFamily">Yazı Fontu</label>
                        <select id="fontFamily" data-style-prop="fontFamily">
                            <option value="'Poppins', sans-serif">Poppins</option>
                            <option value="'Inter', sans-serif">Inter</option>
                            <option value="'Space Grotesk', sans-serif">Space Grotesk</option>
                            <option value="'VT323', monospace">VT323</option>
                            <option value="'Press Start 2P', monospace">Press Start 2P</option>
                            <option value="'Orbitron', sans-serif">Orbitron</option>
                            <option value="'Roboto Mono', monospace">Roboto Mono</option>
                            <option value="'JetBrains Mono', monospace">JetBrains Mono</option>
                            <option value="'Lobster', cursive">Lobster</option>
                            <option value="'Kaushan Script', cursive">Kaushan Script</option>
                            <option value="'Fira Code', monospace">Fira Code</option>
                            <option value="Georgia, serif">Georgia</option>
                            <option value="'Courier New', monospace">Courier New</option>
                            <option value="Impact, sans-serif">Impact</option>
                        </select>
                    </div>
                    <div class="form-group">
                        <label>Yazı Boyutu <span class="value-badge" id="fontSizeVal">30px</span></label>
                        <input type="range" id="fontSizeRange" min="8" max="120" value="30">
                        <input type="number" id="fontSize" data-style-prop="fontSize" data-style-unit="px" value="30" min="1" max="200">
                    </div>
                    <div class="form-group">
                        <label>Font Weight <span class="value-badge" id="fontWeightVal">400</span></label>
                        <input type="range" id="fontWeightRange" min="100" max="900" step="100" value="400">
                        <select id="fontWeight" data-style-prop="fontWeight">
                            <option value="100">100 - Thin</option>
                            <option value="200">200 - Extra Light</option>
                            <option value="300">300 - Light</option>
                            <option value="400" selected>400 - Normal</option>
                            <option value="500">500 - Medium</option>
                            <option value="600">600 - Semi Bold</option>
                            <option value="700">700 - Bold</option>
                            <option value="800">800 - Extra Bold</option>
                            <option value="900">900 - Black</option>
                        </select>
                    </div>
                    <div class="form-group">
                        <label>Yazı Rengi</label>
                        <div id="textColorPicker" class="color-picker-container"></div>
                    </div>
                    <div class="form-group">
                        <label>Yazı Gölgesi</label>
                        <div class="form-row">
                            <label>X:</label><input type="number" id="textShadowX" value="0">
                            <label>Y:</label><input type="number" id="textShadowY" value="0">
                            <label>Blur:</label><input type="number" id="textShadowBlur" value="0" min="0">
                        </div>
                        <div id="textShadowColorPicker" class="color-picker-container"></div>
                    </div>
                    <div class="form-group">
                        <label>Dekorasyon</label>
                        <div class="form-row">
                            <select id="textDecorationLine" data-style-prop="textDecorationLine">
                                <option value="none" selected>Yok</option>
                                <option value="underline">Altı Çizili</option>
                                <option value="overline">Üstü Çizili</option>
                                <option value="line-through">Üzerinden</option>
                            </select>
                            <select id="textDecorationStyle" data-style-prop="textDecorationStyle">
                                <option value="solid" selected>Düz</option>
                                <option value="double">Çift</option>
                                <option value="dotted">Noktalı</option>
                                <option value="dashed">Kesikli</option>
                                <option value="wavy">Dalgalı</option>
                            </select>
                        </div>
                    </div>
                    <div class="form-group">
                        <label for="textAlign">Hizalama</label>
                        <select id="textAlign" data-style-prop="textAlign">
                            <option value="left">Sola</option>
                            <option value="center" selected>Ortala</option>
                            <option value="right">Sağa</option>
                            <option value="justify">İki Yana</option>
                        </select>
                    </div>
                    <div class="form-group">
                        <label>Satır Yüksekliği <span class="value-badge" id="lineHeightVal">1.5</span></label>
                        <input type="range" id="lineHeightRange" min="0.5" max="4" step="0.1" value="1.5">
                    </div>
                    <div class="form-group">
                        <label>Boşluklar</label>
                        <div class="form-row">
                            <label>Harf:</label><input type="number" id="letterSpacing" data-style-prop="letterSpacing" data-style-unit="px" value="0" step="0.5">
                            <label>Kelime:</label><input type="number" id="wordSpacing" data-style-prop="wordSpacing" data-style-unit="px" value="0" step="0.5">
                        </div>
                    </div>
                    <div class="form-group">
                        <label>Padding</label>
                        <div class="form-row">
                            <label>Sol:</label><input type="number" id="paddingLeft" value="0" min="0">
                            <label>Sağ:</label><input type="number" id="paddingRight" value="0" min="0">
                            <label>Üst:</label><input type="number" id="paddingTop" value="0" min="0">
                            <label>Alt:</label><input type="number" id="paddingBottom" value="0" min="0">
                        </div>
                        <select id="paddingUnit">
                            <option value="px" selected>px</option>
                            <option value="%">%</option>
                            <option value="rem">rem</option>
                            <option value="em">em</option>
                        </select>
                    </div>
                    <div class="form-group">
                        <label for="textTransform">Metin Dönüşümü</label>
                        <select id="textTransform" data-style-prop="textTransform">
                            <option value="none" selected>Yok</option>
                            <option value="uppercase">BÜYÜK HARF</option>
                            <option value="lowercase">küçük harf</option>
                            <option value="capitalize">Baş Harf Büyük</option>
                        </select>
                    </div>
                    <div class="form-group">
                        <label for="fontStyle">Font Stili</label>
                        <select id="fontStyle" data-style-prop="fontStyle">
                            <option value="normal" selected>Normal</option>
                            <option value="italic">İtalik</option>
                            <option value="oblique">Eğik</option>
                        </select>
                    </div>
                    <div class="form-group">
                        <label for="writingMode">Yazı Yönü</label>
                        <select id="writingMode" data-style-prop="writingMode">
                            <option value="horizontal-tb" selected>Yatay (Normal)</option>
                            <option value="vertical-rl">Dikey (Sağ-Sol)</option>
                            <option value="vertical-lr">Dikey (Sol-Sağ)</option>
                        </select>
                    </div>
                    <div class="form-group">
                        <label for="textOverflow">Taşma Davranışı</label>
                        <select id="textOverflow" data-style-prop="textOverflow">
                            <option value="clip" selected>Kes</option>
                            <option value="ellipsis">Üç Nokta (...)</option>
                        </select>
                    </div>
                </div>
            </div>

            <!-- 2. ARKA PLAN -->
            <div class="panel" data-panel="background">
                <div class="panel-header">
                    <div class="panel-icon bg"><i class="fas fa-fill-drip"></i></div>
                    <span class="panel-title">Arka Plan</span>
                    <i class="fas fa-chevron-up panel-toggle"></i>
                </div>
                <div class="panel-body">
                    <div class="btn-grid">
                        <button class="style-btn" data-style-target="random-bg-color"><i class="fas fa-fill"></i> Rnd Renk</button>
                        <button class="style-btn" data-style-target="random-gradient"><i class="fas fa-grip-lines"></i> Rnd Gradyan</button>
                        <button class="style-btn" data-style-target="random-bg-gif"><i class="fas fa-film"></i> Rnd GIF</button>
                        <button class="style-btn" data-style-target="random-bg-position"><i class="fas fa-arrows-alt"></i> Rnd Konum</button>
                        <button class="style-btn" data-style-target="random-bg-size"><i class="fas fa-expand"></i> Rnd Boyut</button>
                        <button class="style-btn" data-style-target="random-bg-opacity"><i class="fas fa-adjust"></i> Rnd Opaklık</button>
                        <button class="style-btn" data-style-target="random-bg-pattern"><i class="fas fa-th"></i> Rnd Desen</button>
                        <button class="style-btn" data-style-target="random-bg-blend"><i class="fas fa-layer-group"></i> Rnd Karıştırma</button>
                    </div>
                    <div class="separator"></div>
                    <div class="form-group">
                        <label>Arka Plan Rengi</label>
                        <div id="backgroundColorPicker" class="color-picker-container"></div>
                    </div>
                    <div class="form-group">
                        <label>Opaklık <span class="value-badge" id="bgOpacityVal">1</span></label>
                        <input type="range" id="backgroundOpacityRange" min="0" max="1" step="0.05" value="1">
                    </div>
                    <div class="form-group">
                        <label>GIF/Resim URL</label>
                        <input type="text" id="backgroundImageUrl" placeholder="URL girin...">
                    </div>
                    <div class="form-group">
                        <label>Konum</label>
                        <div class="form-row">
                            <label>X:</label><input type="text" id="backgroundPositionX" placeholder="center">
                            <label>Y:</label><input type="text" id="backgroundPositionY" placeholder="center">
                        </div>
                    </div>
                    <div class="form-group">
                        <label>Boyut</label>
                        <select id="backgroundSize" data-style-prop="backgroundSize">
                            <option value="auto" selected>Otomatik</option>
                            <option value="cover">Kapla</option>
                            <option value="contain">İçer</option>
                            <option value="100% 100%">100% 100%</option>
                            <option value="50% 50%">50% 50%</option>
                        </select>
                    </div>
                    <div class="form-group">
                        <label>Tekrar</label>
                        <select id="backgroundRepeat" data-style-prop="backgroundRepeat">
                            <option value="repeat" selected>Tekrarla</option>
                            <option value="no-repeat">Tekrarlama</option>
                            <option value="repeat-x">Yatay Tekrar</option>
                            <option value="repeat-y">Dikey Tekrar</option>
                        </select>
                    </div>
                    <div class="form-group">
                        <label>Karıştırma Modu</label>
                        <select id="backgroundBlendMode" data-style-prop="backgroundBlendMode">
                            <option value="normal" selected>Normal</option>
                            <option value="multiply">Çarpma</option>
                            <option value="screen">Ekran</option>
                            <option value="overlay">Kaplama</option>
                            <option value="darken">Koyulaştır</option>
                            <option value="lighten">Aydınlat</option>
                            <option value="color-dodge">Renk Etkisi</option>
                            <option value="difference">Fark</option>
                            <option value="hue">Ton</option>
                            <option value="saturation">Doygunluk</option>
                        </select>
                    </div>
                    <div class="separator"></div>
                    <div class="form-group">
                        <label>Gradyan Düzenleyici</label>
                        <div class="form-row">
                            <label>Yön:</label><input type="number" id="gradientAngle" value="90" min="0" max="360">
                            <label>Tür:</label>
                            <select id="gradientType">
                                <option value="linear" selected>Doğrusal</option>
                                <option value="radial">Radyal</option>
                                <option value="conic">Konik</option>
                            </select>
                        </div>
                        <div id="gradientColors" class="gradient-colors"></div>
                        <button class="add-color-btn" id="addGradientColor"><i class="fas fa-plus"></i> Renk Ekle</button>
                    </div>
                </div>
            </div>

            <!-- 3. ÇERÇEVE -->
            <div class="panel" data-panel="border">
                <div class="panel-header">
                    <div class="panel-icon border"><i class="fas fa-border-all"></i></div>
                    <span class="panel-title">Çerçeve & Kenarlar</span>
                    <i class="fas fa-chevron-up panel-toggle"></i>
                </div>
                <div class="panel-body">
                    <div class="btn-grid">
                        <button class="style-btn" data-style-target="random-multi-border"><i class="fas fa-border-style"></i> Rnd Çerçeve</button>
                        <button class="style-btn" data-style-target="random-outline"><i class="fas fa-square"></i> Rnd Dış Çizgi</button>
                        <button class="style-btn" data-style-target="random-border-radius"><i class="fas fa-circle"></i> Rnd Yuvarla</button>
                        <button class="style-btn" data-style-target="random-border-color"><i class="fas fa-palette"></i> Rnd Renk</button>
                    </div>
                    <div class="separator"></div>
                    <div class="form-group">
                        <label>Kenar Genişliği</label>
                        <div class="form-row">
                            <label>Üst:</label><input type="text" id="borderTop" data-style-prop="borderTop" placeholder="2px solid #000">
                            <label>Alt:</label><input type="text" id="borderBottom" data-style-prop="borderBottom" placeholder="2px solid #000">
                        </div>
                        <div class="form-row">
                            <label>Sol:</label><input type="text" id="borderLeft" data-style-prop="borderLeft" placeholder="2px solid #000">
                            <label>Sağ:</label><input type="text" id="borderRight" data-style-prop="borderRight" placeholder="2px solid #000">
                        </div>
                    </div>
                    <div class="form-group">
                        <label>Yuvarlak Kenarlar <span class="value-badge" id="borderRadiusVal">0px</span></label>
                        <input type="range" id="borderRadiusAll" min="0" max="200" value="0">
                        <div class="form-row">
                            <label>ÜS:</label><input type="number" id="borderRadiusTopLeft" data-style-prop="borderTopLeftRadius" data-style-unit="px" value="0" min="0">
                            <label>ÜSa:</label><input type="number" id="borderRadiusTopRight" data-style-prop="borderTopRightRadius" data-style-unit="px" value="0" min="0">
                        </div>
                        <div class="form-row">
                            <label>AS:</label><input type="number" id="borderRadiusBottomLeft" data-style-prop="borderBottomLeftRadius" data-style-unit="px" value="0" min="0">
                            <label>ASa:</label><input type="number" id="borderRadiusBottomRight" data-style-prop="borderBottomRightRadius" data-style-unit="px" value="0" min="0">
                        </div>
                    </div>
                    <div class="form-group">
                        <label>Dış Çizgi (Outline)</label>
                        <div class="form-row">
                            <label>Genişlik:</label><input type="number" id="outlineWidth" data-style-prop="outlineWidth" data-style-unit="px" value="0" min="0">
                            <label>Stil:</label>
                            <select id="outlineStyle" data-style-prop="outlineStyle">
                                <option value="none" selected>Yok</option>
                                <option value="solid">Düz</option>
                                <option value="dashed">Kesik</option>
                                <option value="dotted">Noktalı</option>
                                <option value="double">Çift</option>
                                <option value="groove">Oluk</option>
                                <option value="ridge">Çıkıntı</option>
                            </select>
                        </div>
                        <div id="outlineColorPicker" class="color-picker-container"></div>
                    </div>
                    <div class="form-group">
                        <label>Outline Offset</label>
                        <input type="number" id="outlineOffset" data-style-prop="outlineOffset" data-style-unit="px" value="0">
                    </div>
                </div>
            </div>

            <!-- 4. DÖNÜŞÜM -->
            <div class="panel" data-panel="transform">
                <div class="panel-header">
                    <div class="panel-icon transform"><i class="fas fa-cube"></i></div>
                    <span class="panel-title">Dönüşüm (Transform)</span>
                    <i class="fas fa-chevron-up panel-toggle"></i>
                </div>
                <div class="panel-body">
                    <div class="btn-grid">
                        <button class="style-btn" data-style-target="random-transform"><i class="fas fa-sync"></i> Rnd Dönüşüm</button>
                        <button class="style-btn" data-style-target="reset-transform"><i class="fas fa-undo"></i> Sıfırla</button>
                    </div>
                    <div class="separator"></div>
                    <div class="form-group">
                        <label>Döndür <span class="value-badge" id="rotateVal">0°</span></label>
                        <input type="range" id="rotateRange" min="-360" max="360" value="0">
                        <input type="number" id="rotate" value="0">
                    </div>
                    <div class="form-group">
                        <label>Ölçek <span class="value-badge" id="scaleVal">1</span></label>
                        <input type="range" id="scaleRange" min="0.1" max="3" step="0.05" value="1">
                    </div>
                    <div class="form-group">
                        <label>Eğme</label>
                        <div class="form-row">
                            <label>X:</label><input type="number" id="skewX" value="0">
                            <label>Y:</label><input type="number" id="skewY" value="0">
                        </div>
                    </div>
                    <div class="form-group">
                        <label>Taşıma (Translate)</label>
                        <div class="form-row">
                            <label>X:</label><input type="number" id="translateX" value="0">
                            <label>Y:</label><input type="number" id="translateY" value="0">
                        </div>
                    </div>
                    <div class="form-group">
                        <label>Transform Origin</label>
                        <select id="transformOrigin" data-style-prop="transformOrigin">
                            <option value="center center" selected>Orta</option>
                            <option value="top left">Üst Sol</option>
                            <option value="top right">Üst Sağ</option>
                            <option value="bottom left">Alt Sol</option>
                            <option value="bottom right">Alt Sağ</option>
                            <option value="top center">Üst Orta</option>
                            <option value="bottom center">Alt Orta</option>
                        </select>
                    </div>
                </div>
            </div>

            <!-- 5. KUTU GÖLGESİ -->
            <div class="panel" data-panel="shadow">
                <div class="panel-header">
                    <div class="panel-icon shadow"><i class="fas fa-clone"></i></div>
                    <span class="panel-title">Kutu Gölgesi</span>
                    <i class="fas fa-chevron-up panel-toggle"></i>
                </div>
                <div class="panel-body">
                    <div class="btn-grid">
                        <button class="style-btn" data-style-target="random-box-shadow"><i class="fas fa-clone"></i> Rnd Gölge</button>
                        <button class="style-btn" data-style-target="random-box-shadow-color"><i class="fas fa-palette"></i> Rnd Renk</button>
                        <button class="style-btn" data-style-target="random-multi-shadow"><i class="fas fa-layer-group"></i> Rnd Çoklu</button>
                        <button class="style-btn" data-style-target="random-inset-shadow"><i class="fas fa-compress-alt"></i> Rnd İç Gölge</button>
                    </div>
                    <div class="separator"></div>
                    <div class="form-group">
                        <label>Gölge Ayarları</label>
                        <div class="form-row">
                            <label>X:</label><input type="number" id="boxShadowX" value="0">
                            <label>Y:</label><input type="number" id="boxShadowY" value="4">
                            <label>Blur:</label><input type="number" id="boxShadowBlur" value="15" min="0">
                            <label>Spread:</label><input type="number" id="boxShadowSpread" value="0">
                        </div>
                        <label style="font-size:0.78em;color:var(--text-secondary);margin-top:4px;display:flex;align-items:center;gap:5px;cursor:pointer;">
                            <input type="checkbox" id="boxShadowInset" style="accent-color:var(--accent-primary);cursor:pointer;"> İç Gölge (inset)
                        </label>
                        <div id="boxShadowColorPicker" class="color-picker-container"></div>
                    </div>
                </div>
            </div>

            <!-- 6. ANİMASYON -->
            <div class="panel" data-panel="animation">
                <div class="panel-header">
                    <div class="panel-icon anim"><i class="fas fa-play"></i></div>
                    <span class="panel-title">Animasyon / Geçiş</span>
                    <i class="fas fa-chevron-up panel-toggle"></i>
                </div>
                <div class="panel-body">
                    <div class="btn-grid">
                        <button class="style-btn" data-style-target="random-animation"><i class="fas fa-random"></i> Rnd Anim</button>
                        <button class="style-btn" data-style-target="random-timing-function"><i class="fas fa-clock"></i> Rnd Zamanlama</button>
                        <button class="style-btn" data-style-target="random-iteration-count"><i class="fas fa-redo"></i> Rnd Tekrar</button>
                        <button class="style-btn" data-style-target="stop-animation"><i class="fas fa-stop"></i> Durdur</button>
                    </div>
                    <div class="separator"></div>
                    <div class="form-group">
                        <label>Hazır Animasyonlar</label>
                        <select id="presetAnimation">
                            <option value="">Seçin...</option>
                            <option value="bounce">Zıpla</option>
                            <option value="pulse">Nabız</option>
                            <option value="shake">Salla</option>
                            <option value="fadeIn">Belir</option>
                            <option value="fadeOut">Kaybol</option>
                            <option value="slideInLeft">Sol Kayış</option>
                            <option value="slideInRight">Sağ Kayış</option>
                            <option value="rotateIn">Dönerek Gel</option>
                            <option value="zoomIn">Büyüyerek Gel</option>
                            <option value="flip">Çevir</option>
                            <option value="swing">Sallan</option>
                            <option value="rubberBand">Lastik</option>
                            <option value="jello">Jöle</option>
                            <option value="heartBeat">Kalp Atışı</option>
                            <option value="float">Süzül</option>
                            <option value="glitch">Glitch</option>
                            <option value="neonPulse">Neon Nabız</option>
                            <option value="typewriter">Daktilo</option>
                        </select>
                    </div>
                    <div class="form-group">
                        <label>Süre <span class="value-badge" id="animDurationVal">1s</span></label>
                        <input type="range" id="animationDurationRange" min="0.1" max="10" step="0.1" value="1">
                    </div>
                    <div class="form-group">
                        <label>Zamanlama</label>
                        <select id="animationTimingFunction" data-style-prop="animationTimingFunction">
                            <option value="ease" selected>Ease</option>
                            <option value="linear">Linear</option>
                            <option value="ease-in">Ease-In</option>
                            <option value="ease-out">Ease-Out</option>
                            <option value="ease-in-out">Ease-In-Out</option>
                            <option value="cubic-bezier(0.68, -0.55, 0.265, 1.55)">Bounce</option>
                            <option value="cubic-bezier(0.25, 0.46, 0.45, 0.94)">Soft</option>
                            <option value="steps(10)">Steps(10)</option>
                        </select>
                    </div>
                    <div class="form-group">
                        <label>Tekrar</label>
                        <select id="animationIterationCount">
                            <option value="1" selected>1</option>
                            <option value="2">2</option>
                            <option value="3">3</option>
                            <option value="5">5</option>
                            <option value="infinite">Sonsuz</option>
                        </select>
                    </div>
                    <div class="form-group">
                        <label>Yön</label>
                        <select id="animationDirection" data-style-prop="animationDirection">
                            <option value="normal" selected>Normal</option>
                            <option value="reverse">Ters</option>
                            <option value="alternate">Alternatif</option>
                            <option value="alternate-reverse">Alternatif Ters</option>
                        </select>
                    </div>
                    <div class="form-group">
                        <label>Geçiş (Transition)</label>
                        <div class="form-row">
                            <select id="transitionProperty">
                                <option value="all" selected>Tümü</option>
                                <option value="transform">Transform</option>
                                <option value="opacity">Opaklık</option>
                                <option value="background-color">Arkaplan</option>
                                <option value="color">Renk</option>
                                <option value="box-shadow">Gölge</option>
                            </select>
                            <input type="number" id="transitionDuration" value="0.3" min="0" step="0.1" style="width:60px;">
                            <span style="font-size:0.78em;color:var(--text-secondary);">s</span>
                        </div>
                    </div>
                    <div class="form-group">
                        <label>Özel Keyframes</label>
                        <textarea id="animationKeyframes" placeholder="@keyframes myAnim { 0% { ... } 100% { ... } }"></textarea>
                        <button class="add-color-btn" id="applyKeyframesBtn"><i class="fas fa-play"></i> Keyframes Uygula</button>
                    </div>
                </div>
            </div>

            <!-- 7. KIRMA / CLİP PATH -->
            <div class="panel" data-panel="clip">
                <div class="panel-header">
                    <div class="panel-icon clip"><i class="fas fa-cut"></i></div>
                    <span class="panel-title">Kırma (Clip-Path)</span>
                    <i class="fas fa-chevron-up panel-toggle"></i>
                </div>
                <div class="panel-body">
                    <div class="btn-grid">
                        <button class="style-btn" data-style-target="random-clip-path"><i class="fas fa-cut"></i> Rnd Kırma</button>
                        <button class="style-btn" data-style-target="reset-clip"><i class="fas fa-undo"></i> Sıfırla</button>
                    </div>
                    <div class="separator"></div>
                    <div class="form-group">
                        <label>Hazır Şekiller</label>
                        <select id="presetClipPath">
                            <option value="">Seçin...</option>
                            <option value="none">Yok</option>
                            <option value="circle(50% at 50% 50%)">Daire</option>
                            <option value="ellipse(40% 50% at 50% 50%)">Elips</option>
                            <option value="polygon(50% 0%, 100% 50%, 50% 100%, 0% 50%)">Elmas</option>
                            <option value="polygon(50% 0%, 100% 100%, 0% 100%)">Üçgen</option>
                            <option value="polygon(25% 0%, 75% 0%, 100% 50%, 75% 100%, 25% 100%, 0% 50%)">Altıgen</option>
                            <option value="polygon(50% 0%, 61% 35%, 98% 35%, 68% 57%, 79% 91%, 50% 70%, 21% 91%, 32% 57%, 2% 35%, 39% 35%)">Yıldız</option>
                            <option value="polygon(0% 0%, 100% 0%, 100% 75%, 75% 75%, 75% 100%, 50% 75%, 0% 75%)">Konuşma Balonu</option>
                            <option value="polygon(20% 0%, 80% 0%, 100% 20%, 100% 80%, 80% 100%, 20% 100%, 0% 80%, 0% 20%)">Sekizgen</option>
                            <option value="inset(5% 5% 5% 5% round 10px)">Yuvarlak İç</option>
                            <option value="polygon(0% 15%, 15% 15%, 15% 0%, 85% 0%, 85% 15%, 100% 15%, 100% 85%, 85% 85%, 85% 100%, 15% 100%, 15% 85%, 0% 85%)">Artı</option>
                        </select>
                    </div>
                    <div class="form-group">
                        <label>Özel Clip-Path</label>
                        <input type="text" id="clipPath" data-style-prop="clipPath" placeholder="polygon(50% 0%, ...)">
                    </div>
                </div>
            </div>

            <!-- 8. TRANSPARAN YAZI -->
            <div class="panel" data-panel="transparent">
                <div class="panel-header">
                    <div class="panel-icon transparent"><i class="fas fa-eye-dropper"></i></div>
                    <span class="panel-title">Transparan / Gradyan Yazı</span>
                    <i class="fas fa-chevron-up panel-toggle"></i>
                </div>
                <div class="panel-body">
                    <div class="btn-grid">
                        <button class="style-btn" data-style-target="random-text-opacity"><i class="fas fa-adjust"></i> Rnd Opaklık</button>
                        <button class="style-btn" data-style-target="random-text-gradient"><i class="fas fa-grip-lines"></i> Rnd Gradyan</button>
                        <button class="style-btn" data-style-target="random-text-image-fill"><i class="fas fa-image"></i> Rnd Resim</button>
                        <button class="style-btn" data-style-target="reset-text-fill"><i class="fas fa-undo"></i> Sıfırla</button>
                    </div>
                    <div class="separator"></div>
                    <div class="form-group">
                        <label>Opaklık <span class="value-badge" id="textOpacityVal">1</span></label>
                        <input type="range" id="textOpacityRange" min="0" max="1" step="0.05" value="1">
                    </div>
                    <div class="form-group">
                        <label>Metin Gradyan</label>
                        <div class="form-row">
                            <label>Yön:</label><input type="number" id="textGradientAngle" value="90" min="0" max="360">
                            <label>Tür:</label>
                            <select id="textGradientType">
                                <option value="linear" selected>Doğrusal</option>
                                <option value="radial">Radyal</option>
                            </select>
                        </div>
                        <div id="textGradientColors" class="gradient-colors"></div>
                        <button class="add-color-btn" id="addTextGradientColor"><i class="fas fa-plus"></i> Renk Ekle</button>
                    </div>
                    <div class="form-group">
                        <label>Resim Dolgusu URL</label>
                        <input type="text" id="textImageFill" placeholder="Resim URL...">
                    </div>
                    <div class="form-group">
                        <label>Mix Blend Mode</label>
                        <select id="mixBlendMode" data-style-prop="mixBlendMode">
                            <option value="normal" selected>Normal</option>
                            <option value="multiply">Çarpma</option>
                            <option value="screen">Ekran</option>
                            <option value="overlay">Kaplama</option>
                            <option value="difference">Fark</option>
                            <option value="exclusion">Dışlama</option>
                            <option value="color-dodge">Renk Etkisi</option>
                        </select>
                    </div>
                </div>
            </div>

            <!-- 9. RENK PALETİ -->
            <div class="panel" data-panel="palette">
                <div class="panel-header">
                    <div class="panel-icon palette"><i class="fas fa-swatchbook"></i></div>
                    <span class="panel-title">Renk Paleti Oluşturucu</span>
                    <i class="fas fa-chevron-up panel-toggle"></i>
                </div>
                <div class="panel-body">
                    <div class="btn-grid">
                        <button class="style-btn" data-style-target="generate-palette"><i class="fas fa-swatchbook"></i> Oluştur</button>
                        <button class="style-btn" data-style-target="random-palette"><i class="fas fa-dice"></i> Rnd Palet</button>
                    </div>
                    <div class="separator"></div>
                    <div class="form-group">
                        <label>Temel Renk</label>
                        <div id="baseColorPicker" class="color-picker-container"></div>
                    </div>
                    <div class="form-group">
                        <label>Palet Tipi</label>
                        <select id="paletteType">
                            <option value="monochromatic">Monokromatik</option>
                            <option value="analogous">Analog</option>
                            <option value="complementary">Tamamlayıcı</option>
                            <option value="triadic">Triadik</option>
                            <option value="split-complementary">Bölünmüş Tamamlayıcı</option>
                            <option value="tetradic">Tetradik</option>
                        </select>
                    </div>
                    <div class="form-group">
                        <label>Renk Sayısı</label>
                        <input type="number" id="paletteSize" value="5" min="2" max="12">
                    </div>
                    <div class="form-group">
                        <label>Palet Önizleme</label>
                        <div id="palettePreview" class="palette-preview"></div>
                    </div>
                </div>
            </div>

            <!-- 10. EFEKTLER -->
            <div class="panel" data-panel="effects">
                <div class="panel-header">
                    <div class="panel-icon effects"><i class="fas fa-magic"></i></div>
                    <span class="panel-title">Filtre & Efektler</span>
                    <i class="fas fa-chevron-up panel-toggle"></i>
                </div>
                <div class="panel-body">
                    <div class="btn-grid">
                        <button class="style-btn" data-style-target="random-filter"><i class="fas fa-filter"></i> Rnd Filtre</button>
                        <button class="style-btn" data-style-target="random-cursor"><i class="fas fa-mouse-pointer"></i> Rnd İmleç</button>
                        <button class="style-btn" data-style-target="random-effect"><i class="fas fa-star"></i> Rnd Efekt</button>
                        <button class="style-btn" data-style-target="reset-filters"><i class="fas fa-undo"></i> Sıfırla</button>
                    </div>
                    <div class="separator"></div>
                    <div class="form-group">
                        <label>Bulanıklık <span class="value-badge" id="blurVal">0px</span></label>
                        <input type="range" id="filterBlurRange" min="0" max="30" value="0">
                    </div>
                    <div class="form-group">
                        <label>Parlaklık <span class="value-badge" id="brightnessVal">100%</span></label>
                        <input type="range" id="filterBrightnessRange" min="0" max="300" value="100">
                    </div>
                    <div class="form-group">
                        <label>Kontrast <span class="value-badge" id="contrastVal">100%</span></label>
                        <input type="range" id="filterContrastRange" min="0" max="300" value="100">
                    </div>
                    <div class="form-group">
                        <label>Doygunluk <span class="value-badge" id="saturateVal">100%</span></label>
                        <input type="range" id="filterSaturateRange" min="0" max="300" value="100">
                    </div>
                    <div class="form-group">
                        <label>Ton Döndürme <span class="value-badge" id="hueRotateVal">0°</span></label>
                        <input type="range" id="filterHueRotateRange" min="0" max="360" value="0">
                    </div>
                    <div class="form-group">
                        <label>Ters Çevir <span class="value-badge" id="invertVal">0%</span></label>
                        <input type="range" id="filterInvertRange" min="0" max="100" value="0">
                    </div>
                    <div class="form-group">
                        <label>Sepya <span class="value-badge" id="sepiaVal">0%</span></label>
                        <input type="range" id="filterSepiaRange" min="0" max="100" value="0">
                    </div>
                    <div class="form-group">
                        <label>Gri Tonlama <span class="value-badge" id="grayscaleVal">0%</span></label>
                        <input type="range" id="filterGrayscaleRange" min="0" max="100" value="0">
                    </div>
                    <div class="form-group">
                        <label>Backdrop Blur</label>
                        <input type="range" id="backdropBlurRange" min="0" max="30" value="0">
                    </div>
                    <div class="form-group">
                        <label>İmleç</label>
                        <select id="cursor" data-style-prop="cursor">
                            <option value="auto" selected>Otomatik</option>
                            <option value="pointer">İşaretçi</option>
                            <option value="crosshair">Artı</option>
                            <option value="move">Taşı</option>
                            <option value="text">Metin</option>
                            <option value="not-allowed">Yasak</option>
                            <option value="grab">Yakala</option>
                            <option value="zoom-in">Yakınlaştır</option>
                            <option value="zoom-out">Uzaklaştır</option>
                            <option value="wait">Bekle</option>
                            <option value="help">Yardım</option>
                            <option value="none">Gizle</option>
                        </select>
                    </div>
                </div>
            </div>

            <!-- 11. LAYOUT -->
            <div class="panel" data-panel="layout">
                <div class="panel-header">
                    <div class="panel-icon layout"><i class="fas fa-th-large"></i></div>
                    <span class="panel-title">Boyut & Düzen</span>
                    <i class="fas fa-chevron-up panel-toggle"></i>
                </div>
                <div class="panel-body">
                    <div class="form-group">
                        <label>Genişlik</label>
                        <div class="form-row">
                            <input type="text" id="boxWidth" placeholder="auto" data-style-prop="width">
                            <select id="widthUnit" style="width:60px;">
                                <option value="px">px</option>
                                <option value="%">%</option>
                                <option value="vw">vw</option>
                                <option value="rem">rem</option>
                            </select>
                        </div>
                    </div>
                    <div class="form-group">
                        <label>Yükseklik</label>
                        <div class="form-row">
                            <input type="text" id="boxHeight" placeholder="auto" data-style-prop="height">
                            <select id="heightUnit" style="width:60px;">
                                <option value="px">px</option>
                                <option value="%">%</option>
                                <option value="vh">vh</option>
                                <option value="rem">rem</option>
                            </select>
                        </div>
                    </div>
                    <div class="form-group">
                        <label>Min/Max Genişlik</label>
                        <div class="form-row">
                            <label>Min:</label><input type="text" id="minWidth" placeholder="auto" data-style-prop="minWidth">
                            <label>Max:</label><input type="text" id="maxWidth" placeholder="auto" data-style-prop="maxWidth">
                        </div>
                    </div>
                    <div class="form-group">
                        <label>Min/Max Yükseklik</label>
                        <div class="form-row">
                            <label>Min:</label><input type="text" id="minHeight" placeholder="auto" data-style-prop="minHeight">
                            <label>Max:</label><input type="text" id="maxHeight" placeholder="auto" data-style-prop="maxHeight">
                        </div>
                    </div>
                    <div class="form-group">
                        <label>Overflow</label>
                        <select id="overflow" data-style-prop="overflow">
                            <option value="hidden" selected>Gizle</option>
                            <option value="visible">Göster</option>
                            <option value="scroll">Kaydır</option>
                            <option value="auto">Otomatik</option>
                        </select>
                    </div>
                    <div class="form-group">
                        <label>Display</label>
                        <select id="display" data-style-prop="display">
                            <option value="flex" selected>Flex</option>
                            <option value="block">Block</option>
                            <option value="inline-block">Inline Block</option>
                            <option value="grid">Grid</option>
                            <option value="inline-flex">Inline Flex</option>
                        </select>
                    </div>
                    <div class="form-group">
                        <label>Flex Yönü</label>
                        <select id="flexDirection" data-style-prop="flexDirection">
                            <option value="row">Satır</option>
                            <option value="column">Sütun</option>
                            <option value="row-reverse">Satır Ters</option>
                            <option value="column-reverse">Sütun Ters</option>
                        </select>
                    </div>
                    <div class="form-group">
                        <label>Justify Content</label>
                        <select id="justifyContent" data-style-prop="justifyContent">
                            <option value="center" selected>Ortala</option>
                            <option value="flex-start">Başlangıç</option>
                            <option value="flex-end">Bitiş</option>
                            <option value="space-between">Arası Boşluk</option>
                            <option value="space-around">Etrafı Boşluk</option>
                            <option value="space-evenly">Eşit Boşluk</option>
                        </select>
                    </div>
                    <div class="form-group">
                        <label>Align Items</label>
                        <select id="alignItems" data-style-prop="alignItems">
                            <option value="center" selected>Ortala</option>
                            <option value="flex-start">Başlangıç</option>
                            <option value="flex-end">Bitiş</option>
                            <option value="stretch">Esnet</option>
                            <option value="baseline">Taban Çizgisi</option>
                        </select>
                    </div>
                    <div class="form-group">
                        <label>Gap</label>
                        <input type="text" id="gap" data-style-prop="gap" placeholder="0px">
                    </div>
                </div>
            </div>

            <!-- 12. HAZIR TEMALAR -->
            <div class="panel" data-panel="presets">
                <div class="panel-header">
                    <div class="panel-icon presets"><i class="fas fa-palette"></i></div>
                    <span class="panel-title">Hazır Temalar</span>
                    <i class="fas fa-chevron-up panel-toggle"></i>
                </div>
                <div class="panel-body">
                    <div class="preset-cards">
                        <button class="preset-card" data-style-target="auto-theme-neon"><i class="fas fa-lightbulb"></i> Neon</button>
                        <button class="preset-card" data-style-target="auto-theme-minimal"><i class="fas fa-compress"></i> Minimal</button>
                        <button class="preset-card" data-style-target="auto-theme-vintage"><i class="fas fa-camera-retro"></i> Vintage</button>
                        <button class="preset-card" data-style-target="auto-theme-glassmorphism"><i class="fas fa-glass-whiskey"></i> Glass</button>
                        <button class="preset-card" data-style-target="auto-theme-neumorphism"><i class="fas fa-circle"></i> Neumorphism</button>
                        <button class="preset-card" data-style-target="auto-theme-cyberpunk"><i class="fas fa-robot"></i> Cyberpunk</button>
                        <button class="preset-card" data-style-target="auto-theme-nature"><i class="fas fa-leaf"></i> Doğa</button>
                        <button class="preset-card" data-style-target="auto-theme-ocean"><i class="fas fa-water"></i> Okyanus</button>
                        <button class="preset-card" data-style-target="auto-theme-sunset"><i class="fas fa-sun"></i> Gün Batımı</button>
                        <button class="preset-card" data-style-target="auto-theme-dark-elegant"><i class="fas fa-gem"></i> Zarif Karanlık</button>
                    </div>
                </div>
            </div>

            <!-- 13. KAOS MOTORU -->
            <div class="panel" data-panel="chaos">
                <div class="panel-header">
                    <div class="panel-icon chaos"><i class="fas fa-explosion"></i></div>
                    <span class="panel-title">Kaos Motoru</span>
                    <i class="fas fa-chevron-up panel-toggle"></i>
                </div>
                <div class="panel-body">
                    <div class="btn-grid">
                        <button class="style-btn chaos-btn" data-style-target="auto-generate" style="grid-column:1/-1;padding:12px;font-size:0.9em;">
                            <i class="fas fa-wand-magic-sparkles"></i> Otomatik Stil Oluştur
                        </button>
                        <button class="style-btn chaos-btn" data-style-target="max-chaos" style="grid-column:1/-1;padding:12px;font-size:0.9em;">
                            <i class="fas fa-explosion"></i> MAKSİMUM KAOS!
                        </button>
                    </div>
                    <div class="separator"></div>
                    <div class="form-group">
                        <label>Kaos Kategorileri</label>
                        <div class="checkbox-row">
                            <label><input type="checkbox" id="chaosFont" checked> Yazı</label>
                            <label><input type="checkbox" id="chaosBackground" checked> Arka Plan</label>
                            <label><input type="checkbox" id="chaosBorder" checked> Çerçeve</label>
                        </div>
                        <div class="checkbox-row">
                            <label><input type="checkbox" id="chaosEffects" checked> Efektler</label>
                            <label><input type="checkbox" id="chaosAnimation" checked> Animasyon</label>
                            <label><input type="checkbox" id="chaosClip" checked> Kırma</label>
                        </div>
                        <div class="checkbox-row">
                            <label><input type="checkbox" id="chaosTransform" checked> Dönüşüm</label>
                            <label><input type="checkbox" id="chaosBoxShadow" checked> Gölge</label>
                            <label><input type="checkbox" id="chaosTextGradient" checked> Gradyan</label>
                        </div>
                        <div class="checkbox-row">
                            <label><input type="checkbox" id="chaosTextImage" checked> Resim Dolgusu</label>
                            <label><input type="checkbox" id="chaosOpacity" checked> Opaklık</label>
                            <label><input type="checkbox" id="chaosLayout" checked> Düzen</label>
                        </div>
                    </div>
                </div>
            </div>
        </aside>

        <!-- MAIN CONTENT -->
        <main class="main-content">
            <!-- PREVIEW -->
            <div class="preview-wrapper">
                <div class="preview-label">
                    <h3><i class="fas fa-eye"></i> Canlı Önizleme</h3>
                    <span class="preview-dimensions" id="previewDimensions">-- × --</span>
                </div>
                <div id="preview-box">K3N4N V6.0</div>
                <div class="preview-text-input">
                    <input type="text" id="customText" placeholder="Önizleme metnini değiştir..." maxlength="100">
                    <span class="char-count" id="charCount">0/100</span>
                </div>
            </div>

            <!-- CSS OUTPUT -->
            <div class="output-card">
                <div class="output-tabs">
                    <button class="output-tab active" data-tab="css-tab">CSS Çıktısı</button>
                    <button class="output-tab" data-tab="html-tab">HTML Önizleme</button>
                    <button class="output-tab" data-tab="input-tab">Özel CSS</button>
                </div>

                <div class="tab-content active" id="css-tab">
                    <div class="output-card-body">
                        <textarea id="css-output" readonly></textarea>
                        <div class="output-actions">
                            <button class="output-btn primary" id="copy-css-btn"><i class="fas fa-copy"></i> Kopyala</button>
                            <button class="output-btn secondary" data-action="download-css"><i class="fas fa-download"></i> CSS İndir</button>
                            <button class="output-btn secondary" data-action="download-html"><i class="fas fa-file-code"></i> HTML İndir</button>
                            <button class="output-btn tertiary" data-action="export-styles"><i class="fas fa-file-export"></i> Dışa Aktar</button>
                            <button class="output-btn tertiary" data-action="import-styles"><i class="fas fa-file-import"></i> İçe Aktar</button>
                            <input type="file" id="import-styles" accept=".json">
                        </div>
                        <div class="msg success" id="copy-success"><i class="fas fa-check-circle"></i> CSS panoya kopyalandı!</div>
                        <div class="msg error" id="copy-error"><i class="fas fa-exclamation-circle"></i> Kopyalama başarısız.</div>
                    </div>
                </div>

                <div class="tab-content" id="html-tab">
                    <div class="output-card-body">
                        <div id="htmlPreviewArea"></div>
                    </div>
                </div>

                <div class="tab-content" id="input-tab">
                    <div class="output-card-body">
                        <textarea id="cssInputArea" placeholder="Özel CSS kodunuzu buraya girin..."></textarea>
                        <div class="output-actions">
                            <button class="output-btn primary" id="applyCustomCss"><i class="fas fa-check"></i> CSS Uygula</button>
                        </div>
                        <div class="msg success" id="css-success"><i class="fas fa-check-circle"></i> CSS başarıyla uygulandı!</div>
                        <div class="msg error" id="css-error"><i class="fas fa-exclamation-circle"></i> Geçersiz CSS.</div>
                    </div>
                </div>
            </div>
        </main>
    </div>

    <!-- FOOTER -->
    <footer class="app-footer">
        <p>K3N4N CSS Stil Generator V6.0 © 2025 — Tüm hakları saklıdır.</p>
    </footer>

    <script>
    (function() {
        'use strict';

        const $ = id => document.getElementById(id);
        const $$ = sel => document.querySelectorAll(sel);

        const previewBox = $('preview-box');
        const cssOutput = $('css-output');
        const cssInputArea = $('cssInputArea');
        const customTextInput = $('customText');
        const htmlPreviewArea = $('htmlPreviewArea');
        const toastContainer = $('toastContainer');

        let currentTheme = 'dark';
        let history = [];
        let historyIndex = -1;
        const MAX_HISTORY = 80;

        let currentStyles = getDefaultStyles();

        function getDefaultStyles() {
            return {
                fontFamily: "'Poppins', sans-serif",
                fontSize: '30px',
                fontWeight: '400',
                fontStyle: 'normal',
                color: '#222222',
                textShadow: 'none',
                textDecorationLine: 'none',
                textDecorationStyle: 'solid',
                textAlign: 'center',
                lineHeight: '1.5',
                letterSpacing: '0px',
                wordSpacing: '0px',
                textTransform: 'none',
                writingMode: 'horizontal-tb',
                textOverflow: 'clip',
                paddingLeft: '0px',
                paddingRight: '0px',
                paddingTop: '0px',
                paddingBottom: '0px',
                backgroundColor: '#ffffff',
                backgroundImage: 'none',
                backgroundPositionX: 'center',
                backgroundPositionY: 'center',
                backgroundSize: 'auto',
                backgroundRepeat: 'repeat',
                backgroundBlendMode: 'normal',
                opacity: '1',
                borderTop: '1px solid #cccccc',
                borderBottom: '1px solid #cccccc',
                borderLeft: '1px solid #cccccc',
                borderRight: '1px solid #cccccc',
                borderTopLeftRadius: '10px',
                borderTopRightRadius: '10px',
                borderBottomLeftRadius: '10px',
                borderBottomRightRadius: '10px',
                outlineWidth: '0px',
                outlineStyle: 'none',
                outlineColor: '#ffffff',
                outlineOffset: '0px',
                transform: 'none',
                transformOrigin: 'center center',
                boxShadow: '0 4px 15px rgba(0, 0, 0, 0.08)',
                animationName: 'none',
                animationDuration: '1s',
                animationTimingFunction: 'ease',
                animationIterationCount: '1',
                animationDirection: 'normal',
                clipPath: 'none',
                filter: 'none',
                backdropFilter: 'none',
                cursor: 'auto',
                backgroundClip: 'border-box',
                webkitTextFillColor: '',
                webkitBackgroundClip: '',
                mixBlendMode: 'normal',
                width: 'auto',
                height: 'auto',

### GLM 4.7
*2026-02-07 18:34:58 +03*

<think>
1.  **Analyze the Request:**
    *   **Input:** A large HTML file containing a CSS generator application ("K3N4N CSS Stil Generator V6.0"). The user provided the full code.
    *   **User's Goal:** The user wants to modernize this code ("tamyı uyumlu", "kodlamaya uygun", "modern edıtor olarak").
    *   **Specific Instructions:** "Yalnızca CSS kodunu yazabilirsin ya da tam kodu yaz nasıl istersen" (You can write only the CSS code or the full code, whatever you prefer).
    *   **Implicit Needs:**
        *   The provided code is functional but looks a bit cluttered and has some legacy patterns (e.g., extensive inline styles in JS, large data structures).
        *   "Modern editor" implies better responsiveness, cleaner UI, more accessible controls, and perhaps a more professional "IDE-like" feel (dark mode already exists but could be refined, better typography, smoother transitions).
        *   "Tamyı uyumlu" likely means cross-browser compatible or typo for "tam uyumlu" (fully compatible).
        *   The code structure is mostly HTML + CSS + JS in one file. Refactoring this into a cleaner, more modular structure (even within one file) would be beneficial.

2.  **Strategy for Modernization:**

    *   **UI/UX Improvements:**
        *   Update the color palette to be more professional (refined dark mode contrast).
        *   Improve the sidebar and main layout (flexbox/grid is already used, but can be tightened).
        *   Make input fields look like modern "Design Tools" (e.g., Figma/Canva vibes).
        *   Add better visual feedback (toasts, hover states).

    *   **Code Quality & Performance:**
        *   Organize CSS variables (`:root`) more systematically.
        *   Use CSS Grid/Flexbox more effectively for the control panels.
        *   Clean up the JavaScript structure (use classes or cleaner modules for logic separation, though since it's a single file, a cleaner IIFE structure is best).
        *   Ensure touch targets are large enough for mobile.

    *   **Specific "Modern Editor" Features:**
        *   Sticky header/sidebar.
        *   Better syntax highlighting simulation for the output area.
        *   Cleaner Accordion animations.

3.  **Execution Steps:**

    *   *Step 1: CSS Overhaul.* This is the most visible part. I will rewrite the CSS to use modern layout techniques (`gap`, `clamp`, updated `backdrop-filter`), sharper borders, and a more cohesive color scheme (Slate/Cyan/Indigo).
    *   *Step 2: HTML Cleanup.* Adjust class names to be semantic where possible, ensure `aria` labels are present, and simplify the DOM structure slightly.
    *   *Step 3: JavaScript Refinement.* Ensure the logic robustly handles the new CSS classes and DOM structure. The existing logic is actually quite comprehensive (randomizers, gradients, etc.), so I will keep the logic but ensure it binds correctly.

4.  **Drafting the "Modern" Version (Mental Sandbox):**

    *   *Color Palette:* Switch from the somewhat generic dark blue to a deep "Zinc" or "Slate" background with vibrant, but accessible, accent colors (Cyan/Violet).
    *   *Typography:* Use `Inter` consistently. Make sure the UI text isn't too small (`rem` units).
    *   *Controls:* Custom scrollbars, styled range sliders (which are tricky but look good), and cleaner buttons.
    *   *Layout:* A classic "Sidebar Left, Preview Right, Bottom/Overlay Code" layout. Or keep the current "Sidebar Left, Sidebar Right (Code)" layout but clean it up. The original has "Sidebar Left, Main Content Right". I'll stick to that but make the sidebar floating/collapsible with a glassmorphism effect.

5.  **Refining the Output:**

    Since the user asked for *how I want*, providing the **full modernized code** is the most helpful and "ready-to-use" approach. Writing just CSS would be confusing if the HTML structure needed to change to support it.

    *Plan:*
    1.  **CSS:** Rewrite `:root` variables. Use CSS Grid for the sidebar panels (making them cards). Custom styling for `input[type="range"]`. Improved Toast animations.
    2.  **HTML:** Keep the structure but update classes to match the new CSS.
    3.  **JS:** Keep the core logic as it's good, but update references to IDs and classes that might have changed.

6.  **Writing the Code (Iterative refinement during drafting):**

    *   *Sidebar:* Make it a floating panel on desktop? No, standard sidebar is better for generators. Let's make it clean with distinct headers.
    *   *Inputs:* Add focus rings that look distinct (e.g., a glow).
    *   *Preview Area:* Add a checkerboard background for transparency checks.
    *   *Code Output:* Style it like a mini code editor (monospace font, line numbers lookalike background).

7.  **Final Polish:**
    *   Check responsiveness (media queries).
    *   Ensure the "Kaos" (Chaos) engine and other JS features still map correctly to the DOM.
    *   Translate UI labels to Turkish as in the original source.

8.  **Output Generation:** (This matches the provided good response, combining HTML, CSS, and JS into a single, polished file).

    *   *Self-Correction during code generation:* The original code had a lot of specific IDs. To make it "modern editor" style, I should group inputs better and make the inputs themselves look like form fields (light background with dark text, or dark bg with light text depending on theme). I will stick to a Dark Theme by default as it's popular for dev tools.

    *   *Key Modern CSS features to add:*
        *   `scrollbar-gutter: stable`
        *   `accent-color` for checkboxes/radios.
        *   BackdropFilters for the header.

9.  **Final Result Structure:**
    *   `<!DOCTYPE html>`
    *   `<html>`
    *   `<head>` (Fonts, CSS Reset, Main Styles)
    *   `<body>` (Sidebar, Main Preview, Output, Scripts)

    (I will provide the single complete file as it's the most reliable way to ensure the user has a working "modern editor" immediately).

Let's write the code. I will focus on:
1.  **Visuals:** A "VS Code" / "Figma" inspired aesthetic.
2.  **UX:** Collapsible panels are smoother. Buttons have hover states.
3.  **Responsiveness:** Mobile menu works better.

*(Proceeding to generate the Turkish response with the full code)*
</think>Harika bir proje! Verdiğin temel kod oldukça kapsamlı ancak "Modern Editor" (modern bir tasarım arayüzü) hissiyatını güçlendirmek ve kod yapısını daha temiz, sürdürülebilir bir hale getirmek için **Full Code** (tam kod) olarak yeniden düzenledim.

Yapılan Modernizasyonlar:
1.  **UI/UX:** "VS Code" ve "Figma" benzeri koyu (dark) tema, daha temiz tipografi ve iyileştirilmiş boşluk (spacing) düzeni.
2.  **CSS Grid & Flex:** Düzen sistemi daha güçlü hale getirildi, yan menüyü ve önizleme alanını daha profesyonel böldü.
3.  **Form Elemanları:** Range slider'lar, inputlar ve butonlar modernize edildi, `accent-color` kullanıldı.
4.  **Performans:** DOM seçicilerioptimize edildi, CSS değişkenleri (`:root`) merkezi yönetim için düzenlendi.

İşte modernize edilmiş, tek dosya halinde (HTML + CSS + JS) **K3N4N CSS Generator V7.0 (Modern Edition)**:

```html
<!DOCTYPE html>
<html lang="tr" data-theme="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>K3N4N CSS Generator V7.0 (Modern Studio)</title>
    <!-- Fonts -->
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500&family=Space+Grotesk:wght@500;700&display=swap" rel="stylesheet">
    <!-- Icons -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
    <!-- Libraries -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/chroma-js/2.4.2/chroma.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/@jaames/iro@5/dist/iro.min.js"></script>

    <style>
        /* =========================================
           MODERN CSS STUDIO V7.0
           ========================================= */
        
        /* --- RESET & VARIABLES --- */
        :root {
            /* Palette: Dark Studio */
            --bg-app: #0f1115;
            --bg-sidebar: #161b22;
            --bg-panel: #1f242e;
            --bg-input: #0d1117;
            --bg-surface: #262c36;
            
            /* Text Colors */
            --text-main: #e6edf3;
            --text-muted: #8b949e;
            --text-dim: #6e7681;
            --text-accent: #58a6ff;
            
            /* Accents */
            --primary: #238636; /* Green like commit */
            --primary-hover: #2ea043;
            --accent-blue: #1f6feb;
            --accent-purple: #8957e5;
            --accent-pink: #db61a2;
            --accent-cyan: #39c5bb;
            --border-color: #30363d;
            --border-active: #8b949e;
            
            /* Effects */
            --shadow-sm: 0 1px 2px rgba(0,0,0,0.3);
            --shadow-md: 0 4px 12px rgba(0,0,0,0.4);
            --shadow-lg: 0 10px 30px rgba(0,0,0,0.5);
            --radius-xs: 4px;
            --radius-sm: 6px;
            --radius-md: 8px;
            --radius-lg: 12px;
            
            /* Transitions */
            --trans-fast: 0.15s ease;
            --trans-norm: 0.25s cubic-bezier(0.2, 0, 0, 1);
        }

        * { margin: 0; padding: 0; box-sizing: border-box; outline: none; }
        
        html { font-size: 16px; scroll-behavior: smooth; }
        
        body {
            font-family: 'Inter', sans-serif;
            background-color: var(--bg-app);
            color: var(--text-main);
            height: 100vh;
            overflow: hidden;
            display: flex;
            flex-direction: column;
        }

        /* Custom Scrollbar */
        ::-webkit-scrollbar { width: 6px; height: 6px; }
        ::-webkit-scrollbar-track { background: transparent; }
        ::-webkit-scrollbar-thumb { background: var(--bg-surface); border-radius: 3px; }
        ::-webkit-scrollbar-thumb:hover { background: var(--text-dim); }

        /* --- LAYOUT STRUCTURE --- */
        .app-header {
            height: 50px;
            background: rgba(22, 27, 34, 0.95);
            border-bottom: 1px solid var(--border-color);
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 0 20px;
            backdrop-filter: blur(10px);
            z-index: 100;
            flex-shrink: 0;
        }

        .logo {
            font-family: 'Space Grotesk', sans-serif;
            font-weight: 700;
            font-size: 18px;
            color: var(--text-main);
            display: flex;
            align-items: center;
            gap: 10px;
        }
        .logo i { color: var(--accent-cyan); }
        .logo span { background: linear-gradient(90deg, #fff, #8b949e); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }

        .header-actions { display: flex; gap: 10px; }

        .app-body {
            display: flex;
            flex: 1;
            overflow: hidden;
            position: relative;
        }

        /* --- SIDEBAR --- */
        .sidebar {
            width: 320px;
            background: var(--bg-sidebar);
            border-right: 1px solid var(--border-color);
            display: flex;
            flex-direction: column;
            overflow-y: auto;
            padding: 15px;
            gap: 15px;
            flex-shrink: 0;
            transition: transform var(--trans-norm);
        }

        .search-box {
            background: var(--bg-input);
            border: 1px solid var(--border-color);
            border-radius: var(--radius-md);
            padding: 8px 12px;
            display: flex;
            align-items: center;
            gap: 8px;
            color: var(--text-muted);
        }
        .search-box input {
            background: transparent;
            border: none;
            color: var(--text-main);
            width: 100%;
            font-size: 13px;
        }

        /* --- PANELS (Accordion) --- */
        .panel {
            background: var(--bg-panel);
            border: 1px solid var(--border-color);
            border-radius: var(--radius-md);
            overflow: hidden;
            transition: border-color var(--trans-fast);
        }
        .panel:hover { border-color: var(--text-dim); }

        .panel-header {
            padding: 12px 16px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            cursor: pointer;
            background: rgba(255,255,255,0.02);
            user-select: none;
            border-bottom: 1px solid transparent;
        }
        .panel.expanded .panel-header {
            background: rgba(255,255,255,0.04);
            border-bottom: 1px solid var(--border-color);
        }

        .panel-info { display: flex; align-items: center; gap: 10px; }
        .panel-icon { 
            width: 24px; height: 24px; 
            display: flex; align-items: center; justify-content: center;
            border-radius: 4px;
            font-size: 12px;
        }
        .panel-title { font-size: 13px; font-weight: 600; }
        .panel-arrow { font-size: 10px; color: var(--text-dim); transition: transform 0.3s; }
        .panel.expanded .panel-arrow { transform: rotate(180deg); }

        .panel-body {
            max-height: 0;
            overflow: hidden;
            transition: max-height 0.3s ease-out;
            padding: 0 16px;
        }
        .panel.expanded .panel-body { padding: 16px; max-height: 1000px; overflow-y: auto; }

        /* --- CONTROLS --- */
        .control-group { margin-bottom: 16px; }
        .control-label {
            font-size: 11px;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            color: var(--text-muted);
            margin-bottom: 8px;
            display: flex;
            justify-content: space-between;
        }

        /* Inputs */
        .input-text, .input-select, .input-number {
            width: 100%;
            background: var(--bg-input);
            border: 1px solid var(--border-color);
            color: var(--text-main);
            padding: 8px 10px;
            border-radius: var(--radius-sm);
            font-family: inherit;
            font-size: 13px;
            transition: all var(--trans-fast);
        }
        .input-text:focus, .input-select:focus, .input-number:focus {
            border-color: var(--accent-blue);
            box-shadow: 0 0 0 2px rgba(31, 111, 235, 0.2);
        }

        /* Range Slider */
        .range-wrapper {
            display: flex;
            align-items: center;
            gap: 10px;
        }
        input[type="range"] {
            flex: 1;
            -webkit-appearance: none;
            height: 4px;
            background: var(--bg-surface);
            border-radius: 2px;
            cursor: pointer;
        }
        input[type="range"]::-webkit-slider-thumb {
            -webkit-appearance: none;
            width: 16px; height: 16px;
            background: var(--text-main);
            border-radius: 50%;
            border: 2px solid var(--bg-panel);
            box-shadow: 0 0 0 2px var(--accent-blue);
            transition: transform 0.1s;
        }
        input[type="range"]::-webkit-slider-thumb:hover { transform: scale(1.1); }
        .range-val {
            width: 45px;
            text-align: right;
            font-size: 12px;
            font-family: 'JetBrains Mono', monospace;
            color: var(--text-accent);
        }

        /* Buttons */
        .btn {
            background: var(--bg-surface);
            border: 1px solid var(--border-color);
            color: var(--text-main);
            padding: 6px 12px;
            border-radius: var(--radius-sm);
            font-size: 12px;
            cursor: pointer;
            transition: all var(--trans-fast);
            display: inline-flex;
            align-items: center;
            justify-content: center;
            gap: 6px;
        }
        .btn:hover { background: var(--border-active); border-color: var(--text-muted); transform: translateY(-1px); }
        .btn:active { transform: translateY(0); }
        
        .btn-primary { background: var(--primary); border-color: rgba(255,255,255,0.1); color: #fff; }
        .btn-primary:hover { background: var(--primary-hover); }
        
        .btn-icon { width: 32px; padding: 0; }
        .btn-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 8px; }
        .btn-sm { font-size: 11px; padding: 4px 8px; }

        /* Color Picker Placeholder */
        .color-wrap { display: flex; gap: 10px; align-items: center; }
        .iro-color-picker { margin: 0 !important; }

        /* --- MAIN AREA --- */
        .main-workspace {
            flex: 1;
            display: flex;
            flex-direction: column;
            background: repeating-conic-gradient(#161b22 0% 25%, #0d1117 0% 50%) 50% / 20px 20px;
            position: relative;
            overflow-y: auto;
            padding: 30px;
        }

        .preview-card {
            background: rgba(31, 36, 46, 0.7);
            backdrop-filter: blur(10px);
            border: 1px solid var(--border-color);
            border-radius: var(--radius-lg);
            padding: 20px;
            min-height: 300px;
            display: flex;
            align-items: center;
            justify-content: center;
            margin-bottom: 20px;
            box-shadow: var(--shadow-lg);
            position: relative;
        }
        
        #preview-box {
            box-sizing: border-box; /* Critical */
            text-align: center;
            line-height: 1.4;
            transition: all 0.2s ease;
            max-width: 100%;
            word-break: break-word;
        }

        .preview-controls {
            position: absolute;
            top: 15px;
            right: 15px;
            background: var(--bg-panel);
            padding: 5px;
            border-radius: var(--radius-sm);
            border: 1px solid var(--border-color);
            display: flex;
            gap: 5px;
        }

        /* --- CODE EDITOR PANEL --- */
        .code-panel {
            background: var(--bg-sidebar);
            border: 1px solid var(--border-color);
            border-radius: var(--radius-lg);
            display: flex;
            flex-direction: column;
            overflow: hidden;
            min-height: 250px;
            max-height: 500px;
        }
        
        .code-tabs {
            display: flex;
            background: var(--bg-panel);
            border-bottom: 1px solid var(--border-color);
        }
        .code-tab {
            padding: 10px 20px;
            font-size: 13px;
            color: var(--text-muted);
            cursor: pointer;
            border-right: 1px solid var(--border-color);
            transition: all 0.2s;
        }
        .code-tab:hover { background: rgba(255,255,255,0.05); color: var(--text-main); }
        .code-tab.active { background: var(--bg-sidebar); color: var(--text-accent); border-top: 2px solid var(--text-accent); }
        .code-tab:last-child { border-right: none; }

        .code-content {
            position: relative;
            flex: 1;
            overflow: hidden;
            background: #0d1117;
        }
        
        .code-editor {
            width: 100%;
            height: 100%;
            background: transparent;
            border: none;
            color: #a5d6ff;
            font-family: 'JetBrains Mono', monospace;
            font-size: 13px;
            padding: 15px;
            resize: none;
            line-height: 1.5;
        }

        .code-actions {
            display: flex;
            justify-content: flex-end;
            gap: 10px;
            padding: 10px;
            background: var(--bg-panel);
            border-top: 1px solid var(--border-color);
        }

        /* --- TOASTS --- */
        .toast-container {
            position: fixed;
            bottom: 20px;
            right: 20px;
            z-index: 9999;
            display: flex;
            flex-direction: column;
            gap: 10px;
            pointer-events: none;
        }
        .toast {
            background: var(--bg-panel);
            border: 1px solid var(--border-color);
            border-left: 4px solid var(--primary);
            color: var(--text-main);
            padding: 12px 16px;
            border-radius: var(--radius-sm);
            box-shadow: var(--shadow-lg);
            font-size: 13px;
            display: flex;
            align-items: center;
            gap: 10px;
            animation: slideIn 0.3s cubic-bezier(0.2, 0.8, 0.2, 1);
            pointer-events: all;
            min-width: 250px;
        }
        @keyframes slideIn { from { transform: translateX(50px); opacity: 0; } to { transform: translateX(0); opacity: 1; } }

        /* --- UTILS --- */
        .hidden { display: none !important; }
        .badge {
            background: var(--bg-surface);
            padding: 2px 6px;
            border-radius: 4px;
            font-size: 10px;
            color: var(--text-muted);
        }
        
        /* Mobile Toggle */
        .mobile-toggle { display: none; background: none; border: none; color: var(--text-main); font-size: 20px; cursor: pointer; }

        @media (max-width: 900px) {
            .mobile-toggle { display: block; }
            .sidebar {
                position: fixed;
                top: 50px;
                left: 0; bottom: 0;
                z-index: 90;
                transform: translateX(-100%);
                width: 280px;
            }
            .sidebar.active { transform: translateX(0); }
            .overlay {
                position: fixed; inset: 0; background: rgba(0,0,0,0.6); z-index: 80;
                opacity: 0; pointer-events: none; transition: opacity 0.3s;
            }
            .overlay.active { opacity: 1; pointer-events: all; }
        }
    </style>
</head>
<body>

    <!-- HEADER -->
    <header class="app-header">
        <div class="logo">
            <i class="fas fa-code"></i>
            <span>K3N4N STUDIO <small style="font-size:0.5em; opacity:0.6; font-weight:400">v7.0</small></span>
        </div>
        <div class="header-actions">
            <button class="btn btn-icon" id="btnUndo" title="Geri Al (Ctrl+Z)"><i class="fas fa-undo-alt"></i></button>
            <button class="btn btn-icon" id="btnRedo" title="İleri Al (Ctrl+Y)"><i class="fas fa-redo-alt"></i></button>
            <button class="btn btn-sm" id="btnReset"><i class="fas fa-trash-alt"></i> Sıfırla</button>
            <button class="mobile-toggle" id="menuToggle"><i class="fas fa-bars"></i></button>
        </div>
    </header>

    <div class="app-body">
        <!-- MOBILE OVERLAY -->
        <div class="overlay" id="sidebarOverlay"></div>

        <!-- SIDEBAR CONTROLS -->
        <aside class="sidebar" id="sidebar">
            <!-- Search -->
            <div class="search-box">
                <i class="fas fa-search"></i>
                <input type="text" id="panelSearch" placeholder="Ara: font, border, shadow...">
            </div>

            <!-- 1. TYPOGRAPHY -->
            <div class="panel expanded" data-panel="typography">
                <div class="panel-header">
                    <div class="panel-info">
                        <div class="panel-icon" style="background:rgba(88,166,255,0.2); color:#58a6ff"><i class="fas fa-font"></i></div>
                        <span class="panel-title">Tipografi</span>
                    </div>
                    <i class="fas fa-chevron-down panel-arrow"></i>
                </div>
                <div class="panel-body">
                    <div class="btn-grid">
                        <button class="btn btn-sm" onclick="randomFont()">Rnd Font</button>
                        <button class="btn btn-sm" onclick="randomColor()">Rnd Renk</button>
                    </div>
                    <br>
                    <div class="control-group">
                        <label class="control-label">Font Ailesi</label>
                        <select class="input-select" id="fontFamily">
                            <option value="'Inter', sans-serif">Inter</option>
                            <option value="'Space Grotesk', sans-serif">Space Grotesk</option>
                            <option value="'JetBrains Mono', monospace">JetBrains Mono</option>
                            <option value="Arial, sans-serif">Arial</option>
                            <option value="'Times New Roman', serif">Times New Roman</option>
                            <option value="cursive">Cursive (Handwrite)</option>
                        </select>
                    </div>
                    <div class="control-group">
                        <label class="control-label">Boyut <span class="badge" id="fontSizeBadge">30px</span></label>
                        <div class="range-wrapper">
                            <input type="range" id="fontSizeRange" min="10" max="120" value="30">
                            <input type="number" class="input-number" id="fontSizeInput" value="30" style="width:50px">
                        </div>
                    </div>
                    <div class="control-group">
                        <label class="control-label">Ağırlık</label>
                        <div class="range-wrapper">
                            <input type="range" id="fontWeightRange" min="100" max="900" step="100" value="400">
                            <div class="range-val" id="fontWeightVal">400</div>
                        </div>
                    </div>
                    <div class="control-group">
                        <label class="control-label">Rengi</label>
                        <div class="color-wrap">
                            <div id="textColorPicker"></div>
                            <input type="text" class="input-text" id="textColorText" value="#e6edf3">
                        </div>
                    </div>
                    <div class="control-group">
                        <label class="control-label">Hizalama</label>
                        <div class="btn-grid">
                            <button class="btn btn-sm" onclick="updateStyle('textAlign','left')"><i class="fas fa-align-left"></i></button>
                            <button class="btn btn-sm" onclick="updateStyle('textAlign','center')"><i class="fas fa-align-center"></i></button>
                            <button class="btn btn-sm" onclick="updateStyle('textAlign','right')"><i class="fas fa-align-right"></i></button>
                            <button class="btn btn-sm" onclick="updateStyle('textAlign','justify')"><i class="fas fa-align-justify"></i></button>
                        </div>
                    </div>
                    <div class="control-group">
                        <label class="control-label">Dönüşüm</label>
                        <select class="input-select" id="textTransform" onchange="updateStyle('textTransform', this.value)">
                            <option value="none">Normal</option>
                            <option value="uppercase">BÜYÜK HARF</option>
                            <option value="lowercase">küçük harf</option>
                            <option value="capitalize">Baş Harf Büyük</option>
                        </select>
                    </div>
                </div>
            </div>

            <!-- 2. BACKGROUND -->
            <div class="panel" data-panel="background">
                <div class="panel-header">
                    <div class="panel-info">
                        <div class="panel-icon" style="background:rgba(217,70,239,0.2); color:#d946ef"><i class="fas fa-fill-drip"></i></div>
                        <span class="panel-title">Arka Plan</span>
                    </div>
                    <i class="fas fa-chevron-down panel-arrow"></i>
                </div>
                <div class="panel-body">
                    <div class="btn-grid">
                        <button class="btn btn-sm" onclick="randomBgColor()">Solid</button>
                        <button class="btn btn-sm" onclick="randomGradient()">Gradient</button>
                    </div>
                    <div class="control-group">
                        <label class="control-label">Renk</label>
                        <div class="color-wrap">
                            <div id="bgColorPicker"></div>
                            <input type="text" class="input-text" id="bgColorText" value="#00000000">
                        </div>
                    </div>
                    <div class="control-group">
                        <label class="control-label">Resim URL</label>
                        <input type="text" class="input-text" id="bgImageUrl" placeholder="https://...">
                    </div>
                </div>
            </div>

            <!-- 3. BORDER & RADIUS -->
            <div class="panel" data-panel="border">
                <div class="panel-header">
                    <div class="panel-info">
                        <div class="panel-icon" style="background:rgba(250,204,21,0.2); color:#facc15"><i class="fas fa-vector-square"></i></div>
                        <span class="panel-title">Çerçeve</span>
                    </div>
                    <i class="fas fa-chevron-down panel-arrow"></i>
                </div>
                <div class="panel-body">
                    <div class="control-group">
                        <label class="control-label">Tüm Kenarlar</label>
                        <div class="btn-grid" style="grid-template-columns: 1fr 1fr 1fr 1fr; gap:4px;">
                            <input type="number" class="input-number" id="borderWidth" placeholder="px" value="0">
                            <select class="input-select" id="borderStyle">
                                <option value="solid">Solid</option>
                                <option value="dashed">Dashed</option>
                                <option value="dotted">Dotted</option>
                                <option value="double">Double</option>
                            </select>
                            <div id="borderColorPicker" style="width:100%;"></div>
                            <button class="btn btn-sm" onclick="updateBorder()">Uygula</button>
                        </div>
                    </div>
                    <div class="control-group">
                        <label class="control-label">Yuvarlaklık <span class="badge" id="radiusBadge">0px</span></label>
                        <div class="range-wrapper">
                            <input type="range" id="borderRadiusRange" min="0" max="100" value="0">
                        </div>
                        <div class="btn-grid" style="margin-top:10px;">
                            <button class="btn btn-sm" onclick="setRadius(0, '50%', true)">Pill</button>
                            <button class="btn btn-sm" onclick="setRadius(50, true)">Circle</button>
                        </div>
                    </div>
                </div>
            </div>

            <!-- 4. SHADOWS -->
            <div class="panel" data-panel="shadows">
                <div class="panel-header">
                    <div class="panel-info">
                        <div class="panel-icon" style="background:rgba(107,114,128,0.3); color:#9ca3af"><i class="fas fa-clone"></i></div>
                        <span class="panel-title">Gölgeler</span>
                    </div>
                    <i class="fas fa-chevron-down panel-arrow"></i>
                </div>
                <div class="panel-body">
                    <button class="btn btn-sm" style="width:100%" onclick="randomBoxShadow()">Random Gölge Oluştur</button>
                    <br>
                    <div class="control-group">
                        <label class="control-label">X Offset</label>
                        <input type="range" id="shadowX" min="-50" max="50" value="0">
                    </div>
                    <div class="control-group">
                        <label class="control-label">Y Offset</label>
                        <input type="range" id="shadowY" min="-50" max="50" value="0">
                    </div>
                    <div class="control-group">
                        <label class="control-label">Blur</label>
                        <input type="range" id="shadowBlur" min="0" max="100" value="15">
                    </div>
                    <div class="control-group">
                        <label class="control-label">Renk</label>
                        <div class="color-wrap">
                            <div id="shadowColorPicker"></div>
                        </div>
                    </div>
                    <div class="control-group">
                        <label class="control-label" style="display:flex; align-items:center; gap:8px;">
                            <input type="checkbox" id="shadowInset"> İçe (Inset)
                        </label>
                    </div>
                </div>
            </div>

            <!-- 5. TRANSFORM -->
            <div class="panel" data-panel="transform">
                <div class="panel-header">
                    <div class="panel-info">
                        <div class="panel-icon" style="background:rgba(244,63,94,0.2); color:#f43f5e"><i class="fas fa-sync"></i></div>
                        <span class="panel-title">Dönüşüm</span>
                    </div>
                    <i class="fas fa-chevron-down panel-arrow"></i>
                </div>
                <div class="panel-body">
                    <div class="control-group">
                        <label class="control-label">Rotate <span class="badge" id="rotateVal">0deg</span></label>
                        <input type="range" id="rotateRange" min="-180" max="180" value="0">
                    </div>
                    <div class="control-group">
                        <label class="control-label">Scale <span class="badge" id="scaleVal">1</span></label>
                        <input type="range" id="scaleRange" min="0.5" max="3" step="0.1" value="1">
                    </div>
                    <button class="btn btn-sm" style="width:100%; margin-top:10px;" onclick="resetTransform()">Sıfırla</button>
                </div>
            </div>

            <!-- 6. CHAOS ENGINE -->
            <div class="panel" data-panel="chaos">
                <div class="panel-header">
                    <div class="panel-info">
                        <div class="panel-icon" style="background:rgba(249,115,22,0.2); color:#f97316"><i class="fas fa-bomb"></i></div>
                        <span class="panel-title">Kaos Motoru</span>
                    </div>
                    <i class="fas fa-chevron-down panel-arrow"></i>
                </div>
                <div class="panel-body">
                    <button class="btn btn-primary" style="width:100%; justify-content:center; font-weight:bold;" onclick="chaosMode()">
                        <i class="fas fa-magic"></i> TOTALE KAOS
                    </button>
                    <p style="font-size:11px; color:var(--text-muted); margin-top:8px; text-align:center;">
                        Rastgele font, renk, gölge ve dönüşüm uygular.
                    </p>
                </div>
            </div>

        </aside>

        <!-- MAIN PREVIEW AREA -->
        <main class="main-workspace">
            <div class="preview-card">
                <div id="preview-box">K3N4N STUDIO</div>
                
                <div class="preview-controls">
                    <button class="btn btn-sm btn-icon" id="refreshAnimBtn" title="Animasyonu Yenile"><i class="fas fa-play"></i></button>
                    <input type="text" id="customTextInput" value="K3N4N STUDIO" placeholder="Metni değiştir..." class="input-text" style="width: 200px; background: var(--bg-sidebar);">
                </div>
            </div>

            <div class="code-panel">
                <div class="code-tabs">
                    <div class="code-tab active" data-target="css-tab">CSS</div>
                    <div class="code-tab" data-target="html-tab">HTML + Inline</div>
                </div>
                <div class="code-content">
                    <textarea id="cssOutput" class="code-editor" readonly spellcheck="false"></textarea>
                </div>
                <div class="code-actions">
                    <button class="btn btn-sm" onclick="copyCode()"><i class="fas fa-copy"></i> Kopyala</button>
                    <button class="btn btn-sm" onclick="downloadCSS()"><i class="fas fa-download"></i> İndir</button>
                </div>
            </div>
        </main>
    </div>

    <!-- TOAST CONTAINER -->
    <div class="toast-container" id="toastContainer"></div>

    <script>
        (function() {
            'use strict';

            // --- STATE MANAGEMENT ---
            const $ = (id) => document.getElementById(id);
            const $$ = (sel) => document.querySelectorAll(sel);
            
            const previewBox = $('preview-box');
            const cssOutput = $('cssOutput');
            
            let history = [];
            let historyIndex = -1;
            const MAX_HISTORY = 50;

            // Current Styles Object
            let styles = {
                fontFamily: "'Inter', sans-serif",
                fontSize: '30px',
                fontWeight: '400',
                color: '#e6edf3',
                textAlign: 'center',
                textTransform: 'none',
                backgroundColor: 'rgba(0,0,0,0)', // Transparent initially
                backgroundImage: 'none',
                borderWidth: '0px',
                borderStyle: 'solid',
                borderColor: '#30363d',
                borderRadius: '0px',
                boxShadow: 'none',
                transform: 'none',
                padding: '20px 40px'
            };

            // --- COLOR PICKERS (IRO) ---
            const colorPickers = {};

            function initColorPicker(id, targetProp, textInputId) {
                if(!$(id)) return;
                const picker = new iro.ColorPicker($(id), {
                    width: 140,
                    color: styles[targetProp] || '#ffffff',
                    layout: [{ component: iro.ui.Slider, options: { sliderType: 'value' } }] // Simplified for modern look
                });
                
                colorPickers[targetProp] = picker;

                picker.on('color:change', function(color) {
                    const hex = color.hexString;
                    updateStyleDirect(targetProp, hex);
                    if(textInputId) $(textInputId).value = hex;
                });

                // Text input listener
                if(textInputId) {
                    $(textInputId).addEventListener('input', (e) => {
                        picker.color.hexString = e.target.value;
                    });
                }
            }

            // --- CORE FUNCTIONS ---

            function updateStyleDirect(prop, value, save = true) {
                if(styles[prop] === value) return;
                styles[prop] = value;
                applyStyles();
                if(save) saveHistory();
            }

            function updateStyle(prop, value) {
                // Special handling for shorthand
                if (prop === 'border') {
                    const width = $('borderWidth').value + 'px';
                    const style = $('borderStyle').value;
                    const color = $('borderColorPicker')._iro.color.hexString;
                    
                    styles.borderWidth = width;
                    styles.borderStyle = style;
                    styles.borderColor = color;
                } else {
                    styles[prop] = value;
                }
                applyStyles();
                saveHistory();
            }

            function updateBorder() {
                updateStyle('border');
            }

            function setRadius(val, isPercent = false) {
                styles.borderRadius = val + (isPercent ? '%' : 'px');
                $('borderRadiusRange').value = val; // Sync slider if val is number
                applyStyles();
                saveHistory();
            }

            function applyStyles() {
                // Apply to element
                for (const [key, value] of Object.entries(styles)) {
                    previewBox.style[key] = value;
                }

                // Update UI Inputs
                $('fontSizeRange').value = parseInt(styles.fontSize);
                $('fontSizeInput').value = parseInt(styles.fontSize);
                $('fontSizeBadge').textContent = styles.fontSize;
                
                $('fontWeightRange').value = styles.fontWeight;
                $('fontWeightVal').textContent = styles.fontWeight;

                $('borderRadiusRange').value = parseInt(styles.borderRadius) || 0;
                $('radiusBadge').textContent = styles.borderRadius;

                $('rotateVal').textContent = styles.transform.includes('rotate') ? 
                    styles.transform.match(/rotate\((.*?)\)/)[1] : '0deg';
                
                // Generate CSS Output Text
                generateCode();
            }

            function generateCode() {
                let css = `.my-element {\n`;
                for (const [key, value] of Object.entries(styles)) {
                    if(value !== 'none' && value !== 'normal' && value !== '') {
                        // Convert camelCase to kebab-case
                        const cssKey = key.replace(/([A-Z])/g, "-$1").toLowerCase();
                        css += `    ${cssKey}: ${value};\n`;
                    }
                }
                css += `}`;
                cssOutput.value = css;

                // Update HTML Tab content (stored in a variable or generated on tab click)
                const inlineStyle = css.replace('.my-element {', '').replace('}', '').trim().replace(/\n\s+/g, ' ');
                window._htmlOutput = `<div style="${inlineStyle}">${$('customTextInput').value}</div>`;
            }

            function saveHistory() {
                // Remove future history if we are in the middle
                history = history.slice(0, historyIndex + 1);
                history.push(JSON.parse(JSON.stringify(styles)));
                if(history.length > MAX_HISTORY) history.shift();
                historyIndex = history.length - 1;
                updateHistoryBtns();
            }

            function undo() {
                if(historyIndex > 0) {
                    historyIndex--;
                    styles = JSON.parse(JSON.stringify(history[historyIndex]));
                    applyStyles();
                    updateHistoryBtns();
                    showToast('Geri alındı');
                }
            }

            function redo() {
                if(historyIndex < history.length - 1) {
                    historyIndex++;
                    styles = JSON.parse(JSON.stringify(history[historyIndex]));
                    applyStyles();
                    updateHistoryBtns();
                    showToast('İleri alındı');
                }
            }

            function updateHistoryBtns() {
                $('btnUndo').disabled = historyIndex <= 0;
                $('btnRedo').disabled = historyIndex >= history.length - 1;
                $('btnUndo').style.opacity = historyIndex <= 0 ? 0.5 : 1;
                $('btnRedo').style.opacity = historyIndex >= history.length - 1 ? 0.5 : 1;
            }

            // --- RANDOMIZERS ---

            function rndInt(min, max) { return Math.floor(Math.random() * (max - min + 1)) + min; }
            function rndColor() { return '#' + Math.floor(Math.random()*16777215).toString(16).padStart(6,'0'); }
            
            function randomFont() {
                const fonts = ["'Inter', sans-serif", "'Space Grotesk', sans-serif", "'JetBrains Mono', monospace", "cursive", "serif"];
                styles.fontFamily = fonts[rndInt(0, fonts.length-1)];
                styles.fontSize = rndInt(20, 60) + 'px';
                styles.fontWeight = [300, 400, 700, 900][rndInt(0,3)];
                styles.color = rndColor();
                applyStyles();
                saveHistory();
                showToast('Font Randomize Edildi');
            }

            function randomColor() {
                const color = rndColor();
                colorPickers.color.color.hexString = color;
                $('textColorText').value = color;
            }

            function randomBgColor() {
                const color = rndColor();
                styles.backgroundImage = 'none';
                colorPickers.backgroundColor.color.hexString = color;
                $('bgColorText').value = color;
            }

            function randomGradient() {
                const c1 = rndColor();
                const c2 = rndColor();
                const angle = rndInt(0, 360);
                styles.backgroundImage = `linear-gradient(${angle}deg, ${c1}, ${c2})`;
                applyStyles();
                saveHistory();
                showToast('Gradient Oluşturuldu');
            }

            function randomBoxShadow() {
                const x = rndInt(-20, 20);
                const y = rndInt(-20, 20);
                const blur = rndInt(10, 50);
                const color = Math.random() > 0.5 ? 'rgba(0,0,0,0.5)' : rndColor();
                styles.boxShadow = `${x}px ${y}px ${blur}px ${color}`;
                
                // Update UI inputs roughly
                $('shadowX').value = x;
                $('shadowY').value = y;
                $('shadowBlur').value = blur;
                // Note: Updating color picker hex from rgba is tricky, skipping UI full sync for chaos mode
                
                applyStyles();
                saveHistory();
                showToast('Gölge Oluşturuldu');
            }

            function chaosMode() {
                randomFont();
                Math.random() > 0.5 ? randomGradient() : randomBgColor();
                randomBoxShadow();
                styles.transform = `rotate(${rndInt(-10,10)}deg) scale(${(Math.random()*0.5 + 0.8).toFixed(1)})`;
                styles.borderRadius = rndInt(0, 30) + 'px';
                applyStyles();
                saveHistory();
                showToast('⚡ KAOS MODU! ⚡', 'warn');
            }

            function resetTransform() {
                $('rotateRange').value = 0;
                $('scaleRange').value = 1;
                styles.transform = 'none';
                applyStyles();
                saveHistory();
            }

            // --- TRANSFORM LISTENERS ---
            function updateTransform() {
                const r = $('rotateRange').value;
                const s = $('scaleRange').value;
                styles.transform = `rotate(${r}deg) scale(${s})`;
                applyStyles(); // Don't save history on every slide, could optimize
            }
            
            // Debounce save for sliders to avoid spamming history
            let timeout;
            function debounceSave() {
                clearTimeout(timeout);
                timeout = setTimeout(saveHistory, 500);
            }

            // --- UTILS ---
            function showToast(msg, type='info') {
                const toast = document.createElement('div');
                toast.className = 'toast';
                const icon = type === 'warn' ? 'fa-magic' : 'fa-info-circle';
                toast.innerHTML = `<i class="fas ${icon}"></i> <span>${msg}</span>`;
                $('toastContainer').appendChild(toast);
                setTimeout(() => toast.remove(), 3000);
            }

            function copyCode() {
                navigator.clipboard.writeText(cssOutput.value).then(() => {
                    showToast('CSS Kopyalandı!');
                });
            }

            function downloadCSS() {
                const blob = new Blob([cssOutput.value], {type: 'text/css'});
                const url = URL.createObjectURL(blob);
                const a = document.createElement('a');
                a.href = url; a.download = 'style.css'; a.click();
                URL.revokeObjectURL(url);
            }

            // --- EVENT BINDING ---

            // Accordion
            $$('.panel-header').forEach(h => {
                h.addEventListener('click', () => {
                    h.parentElement.classList.toggle('expanded');
                });
            });

            // Tabs
            $$('.code-tab').forEach(t => {
                t.addEventListener('click', () => {
                    $$('.code-tab').forEach(x => x.classList.remove('active'));
                    t.classList.add('active');
                    const target = t.dataset.target;
                    if(target === 'html-tab') {
                        cssOutput.value = window._htmlOutput || '';
                    } else {
                        generateCode();
                    }
                });
            });

            // Input & Range Listeners
            $('fontFamily').addEventListener('change', (e) => updateStyleDirect('fontFamily', e.target.value));
            $('textTransform').addEventListener('change', (e) => updateStyleDirect('textTransform', e.target.value));
            
            // Font Size sync
            const updateFontSize = (v) => {
                updateStyleDirect('fontSize', v + 'px');
                $('fontSizeRange').value = v;
                $('fontSizeInput').value = v;
                $('fontSizeBadge').innerText = v + 'px';
            };
            $('fontSizeRange').addEventListener('input', (e) => { updateFontSize(e.target.value); debounceSave(); });
            $('fontSizeInput').addEventListener('input', (e) => { updateFontSize(e.target.value); debounceSave(); });

            // Font Weight
            $('fontWeightRange').addEventListener('input', (e) => {
                updateStyleDirect('fontWeight', e.target.value);
                $('fontWeightVal').innerText = e.target.value;
                debounceSave();
            });

            // Radius
            $('borderRadiusRange').addEventListener('input', (e) => {
                setRadius(e.target.value);
                debounceSave();
            });

            // Transform
            $('rotateRange').addEventListener('input', (e) => { updateTransform(); debounceSave(); });
            $('scaleRange').addEventListener('input', (e) => { updateTransform(); debounceSave(); });

            // Shadows
            const updateShadow = () => {
                const inset = $('shadowInset').checked ? 'inset ' : '';
                styles.boxShadow = `${inset}${$('shadowX').value}px ${$('shadowY').value}px ${$('shadowBlur').value}px ${colorPickers.boxShadowColor ? colorPickers.boxShadowColor.color.hexString : '#000'}`;
                applyStyles();
                debounceSave();
            };
            ['shadowX', 'shadowY', 'shadowBlur', 'shadowInset'].forEach(id => $(id).addEventListener('input', updateShadow));

            // Bg Image
            $('bgImageUrl').addEventListener('input', (e) => {
                styles.backgroundImage = e.target.value ? `url('${e.target.value}')` : 'none';
                applyStyles();
                saveHistory();
            });

            // Custom Text
            $('customTextInput').addEventListener('input', (e) => {
                previewBox.innerText = e.target.value;
                generateCode(); // Live update HTML output
            });

            // Header Actions
            $('btnUndo').addEventListener('click', undo);
            $('btnRedo').addEventListener('click', redo);
            $('btnReset').addEventListener('click', () => {
                if(confirm('Tüm stilleri sıfırlamak istediğine emin misin?')) {
                    location.reload();
                }
            });

            // Mobile Toggle
            $('menuToggle').addEventListener('click', () => {
                $('sidebar').classList.toggle('active');
                $('sidebarOverlay').classList.toggle('active');
            });
            $('sidebarOverlay').addEventListener('click', () => {
                $('sidebar').classList.remove('active');
                $('sidebarOverlay').classList.remove('active');
            });

            // Search Filter
            $('panelSearch').addEventListener('input', (e) => {
                const val = e.target.value.toLowerCase();
                $$('.panel').forEach(p => {
                    const txt = p.innerText.toLowerCase();
                    p.style.display = txt.includes(val) ? 'block' : 'none';
                });
            });

            // Keyboard Shortcuts
            document.addEventListener('keydown', (e) => {
                if((e.ctrlKey || e.metaKey) && e.key === 'z') { e.preventDefault(); undo(); }
                if((e.ctrlKey || e.metaKey) && e.key === 'y') { e.preventDefault(); redo(); }
                if((e.ctrlKey || e.metaKey) && e.key === 's') { e.preventDefault(); copyCode(); }
            });

            // --- INIT ---
            initColorPicker('textColorPicker', 'color', 'textColorText');
            initColorPicker('bgColorPicker', 'backgroundColor', 'bgColorText');
            initColorPicker('borderColorPicker', 'borderColor', null);
            initColorPicker('shadowColorPicker', 'boxShadowColor', null); // Used in updateShadow logic manually

            // Initial Apply
            saveHistory(); // Save initial state
            applyStyles();

            console.log('%c K3N4N STUDIO V7.0 READY ', 'background:#222; color:#bada55; font-size:16px; padding:5px; border-radius:4px;');

        })();
    </script>
</body>
</html>
```

## Prompt 2

### You
*2026-02-07 18:47:43 +03*

yazdıgın kodun tam olarak kaldıgı yerden yaz devam et height: 'auto', dan  baslayarak devam et

### Claude Opus 4.6
*2026-02-07 18:47:43 +03*



Kaldığı yerden devam ediyorum — `height: 'auto',` satırından itibaren:

```javascript
                height: 'auto',
                minWidth: 'auto',
                maxWidth: 'auto',
                minHeight: '280px',
                maxHeight: 'auto',
                overflow: 'hidden',
                display: 'flex',
                flexDirection: 'row',
                justifyContent: 'center',
                alignItems: 'center',
                gap: '0px',
                transition: 'none'
            };
        }

        // ===== TOAST =====
        function showToast(message, type = 'success') {
            const toast = document.createElement('div');
            toast.className = `toast ${type}`;
            toast.innerHTML = `<i class="fas fa-${type === 'success' ? 'check-circle' : type === 'error' ? 'exclamation-circle' : 'info-circle'}"></i> ${message}`;
            toastContainer.appendChild(toast);
            setTimeout(() => {
                toast.style.opacity = '0';
                toast.style.transform = 'translateX(40px) scale(0.95)';
                toast.style.transition = 'all 0.3s ease';
                setTimeout(() => toast.remove(), 300);
            }, 2700);
        }

        // ===== COLOR PICKERS =====
        const pickers = {};
        const pickerConfigs = [
            { id: 'textColorPicker', key: 'textColor', default: '#222222', onChange: c => updateStyle('color', c.hexString) },
            { id: 'textShadowColorPicker', key: 'textShadowColor', default: '#000000', onChange: c => updateComplexStyle('textShadowColor', c.hexString) },
            { id: 'backgroundColorPicker', key: 'bgColor', default: '#ffffff', onChange: c => updateStyle('backgroundColor', c.hexString) },
            { id: 'outlineColorPicker', key: 'outlineColor', default: '#ffffff', onChange: c => updateComplexStyle('outlineColor', c.hexString) },
            { id: 'boxShadowColorPicker', key: 'boxShadowColor', default: '#000000', onChange: c => updateComplexStyle('boxShadowColor', c.hexString) },
            { id: 'baseColorPicker', key: 'baseColor', default: '#64ffda', onChange: () => generatePalette() }
        ];

        pickerConfigs.forEach(cfg => {
            const el = $(cfg.id);
            if (!el) return;
            pickers[cfg.key] = new iro.ColorPicker(el, {
                width: 140,
                color: cfg.default,
                borderWidth: 1,
                borderColor: 'rgba(255,255,255,0.15)',
                layoutDirection: 'horizontal',
                layout: [
                    { component: iro.ui.Wheel, options: { wheelLightness: true } },
                    { component: iro.ui.Slider, options: { sliderType: 'value' } }
                ]
            });
            pickers[cfg.key].on('color:change', cfg.onChange);
        });

        // ===== GRADIENT COLORS =====
        let gradientColors = [{ color: '#64ffda', stop: 0 }, { color: '#c084fc', stop: 100 }];
        let textGradientColors = [{ color: '#64ffda', stop: 0 }, { color: '#ff6b9d', stop: 100 }];

        function initGradientPickers(container, colors, type) {
            const el = $(container);
            if (!el) return;
            el.innerHTML = '';
            colors.forEach((gc, i) => {
                const row = document.createElement('div');
                row.className = 'gradient-color-row';

                const colorInput = document.createElement('input');
                colorInput.type = 'color';
                colorInput.value = gc.color;
                colorInput.style.cssText = 'width:40px;height:28px;border:1px solid var(--border-color);border-radius:4px;cursor:pointer;background:var(--bg-dark);padding:1px;flex-shrink:0;';
                colorInput.addEventListener('input', e => {
                    colors[i].color = e.target.value;
                    type === 'bg' ? updateGradient() : updateTextGradient();
                });

                const stopInput = document.createElement('input');
                stopInput.type = 'number';
                stopInput.value = gc.stop;
                stopInput.min = 0;
                stopInput.max = 100;
                stopInput.style.cssText = 'width:55px;padding:5px 6px;background:var(--bg-dark);border:1px solid var(--border-color);border-radius:4px;color:var(--text-white);font-size:11px;text-align:center;outline:none;font-family:"JetBrains Mono",monospace;';
                stopInput.addEventListener('input', e => {
                    colors[i].stop = parseInt(e.target.value) || 0;
                    type === 'bg' ? updateGradient() : updateTextGradient();
                });
                stopInput.addEventListener('focus', function() {
                    this.style.borderColor = 'var(--accent-primary)';
                });
                stopInput.addEventListener('blur', function() {
                    this.style.borderColor = 'var(--border-color)';
                });

                const removeBtn = document.createElement('button');
                removeBtn.innerHTML = '<i class="fas fa-trash"></i>';
                removeBtn.addEventListener('click', () => {
                    if (colors.length > 1) {
                        colors.splice(i, 1);
                        initGradientPickers(container, colors, type);
                        type === 'bg' ? updateGradient() : updateTextGradient();
                    }
                });

                row.appendChild(colorInput);
                row.appendChild(stopInput);
                row.appendChild(removeBtn);
                el.appendChild(row);
            });
        }

        if ($('addGradientColor')) {
            $('addGradientColor').addEventListener('click', () => {
                gradientColors.push({ color: '#' + Math.floor(Math.random()*16777215).toString(16).padStart(6,'0'), stop: 100 });
                initGradientPickers('gradientColors', gradientColors, 'bg');
                updateGradient();
            });
        }

        if ($('addTextGradientColor')) {
            $('addTextGradientColor').addEventListener('click', () => {
                textGradientColors.push({ color: '#' + Math.floor(Math.random()*16777215).toString(16).padStart(6,'0'), stop: 100 });
                initGradientPickers('textGradientColors', textGradientColors, 'text');
                updateTextGradient();
            });
        }

        // ===== CORE FUNCTIONS =====
        function updateStyle(property, value, unit = '') {
            const finalVal = unit ? `${value}${unit}` : value;
            if (currentStyles[property] !== finalVal) {
                currentStyles[property] = finalVal;
                applyStyles();
                saveToHistory();
            }
        }

        function updateComplexStyle(property, value) {
            if (property === 'textShadowColor') {
                const x = $('textShadowX').value || 0;
                const y = $('textShadowY').value || 0;
                const blur = $('textShadowBlur').value || 0;
                currentStyles.textShadow = `${x}px ${y}px ${blur}px ${value}`;
            } else if (property === 'boxShadowColor') {
                const x = $('boxShadowX').value || 0;
                const y = $('boxShadowY').value || 0;
                const blur = $('boxShadowBlur').value || 0;
                const spread = $('boxShadowSpread').value || 0;
                const inset = $('boxShadowInset').checked ? 'inset ' : '';
                currentStyles.boxShadow = `${inset}${x}px ${y}px ${blur}px ${spread}px ${value}`;
            } else if (property === 'outlineColor') {
                currentStyles.outlineWidth = `${$('outlineWidth').value || 0}px`;
                currentStyles.outlineStyle = $('outlineStyle').value;
                currentStyles.outlineColor = value;
            }
            applyStyles();
            saveToHistory();
        }

        function updateGradient() {
            const type = $('gradientType').value;
            const angle = $('gradientAngle').value;
            const stops = gradientColors.map(gc => `${gc.color} ${gc.stop}%`).join(', ');
            let gradient;
            if (type === 'linear') gradient = `linear-gradient(${angle}deg, ${stops})`;
            else if (type === 'radial') gradient = `radial-gradient(circle, ${stops})`;
            else gradient = `conic-gradient(from ${angle}deg, ${stops})`;
            currentStyles.backgroundImage = gradient;
            currentStyles.webkitBackgroundClip = '';
            currentStyles.webkitTextFillColor = '';
            currentStyles.backgroundClip = 'border-box';
            applyStyles();
            saveToHistory();
        }

        function updateTextGradient() {
            const type = $('textGradientType').value;
            const angle = $('textGradientAngle').value;
            const stops = textGradientColors.map(gc => `${gc.color} ${gc.stop}%`).join(', ');
            let gradient;
            if (type === 'linear') gradient = `linear-gradient(${angle}deg, ${stops})`;
            else gradient = `radial-gradient(circle, ${stops})`;
            currentStyles.backgroundImage = gradient;
            currentStyles.webkitBackgroundClip = 'text';
            currentStyles.backgroundClip = 'text';
            currentStyles.webkitTextFillColor = 'transparent';
            applyStyles();
            saveToHistory();
        }

        function updateTextImageFill() {
            const url = $('textImageFill').value.trim();
            if (url) {
                currentStyles.backgroundImage = `url(${url})`;
                currentStyles.backgroundSize = 'cover';
                currentStyles.webkitBackgroundClip = 'text';
                currentStyles.backgroundClip = 'text';
                currentStyles.webkitTextFillColor = 'transparent';
            } else {
                currentStyles.backgroundImage = 'none';
                currentStyles.webkitBackgroundClip = '';
                currentStyles.backgroundClip = 'border-box';
                currentStyles.webkitTextFillColor = '';
            }
            applyStyles();
            saveToHistory();
        }

        function updateBackgroundImageUrl() {
            const url = $('backgroundImageUrl').value.trim();
            if (url) {
                currentStyles.backgroundImage = `url(${url})`;
                currentStyles.webkitBackgroundClip = '';
                currentStyles.webkitTextFillColor = '';
                currentStyles.backgroundClip = 'border-box';
            } else {
                currentStyles.backgroundImage = 'none';
            }
            applyStyles();
            saveToHistory();
        }

        function updateFilter() {
            const blur = $('filterBlurRange').value;
            const brightness = $('filterBrightnessRange').value;
            const contrast = $('filterContrastRange').value;
            const saturate = $('filterSaturateRange').value;
            const hueRotate = $('filterHueRotateRange').value;
            const invert = $('filterInvertRange').value;
            const sepia = $('filterSepiaRange').value;
            const grayscale = $('filterGrayscaleRange').value;
            let parts = [];
            if (parseFloat(blur) > 0) parts.push(`blur(${blur}px)`);
            if (parseFloat(brightness) !== 100) parts.push(`brightness(${brightness}%)`);
            if (parseFloat(contrast) !== 100) parts.push(`contrast(${contrast}%)`);
            if (parseFloat(saturate) !== 100) parts.push(`saturate(${saturate}%)`);
            if (parseFloat(hueRotate) > 0) parts.push(`hue-rotate(${hueRotate}deg)`);
            if (parseFloat(invert) > 0) parts.push(`invert(${invert}%)`);
            if (parseFloat(sepia) > 0) parts.push(`sepia(${sepia}%)`);
            if (parseFloat(grayscale) > 0) parts.push(`grayscale(${grayscale}%)`);
            currentStyles.filter = parts.length ? parts.join(' ') : 'none';

            const backdropBlur = $('backdropBlurRange').value;
            currentStyles.backdropFilter = parseFloat(backdropBlur) > 0 ? `blur(${backdropBlur}px)` : 'none';

            $('blurVal').textContent = blur + 'px';
            $('brightnessVal').textContent = brightness + '%';
            $('contrastVal').textContent = contrast + '%';
            $('saturateVal').textContent = saturate + '%';
            $('hueRotateVal').textContent = hueRotate + '°';
            $('invertVal').textContent = invert + '%';
            $('sepiaVal').textContent = sepia + '%';
            $('grayscaleVal').textContent = grayscale + '%';

            applyStyles();
            saveToHistory();
        }

        function updatePadding() {
            const unit = $('paddingUnit').value;
            currentStyles.paddingLeft = ($('paddingLeft').value || 0) + unit;
            currentStyles.paddingRight = ($('paddingRight').value || 0) + unit;
            currentStyles.paddingTop = ($('paddingTop').value || 0) + unit;
            currentStyles.paddingBottom = ($('paddingBottom').value || 0) + unit;
            applyStyles();
            saveToHistory();
        }

        function updateTransform() {
            const rotate = $('rotate') ? $('rotate').value : ($('rotateRange') ? $('rotateRange').value : 0);
            const scale = $('scaleRange').value;
            const skewX = $('skewX').value || 0;
            const skewY = $('skewY').value || 0;
            const translateX = $('translateX').value || 0;
            const translateY = $('translateY').value || 0;
            let parts = [];
            if (parseFloat(rotate) !== 0) parts.push(`rotate(${rotate}deg)`);
            if (parseFloat(scale) !== 1) parts.push(`scale(${scale})`);
            if (parseFloat(skewX) !== 0) parts.push(`skewX(${skewX}deg)`);
            if (parseFloat(skewY) !== 0) parts.push(`skewY(${skewY}deg)`);
            if (parseFloat(translateX) !== 0) parts.push(`translateX(${translateX}px)`);
            if (parseFloat(translateY) !== 0) parts.push(`translateY(${translateY}px)`);
            currentStyles.transform = parts.length ? parts.join(' ') : 'none';

            if ($('rotateVal')) $('rotateVal').textContent = rotate + '°';
            if ($('scaleVal')) $('scaleVal').textContent = scale;

            applyStyles();
            saveToHistory();
        }

        function updateBoxShadow() {
            const x = $('boxShadowX').value || 0;
            const y = $('boxShadowY').value || 0;
            const blur = $('boxShadowBlur').value || 0;
            const spread = $('boxShadowSpread').value || 0;
            const inset = $('boxShadowInset').checked ? 'inset ' : '';
            const color = pickers.boxShadowColor ? pickers.boxShadowColor.color.hexString : '#000000';
            currentStyles.boxShadow = `${inset}${x}px ${y}px ${blur}px ${spread}px ${color}`;
            applyStyles();
            saveToHistory();
        }

        function updateTransition() {
            const prop = $('transitionProperty').value;
            const dur = $('transitionDuration').value;
            currentStyles.transition = `${prop} ${dur}s ease`;
            applyStyles();
            saveToHistory();
        }

        // ===== APPLY STYLES =====
        function applyStyles() {
            Object.keys(currentStyles).forEach(prop => {
                const val = currentStyles[prop];
                if (val === '' || val === undefined || val === null) return;

                if (prop === 'webkitTextFillColor') {
                    previewBox.style.setProperty('-webkit-text-fill-color', val);
                } else if (prop === 'webkitBackgroundClip') {
                    previewBox.style.setProperty('-webkit-background-clip', val);
                } else {
                    try { previewBox.style[prop] = val; } catch(e) {}
                }
            });

            updateCssOutput();
            updateHtmlPreview();
            updatePreviewDimensions();
        }

        function camelToKebab(str) {
            return str.replace(/[A-Z]/g, m => `-${m.toLowerCase()}`);
        }

        function updateCssOutput() {
            const lines = [];
            Object.entries(currentStyles).forEach(([key, value]) => {
                if (value === '' || value === undefined || value === null) return;
                let cssProp;
                if (key === 'webkitTextFillColor') cssProp = '-webkit-text-fill-color';
                else if (key === 'webkitBackgroundClip') cssProp = '-webkit-background-clip';
                else cssProp = camelToKebab(key);
                lines.push(`    ${cssProp}: ${value};`);
            });
            cssOutput.value = `.my-element {\n${lines.join('\n')}\n}`;
        }

        function updateHtmlPreview() {
            const text = customTextInput.value || 'K3N4N V6.0';
            const inlineStyles = [];
            Object.entries(currentStyles).forEach(([key, value]) => {
                if (value === '' || value === undefined || value === null) return;
                let cssProp;
                if (key === 'webkitTextFillColor') cssProp = '-webkit-text-fill-color';
                else if (key === 'webkitBackgroundClip') cssProp = '-webkit-background-clip';
                else cssProp = camelToKebab(key);
                inlineStyles.push(`${cssProp}: ${value}`);
            });
            if (htmlPreviewArea) {
                htmlPreviewArea.textContent = `<div style="${inlineStyles.join('; ')}">\n  ${text}\n</div>`;
            }
        }

        function updatePreviewDimensions() {
            const rect = previewBox.getBoundingClientRect();
            const el = $('previewDimensions');
            if (el) el.textContent = `${Math.round(rect.width)} × ${Math.round(rect.height)}`;
        }

        // ===== HISTORY =====
        function saveToHistory() {
            history = history.slice(0, historyIndex + 1);
            history.push(JSON.parse(JSON.stringify(currentStyles)));
            if (history.length > MAX_HISTORY) history.shift();
            historyIndex = history.length - 1;
            updateHistoryButtons();
        }

        function updateHistoryButtons() {
            const undoBtn = document.querySelector('[data-action="undo"]');
            const redoBtn = document.querySelector('[data-action="redo"]');
            if (undoBtn) undoBtn.disabled = historyIndex <= 0;
            if (redoBtn) redoBtn.disabled = historyIndex >= history.length - 1;
        }

        function undo() {
            if (historyIndex > 0) {
                historyIndex--;
                currentStyles = JSON.parse(JSON.stringify(history[historyIndex]));
                applyStyles();
                updateHistoryButtons();
                showToast('Geri alındı', 'info');
            }
        }

        function redo() {
            if (historyIndex < history.length - 1) {
                historyIndex++;
                currentStyles = JSON.parse(JSON.stringify(history[historyIndex]));
                applyStyles();
                updateHistoryButtons();
                showToast('İleri alındı', 'info');
            }
        }

        // ===== RANDOM GENERATORS =====
        function rndHex() {
            return '#' + Math.floor(Math.random() * 16777215).toString(16).padStart(6, '0');
        }

        function rndInt(min, max) {
            return Math.floor(Math.random() * (max - min + 1)) + min;
        }

        function rndFloat(min, max, dec = 1) {
            return parseFloat((Math.random() * (max - min) + min).toFixed(dec));
        }

        function rndItem(arr) {
            return arr[Math.floor(Math.random() * arr.length)];
        }

        const allFonts = [
            "'Poppins', sans-serif", "'Inter', sans-serif", "'Space Grotesk', sans-serif",
            "'VT323', monospace", "'Press Start 2P', monospace", "'Orbitron', sans-serif",
            "'Roboto Mono', monospace", "'JetBrains Mono', monospace", "'Lobster', cursive",
            "'Kaushan Script', cursive", "'Fira Code', monospace", "Georgia, serif",
            "'Courier New', monospace", "Impact, sans-serif"
        ];

        function randomFont() {
            updateStyle('fontFamily', rndItem(allFonts));
            updateStyle('fontSize', rndItem([16, 20, 24, 28, 30, 36, 42, 48, 56, 64]) + 'px');
            updateStyle('fontWeight', rndItem(['300', '400', '500', '600', '700', '800', '900']));
            showToast('Yazı tipi randomlandı');
        }

        function randomColor() {
            updateStyle('color', rndHex());
            showToast('Yazı rengi değişti');
        }

        function randomTextShadow() {
            const count = rndInt(1, 3);
            let shadows = [];
            for (let i = 0; i < count; i++) {
                shadows.push(`${rndInt(-8, 8)}px ${rndInt(-8, 8)}px ${rndInt(0, 15)}px ${rndHex()}`);
            }
            currentStyles.textShadow = shadows.join(', ');
            applyStyles();
            saveToHistory();
            showToast('Yazı gölgesi oluşturuldu');
        }

        function randomTextDecoration() {
            updateStyle('textDecorationLine', rndItem(['none', 'underline', 'overline', 'line-through']));
            updateStyle('textDecorationStyle', rndItem(['solid', 'double', 'dotted', 'dashed', 'wavy']));
        }

        function randomSpacing() {
            updateStyle('letterSpacing', rndFloat(-2, 8) + 'px');
            updateStyle('wordSpacing', rndFloat(-2, 10) + 'px');
        }

        function randomAlign() {
            updateStyle('textAlign', rndItem(['left', 'center', 'right', 'justify']));
        }

        function randomLineHeight() {
            const val = rndFloat(0.8, 3.0);
            currentStyles.lineHeight = val.toString();
            if ($('lineHeightRange')) $('lineHeightRange').value = val;
            if ($('lineHeightVal')) $('lineHeightVal').textContent = val;
            applyStyles();
            saveToHistory();
        }

        function randomTextTransform() {
            updateStyle('textTransform', rndItem(['none', 'uppercase', 'lowercase', 'capitalize']));
        }

        function randomBgColor() {
            updateStyle('backgroundColor', rndHex());
            currentStyles.backgroundImage = 'none';
            currentStyles.webkitBackgroundClip = '';
            currentStyles.webkitTextFillColor = '';
            currentStyles.backgroundClip = 'border-box';
            applyStyles();
            saveToHistory();
            showToast('Arka plan rengi değişti');
        }

        function randomGradient() {
            const count = rndInt(2, 4);
            gradientColors = [];
            for (let i = 0; i < count; i++) {
                gradientColors.push({ color: rndHex(), stop: Math.round(i / (count - 1) * 100) });
            }
            $('gradientAngle').value = rndInt(0, 360);
            $('gradientType').value = rndItem(['linear', 'radial', 'conic']);
            initGradientPickers('gradientColors', gradientColors, 'bg');
            updateGradient();
            showToast('Gradyan oluşturuldu');
        }

        function randomBgGif() {
            const gifs = [
                'https://media.giphy.com/media/l0MYt5jPR6QX5pnqM/giphy.gif',
                'https://media.giphy.com/media/3o7btPCcdNniyf0ArS/giphy.gif',
                'https://media.giphy.com/media/xT9IgzoKnwFNmISR8I/giphy.gif',
                'https://media.giphy.com/media/26tn33aiTi1jkl6H6/giphy.gif',
                'https://media.giphy.com/media/l378p60yRSCeVrd5e/giphy.gif'
            ];
            currentStyles.backgroundImage = `url(${rndItem(gifs)})`;
            currentStyles.backgroundSize = 'cover';
            currentStyles.webkitBackgroundClip = '';
            currentStyles.webkitTextFillColor = '';
            currentStyles.backgroundClip = 'border-box';
            applyStyles();
            saveToHistory();
            showToast('GIF arka plan uygulandı');
        }

        function randomBgPosition() {
            const positions = ['center', 'top', 'bottom', 'left', 'right', '25%', '75%'];
            updateStyle('backgroundPositionX', rndItem(positions));
            updateStyle('backgroundPositionY', rndItem(positions));
        }

        function randomBgSize() {
            updateStyle('backgroundSize', rndItem(['auto', 'cover', 'contain', '100% 100%', '50% 50%', '200px 200px']));
        }

        function randomBgOpacity() {
            const val = rndFloat(0.2, 1.0);
            currentStyles.opacity = val.toString();
            if ($('backgroundOpacityRange')) $('backgroundOpacityRange').value = val;
            if ($('bgOpacityVal')) $('bgOpacityVal').textContent = val;
            applyStyles();
            saveToHistory();
        }

        function randomBgPattern() {
            const patterns = [
                `repeating-linear-gradient(45deg, transparent, transparent 10px, ${rndHex()} 10px, ${rndHex()} 20px)`,
                `repeating-radial-gradient(circle at 50% 50%, ${rndHex()}, ${rndHex()} 10px, ${rndHex()} 20px)`,
                `linear-gradient(45deg, ${rndHex()} 25%, transparent 25%), linear-gradient(-45deg, ${rndHex()} 25%, transparent 25%), linear-gradient(45deg, transparent 75%, ${rndHex()} 75%), linear-gradient(-45deg, transparent 75%, ${rndHex()} 75%)`,
                `radial-gradient(circle at 25% 25%, ${rndHex()} 2px, transparent 3px), radial-gradient(circle at 75% 75%, ${rndHex()} 2px, transparent 3px)`
            ];
            currentStyles.backgroundImage = rndItem(patterns);
            currentStyles.webkitBackgroundClip = '';
            currentStyles.webkitTextFillColor = '';
            currentStyles.backgroundClip = 'border-box';
            applyStyles();
            saveToHistory();
            showToast('Desen oluşturuldu');
        }

        function randomBgBlend() {
            updateStyle('backgroundBlendMode', rndItem(['multiply', 'screen', 'overlay', 'darken', 'lighten', 'color-dodge', 'difference', 'hue', 'saturation']));
        }

        function randomMultiBorder() {
            const styles = ['solid', 'dashed', 'dotted', 'double', 'groove', 'ridge'];
            ['borderTop', 'borderBottom', 'borderLeft', 'borderRight'].forEach(side => {
                currentStyles[side] = `${rndInt(1, 6)}px ${rndItem(styles)} ${rndHex()}`;
            });
            applyStyles();
            saveToHistory();
            showToast('Çerçeve oluşturuldu');
        }

        function randomBorderColor() {
            const color = rndHex();
            ['borderTop', 'borderBottom', 'borderLeft', 'borderRight'].forEach(side => {
                const parts = (currentStyles[side] || '').split(' ');
                if (parts.length >= 2) {
                    currentStyles[side] = `${parts[0]} ${parts[1]} ${color}`;
                }
            });
            applyStyles();
            saveToHistory();
        }

        function randomOutline() {
            currentStyles.outlineWidth = `${rndInt(1, 5)}px`;
            currentStyles.outlineStyle = rndItem(['solid', 'dashed', 'dotted', 'double', 'groove', 'ridge']);
            currentStyles.outlineColor = rndHex();
            currentStyles.outlineOffset = `${rndInt(0, 8)}px`;
            applyStyles();
            saveToHistory();
        }

        function randomBorderRadius() {
            const mode = rndItem(['uniform', 'crazy']);
            if (mode === 'uniform') {
                const r = rndInt(0, 50);
                ['borderTopLeftRadius', 'borderTopRightRadius', 'borderBottomLeftRadius', 'borderBottomRightRadius'].forEach(p => {
                    currentStyles[p] = r + 'px';
                });
                if ($('borderRadiusAll')) $('borderRadiusAll').value = r;
                if ($('borderRadiusVal')) $('borderRadiusVal').textContent = r + 'px';
            } else {
                ['borderTopLeftRadius', 'borderTopRightRadius', 'borderBottomLeftRadius', 'borderBottomRightRadius'].forEach(p => {
                    currentStyles[p] = rndInt(0, 80) + 'px';
                });
            }
            applyStyles();
            saveToHistory();
            showToast('Kenar yuvarlatması oluşturuldu');
        }

        function randomTransform() {
            if ($('rotateRange')) $('rotateRange').value = rndInt(-30, 30);
            if ($('rotate')) $('rotate').value = $('rotateRange').value;
            if ($('scaleRange')) $('scaleRange').value = rndFloat(0.7, 1.5);
            if ($('skewX')) $('skewX').value = rndInt(-15, 15);
            if ($('skewY')) $('skewY').value = rndInt(-15, 15);
            if ($('translateX')) $('translateX').value = rndInt(-20, 20);
            if ($('translateY')) $('translateY').value = rndInt(-20, 20);
            updateTransform();
            showToast('Dönüşüm oluşturuldu');
        }

        function randomBoxShadow() {
            const count = rndInt(1, 3);
            let shadows = [];
            for (let i = 0; i < count; i++) {
                const inset = Math.random() > 0.7 ? 'inset ' : '';
                shadows.push(`${inset}${rndInt(-10, 10)}px ${rndInt(-10, 10)}px ${rndInt(5, 30)}px ${rndInt(-5, 10)}px ${rndHex()}`);
            }
            currentStyles.boxShadow = shadows.join(', ');
            applyStyles();
            saveToHistory();
            showToast('Kutu gölgesi oluşturuldu');
        }

        function randomBoxShadowColor() {
            const color = rndHex();
            currentStyles.boxShadow = (currentStyles.boxShadow || '').replace(/#[0-9a-fA-F]{3,8}/g, color);
            applyStyles();
            saveToHistory();
        }

        function randomMultiShadow() {
            let shadows = [];
            const count = rndInt(2, 5);
            for (let i = 0; i < count; i++) {
                shadows.push(`${rndInt(-15, 15)}px ${rndInt(-15, 15)}px ${rndInt(5, 40)}px ${rndInt(-5, 10)}px ${rndHex()}`);
            }
            currentStyles.boxShadow = shadows.join(', ');
            applyStyles();
            saveToHistory();
            showToast('Çoklu gölge oluşturuldu');
        }

        function randomInsetShadow() {
            currentStyles.boxShadow = `inset ${rndInt(-10, 10)}px ${rndInt(-10, 10)}px ${rndInt(10, 40)}px ${rndInt(0, 10)}px ${rndHex()}`;
            applyStyles();
            saveToHistory();
            showToast('İç gölge oluşturuldu');
        }

        // ===== ANIMATIONS =====
        const animationKeyframesMap = {
            bounce: `@keyframes bounce { 0%, 20%, 50%, 80%, 100% { transform: translateY(0); } 40% { transform: translateY(-30px); } 60% { transform: translateY(-15px); } }`,
            pulse: `@keyframes pulse { 0% { transform: scale(1); } 50% { transform: scale(1.08); } 100% { transform: scale(1); } }`,
            shake: `@keyframes shake { 0%, 100% { transform: translateX(0); } 10%, 30%, 50%, 70%, 90% { transform: translateX(-8px); } 20%, 40%, 60%, 80% { transform: translateX(8px); } }`,
            fadeIn: `@keyframes fadeIn { 0% { opacity: 0; } 100% { opacity: 1; } }`,
            fadeOut: `@keyframes fadeOut { 0% { opacity: 1; } 100% { opacity: 0; } }`,
            slideInLeft: `@keyframes slideInLeft { 0% { transform: translateX(-100%); opacity: 0; } 100% { transform: translateX(0); opacity: 1; } }`,
            slideInRight: `@keyframes slideInRight { 0% { transform: translateX(100%); opacity: 0; } 100% { transform: translateX(0); opacity: 1; } }`,
            rotateIn: `@keyframes rotateIn { 0% { transform: rotate(-360deg) scale(0); opacity: 0; } 100% { transform: rotate(0) scale(1); opacity: 1; } }`,
            zoomIn: `@keyframes zoomIn { 0% { transform: scale(0.3); opacity: 0; } 50% { opacity: 1; } 100% { transform: scale(1); } }`,
            flip: `@keyframes flip { 0% { transform: perspective(400px) rotateY(0); } 50% { transform: perspective(400px) rotateY(180deg); } 100% { transform: perspective(400px) rotateY(360deg); } }`,
            swing: `@keyframes swing { 20% { transform: rotate(15deg); } 40% { transform: rotate(-10deg); } 60% { transform: rotate(5deg); } 80% { transform: rotate(-5deg); } 100% { transform: rotate(0deg); } }`,
            rubberBand: `@keyframes rubberBand { 0% { transform: scaleX(1) scaleY(1); } 30% { transform: scaleX(1.25) scaleY(0.75); } 40% { transform: scaleX(0.75) scaleY(1.25); } 50% { transform: scaleX(1.15) scaleY(0.85); } 65% { transform: scaleX(0.95) scaleY(1.05); } 75% { transform: scaleX(1.05) scaleY(0.95); } 100% { transform: scaleX(1) scaleY(1); } }`,
            jello: `@keyframes jello { 0%, 100% { transform: skewX(0) skewY(0); } 30% { transform: skewX(-12.5deg) skewY(-12.5deg); } 40% { transform: skewX(6.25deg) skewY(6.25deg); } 50% { transform: skewX(-3.125deg) skewY(-3.125deg); } 65% { transform: skewX(1.5625deg) skewY(1.5625deg); } 75% { transform: skewX(-0.78125deg) skewY(-0.78125deg); } }`,
            heartBeat: `@keyframes heartBeat { 0% { transform: scale(1); } 14% { transform: scale(1.3); } 28% { transform: scale(1); } 42% { transform: scale(1.3); } 70% { transform: scale(1); } }`,
            float: `@keyframes float { 0%, 100% { transform: translateY(0); } 50% { transform: translateY(-20px); } }`,
            glitch: `@keyframes glitch { 0%, 100% { transform: translate(0); } 20% { transform: translate(-3px, 3px); } 40% { transform: translate(3px, -3px); } 60% { transform: translate(-2px, -2px); } 80% { transform: translate(2px, 2px); } }`,
            neonPulse: `@keyframes neonPulse { 0%, 100% { box-shadow: 0 0 5px #fff, 0 0 10px #fff, 0 0 20px #64ffda, 0 0 40px #64ffda; } 50% { box-shadow: 0 0 10px #fff, 0 0 20px #fff, 0 0 40px #64ffda, 0 0 80px #64ffda; } }`,
            typewriter: `@keyframes typewriter { 0% { width: 0; } 100% { width: 100%; } }`
        };

        let injectedKeyframes = new Set();

        function injectKeyframes(name) {
            if (injectedKeyframes.has(name)) return;
            const kf = animationKeyframesMap[name];
            if (kf) {
                const style = document.createElement('style');
                style.textContent = kf;
                style.setAttribute('data-keyframe', name);
                document.head.appendChild(style);
                injectedKeyframes.add(name);
            }
        }

        function applyAnimation(name) {
            injectKeyframes(name);
            const duration = $('animationDurationRange').value;
            const timing = $('animationTimingFunction').value;
            const iteration = $('animationIterationCount').value;
            const direction = $('animationDirection').value;

            currentStyles.animationName = name;
            currentStyles.animationDuration = duration + 's';
            currentStyles.animationTimingFunction = timing;
            currentStyles.animationIterationCount = iteration;
            currentStyles.animationDirection = direction;

            previewBox.style.animation = 'none';
            previewBox.offsetHeight;
            applyStyles();
            saveToHistory();
        }

        function randomAnimation() {
            const names = Object.keys(animationKeyframesMap);
            const name = rndItem(names);
            if ($('presetAnimation')) $('presetAnimation').value = name;
            if ($('animationDurationRange')) {
                $('animationDurationRange').value = rndFloat(0.5, 3);
                if ($('animDurationVal')) $('animDurationVal').textContent = $('animationDurationRange').value + 's';
            }
            if ($('animationTimingFunction')) $('animationTimingFunction').value = rndItem(['ease', 'linear', 'ease-in', 'ease-out', 'ease-in-out']);
            if ($('animationIterationCount')) $('animationIterationCount').value = rndItem(['1', '2', '3', 'infinite']);
            applyAnimation(name);
            showToast(`Animasyon: ${name}`);
        }

        function randomTimingFunction() {
            const tf = rndItem(['ease', 'linear', 'ease-in', 'ease-out', 'ease-in-out', 'cubic-bezier(0.68, -0.55, 0.265, 1.55)']);
            if ($('animationTimingFunction')) $('animationTimingFunction').value = tf;
            currentStyles.animationTimingFunction = tf;
            applyStyles();
            saveToHistory();
        }

        function randomIterationCount() {
            const ic = rndItem(['1', '2', '3', '5', 'infinite']);
            if ($('animationIterationCount')) $('animationIterationCount').value = ic;
            currentStyles.animationIterationCount = ic;
            applyStyles();
            saveToHistory();
        }

        function stopAnimation() {
            currentStyles.animationName = 'none';
            previewBox.style.animation = 'none';
            applyStyles();
            saveToHistory();
            showToast('Animasyon durduruldu', 'info');
        }

        function randomClipPath() {
            const paths = [
                'polygon(50% 0%, 100% 50%, 50% 100%, 0% 50%)',
                'circle(50% at 50% 50%)',
                'ellipse(40% 50% at 50% 50%)',
                'polygon(50% 0%, 100% 100%, 0% 100%)',
                'polygon(25% 0%, 75% 0%, 100% 50%, 75% 100%, 25% 100%, 0% 50%)',
                'polygon(50% 0%, 61% 35%, 98% 35%, 68% 57%, 79% 91%, 50% 70%, 21% 91%, 32% 57%, 2% 35%, 39% 35%)',
                'inset(5% 5% 5% 5% round 10px)',
                `polygon(${rndInt(10,40)}% 0%, ${rndInt(60,90)}% 0%, 100% ${rndInt(10,40)}%, 100% ${rndInt(60,90)}%, ${rndInt(60,90)}% 100%, ${rndInt(10,40)}% 100%, 0% ${rndInt(60,90)}%, 0% ${rndInt(10,40)}%)`
            ];
            updateStyle('clipPath', rndItem(paths));
            showToast('Clip-path oluşturuldu');
        }

        function randomTextOpacity() {
            const val = rndFloat(0.3, 1.0);
            currentStyles.opacity = val.toString();
            if ($('textOpacityRange')) $('textOpacityRange').value = val;
            if ($('textOpacityVal')) $('textOpacityVal').textContent = val;
            applyStyles();
            saveToHistory();
        }

        function randomTextGradient() {
            const count = rndInt(2, 4);
            textGradientColors = [];
            for (let i = 0; i < count; i++) {
                textGradientColors.push({ color: rndHex(), stop: Math.round(i / (count - 1) * 100) });
            }
            if ($('textGradientAngle')) $('textGradientAngle').value = rndInt(0, 360);
            if ($('textGradientType')) $('textGradientType').value = rndItem(['linear', 'radial']);
            initGradientPickers('textGradientColors', textGradientColors, 'text');
            updateTextGradient();
            showToast('Metin gradyanı oluşturuldu');
        }

        function randomTextImageFill() {
            const images = [
                'https://picsum.photos/seed/' + rndInt(1,1000) + '/400/300',
                'https://picsum.photos/seed/' + rndInt(1,1000) + '/500/400'
            ];
            currentStyles.backgroundImage = `url(${rndItem(images)})`;
            currentStyles.backgroundSize = 'cover';
            currentStyles.webkitBackgroundClip = 'text';
            currentStyles.backgroundClip = 'text';
            currentStyles.webkitTextFillColor = 'transparent';
            applyStyles();
            saveToHistory();
            showToast('Metin resim dolgusu oluşturuldu');
        }

        function randomFilter() {
            if ($('filterBlurRange')) $('filterBlurRange').value = rndInt(0, 3);
            if ($('filterBrightnessRange')) $('filterBrightnessRange').value = rndInt(70, 150);
            if ($('filterContrastRange')) $('filterContrastRange').value = rndInt(80, 150);
            if ($('filterSaturateRange')) $('filterSaturateRange').value = rndInt(60, 200);
            if ($('filterHueRotateRange')) $('filterHueRotateRange').value = rndInt(0, 360);
            if ($('filterInvertRange')) $('filterInvertRange').value = rndInt(0, 30);
            if ($('filterSepiaRange')) $('filterSepiaRange').value = rndInt(0, 50);
            if ($('filterGrayscaleRange')) $('filterGrayscaleRange').value = rndInt(0, 40);
            updateFilter();
            showToast('Filtreler oluşturuldu');
        }

        function randomCursor() {
            const cursors = ['auto', 'pointer', 'crosshair', 'move', 'text', 'not-allowed', 'grab', 'zoom-in', 'zoom-out', 'wait', 'help'];
            updateStyle('cursor', rndItem(cursors));
        }

        function randomEffect() {
            randomFilter();
            randomCursor();
        }

        // ===== PALETTE =====
        function generatePalette() {
            const base = pickers.baseColor ? pickers.baseColor.color.hexString : '#64ffda';
            const type = $('paletteType') ? $('paletteType').value : 'monochromatic';
            const size = parseInt($('paletteSize') ? $('paletteSize').value : 5) || 5;
            let colors = [];

            try {
                const hsl = chroma(base).hsl();
                const baseHue = hsl[0] || 0;

                if (type === 'monochromatic') {
                    colors = chroma.scale([chroma(base).darken(2), base, chroma(base).brighten(2)]).colors(size);
                } else if (type === 'analogous') {
                    for (let i = 0; i < size; i++) {
                        colors.push(chroma.hsl((baseHue + i * 30) % 360, hsl[1] || 0.7, hsl[2] || 0.5).hex());
                    }
                } else if (type === 'complementary') {
                    colors.push(base);
                    colors.push(chroma.hsl((baseHue + 180) % 360, hsl[1] || 0.7, hsl[2] || 0.5).hex());
                    for (let i = 2; i < size; i++) {
                        colors.push(chroma(base).brighten(i * 0.4).hex());
                    }
                } else if (type === 'triadic') {
                    for (let i = 0; i < size; i++) {
                        colors.push(chroma.hsl((baseHue + i * 120) % 360, hsl[1] || 0.7, hsl[2] || 0.5).hex());
                    }
                } else if (type === 'split-complementary') {
                    colors.push(base);
                    colors.push(chroma.hsl((baseHue + 150) % 360, hsl[1] || 0.7, hsl[2] || 0.5).hex());
                    colors.push(chroma.hsl((baseHue + 210) % 360, hsl[1] || 0.7, hsl[2] || 0.5).hex());
                    for (let i = 3; i < size; i++) {
                        colors.push(chroma(base).brighten(i * 0.3).hex());
                    }
                } else if (type === 'tetradic') {
                    for (let i = 0; i < size; i++) {
                        colors.push(chroma.hsl((baseHue + i * 90) % 360, hsl[1] || 0.7, hsl[2] || 0.5).hex());
                    }
                }
            } catch(e) {
                colors = [base];
                for (let i = 1; i < size; i++) colors.push(rndHex());
            }

            const preview = $('palettePreview');
            if (!preview) return;
            preview.innerHTML = colors.map(c =>
                `<div class="palette-color" style="background-color:${c};" data-color="${c}" title="${c}">
                    <span class="tooltip">${c}</span>
                </div>`
            ).join('');

            preview.querySelectorAll('.palette-color').forEach(el => {
                el.addEventListener('click', () => {
                    navigator.clipboard.writeText(el.dataset.color).then(() => {
                        showToast(`Renk kopyalandı: ${el.dataset.color}`);
                    }).catch(() => {});
                });
            });
        }

        // ===== THEME PRESETS =====
        function applyThemePreset(theme) {
            currentStyles = getDefaultStyles();

            const themes = {
                neon: {
                    fontFamily: "'Orbitron', sans-serif", fontSize: '36px', fontWeight: '700',
                    color: '#0ff', backgroundColor: '#0a0a2e',
                    textShadow: '0 0 10px #0ff, 0 0 20px #0ff, 0 0 40px #0ff, 0 0 80px #0ff',
                    borderTop: '2px solid #0ff', borderBottom: '2px solid #0ff',
                    borderLeft: '2px solid #0ff', borderRight: '2px solid #0ff',
                    boxShadow: '0 0 10px #0ff, inset 0 0 10px rgba(0,255,255,0.1)',
                    borderTopLeftRadius: '12px', borderTopRightRadius: '12px',
                    borderBottomLeftRadius: '12px', borderBottomRightRadius: '12px',
                    textTransform: 'uppercase', letterSpacing: '4px'
                },
                minimal: {
                    fontFamily: "'Inter', sans-serif", fontSize: '28px', fontWeight: '300',
                    color: '#333333', backgroundColor: '#fafafa', textShadow: 'none',
                    borderTop: '1px solid #eee', borderBottom: '1px solid #eee',
                    borderLeft: '1px solid #eee', borderRight: '1px solid #eee',
                    boxShadow: '0 1px 3px rgba(0,0,0,0.04)',
                    borderTopLeftRadius: '8px', borderTopRightRadius: '8px',
                    borderBottomLeftRadius: '8px', borderBottomRightRadius: '8px',
                    letterSpacing: '1px'
                },
                vintage: {
                    fontFamily: "'Kaushan Script', cursive", fontSize: '38px', fontWeight: '400',
                    color: '#5c3317', backgroundColor: '#f4e9d8',
                    textShadow: '2px 2px 0px #d4a574',
                    borderTop: '3px double #8b6914', borderBottom: '3px double #8b6914',
                    borderLeft: '3px double #8b6914', borderRight: '3px double #8b6914',
                    boxShadow: '0 4px 8px rgba(92,51,23,0.2)',
                    borderTopLeftRadius: '4px', borderTopRightRadius: '4px',
                    borderBottomLeftRadius: '4px', borderBottomRightRadius: '4px'
                },
                glassmorphism: {
                    fontFamily: "'Inter', sans-serif", fontSize: '30px', fontWeight: '500',
                    color: '#ffffff', backgroundColor: 'rgba(255,255,255,0.1)',
                    backdropFilter: 'blur(12px)', textShadow: '0 1px 2px rgba(0,0,0,0.1)',
                    borderTop: '1px solid rgba(255,255,255,0.2)', borderBottom: '1px solid rgba(255,255,255,0.2)',
                    borderLeft: '1px solid rgba(255,255,255,0.2)', borderRight: '1px solid rgba(255,255,255,0.2)',
                    boxShadow: '0 8px 32px rgba(0,0,0,0.12)',
                    borderTopLeftRadius: '20px', borderTopRightRadius: '20px',
                    borderBottomLeftRadius: '20px', borderBottomRightRadius: '20px'
                },
                neumorphism: {
                    fontFamily: "'Poppins', sans-serif", fontSize: '28px', fontWeight: '600',
                    color: '#6b7b99', backgroundColor: '#e0e5ec',
                    textShadow: '1px 1px 2px rgba(255,255,255,0.8)',
                    borderTop: 'none', borderBottom: 'none', borderLeft: 'none', borderRight: 'none',
                    boxShadow: '8px 8px 16px #b8bec7, -8px -8px 16px #ffffff',
                    borderTopLeftRadius: '20px', borderTopRightRadius: '20px',
                    borderBottomLeftRadius: '20px', borderBottomRightRadius: '20px'
                },
                cyberpunk: {
                    fontFamily: "'Press Start 2P', monospace", fontSize: '22px', fontWeight: '400',
                    color: '#ff2d6a', backgroundColor: '#0d0221',
                    textShadow: '0 0 8px #ff2d6a, 0 0 20px #ff2d6a, 3px 3px 0px #00f0ff',
                    borderTop: '2px solid #ff2d6a', borderBottom: '4px solid #00f0ff',
                    borderLeft: '2px solid #ff2d6a', borderRight: '2px solid #00f0ff',
                    boxShadow: '0 0 15px rgba(255,45,106,0.4), inset 0 0 15px rgba(0,240,255,0.1)',
                    borderTopLeftRadius: '4px', borderTopRightRadius: '4px',
                    borderBottomLeftRadius: '4px', borderBottomRightRadius: '4px',
                    textTransform: 'uppercase', letterSpacing: '3px'
                },
                nature: {
                    fontFamily: "'Space Grotesk', sans-serif", fontSize: '32px', fontWeight: '500',
                    color: '#2d5016', backgroundColor: '#e8f5e9',
                    backgroundImage: 'linear-gradient(135deg, #e8f5e9 0%, #c8e6c9 100%)',
                    textShadow: '1px 1px 2px rgba(45,80,22,0.15)',
                    borderTop: '2px solid #81c784', borderBottom: '2px solid #81c784',
                    borderLeft: '2px solid #81c784', borderRight: '2px solid #81c784',
                    boxShadow: '0 4px 12px rgba(45,80,22,0.15)',
                    borderTopLeftRadius: '16px', borderTopRightRadius: '16px',
                    borderBottomLeftRadius: '16px', borderBottomRightRadius: '16px'
                },
                ocean: {
                    fontFamily: "'Poppins', sans-serif", fontSize: '34px', fontWeight: '600',
                    color: '#ffffff',
                    backgroundImage: 'linear-gradient(135deg, #0077b6, #023e8a, #0096c7)',
                    textShadow: '0 2px 4px rgba(0,0,0,0.3)',
                    borderTop: '2px solid rgba(255,255,255,0.3)', borderBottom: '2px solid rgba(255,255,255,0.3)',
                    borderLeft: '2px solid rgba(255,255,255,0.3)', borderRight: '2px solid rgba(255,255,255,0.3)',
                    boxShadow: '0 8px 24px rgba(0,119,182,0.4)',
                    borderTopLeftRadius: '16px', borderTopRightRadius: '16px',
                    borderBottomLeftRadius: '16px', borderBottomRightRadius: '16px'
                },
                sunset: {
                    fontFamily: "'Lobster', cursive", fontSize: '40px', fontWeight: '400',
                    color: '#fff',
                    backgroundImage: 'linear-gradient(135deg, #ff512f, #f09819, #dd2476)',
                    textShadow: '2px 2px 8px rgba(0,0,0,0.3)',
                    borderTop: 'none', borderBottom: 'none', borderLeft: 'none', borderRight: 'none',
                    boxShadow: '0 10px 30px rgba(255,81,47,0.4)',
                    borderTopLeftRadius: '24px', borderTopRightRadius: '24px',
                    borderBottomLeftRadius: '24px', borderBottomRightRadius: '24px'
                },
                'dark-elegant': {
                    fontFamily: "'Space Grotesk', sans-serif", fontSize: '30px', fontWeight: '500',
                    color: '#d4af37', backgroundColor: '#1a1a2e',
                    textShadow: '0 0 6px rgba(212,175,55,0.3)',
                    borderTop: '1px solid rgba(212,175,55,0.3)', borderBottom: '1px solid rgba(212,175,55,0.3)',
                    borderLeft: '1px solid rgba(212,175,55,0.3)', borderRight: '1px solid rgba(212,175,55,0.3)',
                    boxShadow: '0 8px 24px rgba(0,0,0,0.4), inset 0 1px 0 rgba(212,175,55,0.1)',
                    borderTopLeftRadius: '12px', borderTopRightRadius: '12px',
                    borderBottomLeftRadius: '12px', borderBottomRightRadius: '12px',
                    letterSpacing: '2px'
                }
            };

            if (themes[theme]) {
                Object.assign(currentStyles, themes[theme]);
            }

            applyStyles();
            saveToHistory();
            showToast(`Tema uygulandı: ${theme}`);
        }

        // ===== CHAOS ENGINE =====
        function autoGenerateStyles(mode) {
            const checks = {
                font: $('chaosFont') && $('chaosFont').checked,
                bg: $('chaosBackground') && $('chaosBackground').checked,
                border: $('chaosBorder') && $('chaosBorder').checked,
                effects: $('chaosEffects') && $('chaosEffects').checked,
                animation: $('chaosAnimation') && $('chaosAnimation').checked,
                clip: $('chaosClip') && $('chaosClip').checked,
                transform: $('chaosTransform') && $('chaosTransform').checked,
                shadow: $('chaosBoxShadow') && $('chaosBoxShadow').checked,
                textGradient: $('chaosTextGradient') && $('chaosTextGradient').checked,
                opacity: $('chaosOpacity') && $('chaosOpacity').checked
            };

            if (checks.font) randomFont();
            if (checks.bg) { Math.random() > 0.5 ? randomGradient() : randomBgColor(); }
            if (checks.border) randomMultiBorder();
            if (checks.effects) randomFilter();
            if (checks.animation) randomAnimation();
            if (checks.clip && Math.random() > 0.6) randomClipPath();
            if (checks.transform) randomTransform();
            if (checks.shadow) randomBoxShadow();
            if (checks.textGradient && Math.random() > 0.5) randomTextGradient();
            if (checks.opacity && Math.random() > 0.6) randomTextOpacity();
            randomBorderRadius();
            randomTextShadow();
            randomColor();

            if (mode === 'chaos') {
                showToast('🔥 KAOS MODU AKTİF!');
            } else {
                showToast('✨ Otomatik stil oluşturuldu');
            }
        }

        // ===== KEYBOARD SHORTCUTS =====
        document.addEventListener('keydown', e => {
            if ((e.ctrlKey || e.metaKey) && e.key === 'z' && !e.shiftKey) {
                e.preventDefault(); undo();
            } else if ((e.ctrlKey || e.metaKey) && (e.key === 'y' || (e.key === 'z' && e.shiftKey))) {
                e.preventDefault(); redo();
            } else if ((e.ctrlKey || e.metaKey) && e.key === 's') {
                e.preventDefault();
                navigator.clipboard.writeText(cssOutput.value).then(() => showToast('CSS kopyalandı!')).catch(() => {});
            }
        });

        // ===== EVENT LISTENERS =====

        // Action buttons (header)
        $$('[data-action]').forEach(btn => {
            btn.addEventListener('click', () => {
                const action = btn.dataset.action;
                switch(action) {
                    case 'undo': undo(); break;
                    case 'redo': redo(); break;
                    case 'toggle-theme':
                        currentTheme = currentTheme === 'dark' ? 'light' : 'dark';
                        document.documentElement.setAttribute('data-theme', currentTheme);
                        btn.querySelector('i').className = currentTheme === 'dark' ? 'fas fa-moon' : 'fas fa-sun';
                        showToast(`Tema: ${currentTheme === 'dark' ? 'Koyu' : 'Açık'}`, 'info');
                        break;
                    case 'reset-all':
                        currentStyles = getDefaultStyles();
                        const resetRanges = {
                            fontSizeRange: 30, fontWeightRange: 400, lineHeightRange: 1.5,
                            backgroundOpacityRange: 1, textOpacityRange: 1,
                            rotateRange: 0, scaleRange: 1, borderRadiusAll: 10,
                            filterBlurRange: 0, filterBrightnessRange: 100, filterContrastRange: 100,
                            filterSaturateRange: 100, filterHueRotateRange: 0, filterInvertRange: 0,
                            filterSepiaRange: 0, filterGrayscaleRange: 0, backdropBlurRange: 0
                        };
                        Object.entries(resetRanges).forEach(([id, val]) => {
                            if ($(id)) $(id).value = val;
                        });
                        previewBox.style.animation = 'none';
                        // Clear webkit props
                        previewBox.style.removeProperty('-webkit-text-fill-color');
                        previewBox.style.removeProperty('-webkit-background-clip');
                        applyStyles();
                        saveToHistory();
                        showToast('Tüm stiller sıfırlandı', 'info');
                        break;
                    case 'download-css': {
                        const blob = new Blob([cssOutput.value], { type: 'text/css' });
                        const url = URL.createObjectURL(blob);
                        const a = document.createElement('a');
                        a.href = url; a.download = 'k3n4n-styles.css'; a.click();
                        URL.revokeObjectURL(url);
                        showToast('CSS dosyası indirildi');
                        break;
                    }
                    case 'download-html': {
                        const text = customTextInput.value || 'K3N4N V6.0';
                        const html = `<!DOCTYPE html>\n<html lang="tr">\n<head>\n    <meta charset="UTF-8">\n    <title>K3N4N V6.0 Preview</title>\n    <style>\n${cssOutput.value}\n    </style>\n</head>\n<body style="display:flex;justify-content:center;align-items:center;min-height:100vh;margin:0;background:#1a1a2e;">\n    <div class="my-element">${text}</div>\n</body>\n</html>`;
                        const blob = new Blob([html], { type: 'text/html' });
                        const url = URL.createObjectURL(blob);
                        const a = document.createElement('a');
                        a.href = url; a.download = 'k3n4n-preview.html'; a.click();
                        URL.revokeObjectURL(url);
                        showToast('HTML dosyası indirildi');
                        break;
                    }
                    case 'export-styles': {
                        const data = JSON.stringify(currentStyles, null, 2);
                        const blob = new Blob([data], { type: 'application/json' });
                        const url = URL.createObjectURL(blob);
                        const a = document.createElement('a');
                        a.href = url; a.download = 'k3n4n-styles.json'; a.click();
                        URL.revokeObjectURL(url);
                        showToast('Stiller dışa aktarıldı');
                        break;
                    }
                    case 'import-styles':
                        if ($('import-styles')) $('import-styles').click();
                        break;
                }
            });
        });

        // Style target buttons
        $$('[data-style-target]').forEach(btn => {
            btn.addEventListener('click', () => {
                const target = btn.dataset.styleTarget;
                const handlers = {
                    'random-font': randomFont,
                    'random-color': randomColor,
                    'random-text-shadow': randomTextShadow,
                    'random-text-decoration': randomTextDecoration,
                    'random-spacing': randomSpacing,
                    'random-align': randomAlign,
                    'random-line-height': randomLineHeight,
                    'random-text-transform': randomTextTransform,
                    'random-bg-color': randomBgColor,
                    'random-gradient': randomGradient,
                    'random-bg-gif': randomBgGif,
                    'random-bg-position': randomBgPosition,
                    'random-bg-size': randomBgSize,
                    'random-bg-opacity': randomBgOpacity,
                    'random-bg-pattern': randomBgPattern,
                    'random-bg-blend': randomBgBlend,
                    'random-multi-border': randomMultiBorder,
                    'random-border-color': randomBorderColor,
                    'random-outline': randomOutline,
                    'random-border-radius': randomBorderRadius,
                    'random-transform': randomTransform,
                    'random-box-shadow': randomBoxShadow,
                    'random-box-shadow-color': randomBoxShadowColor,
                    'random-multi-shadow': randomMultiShadow,
                    'random-inset-shadow': randomInsetShadow,
                    'random-animation': randomAnimation,
                    'random-timing-function': randomTimingFunction,
                    'random-iteration-count': randomIterationCount,
                    'stop-animation': stopAnimation,
                    'random-clip-path': randomClipPath,
                    'random-text-opacity': randomTextOpacity,
                    'random-text-gradient': randomTextGradient,
                    'random-text-image-fill': randomTextImageFill,
                    'random-filter': randomFilter,
                    'random-cursor': randomCursor,
                    'random-effect': randomEffect,
                    'generate-palette': generatePalette,
                    'auto-generate': () => autoGenerateStyles('random'),
                    'max-chaos': () => autoGenerateStyles('chaos')
                };

                if (handlers[target]) {
                    handlers[target]();
                    return;
                }

                // Special cases
                switch(target) {
                    case 'reset-transform':
                        ['rotateRange', 'rotate'].forEach(id => { if ($(id)) $(id).value = 0; });
                        if ($('scaleRange')) $('scaleRange').value = 1;
                        ['skewX', 'skewY', 'translateX', 'translateY'].forEach(id => { if ($(id)) $(id).value = 0; });
                        updateTransform();
                        showToast('Dönüşüm sıfırlandı', 'info');
                        break;
                    case 'reset-clip':
                        updateStyle('clipPath', 'none');
                        showToast('Clip-path sıfırlandı', 'info');
                        break;
                    case 'reset-text-fill':
                        currentStyles.backgroundImage = 'none';
                        currentStyles.webkitBackgroundClip = '';
                        currentStyles.webkitTextFillColor = '';
                        currentStyles.backgroundClip = 'border-box';
                        previewBox.style.removeProperty('-webkit-text-fill-color');
                        previewBox.style.removeProperty('-webkit-background-clip');
                        applyStyles();
                        saveToHistory();
                        showToast('Metin dolgusu sıfırlandı', 'info');
                        break;
                    case 'reset-filters':
                        ['filterBlurRange:0', 'filterBrightnessRange:100', 'filterContrastRange:100',
                         'filterSaturateRange:100', 'filterHueRotateRange:0', 'filterInvertRange:0',
                         'filterSepiaRange:0', 'filterGrayscaleRange:0', 'backdropBlurRange:0'].forEach(s => {
                            const [id, val] = s.split(':');
                            if ($(id)) $(id).value = val;
                        });
                        updateFilter();
                        showToast('Filtreler sıfırlandı', 'info');
                        break;
                    case 'random-palette':
                        if (pickers.baseColor) pickers.baseColor.color.hexString = rndHex();
                        generatePalette();
                        showToast('Palet oluşturuldu');
                        break;
                    default:
                        // Theme presets
                        if (target.startsWith('auto-theme-')) {
                            applyThemePreset(target.replace('auto-theme-', ''));
                        }
                        break;
                }
            });
        });

        // Direct style prop inputs
        $$('[data-style-prop]').forEach(input => {
            const handler = () => {
                const prop = input.dataset.styleProp;
                const unit = input.dataset.styleUnit || '';
                if (prop === 'transform') {
                    updateTransform();
                } else if (prop === 'filter') {
                    updateFilter();
                } else {
                    updateStyle(prop, input.value, unit);
                }
            };
            input.addEventListener('input', handler);
            input.addEventListener('change', handler);
        });

        // Range slider sync helpers
        function syncRange(rangeId, valueDisplay, callback) {
            const range = $(rangeId);
            if (!range) return;
            range.addEventListener('input', () => {
                if (valueDisplay) {
                    const el = $(valueDisplay);
                    if (el) el.textContent = range.value + (range.dataset.unit || '');
                }
                if (callback) callback(range.value);
            });
        }

        syncRange('fontSizeRange', 'fontSizeVal', v => {
            if ($('fontSize')) $('fontSize').value = v;
            if ($('fontSizeVal')) $('fontSizeVal').textContent = v + 'px';
            updateStyle('fontSize', v, 'px');
        });

        syncRange('fontWeightRange', 'fontWeightVal', v => {
            if ($('fontWeight')) $('fontWeight').value = v;
            if ($('fontWeightVal')) $('fontWeightVal').textContent = v;
            updateStyle('fontWeight', v);
        });

        if ($('fontWeight')) {
            $('fontWeight').addEventListener('change', () => {
                const v = $('fontWeight').value;
                if ($('fontWeightRange')) $('fontWeightRange').value = v;
                if ($('fontWeightVal')) $('fontWeightVal').textContent = v;
                updateStyle('fontWeight', v);
            });
        }

        syncRange('lineHeightRange', 'lineHeightVal', v => {
            if ($('lineHeightVal')) $('lineHeightVal').textContent = v;
            updateStyle('lineHeight', v);
        });

        syncRange('backgroundOpacityRange', 'bgOpacityVal', v => {
            if ($('bgOpacityVal')) $('bgOpacityVal').textContent = v;
            updateStyle('opacity', v);
        });

        syncRange('textOpacityRange', 'textOpacityVal', v => {
            if ($('textOpacityVal')) $('textOpacityVal').textContent = v;
            updateStyle('opacity', v);
        });

        syncRange('rotateRange', 'rotateVal', v => {
            if ($('rotate')) $('rotate').value = v;
            if ($('rotateVal')) $('rotateVal').textContent = v + '°';
            updateTransform();
        });

        if ($('rotate')) {
            $('rotate').addEventListener('input', () => {
                if ($('rotateRange')) $('rotateRange').value = $('rotate').value;
                if ($('rotateVal')) $('rotateVal').textContent = $('rotate').value + '°';
                updateTransform();
            });
        }

        syncRange('scaleRange', 'scaleVal', v => {
            if ($('scaleVal')) $('scaleVal').textContent = v;
            updateTransform();
        });

        syncRange('borderRadiusAll', 'borderRadiusVal', v => {
            if ($('borderRadiusVal')) $('borderRadiusVal').textContent = v + 'px';
            ['borderRadiusTopLeft', 'borderRadiusTopRight', 'borderRadiusBottomLeft', 'borderRadiusBottomRight'].forEach(id => {
                if ($(id)) $(id).value = v;
            });
            updateStyle('borderTopLeftRadius', v, 'px');
            updateStyle('borderTopRightRadius', v, 'px');
            updateStyle('borderBottomLeftRadius', v, 'px');
            updateStyle('borderBottomRightRadius', v, 'px');
        });

        syncRange('animationDurationRange', 'animDurationVal', v => {
            if ($('animDurationVal')) $('animDurationVal').textContent = v + 's';
            currentStyles.animationDuration = v + 's';
            applyStyles();
        });

        // Filter ranges
        ['filterBlurRange', 'filterBrightnessRange', 'filterContrastRange', 'filterSaturateRange',
         'filterHueRotateRange', 'filterInvertRange', 'filterSepiaRange', 'filterGrayscaleRange', 'backdropBlurRange'].forEach(id => {
            const el = $(id);
            if (el) el.addEventListener('input', updateFilter);
        });

        // Complex inputs
        ['textShadowX', 'textShadowY', 'textShadowBlur'].forEach(id => {
            const el = $(id);
            if (el) el.addEventListener('input', () => {
                const color = pickers.textShadowColor ? pickers.textShadowColor.color.hexString : '#000000';
                updateComplexStyle('textShadowColor', color);
            });
        });

        ['boxShadowX', 'boxShadowY', 'boxShadowBlur', 'boxShadowSpread'].forEach(id => {
            const el = $(id);
            if (el) el.addEventListener('input', updateBoxShadow);
        });

        if ($('boxShadowInset')) $('boxShadowInset').addEventListener('change', updateBoxShadow);

        ['outlineWidth', 'outlineStyle'].forEach(id => {
            const el = $(id);
            if (el) {
                const handler = () => {
                    const color = pickers.outlineColor ? pickers.outlineColor.color.hexString : '#ffffff';
                    updateComplexStyle('outlineColor', color);
                };
                el.addEventListener('input', handler);
                el.addEventListener('change', handler);
            }
        });

        ['skewX', 'skewY', 'translateX', 'translateY'].forEach(id => {
            const el = $(id);
            if (el) el.addEventListener('input', updateTransform);
        });

        ['gradientAngle', 'gradientType'].forEach(id => {
            const el = $(id);
            if (el) {
                el.addEventListener('input', updateGradient);
                el.addEventListener('change', updateGradient);
            }
        });

        ['textGradientAngle', 'textGradientType'].forEach(id => {
            const el = $(id);
            if (el) {
                el.addEventListener('input', updateTextGradient);
                el.addEventListener('change', updateTextGradient);
            }
        });

        if ($('backgroundImageUrl')) $('backgroundImageUrl').addEventListener('input', updateBackgroundImageUrl);
        if ($('textImageFill')) $('textImageFill').addEventListener('input', updateTextImageFill);

        ['paddingLeft', 'paddingRight', 'paddingTop', 'paddingBottom', 'paddingUnit'].forEach(id => {
            const el = $(id);
            if (el) {
                el.addEventListener('input', updatePadding);
                el.addEventListener('change', updatePadding);
            }
        });

        if ($('transitionProperty')) $('transitionProperty').addEventListener('change', updateTransition);
        if ($('transitionDuration')) $('transitionDuration').addEventListener('input', updateTransition);

        // Preset animation
        if ($('presetAnimation')) {
            $('presetAnimation').addEventListener('change', () => {
                const name = $('presetAnimation').value;
                if (name) applyAnimation(name);
            });
        }

        // Preset clip-path
        if ($('presetClipPath')) {
            $('presetClipPath').addEventListener('change', () => {
                const val = $('presetClipPath').value;
                if (val !== '') {
                    updateStyle('clipPath', val);
                    if ($('clipPath')) $('clipPath').value = val;
                }
            });
        }

        // Custom keyframes
        if ($('applyKeyframesBtn')) {
            $('applyKeyframesBtn').addEventListener('click', () => {
                const kf = ($('animationKeyframes') ? $('animationKeyframes').value : '').trim();
                if (kf) {
                    const style = document.createElement('style');
                    style.textContent = kf;
                    document.head.appendChild(style);
                    const match = kf.match(/@keyframes\s+([a-zA-Z0-9_-]+)/);
                    if (match) {
                        applyAnimation(match[1]);
                        showToast(`Keyframes uygulandı: ${match[1]}`);
                    }
                }
            });
        }

        // Custom text input
        if (customTextInput) {
            customTextInput.addEventListener('input', () => {
                previewBox.textContent = customTextInput.value || 'K3N4N V6.0';
                if ($('charCount')) $('charCount').textContent = `${customTextInput.value.length}/100`;
                updateHtmlPreview();
            });
        }

        // Font size number input sync
        if ($('fontSize')) {
            $('fontSize').addEventListener('input', () => {
                const v = $('fontSize').value;
                if ($('fontSizeRange')) $('fontSizeRange').value = v;
                if ($('fontSizeVal')) $('fontSizeVal').textContent = v + 'px';
                updateStyle('fontSize', v, 'px');
            });
        }

        // Custom CSS apply
        if ($('applyCustomCss')) {
            $('applyCustomCss').addEventListener('click', () => {
                try {
                    const css = cssInputArea ? cssInputArea.value.trim() : '';
                    if (!css) return;
                    // Remove any previous custom style
                    const prev = document.querySelector('style[data-custom-css]');
                    if (prev) prev.remove();
                    const style = document.createElement('style');
                    style.setAttribute('data-custom-css', 'true');
                    style.textContent = `#preview-box { ${css} }`;
                    document.head.appendChild(style);
                    if ($('css-success')) { $('css-success').classList.add('visible'); setTimeout(() => $('css-success').classList.remove('visible'), 2500); }
                    if ($('css-error')) $('css-error').classList.remove('visible');
                    showToast('Özel CSS uygulandı');
                } catch(e) {
                    if ($('css-error')) { $('css-error').classList.add('visible'); setTimeout(() => $('css-error').classList.remove('visible'), 2500); }
                    if ($('css-success')) $('css-success').classList.remove('visible');
                }
            });
        }

        // Copy CSS
        if ($('copy-css-btn')) {
            $('copy-css-btn').addEventListener('click', () => {
                navigator.clipboard.writeText(cssOutput.value).then(() => {
                    if ($('copy-success')) { $('copy-success').classList.add('visible'); setTimeout(() => $('copy-success').classList.remove('visible'), 2500); }
                    if ($('copy-error')) $('copy-error').classList.remove('visible');
                    showToast('CSS kopyalandı!');
                }).catch(() => {
                    if ($('copy-error')) { $('copy-error').classList.add('visible'); setTimeout(() => $('copy-error').classList.remove('visible'), 2500); }
                    showToast('Kopyalama başarısız', 'error');
                });
            });
        }

        // Import styles
        if ($('import-styles')) {
            $('import-styles').addEventListener('change', e => {
                const file = e.target.files[0];
                if (!file) return;
                const reader = new FileReader();
                reader.onload = event => {
                    try {
                        const imported = JSON.parse(event.target.result);
                        currentStyles = { ...getDefaultStyles(), ...imported };
                        applyStyles();
                        saveToHistory();
                        showToast('Stiller içe aktarıldı');
                    } catch(err) {
                        showToast('Geçersiz dosya!', 'error');
                    }
                };
                reader.readAsText(file);
                e.target.value = '';
            });
        }

        // ===== PANELS (Accordion) =====
        $$('.panel-header').forEach(header => {
            header.addEventListener('click', () => {
                const panel = header.closest('.panel');
                if (panel) panel.classList.toggle('expanded');
            });
        });

        // ===== TABS =====
        $$('.output-tab').forEach(tab => {
            tab.addEventListener('click', () => {
                $$('.output-tab').forEach(t => t.classList.remove('active'));
                $$('.tab-content').forEach(c => c.classList.remove('active'));
                tab.classList.add('active');
                const target = $(tab.dataset.tab);
                if (target) target.classList.add('active');
            });
        });

        // ===== SIDEBAR TOGGLE (Mobile) =====
        if ($('sidebarToggle')) {
            $('sidebarToggle').addEventListener('click', () => {
                const sidebar = $('sidebar');
                const overlay = $('sidebarOverlay');
                if (sidebar) sidebar.classList.toggle('open');
                if (overlay) overlay.classList.toggle('visible');
            });
        }

        if ($('sidebarOverlay')) {
            $('sidebarOverlay').addEventListener('click', () => {
                const sidebar = $('sidebar');
                const overlay = $('sidebarOverlay');
                if (sidebar) sidebar.classList.remove('open');
                if (overlay) overlay.classList.remove('visible');
            });
        }

        // ===== PANEL SEARCH =====
        if ($('panelSearch')) {
            $('panelSearch').addEventListener('input', e => {
                const q = e.target.value.toLowerCase().trim();
                $$('.panel').forEach(panel => {
                    const title = panel.querySelector('.panel-title');
                    const text = (title ? title.textContent : '').toLowerCase();
                    const panelName = (panel.dataset.panel || '').toLowerCase();
                    panel.style.display = (!q || text.includes(q) || panelName.includes(q)) ? '' : 'none';
                });
            });
        }

        // ===== INITIALIZATION =====
        initGradientPickers('gradientColors', gradientColors, 'bg');
        initGradientPickers('textGradientColors', textGradientColors, 'text');
        applyStyles();
        saveToHistory();
        generatePalette();

        // Set initial badge values
        const initBadges = {
            fontSizeVal: '30px', fontWeightVal: '400', lineHeightVal: '1.5',
            bgOpacityVal: '1', textOpacityVal: '1', rotateVal: '0°', scaleVal: '1',
            borderRadiusVal: '10px', animDurationVal: '1s', blurVal: '0px',
            brightnessVal: '100%', contrastVal: '100%', saturateVal: '100%',
            hueRotateVal: '0°', invertVal: '0%', sepiaVal: '0%', grayscaleVal: '0%'
        };
        Object.entries(initBadges).forEach(([id, val]) => {
            if ($(id)) $(id).textContent = val;
        });

        // Window resize observer for preview dimensions
        if (typeof ResizeObserver !== 'undefined') {
            const resizeObserver = new ResizeObserver(() => updatePreviewDimensions());
            resizeObserver.observe(previewBox);
        }

        console.log('%c🎨 K3N4N CSS Generator V6.0 initialized!', 'color: #22d3ee; font-size: 14px; font-weight: bold;');

    })();
    </script>
</body>
</html>
```

Bu kod önceki mesajdaki CSS ile birlikte **tamamen uyumlu ve eksiksiz çalışan** bir bütündür. Yapılan temel düzeltme ve iyileştirmeler şunlardır:

HTML class isimleri ile CSS selektörleri arasındaki tüm uyumsuzluklar giderildi (`.app-header`, `.header-actions`, `.header-btn`, `.sidebar-search`, `.preview-wrapper`, `.preview-label`, `.output-card`, `.output-card-body`, `.preset-cards`, `.preset-card`, `.style-btn`, `.btn-grid`, `.separator`, `.form-group`, `.form-row`, `.checkbox-row`, `.value-badge`, `.msg` vb.). Light tema desteği CSS variable override ile eklendi. Tüm null-check'ler (`if ($(id))`) eklenerek hata önlendi. Tema presetleri tek bir object map'e dönüştürüldü. Style target handler'lar temiz bir lookup table yapısına alındı. Toast animasyonları kaybolma efektiyle geliştirildi. Özel CSS uygulamasında önceki style tag temizleniyor. Reset işleminde webkit property'ler de temizleniyor.

### GLM 4.7
*2026-02-07 18:47:43 +03*

```javascript
                minWidth: 'auto',
                maxWidth: 'auto',
                minHeight: '280px',
                maxHeight: 'auto',
                overflow: 'hidden',
                display: 'flex',
                flexDirection: 'row',
                justifyContent: 'center',
                alignItems: 'center',
                gap: '0px',
                transition: 'none'
            };
        }

        // ===== TOAST SİSTEMİ =====
        function showToast(message, type = 'success') {
            const toast = document.createElement('div');
            toast.className = `toast ${type}`;
            
            let iconClass = 'info-circle';
            if(type === 'success') iconClass = 'check-circle';
            else if(type === 'error') iconClass = 'exclamation-circle';

            toast.innerHTML = `<i class="fas fa-${iconClass}"></i> ${message}`;
            toastContainer.appendChild(toast);
            
            // Toast kaldırma işlemi
            setTimeout(() => {
                toast.style.opacity = '0';
                toast.style.transform = 'translateX(40px) scale(0.95)';
                setTimeout(() => toast.remove(), 400);
            }, 3000);
        }

        // ===== COLOR PICKERS YAPILANDIRMASI =====
        const pickers = {};
        const pickerConfigs = [
            { id: 'textColorPicker', key: 'textColor', default: '#222222', onChange: c => updateStyle('color', c.hexString) },
            { id: 'textShadowColorPicker', key: 'textShadowColor', default: '#000000', onChange: c => updateComplexStyle('textShadowColor', c.hexString) },
            { id: 'backgroundColorPicker', key: 'bgColor', default: '#ffffff', onChange: c => updateStyle('backgroundColor', c.hexString) },
            { id: 'outlineColorPicker', key: 'outlineColor', default: '#ffffff', onChange: c => updateComplexStyle('outlineColor', c.hexString) },
            { id: 'boxShadowColorPicker', key: 'boxShadowColor', default: '#000000', onChange: c => updateComplexStyle('boxShadowColor', c.hexString) },
            { id: 'baseColorPicker', key: 'baseColor', default: '#64ffda', onChange: () => generatePalette() }
        ];

        pickerConfigs.forEach(cfg => {
            const el = $(cfg.id);
            if (!el) return;
            
            try {
                pickers[cfg.key] = new iro.ColorPicker(el, {
                    width: 140,
                    color: cfg.default,
                    borderWidth: 2,
                    borderColor: 'rgba(255,255,255,0.1)',
                    layoutDirection: 'horizontal',
                    layout: [
                        { component: iro.ui.Wheel, options: { wheelLightness: true, wheelThickness: 10 } },
                        { component: iro.ui.Slider, options: { sliderType: 'value', sliderShape: 'circle' } }
                    ]
                });
                pickers[cfg.key].on('color:change', cfg.onChange);
            } catch(e) {
                console.warn("Color picker init error for:", cfg.id, e);
            }
        });

        // ===== GRADIENT YÖNETİMİ =====
        let gradientColors = [{ color: '#64ffda', stop: 0 }, { color: '#c084fc', stop: 100 }];
        let textGradientColors = [{ color: '#64ffda', stop: 0 }, { color: '#ff6b9d', stop: 100 }];

        function initGradientPickers(containerId, colors, type) {
            const el = $(containerId);
            if (!el) return;
            el.innerHTML = '';
            
            colors.forEach((gc, i) => {
                const row = document.createElement('div');
                row.className = 'gradient-color-row';
                
                // Renk Seçici
                const colorInput = document.createElement('input');
                colorInput.type = 'color';
                colorInput.value = gc.color;
                colorInput.style.cssText = 'width:36px;height:28px;border:1px solid var(--border-light);border-radius:4px;cursor:pointer;background:var(--bg-dark);padding:1px;';
                colorInput.addEventListener('input', e => {
                    colors[i].color = e.target.value;
                    type === 'bg' ? updateGradient() : updateTextGradient();
                });

                // Stop Konumu
                const stopInput = document.createElement('input');
                stopInput.type = 'number';
                stopInput.className = type === 'bg' ? 'gradientStop' : 'textGradientStop';
                stopInput.value = gc.stop;
                stopInput.min = 0;
                stopInput.max = 100;
                stopInput.style.cssText = 'width: 55px; padding: 5px; background: var(--bg-dark); border: 1px solid var(--border-color); border-radius: 4px; color: var(--text-white); font-size: 11px; text-align: center; font-family: inherit;';
                stopInput.addEventListener('input', e => {
                    colors[i].stop = parseInt(e.target.value) || 0;
                    type === 'bg' ? updateGradient() : updateTextGradient();
                });

                // Kaldır Butonu
                const removeBtn = document.createElement('button');
                removeBtn.className = type === 'bg' ? 'removeGradientColor' : 'removeTextGradientColor';
                removeBtn.innerHTML = '<i class="fas fa-trash"></i>';
                removeBtn.addEventListener('click', () => {
                    if (colors.length > 1) {
                        colors.splice(i, 1);
                        initGradientPickers(containerId, colors, type);
                        type === 'bg' ? updateGradient() : updateTextGradient();
                    }
                });

                row.appendChild(colorInput);
                row.appendChild(stopInput);
                row.appendChild(removeBtn);
                el.appendChild(row);
            });
        }

        $('addGradientColor').addEventListener('click', () => {
            gradientColors.push({ color: '#' + Math.floor(Math.random() * 16777215).toString(16).padStart(6,'0'), stop: 100 });
            initGradientPickers('gradientColors', gradientColors, 'bg');
            updateGradient();
        });

        $('addTextGradientColor').addEventListener('click', () => {
            textGradientColors.push({ color: '#' + Math.floor(Math.random() * 16777215).toString(16).padStart(6,'0'), stop: 100 });
            initGradientPickers('textGradientColors', textGradientColors, 'text');
            updateTextGradient();
        });

        // ===== CORE STYLE FONKSİYONLARI =====
        function updateStyle(property, value, unit = '') {
            const finalVal = unit ? `${value}${unit}` : value;
            if (currentStyles[property] !== finalVal) {
                currentStyles[property] = finalVal;
                applyStyles();
                saveToHistory();
            }
        }

        function updateComplexStyle(property, value) {
            if (property === 'textShadowColor') {
                const x = $('textShadowX') ? $('textShadowX').value : 0;
                const y = $('textShadowY') ? $('textShadowY').value : 0;
                const blur = $('textShadowBlur') ? $('textShadowBlur').value : 0;
                currentStyles.textShadow = `${x}px ${y}px ${blur}px ${value}`;
            } else if (property === 'boxShadowColor') {
                const x = $('boxShadowX') ? $('boxShadowX').value : 0;
                const y = $('boxShadowY') ? $('boxShadowY').value : 0;
                const blur = $('boxShadowBlur') ? $('boxShadowBlur').value : 0;
                const spread = $('boxShadowSpread') ? $('boxShadowSpread').value : 0;
                const inset = $('boxShadowInset') && $('boxShadowInset').checked ? 'inset ' : '';
                currentStyles.boxShadow = `${inset}${x}px ${y}px ${blur}px ${spread}px ${value}`;
            } else if (property === 'outlineColor') {
                currentStyles.outlineWidth = ($('outlineWidth').value || 0) + 'px';
                currentStyles.outlineStyle = $('outlineStyle').value;
                currentStyles.outlineColor = value;
            }
            applyStyles();
            saveToHistory();
        }

        function updateGradient() {
            const type = $('gradientType').value;
            const angle = $('gradientAngle').value;
            const stops = gradientColors.map(gc => `${gc.color} ${gc.stop}%`).join(', ');
            let gradient;
            if (type === 'linear') gradient = `linear-gradient(${angle}deg, ${stops})`;
            else if (type === 'radial') gradient = `radial-gradient(circle, ${stops})`;
            else gradient = `conic-gradient(from ${angle}deg, ${stops})`;
            
            currentStyles.backgroundImage = gradient;
            currentStyles.webkitBackgroundClip = '';
            currentStyles.webkitTextFillColor = '';
            currentStyles.backgroundClip = 'border-box';
            applyStyles();
            saveToHistory();
        }

        function updateTextGradient() {
            const type = $('textGradientType').value;
            const angle = $('textGradientAngle').value;
            const stops = textGradientColors.map(gc => `${gc.color} ${gc.stop}%`).join(', ');
            let gradient;
            if (type === 'linear') gradient = `linear-gradient(${angle}deg, ${stops})`;
            else gradient = `radial-gradient(circle, ${stops})`;
            
            currentStyles.backgroundImage = gradient;
            currentStyles.webkitBackgroundClip = 'text';
            currentStyles.backgroundClip = 'text';
            currentStyles.webkitTextFillColor = 'transparent';
            applyStyles();
            saveToHistory();
        }

        function updateTextImageFill() {
            const url = $('textImageFill').value.trim();
            if (url) {
                currentStyles.backgroundImage = `url(${url})`;
                currentStyles.backgroundSize = 'cover';
                currentStyles.webkitBackgroundClip = 'text';
                currentStyles.backgroundClip = 'text';
                currentStyles.webkitTextFillColor = 'transparent';
            } else {
                currentStyles.backgroundImage = 'none';
                currentStyles.webkitBackgroundClip = '';
                currentStyles.backgroundClip = 'border-box';
                currentStyles.webkitTextFillColor = '';
            }
            applyStyles();
            saveToHistory();
        }

        function updateBackgroundImageUrl() {
            const url = $('backgroundImageUrl').value.trim();
            if (url) {
                currentStyles.backgroundImage = `url(${url})`;
                currentStyles.webkitBackgroundClip = '';
                currentStyles.webkitTextFillColor = '';
                currentStyles.backgroundClip = 'border-box';
            } else {
                currentStyles.backgroundImage = 'none';
            }
            applyStyles();
            saveToHistory();
        }

        function updateFilter() {
            const blur = $('filterBlurRange').value;
            const brightness = $('filterBrightnessRange').value;
            const contrast = $('filterContrastRange').value;
            const saturate = $('filterSaturateRange').value;
            const hueRotate = $('filterHueRotateRange').value;
            const invert = $('filterInvertRange').value;
            const sepia = $('filterSepiaRange').value;
            const grayscale = $('filterGrayscaleRange').value;
            
            let parts = [];
            if (parseFloat(blur) > 0) parts.push(`blur(${blur}px)`);
            if (parseFloat(brightness) != 100) parts.push(`brightness(${brightness}%)`);
            if (parseFloat(contrast) != 100) parts.push(`contrast(${contrast}%)`);
            if (parseFloat(saturate) != 100) parts.push(`saturate(${saturate}%)`);
            if (parseFloat(hueRotate) > 0) parts.push(`hue-rotate(${hueRotate}deg)`);
            if (parseFloat(invert) > 0) parts.push(`invert(${invert}%)`);
            if (parseFloat(sepia) > 0) parts.push(`sepia(${sepia}%)`);
            if (parseFloat(grayscale) > 0) parts.push(`grayscale(${grayscale}%)`);
            
            currentStyles.filter = parts.length ? parts.join(' ') : 'none';

            const backdropBlur = $('backdropBlurRange').value;
            currentStyles.backdropFilter = parseFloat(backdropBlur) > 0 ? `blur(${backdropBlur}px)` : 'none';

            // Badge güncellemeleri
            if($('blurVal')) $('blurVal').textContent = blur + 'px';
            if($('brightnessVal')) $('brightnessVal').textContent = brightness + '%';
            if($('contrastVal')) $('contrastVal').textContent = contrast + '%';
            if($('saturateVal')) $('saturateVal').textContent = saturate + '%';
            if($('hueRotateVal')) $('hueRotateVal').textContent = hueRotate + '°';
            if($('invertVal')) $('invertVal').textContent = invert + '%';
            if($('sepiaVal')) $('sepiaVal').textContent = sepia + '%';
            if($('grayscaleVal')) $('grayscaleVal').textContent = grayscale + '%';

            applyStyles();
            saveToHistory();
        }

        function updatePadding() {
            const unit = $('paddingUnit').value;
            currentStyles.paddingLeft = ($('paddingLeft').value || 0) + unit;
            currentStyles.paddingRight = ($('paddingRight').value || 0) + unit;
            currentStyles.paddingTop = ($('paddingTop').value || 0) + unit;
            currentStyles.paddingBottom = ($('paddingBottom').value || 0) + unit;
            applyStyles();
            saveToHistory();
        }

        function updateTransform() {
            const rotate = $('rotate') ? $('rotate').value : ($('rotateRange') ? $('rotateRange').value : 0);
            const scale = $('scaleRange').value;
            const skewX = $('skewX') ? $('skewX').value : 0;
            const skewY = $('skewY') ? $('skewY').value : 0;
            const translateX = $('translateX') ? $('translateX').value : 0;
            const translateY = $('translateY') ? $('translateY').value : 0;
            
            let parts = [];
            if (parseFloat(rotate) != 0) parts.push(`rotate(${rotate}deg)`);
            if (parseFloat(scale) != 1) parts.push(`scale(${scale})`);
            if (parseFloat(skewX) != 0) parts.push(`skewX(${skewX}deg)`);
            if (parseFloat(skewY) != 0) parts.push(`skewY(${skewY}deg)`);
            if (parseFloat(translateX) != 0) parts.push(`translateX(${translateX}px)`);
            if (parseFloat(translateY) != 0) parts.push(`translateY(${translateY}px)`);
            
            currentStyles.transform = parts.length ? parts.join(' ') : 'none';

            if($('rotateVal')) $('rotateVal').textContent = rotate + '°';
            if($('scaleVal')) $('scaleVal').textContent = scale;

            applyStyles();
            saveToHistory();
        }

        function updateBoxShadow() {
            const x = $('boxShadowX') ? $('boxShadowX').value : 0;
            const y = $('boxShadowY') ? $('boxShadowY').value : 0;
            const blur = $('boxShadowBlur') ? $('boxShadowBlur').value : 0;
            const spread = $('boxShadowSpread') ? $('boxShadowSpread').value : 0;
            const inset = $('boxShadowInset') && $('boxShadowInset').checked ? 'inset ' : '';
            const color = pickers.boxShadowColor ? pickers.boxShadowColor.color.hexString : '#000000';
            
            currentStyles.boxShadow = `${inset}${x}px ${y}px ${blur}px ${spread}px ${color}`;
            applyStyles();
            saveToHistory();
        }

        function updateTransition() {
            const prop = $('transitionProperty').value;
            const dur = $('transitionDuration').value;
            currentStyles.transition = `${prop} ${dur}s ease`;
            applyStyles();
            saveToHistory();
        }

        // ===== STİLLERİ UYGULA =====
        function applyStyles() {
            const stylePropMap = {
                webkitTextFillColor: '-webkit-text-fill-color',
                webkitBackgroundClip: '-webkit-background-clip'
            };

            Object.keys(currentStyles).forEach(prop => {
                const val = currentStyles[prop];
                if (val === '' || val === undefined || val === null) return;

                if (prop === 'webkitTextFillColor') {
                    previewBox.style.setProperty('-webkit-text-fill-color', val);
                } else if (prop === 'webkitBackgroundClip') {
                    previewBox.style.setProperty('-webkit-background-clip', val);
                } else {
                    try {
                        previewBox.style[prop] = val;
                    } catch(e) {}
                }
            });

            updateCssOutput();
            updateHtmlPreview();
            updatePreviewDimensions();
        }

        function camelToKebab(str) {
            return str.replace(/[A-Z]/g, m => `-${m.toLowerCase()}`);
        }

        function updateCssOutput() {
            const defaults = getDefaultStyles();
            const lines = [];
            Object.entries(currentStyles).forEach(([key, value]) => {
                if (value === '' || value === undefined || value === null) return;
                
                let cssProp;
                if (key === 'webkitTextFillColor') cssProp = '-webkit-text-fill-color';
                else if (key === 'webkitBackgroundClip') cssProp = '-webkit-background-clip';
                else cssProp = camelToKebab(key);
                
                lines.push(`    ${cssProp}: ${value};`);
            });
            cssOutput.value = `#preview-box {\n${lines.join('\n')}\n}`;
        }

        function updateHtmlPreview() {
            const text = customTextInput ? (customTextInput.value || 'K3N4N V6.0') : 'K3N4N V6.0';
            const inlineStyles = [];
            Object.entries(currentStyles).forEach(([key, value]) => {
                if (value === '' || value === undefined || value === null) return;
                let cssProp;
                if (key === 'webkitTextFillColor') cssProp = '-webkit-text-fill-color';
                else if (key === 'webkitBackgroundClip') cssProp = '-webkit-background-clip';
                else cssProp = camelToKebab(key);
                inlineStyles.push(`${cssProp}: ${value}`);
            });
            htmlPreviewArea.textContent = `<div id="preview-box" style="${inlineStyles.join('; ')}">\n  ${text}\n</div>`;
        }

        function updatePreviewDimensions() {
            const rect = previewBox.getBoundingClientRect();
            const dimEl = $('previewDimensions');
            if(dimEl) dimEl.textContent = `${Math.round(rect.width)} × ${Math.round(rect.height)}`;
        }

        // ===== HİSTORY SİSTEMİ =====
        function saveToHistory() {
            history = history.slice(0, historyIndex + 1);
            history.push(JSON.parse(JSON.stringify(currentStyles)));
            if (history.length > MAX_HISTORY) history.shift();
            historyIndex = history.length - 1;
            updateHistoryButtons();
        }

        function updateHistoryButtons() {
            const undoBtn = document.querySelector('[data-action="undo"]');
            const redoBtn = document.querySelector('[data-action="redo"]');
            if (undoBtn) undoBtn.disabled = historyIndex <= 0;
            if (redoBtn) redoBtn.disabled = historyIndex >= history.length - 1;
        }

        function undo() {
            if (historyIndex > 0) {
                historyIndex--;
                currentStyles = JSON.parse(JSON.stringify(history[historyIndex]));
                applyStyles();
                updateHistoryButtons();
                showToast('Geri alındı', 'info');
            }
        }

        function redo() {
            if (historyIndex < history.length - 1) {
                historyIndex++;
                currentStyles = JSON.parse(JSON.stringify(history[historyIndex]));
                applyStyles();
                updateHistoryButtons();
                showToast('İleri alındı', 'info');
            }
        }

        // ===== RANDOM FONKSİYONLAR =====
        function rndHex() { return '#' + Math.floor(Math.random() * 16777215).toString(16).padStart(6, '0'); }
        function rndInt(min, max) { return Math.floor(Math.random() * (max - min + 1)) + min; }
        function rndFloat(min, max, dec = 1) { return parseFloat((Math.random() * (max - min) + min).toFixed(dec)); }
        function rndItem(arr) { return arr[Math.floor(Math.random() * arr.length)]; }

        const allFonts = [
            "'Poppins', sans-serif", "'Inter', sans-serif", "'Space Grotesk', sans-serif",
            "'VT323', monospace", "'Press Start 2P', monospace", "'Orbitron', sans-serif",
            "'Roboto Mono', monospace", "'JetBrains Mono', monospace", "'Lobster', cursive",
            "'Kaushan Script', cursive", "'Fira Code', monospace", "Georgia, serif",
            "'Courier New', monospace", "Impact, sans-serif"
        ];

        function randomFont() {
            updateStyle('fontFamily', rndItem(allFonts));
            updateStyle('fontSize', rndInt(18, 42), 'px');
            updateStyle('fontWeight', rndItem(['300', '400', '500', '600', '700', '800', '900']));
            showToast('Yazı tipi randomlandı');
        }
        function randomColor() {
            updateStyle('color', rndHex());
            showToast('Yazı rengi değişti');
        }
        function randomTextShadow() {
            const count = rndInt(1, 3);
            let shadows = [];
            for (let i = 0; i < count; i++) {
                shadows.push(`${rndInt(-8, 8)}px ${rndInt(-8, 8)}px ${rndInt(0, 15)}px ${rndHex()}`);
            }
            currentStyles.textShadow = shadows.join(', ');
            applyStyles();
            saveToHistory();
            showToast('Yazı gölgesi oluşturuldu');
        }
        function randomTextDecoration() {
            updateStyle('textDecorationLine', rndItem(['none', 'underline', 'overline', 'line-through']));
            updateStyle('textDecorationStyle', rndItem(['solid', 'double', 'dotted', 'dashed', 'wavy']));
        }
        function randomSpacing() {
            updateStyle('letterSpacing', rndFloat(-2, 5), 'px');
            updateStyle('wordSpacing', rndFloat(-2, 10), 'px');
        }
        function randomAlign() {
            updateStyle('textAlign', rndItem(['left', 'center', 'right', 'justify']));
        }
        function randomLineHeight() {
            const val = rndFloat(0.8, 2.5);
            currentStyles.lineHeight = val.toString();
            if($('lineHeightRange')) $('lineHeightRange').value = val;
            applyStyles();
            saveToHistory();
        }
        function randomTextTransform() {
            updateStyle('textTransform', rndItem(['none', 'uppercase', 'lowercase', 'capitalize']));
        }

        // — Background Randoms —
        function randomBgColor() {
            updateStyle('backgroundColor', rndHex());
            currentStyles.backgroundImage = 'none';
            currentStyles.webkitBackgroundClip = '';
            currentStyles.webkitTextFillColor = '';
            currentStyles.backgroundClip = 'border-box';
            applyStyles();
            saveToHistory();
        }
        function randomGradient() {
            const count = rndInt(2, 4);
            gradientColors = [];
            for (let i = 0; i < count; i++) {
                gradientColors.push({ color: rndHex(), stop: Math.round(i / (count - 1) * 100) });
            }
            if($('gradientAngle')) $('gradientAngle').value = rndInt(0, 360);
            if($('gradientType')) $('gradientType').value = rndItem(['linear', 'radial', 'conic']);
            initGradientPickers('gradientColors', gradientColors, 'bg');
            updateGradient();
        }
        function randomBgGif() {
            const gifs = [
                'https://media.giphy.com/media/l0MYt5jPR6QX5pnqM/giphy.gif',
                'https://media.giphy.com/media/3o7btPCcdNniyf0ArS/giphy.gif',
                'https://media.giphy.com/media/xT9IgzoKnwFNmISR8I/giphy.gif'
            ];
            currentStyles.backgroundImage = `url(${rndItem(gifs)})`;
            currentStyles.backgroundSize = 'cover';
            currentStyles.webkitBackgroundClip = '';
            currentStyles.webkitTextFillColor = '';
            currentStyles.backgroundClip = 'border-box';
            applyStyles();
            saveToHistory();
        }
        function randomBgPosition() {
            const positions = ['center', 'top', 'bottom', 'left', 'right', '25%', '75%'];
            updateStyle('backgroundPositionX', rndItem(positions));
            updateStyle('backgroundPositionY', rndItem(positions));
        }
        
        // — Border Randoms —
        function randomMultiBorder() {
            const styles = ['solid', 'dashed', 'dotted', 'double', 'groove', 'ridge'];
            ['borderTop', 'borderBottom', 'borderLeft', 'borderRight'].forEach(side => {
                currentStyles[side] = `${rndInt(1, 5)}px ${rndItem(styles)} ${rndHex()}`;
            });
            applyStyles();
            saveToHistory();
        }
        function randomOutline() {
            currentStyles.outlineWidth = `${rndInt(1, 5)}px`;
            currentStyles.outlineStyle = rndItem(['solid', 'dashed', 'dotted']);
            currentStyles.outlineColor = rndHex();
            currentStyles.outlineOffset = `${rndInt(0, 5)}px`;
            applyStyles();
            saveToHistory();
        }

        // — Transform & Shadow —
        function randomTransform() {
            if($('rotateRange')) {
                $('rotateRange').value = rndInt(-20, 20);
                $('rotate').value = $('rotateRange').value;
            }
            if($('scaleRange')) $('scaleRange').value = rndFloat(0.8, 1.2);
            $('#skewX, #skewY').forEach(el => { if(el) el.value = rndInt(-10, 10); });
            $('#translateX, #translateY').forEach(el => { if(el) el.value = rndInt(-20, 20); });
            updateTransform();
            showToast('Dönüşüm oluştu');
        }
        function randomBoxShadow() {
             const count = rndInt(1, 3);
            let shadows = [];
            for (let i = 0; i < count; i++) {
                const inset = Math.random() > 0.8 ? 'inset ' : '';
                shadows.push(`${inset}${rndInt(-15, 15)}px ${rndInt(-15, 15)}px ${rndInt(5, 30)}px ${rndHex()}`);
            }
            currentStyles.boxShadow = shadows.join(', ');
            applyStyles();
            saveToHistory();
        }

        // — Animasyonlar —
        const animationKeyframesMap = {
            bounce: `@keyframes bounce { 0%,20%,50%,80%,100% { transform: translateY(0); } 40% { transform: translateY(-30px); } 60% { transform: translateY(-15px); } }`,
            pulse: `@keyframes pulse { 0% { transform: scale(1); } 50% { transform: scale(1.08); } 100% { transform: scale(1); } }`,
            shake: `@keyframes shake { 0%,100% { transform: translateX(0); } 10%,30%,50%,70%,90% { transform: translateX(-8px); } 20%,40%,60%,80% { transform: translateX(8px); } }`,
            fadeIn: `@keyframes fadeIn { 0% { opacity: 0; } 100% { opacity: 1; } }`,
            fadeOut: `@keyframes fadeOut { 0% { opacity: 1; } 100% { opacity: 0; } }`,
            rubberBand: `@keyframes rubberBand { 0%,100% { transform: scaleX(1) scaleY(1); } 30% { transform: scaleX(1.25) scaleY(0.75); } 40% { transform: scaleX(0.75) scaleY(1.25); } 50% { transform: scaleX(1.15) scaleY(0.85); } }`,
            neonPulse: `@keyframes neonPulse { 0%,100% { box-shadow: 0 0 5px #fff, 0 0 10px #fff, 0 0 20px #0ff, 0 0 40px #0ff; } 50% { box-shadow: 0 0 10px #fff, 0 0 20px #fff, 0 0 40px #0ff, 0 0 80px #0ff; } }`
        };

        let injectedKeyframes = new Set();
        function injectKeyframes(name) {
            if (injectedKeyframes.has(name)) return;
            const kf = animationKeyframesMap[name];
            if (kf) {
                const style = document.createElement('style');
                style.textContent = kf;
                style.setAttribute('data-keyframe', name);
                document.head.appendChild(style);
                injectedKeyframes.add(name);
            }
        }

        function applyAnimation(name) {
            injectKeyframes(name);
            currentStyles.animationName = name;
            const dur = $('animationDurationRange').value;
            currentStyles.animationDuration = dur + 's';
            currentStyles.animationTimingFunction = $('animationTimingFunction').value;
            currentStyles.animationIterationCount = $('animationIterationCount').value;
            
            // Animasyonu yeniden başlat
            previewBox.style.animation = 'none';
            previewBox.offsetHeight; // trigger reflow
            applyStyles();
            saveToHistory();
        }

        function randomAnimation() {
            const names = Object.keys(animationKeyframesMap);
            const name = rndItem(names);
            $('presetAnimation').value = name;
            $('animationDurationRange').value = rndFloat(0.5, 2.5);
            applyAnimation(name);
            showToast(`Animasyon: ${name}`);
        }

        // — Clip Path —
        function randomClipPath() {
            const paths = [
                'circle(50% at 50% 50%)',
                'polygon(50% 0%, 100% 50%, 50% 100%, 0% 50%)',
                'polygon(25% 0%, 75% 0%, 100% 50%, 75% 100%, 25% 100%, 0% 50%)',
                'polygon(50% 0%, 61% 35%, 98% 35%, 68% 57%, 79% 91%, 50% 70%, 21% 91%, 32% 57%, 2% 35%, 39% 35%)'
            ];
            updateStyle('clipPath', rndItem(paths));
            showToast('Clip-path oluşturuldu');
        }

        // — Gradyan Yazı —
        function randomTextGradient() {
            const count = rndInt(2, 4);
            textGradientColors = [];
            for (let i = 0; i < count; i++) {
                textGradientColors.push({ color: rndHex(), stop: Math.round(i / (count - 1) * 100) });
            }
            $('textGradientAngle').value = rndInt(0, 360);
            $('textGradientType').value = rndItem(['linear', 'radial']);
            initGradientPickers('textGradientColors', textGradientColors, 'text');
            updateTextGradient();
        }

        // — Filter —
        function randomFilter() {
            $('filterBlurRange').value = rndInt(0, 3);
            $('filterBrightnessRange').value = rndInt(80, 150);
            $('filterContrastRange').value = rndInt(80, 150);
            $('filterSaturateRange').value = rndInt(50, 200);
            $('filterHueRotateRange').value = rndInt(0, 360);
            $('filterInvertRange').value = rndInt(0, 20);
            updateFilter();
            showToast('Filtreler oluşturuldu');
        }

        // — Palet —
        function generatePalette() {
            const base = pickers.baseColor ? pickers.baseColor.color.hexString : '#64ffda';
            const type = $('paletteType').value;
            const size = parseInt($('paletteSize').value) || 5;
            let colors = [];

            try {
                if (type === 'monochromatic') {
                    colors = chroma.scale([chroma(base).darken(2), base, chroma(base).brighten(2)]).colors(size);
                } else if (type === 'analogous') {
                    colors = chroma.scale([chroma(base), chroma(base).set('hsl.h', '+30'), chroma(base).set('hsl.h', '+60')]).colors(size);
                } else if (type === 'complementary') {
                    colors = [base, chroma(base).set('hsl.h', '+180').hex()];
                } else {
                    // Fallback random
                    for(let i=0; i<size; i++) colors.push(rndHex());
                }
            } catch(e) {
                for(let i=0; i<size; i++) colors.push(rndHex());
            }

            const preview = $('palettePreview');
            if(preview) {
                preview.innerHTML = colors.map(c =>
                    `<div class="palette-color" style="background-color:${c};" data-color="${c}" title="${c}">
                        <span class="tooltip">${c}</span>
                    </div>`
                ).join('');

                preview.querySelectorAll('.palette-color').forEach(el => {
                    el.addEventListener('click', () => {
                        const col = el.dataset.color;
                        navigator.clipboard.writeText(col).then(() => {
                            showToast(`Renk kopyalandı: ${col}`);
                        }).catch(() => {});
                    });
                });
            }
        }

        // — Temalar —
        function applyThemePreset(theme) {
            currentStyles = getDefaultStyles();
            
            if (theme === 'neon') {
                Object.assign(currentStyles, {
                    backgroundColor: '#0a0a2e', color: '#0ff', fontFamily: "'Orbitron', sans-serif",
                    textShadow: '0 0 10px #0ff, 0 0 20px #0ff', fontSize: '36px',
                    borderColor: '#0ff', borderWidth: '2px', borderStyle: 'solid'
                });
            } else if (theme === 'minimal') {
                Object.assign(currentStyles, {
                    backgroundColor: '#fafafa', color: '#333333', fontFamily: "'Inter', sans-serif",
                    boxShadow: '0 1px 3px rgba(0,0,0,0.04)', fontSize: '28px'
                });
            } else if (theme === 'vintage') {
                Object.assign(currentStyles, {
                    backgroundColor: '#f4e9d8', color: '#5c3317', fontFamily: "'Kaushan Script', cursive",
                    textShadow: '2px 2px 0px #d4a574', fontSize: '38px'
                });
            } else if (theme === 'glassmorphism') {
                Object.assign(currentStyles, {
                    backgroundColor: 'rgba(255,255,255,0.1)', backdropFilter: 'blur(12px)',
                    border: '1px solid rgba(255,255,255,0.2)', color: '#ffffff'
                });
            } else if (theme === 'neumorphism') {
                Object.assign(currentStyles, {
                    backgroundColor: '#e0e5ec', color: '#6b7b99',
                    boxShadow: '8px 8px 16px #b8bec7, -8px -8px 16px #ffffff',
                    borderRadius: '20px'
                });
            } else if (theme === 'cyberpunk') {
                Object.assign(currentStyles, {
                    backgroundColor: '#0d0221', color: '#ff2d6a', fontFamily: "'Press Start 2P', monospace",
                    textShadow: '0 0 8px #ff2d6a', fontSize: '22px'
                });
            } else if (theme === 'nature') {
                Object.assign(currentStyles, {
                    backgroundColor: '#e8f5e9', color: '#2d5016', fontFamily: "'Space Grotesk', sans-serif",
                    backgroundImage: 'linear-gradient(135deg, #e8f5e9 0%, #c8e6c9 100%)'
                });
            } else if (theme === 'ocean') {
                Object.assign(currentStyles, {
                    backgroundImage: 'linear-gradient(135deg, #0077b6, #023e8a)', color: '#ffffff'
                });
            } else if (theme === 'sunset') {
                Object.assign(currentStyles, {
                    backgroundImage: 'linear-gradient(135deg, #ff512f, #f09819)', color: '#ffffff'
                });
            } else if (theme === 'dark-elegant') {
                Object.assign(currentStyles, {
                    backgroundColor: '#1a1a2e', color: '#d4af37', fontFamily: "'Space Grotesk', sans-serif",
                    textShadow: '0 0 6px rgba(212,175,55,0.3)'
                });
            }
            applyStyles();
            saveToHistory();
            showToast(`Tema: ${theme}`);
        }

        // — Chaos Motoru —
        function autoGenerateStyles(mode) {
            const checks = {
                font: $('chaosFont') ? $('chaosFont').checked : true,
                bg: $('chaosBackground') ? $('chaosBackground').checked : true,
                border: $('chaosBorder') ? $('chaosBorder').checked : true,
                effects: $('chaosEffects') ? $('chaosEffects').checked : true,
                animation: $('chaosAnimation') ? $('chaosAnimation').checked : true,
                clip: $('chaosClip') ? $('chaosClip').checked : true,
                transform: $('chaosTransform') ? $('chaosTransform').checked : true,
                shadow: $('chaosBoxShadow') ? $('chaosBoxShadow').checked : true,
                textGradient: $('chaosTextGradient') ? $('chaosTextGradient').checked : true
            };

            if (checks.font) randomFont();
            if (checks.bg) { Math.random() > 0.5 ? randomGradient() : randomBgColor(); }
            if (checks.border) randomMultiBorder();
            if (checks.effects) randomFilter();
            if (checks.animation) randomAnimation();
            if (checks.clip && Math.random() > 0.6) randomClipPath();
            if (checks.transform) randomTransform();
            if (checks.shadow) randomBoxShadow();
            
            showToast(mode === 'chaos' ? '🔥 KAOS MODU 🔥' : 'Rastgele Stil Oluşturuldu');
        }

        // ===== EVENT LİSTENERLER =====

        // Header Actions
        $$('[data-action]').forEach(btn => {
            btn.addEventListener('click', () => {
                const action = btn.dataset.action;
                switch(action) {
                    case 'undo': undo(); break;
                    case 'redo': redo(); break;
                    case 'toggle-theme':
                        currentTheme = currentTheme === 'dark' ? 'light' : 'dark';
                        document.documentElement.setAttribute('data-theme', currentTheme);
                        const icon = btn.querySelector('i');
                        if(icon) icon.className = currentTheme === 'dark' ? 'fas fa-moon' : 'fas fa-sun';
                        showToast(`Tema: ${currentTheme === 'dark' ? 'Koyu' : 'Açık'}`, 'info');
                        break;
                    case 'reset-all':
                        currentStyles = getDefaultStyles();
                        previewBox.style.animation = 'none';
                        applyStyles();
                        saveToHistory();
                        showToast('Sıfırlandı', 'info');
                        break;
                    case 'download-css':
                        const blob = new Blob([cssOutput.value], {type:'text/css'});
                        const a = document.createElement('a');
                        a.href = URL.createObjectURL(blob); a.download = 'k3n4n-styles.css'; a.click();
                        URL.revokeObjectURL(url);
                        break;
                    case 'download-html':
                        const html = `<!DOCTYPE html><html><head><style>${cssOutput.value}</style></head><body><div id="preview-box">K3N4N V6.0</div></body></html>`;
                        const blob2 = new Blob([html], {type:'text/html'});
                        const b = document.createElement('a');
                        b.href = URL.createObjectURL(blob2); b.download = 'k3n4n-preview.html'; b.click();
                        break;
                    case 'export-styles':
                        const data = JSON.stringify(currentStyles, null, 2);
                        const blob3 = new Blob([data], {type:'application/json'});
                        const c = document.createElement('a');
                        c.href = URL.createObjectURL(blob3); c.download = 'styles.json'; c.click();
                        break;
                    case 'import-styles': $('import-styles').click(); break;
                }
            });
        });

        // Sidebar Toggle Mobile
        if($('sidebarToggle')) $('sidebarToggle').addEventListener('click', () => {
             $('sidebar').classList.toggle('open');
             if($('sidebarOverlay')) $('sidebarOverlay').classList.toggle('visible');
        });
        if($('sidebarOverlay')) $('sidebarOverlay').addEventListener('click', () => {
            $('sidebar').classList.remove('open');
            $('sidebarOverlay').classList.remove('visible');
        });

        // Style Target Buttons
        $$('[data-style-target]').forEach(btn => {
            btn.addEventListener('click', () => {
                const target = btn.dataset.styleTarget;
                if (target === 'random-font') randomFont();
                else if (target === 'random-color') randomColor();
                else if (target === 'random-text-shadow') randomTextShadow();
                else if (target === 'random-text-decoration') randomTextDecoration();
                else if (target === 'random-spacing') randomSpacing();
                else if (target === 'random-align') randomAlign();
                else if (target === 'random-line-height') randomLineHeight();
                else if (target === 'random-text-transform') randomTextTransform();
                else if (target === 'random-bg-color') randomBgColor();
                else if (target === 'random-gradient') randomGradient();
                else if (target === 'random-bg-gif') randomBgGif();
                else if (target === 'random-bg-position') randomBgPosition();
                else if (target === 'random-multi-border') randomMultiBorder();
                else if (target === 'random-outline') randomOutline();
                else if (target === 'random-transform') randomTransform();
                else if (target === 'random-box-shadow') randomBoxShadow();
                else if (target === 'random-animation') randomAnimation();
                else if (target === 'random-clip-path') randomClipPath();
                else if (target === 'random-text-gradient') randomTextGradient();
                else if (target === 'random-filter') randomFilter();
                else if (target === 'generate-palette') generatePalette();
                else if (target === 'auto-generate') autoGenerateStyles('random');
                else if (target === 'max-chaos') autoGenerateStyles('chaos');
                else if (target.startsWith('auto-theme-')) applyThemePreset(target.replace('auto-theme-', ''));
                // Reset handling
                else if (target === 'reset-transform') {
                    $('#rotate, #rotateRange').forEach(el=>el.value=0);
                    $('#scaleRange').val(1);
                    $('#skewX, #skewY, #translateX, #translateY').forEach(el=>el.value=0);
                    updateTransform();
                }
                else if (target === 'reset-clip') { updateStyle('clipPath', 'none'); }
                else if (target === 'stop-animation') {
                    currentStyles.animationName = 'none'; previewBox.style.animation='none';
                    applyStyles();
                }
                else if (target === 'reset-text-fill') {
                    currentStyles.backgroundImage='none';
                    currentStyles.webkitBackgroundClip='';
                    currentStyles.webkitTextFillColor='';
                    currentStyles.backgroundClip='border-box';
                    applyStyles();
                }
                else if (target === 'reset-filters') {
                    $('#filterBlurRange, #filterSaturateRange, #filterContrastRange, #filterHueRotateRange, #filterInvertRange, #filterSepiaRange, #filterGrayscaleRange, #backdropBlurRange').forEach(el => {
                        if(el.id === 'filterBrightnessRange') el.value = 100; else el.value = 0;
                    });
                    updateFilter();
                }
                else if (target === 'random-palette') {
                    if(pickers.baseColor) { pickers.baseColor.color.hexString = rndHex(); generatePalette(); }
                }
            });
        });

        // Direct Inputs
        $$('[data-style-prop]').forEach(input => {
            const handler = () => {
                const prop = input.dataset.styleProp;
                const unit = input.dataset.styleUnit || '';
                if(prop === 'transform') updateTransform();
                else if(prop === 'filter') updateFilter();
                else updateStyle(prop, input.value, unit);
            };
            input.addEventListener('input', handler);
            input.addEventListener('change', handler);
        });

        // Inputs mapped to complex functions
        if($('textShadowX')) $('textShadowX').addEventListener('input', () => {
                updateComplexStyle('textShadowColor', pickers.textShadowColor ? pickers.textShadowColor.color.hexString : '#000');
            });
        if($('textShadowY')) $('textShadowY').addEventListener('input', () => {
                updateComplexStyle('textShadowColor', pickers.textShadowColor ? pickers.textShadowColor.color.hexString : '#000');
            });
        if($('textShadowBlur')) $('textShadowBlur').addEventListener('input', () => {
                updateComplexStyle('textShadowColor', pickers.textShadowColor ? pickers.textShadowColor.color.hexString : '#000');
            });

        $('#boxShadowX, #boxShadowY, #boxShadowBlur, #boxShadowSpread').forEach(el => el && el.addEventListener('input', updateBoxShadow));
        if($('boxShadowInset')) $('boxShadowInset').addEventListener('change', updateBoxShadow);

        $('#outlineWidth, #outlineStyle').forEach(el => el && el.addEventListener('input', () => {
             updateComplexStyle('outlineColor', pickers.outlineColor ? pickers.outlineColor.color.hexString : '#fff');
        }));

        // Range Syncs
        function syncRange(rangeId, valId, unit, cb) {
            const r = $(rangeId);
            const v = $(valId);
            if(r && v) {
                r.addEventListener('input', () => {
                    v.textContent = r.value + unit;
                    if(cb) cb(r.value);
                });
            }
        }
        
        syncRange('fontSizeRange', 'fontSizeVal', 'px', v => {
            if($('fontSize')) $('fontSize').value = v;
            updateStyle('fontSize', v, 'px');
        });

        if($('fontSize')) $('fontSize').addEventListener('input', () => {
            $('fontSizeRange').value = $('fontSize').value;
            $('fontSizeVal').textContent = $('fontSize').value + 'px';
            updateStyle('fontSize', $('fontSize').value, 'px');
        });

        syncRange('fontWeightRange', 'fontWeightVal', '', v => {
            if($('fontWeight')) $('fontWeight').value = v;
            updateStyle('fontWeight', v);
        });
        if($('fontWeight')) $('fontWeight').addEventListener('change', () => {
            $('fontWeightRange').value = $('fontWeight').value;
            $('fontWeightVal').textContent = $('fontWeight').value;
            updateStyle('fontWeight', $('fontWeight').value);
        });

        syncRange('lineHeightRange', 'lineHeightVal', '', v => {currentStyles.lineHeight=v; applyStyles(); saveToHistory();});
        syncRange('backgroundOpacityRange', 'bgOpacityVal', '', v => {currentStyles.opacity=v; applyStyles(); saveToHistory();});
        syncRange('textOpacityRange', 'textOpacityVal', '', v => {currentStyles.opacity=v; applyStyles(); saveToHistory();});
        
        syncRange('rotateRange', 'rotateVal', '°', v => {
            if($('rotate')) $('rotate').value = v;
            updateTransform();
        });
        syncRange('scaleRange', 'scaleVal', '', updateTransform);
        
        syncRange('borderRadiusAll', 'borderRadiusVal', 'px', v => {
            currentStyles.borderTopLeftRadius=v+'px';
            currentStyles.borderTopRightRadius=v+'px';
            currentStyles.borderBottomLeftRadius=v+'px';
            currentStyles.borderBottomRightRadius=v+'px';
            if($('#borderRadiusTopLeft')) $('#borderRadiusTopLeft').value = v;
            applyStyles();
            saveToHistory();
        });

        syncRange('animationDurationRange', 'animDurationVal', 's', v => {currentStyles.animationDuration=v+'s';applyStyles();saveToHistory();});

        // Filter Ranges
        $('#filterBlurRange, #filterBrightnessRange, #filterContrastRange, #filterSaturateRange, #filterHueRotateRange, #filterInvertRange, #filterSepiaRange, #filterGrayscaleRange, #backdropBlurRange').forEach(el => {
            if(el) el.addEventListener('input', updateFilter);
        });

        // Gradients & Transforms specific inputs
        $('#skewX, #skewY, #translateX, #translateY').forEach(el => el && el.addEventListener('input', updateTransform));
        $('#gradientAngle, #gradientType').forEach(el => el && el.addEventListener('change', updateGradient));
        $('#textGradientAngle, #textGradientType').forEach(el => el && el.addEventListener('change', updateTextGradient));
        
        // Text & Image Fill
        if($('backgroundImageUrl')) $('backgroundImageUrl').addEventListener('input', updateBackgroundImageUrl);
        if($('textImageFill')) $('textImageFill').addEventListener('input', updateTextImageFill);
        if($('#paddingLeft, #paddingRight, #paddingTop, #paddingBottom, #paddingUnit').some(x=>x)) {
             $$('#paddingLeft, #paddingRight, #paddingTop, #paddingBottom, #paddingUnit').forEach(el => el.addEventListener('input', updatePadding));
        }

        // Preview Text
        if(customTextInput) {
            customTextInput.addEventListener('input', () => {
                previewBox.textContent = customTextInput.value || 'K3N4N V6.0';
                if($('charCount')) $('charCount').textContent = `${customTextInput.value.length}/100`;
                updateHtmlPreview();
            });
        }

        // Accordion Panels
        $$('.panel-header').forEach(header => {
            header.addEventListener('click', () => header.closest('.panel').classList.toggle('expanded'));
        });

        // Tabs
        $$('.output-tab').forEach(tab => {
            tab.addEventListener('click', () => {
                $$('.output-tab').forEach(t => t.classList.remove('active'));
                $$('.tab-content').forEach(c => c.classList.remove('active'));
                tab.classList.add('active');
                if ($(tab.dataset.tab)) $(tab.dataset.tab).classList.add('active');
            });
        });

        // Output Buttons
        if($('copy-css-btn')) $('copy-css-btn').addEventListener('click', () => {
            navigator.clipboard.writeText(cssOutput.value).then(() => {
                showToast('CSS kopyalandı');
                if($('copy-success')) {
                    $('copy-success').classList.add('visible');
                    setTimeout(()=>$('copy-success').classList.remove('visible'), 2000);
                }
            }).catch(()=>showToast('Hata', 'error'));
        });

        if($('applyCustomCss')) $('applyCustomCss').addEventListener('click', () => {
            try {
                const css = cssInputArea.value.trim();
                if(!css) return;
                const style = document.createElement('style');
                style.textContent = `#preview-box { ${css} }`;
                document.head.appendChild(style);
                showToast('Özel CSS uygulandı');
            } catch(e) { showToast('Geçersiz CSS', 'error'); }
        });

        // Presets
        if($('presetAnimation')) $('presetAnimation').addEventListener('change', () => {
            if($("presetAnimation").value) applyAnimation($('presetAnimation').value);
        });
        if($('presetClipPath')) $('presetClipPath').addEventListener('change', () => {
            if($('presetClipPath').value) updateStyle('clipPath', $('presetClipPath').value);
        });

        // Keyframes
        if($('applyKeyframesBtn')) $('applyKeyframesBtn').addEventListener('click', () => {
            const kf = $('animationKeyframes').value.trim();
            if(kf) {
                const nameMatch = kf.match(/@keyframes\s+([a-zA-Z0-9_-]+)/);
                if(nameMatch) {
                    const name = nameMatch[1];
                    const style = document.createElement('style');
                    style.textContent = kf;
                    document.head.appendChild(style);
                    applyAnimation(name);
                    showToast(`Keyframes: ${name}`);
                } else showToast('Keyframes adı bulunamadı', 'error');
            }
        });

        // Search
        if($('panelSearch')) $('panelSearch').addEventListener('input', e => {
            const q = e.target.value.toLowerCase();
            $$('.panel').forEach(p => {
                const t = (p.querySelector('.panel-title')||{}).textContent.toLowerCase() || '';
                p.style.display = t.includes(q) ? '' : 'none';
            });
        });

        // Imports
        if($('import-styles')) $('import-styles').addEventListener('change', e => {
            const file = e.target.files[0];
            if(!file) return;
            const reader = new FileReader();
            reader.onload = ev => {
                try {
                    const imported = JSON.parse(ev.target.result);
                    currentStyles = { ...getDefaultStyles(), ...imported };
                    applyStyles();
                    saveToHistory();
                    showToast('İçe aktarım başarılı');
                } catch(err) { showToast('Dosya hatası', 'error'); }
            };
            reader.readAsText(file);
            e.target.value='';
        });

        // Keyboard Shortcuts
        document.addEventListener('keydown', e => {
            if((e.ctrlKey||e.metaKey)&&e.key==='z') { e.preventDefault(); undo(); }
            if((e.ctrlKey||e.metaKey)&&(e.key==='y'||(e.key==='z'&&e.shiftKey))) { e.preventDefault(); redo(); }
        });

        // ===== INIT =====
        // İlk açılışta örnek palet
        initGradientPickers('gradientColors', gradientColors, 'bg');
        initGradientPickers('textGradientColors', textGradientColors, 'text');
        setTimeout(generatePalette, 500); // Wait for iro.js
        applyStyles();
        saveToHistory();

        // Resize Observer
        const resizeObserver = new ResizeObserver(() => updatePreviewDimensions());
        resizeObserver.observe(previewBox);

        console.log('K3N4N V6.0 Başlatıldı');
    })();
    </script>
</body>
</html>
```
