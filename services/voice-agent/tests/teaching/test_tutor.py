from types import SimpleNamespace

import pytest
from pydantic import ValidationError

from eng_teacher.providers.openai import OpenAITutorModel, Settings
from eng_teacher.teaching.controls import explicit_control
from eng_teacher.teaching.tutor import InterviewTutor, ModelDecision, RetryDecision, risky_change


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
    def __init__(self, result=None, fail=False, retry_result=None, retry_fail=False):
        self.result = result or decision()
        self.fail = fail
        self.retry_fail = retry_fail
        self.retry_result = retry_result or RetryDecision(
            action="accept", uncertain=False, meaning_preserved=True
        )
        self.inputs = []
        self.retry_inputs = []

    async def explain_correction(self, corrected, explanation, language):
        assert language == "hi"
        return "भूतकाल के लिए इस क्रिया का इस्तेमाल करते हैं।"

    async def help_with_correction(self, corrected, explanation, kind):
        assert kind in ("example", "translate")
        return (
            "एक उदाहरण: मैं ग्राहकों से बात करता हूँ।"
            if kind == "translate"
            else "For example, I handled a call yesterday."
        )

    async def assess_retry(self, original, corrected, explanation):
        self.retry_inputs.append((original, corrected, explanation))
        if self.retry_fail:
            raise RuntimeError("secret-retry-provider-error")
        return self.retry_result

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


async def test_presentation_only_correction_does_not_require_retry():
    original = "  I’ve completed the course! "
    tutor = InterviewTutor(
        FakeModel(
            decision(
                action="correct",
                corrected="I've completed the course.",
                explanation="End the sentence with a period.",
            )
        )
    )
    result = await tutor.turn(original)
    assert result.original == original
    assert result.action == "continue"
    assert result.corrected is None
    assert result.explanation is None
    assert tutor.pending_retry is None
    assert tutor.question_index == 1


@pytest.mark.parametrize(
    "original,corrected",
    [
        ("I didn't handle calls", "I handled calls"),
        ("I mustn't handle calls", "I must handle calls"),
        ("Maine calls nahi handle kiye", "I handled calls"),
        ("Maine calls nhi handle kiye", "I handled calls"),
        ("मैंने काम नहीं किया", "I did the work"),
        ("I helped Rohan in Pune", "I helped Rahul in Mumbai"),
        ("Kal helped me in Pune", "A friend helped me in Pune"),
        ("I handled 12 tickets", "I handled 20 tickets"),
        ("I worked from 9 to 5", "I worked from 5 to 9"),
        ("I packed 2 red pens and 2 blue pens", "I packed 2 red pens and blue pens"),
        ("It was −5 degrees", "It was 5 degrees"),
        ("I used .5 of a litre", "I used 5 litres"),
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


@pytest.mark.parametrize(
    "original,corrected",
    [
        ("इसका मतलब मैंने कल सीखा।", "I learned what this means yesterday."),
        ("मुझे १२ टिकट मिले।", "I received 12 tickets."),
        ("I measured −5 degrees", "I measured -5 degrees."),
    ],
)
def test_guard_allows_preserved_meaning_across_scripts(original, corrected):
    assert not risky_change(original, corrected)


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


@pytest.mark.parametrize("command", ["Give an example", "Translate that into Hindi"])
async def test_failed_teaching_help_reports_recoverable_failure_without_advancing(command):
    class FailingHelp(FakeModel):
        async def help_with_correction(self, corrected, explanation, kind):
            raise RuntimeError("private-provider-payload")

    tutor = InterviewTutor(
        FailingHelp(decision(action="correct", corrected="I worked.", explanation="Past tense."))
    )
    await tutor.turn("I work yesterday")
    feedback = await tutor.turn(command)
    assert tutor.last_provider_failed
    assert tutor.pending_retry == "I worked."
    assert tutor.question_index == 0
    assert feedback.action == "assist"
    assert "private-provider-payload" not in feedback.model_dump_json()


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
        {"action": "correct", "corrected": " ", "explanation": "Reason"},
        {"action": "correct", "corrected": "I worked.", "explanation": " "},
        {"action": "correct", "corrected": "I work", "explanation": None},
        {"corrected": "invented correction"},
        {"original": "model may not overwrite transcript"},
        {"uncertain": "false"},
        {"uncertain": 0},
        {"meaning_preserved": "true"},
        {"meaning_preserved": 1},
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


@pytest.mark.parametrize(
    "input_text,expected",
    [
        ("Please explain that in Hindi", ("explain", "hi")),
        ("Can you repeat the correct sentence?", ("repeat", "en")),
        ("One more try, please.", ("again", "en")),
        ("Skip this question.", ("next", "en")),
        ("हिंदी में समझाओ", ("explain", "hi")),
        ("Please explain that in English", ("explain", "en")),
        ("Could you give me an example?", ("example", "en")),
        ("Translate that into Hindi", ("translate", "hi")),
        ("What is the Hindi meaning of that?", ("translate", "hi")),
        ("Can you please give me another example?", ("example", "en")),
        ("Mujhe isko Hindi mein samjhaiye", ("explain", "hi")),
        ("मुझे यह हिंदी में समझाइए।", ("explain", "hi")),
        ("Ek example dikhao, please", ("example", "en")),
        ("Dobara boliye.", ("repeat", "en")),
        ("Ek baar aur", ("again", "en")),
        ("Iska Hindi matlab batao", ("translate", "hi")),
        ("Why is this sentence correct?", ("explain", "en")),
        ("I explained the situation yesterday", None),
        ("My teacher asked me to explain that in Hindi", None),
    ],
)
def test_voice_control_recognition(input_text, expected):
    assert explicit_control(input_text) == expected


async def test_explain_repeat_another_try_keeps_same_pending_correction():
    model = FakeModel(
        decision(
            action="correct",
            corrected="I handled customer calls.",
            explanation="Use past tense for finished work.",
        )
    )
    tutor = InterviewTutor(model)
    initial = await tutor.turn("Maine customer calls handle kiye")
    assert initial.action == "correct"
    for command in (
        "Mujhe isko Hindi mein samjhaiye",
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
    tutor = InterviewTutor(
        FakeModel(decision(action="correct", corrected="I work.", explanation="Use base verb."))
    )
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

    tutor = InterviewTutor(
        FailingModel(decision(action="correct", corrected="I worked.", explanation="Past tense."))
    )
    await tutor.turn("I work yesterday.")
    result = await tutor.turn("Explain that in Hindi.")
    assert result.action == "assist"
    assert tutor.pending_retry == "I worked."
    assert tutor.question_index == 0
    assert "secret" not in result.model_dump_json()
    assert tutor.last_provider_failed


@pytest.mark.parametrize("command", ["Give an example", "Please show an example"])
def test_example_controls_accept_short_natural_requests(command):
    assert explicit_control(command) == ("example", "en")


async def test_help_followups_never_advance_or_consume_retry():
    model = FakeModel(
        decision(
            action="correct",
            corrected="I handled customer calls.",
            explanation="Use past tense for completed work.",
        )
    )
    tutor = InterviewTutor(model)
    await tutor.turn("I handle calls yesterday")
    assist_responses = []
    for command in (
        "Please explain that in English",
        "Could you give me an example?",
        "Translate that into Hindi",
        "Why is this sentence correct?",
        "Can I say it differently",
        "Could you give me an example?",
    ):
        result = await tutor.turn(command)
        assist_responses.append(result)
        assert result.action == "assist"
        assert tutor.pending_retry == "I handled customer calls."
        assert tutor.question_index == 0
    assert "For example" in assist_responses[1].spoken_response
    assert "एक उदाहरण" in assist_responses[2].spoken_response
    assert "Use past tense for completed work." in assist_responses[3].spoken_response
    assert not model.retry_inputs
    result = await tutor.turn("I handled customer calls.")
    assert result.action == "retry"
    assert tutor.question_index == 1
    assert tutor.pending_retry is None


async def test_unrelated_utterance_cannot_advance_pending_retry():
    model = FakeModel(
        decision(action="correct", corrected="I worked in Delhi.", explanation="Use past tense."),
        retry_result=RetryDecision(action="retry", uncertain=False, meaning_preserved=False),
    )
    tutor = InterviewTutor(model)
    await tutor.turn("I working Delhi")
    result = await tutor.turn("I have a different question about my salary")
    assert result.action == "assist"
    assert tutor.pending_retry == "I worked in Delhi."
    assert tutor.question_index == 0
    assert len(model.retry_inputs) == 1


async def test_acceptable_paraphrase_advances_after_semantic_validation():
    model = FakeModel(
        decision(
            action="correct", corrected="I assisted customers.", explanation="Use past tense."
        ),
        retry_result=RetryDecision(action="accept", uncertain=False, meaning_preserved=True),
    )
    tutor = InterviewTutor(model)
    await tutor.turn("I assist customers yesterday")
    result = await tutor.turn("I helped customers.")
    assert result.action == "retry"
    assert tutor.question_index == 1
    assert model.retry_inputs[0][0] == "I helped customers."


async def test_retry_guard_rejects_name_number_or_negation_change_even_if_model_accepts():
    model = FakeModel(
        decision(
            action="correct",
            corrected="I didn't handle 12 calls for Rohan.",
            explanation="Keep the negative past tense.",
        ),
        retry_result=RetryDecision(action="accept", uncertain=False, meaning_preserved=True),
    )
    tutor = InterviewTutor(model)
    await tutor.turn("I didn't handled 12 calls for Rohan.")
    result = await tutor.turn("I handled 20 calls for Rahul.")
    assert result.action == "assist"
    assert tutor.question_index == 0
    assert tutor.pending_retry is not None


async def test_decimal_retry_cannot_bypass_numeric_guard_even_if_model_accepts():
    model = FakeModel(
        decision(
            action="correct",
            corrected="I handled 1.2 million calls.",
            explanation="Use past tense and keep the same quantity.",
        ),
        retry_result=RetryDecision(action="accept", uncertain=False, meaning_preserved=True),
    )
    tutor = InterviewTutor(model)
    await tutor.turn("I handle 1.2 million calls.")
    result = await tutor.turn("I handled 12 million calls.")
    assert result.action == "assist"
    assert tutor.pending_retry == "I handled 1.2 million calls."
    assert tutor.question_index == 0


async def test_reversed_quantities_cannot_advance_retry_even_if_model_accepts():
    target = "I gave 2 books to Rohan and 3 books to Rahul."
    model = FakeModel(decision(action="correct", corrected=target, explanation="Past tense."))
    tutor = InterviewTutor(model)
    await tutor.turn("I give 2 books to Rohan and 3 books to Rahul yesterday")
    retry = "I gave 3 books to Rohan and 2 books to Rahul."
    feedback = await tutor.turn(retry)
    assert feedback.action == "assist"
    assert tutor.pending_retry == target
    assert tutor.question_index == 0


@pytest.mark.parametrize(
    "original,target,retry",
    [
        (
            "We're ready for interview.",
            "We're ready for the interview.",
            "Were ready for the interview.",
        ),
        ("I re-sign contract.", "I re-sign contracts.", "I resign contracts."),
        ("I handle a board review.", "I handled a board review.", "I handled aboard review."),
    ],
)
async def test_meaningful_punctuation_and_word_boundaries_require_semantic_retry(
    original, target, retry
):
    model = FakeModel(
        decision(action="correct", corrected=target, explanation="Keep the intended meaning."),
        retry_result=RetryDecision(action="retry", uncertain=False, meaning_preserved=False),
    )
    tutor = InterviewTutor(model)
    await tutor.turn(original)
    result = await tutor.turn(retry)
    assert model.retry_inputs == [(retry, target, "Keep the intended meaning.")]
    assert result.action == "assist"
    assert tutor.pending_retry == target
    assert tutor.question_index == 0


@pytest.mark.parametrize(
    "original,target,retry",
    [
        ("I handle calls yesterday.", "I handled calls.", "  i   handled calls!  "),
        (
            "I handle 1.2 million calls yesterday.",
            "I handled 1.2 million calls.",
            "I handled 1.2 million calls?",
        ),
        ("I re-sign contract.", "I re-sign contracts.", "I re-sign contracts।"),
        (
            "We're ready for interview.",
            "We're ready for the interview.",
            "We’re ready for the interview!",
        ),
    ],
)
async def test_equivalent_retry_allows_terminal_punctuation_spacing_and_typographic_apostrophe(
    original, target, retry
):
    model = FakeModel(
        decision(action="correct", corrected=target, explanation="Practice this phrase.")
    )
    tutor = InterviewTutor(model)
    await tutor.turn(original)
    result = await tutor.turn(retry)
    assert result.action == "retry"
    assert tutor.pending_retry is None
    assert tutor.question_index == 1
    assert not model.retry_inputs


async def test_retry_uncertainty_and_provider_failure_keep_correction():
    model = FakeModel(
        decision(action="correct", corrected="I handled calls.", explanation="Past tense."),
        retry_result=RetryDecision(action="clarify", uncertain=True, meaning_preserved=False),
    )
    tutor = InterviewTutor(model)
    await tutor.turn("I handle calls yesterday")
    unclear = await tutor.turn("I handled maybe called")
    assert unclear.action == "clarify"
    assert tutor.question_index == 0
    model.retry_fail = True
    failed = await tutor.turn("I worked on calls")
    assert failed.action == "clarify"
    assert tutor.last_provider_failed
    assert "secret" not in failed.model_dump_json()
    assert tutor.pending_retry == "I handled calls."
    assert tutor.question_index == 0


@pytest.mark.parametrize(
    "payload",
    [
        {"action": "invalid", "uncertain": False, "meaning_preserved": True},
        {"action": "accept", "uncertain": "yes", "meaning_preserved": True},
        {"action": "accept", "uncertain": 0, "meaning_preserved": True},
        {"action": "accept", "uncertain": False, "meaning_preserved": "true"},
        {"action": "accept", "uncertain": False, "meaning_preserved": 1},
        {
            "action": "accept",
            "uncertain": False,
            "meaning_preserved": True,
            "pronunciation_score": 100,
        },
    ],
)
def test_retry_decision_is_schema_strict(payload):
    with pytest.raises(ValidationError):
        RetryDecision(**payload)
