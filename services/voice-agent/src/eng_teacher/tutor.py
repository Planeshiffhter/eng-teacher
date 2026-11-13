"""Provider-independent lesson policy; raw recognition and corrections stay separate."""

from __future__ import annotations

import re
from collections.abc import Sequence
from typing import Literal, Protocol
from uuid import uuid4

from pydantic import BaseModel, ConfigDict, Field, model_validator

from .controls import explicit_control

QUESTIONS = (
    "Tell me a little about yourself and the kind of job you want.",
    "What did you do in your most recent role or project?",
    "Tell me about a time you helped a customer or teammate.",
    "What is one challenge you faced, and how did you handle it?",
    "What is one of your strengths? Can you give an example?",
    "Why are you interested in this role?",
    "What would you like to ask the interviewer?",
)
GREETING = (
    "Welcome! I'm your AI English practice teacher. We have ten minutes for a mock interview. "
    "You can answer in English, Hindi, or a mix, and interrupt me at any time. " + QUESTIONS[0]
)
CLARIFICATION = "I want to keep your meaning. Could you say that again, in Hindi or English?"


class ModelDecision(BaseModel):
    """One candidate correction. The model cannot supply or replace the original transcript."""

    model_config = ConfigDict(extra="forbid")
    action: Literal["correct", "clarify", "continue"]
    corrected: str | None = Field(max_length=1200)
    explanation: str | None = Field(max_length=500)
    reply: str = Field(min_length=1, max_length=600)
    uncertain: bool
    meaning_preserved: bool

    @model_validator(mode="after")
    def correction_is_complete(self):
        if self.action == "correct" and (not self.corrected or not self.explanation):
            raise ValueError("A correction requires a sentence and explanation")
        if self.action != "correct" and self.corrected is not None:
            raise ValueError("Only corrections may contain a corrected sentence")
        return self


class Feedback(BaseModel):
    model_config = ConfigDict(extra="forbid")
    version: Literal[1] = 1
    turn_id: str = Field(default_factory=lambda: str(uuid4()))
    original: str
    corrected: str | None = None
    explanation: str | None = None
    action: Literal["correct", "clarify", "continue", "retry", "assist"]
    spoken_response: str


class TutorModel(Protocol):
    async def decide(
        self, original: str, question: str, history: Sequence[tuple[str, str]]
    ) -> ModelDecision: ...

    async def explain_correction(self, corrected: str, explanation: str, language: str) -> str: ...


_NEGATION = re.compile(
    r"\b(?:not|no|never|cannot|can't|won't|isn't|aren't|wasn't|weren't|don't|doesn't|didn't|haven't|hasn't|hadn't|wouldn't|shouldn't|couldn't|nahi|nahin)\b|नहीं|नही|मत",
    re.IGNORECASE,
)
# Conservative guard, not a linguistic proof: suspicious changes trigger clarification.
_NON_NAMES = {
    "I",
    "I'm",
    "I’ve",
    "I've",
    "The",
    "A",
    "An",
    "My",
    "We",
    "They",
    "He",
    "She",
    "It",
    "In",
    "At",
    "On",
    "When",
    "But",
    "And",
    "Because",
    "Yes",
    "No",
    "Maine",
    "Main",
}


def risky_change(original: str, corrected: str) -> bool:
    a, b = original.replace("’", "'"), corrected.replace("’", "'")
    if bool(_NEGATION.search(a)) != bool(_NEGATION.search(b)):
        return True
    if set(re.findall(r"\d+(?:\.\d+)?", a)) != set(re.findall(r"\d+(?:\.\d+)?", b)):
        return True
    # Keep distinctive capitalized names/acronyms verbatim. May conservatively reject
    # legitimate rewrites; it does not detect every name or semantic change.
    names = {word for word in re.findall(r"\b[A-Z][A-Za-z'-]*\b", a) if word not in _NON_NAMES}
    return any(not re.search(rf"\b{re.escape(name)}\b", b, flags=re.IGNORECASE) for name in names)


class InterviewTutor:
    def __init__(self, model: TutorModel):
        self.model = model
        self.question_index = 0
        self.pending_retry: str | None = None
        self.pending_explanation: str | None = None
        self.history: list[tuple[str, str]] = []
        self.last_provider_failed = False

    def _next_question(self) -> str:
        self.question_index += 1
        if self.question_index < len(QUESTIONS):
            return QUESTIONS[self.question_index]
        return "Tell me more about a specific example from your experience."


    async def _assist(self, original: str, command: str, language: str) -> Feedback:
        target = self.pending_retry
        if command == "next":
            self.pending_retry = None
            self.pending_explanation = None
            return Feedback(original=original, action="continue", spoken_response=self._next_question())
        if command == "repeat":
            reply = (
                f"The corrected sentence is: {target}. Please try saying it when ready."
                if target else f"The interview question is: {QUESTIONS[min(self.question_index, len(QUESTIONS)-1)]}"
            )
            return Feedback(original=original, action="assist", corrected=target, spoken_response=reply)
        if command == "again":
            reply = (
                f"Of course, take another try. You can say: {target}."
                if target else "Of course. Take your time answering the current question."
            )
            return Feedback(original=original, action="assist", corrected=target, spoken_response=reply)
        if not target:
            return Feedback(original=original, action="assist", spoken_response="Which sentence would you like me to explain?")
        explanation = self.pending_explanation or "Let's practice this sentence."
        if language == "hi":
            try:
                explanation = await self.model.explain_correction(target, explanation, "hi")
                if not isinstance(explanation, str) or not explanation.strip():
                    raise ValueError("Empty explanation")
            except Exception:
                # A failed explanation must not advance the question or end the paid call.
                explanation = "माफ़ कीजिए, हिंदी में विस्तार से समझाने में समस्या हुई। सही वाक्य है: " + target
        return Feedback(
            original=original,
            action="assist",
            corrected=target,
            explanation=explanation,
            spoken_response=f"{explanation} Try saying: {target}",
        )

    async def turn(self, original: str) -> Feedback:
        self.last_provider_failed = False
        # Bound provider input without altering what is displayed as the original.
        if not original.strip() or len(original) > 3000:
            return Feedback(original=original, action="clarify", spoken_response=CLARIFICATION)
        control = explicit_control(original)
        if control:
            feedback = await self._assist(original, *control)
        elif self.pending_retry:
            target = self.pending_retry
            self.pending_retry = None
            self.pending_explanation = None
            normalize = lambda value: re.sub(r"[^\w]", "", value.casefold())  # noqa: E731
            if normalize(original) == normalize(target):
                reply = "That matches the phrase we practiced. "
            else:
                # Do not pretend to grade pronunciation or demand an identical paraphrase.
                reply = (
                    "Thanks for trying. You can keep practicing that phrase after our interview. "
                )
            feedback = Feedback(
                original=original, action="retry", spoken_response=reply + self._next_question()
            )
        else:
            try:
                decision = await self.model.decide(
                    original,
                    QUESTIONS[min(self.question_index, len(QUESTIONS) - 1)],
                    self.history[-8:],
                )
            except Exception:
                # Never expose provider payloads (which can include utterances or keys).
                self.last_provider_failed = True
                return Feedback(
                    original=original,
                    action="clarify",
                    spoken_response="My teaching service is temporarily unavailable. Please try again in a moment.",
                )
            if (
                decision.uncertain
                or not decision.meaning_preserved
                or decision.action == "clarify"
                or (
                    decision.action == "correct"
                    and risky_change(original, decision.corrected or "")
                )
            ):
                feedback = Feedback(
                    original=original, action="clarify", spoken_response=CLARIFICATION
                )
            elif decision.action == "correct":
                self.pending_retry = decision.corrected
                self.pending_explanation = decision.explanation
                feedback = Feedback(
                    original=original,
                    action="correct",
                    corrected=decision.corrected,
                    explanation=decision.explanation,
                    spoken_response=(
                        f"Try saying: {decision.corrected} {decision.explanation} "
                        "Could you say that once in your own voice?"
                    ),
                )
            else:
                feedback = Feedback(
                    original=original,
                    action="continue",
                    spoken_response=decision.reply + " " + self._next_question(),
                )
        self.history.append((original, feedback.spoken_response))
        # Only retain a bounded conversation in process memory, never on disk.
        self.history = self.history[-8:]
        return feedback
