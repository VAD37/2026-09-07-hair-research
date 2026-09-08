# CLAUDE.md — 2026-09-07-hair-research

Hobby research: hairstyle catalog for an East Asian male, medium→shoulder length, digital perm. Public repo, also a GitHub Pages site.

- `README.md` — start here: what is inside, how to use the site, token cost, how to publish.
- `catalog.md` — main deliverable. `sources.md` — every source tried; **read before any new search**.
- `notes/` — raw subagent notes. `images/` — harvested images, PDFs, `index.html` gallery.
- `prompt/` — user prompts per Claude Code session + agent summaries + ccusage cost. Regenerate with `python prompt/_build_prompts.py` (reads `~/.claude/projects/D--researchs-hobby/`).
- `index.html` — style picker site; regenerate with `python build_site.py` after `python images/_namesort.py`.

Rules: research goes through subagents (may drive the user's Chrome); main agent only writes reports. Log every query tried in `sources.md`. Never download behind a login. Commit date convention: same day the research folder was last updated.
