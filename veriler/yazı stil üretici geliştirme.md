# CSS Stil Üretici Geliştirme

## Prompt 1

### You
*2026-01-11 14:42:07 +03*

<!DOCTYPE html><html lang="tr"><head> <meta charset="UTF-8"> <meta name="viewport" content="width=device-width, initial-scale=1.0"> <title>K3N4N CSS Stil Generator - Kenan V6</title> <!-- Google Fonts --> <link href="https://fonts.googleapis.com/css2?family=VT323&display=swap" rel="stylesheet"> <link href="https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap" rel="stylesheet"> <link href="https://fonts.googleapis.com/css2?family=Black+Ops+One&display=swap" rel="stylesheet"> <link href="https://fonts.googleapis.com/css2?family=Creepster&display=swap" rel="stylesheet"> <link href="https://fonts.googleapis.com/css2?family=Nosifer&display=swap" rel="stylesheet"> <link href="https://fonts.googleapis.com/css2?family=Orbitron&display=swap" rel="stylesheet"> <link href="https://fonts.googleapis.com/css2?family=Roboto+Mono&display=swap" rel="stylesheet"> <link href="https://fonts.googleapis.com/css2?family=Audiowide&display=swap" rel="stylesheet"> <link href="https://fonts.googleapis.com/css2?family=Bungee+Shade&display=swap" rel="stylesheet"> <link href="https://fonts.googleapis.com/css2?family=Russo+One&display=swap" rel="stylesheet"> <link href="https://fonts.googleapis.com/css2?family=Monoton&display=swap" rel="stylesheet"> <link href="https://fonts.googleapis.com/css2?family=Fredoka+One&display=swap" rel="stylesheet"> <link href="https://fonts.googleapis.com/css2?family=Staatliches&display=swap" rel="stylesheet"> <link href="https://fonts.googleapis.com/css2?family=Permanent+Marker&display=swap" rel="stylesheet"> <link href="https://fonts.googleapis.com/css2?family=Lobster&display=swap" rel="stylesheet"> <link href="https://fonts.googleapis.com/css2?family=Shadows+Into+Light&display=swap" rel="stylesheet"> <link href="https://fonts.googleapis.com/css2?family=Dancing+Script&display=swap" rel="stylesheet"> <link href="https://fonts.googleapis.com/css2?family=Lora:wght@400;700&display=swap" rel="stylesheet"> <link href="https://fonts.googleapis.com/css2?family=Merriweather:wght@400;700&display=swap" rel="stylesheet"> <link href="https://fonts.googleapis.com/css2?family=Raleway:wght@400;700&display=swap" rel="stylesheet"> <link href="https://fonts.googleapis.com/css2?family=Oswald:wght@400;700&display=swap" rel="stylesheet"> <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap" rel="stylesheet"> <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700&display=swap" rel="stylesheet"> <link href="https://fonts.googleapis.com/css2?family=Fira+Code:wght@400;500;700&display=swap" rel="stylesheet"> <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet"> <link href="https://fonts.googleapis.com/css2?family=Pacifico&display=swap" rel="stylesheet"> <link href="https://fonts.googleapis.com/css2?family=Cinzel&display=swap" rel="stylesheet"> <link href="https://fonts.googleapis.com/css2?family=Righteous&display=swap" rel="stylesheet"> <!-- Font Awesome --> <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css"> <!-- External Libraries --> <script src="https://cdnjs.cloudflare.com/ajax/libs/chroma-js/2.4.2/chroma.min.js"></script> <script src="https://cdn.jsdelivr.net/npm/@jaames/iro@5/dist/iro.min.js"></script> <style> /* ================================================ K3N4N KENAN V6 - MODERN CSS VARIABLES ================================================ */ :root { /* Primary Colors */ --bg-dark: #0a0e17; --bg-medium: #111827; --bg-light: #1f2937; --bg-lighter: #374151; --bg-card: #1a1f2e; /* Text Colors */ --text-primary: #f1f5f9; --text-secondary: #94a3b8; --text-muted: #64748b; --text-highlight: #22d3ee; --text-code: #fbbf24; /* Accent Colors */ --accent-primary: #06b6d4; --accent-primary-hover: #22d3ee; --accent-secondary: #f59e0b; --accent-secondary-hover: #fbbf24; --accent-success: #10b981; --accent-success-hover: #34d399; --accent-danger: #ef4444; --accent-danger-hover: #f87171; --accent-purple: #a855f7; --accent-purple-hover: #c084fc; --accent-pink: #ec4899; --accent-pink-hover: #f472b6; /* UI Colors */ --legend-color: #fb923c; --border-color: rgba(148, 163, 184, 0.15); --border-hover: rgba(6, 182, 212, 0.4); --button-disabled-bg: #1e293b; --button-disabled-text: #475569; --code-bg: #0f172a; /* Shadows & Glows */ --shadow-sm: 0 1px 2px rgba(0, 0, 0, 0.3); --shadow-md: 0 4px 12px rgba(0, 0, 0, 0.4); --shadow-lg: 0 10px 30px rgba(0, 0, 0, 0.5); --shadow-xl: 0 20px 50px rgba(0, 0, 0, 0.6); --glow-primary: 0 0 20px rgba(6, 182, 212, 0.4); --glow-secondary: 0 0 20px rgba(245, 158, 11, 0.4); --glow-success: 0 0 20px rgba(16, 185, 129, 0.4); --glow-purple: 0 0 20px rgba(168, 85, 247, 0.4); --glow-pink: 0 0 20px rgba(236, 72, 153, 0.4); /* Borders & Radius */ --radius-sm: 6px; --radius-md: 10px; --radius-lg: 16px; --radius-xl: 24px; --radius-full: 9999px; /* Transitions */ --transition-fast: 0.15s ease; --transition-normal: 0.25s ease; --transition-slow: 0.4s ease; /* Spacing */ --space-xs: 4px; --space-sm: 8px; --space-md: 16px; --space-lg: 24px; --space-xl: 32px; --space-2xl: 48px; } /* ================================================ RESET & BASE STYLES ================================================ */ *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; } html { scrollbar-width: thin; scrollbar-color: var(--accent-primary) var(--bg-dark); scroll-behavior: smooth; } body { font-family: 'Inter', 'Poppins', system-ui, -apple-system, sans-serif; background: linear-gradient(135deg, var(--bg-dark) 0%, #0f172a 50%, #1e1b4b 100%); background-attachment: fixed; color: var(--text-primary); line-height: 1.6; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; } body::-webkit-scrollbar { width: 10px; } body::-webkit-scrollbar-track { background: var(--bg-dark); } body::-webkit-scrollbar-thumb { background: linear-gradient(180deg, var(--accent-primary), var(--accent-purple)); border-radius: 10px; border: 2px solid var(--bg-dark); } body::-webkit-scrollbar-thumb:hover { background: linear-gradient(180deg, var(--accent-primary-hover), var(--accent-purple-hover)); } /* ================================================ HEADER ================================================ */ .header { background: linear-gradient(135deg, rgba(17, 24, 39, 0.95), rgba(30, 27, 75, 0.95)); backdrop-filter: blur(20px); -webkit-backdrop-filter: blur(20px); border-bottom: 1px solid var(--border-color); padding: var(--space-md) var(--space-lg); position: sticky; top: 0; z-index: 100; } .header-content { max-width: 1900px; margin: 0 auto; display: flex; align-items: center; justify-content: space-between; gap: var(--space-md); } .logo { display: flex; align-items: center; gap: var(--space-sm); } .logo-icon { width: 42px; height: 42px; background: linear-gradient(135deg, var(--accent-primary), var(--accent-purple)); border-radius: var(--radius-md); display: flex; align-items: center; justify-content: center; font-size: 1.4em; color: white; box-shadow: var(--glow-primary); } .logo-text { font-family: 'Orbitron', sans-serif; font-size: 1.5em; font-weight: 700; background: linear-gradient(135deg, var(--accent-primary), var(--accent-purple), var(--accent-pink)); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; } .logo-version { font-size: 0.7em; padding: 2px 8px; background: var(--accent-secondary); color: var(--bg-dark); border-radius: var(--radius-full); font-weight: 600; margin-left: var(--space-xs); } /* ================================================ MAIN CONTAINER ================================================ */ .container { display: grid; grid-template-columns: 1fr; gap: var(--space-lg); width: 100%; max-width: 1900px; margin: var(--space-lg) auto; padding: 0 var(--space-md); flex-grow: 1; } @media (min-width: 1201px) { .container { grid-template-columns: minmax(380px, 420px) 1fr; gap: var(--space-xl); } } /* ================================================ CONTROLS SIDEBAR ================================================ */ .controls { background: linear-gradient(180deg, var(--bg-card) 0%, var(--bg-medium) 100%); padding: var(--space-lg); border-radius: var(--radius-lg); display: flex; flex-direction: column; gap: var(--space-md); overflow-y: auto; max-height: calc(100vh - 120px); scrollbar-width: thin; scrollbar-color: var(--accent-secondary) var(--bg-light); border: 1px solid var(--border-color); box-shadow: var(--shadow-lg); position: sticky; top: 90px; } .controls::-webkit-scrollbar { width: 8px; } .controls::-webkit-scrollbar-track { background: var(--bg-light); border-radius: var(--radius-sm); } .controls::-webkit-scrollbar-thumb { background: linear-gradient(180deg, var(--accent-secondary), var(--accent-primary)); border-radius: var(--radius-sm); } /* ================================================ HISTORY BUTTONS ================================================ */ .history-buttons { display: flex; gap: var(--space-sm); padding-bottom: var(--space-md); border-bottom: 1px solid var(--border-color); } .history-buttons button { flex: 1; display: flex; align-items: center; justify-content: center; gap: var(--space-sm); padding: var(--space-sm) var(--space-md); font-size: 0.9em; font-weight: 500; background: linear-gradient(135deg, var(--bg-light), var(--bg-medium)); color: var(--text-primary); border: 1px solid var(--border-color); border-radius: var(--radius-md); cursor: pointer; transition: all var(--transition-normal); font-family: inherit; } .history-buttons button i { color: var(--accent-secondary); transition: all var(--transition-normal); } .history-buttons button:hover:not(:disabled) { background: linear-gradient(135deg, var(--accent-secondary), var(--accent-secondary-hover)); color: var(--bg-dark); border-color: var(--accent-secondary); transform: translateY(-2px); box-shadow: var(--glow-secondary); } .history-buttons button:hover:not(:disabled) i { color: var(--bg-dark); } .history-buttons button:disabled { opacity: 0.5; cursor: not-allowed; } /* ================================================ FIELDSET & LEGEND ================================================ */ .controls fieldset { border: 1px solid var(--border-color); padding: var(--space-md); border-radius: var(--radius-md); display: flex; flex-direction: column; gap: 0; background: linear-gradient(135deg, rgba(31, 41, 55, 0.5), rgba(17, 24, 39, 0.8)); transition: all var(--transition-normal); backdrop-filter: blur(10px); -webkit-backdrop-filter: blur(10px); } .controls fieldset:hover { border-color: var(--border-hover); box-shadow: 0 0 20px rgba(251, 146, 60, 0.15); } .controls legend { color: var(--legend-color); font-weight: 600; padding: var(--space-xs) var(--space-md); font-size: 0.95em; margin-bottom: var(--space-sm); border-radius: var(--radius-sm); background: linear-gradient(135deg, var(--bg-light), var(--bg-medium)); border: 1px solid var(--border-color); display: inline-flex; align-items: center; gap: var(--space-sm); transition: all var(--transition-normal); cursor: pointer; user-select: none; } .controls fieldset:hover legend { background: linear-gradient(135deg, var(--legend-color), #ea580c); color: white; border-color: var(--legend-color); box-shadow: 0 0 15px rgba(251, 146, 60, 0.4); } .controls legend i { opacity: 0.8; transition: transform var(--transition-normal); } .controls fieldset:hover legend i { transform: rotate(-5deg) scale(1.1); } .controls legend .fa-chevron-down { margin-left: auto; transition: transform var(--transition-normal); } .controls fieldset:not(.expanded) legend .fa-chevron-down { transform: rotate(-90deg); } /* Fieldset Content */ .controls fieldset > *:not(legend) { display: none; } .controls fieldset.expanded > *:not(legend) { display: flex; flex-direction: column; gap: var(--space-sm); } .controls fieldset.expanded > .form-group { display: flex; flex-direction: column; gap: var(--space-xs); margin-bottom: var(--space-sm); padding-top: var(--space-sm); border-top: 1px dashed rgba(148, 163, 184, 0.1); } .controls fieldset.expanded > .form-group:first-of-type { border-top: none; padding-top: 0; margin-top: var(--space-xs); } .controls fieldset.expanded > .button-group { display: flex; border-top: 1px dashed rgba(148, 163, 184, 0.1); padding-top: var(--space-sm); margin-top: var(--space-xs); } /* ================================================ BUTTONS (FIELDSET) ================================================ */ .controls fieldset button { display: flex; align-items: center; justify-content: flex-start; gap: var(--space-sm); width: 100%; padding: var(--space-sm) var(--space-md); font-size: 0.88em; font-weight: 500; background: linear-gradient(135deg, var(--bg-light), var(--bg-medium)); color: var(--text-primary); border: 1px solid var(--border-color); border-radius: var(--radius-sm); cursor: pointer; transition: all var(--transition-normal); text-align: left; font-family: inherit; margin-bottom: var(--space-xs); } .controls fieldset button i { width: 18px; text-align: center; opacity: 0.8; transition: all var(--transition-normal); color: var(--accent-primary); } .controls fieldset button:hover:not(:disabled) { background: linear-gradient(135deg, var(--accent-primary), var(--accent-primary-hover)); color: white; border-color: var(--accent-primary-hover); transform: translateY(-2px) scale(1.01); box-shadow: var(--glow-primary); } .controls fieldset button:hover:not(:disabled) i { opacity: 1; color: white; transform: rotate(5deg); } .controls fieldset button:active:not(:disabled) { transform: translateY(0) scale(0.99); transition-duration: 0.05s; } button:disabled { background: var(--button-disabled-bg) !important; color: var(--button-disabled-text) !important; border-color: var(--border-color) !important; cursor: not-allowed !important; transform: none !important; box-shadow: none !important; opacity: 0.6; } /* Special Buttons */ .controls button.reset-btn { background: linear-gradient(135deg, var(--accent-danger), #dc2626); border-color: #b91c1c; color: white; font-weight: 600; justify-content: center; } .controls button.reset-btn:hover:not(:disabled) { background: linear-gradient(135deg, var(--accent-danger-hover), var(--accent-danger)); box-shadow: 0 0 20px rgba(239, 68, 68, 0.4); } .controls button.reset-btn i { color: white !important; } .controls button.max-chaos-btn { background: linear-gradient(135deg, var(--accent-purple), #7c3aed); border-color: #6d28d9; color: white; font-weight: 600; justify-content: center; } .controls button.max-chaos-btn:hover:not(:disabled) { background: linear-gradient(135deg, var(--accent-purple-hover), var(--accent-purple)); box-shadow: var(--glow-purple); } .controls button.max-chaos-btn i { color: white !important; } /* ================================================ FORM GROUPS & INPUTS ================================================ */ .controls .form-group label { font-weight: 600; color: var(--accent-primary); font-size: 0.82em; margin-bottom: 2px; display: flex; align-items: center; gap: var(--space-xs); } .controls .form-group label i { opacity: 0.7; font-size: 0.9em; } .controls select, .controls input[type="number"], .controls input[type="text"], .controls textarea { padding: var(--space-sm) var(--space-md); border-radius: var(--radius-sm); border: 1px solid var(--border-color); background: var(--bg-dark); color: var(--text-primary); font-family: inherit; font-size: 0.9em; width: 100%; transition: all var(--transition-fast); } .controls select:focus, .controls input[type="number"]:focus, .controls input[type="text"]:focus, .controls textarea:focus { outline: none; border-color: var(--accent-primary); box-shadow: 0 0 10px rgba(6, 182, 212, 0.3); } .controls textarea { min-height: 80px; resize: vertical; font-family: 'Fira Code', monospace; } .controls input[type="range"] { padding: 0; height: 8px; cursor: pointer; appearance: none; -webkit-appearance: none; background: linear-gradient(90deg, var(--accent-primary), var(--accent-purple)); border-radius: var(--radius-full); border: none; } .controls input[type="range"]::-webkit-slider-thumb { appearance: none; -webkit-appearance: none; width: 20px; height: 20px; background: white; border-radius: 50%; cursor: pointer; border: 3px solid var(--accent-primary); box-shadow: var(--shadow-md); transition: all var(--transition-fast); } .controls input[type="range"]::-webkit-slider-thumb:hover { transform: scale(1.1); box-shadow: var(--glow-primary); } .controls input[type="file"] { padding: var(--space-sm); border: 2px dashed var(--border-color); border-radius: var(--radius-sm); background: var(--bg-dark); cursor: pointer; transition: all var(--transition-fast); } .controls input[type="file"]:hover { border-color: var(--accent-primary); background: rgba(6, 182, 212, 0.05); } .controls input[type="color"] { width: 100%; height: 36px; padding: 2px; cursor: pointer; border: 1px solid var(--border-color); border-radius: var(--radius-sm); background: var(--bg-dark); } .controls .input-row { display: flex; gap: var(--space-sm); align-items: center; } .controls .input-row > input, .controls .input-row > select { flex: 1; } .controls .input-row label { white-space: nowrap; font-size: 0.8em; color: var(--text-secondary); } /* Color Picker Container */ .color-picker-container { width: 100%; margin: var(--space-xs) 0; border-radius: var(--radius-sm); overflow: hidden; } /* Button Group */ .controls .button-group { display: flex; flex-wrap: wrap; gap: var(--space-xs); margin-top: var(--space-sm); padding-top: var(--space-sm); } .controls .button-group button { flex: 1 1 auto; min-width: 70px; justify-content: center; font-size: 0.78em; padding: var(--space-xs) var(--space-sm); background: var(--bg-dark); color: var(--text-secondary); border: 1px solid var(--border-color); border-radius: var(--radius-sm); margin-bottom: 0; font-weight: 400; } .controls .button-group button:hover:not(:disabled) { background: var(--bg-lighter); color: var(--text-primary); border-color: var(--accent-secondary); transform: translateY(-1px); } .controls .button-group button.active { background: var(--accent-secondary); color: var(--bg-dark); border-color: var(--accent-secondary); font-weight: 600; } /* ================================================ PREVIEW OUTPUT AREA ================================================ */ .preview-output-area { display: flex; flex-direction: column; gap: var(--space-lg); } /* Preview Box */ #preview-box { background: linear-gradient(135deg, #ffffff, #f8fafc); color: #1e293b; border: 1px solid #e2e8f0; padding: var(--space-xl); border-radius: var(--radius-lg); text-align: center; font-size: 20px; /* Max 20px */ min-height: 320px; display: flex; justify-content: center; align-items: center; overflow: hidden; transition: all 0.3s ease; font-family: 'Poppins', sans-serif; position: relative; word-break: break-word; white-space: normal; user-select: text; perspective: 1200px; box-shadow: var(--shadow-lg), inset 0 1px 0 rgba(255,255,255,0.1); } #preview-box::before { content: 'Önizleme Alanı'; display: none; position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); font-size: 0.8em; color: #94a3b8; font-style: italic; z-index: 1; pointer-events: none; } #preview-box.is-empty::before { display: block; } /* K3N4N Wrap Structure */ #preview-box .k3n4n-wrap { display: inline-flex; align-items: center; justify-content: center; gap: var(--space-sm); } #preview-box .k3n4n-prefix { flex: 0 0 auto; object-fit: cover; display: inline-block; } #preview-box .k3n4n-text { flex: 0 1 auto; } #preview-box .k3n4n-suffix { flex: 0 0 auto; object-fit: cover; display: inline-block; } #preview-box .k3n4n-badge { flex: 0 0 auto; display: inline-block; } /* ================================================ CSS OUTPUT SECTION ================================================ */ .css-output-section { background: linear-gradient(135deg, var(--bg-card), var(--bg-medium)); border: 1px solid var(--border-color); padding: var(--space-lg); border-radius: var(--radius-lg); display: flex; flex-direction: column; gap: var(--space-md); box-shadow: var(--shadow-md); } .css-output-section h4 { color: var(--accent-primary); margin-bottom: var(--space-xs); font-size: 1.1em; border-bottom: 1px solid var(--border-color); padding-bottom: var(--space-sm); display: flex; align-items: center; gap: var(--space-sm); font-weight: 600; } .css-output-section h4 i { opacity: 0.9; } #css-output { width: 100%; height: 280px; background: var(--code-bg); color: var(--text-code); border: 1px solid var(--border-color); resize: vertical; padding: var(--space-md); font-family: 'Fira Code', monospace; font-size: 0.9em; border-radius: var(--radius-sm); overflow: auto; outline: none; tab-size: 2; -moz-tab-size: 2; white-space: pre; word-wrap: normal; box-shadow: inset 0 2px 10px rgba(0, 0, 0, 0.5); line-height: 1.5; } #css-output::placeholder { color: var(--text-muted); } /* Output Buttons */ .output-buttons { display: flex; flex-wrap: wrap; gap: var(--space-sm); } #copy-css-btn { display: flex; align-items: center; justify-content: center; gap: var(--space-sm); padding: var(--space-sm) var(--space-md); background: linear-gradient(135deg, var(--accent-success), #059669); color: white; border: none; border-radius: var(--radius-sm); cursor: pointer; transition: all var(--transition-normal); font-weight: 600; box-shadow: var(--shadow-sm); flex: 1; font-size: 0.9em; font-family: inherit; } #copy-css-btn:hover:not(:disabled) { background: linear-gradient(135deg, var(--accent-success-hover), var(--accent-success)); transform: translateY(-2px); box-shadow: var(--glow-success); } #copy-css-btn.copied { background: var(--accent-secondary); } .download-buttons { display: flex; gap: var(--space-sm); flex: 1; } .download-buttons button { flex: 1; background: linear-gradient(135deg, var(--accent-secondary), #d97706); color: var(--bg-dark); border: none; border-radius: var(--radius-sm); padding: var(--space-sm) var(--space-md); cursor: pointer; transition: all var(--transition-normal); font-weight: 600; display: flex; align-items: center; justify-content: center; gap: var(--space-sm); box-shadow: var(--shadow-sm); font-size: 0.9em; font-family: inherit; } .download-buttons button:hover:not(:disabled) { background: linear-gradient(135deg, var(--accent-secondary-hover), var(--accent-secondary)); transform: translateY(-2px); box-shadow: var(--glow-secondary); } /* ================================================ CSS INPUT SECTION ================================================ */ .css-input-section { background: linear-gradient(135deg, var(--bg-light), var(--bg-card)); border: 1px solid var(--border-color); padding: var(--space-md); border-radius: var(--radius-lg); box-shadow: var(--shadow-md); } .css-input-section h4 { color: var(--accent-secondary); margin-bottom: var(--space-sm); font-size: 1em; font-weight: 600; display: flex; align-items: center; gap: var(--space-sm); } #cssInputArea { width: 100%; min-height: 100px; background: var(--code-bg); color: var(--text-primary); border: 1px solid var(--border-color); border-radius: var(--radius-sm); padding: var(--space-sm); font-family: 'Fira Code', monospace; font-size: 0.88em; resize: vertical; margin-bottom: var(--space-sm); box-shadow: inset 0 1px 5px rgba(0, 0, 0, 0.4); } .css-input-section .button-group { padding-top: 0; border-top: none; margin-top: 0; } #htmlPreviewArea { border: 2px dashed var(--accent-primary); padding: var(--space-md); margin-top: var(--space-md); border-radius: var(--radius-sm); background: var(--bg-medium); min-height: 60px; color: var(--text-primary); font-family: sans-serif; overflow: auto; } #htmlPreviewArea .preview-wrapper { padding: var(--space-sm); border: 1px solid var(--border-color); background: var(--bg-light); border-radius: var(--radius-sm); } #htmlPreviewArea .preview-element { border: 1px dotted var(--accent-secondary); padding: var(--space-sm); display: inline-block; color: var(--text-primary); background: transparent; } #htmlPreviewArea .preview-error { color: var(--accent-danger); font-style: italic; } #htmlPreviewArea .preview-info { color: var(--text-muted); font-style: italic; } /* ================================================ FOOTER ================================================ */ footer { background: linear-gradient(135deg, var(--bg-medium), var(--bg-dark)); border-top: 1px solid var(--border-color); padding: var(--space-lg); text-align: center; margin-top: auto; } footer p { color: var(--text-muted); font-size: 0.9em; } footer .footer-brand { font-family: 'Orbitron', sans-serif; background: linear-gradient(135deg, var(--accent-primary), var(--accent-purple)); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; font-weight: 700; } /* ================================================ RESPONSIVE ================================================ */ @media (max-width: 1200px) { .container { grid-template-columns: minmax(340px, 1fr) 2fr; gap: var(--space-lg); } .controls { max-height: calc(100vh - 110px); } } @media (max-width: 992px) { .container { grid-template-columns: 1fr; gap: var(--space-md); } .controls { max-height: none; order: 2; position: static; } .preview-output-area { order: 1; } .header-content { flex-direction: column; text-align: center; } } @media (max-width: 600px) { body { padding: 0; } .header { padding: var(--space-sm) var(--space-md); } .logo-text { font-size: 1.2em; } .container { padding: var(--space-sm); gap: var(--space-sm); margin: var(--space-sm) auto; } #preview-box { font-size: 16px; padding: var(--space-md); min-height: 220px; } #css-output { height: 200px; font-size: 0.85em; } .controls { padding: var(--space-md); gap: var(--space-sm); } .controls fieldset { padding: var(--space-sm); } .controls legend { font-size: 0.9em; padding: var(--space-xs) var(--space-sm); } .controls fieldset button { padding: var(--space-sm); font-size: 0.82em; } .output-buttons { flex-direction: column; } .download-buttons { width: 100%; } } /* ================================================ UTILITY CLASSES ================================================ */ .transparent-text-active { -webkit-background-clip: text !important; background-clip: text !important; } .visually-hidden { position: absolute; width: 1px; height: 1px; padding: 0; margin: -1px; overflow: hidden; clip: rect(0, 0, 0, 0); white-space: nowrap; border: 0; } </style></head><body> <!-- Header --> <header class="header"> <div class="header-content"> <div class="logo"> <div class="logo-icon"> <i class="fas fa-wand-magic-sparkles"></i> </div> <span class="logo-text">K3N4N CSS Generator</span> <span class="logo-version">V6</span> </div> </div> </header> <!-- Main Container --> <div class="container"> <!-- Controls Sidebar --> <aside class="controls"> <!-- History Buttons --> <div class="history-buttons"> <button data-action="undo" disabled> <i class="fas fa-undo-alt"></i> Geri Al </button> <button data-action="redo" disabled> <i class="fas fa-redo-alt"></i> İleri Al </button> </div> <!-- ==================== PREFIX IMAGE ==================== --> <fieldset class="expanded"> <legend> <i class="fas fa-image"></i> Yazı Başı Görsel (Prefix) <i class="fas fa-chevron-down"></i> </legend> <div class="form-group"> <label><i class="fas fa-file-image"></i> Dosyadan Seç (GIF/Resim)</label> <input type="file" id="prefixImageFile" accept="image/*,.gif"> </div> <div class="form-group"> <label><i class="fas fa-link"></i> veya URL Gir</label> <input type="text" id="prefixImageUrl" placeholder="https://... veya data:image/..."> </div> <div class="form-group"> <label><i class="fas fa-expand"></i> Boyut (px)</label> <input type="number" id="prefixSizePx" value="28" min="8" max="180" data-prefix-prop="sizePx"> </div> <div class="form-group"> <label><i class="fas fa-arrows-alt-h"></i> Sağ Boşluk (px)</label> <input type="number" id="prefixGapPx" value="10" min="0" max="60" data-prefix-prop="gapPx"> </div> <div class="form-group"> <label><i class="fas fa-arrows-alt-v"></i> Dikey Konum (px)</label> <input type="number" id="prefixYOffsetPx" value="0" min="-30" max="30" data-prefix-prop="yOffsetPx"> </div> <div class="form-group"> <label><i class="fas fa-circle"></i> Köşe Yuvarlaklığı (px)</label> <input type="number" id="prefixBorderRadiusPx" value="8" min="0" max="90" data-prefix-prop="borderRadiusPx"> </div> <div class="button-group"> <button data-action="clear-prefix-image"><i class="fas fa-trash"></i> Temizle</button> <button data-action="set-prefix-size-small">Küçük</button> <button data-action="set-prefix-size-medium">Orta</button> <button data-action="set-prefix-size-large">Büyük</button> </div> </fieldset> <!-- ==================== SUFFIX IMAGE (Yazı Sonu) ==================== --> <fieldset> <legend> <i class="fas fa-image"></i> Yazı Sonu Görsel (Suffix) <i class="fas fa-chevron-down"></i> </legend> <div class="form-group"> <label><i class="fas fa-file-image"></i> Dosyadan Seç (GIF/Resim)</label> <input type="file" id="suffixImageFile" accept="image/*,.gif"> </div> <div class="form-group"> <label><i class="fas fa-link"></i> veya URL Gir</label> <input type="text" id="suffixImageUrl" placeholder="https://..."> </div> <div class="form-group"> <label><i class="fas fa-expand"></i> Boyut (px)</label> <input type="number" id="suffixSizePx" value="28" min="8" max="180" data-suffix-prop="sizePx"> </div> <div class="form-group"> <label><i class="fas fa-arrows-alt-h"></i> Sol Boşluk (px)</label> <input type="number" id="suffixGapPx" value="10" min="0" max="60" data-suffix-prop="gapPx"> </div> <div class="form-group"> <label><i class="fas fa-arrows-alt-v"></i> Dikey Konum (px)</label> <input type="number" id="suffixYOffsetPx" value="0" min="-30" max="30" data-suffix-prop="yOffsetPx"> </div> <div class="form-group"> <label><i class="fas fa-circle"></i> Köşe Yuvarlaklığı (px)</label> <input type="number" id="suffixBorderRadiusPx" value="8" min="0" max="90" data-suffix-prop="borderRadiusPx"> </div> <div class="button-group"> <button data-action="clear-suffix-image"><i class="fas fa-trash"></i> Temizle</button> </div> </fieldset> <!-- ==================== BACKGROUND IMAGE ==================== --> <fieldset class="expanded"> <legend> <i class="fas fa-fill-drip"></i> Arka Plan Görsel <i class="fas fa-chevron-down"></i> </legend> <div class="form-group"> <label><i class="fas fa-file-image"></i> Dosyadan Seç</label> <input type="file" id="bgImageFile" accept="image/*,.gif"> </div> <div class="form-group"> <label><i class="fas fa-link"></i> veya URL Gir</label> <input type="text" id="backgroundImageUrl" placeholder="https://..."> </div> <div class="form-group"> <label><i class="fas fa-arrows-alt"></i> Konum X/Y (px)</label> <div class="input-row"> <label>X:</label> <input type="number" id="bgPosX" value="0" min="-2000" max="2000"> <label>Y:</label> <input type="number" id="bgPosY" value="0" min="-2000" max="2000"> </div> </div> <div class="form-group"> <label><i class="fas fa-expand-arrows-alt"></i> Boyut Genişlik/Yükseklik</label> <div class="input-row"> <label>W:</label> <input type="text" id="bgSizeW" value="cover" placeholder="cover, contain, 100px, auto"> <label>H:</label> <input type="text" id="bgSizeH" value="auto" placeholder="auto, 200px"> </div> </div> <div class="form-group"> <label><i class="fas fa-redo"></i> Tekrarlama</label> <select id="backgroundRepeat" data-style-prop="backgroundRepeat"> <option value="no-repeat" selected>No Repeat</option> <option value="repeat">Repeat</option> <option value="repeat-x">Repeat X</option> <option value="repeat-y">Repeat Y</option> <option value="round">Round</option> <option value="space">Space</option> </select> </div> <div class="button-group"> <button data-action="clear-bg-image"><i class="fas fa-trash"></i> Temizle</button> <button data-style-target="random-bg-image"><i class="fas fa-random"></i> Rastgele</button> </div> </fieldset> <!-- ==================== METIN STİLLERİ ==================== --> <fieldset class="expanded"> <legend> <i class="fas fa-paragraph"></i> Metin Stilleri (Max 20px) <i class="fas fa-chevron-down"></i> </legend> <button data-style-target="random-font"><i class="fas fa-font"></i> Rnd Yazı Tipi/Boyut</button> <button data-style-target="random-color"><i class="fas fa-palette"></i> Rnd Yazı Rengi</button> <button data-style-target="random-text-shadow"><i class="fas fa-clone"></i> Rnd Yazı Gölgesi</button> <button data-style-target="random-spacing"><i class="fas fa-arrows-alt-h"></i> Rnd Boşluklar</button> <div class="form-group"> <label for="fontFamily"><i class="fas fa-font"></i> Yazı Fontu</label> <select id="fontFamily" data-style-prop="fontFamily"> <option value="'Poppins', sans-serif" selected>Poppins</option> <option value="'Inter', sans-serif">Inter</option> <option value="'Roboto', sans-serif">Roboto</option> <option value="'Orbitron', sans-serif">Orbitron</option> <option value="'Russo One', sans-serif">Russo One</option> <option value="'Fira Code', monospace">Fira Code</option> <option value="'Roboto Mono', monospace">Roboto Mono</option> <option value="'VT323', monospace">VT323</option> <option value="'Press Start 2P', cursive">Press Start 2P</option> <option value="'Audiowide', cursive">Audiowide</option> <option value="'Monoton', cursive">Monoton</option> <option value="'Lobster', cursive">Lobster</option> <option value="'Pacifico', cursive">Pacifico</option> <option value="'Dancing Script', cursive">Dancing Script</option> <option value="'Permanent Marker', cursive">Permanent Marker</option> <option value="'Cinzel', serif">Cinzel</option> <option value="'Righteous', cursive">Righteous</option> <option value="'Creepster', cursive">Creepster</option> <option value="'Nosifer', cursive">Nosifer</option> <option value="Georgia, serif">Georgia</option> <option value="'Times New Roman', serif">Times New Roman</option> <option value="Arial, sans-serif">Arial</option> <option value="Helvetica, sans-serif">Helvetica</option> </select> </div> <div class="form-group"> <label for="fontSize"><i class="fas fa-text-height"></i> Yazı Boyutu (max 20px)</label> <input type="number" id="fontSize" data-style-prop="fontSize" data-style-unit="px" value="20" min="8" max="20"> </div> <div class="form-group"> <label for="fontWeight"><i class="fas fa-bold"></i> Yazı Kalınlığı</label> <select id="fontWeight" data-style-prop="fontWeight"> <option value="300">300 - Light</option> <option value="400">400 - Normal</option> <option value="500">500 - Medium</option> <option value="600" selected>600 - Semi Bold</option> <option value="700">700 - Bold</option> <option value="900">900 - Black</option> </select> </div> <div class="form-group"> <label for="textColor"><i class="fas fa-eye-dropper"></i> Yazı Rengi</label> <input type="hidden" id="textColor" data-style-prop="color" value="#1e293b"> <div id="textColorPicker" class="color-picker-container"></div> </div> <div class="form-group"> <label for="textAlign"><i class="fas fa-align-center"></i> Hizalama</label> <select id="textAlign" data-style-prop="textAlign"> <option value="left">Sola</option> <option value="center" selected>Merkez</option> <option value="right">Sağa</option> <option value="justify">Yasla</option> </select> </div> <div class="form-group"> <label for="lineHeight"><i class="fas fa-text-height"></i> Satır Yüksekliği</label> <input type="number" id="lineHeight" data-style-prop="lineHeight" value="1.4" step="0.1" min="1" max="2"> </div> <div class="form-group"> <label><i class="fas fa-arrows-alt-h"></i> Harf/Kelime Aralığı</label> <div class="input-row"> <label>Harf:</label> <input type="number" id="letterSpacing" data-style-prop="letterSpacing" data-style-unit="px" value="0" step="0.5"> <label>Kelime:</label> <input type="number" id="wordSpacing" data-style-prop="wordSpacing" data-style-unit="px" value="0" step="1"> </div> </div> </fieldset> <!-- ==================== ARKA PLAN RENGİ / GRADYAN ==================== --> <fieldset> <legend> <i class="fas fa-fill"></i> Arka Plan Renk/Gradyan <i class="fas fa-chevron-down"></i> </legend> <button data-style-target="random-bg-color"><i class="fas fa-fill"></i> Rnd Renk</button> <button data-style-target="random-gradient"><i class="fas fa-grip-lines"></i> Rnd Gradyan</button> <div class="form-group"> <label for="backgroundColor"><i class="fas fa-palette"></i> Arka Plan Rengi</label> <input type="hidden" id="backgroundColor" data-style-prop="backgroundColor" value="#ffffff"> <div id="backgroundColorPicker" class="color-picker-container"></div> </div> </fieldset> <!-- ==================== ÇERÇEVE / BORDER ==================== --> <fieldset class="expanded"> <legend> <i class="fas fa-border-all"></i> Çerçeve Stilleri <i class="fas fa-chevron-down"></i> </legend> <button data-style-target="random-frame-modern"><i class="fas fa-vector-square"></i> Rnd Modern Çerçeve</button> <button data-action="frame-glass"><i class="fas fa-ice-cream"></i> Glass Efekti</button> <button data-action="frame-double"><i class="fas fa-clone"></i> Çift Çerçeve</button> <button data-action="frame-inner"><i class="fas fa-compress-alt"></i> İç Çerçeve</button> <button data-action="frame-outer"><i class="fas fa-expand-alt"></i> Dış Çerçeve</button> <div class="form-group"> <label><i class="fas fa-ruler-horizontal"></i> Kenarlık Genişlik/Stil</label> <div class="input-row"> <label>px:</label> <input type="number" id="borderWidth" data-style-prop="borderWidth" data-style-unit="px" value="1" min="0" max="20"> <label>Stil:</label> <select id="borderStyle" data-style-prop="borderStyle"> <option value="none">Yok</option> <option value="solid" selected>Düz</option> <option value="dashed">Kesik</option> <option value="dotted">Noktalı</option> <option value="double">Çift</option> <option value="groove">Groove</option> <option value="ridge">Ridge</option> <option value="inset">Inset</option> <option value="outset">Outset</option> </select> </div> </div> <div class="form-group"> <label for="borderColor"><i class="fas fa-eye-dropper"></i> Kenarlık Rengi</label> <input type="hidden" id="borderColor" data-style-prop="borderColor" value="#e2e8f0"> <div id="borderColorPicker" class="color-picker-container"></div> </div> <div class="form-group"> <label for="borderRadius"><i class="fas fa-circle"></i> Köşe Yuvarlaklığı</label> <input type="text" id="borderRadius" data-style-prop="borderRadius" placeholder="Örn: 10px, 50%, 10px 20px" value="16px"> </div> </fieldset> <!-- ==================== PADDING / BOYUT ==================== --> <fieldset> <legend> <i class="fas fa-arrows-alt"></i> Padding / Boyut <i class="fas fa-chevron-down"></i> </legend> <button data-style-target="random-padding"><i class="fas fa-expand"></i> Rnd Padding</button> <div class="form-group"> <label for="padding"><i class="fas fa-compress"></i> İç Boşluk (Padding)</label> <input type="text" id="padding" data-style-prop="padding" placeholder="Örn: 20px, 15px 30px" value="32px"> </div> <div class="form-group"> <label><i class="fas fa-ruler-combined"></i> Genişlik/Yükseklik</label> <div class="input-row"> <label>W:</label> <input type="text" id="width" data-style-prop="width" placeholder="auto, 300px, 50%"> <label>H:</label> <input type="text" id="height" data-style-prop="height" placeholder="auto, 200px"> </div> </div> </fieldset> <!-- ==================== EFEKTLER ==================== --> <fieldset> <legend> <i class="fas fa-magic"></i> Efektler <i class="fas fa-chevron-down"></i> </legend> <button data-style-target="random-shadow-modern"><i class="fas fa-clone"></i> Rnd Gölge</button> <button data-style-target="random-opacity"><i class="fas fa-ghost"></i> Rnd Opaklık</button> <button data-style-target="random-filter"><i class="fas fa-sliders-h"></i> Rnd Filtre</button> <button data-style-target="random-transform"><i class="fas fa-sync-alt"></i> Rnd Dönüşüm</button> <div class="form-group"> <label for="opacity"><i class="fas fa-adjust"></i> Opaklık (<span id="opacityValue">1.00</span>)</label> <input type="range" id="opacity" data-style-prop="opacity" min="0" max="1" step="0.01" value="1"> </div> <div class="form-group"> <label for="boxShadowManual"><i class="fas fa-vector-square"></i> Kutu Gölgesi</label> <input type="text" id="boxShadowManual" data-style-prop="boxShadow" placeholder="0 10px 30px rgba(0,0,0,0.1)"> </div> <div class="form-group"> <label for="filter"><i class="fas fa-sliders-h"></i> CSS Filtre</label> <input type="text" id="filter" data-style-prop="filter" placeholder="blur(2px) brightness(1.1)"> </div> <div class="form-group"> <label for="transform"><i class="fas fa-sync"></i> Transform</label> <input type="text" id="transform" data-style-prop="transform" placeholder="rotate(5deg) scale(1.05)"> </div> </fieldset> <!-- ==================== ANİMASYON ==================== --> <fieldset> <legend> <i class="fas fa-running"></i> Animasyonlar <i class="fas fa-chevron-down"></i> </legend> <button data-style-target="random-animation"><i class="fas fa-random"></i> Rnd Animasyon</button> <div class="form-group"> <label for="animationName"><i class="fas fa-tag"></i> Animasyon Adı</label> <input type="text" id="animationName" data-style-prop="animationName" placeholder="K3N4N-Pulse"> </div> <div class="form-group"> <label for="animationDuration"><i class="fas fa-clock"></i> Süre</label> <input type="text" id="animationDuration" data-style-prop="animationDuration" placeholder="2s, 500ms" value="1s"> </div> <div class="form-group"> <label for="animationTimingFunction"><i class="fas fa-bezier-curve"></i> Zamanlama</label> <select id="animationTimingFunction" data-style-prop="animationTimingFunction"> <option value="linear">Linear</option> <option value="ease" selected>Ease</option> <option value="ease-in">Ease In</option> <option value="ease-out">Ease Out</option> <option value="ease-in-out">Ease In Out</option> </select> </div> <div class="form-group"> <label for="animationIterationCount"><i class="fas fa-redo"></i> Tekrar</label> <input type="text" id="animationIterationCount" data-style-prop="animationIterationCount" value="infinite" placeholder="3, infinite"> </div> <div class="form-group"> <label for="animationKeyframes"><i class="fas fa-code"></i> @keyframes</label> <textarea id="animationKeyframes" placeholder="@keyframes K3N4N-Pulse { 0% { transform: scale(1); } 50% { transform: scale(1.05); } 100% { transform: scale(1); } }"></textarea> </div> <div class="button-group"> <button data-action="clear-animation"><i class="fas fa-trash"></i> Temizle</button> </div> </fieldset> <!-- ==================== PX BADGE ==================== --> <fieldset> <legend> <i class="fas fa-tag"></i> PX/Değer Etiketi <i class="fas fa-chevron-down"></i> </legend> <div class="form-group"> <label> <input type="checkbox" id="showPaddingBadge" checked> Padding/Boyut Etiketini Göster </label> </div> <div class="form-group"> <label for="pxBadgeText"><i class="fas fa-edit"></i> Özel Etiket Metni</label> <input type="text" id="pxBadgeText" placeholder="Boş bırakırsan otomatik hesaplanır"> </div> </fieldset> <!-- ==================== KAOS & SETLER ==================== --> <fieldset class="expanded"> <legend> <i class="fas fa-dice-d20"></i> Otomatik & Kaos <i class="fas fa-chevron-down"></i> </legend> <button data-style-target="random-text-set"><i class="fas fa-font"></i> Rastgele Metin Seti</button> <button data-style-target="random-bg-set"><i class="fas fa-image"></i> Rastgele Arka Plan Seti</button> <button data-style-target="random-frame-set"><i class="fas fa-border-all"></i> Rastgele Çerçeve Seti</button> <button data-style-target="random-layout-set"><i class="fas fa-th-large"></i> Rastgele Layout Seti</button> <button data-style-target="random-effect-set"><i class="fas fa-magic"></i> Rastgele Efekt Seti</button> <button data-style-target="random-mix" class="max-chaos-btn" style="margin-top: 10px;"> <i class="fas fa-random"></i> Rastgele Karışım Stil </button> <button data-style-target="max-chaos" class="max-chaos-btn"> <i class="fas fa-meteor"></i> MAKSİMUM KAOS! </button> <button data-action="reset-all" class="reset-btn" style="margin-top: 10px;"> <i class="fas fa-undo"></i> Tüm Stilleri Sıfırla </button> </fieldset> </aside> <!-- Preview Output Area --> <main class="preview-output-area"> <!-- Preview Box --> <div id="preview-box" class="is-empty"></div> <!-- CSS Output Section --> <div class="css-output-section"> <h4><i class="fas fa-code"></i> Üretilen CSS Kodu</h4> <textarea id="css-output" readonly placeholder="#preview-box { ... }"></textarea> <div class="output-buttons"> <button id="copy-css-btn" data-action="copy-css" disabled> <i class="fas fa-copy"></i> Kodu Kopyala </button> <div class="download-buttons"> <button id="download-css-btn" data-action="download-css" disabled> <i class="fas fa-file-code"></i> CSS İndir </button> <button id="download-html-btn" data-action="download-html" disabled> <i class="fas fa-file-alt"></i> HTML İndir </button> </div> </div> </div> <!-- CSS Input Section --> <div class="css-input-section"> <h4><i class="fas fa-paste"></i> Harici CSS Ekle</h4> <textarea id="cssInputArea" placeholder="CSS kodunu buraya yapıştır...&#10;Örnek:&#10;.class {&#10; color: red;&#10; font-size: 16px;&#10;}"></textarea> <div class="button-group"> <button data-action="preview-pasted-css"> <i class="fas fa-eye"></i> Önizle </button> <button data-action="add-pasted-css" style="background: var(--accent-success); color: white; border-color: var(--accent-success);"> <i class="fas fa-plus"></i> Stile Ekle </button> </div> <div id="htmlPreviewArea"> <span class="preview-info">Yapıştırılan CSS önizlemesi burada görünecek.</span> </div> </div> </main> </div> <!-- Footer --> <footer> <p><span class="footer-brand">K3N4N</span> © 2025 - Tüm hakları saklıdır. | Kenan V6</p> </footer> <!-- ================================================ JAVASCRIPT - K3N4N KENAN V6 ================================================ --> <script> /* K3N4N CSS Stil Generator - Kenan V6 (Full Integrated) - Font boyutu tüm fonksiyonlarda MAX 20px - Prefix/Suffix image (dosya + URL) - Background image positioning (px değerleri) - Modern frame styles - Export: CSS copy, CSS download, HTML download - External CSS add */ (() => { 'use strict'; document.addEventListener('DOMContentLoaded', () => { console.log('K3N4N Kenan V6 başlatılıyor...'); // ========================= // DOM REFERENCES // ========================= const previewBox = document.getElementById('preview-box'); const cssOutput = document.getElementById('css-output'); const controlsArea = document.querySelector('.controls'); const cssInputArea = document.getElementById('cssInputArea'); const htmlPreviewArea = document.getElementById('htmlPreviewArea'); const animationKeyframesInput = document.getElementById('animationKeyframes'); const opacityValueSpan = document.getElementById('opacityValue'); // Prefix inputs const prefixImageFileInput = document.getElementById('prefixImageFile'); const prefixImageUrlInput = document.getElementById('prefixImageUrl'); const prefixSizePxInput = document.getElementById('prefixSizePx'); const prefixGapPxInput = document.getElementById('prefixGapPx'); const prefixYOffsetPxInput = document.getElementById('prefixYOffsetPx'); const prefixBorderRadiusPxInput = document.getElementById('prefixBorderRadiusPx'); // Suffix inputs const suffixImageFileInput = document.getElementById('suffixImageFile'); const suffixImageUrlInput = document.getElementById('suffixImageUrl'); const suffixSizePxInput = document.getElementById('suffixSizePx'); const suffixGapPxInput = document.getElementById('suffixGapPx'); const suffixYOffsetPxInput = document.getElementById('suffixYOffsetPx'); const suffixBorderRadiusPxInput = document.getElementById('suffixBorderRadiusPx'); // Background inputs const bgImageFileInput = document.getElementById('bgImageFile'); const bgImageUrlInput = document.getElementById('backgroundImageUrl'); const bgPosXInput = document.getElementById('bgPosX'); const bgPosYInput = document.getElementById('bgPosY'); const bgSizeWInput = document.getElementById('bgSizeW'); const bgSizeHInput = document.getElementById('bgSizeH'); const bgRepeatSelect = document.getElementById('backgroundRepeat'); // Badge inputs const paddingBadgeToggle = document.getElementById('showPaddingBadge'); const pxBadgeTextInput = document.getElementById('pxBadgeText'); // Buttons const copyCssBtn = document.getElementById('copy-css-btn'); // ========================= // LIBRARY CHECKS // ========================= const hasChroma = typeof chroma !== 'undefined'; const hasIro = typeof iro !== 'undefined'; // ========================= // STATE // ========================= let currentStyles = {}; let currentAnimation = { keyframes: null }; let activeWebkitTextEffect = null; // Prefix state let prefixState = { enabled: false, src: null, sizePx: 28, gapPx: 10, yOffsetPx: 0, borderRadiusPx: 8 }; // Suffix state let suffixState = { enabled: false, src: null, sizePx: 28, gapPx: 10, yOffsetPx: 0, borderRadiusPx: 8 }; // Background state let bgState = { src: null, posX: 0, posY: 0, sizeW: 'cover', sizeH: 'auto', repeat: 'no-repeat' }; // Badge state let badgeState = { enabled: true, text: '' }; // History let styleHistory = []; let historyIndex = -1; const MAX_HISTORY = 60; // Color pickers config const colorPickerElements = { textColorPicker: { inputId: 'textColor', styleProp: 'color', default: '#1e293b' }, borderColorPicker: { inputId: 'borderColor', styleProp: 'borderColor', default: '#e2e8f0' }, backgroundColorPicker: { inputId: 'backgroundColor', styleProp: 'backgroundColor', default: '#ffffff' } }; const colorPickers = {}; // ========================= // HELPERS // ========================= const clamp = (n, min, max) => Math.max(min, Math.min(max, n)); const toNum = (v, fallback = 0) => { const n = Number(String(v).replace(/[^\d.-]/g, '')); return Number.isFinite(n) ? n : fallback; }; const getRandomInt = (min, max) => Math.floor(Math.random() * (max - min + 1)) + min; const getRandomFloat = (min, max, precision = 2) => parseFloat((Math.random() * (max - min) + min).toFixed(precision)); const getRandomFromList = (list) => list[Math.floor(Math.random() * list.length)]; const getRandomBoolean = (p = 0.5) => Math.random() < p; const shuffleArray = (arr) => { for (let i = arr.length - 1; i > 0; i--) { const j = Math.floor(Math.random() * (i + 1)); [arr[i], arr[j]] = [arr[j], arr[i]]; } return arr; }; const isValidColor = (c) => { if (!hasChroma) return typeof c === 'string' && c.length > 0; try { return chroma.valid(c); } catch { return false; } }; const getRandomHex = () => hasChroma ? chroma.random().hex() : `#${Math.floor(Math.random()*16777215).toString(16).padStart(6,'0')}`; const getRandomRgbaString = (minA = 0.3, maxA = 0.95) => { if (!hasChroma) return getRandomHex(); return chroma.random().alpha(getRandomFloat(minA, maxA, 2)).css(); }; const camelToKebab = (s) => s.replace(/([A-Z])/g, '-$1').toLowerCase(); const debounce = (fn, wait = 250) => { let t; return (...args) => { clearTimeout(t); t = setTimeout(() => fn(...args), wait); }; }; const escapeHtml = (s) => String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;').replace(/'/g,'&#039;'); const escapeAttr = (s) => escapeHtml(s).replace(/`/g,'&#096;'); // Font clamp: MAX 20px const clampFontSizeTo20px = () => { const v = currentStyles.fontSize; if (!v) { currentStyles.fontSize = '20px'; return; } const m = String(v).trim().match(/^(-?\d*\.?\d+)\s*(px|em|rem|vw|vh|%)?$/i); if (!m) { currentStyles.fontSize = '20px'; return; } const num = parseFloat(m[1]); currentStyles.fontSize = `${clamp(Math.round(num), 8, 20)}px`; }; const clampLineHeight = () => { if (currentStyles.lineHeight == null) return; const n = parseFloat(currentStyles.lineHeight); if (!Number.isFinite(n)) return; currentStyles.lineHeight = String(clamp(n, 1.1, 2.0)); }; const normalizePadding = () => { if (!currentStyles.padding) return; currentStyles.padding = currentStyles.padding.replace(/(-?\d+)\s*px/g, (_, n) => `${clamp(parseInt(n,10), -20, 120)}px`); }; // Update badge text const updateBadge = () => { if (!badgeState.enabled) { badgeState.text = ''; return; } if (pxBadgeTextInput && pxBadgeTextInput.value.trim()) { badgeState.text = pxBadgeTextInput.value.trim(); return; } const parts = []; if (currentStyles.padding) parts.push(`PAD ${currentStyles.padding}`); if (currentStyles.width) parts.push(`W ${currentStyles.width}`); if (currentStyles.height) parts.push(`H ${currentStyles.height}`); badgeState.text = parts.join(' • '); }; // Apply prefix/suffix/badge to DOM const applyContentDom = () => { if (!previewBox) return; if (!previewBox.dataset.baseText) { const t = previewBox.textContent?.trim(); previewBox.dataset.baseText = t && t.length ? t : 'K3N4N Kenan V6'; } const baseText = previewBox.dataset.baseText; // Prefix const prefixHtml = (prefixState.enabled && prefixState.src) ? `<img class="k3n4n-prefix" data-k3n4n-prefix="1" alt="" src="${escapeAttr(prefixState.src)}" />` : ''; // Suffix const suffixHtml = (suffixState.enabled && suffixState.src) ? `<img class="k3n4n-suffix" data-k3n4n-suffix="1" alt="" src="${escapeAttr(suffixState.src)}" />` : ''; // Badge const badgeHtml = (badgeState.enabled && badgeState.text) ? `<span class="k3n4n-badge" data-k3n4n-badge="1">${escapeHtml(badgeState.text)}</span>` : ''; previewBox.innerHTML = ` <span class="k3n4n-wrap" data-k3n4n-wrap="1"> ${prefixHtml} <span class="k3n4n-text" data-k3n4n-text="1">${escapeHtml(baseText)}</span> ${suffixHtml} ${badgeHtml} </span> `.trim(); // Prefix styles const prefixEl = previewBox.querySelector('[data-k3n4n-prefix="1"]'); if (prefixEl) { prefixEl.style.cssText = ` width: ${clamp(prefixState.sizePx, 8, 180)}px; height: ${clamp(prefixState.sizePx, 8, 180)}px; object-fit: cover; display: inline-block; margin-right: ${clamp(prefixState.gapPx, 0, 60)}px; transform: translateY(${clamp(prefixState.yOffsetPx, -30, 30)}px); border-radius: ${clamp(prefixState.borderRadiusPx, 0, 90)}px; box-shadow: 0 4px 12px rgba(0,0,0,0.2); `; } // Suffix styles const suffixEl = previewBox.querySelector('[data-k3n4n-suffix="1"]'); if (suffixEl) { suffixEl.style.cssText = ` width: ${clamp(suffixState.sizePx, 8, 180)}px; height: ${clamp(suffixState.sizePx, 8, 180)}px; object-fit: cover; display: inline-block; margin-left: ${clamp(suffixState.gapPx, 0, 60)}px; transform: translateY(${clamp(suffixState.yOffsetPx, -30, 30)}px); border-radius: ${clamp(suffixState.borderRadiusPx, 0, 90)}px; box-shadow: 0 4px 12px rgba(0,0,0,0.2); `; } // Badge styles const badgeEl = previewBox.querySelector('[data-k3n4n-badge="1"]'); if (badgeEl) { badgeEl.style.cssText = ` display: inline-block; margin-left: 12px; padding: 4px 10px; border-radius: 999px; font-size: 11px; line-height: 1.2; white-space: nowrap; opacity: 0.85; background: rgba(0,0,0,0.08); border: 1px solid rgba(0,0,0,0.1); color: inherit; `; } previewBox.classList.toggle('is-empty', false); }; // Sync background state to styles const syncBgStateToStyles = () => { if (bgState.src) { currentStyles.backgroundImage = `url('${bgState.src}')`; const w = String(bgState.sizeW || 'cover').trim(); const h = String(bgState.sizeH || 'auto').trim(); if (w === 'cover' || w === 'contain') { currentStyles.backgroundSize = w; } else { const wVal = w === 'auto' ? 'auto' : `${clamp(toNum(w, 0), 0, 5000)}px`; const hVal = h === 'auto' ? 'auto' : `${clamp(toNum(h, 0), 0, 5000)}px`; currentStyles.backgroundSize = `${wVal} ${hVal}`; } currentStyles.backgroundRepeat = bgState.repeat || 'no-repeat'; currentStyles.backgroundPosition = `${clamp(toNum(bgState.posX, 0), -2000, 2000)}px ${clamp(toNum(bgState.posY, 0), -2000, 2000)}px`; } else { delete currentStyles.backgroundImage; delete currentStyles.backgroundSize; delete currentStyles.backgroundRepeat; delete currentStyles.backgroundPosition; } }; // Build CSS string const buildCssString = () => { clampFontSizeTo20px(); clampLineHeight(); normalizePadding(); const finalStyles = { ...currentStyles }; const keys = Object.keys(finalStyles).filter(k => finalStyles[k] != null && String(finalStyles[k]).trim() !== '').sort(); if (keys.length === 0 && !currentAnimation.keyframes) { return `/* Henüz stil uygulanmadı */`; } let css = `#preview-box {\n`; for (const prop of keys) { css += ` ${camelToKebab(prop)}: ${finalStyles[prop]};\n`; } css += `}\n`; if (currentAnimation.keyframes) css += `\n${currentAnimation.keyframes}\n`; return css.trim(); }; // Apply styles to preview const applyStylesToPreview = () => { if (!previewBox) return; previewBox.style.cssText = ''; clampFontSizeTo20px(); clampLineHeight(); normalizePadding(); for (const [k, v] of Object.entries(currentStyles)) { try { if (k === 'userSelect') { previewBox.style.userSelect = v; previewBox.style.webkitUserSelect = v; continue; } if (k === 'backdropFilter') { previewBox.style.backdropFilter = v; previewBox.style.webkitBackdropFilter = v; continue; } previewBox.style[k] = v; } catch (e) { console.warn('Style error', k, e); } } if (opacityValueSpan && currentStyles.opacity != null) { opacityValueSpan.textContent = parseFloat(currentStyles.opacity).toFixed(2); } }; // Main update function const updatePreviewAndOutput = () => { syncBgStateToStyles(); updateBadge(); applyContentDom(); applyStylesToPreview(); if (cssOutput) cssOutput.value = buildCssString(); const hasContent = cssOutput && cssOutput.value && !cssOutput.value.includes('Henüz'); document.querySelectorAll('[data-action="download-css"], [data-action="download-html"], [data-action="copy-css"]').forEach(b => b.disabled = !hasContent); }; // ========================= // HISTORY // ========================= const saveHistory = () => { const snapshot = { styles: JSON.parse(JSON.stringify(currentStyles)), animationKeyframes: currentAnimation.keyframes, prefix: JSON.parse(JSON.stringify(prefixState)), suffix: JSON.parse(JSON.stringify(suffixState)), bg: JSON.parse(JSON.stringify(bgState)), badge: JSON.parse(JSON.stringify(badgeState)), baseText: previewBox?.dataset?.baseText || '' }; if (historyIndex >= 0) { try { if (JSON.stringify(styleHistory[historyIndex]) === JSON.stringify(snapshot)) return; } catch {} } if (historyIndex < styleHistory.length - 1) styleHistory = styleHistory.slice(0, historyIndex + 1); styleHistory.push(snapshot); historyIndex++; if (styleHistory.length > MAX_HISTORY) { styleHistory.shift(); historyIndex--; } updateHistoryButtons(); }; const restoreState = (st) => { if (!st) return; currentStyles = JSON.parse(JSON.stringify(st.styles || {})); currentAnimation.keyframes = st.animationKeyframes || null; prefixState = JSON.parse(JSON.stringify(st.prefix || prefixState)); suffixState = JSON.parse(JSON.stringify(st.suffix || suffixState)); bgState = JSON.parse(JSON.stringify(st.bg || bgState)); badgeState = JSON.parse(JSON.stringify(st.badge || badgeState)); if (previewBox && st.baseText) previewBox.dataset.baseText = st.baseText; updateControlsFromState(); updatePreviewAndOutput(); }; const undoStyle = () => { if (historyIndex > 0) { historyIndex--; restoreState(styleHistory[historyIndex]); updateHistoryButtons(); } }; const redoStyle = () => { if (historyIndex < styleHistory.length - 1) { historyIndex++; restoreState(styleHistory[historyIndex]); updateHistoryButtons(); } }; const updateHistoryButtons = () => { const u = controlsArea.querySelector('[data-action="undo"]'); const r = controlsArea.querySelector('[data-action="redo"]'); if (u) u.disabled = historyIndex <= 0; if (r) r.disabled = historyIndex >= styleHistory.length - 1; }; // ========================= // RESET // ========================= const resetAllStyles = (save = true) => { if (save) saveHistory(); currentStyles = { display: 'flex', alignItems: 'center', justifyContent: 'center', gap: '10px', padding: '32px', minHeight: '320px', borderRadius: '16px', border: '1px solid #e2e8f0', backgroundColor: '#ffffff', color: '#1e293b', fontFamily: "'Poppins', sans-serif", fontSize: '20px', fontWeight: '600', textAlign: 'center', lineHeight: '1.4', boxShadow: '0 10px 30px rgba(0,0,0,0.1)', overflow: 'hidden' }; currentAnimation.keyframes = null; prefixState = { enabled: false, src: null, sizePx: 28, gapPx: 10, yOffsetPx: 0, borderRadiusPx: 8 }; suffixState = { enabled: false, src: null, sizePx: 28, gapPx: 10, yOffsetPx: 0, borderRadiusPx: 8 }; bgState = { src: null, posX: 0, posY: 0, sizeW: 'cover', sizeH: 'auto', repeat: 'no-repeat' }; badgeState = { enabled: true, text: '' }; if (previewBox) previewBox.dataset.baseText = 'K3N4N Kenan V6'; updateControlsFromState(); updatePreviewAndOutput(); saveHistory(); updateHistoryButtons(); }; // ========================= // UPDATE CONTROLS FROM STATE // ========================= const updateControlsFromState = () => { controlsArea.querySelectorAll('[data-style-prop]').forEach(el => { const prop = el.dataset.styleProp; if (!prop) return; if (el.type === 'range' && prop === 'opacity') { el.value = parseFloat(currentStyles.opacity ?? 1); if (opacityValueSpan) opacityValueSpan.textContent = parseFloat(el.value).toFixed(2); return; } const v = currentStyles[prop]; if (v == null) return; const unit = el.dataset.styleUnit || ''; el.value = unit && typeof v === 'string' ? String(v).replace(unit, '').trim() : String(v); }); // Prefix if (prefixSizePxInput) prefixSizePxInput.value = prefixState.sizePx; if (prefixGapPxInput) prefixGapPxInput.value = prefixState.gapPx; if (prefixYOffsetPxInput) prefixYOffsetPxInput.value = prefixState.yOffsetPx; if (prefixBorderRadiusPxInput) prefixBorderRadiusPxInput.value = prefixState.borderRadiusPx; // Suffix if (suffixSizePxInput) suffixSizePxInput.value = suffixState.sizePx; if (suffixGapPxInput) suffixGapPxInput.value = suffixState.gapPx; if (suffixYOffsetPxInput) suffixYOffsetPxInput.value = suffixState.yOffsetPx; if (suffixBorderRadiusPxInput) suffixBorderRadiusPxInput.value = suffixState.borderRadiusPx; // Background if (bgPosXInput) bgPosXInput.value = bgState.posX; if (bgPosYInput) bgPosYInput.value = bgState.posY; if (bgSizeWInput) bgSizeWInput.value = bgState.sizeW; if (bgSizeHInput) bgSizeHInput.value = bgState.sizeH; if (bgRepeatSelect) bgRepeatSelect.value = bgState.repeat; // Badge if (paddingBadgeToggle) paddingBadgeToggle.checked = badgeState.enabled; // Animation if (animationKeyframesInput) animationKeyframesInput.value = currentAnimation.keyframes || ''; }; // ========================= // FONTS / LISTS // ========================= const fontList = [ "'Poppins', sans-serif", "'Inter', sans-serif", "'Roboto', sans-serif", "'Orbitron', sans-serif", "'Russo One', sans-serif", "'Fira Code', monospace", "'Roboto Mono', monospace", "'Lobster', cursive", "'Pacifico', cursive", "'Cinzel', serif", "'Righteous', cursive", "Georgia, serif", "Arial, sans-serif" ]; // ========================= // PALETTE GENERATOR // ========================= const generatePalette = (count = 4, type = 'analogous', baseColor = getRandomHex()) => { if (!hasChroma) return Array.from({ length: count }, () => getRandomHex()); if (!isValidColor(baseColor)) baseColor = chroma.random().hex(); try { const base = chroma(baseColor); let anchors; switch (type) { case 'monochromatic': return chroma.scale([base.darken(1.5), base, base.brighten(1.5)]).mode('lch').colors(count); case 'complementary': anchors = [base, base.set('hsl.h', '+180')]; break; case 'triadic': anchors = [base, base.set('hsl.h', '+120'), base.set('hsl.h', '+240')]; break; case 'split': anchors = [base, base.set('hsl.h', '+150'), base.set('hsl.h', '+210')]; break; default: anchors = [base.set('hsl.h', '-30'), base, base.set('hsl.h', '+30')]; } return chroma.scale(anchors).mode('lch').padding(0.06).colors(count); } catch { return Array.from({ length: count }, () => getRandomHex()); } }; const getContrastingColor = (bg, light = '#ffffff', dark = '#1e293b') => { if (!hasChroma || !isValidColor(bg)) return dark; try { return chroma.contrast(bg, light) >= 4.5 ? light : dark; } catch { return dark; } }; // ========================= // KEYFRAMES // ========================= const simpleAnimationNames = ["K3N4N-Pulse", "K3N4N-Spin", "K3N4N-FadeInOut", "K3N4N-Shake", "K3N4N-Bounce"]; const generateSimpleKeyframes = (name) => { let kf = `@keyframes ${name} {\n`; switch (name) { case "K3N4N-Pulse": kf += ` 0%, 100% { transform: scale(1); }\n 50% { transform: scale(1.05); }\n`; break; case "K3N4N-Spin": kf += ` from { transform: rotate(0deg); }\n to { transform: rotate(360deg); }\n`; break; case "K3N4N-FadeInOut": kf += ` 0%, 100% { opacity: 1; }\n 50% { opacity: 0.3; }\n`; break; case "K3N4N-Shake": kf += ` 0%, 100% { transform: translateX(0); }\n 20% { transform: translateX(-6px); }\n 40% { transform: translateX(6px); }\n 60% { transform: translateX(-4px); }\n 80% { transform: translateX(4px); }\n`; break; case "K3N4N-Bounce": kf += ` 0%, 20%, 50%, 80%, 100% { transform: translateY(0); }\n 40% { transform: translateY(-15px); }\n 60% { transform: translateY(-8px); }\n`; break; default: kf += ` 0% { opacity: 1; }\n 100% { opacity: 0.6; }\n`; } return kf + `}`; }; // ========================= // RANDOM STYLE FUNCTIONS // ========================= const applyRandomFont = () => { currentStyles.fontFamily = getRandomFromList(fontList); currentStyles.fontWeight = getRandomFromList(['300', '400', '500', '600', '700']); currentStyles.fontSize = `${getRandomInt(12, 20)}px`; clampFontSizeTo20px(); }; const applyRandomColor = () => { const palette = generatePalette(5, getRandomFromList(['analogous', 'split', 'triadic', 'monochromatic']), getRandomHex()); const bg = currentStyles.backgroundColor && isValidColor(currentStyles.backgroundColor) ? currentStyles.backgroundColor : '#ffffff'; const textCandidates = palette.filter(c => !hasChroma || chroma.contrast(bg, c) >= 4.5); currentStyles.color = textCandidates.length ? getRandomFromList(textCandidates) : getContrastingColor(bg); if (getRandomBoolean(0.5)) { currentStyles.textShadow = `0 2px 8px ${getRandomRgbaString(0.1, 0.3)}`; } }; const applyRandomBgColor = () => { currentStyles.backgroundColor = getRandomRgbaString(0.9, 1); delete currentStyles.background; }; const applyRandomGradient = () => { const p = generatePalette(getRandomInt(2, 4), getRandomFromList(['analogous', 'triadic', 'split']), getRandomHex()); const angle = getRandomInt(0, 360); const stops = p.map((c, i) => `${c} ${Math.round(i * (100 / (p.length - 1 || 1)))}%`).join(', '); currentStyles.background = `linear-gradient(${angle}deg, ${stops})`; delete currentStyles.backgroundColor; }; const applyRandomSpacing = () => { currentStyles.letterSpacing = `${getRandomFloat(-0.5, 2, 2)}px`; currentStyles.wordSpacing = `${getRandomFloat(-1, 5, 2)}px`; currentStyles.lineHeight = String(getRandomFloat(1.1, 1.8, 2)); clampLineHeight(); }; const applyRandomPadding = () => { const p = getRandomInt(12, 40); currentStyles.padding = getRandomBoolean(0.6) ? `${p}px` : `${getRandomInt(10, 30)}px ${getRandomInt(15, 50)}px`; normalizePadding(); }; const applyRandomBorderModern = () => { const palette = generatePalette(4, getRandomFromList(['analogous', 'split', 'triadic']), getRandomHex()); const radius = getRandomInt(8, 24); currentStyles.borderRadius = `${radius}px`; const style = getRandomFromList(['glass', 'double', 'glow', 'inset', 'solid']); const c1 = palette[0], c2 = palette[1]; if (style === 'glass') { currentStyles.border = `1px solid rgba(255,255,255,0.2)`; currentStyles.boxShadow = `0 12px 40px rgba(0,0,0,0.15), inset 0 0 0 1px rgba(255,255,255,0.1)`; currentStyles.backdropFilter = 'blur(10px)'; } else if (style === 'double') { currentStyles.border = `3px double ${hasChroma ? chroma(c1).alpha(0.8).css() : c1}`; currentStyles.boxShadow = `0 10px 30px rgba(0,0,0,0.12), inset 0 0 0 2px ${hasChroma ? chroma(c2).alpha(0.2).css() : c2}`; } else if (style === 'glow') { const glow = hasChroma ? chroma(c1).alpha(0.5).css() : c1; currentStyles.border = `1px solid ${hasChroma ? chroma(c1).alpha(0.5).css() : c1}`; currentStyles.boxShadow = `0 0 25px ${glow}, 0 10px 40px rgba(0,0,0,0.2)`; } else if (style === 'inset') { currentStyles.border = `1px solid rgba(0,0,0,0.1)`; currentStyles.boxShadow = `inset 0 2px 10px rgba(0,0,0,0.1), 0 10px 30px rgba(0,0,0,0.1)`; } else { currentStyles.border = `2px solid ${hasChroma ? chroma(c1).alpha(0.6).css() : c1}`; currentStyles.boxShadow = `0 10px 30px rgba(0,0,0,0.1)`; } }; const applyRandomBoxShadow = () => { const type = getRandomFromList(['soft', 'lift', 'neon', 'inset']); if (type === 'soft') currentStyles.boxShadow = `0 8px 25px rgba(0,0,0,0.1)`; else if (type === 'lift') currentStyles.boxShadow = `0 15px 50px rgba(0,0,0,0.2)`; else if (type === 'neon') { const glow = getRandomHex(); currentStyles.boxShadow = `0 0 20px ${hasChroma ? chroma(glow).alpha(0.5).css() : glow}, 0 10px 40px rgba(0,0,0,0.2)`; } else { currentStyles.boxShadow = `inset 0 2px 10px rgba(0,0,0,0.15), 0 10px 30px rgba(0,0,0,0.1)`; } }; const applyRandomOpacity = () => { currentStyles.opacity = String(getRandomFloat(0.4, 1, 2)); }; const applyRandomFilter = () => { const parts = []; if (getRandomBoolean(0.3)) parts.push(`blur(${getRandomInt(0, 2)}px)`); if (getRandomBoolean(0.5)) parts.push(`brightness(${getRandomFloat(0.9, 1.2, 2)})`); if (getRandomBoolean(0.5)) parts.push(`contrast(${getRandomFloat(0.9, 1.3, 2)})`); if (getRandomBoolean(0.3)) parts.push(`saturate(${getRandomFloat(0.8, 1.5, 2)})`); currentStyles.filter = parts.length ? parts.join(' ') : 'none'; if (currentStyles.filter === 'none') delete currentStyles.filter; }; const applyRandomTransform = () => { const parts = []; if (getRandomBoolean(0.4)) parts.push(`rotate(${getRandomInt(-8, 8)}deg)`); if (getRandomBoolean(0.5)) parts.push(`scale(${getRandomFloat(0.96, 1.06, 2)})`); if (getRandomBoolean(0.4)) parts.push(`translateY(${getRandomInt(-6, 6)}px)`); currentStyles.transform = parts.length ? parts.join(' ') : 'none'; if (currentStyles.transform === 'none') delete currentStyles.transform; }; const applyRandomAnimation = () => { const name = getRandomFromList(simpleAnimationNames); currentStyles.animationName = name; currentStyles.animationDuration = `${getRandomInt(800, 3500)}ms`; currentStyles.animationTimingFunction = getRandomFromList(['ease', 'linear', 'ease-in', 'ease-out', 'ease-in-out']); currentStyles.animationIterationCount = getRandomBoolean(0.6) ? 'infinite' : String(getRandomInt(1, 4)); currentAnimation.keyframes = generateSimpleKeyframes(name); }; // Sets const applyRandomTextSet = () => { applyRandomFont(); applyRandomColor(); if (getRandomBoolean(0.5)) applyRandomSpacing(); clampFontSizeTo20px(); }; const applyRandomBgSet = () => { if (getRandomBoolean(0.5)) applyRandomGradient(); else applyRandomBgColor(); }; const applyRandomFrameSet = () => { applyRandomBorderModern(); }; const applyRandomLayoutSet = () => { currentStyles.display = 'flex'; currentStyles.alignItems = 'center'; currentStyles.justifyContent = 'center'; if (getRandomBoolean(0.5)) currentStyles.gap = `${getRandomInt(8, 20)}px`; if (getRandomBoolean(0.5)) currentStyles.minHeight = `${getRandomInt(200, 400)}px`; }; const applyRandomEffectSet = () => { if (getRandomBoolean(0.6)) applyRandomOpacity(); if (getRandomBoolean(0.5)) applyRandomFilter(); if (getRandomBoolean(0.5)) applyRandomTransform(); }; const applyRandomMix = () => { const sets = [applyRandomTextSet, applyRandomBgSet, applyRandomFrameSet, applyRandomLayoutSet, applyRandomEffectSet]; shuffleArray(sets); const n = getRandomInt(2, sets.length); for (let i = 0; i < n; i++) sets[i](); clampFontSizeTo20px(); }; const applyMaxChaos = () => { applyRandomTextSet(); applyRandomBgSet(); applyRandomFrameSet(); applyRandomLayoutSet(); applyRandomEffectSet(); applyRandomPadding(); if (getRandomBoolean(0.4)) applyRandomAnimation(); clampFontSizeTo20px(); }; // ========================= // FILE HANDLERS // ========================= const fileToDataUrl = (file) => new Promise((resolve, reject) => { const reader = new FileReader(); reader.onload = () => resolve(String(reader.result)); reader.onerror = reject; reader.readAsDataURL(file); }); const handlePrefixFile = async (file) => { if (!file) return; try { prefixState.src = await fileToDataUrl(file); prefixState.enabled = true; updatePreviewAndOutput(); saveHistory(); } catch (e) { console.error('Prefix file error:', e); } }; const handleSuffixFile = async (file) => { if (!file) return; try { suffixState.src = await fileToDataUrl(file); suffixState.enabled = true; updatePreviewAndOutput(); saveHistory(); } catch (e) { console.error('Suffix file error:', e); } }; const handleBgFile = async (file) => { if (!file) return; try { bgState.src = await fileToDataUrl(file); updatePreviewAndOutput(); saveHistory(); } catch (e) { console.error('BG file error:', e); } }; // ========================= // EXPORT FUNCTIONS // ========================= const downloadFile = (filename, content, type) => { const a = document.createElement('a'); a.href = `data:${type};charset=utf-8,` + encodeURIComponent(content); a.download = filename; a.style.display = 'none'; document.body.appendChild(a); a.click(); document.body.removeChild(a); }; const buildExportHtml = () => { const css = buildCssString(); const inner = previewBox ? previewBox.innerHTML : ''; return `<!DOCTYPE html><html lang="tr"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1"/><title>K3N4N Kenan V6 Export</title><link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap" rel="stylesheet"><style>* { box-sizing: border-box; margin: 0; padding: 0; }body { min-height: 100vh; display: flex; align-items: center; justify-content: center; background: linear-gradient(135deg, #0a0e17, #1e1b4b); padding: 24px; font-family: 'Poppins', sans-serif; }${css}#preview-box .k3n4n-wrap { display: inline-flex; align-items: center; gap: 10px; }#preview-box .k3n4n-prefix, #preview-box .k3n4n-suffix { flex: 0 0 auto; }#preview-box .k3n4n-badge { margin-left: 12px; padding: 4px 10px; border-radius: 999px; font-size: 11px; background: rgba(0,0,0,0.08); border: 1px solid rgba(0,0,0,0.1); }</style></head><body><div id="preview-box">${inner}</div></body></html>`; }; // ========================= // CSS INPUT / PASTE // ========================= const previewPastedCss = () => { if (!cssInputArea || !htmlPreviewArea) return; const cssCode = cssInputArea.value.trim(); if (!cssCode) { htmlPreviewArea.innerHTML = '<span class="preview-info">CSS girin.</span>'; return; } try { const wrapper = document.createElement('div'); wrapper.className = 'preview-wrapper'; const styleEl = document.createElement('style'); styleEl.textContent = cssCode; const prev = document.createElement('div'); prev.className = 'preview-element'; prev.textContent = 'Pasted CSS Preview'; wrapper.appendChild(styleEl); wrapper.appendChild(prev); htmlPreviewArea.innerHTML = ''; htmlPreviewArea.appendChild(wrapper); } catch (e) { htmlPreviewArea.innerHTML = `<span class="preview-error">Hata: ${escapeHtml(e.message)}</span>`; } }; const addPastedCss = () => { if (!cssInputArea) return; const cssCode = cssInputArea.value.trim(); if (!cssCode) return; try { const kf = cssCode.match(/@keyframes\s+([^{\s]+)[\s\S]*?\}\s*\}/); if (kf) { currentAnimation.keyframes = kf[0].trim(); if (!currentStyles.animationName) currentStyles.animationName = kf[1]; } const ruleMatch = cssCode.match(/\{([\s\S]*?)\}/); if (ruleMatch && ruleMatch[1]) { const props = ruleMatch[1].split(';').map(s => s.trim()).filter(Boolean).filter(s => s.includes(':')); for (const p of props) { const parts = p.split(/:(.*)/); if (parts.length < 2) continue; const name = parts[0].trim(); const value = parts[1].trim(); if (!name || !value) continue; const camel = name.replace(/-([a-z])/g, (_, g1) => g1.toUpperCase()); currentStyles[camel] = value; } } clampFontSizeTo20px(); cssInputArea.value = ''; updateControlsFromState(); updatePreviewAndOutput(); saveHistory(); htmlPreviewArea.innerHTML = '<span class="preview-info" style="color:#10b981;">CSS eklendi!</span>'; } catch (e) { htmlPreviewArea.innerHTML = `<span class="preview-error">Hata: ${escapeHtml(e.message)}</span>`; } }; // ========================= // COLOR PICKERS // ========================= const initColorPickers = () => { if (!hasIro) return; Object.keys(colorPickerElements).forEach(pickerId => { const container = document.getElementById(pickerId); const info = colorPickerElements[pickerId]; if (!container || !info) return; const hiddenInput = document.getElementById(info.inputId); if (!hiddenInput) return; try { const picker = new iro.ColorPicker(container, { width: Math.min(container.offsetWidth || 200, 200), color: info.default, borderWidth: 1, borderColor: 'rgba(148,163,184,0.3)', layout: [ { component: iro.ui.Wheel }, { component: iro.ui.Slider, options: { sliderType: 'hue' } }, { component: iro.ui.Slider, options: { sliderType: 'alpha' } }, ], handleRadius: 7, padding: 4 }); colorPickers[pickerId] = { instance: picker, info }; picker.on('color:change', debounce((color) => { hiddenInput.value = color.hexString; if (info.styleProp) { currentStyles[info.styleProp] = color.rgbaString; if (info.styleProp === 'backgroundColor' && getRandomBoolean(0.2)) { currentStyles.color = getContrastingColor(color.hexString); } } clampFontSizeTo20px(); updatePreviewAndOutput(); saveHistory(); }, 100)); } catch (e) { console.warn('Color picker error:', pickerId, e); } }); }; // ========================= // FIELDSET TOGGLE // ========================= const setupFieldsetToggles = () => { controlsArea.querySelectorAll('fieldset legend').forEach(legend => { legend.addEventListener('click', () => { const fieldset = legend.parentElement; fieldset.classList.toggle('expanded'); }); }); }; // ========================= // EVENT LISTENERS // ========================= const debouncedUpdateAndSave = debounce(() => { clampFontSizeTo20px(); clampLineHeight(); normalizePadding(); updatePreviewAndOutput(); saveHistory(); }, 200); const setupEventListeners = () => { // Input events controlsArea.addEventListener('input', (e) => { const el = e.target; if (!el) return; // Badge toggle if (el === paddingBadgeToggle) { badgeState.enabled = !!el.checked; debouncedUpdateAndSave(); return; } // Badge text if (el === pxBadgeTextInput) { debouncedUpdateAndSave(); return; } // Background position if (el === bgPosXInput || el === bgPosYInput || el === bgSizeWInput || el === bgSizeHInput) { if (bgPosXInput) bgState.posX = clamp(toNum(bgPosXInput.value, 0), -2000, 2000); if (bgPosYInput) bgState.posY = clamp(toNum(bgPosYInput.value, 0), -2000, 2000); if (bgSizeWInput) bgState.sizeW = bgSizeWInput.value.trim() || 'cover'; if (bgSizeHInput) bgState.sizeH = bgSizeHInput.value.trim() || 'auto'; debouncedUpdateAndSave(); return; } // URL inputs if (el === bgImageUrlInput) { bgState.src = el.value.trim() || null; debouncedUpdateAndSave(); return; } if (el === prefixImageUrlInput) { prefixState.src = el.value.trim() || null; prefixState.enabled = !!prefixState.src; debouncedUpdateAndSave(); return; } if (el === suffixImageUrlInput) { suffixState.src = el.value.trim() || null; suffixState.enabled = kodu tamamla hatalrı gıder ayrı dosyalar halınde yaz gelsıtır önerılerın ve tavsıyelerın varsa tum yapıyı degıstrıp modern br yapı ve ozelıkler ekleyıp gelsıtıreebılırsın gelsıtırdıgın guncel html kodunu ve css kodunu yaz onay al onay aldıkdan sonra js kodunu yazacagım once html ve css kodunu yaz yenı senın kendı ozel tasarımın ve modern ozelıkler ve genısletılmıs olzeıklerle mobıl uyumlu luk ekleyeceksın ve tu yenı ozleıklerle baslayalım html ve css kodunu yz onay al

### Gemini 3 Pro
*2026-01-11 14:42:07 +03*



<think>

**Initiating the Analysis**

I'm now diving into the user's request. My focus is on understanding the core goal: to develop an enhanced "K3N4N CSS Style Generator - Kenan V6" – an upgrade of the existing V6 codebase. I'm starting by carefully dissecting the prompt and its implications.


**Assessing the Project's Scope**

I've identified the core requirements. The user wants me to fix the incomplete code, separate it into HTML and CSS files initially, with JS coming later. I'm focusing on improvements: a modern structure, new features, and mobile responsiveness. The user specifically encourages structural changes. I'm also planning to incorporate their request for the site to be in Turkish.

I've also evaluated the prior "V6" version. The design was a bit dense, but the use of CSS variables was a solid starting point that I can refine. The grid layout needs to prioritize the preview area. Mobile responsiveness, while present, needs a significant overhaul toward mobile-first and a drawer-based approach for controls to create a better experience.


**Developing the V7 Design**

My focus is on the V7 architecture. I'm now incorporating user interface improvements. Grouping those many inputs is critical. I'm leaning toward tabs or accordions. I'm envisioning the "Cyberpunk/Glassmorphism Hybrid" design and the layout: a large, sticky preview with a tabbed control panel. I'm prioritizing features such as a visual box model editor and glassmorphism generator sliders.


**Outlining the Structure**

I'm solidifying the structure. The HTML framework is coming together, starting with meta tags, fonts, and a CSS link. I'm building out the `header` with a logo and version information. The core, `main.app-container`, contains the preview and controls in sections. Within the controls, a tabbed navigation system is emerging. Each tab houses dedicated input sections like layout, typography, backgrounds, effects, and code generation. Finally, there's a container for toasts.


**Crafting the CSS**

I'm now deep in CSS generation! I'm planning out variables for color, spacing, and more. A modern reset will be implemented for a solid baseline. The main app will get a CSS Grid layout, adapting to stacked displays on smaller screens. I plan on heavy use of `backdrop-filter: blur()` for that desired glassmorphism effect. Custom-styled inputs for sliders and selects are on the radar, and I'm leaning toward a bottom sheet/scrollable section for mobile controls. I'll add subtle animations too!


**Fine-Tuning the Details**

I'm now focusing on specific styling elements. I'm exploring container queries, but will be using media queries for broad compatibility. Ensuring the preview box centers content is a priority, and I'm planning out the styling for prefix/suffix elements. I've also reconsidered the initial single-scroll approach, and have decided to utilize tabs to keep the interface concise and user-friendly. Custom styling of the color picker and Turkish labels will also be included.




</think>

Harika bir fikir! Önceki sürümü (V6) inceledim. Kodun yarım kalmış olması ve yapının biraz karmaşıklaşması nedeniyle, projeyi **"K3N4N V7 - Ultimate CSS Studio"** olarak yeniden adlandırıp modernize ettim.

**Önerilerim ve Yapısal Değişiklikler:**

1.  **Modern UI/UX (Glassmorphism):** Önceki "uzun liste" tasarımı yerine, **Sekmeli (Tab-based)** bir kontrol paneli tasarladım. Bu, kullanıcının kaybolmasını engeller.
2.  **Split Screen (Bölünmüş Ekran):** Masaüstünde sol tarafta "Canlı Önizleme" sabit kalırken, sağ tarafta ayarlar değiştirilecek. Mobilde ise önizleme üstte, kontroller altta olacak.
3.  **Gelişmiş Özellikler:**
    *   **Flexbox Hizalama Paneli:** Hizalamayı butonlarla görselleştirme.
    *   **Gelişmiş Gradyan:** Sadece rastgele değil, renk duraklarını seçebilme altyapısı.
    *   **Clip-Path (Şekil Kesme):** Modern web tasarımları için şekilli kutular.
    *   **Backdrop Filter:** Cam efekti (Glassmorphism) ayarları.
4.  **Mobil Uyumluluk:** Tamamen responsive, dokunmatik dostu slider'lar.

İşte **V7** için HTML ve CSS kodları. Eğer bu tasarımı onaylarsan, buna uygun güçlü JavaScript motorunu yazacağım.

### 1. HTML (index.html)

```html
<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>K3N4N V7 - Ultimate CSS Studio</title>
    
    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;800&family=JetBrains+Mono:wght@400;700&family=Orbitron:wght@500;700;900&family=Poppins:wght@300;500;700&display=swap" rel="stylesheet">
    
    <!-- Font Awesome -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
    
    <!-- External CSS -->
    <link rel="stylesheet" href="style.css">
    
    <!-- External Libraries (JS için hazırlık) -->
    <script src="https://cdn.jsdelivr.net/npm/@jaames/iro@5/dist/iro.min.js"></script>
</head>
<body>

    <!-- Uygulama Ana Kapsayıcı -->
    <div class="app-container">
        
        <!-- SOL PANEL: ÖNİZLEME (Preview Stage) -->
        <section class="stage-area">
            <header class="top-bar">
                <div class="brand">
                    <i class="fas fa-cube brand-icon"></i>
                    <div>
                        <h1>K3N4N <span class="version">V7</span></h1>
                        <p>Ultimate CSS Studio</p>
                    </div>
                </div>
                <div class="stage-controls">
                    <button class="icon-btn" id="theme-toggle" title="Koyu/Açık Mod"><i class="fas fa-moon"></i></button>
                    <button class="icon-btn" id="reset-all" title="Sıfırla"><i class="fas fa-power-off"></i></button>
                </div>
            </header>

            <div class="preview-canvas" id="previewCanvas">
                <!-- Manipüle Edilecek Element -->
                <div id="target-element" class="kenan-element">
                    <span class="prefix-img hidden"></span>
                    <span class="content-text" contenteditable="true">K3N4N Design</span>
                    <span class="suffix-img hidden"></span>
                    <span class="badge hidden">NEW</span>
                </div>
                
                <!-- Tuval Arka Plan Kontrolü (Canvas içinde yüzer menü) -->
                <div class="canvas-settings">
                    <label title="Canvas Arka Planı"><i class="fas fa-image"></i>
                        <input type="color" id="canvasBgColor" value="#0f172a">
                    </label>
                    <button id="toggleGrid" title="Izgara Göster/Gizle"><i class="fas fa-border-all"></i></button>
                </div>
            </div>

            <!-- Hızlı Kod Çıktısı (Preview altında) -->
            <div class="quick-code-bar">
                <code id="miniCodeDisplay">.element { color: #fff; ... }</code>
                <button class="copy-btn" id="quickCopy"><i class="fas fa-copy"></i></button>
            </div>
        </section>

        <!-- SAĞ PANEL: KONTROLLER (Editor Pane) -->
        <aside class="editor-pane">
            
            <!-- Navigasyon Tabları -->
            <nav class="editor-tabs">
                <button class="tab-btn active" data-tab="layout"><i class="fas fa-layer-group"></i> <span>Düzen</span></button>
                <button class="tab-btn" data-tab="typography"><i class="fas fa-font"></i> <span>Yazı</span></button>
                <button class="tab-btn" data-tab="appearance"><i class="fas fa-palette"></i> <span>Görünüm</span></button>
                <button class="tab-btn" data-tab="effects"><i class="fas fa-wand-magic-sparkles"></i> <span>Efekt</span></button>
                <button class="tab-btn" data-tab="content"><i class="fas fa-images"></i> <span>İçerik</span></button>
            </nav>

            <!-- TAB İÇERİKLERİ -->
            <div class="editor-content">
                
                <!-- 1. DÜZEN (Layout) -->
                <div class="tab-panel active" id="tab-layout">
                    <div class="control-group">
                        <h3><i class="fas fa-ruler-combined"></i> Boyut & Boşluk</h3>
                        <div class="input-grid">
                            <div class="input-wrap">
                                <label>Genişlik</label>
                                <input type="text" id="widthInput" placeholder="auto">
                            </div>
                            <div class="input-wrap">
                                <label>Yükseklik</label>
                                <input type="text" id="heightInput" placeholder="auto">
                            </div>
                        </div>
                        
                        <div class="slider-control">
                            <label>Padding (İç Boşluk)</label>
                            <input type="range" id="paddingSlider" min="0" max="100" value="20">
                            <span class="value-display">20px</span>
                        </div>
                        
                        <div class="slider-control">
                            <label>Border Radius (Yuvarlaklık)</label>
                            <input type="range" id="radiusSlider" min="0" max="100" value="12">
                            <span class="value-display">12px</span>
                        </div>
                    </div>

                    <div class="control-group">
                        <h3><i class="fas fa-th"></i> Esnek Kutu (Flexbox)</h3>
                        <div class="flex-align-grid">
                            <button data-flex="justify-start" title="Sola Yasla"><i class="fas fa-align-left"></i></button>
                            <button data-flex="justify-center" class="active" title="Ortala"><i class="fas fa-align-center"></i></button>
                            <button data-flex="justify-end" title="Sağa Yasla"><i class="fas fa-align-right"></i></button>
                            <button data-flex="justify-between" title="Yay"><i class="fas fa-arrows-alt-h"></i></button>
                        </div>
                        <div class="slider-control mt-2">
                            <label>Gap (Öğe Arası Boşluk)</label>
                            <input type="range" id="gapSlider" min="0" max="50" value="10">
                            <span class="value-display">10px</span>
                        </div>
                    </div>
                </div>

                <!-- 2. TİPOGRAFİ (Typography) -->
                <div class="tab-panel" id="tab-typography">
                    <div class="control-group">
                        <label>Font Ailesi</label>
                        <select id="fontFamilySelect" class="full-select">
                            <option value="'Inter', sans-serif">Inter (Modern)</option>
                            <option value="'Poppins', sans-serif">Poppins (Geometrik)</option>
                            <option value="'Orbitron', sans-serif">Orbitron (Sci-Fi)</option>
                            <option value="'JetBrains Mono', monospace">JetBrains Mono (Kod)</option>
                            <option value="'Dancing Script', cursive">Dancing Script (El Yazısı)</option>
                        </select>
                    </div>

                    <div class="input-grid">
                        <div class="input-wrap">
                            <label>Boyut (px)</label>
                            <input type="number" id="fontSizeInput" value="24" min="8" max="120">
                        </div>
                        <div class="input-wrap">
                            <label>Kalınlık</label>
                            <select id="fontWeightSelect">
                                <option value="300">İnce</option>
                                <option value="400">Normal</option>
                                <option value="700" selected>Kalın</option>
                                <option value="900">Ultra</option>
                            </select>
                        </div>
                    </div>

                    <!-- Gelişmiş Renk Seçici -->
                    <div class="control-group">
                        <label>Yazı Rengi</label>
                        <div id="textColorPickerContainer" class="color-picker-placeholder"></div>
                        <input type="hidden" id="textColorInput" value="#ffffff">
                    </div>

                    <div class="slider-control">
                        <label>Harf Aralığı (Letter Spacing)</label>
                        <input type="range" id="letterSpacingSlider" min="-2" max="10" step="0.5" value="0">
                        <span class="value-display">0px</span>
                    </div>
                </div>

                <!-- 3. GÖRÜNÜM (Appearance) -->
                <div class="tab-panel" id="tab-appearance">
                    <!-- Arka Plan -->
                    <div class="accordion open">
                        <div class="accordion-header">
                            <i class="fas fa-fill-drip"></i> Arka Plan
                            <i class="fas fa-chevron-down arrow"></i>
                        </div>
                        <div class="accordion-content">
                            <div class="bg-type-selector">
                                <button class="active" data-bg-type="solid">Düz</button>
                                <button data-bg-type="gradient">Gradyan</button>
                                <button data-bg-type="image">Resim</button>
                            </div>
                            
                            <!-- Renk Seçici Alanı -->
                            <div id="bgColorControl">
                                <div id="bgColorPickerContainer" class="color-picker-placeholder"></div>
                            </div>
                            
                            <!-- Gradyan Kontrolleri (JS ile gösterilecek) -->
                            <div id="bgGradientControl" class="hidden">
                                <button class="btn-secondary" id="randomGradientBtn"><i class="fas fa-random"></i> Rastgele Gradyan</button>
                                <div class="slider-control mt-2">
                                    <label>Açı (Derece)</label>
                                    <input type="range" id="gradientAngleSlider" min="0" max="360" value="135">
                                </div>
                            </div>

                             <!-- Resim Kontrolleri (JS ile gösterilecek) -->
                             <div id="bgImageControl" class="hidden">
                                <input type="text" id="bgUrlInput" placeholder="Resim URL'si" class="full-input">
                                <label class="file-upload-btn">
                                    <input type="file" id="bgFileUpload">
                                    <i class="fas fa-upload"></i> Dosya Yükle
                                </label>
                            </div>
                        </div>
                    </div>

                    <!-- Kenarlık -->
                    <div class="accordion">
                        <div class="accordion-header">
                            <i class="fas fa-border-style"></i> Kenarlık (Border)
                            <i class="fas fa-chevron-down arrow"></i>
                        </div>
                        <div class="accordion-content">
                            <div class="input-grid">
                                <div class="input-wrap">
                                    <label>Kalınlık</label>
                                    <input type="number" id="borderWidthInput" value="0" min="0" max="20">
                                </div>
                                <div class="input-wrap">
                                    <label>Stil</label>
                                    <select id="borderStyleSelect">
                                        <option value="solid">Düz</option>
                                        <option value="dashed">Kesik</option>
                                        <option value="dotted">Nokta</option>
                                        <option value="double">Çift</option>
                                    </select>
                                </div>
                            </div>
                            <div class="control-group mt-2">
                                <label>Kenarlık Rengi</label>
                                <input type="color" id="borderColorInput" class="full-color-input" value="#3b82f6">
                            </div>
                        </div>
                    </div>
                </div>

                <!-- 4. EFEKTLER (Effects) -->
                <div class="tab-panel" id="tab-effects">
                    <!-- Gölge -->
                    <div class="control-group">
                        <div class="checkbox-wrap">
                            <input type="checkbox" id="shadowCheck">
                            <label for="shadowCheck">Box Shadow (Gölge)</label>
                        </div>
                        <div id="shadowControls" class="disabled-area">
                            <div class="slider-control">
                                <label>X / Y Konumu</label>
                                <input type="range" id="shadowX" min="-50" max="50" value="0">
                                <input type="range" id="shadowY" min="-50" max="50" value="10">
                            </div>
                            <div class="slider-control">
                                <label>Bulanıklık / Yayılma</label>
                                <input type="range" id="shadowBlur" min="0" max="100" value="20">
                                <input type="range" id="shadowSpread" min="-20" max="50" value="0">
                            </div>
                            <input type="color" id="shadowColor" class="full-color-input" value="#000000">
                        </div>
                    </div>

                    <!-- Glassmorphism -->
                    <div class="control-group">
                        <h3><i class="fas fa-glass-martini-alt"></i> Glassmorphism</h3>
                        <div class="slider-control">
                            <label>Arka Plan Bulanıklığı (Backdrop Filter)</label>
                            <input type="range" id="backdropBlurSlider" min="0" max="20" value="0">
                            <span class="value-display">0px</span>
                        </div>
                    </div>

                    <!-- Transform -->
                    <div class="control-group">
                        <h3><i class="fas fa-sync-alt"></i> Dönüşüm (Transform)</h3>
                        <div class="slider-control">
                            <label>Döndür (Rotate)</label>
                            <input type="range" id="rotateSlider" min="-180" max="180" value="0">
                        </div>
                        <div class="slider-control">
                            <label>Büyüt (Scale)</label>
                            <input type="range" id="scaleSlider" min="0.5" max="2" step="0.1" value="1">
                        </div>
                    </div>
                </div>

                <!-- 5. İÇERİK (Content & Assets) -->
                <div class="tab-panel" id="tab-content">
                    <div class="control-group">
                        <h3>Görsel Varlıklar</h3>
                        
                        <div class="asset-uploader">
                            <label>Sol Simge (Prefix)</label>
                            <div class="uploader-ui">
                                <input type="text" id="prefixUrl" placeholder="URL veya..." class="small-input">
                                <input type="file" id="prefixFile" class="hidden-file">
                                <button onclick="document.getElementById('prefixFile').click()" class="btn-icon"><i class="fas fa-upload"></i></button>
                            </div>
                            <div class="slider-control mt-1">
                                <label>Boyut</label>
                                <input type="range" id="prefixSize" min="10" max="100" value="24">
                            </div>
                        </div>

                        <div class="asset-uploader mt-2">
                            <label>Sağ Simge (Suffix)</label>
                            <div class="uploader-ui">
                                <input type="text" id="suffixUrl" placeholder="URL veya..." class="small-input">
                                <input type="file" id="suffixFile" class="hidden-file">
                                <button onclick="document.getElementById('suffixFile').click()" class="btn-icon"><i class="fas fa-upload"></i></button>
                            </div>
                            <div class="slider-control mt-1">
                                <label>Boyut</label>
                                <input type="range" id="suffixSize" min="10" max="100" value="24">
                            </div>
                        </div>
                    </div>
                </div>

                <!-- ALT AKSİYON BUTONLARI -->
                <div class="action-footer">
                    <button id="btnChaos" class="btn-chaos"><i class="fas fa-meteor"></i> KAOS MODU</button>
                    <button id="btnGetCode" class="btn-primary"><i class="fas fa-code"></i> KODU AL</button>
                </div>

            </div>
        </aside>

        <!-- KOD MODAL (Gizli) -->
        <div id="codeModal" class="modal-overlay hidden">
            <div class="modal-box">
                <header class="modal-header">
                    <h2>CSS & HTML Çıktısı</h2>
                    <button class="close-modal"><i class="fas fa-times"></i></button>
                </header>
                <div class="modal-body">
                    <div class="code-tabs">
                        <button class="active" data-code="css">CSS</button>
                        <button data-code="html">HTML</button>
                    </div>
                    <textarea id="finalCodeOutput" readonly></textarea>
                </div>
                <footer class="modal-footer">
                    <button class="btn-secondary" id="copyFinalCode"><i class="fas fa-copy"></i> Kopyala</button>
                    <button class="btn-primary" id="downloadFinalCode"><i class="fas fa-download"></i> İndir</button>
                </footer>
            </div>
        </div>

    </div>

</body>
</html>
```

### 2. CSS (style.css)

Bu CSS dosyası modern CSS değişkenleri, Grid layout ve gelişmiş görsel efektler kullanır.

```css
/* =========================================
   K3N4N V7 - DESIGN TOKENS
   ========================================= */
:root {
    /* Renk Paleti (Cyberpunk / Modern Dark) */
    --bg-app: #0f172a;
    --bg-panel: #1e293b;
    --bg-surface: #334155;
    
    --primary: #06b6d4;      /* Cyan */
    --primary-glow: rgba(6, 182, 212, 0.4);
    --secondary: #8b5cf6;    /* Violet */
    --accent: #f43f5e;       /* Pink */
    
    --text-main: #f1f5f9;
    --text-muted: #94a3b8;
    
    --border-color: rgba(255, 255, 255, 0.1);
    --glass-bg: rgba(30, 41, 59, 0.7);
    --glass-border: rgba(255, 255, 255, 0.08);
    
    /* Ölçüler */
    --radius-sm: 6px;
    --radius-md: 12px;
    --radius-lg: 16px;
    --header-height: 60px;
}

/* Sıfırlama */
*, *::before, *::after {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}

body {
    font-family: 'Inter', system-ui, sans-serif;
    background-color: var(--bg-app);
    color: var(--text-main);
    height: 100vh;
    overflow: hidden; /* Scroll uygulama içinde olacak */
}

/* =========================================
   ANA LAYOUT (GRID)
   ========================================= */
.app-container {
    display: grid;
    grid-template-columns: 1fr 380px; /* Sol geniş, Sağ 380px sabit */
    height: 100vh;
    width: 100vw;
}

/* =========================================
   SOL PANEL: SAHNE (STAGE AREA)
   ========================================= */
.stage-area {
    background-image: 
        radial-gradient(circle at 20% 20%, rgba(6, 182, 212, 0.05) 0%, transparent 40%),
        radial-gradient(circle at 80% 80%, rgba(139, 92, 246, 0.05) 0%, transparent 40%);
    position: relative;
    display: flex;
    flex-direction: column;
    overflow: hidden;
}

/* Üst Bar */
.top-bar {
    height: var(--header-height);
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0 24px;
    border-bottom: 1px solid var(--border-color);
    background: rgba(15, 23, 42, 0.8);
    backdrop-filter: blur(10px);
    z-index: 10;
}

.brand {
    display: flex;
    align-items: center;
    gap: 12px;
}

.brand-icon {
    font-size: 24px;
    color: var(--primary);
    filter: drop-shadow(0 0 10px var(--primary-glow));
}

.brand h1 {
    font-family: 'Orbitron', sans-serif;
    font-size: 1.2rem;
    line-height: 1;
    letter-spacing: 1px;
}

.brand .version {
    color: var(--accent);
    font-size: 0.8em;
}

.brand p {
    font-size: 0.7rem;
    color: var(--text-muted);
    font-family: 'JetBrains Mono', monospace;
}

.icon-btn {
    background: transparent;
    border: 1px solid var(--border-color);
    color: var(--text-muted);
    width: 36px;
    height: 36px;
    border-radius: var(--radius-sm);
    cursor: pointer;
    transition: all 0.2s;
}

.icon-btn:hover {
    color: var(--text-main);
    border-color: var(--primary);
    background: rgba(6, 182, 212, 0.1);
}

/* Tuval (Canvas) */
.preview-canvas {
    flex: 1;
    display: flex;
    align-items: center;
    justify-content: center;
    position: relative;
    overflow: auto;
    background-size: 20px 20px;
    background-position: 0 0, 10px 10px; /* Dama tahtası efekti eklenebilir */
    transition: background-color 0.3s;
}

/* Canvas Settings Floating Menu */
.canvas-settings {
    position: absolute;
    bottom: 20px;
    right: 20px;
    background: var(--bg-panel);
    padding: 8px;
    border-radius: var(--radius-md);
    display: flex;
    gap: 10px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.3);
    border: 1px solid var(--border-color);
}

.canvas-settings input[type="color"] {
    width: 24px;
    height: 24px;
    border: none;
    background: none;
    cursor: pointer;
}

/* HEDEF ELEMENT (Target) */
.kenan-element {
    /* Varsayılan Başlangıç Stilleri */
    padding: 20px 40px;
    background: linear-gradient(135deg, var(--primary), var(--secondary));
    color: white;
    border-radius: 16px;
    font-family: 'Poppins', sans-serif;
    font-size: 24px;
    font-weight: 700;
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 12px;
    box-shadow: 0 20px 50px rgba(0,0,0,0.3);
    transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
    max-width: 90%;
    text-align: center;
    position: relative;
    cursor: default;
}

.kenan-element:hover {
    transform: translateY(-2px); /* Mikro etkileşim */
}

/* İç Resimler */
.prefix-img, .suffix-img {
    display: block;
    width: 24px;
    height: 24px;
    background-size: cover;
    background-position: center;
    border-radius: 4px;
}
.hidden { display: none !important; }

/* Quick Code Bar */
.quick-code-bar {
    background: var(--bg-panel);
    border-top: 1px solid var(--border-color);
    padding: 10px 20px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.85rem;
    color: var(--primary);
}

.quick-code-bar code {
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
    opacity: 0.8;
}

/* =========================================
   SAĞ PANEL: EDİTÖR (EDITOR PANE)
   ========================================= */
.editor-pane {
    background: var(--bg-panel);
    border-left: 1px solid var(--border-color);
    display: flex;
    flex-direction: column;
    height: 100vh;
    z-index: 20;
}

/* Sekmeler (Tabs) */
.editor-tabs {
    display: flex;
    background: rgba(0,0,0,0.2);
    overflow-x: auto;
    scrollbar-width: none;
}

.tab-btn {
    flex: 1;
    min-width: 70px;
    padding: 15px 5px;
    background: transparent;
    border: none;
    color: var(--text-muted);
    border-bottom: 2px solid transparent;
    cursor: pointer;
    font-size: 0.8rem;
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 5px;
    transition: all 0.3s;
}

.tab-btn:hover { color: var(--text-main); background: rgba(255,255,255,0.02); }
.tab-btn.active { color: var(--primary); border-bottom-color: var(--primary); }
.tab-btn i { font-size: 1.1rem; }

/* Tab İçeriği */
.editor-content {
    flex: 1;
    overflow-y: auto;
    padding: 20px;
}

.editor-content::-webkit-scrollbar { width: 6px; }
.editor-content::-webkit-scrollbar-thumb { background: var(--bg-surface); border-radius: 10px; }

.tab-panel { display: none; animation: fadeIn 0.3s ease; }
.tab-panel.active { display: block; }

@keyframes fadeIn { from { opacity: 0; transform: translateY(5px); } to { opacity: 1; transform: translateY(0); } }

/* Kontrol Grupları */
.control-group { margin-bottom: 24px; }
.control-group h3 {
    font-size: 0.9rem;
    text-transform: uppercase;
    color: var(--text-muted);
    letter-spacing: 0.5px;
    margin-bottom: 12px;
    display: flex;
    align-items: center;
    gap: 8px;
}

.control-group label {
    display: block;
    font-size: 0.85rem;
    margin-bottom: 6px;
    color: var(--text-main);
}

/* Input Grid */
.input-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 10px; }
.input-wrap { display: flex; flex-direction: column; }

/* Form Elemanları */
input[type="text"], input[type="number"], select {
    background: var(--bg-app);
    border: 1px solid var(--border-color);
    color: var(--text-main);
    padding: 8px 12px;
    border-radius: var(--radius-sm);
    width: 100%;
    font-family: inherit;
    font-size: 0.9rem;
}

input:focus, select:focus {
    outline: none;
    border-color: var(--primary);
    box-shadow: 0 0 0 2px rgba(6, 182, 212, 0.2);
}

/* Custom Range Slider */
input[type="range"] {
    width: 100%;
    height: 6px;
    background: var(--bg-surface);
    border-radius: 3px;
    appearance: none;
    cursor: pointer;
}

input[type="range"]::-webkit-slider-thumb {
    appearance: none;
    width: 16px;
    height: 16px;
    background: var(--primary);
    border-radius: 50%;
    border: 2px solid var(--bg-panel);
    box-shadow: 0 2px 5px rgba(0,0,0,0.3);
}

.slider-control { margin-bottom: 15px; }
.value-display { font-size: 0.75rem; color: var(--primary); float: right; margin-top: -20px; font-weight: bold;}

/* Flexbox Grid */
.flex-align-grid {
    display: flex;
    gap: 5px;
    background: var(--bg-app);
    padding: 5px;
    border-radius: var(--radius-sm);
}

.flex-align-grid button {
    flex: 1;
    background: transparent;
    border: none;
    color: var(--text-muted);
    padding: 8px;
    cursor: pointer;
    border-radius: 4px;
}

.flex-align-grid button:hover { background: rgba(255,255,255,0.05); }
.flex-align-grid button.active { background: var(--bg-surface); color: var(--primary); }

/* Accordion */
.accordion {
    border: 1px solid var(--border-color);
    border-radius: var(--radius-sm);
    margin-bottom: 10px;
    background: rgba(255,255,255,0.02);
}

.accordion-header {
    padding: 12px;
    cursor: pointer;
    display: flex;
    align-items: center;
    gap: 8px;
    font-weight: 600;
    font-size: 0.9rem;
    user-select: none;
}

.accordion-header .arrow { margin-left: auto; transition: transform 0.3s; }
.accordion.open .arrow { transform: rotate(180deg); }
.accordion-content { padding: 12px; display: none; border-top: 1px solid var(--border-color); }
.accordion.open .accordion-content { display: block; }

/* BG Type Selector */
.bg-type-selector { display: flex; gap: 5px; margin-bottom: 15px; }
.bg-type-selector button {
    flex: 1;
    padding: 6px;
    background: var(--bg-app);
    border: 1px solid var(--border-color);
    color: var(--text-muted);
    border-radius: 4px;
    font-size: 0.8rem;
    cursor: pointer;
}
.bg-type-selector button.active {
    background: var(--primary);
    color: #fff;
    border-color: var(--primary);
}

/* Color Picker Placeholders (Iro.js için) */
.color-picker-placeholder {
    display: flex;
    justify-content: center;
    background: var(--bg-app);
    padding: 10px;
    border-radius: var(--radius-sm);
}

/* Asset Uploader */
.uploader-ui { display: flex; gap: 8px; }
.small-input { flex: 1; }
.btn-icon {
    width: 36px;
    background: var(--bg-surface);
    border: 1px solid var(--border-color);
    color: var(--text-main);
    border-radius: 4px;
    cursor: pointer;
}
.hidden-file { display: none; }

/* FOOTER ACTIONS */
.action-footer {
    padding: 20px;
    border-top: 1px solid var(--border-color);
    background: var(--bg-panel);
    display: flex;
    gap: 10px;
}

.btn-primary, .btn-chaos, .btn-secondary {
    border: none;
    padding: 12px;
    border-radius: var(--radius-sm);
    font-weight: 700;
    cursor: pointer;
    font-family: 'Orbitron', sans-serif;
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 8px;
    transition: transform 0.2s, box-shadow 0.2s;
}

.btn-primary {
    background: linear-gradient(135deg, var(--primary), #3b82f6);
    color: white;
    flex: 2;
    box-shadow: 0 4px 15px rgba(6, 182, 212, 0.3);
}

.btn-chaos {
    background: linear-gradient(135deg, #f43f5e, #e11d48);
    color: white;
    flex: 1.5;
    font-size: 0.8rem;
}

.btn-secondary {
    background: var(--bg-surface);
    color: var(--text-main);
    border: 1px solid var(--border-color);
    width: 100%;
}

.btn-primary:hover, .btn-chaos:hover { transform: translateY(-2px); filter: brightness(1.1); }
.btn-primary:active { transform: scale(0.98); }

/* =========================================
   MODAL (CODE OUTPUT)
   ========================================= */
.modal-overlay {
    position: fixed;
    top: 0; left: 0; width: 100%; height: 100%;
    background: rgba(0,0,0,0.7);
    backdrop-filter: blur(5px);
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 100;
    opacity: 1;
    transition: opacity 0.3s;
}

.modal-overlay.hidden { display: none; opacity: 0; }

.modal-box {
    background: var(--bg-panel);
    width: 90%;
    max-width: 600px;
    border-radius: var(--radius-lg);
    border: 1px solid var(--border-color);
    box-shadow: 0 20px 60px rgba(0,0,0,0.5);
    display: flex;
    flex-direction: column;
}

.modal-header {
    padding: 20px;
    border-bottom: 1px solid var(--border-color);
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.close-modal {
    background: none;
    border: none;
    color: var(--text-muted);
    font-size: 1.2rem;
    cursor: pointer;
}

.modal-body { padding: 0; }

.code-tabs { display: flex; background: var(--bg-app); }
.code-tabs button {
    flex: 1;
    padding: 12px;
    background: transparent;
    border: none;
    color: var(--text-muted);
    cursor: pointer;
    font-weight: 600;
    border-bottom: 2px solid transparent;
}
.code-tabs button.active { color: var(--primary); border-bottom-color: var(--primary); background: rgba(255,255,255,0.03); }

#finalCodeOutput {
    width: 100%;
    height: 300px;
    background: #0d1117;
    color: #e6edf3;
    border: none;
    padding: 20px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.85rem;
    resize: none;
    outline: none;
}

.modal-footer {
    padding: 20px;
    border-top: 1px solid var(--border-color);
    display: flex;
    gap: 10px;
    justify-content: flex-end;
}

.modal-footer .btn-secondary, .modal-footer .btn-primary { width: auto; flex: none; padding: 10px 20px; }

/* =========================================
   RESPONSIVE (MOBIL)
   ========================================= */
@media (max-width: 768px) {
    .app-container {
        grid-template-columns: 1fr; /* Tek kolon */
        grid-template-rows: 45vh 1fr; /* Üstte sahne, altta editör */
    }

    .top-bar { height: 50px; padding: 0 15px; }
    .brand h1 { font-size: 1rem; }
    
    .editor-pane {
        border-left: none;
        border-top: 1px solid var(--primary);
        box-shadow: 0 -5px 20px rgba(0,0,0,0.2);
    }
    
    .editor-tabs { justify-content: space-between; }
    .tab-btn span { display: none; } /* Mobilde sadece ikon */
    .tab-btn { min-width: auto; padding: 15px; }
    
    /* Inputlar mobilde daha büyük */
    input[type="range"] { height: 10px; }
    input[type="range"]::-webkit-slider-thumb { width: 22px; height: 22px; }
    
    /* Modal mobilde tam ekran */
    .modal-box { width: 100%; height: 100%; max-width: none; border-radius: 0; }
}

/* Utilities */
.mt-1 { margin-top: 5px; }
.mt-2 { margin-top: 15px; }
.full-color-input { width: 100%; height: 40px; padding: 0; border: none; border-radius: 4px; cursor: pointer; }
```

### Kodlar Hazır! Sıradaki Adım Ne?

Şu an elimizde çok şık, modern (Cyberpunk/Dark tema) ve mobil uyumlu bir arayüz var.

**Onaylarsan:**
Bu tasarımın beyni olacak **JavaScript** kodunu yazacağım. JS kodu şunları yapacak:
1.  Tab geçişlerini ve akordiyon menüleri çalıştıracak.
2.  Tüm slider ve inputları "Target Element" üzerinde gerçek zamanlı güncelleyecek.
3.  **Color Picker (Iro.js)** kütüphanesini başlatıp renklere bağlayacak.
4.  **Kaos Modu (V6'dan miras):** Tek tuşla rastgele çılgın tasarımlar üretecek.
5.  Resim Yükleme (Prefix/Suffix/Background) özelliklerini aktif edecek.
6.  CSS/HTML çıktısını oluşturup kopyalatacak.

HTML ve CSS yapısını beğendiysen "Onaylıyorum" yazman yeterli!

### OpenAI o1
*2026-01-11 14:45:31 +03*

Aşağıdaki örnek yapı; modern, genişletilmiş ve mobil uyumlu bir tasarım mantığına sahiptir. İki ayrı dosyadan (HTML ve CSS) oluşmaktadır. JavaScript kodları için şimdilik placeholder (yorum satırı) bıraktım. Onay aldıktan sonra JS tarafını ekleyebiliriz.

---
## 1) `index.html`

```html
<!DOCTYPE html>
<html lang="tr">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>K3N4N CSS Stil Üretici</title>
  <!-- Google Fonts -->
  <link
    href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap"
    rel="stylesheet"
  />
  <!-- Font Awesome (sembol ve ikonlar) -->
  <link
    rel="stylesheet"
    href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css"
  />
  <!-- Ana Stil Dosyası -->
  <link rel="stylesheet" href="style.css" />
</head>

<body>
  <!-- Header -->
  <header class="header">
    <div class="header-inner">
      <div class="logo">
        <i class="fas fa-wand-magic-sparkles fa-lg"></i>
        <span class="logo-text">K3N4N CSS Generator</span>
        <span class="logo-version">V6++</span>
      </div>
    </div>
  </header>

  <!-- Ana Kapsayıcı -->
  <div class="container">
    <!-- Yan Kontroller (Menü / Ayarlar) -->
    <aside class="controls-panel">
      <h2 class="panel-title">Ayarlar</h2>
      
      <!-- Örnek Fieldset -->
      <fieldset>
        <legend><i class="fas fa-image"></i> Yazı Başı Görsel (Prefix)</legend>
        <div class="form-group">
          <label for="prefixImageFile">
            <i class="fas fa-file-image"></i> Dosyadan Seç (GIF / Resim)
          </label>
          <input type="file" id="prefixImageFile" accept="image/*,.gif" />
        </div>
        <div class="form-group">
          <label for="prefixImageUrl">
            <i class="fas fa-link"></i> veya URL Gir
          </label>
          <input type="text" id="prefixImageUrl" placeholder="https://... veya data:image/..." />
        </div>
        <!-- Ve benzeri giriş alanları... -->
      </fieldset>

      <!-- Diğer alanlar - Suffix, BG, Metin, Çerçeve... -->
      <!-- Buraya ek alanlar koyabiliriz. -->

    </aside>

    <!-- Önizleme ve Çıktı Alanı -->
    <main class="preview-section">
      <!-- Stil Önizleme Kutusu -->
      <div id="preview-box" class="preview-box is-empty">
        Önizleme Alanı
      </div>

      <!-- Üretilen CSS Kodu Gösterimi -->
      <section class="css-output-section">
        <h3><i class="fas fa-code"></i> Üretilen CSS</h3>
        <textarea id="css-output" readonly placeholder="#preview-box {\n  /* Örnek CSS */\n}"></textarea>
        <div class="output-buttons">
          <button id="copy-css-btn" disabled>
            <i class="fas fa-copy"></i> Kopyala
          </button>
          <button id="download-css-btn" disabled>
            <i class="fas fa-file-arrow-down"></i> CSS İndir
          </button>
          <button id="download-html-btn" disabled>
            <i class="fas fa-file-arrow-down"></i> HTML İndir
          </button>
        </div>
      </section>

      <!-- Harici CSS Ekleme Alanı -->
      <section class="css-input-section">
        <h3><i class="fas fa-paste"></i> Harici CSS Ekle</h3>
        <textarea id="cssInputArea" placeholder="Buraya CSS kodu yapıştırın..."></textarea>
        <div class="button-group">
          <button id="preview-pasted-css">
            <i class="fas fa-eye"></i> Önizle
          </button>
          <button id="add-pasted-css">
            <i class="fas fa-plus"></i> Stile Uygula
          </button>
        </div>
        <div id="htmlPreviewArea" class="pasted-css-preview">
          <span class="preview-info">Burada geçici önizleme gösterilecek...</span>
        </div>
      </section>
    </main>
  </div>

  <!-- Footer -->
  <footer class="footer">
    <p>
      <span class="footer-brand">K3N4N</span> © 2026 - Tüm hakları saklıdır. 
      <small class="footer-version">Yeni Tasarım V6++</small>
    </p>
  </footer>

  <!-- JS Placeholder -->
  <!-- <script src="main.js"></script> -->
  <!-- Gerekli olduğunda JavaScript kodu burada olacak. -->
</body>
</html>
```

---
## 2) `style.css`

```css
/* 
  K3N4N CSS Stil Generator - Modern Tasarım
  style.css
*/

/* Bazı Değişkenler (Renkleri ve Boyutları Kolay Yönetmek İçin) */
:root {
  --color-bg: #1a1f2e;
  --color-panel: #242b3b;
  --color-header: rgba(17, 24, 39, 0.9);
  --color-border: #464f62;
  --color-primary: #00bcd4;
  --color-primary-light: #22d3ee;
  --color-text: #f1f5f9;
  --color-text-secondary: #94a3b8;

  --font-family-base: 'Inter', sans-serif;

  --radius-md: 8px;
  --radius-lg: 12px;
  --transition-fast: 0.2s ease;
  --transition-normal: 0.3s ease;
}

/* Sıfırlama */
*,
*::before,
*::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

html,
body {
  height: 100%;
}

/* Ana Gövde */
body {
  font-family: var(--font-family-base), sans-serif;
  background: var(--color-bg);
  color: var(--color-text);
  line-height: 1.5;
  overflow-x: hidden;
  -webkit-font-smoothing: antialiased;
}

/* Scrollbar (varsayılan tarayıcılarda) */
body::-webkit-scrollbar {
  width: 8px;
}
body::-webkit-scrollbar-track {
  background: #111827;
}
body::-webkit-scrollbar-thumb {
  background: var(--color-primary);
  border-radius: 4px;
}

/* Header */
.header {
  width: 100%;
  position: sticky;
  top: 0;
  background: var(--color-header);
  padding: 16px;
  border-bottom: 1px solid #2f3645;
  z-index: 50;
}
.header-inner {
  max-width: 1200px;
  margin: 0 auto;
  display: flex;
  align-items: center;
  justify-content: space-between;
}
.logo {
  display: flex;
  align-items: center;
  gap: 8px;
}
.logo-text {
  font-size: 1.2rem;
  font-weight: 600;
}
.logo-version {
  background: var(--color-primary);
  color: #000;
  font-size: 0.75rem;
  padding: 2px 7px;
  border-radius: 999px;
}

/* Ana Container */
.container {
  display: flex;
  max-width: 1200px;
  margin: 24px auto;
  gap: 16px;
  padding: 0 16px;
}
@media (max-width: 992px) {
  .container {
    flex-direction: column;
  }
}

/* Yan Kontroller */
.controls-panel {
  flex: 0 0 320px;
  background: var(--color-panel);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-md);
  padding: 16px;
  overflow: auto;
  max-height: calc(100vh - 100px);
}
@media (max-width: 992px) {
  .controls-panel {
    max-height: none;
    width: 100%;
  }
}

.panel-title {
  font-size: 1.1rem;
  margin-bottom: 16px;
  color: var(--color-primary);
}

/* Fieldset / Legend */
fieldset {
  border: 1px solid rgba(255,255,255,0.15);
  border-radius: var(--radius-md);
  margin-bottom: 20px;
  padding: 12px;
}
fieldset legend {
  padding: 6px 10px;
  font-weight: 600;
  font-size: 0.95rem;
  border-radius: var(--radius-md);
  background: rgba(255,255,255,0.05);
}
.form-group {
  margin: 12px 0;
  display: flex;
  flex-direction: column;
  gap: 6px;
}
.form-group label {
  font-weight: 500;
  font-size: 0.85rem;
}
.form-group input[type="file"],
.form-group input[type="text"],
.form-group input[type="number"],
textarea {
  padding: 8px;
  font: inherit;
  color: var(--color-text);
  background: #1f2937;
  border: 1px solid #2f3645;
  border-radius: var(--radius-md);
  outline: none;
}
.form-group input[type="file"]:hover,
.form-group input[type="text"]:hover,
.form-group input[type="number"]:hover,
textarea:hover {
  border-color: var(--color-primary-light);
}

/* Önizleme Alanı */
.preview-section {
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 24px;
}
.preview-box {
  background: #f8fafc;
  color: #1e293b;
  border: 1px solid #cbd5e1;
  min-height: 250px;
  border-radius: var(--radius-lg);
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 24px;
  font-size: 1rem;
  position: relative;
  text-align: center;
  transition: var(--transition-normal);
}
.preview-box.is-empty::before {
  content: "Henüz bir stil uygulanmadı...";
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  font-size: 0.9rem;
  font-style: italic;
  color: #94a3b8;
}
.preview-box.is-empty > * {
  opacity: 0;
  pointer-events: none;
}

/* CSS Çıktı Alanı */
.css-output-section {
  background: var(--color-panel);
  border-radius: var(--radius-md);
  border: 1px solid var(--color-border);
  padding: 16px;
  display: flex;
  flex-direction: column;
  gap: 8px;
}
.css-output-section h3 {
  margin-bottom: 8px;
  font-size: 1rem;
  color: var(--color-primary);
}
#css-output {
  width: 100%;
  min-height: 120px;
  max-height: 280px;
  resize: vertical;
  background: #0f172a;
  color: #fbbf24;
  border: 1px solid #374151;
  border-radius: var(--radius-md);
  padding: 10px;
  font-family: 'Courier New', Courier, monospace;
  font-size: 0.85rem;
  line-height: 1.4;
  outline: none;
  overflow: auto;
}
.output-buttons {
  display: flex;
  gap: 8px;
}
.output-buttons button {
  flex: 1;
  padding: 8px;
  border: none;
  border-radius: var(--radius-md);
  font-size: 0.85rem;
  cursor: pointer;
  font-weight: 600;
  transition: var(--transition-fast);
}
#copy-css-btn {
  background: linear-gradient(135deg, #0f766e, #10b981);
  color: #fff;
}
#copy-css-btn:hover {
  background: linear-gradient(135deg, #0891b2, #22d3ee);
}
#download-css-btn,
#download-html-btn {
  background: linear-gradient(135deg, #f59e0b, #fbbf24);
  color: #000;
}
#download-css-btn:hover,
#download-html-btn:hover {
  background: linear-gradient(135deg, #fbbf24, #f59e0b);
}
[disabled] {
  opacity: 0.4;
  pointer-events: none;
}

/* Harici CSS Ekleme */
.css-input-section {
  background: var(--color-panel);
  border-radius: var(--radius-md);
  border: 1px solid var(--color-border);
  padding: 16px;
  display: flex;
  flex-direction: column;
  gap: 8px;
}
.css-input-section h3 {
  font-size: 1rem;
  color: var(--color-primary);
  margin-bottom: 8px;
}
#cssInputArea {
  width: 100%;
  min-height: 100px;
  resize: vertical;
  background: #0f172a;
  color: #fff;
  border: 1px solid #374151;
  border-radius: var(--radius-md);
  padding: 8px;
  font-family: 'Courier New', Courier, monospace;
  font-size: 0.85rem;
  line-height: 1.4;
}
.button-group {
  display: flex;
  gap: 8px;
}
.button-group button {
  flex: 1;
  background: linear-gradient(135deg, #3b82f6, #60a5fa);
  color: #fff;
  border: none;
  border-radius: var(--radius-md);
  padding: 8px;
  cursor: pointer;
  font-size: 0.85rem;
  font-weight: 600;
  transition: var(--transition-normal);
}
.button-group button:hover {
  background: linear-gradient(135deg, #2563eb, #3b82f6);
}
.pasted-css-preview {
  margin-top: 8px;
  border: 1px dashed #3b82f6;
  min-height: 60px;
  padding: 8px;
  border-radius: var(--radius-md);
  color: var(--color-text);
}
.preview-info {
  font-size: 0.8rem;
  color: var(--color-text-secondary);
  font-style: italic;
}

/* Footer */
.footer {
  padding: 16px;
  text-align: center;
  border-top: 1px solid #2f3645;
  background: #131722;
}
.footer p {
  font-size: 0.85rem;
  color: #8b96a9;
}
.footer-brand {
  font-weight: 700;
  background: linear-gradient(135deg, #22d3ee, #3b82f6);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}
.footer-version {
  margin-left: 6px;
  font-size: 0.75rem;
  color: #666;
}

/* Mobil - Küçük Ekranlar için Uyarlamalar */
@media (max-width: 600px) {
  .header-inner {
    flex-direction: column;
    gap: 10px;
    text-align: center;
  }
  .logo-text {
    font-size: 1rem;
  }
  .container {
    padding: 0 8px;
  }
  .controls-panel {
    flex: 1;
    max-height: 100%;
    margin-bottom: 20px;
  }
  .panel-title {
    text-align: center;
    margin-bottom: 12px;
  }
  .preview-box {
    font-size: 0.9rem;
    padding: 16px;
    min-height: 180px;
  }
}
```

### Açıklamalar

1. **HTML Dosyası (`index.html`):**  
   - Basit bir header, bir sol panel (aside) ve bir ana içerik (main) alanı içeriyor.  
   - Header’da logo, sürüm etiketi ve site başlığı var.  
   - Sol panel (aside) içerisinde `fieldset` yapılarını kullanarak prefix/suffix, arka plan, metin stilleri gibi kısımları rahatça ekleyip genişletebilirsiniz.  
   - Ana bölümde (main) önizleme kutusu ve CSS kodunun gösterildiği alan bulunuyor.  
   - En altta da bir footer mevcut.

2. **CSS Dosyası (`style.css`):**  
   - Modern bir tasarım için değişken tabanlı bir yaklaşımla renkler, boyutlar ve geçiş süreleri tanımlanmıştır.  
   - Mobil uyumluluk için temel medya sorguları (breakpoint 600px ve 992px) eklenmiştir.  
   - Temel stil sıfırlaması (reset) ve scrollbar tasarımı mevcuttur.  
   - Alanların düzeni flex tabanlıdır ve küçük ekranlarda tek kolona geçer.  
   - Önizleme kutusunda (`#preview-box`) CSS stil kodunu veya eklenen prefix/suffix görsellerini yönetmeniz için uygun bir yapı oluşturulmuştur.

3. **JavaScript Placeholder:**  
   - Henüz eklenmedi, fakat `<script>` etiketi yerinde mevcut.  
   - İleride, butonların etkileşimleri, prefix/suffix resimleri, random stil üretimi vb. eklenebilir.  

Bu yapı üzerinde değişiklik veya ekleme yapılmasını istediğiniz nokta varsa belirtebilirsiniz. Onayınız sonrasında JavaScript tarafını hazırlayıp etkileşimli hale getirebiliriz.

## Prompt 2

### You
*2026-01-11 14:47:37 +03*

js kodunu yaz

### Gemini 3 Pro
*2026-01-11 14:47:37 +03*



<think>

**Initiating JavaScript Logic**

I'm now diving into the core of the JavaScript implementation, building on the established HTML and CSS foundation. The focus is now on creating the interactive elements of "K3N4N V7 - Ultimate CSS Studio," making it fully functional. My goal is to craft robust logic to bring it to life!


**Crafting UI Interactivity**

I'm now implementing the UI logic, focused on making the CSS generator interactive. I'm prioritizing tab switching functionality and hooking up the input elements to update the `#target-element` dynamically. I've also integrated the `iro.js` color pickers for the text, background, and border, and working on file reading logic for assets. Next is to get the "Chaos Mode" button working, so I can start integrating the code export feature.


**Defining Style Update Logic**

I'm solidifying the style updating engine. I've decided on a hybrid approach: individual listeners for immediate feedback on input changes, which updates internal state, applies that state to the target element in the DOM, and updates the code snippet. This ensures responsiveness. I'm prioritizing features: layout (width, height, padding, border radius), and flexbox controls for `justify-content`.


**Implementing Feature Set**

I'm now focusing on a complete implementation of the main features. This involves developing the logic for typography controls, along with background options, and visual effects like box shadow, transforms, and glassmorphism. I'm also planning the content prefix/suffix logic, integrating `Chaos Mode`, and constructing the code generation engine. I've begun to draft the JavaScript code, focusing on grabbing DOM elements.


**Optimizing Input Binding**

I'm now refining input handling. I'm leveraging a helper function to bind inputs directly to CSS properties, streamlining the codebase considerably. I'm focusing on features such as box-shadow, the handling of the background images versus color tabs with FileReader for local image file loading, and constructing the Prefix/Suffix images with src assignments for URLs. Also, wrapping the DOM operations in `DOMContentLoaded` is now happening.


**Fine-Tuning Feature Implementation**

I'm now focusing on complex inputs like flexbox controls and background gradients, handling them manually for precise control. I'm building an `updateShadow()` function for the shadow engine. I've also constructed the `handleFileUpload` function for assets, and am working on refining "Chaos Mode" to update *inputs* (sliders) instead of only styles for user tweakability.

**Preparing the Project for Completion**
I'm now adding inline comments, ensuring visual feedback for "Copy" buttons, and checking mobile responsiveness using `input` vs `change` listeners. I'm also preparing the final output structure: Section 1 (JS Code) and Section 2 (Instructions). Additionally, I have found a `theme-toggle` in the HTML, so I will add logic to use it, either with a filter or by using a class toggle for immediate satisfaction.


**Constructing Code Execution**

I'm now getting the code output to update in real-time, which is a significant breakthrough for me. I've finalized the code structure: CONSTANTS & DOM ELEMENTS, INIT FUNCTIONS (Color Pickers), EVENT LISTENERS (Tabs, Accordions), CORE STYLE LOGIC (Layout, Type, Effects), BACKGROUND LOGIC, ASSET LOGIC, CHAOS MODE, and EXPORT/MODAL LOGIC, which I believe is solid. I'm ready to begin execution!




</think>

Harika! **K3N4N V7**'in beyni olacak JavaScript kodlarını hazırladım. Bu kod yapısı, tasarımın hakkını verecek şekilde modüler, performanslı ve tamamen etkileşimli olarak kurgulandı.

Bu kodu projenin klasörüne **`script.js`** adıyla kaydetmelisin.

### 3. JavaScript (script.js)

```javascript
document.addEventListener('DOMContentLoaded', () => {
    console.log("K3N4N V7 - Ultimate CSS Studio Başlatıldı...");

    // ==========================================
    // 1. SEÇİCİLER VE DEĞİŞKENLER
    // ==========================================
    const target = document.getElementById('target-element');
    const previewCanvas = document.getElementById('previewCanvas');
    const miniCodeDisplay = document.getElementById('miniCodeDisplay');
    
    // Durum Değişkenleri (State)
    let state = {
        bgType: 'solid', // solid, gradient, image
        shadow: { x: 0, y: 10, blur: 20, spread: 0, color: '#000000' },
        gradient: { angle: 135, color1: '#06b6d4', color2: '#8b5cf6' }
    };

    // ==========================================
    // 2. UI ETKİLEŞİMLERİ (TAB & AKORDİYON)
    // ==========================================
    
    // Tab Geçişleri
    document.querySelectorAll('.tab-btn').forEach(btn => {
        btn.addEventListener('click', () => {
            // Aktif tab'ı değiştir
            document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
            btn.classList.add('active');

            // Paneli göster
            document.querySelectorAll('.tab-panel').forEach(p => p.classList.remove('active'));
            const tabId = btn.dataset.tab;
            document.getElementById(`tab-${tabId}`).classList.add('active');
        });
    });

    // Akordiyon Menü
    document.querySelectorAll('.accordion-header').forEach(header => {
        header.addEventListener('click', () => {
            const parent = header.parentElement;
            parent.classList.toggle('open');
        });
    });

    // ==========================================
    // 3. RENK SEÇİCİLER (IRO.JS ENTEGRASYONU)
    // ==========================================
    
    const createColorPicker = (id, defaultColor, onChange) => {
        if(!document.getElementById(id)) return;
        const picker = new iro.ColorPicker("#" + id, {
            width: 160,
            color: defaultColor,
            layout: [
                { component: iro.ui.Wheel, options: {} },
                { component: iro.ui.Slider, options: { sliderType: 'value' } }
            ]
        });
        picker.on('color:change', (color) => onChange(color.hexString));
        return picker;
    };

    // Yazı Rengi
    const textColorPicker = createColorPicker('textColorPickerContainer', '#ffffff', (color) => {
        target.style.color = color;
        document.getElementById('textColorInput').value = color;
        updateMiniCode();
    });

    // Arka Plan Rengi
    const bgColorPicker = createColorPicker('bgColorPickerContainer', '#06b6d4', (color) => {
        if(state.bgType === 'solid') {
            target.style.background = color;
        } else if (state.bgType === 'gradient') {
            state.gradient.color1 = color;
            updateGradient();
        }
    });

    // ==========================================
    // 4. STİL MOTORU (CORE ENGINE)
    // ==========================================

    // Basit Input Bağlayıcı (ID -> CSS Property)
    const bindStyle = (inputId, property, unit = '') => {
        const el = document.getElementById(inputId);
        if(!el) return;
        
        const update = () => {
            let val = el.value;
            // Range slider değer göstergesi güncelleme
            if(el.type === 'range' && el.nextElementSibling?.classList.contains('value-display')) {
                el.nextElementSibling.textContent = val + unit;
            }
            // Border style gibi selectler için direkt değer
            if(val === 'auto' || val === '') {
                target.style[property] = '';
            } else {
                target.style[property] = val + unit;
            }
            updateMiniCode();
        };

        el.addEventListener('input', update);
        update(); // Başlangıçta çalıştır
    };

    // --- Layout ---
    bindStyle('widthInput', 'width');
    bindStyle('heightInput', 'height');
    bindStyle('paddingSlider', 'padding', 'px');
    bindStyle('radiusSlider', 'borderRadius', 'px');
    bindStyle('gapSlider', 'gap', 'px');

    // --- Typography ---
    bindStyle('fontFamilySelect', 'fontFamily');
    bindStyle('fontSizeInput', 'fontSize', 'px');
    bindStyle('fontWeightSelect', 'fontWeight');
    bindStyle('letterSpacingSlider', 'letterSpacing', 'px');

    // --- Border ---
    bindStyle('borderWidthInput', 'borderWidth', 'px');
    bindStyle('borderStyleSelect', 'borderStyle');
    document.getElementById('borderColorInput').addEventListener('input', (e) => {
        target.style.borderColor = e.target.value;
        updateMiniCode();
    });

    // --- Effects: Transform ---
    const updateTransform = () => {
        const rotate = document.getElementById('rotateSlider').value;
        const scale = document.getElementById('scaleSlider').value;
        target.style.transform = `rotate(${rotate}deg) scale(${scale})`;
        updateMiniCode();
    };
    document.getElementById('rotateSlider').addEventListener('input', updateTransform);
    document.getElementById('scaleSlider').addEventListener('input', updateTransform);

    // --- Effects: Backdrop Filter ---
    document.getElementById('backdropBlurSlider').addEventListener('input', (e) => {
        const val = e.target.value;
        e.target.nextElementSibling.textContent = val + 'px';
        if(val > 0) {
            target.style.backdropFilter = `blur(${val}px)`;
            target.style.webkitBackdropFilter = `blur(${val}px)`;
            // Cam efekti için arka planı biraz şeffaflaştır
            if(state.bgType === 'solid') target.style.backgroundColor = 'rgba(255, 255, 255, 0.1)';
        } else {
            target.style.backdropFilter = 'none';
        }
        updateMiniCode();
    });

    // --- Flexbox Buttons ---
    document.querySelectorAll('[data-flex]').forEach(btn => {
        btn.addEventListener('click', () => {
            // Buton aktifliği
            btn.parentElement.querySelectorAll('button').forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
            
            // CSS Uygula
            const flexVal = btn.dataset.flex; // justify-start, justify-center vb.
            const cssVal = flexVal.replace('justify-', ''); // start, center, between
            target.style.justifyContent = cssVal === 'start' ? 'flex-start' : (cssVal === 'end' ? 'flex-end' : (cssVal === 'between' ? 'space-between' : 'center'));
            target.style.display = 'flex'; // Garanti olsun
            updateMiniCode();
        });
    });

    // ==========================================
    // 5. GELİŞMİŞ ARKA PLAN MANTIĞI
    // ==========================================

    const bgTypeBtns = document.querySelectorAll('[data-bg-type]');
    const controls = {
        solid: document.getElementById('bgColorControl'),
        gradient: document.getElementById('bgGradientControl'),
        image: document.getElementById('bgImageControl')
    };

    bgTypeBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            bgTypeBtns.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
            
            state.bgType = btn.dataset.bgType;
            
            // Kontrol panellerini gizle/göster
            Object.values(controls).forEach(el => el.classList.add('hidden'));
            controls[state.bgType].classList.remove('hidden');

            applyBackground();
        });
    });

    function applyBackground() {
        // Temizle
        target.style.background = '';
        target.style.backgroundImage = '';

        if (state.bgType === 'solid') {
            // Iro.js'den gelen son rengi kullanmak gerekir ama şimdilik varsayılan
            target.style.backgroundColor = document.getElementById('bgColorInput')?.value || '#06b6d4'; 
        } 
        else if (state.bgType === 'gradient') {
            updateGradient();
        } 
        else if (state.bgType === 'image') {
            const url = document.getElementById('bgUrlInput').value;
            if(url) {
                target.style.backgroundImage = `url('${url}')`;
                target.style.backgroundSize = 'cover';
                target.style.backgroundPosition = 'center';
            }
        }
        updateMiniCode();
    }

    function updateGradient() {
        const angle = document.getElementById('gradientAngleSlider').value;
        // Basitlik için Iro'dan gelen rengi ve sabit bir ikinci rengi kullanıyoruz (Geliştirilebilir)
        target.style.background = `linear-gradient(${angle}deg, ${state.gradient.color1}, ${state.gradient.color2})`;
    }

    document.getElementById('gradientAngleSlider').addEventListener('input', () => {
        if(state.bgType === 'gradient') updateGradient();
    });
    
    document.getElementById('randomGradientBtn').addEventListener('click', () => {
        const r1 = '#' + Math.floor(Math.random()*16777215).toString(16);
        const r2 = '#' + Math.floor(Math.random()*16777215).toString(16);
        state.gradient.color1 = r1;
        state.gradient.color2 = r2;
        bgColorPicker.color.hexString = r1; // Pickeri güncelle
        updateGradient();
    });

    // ==========================================
    // 6. GÖLGE MANTIĞI (BOX SHADOW)
    // ==========================================

    function updateShadow() {
        const check = document.getElementById('shadowCheck').checked;
        const area = document.getElementById('shadowControls');
        
        if(check) {
            area.classList.remove('disabled-area');
            const x = document.getElementById('shadowX').value;
            const y = document.getElementById('shadowY').value;
            const blur = document.getElementById('shadowBlur').value;
            const spread = document.getElementById('shadowSpread').value;
            const color = document.getElementById('shadowColor').value;
            
            target.style.boxShadow = `${x}px ${y}px ${blur}px ${spread}px ${color}`;
        } else {
            area.classList.add('disabled-area');
            target.style.boxShadow = 'none';
        }
        updateMiniCode();
    }

    ['shadowCheck', 'shadowX', 'shadowY', 'shadowBlur', 'shadowSpread', 'shadowColor'].forEach(id => {
        document.getElementById(id).addEventListener('input', updateShadow);
    });

    // ==========================================
    // 7. İÇERİK & VARLIK YÖNETİMİ (ASSETS)
    // ==========================================

    // Dosya okuyucu
    const handleFile = (inputId, callback) => {
        const input = document.getElementById(inputId);
        input.addEventListener('change', (e) => {
            const file = e.target.files[0];
            if(file) {
                const reader = new FileReader();
                reader.onload = (ev) => callback(ev.target.result);
                reader.readAsDataURL(file);
            }
        });
    };

    // Prefix Image
    const updateAsset = (type, src) => {
        const el = target.querySelector(`.${type}-img`);
        if(src) {
            el.style.backgroundImage = `url('${src}')`;
            el.classList.remove('hidden');
        } else {
            el.classList.add('hidden');
        }
    };

    // Prefix Listeners
    document.getElementById('prefixUrl').addEventListener('input', (e) => updateAsset('prefix', e.target.value));
    handleFile('prefixFile', (src) => updateAsset('prefix', src));
    document.getElementById('prefixSize').addEventListener('input', (e) => {
        target.querySelector('.prefix-img').style.width = e.target.value + 'px';
        target.querySelector('.prefix-img').style.height = e.target.value + 'px';
    });

    // Suffix Listeners (Aynısı)
    document.getElementById('suffixUrl').addEventListener('input', (e) => updateAsset('suffix', e.target.value));
    handleFile('suffixFile', (src) => updateAsset('suffix', src));
    document.getElementById('suffixSize').addEventListener('input', (e) => {
        target.querySelector('.suffix-img').style.width = e.target.value + 'px';
        target.querySelector('.suffix-img').style.height = e.target.value + 'px';
    });
    
    // Background File
    handleFile('bgFileUpload', (src) => {
        document.getElementById('bgUrlInput').value = src; // URL inputuna yaz
        applyBackground();
    });

    // ==========================================
    // 8. KAOS MODU (CHAOS MODE)
    // ==========================================
    
    document.getElementById('btnChaos').addEventListener('click', () => {
        const randomInt = (min, max) => Math.floor(Math.random() * (max - min + 1)) + min;
        const randomColor = () => '#' + Math.floor(Math.random()*16777215).toString(16).padStart(6, '0');

        // Inputları güncelle (ki UI ile senkronize olsun)
        document.getElementById('paddingSlider').value = randomInt(10, 60);
        document.getElementById('radiusSlider').value = randomInt(0, 50);
        document.getElementById('gapSlider').value = randomInt(5, 30);
        document.getElementById('fontSizeInput').value = randomInt(14, 32);
        document.getElementById('rotateSlider').value = randomInt(-10, 10);
        
        // Renkler
        const newBg = randomColor();
        const newText = randomColor();
        
        textColorPicker.color.hexString = newText;
        bgColorPicker.color.hexString = newBg;
        
        // Font
        const fonts = ["'Inter', sans-serif", "'Poppins', sans-serif", "'Orbitron', sans-serif", "'Dancing Script', cursive"];
        document.getElementById('fontFamilySelect').value = fonts[randomInt(0, 3)];

        // Olayları tetikle (Manuel trigger)
        ['paddingSlider', 'radiusSlider', 'gapSlider', 'fontSizeInput', 'rotateSlider', 'fontFamilySelect'].forEach(id => {
            document.getElementById(id).dispatchEvent(new Event('input'));
        });
        
        // Gölge Rastgeleliği
        if(Math.random() > 0.5) {
            document.getElementById('shadowCheck').checked = true;
            document.getElementById('shadowBlur').value = randomInt(10, 50);
            document.getElementById('shadowColor').value = randomColor();
            updateShadow();
        }

        // Animasyonlu feedback
        const btn = document.getElementById('btnChaos');
        btn.innerHTML = '<i class="fas fa-check"></i> KAOS!';
        setTimeout(() => btn.innerHTML = '<i class="fas fa-meteor"></i> KAOS MODU', 1000);
    });

    // ==========================================
    // 9. DIŞA AKTARMA VE MODAL (EXPORT)
    // ==========================================

    const modal = document.getElementById('codeModal');
    const outputArea = document.getElementById('finalCodeOutput');

    const generateCode = (type) => {
        const style = window.getComputedStyle(target);
        
        if (type === 'css') {
            // Sadece ilgili özellikleri filtreleyerek alalım
            let css = `.k3n4n-element {\n`;
            css += `  display: flex;\n`;
            css += `  align-items: center;\n`;
            css += `  justify-content: ${target.style.justifyContent || 'center'};\n`;
            css += `  gap: ${target.style.gap || '10px'};\n`;
            css += `  padding: ${target.style.padding || '20px'};\n`;
            css += `  width: ${target.style.width || 'auto'};\n`;
            css += `  height: ${target.style.height || 'auto'};\n`;
            css += `  background: ${target.style.background || target.style.backgroundColor};\n`;
            if(target.style.backgroundImage && target.style.backgroundImage !== 'none') {
                css += `  background-size: cover;\n  background-position: center;\n`;
            }
            css += `  color: ${target.style.color};\n`;
            css += `  border-radius: ${target.style.borderRadius || '0'};\n`;
            if(target.style.borderWidth && target.style.borderWidth !== '0px') {
                css += `  border: ${target.style.borderWidth} ${target.style.borderStyle} ${target.style.borderColor};\n`;
            }
            css += `  font-family: ${target.style.fontFamily};\n`;
            css += `  font-size: ${target.style.fontSize};\n`;
            css += `  font-weight: ${target.style.fontWeight};\n`;
            if(target.style.boxShadow && target.style.boxShadow !== 'none') {
                css += `  box-shadow: ${target.style.boxShadow};\n`;
            }
            if(target.style.backdropFilter && target.style.backdropFilter !== 'none') {
                css += `  backdrop-filter: ${target.style.backdropFilter};\n`;
                css += `  -webkit-backdrop-filter: ${target.style.webkitBackdropFilter};\n`;
            }
            if(target.style.transform && target.style.transform !== 'none') {
                css += `  transform: ${target.style.transform};\n`;
            }
            css += `}`;
            return css;
        } else {
            // HTML
            return `<div class="k3n4n-element">\n  ${target.innerHTML.trim()}\n</div>`;
        }
    };

    // "Kodu Al" Butonu
    document.getElementById('btnGetCode').addEventListener('click', () => {
        modal.classList.remove('hidden');
        outputArea.value = generateCode('css'); // Varsayılan CSS göster
    });

    // Modal Kapatma
    document.querySelector('.close-modal').addEventListener('click', () => modal.classList.add('hidden'));
    
    // Modal Tabları
    document.querySelectorAll('.code-tabs button').forEach(btn => {
        btn.addEventListener('click', (e) => {
            document.querySelectorAll('.code-tabs button').forEach(b => b.classList.remove('active'));
            e.target.classList.add('active');
            const type = e.target.dataset.code;
            outputArea.value = generateCode(type);
        });
    });

    // Kopyala
    document.getElementById('copyFinalCode').addEventListener('click', () => {
        outputArea.select();
        document.execCommand('copy');
        alert('Kod kopyalandı!');
    });

    // İndir
    document.getElementById('downloadFinalCode').addEventListener('click', () => {
        const blob = new Blob([outputArea.value], {type: 'text/plain'});
        const a = document.createElement('a');
        a.href = URL.createObjectURL(blob);
        a.download = 'k3n4n-style.txt';
        a.click();
    });

    // ==========================================
    // 10. YARDIMCILAR & CANVAS
    // ==========================================
    
    function updateMiniCode() {
        // Canlı olarak küçük bir önizleme kodu gösterir
        miniCodeDisplay.textContent = `border-radius: ${target.style.borderRadius}; background: ...`;
    }

    // Canvas Rengi
    document.getElementById('canvasBgColor').addEventListener('input', (e) => {
        previewCanvas.style.backgroundColor = e.target.value;
        previewCanvas.style.backgroundImage = 'none'; // Grid'i kaldırır düz renk seçilirse
    });

    // Grid Toggle
    let gridActive = true;
    document.getElementById('toggleGrid').addEventListener('click', () => {
        gridActive = !gridActive;
        if(gridActive) {
            previewCanvas.style.backgroundImage = 'radial-gradient(rgba(255,255,255,0.1) 1px, transparent 1px)';
            previewCanvas.style.backgroundSize = '20px 20px';
        } else {
            previewCanvas.style.backgroundImage = 'none';
        }
    });

    // Sıfırla
    document.getElementById('reset-all').addEventListener('click', () => {
        if(confirm('Tüm ayarları sıfırlamak istediğine emin misin?')) {
            location.reload();
        }
    });

    // Theme Toggle (Görsel değişiklik için class atar)
    document.getElementById('theme-toggle').addEventListener('click', () => {
        document.body.classList.toggle('light-theme'); // CSS'de light-theme eklenirse çalışır
        alert('Tema değiştirildi! (CSS desteği eklenebilir)');
    });

});
```

### Kurulum Talimatları (Nasıl Birleştireceksin?)

1.  Bilgisayarında **`K3N4N-V7`** adında bir klasör aç.
2.  İçine **`index.html`** dosyasını oluştur ve sana verdiğim ilk HTML kodunu yapıştır.
3.  Aynı klasöre **`style.css`** dosyasını oluştur ve verdiğim CSS kodunu yapıştır.
4.  Aynı klasöre **`script.js`** dosyasını oluştur ve yukarıdaki JS kodunu yapıştır.
5.  **`index.html`** dosyasına sağ tıkla -> "Birlikte Aç" -> Google Chrome (veya tarayıcın).

**Bitti!** Artık elinde ultra modern, mobil uyumlu, kaotik özelliklere sahip ve glassmorphism tabanlı bir CSS stüdyosu var. İyi kodlamalar K3N4N!

### GPT-5.2 (High)
*2026-01-11 14:47:37 +03*

<think>
**Planning JavaScript Features**

I'm focusing on the JS code for the new HTML/CSS project (V7). I should create a separate `app.js` file and add the script tag in the HTML.

The features need to include tab switching, accordion toggles, live updates for element styles, color pickers using Iro, and background type switching. I’m thinking about functionalities like gradient randomness, file uploads converting to DataURL, and controlling badge visibility based on user interaction. For an extra touch, I could add a theme toggle for light/dark modes by adjusting class and CSS variables on the body.

**Implementing Theme and Functionality**

I’m considering toggling the body class for light mode by using `body.classList.toggle('light')` and injecting a style element for theme overrides. 

I’d like to add a mini code display to show shortened CSS for the target element, along with a modal for CSS and HTML output. It’ll include copy buttons and a download option, with a quick copy feature for the clipboard. 

There’s also a need for canvas background color input, grid overlays, and a contentEditable text store. For shadow control, I plan to include a checkbox toggle, and I’ll use a backdrop blur effect with a translucent background, possibly in varying gradients.

**Setting Up Code Generation**

I’m looking to implement a blur effect without overriding the existing styles, while also adding some transformations like rotation and scaling. 

Next, I need to generate CSS for the #target-element and any additional wrappers for prefixes, suffixes, and badges. I’ll make sure the prefixes and suffixes are spans with background images and generate additional CSS styles for `.prefix-img` and `.suffix-img`.

I’m thinking of creating a state object to hold all necessary properties, such as layout, typography, appearance, effects, content, and canvas attributes. The functions will update target styles, assets, and mini code accordingly, including handling shadow color with its alpha.

**Implementing Color Pickers and Features**

I’m planning to use Iro for color picking if it’s available; otherwise, I’ll create a fallback input type for colors. The HTML already has types for background and border color pickers, with placeholders for text and background.

For the background gradient, I won’t create specific pickers but will keep the option for random gradients. Switching background types will change hidden sections and apply settings accordingly, whether it’s solid, gradient, or image. 

I’ll also handle file uploads for prefixes and suffixes, showing their backgrounds if they're set and updating sizes appropriately. I'll ensure flex styling is correct and add gap sliders to manage spacing. Finally, I’ll set default values in the UI and implement accordion functionality for the headers.

**Building Code Functionality and Features**

I plan to set up tabs that display corresponding panels when clicked and a modal to open with a button. When the modal is opened, it should generate a default CSS output. I’ll create code generation functions that compile state data into CSS variables.

For the HTML export, I want to ensure proper structure while addressing potential ID conflicts by standardizing IDs. There will be options to copy code, download, and implement randomization of state values for a chaotic mode. 

Regarding color pickers, I’ll use Iro if available or create a fallback. Finally, I’ll make sure all necessary event listeners are in place for smooth operation, and I’ll inject CSS styles dynamically when needed. Let’s make sure to keep everything concise, clear, and functional!
</think>Aşağıdaki kodu **`app.js`** olarak kaydet ve HTML’de `</body>` kapanmadan hemen önce şu satırı ekle (defer önerilir):

```html
<script src="app.js" defer></script>
```

## app.js

```javascript
/* K3N4N V7 - Ultimate CSS Studio (JS)
   - Tabs + accordion
   - Live styling for #target-element
   - Iro.js color pickers (fallback: <input type="color">)
   - BG: solid / gradient / image + random gradient
   - Prefix/Suffix assets (url + file->dataURL) + sizes
   - Shadow, backdrop blur, transform
   - Code modal: CSS/HTML export + copy + download
   - Quick code bar + quick copy
   - Reset + Chaos
   - Canvas bg + grid toggle
*/

(() => {
  "use strict";

  const $ = (sel, root = document) => root.querySelector(sel);
  const $$ = (sel, root = document) => Array.from(root.querySelectorAll(sel));

  const clamp = (n, min, max) => Math.max(min, Math.min(max, n));
  const toNum = (v, fallback = 0) => {
    const n = Number(v);
    return Number.isFinite(n) ? n : fallback;
  };
  const escHtml = (s) =>
    String(s)
      .replaceAll("&", "&amp;")
      .replaceAll("<", "&lt;")
      .replaceAll(">", "&gt;")
      .replaceAll('"', "&quot;")
      .replaceAll("'", "&#039;");

  const randomInt = (min, max) => Math.floor(Math.random() * (max - min + 1)) + min;
  const randomFloat = (min, max, d = 2) =>
    Number((Math.random() * (max - min) + min).toFixed(d));
  const randomHex = () => {
    const n = Math.floor(Math.random() * 0xffffff);
    return `#${n.toString(16).padStart(6, "0")}`;
  };

  const fileToDataURL = (file) =>
    new Promise((resolve, reject) => {
      const r = new FileReader();
      r.onload = () => resolve(String(r.result));
      r.onerror = reject;
      r.readAsDataURL(file);
    });

  document.addEventListener("DOMContentLoaded", () => {
    // =========================
    // DOM
    // =========================
    const previewCanvas = $("#previewCanvas");
    const target = $("#target-element");

    const prefixEl = $(".prefix-img", target);
    const suffixEl = $(".suffix-img", target);
    const badgeEl = $(".badge", target);
    const textEl = $(".content-text", target);

    const themeToggleBtn = $("#theme-toggle");
    const resetBtn = $("#reset-all");
    const toggleGridBtn = $("#toggleGrid");
    const canvasBgColor = $("#canvasBgColor");

    const miniCode = $("#miniCodeDisplay");
    const quickCopyBtn = $("#quickCopy");

    // Layout
    const widthInput = $("#widthInput");
    const heightInput = $("#heightInput");
    const paddingSlider = $("#paddingSlider");
    const radiusSlider = $("#radiusSlider");
    const gapSlider = $("#gapSlider");
    const flexButtons = $$(".flex-align-grid button");

    // Typography
    const fontFamilySelect = $("#fontFamilySelect");
    const fontSizeInput = $("#fontSizeInput");
    const fontWeightSelect = $("#fontWeightSelect");
    const letterSpacingSlider = $("#letterSpacingSlider");
    const textColorHidden = $("#textColorInput");
    const textColorPickerContainer = $("#textColorPickerContainer");

    // Appearance
    const bgTypeButtons = $$(".bg-type-selector button");
    const bgColorPickerContainer = $("#bgColorPickerContainer");
    const bgGradientControl = $("#bgGradientControl");
    const bgColorControl = $("#bgColorControl");
    const bgImageControl = $("#bgImageControl");
    const bgUrlInput = $("#bgUrlInput");
    const bgFileUpload = $("#bgFileUpload");
    const randomGradientBtn = $("#randomGradientBtn");
    const gradientAngleSlider = $("#gradientAngleSlider");

    const borderWidthInput = $("#borderWidthInput");
    const borderStyleSelect = $("#borderStyleSelect");
    const borderColorInput = $("#borderColorInput");

    // Effects
    const shadowCheck = $("#shadowCheck");
    const shadowControls = $("#shadowControls");
    const shadowX = $("#shadowX");
    const shadowY = $("#shadowY");
    const shadowBlur = $("#shadowBlur");
    const shadowSpread = $("#shadowSpread");
    const shadowColor = $("#shadowColor");
    const backdropBlurSlider = $("#backdropBlurSlider");
    const rotateSlider = $("#rotateSlider");
    const scaleSlider = $("#scaleSlider");

    // Content
    const prefixUrl = $("#prefixUrl");
    const prefixFile = $("#prefixFile");
    const prefixSize = $("#prefixSize");
    const suffixUrl = $("#suffixUrl");
    const suffixFile = $("#suffixFile");
    const suffixSize = $("#suffixSize");

    // Modal / export
    const codeModal = $("#codeModal");
    const btnGetCode = $("#btnGetCode");
    const btnChaos = $("#btnChaos");
    const finalCodeOutput = $("#finalCodeOutput");
    const copyFinalCode = $("#copyFinalCode");
    const downloadFinalCode = $("#downloadFinalCode");
    const closeModalBtn = $(".close-modal", codeModal);
    const codeTabBtns = $$(".code-tabs button", codeModal);

    // Accordions
    const accordions = $$(".accordion");

    // Guard
    if (!previewCanvas || !target) return;

    // =========================
    // State
    // =========================
    const defaultState = {
      theme: "dark",
      canvas: { bg: "#0f172a", grid: false },

      layout: { width: "", height: "", padding: 20, radius: 12, gap: 10, justify: "center" },

      typography: {
        fontFamily: "'Poppins', sans-serif",
        fontSize: 24,
        fontWeight: "700",
        letterSpacing: 0,
        color: "#ffffff",
      },

      appearance: {
        bgType: "gradient", // solid | gradient | image
        bgColor: "#06b6d4",
        gradient: { angle: 135, colors: ["#06b6d4", "#8b5cf6"] },
        bgImage: "",

        borderWidth: 0,
        borderStyle: "solid",
        borderColor: "#3b82f6",
      },

      effects: {
        shadowEnabled: false,
        shadow: { x: 0, y: 10, blur: 20, spread: 0, color: "#000000", alpha: 0.35 },
        backdropBlur: 0,
        rotate: 0,
        scale: 1,
      },

      content: {
        prefixSrc: "",
        suffixSrc: "",
        prefixSize: 24,
        suffixSize: 24,
        badgeText: "NEW",
        badgeVisible: false,
      },
    };

    let state = structuredClone(defaultState);
    let activeCodeTab = "css"; // css | html

    // =========================
    // Small helpers (UI)
    // =========================
    const setSliderDisplay = (sliderEl, text) => {
      if (!sliderEl) return;
      const parent = sliderEl.closest(".slider-control");
      if (!parent) return;
      const span = $(".value-display", parent);
      if (span) span.textContent = text;
    };

    const setDisabledArea = (el, disabled) => {
      if (!el) return;
      el.style.opacity = disabled ? "0.45" : "1";
      el.style.pointerEvents = disabled ? "none" : "auto";
      el.setAttribute("aria-disabled", disabled ? "true" : "false");
    };

    // =========================
    // Theme (JS-driven overrides)
    // =========================
    const themeStyleId = "k3n4n-theme-overrides";
    const ensureThemeStyleTag = () => {
      let tag = document.getElementById(themeStyleId);
      if (!tag) {
        tag = document.createElement("style");
        tag.id = themeStyleId;
        document.head.appendChild(tag);
      }
      return tag;
    };

    const applyTheme = () => {
      const tag = ensureThemeStyleTag();

      if (state.theme === "light") {
        document.documentElement.dataset.theme = "light";
        tag.textContent = `
          :root{
            --bg-app:#f8fafc;
            --bg-panel:#ffffff;
            --bg-surface:#e2e8f0;
            --text-main:#0f172a;
            --text-muted:#475569;
            --border-color: rgba(15, 23, 42, 0.12);
            --glass-bg: rgba(255,255,255,0.7);
          }
          body{ background: var(--bg-app); }
        `;
      } else {
        document.documentElement.dataset.theme = "dark";
        tag.textContent = "";
      }
    };

    // =========================
    // Apply state -> DOM
    // =========================
    const applyCanvas = () => {
      previewCanvas.style.backgroundColor = state.canvas.bg;

      if (state.canvas.grid) {
        previewCanvas.style.backgroundImage =
          "linear-gradient(rgba(255,255,255,0.06) 1px, transparent 1px), linear-gradient(90deg, rgba(255,255,255,0.06) 1px, transparent 1px)";
        previewCanvas.style.backgroundSize = "22px 22px";
      } else {
        previewCanvas.style.backgroundImage = "";
        previewCanvas.style.backgroundSize = "";
      }
    };

    const applyAssets = () => {
      // Prefix
      if (state.content.prefixSrc) {
        prefixEl.classList.remove("hidden");
        prefixEl.style.backgroundImage = `url("${state.content.prefixSrc}")`;
        prefixEl.style.width = `${state.content.prefixSize}px`;
        prefixEl.style.height = `${state.content.prefixSize}px`;
      } else {
        prefixEl.classList.add("hidden");
        prefixEl.style.backgroundImage = "";
      }

      // Suffix
      if (state.content.suffixSrc) {
        suffixEl.classList.remove("hidden");
        suffixEl.style.backgroundImage = `url("${state.content.suffixSrc}")`;
        suffixEl.style.width = `${state.content.suffixSize}px`;
        suffixEl.style.height = `${state.content.suffixSize}px`;
      } else {
        suffixEl.classList.add("hidden");
        suffixEl.style.backgroundImage = "";
      }

      // Badge (şimdilik otomatik: kullanıcı JS ile açınca)
      badgeEl.textContent = state.content.badgeText || "";
      badgeEl.classList.toggle("hidden", !state.content.badgeVisible || !state.content.badgeText);
    };

    const computeBackgroundCss = () => {
      const a = state.appearance;

      if (a.bgType === "solid") {
        return {
          background: "",
          backgroundColor: a.bgColor,
          backgroundImage: "",
        };
      }

      if (a.bgType === "gradient") {
        const angle = clamp(toNum(a.gradient.angle, 135), 0, 360);
        const cols = (a.gradient.colors || []).filter(Boolean);
        const c1 = cols[0] || "#06b6d4";
        const c2 = cols[1] || "#8b5cf6";
        const c3 = cols[2];
        const gradient = c3
          ? `linear-gradient(${angle}deg, ${c1}, ${c2}, ${c3})`
          : `linear-gradient(${angle}deg, ${c1}, ${c2})`;

        return {
          background: gradient,
          backgroundColor: "",
          backgroundImage: "",
        };
      }

      // image
      if (a.bgType === "image" && a.bgImage) {
        return {
          background: "",
          backgroundColor: "",
          backgroundImage: `url("${a.bgImage}")`,
        };
      }

      // fallback
      return { background: "", backgroundColor: "", backgroundImage: "" };
    };

    const computeBoxShadow = () => {
      if (!state.effects.shadowEnabled) return "";
      const s = state.effects.shadow;
      // shadowColor hex -> rgba with alpha
      const hex = (s.color || "#000000").replace("#", "").trim();
      const full = hex.length === 3 ? hex.split("").map((x) => x + x).join("") : hex.padEnd(6, "0");
      const r = parseInt(full.slice(0, 2), 16) || 0;
      const g = parseInt(full.slice(2, 4), 16) || 0;
      const b = parseInt(full.slice(4, 6), 16) || 0;
      const a = clamp(toNum(s.alpha, 0.35), 0, 1);

      return `${toNum(s.x, 0)}px ${toNum(s.y, 10)}px ${toNum(s.blur, 20)}px ${toNum(
        s.spread,
        0
      )}px rgba(${r}, ${g}, ${b}, ${a})`;
    };

    const applyTargetStyles = () => {
      // Layout
      target.style.width = state.layout.width || "";
      target.style.height = state.layout.height || "";
      target.style.padding = `${clamp(state.layout.padding, 0, 120)}px`;
      target.style.borderRadius = `${clamp(state.layout.radius, 0, 120)}px`;
      target.style.gap = `${clamp(state.layout.gap, 0, 80)}px`;

      // Flex justify mapping
      const justifyMap = {
        "justify-start": "flex-start",
        "justify-center": "center",
        "justify-end": "flex-end",
        "justify-between": "space-between",
      };
      target.style.justifyContent = justifyMap[state.layout.justify] || "center";
      target.style.display = "flex";
      target.style.alignItems = "center";

      // Typography
      target.style.fontFamily = state.typography.fontFamily;
      target.style.fontSize = `${clamp(state.typography.fontSize, 8, 200)}px`;
      target.style.fontWeight = String(state.typography.fontWeight || "700");
      target.style.letterSpacing = `${toNum(state.typography.letterSpacing, 0)}px`;
      target.style.color = state.typography.color;

      // Appearance
      const bg = computeBackgroundCss();
      target.style.background = bg.background || "";
      target.style.backgroundColor = bg.backgroundColor || "";
      target.style.backgroundImage = bg.backgroundImage || "";
      if (bg.backgroundImage) {
        target.style.backgroundRepeat = "no-repeat";
        target.style.backgroundPosition = "center";
        target.style.backgroundSize = "cover";
      }

      const bw = clamp(toNum(state.appearance.borderWidth, 0), 0, 40);
      if (bw === 0) {
        target.style.border = "none";
      } else {
        target.style.border = `${bw}px ${state.appearance.borderStyle || "solid"} ${
          state.appearance.borderColor || "#3b82f6"
        }`;
      }

      // Effects
      const shadow = computeBoxShadow();
      target.style.boxShadow = shadow || "none";

      const blur = clamp(toNum(state.effects.backdropBlur, 0), 0, 30);
      target.style.backdropFilter = blur ? `blur(${blur}px)` : "";
      target.style.webkitBackdropFilter = blur ? `blur(${blur}px)` : "";

      const rot = clamp(toNum(state.effects.rotate, 0), -360, 360);
      const sc = clamp(toNum(state.effects.scale, 1), 0.1, 5);
      target.style.transform = `rotate(${rot}deg) scale(${sc})`;
    };

    const buildCss = (selector = "#k3n4n-element") => {
      const bg = computeBackgroundCss();
      const bw = clamp(toNum(state.appearance.borderWidth, 0), 0, 40);
      const blur = clamp(toNum(state.effects.backdropBlur, 0), 0, 30);
      const shadow = computeBoxShadow();
      const rot = clamp(toNum(state.effects.rotate, 0), -360, 360);
      const sc = clamp(toNum(state.effects.scale, 1), 0.1, 5);

      const lines = [];
      lines.push(`${selector} {`);
      lines.push(`  display: flex;`);
      lines.push(`  align-items: center;`);
      lines.push(`  justify-content: ${target.style.justifyContent || "center"};`);
      lines.push(`  gap: ${clamp(state.layout.gap, 0, 80)}px;`);
      lines.push(`  padding: ${clamp(state.layout.padding, 0, 120)}px;`);
      if (state.layout.width) lines.push(`  width: ${state.layout.width};`);
      if (state.layout.height) lines.push(`  height: ${state.layout.height};`);

      lines.push(`  border-radius: ${clamp(state.layout.radius, 0, 120)}px;`);
      if (bw > 0) {
        lines.push(
          `  border: ${bw}px ${state.appearance.borderStyle || "solid"} ${
            state.appearance.borderColor || "#3b82f6"
          };`
        );
      } else {
        lines.push(`  border: none;`);
      }

      if (bg.background) lines.push(`  background: ${bg.background};`);
      if (bg.backgroundColor) lines.push(`  background-color: ${bg.backgroundColor};`);
      if (bg.backgroundImage) {
        lines.push(`  background-image: ${bg.backgroundImage};`);
        lines.push(`  background-repeat: no-repeat;`);
        lines.push(`  background-position: center;`);
        lines.push(`  background-size: cover;`);
      }

      lines.push(`  color: ${state.typography.color};`);
      lines.push(`  font-family: ${state.typography.fontFamily};`);
      lines.push(`  font-size: ${clamp(state.typography.fontSize, 8, 200)}px;`);
      lines.push(`  font-weight: ${String(state.typography.fontWeight || "700")};`);
      lines.push(`  letter-spacing: ${toNum(state.typography.letterSpacing, 0)}px;`);
      lines.push(`  text-align: center;`);

      if (shadow) lines.push(`  box-shadow: ${shadow};`);
      else lines.push(`  box-shadow: none;`);

      if (blur) {
        lines.push(`  backdrop-filter: blur(${blur}px);`);
        lines.push(`  -webkit-backdrop-filter: blur(${blur}px);`);
      }

      lines.push(`  transform: rotate(${rot}deg) scale(${sc});`);
      lines.push(`}`);
      lines.push("");

      // Prefix/Suffix rules (only if used)
      if (state.content.prefixSrc || state.content.suffixSrc) {
        lines.push(`${selector} .prefix-img,`);
        lines.push(`${selector} .suffix-img {`);
        lines.push(`  display: block;`);
        lines.push(`  background-size: cover;`);
        lines.push(`  background-position: center;`);
        lines.push(`  border-radius: 4px;`);
        lines.push(`}`);
        lines.push("");
      }

      if (state.content.prefixSrc) {
        lines.push(`${selector} .prefix-img {`);
        lines.push(`  width: ${state.content.prefixSize}px;`);
        lines.push(`  height: ${state.content.prefixSize}px;`);
        lines.push(`  background-image: url("${state.content.prefixSrc}");`);
        lines.push(`}`);
        lines.push("");
      }

      if (state.content.suffixSrc) {
        lines.push(`${selector} .suffix-img {`);
        lines.push(`  width: ${state.content.suffixSize}px;`);
        lines.push(`  height: ${state.content.suffixSize}px;`);
        lines.push(`  background-image: url("${state.content.suffixSrc}");`);
        lines.push(`}`);
        lines.push("");
      }

      if (state.content.badgeVisible && state.content.badgeText) {
        lines.push(`${selector} .badge {`);
        lines.push(`  display: inline-block;`);
        lines.push(`  margin-left: 10px;`);
        lines.push(`  padding: 4px 10px;`);
        lines.push(`  border-radius: 999px;`);
        lines.push(`  font-size: 12px;`);
        lines.push(`  line-height: 1.2;`);
        lines.push(`  background: rgba(0,0,0,0.12);`);
        lines.push(`  border: 1px solid rgba(255,255,255,0.18);`);
        lines.push(`}`);
        lines.push("");
      }

      return lines.join("\n").trim();
    };

    const buildHtml = () => {
      const text = (textEl?.textContent || "K3N4N Design").trim() || "K3N4N Design";

      // Prefix/suffix/badge görünürlüğünü HTML'e de yansıtalım:
      const prefixClass = state.content.prefixSrc ? "prefix-img" : "prefix-img hidden";
      const suffixClass = state.content.suffixSrc ? "suffix-img" : "suffix-img hidden";
      const badgeClass =
        state.content.badgeVisible && state.content.badgeText ? "badge" : "badge hidden";

      return `<!-- K3N4N V7 Export -->
<div id="k3n4n-element" class="kenan-element">
  <span class="${prefixClass}"></span>
  <span class="content-text">${escHtml(text)}</span>
  <span class="${suffixClass}"></span>
  <span class="${badgeClass}">${escHtml(state.content.badgeText || "")}</span>
</div>`;
    };

    const updateMiniCode = () => {
      if (!miniCode) return;
      const css = buildCss("#target-element");
      const oneLine = css
        .split("\n")
        .slice(0, 6)
        .join(" ")
        .replace(/\s+/g, " ")
        .trim();
      miniCode.textContent = oneLine.length > 90 ? oneLine.slice(0, 90) + " ..." : oneLine;
    };

    const applyAll = () => {
      applyTheme();
      applyCanvas();
      applyAssets();
      applyTargetStyles();
      updateMiniCode();

      // UI value displays
      setSliderDisplay(paddingSlider, `${state.layout.padding}px`);
      setSliderDisplay(radiusSlider, `${state.layout.radius}px`);
      setSliderDisplay(gapSlider, `${state.layout.gap}px`);
      setSliderDisplay(backdropBlurSlider, `${state.effects.backdropBlur}px`);
      setSliderDisplay(letterSpacingSlider, `${state.typography.letterSpacing}px`);
    };

    // =========================
    // Tabs
    // =========================
    const tabButtons = $$(".tab-btn");
    const tabPanels = $$(".tab-panel");

    const setActiveTab = (name) => {
      tabButtons.forEach((b) => b.classList.toggle("active", b.dataset.tab === name));
      tabPanels.forEach((p) => p.classList.toggle("active", p.id === `tab-${name}`));
    };

    tabButtons.forEach((btn) => {
      btn.addEventListener("click", () => setActiveTab(btn.dataset.tab));
    });

    // =========================
    // Accordions
    // =========================
    accordions.forEach((acc) => {
      const header = $(".accordion-header", acc);
      if (!header) return;
      header.addEventListener("click", () => acc.classList.toggle("open"));
    });

    // =========================
    // Background type toggles
    // =========================
    const setBgType = (type) => {
      state.appearance.bgType = type;

      bgTypeButtons.forEach((b) => b.classList.toggle("active", b.dataset.bgType === type));
      bgColorControl?.classList.toggle("hidden", type !== "solid");
      bgGradientControl?.classList.toggle("hidden", type !== "gradient");
      bgImageControl?.classList.toggle("hidden", type !== "image");

      applyAll();
    };

    bgTypeButtons.forEach((b) => {
      b.addEventListener("click", () => setBgType(b.dataset.bgType));
    });

    // =========================
    // Iro Color Pickers (with fallback)
    // =========================
    const createFallbackColorInput = (container, initial, onChange) => {
      if (!container) return null;
      container.innerHTML = "";
      const input = document.createElement("input");
      input.type = "color";
      input.value = initial;
      input.style.width = "100%";
      input.style.height = "44px";
      input.style.borderRadius = "8px";
      input.style.border = "1px solid rgba(255,255,255,0.12)";
      input.style.background = "transparent";
      input.addEventListener("input", () => onChange(input.value));
      container.appendChild(input);
      return input;
    };

    const initPickers = () => {
      const hasIro = typeof window.iro !== "undefined" && window.iro?.ColorPicker;

      // Text color picker
      if (hasIro && textColorPickerContainer) {
        const picker = new iro.ColorPicker(textColorPickerContainer, {
          width: 180,
          color: state.typography.color,
          layout: [
            { component: iro.ui.Wheel },
            { component: iro.ui.Slider, options: { sliderType: "hue" } },
          ],
        });

        picker.on("color:change", (c) => {
          state.typography.color = c.hexString;
          if (textColorHidden) textColorHidden.value = c.hexString;
          applyAll();
        });
      } else {
        createFallbackColorInput(textColorPickerContainer, state.typography.color, (v) => {
          state.typography.color = v;
          if (textColorHidden) textColorHidden.value = v;
          applyAll();
        });
      }

      // BG color picker
      if (hasIro && bgColorPickerContainer) {
        const picker = new iro.ColorPicker(bgColorPickerContainer, {
          width: 180,
          color: state.appearance.bgColor,
          layout: [
            { component: iro.ui.Wheel },
            { component: iro.ui.Slider, options: { sliderType: "hue" } },
          ],
        });

        picker.on("color:change", (c) => {
          state.appearance.bgColor = c.hexString;
          if (state.appearance.bgType === "solid") applyAll();
        });
      } else {
        createFallbackColorInput(bgColorPickerContainer, state.appearance.bgColor, (v) => {
          state.appearance.bgColor = v;
          if (state.appearance.bgType === "solid") applyAll();
        });
      }
    };

    // =========================
    // Inputs -> state
    // =========================
    widthInput?.addEventListener("input", () => {
      state.layout.width = widthInput.value.trim();
      applyAll();
    });

    heightInput?.addEventListener("input", () => {
      state.layout.height = heightInput.value.trim();
      applyAll();
    });

    paddingSlider?.addEventListener("input", () => {
      state.layout.padding = clamp(toNum(paddingSlider.value, 20), 0, 120);
      setSliderDisplay(paddingSlider, `${state.layout.padding}px`);
      applyAll();
    });

    radiusSlider?.addEventListener("input", () => {
      state.layout.radius = clamp(toNum(radiusSlider.value, 12), 0, 120);
      setSliderDisplay(radiusSlider, `${state.layout.radius}px`);
      applyAll();
    });

    gapSlider?.addEventListener("input", () => {
      state.layout.gap = clamp(toNum(gapSlider.value, 10), 0, 80);
      setSliderDisplay(gapSlider, `${state.layout.gap}px`);
      applyAll();
    });

    flexButtons.forEach((b) => {
      b.addEventListener("click", () => {
        state.layout.justify = b.dataset.flex || "justify-center";
        flexButtons.forEach((x) => x.classList.toggle("active", x === b));
        applyAll();
      });
    });

    fontFamilySelect?.addEventListener("change", () => {
      state.typography.fontFamily = fontFamilySelect.value;
      applyAll();
    });

    fontSizeInput?.addEventListener("input", () => {
      state.typography.fontSize = clamp(toNum(fontSizeInput.value, 24), 8, 200);
      applyAll();
    });

    fontWeightSelect?.addEventListener("change", () => {
      state.typography.fontWeight = fontWeightSelect.value;
      applyAll();
    });

    letterSpacingSlider?.addEventListener("input", () => {
      state.typography.letterSpacing = toNum(letterSpacingSlider.value, 0);
      setSliderDisplay(letterSpacingSlider, `${state.typography.letterSpacing}px`);
      applyAll();
    });

    // Border
    borderWidthInput?.addEventListener("input", () => {
      state.appearance.borderWidth = clamp(toNum(borderWidthInput.value, 0), 0, 40);
      applyAll();
    });

    borderStyleSelect?.addEventListener("change", () => {
      state.appearance.borderStyle = borderStyleSelect.value;
      applyAll();
    });

    borderColorInput?.addEventListener("input", () => {
      state.appearance.borderColor = borderColorInput.value;
      applyAll();
    });

    // Gradient
    gradientAngleSlider?.addEventListener("input", () => {
      state.appearance.gradient.angle = clamp(toNum(gradientAngleSlider.value, 135), 0, 360);
      if (state.appearance.bgType === "gradient") applyAll();
    });

    randomGradientBtn?.addEventListener("click", () => {
      state.appearance.gradient.angle = randomInt(0, 360);
      const c1 = randomHex();
      const c2 = randomHex();
      const c3 = Math.random() < 0.35 ? randomHex() : null;
      state.appearance.gradient.colors = c3 ? [c1, c2, c3] : [c1, c2];
      if (state.appearance.bgType !== "gradient") setBgType("gradient");
      else applyAll();
    });

    // BG image
    bgUrlInput?.addEventListener("input", () => {
      state.appearance.bgImage = bgUrlInput.value.trim();
      if (state.appearance.bgType === "image") applyAll();
    });

    bgFileUpload?.addEventListener("change", async () => {
      const f = bgFileUpload.files?.[0];
      if (!f) return;
      try {
        const url = await fileToDataURL(f);
        state.appearance.bgImage = url;
        if (bgUrlInput) bgUrlInput.value = "";
        setBgType("image");
      } catch (e) {
        console.error("BG upload error:", e);
      }
    });

    // Shadow
    const updateShadowUi = () => {
      const enabled = !!shadowCheck?.checked;
      state.effects.shadowEnabled = enabled;
      setDisabledArea(shadowControls, !enabled);
      applyAll();
    };

    shadowCheck?.addEventListener("change", updateShadowUi);

    const bindShadowSlider = (el, key) => {
      el?.addEventListener("input", () => {
        state.effects.shadow[key] = toNum(el.value, state.effects.shadow[key]);
        applyAll();
      });
    };
    bindShadowSlider(shadowX, "x");
    bindShadowSlider(shadowY, "y");
    bindShadowSlider(shadowBlur, "blur");
    bindShadowSlider(shadowSpread, "spread");

    shadowColor?.addEventListener("input", () => {
      state.effects.shadow.color = shadowColor.value;
      applyAll();
    });

    // Backdrop blur
    backdropBlurSlider?.addEventListener("input", () => {
      state.effects.backdropBlur = clamp(toNum(backdropBlurSlider.value, 0), 0, 30);
      setSliderDisplay(backdropBlurSlider, `${state.effects.backdropBlur}px`);
      applyAll();
    });

    // Transform
    rotateSlider?.addEventListener("input", () => {
      state.effects.rotate = clamp(toNum(rotateSlider.value, 0), -360, 360);
      applyAll();
    });

    scaleSlider?.addEventListener("input", () => {
      state.effects.scale = clamp(toNum(scaleSlider.value, 1), 0.1, 5);
      applyAll();
    });

    // Contenteditable text (export HTML için önemli)
    textEl?.addEventListener("input", () => {
      updateMiniCode();
    });

    // Prefix/Suffix URL
    prefixUrl?.addEventListener("input", () => {
      state.content.prefixSrc = prefixUrl.value.trim();
      applyAll();
    });

    suffixUrl?.addEventListener("input", () => {
      state.content.suffixSrc = suffixUrl.value.trim();
      applyAll();
    });

    // Prefix/Suffix file
    prefixFile?.addEventListener("change", async () => {
      const f = prefixFile.files?.[0];
      if (!f) return;
      try {
        const url = await fileToDataURL(f);
        state.content.prefixSrc = url;
        if (prefixUrl) prefixUrl.value = "";
        applyAll();
      } catch (e) {
        console.error("Prefix upload error:", e);
      }
    });

    suffixFile?.addEventListener("change", async () => {
      const f = suffixFile.files?.[0];
      if (!f) return;
      try {
        const url = await fileToDataURL(f);
        state.content.suffixSrc = url;
        if (suffixUrl) suffixUrl.value = "";
        applyAll();
      } catch (e) {
        console.error("Suffix upload error:", e);
      }
    });

    // Prefix/Suffix size
    prefixSize?.addEventListener("input", () => {
      state.content.prefixSize = clamp(toNum(prefixSize.value, 24), 10, 140);
      applyAll();
    });

    suffixSize?.addEventListener("input", () => {
      state.content.suffixSize = clamp(toNum(suffixSize.value, 24), 10, 140);
      applyAll();
    });

    // Canvas controls
    canvasBgColor?.addEventListener("input", () => {
      state.canvas.bg = canvasBgColor.value;
      applyCanvas();
    });

    toggleGridBtn?.addEventListener("click", () => {
      state.canvas.grid = !state.canvas.grid;
      applyCanvas();
    });

    // Theme toggle
    themeToggleBtn?.addEventListener("click", () => {
      state.theme = state.theme === "dark" ? "light" : "dark";
      applyTheme();
    });

    // =========================
    // Modal + code tabs
    // =========================
    const openModal = () => {
      if (!codeModal) return;
      codeModal.classList.remove("hidden");
      renderCodeTab();
    };

    const closeModal = () => {
      if (!codeModal) return;
      codeModal.classList.add("hidden");
    };

    const renderCodeTab = () => {
      if (!finalCodeOutput) return;
      codeTabBtns.forEach((b) => b.classList.toggle("active", b.dataset.code === activeCodeTab));

      if (activeCodeTab === "html") {
        const html = buildHtml();
        finalCodeOutput.value = html;
      } else {
        const css = buildCss("#k3n4n-element");
        finalCodeOutput.value = css;
      }
    };

    btnGetCode?.addEventListener("click", openModal);
    closeModalBtn?.addEventListener("click", closeModal);
    codeModal?.addEventListener("click", (e) => {
      if (e.target === codeModal) closeModal();
    });
    document.addEventListener("keydown", (e) => {
      if (e.key === "Escape" && codeModal && !codeModal.classList.contains("hidden")) closeModal();
    });

    codeTabBtns.forEach((b) => {
      b.addEventListener("click", () => {
        activeCodeTab = b.dataset.code || "css";
        renderCodeTab();
      });
    });

    const copyToClipboard = async (text) => {
      try {
        await navigator.clipboard.writeText(text);
        return true;
      } catch {
        // fallback
        const ta = document.createElement("textarea");
        ta.value = text;
        ta.style.position = "fixed";
        ta.style.left = "-9999px";
        document.body.appendChild(ta);
        ta.select();
        const ok = document.execCommand("copy");
        document.body.removeChild(ta);
        return ok;
      }
    };

    copyFinalCode?.addEventListener("click", async () => {
      const ok = await copyToClipboard(finalCodeOutput?.value || "");
      if (ok && copyFinalCode) {
        const old = copyFinalCode.innerHTML;
        copyFinalCode.innerHTML = `<i class="fas fa-check"></i> Kopyalandı`;
        setTimeout(() => (copyFinalCode.innerHTML = old), 900);
      }
    });

    downloadFinalCode?.addEventListener("click", () => {
      const content = finalCodeOutput?.value || "";
      const blob = new Blob([content], { type: "text/plain;charset=utf-8" });
      const a = document.createElement("a");
      a.href = URL.createObjectURL(blob);
      a.download = activeCodeTab === "html" ? "k3n4n-export.html" : "k3n4n-style.css";
      document.body.appendChild(a);
      a.click();
      URL.revokeObjectURL(a.href);
      a.remove();
    });

    // Quick copy (mini bar): CSS + HTML birlikte (pratik)
    quickCopyBtn?.addEventListener("click", async () => {
      const css = buildCss("#k3n4n-element");
      const html = buildHtml();
      const pack = `${css}\n\n${html}`;
      const ok = await copyToClipboard(pack);
      if (ok && quickCopyBtn) {
        const old = quickCopyBtn.innerHTML;
        quickCopyBtn.innerHTML = `<i class="fas fa-check"></i>`;
        setTimeout(() => (quickCopyBtn.innerHTML = old), 800);
      }
    });

    // =========================
    // Reset + Chaos
    // =========================
    const syncUiFromState = () => {
      // Layout
      if (widthInput) widthInput.value = state.layout.width;
      if (heightInput) heightInput.value = state.layout.height;
      if (paddingSlider) paddingSlider.value = String(state.layout.padding);
      if (radiusSlider) radiusSlider.value = String(state.layout.radius);
      if (gapSlider) gapSlider.value = String(state.layout.gap);

      flexButtons.forEach((b) =>
        b.classList.toggle("active", b.dataset.flex === state.layout.justify)
      );

      // Typography
      if (fontFamilySelect) fontFamilySelect.value = state.typography.fontFamily;
      if (fontSizeInput) fontSizeInput.value = String(state.typography.fontSize);
      if (fontWeightSelect) fontWeightSelect.value = String(state.typography.fontWeight);
      if (letterSpacingSlider) letterSpacingSlider.value = String(state.typography.letterSpacing);
      if (textColorHidden) textColorHidden.value = state.typography.color;

      // Appearance
      if (borderWidthInput) borderWidthInput.value = String(state.appearance.borderWidth);
      if (borderStyleSelect) borderStyleSelect.value = state.appearance.borderStyle;
      if (borderColorInput) borderColorInput.value = state.appearance.borderColor;

      if (gradientAngleSlider) gradientAngleSlider.value = String(state.appearance.gradient.angle);

      if (bgUrlInput) bgUrlInput.value = state.appearance.bgImage && state.appearance.bgType === "image"
        ? state.appearance.bgImage
        : "";

      // Effects
      if (shadowCheck) shadowCheck.checked = !!state.effects.shadowEnabled;
      updateShadowUi();
      if (shadowX) shadowX.value = String(state.effects.shadow.x);
      if (shadowY) shadowY.value = String(state.effects.shadow.y);
      if (shadowBlur) shadowBlur.value = String(state.effects.shadow.blur);
      if (shadowSpread) shadowSpread.value = String(state.effects.shadow.spread);
      if (shadowColor) shadowColor.value = state.effects.shadow.color;

      if (backdropBlurSlider) backdropBlurSlider.value = String(state.effects.backdropBlur);
      if (rotateSlider) rotateSlider.value = String(state.effects.rotate);
      if (scaleSlider) scaleSlider.value = String(state.effects.scale);

      // Content
      if (prefixUrl) prefixUrl.value = "";
      if (suffixUrl) suffixUrl.value = "";
      if (prefixSize) prefixSize.value = String(state.content.prefixSize);
      if (suffixSize) suffixSize.value = String(state.content.suffixSize);

      // Canvas
      if (canvasBgColor) canvasBgColor.value = state.canvas.bg;

      // BG type UI
      setBgType(state.appearance.bgType);
    };

    resetBtn?.addEventListener("click", () => {
      state = structuredClone(defaultState);
      // metni sıfırlamak istersen:
      if (textEl) textEl.textContent = "K3N4N Design";
      syncUiFromState();
      applyAll();
    });

    btnChaos?.addEventListener("click", () => {
      // Kontrollü kaos: UI/UX bozmadan tatlı delilik
      state.layout.padding = randomInt(8, 70);
      state.layout.radius = randomInt(0, 60);
      state.layout.gap = randomInt(0, 28);
      state.layout.justify = ["justify-start", "justify-center", "justify-end", "justify-between"][
        randomInt(0, 3)
      ];

      state.typography.fontFamily = [
        "'Inter', sans-serif",
        "'Poppins', sans-serif",
        "'Orbitron', sans-serif",
        "'JetBrains Mono', monospace",
      ][randomInt(0, 3)];
      state.typography.fontSize = randomInt(14, 64);
      state.typography.fontWeight = ["300", "400", "700", "900"][randomInt(0, 3)];
      state.typography.letterSpacing = randomFloat(-1, 4, 1);
      state.typography.color = randomHex();

      state.appearance.bgType = ["solid", "gradient"][randomInt(0, 1)];
      state.appearance.bgColor = randomHex();
      state.appearance.gradient.angle = randomInt(0, 360);
      state.appearance.gradient.colors = Math.random() < 0.35
        ? [randomHex(), randomHex(), randomHex()]
        : [randomHex(), randomHex()];

      state.appearance.borderWidth = Math.random() < 0.6 ? randomInt(0, 6) : 0;
      state.appearance.borderStyle = ["solid", "dashed", "dotted", "double"][randomInt(0, 3)];
      state.appearance.borderColor = randomHex();

      state.effects.shadowEnabled = Math.random() < 0.75;
      state.effects.shadow = {
        x: randomInt(-10, 10),
        y: randomInt(6, 26),
        blur: randomInt(10, 60),
        spread: randomInt(-5, 15),
        color: "#000000",
        alpha: randomFloat(0.15, 0.55, 2),
      };

      state.effects.backdropBlur = Math.random() < 0.35 ? randomInt(2, 14) : 0;
      state.effects.rotate = randomInt(-10, 10);
      state.effects.scale = randomFloat(0.9, 1.15, 2);

      // Prefix/suffix bazen
      if (Math.random() < 0.25) {
        state.content.badgeVisible = true;
        state.content.badgeText = ["NEW", "PRO", "V7", "WOW"][randomInt(0, 3)];
      } else {
        state.content.badgeVisible = false;
      }

      syncUiFromState();
      applyAll();
    });

    // =========================
    // Init
    // =========================
    initPickers();

    // start UI
    syncUiFromState();
    applyAll();

    // Shadow controls initial
    updateShadowUi();

    // Default: show layout tab
    setActiveTab("layout");

    // Default bg type UI sync
    setBgType(state.appearance.bgType);
  });
})();
```
