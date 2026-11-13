# Copy/Paste Brief for GPT Astra in Codex Cloud

Project repository: https://github.com/Planeshiffhter/eng-teacher (currently **public**, default branch **main**).

## Task

You are the principal engineer building an independent, commercially viable, real-time AI English-speaking tutor. Read README.md, AGENTS.md and **all docs/** before changing code.

**Important:** This repository was documentation-only when the plan was imported. First inspect the current files; do not claim a working product exists until tested. Avoid repeated planning and large untested scaffolds.

## Vision vs first deliverable

Long-term benchmark: Praktika-style avatar conversation, ELSA-style reliable pronunciation feedback, Speak-style adaptive practice, Duolingo-style learning progression; English tutor uniquely strong at preserving Hindi-English meaning.

**FIRST DELIVERABLE ONLY:** Working 10-minute Hindi-English mock interview on mobile web, with:
- actual microphone input and real-time spoken replies;
- ability to interrupt;
- one useful correction by default, optional clarification, retry and continuation;
- original versus proposed sentence shown separately;
- browser speaking avatar with audio-only fallback;
- live transcript and end-of-lesson recap;
- privacy-first practice history and actual API/voice cost metering.

## Open-source reuse

Start from:
- https://github.com/livekit-examples/agent-starter-react
- https://github.com/livekit-examples/agent-starter-python

Trial:
- https://github.com/InterviewFlowAI/talking-avatar
- https://www.sarvam.ai/ for Hindi/English STT and TTS, only after checking current integrations, pricing and terms.

Use Cadence and Sprigo **as references or selectively adapted compatible modules**, not blindly merged apps. Do not implement two overlapping avatar, voice, or account systems. Review docs/OPEN_SOURCE_STACK.md and commercial rights first.

## Engineering rules

1. **Inspect** repository, SDK versions, available environment and dependencies before coding.
2. Write a short audited plan only where needed; maintain docs/DECISIONS.md with evidence.
3. Establish a single minimal app layout, voice agent and typed teaching/correction contract.
4. Implement one complete microphone→response→correction→retry vertical slice.
5. Add live avatar and fallback after audio works; then transcript, recap, learning storage and cost events.
6. Make speech and LLM providers swappable. Keep API secrets on the server and provide safe env examples.
7. Add focused automated tests; show commands/output. Include human-in-the-loop browser/device testing instructions.
8. Set recording **OFF by default**; consent for evaluation/training separately.
9. Preserve names and negation; don't force a correction when English is acceptable.
10. Do not invent features, benchmarks, measured costs, trained models, licenses or external GPU resources.

## Acceptance criteria

Use docs/MVP_AND_ACCEPTANCE.md. Submit working changes with setup and tests. Demonstrate the end-to-end path with genuine connected providers when credentials are present; otherwise mark missing service credentials and explicitly label mocks as mocks. Start with one interview lesson, not the whole market-leading platform.

## Reporting format after each coding task

- Files changed / working demo path.
- Tests actually run and results.
- Features truly implemented vs mocked/deferred.
- Required accounts, API credentials, GPU resources and recurring costs.
- Next smallest testable feature.
