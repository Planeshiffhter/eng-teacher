"""Fakes verify the worker deadline and cleanup; no LiveKit server is contacted."""

import asyncio
import json
import logging
import time
from types import SimpleNamespace
from unittest.mock import AsyncMock

import pytest

from eng_teacher.runtime import agent as module


class FakeSession:
    def __init__(self, **kwargs):
        self.options = kwargs
        self.callbacks = {}
        self.started = None
        self.closed = False
        self.greetings = []

    def on(self, name):
        def register(callback):
            self.callbacks[name] = callback
            return callback

        return register

    async def start(self, **kwargs):
        self.started = kwargs

    async def say(self, *args, **kwargs):
        self.greetings.append(args[0])

    async def aclose(self):
        self.closed = True


class FakeRoom:
    def __init__(self, metadata):
        self.metadata = metadata
        self.name = "offline-room"
        self.callbacks = {}
        self.packets = []
        self.local_participant = SimpleNamespace(publish_data=self.publish)

    def isconnected(self):
        return True

    async def publish(self, data, **kwargs):
        self.packets.append((kwargs["topic"], json.loads(data)))

    def on(self, name):
        def register(callback):
            self.callbacks[name] = callback
            return callback

        return register


class FakeContext:
    def __init__(self, metadata):
        self.room = FakeRoom(metadata)
        self.delete = AsyncMock()
        self.api = SimpleNamespace(room=SimpleNamespace(delete_room=self.delete))
        self.stopped = asyncio.Event()
        self.callbacks = []
        self.reason = None

    async def connect(self):
        return None

    async def wait_for_participant(self):
        return SimpleNamespace(identity="learner")

    def add_shutdown_callback(self, callback):
        self.callbacks.append(callback)

    def shutdown(self, reason):
        self.reason = reason
        self.stopped.set()


@pytest.fixture
def worker(monkeypatch):
    model = SimpleNamespace(aclose=AsyncMock())
    sessions = []

    def new_session(**kwargs):
        # Simulate the dev CLI setting a newly registered speech plugin to DEBUG.
        logging.getLogger("livekit.plugins.openai").setLevel(logging.DEBUG)
        session = FakeSession(**kwargs)
        sessions.append(session)
        return session

    for name in ("LIVEKIT_URL", "LIVEKIT_API_KEY", "LIVEKIT_API_SECRET", "OPENAI_API_KEY"):
        monkeypatch.setenv(name, "offline-only")
    monkeypatch.setattr(module, "create_model", lambda _: model)
    monkeypatch.setattr(module, "create_llm", lambda _: object())
    monkeypatch.setattr(module, "create_stt", lambda _: object())
    monkeypatch.setattr(module, "create_tts", lambda _: object())
    monkeypatch.setattr(module, "AgentSession", new_session)
    monkeypatch.setattr(module.silero.VAD, "load", lambda **_: object())
    return model, sessions


async def test_server_deadline_closes_session_and_deletes_room(worker):
    model, sessions = worker
    deadline = int(time.time() * 1000) + 60
    ctx = FakeContext(json.dumps({"lesson_deadline_ms": deadline}))
    await module.interview(ctx)
    await asyncio.wait_for(ctx.stopped.wait(), timeout=1)
    assert ctx.reason == "time_limit"
    assert sessions[0].closed
    assert logging.getLogger("livekit.plugins.openai").level == logging.WARNING
    assert sessions[0].started["record"] is False
    assert sessions[0].options["llm"] is not None
    assert sessions[0].started["agent"].tutor.lesson.id == "mock-interview"
    ctx.delete.assert_awaited_once()
    assert any(
        topic == "tutor.lesson" and value["state"] == "ended" for topic, value in ctx.room.packets
    )
    for callback in ctx.callbacks:
        await callback()
    model.aclose.assert_awaited_once()


@pytest.mark.parametrize("lesson_id", ["everyday-conversation", "cafe-order"])
async def test_selected_lesson_reaches_worker_and_greeting(worker, lesson_id):
    from eng_teacher.teaching.lessons import get_lesson

    _, sessions = worker
    lesson = get_lesson(lesson_id)
    ctx = FakeContext(
        json.dumps(
            {
                "lesson_deadline_ms": int(time.time() * 1000) + 10000,
                "lesson_id": lesson.id,
            }
        )
    )
    await module.interview(ctx)
    assert sessions[0].started["agent"].tutor.lesson is lesson
    assert sessions[0].greetings == [lesson.greeting]
    for shutdown in ctx.callbacks:
        await shutdown()


@pytest.mark.parametrize("lesson_id", [None, "unknown", [], 123])
async def test_invalid_signed_lesson_never_starts_audio(worker, lesson_id):
    _, sessions = worker
    ctx = FakeContext(
        json.dumps(
            {
                "lesson_deadline_ms": int(time.time() * 1000) + 10000,
                "lesson_id": lesson_id,
            }
        )
    )
    await module.interview(ctx)
    assert ctx.reason == "startup_error"
    assert sessions[0].started is None
    assert not sessions[0].greetings
    assert sessions[0].closed
    for shutdown in ctx.callbacks:
        await shutdown()


async def test_missing_deadline_rejected_without_starting_audio(worker):
    model, sessions = worker
    ctx = FakeContext("{}")
    await module.interview(ctx)
    assert ctx.reason == "startup_error"
    assert sessions[0].started is None
    assert sessions[0].closed
    assert any(topic == "tutor.error" for topic, _ in ctx.room.packets)
    ctx.delete.assert_awaited_once()
    for callback in ctx.callbacks:
        await callback()
    model.aclose.assert_awaited_once()


async def test_learner_disconnect_closes_paid_pipeline(worker):
    _, sessions = worker
    ctx = FakeContext(json.dumps({"lesson_deadline_ms": int(time.time() * 1000) + 10000}))
    await module.interview(ctx)
    ctx.room.callbacks["participant_disconnected"](SimpleNamespace(identity="learner"))
    await asyncio.wait_for(ctx.stopped.wait(), timeout=1)
    assert ctx.reason == "learner_disconnected"
    assert sessions[0].closed
    for callback in ctx.callbacks:
        await callback()


async def test_recoverable_speech_error_reports_warning_without_ending_call(worker):
    model, sessions = worker
    ctx = FakeContext(json.dumps({"lesson_deadline_ms": int(time.time() * 1000) + 10000}))
    await module.interview(ctx)
    callback = sessions[0].callbacks["error"]
    callback(SimpleNamespace(error=SimpleNamespace(recoverable=True)))
    for _ in range(20):
        if any(topic == "tutor.error" for topic, _ in ctx.room.packets):
            break
        await asyncio.sleep(0.01)
    warnings = [value for topic, value in ctx.room.packets if topic == "tutor.error"]
    assert warnings and warnings[-1]["recoverable"] is True
    assert ctx.reason is None
    assert not sessions[0].closed
    for shutdown in ctx.callbacks:
        await shutdown()
    model.aclose.assert_awaited_once()


async def test_fatal_speech_error_ends_call(worker):
    _, sessions = worker
    ctx = FakeContext(json.dumps({"lesson_deadline_ms": int(time.time() * 1000) + 10000}))
    await module.interview(ctx)
    sessions[0].callbacks["error"](SimpleNamespace(error=SimpleNamespace(recoverable=False)))
    await asyncio.wait_for(ctx.stopped.wait(), timeout=1)
    assert ctx.reason == "provider_error"
    assert sessions[0].closed
    assert any(
        topic == "tutor.error" and packet["recoverable"] is False
        for topic, packet in ctx.room.packets
    )
    for shutdown in ctx.callbacks:
        await shutdown()


@pytest.mark.parametrize("stage", ["model", "llm", "stt", "tts", "vad", "session"])
async def test_startup_factory_failure_closes_created_resources_and_hides_payload(
    monkeypatch, caplog, stage
):
    created = []
    private = "private-key-and-provider-payload"

    def factory(name):
        def create(*_args, **_kwargs):
            logging.getLogger("livekit.plugins.openai").setLevel(logging.DEBUG)
            if name == stage:
                raise RuntimeError(private)
            resource = SimpleNamespace(aclose=AsyncMock())
            created.append(resource)
            return resource

        return create

    for name in ("LIVEKIT_URL", "LIVEKIT_API_KEY", "LIVEKIT_API_SECRET", "OPENAI_API_KEY"):
        monkeypatch.setenv(name, "offline-only")
    for name in ("model", "llm", "stt", "tts"):
        monkeypatch.setattr(module, "create_" + name, factory(name))
    monkeypatch.setattr(module.silero.VAD, "load", factory("vad"))
    monkeypatch.setattr(module, "AgentSession", factory("session"))
    ctx = FakeContext(json.dumps({"lesson_deadline_ms": int(time.time() * 1000) + 10000}))
    await module.interview(ctx)
    assert ctx.reason == "startup_error"
    ctx.delete.assert_awaited_once()
    for shutdown in ctx.callbacks:
        await shutdown()
    for resource in created:
        resource.aclose.assert_awaited_once()
    assert logging.getLogger("livekit.plugins.openai").level == logging.WARNING
    assert private not in caplog.text
    assert private not in json.dumps(ctx.room.packets)


async def test_missing_credentials_shuts_down_without_building_resources(monkeypatch):
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    create = AsyncMock()
    monkeypatch.setattr(module, "create_model", create)
    ctx = FakeContext(json.dumps({"lesson_deadline_ms": int(time.time() * 1000) + 10000}))
    await module.interview(ctx)
    assert ctx.reason == "startup_error"
    create.assert_not_called()
    ctx.delete.assert_awaited_once()


async def test_session_close_failure_still_deletes_room_and_closes_model(worker):
    model, sessions = worker
    ctx = FakeContext(json.dumps({"lesson_deadline_ms": int(time.time() * 1000) + 10000}))
    await module.interview(ctx)
    sessions[0].aclose = AsyncMock(side_effect=RuntimeError("private-close-failure"))
    sessions[0].callbacks["error"](SimpleNamespace(error=SimpleNamespace(recoverable=False)))
    await asyncio.wait_for(ctx.stopped.wait(), timeout=1)
    assert ctx.reason == "provider_error"
    ctx.delete.assert_awaited_once()
    for shutdown in ctx.callbacks:
        await shutdown()
    model.aclose.assert_awaited_once()


async def test_worker_startup_cancellation_releases_resources_and_propagates(worker):
    model, sessions = worker
    waiting = asyncio.Event()
    ctx = FakeContext(json.dumps({"lesson_deadline_ms": int(time.time() * 1000) + 10000}))

    async def wait_for_learner():
        waiting.set()
        await asyncio.Future()

    ctx.wait_for_participant = wait_for_learner
    task = asyncio.create_task(module.interview(ctx))
    await asyncio.wait_for(waiting.wait(), timeout=1)
    task.cancel()
    with pytest.raises(asyncio.CancelledError):
        await task
    assert ctx.reason == "cancelled"
    assert sessions[0].closed
    ctx.delete.assert_awaited_once()
    for shutdown in ctx.callbacks:
        await shutdown()
    model.aclose.assert_awaited_once()


async def test_background_packet_failure_does_not_log_private_transport_exception(worker, caplog):
    _, sessions = worker
    ctx = FakeContext(json.dumps({"lesson_deadline_ms": int(time.time() * 1000) + 10000}))
    await module.interview(ctx)
    private = "private-packet-provider-payload"
    failed = asyncio.Event()

    async def publish_failure(*_args, **_kwargs):
        failed.set()
        raise RuntimeError(private)

    ctx.room.local_participant.publish_data = publish_failure
    sessions[0].callbacks["error"](SimpleNamespace(error=SimpleNamespace(recoverable=True)))
    await asyncio.wait_for(failed.wait(), timeout=1)
    # Let the task's completion callback retrieve the exception before shutdown.
    await asyncio.sleep(0)
    await asyncio.sleep(0)
    assert ctx.reason is None
    for shutdown in ctx.callbacks:
        await shutdown()
    assert private not in caplog.text
