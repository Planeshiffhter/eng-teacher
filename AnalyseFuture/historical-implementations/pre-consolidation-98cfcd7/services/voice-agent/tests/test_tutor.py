from types import SimpleNamespace

import pytest
from pydantic import ValidationError

from eng_teacher.controls import explicit_control
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

    async def explain_correction(self, corrected, explanation, language):
        assert language == 'hi'
        return 'भूतकाल के लिए इस क्रिया का इस्तेमाल करते हैं।'

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


@pytest.mark.parametrize("input_text,expected", [
    ("Please explain that in Hindi", ("explain", "hi")),
    ("Can you repeat the correct sentence?", ("repeat", "en")),
    ("One more try, please.", ("again", "en")),
    ("Skip this question.", ("next", "en")),
    ("हिंदी में समझाओ", ("explain", "hi")),
    ("I explained the situation yesterday", None),
])
def test_voice_control_recognition(input_text, expected):
    assert explicit_control(input_text) == expected


async def test_explain_repeat_another_try_keeps_same_pending_correction():
    model = FakeModel(decision(
        action="correct",
        corrected="I handled customer calls.",
        explanation="Use past tense for finished work.",
    ))
    tutor = InterviewTutor(model)
    initial = await tutor.turn("Maine customer calls handle kiye")
    assert initial.action == "correct"
    for command in (
        "Please explain that in Hindi",
        "Can you repeat the correct sentence?",
        "One more try, please.",
    ):
        response = await tutor.turn(command)
        assert response.action == "assist"
        assert tutor.pending_retry == "I handled customer calls."
        assert tutor.question_index == 0
    assert "भूतकाल" in tutor.history[-3][1]
    assert (await tutor.turn("I handled customer calls.")).action == "retry"
    assert tutor.question_index == 1
    assert tutor.pending_retry is None
    assert len(model.inputs) == 1


async def test_skip_explicitly_advances_and_clears_retry():
    tutor = InterviewTutor(FakeModel(decision(
        action="correct", corrected="I work.", explanation="Use base verb."
    )))
    await tutor.turn("I works.")
    skipped = await tutor.turn("Skip this question.")
    assert skipped.action == "continue"
    assert tutor.question_index == 1
    assert tutor.pending_retry is None
    assert (await tutor.turn("Please explain that in Hindi")).action == "assist"
    assert tutor.question_index == 1


async def test_explanation_provider_failure_does_not_consume_retry():
    class FailingModel(FakeModel):
        async def explain_correction(self, corrected, explanation, language):
            raise RuntimeError("provider failure secret payload")

    tutor = InterviewTutor(FailingModel(decision(
        action="correct", corrected="I worked.", explanation="Past tense."
    )))
    await tutor.turn("I work yesterday.")
    result = await tutor.turn("Explain that in Hindi.")
    assert result.action == "assist"
    assert tutor.pending_retry == "I worked."
    assert tutor.question_index == 0
    assert "secret" not in result.model_dump_json()
