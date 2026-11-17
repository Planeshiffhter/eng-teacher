"""Exercise tutor policy with authored text and scripted provider replies."""

from dataclasses import dataclass
from typing import Literal
from unittest.mock import call, create_autospec

import pytest

from eng_teacher.teaching.lessons import get_lesson
from eng_teacher.teaching.tutor import InterviewTutor, ModelDecision, RetryDecision, TutorModel

CASE_VERSION = 1

ProviderMethod = Literal["decide", "assess_retry", "explain_correction", "help_with_correction"]
FeedbackAction = Literal["correct", "clarify", "continue", "retry", "assist"]


@dataclass(frozen=True)
class Turn:
    recognized: str
    action: FeedbackAction
    question_index: int
    pending_retry: str | None = None
    corrected: str | None = None
    explanation: str | None = None
    provider: tuple[ProviderMethod, ModelDecision | RetryDecision | str] | None = None


@dataclass(frozen=True)
class Case:
    id: str
    lesson_id: str
    intended_meaning: str
    turns: tuple[Turn, ...]


def correction(sentence: str, explanation: str) -> tuple[ProviderMethod, ModelDecision]:
    return (
        "decide",
        ModelDecision(
            action="correct",
            corrected=sentence,
            explanation=explanation,
            reply="Let's practice this sentence.",
            uncertain=False,
            meaning_preserved=True,
        ),
    )


ACKNOWLEDGE = ModelDecision(
    action="continue",
    corrected=None,
    explanation=None,
    reply="Thanks for telling me.",
    uncertain=False,
    meaning_preserved=True,
)
UNCERTAIN = ModelDecision(
    action="clarify",
    corrected=None,
    explanation=None,
    reply="Could you say that again?",
    uncertain=True,
    meaning_preserved=False,
)
BUDGET = "I managed a budget of 2.5 lakh for the Pune team."
BUDGET_EXPLANATION = "Use 'managed' for completed work and say 'a budget of' before the amount."
BUDGET_EXAMPLE = "For example, I managed a budget for a workshop last month."
BUDGET_HINDI = "पूरे हो चुके काम के लिए 'managed' कहें और रकम से पहले 'a budget of' लगाएँ।"
DEMO = "I did not give the demo in Jaipur."
DEMO_EXPLANATION = "After 'did not', use the base verb 'give'."
HOURS = "I worked for 0.75 hours."
HOURS_EXPLANATION = "Use 'worked' for the past and retain the exact number of hours."
CALL = "I called my sister yesterday."
CALL_EXPLANATION = "Use 'called' for an action that happened yesterday."

CASES = (
    Case(
        "hinglish-budget-help-and-transfer",
        "mock-interview",
        "The learner managed 2.5 lakh for the Pune team and wants to practice this wording.",
        (
            Turn(
                "Maine Pune team ke liye 2.5 lakh ka budget manage kiya",
                "correct",
                0,
                pending_retry=BUDGET,
                corrected=BUDGET,
                explanation=BUDGET_EXPLANATION,
                provider=correction(BUDGET, BUDGET_EXPLANATION),
            ),
            Turn(
                "Could you show me an example?",
                "assist",
                0,
                pending_retry=BUDGET,
                corrected=BUDGET,
                explanation=BUDGET_EXAMPLE,
                provider=("help_with_correction", BUDGET_EXAMPLE),
            ),
            Turn(
                "Explain the correction in Hindi",
                "assist",
                0,
                pending_retry=BUDGET,
                corrected=BUDGET,
                explanation=BUDGET_HINDI,
                provider=("explain_correction", BUDGET_HINDI),
            ),
            Turn("What does budget mean?", "assist", 0, pending_retry=BUDGET, corrected=BUDGET),
            Turn(
                "For the Pune team, I managed a budget of 2.5 lakh.",
                "retry",
                1,
                provider=(
                    "assess_retry",
                    RetryDecision(action="accept", uncertain=False, meaning_preserved=True),
                ),
            ),
            Turn(
                "In my next role, I managed a budget for training.",
                "continue",
                2,
                provider=("decide", ACKNOWLEDGE),
            ),
        ),
    ),
    Case(
        "devanagari-negation-preserved",
        "mock-interview",
        "The learner did not give the demo in Jaipur.",
        (
            Turn(
                "मैंने Jaipur में demo नहीं दिया।",
                "clarify",
                0,
                provider=correction("I gave the demo in Jaipur.", "Use 'gave' for the past."),
            ),
            Turn(
                "मैंने Jaipur में demo नहीं दिया।",
                "correct",
                0,
                pending_retry=DEMO,
                corrected=DEMO,
                explanation=DEMO_EXPLANATION,
                provider=correction(DEMO, DEMO_EXPLANATION),
            ),
            Turn("  I did not give the demo in Jaipur!  ", "retry", 1),
        ),
    ),
    Case(
        "hinglish-keep-name",
        "mock-interview",
        "The learner worked with Meera, a different person from Mira.",
        (
            Turn(
                "Maine Meera ke saath kaam kiya",
                "clarify",
                0,
                provider=correction("I worked with Mira.", "Use 'worked' for completed work."),
            ),
            Turn("I worked with Meera.", "continue", 1, provider=("decide", ACKNOWLEDGE)),
        ),
    ),
    Case(
        "devanagari-keep-decimal",
        "mock-interview",
        "The learner worked for three quarters of an hour.",
        (
            Turn(
                "मैंने 0.75 घंटे काम किया",
                "clarify",
                0,
                provider=correction("I worked for 75 hours.", HOURS_EXPLANATION),
            ),
            Turn(
                "मैंने 0.75 घंटे काम किया",
                "correct",
                0,
                pending_retry=HOURS,
                corrected=HOURS,
                explanation=HOURS_EXPLANATION,
                provider=correction(HOURS, HOURS_EXPLANATION),
            ),
            Turn("I worked for 0.75 hours.", "retry", 1),
        ),
    ),
    Case(
        "regional-and-casual-english",
        "everyday-conversation",
        "The English is already acceptable. The learner explains their day and hobbies.",
        (
            Turn(
                "It's been good. I'll call my aunt once I reach home.",
                "continue",
                1,
                provider=("decide", ACKNOWLEDGE),
            ),
            Turn(
                "I like playing carrom with my cousins.",
                "continue",
                2,
                provider=("decide", ACKNOWLEDGE),
            ),
        ),
    ),
    Case(
        "uncertain-retry-and-skip",
        "everyday-conversation",
        "The learner called their sister yesterday, then chooses to skip after an unclear retry.",
        (
            Turn(
                "Kal maine apni sister ko phone kiya",
                "correct",
                0,
                pending_retry=CALL,
                corrected=CALL,
                explanation=CALL_EXPLANATION,
                provider=correction(CALL, CALL_EXPLANATION),
            ),
            Turn(
                "I called [unclear] yesterday",
                "clarify",
                0,
                pending_retry=CALL,
                provider=(
                    "assess_retry",
                    RetryDecision(action="clarify", uncertain=True, meaning_preserved=False),
                ),
            ),
            Turn("Skip this question", "continue", 1),
        ),
    ),
    Case(
        "uncertain-recognition-then-clear-answer",
        "mock-interview",
        "The first attempt was uncertain. The learner clarifies that they emailed the report.",
        (
            Turn(
                "Maine [unclear] report send ki",
                "clarify",
                0,
                provider=("decide", UNCERTAIN),
            ),
            Turn("I emailed the report.", "continue", 1, provider=("decide", ACKNOWLEDGE)),
        ),
    ),
)


@pytest.mark.parametrize("case", CASES, ids=lambda case: f"v{CASE_VERSION}-{case.id}")
async def test_teaching_policy(case: Case):
    model = create_autospec(TutorModel, instance=True, spec_set=True)
    tutor = InterviewTutor(model, lesson=get_lesson(case.lesson_id))

    for step, turn in enumerate(case.turns, start=1):
        model.reset_mock(return_value=True)
        context = f"turn {step}: {turn.recognized!r}. Intended meaning: {case.intended_meaning}"
        expected_calls = []
        if turn.provider:
            method, reply = turn.provider
            getattr(model, method).return_value = reply
            expected_calls = [
                {
                    "decide": call.decide(
                        turn.recognized, tutor.current_question, tutor.history[-8:]
                    ),
                    "assess_retry": call.assess_retry(
                        turn.recognized, tutor.pending_retry, tutor.pending_explanation
                    ),
                    "explain_correction": call.explain_correction(
                        tutor.pending_retry, tutor.pending_explanation, "hi"
                    ),
                    "help_with_correction": call.help_with_correction(
                        tutor.pending_retry, tutor.pending_explanation, "example"
                    ),
                }[method]
            ]

        feedback = await tutor.turn(turn.recognized)

        assert model.mock_calls == expected_calls, context
        assert feedback.version == 1, context
        assert feedback.original == turn.recognized, context
        assert feedback.action == turn.action, context
        assert feedback.corrected == turn.corrected, context
        assert feedback.explanation == turn.explanation, context
        assert tutor.question_index == turn.question_index, context
        assert tutor.pending_retry == turn.pending_retry, context
        assert not tutor.last_provider_failed, context
        if feedback.action in {"continue", "retry"}:
            assert tutor.current_question in feedback.spoken_response, context
