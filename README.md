# Eng Teacher — AI English Speaking Tutor

> **Status: Planning / documentation only (13 November 2026).** This repository does **not yet contain a working application**. Do not interpret the roadmap as implemented features.

**Vision:** Build an independently controlled, commercially viable AI English-speaking learning platform with a natural video-call-like teacher, accurate corrections, multilingual explanations, pronunciation practice, and personalized learning. The ambition is to compete on learning quality with Praktika, ELSA Speak, Speak, and Duolingo—not to copy their code, characters, brands, or content.

**First product to prove:** A **10-minute Hindi–English mock interview on mobile web**. A learner speaks naturally, including code-switching; an interruptible speaking avatar listens, offers one helpful meaning-preserving correction, lets the learner repeat it, continues the interview, and provides a recap.

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

## First milestone (not yet implemented)

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
- [ ] Functional application code.
- [ ] Real-device voice and avatar testing.
- [ ] Learner pilot and pronunciation evaluation.
- [ ] Fine-tuned model and production deployment.

**Suggested next action:** Read [Codex task brief](docs/CODEX_IMPLEMENTATION_BRIEF.md) and ask Codex to complete **Milestone 0 (audit)**, then **Milestone 1 (working voice MVP)**. Avoid implementing an entire competitive feature list in one run.
