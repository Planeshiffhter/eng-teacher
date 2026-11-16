"""Recognize short, explicit lesson-control requests without consuming speaking retries."""
import re


def explicit_control(text: str) -> tuple[str, str] | None:
    value = text.strip().casefold().rstrip("?!.,। ")
    if not value or len(value) > 160 or "\n" in value:
        return None
    language = "hi" if re.search(r"\bhindi\b|हिंदी|हिन्दी", value) else "en"
    value = re.sub(r"^(?:please\s+)?(?:(?:can|could|would|will)\s+you\s+)?", "", value)
    value = re.sub(r"[,\s]+please$", "", value)
    patterns = (
        ("next", r"(?:skip(?: this| the| current)? question|skip it|next question|move on|continue|let'?s continue)"),
        ("again", r"(?:one more try|another (?:try|attempt)|let me try again|i(?: want to| would like to)? try again|give me another try|(?:can|could) i try again|फिर से कोशिश|एक बार और)"),
        ("repeat", r"(?:repeat(?: (?:it|that|the (?:correct )?sentence|the correction))?(?: (?:again|slowly))?|say (?:it|that|the (?:correct )?sentence) again|फिर से (?:बोलो|कहो)|दोबारा बोलो)"),
        ("explain", r"(?:explain(?: (?:that|this|it|the correction|the (?:correct )?sentence|the grammar))?(?: (?:to me )?in (?:hindi|english))?|tell me why(?: in (?:hindi|english))?|what does (?:this|that|it) mean(?: in (?:hindi|english))?|hindi (?:mein|me) samjhao|(?:हिंदी|हिन्दी) में समझाओ|समझाओ)"),
    )
    for intent, pattern in patterns:
        if re.fullmatch(pattern, value):
            return intent, language
    return None
