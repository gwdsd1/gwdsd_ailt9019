# Part B - Skill acceptance

Input:

```text
[MEETING NOTES]
Alex will send the slides by Friday.
Question: should the demo use the date or weather tool?
Sam will test the README next Monday.
```

Expected skill-shaped output:

```text
Action items
- Alex, send the slides, Friday
- Sam, test the README, next Monday

Open questions
- Should the demo use the date or weather tool?
```

The output follows `my-skill/SKILL.md`: action lines use `owner, task, due
date`, open questions are separate, and no unrelated content is added.

