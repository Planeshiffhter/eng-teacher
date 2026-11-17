"""Offline usage accounting: no provider requests, learner recordings or billing claims."""

import asyncio
import json
import logging
import time
from dataclasses import asdict
from types import SimpleNamespace
from unittest.mock import AsyncMock

import pytest
from livekit.agents import metrics

from eng_teacher.providers.openai import OpenAITutorModel
from eng_teacher.runtime import agent
from eng_teacher.runtime.usage import MAX_TOTAL, LessonUsage, ModelUsageEvent

from .test_lifecycle import FakeContext, FakeSession

PRIVATE = "private-learner-text-and-secret-key"
DECISION = json.dumps(
    dict(
        action="continue",
        corrected=None,
        explanation=None,
        reply="Keep practicing.",
        uncertain=False,
        meaning_preserved=True,
    )
)
RETRY = json.dumps(dict(action="accept", uncertain=False, meaning_preserved=True))


def response(content, usage):
    return SimpleNamespace(
        choices=[SimpleNamespace(message=SimpleNamespace(content=content))],
        usage=usage,
        id=PRIVATE,
    )


def model_with(result=None, error=None, callback=None):
    create = AsyncMock(return_value=result, side_effect=error)
    client = SimpleNamespace(chat=SimpleNamespace(completions=SimpleNamespace(create=create)))
    return OpenAITutorModel(PRIVATE, client=client, usage_callback=callback), create


async def invoke(model, operation):
    if operation == "decide":
        return await model.decide(PRIVATE, "Practice question", [(PRIVATE, PRIVATE)])
    if operation == "assess":
        return await model.assess_retry(PRIVATE, "Target", "Reason")
    if operation == "explain":
        return await model.explain_correction(PRIVATE, "Reason", "hi")
    return await model.help_with_correction(PRIVATE, "Reason", "example")


@pytest.mark.parametrize("operation", ["decide", "explain", "assess", "help"])
async def test_each_model_operation_reports_only_safe_aggregate_usage(operation, caplog):
    events = []
    content = DECISION if operation == "decide" else RETRY if operation == "assess" else PRIVATE
    model, create = model_with(
        response(content, SimpleNamespace(prompt_tokens=17, completion_tokens=9)),
        callback=events.append,
    )
    await invoke(model, operation)
    create.assert_awaited_once()
    assert events == [ModelUsageEvent(operation, True, False, 17, 9)]
    assert PRIVATE not in json.dumps(asdict(events[0]))
    assert PRIVATE not in caplog.text


@pytest.mark.parametrize("operation", ["decide", "explain", "assess", "help"])
async def test_transport_errors_are_counted_without_inventing_usage(operation):
    usage = LessonUsage()
    model, _ = model_with(error=RuntimeError(PRIVATE), callback=usage.record_model)
    with pytest.raises(RuntimeError, match=PRIVATE):
        await invoke(model, operation)
    totals = usage.snapshot()["model"]
    assert totals["requests"] == totals["errors"] == 1
    assert totals["responses"] == totals["responses_missing_usage"] == 0
    assert totals["prompt_tokens"] == totals["completion_tokens"] == 0
    assert totals["operations"][operation]["errors"] == 1
    assert PRIVATE not in json.dumps(usage.snapshot())


@pytest.mark.parametrize(
    "operation,content",
    [
        ("decide", "invalid-json"),
        ("assess", '{"action":"accept"}'),
        ("explain", " "),
        ("help", None),
    ],
)
async def test_response_validation_errors_still_include_reported_token_usage(operation, content):
    usage = LessonUsage()
    model, _ = model_with(
        response(content, SimpleNamespace(prompt_tokens=21, completion_tokens=4)),
        callback=usage.record_model,
    )
    with pytest.raises(ValueError):
        await invoke(model, operation)
    totals = usage.snapshot()["model"]
    assert totals["requests"] == totals["errors"] == totals["responses"] == 1
    assert totals["prompt_tokens"] == 21
    assert totals["completion_tokens"] == 4
    assert totals["responses_missing_usage"] == 0


@pytest.mark.parametrize(
    "reported,expected_prompt,expected_completion",
    [
        (None, 0, 0),
        (SimpleNamespace(prompt_tokens=7), 7, 0),
        (SimpleNamespace(prompt_tokens=True, completion_tokens=3), 0, 3),
        (SimpleNamespace(prompt_tokens=-2, completion_tokens="secret"), 0, 0),
        (SimpleNamespace(prompt_tokens=1.5, completion_tokens=MAX_TOTAL + 1), 0, 0),
    ],
)
async def test_missing_or_invalid_usage_is_distinct_from_a_model_error(
    reported, expected_prompt, expected_completion
):
    usage = LessonUsage()
    model, _ = model_with(response(DECISION, reported), callback=usage.record_model)
    await invoke(model, "decide")
    totals = usage.snapshot()["model"]
    assert totals["requests"] == totals["responses"] == totals["responses_missing_usage"] == 1
    assert totals["errors"] == 0
    assert totals["prompt_tokens"] == expected_prompt
    assert totals["completion_tokens"] == expected_completion


async def test_no_remote_request_means_no_usage_event():
    events = []
    model, create = model_with(callback=events.append)
    assert (
        await model.explain_correction("Target", "Saved explanation", "en") == "Saved explanation"
    )
    with pytest.raises(ValueError, match="Unsupported"):
        await model.help_with_correction("Target", "Reason", "invalid")
    create.assert_not_awaited()
    assert not events


async def test_broken_collector_cannot_change_success_or_mask_provider_error():
    def broken(_event):
        raise RuntimeError("collector failed")

    model, _ = model_with(response(DECISION, None), callback=broken)
    assert (await invoke(model, "decide")).action == "continue"
    model, _ = model_with(error=ValueError("original provider failure"), callback=broken)
    with pytest.raises(ValueError, match="original provider failure"):
        await invoke(model, "help")


async def test_cancelled_request_is_counted_and_cancellation_propagates():
    events = []
    model, _ = model_with(error=asyncio.CancelledError(), callback=events.append)
    with pytest.raises(asyncio.CancelledError):
        await invoke(model, "decide")
    assert events == [ModelUsageEvent("decide", False, True)]


@pytest.mark.parametrize("invalid", [True, -1, 1.2, "private", MAX_TOTAL + 1])
def test_model_events_reject_non_integer_negative_or_unbounded_usage(invalid):
    with pytest.raises(ValueError):
        ModelUsageEvent("decide", True, False, invalid, 0)


def test_collector_keeps_fixed_size_detached_totals_and_ignores_invalid_speech_units():
    usage = LessonUsage()
    for operation in ("decide", "explain", "assess", "help"):
        usage.record_model(ModelUsageEvent(operation, True, False, MAX_TOTAL, 2))
    usage.record_stt(1.25)
    usage.record_tts(31)
    for invalid in (True, -1, "private", float("inf"), float("nan"), MAX_TOTAL + 1):
        usage.record_stt(invalid)
        usage.record_tts(invalid)
    saved = usage.snapshot()
    assert saved["model"]["requests"] == 4
    assert saved["model"]["prompt_tokens"] == MAX_TOTAL
    assert saved["model"]["completion_tokens"] == 8
    assert saved["stt_seconds"] == 1.25
    assert saved["tts_characters"] == 31
    saved["model"]["operations"]["decide"]["requests"] = 999
    assert usage.snapshot()["model"]["operations"]["decide"]["requests"] == 1


async def test_lesson_finish_log_combines_private_model_and_speech_totals(monkeypatch, caplog):
    model = SimpleNamespace(aclose=AsyncMock())
    sessions = []

    def new_session(**kwargs):
        session = FakeSession(**kwargs)
        sessions.append(session)
        return session

    for name in ("LIVEKIT_URL", "LIVEKIT_API_KEY", "LIVEKIT_API_SECRET", "OPENAI_API_KEY"):
        monkeypatch.setenv(name, PRIVATE)
    monkeypatch.setattr(agent, "create_model", lambda _: model)
    monkeypatch.setattr(agent, "create_llm", lambda _: object())
    monkeypatch.setattr(agent, "create_stt", lambda _: object())
    monkeypatch.setattr(agent, "create_tts", lambda _: object())
    monkeypatch.setattr(agent, "AgentSession", new_session)
    monkeypatch.setattr(agent.silero.VAD, "load", lambda **_: object())
    ctx = FakeContext(json.dumps({"lesson_deadline_ms": int(time.time() * 1000) + 10000}))
    with caplog.at_level(logging.INFO, logger="eng_teacher"):
        await agent.interview(ctx)
        model.usage_callback(ModelUsageEvent("decide", True, False, 13, 6))
        model.usage_callback(ModelUsageEvent("help", True, True, 8, 2))
        common = dict(
            label=PRIVATE, request_id=PRIVATE, timestamp=1.0, duration=0.1, streamed=False
        )
        callback = sessions[0].callbacks["metrics_collected"]
        callback(SimpleNamespace(metrics=metrics.STTMetrics(**common, audio_duration=2.5)))
        callback(
            SimpleNamespace(
                metrics=metrics.TTSMetrics(
                    **common, audio_duration=1.0, ttfb=0.1, cancelled=False, characters_count=42
                )
            )
        )
        ctx.room.callbacks["participant_disconnected"](SimpleNamespace(identity="learner"))
        await asyncio.wait_for(ctx.stopped.wait(), timeout=1)
        # Repeated finish triggers must not duplicate the private totals log.
        sessions[0].callbacks["close"](None)
        for cleanup in ctx.callbacks:
            await cleanup()
    records = [
        record.getMessage() for record in caplog.records if "lesson_finished" in record.message
    ]
    assert len(records) == 1
    totals = json.loads(records[0].split(" usage=", 1)[1])
    assert totals["stt_seconds"] == 2.5
    assert totals["tts_characters"] == 42
    assert totals["model"]["requests"] == 2
    assert totals["model"]["errors"] == 1
    assert totals["model"]["prompt_tokens"] == 21
    assert totals["model"]["completion_tokens"] == 8
    assert PRIVATE not in caplog.text
    assert all(topic != "tutor.usage" for topic, _ in ctx.room.packets)
