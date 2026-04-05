# Android klavye tasarımı ve geliştirme

## Prompt 1

### You
*2026-01-27 03:48:02 +03*

andoid  klayye  yapmak ıstıyoru bır cok ozekık ekleyıp gelsırmek ıstıyoru sesle yazamnın daha on planda oldugu bazı aracakrın fnskıyonarın calsıtıgı maxımum   once klavye tasarlayalım 

### Dart Frog 0120
*2026-01-27 03:48:03 +03*

### Android Klavye (Input Method) Tasarımı – Adım Adım Kılavuz  

Aşağıda **temel bir Android klavyesi** oluşturup **birçok özel işlevi** (özellikle **sesli yazma**) ekleyebileceğiniz, performans odaklı bir yol haritası ve örnek kodlar bulacaksınız. İstediğiniz özellikleri adım adım ekleyebilirsiniz.

---

## 1. Proje Yapısı ve Gerekli Ayarlar  

| Klasör / Dosya | Açıklama |
|----------------|----------|
| `app/manifests/AndroidManifest.xml` | `InputMethodService` için izin ve bildirim |
| `app/src/main/res/xml/method.xml` | Klavyenin ayarlar aktivitesini tanımlar |
| `app/src/main/res/xml/keyboard_layout.xml` | Tuş düzenini (satır, tuşlar) tanımlar |
| `app/src/main/res/layout/keyboard_view.xml` | Klavye UI’sini barındıran layout |
| `app/src/main/res/layout/candidate_view.xml` | Öneri (tahmin) satırı |
| `app/src/main/java/com.example.keyboard/MyInputMethodService.kt` | Ana servis – tuş işleme, sesli yazma vb. |
| `app/src/main/java/com.example.keyboard/SettingsActivity.kt` | Kullanıcı tercihlerini saklamak için basit bir ayar ekranı |
| `app/src/main/java/com.example.keyboard/VoiceRecognizerHelper.kt` | `SpeechRecognizer` sarıcı sınıfı |
| `app/src/main/res/values/strings.xml` | Metinler ve etiketler |
| `app/src/main/res/values/styles.xml` | Tema (karanlık/aydınlık, renkler) |

> **Not:** Projenizi **Kotlin** ile başlatmanızı öneririm (Java da aynı mantık çalışır). Minimum SDK’si **API 21** (Android 5.0) olarak ayarlayabilirsiniz; sesli yazma için `RECORD_AUDIO` izni gereklidir.

### AndroidManifest.xml Örneği  

```xml
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="com.example.keyboard">

    <uses-permission android:name="android.permission.RECORD_AUDIO"/>
    <!-- Gerekirse diğer izinler (INTERNET vb.) -->

    <application
        android:allowBackup="true"
        android:label="@string/app_name"
        android:theme="@style/AppTheme">

        <!-- Klavye servisi -->
        <service
            android:name=".MyInputMethodService"
            android:label="@string/keyboard_name"
            android:permission="android.permission.BIND_INPUT_METHOD">
            <intent-filter>
                <action android:name="android.view.InputMethod" />
            </intent-filter>
            <meta-data
                android:name="android.view.im"
                android:resource="@xml/method" />
        </service>

        <!-- Ayar aktivitesi -->
        <activity
            android:name=".SettingsActivity"
            android:label="@string/settings_title"
            android:exported="false" />
    </application>
</manifest>
```

### method.xml  

```xml
<input-method xmlns:android="http://schemas.android.com/apk/res/android"
    android:settingsActivity="com.example.keyboard.SettingsActivity"/>
```

---

## 2. Klavye Görsel Tasarımı  

### 2.1 Tuş Düzeni (XML) – `keyboard_layout.xml`

```xml
<Keyboard xmlns:android="http://schemas.android.com/apk/res/android"
    android:keyWidth="10%p"
    android:keyHeight="60dp"
    android:horizontalGap="2dp"
    android:verticalGap="2dp">

    <!-- 1. Satır: Sayılar ve Sembolü -->
    <Row android:rowEdgeFlags="top">
        <Key android:codes="49" android:label="1" android:keyEdgeFlags="left"/>
        <Key android:codes="50" android:label="2"/>
        <Key android:codes="51" android:label="3"/>
        <Key android:codes="52" android:label="4"/>
        <Key android:codes="53" android:label="5"/>
        <Key android:codes="54" android:label="6"/>
        <Key android:codes="55" android:label="7"/>
        <Key android:codes="56" android:label="8"/>
        <Key android:codes="57" android:label="9"/>
        <Key android:codes="48" android:label="0" android:keyEdgeFlags="right"/>
    </Row>

    <!-- 2. Satır: Harfler -->
    <Row>
        <Key android:codes="113" android:label="q" android:keyEdgeFlags="left"/>
        <Key android:codes="119" android:label="w"/>
        <Key android:codes="101" android:label="e"/>
        <Key android:codes="114" android:label="r"/>
        <Key android:codes="116" android:label="t"/>
        <Key android:codes="121" android:label="y"/>
        <Key android:codes="117" android:label="u"/>
        <Key android:codes="105" android:label="i"/>
        <Key android:codes="111" android:label="o"/>
        <Key android:codes="112" android:label="p" android:keyEdgeFlags="right"/>
    </Row>

    <!-- 3. Satır: Harfler -->
    <Row>
        <Key android:codes="97" android:label="a" android:keyEdgeFlags="left"/>
        <Key android:codes="115" android:label="s"/>
        <Key android:codes="100" android:label="d"/>
        <Key android:codes="102" android:label="f"/>
        <Key android:codes="103" android:label="g"/>
        <Key android:codes="104" android:label="h"/>
        <Key android:codes="106" android:label="j"/>
        <Key android:codes="107" android:label="k"/>
        <Key android:codes="108" android:label="l" android:keyEdgeFlags="right"/>
    </Row>

    <!-- 4. Satır: Boşluk, mikrofon, geri al, enter -->
    <Row android:rowEdgeFlags="bottom">
        <Key
            android:keyWidth="15%p"
            android:codes="32"
            android:label=" "
            android:keyEdgeFlags="left"/>
        <Key
            android:keyWidth="15%p"
            android:codes="${KEY_VOICE}"
            android:label="@drawable/ic_mic"
            android:isRepeatable="true"/>
        <Key
            android:keyWidth="15%p"
            android:codes="${KEY_BACKSPACE}"
            android:label="@drawable/ic_backspace"
            android:isRepeatable="true"/>
        <Key
            android:keyWidth="55%p"
            android:codes="13"
            android:label="↵"
            android:keyEdgeFlags="right"/>
    </Row>
</Keyboard>
```

> **Önemli:**  
> * `@drawable/ic_mic` ve `@drawable/ic_backspace` gibi vektör drawabler’i projenize ekleyin.  
> * `${KEY_VOICE}` ve `${KEY_BACKSPACE}` yerine `MyInputMethodService` içinde tanımladığınız sabitleri kullanacaksınız (ör. `KEY_VOICE = -1`).

### 2.2 Klavye Görünümü – `keyboard_view.xml`

```xml
<?xml version="1.0" encoding="utf-8"?>
<android.inputmethodservice.KeyboardView
    xmlns:android="http://schemas.android.com/apk/res/android"
    android:id="@+id/keyboard_view"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    android:keyPreviewLayout="@layout/key_preview"
    android:keyBackground="@drawable/key_background"
    android:shadowRadius="0"
    android:paddingTop="5dp"
    android:paddingBottom="5dp"/>
```

* `key_preview` ve `key_background` drawabler’leri ile tuş basma animasyonlarını özelleştirebilirsiniz.

### 2.3 Öneri Satırı – `candidate_view.xml`

```xml
<?xml version="1.0" encoding="utf-8"?>
<androidx.recyclerview.widget.RecyclerView
    xmlns:android="http://schemas.android.com/apk/res/android"
    android:id="@+id/candidate_recycler"
    android:layout_width="match_parent"
    android:layout_height="40dp"
    android:orientation="horizontal"
    android:scrollbars="horizontal"
    android:overScrollMode="never"/>
```

---

## 3. Temel İşlevsellik – `MyInputMethodService.kt`

Aşağıdaki kod, **tuş basma**, **metin girme**, **geri al**, **sesli yazma** ve **öneri** işlevlerini içerir.

```kotlin
package com.example.keyboard

import android.inputmethodservice.InputMethodService
import android.inputmethodservice.Keyboard
import android.inputmethodservice.KeyboardView
import android.view.KeyEvent
import android.view.View
import android.view.inputmethod.EditorInfo
import android.view.inputmethod.InputConnection
import androidx.recyclerview.widget.LinearLayoutManager
import androidx.recyclerview.widget.RecyclerView

class MyInputMethodService : InputMethodService() {

    companion object {
        const val KEY_VOICE = -10   // Mikrofon tuşu için özel kod
        const val KEY_BACKSPACE = -1
        const val KEY_SPACE = 32
        const val KEY_ENTER = 13
    }

    private lateinit var keyboardView: KeyboardView
    private lateinit var candidateRecycler: RecyclerView
    private lateinit var keyboard: Keyboard
    private var voiceHelper: VoiceRecognizerHelper? = null

    override fun onCreateInputView(): View {
        // Klavye layout'ını inflate eder
        val layout = layoutInflater.inflate(R.layout.keyboard_view, null)

        keyboardView = layout.findViewById(R.id.keyboard_view)
        candidateRecycler = layout.findViewById(R.id.candidate_recycler)

        // Öneri satırını hazırla
        candidateRecycler.layoutManager = LinearLayoutManager(this, LinearLayoutManager.HORIZONTAL, false)
        // Örnek bir adaptör (daha sonra doldurulacak)
        // candidateRecycler.adapter = CandidateAdapter(mutableListOf())

        // Klavye düzenini yükle
        keyboard = Keyboard(this, R.xml.keyboard_layout)

        keyboardView.keyboard = keyboard
        keyboardView.setOnKeyboardActionListener(keyboardListener)

        // Mikrofon tuşuna basıldığında sesli yazma başlat
        voiceHelper = VoiceRecognizerHelper(this) { transcript ->
            // Sesli yazı sonucu geldiğinde metne ekle
            val ic = currentInputConnection
            ic?.commitText(transcript, 1)
        }

        return layout
    }

    private val keyboardListener = object : KeyboardView.OnKeyboardActionListener {
        override fun onKey(code: Int) {
            val ic: InputConnection? = currentInputConnection
            if (ic == null) return

            when (code) {
                KEY_BACKSPACE -> {
                    // Geri al (silme)
                    ic.deleteSurroundingText(1, 0)
                }
                KEY_SPACE -> {
                    ic.commitText(" ", 1)
                }
                KEY_ENTER -> {
                    ic.sendKeyEvent(KeyEvent(KeyEvent.ACTION_DOWN, KeyEvent.KEYCODE_ENTER))
                    ic.sendKeyEvent(KeyEvent(KeyEvent.ACTION_UP, KeyEvent.KEYCODE_ENTER))
                }
                KEY_VOICE -> {
                    // Sesli yazma butonu
                    if (voiceHelper?.isListening == true) {
                        voiceHelper?.stopListening()
                    } else {
                        voiceHelper?.startListening()
                    }
                }
                else -> {
                    // Normal karakter
                    val char = code.toChar()
                    ic.commitText(char.toString(), 1)
                }
            }
        }

        // Diğer zorunlu metodlar (boş bırakılabilir)
        override fun onPress(primaryCode: Int) {}
        override fun onRelease(primaryCode: Int) {}
        override fun onText(text: CharSequence) {}
        override fun swipeLeft() {}
        override fun swipeRight() {}
        override fun swipeDown() {}
        override fun swipeUp() {}
    }

    // -----------------------------------------------------------------
    //  Sesli yazma yardımcısı
    // -----------------------------------------------------------------
    inner class VoiceRecognizerHelper(
        private val service: InputMethodService,
        private val onResult: (String) -> Unit
    ) {
        private var speechRecognizer: android.speech.SpeechRecognizer? = null
        private var isListening = false

        init {
            // SpeechRecognizer mevcutsa oluştur
            if (android.speech.SpeechRecognizer.isRecognitionAvailable(service)) {
                speechRecognizer = android.speech.SpeechRecognizer.createSpeechRecognizer(service)
                speechRecognizer?.setRecognitionListener(object : android.speech.RecognitionListener {
                    override fun onReadyForSpeech(params: android.speech.RecognitionListener?) {}
                    override fun onBeginningOfSpeech() { isListening = true }
                    override fun onRmsChanged(rmsdB: Float) {}
                    override fun onBufferReceived(buffer: ByteArray?) {}
                    override fun onEndOfSpeech() { isListening = false }

                    override fun onError(error: Int) {
                        isListening = false
                        // Hata durumunda kullanıcıya bilgi verilebilir
                    }

                    override fun onResults(results: android.speech.Bundle?) {
                        val matches = results?.getStringArrayList(android.speech.SpeechRecognizer.RESULTS_RECOGNITION)
                        if (!matches.isNullOrEmpty()) {
                            onResult(matches[0]) // İlk sonuç
                        }
                    }

                    override fun onPartialResults(results: android.speech.Bundle?) {
                        // Gerçek‑zamanlı sonuçlar (isteğe bağlı)
                    }

                    override fun onEvent(eventType: Int, params: android.speech.Bundle?) {}
                })
            }
        }

        fun startListening() {
            if (speechRecognizer == null) return
            val intent = android.speech.RecognizerIntent()
                .putExtra(android.speech.RecognizerIntent.EXTRA_LANGUAGE_MODEL,
                        android.speech.RecognizerIntent.LANGUAGE_MODEL_FREE_FORM)
                .putExtra(android.speech.RecognizerIntent.EXTRA_PROMPT, "Sesli yazma")
                .putExtra(android.speech.RecognizerIntent.EXTRA_PARTIAL_RESULTS, true)

            // Dil tercihini kullanıcının ayarlardan seçtiği dil ile değiştirebilirsiniz
            // intent.putExtra(RecognizerIntent.EXTRA_LANGUAGE, Locale.getDefault().toString())

            speechRecognizer?.startListening(intent)
            isListening = true
        }

        fun stopListening() {
            speechRecognizer?.stopListening()
            isListening = false
        }

        fun destroy() {
            speechRecognizer?.destroy()
            speechRecognizer = null
        }
    }

    // -----------------------------------------------------------------
    //  Servis ömrü yönetimi
    // -----------------------------------------------------------------
    override fun onDestroy() {
        super.onDestroy()
        voiceHelper?.destroy()
    }
}
```

### 3.1 Tuş Kodları ve Özel Tuşlar  

| Kod | Anlamı |
|-----|--------|
| `-1` | Geri al (Backspace) |
| `-10` | Sesli yazma (Mikrofon) |
| `32` | Boşluk |
| `13` | Enter |
| `>0` | Unicode karakter (ör. `97` → ‘a’) |

> **İpucu:** Özel tuşlar için negatif değerler kullanmak yaygındır; bu değerler `InputConnection` üzerinden doğrudan metin ekler.

### 3.2 Öneri (Tahmin) Satırı  

`CandidateAdapter` ve `CandidateViewHolder` ile kullanıcıya kelime önerileri sunabilirsiniz. Basit bir örnek:

```kotlin
class CandidateAdapter(private val items: MutableList<String>) :
    RecyclerView.Adapter<CandidateAdapter.ViewHolder>() {

    class ViewHolder(itemView: View) : RecyclerView.ViewHolder(itemView) {
        val text: TextView = itemView.findViewById(R.id.candidate_text)
    }

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): ViewHolder {
        val view = LayoutInflater.from(parent.context)
            .inflate(R.layout.item_candidate, parent, false)
        return ViewHolder(view)
    }

    override fun onBindViewHolder(holder: ViewHolder, position: Int) {
        holder.text.text = items[position]
        holder.itemView.setOnClickListener {
            // Kullanıcı bir öneriyi seçtiğinde
            val ic = (holder.itemView.context as InputMethodService).currentInputConnection
            ic?.commitText(items[position] + " ", 1)
        }
    }

    override fun getItemCount(): Int = items.size

    fun updateList(newList: List<String>) {
        items.clear()
        items.addAll(newList)
        notifyDataSetChanged()
    }
}
```

`item_candidate.xml` sadece bir `TextView` içerir. Bu adaptörü `MyInputMethodService` içinde oluşturup `candidateRecycler.adapter` olarak atayabilirsiniz.

---

## 4. Sesli Yazma (Voice Typing) Detayları  

### 4.1 Gerekli İzin  

```kotlin
// SettingsActivity veya ilk başta kullanıcıdan izin isteyin
private fun requestAudioPermission() {
    ActivityCompat.requestPermissions(
        this,
        arrayOf(android.Manifest.permission.RECORD_AUDIO),
        PERM_REQ_CODE_AUDIO
    )
}
```

### 4.2 Dil ve Lokasyon  

`RecognizerIntent.EXTRA_LANGUAGE` ile kullanıcının seçtiği dili belirleyebilirsiniz:

```kotlin
val locale = Locale("tr", "TR") // Türkçe için örnek
intent.putExtra(RecognizerIntent.EXTRA_LANGUAGE, locale.toString())
```

### 4.3 Gerçek‑Zamanlı (Partial) Sonuçlar  

`onPartialResults` içinde kullanıcıya anlık geri bildirim verebilirsiniz (ör. mikrofon ikonu yanıp söner, yazılan kelime geçici olarak gösterilir).

### 4.4 Performans ve Akıllı Kullanım  

* **Sesli yazma yalnızca klavye açıkken** çalışmalı → `onStartInputView` ve `onFinishInputView` içinde `voiceHelper?.stopListening()` çağırın.  
* **Sesli yazma oturumu sonunda** `destroy()` ile `SpeechRecognizer`’ı serbest bırakın.  
* **Ağ bağlantısı yoksa** offline tanıma için `EXTRA_PREFER_OFFLINE` ekleyin:

```kotlin
intent.putExtra(RecognizerIntent.EXTRA_PREFER_OFFLINE, true)
```

### 4.5 UI Geri Bildirimi  

Mikrofon tuşunu “dinlemeden” ikona olarak, dinleme sırasında “dalga” animasyonu ile değiştirebilirsiniz. `VoiceRecognizerHelper` içinde `isListening` bayrağını takip eden bir `LiveData` veya `MutableStateFlow` oluşturup `keyboardView`’a bağlayabilirsiniz.

---

## 5. Ek Özellikler (Özelikler)  

### 5.1 Makro (Özel Komut) Tuşları  

Kullanıcıların sık kullandığı cümleleri bir “makro” olarak kaydetmelerini sağlayabilirsiniz.

1. **Ayarlar ekranında** bir liste tutun (`SharedPreferences` veya `Room` veritabanı).  
2. Makro tuşunu klavyeye ekleyin (`KEY_MACRO = -20`).  
3. Tuşa basıldığında, kullanıcının seçtiği makroyu `commitText` ile ekleyin.

### 5.2 Emojiler  

`EmojiCompat` ile emoji picker ekleyebilirsiniz. Basit bir yol:

```kotlin
val emojiPicker = EmojiPicker(this)
emojiPicker.setOnEmojiSelectedListener { emoji ->
    currentInputConnection?.commitText(emoji, 1)
}
```

### 5.3 Otomatik Düzeltme ve Tahmin  

* **Kelime tahminleri** için `SpellCheckerSession` veya `TextInfo` kullanabilirsiniz.  
* **Kullanıcı girdilerini** bir `HashSet` içinde saklayıp en sık kullanılan kelimeleri öneri listesine ekleyebilirsiniz.

### 5.4 Klavye Temaları  

`styles.xml` içinde farklı temalar tanımlayın ve `SharedPreferences` ile kullanıcı tercihini saklayın. Tema değiştiğinde `keyboardView.invalidateAllKeys()` çağırın.

```xml
<style name="KeyboardTheme.Dark" parent="android:Theme">
    <item name="android:keyBackground">@drawable/key_background_dark</item>
    <item name="android:textColor">#FFFFFF</item>
</style>
```

### 5.5 Hareketli (Swipe) Yazma  

`GestureDetector` ile `onTouchEvent` içinde sağ‑sol kaydırma tanıma:

```kotlin
private val gestureDetector = GestureDetector(this, object : GestureDetector.SimpleOnGestureListener() {
    override fun onFling(e1: MotionEvent?, e2: MotionEvent, velocityX: Float, velocityY: Float): Boolean {
        if (e1 != null && Math.abs(e2.x - e1.x) > SWIPE_THRESHOLD) {
            if (e2.x > e1.x) {
                // Sağ kaydırma → silme (backspace)
                currentInputConnection?.deleteSurroundingText(1, 0)
            } else {
                // Sol kaydırma → boşluk
                currentInputConnection?.commitText(" ", 1)
            }
            return true
        }
        return false
    }
})
```

### 5.6 Haptic ve Ses Geri Bildirimi  

```kotlin
keyboardView.setHapticFeedbackEnabled(true)
keyboardView.soundEffectsEnabled = true
```

---

## 6. Performans ve Optimizasyon  

| Alan | Optimizasyon |
|------|--------------|
| **Görsel** | `KeyboardView`’ın `setPreviewEnabled(false)` ile tuş önizlemesini kapatın (daha akıcı). |
| **Öneri Listesi** | `RecyclerView` ile sadece görünür öğeleri oluşturun; `DiffUtil` kullanarak gereksiz yeniden çizimleri önleyin. |
| **Sesli Yazma** | `SpeechRecognizer`’ı **sadece gerektiğinde** başlatın; `onFinishInputView` içinde durdurun. |
| **Arka Plan İşlemleri** | Ağır işlemleri (`Room` sorguları, makro işleme) `CoroutineScope(Dispatchers.IO)` içinde çalıştırın. |
| **Bellek** | `LeakCanary` ile bellek sızıntılarını tespit edin. |
| **CPU** | `KeyboardView`’ın `setKeyboard(keyboard)` çağrısını **sadece klavye değiştiğinde** yapın; her tuş basışında yeniden oluşturmayın. |
| **Ağır Grafik** | Animasyonlar için `VectorDrawable` yerine `AnimatedVectorDrawable` kullanın; `PropertyAnimation` ile hafif animasyonlar yapın. |

---

## 7. Test, Hata Ayıklama ve Yayımlama  

### 7.1 Test Cihazı / Emülatör  

1. **Klavyeyi etkinleştirin**:  
   `Ayarlar → Sistem → Dil ve Giriş → Sanal Klavye → Yönet → Your Keyboard → Etkinleştir`.  
2. **Metin alanına tıklayın** → klavye otomatik olarak açılacaktır.

### 7.2 Loglama  

```kotlin
private val TAG = "MyKeyboard"
Log.d(TAG, "Voice result: $transcript")
```

### 7.3 Hata Ayıklama  

* **`InputMethodService`** içinde `onCreateInputView` ve `onStartInputView` çağrılarını loglayın.  
* **SpeechRecognizer** hatalarını `onError` içinde detaylı yazdırın.

### 7.4 Yayımlama  

* **`build.gradle`** içinde `android:exported="true"` özelliğini `service` ve `activity` tanımlarına ekleyin (Android 12+).  
* **Gizlilik Politikası**: Sesli yazma kullandığınız için bir politika belgesi oluşturup Play Store’a yükleyin.  
* **İzinler**: `RECORD_AUDIO` iznini manifest’e ekleyin ve ilk açılışta kullanıcıya isteyin.

---

## 8. Sık Sorulan Sorular ve İpuçları  

| Soru | Cevap |
|------|-------|
| **Klavyemi sadece belirli uygulamalarda mı çalıştırmak istiyorum?** | `onStartInputView` içinde `EditorInfo`’dan `inputType` ve `packageName` bilgilerini kontrol edip `if` koşulu ile klavyeyi gizleyebilirsiniz. |
| **Birden fazla dil desteği nasıl eklerim?** | `res/xml` içinde her dil için ayrı bir klavye düzeni oluşturun (`keyboard_layout_tr.xml`, `keyboard_layout_en.xml`). `SharedPreferences` ile kullanıcı dili seçsin, `onCreateInputView` içinde odpowied `keyboard` yükleyin. |
| **Kullanıcı özel tuşlar eklemek istiyor, nasıl saklarım?** | `Room` veritabanında `Macro` tablosu oluşturun (`id`, `title`, `text`). Ayarlar ekranında bir liste ile düzenlenebilir. |
| **Sesli yazma çalışmıyor (hata kodu 9)** | Cihazınızda offline tanıma desteklenmiyor olabilir. `EXTRA_PREFER_OFFLINE` yerine online tanıma geçin veya Google Cloud Speech‑to‑Text API’sini entegre edin (ücretli). |
| **Klavye çok yavaş, nasıl hızlandırırım?** | `KeyboardView`’ın `setPreviewEnabled(false)` yapın, gereksiz `invalidate()` çağrılarını kaldırın, büyük resim dosyalarını küçültün, `RecyclerView` için `setHasFixedSize(true)` kullanın. |
| **Kullanıcı klavyeyi kapattığında sesli yazma durmuyor** | `onFinishInputView` içinde `voiceHelper?.stopListening()` çağırın. |
| **Tema değiştirme nasıl yapılır?** | `SharedPreferences` içinde `"theme"` anahtarı saklayın (`light`/`dark`). `onCreateInputView` içinde bu değeri okuyup `keyboardView.setKeyBackgroundDrawable` ve `textColor` gibi özelliklerini ayarlayın. |

---

## 9. Başlamak İçin Mini‑Checklist  

1. **Proje oluştur** → `InputMethodService` ve gerekli XML’leri ekle.  
2. **Klavye düzeni** (`keyboard_layout.xml`) oluştur ve `R.xml.keyboard_layout` referansını yükle.  
3. **`MyInputMethodService`** içinde `onCreateInputView`’da klavyeyi ve `KeyboardView`’ı bağla.  
4. **Tuş işleme** (`onKey`) ile temel metin girme, silme, boşluk, enter ve mikrofon tuşunu uygula.  
5. **`VoiceRecognizerHelper`** sınıfını yaz ve mikrofon tuşuna basıldığında sesli yazma başlat/durdur.  
6. **İzinleri** `AndroidManifest.xml` ve runtime’da iste.  
7. **Ayarlar ekranı** (`SettingsActivity`) ile kullanıcı tercihlerini (dil, tema, makrolar) sakla.  
8. **Öneri satırı** (`RecyclerView`) ve basit bir `CandidateAdapter` ekle.  
9. **Test et**: Klavyeyi etkinleştir, metin alanına tıklayıp tuş ve sesli yazmayı dene.  
10. **Optimizasyon ve hata ayıklama** → Loglar, LeakCanary, profil araçları.  

---

### Sonraki Adımlar  

* Hangi **özellikleri** öncelikli olarak eklemek istediğinizi belirleyin (ör. makro tuşları, emoji picker, dil değiştirme).  
* Kullanılacak **dil** (sadece Türkçe mi, çoklu dil mi) ve **tema** (açık/karanlık) kararlarını verin.  
* **Kotlin** mi yoksa **Java** mı kullanacağınızı seçin (örnek kodlar Kotlin ile verilmiştir).  

Bu kılavuza göre adım adım ilerlerseniz, **sesli yazma** ve birçok özel işlevi barındıran, performanslı bir Android klavyesi oluşturabilirsiniz.  

**Başarılar!** 🚀  

---  

*Herhangi bir noktada takıldığınız ya da eklemek istediğiniz bir özellik varsa, detaylı sorularınızı sorabilirsiniz.*

### DeepSeek V3
*2026-01-27 03:48:03 +03*

Anladığım kadarıyla, Android için klavye tasarımı ve geliştirmesi üzerine odaklanmak istiyorsunuz. Öncelikle, klavye tasarımında dikkat edilmesi gereken bazı önemli noktaları ele alalım:

1. **Kullanıcı Arayüzü (UI) Tasarımı:**
   - **Maksimum Ölçeklenebilirlik (Scalability):** Klavyenin farklı ekran boyutlarına ve çözünürlüklerine uyum sağlayacak şekilde tasarlanmalıdır. Bu, hem küçük hem de büyük ekranlı cihazlarda kullanıcı deneyimini optimize eder.
   - **Sesle Yazma Özelliği:** Sesle yazma (Voice Typing) özelliği, klavyenin kullanımını kolaylaştırabilir ve hızlandırabilir. Bu özellik, özellikle mobil cihazlarda çok kullanışlıdır.

2. **Fonksiyonellik:**
   - **Özelleştirilebilir Anahtarlar:** Kullanıcıların sık kullandıkları tuşları özelleştirebilmeli ve bunları kolayca erişilebilir kılmalıdır. Bu, kullanıcı deneyimini artırır.
   - **Yapay Zeka Entegrasyonu:** Klavye, yapay zeka destekli öneriler ve tahminler sunabilir. Örneğin, yazım hatalarını düzeltme, kelime önerileri gibi.

3. **Performans ve Optimizasyon:**
   - **Hızlı ve Akıcı Yazma Deneyimi:** Klavye, yüksek performanslı ve gecikmesiz bir yazma deneyimi sunmalıdır.
   - **Minimum Kaynak Kullanımı:** Klavye, cihazın işlemci ve bellek kullanımını minimize edecek şekilde optimize edilmelidir.

4. **Geliştirme ve Test Süreçleri:**
   - **Sürekli İyileştirme:** Klavye, kullanıcı geri bildirimleri doğrultusunda sürekli olarak iyileştirilmeli ve güncellenmelidir.
   - **Geniş Kapsamlı Testler:** Klavye, farklı cihazlarda ve işletim sistemi sürümlerinde geniş çaplı testlerden geçmelidir.

Bu adımları takip ederek, Android için hem kullanıcı dostu hem de performansı yüksek bir klavye tasarlamak mümkündür. Eğer detaylı bir planlama veya prototip oluşturma aşamasında yardıma ihtiyacınız olursa, bu konuda da destek olabilirim.
