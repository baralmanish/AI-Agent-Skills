# Humanizer — Quick Reference

## Trigger Phrases

```
"Humanize this"
"Make this sound less like AI"
"Rewrite this to sound more natural"
"Remove the AI tone from this"
"Make this sound like a real person wrote it"
```

## How It Works

1. **Draft** — rewrites with varied sentence lengths, first-person where appropriate, concrete details
2. **Audit** — scans against BANNED_PATTERNS.json (words, phrases, grammatical tells, formatting)
3. **Final Pass** — removes all flagged items, smooths transitions, delivers plain text output

## What Gets Removed

| Category             | Examples                                                                         |
| -------------------- | -------------------------------------------------------------------------------- |
| Banned words         | delve, tapestry, vibrant, leverage, utilize, holistic, robust, seamless          |
| Banned phrases       | "In today's fast-paced world", "It is worth noting", "In conclusion"             |
| Grammatical tells    | Em-dash overuse, Rule of Three triads, "not only… but also", "serves as"         |
| Formatting fluff     | Decorative emojis, Title Case headers, every paragraph ending in a vague summary |
| Boilerplate sections | "Challenges and Future Prospects", "Key Takeaways", "The Road Ahead"             |

## Four Quality Properties of the Output

| Property         | Meaning                                                            |
| ---------------- | ------------------------------------------------------------------ |
| Rhythmic Variety | Mix of short punchy and longer sentences — no monotonous pattern   |
| Decisive Voice   | Direct and owned — no passive hedging on the writer's own views    |
| Grounded Clarity | Abstract claims paired with concrete details or specific examples  |
| Data Integrity   | All facts and numbers preserved exactly — no rounding or invention |

## Output Format

- Plain text only
- No introduction, no explanation — just the rewritten content
- Ready to copy-paste directly

## Reference Files

- `references/BANNED_PATTERNS.json` — complete ban list: words, phrases, grammatical tells, formatting fluff, structural boilerplate, and quality check rules
