"""Build prompt/ from Claude Code session logs.

Reads every session .jsonl under ~/.claude/projects/D--researchs-hobby/ (plus its subagents/ folders),
keeps ONLY the user's own prompt text (no tool output, no assistant prose, no system-injected
task notifications or compaction summaries), lists every subagent launched with a short summary of
what it did, and attaches ccusage token cost per session.

Usage:  python prompt/_build_prompts.py [path/to/ccusage-session.json]
        (without the argument it runs `npx -y ccusage@latest session --json --offline`)

Outputs: prompt/README.md, prompt/NN-YYYY-MM-DD-<sid8>.md, prompt/ccusage.json
"""
import glob
import json
import os
import subprocess
import sys
from collections import Counter
from datetime import datetime, timedelta, timezone

HERE = os.path.dirname(os.path.abspath(__file__))
LOGS = os.path.join(os.path.expanduser("~"), ".claude", "projects", "D--researchs-hobby")
TZ = timezone(timedelta(hours=7))  # Asia/Ho_Chi_Minh
TOKEN_KEYS = ("input_tokens", "output_tokens", "cache_creation_input_tokens", "cache_read_input_tokens")

# Hand-written summaries. Keyed by session id prefix / agent id. Anything not listed falls back to
# the agent's own final message, truncated.
SESSION_SUMMARY = {
    "768fd652": (
        "Pass 1. Main agent read the brief, split it into five research lanes and launched five "
        "subagents in parallel (four opus, one sonnet). They wrote notes/01-05 (reddit street "
        "findings, KR/JP salon glossary and styles, books, maintenance/cost, image refs). Main agent "
        "then merged them into catalog.md, sources.md and README.md. Context was compacted once. "
        "Later the user asked to download every referenced image; two sonnet agents were launched "
        "for that but the Claude in Chrome extension was not connected, so both stopped without "
        "output and the session ended with instructions for connecting Chrome Canary."
    ),
    "932e8f92": (
        "Housekeeping at the hobby root: ran /init and /project-audit, which wrote and then trimmed "
        "the parent folder's CLAUDE.md to a one-line pointer per topic folder."
    ),
    "9820d435": (
        "Pass 2. Main agent verified the Chrome extension was connected, then launched six opus "
        "subagents in parallel, each owning one region/source: hairmode.jp preview PDFs, JP catalog "
        "images, KR salon lookbooks, CN/TW/HK, VN/SEA, and Pinterest/IG/Reddit. Each agent drove "
        "the user's logged-in Chrome (or curl for URLs found that way), downloaded into images/<region>/ "
        "and wrote notes/06-11. Main agent wrote catalog.md sections 8-13, updated sources.md, and "
        "built the thumbnail gallery images/index.html. The user then asked which cuts work with a "
        "digital perm and whether a messy grunge look is possible, and asked to sort every image "
        "into categories with a digital-vs-cold verdict. Six vision-classification agents were "
        "started, then stopped (TaskStop) in favour of a filename-keyword sort: images/_namesort.py, "
        "images/classified.csv, catalog.md section 14, and the gallery regrouped by category with "
        "digital/either/cold badges."
    ),
    "ac311da8": (
        "One-off copy of the research folder to another machine over ssh (tar piped through ssh, "
        "since rsync is not on Windows). No research content changed."
    ),
    "f0a57ed2": (
        "Repo packaging. Renamed the folder to a date-prefixed name, patched the hardcoded path in "
        "images/_namesort.py, added CLAUDE.md, .nojekyll, .gitignore, a root index.html style-picker "
        "site (build_site.py), rewrote README.md with cost and publishing steps, generated this "
        "prompt/ folder from the session logs and ccusage, then git init and one commit backdated to "
        "the day the research folder was last updated (2026-09-08)."
    ),
}

AGENT_SUMMARY = {
    # session 768fd652 (pass 1)
    "a3226a358e4d62bf6": "Reddit via the user's Chrome (old.reddit search pages); WebFetch and the sandboxed browser were blocked. Wrote notes/01 with 18 styles/findings and the access matrix.",
    "a7799fff973367e96": "KR/JP salon catalogs via WebSearch/WebFetch/Chrome. Wrote notes/02: ~90-term glossary, 30 styles, image refs, price table, 51-row search log.",
    "a6fb8df476cc07213": "Books and print references via WebSearch/WebFetch. Wrote notes/03 with ~28 books/mooks and 47 logged search attempts.",
    "ad3281fecd56f1375": "Perm maintenance, longevity and salon cost by region via WebSearch/WebFetch. Wrote notes/04 (8 sections, 47 logged searches).",
    "ae14b77258491e3df": "Pinterest/Instagram/YouTube image refs via WebSearch + Chrome screenshots. Wrote notes/05 (~38 refs); Instagram skipped at login wall.",
    "a7ebacd2d8595a611": "Was to fetch reddit gallery image URLs through Chrome; extension not connected after 3 retries, stopped with no output.",
    "a08d9369cb5dd3324": "Was to collect Pinterest/IG/Google image URLs through Chrome; extension not connected after 3 retries, stopped with no output.",
    # session 9820d435 (pass 2)
    "af75ce5f3e2d1249a": "Found hairmode.jp WooCommerce API -> flipbook -> raw PDF route; downloaded 42 preview PDFs (1,192 pages) to images/pdf/ and 23 sample spreads to images/jp-samples/. Wrote notes/06.",
    "ad9d810a8a44504f2": "Hot Pepper Beauty, OZmall, LIPPS and Bing image harvest via Chrome + curl; 482 images to images/jp/ grouped by silhouette. Wrote notes/07.",
    "ae5ec5a404f405ab8": "Found mamedene.com JSON stylebook API (successor of Kakao Hairshop); 171 screened images to images/kr/. Wrote notes/08.",
    "afe8a72fd3bb9803a": "360 image search JSON route (Baidu dead); 150 CN + 18 StyleMap TW images to images/cn/. Wrote notes/09.",
    "acfcaa19f4e0fe785": "VN/TH/ID/SG/MY/PH sources via Chrome + curl; 170 images to images/sea/ with local terminology and prices. Wrote notes/10.",
    "a0a889bb40c84074b": "Pinterest hubs, Instagram /popular/ tags, reddit .json, YouTube thumbs, Lemon8 via Chrome; 515 downloaded, 245 kept after contact-sheet filtering in images/social/. Wrote notes/11.",
    "ab3ce076953eb8a09": "Vision classification of images/jp 0-241: built contact sheets, then stopped by main agent (TaskStop) before finishing.",
    "a5f809716294374f9": "Vision classification of images/jp 241-482: built contact sheets, then stopped by main agent (TaskStop) before finishing.",
    "a9a92e58627afcee7": "Vision classification of images/kr: stopped by main agent (TaskStop) right after reading the brief.",
    "ae400b7daff17b290": "Vision classification of images/social: built contact sheets, then stopped by main agent (TaskStop).",
    "a3928a6fcb85cea3b": "Vision classification of images/cn: built contact sheets, then stopped by main agent (TaskStop).",
    "a0948e28c6c0e3b44": "Vision classification of images/sea: stopped by main agent (TaskStop) right after reading the brief.",
}


def load(path):
    out = []
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            try:
                out.append(json.loads(line))
            except ValueError:
                pass
    return out


def text_of(content):
    if isinstance(content, str):
        return content
    return "\n".join(x.get("text", "") for x in content or [] if isinstance(x, dict) and x.get("type") == "text")


def is_injected(txt):
    """System-injected user turns: task notifications, slash-command wrappers, compaction summaries."""
    t = txt.lstrip()
    return (t.startswith("<task-notification>") or t.startswith("<command-") or t.startswith("<local-command")
            or t.startswith("This session is being continued from a previous conversation")
            or t.startswith("[Request interrupted"))


def slash_command(txt):
    t = txt.lstrip()
    if t.startswith("<command-name>"):
        return t.split("<command-name>")[1].split("</command-name>")[0].strip()
    return None


def local(ts):
    return datetime.fromisoformat(ts.replace("Z", "+00:00")).astimezone(TZ)


def session_info(path):
    recs = load(path)
    sid = os.path.basename(path)[:-6]
    first = last = None
    prompts, commands, agents = [], [], []
    tools = Counter()
    compactions = 0
    for o in recs:
        ts = o.get("timestamp")
        if ts:
            first = first or ts
            last = ts
        t = o.get("type")
        if t == "user" and not o.get("isSidechain") and not o.get("isMeta"):
            c = o.get("message", {}).get("content")
            if isinstance(c, list) and c and all(isinstance(x, dict) and x.get("type") == "tool_result" for x in c):
                continue
            txt = text_of(c)
            if not txt.strip():
                continue
            cmd = slash_command(txt)
            if cmd:
                commands.append((ts, cmd))
            elif txt.lstrip().startswith("This session is being continued"):
                compactions += 1
            elif not is_injected(txt):
                prompts.append((ts, txt.strip()))
        elif t == "assistant":
            for x in o.get("message", {}).get("content") or []:
                if isinstance(x, dict) and x.get("type") == "tool_use":
                    tools[x.get("name")] += 1
                    if x.get("name") == "Agent":
                        inp = x.get("input", {})
                        agents.append({"ts": ts, "tool_use_id": x.get("id"), "type": inp.get("subagent_type"),
                                       "model": inp.get("model"), "desc": inp.get("description"),
                                       "prompt": inp.get("prompt", "")})
    # map agent launches to subagent transcript files via tool-use id in meta.json
    subs = {}
    for mp in glob.glob(os.path.join(LOGS, sid, "subagents", "*.meta.json")):
        with open(mp, encoding="utf-8") as fh:
            meta = json.load(fh)
        aid = os.path.basename(mp).replace("agent-", "").replace(".meta.json", "")
        jp = mp.replace(".meta.json", ".jsonl")
        srecs = load(jp) if os.path.exists(jp) else []
        stools = Counter()
        sfirst = slast = None
        final = ""
        for o in srecs:
            if o.get("timestamp"):
                sfirst = sfirst or o["timestamp"]
                slast = o["timestamp"]
            if o.get("type") == "assistant":
                for x in o.get("message", {}).get("content") or []:
                    if isinstance(x, dict) and x.get("type") == "tool_use":
                        stools[x.get("name")] += 1
                    elif isinstance(x, dict) and x.get("type") == "text" and x.get("text", "").strip():
                        final = x["text"].strip()
        subs[aid] = {"id": aid, "meta": meta, "tools": stools, "first": sfirst, "last": slast, "final": final}
    for a in agents:
        a["sub"] = next((s for s in subs.values() if s["meta"].get("toolUseId") == a["tool_use_id"]), None)
        if a["sub"] is None:  # fall back: same description
            a["sub"] = next((s for s in subs.values() if s["meta"].get("description") == a["desc"]), None)
    return {"sid": sid, "first": first, "last": last, "prompts": prompts, "commands": commands,
            "agents": agents, "tools": tools, "compactions": compactions}


def ccusage(arg):
    if arg and os.path.exists(arg):
        with open(arg, encoding="utf-8") as fh:
            return json.load(fh)
    out = subprocess.run("npx -y ccusage@latest session --json --offline", shell=True, capture_output=True,
                         text=True, encoding="utf-8")
    return json.loads(out.stdout)


def fmt_tokens(n):
    return f"{n:,}"


def main():
    sessions = sorted((session_info(p) for p in glob.glob(os.path.join(LOGS, "*.jsonl"))), key=lambda s: s["first"])
    cc = ccusage(sys.argv[1] if len(sys.argv) > 1 else None)
    rows = {r.get("period") or r.get("sessionId"): r for r in cc.get("session", [])}
    kept = [rows[s["sid"]] for s in sessions if s["sid"] in rows]
    with open(os.path.join(HERE, "ccusage.json"), "w", encoding="utf-8") as fh:
        json.dump({"generated": datetime.now(TZ).isoformat(timespec="seconds"),
                   "command": "npx -y ccusage@latest session --json --offline (filtered to this project's session ids)",
                   "session": kept}, fh, indent=1, ensure_ascii=False)

    # remove stale per-session files
    for f in glob.glob(os.path.join(HERE, "[0-9][0-9]-*.md")):
        os.remove(f)

    index = ["# prompt/ — what was asked, what the agents did, what it cost", "",
             "Every Claude Code session that touched this folder. Each file holds **only the user's typed prompts** "
             "(verbatim, including typos), the slash commands run, every subagent launched with a one-line summary of "
             "what it did, and the token/cost line from [ccusage](https://github.com/ryoppippi/ccusage). "
             "Tool output, page content and assistant prose are not included.", "",
             "Regenerate: `python prompt/_build_prompts.py` (reads `~/.claude/projects/D--researchs-hobby/`).", "",
             "## Sessions", "",
             "| # | Date (UTC+7) | Session | Prompts | Agents | Models | Tokens in (fresh + cache write) | Cache read | Tokens out | Cost USD |",
             "|---|---|---|---|---|---|---|---|---|---|"]
    tot = Counter()
    total_cost = 0.0
    for i, s in enumerate(sessions, 1):
        r = rows.get(s["sid"], {})
        d = local(s["first"])
        fname = f"{i:02d}-{d:%Y-%m-%d}-{s['sid'][:8]}.md"
        cost = r.get("totalCost", 0.0)
        total_cost += cost
        fresh = r.get("inputTokens", 0) + r.get("cacheCreationTokens", 0)
        tot["fresh"] += fresh
        tot["read"] += r.get("cacheReadTokens", 0)
        tot["out"] += r.get("outputTokens", 0)
        index.append(f"| {i} | {d:%Y-%m-%d %H:%M}→{local(s['last']):%H:%M} | [{s['sid'][:8]}]({fname}) | {len(s['prompts'])} | "
                     f"{len(s['agents'])} | {', '.join(m.replace('claude-', '') for m in r.get('modelsUsed', []))} | "
                     f"{fmt_tokens(fresh)} | {fmt_tokens(r.get('cacheReadTokens', 0))} | {fmt_tokens(r.get('outputTokens', 0))} | {cost:.2f} |")
        write_session(i, s, r, fname)
    index.append(f"| | **Total** | | {sum(len(s['prompts']) for s in sessions)} | {sum(len(s['agents']) for s in sessions)} | | "
                 f"**{fmt_tokens(tot['fresh'])}** | **{fmt_tokens(tot['read'])}** | **{fmt_tokens(tot['out'])}** | **{total_cost:.2f}** |")
    index += ["",
              "Cost is ccusage's estimate at list API prices (fable-5-1, opus-5, sonnet-5), counting subagent turns "
              "inside their parent session. Cache read tokens dominate because every subagent turn re-reads a large "
              "cached context; they are billed at a fraction of fresh input. Raw numbers per model: `ccusage.json`.", "",
              "## Model breakdown", "", "| Session | Model | Fresh in | Cache write | Cache read | Out | Cost USD |", "|---|---|---|---|---|---|---|"]
    for s in sessions:
        r = rows.get(s["sid"], {})
        for mb in r.get("modelBreakdowns", []):
            index.append(f"| {s['sid'][:8]} | {mb['modelName']} | {fmt_tokens(mb['inputTokens'])} | {fmt_tokens(mb['cacheCreationTokens'])} | "
                         f"{fmt_tokens(mb['cacheReadTokens'])} | {fmt_tokens(mb['outputTokens'])} | {mb['cost']:.2f} |")
    with open(os.path.join(HERE, "README.md"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(index) + "\n")
    patch_root_readme(sessions, rows, tot, total_cost)
    print(f"{len(sessions)} sessions, total ${total_cost:.2f}")


def patch_root_readme(sessions, rows, tot, total_cost):
    """Rewrite the block between <!-- cost:start --> and <!-- cost:end --> in ../README.md."""
    path = os.path.join(HERE, "..", "README.md")
    if not os.path.exists(path):
        return
    block = ["<!-- cost:start -->",
             "| Session | Date | What | Agents | Fresh + cache-write in | Cache read | Out | USD |",
             "|---|---|---|---|---|---|---|---|"]
    short = {"768fd652": "Pass 1: reddit, KR/JP salon, books, cost, image refs → catalog.md",
             "932e8f92": "/init + /project-audit at the parent folder",
             "9820d435": "Pass 2: 42 PDFs + 1,255 images across JP/KR/CN/SEA/social, gallery, digital-vs-cold sort",
             "ac311da8": "Copy folder to another machine",
             "f0a57ed2": "Git repo, picker site, prompt/ folder, README"}
    for s in sessions:
        r = rows.get(s["sid"], {})
        fresh = r.get("inputTokens", 0) + r.get("cacheCreationTokens", 0)
        block.append(f"| {s['sid'][:8]} | {local(s['first']):%Y-%m-%d} | {short.get(s['sid'][:8], '')} | {len(s['agents'])} | "
                     f"{fmt_tokens(fresh)} | {fmt_tokens(r.get('cacheReadTokens', 0))} | {fmt_tokens(r.get('outputTokens', 0))} | {r.get('totalCost', 0):.2f} |")
    block.append(f"| **Total** | | {len(sessions)} sessions, {sum(len(s['prompts']) for s in sessions)} user prompts | "
                 f"{sum(len(s['agents']) for s in sessions)} | **{fmt_tokens(tot['fresh'])}** | **{fmt_tokens(tot['read'])}** | "
                 f"**{fmt_tokens(tot['out'])}** | **{total_cost:.2f}** |")
    block.append(f"\nGenerated {datetime.now(TZ):%Y-%m-%d %H:%M} UTC+7 by `prompt/_build_prompts.py`.")
    block.append("<!-- cost:end -->")
    with open(path, encoding="utf-8") as fh:
        txt = fh.read()
    a, b = txt.find("<!-- cost:start -->"), txt.find("<!-- cost:end -->")
    if a < 0 or b < 0:
        return
    txt = txt[:a] + "\n".join(block) + txt[b + len("<!-- cost:end -->"):]
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(txt)


def write_session(i, s, r, fname):
    d0, d1 = local(s["first"]), local(s["last"])
    lines = [f"# Session {i} — {d0:%Y-%m-%d} — `{s['sid']}`", "",
             f"**When:** {d0:%Y-%m-%d %H:%M} → {d1:%H:%M} (UTC+7)  ",
             f"**Models:** {', '.join(r.get('modelsUsed', []))}  ",
             f"**Cost (ccusage):** ${r.get('totalCost', 0):.2f} — in {fmt_tokens(r.get('inputTokens', 0))} fresh + "
             f"{fmt_tokens(r.get('cacheCreationTokens', 0))} cache write, {fmt_tokens(r.get('cacheReadTokens', 0))} cache read, "
             f"out {fmt_tokens(r.get('outputTokens', 0))}  ",
             f"**Main-agent tool calls:** {sum(s['tools'].values())} ({', '.join(f'{k} {v}' for k, v in s['tools'].most_common())})  "]
    if s["compactions"]:
        lines.append(f"**Context compactions:** {s['compactions']}  ")
    lines += ["", "## What happened", "", SESSION_SUMMARY.get(s["sid"][:8], "(no summary written)"), ""]
    if s["commands"]:
        lines += ["## Slash commands", ""] + [f"- {local(ts):%H:%M} `/{c}`" for ts, c in s["commands"]] + [""]
    lines += ["## User prompts (verbatim)", ""]
    for ts, txt in s["prompts"]:
        lines += [f"### {local(ts):%H:%M}", "", "```text", txt, "```", ""]
    if s["agents"]:
        lines += ["## Subagents launched", "", "| Time | Model | Task | What it did |", "|---|---|---|---|"]
        for a in s["agents"]:
            sub = a["sub"]
            aid = sub["id"] if sub else None
            summ = AGENT_SUMMARY.get(aid or "", None)
            if summ is None:
                summ = (sub["final"][:300].replace("\n", " ") + "…") if sub and sub["final"] else "(no transcript found)"
            tl = ""
            if sub and sub["tools"]:
                tl = " Tools: " + ", ".join(f"{k} {v}" for k, v in sub["tools"].most_common(6)) + "."
            lines.append(f"| {local(a['ts']):%H:%M} | {a['model'] or 'inherit'} | {a['desc']} | {summ}{tl} |")
        lines += ["", "### Prompts given to subagents", ""]
        for a in s["agents"]:
            lines += ["<details>", f"<summary>{local(a['ts']):%H:%M} · {a['model'] or 'inherit'} · {a['desc']}</summary>", "",
                      "```text", a["prompt"].strip(), "```", "", "</details>", ""]
    with open(os.path.join(HERE, fname), "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
