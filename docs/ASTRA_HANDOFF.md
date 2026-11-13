# GPT Astra / Prior Project Discussion — Handoff

**Prepared:** 13 November 2026. **Source:** earlier project chat and its feasibility report. This is a consolidated engineering summary, not a verbatim transcript and not evidence of implemented code.

## What Astra recommended

**Proceed with a narrow pilot**, rather than attempt a full Praktika + ELSA + Speak + Duolingo competitor in the first Codex run:

- One ten-minute **Hindi–English mock interview** on **mobile web**.
- Live mic-to-mic conversation; the learner can interrupt the teacher.
- A browser-rendered, speaking animated avatar, with an **audio-only fallback**.
- Live transcript, meaning-preserving one-at-a-time correction, repeat attempt, and useful recap.
- Example: learner says “Maine customer calls handle kiye”; teacher suggests “I handled customer calls”, asks for a retry, then continues with a different interview question.
- If uncertain about a phrase, name, negation, or intent, clarify instead of inventing a correction.
- Keep the *original* learner wording separate from the *suggested* correction.
- Save progress and selected practice phrases; **recording disabled by default**, separate consent for research/training.

## Preferred first-pass implementation

- **Use:** LiveKit React starter + LiveKit Python Agents starter for call UI, transport, audio and turn-taking.
- **Trial:** Sarvam recognition and speech via supported integrations for Indian-language code-switching; verify language, latency, billing and terms before adopting.
- **Use/evaluate:** InterviewFlowAI Talking Avatar browser SDK for an early low-cost visual teacher.
- **Review for teaching ideas:** Sprigo and Cadence; do not merge entire applications.
- **Defer:** OpenPronounce until audio-based evaluation on varied accents/noisy conditions; FSRS until there is saved practice history; Promptfoo after you have correction test cases.
- **Later:** Compare faster-whisper and Kokoro for self-hosted audio; choose open-weight Qwen + LoRA only after collecting teacher-reviewed failure examples.

## Proposed research and pilot checks (not achievements)

- Ask **five** initial target learners to try a competing tutor task.
- Assemble **30** mixed-language utterances and **20** already-correct English utterances with teacher-reviewed expected handling, with consent.
- Target at least **27/30** meaning-preserving mixed-language corrections.
- Target at most **1/20** false corrections on already-correct English.
- Aim for median under **2 seconds** from end of speech to first audible reply; also inspect slow 10% and interruption failures.
- Pilot idea: **20 adult learners**, three sessions each. Measure next-day independent reuse and return behavior.
- Treat these as **initial proposed evaluation thresholds**, not scientific validation or guaranteed results.

## Planning costs from the dated feasibility example

The earlier report used illustrative Sarvam rates of **₹0.49 per recognition minute** and **₹3.00 per 1,000 generated voice characters**. At five billed recognition minutes plus 2,000 generated characters, the example subtotal is **₹8.45 per 10-minute lesson**; at ten billed minutes it is **₹10.90**. These are **not live quotes** and exclude language-model costs, LiveKit usage, hosting, storage, failures/retries, tax and development credits. Recheck every provider price and meter before making a budget.

## Cautions

- Natural mixed-language transcription may get negation, names, pauses and speaker turns wrong. Evaluate the raw audio with bilingual reviewers.
- No speech or avatar vendor automatically guarantees educationally correct feedback.
- Native-language support for Bengali/Punjabi and turn detection need their own device and speaker testing before enabling them.
- Train custom model adapters only on data with permission and evaluate against a held-out test set before replacing a hosted model.
- Keep ownership of original curriculum, correction policies, evaluation sets and deployment credentials. Review upstream model/asset/code commercial rights.

## Scope reconciled with other project discussions

The **big vision** is an independent full-featured AI learning platform. The **delivery plan** is to prove one reliable speaking lesson first. This resolves the earlier difference between “build every feature” and “protect Codex credits by reusing code and shipping in slices.”
