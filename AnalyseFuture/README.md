# Preserved work and future analysis

This area separates complete reference projects, superseded implementations,
future product ideas and dated recovery evidence from the active tutor. Placement
here is not a claim that a file is malicious or useless. No preserved application
is installed or executed by the normal active workspace.

## Functional collections

| Collection | Purpose |
| --- | --- |
| [original-projects](original-projects/) | Original ZIPs and complete extracted Cadence/Talking Avatar projects |
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
The current per-file collection index is
[FUNCTIONAL_FILE_INVENTORY.txt](recovery/inventory/FUNCTIONAL_FILE_INVENTORY.txt).

## How to read historical records

Earlier audit/feature/validation reports are preserved as snapshots of their
recorded commits. Paths and counts inside them refer to those snapshots. Their
original bodies are retained so evidence is not silently rewritten. Use the new
relocation map to find the payloads today, and use the root structure document
for current operational instructions. Earlier passing tests do not validate this
new layout: the owner requested that no tests be run during this organization.

The original preservation manifest is now
[recovery/inventory/PRESERVATION_MANIFEST.json](recovery/inventory/PRESERVATION_MANIFEST.json).
Its 1,478 payloads are unchanged; its older location fields can be resolved through
the new map. The ten historical copies and their hashes are recorded in
[CONSOLIDATION_BASELINE.json](recovery/migration/CONSOLIDATION_BASELINE.json).

## Original-project integrity

[Original import navigation](original-projects/reference-sources/README.md) remains
beside the original project structure. Both ZIPs are one level above it, preserving
its relative links. Source, data, fixtures, model binaries, assets, licenses and
credits inside both extracted projects remain unchanged. Each complete project is
kept as a functional unit; it is not flattened into extension-based folders.

Archived installers have known review prerequisites. Existing workspace, package,
TypeScript, browser and Python discovery boundaries exclude these projects. This
is operational separation, not a sandbox against explicitly executing a command.
Never place discovered live credentials or private learner recordings in this
public archive; preserve such evidence through an appropriate private mechanism.
