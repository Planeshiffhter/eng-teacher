"""Fakes verify the worker deadline and cleanup; no LiveKit server is contacted."""

import asyncio
import json
import logging
import time
from types import SimpleNamespace
from unittest.mock import AsyncMock

import pytest

from eng_teacher import agent as module


class FakeSession:
    def __init__(self, **kwargs):
        self.options = kwargs
        self.callbacks = {}
        self.started = None
        self.closed = False

    def on(self, name):
        def register(callback):
            self.callbacks[name] = callback
            return callback

        return register

    async def start(self, **kwargs):
        self.started = kwargs

    async def say(self, *args, **kwargs):
        return None

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
    ctx.delete.assert_awaited_once()
    assert any(
        topic == "tutor.lesson" and value["state"] == "ended" for topic, value in ctx.room.packets
    )
    for callback in ctx.callbacks:
        await callback()
    model.aclose.assert_awaited_once()


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
