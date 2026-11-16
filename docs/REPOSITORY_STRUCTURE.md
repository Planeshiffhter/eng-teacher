# Repository audit and working structure

Audit date: **17 November 2026 (Asia/Calcutta)**.

## What the inspection establishes

At the start of this work, the local checkout, fetched `origin/main`, and GitHub's
advertised `main` all pointed to
`38e9d0034ba613052b3e7d37f902ed635eae8d9c`, the last commit verified in the preceding
session. The working tree was clean. There were **1,531 tracked files**, including
**1,476 files under `reference-sources`**, two uploaded ZIPs, and 53 other files.

The two archives and extracted snapshots were added during the owner's previous
explicit preservation request. Their presence alone is not evidence of an attack.
No newer tracked changes were found relative to that verified commit. This is a
repository-tree inspection, not an investigation of GitHub login history, account
permissions, deleted remote history, credentials, or attribution. It neither proves
nor disproves the owner's report of earlier unauthorized access.

The active package scripts, manifests, workflow, source layout and test discovery
were inspected before executing checks. The root npm workspace includes only
`apps/web`; Python runs from `services/voice-agent`; Playwright uses `tests/browser`.
The inspected active manifests have no preinstall/postinstall lifecycle hooks or
unexpected shell execution steps. No archived scripts were executed in this task.

## Final directory responsibilities

```text
eng-teacher/
  README.md                         Entry point and development links
  PROJECT_IDEA.txt                   Detailed product idea, feasibility and future phases
  AGENTS.md                         Current owner/agent working rules
  OPEN_SOURCE_REPOSITORIES.txt       Existing 21-repository research inventory
  THIRD_PARTY_NOTICES.md             Existing and preserved-source notices
  package.json / package-lock.json   Active npm workspace and pinned dependencies
  .nvmrc                            Node 24 requirement
  .gitignore                        Local/generated file exclusions
  playwright.config.ts              Active browser-test configuration
  .github/workflows/checks.yml       Active CI
  apps/
    web/
      app/                          Next.js pages, styles and API route
      components/                   Learner call and correction UI
      lib/                          Tutor events and server token signing
      tests/                        Web unit tests
      .env.example                  Credential names/placeholders, no real values
      package.json / tsconfig.json   Web build/type configuration
  services/
    voice-agent/
      src/eng_teacher/              Agent lifecycle, tutor policy, controls, providers
      tests/                        Offline tutor, scheduler and lifecycle tests
      pyproject.toml / uv.lock       Python project and locked dependencies
      .python-version               Python 3.12 pin
      .env.example                  Worker configuration example
  tests/
    browser/                        Desktop/mobile viewport browser smoke tests
  docs/                             Existing research, architecture, plans and evidence
    REPOSITORY_STRUCTURE.md         This audit and navigation map
    PROJECT_CONTINUITY_HANDOFF.md   Existing project history and continuation guide
    DEVELOPMENT.md                 Install/start commands
    VALIDATION.md                  Historical results and real-provider checklist
    ...                            All earlier specifications and research retained
  AnalyseFuture/
    README.md                       Preservation purpose and navigation
    PRESERVATION_MANIFEST.json      Old/new paths and SHA-256 of every moved file
    Cadence-main.zip                Original uploaded ZIP
    talking-avatar-master.zip      Original uploaded ZIP
    reference-sources/
      README.md                     Original snapshot navigation, retained unchanged
      ARCHIVES.json                 Original archive hashes and counts
      Cadence-main/                 Full uploaded upstream snapshot
      talking-avatar-master/        Full uploaded upstream snapshot
```

`node_modules`, `.next`, `.venv`, test results and caches are local generated state,
not project source. They remain ignored. No empty placeholder services, replacement
framework, database, mobile application or additional dependency workspace was
introduced during this reorganization.

## What was preserved and moved

| Previous location | Current location | Reason |
| --- | --- | --- |
| `reference-sources/` | `AnalyseFuture/reference-sources/` | Keep full research snapshots available without competing active applications at the root |
| `Cadence-main.zip` | `AnalyseFuture/Cadence-main.zip` | Preserve original upload alongside its extracted snapshot |
| `talking-avatar-master.zip` | `AnalyseFuture/talking-avatar-master.zip` | Preserve original upload alongside its extracted snapshot |

All **1,478 relocated files** were hashed before and after moving; their bytes are
unchanged. This includes all 1,474 extracted upstream files, both original snapshot
navigation/manifest files, and both ZIPs. The active application source, tests,
dependency declarations and lockfiles were retained in their existing locations.
Navigation and ownership documents are updated separately.

The ZIPs sit directly under `AnalyseFuture` so the unchanged original snapshot
README's relative links still resolve. Root notices now link to the new paths.
Original archives remain recoverable both as ZIP files and as ordinary Git files.
Moving material into this folder does not label it malicious, defective or approved
for production use.

Cadence contains a complete separate web product, Python speech/coaching services,
mobile and desktop clients, content, deployment files and tests. Talking Avatar
contains a browser SDK, model, GLB avatars and tests. Those are useful references,
not additional running Eng Teacher services. Their nested `.github` directories do
not become root GitHub workflows. Their licenses, notices and credits are retained.

## Verification and its limits

Preservation checks verify hashes for every relocated file and compare the two
extracted upstream trees with the original ZIP entries. The path mapping is stored
in `AnalyseFuture/PRESERVATION_MANIFEST.json`, with baseline commit and SHA-256.
The baseline tree can be recovered from Git without relying on a local workspace.

Active workflow checks for this reorganization are recorded in the final task
update below. The existing meaningful checks are JavaScript unit tests, Python
pytest, Ruff, Next.js production build, TypeScript and browser smoke tests. Browser
fixtures use synthetic microphone input and expected missing-config/failed-room
paths. They do not demonstrate a live voice conversation or Bengali translation.

No archived application was installed or validated as a complete running product.
No real microphone-to-provider lesson, language-quality evaluation, Android device
test, avatar integration or pronunciation benchmark was performed by moving files.
Those remain separate acceptance tasks in the existing development documents.

## Development boundaries and next work

Keep TypeScript for the web UI and Python for the existing voice worker. They form
one application through LiveKit audio and versioned event contracts. A language
rewrite does not improve folder organization and is outside this task.

The owner's new product idea gives Bengali-English learning explicit priority
alongside the existing Hindi-English research. This changes the intended roadmap,
not a claim that Bengali speech/translation is implemented or validated. Read
`../PROJECT_IDEA.txt` before choosing the next feature. Do not reimplement existing
correction controls from an outdated prompt or treat archived code as integrated.

Work directly on `main`, without a feature branch or new PR. Push normal fast-forward
checkpoints at least every five minutes while editing when changes are available;
do not force-push or reset shared history. Preserve unexpected files for analysis,
and investigate credentials privately rather than committing them into an archive.

If the owner suspects GitHub account compromise, repository organization alone
cannot restore account security. The account owner should review active sessions,
SSH keys, tokens, installed applications, collaborator access and recent account
security events, and revoke unfamiliar access through GitHub settings. No account
credentials or permissions were changed in this task.

## Current task validation

Pending execution after the relocation; results will be updated before the final
push. Preservation verification has already passed for all 1,478 moved files.
