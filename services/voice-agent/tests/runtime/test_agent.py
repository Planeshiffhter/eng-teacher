"""Offline SDK tests. These do not call a microphone, network or real speech model."""

import asyncio
import json

import pytest
from livekit import rtc
from livekit.agents import AgentSession
from livekit.agents.voice import io
from livekit.plugins import openai

from eng_teacher.runtime.agent import InterviewAgent, lesson_deadline_ms
from eng_teacher.teaching.tutor import InterviewTutor

from ..teaching.test_tutor import FakeModel, decision


@pytest.mark.parametrize(
    "metadata",
    [
        "",
        "{}",
        "[]",
        "null",
        '{"lesson_deadline_ms": true}',
        '{"lesson_deadline_ms": 999}',
        '{"lesson_deadline_ms": 601001}',
    ],
)
def test_missing_invalid_or_expired_deadline_is_rejected(metadata):
    with pytest.raises(ValueError):
        lesson_deadline_ms(metadata, now_ms=1000)


def test_signed_deadline_survives_reconnect_instead_of_resetting():
    metadata = json.dumps({"lesson_deadline_ms": 600000})
    assert lesson_deadline_ms(metadata, now_ms=1000) == 600000
    assert lesson_deadline_ms(metadata, now_ms=599999) == 600000
    with pytest.raises(ValueError):
        lesson_deadline_ms(metadata, now_ms=600000)


async def test_sdk_scheduler_runs_custom_model_and_fake_tts_then_retry():
    """Exercise real AgentSession routing, including its mandatory configured-LLM gate."""
    packets = []
    spoken = []

    async def publish(topic, data):
        packets.append((topic, data))

    class Sink(io.AudioOutput):
        def __init__(self):
            super().__init__(
                label="offline-test", capabilities=io.AudioOutputCapabilities(pause=False)
            )
            self.frames = 0

        async def capture_frame(self, frame):
            await super().capture_frame(frame)
            self.frames += 1

        def flush(self):
            super().flush()
            if self._pending_playback_count:
                self.on_playback_finished(playback_position=0.01, interrupted=False)

        def clear_buffer(self):
            if self._pending_playback_count:
                self.on_playback_finished(playback_position=0.0, interrupted=True)

    class CapturingAgent(InterviewAgent):
        async def tts_node(self, text, model_settings):
            async for chunk in text:
                spoken.append(str(chunk))
                # A synthetic silent frame proves node flow, not real TTS quality.
                yield rtc.AudioFrame.create(
                    sample_rate=24000, num_channels=1, samples_per_channel=240
                )

    model = FakeModel(
        decision(
            action="correct", corrected="I handle calls.", explanation="Use the base verb with I."
        )
    )
    agent = CapturingAgent(InterviewTutor(model), publish)
    async with AgentSession(
        # No requests reach this object because llm_node is overridden. Its
        # presence matters: SDK automatic and explicit reply paths require it.
        llm=openai.LLM(api_key="offline-test-only"),
        tts=openai.TTS(api_key="offline-test-only"),
    ) as session:
        sink = Sink()
        session.output.audio = sink
        await session.start(agent, record=False)
        await asyncio.wait_for(session.run(user_input="I handles calls"), timeout=10)
        assert packets[0][0] == "tutor.feedback"
        assert packets[0][1]["original"] == "I handles calls"
        assert packets[0][1]["action"] == "correct"
        await asyncio.wait_for(session.run(user_input="I handle calls"), timeout=10)
        assert packets[1][1]["action"] == "retry"
        assert "most recent role" in packets[1][1]["spoken_response"]
        assert all(value is False for value in session._opts.recording_options.values())
    assert "I handle calls" in " ".join(spoken)
    assert sink.frames > 0
    assert len(model.inputs) == 1
