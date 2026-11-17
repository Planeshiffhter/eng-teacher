# Functional organization record

Date: 17 November 2026 (Asia/Calcutta).

Starting commit: `05269aec2449605756a6bfa2beadc98ce714b9a3`.
Backup tag: `recovery/pre-functional-sort-20261117-05269ae`, pushed before edits.
First organization checkpoint: `4e33517` on `main`, with `[skip ci]`.

## Whole-repository decisions

- All 1,567 starting tracked files have a row in `FILE_RELOCATION_MAP.json`.
  Destinations were selected by ownership, dependencies and runtime role, not
  extension. There were no untracked non-ignored user files at discovery.
- 1,525 original files moved into functional collections. Forty-two initial
  locations stayed because they already match a feature or a tool convention.
- Documentation now separates product, architecture, development, research,
  continuity and legal material. Recovery evidence is grouped by report subject;
  future ideas have a separate collection.
- Original uploads and extracted projects moved inside one wrapper. Every
  internal upstream path, asset, source file, test, notice and relative ZIP link
  remains intact. Historical implementation snapshots are already properly
  grouped and were retained in place.
- The Python service separates teaching, provider adapters and runtime. Fixtures
  follow those owners. Package markers support the relocated relative imports.
  The declared CLI entrypoint remains `eng_teacher.agent:main`; a small
  compatibility module delegates to the runtime implementation. Internal source
  imports now use `eng_teacher.teaching`, `eng_teacher.providers.openai` and
  `eng_teacher.runtime`; any separately maintained internal imports should follow
  those namespaces. No dependency declaration or lockfile change was needed.
- Web lesson/session features, thin Next.js routes, service working directories,
  root workspace/test configuration and app-local licenses remain conventional.
- Installed dependencies, builds and caches are preserved as ignored local state.
  Their 24,622 discovery paths are generated/local artifacts, not source to flatten
  into new folders or push into Git.

## Static evidence collected

No tests, builds, installs, application imports or application startup ran in this
task. No test collection or lint runner was invoked. Organization commits use
`[skip ci]` to avoid starting the existing GitHub Actions test workflow.

The inspection read the new Python syntax with the standard-library AST parser
without importing it. Internal module references resolve to their moved source
files/package markers. Comparing the seven moved service/fixture modules against
the starting Git blobs shows unchanged bodies after removing module import
declarations. Current namespace/package setup is statically reviewed; execution
is not represented as validated.

The 1,478 original import payloads and ten superseded historical payloads remain
byte-identical through the location map. Canonical Markdown links were rebased
from their original resolved targets; two same-collection links found during
inspection were corrected. Original historical report contents and their dated
path/count statements remain preserved rather than being rewritten as new claims.

`FILE_RELOCATION_MAP.json` records old/new paths, original SHA-256, current SHA-256,
collection and whether a payload only moved or needed import/navigation/tool-path
adaptation. The new functional inventory covers every intended tracked file.
It uses static definitions/imports and recorded ownership, not a claim that every
binary/model/media asset was semantically validated.

## Delivery and limits

All changes are delivered through normal commits directly to `main`. No feature
branch, PR, force push, history reset or branch/tag deletion is used. Original
work remains recoverable from the backup tag and explicitly mapped files.

Runtime, type/build and test behavior must be checked in a later authorized task.
Earlier 14/71/6 results in preserved recovery reports apply to their old recorded
tree, not to this new module layout. Live speech, provider access, device behavior,
language quality and archived model/application execution remain outside this
organization-only task.
