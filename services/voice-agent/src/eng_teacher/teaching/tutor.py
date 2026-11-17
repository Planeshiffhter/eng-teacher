"""Provider-independent lesson policy; raw recognition and corrections stay separate."""

from __future__ import annotations

import re
from collections.abc import Sequence
from typing import Literal, Protocol
from unicodedata import decimal
from uuid import uuid4

from pydantic import BaseModel, ConfigDict, Field, StrictBool, model_validator

from .controls import explicit_control
from .lessons import LessonDefinition, get_lesson

# Retain these default aliases for callers using the original interview entrypoint.
QUESTIONS = get_lesson().questions
GREETING = get_lesson().greeting
CLARIFICATION = "I want to keep your meaning. Could you say that again, in Hindi or English?"


class ModelDecision(BaseModel):
    """One candidate correction. The model cannot supply or replace the original transcript."""

    model_config = ConfigDict(extra="forbid")
    action: Literal["correct", "clarify", "continue"]
    corrected: str | None = Field(max_length=1200)
    explanation: str | None = Field(max_length=500)
    reply: str = Field(min_length=1, max_length=600)
    uncertain: StrictBool
    meaning_preserved: StrictBool

    @model_validator(mode="after")
    def correction_is_complete(self):
        if self.action == "correct" and (
            not (self.corrected or "").strip() or not (self.explanation or "").strip()
        ):
            raise ValueError("A correction requires a sentence and explanation")
        if self.action != "correct" and self.corrected is not None:
            raise ValueError("Only corrections may contain a corrected sentence")
        return self


class RetryDecision(BaseModel):
    """Text-only semantic check of a retry, never a pronunciation assessment."""

    model_config = ConfigDict(extra="forbid")
    action: Literal["accept", "retry", "clarify"]
    uncertain: StrictBool
    meaning_preserved: StrictBool


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

    async def help_with_correction(self, corrected: str, explanation: str, kind: str) -> str: ...

    async def assess_retry(
        self, original: str, corrected: str, explanation: str
    ) -> RetryDecision: ...


_NEGATION = re.compile(
    r"\b(?:not|no|never|cannot|\w+n't|nahi|nahin|nhi)\b"
    r"|(?<![\w\u0900-\u0963\u0970-\u097f])(?:नहीं|नही|मत)(?![\w\u0900-\u0963\u0970-\u097f])",
    re.IGNORECASE,
)
_NUMBER = re.compile(r"(?:(?<![\w.,])[-+−])?(?:\d+(?:[.,:/-]\d+)*|(?<!\w)\.\d+)")
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


def _number_tokens(text: str) -> list[str]:
    """Preserve number order, repetitions and signs across numeral scripts."""
    return [
        "".join(str(decimal(char)) if char.isdecimal() else char for char in token).replace(
            "−", "-"
        )
        for token in _NUMBER.findall(text)
    ]


def risky_change(original: str, corrected: str) -> bool:
    a, b = original.replace("’", "'"), corrected.replace("’", "'")
    if bool(_NEGATION.search(a)) != bool(_NEGATION.search(b)):
        return True
    if _number_tokens(a) != _number_tokens(b):
        return True
    # Keep distinctive capitalized names/acronyms verbatim. May conservatively reject
    # legitimate rewrites; it does not detect every name or semantic change.
    # In a Romanized Hindi opener such as "Kal maine", the first word marks time.
    name_text = re.sub(r"^\s*(?:aaj|kal)(?=\s+maine\b)", "", a, flags=re.IGNORECASE)
    names = {
        word for word in re.findall(r"\b[A-Z][A-Za-z'-]*\b", name_text) if word not in _NON_NAMES
    }
    return any(not re.search(rf"\b{re.escape(name)}\b", b, flags=re.IGNORECASE) for name in names)


def looks_like_question(text: str) -> bool:
    """Prefer preserving a pending correction to misclassifying a help question as a retry."""
    value = text.strip().casefold()
    return "?" in value or bool(
        re.match(
            r"^(?:what|why|how|when|where|which|who|can|could|would|should|is|are|do|does|did|may|"
            r"tell me|i wonder|i have a question|mujhe|iska matlab|ये|यह|क्या|कैसे|क्यों)\b",
            value,
        )
    )


def normalized_retry(text: str) -> str:
    """Ignore presentation differences without joining words or changing their meaning."""
    value = text.strip().casefold().replace("’", "'")
    # Apostrophes, hyphens, decimal separators and word boundaries can carry
    # meaning. Only sentence-final punctuation is safe to ignore here.
    value = re.sub(r"[\s.,!?;:।]+$", "", value)
    return " ".join(value.split())


class InterviewTutor:
    def __init__(self, model: TutorModel, *, lesson: LessonDefinition | None = None):
        self.model = model
        self.lesson = lesson or get_lesson()
        self.question_index = 0
        self.pending_retry: str | None = None
        self.pending_explanation: str | None = None
        self.history: list[tuple[str, str]] = []
        self.last_provider_failed = False

    @property
    def current_question(self) -> str:
        if self.question_index < len(self.lesson.questions):
            return self.lesson.questions[self.question_index]
        return self.lesson.continuation

    def _next_question(self) -> str:
        self.question_index += 1
        return self.current_question

    async def _assist(self, original: str, command: str, language: str) -> Feedback:
        target = self.pending_retry
        if command == "next":
            self.pending_retry = None
            self.pending_explanation = None
            return Feedback(
                original=original, action="continue", spoken_response=self._next_question()
            )
        if command == "repeat":
            reply = (
                f"The corrected sentence is: {target}. Please try saying it when ready."
                if target
                else f"Our practice question is: {self.current_question}"
            )
            return Feedback(
                original=original, action="assist", corrected=target, spoken_response=reply
            )
        if command == "again":
            reply = (
                f"Of course, take another try. You can say: {target}."
                if target
                else "Of course. Take your time answering the current question."
            )
            return Feedback(
                original=original, action="assist", corrected=target, spoken_response=reply
            )
        if command in {"example", "translate"}:
            if not target:
                return Feedback(
                    original=original,
                    action="assist",
                    spoken_response="Let's answer the current question first, then we can work on an example or translation.",
                )
            try:
                explanation = await self.model.help_with_correction(
                    target, self.pending_explanation or "", command
                )
                if not isinstance(explanation, str) or not explanation.strip():
                    raise ValueError("Empty teaching assistance")
            except Exception:
                self.last_provider_failed = True
                explanation = (
                    "I cannot translate that right now. The English sentence is: " + target
                    if command == "translate"
                    else "For practice, you can say: " + target
                )
            return Feedback(
                original=original,
                action="assist",
                corrected=target,
                explanation=explanation,
                spoken_response=explanation + " Try the corrected sentence when you're ready.",
            )
        if not target:
            return Feedback(
                original=original,
                action="assist",
                spoken_response="Which sentence would you like me to explain?",
            )
        explanation = self.pending_explanation or "Let's practice this sentence."
        if language == "hi":
            try:
                explanation = await self.model.explain_correction(target, explanation, "hi")
                if not isinstance(explanation, str) or not explanation.strip():
                    raise ValueError("Empty explanation")
            except Exception:
                # A failed explanation must not advance the question or end the paid call.
                self.last_provider_failed = True
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
            if normalized_retry(original) == normalized_retry(target) and not risky_change(
                target, original
            ):
                self.pending_retry = None
                self.pending_explanation = None
                feedback = Feedback(
                    original=original,
                    action="retry",
                    spoken_response="That matches the phrase we practiced. "
                    + self._next_question(),
                )
            elif looks_like_question(original):
                feedback = Feedback(
                    original=original,
                    action="assist",
                    corrected=target,
                    spoken_response=(
                        "We can stay with this correction. Ask me to explain it, translate it "
                        "into Hindi, or give an example. When ready, try saying: " + target
                    ),
                )
            else:
                try:
                    assessment = await self.model.assess_retry(
                        original, target, self.pending_explanation or ""
                    )
                except Exception:
                    self.last_provider_failed = True
                    return Feedback(
                        original=original,
                        action="clarify",
                        spoken_response=(
                            "I couldn't check that retry just now. Your correction is still here. "
                            "Please try again."
                        ),
                    )
                if assessment.uncertain or assessment.action == "clarify":
                    feedback = Feedback(
                        original=original,
                        action="clarify",
                        spoken_response="I may have misheard the retry. Could you say it again?",
                    )
                elif (
                    assessment.action != "accept"
                    or not assessment.meaning_preserved
                    or risky_change(target, original)
                ):
                    feedback = Feedback(
                        original=original,
                        action="assist",
                        corrected=target,
                        spoken_response=(
                            "Let's practice the same idea without changing its meaning. "
                            "Try saying: " + target
                        ),
                    )
                else:
                    self.pending_retry = None
                    self.pending_explanation = None
                    feedback = Feedback(
                        original=original,
                        action="retry",
                        spoken_response="Thanks for trying. That expresses the idea. "
                        + self._next_question(),
                    )
        else:
            try:
                decision = await self.model.decide(
                    original,
                    self.current_question,
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
            elif decision.corrected and normalized_retry(original) != normalized_retry(
                decision.corrected
            ):
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
                reply = "Your wording works." if decision.action == "correct" else decision.reply
                feedback = Feedback(
                    original=original,
                    action="continue",
                    spoken_response=reply + " " + self._next_question(),
                )
        self.history.append((original, feedback.spoken_response))
        # Only retain a bounded conversation in process memory, never on disk.
        self.history = self.history[-8:]
        return feedback
