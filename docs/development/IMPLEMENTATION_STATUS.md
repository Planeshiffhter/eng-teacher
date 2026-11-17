# Current implementation and validation

Updated **18 November 2026 (Asia/Calcutta)**. This page is the current delivery
record. Dated validation and recovery reports retain their original scope.

| Capability | Status | Evidence and limits |
| --- | --- | --- |
| Mock interview and Everyday English | Implemented, partially verified | Signed selection, worker progression, private numeric usage totals, ten-minute deadline logic, subtitles and recaps have automated coverage. Live speech and provider reliability still need a pilot. |
| Café order | Implemented, partially verified | The original role-play introduces a drink order, follow-up details and a new order for independent practice. Live speech and educator review are pending. |
| Tutor correction and help | Verified with scripted text | Policy preserves ordered quantities, signs and repeated numbers, accepts equivalent numeral scripts and keeps the pending target during help. Seven authored scenarios cover 21 scripted turns. Full meaning preservation still depends on recognition and model quality. |
| Quick exercises | Working and verified offline | Original work-update and train scenarios give grammar, vocabulary and dialogue feedback and finish with an ungraded speaking prompt. No room or credentials are required. |
| Optional teacher avatar | Verified with synthetic audio over local LiveKit | An audio analyzer drives two original lightweight portraits from the remote teacher track. LiveKit owns playback. The audio-only default and fallback are available. This amplitude-driven animation has no phoneme-level visemes. Live speech and physical-device performance still need testing. |
| Self-listening | Working and verified with synthetic browser audio | An explicit browser recording lets the learner replay a short example attempt. It makes no uploads and releases the microphone and clip on exit. Physical-device compatibility remains to be tested. |
| Pronunciation assessment, Bengali–English support and learner accounts | Not implemented | Model and educator validation are required for pronunciation and language support. Persistent learner progress requires consent and account and deletion controls. |

The runtime boundaries are `apps/web/features/lesson` for the live experience,
`session` for restricted admission and token signing, `avatar` for the visual
adapter, and `practice` and `pronunciation` for offline learning and self-listening.
The Python worker owns the tutor policy under `teaching`, the speech/model
boundary under `providers` and the timed room and private usage under `runtime`.
The public session route, feedback version, legacy default lesson and
microphone-only grants remain compatible. Deploy the web app and worker from
the same revision so their catalogs agree.

## Validation

The pre-change checkpoint
[`600a361`](https://github.com/Planeshiffhter/eng-teacher/commit/600a361e9f97a76603aa260141ce3876d7b94c62)
passed **24 web, 136 worker, 8 maintenance and 8 Chromium tests**. After the
changes, **30 web, 168 worker, 8 maintenance and 18 desktop/mobile Chromium
tests** passed. Production build, TypeScript, Ruff lint and formatting passed.
Browser coverage checks lesson selection, simulated connection failure, avatar
selection and fallback, synthetic audio analysis and recording cleanup.

A separate local smoke check used checksum-verified LiveKit 1.13.11. The web app
rejected an incorrect pilot code and issued a valid token for Everyday English.
Both a native learner and managed Chromium reached the named synthetic worker
over real WebRTC. Chromium used LiveKit's loopback TCP media configuration
(`rtc.force_tcp` and `rtc.enable_loopback_candidate`) with the existing browser
policy. The test exercised audio in
both directions, both avatar choices, muted and unmuted microphone, audio-only
fallback, separate original and corrected text, recap, and disconnect. Only the
teacher's audio moved the avatar. One audio element handled playback throughout.
This run used synthesized audio and a test worker. OpenAI speech, barge-in,
reconnect and physical-device performance still need testing.

The [development guide](DEVELOPMENT.md) lists commands. The
[live acceptance checklist](VALIDATION.md#live-acceptance-still-required)
covers provider and physical-device testing.

## Repository integrity and dependencies

Git object integrity passed for the advertised GitHub branches and tags. The
redacted credential-pattern scan covered 63 reachable commits, 1,727 unique
blobs and 1,474 ZIP members at the starting remote state and found no matches.
A historical workflow at
[`2bf1868`](https://github.com/Planeshiffhter/eng-teacher/commit/2bf1868)
printed six tracked Python files in CI. That step was removed at
[`da2796e`](https://github.com/Planeshiffhter/eng-teacher/commit/da2796e).
Run visibility and account access history could not be verified here. The owner
can check GitHub access history, installed apps, keys and Actions logs, and
rotate credentials with plausible exposure.

The npm production advisory scan returned zero results. The full development
tree contains an unresolved high-severity
[picomatch advisory](https://github.com/advisories/GHSA-fc5q-39xc-vjpf) through
Vitest. No fixed version was published at the time of the check. PyPI metadata
returned no active advisories for the 85 locked Python releases. Access to
uv's separate OSV feed was blocked.

Both original reference ZIPs passed byte-for-byte recovery checks before the
duplicate extracted trees were removed. The Cadence desktop runtime downloader
extracts a network or cached artifact without an independent integrity check.
It remained outside the active app and was not run. The active product uses
original exercise and visual implementations. See the
[reference decisions](../research/TWO_PRIMARY_REFERENCE_REPOS.md) and
[recovery instructions](../../AnalyseFuture/original-projects/reference-sources/README.md).

## Next acceptance checks

1. Run a complete ten-minute voice lesson on desktop and physical Android with
   authorized LiveKit and OpenAI access. Verify greeting, speech, help, retry,
   captions, interruption, audio-only fallback, reconnect and cleanup. Measure
   latency and usage with actual provider audio.
2. Have bilingual reviewers evaluate the held-out Hindi–English turns and correct
   English controls. Review Bengali recognition, explanation and synthesis
   separately before offering a language preference.
3. Measure avatar behavior and performance on a physical phone. Evaluate
   candidate audio-based pronunciation feedback with qualified teachers before
   presenting scores. Individual accounts and privacy controls come before
   persistent progress and personalized review.
