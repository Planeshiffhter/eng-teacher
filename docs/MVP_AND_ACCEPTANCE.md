# First MVP: 10-Minute Hindi–English Mock Interview

**Status:** requirements and provisional benchmarks.

## User experience

1. Learner opens mobile web, chooses interview practice and grants microphone permission.
2. Avatar greets learner with a spoken first question; a clear audio-only fallback is available.
3. Learner answers in English, Hindi or mixed Hindi–English.
4. System displays the original wording it recognized. If uncertain, asks what the learner meant.
5. Tutor selects at most **one valuable correction per turn by default**, offers a short explanation and a retry.
6. Learner repeats the phrase; tutor continues naturally with a follow-up question.
7. Learner may interrupt the AI voice while it is speaking.
8. At lesson end, a readable recap shows original vs corrected sentences, what to practice and a next session suggestion.
9. Persist learner-selected practice items (only according to consent); do not save raw audio by default.
10. Log usage units and failures in aggregate so costs can be compared across providers.

## Functional acceptance

- Actual browser microphone and AI speaker pipeline; no pretend call.
- Supported mobile browser smoke test including normal Android hardware.
- Voice, captions and avatar synchronized enough for usability.
- Correct handling of muted microphone, interrupted AI reply, connection loss and unclear speech.
- Original transcript is never silently overwritten by the corrected sentence.
- At least one end-to-end test includes Hindi-English code switching, proper names and negation.
- All provider credentials remain server-side; no hardcoded keys in React.
- If speech/avatar services are unavailable, UI reports this honestly and falls back when possible.

## Pilot evaluation set

With permission, gather **30 code-switched turns** and **20 already-correct English turns**, each independently reviewed by a bilingual teacher. Keep testing speakers separate from model-training examples.

| Metric | Initial proposed target |
|---|---|
| Meaning preservation | ≥27/30 mixed-language turns accepted by bilingual reviewer |
| False corrections | ≤1/20 correct English turns incorrectly marked wrong |
| End-of-speech → first audio reply | Median <2 seconds (stretch target, hardware/network dependent) |
| Reuse across new questions | Initial research target: 6/10 learners reuse the practiced pattern without a hint next day |
| Repeat use | Initial research target: 10/20 pilot learners complete 3 short sessions in one week |
| Cost | Measure real total per completed lesson; compare against willingness to pay |

These are **hypotheses / initial targets**, not already-achieved scores or guarantees. Track P90 latency, unstable network behavior, ASR errors, teacher correction accuracy and dropout reasons too.

## Teaching-quality review cases

- Already-correct informal or regional English — no forced correction.
- Mixed Hindi and English — preserve intended meaning.
- Negation: “didn't” must not become “did”.
- Names, place names and uncommon words — clarify when uncertain.
- Pauses, slow speech, microphone noise, accidental barge-ins.
- Distinguish grammatical feedback from pronunciation feedback; do not score phonemes from text alone.
- Try correction retry and **later independent reuse**, not only parroting.

## Pilot safety/privacy

Adult testers for the initial opt-in pilot; accessible language for all learners. No recording by default. Explicit consent for storing audio or using clips in evaluations/training. Offer deletion controls and minimize retained transcripts.
