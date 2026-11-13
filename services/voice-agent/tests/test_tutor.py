from types import SimpleNamespace

import pytest
from pydantic import ValidationError

from eng_teacher.providers import OpenAITutorModel, Settings
from eng_teacher.tutor import InterviewTutor, ModelDecision, risky_change


def decision(**changes):
    fields = dict(
        action="continue",
        corrected=None,
        explanation=None,
        reply="Thanks for sharing.",
        uncertain=False,
        meaning_preserved=True,
    )
    return ModelDecision(**(fields | changes))


class FakeModel:
    def __init__(self, result=None, fail=False):
        self.result = result or decision()
        self.fail = fail
        self.inputs = []

    async def decide(self, original, question, history):
        self.inputs.append((original, question, history))
        if self.fail:
            raise RuntimeError("secret-provider-error-with-transcript")
        return self.result


async def test_mixed_language_correction_original_and_retry_continue():
    model = FakeModel(
        decision(
            action="correct",
            corrected="I handled customer calls.",
            explanation="Use the past tense for finished work.",
        )
    )
    tutor = InterviewTutor(model)
    original = "Maine customer calls handle kiye"
    feedback = await tutor.turn(original)
    assert feedback.original == original
    assert feedback.corrected == "I handled customer calls."
    assert feedback.action == "correct"
    assert "Could you say" in feedback.spoken_response
    retry = await tutor.turn("I handled customer calls")
    assert retry.action == "retry"
    assert "matches the phrase" in retry.spoken_response
    assert "most recent role" in retry.spoken_response
    assert tutor.pending_retry is None
    assert len(model.inputs) == 1
    assert (await tutor.turn("I worked in support.")).action == "correct"
    assert len(model.inputs) == 2


async def test_acceptable_regional_english_is_not_forced_into_correction():
    tutor = InterviewTutor(FakeModel())
    result = await tutor.turn("I work in customer support and I enjoy helping people.")
    assert result.action == "continue"
    assert result.corrected is None
    assert tutor.question_index == 1


@pytest.mark.parametrize(
    "original,corrected",
    [
        ("I didn't handle calls", "I handled calls"),
        ("Maine calls nahi handle kiye", "I handled calls"),
        ("मैंने काम नहीं किया", "I did the work"),
        ("I helped Rohan in Pune", "I helped Rahul in Mumbai"),
        ("I handled 12 tickets", "I handled 20 tickets"),
    ],
)
async def test_suspicious_rewrite_clarifies(original, corrected):
    model = FakeModel(
        decision(action="correct", corrected=corrected, explanation="A grammar suggestion.")
    )
    result = await InterviewTutor(model).turn(original)
    assert result.original == original
    assert result.action == "clarify"
    assert result.corrected is None


def test_guard_allows_name_negation_and_number_preserving_fix():
    assert not risky_change(
        "I didn't handled 12 calls for Rohan", "I didn't handle 12 calls for Rohan."
    )


async def test_uncertainty_clarifies_without_advancing_question():
    tutor = InterviewTutor(FakeModel(decision(uncertain=True)))
    result = await tutor.turn("I worked with [unclear]")
    assert result.action == "clarify"
    assert tutor.question_index == 0
    assert tutor.pending_retry is None


async def test_failed_provider_does_not_leak_error_or_mutate_retry_state():
    tutor = InterviewTutor(FakeModel(fail=True))
    result = await tutor.turn("I need help")
    assert result.action == "clarify"
    assert "secret" not in result.model_dump_json()
    assert tutor.last_provider_failed
    assert not tutor.pending_retry


async def test_nonidentical_retry_continues_without_claiming_pronunciation_grade():
    tutor = InterviewTutor(
        FakeModel(
            decision(
                action="correct",
                corrected="I handle calls.",
                explanation="Use the base verb with I.",
            )
        )
    )
    await tutor.turn("I handles calls")
    result = await tutor.turn("I help customers over the phone")
    assert result.action == "retry"
    assert "Thanks for trying" in result.spoken_response
    assert result.corrected is None
    assert tutor.pending_retry is None


@pytest.mark.parametrize(
    "changes",
    [
        {"action": "correct", "corrected": None},
        {"action": "correct", "corrected": "I work", "explanation": None},
        {"corrected": "invented correction"},
        {"original": "model may not overwrite transcript"},
    ],
)
def test_invalid_model_decision_is_rejected(changes):
    with pytest.raises(ValidationError):
        decision(**changes)


async def test_input_bounds_never_send_long_or_blank_transcript_to_model():
    model = FakeModel()
    tutor = InterviewTutor(model)
    for original in (" ", "x" * 3001):
        result = await tutor.turn(original)
        assert result.action == "clarify"
        assert result.original == original
    assert not model.inputs


async def test_bounded_history():
    tutor = InterviewTutor(FakeModel())
    for _ in range(12):
        await tutor.turn("I enjoy helping customers.")
    assert len(tutor.history) == 8


def test_settings_reject_unknown_provider_and_only_list_missing_names():
    with pytest.raises(ValueError, match="Unsupported provider"):
        Settings.from_env({"STT_PROVIDER": "fake"})
    with pytest.raises(ValueError, match="OPENAI_API_KEY"):
        Settings().validate_credentials({"LIVEKIT_URL": "wss://secret-url"})
    assert Settings.from_env({"TTS_VOICE": "alloy"}).voice == "alloy"


@pytest.mark.parametrize("content", ['{"bad":"schema"}', "not-json", None])
async def test_provider_rejects_malformed_or_empty_json(content):
    class Completions:
        async def create(self, **kwargs):
            assert kwargs["response_format"]["json_schema"]["strict"]
            return SimpleNamespace(
                choices=[SimpleNamespace(message=SimpleNamespace(content=content))]
            )

    client = SimpleNamespace(chat=SimpleNamespace(completions=Completions()))
    model = OpenAITutorModel("test-model", client=client)
    with pytest.raises((ValueError, ValidationError)):
        await model.decide("I work", "Tell me about your work", [])
