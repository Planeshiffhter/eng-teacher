# Proposed Technical Architecture

**Status:** proposed; no application services are implemented in this repository yet.

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
