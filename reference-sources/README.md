# Preserved project sources

These directories preserve the two ZIP archives uploaded to this repository.
They are committed so future work does not depend on the cloud workspace surviving.

| Directory | Original archive | Upstream |
| --- | --- | --- |
| [Cadence-main](Cadence-main/) | [Cadence-main.zip](../Cadence-main.zip) | https://github.com/pstepanovum/Cadence |
| [talking-avatar-master](talking-avatar-master/) | [talking-avatar-master.zip](../talking-avatar-master.zip) | https://github.com/InterviewFlowAI/talking-avatar |

Every extracted file was compared byte for byte with its ZIP entry before committing.
[ARCHIVES.json](ARCHIVES.json) records archive SHA-256 hashes and file counts.
The ZIP filenames do not establish an upstream commit; these are snapshots of the
uploaded archives, not newly fetched upstream revisions.

The existing Eng Teacher application remains in `apps/web` and `services/voice-agent`.
These snapshots are not registered as workspaces, installed, connected to the app,
or validated as running features. Feature integration, restructuring, and language
migration are deferred until the owner gives the next instructions.

Upstream source, assets, licenses, notices, and credits are preserved unchanged.
Cadence and Talking Avatar carry MIT project licenses; their included components
retain their own notices. In particular, retain Cadence's `NOTICE` and `CREDITS.md`
and Talking Avatar's `avatars/LICENSE`. Preservation is not a complete dependency,
model, content, or commercial-use audit.

Owner's requested workflow: work directly on `main`, without feature branches or
PRs; make and push checkpoints at least every five minutes while editing, when
there are changes to save. Follow the owner's requested scope for further work.
