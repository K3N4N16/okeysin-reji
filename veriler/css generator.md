# CSS Generator JavaScript Kodu

## Prompt 1

### You
*2026-03-06 20:06:54 +03*

<!DOCTYPE html>
<html lang="tr" data-theme="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>K3N4N CSS Generator V7.0 — Ultimate Pro</title>

    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=VT323&family=Press+Start+2P&family=Orbitron:wght@400;500;600;700;800;900&family=Roboto+Mono:ital,wght@0,400;0,700;1,400&family=Lobster&family=Kaushan+Script&family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,400&family=Fira+Code:wght@300;400;500;600;700&family=Inter:wght@100;200;300;400;500;600;700;800;900&family=Space+Grotesk:wght@300;400;500;600;700&family=JetBrains+Mono:ital,wght@0,400;0,700;1,400&family=Playfair+Display:ital,wght@0,400;0,700;0,900;1,400&family=Raleway:ital,wght@0,100;0,400;0,700;0,900;1,400&family=Bebas+Neue&family=Dancing+Script:wght@400;700&family=Pacifico&family=Righteous&family=Cinzel:wght@400;700;900&family=Exo+2:ital,wght@0,100;0,400;0,700;0,900;1,400&family=Nunito:wght@200;400;700;900&family=Secular+One&family=Monoton&family=Bungee&family=Bungee+Shade&display=swap" rel="stylesheet">

    <!-- Font Awesome 6 -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">

    <!-- External Libraries -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/chroma-js/2.4.2/chroma.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/@jaames/iro@5/dist/iro.min.js"></script>

    <!-- Ana CSS -->
    <link rel="stylesheet" href="style.css">
</head>
<body>

    <!-- ═══════════════════════════════════════════════════
         TOAST NOTIFICATION CONTAINER
    ═══════════════════════════════════════════════════ -->
    <div class="toast-container" id="toastContainer" aria-live="polite" aria-atomic="true"></div>

    <!-- ═══════════════════════════════════════════════════
         COMMAND PALETTE (Ctrl+K)
    ═══════════════════════════════════════════════════ -->
    <div class="command-palette-overlay" id="commandPaletteOverlay">
        <div class="command-palette" id="commandPalette" role="dialog" aria-label="Komut Paleti">
            <div class="command-palette-header">
                <i class="fas fa-terminal"></i>
                <input type="text" id="commandPaletteInput" placeholder="Komut ara... (örn: neon, gradient, reset)" autocomplete="off" spellcheck="false">
                <kbd>ESC</kbd>
            </div>
            <div class="command-palette-results" id="commandPaletteResults"></div>
            <div class="command-palette-footer">
                <span><kbd>↑↓</kbd> Gezin</span>
                <span><kbd>Enter</kbd> Uygula</span>
                <span><kbd>Esc</kbd> Kapat</span>
            </div>
        </div>
    </div>

    <!-- ═══════════════════════════════════════════════════
         SHORTCUT CHEAT SHEET MODAL
    ═══════════════════════════════════════════════════ -->
    <div class="modal-overlay" id="shortcutModalOverlay">
        <div class="modal" id="shortcutModal" role="dialog" aria-label="Klavye Kısayolları">
            <div class="modal-header">
                <h2><i class="fas fa-keyboard"></i> Klavye Kısayolları</h2>
                <button class="modal-close" id="shortcutModalClose" aria-label="Kapat"><i class="fas fa-times"></i></button>
            </div>
            <div class="modal-body">
                <div class="shortcut-grid">
                    <div class="shortcut-section">
                        <h3>Genel</h3>
                        <div class="shortcut-item"><kbd>Ctrl</kbd>+<kbd>Z</kbd><span>Geri Al</span></div>
                        <div class="shortcut-item"><kbd>Ctrl</kbd>+<kbd>Y</kbd><span>İleri Al</span></div>
                        <div class="shortcut-item"><kbd>Ctrl</kbd>+<kbd>S</kbd><span>CSS Kopyala</span></div>
                        <div class="shortcut-item"><kbd>Ctrl</kbd>+<kbd>K</kbd><span>Komut Paleti</span></div>
                        <div class="shortcut-item"><kbd>Ctrl</kbd>+<kbd>D</kbd><span>CSS İndir</span></div>
                        <div class="shortcut-item"><kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>R</kbd><span>Tümünü Sıfırla</span></div>
                        <div class="shortcut-item"><kbd>Ctrl</kbd>+<kbd>T</kbd><span>Tema Değiştir</span></div>
                        <div class="shortcut-item"><kbd>?</kbd><span>Kısayolları Göster</span></div>
                    </div>
                    <div class="shortcut-section">
                        <h3>Kaos & Stil</h3>
                        <div class="shortcut-item"><kbd>Ctrl</kbd>+<kbd>G</kbd><span>Otomatik Stil Oluştur</span></div>
                        <div class="shortcut-item"><kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>G</kbd><span>Maksimum Kaos</span></div>
                        <div class="shortcut-item"><kbd>Ctrl</kbd>+<kbd>R</kbd><span>Rnd Renk</span></div>
                        <div class="shortcut-item"><kbd>Ctrl</kbd>+<kbd>F</kbd><span>Rnd Font</span></div>
                        <div class="shortcut-item"><kbd>Space</kbd><span>Anim. Durdur/Başlat</span></div>
                    </div>
                    <div class="shortcut-section">
                        <h3>Önizleme</h3>
                        <div class="shortcut-item"><kbd>Ctrl</kbd>+<kbd>1</kbd><span>Mobil Görünüm</span></div>
                        <div class="shortcut-item"><kbd>Ctrl</kbd>+<kbd>2</kbd><span>Tablet Görünüm</span></div>
                        <div class="shortcut-item"><kbd>Ctrl</kbd>+<kbd>3</kbd><span>Masaüstü Görünüm</span></div>
                        <div class="shortcut-item"><kbd>Ctrl</kbd>+<kbd>P</kbd><span>Tam Ekran Önizleme</span></div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- ═══════════════════════════════════════════════════
         FULLSCREEN PREVIEW MODAL
    ═══════════════════════════════════════════════════ -->
    <div class="modal-overlay fullscreen-preview-overlay" id="fullscreenPreviewOverlay">
        <div class="fullscreen-preview-modal" id="fullscreenPreviewModal">
            <button class="fullscreen-close" id="fullscreenClose" aria-label="Kapat">
                <i class="fas fa-times"></i>
            </button>
            <div class="fullscreen-preview-inner">
                <div id="fullscreenPreviewBox"></div>
            </div>
        </div>
    </div>

    <!-- ═══════════════════════════════════════════════════
         CUBIC-BEZIER EDITOR MODAL
    ═══════════════════════════════════════════════════ -->
    <div class="modal-overlay" id="bezierModalOverlay">
        <div class="modal bezier-modal" id="bezierModal" role="dialog" aria-label="Cubic Bezier Editörü">
            <div class="modal-header">
                <h2><i class="fas fa-bezier-curve"></i> Cubic Bezier Editörü</h2>
                <button class="modal-close" id="bezierModalClose" aria-label="Kapat"><i class="fas fa-times"></i></button>
            </div>
            <div class="modal-body">
                <canvas id="bezierCanvas" width="260" height="260"></canvas>
                <div class="bezier-controls">
                    <div class="form-row">
                        <label>P1 X:</label><input type="number" id="bezierP1x" value="0.25" min="0" max="1" step="0.01">
                        <label>P1 Y:</label><input type="number" id="bezierP1y" value="0.46" min="-2" max="3" step="0.01">
                    </div>
                    <div class="form-row">
                        <label>P2 X:</label><input type="number" id="bezierP2x" value="0.45" min="0" max="1" step="0.01">
                        <label>P2 Y:</label><input type="number" id="bezierP2y" value="0.94" min="-2" max="3" step="0.01">
                    </div>
                    <div class="bezier-output" id="bezierOutput">cubic-bezier(0.25, 0.46, 0.45, 0.94)</div>
                    <div class="bezier-presets">
                        <button class="bezier-preset-btn" data-bezier="0.25,0.46,0.45,0.94">Soft</button>
                        <button class="bezier-preset-btn" data-bezier="0.68,-0.55,0.265,1.55">Bounce</button>
                        <button class="bezier-preset-btn" data-bezier="0.34,1.56,0.64,1">Spring</button>
                        <button class="bezier-preset-btn" data-bezier="0.77,0,0.175,1">Expo</button>
                        <button class="bezier-preset-btn" data-bezier="0.23,1,0.32,1">Quint</button>
                        <button class="bezier-preset-btn" data-bezier="0.175,0.885,0.32,1.275">Back</button>
                    </div>
                    <button class="output-btn primary" id="applyBezierBtn" style="width:100%;margin-top:8px;">
                        <i class="fas fa-check"></i> Uygula
                    </button>
                </div>
            </div>
        </div>
    </div>

    <!-- ═══════════════════════════════════════════════════
         HEADER / TOP BAR
    ═══════════════════════════════════════════════════ -->
    <header class="app-header" role="banner">
        <!-- Logo -->
        <a class="logo" href="#" aria-label="K3N4N CSS Generator V7.0">
            <div class="logo-icon">
                <i class="fas fa-wand-magic-sparkles"></i>
            </div>
            <div class="logo-text">
                <span class="logo-title">K3N4N</span>
                <span class="logo-sub">CSS Generator <em>V7.0</em></span>
            </div>
        </a>

        <!-- Center: Quick Actions -->
        <div class="header-center">
            <button class="quick-action-btn" data-style-target="auto-generate" data-tooltip="Otomatik Stil (Ctrl+G)">
                <i class="fas fa-wand-magic-sparkles"></i><span>Auto Stil</span>
            </button>
            <button class="quick-action-btn chaos" data-style-target="max-chaos" data-tooltip="Kaos Modu (Ctrl+Shift+G)">
                <i class="fas fa-explosion"></i><span>Kaos</span>
            </button>
            <div class="header-separator"></div>
            <button class="quick-action-btn" data-action="command-palette" data-tooltip="Komut Paleti (Ctrl+K)">
                <i class="fas fa-terminal"></i><span>⌘K</span>
            </button>
        </div>

        <!-- Right: Header Actions -->
        <div class="header-actions">
            <!-- Responsive Preview Switcher -->
            <div class="preview-size-group" role="group" aria-label="Önizleme boyutu">
                <button class="preview-size-btn active" data-preview-size="desktop" data-tooltip="Masaüstü" aria-pressed="true">
                    <i class="fas fa-desktop"></i>
                </button>
                <button class="preview-size-btn" data-preview-size="tablet" data-tooltip="Tablet" aria-pressed="false">
                    <i class="fas fa-tablet-screen-button"></i>
                </button>
                <button class="preview-size-btn" data-preview-size="mobile" data-tooltip="Mobil" aria-pressed="false">
                    <i class="fas fa-mobile-screen"></i>
                </button>
            </div>

            <div class="header-separator"></div>

            <!-- Undo/Redo -->
            <button class="header-btn" data-action="undo" disabled data-tooltip="Geri Al (Ctrl+Z)" aria-label="Geri Al">
                <i class="fas fa-undo-alt"></i>
                <span class="history-count" id="undoCount">0</span>
            </button>
            <button class="header-btn" data-action="redo" disabled data-tooltip="İleri Al (Ctrl+Y)" aria-label="İleri Al">
                <i class="fas fa-redo-alt"></i>
                <span class="history-count" id="redoCount">0</span>
            </button>

            <div class="header-separator"></div>

            <!-- Theme Toggle -->
            <button class="header-btn icon-btn theme-btn" data-action="toggle-theme" data-tooltip="Tema Değiştir (Ctrl+T)" aria-label="Tema Değiştir">
                <i class="fas fa-moon"></i>
            </button>

            <!-- Shortcuts -->
            <button class="header-btn icon-btn" data-action="show-shortcuts" data-tooltip="Kısayollar (?)" aria-label="Kısayolları Göster">
                <i class="fas fa-keyboard"></i>
            </button>

            <!-- Fullscreen Preview -->
            <button class="header-btn icon-btn" data-action="fullscreen-preview" data-tooltip="Tam Ekran (Ctrl+P)" aria-label="Tam Ekran">
                <i class="fas fa-expand"></i>
            </button>

            <!-- Reset -->
            <button class="header-btn reset-btn" data-action="reset-all" data-tooltip="Sıfırla (Ctrl+Shift+R)" aria-label="Tümünü Sıfırla">
                <i class="fas fa-trash-restore"></i>
                <span>Sıfırla</span>
            </button>
        </div>
    </header>

    <!-- ═══════════════════════════════════════════════════
         MOBILE SIDEBAR TOGGLE
    ═══════════════════════════════════════════════════ -->
    <button class="sidebar-toggle" id="sidebarToggle" aria-label="Menüyü aç/kapat" aria-expanded="false">
        <i class="fas fa-sliders-h"></i>
    </button>
    <div class="sidebar-overlay" id="sidebarOverlay" aria-hidden="true"></div>

    <!-- ═══════════════════════════════════════════════════
         APP CONTAINER
    ═══════════════════════════════════════════════════ -->
    <div class="app-container">

        <!-- ══════════════════════════════════════
             SIDEBAR
        ══════════════════════════════════════ -->
        <aside class="sidebar" id="sidebar" role="navigation" aria-label="Stil Panelleri">

            <!-- Sidebar Header -->
            <div class="sidebar-header">
                <div class="sidebar-search">
                    <i class="fas fa-search" aria-hidden="true"></i>
                    <input type="text" id="panelSearch" placeholder="Panel ara..." aria-label="Panel arama" autocomplete="off">
                    <button class="search-clear" id="searchClear" aria-label="Aramayı temizle" style="display:none;">
                        <i class="fas fa-times"></i>
                    </button>
                </div>
            </div>

            <!-- ─────────────────────────────────
                 PANEL 1: METİN STİLLERİ PRO
            ───────────────────────────────── -->
            <div class="panel expanded" data-panel="text">
                <div class="panel-header" role="button" tabindex="0" aria-expanded="true">
                    <div class="panel-icon text"><i class="fas fa-font" aria-hidden="true"></i></div>
                    <span class="panel-title">Metin Stilleri Pro</span>
                    <span class="panel-badge">PRO</span>
                    <i class="fas fa-chevron-up panel-toggle" aria-hidden="true"></i>
                </div>
                <div class="panel-body">
                    <!-- Quick Random Buttons -->
                    <div class="btn-grid">
                        <button class="style-btn" data-style-target="random-font"><i class="fas fa-dice"></i> Rnd Font</button>
                        <button class="style-btn" data-style-target="random-color"><i class="fas fa-palette"></i> Rnd Renk</button>
                        <button class="style-btn" data-style-target="random-text-shadow"><i class="fas fa-clone"></i> Rnd Gölge</button>
                        <button class="style-btn" data-style-target="random-text-decoration"><i class="fas fa-underline"></i> Rnd Dekor</button>
                        <button class="style-btn" data-style-target="random-spacing"><i class="fas fa-arrows-alt-h"></i> Rnd Boşluk</button>
                        <button class="style-btn" data-style-target="random-align"><i class="fas fa-align-center"></i> Rnd Hiza</button>
                        <button class="style-btn" data-style-target="random-line-height"><i class="fas fa-text-height"></i> Rnd Satır</button>
                        <button class="style-btn" data-style-target="random-text-transform"><i class="fas fa-text-width"></i> Rnd Dönüşüm</button>
                        <!-- YENİ -->
                        <button class="style-btn" data-style-target="random-text-stroke"><i class="fas fa-pen-nib"></i> Rnd Stroke</button>
                        <button class="style-btn" data-style-target="random-multi-text-shadow"><i class="fas fa-layer-group"></i> Çoklu Gölge</button>
                    </div>

                    <div class="separator"></div>

                    <!-- Font Family -->
                    <div class="form-group">
                        <label for="fontFamily">
                            <i class="fas fa-font"></i> Yazı Fontu
                        </label>
                        <div class="font-preview-wrapper">
                            <select id="fontFamily" data-style-prop="fontFamily" aria-label="Yazı tipi seçin">
                                <optgroup label="Sans-Serif">
                                    <option value="'Poppins', sans-serif">Poppins</option>
                                    <option value="'Inter', sans-serif">Inter</option>
                                    <option value="'Space Grotesk', sans-serif">Space Grotesk</option>
                                    <option value="'Raleway', sans-serif">Raleway</option>
                                    <option value="'Nunito', sans-serif">Nunito</option>
                                    <option value="'Exo 2', sans-serif">Exo 2</option>
                                </optgroup>
                                <optgroup label="Display">
                                    <option value="'Orbitron', sans-serif">Orbitron</option>
                                    <option value="'Bebas Neue', sans-serif">Bebas Neue</option>
                                    <option value="'Righteous', sans-serif">Righteous</option>
                                    <option value="'Secular One', sans-serif">Secular One</option>
                                    <option value="'Bungee', sans-serif">Bungee</option>
                                    <option value="'Bungee Shade', sans-serif">Bungee Shade</option>
                                    <option value="'Monoton', cursive">Monoton</option>
                                </optgroup>
                                <optgroup label="Serif">
                                    <option value="'Playfair Display', serif">Playfair Display</option>
                                    <option value="'Cinzel', serif">Cinzel</option>
                                    <option value="Georgia, serif">Georgia</option>
                                </optgroup>
                                <optgroup label="Monospace">
                                    <option value="'VT323', monospace">VT323</option>
                                    <option value="'Press Start 2P', monospace">Press Start 2P</option>
                                    <option value="'Roboto Mono', monospace">Roboto Mono</option>
                                    <option value="'JetBrains Mono', monospace">JetBrains Mono</option>
                                    <option value="'Fira Code', monospace">Fira Code</option>
                                    <option value="'Courier New', monospace">Courier New</option>
                                </optgroup>
                                <optgroup label="Kursiv / El Yazısı">
                                    <option value="'Lobster', cursive">Lobster</option>
                                    <option value="'Kaushan Script', cursive">Kaushan Script</option>
                                    <option value="'Dancing Script', cursive">Dancing Script</option>
                                    <option value="'Pacifico', cursive">Pacifico</option>
                                </optgroup>
                                <optgroup label="Sistem">
                                    <option value="Impact, sans-serif">Impact</option>
                                    <option value="'Arial Black', sans-serif">Arial Black</option>
                                </optgroup>
                            </select>
                            <div class="font-preview-text" id="fontPreviewText" aria-hidden="true">Aa</div>
                        </div>
                    </div>

                    <!-- Font Size -->
                    <div class="form-group">
                        <label>
                            <i class="fas fa-text-height"></i> Yazı Boyutu
                            <span class="value-badge" id="fontSizeVal">30px</span>
                        </label>
                        <input type="range" id="fontSizeRange" min="8" max="120" value="30" aria-label="Yazı boyutu">
                        <input type="number" id="fontSize" data-style-prop="fontSize" data-style-unit="px" value="30" min="1" max="300" aria-label="Yazı boyutu piksel">
                    </div>

                    <!-- Font Weight -->
                    <div class="form-group">
                        <label>
                            <i class="fas fa-bold"></i> Font Ağırlığı
                            <span class="value-badge" id="fontWeightVal">400</span>
                        </label>
                        <input type="range" id="fontWeightRange" min="100" max="900" step="100" value="400" aria-label="Font ağırlığı">
                        <select id="fontWeight" data-style-prop="fontWeight" aria-label="Font ağırlığı seçin">
                            <option value="100">100 — Thin</option>
                            <option value="200">200 — Extra Light</option>
                            <option value="300">300 — Light</option>
                            <option value="400" selected>400 — Normal</option>
                            <option value="500">500 — Medium</option>
                            <option value="600">600 — Semi Bold</option>
                            <option value="700">700 — Bold</option>
                            <option value="800">800 — Extra Bold</option>
                            <option value="900">900 — Black</option>
                        </select>
                    </div>

                    <!-- Text Color -->
                    <div class="form-group">
                        <label><i class="fas fa-droplet"></i> Yazı Rengi</label>
                        <div id="textColorPicker" class="color-picker-container" aria-label="Yazı rengi seçici"></div>
                        <div class="color-hex-row">
                            <input type="text" id="textColorHex" placeholder="#ffffff" maxlength="9" aria-label="Hex renk kodu">
                            <div class="color-swatch" id="textColorSwatch" style="background:#222222;" aria-hidden="true"></div>
                        </div>
                    </div>

                    <!-- Text Shadow Layers — YENİ: Çoklu Gölge -->
                    <div class="form-group">
                        <label>
                            <i class="fas fa-clone"></i> Yazı Gölgeleri
                            <button class="inline-btn" id="addTextShadowLayer" data-tooltip="Yeni gölge katmanı ekle">
                                <i class="fas fa-plus"></i>
                            </button>
                        </label>
                        <div id="textShadowLayers" class="shadow-layers-container">
                            <!-- JS ile doldurulacak -->
                        </div>
                    </div>

                    <!-- Text Stroke — YENİ -->
                    <div class="form-group">
                        <label>
                            <i class="fas fa-pen-nib"></i> Metin Çerçevesi (Stroke)
                            <span class="value-badge" id="textStrokeWidthVal">0px</span>
                        </label>
                        <input type="range" id="textStrokeWidthRange" min="0" max="10" step="0.5" value="0" aria-label="Metin çerçeve kalınlığı">
                        <div id="textStrokeColorPicker" class="color-picker-container" aria-label="Metin çerçeve rengi"></div>
                    </div>

                    <!-- Decoration -->
                    <div class="form-group">
                        <label><i class="fas fa-underline"></i> Metin Dekorasyonu</label>
                        <div class="form-row">
                            <select id="textDecorationLine" data-style-prop="textDecorationLine" aria-label="Dekorasyon çizgisi">
                                <option value="none" selected>Yok</option>
                                <option value="underline">Alt Çizgi</option>
                                <option value="overline">Üst Çizgi</option>
                                <option value="line-through">Üzeri Çizili</option>
                                <option value="underline overline">Alt + Üst</option>
                            </select>
                            <select id="textDecorationStyle" data-style-prop="textDecorationStyle" aria-label="Dekorasyon stili">
                                <option value="solid" selected>Düz</option>
                                <option value="double">Çift</option>
                                <option value="dotted">Noktalı</option>
                                <option value="dashed">Kesikli</option>
                                <option value="wavy">Dalgalı</option>
                            </select>
                        </div>
                        <div id="textDecorationColorPicker" class="color-picker-container" aria-label="Dekorasyon rengi"></div>
                    </div>

                    <!-- Alignment -->
                    <div class="form-group">
                        <label><i class="fas fa-align-left"></i> Hizalama</label>
                        <div class="align-buttons" role="group" aria-label="Metin hizalama">
                            <button class="align-btn active" data-align="left" aria-pressed="false" aria-label="Sola Hizala"><i class="fas fa-align-left"></i></button>
                            <button class="align-btn active" data-align="center" aria-pressed="true" aria-label="Ortala"><i class="fas fa-align-center"></i></button>
                            <button class="align-btn" data-align="right" aria-pressed="false" aria-label="Sağa Hizala"><i class="fas fa-align-right"></i></button>
                            <button class="align-btn" data-align="justify" aria-pressed="false" aria-label="İki Yana Hizala"><i class="fas fa-align-justify"></i></button>
                        </div>
                    </div>

                    <!-- Line Height -->
                    <div class="form-group">
                        <label>
                            <i class="fas fa-arrows-alt-v"></i> Satır Yüksekliği
                            <span class="value-badge" id="lineHeightVal">1.5</span>
                        </label>
                        <input type="range" id="lineHeightRange" min="0.5" max="4" step="0.1" value="1.5" aria-label="Satır yüksekliği">
                    </div>

                    <!-- Spacing -->
                    <div class="form-group">
                        <label><i class="fas fa-arrows-alt-h"></i> Boşluklar</label>
                        <div class="form-row">
                            <label>Harf:</label>
                            <input type="number" id="letterSpacing" data-style-prop="letterSpacing" data-style-unit="px" value="0" step="0.5" aria-label="Harf aralığı">
                            <label>Kelime:</label>
                            <input type="number" id="wordSpacing" data-style-prop="wordSpacing" data-style-unit="px" value="0" step="0.5" aria-label="Kelime aralığı">
                        </div>
                    </div>

                    <!-- Text Transform -->
                    <div class="form-group">
                        <label><i class="fas fa-text-width"></i> Metin Dönüşümü</label>
                        <select id="textTransform" data-style-prop="textTransform" aria-label="Metin dönüşümü">
                            <option value="none" selected>Yok</option>
                            <option value="uppercase">BÜYÜK HARF</option>
                            <option value="lowercase">küçük harf</option>
                            <option value="capitalize">Baş Harfler Büyük</option>
                        </select>
                    </div>

                    <!-- Font Style -->
                    <div class="form-group">
                        <label><i class="fas fa-italic"></i> Font Stili</label>
                        <select id="fontStyle" data-style-prop="fontStyle" aria-label="Font stili">
                            <option value="normal" selected>Normal</option>
                            <option value="italic">İtalik</option>
                            <option value="oblique">Eğik</option>
                        </select>
                    </div>

                    <!-- Font Variant — YENİ -->
                    <div class="form-group">
                        <label><i class="fas fa-font"></i> Font Varyant</label>
                        <div class="checkbox-row">
                            <label><input type="checkbox" id="fontVariantSmallCaps" aria-label="Küçük büyük harf"> small-caps</label>
                            <label><input type="checkbox" id="fontVariantLiga" aria-label="Ligature"> Ligature</label>
                            <label><input type="checkbox" id="fontVariantNum" aria-label="Numerik özellikler"> Tabular Num</label>
                        </div>
                    </div>

                    <!-- Writing Mode -->
                    <div class="form-group">
                        <label><i class="fas fa-arrows-rotate"></i> Yazı Yönü</label>
                        <select id="writingMode" data-style-prop="writingMode" aria-label="Yazı yönü">
                            <option value="horizontal-tb" selected>Yatay (Normal)</option>
                            <option value="vertical-rl">Dikey (Sağ→Sol)</option>
                            <option value="vertical-lr">Dikey (Sol→Sağ)</option>
                        </select>
                    </div>

                    <!-- Text Overflow -->
                    <div class="form-group">
                        <label><i class="fas fa-ellipsis-h"></i> Taşma Davranışı</label>
                        <select id="textOverflow" data-style-prop="textOverflow" aria-label="Metin taşma davranışı">
                            <option value="clip" selected>Kes</option>
                            <option value="ellipsis">Üç Nokta (…)</option>
                        </select>
                    </div>

                    <!-- Padding -->
                    <div class="form-group">
                        <label><i class="fas fa-border-none"></i> Padding</label>
                        <div class="padding-grid" id="paddingGrid">
                            <div class="padding-side">
                                <label>Üst</label>
                                <input type="number" id="paddingTop" value="0" min="0" aria-label="Üst padding">
                            </div>
                            <div class="padding-side">
                                <label>Sağ</label>
                                <input type="number" id="paddingRight" value="0" min="0" aria-label="Sağ padding">
                            </div>
                            <div class="padding-side">
                                <label>Alt</label>
                                <input type="number" id="paddingBottom" value="0" min="0" aria-label="Alt padding">
                            </div>
                            <div class="padding-side">
                                <label>Sol</label>
                                <input type="number" id="paddingLeft" value="0" min="0" aria-label="Sol padding">
                            </div>
                            <div class="padding-center">
                                <select id="paddingUnit" aria-label="Padding birimi">
                                    <option value="px" selected>px</option>
                                    <option value="%">%</option>
                                    <option value="rem">rem</option>
                                    <option value="em">em</option>
                                    <option value="vw">vw</option>
                                </select>
                            </div>
                        </div>
                        <label style="margin-top:5px;display:flex;align-items:center;gap:5px;cursor:pointer;font-size:11px;">
                            <input type="checkbox" id="paddingLinked" checked aria-label="Tüm kenarları bağla">
                            <i class="fas fa-link" style="font-size:10px;"></i> Bağlantılı
                        </label>
                    </div>
                </div>
            </div>

            <!-- ─────────────────────────────────
                 PANEL 2: ARKA PLAN PRO
            ───────────────────────────────── -->
            <div class="panel" data-panel="background">
                <div class="panel-header" role="button" tabindex="0" aria-expanded="false">
                    <div class="panel-icon bg"><i class="fas fa-fill-drip" aria-hidden="true"></i></div>
                    <span class="panel-title">Arka Plan Pro</span>
                    <i class="fas fa-chevron-up panel-toggle" aria-hidden="true"></i>
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
                        <button class="style-btn" data-style-target="random-bg-blend"><i class="fas fa-layer-group"></i> Rnd Karış.</button>
                        <!-- YENİ -->
                        <button class="style-btn" data-style-target="random-mesh-gradient"><i class="fas fa-circle-nodes"></i> Mesh Grad.</button>
                        <button class="style-btn" data-style-target="random-noise-texture"><i class="fas fa-wave-square"></i> Gürültü</button>
                    </div>

                    <div class="separator"></div>

                    <!-- Background Tabs -->
                    <div class="sub-tabs" role="tablist">
                        <button class="sub-tab active" data-sub-tab="bg-solid" role="tab" aria-selected="true">Düz</button>
                        <button class="sub-tab" data-sub-tab="bg-gradient" role="tab" aria-selected="false">Gradyan</button>
                        <button class="sub-tab" data-sub-tab="bg-image" role="tab" aria-selected="false">Resim</button>
                        <button class="sub-tab" data-sub-tab="bg-pattern" role="tab" aria-selected="false">Desen</button>
                    </div>

                    <!-- Solid Color Tab -->
                    <div class="sub-tab-content active" id="bg-solid">
                        <div class="form-group">
                            <label><i class="fas fa-droplet"></i> Arka Plan Rengi</label>
                            <div id="backgroundColorPicker" class="color-picker-container" aria-label="Arka plan rengi seçici"></div>
                            <div class="color-hex-row">
                                <input type="text" id="bgColorHex" placeholder="#ffffff" maxlength="9" aria-label="Arka plan hex renk kodu">
                                <div class="color-swatch" id="bgColorSwatch" style="background:#ffffff;" aria-hidden="true"></div>
                            </div>
                        </div>
                        <div class="form-group">
                            <label>
                                <i class="fas fa-circle-half-stroke"></i> Opaklık
                                <span class="value-badge" id="bgOpacityVal">1</span>
                            </label>
                            <input type="range" id="backgroundOpacityRange" min="0" max="1" step="0.05" value="1" aria-label="Arka plan opaklığı">
                        </div>
                    </div>

                    <!-- Gradient Tab -->
                    <div class="sub-tab-content" id="bg-gradient">
                        <div class="form-group">
                            <label><i class="fas fa-sliders-h"></i> Gradyan Ayarları</label>
                            <div class="form-row">
                                <label>Tür:</label>
                                <select id="gradientType" aria-label="Gradyan türü">
                                    <option value="linear" selected>Doğrusal</option>
                                    <option value="radial">Radyal</option>
                                    <option value="conic">Konik</option>
                                </select>
                            </div>
                            <div class="form-row">
                                <label>Açı:</label>
                                <input type="number" id="gradientAngle" value="90" min="0" max="360" aria-label="Gradyan açısı">
                                <span class="unit-label">°</span>
                                <input type="range" id="gradientAngleRange" min="0" max="360" value="90" style="flex:2;" aria-label="Gradyan açısı kaydırıcı">
                            </div>
                        </div>
                        <div id="gradientColors" class="gradient-colors"></div>
                        <button class="add-color-btn" id="addGradientColor">
                            <i class="fas fa-plus"></i> Renk Ekle
                        </button>
                        <!-- Gradient Preview Bar -->
                        <div class="gradient-preview-bar" id="gradientPreviewBar" aria-hidden="true"></div>
                    </div>

                    <!-- Image Tab -->
                    <div class="sub-tab-content" id="bg-image">
                        <div class="form-group">
                            <label><i class="fas fa-link"></i> Resim/GIF URL</label>
                            <input type="text" id="backgroundImageUrl" placeholder="https://..." aria-label="Arka plan resim URL">
                        </div>
                        <div class="form-group">
                            <label><i class="fas fa-arrows-alt"></i> Konum</label>
                            <div class="bg-position-grid" id="bgPositionGrid" aria-label="Arka plan konumu">
                                <button class="pos-btn" data-pos="top left">↖</button>
                                <button class="pos-btn" data-pos="top center">↑</button>
                                <button class="pos-btn" data-pos="top right">↗</button>
                                <button class="pos-btn" data-pos="center left">←</button>
                                <button class="pos-btn active" data-pos="center center">⊕</button>
                                <button class="pos-btn" data-pos="center right">→</button>
                                <button class="pos-btn" data-pos="bottom left">↙</button>
                                <button class="pos-btn" data-pos="bottom center">↓</button>
                                <button class="pos-btn" data-pos="bottom right">↘</button>
                            </div>
                        </div>
                        <div class="form-group">
                            <label><i class="fas fa-expand-arrows-alt"></i> Boyut</label>
                            <select id="backgroundSize" data-style-prop="backgroundSize" aria-label="Arka plan boyutu">
                                <option value="auto" selected>Otomatik</option>
                                <option value="cover">Kapla (Cover)</option>
                                <option value="contain">İçer (Contain)</option>
                                <option value="100% 100%">100% × 100%</option>
                                <option value="50% 50%">50% × 50%</option>
                            </select>
                        </div>
                        <div class="form-group">
                            <label><i class="fas fa-redo"></i> Tekrar</label>
                            <select id="backgroundRepeat" data-style-prop="backgroundRepeat" aria-label="Arka plan tekrar">
                                <option value="no-repeat" selected>Tekrarlama</option>
                                <option value="repeat">Her İki Yön</option>
                                <option value="repeat-x">Yatay</option>
                                <option value="repeat-y">Dikey</option>
                                <option value="space">Boşluklu</option>
                                <option value="round">Yuvarlak</option>
                            </select>
                        </div>
                    </div>

                    <!-- Pattern Library Tab — YENİ -->
                    <div class="sub-tab-content" id="bg-pattern">
                        <div class="form-group">
                            <label><i class="fas fa-th"></i> Desen Kütüphanesi</label>
                            <div class="pattern-gallery" id="patternGallery" aria-label="CSS desen galerisi">
                                <!-- JS ile doldurulacak -->
                            </div>
                        </div>
                    </div>

                    <!-- Blend Mode (global) -->
                    <div class="separator"></div>
                    <div class="form-group">
                        <label><i class="fas fa-layer-group"></i> Karıştırma Modu</label>
                        <select id="backgroundBlendMode" data-style-prop="backgroundBlendMode" aria-label="Arka plan karıştırma modu">
                            <option value="normal" selected>Normal</option>
                            <option value="multiply">Çarpma</option>
                            <option value="screen">Ekran</option>
                            <option value="overlay">Kaplama</option>
                            <option value="darken">Koyulaştır</option>
                            <option value="lighten">Aydınlat</option>
                            <option value="color-dodge">Renk Etkisi</option>
                            <option value="color-burn">Renk Yakma</option>
                            <option value="hard-light">Sert Işık</option>
                            <option value="soft-light">Yumuşak Işık</option>
                            <option value="difference">Fark</option>
                            <option value="exclusion">Dışlama</option>
                            <option value="hue">Ton</option>
                            <option value="saturation">Doygunluk</option>
                            <option value="color">Renk</option>
                            <option value="luminosity">Parlaklık</option>
                        </select>
                    </div>
                </div>
            </div>

            <!-- ─────────────────────────────────
                 PANEL 3: ÇERÇEVE & KENARLAR
            ───────────────────────────────── -->
            <div class="panel" data-panel="border">
                <div class="panel-header" role="button" tabindex="0" aria-expanded="false">
                    <div class="panel-icon border"><i class="fas fa-border-all" aria-hidden="true"></i></div>
                    <span class="panel-title">Çerçeve & Kenarlar</span>
                    <i class="fas fa-chevron-up panel-toggle" aria-hidden="true"></i>
                </div>
                <div class="panel-body">
                    <div class="btn-grid">
                        <button class="style-btn" data-style-target="random-multi-border"><i class="fas fa-border-style"></i> Rnd Çerçeve</button>
                        <button class="style-btn" data-style-target="random-outline"><i class="fas fa-square"></i> Rnd Outline</button>
                        <button class="style-btn" data-style-target="random-border-radius"><i class="fas fa-circle"></i> Rnd Yuvarla</button>
                        <button class="style-btn" data-style-target="random-border-color"><i class="fas fa-palette"></i> Rnd Renk</button>
                        <!-- YENİ -->
                        <button class="style-btn" data-style-target="random-gradient-border"><i class="fas fa-wand-sparkles"></i> Gradyan Çerçeve</button>
                        <button class="style-btn" data-style-target="random-border-image"><i class="fas fa-image"></i> Resim Çerçeve</button>
                    </div>

                    <div class="separator"></div>

                    <!-- Border Linked Toggle -->
                    <div class="form-group">
                        <label>
                            <i class="fas fa-border-top-left"></i> Kenar Kalınlığı
                            <label style="font-weight:normal;font-size:10.5px;cursor:pointer;display:flex;align-items:center;gap:4px;">
                                <input type="checkbox" id="borderLinked" checked aria-label="Kenarları birbirine bağla">
                                <i class="fas fa-link" style="font-size:10px;"></i> Bağlı
                            </label>
                        </label>
                        <div class="border-visual-grid">
                            <div></div>
                            <div>
                                <input type="text" id="borderTop" placeholder="2px solid #ccc" aria-label="Üst çerçeve" data-border-side="top">
                            </div>
                            <div></div>
                            <div>
                                <input type="text" id="borderLeft" placeholder="2px solid #ccc" aria-label="Sol çerçeve" data-border-side="left">
                            </div>
                            <div class="border-center-box" aria-hidden="true">
                                <i class="fas fa-square"></i>
                            </div>
                            <div>
                                <input type="text" id="borderRight" placeholder="2px solid #ccc" aria-label="Sağ çerçeve" data-border-side="right">
                            </div>
                            <div></div>
                            <div>
                                <input type="text" id="borderBottom" placeholder="2px solid #ccc" aria-label="Alt çerçeve" data-border-side="bottom">
                            </div>
                            <div></div>
                        </div>
                    </div>

                    <!-- Gradient Border — YENİ -->
                    <div class="form-group">
                        <label>
                            <i class="fas fa-wand-sparkles"></i> Gradyan Çerçeve
                            <span class="badge-new">Yeni</span>
                        </label>
                        <div class="form-row">
                            <label>Genişlik:</label>
                            <input type="number" id="gradientBorderWidth" value="2" min="0" max="20" aria-label="Gradyan çerçeve genişliği">
                            <span class="unit-label">px</span>
                        </div>
                        <div id="gradientBorderColors" class="gradient-colors"></div>
                        <button class="add-color-btn" id="addGradientBorderColor">
                            <i class="fas fa-plus"></i> Renk Ekle
                        </button>
                        <button class="output-btn secondary" id="applyGradientBorder" style="margin-top:6px;width:100%;">
                            <i class="fas fa-check"></i> Gradyan Çerçeve Uygula
                        </button>
                    </div>

                    <!-- Border Radius -->
                    <div class="form-group">
                        <label>
                            <i class="fas fa-circle-dot"></i> Yuvarlak Kenarlar
                            <span class="value-badge" id="borderRadiusVal">10px</span>
                        </label>
                        <input type="range" id="borderRadiusAll" min="0" max="200" value="10" aria-label="Tüm köşeler">
                        <div class="corner-grid">
                            <input type="number" id="borderRadiusTopLeft" data-style-prop="borderTopLeftRadius" data-style-unit="px" value="10" min="0" placeholder="↖" aria-label="Sol üst köşe">
                            <input type="number" id="borderRadiusTopRight" data-style-prop="borderTopRightRadius" data-style-unit="px" value="10" min="0" placeholder="↗" aria-label="Sağ üst köşe">
                            <div class="corner-center" aria-hidden="true"><i class="fas fa-square-full"></i></div>
                            <input type="number" id="borderRadiusBottomLeft" data-style-prop="borderBottomLeftRadius" data-style-unit="px" value="10" min="0" placeholder="↙" aria-label="Sol alt köşe">
                            <input type="number" id="borderRadiusBottomRight" data-style-prop="borderBottomRightRadius" data-style-unit="px" value="10" min="0" placeholder="↘" aria-label="Sağ alt köşe">
                        </div>
                    </div>

                    <!-- Outline -->
                    <div class="form-group">
                        <label><i class="fas fa-vector-square"></i> Dış Çizgi (Outline)</label>
                        <div class="form-row">
                            <label>Genişlik:</label>
                            <input type="number" id="outlineWidth" data-style-prop="outlineWidth" data-style-unit="px" value="0" min="0" aria-label="Outline genişliği">
                            <label>Stil:</label>
                            <select id="outlineStyle" data-style-prop="outlineStyle" aria-label="Outline stili">
                                <option value="none" selected>Yok</option>
                                <option value="solid">Düz</option>
                                <option value="dashed">Kesik</option>
                                <option value="dotted">Noktalı</option>
                                <option value="double">Çift</option>
                                <option value="groove">Oluk</option>
                                <option value="ridge">Çıkıntı</option>
                            </select>
                        </div>
                        <div id="outlineColorPicker" class="color-picker-container" aria-label="Outline rengi"></div>
                        <div class="form-row" style="margin-top:6px;">
                            <label>Offset:</label>
                            <input type="number" id="outlineOffset" data-style-prop="outlineOffset" data-style-unit="px" value="0" aria-label="Outline offset">
                            <span class="unit-label">px</span>
                        </div>
                    </div>
                </div>
            </div>

            <!-- ─────────────────────────────────
                 PANEL 4: DÖNÜŞÜM 3D PRO
            ───────────────────────────────── -->
            <div class="panel" data-panel="transform">
                <div class="panel-header" role="button" tabindex="0" aria-expanded="false">
                    <div class="panel-icon transform"><i class="fas fa-cube" aria-hidden="true"></i></div>
                    <span class="panel-title">Dönüşüm 3D Pro</span>
                    <span class="panel-badge">3D</span>
                    <i class="fas fa-chevron-up panel-toggle" aria-hidden="true"></i>
                </div>
                <div class="panel-body">
                    <div class="btn-grid">
                        <button class="style-btn" data-style-target="random-transform"><i class="fas fa-sync"></i> Rnd Dönüşüm</button>
                        <button class="style-btn" data-style-target="random-3d-transform"><i class="fas fa-cube"></i> Rnd 3D</button>
                        <button class="style-btn" data-style-target="reset-transform"><i class="fas fa-undo"></i> Sıfırla</button>
                    </div>

                    <div class="separator"></div>

                    <!-- 2D Transforms -->
                    <div class="form-group">
                        <label>
                            <i class="fas fa-rotate"></i> Döndür (Rotate)
                            <span class="value-badge" id="rotateVal">0°</span>
                        </label>
                        <input type="range" id="rotateRange" min="-360" max="360" value="0" aria-label="Döndürme açısı">
                        <input type="number" id="rotate" value="0" aria-label="Döndürme açısı değeri">
                    </div>

                    <div class="form-group">
                        <label>
                            <i class="fas fa-up-right-and-down-left-from-center"></i> Ölçek (Scale)
                            <span class="value-badge" id="scaleVal">1</span>
                        </label>
                        <input type="range" id="scaleRange" min="0.1" max="3" step="0.05" value="1" aria-label="Ölçek">
                    </div>

                    <div class="form-group">
                        <label><i class="fas fa-angles-right"></i> Ölçek X/Y</label>
                        <div class="form-row">
                            <label>X:</label>
                            <input type="number" id="scaleX" value="1" step="0.05" min="0.1" max="5" aria-label="Ölçek X">
                            <label>Y:</label>
                            <input type="number" id="scaleY" value="1" step="0.05" min="0.1" max="5" aria-label="Ölçek Y">
                        </div>
                    </div>

                    <div class="form-group">
                        <label><i class="fas fa-shrimp"></i> Eğme (Skew)</label>
                        <div class="form-row">
                            <label>X:</label>
                            <input type="number" id="skewX" value="0" aria-label="Yatay eğme">
                            <label>Y:</label>
                            <input type="number" id="skewY" value="0" aria-label="Dikey eğme">
                        </div>
                    </div>

                    <div class="form-group">
                        <label><i class="fas fa-up-down-left-right"></i> Taşıma (Translate)</label>
                        <div class="form-row">
                            <label>X:</label>
                            <input type="number" id="translateX" value="0" aria-label="Yatay taşıma">
                            <label>Y:</label>
                            <input type="number" id="translateY" value="0" aria-label="Dikey taşıma">
                        </div>
                    </div>

                    <!-- 3D Transforms — YENİ -->
                    <div class="separator"></div>
                    <div class="form-group">
                        <label>
                            <i class="fas fa-cube"></i> 3D Dönüşümler
                            <span class="badge-new">Yeni</span>
                        </label>
                        <div class="form-row">
                            <label>RotX:</label>
                            <input type="number" id="rotateX" value="0" aria-label="X ekseni rotasyon">
                            <label>RotY:</label>
                            <input type="number" id="rotateY" value="0" aria-label="Y ekseni rotasyon">
                        </div>
                        <div class="form-row">
                            <label>RotZ:</label>
                            <input type="number" id="rotateZ" value="0" aria-label="Z ekseni rotasyon">
                            <label>Persp:</label>
                            <input type="number" id="perspective" value="0" min="0" max="2000" aria-label="Perspektif">
                        </div>
                    </div>

                    <!-- Transform Origin -->
                    <div class="form-group">
                        <label><i class="fas fa-crosshairs"></i> Transform Merkezi</label>
                        <div class="transform-origin-grid" id="transformOriginGrid" aria-label="Transform merkez noktası">
                            <button class="origin-btn" data-origin="top left">↖</button>
                            <button class="origin-btn" data-origin="top center">↑</button>
                            <button class="origin-btn" data-origin="top right">↗</button>
                            <button class="origin-btn" data-origin="center left">←</button>
                            <button class="origin-btn active" data-origin="center center">⊕</button>
                            <button class="origin-btn" data-origin="center right">→</button>
                            <button class="origin-btn" data-origin="bottom left">↙</button>
                            <button class="origin-btn" data-origin="bottom center">↓</button>
                            <button class="origin-btn" data-origin="bottom right">↘</button>
                        </div>
                    </div>
                </div>
            </div>

            <!-- ─────────────────────────────────
                 PANEL 5: KUTU GÖLGESİ PRO
            ───────────────────────────────── -->
            <div class="panel" data-panel="shadow">
                <div class="panel-header" role="button" tabindex="0" aria-expanded="false">
                    <div class="panel-icon shadow"><i class="fas fa-clone" aria-hidden="true"></i></div>
                    <span class="panel-title">Kutu Gölgesi Pro</span>
                    <i class="fas fa-chevron-up panel-toggle" aria-hidden="true"></i>
                </div>
                <div class="panel-body">
                    <div class="btn-grid">
                        <button class="style-btn" data-style-target="random-box-shadow"><i class="fas fa-clone"></i> Rnd Gölge</button>
                        <button class="style-btn" data-style-target="random-box-shadow-color"><i class="fas fa-palette"></i> Rnd Renk</button>
                        <button class="style-btn" data-style-target="random-multi-shadow"><i class="fas fa-layer-group"></i> Rnd Çoklu</button>
                        <button class="style-btn" data-style-target="random-inset-shadow"><i class="fas fa-compress-alt"></i> Rnd İç</button>
                        <!-- YENİ -->
                        <button class="style-btn" data-style-target="random-neon-glow"><i class="fas fa-lightbulb"></i> Neon Glow</button>
                        <button class="style-btn" data-style-target="random-long-shadow"><i class="fas fa-align-left"></i> Uzun Gölge</button>
                    </div>

                    <div class="separator"></div>

                    <!-- Shadow Layers — YENİ: Çoklu Katman -->
                    <div class="form-group">
                        <label>
                            <i class="fas fa-layer-group"></i> Gölge Katmanları
                            <button class="inline-btn" id="addBoxShadowLayer" data-tooltip="Yeni gölge katmanı ekle">
                                <i class="fas fa-plus"></i>
                            </button>
                        </label>
                        <div id="boxShadowLayers" class="shadow-layers-container">
                            <!-- JS ile doldurulacak -->
                        </div>
                    </div>
                </div>
            </div>

            <!-- ─────────────────────────────────
                 PANEL 6: ANİMASYON PRO
            ───────────────────────────────── -->
            <div class="panel" data-panel="animation">
                <div class="panel-header" role="button" tabindex="0" aria-expanded="false">
                    <div class="panel-icon anim"><i class="fas fa-play" aria-hidden="true"></i></div>
                    <span class="panel-title">Animasyon Pro</span>
                    <span class="panel-badge">30+</span>
                    <i class="fas fa-chevron-up panel-toggle" aria-hidden="true"></i>
                </div>
                <div class="panel-body">
                    <div class="btn-grid">
                        <button class="style-btn" data-style-target="random-animation"><i class="fas fa-random"></i> Rnd Anim</button>
                        <button class="style-btn" data-style-target="random-timing-function"><i class="fas fa-clock"></i> Rnd Timing</button>
                        <button class="style-btn" data-style-target="random-iteration-count"><i class="fas fa-redo"></i> Rnd Tekrar</button>
                        <button class="style-btn" data-style-target="stop-animation"><i class="fas fa-stop"></i> Durdur</button>
                        <!-- YENİ -->
                        <button class="style-btn" data-style-target="pause-animation"><i class="fas fa-pause"></i> Beklet</button>
                        <button class="style-btn" data-style-target="play-animation"><i class="fas fa-play"></i> Oynat</button>
                    </div>

                    <div class="separator"></div>

                    <!-- Animation Categories -->
                    <div class="form-group">
                        <label><i class="fas fa-list"></i> Animasyon Kategorisi</label>
                        <div class="sub-tabs" role="tablist">
                            <button class="sub-tab active" data-sub-tab="anim-basic" role="tab">Temel</button>
                            <button class="sub-tab" data-sub-tab="anim-attention" role="tab">Dikkat</button>
                            <button class="sub-tab" data-sub-tab="anim-3d" role="tab">3D</button>
                            <button class="sub-tab" data-sub-tab="anim-special" role="tab">Özel</button>
                        </div>

                        <div class="sub-tab-content active" id="anim-basic">
                            <div class="animation-grid" role="group" aria-label="Temel animasyonlar">
                                <button class="anim-btn" data-anim="bounce">🏀 Bounce</button>
                                <button class="anim-btn" data-anim="pulse">💓 Pulse</button>
                                <button class="anim-btn" data-anim="fadeIn">👁 Fade In</button>
                                <button class="anim-btn" data-anim="fadeOut">🌫 Fade Out</button>
                                <button class="anim-btn" data-anim="slideInLeft">⬅ Slide L</button>
                                <button class="anim-btn" data-anim="slideInRight">➡ Slide R</button>
                                <button class="anim-btn" data-anim="slideInUp">⬆ Slide Up</button>
                                <button class="anim-btn" data-anim="slideInDown">⬇ Slide Down</button>
                            </div>
                        </div>

                        <div class="sub-tab-content" id="anim-attention">
                            <div class="animation-grid" role="group" aria-label="Dikkat animasyonları">
                                <button class="anim-btn" data-anim="shake">😤 Shake</button>
                                <button class="anim-btn" data-anim="swing">🎪 Swing</button>
                                <button class="anim-btn" data-anim="rubberBand">🎸 Rubber</button>
                                <button class="anim-btn" data-anim="jello">🍮 Jello</button>
                                <button class="anim-btn" data-anim="heartBeat">❤️ HeartBeat</button>
                                <button class="anim-btn" data-anim="wobble">🌊 Wobble</button>
                                <button class="anim-btn" data-anim="tada">🎉 Tada</button>
                                <button class="anim-btn" data-anim="headShake">🙅 HeadShake</button>
                            </div>
                        </div>

                        <div class="sub-tab-content" id="anim-3d">
                            <div class="animation-grid" role="group" aria-label="3D animasyonlar">
                                <button class="anim-btn" data-anim="flip">🪃 Flip</button>
                                <button class="anim-btn" data-anim="flipInX">↔ Flip X</button>
                                <button class="anim-btn" data-anim="flipInY">↕ Flip Y</button>
                                <button class="anim-btn" data-anim="rotateIn">🔄 Rotate In</button>
                                <button class="anim-btn" data-anim="zoomIn">🔍 Zoom In</button>
                                <button class="anim-btn" data-anim="zoomOut">🔎 Zoom Out</button>
                                <button class="anim-btn" data-anim="rollIn">🎳 Roll In</button>
                                <button class="anim-btn" data-anim="lightSpeedIn">⚡ Light Speed</button>
                            </div>
                        </div>

                        <div class="sub-tab-content" id="anim-special">
                            <div class="animation-grid" role="group" aria-label="Özel animasyonlar">
                                <button class="anim-btn" data-anim="float">🎈 Float</button>
                                <button class="anim-btn" data-anim="glitch">📺 Glitch</button>
                                <button class="anim-btn" data-anim="neonPulse">💡 Neon</button>
                                <button class="anim-btn" data-anim="typewriter">⌨️ Typewriter</button>
                                <button class="anim-btn" data-anim="colorWave">🌈 Color Wave</button>
                                <button class="anim-btn" data-anim="morphShape">🔮 Morph</button>
                                <button class="anim-btn" data-anim="liquidWave">💧 Liquid</button>
                                <button class="anim-btn" data-anim="matrix">🖥 Matrix</button>
                                <button class="anim-btn" data-anim="fire">🔥 Fire</button>
                                <button class="anim-btn" data-anim="electric">⚡ Electric</button>
                            </div>
                        </div>
                    </div>

                    <!-- Duration -->
                    <div class="form-group">
                        <label>
                            <i class="fas fa-stopwatch"></i> Süre
                            <span class="value-badge" id="animDurationVal">1s</span>
                        </label>
                        <input type="range" id="animationDurationRange" min="0.1" max="10" step="0.1" value="1" aria-label="Animasyon süresi">
                    </div>

                    <!-- Delay — YENİ -->
                    <div class="form-group">
                        <label>
                            <i class="fas fa-hourglass-start"></i> Gecikme
                            <span class="value-badge" id="animDelayVal">0s</span>
                        </label>
                        <input type="range" id="animationDelayRange" min="0" max="5" step="0.1" value="0" aria-label="Animasyon gecikmesi">
                    </div>

                    <!-- Timing Function -->
                    <div class="form-group">
                        <label><i class="fas fa-bezier-curve"></i> Zamanlama Fonksiyonu</label>
                        <div class="form-row">
                            <select id="animationTimingFunction" data-style-prop="animationTimingFunction" aria-label="Zamanlama fonksiyonu">
                                <option value="ease" selected>Ease</option>
                                <option value="linear">Linear</option>
                                <option value="ease-in">Ease-In</option>
                                <option value="ease-out">Ease-Out</option>
                                <option value="ease-in-out">Ease-In-Out</option>
                                <option value="cubic-bezier(0.68,-0.55,0.265,1.55)">Bounce</option>
                                <option value="cubic-bezier(0.25,0.46,0.45,0.94)">Soft</option>
                                <option value="cubic-bezier(0.34,1.56,0.64,1)">Spring</option>
                                <option value="steps(10)">Steps(10)</option>
                                <option value="steps(20)">Steps(20)</option>
                                <option value="custom">Özel Bezier...</option>
                            </select>
                            <button class="inline-btn" id="openBezierEditor" data-tooltip="Bezier Editörü Aç" aria-label="Cubic Bezier Editörü Aç">
                                <i class="fas fa-bezier-curve"></i>
                            </button>
                        </div>
                    </div>

                    <!-- Iteration -->
                    <div class="form-group">
                        <label><i class="fas fa-repeat"></i> Tekrar Sayısı</label>
                        <select id="animationIterationCount" aria-label="Animasyon tekrar sayısı">
                            <option value="1" selected>1</option>
                            <option value="2">2</option>
                            <option value="3">3</option>
                            <option value="5">5</option>
                            <option value="10">10</option>
                            <option value="infinite">Sonsuz ∞</option>
                        </select>
                    </div>

                    <!-- Direction & Fill Mode — YENİ -->
                    <div class="form-group">
                        <label><i class="fas fa-arrows-left-right-to-line"></i> Yön & Dolgu Modu</label>
                        <div class="form-row">
                            <select id="animationDirection" data-style-prop="animationDirection" aria-label="Animasyon yönü">
                                <option value="normal" selected>Normal</option>
                                <option value="reverse">Ters</option>
                                <option value="alternate">Alternatif</option>
                                <option value="alternate-reverse">Alt. Ters</option>
                            </select>
                            <select id="animationFillMode" data-style-prop="animationFillMode" aria-label="Dolgu modu">
                                <option value="none" selected>Yok</option>
                                <option value="forwards">İleri</option>
                                <option value="backwards">Geri</option>
                                <option value="both">İkisi</option>
                            </select>
                        </div>
                    </div>

                    <!-- Play State — YENİ -->
                    <div class="form-group">
                        <label><i class="fas fa-circle-play"></i> Oynatma Durumu</label>
                        <div class="toggle-group" role="group" aria-label="Animasyon oynatma durumu">
                            <button class="toggle-btn active" data-play="running" aria-pressed="true">
                                <i class="fas fa-play"></i> Oynat
                            </button>
                            <button class="toggle-btn" data-play="paused" aria-pressed="false">
                                <i class="fas fa-pause"></i> Beklet
                            </button>
                        </div>
                    </div>

                    <!-- Transition -->
                    <div class="separator"></div>
                    <div class="form-group">
                        <label><i class="fas fa-arrows-left-right"></i> Geçiş (Transition)</label>
                        <div class="form-row">
                            <select id="transitionProperty" aria-label="Geçiş özelliği">
                                <option value="all" selected>Tümü</option>
                                <option value="transform">Transform</option>
                                <option value="opacity">Opaklık</option>
                                <option value="background-color">Arka Plan</option>
                                <option value="color">Renk</option>
                                <option value="box-shadow">Gölge</option>
                                <option value="border-radius">Köşe</option>
                                <option value="filter">Filtre</option>
                            </select>
                            <input type="number" id="transitionDuration" value="0.3" min="0" step="0.1" style="width:60px;" aria-label="Geçiş süresi">
                            <span class="unit-label">s</span>
                        </div>
                        <div class="form-row">
                            <select id="transitionTimingFunction" aria-label="Geçiş zamanlama fonksiyonu">
                                <option value="ease" selected>Ease</option>
                                <option value="linear">Linear</option>
                                <option value="ease-in">Ease-In</option>
                                <option value="ease-out">Ease-Out</option>
                                <option value="ease-in-out">Ease-In-Out</option>
                                <option value="cubic-bezier(0.34,1.56,0.64,1)">Spring</option>
                            </select>
                            <input type="number" id="transitionDelay" value="0" min="0" step="0.1" style="width:60px;" aria-label="Geçiş gecikmesi">
                            <span class="unit-label">s</span>
                        </div>
                    </div>

                    <!-- Custom Keyframes -->
                    <div class="form-group">
                        <label><i class="fas fa-code"></i> Özel Keyframes</label>
                        <textarea id="animationKeyframes" placeholder="@keyframes myAnim {&#10;  0% { opacity: 0; }&#10;  100% { opacity: 1; }&#10;}" aria-label="Özel keyframes kodu"></textarea>
                        <button class="add-color-btn" id="applyKeyframesBtn">
                            <i class="fas fa-play"></i> Keyframes Uygula
                        </button>
                    </div>
                </div>
            </div>

            <!-- ─────────────────────────────────
                 PANEL 7: CLIP PATH & ŞEKILLER
            ───────────────────────────────── -->
            <div class="panel" data-panel="clip">
                <div class="panel-header" role="button" tabindex="0" aria-expanded="false">
                    <div class="panel-icon clip"><i class="fas fa-cut" aria-hidden="true"></i></div>
                    <span class="panel-title">Clip-Path & Şekiller</span>
                    <i class="fas fa-chevron-up panel-toggle" aria-hidden="true"></i>
                </div>
                <div class="panel-body">
                    <div class="btn-grid">
                        <button class="style-btn" data-style-target="random-clip-path"><i class="fas fa-cut"></i> Rnd Kırma</button>
                        <button class="style-btn" data-style-target="reset-clip"><i class="fas fa-undo"></i> Sıfırla</button>
                    </div>

                    <div class="separator"></div>

                    <!-- Shape Gallery — YENİ: Görsel Galeri -->
                    <div class="form-group">
                        <label><i class="fas fa-shapes"></i> Şekil Galerisi</label>
                        <div class="clip-shape-gallery" id="clipShapeGallery" aria-label="Clip-path şekil galerisi">
                            <!-- JS ile doldurulacak -->
                        </div>
                    </div>

                    <!-- Custom Clip -->
                    <div class="form-group">
                        <label><i class="fas fa-pen"></i> Özel Clip-Path</label>
                        <input type="text" id="clipPath" data-style-prop="clipPath" placeholder="polygon(50% 0%, ...)" aria-label="Özel clip-path değeri">
                    </div>
                </div>
            </div>

            <!-- ─────────────────────────────────
                 PANEL 8: TRANSPARAN / GRADYAN YAZI
            ───────────────────────────────── -->
            <div class="panel" data-panel="transparent">
                <div class="panel-header" role="button" tabindex="0" aria-expanded="false">
                    <div class="panel-icon transparent"><i class="fas fa-eye-dropper" aria-hidden="true"></i></div>
                    <span class="panel-title">Transparan & Gradyan Yazı</span>
                    <i class="fas fa-chevron-up panel-toggle" aria-hidden="true"></i>
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
                        <label>
                            <i class="fas fa-circle-half-stroke"></i> Opaklık
                            <span class="value-badge" id="textOpacityVal">1</span>
                        </label>
                        <input type="range" id="textOpacityRange" min="0" max="1" step="0.05" value="1" aria-label="Yazı opaklığı">
                    </div>

                    <div class="form-group">
                        <label><i class="fas fa-gradient"></i> Metin Gradyanı</label>
                        <div class="form-row">
                            <label>Açı:</label>
                            <input type="number" id="textGradientAngle" value="90" min="0" max="360" aria-label="Metin gradyan açısı">
                            <label>Tür:</label>
                            <select id="textGradientType" aria-label="Metin gradyan türü">
                                <option value="linear" selected>Doğrusal</option>
                                <option value="radial">Radyal</option>
                                <option value="conic">Konik</option>
                            </select>
                        </div>
                        <div id="textGradientColors" class="gradient-colors"></div>
                        <button class="add-color-btn" id="addTextGradientColor">
                            <i class="fas fa-plus"></i> Renk Ekle
                        </button>
                    </div>

                    <div class="form-group">
                        <label><i class="fas fa-image"></i> Resim Dolgusu URL</label>
                        <input type="text" id="textImageFill" placeholder="https://..." aria-label="Metin resim dolgusu URL">
                    </div>

                    <div class="form-group">
                        <label><i class="fas fa-blender"></i> Mix Blend Modu</label>
                        <select id="mixBlendMode" data-style-prop="mixBlendMode" aria-label="Mix blend modu">
                            <option value="normal" selected>Normal</option>
                            <option value="multiply">Çarpma</option>
                            <option value="screen">Ekran</option>
                            <option value="overlay">Kaplama</option>
                            <option value="difference">Fark</option>
                            <option value="exclusion">Dışlama</option>
                            <option value="color-dodge">Renk Etkisi</option>
                            <option value="color-burn">Renk Yakma</option>
                            <option value="hard-light">Sert Işık</option>
                            <option value="soft-light">Yumuşak Işık</option>
                            <option value="hue">Ton</option>
                            <option value="saturation">Doygunluk</option>
                            <option value="luminosity">Parlaklık</option>
                        </select>
                    </div>
                </div>
            </div>

            <!-- ─────────────────────────────────
                 PANEL 9: RENK PALETİ
            ───────────────────────────────── -->
            <div class="panel" data-panel="palette">
                <div class="panel-header" role="button" tabindex="0" aria-expanded="false">
                    <div class="panel-icon palette"><i class="fas fa-swatchbook" aria-hidden="true"></i></div>
                    <span class="panel-title">Renk Paleti Oluşturucu</span>
                    <i class="fas fa-chevron-up panel-toggle" aria-hidden="true"></i>
                </div>
                <div class="panel-body">
                    <div class="btn-grid">
                        <button class="style-btn" data-style-target="generate-palette"><i class="fas fa-swatchbook"></i> Oluştur</button>
                        <button class="style-btn" data-style-target="random-palette"><i class="fas fa-dice"></i> Rnd Palet</button>
                        <!-- YENİ -->
                        <button class="style-btn" data-style-target="export-palette"><i class="fas fa-download"></i> Dışa Aktar</button>
                        <button class="style-btn" data-style-target="copy-palette-css"><i class="fas fa-copy"></i> CSS Kopyala</button>
                    </div>

                    <div class="separator"></div>

                    <div class="form-group">
                        <label><i class="fas fa-droplet"></i> Temel Renk</label>
                        <div id="baseColorPicker" class="color-picker-container" aria-label="Palet temel rengi"></div>
                    </div>

                    <div class="form-group">
                        <label><i class="fas fa-circle-nodes"></i> Palet Tipi</label>
                        <select id="paletteType" aria-label="Palet tipi">
                            <option value="monochromatic">Monokromatik</option>
                            <option value="analogous">Analog</option>
                            <option value="complementary">Tamamlayıcı</option>
                            <option value="triadic">Triadik</option>
                            <option value="split-complementary">Bölünmüş Tamam.</option>
                            <option value="tetradic">Tetradik</option>
                            <option value="shades">Tonal Skalası</option>
                            <option value="pastel">Pastel</option>
                        </select>
                    </div>

                    <div class="form-group">
                        <label><i class="fas fa-list-ol"></i> Renk Sayısı</label>
                        <input type="number" id="paletteSize" value="5" min="2" max="12" aria-label="Palet renk sayısı">
                    </div>

                    <div class="form-group">
                        <label><i class="fas fa-eye"></i> Palet Önizleme</label>
                        <div id="palettePreview" class="palette-preview" aria-label="Palet önizleme"></div>
                    </div>

                    <!-- Gradient from Palette — YENİ -->
                    <button class="add-color-btn" id="paletteToGradient" style="width:100%;margin-top:4px;">
                        <i class="fas fa-arrows-left-right-to-line"></i> Gradyana Dönüştür
                    </button>
                </div>
            </div>

            <!-- ─────────────────────────────────
                 PANEL 10: FİLTRE & EFEKTLER
            ───────────────────────────────── -->
            <div class="panel" data-panel="effects">
                <div class="panel-header" role="button" tabindex="0" aria-expanded="false">
                    <div class="panel-icon effects"><i class="fas fa-magic" aria-hidden="true"></i></div>
                    <span class="panel-title">Filtre & Efektler Pro</span>
                    <i class="fas fa-chevron-up panel-toggle" aria-hidden="true"></i>
                </div>
                <div class="panel-body">
                    <div class="btn-grid">
                        <button class="style-btn" data-style-target="random-filter"><i class="fas fa-filter"></i> Rnd Filtre</button>
                        <button class="style-btn" data-style-target="random-cursor"><i class="fas fa-mouse-pointer"></i> Rnd İmleç</button>
                        <button class="style-btn" data-style-target="random-effect"><i class="fas fa-star"></i> Rnd Efekt</button>
                        <button class="style-btn" data-style-target="reset-filters"><i class="fas fa-undo"></i> Sıfırla</button>
                        <!-- YENİ -->
                        <button class="style-btn" data-style-target="filter-vintage"><i class="fas fa-camera-retro"></i> Vintage</button>
                        <button class="style-btn" data-style-target="filter-cold"><i class="fas fa-snowflake"></i> Soğuk</button>
                        <button class="style-btn" data-style-target="filter-warm"><i class="fas fa-sun"></i> Sıcak</button>
                        <button class="style-btn" data-style-target="filter-dramatic"><i class="fas fa-theater-masks"></i> Dramatik</button>
                    </div>

                    <div class="separator"></div>

                    <!-- Filter Sliders -->
                    <div class="form-group">
                        <label><i class="fas fa-circle-dot"></i> Bulanıklık <span class="value-badge" id="blurVal">0px</span></label>
                        <input type="range" id="filterBlurRange" min="0" max="30" value="0" aria-label="Bulanıklık">
                    </div>

                    <div class="form-group">
                        <label><i class="fas fa-sun"></i> Parlaklık <span class="value-badge" id="brightnessVal">100%</span></label>
                        <input type="range" id="filterBrightnessRange" min="0" max="300" value="100" aria-label="Parlaklık">
                    </div>

                    <div class="form-group">
                        <label><i class="fas fa-circle-half-stroke"></i> Kontrast <span class="value-badge" id="contrastVal">100%</span></label>
                        <input type="range" id="filterContrastRange" min="0" max="300" value="100" aria-label="Kontrast">
                    </div>

                    <div class="form-group">
                        <label><i class="fas fa-droplet"></i> Doygunluk <span class="value-badge" id="saturateVal">100%</span></label>
                        <input type="range" id="filterSaturateRange" min="0" max="300" value="100" aria-label="Doygunluk">
                    </div>

                    <div class="form-group">
                        <label><i class="fas fa-rotate"></i> Ton Döndürme <span class="value-badge" id="hueRotateVal">0°</span></label>
                        <input type="range" id="filterHueRotateRange" min="0" max="360" value="0" aria-label="Ton döndürme">
                    </div>

                    <div class="form-group">
                        <label><i class="fas fa-circle-xmark"></i> Ters Çevir <span class="value-badge" id="invertVal">0%</span></label>
                        <input type="range" id="filterInvertRange" min="0" max="100" value="0" aria-label="Ters çevir">
                    </div>

                    <div class="form-group">
                        <label><i class="fas fa-mug-hot"></i> Sepya <span class="value-badge" id="sepiaVal">0%</span></label>
                        <input type="range" id="filterSepiaRange" min="0" max="100" value="0" aria-label="Sepya">
                    </div>

                    <div class="form-group">
                        <label><i class="fas fa-circle"></i> Gri Tonlama <span class="value-badge" id="grayscaleVal">0%</span></label>
                        <input type="range" id="filterGrayscaleRange" min="0" max="100" value="0" aria-label="Gri tonlama">
                    </div>

                    <!-- Drop Shadow Filter — YENİ -->
                    <div class="form-group">
                        <label>
                            <i class="fas fa-cloud-sun"></i> Drop-Shadow Filtresi
                            <span class="badge-new">Yeni</span>
                        </label>
                        <div class="form-row">
                            <label>X:</label><input type="number" id="dropShadowX" value="0" aria-label="Drop shadow X">
                            <label>Y:</label><input type="number" id="dropShadowY" value="0" aria-label="Drop shadow Y">
                            <label>B:</label><input type="number" id="dropShadowBlur" value="0" min="0" aria-label="Drop shadow blur">
                        </div>
                        <div id="dropShadowColorPicker" class="color-picker-container" aria-label="Drop shadow rengi"></div>
                    </div>

                    <!-- Backdrop Filter -->
                    <div class="form-group">
                        <label><i class="fas fa-layer-group"></i> Backdrop Blur <span class="value-badge" id="backdropBlurVal">0px</span></label>
                        <input type="range" id="backdropBlurRange" min="0" max="30" value="0" aria-label="Backdrop blur">
                    </div>

                    <!-- Cursor -->
                    <div class="form-group">
                        <label><i class="fas fa-mouse-pointer"></i> İmleç Stili</label>
                        <select id="cursor" data-style-prop="cursor" aria-label="İmleç stili">
                            <option value="auto" selected>Otomatik</option>
                            <option value="default">Varsayılan</option>
                            <option value="pointer">İşaretçi</option>
                            <option value="crosshair">Artı</option>
                            <option value="move">Taşı</option>
                            <option value="text">Metin</option>
                            <option value="not-allowed">Yasak</option>
                            <option value="grab">Yakala</option>
                            <option value="grabbing">Yakalanıyor</option>
                            <option value="zoom-in">Yakınlaştır</option>
                            <option value="zoom-out">Uzaklaştır</option>
                            <option value="wait">Bekle</option>
                            <option value="help">Yardım</option>
                            <option value="progress">İlerleme</option>
                            <option value="cell">Hücre</option>
                            <option value="col-resize">Sütun Yeniden Boyutlandır</option>
                            <option value="row-resize">Satır Yeniden Boyutlandır</option>
                            <option value="none">Gizle</option>
                        </select>
                    </div>
                </div>
            </div>

            <!-- ─────────────────────────────────
                 PANEL 11: BOYUT & DÜZEN PRO
            ───────────────────────────────── -->
            <div class="panel" data-panel="layout">
                <div class="panel-header" role="button" tabindex="0" aria-expanded="false">
                    <div class="panel-icon layout"><i class="fas fa-th-large" aria-hidden="true"></i></div>
                    <span class="panel-title">Boyut & Düzen Pro</span>
                    <i class="fas fa-chevron-up panel-toggle" aria-hidden="true"></i>
                </div>
                <div class="panel-body">
                    <!-- Box Model Visual — YENİ -->
                    <div class="box-model-visual" id="boxModelVisual" aria-label="Box model görsel editörü">
                        <div class="bm-margin-label">Margin</div>
                        <div class="bm-margin">
                            <input type="number" id="marginTop" value="0" placeholder="0" data-bm="marginTop" aria-label="Üst margin">
                            <div class="bm-padding-label">Padding</div>
                            <div class="bm-inner-row">
                                <input type="number" id="marginLeft" value="0" placeholder="0" data-bm="marginLeft" aria-label="Sol margin">
                                <div class="bm-content">
                                    <span>W</span>
                                    <i class="fas fa-times"></i>
                                    <span>H</span>
                                </div>
                                <input type="number" id="marginRight" value="0" placeholder="0" data-bm="marginRight" aria-label="Sağ margin">
                            </div>
                            <input type="number" id="marginBottom" value="0" placeholder="0" data-bm="marginBottom" aria-label="Alt margin">
                        </div>
                        <div class="bm-unit-row">
                            <select id="marginUnit" aria-label="Margin birimi">
                                <option value="px" selected>px</option>
                                <option value="%">%</option>
                                <option value="rem">rem</option>
                                <option value="em">em</option>
                                <option value="auto">auto</option>
                            </select>
                        </div>
                    </div>

                    <div class="separator"></div>

                    <!-- Size -->
                    <div class="form-group">
                        <label><i class="fas fa-arrows-alt-h"></i> Genişlik</label>
                        <div class="form-row">
                            <input type="text" id="boxWidth" placeholder="auto" data-style-prop="width" aria-label="Genişlik değeri">
                            <select id="widthUnit" style="width:60px;" aria-label="Genişlik birimi">
                                <option value="px">px</option>
                                <option value="%">%</option>
                                <option value="vw">vw</option>
                                <option value="rem">rem</option>
                                <option value="em">em</option>
                                <option value="ch">ch</option>
                            </select>
                        </div>
                    </div>

                    <div class="form-group">
                        <label><i class="fas fa-arrows-alt-v"></i> Yükseklik</label>
                        <div class="form-row">
                            <input type="text" id="boxHeight" placeholder="auto" data-style-prop="height" aria-label="Yükseklik değeri">
                            <select id="heightUnit" style="width:60px;" aria-label="Yükseklik birimi">
                                <option value="px">px</option>
                                <option value="%">%</option>
                                <option value="vh">vh</option>
                                <option value="rem">rem</option>
                                <option value="em">em</option>
                            </select>
                        </div>
                    </div>

                    <!-- Min/Max -->
                    <div class="form-group">
                        <label><i class="fas fa-ruler-horizontal"></i> Min / Max Genişlik</label>
                        <div class="form-row">
                            <label>Min:</label><input type="text" id="minWidth" placeholder="auto" data-style-prop="minWidth" aria-label="Min genişlik">
                            <label>Max:</label><input type="text" id="maxWidth" placeholder="auto" data-style-prop="maxWidth" aria-label="Max genişlik">
                        </div>
                    </div>

                    <div class="form-group">
                        <label><i class="fas fa-ruler-vertical"></i> Min / Max Yükseklik</label>
                        <div class="form-row">
                            <label>Min:</label><input type="text" id="minHeight" placeholder="auto" data-style-prop="minHeight" aria-label="Min yükseklik">
                            <label>Max:</label><input type="text" id="maxHeight" placeholder="auto" data-style-prop="maxHeight" aria-label="Max yükseklik">
                        </div>
                    </div>

                    <!-- Display & Overflow -->
                    <div class="form-group">
                        <label><i class="fas fa-table-cells"></i> Display & Overflow</label>
                        <div class="form-row">
                            <select id="display" data-style-prop="display" aria-label="Display türü">
                                <option value="flex" selected>Flex</option>
                                <option value="block">Block</option>
                                <option value="inline-block">Inline Block</option>
                                <option value="inline-flex">Inline Flex</option>
                                <option value="grid">Grid</option>
                                <option value="inline-grid">Inline Grid</option>
                                <option value="none">None (Gizle)</option>
                            </select>
                            <select id="overflow" data-style-prop="overflow" aria-label="Taşma davranışı">
                                <option value="hidden" selected>Gizle</option>
                                <option value="visible">Göster</option>
                                <option value="scroll">Kaydır</option>
                                <option value="auto">Otomatik</option>
                                <option value="clip">Kes</option>
                            </select>
                        </div>
                    </div>

                    <!-- Flex Controls -->
                    <div class="form-group" id="flexControls">
                        <label><i class="fas fa-arrows-to-dot"></i> Flexbox</label>
                        <div class="form-row">
                            <select id="flexDirection" data-style-prop="flexDirection" aria-label="Flex yönü">
                                <option value="row">Satır →</option>
                                <option value="column">Sütun ↓</option>
                                <option value="row-reverse">Satır Ters ←</option>
                                <option value="column-reverse">Sütun Ters ↑</option>
                            </select>
                            <select id="flexWrap" data-style-prop="flexWrap" aria-label="Flex sarmalama">
                                <option value="nowrap">Sarma</option>
                                <option value="wrap">Sarmal</option>
                                <option value="wrap-reverse">Ters Sarmal</option>
                            </select>
                        </div>
                        <div class="form-row">
                            <select id="justifyContent" data-style-prop="justifyContent" aria-label="Yatay hizalama">
                                <option value="center" selected>Merkez</option>
                                <option value="flex-start">Başlangıç</option>
                                <option value="flex-end">Bitiş</option>
                                <option value="space-between">Arası</option>
                                <option value="space-around">Çevresi</option>
                                <option value="space-evenly">Eşit</option>
                            </select>
                            <select id="alignItems" data-style-prop="alignItems" aria-label="Dikey hizalama">
                                <option value="center" selected>Merkez</option>
                                <option value="flex-start">Başlangıç</option>
                                <option value="flex-end">Bitiş</option>
                                <option value="stretch">Esnet</option>
                                <option value="baseline">Taban</option>
                            </select>
                        </div>
                        <div class="form-row">
                            <label>Gap:</label>
                            <input type="text" id="gap" data-style-prop="gap" placeholder="0px" aria-label="Boşluk">
                        </div>
                    </div>

                    <!-- Grid Controls — YENİ -->
                    <div class="form-group" id="gridControls" style="display:none;">
                        <label>
                            <i class="fas fa-table"></i> Grid
                            <span class="badge-new">Yeni</span>
                        </label>
                        <div class="form-row">
                            <label>Sütun:</label>
                            <input type="text" id="gridTemplateColumns" data-style-prop="gridTemplateColumns" placeholder="1fr 1fr 1fr" aria-label="Grid sütun şablonu">
                        </div>
                        <div class="form-row">
                            <label>Satır:</label>
                            <input type="text" id="gridTemplateRows" data-style-prop="gridTemplateRows" placeholder="auto" aria-label="Grid satır şablonu">
                        </div>
                        <div class="form-row">
                            <label>Gap:</label>
                            <input type="text" id="gridGap" data-style-prop="gap" placeholder="10px" aria-label="Grid boşluk">
                        </div>
                    </div>

                    <!-- Position — YENİ -->
                    <div class="form-group">
                        <label><i class="fas fa-map-pin"></i> Konumlandırma</label>
                        <div class="form-row">
                            <select id="position" data-style-prop="position" aria-label="Konumlandırma türü">
                                <option value="static" selected>Static</option>
                                <option value="relative">Relative</option>
                                <option value="absolute">Absolute</option>
                                <option value="fixed">Fixed</option>
                                <option value="sticky">Sticky</option>
                            </select>
                            <select id="zIndex" data-style-prop="zIndex" aria-label="Z-index">
                                <option value="auto" selected>Auto</option>
                                <option value="-1">-1</option>
                                <option value="0">0</option>
                                <option value="1">1</option>
                                <option value="10">10</option>
                                <option value="100">100</option>
                                <option value="999">999</option>
                            </select>
                        </div>
                    </div>
                </div>
            </div>

            <!-- ─────────────────────────────────
                 PANEL 12: PSEUDO ELEMENTS — YENİ
            ───────────────────────────────── -->
            <div class="panel" data-panel="pseudo">
                <div class="panel-header" role="button" tabindex="0" aria-expanded="false">
                    <div class="panel-icon effects" style="background:var(--accent-blue-dim);color:var(--accent-blue)"><i class="fas fa-code" aria-hidden="true"></i></div>
                    <span class="panel-title">::Before / ::After</span>
                    <span class="badge-new" style="margin-left:6px;">Yeni</span>
                    <i class="fas fa-chevron-up panel-toggle" aria-hidden="true"></i>
                </div>
                <div class="panel-body">
                    <div class="sub-tabs" role="tablist">
                        <button class="sub-tab active" data-sub-tab="pseudo-before" role="tab">::before</button>
                        <button class="sub-tab" data-sub-tab="pseudo-after" role="tab">::after</button>
                    </div>

                    <div class="sub-tab-content active" id="pseudo-before">
                        <div class="form-group">
                            <label><i class="fas fa-quote-left"></i> İçerik (content)</label>
                            <input type="text" id="beforeContent" placeholder="'✨'" aria-label="::before içeriği">
                        </div>
                        <div class="form-group">
                            <label><i class="fas fa-location-dot"></i> Konumlandırma</label>
                            <div class="form-row">
                                <label>Üst:</label><input type="text" id="beforeTop" placeholder="auto" aria-label="::before top">
                                <label>Sol:</label><input type="text" id="beforeLeft" placeholder="auto" aria-label="::before left">
                            </div>
                        </div>
                        <div class="form-group">
                            <label><i class="fas fa-droplet"></i> Renk</label>
                            <input type="text" id="beforeColor" placeholder="#ffffff" aria-label="::before renk">
                        </div>
                        <div class="form-group">
                            <label><i class="fas fa-text-height"></i> Boyut</label>
                            <input type="text" id="beforeFontSize" placeholder="1em" aria-label="::before yazı boyutu">
                        </div>
                    </div>

                    <div class="sub-tab-content" id="pseudo-after">
                        <div class="form-group">
                            <label><i class="fas fa-quote-right"></i> İçerik (content)</label>
                            <input type="text" id="afterContent" placeholder="'🎨'" aria-label="::after içeriği">
                        </div>
                        <div class="form-group">
                            <label><i class="fas fa-location-dot"></i> Konumlandırma</label>
                            <div class="form-row">
                                <label>Üst:</label><input type="text" id="afterTop" placeholder="auto" aria-label="::after top">
                                <label>Sağ:</label><input type="text" id="afterRight" placeholder="auto" aria-label="::after right">
                            </div>
                        </div>
                        <div class="form-group">
                            <label><i class="fas fa-droplet"></i> Renk</label>
                            <input type="text" id="afterColor" placeholder="#ffffff" aria-label="::after renk">
                        </div>
                        <div class="form-group">
                            <label><i class="fas fa-text-height"></i> Boyut</label>
                            <input type="text" id="afterFontSize" placeholder="1em" aria-label="::after yazı boyutu">
                        </div>
                    </div>

                    <button class="add-color-btn" id="applyPseudoBtn" style="width:100%;margin-top:8px;">
                        <i class="fas fa-check"></i> Pseudo Element Uygula
                    </button>
                </div>
            </div>

            <!-- ─────────────────────────────────
                 PANEL 13: HAZIR TEMALAR V2
            ───────────────────────────────── -->
            <div class="panel" data-panel="presets">
                <div class="panel-header" role="button" tabindex="0" aria-expanded="false">
                    <div class="panel-icon presets"><i class="fas fa-palette" aria-hidden="true"></i></div>
                    <span class="panel-title">Hazır Temalar V2</span>
                    <span class="panel-badge">20</span>
                    <i class="fas fa-chevron-up panel-toggle" aria-hidden="true"></i>
                </div>
                <div class="panel-body">
                    <!-- Theme Search -->
                    <div class="sidebar-search" style="margin-bottom:8px;">
                        <i class="fas fa-search"></i>
                        <input type="text" id="themeSearch" placeholder="Tema ara..." aria-label="Tema ara">
                    </div>

                    <div class="preset-cards" id="themePresetCards">
                        <!-- Row 1: Dark Themes -->
                        <button class="preset-card" data-style-target="auto-theme-neon" data-theme-color="#0ff,#0a0a2e">
                            <i class="fas fa-lightbulb"></i> Neon
                        </button>
                        <button class="preset-card" data-style-target="auto-theme-cyberpunk" data-theme-color="#ff2d6a,#0d0221">
                            <i class="fas fa-robot"></i> Cyberpunk
                        </button>
                        <button class="preset-card" data-style-target="auto-theme-dark-elegant" data-theme-color="#d4af37,#1a1a2e">
                            <i class="fas fa-gem"></i> Zarif Karanlık
                        </button>
                        <button class="preset-card" data-style-target="auto-theme-matrix" data-theme-color="#00ff41,#0d0208">
                            <i class="fas fa-terminal"></i> Matrix
                        </button>
                        <!-- Row 2: Light Themes -->
                        <button class="preset-card" data-style-target="auto-theme-minimal" data-theme-color="#333,#fafafa">
                            <i class="fas fa-compress"></i> Minimal
                        </button>
                        <button class="preset-card" data-style-target="auto-theme-vintage" data-theme-color="#5c3317,#f4e9d8">
                            <i class="fas fa-camera-retro"></i> Vintage
                        </button>
                        <button class="preset-card" data-style-target="auto-theme-pastel" data-theme-color="#c9a0dc,#fff0f5">
                            <i class="fas fa-cloud"></i> Pastel
                        </button>
                        <button class="preset-card" data-style-target="auto-theme-paper" data-theme-color="#444,#f5f0e8">
                            <i class="fas fa-scroll"></i> Kağıt
                        </button>
                        <!-- Row 3: Glass & Special -->
                        <button class="preset-card" data-style-target="auto-theme-glassmorphism" data-theme-color="#fff,rgba(255,255,255,0.1)">
                            <i class="fas fa-glass-whiskey"></i> Glass
                        </button>
                        <button class="preset-card" data-style-target="auto-theme-neumorphism" data-theme-color="#6b7b99,#e0e5ec">
                            <i class="fas fa-circle"></i> Neumorphism
                        </button>
                        <button class="preset-card" data-style-target="auto-theme-aurora" data-theme-color="#a8ff78,#141e30">
                            <i class="fas fa-sun"></i> Aurora
                        </button>
                        <button class="preset-card" data-style-target="auto-theme-holographic" data-theme-color="#ff6ec7,#1a1a2e">
                            <i class="fas fa-compact-disc"></i> Holografik
                        </button>
                        <!-- Row 4: Nature & Ambient -->
                        <button class="preset-card" data-style-target="auto-theme-nature" data-theme-color="#2d5016,#e8f5e9">
                            <i class="fas fa-leaf"></i> Doğa
                        </button>
                        <button class="preset-card" data-style-target="auto-theme-ocean" data-theme-color="#fff,#0077b6">
                            <i class="fas fa-water"></i> Okyanus
                        </button>
                        <button class="preset-card" data-style-target="auto-theme-sunset" data-theme-color="#fff,linear-gradient">
                            <i class="fas fa-sun"></i> Gün Batımı
                        </button>
                        <button class="preset-card" data-style-target="auto-theme-forest" data-theme-color="#1a3a1a,#2d5a2d">
                            <i class="fas fa-tree"></i> Orman
                        </button>
                        <!-- Row 5: Pop & Creative -->
                        <button class="preset-card" data-style-target="auto-theme-candy" data-theme-color="#ff6b9d,#fff0f5">
                            <i class="fas fa-candy-cane"></i> Şeker
                        </button>
                        <button class="preset-card" data-style-target="auto-theme-retrowave" data-theme-color="#ff71ce,#030014">
                            <i class="fas fa-wave-square"></i> RetroWave
                        </button>
                        <button class="preset-card" data-style-target="auto-theme-brutalist" data-theme-color="#000,#ff0">
                            <i class="fas fa-hammer"></i> Brutalist
                        </button>
                        <button class="preset-card" data-style-target="auto-theme-lofi" data-theme-color="#d4a5a5,#f5f0e8">
                            <i class="fas fa-headphones"></i> Lo-Fi
                        </button>
                    </div>
                </div>
            </div>

            <!-- ─────────────────────────────────
                 PANEL 14: KAOS MOTORU V2
            ───────────────────────────────── -->
            <div class="panel" data-panel="chaos">
                <div class="panel-header" role="button" tabindex="0" aria-expanded="false">
                    <div class="panel-icon chaos"><i class="fas fa-explosion" aria-hidden="true"></i></div>
                    <span class="panel-title">Kaos Motoru V2</span>
                    <i class="fas fa-chevron-up panel-toggle" aria-hidden="true"></i>
                </div>
                <div class="panel-body">
                    <div class="btn-grid">
                        <button class="style-btn chaos-btn" data-style-target="auto-generate" style="grid-column:1/-1;padding:14px;font-size:11.5px;">
                            <i class="fas fa-wand-magic-sparkles"></i> Otomatik Stil Oluştur
                        </button>
                        <button class="style-btn chaos-btn" data-style-target="max-chaos" style="grid-column:1/-1;padding:14px;font-size:11.5px;background:linear-gradient(135deg,rgba(248,113,113,0.15),rgba(167,139,250,0.15),rgba(251,191,36,0.1))">
                            <i class="fas fa-explosion"></i> MAKSİMUM KAOS!
                        </button>
                    </div>

                    <div class="separator"></div>

                    <!-- Chaos Level — YENİ -->
                    <div class="form-group">
                        <label>
                            <i class="fas fa-gauge-high"></i> Kaos Seviyesi
                            <span class="value-badge" id="chaosLevelVal">5</span>
                        </label>
                        <input type="range" id="chaosLevel" min="1" max="10" value="5" aria-label="Kaos seviyesi">
                    </div>

                    <!-- Category Checkboxes -->
                    <div class="form-group">
                        <label><i class="fas fa-list-check"></i> Kaos Kategorileri</label>
                        <div class="checkbox-row">
                            <label><input type="checkbox" id="chaosFont" checked aria-label="Yazı kaos"> <i class="fas fa-font"></i> Yazı</label>
                            <label><input type="checkbox" id="chaosBackground" checked aria-label="Arka plan kaos"> <i class="fas fa-fill"></i> Arka Plan</label>
                            <label><input type="checkbox" id="chaosBorder" checked aria-label="Çerçeve kaos"> <i class="fas fa-border-all"></i> Çerçeve</label>
                        </div>
                        <div class="checkbox-row">
                            <label><input type="checkbox" id="chaosEffects" checked aria-label="Efekt kaos"> <i class="fas fa-filter"></i> Efektler</label>
                            <label><input type="checkbox" id="chaosAnimation" checked aria-label="Animasyon kaos"> <i class="fas fa-play"></i> Animasyon</label>
                            <label><input type="checkbox" id="chaosClip" checked aria-label="Clip kaos"> <i class="fas fa-cut"></i> Kırma</label>
                        </div>
                        <div class="checkbox-row">
                            <label><input type="checkbox" id="chaosTransform" checked aria-label="Dönüşüm kaos"> <i class="fas fa-cube"></i> Dönüşüm</label>
                            <label><input type="checkbox" id="chaosBoxShadow" checked aria-label="Gölge kaos"> <i class="fas fa-clone"></i> Gölge</label>
                            <label><input type="checkbox" id="chaosTextGradient" checked aria-label="Gradyan kaos"> <i class="fas fa-grip-lines"></i> Gradyan</label>
                        </div>
                        <div class="checkbox-row">
                            <label><input type="checkbox" id="chaosTextImage" checked aria-label="Resim dolgu kaos"> <i class="fas fa-image"></i> Resim</label>
                            <label><input type="checkbox" id="chaosOpacity" checked aria-label="Opaklık kaos"> <i class="fas fa-adjust"></i> Opaklık</label>
                            <label><input type="checkbox" id="chaosLayout" checked aria-label="Düzen kaos"> <i class="fas fa-th-large"></i> Düzen</label>
                        </div>

                        <!-- Quick select buttons -->
                        <div class="form-row" style="margin-top:6px;gap:4px;">
                            <button class="output-btn secondary" id="selectAllChaos" style="flex:1;padding:6px;">
                                <i class="fas fa-check-double"></i> Tümünü Seç
                            </button>
                            <button class="output-btn secondary" id="deselectAllChaos" style="flex:1;padding:6px;">
                                <i class="fas fa-times"></i> Temizle
                            </button>
                        </div>
                    </div>

                    <!-- Auto-play Mode — YENİ -->
                    <div class="form-group">
                        <label>
                            <i class="fas fa-rotate"></i> Otomatik Kaos Modu
                            <span class="badge-new">Yeni</span>
                        </label>
                        <div class="form-row">
                            <button class="output-btn secondary" id="startAutoPlay" style="flex:1;">
                                <i class="fas fa-play"></i> Başlat
                            </button>
                            <button class="output-btn secondary" id="stopAutoPlay" style="flex:1;" disabled>
                                <i class="fas fa-stop"></i> Durdur
                            </button>
                            <input type="number" id="autoPlayInterval" value="3" min="1" max="30" style="width:50px;" aria-label="Otomatik kaos aralığı (saniye)">
                            <span class="unit-label">s</span>
                        </div>
                    </div>
                </div>
            </div>

        </aside>

        <!-- ══════════════════════════════════════
             MAIN CONTENT
        ══════════════════════════════════════ -->
        <main class="main-content" role="main">

            <!-- ─────────────────────────────────
                 PREVIEW SECTION
            ───────────────────────────────── -->
            <div class="preview-wrapper">
                <!-- Preview Header -->
                <div class="preview-header">
                    <h2 class="preview-title">
                        <i class="fas fa-eye" aria-hidden="true"></i>
                        Canlı Önizleme
                    </h2>
                    <div class="preview-controls">
                        <!-- Ruler Toggle — YENİ -->
                        <button class="preview-control-btn" data-action="toggle-ruler" data-tooltip="Cetvel" aria-label="Cetveli Aç/Kapat" aria-pressed="false">
                            <i class="fas fa-ruler"></i>
                        </button>
                        <!-- Grid Toggle — YENİ -->
                        <button class="preview-control-btn" data-action="toggle-grid" data-tooltip="Grid" aria-label="Grid Aç/Kapat" aria-pressed="false">
                            <i class="fas fa-border-all"></i>
                        </button>
                        <!-- Dark Preview Background -->
                        <button class="preview-control-btn" data-action="toggle-preview-bg" data-tooltip="Önizleme Arkaplanı" aria-label="Önizleme arkaplanı değiştir">
                            <i class="fas fa-circle-half-stroke"></i>
                        </button>
                        <span class="preview-dimensions" id="previewDimensions" aria-live="polite">-- × --</span>
                    </div>
                </div>

                <!-- Preview Container -->
                <div class="preview-container" id="previewContainer">
                    <!-- Ruler — YENİ -->
                    <div class="ruler ruler-h" id="rulerH" aria-hidden="true" style="display:none;"></div>
                    <div class="ruler ruler-v" id="rulerV" aria-hidden="true" style="display:none;"></div>

                    <!-- Preview Box -->
                    <div class="preview-frame" id="previewFrame" data-size="desktop">
                        <div id="preview-box" role="img" aria-label="Stil önizleme alanı">K3N4N V7.0</div>
                    </div>
                </div>

                <!-- Preview Text Input -->
                <div class="preview-text-input">
                    <div class="preview-input-wrapper">
                        <i class="fas fa-pencil" aria-hidden="true"></i>
                        <input
                            type="text"
                            id="customText"
                            placeholder="Önizleme metnini değiştir..."
                            maxlength="200"
                            aria-label="Önizleme metni"
                            value="K3N4N V7.0"
                        >
                        <span class="char-count" id="charCount" aria-live="polite">9/200</span>
                    </div>
                    <button class="preview-control-btn" data-action="randomize-text" data-tooltip="Rastgele Metin">
                        <i class="fas fa-dice"></i>
                    </button>
                    <button class="preview-control-btn" data-action="clear-text" data-tooltip="Temizle">
                        <i class="fas fa-times"></i>
                    </button>
                </div>

                <!-- History Timeline — YENİ -->
                <div class="history-timeline" id="historyTimeline" aria-label="Stil geçmişi">
                    <div class="history-label"><i class="fas fa-clock-rotate-left"></i> Geçmiş</div>
                    <div class="history-items" id="historyItems"></div>
                </div>
            </div>

            <!-- ─────────────────────────────────
                 OUTPUT SECTION
            ───────────────────────────────── -->
            <div class="output-card">
                <!-- Output Tabs -->
                <div class="output-tabs" role="tablist">
                    <button class="output-tab active" data-tab="css-tab" role="tab" aria-selected="true">
                        <i class="fab fa-css3-alt"></i> CSS
                    </button>
                    <button class="output-tab" data-tab="html-tab" role="tab" aria-selected="false">
                        <i class="fab fa-html5"></i> HTML
                    </button>
                    <button class="output-tab" data-tab="json-tab" role="tab" aria-selected="false">
                        <i class="fas fa-file-code"></i> JSON
                    </button>
                    <button class="output-tab" data-tab="tailwind-tab" role="tab" aria-selected="false">
                        <i class="fas fa-wind"></i> Tailwind
                    </button>
                    <button class="output-tab" data-tab="input-tab" role="tab" aria-selected="false">
                        <i class="fas fa-pen"></i> Özel CSS
                    </button>
                </div>

                <!-- CSS Tab -->
                <div class="tab-content active" id="css-tab" role="tabpanel">
                    <div class="output-card-body">
                        <div class="output-toolbar">
                            <div class="output-toolbar-left">
                                <span class="output-filename">
                                    <i class="fab fa-css3-alt"></i> styles.css
                                </span>
                                <span class="output-lines" id="cssLineCount" aria-live="polite">0 satır</span>
                            </div>
                            <div class="output-toolbar-right">
                                <button class="toolbar-btn" data-action="format-css" data-tooltip="Formatla">
                                    <i class="fas fa-align-left"></i>
                                </button>
                                <button class="toolbar-btn" data-action="minify-css" data-tooltip="Minify">
                                    <i class="fas fa-compress-alt"></i>
                                </button>
                            </div>
                        </div>
                        <textarea id="css-output" readonly aria-label="CSS çıktısı" spellcheck="false"></textarea>
                        <div class="output-actions">
                            <button class="output-btn primary" id="copy-css-btn">
                                <i class="fas fa-copy"></i> Kopyala
                            </button>
                            <button class="output-btn secondary" data-action="download-css">
                                <i class="fas fa-download"></i> CSS İndir
                            </button>
                            <button class="output-btn secondary" data-action="download-html">
                                <i class="fas fa-file-code"></i> HTML İndir
                            </button>
                            <button class="output-btn tertiary" data-action="export-styles">
                                <i class="fas fa-file-export"></i> Dışa Aktar
                            </button>
                            <button class="output-btn tertiary" data-action="import-styles">
                                <i class="fas fa-file-import"></i> İçe Aktar
                            </button>
                            <input type="file" id="import-styles" accept=".json" aria-label="Stil dosyası içe aktar">
                        </div>
                        <!-- Status Messages -->
                        <div class="msg success" id="copy-success" role="alert">
                            <i class="fas fa-check-circle"></i> CSS panoya kopyalandı!
                        </div>
                        <div class="msg error" id="copy-error" role="alert">
                            <i class="fas fa-exclamation-circle"></i> Kopyalama başarısız.
                        </div>
                    </div>
                </div>

                <!-- HTML Tab -->
                <div class="tab-content" id="html-tab" role="tabpanel">
                    <div class="output-card-body">
                        <div class="output-toolbar">
                            <span class="output-filename"><i class="fab fa-html5"></i> preview.html</span>
                        </div>
                        <div id="htmlPreviewArea" class="code-display" aria-label="HTML önizleme kodu"></div>
                        <div class="output-actions">
                            <button class="output-btn primary" id="copy-html-btn">
                                <i class="fas fa-copy"></i> HTML Kopyala
                            </button>
                        </div>
                    </div>
                </div>

                <!-- JSON Tab — YENİ -->
                <div class="tab-content" id="json-tab" role="tabpanel">
                    <div class="output-card-body">
                        <div class="output-toolbar">
                            <span class="output-filename"><i class="fas fa-file-code"></i> styles.json</span>
                        </div>
                        <textarea id="json-output" readonly aria-label="JSON çıktısı" spellcheck="false"></textarea>
                        <div class="output-actions">
                            <button class="output-btn primary" id="copy-json-btn">
                                <i class="fas fa-copy"></i> JSON Kopyala
                            </button>
                            <button class="output-btn secondary" data-action="download-json">
                                <i class="fas fa-download"></i> JSON İndir
                            </button>
                        </div>
                    </div>
                </div>

                <!-- Tailwind Tab — YENİ -->
                <div class="tab-content" id="tailwind-tab" role="tabpanel">
                    <div class="output-card-body">
                        <div class="output-toolbar">
                            <span class="output-filename"><i class="fas fa-wind"></i> Tailwind Eşdeğerleri</span>
                            <span class="output-note">⚠️ Yaklaşık karşılıklar</span>
                        </div>
                        <div id="tailwindOutput" class="code-display" aria-label="Tailwind CSS çıktısı"></div>
                        <div class="output-actions">
                            <button class="output-btn primary" id="copy-tailwind-btn">
                                <i class="fas fa-copy"></i> Tailwind Kopyala
                            </button>
                        </div>
                    </div>
                </div>

                <!-- Custom CSS Input Tab -->
                <div class="tab-content" id="input-tab" role="tabpanel">
                    <div class="output-card-body">
                        <div class="output-toolbar">
                            <span class="output-filename"><i class="fas fa-pen"></i> Özel CSS Editörü</span>
                        </div>
                        <textarea
                            id="cssInputArea"
                            placeholder="/* Özel CSS kodunuzu buraya yazın */&#10;font-size: 48px;&#10;color: #ff6b9d;&#10;background: linear-gradient(...);"
                            aria-label="Özel CSS girişi"
                            spellcheck="false"
                        ></textarea>
                        <div class="output-actions">
                            <button class="output-btn primary" id="applyCustomCss">
                                <i class="fas fa-check"></i> CSS Uygula
                            </button>
                            <button class="output-btn secondary" id="clearCustomCss">
                                <i class="fas fa-trash"></i> Temizle
                            </button>
                            <button class="output-btn tertiary" id="parseAndApply">
                                <i class="fas fa-magic"></i> Ayrıştır & Uygula
                            </button>
                        </div>
                        <div class="msg success" id="css-success" role="alert">
                            <i class="fas fa-check-circle"></i> CSS başarıyla uygulandı!
                        </div>
                        <div class="msg error" id="css-error" role="alert">
                            <i class="fas fa-exclamation-circle"></i> Geçersiz CSS sözdizimi.
                        </div>
                    </div>
                </div>
            </div>

        </main>
    </div>

    <!-- ═══════════════════════════════════════════════════
         FOOTER
    ═══════════════════════════════════════════════════ -->
    <footer class="app-footer" role="contentinfo">
        <div class="footer-inner">
            <span class="footer-logo">
                <i class="fas fa-wand-magic-sparkles" aria-hidden="true"></i>
                K3N4N CSS Generator V7.0
            </span>
            <span class="footer-sep" aria-hidden="true">•</span>
            <span>2025 — Tüm hakları saklıdır</span>
            <span class="footer-sep" aria-hidden="true">•</span>
            <span class="footer-shortcuts-hint">
                <kbd>Ctrl</kbd>+<kbd>K</kbd> Komut Paleti
            </span>
        </div>
    </footer>

    <!-- Ana JavaScript -->
    <script src="script.js"></script>
</body>
</html> html koduma tam uyunlu tam tum fonksıyonların calsıtıgı js  kodunu yaz  istersen css kodunu da atabıılıırm 

### Concord Grape
*2026-03-06 20:06:55 +03*

<think>The user is asking me to write a complete JavaScript file that will work with their HTML code for a CSS Generator application. This is a very comprehensive HTML file with many features including:

1. Toast notifications
2. Command palette (Ctrl+K)
3. Shortcut modal
4. Fullscreen preview
5. Cubic Bezier editor
6. Multiple panels for styling:
   - Text styles (font, color, shadow, stroke, etc.)
   - Background (solid, gradient, image, pattern)
   - Border & corners
   - 3D Transform
   - Box shadow
   - Animations
   - Clip-path & shapes
   - Transparent & gradient text
   - Color palette generator
   - Filters & effects
   - Size & layout
   - Pseudo elements
   - Ready themes
   - Chaos engine

7. Preview section with rulers, grid, responsive sizes
8. Output tabs (CSS, HTML, JSON, Tailwind, Custom CSS)
9. Undo/Redo functionality
10. Theme toggle (dark/light)
11. Import/Export styles
12. History timeline

This is a massive project. I need to write a comprehensive JavaScript file that handles all these features. Let me structure this properly.

Given the complexity and the fact that I have limited space, I'll need to write a well-organized but comprehensive JS file. I'll focus on making all the core functionality work.

Let me start writing the JavaScript code:</think>Bu çok kapsamlı bir proje. Size tam çalışan bir JavaScript dosyası yazacağım. Kod çok uzun olacağı için parçalar halinde vereceğim.

```javascript
// ═══════════════════════════════════════════════════════════════════════════
// K3N4N CSS Generator V7.0 — Ultimate Pro
// Tam özellikli JavaScript kodu
// ═══════════════════════════════════════════════════════════════════════════

(function() {
    'use strict';

    // ═══════════════════════════════════════════════════════════════════════
    // GLOBAL STATE & CONFIG
    // ═══════════════════════════════════════════════════════════════════════
    
    const STATE = {
        history: [],
        historyIndex: -1,
        maxHistory: 50,
        currentStyles: {},
        colorPickers: {},
        autoPlayInterval: null,
        isPlaying: false,
        animationPaused: false,
        previewBgIndex: 0,
        rulerVisible: false,
        gridVisible: false,
        textShadowLayers: [],
        boxShadowLayers: [],
        gradientColors: [],
        textGradientColors: [],
        gradientBorderColors: [],
        customKeyframes: '',
        pseudoStyles: { before: {}, after: {} }
    };

    const CONFIG = {
        previewBackgrounds: [
            'var(--preview-bg)',
            '#1a1a2e',
            '#ffffff',
            'linear-gradient(135deg, #667eea 0%, #764ba2 100%)',
            'linear-gradient(45deg, #000 25%, transparent 25%, transparent 75%, #000 75%), linear-gradient(45deg, #000 25%, transparent 25%, transparent 75%, #000 75%)',
            '#0a0a0a'
        ],
        fonts: [
            "'Poppins', sans-serif", "'Inter', sans-serif", "'Space Grotesk', sans-serif",
            "'Orbitron', sans-serif", "'Bebas Neue', sans-serif", "'VT323', monospace",
            "'Press Start 2P', monospace", "'Lobster', cursive", "'Playfair Display', serif",
            "'Fira Code', monospace", "'JetBrains Mono', monospace", "'Monoton', cursive",
            "'Bungee', sans-serif", "'Cinzel', serif", "'Dancing Script', cursive"
        ],
        animations: {
            bounce: { name: 'bounce', keyframes: '@keyframes bounce{0%,20%,50%,80%,100%{transform:translateY(0)}40%{transform:translateY(-30px)}60%{transform:translateY(-15px)}}' },
            pulse: { name: 'pulse', keyframes: '@keyframes pulse{0%{transform:scale(1)}50%{transform:scale(1.1)}100%{transform:scale(1)}}' },
            fadeIn: { name: 'fadeIn', keyframes: '@keyframes fadeIn{from{opacity:0}to{opacity:1}}' },
            fadeOut: { name: 'fadeOut', keyframes: '@keyframes fadeOut{from{opacity:1}to{opacity:0}}' },
            slideInLeft: { name: 'slideInLeft', keyframes: '@keyframes slideInLeft{from{transform:translateX(-100%);opacity:0}to{transform:translateX(0);opacity:1}}' },
            slideInRight: { name: 'slideInRight', keyframes: '@keyframes slideInRight{from{transform:translateX(100%);opacity:0}to{transform:translateX(0);opacity:1}}' },
            slideInUp: { name: 'slideInUp', keyframes: '@keyframes slideInUp{from{transform:translateY(100%);opacity:0}to{transform:translateY(0);opacity:1}}' },
            slideInDown: { name: 'slideInDown', keyframes: '@keyframes slideInDown{from{transform:translateY(-100%);opacity:0}to{transform:translateY(0);opacity:1}}' },
            shake: { name: 'shake', keyframes: '@keyframes shake{0%,100%{transform:translateX(0)}10%,30%,50%,70%,90%{transform:translateX(-10px)}20%,40%,60%,80%{transform:translateX(10px)}}' },
            swing: { name: 'swing', keyframes: '@keyframes swing{20%{transform:rotate3d(0,0,1,15deg)}40%{transform:rotate3d(0,0,1,-10deg)}60%{transform:rotate3d(0,0,1,5deg)}80%{transform:rotate3d(0,0,1,-5deg)}100%{transform:rotate3d(0,0,1,0deg)}}' },
            rubberBand: { name: 'rubberBand', keyframes: '@keyframes rubberBand{0%{transform:scale3d(1,1,1)}30%{transform:scale3d(1.25,.75,1)}40%{transform:scale3d(.75,1.25,1)}50%{transform:scale3d(1.15,.85,1)}65%{transform:scale3d(.95,1.05,1)}75%{transform:scale3d(1.05,.95,1)}100%{transform:scale3d(1,1,1)}}' },
            jello: { name: 'jello', keyframes: '@keyframes jello{0%,11.1%,100%{transform:none}22.2%{transform:skewX(-12.5deg) skewY(-12.5deg)}33.3%{transform:skewX(6.25deg) skewY(6.25deg)}44.4%{transform:skewX(-3.125deg) skewY(-3.125deg)}55.5%{transform:skewX(1.5625deg) skewY(1.5625deg)}66.6%{transform:skewX(-.78125deg) skewY(-.78125deg)}77.7%{transform:skewX(.390625deg) skewY(.390625deg)}88.8%{transform:skewX(-.1953125deg) skewY(-.1953125deg)}}' },
            heartBeat: { name: 'heartBeat', keyframes: '@keyframes heartBeat{0%{transform:scale(1)}14%{transform:scale(1.3)}28%{transform:scale(1)}42%{transform:scale(1.3)}70%{transform:scale(1)}}' },
            wobble: { name: 'wobble', keyframes: '@keyframes wobble{0%{transform:none}15%{transform:translate3d(-25%,0,0) rotate3d(0,0,1,-5deg)}30%{transform:translate3d(20%,0,0) rotate3d(0,0,1,3deg)}45%{transform:translate3d(-15%,0,0) rotate3d(0,0,1,-3deg)}60%{transform:translate3d(10%,0,0) rotate3d(0,0,1,2deg)}75%{transform:translate3d(-5%,0,0) rotate3d(0,0,1,-1deg)}100%{transform:none}}' },
            tada: { name: 'tada', keyframes: '@keyframes tada{0%{transform:scale3d(1,1,1)}10%,20%{transform:scale3d(.9,.9,.9) rotate3d(0,0,1,-3deg)}30%,50%,70%,90%{transform:scale3d(1.1,1.1,1.1) rotate3d(0,0,1,3deg)}40%,60%,80%{transform:scale3d(1.1,1.1,1.1) rotate3d(0,0,1,-3deg)}100%{transform:scale3d(1,1,1)}}' },
            headShake: { name: 'headShake', keyframes: '@keyframes headShake{0%{transform:translateX(0)}6.5%{transform:translateX(-6px) rotateY(-9deg)}18.5%{transform:translateX(5px) rotateY(7deg)}31.5%{transform:translateX(-3px) rotateY(-5deg)}43.5%{transform:translateX(2px) rotateY(3deg)}50%{transform:translateX(0)}}' },
            flip: { name: 'flip', keyframes: '@keyframes flip{0%{transform:perspective(400px) rotateY(-1turn)}40%{transform:perspective(400px) translateZ(150px) rotateY(-190deg)}50%{transform:perspective(400px) translateZ(150px) rotateY(-170deg)}80%{transform:perspective(400px) scale3d(.95,.95,.95)}100%{transform:perspective(400px)}}' },
            flipInX: { name: 'flipInX', keyframes: '@keyframes flipInX{0%{transform:perspective(400px) rotateX(90deg);opacity:0}40%{transform:perspective(400px) rotateX(-20deg)}60%{transform:perspective(400px) rotateX(10deg);opacity:1}80%{transform:perspective(400px) rotateX(-5deg)}100%{transform:perspective(400px)}}' },
            flipInY: { name: 'flipInY', keyframes: '@keyframes flipInY{0%{transform:perspective(400px) rotateY(90deg);opacity:0}40%{transform:perspective(400px) rotateY(-20deg)}60%{transform:perspective(400px) rotateY(10deg);opacity:1}80%{transform:perspective(400px) rotateY(-5deg)}100%{transform:perspective(400px)}}' },
            rotateIn: { name: 'rotateIn', keyframes: '@keyframes rotateIn{0%{transform:rotate(-200deg);opacity:0}100%{transform:none;opacity:1}}' },
            zoomIn: { name: 'zoomIn', keyframes: '@keyframes zoomIn{0%{opacity:0;transform:scale3d(.3,.3,.3)}50%{opacity:1}}' },
            zoomOut: { name: 'zoomOut', keyframes: '@keyframes zoomOut{0%{opacity:1}50%{transform:scale3d(.3,.3,.3)}100%{opacity:0}}' },
            rollIn: { name: 'rollIn', keyframes: '@keyframes rollIn{0%{opacity:0;transform:translate3d(-100%,0,0) rotate3d(0,0,1,-120deg)}100%{opacity:1;transform:none}}' },
            lightSpeedIn: { name: 'lightSpeedIn', keyframes: '@keyframes lightSpeedIn{0%{transform:translate3d(100%,0,0) skewX(-30deg);opacity:0}60%{transform:skewX(20deg);opacity:1}80%{transform:skewX(-5deg)}100%{transform:none}}' },
            float: { name: 'float', keyframes: '@keyframes float{0%,100%{transform:translateY(0)}50%{transform:translateY(-20px)}}' },
            glitch: { name: 'glitch', keyframes: '@keyframes glitch{0%{transform:translate(0)}20%{transform:translate(-2px,2px)}40%{transform:translate(-2px,-2px)}60%{transform:translate(2px,2px)}80%{transform:translate(2px,-2px)}100%{transform:translate(0)}}' },
            neonPulse: { name: 'neonPulse', keyframes: '@keyframes neonPulse{0%,100%{text-shadow:0 0 5px currentColor,0 0 10px currentColor,0 0 20px currentColor}50%{text-shadow:0 0 10px currentColor,0 0 20px currentColor,0 0 40px currentColor,0 0 80px currentColor}}' },
            typewriter: { name: 'typewriter', keyframes: '@keyframes typewriter{from{width:0}to{width:100%}}' },
            colorWave: { name: 'colorWave', keyframes: '@keyframes colorWave{0%{filter:hue-rotate(0deg)}100%{filter:hue-rotate(360deg)}}' },
            morphShape: { name: 'morphShape', keyframes: '@keyframes morphShape{0%,100%{border-radius:60% 40% 30% 70%/60% 30% 70% 40%}50%{border-radius:30% 60% 70% 40%/50% 60% 30% 60%}}' },
            liquidWave: { name: 'liquidWave', keyframes: '@keyframes liquidWave{0%,100%{border-radius:30% 70% 70% 30%/30% 30% 70% 70%}50%{border-radius:70% 30% 30% 70%/70% 70% 30% 30%}}' },
            matrix: { name: 'matrix', keyframes: '@keyframes matrix{0%{text-shadow:0 0 0 #0f0}50%{text-shadow:0 0 20px #0f0,0 0 30px #0f0}100%{text-shadow:0 0 0 #0f0}}' },
            fire: { name: 'fire', keyframes: '@keyframes fire{0%,100%{text-shadow:0 -5px 10px #ff6600,0 -10px 20px #ff3300,0 -15px 30px #ff0000}50%{text-shadow:0 -10px 20px #ff6600,0 -20px 40px #ff3300,0 -30px 60px #ff0000}}' },
            electric: { name: 'electric', keyframes: '@keyframes electric{0%,100%{text-shadow:0 0 5px #fff,0 0 10px #fff,0 0 15px #0ff,0 0 20px #0ff}50%{text-shadow:0 0 10px #fff,0 0 20px #0ff,0 0 30px #0ff,0 0 40px #00f}}' }
        },
        clipPaths: [
            { name: 'Yok', value: 'none', preview: '' },
            { name: 'Daire', value: 'circle(50%)', preview: '●' },
            { name: 'Elips', value: 'ellipse(50% 30%)', preview: '⬭' },
            { name: 'Üçgen', value: 'polygon(50% 0%, 0% 100%, 100% 100%)', preview: '▲' },
            { name: 'Ters Üçgen', value: 'polygon(0% 0%, 100% 0%, 50% 100%)', preview: '▼' },
            { name: 'Paralelkenar', value: 'polygon(20% 0%, 100% 0%, 80% 100%, 0% 100%)', preview: '▱' },
            { name: 'Eşkenar Dörtgen', value: 'polygon(50% 0%, 100% 50%, 50% 100%, 0% 50%)', preview: '◆' },
            { name: 'Pentagon', value: 'polygon(50% 0%, 100% 38%, 82% 100%, 18% 100%, 0% 38%)', preview: '⬠' },
            { name: 'Hexagon', value: 'polygon(25% 0%, 75% 0%, 100% 50%, 75% 100%, 25% 100%, 0% 50%)', preview: '⬡' },
            { name: 'Yıldız', value: 'polygon(50% 0%, 61% 35%, 98% 35%, 68% 57%, 79% 91%, 50% 70%, 21% 91%, 32% 57%, 2% 35%, 39% 35%)', preview: '★' },
            { name: 'Ok Sağ', value: 'polygon(0% 20%, 60% 20%, 60% 0%, 100% 50%, 60% 100%, 60% 80%, 0% 80%)', preview: '➤' },
            { name: 'Çapraz', value: 'polygon(20% 0%, 0% 20%, 30% 50%, 0% 80%, 20% 100%, 50% 70%, 80% 100%, 100% 80%, 70% 50%, 100% 20%, 80% 0%, 50% 30%)', preview: '✖' },
            { name: 'Kalp', value: 'polygon(50% 15%, 60% 5%, 80% 0%, 100% 15%, 100% 35%, 85% 60%, 50% 100%, 15% 60%, 0% 35%, 0% 15%, 20% 0%, 40% 5%)', preview: '♥' },
            { name: 'Oval Sol', value: 'ellipse(30% 50% at 30% 50%)', preview: '◖' },
            { name: 'Inset', value: 'inset(10% 20% 10% 20% round 10px)', preview: '▢' }
        ],
        patterns: [
            { name: 'Izgara', css: 'linear-gradient(#333 1px, transparent 1px), linear-gradient(90deg, #333 1px, transparent 1px)', size: '20px 20px' },
            { name: 'Noktalar', css: 'radial-gradient(circle, #333 1px, transparent 1px)', size: '10px 10px' },
            { name: 'Çapraz Çizgi', css: 'repeating-linear-gradient(45deg, transparent, transparent 10px, rgba(255,255,255,.1) 10px, rgba(255,255,255,.1) 20px)', size: 'auto' },
            { name: 'Zigzag', css: 'linear-gradient(135deg, #333 25%, transparent 25%), linear-gradient(225deg, #333 25%, transparent 25%), linear-gradient(45deg, #333 25%, transparent 25%), linear-gradient(315deg, #333 25%, transparent 25%)', size: '20px 20px' },
            { name: 'Dalga', css: 'radial-gradient(ellipse at 50% 0%, transparent 70%, rgba(255,255,255,.1) 70%)', size: '40px 20px' },
            { name: 'Kareler', css: 'linear-gradient(45deg, #222 25%, transparent 25%), linear-gradient(-45deg, #222 25%, transparent 25%), linear-gradient(45deg, transparent 75%, #222 75%), linear-gradient(-45deg, transparent 75%, #222 75%)', size: '20px 20px' },
            { name: 'Bal Peteği', css: 'radial-gradient(circle farthest-side at 0% 50%, #333 23.5%, transparent 0) 21px 30px, radial-gradient(circle farthest-side at 0% 50%, #444 24%, transparent 0) 19px 30px', size: '42px 60px' },
            { name: 'Piramit', css: 'linear-gradient(315deg, transparent 75%, #333 75%), linear-gradient(45deg, transparent 75%, #333 75%), linear-gradient(135deg, #333 50%, transparent 50%), linear-gradient(45deg, #444 50%, #333 50%)', size: '20px 20px' }
        ],
        randomTexts: [
            'Hello World!', 'Merhaba Dünya!', 'CSS is Awesome', 'K3N4N V7.0',
            'Creative Design', 'Web Magic', 'Style Master', 'Pixel Perfect',
            'Code & Design', 'Future UI', 'Neon Dreams', 'Cyber Style'
        ]
    };

    // ═══════════════════════════════════════════════════════════════════════
    // DOM ELEMENTS CACHE
    // ═══════════════════════════════════════════════════════════════════════
    
    const DOM = {};

    function cacheDOM() {
        // Preview
        DOM.previewBox = document.getElementById('preview-box');
        DOM.previewFrame = document.getElementById('previewFrame');
        DOM.previewContainer = document.getElementById('previewContainer');
        DOM.customText = document.getElementById('customText');
        DOM.charCount = document.getElementById('charCount');
        DOM.previewDimensions = document.getElementById('previewDimensions');

        // Output
        DOM.cssOutput = document.getElementById('css-output');
        DOM.jsonOutput = document.getElementById('json-output');
        DOM.htmlPreviewArea = document.getElementById('htmlPreviewArea');
        DOM.tailwindOutput = document.getElementById('tailwindOutput');
        DOM.cssInputArea = document.getElementById('cssInputArea');
        DOM.cssLineCount = document.getElementById('cssLineCount');

        // Sidebar
        DOM.sidebar = document.getElementById('sidebar');
        DOM.sidebarToggle = document.getElementById('sidebarToggle');
        DOM.sidebarOverlay = document.getElementById('sidebarOverlay');
        DOM.panelSearch = document.getElementById('panelSearch');
        DOM.searchClear = document.getElementById('searchClear');

        // Modals
        DOM.commandPaletteOverlay = document.getElementById('commandPaletteOverlay');
        DOM.commandPalette = document.getElementById('commandPalette');
        DOM.commandPaletteInput = document.getElementById('commandPaletteInput');
        DOM.commandPaletteResults = document.getElementById('commandPaletteResults');
        DOM.shortcutModalOverlay = document.getElementById('shortcutModalOverlay');
        DOM.fullscreenPreviewOverlay = document.getElementById('fullscreenPreviewOverlay');
        DOM.fullscreenPreviewBox = document.getElementById('fullscreenPreviewBox');
        DOM.bezierModalOverlay = document.getElementById('bezierModalOverlay');
        DOM.bezierCanvas = document.getElementById('bezierCanvas');

        // Toast
        DOM.toastContainer = document.getElementById('toastContainer');

        // History
        DOM.undoCount = document.getElementById('undoCount');
        DOM.redoCount = document.getElementById('redoCount');
        DOM.historyItems = document.getElementById('historyItems');

        // Rulers
        DOM.rulerH = document.getElementById('rulerH');
        DOM.rulerV = document.getElementById('rulerV');

        // Shadow layers containers
        DOM.textShadowLayers = document.getElementById('textShadowLayers');
        DOM.boxShadowLayers = document.getElementById('boxShadowLayers');

        // Gradient containers
        DOM.gradientColors = document.getElementById('gradientColors');
        DOM.textGradientColors = document.getElementById('textGradientColors');
        DOM.gradientBorderColors = document.getElementById('gradientBorderColors');

        // Pattern & Clip galleries
        DOM.patternGallery = document.getElementById('patternGallery');
        DOM.clipShapeGallery = document.getElementById('clipShapeGallery');

        // Palette
        DOM.palettePreview = document.getElementById('palettePreview');

        // Gradient preview
        DOM.gradientPreviewBar = document.getElementById('gradientPreviewBar');
    }

    // ═══════════════════════════════════════════════════════════════════════
    // UTILITY FUNCTIONS
    // ═══════════════════════════════════════════════════════════════════════
    
    const Utils = {
        randomInt(min, max) {
            return Math.floor(Math.random() * (max - min + 1)) + min;
        },

        randomFloat(min, max, decimals = 2) {
            return parseFloat((Math.random() * (max - min) + min).toFixed(decimals));
        },

        randomFromArray(arr) {
            return arr[Math.floor(Math.random() * arr.length)];
        },

        randomColor() {
            return '#' + Math.floor(Math.random() * 16777215).toString(16).padStart(6, '0');
        },

        randomHSL(satMin = 50, satMax = 100, lightMin = 40, lightMax = 70) {
            const h = this.randomInt(0, 360);
            const s = this.randomInt(satMin, satMax);
            const l = this.randomInt(lightMin, lightMax);
            return `hsl(${h}, ${s}%, ${l}%)`;
        },

        hexToRgba(hex, alpha = 1) {
            const r = parseInt(hex.slice(1, 3), 16);
            const g = parseInt(hex.slice(3, 5), 16);
            const b = parseInt(hex.slice(5, 7), 16);
            return `rgba(${r}, ${g}, ${b}, ${alpha})`;
        },

        rgbaToHex(rgba) {
            const match = rgba.match(/rgba?\((\d+),\s*(\d+),\s*(\d+)/);
            if (!match) return '#000000';
            const r = parseInt(match[1]).toString(16).padStart(2, '0');
            const g = parseInt(match[2]).toString(16).padStart(2, '0');
            const b = parseInt(match[3]).toString(16).padStart(2, '0');
            return `#${r}${g}${b}`;
        },

        debounce(func, wait) {
            let timeout;
            return function executedFunction(...args) {
                const later = () => {
                    clearTimeout(timeout);
                    func(...args);
                };
                clearTimeout(timeout);
                timeout = setTimeout(later, wait);
            };
        },

        escapeHtml(text) {
            const div = document.createElement('div');
            div.textContent = text;
            return div.innerHTML;
        },

        copyToClipboard(text) {
            if (navigator.clipboard && navigator.clipboard.writeText) {
                return navigator.clipboard.writeText(text);
            }
            const textarea = document.createElement('textarea');
            textarea.value = text;
            textarea.style.position = 'fixed';
            textarea.style.opacity = '0';
            document.body.appendChild(textarea);
            textarea.select();
            document.execCommand('copy');
            document.body.removeChild(textarea);
            return Promise.resolve();
        },

        downloadFile(content, filename, type = 'text/css') {
            const blob = new Blob([content], { type });
            const url = URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            a.download = filename;
            a.click();
            URL.revokeObjectURL(url);
        },

        generateUniqueId() {
            return 'id_' + Math.random().toString(36).substr(2, 9);
        },

        camelToKebab(str) {
            return str.replace(/([a-z0-9])([A-Z])/g, '$1-$2').toLowerCase();
        },

        kebabToCamel(str) {
            return str.replace(/-([a-z])/g, (g) => g[1].toUpperCase());
        }
    };

    // ═══════════════════════════════════════════════════════════════════════
    // TOAST NOTIFICATIONS
    // ═══════════════════════════════════════════════════════════════════════
    
    const Toast = {
        show(message, type = 'info', duration = 3000) {
            const toast = document.createElement('div');
            toast.className = `toast toast-${type}`;
            
            const icons = {
                success: 'fa-check-circle',
                error: 'fa-exclamation-circle',
                warning: 'fa-exclamation-triangle',
                info: 'fa-info-circle'
            };
            
            toast.innerHTML = `
                <i class="fas ${icons[type] || icons.info}"></i>
                <span>${message}</span>
            `;
            
            DOM.toastContainer.appendChild(toast);
            
            requestAnimationFrame(() => {
                toast.classList.add('show');
            });
            
            setTimeout(() => {
                toast.classList.remove('show');
                setTimeout(() => toast.remove(), 300);
            }, duration);
        },

        success(msg) { this.show(msg, 'success'); },
        error(msg) { this.show(msg, 'error'); },
        warning(msg) { this.show(msg, 'warning'); },
        info(msg) { this.show(msg, 'info'); }
    };

    // ═══════════════════════════════════════════════════════════════════════
    // HISTORY MANAGEMENT (UNDO/REDO)
    // ═══════════════════════════════════════════════════════════════════════
    
    const History = {
        save() {
            const currentState = JSON.stringify(STATE.currentStyles);
            
            // Remove future states if we're not at the end
            if (STATE.historyIndex < STATE.history.length - 1) {
                STATE.history = STATE.history.slice(0, STATE.historyIndex + 1);
            }
            
            // Don't save duplicate states
            if (STATE.history[STATE.historyIndex] === currentState) return;
            
            STATE.history.push(currentState);
            
            // Limit history size
            if (STATE.history.length > STATE.maxHistory) {
                STATE.history.shift();
            } else {
                STATE.historyIndex++;
            }
            
            this.updateUI();
            this.updateTimeline();
        },

        undo() {
            if (STATE.historyIndex > 0) {
                STATE.historyIndex--;
                this.restore();
            }
        },

        redo() {
            if (STATE.historyIndex < STATE.history.length - 1) {
                STATE.historyIndex++;
                this.restore();
            }
        },

        restore() {
            if (STATE.history[STATE.historyIndex]) {
                const styles = JSON.parse(STATE.history[STATE.historyIndex]);
                STATE.currentStyles = styles;
                StyleManager.applyStyles(styles, false);
                this.updateUI();
            }
        },

        updateUI() {
            const undoBtn = document.querySelector('[data-action="undo"]');
            const redoBtn = document.querySelector('[data-action="redo"]');
            
            if (undoBtn) {
                undoBtn.disabled = STATE.historyIndex <= 0;
                DOM.undoCount.textContent = STATE.historyIndex;
            }
            if (redoBtn) {
                redoBtn.disabled = STATE.historyIndex >= STATE.history.length - 1;
                DOM.redoCount.textContent = Math.max(0, STATE.history.length - 1 - STATE.historyIndex);
            }
        },

        updateTimeline() {
            if (!DOM.historyItems) return;
            
            DOM.historyItems.innerHTML = '';
            
            const start = Math.max(0, STATE.history.length - 10);
            for (let i = start; i < STATE.history.length; i++) {
                const item = document.createElement('button');
                item.className = 'history-item' + (i === STATE.historyIndex ? ' active' : '');
                item.textContent = i + 1;
                item.title = `Durum ${i + 1}`;
                item.addEventListener('click', () => {
                    STATE.historyIndex = i;
                    this.restore();
                    this.updateTimeline();
                });
                DOM.historyItems.appendChild(item);
            }
        },

        clear() {
            STATE.history = [];
            STATE.historyIndex = -1;
            this.updateUI();
            this.updateTimeline();
        }
    };

    // ═══════════════════════════════════════════════════════════════════════
    // STYLE MANAGER
    // ═══════════════════════════════════════════════════════════════════════
    
    const StyleManager = {
        applyStyles(styles, saveHistory = true) {
            Object.assign(STATE.currentStyles, styles);
            
            for (const [prop, value] of Object.entries(styles)) {
                if (value !== undefined && value !== null && value !== '') {
                    DOM.previewBox.style[prop] = value;
                }
            }
            
            if (saveHistory) {
                History.save();
            }
            
            this.updateOutput();
        },

        applyStyle(prop, value, saveHistory = true) {
            this.applyStyles({ [prop]: value }, saveHistory);
        },

        removeStyle(prop) {
            delete STATE.currentStyles[prop];
            DOM.previewBox.style[prop] = '';
            this.updateOutput();
        },

        resetAll() {
            STATE.currentStyles = {};
            STATE.textShadowLayers = [];
            STATE.boxShadowLayers = [];
            STATE.gradientColors = [];
            STATE.textGradientColors = [];
            STATE.gradientBorderColors = [];
            STATE.customKeyframes = '';
            STATE.pseudoStyles = { before: {}, after: {} };
            
            DOM.previewBox.removeAttribute('style');
            DOM.previewBox.textContent = 'K3N4N V7.0';
            DOM.customText.value = 'K3N4N V7.0';
            
            // Reset form elements
            this.resetFormElements();
            
            // Re-initialize shadow layers
            ShadowLayers.initTextShadowLayers();
            ShadowLayers.initBoxShadowLayers();
            
            // Re-initialize gradient colors
            GradientManager.initGradientColors();
            GradientManager.initTextGradientColors();
            
            History.save();
            this.updateOutput();
            Toast.success('Tüm stiller sıfırlandı!');
        },

        resetFormElements() {
            // Font
            const fontFamily = document.getElementById('fontFamily');
            if (fontFamily) fontFamily.value = "'Poppins', sans-serif";
            
            const fontSize = document.getElementById('fontSize');
            const fontSizeRange = document.getElementById('fontSizeRange');
            if (fontSize) fontSize.value = 30;
            if (fontSizeRange) fontSizeRange.value = 30;
            
            const fontWeight = document.getElementById('fontWeight');
            const fontWeightRange = document.getElementById('fontWeightRange');
            if (fontWeight) fontWeight.value = '400';
            if (fontWeightRange) fontWeightRange.value = 400;
            
            // Reset sliders
            document.querySelectorAll('input[type="range"]').forEach(range => {
                const defaultVal = range.getAttribute('data-default') || range.min || 0;
                range.value = defaultVal;
            });
            
            // Reset number inputs
            document.querySelectorAll('input[type="number"]').forEach(input => {
                if (!input.id.includes('margin') && !input.id.includes('padding')) {
                    input.value = input.getAttribute('data-default') || 0;
                }
            });
            
            // Reset selects
            document.querySelectorAll('select').forEach(select => {
                select.selectedIndex = 0;
            });
            
            // Reset checkboxes
            document.querySelectorAll('input[type="checkbox"]').forEach(cb => {
                if (cb.id.includes('chaos') || cb.id.includes('Linked')) {
                    cb.checked = true;
                } else {
                    cb.checked = false;
                }
            });
        },

        updateOutput() {
            this.updateCSSOutput();
            this.updateHTMLOutput();
            this.updateJSONOutput();
            this.updateTailwindOutput();
            this.updatePreviewDimensions();
        },

        updateCSSOutput() {
            let css = '.my-element {\n';
            
            for (const [prop, value] of Object.entries(STATE.currentStyles)) {
                if (value !== undefined && value !== null && value !== '') {
                    const kebabProp = Utils.camelToKebab(prop);
                    css += `    ${kebabProp}: ${value};\n`;
                }
            }
            
            css += '}';
            
            // Add keyframes if any
            if (STATE.customKeyframes) {
                css += '\n\n' + STATE.customKeyframes;
            }
            
            // Add pseudo elements if any
            if (STATE.pseudoStyles.before.content) {
                css += '\n\n.my-element::before {\n';
                for (const [prop, value] of Object.entries(STATE.pseudoStyles.before)) {
                    if (value) css += `    ${Utils.camelToKebab(prop)}: ${value};\n`;
                }
                css += '}';
            }
            
            if (STATE.pseudoStyles.after.content) {
                css += '\n\n.my-element::after {\n';
                for (const [prop, value] of Object.entries(STATE.pseudoStyles.after)) {
                    if (value) css += `    ${Utils.camelToKebab(prop)}: ${value};\n`;
                }
                css += '}';
            }
            
            DOM.cssOutput.value = css;
            
            // Update line count
            const lineCount = css.split('\n').length;
            DOM.cssLineCount.textContent = `${lineCount} satır`;
        },

        updateHTMLOutput() {
            const text = DOM.previewBox.textContent || 'K3N4N V7.0';
            const styles = DOM.previewBox.getAttribute('style') || '';
            
            let html = `<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>K3N4N CSS Generator Export</title>
    <style>
        body {
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            background: #1a1a2e;
            margin: 0;
        }
        .my-element {
            ${styles.split(';').filter(s => s.trim()).map(s => s.trim() + ';').join('\n            ')}
        }
    </style>
</head>
<body>
    <div class="my-element">${Utils.escapeHtml(text)}</div>
</body>
</html>`;
            
            DOM.htmlPreviewArea.innerHTML = `<pre><code>${Utils.escapeHtml(html)}</code></pre>`;
        },

        updateJSONOutput() {
            const json = JSON.stringify(STATE.currentStyles, null, 2);
            DOM.jsonOutput.value = json;
        },

        updateTailwindOutput() {
            const tailwindClasses = [];
            const styles = STATE.currentStyles;
            
            // Font size mapping
            if (styles.fontSize) {
                const size = parseInt(styles.fontSize);
                if (size <= 12) tailwindClasses.push('text-xs');
                else if (size <= 14) tailwindClasses.push('text-sm');
                else if (size <= 16) tailwindClasses.push('text-base');
                else if (size <= 18) tailwindClasses.push('text-lg');
                else if (size <= 20) tailwindClasses.push('text-xl');
                else if (size <= 24) tailwindClasses.push('text-2xl');
                else if (size <= 30) tailwindClasses.push('text-3xl');
                else if (size <= 36) tailwindClasses.push('text-4xl');
                else if (size <= 48) tailwindClasses.push('text-5xl');
                else if (size <= 60) tailwindClasses.push('text-6xl');
                else tailwindClasses.push('text-7xl');
            }
            
            // Font weight
            if (styles.fontWeight) {
                const weights = { 100: 'thin', 200: 'extralight', 300: 'light', 400: 'normal', 500: 'medium', 600: 'semibold', 700: 'bold', 800: 'extrabold', 900: 'black' };
                tailwindClasses.push(`font-${weights[styles.fontWeight] || 'normal'}`);
            }
            
            // Text align
            if (styles.textAlign) {
                tailwindClasses.push(`text-${styles.textAlign}`);
            }
            
            // Border radius
            if (styles.borderRadius) {
                const r = parseInt(styles.borderRadius);
                if (r === 0) tailwindClasses.push('rounded-none');
                else if (r <= 4) tailwindClasses.push('rounded-sm');
                else if (r <= 8) tailwindClasses.push('rounded');
                else if (r <= 12) tailwindClasses.push('rounded-md');
                else if (r <= 16) tailwindClasses.push('rounded-lg');
                else if (r <= 24) tailwindClasses.push('rounded-xl');
                else if (r <= 32) tailwindClasses.push('rounded-2xl');
                else if (r <= 48) tailwindClasses.push('rounded-3xl');
                else tailwindClasses.push('rounded-full');
            }
            
            // Display
            if (styles.display) {
                const displayMap = { flex: 'flex', grid: 'grid', block: 'block', 'inline-block': 'inline-block', 'inline-flex': 'inline-flex', none: 'hidden' };
                if (displayMap[styles.display]) tailwindClasses.push(displayMap[styles.display]);
            }
            
            const output = tailwindClasses.length > 0 
                ? `class="${tailwindClasses.join(' ')}"` 
                : '/* Tailwind eşdeğerleri bulunamadı */';
            
            DOM.tailwindOutput.innerHTML = `<pre><code>${output}</code></pre>`;
        },

        updatePreviewDimensions() {
            if (DOM.previewBox) {
                const rect = DOM.previewBox.getBoundingClientRect();
                DOM.previewDimensions.textContent = `${Math.round(rect.width)} × ${Math.round(rect.height)}`;
            }
        }
    };

    // ═══════════════════════════════════════════════════════════════════════
    // COLOR PICKER MANAGER
    // ═══════════════════════════════════════════════════════════════════════
    
    const ColorPickerManager = {
        init() {
            this.createPicker('textColorPicker', '#222222', (color) => {
                StyleManager.applyStyle('color', color.hexString);
                document.getElementById('textColorHex').value = color.hexString;
                document.getElementById('textColorSwatch').style.background = color.hexString;
            });
            
            this.createPicker('backgroundColorPicker', '#ffffff', (color) => {
                StyleManager.applyStyle('backgroundColor', color.hexString);
                document.getElementById('bgColorHex').value = color.hexString;
                document.getElementById('bgColorSwatch').style.background = color.hexString;
            });
            
            this.createPicker('outlineColorPicker', '#000000', (color) => {
                StyleManager.applyStyle('outlineColor', color.hexString);
            });
            
            this.createPicker('textDecorationColorPicker', '#000000', (color) => {
                StyleManager.applyStyle('textDecorationColor', color.hexString);
            });
            
            this.createPicker('textStrokeColorPicker', '#000000', (color) => {
                const width = document.getElementById('textStrokeWidthRange')?.value || 0;
                StyleManager.applyStyle('webkitTextStroke', `${width}px ${color.hexString}`);
            });
            
            this.createPicker('baseColorPicker', '#6366f1', (color) => {
                PaletteGenerator.generateFromBase(color.hexString);
            });
            
            this.createPicker('dropShadowColorPicker', '#000000', (color) => {
                FilterManager.updateDropShadow();
            });
        },

        createPicker(containerId, initialColor, onChange) {
            const container = document.getElementById(containerId);
            if (!container || typeof iro === 'undefined') return;
            
            const picker = new iro.ColorPicker(container, {
                width: 180,
                color: initialColor,
                layout: [
                    { component: iro.ui.Box },
                    { component: iro.ui.Slider, options: { sliderType: 'hue' } },
                    { component: iro.ui.Slider, options: { sliderType: 'alpha' } }
                ]
            });
            
            picker.on('color:change', onChange);
            STATE.colorPickers[containerId] = picker;
        },

        setColor(pickerId, color) {
            if (STATE.colorPickers[pickerId]) {
                STATE.colorPickers[pickerId].color.hexString = color;
            }
        }
    };

    // ═══════════════════════════════════════════════════════════════════════
    // SHADOW LAYERS MANAGER
    // ═══════════════════════════════════════════════════════════════════════
    
    const ShadowLayers = {
        initTextShadowLayers() {
            STATE.textShadowLayers = [
                { x: 2, y: 2, blur: 4, color: 'rgba(0,0,0,0.3)' }
            ];
            this.renderTextShadowLayers();
        },

        initBoxShadowLayers() {
            STATE.boxShadowLayers = [
                { x: 0, y: 4, blur: 15, spread: 0, color: 'rgba(0,0,0,0.2)', inset: false }
            ];
            this.renderBoxShadowLayers();
        },

        addTextShadowLayer() {
            STATE.textShadowLayers.push({
                x: Utils.randomInt(-5, 5),
                y: Utils.randomInt(-5, 5),
                blur: Utils.randomInt(2, 10),
                color: Utils.randomColor()
            });
            this.renderTextShadowLayers();
            this.applyTextShadow();
        },

        addBoxShadowLayer() {
            STATE.boxShadowLayers.push({
                x: Utils.randomInt(-10, 10),
                y: Utils.randomInt(-10, 10),
                blur: Utils.randomInt(5, 30),
                spread: Utils.randomInt(-5, 10),
                color: Utils.hexToRgba(Utils.randomColor(), 0.3),
                inset: false
            });
            this.renderBoxShadowLayers();
            this.applyBoxShadow();
        },

        removeTextShadowLayer(index) {
            STATE.textShadowLayers.splice(index, 1);
            this.renderTextShadowLayers();
            this.applyTextShadow();
        },

        removeBoxShadowLayer(index) {
            STATE.boxShadowLayers.splice(index, 1);
            this.renderBoxShadowLayers();
            this.applyBoxShadow();
        },

        renderTextShadowLayers() {
            if (!DOM.textShadowLayers) return;
            
            DOM.textShadowLayers.innerHTML = STATE.textShadowLayers.map((layer, i) => `
                <div class="shadow-layer" data-index="${i}">
                    <div class="shadow-layer-header">
                        <span>Katman ${i + 1}</span>
                        <button class="remove-layer-btn" data-action="remove-text-shadow" data-index="${i}">
                            <i class="fas fa-times"></i>
                        </button>
                    </div>
                    <div class="shadow-layer-controls">
                        <div class="form-row">
                            <label>X:</label>
                            <input type="number" class="ts-x" value="${layer.x}" data-index="${i}">
                            <label>Y:</label>
                            <input type="number" class="ts-y" value="${layer.y}" data-index="${i}">
                        </div>
                        <div class="form-row">
                            <label>Blur:</label>
                            <input type="number" class="ts-blur" value="${layer.blur}" min="0" data-index="${i}">
                            <label>Renk:</label>
                            <input type="color" class="ts-color" value="${Utils.rgbaToHex(layer.color)}" data-index="${i}">
                        </div>
                    </div>
                </div>
            `).join('');
            
            // Add event listeners
            DOM.textShadowLayers.querySelectorAll('input').forEach(input => {
                input.addEventListener('change', () => this.updateTextShadowLayer(input));
            });
            
            DOM.textShadowLayers.querySelectorAll('[data-action="remove-text-shadow"]').forEach(btn => {
                btn.addEventListener('click', () => this.removeTextShadowLayer(parseInt(btn.dataset.index)));
            });
        },

        renderBoxShadowLayers() {
            if (!DOM.boxShadowLayers) return;
            
            DOM.boxShadowLayers.innerHTML = STATE.boxShadowLayers.map((layer, i) => `
                <div class="shadow-layer" data-index="${i}">
                    <div class="shadow-layer-header">
                        <span>Katman ${i + 1}</span>
                        <label style="font-size:10px;display:flex;align-items:center;gap:4px;">
                            <input type="checkbox" class="bs-inset" ${layer.inset ? 'checked' : ''} data-index="${i}"> İç
                        </label>
                        <button class="remove-layer-btn" data-action="remove-box-shadow" data-index="${i}">
                            <i class="fas fa-times"></i>
                        </button>
                    </div>
                    <div class="shadow-layer-controls">
                        <div class="form-row">
                            <label>X:</label>
                            <input type="number" class="bs-x" value="${layer.x}" data-index="${i}">
                            <label>Y:</label>
                            <input type="number" class="bs-y" value="${layer.y}" data-index="${i}">
                        </div>
                        <div class="form-row">
                            <label>B:</label>
                            <input type="number" class="bs-blur" value="${layer.blur}" min="0" data-index="${i}">
                            <label>S:</label>
                            <input type="number" class="bs-spread" value="${layer.spread}" data-index="${i}">
                        </div>
                        <div class="form-row">
                            <label>Renk:</label>
                            <input type="color" class="bs-color" value="${Utils.rgbaToHex(layer.color)}" data-index="${i}">
                        </div>
                    </div>
                </div>
            `).join('');
            
            // Add event listeners
            DOM.boxShadowLayers.querySelectorAll('input').forEach(input => {
                input.addEventListener('change', () => this.updateBoxShadowLayer(input));
            });
            
            DOM.boxShadowLayers.querySelectorAll('[data-action="remove-box-shadow"]').forEach(btn => {
                btn.addEventListener('click', () => this.removeBoxShadowLayer(parseInt(btn.dataset.index)));
            });
        },

        updateTextShadowLayer(input) {
            const index = parseInt(input.dataset.index);
            const layer = STATE.textShadowLayers[index];
            
            if (input.classList.contains('ts-x')) layer.x = parseInt(input.value);
            else if (input.classList.contains('ts-y')) layer.y = parseInt(input.value);
            else if (input.classList.contains('ts-blur')) layer.blur = parseInt(input.value);
            else if (input.classList.contains('ts-color')) layer.color = input.value;
            
            this.applyTextShadow();
        },

        updateBoxShadowLayer(input) {
            const index = parseInt(input.dataset.index);
            const layer = STATE.boxShadowLayers[index];
            
            if (input.classList.contains('bs-x')) layer.x = parseInt(input.value);
            else if (input.classList.contains('bs-y')) layer.y = parseInt(input.value);
            else if (input.classList.contains('bs-blur')) layer.blur = parseInt(input.value);
            else if (input.classList.contains('bs-spread')) layer.spread = parseInt(input.value);
            else if (input.classList.contains('bs-color')) layer.color = input.value;
            else if (input.classList.contains('bs-inset')) layer.inset = input.checked;
            
            this.applyBoxShadow();
        },

        applyTextShadow() {
            const shadow = STATE.textShadowLayers
                .map(l => `${l.x}px ${l.y}px ${l.blur}px ${l.color}`)
                .join(', ');
            StyleManager.applyStyle('textShadow', shadow || 'none');
        },

        applyBoxShadow() {
            const shadow = STATE.boxShadowLayers
                .map(l => `${l.inset ? 'inset ' : ''}${l.x}px ${l.y}px ${l.blur}px ${l.spread}px ${l.color}`)
                .join(', ');
            StyleManager.applyStyle('boxShadow', shadow || 'none');
        }
    };

    // ═══════════════════════════════════════════════════════════════════════
    // GRADIENT MANAGER
    // ═══════════════════════════════════════════════════════════════════════
    
    const GradientManager = {
        initGradientColors() {
            STATE.gradientColors = [
                { color: '#6366f1', position: 0 },
                { color: '#a855f7', position: 100 }
            ];
            this.renderGradientColors();
        },

        initTextGradientColors() {
            STATE.textGradientColors = [
                { color: '#ff6b9d', position: 0 },
                { color: '#c471ed', position: 50 },
                { color: '#12c2e9', position: 100 }
            ];
            this.renderTextGradientColors();
        },

        initGradientBorderColors() {
            STATE.gradientBorderColors = [
                { color: '#ff0080', position: 0 },
                { color: '#7928ca', position: 100 }
            ];
            this.renderGradientBorderColors();
        },

        renderGradientColors() {
            if (!DOM.gradientColors) return;
            
            DOM.gradientColors.innerHTML = STATE.gradientColors.map((gc, i) => `
                <div class="gradient-color-item" data-index="${i}">
                    <input type="color" class="gc-color" value="${gc.color}" data-index="${i}">
                    <input type="number" class="gc-position" value="${gc.position}" min="0" max="100" data-index="${i}">
                    <span>%</span>
                    ${STATE.gradientColors.length > 2 ? `<button class="remove-gc-btn" data-index="${i}"><i class="fas fa-times"></i></button>` : ''}
                </div>
            `).join('');
            
            this.addGradientColorListeners(DOM.gradientColors, 'bg');
            this.updateGradientPreview();
        },

        renderTextGradientColors() {
            if (!DOM.textGradientColors) return;
            
            DOM.textGradientColors.innerHTML = STATE.textGradientColors.map((gc, i) => `
                <div class="gradient-color-item" data-index="${i}">
                    <input type="color" class="tgc-color" value="${gc.color}" data-index="${i}">
                    <input type="number" class="tgc-position" value="${gc.position}" min="0" max="100" data-index="${i}">
                    <span>%</span>
                    ${STATE.textGradientColors.length > 2 ? `<button class="remove-tgc-btn" data-index="${i}"><i class="fas fa-times"></i></button>` : ''}
                </div>
            `).join('');
            
            this.addGradientColorListeners(DOM.textGradientColors, 'text');
        },

        renderGradientBorderColors() {
            if (!DOM.gradientBorderColors) return;
            
            DOM.gradientBorderColors.innerHTML = STATE.gradientBorderColors.map((gc, i) => `
                <div class="gradient-color-item" data-index="${i}">
                    <input type="color" class="gbc-color" value="${gc.color}" data-index="${i}">
                    <input type="number" class="gbc-position" value="${gc.position}" min="0" max="100" data-index="${i}">
                    <span>%</span>
                    ${STATE.gradientBorderColors.length > 2 ? `<button class="remove-gbc-btn" data-index="${i}"><i class="fas fa-times"></i></button>` : ''}
                </div>
            `).join('');
            
            this.addGradientColorListeners(DOM.gradientBorderColors, 'border');
        },

        addGradientColorListeners(container, type) {
            container.querySelectorAll('input').forEach(input => {
                input.addEventListener('change', () => {
                    const index = parseInt(input.dataset.index);
                    let arr;
                    
                    if (type === 'bg') arr = STATE.gradientColors;
                    else if (type === 'text') arr = STATE.textGradientColors;
                    else arr = STATE.gradientBorderColors;
                    
                    if (input.type === 'color') arr[index].color = input.value;
                    else arr[index].position = parseInt(input.value);
                    
                    if (type === 'bg') {
                        this.applyBackgroundGradient();
                        this.updateGradientPreview();
                    }
                    else if (type === 'text') this.applyTextGradient();
                });
            });
            
            container.querySelectorAll('button').forEach(btn => {
                btn.addEventListener('click', () => {
                    const index = parseInt(btn.dataset.index);
                    if (type === 'bg') {
                        STATE.gradientColors.splice(index, 1);
                        this.renderGradientColors();
                        this.applyBackgroundGradient();
                    } else if (type === 'text') {
                        STATE.textGradientColors.splice(index, 1);
                        this.renderTextGradientColors();
                        this.applyTextGradient();
                    } else {
                        STATE.gradientBorderColors.splice(index, 1);
                        this.renderGradientBorderColors();
                    }
                });
            });
        },

        addGradientColor(type) {
            const newColor = {
                color: Utils.randomColor(),
                position: Utils.randomInt(20, 80)
            };
            
            if (type === 'bg') {
                STATE.gradientColors.push(newColor);
                STATE.gradientColors.sort((a, b) => a.position - b.position);
                this.renderGradientColors();
                this.applyBackgroundGradient();
            } else if (type === 'text') {
                STATE.textGradientColors.push(newColor);
                STATE.textGradientColors.sort((a, b) => a.position - b.position);
                this.renderTextGradientColors();
                this.applyTextGradient();
            } else {
                STATE.gradientBorderColors.push(newColor);
                STATE.gradientBorderColors.sort((a, b) => a.position - b.position);
                this.renderGradientBorderColors();
            }
        },

        applyBackgroundGradient() {
            const type = document.getElementById('gradientType')?.value || 'linear';
            const angle = document.getElementById('gradientAngle')?.value || 90;
            
            const colorStops = STATE.gradientColors
                .map(gc => `${gc.color} ${gc.position}%`)
                .join(', ');
            
            let gradient;
            if (type === 'linear') {
                gradient = `linear-gradient(${angle}deg, ${colorStops})`;
            } else if (type === 'radial') {
                gradient = `radial-gradient(circle, ${colorStops})`;
            } else {
                gradient = `conic-gradient(from ${angle}deg, ${colorStops})`;
            }
            
            StyleManager.applyStyle('background', gradient);
        },

        applyTextGradient() {
            const type = document.getElementById('textGradientType')?.value || 'linear';
            const angle = document.getElementById('textGradientAngle')?.value || 90;
            
            const colorStops = STATE.textGradientColors
                .map(gc => `${gc.color} ${gc.position}%`)
                .join(', ');
            
            let gradient;
            if (type === 'linear') {
                gradient = `linear-gradient(${angle}deg, ${colorStops})`;
            } else if (type === 'radial') {
                gradient = `radial-gradient(circle, ${colorStops})`;
            } else {
                gradient = `conic-gradient(from ${angle}deg, ${colorStops})`;
            }
            
            StyleManager.applyStyles({
                background: gradient,
                backgroundClip: 'text',
                webkitBackgroundClip: 'text',
                webkitTextFillColor: 'transparent',
                color: 'transparent'
            });
        },

        updateGradientPreview() {
            if (!DOM.gradientPreviewBar) return;
            
            const colorStops = STATE.gradientColors
                .map(gc => `${gc.color} ${gc.position}%`)
                .join(', ');
            
            DOM.gradientPreviewBar.style.background = `linear-gradient(90deg, ${colorStops})`;
        },

        applyGradientBorder() {
            const width = document.getElementById('gradientBorderWidth')?.value || 2;
            
            const colorStops = STATE.gradientBorderColors
                .map(gc => `${gc.color} ${gc.position}%`)
                .join(', ');
            
            const gradient = `linear-gradient(90deg, ${colorStops})`;
            
            StyleManager.applyStyles({
                border: `${width}px solid transparent`,
                borderImage: `${gradient} 1`
            });
            
            Toast.success('Gradyan çerçeve uygulandı!');
        }
    };

    // ═══════════════════════════════════════════════════════════════════════
    // PALETTE GENERATOR
    // ═══════════════════════════════════════════════════════════════════════
    
    const PaletteGenerator = {
        generateFromBase(baseColor) {
            const type = document.getElementById('paletteType')?.value || 'monochromatic';
            const size = parseInt(document.getElementById('paletteSize')?.value) || 5;
            
            let colors = [];
            
            if (typeof chroma !== 'undefined') {
                const base = chroma(baseColor);
                
                switch (type) {
                    case 'monochromatic':
                        colors = chroma.scale([base.darken(2), base, base.brighten(2)]).colors(size);
                        break;
                    case 'analogous':
                        for (let i = 0; i < size; i++) {
                            colors.push(base.set('hsl.h', `+${(i - Math.floor(size/2)) * 30}`).hex());
                        }
                        break;
                    case 'complementary':
                        colors.push(base.hex());
                        colors.push(base.set('hsl.h', '+180').hex());
                        colors = chroma.scale(colors).colors(size);
                        break;
                    case 'triadic':
                        colors.push(base.hex());
                        colors.push(base.set('hsl.h', '+120').hex());
                        colors.push(base.set('hsl.h', '+240').hex());
                        colors = chroma.scale(colors).colors(size);
                        break;
                    case 'split-complementary':
                        colors.push(base.hex());
                        colors.push(base.set('hsl.h', '+150').hex());
                        colors.push(base.set('hsl.h', '+210').hex());
                        colors = chroma.scale(colors).colors(size);
                        break;
                    case 'tetradic':
                        colors.push(base.hex());
                        colors.push(base.set('hsl.h', '+90').hex());
                        colors.push(base.set('hsl.h', '+180').hex());
                        colors.push(base.set('hsl.h', '+270').hex());
                        colors = chroma.scale(colors).colors(size);
                        break;
                    case 'shades':
                        colors = chroma.scale([base.darken(3), base, base.brighten(0.5)]).colors(size);
                        break;
                    case 'pastel':
                        colors = chroma.scale([base.saturate(-2).brighten(2), base.saturate(-1).brighten(1)]).colors(size);
                        break;
                    default:
                        colors = chroma.scale(['#f00', '#0f0', '#00f']).colors(size);
                }
            } else {
                // Fallback without chroma
                for (let i = 0; i < size; i++) {
                    colors.push(Utils.randomColor());
                }
            }
            
            this.renderPalette(colors);
            STATE.currentPalette = colors;
        },

        renderPalette(colors) {
            if (!DOM.palettePreview) return;
            
            DOM.palettePreview.innerHTML = colors.map(color => `
                <div class="palette-color" 
                     style="background-color: ${color};"
                     data-color="${color}"
                     title="${color}">
                </div>
            `).join('');
            
            // Add click to copy
            DOM.palettePreview.querySelectorAll('.palette-color').forEach(el => {
                el.addEventListener('click', () => {
                    Utils.copyToClipboard(el.dataset.color);
                    Toast.success(`${el.dataset.color} kopyalandı!`);
                });
            });
        },

        paletteToGradient() {
            if (!STATE.currentPalette || STATE.currentPalette.length < 2) {
                Toast.warning('Önce bir palet oluşturun!');
                return;
            }
            
            const step = 100 / (STATE.currentPalette.length - 1);
            STATE.gradientColors = STATE.currentPalette.map((color, i) => ({
                color: color,
                position: Math.round(i * step)
            }));
            
            GradientManager.renderGradientColors();
            GradientManager.applyBackgroundGradient();
            
            // Switch to gradient tab
            document.querySelector('[data-sub-tab="bg-gradient"]')?.click();
            Toast.success('Palet gradyana dönüştürüldü!');
        }
    };

    // ═══════════════════════════════════════════════════════════════════════
    // FILTER MANAGER
    // ═══════════════════════════════════════════════════════════════════════
    
    const FilterManager = {
        updateFilters() {
            const blur = document.getElementById('filterBlurRange')?.value || 0;
            const brightness = document.getElementById('filterBrightnessRange')?.value || 100;
            const contrast = document.getElementById('filterContrastRange')?.value || 100;
            const saturate = document.getElementById('filterSaturateRange')?.value || 100;
            const hueRotate = document.getElementById('filterHueRotateRange')?.value || 0;
            const invert = document.getElementById('filterInvertRange')?.value || 0;
            const sepia = document.getElementById('filterSepiaRange')?.value || 0;
            const grayscale = document.getElementById('filterGrayscaleRange')?.value || 0;
            
            let filter = [];
            
            if (blur != 0) filter.push(`blur(${blur}px)`);
            if (brightness != 100) filter.push(`brightness(${brightness}%)`);
            if (contrast != 100) filter.push(`contrast(${contrast}%)`);
            if (saturate != 100) filter.push(`saturate(${saturate}%)`);
            if (hueRotate != 0) filter.push(`hue-rotate(${hueRotate}deg)`);
            if (invert != 0) filter.push(`invert(${invert}%)`);
            if (sepia != 0) filter.push(`sepia(${sepia}%)`);
            if (grayscale != 0) filter.push(`grayscale(${grayscale}%)`);
            
            // Add drop shadow
            const dsX = document.getElementById('dropShadowX')?.value || 0;
            const dsY = document.getElementById('dropShadowY')?.value || 0;
            const dsBlur = document.getElementById('dropShadowBlur')?.value || 0;
            const dsColor = STATE.colorPickers['dropShadowColorPicker']?.color?.hexString || '#000000';
            
            if (dsX != 0 || dsY != 0 || dsBlur != 0) {
                filter.push(`drop-shadow(${dsX}px ${dsY}px ${dsBlur}px ${dsColor})`);
            }
            
            StyleManager.applyStyle('filter', filter.length > 0 ? filter.join(' ') : 'none');
        },

        updateDropShadow() {
            this.updateFilters();
        },

        updateBackdropBlur() {
            const blur = document.getElementById('backdropBlurRange')?.value || 0;
            StyleManager.applyStyle('backdropFilter', blur > 0 ? `blur(${blur}px)` : 'none');
        },

        applyPreset(preset) {
            const presets = {
                vintage: { sepia: 40, brightness: 90, contrast: 110, saturate: 80 },
                cold: { saturate: 120, hueRotate: 180, brightness: 105 },
                warm: { saturate: 110, hueRotate: 20, brightness: 105 },
                dramatic: { contrast: 140, saturate: 130, brightness: 90 }
            };
            
            if (presets[preset]) {
                const p = presets[preset];
                if (p.sepia !== undefined) document.getElementById('filterSepiaRange').value = p.sepia;
                if (p.brightness !== undefined) document.getElementById('filterBrightnessRange').value = p.brightness;
                if (p.contrast !== undefined) document.getElementById('filterContrastRange').value = p.contrast;
                if (p.saturate !== undefined) document.getElementById('filterSaturateRange').value = p.saturate;
                if (p.hueRotate !== undefined) document.getElementById('filterHueRotateRange').value = p.hueRotate;
                
                this.updateFilters();
                this.updateValueBadges();
                Toast.success(`${preset.charAt(0).toUpperCase() + preset.slice(1)} filtresi uygulandı!`);
            }
        },

        updateValueBadges() {
            const badges = {
                blurVal: ['filterBlurRange', 'px'],
                brightnessVal: ['filterBrightnessRange', '%'],
                contrastVal: ['filterContrastRange', '%'],
                saturateVal: ['filterSaturateRange', '%'],
                hueRotateVal: ['filterHueRotateRange', '°'],
                invertVal: ['filterInvertRange', '%'],
                sepiaVal: ['filterSepiaRange', '%'],
                grayscaleVal: ['filterGrayscaleRange', '%'],
                backdropBlurVal: ['backdropBlurRange', 'px']
            };
            
            for (const [badgeId, [inputId, unit]] of Object.entries(badges)) {
                const badge = document.getElementById(badgeId);
                const input = document.getElementById(inputId);
                if (badge && input) {
                    badge.textContent = input.value + unit;
                }
            }
        },

        resetFilters() {
            const ranges = [
                'filterBlurRange', 'filterBrightnessRange', 'filterContrastRange',
                'filterSaturateRange', 'filterHueRotateRange', 'filterInvertRange',
                'filterSepiaRange', 'filterGrayscaleRange', 'backdropBlurRange'
            ];
            
            ranges.forEach(id => {
                const el = document.getElementById(id);
                if (el) {
                    if (id.includes('Brightness') || id.includes('Contrast') || id.includes('Saturate')) {
                        el.value = 100;
                    } else {
                        el.value = 0;
                    }
                }
            });
            
            document.getElementById('dropShadowX').value = 0;
            document.getElementById('dropShadowY').value = 0;
            document.getElementById('dropShadowBlur').value = 0;
            
            StyleManager.applyStyles({
                filter: 'none',
                backdropFilter: 'none'
            });
            
            this.updateValueBadges();
            Toast.success('Filtreler sıfırlandı!');
        }
    };

    // ═══════════════════════════════════════════════════════════════════════
    // ANIMATION MANAGER
    // ═══════════════════════════════════════════════════════════════════════
    
    const AnimationManager = {
        applyAnimation(animName) {
            const anim = CONFIG.animations[animName];
            if (!anim) return;
            
            // Add keyframes to document
            this.injectKeyframes(anim.keyframes);
            STATE.customKeyframes = anim.keyframes;
            
            const duration = document.getElementById('animationDurationRange')?.value || 1;
            const delay = document.getElementById('animationDelayRange')?.value || 0;
            const timing = document.getElementById('animationTimingFunction')?.value || 'ease';
            const iteration = document.getElementById('animationIterationCount')?.value || '1';
            const direction = document.getElementById('animationDirection')?.value || 'normal';
            const fillMode = document.getElementById('animationFillMode')?.value || 'none';
            
            const animationValue = `${anim.name} ${duration}s ${timing} ${delay}s ${iteration} ${direction} ${fillMode}`;
            
            StyleManager.applyStyle('animation', animationValue);
            Toast.success(`${animName} animasyonu uygulandı!`);
        },

        injectKeyframes(keyframes) {
            // Remove old custom keyframes
            const oldStyle = document.getElementById('custom-keyframes');
            if (oldStyle) oldStyle.remove();
            
            // Add new keyframes
            const style = document.createElement('style');
            style.id = 'custom-keyframes';
            style.textContent = keyframes;
            document.head.appendChild(style);
        },

        stopAnimation() {
            StyleManager.applyStyle('animation', 'none');
            Toast.info('Animasyon durduruldu.');
        },

        pauseAnimation() {
            StyleManager.applyStyle('animationPlayState', 'paused');
            STATE.animationPaused = true;
        },

        playAnimation() {
            StyleManager.applyStyle('animationPlayState', 'running');
            STATE.animationPaused = false;
        },

        toggleAnimation() {
            if (STATE.animationPaused) {
                this.playAnimation();
            } else {
                this.pauseAnimation();
            }
        },

        applyCustomKeyframes() {
            const keyframesCode = document.getElementById('animationKeyframes')?.value;
            if (!keyframesCode) {
                Toast.warning('Keyframes kodu boş!');
                return;
            }
            
            // Extract animation name
            const nameMatch = keyframesCode.match(/@keyframes\s+(\w+)/);
            if (!nameMatch) {
                Toast.error('Geçersiz keyframes formatı!');
                return;
            }
            
            const animName = nameMatch[1];
            this.injectKeyframes(keyframesCode);
            STATE.customKeyframes = keyframesCode;
            
            const duration = document.getElementById('animationDurationRange')?.value || 1;
            const timing = document.getElementById('animationTimingFunction')?.value || 'ease';
            const iteration = document.getElementById('animationIterationCount')?.value || 'infinite';
            
            StyleManager.applyStyle('animation', `${animName} ${duration}s ${timing} ${iteration}`);
            Toast.success('Özel animasyon uygulandı!');
        },

        randomAnimation() {
            const animNames = Object.keys(CONFIG.animations);
            const randomAnim = Utils.randomFromArray(animNames);
            this.applyAnimation(randomAnim);
        },

        randomTimingFunction() {
            const timings = ['ease', 'linear', 'ease-in', 'ease-out', 'ease-in-out', 
                'cubic-bezier(0.68,-0.55,0.265,1.55)', 'cubic-bezier(0.34,1.56,0.64,1)'];
            const timing = Utils.randomFromArray(timings);
            document.getElementById('animationTimingFunction').value = timing;
            
            // Re-apply current animation with new timing
            const currentAnim = DOM.previewBox.style.animationName;
            if (currentAnim && currentAnim !== 'none') {
                const duration = document.getElementById('animationDurationRange')?.value || 1;
                const iteration = document.getElementById('animationIterationCount')?.value || '1';
                StyleManager.applyStyle('animation', `${currentAnim} ${duration}s ${timing} ${iteration}`);
            }
        }
    };

    // ═══════════════════════════════════════════════════════════════════════
    // CLIP PATH MANAGER
    // ═══════════════════════════════════════════════════════════════════════
    
    const ClipPathManager = {
        init() {
            this.renderGallery();
        },

        renderGallery() {
            if (!DOM.clipShapeGallery) return;
            
            DOM.clipShapeGallery.innerHTML = CONFIG.clipPaths.map(shape => `
                <button class="clip-shape-btn" data-clip="${shape.value}" title="${shape.name}">
                    <span class="clip-preview">${shape.preview || '□'}</span>
                    <span class="clip-name">${shape.name}</span>
                </button>
            `).join('');
            
            DOM.clipShapeGallery.querySelectorAll('.clip-shape-btn').forEach(btn => {
                btn.addEventListener('click', () => {
                    this.applyClipPath(btn.dataset.clip);
                    
                    // Update active state
                    DOM.clipShapeGallery.querySelectorAll('.clip-shape-btn').forEach(b => b.classList.remove('active'));
                    btn.classList.add('active');
                });
            });
        },

        applyClipPath(value) {
            StyleManager.applyStyle('clipPath', value);
            document.getElementById('clipPath').value = value;
        },

        randomClipPath() {
            const shape = Utils.randomFromArray(CONFIG.clipPaths.filter(s => s.value !== 'none'));
            this.applyClipPath(shape.value);
            Toast.success(`${shape.name} şekli uygulandı!`);
        },

        resetClipPath() {
            StyleManager.applyStyle('clipPath', 'none');
            document.getElementById('clipPath').value = '';
            Toast.info('Clip-path sıfırlandı.');
        }
    };

    // ═══════════════════════════════════════════════════════════════════════
    // PATTERN MANAGER
    // ═══════════════════════════════════════════════════════════════════════
    
    const PatternManager = {
        init() {
            this.renderGallery();
        },

        renderGallery() {
            if (!DOM.patternGallery) return;
            
            DOM.patternGallery.innerHTML = CONFIG.patterns.map((pattern, i) => `
                <button class="pattern-btn" data-pattern="${i}" title="${pattern.name}">
                    <div class="pattern-preview" style="background: ${pattern.css}; background-size: ${pattern.size};"></div>
                    <span>${pattern.name}</span>
                </button>
            `).join('');
            
            DOM.patternGallery.querySelectorAll('.pattern-btn').forEach(btn => {
                btn.addEventListener('click', () => {
                    const pattern = CONFIG.patterns[parseInt(btn.dataset.pattern)];
                    this.applyPattern(pattern);
                });
            });
        },

        applyPattern(pattern) {
            StyleManager.applyStyles({
                background: pattern.css,
                backgroundSize: pattern.size
            });
            Toast.success(`${pattern.name} deseni uygulandı!`);
        },

        randomPattern() {
            const pattern = Utils.randomFromArray(CONFIG.patterns);
            this.applyPattern(pattern);
        }
    };

    // ═══════════════════════════════════════════════════════════════════════
    // TRANSFORM MANAGER
    // ═══════════════════════════════════════════════════════════════════════
    
    const TransformManager = {
        update() {
            const rotate = document.getElementById('rotate')?.value || 0;
            const scaleX = document.getElementById('scaleX')?.value || 1;
            const scaleY = document.getElementById('scaleY')?.value || 1;
            const skewX = document.getElementById('skewX')?.value || 0;
            const skewY = document.getElementById('skewY')?.value || 0;
            const translateX = document.getElementById('translateX')?.value || 0;
            const translateY = document.getElementById('translateY')?.value || 0;
            const rotateX = document.getElementById('rotateX')?.value || 0;
            const rotateY = document.getElementById('rotateY')?.value || 0;
            const rotateZ = document.getElementById('rotateZ')?.value || 0;
            const perspective = document.getElementById('perspective')?.value || 0;
            
            let transforms = [];
            
            if (perspective != 0) transforms.push(`perspective(${perspective}px)`);
            if (rotate != 0) transforms.push(`rotate(${rotate}deg)`);
            if (rotateX != 0) transforms.push(`rotateX(${rotateX}deg)`);
            if (rotateY != 0) transforms.push(`rotateY(${rotateY}deg)`);
            if (rotateZ != 0) transforms.push(`rotateZ(${rotateZ}deg)`);
            if (scaleX != 1 || scaleY != 1) transforms.push(`scale(${scaleX}, ${scaleY})`);
            if (skewX != 0 || skewY != 0) transforms.push(`skew(${skewX}deg, ${skewY}deg)`);
            if (translateX != 0 || translateY != 0) transforms.push(`translate(${translateX}px, ${translateY}px)`);
            
            StyleManager.applyStyle('transform', transforms.length > 0 ? transforms.join(' ') : 'none');
        },

        setOrigin(origin) {
            StyleManager.applyStyle('transformOrigin', origin);
        },

        reset() {
            const inputs = ['rotate', 'skewX', 'skewY', 'translateX', 'translateY', 'rotateX', 'rotateY', 'rotateZ', 'perspective'];
            inputs.forEach(id => {
                const el = document.getElementById(id);
                if (el) el.value = 0;
            });
            
            document.getElementById('scaleX').value = 1;
            document.getElementById('scaleY').value = 1;
            document.getElementById('scaleRange').value = 1;
            document.getElementById('rotateRange').value = 0;
            
            StyleManager.applyStyles({
                transform: 'none',
                transformOrigin: 'center center'
            });
            
            document.getElementById('rotateVal').textContent = '0°';
            document.getElementById('scaleVal').textContent = '1';
            
            Toast.info('Dönüşümler sıfırlandı.');
        },

        random() {
            document.getElementById('rotate').value = Utils.randomInt(-30, 30);
            document.getElementById('scaleX').value = Utils.randomFloat(0.8, 1.3);
            document.getElementById('scaleY').value = Utils.randomFloat(0.8, 1.3);
            document.getElementById('skewX').value = Utils.randomInt(-15, 15);
            document.getElementById('skewY').value = Utils.randomInt(-15, 15);
            document.getElementById('translateX').value = Utils.randomInt(-20, 20);
            document.getElementById('translateY').value = Utils.randomInt(-20, 20);
            
            this.update();
        },

        random3D() {
            document.getElementById('rotateX').value = Utils.randomInt(-45, 45);
            document.getElementById('rotateY').value = Utils.randomInt(-45, 45);
            document.getElementById('rotateZ').value = Utils.randomInt(-30, 30);
            document.getElementById('perspective').value = Utils.randomInt(500, 1500);
            
            this.update();
        }
    };

    // ═══════════════════════════════════════════════════════════════════════
    // CHAOS ENGINE
    // ═══════════════════════════════════════════════════════════════════════
    
    const ChaosEngine = {
        generate(maxChaos = false) {
            const level = maxChaos ? 10 : parseInt(document.getElementById('chaosLevel')?.value || 5);
            const styles = {};
            
            // Font chaos
            if (document.getElementById('chaosFont')?.checked) {
                styles.fontFamily = Utils.randomFromArray(CONFIG.fonts);
                styles.fontSize = `${Utils.randomInt(20 + level * 2, 40 + level * 8)}px`;
                styles.fontWeight = Utils.randomFromArray(['400', '500', '600', '700', '800', '900']);
                styles.color = Utils.randomHSL();
                
                if (level > 5) {
                    styles.letterSpacing = `${Utils.randomInt(-2, 10)}px`;
                    styles.textTransform = Utils.randomFromArray(['none', 'uppercase', 'lowercase', 'capitalize']);
                }
            }
            
            // Background chaos
            if (document.getElementById('chaosBackground')?.checked) {
                if (Math.random() > 0.5) {
                    // Gradient
                    const colors = [];
                    const colorCount = Utils.randomInt(2, 4);
                    for (let i = 0; i < colorCount; i++) {
                        colors.push(Utils.randomHSL());
                    }
                    const angle = Utils.randomInt(0, 360);
                    const type = Utils.randomFromArray(['linear', 'radial', 'conic']);
                    
                    if (type === 'linear') {
                        styles.background = `linear-gradient(${angle}deg, ${colors.join(', ')})`;
                    } else if (type === 'radial') {
                        styles.background = `radial-gradient(circle, ${colors.join(', ')})`;
                    } else {
                        styles.background = `conic-gradient(from ${angle}deg, ${colors.join(', ')})`;
                    }
                } else {
                    styles.backgroundColor = Utils.randomHSL(40, 70, 20, 50);
                }
            }
            
            // Border chaos
            if (document.getElementById('chaosBorder')?.checked) {
                const borderWidth = Utils.randomInt(1, 5 + level);
                const borderStyle = Utils.randomFromArray(['solid', 'dashed', 'dotted', 'double']);
                const borderColor = Utils.randomHSL();
                styles.border = `${borderWidth}px ${borderStyle} ${borderColor}`;
                
                styles.borderRadius = `${Utils.randomInt(0, 30 + level * 5)}px`;
            }
            
            // Effects chaos
            if (document.getElementById('chaosEffects')?.checked && level > 3) {
                const filters = [];
                if (Math.random() > 0.6) filters.push(`blur(${Utils.randomInt(0, 2)}px)`);
                if (Math.random() > 0.5) filters.push(`brightness(${Utils.randomInt(90, 130)}%)`);
                if (Math.random() > 0.5) filters.push(`saturate(${Utils.randomInt(80, 150)}%)`);
                if (Math.random() > 0.7) filters.push(`hue-rotate(${Utils.randomInt(0, 360)}deg)`);
                
                if (filters.length > 0) {
                    styles.filter = filters.join(' ');
                }
            }
            
            // Transform chaos
            if (document.getElementById('chaosTransform')?.checked && level > 4) {
                const transforms = [];
                if (Math.random() > 0.5) transforms.push(`rotate(${Utils.randomInt(-15, 15)}deg)`);
                if (Math.random() > 0.6) transforms.push(`scale(${Utils.randomFloat(0.9, 1.2)})`);
                if (Math.random() > 0.7) transforms.push(`skew(${Utils.randomInt(-10, 10)}deg)`);
                
                if (transforms.length > 0) {
                    styles.transform = transforms.join(' ');
                }
            }
            
            // Box shadow chaos
            if (document.getElementById('chaosBoxShadow')?.checked) {
                const shadows = [];
                const shadowCount = Utils.randomInt(1, 2 + Math.floor(level / 3));
                
                for (let i = 0; i < shadowCount; i++) {
                    const inset = Math.random() > 0.8 ? 'inset ' : '';
                    const x = Utils.randomInt(-20, 20);
                    const y = Utils.randomInt(-20, 20);
                    const blur = Utils.randomInt(5, 30 + level * 3);
                    const spread = Utils.randomInt(-5, 10);
                    const color = Utils.hexToRgba(Utils.randomColor(), Utils.randomFloat(0.2, 0.6));
                    
                    shadows.push(`${inset}${x}px ${y}px ${blur}px ${spread}px ${color}`);
                }
                
                styles.boxShadow = shadows.join(', ');
            }
            
            // Text shadow chaos
            if (document.getElementById('chaosFont')?.checked && level > 3) {
                const textShadows = [];
                const count = Utils.randomInt(1, 3);
                
                for (let i = 0; i < count; i++) {
                    const x = Utils.randomInt(-5, 5);
                    const y = Utils.randomInt(-5, 5);
                    const blur = Utils.randomInt(0, 15);
                    const color = Utils.randomHSL();
                    textShadows.push(`${x}px ${y}px ${blur}px ${color}`);
                }
                
                styles.textShadow = textShadows.join(', ');
            }
            
            // Animation chaos
            if (document.getElementById('chaosAnimation')?.checked && level > 5) {
                const animNames = Object.keys(CONFIG.animations);
                const anim = Utils.randomFromArray(animNames);
                const animConfig = CONFIG.animations[anim];
                
                AnimationManager.injectKeyframes(animConfig.keyframes);
                STATE.customKeyframes = animConfig.keyframes;
                
                const duration = Utils.randomFloat(0.5, 3);
                const timing = Utils.randomFromArray(['ease', 'linear', 'ease-in-out', 'cubic-bezier(0.68,-0.55,0.265,1.55)']);
                
                styles.animation = `${anim} ${duration}s ${timing} infinite`;
            }
            
            // Clip path chaos
            if (document.getElementById('chaosClip')?.checked && level > 6 && Math.random() > 0.6) {
                const shape = Utils.randomFromArray(CONFIG.clipPaths.filter(s => s.value !== 'none'));
                styles.clipPath = shape.value;
            }
            
            // Text gradient chaos
            if (document.getElementById('chaosTextGradient')?.checked && level > 7 && Math.random() > 0.5) {
                const colors = [Utils.randomHSL(), Utils.randomHSL(), Utils.randomHSL()];
                const angle = Utils.randomInt(0, 360);
                
                styles.background = `linear-gradient(${angle}deg, ${colors.join(', ')})`;
                styles.backgroundClip = 'text';
                styles.webkitBackgroundClip = 'text';
                styles.webkitTextFillColor = 'transparent';
                styles.color = 'transparent';
            }
            
            StyleManager.applyStyles(styles);
            Toast.success(maxChaos ? '🔥 MAKSİMUM KAOS!' : 'Kaos stili oluşturuldu!');
        },

        startAutoPlay() {
            if (STATE.autoPlayInterval) return;
            
            const interval = (parseInt(document.getElementById('autoPlayInterval')?.value) || 3) * 1000;
            
            STATE.autoPlayInterval = setInterval(() => {
                this.generate(false);
            }, interval);
            
            STATE.isPlaying = true;
            document.getElementById('startAutoPlay').disabled = true;
            document.getElementById('stopAutoPlay').disabled = false;
            
            Toast.info('Otomatik kaos modu başladı!');
        },

        stopAutoPlay() {
            if (STATE.autoPlayInterval) {
                clearInterval(STATE.autoPlayInterval);
                STATE.autoPlayInterval = null;
            }
            
            STATE.isPlaying = false;
            document.getElementById('startAutoPlay').disabled = false;
            document.getElementById('stopAutoPlay').disabled = true;
            
            Toast.info('Otomatik kaos modu durduruldu.');
        }
    };

    // ═══════════════════════════════════════════════════════════════════════
    // THEME PRESETS
    // ═══════════════════════════════════════════════════════════════════════
    
    const ThemePresets = {
        apply(themeName) {
            const themes = {
                'auto-theme-neon': {
                    color: '#0ff',
                    backgroundColor: '#0a0a2e',
                    textShadow: '0 0 5px #0ff, 0 0 10px #0ff, 0 0 20px #0ff, 0 0 40px #0ff',
                    fontFamily: "'Orbitron', sans-serif",
                    fontSize: '36px',
                    fontWeight: '700',
                    borderRadius: '10px',
                    padding: '30px 50px'
                },
                'auto-theme-cyberpunk': {
                    color: '#ff2d6a',
                    backgroundColor: '#0d0221',
                    textShadow: '2px 2px 0 #00f9ff, -2px -2px 0 #ff2d6a',
                    fontFamily: "'Press Start 2P', monospace",
                    fontSize: '24px',
                    border: '3px solid #ff2d6a',
                    borderRadius: '0',
                    padding: '25px 40px'
                },
                'auto-theme-dark-elegant': {
                    color: '#d4af37',
                    backgroundColor: '#1a1a2e',
                    fontFamily: "'Playfair Display', serif",
                    fontSize: '42px',
                    fontWeight: '700',
                    fontStyle: 'italic',
                    letterSpacing: '3px',
                    borderBottom: '2px solid #d4af37',
                    padding: '30px 50px'
                },
                'auto-theme-matrix': {
                    color: '#00ff41',
                    backgroundColor: '#0d0208',
                    textShadow: '0 0 5px #00ff41, 0 0 10px #00ff41',
                    fontFamily: "'VT323', monospace",
                    fontSize: '40px',
                    padding: '25px 45px'
                },
                'auto-theme-minimal': {
                    color: '#333',
                    backgroundColor: '#fafafa',
                    fontFamily: "'Inter', sans-serif",
                    fontSize: '32px',
                    fontWeight: '300',
                    padding: '30px 50px'
                },
                'auto-theme-vintage': {
                    color: '#5c3317',
                    backgroundColor: '#f4e9d8',
                    fontFamily: "'Playfair Display', serif",
                    fontSize: '36px',
                    fontStyle: 'italic',
                    filter: 'sepia(20%)',
                    borderRadius: '5px',
                    boxShadow: '5px 5px 15px rgba(0,0,0,0.2)',
                    padding: '30px 50px'
                },
                'auto-theme-pastel': {
                    color: '#6b5b95',
                    backgroundColor: '#fff0f5',
                    fontFamily: "'Nunito', sans-serif",
                    fontSize: '34px',
                    fontWeight: '600',
                    borderRadius: '25px',
                    boxShadow: '0 10px 30px rgba(107, 91, 149, 0.2)',
                    padding: '30px 50px'
                },
                'auto-theme-glassmorphism': {
                    color: '#fff',
                    background: 'rgba(255, 255, 255, 0.1)',
                    backdropFilter: 'blur(10px)',
                    fontFamily: "'Poppins', sans-serif",
                    fontSize: '32px',
                    fontWeight: '500',
                    borderRadius: '20px',
                    border: '1px solid rgba(255, 255, 255, 0.2)',
                    boxShadow: '0 8px 32px rgba(0, 0, 0, 0.3)',
                    padding: '30px 50px'
                },
                'auto-theme-neumorphism': {
                    color: '#6b7b99',
                    backgroundColor: '#e0e5ec',
                    fontFamily: "'Inter', sans-serif",
                    fontSize: '32px',
                    fontWeight: '600',
                    borderRadius: '20px',
                    boxShadow: '10px 10px 20px #a3b1c6, -10px -10px 20px #ffffff',
                    padding: '30px 50px'
                },
                'auto-theme-aurora': {
                    color: '#fff',
                    background: 'linear-gradient(135deg, #141e30, #243b55, #141e30)',
                    fontFamily: "'Space Grotesk', sans-serif",
                    fontSize: '36px',
                    fontWeight: '700',
                    textShadow: '0 0 20px rgba(168, 255, 120, 0.5)',
                    borderRadius: '15px',
                    padding: '30px 50px'
                },
                'auto-theme-holographic': {
                    color: '#fff',
                    background: 'linear-gradient(135deg, #ff6ec7, #7873f5, #4adede, #ff6ec7)',
                    backgroundSize: '400% 400%',
                    fontFamily: "'Bebas Neue', sans-serif",
                    fontSize: '48px',
                    letterSpacing: '5px',
                    borderRadius: '10px',
                    animation: 'colorWave 3s ease infinite',
                    padding: '30px 60px'
                },
                'auto-theme-nature': {
                    color: '#2d5016',
                    backgroundColor: '#e8f5e9',
                    fontFamily: "'Raleway', sans-serif",
                    fontSize: '34px',
                    fontWeight: '500',
                    borderRadius: '30px',
                    boxShadow: '0 5px 20px rgba(45, 80, 22, 0.2)',
                    padding: '30px 50px'
                },
                'auto-theme-ocean': {
                    color: '#fff',
                    background: 'linear-gradient(180deg, #0077b6, #00b4d8, #90e0ef)',
                    fontFamily: "'Exo 2', sans-serif",
                    fontSize: '36px',
                    fontWeight: '700',
                    borderRadius: '20px',
                    textShadow: '2px 2px 4px rgba(0,0,0,0.3)',
                    padding: '30px 50px'
                },
                'auto-theme-sunset': {
                    color: '#fff',
                    background: 'linear-gradient(135deg, #ff512f, #f09819, #ff512f)',
                    fontFamily: "'Dancing Script', cursive",
                    fontSize: '48px',
                    fontWeight: '700',
                    textShadow: '2px 2px 4px rgba(0,0,0,0.3)',
                    borderRadius: '15px',
                    padding: '30px 60px'
                },
                'auto-theme-candy': {
                    color: '#ff6b9d',
                    backgroundColor: '#fff0f5',
                    fontFamily: "'Pacifico', cursive",
                    fontSize: '42px',
                    textShadow: '2px 2px 0 #ffb6c1',
                    borderRadius: '30px',
                    border: '3px dashed #ff6b9d',
                    padding: '30px 50px'
                },
                'auto-theme-retrowave': {
                    color: '#ff71ce',
                    background: 'linear-gradient(180deg, #030014, #1a0a2e, #030014)',
                    fontFamily: "'Righteous', cursive",
                    fontSize: '40px',
                    textShadow: '0 0 10px #ff71ce, 0 0 20px #01cdfe, 0 0 30px #b967ff',
                    borderRadius: '0',
                    padding: '30px 50px'
                },
                'auto-theme-brutalist': {
                    color: '#000',
                    backgroundColor: '#ff0',
                    fontFamily: "'Impact', sans-serif",
                    fontSize: '48px',
                    fontWeight: '900',
                    textTransform: 'uppercase',
                    border: '5px solid #000',
                    borderRadius: '0',
                    boxShadow: '10px 10px 0 #000',
                    padding: '20px 40px'
                },
                'auto-theme-lofi': {
                    color: '#5d4e60',
                    backgroundColor: '#f5f0e8',
                    fontFamily: "'Courier New', monospace",
                    fontSize: '30px',
                    filter: 'sepia(15%) saturate(80%)',
                    borderRadius: '8px',
                    boxShadow: '4px 4px 0 #d4a5a5',
                    padding: '25px 45px'
                },
                'auto-theme-forest': {
                    color: '#c4e538',
                    background: 'linear-gradient(135deg, #1a3a1a, #2d5a2d, #1a3a1a)',
                    fontFamily: "'Cinzel', serif",
                    fontSize: '36px',
                    fontWeight: '700',
                    textShadow: '0 0 10px rgba(196, 229, 56, 0.5)',
                    borderRadius: '15px',
                    padding: '30px 50px'
                },
                'auto-theme-paper': {
                    color: '#444',
                    backgroundColor: '#f5f0e8',
                    fontFamily: "'Georgia', serif",
                    fontSize: '32px',
                    fontStyle: 'italic',
                    borderRadius: '3px',
                    boxShadow: '0 2px 10px rgba(0,0,0,0.1), inset 0 0 50px rgba(0,0,0,0.05)',
                    padding: '30px 50px'
                }
            };
            
            const theme = themes[themeName];
            if (theme) {
                // Inject color wave animation if needed
                if (themeName === 'auto-theme-holographic') {
                    AnimationManager.injectKeyframes('@keyframes colorWave{0%{background-position:0% 50%}50%{background-position:100% 50%}100%{background-position:0% 50%}}');
                    STATE.customKeyframes = '@keyframes colorWave{0%{background-position:0% 50%}50%{background-position:100% 50%}100%{background-position:0% 50%}}';
                }
                
                StyleManager.applyStyles(theme);
                Toast.success(`${themeName.replace('auto-theme-', '').charAt(0).toUpperCase() + themeName.replace('auto-theme-', '').slice(1)} teması uygulandı!`);
            }
        }
    };

    // ═══════════════════════════════════════════════════════════════════════
    // BEZIER EDITOR
    // ═══════════════════════════════════════════════════════════════════════
    
    const BezierEditor = {
        p1: { x: 0.25, y: 0.46 },
        p2: { x: 0.45, y: 0.94 },
        dragging: null,

        init() {
            this.canvas = DOM.bezierCanvas;
            if (!this.canvas) return;
            
            this.ctx = this.canvas.getContext('2d');
            this.draw();
            
            // Event listeners
            this.canvas.addEventListener('mousedown', (e) => this.onMouseDown(e));
            document.addEventListener('mousemove', (e) => this.onMouseMove(e));
            document.addEventListener('mouseup', () => this.dragging = null);
            
            // Input listeners
            ['bezierP1x', 'bezierP1y', 'bezierP2x', 'bezierP2y'].forEach(id => {
                const input = document.getElementById(id);
                if (input) {
                    input.addEventListener('change', () => {
                        this.p1.x = parseFloat(document.getElementById('bezierP1x').value);
                        this.p1.y = parseFloat(document.getElementById('bezierP1y').value);
                        this.p2.x = parseFloat(document.getElementById('bezierP2x').value);
                        this.p2.y = parseFloat(document.getElementById('bezierP2y').value);
                        this.draw();
                        this.updateOutput();
                    });
                }
            });
            
            // Preset buttons
            document.querySelectorAll('.bezier-preset-btn').forEach(btn => {
                btn.addEventListener('click', () => {
                    const values = btn.dataset.bezier.split(',').map(Number);
                    this.p1 = { x: values[0], y: values[1] };
                    this.p2 = { x: values[2], y: values[3] };
                    this.draw();
                    this.updateInputs();
                    this.updateOutput();
                });
            });
        },

        draw() {
            const ctx = this.ctx;
            const w = this.canvas.width;
            const h = this.canvas.height;
            const padding = 20;
            const graphW = w - padding * 2;
            const graphH = h - padding * 2;
            
            // Clear
            ctx.clearRect(0, 0, w, h);
            
            // Background grid
            ctx.strokeStyle = '#333';
            ctx.lineWidth = 1;
            for (let i = 0; i <= 4; i++) {
                const x = padding + (graphW / 4) * i;
                const y = padding + (graphH / 4) * i;
                ctx.beginPath();
                ctx.moveTo(x, padding);
                ctx.lineTo(x, h - padding);
                ctx.stroke();
                ctx.beginPath();
                ctx.moveTo(padding, y);
                ctx.lineTo(w - padding, y);
                ctx.stroke();
            }
            
            // Bezier curve
            ctx.strokeStyle = '#6366f1';
            ctx.lineWidth = 3;
            ctx.beginPath();
            ctx.moveTo(padding, h - padding);
            ctx.bezierCurveTo(
                padding + this.p1.x * graphW,
                h - padding - this.p1.y * graphH,
                padding + this.p2.x * graphW,
                h - padding - this.p2.y * graphH,
                w - padding,
                padding
            );
            ctx.stroke();
            
            // Control lines
            ctx.strokeStyle = 'rgba(255, 255, 255, 0.3)';
            ctx.lineWidth = 1;
            ctx.setLineDash([5, 5]);
            ctx.beginPath();
            ctx.moveTo(padding, h - padding);
            ctx.lineTo(padding + this.p1.x * graphW, h - padding - this.p1.y * graphH);
            ctx.stroke();
            ctx.beginPath();
            ctx.moveTo(w - padding, padding);
            ctx.lineTo(padding + this.p2.x * graphW, h - padding - this.p2.y * graphH);
            ctx.stroke();
            ctx.setLineDash([]);
            
            // Control points
            ctx.fillStyle = '#f472b6';
            ctx.beginPath();
            ctx.arc(padding + this.p1.x * graphW, h - padding - this.p1.y * graphH, 8, 0, Math.PI * 2);
            ctx.fill();
            
            ctx.fillStyle = '#34d399';
            ctx.beginPath();
            ctx.arc(padding + this.p2.x * graphW, h - padding - this.p2.y * graphH, 8, 0, Math.PI * 2);
            ctx.fill();
        },

        onMouseDown(e) {
            const rect = this.canvas.getBoundingClientRect();
            const x = e.clientX - rect.left;
            const y = e.clientY - rect.top;
            const padding = 20;
            const graphW = this.canvas.width - padding * 2;
            const graphH = this.canvas.height - padding * 2;
            
            const p1x = padding + this.p1.x * graphW;
            const p1y = this.canvas.height - padding - this.p1.y * graphH;
            const p2x = padding + this.p2.x * graphW;
            const p2y = this.canvas.height - padding - this.p2.y * graphH;
            
            if (Math.hypot(x - p1x, y - p1y) < 15) {
                this.dragging = 'p1';
            } else if (Math.hypot(x - p2x, y - p2y) < 15) {
                this.dragging = 'p2';
            }
        },

        onMouseMove(e) {
            if (!this.dragging) return;
            
            const rect = this.canvas.getBoundingClientRect();
            const x = e.clientX - rect.left;
            const y = e.clientY - rect.top;
            const padding = 20;
            const graphW = this.canvas.width - padding * 2;
            const graphH = this.canvas.height - padding * 2;
            
            const newX = Math.max(0, Math.min(1, (x - padding) / graphW));
            const newY = Math.max(-0.5, Math.min(1.5, (this.canvas.height - padding - y) / graphH));
            
            if (this.dragging === 'p1') {
                this.p1.x = newX;
                this.p1.y = newY;
            } else {
                this.p2.x = newX;
                this.p2.y = newY;
            }
            
            this.draw();
            this.updateInputs();
            this.updateOutput();
        },

        updateInputs() {
            document.getElementById('bezierP1x').value = this.p1.x.toFixed(2);
            document.getElementById('bezierP1y').value = this.p1.y.toFixed(2);
            document.getElementById('bezierP2x').value = this.p2.x.toFixed(2);
            document.getElementById('bezierP2y').value = this.p2.y.toFixed(2);
        },

        updateOutput() {
            const output = `cubic-bezier(${this.p1.x.toFixed(2)}, ${this.p1.y.toFixed(2)}, ${this.p2.x.toFixed(2)}, ${this.p2.y.toFixed(2)})`;
            document.getElementById('bezierOutput').textContent = output;
        },

        apply() {
            const bezier = `cubic-bezier(${this.p1.x.toFixed(2)}, ${this.p1.y.toFixed(2)}, ${this.p2.x.toFixed(2)}, ${this.p2.y.toFixed(2)})`;
            document.getElementById('animationTimingFunction').value = 'custom';
            
            // Re-apply animation with new timing
            const currentAnim = DOM.previewBox.style.animationName;
            if (currentAnim && currentAnim !== 'none') {
                const duration = document.getElementById('animationDurationRange')?.value || 1;
                const iteration = document.getElementById('animationIterationCount')?.value || '1';
                StyleManager.applyStyle('animation', `${currentAnim} ${duration}s ${bezier} ${iteration}`);
            }
            
            this.closeModal();
            Toast.success('Bezier fonksiyonu uygulandı!');
        },

        closeModal() {
            DOM.bezierModalOverlay.classList.remove('active');
        }
    };

    // ═══════════════════════════════════════════════════════════════════════
    // COMMAND PALETTE
    // ═══════════════════════════════════════════════════════════════════════
    
    const CommandPalette = {
        commands: [
            { name: 'Neon Tema', action: () => ThemePresets.apply('auto-theme-neon'), icon: 'fa-lightbulb', category: 'Tema' },
            { name: 'Cyberpunk Tema', action: () => ThemePresets.apply('auto-theme-cyberpunk'), icon: 'fa-robot', category: 'Tema' },
            { name: 'Minimal Tema', action: () => ThemePresets.apply('auto-theme-minimal'), icon: 'fa-compress', category: 'Tema' },
            { name: 'Glass Tema', action: () => ThemePresets.apply('auto-theme-glassmorphism'), icon: 'fa-glass-whiskey', category: 'Tema' },
            { name: 'Rastgele Font', action: () => RandomStyles.font(), icon: 'fa-font', category: 'Rastgele' },
            { name: 'Rastgele Renk', action: () => RandomStyles.color(), icon: 'fa-palette', category: 'Rastgele' },
            { name: 'Rastgele Gradyan', action: () => RandomStyles.gradient(), icon: 'fa-grip-lines', category: 'Rastgele' },
            { name: 'Rastgele Animasyon', action: () => AnimationManager.randomAnimation(), icon: 'fa-play', category: 'Rastgele' },
            { name: 'Kaos Oluştur', action: () => ChaosEngine.generate(false), icon: 'fa-wand-magic-sparkles', category: 'Kaos' },
            { name: 'Maksimum Kaos', action: () => ChaosEngine.generate(true), icon: 'fa-explosion', category: 'Kaos' },
            { name: 'Tümünü Sıfırla', action: () => StyleManager.resetAll(), icon: 'fa-trash-restore', category: 'Genel' },
            { name: 'CSS Kopyala', action: () => Actions.copyCss(), icon: 'fa-copy', category: 'Çıktı' },
            { name: 'CSS İndir', action: () => Actions.downloadCss(), icon: 'fa-download', category: 'Çıktı' },
            { name: 'Geri Al', action: () => History.undo(), icon: 'fa-undo-alt', category: 'Genel' },
            { name: 'İleri Al', action: () => History.redo(), icon: 'fa-redo-alt', category: 'Genel' },
            { name: 'Animasyonu Durdur', action: () => AnimationManager.stopAnimation(), icon: 'fa-stop', category: 'Animasyon' },
            { name: 'Filtreleri Sıfırla', action: () => FilterManager.resetFilters(), icon: 'fa-filter', category: 'Filtre' },
            { name: 'Dönüşümleri Sıfırla', action: () => TransformManager.reset(), icon: 'fa-cube', category: 'Dönüşüm' }
        ],
        selectedIndex: 0,

        open() {
            DOM.commandPaletteOverlay.classList.add('active');
            DOM.commandPaletteInput.value = '';
            DOM.commandPaletteInput.focus();
            this.selectedIndex = 0;
            this.render(this.commands);
        },

        close() {
            DOM.commandPaletteOverlay.classList.remove('active');
        },

        filter(query) {
            const filtered = this.commands.filter(cmd => 
                cmd.name.toLowerCase().includes(query.toLowerCase()) ||
                cmd.category.toLowerCase().includes(query.toLowerCase())
            );
            this.selectedIndex = 0;
            this.render(filtered);
        },

        render(cmds) {
            DOM.commandPaletteResults.innerHTML = cmds.map((cmd, i) => `
                <button class="command-item ${i === this.selectedIndex ? 'selected' : ''}" data-index="${i}">
                    <i class="fas ${cmd.icon}"></i>
                    <span class="command-name">${cmd.name}</span>
                    <span class="command-category">${cmd.category}</span>
                </button>
            `).join('');
            
            DOM.commandPaletteResults.querySelectorAll('.command-item').forEach((item, i) => {
                item.addEventListener('click', () => {
                    cmds[i].action();
                    this.close();
                });
            });
        },

        navigate(direction) {
            const items = DOM.commandPaletteResults.querySelectorAll('.command-item');
            if (items.length === 0) return;
            
            items[this.selectedIndex]?.classList.remove('selected');
            
            if (direction === 'up') {
                this.selectedIndex = this.selectedIndex > 0 ? this.selectedIndex - 1 : items.length - 1;
            } else {
                this.selectedIndex = this.selectedIndex < items.length - 1 ? this.selectedIndex + 1 : 0;
            }
            
            items[this.selectedIndex]?.classList.add('selected');
            items[this.selectedIndex]?.scrollIntoView({ block: 'nearest' });
        },

        execute() {
            const items = DOM.commandPaletteResults.querySelectorAll('.command-item');
            if (items[this.selectedIndex]) {
                items[this.selected

### Claude Sonnet 4.6
*2026-03-06 20:06:55 +03*

# K3N4N CSS Generator V7.0 — Full JavaScript

Bu proje oldukça büyük olduğundan, önce CSS kodunu da paylaşmanı öneririm — ama JS'i şimdi yazıyorum. Tüm panelleri, animasyonları, renk seçicileri, kaos motorunu, undo/redo sistemini, klavye kısayollarını ve çıktı sekmelerini kapsayacak şekilde yazacağım.

```javascript
/* ═══════════════════════════════════════════════════════════════════════
   K3N4N CSS Generator V7.0 — script.js
   FULL FEATURE JAVASCRIPT
═══════════════════════════════════════════════════════════════════════ */

'use strict';

/* ─────────────────────────────────────────────────────────────────────
   1. GLOBAL STATE
───────────────────────────────────────────────────────────────────── */
const STATE = {
  // Core styles
  styles: {
    fontFamily: "'Poppins', sans-serif",
    fontSize: '30px',
    fontWeight: '400',
    fontStyle: 'normal',
    color: '#ffffff',
    textAlign: 'center',
    lineHeight: '1.5',
    letterSpacing: '0px',
    wordSpacing: '0px',
    textTransform: 'none',
    textDecorationLine: 'none',
    textDecorationStyle: 'solid',
    textDecorationColor: '#ffffff',
    textOverflow: 'clip',
    writingMode: 'horizontal-tb',
    opacity: '1',
    padding: '0px 0px 0px 0px',
    // Background
    backgroundColor: '#111111',
    backgroundImage: 'none',
    backgroundSize: 'auto',
    backgroundPosition: 'center center',
    backgroundRepeat: 'no-repeat',
    backgroundBlendMode: 'normal',
    // Border
    border: 'none',
    borderTopLeftRadius: '10px',
    borderTopRightRadius: '10px',
    borderBottomLeftRadius: '10px',
    borderBottomRightRadius: '10px',
    outline: 'none',
    outlineOffset: '0px',
    // Transform
    transform: 'none',
    transformOrigin: 'center center',
    // Shadow
    boxShadow: 'none',
    // Animation
    animationName: 'none',
    animationDuration: '1s',
    animationDelay: '0s',
    animationTimingFunction: 'ease',
    animationIterationCount: '1',
    animationDirection: 'normal',
    animationFillMode: 'none',
    animationPlayState: 'running',
    transition: 'all 0.3s ease',
    // Filter
    filter: 'none',
    backdropFilter: 'none',
    // Layout
    display: 'flex',
    justifyContent: 'center',
    alignItems: 'center',
    overflow: 'hidden',
    width: '100%',
    height: '200px',
    // Misc
    cursor: 'auto',
    mixBlendMode: 'normal',
    clipPath: 'none',
  },

  // Multi-layer shadows
  boxShadowLayers: [],
  textShadowLayers: [],

  // Gradient bg
  gradientColors: [
    { color: '#667eea', stop: 0 },
    { color: '#764ba2', stop: 100 },
  ],
  gradientType: 'linear',
  gradientAngle: 90,

  // Text gradient
  textGradientColors: [
    { color: '#ff6b9d', stop: 0 },
    { color: '#c44dff', stop: 50 },
    { color: '#4df0ff', stop: 100 },
  ],
  textGradientType: 'linear',
  textGradientAngle: 90,
  textGradientActive: false,

  // Gradient border
  gradientBorderColors: [
    { color: '#ff6b9d', stop: 0 },
    { color: '#4df0ff', stop: 100 },
  ],
  gradientBorderWidth: 2,

  // Text stroke
  textStrokeWidth: 0,
  textStrokeColor: '#ffffff',

  // Transform components
  transformRotate: 0,
  transformScaleX: 1,
  transformScaleY: 1,
  transformSkewX: 0,
  transformSkewY: 0,
  transformTranslateX: 0,
  transformTranslateY: 0,
  transformRotateX: 0,
  transformRotateY: 0,
  transformRotateZ: 0,
  transformPerspective: 0,

  // Filter components
  filterBlur: 0,
  filterBrightness: 100,
  filterContrast: 100,
  filterSaturate: 100,
  filterHueRotate: 0,
  filterInvert: 0,
  filterSepia: 0,
  filterGrayscale: 0,
  dropShadowX: 0,
  dropShadowY: 0,
  dropShadowBlur: 0,
  dropShadowColor: '#000000',
  backdropBlur: 0,

  // Palette
  paletteBaseColor: '#667eea',
  paletteType: 'monochromatic',
  paletteSize: 5,
  palette: [],

  // Pseudo elements
  beforeContent: '',
  beforeTop: 'auto',
  beforeLeft: 'auto',
  beforeColor: '#ffffff',
  beforeFontSize: '1em',
  afterContent: '',
  afterTop: 'auto',
  afterRight: 'auto',
  afterColor: '#ffffff',
  afterFontSize: '1em',

  // Custom keyframes
  customKeyframes: '',

  // Preview
  previewText: 'K3N4N V7.0',
  previewSize: 'desktop',
  previewBgDark: true,
  rulerVisible: false,
  gridVisible: false,

  // Undo/Redo
  history: [],
  historyIndex: -1,
  maxHistory: 50,

  // Auto-play chaos
  autoPlayTimer: null,
  autoPlayInterval: 3,

  // Bezier
  bezierValues: [0.25, 0.46, 0.45, 0.94],

  // Theme
  appTheme: 'dark',

  // Active background mode
  activeBgTab: 'bg-solid',
};

/* ─────────────────────────────────────────────────────────────────────
   2. ANIMATION KEYFRAMES LIBRARY
───────────────────────────────────────────────────────────────────── */
const KEYFRAMES = {
  bounce: `@keyframes bounce {
  0%, 20%, 50%, 80%, 100% { transform: translateY(0); }
  40% { transform: translateY(-30px); }
  60% { transform: translateY(-15px); }
}`,
  pulse: `@keyframes pulse {
  0%, 100% { transform: scale(1); }
  50% { transform: scale(1.08); }
}`,
  fadeIn: `@keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}`,
  fadeOut: `@keyframes fadeOut {
  from { opacity: 1; }
  to { opacity: 0; }
}`,
  slideInLeft: `@keyframes slideInLeft {
  from { transform: translateX(-100px); opacity: 0; }
  to { transform: translateX(0); opacity: 1; }
}`,
  slideInRight: `@keyframes slideInRight {
  from { transform: translateX(100px); opacity: 0; }
  to { transform: translateX(0); opacity: 1; }
}`,
  slideInUp: `@keyframes slideInUp {
  from { transform: translateY(60px); opacity: 0; }
  to { transform: translateY(0); opacity: 1; }
}`,
  slideInDown: `@keyframes slideInDown {
  from { transform: translateY(-60px); opacity: 0; }
  to { transform: translateY(0); opacity: 1; }
}`,
  shake: `@keyframes shake {
  0%, 100% { transform: translateX(0); }
  10%, 30%, 50%, 70%, 90% { transform: translateX(-8px); }
  20%, 40%, 60%, 80% { transform: translateX(8px); }
}`,
  swing: `@keyframes swing {
  20% { transform: rotate3d(0,0,1,15deg); }
  40% { transform: rotate3d(0,0,1,-10deg); }
  60% { transform: rotate3d(0,0,1,5deg); }
  80% { transform: rotate3d(0,0,1,-5deg); }
  100% { transform: rotate3d(0,0,1,0deg); }
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
  0%, 100% { transform: skewX(0deg) skewY(0deg); }
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
  wobble: `@keyframes wobble {
  0% { transform: translateX(0); }
  15% { transform: translateX(-25px) rotate(-5deg); }
  30% { transform: translateX(20px) rotate(3deg); }
  45% { transform: translateX(-15px) rotate(-3deg); }
  60% { transform: translateX(10px) rotate(2deg); }
  75% { transform: translateX(-5px) rotate(-1deg); }
  100% { transform: translateX(0); }
}`,
  tada: `@keyframes tada {
  0% { transform: scaleX(1); }
  10%, 20% { transform: scale3d(0.9,0.9,0.9) rotate(-3deg); }
  30%, 50%, 70%, 90% { transform: scale3d(1.1,1.1,1.1) rotate(3deg); }
  40%, 60%, 80% { transform: scale3d(1.1,1.1,1.1) rotate(-3deg); }
  100% { transform: scaleX(1); }
}`,
  headShake: `@keyframes headShake {
  0% { transform: translateX(0); }
  6.5% { transform: translateX(-6px) rotateY(-9deg); }
  18.5% { transform: translateX(5px) rotateY(7deg); }
  31.5% { transform: translateX(-3px) rotateY(-5deg); }
  43.5% { transform: translateX(2px) rotateY(3deg); }
  50% { transform: translateX(0); }
}`,
  flip: `@keyframes flip {
  0% { transform: perspective(400px) rotateY(-1turn); }
  40% { transform: perspective(400px) rotateY(-190deg); }
  50% { transform: perspective(400px) rotateY(-170deg); }
  80% { transform: perspective(400px) scale3d(0.95,0.95,0.95) rotateY(0deg); }
  100% { transform: perspective(400px) scale3d(1,1,1) rotateY(0deg); }
}`,
  flipInX: `@keyframes flipInX {
  0% { transform: perspective(400px) rotateX(90deg); opacity: 0; }
  40% { transform: perspective(400px) rotateX(-20deg); }
  60% { transform: perspective(400px) rotateX(10deg); opacity: 1; }
  80% { transform: perspective(400px) rotateX(-5deg); }
  100% { transform: perspective(400px); }
}`,
  flipInY: `@keyframes flipInY {
  0% { transform: perspective(400px) rotateY(90deg); opacity: 0; }
  40% { transform: perspective(400px) rotateY(-20deg); }
  60% { transform: perspective(400px) rotateY(10deg); opacity: 1; }
  80% { transform: perspective(400px) rotateY(-5deg); }
  100% { transform: perspective(400px); }
}`,
  rotateIn: `@keyframes rotateIn {
  0% { transform-origin: center; transform: rotate(-200deg); opacity: 0; }
  100% { transform-origin: center; transform: none; opacity: 1; }
}`,
  zoomIn: `@keyframes zoomIn {
  0% { opacity: 0; transform: scale3d(0.3,0.3,0.3); }
  50% { opacity: 1; }
}`,
  zoomOut: `@keyframes zoomOut {
  0% { opacity: 1; }
  50% { opacity: 0; transform: scale3d(0.3,0.3,0.3); }
  100% { opacity: 0; }
}`,
  rollIn: `@keyframes rollIn {
  0% { opacity: 0; transform: translate3d(-100%,0,0) rotate(-120deg); }
  100% { opacity: 1; transform: none; }
}`,
  lightSpeedIn: `@keyframes lightSpeedIn {
  0% { transform: translate3d(100%,0,0) skewX(-30deg); opacity: 0; }
  60% { transform: skewX(20deg); opacity: 1; }
  80% { transform: skewX(-5deg); }
  100% { transform: none; }
}`,
  float: `@keyframes float {
  0%, 100% { transform: translateY(0px); }
  50% { transform: translateY(-20px); }
}`,
  glitch: `@keyframes glitch {
  0% { text-shadow: 2px 0 #ff0000, -2px 0 #00ffff; }
  20% { text-shadow: -2px 0 #ff0000, 2px 0 #00ffff; clip-path: polygon(0 30%, 100% 30%, 100% 40%, 0 40%); transform: translate(-2px, 0); }
  40% { text-shadow: 2px 0 #ff0000, -2px 0 #00ffff; clip-path: polygon(0 60%, 100% 60%, 100% 70%, 0 70%); transform: translate(2px, 0); }
  60% { text-shadow: -2px 0 #ff0000, 2px 0 #00ffff; clip-path: none; transform: translate(0); }
  80% { text-shadow: 2px 0 #ff0000, -2px 0 #00ffff; transform: translate(1px, -1px); }
  100% { text-shadow: none; transform: none; }
}`,
  neonPulse: `@keyframes neonPulse {
  0%, 100% { text-shadow: 0 0 5px #fff, 0 0 10px #fff, 0 0 20px #0ff, 0 0 40px #0ff, 0 0 80px #0ff; }
  50% { text-shadow: 0 0 2px #fff, 0 0 5px #0ff, 0 0 10px #0ff; }
}`,
  typewriter: `@keyframes typewriter {
  from { width: 0; }
  to { width: 100%; }
}`,
  colorWave: `@keyframes colorWave {
  0% { color: #ff0000; }
  14% { color: #ff7700; }
  28% { color: #ffff00; }
  42% { color: #00ff00; }
  56% { color: #0000ff; }
  70% { color: #8b00ff; }
  85% { color: #ff00ff; }
  100% { color: #ff0000; }
}`,
  morphShape: `@keyframes morphShape {
  0%, 100% { border-radius: 10px; }
  25% { border-radius: 50% 10px 50% 10px; }
  50% { border-radius: 50%; }
  75% { border-radius: 10px 50% 10px 50%; }
}`,
  liquidWave: `@keyframes liquidWave {
  0%, 100% { border-radius: 60% 40% 30% 70% / 60% 30% 70% 40%; }
  50% { border-radius: 30% 60% 70% 40% / 50% 60% 30% 60%; }
}`,
  matrix: `@keyframes matrix {
  0% { color: #00ff41; text-shadow: 0 0 5px #00ff41; }
  50% { color: #00cc33; text-shadow: 0 0 20px #00ff41, 0 0 40px #00ff41; }
  100% { color: #00ff41; text-shadow: 0 0 5px #00ff41; }
}`,
  fire: `@keyframes fire {
  0%, 100% { text-shadow: 0 0 5px #ff4500, 0 0 10px #ff6b00, 0 0 20px #ffaa00; color: #ffaa00; }
  33% { text-shadow: 0 0 8px #ff0000, 0 0 15px #ff4500, 0 0 30px #ff6b00; color: #ff6b00; }
  66% { text-shadow: 0 0 5px #ffcc00, 0 0 10px #ff8800, 0 0 20px #ff4500; color: #ffcc00; }
}`,
  electric: `@keyframes electric {
  0%, 100% { text-shadow: 0 0 5px #fff, 0 0 10px #e6f, 0 0 20px #e6f, 0 0 40px #e6f; }
  25% { text-shadow: 0 0 3px #fff, 0 0 6px #a0f, 0 0 12px #a0f; transform: skewX(1deg); }
  50% { text-shadow: 0 0 8px #fff, 0 0 15px #e6f, 0 0 30px #e6f, 0 0 60px #a0f; }
  75% { text-shadow: 0 0 2px #fff, 0 0 5px #e6f; transform: skewX(-1deg); }
}`,
};

/* ─────────────────────────────────────────────────────────────────────
   3. PRESET THEMES
───────────────────────────────────────────────────────────────────── */
const THEMES = {
  'auto-theme-neon': {
    color: '#0ff',
    backgroundColor: '#0a0a2e',
    backgroundImage: 'none',
    fontFamily: "'Orbitron', sans-serif",
    fontWeight: '700',
    fontSize: '36px',
    boxShadow: '0 0 30px rgba(0,255,255,0.5)',
    textShadow: '0 0 10px #0ff, 0 0 20px #0ff, 0 0 40px #0ff',
    borderRadius: '10px',
    border: '1px solid rgba(0,255,255,0.3)',
  },
  'auto-theme-cyberpunk': {
    color: '#ff2d6a',
    backgroundColor: '#0d0221',
    backgroundImage: 'none',
    fontFamily: "'Bebas Neue', sans-serif",
    fontWeight: '400',
    fontSize: '48px',
    letterSpacing: '4px',
    textTransform: 'uppercase',
    boxShadow: '5px 5px 0 #ff2d6a, 10px 10px 0 rgba(255,45,106,0.3)',
    border: '2px solid #ff2d6a',
    borderRadius: '0px',
  },
  'auto-theme-dark-elegant': {
    color: '#d4af37',
    backgroundColor: '#1a1a2e',
    backgroundImage: 'none',
    fontFamily: "'Cinzel', serif",
    fontWeight: '700',
    fontSize: '34px',
    letterSpacing: '6px',
    textTransform: 'uppercase',
    boxShadow: '0 10px 40px rgba(212,175,55,0.2)',
    border: '1px solid rgba(212,175,55,0.3)',
    borderRadius: '4px',
  },
  'auto-theme-matrix': {
    color: '#00ff41',
    backgroundColor: '#0d0208',
    backgroundImage: 'none',
    fontFamily: "'VT323', monospace",
    fontWeight: '400',
    fontSize: '42px',
    textShadow: '0 0 10px #00ff41',
    boxShadow: 'inset 0 0 60px rgba(0,255,65,0.1)',
    border: '1px solid rgba(0,255,65,0.3)',
    borderRadius: '2px',
    animationName: 'matrix',
    animationDuration: '2s',
    animationIterationCount: 'infinite',
  },
  'auto-theme-minimal': {
    color: '#333333',
    backgroundColor: '#fafafa',
    backgroundImage: 'none',
    fontFamily: "'Inter', sans-serif",
    fontWeight: '300',
    fontSize: '28px',
    letterSpacing: '2px',
    boxShadow: 'none',
    border: 'none',
    borderRadius: '0px',
  },
  'auto-theme-vintage': {
    color: '#5c3317',
    backgroundColor: '#f4e9d8',
    backgroundImage: 'none',
    fontFamily: "'Playfair Display', serif",
    fontWeight: '700',
    fontStyle: 'italic',
    fontSize: '32px',
    textShadow: '1px 1px 2px rgba(0,0,0,0.2)',
    border: '2px solid #c4a882',
    borderRadius: '4px',
    boxShadow: '4px 4px 0 rgba(92,51,23,0.15)',
    filter: 'sepia(20%)',
  },
  'auto-theme-pastel': {
    color: '#8b5cf6',
    backgroundColor: '#fff0f5',
    backgroundImage: 'linear-gradient(135deg, #fff0f5 0%, #fce4ff 100%)',
    fontFamily: "'Nunito', sans-serif",
    fontWeight: '800',
    fontSize: '32px',
    border: '2px solid #c9a0dc',
    borderRadius: '20px',
    boxShadow: '0 8px 32px rgba(201,160,220,0.4)',
  },
  'auto-theme-glassmorphism': {
    color: '#ffffff',
    backgroundColor: 'rgba(255,255,255,0.1)',
    backgroundImage: 'none',
    fontFamily: "'Poppins', sans-serif",
    fontWeight: '600',
    fontSize: '30px',
    border: '1px solid rgba(255,255,255,0.3)',
    borderRadius: '16px',
    boxShadow: '0 8px 32px rgba(0,0,0,0.3)',
    backdropFilter: 'blur(10px)',
    WebkitBackdropFilter: 'blur(10px)',
  },
  'auto-theme-neumorphism': {
    color: '#6b7b99',
    backgroundColor: '#e0e5ec',
    backgroundImage: 'none',
    fontFamily: "'Poppins', sans-serif",
    fontWeight: '600',
    fontSize: '28px',
    border: 'none',
    borderRadius: '20px',
    boxShadow: '8px 8px 16px #b8bec7, -8px -8px 16px #ffffff',
  },
  'auto-theme-aurora': {
    color: '#ffffff',
    backgroundColor: '#141e30',
    backgroundImage: 'linear-gradient(135deg, #141e30 0%, #243b55 50%, #141e30 100%)',
    fontFamily: "'Space Grotesk', sans-serif",
    fontWeight: '700',
    fontSize: '32px',
    textShadow: '0 0 20px rgba(168,255,120,0.8)',
    border: '1px solid rgba(168,255,120,0.3)',
    borderRadius: '12px',
    boxShadow: '0 0 40px rgba(168,255,120,0.2)',
  },
  'auto-theme-holographic': {
    color: '#ff6ec7',
    backgroundColor: '#1a1a2e',
    backgroundImage: 'linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%)',
    fontFamily: "'Orbitron', sans-serif",
    fontWeight: '700',
    fontSize: '30px',
    letterSpacing: '4px',
    textTransform: 'uppercase',
    textShadow: '0 0 10px #ff6ec7, 0 0 20px #a855f7',
    border: '1px solid rgba(255,110,199,0.4)',
    borderRadius: '8px',
    boxShadow: '0 0 30px rgba(255,110,199,0.3)',
    animationName: 'colorWave',
    animationDuration: '3s',
    animationIterationCount: 'infinite',
  },
  'auto-theme-nature': {
    color: '#2d5016',
    backgroundColor: '#e8f5e9',
    backgroundImage: 'linear-gradient(135deg, #e8f5e9 0%, #c8e6c9 100%)',
    fontFamily: "'Nunito', sans-serif",
    fontWeight: '700',
    fontSize: '30px',
    border: '2px solid #a5d6a7',
    borderRadius: '50px',
    boxShadow: '0 8px 24px rgba(45,80,22,0.2)',
  },
  'auto-theme-ocean': {
    color: '#ffffff',
    backgroundColor: '#0077b6',
    backgroundImage: 'linear-gradient(180deg, #0077b6 0%, #023e8a 100%)',
    fontFamily: "'Raleway', sans-serif",
    fontWeight: '700',
    fontSize: '32px',
    letterSpacing: '3px',
    textTransform: 'uppercase',
    border: '2px solid rgba(255,255,255,0.3)',
    borderRadius: '12px',
    boxShadow: '0 10px 40px rgba(0,119,182,0.5)',
  },
  'auto-theme-sunset': {
    color: '#ffffff',
    backgroundColor: '#ff6b35',
    backgroundImage: 'linear-gradient(135deg, #ff6b35 0%, #ff8e53 25%, #ff6b9d 75%, #c44dff 100%)',
    fontFamily: "'Pacifico', cursive",
    fontWeight: '400',
    fontSize: '32px',
    border: 'none',
    borderRadius: '16px',
    textShadow: '2px 2px 8px rgba(0,0,0,0.3)',
    boxShadow: '0 15px 40px rgba(255,107,53,0.4)',
  },
  'auto-theme-forest': {
    color: '#a8e6cf',
    backgroundColor: '#1a3a1a',
    backgroundImage: 'radial-gradient(circle at 50% 50%, #2d5a2d 0%, #1a3a1a 70%)',
    fontFamily: "'Cinzel', serif",
    fontWeight: '700',
    fontSize: '30px',
    letterSpacing: '5px',
    textShadow: '0 0 20px rgba(168,230,207,0.5)',
    border: '1px solid rgba(168,230,207,0.3)',
    borderRadius: '4px',
    boxShadow: '0 0 40px rgba(45,90,45,0.8)',
  },
  'auto-theme-candy': {
    color: '#ff6b9d',
    backgroundColor: '#fff0f5',
    backgroundImage: 'linear-gradient(135deg, #fff0f5 0%, #ffe4f0 100%)',
    fontFamily: "'Dancing Script', cursive",
    fontWeight: '700',
    fontSize: '42px',
    textShadow: '2px 2px 0 rgba(255,107,157,0.3)',
    border: '3px solid #ffb3cc',
    borderRadius: '50% 10px',
    boxShadow: '0 8px 24px rgba(255,107,157,0.3)',
  },
  'auto-theme-retrowave': {
    color: '#ff71ce',
    backgroundColor: '#030014',
    backgroundImage: 'linear-gradient(180deg, #030014 60%, #0d0030 100%)',
    fontFamily: "'Orbitron', sans-serif",
    fontWeight: '900',
    fontSize: '28px',
    letterSpacing: '6px',
    textTransform: 'uppercase',
    textShadow: '0 0 10px #ff71ce, 0 0 20px #b967ff',
    border: '1px solid #01cdfe',
    borderRadius: '2px',
    boxShadow: '0 0 40px rgba(185,103,255,0.4), inset 0 0 40px rgba(255,113,206,0.05)',
    animationName: 'neonPulse',
    animationDuration: '2s',
    animationIterationCount: 'infinite',
  },
  'auto-theme-brutalist': {
    color: '#000000',
    backgroundColor: '#ffff00',
    backgroundImage: 'none',
    fontFamily: "'Bebas Neue', sans-serif",
    fontWeight: '400',
    fontSize: '48px',
    letterSpacing: '8px',
    textTransform: 'uppercase',
    border: '4px solid #000000',
    borderRadius: '0px',
    boxShadow: '6px 6px 0 #000000',
    textShadow: 'none',
  },
  'auto-theme-lofi': {
    color: '#8b7355',
    backgroundColor: '#f5f0e8',
    backgroundImage: 'none',
    fontFamily: "'Kaushan Script', cursive",
    fontWeight: '400',
    fontSize: '36px',
    textShadow: '1px 1px 2px rgba(0,0,0,0.1)',
    border: '2px solid #d4a5a5',
    borderRadius: '12px',
    boxShadow: '4px 4px 16px rgba(139,115,85,0.2)',
    filter: 'sepia(10%)',
  },
  'auto-theme-paper': {
    color: '#444444',
    backgroundColor: '#f5f0e8',
    backgroundImage: 'none',
    fontFamily: "'Playfair Display', serif",
    fontWeight: '400',
    fontSize: '30px',
    lineHeight: '1.8',
    letterSpacing: '1px',
    border: '1px solid #d4c5a9',
    borderRadius: '2px',
    boxShadow: '2px 2px 8px rgba(0,0,0,0.1), -2px -2px 8px rgba(255,255,255,0.8)',
  },
};

/* ─────────────────────────────────────────────────────────────────────
   4. CSS PATTERN LIBRARY
───────────────────────────────────────────────────────────────────── */
const PATTERNS = [
  { name: 'Polka Dot', css: 'radial-gradient(circle, rgba(255,255,255,0.15) 2px, transparent 2px)', size: '20px 20px' },
  { name: 'Çizgili', css: 'repeating-linear-gradient(90deg, transparent, transparent 10px, rgba(255,255,255,0.05) 10px, rgba(255,255,255,0.05) 11px)', size: 'auto' },
  { name: 'Dikey Çizgi', css: 'repeating-linear-gradient(0deg, transparent, transparent 10px, rgba(255,255,255,0.05) 10px, rgba(255,255,255,0.05) 11px)', size: 'auto' },
  { name: 'Kareler', css: 'linear-gradient(rgba(255,255,255,0.05) 1px, transparent 1px), linear-gradient(90deg, rgba(255,255,255,0.05) 1px, transparent 1px)', size: '20px 20px' },
  { name: 'Baklava', css: 'linear-gradient(45deg, rgba(255,255,255,0.05) 25%, transparent 25%), linear-gradient(-45deg, rgba(255,255,255,0.05) 25%, transparent 25%), linear-gradient(45deg, transparent 75%, rgba(255,255,255,0.05) 75%), linear-gradient(-45deg, transparent 75%, rgba(255,255,255,0.05) 75%)', size: '20px 20px' },
  { name: 'Üçgenler', css: 'linear-gradient(135deg, rgba(255,255,255,0.05) 25%, transparent 25%) -10px 0, linear-gradient(225deg, rgba(255,255,255,0.05) 25%, transparent 25%) -10px 0, linear-gradient(315deg, rgba(255,255,255,0.05) 25%, transparent 25%), linear-gradient(45deg, rgba(255,255,255,0.05) 25%, transparent 25%)', size: '20px 20px' },
  { name: 'Balık Pulu', css: 'radial-gradient(circle at 100% 150%, rgba(255,255,255,0.05) 24%, white 25%, white 28%, rgba(255,255,255,0.05) 29%, rgba(255,255,255,0.05) 36%, white 36%, white 40%, transparent 40%, transparent), radial-gradient(circle at 0 150%, rgba(255,255,255,0.05) 24%, white 25%, white 28%, rgba(255,255,255,0.05) 29%, rgba(255,255,255,0.05) 36%, white 36%, white 40%, transparent 40%, transparent)', size: '30px 30px' },
  { name: 'Dalga', css: 'repeating-radial-gradient(circle at 0 0, transparent 0, rgba(255,255,255,0.03) 10px), repeating-linear-gradient(rgba(255,255,255,0.05), rgba(255,255,255,0.05))', size: 'auto' },
];

/* ─────────────────────────────────────────────────────────────────────
   5. CLIP PATH SHAPES
───────────────────────────────────────────────────────────────────── */
const CLIP_SHAPES = [
  { name: 'Normal', value: 'none', preview: '▬' },
  { name: 'Daire', value: 'circle(50%)', preview: '●' },
  { name: 'Elips', value: 'ellipse(60% 40% at 50% 50%)', preview: '⬭' },
  { name: 'Üçgen ↑', value: 'polygon(50% 0%, 0% 100%, 100% 100%)', preview: '▲' },
  { name: 'Üçgen ↓', value: 'polygon(0 0, 100% 0, 50% 100%)', preview: '▼' },
  { name: 'Eşkenar', value: 'polygon(50% 0%, 100% 25%, 100% 75%, 50% 100%, 0% 75%, 0% 25%)', preview: '⬡' },
  { name: 'Pentagon', value: 'polygon(50% 0%, 100% 38%, 82% 100%, 18% 100%, 0% 38%)', preview: '⬠' },
  { name: 'Yıldız', value: 'polygon(50% 0%, 61% 35%, 98% 35%, 68% 57%, 79% 91%, 50% 70%, 21% 91%, 32% 57%, 2% 35%, 39% 35%)', preview: '★' },
  { name: 'Çarpı', value: 'polygon(20% 0%, 80% 0%, 80% 20%, 100% 20%, 100% 80%, 80% 80%, 80% 100%, 20% 100%, 20% 80%, 0% 80%, 0% 20%, 20% 20%)', preview: '✛' },
  { name: 'Ok →', value: 'polygon(0% 20%, 60% 20%, 60% 0%, 100% 50%, 60% 100%, 60% 80%, 0% 80%)', preview: '➤' },
  { name: 'Ok ←', value: 'polygon(40% 0%, 40% 20%, 100% 20%, 100% 80%, 40% 80%, 40% 100%, 0% 50%)', preview: '◄' },
  { name: 'Elmas', value: 'polygon(50% 0%, 100% 50%, 50% 100%, 0% 50%)', preview: '◆' },
  { name: 'Trapez', value: 'polygon(20% 0%, 80% 0%, 100% 100%, 0% 100%)', preview: '⏢' },
  { name: 'Sol Eğri', value: 'polygon(0 0, 100% 0, 100% 100%, 0 80%)', preview: '◿' },
  { name: 'Sağ Eğri', value: 'polygon(0 0, 100% 0, 100% 80%, 0 100%)', preview: '◺' },
  { name: 'Mesaj', value: 'polygon(0% 0%, 100% 0%, 100% 75%, 75% 75%, 75% 100%, 50% 75%, 0% 75%)', preview: '💬' },
];

/* ─────────────────────────────────────────────────────────────────────
   6. RANDOM TEXT SAMPLES
───────────────────────────────────────────────────────────────────── */
const RANDOM_TEXTS = [
  'K3N4N V7.0', 'CSS MAGIC', 'HELLO WORLD', 'STYLE IT!',
  '🎨 DESIGN', 'NEON GLOW', 'CYBER 2077', 'PIXEL PERFECT',
  'WEB ART', '✨ CREATIVE', 'DARK MODE', 'GRADIENT',
  'ANIMATION', 'MORPHING', 'GLITCH ART', 'TYPOGRAPHY',
  'BOLD MOVE', 'ULTRA PRO', 'CHAOS!', '🔥 FIRE',
];

/* ─────────────────────────────────────────────────────────────────────
   7. UTILITY FUNCTIONS
───────────────────────────────────────────────────────────────────── */
const $ = (id) => document.getElementById(id);
const $$ = (sel, ctx = document) => ctx.querySelectorAll(sel);
const rand = (min, max) => Math.random() * (max - min) + min;
const randInt = (min, max) => Math.floor(rand(min, max + 1));
const randPick = (arr) => arr[randInt(0, arr.length - 1)];
const clamp = (val, min, max) => Math.max(min, Math.min(max, val));
const hexToRgb = (hex) => {
  const r = /^#?([a-f\d]{2})([a-f\d]{2})([a-f\d]{2})$/i.exec(hex);
  return r ? { r: parseInt(r[1], 16), g: parseInt(r[2], 16), b: parseInt(r[3], 16) } : null;
};
const randomHex = () => '#' + Math.floor(Math.random() * 0xffffff).toString(16).padStart(6, '0');

function randGradientCss() {
  const c1 = randomHex(), c2 = randomHex(), c3 = randomHex();
  const angle = randInt(0, 360);
  return `linear-gradient(${angle}deg, ${c1}, ${c2}, ${c3})`;
}

function showToast(msg, type = 'success', duration = 2800) {
  const container = $('toastContainer');
  const toast = document.createElement('div');
  toast.className = `toast toast-${type}`;
  const icons = { success: 'check-circle', error: 'times-circle', info: 'info-circle', warning: 'exclamation-triangle' };
  toast.innerHTML = `<i class="fas fa-${icons[type] || 'info-circle'}"></i><span>${msg}</span>`;
  container.appendChild(toast);
  requestAnimationFrame(() => toast.classList.add('show'));
  setTimeout(() => {
    toast.classList.remove('show');
    setTimeout(() => toast.remove(), 400);
  }, duration);
}

function escapeHtml(str) {
  return str.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
}

/* ─────────────────────────────────────────────────────────────────────
   8. COLOR PICKERS (iro.js)
───────────────────────────────────────────────────────────────────── */
const COLOR_PICKERS = {};

function createColorPicker(containerId, initialColor, onChange) {
  const container = document.getElementById(containerId);
  if (!container) return null;
  container.innerHTML = '';

  try {
    const picker = new iro.ColorPicker(container, {
      width: 180,
      color: initialColor || '#ffffff',
      borderWidth: 1,
      borderColor: 'rgba(255,255,255,0.1)',
      layout: [
        { component: iro.ui.Wheel },
        { component: iro.ui.Slider, options: { sliderType: 'value' } },
        { component: iro.ui.Slider, options: { sliderType: 'alpha' } },
      ],
    });
    picker.on('color:change', (color) => {
      if (onChange) onChange(color.hex8String || color.hexString);
    });
    COLOR_PICKERS[containerId] = picker;
    return picker;
  } catch (e) {
    // Fallback if iro.js fails
    const input = document.createElement('input');
    input.type = 'color';
    input.value = initialColor || '#ffffff';
    input.style.cssText = 'width:100%;height:40px;cursor:pointer;border:none;border-radius:8px;';
    input.addEventListener('input', () => onChange && onChange(input.value));
    container.appendChild(input);
    return { set color(c) { input.value = c; } };
  }
}

function initColorPickers() {
  // Text Color
  COLOR_PICKERS.text = createColorPicker('textColorPicker', '#ffffff', (hex) => {
    STATE.styles.color = hex;
    if ($('textColorHex')) $('textColorHex').value = hex;
    if ($('textColorSwatch')) $('textColorSwatch').style.background = hex;
    applyStyles();
  });

  // Background Color
  COLOR_PICKERS.bg = createColorPicker('backgroundColorPicker', '#111111', (hex) => {
    STATE.styles.backgroundColor = hex;
    if ($('bgColorHex')) $('bgColorHex').value = hex;
    if ($('bgColorSwatch')) $('bgColorSwatch').style.background = hex;
    applyStyles();
  });

  // Outline Color
  COLOR_PICKERS.outline = createColorPicker('outlineColorPicker', '#ffffff', (hex) => {
    STATE.styles.outlineColor = hex;
    applyStyles();
  });

  // Text Decoration Color
  COLOR_PICKERS.textDecoration = createColorPicker('textDecorationColorPicker', '#ffffff', (hex) => {
    STATE.styles.textDecorationColor = hex;
    applyStyles();
  });

  // Text Stroke Color
  COLOR_PICKERS.textStroke = createColorPicker('textStrokeColorPicker', '#ffffff', (hex) => {
    STATE.textStrokeColor = hex;
    applyStyles();
  });

  // Drop Shadow Color
  COLOR_PICKERS.dropShadow = createColorPicker('dropShadowColorPicker', '#000000', (hex) => {
    STATE.dropShadowColor = hex;
    applyStyles();
  });

  // Palette Base Color
  COLOR_PICKERS.palette = createColorPicker('baseColorPicker', '#667eea', (hex) => {
    STATE.paletteBaseColor = hex;
    generatePalette();
  });
}

/* ─────────────────────────────────────────────────────────────────────
   9. APPLY STYLES
───────────────────────────────────────────────────────────────────── */
function applyStyles() {
  const box = $('preview-box');
  if (!box) return;

  const s = STATE.styles;

  // Core text
  box.style.fontFamily = s.fontFamily;
  box.style.fontSize = s.fontSize;
  box.style.fontWeight = s.fontWeight;
  box.style.fontStyle = s.fontStyle;
  box.style.color = s.color;
  box.style.textAlign = s.textAlign;
  box.style.lineHeight = s.lineHeight;
  box.style.letterSpacing = s.letterSpacing;
  box.style.wordSpacing = s.wordSpacing;
  box.style.textTransform = s.textTransform;
  box.style.textDecorationLine = s.textDecorationLine;
  box.style.textDecorationStyle = s.textDecorationStyle;
  box.style.textDecorationColor = s.textDecorationColor;
  box.style.writingMode = s.writingMode;
  box.style.textOverflow = s.textOverflow;
  box.style.padding = s.padding;

  // Background
  if (STATE.activeBgTab === 'bg-gradient') {
    box.style.backgroundColor = 'transparent';
    box.style.backgroundImage = buildGradientCss();
  } else if (STATE.activeBgTab === 'bg-image' && s.backgroundImage && s.backgroundImage !== 'none') {
    box.style.backgroundColor = s.backgroundColor;
    box.style.backgroundImage = `url('${s.backgroundImage}')`;
  } else if (STATE.activeBgTab === 'bg-pattern') {
    box.style.backgroundColor = s.backgroundColor;
    // pattern is applied separately
  } else {
    box.style.backgroundColor = s.backgroundColor;
    if (!box.style.backgroundImage || box.style.backgroundImage === 'none') {
      box.style.backgroundImage = 'none';
    }
  }
  box.style.backgroundSize = s.backgroundSize;
  box.style.backgroundPosition = s.backgroundPosition;
  box.style.backgroundRepeat = s.backgroundRepeat;
  box.style.backgroundBlendMode = s.backgroundBlendMode;

  // Opacity
  box.style.opacity = s.opacity;

  // Border
  box.style.borderTop = s.borderTop || s.border || 'none';
  box.style.borderRight = s.borderRight || s.border || 'none';
  box.style.borderBottom = s.borderBottom || s.border || 'none';
  box.style.borderLeft = s.borderLeft || s.border || 'none';
  box.style.borderTopLeftRadius = s.borderTopLeftRadius;
  box.style.borderTopRightRadius = s.borderTopRightRadius;
  box.style.borderBottomLeftRadius = s.borderBottomLeftRadius;
  box.style.borderBottomRightRadius = s.borderBottomRightRadius;
  box.style.outline = s.outlineWidth && s.outlineStyle && s.outlineStyle !== 'none'
    ? `${s.outlineWidth}px ${s.outlineStyle} ${s.outlineColor || '#fff'}`
    : 'none';
  box.style.outlineOffset = s.outlineOffset || '0px';

  // Transform
  const tf = buildTransformCss();
  box.style.transform = tf;
  box.style.transformOrigin = s.transformOrigin;

  // Box Shadow
  const bsh = buildBoxShadowCss();
  box.style.boxShadow = bsh || 'none';

  // Text Shadow
  const tsh = buildTextShadowCss();
  box.style.textShadow = tsh || 'none';

  // Text Stroke
  if (STATE.textStrokeWidth > 0) {
    box.style.webkitTextStroke = `${STATE.textStrokeWidth}px ${STATE.textStrokeColor}`;
    box.style['-webkit-text-stroke'] = `${STATE.textStrokeWidth}px ${STATE.textStrokeColor}`;
  } else {
    box.style.webkitTextStroke = '';
    box.style['-webkit-text-stroke'] = '';
  }

  // Text Gradient / Image Fill
  if (STATE.textGradientActive) {
    box.style.backgroundImage = buildTextGradientCss();
    box.style.webkitBackgroundClip = 'text';
    box.style['-webkit-background-clip'] = 'text';
    box.style.webkitTextFillColor = 'transparent';
    box.style['-webkit-text-fill-color'] = 'transparent';
    box.style.backgroundClip = 'text';
    box.style.color = 'transparent';
  } else {
    box.style.webkitBackgroundClip = '';
    box.style['-webkit-background-clip'] = '';
    box.style.webkitTextFillColor = '';
    box.style['-webkit-text-fill-color'] = '';
    box.style.backgroundClip = '';
  }

  // Filters
  const filterStr = buildFilterCss();
  box.style.filter = filterStr || 'none';

  // Backdrop Filter
  const bdFilter = STATE.backdropBlur > 0 ? `blur(${STATE.backdropBlur}px)` : 'none';
  box.style.backdropFilter = bdFilter;
  box.style['-webkit-backdrop-filter'] = bdFilter;

  // Clip Path
  box.style.clipPath = s.clipPath || 'none';

  // Mix Blend Mode
  box.style.mixBlendMode = s.mixBlendMode || 'normal';

  // Animation
  if (s.animationName && s.animationName !== 'none') {
    // Inject keyframes if not already injected
    injectKeyframes(s.animationName);
    box.style.animationName = s.animationName;
    box.style.animationDuration = s.animationDuration;
    box.style.animationDelay = s.animationDelay;
    box.style.animationTimingFunction = s.animationTimingFunction;
    box.style.animationIterationCount = s.animationIterationCount;
    box.style.animationDirection = s.animationDirection;
    box.style.animationFillMode = s.animationFillMode;
    box.style.animationPlayState = s.animationPlayState;
  } else {
    box.style.animation = 'none';
  }

  // Transition
  box.style.transition = buildTransitionCss();

  // Display & Layout
  box.style.display = s.display;
  box.style.justifyContent = s.justifyContent;
  box.style.alignItems = s.alignItems;
  box.style.overflow = s.overflow;
  box.style.cursor = s.cursor;

  // Width/Height
  box.style.width = s.width || '100%';
  box.style.height = s.height || '200px';

  // Font variant features
  let fontVariant = [];
  if ($('fontVariantSmallCaps') && $('fontVariantSmallCaps').checked) fontVariant.push('small-caps');
  if (fontVariant.length) box.style.fontVariant = fontVariant.join(' ');
  else box.style.fontVariant = 'normal';

  let fontFeature = [];
  if ($('fontVariantLiga') && $('fontVariantLiga').checked) fontFeature.push('"liga" 1');
  if ($('fontVariantNum') && $('fontVariantNum').checked) fontFeature.push('"tnum" 1');
  if (fontFeature.length) box.style.fontFeatureSettings = fontFeature.join(', ');
  else box.style.fontFeatureSettings = 'normal';

  updateCssOutput();
}

/* ─────────────────────────────────────────────────────────────────────
   10. CSS BUILDERS
───────────────────────────────────────────────────────────────────── */
function buildGradientCss() {
  const colors = STATE.gradientColors.map(c => `${c.color} ${c.stop}%`).join(', ');
  if (STATE.gradientType === 'radial') return `radial-gradient(circle, ${colors})`;
  if (STATE.gradientType === 'conic') return `conic-gradient(from ${STATE.gradientAngle}deg, ${colors})`;
  return `linear-gradient(${STATE.gradientAngle}deg, ${colors})`;
}

function buildTextGradientCss() {
  const colors = STATE.textGradientColors.map(c => `${c.color} ${c.stop}%`).join(', ');
  if (STATE.textGradientType === 'radial') return `radial-gradient(circle, ${colors})`;
  if (STATE.textGradientType === 'conic') return `conic-gradient(from ${STATE.textGradientAngle}deg, ${colors})`;
  return `linear-gradient(${STATE.textGradientAngle}deg, ${colors})`;
}

function buildBoxShadowCss() {
  if (!STATE.boxShadowLayers.length) return STATE.styles.boxShadow || 'none';
  return STATE.boxShadowLayers
    .filter(l => l.active !== false)
    .map(l => `${l.inset ? 'inset ' : ''}${l.x || 0}px ${l.y || 0}px ${l.blur || 0}px ${l.spread || 0}px ${l.color || '#000'}`)
    .join(', ') || 'none';
}

function buildTextShadowCss() {
  if (!STATE.textShadowLayers.length) return STATE.styles.textShadow || 'none';
  return STATE.textShadowLayers
    .filter(l => l.active !== false)
    .map(l => `${l.x || 0}px ${l.y || 0}px ${l.blur || 0}px ${l.color || '#000'}`)
    .join(', ') || 'none';
}

function buildTransformCss() {
  const parts = [];
  if (STATE.transformPerspective > 0) parts.push(`perspective(${STATE.transformPerspective}px)`);
  if (STATE.transformRotate !== 0) parts.push(`rotate(${STATE.transformRotate}deg)`);
  if (STATE.transformRotateX !== 0) parts.push(`rotateX(${STATE.transformRotateX}deg)`);
  if (STATE.transformRotateY !== 0) parts.push(`rotateY(${STATE.transformRotateY}deg)`);
  if (STATE.transformRotateZ !== 0) parts.push(`rotateZ(${STATE.transformRotateZ}deg)`);
  if (STATE.transformScaleX !== 1 || STATE.transformScaleY !== 1)
    parts.push(`scale(${STATE.transformScaleX}, ${STATE.transformScaleY})`);
  if (STATE.transformSkewX !== 0 || STATE.transformSkewY !== 0)
    parts.push(`skew(${STATE.transformSkewX}deg, ${STATE.transformSkewY}deg)`);
  if (STATE.transformTranslateX !== 0 || STATE.transformTranslateY !== 0)
    parts.push(`translate(${STATE.transformTranslateX}px, ${STATE.transformTranslateY}px)`);
  return parts.length ? parts.join(' ') : 'none';
}

function buildFilterCss() {
  const parts = [];
  if (STATE.filterBlur > 0) parts.push(`blur(${STATE.filterBlur}px)`);
  if (STATE.filterBrightness !== 100) parts.push(`brightness(${STATE.filterBrightness}%)`);
  if (STATE.filterContrast !== 100) parts.push(`contrast(${STATE.filterContrast}%)`);
  if (STATE.filterSaturate !== 100) parts.push(`saturate(${STATE.filterSaturate}%)`);
  if (STATE.filterHueRotate !== 0) parts.push(`hue-rotate(${STATE.filterHueRotate}deg)`);
  if (STATE.filterInvert > 0) parts.push(`invert(${STATE.filterInvert}%)`);
  if (STATE.filterSepia > 0) parts.push(`sepia(${STATE.filterSepia}%)`);
  if (STATE.filterGrayscale > 0) parts.push(`grayscale(${STATE.filterGrayscale}%)`);
  if (STATE.dropShadowX !== 0 || STATE.dropShadowY !== 0 || STATE.dropShadowBlur > 0)
    parts.push(`drop-shadow(${STATE.dropShadowX}px ${STATE.dropShadowY}px ${STATE.dropShadowBlur}px ${STATE.dropShadowColor})`);
  return parts.join(' ');
}

function buildTransitionCss() {
  const prop = ($('transitionProperty') || {}).value || 'all';
  const dur = ($('transitionDuration') || {}).value || '0.3';
  const timing = ($('transitionTimingFunction') || {}).value || 'ease';
  const delay = ($('transitionDelay') || {}).value || '0';
  return `${prop} ${dur}s ${timing} ${delay}s`;
}

function injectKeyframes(animName) {
  const styleId = `kf-${animName}`;
  if (document.getElementById(styleId)) return;

  // Custom keyframes from textarea
  const customKf = $('animationKeyframes');
  if (customKf && customKf.value.trim()) {
    const el = document.createElement('style');
    el.id = styleId;
    el.textContent = customKf.value;
    document.head.appendChild(el);
    return;
  }

  if (KEYFRAMES[animName]) {
    const el = document.createElement('style');
    el.id = styleId;
    el.textContent = KEYFRAMES[animName];
    document.head.appendChild(el);
  }
}

/* ─────────────────────────────────────────────────────────────────────
   11. CSS OUTPUT GENERATION
───────────────────────────────────────────────────────────────────── */
function updateCssOutput() {
  const box = $('preview-box');
  if (!box) return;

  const s = STATE.styles;
  const lines = [];

  const add = (prop, val) => {
    if (val && val !== 'none' && val !== '' && val !== 'initial') {
      lines.push(`  ${prop}: ${val};`);
    }
  };

  const addRaw = (prop, val) => {
    if (val !== undefined && val !== null && val !== '') {
      lines.push(`  ${prop}: ${val};`);
    }
  };

  // Typography
  addRaw('font-family', s.fontFamily);
  addRaw('font-size', s.fontSize);
  addRaw('font-weight', s.fontWeight);
  if (s.fontStyle !== 'normal') add('font-style', s.fontStyle);
  if (s.textTransform !== 'none') add('text-transform', s.textTransform);
  if (s.letterSpacing !== '0px') add('letter-spacing', s.letterSpacing);
  if (s.wordSpacing !== '0px') add('word-spacing', s.wordSpacing);
  if (s.lineHeight !== '1.5') addRaw('line-height', s.lineHeight);
  addRaw('color', s.color);
  addRaw('text-align', s.textAlign);
  if (s.writingMode !== 'horizontal-tb') add('writing-mode', s.writingMode);
  if (s.textDecorationLine !== 'none') {
    add('text-decoration-line', s.textDecorationLine);
    add('text-decoration-style', s.textDecorationStyle);
    add('text-decoration-color', s.textDecorationColor);
  }

  // Text Shadow
  const tsh = buildTextShadowCss();
  if (tsh && tsh !== 'none') addRaw('text-shadow', tsh);

  // Text Stroke
  if (STATE.textStrokeWidth > 0) {
    addRaw('-webkit-text-stroke', `${STATE.textStrokeWidth}px ${STATE.textStrokeColor}`);
  }

  // Text Gradient
  if (STATE.textGradientActive) {
    addRaw('background-image', buildTextGradientCss());
    addRaw('-webkit-background-clip', 'text');
    addRaw('background-clip', 'text');
    addRaw('-webkit-text-fill-color', 'transparent');
  }

  // Background
  if (STATE.activeBgTab === 'bg-gradient') {
    addRaw('background-image', buildGradientCss());
  } else {
    addRaw('background-color', s.backgroundColor);
    if (s.backgroundImage && s.backgroundImage !== 'none') {
      addRaw('background-image', `url('${s.backgroundImage}')`);
      addRaw('background-size', s.backgroundSize);
      addRaw('background-position', s.backgroundPosition);
      addRaw('background-repeat', s.backgroundRepeat);
    }
  }
  if (s.backgroundBlendMode !== 'normal') add('background-blend-mode', s.backgroundBlendMode);

  // Opacity
  if (s.opacity !== '1') addRaw('opacity', s.opacity);

  // Padding
  if (s.padding !== '0px 0px 0px 0px' && s.padding !== '0px') addRaw('padding', s.padding);

  // Border
  const borders = ['Top', 'Right', 'Bottom', 'Left'];
  const allSameBorder = borders.every(side => (s[`border${side}`] || 'none') === (s.borderTop || 'none'));
  if (allSameBorder && s.borderTop && s.borderTop !== 'none') {
    addRaw('border', s.borderTop);
  } else {
    borders.forEach(side => {
      if (s[`border${side}`] && s[`border${side}`] !== 'none') {
        addRaw(`border-${side.toLowerCase()}`, s[`border${side}`]);
      }
    });
  }

  // Gradient Border (pseudo approach)
  // Border Radius
  const allSameRadius = [s.borderTopLeftRadius, s.borderTopRightRadius, s.borderBottomLeftRadius, s.borderBottomRightRadius]
    .every(v => v === s.borderTopLeftRadius);
  if (allSameRadius) {
    if (s.borderTopLeftRadius !== '0px' && s.borderTopLeftRadius !== '0') {
      addRaw('border-radius', s.borderTopLeftRadius);
    }
  } else {
    addRaw('border-radius', `${s.borderTopLeftRadius} ${s.borderTopRightRadius} ${s.borderBottomRightRadius} ${s.borderBottomLeftRadius}`);
  }

  // Outline
  if (s.outlineStyle && s.outlineStyle !== 'none') {
    addRaw('outline', `${s.outlineWidth || 0}px ${s.outlineStyle} ${s.outlineColor || '#fff'}`);
    if (s.outlineOffset !== '0px') addRaw('outline-offset', s.outlineOffset);
  }

  // Transform
  const tf = buildTransformCss();
  if (tf !== 'none') {
    addRaw('transform', tf);
    if (s.transformOrigin !== 'center center') addRaw('transform-origin', s.transformOrigin);
  }

  // Box Shadow
  const bsh = buildBoxShadowCss();
  if (bsh && bsh !== 'none') addRaw('box-shadow', bsh);

  // Filter
  const filterStr = buildFilterCss();
  if (filterStr) addRaw('filter', filterStr);

  // Backdrop Filter
  if (STATE.backdropBlur > 0) {
    addRaw('backdrop-filter', `blur(${STATE.backdropBlur}px)`);
    addRaw('-webkit-backdrop-filter', `blur(${STATE.backdropBlur}px)`);
  }

  // Clip Path
  if (s.clipPath && s.clipPath !== 'none') addRaw('clip-path', s.clipPath);

  // Mix Blend Mode
  if (s.mixBlendMode !== 'normal') addRaw('mix-blend-mode', s.mixBlendMode);

  // Animation
  if (s.animationName && s.animationName !== 'none') {
    addRaw('animation-name', s.animationName);
    addRaw('animation-duration', s.animationDuration);
    if (s.animationDelay !== '0s') addRaw('animation-delay', s.animationDelay);
    addRaw('animation-timing-function', s.animationTimingFunction);
    addRaw('animation-iteration-count', s.animationIterationCount);
    if (s.animationDirection !== 'normal') addRaw('animation-direction', s.animationDirection);
    if (s.animationFillMode !== 'none') addRaw('animation-fill-mode', s.animationFillMode);
    if (s.animationPlayState !== 'running') addRaw('animation-play-state', s.animationPlayState);
  }

  // Transition
  const trans = buildTransitionCss();
  if (trans !== 'all 0.3s ease 0s') addRaw('transition', trans);

  // Display & Layout
  if (s.display !== 'flex') addRaw('display', s.display);
  if (s.display === 'flex' || s.display === 'inline-flex') {
    if (s.justifyContent !== 'center') addRaw('justify-content', s.justifyContent);
    if (s.alignItems !== 'center') addRaw('align-items', s.alignItems);
  }
  if (s.overflow !== 'hidden') addRaw('overflow', s.overflow);
  if (s.cursor !== 'auto') addRaw('cursor', s.cursor);

  const cssStr = `.my-element {\n${lines.join('\n')}\n}`;

  // Add keyframes if animation is active
  let fullCss = cssStr;
  if (s.animationName && s.animationName !== 'none' && KEYFRAMES[s.animationName]) {
    fullCss = KEYFRAMES[s.animationName] + '\n\n' + cssStr;
  }
  if (STATE.customKeyframes) {
    fullCss = STATE.customKeyframes + '\n\n' + cssStr;
  }

  const cssOutput = $('css-output');
  if (cssOutput) {
    cssOutput.value = fullCss;
    const lineCount = fullCss.split('\n').length;
    const lineEl = $('cssLineCount');
    if (lineEl) lineEl.textContent = `${lineCount} satır`;
  }

  // Update other tabs
  updateHtmlOutput(fullCss);
  updateJsonOutput();
  updateTailwindOutput();
}

function updateHtmlOutput(css) {
  const area = $('htmlPreviewArea');
  if (!area) return;
  const text = STATE.previewText || 'K3N4N V7.0';
  const html = `<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Preview</title>
  <style>
${css}
  </style>
</head>
<body>
  <div class="my-element">${escapeHtml(text)}</div>
</body>
</html>`;
  area.innerHTML = `<pre><code>${escapeHtml(html)}</code></pre>`;
}

function updateJsonOutput() {
  const out = $('json-output');
  if (!out) return;
  const obj = {
    styles: STATE.styles,
    boxShadowLayers: STATE.boxShadowLayers,
    textShadowLayers: STATE.textShadowLayers,
    gradientColors: STATE.gradientColors,
    textGradientColors: STATE.textGradientColors,
    textGradientActive: STATE.textGradientActive,
    textStrokeWidth: STATE.textStrokeWidth,
    textStrokeColor: STATE.textStrokeColor,
    filters: {
      blur: STATE.filterBlur,
      brightness: STATE.filterBrightness,
      contrast: STATE.filterContrast,
      saturate: STATE.filterSaturate,
      hueRotate: STATE.filterHueRotate,
      invert: STATE.filterInvert,
      sepia: STATE.filterSepia,
      grayscale: STATE.filterGrayscale,
    },
  };
  out.value = JSON.stringify(obj, null, 2);
}

function updateTailwindOutput() {
  const out = $('tailwindOutput');
  if (!out) return;
  const s = STATE.styles;
  const classes = [];

  // Font size rough mapping
  const fsz = parseInt(s.fontSize);
  if (fsz <= 12) classes.push('text-xs');
  else if (fsz <= 14) classes.push('text-sm');
  else if (fsz <= 16) classes.push('text-base');
  else if (fsz <= 18) classes.push('text-lg');
  else if (fsz <= 20) classes.push('text-xl');
  else if (fsz <= 24) classes.push('text-2xl');
  else if (fsz <= 30) classes.push('text-3xl');
  else if (fsz <= 36) classes.push('text-4xl');
  else if (fsz <= 48) classes.push('text-5xl');
  else classes.push('text-6xl');

  // Font weight
  const fw = { '100': 'font-thin', '200': 'font-extralight', '300': 'font-light', '400': 'font-normal', '500': 'font-medium', '600': 'font-semibold', '700': 'font-bold', '800': 'font-extrabold', '900': 'font-black' };
  if (fw[s.fontWeight]) classes.push(fw[s.fontWeight]);

  // Text align
  const ta = { 'left': 'text-left', 'center': 'text-center', 'right': 'text-right', 'justify': 'text-justify' };
  if (ta[s.textAlign]) classes.push(ta[s.textAlign]);

  // Transform
  if (s.textTransform === 'uppercase') classes.push('uppercase');
  if (s.textTransform === 'lowercase') classes.push('lowercase');
  if (s.textTransform === 'capitalize') classes.push('capitalize');

  // Italic
  if (s.fontStyle === 'italic') classes.push('italic');

  // Overflow
  if (s.overflow === 'hidden') classes.push('overflow-hidden');
  if (s.overflow === 'scroll') classes.push('overflow-scroll');
  if (s.overflow === 'auto') classes.push('overflow-auto');

  // Border radius
  const br = parseInt(s.borderTopLeftRadius);
  if (br === 0) classes.push('rounded-none');
  else if (br <= 2) classes.push('rounded-sm');
  else if (br <= 4) classes.push('rounded');
  else if (br <= 6) classes.push('rounded-md');
  else if (br <= 8) classes.push('rounded-lg');
  else if (br <= 12) classes.push('rounded-xl');
  else if (br >= 9999 || s.borderTopLeftRadius === '50%') classes.push('rounded-full');
  else classes.push('rounded-2xl');

  // Display
  if (s.display === 'flex') classes.push('flex');
  if (s.display === 'grid') classes.push('grid');
  if (s.display === 'block') classes.push('block');
  if (s.display === 'inline-flex') classes.push('inline-flex');
  if (s.display === 'none') classes.push('hidden');

  // Flex
  if (s.display === 'flex' || s.display === 'inline-flex') {
    if (s.justifyContent === 'center') classes.push('justify-center');
    if (s.justifyContent === 'flex-start') classes.push('justify-start');
    if (s.justifyContent === 'flex-end') classes.push('justify-end');
    if (s.justifyContent === 'space-between') classes.push('justify-between');
    if (s.alignItems === 'center') classes.push('items-center');
    if (s.alignItems === 'flex-start') classes.push('items-start');
    if (s.alignItems === 'flex-end') classes.push('items-end');
  }

  out.innerHTML = `<pre><code class="tailwind-classes">&lt;div class="${classes.join(' ')}"&gt;\n  <!-- Note: Some styles require custom CSS -->\n  <!-- e.g., text-shadow, clip-path, animations -->\n&lt;/div&gt;\n\n/* Tailwind Classes: */\n"${classes.join(' ')}"</code></pre>`;
}

/* ─────────────────────────────────────────────────────────────────────
   12. HISTORY (UNDO/REDO)
───────────────────────────────────────────────────────────────────── */
function saveHistory() {
  const snapshot = JSON.stringify({
    styles: STATE.styles,
    boxShadowLayers: STATE.boxShadowLayers,
    textShadowLayers: STATE.textShadowLayers,
    gradientColors: STATE.gradientColors,
    textGradientColors: STATE.textGradientColors,
    textGradientActive: STATE.textGradientActive,
    textStrokeWidth: STATE.textStrokeWidth,
    textStrokeColor: STATE.textStrokeColor,
    filterBlur: STATE.filterBlur,
    filterBrightness: STATE.filterBrightness,
    filterContrast: STATE.filterContrast,
    filterSaturate: STATE.filterSaturate,
    filterHueRotate: STATE.filterHueRotate,
    filterInvert: STATE.filterInvert,
    filterSepia: STATE.filterSepia,
    filterGrayscale: STATE.filterGrayscale,
    backdropBlur: STATE.backdropBlur,
    transformRotate: STATE.transformRotate,
    transformScaleX: STATE.transformScaleX,
    transformScaleY: STATE.transformScaleY,
    transformSkewX: STATE.transformSkewX,
    transformSkewY: STATE.transformSkewY,
    transformTranslateX: STATE.transformTranslateX,
    transformTranslateY: STATE.transformTranslateY,
    transformRotateX: STATE.transformRotateX,
    transformRotateY: STATE.transformRotateY,
    transformRotateZ: STATE.transformRotateZ,
    transformPerspective: STATE.transformPerspective,
  });

  // Don't save duplicate
  if (STATE.history[STATE.historyIndex] === snapshot) return;

  // Truncate redo stack
  STATE.history = STATE.history.slice(0, STATE.historyIndex + 1);
  STATE.history.push(snapshot);

  if (STATE.history.length > STATE.maxHistory) {
    STATE.history.shift();
  } else {
    STATE.historyIndex++;
  }

  updateHistoryUI();
  updateHistoryTimeline();
}

function restoreHistory(snapshot) {
  const data = JSON.parse(snapshot);
  Object.assign(STATE, data);
  Object.assign(STATE.styles, data.styles);
  syncAllControls();
  applyStyles();
}

function undo() {
  if (STATE.historyIndex <= 0) return;
  STATE.historyIndex--;
  restoreHistory(STATE.history[STATE.historyIndex]);
  showToast('Geri alındı', 'info', 1500);
}

function redo() {
  if (STATE.historyIndex >= STATE.history.length - 1) return;
  STATE.historyIndex++;
  restoreHistory(STATE.history[STATE.historyIndex]);
  showToast('İleri alındı', 'info', 1500);
}

function updateHistoryUI() {
  const undoBtn = document.querySelector('[data-action="undo"]');
  const redoBtn = document.querySelector('[data-action="redo"]');
  const undoCount = $('undoCount');
  const redoCount = $('redoCount');

  if (undoBtn) undoBtn.disabled = STATE.historyIndex <= 0;
  if (redoBtn) redoBtn.disabled = STATE.historyIndex >= STATE.history.length - 1;
  if (undoCount) undoCount.textContent = STATE.historyIndex;
  if (redoCount) redoCount.textContent = STATE.history.length - 1 - STATE.historyIndex;
}

function updateHistoryTimeline() {
  const items = $('historyItems');
  if (!items) return;
  items.innerHTML = '';

  const recent = STATE.history.slice(-8);
  recent.forEach((snap, i) => {
    const idx = STATE.history.length - recent.length + i;
    const div = document.createElement('div');
    div.className = `history-item${idx === STATE.historyIndex ? ' active' : ''}`;
    div.innerHTML = `<i class="fas fa-clock-rotate-left"></i><span>#${idx + 1}</span>`;
    div.title = `Durum #${idx + 1}`;
    div.addEventListener('click', () => {
      STATE.historyIndex = idx;
      restoreHistory(STATE.history[idx]);
    });
    items.appendChild(div);
  });
}

/* ─────────────────────────────────────────────────────────────────────
   13. PANELS
───────────────────────────────────────────────────────────────────── */
function initPanels() {
  $$('.panel-header').forEach(header => {
    header.addEventListener('click', () => togglePanel(header.closest('.panel')));
    header.addEventListener('keydown', (e) => {
      if (e.key === 'Enter' || e.key === ' ') {
        e.preventDefault();
        togglePanel(header.closest('.panel'));
      }
    });
  });
}

function togglePanel(panel) {
  if (!panel) return;
  const isExpanded = panel.classList.contains('expanded');
  panel.classList.toggle('expanded', !isExpanded);
  const header = panel.querySelector('.panel-header');
  if (header) header.setAttribute('aria-expanded', !isExpanded);
}

function initSubTabs() {
  $$('.sub-tab').forEach(btn => {
    btn.addEventListener('click', () => {
      const targetId = btn.dataset.subTab;
      const parent = btn.closest('.panel-body') || btn.closest('.output-card');

      // Update buttons
      btn.closest('.sub-tabs').querySelectorAll('.sub-tab').forEach(b => {
        b.classList.remove('active');
        b.setAttribute('aria-selected', 'false');
      });
      btn.classList.add('active');
      btn.setAttribute('aria-selected', 'true');

      // Update content
      const contents = parent ? parent.querySelectorAll('.sub-tab-content') : $$(`#${targetId}`);
      if (parent) {
        parent.querySelectorAll('.sub-tab-content').forEach(c => c.classList.remove('active'));
      }
      const target = $(`${targetId}`);
      if (target) target.classList.add('active');

      // Track active bg tab
      if (['bg-solid', 'bg-gradient', 'bg-image', 'bg-pattern'].includes(targetId)) {
        STATE.activeBgTab = targetId;
        applyStyles();
      }
    });
  });
}

/* ─────────────────────────────────────────────────────────────────────
   14. OUTPUT TABS
───────────────────────────────────────────────────────────────────── */
function initOutputTabs() {
  $$('.output-tab').forEach(btn => {
    btn.addEventListener('click', () => {
      const targetId = btn.dataset.tab;
      $$('.output-tab').forEach(b => { b.classList.remove('active'); b.setAttribute('aria-selected', 'false'); });
      $$('.tab-content').forEach(c => c.classList.remove('active'));
      btn.classList.add('active');
      btn.setAttribute('aria-selected', 'true');
      const target = $(targetId);
      if (target) target.classList.add('active');
    });
  });
}

/* ─────────────────────────────────────────────────────────────────────
   15. FORM CONTROLS INITIALIZATION
───────────────────────────────────────────────────────────────────── */
function initControls() {
  /* ── Font Size ── */
  const fontSizeRange = $('fontSizeRange');
  const fontSizeInput = $('fontSize');
  const fontSizeVal = $('fontSizeVal');
  if (fontSizeRange && fontSizeInput) {
    fontSizeRange.addEventListener('input', () => {
      fontSizeInput.value = fontSizeRange.value;
      fontSizeVal.textContent = fontSizeRange.value + 'px';
      STATE.styles.fontSize = fontSizeRange.value + 'px';
      applyAndSave();
    });
    fontSizeInput.addEventListener('input', () => {
      fontSizeRange.value = fontSizeInput.value;
      fontSizeVal.textContent = fontSizeInput.value + 'px';
      STATE.styles.fontSize = fontSizeInput.value + 'px';
      applyAndSave();
    });
  }

  /* ── Font Weight ── */
  const fontWeightRange = $('fontWeightRange');
  const fontWeightSelect = $('fontWeight');
  if (fontWeightRange && fontWeightSelect) {
    fontWeightRange.addEventListener('input', () => {
      const val = fontWeightRange.value;
      fontWeightSelect.value = val;
      $('fontWeightVal').textContent = val;
      STATE.styles.fontWeight = val;
      applyAndSave();
    });
    fontWeightSelect.addEventListener('change', () => {
      fontWeightRange.value = fontWeightSelect.value;
      $('fontWeightVal').textContent = fontWeightSelect.value;
      STATE.styles.fontWeight = fontWeightSelect.value;
      applyAndSave();
    });
  }

  /* ── Font Family ── */
  const fontFamily = $('fontFamily');
  if (fontFamily) {
    fontFamily.addEventListener('change', () => {
      STATE.styles.fontFamily = fontFamily.value;
      updateFontPreview(fontFamily.value);
      applyAndSave();
    });
  }

  /* ── Font Style / Transform / Overflow / Writing Mode ── */
  ['fontStyle', 'textTransform', 'textOverflow', 'writingMode'].forEach(id => {
    const el = $(id);
    if (el) el.addEventListener('change', () => {
      STATE.styles[id] = el.value;
      applyAndSave();
    });
  });

  /* ── Font Variant ── */
  ['fontVariantSmallCaps', 'fontVariantLiga', 'fontVariantNum'].forEach(id => {
    const el = $(id);
    if (el) el.addEventListener('change', () => applyAndSave());
  });

  /* ── Text Decoration ── */
  const textDecoLine = $('textDecorationLine');
  const textDecoStyle = $('textDecorationStyle');
  if (textDecoLine) textDecoLine.addEventListener('change', () => { STATE.styles.textDecorationLine = textDecoLine.value; applyAndSave(); });
  if (textDecoStyle) textDecoStyle.addEventListener('change', () => { STATE.styles.textDecorationStyle = textDecoStyle.value; applyAndSave(); });

  /* ── Text Color Hex Input ── */
  const textColorHex = $('textColorHex');
  if (textColorHex) {
    textColorHex.addEventListener('input', () => {
      const hex = textColorHex.value;
      if (/^#[0-9A-Fa-f]{6}$/.test(hex) || /^#[0-9A-Fa-f]{8}$/.test(hex)) {
        STATE.styles.color = hex;
        if (COLOR_PICKERS.text) try { COLOR_PICKERS.text.color = hex; } catch (e) {}
        $('textColorSwatch').style.background = hex;
        applyAndSave();
      }
    });
  }

  /* ── BG Color Hex Input ── */
  const bgColorHex = $('bgColorHex');
  if (bgColorHex) {
    bgColorHex.addEventListener('input', () => {
      const hex = bgColorHex.value;
      if (/^#[0-9A-Fa-f]{6}$/.test(hex)) {
        STATE.styles.backgroundColor = hex;
        if (COLOR_PICKERS.bg) try { COLOR_PICKERS.bg.color = hex; } catch (e) {}
        $('bgColorSwatch').style.background = hex;
        applyAndSave();
      }
    });
  }

  /* ── Line Height ── */
  const lineHeightRange = $('lineHeightRange');
  if (lineHeightRange) {
    lineHeightRange.addEventListener('input', () => {
      const val = lineHeightRange.value;
      $('lineHeightVal').textContent = val;
      STATE.styles.lineHeight = val;
      applyAndSave();
    });
  }

  /* ── Letter / Word Spacing ── */
  const letterSpacing = $('letterSpacing');
  const wordSpacing = $('wordSpacing');
  if (letterSpacing) letterSpacing.addEventListener('input', () => { STATE.styles.letterSpacing = letterSpacing.value + 'px'; applyAndSave(); });
  if (wordSpacing) wordSpacing.addEventListener('input', () => { STATE.styles.wordSpacing = wordSpacing.value + 'px'; applyAndSave(); });

  /* ── Text Align Buttons ── */
  $$('.align-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      $$('.align-btn').forEach(b => { b.classList.remove('active'); b.setAttribute('aria-pressed', 'false'); });
      btn.classList.add('active');
      btn.setAttribute('aria-pressed', 'true');
      STATE.styles.textAlign = btn.dataset.align;
      applyAndSave();
    });
  });

  /* ── Background Opacity ── */
  const bgOpacityRange = $('backgroundOpacityRange');
  if (bgOpacityRange) {
    bgOpacityRange.addEventListener('input', () => {
      const val = bgOpacityRange.value;
      $('bgOpacityVal').textContent = val;
      STATE.styles.opacity = val;
      applyAndSave();
    });
  }

  /* ── Text Opacity ── */
  const textOpacityRange = $('textOpacityRange');
  if (textOpacityRange) {
    textOpacityRange.addEventListener('input', () => {
      const val = textOpacityRange.value;
      $('textOpacityVal').textContent = val;
      STATE.styles.opacity = val;
      applyAndSave();
    });
  }

  /* ── Gradient Settings ── */
  const gradientType = $('gradientType');
  const gradientAngle = $('gradientAngle');
  const gradientAngleRange = $('gradientAngleRange');
  if (gradientType) gradientType.addEventListener('change', () => { STATE.gradientType = gradientType.value; updateGradientPreviewBar(); applyAndSave(); });
  if (gradientAngle) gradientAngle.addEventListener('input', () => {
    if (gradientAngleRange) gradientAngleRange.value = gradientAngle.value;
    STATE.gradientAngle = parseInt(gradientAngle.value);
    updateGradientPreviewBar();
    applyAndSave();
  });
  if (gradientAngleRange) gradientAngleRange.addEventListener('input', () => {
    if (gradientAngle) gradientAngle.value = gradientAngleRange.value;
    STATE.gradientAngle = parseInt(gradientAngleRange.value);
    updateGradientPreviewBar();
    applyAndSave();
  });

  /* ── Background Image URL ── */
  const bgImageUrl = $('backgroundImageUrl');
  if (bgImageUrl) {
    bgImageUrl.addEventListener('input', () => {
      STATE.styles.backgroundImage = bgImageUrl.value;
      applyAndSave();
    });
  }

  /* ── Background Size / Repeat ── */
  const backgroundSize = $('backgroundSize');
  const backgroundRepeat = $('backgroundRepeat');
  if (backgroundSize) backgroundSize.addEventListener('change', () => { STATE.styles.backgroundSize = backgroundSize.value; applyAndSave(); });
  if (backgroundRepeat) backgroundRepeat.addEventListener('change', () => { STATE.styles.backgroundRepeat = backgroundRepeat.value; applyAndSave(); });

  /* ── Background Blend Mode ── */
  const bgBlendMode = $('backgroundBlendMode');
  if (bgBlendMode) bgBlendMode.addEventListener('change', () => { STATE.styles.backgroundBlendMode = bgBlendMode.value; applyAndSave(); });

  /* ── BG Position Grid ── */
  $$('.pos-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      $$('.pos-btn').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      STATE.styles.backgroundPosition = btn.dataset.pos;
      applyAndSave();
    });
  });

  /* ── Border Controls ── */
  initBorderControls();

  /* ── Border Radius ── */
  const borderRadiusAll = $('borderRadiusAll');
  if (borderRadiusAll) {
    borderRadiusAll.addEventListener('input', () => {
      const val = borderRadiusAll.value;
      $('borderRadiusVal').textContent = val + 'px';
      ['TopLeft', 'TopRight', 'BottomLeft', 'BottomRight'].forEach(corner => {
        const inp = $(`borderRadius${corner}`);
        if (inp) inp.value = val;
        STATE.styles[`border${corner}Radius`] = val + 'px';
      });
      applyAndSave();
    });
  }

  ['TopLeft', 'TopRight', 'BottomLeft', 'BottomRight'].forEach(corner => {
    const inp = $(`borderRadius${corner}`);
    if (inp) inp.addEventListener('input', () => {
      STATE.styles[`border${corner}Radius`] = inp.value + 'px';
      applyAndSave();
    });
  });

  /* ── Outline ── */
  const outlineWidth = $('outlineWidth');
  const outlineStyle = $('outlineStyle');
  const outlineOffset = $('outlineOffset');
  if (outlineWidth) outlineWidth.addEventListener('input', () => { STATE.styles.outlineWidth = outlineWidth.value; applyAndSave(); });
  if (outlineStyle) outlineStyle.addEventListener('change', () => { STATE.styles.outlineStyle = outlineStyle.value; applyAndSave(); });
  if (outlineOffset) outlineOffset.addEventListener('input', () => { STATE.styles.outlineOffset = outlineOffset.value + 'px'; applyAndSave(); });

  /* ── Transform ── */
  initTransformControls();

  /* ── Filters ── */
  initFilterControls();

  /* ── Animation ── */
  initAnimationControls();

  /* ── Layout ── */
  initLayoutControls();

  /* ── Padding ── */
  initPaddingControls();

  /* ── Text Stroke ── */
  const textStrokeRange = $('textStrokeWidthRange');
  if (textStrokeRange) {
    textStrokeRange.addEventListener('input', () => {
      STATE.textStrokeWidth = parseFloat(textStrokeRange.value);
      $('textStrokeWidthVal').textContent = STATE.textStrokeWidth + 'px';
      applyAndSave();
    });
  }

  /* ── Clip Path Input ── */
  const clipPathInput = $('clipPath');
  if (clipPathInput) {
    clipPathInput.addEventListener('input', () => {
      STATE.styles.clipPath = clipPathInput.value;
      applyAndSave();
    });
  }

  /* ── Text Gradient ── */
  initTextGradientControls();

  /* ── Mix Blend Mode ── */
  const mixBlendMode = $('mixBlendMode');
  if (mixBlendMode) mixBlendMode.addEventListener('change', () => { STATE.styles.mixBlendMode = mixBlendMode.value; applyAndSave(); });

  /* ── Preview Text ── */
  const customText = $('customText');
  if (customText) {
    customText.addEventListener('input', () => {
      STATE.previewText = customText.value;
      const box = $('preview-box');
      if (box) box.textContent = customText.value;
      const charCount = $('charCount');
      if (charCount) charCount.textContent = `${customText.value.length}/200`;
      updateCssOutput();
    });
  }

  /* ── Palette Controls ── */
  const paletteType = $('paletteType');
  const paletteSize = $('paletteSize');
  if (paletteType) paletteType.addEventListener('change', () => { STATE.paletteType = paletteType.value; generatePalette(); });
  if (paletteSize) paletteSize.addEventListener('change', () => { STATE.paletteSize = parseInt(paletteSize.value); generatePalette(); });

  /* ── Chaos Level ── */
  const chaosLevel = $('chaosLevel');
  if (chaosLevel) chaosLevel.addEventListener('input', () => { $('chaosLevelVal').textContent = chaosLevel.value; });

  /* ── Theme Search ── */
  const themeSearch = $('themeSearch');
  if (themeSearch) {
    themeSearch.addEventListener('input', () => {
      const query = themeSearch.value.toLowerCase();
      $$('.preset-card').forEach(card => {
        card.style.display = card.textContent.toLowerCase().includes(query) ? '' : 'none';
      });
    });
  }

  /* ── Panel Search ── */
  const panelSearch = $('panelSearch');
  const searchClear = $('searchClear');
  if (panelSearch) {
    panelSearch.addEventListener('input', () => {
      const query = panelSearch.value.toLowerCase();
      if (searchClear) searchClear.style.display = query ? 'flex' : 'none';
      $$('.panel').forEach(panel => {
        const title = panel.querySelector('.panel-title');
        if (!title) return;
        const matches = title.textContent.toLowerCase().includes(query);
        panel.style.display = query ? (matches ? '' : 'none') : '';
        if (matches && query) panel.classList.add('expanded');
      });
    });
  }
  if (searchClear) {
    searchClear.addEventListener('click', () => {
      panelSearch.value = '';
      searchClear.style.display = 'none';
      $$('.panel').forEach(p => p.style.display = '');
    });
  }
}

function applyAndSave() {
  applyStyles();
  saveHistory();
}

function initBorderControls() {
  const borderLinked = $('borderLinked');
  const borderSides = ['Top', 'Right', 'Bottom', 'Left'];

  borderSides.forEach(side => {
    const inp = $(`border${side}`);
    if (!inp) return;
    inp.addEventListener('input', () => {
      if (borderLinked && borderLinked.checked) {
        borderSides.forEach(s => {
          const other = $(`border${s}`);
          if (other) other.value = inp.value;
          STATE.styles[`border${s}`] = inp.value;
        });
      } else {
        STATE.styles[`border${side}`] = inp.value;
      }
      applyAndSave();
    });
  });
}

function initTransformControls() {
  const maps = [
    ['rotateRange', 'rotate', (v) => { STATE.transformRotate = parseFloat(v); $('rotateVal').textContent = v + '°'; }],
    ['scaleRange', null, (v) => { STATE.transformScaleX = parseFloat(v); STATE.transformScaleY = parseFloat(v); $('scaleVal').textContent = parseFloat(v).toFixed(2); }],
    ['scaleX', null, (v) => { STATE.transformScaleX = parseFloat(v); }],
    ['scaleY', null, (v) => { STATE.transformScaleY = parseFloat(v); }],
    ['skewX', null, (v) => { STATE.transformSkewX = parseFloat(v); }],
    ['skewY', null, (v) => { STATE.transformSkewY = parseFloat(v); }],
    ['translateX', null, (v) => { STATE.transformTranslateX = parseFloat(v); }],
    ['translateY', null, (v) => { STATE.transformTranslateY = parseFloat(v); }],
    ['rotateX', null, (v) => { STATE.transformRotateX = parseFloat(v); }],
    ['rotateY', null, (v) => { STATE.transformRotateY = parseFloat(v); }],
    ['rotateZ', null, (v) => { STATE.transformRotateZ = parseFloat(v); }],
    ['perspective', null, (v) => { STATE.transformPerspective = parseFloat(v); }],
  ];

  maps.forEach(([rangeId, inputId, fn]) => {
    const rangeEl = $(rangeId);
    const inputEl = inputId ? $(inputId) : null;
    if (rangeEl) rangeEl.addEventListener('input', () => { fn(rangeEl.value); if (inputEl) inputEl.value = rangeEl.value; applyAndSave(); });
    if (inputEl) inputEl.addEventListener('input', () => { fn(inputEl.value); if (rangeEl) rangeEl.value = inputEl.value; applyAndSave(); });
  });

  // Sync rotate range and input
  const rotateInput = $('rotate');
  const rotateRange = $('rotateRange');
  if (rotateInput && rotateRange) {
    rotateInput.addEventListener('input', () => {
      rotateRange.value = rotateInput.value;
      STATE.transformRotate = parseFloat(rotateInput.value);
      $('rotateVal').textContent = rotateInput.value + '°';
      applyAndSave();
    });
  }

  // Transform Origin Grid
  $$('.origin-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      $$('.origin-btn').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      STATE.styles.transformOrigin = btn.dataset.origin;
      applyAndSave();
    });
  });
}

function initFilterControls() {
  const filterMap = [
    ['filterBlurRange', 'blurVal', 'px', (v) => { STATE.filterBlur = parseFloat(v); }],
    ['filterBrightnessRange', 'brightnessVal', '%', (v) => { STATE.filterBrightness = parseFloat(v); }],
    ['filterContrastRange', 'contrastVal', '%', (v) => { STATE.filterContrast = parseFloat(v); }],
    ['filterSaturateRange', 'saturateVal', '%', (v) => { STATE.filterSaturate = parseFloat(v); }],
    ['filterHueRotateRange', 'hueRotateVal', '°', (v) => { STATE.filterHueRotate = parseFloat(v); }],
    ['filterInvertRange', 'invertVal', '%', (v) => { STATE.filterInvert = parseFloat(v); }],
    ['filterSepiaRange', 'sepiaVal', '%', (v) => { STATE.filterSepia = parseFloat(v); }],
    ['filterGrayscaleRange', 'grayscaleVal', '%', (v) => { STATE.filterGrayscale = parseFloat(v); }],
    ['backdropBlurRange', 'backdropBlurVal', 'px', (v) => { STATE.backdropBlur = parseFloat(v); }],
  ];

  filterMap.forEach(([id, valId, unit, fn]) => {
    const el = $(id);
    if (el) el.addEventListener('input', () => {
      fn(el.value);
      const valEl = $(valId);
      if (valEl) valEl.textContent = el.value + unit;
      applyAndSave();
    });
  });

  // Drop Shadow
  ['dropShadowX', 'dropShadowY', 'dropShadowBlur'].forEach(id => {
    const el = $(id);
    if (el) el.addEventListener('input', () => {
      STATE[id] = parseFloat(el.value);
      applyAndSave();
    });
  });

  // Cursor
  const cursor = $('cursor');
  if (cursor) cursor.addEventListener('change', () => { STATE.styles.cursor = cursor.value; applyAndSave(); });
}

function initAnimationControls() {
  /* Animation buttons */
  $$('.anim-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      $$('.anim-btn').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      const animName = btn.dataset.anim;
      STATE.styles.animationName = animName;
      // Restart animation
      const box = $('preview-box');
      if (box) {
        box.style.animationName = 'none';
        box.offsetHeight; // reflow
      }
      applyAndSave();
    });
  });

  /* Duration */
  const animDurRange = $('animationDurationRange');
  if (animDurRange) {
    animDurRange.addEventListener('input', () => {
      const val = animDurRange.value;
      $('animDurationVal').textContent = val + 's';
      STATE.styles.animationDuration = val + 's';
      applyAndSave();
    });
  }

  /* Delay */
  const animDelayRange = $('animationDelayRange');
  if (animDelayRange) {
    animDelayRange.addEventListener('input', () => {
      const val = animDelayRange.value;
      $('animDelayVal').textContent = val + 's';
      STATE.styles.animationDelay = val + 's';
      applyAndSave();
    });
  }

  /* Timing Function */
  const timingFn = $('animationTimingFunction');
  if (timingFn) {
    timingFn.addEventListener('change', () => {
      if (timingFn.value === 'custom') {
        openBezierEditor();
        return;
      }
      STATE.styles.animationTimingFunction = timingFn.value;
      applyAndSave();
    });
  }

  /* Iteration */
  const iteration = $('animationIterationCount');
  if (iteration) iteration.addEventListener('change', () => { STATE.styles.animationIterationCount = iteration.value; applyAndSave(); });

  /* Direction & Fill Mode */
  const direction = $('animationDirection');
  const fillMode = $('animationFillMode');
  if (direction) direction.addEventListener('change', () => { STATE.styles.animationDirection = direction.value; applyAndSave(); });
  if (fillMode) fillMode.addEventListener('change', () => { STATE.styles.animationFillMode = fillMode.value; applyAndSave(); });

  /* Play State Toggle */
  $$('.toggle-btn[data-play]').forEach(btn => {
    btn.addEventListener('click', () => {
      $$('.toggle-btn[data-play]').forEach(b => { b.classList.remove('active'); b.setAttribute('aria-pressed', 'false'); });
      btn.classList.add('active');
      btn.setAttribute('aria-pressed', 'true');
      STATE.styles.animationPlayState = btn.dataset.play;
      applyAndSave();
    });
  });

  /* Keyframes Apply */
  const applyKf = $('applyKeyframesBtn');
  if (applyKf) {
    applyKf.addEventListener('click', () => {
      const kfText = $('animationKeyframes').value;
      if (!kfText.trim()) return;
      STATE.customKeyframes = kfText;

      // Extract animation name from keyframes
      const match = kfText.match(/@keyframes\s+(\S+)/);
      if (match) {
        STATE.styles.animationName = match[1];
        const styleId = `kf-${match[1]}`;
        const existing = document.getElementById(styleId);
        if (existing) existing.remove();
        const el = document.createElement('style');
        el.id = styleId;
        el.textContent = kfText;
        document.head.appendChild(el);
      }
      applyAndSave();
      showToast('Keyframes uygulandı!', 'success');
    });
  }

  /* Open Bezier Editor */
  const openBezierBtn = $('openBezierEditor');
  if (openBezierBtn) openBezierBtn.addEventListener('click', openBezierEditor);
}

function initLayoutControls() {
  ['display', 'overflow', 'flexDirection', 'flexWrap', 'justifyContent', 'alignItems', 'position', 'zIndex',
    'gridTemplateColumns', 'gridTemplateRows'].forEach(id => {
    const el = $(id);
    if (!el) return;
    el.addEventListener('change', () => {
      STATE.styles[id] = el.value;
      // Show/hide flex/grid controls
      if (id === 'display') {
        const flexControls = $('flexControls');
        const gridControls = $('gridControls');
        if (flexControls) flexControls.style.display = (el.value === 'flex' || el.value === 'inline-flex') ? '' : 'none';
        if (gridControls) gridControls.style.display = (el.value === 'grid' || el.value === 'inline-grid') ? '' : 'none';
      }
      applyAndSave();
    });
  });

  // Gap
  const gap = $('gap');
  if (gap) gap.addEventListener('input', () => { STATE.styles.gap = gap.value; applyAndSave(); });

  // Box dimensions
  const boxWidth = $('boxWidth');
  const boxHeight = $('boxHeight');
  const widthUnit = $('widthUnit');
  const heightUnit = $('heightUnit');

  if (boxWidth && widthUnit) {
    const updateWidth = () => {
      const val = boxWidth.value;
      const unit = widthUnit.value;
      STATE.styles.width = val ? (val + unit) : '100%';
      applyAndSave();
    };
    boxWidth.addEventListener('input', updateWidth);
    widthUnit.addEventListener('change', updateWidth);
  }

  if (boxHeight && heightUnit) {
    const updateHeight = () => {
      const val = boxHeight.value;
      const unit = heightUnit.value;
      STATE.styles.height = val ? (val + unit) : '200px';
      applyAndSave();
    };
    boxHeight.addEventListener('input', updateHeight);
    heightUnit.addEventListener('change', updateHeight);
  }

  // Min/Max
  ['minWidth', 'maxWidth', 'minHeight', 'maxHeight'].forEach(id => {
    const el = $(id);
    if (el) el.addEventListener('input', () => { STATE.styles[id] = el.value || 'none'; applyAndSave(); });
  });

  // Margin (from box model)
  ['marginTop', 'marginRight', 'marginBottom', 'marginLeft'].forEach(id => {
    const el = $(id);
    if (el) el.addEventListener('input', () => applyAndSave());
  });
}

function initPaddingControls() {
  const paddingLinked = $('paddingLinked');
  const paddingUnit = $('paddingUnit');
  const sides = ['paddingTop', 'paddingRight', 'paddingBottom', 'paddingLeft'];

  const updatePadding = () => {
    const unit = paddingUnit ? paddingUnit.value : 'px';
    const vals = sides.map(id => {
      const el = $(id);
      return el ? (el.value || '0') + unit : '0px';
    });
    STATE.styles.padding = vals.join(' ');
    applyAndSave();
  };

  sides.forEach(id => {
    const el = $(id);
    if (el) el.addEventListener('input', () => {
      if (paddingLinked && paddingLinked.checked) {
        const val = el.value;
        sides.forEach(sid => { const other = $(sid); if (other) other.value = val; });
      }
      updatePadding();
    });
  });

  if (paddingUnit) paddingUnit.addEventListener('change', updatePadding);
}

function initTextGradientControls() {
  const textGradAngle = $('textGradientAngle');
  const textGradType = $('textGradientType');

  if (textGradAngle) textGradAngle.addEventListener('input', () => {
    STATE.textGradientAngle = parseInt(textGradAngle.value);
    if (STATE.textGradientActive) applyAndSave();
  });
  if (textGradType) textGradType.addEventListener('change', () => {
    STATE.textGradientType = textGradType.value;
    if (STATE.textGradientActive) applyAndSave();
  });

  const addTextGradColor = $('addTextGradientColor');
  if (addTextGradColor) {
    addTextGradColor.addEventListener('click', () => {
      STATE.textGradientColors.push({ color: randomHex(), stop: 100 });
      renderTextGradientColors();
      applyAndSave();
    });
  }

  const textImageFill = $('textImageFill');
  if (textImageFill) {
    textImageFill.addEventListener('input', () => {
      if (textImageFill.value) {
        const box = $('preview-box');
        if (box) {
          box.style.backgroundImage = `url('${textImageFill.value}')`;
          box.style.webkitBackgroundClip = 'text';
          box.style['-webkit-background-clip'] = 'text';
          box.style.webkitTextFillColor = 'transparent';
          box.style['-webkit-text-fill-color'] = 'transparent';
          box.style.backgroundClip = 'text';
          box.style.color = 'transparent';
          STATE.textGradientActive = true;
        }
      }
      applyAndSave();
    });
  }
}

/* ─────────────────────────────────────────────────────────────────────
   16. GRADIENT COLOR PICKERS (Dynamic)
───────────────────────────────────────────────────────────────────── */
function renderGradientColors() {
  const container = $('gradientColors');
  if (!container) return;
  container.innerHTML = '';

  STATE.gradientColors.forEach((gc, i) => {
    const row = document.createElement('div');
    row.className = 'gradient-color-row';
    row.innerHTML = `
      <input type="color" class="color-dot" value="${gc.color}">
      <input type="text" class="hex-input" value="${gc.color}" maxlength="9" placeholder="#ffffff">
      <input type="number" class="stop-input" value="${gc.stop}" min="0" max="100">
      <span class="stop-label">%</span>
      <button class="remove-btn" ${STATE.gradientColors.length <= 2 ? 'disabled' : ''}>
        <i class="fas fa-times"></i>
      </button>
    `;

    const colorInput = row.querySelector('.color-dot');
    const hexInput = row.querySelector('.hex-input');
    const stopInput = row.querySelector('.stop-input');
    const removeBtn = row.querySelector('.remove-btn');

    colorInput.addEventListener('input', () => {
      gc.color = colorInput.value;
      hexInput.value = colorInput.value;
      updateGradientPreviewBar();
      applyAndSave();
    });
    hexInput.addEventListener('input', () => {
      if (/^#[0-9A-Fa-f]{6}$/.test(hexInput.value)) {
        gc.color = hexInput.value;
        colorInput.value = hexInput.value;
        updateGradientPreviewBar();
        applyAndSave();
      }
    });
    stopInput.addEventListener('input', () => {
      gc.stop = parseInt(stopInput.value);
      updateGradientPreviewBar();
      applyAndSave();
    });
    removeBtn.addEventListener('click', () => {
      STATE.gradientColors.splice(i, 1);
      renderGradientColors();
      updateGradientPreviewBar();
      applyAndSave();
    });

    container.appendChild(row);
  });
}

function renderTextGradientColors() {
  const container = $('textGradientColors');
  if (!container) return;
  container.innerHTML = '';

  STATE.textGradientColors.forEach((gc, i) => {
    const row = document.createElement('div');
    row.className = 'gradient-color-row';
    row.innerHTML = `
      <input type="color" class="color-dot" value="${gc.color}">
      <input type="text" class="hex-input" value="${gc.color}" maxlength="9">
      <input type="number" class="stop-input" value="${gc.stop}" min="0" max="100">
      <span class="stop-label">%</span>
      <button class="remove-btn" ${STATE.textGradientColors.length <= 2 ? 'disabled' : ''}>
        <i class="fas fa-times"></i>
      </button>
    `;

    const colorInput = row.querySelector('.color-dot');
    const hexInput = row.querySelector('.hex-input');
    const stopInput = row.querySelector('.stop-input');
    const removeBtn = row.querySelector('.remove-btn');

    colorInput.addEventListener('input', () => { gc.color = colorInput.value; hexInput.value = colorInput.value; STATE.textGradientActive = true; applyAndSave(); });
    hexInput.addEventListener('input', () => { if (/^#[0-9A-Fa-f]{6}$/.test(hexInput.value)) { gc.color = hexInput.value; colorInput.value = hexInput.value; STATE.textGradientActive = true; applyAndSave(); } });
    stopInput.addEventListener('input', () => { gc.stop = parseInt(stopInput.value); STATE.textGradientActive = true; applyAndSave(); });
    removeBtn.addEventListener('click', () => { STATE.textGradientColors.splice(i, 1); renderTextGradientColors(); STATE.textGradientActive = true; applyAndSave(); });

    container.appendChild(row);
  });
}

function renderGradientBorderColors() {
  const container = $('gradientBorderColors');
  if (!container) return;
  container.innerHTML = '';

  STATE.gradientBorderColors.forEach((gc, i) => {
    const row = document.createElement('div');
    row.className = 'gradient-color-row';
    row.innerHTML = `
      <input type="color" class="color-dot" value="${gc.color}">
      <input type="number" class="stop-input" value="${gc.stop}" min="0" max="100">
      <span class="stop-label">%</span>
      <button class="remove-btn" ${STATE.gradientBorderColors.length <= 2 ? 'disabled' : ''}>
        <i class="fas fa-times"></i>
      </button>
    `;

    const colorInput = row.querySelector('.color-dot');
    const stopInput = row.querySelector('.stop-input');
    const removeBtn = row.querySelector('.remove-btn');

    colorInput.addEventListener('input', () => { gc.color = colorInput.value; });
    stopInput.addEventListener('input', () => { gc.stop = parseInt(stopInput.value); });
    removeBtn.addEventListener('click', () => { STATE.gradientBorderColors.splice(i, 1); renderGradientBorderColors(); });

    container.appendChild(row);
  });
}

function updateGradientPreviewBar() {
  const bar = $('gradientPreviewBar');
  if (!bar) return;
  bar.style.background = buildGradientCss();
}

/* ─────────────────────────────────────────────────────────────────────
   17. SHADOW LAYER UI
───────────────────────────────────────────────────────────────────── */
function addBoxShadowLayer(props = {}) {
  const layer = {
    id: Date.now(),
    x: props.x || 0,
    y: props.y || 4,
    blur: props.blur || 8,
    spread: props.spread || 0,
    color: props.color || 'rgba(0,0,0,0.5)',
    inset: props.inset || false,
    active: true,
  };
  STATE.boxShadowLayers.push(layer);
  renderBoxShadowLayers();
  applyAndSave();
}

function renderBoxShadowLayers() {
  const container = $('boxShadowLayers');
  if (!container) return;
  container.innerHTML = '';

  STATE.boxShadowLayers.forEach((layer, i) => {
    const div = document.createElement('div');
    div.className = 'shadow-layer';
    div.innerHTML = `
      <div class="shadow-layer-header">
        <label class="shadow-toggle">
          <input type="checkbox" ${layer.active ? 'checked' : ''}>
          <span>Katman ${i + 1}</span>
        </label>
        <label class="inset-toggle">
          <input type="checkbox" ${layer.inset ? 'checked' : ''}> inset
        </label>
        <button class="remove-shadow-btn"><i class="fas fa-times"></i></button>
      </div>
      <div class="shadow-layer-inputs">
        <div class="shadow-input-group"><label>X</label><input type="number" class="sx" value="${layer.x}"></div>
        <div class="shadow-input-group"><label>Y</label><input type="number" class="sy" value="${layer.y}"></div>
        <div class="shadow-input-group"><label>Blur</label><input type="number" class="sb" value="${layer.blur}" min="0"></div>
        <div class="shadow-input-group"><label>Spread</label><input type="number" class="ss" value="${layer.spread}"></div>
        <div class="shadow-input-group shadow-color-group"><label>Renk</label><input type="color" class="sc" value="${layer.color.startsWith('rgba') ? '#000000' : layer.color}"></div>
      </div>
    `;

    const toggle = div.querySelector('input[type="checkbox"]');
    const insetToggle = div.querySelector('.inset-toggle input');
    const removeBtn = div.querySelector('.remove-shadow-btn');
    const sx = div.querySelector('.sx');
    const sy = div.querySelector('.sy');
    const sb = div.querySelector('.sb');
    const ss = div.querySelector('.ss');
    const sc = div.querySelector('.sc');

    toggle.addEventListener('change', () => { layer.active = toggle.checked; applyAndSave(); });
    insetToggle.addEventListener('change', () => { layer.inset = insetToggle.checked; applyAndSave(); });
    removeBtn.addEventListener('click', () => { STATE.boxShadowLayers.splice(i, 1); renderBoxShadowLayers(); applyAndSave(); });
    sx.addEventListener('input', () => { layer.x = parseFloat(sx.value); applyAndSave(); });
    sy.addEventListener('input', () => { layer.y = parseFloat(sy.value); applyAndSave(); });
    sb.addEventListener('input', () => { layer.blur = parseFloat(sb.value); applyAndSave(); });
    ss.addEventListener('input', () => { layer.spread = parseFloat(ss.value); applyAndSave(); });
    sc.addEventListener('input', () => { layer.color = sc.value; applyAndSave(); });

    container.appendChild(div);
  });
}

function addTextShadowLayer(props = {}) {
  const layer = {
    id: Date.now(),
    x: props.x || 2,
    y: props.y || 2,
    blur: props.blur || 4,
    color: props.color || 'rgba(0,0,0,0.5)',
    active: true,
  };
  STATE.textShadowLayers.push(layer);
  renderTextShadowLayers();
  applyAndSave();
}

function renderTextShadowLayers() {
  const container = $('textShadowLayers');
  if (!container) return;
  container.innerHTML = '';

  STATE.textShadowLayers.forEach((layer, i) => {
    const div = document.createElement('div');
    div.className = 'shadow-layer';
    div.innerHTML = `
      <div class="shadow-layer-header">
        <label class="shadow-toggle">
          <input type="checkbox" ${layer.active ? 'checked' : ''}>
          <span>Gölge ${i + 1}</span>
        </label>
        <button class="remove-shadow-btn"><i class="fas fa-times"></i></button>
      </div>
      <div class="shadow-layer-inputs">
        <div class="shadow-input-group"><label>X</label><input type="number" class="sx" value="${layer.x}"></div>
        <div class="shadow-input-group"><label>Y</label><input type="number" class="sy" value="${layer.y}"></div>
        <div class="shadow-input-group"><label>Blur</label><input type="number" class="sb" value="${layer.blur}" min="0"></div>
        <div class="shadow-input-group"><label>Renk</label><input type="color" class="sc" value="${layer.color.startsWith('rgba') ? '#000000' : layer.color}"></div>
      </div>
    `;

    const toggle = div.querySelector('input[type="checkbox"]');
    const removeBtn = div.querySelector('.remove-shadow-btn');
    const sx = div.querySelector('.sx');
    const sy = div.querySelector('.sy');
    const sb = div.querySelector('.sb');
    const sc = div.querySelector('.sc');

    toggle.addEventListener('change', () => { layer.active = toggle.checked; applyAndSave(); });
    removeBtn.addEventListener('click', () => { STATE.textShadowLayers.splice(i, 1); renderTextShadowLayers(); applyAndSave(); });
    sx.addEventListener('input', () => { layer.x = parseFloat(sx.value); applyAndSave(); });
    sy.addEventListener('input', () => { layer.y = parseFloat(sy.value); applyAndSave(); });
    sb.addEventListener('input', () => { layer.blur = parseFloat(sb.value); applyAndSave(); });
    sc.addEventListener('input', () => { layer.color = sc.value; applyAndSave(); });

    container.appendChild(div);
  });
}

/* ─────────────────────────────────────────────────────────────────────
   18. PATTERN GALLERY
───────────────────────────────────────────────────────────────────── */
function initPatternGallery() {
  const gallery = $('patternGallery');
  if (!gallery) return;

  PATTERNS.forEach((pattern, i) => {
    const item = document.createElement('div');
    item.className = 'pattern-item';
    item.style.backgroundImage = pattern.css;
    item.style.backgroundSize = pattern.size;
    item.style.backgroundColor = '#333';
    item.title = pattern.name;
    item.innerHTML = `<span>${pattern.name}</span>`;
    item.addEventListener('click', () => {
      $$('.pattern-item').forEach(p => p.classList.remove('active'));
      item.classList.add('active');
      const box = $('preview-box');
      if (box) {
        box.style.backgroundImage = pattern.css;
        box.style.backgroundSize = pattern.size;
      }
      STATE.activeBgTab = 'bg-pattern';
      applyAndSave();
    });
    gallery.appendChild(item);
  });
}

/* ─────────────────────────────────────────────────────────────────────
   19. CLIP PATH GALLERY
───────────────────────────────────────────────────────────────────── */
function initClipShapeGallery() {
  const gallery = $('clipShapeGallery');
  if (!gallery) return;

  CLIP_SHAPES.forEach(shape => {
    const btn = document.createElement('button');
    btn.className = 'clip-shape-btn';
    btn.innerHTML = `<span class="clip-preview">${shape.preview}</span><span>${shape.name}</span>`;
    btn.title = shape.value;
    btn.addEventListener('click', () => {
      $$('.clip-shape-btn').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      STATE.styles.clipPath = shape.value;
      const clipInput = $('clipPath');
      if (clipInput) clipInput.value = shape.value;
      applyAndSave();
    });
    gallery.appendChild(btn);
  });
}

/* ─────────────────────────────────────────────────────────────────────
   20. PALETTE GENERATOR
───────────────────────────────────────────────────────────────────── */
function generatePalette() {
  const preview = $('palettePreview');
  if (!preview) return;

  try {
    let colors = [];
    const base = STATE.paletteBaseColor;
    const size = STATE.paletteSize;
    const baseChroma = chroma(base);

    switch (STATE.paletteType) {
      case 'monochromatic':
        colors = chroma.scale([baseChroma.brighten(2), base, baseChroma.darken(2)]).mode('lab').colors(size);
        break;
      case 'analogous':
        colors = Array.from({ length: size }, (_, i) => chroma(base).set('hsl.h', `+${(i - Math.floor(size / 2)) * 30}`).hex());
        break;
      case 'complementary':
        colors = [base, chroma(base).set('hsl.h', '+180').hex(), ...chroma.scale([base, chroma(base).set('hsl.h', '+180').hex()]).colors(size - 2)];
        break;
      case 'triadic':
        colors = [base, chroma(base).set('hsl.h', '+120').hex(), chroma(base).set('hsl.h', '+240').hex(), ...Array.from({ length: size - 3 }, (_, i) => chroma(base).set('hsl.h', `+${(i + 1) * 60}`).hex())].slice(0, size);
        break;
      case 'split-complementary':
        colors = [base, chroma(base).set('hsl.h', '+150').hex(), chroma(base).set('hsl.h', '+210').hex(), ...chroma.scale([base, chroma(base).set('hsl.h', '+180').hex()]).colors(size - 3)].slice(0, size);
        break;
      case 'tetradic':
        colors = [base, chroma(base).set('hsl.h', '+90').hex(), chroma(base).set('hsl.h', '+180').hex(), chroma(base).set('hsl.h', '+270').hex(), ...chroma.scale([base, chroma(base).set('hsl.h', '+180').hex()]).colors(size - 4)].slice(0, size);
        break;
      case 'shades':
        colors = chroma.scale(['#ffffff', base, '#000000']).mode('lab').colors(size);
        break;
      case 'pastel':
        colors = Array.from({ length: size }, (_, i) => chroma(base).set('hsl.h', `+${i * (360 / size)}`).set('hsl.s', 0.4).set('hsl.l', 0.75).hex());
        break;
      default:
        colors = chroma.scale([base, chroma(base).set('hsl.h', '+180').hex()]).mode('lab').colors(size);
    }

    STATE.palette = colors;
    preview.innerHTML = '';
    colors.forEach((c, i) => {
      const swatch = document.createElement('div');
      swatch.className = 'palette-swatch';
      swatch.style.backgroundColor = c;
      swatch.title = c;
      swatch.dataset.color = c;
      swatch.innerHTML = `<span class="palette-hex">${c}</span>`;
      swatch.addEventListener('click', () => {
        navigator.clipboard.writeText(c);
        showToast(`${c} kopyalandı!`, 'success', 1500);
      });
      swatch.addEventListener('dblclick', () => {
        STATE.styles.color = c;
        applyAndSave();
        showToast(`Yazı rengi: ${c}`, 'info', 1500);
      });
      preview.appendChild(swatch);
    });
  } catch (e) {
    // Fallback without chroma.js
    const colors = Array.from({ length: STATE.paletteSize }, () => randomHex());
    STATE.palette = colors;
    preview.innerHTML = '';
    colors.forEach(c => {
      const swatch = document.createElement('div');
      swatch.className = 'palette-swatch';
      swatch.style.backgroundColor = c;
      swatch.title = c;
      swatch.innerHTML = `<span class="palette-hex">${c}</span>`;
      swatch.addEventListener('click', () => { navigator.clipboard.writeText(c); showToast(`${c} kopyalandı!`, 'success', 1500); });
      preview.appendChild(swatch);
    });
  }
}

/* ─────────────────────────────────────────────────────────────────────
   21. STYLE BUTTONS (Random & Quick Actions)
───────────────────────────────────────────────────────────────────── */
function initStyleButtons() {
  $$('[data-style-target]').forEach(btn => {
    btn.addEventListener('click', () => handleStyleTarget(btn.dataset.styleTarget));
  });
}

function handleStyleTarget(target) {
  const s = STATE.styles;
  const FONTS = [
    "'Poppins', sans-serif", "'Inter', sans-serif", "'Orbitron', sans-serif",
    "'Bebas Neue', sans-serif", "'VT323', monospace", "'Press Start 2P', monospace",
    "'Lobster', cursive", "'Dancing Script', cursive", "'Playfair Display', serif",
    "'Cinzel', serif", "'Raleway', sans-serif", "'Righteous', sans-serif",
    "'Monoton', cursive", "'Space Grotesk', sans-serif", "'JetBrains Mono', monospace",
    "'Pacifico', cursive", "'Nunito', sans-serif", "'Exo 2', sans-serif",
    "'Kaushan Script', cursive", "'Fira Code', monospace", "'Bungee', sans-serif",
  ];

  switch (target) {
    /* ── Text Panel ── */
    case 'random-font':
      s.fontFamily = randPick(FONTS);
      syncSelect('fontFamily', s.fontFamily);
      updateFontPreview(s.fontFamily);
      break;
    case 'random-color':
      s.color = randomHex();
      if (COLOR_PICKERS.text) try { COLOR_PICKERS.text.color = s.color; } catch (e) {}
      if ($('textColorHex')) $('textColorHex').value = s.color;
      if ($('textColorSwatch')) $('textColorSwatch').style.background = s.color;
      break;
    case 'random-text-shadow':
      STATE.textShadowLayers = [];
      addTextShadowLayer({ x: randInt(-10, 10), y: randInt(-10, 10), blur: randInt(0, 20), color: randomHex() });
      return;
    case 'random-multi-text-shadow':
      STATE.textShadowLayers = [];
      const shadowCount = randInt(2, 5);
      for (let i = 0; i < shadowCount; i++) {
        addTextShadowLayer({ x: randInt(-15, 15), y: randInt(-15, 15), blur: randInt(0, 30), color: randomHex() });
      }
      return;
    case 'random-text-decoration':
      s.textDecorationLine = randPick(['none', 'underline', 'overline', 'line-through', 'underline overline']);
      s.textDecorationStyle = randPick(['solid', 'double', 'dotted', 'dashed', 'wavy']);
      s.textDecorationColor = randomHex();
      syncSelect('textDecorationLine', s.textDecorationLine);
      syncSelect('textDecorationStyle', s.textDecorationStyle);
      break;
    case 'random-spacing':
      s.letterSpacing = randInt(-2, 10) + 'px';
      s.wordSpacing = randInt(0, 20) + 'px';
      break;
    case 'random-align':
      s.textAlign = randPick(['left', 'center', 'right', 'justify']);
      $$('.align-btn').forEach(b => {
        b.classList.toggle('active', b.dataset.align === s.textAlign);
        b.setAttribute('aria-pressed', b.dataset.align === s.textAlign);
      });
      break;
    case 'random-line-height':
      s.lineHeight = (rand(0.8, 3)).toFixed(1);
      if ($('lineHeightRange')) $('lineHeightRange').value = s.lineHeight;
      if ($('lineHeightVal')) $('lineHeightVal').textContent = s.lineHeight;
      break;
    case 'random-text-transform':
      s.textTransform = randPick(['none', 'uppercase', 'lowercase', 'capitalize']);
      syncSelect('textTransform', s.textTransform);
      break;
    case 'random-text-stroke':
      STATE.textStrokeWidth = rand(0.5, 4);
      STATE.textStrokeColor = randomHex();
      if ($('textStrokeWidthRange')) $('textStrokeWidthRange').value = STATE.textStrokeWidth;
      if ($('textStrokeWidthVal')) $('textStrokeWidthVal').textContent = STATE.textStrokeWidth.toFixed(1) + 'px';
      break;

    /* ── Background Panel ── */
    case 'random-bg-color':
      s.backgroundColor = randomHex();
      STATE.activeBgTab = 'bg-solid';
      if (COLOR_PICKERS.bg) try { COLOR_PICKERS.bg.color = s.backgroundColor; } catch (e) {}
      if ($('bgColorHex')) $('bgColorHex').value = s.backgroundColor;
      if ($('bgColorSwatch')) $('bgColorSwatch').style.background = s.backgroundColor;
      break;
    case 'random-gradient':
      STATE.gradientColors = [
        { color: randomHex(), stop: 0 },
        { color: randomHex(), stop: 50 },
        { color: randomHex(), stop: 100 },
      ];
      STATE.gradientAngle = randInt(0, 360);
      STATE.gradientType = randPick(['linear', 'radial', 'conic']);
      STATE.activeBgTab = 'bg-gradient';
      renderGradientColors();
      updateGradientPreviewBar();
      break;
    case 'random-bg-gif':
      const gifs = [
        'https://media.giphy.com/media/3o7TKSx0g7RqRnVqqM/giphy.gif',
        'https://media.giphy.com/media/26n6WywJyh39n1pBu/giphy.gif',
        'https://media.giphy.com/media/l4FGuhL4U2WyjdkaY/giphy.gif',
      ];
      s.backgroundImage = randPick(gifs);
      s.backgroundSize = 'cover';
      STATE.activeBgTab = 'bg-image';
      if ($('backgroundImageUrl')) $('backgroundImageUrl').value = s.backgroundImage;
      break;
    case 'random-bg-position':
      const positions = ['top left', 'top center', 'top right', 'center left', 'center center', 'center right', 'bottom left', 'bottom center', 'bottom right'];
      s.backgroundPosition = randPick(positions);
      $$('.pos-btn').forEach(b => b.classList.toggle('active', b.dataset.pos === s.backgroundPosition));
      break;
    case 'random-bg-size':
      s.backgroundSize = randPick(['auto', 'cover', 'contain', '50% 50%', '100% 100%']);
      syncSelect('backgroundSize', s.backgroundSize);
      break;
    case 'random-bg-opacity':
      s.opacity = rand(0.3, 1).toFixed(2);
      if ($('backgroundOpacityRange')) $('backgroundOpacityRange').value = s.opacity;
      if ($('bgOpacityVal')) $('bgOpacityVal').textContent = s.opacity;
      break;
    case 'random-bg-pattern':
      const pattern = randPick(PATTERNS);
      const box = $('preview-box');
      if (box) { box.style.backgroundImage = pattern.css; box.style.backgroundSize = pattern.size; }
      STATE.activeBgTab = 'bg-pattern';
      break;
    case 'random-bg-blend':
      const blendModes = ['normal', 'multiply', 'screen', 'overlay', 'darken', 'lighten', 'color-dodge', 'difference', 'exclusion', 'hue', 'saturation', 'luminosity'];
      s.backgroundBlendMode = randPick(blendModes);
      syncSelect('backgroundBlendMode', s.backgroundBlendMode);
      break;
    case 'random-mesh-gradient':
      const c1 = randomHex(), c2 = randomHex(), c3 = randomHex(), c4 = randomHex();
      STATE.gradientColors = [
        { color: c1, stop: 0 }, { color: c2, stop: 33 },
        { color: c3, stop: 66 }, { color: c4, stop: 100 },
      ];
      STATE.gradientType = 'radial';
      STATE.activeBgTab = 'bg-gradient';
      renderGradientColors();
      break;
    case 'random-noise-texture':
      const noiseBox = $('preview-box');
      if (noiseBox) {
        noiseBox.style.backgroundImage = `url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noise'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noise)' opacity='0.2'/%3E%3C/svg%3E")`;
        noiseBox.style.backgroundSize = '256px 256px';
      }
      STATE.activeBgTab = 'bg-pattern';
      break;

    /* ── Border Panel ── */
    case 'random-multi-border':
      const bStyles = ['solid', 'dashed', 'dotted', 'double', 'groove', 'ridge'];
      const bWidth = randInt(1, 5);
      const bColor = randomHex();
      const bStyle = randPick(bStyles);
      const borderVal = `${bWidth}px ${bStyle} ${bColor}`;
      ['Top', 'Right', 'Bottom', 'Left'].forEach(side => {
        s[`border${side}`] = borderVal;
        const inp = $(`border${side}`);
        if (inp) inp.value = borderVal;
      });
      break;
    case 'random-outline':
      s.outlineWidth = randInt(1, 5);
      s.outlineStyle = randPick(['solid', 'dashed', 'dotted', 'double', 'groove', 'ridge']);
      s.outlineColor = randomHex();
      s.outlineOffset = randInt(0, 8) + 'px';
      if ($('outlineWidth')) $('outlineWidth').value = s.outlineWidth;
      syncSelect('outlineStyle', s.outlineStyle);
      break;
    case 'random-border-radius':
      if (Math.random() > 0.5) {
        const r = randInt(0, 50);
        ['TopLeft', 'TopRight', 'BottomLeft', 'BottomRight'].forEach(corner => {
          s[`border${corner}Radius`] = r + 'px';
          const inp = $(`borderRadius${corner}`);
          if (inp) inp.value = r;
        });
        if ($('borderRadiusAll')) $('borderRadiusAll').value = r;
        if ($('borderRadiusVal')) $('borderRadiusVal').textContent = r + 'px';
      } else {
        const corners = ['TopLeft', 'TopRight', 'BottomLeft', 'BottomRight'];
        corners.forEach(corner => {
          const r = randInt(0, 80);
          s[`border${corner}Radius`] = r + 'px';
          const inp = $(`borderRadius${corner}`);
          if (inp) inp.value = r;
        });
      }
      break;
    case 'random-border-color':
      const newBorderColor = randomHex();
      ['Top', 'Right', 'Bottom', 'Left'].forEach(side => {
        const inp = $(`border${side}`);
        if (inp && inp.value) {
          const parts = inp.value.split(' ');
          if (parts.length >= 2) {
            s[`border${side}`] = `${parts[0]} ${parts[1]} ${newBorderColor}`;
            inp.value = s[`border${side}`];
          }
        }
      });
      break;
    case 'random-gradient-border':
    case 'applyGradientBorder':
      applyGradientBorder();
      return;
    case 'random-border-image':
      const box2 = $('preview-box');
      if (box2) {
        box2.style.borderImage = `linear-gradient(${randInt(0, 360)}deg, ${randomHex()}, ${randomHex()}) 1`;
        box2.style.borderWidth = randInt(2, 8) + 'px';
        box2.style.borderStyle = 'solid';
      }
      break;

    /* ── Transform Panel ── */
    case 'random-transform':
      STATE.transformRotate = randInt(-45, 45);
      STATE.transformScaleX = rand(0.7, 1.3);
      STATE.transformScaleY = rand(0.7, 1.3);
      STATE.transformSkewX = randInt(-15, 15);
      STATE.transformSkewY = randInt(-15, 15);
      STATE.transformTranslateX = randInt(-20, 20);
      STATE.transformTranslateY = randInt(-20, 20);
      syncTransformUI();
      break;
    case 'random-3d-transform':
      STATE.transformRotateX = randInt(-60, 60);
      STATE.transformRotateY = randInt(-60, 60);
      STATE.transformRotateZ = randInt(-45, 45);
      STATE.transformPerspective = randInt(400, 1200);
      syncTransformUI();
      break;
    case 'reset-transform':
      STATE.transformRotate = 0;
      STATE.transformScaleX = 1; STATE.transformScaleY = 1;
      STATE.transformSkewX = 0; STATE.transformSkewY = 0;
      STATE.transformTranslateX = 0; STATE.transformTranslateY = 0;
      STATE.transformRotateX = 0; STATE.transformRotateY = 0;
      STATE.transformRotateZ = 0; STATE.transformPerspective = 0;
      syncTransformUI();
      break;

    /* ── Shadow Panel ── */
    case 'random-box-shadow':
      STATE.boxShadowLayers = [];
      addBoxShadowLayer({ x: randInt(-20, 20), y: randInt(-20, 20), blur: randInt(0, 40), spread: randInt(-5, 15), color: randomHex() });
      return;
    case 'random-box-shadow-color':
      if (STATE.boxShadowLayers.length > 0) {
        STATE.boxShadowLayers[0].color = randomHex();
        renderBoxShadowLayers();
      }
      break;
    case 'random-multi-shadow':
      STATE.boxShadowLayers = [];
      const shadowNum = randInt(2, 4);
      for (let i = 0; i < shadowNum; i++) {
        STATE.boxShadowLayers.push({
          id: Date.now() + i, x: randInt(-20, 20), y: randInt(-20, 20),
          blur: randInt(0, 40), spread: randInt(-5, 10), color: randomHex(), inset: false, active: true,
        });
      }
      renderBoxShadowLayers();
      break;
    case 'random-inset-shadow':
      STATE.boxShadowLayers = [];
      STATE.boxShadowLayers.push({
        id: Date.now(), x: randInt(-10, 10), y: randInt(-10, 10),
        blur: randInt(5, 30), spread: randInt(-5, 5), color: randomHex(), inset: true, active: true,
      });
      renderBoxShadowLayers();
      break;
    case 'random-neon-glow':
      const neonColor = randomHex();
      STATE.boxShadowLayers = [
        { id: 1, x: 0, y: 0, blur: 10, spread: 0, color: neonColor, inset: false, active: true },
        { id: 2, x: 0, y: 0, blur: 30, spread: 0, color: neonColor, inset: false, active: true },
        { id: 3, x: 0, y: 0, blur: 60, spread: 0, color: neonColor + '80', inset: false, active: true },
      ];
      s.color = neonColor;
      STATE.textShadowLayers = [
        { id: 10, x: 0, y: 0, blur: 10, color: neonColor, active: true },
        { id: 11, x: 0, y: 0, blur: 20, color: neonColor, active: true },
      ];
      renderBoxShadowLayers();
      renderTextShadowLayers();
      break;
    case 'random-long-shadow':
      STATE.boxShadowLayers = [];
      const longColor = randomHex() + '40';
      for (let i = 1; i <= 20; i++) {
        STATE.boxShadowLayers.push({ id: i, x: i, y: i, blur: 0, spread: 0, color: longColor, inset: false, active: true });
      }
      renderBoxShadowLayers();
      break;

    /* ── Animation Panel ── */
    case 'random-animation':
      const animKeys = Object.keys(KEYFRAMES);
      s.animationName = randPick(animKeys);
      s.animationDuration = rand(0.5, 3).toFixed(1) + 's';
      s.animationIterationCount = 'infinite';
      $$('.anim-btn').forEach(b => b.classList.toggle('active', b.dataset.anim === s.animationName));
      if ($('animationDurationRange')) $('animationDurationRange').value = parseFloat(s.animationDuration);
      if ($('animDurationVal')) $('animDurationVal').textContent = s.animationDuration;
      break;
    case 'random-timing-function':
      const timings = ['ease', 'linear', 'ease-in', 'ease-out', 'ease-in-out', 'cubic-bezier(0.68,-0.55,0.265,1.55)', 'cubic-bezier(0.25,0.46,0.45,0.94)'];
      s.animationTimingFunction = randPick(timings);
      syncSelect('animationTimingFunction', s.animationTimingFunction);
      break;
    case 'random-iteration-count':
      s.animationIterationCount = randPick(['1', '2', '3', '5', '10', 'infinite']);
      syncSelect('animationIterationCount', s.animationIterationCount);
      break;
    case 'stop-animation':
      s.animationName = 'none';
      $$('.anim-btn').forEach(b => b.classList.remove('active'));
      break;
    case 'pause-animation':
      s.animationPlayState = 'paused';
      $$('.toggle-btn[data-play]').forEach(b => {
        b.classList.toggle('active', b.dataset.play === 'paused');
        b.setAttribute('aria-pressed', b.dataset.play === 'paused');
      });
      break;
    case 'play-animation':
      s.animationPlayState = 'running';
      $$('.toggle-btn[data-play]').forEach(b => {
        b.classList.toggle('active', b.dataset.play === 'running');
        b.setAttribute('aria-pressed', b.dataset.play === 'running');
      });
      break;

    /* ── Clip Panel ── */
    case 'random-clip-path':
      s.clipPath = randPick(CLIP_SHAPES.filter(sh => sh.value !== 'none')).value;
      if ($('clipPath')) $('clipPath').value = s.clipPath;
      $$('.clip-shape-btn').forEach(b => b.classList.toggle('active', b.title === s.clipPath));
      break;
    case 'reset-clip':
      s.clipPath = 'none';
      if ($('clipPath')) $('clipPath').value = 'none';
      $$('.clip-shape-btn').forEach(b => b.classList.remove('active'));
      break;

    /* ── Text Gradient Panel ── */
    case 'random-text-opacity':
      s.opacity = rand(0.3, 1).toFixed(2);
      if ($('textOpacityRange')) $('textOpacityRange').value = s.opacity;
      if ($('textOpacityVal')) $('textOpacityVal').textContent = s.opacity;
      break;
    case 'random-text-gradient':
      STATE.textGradientColors = [
        { color: randomHex(), stop: 0 },
        { color: randomHex(), stop: 50 },
        { color: randomHex(), stop: 100 },
      ];
      STATE.textGradientAngle = randInt(0, 360);
      STATE.textGradientActive = true;
      renderTextGradientColors();
      break;
    case 'random-text-image-fill':
      const images = [
        'https://picsum.photos/400/200?random=1',
        'https://picsum.photos/400/200?random=2',
        'https://picsum.photos/400/200?random=3',
      ];
      STATE.textGradientActive = true;
      const imgUrl = randPick(images);
      const fillBox = $('preview-box');
      if (fillBox) {
        fillBox.style.backgroundImage = `url('${imgUrl}')`;
        fillBox.style.webkitBackgroundClip = 'text';
        fillBox.style['-webkit-background-clip'] = 'text';
        fillBox.style.webkitTextFillColor = 'transparent';
        fillBox.style['-webkit-text-fill-color'] = 'transparent';
        fillBox.style.backgroundClip = 'text';
        fillBox.style.backgroundSize = 'cover';
      }
      if ($('textImageFill')) $('textImageFill').value = imgUrl;
      break;
    case 'reset-text-fill':
      STATE.textGradientActive = false;
      const resetBox = $('preview-box');
      if (resetBox) {
        resetBox.style.webkitBackgroundClip = '';
        resetBox.style['-webkit-background-clip'] = '';
        resetBox.style.webkitTextFillColor = '';
        resetBox.style['-webkit-text-fill-color'] = '';
        resetBox.style.backgroundClip = '';
        resetBox.style.color = s.color;
      }
      break;

    /* ── Filter Panel ── */
    case 'random-filter':
      STATE.filterBrightness = randInt(70, 150);
      STATE.filterContrast = randInt(80, 200);
      STATE.filterSaturate = randInt(50, 300);
      STATE.filterHueRotate = randInt(0, 360);
      STATE.filterBlur = randInt(0, 5);
      STATE.filterSepia = randInt(0, 50);
      syncFilterUI();
      break;
    case 'filter-vintage':
      STATE.filterSepia = 60;
      STATE.filterContrast = 110;
      STATE.filterBrightness = 90;
      STATE.filterSaturate = 80;
      syncFilterUI();
      break;
    case 'filter-cold':
      STATE.filterHueRotate = 200;
      STATE.filterSaturate = 130;
      STATE.filterBrightness = 110;
      STATE.filterContrast = 90;
      syncFilterUI();
      break;
    case 'filter-warm':
      STATE.filterSepia = 30;
      STATE.filterSaturate = 140;
      STATE.filterBrightness = 110;
      STATE.filterHueRotate = 10;
      syncFilterUI();
      break;
    case 'filter-dramatic':
      STATE.filterContrast = 200;
      STATE.filterBrightness = 80;
      STATE.filterSaturate = 50;
      STATE.filterGrayscale = 20;
      syncFilterUI();
      break;
    case 'random-cursor':
      const cursors = ['pointer', 'crosshair', 'move', 'grab', 'zoom-in', 'not-allowed', 'cell', 'help', 'wait'];
      s.cursor = randPick(cursors);
      syncSelect('cursor', s.cursor);
      break;
    case 'random-effect':
      handleStyleTarget('random-filter');
      handleStyleTarget('random-box-shadow');
      handleStyleTarget('random-border-radius');
      break;
    case 'reset-filters':
      STATE.filterBlur = 0; STATE.filterBrightness = 100; STATE.filterContrast = 100;
      STATE.filterSaturate = 100; STATE.filterHueRotate = 0; STATE.filterInvert = 0;
      STATE.filterSepia = 0; STATE.filterGrayscale = 0; STATE.backdropBlur = 0;
      STATE.dropShadowX = 0; STATE.dropShadowY = 0; STATE.dropShadowBlur = 0;
      syncFilterUI();
      break;

    /* ── Palette Panel ── */
    case 'generate-palette':
    case 'random-palette':
      if (target === 'random-palette') {
        STATE.paletteBaseColor = randomHex();
        STATE.paletteType = randPick(['monochromatic', 'analogous', 'complementary', 'triadic', 'pastel', 'shades']);
        if (COLOR_PICKERS.palette) try { COLOR_PICKERS.palette.color = STATE.paletteBaseColor; } catch (e) {}
        syncSelect('paletteType', STATE.paletteType);
      }
      generatePalette();
      return;
    case 'export-palette':
      if (STATE.palette.length) {
        const json = JSON.stringify({ palette: STATE.palette, type: STATE.paletteType, base: STATE.paletteBaseColor }, null, 2);
        downloadFile('palette.json', json, 'application/json');
        showToast('Palet dışa aktarıldı!', 'success');
      }
      return;
    case 'copy-palette-css':
      if (STATE.palette.length) {
        const cssVars = STATE.palette.map((c, i) => `  --color-${i + 1}: ${c};`).join('\n');
        const cssPalette = `:root {\n${cssVars}\n}`;
        copyToClipboard(cssPalette);
        showToast('Palet CSS kopyalandı!', 'success');
      }
      return;

    /* ── Themes ── */
    case 'auto-theme-neon': case 'auto-theme-cyberpunk': case 'auto-theme-dark-elegant':
    case 'auto-theme-matrix': case 'auto-theme-minimal': case 'auto-theme-vintage':
    case 'auto-theme-pastel': case 'auto-theme-glassmorphism': case 'auto-theme-neumorphism':
    case 'auto-theme-aurora': case 'auto-theme-holographic': case 'auto-theme-nature':
    case 'auto-theme-ocean': case 'auto-theme-sunset': case 'auto-theme-forest':
    case 'auto-theme-candy': case 'auto-theme-retrowave': case 'auto-theme-brutalist':
    case 'auto-theme-lofi': case 'auto-theme-paper':
      applyTheme(target);
      return;

    /* ── Chaos / Auto ── */
    case 'auto-generate':
      autoGenerateStyle();
      return;
    case 'max-chaos':
      maxChaos();
      return;

    /* ── Palette to Gradient ── */
    case 'export-palette':
    // handled above

    default:
      break;
  }

  applyAndSave();
}

function applyTheme(themeKey) {
  const theme = THEMES[themeKey];
  if (!theme) return;

  // Reset
  STATE.boxShadowLayers = [];
  STATE.textShadowLayers = [];
  STATE.textGradientActive = false;
  STATE.filterBlur = 0; STATE.filterBrightness = 100; STATE.filterContrast = 100;
  STATE.filterSaturate = 100; STATE.filterHueRotate = 0; STATE.filterInvert = 0;
  STATE.filterSepia = 0; STATE.filterGrayscale = 0;

  // Apply theme values
  Object.entries(theme).forEach(([k, v]) => {
    if (k in STATE.styles) {
      STATE.styles[k] = v;
    }
  });

  // Special: parse text-shadow if given
  if (theme.textShadow) {
    STATE.styles.textShadow = theme.textShadow;
  }

  // Special: parse box-shadow if given
  if (theme.boxShadow) {
    STATE.styles.boxShadow = theme.boxShadow;
  }

  // Special: filter
  if (theme.filter) {
    const sepiaMatch = theme.filter.match(/sepia\((\d+)%\)/);
    if (sepiaMatch) STATE.filterSepia = parseInt(sepiaMatch[1]);
  }

  if (theme.backdropFilter) STATE.backdropBlur = 10;

  syncAllControls();
  applyAndSave();
  showToast(`Tema uygulandı! ✨`, 'success');
}

/* ─────────────────────────────────────────────────────────────────────
   22. AUTO GENERATE & MAX CHAOS
───────────────────────────────────────────────────────────────────── */
function autoGenerateStyle() {
  const chaosLvl = parseInt(($('chaosLevel') || {}).value || 5);
  const useFont = !$('chaosFont') || $('chaosFont').checked;
  const useBg = !$('chaosBackground') || $('chaosBackground').checked;
  const useBorder = !$('chaosBorder') || $('chaosBorder').checked;
  const useEffects = !$('chaosEffects') || $('chaosEffects').checked;
  const useAnimation = !$('chaosAnimation') || $('chaosAnimation').checked;
  const useClip = !$('chaosClip') || $('chaosClip').checked;
  const useTransform = !$('chaosTransform') || $('chaosTransform').checked;
  const useBoxShadow = !$('chaosBoxShadow') || $('chaosBoxShadow').checked;
  const useGradient = !$('chaosTextGradient') || $('chaosTextGradient').checked;
  const useOpacity = !$('chaosOpacity') || $('chaosOpacity').checked;

  const FONTS = [
    "'Poppins', sans-serif", "'Inter', sans-serif", "'Orbitron', sans-serif",
    "'Bebas Neue', sans-serif", "'VT323', monospace", "'Lobster', cursive",
    "'Playfair Display', serif", "'Cinzel', serif", "'Righteous', sans-serif",
    "'Nunito', sans-serif", "'Space Grotesk', sans-serif", "'Pacifico', cursive",
  ];

  if (useFont) {
    STATE.styles.fontFamily = randPick(FONTS);
    STATE.styles.fontWeight = randPick(['400', '600', '700', '800', '900']);
    STATE.styles.fontSize = randInt(18, 48 + chaosLvl * 3) + 'px';
    STATE.styles.letterSpacing = randInt(-1, chaosLvl) + 'px';
    STATE.styles.textTransform = randPick(['none', 'uppercase', 'capitalize']);
    STATE.styles.fontStyle = Math.random() > 0.8 ? 'italic' : 'normal';
    STATE.styles.color = randomHex();
  }

  if (useBg) {
    if (Math.random() > 0.5) {
      STATE.gradientColors = [
        { color: randomHex(), stop: 0 },
        { color: randomHex(), stop: 50 },
        { color: randomHex(), stop: 100 },
      ];
      STATE.gradientAngle = randInt(0, 360);
      STATE.gradientType = randPick(['linear', 'radial', 'conic']);
      STATE.activeBgTab = 'bg-gradient';
    } else {
      STATE.styles.backgroundColor = randomHex();
      STATE.activeBgTab = 'bg-solid';
    }
  }

  if (useBorder) {
    const bStyles = ['solid', 'dashed', 'dotted', 'double'];
    const bWidth = randInt(0, chaosLvl > 5 ? 4 : 2);
    const bColor = randomHex();
    const bStyle = randPick(bStyles);
    const bv = bWidth > 0 ? `${bWidth}px ${bStyle} ${bColor}` : 'none';
    ['Top', 'Right', 'Bottom', 'Left'].forEach(side => {
      STATE.styles[`border${side}`] = bv;
    });
    const radius = randInt(0, chaosLvl * 8);
    ['TopLeft', 'TopRight', 'BottomLeft', 'BottomRight'].forEach(corner => {
      STATE.styles[`border${corner}Radius`] = (chaosLvl > 7 ? randInt(0, 80) : radius) + 'px';
    });
  }

  if (useBoxShadow) {
    STATE.boxShadowLayers = [];
    const shadowCount = randInt(1, Math.min(chaosLvl, 4));
    for (let i = 0; i < shadowCount; i++) {
      STATE.boxShadowLayers.push({
        id: Date.now() + i,
        x: randInt(-chaosLvl * 3, chaosLvl * 3),
        y: randInt(-chaosLvl * 3, chaosLvl * 3),
        blur: randInt(0, chaosLvl * 8),
        spread: randInt(-3, 5),
        color: randomHex() + (chaosLvl < 5 ? '99' : ''),
        inset: Math.random() > 0.8,
        active: true,
      });
    }
    renderBoxShadowLayers();
  }

  if (useTransform && chaosLvl > 3) {
    STATE.transformRotate = randInt(-chaosLvl * 5, chaosLvl * 5);
    STATE.transformScaleX = rand(0.8, 1.2);
    STATE.transformScaleY = rand(0.8, 1.2);
    if (chaosLvl > 6) {
      STATE.transformSkewX = randInt(-10, 10);
      STATE.transformSkewY = randInt(-10, 10);
    }
    syncTransformUI();
  }

  if (useEffects && chaosLvl > 4) {
    STATE.filterBrightness = randInt(80, 130);
    STATE.filterContrast = randInt(80, 150);
    STATE.filterSaturate = randInt(80, 200);
    STATE.filterHueRotate = chaosLvl > 7 ? randInt(0, 360) : randInt(0, 60);
    syncFilterUI();
  }

  if (useAnimation && Math.random() > (1 - chaosLvl / 12)) {
    const animKeys = Object.keys(KEYFRAMES);
    STATE.styles.animationName = randPick(animKeys);
    STATE.styles.animationDuration = rand(0.5, 3).toFixed(1) + 's';
    STATE.styles.animationIterationCount = 'infinite';
    STATE.styles.animationTimingFunction = randPick(['ease', 'ease-in-out', 'linear', 'cubic-bezier(0.68,-0.55,0.265,1.55)']);
  }

  if (useGradient && Math.random() > 0.6) {
    STATE.textGradientColors = [{ color: randomHex(), stop: 0 }, { color: randomHex(), stop: 50 }, { color: randomHex(), stop: 100 }];
    STATE.textGradientActive = true;
    renderTextGradientColors();
  } else {
    STATE.textGradientActive = false;
  }

  if (useClip && chaosLvl > 6 && Math.random() > 0.7) {
    const shapes = CLIP_SHAPES.filter(s => s.value !== 'none');
    STATE.styles.clipPath = randPick(shapes).value;
  }

  if (useOpacity && chaosLvl > 5) {
    STATE.styles.opacity = rand(0.6, 1).toFixed(2);
  }

  syncAllControls();
  applyAndSave();
  showToast('Otomatik stil oluşturuldu! 🎨', 'success');
}

function maxChaos() {
  // Override chaos level
  const savedLevel = ($('chaosLevel') || {}).value;
  if ($('chaosLevel')) $('chaosLevel').value = 10;

  // Force all categories on
  $$('[id^="chaos"]').forEach(cb => { if (cb.type === 'checkbox') cb.checked = true; });

  autoGenerateStyle();

  // Extra chaos
  STATE.textShadowLayers = [];
  for (let i = 0; i < randInt(2, 5); i++) {
    STATE.textShadowLayers.push({ id: Date.now() + i, x: randInt(-20, 20), y: randInt(-20, 20), blur: randInt(0, 40), color: randomHex(), active: true });
  }
  renderTextShadowLayers();

  STATE.styles.textTransform = randPick(['uppercase', 'lowercase', 'capitalize', 'none']);
  STATE.styles.writingMode = Math.random() > 0.85 ? 'vertical-rl' : 'horizontal-tb';
  STATE.styles.mixBlendMode = randPick(['normal', 'screen', 'overlay', 'difference', 'exclusion', 'hard-light']);
  STATE.filterInvert = Math.random() > 0.7 ? randInt(0, 100) : 0;
  STATE.backdropBlur = Math.random() > 0.7 ? randInt(0, 20) : 0;

  syncAllControls();
  applyAndSave();
  showToast('💥 MAKSİMUM KAOS!', 'warning');
}

/* ─────────────────────────────────────────────────────────────────────
   23. GRADIENT BORDER
───────────────────────────────────────────────────────────────────── */
function applyGradientBorder() {
  const colors = STATE.gradientBorderColors.map(c => `${c.color} ${c.stop}%`).join(', ');
  const gradientStr = `linear-gradient(135deg, ${colors})`;
  const width = parseInt(($('gradientBorderWidth') || {}).value || 2);

  const box = $('preview-box');
  if (box) {
    box.style.border = `${width}px solid transparent`;
    box.style.backgroundImage = `${gradientStr}`;
    box.style.backgroundOrigin = 'border-box';
    box.style.backgroundClip = 'padding-box, border-box';
    box.style.webkitBackgroundClip = 'padding-box, border-box';
  }
  showToast('Gradyan çerçeve uygulandı!', 'success');
  applyAndSave();
}

/* ─────────────────────────────────────────────────────────────────────
   24. SYNC UI
───────────────────────────────────────────────────────────────────── */
function syncSelect(id, val) {
  const el = $(id);
  if (el) el.value = val;
}

function updateFontPreview(fontFamily) {
  const preview = $('fontPreviewText');
  if (preview) {
    preview.style.fontFamily = fontFamily;
    preview.textContent = 'Aa';
  }
}

function syncTransformUI() {
  if ($('rotateRange')) $('rotateRange').value = STATE.transformRotate;
  if ($('rotate')) $('rotate').value = STATE.transformRotate;
  if ($('rotateVal')) $('rotateVal').textContent = STATE.transformRotate + '°';
  if ($('scaleRange')) $('scaleRange').value = STATE.transformScaleX;
  if ($('scaleVal')) $('scaleVal').textContent = STATE.transformScaleX.toFixed(2);
  if ($('scaleX')) $('scaleX').value = STATE.transformScaleX.toFixed(2);
  if ($('scaleY')) $('scaleY').value = STATE.transformScaleY.toFixed(2);
  if ($('skewX')) $('skewX').value = STATE.transformSkewX;
  if ($('skewY')) $('skewY').value = STATE.transformSkewY;
  if ($('translateX')) $('translateX').value = STATE.transformTranslateX;
  if ($('translateY')) $('translateY').value = STATE.transformTranslateY;
  if ($('rotateX')) $('rotateX').value = STATE.transformRotateX;
  if ($('rotateY')) $('rotateY').value = STATE.transformRotateY;
  if ($('rotateZ')) $('rotateZ').value = STATE.transformRotateZ;
  if ($('perspective')) $('perspective').value = STATE.transformPerspective;
}

function syncFilterUI() {
  const filterMap = [
    ['filterBlurRange', 'blurVal', STATE.filterBlur, 'px'],
    ['filterBrightnessRange', 'brightnessVal', STATE.filterBrightness, '%'],
    ['filterContrastRange', 'contrastVal', STATE.filterContrast, '%'],
    ['filterSaturateRange', 'saturateVal', STATE.filterSaturate, '%'],
    ['filterHueRotateRange', 'hueRotateVal', STATE.filterHueRotate, '°'],
    ['filterInvertRange', 'invertVal', STATE.filterInvert, '%'],
    ['filterSepiaRange', 'sepiaVal', STATE.filterSepia, '%'],
    ['filterGrayscaleRange', 'grayscaleVal', STATE.filterGrayscale, '%'],
    ['backdropBlurRange', 'backdropBlurVal', STATE.backdropBlur, 'px'],
  ];
  filterMap.forEach(([rangeId, valId, val, unit]) => {
    const range = $(rangeId);
    const label = $(valId);
    if (range) range.value = val;
    if (label) label.textContent = val + unit;
  });
}

function syncAllControls() {
  const s = STATE.styles;

  syncSelect('fontFamily', s.fontFamily);
  updateFontPreview(s.fontFamily);

  if ($('fontSize')) $('fontSize').value = parseInt(s.fontSize) || 30;
  if ($('fontSizeRange')) $('fontSizeRange').value = parseInt(s.fontSize) || 30;
  if ($('fontSizeVal')) $('fontSizeVal').textContent = (parseInt(s.fontSize) || 30) + 'px';

  syncSelect('fontWeight', s.fontWeight);
  if ($('fontWeightRange')) $('fontWeightRange').value = s.fontWeight;
  if ($('fontWeightVal')) $('fontWeightVal').textContent = s.fontWeight;

  syncSelect('fontStyle', s.fontStyle);
  syncSelect('textTransform', s.textTransform);
  syncSelect('textDecorationLine', s.textDecorationLine);
  syncSelect('textDecorationStyle', s.textDecorationStyle);
  syncSelect('writingMode', s.writingMode);
  syncSelect('textOverflow', s.textOverflow);

  if ($('textColorHex')) $('textColorHex').value = s.color;
  if ($('textColorSwatch')) $('textColorSwatch').style.background = s.color;
  if (COLOR_PICKERS.text) try { COLOR_PICKERS.text.color = s.color; } catch (e) {}

  if ($('bgColorHex')) $('bgColorHex').value = s.backgroundColor;
  if ($('bgColorSwatch')) $('bgColorSwatch').style.background = s.backgroundColor;
  if (COLOR_PICKERS.bg) try { COLOR_PICKERS.bg.color = s.backgroundColor; } catch (e) {}

  if ($('lineHeightRange')) $('lineHeightRange').value = s.lineHeight;
  if ($('lineHeightVal')) $('lineHeightVal').textContent = s.lineHeight;

  $$('.align-btn').forEach(b => {
    b.classList.toggle('active', b.dataset.align === s.textAlign);
    b.setAttribute('aria-pressed', b.dataset.align === s.textAlign);
  });

  // Border radius
  ['TopLeft', 'TopRight', 'BottomLeft', 'BottomRight'].forEach(corner => {
    const inp = $(`borderRadius${corner}`);
    if (inp) inp.value = parseInt(s[`border${corner}Radius`]) || 0;
  });

  syncSelect('backgroundSize', s.backgroundSize);
  syncSelect('backgroundRepeat', s.backgroundRepeat);
  syncSelect('backgroundBlendMode', s.backgroundBlendMode);
  syncSelect('display', s.display);
  syncSelect('overflow', s.overflow);
  syncSelect('cursor', s.cursor);
  syncSelect('mixBlendMode', s.mixBlendMode);

  if ($('clipPath')) $('clipPath').value = s.clipPath || 'none';

  // Animation
  $$('.anim-btn').forEach(b => b.classList.toggle('active', b.dataset.anim === s.animationName));
  if ($('animationDurationRange')) $('animationDurationRange').value = parseFloat(s.animationDuration) || 1;
  if ($('animDurationVal')) $('animDurationVal').textContent = s.animationDuration || '1s';
  syncSelect('animationTimingFunction', s.animationTimingFunction);
  syncSelect('animationIterationCount', s.animationIterationCount);
  syncSelect('animationDirection', s.animationDirection);
  syncSelect('animationFillMode', s.animationFillMode);

  syncTransformUI();
  syncFilterUI();
  renderGradientColors();
  renderTextGradientColors();
  renderBoxShadowLayers();
  renderTextShadowLayers();
  updateGradientPreviewBar();
}

/* ─────────────────────────────────────────────────────────────────────
   25. PREVIEW CONTROLS
───────────────────────────────────────────────────────────────────── */
function initPreviewControls() {
  // Size buttons
  $$('.preview-size-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      $$('.preview-size-btn').forEach(b => { b.classList.remove('active'); b.setAttribute('aria-pressed', 'false'); });
      btn.classList.add('active');
      btn.setAttribute('aria-pressed', 'true');
      const size = btn.dataset.previewSize;
      setPreviewSize(size);
    });
  });

  // Preview control buttons
  $$('[data-action]').forEach(btn => {
    btn.addEventListener('click', () => handleAction(btn.dataset.action, btn));
  });

  // Preview dimensions observer
  const frame = $('previewFrame');
  if (frame && window.ResizeObserver) {
    const ro = new ResizeObserver(entries => {
      for (const entry of entries) {
        const { width, height } = entry.contentRect;
        const dim = $('previewDimensions');
        if (dim) dim.textContent = `${Math.round(width)} × ${Math.round(height)}`;
      }
    });
    ro.observe(frame);
  }
}

function setPreviewSize(size) {
  STATE.previewSize = size;
  const frame = $('previewFrame');
  if (!frame) return;
  frame.dataset.size = size;

  // Apply size constraints
  const sizes = { mobile: '375px', tablet: '768px', desktop: '100%' };
  frame.style.maxWidth = sizes[size] || '100%';
  frame.style.margin = '0 auto';
}

function handleAction(action, btn) {
  switch (action) {
    case 'undo': undo(); break;
    case 'redo': redo(); break;
    case 'toggle-theme': toggleAppTheme(); break;
    case 'show-shortcuts': openModal('shortcutModalOverlay'); break;
    case 'fullscreen-preview': openFullscreenPreview(); break;
    case 'reset-all': resetAll(); break;
    case 'command-palette': openCommandPalette(); break;
    case 'download-css': downloadCSS(); break;
    case 'download-html': downloadHTML(); break;
    case 'download-json': downloadJSON(); break;
    case 'export-styles': exportStyles(); break;
    case 'import-styles': $('import-styles').click(); break;
    case 'format-css': formatCSS(); break;
    case 'minify-css': minifyCSS(); break;
    case 'toggle-ruler': toggleRuler(btn); break;
    case 'toggle-grid': toggleGrid(btn); break;
    case 'toggle-preview-bg': togglePreviewBg(); break;
    case 'randomize-text': randomizeText(); break;
    case 'clear-text': clearPreviewText(); break;
  }
}

function toggleRuler(btn) {
  STATE.rulerVisible = !STATE.rulerVisible;
  if (btn) { btn.classList.toggle('active', STATE.rulerVisible); btn.setAttribute('aria-pressed', STATE.rulerVisible); }
  const rulerH = $('rulerH');
  const rulerV = $('rulerV');
  if (rulerH) rulerH.style.display = STATE.rulerVisible ? 'block' : 'none';
  if (rulerV) rulerV.style.display = STATE.rulerVisible ? 'block' : 'none';
  if (STATE.rulerVisible) renderRulers();
}

function renderRulers() {
  const rulerH = $('rulerH');
  const rulerV = $('rulerV');
  const container = $('previewContainer');
  if (!rulerH || !rulerV || !container) return;

  const width = container.offsetWidth;
  const height = container.offsetHeight;

  // Horizontal ruler
  rulerH.innerHTML = '';
  for (let i = 0; i <= width; i += 50) {
    const mark = document.createElement('div');
    mark.className = 'ruler-mark';
    mark.style.left = i + 'px';
    mark.textContent = i;
    rulerH.appendChild(mark);
  }

  // Vertical ruler
  rulerV.innerHTML = '';
  for (let i = 0; i <= height; i += 50) {
    const mark = document.createElement('div');
    mark.className = 'ruler-mark';
    mark.style.top = i + 'px';
    mark.textContent = i;
    rulerV.appendChild(mark);
  }
}

function toggleGrid(btn) {
  STATE.gridVisible = !STATE.gridVisible;
  if (btn) { btn.classList.toggle('active', STATE.gridVisible); btn.setAttribute('aria-pressed', STATE.gridVisible); }
  const container = $('previewContainer');
  if (container) container.classList.toggle('grid-overlay', STATE.gridVisible);
}

function togglePreviewBg() {
  STATE.previewBgDark = !STATE.previewBgDark;
  const container = $('previewContainer');
  if (container) container.classList.toggle('preview-bg-light', !STATE.previewBgDark);
}

function randomizeText() {
  const text = randPick(RANDOM_TEXTS);
  const customText = $('customText');
  if (customText) {
    customText.value = text;
    STATE.previewText = text;
    const box = $('preview-box');
    if (box) box.textContent = text;
    const charCount = $('charCount');
    if (charCount) charCount.textContent = `${text.length}/200`;
  }
}

function clearPreviewText() {
  const customText = $('customText');
  if (customText) {
    customText.value = '';
    STATE.previewText = '';
    const box = $('preview-box');
    if (box) box.textContent = '';
    const charCount = $('charCount');
    if (charCount) charCount.textContent = '0/200';
  }
}

/* ─────────────────────────────────────────────────────────────────────
   26. MODALS
───────────────────────────────────────────────────────────────────── */
function openModal(overlayId) {
  const overlay = $(overlayId);
  if (overlay) { overlay.classList.add('active'); overlay.style.display = 'flex'; }
}

function closeModal(overlayId) {
  const overlay = $(overlayId);
  if (overlay) { overlay.classList.remove('active'); overlay.style.display = ''; }
}

function initModals() {
  // Close on overlay click
  $$('.modal-overlay').forEach(overlay => {
    overlay.addEventListener('click', (e) => {
      if (e.target === overlay) closeModal(overlay.id);
    });
  });

  // Close buttons
  const shortcutClose = $('shortcutModalClose');
  if (shortcutClose) shortcutClose.addEventListener('click', () => closeModal('shortcutModalOverlay'));

  const bezierClose = $('bezierModalClose');
  if (bezierClose) bezierClose.addEventListener('click', () => closeModal('bezierModalOverlay'));

  const fsClose = $('fullscreenClose');
  if (fsClose) fsClose.addEventListener('click', () => closeModal('fullscreenPreviewOverlay'));

  // Bezier Editor
  initBezierEditor();

  // Import styles
  const importInput = $('import-styles');
  if (importInput) {
    importInput.addEventListener('change', (e) => {
      const file = e.target.files[0];
      if (!file) return;
      const reader = new FileReader();
      reader.onload = (ev) => {
        try {
          const data = JSON.parse(ev.target.result);
          if (data.styles) {
            Object.assign(STATE.styles, data.styles);
            if (data.boxShadowLayers) STATE.boxShadowLayers = data.boxShadowLayers;
            if (data.textShadowLayers) STATE.textShadowLayers = data.textShadowLayers;
            if (data.gradientColors) STATE.gradientColors = data.gradientColors;
            syncAllControls();
            applyAndSave();
            showToast('Stiller içe aktarıldı!', 'success');
          }
        } catch (err) {
          showToast('Geçersiz dosya formatı', 'error');
        }
      };
      reader.readAsText(file);
      importInput.value = '';
    });
  }
}

function openFullscreenPreview() {
  const overlay = $('fullscreenPreviewOverlay');
  const fsBox = $('fullscreenPreviewBox');
  const previewBox = $('preview-box');
  if (overlay && fsBox && previewBox) {
    fsBox.innerHTML = '';
    const clone = previewBox.cloneNode(true);
    clone.style.width = 'auto';
    clone.style.minWidth = '400px';
    clone.style.minHeight = '200px';
    clone.style.padding = '40px 60px';
    fsBox.appendChild(clone);
    openModal('fullscreenPreviewOverlay');
  }
}

/* ─────────────────────────────────────────────────────────────────────
   27. BEZIER EDITOR
───────────────────────────────────────────────────────────────────── */
function openBezierEditor() {
  openModal('bezierModalOverlay');
  drawBezierCurve();
}

function initBezierEditor() {
  const inputs = ['bezierP1x', 'bezierP1y', 'bezierP2x', 'bezierP2y'];
  inputs.forEach(id => {
    const inp = $(id);
    if (inp) inp.addEventListener('input', () => {
      updateBezierOutput();
      drawBezierCurve();
    });
  });

  // Presets
  $$('.bezier-preset-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      const vals = btn.dataset.bezier.split(',').map(Number);
      if ($('bezierP1x')) $('bezierP1x').value = vals[0];
      if ($('bezierP1y')) $('bezierP1y').value = vals[1];
      if ($('bezierP2x')) $('bezierP2x').value = vals[2];
      if ($('bezierP2y')) $('bezierP2y').value = vals[3];
      updateBezierOutput();
      drawBezierCurve();
    });
  });

  // Apply
  const applyBtn = $('applyBezierBtn');
  if (applyBtn) {
    applyBtn.addEventListener('click', () => {
      const p1x = parseFloat($('bezierP1x').value);
      const p1y = parseFloat($('bezierP1y').value);
      const p2x = parseFloat($('bezierP2x').value);
      const p2y = parseFloat($('bezierP2y').value);
      const bezierStr = `cubic-bezier(${p1x}, ${p1y}, ${p2x}, ${p2y})`;
      STATE.styles.animationTimingFunction = bezierStr;
      syncSelect('animationTimingFunction', bezierStr);
      closeModal('bezierModalOverlay');
      applyAndSave();
      showToast('Bezier uygulandı!', 'success');
    });
  }
}

function updateBezierOutput() {
  const p1x = parseFloat(($('bezierP1x') || {}).value || 0.25);
  const p1y = parseFloat(($('bezierP1y') || {}).value || 0.46);
  const p2x = parseFloat(($('bezierP2x') || {}).value || 0.45);
  const p2y = parseFloat(($('bezierP2y') || {}).value || 0.94);
  const out = $('bezierOutput');
  if (out) out.textContent = `cubic-bezier(${p1x}, ${p1y}, ${p2x}, ${p2y})`;
}

function drawBezierCurve() {
  const canvas = $('bezierCanvas');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');
  const w = canvas.width, h = canvas.height;
  const pad = 30;

  const p1x = parseFloat(($('bezierP1x') || {}).value || 0.25);
  const p1y = parseFloat(($('bezierP1y') || {}).value || 0.46);
  const p2x = parseFloat(($('bezierP2x') || {}).value || 0.45);
  const p2y = parseFloat(($('bezierP2y') || {}).value || 0.94);

  ctx.clearRect(0, 0, w, h);

  // Background
  ctx.fillStyle = 'rgba(255,255,255,0.03)';
  ctx.fillRect(0, 0, w, h);

  // Grid
  ctx.strokeStyle = 'rgba(255,255,255,0.08)';
  ctx.lineWidth = 1;
  for (let i = 0; i <= 4; i++) {
    const x = pad + (w - pad * 2) * i / 4;
    const y = pad + (h - pad * 2) * i / 4;
    ctx.beginPath(); ctx.moveTo(x, pad); ctx.lineTo(x, h - pad); ctx.stroke();
    ctx.beginPath(); ctx.moveTo(pad, y); ctx.lineTo(w - pad, y); ctx.stroke();
  }

  const toX = (t) => pad + t * (w - pad * 2);
  const toY = (t) => (h - pad) - t * (h - pad * 2);

  // Control lines
  ctx.strokeStyle = 'rgba(99, 102, 241, 0.4)';
  ctx.lineWidth = 1;
  ctx.setLineDash([4, 4]);
  ctx.beginPath(); ctx.moveTo(toX(0), toY(0)); ctx.lineTo(toX(p1x), toY(p1y)); ctx.stroke();
  ctx.beginPath(); ctx.moveTo(toX(1), toY(1)); ctx.lineTo(toX(p2x), toY(p2y)); ctx.stroke();
  ctx.setLineDash([]);

  // Curve
  ctx.strokeStyle = '#818cf8';
  ctx.lineWidth = 2.5;
  ctx.beginPath();
  ctx.moveTo(toX(0), toY(0));
  ctx.bezierCurveTo(toX(p1x), toY(p1y), toX(p2x), toY(p2y), toX(1), toY(1));
  ctx.stroke();

  // Control points
  const drawPoint = (x, y, color) => {
    ctx.fillStyle = color;
    ctx.strokeStyle = '#fff';
    ctx.lineWidth = 2;
    ctx.beginPath();
    ctx.arc(toX(x), toY(y), 7, 0, Math.PI * 2);
    ctx.fill();
    ctx.stroke();
  };
  drawPoint(p1x, p1y, '#f472b6');
  drawPoint(p2x, p2y, '#34d399');

  // Endpoints
  ctx.fillStyle = '#fff';
  ctx.beginPath(); ctx.arc(toX(0), toY(0), 5, 0, Math.PI * 2); ctx.fill();
  ctx.beginPath(); ctx.arc(toX(1), toY(1), 5, 0, Math.PI * 2); ctx.fill();
}

/* ─────────────────────────────────────────────────────────────────────
   28. COMMAND PALETTE
───────────────────────────────────────────────────────────────────── */
const COMMANDS = [
  { name: 'Neon Teması', desc: 'Neon glow efekti', icon: 'lightbulb', action: () => applyTheme('auto-theme-neon') },
  { name: 'Cyberpunk Teması', desc: 'Cyberpunk stili', icon: 'robot', action: () => applyTheme('auto-theme-cyberpunk') },
  { name: 'Matrix Teması', desc: 'Matrix efekti', icon: 'terminal', action: () => applyTheme('auto-theme-matrix') },
  { name: 'Glassmorphism', desc: 'Cam efekti', icon: 'glass-whiskey', action: () => applyTheme('auto-theme-glassmorphism') },
  { name: 'Retrowave', desc: 'Retrowave stili', icon: 'wave-square', action: () => applyTheme('auto-theme-retrowave') },
  { name: 'Otomatik Stil', desc: 'Rastgele stil oluştur', icon: 'wand-magic-sparkles', action: () => autoGenerateStyle() },
  { name: 'Maksimum Kaos', desc: 'Tüm kaos parametreleri', icon: 'explosion', action: () => maxChaos() },
  { name: 'Tümünü Sıfırla', desc: 'Başlangıç değerleri', icon: 'trash-restore', action: () => resetAll() },
  { name: 'Geri Al', desc: 'Son değişikliği geri al', icon: 'undo-alt', action: () => undo() },
  { name: 'İleri Al', desc: 'Geri alınan değişikliği ileri al', icon: 'redo-alt', action: () => redo() },
  { name: 'CSS Kopyala', desc: 'CSS kodunu kopyala', icon: 'copy', action: () => copyCSS() },
  { name: 'CSS İndir', desc: 'CSS dosyasını indir', icon: 'download', action: () => downloadCSS() },
  { name: 'Rastgele Font', desc: 'Rastgele yazı tipi', icon: 'font', action: () => handleStyleTarget('random-font') },
  { name: 'Rastgele Renk', desc: 'Rastgele metin rengi', icon: 'palette', action: () => handleStyleTarget('random-color') },
  { name: 'Rastgele Gradyan', desc: 'Rastgele arka plan gradyanı', icon: 'grip-lines', action: () => handleStyleTarget('random-gradient') },
  { name: 'Rastgele Animasyon', desc: 'Rastgele animasyon uygula', icon: 'play', action: () => handleStyleTarget('random-animation') },
  { name: 'Neon Glow', desc: 'Neon ışıma efekti', icon: 'lightbulb', action: () => handleStyleTarget('random-neon-glow') },
  { name: 'Tam Ekran Önizleme', desc: 'Tam ekran mod', icon: 'expand', action: () => openFullscreenPreview() },
  { name: 'Mobil Görünüm', desc: '375px genişlik', icon: 'mobile-screen', action: () => setPreviewSize('mobile') },
  { name: 'Tablet Görünüm', desc: '768px genişlik', icon: 'tablet-screen-button', action: () => setPreviewSize('tablet') },
  { name: 'Masaüstü Görünüm', desc: 'Tam genişlik', icon: 'desktop', action: () => setPreviewSize('desktop') },
  { name: 'Vintage Filtre', desc: 'Retro fotoğraf efekti', icon: 'camera-retro', action: () => { handleStyleTarget('filter-vintage'); applyAndSave(); } },
  { name: 'Palet Oluştur', desc: 'Renk paleti oluştur', icon: 'swatchbook', action: () => generatePalette() },
];

let cpSelectedIndex = -1;

function openCommandPalette() {
  openModal('commandPaletteOverlay');
  const input = $('commandPaletteInput');
  if (input) { input.value = ''; input.focus(); }
  renderCommandResults('');
  cpSelectedIndex = -1;
}

function closeCommandPalette() {
  closeModal('commandPaletteOverlay');
}

function renderCommandResults(query) {
  const results = $('commandPaletteResults');
  if (!results) return;
  results.innerHTML = '';

  const filtered = query
    ? COMMANDS.filter(c => c.name.toLowerCase().includes(query.toLowerCase()) || (c.desc && c.desc.toLowerCase().includes(query.toLowerCase())))
    : COMMANDS;

  filtered.forEach((cmd, i) => {
    const item = document.createElement('div');
    item.className = `cp-result-item${i === cpSelectedIndex ? ' selected' : ''}`;
    item.innerHTML = `<i class="fas fa-${cmd.icon}"></i><div><div class="cp-name">${cmd.name}</div><div class="cp-desc">${cmd.desc || ''}</div></div>`;
    item.addEventListener('click', () => {
      cmd.action();
      closeCommandPalette();
    });
    item.addEventListener('mouseenter', () => {
      cpSelectedIndex = i;
      results.querySelectorAll('.cp-result-item').forEach((el, j) => el.classList.toggle('selected', j === i));
    });
    results.appendChild(item);
  });
}

function initCommandPalette() {
  const overlay = $('commandPaletteOverlay');
  if (overlay) overlay.addEventListener('click', (e) => { if (e.target === overlay) closeCommandPalette(); });

  const input = $('commandPaletteInput');
  if (input) {
    input.addEventListener('input', () => {
      cpSelectedIndex = -1;
      renderCommandResults(input.value);
    });
    input.addEventListener('keydown', (e) => {
      const results = $('commandPaletteResults');
      const items = results ? results.querySelectorAll('.cp-result-item') : [];
      if (e.key === 'ArrowDown') {
        e.preventDefault();
        cpSelectedIndex = Math.min(cpSelectedIndex + 1, items.length - 1);
        items.forEach((el, i) => el.classList.toggle('selected', i === cpSelectedIndex));
        if (items[cpSelectedIndex]) items[cpSelectedIndex].scrollIntoView({ block: 'nearest' });
      } else if (e.key === 'ArrowUp') {
        e.preventDefault();
        cpSelectedIndex = Math.max(cpSelectedIndex - 1, 0);
        items.forEach((el, i) => el.classList.toggle('selected', i === cpSelectedIndex));
        if (items[cpSelectedIndex]) items[cpSelectedIndex].scrollIntoView({ block: 'nearest' });
      } else if (e.key === 'Enter') {
        const filtered = input.value
          ? COMMANDS.filter(c => c.name.toLowerCase().includes(input.value.toLowerCase()))
          : COMMANDS;
        const cmd = filtered[cpSelectedIndex] || filtered[0];
        if (cmd) { cmd.action(); closeCommandPalette(); }
      } else if (e.key === 'Escape') {
        closeCommandPalette();
      }
    });
  }
}

/* ─────────────────────────────────────────────────────────────────────
   29. KEYBOARD SHORTCUTS
───────────────────────────────────────────────────────────────────── */
function initKeyboardShortcuts() {
  document.addEventListener('keydown', (e) => {
    const active = document.activeElement;
    const isInput = active && (active.tagName === 'INPUT' || active.tagName === 'TEXTAREA' || active.tagName === 'SELECT');

    // Space: pause/play animation
    if (e.key === ' ' && !isInput) {
      e.preventDefault();
      const playing = STATE.styles.animationPlayState === 'running';
      STATE.styles.animationPlayState = playing ? 'paused' : 'running';
      applyStyles();
      return;
    }

    // ? show shortcuts
    if (e.key === '?' && !isInput) {
      openModal('shortcutModalOverlay');
      return;
    }

    if (!e.ctrlKey && !e.metaKey) return;

    switch (e.key) {
      case 'z': case 'Z':
        if (!e.shiftKey) { e.preventDefault(); undo(); }
        break;
      case 'y': case 'Y':
        e.preventDefault(); redo();
        break;
      case 's': case 'S':
        e.preventDefault(); copyCSS();
        break;
      case 'k': case 'K':
        e.preventDefault(); openCommandPalette();
        break;
      case 'd': case 'D':
        e.preventDefault(); downloadCSS();
        break;
      case 'r': case 'R':
        if (e.shiftKey) { e.preventDefault(); resetAll(); }
        else if (!isInput) { e.preventDefault(); handleStyleTarget('random-color'); }
        break;
      case 't': case 'T':
        e.preventDefault(); toggleAppTheme();
        break;
      case 'g': case 'G':
        e.preventDefault();
        if (e.shiftKey) maxChaos();
        else autoGenerateStyle();
        break;
      case 'f': case 'F':
        if (!isInput) { e.preventDefault(); handleStyleTarget('random-font'); }
        break;
      case 'p': case 'P':
        e.preventDefault(); openFullscreenPreview();
        break;
      case '1':
        e.preventDefault(); setPreviewSize('mobile'); updateSizeBtns('mobile');
        break;
      case '2':
        e.preventDefault(); setPreviewSize('tablet'); updateSizeBtns('tablet');
        break;
      case '3':
        e.preventDefault(); setPreviewSize('desktop'); updateSizeBtns('desktop');
        break;
    }

    // ESC
    if (e.key === 'Escape') {
      closeCommandPalette();
      closeModal('shortcutModalOverlay');
      closeModal('bezierModalOverlay');
      closeModal('fullscreenPreviewOverlay');
    }
  });

  document.addEventListener('keyup', (e) => {
    if (e.key === 'Escape') {
      closeCommandPalette();
    }
  });
}

function updateSizeBtns(size) {
  $$('.preview-size-btn').forEach(b => {
    b.classList.toggle('active', b.dataset.previewSize === size);
    b.setAttribute('aria-pressed', b.dataset.previewSize === size);
  });
}

/* ─────────────────────────────────────────────────────────────────────
   30. COPY / DOWNLOAD / EXPORT
───────────────────────────────────────────────────────────────────── */
async function copyToClipboard(text) {
  try {
    await navigator.clipboard.writeText(text);
    return true;
  } catch (e) {
    const ta = document.createElement('textarea');
    ta.value = text;
    ta.style.position = 'fixed';
    ta.style.opacity = '0';
    document.body.appendChild(ta);
    ta.select();
    const success = document.execCommand('copy');
    document.body.removeChild(ta);
    return success;
  }
}

async function copyCSS() {
  const cssOutput = $('css-output');
  if (!cssOutput) return;
  const success = await copyToClipboard(cssOutput.value);
  const successEl = $('copy-success');
  const errorEl = $('copy-error');
  if (success) {
    if (successEl) { successEl.style.display = 'flex'; setTimeout(() => successEl.style.display = '', 2000); }
    showToast('CSS kopyalandı! 📋', 'success');
  } else {
    if (errorEl) { errorEl.style.display = 'flex'; setTimeout(() => errorEl.style.display = '', 2000); }
    showToast('Kopyalama başarısız', 'error');
  }
}

function downloadFile(filename, content, type = 'text/plain') {
  const blob = new Blob([content], { type });
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = filename;
  document.body.appendChild(a);
  a.click();
  document.body.removeChild(a);
  URL.revokeObjectURL(url);
}

function downloadCSS() {
  const cssOutput = $('css-output');
  if (cssOutput) {
    downloadFile('styles.css', cssOutput.value, 'text/css');
    showToast('CSS indirildi!', 'success');
  }
}

function downloadHTML() {
  const text = STATE.previewText || 'K3N4N V7.0';
  const cssOutput = $('css-output');
  const css = cssOutput ? cssOutput.value : '';
  const html = `<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>K3N4N CSS Preview</title>
  <style>
    body { margin: 0; display: flex; justify-content: center; align-items: center; min-height: 100vh; background: #111; }
${css}
  </style>
</head>
<body>
  <div class="my-element">${escapeHtml(text)}</div>
</body>
</html>`;
  downloadFile('preview.html', html, 'text/html');
  showToast('HTML indirildi!', 'success');
}

function downloadJSON() {
  const jsonOutput = $('json-output');
  if (jsonOutput) {
    downloadFile('styles.json', jsonOutput.value, 'application/json');
    showToast('JSON indirildi!', 'success');
  }
}

function exportStyles() {
  const data = {
    styles: STATE.styles,
    boxShadowLayers: STATE.boxShadowLayers,
    textShadowLayers: STATE.textShadowLayers,
    gradientColors: STATE.gradientColors,
    textGradientColors: STATE.textGradientColors,
    textGradientActive: STATE.textGradientActive,
    textStrokeWidth: STATE.textStrokeWidth,
    textStrokeColor: STATE.textStrokeColor,
    filters: {
      blur: STATE.filterBlur, brightness: STATE.filterBrightness,
      contrast: STATE.filterContrast, saturate: STATE.filterSaturate,
      hueRotate: STATE.filterHueRotate, invert: STATE.filterInvert,
      sepia: STATE.filterSepia, grayscale: STATE.filterGrayscale,
    },
    version: '7.0',
    exported: new Date().toISOString(),
  };
  downloadFile('k3n4n-styles.json', JSON.stringify(data, null, 2), 'application/json');
  showToast('Stiller dışa aktarıldı!', 'success');
}

function formatCSS() {
  const output = $('css-output');
  if (!output) return;
  const lines = output.value.split('\n');
  const formatted = lines.map(l => l.trim() ? l : '').filter(Boolean).join('\n');
  output.value = formatted;
  showToast('CSS formatlandı', 'info');
}

function minifyCSS() {
  const output = $('css-output');
  if (!output) return;
  const minified = output.value
    .replace(/\/\*[\s\S]*?\*\//g, '')
    .replace(/\s+/g, ' ')
    .replace(/\s*{\s*/g, '{')
    .replace(/\s*}\s*/g, '}')
    .replace(/\s*:\s*/g, ':')
    .replace(/\s*;\s*/g, ';')
    .trim();
  output.value = minified;
  showToast('CSS minify edildi', 'info');
}

/* ─────────────────────────────────────────────────────────────────────
   31. COPY BUTTONS
───────────────────────────────────────────────────────────────────── */
function initCopyButtons() {
  const copyCssBtn = $('copy-css-btn');
  if (copyCssBtn) copyCssBtn.addEventListener('click', copyCSS);

  const copyHtmlBtn = $('copy-html-btn');
  if (copyHtmlBtn) {
    copyHtmlBtn.addEventListener('click', async () => {
      const area = $('htmlPreviewArea');
      if (area) {
        const text = area.textContent || area.innerText;
        await copyToClipboard(text);
        showToast('HTML kopyalandı!', 'success');
      }
    });
  }

  const copyJsonBtn = $('copy-json-btn');
  if (copyJsonBtn) {
    copyJsonBtn.addEventListener('click', async () => {
      const out = $('json-output');
      if (out) {
        await copyToClipboard(out.value);
        showToast('JSON kopyalandı!', 'success');
      }
    });
  }

  const copyTailwindBtn = $('copy-tailwind-btn');
  if (copyTailwindBtn) {
    copyTailwindBtn.addEventListener('click', async () => {
      const out = $('tailwindOutput');
      if (out) {
        await copyToClipboard(out.textContent || out.innerText);
        showToast('Tailwind sınıfları kopyalandı!', 'success');
      }
    });
  }
}

/* ─────────────────────────────────────────────────────────────────────
   32. CUSTOM CSS EDITOR
───────────────────────────────────────────────────────────────────── */
function initCustomCssEditor() {
  const applyBtn = $('applyCustomCss');
  const clearBtn = $('clearCustomCss');
  const parseBtn = $('parseAndApply');
  const textarea = $('cssInputArea');
  const successMsg = $('css-success');
  const errorMsg = $('css-error');

  if (applyBtn) {
    applyBtn.addEventListener('click', () => {
      if (!textarea) return;
      const css = textarea.value.trim();
      if (!css) return;

      const box = $('preview-box');
      if (box) {
        try {
          // Apply raw CSS string
          const lines = css.split(';').map(l => l.trim()).filter(Boolean);
          lines.forEach(line => {
            const colonIdx = line.indexOf(':');
            if (colonIdx > 0) {
              const prop = line.substring(0, colonIdx).trim();
              const val = line.substring(colonIdx + 1).trim();
              // Convert kebab-case to camelCase
              const camel = prop.replace(/-([a-z])/g, (g) => g[1].toUpperCase());
              try { box.style[camel] = val; } catch (e) {}
            }
          });
          if (successMsg) { successMsg.style.display = 'flex'; setTimeout(() => successMsg.style.display = '', 2500); }
          showToast('Özel CSS uygulandı!', 'success');
        } catch (err) {
          if (errorMsg) { errorMsg.style.display = 'flex'; setTimeout(() => errorMsg.style.display = '', 2500); }
          showToast('CSS sözdizimi hatası', 'error');
        }
      }
    });
  }

  if (clearBtn) {
    clearBtn.addEventListener('click', () => {
      if (textarea) textarea.value = '';
    });
  }

  if (parseBtn) {
    parseBtn.addEventListener('click', () => {
      if (!textarea) return;
      const css = textarea.value.trim();
      if (!css) return;

      // Parse and map to STATE
      const lines = css.split(';').map(l => l.trim()).filter(Boolean);
      let changed = false;

      lines.forEach(line => {
        const colonIdx = line.indexOf(':');
        if (colonIdx < 0) return;
        const prop = line.substring(0, colonIdx).trim();
        const val = line.substring(colonIdx + 1).trim();
        const camel = prop.replace(/-([a-z])/g, (g) => g[1].toUpperCase());

        if (camel in STATE.styles) {
          STATE.styles[camel] = val;
          changed = true;
        }

        // Special mappings
        if (prop === 'font-size') {
          STATE.styles.fontSize = val;
          const num = parseInt(val);
          if ($('fontSize')) $('fontSize').value = num;
          if ($('fontSizeRange')) $('fontSizeRange').value = num;
          if ($('fontSizeVal')) $('fontSizeVal').textContent = val;
          changed = true;
        }
        if (prop === 'color') {
          STATE.styles.color = val;
          if ($('textColorHex')) $('textColorHex').value = val;
          changed = true;
        }
        if (prop === 'background-color') {
          STATE.styles.backgroundColor = val;
          changed = true;
        }
        if (prop === 'animation-name') {
          STATE.styles.animationName = val;
          changed = true;
        }
      });

      if (changed) {
        syncAllControls();
        applyAndSave();
        if (successMsg) { successMsg.style.display = 'flex'; setTimeout(() => successMsg.style.display = '', 2500); }
        showToast('CSS ayrıştırıldı ve uygulandı!', 'success');
      }
    });
  }
}

/* ─────────────────────────────────────────────────────────────────────
   33. PSEUDO ELEMENT EDITOR
───────────────────────────────────────────────────────────────────── */
function initPseudoEditor() {
  const applyBtn = $('applyPseudoBtn');
  if (applyBtn) {
    applyBtn.addEventListener('click', () => {
      const beforeContent = ($('beforeContent') || {}).value || '';
      const beforeTop = ($('beforeTop') || {}).value || 'auto';
      const beforeLeft = ($('beforeLeft') || {}).value || 'auto';
      const beforeColor = ($('beforeColor') || {}).value || '#ffffff';
      const beforeFontSize = ($('beforeFontSize') || {}).value || '1em';

      const afterContent = ($('afterContent') || {}).value || '';
      const afterTop = ($('afterTop') || {}).value || 'auto';
      const afterRight = ($('afterRight') || {}).value || 'auto';
      const afterColor = ($('afterColor') || {}).value || '#ffffff';
      const afterFontSize = ($('afterFontSize') || {}).value || '1em';

      // Inject pseudo element CSS
      const styleId = 'pseudo-element-styles';
      let styleEl = document.getElementById(styleId);
      if (!styleEl) {
        styleEl = document.createElement('style');
        styleEl.id = styleId;
        document.head.appendChild(styleEl);
      }

      styleEl.textContent = `
        #preview-box { position: relative; }
        #preview-box::before {
          content: '${beforeContent.replace(/'/g, "\\'")}';
          position: absolute;
          top: ${beforeTop};
          left: ${beforeLeft};
          color: ${beforeColor};
          font-size: ${beforeFontSize};
        }
        #preview-box::after {
          content: '${afterContent.replace(/'/g, "\\'")}';
          position: absolute;
          top: ${afterTop};
          right: ${afterRight};
          color: ${afterColor};
          font-size: ${afterFontSize};
        }
      `;

      showToast('Pseudo element uygulandı!', 'success');
      updateCssOutput();
    });
  }
}

/* ─────────────────────────────────────────────────────────────────────
   34. AUTO PLAY CHAOS
───────────────────────────────────────────────────────────────────── */
function initAutoPlayChaos() {
  const startBtn = $('startAutoPlay');
  const stopBtn = $('stopAutoPlay');
  const intervalInput = $('autoPlayInterval');

  if (startBtn) {
    startBtn.addEventListener('click', () => {
      if (STATE.autoPlayTimer) return;
      const interval = parseInt((intervalInput || {}).value || 3) * 1000;
      startBtn.disabled = true;
      if (stopBtn) stopBtn.disabled = false;
      showToast('Otomatik kaos başladı! 🎲', 'info');
      STATE.autoPlayTimer = setInterval(() => {
        autoGenerateStyle();
      }, interval);
    });
  }

  if (stopBtn) {
    stopBtn.addEventListener('click', () => {
      if (STATE.autoPlayTimer) {
        clearInterval(STATE.autoPlayTimer);
        STATE.autoPlayTimer = null;
      }
      if (startBtn) startBtn.disabled = false;
      stopBtn.disabled = true;
      showToast('Otomatik kaos durduruldu', 'info');
    });
  }

  if (intervalInput) {
    intervalInput.addEventListener('change', () => {
      STATE.autoPlayInterval = parseInt(intervalInput.value);
    });
  }

  // Chaos category selectors
  const selectAll = $('selectAllChaos');
  const deselectAll = $('deselectAllChaos');
  if (selectAll) selectAll.addEventListener('click', () => {
    $$('[id^="chaos"]').forEach(cb => { if (cb.type === 'checkbox') cb.checked = true; });
  });
  if (deselectAll) deselectAll.addEventListener('click', () => {
    $$('[id^="chaos"]').forEach(cb => { if (cb.type === 'checkbox') cb.checked = false; });
  });
}

/* ─────────────────────────────────────────────────────────────────────
   35. THEME TOGGLE
───────────────────────────────────────────────────────────────────── */
function toggleAppTheme() {
  STATE.appTheme = STATE.appTheme === 'dark' ? 'light' : 'dark';
  document.documentElement.setAttribute('data-theme', STATE.appTheme);
  const btn = document.querySelector('[data-action="toggle-theme"]');
  if (btn) {
    const icon = btn.querySelector('i');
    if (icon) {
      icon.className = STATE.appTheme === 'dark' ? 'fas fa-moon' : 'fas fa-sun';
    }
  }
  showToast(STATE.appTheme === 'dark' ? 'Karanlık mod 🌙' : 'Aydınlık mod ☀️', 'info', 1500);
}

/* ─────────────────────────────────────────────────────────────────────
   36. RESET ALL
───────────────────────────────────────────────────────────────────── */
function resetAll() {
  if (!confirm('Tüm ayarlar sıfırlanacak. Emin misiniz?')) return;

  STATE.styles = {
    fontFamily: "'Poppins', sans-serif",
    fontSize: '30px',
    fontWeight: '400',
    fontStyle: 'normal',
    color: '#ffffff',
    textAlign: 'center',
    lineHeight: '1.5',
    letterSpacing: '0px',
    wordSpacing: '0px',
    textTransform: 'none',
    textDecorationLine: 'none',
    textDecorationStyle: 'solid',
    textDecorationColor: '#ffffff',
    textOverflow: 'clip',
    writingMode: 'horizontal-tb',
    opacity: '1',
    padding: '0px',
    backgroundColor: '#111111',
    backgroundImage: 'none',
    backgroundSize: 'auto',
    backgroundPosition: 'center center',
    backgroundRepeat: 'no-repeat',
    backgroundBlendMode: 'normal',
    border: 'none',
    borderTop: 'none', borderRight: 'none', borderBottom: 'none', borderLeft: 'none',
    borderTopLeftRadius: '10px', borderTopRightRadius: '10px',
    borderBottomLeftRadius: '10px', borderBottomRightRadius: '10px',
    outline: 'none',
    outlineOffset: '0px',
    transform: 'none',
    transformOrigin: 'center center',
    boxShadow: 'none',
    animationName: 'none',
    animationDuration: '1s',
    animationDelay: '0s',
    animationTimingFunction: 'ease',
    animationIterationCount: '1',
    animationDirection: 'normal',
    animationFillMode: 'none',
    animationPlayState: 'running',
    transition: 'all 0.3s ease',
    filter: 'none',
    backdropFilter: 'none',
    display: 'flex',
    justifyContent: 'center',
    alignItems: 'center',
    overflow: 'hidden',
    width: '100%',
    height: '200px',
    cursor: 'auto',
    mixBlendMode: 'normal',
    clipPath: 'none',
  };

  STATE.boxShadowLayers = [];
  STATE.textShadowLayers = [];
  STATE.textGradientActive = false;
  STATE.textStrokeWidth = 0;
  STATE.textStrokeColor = '#ffffff';
  STATE.filterBlur = 0; STATE.filterBrightness = 100; STATE.filterContrast = 100;
  STATE.filterSaturate = 100; STATE.filterHueRotate = 0; STATE.filterInvert = 0;
  STATE.filterSepia = 0; STATE.filterGrayscale = 0; STATE.backdropBlur = 0;
  STATE.dropShadowX = 0; STATE.dropShadowY = 0; STATE.dropShadowBlur = 0;
  STATE.transformRotate = 0; STATE.transformScaleX = 1; STATE.transformScaleY = 1;
  STATE.transformSkewX = 0; STATE.transformSkewY = 0;
  STATE.transformTranslateX = 0; STATE.transformTranslateY = 0;
  STATE.transformRotateX = 0; STATE.transformRotateY = 0;
  STATE.transformRotateZ = 0; STATE.transformPerspective = 0;
  STATE.gradientColors = [{ color: '#667eea', stop: 0 }, { color: '#764ba2', stop: 100 }];
  STATE.textGradientColors = [{ color: '#ff6b9d', stop: 0 }, { color: '#c44dff', stop: 50 }, { color: '#4df0ff', stop: 100 }];
  STATE.activeBgTab = 'bg-solid';

  // Remove pseudo styles
  const pseudoStyle = document.getElementById('pseudo-element-styles');
  if (pseudoStyle) pseudoStyle.remove();

  syncAllControls();
  applyAndSave();
  showToast('Tüm ayarlar sıfırlandı ↺', 'info');
}

/* ─────────────────────────────────────────────────────────────────────
   37. SIDEBAR MOBILE TOGGLE
───────────────────────────────────────────────────────────────────── */
function initSidebarToggle() {
  const toggleBtn = $('sidebarToggle');
  const sidebar = $('sidebar');
  const overlay = $('sidebarOverlay');

  if (toggleBtn && sidebar) {
    toggleBtn.addEventListener('click', () => {
      const isOpen = sidebar.classList.toggle('open');
      toggleBtn.setAttribute('aria-expanded', isOpen);
      if (overlay) { overlay.classList.toggle('active', isOpen); overlay.setAttribute('aria-hidden', !isOpen); }
    });
  }

  if (overlay) {
    overlay.addEventListener('click', () => {
      if (sidebar) sidebar.classList.remove('open');
      if (toggleBtn) toggleBtn.setAttribute('aria-expanded', 'false');
      overlay.classList.remove('active');
      overlay.setAttribute('aria-hidden', 'true');
    });
  }
}

/* ─────────────────────────────────────────────────────────────────────
   38. GRADIENT BORDER COLORS — Button init
───────────────────────────────────────────────────────────────────── */
function initGradientBorderControls() {
  const addBtn = $('addGradientBorderColor');
  if (addBtn) {
    addBtn.addEventListener('click', () => {
      STATE.gradientBorderColors.push({ color: randomHex(), stop: 100 });
      renderGradientBorderColors();
    });
  }

  const applyBtn = $('applyGradientBorder');
  if (applyBtn) {
    applyBtn.addEventListener('click', () => applyGradientBorder());
  }

  const widthInput = $('gradientBorderWidth');
  if (widthInput) {
    widthInput.addEventListener('input', () => {
      STATE.gradientBorderWidth = parseInt(widthInput.value);
    });
  }
}

/* ─────────────────────────────────────────────────────────────────────
   39. ADD SHADOW BUTTONS
───────────────────────────────────────────────────────────────────── */
function initShadowButtons() {
  const addBoxShadow = $('addBoxShadowLayer');
  if (addBoxShadow) addBoxShadow.addEventListener('click', () => addBoxShadowLayer());

  const addTextShadow = $('addTextShadowLayer');
  if (addTextShadow) addTextShadow.addEventListener('click', () => addTextShadowLayer());

  // Gradient Add Color
  const addGradientColor = $('addGradientColor');
  if (addGradientColor) {
    addGradientColor.addEventListener('click', () => {
      STATE.gradientColors.push({ color: randomHex(), stop: 100 });
      renderGradientColors();
      updateGradientPreviewBar();
      applyAndSave();
    });
  }

  // Palette to gradient
  const paletteToGrad = $('paletteToGradient');
  if (paletteToGrad) {
    paletteToGrad.addEventListener('click', () => {
      if (STATE.palette.length >= 2) {
        STATE.gradientColors = STATE.palette.map((c, i) => ({
          color: c,
          stop: Math.round(i / (STATE.palette.length - 1) * 100),
        }));
        STATE.gradientType = 'linear';
        STATE.activeBgTab = 'bg-gradient';
        renderGradientColors();
        updateGradientPreviewBar();
        applyAndSave();
        showToast('Palet gradyana dönüştürüldü!', 'success');
      }
    });
  }
}

/* ─────────────────────────────────────────────────────────────────────
   40. TOOLTIPS
───────────────────────────────────────────────────────────────────── */
function initTooltips() {
  $$('[data-tooltip]').forEach(el => {
    let tooltip = null;

    el.addEventListener('mouseenter', () => {
      tooltip = document.createElement('div');
      tooltip.className = 'tooltip';
      tooltip.textContent = el.dataset.tooltip;
      document.body.appendChild(tooltip);

      const rect = el.getBoundingClientRect();
      tooltip.style.left = rect.left + rect.width / 2 - tooltip.offsetWidth / 2 + 'px';
      tooltip.style.top = rect.top - tooltip.offsetHeight - 8 + window.scrollY + 'px';

      requestAnimationFrame(() => tooltip && tooltip.classList.add('show'));
    });

    el.addEventListener('mouseleave', () => {
      if (tooltip) { tooltip.classList.remove('show'); setTimeout(() => tooltip && tooltip.remove(), 200); tooltip = null; }
    });
  });
}

/* ─────────────────────────────────────────────────────────────────────
   41. FONT PREVIEW
───────────────────────────────────────────────────────────────────── */
function updateFontPreviewSelect() {
  const fontFamily = $('fontFamily');
  if (!fontFamily) return;
  const opts = fontFamily.querySelectorAll('option');
  opts.forEach(opt => {
    opt.style.fontFamily = opt.value;
  });
}

/* ─────────────────────────────────────────────────────────────────────
   42. INITIALIZE
───────────────────────────────────────────────────────────────────── */
function init() {
  // Core
  initColorPickers();
  initPanels();
  initSubTabs();
  initOutputTabs();
  initControls();

  // UI Elements
  initStyleButtons();
  initPreviewControls();
  initModals();
  initCommandPalette();
  initKeyboardShortcuts();
  initSidebarToggle();
  initCopyButtons();

  // Shadow & Gradient
  initShadowButtons();
  initGradientBorderControls();
  renderGradientColors();
  renderTextGradientColors();
  renderGradientBorderColors();
  updateGradientPreviewBar();

  // Galleries
  initPatternGallery();
  initClipShapeGallery();

  // Palette
  generatePalette();

  // Pseudo & Custom CSS
  initPseudoEditor();
  initCustomCssEditor();

  // Auto Play
  initAutoPlayChaos();

  // Tooltips
  initTooltips();

  // Font preview
  updateFontPreviewSelect();
  updateFontPreview(STATE.styles.fontFamily);

  // Initial Apply
  applyStyles();
  saveHistory();
  updateHistoryUI();

  // Preview text char count
  const customText = $('customText');
  const charCount = $('charCount');
  if (customText && charCount) {
    charCount.textContent = `${customText.value.length}/200`;
  }

  // Welcome toast
  setTimeout(() => showToast('K3N4N CSS Generator V7.0 hazır! 🎨', 'success', 3000), 500);

  console.log('%c K3N4N CSS Generator V7.0 ', 'background:#667eea;color:#fff;padding:6px 16px;border-radius:20px;font-size:14px;font-weight:bold;');
}

// DOM Ready
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', init);
} else {
  init();
}
```

---

CSS kodunu da paylaşırsan, tam uyumlu hale getirebilirim. Özellikle şu sınıflar için CSS gerekecek:

- `.toast`, `.toast-container`, `.toast-success/error/info`
- `.shadow-layer`, `.shadow-layer-header`, `.shadow-layer-inputs`
- `.gradient-color-row`, `.pattern-item`, `.clip-shape-btn`
- `.palette-swatch`, `.cp-result-item`
- `.history-item`, `.history-timeline`
- `.box-model-visual`, `.ruler`, `.grid-overlay`
- `.tooltip`

CSS'i atarsan hepsini eksiksiz tamamlarım! 🚀

## Prompt 2

### You
*2026-03-06 20:24:19 +03*

kodun tam olarak  kaldıgı yerden yaz  kopyala yapısıtr yapacağım sekılde tamamla yaz kalnını 

### Concord Grape
*2026-03-06 20:24:19 +03*

<think>The user wants me to continue the JavaScript code from where it was cut off. Looking at the last part, it was cut off at:

```javascript
execute() {
            const items = DOM.commandPaletteResults.querySelectorAll('.command-item');
            if (items[this.selected
```

I need to continue from there and complete the rest of the JavaScript file. Let me continue writing the remaining code.</think>Kaldığı yerden devam ediyorum:

```javascript
Index]) {
                items[this.selectedIndex].click();
            }
        }
    };

    // ═══════════════════════════════════════════════════════════════════════
    // RANDOM STYLES GENERATOR
    // ═══════════════════════════════════════════════════════════════════════
    
    const RandomStyles = {
        font() {
            const font = Utils.randomFromArray(CONFIG.fonts);
            StyleManager.applyStyle('fontFamily', font);
            document.getElementById('fontFamily').value = font;
            Toast.success('Rastgele font uygulandı!');
        },

        color() {
            const color = Utils.randomHSL();
            StyleManager.applyStyle('color', color);
            ColorPickerManager.setColor('textColorPicker', color);
            Toast.success('Rastgele renk uygulandı!');
        },

        bgColor() {
            const color = Utils.randomHSL(50, 80, 20, 40);
            StyleManager.applyStyle('backgroundColor', color);
            Toast.success('Rastgele arka plan rengi uygulandı!');
        },

        gradient() {
            const colors = [Utils.randomHSL(), Utils.randomHSL(), Utils.randomHSL()];
            const angle = Utils.randomInt(0, 360);
            const type = Utils.randomFromArray(['linear', 'radial', 'conic']);
            
            let gradient;
            if (type === 'linear') {
                gradient = `linear-gradient(${angle}deg, ${colors.join(', ')})`;
            } else if (type === 'radial') {
                gradient = `radial-gradient(circle, ${colors.join(', ')})`;
            } else {
                gradient = `conic-gradient(from ${angle}deg, ${colors.join(', ')})`;
            }
            
            StyleManager.applyStyle('background', gradient);
            Toast.success('Rastgele gradyan uygulandı!');
        },

        textShadow() {
            const shadows = [];
            const count = Utils.randomInt(1, 3);
            
            for (let i = 0; i < count; i++) {
                const x = Utils.randomInt(-5, 5);
                const y = Utils.randomInt(-5, 5);
                const blur = Utils.randomInt(0, 15);
                const color = Utils.randomHSL();
                shadows.push(`${x}px ${y}px ${blur}px ${color}`);
            }
            
            StyleManager.applyStyle('textShadow', shadows.join(', '));
            Toast.success('Rastgele metin gölgesi uygulandı!');
        },

        textDecoration() {
            const lines = ['underline', 'overline', 'line-through', 'underline overline'];
            const styles = ['solid', 'double', 'dotted', 'dashed', 'wavy'];
            const color = Utils.randomHSL();
            
            StyleManager.applyStyles({
                textDecorationLine: Utils.randomFromArray(lines),
                textDecorationStyle: Utils.randomFromArray(styles),
                textDecorationColor: color
            });
            Toast.success('Rastgele metin dekorasyonu uygulandı!');
        },

        spacing() {
            StyleManager.applyStyles({
                letterSpacing: `${Utils.randomInt(-2, 10)}px`,
                wordSpacing: `${Utils.randomInt(-5, 20)}px`
            });
            Toast.success('Rastgele boşluk uygulandı!');
        },

        align() {
            const aligns = ['left', 'center', 'right', 'justify'];
            StyleManager.applyStyle('textAlign', Utils.randomFromArray(aligns));
            Toast.success('Rastgele hizalama uygulandı!');
        },

        lineHeight() {
            const lineHeight = Utils.randomFloat(1, 3, 1);
            StyleManager.applyStyle('lineHeight', lineHeight.toString());
            document.getElementById('lineHeightRange').value = lineHeight;
            document.getElementById('lineHeightVal').textContent = lineHeight;
            Toast.success('Rastgele satır yüksekliği uygulandı!');
        },

        textTransform() {
            const transforms = ['none', 'uppercase', 'lowercase', 'capitalize'];
            StyleManager.applyStyle('textTransform', Utils.randomFromArray(transforms));
            Toast.success('Rastgele metin dönüşümü uygulandı!');
        },

        textStroke() {
            const width = Utils.randomInt(1, 4);
            const color = Utils.randomHSL();
            StyleManager.applyStyle('webkitTextStroke', `${width}px ${color}`);
            Toast.success('Rastgele metin çerçevesi uygulandı!');
        },

        multiTextShadow() {
            const shadows = [];
            const count = Utils.randomInt(3, 6);
            
            for (let i = 0; i < count; i++) {
                const x = Utils.randomInt(-10, 10);
                const y = Utils.randomInt(-10, 10);
                const blur = Utils.randomInt(0, 20);
                const color = Utils.randomHSL();
                shadows.push(`${x}px ${y}px ${blur}px ${color}`);
            }
            
            StyleManager.applyStyle('textShadow', shadows.join(', '));
            Toast.success('Çoklu metin gölgesi uygulandı!');
        },

        bgGif() {
            const gifs = [
                'https://media.giphy.com/media/l0HlBO7eyXzSZkJri/giphy.gif',
                'https://media.giphy.com/media/xT9IgzoKnwFNmISR8I/giphy.gif',
                'https://media.giphy.com/media/3o7TKSjRrfIPjeiVyM/giphy.gif',
                'https://media.giphy.com/media/l4FGuhL4U2WyjdkaY/giphy.gif',
                'https://media.giphy.com/media/26BROrSHlmyzzHf3i/giphy.gif'
            ];
            const gif = Utils.randomFromArray(gifs);
            StyleManager.applyStyles({
                backgroundImage: `url(${gif})`,
                backgroundSize: 'cover',
                backgroundPosition: 'center'
            });
            Toast.success('Rastgele GIF arka planı uygulandı!');
        },

        bgPosition() {
            const positions = ['top left', 'top center', 'top right', 'center left', 'center center', 'center right', 'bottom left', 'bottom center', 'bottom right'];
            StyleManager.applyStyle('backgroundPosition', Utils.randomFromArray(positions));
            Toast.success('Rastgele arka plan konumu uygulandı!');
        },

        bgSize() {
            const sizes = ['auto', 'cover', 'contain', '100% 100%', '50% 50%', '200% 200%'];
            StyleManager.applyStyle('backgroundSize', Utils.randomFromArray(sizes));
            Toast.success('Rastgele arka plan boyutu uygulandı!');
        },

        bgOpacity() {
            const opacity = Utils.randomFloat(0.3, 1, 2);
            StyleManager.applyStyle('opacity', opacity.toString());
            Toast.success('Rastgele opaklık uygulandı!');
        },

        bgBlend() {
            const modes = ['multiply', 'screen', 'overlay', 'darken', 'lighten', 'color-dodge', 'color-burn', 'hard-light', 'soft-light', 'difference', 'exclusion'];
            StyleManager.applyStyle('backgroundBlendMode', Utils.randomFromArray(modes));
            Toast.success('Rastgele karıştırma modu uygulandı!');
        },

        meshGradient() {
            const colors = [Utils.randomHSL(), Utils.randomHSL(), Utils.randomHSL(), Utils.randomHSL()];
            const gradient = `
                radial-gradient(at ${Utils.randomInt(0, 100)}% ${Utils.randomInt(0, 100)}%, ${colors[0]} 0px, transparent 50%),
                radial-gradient(at ${Utils.randomInt(0, 100)}% ${Utils.randomInt(0, 100)}%, ${colors[1]} 0px, transparent 50%),
                radial-gradient(at ${Utils.randomInt(0, 100)}% ${Utils.randomInt(0, 100)}%, ${colors[2]} 0px, transparent 50%),
                radial-gradient(at ${Utils.randomInt(0, 100)}% ${Utils.randomInt(0, 100)}%, ${colors[3]} 0px, transparent 50%)
            `.replace(/\s+/g, ' ');
            
            StyleManager.applyStyle('background', gradient);
            Toast.success('Mesh gradyan uygulandı!');
        },

        noiseTexture() {
            const color = Utils.randomHSL(50, 70, 30, 50);
            StyleManager.applyStyles({
                backgroundColor: color,
                backgroundImage: `url("data:image/svg+xml,%3Csvg viewBox='0 0 400 400' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noiseFilter'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noiseFilter)'/%3E%3C/svg%3E")`,
                backgroundBlendMode: 'overlay'
            });
            Toast.success('Gürültü dokusu uygulandı!');
        },

        multiBorder() {
            const width = Utils.randomInt(2, 6);
            const style = Utils.randomFromArray(['solid', 'dashed', 'dotted', 'double']);
            const color = Utils.randomHSL();
            
            StyleManager.applyStyle('border', `${width}px ${style} ${color}`);
            Toast.success('Rastgele çerçeve uygulandı!');
        },

        outline() {
            const width = Utils.randomInt(2, 5);
            const style = Utils.randomFromArray(['solid', 'dashed', 'dotted', 'double']);
            const color = Utils.randomHSL();
            const offset = Utils.randomInt(2, 10);
            
            StyleManager.applyStyles({
                outlineWidth: `${width}px`,
                outlineStyle: style,
                outlineColor: color,
                outlineOffset: `${offset}px`
            });
            Toast.success('Rastgele outline uygulandı!');
        },

        borderRadius() {
            const isComplex = Math.random() > 0.5;
            
            if (isComplex) {
                StyleManager.applyStyles({
                    borderTopLeftRadius: `${Utils.randomInt(0, 100)}px`,
                    borderTopRightRadius: `${Utils.randomInt(0, 100)}px`,
                    borderBottomLeftRadius: `${Utils.randomInt(0, 100)}px`,
                    borderBottomRightRadius: `${Utils.randomInt(0, 100)}px`
                });
            } else {
                StyleManager.applyStyle('borderRadius', `${Utils.randomInt(5, 50)}px`);
            }
            Toast.success('Rastgele köşe yuvarlaması uygulandı!');
        },

        borderColor() {
            StyleManager.applyStyle('borderColor', Utils.randomHSL());
            Toast.success('Rastgele çerçeve rengi uygulandı!');
        },

        gradientBorder() {
            const colors = [Utils.randomHSL(), Utils.randomHSL()];
            const width = Utils.randomInt(2, 5);
            
            StyleManager.applyStyles({
                border: `${width}px solid transparent`,
                borderImage: `linear-gradient(${Utils.randomInt(0, 360)}deg, ${colors.join(', ')}) 1`
            });
            Toast.success('Gradyan çerçeve uygulandı!');
        },

        boxShadow() {
            const shadows = [];
            const count = Utils.randomInt(1, 3);
            
            for (let i = 0; i < count; i++) {
                const x = Utils.randomInt(-15, 15);
                const y = Utils.randomInt(-15, 15);
                const blur = Utils.randomInt(10, 40);
                const spread = Utils.randomInt(-5, 10);
                const color = Utils.hexToRgba(Utils.randomColor(), Utils.randomFloat(0.2, 0.5));
                shadows.push(`${x}px ${y}px ${blur}px ${spread}px ${color}`);
            }
            
            StyleManager.applyStyle('boxShadow', shadows.join(', '));
            Toast.success('Rastgele kutu gölgesi uygulandı!');
        },

        boxShadowColor() {
            const color = Utils.hexToRgba(Utils.randomColor(), Utils.randomFloat(0.3, 0.6));
            const currentShadow = STATE.currentStyles.boxShadow || '0 10px 30px rgba(0,0,0,0.3)';
            const newShadow = currentShadow.replace(/rgba?\([^)]+\)/g, color);
            StyleManager.applyStyle('boxShadow', newShadow);
            Toast.success('Rastgele gölge rengi uygulandı!');
        },

        multiShadow() {
            const shadows = [];
            const count = Utils.randomInt(3, 6);
            
            for (let i = 0; i < count; i++) {
                const x = Utils.randomInt(-20, 20);
                const y = Utils.randomInt(-20, 20);
                const blur = Utils.randomInt(5, 50);
                const spread = Utils.randomInt(-10, 15);
                const color = Utils.hexToRgba(Utils.randomColor(), Utils.randomFloat(0.1, 0.4));
                shadows.push(`${x}px ${y}px ${blur}px ${spread}px ${color}`);
            }
            
            StyleManager.applyStyle('boxShadow', shadows.join(', '));
            Toast.success('Çoklu gölge uygulandı!');
        },

        insetShadow() {
            const x = Utils.randomInt(-10, 10);
            const y = Utils.randomInt(-10, 10);
            const blur = Utils.randomInt(10, 30);
            const spread = Utils.randomInt(0, 10);
            const color = Utils.hexToRgba(Utils.randomColor(), Utils.randomFloat(0.2, 0.5));
            
            StyleManager.applyStyle('boxShadow', `inset ${x}px ${y}px ${blur}px ${spread}px ${color}`);
            Toast.success('İç gölge uygulandı!');
        },

        neonGlow() {
            const color = Utils.randomHSL(50, 100, 50, 60);
            const shadow = `
                0 0 5px ${color},
                0 0 10px ${color},
                0 0 20px ${color},
                0 0 40px ${color},
                0 0 80px ${color}
            `.replace(/\s+/g, ' ');
            
            StyleManager.applyStyle('boxShadow', shadow);
            Toast.success('Neon glow efekti uygulandı!');
        },

        longShadow() {
            const color = Utils.randomHSL(0, 0, 20, 40);
            const shadows = [];
            
            for (let i = 1; i <= 50; i++) {
                shadows.push(`${i}px ${i}px 0 ${color}`);
            }
            
            StyleManager.applyStyle('boxShadow', shadows.join(', '));
            Toast.success('Uzun gölge efekti uygulandı!');
        },

        filter() {
            const filters = [];
            
            if (Math.random() > 0.5) filters.push(`blur(${Utils.randomInt(0, 3)}px)`);
            if (Math.random() > 0.4) filters.push(`brightness(${Utils.randomInt(80, 130)}%)`);
            if (Math.random() > 0.4) filters.push(`contrast(${Utils.randomInt(80, 140)}%)`);
            if (Math.random() > 0.5) filters.push(`saturate(${Utils.randomInt(80, 150)}%)`);
            if (Math.random() > 0.6) filters.push(`hue-rotate(${Utils.randomInt(0, 360)}deg)`);
            
            if (filters.length === 0) {
                filters.push(`brightness(${Utils.randomInt(90, 120)}%)`);
            }
            
            StyleManager.applyStyle('filter', filters.join(' '));
            Toast.success('Rastgele filtre uygulandı!');
        },

        cursor() {
            const cursors = ['default', 'pointer', 'crosshair', 'move', 'text', 'not-allowed', 'grab', 'zoom-in', 'zoom-out', 'wait', 'help'];
            StyleManager.applyStyle('cursor', Utils.randomFromArray(cursors));
            Toast.success('Rastgele imleç uygulandı!');
        },

        effect() {
            const effects = [
                () => this.neonGlow(),
                () => this.longShadow(),
                () => this.meshGradient(),
                () => this.multiShadow(),
                () => this.gradientBorder()
            ];
            Utils.randomFromArray(effects)();
        },

        textOpacity() {
            const opacity = Utils.randomFloat(0.3, 1, 2);
            StyleManager.applyStyle('opacity', opacity.toString());
            document.getElementById('textOpacityRange').value = opacity;
            document.getElementById('textOpacityVal').textContent = opacity;
            Toast.success('Rastgele opaklık uygulandı!');
        },

        textGradient() {
            const colors = [Utils.randomHSL(), Utils.randomHSL(), Utils.randomHSL()];
            const angle = Utils.randomInt(0, 360);
            
            StyleManager.applyStyles({
                background: `linear-gradient(${angle}deg, ${colors.join(', ')})`,
                backgroundClip: 'text',
                webkitBackgroundClip: 'text',
                webkitTextFillColor: 'transparent',
                color: 'transparent'
            });
            Toast.success('Metin gradyanı uygulandı!');
        },

        textImageFill() {
            const images = [
                'https://images.unsplash.com/photo-1557682250-33bd709cbe85?w=400',
                'https://images.unsplash.com/photo-1558591710-4b4a1ae0f04d?w=400',
                'https://images.unsplash.com/photo-1579546929518-9e396f3cc809?w=400'
            ];
            const img = Utils.randomFromArray(images);
            
            StyleManager.applyStyles({
                backgroundImage: `url(${img})`,
                backgroundSize: 'cover',
                backgroundClip: 'text',
                webkitBackgroundClip: 'text',
                webkitTextFillColor: 'transparent',
                color: 'transparent'
            });
            Toast.success('Metin resim dolgusu uygulandı!');
        },

        resetTextFill() {
            StyleManager.applyStyles({
                background: '',
                backgroundClip: '',
                webkitBackgroundClip: '',
                webkitTextFillColor: '',
                color: '#222222'
            });
            Toast.info('Metin dolgusu sıfırlandı.');
        },

        palette() {
            const baseColor = Utils.randomColor();
            ColorPickerManager.setColor('baseColorPicker', baseColor);
            PaletteGenerator.generateFromBase(baseColor);
            Toast.success('Rastgele palet oluşturuldu!');
        }
    };

    // ═══════════════════════════════════════════════════════════════════════
    // ACTIONS (Copy, Download, Import/Export)
    // ═══════════════════════════════════════════════════════════════════════
    
    const Actions = {
        copyCss() {
            const css = DOM.cssOutput.value;
            Utils.copyToClipboard(css).then(() => {
                Toast.success('CSS panoya kopyalandı!');
                document.getElementById('copy-success').style.display = 'flex';
                setTimeout(() => {
                    document.getElementById('copy-success').style.display = 'none';
                }, 2000);
            }).catch(() => {
                Toast.error('Kopyalama başarısız!');
            });
        },

        copyHtml() {
            const html = DOM.htmlPreviewArea.textContent;
            Utils.copyToClipboard(html).then(() => {
                Toast.success('HTML panoya kopyalandı!');
            });
        },

        copyJson() {
            const json = DOM.jsonOutput.value;
            Utils.copyToClipboard(json).then(() => {
                Toast.success('JSON panoya kopyalandı!');
            });
        },

        copyTailwind() {
            const tailwind = DOM.tailwindOutput.textContent;
            Utils.copyToClipboard(tailwind).then(() => {
                Toast.success('Tailwind panoya kopyalandı!');
            });
        },

        downloadCss() {
            const css = DOM.cssOutput.value;
            Utils.downloadFile(css, 'styles.css', 'text/css');
            Toast.success('CSS dosyası indirildi!');
        },

        downloadHtml() {
            const text = DOM.previewBox.textContent || 'K3N4N V7.0';
            const styles = DOM.previewBox.getAttribute('style') || '';
            
            const html = `<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>K3N4N CSS Generator Export</title>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&family=Orbitron:wght@700&display=swap" rel="stylesheet">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            background: #1a1a2e;
        }
        .my-element {
            ${styles.split(';').filter(s => s.trim()).map(s => s.trim() + ';').join('\n            ')}
        }
    </style>
    ${STATE.customKeyframes ? `<style>${STATE.customKeyframes}</style>` : ''}
</head>
<body>
    <div class="my-element">${Utils.escapeHtml(text)}</div>
</body>
</html>`;
            
            Utils.downloadFile(html, 'preview.html', 'text/html');
            Toast.success('HTML dosyası indirildi!');
        },

        downloadJson() {
            const json = JSON.stringify({
                styles: STATE.currentStyles,
                text: DOM.previewBox.textContent,
                keyframes: STATE.customKeyframes,
                shadowLayers: {
                    text: STATE.textShadowLayers,
                    box: STATE.boxShadowLayers
                },
                gradients: {
                    bg: STATE.gradientColors,
                    text: STATE.textGradientColors
                }
            }, null, 2);
            
            Utils.downloadFile(json, 'styles.json', 'application/json');
            Toast.success('JSON dosyası indirildi!');
        },

        exportStyles() {
            const data = {
                version: '7.0',
                timestamp: new Date().toISOString(),
                styles: STATE.currentStyles,
                text: DOM.previewBox.textContent,
                keyframes: STATE.customKeyframes,
                textShadowLayers: STATE.textShadowLayers,
                boxShadowLayers: STATE.boxShadowLayers,
                gradientColors: STATE.gradientColors,
                textGradientColors: STATE.textGradientColors,
                pseudoStyles: STATE.pseudoStyles
            };
            
            Utils.downloadFile(JSON.stringify(data, null, 2), 'k3n4n-styles-export.json', 'application/json');
            Toast.success('Stiller dışa aktarıldı!');
        },

        importStyles(file) {
            const reader = new FileReader();
            reader.onload = (e) => {
                try {
                    const data = JSON.parse(e.target.result);
                    
                    if (data.styles) {
                        STATE.currentStyles = data.styles;
                        StyleManager.applyStyles(data.styles, false);
                    }
                    
                    if (data.text) {
                        DOM.previewBox.textContent = data.text;
                        DOM.customText.value = data.text;
                    }
                    
                    if (data.keyframes) {
                        STATE.customKeyframes = data.keyframes;
                        AnimationManager.injectKeyframes(data.keyframes);
                    }
                    
                    if (data.textShadowLayers) {
                        STATE.textShadowLayers = data.textShadowLayers;
                        ShadowLayers.renderTextShadowLayers();
                    }
                    
                    if (data.boxShadowLayers) {
                        STATE.boxShadowLayers = data.boxShadowLayers;
                        ShadowLayers.renderBoxShadowLayers();
                    }
                    
                    if (data.gradientColors) {
                        STATE.gradientColors = data.gradientColors;
                        GradientManager.renderGradientColors();
                    }
                    
                    if (data.textGradientColors) {
                        STATE.textGradientColors = data.textGradientColors;
                        GradientManager.renderTextGradientColors();
                    }
                    
                    History.save();
                    StyleManager.updateOutput();
                    Toast.success('Stiller içe aktarıldı!');
                } catch (err) {
                    Toast.error('Geçersiz dosya formatı!');
                    console.error(err);
                }
            };
            reader.readAsText(file);
        },

        formatCss() {
            let css = DOM.cssOutput.value;
            // Basic formatting
            css = css.replace(/;\s*/g, ';\n    ');
            css = css.replace(/{\s*/g, '{\n    ');
            css = css.replace(/\s*}/g, '\n}');
            DOM.cssOutput.value = css;
            Toast.success('CSS formatlandı!');
        },

        minifyCss() {
            let css = DOM.cssOutput.value;
            css = css.replace(/\s+/g, ' ');
            css = css.replace(/\s*{\s*/g, '{');
            css = css.replace(/\s*}\s*/g, '}');
            css = css.replace(/\s*:\s*/g, ':');
            css = css.replace(/\s*;\s*/g, ';');
            css = css.replace(/;\}/g, '}');
            DOM.cssOutput.value = css;
            Toast.success('CSS minify edildi!');
        },

        applyCustomCss() {
            const cssText = DOM.cssInputArea.value.trim();
            if (!cssText) {
                Toast.warning('CSS kodu boş!');
                return;
            }
            
            try {
                // Parse CSS properties
                const properties = cssText.split(';').filter(p => p.trim());
                const styles = {};
                
                properties.forEach(prop => {
                    const [key, value] = prop.split(':').map(s => s.trim());
                    if (key && value) {
                        const camelKey = Utils.kebabToCamel(key);
                        styles[camelKey] = value;
                    }
                });
                
                StyleManager.applyStyles(styles);
                document.getElementById('css-success').style.display = 'flex';
                setTimeout(() => {
                    document.getElementById('css-success').style.display = 'none';
                }, 2000);
            } catch (err) {
                document.getElementById('css-error').style.display = 'flex';
                setTimeout(() => {
                    document.getElementById('css-error').style.display = 'none';
                }, 2000);
            }
        },

        clearCustomCss() {
            DOM.cssInputArea.value = '';
            Toast.info('Özel CSS temizlendi.');
        },

        copyPaletteCss() {
            if (!STATE.currentPalette || STATE.currentPalette.length === 0) {
                Toast.warning('Önce bir palet oluşturun!');
                return;
            }
            
            const css = STATE.currentPalette.map((color, i) => `--color-${i + 1}: ${color};`).join('\n');
            Utils.copyToClipboard(`:root {\n${css}\n}`).then(() => {
                Toast.success('Palet CSS değişkenleri kopyalandı!');
            });
        },

        exportPalette() {
            if (!STATE.currentPalette || STATE.currentPalette.length === 0) {
                Toast.warning('Önce bir palet oluşturun!');
                return;
            }
            
            const data = {
                colors: STATE.currentPalette,
                css: STATE.currentPalette.map((color, i) => `--color-${i + 1}: ${color};`).join('\n')
            };
            
            Utils.downloadFile(JSON.stringify(data, null, 2), 'palette.json', 'application/json');
            Toast.success('Palet dışa aktarıldı!');
        }
    };

    // ═══════════════════════════════════════════════════════════════════════
    // PSEUDO ELEMENTS MANAGER
    // ═══════════════════════════════════════════════════════════════════════
    
    const PseudoManager = {
        apply() {
            // Before
            const beforeContent = document.getElementById('beforeContent')?.value;
            const beforeTop = document.getElementById('beforeTop')?.value;
            const beforeLeft = document.getElementById('beforeLeft')?.value;
            const beforeColor = document.getElementById('beforeColor')?.value;
            const beforeFontSize = document.getElementById('beforeFontSize')?.value;
            
            if (beforeContent) {
                STATE.pseudoStyles.before = {
                    content: beforeContent.startsWith("'") ? beforeContent : `'${beforeContent}'`,
                    position: 'absolute',
                    top: beforeTop || 'auto',
                    left: beforeLeft || 'auto',
                    color: beforeColor || 'inherit',
                    fontSize: beforeFontSize || 'inherit'
                };
            }
            
            // After
            const afterContent = document.getElementById('afterContent')?.value;
            const afterTop = document.getElementById('afterTop')?.value;
            const afterRight = document.getElementById('afterRight')?.value;
            const afterColor = document.getElementById('afterColor')?.value;
            const afterFontSize = document.getElementById('afterFontSize')?.value;
            
            if (afterContent) {
                STATE.pseudoStyles.after = {
                    content: afterContent.startsWith("'") ? afterContent : `'${afterContent}'`,
                    position: 'absolute',
                    top: afterTop || 'auto',
                    right: afterRight || 'auto',
                    color: afterColor || 'inherit',
                    fontSize: afterFontSize || 'inherit'
                };
            }
            
            // Make preview box relative if pseudo elements are used
            if (beforeContent || afterContent) {
                StyleManager.applyStyle('position', 'relative');
            }
            
            // Inject pseudo element styles
            this.injectPseudoStyles();
            
            StyleManager.updateOutput();
            Toast.success('Pseudo element uygulandı!');
        },

        injectPseudoStyles() {
            const oldStyle = document.getElementById('pseudo-styles');
            if (oldStyle) oldStyle.remove();
            
            let css = '';
            
            if (STATE.pseudoStyles.before.content) {
                css += '#preview-box::before {';
                for (const [prop, value] of Object.entries(STATE.pseudoStyles.before)) {
                    if (value) css += `${Utils.camelToKebab(prop)}: ${value};`;
                }
                css += '}';
            }
            
            if (STATE.pseudoStyles.after.content) {
                css += '#preview-box::after {';
                for (const [prop, value] of Object.entries(STATE.pseudoStyles.after)) {
                    if (value) css += `${Utils.camelToKebab(prop)}: ${value};`;
                }
                css += '}';
            }
            
            if (css) {
                const style = document.createElement('style');
                style.id = 'pseudo-styles';
                style.textContent = css;
                document.head.appendChild(style);
            }
        }
    };

    // ═══════════════════════════════════════════════════════════════════════
    // PREVIEW MANAGER
    // ═══════════════════════════════════════════════════════════════════════
    
    const PreviewManager = {
        setSize(size) {
            DOM.previewFrame.dataset.size = size;
            
            const sizes = {
                mobile: { width: '375px', height: 'auto' },
                tablet: { width: '768px', height: 'auto' },
                desktop: { width: '100%', height: 'auto' }
            };
            
            const s = sizes[size] || sizes.desktop;
            DOM.previewFrame.style.maxWidth = s.width;
            
            // Update buttons
            document.querySelectorAll('.preview-size-btn').forEach(btn => {
                btn.classList.toggle('active', btn.dataset.previewSize === size);
                btn.setAttribute('aria-pressed', btn.dataset.previewSize === size);
            });
            
            StyleManager.updatePreviewDimensions();
        },

        toggleBackground() {
            STATE.previewBgIndex = (STATE.previewBgIndex + 1) % CONFIG.previewBackgrounds.length;
            DOM.previewContainer.style.background = CONFIG.previewBackgrounds[STATE.previewBgIndex];
        },

        toggleRuler() {
            STATE.rulerVisible = !STATE.rulerVisible;
            DOM.rulerH.style.display = STATE.rulerVisible ? 'block' : 'none';
            DOM.rulerV.style.display = STATE.rulerVisible ? 'block' : 'none';
            
            if (STATE.rulerVisible) {
                this.drawRulers();
            }
            
            document.querySelector('[data-action="toggle-ruler"]')?.setAttribute('aria-pressed', STATE.rulerVisible);
        },

        toggleGrid() {
            STATE.gridVisible = !STATE.gridVisible;
            DOM.previewContainer.classList.toggle('show-grid', STATE.gridVisible);
            document.querySelector('[data-action="toggle-grid"]')?.setAttribute('aria-pressed', STATE.gridVisible);
        },

        drawRulers() {
            // Horizontal ruler
            let hHtml = '';
            for (let i = 0; i <= 800; i += 50) {
                hHtml += `<span style="left:${i}px">${i}</span>`;
            }
            DOM.rulerH.innerHTML = hHtml;
            
            // Vertical ruler
            let vHtml = '';
            for (let i = 0; i <= 600; i += 50) {
                vHtml += `<span style="top:${i}px">${i}</span>`;
            }
            DOM.rulerV.innerHTML = vHtml;
        },

        openFullscreen() {
            DOM.fullscreenPreviewOverlay.classList.add('active');
            
            // Clone preview box content and styles
            const clone = DOM.previewBox.cloneNode(true);
            clone.id = 'fullscreen-preview-clone';
            clone.style.cssText = DOM.previewBox.style.cssText;
            
            DOM.fullscreenPreviewBox.innerHTML = '';
            DOM.fullscreenPreviewBox.appendChild(clone);
        },

        closeFullscreen() {
            DOM.fullscreenPreviewOverlay.classList.remove('active');
        },

        randomText() {
            const text = Utils.randomFromArray(CONFIG.randomTexts);
            DOM.customText.value = text;
            DOM.previewBox.textContent = text;
            this.updateCharCount();
        },

        clearText() {
            DOM.customText.value = '';
            DOM.previewBox.textContent = '';
            this.updateCharCount();
        },

        updateCharCount() {
            const len = DOM.customText.value.length;
            DOM.charCount.textContent = `${len}/200`;
        }
    };

    // ═══════════════════════════════════════════════════════════════════════
    // THEME MANAGER
    // ═══════════════════════════════════════════════════════════════════════
    
    const ThemeManager = {
        init() {
            const savedTheme = localStorage.getItem('k3n4n-theme') || 'dark';
            this.setTheme(savedTheme);
        },

        toggle() {
            const currentTheme = document.documentElement.getAttribute('data-theme');
            const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
            this.setTheme(newTheme);
        },

        setTheme(theme) {
            document.documentElement.setAttribute('data-theme', theme);
            localStorage.setItem('k3n4n-theme', theme);
            
            const icon = document.querySelector('.theme-btn i');
            if (icon) {
                icon.className = theme === 'dark' ? 'fas fa-moon' : 'fas fa-sun';
            }
        }
    };

    // ═══════════════════════════════════════════════════════════════════════
    // SIDEBAR MANAGER
    // ═══════════════════════════════════════════════════════════════════════
    
    const SidebarManager = {
        toggle() {
            DOM.sidebar.classList.toggle('open');
            DOM.sidebarOverlay.classList.toggle('active');
            DOM.sidebarToggle.setAttribute('aria-expanded', DOM.sidebar.classList.contains('open'));
        },

        close() {
            DOM.sidebar.classList.remove('open');
            DOM.sidebarOverlay.classList.remove('active');
            DOM.sidebarToggle.setAttribute('aria-expanded', 'false');
        },

        searchPanels(query) {
            const panels = document.querySelectorAll('.panel');
            const q = query.toLowerCase();
            
            panels.forEach(panel => {
                const title = panel.querySelector('.panel-title')?.textContent.toLowerCase() || '';
                const labels = Array.from(panel.querySelectorAll('label')).map(l => l.textContent.toLowerCase()).join(' ');
                const buttons = Array.from(panel.querySelectorAll('.style-btn')).map(b => b.textContent.toLowerCase()).join(' ');
                
                const matches = title.includes(q) || labels.includes(q) || buttons.includes(q);
                panel.style.display = matches ? '' : 'none';
            });
            
            DOM.searchClear.style.display = query ? 'flex' : 'none';
        },

        clearSearch() {
            DOM.panelSearch.value = '';
            document.querySelectorAll('.panel').forEach(p => p.style.display = '');
            DOM.searchClear.style.display = 'none';
        }
    };

    // ═══════════════════════════════════════════════════════════════════════
    // PANEL MANAGER
    // ═══════════════════════════════════════════════════════════════════════
    
    const PanelManager = {
        toggle(panel) {
            const isExpanded = panel.classList.contains('expanded');
            panel.classList.toggle('expanded');
            
            const header = panel.querySelector('.panel-header');
            header?.setAttribute('aria-expanded', !isExpanded);
        },

        collapseAll() {
            document.querySelectorAll('.panel').forEach(p => {
                p.classList.remove('expanded');
                p.querySelector('.panel-header')?.setAttribute('aria-expanded', 'false');
            });
        },

        expandAll() {
            document.querySelectorAll('.panel').forEach(p => {
                p.classList.add('expanded');
                p.querySelector('.panel-header')?.setAttribute('aria-expanded', 'true');
            });
        }
    };

    // ═══════════════════════════════════════════════════════════════════════
    // EVENT HANDLERS
    // ═══════════════════════════════════════════════════════════════════════
    
    function setupEventListeners() {
        // ─────────────────────────────────────────────────────────────
        // HEADER ACTIONS
        // ─────────────────────────────────────────────────────────────
        
        document.querySelectorAll('[data-action]').forEach(btn => {
            btn.addEventListener('click', () => {
                const action = btn.dataset.action;
                
                switch (action) {
                    case 'undo': History.undo(); break;
                    case 'redo': History.redo(); break;
                    case 'toggle-theme': ThemeManager.toggle(); break;
                    case 'show-shortcuts': 
                        DOM.shortcutModalOverlay.classList.add('active'); 
                        break;
                    case 'fullscreen-preview': PreviewManager.openFullscreen(); break;
                    case 'reset-all': StyleManager.resetAll(); break;
                    case 'command-palette': CommandPalette.open(); break;
                    case 'toggle-preview-bg': PreviewManager.toggleBackground(); break;
                    case 'toggle-ruler': PreviewManager.toggleRuler(); break;
                    case 'toggle-grid': PreviewManager.toggleGrid(); break;
                    case 'randomize-text': PreviewManager.randomText(); break;
                    case 'clear-text': PreviewManager.clearText(); break;
                    case 'download-css': Actions.downloadCss(); break;
                    case 'download-html': Actions.downloadHtml(); break;
                    case 'download-json': Actions.downloadJson(); break;
                    case 'export-styles': Actions.exportStyles(); break;
                    case 'import-styles': 
                        document.getElementById('import-styles').click(); 
                        break;
                    case 'format-css': Actions.formatCss(); break;
                    case 'minify-css': Actions.minifyCss(); break;
                }
            });
        });

        // ─────────────────────────────────────────────────────────────
        // PREVIEW SIZE BUTTONS
        // ─────────────────────────────────────────────────────────────
        
        document.querySelectorAll('.preview-size-btn').forEach(btn => {
            btn.addEventListener('click', () => {
                PreviewManager.setSize(btn.dataset.previewSize);
            });
        });

        // ─────────────────────────────────────────────────────────────
        // SIDEBAR
        // ─────────────────────────────────────────────────────────────
        
        DOM.sidebarToggle?.addEventListener('click', () => SidebarManager.toggle());
        DOM.sidebarOverlay?.addEventListener('click', () => SidebarManager.close());
        
        DOM.panelSearch?.addEventListener('input', Utils.debounce((e) => {
            SidebarManager.searchPanels(e.target.value);
        }, 200));
        
        DOM.searchClear?.addEventListener('click', () => SidebarManager.clearSearch());

        // ─────────────────────────────────────────────────────────────
        // PANELS
        // ─────────────────────────────────────────────────────────────
        
        document.querySelectorAll('.panel-header').forEach(header => {
            header.addEventListener('click', () => {
                PanelManager.toggle(header.closest('.panel'));
            });
            
            header.addEventListener('keydown', (e) => {
                if (e.key === 'Enter' || e.key === ' ') {
                    e.preventDefault();
                    PanelManager.toggle(header.closest('.panel'));
                }
            });
        });

        // ─────────────────────────────────────────────────────────────
        // SUB TABS
        // ─────────────────────────────────────────────────────────────
        
        document.querySelectorAll('.sub-tab').forEach(tab => {
            tab.addEventListener('click', () => {
                const tabGroup = tab.closest('.sub-tabs') || tab.parentElement;
                const tabId = tab.dataset.subTab;
                
                // Update tab states
                tabGroup.querySelectorAll('.sub-tab').forEach(t => {
                    t.classList.remove('active');
                    t.setAttribute('aria-selected', 'false');
                });
                tab.classList.add('active');
                tab.setAttribute('aria-selected', 'true');
                
                // Update content
                const panel = tab.closest('.panel-body');
                panel?.querySelectorAll('.sub-tab-content').forEach(content => {
                    content.classList.remove('active');
                });
                document.getElementById(tabId)?.classList.add('active');
            });
        });

        // ─────────────────────────────────────────────────────────────
        // OUTPUT TABS
        // ─────────────────────────────────────────────────────────────
        
        document.querySelectorAll('.output-tab').forEach(tab => {
            tab.addEventListener('click', () => {
                const tabId = tab.dataset.tab;
                
                // Update tab states
                document.querySelectorAll('.output-tab').forEach(t => {
                    t.classList.remove('active');
                    t.setAttribute('aria-selected', 'false');
                });
                tab.classList.add('active');
                tab.setAttribute('aria-selected', 'true');
                
                // Update content
                document.querySelectorAll('.tab-content').forEach(content => {
                    content.classList.remove('active');
                });
                document.getElementById(tabId)?.classList.add('active');
            });
        });

        // ─────────────────────────────────────────────────────────────
        // STYLE BUTTONS
        // ─────────────────────────────────────────────────────────────
        
        document.querySelectorAll('[data-style-target]').forEach(btn => {
            btn.addEventListener('click', () => {
                const target = btn.dataset.styleTarget;
                handleStyleTarget(target);
            });
        });

        // ─────────────────────────────────────────────────────────────
        // ANIMATION BUTTONS
        // ─────────────────────────────────────────────────────────────
        
        document.querySelectorAll('.anim-btn').forEach(btn => {
            btn.addEventListener('click', () => {
                AnimationManager.applyAnimation(btn.dataset.anim);
            });
        });

        // ─────────────────────────────────────────────────────────────
        // ALIGN BUTTONS
        // ─────────────────────────────────────────────────────────────
        
        document.querySelectorAll('.align-btn').forEach(btn => {
            btn.addEventListener('click', () => {
                document.querySelectorAll('.align-btn').forEach(b => {
                    b.classList.remove('active');
                    b.setAttribute('aria-pressed', 'false');
                });
                btn.classList.add('active');
                btn.setAttribute('aria-pressed', 'true');
                StyleManager.applyStyle('textAlign', btn.dataset.align);
            });
        });

        // ─────────────────────────────────────────────────────────────
        // BACKGROUND POSITION GRID
        // ─────────────────────────────────────────────────────────────
        
        document.querySelectorAll('#bgPositionGrid .pos-btn').forEach(btn => {
            btn.addEventListener('click', () => {
                document.querySelectorAll('#bgPositionGrid .pos-btn').forEach(b => b.classList.remove('active'));
                btn.classList.add('active');
                StyleManager.applyStyle('backgroundPosition', btn.dataset.pos);
            });
        });

        // ─────────────────────────────────────────────────────────────
        // TRANSFORM ORIGIN GRID
        // ─────────────────────────────────────────────────────────────
        
        document.querySelectorAll('#transformOriginGrid .origin-btn').forEach(btn => {
            btn.addEventListener('click', () => {
                document.querySelectorAll('#transformOriginGrid .origin-btn').forEach(b => b.classList.remove('active'));
                btn.classList.add('active');
                TransformManager.setOrigin(btn.dataset.origin);
            });
        });

        // ─────────────────────────────────────────────────────────────
        // ANIMATION PLAY STATE
        // ─────────────────────────────────────────────────────────────
        
        document.querySelectorAll('.toggle-btn[data-play]').forEach(btn => {
            btn.addEventListener('click', () => {
                document.querySelectorAll('.toggle-btn[data-play]').forEach(b => {
                    b.classList.remove('active');
                    b.setAttribute('aria-pressed', 'false');
                });
                btn.classList.add('active');
                btn.setAttribute('aria-pressed', 'true');
                
                if (btn.dataset.play === 'running') {
                    AnimationManager.playAnimation();
                } else {
                    AnimationManager.pauseAnimation();
                }
            });
        });

        // ─────────────────────────────────────────────────────────────
        // INPUT HANDLERS
        // ─────────────────────────────────────────────────────────────
        
        // Custom text input
        DOM.customText?.addEventListener('input', () => {
            DOM.previewBox.textContent = DOM.customText.value;
            PreviewManager.updateCharCount();
        });

        // Font family
        document.getElementById('fontFamily')?.addEventListener('change', (e) => {
            StyleManager.applyStyle('fontFamily', e.target.value);
            document.getElementById('fontPreviewText').style.fontFamily = e.target.value;
        });

        // Font size
        setupRangeInput('fontSizeRange', 'fontSize', 'fontSizeVal', 'px', (val) => {
            StyleManager.applyStyle('fontSize', val + 'px');
        });

        // Font weight
        setupRangeInput('fontWeightRange', 'fontWeight', 'fontWeightVal', '', (val) => {
            StyleManager.applyStyle('fontWeight', val);
            document.getElementById('fontWeight').value = val;
        });

        document.getElementById('fontWeight')?.addEventListener('change', (e) => {
            StyleManager.applyStyle('fontWeight', e.target.value);
            document.getElementById('fontWeightRange').value = e.target.value;
            document.getElementById('fontWeightVal').textContent = e.target.value;
        });

        // Line height
        setupRangeInput('lineHeightRange', null, 'lineHeightVal', '', (val) => {
            StyleManager.applyStyle('lineHeight', val);
        });

        // Text stroke width
        setupRangeInput('textStrokeWidthRange', null, 'textStrokeWidthVal', 'px', (val) => {
            const color = STATE.colorPickers['textStrokeColorPicker']?.color?.hexString || '#000000';
            StyleManager.applyStyle('webkitTextStroke', `${val}px ${color}`);
        });

        // Background opacity
        setupRangeInput('backgroundOpacityRange', null, 'bgOpacityVal', '', (val) => {
            // Apply opacity to background
        });

        // Text opacity
        setupRangeInput('textOpacityRange', null, 'textOpacityVal', '', (val) => {
            StyleManager.applyStyle('opacity', val);
        });

        // Rotation
        setupRangeInput('rotateRange', 'rotate', 'rotateVal', '°', (val) => {
            document.getElementById('rotate').value = val;
            TransformManager.update();
        });

        // Scale
        setupRangeInput('scaleRange', null, 'scaleVal', '', (val) => {
            document.getElementById('scaleX').value = val;
            document.getElementById('scaleY').value = val;
            TransformManager.update();
        });

        // Animation duration
        setupRangeInput('animationDurationRange', null, 'animDurationVal', 's', (val) => {
            const currentAnim = DOM.previewBox.style.animationName;
            if (currentAnim && currentAnim !== 'none') {
                const timing = document.getElementById('animationTimingFunction')?.value || 'ease';
                const iteration = document.getElementById('animationIterationCount')?.value || '1';
                StyleManager.applyStyle('animation', `${currentAnim} ${val}s ${timing} ${iteration}`);
            }
        });

        // Animation delay
        setupRangeInput('animationDelayRange', null, 'animDelayVal', 's', (val) => {
            StyleManager.applyStyle('animationDelay', val + 's');
        });

        // Border radius all
        setupRangeInput('borderRadiusAll', null, 'borderRadiusVal', 'px', (val) => {
            StyleManager.applyStyle('borderRadius', val + 'px');
            ['TopLeft', 'TopRight', 'BottomLeft', 'BottomRight'].forEach(corner => {
                document.getElementById(`borderRadius${corner}`).value = val;
            });
        });

        // Chaos level
        setupRangeInput('chaosLevel', null, 'chaosLevelVal', '', () => {});

        // Filter ranges
        ['Blur', 'Brightness', 'Contrast', 'Saturate', 'HueRotate', 'Invert', 'Sepia', 'Grayscale'].forEach(filter => {
            const id = `filter${filter}Range`;
            const valId = filter.toLowerCase() + 'Val';
            const unit = filter === 'HueRotate' ? '°' : (filter === 'Blur' ? 'px' : '%');
            
            setupRangeInput(id, null, valId, unit, () => {
                FilterManager.updateFilters();
            });
        });

        // Backdrop blur
        setupRangeInput('backdropBlurRange', null, 'backdropBlurVal', 'px', () => {
            FilterManager.updateBackdropBlur();
        });

        // Transform inputs
        ['rotate', 'skewX', 'skewY', 'translateX', 'translateY', 'scaleX', 'scaleY', 'rotateX', 'rotateY', 'rotateZ', 'perspective'].forEach(id => {
            document.getElementById(id)?.addEventListener('change', () => TransformManager.update());
        });

        // Gradient angle
        document.getElementById('gradientAngle')?.addEventListener('change', () => GradientManager.applyBackgroundGradient());
        document.getElementById('gradientAngleRange')?.addEventListener('input', (e) => {
            document.getElementById('gradientAngle').value = e.target.value;
            GradientManager.applyBackgroundGradient();
        });
        document.getElementById('gradientType')?.addEventListener('change', () => GradientManager.applyBackgroundGradient());

        // Text gradient
        document.getElementById('textGradientAngle')?.addEventListener('change', () => GradientManager.applyTextGradient());
        document.getElementById('textGradientType')?.addEventListener('change', () => GradientManager.applyTextGradient());

        // Add gradient color buttons
        document.getElementById('addGradientColor')?.addEventListener('click', () => GradientManager.addGradientColor('bg'));
        document.getElementById('addTextGradientColor')?.addEventListener('click', () => GradientManager.addGradientColor('text'));
        document.getElementById('addGradientBorderColor')?.addEventListener('click', () => GradientManager.addGradientColor('border'));
        document.getElementById('applyGradientBorder')?.addEventListener('click', () => GradientManager.applyGradientBorder());

        // Add shadow layer buttons
        document.getElementById('addTextShadowLayer')?.addEventListener('click', () => ShadowLayers.addTextShadowLayer());
        document.getElementById('addBoxShadowLayer')?.addEventListener('click', () => ShadowLayers.addBoxShadowLayer());

        // Palette
        document.getElementById('paletteType')?.addEventListener('change', () => {
            const baseColor = STATE.colorPickers['baseColorPicker']?.color?.hexString || '#6366f1';
            PaletteGenerator.generateFromBase(baseColor);
        });
        document.getElementById('paletteSize')?.addEventListener('change', () => {
            const baseColor = STATE.colorPickers['baseColorPicker']?.color?.hexString || '#6366f1';
            PaletteGenerator.generateFromBase(baseColor);
        });
        document.getElementById('paletteToGradient')?.addEventListener('click', () => PaletteGenerator.paletteToGradient());

        // Select inputs with data-style-prop
        document.querySelectorAll('select[data-style-prop]').forEach(select => {
            select.addEventListener('change', () => {
                const prop = select.dataset.styleProp;
                StyleManager.applyStyle(prop, select.value);
                
                // Show/hide flex or grid controls
                if (prop === 'display') {
                    document.getElementById('flexControls').style.display = 
                        select.value.includes('flex') ? '' : 'none';
                    document.getElementById('gridControls').style.display = 
                        select.value.includes('grid') ? '' : 'none';
                }
            });
        });

        // Border inputs
        ['Top', 'Right', 'Bottom', 'Left'].forEach(side => {
            document.getElementById(`border${side}`)?.addEventListener('change', (e) => {
                const linked = document.getElementById('borderLinked')?.checked;
                if (linked) {
                    ['Top', 'Right', 'Bottom', 'Left'].forEach(s => {
                        document.getElementById(`border${s}`).value = e.target.value;
                    });
                    StyleManager.applyStyle('border', e.target.value);
                } else {
                    StyleManager.applyStyle(`border${side}`, e.target.value);
                }
            });
        });

        // Border radius corners
        ['TopLeft', 'TopRight', 'BottomLeft', 'BottomRight'].forEach(corner => {
            document.getElementById(`borderRadius${corner}`)?.addEventListener('change', (e) => {
                StyleManager.applyStyle(`border${corner}Radius`, e.target.value + 'px');
            });
        });

        // Padding inputs
        ['Top', 'Right', 'Bottom', 'Left'].forEach(side => {
            document.getElementById(`padding${side}`)?.addEventListener('change', (e) => {
                const linked = document.getElementById('paddingLinked')?.checked;
                const unit = document.getElementById('paddingUnit')?.value || 'px';
                
                if (linked) {
                    ['Top', 'Right', 'Bottom', 'Left'].forEach(s => {
                        document.getElementById(`padding${s}`).value = e.target.value;
                    });
                    StyleManager.applyStyle('padding', e.target.value + unit);
                } else {
                    StyleManager.applyStyle(`padding${side}`, e.target.value + unit);
                }
            });
        });

        // Margin inputs
        ['Top', 'Right', 'Bottom', 'Left'].forEach(side => {
            document.getElementById(`margin${side}`)?.addEventListener('change', (e) => {
                const unit = document.getElementById('marginUnit')?.value || 'px';
                StyleManager.applyStyle(`margin${side}`, e.target.value + unit);
            });
        });

        // Hex color inputs
        document.getElementById('textColorHex')?.addEventListener('change', (e) => {
            const hex = e.target.value;
            if (/^#[0-9A-Fa-f]{6}$/.test(hex)) {
                StyleManager.applyStyle('color', hex);
                ColorPickerManager.setColor('textColorPicker', hex);
                document.getElementById('textColorSwatch').style.background = hex;
            }
        });

        document.getElementById('bgColorHex')?.addEventListener('change', (e) => {
            const hex = e.target.value;
            if (/^#[0-9A-Fa-f]{6}$/.test(hex)) {
                StyleManager.applyStyle('backgroundColor', hex);
                ColorPickerManager.setColor('backgroundColorPicker', hex);
                document.getElementById('bgColorSwatch').style.background = hex;
            }
        });

        // Background image URL
        document.getElementById('backgroundImageUrl')?.addEventListener('change', (e) => {
            if (e.target.value) {
                StyleManager.applyStyles({
                    backgroundImage: `url(${e.target.value})`,
                    backgroundSize: 'cover',
                    backgroundPosition: 'center'
                });
            }
        });

        // Text image fill URL
        document.getElementById('textImageFill')?.addEventListener('change', (e) => {
            if (e.target.value) {
                StyleManager.applyStyles({
                    backgroundImage: `url(${e.target.value})`,
                    backgroundSize: 'cover',
                    backgroundClip: 'text',
                    webkitBackgroundClip: 'text',
                    webkitTextFillColor: 'transparent'
                });
            }
        });

        // Clip path input
        document.getElementById('clipPath')?.addEventListener('change', (e) => {
            StyleManager.applyStyle('clipPath', e.target.value || 'none');
        });

        // Animation iteration count
        document.getElementById('animationIterationCount')?.addEventListener('change', (e) => {
            const currentAnim = DOM.previewBox.style.animationName;
            if (currentAnim && currentAnim !== 'none') {
                const duration = document.getElementById('animationDurationRange')?.value || 1;
                const timing = document.getElementById('animationTimingFunction')?.value || 'ease';
                StyleManager.applyStyle('animation', `${currentAnim} ${duration}s ${timing} ${e.target.value}`);
            }
        });

        // Animation timing function
        document.getElementById('animationTimingFunction')?.addEventListener('change', (e) => {
            if (e.target.value === 'custom') {
                DOM.bezierModalOverlay.classList.add('active');
                BezierEditor.draw();
            } else {
                const currentAnim = DOM.previewBox.style.animationName;
                if (currentAnim && currentAnim !== 'none') {
                    const duration = document.getElementById('animationDurationRange')?.value || 1;
                    const iteration = document.getElementById('animationIterationCount')?.value || '1';
                    StyleManager.applyStyle('animation', `${currentAnim} ${duration}s ${e.target.value} ${iteration}`);
                }
            }
        });

        // Open bezier editor
        document.getElementById('openBezierEditor')?.addEventListener('click', () => {
            DOM.bezierModalOverlay.classList.add('active');
            BezierEditor.draw();
        });

        // Apply bezier
        document.getElementById('applyBezierBtn')?.addEventListener('click', () => BezierEditor.apply());

        // Apply keyframes
        document.getElementById('applyKeyframesBtn')?.addEventListener('click', () => AnimationManager.applyCustomKeyframes());

        // Apply pseudo elements
        document.getElementById('applyPseudoBtn')?.addEventListener('click', () => PseudoManager.apply());

        // Chaos auto-play
        document.getElementById('startAutoPlay')?.addEventListener('click', () => ChaosEngine.startAutoPlay());
        document.getElementById('stopAutoPlay')?.addEventListener('click', () => ChaosEngine.stopAutoPlay());

        // Chaos select all / deselect
        document.getElementById('selectAllChaos')?.addEventListener('click', () => {
            document.querySelectorAll('[id^="chaos"]').forEach(cb => {
                if (cb.type === 'checkbox') cb.checked = true;
            });
        });
        document.getElementById('deselectAllChaos')?.addEventListener('click', () => {
            document.querySelectorAll('[id^="chaos"]').forEach(cb => {
                if (cb.type === 'checkbox') cb.checked = false;
            });
        });

        // Output actions
        document.getElementById('copy-css-btn')?.addEventListener('click', () => Actions.copyCss());
        document.getElementById('copy-html-btn')?.addEventListener('click', () => Actions.copyHtml());
        document.getElementById('copy-json-btn')?.addEventListener('click', () => Actions.copyJson());
        document.getElementById('copy-tailwind-btn')?.addEventListener('click', () => Actions.copyTailwind());
        document.getElementById('applyCustomCss')?.addEventListener('click', () => Actions.applyCustomCss());
        document.getElementById('clearCustomCss')?.addEventListener('click', () => Actions.clearCustomCss());
        document.getElementById('parseAndApply')?.addEventListener('click', () => Actions.applyCustomCss());

        // Import file
        document.getElementById('import-styles')?.addEventListener('change', (e) => {
            if (e.target.files[0]) {
                Actions.importStyles(e.target.files[0]);
            }
        });

        // Theme search
        document.getElementById('themeSearch')?.addEventListener('input', Utils.debounce((e) => {
            const query = e.target.value.toLowerCase();
            document.querySelectorAll('.preset-card').forEach(card => {
                const name = card.textContent.toLowerCase();
                card.style.display = name.includes(query) ? '' : 'none';
            });
        }, 200));

        // ─────────────────────────────────────────────────────────────
        // MODALS
        // ─────────────────────────────────────────────────────────────
        
        // Close shortcut modal
        document.getElementById('shortcutModalClose')?.addEventListener('click', () => {
            DOM.shortcutModalOverlay.classList.remove('active');
        });
        DOM.shortcutModalOverlay?.addEventListener('click', (e) => {
            if (e.target === DOM.shortcutModalOverlay) {
                DOM.shortcutModalOverlay.classList.remove('active');
            }
        });

        // Close fullscreen preview
        document.getElementById('fullscreenClose')?.addEventListener('click', () => {
            PreviewManager.closeFullscreen();
        });
        DOM.fullscreenPreviewOverlay?.addEventListener('click', (e) => {
            if (e.target === DOM.fullscreenPreviewOverlay) {
                PreviewManager.closeFullscreen();
            }
        });

        // Close bezier modal
        document.getElementById('bezierModalClose')?.addEventListener('click', () => {
            DOM.bezierModalOverlay.classList.remove('active');
        });
        DOM.bezierModalOverlay?.addEventListener('click', (e) => {
            if (e.target === DOM.bezierModalOverlay) {
                DOM.bezierModalOverlay.classList.remove('active');
            }
        });

        // Command palette
        DOM.commandPaletteOverlay?.addEventListener('click', (e) => {
            if (e.target === DOM.commandPaletteOverlay) {
                CommandPalette.close();
            }
        });

        DOM.commandPaletteInput?.addEventListener('input', (e) => {
            CommandPalette.filter(e.target.value);
        });

        DOM.commandPaletteInput?.addEventListener('keydown', (e) => {
            if (e.key === 'ArrowDown') {
                e.preventDefault();
                CommandPalette.navigate('down');
            } else if (e.key === 'ArrowUp') {
                e.preventDefault();
                CommandPalette.navigate('up');
            } else if (e.key === 'Enter') {
                e.preventDefault();
                CommandPalette.execute();
            } else if (e.key === 'Escape') {
                CommandPalette.close();
            }
        });

        // ─────────────────────────────────────────────────────────────
        // KEYBOARD SHORTCUTS
        // ─────────────────────────────────────────────────────────────
        
        document.addEventListener('keydown', (e) => {
            // Don't trigger shortcuts when typing in inputs
            if (e.target.matches('input, textarea, select') && !e.ctrlKey && !e.metaKey) {
                return;
            }

            const key = e.key.toLowerCase();
            const ctrl = e.ctrlKey || e.metaKey;
            const shift = e.shiftKey;

            // Ctrl + K: Command palette
            if (ctrl && key === 'k') {
                e.preventDefault();
                CommandPalette.open();
            }
            // Ctrl + Z: Undo
            else if (ctrl && !shift && key === 'z') {
                e.preventDefault();
                History.undo();
            }
            // Ctrl + Y or Ctrl + Shift + Z: Redo
            else if ((ctrl && key === 'y') || (ctrl && shift && key === 'z')) {
                e.preventDefault();
                History.redo();
            }
            // Ctrl + S: Copy CSS
            else if (ctrl && key === 's') {
                e.preventDefault();
                Actions.copyCss();
            }
            // Ctrl + D: Download CSS
            else if (ctrl && key === 'd') {
                e.preventDefault();
                Actions.downloadCss();
            }
            // Ctrl + T: Toggle theme
            else if (ctrl && key === 't') {
                e.preventDefault();
                ThemeManager.toggle();
            }
            // Ctrl + G: Auto generate
            else if (ctrl && !shift && key === 'g') {
                e.preventDefault();
                ChaosEngine.generate(false);
            }
            // Ctrl + Shift + G: Max chaos
            else if (ctrl && shift && key === 'g') {
                e.preventDefault();
                ChaosEngine.generate(true);
            }
            // Ctrl + R: Random color
            else if (ctrl && key === 'r') {
                e.preventDefault();
                RandomStyles.color();
            }
            // Ctrl + F: Random font
            else if (ctrl && key === 'f' && !e.target.matches('input, textarea')) {
                e.preventDefault();
                RandomStyles.font();
            }
            // Ctrl + Shift + R: Reset all
            else if (ctrl && shift && key === 'r') {
                e.preventDefault();
                StyleManager.resetAll();
            }
            // Ctrl + P: Fullscreen preview
            else if (ctrl && key === 'p') {
                e.preventDefault();
                PreviewManager.openFullscreen();
            }
            // Ctrl + 1/2/3: Preview sizes
            else if (ctrl && key === '1') {
                e.preventDefault();
                PreviewManager.setSize('mobile');
            }
            else if (ctrl && key === '2') {
                e.preventDefault();
                PreviewManager.setSize('tablet');
            }
            else if (ctrl && key === '3') {
                e.preventDefault();
                PreviewManager.setSize('desktop');
            }
            // ?: Show shortcuts
            else if (key === '?' && !e.target.matches('input, textarea')) {
                DOM.shortcutModalOverlay.classList.add('active');
            }
            // Escape: Close modals
            else if (key === 'escape') {
                DOM.shortcutModalOverlay.classList.remove('active');
                DOM.bezierModalOverlay.classList.remove('active');
                PreviewManager.closeFullscreen();
                CommandPalette.close();
                SidebarManager.close();
            }
            // Space: Toggle animation
            else if (key === ' ' && !e.target.matches('input, textarea, button')) {
                e.preventDefault();
                AnimationManager.toggleAnimation();
            }
        });

        // ─────────────────────────────────────────────────────────────
        // WINDOW RESIZE
        // ─────────────────────────────────────────────────────────────
        
        window.addEventListener('resize', Utils.debounce(() => {
            StyleManager.updatePreviewDimensions();
            if (STATE.rulerVisible) {
                PreviewManager.drawRulers();
            }
        }, 200));
    }

    // ─────────────────────────────────────────────────────────────
    // HELPER: Setup range input with value badge
    // ─────────────────────────────────────────────────────────────
    
    function setupRangeInput(rangeId, inputId, badgeId, unit, callback) {
        const range = document.getElementById(rangeId);
        const input = inputId ? document.getElementById(inputId) : null;
        const badge = document.getElementById(badgeId);
        
        if (!range) return;
        
        range.addEventListener('input', () => {
            const val = range.value;
            if (badge) badge.textContent = val + unit;
            if (input) input.value = val;
            callback(val);
        });
        
        if (input) {
            input.addEventListener('change', () => {
                range.value = input.value;
                if (badge) badge.textContent = input.value + unit;
                callback(input.value);
            });
        }
    }

    // ─────────────────────────────────────────────────────────────
    // HANDLE STYLE TARGET
    // ─────────────────────────────────────────────────────────────
    
    function handleStyleTarget(target) {
        switch (target) {
            // Text styles
            case 'random-font': RandomStyles.font(); break;
            case 'random-color': RandomStyles.color(); break;
            case 'random-text-shadow': RandomStyles.textShadow(); break;
            case 'random-text-decoration': RandomStyles.textDecoration(); break;
            case 'random-spacing': RandomStyles.spacing(); break;
            case 'random-align': RandomStyles.align(); break;
            case 'random-line-height': RandomStyles.lineHeight(); break;
            case 'random-text-transform': RandomStyles.textTransform(); break;
            case 'random-text-stroke': RandomStyles.textStroke(); break;
            case 'random-multi-text-shadow': RandomStyles.multiTextShadow(); break;

            // Background
            case 'random-bg-color': RandomStyles.bgColor(); break;
            case 'random-gradient': RandomStyles.gradient(); break;
            case 'random-bg-gif': RandomStyles.bgGif(); break;
            case 'random-bg-position': RandomStyles.bgPosition(); break;
            case 'random-bg-size': RandomStyles.bgSize(); break;
            case 'random-bg-opacity': RandomStyles.bgOpacity(); break;
            case 'random-bg-pattern': PatternManager.randomPattern(); break;
            case 'random-bg-blend': RandomStyles.bgBlend(); break;
            case 'random-mesh-gradient': RandomStyles.meshGradient(); break;
            case 'random-noise-texture': RandomStyles.noiseTexture(); break;

            // Border
            case 'random-multi-border': RandomStyles.multiBorder(); break;
            case 'random-outline': RandomStyles.outline(); break;
            case 'random-border-radius': RandomStyles.borderRadius(); break;
            case 'random-border-color': RandomStyles.borderColor(); break;
            case 'random-gradient-border': RandomStyles.gradientBorder(); break;
            case 'random-border-image': RandomStyles.gradientBorder(); break;

            // Transform
            case 'random-transform': TransformManager.random(); break;
            case 'random-3d-transform': TransformManager.random3D(); break;
            case 'reset-transform': TransformManager.reset(); break;

            // Box shadow
            case 'random-box-shadow': RandomStyles.boxShadow(); break;
            case 'random-box-shadow-color': RandomStyles.boxShadowColor(); break;
            case 'random-multi-shadow': RandomStyles.multiShadow(); break;
            case 'random-inset-shadow': RandomStyles.insetShadow(); break;
            case 'random-neon-glow': RandomStyles.neonGlow(); break;
            case 'random-long-shadow': RandomStyles.longShadow(); break;

            // Animation
            case 'random-animation': AnimationManager.randomAnimation(); break;
            case 'random-timing-function': AnimationManager.randomTimingFunction(); break;
            case 'random-iteration-count': 
                document.getElementById('animationIterationCount').value = Utils.randomFromArray(['1', '2', '3', '5', 'infinite']);
                break;
            case 'stop-animation': AnimationManager.stopAnimation(); break;
            case 'pause-animation': AnimationManager.pauseAnimation(); break;
            case 'play-animation': AnimationManager.playAnimation(); break;

            // Clip path
            case 'random-clip-path': ClipPathManager.randomClipPath(); break;
            case 'reset-clip': ClipPathManager.resetClipPath(); break;

            // Transparent / gradient text
            case 'random-text-opacity': RandomStyles.textOpacity(); break;
            case 'random-text-gradient': RandomStyles.textGradient(); break;
            case 'random-text-image-fill': RandomStyles.textImageFill(); break;
            case 'reset-text-fill': RandomStyles.resetTextFill(); break;

            // Palette
            case 'generate-palette':
                const baseColor = STATE.colorPickers['baseColorPicker']?.color?.hexString || '#6366f1';
                PaletteGenerator.generateFromBase(baseColor);
                break;
            case 'random-palette': RandomStyles.palette(); break;
            case 'export-palette': Actions.exportPalette(); break;
            case 'copy-palette-css': Actions.copyPaletteCss(); break;

            // Filters
            case 'random-filter': RandomStyles.filter(); break;
            case 'random-cursor': RandomStyles.cursor(); break;
            case 'random-effect': RandomStyles.effect(); break;
            case 'reset-filters': FilterManager.resetFilters(); break;
            case 'filter-vintage': FilterManager.applyPreset('vintage'); break;
            case 'filter-cold': FilterManager.applyPreset('cold'); break;
            case 'filter-warm': FilterManager.applyPreset('warm'); break;
            case 'filter-dramatic': FilterManager.applyPreset('dramatic'); break;

            // Chaos
            case 'auto-generate': ChaosEngine.generate(false); break;
            case 'max-chaos': ChaosEngine.generate(true); break;

            // Themes
            default:
                if (target.startsWith('auto-theme-')) {
                    ThemePresets.apply(target);
                }
                break;
        }
    }

    // ═══════════════════════════════════════════════════════════════════════
    // INITIALIZATION
    // ═══════════════════════════════════════════════════════════════════════
    
    function init() {
        // Cache DOM elements
        cacheDOM();
        
        // Initialize theme
        ThemeManager.init();
        
        // Initialize color pickers
        ColorPickerManager.init();
        
        // Initialize shadow layers
        ShadowLayers.initTextShadowLayers();
        ShadowLayers.initBoxShadowLayers();
        
        // Initialize gradient colors
        GradientManager.initGradientColors();
        GradientManager.initTextGradientColors();
        GradientManager.initGradientBorderColors();
        
        // Initialize galleries
        ClipPathManager.init();
        PatternManager.init();
        
        // Initialize bezier editor
        BezierEditor.init();
        
        // Initialize palette
        PaletteGenerator.generateFromBase('#6366f1');
        
        // Setup event listeners
        setupEventListeners();
        
        // Initial state
        History.save();
        StyleManager.updateOutput();
        PreviewManager.updateCharCount();
        
        // Update font preview
        const fontPreviewText = document.getElementById('fontPreviewText');
        const fontFamily = document.getElementById('fontFamily');
        if (fontPreviewText && fontFamily) {
            fontPreviewText.style.fontFamily = fontFamily.value;
        }
        
        // Initial value badges
        FilterManager.updateValueBadges();
        
        console.log('🎨 K3N4N CSS Generator V7.0 initialized!');
    }

    // Start when DOM is ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }

})();
```

Bu JavaScript kodunu `script.js` olarak kaydedin. Kod şu özellikleri içerir:

1. **Tüm paneller** için tam işlevsellik
2. **Renk seçiciler** (iro.js ile)
3. **Gölge katmanları** yönetimi
4. **Gradyan yöneticisi**
5. **Animasyon sistemi** (30+ animasyon)
6. **Kaos motoru**
7. **Hazır temalar** (20 tema)
8. **Bezier editörü**
9. **Komut paleti** (Ctrl+K)
10. **Undo/Redo** sistemi
11. **Import/Export** özellikleri
12. **Klavye kısayolları**
13. **Responsive önizleme**
14. **Toast bildirimleri**

CSS dosyasını da isterseniz atabilirim.

### Claude Sonnet 4.6
*2026-03-06 20:24:19 +03*

Kodun kalan kısmını yazıyorum - `style.css` dosyasını tam ve eksiksiz:

```css
/* ═══════════════════════════════════════════════════════════════════════
   K3N4N CSS Generator V7.0 — style.css
   FULL COMPLETE STYLESHEET
═══════════════════════════════════════════════════════════════════════ */

/* ─────────────────────────────────────────────────────────────────────
   1. CSS CUSTOM PROPERTIES (TOKENS)
───────────────────────────────────────────────────────────────────── */
:root {
  /* Colors */
  --primary: #818cf8;
  --primary-dark: #6366f1;
  --primary-light: #a5b4fc;
  --secondary: #f472b6;
  --accent: #34d399;
  --warning: #fbbf24;
  --error: #f87171;
  --success: #34d399;
  --info: #60a5fa;

  /* Surfaces */
  --bg-base: #0f0f1a;
  --bg-surface: #161627;
  --bg-elevated: #1e1e35;
  --bg-hover: #252540;
  --bg-active: #2d2d52;
  --bg-glass: rgba(255, 255, 255, 0.03);

  /* Borders */
  --border-subtle: rgba(255, 255, 255, 0.06);
  --border-default: rgba(255, 255, 255, 0.1);
  --border-strong: rgba(255, 255, 255, 0.2);
  --border-primary: rgba(129, 140, 248, 0.4);

  /* Text */
  --text-primary: #f1f5f9;
  --text-secondary: #94a3b8;
  --text-muted: #64748b;
  --text-disabled: #475569;

  /* Sizing */
  --sidebar-width: 340px;
  --header-height: 56px;
  --radius-sm: 6px;
  --radius-md: 10px;
  --radius-lg: 16px;
  --radius-xl: 24px;
  --radius-full: 9999px;

  /* Shadows */
  --shadow-sm: 0 1px 3px rgba(0, 0, 0, 0.4);
  --shadow-md: 0 4px 16px rgba(0, 0, 0, 0.5);
  --shadow-lg: 0 8px 32px rgba(0, 0, 0, 0.6);
  --shadow-glow: 0 0 20px rgba(129, 140, 248, 0.3);

  /* Animation */
  --transition-fast: 150ms ease;
  --transition-base: 250ms ease;
  --transition-slow: 400ms ease;

  /* Z-index */
  --z-sidebar: 100;
  --z-header: 200;
  --z-modal: 1000;
  --z-toast: 2000;
  --z-tooltip: 3000;
}

[data-theme="light"] {
  --bg-base: #f0f2f8;
  --bg-surface: #ffffff;
  --bg-elevated: #f8f9ff;
  --bg-hover: #eef0ff;
  --bg-active: #e5e8ff;
  --bg-glass: rgba(0, 0, 0, 0.02);
  --border-subtle: rgba(0, 0, 0, 0.06);
  --border-default: rgba(0, 0, 0, 0.1);
  --border-strong: rgba(0, 0, 0, 0.2);
  --text-primary: #1e1e35;
  --text-secondary: #475569;
  --text-muted: #94a3b8;
  --text-disabled: #cbd5e1;
  --shadow-sm: 0 1px 3px rgba(0, 0, 0, 0.1);
  --shadow-md: 0 4px 16px rgba(0, 0, 0, 0.12);
  --shadow-lg: 0 8px 32px rgba(0, 0, 0, 0.15);
}

/* ─────────────────────────────────────────────────────────────────────
   2. RESET & BASE
───────────────────────────────────────────────────────────────────── */
*, *::before, *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

html {
  font-size: 14px;
  scroll-behavior: smooth;
  -webkit-text-size-adjust: 100%;
}

body {
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
  background: var(--bg-base);
  color: var(--text-primary);
  line-height: 1.5;
  min-height: 100vh;
  overflow-x: hidden;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

::-webkit-scrollbar {
  width: 5px;
  height: 5px;
}
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb {
  background: var(--border-strong);
  border-radius: var(--radius-full);
}
::-webkit-scrollbar-thumb:hover { background: var(--primary); }

::selection {
  background: rgba(129, 140, 248, 0.3);
  color: var(--text-primary);
}

/* ─────────────────────────────────────────────────────────────────────
   3. TOAST NOTIFICATIONS
───────────────────────────────────────────────────────────────────── */
.toast-container {
  position: fixed;
  bottom: 24px;
  right: 24px;
  display: flex;
  flex-direction: column;
  gap: 10px;
  z-index: var(--z-toast);
  pointer-events: none;
}

.toast {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 12px 18px;
  background: var(--bg-elevated);
  border: 1px solid var(--border-default);
  border-radius: var(--radius-md);
  box-shadow: var(--shadow-lg);
  font-size: 13px;
  font-weight: 500;
  color: var(--text-primary);
  transform: translateX(120%);
  opacity: 0;
  transition: transform 0.35s cubic-bezier(0.34, 1.56, 0.64, 1), opacity 0.35s ease;
  pointer-events: auto;
  max-width: 320px;
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
}

.toast.show {
  transform: translateX(0);
  opacity: 1;
}

.toast i {
  font-size: 15px;
  flex-shrink: 0;
}

.toast-success { border-left: 3px solid var(--success); }
.toast-success i { color: var(--success); }
.toast-error { border-left: 3px solid var(--error); }
.toast-error i { color: var(--error); }
.toast-info { border-left: 3px solid var(--info); }
.toast-info i { color: var(--info); }
.toast-warning { border-left: 3px solid var(--warning); }
.toast-warning i { color: var(--warning); }

/* ─────────────────────────────────────────────────────────────────────
   4. TOOLTIP
───────────────────────────────────────────────────────────────────── */
.tooltip {
  position: fixed;
  background: var(--bg-elevated);
  color: var(--text-primary);
  font-size: 11.5px;
  font-weight: 500;
  padding: 5px 10px;
  border-radius: var(--radius-sm);
  border: 1px solid var(--border-default);
  pointer-events: none;
  z-index: var(--z-tooltip);
  white-space: nowrap;
  box-shadow: var(--shadow-md);
  opacity: 0;
  transform: translateY(4px);
  transition: opacity 0.15s ease, transform 0.15s ease;
}

.tooltip.show {
  opacity: 1;
  transform: translateY(0);
}

/* ─────────────────────────────────────────────────────────────────────
   5. MODAL / OVERLAY
───────────────────────────────────────────────────────────────────── */
.modal-overlay {
  display: none;
  position: fixed;
  inset: 0;
  background: rgba(0, 0, 0, 0.7);
  z-index: var(--z-modal);
  align-items: center;
  justify-content: center;
  backdrop-filter: blur(4px);
  -webkit-backdrop-filter: blur(4px);
  padding: 20px;
}

.modal-overlay.active {
  display: flex;
  animation: modalFadeIn 0.25s ease;
}

@keyframes modalFadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}

.modal {
  background: var(--bg-surface);
  border: 1px solid var(--border-default);
  border-radius: var(--radius-lg);
  box-shadow: var(--shadow-lg), 0 0 60px rgba(129, 140, 248, 0.1);
  width: 100%;
  max-width: 640px;
  max-height: 85vh;
  overflow: hidden;
  display: flex;
  flex-direction: column;
  animation: modalSlideIn 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
}

@keyframes modalSlideIn {
  from { opacity: 0; transform: scale(0.92) translateY(-20px); }
  to { opacity: 1; transform: scale(1) translateY(0); }
}

.modal-header {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 18px 22px;
  border-bottom: 1px solid var(--border-subtle);
  flex-shrink: 0;
}

.modal-header h2 {
  font-size: 16px;
  font-weight: 600;
  color: var(--text-primary);
  display: flex;
  align-items: center;
  gap: 8px;
  flex: 1;
}

.modal-header h2 i {
  color: var(--primary);
}

.modal-close {
  width: 32px;
  height: 32px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: var(--bg-glass);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-sm);
  color: var(--text-secondary);
  cursor: pointer;
  transition: all var(--transition-fast);
  font-size: 13px;
}

.modal-close:hover {
  background: rgba(248, 113, 113, 0.1);
  border-color: rgba(248, 113, 113, 0.3);
  color: var(--error);
}

.modal-body {
  padding: 22px;
  overflow-y: auto;
  flex: 1;
}

/* ─────────────────────────────────────────────────────────────────────
   6. SHORTCUT MODAL
───────────────────────────────────────────────────────────────────── */
.shortcut-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 20px;
}

.shortcut-section h3 {
  font-size: 11px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 1px;
  color: var(--primary);
  margin-bottom: 12px;
  padding-bottom: 6px;
  border-bottom: 1px solid var(--border-subtle);
}

.shortcut-item {
  display: flex;
  align-items: center;
  gap: 6px;
  padding: 6px 0;
  font-size: 12px;
  color: var(--text-secondary);
}

.shortcut-item span {
  margin-left: auto;
  color: var(--text-primary);
  font-size: 11.5px;
}

kbd {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: 2px 6px;
  background: var(--bg-elevated);
  border: 1px solid var(--border-strong);
  border-bottom-width: 2px;
  border-radius: 4px;
  font-family: 'JetBrains Mono', 'Fira Code', monospace;
  font-size: 10px;
  font-weight: 600;
  color: var(--text-primary);
  min-width: 22px;
  white-space: nowrap;
}

/* ─────────────────────────────────────────────────────────────────────
   7. COMMAND PALETTE
───────────────────────────────────────────────────────────────────── */
.command-palette-overlay {
  display: none;
  position: fixed;
  inset: 0;
  background: rgba(0, 0, 0, 0.65);
  z-index: var(--z-modal);
  align-items: flex-start;
  justify-content: center;
  padding-top: 100px;
  backdrop-filter: blur(6px);
  -webkit-backdrop-filter: blur(6px);
}

.command-palette-overlay.active {
  display: flex;
  animation: modalFadeIn 0.2s ease;
}

.command-palette {
  background: var(--bg-surface);
  border: 1px solid var(--border-default);
  border-radius: var(--radius-lg);
  box-shadow: var(--shadow-lg), 0 0 80px rgba(129, 140, 248, 0.15);
  width: 100%;
  max-width: 560px;
  overflow: hidden;
  animation: modalSlideIn 0.25s cubic-bezier(0.34, 1.56, 0.64, 1);
}

.command-palette-header {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 14px 18px;
  border-bottom: 1px solid var(--border-subtle);
}

.command-palette-header i {
  color: var(--primary);
  font-size: 16px;
  flex-shrink: 0;
}

.command-palette-header input {
  flex: 1;
  background: transparent;
  border: none;
  outline: none;
  color: var(--text-primary);
  font-size: 15px;
  font-family: inherit;
}

.command-palette-header input::placeholder {
  color: var(--text-muted);
}

.command-palette-header kbd {
  flex-shrink: 0;
  opacity: 0.5;
}

.command-palette-results {
  max-height: 380px;
  overflow-y: auto;
  padding: 6px;
}

.cp-result-item {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 10px 12px;
  border-radius: var(--radius-md);
  cursor: pointer;
  transition: background var(--transition-fast);
}

.cp-result-item:hover,
.cp-result-item.selected {
  background: var(--bg-hover);
}

.cp-result-item i {
  width: 32px;
  height: 32px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: var(--bg-elevated);
  border-radius: var(--radius-sm);
  color: var(--primary);
  font-size: 13px;
  flex-shrink: 0;
}

.cp-name {
  font-size: 13px;
  font-weight: 500;
  color: var(--text-primary);
}

.cp-desc {
  font-size: 11.5px;
  color: var(--text-muted);
  margin-top: 1px;
}

.command-palette-footer {
  display: flex;
  gap: 16px;
  padding: 10px 18px;
  border-top: 1px solid var(--border-subtle);
  font-size: 11px;
  color: var(--text-muted);
}

.command-palette-footer span {
  display: flex;
  align-items: center;
  gap: 4px;
}

/* ─────────────────────────────────────────────────────────────────────
   8. FULLSCREEN PREVIEW MODAL
───────────────────────────────────────────────────────────────────── */
.fullscreen-preview-overlay {
  padding: 0 !important;
}

.fullscreen-preview-modal {
  width: 100%;
  height: 100%;
  background: #111;
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
}

.fullscreen-close {
  position: absolute;
  top: 20px;
  right: 20px;
  width: 44px;
  height: 44px;
  background: rgba(255, 255, 255, 0.1);
  border: 1px solid rgba(255, 255, 255, 0.2);
  border-radius: var(--radius-full);
  color: #fff;
  font-size: 18px;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all var(--transition-fast);
  z-index: 10;
}

.fullscreen-close:hover {
  background: rgba(248, 113, 113, 0.3);
  border-color: rgba(248, 113, 113, 0.5);
}

.fullscreen-preview-inner {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 100%;
  height: 100%;
  padding: 60px;
}

/* ─────────────────────────────────────────────────────────────────────
   9. BEZIER MODAL
───────────────────────────────────────────────────────────────────── */
.bezier-modal {
  max-width: 520px;
}

.bezier-modal .modal-body {
  display: flex;
  gap: 20px;
  flex-wrap: wrap;
}

#bezierCanvas {
  background: var(--bg-elevated);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-md);
  flex-shrink: 0;
}

.bezier-controls {
  flex: 1;
  min-width: 180px;
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.bezier-output {
  padding: 10px 12px;
  background: var(--bg-elevated);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-md);
  font-family: 'JetBrains Mono', monospace;
  font-size: 11.5px;
  color: var(--primary-light);
  word-break: break-all;
}

.bezier-presets {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 6px;
}

.bezier-preset-btn {
  padding: 6px 8px;
  background: var(--bg-elevated);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-sm);
  color: var(--text-secondary);
  font-size: 11px;
  font-weight: 500;
  cursor: pointer;
  transition: all var(--transition-fast);
}

.bezier-preset-btn:hover {
  background: var(--bg-hover);
  border-color: var(--primary);
  color: var(--primary);
}

/* ─────────────────────────────────────────────────────────────────────
   10. HEADER
───────────────────────────────────────────────────────────────────── */
.app-header {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  height: var(--header-height);
  background: var(--bg-surface);
  border-bottom: 1px solid var(--border-subtle);
  display: flex;
  align-items: center;
  gap: 16px;
  padding: 0 16px;
  z-index: var(--z-header);
  backdrop-filter: blur(16px);
  -webkit-backdrop-filter: blur(16px);
}

/* Logo */
.logo {
  display: flex;
  align-items: center;
  gap: 10px;
  text-decoration: none;
  flex-shrink: 0;
}

.logo-icon {
  width: 34px;
  height: 34px;
  background: linear-gradient(135deg, var(--primary), var(--secondary));
  border-radius: var(--radius-md);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 16px;
  color: #fff;
  box-shadow: 0 0 16px rgba(129, 140, 248, 0.4);
  flex-shrink: 0;
}

.logo-text {
  display: flex;
  flex-direction: column;
  line-height: 1.2;
}

.logo-title {
  font-size: 14px;
  font-weight: 800;
  letter-spacing: 2px;
  background: linear-gradient(90deg, var(--primary), var(--secondary));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.logo-sub {
  font-size: 9.5px;
  color: var(--text-muted);
  font-weight: 500;
  letter-spacing: 0.5px;
}

.logo-sub em {
  color: var(--primary);
  font-style: normal;
  font-weight: 700;
}

/* Header Center */
.header-center {
  display: flex;
  align-items: center;
  gap: 8px;
  flex: 1;
  justify-content: center;
}

.quick-action-btn {
  display: flex;
  align-items: center;
  gap: 7px;
  padding: 7px 14px;
  background: var(--bg-glass);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-full);
  color: var(--text-secondary);
  font-size: 12px;
  font-weight: 500;
  cursor: pointer;
  transition: all var(--transition-fast);
  white-space: nowrap;
  font-family: inherit;
}

.quick-action-btn:hover {
  background: var(--bg-hover);
  border-color: var(--primary);
  color: var(--primary);
}

.quick-action-btn.chaos {
  border-color: rgba(251, 191, 36, 0.3);
  color: var(--warning);
}

.quick-action-btn.chaos:hover {
  background: rgba(251, 191, 36, 0.1);
  border-color: var(--warning);
  box-shadow: 0 0 16px rgba(251, 191, 36, 0.2);
}

.quick-action-btn i { font-size: 13px; }

.header-separator {
  width: 1px;
  height: 24px;
  background: var(--border-subtle);
  flex-shrink: 0;
}

/* Header Actions */
.header-actions {
  display: flex;
  align-items: center;
  gap: 6px;
  flex-shrink: 0;
}

.header-btn {
  display: flex;
  align-items: center;
  gap: 6px;
  padding: 6px 10px;
  background: var(--bg-glass);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-sm);
  color: var(--text-secondary);
  font-size: 12px;
  font-weight: 500;
  cursor: pointer;
  transition: all var(--transition-fast);
  font-family: inherit;
  white-space: nowrap;
  position: relative;
}

.header-btn:hover {
  background: var(--bg-hover);
  border-color: var(--border-default);
  color: var(--text-primary);
}

.header-btn:disabled {
  opacity: 0.35;
  cursor: not-allowed;
}

.header-btn.icon-btn {
  width: 32px;
  height: 32px;
  padding: 0;
  justify-content: center;
}

.header-btn.icon-btn i { font-size: 14px; }

.header-btn.reset-btn {
  border-color: rgba(248, 113, 113, 0.3);
  color: var(--error);
}

.header-btn.reset-btn:hover {
  background: rgba(248, 113, 113, 0.1);
  border-color: var(--error);
}

.history-count {
  background: var(--primary);
  color: #fff;
  font-size: 9px;
  font-weight: 700;
  min-width: 16px;
  height: 16px;
  border-radius: var(--radius-full);
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 0 3px;
}

/* Preview Size Group */
.preview-size-group {
  display: flex;
  align-items: center;
  background: var(--bg-elevated);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-sm);
  padding: 2px;
  gap: 2px;
}

.preview-size-btn {
  width: 28px;
  height: 28px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: transparent;
  border: none;
  border-radius: 5px;
  color: var(--text-muted);
  font-size: 13px;
  cursor: pointer;
  transition: all var(--transition-fast);
}

.preview-size-btn.active,
.preview-size-btn:hover {
  background: var(--primary);
  color: #fff;
}

.theme-btn i { font-size: 14px; }

/* ─────────────────────────────────────────────────────────────────────
   11. SIDEBAR TOGGLE (MOBILE)
───────────────────────────────────────────────────────────────────── */
.sidebar-toggle {
  display: none;
  position: fixed;
  bottom: 20px;
  left: 20px;
  width: 52px;
  height: 52px;
  background: linear-gradient(135deg, var(--primary), var(--secondary));
  border: none;
  border-radius: var(--radius-full);
  color: #fff;
  font-size: 20px;
  cursor: pointer;
  z-index: calc(var(--z-sidebar) + 10);
  box-shadow: 0 4px 20px rgba(129, 140, 248, 0.5);
  align-items: center;
  justify-content: center;
  transition: all var(--transition-base);
}

.sidebar-toggle:hover {
  transform: scale(1.08);
}

.sidebar-overlay {
  display: none;
  position: fixed;
  inset: 0;
  background: rgba(0, 0, 0, 0.6);
  z-index: calc(var(--z-sidebar) - 1);
  backdrop-filter: blur(4px);
}

.sidebar-overlay.active {
  display: block;
}

/* ─────────────────────────────────────────────────────────────────────
   12. APP CONTAINER LAYOUT
───────────────────────────────────────────────────────────────────── */
.app-container {
  display: flex;
  height: calc(100vh - var(--header-height));
  margin-top: var(--header-height);
  overflow: hidden;
}

/* ─────────────────────────────────────────────────────────────────────
   13. SIDEBAR
───────────────────────────────────────────────────────────────────── */
.sidebar {
  width: var(--sidebar-width);
  min-width: var(--sidebar-width);
  height: 100%;
  background: var(--bg-surface);
  border-right: 1px solid var(--border-subtle);
  overflow-y: auto;
  overflow-x: hidden;
  flex-shrink: 0;
  display: flex;
  flex-direction: column;
  transition: transform var(--transition-base);
}

.sidebar-header {
  padding: 12px 14px;
  border-bottom: 1px solid var(--border-subtle);
  position: sticky;
  top: 0;
  background: var(--bg-surface);
  z-index: 10;
}

.sidebar-search {
  display: flex;
  align-items: center;
  gap: 8px;
  background: var(--bg-elevated);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-md);
  padding: 8px 12px;
  transition: border-color var(--transition-fast);
}

.sidebar-search:focus-within {
  border-color: var(--primary);
  box-shadow: 0 0 0 3px rgba(129, 140, 248, 0.1);
}

.sidebar-search i {
  color: var(--text-muted);
  font-size: 12px;
  flex-shrink: 0;
}

.sidebar-search input {
  flex: 1;
  background: transparent;
  border: none;
  outline: none;
  color: var(--text-primary);
  font-size: 12.5px;
  font-family: inherit;
}

.sidebar-search input::placeholder { color: var(--text-muted); }

.search-clear {
  width: 18px;
  height: 18px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: var(--bg-hover);
  border: none;
  border-radius: var(--radius-full);
  color: var(--text-muted);
  font-size: 10px;
  cursor: pointer;
}

/* ─────────────────────────────────────────────────────────────────────
   14. PANELS
───────────────────────────────────────────────────────────────────── */
.panel {
  border-bottom: 1px solid var(--border-subtle);
  overflow: hidden;
  transition: all var(--transition-base);
}

.panel-header {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 13px 14px;
  cursor: pointer;
  user-select: none;
  transition: background var(--transition-fast);
  position: relative;
}

.panel-header:hover {
  background: var(--bg-glass);
}

.panel-icon {
  width: 28px;
  height: 28px;
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 12px;
  flex-shrink: 0;
}

.panel-icon.text { background: rgba(129, 140, 248, 0.15); color: var(--primary); }
.panel-icon.bg { background: rgba(52, 211, 153, 0.15); color: var(--accent); }
.panel-icon.border { background: rgba(251, 191, 36, 0.15); color: var(--warning); }
.panel-icon.transform { background: rgba(244, 114, 182, 0.15); color: var(--secondary); }
.panel-icon.shadow { background: rgba(96, 165, 250, 0.15); color: var(--info); }
.panel-icon.anim { background: rgba(167, 139, 250, 0.15); color: #a78bfa; }
.panel-icon.clip { background: rgba(248, 113, 113, 0.15); color: var(--error); }
.panel-icon.transparent { background: rgba(52, 211, 153, 0.15); color: var(--accent); }
.panel-icon.palette { background: rgba(251, 191, 36, 0.15); color: var(--warning); }
.panel-icon.effects { background: rgba(129, 140, 248, 0.15); color: var(--primary); }
.panel-icon.layout { background: rgba(244, 114, 182, 0.15); color: var(--secondary); }

.panel-title {
  flex: 1;
  font-size: 12.5px;
  font-weight: 600;
  color: var(--text-primary);
  letter-spacing: 0.2px;
}

.panel-badge {
  font-size: 9px;
  font-weight: 700;
  padding: 2px 6px;
  background: linear-gradient(135deg, var(--primary), var(--secondary));
  color: #fff;
  border-radius: var(--radius-full);
  letter-spacing: 0.5px;
  text-transform: uppercase;
}

.badge-new {
  font-size: 9px;
  font-weight: 700;
  padding: 2px 6px;
  background: linear-gradient(135deg, var(--accent), #06b6d4);
  color: #fff;
  border-radius: var(--radius-full);
  letter-spacing: 0.3px;
  text-transform: uppercase;
  vertical-align: middle;
  margin-left: 4px;
}

.panel-toggle {
  font-size: 11px;
  color: var(--text-muted);
  transition: transform var(--transition-base);
  flex-shrink: 0;
}

.panel:not(.expanded) .panel-toggle {
  transform: rotate(180deg);
}

.panel-body {
  display: none;
  padding: 14px;
  flex-direction: column;
  gap: 14px;
}

.panel.expanded .panel-body {
  display: flex;
}

/* ─────────────────────────────────────────────────────────────────────
   15. FORM ELEMENTS
───────────────────────────────────────────────────────────────────── */
.form-group {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.form-group label {
  display: flex;
  align-items: center;
  gap: 6px;
  font-size: 11.5px;
  font-weight: 600;
  color: var(--text-secondary);
  text-transform: uppercase;
  letter-spacing: 0.4px;
}

.form-group label i {
  color: var(--primary);
  font-size: 11px;
  width: 14px;
  text-align: center;
}

.form-group label .value-badge {
  margin-left: auto;
  font-size: 11px;
  font-weight: 700;
  color: var(--primary);
  background: rgba(129, 140, 248, 0.1);
  padding: 1px 8px;
  border-radius: var(--radius-full);
  border: 1px solid rgba(129, 140, 248, 0.2);
  text-transform: none;
  letter-spacing: 0;
}

input[type="text"],
input[type="number"],
input[type="url"],
textarea,
select {
  width: 100%;
  padding: 8px 10px;
  background: var(--bg-elevated);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-sm);
  color: var(--text-primary);
  font-size: 12px;
  font-family: inherit;
  transition: all var(--transition-fast);
  outline: none;
  -webkit-appearance: none;
}

input[type="text"]:focus,
input[type="number"]:focus,
input[type="url"]:focus,
textarea:focus,
select:focus {
  border-color: var(--primary);
  box-shadow: 0 0 0 3px rgba(129, 140, 248, 0.1);
  background: var(--bg-hover);
}

select {
  cursor: pointer;
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='10' height='6' viewBox='0 0 10 6'%3E%3Cpath fill='%2394a3b8' d='M0 0l5 6 5-6z'/%3E%3C/svg%3E");
  background-repeat: no-repeat;
  background-position: right 8px center;
  padding-right: 26px;
}

select option {
  background: var(--bg-elevated);
  color: var(--text-primary);
}

textarea {
  resize: vertical;
  min-height: 90px;
  font-family: 'JetBrains Mono', 'Fira Code', monospace;
  font-size: 11px;
  line-height: 1.6;
}

input[type="range"] {
  -webkit-appearance: none;
  appearance: none;
  width: 100%;
  height: 4px;
  background: var(--bg-elevated);
  border-radius: var(--radius-full);
  border: none;
  outline: none;
  cursor: pointer;
}

input[type="range"]::-webkit-slider-thumb {
  -webkit-appearance: none;
  width: 16px;
  height: 16px;
  background: var(--primary);
  border-radius: var(--radius-full);
  border: 2px solid var(--bg-surface);
  box-shadow: 0 0 6px rgba(129, 140, 248, 0.5);
  cursor: grab;
  transition: all var(--transition-fast);
}

input[type="range"]::-webkit-slider-thumb:active {
  cursor: grabbing;
  transform: scale(1.15);
}

input[type="range"]::-moz-range-thumb {
  width: 16px;
  height: 16px;
  background: var(--primary);
  border-radius: var(--radius-full);
  border: 2px solid var(--bg-surface);
  cursor: grab;
}

input[type="color"] {
  -webkit-appearance: none;
  appearance: none;
  width: 32px;
  height: 32px;
  border: 1px solid var(--border-default);
  border-radius: var(--radius-sm);
  cursor: pointer;
  padding: 2px;
  background: var(--bg-elevated);
}

input[type="color"]::-webkit-color-swatch-wrapper { padding: 0; }
input[type="color"]::-webkit-color-swatch {
  border: none;
  border-radius: 4px;
}

input[type="checkbox"] {
  width: 14px;
  height: 14px;
  accent-color: var(--primary);
  cursor: pointer;
}

.form-row {
  display: flex;
  align-items: center;
  gap: 8px;
  flex-wrap: wrap;
}

.form-row label {
  font-size: 11px;
  color: var(--text-muted);
  white-space: nowrap;
  text-transform: none;
  letter-spacing: 0;
  font-weight: 500;
}

.form-row input,
.form-row select {
  flex: 1;
  min-width: 0;
}

.unit-label {
  font-size: 11px;
  color: var(--text-muted);
  flex-shrink: 0;
  font-weight: 600;
}

.separator {
  height: 1px;
  background: var(--border-subtle);
  margin: 2px 0;
}

.checkbox-row {
  display: flex;
  gap: 12px;
  flex-wrap: wrap;
}

.checkbox-row label {
  display: flex;
  align-items: center;
  gap: 5px;
  font-size: 11.5px;
  color: var(--text-secondary);
  cursor: pointer;
  text-transform: none;
  letter-spacing: 0;
  font-weight: 400;
}

/* ─────────────────────────────────────────────────────────────────────
   16. STYLE BUTTONS GRID
───────────────────────────────────────────────────────────────────── */
.btn-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 6px;
}

.style-btn {
  display: flex;
  align-items: center;
  gap: 6px;
  padding: 7px 10px;
  background: var(--bg-elevated);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-sm);
  color: var(--text-secondary);
  font-size: 11px;
  font-weight: 500;
  cursor: pointer;
  transition: all var(--transition-fast);
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  font-family: inherit;
}

.style-btn:hover {
  background: var(--bg-hover);
  border-color: var(--primary);
  color: var(--primary);
  transform: translateY(-1px);
  box-shadow: var(--shadow-sm);
}

.style-btn:active {
  transform: translateY(0);
}

.style-btn i {
  font-size: 12px;
  flex-shrink: 0;
  color: var(--primary);
}

.inline-btn {
  width: 24px;
  height: 24px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  background: var(--bg-elevated);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-sm);
  color: var(--text-secondary);
  font-size: 11px;
  cursor: pointer;
  transition: all var(--transition-fast);
  flex-shrink: 0;
  margin-left: auto;
}

.inline-btn:hover {
  background: var(--primary);
  border-color: var(--primary);
  color: #fff;
}

.add-color-btn {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 6px;
  padding: 8px;
  background: var(--bg-glass);
  border: 1px dashed var(--border-default);
  border-radius: var(--radius-sm);
  color: var(--text-muted);
  font-size: 11.5px;
  font-weight: 500;
  cursor: pointer;
  transition: all var(--transition-fast);
  width: 100%;
  font-family: inherit;
}

.add-color-btn:hover {
  border-color: var(--primary);
  color: var(--primary);
  background: rgba(129, 140, 248, 0.05);
}

/* ─────────────────────────────────────────────────────────────────────
   17. SUB TABS
───────────────────────────────────────────────────────────────────── */
.sub-tabs {
  display: flex;
  gap: 4px;
  background: var(--bg-elevated);
  border-radius: var(--radius-sm);
  padding: 3px;
  flex-wrap: wrap;
}

.sub-tab {
  flex: 1;
  padding: 6px 10px;
  background: transparent;
  border: none;
  border-radius: 5px;
  color: var(--text-muted);
  font-size: 11px;
  font-weight: 500;
  cursor: pointer;
  transition: all var(--transition-fast);
  white-space: nowrap;
  font-family: inherit;
}

.sub-tab.active,
.sub-tab:hover {
  background: var(--bg-surface);
  color: var(--primary);
  box-shadow: var(--shadow-sm);
}

.sub-tab.active {
  font-weight: 600;
}

.sub-tab-content {
  display: none;
}

.sub-tab-content.active {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

/* ─────────────────────────────────────────────────────────────────────
   18. COLOR PICKER
───────────────────────────────────────────────────────────────────── */
.color-picker-container {
  display: flex;
  justify-content: center;
  padding: 8px;
  background: var(--bg-elevated);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-md);
  overflow: hidden;
}

.color-picker-container .IroColorPicker {
  margin: 0 auto;
}

.color-hex-row {
  display: flex;
  align-items: center;
  gap: 8px;
}

.color-hex-row input {
  flex: 1;
  font-family: 'JetBrains Mono', monospace;
  font-size: 12px;
}

.color-swatch {
  width: 36px;
  height: 36px;
  border-radius: var(--radius-sm);
  border: 1px solid var(--border-default);
  flex-shrink: 0;
  cursor: pointer;
  transition: transform var(--transition-fast);
}

.color-swatch:hover {
  transform: scale(1.1);
}

/* ─────────────────────────────────────────────────────────────────────
   19. FONT PREVIEW
───────────────────────────────────────────────────────────────────── */
.font-preview-wrapper {
  display: flex;
  gap: 8px;
  align-items: center;
}

.font-preview-wrapper select {
  flex: 1;
}

.font-preview-text {
  width: 48px;
  height: 36px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: var(--bg-elevated);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-sm);
  font-size: 22px;
  color: var(--text-primary);
  flex-shrink: 0;
  transition: all var(--transition-base);
}

/* ─────────────────────────────────────────────────────────────────────
   20. ALIGN BUTTONS
───────────────────────────────────────────────────────────────────── */
.align-buttons {
  display: flex;
  gap: 4px;
  background: var(--bg-elevated);
  border-radius: var(--radius-sm);
  padding: 3px;
}

.align-btn {
  flex: 1;
  height: 32px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: transparent;
  border: none;
  border-radius: 5px;
  color: var(--text-muted);
  font-size: 13px;
  cursor: pointer;
  transition: all var(--transition-fast);
}

.align-btn.active,
.align-btn:hover {
  background: var(--bg-surface);
  color: var(--primary);
}

/* ─────────────────────────────────────────────────────────────────────
   21. PADDING GRID
───────────────────────────────────────────────────────────────────── */
.padding-grid {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  grid-template-rows: auto auto auto;
  gap: 6px;
  align-items: center;
}

.padding-side {
  display: flex;
  flex-direction: column;
  gap: 3px;
}

.padding-side label {
  font-size: 9.5px;
  color: var(--text-muted);
  text-align: center;
  text-transform: uppercase;
  letter-spacing: 0.3px;
}

.padding-side input {
  text-align: center;
  padding: 5px;
}

.padding-center {
  display: flex;
  align-items: center;
  justify-content: center;
  grid-column: 2;
  grid-row: 2;
}

/* ─────────────────────────────────────────────────────────────────────
   22. BORDER VISUAL GRID
───────────────────────────────────────────────────────────────────── */
.border-visual-grid {
  display: grid;
  grid-template-columns: 1fr 2fr 1fr;
  grid-template-rows: auto auto auto;
  gap: 6px;
  align-items: center;
  justify-items: center;
}

.border-visual-grid input {
  width: 100%;
  font-size: 10.5px;
  padding: 5px 6px;
}

.border-center-box {
  width: 40px;
  height: 40px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: var(--bg-elevated);
  border: 1px solid var(--border-default);
  border-radius: var(--radius-sm);
  color: var(--text-muted);
  font-size: 18px;
}

/* ─────────────────────────────────────────────────────────────────────
   23. CORNER GRID (BORDER RADIUS)
───────────────────────────────────────────────────────────────────── */
.corner-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  grid-template-rows: 1fr 1fr;
  gap: 6px;
  position: relative;
}

.corner-center {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 32px;
  height: 32px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--text-muted);
  font-size: 14px;
  background: var(--bg-elevated);
  border-radius: var(--radius-sm);
}

.corner-grid input {
  text-align: center;
  font-size: 11px;
  padding: 6px;
}

/* ─────────────────────────────────────────────────────────────────────
   24. TRANSFORM ORIGIN GRID
───────────────────────────────────────────────────────────────────── */
.transform-origin-grid,
.bg-position-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 4px;
}

.origin-btn,
.pos-btn {
  height: 32px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: var(--bg-elevated);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-sm);
  color: var(--text-muted);
  font-size: 14px;
  cursor: pointer;
  transition: all var(--transition-fast);
}

.origin-btn:hover,
.pos-btn:hover,
.origin-btn.active,
.pos-btn.active {
  background: var(--primary);
  border-color: var(--primary);
  color: #fff;
}

/* ─────────────────────────────────────────────────────────────────────
   25. SHADOW LAYERS
───────────────────────────────────────────────────────────────────── */
.shadow-layers-container {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.shadow-layer {
  background: var(--bg-elevated);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-md);
  overflow: hidden;
  transition: border-color var(--transition-fast);
}

.shadow-layer:hover {
  border-color: var(--border-default);
}

.shadow-layer-header {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 8px 10px;
  background: var(--bg-glass);
  border-bottom: 1px solid var(--border-subtle);
}

.shadow-toggle {
  display: flex !important;
  align-items: center;
  gap: 6px;
  font-size: 11.5px !important;
  font-weight: 500 !important;
  color: var(--text-secondary) !important;
  cursor: pointer;
  flex: 1;
  text-transform: none !important;
  letter-spacing: 0 !important;
}

.inset-toggle {
  display: flex;
  align-items: center;
  gap: 4px;
  font-size: 10.5px;
  color: var(--text-muted);
  cursor: pointer;
}

.remove-shadow-btn {
  width: 20px;
  height: 20px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: transparent;
  border: none;
  border-radius: var(--radius-sm);
  color: var(--text-muted);
  font-size: 11px;
  cursor: pointer;
  transition: all var(--transition-fast);
}

.remove-shadow-btn:hover {
  background: rgba(248, 113, 113, 0.1);
  color: var(--error);
}

.shadow-layer-inputs {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 6px;
  padding: 8px;
}

.shadow-input-group {
  display: flex;
  flex-direction: column;
  gap: 3px;
}

.shadow-input-group label {
  font-size: 9.5px !important;
  color: var(--text-muted) !important;
  text-align: center;
  text-transform: uppercase !important;
  letter-spacing: 0.3px;
  font-weight: 600 !important;
}

.shadow-input-group input {
  text-align: center;
  padding: 5px;
  font-size: 11px;
}

.shadow-color-group {
  grid-column: span 1;
}

.shadow-color-group input[type="color"] {
  width: 100%;
  height: 32px;
}

/* ─────────────────────────────────────────────────────────────────────
   26. GRADIENT COLOR ROWS
───────────────────────────────────────────────────────────────────── */
.gradient-colors {
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.gradient-color-row {
  display: flex;
  align-items: center;
  gap: 7px;
}

.gradient-color-row .color-dot {
  width: 30px;
  height: 30px;
  padding: 2px;
  flex-shrink: 0;
}

.gradient-color-row .hex-input {
  flex: 1;
  font-family: 'JetBrains Mono', monospace;
  font-size: 11px;
}

.gradient-color-row .stop-input {
  width: 54px;
  text-align: center;
}

.stop-label {
  font-size: 10px;
  color: var(--text-muted);
  font-weight: 600;
  flex-shrink: 0;
}

.gradient-color-row .remove-btn {
  width: 24px;
  height: 24px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: transparent;
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-sm);
  color: var(--text-muted);
  font-size: 10px;
  cursor: pointer;
  transition: all var(--transition-fast);
  flex-shrink: 0;
}

.gradient-color-row .remove-btn:hover:not(:disabled) {
  background: rgba(248, 113, 113, 0.1);
  border-color: var(--error);
  color: var(--error);
}

.gradient-color-row .remove-btn:disabled {
  opacity: 0.3;
  cursor: not-allowed;
}

.gradient-preview-bar {
  height: 10px;
  border-radius: var(--radius-full);
  border: 1px solid var(--border-subtle);
  margin-top: 4px;
  background: linear-gradient(90deg, #667eea, #764ba2);
}

/* ─────────────────────────────────────────────────────────────────────
   27. PATTERN GALLERY
───────────────────────────────────────────────────────────────────── */
.pattern-gallery {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 8px;
}

.pattern-item {
  height: 60px;
  border-radius: var(--radius-md);
  border: 2px solid var(--border-subtle);
  cursor: pointer;
  transition: all var(--transition-fast);
  position: relative;
  overflow: hidden;
  display: flex;
  align-items: flex-end;
}

.pattern-item span {
  font-size: 9.5px;
  font-weight: 600;
  color: #fff;
  background: rgba(0, 0, 0, 0.6);
  padding: 2px 6px;
  width: 100%;
  text-align: center;
  backdrop-filter: blur(2px);
}

.pattern-item:hover,
.pattern-item.active {
  border-color: var(--primary);
  transform: scale(1.02);
  box-shadow: 0 0 12px rgba(129, 140, 248, 0.3);
}

/* ─────────────────────────────────────────────────────────────────────
   28. CLIP SHAPE GALLERY
───────────────────────────────────────────────────────────────────── */
.clip-shape-gallery {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 6px;
}

.clip-shape-btn {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 4px;
  padding: 8px 4px;
  background: var(--bg-elevated);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-sm);
  color: var(--text-secondary);
  font-size: 9px;
  cursor: pointer;
  transition: all var(--transition-fast);
  font-family: inherit;
}

.clip-shape-btn:hover,
.clip-shape-btn.active {
  background: rgba(129, 140, 248, 0.1);
  border-color: var(--primary);
  color: var(--primary);
}

.clip-preview {
  font-size: 18px;
  line-height: 1;
}

/* ─────────────────────────────────────────────────────────────────────
   29. ANIMATION GRID
───────────────────────────────────────────────────────────────────── */
.animation-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 6px;
}

.anim-btn {
  padding: 7px 8px;
  background: var(--bg-elevated);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-sm);
  color: var(--text-secondary);
  font-size: 11px;
  font-weight: 500;
  cursor: pointer;
  transition: all var(--transition-fast);
  text-align: left;
  font-family: inherit;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.anim-btn:hover,
.anim-btn.active {
  background: rgba(129, 140, 248, 0.1);
  border-color: var(--primary);
  color: var(--primary);
}

.anim-btn.active {
  font-weight: 700;
}

/* ─────────────────────────────────────────────────────────────────────
   30. TOGGLE GROUP
───────────────────────────────────────────────────────────────────── */
.toggle-group {
  display: flex;
  gap: 6px;
}

.toggle-btn {
  flex: 1;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 6px;
  padding: 8px;
  background: var(--bg-elevated);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-sm);
  color: var(--text-secondary);
  font-size: 11.5px;
  font-weight: 500;
  cursor: pointer;
  transition: all var(--transition-fast);
  font-family: inherit;
}

.toggle-btn.active,
.toggle-btn:hover {
  background: rgba(129, 140, 248, 0.1);
  border-color: var(--primary);
  color: var(--primary);
}

.toggle-btn.active {
  font-weight: 600;
}

/* ─────────────────────────────────────────────────────────────────────
   31. PALETTE PREVIEW
───────────────────────────────────────────────────────────────────── */
.palette-preview {
  display: flex;
  gap: 4px;
  height: 56px;
  border-radius: var(--radius-md);
  overflow: hidden;
  border: 1px solid var(--border-subtle);
}

.palette-swatch {
  flex: 1;
  cursor: pointer;
  transition: all var(--transition-fast);
  display: flex;
  align-items: flex-end;
  justify-content: center;
  padding-bottom: 3px;
  position: relative;
  overflow: hidden;
}

.palette-swatch:hover {
  flex: 2;
}

.palette-hex {
  font-size: 8px;
  font-weight: 700;
  color: rgba(255, 255, 255, 0.9);
  background: rgba(0, 0, 0, 0.4);
  padding: 1px 3px;
  border-radius: 2px;
  opacity: 0;
  transition: opacity var(--transition-fast);
  white-space: nowrap;
}

.palette-swatch:hover .palette-hex {
  opacity: 1;
}

/* ─────────────────────────────────────────────────────────────────────
   32. BOX MODEL VISUAL
───────────────────────────────────────────────────────────────────── */
.box-model-visual {
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-md);
  padding: 10px;
  background: var(--bg-elevated);
  position: relative;
}

.bm-margin-label,
.bm-padding-label {
  font-size: 9px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 1px;
  color: var(--text-muted);
  text-align: center;
  margin-bottom: 4px;
}

.bm-margin {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 4px;
  border: 1px dashed rgba(251, 191, 36, 0.3);
  border-radius: var(--radius-sm);
  padding: 6px;
  background: rgba(251, 191, 36, 0.03);
}

.bm-inner-row {
  display: flex;
  align-items: center;
  gap: 4px;
  width: 100%;
}

.bm-content {
  flex: 1;
  min-height: 40px;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 4px;
  background: rgba(129, 140, 248, 0.1);
  border: 1px solid rgba(129, 140, 248, 0.3);
  border-radius: var(--radius-sm);
  font-size: 11px;
  color: var(--primary);
  font-weight: 600;
}

.bm-content i {
  font-size: 9px;
  color: var(--text-muted);
}

.bm-margin input {
  width: 50px;
  text-align: center;
  padding: 4px;
  font-size: 11px;
}

.bm-unit-row {
  display: flex;
  justify-content: center;
  margin-top: 4px;
}

.bm-unit-row select {
  width: 70px;
  padding: 4px 8px;
  font-size: 11px;
}

/* ─────────────────────────────────────────────────────────────────────
   33. MAIN CONTENT AREA
───────────────────────────────────────────────────────────────────── */
.main-content {
  flex: 1;
  display: flex;
  flex-direction: column;
  overflow: hidden;
  background: var(--bg-base);
}

/* ─────────────────────────────────────────────────────────────────────
   34. PREVIEW SECTION
───────────────────────────────────────────────────────────────────── */
.preview-section {
  flex: 1;
  display: flex;
  flex-direction: column;
  overflow: hidden;
  border-bottom: 1px solid var(--border-subtle);
}

.preview-toolbar {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 8px 14px;
  background: var(--bg-surface);
  border-bottom: 1px solid var(--border-subtle);
  flex-shrink: 0;
  flex-wrap: wrap;
}

.preview-toolbar-left {
  display: flex;
  align-items: center;
  gap: 6px;
  flex: 1;
  min-width: 200px;
}

.preview-toolbar-right {
  display: flex;
  align-items: center;
  gap: 6px;
}

.preview-label {
  font-size: 11px;
  font-weight: 600;
  color: var(--text-muted);
  text-transform: uppercase;
  letter-spacing: 0.5px;
  flex-shrink: 0;
}

.preview-text-input {
  flex: 1;
  padding: 6px 10px;
  background: var(--bg-elevated);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-sm);
  color: var(--text-primary);
  font-size: 12px;
  min-width: 0;
}

.preview-text-input:focus {
  border-color: var(--primary);
  outline: none;
}

.char-count {
  font-size: 10px;
  color: var(--text-muted);
  white-space: nowrap;
}

.preview-control-btn {
  width: 30px;
  height: 30px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: var(--bg-elevated);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-sm);
  color: var(--text-secondary);
  font-size: 12px;
  cursor: pointer;
  transition: all var(--transition-fast);
}

.preview-control-btn:hover,
.preview-control-btn.active {
  background: var(--bg-hover);
  border-color: var(--primary);
  color: var(--primary);
}

#previewDimensions {
  font-size: 10px;
  color: var(--text-muted);
  font-family: 'JetBrains Mono', monospace;
  padding: 2px 8px;
  background: var(--bg-elevated);
  border-radius: var(--radius-full);
  border: 1px solid var(--border-subtle);
}

.preview-container {
  flex: 1;
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
  padding: 20px;
  background:
    radial-gradient(circle at 50% 50%, rgba(129, 140, 248, 0.03) 0%, transparent 70%),
    repeating-linear-gradient(0deg, transparent, transparent 24px, var(--border-subtle) 24px, var(--border-subtle) 25px),
    repeating-linear-gradient(90deg, transparent, transparent 24px, var(--border-subtle) 24px, var(--border-subtle) 25px);
  background-color: var(--bg-base);
  position: relative;
}

.preview-container.preview-bg-light {
  background-color: #ffffff;
}

.preview-container.grid-overlay::after {
  content: '';
  position: absolute;
  inset: 0;
  background-image:
    linear-gradient(rgba(129, 140, 248, 0.15) 1px, transparent 1px),
    linear-gradient(90deg, rgba(129, 140, 248, 0.15) 1px, transparent 1px);
  background-size: 40px 40px;
  pointer-events: none;
}

.preview-frame {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 100%;
  max-width: 100%;
  transition: max-width var(--transition-base);
  position: relative;
}

#preview-box {
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 120px;
  min-width: 200px;
  padding: 20px 30px;
  word-break: break-word;
  overflow-wrap: break-word;
  cursor: default;
  transition: all 0.3s ease;
}

/* Ruler */
.ruler-h,
.ruler-v {
  position: absolute;
  background: rgba(129, 140, 248, 0.1);
  z-index: 5;
  pointer-events: none;
}

.ruler-h {
  top: 0;
  left: 0;
  right: 0;
  height: 20px;
}

.ruler-v {
  top: 0;
  left: 0;
  bottom: 0;
  width: 20px;
}

.ruler-mark {
  position: absolute;
  font-size: 8px;
  color: var(--text-muted);
  font-family: monospace;
}

/* ─────────────────────────────────────────────────────────────────────
   35. OUTPUT SECTION
───────────────────────────────────────────────────────────────────── */
.output-section {
  height: 300px;
  flex-shrink: 0;
  display: flex;
  flex-direction: column;
  overflow: hidden;
  background: var(--bg-surface);
  border-top: 1px solid var(--border-subtle);
  resize: vertical;
  min-height: 200px;
  max-height: 50vh;
}

.output-tabs {
  display: flex;
  gap: 2px;
  padding: 8px 12px 0;
  border-bottom: 1px solid var(--border-subtle);
  background: var(--bg-elevated);
  flex-shrink: 0;
  overflow-x: auto;
}

.output-tab {
  padding: 7px 14px;
  background: transparent;
  border: none;
  border-bottom: 2px solid transparent;
  color: var(--text-muted);
  font-size: 11.5px;
  font-weight: 500;
  cursor: pointer;
  transition: all var(--transition-fast);
  white-space: nowrap;
  font-family: inherit;
  display: flex;
  align-items: center;
  gap: 6px;
}

.output-tab:hover {
  color: var(--text-primary);
}

.output-tab.active {
  color: var(--primary);
  border-bottom-color: var(--primary);
  font-weight: 600;
}

.output-tab i {
  font-size: 12px;
}

.output-card {
  flex: 1;
  overflow: hidden;
  display: none;
  flex-direction: column;
}

.output-card.active {
  display: flex;
}

.output-card-header {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 8px 12px;
  border-bottom: 1px solid var(--border-subtle);
  flex-shrink: 0;
}

.output-card-title {
  font-size: 11px;
  font-weight: 600;
  color: var(--text-secondary);
  text-transform: uppercase;
  letter-spacing: 0.5px;
  flex: 1;
}

.output-card-actions {
  display: flex;
  gap: 6px;
  align-items: center;
}

.output-btn {
  display: flex;
  align-items: center;
  gap: 6px;
  padding: 6px 12px;
  border-radius: var(--radius-sm);
  font-size: 11.5px;
  font-weight: 500;
  cursor: pointer;
  transition: all var(--transition-fast);
  border: 1px solid transparent;
  font-family: inherit;
}

.output-btn.primary {
  background: var(--primary);
  color: #fff;
  border-color: var(--primary);
}

.output-btn.primary:hover {
  background: var(--primary-dark);
  box-shadow: 0 0 12px rgba(129, 140, 248, 0.4);
}

.output-btn.secondary {
  background: var(--bg-elevated);
  color: var(--text-secondary);
  border-color: var(--border-subtle);
}

.output-btn.secondary:hover {
  background: var(--bg-hover);
  border-color: var(--border-default);
  color: var(--text-primary);
}

.output-btn.success-state {
  background: var(--success) !important;
  border-color: var(--success) !important;
}

.output-btn.error-state {
  background: var(--error) !important;
  border-color: var(--error) !important;
}

#css-output,
#json-output {
  flex: 1;
  resize: none;
  border: none;
  background: var(--bg-elevated);
  color: var(--primary-light);
  font-family: 'JetBrains Mono', 'Fira Code', 'Courier New', monospace;
  font-size: 12px;
  line-height: 1.7;
  padding: 14px 16px;
  outline: none;
  border-radius: 0;
}

#json-output {
  color: var(--accent);
}

.css-line-count {
  font-size: 10px;
  color: var(--text-muted);
  padding: 2px 8px;
  background: var(--bg-elevated);
  border-radius: var(--radius-full);
  border: 1px solid var(--border-subtle);
  font-family: monospace;
}

#htmlPreviewArea,
#tailwindOutput {
  flex: 1;
  overflow-y: auto;
  padding: 12px;
  background: var(--bg-elevated);
}

#htmlPreviewArea pre,
#tailwindOutput pre {
  font-family: 'JetBrains Mono', monospace;
  font-size: 11.5px;
  line-height: 1.7;
  color: var(--text-secondary);
  white-space: pre-wrap;
  word-break: break-all;
}

#htmlPreviewArea code { color: #a78bfa; }
#tailwindOutput code { color: var(--accent); }

.copy-feedback {
  display: none;
  align-items: center;
  gap: 5px;
  font-size: 11px;
  font-weight: 600;
  padding: 4px 10px;
  border-radius: var(--radius-sm);
}

.copy-feedback.success { color: var(--success); }
.copy-feedback.error { color: var(--error); }

/* ─────────────────────────────────────────────────────────────────────
   36. RIGHT PANEL (SECOND SIDEBAR)
───────────────────────────────────────────────────────────────────── */
.right-panel {
  width: 300px;
  min-width: 300px;
  height: 100%;
  background: var(--bg-surface);
  border-left: 1px solid var(--border-subtle);
  overflow-y: auto;
  flex-shrink: 0;
  display: flex;
  flex-direction: column;
}

.right-panel-section {
  border-bottom: 1px solid var(--border-subtle);
}

.right-panel-header {
  padding: 12px 14px;
  font-size: 11px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.8px;
  color: var(--text-muted);
  display: flex;
  align-items: center;
  gap: 8px;
  cursor: pointer;
  user-select: none;
}

.right-panel-header i {
  color: var(--primary);
  font-size: 12px;
}

.right-panel-body {
  padding: 12px 14px;
  display: flex;
  flex-direction: column;
  gap: 10px;
}

/* ─────────────────────────────────────────────────────────────────────
   37. PRESET CARDS / THEMES
───────────────────────────────────────────────────────────────────── */
.preset-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 8px;
}

.preset-card {
  position: relative;
  height: 80px;
  border-radius: var(--radius-md);
  border: 2px solid var(--border-subtle);
  cursor: pointer;
  overflow: hidden;
  transition: all var(--transition-base);
  display: flex;
  align-items: center;
  justify-content: center;
}

.preset-card:hover {
  border-color: var(--primary);
  transform: translateY(-2px);
  box-shadow: var(--shadow-md), 0 0 16px rgba(129, 140, 248, 0.2);
}

.preset-card-name {
  font-size: 10px;
  font-weight: 700;
  text-align: center;
  padding: 0 6px;
  text-shadow: 0 1px 4px rgba(0, 0, 0, 0.5);
  line-height: 1.3;
  z-index: 1;
}

.preset-card-overlay {
  position: absolute;
  inset: 0;
  background: linear-gradient(to top, rgba(0, 0, 0, 0.5), transparent);
  transition: opacity var(--transition-fast);
}

.preset-card:hover .preset-card-overlay {
  opacity: 0.7;
}

/* ─────────────────────────────────────────────────────────────────────
   38. HISTORY TIMELINE
───────────────────────────────────────────────────────────────────── */
.history-timeline {
  display: flex;
  gap: 4px;
  flex-wrap: wrap;
  padding: 8px;
  background: var(--bg-elevated);
  border-radius: var(--radius-md);
  min-height: 40px;
  border: 1px solid var(--border-subtle);
}

.history-item {
  display: flex;
  align-items: center;
  gap: 4px;
  padding: 4px 8px;
  background: var(--bg-glass);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-sm);
  font-size: 10px;
  color: var(--text-muted);
  cursor: pointer;
  transition: all var(--transition-fast);
}

.history-item:hover {
  background: var(--bg-hover);
  color: var(--text-primary);
}

.history-item.active {
  background: rgba(129, 140, 248, 0.15);
  border-color: var(--primary);
  color: var(--primary);
  font-weight: 600;
}

/* ─────────────────────────────────────────────────────────────────────
   39. CUSTOM CSS EDITOR
───────────────────────────────────────────────────────────────────── */
.css-editor-wrapper {
  position: relative;
}

#cssInputArea {
  width: 100%;
  min-height: 140px;
  font-family: 'JetBrains Mono', monospace;
  font-size: 11.5px;
  line-height: 1.7;
  background: var(--bg-elevated);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-md);
  color: var(--text-primary);
  padding: 12px;
  resize: vertical;
}

.css-editor-actions {
  display: flex;
  gap: 6px;
  margin-top: 6px;
  flex-wrap: wrap;
}

/* ─────────────────────────────────────────────────────────────────────
   40. PSEUDO ELEMENT EDITOR
───────────────────────────────────────────────────────────────────── */
.pseudo-editor {
  display: flex;
  flex-direction: column;
  gap: 14px;
}

.pseudo-section {
  background: var(--bg-elevated);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-md);
  padding: 12px;
}

.pseudo-section-title {
  font-size: 11px;
  font-weight: 700;
  color: var(--primary);
  margin-bottom: 10px;
  display: flex;
  align-items: center;
  gap: 6px;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.pseudo-section-title::before {
  content: '::';
  font-family: monospace;
  color: var(--secondary);
}

/* ─────────────────────────────────────────────────────────────────────
   41. CHAOS CONTROLS
───────────────────────────────────────────────────────────────────── */
.chaos-controls {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.chaos-categories {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 6px;
}

.chaos-category {
  display: flex;
  align-items: center;
  gap: 6px;
  padding: 6px 8px;
  background: var(--bg-elevated);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-sm);
  cursor: pointer;
  transition: all var(--transition-fast);
}

.chaos-category:hover {
  border-color: var(--primary);
  background: rgba(129, 140, 248, 0.05);
}

.chaos-category label {
  font-size: 11px;
  color: var(--text-secondary);
  cursor: pointer;
  text-transform: none !important;
  letter-spacing: 0 !important;
  font-weight: 400 !important;
}

.chaos-actions {
  display: flex;
  gap: 6px;
}

.auto-play-controls {
  display: flex;
  align-items: center;
  gap: 8px;
  flex-wrap: wrap;
}

.auto-play-controls input[type="number"] {
  width: 60px;
}

/* ─────────────────────────────────────────────────────────────────────
   42. THEME SEARCH
───────────────────────────────────────────────────────────────────── */
.theme-search-wrapper {
  position: relative;
  margin-bottom: 10px;
}

.theme-search-wrapper i {
  position: absolute;
  left: 10px;
  top: 50%;
  transform: translateY(-50%);
  color: var(--text-muted);
  font-size: 12px;
  pointer-events: none;
}

#themeSearch {
  padding-left: 30px;
}

/* ─────────────────────────────────────────────────────────────────────
   43. RESPONSIVE
───────────────────────────────────────────────────────────────────── */
@media (max-width: 1200px) {
  .right-panel {
    display: none;
  }
}

@media (max-width: 900px) {
  :root {
    --sidebar-width: 300px;
  }

  .header-center {
    display: none;
  }

  .logo-text { display: none; }

  .sidebar {
    position: fixed;
    top: var(--header-height);
    left: 0;
    height: calc(100vh - var(--header-height));
    z-index: var(--z-sidebar);
    transform: translateX(-100%);
    box-shadow: var(--shadow-lg);
  }

  .sidebar.open {
    transform: translateX(0);
  }

  .sidebar-toggle {
    display: flex;
  }

  .main-content {
    width: 100%;
  }
}

@media (max-width: 600px) {
  :root {
    --header-height: 52px;
  }

  .header-actions {
    gap: 4px;
  }

  .header-btn span { display: none; }

  .preview-toolbar {
    gap: 6px;
    padding: 6px 10px;
  }

  .output-section {
    height: 250px;
  }

  .shortcut-grid {
    grid-template-columns: 1fr;
  }

  .preset-grid {
    grid-template-columns: repeat(2, 1fr);
  }

  .toast-container {
    right: 12px;
    bottom: 80px;
    left: 12px;
  }

  .toast {
    max-width: 100%;
  }
}

/* ─────────────────────────────────────────────────────────────────────
   44. ANIMATIONS (APP UI)
───────────────────────────────────────────────────────────────────── */
@keyframes pulse-ring {
  0% { transform: scale(1); opacity: 0.8; }
  100% { transform: scale(1.5); opacity: 0; }
}

@keyframes spin {
  from { transform: rotate(0deg); }
  to { transform: rotate(360deg); }
}

@keyframes fadeInUp {
  from { opacity: 0; transform: translateY(16px); }
  to { opacity: 1; transform: translateY(0); }
}

@keyframes shimmer {
  0% { background-position: -200% 0; }
  100% { background-position: 200% 0; }
}

.loading-shimmer {
  background: linear-gradient(90deg, var(--bg-elevated) 0%, var(--bg-hover) 50%, var(--bg-elevated) 100%);
  background-size: 200% 100%;
  animation: shimmer 1.5s infinite;
}

/* ─────────────────────────────────────────────────────────────────────
   45. UTILITY CLASSES
───────────────────────────────────────────────────────────────────── */
.hidden { display: none !important; }
.sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  white-space: nowrap;
  border-width: 0;
}

.text-primary { color: var(--text-primary); }
.text-secondary { color: var(--text-secondary); }
.text-muted { color: var(--text-muted); }
.text-accent { color: var(--primary); }

.fw-400 { font-weight: 400; }
.fw-600 { font-weight: 600; }
.fw-700 { font-weight: 700; }

.gap-4 { gap: 4px; }
.gap-8 { gap: 8px; }
.gap-12 { gap: 12px; }
.gap-16 { gap: 16px; }

.flex { display: flex; }
.flex-col { flex-direction: column; }
.items-center { align-items: center; }
.justify-center { justify-content: center; }
.flex-1 { flex: 1; }
.w-full { width: 100%; }

.mt-4 { margin-top: 4px; }
.mt-8 { margin-top: 8px; }
.mt-12 { margin-top: 12px; }

/* ─────────────────────────────────────────────────────────────────────
   46. FOCUS VISIBLE (ACCESSIBILITY)
───────────────────────────────────────────────────────────────────── */
:focus-visible {
  outline: 2px solid var(--primary);
  outline-offset: 2px;
  border-radius: 4px;
}

button:focus-visible,
a:focus-visible,
input:focus-visible,
select:focus-visible,
textarea:focus-visible {
  outline: 2px solid var(--primary);
  outline-offset: 2px;
}

/* ─────────────────────────────────────────────────────────────────────
   47. PRINT STYLES
───────────────────────────────────────────────────────────────────── */
@media print {
  .sidebar,
  .app-header,
  .preview-toolbar,
  .output-section,
  .right-panel,
  .sidebar-toggle,
  .toast-container {
    display: none !important;
  }

  .main-content {
    margin: 0;
    height: auto;
  }

  .preview-container {
    height: 100vh;
  }
}

/* ─────────────────────────────────────────────────────────────────────
   48. PREFERS REDUCED MOTION
───────────────────────────────────────────────────────────────────── */
@media (prefers-reduced-motion: reduce) {
  *,
  *::before,
  *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
    scroll-behavior: auto !important;
  }
}
```

Bu `style.css` dosyası **tüm** component'leri kapsar. `script.js` ile tam uyumlu çalışır. İkisini aynı klasöre koy, `index.html` ile birlikte çalıştır! 🚀
