# Agent Instructions — Eng Teacher

This file applies to coding agents working in this repository.

## Current owner instructions

- The owner has now authorized incremental implementation and testing. Run the
  relevant tests, lint, format, build and browser checks for each feature. The
  preceding organization-only/no-test constraint was task-specific and is over.
  Implementation commits should run the normal CI workflow (no `[skip ci]`).
- `PROJECT_STRUCTURE.md` is the current path/ownership guide. Documentation is
  grouped by purpose under `docs`; earlier audit reports are grouped under
  `AnalyseFuture/recovery` and retain their recorded historical paths.
- Read `docs/development/IMPLEMENTATION_STATUS.md` for current delivered features,
  local validation and remaining integration work. Guided Everyday English and
  private usage counters now live in the active catalog/runtime feature modules;
  do not rebuild them from older historical TODOs.


- Work directly on `main`; do not create feature branches or new PRs for this project unless the owner changes this instruction. Never force-push shared history.
- Before starting a new task, check for existing work and commit and push any reviewed, safe changes to `main` first so they survive workspace loss. If the checkout is clean, report the existing checkpoint; do not create an empty commit. Never include credentials, private learner data, generated dependencies or local environment files in a checkpoint.
- Commit and push useful checkpoints at least every five minutes while editing when there are changes to save. Local commits alone do not protect against workspace loss.
- Stay within the owner's requested task. Keep prior work; move material set aside for future analysis into `AnalyseFuture/` instead of deleting it. Never commit discovered credentials or private learner data there.
- `apps/web` and `services/voice-agent` are the active application. `AnalyseFuture/original-projects/reference-sources` contains preserved upstream snapshots, not integrated features or extra setup targets. Do not execute their scripts as part of normal setup.
- Read `docs/product/PROJECT_IDEA.txt` for the current product vision and `docs/architecture/REPOSITORY_STRUCTURE.md` for the active/archive layout. Historical feature-branch/PR suggestions in older handoffs are superseded by the owner's current workflow.
- Read `AnalyseFuture/recovery/migration/REPOSITORY_AUDIT.txt` and the historical continuation report for the completed consolidation. Web lesson/session owners live under `apps/web/features`; root `pytest.ini` excludes archives. Run the existing scoped commands and preserve their exit status.
- The retry/help/recoverable-error improvements from `da2796e` are integrated, with punctuation/decimal retry regressions repaired. Do not reimplement them from an older prompt. The preceding recovery task reported 14 JS / 71 Python / 6 browser tests; live voice/language/avatar quality remains unverified.

## First read

**Continuity-first rule:** Read [docs/continuity/PROJECT_CONTINUITY_HANDOFF.md](docs/continuity/PROJECT_CONTINUITY_HANDOFF.md) **before** relying on any old chat prompt or rebuilding features. It includes previous project research, source map, implementation history, Mermaid diagrams, 21 study repositories, current-versus-PR distinction, live-test blockers and the next unblocked task. The handoff is a dated snapshot: inspect current GitHub main, PRs, CI and actual code before acting. Update it after significant changes without committing personal data, secrets or learner recordings.

Read README.md and docs/product/PRODUCT_VISION.md, docs/research/ASTRA_HANDOFF.md, docs/architecture/ARCHITECTURE.md, docs/research/OPEN_SOURCE_STACK.md, docs/product/MVP_AND_ACCEPTANCE.md, docs/product/ROADMAP.md, docs/architecture/DECISIONS.md, docs/development/CODEX_IMPLEMENTATION_BRIEF.md, **docs/development/IMPLEMENTATION_CHECKLIST.md**, and **docs/development/CODEX_MASTER_BUILD_PROMPT.md**.

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
