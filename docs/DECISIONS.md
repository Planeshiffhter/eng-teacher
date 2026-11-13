# Decisions and Open Questions

| Item | Decision as of 13 Nov 2026 | Status |
|---|---|---|
| Product | Independent AI English-speaking teaching platform with avatar calls, corrections, personalization | Vision agreed |
| Benchmark | Praktika + ELSA + Speak + Duolingo behaviors, without copying their proprietary material | Agreed |
| Delivery strategy | One coherent GitHub monorepo, selectively integrate open-source components | Agreed |
| MVP | 10-minute Hindi–English mock interview on mobile web | Preferred from Astra feasibility review |
| Base voice engine | LiveKit React + Python Agent starters | Proposed; verify |
| Avatar MVP | Trial browser Talking Avatar; always provide audio-only option | Proposed; benchmark |
| Initial speech | Trial Sarvam for Hindi-English; retain replaceable adapters | Proposed; benchmark |
| Corrections | One useful correction/turn, let learner finish, preserve meaning, ask when uncertain | Teaching policy |
| Learner data | Keep original and corrected separately, recording off by default | Design requirement |
| Bengali/Punjabi | Later after real-speaker and turn-detection testing | Deferred |
| Pronunciation | Validate on audio with qualified reviewers, not transcript-only | Deferred |
| Fine-tuning | Consent-based reviewed data, Qwen LoRA after baseline proves needs | Deferred |
| Hosting | Repository alone does not run production GPU/voice services | Open infrastructure choice |
| Revenue | Measure real cost and willingness to pay before subscriptions/unlimited calling | Deferred |
| Public GitHub | Current repo is public; no proprietary data/secrets in it | Verified current visibility |

## Open questions for engineering evidence (not blocking the documentation)

- Which Sarvam/alternative STT/TTS combination best recognizes local accents and mixed Hindi-English speech in end-to-end live calls?
- Can the selected Talking Avatar provide suitable lip-sync on midrange Android devices?
- Which authentication and database deployment is simplest for the actual MVP?
- What is the measured full cost of an uninterrupted lesson after all services and taxes?
- Which pronunciation feedback methods align well with bilingual teacher judgments?
- What commercial licensing obligations apply to every selected model weight, avatar asset and speech voice?

When a decision changes, record the *reason, test evidence and date* here.
