"""Recognize short, explicit lesson-control requests without consuming speaking retries."""

import re


def explicit_control(text: str) -> tuple[str, str] | None:
    value = text.strip().casefold().rstrip("?!.,। ")
    if not value or len(value) > 160 or "\n" in value:
        return None
    language = "hi" if re.search(r"\bhindi\b|हिंदी|हिन्दी", value) else "en"
    value = " ".join(value.split())
    value = re.sub(
        r"^(?:please[, ]+)?(?:(?:can|could|would|will) you (?:please[, ]+)?)?", "", value
    )
    value = re.sub(r"[,\s]+please$", "", value)
    patterns = (
        (
            "next",
            r"(?:skip(?: this| the| current)? question|skip it|next question|move on|continue|let'?s continue)",
        ),
        (
            "again",
            r"(?:one more try|another (?:try|attempt)|let me try again|i(?: want to| would like to)? try again|give me another try|(?:can|could) i try again|फिर से कोशिश|एक बार और|ek baar aur)",
        ),
        (
            "repeat",
            r"(?:repeat(?: (?:it|that|the (?:correct )?sentence|the correction))?(?: (?:again|slowly))?|say (?:it|that|the (?:correct )?sentence) again|फिर से (?:बोलो|कहो)|दोबारा बोलो|(?:phir se|fir se|dobara) (?:bolo|boliye))",
        ),
        (
            "example",
            r"(?:(?:give|show)(?: me)? (?:an?|one|another) example|(?:another|one) example|(?:ek|एक) (?:example|उदाहरण)(?: (?:do|dikhao|दो|दिखाओ))?)",
        ),
        (
            "translate",
            r"(?:translate(?: (?:it|this|that|the (?:corrected|correct )?sentence))? (?:into|to) hindi|(?:what is|what's) (?:the )?hindi (?:translation|meaning)(?: of (?:this|that|it|the sentence))?|(?:hindi|हिंदी|हिन्दी) (?:translation|अनुवाद)|इसका (?:हिंदी|हिन्दी) (?:अनुवाद|मतलब)(?: बताओ)?|iska hindi (?:translation|matlab)(?: batao)?)",
        ),
        (
            "explain",
            r"(?:explain(?: (?:that|this|it|the correction|the (?:correct )?sentence|the grammar))?(?: (?:to me )?in (?:hindi|english))?|tell me why(?: in (?:hindi|english))?|why is (?:that|this|it|(?:this|that) sentence) correct(?: in (?:hindi|english))?|what does (?:this|that|it) mean(?: in (?:hindi|english))?"
            r"|(?:mujhe )?(?:(?:ye|yeh|isko) )?hindi (?:mein|me) (?:samjhao|samjhaiye|explain karo)"
            r"|(?:मुझे )?(?:(?:यह|ये|इसको) )?(?:हिंदी|हिन्दी) में (?:समझाओ|समझाइए)|समझाओ)",
        ),
    )
    for intent, pattern in patterns:
        if re.fullmatch(pattern, value):
            return intent, language
    return None
