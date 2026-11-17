# Project structure

This is the current map of the AI English-speaking companion. Files are grouped
by the responsibility they serve. Reference ZIPs preserve complete upstream
project layouts.

For current delivery status, detailed continuation tasks and contributor PR
instructions, read [PROJECT_HANDOFF.md](PROJECT_HANDOFF.md). The
[file guide](docs/development/REPOSITORY_FILE_GUIDE.md) links the active collections
and the historical per-file appendix.

Organization date: **17 November 2026 (Asia/Calcutta)**. Starting commit:
`05269aec2449605756a6bfa2beadc98ce714b9a3`.

**Implementation has resumed with testing.** The organization-only policy below
records that completed phase. See
[IMPLEMENTATION_STATUS.md](docs/development/IMPLEMENTATION_STATUS.md) for current
lesson selection, private usage accounting and the latest executed checks.

## Main collections

```text
eng-teacher/
  README.md                         Project introduction and navigation
  PROJECT_STRUCTURE.md              This current ownership map
  AGENTS.md                         Owner/maintainer working agreement
  package.json / package-lock.json   npm workspace entrypoint and frozen lock
  .nvmrc / .gitignore                Runtime pin and generated/local exclusions
  playwright.config.ts              Browser runner entrypoint
  pytest.ini                        Default active Python discovery boundary
  .github/workflows/                 Root GitHub Actions entrypoints

  apps/web/
    app/                            Next.js page/layout/styles/API entrypoints
    features/
      lesson/
        catalog.ts                  Public lesson choices and safe lookup
        components/                 Call UI, microphone/audio, captions and recap
        tutor-events.ts             Untrusted event contract and bounded state
        tests/                      Event and lesson helper fixtures
      session/
        server/                     Admission, pilot code, origin/budget and JWTs
        tests/                      Session policy fixtures
      avatar/                      Optional remote-audio teacher animation
      practice/                    Standalone scenario exercises and feedback
      pronunciation/               Local self-listening recorder and tests
    package.json / tsconfig.json    App-local build and type configuration
    .env.example / LICENSE          App configuration example and attribution

  services/voice-agent/
    src/eng_teacher/
      __init__.py                   Package identity
      agent.py                      Stable CLI compatibility entrypoint only
      teaching/
        lessons.py                  Original immutable guided lesson curriculum
        tutor.py                    Interview policy, correction/retry and guards
        controls.py                 Learner help/repeat/example/skip recognition
      providers/
        openai.py                   Settings and current speech/text adapters
      runtime/
        agent.py                    SDK audio pipeline, privacy and room lifecycle
        usage.py                    Bounded private numeric usage totals
    tests/
      teaching/                     Tutor, control and provider-contract fixtures
      runtime/                      SDK scheduling and lifecycle fixtures
      evaluations/                  Scripted teaching-policy evaluations
    pyproject.toml / uv.lock         Service packaging, CLI and frozen dependencies
    .python-version / .env.example   Runtime pin and service configuration names
    LICENSE                         Service attribution

  tests/browser/                    Cross-component browser scenarios
  tests/contracts/                  Shared lesson-ID/default contract fixtures
  tests/maintenance/                Isolated Git-fixture CLI regressions
  scripts/maintenance/               Read-only inventory and security utilities

  docs/
    README.md                       Documentation catalogue
    product/                        User problem, detailed idea, acceptance, roadmap
    architecture/                   Design, decisions and implementation topology
    development/                    Setup, validation, checklist and coding briefs
    research/                       Prior research, reference studies and inventory
    continuity/                     Project history and continuation context
    legal/                          Attribution and dependency/license review

  AnalyseFuture/
    README.md                       Preservation and evidence catalogue
    original-projects/
      Cadence-main.zip              Original uploaded archive
      talking-avatar-master.zip    Original uploaded archive
      reference-sources/
        README.md / ARCHIVES.json  ZIP integrity, source recovery and provenance
    historical-implementations/
      pre-consolidation-98cfcd7/     Ten superseded source/test/CI payloads
    future-ideas/                   Detailed long-term vision and research roadmap
    recovery/
      inventory/                    File inventories, old mapping and hash manifests
      features/                     Feature/duplicate reports and semantic evidence
      security/                     Security findings and scan evidence
      migration/                    Recovery decisions, debt and migration records
        functional-sort-2026-11-17/ Complete mapping for this reorganization
      validation/                   Earlier executed-check reports, retained by date
      continuation/                 Earlier progress and continuation records
```

Package initializers inside the new Python directories are explicit package
boundaries. They contain no duplicated tutor implementation. The CLI module at
`eng_teacher/agent.py` delegates to `runtime/agent.py`, retaining the installed
`eng-teacher-agent` command and the existing packaging declaration. The worker's
working directory and `.env.local` lookup are unchanged. Runtime fixture imports
now refer to the runtime owner; shared teaching fixtures use a package-relative
import rather than relying on a flat test folder.

## Organization record from 17 November 2026

All **1,567 starting tracked files** were read and given an explicit destination
or a reason to stay. **1,525 original payloads moved**; **42 initial paths stayed**
where their existing functional or framework role was already correct. New index,
package-boundary and navigation files supplement the organization. The final tracked
organization index contained **1,580 files**, including those new navigation, package and
preservation records.

The complete old/new record is
[FILE_RELOCATION_MAP.json](AnalyseFuture/recovery/migration/functional-sort-2026-11-17/FILE_RELOCATION_MAP.json).
It covers every starting path, including deeply nested files; it is not only a
list of top-level directories. That phase's per-file ownership/import inventory is
[FUNCTIONAL_FILE_INVENTORY.txt](AnalyseFuture/recovery/inventory/FUNCTIONAL_FILE_INVENTORY.txt).

- Product documents explain who learns, what the teacher should do and what is
  proposed. They are not implementation or proof of speech quality.
- Architecture documents explain runtime responsibilities and decisions.
- Development documents own install/run instructions, earlier validation and
  implementation sequencing. Continuity owns dated project history.
- Research and legal documents retain previous findings and rights obligations.
- Recovery reports are categorized by their actual subject. Historical reports
  remain snapshots of their recorded commits; old paths are resolved through the
  new relocation map rather than rewriting forensic evidence silently.
- Web lesson and session folders already had clear owners and remain intact.
  The Python service now has the same visible separation between teaching,
  providers and runtime. Browser scenarios stay cross-component.

## Why some things remain together

The original Cadence and Talking Avatar ZIPs preserve source, configuration,
assets, tests, documentation and notices. Each formerly extracted copy matched
its corresponding ZIP byte for byte before the duplicate copies were removed.
See [source recovery](AnalyseFuture/original-projects/reference-sources/README.md)
for the Git recovery revision and [feature analyses](AnalyseFuture/recovery/features/)
for component findings.

Likewise, root package manifests, framework configuration, app-local licenses,
environment examples and GitHub's root workflow directory are conventional tool
entrypoints. They stay at the paths those tools expect. This organization is by
responsibility, not by extension and not by moving every configuration into one
unrelated global folder.

Prior hash manifests retain their recorded paths. The recovery revision contains
the 1,478 original import payloads and ten historical implementation payloads.
The ten historical implementation payloads also remain in the working tree.

## Execution boundaries and local state

The active npm workspace remains only `apps/web`; app TypeScript stays app-local.
Python packaging still finds the service under `src`, with explicit subpackages.
Root `pytest.ini` continues to exclude all `AnalyseFuture`; Playwright still owns
only `tests/browser`. Historical workflows stay outside root `.github/workflows`.
Keep reference installers outside normal setup.

There were **24,622 ignored local/generated files** at discovery: installed npm
dependencies, Python dependencies/cache, Next output and runner caches/results.
They are classified as generated/local state and preserved at tool-required paths;
they are not recommitted, flattened into source folders or represented as original
project code. No untracked non-ignored user files were present at discovery.

## Historical organization verification policy

**No tests, builds, installations, application imports or startup were run.**
The owner explicitly requested organization only. Earlier test results retained
in recovery/validation are historical and do not validate this new layout.

Review is limited to Git/path inventories, byte hashes, static Python syntax and
import resolution, Markdown references, declared entrypoints and the complete
diff. Organization commits use `[skip ci]` so normal pushes do not start the
existing GitHub Actions test workflow. The workflow itself remains intact for a
later authorized validation task.

Before claiming runtime readiness, a later task should install/refresh only as
needed and run the existing scoped checks for the reorganized paths. Current CLI
compatibility is maintained structurally, but execution was deliberately deferred.

## Pre-organization preservation

The pre-change backup tag is
`recovery/pre-functional-sort-20261117-05269ae`, pushed before editing. Moves use
normal Git history; no force push, reset, branch deletion or feature PR is needed.
All original payloads have a mapped destination; reference/history binaries and
source remain intact. Only imports, navigation and maintenance-tool locations are
adapted where their responsibilities moved. Existing user work was not overwritten
by another implementation.
