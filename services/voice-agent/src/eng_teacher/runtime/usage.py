"""Bounded, in-memory lesson totals. Never retain text, identifiers or provider payloads."""

from __future__ import annotations

import math
from collections.abc import Callable
from dataclasses import dataclass
from typing import Literal

Operation = Literal["decide", "explain", "assess", "help"]
OPERATIONS: tuple[Operation, ...] = ("decide", "explain", "assess", "help")
MAX_TOTAL = 2**53 - 1


def token_count(value: object) -> int | None:
    """Accept reported integer units only; missing/invalid usage stays unknown."""
    return value if type(value) is int and 0 <= value <= MAX_TOTAL else None


@dataclass(frozen=True, slots=True)
class ModelUsageEvent:
    operation: Operation
    response_received: bool
    failed: bool
    prompt_tokens: int | None = None
    completion_tokens: int | None = None

    def __post_init__(self) -> None:
        if self.operation not in OPERATIONS:
            raise ValueError("Unknown model usage operation")
        if type(self.response_received) is not bool or type(self.failed) is not bool:
            raise ValueError("Model usage flags must be booleans")
        for value in (self.prompt_tokens, self.completion_tokens):
            if value is not None and token_count(value) is None:
                raise ValueError("Model usage requires nonnegative integer token counts")
            if value is not None and not self.response_received:
                raise ValueError("Token usage requires a received response")


UsageCallback = Callable[[ModelUsageEvent], None]
_FIELDS = (
    "requests",
    "errors",
    "responses",
    "responses_missing_usage",
    "prompt_tokens",
    "completion_tokens",
)


class LessonUsage:
    """Fixed-size aggregate counters for logical adapter calls, not SDK retry attempts."""

    def __init__(self) -> None:
        self._model = {operation: dict.fromkeys(_FIELDS, 0) for operation in OPERATIONS}
        self._stt_seconds = 0.0
        self._tts_characters = 0

    def record_model(self, event: ModelUsageEvent) -> None:
        values = self._model[event.operation]
        increments = {
            "requests": 1,
            "errors": int(event.failed),
            "responses": int(event.response_received),
            "responses_missing_usage": int(
                event.response_received
                and (event.prompt_tokens is None or event.completion_tokens is None)
            ),
            "prompt_tokens": event.prompt_tokens or 0,
            "completion_tokens": event.completion_tokens or 0,
        }
        for key, increment in increments.items():
            values[key] = min(MAX_TOTAL, values[key] + increment)

    def record_stt(self, seconds: object) -> None:
        if type(seconds) in (int, float) and 0 <= seconds <= MAX_TOTAL and math.isfinite(seconds):
            self._stt_seconds = min(float(MAX_TOTAL), self._stt_seconds + seconds)

    def record_tts(self, characters: object) -> None:
        value = token_count(characters)
        if value is not None:
            self._tts_characters = min(MAX_TOTAL, self._tts_characters + value)

    def snapshot(self) -> dict:
        operations = {operation: values.copy() for operation, values in self._model.items()}
        totals = {
            key: min(MAX_TOTAL, sum(values[key] for values in operations.values()))
            for key in _FIELDS
        }
        return {
            "stt_seconds": self._stt_seconds,
            "tts_characters": self._tts_characters,
            "model": {**totals, "operations": operations},
        }
