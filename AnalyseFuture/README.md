# Preserved work and future analysis

This area separates preserved reference projects, superseded implementations,
future product ideas and dated recovery evidence from the active tutor.

## Functional collections

| Collection | Purpose |
| --- | --- |
| [original-projects](original-projects/reference-sources/README.md) | Original ZIPs, integrity checks and recovery revision for Cadence and Talking Avatar |
| [historical-implementations](historical-implementations/) | Ten superseded source/test/CI payloads preserved before recovery |
| [future-ideas](future-ideas/) | [Detailed vision and roadmap](future-ideas/PROJECT_VISION_AND_FUTURE_ROADMAP.txt) |
| [recovery/inventory](recovery/inventory/) | Earlier inventories, archive manifests and preservation hashes |
| [recovery/features](recovery/features/) | Feature ownership, duplicate analysis and semantic source review |
| [recovery/security](recovery/security/) | Security findings and recorded no-value scan results |
| [recovery/migration](recovery/migration/) | Recovery decisions, consolidation baseline, migration history and debt |
| [recovery/validation](recovery/validation/) | Earlier executed validation evidence, retained by date/commit |
| [recovery/continuation](recovery/continuation/) | Earlier progress and continuation records |

Read [PROJECT_STRUCTURE.md](../PROJECT_STRUCTURE.md) for the current architecture.
The complete mapping for this organization is
[FILE_RELOCATION_MAP.json](recovery/migration/functional-sort-2026-11-17/FILE_RELOCATION_MAP.json),
with [progress](recovery/migration/functional-sort-2026-11-17/WORK_PROGRESS.txt).
The per-file collection index from that organization is
[FUNCTIONAL_FILE_INVENTORY.txt](recovery/inventory/FUNCTIONAL_FILE_INVENTORY.txt).

## How to read historical records

Earlier audit/feature/validation reports are preserved as snapshots of their
recorded commits. Paths and counts inside them refer to those snapshots. Their
original bodies are retained. Use the relocation map to follow paths from that
phase and the root structure document for current operational instructions.

The original preservation manifest is now
[recovery/inventory/PRESERVATION_MANIFEST.json](recovery/inventory/PRESERVATION_MANIFEST.json).
Its 1,478 payloads were verified at the recovery revision, resolving older path
fields through the relocation map. The ten historical copies and their hashes are recorded in
[CONSOLIDATION_BASELINE.json](recovery/migration/CONSOLIDATION_BASELINE.json).

## Original-project integrity

[Source recovery](original-projects/reference-sources/README.md) documents the
original ZIPs and the exact Git revision of the former extracted trees. All
1,474 extracted source, asset, license and fixture files matched their ZIP members
byte for byte before their duplicate working-tree copies were removed.

Keep reference installers outside normal workspace setup. The Cadence desktop
runtime downloader requires an independent integrity check before use.
