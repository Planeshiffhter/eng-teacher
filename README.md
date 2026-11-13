# Eng Teacher — AI English Speaking Tutor

> **Status: First voice-tutor implementation (13 November 2026), awaiting live-provider validation.** This repository now includes a mobile-responsive Next.js client and a LiveKit Python voice agent. Automated checks use fake inputs where noted; a real microphone-to-provider call, Hindi–English quality, and avatar behavior have not been validated. The planning documents remain the product goals.

**Vision:** Build an independently controlled, commercially viable AI English-speaking learning platform with a natural video-call-like teacher, accurate corrections, multilingual explanations, pronunciation practice, and personalized learning. The ambition is to compete on learning quality with Praktika, ELSA Speak, Speak, and Duolingo—not to copy their code, characters, brands, or content.

**First product to prove:** A **10-minute Hindi–English mock interview on mobile web**. A learner speaks naturally, including code-switching; an interruptible speaking avatar listens, offers one helpful meaning-preserving correction, lets the learner repeat it, continues the interview, and provides a recap.

## Run the implementation

Read [installation and startup instructions](docs/DEVELOPMENT.md), [validation results and live test checklist](docs/VALIDATION.md), and the [focused dependency audit](docs/DEPENDENCY_AUDIT.md). The monorepo has `apps/web` and `services/voice-agent`; run `npm ci` and `uv sync --frozen --project services/voice-agent`, configure the ignored environment files from their examples, then start the worker and web server in separate terminals. LiveKit and OpenAI credentials are required for a live lesson. No GPU is required.

The first slice is audio-only: live session controls, microphone publishing, configurable recognition/model/voice adapters, interruption handling, original/corrected sentence cards, speaking retries, subtitles, and a timed mock interview. No avatar or live-quality claim is made. See validation status before treating the acceptance gates as passed.

## Project links (start here)

| Document | Read it for |
|---|---|
| [Product vision](docs/PRODUCT_VISION.md) | Target learner, competitor benchmarks, full feature ambition |
| [Astra handoff](docs/ASTRA_HANDOFF.md) | Previous GPT Astra feasibility findings and constraints |
| [MVP and acceptance tests](docs/MVP_AND_ACCEPTANCE.md) | Exact first pilot and measurable quality gates |
| [Architecture](docs/ARCHITECTURE.md) | How the web app, LiveKit voice agent, tutor engine, avatar and data fit together |
| [Open-source reuse plan](docs/OPEN_SOURCE_STACK.md) | Candidate repositories, adoption decisions, licenses and verification |
| [Roadmap](docs/ROADMAP.md) | Release sequence, priorities, cost controls and risks |
| [Decision log](docs/DECISIONS.md) | Settled decisions versus open questions |
| [Codex task brief](docs/CODEX_IMPLEMENTATION_BRIEF.md) | Ready-to-use phased engineering instructions |
| [AGENTS.md](AGENTS.md) | Repository instructions for Codex and other coding agents |

## First milestone (product requirements; live acceptance pending)

Build a mobile-web interview with microphone permissions, real-time two-way voice, interruptible replies, browser avatar with audio-only fallback, live transcript, correction → retry, recap, and per-lesson cost logs. Preserve what the learner actually said separately from the suggested English. Test uncertain recognition instead of silently rewriting it.

**Recommended starting point:** LiveKit React and Python Agent starters. Trial a compatible Indian-language speech provider (Astra suggested Sarvam) and browser talking-avatar SDK. Keep providers replaceable. **Do not fork/merge multiple complete tutor apps blindly.**

## Ownership and visibility

- This is currently a **public** GitHub repository. Anyone can read the documents and any future code pushed here.
- Keep API credentials, learner recordings, personal data, proprietary training data and production secrets **out of Git**.
- Original application code can be controlled by the repository owner; third-party dependencies, code, voices, models and assets retain their own licenses. Audit licenses before copying or commercial deployment.
- If proprietary code needs to remain private, change GitHub visibility or move that code into a separate private repository before adding it.

## Current state

- [x] Product research consolidated from earlier project discussions, including Astra feasibility review.
- [x] Initial engineering documentation.
- [ ] Architecture and license audit validated against current upstream repositories.
- [x] First client/agent source implementation; live speech acceptance remains pending.
- [ ] Real-device voice and avatar testing.
- [ ] Learner pilot and pronunciation evaluation.
- [ ] Fine-tuned model and production deployment.

**Next validation:** Configure the service credentials and run the live checklist in [docs/VALIDATION.md](docs/VALIDATION.md), including Hindi–English speech, interruption, meaning preservation and a full ten-minute lesson. The current slice is an invited pilot, not a production-ready platform.
