# Module validation and fixes

Date: **17 November 2026 (Asia/Calcutta)**.
Starting source: `eeb15dbd8240ae96ed76a94c8518fb122cbb10b3`.

This pass exercises the active application, maintenance tools and the runnable
reference modules. The reference projects were tested in isolated copies outside
the checkout. Their original source, ZIPs, licenses and historical snapshots
remain unchanged. Native applications and paid/live services have separate
prerequisites and are explicitly listed below.

## Results

| Module or boundary | Executed result | Scope |
| --- | --- | --- |
| Active web lesson/session modules and Next API handler | **24 tests passed**, four Vitest files | Local JWT signing, grants, selected lesson, input/media/origin failures, route budget, parser and lesson contracts |
| Active Python voice service | **136 tests passed** | Tutor/controls, lesson catalog, provider adapters, numeric usage, SDK scheduler and worker lifecycle |
| Repository maintenance tools | **8 tests passed** | Real CLI invocations against disposable local Git fixtures; no application imports |
| Active browser UI | **8 tests passed**, zero skipped/flaky | Desktop/mobile viewports, synthetic microphone, selected mode, controls and failure recovery |
| Preserved Cadence pure modules | **470 tests passed**, 95 suites, 44 files; zero skipped/cancelled | Content, domain logic, contracts and selected dependency-free server helpers |
| Preserved Talking Avatar DSP/model modules | **16 tests passed**, zero skipped | Coarticulation, resampling, viseme detection and bundled model parity |

That is **662 successful automated test cases**: 176 in the active project and
486 in isolated references. The root Python run reports **144 passed**, which is
the same 136 service plus 8 maintenance cases, not 144 additional tests.

Other executed checks passed:

- Active production build, TypeScript, service Ruff lint/format and maintenance
  Ruff lint/format.
- Installed `eng-teacher-agent --help` through the compatibility entrypoint.
- Actual production HTTP checks with deliberately fake, local-only configuration.
- Avatar package typecheck, build and package dry-run in its isolated copy.
- Actual browser WebGL/AudioWorklet/model and disposal smoke scenarios.
- Packaged Silero CPU VAD inference: one second of synthetic 16 kHz mono silence
  produced 31 inference events and zero speech-start events, without downloads,
  provider calls or microphone access. This checks native/model loading and the
  streaming path, not speech-detection accuracy on human recordings.
- Active npm advisory audit: **zero known advisories** for the resolved active lock.
- Hash preservation for all **1,478** original import payloads and **10** historical
  implementation payloads.

Machine-readable evidence is under
[evidence/module-validation-2026-11-17](evidence/module-validation-2026-11-17/).
The summaries identify which commands ran and which scenarios were exercised.
No real JWT, secret or provider response payload is stored in those results.

## Fixed: worker resource lifecycle

Checkpoint: [`ca5ceb4`](https://github.com/Planeshiffhter/eng-teacher/commit/ca5ceb4).

The former initialization path constructed clients and SDK components before the
guarded lifecycle and shutdown callback existed. A model/LLM/STT/TTS/VAD/session
construction failure could escape while earlier clients stayed open. A failing
session close could also prevent model cleanup and room deletion.

The worker now registers cleanup before initialization, records each constructed
resource and makes best-effort, idempotent close attempts in reverse order. A
close failure cannot skip the remaining clients or room deletion. Startup
cancellation performs cleanup and propagates. Background packet-task exceptions
are retrieved without logging private exception text; failed lazy initialization
restores the intended private logger levels.

Ten new lifecycle regressions reproduce these paths, including factory failures,
missing configuration, close failure, cancellation and background transport errors.
The installed SDK scheduler tests remain in the suite. These results do not prove
that every external SDK/network failure can be forced closed under all conditions.

## Fixed: JSON media-type admission

Checkpoint: [`0650864`](https://github.com/Planeshiffhter/eng-teacher/commit/0650864).

The session policy used a prefix comparison, accepting `application/json-invalid`
and rejecting valid mixed-case `Application/JSON`. Regression tests demonstrated
both failures. The policy now compares the normalized media type exactly while
retaining valid charset parameters.

New Next API handler tests verify successful signing, no-store responses, typed
admission failures, missing/malformed configuration without secret exposure and
the request budget's 429/Retry-After response. These use actual installed token
signing/verification with explicit test-only keys, not a remote LiveKit project.

## Fixed: maintenance module verification gap

The maintenance inventory failed its formatting check after the organization
moves. It is now formatted, and both scripts have direct CLI regression coverage.
The tests create disposable Git fixtures, including paths with spaces, immutable
history, staged files, binary input, synthetic credential candidates and ZIPs.

Coverage verifies that inventory does not execute inspected Python source, scans
do not print candidate values, historical candidates remain detectable, ZIP
members are read without extraction, and corrupt ZIPs produce a failed scan rather
than a false clean result. Synthetic candidates exist only in temporary fixtures;
no credential was introduced into the real repository.

`npm run test:maintenance` and maintenance lint/format are now part of CI. Default
root pytest discovers the service and maintenance tests while still excluding
all `AnalyseFuture` source trees. The tools' output ownership now recognizes
maintenance fixtures separately from browser scenarios.

## Production HTTP smoke

An isolated child server bound to loopback port 3202 used deliberate offline-only
keys and `ws://127.0.0.1:1` as the nonfunctional media URL. No browser joined a
room, and no real LiveKit/OpenAI/provider request occurred. The owned process
group was stopped afterward.

Ten scenarios passed: page 200, configured session 200, invalid media 415,
mixed-case JSON 200, wrong code 401, wrong origin 403, unknown lesson 400,
malformed JSON 400, oversized body 413 and request budget 429 with retry hint.
The produced test token was verified in memory for its HMAC signature, issuer,
room/learner scope, selected Everyday English metadata, named worker, microphone
grants, two-participant limit and original ten-minute TTL/deadline. Tokens and
fake key values were omitted from saved evidence.

## Isolated reference validation

### Cadence

The audited dependency-free group ran under Node 24 with no installation or app
startup. It covered `tests/auth`, `cloud`, `content`, `platform`, `pairing`, `web`,
`email`, selected mobile sync/desktop update/release contracts, and two pure server
helpers. The exact 44-file argument list is retained in
[cadence-pure-modules.json](evidence/module-validation-2026-11-17/cadence-pure-modules.json).
All 1,443 original source files remained byte-identical.

### Talking Avatar

The isolated copy used its committed npm lock and `npm ci --ignore-scripts`.
Typecheck, 16 tests, build and package dry-run passed. The package includes required
exports, model/assets and license notices. All 31 original source files remained
byte-identical; generated dependencies/builds stayed in the isolated copy.

A system Chromium browser with software WebGL then loaded the local female GLB
and model, attached muted synthetic 48 kHz audio, observed actual AudioWorklet
capture/model events, detached without stopping the caller-owned source, reattached,
swapped to the male GLB and disposed twice. Disposal removed the canvas, closed
the SDK context and detached the stream; the harness stopped its own audio source.
Both avatars and the model returned local HTTP 200. There were no external
requests, SDK/page errors or browser console errors.

[Female render](evidence/module-validation-2026-11-17/avatar-female.png) and
[male render](evidence/module-validation-2026-11-17/avatar-male.png) were visually
inspected. This is isolated SDK evidence, not an avatar integration in Eng Teacher.
The supplied characters derive from Microsoft Rocketbox. See the
[Microsoft avatar and SDK/model notices](../legal/THIRD_PARTY_NOTICES.md#preserved-uploaded-project-archives).

## Not run and remaining prerequisites

These are **unexecuted**, not passed or skipped test results:

- A real learner microphone -> LiveKit -> OpenAI -> teacher audio lesson. Actual
  LiveKit/OpenAI/pilot variables and local environment files were absent when
  checked. Real provider permissions, media/TURN connectivity and service billing
  require operator configuration and human acceptance.
- Physical Android/other device performance, real Hindi/Bengali recognition and
  teaching quality, pronunciation calibration and live interruption latency.
- Avatar React-wrapper lifecycle, LiveKit teacher-track integration and real
  speech/phone lip-sync quality. Synthetic local rendering does not establish them.
- Complete archived Cadence browser/native/desktop deployments, Firebase/emulator
  rules and billing/OAuth/MCP/provider integrations, release/publish operations,
  Python speech model downloads/inference and desktop installer execution.
  Those require separate dependencies/platforms/infrastructure. No unsafe installer
  or cloud side effect was invoked to obtain a passing result. Its previously
  recorded downloader checksum gap remains a future adoption prerequisite.
- A Python dependency advisory database scan, formal penetration test or remote
  GitHub Actions/security audit. The current report records local execution.

No active test/build/type/lint failure remains. That is a scoped engineering result,
not a claim that every archived application or external service is production-ready.

## Repeat the active checks

From the repository root with the existing Node 24/Python 3.12 environment:

```sh
npm test
UV_CACHE_DIR=/workspace/.cache/uv npm run test:agent
UV_CACHE_DIR=/workspace/.cache/uv npm run test:maintenance
UV_CACHE_DIR=/workspace/.cache/uv uv run --frozen --project services/voice-agent ruff check services/voice-agent scripts/maintenance tests/maintenance
UV_CACHE_DIR=/workspace/.cache/uv uv run --frozen --project services/voice-agent ruff format --check services/voice-agent scripts/maintenance tests/maintenance
NEXT_TELEMETRY_DISABLED=1 npm run build
npm run typecheck
CI=1 NEXT_TELEMETRY_DISABLED=1 npm run test:browser
```

Stop only owned dev/start servers before rebuilding the shared `.next` directory.
Do not include archived code in default app tests or normal setup. Reference
validation copies and their generated state are outside the Git checkout.
