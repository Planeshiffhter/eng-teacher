"""Original lesson selection and correction state; no real providers are called."""

import json
from dataclasses import FrozenInstanceError
from pathlib import Path

import pytest

from eng_teacher.teaching.lessons import (
    DEFAULT_LESSON_ID,
    LESSONS,
    get_lesson,
    lesson_from_metadata,
)
from eng_teacher.teaching.tutor import InterviewTutor

from .test_tutor import FakeModel, decision


def test_catalog_matches_cross_runtime_contract_and_is_immutable():
    contract = json.loads(
        (Path(__file__).parents[4] / "tests/contracts/lesson-catalog.json").read_text()
    )
    assert set(LESSONS) == set(contract["lesson_ids"])
    assert DEFAULT_LESSON_ID == contract["default_lesson_id"]
    with pytest.raises(TypeError):
        LESSONS["new"] = get_lesson()
    with pytest.raises(FrozenInstanceError):
        get_lesson().title = "Replaced"
    for lesson in LESSONS.values():
        assert lesson.questions and all(question.strip() for question in lesson.questions)
        assert lesson.questions[0] in lesson.greeting
        assert lesson.goal and lesson.continuation


def test_legacy_metadata_defaults_only_when_lesson_is_omitted():
    assert lesson_from_metadata('{"lesson_deadline_ms": 123}').id == DEFAULT_LESSON_ID
    assert get_lesson().id == DEFAULT_LESSON_ID
    assert (
        lesson_from_metadata('{"lesson_id":"everyday-conversation"}').id == "everyday-conversation"
    )


@pytest.mark.parametrize(
    "value", [None, 1, True, [], {}, "", "constructor", "__proto__", "unknown"]
)
def test_invalid_lesson_selection_never_becomes_a_prompt(value):
    with pytest.raises(ValueError, match="Unsupported practice lesson"):
        lesson_from_metadata(json.dumps({"lesson_id": value}))


@pytest.mark.parametrize("metadata", ["null", "[]", "true", "42", '"mock-interview"', "{bad"])
def test_metadata_requires_a_json_object(metadata):
    with pytest.raises(ValueError):
        lesson_from_metadata(metadata)


async def test_everyday_help_retry_and_continuation_keep_the_selected_lesson():
    lesson = get_lesson("everyday-conversation")
    model = FakeModel(
        decision(action="correct", corrected="I enjoyed my day.", explanation="Past tense.")
    )
    tutor = InterviewTutor(model, lesson=lesson)
    await tutor.turn("I enjoy my day yesterday")
    assert model.inputs[0][1] == lesson.questions[0]
    for command in ["Please explain that in English", "Can you give an example?", "Repeat that"]:
        result = await tutor.turn(command)
        assert result.action == "assist"
        assert tutor.question_index == 0
        assert tutor.pending_retry == "I enjoyed my day."
    retried = await tutor.turn("I enjoyed my day.")
    assert retried.action == "retry"
    assert lesson.questions[1] in retried.spoken_response
    assert tutor.pending_retry is None
    repeat = await tutor.turn("Repeat that")
    assert lesson.questions[1] in repeat.spoken_response
    for _ in lesson.questions:
        await tutor.turn("Skip this question")
    assert tutor.current_question == lesson.continuation
    assert lesson.continuation in (await tutor.turn("Repeat that")).spoken_response


async def test_instances_do_not_share_lesson_or_progress():
    interview = InterviewTutor(FakeModel())
    everyday = InterviewTutor(FakeModel(), lesson=get_lesson("everyday-conversation"))
    await everyday.turn("My day went well.")
    assert interview.question_index == 0
    assert everyday.question_index == 1
    assert interview.current_question != everyday.current_question
