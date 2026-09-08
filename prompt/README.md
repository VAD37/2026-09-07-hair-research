# prompt/ — what was asked, what the agents did, what it cost

Every Claude Code session that touched this folder. Each file holds **only the user's typed prompts** (verbatim, including typos), the slash commands run, every subagent launched with a one-line summary of what it did, and the token/cost line from [ccusage](https://github.com/ryoppippi/ccusage). Tool output, page content and assistant prose are not included.

Regenerate: `python prompt/_build_prompts.py` (reads `~/.claude/projects/D--researchs-hobby/`).

## Sessions

| # | Date (UTC+7) | Session | Prompts | Agents | Models | Tokens in (fresh + cache write) | Cache read | Tokens out | Cost USD |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 2026-09-07 10:30→21:21 | [768fd652](01-2026-09-07-768fd652.md) | 3 | 7 | fable-5-1, sonnet-5, opus-5 | 1,003,918 | 14,800,565 | 176,864 | 19.31 |
| 2 | 2026-09-08 15:48→15:50 | [932e8f92](02-2026-09-08-932e8f92.md) | 0 | 0 | fable-5-1 | 36,398 | 610,157 | 4,058 | 1.08 |
| 3 | 2026-09-08 15:53→18:19 | [9820d435](03-2026-09-08-9820d435.md) | 3 | 12 | fable-5-1, opus-5 | 1,787,439 | 89,975,915 | 499,507 | 73.29 |
| 4 | 2026-09-09 09:24→09:25 | [ac311da8](04-2026-09-09-ac311da8.md) | 1 | 0 | fable-5-1 | 24,353 | 298,326 | 1,164 | 0.62 |
| 5 | 2026-09-28 13:22→13:40 | [f0a57ed2](05-2026-09-28-f0a57ed2.md) | 1 | 0 | fable-5-1 | 275,122 | 5,086,224 | 46,888 | 9.11 |
| | **Total** | | 8 | 19 | | **3,127,230** | **110,771,187** | **728,481** | **103.41** |

Cost is ccusage's estimate at list API prices (fable-5-1, opus-5, sonnet-5), counting subagent turns inside their parent session. Cache read tokens dominate because every subagent turn re-reads a large cached context; they are billed at a fraction of fresh input. Raw numbers per model: `ccusage.json`.

## Model breakdown

| Session | Model | Fresh in | Cache write | Cache read | Out | Cost USD |
|---|---|---|---|---|---|---|
| 768fd652 | claude-opus-5 | 208 | 563,780 | 8,774,046 | 97,266 | 10.34 |
| 768fd652 | claude-fable-5-1 | 888 | 203,150 | 3,258,515 | 53,435 | 7.56 |
| 768fd652 | claude-sonnet-5 | 72 | 235,820 | 2,768,004 | 26,163 | 1.40 |
| 932e8f92 | claude-fable-5-1 | 198 | 36,200 | 610,157 | 4,058 | 1.08 |
| 9820d435 | claude-opus-5 | 1,164 | 1,461,120 | 84,448,271 | 436,803 | 62.28 |
| 9820d435 | claude-fable-5-1 | 890 | 324,265 | 5,527,644 | 62,704 | 11.01 |
| ac311da8 | claude-fable-5-1 | 130 | 24,223 | 298,326 | 1,164 | 0.62 |
| f0a57ed2 | claude-fable-5-1 | 1,316 | 273,806 | 5,086,224 | 46,888 | 9.11 |
