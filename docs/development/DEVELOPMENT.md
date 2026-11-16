# Run the first voice-tutor implementation

> This is setup guidance for a later authorized execution task. During the current
> organization, no installs, tests, builds, app imports or startup were run. See
> [PROJECT_STRUCTURE.md](../../PROJECT_STRUCTURE.md) for current module locations.
> The `eng-teacher-agent` console command still enters `eng_teacher.agent:main`;
> that compatibility module delegates to `eng_teacher.runtime.agent`.

## Current code ownership after recovery

Next.js pages and the `/api/session` route are thin framework entrypoints. The web
room UI, event parser and their tests are grouped in `apps/web/features/lesson`;
server admission/token policy and its tests are in `apps/web/features/session`.
Python controls, provider adapters, policy and lifecycle stay in the existing
`services/voice-agent/src/eng_teacher` package. See
[the consolidation report](../../AnalyseFuture/recovery/migration/CONSOLIDATION_REPORT.txt) for contracts
and compatibility. Public session URL and event version remain unchanged.

Root `pytest.ini` restricts default collection to the active worker. Prefer the
scoped commands below; do not install or collect tests from `AnalyseFuture` as part
of normal setup. The model adapter now implements `assess_retry` and
`help_with_correction`; any separately maintained adapter must follow that
validated protocol. No additional adapter was found here.

Current local validation is **14 JavaScript / 71 Python / 6 browser tests**, plus
build, typecheck, Ruff lint and formatting. Add
`uv run --frozen ruff format --check .` from `services/voice-agent` to the Python
checks. Refresh the inventory explicitly with
`python3 scripts/maintenance/repository_inventory.py --output AnalyseFuture/recovery/inventory/COMPLETE_FILE_INVENTORY.txt`
after staging intended new tracked files.

This branch contains a real LiveKit browser/agent integration. Automated tests use explicitly fake tutor/speech inputs; live provider calls and human speech quality have not been validated without credentials. The existing product and acceptance documents remain requirements, not proof of acceptance.

## Prerequisites

- Node.js 24 and npm; Python 3.12 and [uv](https://docs.astral.sh/uv/).
- A LiveKit Cloud project, or a compatible LiveKit server reachable by both browser and worker. The server must support named agent dispatch via room configuration. No database or GPU is required.
- An OpenAI project with access to `whisper-1`, `gpt-4.1-mini`, and `gpt-4o-mini-tts`. The three adapters/models are independently configurable; this milestone implements OpenAI adapters only. Sarvam is a future candidate, not integrated.
- HTTPS for a phone or deployed site; browsers permit microphone access on localhost for desktop development. Use headphones.

Install from the repository root:

```sh
npm ci
uv sync --frozen --project services/voice-agent
cp apps/web/.env.example apps/web/.env.local
cp services/voice-agent/.env.example services/voice-agent/.env.local
```

Fill the two ignored `.env.local` files securely. Both need the same `LIVEKIT_URL`, `LIVEKIT_API_KEY`, and `LIVEKIT_API_SECRET`. The worker also needs `OPENAI_API_KEY`. The web server needs a random `PILOT_ACCESS_CODE` of at least 16 characters (32 recommended); share it only with invited pilot participants. LiveKit's API secret must be at least 32 characters. Do not put any API key into a `NEXT_PUBLIC_*` variable or into a commit. Example files contain names and placeholders only.

For an environment with restricted outbound access, permit `api.openai.com`, your exact LiveKit project hostname (HTTPS/WebSocket), and LiveKit's required WebRTC media connectivity. The worker and browser both need a working LiveKit connection. Environment policy may require additional UDP/TCP/TURN support; package-manager access alone does not establish media connectivity. Provider credentials must work in local SDK processes, not merely be declared in settings. Do not disable TLS verification.

## Start the two processes

Terminal one, from the repository root:

```sh
cd services/voice-agent
uv run --frozen eng-teacher-agent dev
```

Terminal two, from the repository root:

```sh
npm run dev
```

Open the web server in your browser, enter the pilot code, and start a lesson. Allow the microphone. The server issues a short-lived room-scoped token and dispatches the worker named `eng-teacher`. Wait for the tutor's spoken greeting, answer the interview question, and interrupt with speech when needed. Use Mute mic or End lesson at any time. If the browser blocks playback, press Enable tutor audio.

The worker uses official OpenAI STT/TTS plugins, Silero voice-activity detection, and the SDK's interruptible audio pipeline. Whisper is a turn-based recognizer behind LiveKit's stream adapter: learner captions appear after recognized speech segments, rather than word-by-word partial recognition. Mixed Hindi–English recognition and Hindi pronunciation must still be evaluated with bilingual speakers. No phoneme scoring is implemented.

The lesson offers one correction at a time, displays recognized original and suggested wording separately, invites a spoken retry, and then advances the interview. Uncertain or obviously risky corrections ask for clarification. Meaning checks are conservative heuristics plus model instructions, not a guarantee of correctness. A mistaken recognized transcript remains possible.

Both browser and worker enforce a ten-minute cap; the token carries a fixed server deadline so reconnecting cannot restart the allotted time. Ending a lesson stops microphone tracks; the worker closes and deletes the room when the learner leaves or the deadline arrives. The recap stays only in the page's memory and is lost on refresh.

## Validation

```sh
npm test
npm run typecheck
npm run build
npm run test:agent
cd services/voice-agent
uv run --frozen ruff check .
```

Browser checks run against a production build with deliberately empty voice credentials:

```sh
npm run build
npx playwright install chromium
npm run test:browser
```

The tests use an existing `/usr/bin/chromium` when available; set `PLAYWRIGHT_CHROMIUM_EXECUTABLE` for another installed Chromium, or let Playwright use its managed download. On supported Linux hosts, Playwright's browser system dependencies may also need installation. Browser tests verify desktop/mobile layouts, a synthetic Chromium microphone, missing-configuration errors, and failed-room recovery. They do not prove a real learner-to-provider voice call.

See [validation status and the live checklist](VALIDATION.md) for results and unrun checks.

## Deployment boundaries

`npm run build && npm start` serves the production frontend. Run `uv run --frozen eng-teacher-agent start` from `services/voice-agent` as a separate supervised worker. Set `APP_ORIGIN` to the exact public HTTPS origin, especially behind a reverse proxy. Use real environment secrets rather than copying local files into public images. Keep worker/service logs private.

Access is gated by a shared pilot code and a small process-local request budget. This is an invited-pilot implementation, not a public SaaS authentication or billing system. Before public launch add individual authentication, distributed rate limits/quotas, provider spending limits, deployment monitoring, retention review, and the acceptance evaluations. A token is not a provider credential, but treat it as a short-lived bearer credential.

The application starts no audio recording or egress. The worker disables LiveKit session recording and cloud session transcript/trace uploads; no lesson text or audio is written to a database or browser storage. LiveKit and OpenAI still process audio/text to provide the call. Review their retention, region and commercial terms separately. No avatar, pronunciation assessor, fine-tuning, mobile-native client or gamification is included.
