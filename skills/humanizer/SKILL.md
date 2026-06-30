---
name: humanizer
description: Use this skill to transform AI-generated text into natural, human-sounding prose by applying a strict humanization protocol.
tags: [writing, humanization, ai-text, editing, tone]
argument-hint: "Paste the AI-generated text you want humanized"
user-invocable: true
disable-model-invocation: false
---

## Process:

1. Draft: Rewrite the provided text using varied sentence lengths, incorporating a mix of short and long sentences. Use first-person ("I") where appropriate to establish a clear stance. Favor specific, concrete details over vague generalizations.
2. Audit: Scan the rewritten text to identify and eliminate all elements from the strict pattern ban list:
   - Banned Words: delve, tapestry, vibrant, pivotal, testament, underscore, intricate, multifaceted, enhance, foster, alignment.
   - Grammatical Tells: Em-dashes (—), "Rule of Three" groupings in prose, and structures like "not only... but also" or "serves/stands as."
   - Clutter & Boilerplate: Phrases like "in order to" or "due to the fact that." Avoid generic sections like "Challenges and Future Prospects."
   - Formatting Fluff: Emojis, Title Case subheadings, bold headers inside lists, and curly quotes.
3. Final Pass: Purge all flagged elements identified in the Audit step. Smooth transitions to ensure the text flows naturally and embodies a genuine human voice. Ensure the final output consistently reflects Rhythmic Variety, Decisive Voice, Grounded Clarity, and Absolute Data Integrity.

## Supporting References

This skill includes a comprehensive ban list:

- **BANNED_PATTERNS.json** — Four categories of patterns to eliminate: banned words (40+ AI-signature words with plain-English replacements), banned phrases (50+ clichéd multi-word patterns), grammatical tells (em-dash overuse, Rule of Three triads, passive-voice hedging, etc.), and formatting fluff (decorative emojis, Title Case headers, boilerplate section names). Also includes four quality check rules (Rhythmic Variety, Decisive Voice, Grounded Clarity, Data Integrity). Located in `references/`.

The AI applies BANNED_PATTERNS.json in the Audit step to flag every violation before the Final Pass.

## Output format:

The output will be a direct, humanized rewrite of the input text. There should be zero conversational filler, introductory text, or explanations accompanying the rewritten content. The output should be plain text, suitable for immediate use.

## Ideal outputs:

The finished product should be text that is indistinguishable from human writing, characterized by:

- Rhythmic Variety: Sentences will exhibit diverse lengths, avoiding predictable or monotonous patterns.
- Decisive Voice: The tone will be clear and assertive, free from detached or hyper-neutral corporate language.
- Grounded Clarity: Vague or high-level claims will be replaced with concrete details and sharp, specific observations.
- Absolute Data Integrity: All facts and data presented will be precise and accurate.
