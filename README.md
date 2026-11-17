# Eng Teacher

Eng Teacher is a Hindi–English speaking tutor with Mock interview, Everyday
English and Café order lessons. In a ten-minute lesson, the AI tutor keeps the
recognized transcript separate from suggestions, and offers a correction,
explanation and speaking retry when useful.

**Quick exercises** offers standalone grammar, vocabulary and conversation
practice. You can open it without a pilot code or a voice service. Optional
self-listening records a short clip locally for playback in the current tab.
Enable **Save progress on this browser** to resume an exercise and keep its
latest score. Turning it off clears saved exercise progress.

## Run locally

Use Node.js 24, Python 3.12 and uv. From the repository root:

```sh
npm ci
uv sync --frozen --project services/voice-agent
npm run dev
```

For a live lesson, configure LiveKit, OpenAI and a pilot code securely, then
start the named worker in a separate terminal. See the
[development guide](docs/development/DEVELOPMENT.md) for credentials, startup,
browser checks and the cloud environment. The voice lesson does not start
recording. Connected providers process audio during the call.

## Work on the project

- [Current implementation and test status](docs/development/IMPLEMENTATION_STATUS.md)
- [System architecture](docs/architecture/ARCHITECTURE.md) and [source map](PROJECT_STRUCTURE.md)
- [Repository instructions](AGENTS.md) and [continuation notes](docs/continuity/PROJECT_CONTINUITY_HANDOFF.md)
- [Product vision](docs/product/PRODUCT_VISION.md), [pilot acceptance](docs/product/MVP_AND_ACCEPTANCE.md) and [roadmap](docs/product/ROADMAP.md)
- [Dependency audit](docs/legal/DEPENDENCY_AUDIT.md) and [third-party notices](docs/legal/THIRD_PARTY_NOTICES.md)
- [Preserved archives and recovery records](AnalyseFuture/README.md)

This repository is public. Keep credentials, learner audio, personal data and
production logs out of Git.
