# AILT9019 Tutorial 2 — Agent Practice (Parts A–E)

This repository contains my completed practice work for **AILT9019 Tutorial 2**. It follows the workflow described in `Week_02_tutorial.pdf` and implements the five tasks specified in `Week_02_Build_Start.pdf`.

The project is intentionally small and reproducible. Each part has a short evidence file under `evidence/`.

## Part A — Context Engineering

Part A demonstrates that an agent can produce different answers for the same task when only the session instruction changes.

I used the same explanation task twice:

1. A baseline instruction asking for a concise coding-tutor response.
2. A revised instruction adding an audience and output-format constraint.

Both requests were sent to DeepSeek. The returned wording changed after the instruction changed, even though the underlying task stayed the same. The comparison and acceptance explanation are recorded in [`evidence/part-a.md`](evidence/part-a.md).

## Part B — Building and Reusing a Skill

Part B turns a repeated workflow into a reusable skill. The skill is a meeting-notes cleaner that must:

- output exactly three sections: `Summary`, `Decisions`, and `Action Items`;
- keep each section concise;
- avoid inventing owners or dates that are not present in the notes.

The skill definition is stored in [`my-skill/SKILL.md`](my-skill/SKILL.md). A fake meeting note and the expected skill-shaped result are documented in [`evidence/part-b.md`](evidence/part-b.md).

The same skill is also registered for Pi at [`.pi/skills/meeting-notes-cleaner/SKILL.md`](.pi/skills/meeting-notes-cleaner/SKILL.md).

## Part C — Registering and Calling an MCP Tool

Part C implements a minimal local MCP server using Python and stdio transport. The server is named `week2-date-server` and exposes one tool:

- `current_date` — returns the host's local date.

[`mcp/date_server.py`](mcp/date_server.py) implements the JSON-RPC/MCP server. [`mcp/probe.py`](mcp/probe.py) acts as a small client: it initializes the server, discovers the available tools, calls `current_date`, and prints the real response. The captured discovery and call result are in [`evidence/part-c.md`](evidence/part-c.md).

## Part D — Using Pi with DeepSeek

Part D installs and runs the Pi coding agent with a DeepSeek provider.

- Package: `@earendil-works/pi-coding-agent`
- Provider: DeepSeek
- Authentication: supplied at run time through the `DEEPSEEK_API_KEY` environment variable
- Practice script: [`fibonacci.py`](fibonacci.py)

Pi was used in an isolated directory to create a minimal Fibonacci script. The script was then executed and produced `0 1 1 2 3`. A second Pi session applied the meeting-notes output contract from Part B to sample notes. The transcript and verification notes are in [`evidence/part-d.md`](evidence/part-d.md).

The API key is never stored in this repository, committed to Git, or included in the evidence files.

## Part E — Publishing and Verifying the Work

The completed practice folder was published as a public repository:

**https://github.com/gwdsd1/gwdsd_ailt9019**

The local `practice` repository was pushed to GitHub as the `main` branch. A fresh clone was then created in a separate workspace directory. The clone was checked for the required skills, MCP files, Fibonacci script, evidence files, and a clean Git working tree. The final acceptance notes are in [`evidence/part-e.md`](evidence/part-e.md).

## Repository Layout

```text
.
├── .pi/skills/meeting-notes-cleaner/SKILL.md  Pi skill registration
├── evidence/                                  Part A–E acceptance notes
├── mcp/date_server.py                         Local MCP date server
├── mcp/probe.py                               MCP discovery and call probe
├── my-skill/SKILL.md                          Reusable meeting-notes skill
├── fibonacci.py                              Fibonacci practice script
├── package.json                               Pi dependency declaration
└── pnpm-lock.yaml                             Locked JavaScript dependencies
```

## Running the Local Checks

From the repository root:

```powershell
# Check MCP initialization, tool discovery, and the real tool call
python mcp/probe.py

# Run the Fibonacci script
python fibonacci.py
```

Expected Fibonacci output:

```text
0 1 1 2 3
```

To install the Pi dependency locally:

```powershell
pnpm install
```

To use DeepSeek with Pi, set the key only in the current shell session and do not commit it:

```powershell
$env:DEEPSEEK_API_KEY = "<your-key>"
```

The MCP date server itself has no network dependency.

## Source Documents

- `Week_02_tutorial.pdf` — tutorial workflow and tool guidance.
- `Week_02_Build_Start.pdf` — Part A–E task requirements.
