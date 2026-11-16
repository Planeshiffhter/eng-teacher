# Material preserved for future analysis

This folder keeps the uploaded projects and original ZIPs available without mixing
their applications into Eng Teacher's active source tree. Nothing here was removed
because it appeared unnecessary, and placement here is not a finding of malicious
code. Future use requires an explicit integration decision and appropriate review.

| Location | Contents |
| --- | --- |
| [reference-sources/Cadence-main](reference-sources/Cadence-main/) | Complete extracted Cadence snapshot: web, Python services, mobile, desktop, content and tests |
| [reference-sources/talking-avatar-master](reference-sources/talking-avatar-master/) | Complete extracted Talking Avatar SDK, model, avatars and tests |
| [Cadence-main.zip](Cadence-main.zip) | Original uploaded Cadence archive |
| [talking-avatar-master.zip](talking-avatar-master.zip) | Original uploaded Talking Avatar archive |
| [reference-sources/ARCHIVES.json](reference-sources/ARCHIVES.json) | Original archive hashes and extracted file counts |
| [PRESERVATION_MANIFEST.json](PRESERVATION_MANIFEST.json) | Previous/new paths and SHA-256 for all 1,478 relocated files |

The ZIPs stay at this level so the original snapshot README's relative links keep
working. All relocated payloads, including the snapshot README and original
manifest, match their pre-move bytes. Upstream licenses, notices, model files,
assets and credits remain intact. Do not run archived install or deployment scripts
as part of the active app's setup merely because they are present here.

The active project remains in `../apps/web` and `../services/voice-agent`, with
cross-component browser tests in `../tests/browser`. See the
[repository audit and structure](../docs/REPOSITORY_STRUCTURE.md) for the findings
and the [product idea](../PROJECT_IDEA.txt) for planned features and limitations.
