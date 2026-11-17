# Proposed Technical Architecture

## Latest integrated slice

The web lesson catalog offers mock interview and original Everyday English.
The admission feature allowlists the choice and signs `lesson_id` beside the
fixed deadline. The worker resolves its trusted curriculum from
`teaching/lessons.py`; tutor questions, instructions and greeting follow that
selection. Older omitted IDs retain the interview default. No client-provided
prompt or curriculum is accepted.

`runtime/usage.py` receives bounded numeric events from the text adapter and SDK
speech metrics, then supplies the private final lesson log. It keeps no text or
provider payloads and distinguishes missing usage from reported totals. These
are logical requests and known units, not inferred HTTP retries or billing cost.
See [implementation status](../development/IMPLEMENTATION_STATUS.md) for tests
and remaining real voice, Bengali and avatar acceptance.

## Current ownership after consolidation

The active web app has two feature owners: `features/session` owns server-side
admission/signing and tests; `features/lesson` owns call UI, event parsing and
tests. Next `app/page.tsx` and `app/api/session/route.ts` delegate to those owners.
The existing Python package owns controls, tutor policy and provider adapters,
with the worker coordinating SDK audio and lifecycle. Version 1 room packets
remain the cross-runtime contract; there is no new public API or database.

Retry/help/recoverable-error work from `da2796e` is now consolidated, with an
additional number/punctuation preservation fix. The target architecture below
still contains future modules that are not implemented. See the
[current structure](REPOSITORY_STRUCTURE.md),
[feature inventory](../../AnalyseFuture/recovery/features/FEATURE_INVENTORY.txt) and
[consolidation report](../../AnalyseFuture/recovery/migration/CONSOLIDATION_REPORT.txt) for actual code.

**Status:** the target architecture below remains the product plan. The first audio-only slice now has `apps/web` (Next.js + LiveKit React) and `services/voice-agent` (LiveKit Python Agents, official OpenAI STT/TTS, Silero VAD, and a separate structured tutor-model adapter). Web tokens dispatch the named agent into a private room; versioned reliable data events carry correction cards. Both services enforce a fixed ten-minute lesson deadline. No database, avatar, mobile-native app or training service is implemented. Live-provider acceptance remains pending; see [development instructions](../development/DEVELOPMENT.md) and [validation](../development/VALIDATION.md).

## System flow

Learner (mobile browser microphone)
→ LiveKit/WebRTC call
→ voice agent (VAD/turn-taking, interruptibility)
→ streaming STT (preserve original utterance; confidence/uncertainty)
→ tutor policy & LLM (understanding, correction, response plan)
→ streaming TTS
→ avatar animation + audio playback
→ transcript / retry card / end-of-lesson recap
→ privacy-aware progress and cost-event persistence

**Rule:** A raw transcript is NOT an authoritative record of actual pronunciation. Phoneme-level exercises require original audio and a validated assessment tool.

## Suggested monorepo target

- apps/web — responsive Next.js interface, call screen, progress UI.
- apps/mobile — future React Native client; do not build before mobile-web MVP works.
- services/voice-agent — LiveKit Python agent; STT/TTS/model adapters, interruptions.
- services/tutor-api — FastAPI endpoints for lessons, history, corrections and progress.
- packages/shared — typed events, requests and correction response schema.
- packages/avatar — client SDK integration with audio-only fallback.
- packages/learning — lesson flows, FSRS integration when justified.
- ml/datasets, ml/evaluation, ml/training, ml/inference — offline evaluations, permitted training and model-serving adapters.
- infrastructure/ — Docker/deployment configurations and cost monitoring.
- tests/ — unit, integration, conversation-regression, browser/device smoke tests.
- docs/ — requirements, decisions, design and compliance.

Use this as a target layout, not a reason to create empty boilerplate directories unnecessarily.

## Core event/data concepts

- Utterance: session ID, original transcript, recognized language(s), timestamps, uncertainty flag, optional opt-in audio reference.
- Tutor correction: original phrase, proposed phrase, explanation language, reason, confidence, whether correction is necessary, retry request.
- Practice attempt: learner's retry, prompt, lesson concept, reviewer/evaluation result if available.
- Lesson summary: practiced concepts, selected review prompts, next session suggestion.
- Service usage: STT billed seconds, TTS chars, LLM tokens, voice-session minutes, errors/retries, approximate spend by provider.
- Consent: separate options for learning history and for voice recordings / model training; retention and deletion.

## Replaceable adapters

Provide narrow interfaces for: speech recognition, speech generation, conversational model, pronunciation assessor, avatar renderer and lesson-revision scheduler. Support hosted or self-hosted providers without changes to tutor policy. Keep credentials server-side.

## Latency and resilience

Stream audio and start voice response promptly; interrupt speech when learner barges in. Allow the avatar to lag or fail without breaking the audio lesson. Gracefully fall back from live STT to repeat/clarification. Measure end-of-speech to first audible reply, disconnects, dropout and cost.

## Privacy, security and licensing

- Never commit secrets, recordings or learner personal data.
- Disable lesson recording by default. Require explicit separate consent for evaluation or training data.
- Minimize personal data in logs and analytics; enforce access controls and deletion.
- Audit source, model, voice, and 3D asset licenses individually; preserve attribution and avoid noncommercial code in a commercial product.
- Do not copy competitor UI assets/characters/proprietary lessons.
