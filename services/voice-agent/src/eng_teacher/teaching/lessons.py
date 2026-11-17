"""Original guided practice, independent of speech providers and transport."""

from __future__ import annotations

import json
from dataclasses import dataclass
from types import MappingProxyType

DEFAULT_LESSON_ID = "mock-interview"


@dataclass(frozen=True)
class LessonDefinition:
    id: str
    title: str
    goal: str
    greeting: str
    questions: tuple[str, ...]
    continuation: str


_INTERVIEW_QUESTIONS = (
    "Tell me a little about yourself and the kind of job you want.",
    "What did you do in your most recent role or project?",
    "Tell me about a time you helped a customer or teammate.",
    "What is one challenge you faced, and how did you handle it?",
    "What is one of your strengths? Can you give an example?",
    "Why are you interested in this role?",
    "What would you like to ask the interviewer?",
)
_EVERYDAY_QUESTIONS = (
    "How has your day been so far?",
    "Tell me about something you enjoy doing in your free time.",
    "What is one small thing that made you smile recently?",
    "Tell me about a meal or a place you like.",
    "Tell me about a small challenge you solved recently.",
    "What are you looking forward to tomorrow?",
    "What would you like to ask me about everyday English?",
)
_CAFE_QUESTIONS = (
    "Welcome to the café. What would you like to drink?",
    "How would you like your drink prepared?",
    "Would you like anything to eat with that?",
    "Is that for here or to go?",
    "Imagine we're out of your first choice. What would you ask for instead?",
    "Let's try a new order to go. Could you order two drinks and say how you'd like one prepared?",
)

# Original content written for this tutor, not copied from the reference projects.
LESSONS = MappingProxyType(
    {
        DEFAULT_LESSON_ID: LessonDefinition(
            id=DEFAULT_LESSON_ID,
            title="Mock interview",
            goal="Practice clear answers about work and experience, one correction at a time.",
            greeting=(
                "Welcome! I'm your AI English practice teacher. We have ten minutes for a mock interview. "
                "You can answer in English, Hindi, or a mix, and interrupt me at any time. "
                + _INTERVIEW_QUESTIONS[0]
            ),
            questions=_INTERVIEW_QUESTIONS,
            continuation="Tell me more about a specific example from your experience.",
        ),
        "everyday-conversation": LessonDefinition(
            id="everyday-conversation",
            title="Everyday English",
            goal="Share everyday experiences in a relaxed conversation and practice a useful phrase.",
            greeting=(
                "Hi! I'm your AI English practice partner. Let's have a relaxed ten-minute conversation. "
                "Take your time; English, Hindi, or a mix is welcome. You can interrupt or skip a question. "
                + _EVERYDAY_QUESTIONS[0]
            ),
            questions=_EVERYDAY_QUESTIONS,
            continuation="Tell me a little more about that, or choose another everyday topic.",
        ),
        "cafe-order": LessonDefinition(
            id="cafe-order",
            title="Café order",
            goal="Practice a polite café order, add details and ask for an alternative.",
            greeting=(
                "Hi! I'm your AI English practice partner. I'll take your order in this role-play. "
                "You can answer in English, Hindi, or a mix. Say give me an example if you need help. "
                + _CAFE_QUESTIONS[0]
            ),
            questions=_CAFE_QUESTIONS,
            continuation="Try one more order. This time, ask how much it costs before paying.",
        ),
    }
)


def get_lesson(lesson_id: object = DEFAULT_LESSON_ID) -> LessonDefinition:
    """Use only a catalog entry; user text can never supply prompts or curriculum."""
    if not isinstance(lesson_id, str) or lesson_id not in LESSONS:
        raise ValueError("Unsupported practice lesson")
    return LESSONS[lesson_id]


def lesson_from_metadata(metadata: str) -> LessonDefinition:
    """Old signed tokens default only when the lesson field is absent."""
    try:
        data = json.loads(metadata)
    except (TypeError, ValueError) as exc:
        raise ValueError("Invalid practice lesson metadata") from exc
    if not isinstance(data, dict):
        raise ValueError("Invalid practice lesson metadata")
    return get_lesson(data.get("lesson_id", DEFAULT_LESSON_ID))
