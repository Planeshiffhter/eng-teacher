# Validation record — first voice-tutor slice

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

No LiveKit or OpenAI credentials were configured in the execution environment. There was no real microphone → LiveKit → recognition → tutor → voice-provider call. No teaching-quality, code-switching accuracy, interruption-latency, cost or pronunciation benchmark is claimed. No avatar is implemented or tested.

After securely configuring the examples described in [DEVELOPMENT.md](DEVELOPMENT.md):

1. Start the web server and named worker. Use a real Android mobile browser over HTTPS and a desktop browser. Start/end a lesson, mute/unmute, deny microphone permission, permit audio playback, and confirm microphone tracks stop after leaving.
2. Hear the greeting and answer a job-interview question with real speech. Verify both learner and tutor subtitles, including partially completed/interrupted tutor replies.
3. Say “Maine customer calls handle kiye.” Check the original recognition separately from a suggested English version. Ask for an explanation, retry aloud, and confirm the tutor advances the interview rather than repeatedly correcting the retry.
4. Exercise names (for example, Aditi and Pune), numbers, “I didn't approve the payment,” valid regional English, unclear speech and background noise. The tutor should preserve meaning or ask for clarification. Use bilingual reviewers and the acceptance document's held-out 30 mixed-language / 20 already-correct cases; the deterministic unit tests do not replace this evaluation.
5. Pause slowly, then speak over the AI. Verify barge-in stops audio and recognition still captures the new answer. Measure end-of-speech to first audible reply and slow-tail latency; do not infer these from VAD settings.
6. Disconnect/reconnect the network, stop the worker, and simulate provider access failures. Check visible errors, clean room termination, and no unnoticed paid session continuing after leaving.
7. Run the full ten-minute lesson. Confirm the original signed deadline still applies after reconnect, the room is deleted, audio stops, and the recap retains original/suggested pairs only in page memory.
8. Inspect private server aggregate usage and provider billing. Confirm no lesson recordings, database transcripts, cloud trace uploads or browser persistence were enabled. Review provider-side retention independently. Model token costs, exact total lesson cost and measured latency remain unvalidated.

Run the full [MVP acceptance criteria](MVP_AND_ACCEPTANCE.md) before a learner pilot. Public rollout also requires individual authentication, distributed quotas/rate limiting, deployment operations and commercial artifact/voice review. These are recorded limitations rather than silently mocked features.
