# Part A - Context engineering

Small task used both times: explain why a coding agent can change its output when
only the session instruction changes.

## Attempt 1

Session instruction:

> You are helping me build a small Python tool. Keep answers short and show
> commands I can run.

DeepSeek output:

> Changing only the session instruction alters the agent's context, priorities, or constraints, which reshapes its internal reasoning and decision-making process, thereby producing different outputs even for the same task.

## Attempt 2 (only the instruction changed)

Session instruction:

> You are helping me build a small Python tool. Keep answers short, show
> commands I can run, and always include a usage example for a first-year student.

DeepSeek output:

> Changing only the session instruction alters the AI's context and priorities, which reshapes its internal reasoning and decision-making, so even with the same task, it will generate different code or solutions based on that new guidance.

## Acceptance explanation

The two calls used the same user task but different session instructions. The
second instruction added an audience and format constraint, and the resulting
wording changed accordingly. This is the requested acceptance evidence that a
session-only change can alter the output.
