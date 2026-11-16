# ENG TEACHER — PROJECT CONTINUITY, RESEARCH AND CHAT HANDOFF

**Latest organization update:** 17 November 2026 (Asia/Calcutta)

**Historical research snapshot:** 16 November 2026
**Main repository:** https://github.com/Planeshiffhter/eng-teacher  
**Purpose:** A self-contained, GitHub-readable continuity document for a future human engineer, ChatGPT, or GPT Codex session when the original chat is unavailable or too long.  
**Read order:** This file → AGENTS.md → latest GitHub tree/PRs/CI → relevant code → canonical docs.  
**Scope:** Consolidates the project-relevant facts and available earlier conversation summaries, implementation evidence, research findings, GitHub links, diagrams and decisions. It is **not a complete verbatim export of every prior private chat**. Anything not independently verified must be checked before acting.

> **CURRENT ORGANIZATION UPDATE:** The owner requested a structure audit, preservation of deferred material in `AnalyseFuture/`, and a detailed product idea. Work began from verified local/remote `main` at `38e9d0034ba613052b3e7d37f902ed635eae8d9c`; no newer tracked changes established an attack. The organization checkpoint is [`a1457a3`](https://github.com/Planeshiffhter/eng-teacher/commit/a1457a3). All 1,478 moved files are byte-identical. Active source remains in `apps/web` and `services/voice-agent`. Read [the structure audit](REPOSITORY_STRUCTURE.md), [current validation](VALIDATION.md), and [PROJECT_IDEA.txt](../PROJECT_IDEA.txt), including the owner's Bengali-English and friendly on-screen teacher goals. Current local checks passed: 14 JavaScript tests, 42 Python tests, 6 browser tests, build, typecheck and Ruff. This is preservation/planning work, not a new voice/translation/avatar implementation or an account-security investigation.

> **CURRENT OWNER WORKFLOW:** Work directly on `main`, without a feature branch or new PR; commit and push useful checkpoints at least every five minutes while editing when changes exist. Keep prior work and preserve material set aside for future analysis in `AnalyseFuture/`. These instructions supersede historical branch/PR suggestions below. Do not force-push shared history. No historical PR was merged as part of this organization task.

> **HISTORICAL STATUS SNAPSHOT:** At the time the original research snapshot was written, the most recent audited main commit was [88f600d3176a943d355deb9db4490a6387523fad](https://github.com/Planeshiffhter/eng-teacher/commit/88f600d3176a943d355deb9db4490a6387523fad) (15 Nov 2026). [PR #1](https://github.com/Planeshiffhter/eng-teacher/pull/1) was OPEN, **not merged**, at head [da2796ebaca461c7ac0551182bfb7534f8498551](https://github.com/Planeshiffhter/eng-teacher/commit/da2796ebaca461c7ac0551182bfb7534f8498551). Its [final CI run 43749668384](https://github.com/Planeshiffhter/eng-teacher/actions/runs/43749668384) succeeded. These are dated historical observations, not a new verification of PR or remote CI status.

## 1. For a new GPT/Codex session: start here, not from scratch

1. Read this document, [AGENTS.md](../AGENTS.md), [README.md](../README.md), the latest [implementation checklist](IMPLEMENTATION_CHECKLIST.md), and [validation](VALIDATION.md).
2. Inspect **actual current** branch/head, open PRs and CI before coding. Source and running tests override stale prompts or checkboxes.
3. Examine existing Next.js/LiveKit and Python agent code; **do not rebuild the voice foundation** or copy another whole tutor app.
4. Check whether [PR #1](https://github.com/Planeshiffhter/eng-teacher/pull/1) was merged. If yes, consider its state-machine changes already implemented. If still open, base further work carefully on the right branch and avoid duplicate fixes.
5. Preserve an **honest separation** between offline passing tests, real browser/device/provider tests and unimplemented features.
6. Change one useful vertical slice at a time, with focused regression tests, no secrets and measured status.
7. Update this handoff's snapshot and the existing checklist/validation whenever a milestone materially changes. Add a commit and PR link.
8. Prefer the next unblocked engineering task: privacy-safe model usage and error counters, then real bilingual speech acceptance. Do not spend entire work sessions inventing new plans.

**Owner's recurring request:** Make the project self-contained in GitHub because long ChatGPT conversations can become inaccessible. A new engineer should learn the goal, work done, evidence and next steps from the repository alone. The owner wants working commits and reproducible tests, not a perpetual planning-only effort.

## 2. The mission and product differentiator

Build an **independently controlled, commercially viable AI English-speaking teacher**, beginning with learners who speak Hindi and English (including Hinglish). Eventually support additional Indian languages once validated by speakers.

### Competitor feature benchmarks, not permission to copy

| Benchmark | Experience to learn from | Our original product goal |
| --- | --- | --- |
| Praktika | Natural avatar-led two-way conversations | Original animated teacher, interruptible real voice |
| ELSA Speak | Audio-based pronunciation feedback | Validated word/phoneme feedback based on the learner's actual audio |
| Speak | Speaking-first adaptive coaching | Personal follow-ups, natural error correction and conversation |
| Duolingo | Structured lessons and progression | CEFR-oriented original content, exercises, meaningful review |
| Supernova | Indian-language English tutoring workflow | Useful Hindi explanations and later regional language support |

Our **measurable differentiator** is learning effectiveness: preserve the learner's meaning while correcting one important issue; let them ask questions in Hindi/English, retry, and use the improved pattern independently the next day. A cosmetic avatar alone is not the product advantage.

### Intended eventual feature scope

- Real-time tutor conversations, optional character/avatar/lip sync, teacher speech/listening/idle behavior and audio-only fallback.
- Correct handling of Hindi-English code-switching, long pauses and Indian English accents.
- Grammar, vocabulary, phrase examples and useful meaning-preserving corrections.
- Separate, **audio-grounded** pronunciation coaching: do not assign pronunciation scores from transcript similarity.
- Interview, workplace, shopping, travel, everyday conversation and scenario roleplays.
- Short exercises, CEFR-aligned learner goals/placement, progress and spaced retrieval.
- Secure account/login, consented personal history, exports/deletion, dashboard and accessibility.
- Provider abstraction, measured operating costs and eventually independently hosted/fine-tuned models when justified.
- Original characters, artwork, curricula and brand; do not reproduce proprietary competitor assets.

**First measurable pilot:** One ten-minute, mobile-browser, Hindi-English mock job interview. Real two-way speech; one meaningful correction; learner may ask for Hindi/English help, repeat or another example; can retry and continue; readable subtitles and recap; audio-only initially; privacy-safe usage metering; real-device validation required.

## 3. Recoverable chat and engineering timeline

This is a project-focused chronology reconstructed from available chat context and committed documents. It **does not pretend to include full private-chat transcripts**.

| Date | Discussion / request | Recorded outcome and evidence |
| --- | --- | --- |
| **13 Nov 2026** | Feasibility of building a Praktika/ELSA/Speak/Duolingo-class original tutor; could it be achieved and what should change? | Agreed to a narrow ten-minute Hindi-English voice pilot while retaining long-term commercial scope. Astra feasibility summary saved in [ASTRA_HANDOFF.md](ASTRA_HANDOFF.md). |
| **13 Nov 2026** | User requested a complete project prompt and full ordered implementation checklist; wanted Codex to make code, not just a plan. | [CODEX_MASTER_BUILD_PROMPT.md](CODEX_MASTER_BUILD_PROMPT.md), [CODEX_IMPLEMENTATION_BRIEF.md](CODEX_IMPLEMENTATION_BRIEF.md), [IMPLEMENTATION_CHECKLIST.md](IMPLEMENTATION_CHECKLIST.md). |
| **13 Nov 2026** | First source implementation and tests, using official LiveKit starters plus a tutor policy. | Browser app, Python agent, limited access-code session route, data events, ten-minute deadline, fake/offline tests. [Architecture](ARCHITECTURE.md), [Dependency audit](DEPENDENCY_AUDIT.md), [Validation](VALIDATION.md). |
| **13 Nov 2026** | A bug was found: asking “Please explain that in Hindi” after a correction consumed a pending speaking retry and advanced the question. | Fixed in the code on main before the Nov 16 audit; existing [earlier fix commit](https://github.com/Planeshiffhter/eng-teacher/commit/aacc0e78a16ed0cb7bdaa6490e837f69ce6a9d82) and regression tests. **Do not reimplement this older fix.** |
| **15 Nov 2026** | Request to find all study repositories and persist the list in GitHub; check PRs and merges. | [OPEN_SOURCE_REPOSITORIES.txt](../OPEN_SOURCE_REPOSITORIES.txt) lists **21 verified public GitHub repositories** with purpose, priority and licensing cautions. Commit [43dca05](https://github.com/Planeshiffhter/eng-teacher/commit/43dca05d43d931498ae15db6288822a5336f8e7c). |
| **15–16 Nov 2026** | Principal-engineer deep-research mission: audit full current project, deeply inspect Cadence and Talking Avatar, **implement next unblocked change**, test and push PR. | Investigated source and reference revisions; implemented safer pending-retry semantics and recoverable errors on [PR #1](https://github.com/Planeshiffhter/eng-teacher/pull/1). Final PR run [43749668384](https://github.com/Planeshiffhter/eng-teacher/actions/runs/43749668384) passed. Pinned research: [TWO_PRIMARY_REFERENCE_REPOS.md on PR branch](https://github.com/Planeshiffhter/eng-teacher/blob/feat/tutor-retry-intents-and-reference-audit/docs/TWO_PRIMARY_REFERENCE_REPOS.md). **PR remains separate from main until actually merged.** |
| **16 Nov 2026** | Owner requested all important project chat research, diagrams, links and progress to be permanently stored in GitHub to allow seamless future continuation. | **This living document** provides the consolidated resume point, while canonical specs, code, test evidence and the 21-repo inventory remain separately linked. |

### Key early feasibility conclusions (proposals, not achieved metrics)

- Prefer mobile web over immediately building native Android or desktop.
- Reuse LiveKit React and Python Agents first; initially trial OpenAI multilingual speech adapters, later compare Sarvam for mixed Hindi-English and accents.
- Trial Talking Avatar **only after reliable audio**, with visual fallback. Reuse Cadence/Sprigo teaching patterns selectively; defer an entire second voice engine, phoneme scoring models and fine-tuning.
- Suggested first evaluation: **30** teacher-reviewed mixed-language utterances and **20** already-acceptable English utterances. Initial proposed gates: at least **27/30** meaning-preserved and no more than **1/20** false corrections, subject to later rubric/teacher review. Not measured yet.
- Initial pilot idea: 20 consenting adult learners, three sessions each; measure next-day unprompted usage, willingness to return, teacher accuracy and real cost. These were planning targets, **not completed studies**.
- Proposed median latency under 2 seconds end-of-speech to first audible reply; this is a goal, **not a benchmark result**.
- An old illustrative Sarvam speech estimate from the feasibility note was **₹8.45 per 10-minute lesson** with 5 billed input minutes and 2,000 TTS characters, or **₹10.90** with 10 billed input minutes. These are historical assumptions, **NOT current quotes**; exclude LLM, LiveKit, tax, hosting, failed sessions and other costs. Revalidate actual prices before budgeting.

## 4. Architecture: what exists vs what is aspirational

### Current data path — shipped source, live-provider quality unverified

~~~mermaid
flowchart TD
  A["Learner browser microphone<br/>Next.js / React"] --> B["LiveKit WebRTC room"]
  B --> C["Python LiveKit AgentSession<br/>Silero VAD / turn handling"]
  C --> D["OpenAI multilingual STT<br/>raw recognized words"]
  D --> E["InterviewTutor<br/>question + pending correction + history"]
  E --> F["ModelDecision and retry/help policy<br/>OpenAI text model adapter"]
  F --> G["OpenAI TTS"]
  G --> H["LiveKit teacher audio"]
  H --> I["RoomAudioRenderer<br/>browser speaker"]
  E --> J["Versioned reliable data events"]
  J --> K["Feedback cards + subtitles + recap<br/>browser memory only"]
~~~

**Audio truth:** This pipeline is present in code. Offline test fakes do **not** demonstrate real speech accuracy, interruption quality, Android behavior, natural Hindi TTS or total cost.

### Future product extensions — NOT implemented by this flowchart

~~~mermaid
flowchart LR
  Core["Existing LiveKit + InterviewTutor"] --> Lesson["Original guided lessons and placement"]
  Core --> Avatar["Single-owner audio-driven avatar trial"]
  Core --> Assess["Audio-based pronunciation assessor<br/>human-calibrated"]
  Lesson --> Progress["Consented saved progress + FSRS"]
  Progress --> Accounts["Secure auth / exports / deletion"]
  Core --> Eval["Evaluation + usage and latency metrics"]
  Eval --> Models["Evaluate self-hosting / LoRA only if justified"]
~~~

### Current code map

| Path (GitHub main unless indicated) | Responsibility and important constraint |
| --- | --- |
| [apps/web/components/tutor-app.tsx](../apps/web/components/tutor-app.tsx) | Next.js React room UI, microphone permission, join/end, mute, presence waveform, live captions, correction/recap cards; **audio-only**, not actual face animation. |
| [apps/web/lib/tutor-events.ts](../apps/web/lib/tutor-events.ts) | Versioned room packet schema, feedback/action validation, replay deduplication, bounded history and browser time caps. PR #1 extends recoverable error packets. |
| [apps/web/lib/server/session.ts](../apps/web/lib/server/session.ts) | Server-only LiveKit token signing, restricted mic publishing, named worker dispatch, strong pilot code/origin checks, process-local request budget and signed deadline. **Not public SaaS auth.** |
| [apps/web/app/api/session/route.ts](../apps/web/app/api/session/route.ts) | POST endpoint issues bounded, no-store, room-specific join token; provider secrets remain server-side. |
| [services/voice-agent/src/eng_teacher/agent.py](../services/voice-agent/src/eng_teacher/agent.py) | LiveKit AgentServer / AgentSession, greeting, no-recording flags, VAD, interruption, deadline cleanup and room deletion, usage metrics; PR #1 adds recoverable error handling. |
| [services/voice-agent/src/eng_teacher/tutor.py](../services/voice-agent/src/eng_teacher/tutor.py) | Provider-independent interview questions, correction state, validated feedback, meaning/name/number/negation guard, retry logic; **main vs PR #1 differs materially**. |
| [services/voice-agent/src/eng_teacher/controls.py](../services/voice-agent/src/eng_teacher/controls.py) | Explicit Hindi/English teaching assistance, retry, repeat and skip controls; PR #1 adds example and Hindi-translation requests. |
| [services/voice-agent/src/eng_teacher/providers.py](../services/voice-agent/src/eng_teacher/providers.py) | Replaceable OpenAI STT, TTS and structured tutor decision adapter; no production support for a second provider yet. PR #1 adds semantic retry check and example/translation help. |
| [services/voice-agent/tests/](../services/voice-agent/tests/) | Python tutor, provider/SDK scheduler and worker lifecycle tests; tests use fakes/silent synthetic audio, not live speech. |
| [apps/web/tests/](../apps/web/tests/) | Vitest token/session boundary and versioned event/unit tests. |
| [tests/browser/lesson.spec.ts](../tests/browser/lesson.spec.ts) | Playwright desktop/mobile viewport smoke, synthetic Chromium microphone, expected missing-config and failed-room recovery. |
| [.github/workflows/checks.yml](../.github/workflows/checks.yml) | npm install/tests/build/typecheck, frozen uv + pytest, Ruff, Playwright; PR #1 adds Ruff formatting check. |
| [package.json](../package.json), [apps/web/package.json](../apps/web/package.json), [services/voice-agent/pyproject.toml](../services/voice-agent/pyproject.toml) | Node 24 workspaces / Next.js 15 / React 19 / LiveKit packages, Python >=3.11,<3.14 and pinned SDK via uv lock. Consult actual lockfiles. |

### Core policies and state invariants

- One ten-minute interview room with an initial server-signed deadline; a browser reconnect **must not** mint another ten minutes. Room closed/deleted on deadline/disconnect/fatal error.
- The learner's **recognized original transcript** and **model-suggested correction** must never be conflated. Never silently rewrite proper nouns, quantities or negation.
- Give at most one worthwhile correction per turn, tolerate already-acceptable Indian English, ask for clarification when ASR/meaning is uncertain.
- A pending correction remains pending after “explain in Hindi/English”, “repeat”, “try again”, “give an example”, “translate” or a genuine clarification question.
- Do **not** auto-advance on arbitrary text: a retry must be genuine. Paraphrases may be acceptable if meaning/entities are preserved. Exact text match is not a pronunciation judgment.
- An explicit skip/next request intentionally moves on. No speculative generation may corrupt session state.
- Separate provider errors that are genuinely recoverable from fatal errors; avoid abandoning a billed lesson unnecessarily.
- Raw audio and recordings are not persisted by the app by default; current session transcript/feedback is bounded and in memory. External provider retention and terms must be reviewed separately.
- Only an actual teacher-audio track may drive a future avatar; **never attach the learner mic** to it, and never play one track through two audio outputs.

## 5. Implementation status — do not interpret roadmap tasks as shipped

| Capability | Main as of 88f600d | PR #1 | Live/production acceptance |
| --- | --- | --- | --- |
| Next.js mobile-responsive entry and audio room | Source present | Preserved | Real Android and live network still needed |
| LiveKit restricted session tokens, named worker, ten-minute cap | Source and deterministic tests | Preserved | Real provider lifecycle needed |
| STT → tutor → TTS audio pipeline | Integrated in code | Preserved | **UNVERIFIED with actual speech** |
| Captions, original/suggested cards, recap | Source and offline/browser tests | Preserved | Real connected session still needed |
| Hindi explanation, repeat, retry-again, skip control bug | **Fixed and regression-tested on main** | Preserved | Natural spoken request variants still need evaluation |
| Example/translation requests and unrecognized follow-up questions | Missing/unsafe for pending correction | **Implemented/tested on PR only** | Broader free-form Hinglish requests still unverified |
| Meaning-aware nonidentical retries | Old behavior could advance on any non-control text | **Strict text-only decision + guards on PR** | Model quality and audio recognition unverified |
| Recoverable speech errors shown without ending call | Old UI treated tutor errors as fatal | **Updated on PR** | Real provider recovery not demonstrated |
| STT seconds and TTS character usage | Partial private aggregate logging | Preserved | Missing total LLM tokens and real billing totals |
| Browser avatar and lip sync | **Not implemented** | Research only | Single-owner audio experiment + Android profiling |
| Audio-based pronunciation grade | **Not implemented** | Research only | Human-reviewed audio scoring required |
| Original structured guided lesson catalog | **Not implemented** | Design references only | Author one vertical slice |
| Login, persistent progress, FSRS, learner history/deletion | **Not implemented** | Not added | Design secure consent and storage |
| Multilingual beyond Hindi/English, native Android, model fine-tuning | **Not implemented** | Not added | Later evidence-based phases |

## 6. High-priority dialogue examples to retain as regression/evaluation cases

| Learner turn | Desired teacher action | Question advancement? |
| --- | --- | --- |
| “Maine customer calls handle kiye” | Preserve recognized original, suggest an appropriate English version with one explanation if needed | Wait for retry if corrected |
| “Please explain that in Hindi” | Explain current correction in Hindi; keep the correction | **No** |
| “Please explain that in English” | Explain the same saved correction in English | **No** |
| “Can you repeat the correct sentence?” | Repeat saved correction | **No** |
| “Could you give me an example?” | Give a brief, truthful example; no invented learner facts | **No** |
| “Translate that into Hindi” | Faithful Hindi translation of the saved sentence | **No** |
| “One more try, please” | Give learner another attempt | **No** |
| “Why is that correct?” | Treat as help/clarification rather than a completed retry | **No** |
| Exact corrected sentence | Accept as text retry; no phoneme/pronunciation claim | Yes, when appropriate |
| Natural meaning-equivalent paraphrase | Evaluate intent/meaning with clear uncertainty fallback; do not require verbatim match | Yes only if accepted |
| Unrelated response, uncertain STT or invalid meaning change | Keep correction, clarify and/or offer example; do not mis-grade | **No** |
| “Skip this question” | Explicitly clear pending correction and advance once | **Yes** |
| Learner changes “didn't” to affirmative, 12 to 20, or “Rohan” to “Rahul” | Reject unsafe semantic claim or clarify | **No** |
| Already good regional English | Continue without manufacturing grammar mistakes | Yes if genuinely answered |
| Provider fails during retry explanation | Sanitized recoverable message; keep state, never expose payload | **No** |

**Remaining gaps:** More varied spoken Hinglish intent classification (especially forms not matching regex), pause/end learner controls, provider timeout/interrupt race conditions, third-party evaluator review of output. Do not mark these solved merely because deterministic tests pass.

## 7. The 16 November two-reference deep research

**Selection rule:** Study **exactly two additional primary repositories**, Cadence and Talking Avatar, alongside the already integrated LiveKit starter foundation. See the detailed [pinned-source report in PR #1](https://github.com/Planeshiffhter/eng-teacher/blob/feat/tutor-retry-intents-and-reference-audit/docs/TWO_PRIMARY_REFERENCE_REPOS.md). If PR is merged, the same report will be available at docs/TWO_PRIMARY_REFERENCE_REPOS.md on main. Avoid importing unrelated second voice engines or infrastructure.

### A. Cadence — ADOPT teaching patterns, DEFER heavyweight scoring

- Repo: https://github.com/pstepanovum/Cadence
- Inspected revision: [e97a87584716868925ea94fc0e540f3cf309a2f8](https://github.com/pstepanovum/Cadence/tree/e97a87584716868925ea94fc0e540f3cf309a2f8), 8 Nov 2026. Root [MIT license](https://github.com/pstepanovum/Cadence/blob/e97a87584716868925ea94fc0e540f3cf309a2f8/LICENSE); read [NOTICE](https://github.com/pstepanovum/Cadence/blob/e97a87584716868925ea94fc0e540f3cf309a2f8/NOTICE).
- Architecture: Next.js 16 / React 19, Firebase, FastAPI ai-engine and coach-engine, optional Electron/mobile. Existing Eng Teacher must not add duplicate Firebase/Stripe/desktop/coach services just to use lesson ideas.
- [src/lib/conversation.ts](https://github.com/pstepanovum/Cadence/blob/e97a87584716868925ea94fc0e540f3cf309a2f8/src/lib/conversation.ts): module metadata (scenario, level, focus, expected response, coaching cue, ordered turns). [ConversationSession.tsx](https://github.com/pstepanovum/Cadence/blob/e97a87584716868925ea94fc0e540f3cf309a2f8/src/components/conversation/ConversationSession.tsx): explicit intro/coach/record/assess/result/done workflow. [PracticeLesson.tsx](https://github.com/pstepanovum/Cadence/blob/e97a87584716868925ea94fc0e540f3cf309a2f8/src/components/learn/PracticeLesson.tsx): targeted attempts, progression, feedback.
- [phoneme_scorer.py](https://github.com/pstepanovum/Cadence/blob/e97a87584716868925ea94fc0e540f3cf309a2f8/src/backend/ai-engine/phoneme_scorer.py) uses decoded audio/Wav2Vec2 phoneme processing; [speech_transcriber.py](https://github.com/pstepanovum/Cadence/blob/e97a87584716868925ea94fc0e540f3cf309a2f8/src/backend/ai-engine/speech_transcriber.py) defaults to **English-only** Whisper base, not a direct Hinglish STT replacement.
- [Pronunciation types](https://github.com/pstepanovum/Cadence/blob/e97a87584716868925ea94fc0e540f3cf309a2f8/src/lib/pronunciation.ts) distinguish transcript, target, phonemes and timing. [Endpoint tests](https://github.com/pstepanovum/Cadence/blob/e97a87584716868925ea94fc0e540f3cf309a2f8/src/backend/ai-engine/tests/test_endpoints.py) validate upload limitations using fakes, **not** human pronunciation accuracy. [Requirements](https://github.com/pstepanovum/Cadence/blob/e97a87584716868925ea94fc0e540f3cf309a2f8/src/backend/ai-engine/requirements.txt) include Torch/Transformers and model runtime overhead; check weight/voice licenses separately.
- Maintenance evidence: Nov 8 commits, wide CI (web/desktop/mobile/secret scanning), tests. No full local Cadence runtime/benchmarks performed.
- **Practical integration:** write one **original** guided speaking module/lesson-definition test in existing Eng Teacher architecture. Do not copy Cadence lesson text or bulk code. Audio pronunciation adapter comes later, with human-calibrated recordings and distinct scores.

### B. Talking Avatar — TRIAL only with one audio owner

- Repo: https://github.com/InterviewFlowAI/talking-avatar
- Inspected revision: [d3e4dcf6609d733097466eb17b3fa63fc720140a](https://github.com/InterviewFlowAI/talking-avatar/tree/d3e4dcf6609d733097466eb17b3fa63fc720140a), 2 Nov 2026; [MIT SDK](https://github.com/InterviewFlowAI/talking-avatar/blob/d3e4dcf6609d733097466eb17b3fa63fc720140a/LICENSE), [Rocketbox avatar asset attribution](https://github.com/InterviewFlowAI/talking-avatar/blob/d3e4dcf6609d733097466eb17b3fa63fc720140a/avatars/LICENSE). Independently check model-training data, model binary and commercial redistribution rights.
- Browser [TalkingAvatar.ts](https://github.com/InterviewFlowAI/talking-avatar/blob/d3e4dcf6609d733097466eb17b3fa63fc720140a/src/TalkingAvatar.ts) attaches a real MediaStream, analyzes audio via AudioWorklet and client-side viseme inference, then **plays it itself** through AudioContext.destination with a default approximately 150 ms stream delay.
- [React wrapper](https://github.com/InterviewFlowAI/talking-avatar/blob/d3e4dcf6609d733097466eb17b3fa63fc720140a/src/react.tsx) accepts stream and listening/thinking status. [Viseme model](https://github.com/InterviewFlowAI/talking-avatar/blob/d3e4dcf6609d733097466eb17b3fa63fc720140a/src/visemeModel.ts), [detector](https://github.com/InterviewFlowAI/talking-avatar/blob/d3e4dcf6609d733097466eb17b3fa63fc720140a/src/visemeDetector.ts), [renderer](https://github.com/InterviewFlowAI/talking-avatar/blob/d3e4dcf6609d733097466eb17b3fa63fc720140a/src/renderer.ts) drive mouth shapes, blinking and brows. [Tests](https://github.com/InterviewFlowAI/talking-avatar/blob/d3e4dcf6609d733097466eb17b3fa63fc720140a/test/visemeModel.test.ts) include model parity fixture; no Eng Teacher integration validation.
- React peer >=18, Three >=0.160; ESM/browser/WebGL/WebAudio. Do not assume Android CPU/GPU or battery performance from upstream README claims.
- **CRITICAL:** Eng Teacher currently uses LiveKit RoomAudioRenderer to play teacher audio. Calling avatar.attachStream on the same track while RoomAudioRenderer also plays it can **double audio** and impair lip sync, interruptions and mute. Select only the LiveKit *agent remote audio track* and choose exactly **one** playback owner. Keep audio-only fallback if avatar fails, and test interruptions, reconnects, browser autoplay, cleanup, microphone permissions and low-end Android first.
- Trial decision only: **no avatar SDK dependency, weights, GLB assets, second RTC or production server added by PR #1**.

### Why these two over the other 19

Of 21 recorded public references, the two LiveKit starters are **already** the core implementation. The remaining repositories supply infrastructure alternatives, narrower speech libraries, later-stage auth/learning memory, model training or overlapping whole tutor apps. Cadence best informs structured teaching quality; Talking Avatar best addresses optional speech-synchronized visual presentation. Neither is a reason to replace the existing voice stack.

## 8. All 21 public study repositories — complete archive index

Source of truth for these labels and caveats: [OPEN_SOURCE_REPOSITORIES.txt](../OPEN_SOURCE_REPOSITORIES.txt), checked 15 Nov 2026. **License labels are repository-level summaries, not complete commercial rights audits.**

| # | Public repository | Study focus | Status |
| --- | --- | --- | --- |
| 01 | [LiveKit React starter](https://github.com/livekit-examples/agent-starter-react) | Next.js/WebRTC room UI/captions | **Already integrated core** |
| 02 | [LiveKit Python starter](https://github.com/livekit-examples/agent-starter-python) | AgentServer/AgentSession audio pipeline | **Already integrated core** |
| 03 | [LiveKit Server](https://github.com/livekit/livekit) | Optional self-hosted RTC | Later |
| 04 | [Pipecat examples](https://github.com/pipecat-ai/pipecat-examples) | Alternative voice-agent orchestration | Study only; no second engine |
| 05 | [Talking Avatar](https://github.com/InterviewFlowAI/talking-avatar) | Audio-driven browser visemes, face animation | Primary **trial** |
| 06 | [Three-VRM](https://github.com/pixiv/three-vrm) | Alternate VRM avatar renderer | Only if needed |
| 07 | [Faster-Whisper](https://github.com/SYSTRAN/faster-whisper) | Self-hosted STT alternative | Benchmark later |
| 08 | [Kokoro](https://github.com/hexgrad/kokoro) | Self-hosted TTS alternative | Benchmark later |
| 09 | [Cadence](https://github.com/pstepanovum/Cadence) | Guided speaking and audio scoring design | Primary **learning reference** |
| 10 | [Sprigo](https://github.com/ozerozdas/sprigo) | Lesson/roleplay/progression patterns | Study only |
| 11 | [AI English Conversation Tutor](https://github.com/Yurikada/ai-english-conversation-tutor) | Ollama/FastAPI speaking tutor | Study only |
| 12 | [ThirtyTutors](https://github.com/wiss84/thirtytutors) | Multiple avatar-tutor concepts | **Noncommercial license; do not copy** |
| 13 | [FreeSurf Language Tutor](https://github.com/freesurf-ecosystem/language-tutor) | Mobile language tutor concepts | **GPL + additional terms; legal review** |
| 14 | [OpenPronounce](https://github.com/Halleck45/OpenPronounce) | Audio phoneme scoring | Human-calibrated trial later |
| 15 | [TS-FSRS](https://github.com/open-spaced-repetition/ts-fsrs) | Spaced repetition | Add after consented progress |
| 16 | [Promptfoo](https://github.com/promptfoo/promptfoo) | Prompt and model evaluations | Add with reviewed test corpus |
| 17 | [Supabase](https://github.com/supabase/supabase) | Secure auth/database option | Choose one backend later |
| 18 | [Unsloth](https://github.com/unslothai/unsloth) | Efficient LoRA tuning | Later; review model/component licenses |
| 19 | [vLLM](https://github.com/vllm-project/vllm) | Self-hosted LLM inference | Later, if economics justify |
| 20 | [LiveKit Android starter](https://github.com/livekit-examples/agent-starter-android) | Native Android LiveKit interface | Later option |
| 21 | [LiveKit React Native starter](https://github.com/livekit-examples/agent-starter-react-native) | Expo/React Native mobile interface | Later alternative |

Additional non-GitHub references: [Sarvam AI](https://www.sarvam.ai/) (candidate Indian-language speech provider, **not adopted**), [Qwen3.5-4B model card](https://huggingface.co/Qwen/Qwen3.5-4B) (possible future base model, **not trained here**). Feature benchmarks: Praktika, ELSA Speak, Speak, Duolingo, Supernova.

## 9. GitHub evidence: branches, commits and tests

| Artifact | Link | Meaning |
| --- | --- | --- |
| Last audited main | [88f600d](https://github.com/Planeshiffhter/eng-teacher/commit/88f600d3176a943d355deb9db4490a6387523fad) | Source baseline as of 15 Nov 2026 |
| Main CI | [Run 43712040973](https://github.com/Planeshiffhter/eng-teacher/actions/runs/43712040973) | Main offline tests passed |
| 21-repo catalog commit | [43dca05](https://github.com/Planeshiffhter/eng-teacher/commit/43dca05d43d931498ae15db6288822a5336f8e7c) | Reference catalog on main |
| Original Hindi-control fix | [aacc0e7](https://github.com/Planeshiffhter/eng-teacher/commit/aacc0e78a16ed0cb7bdaa6490e837f69ce6a9d82) | Earlier bug was fixed before current PR |
| Proposed engineering PR | [PR #1](https://github.com/Planeshiffhter/eng-teacher/pull/1) | More robust help/semantic retry and error behavior |
| Tested PR head | [da2796e](https://github.com/Planeshiffhter/eng-teacher/commit/da2796ebaca461c7ac0551182bfb7534f8498551) | 16 Nov snapshot, **not merged** |
| Passing PR CI | [Run 43749668384](https://github.com/Planeshiffhter/eng-teacher/actions/runs/43749668384) | 14 Vitest, 56 Python pytest, Ruff check and format, Next build, TS typecheck, 6 Playwright tests all passed |
| Two-repository audit | [PR branch report](https://github.com/Planeshiffhter/eng-teacher/blob/feat/tutor-retry-intents-and-reference-audit/docs/TWO_PRIMARY_REFERENCE_REPOS.md) | Pinned code, model/asset license caveats, audio ownership |
| Main history | [Commits](https://github.com/Planeshiffhter/eng-teacher/commits/main/) | Always check again |
| PR queue | [Pull requests](https://github.com/Planeshiffhter/eng-teacher/pulls) | Always check for new changes |
| CI history | [Actions](https://github.com/Planeshiffhter/eng-teacher/actions) | Do not assume a passing prior run covers new commits |

**Precise CI interpretation:** Those 14 + 56 + 6 tests are the successful final PR CI run, **not** human speech, live provider quality, pronunciation, face animation, physical Android profiling or billing verification. Earlier failures prompted strict boolean schema changes and Ruff formatting; the final verified run succeeded.

## 10. Reproducible development and test commands

Read [DEVELOPMENT.md](DEVELOPMENT.md) for current setup. Validate scripts and lockfiles before rerunning.

From repo root, using Node.js **24.x**, Python **3.12 recommended** and uv:

~~~bash
npm ci
uv sync --frozen --project services/voice-agent
npm test
npm run test:agent
uv run --frozen --project services/voice-agent ruff check services/voice-agent
uv run --frozen --project services/voice-agent ruff format --check services/voice-agent
npm run typecheck
npm run build
npx playwright install chromium
npm run test:browser
~~~

To operate a **real** lesson, separately configure ignored environment files using [apps/web/.env.example](../apps/web/.env.example) and [services/voice-agent/.env.example](../services/voice-agent/.env.example). Do **not** put values into README, issues, Git commits, PR logs or this handoff. Expected server-side names include LIVEKIT_URL, LIVEKIT_API_KEY, LIVEKIT_API_SECRET, OPENAI_API_KEY and PILOT_ACCESS_CODE, plus APP_ORIGIN when deployed. Start web and voice agent as separate supervised processes using the documented scripts.

Current speech defaults in [providers.py](../services/voice-agent/src/eng_teacher/providers.py): Whisper-1 STT, GPT-4.1-mini tutoring, GPT-4o-mini-TTS, configurable voice. These are provider-adapter defaults in code, **not evidence of best quality for Indian accents**, permanent model availability or pricing.

### Offline testing boundaries

- Browser tests use synthetic mic and intentionally invalid/missing connection, not a successful simulated paid lesson.
- Python agent tests include the real AgentSession scheduling path but fake the model, room or output; a generated silent frame is not real voice synthesis.
- All live acceptance tasks remain external until operator-owned credentials, real browsers and consenting speakers are available.

## 11. Full live validation to carry out before a commercial pilot

1. Run an actual HTTPS browser lesson through LiveKit, STT, InterviewTutor, TTS and speakers on desktop Chrome and **physical midrange Android**; record exact setup and observed issues without retaining raw voice by default.
2. Check mic allow/deny/re-enable, user gesture/autoplay, captions and mobile responsive layout.
3. Speak Hindi, English and mixed Hindi-English; inspect mistakes involving proper names, negation, dates/numbers, word order and Indian English accents.
4. While correction is pending, ask Hindi explanation, English explanation, example, translation and repeat *several times*; confirm no accidental question advancement.
5. Try an exact retry, equivalent paraphrase, unrelated answer and ambiguous ASR; ensure appropriate acknowledgment/clarification, never invented pronunciation grades.
6. Test long silences, speaking over tutor audio (barge-in), slow networks, reconnect, bad STT, provider timeout and recoverable/fatal failures.
7. Run until full server-enforced ten-minute deadline; verify room deletion, browser audio stop and no unauthorized extra billable time after browser reconnect.
8. Collect private aggregate usage/latency only: STT audio seconds, TTS characters, LLM input/output tokens, provider failure/retry counters, end-of-speech to first audible response p50/p90, session and billed minutes, total cost including retries.
9. Use the initial **30 mixed + 20 acceptable** human-reviewed test set as a starting rubric; proposed gates 27/30 meaning-preserved and at most 1/20 falsely corrected, not automatic release proof.
10. Confirm no raw recordings/traces/credentials/PII are committed or inadvertently logged; review retention with every third-party provider.

~~~mermaid
flowchart TD
  A["Deterministic unit / schema / browser checks"] --> B{"Passing?"}
  B -- No --> C["Fix code and regressions"]
  C --> A
  B -- Yes --> D["Owner-configured live voice test"]
  D --> E["Human-reviewed bilingual acceptance"]
  E --> F["Actual cost + latency + security review"]
  F --> G{"Product quality and cost acceptable?"}
  G -- No --> H["Target measured failures and re-test"]
  H --> D
  G -- Yes --> I["Controlled pilot, then larger platform milestones"]
~~~

### Important cost and security boundaries

- The current pilot access code and in-process request budget are **not** production-grade user auth, per-account quotas or distributed rate limiting.
- Signed room-specific tokens permit learner microphone publishing, not arbitrary publishing or room selection.
- Recording is off by default, recap is browser memory-only, and provider processes still handle learner audio/text. Do not promise provider-side zero retention without contract evidence.
- Before public paid launch: secure auth, distributed quotas/spending caps, reliable retry/error metrics, retention/deletion, regulatory/age/accessibility review and infrastructure monitoring.
- No fake learning completion, invented spoken quality scores or training claims.

## 12. Ordered development path and gates

~~~mermaid
flowchart TD
  P0["P0: Existing LiveKit MVP + baseline CI"] --> P1["P1: Correct and reliable teaching state<br/>PR #1 ready for review"]
  P1 --> P2["P2: Privacy-safe usage + real 10-minute bilingual audio"]
  P2 --> P3["P3: Original guided speaking exercise<br/>Cadence-inspired structure"]
  P3 --> P4["P4: Isolated audio-driven avatar trial<br/>single playback owner"]
  P4 --> P5["P5: Validated audio pronunciation practice"]
  P5 --> P6["P6: Secure learner accounts + progress + consent"]
  P6 --> P7["P7: Adaptive lessons, additional languages and FSRS"]
  P7 --> P8["P8: Measured economics then independent models/native apps"]
~~~

| Order | Next increment | Required acceptance |
| --- | --- | --- |
| 1 | **Review/merge PR #1 when actually safe** | Fresh head/base, green CI, meaningful review; never force-push or overwrite |
| 2 | Add **privacy-safe** tutor-model token totals and errors to Python worker | Tests for aggregate counters, no transcripts or payload logging, proper cleanup |
| 3 | Run real Hindi-English ten-minute lesson and gather latency/billing | Real provider credentials and actual microphone/speaker evidence |
| 4 | Define one **original** structured exercise, guided target, example and repeat | Content validation and state-transition tests |
| 5 | Trial Talking Avatar with teacher track and one playback owner | Single sound source, no latency/interrupt regression, fallback, Android |
| 6 | Add audio-based pronunciation feedback as a separate assessor | Consent + teacher-calibrated audio evidence across accents |
| 7 | Add secure individual accounts, learner opt-in saved lessons and deletion | Correct authorization, retention, export/delete, no raw recording by default |
| 8 | Expand CEFR scenarios, spaced review and localization | Useful learning outcomes and original content |
| 9 | Compare model hosting/LoRA and native app only on measured need | Proven licensing, permissioned datasets, evaluation holdout, real compute cost |

## 13. Canonical document inventory (all links)

**Do not create competing giant instruction files on every session.** Keep these canonical documents and update them with actual engineering evidence.

| File | Role | Status caution |
| --- | --- | --- |
| [README.md](../README.md) | Entry point and project state | Some first-MVP language predates PR #1 |
| [AGENTS.md](../AGENTS.md) | Rules for every coding agent | Read before all code changes |
| [PRODUCT_VISION.md](PRODUCT_VISION.md) | Product scope and differentiation | Product goals, not shipped features |
| [ASTRA_HANDOFF.md](ASTRA_HANDOFF.md) | Earlier feasibility and costs | Historical proposal, not current quotes |
| [ARCHITECTURE.md](ARCHITECTURE.md) | Current slice + target future stack | Illustrates future modules not built |
| [ROADMAP.md](ROADMAP.md) | Planned milestones | Contains older “initially docs only” assumptions |
| [IMPLEMENTATION_CHECKLIST.md](IMPLEMENTATION_CHECKLIST.md) | Ordered acceptance tasks and status | Check PR merge and test evidence |
| [MVP_AND_ACCEPTANCE.md](MVP_AND_ACCEPTANCE.md) | Pilot acceptance rubric | No live quality score achieved yet |
| [CODEX_MASTER_BUILD_PROMPT.md](CODEX_MASTER_BUILD_PROMPT.md) | Long-term engineering directive | Contains an **outdated immediate Hindi retry bug** instruction: FIXED earlier |
| [CODEX_IMPLEMENTATION_BRIEF.md](CODEX_IMPLEMENTATION_BRIEF.md) | Shorter Codex handoff | Not a substitute for real code inspection |
| [DECISIONS.md](DECISIONS.md) | Decisions and reasons | PR branch contains 16 Nov research updates |
| [VALIDATION.md](VALIDATION.md) | Tests, credentials and live blockers | Historical counts change after PR merges |
| [DEVELOPMENT.md](DEVELOPMENT.md) | Local/test/worker startup | Use actual scripts and env examples |
| [DEPENDENCY_AUDIT.md](DEPENDENCY_AUDIT.md) | LiveKit/OpenAI/Silero license audit | Not total commercial licensing audit |
| [OPEN_SOURCE_STACK.md](OPEN_SOURCE_STACK.md) | Earlier reuse shortlist | Superseded for completeness by 21-repo catalog |
| [OPEN_SOURCE_REPOSITORIES.txt](../OPEN_SOURCE_REPOSITORIES.txt) | **All 21** references and warnings | Verified 15 Nov 2026, recheck upstream changes |
| [TWO_PRIMARY_REFERENCE_REPOS.md (PR #1)](https://github.com/Planeshiffhter/eng-teacher/blob/feat/tutor-retry-intents-and-reference-audit/docs/TWO_PRIMARY_REFERENCE_REPOS.md) | Detailed Cadence / Talking Avatar audit | Not on main until PR merges |
| [THIRD_PARTY_NOTICES.md](../THIRD_PARTY_NOTICES.md) | Attributions and licenses | Expand if importing new code/assets |
| **This file: PROJECT_CONTINUITY_HANDOFF.md** | Condensed project/research/chat continuity, architecture diagrams, resume prompt | Update alongside significant milestones |

## 14. What is stale or easily misread

- [CODEX_MASTER_BUILD_PROMPT.md](CODEX_MASTER_BUILD_PROMPT.md) described Hindi “explain that” pending-retry handling as the *next* immediate bug. Source and tests **already fixed this on main**; the newer general retry/intent improvement is in PR #1.
- [ROADMAP.md](ROADMAP.md) describes a repository “initially documentation only”. The project has an implemented Next.js UI, session server and LiveKit agent. Roadmap remains useful as a future milestone list.
- The early handoff suggested Sarvam as a first-pass speech provider. The current code actually uses OpenAI speech plugins; Sarvam remains a candidate **until measured**.
- Product goals describe an animated face, saved learner progression and pronunciation scoring; **none are currently live product features**.
- A passing CI run does not show that the actual educator conversation, voices, avatars, costs or phones have been successfully tested.
- Plans and specific dated cost examples are not purchase quotes, licensing approval or implementation proof.
- The PR #1 branch state changes only when actually merged; this file's status must not silently reclassify it as part of main.

## 15. Suggested handoff prompt for future chat/Codex

Copy the following into a new ChatGPT Work/Codex conversation if the original chat history cannot be loaded:

> Work on https://github.com/Planeshiffhter/eng-teacher within the owner's current requested scope. Start by reading AGENTS.md, PROJECT_IDEA.txt, docs/REPOSITORY_STRUCTURE.md, this handoff, README.md, OPEN_SOURCE_REPOSITORIES.txt, docs/IMPLEMENTATION_CHECKLIST.md and docs/VALIDATION.md. Inspect current main, history, prior PR status and relevant source before coding. The existing LiveKit React/Python foundation is the product; **do not rebuild it** or execute archived project scripts as normal setup. Work directly on main, without a feature branch or new PR, and push useful checkpoints at least every five minutes while editing when changes exist; never force-push. Preserve deferred material in AnalyseFuture rather than deleting it. For an authorized next implementation task, consider privacy-safe usage/error metrics and real voice validation before a Bengali-English experiment or optional avatar. Do not claim real speech, translation, pronunciation or avatar quality without the appropriate service, speaker and device evidence. Keep historical results distinct from current validation.

## 16. How to update this file responsibly

When you finish meaningful work, amend **the snapshot first**: date, main SHA, open/merged PRs, latest CI, proven implemented features, unverified features, current blockers, next smallest task. Append a short changelog line with links; do not delete old historical evidence just because status advances. Keep secrets, user identities, recordings, private conversations unrelated to the product and raw transcripts **out of this public repo**.

**Living handoff creation:** 16 Nov 2026 — consolidated available Eng Teacher project conversation summaries, 21 reference repos, two pinned research investigations, code map, test evidence, architecture diagrams, stage gates and continuation instructions. **This document is documentation, not a new implementation or live test.**

**17 Nov 2026 organization update:** Added the owner-requested detailed product idea,
documented the repository audit, moved the original ZIPs and complete upstream
snapshots into `AnalyseFuture/` without changing their bytes, retained the active
application and earlier research, and verified the offline checks recorded above.
