"""Build index.html (the style-picker site) from images/classified.csv + hand-written cards below.

Run after images/_namesort.py. No dependencies beyond the standard library.
Photos on each card are matched by filename keyword (same rule as the gallery), not by looking at the image.
"""
import csv
import html
import os
import re
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
ROWS = list(csv.DictReader(open(os.path.join(HERE, "images", "classified.csv"), encoding="utf-8")))
DIRECT = sorted(f for f in os.listdir(os.path.join(HERE, "images", "direct")))

# Each card: key, title, native names, verdict for the brief, fit (1-5), one-line why, spec to ask for,
# slick-back answer, cost line, hold line, image regex (against "folder/file"), catalog row(s).
CARDS = [
    dict(key="allback", title="Pushed-back wave (kakiage / all-back)", names="올백펌 · 슬릭백 · かきあげ · オールバック · 后梳",
         verdict="digital", fit=5,
         why="The reason to choose digital at all: wave sits in the length, top lies back and stays. Root lift needs a separate root/iron perm or blow-dry.",
         spec="Digital or setting perm, large rods, mid-lengths→ends. Add root perm at the front if you want lift. Gel on damp roots, comb back.",
         back="Yes — this is the target", cost="KR ₩150–300k · JP ¥12–18k · + down perm ₩20–40k if sides still short", hold="3–4 mo (JP stylists) · 1.5 mo on thick hair (reddit)",
         rx=r"kakiage|allback|all-back|manbun|slick", rows="#9, #3"),
    dict(key="shadow", title="Shadow perm", names="쉐도우펌 · シャドウパーマ",
         verdict="digital", fit=5,
         why="Curl only on mid-lengths and ends, root left natural, so it combs back cleanly and frizzes less. Korean origin, now a LIPPS category in Japan.",
         spec="Say 'shadow perm, root natural, S-wave not C-curl, I will push it back'.",
         back="Yes", cost="KR ₩50–120k · JP perm tier", hold="2 mo KR · 3–4 mo if done digital",
         rx=r"shadowperm|shadow", rows="#2"),
    dict(key="vintage", title="Vintage perm (end-only S-curl)", names="빈티지펌 · 중단발",
         verdict="digital", fit=5,
         why="Closest single Korean term for the brief: chin→collarbone length, soft S on the ends, flat root, dry-and-go. Salon marketing name, not a booking-app tag.",
         spec="Ask for 빈티지펌 on 중단발; fringe to the eyes, sides clear the ear, nape grown.",
         back="Yes (root flat)", cost="KR ₩88k cold / ₩112k heat · premium ₩219k", hold="3 mo (stylist-verified)",
         rx=r"jangbal|장발|natural|내추럴|leafpeom|리프펌", rows="#1"),
    dict(key="leaf", title="Leaf cut + soft wave", names="리프컷 · 리프펌",
         verdict="either", fit=5,
         why="Softest Korean cut base for a light wave; long nape, flexible length, pushes back easily. KR salons usually do 리프펌 cold; ask digital if you want it to slick back.",
         spec="리프컷 base, then digital on ends. Refuse two-block explicitly.",
         back="Yes", cost="cut ₩15–30k + perm", hold="8-week trims",
         rx=r"리프|leaf", rows="#16"),
    dict(key="digital", title="Digital wave / body-wave", names="디지털펌 · デジタルパーマ · 韓国風デジタルパーマ · uốn kỹ thuật số",
         verdict="digital", fit=5,
         why="The technique itself: heated rods, shape-memory, shows its wave dry. Needs 12 cm+, priced at the medium/long tier. Korean-style variant adds a comb-through gloss finish.",
         spec="Large rods, loose S, ends only. Routine: mist, pat dry, cream mid→ends, blow-dry low, cool-air set.",
         back="Best partner (inference)", cost="KR ₩150–300k · JP ¥12–18k · TW NT$3,400 · US $150–450", hold="3–4 mo",
         rx=r"digitalperm|digital|setting|셋팅|dijital", rows="#3, #4"),
    dict(key="nuance", title="Nuance / feather / wave-wrap perm", names="ニュアンスパーマ · フェザーパーマ · 波巻きパーマ",
         verdict="either", fit=4,
         why="Japan's lightest register: loosest wind, least damage, 'natural movement'. Often done cold on men, so it drops in 1–2 months; do it digital for hold.",
         spec="ニュアンスパーマ or 波巻き on medium; ask for 弱め.",
         back="Partial", cost="JP ¥6–20k incl. cut", hold="1–2 mo cold · 3–4 mo digital",
         rx=r"nuance|feather|namimaki|annui|moist|surfcurl", rows="#5, #6"),
    dict(key="centerpart", title="Center part / curtain (worn down)", names="중간가르마 · 가르마펌 · センターパート · カルマパーマ · 中分",
         verdict="digital", fit=4,
         why="The 'down' half of the brief. Digital gives a clean glossy C-bend from the cheekbone, flat crown. Karma perm adds root lift at the part so it can also push back.",
         spec="Center part + digital on ends; optional root perm at the part (카르마펌). Needs a decent forehead.",
         back="No as a forward style · Yes with karma root lift", cost="JP ¥10–15k · KR ₩50–100k", hold="1–2 mo (root) · 3–4 mo (ends)",
         rx=r"centerpart|center-part|curtain|가르마|중분|zhongfen|middle", rows="#7, #14"),
    dict(key="wolf", title="Wolf / layered / hush + light perm", names="울프컷 · 레이어드컷 · 허쉬컷 · ウルフパーマ · マッシュウルフ",
         verdict="either", fit=4,
         why="Jaw front, shoulder back. Redditors: 'brushing it back has 100% helped'. Digital = tidy K-wolf; cold = shaggy volume. Trim every 8 weeks or it becomes a mullet.",
         spec="Wolf/layered base + light wave on the layers (波巻き / nuance), digital if you want it neat.",
         back="Yes", cost="JP cut+perm ¥11–14k", hold="2–3 mo",
         rx=r"wolf|울프|layer|레이어드|hush|허쉬|shag", rows="#15, #17, #18"),
    dict(key="mash", title="Mash-long / men's bob (one length)", names="マッシュロング · メンズボブ · 중단발 · 披肩",
         verdict="digital", fit=3,
         why="Uniform big wave from the ear down, the JP 'ミディアムパーマ' catalog look. Heavy curtain; needs side thinning or down perm below shoulder length on thick hair.",
         spec="One-length bob + digital from ear down; ask for thinning at the sides.",
         back="Partial", cost="JP perm tier", hold="3–4 mo",
         rx=r"bob|ronge|mash|mush|long-medium|_long", rows="#28 area, §14"),
    dict(key="hippie", title="Hippie / semi-hippie / grunge (reference: what digital cannot do)", names="히피펌 · 세미히피펌 · 그런지펌",
         verdict="cold", fit=2,
         why="Root-to-tip irregular S, messy, matte, full volume. Digital leaves the top 3–5 cm straight, so all-over crimp is impossible. Hybrid (cold root + digital ends) is the compromise.",
         spec="If you want this, it is a cold perm. Ask for 세미 (looser) to stay near the brief.",
         back="Low (full) · medium (semi)", cost="KR ₩88–112k · tourist ₩120–220k", hold="2–3 mo",
         rx=r"hippie|히피|grunge|그런지", rows="#11, #17"),
]

PICK_PER_CARD = 8
BADGE = {"digital": "Digital", "either": "Either", "cold": "Cold perm", "unknown": "?"}


def pick(rx, n=PICK_PER_CARD):
    """Rows whose folder/file matches rx; prefer digital, then either, then cold; spread across folders."""
    cand = [r for r in ROWS if re.search(rx, (r["folder"] + "/" + r["file"]).lower())]
    order = {"digital": 0, "either": 1, "cold": 2, "unknown": 3}
    cand.sort(key=lambda r: order[r["verdict"]])
    out, per = [], Counter()
    for r in cand:  # first pass: at most 3 per folder
        if per[r["folder"]] < 3:
            out.append(r)
            per[r["folder"]] += 1
        if len(out) >= n:
            break
    if len(out) < n:
        for r in cand:
            if r not in out:
                out.append(r)
            if len(out) >= n:
                break
    return out, len(cand)


def thumb(r):
    return "images/_thumbs/" + r["folder"] + "__" + r["file"].rsplit(".", 1)[0] + ".jpg"


def img(r):
    return (f'<a href="images/{html.escape(r["folder"] + "/" + r["file"])}" target="_blank" class="t v-{r["verdict"]}" '
            f'title="{html.escape(r["folder"] + " · " + r["file"])}"><img loading="lazy" src="{html.escape(thumb(r))}" alt=""><i>{r["verdict"]}</i></a>')


def card(c):
    rs, total = pick(c["rx"])
    stars = "★" * c["fit"] + "☆" * (5 - c["fit"])
    return f'''<article class="card" id="{c["key"]}" data-key="{c["key"]}">
  <header>
    <div>
      <h3>{html.escape(c["title"])}</h3>
      <p class="names">{html.escape(c["names"])}</p>
    </div>
    <button class="pick" data-key="{c["key"]}" aria-pressed="false" title="Add to my shortlist">☆ pick</button>
  </header>
  <p class="meta"><span class="badge b-{c["verdict"]}">{BADGE[c["verdict"]]}</span> <span class="fit" title="fit for the brief">{stars}</span> · slick-back: <b>{html.escape(c["back"])}</b> · catalog rows {html.escape(c["rows"])}</p>
  <p>{html.escape(c["why"])}</p>
  <dl>
    <dt>Ask for</dt><dd>{html.escape(c["spec"])}</dd>
    <dt>Cost</dt><dd>{html.escape(c["cost"])}</dd>
    <dt>Hold</dt><dd>{html.escape(c["hold"])}</dd>
  </dl>
  <div class="strip">{"".join(img(r) for r in rs)}</div>
  <p class="small">{len(rs)} of {total} name-matched photos · <a href="images/index.html">all in the gallery</a></p>
</article>'''


ig = [r for r in ROWS if r["file"].startswith("ig_jangbalperm")][:14]
reddit = [r for r in ROWS if r["folder"] == "direct" and ("redd.it" in r["file"] or "evanstyle" in r["file"])]
kr_leaf = [r for r in ROWS if r["folder"] == "kr" and "리프" in r["file"]][:10]

page = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Perm picker</title>
<meta name="description" content="Which perm and cut to ask for at the next salon visit: East Asian male, medium to shoulder length, digital perm, light wave, must also slick back.">
<style>
:root{{--bg:#0f1115;--panel:#171a21;--line:#2a2f3a;--fg:#e6e6e6;--mut:#9aa3b2;--acc:#8ccfff;--dig:#2e8b57;--eit:#b8860b;--col:#b22222;--pick:#ffd166}}
:root[data-theme="light"]{{--bg:#f6f7f9;--panel:#fff;--line:#dde1e7;--fg:#1a1d23;--mut:#5b6472;--acc:#0b63c7}}
*{{box-sizing:border-box}}
body{{margin:0;background:var(--bg);color:var(--fg);font:15px/1.5 system-ui,-apple-system,"Segoe UI",Roboto,"Noto Sans JP","Noto Sans KR",sans-serif}}
a{{color:var(--acc)}}
.wrap{{max-width:1180px;margin:0 auto;padding:0 16px}}
header.top{{padding:28px 0 12px;border-bottom:1px solid var(--line)}}
header.top h1{{margin:0 0 6px;font-size:26px}}
header.top p{{margin:4px 0;color:var(--mut)}}
nav.bar{{position:sticky;top:0;z-index:5;background:var(--bg);border-bottom:1px solid var(--line);padding:8px 0;display:flex;gap:12px;flex-wrap:wrap;align-items:center;font-size:14px}}
nav.bar button{{cursor:pointer;background:var(--panel);color:var(--fg);border:1px solid var(--line);border-radius:6px;padding:4px 10px}}
nav.bar button[aria-pressed="true"]{{border-color:var(--acc);color:var(--acc)}}
section{{padding:22px 0}}
h2{{font-size:20px;margin:0 0 10px}}
.facts{{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:10px}}
.facts div{{background:var(--panel);border:1px solid var(--line);border-radius:8px;padding:10px 12px;font-size:14px}}
.facts b{{display:block;margin-bottom:4px}}
.grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(340px,1fr));gap:14px}}
.card{{background:var(--panel);border:1px solid var(--line);border-radius:10px;padding:14px;display:flex;flex-direction:column;gap:8px}}
.card.picked{{border-color:var(--pick);box-shadow:0 0 0 1px var(--pick) inset}}
.card header{{display:flex;justify-content:space-between;gap:10px;align-items:flex-start}}
.card h3{{margin:0;font-size:17px}}
.names{{margin:2px 0 0;color:var(--mut);font-size:13px}}
.card p{{margin:0}}
.meta{{font-size:13px;color:var(--mut)}}
.badge{{display:inline-block;padding:1px 7px;border-radius:4px;color:#fff;font-size:12px;font-weight:600}}
.b-digital{{background:var(--dig)}}.b-either{{background:var(--eit)}}.b-cold{{background:var(--col)}}
.fit{{color:var(--pick);letter-spacing:1px}}
dl{{margin:0;display:grid;grid-template-columns:auto 1fr;gap:2px 10px;font-size:13px}}
dt{{color:var(--mut)}}dd{{margin:0}}
.pick{{cursor:pointer;white-space:nowrap;background:transparent;color:var(--fg);border:1px solid var(--line);border-radius:6px;padding:4px 10px;font-size:13px}}
.pick[aria-pressed="true"]{{background:var(--pick);color:#000;border-color:var(--pick)}}
.strip{{display:grid;grid-template-columns:repeat(4,1fr);gap:4px}}
.t{{position:relative;display:block;aspect-ratio:3/4;overflow:hidden;border-radius:4px;background:#222}}
.t img{{width:100%;height:100%;object-fit:cover;display:block}}
.t i{{position:absolute;left:3px;top:3px;font:600 10px/1 system-ui;font-style:normal;color:#fff;padding:2px 4px;border-radius:3px;background:#555}}
.t.v-digital i{{background:var(--dig)}}.t.v-either i{{background:var(--eit)}}.t.v-cold i{{background:var(--col)}}
.small{{font-size:12px;color:var(--mut)}}
.wide{{display:grid;grid-template-columns:repeat(auto-fill,minmax(120px,1fr));gap:6px}}
.wide .t{{aspect-ratio:3/4}}
table{{border-collapse:collapse;width:100%;font-size:14px}}
th,td{{text-align:left;padding:6px 8px;border-bottom:1px solid var(--line);vertical-align:top}}
th{{color:var(--mut);font-weight:600}}
.script{{background:var(--panel);border:1px solid var(--line);border-left:4px solid var(--acc);border-radius:8px;padding:12px 14px}}
.script ol{{margin:6px 0 0 18px;padding:0}}
#tray{{position:fixed;left:0;right:0;bottom:0;background:var(--panel);border-top:1px solid var(--line);padding:8px 16px;display:none;gap:10px;align-items:center;flex-wrap:wrap;z-index:6;font-size:14px}}
#tray.on{{display:flex}}
#tray button{{cursor:pointer;background:var(--pick);color:#000;border:0;border-radius:6px;padding:5px 10px;font-weight:600}}
#tray .clr{{background:transparent;color:var(--mut);border:1px solid var(--line)}}
footer{{padding:24px 0 80px;color:var(--mut);font-size:13px;border-top:1px solid var(--line)}}
@media (prefers-color-scheme: light){{:root:not([data-theme="dark"]){{--bg:#f6f7f9;--panel:#fff;--line:#dde1e7;--fg:#1a1d23;--mut:#5b6472;--acc:#0b63c7}}}}
@media (max-width:480px){{.strip{{grid-template-columns:repeat(4,1fr)}}.card header{{flex-direction:column}}}}
</style>
</head>
<body>
<div class="wrap">
<header class="top">
  <h1>Which perm do I ask for?</h1>
  <p><b>Brief:</b> East Asian male · oval face · thick straight hair · chin→shoulder length · light flowy wave · must also push/slick back · street and salon references, not editorial.</p>
  <p>Pick cards below, then copy the shortlist for the stylist. Photos come from the research library ({len(ROWS):,} images, 42 preview PDFs); badge = digital / either / cold by <em>filename keyword</em>, not by looking at the photo. Full findings: <a href="catalog.md">catalog.md</a> · every source tried: <a href="sources.md">sources.md</a> · <a href="README.md">README</a> · token cost: <a href="prompt/README.md">prompt/</a>.</p>
</header>

<nav class="bar">
  <a href="#cards">Styles</a> <a href="#real">Real people</a> <a href="#script">Salon script</a> <a href="#cost">Cost</a> <a href="images/index.html">Gallery ({len(ROWS):,})</a>
  <span style="flex:1"></span>
  <button id="f-all" aria-pressed="true">all</button><button id="f-digital">digital only</button><button id="f-back">slicks back</button>
  <button id="theme" title="toggle theme">◐</button>
</nav>

<section id="facts">
  <h2>Five facts that decide everything</h2>
  <div class="facts">
    <div><b>Digital perm needs 12 cm+.</b> Chin→shoulder is exactly where it becomes the right tool, but you pay the medium/long tier.</div>
    <div><b>Digital shows its wave dry, cold shows it wet.</b> Digital combs back cleanly; cold re-springs when it meets gel or water.</div>
    <div><b>Digital cannot be wound near the root.</b> Root lift for a pushed-back front is a separate root / cold / iron perm.</div>
    <div><b>Thick straight hair will not stay back on product alone.</b> Wave on top, and down perm on the sides while they are still short.</div>
    <div><b>Plan a re-perm every 3 months.</b> Reddit thick hair: 4 days–1.5 mo. JP stylists: 3–4 mo. Anything over 4 mo is marketing.</div>
  </div>
</section>

<section id="cards">
  <h2>Candidate styles</h2>
  <div class="grid">
{chr(10).join(card(c) for c in CARDS)}
  </div>
</section>

<section id="real">
  <h2>Real people, not catalog models</h2>
  <p class="small">Instagram #남자장발펌 salon posts naming the exact perm used, and the reddit before/afters the catalog cites. Click for the original.</p>
  <div class="wide">{"".join(img(r) for r in ig)}{"".join(img(r) for r in reddit)}</div>
  <h2 style="margin-top:18px">Korean leaf cut set (cleanest salon shots)</h2>
  <div class="wide">{"".join(img(r) for r in kr_leaf)}</div>
</section>

<section id="script">
  <h2>What to say at the salon</h2>
  <div class="script">
    <b>Synthesis from the catalog (§3), not a quote from any one stylist.</b>
    <ol>
      <li>Base cut: leaf cut or light layers (리프컷 / シースルーレイヤー). <b>No two-block</b>, say it out loud, barbers default to it.</li>
      <li>Perm: digital or setting perm on <b>large rods</b>, mid-lengths→ends only. Register: 빈티지펌 / 쉐도우펌 / ニュアンス. "Not too much volume, S-wave not C-curl, I will push it back."</li>
      <li>Want the pushed-back front to stand? Add a <b>root perm</b> (cold or iron) as a separate line item.</li>
      <li>Skip down perm unless the sides are still at chin length.</li>
      <li>Show the wave-strength scale in <a href="images/pdf/hairmode_jm25971_goald-tokyo-mens-hair-book.pdf">GOALD Tokyo Men's Hair Book (PDF)</a> and point at 10–30 %.</li>
      <li>After: no wash 48–72 h, no hats or rain in that window, sulfate-free wash, product on damp hair squeezed not combed, blow-dry toward where it should sit.</li>
    </ol>
  </div>
</section>

<section id="cost">
  <h2>Digital perm cost, medium/long tier (≈USD)</h2>
  <table>
    <tr><th>Region</th><th>One perm</th><th>Per year (2–3 perms + trims + products)</th></tr>
    <tr><td>Korea</td><td>$107–254</td><td>$340–680</td></tr>
    <tr><td>Japan</td><td>$56–147</td><td>$380–670</td></tr>
    <tr><td>Taiwan</td><td>$62–156</td><td>$420–680</td></tr>
    <tr><td>Vietnam (uốn nhẹ Hàn Quốc)</td><td>₫500–900k</td><td>rises with length, never tiered explicitly</td></tr>
    <tr><td>Singapore (by length)</td><td>S$240 / 270 / 300+</td><td>—</td></tr>
    <tr><td>US</td><td>$150–450</td><td>$400–900 (up to 1,550)</td></tr>
    <tr><td>Australia</td><td>$118–204</td><td>$720–1,140</td></tr>
    <tr><td>UK</td><td>$244–295</td><td>$830–1,340</td></tr>
  </table>
  <p class="small">Every headline price is a "from" for very short hair. Budget the top of the range. Sources per number in catalog.md §2.</p>
</section>

<footer>
  Research done with Claude Code: subagents drove a logged-in Chrome session to get past login walls, IP blocks and Cloudflare checks; the main agent only wrote reports. Photos and PDFs belong to their original salons, publishers and posters; they are collected here for personal reference only. See <a href="README.md">README</a> for provenance, cost and how this was built.
</footer>
</div>

<div id="tray"><b>Shortlist:</b> <span id="tray-list"></span> <button id="copy">copy for stylist</button> <button class="clr" id="clear">clear</button></div>

<script>
(function(){{
  var KEY='hair-picks', picks=[];
  try{{ picks=JSON.parse(localStorage.getItem(KEY)||'[]'); }}catch(e){{ picks=[]; }}
  var titles={{}};
  document.querySelectorAll('.card').forEach(function(c){{ titles[c.dataset.key]=c.querySelector('h3').textContent; }});
  function save(){{ try{{ localStorage.setItem(KEY, JSON.stringify(picks)); }}catch(e){{}} }}
  function render(){{
    document.querySelectorAll('.card').forEach(function(c){{
      var on=picks.indexOf(c.dataset.key)>=0; c.classList.toggle('picked',on);
      var b=c.querySelector('.pick'); b.setAttribute('aria-pressed',on?'true':'false'); b.textContent=on?'★ picked':'☆ pick';
    }});
    var t=document.getElementById('tray'); t.classList.toggle('on',picks.length>0);
    document.getElementById('tray-list').textContent=picks.map(function(k){{return titles[k];}}).join(' · ');
  }}
  document.querySelectorAll('.pick').forEach(function(b){{ b.addEventListener('click',function(){{
    var k=b.dataset.key, i=picks.indexOf(k); if(i>=0) picks.splice(i,1); else picks.push(k); save(); render(); }}); }});
  document.getElementById('clear').addEventListener('click',function(){{ picks=[]; save(); render(); }});
  document.getElementById('copy').addEventListener('click',function(){{
    var txt='Hair brief: East Asian male, oval face, thick straight hair, chin-to-shoulder length. Light flowy S-wave, must also push back.\\n'+
      'Base: leaf cut / light layers, NO two-block.\\nPerm: digital or setting perm, large rods, mid-lengths to ends only, root natural. Optional separate root perm at the front.\\n'+
      'Styles I like: '+picks.map(function(k){{return titles[k];}}).join('; ')+'\\nWave strength: 10-30% on the GOALD scale.';
    if(navigator.clipboard) navigator.clipboard.writeText(txt).then(function(){{ document.getElementById('copy').textContent='copied'; setTimeout(function(){{document.getElementById('copy').textContent='copy for stylist';}},1500); }});
    else window.prompt('Copy:',txt);
  }});
  // filters
  var fs={{'f-all':function(c){{return true;}}, 'f-digital':function(c){{return c.querySelector('.badge').classList.contains('b-digital');}},
           'f-back':function(c){{return /^Yes|Best/.test(c.querySelector('.meta b').textContent);}}}};
  Object.keys(fs).forEach(function(id){{ document.getElementById(id).addEventListener('click',function(){{
    Object.keys(fs).forEach(function(j){{ document.getElementById(j).setAttribute('aria-pressed', j===id?'true':'false'); }});
    document.querySelectorAll('.card').forEach(function(c){{ c.style.display=fs[id](c)?'':'none'; }}); }}); }});
  // theme
  var root=document.documentElement;
  try{{ var th=localStorage.getItem('hair-theme'); if(th) root.setAttribute('data-theme',th); }}catch(e){{}}
  document.getElementById('theme').addEventListener('click',function(){{
    var cur=root.getAttribute('data-theme'); var dark=cur?cur==='dark':!window.matchMedia('(prefers-color-scheme: light)').matches;
    var nxt=dark?'light':'dark'; root.setAttribute('data-theme',nxt); try{{ localStorage.setItem('hair-theme',nxt); }}catch(e){{}} }});
  render();
}})();
</script>
</body>
</html>
'''

with open(os.path.join(HERE, "index.html"), "w", encoding="utf-8") as fh:
    fh.write(page)
for c in CARDS:
    rs, total = pick(c["rx"])
    print(f'{c["key"]:12s} {len(rs)}/{total}  ' + ", ".join(sorted(set(r["folder"] for r in rs))))
print("ig", len(ig), "reddit", len(reddit), "kr_leaf", len(kr_leaf))
