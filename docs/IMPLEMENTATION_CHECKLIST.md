# Full Ordered Implementation Checklist — Eng Teacher

**Last updated:** 13 Nov 2026. **Purpose:** a single prioritized source of truth for GitHub/Codex, from existing MVP to competitive product. **Checkboxes reflect verified work, with evidence linked below.** Source code existing is not the same as a verified working live product.

**Repository:** https://github.com/Planeshiffhter/eng-teacher. **Public** at checklist creation. Never store secrets or learner audio in this repository.

## Existing source inventory (not completed acceptance gates)

- Source present: Next.js browser interface, LiveKit Python agent, correction cards, transcripts, access-code pilot session endpoint, ten-minute deadline and unit/browser tests.
- No claim of verified real audio quality, Hindi-English comprehension, talking avatar, pronunciation scoring, user accounts, production billing or fine-tuned model.
- Explicit explanation/repeat/retry/skip commands now preserve correction state. **Important:** wider free-form intent detection and live speech remain unverified.

## Execution rules

1. Advance phase by phase, but implement **one tested vertical slice per commit**. Do not generate empty future-service scaffolds.
2. A feature is **complete** only after the stated acceptance gate passes. For credentials/hardware/manual checks, mark **BLOCKED** in the engineering report instead of checking it.
3. **Reuse-first:** official LiveKit starters, an audited avatar SDK, evaluated pronunciation engines, FSRS, model tests. Do not merge nine unrelated applications.
4. **Security/privacy:** consent, recording off by default, no tokens/audio in Git, data minimization, age-appropriate safeguards and separate commercial licence review for code, weights and assets.
5. **Cost discipline:** track billable units, retries, model usage and latency. Do not self-host GPU services until quality and unit economics justify it.
6. Completion statuses should be changed by a developer only with a commit/test/evidence link. The initial checks are intentionally conservative.

## Verified progress — 13 November 2026

- **P0.01** Repository inventory inspected.
- **P0.02** Automated CI succeeded including frontend/Python tests, Ruff, Next.js build/type-check and Playwright browser checks: https://github.com/Planeshiffhter/eng-teacher/actions/runs/43471210303
- **P1.06** Explicit assistance commands implemented and regression-tested: https://github.com/Planeshiffhter/eng-teacher/commit/aacc0e78a16ed0cb7bdaa6490e837f69ce6a9d82
- **Next unblocked coding task:** P1.07 (broader intent classification, ambiguous turns, Hinglish controls and equivalent paraphrase handling), plus P2.16 (privacy-safe model-token usage metrics).
- **External verification remains blocked:** P2.12–P2.15 require owner-managed service credentials, connectivity, consenting speakers and a physical Android test.

## P0: Foundation, safety and current baseline

- [x] **P0.01** Inventory current Next.js, Python, CI and tests
  - **Acceptance:** Repository tree + source inventory verified
  - **Dependency/blocker:** None
- [x] **P0.02** Run locked frontend/agent tests and CI
  - **Acceptance:** CI green on current branch
  - **Dependency/blocker:** Actions runner / network for npm and uv
- [ ] **P0.03** Verify licences of imported libraries and all voice/avatar/model assets
  - **Acceptance:** THIRD_PARTY_NOTICES updated with evidence
  - **Dependency/blocker:** Current upstream licence audit
- [ ] **P0.04** Protect secrets and public repository; validate signed sessions and recording-off behavior
  - **Acceptance:** Security review and no keys in git
  - **Dependency/blocker:** Owner may choose private visibility
- [ ] **P0.05** Document one reproducible local and production-mode start procedure
  - **Acceptance:** Another developer can start both processes
  - **Dependency/blocker:** Provider credentials for real calls

## P1: Dialogue engine — immediate coding

- [x] **P1.06** Fix Hindi explanations, repeat, retry-again and skip without accidental advancement
  - **Acceptance:** Regression tests preserve pending correction/question index
  - **Dependency/blocker:** None
- [ ] **P1.07** Differentiate genuine retry vs learner request; safe uncertainty fallback
  - **Acceptance:** Conversational test matrix including Hinglish commands
  - **Dependency/blocker:** Test model adapter if needed
- [ ] **P1.08** Preserve learner's original text, intent, negation, numbers and names
  - **Acceptance:** Teacher-reviewed test fixtures and typed feedback events
  - **Dependency/blocker:** Bilingual reviewer for quality
- [ ] **P1.09** Avoid false correction and accept natural paraphrases
  - **Acceptance:** No invented grammar errors; retry not scored by exact string
  - **Dependency/blocker:** Evaluation fixtures
- [ ] **P1.10** Add correction styles: instant, natural conversation, explain on request
  - **Acceptance:** Mode persists across session; tests
  - **Dependency/blocker:** None
- [ ] **P1.11** Make interruptions and session end leave dialogue state consistent
  - **Acceptance:** Agent integration tests pass
  - **Dependency/blocker:** Live microphone for final verification

## P2: Live audio, validation and observable cost

- [ ] **P2.12** Complete mic→STT→tutor→TTS→speaker call with real providers
  - **Acceptance:** Desktop/Android real call recorded as a test result, not a demo mock
  - **Dependency/blocker:** LIVEKIT_URL, LIVEKIT_API_KEY, LIVEKIT_API_SECRET, OPENAI_API_KEY, PILOT_ACCESS_CODE
- [ ] **P2.13** Validate Hindi–English mixed speech (names, negation, silence, accent, noise)
  - **Acceptance:** 30 reviewed mixed turns; proposed ≥27/30 correct intent
  - **Dependency/blocker:** Consented bilingual speakers
- [ ] **P2.14** Validate no forced corrections of valid regional English
  - **Acceptance:** 20 reviewed valid utterances; proposed ≤1/20 false corrections
  - **Dependency/blocker:** Bilingual reviewer
- [ ] **P2.15** Test barge-in, mic permissions, subtitles, reconnects and 10-minute cap
  - **Acceptance:** Device/network checklist passes
  - **Dependency/blocker:** LiveKit real service + physical Android
- [ ] **P2.16** Collect STT time, TTS characters, model tokens, provider failures and billed minutes
  - **Acceptance:** Aggregate usage present without raw audio/utterances
  - **Dependency/blocker:** Provider SDK metrics / billing
- [ ] **P2.17** Measure end-of-speech→first audible response and dropped calls
  - **Acceptance:** P50 and P90 from real calls; proposed P50 <2 s
  - **Dependency/blocker:** Live testing + instrumentation
- [ ] **P2.18** Calculate total service cost per completed lesson and cap spend
  - **Acceptance:** Document complete measured cost incl. failed calls and hosting
  - **Dependency/blocker:** Provider billing dashboard

## P3: Video-call avatar — genuine moving teacher

- [ ] **P3.19** Audit and prototype one commercially compatible talking avatar
  - **Acceptance:** Real audio-driven animation, verified asset/model licence
  - **Dependency/blocker:** Upstream repo, licence and assets
- [ ] **P3.20** Integrate avatar with existing LiveKit audio without rebuilding voice transport
  - **Acceptance:** Lip sync follows speech; audio-only fallback works
  - **Dependency/blocker:** Browser hardware
- [ ] **P3.21** Provide clear video-call controls, captions and responsive mobile UI
  - **Acceptance:** Accessible UX; mobile/desktop smoke tests
  - **Dependency/blocker:** Android test phone
- [ ] **P3.22** Measure avatar CPU/GPU overhead and effect on conversational latency
  - **Acceptance:** P50/P90 latency and fps on midrange hardware
  - **Dependency/blocker:** Real device
- [ ] **P3.23** Add configurable avatar/voice choices after first avatar is validated
  - **Acceptance:** Working provider configuration without duplicate engines
  - **Dependency/blocker:** Licensed assets

## P4: Learning curriculum and lesson modes

- [ ] **P4.24** Define original CEFR-oriented placement, goals and skill map
  - **Acceptance:** Educator-reviewed scope and level rubric
  - **Dependency/blocker:** Qualified reviewer
- [ ] **P4.25** Build daily English, interview, work, travel, shopping and roleplay lessons
  - **Acceptance:** Real authored dialogue with lesson goals and tests
  - **Dependency/blocker:** Content authoring
- [ ] **P4.26** Teach grammar and vocabulary with examples and exercises
  - **Acceptance:** Reviewed explanation and guided retries
  - **Dependency/blocker:** Educator review
- [ ] **P4.27** Add lessons for listening comprehension and free speaking
  - **Acceptance:** Completed lesson events and progression
  - **Dependency/blocker:** Audio content
- [ ] **P4.28** Provide native-language help and correction preferences
  - **Acceptance:** Learner can change language/mode without losing conversation
  - **Dependency/blocker:** Languages validated separately

## P5: Audio-based pronunciation

- [ ] **P5.29** Select/test audio phoneme scoring candidate, including OpenPronounce
  - **Acceptance:** Document licence, accent/error characteristics
  - **Dependency/blocker:** Speech test recordings + consent
- [ ] **P5.30** Separate grammar accuracy, ASR transcription and pronunciation evidence
  - **Acceptance:** No phoneme grades from plain transcripts
  - **Dependency/blocker:** Audio + reference utterances
- [ ] **P5.31** Implement repeat-after-me, stress, sounds and intonation feedback
  - **Acceptance:** Teacher-validated practice clips and feedback
  - **Dependency/blocker:** Expert review
- [ ] **P5.32** Check scores across Indian accents, microphones and noisy rooms
  - **Acceptance:** Calibration report, fallback for uncertain scores
  - **Dependency/blocker:** Diverse consenting speakers

## P6: Accounts, learning memory and retention

- [ ] **P6.33** Choose authentication and data store with access controls
  - **Acceptance:** Secure login and user-specific database authorization
  - **Dependency/blocker:** Hosting decision
- [ ] **P6.34** Add consent and delete/export controls; raw recording off by default
  - **Acceptance:** Privacy test cases and verified deletion flow
  - **Dependency/blocker:** Data policy
- [ ] **P6.35** Save learner-approved phrases, progress and errors
  - **Acceptance:** Private user history; no unintended storage
  - **Dependency/blocker:** Database
- [ ] **P6.36** Add next-session practice and spaced repetition using TS-FSRS
  - **Acceptance:** New prompt tests independent reuse next day
  - **Dependency/blocker:** Learner pilot
- [ ] **P6.37** Build dashboard, streaks and milestones without fake progress scores
  - **Acceptance:** Progress derived from genuine lessons
  - **Dependency/blocker:** Event model
- [ ] **P6.38** Add course/admin content management
  - **Acceptance:** Role-aware content editing and audit trail
  - **Dependency/blocker:** Authentication

## P7: Additional language expansion

- [ ] **P7.39** Validate Hindi production experience first
  - **Acceptance:** Bilingual review and measured recognition quality
  - **Dependency/blocker:** P2 validation
- [ ] **P7.40** Add Punjabi, Bengali and other Indian-language recognition/explanations
  - **Acceptance:** Native-speaker fixtures for each language
  - **Dependency/blocker:** Provider coverage and reviewers
- [ ] **P7.41** Test slower speakers, language switching and turn detection per language
  - **Acceptance:** No premature interruption / unsafe interpretation
  - **Dependency/blocker:** Real mic audio

## P8: Independent fine-tuned model

- [ ] **P8.42** Publish data schema, consent standards and redaction pipeline
  - **Acceptance:** Versioned dataset structure and privacy rules
  - **Dependency/blocker:** Rights/consent
- [ ] **P8.43** Collect teacher-reviewed permitted data and independent held-out set
  - **Acceptance:** No evaluation leakage into training
  - **Dependency/blocker:** Educators and participant consent
- [ ] **P8.44** Benchmark hosted model and open-weight Qwen baseline
  - **Acceptance:** Accuracy/latency/cost on same held-out cases
  - **Dependency/blocker:** Inference credits/GPU
- [ ] **P8.45** Build Unsloth/LoRA reproducible notebook and scripts
  - **Acceptance:** Smoke run + export with clearly reported limits
  - **Dependency/blocker:** Colab or rented GPU
- [ ] **P8.46** Train and evaluate adapter against baseline before switching
  - **Acceptance:** Measured net benefit; roll-back plan
  - **Dependency/blocker:** GPU + permissioned data
- [ ] **P8.47** Add scalable own-model serving, optional faster-whisper/Kokoro alternatives
  - **Acceptance:** Concurrency, quality and total cost verified
  - **Dependency/blocker:** GPU hosting

## P9: Commercial launch and long-term competitiveness

- [ ] **P9.48** Deploy encrypted production web/agent infrastructure
  - **Acceptance:** Monitoring, backups, rollback, TLS and quotas
  - **Dependency/blocker:** Hosting
- [ ] **P9.49** Replace pilot access code with individual auth and abuse controls
  - **Acceptance:** Authenticated gated sessions, rate limits and spending caps
  - **Dependency/blocker:** P6 auth
- [ ] **P9.50** Add subscription products and payment flows only after measured economics
  - **Acceptance:** Verified billing, cancellation, refunds and server webhooks
  - **Dependency/blocker:** Payment provider
- [ ] **P9.51** Build native Android app after mobile-web call behavior is stable
  - **Acceptance:** Physical device and store-compliance testing
  - **Dependency/blocker:** Android build environment
- [ ] **P9.52** Conduct learner experiments against competitor workflows
  - **Acceptance:** Human-reviewed learning transfer and repeat use
  - **Dependency/blocker:** Consenting participants
- [ ] **P9.53** Security/accessibility/privacy review and load/concurrency test
  - **Acceptance:** Critical issues fixed; incident response; launch checklist
  - **Dependency/blocker:** Independent review
- [ ] **P9.54** Release, monitor, improve based on outcomes and retention
  - **Acceptance:** Measured results vs objectives, not vanity metrics
  - **Dependency/blocker:** Deployment

## Explicit requests for the repository owner

**Needed for P2 live verification:** working `LIVEKIT_URL`, `LIVEKIT_API_KEY`, `LIVEKIT_API_SECRET`, `OPENAI_API_KEY`, `PILOT_ACCESS_CODE`, a deployment/test machine with network access and at least one Android phone. Set them as encrypted secrets or local ignored environment variables; **never paste secret values into this repository or chat**.

**Later, only when required:** approved talking-avatar assets/licence, bilingual English teacher feedback and consenting testers, privacy/retention policy, database/auth choice, permitted dataset, GPU/Colab quota, hosting and payment accounts. Do not block P1 coding waiting for these.

## Immediate next working task (P1)

Fix `services/voice-agent/src/eng_teacher/tutor.py`: an explicit Hindi explanation / repeat / another-attempt request must **not** consume the pending correction or advance the question. Add Python regressions for a single sequence of correction → Hindi explanation → repeat → another attempt → accepted retry → one advancement. Keep LiveKit event schemas in sync with the UI and run CI. Then instrument privacy-safe usage.
