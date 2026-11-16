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
| [historical-implementations/pre-consolidation-98cfcd7](historical-implementations/pre-consolidation-98cfcd7/) | Ten superseded code/test/CI payloads retained before consolidation |
| [recovery-notes/CONSOLIDATION_BASELINE.json](recovery-notes/CONSOLIDATION_BASELINE.json) | Original paths and SHA-256 for those ten payloads |
| [repository-inventory](repository-inventory/) | Detailed semantic review and no-value security scan evidence |

## Complete recovery records

Begin with [REPOSITORY_AUDIT.txt](REPOSITORY_AUDIT.txt) and
[WORK_PROGRESS.txt](WORK_PROGRESS.txt). The full
[file inventory](COMPLETE_FILE_INVENTORY.txt) covers every current tracked path;
the [feature inventory](FEATURE_INVENTORY.txt) records 77 scoped implementation
and responsibility groups, including overlapping archived client variants.

- [Duplicate analysis](DUPLICATE_ANALYSIS.txt)
- [Security audit](SECURITY_AUDIT.txt)
- [Original/new path mapping](ORIGINAL_TO_NEW_PATH_MAPPING.txt)
- [Consolidation report](CONSOLIDATION_REPORT.txt)
- [Archived files manifest](ARCHIVED_FILES_MANIFEST.txt)
- [Future vision and roadmap](PROJECT_VISION_AND_FUTURE_ROADMAP.txt)
- [Technical debt](TECHNICAL_DEBT.txt)
- [Test and validation report](TEST_AND_VALIDATION_REPORT.txt)
- [Migration summary](MIGRATION_SUMMARY.txt)
- [Next developer instructions](NEXT_DEVELOPER_INSTRUCTIONS.txt)

The ZIPs stay at this level so the original snapshot README's relative links keep
working. All relocated payloads, including the snapshot README and original
manifest, match their pre-move bytes. Upstream licenses, notices, model files,
assets and credits remain intact. Do not run archived install or deployment scripts
as part of the active app's setup merely because they are present here.

The active project remains in `../apps/web` and `../services/voice-agent`, with
cross-component browser tests in `../tests/browser`. See the
[repository audit and structure](../docs/REPOSITORY_STRUCTURE.md) for the findings
and the [product idea](../PROJECT_IDEA.txt) for planned features and limitations.

Active web responsibilities now live in `apps/web/features/lesson` and
`apps/web/features/session`. Root `pytest.ini` prevents ordinary default test
collection from importing the archived Python modules. Explicitly running an
archived command is still possible; this folder is not a security sandbox.
