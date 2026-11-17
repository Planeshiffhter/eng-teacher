# Preserved reference projects

The original uploads contain all **1,474** files from the two reference projects.
Every ZIP file entry matched its previously extracted tracked copy byte for byte.
The ZIPs retain the original layout, source, tooling, models, assets and notices.

| Project | Original upload | Extracted tree at the verified recovery revision |
| --- | --- | --- |
| Cadence (1,443 files) | [Cadence-main.zip](../Cadence-main.zip) | [Cadence-main](https://github.com/Planeshiffhter/eng-teacher/tree/600a361e9f97a76603aa260141ce3876d7b94c62/AnalyseFuture/original-projects/reference-sources/Cadence-main) |
| Talking Avatar (31 files) | [talking-avatar-master.zip](../talking-avatar-master.zip) | [talking-avatar-master](https://github.com/Planeshiffhter/eng-teacher/tree/600a361e9f97a76603aa260141ce3876d7b94c62/AnalyseFuture/original-projects/reference-sources/talking-avatar-master) |

The extracted trees are recoverable from either original ZIP or Git at
`600a361e9f97a76603aa260141ce3876d7b94c62`. See [ARCHIVES.json](ARCHIVES.json) for
the ZIP SHA-256 hashes, member counts and exact Git path. The baseline also retains
the original import README and metadata referenced by the older
[preservation manifest](../../recovery/inventory/PRESERVATION_MANIFEST.json).

From the repository root, verify both archives without extracting them:

```sh
cd AnalyseFuture/original-projects
sha256sum Cadence-main.zip talking-avatar-master.zip
python3 -m zipfile -t Cadence-main.zip
python3 -m zipfile -t talking-avatar-master.zip
```

Compare the SHA-256 output with [ARCHIVES.json](ARCHIVES.json). Inspect individual
members with `unzip -p <ZIP> <member>`. Restore a tree into a separate directory
only for a task that needs it. The repository uses
[Cadence](https://github.com/pstepanovum/Cadence) and
[Talking Avatar](https://github.com/InterviewFlowAI/talking-avatar) as references.
The uploaded ZIP filenames do not establish upstream commits.

[Third-party notices](../../../docs/legal/THIRD_PARTY_NOTICES.md) identify the
original project licenses and separate model/asset terms. The
[reference studies](../../../docs/research/TWO_PRIMARY_REFERENCE_REPOS.md) and
[recorded isolated validation](../../../docs/development/MODULE_VALIDATION.md)
describe selective reuse and relevant security and licensing prerequisites.
