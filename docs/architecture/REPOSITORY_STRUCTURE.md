# Repository structure and ownership

> **Functional organization update:** See [PROJECT_STRUCTURE.md](../../PROJECT_STRUCTURE.md)
> for the current collections. Python policy/controls now live under `teaching`,
> adapters under `providers`, and SDK lifecycle under `runtime`. The installed
> CLI retains a compatibility entrypoint. Documents and recovery records are now
> grouped by purpose. This task ran no tests or builds; the earlier results below
> are historical evidence.
>
> The reference layout below describes the recorded consolidation. See
> [source recovery](../../AnalyseFuture/original-projects/reference-sources/README.md)
> for the current ZIPs and immutable extracted-tree revision.

Updated: **17 November 2026 (Asia/Calcutta)**.

## Scope and provenance

The complete consolidation started from local and remote `main` at
`98cfcd77b814848f5637b590b0e05843d69c8d84`, with a clean working tree and 1,535
tracked paths. All advertised branches/tags were fetched. The starting 46 reachable
commits and all tracked payloads were read or byte-inventoried. This is repository
recovery evidence; it does not establish account ownership, deleted history, or
who made an unauthorized change.

The earlier organization checkpoint moved 1,478 uploaded snapshot/ZIP payloads
into `AnalyseFuture/`; their bytes remain unchanged. This task recovered compatible
work from the disconnected retry branch, repaired a reproduced meaning-loss bug,
and grouped five web files by feature. No active framework, language, dependency
lockfile, public API, event version or database schema was replaced.

## Active architecture

```text
eng-teacher/
  README.md / docs/product/PROJECT_IDEA.txt       Project entry and owner product idea
  AGENTS.md                         Current working agreement
  docs/research/OPEN_SOURCE_REPOSITORIES.txt       Existing research inventory
  docs/legal/THIRD_PARTY_NOTICES.md             Licenses and preserved-source notices
  package.json / package-lock.json   Explicit apps/web workspace and lock
  .nvmrc / .gitignore                Runtime pin and local-output exclusions
  playwright.config.ts              Scoped browser checks
  pytest.ini                        Scoped default root Python collection
  .github/workflows/checks.yml       Active read-only CI
  apps/web/
    app/                            Next layout/styles/page and thin API route
      api/session/route.ts          Public admission entrypoint remains here
    features/
      lesson/
        components/tutor-app.tsx    Room, mic, audio, subtitles, cards and recap
        tutor-events.ts             Versioned parser, bounds, deadlines
        tests/tutor-events.test.ts  Contract/state helper tests
      session/
        server/session.ts           Pilot code, origin/budget, JWT and dispatch
        tests/session.test.ts       Local signing and security boundary tests
    package.json / tsconfig.json    Existing web tool configuration
    .env.example / LICENSE          Configuration example and attribution
  services/voice-agent/
    src/eng_teacher/
      agent.py                      SDK pipeline, privacy and room lifecycle
      controls.py                   Explicit help/repeat/example/skip intents
      tutor.py                      Interview and pending-retry policy
      providers.py                  Validated OpenAI speech/text adapters
    tests/                          Tutor, SDK scheduling and lifecycle checks
    pyproject.toml / uv.lock         Existing Python package and frozen lock
    .python-version / .env.example   Python 3.12 and credential names
  tests/browser/                    Cross-component desktop/mobile smoke
  scripts/
    repository_inventory.py         Static tracked-path ownership/import inventory
    security_history_scan.py        No-value history/worktree/ZIP pattern scan
  docs/                             Existing research, setup and actual status
  AnalyseFuture/
    *.txt                           Requested audit, feature and future reports
    PRESERVATION_MANIFEST.json      Earlier 1,478 original/new path hashes
    Cadence-main.zip                 Original uploaded archive
    talking-avatar-master.zip       Original uploaded archive
    reference-sources/              Complete immutable uploaded source snapshots
    historical-implementations/
      pre-consolidation-98cfcd7/     Ten superseded source/test/CI payloads
    recovery-notes/                 Baseline mapping and hashes
    repository-inventory/           Semantic review and security evidence
```

Generated dependencies/builds/caches (`node_modules`, `.next`, `.venv`, test
outputs) remain ignored local state. No unrelated replacement service, empty
shared package, new database, or additional active native client was created.

## Feature and data ownership

The Next page imports the lesson component. The API route delegates admission to
its session feature. Session policy generates microphone-only room tokens and a
fixed deadline. Browser audio travels through LiveKit to the existing Python
worker, whose controls/tutor/provider modules preserve original recognition and
corrections separately. Version 1 data packets drive feedback, status and recap.
Provider credentials stay in server/worker processes.

Examples, Hindi translations and help questions preserve a pending correction.
Semantic retry decisions cannot advance on unrelated or uncertain text. Internal
punctuation and numbers survive exact matching. Recoverable error events leave
the call open, while fatal failures terminate it. Those behaviors have local
regression coverage; they are not a live speech-quality benchmark.

## Preservation and execution boundaries

The active npm workspace is explicitly `apps/web`. TypeScript includes are local
to that app, Python packaging finds only the worker source, and Playwright uses
`tests/browser`. Root `pytest.ini` restricts ordinary collection to the 71 active
worker tests and excludes `AnalyseFuture`. Nested archived Actions workflows are
not root workflows. These boundaries prevent ordinary accidental discovery; they
are not a sandbox against explicitly running an archived command.

All ten superseded payloads are copied from immutable starting Git blobs, with
hashes in `AnalyseFuture/recovery/migration/CONSOLIDATION_BASELINE.json`. The earlier
1,478 preserved files and both uploaded ZIPs remain byte-identical. The snapshot
README's relative ZIP links still work because the ZIPs remain directly under
`AnalyseFuture`. Original branches and both remote backup tags are retained.

Do not execute archived installers as normal setup. The archived desktop runtime
downloader lacks an independent checksum check; archived ML/logging paths require
review before any selected port. The archive is evidence and future reference,
not a second production application or a finding that every file is unsafe.

## Current validation and continuation

Passed: 14 JavaScript tests, 71 Python tests, 6 browser checks, production build,
TypeScript, Ruff lint/format, frozen install refresh, root collection isolation,
HTTP startup/API checks and active npm advisory audit (zero known advisories).
Preservation and ZIP comparisons passed. See the detailed
[validation report](../../AnalyseFuture/recovery/validation/TEST_AND_VALIDATION_REPORT.txt).

Not established: successful provider/media call, physical Android, teaching or
Bengali quality, integrated avatar, pronunciation model quality, archived runtime,
remote Actions status, account incident attribution or branch-protection API
metadata. The metadata API returned Forbidden; normal Git pushes succeeded.

Read [REPOSITORY_AUDIT.txt](../../AnalyseFuture/recovery/migration/REPOSITORY_AUDIT.txt),
[FEATURE_INVENTORY.txt](../../AnalyseFuture/recovery/features/FEATURE_INVENTORY.txt),
[SECURITY_AUDIT.txt](../../AnalyseFuture/recovery/security/SECURITY_AUDIT.txt) and
[NEXT_DEVELOPER_INSTRUCTIONS.txt](../../AnalyseFuture/recovery/continuation/NEXT_DEVELOPER_INSTRUCTIONS.txt).
The owner directs work on `main`, without new branches or PRs, using normal pushed
checkpoints. Preserve earlier work and keep actual test evidence distinct from
future product goals.
