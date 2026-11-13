# Voice MVP dependency audit

Inspected on 13 November 2026. This is the focused adoption record for the first microphone → tutor → spoken response implementation. It records source and package evidence; it is not a completed commercial release review of every transitive dependency, voice, service term or model artifact.

## Official foundations adopted

| Foundation | Exact inspected commit | Latest commit date at inspection | License evidence | Decision and scope |
| --- | --- | --- | --- | --- |
| [LiveKit React starter](https://github.com/livekit-examples/agent-starter-react/tree/9e1fc2f40fd7ceaccbe4a872b21765b49eefea80) | `9e1fc2f40fd7ceaccbe4a872b21765b49eefea80` | 19 October 2026; Next.js security update | Repository `LICENSE`: MIT, Copyright 2025 LiveKit, Inc. | Adopt its Next.js, server-side token issuance, LiveKit room/audio and transcript integration foundation; keep a minimal lesson UI rather than copy the whole component catalog. |
| [LiveKit Python starter](https://github.com/livekit-examples/agent-starter-python/tree/228095c442fcb259c80e9786fc0d7c5534e6af46) | `228095c442fcb259c80e9786fc0d7c5534e6af46` | 4 November 2026; initial greeting update | Repository `LICENSE`: MIT, Copyright 2025 LiveKit, Inc. | Adopt `AgentServer`/`AgentSession`, connection and greeting lifecycle; replace the general assistant with structured tutor policy and configurable speech/model adapters. |

Both repositories are maintained by the LiveKit examples organization. Recent commits are maintenance evidence, not a guarantee of future support. Starter MIT notices are preserved in `apps/web/LICENSE`, `services/voice-agent/LICENSE` and [THIRD_PARTY_NOTICES.md](../THIRD_PARTY_NOTICES.md). No avatar, brand illustration, external lesson content or unrelated application is imported.

## Runtime packages and compatibility

The checked-in npm and uv lockfiles are the authoritative resolved inventory. Versions below identify directly inspected foundation releases and installed Python packages; a compatible npm range may resolve a newer patch in the lockfile.

| Package | Version inspected | Declared license and evidence | Purpose / compatibility |
| --- | --- | --- | --- |
| `@livekit/components-react` | 2.9.24 | Apache-2.0, npm metadata and tarball `LICENSE` | Official React room/audio/hooks; compatible with the starter's React 19 foundation. |
| `livekit-client` | 2.22.2 | Apache-2.0, npm metadata and tarball `LICENSE` | Browser WebRTC microphone, remote audio, data packets and transcription. |
| `livekit-server-sdk` | 2.18.0 | Apache-2.0, npm metadata and tarball `LICENSE` | Server-side room-scoped access tokens and named agent dispatch. |
| `next` | 15.5.29 adopted; 15.5.27 in inspected starter | MIT, npm metadata | Adopt the newer 15.5.29 security backport after the initial dependency audit reported advisories against upstream 15.5.27. App Router server-side API routes keep provider keys out of client bundles. |
| `react`, `react-dom` | 19.x; 19.0.0 foundation inspected | MIT, npm metadata | Browser UI. Node 24 is the inspected starter's declared runtime. |
| `livekit-agents` | 1.8.11 | Apache-2.0, installed/PyPI metadata | Current SDK matching the Python starter's `~=1.8`; Python 3.12 installed. |
| `livekit-plugins-openai` | 1.8.11 | Apache-2.0, installed/PyPI metadata | Official speech recognition and synthesis integrations; no custom speech infrastructure. |
| `livekit-plugins-silero` | 1.8.11 | Apache-2.0 plugin, installed/PyPI metadata | Local CPU voice activity detection. See separate model note below. |
| `livekit`, `livekit-api` | 1.2.0, 1.2.2 | Apache-2.0, installed metadata | RTC transport and server room lifecycle. |
| `openai` | 3.50.0 | Apache-2.0, installed/PyPI metadata | Replaceable structured tutor-model adapter. |
| `pydantic` | 2.14.3 | MIT, installed/PyPI metadata | Validate tutor decisions and keep original transcript separate from corrections. |
| `python-dotenv` | 1.2.4 | BSD-3-Clause, installed/PyPI metadata | Local server-only configuration. |
| `onnxruntime` | 1.31.1 | MIT, installed metadata and package `LICENSE` | CPU inference for the bundled Silero VAD model; no GPU required. |

Apache-2.0 permits commercial reuse subject to its conditions, including preserving notices and license text and marking modifications to copied source. MIT and BSD-3-Clause also require retaining their notices. These package licenses do not supply commercial rights to arbitrary external models, voices or assets. Retain package-manager license files and produce an exact transitive inventory before distributing production binaries.

The first npm audit also reported advisories in the initial test tooling and PostCSS resolution. The implementation updates Vitest to 4.1.12 and overrides PostCSS to 8.5.32; these are security maintenance changes relative to the inspected starter. Both declare MIT licenses in npm metadata. The final audit result belongs with the actual test results; updating version numbers alone does not establish a clean dependency tree.

## Speech/model selection

| Need | Initial adapter | Decision / outstanding evidence |
| --- | --- | --- |
| Recognition | Official OpenAI plugin, multilingual `whisper-1`, with automatic language detection | Trial. English/Hindi recognition is supported by the provider interface, but code-switching, names, negation and noisy mobile microphone quality need real audio evaluation. Do not force an English-only recognition language. |
| Tutor reasoning | OpenAI structured JSON model adapter, default `gpt-4.1-mini` | Trial. Explicit single-correction, meaning-preservation and clarification instructions plus schema/state guards; no claim of guaranteed teaching accuracy. Provider implementation and model are replaceable. |
| Spoken response | Official OpenAI plugin, default `gpt-4o-mini-tts` and `coral` voice | Trial. Voice/model are configurable. Verify actual pronunciation, bilingual speech, naturalness and voice permissions under the account's current terms. |
| Turn detection / interruption | Official Silero VAD plugin plus LiveKit's interruption handling | Adopt framework capability. Listening pauses, barge-in and playback timing still require a real device/provider test. Batch Whisper recognition may add turn latency; measure before choosing a streaming replacement. |
| Hindi-focused alternative | Sarvam through an official compatible adapter, if selected later | Defer dependency until real Hindi-English evaluations justify adoption. No Sarvam credential is required for the current adapter. |
| Avatar | None | Defer. Current lesson is explicitly audio-only; no avatar operation is claimed. |

All selected inference/speech models above are hosted services. No model weights, proprietary speech engine or recording dataset is copied. Access requires account credentials and provider/network access. SDK license inspection is not acceptance of hosted-provider terms. Recheck model availability, service terms, retention settings, region and current prices before a paid pilot. No benchmark, per-lesson cost or latency target has been measured merely by selecting these adapters.

## Silero model artifact

The installed `livekit-plugins-silero` 1.8.11 wheel includes `livekit/plugins/silero/resources/silero_vad.onnx` (2,327,524 bytes), SHA-256 `1a153a22f4509e292a94e67d6f9b85e8deb25b4988682b7e174c65279d8788e3`. It can run on CPU from the installed package, so this release does not require a separate model download for the default VAD.

The [upstream Silero VAD license](https://github.com/snakers4/silero-vad/blob/master/LICENSE), read during this audit, is MIT, Copyright 2020-present Silero Team; that notice is retained in THIRD_PARTY_NOTICES.md. The plugin wrapper is Apache-2.0. The installed package does not identify a separate upstream model commit in its package metadata; the exact model-to-upstream revision provenance remains a commercial distribution review item. The artifact hash identifies what was tested, not an independent origin attestation. No additional TTS, ASR or LLM weights are downloaded.

## Validation boundaries

Dependency installation, SDK import/signature checks, offline tutor-policy tests, web build/type checks and browser/UI tests demonstrate development integration only. Tests with deterministic/fake model outputs are not real speech or educational-quality evaluations. See the setup/testing documentation for actual commands and results.

No LiveKit or OpenAI service credentials were present at initial implementation inspection. A connected mobile microphone → recognition → tutor → voice test, Hindi-English teacher-reviewed cases, interruption/slow-pause behavior, reconnect handling, full 10-minute timing and latency/cost measurements therefore remain required with real accounts. Record those outcomes separately from offline tests before claiming the live product works.
