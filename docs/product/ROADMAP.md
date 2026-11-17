# Roadmap and Resource Priorities

**Status:** planned milestones; dates are estimates, not delivery commitments.

**17 November implementation update:** original Everyday English and existing mock
interview practice are selectable end to end through signed session metadata.
Private model-token/error counters and speech totals are integrated. Current local
checks are 18 JS / 126 Python / 8 browser tests plus build/typecheck/lint/format.
This does not complete live voice, Bengali, avatar or public-service acceptance.
See [current delivery and next steps](../development/IMPLEMENTATION_STATUS.md).

## Milestone 0 — Audit the starting point

- Inspect repository status (initially documentation only) and upstream LiveKit/Avatar components.
- Validate licenses including assets/weights and live dependency APIs.
- Record key decisions, risks, test commands and provider requirements.
- Choose one hosted voice/STT path for the prototype and one avatar.
- Acceptance: executable setup instructions, dependency decisions, small smoke test, baseline cost meters planned.

## Milestone 1 — Working 10-minute speaking MVP

- Mobile-web LiveKit UI + Python voice agent.
- Hindi/English speech input, voice output, low-latency turn-taking.
- Meaning-preserving correction, clarification, retry, recap.
- Avatar and audio-only fallback.
- Secure provider configuration, basic learner-selected practice storage, usage metering.
- Run actual browser/device and bilingual teacher evaluations from the MVP doc.

## Milestone 2 — Pilot and learning-quality iteration

- Compare with one competing app on the same speaking scenario.
- Adult user pilot with explicit consent; validate 30 mixed / 20 correct evaluation set.
- Fix correction failures, accents, names, negation, silence, dropped calls.
- Evaluate next-day independent use and real lesson cost.
- Decide whether users find enough value to pay.

## Milestone 3 — Broader platform

- Placement and goal selection, CEFR-oriented curriculum, structured roleplays, progress dashboard.
- Personalized follow-up, spaced repetition, account controls and deletion.
- Gradual Bengali/Punjabi support only after language/turn-taking evaluations.
- Admin tools and payment features only after value/operations validation.

## Milestone 4 — Pronunciation and advanced avatars

- Trial audio-based pronunciation tool against qualified teacher judgments.
- Upgrade the avatar if it improves learning or retention relative to performance/cost.
- Test diverse microphones, accents, phone hardware and noisy environments.

## Milestone 5 — Independent model and scaling

- Curate consented, reviewed training data with held-out tests.
- Fine-tune a suitably licensed Qwen model with LoRA only if it beats baseline on cost/quality.
- Evaluate hosted versus self-hosted STT/TTS/LLM under concurrent load.
- Add native Android app and production scaling after core web behavior is stable.

## Avoid wasting Codex credits

1. Reuse vetted packages; do not rebuild LiveKit, STT, TTS, lip-sync, auth or FSRS unnecessarily.
2. Audit the current code before creating more files.
3. Change one vertical slice at a time; test after each feature.
4. Never label mocks as complete production features.
5. Do not start GPU fine-tuning until a verified dataset and baseline exist.
6. Preserve implementation history, decisions, environment setup and test scripts so Codex can resume without re-researching.
