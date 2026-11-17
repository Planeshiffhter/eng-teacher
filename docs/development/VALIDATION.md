# Validation record — first voice-tutor slice

See the [implementation status](IMPLEMENTATION_STATUS.md) for current test
counts, verified features and remaining acceptance checks.

## Complete module pass — 17 November 2026

Current local checks passed: **24 web/API tests, 136 voice-service tests,
8 maintenance CLI tests and 8 active browser tests**. The root Python invocation
reports 144, which is the same 136 service plus 8 maintenance cases.
Build, typecheck, lint/format and production HTTP checks passed. Fixed worker
construction/shutdown cleanup, background exception privacy, exact JSON media
admission and maintenance formatting/verification. Maintenance checks now run in CI.

In read-only-original isolated copies, **470 Cadence pure-module cases and
16 avatar package cases** passed, plus a real local avatar WebGL/AudioWorklet
smoke with synthetic audio. Neither is an integration of those apps into the tutor.
See [MODULE_VALIDATION.md](MODULE_VALIDATION.md) and its saved evidence for exact
commands, counts, fixed regressions and unexecuted live/native/cloud checks.

## Guided practice and private usage — 17 November 2026

Implementation/testing resumed from organized `main` at `9c94c84`. The new
Everyday English lesson, signed lesson selection and private usage accounting
passed **18 JavaScript tests, 126 Python tests and 8 Chromium browser tests**, plus
production build, TypeScript, Ruff lint and formatting. New browser coverage checks
the chosen mode, signed-request selection, joining controls and failure recovery.
Existing deadline, meaning-preservation and authentication checks remain.

Fixtures use fake models/rooms and synthetic audio. Missing service credentials
prevent a real provider lesson; no new Bengali, device, avatar, speech-quality or
billing claim is made. See [implementation status](IMPLEMENTATION_STATUS.md) for
exact ownership, metric limits and remaining integrations. Earlier sections below
retain their own recorded validation scope.

## Consolidation validation — 17 November 2026

Starting at `98cfcd7`, reviewed retry/help/recoverable-error work from `da2796e`
was selectively recovered at `8f1c988`, with a punctuation/decimal retry repair.
Web source and tests moved into lesson/session features. **14 JavaScript tests,
71 Python tests and 6 browser tests passed**, together with frozen installs,
Ruff lint/format, build, typecheck and real local HTTP startup. Root pytest
collection found only the 71 active tests after the archive-discovery guard.
The active npm advisory audit returned zero known vulnerabilities.

The earlier 14/42/6 organization-only record below remains historical evidence.
The current [validation report](../../AnalyseFuture/recovery/validation/TEST_AND_VALIDATION_REPORT.txt)
records commands, recovered regressions and unexecuted checks. No live voice,
physical Android, Bengali quality, pronunciation or integrated-avatar result is
claimed. Remote Actions/account/protection API access was unavailable.

## Repository organization check — 17 November 2026

The source-preservation and product-idea task moved uploaded projects and ZIPs
into `AnalyseFuture/`. It did not change active application source, tests, runtime
configuration, dependency declarations or lockfiles. The baseline before this task
was `38e9d0034ba613052b3e7d37f902ed635eae8d9c`; the initial organization checkpoint is
[`a1457a3`](https://github.com/Planeshiffhter/eng-teacher/commit/a1457a3).

After the move: **14 JavaScript tests, 42 Python tests and 6 Chromium browser
checks passed**, together with Ruff, the production build and TypeScript. All
1,478 relocated files retained their SHA-256 hashes; all 1,474 extracted upstream
payloads matched their original ZIP entries. See
[the repository audit](../architecture/REPOSITORY_STRUCTURE.md) for commands, paths and limits.

These are current local/offline results, separate from the older record below and
the historical PR test counts. No real provider lesson, Bengali quality, avatar
integration or physical Android behavior was validated in this task. Existing
live acceptance work remains necessary. The detailed new idea is in
[`docs/product/PROJECT_IDEA.txt`](../product/PROJECT_IDEA.txt); it describes planned features.

## Original implementation record

Date: 13 November 2026. Branch: `feat/voice-tutor-mvp`.

## Verified locally

| Check | Result | What this establishes |
| --- | --- | --- |
| `npm ci` | Passed against committed lockfile | Reproducible JavaScript dependency installation. |
| `uv sync --frozen --project services/voice-agent` | Passed | Python agent dependencies install on Python 3.12, without GPU. |
| `npm test` | 13 tests passed | Real local JWT signing/verification, microphone-only room grants, pilot code/origin checks, bounded requests, tutor packet parsing and lesson time/retention guards. No LiveKit connection is made by these unit tests. |
| `npm run typecheck` | Passed | TypeScript checks against installed LiveKit SDK types. |
| `npm run build` | Passed | Optimized Next.js production build. |
| `npm run test:browser` | 6 tests passed across desktop/mobile Chromium | Responsive page, synthetic browser microphone open/stop, honest missing-configuration errors, failed-room recovery. The failure test mocks the token endpoint only; it does not simulate a successful voice lesson. |
| `npm audit` | 0 known vulnerabilities reported | Registry audit of the resolved npm lockfile at validation time; not a complete security assessment. |
| Agent CLI `--help` | Passed | Installed entry point and native SDK/VAD imports work. |
| `uv run --frozen pytest` in `services/voice-agent` | 33 tests passed | Tutor policy/adapter checks, installed SDK session routing with fake model and synthetic speech frames, correction → retry → continuation, immutable deadline validation, deadline expiry, room deletion and learner-disconnect lifecycle. |
| `uv run --frozen ruff check .` and `ruff format --check .` in the agent | Passed | Python lint and formatting. |

The SDK-session test uses the real LiveKit scheduler and a fake audio sink, but injects text instead of recognizing microphone audio and synthesizes silent frames instead of calling a voice provider. Worker lifecycle tests use fake room/session APIs. These results do not establish live speech acceptance. The GitHub Actions workflow is checked in; it has not been observed running remotely from this environment.

## Live acceptance still required

Live acceptance requires configured LiveKit and OpenAI access and a real
microphone-to-provider lesson. Teaching quality, code-switching accuracy,
interruption latency, cost, pronunciation and avatar behavior with live speech
still require measurement.

After securely configuring the examples described in [DEVELOPMENT.md](DEVELOPMENT.md):

1. Start the web server and named worker. Use a real Android mobile browser over HTTPS and a desktop browser. Start/end a lesson, mute/unmute, deny microphone permission, permit audio playback, and confirm microphone tracks stop after leaving.
2. Hear the greeting and answer a job-interview question with real speech. Verify both learner and tutor subtitles, including partially completed/interrupted tutor replies.
3. Say “Maine customer calls handle kiye.” Check the original recognition separately from a suggested English version. Ask for an explanation, retry aloud, and confirm the tutor advances the interview rather than repeatedly correcting the retry.
4. Exercise names (for example, Aditi and Pune), numbers, “I didn't approve the payment,” valid regional English, unclear speech and background noise. The tutor should preserve meaning or ask for clarification. Use bilingual reviewers and the acceptance document's held-out 30 mixed-language / 20 already-correct cases; the deterministic unit tests do not replace this evaluation.
5. Pause slowly, then speak over the AI. Verify barge-in stops audio and recognition still captures the new answer. Measure end-of-speech to first audible reply and slow-tail latency; do not infer these from VAD settings.
6. Disconnect/reconnect the network, stop the worker, and simulate provider access failures. Check visible errors, clean room termination, and no unnoticed paid session continuing after leaving.
7. Run the full ten-minute lesson. Confirm the original signed deadline still applies after reconnect, the room is deleted, audio stops, and the recap retains original/suggested pairs only in page memory.
8. Inspect private server aggregate usage and provider billing. Confirm no lesson recordings, database transcripts, cloud trace uploads or browser persistence were enabled. Review provider-side retention independently. Model token costs, exact total lesson cost and measured latency remain unvalidated.

Run the full [MVP acceptance criteria](../product/MVP_AND_ACCEPTANCE.md) before a learner pilot. Public rollout also requires individual authentication, distributed quotas/rate limiting, deployment operations and commercial artifact/voice review. These are recorded limitations rather than silently mocked features.
