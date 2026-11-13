# Open-Source Component Reuse Audit — Candidate List

**Not a completed dependency or license audit.** These are repositories to inspect before writing duplicate code. A recommendation to *evaluate* is not permission to copy without checking current license, model weights, assets, maintainer status, and compatibility.

| Need | Candidate | Intended decision |
|---|---|---|
| Live call UI | [LiveKit React starter](https://github.com/livekit-examples/agent-starter-react) | **Core foundation** |
| Streaming voice agent | [LiveKit Python starter](https://github.com/livekit-examples/agent-starter-python) | **Core foundation** |
| Browser avatar/lip sync | [Talking Avatar](https://github.com/InterviewFlowAI/talking-avatar) | **Trial for MVP** |
| Indian-language voice and recognition | [Sarvam](https://www.sarvam.ai/) | **Trial hosted APIs/integrations**; verify live prices and terms |
| Speaking practice modules | [Cadence](https://github.com/pstepanovum/Cadence) | **Study / selectively adapt** |
| Animated tutoring lesson ideas | [Sprigo](https://github.com/ozerozdas/sprigo) | **Study / selectively adapt** |
| Pronunciation | [OpenPronounce](https://github.com/Halleck45/OpenPronounce) | **Experimental evaluation only**; accent/noise accuracy |
| Revision | [TS-FSRS](https://github.com/open-spaced-repetition/ts-fsrs) | **Integrate after lessons save review items** |
| LLM workflow tests | [Promptfoo](https://github.com/promptfoo/promptfoo) | **Integrate once test cases exist** |
| Self-hosted STT | [faster-whisper](https://github.com/SYSTRAN/faster-whisper) | **Later provider comparison** |
| Self-hosted English TTS | [Kokoro](https://github.com/hexgrad/kokoro) | **Later provider comparison** |
| Training | [Unsloth](https://github.com/unslothai/unsloth) | **Prepare later; train only with dataset** |
| Text inference | [vLLM](https://github.com/vllm-project/vllm) | **Later self-hosting** |
| Avatar rendering alternative | [three-vrm](https://github.com/pixiv/three-vrm) | **Alternative, not simultaneous duplicate lip-sync engine** |
| Backend/auth/database | [Supabase](https://github.com/supabase/supabase) or PostgreSQL + selected auth | **Choose one solution, not both stacks** |
| Realtime infrastructure | [LiveKit Server](https://github.com/livekit/livekit) | **Self-hosting option later** |

## Exclusions / safeguards

- **ThirtyTutors** was reported under a noncommercial license; do **not** use its code in a commercial product without verifying and obtaining permission.
- No mass-copying nine repos into the monorepo.
- Do not add second independent WebRTC, voice-session, account, or avatar engine without documented need.
- A package license does not automatically cover its weights, voices, fonts, third-party assets or content.
- OpenPronounce scores are not ready for automatic high-stakes learner judgments without independent tests.
- Prefer official libraries/SDKs and small compatible modules to forks of whole SaaS apps.

## Required Codex audit before adoption

For each candidate, record: version/commit, maintainers and maintenance recency, source license, dependency license, model/asset license, app compatibility, running requirements, latency and deployment cost, tests performed, feature overlap, and decision (**Adopt / Trial / Defer / Reject**). Record evidence in docs/DECISIONS.md or a dedicated audit before integration.
