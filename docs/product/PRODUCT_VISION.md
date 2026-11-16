# Product Vision and Competitive Scope

**Status:** Product ambition and requirements, not shipped features.

## Problem and learner

Many English learners can understand English but struggle to speak spontaneously, especially when they think first in Hindi or another language. We want a tutor that lets them finish, accepts code-switching, preserves meaning, corrects usefully, and helps them apply the correction independently the next day.

**Initial focus:** Hindi–English learners practicing interviews and everyday situations on mobile web. Expand to Bengali, Punjabi, and other languages only after native-speaker evaluation. Build accessible, age-appropriate, privacy-conscious learning experiences.

## Competitor benchmarks (inspiration, not source code)

| Reference product | Experience to benchmark |
|---|---|
| Praktika | Personable avatar-led conversation and roleplay |
| ELSA Speak | Granular pronunciation, stress and intonation feedback |
| Speak | Speaking-first lessons, learner-specific feedback and practice |
| Duolingo | Structured learning paths, repeat use, progress, motivating activities |
| Supernova | Regional-language English-learning workflows and interview practice |

No single download-count claim should be equated with universal quality leadership. Benchmark **our** app using independent learner evaluations, not advertising claims.

## Full product goals

**Conversation and video:** Low-latency, interruptible two-way speech; video-call UI; animated teacher avatar, lip sync and facial motion; captions; audio-only fallback; selectable voices; roleplays and free conversation.

**Teaching:** Grammar and vocabulary corrections, natural phrasing, brief native-language explanations, meaning-preserving rewrites, gentle retry/roleplay progression, configurable correction frequency, correct handling of already acceptable English, CEFR-oriented lessons.

**Pronunciation:** Repeat-after-me practice, phoneme and word-level feedback where validated, stress/intonation exercises, diverse accent support. Do not confuse speech-recognition confidence with pronunciation accuracy.

**Personalization:** Placement/goal selection; learner-approved progress history; recurring mistake groups; spaced-repetition review; personalized follow-up lessons and explanations; dashboards and assessments.

**Platform:** Responsive web, future Android app, authentication, lesson content/admin tools, accessibility, consent/privacy controls, subscriptions after validated unit economics, analytics and operational monitoring.

**AI independence:** Replaceable speech and text inference providers, reproducible teacher evaluations, original teaching content and datasets used with permission, eventual LoRA fine-tuning of an appropriately licensed open-weight model.

## Teaching behavior (core differentiated experience)

1. Let the learner finish and tolerate pauses; support barge-in.
2. If the speech or intent is uncertain, ask a clarifying question.
3. Give **one useful change per turn by default**, not a flood of corrections.
4. Show the original utterance and the suggestion separately; don't change names or negation.
5. Explain simply, invite a retry, then **continue the real conversation**.
6. Keep extra suggestions in the end-of-lesson recap.
7. Never mark valid regional or everyday English incorrect just to produce feedback.
8. Check whether a previously learned pattern is reused on a different question the next day.

## What makes this competitive

A good avatar is table stakes. The measurable advantage should be **learning transfer**: fewer repeated mistakes, preserved intended meaning across language switching, low false-correction rate, good call quality and return use. Measure these before producing additional teacher avatars or gamification.
