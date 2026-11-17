# Current implementation and next integrations

Updated: **17 November 2026 (Asia/Calcutta)**.

The owner has resumed implementation and testing after the organization-only
phase. The existing TypeScript/Next.js and Python/LiveKit foundation remains the
active product. Reference projects remain preserved; they were not installed as
competing applications.

## Delivered: selectable guided conversation

Before a lesson, **Practice focus** offers **Mock interview** and **Everyday
English**. Everyday practice is an original, relaxed conversation about the
learner's day, hobbies and ordinary experiences. The teacher identifies itself
as AI, offers one useful correction, allows help/repeat/skip, and continues with
the selected lesson's questions. It remains an audio-only guided lesson.

| Responsibility | Implementation |
| --- | --- |
| Accessible picker and matching entry/live copy | `apps/web/features/lesson/components/tutor-app.tsx` |
| Public lesson IDs and display data | `apps/web/features/lesson/catalog.ts` |
| Allowlisted admission and signed `lesson_id` | `apps/web/features/session/server/session.ts` |
| Original immutable curriculum | `services/voice-agent/src/eng_teacher/teaching/lessons.py` |
| Selected question/retry/help progression | `services/voice-agent/src/eng_teacher/teaching/tutor.py` |
| Selected worker instructions and greeting | `services/voice-agent/src/eng_teacher/runtime/agent.py` |
| Cross-runtime lesson-ID/default contract | `tests/contracts/lesson-catalog.json` |

Only catalog IDs are accepted: `mock-interview` and `everyday-conversation`.
An omitted selection preserves the existing interview default for older clients
and signed metadata. Explicit null, wrong types, unknown strings and prototype
property names are rejected. Client input cannot provide prompts, greetings,
questions, worker names or a longer deadline. The public `/api/session`, ten-minute
cap, named worker, microphone-only grants and version 1 feedback remain intact.

Restart/deploy the web server and voice worker from the same implementation
revision. An older worker does not understand the new selection, and the new web
client requires the server's canonical lesson ID in its response before joining.

The worker validates lesson metadata before starting audio. Separate tutor
instances keep separate progress, and repeating the last question uses the
selected lesson's continuation instead of falling back to interview text.

## Delivered: private usage totals

`runtime/usage.py` provides fixed-size, in-memory counters. The OpenAI text adapter
reports one logical request outcome for each decision, explanation, semantic retry
assessment or teaching-help call. Totals include:

- Reported prompt/completion tokens, including responses whose output fails
  validation.
- Logical request, response and error counts, per operation and in total.
- Responses with missing/invalid token usage, kept distinct from known totals.
- Validated speech-recognition seconds and synthesized character totals.

The worker writes the bounded numeric snapshot to its existing private lesson-end
log. Counters retain no utterances, prompts, response text, provider exceptions,
model/request identifiers, audio or credentials. Snapshot copies cannot mutate
live counters. Callback failures do not interrupt teaching; cancellation propagates.

These are known reported units, not a billing estimate. SDK-internal HTTP retries,
unreported usage, full media/hosting cost and measured lesson pricing remain
unverified. No artificial token total or price is substituted for missing data.

## Delivered: recoverable assistance failures

Failed example, translation or Hindi explanation calls keep the practice target
and signal the existing recoverable-error path. Short natural requests such as
"Give an example" and "Please show an example" are recognized as help instead of
being consumed as a speaking retry.

## Validation and limits

Current automated checks: **24 JavaScript tests, 136 service Python tests,
8 maintenance tests and 8 desktop/mobile Chromium tests passed**, plus production
build, TypeScript, Ruff lint and formatting. Isolated reference validation passed
470 Cadence cases, 16 avatar cases and basic avatar browser rendering/audio smoke.
See [MODULE_VALIDATION.md](MODULE_VALIDATION.md) for scope, fixes and limitations.
The prior reorganized Python tree first passed its existing 71 tests;
two import-order lint issues left by the no-test organization were corrected.
The installed worker CLI also imports successfully through its compatibility
entrypoint. Production HTTP startup serves the lesson picker and retains the
expected no-token response when voice configuration is missing.

Coverage includes signed JWT lesson selection, rejection of unsupported IDs,
worker metadata/greeting selection, correction -> help -> retry -> next question,
independent lesson state, private numeric accounting, malformed output/failures,
and browser selection/submission/disabled controls/failure recovery. Browser audio
is synthetic; model and room fixtures are fake. A successful real voice lesson
has not been demonstrated by these checks.

No LiveKit/OpenAI/pilot credentials were present when checked. Bengali support,
physical Android behavior, speech quality, actual latency/cost, and app-integrated
avatar behavior remain unverified. Isolated SDK graphics/audio smoke is not a
LiveKit lesson integration. Hindi-English speech adapters are present in source; the new
lesson catalog is not evidence of additional language support.

## What remains, in order

1. Configure actual provider access securely and validate one complete real voice
   lesson: greeting, learner speech, correction/help/retry, interruptions, reconnect
   and the original ten-minute deadline. Compare private usage with provider bills.
2. Run a small Bengali-English recognition/translation/explanation trial with fluent
   reviewers. Add a tested language preference only after its supported behavior
   and uncertainty fallback are defined; do not advertise all languages.
3. Trial the preserved browser avatar through a narrow lesson feature adapter.
   Select only the remote teacher track and exactly one audio playback owner;
   verify permissions/autoplay, barge-in, cleanup, fallback and ordinary phones.
   Review exact model/asset notices before selecting dependencies.
4. Add reviewed original exercises, then opt-in progress/history with proper
   authentication, retention/export/deletion and distributed spending safeguards.
5. Extend speech/provider failure and retry observability where the SDK exposes
   actual events. Startup/cancellation/close-failure resource cleanup has now been
   repaired and covered by lifecycle regressions. Do not log private provider payloads.

Work continues directly on `main` with normal tested checkpoints. The original
archives, historical reports and the organization mapping retain their recorded
scope; new behavior belongs in the active feature folders described above.
