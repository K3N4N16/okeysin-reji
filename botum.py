import { useEffect, useMemo, useRef, useState, type FormEvent } from "react";

type Mode = {
  id: string;
  name: string;
  vibe: string;
  accent: string;
  glow: string;
  surface: string;
  description: string;
  responseTone: string;
  pitch: number;
  rate: number;
};

type ChatMessage = {
  id: string;
  role: "user" | "assistant";
  text: string;
  meta?: string;
};

const modes: Mode[] = [
  {
    id: "gece",
    name: "Gece Akışı",
    vibe: "derin, sakin ve rafine",
    accent: "#7dd3fc",
    glow: "rgba(45, 212, 191, 0.28)",
    surface: "rgba(15, 23, 42, 0.82)",
    description: "Yumuşak geçişler, net anonslar ve gece yayınına uygun sıcak bir ton.",
    responseTone: "sakin bir frekansla",
    pitch: 0.95,
    rate: 0.98,
  },
  {
    id: "neon",
    name: "Neon Yayın",
    vibe: "enerjik, parlak ve modern",
    accent: "#f472b6",
    glow: "rgba(244, 114, 182, 0.30)",
    surface: "rgba(24, 16, 43, 0.84)",
    description: "Hızlı anonslar, vurucu girişler ve sahneye çıkan canlı bir stil.",
    responseTone: "parlak bir ritimle",
    pitch: 1.1,
    rate: 1.04,
  },
  {
    id: "ask",
    name: "Aşk Frekansı",
    vibe: "işveli, sıcak ve yakın",
    accent: "#fb7185",
    glow: "rgba(251, 113, 133, 0.28)",
    surface: "rgba(40, 19, 32, 0.84)",
    description: "Mesajlara romantik bir tını, yumuşak ses geçişleri ve samimi bir sahne.",
    responseTone: "tatlı bir tebessümle",
    pitch: 1.18,
    rate: 1.0,
  },
];

const featureRows = [
  {
    title: "Hibrit ses motoru",
    text: "RVC destekli akış, Edge-TTS yedeği ve gTTS kurtarma zinciri ile yayını güvenli tutar.",
  },
  {
    title: "Modlu sahne tasarımı",
    text: "Gece, neon ve aşk frekansı temaları arasında tek dokunuşla geçiş yapar.",
  },
  {
    title: "Canlı metin anonsu",
    text: "Yazdığın cümleyi stüdyo diline çevirir, ardından konuşma ritmiyle dinletir.",
  },
  {
    title: "Yayına hazır akış",
    text: "Sohbet, cevap üretimi ve sesli okuma tek ekranda, sade ama güçlü bir düzenle birleşir.",
  },
];

const flowSteps = [
  {
    step: "01",
    title: "Yaz",
    text: "Patron kısa ya da uzun bir mesaj bırakır, sahne onu alır.",
  },
  {
    step: "02",
    title: "Kurgula",
    text: "Tonda, modda ve yayının karakterinde anlık ayar yapılır.",
  },
  {
    step: "03",
    title: "Konuş",
    text: "Yanıt üretilir, ardından uygun bir sesle duyurulur.",
  },
  {
    step: "04",
    title: "Yayına al",
    text: "Hazır mesaj stüdyo akışına yerleşir ve canlı hissi korunur.",
  },
];

const quickPrompts = [
  "Bursa'dan geceye özel selam ver",
  "Bana kısa bir şarkı arası anons yaz",
  "Patron için tatlı ve modern bir karşılama hazırla",
];

function createReply(input: string, mode: Mode) {
  const normalized = input.toLowerCase();

  if (normalized.includes("selam") || normalized.includes("merhaba")) {
    return `Selam patron. ${mode.name} modunda ${mode.responseTone} seni karşıladım; frekans şimdi tamamen bize ait.`;
  }

  if (normalized.includes("şark") || normalized.includes("sarki")) {
    return `${mode.name} için kısa bir anons: "Sıradaki parça geldi, ışıklar yumuşasın, ses yükselsin."`;
  }

  if (normalized.includes("aşk") || normalized.includes("ask")) {
    return `Bu cümleyi ${mode.responseTone} işledim: "Kalbimiz yayında, sözlerimiz tam yerinde."`;
  }

  if (normalized.includes("bursa")) {
    return `Bursa sahnesi hazır. ${mode.name} tonu ile şehrin enerjisini pürüzsüz ve sıcak bir anonsa dönüştürdüm.`;
  }

  return `${mode.name} altında ${mode.responseTone} şunu derim: "${input.trim()}". Cümle hazır, mikrofon açık, ışıklar bize bakıyor.`;
}

function makeId() {
  return `${Date.now()}-${Math.random().toString(36).slice(2, 8)}`;
}

export default function App() {
  const [modeId, setModeId] = useState(modes[0].id);
  const [draft, setDraft] = useState("");
  const [isSending, setIsSending] = useState(false);
  const [clock, setClock] = useState(() => new Date());
  const [messages, setMessages] = useState<ChatMessage[]>([
    {
      id: makeId(),
      role: "assistant",
      text: "Hazırım patron. Bana bir cümle ver, onu modern bir stüdyo tonuna çevireyim.",
      meta: "Sistem durumu: canlı",
    },
  ]);
  const timerRef = useRef<number | null>(null);

  const activeMode = useMemo(() => modes.find((item) => item.id === modeId) ?? modes[0], [modeId]);
  const lastAssistantMessage = useMemo(() => [...messages].reverse().find((message) => message.role === "assistant"), [messages]);

  useEffect(() => {
    const tick = window.setInterval(() => setClock(new Date()), 1000);
    return () => window.clearInterval(tick);
  }, []);

  useEffect(() => {
    return () => {
      if (timerRef.current) {
        window.clearTimeout(timerRef.current);
      }
      if ("speechSynthesis" in window) {
        window.speechSynthesis.cancel();
      }
    };
  }, []);

  const speak = (text: string) => {
    if (!("speechSynthesis" in window)) return;

    const synth = window.speechSynthesis;
    const utterance = new SpeechSynthesisUtterance(text);
    const voices = synth.getVoices();
    const preferredVoice = voices.find((voice) => voice.lang.toLowerCase().startsWith("tr")) ?? voices[0];

    utterance.lang = "tr-TR";
    utterance.rate = activeMode.rate;
    utterance.pitch = activeMode.pitch;

    if (preferredVoice) {
      utterance.voice = preferredVoice;
    }

    synth.cancel();
    synth.speak(utterance);
  };

  const sendPrompt = (value: string) => {
    const prompt = value.trim();
    if (!prompt || isSending) return;

    const userMessage: ChatMessage = { id: makeId(), role: "user", text: prompt };
    const reply = createReply(prompt, activeMode);
    const assistantMessage: ChatMessage = {
      id: makeId(),
      role: "assistant",
      text: reply,
      meta: `${activeMode.name} · ses hazır`,
    };

    setMessages((current) => [...current, userMessage]);
    setIsSending(true);
    setDraft("");

    timerRef.current = window.setTimeout(() => {
      setMessages((current) => [...current, assistantMessage]);
      setIsSending(false);
      speak(reply);
    }, 750);
  };

  const handleSubmit = (event: FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    sendPrompt(draft);
  };

  return (
    <div
      className="min-h-screen overflow-hidden text-white"
      style={{
        backgroundImage: `radial-gradient(circle at 20% 10%, ${activeMode.glow}, transparent 28%), radial-gradient(circle at 80% 20%, rgba(99, 102, 241, 0.22), transparent 26%), radial-gradient(circle at 60% 85%, rgba(15, 23, 42, 0.92), transparent 30%), linear-gradient(180deg, #020617 0%, #050816 45%, #081020 100%)`,
      }}
    >
      <header className="mx-auto flex max-w-7xl items-center justify-between px-6 py-6 lg:px-10">
        <div>
          <p className="text-[0.68rem] uppercase tracking-[0.5em] text-white/45">Faslı Muhabbet v16.0</p>
          <p className="mt-1 text-sm text-white/65">Bursa Stüdyosu · {clock.toLocaleTimeString("tr-TR", { hour: "2-digit", minute: "2-digit" })}</p>
        </div>
        <a
          href="#demo"
          className="rounded-full border border-white/12 bg-white/5 px-4 py-2 text-sm text-white/80 transition hover:border-white/25 hover:bg-white/10"
        >
          Canlı demo
        </a>
      </header>

      <main>
        <section className="relative mx-auto min-h-[calc(100vh-84px)] max-w-7xl px-6 pb-14 lg:px-10">
          <div className="absolute left-[-8rem] top-10 h-72 w-72 rounded-full blur-3xl animate-float" style={{ background: activeMode.glow }} />
          <div className="absolute right-[-7rem] top-28 h-80 w-80 rounded-full bg-fuchsia-500/10 blur-3xl animate-drift" />

          <div className="grid min-h-[calc(100vh-140px)] items-center gap-12 lg:grid-cols-[1.05fr_0.95fr]">
            <div className="relative z-10 max-w-2xl">
              <p className="text-sm uppercase tracking-[0.35em] text-white/45">Modern ses sahnesi</p>
              <h1 className="mt-6 text-5xl font-semibold tracking-tight text-white sm:text-6xl lg:text-7xl">
                Canlı ses, sıcak sohbet ve tek dokunuşta şık yayın akışı.
              </h1>
              <p className="mt-6 max-w-xl text-lg leading-8 text-white/72 sm:text-xl">
                Faslı Muhabbet, mesajı sadece yanıtlamaz; onu stüdyo havasına sokar, güçlü bir tonla sunar ve
                ekranda modern bir deneyime dönüştürür.
              </p>

              <div className="mt-8 flex flex-wrap gap-3">
                <a
                  href="#demo"
                  className="rounded-full px-5 py-3 text-sm font-medium text-slate-950 transition hover:scale-[1.01]"
                  style={{ background: activeMode.accent, boxShadow: `0 0 0 1px ${activeMode.accent}40, 0 18px 55px ${activeMode.glow}` }}
                >
                  Canlı dene
                </a>
                <a
                  href="#features"
                  className="rounded-full border border-white/14 bg-white/5 px-5 py-3 text-sm font-medium text-white/85 transition hover:border-white/24 hover:bg-white/10"
                >
                  Yeni özellikler
                </a>
              </div>

              <div className="mt-10 inline-flex flex-wrap gap-2 rounded-full border border-white/10 bg-white/6 p-2 backdrop-blur-xl">
                {modes.map((mode) => {
                  const active = mode.id === activeMode.id;
                  return (
                    <button
                      key={mode.id}
                      type="button"
                      onClick={() => setModeId(mode.id)}
                      className="rounded-full px-4 py-2 text-sm transition"
                      style={{
                        background: active ? mode.accent : "transparent",
                        color: active ? "#020617" : "rgba(255,255,255,0.8)",
                      }}
                    >
                      {mode.name}
                    </button>
                  );
                })}
              </div>

              <p className="mt-5 max-w-2xl text-sm leading-7 text-white/56">{activeMode.description}</p>
            </div>

            <div className="relative z-10">
              <div
                className="relative overflow-hidden rounded-[2rem] border border-white/12 p-6 shadow-2xl shadow-slate-950/40 backdrop-blur-2xl"
                style={{ background: activeMode.surface }}
              >
                <div className="absolute inset-0 opacity-70" style={{ background: `linear-gradient(145deg, ${activeMode.glow}, transparent 40%)` }} />
                <div className="relative">
                  <div className="flex items-center justify-between">
                    <div>
                      <p className="text-xs uppercase tracking-[0.35em] text-white/45">Canlı stüdyo</p>
                      <h2 className="mt-2 text-2xl font-semibold text-white">Ses sahnesi aktif</h2>
                    </div>
                    <span
                      className="rounded-full border px-3 py-1 text-xs font-medium"
                      style={{ borderColor: `${activeMode.accent}50`, color: activeMode.accent }}
                    >
                      Live
                    </span>
                  </div>

                  <div className="mt-8 grid gap-6 lg:grid-cols-[0.9fr_1.1fr]">
                    <div className="relative flex min-h-[22rem] items-center justify-center overflow-hidden rounded-[1.8rem] border border-white/10 bg-white/5">
                      <div className="absolute inset-0 bg-[radial-gradient(circle_at_center,rgba(255,255,255,0.14),transparent_55%)]" />
                      <div className="absolute h-40 w-40 rounded-full border border-white/20 animate-glow" style={{ boxShadow: `0 0 0 1px ${activeMode.accent}40, 0 0 80px ${activeMode.glow}` }} />
                      <div className="absolute h-24 w-24 rounded-full border border-white/18 bg-white/8 backdrop-blur-md" />
                      <div className="relative flex h-14 w-14 items-center justify-center rounded-full" style={{ background: activeMode.accent }}>
                        <svg viewBox="0 0 24 24" className="h-7 w-7 text-slate-950" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                          <path d="M12 1v11" />
                          <rect x="8" y="3" width="8" height="12" rx="4" />
                          <path d="M6 11a6 6 0 0 0 12 0" />
                          <path d="M12 19v4" />
                          <path d="M8 23h8" />
                        </svg>
                      </div>

                      <div className="absolute bottom-8 left-1/2 flex -translate-x-1/2 items-end gap-1.5">
                        {[22, 38, 62, 46, 78, 52, 84, 56, 40, 28].map((height, index) => (
                          <span
                            key={`${height}-${index}`}
                            className="w-1.5 rounded-full bg-white/70 animate-wave"
                            style={{ height: `${height}px`, animationDelay: `${index * 90}ms`, backgroundColor: index % 2 === 0 ? activeMode.accent : "rgba(255,255,255,0.6)" }}
                          />
                        ))}
                      </div>

                      <div className="absolute left-6 top-6 rounded-full border border-white/10 bg-black/25 px-3 py-1 text-xs text-white/70 backdrop-blur-md">
                        Ses motoru: hibrit
                      </div>
                      <div className="absolute right-6 top-6 rounded-full border border-white/10 bg-black/25 px-3 py-1 text-xs text-white/70 backdrop-blur-md">
                        {activeMode.name}
                      </div>
                    </div>

                    <div className="flex flex-col justify-between gap-4 rounded-[1.8rem] border border-white/10 bg-black/20 p-5 backdrop-blur-md">
                      <div className="space-y-4">
                        <div>
                          <p className="text-xs uppercase tracking-[0.35em] text-white/40">Kısa durum</p>
                          <p className="mt-2 text-lg font-medium text-white">Yedek zinciri hazır, yayın akışı stabil.</p>
                        </div>

                        <div className="space-y-3 text-sm text-white/74">
                          <div className="flex items-center justify-between rounded-2xl border border-white/10 bg-white/5 px-4 py-3">
                            <span>RVC uyumu</span>
                            <span className="font-medium" style={{ color: activeMode.accent }}>Hazır</span>
                          </div>
                          <div className="flex items-center justify-between rounded-2xl border border-white/10 bg-white/5 px-4 py-3">
                            <span>Edge-TTS</span>
                            <span className="font-medium text-emerald-300">Yedek açık</span>
                          </div>
                          <div className="flex items-center justify-between rounded-2xl border border-white/10 bg-white/5 px-4 py-3">
                            <span>gTTS</span>
                            <span className="font-medium text-sky-300">Kurtarma aktif</span>
                          </div>
                        </div>
                      </div>

                      <div className="rounded-[1.4rem] border border-white/10 bg-white/6 p-4 text-sm text-white/72">
                        <p className="text-white/50">Canlı örnek</p>
                        <p className="mt-2 leading-7">
                          {`Patron, gece frekansı açık. Bugün sahne ${activeMode.responseTone} akıyor ve her söz stüdyo ışığında parlıyor.`}
                        </p>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </section>

        <section id="features" className="mx-auto max-w-7xl px-6 pb-6 lg:px-10">
          <div className="grid gap-10 lg:grid-cols-[0.9fr_1.1fr]">
            <div>
              <p className="text-sm uppercase tracking-[0.35em] text-white/40">Yeni özellikler</p>
              <h2 className="mt-4 text-3xl font-semibold tracking-tight text-white sm:text-4xl">
                Daha modern, daha kontrol edilebilir, daha gösterişli bir yayın deneyimi.
              </h2>
              <p className="mt-4 max-w-xl text-base leading-7 text-white/65">
                Bu sürüm, tek ekranda daha net bir sahne kurar. Arka plan, ton ve yanıt akışı birleşir; sonuçta hem
                şık bir arayüz hem de hızlı bir demo ortaya çıkar.
              </p>
            </div>

            <div className="space-y-0 rounded-[2rem] border border-white/10 bg-white/5 backdrop-blur-xl">
              {featureRows.map((row, index) => (
                <div
                  key={row.title}
                  className={`grid gap-4 px-5 py-5 ${index !== featureRows.length - 1 ? "border-b border-white/10" : ""} sm:grid-cols-[0.7fr_1.3fr]`}
                >
                  <h3 className="text-base font-medium text-white">{row.title}</h3>
                  <p className="text-sm leading-7 text-white/66">{row.text}</p>
                </div>
              ))}
            </div>
          </div>
        </section>

        <section id="demo" className="mx-auto max-w-7xl px-6 py-16 lg:px-10">
          <div className="grid gap-8 lg:grid-cols-[1.1fr_0.9fr]">
            <div className="rounded-[2rem] border border-white/10 bg-white/5 p-6 backdrop-blur-xl">
              <div className="flex items-start justify-between gap-4">
                <div>
                  <p className="text-sm uppercase tracking-[0.35em] text-white/40">Canlı deneme</p>
                  <h2 className="mt-3 text-3xl font-semibold tracking-tight text-white">Mesajı yaz, sahnede duymalısın.</h2>
                </div>
                <button
                  type="button"
                  onClick={() => speak(lastAssistantMessage?.text ?? messages[messages.length - 1]?.text ?? "")}
                  className="rounded-full border border-white/12 bg-white/5 px-4 py-2 text-sm text-white/80 transition hover:border-white/25 hover:bg-white/10"
                >
                  Son cevabı dinlet
                </button>
              </div>

              <div className="mt-6 space-y-3">
                {messages.map((message) => (
                  <div
                    key={message.id}
                    className={`max-w-[92%] rounded-[1.35rem] px-4 py-3 text-sm leading-7 ${
                      message.role === "user"
                        ? "ml-auto border border-white/12 bg-white/10 text-white"
                        : "border border-white/10 bg-black/18 text-white/84"
                    }`}
                  >
                    <p>{message.text}</p>
                    {message.meta ? <p className="mt-2 text-[0.72rem] uppercase tracking-[0.25em] text-white/40">{message.meta}</p> : null}
                  </div>
                ))}

                {isSending ? (
                  <div className="max-w-[65%] rounded-[1.35rem] border border-white/10 bg-black/18 px-4 py-3 text-sm text-white/60">
                    Dilay düşünüyor, mikrofon ışığı açık...
                  </div>
                ) : null}
              </div>

              <form onSubmit={handleSubmit} className="mt-6 space-y-4">
                <div className="rounded-[1.4rem] border border-white/12 bg-black/22 p-3 shadow-inner shadow-black/20">
                  <textarea
                    value={draft}
                    onChange={(event) => setDraft(event.target.value)}
                    placeholder="Patron, bir cümle bırak..."
                    rows={3}
                    className="w-full resize-none bg-transparent px-2 py-1 text-sm leading-7 text-white outline-none placeholder:text-white/30"
                  />
                </div>

                <div className="flex flex-wrap items-center gap-3">
                  <button
                    type="submit"
                    className="rounded-full px-5 py-3 text-sm font-medium text-slate-950 transition hover:scale-[1.01] disabled:cursor-not-allowed disabled:opacity-60"
                    style={{ background: activeMode.accent }}
                    disabled={isSending}
                  >
                    Yayına gönder
                  </button>

                  {quickPrompts.map((prompt) => (
                    <button
                      key={prompt}
                      type="button"
                      onClick={() => sendPrompt(prompt)}
                      className="rounded-full border border-white/12 bg-white/5 px-4 py-2 text-xs text-white/74 transition hover:border-white/24 hover:bg-white/10"
                    >
                      {prompt}
                    </button>
                  ))}
                </div>
              </form>
            </div>

            <div className="space-y-6">
              <div className="rounded-[2rem] border border-white/10 bg-white/5 p-6 backdrop-blur-xl">
                <p className="text-sm uppercase tracking-[0.35em] text-white/40">Aktif mod</p>
                <h3 className="mt-3 text-2xl font-semibold text-white">{activeMode.name}</h3>
                <p className="mt-3 text-sm leading-7 text-white/65">{activeMode.description}</p>

                <div className="mt-5 flex flex-wrap gap-2 text-xs text-white/60">
                  <span className="rounded-full border border-white/10 bg-white/5 px-3 py-1">Vibe: {activeMode.vibe}</span>
                  <span className="rounded-full border border-white/10 bg-white/5 px-3 py-1">Pitch: {activeMode.pitch.toFixed(2)}</span>
                  <span className="rounded-full border border-white/10 bg-white/5 px-3 py-1">Rate: {activeMode.rate.toFixed(2)}</span>
                </div>
              </div>

              <div className="rounded-[2rem] border border-white/10 bg-white/5 p-6 backdrop-blur-xl">
                <p className="text-sm uppercase tracking-[0.35em] text-white/40">Yayın akışı</p>
                <div className="mt-5 space-y-4">
                  {flowSteps.map((item) => (
                    <div key={item.step} className="flex gap-4 rounded-[1.2rem] border border-white/10 bg-black/18 px-4 py-4">
                      <div className="flex h-11 w-11 shrink-0 items-center justify-center rounded-full border border-white/10 bg-white/6 text-sm font-semibold text-white/70">
                        {item.step}
                      </div>
                      <div>
                        <h4 className="text-base font-medium text-white">{item.title}</h4>
                        <p className="mt-1 text-sm leading-7 text-white/64">{item.text}</p>
                      </div>
                    </div>
                  ))}
                </div>
              </div>
            </div>
          </div>
        </section>
      </main>

      <footer className="mx-auto max-w-7xl px-6 pb-8 text-sm text-white/45 lg:px-10">
        Faslı Muhabbet, modern yayın sahnesi için tasarlanmış tek sayfalık bir demo deneyimidir.
      </footer>
    </div>
  );
}
