# MASTER BUILD DIRECTIVE FOR CODEX — Eng Teacher

> **Current recovery note (17 November 2026):** The immediate retry/help/error
> work described below is now recovered and tested on `main`; do not rebuild it
> from this older directive. Read AGENTS.md and
> [NEXT_DEVELOPER_INSTRUCTIONS.txt](../AnalyseFuture/NEXT_DEVELOPER_INSTRUCTIONS.txt)
> for actual feature paths, 14/71/6 local checks and the next scoped task. Broader
> release sections below remain product goals, not completed features.

**Status:** current development directive; do not mistake aspirations for shipped features.
**Repository:** https://github.com/Planeshiffhter/eng-teacher
**Last known implementation when this was prepared:** commit `fa600a6` on `main`, with a Next.js LiveKit web MVP, Python voice-agent, tutor policy, correction cards, captions and automated test files. Always inspect the latest actual files before changing anything.

## Mission — not only a ten-minute interview

Build an independently controlled, commercial-quality, multilingual **AI English-speaking learning platform**. Our product benchmarks are:

- **Praktika:** appealing responsive talking-avatar conversational experience;
- **ELSA Speak:** accurate *audio-based* pronunciation coaching;
- **Speak:** effective level-adaptive conversation and feedback;
- **Duolingo:** coherent curriculum, practice scheduling, progress and engagement;
- **Our original differentiator:** meaning-preserving Hindi-English teaching and later regional-language support, with demonstrable next-day learning transfer.

These are public feature benchmarks, NOT permission to copy private code, copyrighted curricula, characters, designs or branding.

**Do not pivot to a generic text chatbot, build only static screens, restart from a different scaffold, or spend credits endlessly rewriting planning documents.** Keep advancing the existing implementation along measurable releases.

## Verified starting points and immediate bug

Inspect:
- `services/voice-agent/src/eng_teacher/tutor.py`
- `services/voice-agent/src/eng_teacher/providers.py`
- `services/voice-agent/src/eng_teacher/agent.py`
- `services/voice-agent/tests/test_tutor.py`
- `apps/web/features/lesson/components/tutor-app.tsx`
- `apps/web/features/lesson/tutor-events.ts`
- `docs/DEVELOPMENT.md`, `docs/VALIDATION.md`, and `AGENTS.md`.

A previously reproduced bug: after correction, the tutor treats **every next utterance** as the retry. If the learner asks “Please explain that in Hindi,” it clears pending retry and advances the question. That is a real correctness bug and **the next coding change**, but not the end of the project.

## Release A: Make the dialogue a real teacher (IMPLEMENT NOW)

Implement a robust, typed, testable tutor interaction state machine.

**Intents required:** answer question; ask for explanation in English or Hindi; ask for translation; ask to repeat; ask for an example; attempt corrected sentence; ask for another attempt; ask to skip or continue; clarify recognition; pause/end session. A learner can change mind or mix Hindi and English. Handle explicit commands before a retry is consumed. Use a hybrid rules/LLM intent approach where appropriate, with validated structured decisions and safe uncertain fallback. Avoid brittle exact-match-only or arbitrary keyword classification.

**State:** current lesson/question, pending correction, explanation history, retry attempts, question advancement, user-chosen language and ending status; only advance intentionally. Respect correct paraphrases instead of exact matching; never infer pronunciation from plain text. If the learner asks for Hindi explanation, explain the current correction **in Hindi**, keep it pending, and then let them retry; asking to repeat must not create an additional correction. No speculative generation may mutate state.

**Required behavior examples:**
1. Student: “Yesterday I go market.” → Teacher: “Yesterday, I went to the market.” + one short explanation + retry invitation.
2. Student: “Please explain that in Hindi.” → Explain **went** / past tense in Hindi, do NOT advance, keep correction open.
3. Student: “Can you repeat the correct sentence?” → Repeat the suggested sentence and keep state.
4. Student retries accurately or with equivalent natural paraphrase → Acknowledge without claiming an audio pronunciation grade; advance when appropriate.
5. Student: “One more try, please.” → Keep current question and practice target.
6. Student: “Skip this question.” → Honor the request and move forward once.
7. Student says understandable English without material error → Do not manufacture corrections.
8. Hindi-English code switch, proper names, numbers and negation → Preserve meaning; ask if unsure.
9. Failed or delayed provider → Recover gracefully without leaking keys/utterances or corrupting lesson state.

Extend Python tests and, if event schemas change, TypeScript parsers/UI tests; include explicit regression assertions that explaining in Hindi or asking to repeat **never** advances the interview question or silently clears pending correction. Run targeted and full relevant tests. Make code changes, not only a prose proposal.

## Release B: Real usage and educational validation

- The current agent already collects some STT/TTS usage. Extend it to non-sensitive per-lesson totals for actual model tokens, recognition duration, synthesized characters, provider errors and retries. Measure elapsed end-of-speech to first audible response where technically observable; distinguish estimated from measured metrics.
- Keep credentials server-side, do not log raw audio or learner utterances, disable recording by default, avoid storing personally identifying data without authorization.
- Write one simple end-to-end runbook and real-device checklist for desktop Chrome and ordinary Android browsers (mic permissions, slow pauses, interrupts, reconnect, cost, 10-minute deadline).
- **Never claim a live call was verified** without configured services and an actual device/browser test. If missing credentials, run available static/unit/integration tests and identify exactly what must be tested manually.
- Measure with teacher-reviewed, consented held-out cases: 30 Hindi-English turns and 20 acceptable English turns. Initial experimental targets from the pilot: ≥27/30 meaning preserved and ≤1/20 false correction. These are *targets*, not achieved results.
- Compare one full practice task against competitor experiences; record weaknesses without copying proprietary assets.

## Release C: Talking teacher with mobile-first call UX

- Use existing LiveKit/WebRTC; evaluate `InterviewFlowAI/talking-avatar` as one browser avatar integration. Audit CURRENT code, weights, asset and commercial rights before choosing it.
- Animate mouth/micro-expressions in response to real audio output; do not mislabel a static picture/audio waveform as a fully talking teacher.
- Keep audio-only fallback and test avatar quality, frame rate and latency on ordinary Android devices.
- Preserve end, mute, reconnect, caption, correction card, accessible controls, responsive layout.

## Release D: Real learning platform

Implement progressively, each as tested slices:
- Placement/level and goals, CEFR-aligned curriculum with original learning content;
- daily conversation, interview, shopping, workplace, travel and roleplay lessons;
- personalized learner profile, practice history, recurring errors, learner-controlled saved phrases;
- `ts-fsrs` scheduling where useful; spaced retrieval across different questions;
- progress measures reflecting real learning rather than fabricated fluency scores;
- secure accounts, data deletion/consent, educator-reviewed lesson/content authoring and admin tools;
- mobile app later, subscriptions only after authenticating users, measuring actual cost and designing secure billing.

Use Cadence/Sprigo as **references or selectively adapted compatible modules**, not entire copied applications.

## Release E: Audio-based pronunciation quality

- Evaluate `Halleck45/OpenPronounce` and competing options using original speech audio and known target sentences.
- Distinguish ASR mistakes, grammar mistakes, accent variation and actual pronunciation problems.
- Calibrate against human teachers across microphones, accents, noise and language backgrounds. Do not claim ELSA-level phoneme scoring without evidence.
- Preserve privacy and do not use pronunciation scores to shame learners.

## Release F: Custom model independence and scaling

- Keep inference adapters for speech, TTS and tutor LLM; compare hosted services against self-hosted faster-whisper, Kokoro, and open-weight Qwen where licensed and feasible.
- Create dataset schemas, consent documentation, quality review, independent held-out evaluations, LoRA/Unsloth Colab training scripts, model export and inference integration.
- Do **not** declare fine-tuning complete without a real training run. Evaluate baseline vs fine-tuned model for corrections, multilingual meaning, latency and cost before changing production default.
- Consider vLLM/serving, observability, cost and concurrency planning when traffic justifies GPU expense.

## Reuse-first inventory (audit, don't bulk-install)

Core: `livekit-examples/agent-starter-react`, `livekit-examples/agent-starter-python`.
Evaluate next: `InterviewFlowAI/talking-avatar`; speech provider with verified Hindi-English capabilities.
Reference: `pstepanovum/Cadence`, `ozerozdas/sprigo`.
Later or as-needed: `Halleck45/OpenPronounce`, `open-spaced-repetition/ts-fsrs`, `promptfoo/promptfoo`, `SYSTRAN/faster-whisper`, `hexgrad/kokoro`, `unslothai/unsloth`, `vllm-project/vllm`.

Do not bring in a second competing voice-agent or avatar stack without measured reasons. Track source/asset/model licenses and notices.

## Execution contract for Codex

1. Inspect the existing repository and current branch. Preserve working code, existing tests and docs. `main` is the current integration branch; make small commits or a feature PR according to repository/user preference. Never force-push.
2. Start **immediately** by implementing Release A's intent/state bug fix and tests. Do not respond with only another recommendation to do so.
3. After tests pass, implement the next smallest concrete unblocked item from Release B (privacy-safe model token/latency usage where possible) in the same work session if feasible.
4. Do not stop advancing the long-term roadmap because the interview MVP exists. Update status after each meaningful implementation.
5. Keep the existing LiveKit, Next.js, Python, Pydantic and test stack unless empirical evidence justifies changing it.
6. Do not silently claim fake or mocked services are production-ready. When credentials, paid accounts, real-device checks or GPU are needed, clearly separate executable completed work from blocked external verification.
7. Avoid unnecessary repeated dependency upgrades, feature churn, unbounded scaffolding, redesigning the UI without a reason, or generating new huge architecture documents.
8. Protect the public repository: no tokens, provider keys, learner audio, private datasets or personal secrets.
9. Run `npm run typecheck`, `npm test`, `npm run build`, `npm run test:agent`, and browser tests where possible; document exact commands/errors honestly (inspect `package.json` if changed).
10. Update docs only where design or limitations actually change and provide a concise handoff:

**Report for each task:** files changed; code that runs; tests passed/failed; real vs simulated functionality; provider keys/services still required; measured performance/cost if measured; precise next item from the roadmap.

## Acceptance gate for the immediate task

A user can ask for a Hindi explanation, a repeat, another attempt, and then give a valid corrected sentence during the **same pending-correction interaction**, without accidental interview advancement or loss of correction state. Relevant tests pass. The application remains able to start and end sessions without regressions.

**Your next output must include actual implementation work and test evidence, not only high-level advice.**
