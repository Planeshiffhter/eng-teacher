# Complete repository file and folder guide

Snapshot date: **17 November 2026 (Asia/Calcutta)**. This appendix lists **1,603 files** and **476 folders including the root**: the 1,600 previously tracked paths plus `PROJECT_HANDOFF.md`, this guide and `.github/pull_request_template.md` added in this documentation pass.

Start with [PROJECT_HANDOFF.md](../../PROJECT_HANDOFF.md) for detailed active feature ownership, goals, implemented behavior, remaining tasks and collaboration rules. [PROJECT_STRUCTURE.md](../../PROJECT_STRUCTURE.md) is the shorter collection map. Every file below has exactly one entry under its exact parent folder; every ancestor folder, including hidden directories, has a linked heading. The root folder is shown as `/`.

This is a static navigation index. Ownership and declaration analysis reuse the trusted maintenance inventory helpers without importing or executing inspected application or archived source. Purposes describe source/artifact responsibility, not successful runtime acceptance. Archive configuration, tests, models, content and assets remain preserved references; their presence does not make those features part of Eng Teacher. Evidence/snapshots retain their dated scope. Package markers are identified explicitly. No credentials, source excerpts, content hashes or self-referential source commit are included.

Refresh this appendix whenever tracked files, parent folders or responsibilities change; include intended new tracked paths and verify complete coverage before committing. The stated counts describe this snapshot, not all future repository states. Excluded ignored dependencies, caches, local environment files, untracked work and generated builds are not missing product modules. The separate [static inventory](../../AnalyseFuture/recovery/inventory/COMPLETE_FILE_INVENTORY.txt) carries deeper recorded ownership/import/preservation details.

Quick navigation: [root](#root) · [active web](#active-web) · [voice worker](#voice-worker) · [shared tests](#shared-tests) · [documentation](#documentation) · [maintenance](#maintenance) · [preserved material](#preserved-material).

<a id="root"></a>

## [/](../../)

Root navigation, owner instructions, runtime pins and shared build/test entrypoints for the active monorepo.

| File | Purpose | Status |
| --- | --- | --- |
| [.gitignore](../../.gitignore) | Excludes local credentials, dependencies, caches and generated build/test outputs from Git. | root configuration |
| [.nvmrc](../../.nvmrc) | Pins the active npm workspace to Node.js 24. | root configuration |
| [AGENTS.md](../../AGENTS.md) | Owner instructions, maintaining-agent workflow, safe pushed checkpoints and implementation boundaries. | maintainer documentation |
| [PROJECT_HANDOFF.md](../../PROJECT_HANDOFF.md) | Current goals, implemented features, active source responsibilities, ordered remaining work and collaboration/review process. | Current maintainer/contributor handoff |
| [PROJECT_STRUCTURE.md](../../PROJECT_STRUCTURE.md) | Repository collection and source ownership map; preserves the recorded organization context. | maintainer documentation |
| [README.md](../../README.md) | Repository homepage, product introduction and links to the current handoff and documentation. | maintainer documentation |
| [package-lock.json](../../package-lock.json) | Frozen npm dependency resolutions and integrity metadata for the active workspace. | root configuration |
| [package.json](../../package.json) | Root npm workspace scripts and shared browser-test tooling; the active workspace is apps/web. | root configuration |
| [playwright.config.ts](../../playwright.config.ts) | Desktop/mobile Chromium scenarios and production test-server startup with deliberately empty voice credentials. | root configuration |
| [pytest.ini](../../pytest.ini) | Default service/maintenance Python test discovery and exclusion of preserved reference projects. | root configuration |

## [.github/](../../.github/)

Active repository collaboration templates and GitHub automation configuration.

| File | Purpose | Status |
| --- | --- | --- |
| [pull_request_template.md](../../.github/pull_request_template.md) | Contributor checklist for scope, current implementation, test evidence, live limitations and reviewer handoff. | Active contribution guidance |

## [.github/workflows/](../../.github/workflows/)

Root workflows that execute the active project checks on GitHub.

| File | Purpose | Status |
| --- | --- | --- |
| [checks.yml](../../.github/workflows/checks.yml) | Active GitHub Actions installation, unit/maintenance tests, Ruff, build, typecheck and browser checks. | active root workflow |

<a id="preserved-material"></a>

## [AnalyseFuture/](../../AnalyseFuture/)

Preserved uploads, superseded implementations, audits and future ideas; not a second active application.

| File | Purpose | Status |
| --- | --- | --- |
| [README.md](../../AnalyseFuture/README.md) | Containing collection/component introduction, navigation and documented usage; retain the scope of the original project. | Historical/planning evidence; not active application |

## [AnalyseFuture/future-ideas/](../../AnalyseFuture/future-ideas/)

Deferred product concepts and roadmaps, separate from implemented capabilities.

| File | Purpose | Status |
| --- | --- | --- |
| [PROJECT_VISION_AND_FUTURE_ROADMAP.txt](../../AnalyseFuture/future-ideas/PROJECT_VISION_AND_FUTURE_ROADMAP.txt) | Documentation/research record for PROJECT VISION AND FUTURE ROADMAP; requirements and historical observations are not automatically implemented behavior. | Historical/planning evidence; not active application |

## [AnalyseFuture/historical-implementations/](../../AnalyseFuture/historical-implementations/)

Superseded source snapshots retained to explain recovery and compare historical behavior.

Contains the subfolders listed in their own sections; no tracked files directly in this folder.

## [AnalyseFuture/historical-implementations/pre-consolidation-98cfcd7/](../../AnalyseFuture/historical-implementations/pre-consolidation-98cfcd7/)

Superseded pre-consolidation implementation snapshot; retained for comparison, not the active setup/test target.

Contains the subfolders listed in their own sections; no tracked files directly in this folder.

## [AnalyseFuture/historical-implementations/pre-consolidation-98cfcd7/.github/](../../AnalyseFuture/historical-implementations/pre-consolidation-98cfcd7/.github/)

Superseded pre-consolidation .github snapshot; retained for comparison, not the active setup/test target.

Contains the subfolders listed in their own sections; no tracked files directly in this folder.

## [AnalyseFuture/historical-implementations/pre-consolidation-98cfcd7/.github/workflows/](../../AnalyseFuture/historical-implementations/pre-consolidation-98cfcd7/.github/workflows/)

Superseded pre-consolidation .github / workflows snapshot; retained for comparison, not the active setup/test target.

| File | Purpose | Status |
| --- | --- | --- |
| [checks.yml](../../AnalyseFuture/historical-implementations/pre-consolidation-98cfcd7/.github/workflows/checks.yml) | Declarative checks workflow/scenario/build configuration for the containing component. | Historical/planning evidence; not active application |

## [AnalyseFuture/historical-implementations/pre-consolidation-98cfcd7/apps/](../../AnalyseFuture/historical-implementations/pre-consolidation-98cfcd7/apps/)

Superseded pre-consolidation apps snapshot; retained for comparison, not the active setup/test target.

Contains the subfolders listed in their own sections; no tracked files directly in this folder.

## [AnalyseFuture/historical-implementations/pre-consolidation-98cfcd7/apps/web/](../../AnalyseFuture/historical-implementations/pre-consolidation-98cfcd7/apps/web/)

Superseded pre-consolidation apps / web snapshot; retained for comparison, not the active setup/test target.

Contains the subfolders listed in their own sections; no tracked files directly in this folder.

## [AnalyseFuture/historical-implementations/pre-consolidation-98cfcd7/apps/web/components/](../../AnalyseFuture/historical-implementations/pre-consolidation-98cfcd7/apps/web/components/)

Superseded pre-consolidation apps / web / components snapshot; retained for comparison, not the active setup/test target.

| File | Purpose | Status |
| --- | --- | --- |
| [tutor-app.tsx](../../AnalyseFuture/historical-implementations/pre-consolidation-98cfcd7/apps/web/components/tutor-app.tsx) | tutor app module; static declarations include RemoteParticipant, TutorFeedback, ConnectionDetails, MicIcon, ArrowIcon, SoundMark. No behavior is executed by this guide. | Historical/planning evidence; not active application |

## [AnalyseFuture/historical-implementations/pre-consolidation-98cfcd7/apps/web/lib/](../../AnalyseFuture/historical-implementations/pre-consolidation-98cfcd7/apps/web/lib/)

Superseded pre-consolidation apps / web / lib snapshot; retained for comparison, not the active setup/test target.

| File | Purpose | Status |
| --- | --- | --- |
| [tutor-events.ts](../../AnalyseFuture/historical-implementations/pre-consolidation-98cfcd7/apps/web/lib/tutor-events.ts) | tutor events module; static declarations include FeedbackAction, TutorFeedback, LessonEvent, TutorEvent, parseTutorEvent, lessonDeadline. No behavior is executed by this guide. | Historical/planning evidence; not active application |

## [AnalyseFuture/historical-implementations/pre-consolidation-98cfcd7/apps/web/tests/](../../AnalyseFuture/historical-implementations/pre-consolidation-98cfcd7/apps/web/tests/)

Superseded pre-consolidation apps / web / tests snapshot; retained for comparison, not the active setup/test target.

| File | Purpose | Status |
| --- | --- | --- |
| [tutor-events.test.ts](../../AnalyseFuture/historical-implementations/pre-consolidation-98cfcd7/apps/web/tests/tutor-events.test.ts) | Regression/scenario definitions for tutor events.test; execution and test boundaries are recorded separately. | Historical/planning evidence; not active application |

## [AnalyseFuture/historical-implementations/pre-consolidation-98cfcd7/services/](../../AnalyseFuture/historical-implementations/pre-consolidation-98cfcd7/services/)

Superseded pre-consolidation services snapshot; retained for comparison, not the active setup/test target.

Contains the subfolders listed in their own sections; no tracked files directly in this folder.

## [AnalyseFuture/historical-implementations/pre-consolidation-98cfcd7/services/voice-agent/](../../AnalyseFuture/historical-implementations/pre-consolidation-98cfcd7/services/voice-agent/)

Superseded pre-consolidation services / voice agent snapshot; retained for comparison, not the active setup/test target.

Contains the subfolders listed in their own sections; no tracked files directly in this folder.

## [AnalyseFuture/historical-implementations/pre-consolidation-98cfcd7/services/voice-agent/src/](../../AnalyseFuture/historical-implementations/pre-consolidation-98cfcd7/services/voice-agent/src/)

Superseded pre-consolidation services / voice agent / src snapshot; retained for comparison, not the active setup/test target.

Contains the subfolders listed in their own sections; no tracked files directly in this folder.

## [AnalyseFuture/historical-implementations/pre-consolidation-98cfcd7/services/voice-agent/src/eng_teacher/](../../AnalyseFuture/historical-implementations/pre-consolidation-98cfcd7/services/voice-agent/src/eng_teacher/)

Superseded pre-consolidation services / voice agent / src / eng teacher snapshot; retained for comparison, not the active setup/test target.

| File | Purpose | Status |
| --- | --- | --- |
| [agent.py](../../AnalyseFuture/historical-implementations/pre-consolidation-98cfcd7/services/voice-agent/src/eng_teacher/agent.py) | agent module; static declarations include lesson_deadline_ms, InterviewAgent, interview, configure_private_logging, main. No behavior is executed by this guide. | Historical/planning evidence; not active application |
| [controls.py](../../AnalyseFuture/historical-implementations/pre-consolidation-98cfcd7/services/voice-agent/src/eng_teacher/controls.py) | controls module; static declarations include explicit_control. No behavior is executed by this guide. | Historical/planning evidence; not active application |
| [providers.py](../../AnalyseFuture/historical-implementations/pre-consolidation-98cfcd7/services/voice-agent/src/eng_teacher/providers.py) | providers module; static declarations include Settings, OpenAITutorModel, create_model, create_stt, create_tts, create_llm. No behavior is executed by this guide. | Historical/planning evidence; not active application |
| [tutor.py](../../AnalyseFuture/historical-implementations/pre-consolidation-98cfcd7/services/voice-agent/src/eng_teacher/tutor.py) | tutor module; static declarations include ModelDecision, Feedback, TutorModel, risky_change, InterviewTutor. No behavior is executed by this guide. | Historical/planning evidence; not active application |

## [AnalyseFuture/historical-implementations/pre-consolidation-98cfcd7/services/voice-agent/tests/](../../AnalyseFuture/historical-implementations/pre-consolidation-98cfcd7/services/voice-agent/tests/)

Superseded pre-consolidation services / voice agent / tests snapshot; retained for comparison, not the active setup/test target.

| File | Purpose | Status |
| --- | --- | --- |
| [test_lifecycle.py](../../AnalyseFuture/historical-implementations/pre-consolidation-98cfcd7/services/voice-agent/tests/test_lifecycle.py) | Regression/scenario definitions for test lifecycle; execution and test boundaries are recorded separately. | Historical/planning evidence; not active application |
| [test_tutor.py](../../AnalyseFuture/historical-implementations/pre-consolidation-98cfcd7/services/voice-agent/tests/test_tutor.py) | Regression/scenario definitions for test tutor; execution and test boundaries are recorded separately. | Historical/planning evidence; not active application |

## [AnalyseFuture/original-projects/](../../AnalyseFuture/original-projects/)

Original uploaded ZIPs, import provenance and preserved extracted projects.

| File | Purpose | Status |
| --- | --- | --- |
| [Cadence-main.zip](../../AnalyseFuture/original-projects/Cadence-main.zip) | Original uploaded project ZIP retained for provenance and byte-preservation comparisons; do not run/extract as normal setup. | Historical/planning evidence; not active application |
| [talking-avatar-master.zip](../../AnalyseFuture/original-projects/talking-avatar-master.zip) | Original uploaded project ZIP retained for provenance and byte-preservation comparisons; do not run/extract as normal setup. | Historical/planning evidence; not active application |

## [AnalyseFuture/original-projects/reference-sources/](../../AnalyseFuture/original-projects/reference-sources/)

Complete reference snapshots retained for selective study; no normal setup or product-integration claim.

| File | Purpose | Status |
| --- | --- | --- |
| [ARCHIVES.json](../../AnalyseFuture/original-projects/reference-sources/ARCHIVES.json) | Structured ARCHIVES content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [README.md](../../AnalyseFuture/original-projects/reference-sources/README.md) | Containing collection/component introduction, navigation and documented usage; retain the scope of the original project. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/)

Preserved Cadence multi-client learning application snapshot; study/evidence only, not an integrated product dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [.dockerignore](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/.dockerignore) | Component .dockerignore configuration/policy; upstream cloud/security settings are reference material, not deployed Eng Teacher infrastructure. | Preserved upstream reference; not integrated |
| [.env.docker.example](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/.env.docker.example) | Component .env.docker configuration/policy; upstream cloud/security settings are reference material, not deployed Eng Teacher infrastructure. | Preserved upstream reference; not integrated |
| [.gitignore](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/.gitignore) | Original component exclusions for generated outputs, dependencies and local configuration. | Preserved upstream reference; not integrated |
| [.nvmrc](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/.nvmrc) | Interpreter version selection for the containing component; archived pins do not change the active root toolchain. | Preserved upstream reference; not integrated |
| [.vercelignore](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/.vercelignore) | Component .vercelignore configuration/policy; upstream cloud/security settings are reference material, not deployed Eng Teacher infrastructure. | Preserved upstream reference; not integrated |
| [AGENTS.md](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/AGENTS.md) | Original upstream agent/contributor instructions; historical reference rules do not override current root owner instructions. | Preserved upstream reference; not integrated |
| [CHANGELOG.md](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/CHANGELOG.md) | Documentation/research record for CHANGELOG; requirements and historical observations are not automatically implemented behavior. | Preserved upstream reference; not integrated |
| [CONTRIBUTING.md](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/CONTRIBUTING.md) | Documentation/research record for CONTRIBUTING; requirements and historical observations are not automatically implemented behavior. | Preserved upstream reference; not integrated |
| [CREDITS.md](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/CREDITS.md) | Licence/attribution record for the related component/assets; preserve notices and review the exact distribution rights. | Preserved upstream reference; not integrated |
| [Dockerfile](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/Dockerfile) | Original container build/runtime recipe for this component; not the active environment setup target. | Preserved upstream reference; not integrated |
| [LICENSE](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/LICENSE) | Licence/attribution record for the related component/assets; preserve notices and review the exact distribution rights. | Preserved upstream reference; not integrated |
| [NOTICE](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/NOTICE) | Licence/attribution record for the related component/assets; preserve notices and review the exact distribution rights. | Preserved upstream reference; not integrated |
| [README.md](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/README.md) | Containing collection/component introduction, navigation and documented usage; retain the scope of the original project. | Preserved upstream reference; not integrated |
| [SECURITY.md](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/SECURITY.md) | Documentation/research record for SECURITY; requirements and historical observations are not automatically implemented behavior. | Preserved upstream reference; not integrated |
| [docker-compose.yml](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/docker-compose.yml) | Declarative docker compose workflow/scenario/build configuration for the containing component. | Preserved upstream reference; not integrated |
| [eslint.config.mjs](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/eslint.config.mjs) | eslint.config build/runtime/tool configuration for the containing component. | Preserved upstream reference; not integrated |
| [firebase.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/firebase.json) | Component firebase configuration/policy; upstream cloud/security settings are reference material, not deployed Eng Teacher infrastructure. | Preserved upstream reference; not integrated |
| [firestore.indexes.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/firestore.indexes.json) | Component firestore.indexes configuration/policy; upstream cloud/security settings are reference material, not deployed Eng Teacher infrastructure. | Preserved upstream reference; not integrated |
| [firestore.rules](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/firestore.rules) | Component firestore configuration/policy; upstream cloud/security settings are reference material, not deployed Eng Teacher infrastructure. | Preserved upstream reference; not integrated |
| [lighthouserc.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/lighthouserc.json) | Structured lighthouserc content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [next.config.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/next.config.ts) | next.config build/runtime/tool configuration for the containing component. | Preserved upstream reference; not integrated |
| [package.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/package.json) | Containing component dependency/build/test declarations; consult its scope before installing. | Preserved upstream reference; not integrated |
| [playwright.config.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/playwright.config.ts) | playwright.config build/runtime/tool configuration for the containing component. | Preserved upstream reference; not integrated |
| [pnpm-lock.yaml](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/pnpm-lock.yaml) | Resolved component dependency versions/integrity; not an implemented product feature. | Preserved upstream reference; not integrated |
| [postcss.config.mjs](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/postcss.config.mjs) | postcss.config build/runtime/tool configuration for the containing component. | Preserved upstream reference; not integrated |
| [storage.rules](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/storage.rules) | Component storage configuration/policy; upstream cloud/security settings are reference material, not deployed Eng Teacher infrastructure. | Preserved upstream reference; not integrated |
| [tsconfig.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/tsconfig.json) | Structured tsconfig content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [vercel.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/vercel.json) | Structured vercel content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/.github/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/.github/)

Original upstream automation or contribution configuration. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [dependabot.yml](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/.github/dependabot.yml) | Declarative dependabot workflow/scenario/build configuration for the containing component. | Preserved upstream reference; not integrated |
| [pull_request_template.md](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/.github/pull_request_template.md) | Documentation/research record for pull request template; requirements and historical observations are not automatically implemented behavior. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/.github/ISSUE_TEMPLATE/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/.github/ISSUE_TEMPLATE/)

Original upstream automation or contribution configuration. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [bug_report.md](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/.github/ISSUE_TEMPLATE/bug_report.md) | Documentation/research record for bug report; requirements and historical observations are not automatically implemented behavior. | Preserved upstream reference; not integrated |
| [feature_request.md](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/.github/ISSUE_TEMPLATE/feature_request.md) | Documentation/research record for feature request; requirements and historical observations are not automatically implemented behavior. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/.github/workflows/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/.github/workflows/)

Original upstream automation or contribution configuration. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [ci.yml](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/.github/workflows/ci.yml) | Declarative ci workflow/scenario/build configuration for the containing component. | Preserved upstream reference; not integrated |
| [desktop-release.yml](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/.github/workflows/desktop-release.yml) | Declarative desktop release workflow/scenario/build configuration for the containing component. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/content/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/)

Upstream authored content content, pack data or fixtures; content rights/quality need separate review. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [modules.sql](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/modules.sql) | Upstream database schema/migration material for modules; no active Eng Teacher datastore is created by its presence. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/content/articulation/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/articulation/)

Upstream authored articulation content, pack data or fixtures; content rights/quality need separate review. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [consonants.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/articulation/consonants.json) | Structured consonants content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [diphthongs.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/articulation/diphthongs.json) | Structured diphthongs content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [references.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/articulation/references.json) | Structured references content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [vowels.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/articulation/vowels.json) | Structured vowels content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/content/fossilization/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/fossilization/)

Upstream authored fossilization content, pack data or fixtures; content rights/quality need separate review. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [articles-general.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/fossilization/articles-general.json) | Structured articles general content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [conditionals-will.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/fossilization/conditionals-will.json) | Structured conditionals will content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [contrastive-stress.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/fossilization/contrastive-stress.json) | Structured contrastive stress content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [cup-cat-cot.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/fossilization/cup-cat-cot.json) | Structured cup cat cot content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [despite-of.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/fossilization/despite-of.json) | Structured despite of content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [false-friends.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/fossilization/false-friends.json) | Structured false friends content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [final-devoicing.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/fossilization/final-devoicing.json) | Structured final devoicing content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [gerund-infinitive.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/fossilization/gerund-infinitive.json) | Structured gerund infinitive content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [linking.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/fossilization/linking.json) | Structured linking content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [make-do.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/fossilization/make-do.json) | Structured make do content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [noun-verb-stress.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/fossilization/noun-verb-stress.json) | Structured noun verb stress content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [prepositions-dependent.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/fossilization/prepositions-dependent.json) | Structured prepositions dependent content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [present-perfect-duration.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/fossilization/present-perfect-duration.json) | Structured present perfect duration content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [present-perfect-vs-past.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/fossilization/present-perfect-vs-past.json) | Structured present perfect vs past content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [question-intonation.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/fossilization/question-intonation.json) | Structured question intonation content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [question-word-order.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/fossilization/question-word-order.json) | Structured question word order content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [r-l.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/fossilization/r-l.json) | Structured r l content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [say-tell-explain.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/fossilization/say-tell-explain.json) | Structured say tell explain content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [schwa.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/fossilization/schwa.json) | Structured schwa content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [sentence-stress.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/fossilization/sentence-stress.json) | Structured sentence stress content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [ship-sheep.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/fossilization/ship-sheep.json) | Structured ship sheep content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [since-for-ago.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/fossilization/since-for-ago.json) | Structured since for ago content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [th-sounds.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/fossilization/th-sounds.json) | Structured th sounds content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [third-person-s.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/fossilization/third-person-s.json) | Structured third person s content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [uncountable-nouns.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/fossilization/uncountable-nouns.json) | Structured uncountable nouns content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [v-w.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/fossilization/v-w.json) | Structured v w content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [word-stress.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/fossilization/word-stress.json) | Structured word stress content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [would-for-wishes.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/fossilization/would-for-wishes.json) | Structured would for wishes content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/content/grammar/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/grammar/)

Upstream authored grammar content, pack data or fixtures; content rights/quality need separate review. Archived reference; not an active Eng Teacher feature or dependency.

Contains the subfolders listed in their own sections; no tracked files directly in this folder.

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/content/grammar/a1/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/grammar/a1/)

Upstream authored a1 content, pack data or fixtures; content rights/quality need separate review. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [articles-a-an-the.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/grammar/a1/articles-a-an-the.json) | Structured articles a an the content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [can-for-ability.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/grammar/a1/can-for-ability.json) | Structured can for ability content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [past-simple-be.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/grammar/a1/past-simple-be.json) | Structured past simple be content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [plural-nouns.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/grammar/a1/plural-nouns.json) | Structured plural nouns content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [possessive-adjectives.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/grammar/a1/possessive-adjectives.json) | Structured possessive adjectives content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [prepositions-of-place.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/grammar/a1/prepositions-of-place.json) | Structured prepositions of place content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [present-continuous.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/grammar/a1/present-continuous.json) | Structured present continuous content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [present-simple.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/grammar/a1/present-simple.json) | Structured present simple content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [question-words.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/grammar/a1/question-words.json) | Structured question words content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [subject-and-object-pronouns.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/grammar/a1/subject-and-object-pronouns.json) | Structured subject and object pronouns content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [there-is-there-are.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/grammar/a1/there-is-there-are.json) | Structured there is there are content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [verb-to-be.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/grammar/a1/verb-to-be.json) | Structured verb to be content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/content/grammar/a2/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/grammar/a2/)

Upstream authored a2 content, pack data or fixtures; content rights/quality need separate review. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [adverbs-of-frequency.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/grammar/a2/adverbs-of-frequency.json) | Structured adverbs of frequency content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [adverbs-of-manner.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/grammar/a2/adverbs-of-manner.json) | Structured adverbs of manner content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [and-but-or-because-so.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/grammar/a2/and-but-or-because-so.json) | Structured and but or because so content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [comparative-adjectives.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/grammar/a2/comparative-adjectives.json) | Structured comparative adjectives content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [countable-and-uncountable-nouns.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/grammar/a2/countable-and-uncountable-nouns.json) | Structured countable and uncountable nouns content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [going-to-future.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/grammar/a2/going-to-future.json) | Structured going to future content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [have-to-and-must.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/grammar/a2/have-to-and-must.json) | Structured have to and must content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [imperatives.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/grammar/a2/imperatives.json) | Structured imperatives content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [like-love-hate-ing.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/grammar/a2/like-love-hate-ing.json) | Structured like love hate ing content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [much-many-a-lot-of.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/grammar/a2/much-many-a-lot-of.json) | Structured much many a lot of content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [past-continuous.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/grammar/a2/past-continuous.json) | Structured past continuous content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [past-simple-irregular.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/grammar/a2/past-simple-irregular.json) | Structured past simple irregular content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [past-simple-regular.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/grammar/a2/past-simple-regular.json) | Structured past simple regular content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [possessive-s.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/grammar/a2/possessive-s.json) | Structured possessive s content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [prepositions-of-time.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/grammar/a2/prepositions-of-time.json) | Structured prepositions of time content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [present-continuous-for-arrangements.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/grammar/a2/present-continuous-for-arrangements.json) | Structured present continuous for arrangements content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [present-perfect-experience.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/grammar/a2/present-perfect-experience.json) | Structured present perfect experience content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [present-perfect-just-already-yet.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/grammar/a2/present-perfect-just-already-yet.json) | Structured present perfect just already yet content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [should-for-advice.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/grammar/a2/should-for-advice.json) | Structured should for advice content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [some-and-any.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/grammar/a2/some-and-any.json) | Structured some and any content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [superlative-adjectives.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/grammar/a2/superlative-adjectives.json) | Structured superlative adjectives content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [too-and-enough.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/grammar/a2/too-and-enough.json) | Structured too and enough content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [will-for-predictions-and-decisions.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/grammar/a2/will-for-predictions-and-decisions.json) | Structured will for predictions and decisions content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [would-like-and-want.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/grammar/a2/would-like-and-want.json) | Structured would like and want content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/content/grammar/b1/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/grammar/b1/)

Upstream authored b1 content, pack data or fixtures; content rights/quality need separate review. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [although-however-though.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/grammar/b1/although-however-though.json) | Structured although however though content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [as-as-comparisons.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/grammar/b1/as-as-comparisons.json) | Structured as as comparisons content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [both-either-neither.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/grammar/b1/both-either-neither.json) | Structured both either neither content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [defining-relative-clauses.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/grammar/b1/defining-relative-clauses.json) | Structured defining relative clauses content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [dont-have-to-vs-mustnt.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/grammar/b1/dont-have-to-vs-mustnt.json) | Structured dont have to vs mustnt content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [few-little-a-few-a-little.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/grammar/b1/few-little-a-few-a-little.json) | Structured few little a few a little content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [first-conditional.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/grammar/b1/first-conditional.json) | Structured first conditional content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [gerund-or-infinitive.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/grammar/b1/gerund-or-infinitive.json) | Structured gerund or infinitive content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [indirect-questions.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/grammar/b1/indirect-questions.json) | Structured indirect questions content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [might-may-could-for-possibility.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/grammar/b1/might-may-could-for-possibility.json) | Structured might may could for possibility content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [must-and-cant-for-deduction.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/grammar/b1/must-and-cant-for-deduction.json) | Structured must and cant for deduction content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [passive-present-and-past.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/grammar/b1/passive-present-and-past.json) | Structured passive present and past content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [past-perfect.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/grammar/b1/past-perfect.json) | Structured past perfect content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [phrasal-verbs-basics.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/grammar/b1/phrasal-verbs-basics.json) | Structured phrasal verbs basics content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [present-perfect-continuous.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/grammar/b1/present-perfect-continuous.json) | Structured present perfect continuous content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [present-perfect-for-and-since.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/grammar/b1/present-perfect-for-and-since.json) | Structured present perfect for and since content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [present-perfect-vs-past-simple.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/grammar/b1/present-perfect-vs-past-simple.json) | Structured present perfect vs past simple content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [question-tags.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/grammar/b1/question-tags.json) | Structured question tags content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [reflexive-pronouns.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/grammar/b1/reflexive-pronouns.json) | Structured reflexive pronouns content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [reported-questions.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/grammar/b1/reported-questions.json) | Structured reported questions content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [reported-statements.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/grammar/b1/reported-statements.json) | Structured reported statements content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [second-conditional.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/grammar/b1/second-conditional.json) | Structured second conditional content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [so-and-such.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/grammar/b1/so-and-such.json) | Structured so and such content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [subject-and-object-questions.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/grammar/b1/subject-and-object-questions.json) | Structured subject and object questions content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [time-clauses.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/grammar/b1/time-clauses.json) | Structured time clauses content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [used-to.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/grammar/b1/used-to.json) | Structured used to content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [verb-object-infinitive.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/grammar/b1/verb-object-infinitive.json) | Structured verb object infinitive content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [zero-conditional.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/grammar/b1/zero-conditional.json) | Structured zero conditional content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/content/grammar/b2/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/grammar/b2/)

Upstream authored b2 content, pack data or fixtures; content rights/quality need separate review. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [advanced-linkers-for-essays.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/grammar/b2/advanced-linkers-for-essays.json) | Structured advanced linkers for essays content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [articles-in-general-statements.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/grammar/b2/articles-in-general-statements.json) | Structured articles in general statements content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [be-used-to-and-get-used-to.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/grammar/b2/be-used-to-and-get-used-to.json) | Structured be used to and get used to content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [causative-have-and-get.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/grammar/b2/causative-have-and-get.json) | Structured causative have and get content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [describing-trends-and-data.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/grammar/b2/describing-trends-and-data.json) | Structured describing trends and data content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [despite-and-in-spite-of.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/grammar/b2/despite-and-in-spite-of.json) | Structured despite and in spite of content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [each-every-all.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/grammar/b2/each-every-all.json) | Structured each every all content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [emphatic-do.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/grammar/b2/emphatic-do.json) | Structured emphatic do content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [future-continuous.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/grammar/b2/future-continuous.json) | Structured future continuous content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [future-perfect.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/grammar/b2/future-perfect.json) | Structured future perfect content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [gradable-and-extreme-adjectives.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/grammar/b2/gradable-and-extreme-adjectives.json) | Structured gradable and extreme adjectives content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [had-better.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/grammar/b2/had-better.json) | Structured had better content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [it-cleft-sentences.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/grammar/b2/it-cleft-sentences.json) | Structured it cleft sentences content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [its-time-and-would-rather.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/grammar/b2/its-time-and-would-rather.json) | Structured its time and would rather content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [likelihood-expressions.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/grammar/b2/likelihood-expressions.json) | Structured likelihood expressions content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [linking-cause-and-effect.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/grammar/b2/linking-cause-and-effect.json) | Structured linking cause and effect content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [mixed-conditionals.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/grammar/b2/mixed-conditionals.json) | Structured mixed conditionals content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [modal-perfects-for-deduction.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/grammar/b2/modal-perfects-for-deduction.json) | Structured modal perfects for deduction content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [non-defining-relative-clauses.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/grammar/b2/non-defining-relative-clauses.json) | Structured non defining relative clauses content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [order-of-adjectives.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/grammar/b2/order-of-adjectives.json) | Structured order of adjectives content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [participle-clauses.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/grammar/b2/participle-clauses.json) | Structured participle clauses content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [passive-all-tenses.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/grammar/b2/passive-all-tenses.json) | Structured passive all tenses content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [purpose-clauses.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/grammar/b2/purpose-clauses.json) | Structured purpose clauses content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [remember-stop-try-forget.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/grammar/b2/remember-stop-try-forget.json) | Structured remember stop try forget content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [reporting-passive.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/grammar/b2/reporting-passive.json) | Structured reporting passive content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [reporting-verbs.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/grammar/b2/reporting-verbs.json) | Structured reporting verbs content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [should-have-and-could-have.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/grammar/b2/should-have-and-could-have.json) | Structured should have and could have content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [the-more-the-better.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/grammar/b2/the-more-the-better.json) | Structured the more the better content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [third-conditional.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/grammar/b2/third-conditional.json) | Structured third conditional content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [unless-and-as-long-as.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/grammar/b2/unless-and-as-long-as.json) | Structured unless and as long as content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [wish-and-if-only.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/grammar/b2/wish-and-if-only.json) | Structured wish and if only content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [would-for-past-habits.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/grammar/b2/would-for-past-habits.json) | Structured would for past habits content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/content/grammar/c1/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/grammar/c1/)

Upstream authored c1 content, pack data or fixtures; content rights/quality need separate review. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [academic-register-impersonal.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/grammar/c1/academic-register-impersonal.json) | Structured academic register impersonal content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [advanced-passive-forms.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/grammar/c1/advanced-passive-forms.json) | Structured advanced passive forms content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [advanced-relative-clauses.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/grammar/c1/advanced-relative-clauses.json) | Structured advanced relative clauses content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [articles-with-abstract-nouns.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/grammar/c1/articles-with-abstract-nouns.json) | Structured articles with abstract nouns content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [as-if-and-as-though.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/grammar/c1/as-if-and-as-though.json) | Structured as if and as though content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [causatives-advanced.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/grammar/c1/causatives-advanced.json) | Structured causatives advanced content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [cohesion-reference-and-summary-nouns.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/grammar/c1/cohesion-reference-and-summary-nouns.json) | Structured cohesion reference and summary nouns content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [collective-nouns-and-agreement.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/grammar/c1/collective-nouns-and-agreement.json) | Structured collective nouns and agreement content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [complex-prepositions.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/grammar/c1/complex-prepositions.json) | Structured complex prepositions content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [concession-clauses.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/grammar/c1/concession-clauses.json) | Structured concession clauses content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [discourse-markers.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/grammar/c1/discourse-markers.json) | Structured discourse markers content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [distancing-with-passive-infinitives.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/grammar/c1/distancing-with-passive-infinitives.json) | Structured distancing with passive infinitives content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [ellipsis-and-substitution.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/grammar/c1/ellipsis-and-substitution.json) | Structured ellipsis and substitution content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [fronting-for-emphasis.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/grammar/c1/fronting-for-emphasis.json) | Structured fronting for emphasis content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [future-in-the-past.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/grammar/c1/future-in-the-past.json) | Structured future in the past content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [hedging-language.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/grammar/c1/hedging-language.json) | Structured hedging language content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [inversion-after-negative-adverbials.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/grammar/c1/inversion-after-negative-adverbials.json) | Structured inversion after negative adverbials content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [inversion-after-only-and-not-until.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/grammar/c1/inversion-after-only-and-not-until.json) | Structured inversion after only and not until content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [inverted-conditionals.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/grammar/c1/inverted-conditionals.json) | Structured inverted conditionals content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [modal-perfects-advanced.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/grammar/c1/modal-perfects-advanced.json) | Structured modal perfects advanced content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [neednt-have-vs-didnt-need-to.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/grammar/c1/neednt-have-vs-didnt-need-to.json) | Structured neednt have vs didnt need to content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [nominalisation.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/grammar/c1/nominalisation.json) | Structured nominalisation content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [perfect-and-passive-participle-clauses.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/grammar/c1/perfect-and-passive-participle-clauses.json) | Structured perfect and passive participle clauses content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [reporting-and-citing-sources.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/grammar/c1/reporting-and-citing-sources.json) | Structured reporting and citing sources content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [subjunctive-after-suggest-insist.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/grammar/c1/subjunctive-after-suggest-insist.json) | Structured subjunctive after suggest insist content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [the-reason-why-the-way-that.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/grammar/c1/the-reason-why-the-way-that.json) | Structured the reason why the way that content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [verb-object-ing-patterns.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/grammar/c1/verb-object-ing-patterns.json) | Structured verb object ing patterns content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [were-to-and-should-conditionals.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/grammar/c1/were-to-and-should-conditionals.json) | Structured were to and should conditionals content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [what-cleft-sentences.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/grammar/c1/what-cleft-sentences.json) | Structured what cleft sentences content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [whatever-wherever-however.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/grammar/c1/whatever-wherever-however.json) | Structured whatever wherever however content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/content/grammar/c2/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/grammar/c2/)

Upstream authored c2 content, pack data or fixtures; content rights/quality need separate review. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [absolute-constructions.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/grammar/c2/absolute-constructions.json) | Structured absolute constructions content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [academic-nominal-style.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/grammar/c2/academic-nominal-style.json) | Structured academic nominal style content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [advanced-modality.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/grammar/c2/advanced-modality.json) | Structured advanced modality content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [cleft-variations.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/grammar/c2/cleft-variations.json) | Structured cleft variations content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [complex-noun-phrases.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/grammar/c2/complex-noun-phrases.json) | Structured complex noun phrases content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [conditions-without-if.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/grammar/c2/conditions-without-if.json) | Structured conditions without if content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [ellipsis-in-speech.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/grammar/c2/ellipsis-in-speech.json) | Structured ellipsis in speech content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [fixed-word-pairs.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/grammar/c2/fixed-word-pairs.json) | Structured fixed word pairs content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [formulaic-subjunctive.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/grammar/c2/formulaic-subjunctive.json) | Structured formulaic subjunctive content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [hedging-and-boosting.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/grammar/c2/hedging-and-boosting.json) | Structured hedging and boosting content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [intensifying-collocations.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/grammar/c2/intensifying-collocations.json) | Structured intensifying collocations content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [inversion-with-so-and-such.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/grammar/c2/inversion-with-so-and-such.json) | Structured inversion with so and such content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [lest-and-mandative-subjunctive.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/grammar/c2/lest-and-mandative-subjunctive.json) | Structured lest and mandative subjunctive content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [mixed-inverted-conditionals.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/grammar/c2/mixed-inverted-conditionals.json) | Structured mixed inverted conditionals content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [nominal-clauses.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/grammar/c2/nominal-clauses.json) | Structured nominal clauses content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [nuanced-reporting-verbs.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/grammar/c2/nuanced-reporting-verbs.json) | Structured nuanced reporting verbs content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [past-tenses-for-politeness.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/grammar/c2/past-tenses-for-politeness.json) | Structured past tenses for politeness content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [register-shifts.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/grammar/c2/register-shifts.json) | Structured register shifts content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [regrets-and-hypothetical-past.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/grammar/c2/regrets-and-hypothetical-past.json) | Structured regrets and hypothetical past content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [stance-adverbs.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/grammar/c2/stance-adverbs.json) | Structured stance adverbs content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [subtle-quantifiers.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/grammar/c2/subtle-quantifiers.json) | Structured subtle quantifiers content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [verbless-and-reduced-clauses.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/grammar/c2/verbless-and-reduced-clauses.json) | Structured verbless and reduced clauses content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/content/phrases/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/phrases/)

Upstream authored phrases content, pack data or fixtures; content rights/quality need separate review. Archived reference; not an active Eng Teacher feature or dependency.

Contains the subfolders listed in their own sections; no tracked files directly in this folder.

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/content/phrases/b2/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/phrases/b2/)

Upstream authored b2 content, pack data or fixtures; content rights/quality need separate review. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [academic.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/phrases/b2/academic.json) | Structured academic content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [calls.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/phrases/b2/calls.json) | Structured calls content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [disagreeing.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/phrases/b2/disagreeing.json) | Structured disagreeing content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [explaining.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/phrases/b2/explaining.json) | Structured explaining content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [feedback.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/phrases/b2/feedback.json) | Structured feedback content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [interviews.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/phrases/b2/interviews.json) | Structured interviews content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [meetings.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/phrases/b2/meetings.json) | Structured meetings content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [negotiation.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/phrases/b2/negotiation.json) | Structured negotiation content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [persuading.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/phrases/b2/persuading.json) | Structured persuading content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [presenting.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/phrases/b2/presenting.json) | Structured presenting content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [problem-solving.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/phrases/b2/problem-solving.json) | Structured problem solving content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [reacting.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/phrases/b2/reacting.json) | Structured reacting content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [small-talk.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/phrases/b2/small-talk.json) | Structured small talk content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [socialising.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/phrases/b2/socialising.json) | Structured socialising content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [storytelling.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/phrases/b2/storytelling.json) | Structured storytelling content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [travel.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/phrases/b2/travel.json) | Structured travel content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/content/phrases/c1/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/phrases/c1/)

Upstream authored c1 content, pack data or fixtures; content rights/quality need separate review. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [academic.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/phrases/c1/academic.json) | Structured academic content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [calls.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/phrases/c1/calls.json) | Structured calls content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [disagreeing.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/phrases/c1/disagreeing.json) | Structured disagreeing content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [explaining.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/phrases/c1/explaining.json) | Structured explaining content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [feedback.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/phrases/c1/feedback.json) | Structured feedback content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [interviews.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/phrases/c1/interviews.json) | Structured interviews content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [meetings.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/phrases/c1/meetings.json) | Structured meetings content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [negotiation.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/phrases/c1/negotiation.json) | Structured negotiation content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [persuading.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/phrases/c1/persuading.json) | Structured persuading content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [presenting.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/phrases/c1/presenting.json) | Structured presenting content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [problem-solving.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/phrases/c1/problem-solving.json) | Structured problem solving content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [reacting.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/phrases/c1/reacting.json) | Structured reacting content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [small-talk.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/phrases/c1/small-talk.json) | Structured small talk content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [socialising.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/phrases/c1/socialising.json) | Structured socialising content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [storytelling.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/phrases/c1/storytelling.json) | Structured storytelling content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [travel.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/phrases/c1/travel.json) | Structured travel content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/content/phrases/c2/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/phrases/c2/)

Upstream authored c2 content, pack data or fixtures; content rights/quality need separate review. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [academic.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/phrases/c2/academic.json) | Structured academic content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [calls.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/phrases/c2/calls.json) | Structured calls content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [disagreeing.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/phrases/c2/disagreeing.json) | Structured disagreeing content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [explaining.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/phrases/c2/explaining.json) | Structured explaining content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [feedback.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/phrases/c2/feedback.json) | Structured feedback content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [interviews.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/phrases/c2/interviews.json) | Structured interviews content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [meetings.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/phrases/c2/meetings.json) | Structured meetings content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [negotiation.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/phrases/c2/negotiation.json) | Structured negotiation content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [persuading.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/phrases/c2/persuading.json) | Structured persuading content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [presenting.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/phrases/c2/presenting.json) | Structured presenting content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [problem-solving.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/phrases/c2/problem-solving.json) | Structured problem solving content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [reacting.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/phrases/c2/reacting.json) | Structured reacting content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [small-talk.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/phrases/c2/small-talk.json) | Structured small talk content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [socialising.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/phrases/c2/socialising.json) | Structured socialising content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [storytelling.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/phrases/c2/storytelling.json) | Structured storytelling content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [travel.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/phrases/c2/travel.json) | Structured travel content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/content/placement/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/placement/)

Upstream authored placement content, pack data or fixtures; content rights/quality need separate review. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [a1.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/placement/a1.json) | Structured a1 content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [a2.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/placement/a2.json) | Structured a2 content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [b1.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/placement/b1.json) | Structured b1 content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [b2.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/placement/b2.json) | Structured b2 content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [c1.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/placement/c1.json) | Structured c1 content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [c2.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/placement/c2.json) | Structured c2 content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/content/scenarios/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/scenarios/)

Upstream authored scenarios content, pack data or fixtures; content rights/quality need separate review. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [scenarios.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/scenarios/scenarios.json) | Structured scenarios content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/content/sentences/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/sentences/)

Upstream authored sentences content, pack data or fixtures; content rights/quality need separate review. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [a1.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/sentences/a1.json) | Structured a1 content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [a2.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/sentences/a2.json) | Structured a2 content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [b1.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/sentences/b1.json) | Structured b1 content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [b2.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/sentences/b2.json) | Structured b2 content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [c1.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/sentences/c1.json) | Structured c1 content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [c2.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/sentences/c2.json) | Structured c2 content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/content/slang/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/slang/)

Upstream authored slang content, pack data or fixtures; content rights/quality need separate review. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [agreement.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/slang/agreement.json) | Structured agreement content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [feelings.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/slang/feelings.json) | Structured feelings content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [going-out.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/slang/going-out.json) | Structured going out content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [money.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/slang/money.json) | Structured money content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [online.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/slang/online.json) | Structured online content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [people.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/slang/people.json) | Structured people content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [quality.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/slang/quality.json) | Structured quality content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [reactions.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/slang/reactions.json) | Structured reactions content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [relationships.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/slang/relationships.json) | Structured relationships content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [uk.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/slang/uk.json) | Structured uk content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [us.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/slang/us.json) | Structured us content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [work.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/slang/work.json) | Structured work content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/content/sounds/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/sounds/)

Upstream authored sounds content, pack data or fixtures; content rights/quality need separate review. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [minimal-pairs.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/sounds/minimal-pairs.json) | Structured minimal pairs content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/content/vocab/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/vocab/)

Upstream authored vocab content, pack data or fixtures; content rights/quality need separate review. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [a1.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/vocab/a1.json) | Structured a1 content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [a2.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/vocab/a2.json) | Structured a2 content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [b1.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/vocab/b1.json) | Structured b1 content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [b2.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/vocab/b2.json) | Structured b2 content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [c1.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/vocab/c1.json) | Structured c1 content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [c2.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/content/vocab/c2.json) | Structured c2 content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/deploy/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/deploy/)

Original upstream deploy source/configuration collection. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [cadence-web.env.example](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/deploy/cadence-web.env.example) | Configuration-name/example template for its component; not a configured live service or a place for real secrets. | Preserved upstream reference; not integrated |
| [cloudbuild.ai.yaml](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/deploy/cloudbuild.ai.yaml) | Declarative cloudbuild.ai workflow/scenario/build configuration for the containing component. | Preserved upstream reference; not integrated |
| [cloudbuild.web.yaml](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/deploy/cloudbuild.web.yaml) | Declarative cloudbuild.web workflow/scenario/build configuration for the containing component. | Preserved upstream reference; not integrated |
| [cloudrun.sh](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/deploy/cloudrun.sh) | cloudrun shell utility; inspect supported targets and verification before any explicit execution. | Preserved upstream reference; not integrated |
| [tts-cache-lifecycle.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/deploy/tts-cache-lifecycle.json) | Structured tts cache lifecycle content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [web-build.env.example](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/deploy/web-build.env.example) | Configuration-name/example template for its component; not a configured live service or a place for real secrets. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/desktop/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/desktop/)

Original desktop desktop runtime or packaging support. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [.gitignore](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/desktop/.gitignore) | Original component exclusions for generated outputs, dependencies and local configuration. | Preserved upstream reference; not integrated |
| [INSTALLER_ARCHITECTURE.md](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/desktop/INSTALLER_ARCHITECTURE.md) | Documentation/research record for INSTALLER ARCHITECTURE; requirements and historical observations are not automatically implemented behavior. | Preserved upstream reference; not integrated |
| [README.md](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/desktop/README.md) | Containing collection/component introduction, navigation and documented usage; retain the scope of the original project. | Preserved upstream reference; not integrated |
| [electron-builder.yml](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/desktop/electron-builder.yml) | Declarative electron builder workflow/scenario/build configuration for the containing component. | Preserved upstream reference; not integrated |
| [package.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/desktop/package.json) | Containing component dependency/build/test declarations; consult its scope before installing. | Preserved upstream reference; not integrated |
| [pnpm-lock.yaml](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/desktop/pnpm-lock.yaml) | Resolved component dependency versions/integrity; not an implemented product feature. | Preserved upstream reference; not integrated |
| [tsconfig.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/desktop/tsconfig.json) | Structured tsconfig content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/desktop/assets/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/desktop/assets/)

Original assets assets, models or packaging resources; retain associated notices. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [entitlements.mac.plist](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/desktop/assets/entitlements.mac.plist) | Native Apple/mobile entitlements.mac implementation, packaging or privacy declaration; not an active web/worker dependency. | Preserved upstream reference; not integrated |
| [icon.icns](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/desktop/assets/icon.icns) | icon visual/font/icon resource; preserve applicable asset attribution and review rights before reuse. | Preserved upstream reference; not integrated |
| [icon.png](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/desktop/assets/icon.png) | icon visual/font/icon resource; preserve applicable asset attribution and review rights before reuse. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/desktop/scripts/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/desktop/scripts/)

Original desktop scripts runtime or packaging support. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [clean-test.mjs](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/desktop/scripts/clean-test.mjs) | clean test implementation/helper module in the containing upstream reference component. | Preserved upstream reference; not integrated |
| [dev.mjs](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/desktop/scripts/dev.mjs) | dev implementation/helper module in the containing upstream reference component. | Preserved upstream reference; not integrated |
| [fix-standalone.mjs](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/desktop/scripts/fix-standalone.mjs) | fix standalone module; static declarations include isBrokenSymlink, findSemverTarget, main. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [prepare-build.mjs](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/desktop/scripts/prepare-build.mjs) | prepare build implementation/helper module in the containing upstream reference component. | Preserved upstream reference; not integrated |
| [prepare-python-runtime.mjs](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/desktop/scripts/prepare-python-runtime.mjs) | prepare python runtime module; static declarations include log, getAssetUrl, getTargetDir, getInterpreterPath, readManifest, run. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [prepare-release.mjs](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/desktop/scripts/prepare-release.mjs) | prepare release implementation/helper module in the containing upstream reference component. | Preserved upstream reference; not integrated |
| [reset-runtime.mjs](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/desktop/scripts/reset-runtime.mjs) | reset runtime module; static declarations include getUserDataDir, runCommand, pathExists, detectComposeCommand, stopComposeRuntime, removeCadenceImages. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [run-electron-builder.mjs](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/desktop/scripts/run-electron-builder.mjs) | run electron builder implementation/helper module in the containing upstream reference component. | Preserved upstream reference; not integrated |
| [smoke.mjs](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/desktop/scripts/smoke.mjs) | smoke module; static declarations include installFromDmg, packagedBinary, record, engineReady. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [test-update-feed.mjs](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/desktop/scripts/test-update-feed.mjs) | test update feed implementation/helper module in the containing upstream reference component. | Preserved upstream reference; not integrated |
| [test-update-install.mjs](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/desktop/scripts/test-update-install.mjs) | test update install module; static declarations include record, sign, setVersion. No behavior is executed by this guide. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/desktop/src/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/desktop/src/)

Original desktop src runtime or packaging support. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [main.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/desktop/src/main.ts) | main module; static declarations include UtilityProcess, DesktopUpdater, debugLog, getDesktopHomePath, bootWindow, pairingPreferences. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [preload.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/desktop/src/preload.ts) | preload module; static declarations include markElectronDocument, UpdateNotice, renderUpdateNotice. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [setup-manager.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/desktop/src/setup-manager.ts) | setup manager module; static declarations include DesktopSetupManager. No behavior is executed by this guide. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/desktop/src/main/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/desktop/src/main/)

Original desktop main runtime or packaging support. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [browser-window.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/desktop/src/main/browser-window.ts) | browser window module; static declarations include WindowSize, FixedWindowSize, CreateCadenceWindowOptions, createCadenceWindow, on, html. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [constants.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/desktop/src/main/constants.ts) | constants implementation/helper module in the containing upstream reference component. | Preserved upstream reference; not integrated |
| [menu.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/desktop/src/main/menu.ts) | menu module; static declarations include MenuActions, updateItems, buildMenu. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [next-server.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/desktop/src/main/next-server.ts) | next server module; static declarations include UtilityProcess, waitForServer, startNextServer. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [pairing.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/desktop/src/main/pairing.ts) | pairing module; static declarations include PairingPreferences, PairingPaths, resolvePairingPaths, readPairingPreferences, writePairingPreferences, findLanAddress. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [setup-ipc.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/desktop/src/main/setup-ipc.ts) | setup ipc module; static declarations include registerSetupIpc. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [update-policy.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/desktop/src/main/update-policy.ts) | update policy module; static declarations include InstallKind, detectInstallKind, canSelfUpdate, releasePageUrl, safeFeedOverride, UpdateState. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [updater.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/desktop/src/main/updater.ts) | updater module; static declarations include InstallKind, UpdateEvent, UpdateState, UpdatePreferences, UpdateMenuItem, DesktopUpdater. No behavior is executed by this guide. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/desktop/src/setup/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/desktop/src/setup/)

Original desktop setup runtime or packaging support. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [constants.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/desktop/src/setup/constants.ts) | constants implementation/helper module in the containing upstream reference component. | Preserved upstream reference; not integrated |
| [support.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/desktop/src/setup/support.ts) | support module; static declarations include ChildProcess, ServiceName, RuntimeManifestFile, ServiceProcessSnapshot, PythonCommandDetails, DesktopSetupSupport. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [types.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/desktop/src/setup/types.ts) | types module; static declarations include DesktopSetupPhase, DesktopSetupState, DesktopRuntimeDetails, DesktopRuntimeLocation, SetupManifest, AiEngineHealthPayload. No behavior is executed by this guide. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/docs/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/docs/)

Upstream documentation for docs. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [CONNECT_YOUR_PHONE.md](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/docs/CONNECT_YOUR_PHONE.md) | Documentation/research record for CONNECT YOUR PHONE; requirements and historical observations are not automatically implemented behavior. | Preserved upstream reference; not integrated |
| [DEPLOY.md](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/docs/DEPLOY.md) | Documentation/research record for DEPLOY; requirements and historical observations are not automatically implemented behavior. | Preserved upstream reference; not integrated |
| [GITHUB_UPDATE.md](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/docs/GITHUB_UPDATE.md) | Documentation/research record for GITHUB UPDATE; requirements and historical observations are not automatically implemented behavior. | Preserved upstream reference; not integrated |
| [PAIRING_PROTOCOL.md](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/docs/PAIRING_PROTOCOL.md) | Documentation/research record for PAIRING PROTOCOL; requirements and historical observations are not automatically implemented behavior. | Preserved upstream reference; not integrated |
| [PLATFORM.md](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/docs/PLATFORM.md) | Documentation/research record for PLATFORM; requirements and historical observations are not automatically implemented behavior. | Preserved upstream reference; not integrated |
| [RELEASING.md](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/docs/RELEASING.md) | Documentation/research record for RELEASING; requirements and historical observations are not automatically implemented behavior. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/)

Original native-mobile mobile modules, screens or supporting resources. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [.env.example](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/.env.example) | Configuration-name/example template for its component; not a configured live service or a place for real secrets. | Preserved upstream reference; not integrated |
| [.env.release.example](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/.env.release.example) | Component .env.release configuration/policy; upstream cloud/security settings are reference material, not deployed Eng Teacher infrastructure. | Preserved upstream reference; not integrated |
| [.gitignore](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/.gitignore) | Original component exclusions for generated outputs, dependencies and local configuration. | Preserved upstream reference; not integrated |
| [AGENTS.md](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/AGENTS.md) | Original upstream agent/contributor instructions; historical reference rules do not override current root owner instructions. | Preserved upstream reference; not integrated |
| [ExportOptions.plist](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/ExportOptions.plist) | Native Apple/mobile Export Options implementation, packaging or privacy declaration; not an active web/worker dependency. | Preserved upstream reference; not integrated |
| [LICENSE](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/LICENSE) | Licence/attribution record for the related component/assets; preserve notices and review the exact distribution rights. | Preserved upstream reference; not integrated |
| [README.md](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/README.md) | Containing collection/component introduction, navigation and documented usage; retain the scope of the original project. | Preserved upstream reference; not integrated |
| [app.config.js](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/app.config.js) | app.config build/runtime/tool configuration for the containing component. | Preserved upstream reference; not integrated |
| [app.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/app.json) | Structured app content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [babel.config.js](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/babel.config.js) | babel.config build/runtime/tool configuration for the containing component. | Preserved upstream reference; not integrated |
| [eslint.config.js](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/eslint.config.js) | eslint.config build/runtime/tool configuration for the containing component. | Preserved upstream reference; not integrated |
| [metro.config.js](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/metro.config.js) | metro.config build/runtime/tool configuration for the containing component. | Preserved upstream reference; not integrated |
| [package-lock.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/package-lock.json) | Resolved component dependency versions/integrity; not an implemented product feature. | Preserved upstream reference; not integrated |
| [package.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/package.json) | Containing component dependency/build/test declarations; consult its scope before installing. | Preserved upstream reference; not integrated |
| [tsconfig.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/tsconfig.json) | Structured tsconfig content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/assets/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/assets/)

Original assets assets, models or packaging resources; retain associated notices. Archived reference; not an active Eng Teacher feature or dependency.

Contains the subfolders listed in their own sections; no tracked files directly in this folder.

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/assets/images/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/assets/images/)

Original images assets, models or packaging resources; retain associated notices. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [favicon.png](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/assets/images/favicon.png) | favicon visual/font/icon resource; preserve applicable asset attribution and review rights before reuse. | Preserved upstream reference; not integrated |
| [icon.png](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/assets/images/icon.png) | icon visual/font/icon resource; preserve applicable asset attribution and review rights before reuse. | Preserved upstream reference; not integrated |
| [ios-icon.png](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/assets/images/ios-icon.png) | ios icon visual/font/icon resource; preserve applicable asset attribution and review rights before reuse. | Preserved upstream reference; not integrated |
| [splash-mark-dark.png](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/assets/images/splash-mark-dark.png) | splash mark dark visual/font/icon resource; preserve applicable asset attribution and review rights before reuse. | Preserved upstream reference; not integrated |
| [splash-mark.png](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/assets/images/splash-mark.png) | splash mark visual/font/icon resource; preserve applicable asset attribution and review rights before reuse. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/assets/packs/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/assets/packs/)

Upstream authored packs content, pack data or fixtures; content rights/quality need separate review. Archived reference; not an active Eng Teacher feature or dependency.

Contains the subfolders listed in their own sections; no tracked files directly in this folder.

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/assets/packs/core-a1/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/assets/packs/core-a1/)

Upstream authored core a1 content, pack data or fixtures; content rights/quality need separate review. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [content.cpack](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/assets/packs/core-a1/content.cpack) | Packaged upstream content learning content; not active Eng Teacher curriculum. | Preserved upstream reference; not integrated |
| [manifest.cpack](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/assets/packs/core-a1/manifest.cpack) | Packaged upstream manifest learning content; not active Eng Teacher curriculum. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/assets/packs/core-a2/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/assets/packs/core-a2/)

Upstream authored core a2 content, pack data or fixtures; content rights/quality need separate review. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [content.cpack](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/assets/packs/core-a2/content.cpack) | Packaged upstream content learning content; not active Eng Teacher curriculum. | Preserved upstream reference; not integrated |
| [manifest.cpack](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/assets/packs/core-a2/manifest.cpack) | Packaged upstream manifest learning content; not active Eng Teacher curriculum. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/assets/packs/core-b1/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/assets/packs/core-b1/)

Upstream authored core b1 content, pack data or fixtures; content rights/quality need separate review. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [content.cpack](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/assets/packs/core-b1/content.cpack) | Packaged upstream content learning content; not active Eng Teacher curriculum. | Preserved upstream reference; not integrated |
| [manifest.cpack](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/assets/packs/core-b1/manifest.cpack) | Packaged upstream manifest learning content; not active Eng Teacher curriculum. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/assets/packs/core-b2/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/assets/packs/core-b2/)

Upstream authored core b2 content, pack data or fixtures; content rights/quality need separate review. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [content.cpack](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/assets/packs/core-b2/content.cpack) | Packaged upstream content learning content; not active Eng Teacher curriculum. | Preserved upstream reference; not integrated |
| [manifest.cpack](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/assets/packs/core-b2/manifest.cpack) | Packaged upstream manifest learning content; not active Eng Teacher curriculum. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/assets/packs/fossilization/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/assets/packs/fossilization/)

Upstream authored fossilization content, pack data or fixtures; content rights/quality need separate review. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [content.cpack](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/assets/packs/fossilization/content.cpack) | Packaged upstream content learning content; not active Eng Teacher curriculum. | Preserved upstream reference; not integrated |
| [manifest.cpack](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/assets/packs/fossilization/manifest.cpack) | Packaged upstream manifest learning content; not active Eng Teacher curriculum. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/assets/packs/phrases-b2/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/assets/packs/phrases-b2/)

Upstream authored phrases b2 content, pack data or fixtures; content rights/quality need separate review. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [content.cpack](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/assets/packs/phrases-b2/content.cpack) | Packaged upstream content learning content; not active Eng Teacher curriculum. | Preserved upstream reference; not integrated |
| [manifest.cpack](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/assets/packs/phrases-b2/manifest.cpack) | Packaged upstream manifest learning content; not active Eng Teacher curriculum. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/assets/packs/phrases-c1/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/assets/packs/phrases-c1/)

Upstream authored phrases c1 content, pack data or fixtures; content rights/quality need separate review. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [content.cpack](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/assets/packs/phrases-c1/content.cpack) | Packaged upstream content learning content; not active Eng Teacher curriculum. | Preserved upstream reference; not integrated |
| [manifest.cpack](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/assets/packs/phrases-c1/manifest.cpack) | Packaged upstream manifest learning content; not active Eng Teacher curriculum. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/assets/packs/phrases-c2/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/assets/packs/phrases-c2/)

Upstream authored phrases c2 content, pack data or fixtures; content rights/quality need separate review. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [content.cpack](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/assets/packs/phrases-c2/content.cpack) | Packaged upstream content learning content; not active Eng Teacher curriculum. | Preserved upstream reference; not integrated |
| [manifest.cpack](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/assets/packs/phrases-c2/manifest.cpack) | Packaged upstream manifest learning content; not active Eng Teacher curriculum. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/assets/packs/placement/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/assets/packs/placement/)

Upstream authored placement content, pack data or fixtures; content rights/quality need separate review. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [content.cpack](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/assets/packs/placement/content.cpack) | Packaged upstream content learning content; not active Eng Teacher curriculum. | Preserved upstream reference; not integrated |
| [manifest.cpack](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/assets/packs/placement/manifest.cpack) | Packaged upstream manifest learning content; not active Eng Teacher curriculum. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/assets/packs/slang/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/assets/packs/slang/)

Upstream authored slang content, pack data or fixtures; content rights/quality need separate review. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [content.cpack](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/assets/packs/slang/content.cpack) | Packaged upstream content learning content; not active Eng Teacher curriculum. | Preserved upstream reference; not integrated |
| [manifest.cpack](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/assets/packs/slang/manifest.cpack) | Packaged upstream manifest learning content; not active Eng Teacher curriculum. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/assets/packs/sounds/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/assets/packs/sounds/)

Upstream authored sounds content, pack data or fixtures; content rights/quality need separate review. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [content.cpack](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/assets/packs/sounds/content.cpack) | Packaged upstream content learning content; not active Eng Teacher curriculum. | Preserved upstream reference; not integrated |
| [manifest.cpack](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/assets/packs/sounds/manifest.cpack) | Packaged upstream manifest learning content; not active Eng Teacher curriculum. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/assets/sounds/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/assets/sounds/)

Original sounds assets, models or packaging resources; retain associated notices. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [complete.wav](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/assets/sounds/complete.wav) | complete audio/media resource for the original component; rights and appropriate consent require separate review before reuse. | Preserved upstream reference; not integrated |
| [correct.wav](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/assets/sounds/correct.wav) | correct audio/media resource for the original component; rights and appropriate consent require separate review before reuse. | Preserved upstream reference; not integrated |
| [incorrect.wav](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/assets/sounds/incorrect.wav) | incorrect audio/media resource for the original component; rights and appropriate consent require separate review before reuse. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/assets/svg/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/assets/svg/)

Original svg assets, models or packaging resources; retain associated notices. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [communication-1.svg](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/assets/svg/communication-1.svg) | communication 1 visual/font/icon resource; preserve applicable asset attribution and review rights before reuse. | Preserved upstream reference; not integrated |
| [following-your-dreams-1.svg](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/assets/svg/following-your-dreams-1.svg) | following your dreams 1 visual/font/icon resource; preserve applicable asset attribution and review rights before reuse. | Preserved upstream reference; not integrated |
| [icon-dark.svg](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/assets/svg/icon-dark.svg) | icon dark visual/font/icon resource; preserve applicable asset attribution and review rights before reuse. | Preserved upstream reference; not integrated |
| [icon-green-dark.svg](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/assets/svg/icon-green-dark.svg) | icon green dark visual/font/icon resource; preserve applicable asset attribution and review rights before reuse. | Preserved upstream reference; not integrated |
| [icon-green-white.svg](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/assets/svg/icon-green-white.svg) | icon green white visual/font/icon resource; preserve applicable asset attribution and review rights before reuse. | Preserved upstream reference; not integrated |
| [logo-dark.svg](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/assets/svg/logo-dark.svg) | logo dark visual/font/icon resource; preserve applicable asset attribution and review rights before reuse. | Preserved upstream reference; not integrated |
| [logo-green-dark.svg](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/assets/svg/logo-green-dark.svg) | logo green dark visual/font/icon resource; preserve applicable asset attribution and review rights before reuse. | Preserved upstream reference; not integrated |
| [logo-green-white.svg](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/assets/svg/logo-green-white.svg) | logo green white visual/font/icon resource; preserve applicable asset attribution and review rights before reuse. | Preserved upstream reference; not integrated |
| [progress-1.svg](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/assets/svg/progress-1.svg) | progress 1 visual/font/icon resource; preserve applicable asset attribution and review rights before reuse. | Preserved upstream reference; not integrated |
| [success-1.svg](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/assets/svg/success-1.svg) | success 1 visual/font/icon resource; preserve applicable asset attribution and review rights before reuse. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/e2e/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/e2e/)

Upstream verification scenarios/fixtures for e2e. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [01-own-server-onboarding.yaml](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/e2e/01-own-server-onboarding.yaml) | Regression/scenario definitions for 01 own server onboarding; execution and test boundaries are recorded separately. | Preserved upstream reference; not integrated |
| [02-practice.yaml](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/e2e/02-practice.yaml) | Regression/scenario definitions for 02 practice; execution and test boundaries are recorded separately. | Preserved upstream reference; not integrated |
| [03-mouth-map.yaml](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/e2e/03-mouth-map.yaml) | Regression/scenario definitions for 03 mouth map; execution and test boundaries are recorded separately. | Preserved upstream reference; not integrated |
| [04-pair-link.yaml](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/e2e/04-pair-link.yaml) | Regression/scenario definitions for 04 pair link; execution and test boundaries are recorded separately. | Preserved upstream reference; not integrated |
| [05-offline.yaml](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/e2e/05-offline.yaml) | Regression/scenario definitions for 05 offline; execution and test boundaries are recorded separately. | Preserved upstream reference; not integrated |
| [06-cloud-onboarding.yaml](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/e2e/06-cloud-onboarding.yaml) | Regression/scenario definitions for 06 cloud onboarding; execution and test boundaries are recorded separately. | Preserved upstream reference; not integrated |
| [07-paywall.yaml](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/e2e/07-paywall.yaml) | Regression/scenario definitions for 07 paywall; execution and test boundaries are recorded separately. | Preserved upstream reference; not integrated |
| [08-account.yaml](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/e2e/08-account.yaml) | Regression/scenario definitions for 08 account; execution and test boundaries are recorded separately. | Preserved upstream reference; not integrated |
| [09-auth-screens.yaml](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/e2e/09-auth-screens.yaml) | Regression/scenario definitions for 09 auth screens; execution and test boundaries are recorded separately. | Preserved upstream reference; not integrated |
| [10-apple-google.yaml](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/e2e/10-apple-google.yaml) | Regression/scenario definitions for 10 apple google; execution and test boundaries are recorded separately. | Preserved upstream reference; not integrated |
| [11-advanced.yaml](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/e2e/11-advanced.yaml) | Regression/scenario definitions for 11 advanced; execution and test boundaries are recorded separately. | Preserved upstream reference; not integrated |
| [config.yaml](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/e2e/config.yaml) | Regression/scenario definitions for config; execution and test boundaries are recorded separately. | Preserved upstream reference; not integrated |
| [run.sh](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/e2e/run.sh) | Regression/scenario definitions for run; execution and test boundaries are recorded separately. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/e2e/screenshots/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/e2e/screenshots/)

Upstream verification scenarios/fixtures for screenshots. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [coach.yaml](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/e2e/screenshots/coach.yaml) | Regression/scenario definitions for coach; execution and test boundaries are recorded separately. | Preserved upstream reference; not integrated |
| [flashcards.yaml](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/e2e/screenshots/flashcards.yaml) | Regression/scenario definitions for flashcards; execution and test boundaries are recorded separately. | Preserved upstream reference; not integrated |
| [free-to-paywall.yaml](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/e2e/screenshots/free-to-paywall.yaml) | Regression/scenario definitions for free to paywall; execution and test boundaries are recorded separately. | Preserved upstream reference; not integrated |
| [grammar-builder.yaml](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/e2e/screenshots/grammar-builder.yaml) | Regression/scenario definitions for grammar builder; execution and test boundaries are recorded separately. | Preserved upstream reference; not integrated |
| [mouth-map.yaml](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/e2e/screenshots/mouth-map.yaml) | Regression/scenario definitions for mouth map; execution and test boundaries are recorded separately. | Preserved upstream reference; not integrated |
| [onboard-free.yaml](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/e2e/screenshots/onboard-free.yaml) | Regression/scenario definitions for onboard free; execution and test boundaries are recorded separately. | Preserved upstream reference; not integrated |
| [onboard-plus.yaml](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/e2e/screenshots/onboard-plus.yaml) | Regression/scenario definitions for onboard plus; execution and test boundaries are recorded separately. | Preserved upstream reference; not integrated |
| [sounds-to-fix.yaml](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/e2e/screenshots/sounds-to-fix.yaml) | Regression/scenario definitions for sounds to fix; execution and test boundaries are recorded separately. | Preserved upstream reference; not integrated |
| [streaks.yaml](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/e2e/screenshots/streaks.yaml) | Regression/scenario definitions for streaks; execution and test boundaries are recorded separately. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/e2e/subflows/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/e2e/subflows/)

Upstream verification scenarios/fixtures for subflows. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [accept-open-link.yaml](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/e2e/subflows/accept-open-link.yaml) | Regression/scenario definitions for accept open link; execution and test boundaries are recorded separately. | Preserved upstream reference; not integrated |
| [answer-session.yaml](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/e2e/subflows/answer-session.yaml) | Regression/scenario definitions for answer session; execution and test boundaries are recorded separately. | Preserved upstream reference; not integrated |
| [decline-save-password.yaml](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/e2e/subflows/decline-save-password.yaml) | Regression/scenario definitions for decline save password; execution and test boundaries are recorded separately. | Preserved upstream reference; not integrated |
| [match-all.yaml](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/e2e/subflows/match-all.yaml) | Regression/scenario definitions for match all; execution and test boundaries are recorded separately. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/modules/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/modules/)

Original native-mobile modules modules, screens or supporting resources. Archived reference; not an active Eng Teacher feature or dependency.

Contains the subfolders listed in their own sections; no tracked files directly in this folder.

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/modules/cadence-app-attest/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/modules/cadence-app-attest/)

Original native-mobile cadence app attest modules, screens or supporting resources. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [expo-module.config.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/modules/cadence-app-attest/expo-module.config.json) | Structured expo module.config content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [package.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/modules/cadence-app-attest/package.json) | Containing component dependency/build/test declarations; consult its scope before installing. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/modules/cadence-app-attest/ios/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/modules/cadence-app-attest/ios/)

Original native-mobile ios modules, screens or supporting resources. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [CadenceAppAttest.podspec](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/modules/cadence-app-attest/ios/CadenceAppAttest.podspec) | Native Apple/mobile Cadence App Attest implementation, packaging or privacy declaration; not an active web/worker dependency. | Preserved upstream reference; not integrated |
| [CadenceAppAttestModule.swift](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/modules/cadence-app-attest/ios/CadenceAppAttestModule.swift) | Native Apple/mobile Cadence App Attest Module implementation, packaging or privacy declaration; not an active web/worker dependency. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/modules/cadence-icloud/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/modules/cadence-icloud/)

Original native-mobile cadence icloud modules, screens or supporting resources. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [expo-module.config.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/modules/cadence-icloud/expo-module.config.json) | Structured expo module.config content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [package.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/modules/cadence-icloud/package.json) | Containing component dependency/build/test declarations; consult its scope before installing. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/modules/cadence-icloud/ios/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/modules/cadence-icloud/ios/)

Original native-mobile ios modules, screens or supporting resources. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [CadenceICloud.podspec](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/modules/cadence-icloud/ios/CadenceICloud.podspec) | Native Apple/mobile Cadence ICloud implementation, packaging or privacy declaration; not an active web/worker dependency. | Preserved upstream reference; not integrated |
| [CadenceICloudModule.swift](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/modules/cadence-icloud/ios/CadenceICloudModule.swift) | Native Apple/mobile Cadence ICloud Module implementation, packaging or privacy declaration; not an active web/worker dependency. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/plugins/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/plugins/)

Original native-mobile plugins modules, screens or supporting resources. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [with-icloud-recordings.js](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/plugins/with-icloud-recordings.js) | with icloud recordings module; static declarations include withICloudRecordings. No behavior is executed by this guide. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/scripts/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/scripts/)

Original native-mobile scripts modules, screens or supporting resources. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [bump-ios-build.mjs](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/scripts/bump-ios-build.mjs) | bump ios build implementation/helper module in the containing upstream reference component. | Preserved upstream reference; not integrated |
| [ios-release.mjs](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/scripts/ios-release.mjs) | ios release module; static declarations include required, run, bundlingEnv, refuseTestEnv, checkArchivedBundle. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [sync-content.mjs](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/scripts/sync-content.mjs) | sync content module; static declarations include collectPacks, collectArticulation, plan, BundledPack, listFiles. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [sync-illustrations.mjs](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/scripts/sync-illustrations.mjs) | sync illustrations module; static declarations include IllustrationName. No behavior is executed by this guide. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/)

Original native-mobile src modules, screens or supporting resources. Archived reference; not an active Eng Teacher feature or dependency.

Contains the subfolders listed in their own sections; no tracked files directly in this folder.

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/api/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/api/)

Original upstream HTTP/API route area for api. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [account.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/api/account.ts) | account module; static declarations include getMe, setNewsletter, exportAccount, deleteAccount, getVersionInfo, syncSummary. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [client.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/api/client.ts) | client module; static declarations include Transport, ApiError, authHeader, send, FetchOptions, headersFor. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [endpoints.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/api/endpoints.ts) | endpoints module; static declarations include RecordedAudio, audioFormData, for, assess, transcribe, getAssessReadiness. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [transport.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/api/transport.ts) | transport module; static declarations include TransportMode, Transport, setTransport, NoTransportError, setLocalAiTransport, getLocalAiTransport. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [types.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/api/types.ts) | types module; static declarations include PronunciationStatus, PronunciationHighlight, PronunciationPhoneme, PronunciationAssessment, Module, UserProgress. No behavior is executed by this guide. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/app/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/app/)

Original native-mobile app modules, screens or supporting resources. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [+native-intent.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/app/%2Bnative-intent.tsx) | +native intent module; static declarations include redirectSystemPath. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [_layout.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/app/_layout.tsx) | layout module; static declarations include ErrorBoundary, RootNavigator, Gate, RootLayout. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [account.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/app/account.tsx) | account module; static declarations include AccountScreen, run. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [badges.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/app/badges.tsx) | badges module; static declarations include Badge, BadgeGroup, BadgesScreen, share, ShareStat, BadgeTile. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [onboarding.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/app/onboarding.tsx) | onboarding module; static declarations include OnboardingScreen. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [pair.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/app/pair.tsx) | pair module; static declarations include ConnectionFailure, PairLinkScreen, connect. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [plus.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/app/plus.tsx) | plus module; static declarations include PlusScreen. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [profile.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/app/profile.tsx) | profile module; static declarations include LearningGoal, PracticeCadence, ProfileScreen, ProfileForm, handleSave, edited. No behavior is executed by this guide. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/app/(auth)/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/app/%28auth%29/)

Original native-mobile (auth) modules, screens or supporting resources. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [_layout.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/app/%28auth%29/_layout.tsx) | layout module; static declarations include AuthLayout. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [forgot-password.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/app/%28auth%29/forgot-password.tsx) | forgot password module; static declarations include sendResetEmail, ForgotPasswordScreen, handleReset. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [index.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/app/%28auth%29/index.tsx) | index module; static declarations include AuthIndex. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [login.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/app/%28auth%29/login.tsx) | login module; static declarations include LoginScreen. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [signup.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/app/%28auth%29/signup.tsx) | signup module; static declarations include SignupScreen. No behavior is executed by this guide. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/app/(tabs)/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/app/%28tabs%29/)

Original native-mobile (tabs) modules, screens or supporting resources. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [_layout.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/app/%28tabs%29/_layout.tsx) | layout module; static declarations include TabBarBackground, TabsLayout. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [coach.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/app/%28tabs%29/coach.tsx) | coach module; static declarations include SavedCoachSession, CoachScreen, startSession, resume, confirmDelete, HistoryRow. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [conversation.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/app/%28tabs%29/conversation.tsx) | conversation module; static declarations include ConversationScreen, ScenarioCard. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [index.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/app/%28tabs%29/index.tsx) | index module; static declarations include RecordedAudio, HomeScreen, handleTake, pickWord, shuffle. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [play.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/app/%28tabs%29/play.tsx) | play module; static declarations include VocabLevel, GameInfo, GameId, GameResult, PlayScreen, DeckStat. No behavior is executed by this guide. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/app/(tabs)/learn/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/app/%28tabs%29/learn/)

Original native-mobile learn modules, screens or supporting resources. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [\[moduleId\].tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/app/%28tabs%29/learn/%5BmoduleId%5D.tsx) | \[module Id\] module; static declarations include ModuleLessonsScreen, LessonRow. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [_layout.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/app/%28tabs%29/learn/_layout.tsx) | layout module; static declarations include LearnLayout. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [index.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/app/%28tabs%29/learn/index.tsx) | index module; static declarations include PracticeMode, CefrLevel, LearnHub, NotOnPhone, ModeTile, HubRow. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [modules.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/app/%28tabs%29/learn/modules.tsx) | modules module; static declarations include ModulesScreen, ModuleCard. No behavior is executed by this guide. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/app/advanced/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/app/advanced/)

Original native-mobile advanced modules, screens or supporting resources. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [index.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/app/advanced/index.tsx) | index module; static declarations include AdvancedHub. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [plateau.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/app/advanced/plateau.tsx) | plateau module; static declarations include DiagnosticItem, Evidence, FossilError, Track, PlateauScreen, Intro. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [recordings.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/app/advanced/recordings.tsx) | recordings module; static declarations include Recording, ICloudStatus, RecordingsScreen, IconButton. No behavior is executed by this guide. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/app/advanced/phrases/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/app/advanced/phrases/)

Original native-mobile phrases modules, screens or supporting resources. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [\[id\].tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/app/advanced/phrases/%5Bid%5D.tsx) | \[id\] module; static declarations include Phrase, PhraseScreen, PhraseBody, GapFill, Rephrase, it. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [index.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/app/advanced/phrases/index.tsx) | index module; static declarations include PhraseBankScreen. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [practice.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/app/advanced/phrases/practice.tsx) | practice module; static declarations include Phrase, PhraseDrill, PhrasePracticeScreen, DrillCard. No behavior is executed by this guide. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/app/advanced/slang/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/app/advanced/slang/)

Original native-mobile slang modules, screens or supporting resources. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [\[id\].tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/app/advanced/slang/%5Bid%5D.tsx) | \[id\] module; static declarations include SlangEntryScreen. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [index.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/app/advanced/slang/index.tsx) | index module; static declarations include SlangFit, SlangRegion, SlangScreen. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [quiz.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/app/advanced/slang/quiz.tsx) | quiz module; static declarations include SlangEntry, SlangQuizScreen. No behavior is executed by this guide. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/app/coach/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/app/coach/)

Original native-mobile coach modules, screens or supporting resources. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [session.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/app/coach/session.tsx) | session module; static declarations include FlatList, RecordedAudio, CoachSessionTurn, SavedCoachSession, buildHistory, newSessionId. No behavior is executed by this guide. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/app/connect/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/app/connect/)

Original native-mobile connect modules, screens or supporting resources. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [_layout.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/app/connect/_layout.tsx) | layout module; static declarations include ConnectLayout. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [index.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/app/connect/index.tsx) | index module; static declarations include ConnectIndexScreen. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [manual.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/app/connect/manual.tsx) | manual module; static declarations include TextInput, ConnectionFailure, PairingPayload, ManualConnectScreen, connect. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [scan.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/app/connect/scan.tsx) | scan module; static declarations include ConnectionFailure, ScanScreen. No behavior is executed by this guide. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/app/conversation/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/app/conversation/)

Original native-mobile conversation modules, screens or supporting resources. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [\[slug\].tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/app/conversation/%5Bslug%5D.tsx) | \[slug\] module; static declarations include RecordedAudio, ConversationSessionScreen, ScenarioRun, handleTake, advance, retryTurn. No behavior is executed by this guide. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/app/game/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/app/game/)

Original native-mobile game modules, screens or supporting resources. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [_layout.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/app/game/_layout.tsx) | layout module; static declarations include GameLayout. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [flashcards.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/app/game/flashcards.tsx) | flashcards module; static declarations include CardState, Grade, FlashcardsScreen, FlashcardSession, finish, grade. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [meaning-match.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/app/game/meaning-match.tsx) | meaning match module; static declarations include ChoiceState, MeaningQuestion, newRound, MeaningMatchScreen, choose, next. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [scramble.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/app/game/scramble.tsx) | scramble module; static declarations include TileState, VocabWord, ScrambleTile, Phase, pickWords, tileLayoutFor. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [sound-match.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/app/game/sound-match.tsx) | sound match module; static declarations include ChoiceState, SoundRound, SoundMatchScreen, start, choose, next. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [spelling.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/app/game/spelling.tsx) | spelling module; static declarations include VocabWord, Verdict, SpellingScreen, submit, next, finish. No behavior is executed by this guide. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/app/grammar/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/app/grammar/)

Original native-mobile grammar modules, screens or supporting resources. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [\[pointId\].tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/app/grammar/%5BpointId%5D.tsx) | \[point Id\] module; static declarations include GrammarPointScreen. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [index.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/app/grammar/index.tsx) | index module; static declarations include CefrLevel, GrammarPoint, GrammarIndex, PointRow. No behavior is executed by this guide. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/app/lesson/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/app/lesson/)

Original native-mobile lesson modules, screens or supporting resources. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [\[lessonId\].tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/app/lesson/%5BlessonId%5D.tsx) | \[lesson Id\] module; static declarations include RecordedAudio, LessonScreen, TheoryLesson, markAsRead, WordQueueLesson, retryWord. No behavior is executed by this guide. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/app/practice/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/app/practice/)

Original native-mobile practice modules, screens or supporting resources. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [\[mode\].tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/app/practice/%5Bmode%5D.tsx) | \[mode\] module; static declarations include PracticeMode, PracticeScreen. No behavior is executed by this guide. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/app/practice/lesson/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/app/practice/lesson/)

Original native-mobile lesson modules, screens or supporting resources. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [\[lessonId\].tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/app/practice/lesson/%5BlessonId%5D.tsx) | \[lesson Id\] module; static declarations include GrammarLessonScreen. No behavior is executed by this guide. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/app/settings/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/app/settings/)

Original native-mobile settings modules, screens or supporting resources. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [index.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/app/settings/index.tsx) | index module; static declarations include PermissionState, SettingsScreen, setReminder, restore, confirmSignOut. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [level.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/app/settings/level.tsx) | level module; static declarations include CefrLevel, LevelSkill, SkillChoice, LevelSettingsScreen. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [onboarding.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/app/settings/onboarding.tsx) | onboarding module; static declarations include SetupAgainScreen. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [packs.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/app/settings/packs.tsx) | packs module; static declarations include AvailablePack, formatBytes, PacksScreen, refreshAll, get, remove. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [placement.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/app/settings/placement.tsx) | placement module; static declarations include RetakePlacementScreen. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [sign-in.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/app/settings/sign-in.tsx) | sign in module; static declarations include ProviderMethod, SignInMethod, Message, MethodIcon, SignInMethodsScreen, run. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [voice.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/app/settings/voice.tsx) | voice module; static declarations include options, CoachVoiceScreen, change. No behavior is executed by this guide. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/app/sounds/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/app/sounds/)

Original sounds assets, models or packaging resources; retain associated notices. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [\[soundId\].tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/app/sounds/%5BsoundId%5D.tsx) | \[sound Id\] module; static declarations include SoundScreen. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [compare.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/app/sounds/compare.tsx) | compare module; static declarations include ChoiceState, CompareScreen, play, pickWord. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [index.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/app/sounds/index.tsx) | index module; static declarations include SoundsLibrary. No behavior is executed by this guide. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/app/sounds/drill/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/app/sounds/drill/)

Original drill assets, models or packaging resources; retain associated notices. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [\[soundId\].tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/app/sounds/drill/%5BsoundId%5D.tsx) | \[sound Id\] module; static declarations include RecordedAudio, DrillScreen, handleTake. No behavior is executed by this guide. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/app/word/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/app/word/)

Original native-mobile word modules, screens or supporting resources. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [\[wordId\].tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/app/word/%5BwordId%5D.tsx) | \[word Id\] module; static declarations include RecordedAudio, WordScreen, handleTake. No behavior is executed by this guide. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/audio/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/audio/)

Original native-mobile audio modules, screens or supporting resources. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [feedback.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/audio/feedback.ts) | feedback module; static declarations include AudioSource, play, playAssessmentFeedback, playCompletionSound. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [recorder.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/audio/recorder.ts) | recorder module; static declarations include RecordingOptions, enableRecordingMode, enablePlaybackMode, recordedAudioFromUri. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [reference-audio.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/audio/reference-audio.ts) | reference audio module; static declarations include ReferenceAudioError, cacheKey, cacheDirectory, discard, getReferenceAudio, prefetchReferenceAudio. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [take-machine.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/audio/take-machine.ts) | take machine module; static declarations include TakeStatus, TakeState, TakeEvent, idle, takeReducer, isBusy. No behavior is executed by this guide. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/components/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/components/)

Original upstream components UI components. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [AiOffer.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/components/AiOffer.tsx) | Ai Offer module; static declarations include AiOffer, act. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [BadgeCelebration.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/components/BadgeCelebration.tsx) | Badge Celebration module; static declarations include BadgeCelebration. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [EngagementWatcher.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/components/EngagementWatcher.tsx) | Engagement Watcher module; static declarations include Href, Badge, EngagementWatcher, forgetPushRegistration. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [Illustration.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/components/Illustration.tsx) | Illustration module; static declarations include StyleProp, ViewStyle, IllustrationName, recolour, Illustration. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [LaunchSplash.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/components/LaunchSplash.tsx) | Launch Splash module; static declarations include liquidPath, rise, LaunchSplash. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [NewsletterToggle.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/components/NewsletterToggle.tsx) | Newsletter Toggle module; static declarations include NewsletterToggle, change. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [TimePicker.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/components/TimePicker.tsx) | Time Picker module; static declarations include TimePicker. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [UpdateNotice.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/components/UpdateNotice.tsx) | Update Notice module; static declarations include UpdateNotice, useUpdateNotice, UpdateBanner, UpdateGate. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [settings.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/components/settings.tsx) | settings module; static declarations include SettingsRow, SwitchRow. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [status.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/components/status.tsx) | status module; static declarations include ServerBanner, ReadinessBanner. No behavior is executed by this guide. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/components/auth/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/components/auth/)

Original upstream auth UI components. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [SignInOptions.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/components/auth/SignInOptions.tsx) | Sign In Options module; static declarations include TextInput, ProviderMethod, AuthField, Wordmark, TestBuildNote, AuthIntent. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [SwitchLine.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/components/auth/SwitchLine.tsx) | Switch Line module; static declarations include SwitchLine. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [layout.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/components/auth/layout.tsx) | Upstream framework layout entrypoint for auth. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/components/billing/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/components/billing/)

Original upstream billing UI components. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [PaywallHero.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/components/billing/PaywallHero.tsx) | Paywall Hero module; static declarations include PaywallHero. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [PlusPaywall.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/components/billing/PlusPaywall.tsx) | Plus Paywall module; static declarations include PlusPlan, PlusPlanId, planDetail, PlusPaywall, buy, restore. No behavior is executed by this guide. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/components/exercises/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/components/exercises/)

Original upstream exercises UI components. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [ExerciseView.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/components/exercises/ExerciseView.tsx) | Exercise View module; static declarations include ChoiceState, Exercise, ExerciseAnswer, GradeResult, ExerciseViewProps, seedFor. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [SessionRunner.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/components/exercises/SessionRunner.tsx) | Session Runner module; static declarations include CefrLevel, Exercise, ExerciseAnswer, GradeResult, SessionRunnerProps, SessionRunner. No behavior is executed by this guide. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/components/games/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/components/games/)

Original upstream games UI components. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [ChoiceButton.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/components/games/ChoiceButton.tsx) | Choice Button module; static declarations include ChoiceState, ChoiceButton, pressTo. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [FlipCard.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/components/games/FlipCard.tsx) | Flip Card module; static declarations include FlipCard. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [LetterTile.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/components/games/LetterTile.tsx) | Letter Tile module; static declarations include TileState, LetterTile, pressTo. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [RoundSummary.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/components/games/RoundSummary.tsx) | Round Summary module; static declarations include SummaryItem, RoundSummary. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [ScoreStrip.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/components/games/ScoreStrip.tsx) | Score Strip module; static declarations include ScoreStrip. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [SpeakerButton.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/components/games/SpeakerButton.tsx) | Speaker Button module; static declarations include SpeakerButton. No behavior is executed by this guide. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/components/mouth-map/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/components/mouth-map/)

Original upstream mouth map UI components. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [CompareView.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/components/mouth-map/CompareView.tsx) | Compare View module; static declarations include Side, CompareView. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [FrontLipsView.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/components/mouth-map/FrontLipsView.tsx) | Front Lips View module; static declarations include OverlayId, VocalTractParams, FrontLipsView. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [MouthMap.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/components/mouth-map/MouthMap.tsx) | Mouth Map module; static declarations include MouthPalette, MotionGoal, useMouthPalette, goalFor, mouthLabel, MouthMap. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [VocalTractView.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/components/mouth-map/VocalTractView.tsx) | Vocal Tract View module; static declarations include LayerId, OverlayId, PlaceAnchor, Point, VocalTractParams, VocalTractViewProps. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [index.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/components/mouth-map/index.ts) | index module; static declarations include MouthPalette. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [palette.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/components/mouth-map/palette.ts) | palette module; static declarations include MouthPalette. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [useArticulationMotion.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/components/mouth-map/useArticulationMotion.ts) | use Articulation Motion module; static declarations include Keyframe, VocalTractParams, MotionGoal, goalStart, goalEnd, Motion. No behavior is executed by this guide. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/components/onboarding/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/components/onboarding/)

Original upstream onboarding UI components. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [AccountStep.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/components/onboarding/AccountStep.tsx) | Account Step module; static declarations include AuthIntent, AccountStep. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [ChoiceCard.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/components/onboarding/ChoiceCard.tsx) | Choice Card module; static declarations include ChoiceCard. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [OnboardingFlow.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/components/onboarding/OnboardingFlow.tsx) | Onboarding Flow module; static declarations include ReactNode, DailyGoal, OnboardingAnswers, OnboardingPosition, OnboardingFlow, finish. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [OnboardingProgress.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/components/onboarding/OnboardingProgress.tsx) | Onboarding Progress module; static declarations include LayoutChangeEvent, OnboardingProgress. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [OnboardingTopBar.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/components/onboarding/OnboardingTopBar.tsx) | Onboarding Top Bar module; static declarations include OnboardingTopBar. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [PlacementQuiz.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/components/onboarding/PlacementQuiz.tsx) | Placement Quiz module; static declarations include CefrLevel, PlacementQuiz, answer. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [StepHeading.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/components/onboarding/StepHeading.tsx) | Step Heading module; static declarations include StepHeading. No behavior is executed by this guide. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/components/placement/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/components/placement/)

Original upstream placement UI components. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [PlacementTest.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/components/placement/PlacementTest.tsx) | Placement Test module; static declarations include CefrLevel, Exercise, ExerciseAnswer, AdaptiveResponse, AdaptiveResult, BankItem. No behavior is executed by this guide. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/components/practice/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/components/practice/)

Original upstream practice UI components. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [AssessmentView.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/components/practice/AssessmentView.tsx) | Assessment View module; static declarations include spokenWord, AssessmentView, openSound, hearWord. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [CoachBubble.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/components/practice/CoachBubble.tsx) | Coach Bubble module; static declarations include CoachBubble, ReplyPanel. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [RecorderPanel.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/components/practice/RecorderPanel.tsx) | Recorder Panel module; static declarations include RecorderPanelProps, RecorderPanel. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [ResultSummary.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/components/practice/ResultSummary.tsx) | Result Summary module; static declarations include ChipStatus, SummaryItem, ResultSummary. No behavior is executed by this guide. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/components/ui/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/components/ui/)

Original upstream ui UI components. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [buttons.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/components/ui/buttons.tsx) | buttons module; static declarations include PressableProps, StyleProp, ViewStyle, ButtonVariant, buttonIconColor, Button. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [feedback.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/components/ui/feedback.tsx) | feedback module; static declarations include StyleProp, ViewStyle, BannerTone, Banner, EmptyState, useReduceMotion. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [forms.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/components/ui/forms.tsx) | forms module; static declarations include Ref, TextInputProps, FieldLabel, TextField, OptionRow, MultiOptionRow. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [index.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/components/ui/index.tsx) | index implementation/helper module in the containing upstream reference component. | Preserved upstream reference; not integrated |
| [layout.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/components/ui/layout.tsx) | Upstream framework layout entrypoint for ui. | Preserved upstream reference; not integrated |
| [progress.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/components/ui/progress.tsx) | progress module; static declarations include StyleProp, ViewStyle, ProgressBar, SegmentedProgress, ProgressRing, StatTile. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [text.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/components/ui/text.tsx) | text module; static declarations include Href, StyleProp, TextStyle, Title, Body, Eyebrow. No behavior is executed by this guide. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/content/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/content/)

Upstream authored content content, pack data or fixtures; content rights/quality need separate review. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [articulation.generated.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/content/articulation.generated.json) | Structured articulation.generated content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [articulation.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/content/articulation.ts) | articulation module; static declarations include AccentVariant, ArticulationTarget, SoundInfo, targetFor, soundsFor, ipaFor. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [bundled.generated.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/content/bundled.generated.ts) | bundled.generated module; static declarations include BundledPack. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [catalog.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/content/catalog.ts) | catalog module; static declarations include CefrLevel, Exercise, ExerciseKind, FlashcardExercise, GrammarPoint, Lesson. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [packs.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/content/packs.ts) | packs module; static declarations include CefrLevel, PackContent, PackIndex, PackManifest, InstalledPack, DownloadedRecord. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [useContent.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/content/useContent.ts) | use Content module; static declarations include CefrLevel, useInstalledPacks, useLevelPack, useLearnLevel, parseLevelParam, usePlacementBank. No behavior is executed by this guide. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/content/fixtures/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/content/fixtures/)

Upstream verification scenarios/fixtures for fixtures. Archived reference; not an active Eng Teacher feature or dependency.

Contains the subfolders listed in their own sections; no tracked files directly in this folder.

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/content/fixtures/articulation/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/content/fixtures/articulation/)

Upstream verification scenarios/fixtures for articulation. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [fixture.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/content/fixtures/articulation/fixture.json) | Structured fixture content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/content/fixtures/packs/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/content/fixtures/packs/)

Upstream verification scenarios/fixtures for packs. Archived reference; not an active Eng Teacher feature or dependency.

Contains the subfolders listed in their own sections; no tracked files directly in this folder.

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/content/fixtures/packs/core-a1/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/content/fixtures/packs/core-a1/)

Upstream verification scenarios/fixtures for core a1. Archived reference; not an active Eng Teacher feature or dependency.

Contains the subfolders listed in their own sections; no tracked files directly in this folder.

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/content/fixtures/packs/core-a1/v1/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/content/fixtures/packs/core-a1/v1/)

Upstream verification scenarios/fixtures for v1. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [content.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/content/fixtures/packs/core-a1/v1/content.json) | Structured content content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/content/fixtures/packs/core-b1/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/content/fixtures/packs/core-b1/)

Upstream verification scenarios/fixtures for core b1. Archived reference; not an active Eng Teacher feature or dependency.

Contains the subfolders listed in their own sections; no tracked files directly in this folder.

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/content/fixtures/packs/core-b1/v1/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/content/fixtures/packs/core-b1/v1/)

Upstream verification scenarios/fixtures for v1. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [content.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/content/fixtures/packs/core-b1/v1/content.json) | Structured content content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/context/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/context/)

Original native-mobile context modules, screens or supporting resources. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [account.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/context/account.tsx) | account module; static declarations include StoreStatus, Me, AiCapability, DataTier, AccountValue, AccountProvider. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [auth.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/context/auth.tsx) | auth module; static declarations include User, Profile, StoredProfile, LearningGoal, PracticeCadence, PracticeFocus. No behavior is executed by this guide. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/copy/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/copy/)

Original native-mobile copy modules, screens or supporting resources. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [ai-offer.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/copy/ai-offer.ts) | ai offer module; static declarations include blockMessage, offerLabel. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [auth-errors.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/copy/auth-errors.ts) | auth errors module; static declarations include authErrorCode, AuthErrorContext, isCancelledSignIn, describeAuthError. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [errors.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/copy/errors.ts) | errors module; static declarations include messageOf, describeError. No behavior is executed by this guide. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/data/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/data/)

Original native-mobile data modules, screens or supporting resources. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [illustrations.generated.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/data/illustrations.generated.ts) | illustrations.generated module; static declarations include IllustrationName. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [minimal-pairs.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/data/minimal-pairs.ts) | minimal pairs module; static declarations include PairGroup, pairGroup. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [pair-sounds.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/data/pair-sounds.ts) | pair sounds implementation/helper module in the containing upstream reference component. | Preserved upstream reference; not integrated |
| [practice-targets.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/data/practice-targets.ts) | practice targets module; static declarations include PracticeTarget. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [svg.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/data/svg.ts) | svg implementation/helper module in the containing upstream reference component. | Preserved upstream reference; not integrated |
| [vocabulary.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/data/vocabulary.ts) | vocabulary module; static declarations include VocabLevel, PartOfSpeech, VocabWord, isVocabLevel, parseLevel, levelLabel. No behavior is executed by this guide. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/engagement/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/engagement/)

Original native-mobile engagement modules, screens or supporting resources. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [badges.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/engagement/badges.ts) | badges module; static declarations include CefrLevel, BadgeGroup, Badge, ContentFacts, BadgeInput, lessonsDoneAt. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [streak.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/engagement/streak.ts) | streak module; static declarations include StreakStatus, normaliseDays, streakStatus, daysToNextFreeze. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [today.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/engagement/today.ts) | today module; static declarations include StreakStatus, DailyGoal, isDailyGoal, TodayStatus, todayStatus, dueByDay. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [useEngagement.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/engagement/useEngagement.ts) | use Engagement module; static declarations include Badge, ContentFacts, TodayStatus, loadFacts, useContentFacts, useTodayKey. No behavior is executed by this guide. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/engine/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/engine/)

Original native-mobile engine modules, screens or supporting resources. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [useEngineRoute.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/engine/useEngineRoute.ts) | use Engine Route module; static declarations include AiCapability, RouteDecision, useEngineRoute. No behavior is executed by this guide. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/games/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/games/)

Original native-mobile games modules, screens or supporting resources. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [catalog.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/games/catalog.ts) | catalog module; static declarations include GameInfo, gameInfo. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [progress.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/games/progress.ts) | progress module; static declarations include CardState, Grade, GameId, GameResult, GameProgress, emptyProgress. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [quiz.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/games/quiz.ts) | quiz module; static declarations include Rng, pointsFor, accuracy, RoundTally, tallyAnswer, roundVerdict. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [random.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/games/random.ts) | random module; static declarations include Rng, seededRng, clockSeed, shuffle, pickOne, sample. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [srs.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/games/srs.ts) | srs implementation/helper module in the containing upstream reference component. | Preserved upstream reference; not integrated |
| [store.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/games/store.ts) | store module; static declarations include GameProgress, GameResult, storageKey, Snapshot, emit, subscribe. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [text.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/games/text.ts) | text module; static declarations include Rng, normalizeAnswer, levenshtein, SpellingCheck, checkSpelling, LetterStatus. No behavior is executed by this guide. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/hooks/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/hooks/)

Original native-mobile hooks modules, screens or supporting resources. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [useAccent.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/hooks/useAccent.ts) | use Accent module; static declarations include useAccent. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [useCoachVoice.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/hooks/useCoachVoice.ts) | use Coach Voice module; static declarations include CoachVoiceSettings, voiceInstruct, sanitize, emit, subscribe, getSnapshot. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [useEngineReadiness.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/hooks/useEngineReadiness.ts) | use Engine Readiness module; static declarations include EngineReadiness, useAssessReadiness, useCoachReadiness, blockedReadiness. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [useEnterAppWhenPaired.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/hooks/useEnterAppWhenPaired.ts) | use Enter App When Paired module; static declarations include useEnterAppWhenPaired. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [useExitGuard.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/hooks/useExitGuard.ts) | use Exit Guard module; static declarations include useExitGuard. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [usePlayback.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/hooks/usePlayback.ts) | use Playback module; static declarations include AudioPlayer, Playback, usePlayback. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [usePracticeVoice.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/hooks/usePracticeVoice.ts) | use Practice Voice module; static declarations include PracticeVoice, usePracticeVoice. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [useRefresh.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/hooks/useRefresh.ts) | use Refresh module; static declarations include useRefresh, onRefresh. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [useServerStatus.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/hooks/useServerStatus.ts) | use Server Status module; static declarations include ServerStatus, useServerStatus, useServerStatusBase. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [useSpeech.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/hooks/useSpeech.ts) | use Speech module; static declarations include Speech, useSpeech, playAt, speechStateFor. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [useTakeRecorder.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/hooks/useTakeRecorder.ts) | use Take Recorder module; static declarations include TakeHint, TakeState, TakeRecorder, useTakeRecorder. No behavior is executed by this guide. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/learning/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/learning/)

Original native-mobile learning modules, screens or supporting resources. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [advanced-content.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/learning/advanced-content.ts) | advanced content module; static declarations include AdvancedContent, readBundled, Body, load, loadAdvancedContent, useAdvancedContent. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [advanced-state.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/learning/advanced-state.ts) | advanced state module; static declarations include Track, StoredCard, AdvancedState, parseAdvancedState. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [advanced-store.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/learning/advanced-store.ts) | advanced store module; static declarations include Track, PracticeListItem, RecordingIndex, Grade, AdvancedState, StoredCard. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [advanced-ui.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/learning/advanced-ui.tsx) | advanced ui module; static declarations include Tag, ItemRow, SelfRating, RateRow, QuizOptions, Highlighted. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [deck.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/learning/deck.ts) | deck module; static declarations include deckFor, todaysCards, deckSummary. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [goals.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/learning/goals.ts) | goals module; static declarations include LearningGoal, useLearningGoals. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [level-store.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/learning/level-store.ts) | level store module; static declarations include LevelPrefs, LevelSkill, currentLevel, useLevel, setOverallLevel, setSkillLevel. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [levels.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/learning/levels.ts) | levels module; static declarations include LevelPrefs, useLevelSync. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [log.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/learning/log.ts) | log module; static declarations include FinishedSession, logPractice, useSessionClock. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [state.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/learning/state.ts) | state module; static declarations include Activity, ActivityKind, ProgressSummary, SoundMasteryMap, CardState, Grade. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [store.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/learning/store.ts) | store module; static declarations include LearningState, Snapshot, emit, subscribe, setLearner, getLearning. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [sync.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/learning/sync.ts) | sync module; static declarations include syncOnce, syncProgress. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [useTarget.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/learning/useTarget.ts) | use Target module; static declarations include TargetSource, useTarget. No behavior is executed by this guide. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/lib/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/lib/)

Original native-mobile lib modules, screens or supporting resources. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [app-check-rest.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/lib/app-check-rest.ts) | app check rest module; static declarations include attestationBody, assertionBody, isAppCheckRefusal. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [app-check.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/lib/app-check.ts) | app check module; static declarations include AppAttestModule, endpoint, post, TokenResponse, viaDebug, viaAppAttest. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [coach-storage.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/lib/coach-storage.ts) | coach storage module; static declarations include CoachSessionTurn, SavedCoachSession, storageKey, readCoachSessions, saveCoachSession, deleteCoachSession. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [config.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/lib/config.ts) | config build/runtime/tool configuration for the containing component. | Preserved upstream reference; not integrated |
| [firebase-env.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/lib/firebase-env.ts) | firebase env module; static declarations include AuthTarget, isDemoProject, authTarget, hostOf, releaseEnvProblems, bundleProblems. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [firebase-providers.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/lib/firebase-providers.ts) | firebase providers module; static declarations include AuthCredential, User, PendingLink, SignInMethod, ProviderMethod, ProviderUnavailableError. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [firebase.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/lib/firebase.ts) | firebase module; static declarations include Auth, getFirebaseAuth, requireFirebaseAuth. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [haptics.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/lib/haptics.ts) | haptics module; static declarations include quietly. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [install-id.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/lib/install-id.ts) | install id module; static declarations include getInstallId. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [me.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/lib/me.ts) | me module; static declarations include AiCapability, DailyUsage, DataTier, PlusRecord, Me, parsePlus. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [prefs.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/lib/prefs.ts) | prefs module; static declarations include DailyGoal, Prefs, parsePrefs, setPref. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [profile.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/lib/profile.ts) | profile module; static declarations include LearningGoal, PracticeFocus, LevelPrefs, Profile, PracticeCadence, StoredProfile. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [stored-value.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/lib/stored-value.ts) | stored value module; static declarations include StoredValue, storedValue. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [version-check.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/lib/version-check.ts) | version check module; static declarations include VersionInfo, UpdateNotice, toBuild, parseVersionInfo, compareVersions, updateNotice. No behavior is executed by this guide. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/lib/billing/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/lib/billing/)

Original native-mobile billing modules, screens or supporting resources. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [no-browser-mode.js](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/lib/billing/no-browser-mode.js) | no browser mode implementation/helper module in the containing upstream reference component. | Preserved upstream reference; not integrated |
| [plans.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/lib/billing/plans.ts) | plans module; static declarations include PlusPlanId, PlusPlan, or, planForPackage, sortPlans, yearlySavingsPercent. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [purchases.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/lib/billing/purchases.ts) | purchases module; static declarations include CustomerInfo, PurchasesPackage, PlusPlan, PlusPlanId, StoreStatus, PurchaseError. No behavior is executed by this guide. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/lib/widget/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/lib/widget/)

Original native-mobile widget modules, screens or supporting resources. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [snapshot.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/lib/widget/snapshot.ts) | snapshot module; static declarations include VocabWord, WidgetWord, CadenceWidgetSnapshot, dayNumber, wordOfTheDay, SnapshotInput. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [sync.ios.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/lib/widget/sync.ios.ts) | sync.ios module; static declarations include reload, syncWidget, clearWidget. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [sync.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/lib/widget/sync.ts) | sync module; static declarations include syncWidget, clearWidget. No behavior is executed by this guide. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/notifications/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/notifications/)

Original native-mobile notifications modules, screens or supporting resources. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [plan.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/notifications/plan.ts) | plan module; static declarations include QuietHours, ReminderSettings, NotificationKind, PlannedNotification, PlanInput, inQuietHours. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [schedule.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/notifications/schedule.ts) | schedule module; static declarations include PlannedNotification, PermissionState, notificationPermission, askForNotifications, replacePlan, clearPlan. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [settings.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/notifications/settings.ts) | settings module; static declarations include ReminderSettings, updateReminders. No behavior is executed by this guide. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/onboarding/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/onboarding/)

Original native-mobile onboarding modules, screens or supporting resources. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [flow.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/onboarding/flow.ts) | flow module; static declarations include LearningGoal, CefrLevel, DailyGoal, OnboardingStep, LearningGoal, shortExamLine. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [placement.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/onboarding/placement.ts) | placement module; static declarations include CefrLevel, MultipleChoiceExercise, placementLevel, placementScore. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [store.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/onboarding/store.ts) | store module; static declarations include OnboardingAnswers, OnboardingPosition, StoredOnboarding, getOnboarding, saveOnboardingProgress, completeOnboarding. No behavior is executed by this guide. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/pairing/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/pairing/)

Original native-mobile pairing modules, screens or supporting resources. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [address.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/pairing/address.ts) | address module; static declarations include ParsedAddress, parseAddress, isValidPort. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [client.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/pairing/client.ts) | client module; static declarations include ClaimResponse, PairingPayload, ServerInfo, ConnectionFailure, ProbeResult, probeServer. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [context.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/pairing/context.tsx) | context module; static declarations include ConnectionState, StoredConnection, AppMode, ConnectionValue, ConnectionProvider, API. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [discovery.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/pairing/discovery.ts) | discovery module; static declarations include ServerInfo, StoredConnection, ConnectionState, NetworkContext, DiscoveryEvent, buildCandidates. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [errors.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/pairing/errors.ts) | errors module; static declarations include ConnectionFailure, FailureMessage, the, describeFailure, failureFromServerCode, failureFromParseFailure. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [protocol.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/pairing/protocol.ts) | protocol module; static declarations include removed, into, PairingPayload, PairedDeviceSummary, ServerInfo, ClaimRequest. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [storage.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/pairing/storage.ts) | storage module; static declarations include StoredPairing, readPairing, writePairing, updateStoredConnection, clearPairing. No behavior is executed by this guide. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/platform/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/platform/)

Original native-mobile platform modules, screens or supporting resources. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [content-model.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/platform/content-model.ts) | content model module; static declarations include CefrLevel, isCefrLevel, compareCefr, prefix, IdPrefix, isContentId. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [daily-plan.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/platform/daily-plan.ts) | daily plan module; static declarations include runs, LearningGoal, PlanInput, PlanItem, DailyPlan, weakSounds. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [engine-routing.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/platform/engine-routing.ts) | engine routing module; static declarations include AiCapability, PlusSource, PlusRecord, isRecordActive, resolvePlus, hasPlus. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [fossilization.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/platform/fossilization.ts) | fossilization module; static declarations include CardState, Grade, FossilArea, FossilError, FossilizationData, validateFossilError. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [goals.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/platform/goals.ts) | goals module; static declarations include LearningGoal, PracticeFocus, isLearningGoal, parseGoals, toggleGoal, sameGoals. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [levels.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/platform/levels.ts) | levels module; static declarations include CefrLevel, LevelInfo, examLine, LevelSkill, LevelSource, LevelPrefs. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [phrase-bank.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/platform/phrase-bank.ts) | phrase bank module; static declarations include CefrLevel, CardState, Grade, PhraseSituation, PhraseKind, Phrase. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [placement.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/platform/placement.ts) | placement module; static declarations include CefrLevel, Exercise, PlacementItem, PlacementScores, PlacementConfidence, PlacementEstimate. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [practice-day.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/platform/practice-day.ts) | practice day module; static declarations include FossilError, Track, Phrase, PracticeListItem, SlangEntry, CardState. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [progress-model.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/platform/progress-model.ts) | progress model module; static declarations include CefrLevel, ActivityKind, RecentResult, ProgressSummary, Activity, emptySummary. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [recordings.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/platform/recordings.ts) | recordings module; static declarations include RecordingKind, Recording, RecordingIndex, isRecording, parseIndex, recordingId. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [sign-in-methods.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/platform/sign-in-methods.ts) | sign in methods module; static declarations include SignInMethod, SignInSurface, isSignInMethod, methodLabel, continueLabel, providerButtons. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [srs.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/platform/srs.ts) | srs module; static declarations include Grade, CardState, dayKey, addDays, isNew, isDue. No behavior is executed by this guide. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/platform/vocal-tract/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/platform/vocal-tract/)

Original native-mobile vocal tract modules, screens or supporting resources. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [animate.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/platform/vocal-tract/animate.ts) | animate module; static declarations include VocalTractParams, lerpParams, easeInOut, Keyframe, paramsAt, glottisPulse. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [articulation.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/platform/vocal-tract/articulation.ts) | articulation module; static declarations include VocalTractParams, AccentVariant, SoundKind, SoundInfo, Place, Manner. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [codebook.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/platform/vocal-tract/codebook.ts) | codebook module; static declarations include CodebookEntry. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [fit.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/platform/vocal-tract/fit.ts) | fit module; static declarations include MovablePoints, ParamKey, Point, VocalTractParams, FitTargets, FitOptions. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [geometry.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/platform/vocal-tract/geometry.ts) | geometry module; static declarations include Run, Subpath, LayerId, FillId, GlottisShape, VocalTractShape. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [index.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/platform/vocal-tract/index.ts) | index implementation/helper module in the containing upstream reference component. | Preserved upstream reference; not integrated |
| [maeda.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/platform/vocal-tract/maeda.ts) | maeda module; static declarations include VocalTractParams, ParamKey, paramsFromVector, paramsToVector, clampParam, Point. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [svg-path.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/platform/vocal-tract/svg-path.ts) | svg path module; static declarations include Viewport, Box, createViewport, runCommands, subpathToSvg, subpathsToSvg. No behavior is executed by this guide. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/practice/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/practice/)

Original native-mobile practice modules, screens or supporting resources. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [narration.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/practice/narration.ts) | narration module; static declarations include htmlToPlainText, narrationChunks. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [progression.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/practice/progression.ts) | progression module; static declarations include LessonKind, passMark, didPass, LessonLike, inOrder, isCleared. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [scoring.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/practice/scoring.ts) | scoring module; static declarations include ScoreStatus, normalizeScore, scoreStatus, scoreLabel, averageScore, bestScore. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [sound-coach.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/practice/sound-coach.ts) | sound coach module; static declarations include DrillStep, SoundMastery, SoundMasteryMap, emptyMastery, addDays, clampScore. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [sounds.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/practice/sounds.ts) | sounds module; static declarations include ArticulationTarget, OverlayId, SoundInfo, describeTarget, compareTargets, soundIdForSymbol. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [targets.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/practice/targets.ts) | targets module; static declarations include PracticeTarget, TargetGroup, titleCase, targetGroups, suggestedGroupKey. No behavior is executed by this guide. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/recordings/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/recordings/)

Original native-mobile recordings modules, screens or supporting resources. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [RecordCompare.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/recordings/RecordCompare.tsx) | Record Compare module; static declarations include TargetSource, Pill, RecordCompare, run, record, keep. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [icloud.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/recordings/icloud.ts) | icloud module; static declarations include ICloudModule, ICloudStatus, icloudStatus, icloudEnabled, setICloudEnabled, copyToICloud. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [store.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/recordings/store.ts) | store module; static declarations include Recording, RecordingIndex, dir, readIndex, write, serial. No behavior is executed by this guide. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/theme/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/theme/)

Original native-mobile theme modules, screens or supporting resources. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [theme.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/theme/theme.ts) | theme module; static declarations include Palette, scale, scoreColor, ColorScheme, currentScheme, applyColorScheme. No behavior is executed by this guide. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/types/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/types/)

Original native-mobile types modules, screens or supporting resources. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [assets.d.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/src/types/assets.d.ts) | assets.d implementation/helper module in the containing upstream reference component. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/targets/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/targets/)

Original native-mobile targets modules, screens or supporting resources. Archived reference; not an active Eng Teacher feature or dependency.

Contains the subfolders listed in their own sections; no tracked files directly in this folder.

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/targets/widget/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/targets/widget/)

Original native-mobile widget modules, screens or supporting resources. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [CadenceWidget.swift](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/targets/widget/CadenceWidget.swift) | Native Apple/mobile Cadence Widget implementation, packaging or privacy declaration; not an active web/worker dependency. | Preserved upstream reference; not integrated |
| [FunnelDisplay-OFL.txt](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/targets/widget/FunnelDisplay-OFL.txt) | Documentation/research record for Funnel Display OFL; requirements and historical observations are not automatically implemented behavior. | Preserved upstream reference; not integrated |
| [FunnelDisplay_500Medium.ttf](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/targets/widget/FunnelDisplay_500Medium.ttf) | Funnel Display 500 Medium visual/font/icon resource; preserve applicable asset attribution and review rights before reuse. | Preserved upstream reference; not integrated |
| [FunnelDisplay_700Bold.ttf](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/targets/widget/FunnelDisplay_700Bold.ttf) | Funnel Display 700 Bold visual/font/icon resource; preserve applicable asset attribution and review rights before reuse. | Preserved upstream reference; not integrated |
| [Info.plist](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/targets/widget/Info.plist) | Native Apple/mobile Info implementation, packaging or privacy declaration; not an active web/worker dependency. | Preserved upstream reference; not integrated |
| [PrivacyInfo.xcprivacy](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/targets/widget/PrivacyInfo.xcprivacy) | Native Apple/mobile Privacy Info implementation, packaging or privacy declaration; not an active web/worker dependency. | Preserved upstream reference; not integrated |
| [Snapshot.swift](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/targets/widget/Snapshot.swift) | Native Apple/mobile Snapshot implementation, packaging or privacy declaration; not an active web/worker dependency. | Preserved upstream reference; not integrated |
| [expo-target.config.js](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/targets/widget/expo-target.config.js) | expo target.config build/runtime/tool configuration for the containing component. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/targets/widget/Assets.xcassets/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/targets/widget/Assets.xcassets/)

Original Assets.xcassets assets, models or packaging resources; retain associated notices. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [Contents.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/targets/widget/Assets.xcassets/Contents.json) | Structured Contents content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/targets/widget/Assets.xcassets/CadenceMark.imageset/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/targets/widget/Assets.xcassets/CadenceMark.imageset/)

Original Cadence Mark.imageset assets, models or packaging resources; retain associated notices. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [CadenceMark.svg](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/targets/widget/Assets.xcassets/CadenceMark.imageset/CadenceMark.svg) | Cadence Mark visual/font/icon resource; preserve applicable asset attribution and review rights before reuse. | Preserved upstream reference; not integrated |
| [Contents.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/targets/widget/Assets.xcassets/CadenceMark.imageset/Contents.json) | Structured Contents content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/tests/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/tests/)

Upstream verification scenarios/fixtures for tests. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [account.test.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/tests/account.test.ts) | Regression/scenario definitions for account.test; execution and test boundaries are recorded separately. | Preserved upstream reference; not integrated |
| [advanced.test.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/tests/advanced.test.ts) | Regression/scenario definitions for advanced.test; execution and test boundaries are recorded separately. | Preserved upstream reference; not integrated |
| [ai-offer.test.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/tests/ai-offer.test.ts) | Regression/scenario definitions for ai offer.test; execution and test boundaries are recorded separately. | Preserved upstream reference; not integrated |
| [app-check.test.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/tests/app-check.test.ts) | Regression/scenario definitions for app check.test; execution and test boundaries are recorded separately. | Preserved upstream reference; not integrated |
| [auth-errors.test.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/tests/auth-errors.test.ts) | Regression/scenario definitions for auth errors.test; execution and test boundaries are recorded separately. | Preserved upstream reference; not integrated |
| [content.test.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/tests/content.test.ts) | Regression/scenario definitions for content.test; execution and test boundaries are recorded separately. | Preserved upstream reference; not integrated |
| [engagement.test.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/tests/engagement.test.ts) | Regression/scenario definitions for engagement.test; execution and test boundaries are recorded separately. | Preserved upstream reference; not integrated |
| [errors.test.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/tests/errors.test.ts) | Regression/scenario definitions for errors.test; execution and test boundaries are recorded separately. | Preserved upstream reference; not integrated |
| [firebase-env.test.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/tests/firebase-env.test.ts) | Regression/scenario definitions for firebase env.test; execution and test boundaries are recorded separately. | Preserved upstream reference; not integrated |
| [learning-state.test.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/tests/learning-state.test.ts) | Regression/scenario definitions for learning state.test; execution and test boundaries are recorded separately. | Preserved upstream reference; not integrated |
| [narration.test.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/tests/narration.test.ts) | Regression/scenario definitions for narration.test; execution and test boundaries are recorded separately. | Preserved upstream reference; not integrated |
| [notifications.test.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/tests/notifications.test.ts) | Regression/scenario definitions for notifications.test; execution and test boundaries are recorded separately. | Preserved upstream reference; not integrated |
| [onboarding.test.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/tests/onboarding.test.ts) | Regression/scenario definitions for onboarding.test; execution and test boundaries are recorded separately. | Preserved upstream reference; not integrated |
| [profile.test.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/tests/profile.test.ts) | Regression/scenario definitions for profile.test; execution and test boundaries are recorded separately. | Preserved upstream reference; not integrated |
| [progress.test.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/tests/progress.test.ts) | Regression/scenario definitions for progress.test; execution and test boundaries are recorded separately. | Preserved upstream reference; not integrated |
| [progression.test.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/tests/progression.test.ts) | Regression/scenario definitions for progression.test; execution and test boundaries are recorded separately. | Preserved upstream reference; not integrated |
| [quiz.test.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/tests/quiz.test.ts) | Regression/scenario definitions for quiz.test; execution and test boundaries are recorded separately. | Preserved upstream reference; not integrated |
| [scoring.test.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/tests/scoring.test.ts) | Regression/scenario definitions for scoring.test; execution and test boundaries are recorded separately. | Preserved upstream reference; not integrated |
| [sound-coach.test.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/tests/sound-coach.test.ts) | Regression/scenario definitions for sound coach.test; execution and test boundaries are recorded separately. | Preserved upstream reference; not integrated |
| [take-machine.test.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/tests/take-machine.test.ts) | Regression/scenario definitions for take machine.test; execution and test boundaries are recorded separately. | Preserved upstream reference; not integrated |
| [text.test.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/tests/text.test.ts) | Regression/scenario definitions for text.test; execution and test boundaries are recorded separately. | Preserved upstream reference; not integrated |
| [widget.test.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/mobile/tests/widget.test.ts) | Regression/scenario definitions for widget.test; execution and test boundaries are recorded separately. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/public/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/public/)

Original public assets, models or packaging resources; retain associated notices. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [sw.js](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/public/sw.js) | sw implementation/helper module in the containing upstream reference component. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/public/email/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/public/email/)

Original email assets, models or packaging resources; retain associated notices. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [logo-dark.png](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/public/email/logo-dark.png) | logo dark visual/font/icon resource; preserve applicable asset attribution and review rights before reuse. | Preserved upstream reference; not integrated |
| [logo.png](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/public/email/logo.png) | logo visual/font/icon resource; preserve applicable asset attribution and review rights before reuse. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/public/favicon/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/public/favicon/)

Original favicon assets, models or packaging resources; retain associated notices. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [apple-touch-icon.png](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/public/favicon/apple-touch-icon.png) | apple touch icon visual/font/icon resource; preserve applicable asset attribution and review rights before reuse. | Preserved upstream reference; not integrated |
| [favicon-96x96.png](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/public/favicon/favicon-96x96.png) | favicon 96x96 visual/font/icon resource; preserve applicable asset attribution and review rights before reuse. | Preserved upstream reference; not integrated |
| [favicon.ico](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/public/favicon/favicon.ico) | favicon visual/font/icon resource; preserve applicable asset attribution and review rights before reuse. | Preserved upstream reference; not integrated |
| [favicon.svg](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/public/favicon/favicon.svg) | favicon visual/font/icon resource; preserve applicable asset attribution and review rights before reuse. | Preserved upstream reference; not integrated |
| [site.webmanifest](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/public/favicon/site.webmanifest) | site presentation/page/browser-install resource for the containing component. | Preserved upstream reference; not integrated |
| [web-app-manifest-192x192.png](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/public/favicon/web-app-manifest-192x192.png) | web app manifest 192x192 visual/font/icon resource; preserve applicable asset attribution and review rights before reuse. | Preserved upstream reference; not integrated |
| [web-app-manifest-512x512.png](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/public/favicon/web-app-manifest-512x512.png) | web app manifest 512x512 visual/font/icon resource; preserve applicable asset attribution and review rights before reuse. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/public/icon/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/public/icon/)

Original icon assets, models or packaging resources; retain associated notices. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [apple.svg](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/public/icon/apple.svg) | apple visual/font/icon resource; preserve applicable asset attribution and review rights before reuse. | Preserved upstream reference; not integrated |
| [privacyoptions.svg](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/public/icon/privacyoptions.svg) | privacyoptions visual/font/icon resource; preserve applicable asset attribution and review rights before reuse. | Preserved upstream reference; not integrated |
| [windows.svg](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/public/icon/windows.svg) | windows visual/font/icon resource; preserve applicable asset attribution and review rights before reuse. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/public/illustration/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/public/illustration/)

Original illustration assets, models or packaging resources; retain associated notices. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [always-in-hurry-1.svg](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/public/illustration/always-in-hurry-1.svg) | always in hurry 1 visual/font/icon resource; preserve applicable asset attribution and review rights before reuse. | Preserved upstream reference; not integrated |
| [analysing-1.svg](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/public/illustration/analysing-1.svg) | analysing 1 visual/font/icon resource; preserve applicable asset attribution and review rights before reuse. | Preserved upstream reference; not integrated |
| [balancing-1.svg](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/public/illustration/balancing-1.svg) | balancing 1 visual/font/icon resource; preserve applicable asset attribution and review rights before reuse. | Preserved upstream reference; not integrated |
| [carrying-too-much-1.svg](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/public/illustration/carrying-too-much-1.svg) | carrying too much 1 visual/font/icon resource; preserve applicable asset attribution and review rights before reuse. | Preserved upstream reference; not integrated |
| [communication-1.svg](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/public/illustration/communication-1.svg) | communication 1 visual/font/icon resource; preserve applicable asset attribution and review rights before reuse. | Preserved upstream reference; not integrated |
| [daily-activity-1.svg](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/public/illustration/daily-activity-1.svg) | daily activity 1 visual/font/icon resource; preserve applicable asset attribution and review rights before reuse. | Preserved upstream reference; not integrated |
| [figuring-it-out-1.svg](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/public/illustration/figuring-it-out-1.svg) | figuring it out 1 visual/font/icon resource; preserve applicable asset attribution and review rights before reuse. | Preserved upstream reference; not integrated |
| [following-your-dreams-1.svg](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/public/illustration/following-your-dreams-1.svg) | following your dreams 1 visual/font/icon resource; preserve applicable asset attribution and review rights before reuse. | Preserved upstream reference; not integrated |
| [getting-help-1.svg](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/public/illustration/getting-help-1.svg) | getting help 1 visual/font/icon resource; preserve applicable asset attribution and review rights before reuse. | Preserved upstream reference; not integrated |
| [navigating--1.svg](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/public/illustration/navigating--1.svg) | navigating 1 visual/font/icon resource; preserve applicable asset attribution and review rights before reuse. | Preserved upstream reference; not integrated |
| [overcome-problems-1.svg](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/public/illustration/overcome-problems-1.svg) | overcome problems 1 visual/font/icon resource; preserve applicable asset attribution and review rights before reuse. | Preserved upstream reference; not integrated |
| [overloaded-1.svg](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/public/illustration/overloaded-1.svg) | overloaded 1 visual/font/icon resource; preserve applicable asset attribution and review rights before reuse. | Preserved upstream reference; not integrated |
| [progress-1.svg](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/public/illustration/progress-1.svg) | progress 1 visual/font/icon resource; preserve applicable asset attribution and review rights before reuse. | Preserved upstream reference; not integrated |
| [success-1.svg](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/public/illustration/success-1.svg) | success 1 visual/font/icon resource; preserve applicable asset attribution and review rights before reuse. | Preserved upstream reference; not integrated |
| [tired-1.svg](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/public/illustration/tired-1.svg) | tired 1 visual/font/icon resource; preserve applicable asset attribution and review rights before reuse. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/public/logo/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/public/logo/)

Original logo assets, models or packaging resources; retain associated notices. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [icon-dark.svg](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/public/logo/icon-dark.svg) | icon dark visual/font/icon resource; preserve applicable asset attribution and review rights before reuse. | Preserved upstream reference; not integrated |
| [icon-green-dark.svg](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/public/logo/icon-green-dark.svg) | icon green dark visual/font/icon resource; preserve applicable asset attribution and review rights before reuse. | Preserved upstream reference; not integrated |
| [icon-green-white.svg](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/public/logo/icon-green-white.svg) | icon green white visual/font/icon resource; preserve applicable asset attribution and review rights before reuse. | Preserved upstream reference; not integrated |
| [icon-white.svg](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/public/logo/icon-white.svg) | icon white visual/font/icon resource; preserve applicable asset attribution and review rights before reuse. | Preserved upstream reference; not integrated |
| [logo-dark.svg](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/public/logo/logo-dark.svg) | logo dark visual/font/icon resource; preserve applicable asset attribution and review rights before reuse. | Preserved upstream reference; not integrated |
| [logo-green-dark.svg](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/public/logo/logo-green-dark.svg) | logo green dark visual/font/icon resource; preserve applicable asset attribution and review rights before reuse. | Preserved upstream reference; not integrated |
| [logo-green-white.svg](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/public/logo/logo-green-white.svg) | logo green white visual/font/icon resource; preserve applicable asset attribution and review rights before reuse. | Preserved upstream reference; not integrated |
| [logo-white.svg](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/public/logo/logo-white.svg) | logo white visual/font/icon resource; preserve applicable asset attribution and review rights before reuse. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/public/packs/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/public/packs/)

Upstream authored packs content, pack data or fixtures; content rights/quality need separate review. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [index.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/public/packs/index.json) | Structured index content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/public/packs/core-a1/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/public/packs/core-a1/)

Upstream authored core a1 content, pack data or fixtures; content rights/quality need separate review. Archived reference; not an active Eng Teacher feature or dependency.

Contains the subfolders listed in their own sections; no tracked files directly in this folder.

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/public/packs/core-a1/v1/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/public/packs/core-a1/v1/)

Upstream authored v1 content, pack data or fixtures; content rights/quality need separate review. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [content.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/public/packs/core-a1/v1/content.json) | Structured content content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [manifest.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/public/packs/core-a1/v1/manifest.json) | Structured manifest content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [sentences.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/public/packs/core-a1/v1/sentences.json) | Structured sentences content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/public/packs/core-a2/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/public/packs/core-a2/)

Upstream authored core a2 content, pack data or fixtures; content rights/quality need separate review. Archived reference; not an active Eng Teacher feature or dependency.

Contains the subfolders listed in their own sections; no tracked files directly in this folder.

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/public/packs/core-a2/v1/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/public/packs/core-a2/v1/)

Upstream authored v1 content, pack data or fixtures; content rights/quality need separate review. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [content.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/public/packs/core-a2/v1/content.json) | Structured content content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [manifest.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/public/packs/core-a2/v1/manifest.json) | Structured manifest content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [scenarios.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/public/packs/core-a2/v1/scenarios.json) | Structured scenarios content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [sentences.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/public/packs/core-a2/v1/sentences.json) | Structured sentences content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/public/packs/core-a2/v2/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/public/packs/core-a2/v2/)

Upstream authored v2 content, pack data or fixtures; content rights/quality need separate review. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [content.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/public/packs/core-a2/v2/content.json) | Structured content content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [manifest.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/public/packs/core-a2/v2/manifest.json) | Structured manifest content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [scenarios.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/public/packs/core-a2/v2/scenarios.json) | Structured scenarios content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [sentences.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/public/packs/core-a2/v2/sentences.json) | Structured sentences content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/public/packs/core-b1/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/public/packs/core-b1/)

Upstream authored core b1 content, pack data or fixtures; content rights/quality need separate review. Archived reference; not an active Eng Teacher feature or dependency.

Contains the subfolders listed in their own sections; no tracked files directly in this folder.

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/public/packs/core-b1/v1/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/public/packs/core-b1/v1/)

Upstream authored v1 content, pack data or fixtures; content rights/quality need separate review. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [content.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/public/packs/core-b1/v1/content.json) | Structured content content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [manifest.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/public/packs/core-b1/v1/manifest.json) | Structured manifest content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [scenarios.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/public/packs/core-b1/v1/scenarios.json) | Structured scenarios content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [sentences.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/public/packs/core-b1/v1/sentences.json) | Structured sentences content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/public/packs/core-b1/v2/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/public/packs/core-b1/v2/)

Upstream authored v2 content, pack data or fixtures; content rights/quality need separate review. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [content.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/public/packs/core-b1/v2/content.json) | Structured content content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [manifest.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/public/packs/core-b1/v2/manifest.json) | Structured manifest content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [scenarios.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/public/packs/core-b1/v2/scenarios.json) | Structured scenarios content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [sentences.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/public/packs/core-b1/v2/sentences.json) | Structured sentences content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/public/packs/core-b2/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/public/packs/core-b2/)

Upstream authored core b2 content, pack data or fixtures; content rights/quality need separate review. Archived reference; not an active Eng Teacher feature or dependency.

Contains the subfolders listed in their own sections; no tracked files directly in this folder.

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/public/packs/core-b2/v1/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/public/packs/core-b2/v1/)

Upstream authored v1 content, pack data or fixtures; content rights/quality need separate review. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [content.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/public/packs/core-b2/v1/content.json) | Structured content content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [manifest.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/public/packs/core-b2/v1/manifest.json) | Structured manifest content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [scenarios.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/public/packs/core-b2/v1/scenarios.json) | Structured scenarios content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [sentences.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/public/packs/core-b2/v1/sentences.json) | Structured sentences content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/public/packs/core-b2/v2/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/public/packs/core-b2/v2/)

Upstream authored v2 content, pack data or fixtures; content rights/quality need separate review. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [content.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/public/packs/core-b2/v2/content.json) | Structured content content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [manifest.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/public/packs/core-b2/v2/manifest.json) | Structured manifest content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [scenarios.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/public/packs/core-b2/v2/scenarios.json) | Structured scenarios content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [sentences.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/public/packs/core-b2/v2/sentences.json) | Structured sentences content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/public/packs/core-c1/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/public/packs/core-c1/)

Upstream authored core c1 content, pack data or fixtures; content rights/quality need separate review. Archived reference; not an active Eng Teacher feature or dependency.

Contains the subfolders listed in their own sections; no tracked files directly in this folder.

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/public/packs/core-c1/v1/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/public/packs/core-c1/v1/)

Upstream authored v1 content, pack data or fixtures; content rights/quality need separate review. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [content.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/public/packs/core-c1/v1/content.json) | Structured content content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [manifest.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/public/packs/core-c1/v1/manifest.json) | Structured manifest content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [scenarios.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/public/packs/core-c1/v1/scenarios.json) | Structured scenarios content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [sentences.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/public/packs/core-c1/v1/sentences.json) | Structured sentences content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/public/packs/core-c1/v2/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/public/packs/core-c1/v2/)

Upstream authored v2 content, pack data or fixtures; content rights/quality need separate review. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [content.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/public/packs/core-c1/v2/content.json) | Structured content content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [manifest.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/public/packs/core-c1/v2/manifest.json) | Structured manifest content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [scenarios.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/public/packs/core-c1/v2/scenarios.json) | Structured scenarios content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [sentences.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/public/packs/core-c1/v2/sentences.json) | Structured sentences content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/public/packs/core-c2/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/public/packs/core-c2/)

Upstream authored core c2 content, pack data or fixtures; content rights/quality need separate review. Archived reference; not an active Eng Teacher feature or dependency.

Contains the subfolders listed in their own sections; no tracked files directly in this folder.

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/public/packs/core-c2/v1/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/public/packs/core-c2/v1/)

Upstream authored v1 content, pack data or fixtures; content rights/quality need separate review. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [content.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/public/packs/core-c2/v1/content.json) | Structured content content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [manifest.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/public/packs/core-c2/v1/manifest.json) | Structured manifest content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [sentences.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/public/packs/core-c2/v1/sentences.json) | Structured sentences content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/public/packs/core-c2/v2/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/public/packs/core-c2/v2/)

Upstream authored v2 content, pack data or fixtures; content rights/quality need separate review. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [content.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/public/packs/core-c2/v2/content.json) | Structured content content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [manifest.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/public/packs/core-c2/v2/manifest.json) | Structured manifest content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [sentences.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/public/packs/core-c2/v2/sentences.json) | Structured sentences content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/public/packs/fossilization/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/public/packs/fossilization/)

Upstream authored fossilization content, pack data or fixtures; content rights/quality need separate review. Archived reference; not an active Eng Teacher feature or dependency.

Contains the subfolders listed in their own sections; no tracked files directly in this folder.

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/public/packs/fossilization/v1/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/public/packs/fossilization/v1/)

Upstream authored v1 content, pack data or fixtures; content rights/quality need separate review. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [content.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/public/packs/fossilization/v1/content.json) | Structured content content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [manifest.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/public/packs/fossilization/v1/manifest.json) | Structured manifest content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/public/packs/phrases-b2/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/public/packs/phrases-b2/)

Upstream authored phrases b2 content, pack data or fixtures; content rights/quality need separate review. Archived reference; not an active Eng Teacher feature or dependency.

Contains the subfolders listed in their own sections; no tracked files directly in this folder.

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/public/packs/phrases-b2/v1/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/public/packs/phrases-b2/v1/)

Upstream authored v1 content, pack data or fixtures; content rights/quality need separate review. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [content.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/public/packs/phrases-b2/v1/content.json) | Structured content content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [manifest.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/public/packs/phrases-b2/v1/manifest.json) | Structured manifest content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/public/packs/phrases-c1/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/public/packs/phrases-c1/)

Upstream authored phrases c1 content, pack data or fixtures; content rights/quality need separate review. Archived reference; not an active Eng Teacher feature or dependency.

Contains the subfolders listed in their own sections; no tracked files directly in this folder.

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/public/packs/phrases-c1/v1/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/public/packs/phrases-c1/v1/)

Upstream authored v1 content, pack data or fixtures; content rights/quality need separate review. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [content.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/public/packs/phrases-c1/v1/content.json) | Structured content content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [manifest.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/public/packs/phrases-c1/v1/manifest.json) | Structured manifest content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/public/packs/phrases-c2/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/public/packs/phrases-c2/)

Upstream authored phrases c2 content, pack data or fixtures; content rights/quality need separate review. Archived reference; not an active Eng Teacher feature or dependency.

Contains the subfolders listed in their own sections; no tracked files directly in this folder.

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/public/packs/phrases-c2/v1/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/public/packs/phrases-c2/v1/)

Upstream authored v1 content, pack data or fixtures; content rights/quality need separate review. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [content.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/public/packs/phrases-c2/v1/content.json) | Structured content content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [manifest.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/public/packs/phrases-c2/v1/manifest.json) | Structured manifest content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/public/packs/placement/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/public/packs/placement/)

Upstream authored placement content, pack data or fixtures; content rights/quality need separate review. Archived reference; not an active Eng Teacher feature or dependency.

Contains the subfolders listed in their own sections; no tracked files directly in this folder.

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/public/packs/placement/v1/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/public/packs/placement/v1/)

Upstream authored v1 content, pack data or fixtures; content rights/quality need separate review. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [content.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/public/packs/placement/v1/content.json) | Structured content content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [manifest.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/public/packs/placement/v1/manifest.json) | Structured manifest content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/public/packs/slang/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/public/packs/slang/)

Upstream authored slang content, pack data or fixtures; content rights/quality need separate review. Archived reference; not an active Eng Teacher feature or dependency.

Contains the subfolders listed in their own sections; no tracked files directly in this folder.

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/public/packs/slang/v1/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/public/packs/slang/v1/)

Upstream authored v1 content, pack data or fixtures; content rights/quality need separate review. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [content.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/public/packs/slang/v1/content.json) | Structured content content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [manifest.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/public/packs/slang/v1/manifest.json) | Structured manifest content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/public/packs/slang/v2/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/public/packs/slang/v2/)

Upstream authored v2 content, pack data or fixtures; content rights/quality need separate review. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [content.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/public/packs/slang/v2/content.json) | Structured content content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [manifest.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/public/packs/slang/v2/manifest.json) | Structured manifest content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/public/packs/sounds/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/public/packs/sounds/)

Upstream authored sounds content, pack data or fixtures; content rights/quality need separate review. Archived reference; not an active Eng Teacher feature or dependency.

Contains the subfolders listed in their own sections; no tracked files directly in this folder.

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/public/packs/sounds/v1/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/public/packs/sounds/v1/)

Upstream authored v1 content, pack data or fixtures; content rights/quality need separate review. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [articulation.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/public/packs/sounds/v1/articulation.json) | Structured articulation content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [content.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/public/packs/sounds/v1/content.json) | Structured content content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [manifest.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/public/packs/sounds/v1/manifest.json) | Structured manifest content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/public/sound/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/public/sound/)

Original sound assets, models or packaging resources; retain associated notices. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [complete.wav](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/public/sound/complete.wav) | complete audio/media resource for the original component; rights and appropriate consent require separate review before reuse. | Preserved upstream reference; not integrated |
| [correct.wav](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/public/sound/correct.wav) | correct audio/media resource for the original component; rights and appropriate consent require separate review before reuse. | Preserved upstream reference; not integrated |
| [incorrect.wav](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/public/sound/incorrect.wav) | incorrect audio/media resource for the original component; rights and appropriate consent require separate review before reuse. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/release/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/release/)

Original upstream release source/configuration collection. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [manifest.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/release/manifest.json) | Structured manifest content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/scripts/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/scripts/)

Original upstream scripts maintenance/build utilities; not normal Eng Teacher setup commands. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [dev-all.mjs](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/scripts/dev-all.mjs) | dev all module; static declarations include isPortAvailable, prefixedSpawn, printLines, log, clearElectronUserDataPreservingModels, trackChild. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [dev.mjs](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/scripts/dev.mjs) | dev module; static declarations include isPortAvailable. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [serve.mjs](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/scripts/serve.mjs) | serve module; static declarations include say, readFlag, findLanAddress, probe, waitForServer, run. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [vercel-ignore-command.mjs](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/scripts/vercel-ignore-command.mjs) | vercel ignore command module; static declarations include runGit. No behavior is executed by this guide. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/scripts/bench/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/scripts/bench/)

Original upstream bench maintenance/build utilities; not normal Eng Teacher setup commands. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [transcribe.mjs](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/scripts/bench/transcribe.mjs) | transcribe module; static declarations include geminiKey, clips, words, edits, runGemini, runWhisper. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [whisper_cpu.py](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/scripts/bench/whisper_cpu.py) | whisper cpu module; static declarations include main. No behavior is executed by this guide. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/scripts/budgets/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/scripts/budgets/)

Original upstream budgets maintenance/build utilities; not normal Eng Teacher setup commands. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [web.mjs](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/scripts/budgets/web.mjs) | web module; static declarations include gzipKb, measure, main. No behavior is executed by this guide. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/scripts/content/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/scripts/content/)

Upstream authored content content, pack data or fixtures; content rights/quality need separate review. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [.gitignore](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/scripts/content/.gitignore) | Original component exclusions for generated outputs, dependencies and local configuration. | Preserved upstream reference; not integrated |
| [README.md](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/scripts/content/README.md) | Containing collection/component introduction, navigation and documented usage; retain the scope of the original project. | Preserved upstream reference; not integrated |
| [audio.mjs](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/scripts/content/audio.mjs) | audio implementation/helper module in the containing upstream reference component. | Preserved upstream reference; not integrated |
| [build.mjs](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/scripts/content/build.mjs) | build module; static declarations include audioRefs. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [check.mjs](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/scripts/content/check.mjs) | check module; static declarations include passing, jobFor, topUp. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [examples.mjs](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/scripts/content/examples.mjs) | examples implementation/helper module in the containing upstream reference component. | Preserved upstream reference; not integrated |
| [fit-articulation.mjs](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/scripts/content/fit-articulation.mjs) | fit articulation module; static declarations include commonsInfo, fetchDrawings, rmsOf, fitDrawing, vowelFeatures, base. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [fossilization.mjs](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/scripts/content/fossilization.mjs) | fossilization module; static declarations include prompt, build. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [generate.mjs](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/scripts/content/generate.mjs) | generate implementation/helper module in the containing upstream reference component. | Preserved upstream reference; not integrated |
| [phrases.mjs](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/scripts/content/phrases.mjs) | phrases module; static declarations include prompt, distractorsFor, cleanItem, draftProblem, draft, check. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [placement.mjs](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/scripts/content/placement.mjs) | placement module; static declarations include error, typeBrief, toExercise, itemProblems, rateLevels, the. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [slang.mjs](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/scripts/content/slang.mjs) | slang module; static declarations include prompt, registerCheck, cleanEntry, entryProblem, distractors, draft. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [tatoeba.mjs](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/scripts/content/tatoeba.mjs) | tatoeba module; static declarations include freq, sentences. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [validate-articulation.mjs](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/scripts/content/validate-articulation.mjs) | validate articulation implementation/helper module in the containing upstream reference component. | Preserved upstream reference; not integrated |
| [validate.mjs](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/scripts/content/validate.mjs) | validate implementation/helper module in the containing upstream reference component. | Preserved upstream reference; not integrated |
| [vocab.mjs](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/scripts/content/vocab.mjs) | vocab module; static declarations include chunk. No behavior is executed by this guide. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/scripts/content/data/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/scripts/content/data/)

Upstream authored data content, pack data or fixtures; content rights/quality need separate review. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [fossilization-plan.mjs](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/scripts/content/data/fossilization-plan.mjs) | fossilization plan module; static declarations include words. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [grammar-outline.mjs](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/scripts/content/data/grammar-outline.mjs) | grammar outline implementation/helper module in the containing upstream reference component. | Preserved upstream reference; not integrated |
| [phrase-plan.mjs](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/scripts/content/data/phrase-plan.mjs) | phrase plan implementation/helper module in the containing upstream reference component. | Preserved upstream reference; not integrated |
| [placement-plan.mjs](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/scripts/content/data/placement-plan.mjs) | placement plan module; static declarations include grammarFocus, vocabularyFocus, readingFocus. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [sound-plan.mjs](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/scripts/content/data/sound-plan.mjs) | sound plan implementation/helper module in the containing upstream reference component. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/scripts/content/lib/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/scripts/content/lib/)

Upstream authored lib content, pack data or fixtures; content rights/quality need separate review. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [advanced.mjs](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/scripts/content/lib/advanced.mjs) | advanced module; static declarations include loadPhrases, loadSlang, loadFossilization, advancedPacks. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [articulation-check.mjs](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/scripts/content/lib/articulation-check.mjs) | articulation check module; static declarations include loadTargets, soundIdForIpa, splitIpa, coverageProblems, fitProblems. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [articulation-trace.mjs](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/scripts/content/lib/articulation-trace.mjs) | articulation trace module; static declarations include bounds, parts, landmarks, calibrate, of, gridLine. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [assemble.mjs](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/scripts/content/lib/assemble.mjs) | assemble module; static declarations include loadGrammar, passingExercises, loadVocab, loadSentences, relatedFor, corePack. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [blind-check.mjs](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/scripts/content/lib/blind-check.mjs) | blind check module; static declarations include answerBlind, judge, widenKey, checkSet. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [blind.mjs](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/scripts/content/lib/blind.mjs) | blind module; static declarations include seededOrder, shuffleFor, rightOrder, tokenOrder, blindView, fromBlindAnswer. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [gemini.mjs](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/scripts/content/lib/gemini.mjs) | gemini module; static declarations include apiKey, generateJson, pool. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [grammar-gen.mjs](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/scripts/content/lib/grammar-gen.mjs) | grammar gen module; static declarations include grammarPrompt, toContent. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [lexicon.mjs](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/scripts/content/lib/lexicon.mjs) | lexicon module; static declarations include loadLexicon, levelForRank, estimateLevel. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [paths.mjs](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/scripts/content/lib/paths.mjs) | paths implementation/helper module in the containing upstream reference component. | Preserved upstream reference; not integrated |
| [placement-bank.mjs](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/scripts/content/lib/placement-bank.mjs) | placement bank module; static declarations include ratingFits, passingItems, loadPlacementBanks. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [repair.mjs](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/scripts/content/lib/repair.mjs) | repair module; static declarations include repairExercise, fitSummary. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [slang-exclusions.mjs](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/scripts/content/lib/slang-exclusions.mjs) | slang exclusions implementation/helper module in the containing upstream reference component. | Preserved upstream reference; not integrated |
| [svg-path.mjs](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/scripts/content/lib/svg-path.mjs) | svg path module; static declarations include tokenize, cubic, pathToPolylines, pathsById. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [tatoeba.mjs](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/scripts/content/lib/tatoeba.mjs) | tatoeba module; static declarations include download, ensureExport, readSentences, readNativeSpeakers, isCleanSentence, cleanSentences. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [text.mjs](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/scripts/content/lib/text.mjs) | text module; static declarations include slugify, wordsOf, profanityIn, sha256Hex, textKey, isSensitive. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [validators.mjs](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/scripts/content/lib/validators.mjs) | validators module; static declarations include keyAnswer, textsOf, exerciseKey, packProblems, corpusProblems, tatoebaProblems. No behavior is executed by this guide. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/scripts/email/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/scripts/email/)

Original upstream email maintenance/build utilities; not normal Eng Teacher setup commands. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [assets.mjs](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/scripts/email/assets.mjs) | assets implementation/helper module in the containing upstream reference component. | Preserved upstream reference; not integrated |
| [brevo-doi-template.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/scripts/email/brevo-doi-template.ts) | brevo doi template implementation/helper module in the containing upstream reference component. | Preserved upstream reference; not integrated |
| [lint.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/scripts/email/lint.ts) | lint implementation/helper module in the containing upstream reference component. | Preserved upstream reference; not integrated |
| [package.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/scripts/email/package.json) | Containing component dependency/build/test declarations; consult its scope before installing. | Preserved upstream reference; not integrated |
| [preview.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/scripts/email/preview.ts) | preview module; static declarations include html. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [send-test.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/scripts/email/send-test.ts) | send test implementation/helper module in the containing upstream reference component. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/scripts/platform/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/scripts/platform/)

Original upstream platform maintenance/build utilities; not normal Eng Teacher setup commands. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [sync-mobile.mjs](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/scripts/platform/sync-mobile.mjs) | sync mobile module; static declarations include listTs, mobileVersion. No behavior is executed by this guide. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/scripts/release/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/scripts/release/)

Original upstream release maintenance/build utilities; not normal Eng Teacher setup commands. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [bump.mjs](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/scripts/release/bump.mjs) | bump module; static declarations include parseArgs, usage. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [lib.mjs](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/scripts/release/lib.mjs) | lib module; static declarations include parseSemver, compareSemver, bumpSemver, tagFor, unreleasedHeading, splitSections. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [notes.mjs](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/scripts/release/notes.mjs) | notes implementation/helper module in the containing upstream reference component. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/scripts/screenshots/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/scripts/screenshots/)

Original screenshots assets, models or packaging resources; retain associated notices. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [capture.mjs](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/scripts/screenshots/capture.mjs) | capture module; static declarations include bootedProMax, flow, shot. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [cleanup-demo.mts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/scripts/screenshots/cleanup-demo.mts) | cleanup demo implementation/helper module in the containing upstream reference component. | Preserved upstream reference; not integrated |
| [demo-accounts.mts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/scripts/screenshots/demo-accounts.mts) | demo accounts implementation/helper module in the containing upstream reference component. | Preserved upstream reference; not integrated |
| [stage-demo.mts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/scripts/screenshots/stage-demo.mts) | stage demo implementation/helper module in the containing upstream reference component. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/scripts/vocal-tract/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/scripts/vocal-tract/)

Original upstream vocal tract maintenance/build utilities; not normal Eng Teacher setup commands. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [make-reference.mjs](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/scripts/vocal-tract/make-reference.mjs) | make reference implementation/helper module in the containing upstream reference component. | Preserved upstream reference; not integrated |
| [reference.tex](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/scripts/vocal-tract/reference.tex) | Documentation/research record for reference; requirements and historical observations are not automatically implemented behavior. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/scripts/webhooks/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/scripts/webhooks/)

Original upstream webhooks maintenance/build utilities; not normal Eng Teacher setup commands. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [package.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/scripts/webhooks/package.json) | Containing component dependency/build/test declarations; consult its scope before installing. | Preserved upstream reference; not integrated |
| [replay-revenuecat.mjs](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/scripts/webhooks/replay-revenuecat.mjs) | replay revenuecat module; static declarations include send. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [replay-stripe.mjs](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/scripts/webhooks/replay-stripe.mjs) | replay stripe module; static declarations include send. No behavior is executed by this guide. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/scripts/webhooks/fixtures/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/scripts/webhooks/fixtures/)

Upstream verification scenarios/fixtures for fixtures. Archived reference; not an active Eng Teacher feature or dependency.

Contains the subfolders listed in their own sections; no tracked files directly in this folder.

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/scripts/webhooks/fixtures/revenuecat/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/scripts/webhooks/fixtures/revenuecat/)

Upstream verification scenarios/fixtures for revenuecat. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [01-INITIAL_PURCHASE.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/scripts/webhooks/fixtures/revenuecat/01-INITIAL_PURCHASE.json) | Structured 01 INITIAL PURCHASE content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [02-RENEWAL.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/scripts/webhooks/fixtures/revenuecat/02-RENEWAL.json) | Structured 02 RENEWAL content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [03-PRODUCT_CHANGE.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/scripts/webhooks/fixtures/revenuecat/03-PRODUCT_CHANGE.json) | Structured 03 PRODUCT CHANGE content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [04-BILLING_ISSUE.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/scripts/webhooks/fixtures/revenuecat/04-BILLING_ISSUE.json) | Structured 04 BILLING ISSUE content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [05-CANCELLATION.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/scripts/webhooks/fixtures/revenuecat/05-CANCELLATION.json) | Structured 05 CANCELLATION content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [06-UNCANCELLATION.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/scripts/webhooks/fixtures/revenuecat/06-UNCANCELLATION.json) | Structured 06 UNCANCELLATION content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [07-SUBSCRIPTION_PAUSED.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/scripts/webhooks/fixtures/revenuecat/07-SUBSCRIPTION_PAUSED.json) | Structured 07 SUBSCRIPTION PAUSED content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [08-TRANSFER.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/scripts/webhooks/fixtures/revenuecat/08-TRANSFER.json) | Structured 08 TRANSFER content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [09-EXPIRATION.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/scripts/webhooks/fixtures/revenuecat/09-EXPIRATION.json) | Structured 09 EXPIRATION content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [10-TEST.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/scripts/webhooks/fixtures/revenuecat/10-TEST.json) | Structured 10 TEST content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/scripts/webhooks/fixtures/stripe/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/scripts/webhooks/fixtures/stripe/)

Upstream verification scenarios/fixtures for stripe. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [01-checkout.session.completed.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/scripts/webhooks/fixtures/stripe/01-checkout.session.completed.json) | Structured 01 checkout.session.completed content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [02-customer.subscription.updated.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/scripts/webhooks/fixtures/stripe/02-customer.subscription.updated.json) | Structured 02 customer.subscription.updated content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [03-invoice.payment_failed.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/scripts/webhooks/fixtures/stripe/03-invoice.payment_failed.json) | Structured 03 invoice.payment failed content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [04-customer.subscription.deleted.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/scripts/webhooks/fixtures/stripe/04-customer.subscription.deleted.json) | Structured 04 customer.subscription.deleted content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/)

Original upstream src source/configuration collection. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [proxy.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/proxy.ts) | proxy module; static declarations include NextRequest, proxy. No behavior is executed by this guide. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/)

Original upstream web route group/page area for app. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [favicon.svg](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/favicon.svg) | favicon visual/font/icon resource; preserve applicable asset attribution and review rights before reuse. | Preserved upstream reference; not integrated |
| [globals.css](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/globals.css) | globals presentation/page/browser-install resource for the containing component. | Preserved upstream reference; not integrated |
| [layout.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/layout.tsx) | Upstream framework layout entrypoint for app. | Preserved upstream reference; not integrated |
| [robots.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/robots.ts) | robots module; static declarations include robots. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [sitemap.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/sitemap.ts) | sitemap module; static declarations include sitemap. No behavior is executed by this guide. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/(auth)/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/%28auth%29/)

Original upstream web route group/page area for (auth). Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [layout.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/%28auth%29/layout.tsx) | Upstream framework layout entrypoint for (auth). | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/(auth)/forgot-password/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/%28auth%29/forgot-password/)

Original upstream web route group/page area for forgot password. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [page.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/%28auth%29/forgot-password/page.tsx) | Upstream framework page entrypoint for forgot password. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/(auth)/login/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/%28auth%29/login/)

Original upstream web route group/page area for login. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [page.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/%28auth%29/login/page.tsx) | Upstream framework page entrypoint for login. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/(auth)/reset-password/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/%28auth%29/reset-password/)

Original upstream web route group/page area for reset password. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [page.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/%28auth%29/reset-password/page.tsx) | Upstream framework page entrypoint for reset password. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/(auth)/signup/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/%28auth%29/signup/)

Original upstream web route group/page area for signup. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [page.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/%28auth%29/signup/page.tsx) | Upstream framework page entrypoint for signup. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/(auth)/verify-email/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/%28auth%29/verify-email/)

Original upstream web route group/page area for verify email. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [page.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/%28auth%29/verify-email/page.tsx) | Upstream framework page entrypoint for verify email. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/(dashboard)/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/%28dashboard%29/)

Original upstream web route group/page area for (dashboard). Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [layout.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/%28dashboard%29/layout.tsx) | Upstream framework layout entrypoint for (dashboard). | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/(dashboard)/account/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/%28dashboard%29/account/)

Original upstream web route group/page area for account. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [page.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/%28dashboard%29/account/page.tsx) | Upstream framework page entrypoint for account. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/(dashboard)/account/connections/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/%28dashboard%29/account/connections/)

Original upstream web route group/page area for connections. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [page.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/%28dashboard%29/account/connections/page.tsx) | Upstream framework page entrypoint for connections. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/(dashboard)/account/level/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/%28dashboard%29/account/level/)

Original upstream web route group/page area for level. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [page.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/%28dashboard%29/account/level/page.tsx) | Upstream framework page entrypoint for level. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/(dashboard)/account/level/placement/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/%28dashboard%29/account/level/placement/)

Original upstream web route group/page area for placement. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [page.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/%28dashboard%29/account/level/placement/page.tsx) | Upstream framework page entrypoint for placement. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/(dashboard)/bookmarks/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/%28dashboard%29/bookmarks/)

Original upstream web route group/page area for bookmarks. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [page.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/%28dashboard%29/bookmarks/page.tsx) | Upstream framework page entrypoint for bookmarks. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/(dashboard)/checkout/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/%28dashboard%29/checkout/)

Original upstream web route group/page area for checkout. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [page.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/%28dashboard%29/checkout/page.tsx) | Upstream framework page entrypoint for checkout. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/(dashboard)/coach/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/%28dashboard%29/coach/)

Original upstream web route group/page area for coach. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [page.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/%28dashboard%29/coach/page.tsx) | Upstream framework page entrypoint for coach. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/(dashboard)/coach/history/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/%28dashboard%29/coach/history/)

Original upstream web route group/page area for history. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [page.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/%28dashboard%29/coach/history/page.tsx) | Upstream framework page entrypoint for history. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/(dashboard)/connect-phone/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/%28dashboard%29/connect-phone/)

Original upstream web route group/page area for connect phone. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [page.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/%28dashboard%29/connect-phone/page.tsx) | Upstream framework page entrypoint for connect phone. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/(dashboard)/conversation/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/%28dashboard%29/conversation/)

Original upstream web route group/page area for conversation. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [page.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/%28dashboard%29/conversation/page.tsx) | Upstream framework page entrypoint for conversation. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/(dashboard)/conversation/\[moduleSlug\]/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/%28dashboard%29/conversation/%5BmoduleSlug%5D/)

Original upstream web route group/page area for [module Slug]. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [page.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/%28dashboard%29/conversation/%5BmoduleSlug%5D/page.tsx) | Upstream framework page entrypoint for \[module Slug\]. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/(dashboard)/dashboard/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/%28dashboard%29/dashboard/)

Original upstream web route group/page area for dashboard. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [page.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/%28dashboard%29/dashboard/page.tsx) | Upstream framework page entrypoint for dashboard. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/(dashboard)/dictionary/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/%28dashboard%29/dictionary/)

Original upstream web route group/page area for dictionary. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [page.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/%28dashboard%29/dictionary/page.tsx) | Upstream framework page entrypoint for dictionary. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/(dashboard)/grammar/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/%28dashboard%29/grammar/)

Original upstream web route group/page area for grammar. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [page.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/%28dashboard%29/grammar/page.tsx) | Upstream framework page entrypoint for grammar. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/(dashboard)/grammar/\[pointId\]/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/%28dashboard%29/grammar/%5BpointId%5D/)

Original upstream web route group/page area for [point Id]. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [page.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/%28dashboard%29/grammar/%5BpointId%5D/page.tsx) | Upstream framework page entrypoint for \[point Id\]. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/(dashboard)/just-speak/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/%28dashboard%29/just-speak/)

Original upstream web route group/page area for just speak. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [page.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/%28dashboard%29/just-speak/page.tsx) | Upstream framework page entrypoint for just speak. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/(dashboard)/learn/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/%28dashboard%29/learn/)

Original upstream web route group/page area for learn. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [page.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/%28dashboard%29/learn/page.tsx) | Upstream framework page entrypoint for learn. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/(dashboard)/learn/\[moduleSlug\]/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/%28dashboard%29/learn/%5BmoduleSlug%5D/)

Original upstream web route group/page area for [module Slug]. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [page.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/%28dashboard%29/learn/%5BmoduleSlug%5D/page.tsx) | Upstream framework page entrypoint for \[module Slug\]. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/(dashboard)/learn/\[moduleSlug\]/\[lessonSlug\]/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/%28dashboard%29/learn/%5BmoduleSlug%5D/%5BlessonSlug%5D/)

Original upstream web route group/page area for [lesson Slug]. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [page.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/%28dashboard%29/learn/%5BmoduleSlug%5D/%5BlessonSlug%5D/page.tsx) | Upstream framework page entrypoint for \[lesson Slug\]. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/(dashboard)/onboarding/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/%28dashboard%29/onboarding/)

Original upstream web route group/page area for onboarding. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [page.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/%28dashboard%29/onboarding/page.tsx) | Upstream framework page entrypoint for onboarding. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/(dashboard)/phrases/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/%28dashboard%29/phrases/)

Original upstream web route group/page area for phrases. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [page.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/%28dashboard%29/phrases/page.tsx) | Upstream framework page entrypoint for phrases. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/(dashboard)/phrases/\[id\]/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/%28dashboard%29/phrases/%5Bid%5D/)

Original upstream web route group/page area for [id]. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [page.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/%28dashboard%29/phrases/%5Bid%5D/page.tsx) | Upstream framework page entrypoint for \[id\]. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/(dashboard)/phrases/practice/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/%28dashboard%29/phrases/practice/)

Original upstream web route group/page area for practice. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [page.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/%28dashboard%29/phrases/practice/page.tsx) | Upstream framework page entrypoint for practice. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/(dashboard)/plateau/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/%28dashboard%29/plateau/)

Original upstream web route group/page area for plateau. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [page.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/%28dashboard%29/plateau/page.tsx) | Upstream framework page entrypoint for plateau. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/(dashboard)/practice/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/%28dashboard%29/practice/)

Original upstream web route group/page area for practice. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [page.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/%28dashboard%29/practice/page.tsx) | Upstream framework page entrypoint for practice. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/(dashboard)/practice/\[mode\]/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/%28dashboard%29/practice/%5Bmode%5D/)

Original upstream web route group/page area for [mode]. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [page.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/%28dashboard%29/practice/%5Bmode%5D/page.tsx) | Upstream framework page entrypoint for \[mode\]. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/(dashboard)/profile/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/%28dashboard%29/profile/)

Original upstream web route group/page area for profile. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [page.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/%28dashboard%29/profile/page.tsx) | Upstream framework page entrypoint for profile. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/(dashboard)/recordings/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/%28dashboard%29/recordings/)

Original upstream web route group/page area for recordings. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [page.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/%28dashboard%29/recordings/page.tsx) | Upstream framework page entrypoint for recordings. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/(dashboard)/slang/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/%28dashboard%29/slang/)

Original upstream web route group/page area for slang. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [page.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/%28dashboard%29/slang/page.tsx) | Upstream framework page entrypoint for slang. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/(dashboard)/slang/\[id\]/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/%28dashboard%29/slang/%5Bid%5D/)

Original upstream web route group/page area for [id]. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [page.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/%28dashboard%29/slang/%5Bid%5D/page.tsx) | Upstream framework page entrypoint for \[id\]. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/(dashboard)/slang/quiz/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/%28dashboard%29/slang/quiz/)

Original upstream web route group/page area for quiz. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [page.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/%28dashboard%29/slang/quiz/page.tsx) | Upstream framework page entrypoint for quiz. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/(dashboard)/sound-library/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/%28dashboard%29/sound-library/)

Original upstream web route group/page area for sound library. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [page.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/%28dashboard%29/sound-library/page.tsx) | Upstream framework page entrypoint for sound library. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/(dashboard)/sounds/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/%28dashboard%29/sounds/)

Original sounds assets, models or packaging resources; retain associated notices. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [page.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/%28dashboard%29/sounds/page.tsx) | Upstream framework page entrypoint for sounds. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/(dashboard)/sounds/\[soundId\]/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/%28dashboard%29/sounds/%5BsoundId%5D/)

Original [sound Id] assets, models or packaging resources; retain associated notices. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [page.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/%28dashboard%29/sounds/%5BsoundId%5D/page.tsx) | Upstream framework page entrypoint for \[sound Id\]. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/(dashboard)/sounds/compare/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/%28dashboard%29/sounds/compare/)

Original compare assets, models or packaging resources; retain associated notices. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [page.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/%28dashboard%29/sounds/compare/page.tsx) | Upstream framework page entrypoint for compare. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/(dashboard)/today/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/%28dashboard%29/today/)

Original upstream web route group/page area for today. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [page.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/%28dashboard%29/today/page.tsx) | Upstream framework page entrypoint for today. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/(landing)/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/%28landing%29/)

Original upstream web route group/page area for (landing). Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [page.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/%28landing%29/page.tsx) | Upstream framework page entrypoint for (landing). | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/(landing)/connector/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/%28landing%29/connector/)

Original upstream web route group/page area for connector. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [page.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/%28landing%29/connector/page.tsx) | Upstream framework page entrypoint for connector. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/(landing)/contact/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/%28landing%29/contact/)

Original upstream web route group/page area for contact. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [page.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/%28landing%29/contact/page.tsx) | Upstream framework page entrypoint for contact. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/(landing)/credits/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/%28landing%29/credits/)

Original upstream web route group/page area for credits. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [page.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/%28landing%29/credits/page.tsx) | Upstream framework page entrypoint for credits. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/(landing)/download/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/%28landing%29/download/)

Original upstream web route group/page area for download. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [page.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/%28landing%29/download/page.tsx) | Upstream framework page entrypoint for download. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/(landing)/help/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/%28landing%29/help/)

Original upstream web route group/page area for help. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [page.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/%28landing%29/help/page.tsx) | Upstream framework page entrypoint for help. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/(landing)/newsletter/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/%28landing%29/newsletter/)

Original upstream web route group/page area for newsletter. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [page.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/%28landing%29/newsletter/page.tsx) | Upstream framework page entrypoint for newsletter. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/(landing)/newsletter/confirmed/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/%28landing%29/newsletter/confirmed/)

Original upstream web route group/page area for confirmed. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [page.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/%28landing%29/newsletter/confirmed/page.tsx) | Upstream framework page entrypoint for confirmed. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/(landing)/pricing/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/%28landing%29/pricing/)

Original upstream web route group/page area for pricing. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [page.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/%28landing%29/pricing/page.tsx) | Upstream framework page entrypoint for pricing. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/(landing)/privacy/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/%28landing%29/privacy/)

Original upstream web route group/page area for privacy. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [page.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/%28landing%29/privacy/page.tsx) | Upstream framework page entrypoint for privacy. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/(landing)/redeem/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/%28landing%29/redeem/)

Original upstream web route group/page area for redeem. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [page.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/%28landing%29/redeem/page.tsx) | Upstream framework page entrypoint for redeem. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/(landing)/support/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/%28landing%29/support/)

Original upstream web route group/page area for support. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [page.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/%28landing%29/support/page.tsx) | Upstream framework page entrypoint for support. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/(landing)/terms/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/%28landing%29/terms/)

Original upstream web route group/page area for terms. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [page.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/%28landing%29/terms/page.tsx) | Upstream framework page entrypoint for terms. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/.well-known/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/.well-known/)

Original upstream web route group/page area for .well known. Archived reference; not an active Eng Teacher feature or dependency.

Contains the subfolders listed in their own sections; no tracked files directly in this folder.

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/.well-known/oauth-authorization-server/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/.well-known/oauth-authorization-server/)

Original upstream web route group/page area for oauth authorization server. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [route.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/.well-known/oauth-authorization-server/route.ts) | Upstream HTTP route handler for oauth authorization server; not an active Eng Teacher endpoint. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/.well-known/oauth-protected-resource/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/.well-known/oauth-protected-resource/)

Original upstream web route group/page area for oauth protected resource. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [route.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/.well-known/oauth-protected-resource/route.ts) | Upstream HTTP route handler for oauth protected resource; not an active Eng Teacher endpoint. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/.well-known/oauth-protected-resource/api/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/.well-known/oauth-protected-resource/api/)

Original upstream HTTP/API route area for api. Archived reference; not an active Eng Teacher feature or dependency.

Contains the subfolders listed in their own sections; no tracked files directly in this folder.

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/.well-known/oauth-protected-resource/api/mcp/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/.well-known/oauth-protected-resource/api/mcp/)

Original upstream HTTP/API route area for mcp. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [route.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/.well-known/oauth-protected-resource/api/mcp/route.ts) | Upstream HTTP route handler for mcp; not an active Eng Teacher endpoint. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/)

Original upstream HTTP/API route area for api. Archived reference; not an active Eng Teacher feature or dependency.

Contains the subfolders listed in their own sections; no tracked files directly in this folder.

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/account/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/account/)

Original upstream HTTP/API route area for account. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [route.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/account/route.ts) | Upstream HTTP route handler for account; not an active Eng Teacher endpoint. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/account/connections/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/account/connections/)

Original upstream HTTP/API route area for connections. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [route.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/account/connections/route.ts) | Upstream HTTP route handler for connections; not an active Eng Teacher endpoint. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/account/email/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/account/email/)

Original upstream HTTP/API route area for email. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [route.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/account/email/route.ts) | Upstream HTTP route handler for email; not an active Eng Teacher endpoint. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/account/export/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/account/export/)

Original upstream HTTP/API route area for export. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [route.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/account/export/route.ts) | Upstream HTTP route handler for export; not an active Eng Teacher endpoint. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/admin/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/admin/)

Original upstream HTTP/API route area for admin. Archived reference; not an active Eng Teacher feature or dependency.

Contains the subfolders listed in their own sections; no tracked files directly in this folder.

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/admin/codes/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/admin/codes/)

Original upstream HTTP/API route area for codes. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [route.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/admin/codes/route.ts) | Upstream HTTP route handler for codes; not an active Eng Teacher endpoint. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/admin/support/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/admin/support/)

Original upstream HTTP/API route area for support. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [route.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/admin/support/route.ts) | Upstream HTTP route handler for support; not an active Eng Teacher endpoint. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/ai/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/ai/)

Original upstream HTTP/API route area for ai. Archived reference; not an active Eng Teacher feature or dependency.

Contains the subfolders listed in their own sections; no tracked files directly in this folder.

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/ai-coach/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/ai-coach/)

Original upstream HTTP/API route area for ai coach. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [route.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/ai-coach/route.ts) | Upstream HTTP route handler for ai coach; not an active Eng Teacher endpoint. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/ai/grammar-feedback/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/ai/grammar-feedback/)

Original upstream HTTP/API route area for grammar feedback. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [route.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/ai/grammar-feedback/route.ts) | Upstream HTTP route handler for grammar feedback; not an active Eng Teacher endpoint. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/ai/placement/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/ai/placement/)

Original upstream HTTP/API route area for placement. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [route.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/ai/placement/route.ts) | Upstream HTTP route handler for placement; not an active Eng Teacher endpoint. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/assess/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/assess/)

Original upstream HTTP/API route area for assess. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [route.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/assess/route.ts) | Upstream HTTP route handler for assess; not an active Eng Teacher endpoint. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/attempts/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/attempts/)

Original upstream HTTP/API route area for attempts. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [route.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/attempts/route.ts) | Upstream HTTP route handler for attempts; not an active Eng Teacher endpoint. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/auth/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/auth/)

Original upstream HTTP/API route area for auth. Archived reference; not an active Eng Teacher feature or dependency.

Contains the subfolders listed in their own sections; no tracked files directly in this folder.

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/auth/password-changed/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/auth/password-changed/)

Original upstream HTTP/API route area for password changed. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [route.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/auth/password-changed/route.ts) | Upstream HTTP route handler for password changed; not an active Eng Teacher endpoint. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/auth/password-reset/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/auth/password-reset/)

Original upstream HTTP/API route area for password reset. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [route.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/auth/password-reset/route.ts) | Upstream HTTP route handler for password reset; not an active Eng Teacher endpoint. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/auth/session/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/auth/session/)

Original upstream HTTP/API route area for session. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [route.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/auth/session/route.ts) | Upstream HTTP route handler for session; not an active Eng Teacher endpoint. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/auth/sign-in-failed/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/auth/sign-in-failed/)

Original upstream HTTP/API route area for sign in failed. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [route.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/auth/sign-in-failed/route.ts) | Upstream HTTP route handler for sign in failed; not an active Eng Teacher endpoint. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/auth/verify-email/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/auth/verify-email/)

Original upstream HTTP/API route area for verify email. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [route.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/auth/verify-email/route.ts) | Upstream HTTP route handler for verify email; not an active Eng Teacher endpoint. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/billing/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/billing/)

Original upstream HTTP/API route area for billing. Archived reference; not an active Eng Teacher feature or dependency.

Contains the subfolders listed in their own sections; no tracked files directly in this folder.

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/billing/checkout/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/billing/checkout/)

Original upstream HTTP/API route area for checkout. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [route.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/billing/checkout/route.ts) | Upstream HTTP route handler for checkout; not an active Eng Teacher endpoint. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/billing/portal/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/billing/portal/)

Original upstream HTTP/API route area for portal. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [route.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/billing/portal/route.ts) | Upstream HTTP route handler for portal; not an active Eng Teacher endpoint. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/codes/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/codes/)

Original upstream HTTP/API route area for codes. Archived reference; not an active Eng Teacher feature or dependency.

Contains the subfolders listed in their own sections; no tracked files directly in this folder.

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/codes/redeem/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/codes/redeem/)

Original upstream HTTP/API route area for redeem. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [route.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/codes/redeem/route.ts) | Upstream HTTP route handler for redeem; not an active Eng Teacher endpoint. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/conversation-progress/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/conversation-progress/)

Original upstream HTTP/API route area for conversation progress. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [route.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/conversation-progress/route.ts) | Upstream HTTP route handler for conversation progress; not an active Eng Teacher endpoint. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/devices/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/devices/)

Original upstream HTTP/API route area for devices. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [route.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/devices/route.ts) | Upstream HTTP route handler for devices; not an active Eng Teacher endpoint. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/email/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/email/)

Original upstream HTTP/API route area for email. Archived reference; not an active Eng Teacher feature or dependency.

Contains the subfolders listed in their own sections; no tracked files directly in this folder.

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/email/unsubscribe/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/email/unsubscribe/)

Original upstream HTTP/API route area for unsubscribe. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [route.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/email/unsubscribe/route.ts) | Upstream HTTP route handler for unsubscribe; not an active Eng Teacher endpoint. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/health/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/health/)

Original upstream HTTP/API route area for health. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [route.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/health/route.ts) | Upstream HTTP route handler for health; not an active Eng Teacher endpoint. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/jobs/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/jobs/)

Original upstream HTTP/API route area for jobs. Archived reference; not an active Eng Teacher feature or dependency.

Contains the subfolders listed in their own sections; no tracked files directly in this folder.

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/jobs/daily/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/jobs/daily/)

Original upstream HTTP/API route area for daily. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [route.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/jobs/daily/route.ts) | Upstream HTTP route handler for daily; not an active Eng Teacher endpoint. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/jobs/mail/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/jobs/mail/)

Original upstream HTTP/API route area for mail. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [route.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/jobs/mail/route.ts) | Upstream HTTP route handler for mail; not an active Eng Teacher endpoint. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/jobs/push/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/jobs/push/)

Original upstream HTTP/API route area for push. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [route.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/jobs/push/route.ts) | Upstream HTTP route handler for push; not an active Eng Teacher endpoint. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/just-speak/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/just-speak/)

Original upstream HTTP/API route area for just speak. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [route.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/just-speak/route.ts) | Upstream HTTP route handler for just speak; not an active Eng Teacher endpoint. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/mcp/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/mcp/)

Original upstream HTTP/API route area for mcp. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [route.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/mcp/route.ts) | Upstream HTTP route handler for mcp; not an active Eng Teacher endpoint. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/me/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/me/)

Original upstream HTTP/API route area for me. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [route.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/me/route.ts) | Upstream HTTP route handler for me; not an active Eng Teacher endpoint. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/modules/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/modules/)

Original upstream HTTP/API route area for modules. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [route.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/modules/route.ts) | Upstream HTTP route handler for modules; not an active Eng Teacher endpoint. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/modules/\[moduleId\]/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/modules/%5BmoduleId%5D/)

Original upstream HTTP/API route area for [module Id]. Archived reference; not an active Eng Teacher feature or dependency.

Contains the subfolders listed in their own sections; no tracked files directly in this folder.

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/modules/\[moduleId\]/lessons/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/modules/%5BmoduleId%5D/lessons/)

Original upstream HTTP/API route area for lessons. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [route.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/modules/%5BmoduleId%5D/lessons/route.ts) | Upstream HTTP route handler for lessons; not an active Eng Teacher endpoint. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/newsletter/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/newsletter/)

Original upstream HTTP/API route area for newsletter. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [route.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/newsletter/route.ts) | Upstream HTTP route handler for newsletter; not an active Eng Teacher endpoint. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/newsletter/confirmed/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/newsletter/confirmed/)

Original upstream HTTP/API route area for confirmed. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [route.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/newsletter/confirmed/route.ts) | Upstream HTTP route handler for confirmed; not an active Eng Teacher endpoint. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/oauth/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/oauth/)

Original upstream HTTP/API route area for oauth. Archived reference; not an active Eng Teacher feature or dependency.

Contains the subfolders listed in their own sections; no tracked files directly in this folder.

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/oauth/authorize/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/oauth/authorize/)

Original upstream HTTP/API route area for authorize. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [route.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/oauth/authorize/route.ts) | Upstream HTTP route handler for authorize; not an active Eng Teacher endpoint. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/oauth/register/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/oauth/register/)

Original upstream HTTP/API route area for register. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [route.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/oauth/register/route.ts) | Upstream HTTP route handler for register; not an active Eng Teacher endpoint. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/oauth/revoke/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/oauth/revoke/)

Original upstream HTTP/API route area for revoke. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [route.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/oauth/revoke/route.ts) | Upstream HTTP route handler for revoke; not an active Eng Teacher endpoint. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/oauth/token/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/oauth/token/)

Original upstream HTTP/API route area for token. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [route.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/oauth/token/route.ts) | Upstream HTTP route handler for token; not an active Eng Teacher endpoint. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/pair/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/pair/)

Original upstream HTTP/API route area for pair. Archived reference; not an active Eng Teacher feature or dependency.

Contains the subfolders listed in their own sections; no tracked files directly in this folder.

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/pair/claim/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/pair/claim/)

Original upstream HTTP/API route area for claim. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [route.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/pair/claim/route.ts) | Upstream HTTP route handler for claim; not an active Eng Teacher endpoint. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/pair/code/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/pair/code/)

Original upstream HTTP/API route area for code. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [route.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/pair/code/route.ts) | Upstream HTTP route handler for code; not an active Eng Teacher endpoint. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/pair/devices/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/pair/devices/)

Original upstream HTTP/API route area for devices. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [route.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/pair/devices/route.ts) | Upstream HTTP route handler for devices; not an active Eng Teacher endpoint. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/pair/devices/\[deviceId\]/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/pair/devices/%5BdeviceId%5D/)

Original upstream HTTP/API route area for [device Id]. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [route.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/pair/devices/%5BdeviceId%5D/route.ts) | Upstream HTTP route handler for \[device Id\]; not an active Eng Teacher endpoint. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/pair/info/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/pair/info/)

Original upstream HTTP/API route area for info. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [route.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/pair/info/route.ts) | Upstream HTTP route handler for info; not an active Eng Teacher endpoint. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/pair/session/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/pair/session/)

Original upstream HTTP/API route area for session. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [route.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/pair/session/route.ts) | Upstream HTTP route handler for session; not an active Eng Teacher endpoint. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/pair/unlock/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/pair/unlock/)

Original upstream HTTP/API route area for unlock. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [route.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/pair/unlock/route.ts) | Upstream HTTP route handler for unlock; not an active Eng Teacher endpoint. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/practice/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/practice/)

Original upstream HTTP/API route area for practice. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [route.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/practice/route.ts) | Upstream HTTP route handler for practice; not an active Eng Teacher endpoint. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/profile/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/profile/)

Original upstream HTTP/API route area for profile. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [route.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/profile/route.ts) | Upstream HTTP route handler for profile; not an active Eng Teacher endpoint. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/progress/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/progress/)

Original upstream HTTP/API route area for progress. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [route.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/progress/route.ts) | Upstream HTTP route handler for progress; not an active Eng Teacher endpoint. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/reference-audio/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/reference-audio/)

Original upstream HTTP/API route area for reference audio. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [route.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/reference-audio/route.ts) | Upstream HTTP route handler for reference audio; not an active Eng Teacher endpoint. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/reference-audio/generate/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/reference-audio/generate/)

Original upstream HTTP/API route area for generate. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [route.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/reference-audio/generate/route.ts) | Upstream HTTP route handler for generate; not an active Eng Teacher endpoint. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/sessions/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/sessions/)

Original upstream HTTP/API route area for sessions. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [route.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/sessions/route.ts) | Upstream HTTP route handler for sessions; not an active Eng Teacher endpoint. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/sessions/\[sessionId\]/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/sessions/%5BsessionId%5D/)

Original upstream HTTP/API route area for [session Id]. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [route.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/sessions/%5BsessionId%5D/route.ts) | Upstream HTTP route handler for \[session Id\]; not an active Eng Teacher endpoint. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/setup/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/setup/)

Original upstream HTTP/API route area for setup. Archived reference; not an active Eng Teacher feature or dependency.

Contains the subfolders listed in their own sections; no tracked files directly in this folder.

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/setup/mode/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/setup/mode/)

Original upstream HTTP/API route area for mode. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [route.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/setup/mode/route.ts) | Upstream HTTP route handler for mode; not an active Eng Teacher endpoint. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/stats/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/stats/)

Original upstream HTTP/API route area for stats. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [route.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/stats/route.ts) | Upstream HTTP route handler for stats; not an active Eng Teacher endpoint. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/stripe/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/stripe/)

Original upstream HTTP/API route area for stripe. Archived reference; not an active Eng Teacher feature or dependency.

Contains the subfolders listed in their own sections; no tracked files directly in this folder.

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/stripe/cancel/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/stripe/cancel/)

Original upstream HTTP/API route area for cancel. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [route.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/stripe/cancel/route.ts) | Upstream HTTP route handler for cancel; not an active Eng Teacher endpoint. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/support/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/support/)

Original upstream HTTP/API route area for support. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [route.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/support/route.ts) | Upstream HTTP route handler for support; not an active Eng Teacher endpoint. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/sync/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/sync/)

Original upstream HTTP/API route area for sync. Archived reference; not an active Eng Teacher feature or dependency.

Contains the subfolders listed in their own sections; no tracked files directly in this folder.

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/sync/advanced/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/sync/advanced/)

Original upstream HTTP/API route area for advanced. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [route.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/sync/advanced/route.ts) | Upstream HTTP route handler for advanced; not an active Eng Teacher endpoint. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/sync/import/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/sync/import/)

Original upstream HTTP/API route area for import. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [route.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/sync/import/route.ts) | Upstream HTTP route handler for import; not an active Eng Teacher endpoint. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/sync/inbox/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/sync/inbox/)

Original upstream HTTP/API route area for inbox. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [route.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/sync/inbox/route.ts) | Upstream HTTP route handler for inbox; not an active Eng Teacher endpoint. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/sync/pull/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/sync/pull/)

Original upstream HTTP/API route area for pull. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [route.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/sync/pull/route.ts) | Upstream HTTP route handler for pull; not an active Eng Teacher endpoint. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/sync/push/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/sync/push/)

Original upstream HTTP/API route area for push. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [route.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/sync/push/route.ts) | Upstream HTTP route handler for push; not an active Eng Teacher endpoint. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/sync/summary/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/sync/summary/)

Original upstream HTTP/API route area for summary. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [route.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/sync/summary/route.ts) | Upstream HTTP route handler for summary; not an active Eng Teacher endpoint. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/transcribe/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/transcribe/)

Original upstream HTTP/API route area for transcribe. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [route.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/transcribe/route.ts) | Upstream HTTP route handler for transcribe; not an active Eng Teacher endpoint. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/version/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/version/)

Original upstream HTTP/API route area for version. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [route.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/version/route.ts) | Upstream HTTP route handler for version; not an active Eng Teacher endpoint. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/webhooks/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/webhooks/)

Original upstream HTTP/API route area for webhooks. Archived reference; not an active Eng Teacher feature or dependency.

Contains the subfolders listed in their own sections; no tracked files directly in this folder.

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/webhooks/revenuecat/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/webhooks/revenuecat/)

Original upstream HTTP/API route area for revenuecat. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [route.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/webhooks/revenuecat/route.ts) | Upstream HTTP route handler for revenuecat; not an active Eng Teacher endpoint. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/webhooks/stripe/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/webhooks/stripe/)

Original upstream HTTP/API route area for stripe. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [route.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/api/webhooks/stripe/route.ts) | Upstream HTTP route handler for stripe; not an active Eng Teacher endpoint. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/desktop/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/desktop/)

Original upstream web route group/page area for desktop. Archived reference; not an active Eng Teacher feature or dependency.

Contains the subfolders listed in their own sections; no tracked files directly in this folder.

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/desktop/setup/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/desktop/setup/)

Original upstream web route group/page area for setup. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [page.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/desktop/setup/page.tsx) | Upstream framework page entrypoint for setup. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/oauth/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/oauth/)

Original upstream web route group/page area for oauth. Archived reference; not an active Eng Teacher feature or dependency.

Contains the subfolders listed in their own sections; no tracked files directly in this folder.

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/oauth/authorize/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/oauth/authorize/)

Original upstream web route group/page area for authorize. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [page.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/oauth/authorize/page.tsx) | Upstream framework page entrypoint for authorize. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/pair/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/pair/)

Original upstream web route group/page area for pair. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [page.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/pair/page.tsx) | Upstream framework page entrypoint for pair. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/setup/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/setup/)

Original upstream web route group/page area for setup. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [page.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/app/setup/page.tsx) | Upstream framework page entrypoint for setup. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/backend/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/backend/)

Original upstream backend backend inference/data support. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [.dockerignore](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/backend/.dockerignore) | Component .dockerignore configuration/policy; upstream cloud/security settings are reference material, not deployed Eng Teacher infrastructure. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/backend/ai-engine/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/backend/ai-engine/)

Original upstream ai engine backend inference/data support. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [.dockerignore](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/backend/ai-engine/.dockerignore) | Component .dockerignore configuration/policy; upstream cloud/security settings are reference material, not deployed Eng Teacher infrastructure. | Preserved upstream reference; not integrated |
| [Dockerfile](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/backend/ai-engine/Dockerfile) | Original container build/runtime recipe for this component; not the active environment setup target. | Preserved upstream reference; not integrated |
| [Dockerfile.cloud](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/backend/ai-engine/Dockerfile.cloud) | Original container build/runtime recipe for this component; not the active environment setup target. | Preserved upstream reference; not integrated |
| [audio_limits.py](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/backend/ai-engine/audio_limits.py) | audio limits module; static declarations include _env_number, AudioRejected, sniff_audio, wav_seconds, estimate_seconds, check_audio. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [main.py](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/backend/ai-engine/main.py) | main module; static declarations include configure_torch_cpu_threads, prime_audio_runtime_imports, ensure_runtime_warmup_started, lifespan, read_checked_audio, health. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [phoneme_scorer.py](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/backend/ai-engine/phoneme_scorer.py) | phoneme scorer module; static declarations include _clamp, _normalize_phoneme_string, _decode_ctc_predictions, _decode_with_ffmpeg, _load_audio, _tokenize_visible_words. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [pytest.ini](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/backend/ai-engine/pytest.ini) | pytest component resource/configuration; role follows the containing folder described above. | Preserved upstream reference; not integrated |
| [reference_tts.py](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/backend/ai-engine/reference_tts.py) | reference tts module; static declarations include _load_json, _preview_text, normalize_narration_text, sanitize_instruct_text, simplify_instruct_text, classify_tts_mode. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [requirements.desktop.arm64.txt](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/backend/ai-engine/requirements.desktop.arm64.txt) | Containing component dependency/build/test declarations; consult its scope before installing. | Preserved upstream reference; not integrated |
| [requirements.desktop.txt](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/backend/ai-engine/requirements.desktop.txt) | Containing component dependency/build/test declarations; consult its scope before installing. | Preserved upstream reference; not integrated |
| [requirements.test.txt](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/backend/ai-engine/requirements.test.txt) | Containing component dependency/build/test declarations; consult its scope before installing. | Preserved upstream reference; not integrated |
| [requirements.txt](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/backend/ai-engine/requirements.txt) | Containing component dependency/build/test declarations; consult its scope before installing. | Preserved upstream reference; not integrated |
| [speech_transcriber.py](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/backend/ai-engine/speech_transcriber.py) | speech transcriber module; static declarations include SpeechTranscriber. No behavior is executed by this guide. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/backend/ai-engine/tests/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/backend/ai-engine/tests/)

Upstream verification scenarios/fixtures for tests. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [test_audio_limits.py](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/backend/ai-engine/tests/test_audio_limits.py) | Regression/scenario definitions for test audio limits; execution and test boundaries are recorded separately. | Preserved upstream reference; not integrated |
| [test_endpoints.py](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/backend/ai-engine/tests/test_endpoints.py) | Regression/scenario definitions for test endpoints; execution and test boundaries are recorded separately. | Preserved upstream reference; not integrated |
| [test_warmup.py](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/backend/ai-engine/tests/test_warmup.py) | Regression/scenario definitions for test warmup; execution and test boundaries are recorded separately. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/backend/coach-engine/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/backend/coach-engine/)

Original upstream coach engine backend inference/data support. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [.dockerignore](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/backend/coach-engine/.dockerignore) | Component .dockerignore configuration/policy; upstream cloud/security settings are reference material, not deployed Eng Teacher infrastructure. | Preserved upstream reference; not integrated |
| [Dockerfile](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/backend/coach-engine/Dockerfile) | Original container build/runtime recipe for this component; not the active environment setup target. | Preserved upstream reference; not integrated |
| [coach_llm.py](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/backend/coach-engine/coach_llm.py) | coach llm implementation/helper module in the containing upstream reference component. | Preserved upstream reference; not integrated |
| [main.py](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/backend/coach-engine/main.py) | main module; static declarations include configure_torch_cpu_threads, ensure_coach_warmup_started, lifespan, sanitize_payload, health, coach_status. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [model.py](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/backend/coach-engine/model.py) | model module; static declarations include _format_support_error, QwenCoachEngine. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [parsing.py](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/backend/coach-engine/parsing.py) | parsing module; static declarations include clean_model_output, strip_role_prefix, sanitize_sentence, sanitize_coach_message, _parse_labeled, _parse_plain_text. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [prompts.py](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/backend/coach-engine/prompts.py) | prompts module; static declarations include target_system_prompt, freedom_system_prompt, _serialize_history, _user_prompt, build_messages. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [requirements.desktop.txt](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/backend/coach-engine/requirements.desktop.txt) | Containing component dependency/build/test declarations; consult its scope before installing. | Preserved upstream reference; not integrated |
| [requirements.txt](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/backend/coach-engine/requirements.txt) | Containing component dependency/build/test declarations; consult its scope before installing. | Preserved upstream reference; not integrated |
| [validation.py](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/backend/coach-engine/validation.py) | validation module; static declarations include latest_history_content, normalize_for_match, looks_like_prompt_echo, should_reject_coach_message. No behavior is executed by this guide. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/backend/data/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/backend/data/)

Original upstream data backend inference/data support. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [ipa_narration.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/backend/data/ipa_narration.json) | Structured ipa narration content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [phoneme_catalog.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/backend/data/phoneme_catalog.json) | Structured phoneme catalog content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [practice_targets.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/backend/data/practice_targets.json) | Structured practice targets content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [voice_config.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/backend/data/voice_config.json) | Structured voice config content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/)

Original upstream components UI components. Archived reference; not an active Eng Teacher feature or dependency.

Contains the subfolders listed in their own sections; no tracked files directly in this folder.

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/account/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/account/)

Original upstream account UI components. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [AccountPanel.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/account/AccountPanel.tsx) | Account Panel module; static declarations include FormEvent, Me, SignInMethod, AccountPanel, PlusCard, NewsletterCard. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [ConnectedApps.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/account/ConnectedApps.tsx) | Connected Apps module; static declarations include Connection, ConnectedApps, disconnect. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [me.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/account/me.ts) | me module; static declarations include Me, toMillis, parseMe, readMe. No behavior is executed by this guide. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/advanced/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/advanced/)

Original upstream advanced UI components. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [PhraseBank.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/advanced/PhraseBank.tsx) | Phrase Bank module; static declarations include PhraseKind, PhraseBank. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [PhraseDetail.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/advanced/PhraseDetail.tsx) | Phrase Detail module; static declarations include Phrase, PhraseDetail, PhraseView, highlight, GapFill, Rephrase. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [PhrasePractice.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/advanced/PhrasePractice.tsx) | Phrase Practice module; static declarations include Phrase, PhraseDrill, PhrasePractice, DrillCard. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [PlateauTrack.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/advanced/PlateauTrack.tsx) | Plateau Track module; static declarations include DiagnosticItem, Evidence, FossilError, Track, soundEvidence, PlateauTrack. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [RecordCompare.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/advanced/RecordCompare.tsx) | Record Compare module; static declarations include Recording, Status, pickMime, of, RecordCompare, start. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [RecordingsLibrary.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/advanced/RecordingsLibrary.tsx) | Recordings Library module; static declarations include Recording, play, RecordingsLibrary. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [Slang.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/advanced/Slang.tsx) | Slang module; static declarations include SlangEntry, SlangFit, SlangRegion, SlangDictionary, SlangDetail, QuizOptions. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [TodayPlan.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/advanced/TodayPlan.tsx) | Today Plan module; static declarations include PlanItem, planLabel, TodayPlan. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [content.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/advanced/content.ts) | content module; static declarations include AdvancedContent, getJson, load, loadAdvancedContent, useAdvancedContent. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [recordings-store.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/advanced/recordings-store.ts) | recordings store module; static declarations include Recording, RecordingIndex, openDb, withStore, readIndex, changed. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [store.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/advanced/store.ts) | store module; static declarations include Track, PracticeListItem, RecordingIndex, CardState, Grade, StoredCard. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [target-audio.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/advanced/target-audio.ts) | target audio module; static declarations include stopTarget, playUrl, speakInBrowser, playTarget. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [ui.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/advanced/ui.tsx) | ui module; static declarations include AdvancedNav, PageHead, Chip, Surface, Tag, RowLink. No behavior is executed by this guide. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/ai/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/ai/)

Original upstream ai UI components. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [AiOfferBanner.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/ai/AiOfferBanner.tsx) | Ai Offer Banner module; static declarations include AiBlockedDetail, AiOfferBanner. No behavior is executed by this guide. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/audio/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/audio/)

Original upstream audio UI components. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [AudioRecorder.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/audio/AudioRecorder.tsx) | Audio Recorder module; static declarations include AudioRecorderProps, AudioRecorder, handleReferenceAudio, handleTakeAudio. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [CoachVoiceCard.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/audio/CoachVoiceCard.tsx) | Coach Voice Card module; static declarations include CoachVoiceSettings, CoachVoiceCardProps, CoachVoiceCard, handlePlaySample. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [PracticeStudio.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/audio/PracticeStudio.tsx) | Practice Studio module; static declarations include PronunciationAssessment, PronunciationHighlight, PracticeStudioProps, HighlightChip, PracticeStudio, handleClearTake. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [ProfileCoachVoice.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/audio/ProfileCoachVoice.tsx) | Profile Coach Voice module; static declarations include ProfileCoachVoice. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [QuickPracticeHome.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/audio/QuickPracticeHome.tsx) | Quick Practice Home module; static declarations include QuickPracticeHomeProps, QuickPracticeHome. No behavior is executed by this guide. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/auth/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/auth/)

Original upstream auth UI components. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [AuthCard.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/auth/AuthCard.tsx) | Auth Card module; static declarations include AuthCardProps, AuthCard, AuthNotice, FieldLabel. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [AuthForm.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/auth/AuthForm.tsx) | Auth Form module; static declarations include FormEvent, ProviderMethod, PendingLink, AuthFormProps, AuthForm, enter. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [ForgotPasswordForm.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/auth/ForgotPasswordForm.tsx) | Forgot Password Form module; static declarations include FormEvent, cooldownLeft, requestReset, ForgotPasswordForm, handleSubmit. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [OnboardingWizard.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/auth/OnboardingWizard.tsx) | Onboarding Wizard module; static declarations include LearningGoal, OnboardingWizard, handleSubmit. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [PasswordChecklist.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/auth/PasswordChecklist.tsx) | Password Checklist module; static declarations include PasswordChecklist. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [ProviderButtons.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/auth/ProviderButtons.tsx) | Provider Buttons module; static declarations include SignInMethod, GoogleG, AppleLogo, ProviderButton, OrDivider. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [ResetPasswordForm.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/auth/ResetPasswordForm.tsx) | Reset Password Form module; static declarations include FormEvent, Stage, tellServerAndSignIn, ResetPasswordForm, handleSubmit. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [SetupSelection.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/auth/SetupSelection.tsx) | Setup Selection module; static declarations include SetupSelectionProps, SetupSelection, handleModeSelection. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [SignInMethods.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/auth/SignInMethods.tsx) | Sign In Methods module; static declarations include FormEvent, ProviderMethod, SignInMethod, Note, Icon, SignInMethods. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [VerifyEmailPanel.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/auth/VerifyEmailPanel.tsx) | Verify Email Panel module; static declarations include User, Stage, VerifyEmailPanel, resend. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [password-rules.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/auth/password-rules.ts) | password rules module; static declarations include PasswordRule, checkPassword, isPasswordAcceptable. No behavior is executed by this guide. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/billing/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/billing/)

Original upstream billing UI components. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [BillingAction.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/billing/BillingAction.tsx) | Billing Action module; static declarations include BillingAction, go. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [CheckoutRedirect.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/billing/CheckoutRedirect.tsx) | Checkout Redirect module; static declarations include PlanInterval, CheckoutRedirect. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [PlanButton.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/billing/PlanButton.tsx) | Plan Button module; static declarations include PlanButton, PortalButton. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [PlanCards.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/billing/PlanCards.tsx) | Plan Cards module; static declarations include Ticks, PlanCards, Unavailable, Plan. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [billing-api.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/billing/billing-api.ts) | billing api module; static declarations include PlanInterval, BillingOutcome, post. No behavior is executed by this guide. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/coach/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/coach/)

Original upstream coach UI components. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [AiCoachHistory.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/coach/AiCoachHistory.tsx) | Ai Coach History module; static declarations include formatTimestamp, AiCoachHistory, handleDeleteSession. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [AiCoachPlayground.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/coach/AiCoachPlayground.tsx) | Ai Coach Playground module; static declarations include EngineStatusPayload, buildHistory, createTurn, AiCoachPlayground, loadStatus, registerReplyAudioUrl. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [AiCoachSidebarHistory.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/coach/AiCoachSidebarHistory.tsx) | Ai Coach Sidebar History module; static declarations include formatTimestamp, AiCoachSidebarHistory, syncSessions, handleStorage, handleSessionsChanged. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [CoachOverviewCard.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/coach/CoachOverviewCard.tsx) | Coach Overview Card module; static declarations include CoachOverviewCardProps, CoachOverviewCard. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [CoachSetupCard.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/coach/CoachSetupCard.tsx) | Coach Setup Card module; static declarations include CoachSetupCardProps, CoachSetupCard. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [CoachSidePanel.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/coach/CoachSidePanel.tsx) | Coach Side Panel module; static declarations include CoachSidePanelProps, CoachSidePanel. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [CoachThread.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/coach/CoachThread.tsx) | Coach Thread module; static declarations include formatReplySentence, CoachThreadProps, CoachThread. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [FreedomAssessmentPanel.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/coach/FreedomAssessmentPanel.tsx) | Freedom Assessment Panel module; static declarations include getHighlightStyles, FreedomAssessmentPanelProps, FreedomAssessmentPanel. No behavior is executed by this guide. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/conversation/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/conversation/)

Original upstream conversation UI components. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [ConversationFlowCard.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/conversation/ConversationFlowCard.tsx) | Conversation Flow Card module; static declarations include getHighlightStyles, ReplyWordFeedback, getEngineMessage, ConversationFlowCardProps, ConversationFlowCard. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [ConversationModuleCard.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/conversation/ConversationModuleCard.tsx) | Conversation Module Card module; static declarations include ConversationModuleCardProps, ConversationModuleCard. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [ConversationModuleGrid.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/conversation/ConversationModuleGrid.tsx) | Conversation Module Grid module; static declarations include ConversationModuleGridProps, ConversationModuleGrid. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [ConversationModuleHeader.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/conversation/ConversationModuleHeader.tsx) | Conversation Module Header module; static declarations include ConversationModuleHeaderProps, ConversationModuleHeader. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [ConversationResult.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/conversation/ConversationResult.tsx) | Conversation Result module; static declarations include ConversationResultProps, ConversationResult. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [ConversationSession.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/conversation/ConversationSession.tsx) | Conversation Session module; static declarations include Phase, CoachAudioState, TurnResponse, ConversationSessionProps, ConversationSession, stopCoachAudio. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [ConversationSidePanel.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/conversation/ConversationSidePanel.tsx) | Conversation Side Panel module; static declarations include ConversationSidePanelProps, ConversationSidePanel. No behavior is executed by this guide. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/desktop/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/desktop/)

Original upstream desktop UI components. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [desktop-setup.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/desktop/desktop-setup.tsx) | desktop setup module; static declarations include StatusPill, DesktopSetup, waitForDesktopSetupBridge, handlePrimaryAction, handleOpenLogs. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [profile-desktop-runtime.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/desktop/profile-desktop-runtime.tsx) | profile desktop runtime module; static declarations include formatDate, formatPhase, StatusPill, InfoCard, baseName, RuntimeLocationRow. No behavior is executed by this guide. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/just-speak/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/just-speak/)

Original upstream just speak UI components. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [JustSpeakStudio.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/just-speak/JustSpeakStudio.tsx) | Just Speak Studio module; static declarations include JustSpeakFeedback, JustSpeakResult, JustSpeakHistoryItem, safeReadHistory, safeWriteHistory, formatWhen. No behavior is executed by this guide. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/learn/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/learn/)

Original upstream learn UI components. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [AssessmentResult.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/learn/AssessmentResult.tsx) | Assessment Result module; static declarations include PronunciationAssessment, PronunciationHighlight, getHighlightStyles, SentenceFeedback, AssessmentResultProps, AssessmentResult. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [ExamLesson.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/learn/ExamLesson.tsx) | Exam Lesson module; static declarations include ExamLessonProps, Phase, ExamLesson, runAssessment, handleRetry, handleNext. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [ExamResult.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/learn/ExamResult.tsx) | Exam Result module; static declarations include ExamResultProps, ExamResult. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [LessonList.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/learn/LessonList.tsx) | Lesson List module; static declarations include LessonListProps, LessonList. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [LessonRow.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/learn/LessonRow.tsx) | Lesson Row module; static declarations include LessonRowProps, LessonRow. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [LessonSummary.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/learn/LessonSummary.tsx) | Lesson Summary module; static declarations include LessonSummaryProps, LessonSummary. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [ModuleCard.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/learn/ModuleCard.tsx) | Module Card module; static declarations include ModuleCardProps, ModuleCard. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [ModuleGrid.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/learn/ModuleGrid.tsx) | Module Grid module; static declarations include ModuleGridProps, ModuleGrid. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [PracticeLesson.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/learn/PracticeLesson.tsx) | Practice Lesson module; static declarations include PracticeLessonProps, Phase, PracticeLesson, runAssessment, handleRetry, handleNext. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [ProgressRing.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/learn/ProgressRing.tsx) | Progress Ring module; static declarations include ProgressRingProps, ProgressRing. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [TheoryLesson.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/learn/TheoryLesson.tsx) | Theory Lesson module; static declarations include TheoryLessonProps, TheoryLesson. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [TheoryNarrationButton.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/learn/TheoryNarrationButton.tsx) | Theory Narration Button module; static declarations include TheoryNarrationButtonProps, stripHtml, TheoryNarrationButton, handleToggleNarration. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [WordQueue.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/learn/WordQueue.tsx) | Word Queue module; static declarations include WordQueueProps, WordQueue. No behavior is executed by this guide. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/learn-hub/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/learn-hub/)

Original upstream learn hub UI components. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [ExerciseCard.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/learn-hub/ExerciseCard.tsx) | Exercise Card module; static declarations include FormEvent, Exercise, ExerciseAnswer, GradeResult, shuffled, ExerciseCardProps. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [FlashcardDeck.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/learn-hub/FlashcardDeck.tsx) | Flashcard Deck module; static declarations include CardState, Grade, DeckCard, FlashcardDeck, grade. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [GrammarBrowser.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/learn-hub/GrammarBrowser.tsx) | Grammar Browser module; static declarations include CefrLevel, GrammarPoint, GrammarBrowser. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [GrammarPointView.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/learn-hub/GrammarPointView.tsx) | Grammar Point View module; static declarations include Emphasis, ExampleLine, GrammarPointView. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [LevelPicker.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/learn-hub/LevelPicker.tsx) | Level Picker module; static declarations include CefrLevel, useLevel, LevelPicker. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [PackCacheRegistration.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/learn-hub/PackCacheRegistration.tsx) | Pack Cache Registration module; static declarations include PackCacheRegistration. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [PracticeHub.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/learn-hub/PracticeHub.tsx) | Practice Hub module; static declarations include PracticeHub, Stat, HubCard, plural. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [PracticeSession.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/learn-hub/PracticeSession.tsx) | Practice Session module; static declarations include pick, PracticeSession, Round. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [ShareCard.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/learn-hub/ShareCard.tsx) | Share Card module; static declarations include drawShareCard, ShareCardButton, share. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [fixture-pack.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/learn-hub/fixture-pack.ts) | fixture pack module; static declarations include LevelSeed, seed, fixturePack. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [modes.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/learn-hub/modes.ts) | modes module; static declarations include CefrLevel, ExerciseKind, PracticeMode, modeById, parseLevel. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [packs.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/learn-hub/packs.ts) | packs module; static declarations include CefrLevel, PackContent, PackIndex, PackManifest, LoadedPack, loadIndex. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [progress.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/learn-hub/progress.ts) | progress module; static declarations include Activity, ActivityKind, ProgressSummary, CardState, read, write. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [srs.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/learn-hub/srs.ts) | srs module; static declarations include CardState, buildQueue. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [sync-logic.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/learn-hub/sync-logic.ts) | sync logic module; static declarations include SyncedCard, CustomCard, SyncMarks, deckFor, cleanCard, cardsSince. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [sync.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/learn-hub/sync.ts) | sync module; static declarations include CustomCard, SyncMarks, SyncedCard, read, write, installId. No behavior is executed by this guide. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/levels/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/levels/)

Original upstream levels UI components. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [LevelSettings.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/levels/LevelSettings.tsx) | Level Settings module; static declarations include CefrLevel, LevelSettings. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [PlacementTest.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/levels/PlacementTest.tsx) | Placement Test module; static declarations include AdaptiveResponse, AdaptiveResult, PlacementTest, answer, PlacementResult. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [level-store.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/levels/level-store.ts) | level store module; static declarations include LevelPrefs, LevelSkill, read, write, readLevelPrefs, subscribe. No behavior is executed by this guide. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/mouth-map/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/mouth-map/)

Original upstream mouth map UI components. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [AccentSwitch.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/mouth-map/AccentSwitch.tsx) | Accent Switch module; static declarations include AccentSwitch, parseVariant. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [CompareView.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/mouth-map/CompareView.tsx) | Compare View module; static declarations include Variant, Side, CompareView, morph. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [DrillLadder.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/mouth-map/DrillLadder.tsx) | Drill Ladder module; static declarations include DrillLadder. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [FrontLipsSvg.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/mouth-map/FrontLipsSvg.tsx) | Front Lips Svg module; static declarations include VocalTractParams, FrontLipsSvg. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [LazyMouthMapDemo.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/mouth-map/LazyMouthMapDemo.tsx) | Lazy Mouth Map Demo module; static declarations include ComponentType, ReactNode, Demo, LazyMouthMapDemo. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [MouthMap.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/mouth-map/MouthMap.tsx) | Mouth Map module; static declarations include Variant, MouthMapProps, MouthMap, play. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [MouthMapDemo.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/mouth-map/MouthMapDemo.tsx) | Mouth Map Demo module; static declarations include DemoSound, MouthMapDemo. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [MouthMapSvg.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/mouth-map/MouthMapSvg.tsx) | Mouth Map Svg module; static declarations include FillId, LayerId, OverlayId, PlaceAnchor, Point, VocalTractParams. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [SoundLink.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/mouth-map/SoundLink.tsx) | Sound Link module; static declarations include SoundLink, RecordPhonemes. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [SoundsToFix.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/mouth-map/SoundsToFix.tsx) | Sounds To Fix module; static declarations include Variant, SoundsToFix. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [copy.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/mouth-map/copy.ts) | copy module; static declarations include voicingText, howTo, describeForScreenReader. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [fixture-targets.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/mouth-map/fixture-targets.json) | Structured fixture targets content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [load-targets.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/mouth-map/load-targets.ts) | load targets module; static declarations include ArticulationTarget, LoadedTargets, accept. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [sound-practice.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/mouth-map/sound-practice.ts) | sound practice module; static declarations include SoundRecord, SoundStore, recordScore, SoundToFix, soundsToFix, DrillStep. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [sound-store.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/mouth-map/sound-store.ts) | sound store module; static declarations include SoundStore, loadSoundStore, saveSoundStore, useSoundStore, recordPhonemeScores. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [speak.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/mouth-map/speak.ts) | speak module; static declarations include canSpeak, speakWord. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [targets.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/mouth-map/targets.ts) | targets module; static declarations include Variant, targetFor, soundsIn, ipaOf, soundIdFromSymbol. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [use-articulation.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/mouth-map/use-articulation.ts) | use articulation module; static declarations include ArticulationTarget, VocalTractParams, shapeAt, prefersReducedMotion, Options, useArticulation. No behavior is executed by this guide. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/newsletter/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/newsletter/)

Original upstream newsletter UI components. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [NewsletterForm.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/newsletter/NewsletterForm.tsx) | Newsletter Form module; static declarations include FormEvent, NewsletterFormProps, NewsletterForm, submit. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [newsletter-api.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/newsletter/newsletter-api.ts) | newsletter api module; static declarations include NewsletterSource, SubscribeResult, looksLikeEmail, subscribeToNewsletter, unsubscribeFromNewsletter, describeSubscribeFailure. No behavior is executed by this guide. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/oauth/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/oauth/)

Original upstream oauth UI components. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [AuthorizeConsent.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/oauth/AuthorizeConsent.tsx) | Authorize Consent module; static declarations include FormEvent, ScopeOption, Request, State, idToken, errorText. No behavior is executed by this guide. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/pair/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/pair/)

Original upstream pair UI components. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [PairPanel.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/pair/PairPanel.tsx) | Pair Panel module; static declarations include IssuedCode, PairPanelProps, PairPanel, revoke, this. No behavior is executed by this guide. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/redeem/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/redeem/)

Original upstream redeem UI components. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [RedeemPanel.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/redeem/RedeemPanel.tsx) | Redeem Panel module; static declarations include FormEvent, Account, Done, readBody, refusal, RedeemPanel. No behavior is executed by this guide. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/support/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/support/)

Original upstream support UI components. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [SupportForm.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/support/SupportForm.tsx) | Support Form module; static declarations include FormEvent, SupportTopic, SupportForm, submit. No behavior is executed by this guide. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/theme/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/theme/)

Original upstream theme UI components. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [ThemeToggle.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/theme/ThemeToggle.tsx) | Theme Toggle module; static declarations include ThemeChoice, subscribe, readChoice, apply, Icon, ThemeToggle. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [theme.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/theme/theme.ts) | theme module; static declarations include ThemeChoice, parseThemeChoice, nextThemeChoice. No behavior is executed by this guide. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/ui/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/ui/)

Original upstream ui UI components. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [app-page.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/ui/app-page.tsx) | app page module; static declarations include NavKey, AppPage, AppIntro. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [app-shell.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/ui/app-shell.tsx) | app shell module; static declarations include AppShell. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [brand-mark.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/ui/brand-mark.tsx) | brand mark module; static declarations include BrandMarkProps, Logo, BrandMark. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [button.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/ui/button.tsx) | button module; static declarations include ButtonVariant, ButtonSize, buttonVariants, ButtonProps. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [card.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/ui/card.tsx) | card module; static declarations include Card, CardTitle, CardDescription. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [contact.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/ui/contact.ts) | contact implementation/helper module in the containing upstream reference component. | Preserved upstream reference; not integrated |
| [copy-field.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/ui/copy-field.tsx) | copy field module; static declarations include CopyField. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [desktop-shell.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/ui/desktop-shell.tsx) | desktop shell module; static declarations include DesktopShell. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [desktop-sidebar.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/ui/desktop-sidebar.tsx) | desktop sidebar module; static declarations include DesktopSidebar. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [desktop-top-bar.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/ui/desktop-top-bar.tsx) | desktop top bar module; static declarations include DesktopTopBar. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [empty-state.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/ui/empty-state.tsx) | empty state module; static declarations include EmptyState. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [faq-section.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/ui/faq-section.tsx) | faq section module; static declarations include FaqSection. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [footer.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/ui/footer.tsx) | footer module; static declarations include Footer. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [input.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/ui/input.tsx) | input module; static declarations include InputHTMLAttributes, Input. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [legal-page.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/ui/legal-page.tsx) | legal page module; static declarations include LegalSection, LegalBody. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [module-progress-frame.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/ui/module-progress-frame.tsx) | module progress frame module; static declarations include ModuleProgressFrameProps, ModuleProgressFrame. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [module-progress.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/ui/module-progress.tsx) | module progress module; static declarations include ProgressBar, ModuleProgress. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [navbar-frame.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/ui/navbar-frame.tsx) | navbar frame module; static declarations include NavbarFrameProps, NavbarFrame. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [navbar.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/ui/navbar.tsx) | navbar module; static declarations include NavKey, NavbarProps, Navbar. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [page-shell.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/ui/page-shell.tsx) | page shell module; static declarations include PageShell, PageIntro. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [privacy-choices-modal.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/ui/privacy-choices-modal.tsx) | privacy choices modal module; static declarations include ComponentType, Panel, PrivacyChoicesModal, open. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [privacy-choices-panel.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/ui/privacy-choices-panel.tsx) | privacy choices panel module; static declarations include ToggleProps, Toggle, PrivacyChoicesPanel. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [select.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/ui/select.tsx) | select module; static declarations include SelectHTMLAttributes, SelectProps, Select. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [sign-out-button.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/ui/sign-out-button.tsx) | sign out button module; static declarations include SignOutButton, handleSignOut. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [smooth-scroll.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/ui/smooth-scroll.tsx) | smooth scroll module; static declarations include ReactNode, SmoothScroll. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [split-text.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/components/ui/split-text.tsx) | split text module; static declarations include CSSProperties, ElementType, SplitTextProps, SplitText. No behavior is executed by this guide. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/email-templates/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/email-templates/)

Original upstream email templates source/configuration collection. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [confirm.html](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/email-templates/confirm.html) | confirm presentation/page/browser-install resource for the containing component. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/hooks/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/hooks/)

Original upstream hooks source/configuration collection. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [cloud-fetch.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/hooks/cloud-fetch.ts) | cloud fetch module; static declarations include firebaseApp, getAppCheck, createAppCheck, appCheckToken, idToken, CloudFetchInit. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [use-is-electron.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/hooks/use-is-electron.ts) | use is electron module; static declarations include subscribe, getSnapshot, useIsElectron. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [use-stored.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/hooks/use-stored.ts) | use stored module; static declarations include subscribeStorage, readStorage, useStoredString, writeStored, notifyStored, useClientCheck. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [useAudioRecorder.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/hooks/useAudioRecorder.ts) | use Audio Recorder module; static declarations include getSupportedMimeType, encodeWav, convertBlobToWav, useAudioRecorder, cleanupTracks, clearRecording. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [useCoachVoice.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/hooks/useCoachVoice.ts) | use Coach Voice module; static declarations include CoachVoiceSettings, getSnapshot, getServerSnapshot, subscribe, useCoachVoice. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [useEngineReady.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/hooks/useEngineReady.ts) | use Engine Ready module; static declarations include useEngineReady, check. No behavior is executed by this guide. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/lib/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/lib/)

Original upstream lib shared/domain/service helpers. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [ai-coach-gemini.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/lib/ai-coach-gemini.ts) | ai coach gemini module; static declarations include isGeminiCoachConfigured, latestUserContent, serializeHistory, buildUserPromptText, systemInstructionForMode, responseSchemaForMode. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [ai-coach-storage.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/lib/ai-coach-storage.ts) | ai coach storage module; static declarations include getAiCoachStorageKey, readSavedAiCoachSessions, writeSavedAiCoachSessions, deleteSavedAiCoachSession. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [ai-coach.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/lib/ai-coach.ts) | ai coach module; static declarations include AiCoachRole, AiCoachReplyMode, AiCoachPhase, AiCoachTurn, AiCoachGeneratedTurn, AiCoachHistoryEntry. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [app-mode.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/lib/app-mode.ts) | app mode module; static declarations include AppMode, parseAppMode, getAppModeCookieOptions. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [app-session.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/lib/app-session.ts) | app session module; static declarations include BillingState, LearningGoal, AppUser, AppSession, getAppSession, requireAppUser. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [audio-feedback.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/lib/audio-feedback.ts) | audio feedback module; static declarations include createCorrectAudio, createIncorrectAudio, createCompleteAudio, configureReferenceWordPlayback, playLearnerRecordingSegment. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [conversation-progress-sync.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/lib/conversation-progress-sync.ts) | conversation progress sync module; static declarations include loadConversationProgressForMode. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [conversation.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/lib/conversation.ts) | conversation module; static declarations include ConversationTurn, ConversationModule, ConversationProgressEntry, ConversationProgressMap, ConversationModuleWithProgress, parseConversationProgress. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [just-speak-gemini.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/lib/just-speak-gemini.ts) | just speak gemini module; static declarations include JustSpeakFeedback, buildPrompt, isJustSpeakGeminiConfigured, generateJustSpeakFeedbackWithGemini. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [learn-catalog.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/lib/learn-catalog.ts) | learn catalog module; static declarations include LearnCatalog, getLearnCatalog, getModuleFromCatalog, getLessonFromCatalog, getLessonByIdFromCatalog, findCatalogSqlUnderDir. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [learn-data.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/lib/learn-data.ts) | learn data module; static declarations include getModulesWithProgressForMode, getModuleLessonDataForMode, getLessonDataForMode, getModuleProgressStatsForMode, getLearningStatsForMode. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [learn.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/lib/learn.ts) | learn module; static declarations include Module, UserProgress, ModuleWithProgress, LessonType, LessonWord, Lesson. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [lesson-progress-client.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/lib/lesson-progress-client.ts) | lesson progress client module; static declarations include send, startLessonSession, endLessonSession, recordAttempt, saveExamScore, saveConversationScore. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [local-learn.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/lib/local-learn.ts) | local learn module; static declarations include CookieValue, CookieReader, CookieWriter, CompactModuleState, CompactLessonState, CompactPendingSession. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [local-profile.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/lib/local-profile.ts) | local profile module; static declarations include CookieValue, CookieReader, CookieWriter, LocalProfile, createDefaultLocalProfile, parseLocalProfile. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [practice-targets.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/lib/practice-targets.ts) | practice targets module; static declarations include PracticeTargetSegment, PracticeTargetRecord, PracticeTargetOption, toLabel, buildCue, getPracticeTarget. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [pronunciation.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/lib/pronunciation.ts) | pronunciation module; static declarations include PronunciationStatus, PronunciationHighlight, PronunciationPhoneme, PronunciationAssessment. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [stripe.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/lib/stripe.ts) | stripe module; static declarations include getStripe, isStripeConfigured. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [support-request.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/lib/support-request.ts) | support request module; static declarations include SupportTopic, SupportPlatform, SupportRequest, SupportStatus, topicLabel, cleanSupportText. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [utils.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/lib/utils.ts) | utils module; static declarations include ClassValue, cn. No behavior is executed by this guide. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/lib/auth/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/lib/auth/)

Original upstream auth shared/domain/service helpers. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [bearer.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/lib/auth/bearer.ts) | bearer module; static declarations include readBearerToken, SessionSource, chooseSessionSource. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [proxy.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/lib/auth/proxy.ts) | proxy module; static declarations include NextRequest, gateRequest, hasValidSessionCookie. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [route-gate.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/lib/auth/route-gate.ts) | route gate module; static declarations include matchesRoute, RouteDecision, RouteGateInput, needsSignInCheck, decideRoute. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [safe-next.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/lib/auth/safe-next.ts) | safe next module; static declarations include safeNextPath. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [session-cookie.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/lib/auth/session-cookie.ts) | session cookie module; static declarations include getSessionCookieOptions, isRecentSignIn. No behavior is executed by this guide. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/lib/cloud/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/lib/cloud/)

Original upstream cloud shared/domain/service helpers. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [attempt-input.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/lib/cloud/attempt-input.ts) | attempt input module; static declarations include clampScore, AttemptInput, AttemptParseResult, boundedString, isPlainObject, boundedDetail. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [profile-input.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/lib/cloud/profile-input.ts) | profile input module; static declarations include LearningGoal, LevelPrefs, ProfileUpdate, ProfileParseResult, parseProfileUpdate, reconcileFocusOnly. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [progress-logic.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/lib/cloud/progress-logic.ts) | progress logic module; static declarations include ModuleProgressRecord, applyExamResult, toUserProgress, EndedSessionRecord, LessonSummary, summarizeLessonSessions. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [store.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/lib/cloud/store.ts) | store module; static declarations include here, DocumentData, LearningGoal, LevelPrefs, EndedSessionRecord, ModuleProgressRecord. No behavior is executed by this guide. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/lib/firebase/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/lib/firebase/)

Original upstream firebase shared/domain/service helpers. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [admin.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/lib/firebase/admin.ts) | admin module; static declarations include App, getFirebaseProjectId, isFirebaseServerConfigured, hasAdminCredentials, isCloudServerReady, readServiceAccount. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [auth-errors.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/lib/firebase/auth-errors.ts) | auth errors module; static declarations include describeAuthError. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [client.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/lib/firebase/client.ts) | client module; static declarations include Auth, User, getFirebaseAuth, startServerSession, getCurrentIdToken. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [config.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/lib/firebase/config.ts) | config build/runtime/tool configuration for the containing component. | Preserved upstream reference; not integrated |
| [providers.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/lib/firebase/providers.ts) | providers module; static declarations include AuthProvider, User, UserCredential, PendingLink, SignInMethod, ProviderMethod. No behavior is executed by this guide. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/lib/mcp/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/lib/mcp/)

Original upstream mcp shared/domain/service helpers. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [advanced-content.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/lib/mcp/advanced-content.ts) | advanced content module; static declarations include PackIndex, PackManifest, AdvancedLibrary, readJson, AdvancedContent, load. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [handler.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/lib/mcp/handler.ts) | handler module; static declarations include rpcError, handleMcpPost, handleMcpPostOnly. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [quiz.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/lib/mcp/quiz.ts) | quiz module; static declarations include Env, secret, QuizClaims, signQuiz, verifyQuiz, QuizFilter. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [server.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/lib/mcp/server.ts) | server module; static declarations include RateLimitResult, McpContext, buildCadenceMcpServer, countToolCalls, limitToolCalls, rateLimitedBody. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [teacher-tools.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/lib/mcp/teacher-tools.ts) | teacher tools module; static declarations include Phrase, SlangEntry, PracticeDayItem, ConnectorReview, AdvancedLibrary, ToolResult. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [tools.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/lib/mcp/tools.ts) | tools module; static declarations include Exercise, ExerciseAnswer, Activity, ActivityKind, ToolContext, ToolResult. No behavior is executed by this guide. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/lib/oauth/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/lib/oauth/)

Original upstream oauth shared/domain/service helpers. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [authorize.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/lib/oauth/authorize.ts) | authorize module; static declarations include OAuthClient, AuthorizeParams, AuthorizeValidation, RawParams, validateAuthorizeParams, is. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [client-identity.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/lib/oauth/client-identity.ts) | client identity module; static declarations include KnownProduct, isStringList, parseKnownProducts, knownProducts, sanitizeClientName, fold. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [config.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/lib/oauth/config.ts) | config build/runtime/tool configuration for the containing component. | Preserved upstream reference; not integrated |
| [cors.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/lib/oauth/cors.ts) | cors module; static declarations include withCors, corsPreflightResponse, mcpPostOnlyResponse. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [metadata.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/lib/oauth/metadata.ts) | metadata module; static declarations include protectedResourceMetadata, authorizationServerMetadata. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [redirect-uri.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/lib/oauth/redirect-uri.ts) | redirect uri module; static declarations include isAllowedRedirectUri. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [request.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/lib/oauth/request.ts) | request module; static declarations include BodyTooLargeError, readText, readOAuthFormBody, readJsonObject, jsonResponse, oauthErrorResponse. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [store.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/lib/oauth/store.ts) | store module; static declarations include DocumentReference, OAuthClient, TokenRecord, IssuedTokenSet, OAuthError, TokenOutcome. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [verify.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/lib/oauth/verify.ts) | verify module; static declarations include TokenRecord, McpAuthContext, AuthResult, getBearerToken, challengeResponse, authenticateMcpRequest. No behavior is executed by this guide. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/lib/pairing/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/lib/pairing/)

Original upstream pairing shared/domain/service helpers. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [admin.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/lib/pairing/admin.ts) | admin module; static declarations include requirePairingAdmin, hasPairingAdminCookie, getAdminCookieOptions, unauthorizedResponse. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [engines.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/lib/pairing/engines.ts) | engines module; static declarations include areEnginesReady. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [identity.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/lib/pairing/identity.ts) | identity module; static declarations include LanAddress, getLanAddresses, getPrimaryLanAddress, getMdnsHostname, getServerDisplayName, getServerPort. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [learn-store.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/lib/pairing/learn-store.ts) | learn store module; static declarations include resolveLearnFile, readDeviceLearnState, writeDeviceLearnState. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [protocol.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/lib/pairing/protocol.ts) | protocol module; static declarations include removed, into, PairingPayload, PairedDeviceSummary, ServerInfo, ClaimRequest. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [qr.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/lib/pairing/qr.ts) | qr module; static declarations include renderQrSvg. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [request.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/lib/pairing/request.ts) | request module; static declarations include resolveDeviceFromRequest, resolveDeviceFromHeaders. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [service-logic.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/lib/pairing/service-logic.ts) | service logic module; static declarations include PairedDeviceSummary, PairingErrorCode, Mutation, Outcome, generatePairingCode, generateDeviceToken. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [service.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/lib/pairing/service.ts) | service module; static declarations include PairedDeviceSummary, PairingPayload, ServerInfo, ClaimInput, ClaimOutput, Outcome. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [store.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/lib/pairing/store.ts) | store module; static declarations include PairingCodeRecord, PairedDeviceRecord, PairingState, resolveDataDir, resolvePairingFile, createInitialState. No behavior is executed by this guide. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/lib/platform/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/lib/platform/)

Original upstream platform shared/domain/service helpers. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [content-model.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/lib/platform/content-model.ts) | content model module; static declarations include CefrLevel, isCefrLevel, compareCefr, prefix, IdPrefix, isContentId. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [daily-plan.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/lib/platform/daily-plan.ts) | daily plan module; static declarations include runs, LearningGoal, PlanInput, PlanItem, DailyPlan, weakSounds. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [engine-routing.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/lib/platform/engine-routing.ts) | engine routing module; static declarations include AiCapability, PlusSource, PlusRecord, isRecordActive, resolvePlus, hasPlus. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [fossilization.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/lib/platform/fossilization.ts) | fossilization module; static declarations include CardState, Grade, FossilArea, FossilError, FossilizationData, validateFossilError. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [goals.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/lib/platform/goals.ts) | goals module; static declarations include LearningGoal, PracticeFocus, isLearningGoal, parseGoals, toggleGoal, sameGoals. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [levels.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/lib/platform/levels.ts) | levels module; static declarations include CefrLevel, LevelInfo, examLine, LevelSkill, LevelSource, LevelPrefs. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [phrase-bank.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/lib/platform/phrase-bank.ts) | phrase bank module; static declarations include CefrLevel, CardState, Grade, PhraseSituation, PhraseKind, Phrase. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [placement.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/lib/platform/placement.ts) | placement module; static declarations include CefrLevel, Exercise, PlacementItem, PlacementScores, PlacementConfidence, PlacementEstimate. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [practice-day.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/lib/platform/practice-day.ts) | practice day module; static declarations include FossilError, Track, Phrase, PracticeListItem, SlangEntry, CardState. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [progress-model.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/lib/platform/progress-model.ts) | progress model module; static declarations include CefrLevel, ActivityKind, RecentResult, ProgressSummary, Activity, emptySummary. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [recordings.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/lib/platform/recordings.ts) | recordings module; static declarations include RecordingKind, Recording, RecordingIndex, isRecording, parseIndex, recordingId. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [sign-in-methods.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/lib/platform/sign-in-methods.ts) | sign in methods module; static declarations include SignInMethod, SignInSurface, isSignInMethod, methodLabel, continueLabel, providerButtons. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [srs.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/lib/platform/srs.ts) | srs module; static declarations include Grade, CardState, dayKey, addDays, isNew, isDue. No behavior is executed by this guide. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/lib/platform/vocal-tract/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/lib/platform/vocal-tract/)

Original upstream vocal tract shared/domain/service helpers. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [animate.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/lib/platform/vocal-tract/animate.ts) | animate module; static declarations include VocalTractParams, lerpParams, easeInOut, Keyframe, paramsAt, glottisPulse. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [articulation.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/lib/platform/vocal-tract/articulation.ts) | articulation module; static declarations include VocalTractParams, AccentVariant, SoundKind, SoundInfo, Place, Manner. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [codebook.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/lib/platform/vocal-tract/codebook.ts) | codebook module; static declarations include CodebookEntry. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [fit.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/lib/platform/vocal-tract/fit.ts) | fit module; static declarations include MovablePoints, ParamKey, Point, VocalTractParams, FitTargets, FitOptions. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [geometry.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/lib/platform/vocal-tract/geometry.ts) | geometry module; static declarations include Run, Subpath, LayerId, FillId, GlottisShape, VocalTractShape. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [index.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/lib/platform/vocal-tract/index.ts) | index implementation/helper module in the containing upstream reference component. | Preserved upstream reference; not integrated |
| [maeda.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/lib/platform/vocal-tract/maeda.ts) | maeda module; static declarations include VocalTractParams, ParamKey, paramsFromVector, paramsToVector, clampParam, Point. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [svg-path.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/lib/platform/vocal-tract/svg-path.ts) | svg path module; static declarations include Viewport, Box, createViewport, runCommands, subpathToSvg, subpathsToSvg. No behavior is executed by this guide. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/lib/runtime/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/lib/runtime/)

Original upstream runtime shared/domain/service helpers. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [request-runtime.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/lib/runtime/request-runtime.ts) | request runtime module; static declarations include AppRuntime, getRequestRuntime, getRuntimeFromUserAgent, getRequestRuntimeFromRequest, getAiEngineUrl, getCoachEngineUrl. No behavior is executed by this guide. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/lib/security/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/lib/security/)

Original upstream security shared/domain/service helpers. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [headers.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/lib/security/headers.ts) | headers module; static declarations include CspOptions, createNonce, buildCsp. No behavior is executed by this guide. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/lib/server/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/lib/server/)

Original upstream server shared/domain/service helpers. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [account-events.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/lib/server/account-events.ts) | account events module; static declarations include QueueInput, TemplateId, deviceLabel, deviceHash, SignInContext, SignInDeps. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [account.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/lib/server/account.ts) | account module; static declarations include Firestore, DeletionStep, plain, dumpDocument, exportAccount, DeletionDeps. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [admin-auth.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/lib/server/admin-auth.ts) | admin auth module; static declarations include isAdminAuthorized. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [ai-gate.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/lib/server/ai-gate.ts) | ai gate module; static declarations include AiCapability, BlockReason, DailyUsage, Offer, UsageRequest, blockedResponse. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [ai-route.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/lib/server/ai-route.ts) | ai route module; static declarations include AiAccess, AudioUpload, Granted, readCappedForm, readAudio, engineErrorResponse. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [ai-tts.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/lib/server/ai-tts.ts) | ai tts module; static declarations include speak. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [app-check.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/lib/server/app-check.ts) | app check module; static declarations include Env, AppCheckOutcome, AppCheckOptions, requireAppCheck. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [entitlement.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/lib/server/entitlement.ts) | entitlement module; static declarations include DocumentReference, DocumentData, Firestore, Transaction, DataTier, PlusRecord. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [env.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/lib/server/env.ts) | env module; static declarations include Env, isHostedCloud, flag, isAppCheckEnforced, appOrigin, firebaseProjectId. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [firebase.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/lib/server/firebase.ts) | firebase module; static declarations include that, App, Auth, Firestore, adminApp, db. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [http.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/lib/server/http.ts) | http module; static declarations include json, errorResponse, BodyTooLargeError, readTextCapped, readBytesCapped, readFormCapped. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [identity.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/lib/server/identity.ts) | identity module; static declarations include CloudIdentity, RequestIdentity, identify, cloudIdentity, verify, isRecentAuth. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [jobs.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/lib/server/jobs.ts) | jobs module; static declarations include DocumentSnapshot, Firestore, isJobAuthorized, DailyReport, remindersFor, runDailyJob. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [mcp-teacher-store.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/lib/server/mcp-teacher-store.ts) | mcp teacher store module; static declarations include takes, Track, PracticeListItem, RecordingMeta, CardState, Grade. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [me.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/lib/server/me.ts) | me module; static declarations include loadMe. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [newsletter.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/lib/server/newsletter.ts) | newsletter module; static declarations include ContactAttributes, Env, secret, confirmToken, verifyConfirmToken, doiTemplateId. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [packs.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/lib/server/packs.ts) | packs module; static declarations include CefrLevel, Exercise, GrammarPoint, PackContent, PackIndex, PackManifest. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [push-messages.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/lib/server/push-messages.ts) | push messages module; static declarations include PushDevice, PushCampaign, isExpoPushToken, parsePushDevice, isInstallId, buildExpoMessages. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [push.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/lib/server/push.ts) | push module; static declarations include PushCampaign, PushDevice, deviceRef, savePushDevice, removePushDevice, pushTokensFor. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [quota.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/lib/server/quota.ts) | quota module; static declarations include Firestore, AiCapability, DailyUsage, UsageRequest, utcDay, readUsage. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [rate-limit.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/lib/server/rate-limit.ts) | rate limit module; static declarations include Firestore, RateLimitRule, RateLimitResult, windowStart, rateLimitKey, decide. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [route.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/lib/server/route.ts) | Upstream HTTP route handler for server; not an active Eng Teacher endpoint. | Preserved upstream reference; not integrated |
| [support-http.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/lib/server/support-http.ts) | support http module; static declarations include SupportStatus, HandlerDeps, readBody, handleSupportPost, unauthorized, handleAdminSupportGet. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [support.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/lib/server/support.ts) | support module; static declarations include Firestore, SupportRequest, SupportStatus, SupportReply, StoredSupportRequest, SubmitMeta. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [sync-input.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/lib/server/sync-input.ts) | sync input module; static declarations include Activity, ActivityKind, Parsed, isKind, isRefId, parseActivity. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [sync.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/lib/server/sync.ts) | sync module; static declarations include Firestore, Activity, ProgressSummary, RateLimitRule, AttemptRecord, CardRecord. No behavior is executed by this guide. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/lib/server/billing/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/lib/server/billing/)

Original upstream billing shared/domain/service helpers. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [checkout.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/lib/server/billing/checkout.ts) | checkout module; static declarations include Firestore, PlusInterval, CheckoutErrorCode, CheckoutError, isPlusInterval, ensureCustomer. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [revenuecat-map.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/lib/server/billing/revenuecat-map.ts) | revenuecat map module; static declarations include RevenueCatEventType, RevenueCatEvent, isFirebaseUid, touchesPlus, RevenueCatEffect, revenueCatEffect. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [revenuecat.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/lib/server/billing/revenuecat.ts) | revenuecat module; static declarations include StoredPlusRecord, QueueInput, RevenueCatEvent, Env, isAuthorizedRevenueCat, RevenueCatApi. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [stripe-client.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/lib/server/billing/stripe-client.ts) | stripe client module; static declarations include isStripeKeyConfigured, stripe. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [stripe-map.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/lib/server/billing/stripe-map.ts) | stripe map module; static declarations include PlusInterval, StripeProductLike, StripePriceLike, StripeSubscriptionLike, idOf, firstItem. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [stripe-webhook.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/lib/server/billing/stripe-webhook.ts) | stripe webhook module; static declarations include StoredPlusRecord, QueueInput, StripeSubscriptionLike, StripeEventLike, StripeApi, WebhookResult. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [webhook-events.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/lib/server/billing/webhook-events.ts) | webhook events module; static declarations include Firestore, Transaction, WebhookSource, eventRef, seenInTx, recordInTx. No behavior is executed by this guide. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/lib/server/codes/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/lib/server/codes/)

Original upstream codes shared/domain/service helpers. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [http.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/lib/server/codes/http.ts) | http module; static declarations include error, readBody, handleAdminCodesGet, handleAdminCodesPost, handleAdminCodesPatch, account. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [logic.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/lib/server/codes/logic.ts) | logic module; static declarations include FriendCode, FriendCodeRedemption, describeGrantDuration, normalizeCode, isWellFormedCode, hashCode. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [store.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/lib/server/codes/store.ts) | store module; static declarations include Firestore, PlusSource, StoredPlusRecord, CreateCodeInput, FriendCode, FriendCodeRedemption. No behavior is executed by this guide. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/lib/server/email/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/lib/server/email/)

Original upstream email shared/domain/service helpers. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [brevo.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/lib/server/email/brevo.ts) | brevo module; static declarations include Mailbox, brevoApiBase, Env, EmailErrorKind, EmailError, OutgoingEmail. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [layout.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/lib/server/email/layout.ts) | layout module; static declarations include EmailCategory, EmailList, RenderedEmail, escapeHtml, cleanText, firstName. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [queue.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/lib/server/email/queue.ts) | queue module; static declarations include Firestore, Transaction, BrevoDeps, TemplateId, TemplateProps, QueuedProps. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [senders.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/lib/server/email/senders.ts) | senders module; static declarations include Mailbox, isEmailAddress, parseMailbox, senders, supportInbox. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [unsubscribe.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/lib/server/email/unsubscribe.ts) | unsubscribe module; static declarations include Env, UnsubscribeNotConfiguredError, secretFrom, sign, unsubscribeToken, verifyUnsubscribeToken. No behavior is executed by this guide. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/lib/server/email/templates/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/lib/server/email/templates/)

Original upstream templates shared/domain/service helpers. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [account.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/lib/server/email/templates/account.ts) | account module; static declarations include of, RenderedEmail, lifetime, WelcomeProps, renderWelcome, VerifyEmailProps. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [billing.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/lib/server/email/templates/billing.ts) | billing module; static declarations include RenderedEmail, BillingStore, planLabel, priceLabel, manageLine, PlusWelcomeProps. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [engagement.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/lib/server/email/templates/engagement.ts) | engagement module; static declarations include RenderedEmail, StreakAtRiskProps, renderStreakAtRisk, WeeklySummaryProps, renderWeeklySummary, BadgeEarnedProps. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [index.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/lib/server/email/templates/index.ts) | index module; static declarations include TemplateProps, TemplateId, TemplateEntry, isTemplateId, renderTemplate, renderFixture. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [security.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/lib/server/email/templates/security.ts) | security module; static declarations include RenderedEmail, McpAuthorizedProps, renderMcpAuthorized, DevicePairedProps, renderDevicePaired, SuspiciousActivityProps. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [support.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/lib/server/email/templates/support.ts) | support module; static declarations include RenderedEmail, SupportRequestProps, SupportReplyProps, paragraphsOf, renderSupportRequest, renderSupportReply. No behavior is executed by this guide. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/lib/server/engines/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/lib/server/engines/)

Original upstream engines shared/domain/service helpers. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [audio-duration.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/lib/server/engines/audio-duration.ts) | audio duration module; static declarations include ascii, view, WavFormat, wavDuration, opusPacketSeconds, oggOpusDuration. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [audio.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/lib/server/engines/audio.ts) | audio module; static declarations include AudioContainer, AudioUpload, AudioCheck, wavSeconds, estimateSeconds, checkAudio. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [gemini.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/lib/server/engines/gemini.ts) | gemini module; static declarations include GeminiPart, GeminiContent, GeminiRequest, isGeminiConfigured, viaVertex, GeminiError. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [google-auth.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/lib/server/engines/google-auth.ts) | google auth module; static declarations include accessToken, expiryOf, idToken, engineNeedsIdToken. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [index.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/lib/server/engines/index.ts) | index module; static declarations include per, AudioUpload, CoachScenario, CoachTurn, GrammarCandidate, GrammarIssue. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [prompts.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/lib/server/engines/prompts.ts) | prompts module; static declarations include CefrLevel, PlacementEstimate, CoachScenario, CoachTurn, coachSystemPrompt, cleanLearnerText. No behavior is executed by this guide. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/src/types/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/types/)

Original upstream types source/configuration collection. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [electron.d.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/src/types/electron.d.ts) | electron.d module; static declarations include DesktopRuntimeLocation, DesktopRuntimeDetails, DesktopSetupState, Window. No behavior is executed by this guide. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/store/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/store/)

Original upstream store source/configuration collection. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [.gitignore](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/store/.gitignore) | Original component exclusions for generated outputs, dependencies and local configuration. | Preserved upstream reference; not integrated |
| [APP_STORE.md](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/store/APP_STORE.md) | Documentation/research record for APP STORE; requirements and historical observations are not automatically implemented behavior. | Preserved upstream reference; not integrated |
| [README.md](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/store/README.md) | Containing collection/component introduction, navigation and documented usage; retain the scope of the original project. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/store/screenshot-studio/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/store/screenshot-studio/)

Original upstream screenshot studio source/configuration collection. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [.gitignore](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/store/screenshot-studio/.gitignore) | Original component exclusions for generated outputs, dependencies and local configuration. | Preserved upstream reference; not integrated |
| [index.html](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/store/screenshot-studio/index.html) | index presentation/page/browser-install resource for the containing component. | Preserved upstream reference; not integrated |
| [package-lock.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/store/screenshot-studio/package-lock.json) | Resolved component dependency versions/integrity; not an implemented product feature. | Preserved upstream reference; not integrated |
| [package.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/store/screenshot-studio/package.json) | Containing component dependency/build/test declarations; consult its scope before installing. | Preserved upstream reference; not integrated |
| [tsconfig.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/store/screenshot-studio/tsconfig.json) | Structured tsconfig content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [vite.config.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/store/screenshot-studio/vite.config.ts) | vite.config build/runtime/tool configuration for the containing component. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/store/screenshot-studio/config/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/store/screenshot-studio/config/)

Original upstream config source/configuration collection. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [slides.config.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/store/screenshot-studio/config/slides.config.json) | Structured slides.config content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/store/screenshot-studio/scripts/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/store/screenshot-studio/scripts/)

Original upstream scripts source/configuration collection. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [copy-assets.mjs](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/store/screenshot-studio/scripts/copy-assets.mjs) | copy assets module; static declarations include copyAssets. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [export.mjs](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/store/screenshot-studio/scripts/export.mjs) | export module; static declarations include parseArgs, captureState, main. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [png.mjs](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/store/screenshot-studio/scripts/png.mjs) | png module; static declarations include 2, writeOpaquePng. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [raw-files.d.mts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/store/screenshot-studio/scripts/raw-files.d.mts) | raw files.d implementation/helper module in the containing upstream reference component. | Preserved upstream reference; not integrated |
| [raw-files.mjs](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/store/screenshot-studio/scripts/raw-files.mjs) | raw files module; static declarations include readPngSize, rawManifest. No behavior is executed by this guide. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/store/screenshot-studio/src/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/store/screenshot-studio/src/)

Original upstream src source/configuration collection. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [config-io.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/store/screenshot-studio/src/config-io.ts) | config io build/runtime/tool configuration for the containing component. | Preserved upstream reference; not integrated |
| [config.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/store/screenshot-studio/src/config.ts) | config build/runtime/tool configuration for the containing component. | Preserved upstream reference; not integrated |
| [dashboard.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/store/screenshot-studio/src/dashboard.tsx) | dashboard module; static declarations include RawManifest, Dashboard. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [device-sizes.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/store/screenshot-studio/src/device-sizes.json) | Structured device sizes content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [devices.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/store/screenshot-studio/src/devices.ts) | devices module; static declarations include Device, deviceById, layoutFor. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [main.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/store/screenshot-studio/src/main.tsx) | main implementation/helper module in the containing upstream reference component. | Preserved upstream reference; not integrated |
| [render-view.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/store/screenshot-studio/src/render-view.tsx) | render view module; static declarations include RawManifest, RenderView. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [slide.tsx](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/store/screenshot-studio/src/slide.tsx) | slide module; static declarations include Device, Caption, Wallpaper, Screen, SlideCanvas, IapReviewCanvas. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [styles.css](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/store/screenshot-studio/src/styles.css) | styles presentation/page/browser-install resource for the containing component. | Preserved upstream reference; not integrated |
| [theme.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/store/screenshot-studio/src/theme.ts) | theme module; static declarations include Ground, groundColors. No behavior is executed by this guide. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/store/screenshots/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/store/screenshots/)

Original screenshots assets, models or packaging resources; retain associated notices. Archived reference; not an active Eng Teacher feature or dependency.

Contains the subfolders listed in their own sections; no tracked files directly in this folder.

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/store/screenshots/raw/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/store/screenshots/raw/)

Original raw assets, models or packaging resources; retain associated notices. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [coach.png](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/store/screenshots/raw/coach.png) | coach visual/font/icon resource; preserve applicable asset attribution and review rights before reuse. | Preserved upstream reference; not integrated |
| [flashcards.png](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/store/screenshots/raw/flashcards.png) | flashcards visual/font/icon resource; preserve applicable asset attribution and review rights before reuse. | Preserved upstream reference; not integrated |
| [grammar-builder.png](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/store/screenshots/raw/grammar-builder.png) | grammar builder visual/font/icon resource; preserve applicable asset attribution and review rights before reuse. | Preserved upstream reference; not integrated |
| [mouth-map.png](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/store/screenshots/raw/mouth-map.png) | mouth map visual/font/icon resource; preserve applicable asset attribution and review rights before reuse. | Preserved upstream reference; not integrated |
| [own-server.png](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/store/screenshots/raw/own-server.png) | own server visual/font/icon resource; preserve applicable asset attribution and review rights before reuse. | Preserved upstream reference; not integrated |
| [plus.png](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/store/screenshots/raw/plus.png) | plus visual/font/icon resource; preserve applicable asset attribution and review rights before reuse. | Preserved upstream reference; not integrated |
| [sounds-to-fix.png](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/store/screenshots/raw/sounds-to-fix.png) | sounds to fix visual/font/icon resource; preserve applicable asset attribution and review rights before reuse. | Preserved upstream reference; not integrated |
| [streaks.png](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/store/screenshots/raw/streaks.png) | streaks visual/font/icon resource; preserve applicable asset attribution and review rights before reuse. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/tests/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/tests/)

Upstream verification scenarios/fixtures for tests. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [package.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/tests/package.json) | Containing component dependency/build/test declarations; consult its scope before installing. | Preserved upstream reference; not integrated |
| [register.mjs](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/tests/register.mjs) | Regression/scenario definitions for register; execution and test boundaries are recorded separately. | Preserved upstream reference; not integrated |
| [tsconfig.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/tests/tsconfig.json) | Verification fixture for tsconfig; test data/result presence is not a product acceptance claim. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/tests/auth/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/tests/auth/)

Upstream verification scenarios/fixtures for auth. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [auth-errors.test.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/tests/auth/auth-errors.test.ts) | Regression/scenario definitions for auth errors.test; execution and test boundaries are recorded separately. | Preserved upstream reference; not integrated |
| [route-gate.test.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/tests/auth/route-gate.test.ts) | Regression/scenario definitions for route gate.test; execution and test boundaries are recorded separately. | Preserved upstream reference; not integrated |
| [safe-next.test.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/tests/auth/safe-next.test.ts) | Regression/scenario definitions for safe next.test; execution and test boundaries are recorded separately. | Preserved upstream reference; not integrated |
| [session-order.test.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/tests/auth/session-order.test.ts) | Regression/scenario definitions for session order.test; execution and test boundaries are recorded separately. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/tests/cloud/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/tests/cloud/)

Upstream verification scenarios/fixtures for cloud. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [attempt-input.test.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/tests/cloud/attempt-input.test.ts) | Regression/scenario definitions for attempt input.test; execution and test boundaries are recorded separately. | Preserved upstream reference; not integrated |
| [profile-input.test.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/tests/cloud/profile-input.test.ts) | Regression/scenario definitions for profile input.test; execution and test boundaries are recorded separately. | Preserved upstream reference; not integrated |
| [progress-logic.test.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/tests/cloud/progress-logic.test.ts) | Regression/scenario definitions for progress logic.test; execution and test boundaries are recorded separately. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/tests/content/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/tests/content/)

Upstream verification scenarios/fixtures for content. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [articulation.test.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/tests/content/articulation.test.ts) | Regression/scenario definitions for articulation.test; execution and test boundaries are recorded separately. | Preserved upstream reference; not integrated |
| [packs.test.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/tests/content/packs.test.ts) | Regression/scenario definitions for packs.test; execution and test boundaries are recorded separately. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/tests/desktop/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/tests/desktop/)

Upstream verification scenarios/fixtures for desktop. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [update-policy.test.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/tests/desktop/update-policy.test.ts) | Regression/scenario definitions for update policy.test; execution and test boundaries are recorded separately. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/tests/e2e/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/tests/e2e/)

Upstream verification scenarios/fixtures for e2e. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [auth-providers.spec.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/tests/e2e/auth-providers.spec.ts) | Regression/scenario definitions for auth providers.spec; execution and test boundaries are recorded separately. | Preserved upstream reference; not integrated |
| [newsletter.spec.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/tests/e2e/newsletter.spec.ts) | Regression/scenario definitions for newsletter.spec; execution and test boundaries are recorded separately. | Preserved upstream reference; not integrated |
| [oauth-consent.spec.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/tests/e2e/oauth-consent.spec.ts) | Regression/scenario definitions for oauth consent.spec; execution and test boundaries are recorded separately. | Preserved upstream reference; not integrated |
| [smoke.spec.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/tests/e2e/smoke.spec.ts) | Regression/scenario definitions for smoke.spec; execution and test boundaries are recorded separately. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/tests/e2e/support/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/tests/e2e/support/)

Upstream verification scenarios/fixtures for support. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [brevo-stub.mjs](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/tests/e2e/support/brevo-stub.mjs) | Regression/scenario definitions for brevo stub; execution and test boundaries are recorded separately. | Preserved upstream reference; not integrated |
| [fixtures.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/tests/e2e/support/fixtures.ts) | Regression/scenario definitions for fixtures; execution and test boundaries are recorded separately. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/tests/email/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/tests/email/)

Upstream verification scenarios/fixtures for email. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [brevo-base.test.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/tests/email/brevo-base.test.ts) | Regression/scenario definitions for brevo base.test; execution and test boundaries are recorded separately. | Preserved upstream reference; not integrated |
| [render.test.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/tests/email/render.test.ts) | Regression/scenario definitions for render.test; execution and test boundaries are recorded separately. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/tests/mobile/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/tests/mobile/)

Upstream verification scenarios/fixtures for mobile. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [sync-contract.test.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/tests/mobile/sync-contract.test.ts) | Regression/scenario definitions for sync contract.test; execution and test boundaries are recorded separately. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/tests/pairing/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/tests/pairing/)

Upstream verification scenarios/fixtures for pairing. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [address.test.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/tests/pairing/address.test.ts) | Regression/scenario definitions for address.test; execution and test boundaries are recorded separately. | Preserved upstream reference; not integrated |
| [discovery.test.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/tests/pairing/discovery.test.ts) | Regression/scenario definitions for discovery.test; execution and test boundaries are recorded separately. | Preserved upstream reference; not integrated |
| [errors.test.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/tests/pairing/errors.test.ts) | Regression/scenario definitions for errors.test; execution and test boundaries are recorded separately. | Preserved upstream reference; not integrated |
| [protocol.test.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/tests/pairing/protocol.test.ts) | Regression/scenario definitions for protocol.test; execution and test boundaries are recorded separately. | Preserved upstream reference; not integrated |
| [token-exchange.test.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/tests/pairing/token-exchange.test.ts) | Regression/scenario definitions for token exchange.test; execution and test boundaries are recorded separately. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/tests/platform/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/tests/platform/)

Upstream verification scenarios/fixtures for platform. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [adaptive-placement.test.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/tests/platform/adaptive-placement.test.ts) | Regression/scenario definitions for adaptive placement.test; execution and test boundaries are recorded separately. | Preserved upstream reference; not integrated |
| [content-model.test.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/tests/platform/content-model.test.ts) | Regression/scenario definitions for content model.test; execution and test boundaries are recorded separately. | Preserved upstream reference; not integrated |
| [daily-plan.test.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/tests/platform/daily-plan.test.ts) | Regression/scenario definitions for daily plan.test; execution and test boundaries are recorded separately. | Preserved upstream reference; not integrated |
| [drift.test.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/tests/platform/drift.test.ts) | Regression/scenario definitions for drift.test; execution and test boundaries are recorded separately. | Preserved upstream reference; not integrated |
| [engine-routing.test.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/tests/platform/engine-routing.test.ts) | Regression/scenario definitions for engine routing.test; execution and test boundaries are recorded separately. | Preserved upstream reference; not integrated |
| [fossilization.test.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/tests/platform/fossilization.test.ts) | Regression/scenario definitions for fossilization.test; execution and test boundaries are recorded separately. | Preserved upstream reference; not integrated |
| [goals.test.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/tests/platform/goals.test.ts) | Regression/scenario definitions for goals.test; execution and test boundaries are recorded separately. | Preserved upstream reference; not integrated |
| [levels.test.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/tests/platform/levels.test.ts) | Regression/scenario definitions for levels.test; execution and test boundaries are recorded separately. | Preserved upstream reference; not integrated |
| [phrase-bank.test.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/tests/platform/phrase-bank.test.ts) | Regression/scenario definitions for phrase bank.test; execution and test boundaries are recorded separately. | Preserved upstream reference; not integrated |
| [placement.test.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/tests/platform/placement.test.ts) | Regression/scenario definitions for placement.test; execution and test boundaries are recorded separately. | Preserved upstream reference; not integrated |
| [practice-day.test.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/tests/platform/practice-day.test.ts) | Regression/scenario definitions for practice day.test; execution and test boundaries are recorded separately. | Preserved upstream reference; not integrated |
| [progress-model.test.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/tests/platform/progress-model.test.ts) | Regression/scenario definitions for progress model.test; execution and test boundaries are recorded separately. | Preserved upstream reference; not integrated |
| [recordings.test.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/tests/platform/recordings.test.ts) | Regression/scenario definitions for recordings.test; execution and test boundaries are recorded separately. | Preserved upstream reference; not integrated |
| [sign-in-methods.test.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/tests/platform/sign-in-methods.test.ts) | Regression/scenario definitions for sign in methods.test; execution and test boundaries are recorded separately. | Preserved upstream reference; not integrated |
| [srs.test.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/tests/platform/srs.test.ts) | Regression/scenario definitions for srs.test; execution and test boundaries are recorded separately. | Preserved upstream reference; not integrated |
| [vocal-tract.test.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/tests/platform/vocal-tract.test.ts) | Regression/scenario definitions for vocal tract.test; execution and test boundaries are recorded separately. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/tests/platform/fixtures/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/tests/platform/fixtures/)

Upstream verification scenarios/fixtures for fixtures. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [vocaltract-reference.json](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/tests/platform/fixtures/vocaltract-reference.json) | Verification fixture for vocaltract reference; test data/result presence is not a product acceptance claim. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/tests/release/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/tests/release/)

Upstream verification scenarios/fixtures for release. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [bump.test.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/tests/release/bump.test.ts) | Regression/scenario definitions for bump.test; execution and test boundaries are recorded separately. | Preserved upstream reference; not integrated |
| [lib.test.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/tests/release/lib.test.ts) | Regression/scenario definitions for lib.test; execution and test boundaries are recorded separately. | Preserved upstream reference; not integrated |
| [manifest.test.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/tests/release/manifest.test.ts) | Regression/scenario definitions for manifest.test; execution and test boundaries are recorded separately. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/tests/rules/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/tests/rules/)

Upstream verification scenarios/fixtures for rules. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [firestore.test.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/tests/rules/firestore.test.ts) | Regression/scenario definitions for firestore.test; execution and test boundaries are recorded separately. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/tests/server/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/tests/server/)

Upstream verification scenarios/fixtures for server. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [ai-route-form.test.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/tests/server/ai-route-form.test.ts) | Regression/scenario definitions for ai route form.test; execution and test boundaries are recorded separately. | Preserved upstream reference; not integrated |
| [billing-map.test.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/tests/server/billing-map.test.ts) | Regression/scenario definitions for billing map.test; execution and test boundaries are recorded separately. | Preserved upstream reference; not integrated |
| [guards.test.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/tests/server/guards.test.ts) | Regression/scenario definitions for guards.test; execution and test boundaries are recorded separately. | Preserved upstream reference; not integrated |
| [push.test.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/tests/server/push.test.ts) | Regression/scenario definitions for push.test; execution and test boundaries are recorded separately. | Preserved upstream reference; not integrated |
| [support-and-codes.test.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/tests/server/support-and-codes.test.ts) | Regression/scenario definitions for support and codes.test; execution and test boundaries are recorded separately. | Preserved upstream reference; not integrated |
| [teacher.test.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/tests/server/teacher.test.ts) | Regression/scenario definitions for teacher.test; execution and test boundaries are recorded separately. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/tests/server/emulator/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/tests/server/emulator/)

Upstream verification scenarios/fixtures for emulator. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [account-mail-jobs.test.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/tests/server/emulator/account-mail-jobs.test.ts) | Regression/scenario definitions for account mail jobs.test; execution and test boundaries are recorded separately. | Preserved upstream reference; not integrated |
| [firestore-counter.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/tests/server/emulator/firestore-counter.ts) | Regression/scenario definitions for firestore counter; execution and test boundaries are recorded separately. | Preserved upstream reference; not integrated |
| [helpers.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/tests/server/emulator/helpers.ts) | Regression/scenario definitions for helpers; execution and test boundaries are recorded separately. | Preserved upstream reference; not integrated |
| [mcp-teacher.test.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/tests/server/emulator/mcp-teacher.test.ts) | Regression/scenario definitions for mcp teacher.test; execution and test boundaries are recorded separately. | Preserved upstream reference; not integrated |
| [mcp.test.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/tests/server/emulator/mcp.test.ts) | Regression/scenario definitions for mcp.test; execution and test boundaries are recorded separately. | Preserved upstream reference; not integrated |
| [session-cost.test.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/tests/server/emulator/session-cost.test.ts) | Regression/scenario definitions for session cost.test; execution and test boundaries are recorded separately. | Preserved upstream reference; not integrated |
| [support-and-codes.test.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/tests/server/emulator/support-and-codes.test.ts) | Regression/scenario definitions for support and codes.test; execution and test boundaries are recorded separately. | Preserved upstream reference; not integrated |
| [sync-and-gates.test.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/tests/server/emulator/sync-and-gates.test.ts) | Regression/scenario definitions for sync and gates.test; execution and test boundaries are recorded separately. | Preserved upstream reference; not integrated |
| [webhooks.test.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/tests/server/emulator/webhooks.test.ts) | Regression/scenario definitions for webhooks.test; execution and test boundaries are recorded separately. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/tests/server/fixtures/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/tests/server/fixtures/)

Upstream verification scenarios/fixtures for fixtures. Archived reference; not an active Eng Teacher feature or dependency.

Contains the subfolders listed in their own sections; no tracked files directly in this folder.

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/tests/server/fixtures/audio/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/tests/server/fixtures/audio/)

Upstream verification scenarios/fixtures for audio. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [long-45s-low-bitrate.m4a](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/tests/server/fixtures/audio/long-45s-low-bitrate.m4a) | Verification fixture for long 45s low bitrate; test data/result presence is not a product acceptance claim. | Preserved upstream reference; not integrated |
| [long-45s-low-bitrate.webm](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/tests/server/fixtures/audio/long-45s-low-bitrate.webm) | Verification fixture for long 45s low bitrate; test data/result presence is not a product acceptance claim. | Preserved upstream reference; not integrated |
| [speech-3s-fragmented.m4a](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/tests/server/fixtures/audio/speech-3s-fragmented.m4a) | Verification fixture for speech 3s fragmented; test data/result presence is not a product acceptance claim. | Preserved upstream reference; not integrated |
| [speech-3s-live.webm](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/tests/server/fixtures/audio/speech-3s-live.webm) | Verification fixture for speech 3s live; test data/result presence is not a product acceptance claim. | Preserved upstream reference; not integrated |
| [speech-3s.m4a](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/tests/server/fixtures/audio/speech-3s.m4a) | Verification fixture for speech 3s; test data/result presence is not a product acceptance claim. | Preserved upstream reference; not integrated |
| [speech-3s.mp3](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/tests/server/fixtures/audio/speech-3s.mp3) | Verification fixture for speech 3s; test data/result presence is not a product acceptance claim. | Preserved upstream reference; not integrated |
| [speech-3s.ogg](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/tests/server/fixtures/audio/speech-3s.ogg) | Verification fixture for speech 3s; test data/result presence is not a product acceptance claim. | Preserved upstream reference; not integrated |
| [speech-3s.webm](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/tests/server/fixtures/audio/speech-3s.webm) | Verification fixture for speech 3s; test data/result presence is not a product acceptance claim. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/Cadence-main/tests/web/](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/tests/web/)

Upstream verification scenarios/fixtures for web. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [content-fixtures.test.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/tests/web/content-fixtures.test.ts) | Regression/scenario definitions for content fixtures.test; execution and test boundaries are recorded separately. | Preserved upstream reference; not integrated |
| [password-rules.test.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/tests/web/password-rules.test.ts) | Regression/scenario definitions for password rules.test; execution and test boundaries are recorded separately. | Preserved upstream reference; not integrated |
| [security-headers.test.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/tests/web/security-headers.test.ts) | Regression/scenario definitions for security headers.test; execution and test boundaries are recorded separately. | Preserved upstream reference; not integrated |
| [sound-practice.test.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/tests/web/sound-practice.test.ts) | Regression/scenario definitions for sound practice.test; execution and test boundaries are recorded separately. | Preserved upstream reference; not integrated |
| [srs.test.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/tests/web/srs.test.ts) | Regression/scenario definitions for srs.test; execution and test boundaries are recorded separately. | Preserved upstream reference; not integrated |
| [sync-logic.test.ts](../../AnalyseFuture/original-projects/reference-sources/Cadence-main/tests/web/sync-logic.test.ts) | Regression/scenario definitions for sync logic.test; execution and test boundaries are recorded separately. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/talking-avatar-master/](../../AnalyseFuture/original-projects/reference-sources/talking-avatar-master/)

Preserved Talking Avatar browser SDK, model, assets and tests; study/evidence only, not an integrated product dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [.gitignore](../../AnalyseFuture/original-projects/reference-sources/talking-avatar-master/.gitignore) | Original component exclusions for generated outputs, dependencies and local configuration. | Preserved upstream reference; not integrated |
| [CHANGELOG.md](../../AnalyseFuture/original-projects/reference-sources/talking-avatar-master/CHANGELOG.md) | Documentation/research record for CHANGELOG; requirements and historical observations are not automatically implemented behavior. | Preserved upstream reference; not integrated |
| [CONTRIBUTING.md](../../AnalyseFuture/original-projects/reference-sources/talking-avatar-master/CONTRIBUTING.md) | Documentation/research record for CONTRIBUTING; requirements and historical observations are not automatically implemented behavior. | Preserved upstream reference; not integrated |
| [LICENSE](../../AnalyseFuture/original-projects/reference-sources/talking-avatar-master/LICENSE) | Licence/attribution record for the related component/assets; preserve notices and review the exact distribution rights. | Preserved upstream reference; not integrated |
| [README.md](../../AnalyseFuture/original-projects/reference-sources/talking-avatar-master/README.md) | Containing collection/component introduction, navigation and documented usage; retain the scope of the original project. | Preserved upstream reference; not integrated |
| [SECURITY.md](../../AnalyseFuture/original-projects/reference-sources/talking-avatar-master/SECURITY.md) | Documentation/research record for SECURITY; requirements and historical observations are not automatically implemented behavior. | Preserved upstream reference; not integrated |
| [package-lock.json](../../AnalyseFuture/original-projects/reference-sources/talking-avatar-master/package-lock.json) | Resolved component dependency versions/integrity; not an implemented product feature. | Preserved upstream reference; not integrated |
| [package.json](../../AnalyseFuture/original-projects/reference-sources/talking-avatar-master/package.json) | Containing component dependency/build/test declarations; consult its scope before installing. | Preserved upstream reference; not integrated |
| [tsconfig.build.json](../../AnalyseFuture/original-projects/reference-sources/talking-avatar-master/tsconfig.build.json) | Structured tsconfig.build content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [tsconfig.json](../../AnalyseFuture/original-projects/reference-sources/talking-avatar-master/tsconfig.json) | Structured tsconfig content, contract, metadata or component configuration in this directory. | Preserved upstream reference; not integrated |
| [vite.config.ts](../../AnalyseFuture/original-projects/reference-sources/talking-avatar-master/vite.config.ts) | vite.config build/runtime/tool configuration for the containing component. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/talking-avatar-master/.github/](../../AnalyseFuture/original-projects/reference-sources/talking-avatar-master/.github/)

Original upstream automation or contribution configuration. Archived reference; not an active Eng Teacher feature or dependency.

Contains the subfolders listed in their own sections; no tracked files directly in this folder.

## [AnalyseFuture/original-projects/reference-sources/talking-avatar-master/.github/workflows/](../../AnalyseFuture/original-projects/reference-sources/talking-avatar-master/.github/workflows/)

Original upstream automation or contribution configuration. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [ci.yml](../../AnalyseFuture/original-projects/reference-sources/talking-avatar-master/.github/workflows/ci.yml) | Declarative ci workflow/scenario/build configuration for the containing component. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/talking-avatar-master/avatars/](../../AnalyseFuture/original-projects/reference-sources/talking-avatar-master/avatars/)

Original avatars assets, models or packaging resources; retain associated notices. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [LICENSE](../../AnalyseFuture/original-projects/reference-sources/talking-avatar-master/avatars/LICENSE) | Licence/attribution record for the related component/assets; preserve notices and review the exact distribution rights. | Preserved upstream reference; not integrated |
| [female.glb](../../AnalyseFuture/original-projects/reference-sources/talking-avatar-master/avatars/female.glb) | female model/binary resource; retained as an artifact, not evidence of active inference/integration. | Preserved upstream reference; not integrated |
| [male.glb](../../AnalyseFuture/original-projects/reference-sources/talking-avatar-master/avatars/male.glb) | male model/binary resource; retained as an artifact, not evidence of active inference/integration. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/talking-avatar-master/model/](../../AnalyseFuture/original-projects/reference-sources/talking-avatar-master/model/)

Original model assets, models or packaging resources; retain associated notices. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [viseme-model.bin](../../AnalyseFuture/original-projects/reference-sources/talking-avatar-master/model/viseme-model.bin) | viseme model model/binary resource; retained as an artifact, not evidence of active inference/integration. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/talking-avatar-master/src/](../../AnalyseFuture/original-projects/reference-sources/talking-avatar-master/src/)

Original upstream src source/configuration collection. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [TalkingAvatar.ts](../../AnalyseFuture/original-projects/reference-sources/talking-avatar-master/src/TalkingAvatar.ts) | Talking Avatar module; static declarations include Segment, Mode, MorphTargetMap, VisemeEvent, VisemeModel, TalkingAvatarOptions. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [coarticulation.ts](../../AnalyseFuture/original-projects/reference-sources/talking-avatar-master/src/coarticulation.ts) | coarticulation module; static declarations include Segment, buildSegments, activation, mouthAt, isSpeakingAt. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [index.ts](../../AnalyseFuture/original-projects/reference-sources/talking-avatar-master/src/index.ts) | index module; static declarations include AvatarStatus, TalkingAvatarOptions. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [react.tsx](../../AnalyseFuture/original-projects/reference-sources/talking-avatar-master/src/react.tsx) | react module; static declarations include CSSProperties, AvatarStatus, TalkingAvatarViewProps, TalkingAvatarView. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [renderer.ts](../../AnalyseFuture/original-projects/reference-sources/talking-avatar-master/src/renderer.ts) | renderer module; static declarations include MorphTargetMap, Mode, faceCenter, refineMaterial, disposeObject, AvatarRenderer. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [resampler.ts](../../AnalyseFuture/original-projects/reference-sources/talking-avatar-master/src/resampler.ts) | resampler module; static declarations include Resampler. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [visemeDetector.ts](../../AnalyseFuture/original-projects/reference-sources/talking-avatar-master/src/visemeDetector.ts) | viseme Detector module; static declarations include VisemeModel, VisemeEvent, VisemeDetector. No behavior is executed by this guide. | Preserved upstream reference; not integrated |
| [visemeModel.ts](../../AnalyseFuture/original-projects/reference-sources/talking-avatar-master/src/visemeModel.ts) | viseme Model module; static declarations include VisemeModel, parseVisemeModel, melFilterbank, fft, matAdd, VisemeStream. No behavior is executed by this guide. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/talking-avatar-master/test/](../../AnalyseFuture/original-projects/reference-sources/talking-avatar-master/test/)

Upstream verification scenarios/fixtures for test. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [coarticulation.test.ts](../../AnalyseFuture/original-projects/reference-sources/talking-avatar-master/test/coarticulation.test.ts) | Regression/scenario definitions for coarticulation.test; execution and test boundaries are recorded separately. | Preserved upstream reference; not integrated |
| [helpers.ts](../../AnalyseFuture/original-projects/reference-sources/talking-avatar-master/test/helpers.ts) | Regression/scenario definitions for helpers; execution and test boundaries are recorded separately. | Preserved upstream reference; not integrated |
| [resampler.test.ts](../../AnalyseFuture/original-projects/reference-sources/talking-avatar-master/test/resampler.test.ts) | Regression/scenario definitions for resampler.test; execution and test boundaries are recorded separately. | Preserved upstream reference; not integrated |
| [visemeDetector.test.ts](../../AnalyseFuture/original-projects/reference-sources/talking-avatar-master/test/visemeDetector.test.ts) | Regression/scenario definitions for viseme Detector.test; execution and test boundaries are recorded separately. | Preserved upstream reference; not integrated |
| [visemeModel.test.ts](../../AnalyseFuture/original-projects/reference-sources/talking-avatar-master/test/visemeModel.test.ts) | Regression/scenario definitions for viseme Model.test; execution and test boundaries are recorded separately. | Preserved upstream reference; not integrated |

## [AnalyseFuture/original-projects/reference-sources/talking-avatar-master/test/fixtures/](../../AnalyseFuture/original-projects/reference-sources/talking-avatar-master/test/fixtures/)

Upstream verification scenarios/fixtures for fixtures. Archived reference; not an active Eng Teacher feature or dependency.

| File | Purpose | Status |
| --- | --- | --- |
| [parity-audio.f32](../../AnalyseFuture/original-projects/reference-sources/talking-avatar-master/test/fixtures/parity-audio.f32) | Verification fixture for parity audio; test data/result presence is not a product acceptance claim. | Preserved upstream reference; not integrated |
| [parity-visemes.u8](../../AnalyseFuture/original-projects/reference-sources/talking-avatar-master/test/fixtures/parity-visemes.u8) | Verification fixture for parity visemes; test data/result presence is not a product acceptance claim. | Preserved upstream reference; not integrated |

## [AnalyseFuture/recovery/](../../AnalyseFuture/recovery/)

Historical migration, preservation, feature, inventory, security and validation evidence.

Contains the subfolders listed in their own sections; no tracked files directly in this folder.

## [AnalyseFuture/recovery/continuation/](../../AnalyseFuture/recovery/continuation/)

Historical recovery progress and continuation instructions; consult the current root handoff before executing old tasks.

| File | Purpose | Status |
| --- | --- | --- |
| [NEXT_DEVELOPER_INSTRUCTIONS.txt](../../AnalyseFuture/recovery/continuation/NEXT_DEVELOPER_INSTRUCTIONS.txt) | Recorded next developer instructions audit, mapping, inventory or validation artifact; retain its dated scope. | Historical/planning evidence; not active application |
| [WORK_PROGRESS.txt](../../AnalyseFuture/recovery/continuation/WORK_PROGRESS.txt) | Recorded work progress audit, mapping, inventory or validation artifact; retain its dated scope. | Historical/planning evidence; not active application |

## [AnalyseFuture/recovery/features/](../../AnalyseFuture/recovery/features/)

Recorded feature/duplicate and semantic audits; source presence is not proof of integrated or live functionality.

| File | Purpose | Status |
| --- | --- | --- |
| [CADENCE_WEB_SEMANTIC_AUDIT.json](../../AnalyseFuture/recovery/features/CADENCE_WEB_SEMANTIC_AUDIT.json) | Recorded cadence web semantic audit audit, mapping, inventory or validation artifact; retain its dated scope. | Historical/planning evidence; not active application |
| [CLIENTS_AND_AVATAR_SEMANTIC_AUDIT.json](../../AnalyseFuture/recovery/features/CLIENTS_AND_AVATAR_SEMANTIC_AUDIT.json) | Recorded clients and avatar semantic audit audit, mapping, inventory or validation artifact; retain its dated scope. | Historical/planning evidence; not active application |
| [DUPLICATE_ANALYSIS.txt](../../AnalyseFuture/recovery/features/DUPLICATE_ANALYSIS.txt) | Recorded duplicate analysis audit, mapping, inventory or validation artifact; retain its dated scope. | Historical/planning evidence; not active application |
| [FEATURE_INVENTORY.txt](../../AnalyseFuture/recovery/features/FEATURE_INVENTORY.txt) | Recorded feature inventory audit, mapping, inventory or validation artifact; retain its dated scope. | Historical/planning evidence; not active application |

## [AnalyseFuture/recovery/inventory/](../../AnalyseFuture/recovery/inventory/)

Static file classifications, path mappings and preservation manifests for the recorded repository state.

| File | Purpose | Status |
| --- | --- | --- |
| [ARCHIVED_FILES_MANIFEST.txt](../../AnalyseFuture/recovery/inventory/ARCHIVED_FILES_MANIFEST.txt) | Recorded archived files manifest audit, mapping, inventory or validation artifact; retain its dated scope. | Historical/planning evidence; not active application |
| [COMPLETE_FILE_INVENTORY.txt](../../AnalyseFuture/recovery/inventory/COMPLETE_FILE_INVENTORY.txt) | Recorded complete file inventory audit, mapping, inventory or validation artifact; retain its dated scope. | Historical/planning evidence; not active application |
| [FUNCTIONAL_FILE_INVENTORY.txt](../../AnalyseFuture/recovery/inventory/FUNCTIONAL_FILE_INVENTORY.txt) | Recorded functional file inventory audit, mapping, inventory or validation artifact; retain its dated scope. | Historical/planning evidence; not active application |
| [ORIGINAL_TO_NEW_PATH_MAPPING.txt](../../AnalyseFuture/recovery/inventory/ORIGINAL_TO_NEW_PATH_MAPPING.txt) | Recorded original to new path mapping audit, mapping, inventory or validation artifact; retain its dated scope. | Historical/planning evidence; not active application |
| [PRESERVATION_MANIFEST.json](../../AnalyseFuture/recovery/inventory/PRESERVATION_MANIFEST.json) | Recorded preservation manifest audit, mapping, inventory or validation artifact; retain its dated scope. | Historical/planning evidence; not active application |

## [AnalyseFuture/recovery/migration/](../../AnalyseFuture/recovery/migration/)

Consolidation/organization baselines, relocation mappings and technical-debt records.

| File | Purpose | Status |
| --- | --- | --- |
| [CONSOLIDATION_BASELINE.json](../../AnalyseFuture/recovery/migration/CONSOLIDATION_BASELINE.json) | Recorded consolidation baseline audit, mapping, inventory or validation artifact; retain its dated scope. | Historical/planning evidence; not active application |
| [CONSOLIDATION_REPORT.txt](../../AnalyseFuture/recovery/migration/CONSOLIDATION_REPORT.txt) | Recorded consolidation report audit, mapping, inventory or validation artifact; retain its dated scope. | Historical/planning evidence; not active application |
| [MIGRATION_SUMMARY.txt](../../AnalyseFuture/recovery/migration/MIGRATION_SUMMARY.txt) | Recorded migration summary audit, mapping, inventory or validation artifact; retain its dated scope. | Historical/planning evidence; not active application |
| [REPOSITORY_AUDIT.txt](../../AnalyseFuture/recovery/migration/REPOSITORY_AUDIT.txt) | Recorded repository audit audit, mapping, inventory or validation artifact; retain its dated scope. | Historical/planning evidence; not active application |
| [TECHNICAL_DEBT.txt](../../AnalyseFuture/recovery/migration/TECHNICAL_DEBT.txt) | Recorded technical debt audit, mapping, inventory or validation artifact; retain its dated scope. | Historical/planning evidence; not active application |

## [AnalyseFuture/recovery/migration/functional-sort-2026-11-17/](../../AnalyseFuture/recovery/migration/functional-sort-2026-11-17/)

Consolidation/organization baselines, relocation mappings and technical-debt records.

| File | Purpose | Status |
| --- | --- | --- |
| [FILE_RELOCATION_MAP.json](../../AnalyseFuture/recovery/migration/functional-sort-2026-11-17/FILE_RELOCATION_MAP.json) | Recorded file relocation map audit, mapping, inventory or validation artifact; retain its dated scope. | Historical/planning evidence; not active application |
| [ORGANIZATION_RECORD.md](../../AnalyseFuture/recovery/migration/functional-sort-2026-11-17/ORGANIZATION_RECORD.md) | Recorded organization record audit, mapping, inventory or validation artifact; retain its dated scope. | Historical/planning evidence; not active application |
| [WORK_PROGRESS.txt](../../AnalyseFuture/recovery/migration/functional-sort-2026-11-17/WORK_PROGRESS.txt) | Recorded work progress audit, mapping, inventory or validation artifact; retain its dated scope. | Historical/planning evidence; not active application |

## [AnalyseFuture/recovery/security/](../../AnalyseFuture/recovery/security/)

Recorded pattern-scan and review evidence; no account-security or comprehensive security guarantee.

| File | Purpose | Status |
| --- | --- | --- |
| [SECURITY_AUDIT.txt](../../AnalyseFuture/recovery/security/SECURITY_AUDIT.txt) | Recorded security audit audit, mapping, inventory or validation artifact; retain its dated scope. | Historical/planning evidence; not active application |
| [SECURITY_SCAN_RESULTS.json](../../AnalyseFuture/recovery/security/SECURITY_SCAN_RESULTS.json) | Recorded security scan results audit, mapping, inventory or validation artifact; retain its dated scope. | Historical/planning evidence; not active application |

## [AnalyseFuture/recovery/validation/](../../AnalyseFuture/recovery/validation/)

Historical test reports and explicit unexecuted/live acceptance boundaries.

| File | Purpose | Status |
| --- | --- | --- |
| [TEST_AND_VALIDATION_REPORT.txt](../../AnalyseFuture/recovery/validation/TEST_AND_VALIDATION_REPORT.txt) | Recorded test and validation report audit, mapping, inventory or validation artifact; retain its dated scope. | Historical/planning evidence; not active application |

## [apps/](../../apps/)

Active application clients; currently the web application.

Contains the subfolders listed in their own sections; no tracked files directly in this folder.

<a id="active-web"></a>

## [apps/web/](../../apps/web/)

Active Next.js/React mobile-web application and its package/framework configuration.

| File | Purpose | Status |
| --- | --- | --- |
| [.env.example](../../apps/web/.env.example) | Configuration-name/example template for its component; not a configured live service or a place for real secrets. | active web application |
| [LICENSE](../../apps/web/LICENSE) | Licence/attribution record for the related component/assets; preserve notices and review the exact distribution rights. | active web application |
| [next-env.d.ts](../../apps/web/next-env.d.ts) | Next.js TypeScript ambient declarations; generated framework entrypoint tracked by the project. | active web application |
| [next.config.ts](../../apps/web/next.config.ts) | Active Next.js framework configuration. | active web application |
| [package.json](../../apps/web/package.json) | Containing component dependency/build/test declarations; consult its scope before installing. | active web application |
| [tsconfig.json](../../apps/web/tsconfig.json) | Active app TypeScript includes, compiler settings and generated Next.js route types. | active web application |

## [apps/web/app/](../../apps/web/app/)

Thin Next.js page/layout/style and API entrypoints; feature behavior belongs below features.

| File | Purpose | Status |
| --- | --- | --- |
| [globals.css](../../apps/web/app/globals.css) | Responsive lesson interface, controls, captions and feedback styling. | active web application |
| [layout.tsx](../../apps/web/app/layout.tsx) | Next.js document layout, global styles and page metadata. | active web application |
| [page.tsx](../../apps/web/app/page.tsx) | Thin Next.js page entrypoint mounting the existing lesson application. | active web application |

## [apps/web/app/api/](../../apps/web/app/api/)

Server HTTP route entrypoints for the active Next.js application.

Contains the subfolders listed in their own sections; no tracked files directly in this folder.

## [apps/web/app/api/session/](../../apps/web/app/api/session/)

Session admission/token endpoint entrypoint.

| File | Purpose | Status |
| --- | --- | --- |
| [route.ts](../../apps/web/app/api/session/route.ts) | Thin Next.js POST entrypoint delegating admission and token issuance to the session feature. | active server feature |

## [apps/web/features/](../../apps/web/features/)

Active web features grouped by lesson and session responsibility.

Contains the subfolders listed in their own sections; no tracked files directly in this folder.

## [apps/web/features/lesson/](../../apps/web/features/lesson/)

Lesson catalog, bounded tutor-event state, room UI and matching tests.

| File | Purpose | Status |
| --- | --- | --- |
| [catalog.ts](../../apps/web/features/lesson/catalog.ts) | Allowlisted public lesson choices, labels, defaults and safe lookup helpers. | active web feature |
| [tutor-events.ts](../../apps/web/features/lesson/tutor-events.ts) | Validates untrusted tutor events and maintains bounded feedback, retry, deadline and recap state. | active web feature |

## [apps/web/features/lesson/components/](../../apps/web/features/lesson/components/)

Lesson/call React UI and browser microphone/audio interaction.

| File | Purpose | Status |
| --- | --- | --- |
| [tutor-app.tsx](../../apps/web/features/lesson/components/tutor-app.tsx) | Lesson selection, room/microphone/audio controls, captions, correction cards, recovery and in-memory recap. | active web feature |

## [apps/web/features/lesson/tests/](../../apps/web/features/lesson/tests/)

Catalog and event regression tests; synthetic/local fixtures do not establish live speech quality.

| File | Purpose | Status |
| --- | --- | --- |
| [catalog.test.ts](../../apps/web/features/lesson/tests/catalog.test.ts) | Regression/scenario definitions for catalog.test; execution and test boundaries are recorded separately. | active web feature |
| [tutor-events.test.ts](../../apps/web/features/lesson/tests/tutor-events.test.ts) | Regression/scenario definitions for tutor events.test; execution and test boundaries are recorded separately. | active web feature |

## [apps/web/features/session/](../../apps/web/features/session/)

Server admission/token policy and focused regression coverage.

Contains the subfolders listed in their own sections; no tracked files directly in this folder.

## [apps/web/features/session/server/](../../apps/web/features/session/server/)

Pilot/origin/budget policy, validated requests and JWT generation.

| File | Purpose | Status |
| --- | --- | --- |
| [session.ts](../../apps/web/features/session/server/session.ts) | Pilot/origin/input/budget policy and room-scoped JWTs carrying the canonical lesson and fixed deadline. | active server feature |

## [apps/web/features/session/tests/](../../apps/web/features/session/tests/)

Local policy and thin API-handler regression tests using test-only credentials.

| File | Purpose | Status |
| --- | --- | --- |
| [route.test.ts](../../apps/web/features/session/tests/route.test.ts) | Regression/scenario definitions for route.test; execution and test boundaries are recorded separately. | active server feature |
| [session.test.ts](../../apps/web/features/session/tests/session.test.ts) | Regression/scenario definitions for session.test; execution and test boundaries are recorded separately. | active server feature |

<a id="documentation"></a>

## [docs/](../)

Product, architecture, setup, research, evidence, legal review and continuity documentation.

| File | Purpose | Status |
| --- | --- | --- |
| [README.md](../README.md) | Containing collection/component introduction, navigation and documented usage; retain the scope of the original project. | documentation, not implementation |

## [docs/architecture/](../architecture/)

Design boundaries, decisions and active-versus-preserved source organization.

| File | Purpose | Status |
| --- | --- | --- |
| [ARCHITECTURE.md](../architecture/ARCHITECTURE.md) | Documentation/research record for ARCHITECTURE; requirements and historical observations are not automatically implemented behavior. | documentation, not implementation |
| [DECISIONS.md](../architecture/DECISIONS.md) | Documentation/research record for DECISIONS; requirements and historical observations are not automatically implemented behavior. | documentation, not implementation |
| [REPOSITORY_STRUCTURE.md](../architecture/REPOSITORY_STRUCTURE.md) | Documentation/research record for REPOSITORY STRUCTURE; requirements and historical observations are not automatically implemented behavior. | documentation, not implementation |

## [docs/continuity/](../continuity/)

Historical research/implementation handoff; current status and root handoff override stale next-task instructions.

| File | Purpose | Status |
| --- | --- | --- |
| [PROJECT_CONTINUITY_HANDOFF.md](../continuity/PROJECT_CONTINUITY_HANDOFF.md) | Documentation/research record for PROJECT CONTINUITY HANDOFF; requirements and historical observations are not automatically implemented behavior. | documentation, not implementation |

## [docs/development/](./)

Installation, startup, checks, implementation status, continuation guides and dated validation.

| File | Purpose | Status |
| --- | --- | --- |
| [CODEX_IMPLEMENTATION_BRIEF.md](CODEX_IMPLEMENTATION_BRIEF.md) | Initial engineering brief and acceptance requirements; not an inventory of work still missing. | documentation, not implementation |
| [CODEX_MASTER_BUILD_PROMPT.md](CODEX_MASTER_BUILD_PROMPT.md) | Preserved implementation brief and long-term releases; inspect current handoff before following older task orders. | documentation, not implementation |
| [DEVELOPMENT.md](DEVELOPMENT.md) | Supported installation, cloud caches, service startup, active checks, credentials and deployment boundaries. | documentation, not implementation |
| [IMPLEMENTATION_CHECKLIST.md](IMPLEMENTATION_CHECKLIST.md) | Historical phase/task checklist; current handoff/status supersede completed immediate-task instructions. | documentation, not implementation |
| [IMPLEMENTATION_STATUS.md](IMPLEMENTATION_STATUS.md) | Delivered feature ownership, evidence limits and current remaining integrations. | documentation, not implementation |
| [MODULE_VALIDATION.md](MODULE_VALIDATION.md) | Recorded active/reference validation, repaired defects and limits of the dated evidence. | documentation, not implementation |
| [REPOSITORY_FILE_GUIDE.md](REPOSITORY_FILE_GUIDE.md) | This complete linked file/folder appendix; refresh it when the tracked path set or ownership changes. | Static navigation appendix |
| [VALIDATION.md](VALIDATION.md) | Dated validation history and real-provider/device acceptance checklist. | documentation, not implementation |

## [docs/development/evidence/](evidence/)

Saved validation summaries/screenshots; evidence of their stated checks, not implementation modules.

Contains the subfolders listed in their own sections; no tracked files directly in this folder.

## [docs/development/evidence/module-validation-2026-11-17/](evidence/module-validation-2026-11-17/)

Dated module-validation artifacts and screenshots; preserve their original test scope and distinguish isolated references from active integration.

| File | Purpose | Status |
| --- | --- | --- |
| [active-browser.json](evidence/module-validation-2026-11-17/active-browser.json) | Saved active browser validation summary and stated scenario outcomes; consult the module validation report for limits. | Dated validation evidence; not implementation |
| [active-vad.json](evidence/module-validation-2026-11-17/active-vad.json) | Saved active vad validation summary and stated scenario outcomes; consult the module validation report for limits. | Dated validation evidence; not implementation |
| [avatar-browser.json](evidence/module-validation-2026-11-17/avatar-browser.json) | Saved avatar browser validation summary and stated scenario outcomes; consult the module validation report for limits. | Dated validation evidence; not implementation |
| [avatar-female.png](evidence/module-validation-2026-11-17/avatar-female.png) | Saved avatar female rendering/smoke screenshot; does not prove a real LiveKit lesson integration. | Dated validation evidence; not implementation |
| [avatar-male.png](evidence/module-validation-2026-11-17/avatar-male.png) | Saved avatar male rendering/smoke screenshot; does not prove a real LiveKit lesson integration. | Dated validation evidence; not implementation |
| [avatar-package.json](evidence/module-validation-2026-11-17/avatar-package.json) | Saved avatar package validation summary and stated scenario outcomes; consult the module validation report for limits. | Dated validation evidence; not implementation |
| [cadence-pure-modules.json](evidence/module-validation-2026-11-17/cadence-pure-modules.json) | Saved cadence pure modules validation summary and stated scenario outcomes; consult the module validation report for limits. | Dated validation evidence; not implementation |
| [configured-http.json](evidence/module-validation-2026-11-17/configured-http.json) | Saved configured http validation summary and stated scenario outcomes; consult the module validation report for limits. | Dated validation evidence; not implementation |
| [npm-advisories.json](evidence/module-validation-2026-11-17/npm-advisories.json) | Saved npm advisories validation summary and stated scenario outcomes; consult the module validation report for limits. | Dated validation evidence; not implementation |

## [docs/legal/](../legal/)

Third-party notices and scoped dependency/asset review; not blanket commercial approval.

| File | Purpose | Status |
| --- | --- | --- |
| [DEPENDENCY_AUDIT.md](../legal/DEPENDENCY_AUDIT.md) | Documentation/research record for DEPENDENCY AUDIT; requirements and historical observations are not automatically implemented behavior. | documentation, not implementation |
| [THIRD_PARTY_NOTICES.md](../legal/THIRD_PARTY_NOTICES.md) | Licence/attribution record for the related component/assets; preserve notices and review the exact distribution rights. | documentation, not implementation |

## [docs/product/](../product/)

Product ambition, learner experience, provisional acceptance gates and longer-term roadmap.

| File | Purpose | Status |
| --- | --- | --- |
| [MVP_AND_ACCEPTANCE.md](../product/MVP_AND_ACCEPTANCE.md) | Documentation/research record for MVP AND ACCEPTANCE; requirements and historical observations are not automatically implemented behavior. | documentation, not implementation |
| [PRODUCT_VISION.md](../product/PRODUCT_VISION.md) | Documentation/research record for PRODUCT VISION; requirements and historical observations are not automatically implemented behavior. | documentation, not implementation |
| [PROJECT_IDEA.txt](../product/PROJECT_IDEA.txt) | Documentation/research record for PROJECT IDEA; requirements and historical observations are not automatically implemented behavior. | documentation, not implementation |
| [ROADMAP.md](../product/ROADMAP.md) | Documentation/research record for ROADMAP; requirements and historical observations are not automatically implemented behavior. | documentation, not implementation |

## [docs/research/](../research/)

Source studies, feasibility notes and reuse candidates; recommendations must be checked against delivered work.

| File | Purpose | Status |
| --- | --- | --- |
| [ASTRA_HANDOFF.md](../research/ASTRA_HANDOFF.md) | Documentation/research record for ASTRA HANDOFF; requirements and historical observations are not automatically implemented behavior. | documentation, not implementation |
| [OPEN_SOURCE_REPOSITORIES.txt](../research/OPEN_SOURCE_REPOSITORIES.txt) | Documentation/research record for OPEN SOURCE REPOSITORIES; requirements and historical observations are not automatically implemented behavior. | documentation, not implementation |
| [OPEN_SOURCE_STACK.md](../research/OPEN_SOURCE_STACK.md) | Documentation/research record for OPEN SOURCE STACK; requirements and historical observations are not automatically implemented behavior. | documentation, not implementation |
| [TWO_PRIMARY_REFERENCE_REPOS.md](../research/TWO_PRIMARY_REFERENCE_REPOS.md) | Documentation/research record for TWO PRIMARY REFERENCE REPOS; requirements and historical observations are not automatically implemented behavior. | documentation, not implementation |

<a id="maintenance"></a>

## [scripts/](../../scripts/)

Explicit repository maintenance utilities, not automatically started application services.

Contains the subfolders listed in their own sections; no tracked files directly in this folder.

## [scripts/maintenance/](../../scripts/maintenance/)

Read-only inventory/security commands with scoped disposable-fixture regression coverage.

| File | Purpose | Status |
| --- | --- | --- |
| [repository_inventory.py](../../scripts/maintenance/repository_inventory.py) | Reads tracked payloads and statically describes ownership/imports without importing inspected application/reference code. | explicit maintenance command |
| [security_history_scan.py](../../scripts/maintenance/security_history_scan.py) | Explicit read-only pattern scanning of tracked files, Git history and ZIP members without printing candidate secret values. | explicit maintenance command |

## [services/](../../services/)

Active backend processes; currently the Python voice worker.

Contains the subfolders listed in their own sections; no tracked files directly in this folder.

<a id="voice-worker"></a>

## [services/voice-agent/](../../services/voice-agent/)

Active Python LiveKit worker, packaging, runtime pin, configuration examples and scoped tests.

| File | Purpose | Status |
| --- | --- | --- |
| [.env.example](../../services/voice-agent/.env.example) | Configuration-name/example template for its component; not a configured live service or a place for real secrets. | active Python service |
| [.python-version](../../services/voice-agent/.python-version) | Pins the active worker interpreter to Python 3.12. | active Python service |
| [LICENSE](../../services/voice-agent/LICENSE) | Licence/attribution record for the related component/assets; preserve notices and review the exact distribution rights. | active Python service |
| [pyproject.toml](../../services/voice-agent/pyproject.toml) | Python package, CLI entrypoint, dependencies, test settings and Ruff configuration. | active Python service |
| [uv.lock](../../services/voice-agent/uv.lock) | Frozen Python dependency resolutions for reproducible worker and development installs. | active Python service |

## [services/voice-agent/src/](../../services/voice-agent/src/)

Installable Python source tree for the existing worker.

Contains the subfolders listed in their own sections; no tracked files directly in this folder.

## [services/voice-agent/src/eng_teacher/](../../services/voice-agent/src/eng_teacher/)

Voice package identity, stable CLI compatibility and implementation subpackages.

| File | Purpose | Status |
| --- | --- | --- |
| [__init__.py](../../services/voice-agent/src/eng_teacher/__init__.py) | Python package marker for eng_teacher; establishes its import/package boundary. | active Python service |
| [agent.py](../../services/voice-agent/src/eng_teacher/agent.py) | Stable CLI compatibility entrypoint delegating to the runtime module. | active Python service |

## [services/voice-agent/src/eng_teacher/providers/](../../services/voice-agent/src/eng_teacher/providers/)

Current replaceable speech/text provider boundary and validated OpenAI adapters.

| File | Purpose | Status |
| --- | --- | --- |
| [__init__.py](../../services/voice-agent/src/eng_teacher/providers/__init__.py) | Python package marker for providers; establishes its import/package boundary. | active provider boundary |
| [openai.py](../../services/voice-agent/src/eng_teacher/providers/openai.py) | Validated OpenAI settings, structured tutor decisions, retry/help decisions and speech adapter configuration. | active provider boundary |

## [services/voice-agent/src/eng_teacher/runtime/](../../services/voice-agent/src/eng_teacher/runtime/)

LiveKit audio/events, room lifecycle and private numeric usage accounting.

| File | Purpose | Status |
| --- | --- | --- |
| [__init__.py](../../services/voice-agent/src/eng_teacher/runtime/__init__.py) | Python package marker for runtime; establishes its import/package boundary. | active LiveKit worker |
| [agent.py](../../services/voice-agent/src/eng_teacher/runtime/agent.py) | LiveKit audio session orchestration, metadata, controls, events, privacy settings and guarded room/resource lifecycle. | active LiveKit worker |
| [usage.py](../../services/voice-agent/src/eng_teacher/runtime/usage.py) | Bounded private numeric model/speech/error counters; not a complete billing estimate. | active LiveKit worker |

## [services/voice-agent/src/eng_teacher/teaching/](../../services/voice-agent/src/eng_teacher/teaching/)

Original lesson definitions, learner controls and provider-independent correction/retry policy.

| File | Purpose | Status |
| --- | --- | --- |
| [__init__.py](../../services/voice-agent/src/eng_teacher/teaching/__init__.py) | Python package marker for teaching; establishes its import/package boundary. | active Python teaching module |
| [controls.py](../../services/voice-agent/src/eng_teacher/teaching/controls.py) | Recognizes explicit help, language explanation, repeat, example, retry and skip requests. | active Python teaching module |
| [lessons.py](../../services/voice-agent/src/eng_teacher/teaching/lessons.py) | Original immutable Mock interview/Everyday English curriculum and validated lesson selection. | active Python teaching module |
| [tutor.py](../../services/voice-agent/src/eng_teacher/teaching/tutor.py) | Provider-independent teaching state, single correction, meaning guards, help/retry and question progression. | active Python teaching module |

## [services/voice-agent/tests/](../../services/voice-agent/tests/)

Scoped worker verification using policy, provider and SDK fixtures; not real-provider acceptance.

| File | Purpose | Status |
| --- | --- | --- |
| [__init__.py](../../services/voice-agent/tests/__init__.py) | Python package marker for tests; establishes its import/package boundary. | active service verification fixtures; execution recorded in validation reports |

## [services/voice-agent/tests/runtime/](../../services/voice-agent/tests/runtime/)

Session scheduling, initialization/shutdown/cancellation, room cleanup and usage regressions.

| File | Purpose | Status |
| --- | --- | --- |
| [__init__.py](../../services/voice-agent/tests/runtime/__init__.py) | Python package marker for runtime; establishes its import/package boundary. | active service verification fixtures; execution recorded in validation reports |
| [test_agent.py](../../services/voice-agent/tests/runtime/test_agent.py) | Regression/scenario definitions for test agent; execution and test boundaries are recorded separately. | active service verification fixtures; execution recorded in validation reports |
| [test_lifecycle.py](../../services/voice-agent/tests/runtime/test_lifecycle.py) | Regression/scenario definitions for test lifecycle; execution and test boundaries are recorded separately. | active service verification fixtures; execution recorded in validation reports |
| [test_usage.py](../../services/voice-agent/tests/runtime/test_usage.py) | Regression/scenario definitions for test usage; execution and test boundaries are recorded separately. | active service verification fixtures; execution recorded in validation reports |

## [services/voice-agent/tests/teaching/](../../services/voice-agent/tests/teaching/)

Curriculum, learner intents, meaning guards, help/retry and adapter contract regressions.

| File | Purpose | Status |
| --- | --- | --- |
| [__init__.py](../../services/voice-agent/tests/teaching/__init__.py) | Python package marker for teaching; establishes its import/package boundary. | active service verification fixtures; execution recorded in validation reports |
| [test_lessons.py](../../services/voice-agent/tests/teaching/test_lessons.py) | Regression/scenario definitions for test lessons; execution and test boundaries are recorded separately. | active service verification fixtures; execution recorded in validation reports |
| [test_tutor.py](../../services/voice-agent/tests/teaching/test_tutor.py) | Regression/scenario definitions for test tutor; execution and test boundaries are recorded separately. | active service verification fixtures; execution recorded in validation reports |

<a id="shared-tests"></a>

## [tests/](../../tests/)

Cross-component browser tests, shared contracts and repository maintenance fixtures.

Contains the subfolders listed in their own sections; no tracked files directly in this folder.

## [tests/browser/](../../tests/browser/)

Desktop/mobile viewport scenarios using synthetic microphone and failure recovery, not a successful provider lesson.

| File | Purpose | Status |
| --- | --- | --- |
| [lesson.spec.ts](../../tests/browser/lesson.spec.ts) | Regression/scenario definitions for lesson.spec; execution and test boundaries are recorded separately. | active scoped tests |

## [tests/contracts/](../../tests/contracts/)

Shared cross-runtime verification data; not a separate source of runtime curriculum.

| File | Purpose | Status |
| --- | --- | --- |
| [lesson-catalog.json](../../tests/contracts/lesson-catalog.json) | Shared test fixture keeping TypeScript/Python lesson IDs and default selection aligned. | active verification fixture, not runtime curriculum |

## [tests/maintenance/](../../tests/maintenance/)

CLI regressions against disposable Git fixtures, including scan privacy and archive handling.

| File | Purpose | Status |
| --- | --- | --- |
| [test_repository_tools.py](../../tests/maintenance/test_repository_tools.py) | test repository tools module; static declarations include git, repo, run_tool, test_inventory_covers_staged_paths_and_does_not_import_source, test_inventory_ref_reads_immutable_payloads, test_inventory_missing_git_root_fails_instead_of_claiming_coverage. No behavior is executed by this guide. | active CLI fixtures using disposable Git repositories |
