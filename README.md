# Week 2 Agent Practice

This folder contains the smallest reproducible implementation of Parts A-E from
`Week_02_Build_Start.pdf`, following the workflow in `Week_02_tutorial.pdf`.

## Contents

- `evidence/part-a.md`: same task with two context instructions.
- `my-skill/SKILL.md`: the reusable meeting-notes skill from Part B.
- `evidence/part-b.md`: a fake meeting note and the skill-shaped result.
- `mcp/date_server.py`: a local MCP server exposing `current_date`.
- `mcp/probe.py`: a small MCP client used to verify the real tool response.
- `evidence/part-c.md`: the captured MCP discovery and tool-call result.
- `fibonacci.py`: the small script created for Part D.
- `evidence/part-d.md`: Pi Agent run notes and skill verification.
- `evidence/part-e.md`: Git commit and fresh-clone verification notes.

## Local checks

From this directory:

```powershell
python mcp/probe.py
python fibonacci.py
```

The MCP server uses stdio and has no network dependency. The DeepSeek key is
never stored in this repository; Pi receives it through `DEEPSEEK_API_KEY`.

