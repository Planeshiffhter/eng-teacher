# Agent Instructions — Eng Teacher

This file applies to coding agents working in this repository.

## First read

Read README.md and docs/PRODUCT_VISION.md, docs/ASTRA_HANDOFF.md, docs/ARCHITECTURE.md, docs/OPEN_SOURCE_STACK.md, docs/MVP_AND_ACCEPTANCE.md, docs/ROADMAP.md, docs/DECISIONS.md, docs/CODEX_IMPLEMENTATION_BRIEF.md, **docs/IMPLEMENTATION_CHECKLIST.md**, and **docs/CODEX_MASTER_BUILD_PROMPT.md**.

## Core principles

- One monorepo. Reuse proven, compatible open-source SDKs instead of recreating core infrastructure.
- Do not copy entire unrelated apps, competitor brand assets or proprietary curriculum.
- Audit **current** code, dependencies, license obligations (including model weights/assets) before importing external code.
- Prioritize a working Hindi-English 10-minute mock-interview voice vertical slice over speculative full-platform scaffolding, **but preserve the larger competitive product roadmap in the master prompt and deliver tested milestones beyond the interview**.
- Make original utterance, correction, pronunciation score and teacher explanation distinct data fields.
- Let the learner finish; if ASR/meaning is uncertain ask a clarification; correct at most one important issue per turn by default.
- Never assume the software is complete because a mock API or screenshot works.
- Preserve browser audio-only fallback if avatar fails.
- Keep credentials server-side; don't commit keys, recordings, sensitive profile data, licensed training data or production dumps.
- Recording is off by default. Obtain explicit permission for evaluation/training data.
- Test language mixing, names, negation, slow pauses, interruptions and valid regional English.
- Measure end-to-end speech latency and cost per completed lesson; don't treat assumptions as benchmarks.
- Fine-tuning must be based on permissioned, quality-reviewed data and held-out tests; no claims of training without a completed run.
- Prefer small, verifiable commits and accurate tests over broad unvalidated code generation.

## Before concluding work

Update documentation if assumptions or architecture change. Report actual tests run, outstanding API/GPU requirements, mock-only features and next smallest task. Do not silently overwrite existing working code.
