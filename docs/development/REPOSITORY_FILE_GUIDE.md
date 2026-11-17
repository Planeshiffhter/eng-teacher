# Repository file guide

Use the [project structure](../../PROJECT_STRUCTURE.md) for feature ownership and
the [project handoff](../../PROJECT_HANDOFF.md) for active entrypoints and contracts.
The [implementation status](IMPLEMENTATION_STATUS.md) records current behavior and
validation.

| Collection | Where to look |
| --- | --- |
| Web application | [Next.js entrypoints](../../apps/web/app/), [lesson UI and events](../../apps/web/features/lesson/), [session admission](../../apps/web/features/session/) |
| Voice worker | [CLI, teaching, providers and runtime](../../services/voice-agent/src/eng_teacher/), [worker tests](../../services/voice-agent/tests/) |
| Shared checks | [browser, contracts and maintenance tests](../../tests/), [GitHub Actions](../../.github/workflows/) |
| Maintenance tools | [static inventory and secret-pattern scan](../../scripts/maintenance/) |
| Project documentation | [docs index](../README.md) |
| Research and recovery | [archive navigation, hashes and source recovery](../../AnalyseFuture/README.md) |

The [complete 1,603-file guide at the recovery revision](https://github.com/Planeshiffhter/eng-teacher/blob/600a361e9f97a76603aa260141ce3876d7b94c62/docs/development/REPOSITORY_FILE_GUIDE.md)
retains the original per-file and folder descriptions, including the expanded
reference projects. Historical inventory paths refer to that checkout and related
[recovery records](../../AnalyseFuture/recovery/inventory/).
