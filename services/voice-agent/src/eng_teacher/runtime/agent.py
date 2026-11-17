"""LiveKit pipeline adapted from the MIT-licensed official Python agent starter."""

from __future__ import annotations

import asyncio
import json
import logging
import time
from collections.abc import AsyncIterable, Awaitable, Callable
from contextlib import suppress

from dotenv import load_dotenv
from livekit import api, rtc
from livekit.agents import (
    Agent,
    AgentServer,
    AgentSession,
    JobContext,
    ModelSettings,
    Plugin,
    cli,
    llm,
    metrics,
    room_io,
)
from livekit.plugins import silero

from ..providers.openai import Settings, create_llm, create_model, create_stt, create_tts
from ..teaching.lessons import lesson_from_metadata
from ..teaching.tutor import InterviewTutor
from .usage import LessonUsage

logger = logging.getLogger("eng_teacher")
LESSON_SECONDS = 600
AGENT_NAME = "eng-teacher"
Publish = Callable[[str, dict], Awaitable[None]]


def lesson_deadline_ms(metadata: str, *, now_ms: int | None = None) -> int:
    """Reject missing/expired/malformed room deadlines rather than resetting them."""
    now_ms = int(time.time() * 1000) if now_ms is None else now_ms
    try:
        value = json.loads(metadata)["lesson_deadline_ms"]
    except (ValueError, TypeError, KeyError) as exc:
        raise ValueError("Room requires a signed lesson deadline") from exc
    if type(value) is not int or not now_ms < value <= now_ms + LESSON_SECONDS * 1000:
        raise ValueError("Invalid or expired lesson deadline")
    return value


class InterviewAgent(Agent):
    def __init__(self, tutor: InterviewTutor, publish: Publish):
        # The SDK's llm_node extension point allows a validated, replaceable text
        # adapter while retaining official STT, turn-taking, TTS and WebRTC.
        super().__init__(instructions=f"Guide a ten-minute speaking practice. {tutor.lesson.goal}")
        self.tutor = tutor
        self.publish = publish

    async def llm_node(
        self, chat_ctx: llm.ChatContext, tools: list[llm.Tool], model_settings: ModelSettings
    ) -> AsyncIterable[str]:
        original = next(
            (
                item.text_content
                for item in reversed(chat_ctx.items)
                if isinstance(item, llm.ChatMessage) and item.role == "user"
            ),
            None,
        )
        if not original:
            return
        feedback = await self.tutor.turn(original)
        await self.publish("tutor.feedback", feedback.model_dump())
        if self.tutor.last_provider_failed:
            await self.publish(
                "tutor.error",
                {
                    "version": 1,
                    "message": "The teaching service is temporarily unavailable. Please try again.",
                    "recoverable": True,
                },
            )
        yield feedback.spoken_response


server = AgentServer()


@server.rtc_session(agent_name=AGENT_NAME)
async def interview(ctx: JobContext):
    configure_private_logging()
    usage = LessonUsage()
    resources: list[object] = []
    closed_resources: set[int] = set()

    def keep(resource):
        resources.append(resource)
        return resource

    tasks: set[asyncio.Task] = set()
    finished = False
    deadline_ms = 0

    def spawn(coroutine):
        task = asyncio.create_task(coroutine)
        tasks.add(task)

        def completed(done):
            tasks.discard(done)
            if not done.cancelled():
                # Retrieve background transport failures without logging provider
                # exceptions, which may contain credentials or learner text.
                done.exception()

        task.add_done_callback(completed)
        return task

    async def publish(topic: str, body: dict) -> None:
        if ctx.room.isconnected():
            await ctx.room.local_participant.publish_data(
                json.dumps(body, ensure_ascii=False), topic=topic, reliable=True
            )

    async def finish(reason: str) -> None:
        nonlocal finished
        if finished:
            return
        finished = True
        try:
            with suppress(Exception):
                await publish(
                    "tutor.lesson",
                    {"version": 1, "state": "ended", "deadline_ms": deadline_ms, "reason": reason},
                )
            await cleanup()
            # Delete the room as a server action, so reconnecting a browser cannot
            # continue a paid lesson beyond its server deadline.
            with suppress(Exception):
                await ctx.api.room.delete_room(api.DeleteRoomRequest(room=ctx.room.name))
        finally:
            # Only aggregate units; no text, raw audio, keys or provider payloads.
            logger.info("lesson_finished reason=%s usage=%s", reason, json.dumps(usage.snapshot()))
            ctx.shutdown(reason)

    async def deadline() -> None:
        await asyncio.sleep(max(0.0, (deadline_ms - time.time() * 1000) / 1000))
        await finish("time_limit")

    async def cleanup() -> None:
        current = asyncio.current_task()
        pending = [task for task in tasks if task is not current]
        for task in pending:
            task.cancel()
        await asyncio.gather(*pending, return_exceptions=True)
        # Close the session first, then every constructed provider. A failed
        # constructor or close must not strand earlier clients or skip cleanup.
        for resource in reversed(resources):
            identity = id(resource)
            if identity in closed_resources:
                continue
            closed_resources.add(identity)
            close = getattr(resource, "aclose", None)
            if close is not None:
                with suppress(Exception):
                    await close()

    ctx.add_shutdown_callback(cleanup)
    try:
        settings = Settings.from_env()
        settings.validate_credentials()
        model = keep(create_model(settings))
        model.usage_callback = usage.record_model
        routed_llm = keep(create_llm(settings))
        recognizer = keep(create_stt(settings))
        synthesizer = keep(create_tts(settings))
        vad = keep(silero.VAD.load(min_silence_duration=1.2, force_cpu=True))
        session = keep(
            AgentSession(
                # SDK gates automatic microphone replies on a configured LLM. The
                # custom llm_node below performs the validated structured model call.
                llm=routed_llm,
                stt=recognizer,
                tts=synthesizer,
                vad=vad,
                turn_handling={
                    "turn_detection": "vad",
                    "endpointing": {"min_delay": 0.2, "max_delay": 3.0},
                    "interruption": {
                        "enabled": True,
                        "mode": "vad",
                        "min_duration": 0.4,
                        "min_words": 0,
                    },
                    # Speculative generations must not consume correction/retry state.
                    "preemptive_generation": {"enabled": False},
                },
                # Avoid unsupported, automatic away/goodbye generations in this lesson.
                user_away_timeout=None,
            )
        )
        # Factories can register plugins lazily; the dev CLI assigns their loggers
        # DEBUG on registration. Reset levels after those imports, before any speech.
        configure_private_logging()

        @session.on("metrics_collected")
        def collect_usage(event):
            item = event.metrics
            if isinstance(item, metrics.STTMetrics):
                usage.record_stt(item.audio_duration)
            elif isinstance(item, metrics.TTSMetrics):
                usage.record_tts(item.characters_count)

        @session.on("error")
        def provider_error(event):
            spawn(
                publish(
                    "tutor.error",
                    {
                        "version": 1,
                        "message": "A speech service failed. Please try speaking again."
                        if getattr(event.error, "recoverable", False)
                        else "A speech service is unavailable. Please end the session and try again.",
                        "recoverable": bool(getattr(event.error, "recoverable", False)),
                    },
                )
            )
            if not getattr(event.error, "recoverable", False):
                spawn(finish("provider_error"))

        @session.on("close")
        def session_closed(_event):
            spawn(finish("session_closed"))

        await ctx.connect()
        # The web server signs this in RoomConfiguration.metadata. Reusing a
        # still-valid join token cannot mint a fresh ten minutes in the worker.
        deadline_ms = lesson_deadline_ms(ctx.room.metadata)
        lesson = lesson_from_metadata(ctx.room.metadata)
        spawn(deadline())
        remaining = max(0.0, (deadline_ms - time.time() * 1000) / 1000)
        learner = await asyncio.wait_for(ctx.wait_for_participant(), timeout=min(30, remaining))

        @ctx.room.on("participant_disconnected")
        def learner_left(participant: rtc.RemoteParticipant):
            if participant.identity == learner.identity:
                spawn(finish("learner_disconnected"))

        await session.start(
            agent=InterviewAgent(InterviewTutor(model, lesson=lesson), publish),
            room=ctx.room,
            room_options=room_io.RoomOptions(
                participant_identity=learner.identity,
                audio_input=room_io.AudioInputOptions(),
                audio_output=room_io.AudioOutputOptions(),
                # Built-in live lk.transcription output remains enabled for captions.
                text_input=False,
                video_input=False,
                close_on_disconnect=True,
            ),
            # Explicitly disable audio recording AND cloud transcript/trace/log uploads.
            record=False,
        )
        await publish(
            "tutor.lesson", {"version": 1, "state": "started", "deadline_ms": deadline_ms}
        )
        # say() bypasses the correction pipeline for the initial greeting.
        await session.say(lesson.greeting, allow_interruptions=True)
    except asyncio.CancelledError:
        configure_private_logging()
        await finish("cancelled")
        raise
    except Exception:
        configure_private_logging()
        with suppress(Exception):
            await publish(
                "tutor.error",
                {
                    "version": 1,
                    "message": "The voice session could not start. Check the server's provider configuration.",
                },
            )
        await finish("startup_error")


def configure_private_logging() -> None:
    # Apply inside the worker too, after the CLI has configured child logging.
    # CLI dev otherwise enables debug logs, which can include recognized text.
    logging.getLogger("livekit.agents").setLevel(logging.WARNING)
    logging.getLogger("livekit.plugins").setLevel(logging.WARNING)
    logging.getLogger("livekit.plugins.openai").setLevel(logging.WARNING)
    for plugin in Plugin.registered_plugins:
        if plugin.logger is not None:
            plugin.logger.setLevel(logging.WARNING)


def main() -> None:
    load_dotenv(".env.local")
    configure_private_logging()
    cli.run_app(server)


if __name__ == "__main__":
    main()
