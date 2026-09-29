"""Build index.html, the photo lookbook: every photo in images/classified.csv, grouped by the categories in
images/_namesort.py, with a lightbox (filmstrip, jump-to-number, swipe) and the preview PDFs.

Run after images/_namesort.py. No dependencies beyond the standard library.
Grouping is by filename keyword (same rule as images/index.html), not by looking at the image.
"""
import ast
import csv
import html
import os
import re
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
ROWS = list(csv.DictReader(open(os.path.join(HERE, "images", "classified.csv"), encoding="utf-8")))
DIRECT = sorted(f for f in os.listdir(os.path.join(HERE, "images", "direct")))

# Research summary per style (mirrors catalog.md). No longer rendered: the page is a pure gallery now.
# Kept as data. Each card: key, title, native names, verdict for the brief, fit (1-5), one-line why, spec to ask for,
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


def cats_from_namesort():
    """Gallery groups = CATS in images/_namesort.py, read without importing it (it rewrites files on import)."""
    tree = ast.parse(open(os.path.join(HERE, "images", "_namesort.py"), encoding="utf-8").read())
    for node in tree.body:
        if isinstance(node, ast.Assign) and any(getattr(t, "id", None) == "CATS" for t in node.targets):
            return [(c, label) for c, label, _ in ast.literal_eval(node.value)]
    raise SystemExit("CATS not found in images/_namesort.py")


CATS = cats_from_namesort()

SITE = {"hotpepper": "Hot Pepper Beauty", "ozmall": "OZmall", "lipps": "LIPPS", "mensnonno": "Men's Non-no",
        "pinterest": "Pinterest", "hiroginza": "HIRO GINZA", "mamedene": "Mamedene", "natebeauty": "Nate Beauty",
        "so360": "360 image search", "stylemap": "Stylemap", "ig": "Instagram", "lemon8": "Lemon8", "pin": "Pinterest",
        "rd": "Reddit", "yt": "YouTube", "i.redd.it": "Reddit", "preview.redd.it": "Reddit", "evanstyle.co.kr": "Evan Style",
        "cdn.shopify.com": "men's hair blog", "3second": "3Second", "idntimes": "IDN Times", "liputan6": "Liputan6",
        "miinhair": "Miin Hair", "smartlocalmy": "SmartLocal", "culturedgrooming": "Cultured Grooming",
        "dailyvanity": "Daily Vanity", "gowabi": "Gowabi", "hairtran": "Hairtran", "pantip": "Pantip",
        "wongnai": "Wongnai", "anhtoc": "Anh Toc", "cardina": "Cardina", "chiaki": "Chiaki", "laforce": "Laforce",
        "pkbarber": "PK Barber", "tiendich": "Tien Dich"}
REGION = {"jp": "JP", "jp-samples": "JP", "kr": "KR", "cn": "CN", "vn": "VN", "id": "ID", "th": "TH", "sg": "SG",
          "my": "MY", "ph": "PH"}


def source(r):
    """Human source label from the filename convention, e.g. 'Hot Pepper Beauty (JP)'."""
    f, d = r["file"], r["folder"]
    if d == "sea":
        reg, site = f.split("_")[:2]
        return f'{SITE.get(site, site.title())} ({REGION.get(reg, reg.upper())})'
    if d == "direct":
        dom = f.split("_")[0]
        return SITE.get(dom, dom) + (" (KR)" if "evanstyle" in dom else "")
    pre = re.split(r"[_\-.]", f)[0]
    name = SITE.get(pre, "salon site" if d.startswith("jp") else pre)
    return name + (f" ({REGION[d]})" if d in REGION else "")


def thumb(r):
    """Pre-made thumbnail if it exists (images/_thumbs/<folder>__<name>.jpg), else the original."""
    t = "images/_thumbs/" + r["folder"] + "__" + r["file"].rsplit(".", 1)[0] + ".jpg"
    return t if os.path.exists(os.path.join(HERE, t)) else "images/" + r["folder"] + "/" + r["file"]


# Friendly name + one-line description per _namesort category. Falls back to the first part of the
# _namesort label if a new category appears.
NAMES = {
    "A_center_part": ("Center part", "Curtain bangs and leaf cut, worn down"),
    "B_pushed_back": ("Pushed back", "Slicked back, or tied up in a man bun"),
    "C_wolf_layered": ("Wolf cut", "Mullet, shag and choppy layers"),
    "D_mash_long": ("Mushroom & bob", "Mash (mushroom) cut, bob, long one-length"),
    "E_hippie_grunge": ("Hippie", "Grunge, vintage, loose waves all over"),
    "F_spiral_tight": ("Spiral", "Tight spiral curls and twist perms"),
    "G_comma_short": ("Comma", "Short K-pop style, fringe curled like a comma"),
    "H_generic_perm": ("Other perms", "Style not named on the page they came from"),
}


def names(c, label):
    return NAMES.get(c, (label.split(" / ")[0].split(" (")[0], label))


def tile(r, g, i, name):
    s = source(r)
    return (f'<a class="t" href="images/{html.escape(r["folder"] + "/" + r["file"])}" target="_blank" data-g="{g}" data-i="{i}" '
            f'data-s="{html.escape(s)}" aria-label="{html.escape(name)}, photo {i + 1}, from {html.escape(s)}">'
            f'<img loading="lazy" decoding="async" src="{html.escape(thumb(r))}" alt=""></a>')


def head(name, sub, count):
    return f'<h2><span>{html.escape(name)}</span> <small>{html.escape(sub)} · {count}</small></h2>'


# ---- Style guide: the 10 CARDS styles, shown above the gallery. Facts come from CARDS and catalog.md (§2, §3, §10, §14).
BADGE = {"digital": "Digital perm", "either": "Digital or cold", "cold": "Cold perm"}
# Closest gallery group for each style (most of its filename matches land there; catalog.md §14 for the rest).
GUIDE_GROUP = {"allback": "B_pushed_back", "shadow": "H_generic_perm", "vintage": "D_mash_long", "leaf": "A_center_part",
               "digital": "H_generic_perm", "nuance": "H_generic_perm", "centerpart": "A_center_part",
               "wolf": "C_wolf_layered", "mash": "D_mash_long", "hippie": "E_hippie_grunge"}
# Groups no guide style covers: perm type from catalog.md §14.
GROUP_PERM = {"F_spiral_tight": "Usually a cold perm (too curly for digital rods).",
              "G_comma_short": "Usually a cold perm (too short for digital rods)."}
# Daily styling and upkeep, short, from catalog.md §2 master table (rows in brackets).
UPKEEP = {
    "allback": "Gel on damp roots, comb back, light spray: 1–3 minutes. A down perm on the sides looks good for 3–4 weeks.",
    "shadow": "Towel-dry, squeeze in cream. Trim every 8 weeks.",
    "vintage": "Dry and go: squeeze in balm or essence. Trim every 8 weeks.",
    "leaf": "A little balm, about 2 minutes. Trim every 8 weeks.",
    "digital": "Mist, pat dry, cream on the lengths, blow-dry on low, cool air to set: about 5 minutes. Trim every 8 weeks.",
    "nuance": "Light wax, or scatter with fingers and soft wax. Trim every 8 weeks.",
    "centerpart": "Oil or balm through damp hair, set the part with your fingers. Wind ruins it. Trim every 8 weeks.",
    "wolf": "Diffuser and volume powder, brush back. Trim every 8 weeks, or it turns into a mullet.",
    "mash": "Needs thinning or a down perm at the sides on thick hair.",
    "hippie": "Hairspray; a deep conditioning mask every week. Trim every 8 weeks.",
}
EXTRA_NAMES = {"allback": {"VN": "vuốt ngược"}}  # catalog.md §10 Vietnamese vocabulary
# Plain-English fixes and one-time glosses for the salon jargon in CARDS.
FIX = [(" (inference)", ""), ("Best partner", "Yes, the best match"), ("8-week trims", "Trim every 8 weeks"),
       ("Digital or setting perm", "Digital perm"), ("mid-lengths→ends", "middle to ends"), ("mid→ends", "middle to ends"),
       ("(JP stylists)", "(Japanese stylists)"), ("(stylist-verified)", "(confirmed by a stylist)"),
       ("JP perm tier", "JP standard perm price"), (" Needs a decent forehead.", " Shows your forehead."),
       ("Refuse two-block explicitly.", "Say no to a two-block."),
       ("No as a forward style · Yes with karma root lift", "No when worn forward; yes with a root perm at the part"),
       ("Low (full) · medium (semi)", "Not much (full hippie); partly (semi-hippie)")]
GLOSS = [("down perm", " (flattens puffy sides)"), ("two-block", " (shaved short sides)"), ("C-curl", " (tight inward curl)"),
         ("root perm", " (lifts the hair at the scalp)"), ("S-wave", " (loose S-shaped wave)")]


def plain(texts):
    seen, out = set(), []
    for t in texts:
        for a, b in FIX:
            t = t.replace(a, b)
        for w, g in GLOSS:
            m = re.search(re.escape(w), t, re.I)
            if w not in seen and m:
                t = t[:m.end()] + g + t[m.end():]
                seen.add(w)
        out.append(t)
    return out


def by_country(names, key):
    """Split 'a · b · c' into KR / JP / CN / VN by script. Latin names with no Vietnamese marks are skipped."""
    out = {}
    for n in [n.strip() for n in names.split("·")]:
        if re.search(r"[가-힣]", n):
            k = "KR"
        elif re.search(r"[぀-ヿ]", n):
            k = "JP"
        elif re.search(r"[一-鿿]", n):
            k = "CN"
        elif re.search(r"[ăâđêôơưạảấầẩẫậắằẳẵặẹẻẽếềểễệỉịọỏốồổỗộớờởỡợụủứừửữựỳỵỷỹ]", n.lower()):
            k = "VN"
        else:
            continue
        out.setdefault(k, []).append(n)
    for k, v in EXTRA_NAMES.get(key, {}).items():
        out.setdefault(k, []).append(v)
    return [(k, " · ".join(out[k])) for k in ("KR", "JP", "CN", "VN") if k in out]


def back_word(b):
    return "Yes" if re.match(r"^Yes|Best", b) else "No" if b.startswith("No") else "Partly"


GROUP_NAME = {c: names(c, label)[0] for c, label in CATS}
GROUP_COUNT = Counter(r["category"] for r in ROWS)
USED_THUMBS = set()
GUIDE_LINKS = {}  # gallery group -> guide styles that point to it


def guide_card(c):
    main = c["title"].split(" (")[0]
    matches = [r for r in ROWS if re.search(c["rx"], (r["folder"] + "/" + r["file"]).lower())]
    order = {"digital": 0, "either": 1, "cold": 2, "unknown": 3}
    ranked = sorted(matches, key=lambda r: order[r["verdict"]])
    hero = next((r for r in ranked if r["file"] not in USED_THUMBS), ranked[0])  # no repeated thumbs across cards
    USED_THUMBS.add(hero["file"])
    g = GUIDE_GROUP[c["key"]]
    GUIDE_LINKS.setdefault(g, []).append((c["key"], main, c["verdict"]))
    spec, cost, hold, back = plain([c["spec"], c["cost"], c["hold"], c["back"]])
    local = "".join(f'<dt>{k}</dt><dd lang="{ {"KR": "ko", "JP": "ja", "CN": "zh", "VN": "vi"}[k] }">{html.escape(v)}</dd>'
                    for k, v in by_country(c["names"], c["key"]))
    return f'''<article class="gcard" id="guide-{c["key"]}">
  <div class="gtop">
    <img class="gthumb" loading="lazy" decoding="async" src="{html.escape(thumb(hero))}" alt="">
    <div>
      <h3>{html.escape(main)}</h3>
      <span class="badge b-{c["verdict"]}">{BADGE[c["verdict"]]}</span>
    </div>
  </div>
  <dl class="local">{local}</dl>
  <details>
    <summary>Details</summary>
    <dl class="facts">
      <dt>What to ask</dt><dd>{html.escape(spec)}</dd>
      <dt>Cost</dt><dd>{html.escape(cost)}</dd>
      <dt>Lasts</dt><dd>{html.escape(hold)}</dd>
      <dt>Upkeep</dt><dd>{html.escape(UPKEEP[c["key"]])}</dd>
      <dt>Pushes back?</dt><dd>{html.escape(back if "·" in back else back_word(c["back"]))}</dd>
    </dl>
  </details>
  <a class="see" href="#{g}">See {GROUP_COUNT[g]} photos: {html.escape(GROUP_NAME[g])} →</a>
</article>'''


GUIDE_HTML = "\n".join(guide_card(c) for c in CARDS)


def guide_line(g):
    """Small line under a gallery group header, linking back to its style guide card(s)."""
    if g in GUIDE_LINKS:
        items = " · ".join(f'<a href="#guide-{k}">{html.escape(n)}</a> ({BADGE[v].lower()})' for k, n, v in GUIDE_LINKS[g])
        return f'<p class="gline">In the style guide: {items}</p>'
    if g in GROUP_PERM:
        return f'<p class="gline">{html.escape(GROUP_PERM[g])}</p>'
    return ""


SECTIONS, CHIPS, N_TILES = [], [], 0
for c, label in CATS:
    rs = [r for r in ROWS if r["category"] == c]
    if not rs:
        continue
    N_TILES += len(rs)
    name, sub = names(c, label)
    CHIPS.append(f'<a class="chip" href="#{c}" data-cat="{c}">{html.escape(name)} <span>{len(rs)}</span></a>')
    SECTIONS.append(f'''<section class="gsec" id="{c}" data-name="{html.escape(name)}">
  {head(name, sub, f"{len(rs)} photos")}{guide_line(c)}
  <div class="gg">{"".join(tile(r, c, i, name) for i, r in enumerate(rs))}</div>
</section>''')
assert N_TILES == len(ROWS), (N_TILES, len(ROWS))

PDFS = sorted(f for f in os.listdir(os.path.join(HERE, "images", "pdf")) if f.lower().endswith(".pdf"))
PDF_OVERRIDE = {
    "basic-of-basic-06-perm-layer-a": "Basic of Basic 06: Perm Layer A",
    "basic-of-basic-07-perm-layer-b": "Basic of Basic 07: Perm Layer B",
    "basic-of-basic-08-perm-graduation": "Basic of Basic 08: Perm Graduation",
    "mens-hair-7-problems-perm": "Men's Hair 7 Problems: Perm",
    "perm-book-damaged-history-hair": "Perm Book for Damaged Hair",
}
PDF_WORDS = {"mens": "Men's", "haircatalog": "Hair Catalog", "goald": "GOALD", "yog": "YOG", "dada": "DADA",
             "of": "of", "the": "the", "for": "for"}


def pdf_name(f):
    """'hairmode_jm19558_mens-perm-haircatalog-2021-2022.pdf' -> "Men's Perm Hair Catalog 2021–22"."""
    n, pre = f[:-4], ""
    if n.startswith("salon_frogstar_"):
        n, pre = n[len("salon_frogstar_"):], "Salon Frogstar "
    n = re.sub(r"^hairmode_jm\d+_", "", n)
    if n in PDF_OVERRIDE:
        return pre + PDF_OVERRIDE[n]
    n = re.sub(r"(20\d\d)-20(\d\d)(?!\d)", r"\1–\2", n)       # 2021-2022 -> 2021–22
    n = re.sub(r"(20\d\d)-(\d\d)(?!\d)", r"\1–\2", n)         # 2019-20   -> 2019–20
    n = re.sub(r"(?<![\d–])(\d\d)-(\d\d)(?!\d)", r"20\1–\2", n)  # 18-19     -> 2018–19
    words = [PDF_WORDS.get(w, w[:1].upper() + w[1:]) for w in n.split("-")]
    if words:
        words[0] = words[0][:1].upper() + words[0][1:]
    return pre + " ".join(words)


PDF_HTML = "".join(
    f'<a class="pdf" href="images/pdf/{html.escape(f)}" target="_blank"><img loading="lazy" decoding="async" src="images/_thumbs/pdf__{html.escape(f[:-4])}.jpg" alt=""><span>{html.escape(pdf_name(f))}</span></a>'
    for f in PDFS)
CHIPS.append(f'<a class="chip" href="#pdf" data-cat="pdf">Magazines <span>{len(PDFS)}</span></a>')


def count_sources():
    """Data rows across every table in sources.md = sites and queries tried."""
    lines = open(os.path.join(HERE, "sources.md"), encoding="utf-8").read().splitlines()
    rows = [l for l in lines if l.startswith("|")]
    seps = [l for l in rows if set(l.replace("|", "").strip()) <= set("-: ")]
    return len(rows) - 2 * len(seps)  # minus separator and header row of each table


def total_cost():
    m = re.search(r"\*\*Total\*\*.*\|\s*\*\*([\d.,]+)\*\*\s*\|", open(os.path.join(HERE, "README.md"), encoding="utf-8").read())
    return m.group(1) if m else None


N_SRC = count_sources()
COST = total_cost()
cost_txt = f"about ${float(COST.replace(',', '')):.0f}" if COST else "see prompt/README.md"
REPO = "https://github.com/VAD37/2026-09-07-hair-research"
GH_SVG = ('<svg viewBox="0 0 16 16" width="18" height="18" aria-hidden="true" focusable="false"><path fill="currentColor" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z"/></svg>')

CSS = """
:root{--bg:#faf8f4;--panel:#fff;--soft:#efeae2;--line:#e3ddd2;--fg:#1c1a17;--mut:#6d675e;--acc:#b0502a;--acc-fg:#fff;
  --serif:"Iowan Old Style","Palatino Linotype",Palatino,Georgia,"Noto Serif KR",serif;
  --sans:system-ui,-apple-system,"Segoe UI",Roboto,"Noto Sans JP","Noto Sans KR","Malgun Gothic",sans-serif}
:root[data-theme="dark"]{--bg:#141311;--panel:#1d1b18;--soft:#26231f;--line:#34302a;--fg:#ede8df;--mut:#a59e92;--acc:#e08a5f;--acc-fg:#1a1410}
@media (prefers-color-scheme: dark){:root:not([data-theme="light"]){--bg:#141311;--panel:#1d1b18;--soft:#26231f;--line:#34302a;--fg:#ede8df;--mut:#a59e92;--acc:#e08a5f;--acc-fg:#1a1410}}
*{box-sizing:border-box}
html{scroll-padding-top:120px}
body{margin:0;background:var(--bg);color:var(--fg);font:16px/1.5 var(--sans);-webkit-text-size-adjust:100%}
a{color:var(--acc)}
.wrap{max-width:1400px;margin:0 auto;padding:0 16px}
/* header */
.mast{padding-top:36px;padding-bottom:18px;display:grid;grid-template-columns:1fr auto;gap:0 16px;align-items:start}
.mast h1{margin:0;font:600 clamp(34px,5.4vw,62px)/1.04 var(--serif);letter-spacing:-.01em}
.mast .sub{grid-column:1;margin:12px 0 0;max-width:56ch;font-size:clamp(17px,1.9vw,20px);line-height:1.45;color:var(--mut)}
.stats{grid-column:1;margin:12px 0 0;font-size:15px;color:var(--mut)}
.stats b{color:var(--fg);font-weight:700}
.nw{white-space:nowrap}
.tools{grid-column:2;grid-row:1;display:flex;gap:6px}
.ib{cursor:pointer;display:inline-flex;align-items:center;justify-content:center;width:44px;height:44px;border-radius:999px;border:1px solid var(--line);background:var(--panel);color:var(--fg);font:inherit;font-size:16px;text-decoration:none}
.ib:hover{border-color:var(--acc);color:var(--acc)}
/* sticky style chips: they wrap on wider screens, scroll sideways on phones */
.gbar{position:sticky;top:0;z-index:5;background:color-mix(in srgb,var(--bg) 92%,transparent);backdrop-filter:blur(8px);-webkit-backdrop-filter:blur(8px);border-bottom:1px solid var(--line)}
.chips{display:flex;flex-wrap:wrap;gap:5px;padding-top:8px;padding-bottom:8px}
.chip{flex:none;display:inline-flex;align-items:center;gap:5px;min-height:38px;padding:0 11px;border-radius:999px;border:1px solid var(--line);background:var(--panel);color:var(--fg);text-decoration:none;font-size:14px;white-space:nowrap;cursor:pointer}
.chip span{color:var(--mut);font-size:12px;font-variant-numeric:tabular-nums}
.chip:hover{border-color:var(--acc)}
.chip.here{border-color:var(--acc);box-shadow:inset 0 0 0 1px var(--acc)}
.chip[aria-current="true"]{background:var(--fg);color:var(--bg);border-color:var(--fg);box-shadow:none}
.chip[aria-current="true"] span{color:inherit;opacity:.7}
/* style guide */
.hbtn{grid-column:1;margin:14px 0 0}
.btn{display:inline-flex;align-items:center;min-height:44px;padding:0 18px;border-radius:999px;background:var(--fg);color:var(--bg);text-decoration:none;font-weight:600;font-size:15px}
.btn:hover{background:var(--acc);color:var(--acc-fg)}
.guide-chip{font-weight:600;border-color:var(--acc);color:var(--acc)}
.guide{padding-top:26px;padding-bottom:10px}
.guide h2{margin:0 0 8px;font:600 clamp(24px,2.6vw,30px)/1.2 var(--serif)}
.legend{margin:0 0 8px;max-width:90ch;font-size:14px;line-height:1.7;color:var(--mut)}
.legend .badge{margin-right:2px}
.ggrid{display:grid;grid-template-columns:repeat(auto-fill,minmax(250px,1fr));gap:10px;align-items:start;margin-top:14px}
.gcard{background:var(--panel);border:1px solid var(--line);border-radius:12px;padding:12px 14px;display:flex;flex-direction:column;gap:8px;min-width:0}
.gtop{display:flex;gap:12px;align-items:center}
.gthumb{width:56px;height:56px;border-radius:8px;object-fit:cover;flex:none;background:var(--soft)}
.gcard h3{margin:0 0 4px;font:600 17px/1.25 var(--serif)}
.badge{display:inline-block;padding:2px 9px;border-radius:999px;font-size:12px;font-weight:600;line-height:1.5;white-space:nowrap}
.b-digital{background:#e3f0e8;color:#2f6f4f}.b-either{background:#f6ecd6;color:#8a5d0f}.b-cold{background:#f7e1dc;color:#9c3426}
:root[data-theme="dark"] .b-digital{background:#1f3328;color:#8fd0ab}:root[data-theme="dark"] .b-either{background:#352a15;color:#e3bd6c}:root[data-theme="dark"] .b-cold{background:#3a201b;color:#f0998a}
@media (prefers-color-scheme: dark){:root:not([data-theme="light"]) .b-digital{background:#1f3328;color:#8fd0ab}:root:not([data-theme="light"]) .b-either{background:#352a15;color:#e3bd6c}:root:not([data-theme="light"]) .b-cold{background:#3a201b;color:#f0998a}}
.local{margin:0;display:grid;grid-template-columns:auto 1fr;gap:2px 8px;font-size:13px}
.local dt{color:var(--mut);font-weight:600;font-size:11px;letter-spacing:.05em;padding-top:2px}
.local dd{margin:0;overflow-wrap:anywhere}
.gcard details{border-top:1px solid var(--line)}
.gcard summary{cursor:pointer;display:flex;align-items:center;min-height:44px;font-size:14px;font-weight:600;color:var(--acc);list-style:none}
.gcard summary::-webkit-details-marker{display:none}
.gcard summary::after{content:"+";margin-left:6px}
.gcard details[open] summary::after{content:"−"}
.facts{margin:0 0 6px;display:grid;grid-template-columns:auto 1fr;gap:6px 10px;font-size:14px;line-height:1.45}
.facts dt{color:var(--mut)}.facts dd{margin:0;min-width:0;overflow-wrap:anywhere}
.see{display:inline-flex;align-items:center;min-height:44px;font-size:14px;font-weight:600;text-decoration:none;margin-top:-8px}
.see:hover{text-decoration:underline}
.gline{margin:-8px 0 12px;font-size:14px;color:var(--mut)}
.gline a{display:inline-block;padding:4px 0}
/* gallery */
.gsec{padding:44px 0 6px;border-top:1px solid var(--line)}
#gallery>.gsec:first-child,.filtered .gsec.on{padding-top:22px;border-top:0}
.gsec h2{margin:0 0 14px;display:flex;flex-wrap:wrap;align-items:baseline;column-gap:12px;row-gap:2px;font:600 clamp(24px,2.6vw,30px)/1.2 var(--serif)}
.gsec h2 small{font:400 14px/1.4 var(--sans);color:var(--mut)}
.gg{display:grid;grid-template-columns:repeat(auto-fill,minmax(132px,1fr));gap:4px}
.t{display:block;aspect-ratio:3/4;overflow:hidden;border-radius:6px;background:var(--soft)}
.t img{width:100%;height:100%;object-fit:cover;display:block;transition:transform .25s}
.t:hover img{transform:scale(1.04)}
.t:focus-visible{outline:3px solid var(--acc);outline-offset:1px}
.pdfs{display:grid;grid-template-columns:repeat(auto-fill,minmax(150px,1fr));gap:14px 12px}
.pdf{display:flex;flex-direction:column;gap:6px;color:var(--fg);text-decoration:none;font-size:13px;line-height:1.3}
.pdf img{width:100%;aspect-ratio:3/4;object-fit:cover;border-radius:6px;background:var(--soft);border:1px solid var(--line)}
.pdf:hover span{color:var(--acc)}
.pdf span{overflow-wrap:anywhere}
.filtered .gsec{display:none}.filtered .gsec.on{display:block}
/* footer */
footer{margin-top:40px;padding:22px 0 32px;border-top:1px solid var(--line);color:var(--mut);font-size:14px;line-height:1.6}
footer p{margin:0 0 8px;max-width:72ch}
footer .links a{white-space:nowrap;display:inline-block;padding:2px 0}
/* lightbox: stage, caption with a jump-to counter, filmstrip */
#lb{position:fixed;inset:0;z-index:20;background:#0b0a09;color:#e8e4dd;display:none;flex-direction:column;outline:0}
#lb.on{display:flex}
#lb .stage{flex:1;min-height:0;position:relative;display:flex;align-items:center;justify-content:center;padding:56px 64px 8px;touch-action:pan-y}
#lb .stage img{max-width:100%;max-height:100%;object-fit:contain;border-radius:6px;transition:opacity .15s}
#lb .stage img.loading{opacity:.25}
#lb .nb{position:absolute;cursor:pointer;background:rgba(255,255,255,.14);color:#fff;border:0;border-radius:999px;width:44px;height:44px;font-size:22px;line-height:1}
#lb .nb:hover{background:rgba(255,255,255,.25)}
#lb .x{top:10px;right:10px}#lb .pv{left:10px;top:50%;transform:translateY(-50%)}#lb .nx{right:10px;top:50%;transform:translateY(-50%)}
#lb .cap{display:flex;gap:4px 14px;align-items:center;justify-content:center;flex-wrap:wrap;padding:6px 16px 0;font-size:14px;text-align:center}
#lb .nm{font-weight:700;color:#fff}
#lb .src{color:rgba(232,228,221,.65)}
#lb .src a{color:inherit;display:inline-block;padding:6px 2px}
#lb .src a:hover{color:#fff}
#lb .cnt{display:inline-flex;align-items:center;gap:4px;font-variant-numeric:tabular-nums;color:rgba(232,228,221,.8)}
#lb .cnt input{width:3.4em;min-height:36px;text-align:center;font:inherit;color:#fff;background:transparent;border:1px solid transparent;border-radius:6px}
#lb .cnt input:hover,#lb .cnt input:focus{border-color:rgba(255,255,255,.4);background:rgba(255,255,255,.08)}
#lb .strip{display:flex;gap:6px;overflow-x:auto;padding:10px 16px 14px;scrollbar-width:thin}
#lb .fs{flex:none;width:56px;height:56px;padding:0;cursor:pointer;border:2px solid transparent;border-radius:6px;overflow:hidden;background:#2a2723;opacity:.55}
#lb .fs:hover{opacity:.9}
#lb .fs.on{border-color:#fff;opacity:1}
#lb .fs img{width:100%;height:100%;object-fit:cover;display:block}
#lb button:focus-visible,#lb a:focus-visible,#lb input:focus-visible{outline:2px solid #fff;outline-offset:2px}
@media (max-width:760px){
  .mast{padding-top:24px}
  .gbar{background:var(--bg);backdrop-filter:none;-webkit-backdrop-filter:none}
  .chips{flex-wrap:nowrap;overflow-x:auto;scrollbar-width:none;-webkit-mask-image:linear-gradient(90deg,#000 88%,transparent);mask-image:linear-gradient(90deg,#000 88%,transparent);padding-right:28px}
  .chips::-webkit-scrollbar{display:none}
  .chip{min-height:44px}
  html{scroll-padding-top:70px}
  .gsec{padding-top:32px}
  .ggrid{display:flex;align-items:flex-start;gap:10px;overflow-x:auto;scroll-snap-type:x mandatory;scrollbar-width:none;margin-right:-16px;padding-right:28px;padding-bottom:4px;-webkit-mask-image:linear-gradient(90deg,#000 88%,transparent);mask-image:linear-gradient(90deg,#000 88%,transparent)}
  .ggrid::-webkit-scrollbar{display:none}
  .gcard{flex:0 0 80vw;max-width:340px;scroll-snap-align:start}
  .legend{font-size:13px;line-height:1.6}
  .gg{grid-template-columns:repeat(3,1fr);gap:3px}
  .t{border-radius:4px}
  .pdfs{grid-template-columns:repeat(2,1fr)}
  footer .links a{padding:10px 0}
  #lb .stage{padding:56px 8px 60px}#lb .pv,#lb .nx{top:auto;bottom:8px;transform:none}
  #lb .cnt input{min-height:44px}
  #lb .fs{width:48px;height:48px}
}
"""

JS = r"""
(function(){
  var main=document.getElementById('gallery'), chips=Array.prototype.slice.call(document.querySelectorAll('.chip[data-cat]'));
  var cats=chips.map(function(c){ return c.dataset.cat; });
  // style chips are plain #links: the hash picks the filter, so Back/Forward undo it
  function pickCat(cat){
    chips.forEach(function(c){ c.setAttribute('aria-current', c.dataset.cat===cat?'true':'false'); });
    if(cat==='all'){ main.classList.remove('filtered'); }
    else{ main.classList.add('filtered'); main.querySelectorAll('.gsec').forEach(function(s){ s.classList.toggle('on', s.id===cat); }); }
    var top=main.getBoundingClientRect().top+window.scrollY-2; if(cat!=='all' || window.scrollY>top) window.scrollTo(0, cat==='all'?top:Math.min(window.scrollY, top));
    var cur=chips[cats.indexOf(cat)]; if(cur) cur.parentNode.scrollTo({left:cur.offsetLeft-40,behavior:'smooth'});
  }
  function fromHash(){ var h=location.hash.slice(1); pickCat(cats.indexOf(h)>=0 && h!=='all' ? h : 'all'); }
  window.addEventListener('hashchange',fromHash);
  if(location.hash) fromHash();
  // "you are here" outline while scrolling the full gallery
  if('IntersectionObserver' in window){
    var io=new IntersectionObserver(function(es){
      es.forEach(function(e){ if(!e.isIntersecting || main.classList.contains('filtered')) return;
        chips.forEach(function(c){ c.classList.toggle('here', c.dataset.cat===e.target.id); }); });
    },{rootMargin:'-120px 0px -70% 0px'});
    main.querySelectorAll('.gsec').forEach(function(s){ io.observe(s); });
  }
  // lightbox over one gallery group; the filmstrip is built only when it opens
  var lb=document.getElementById('lb'), lbi=lb.querySelector('.stage img'), strip=lb.querySelector('.strip'),
      num=lb.querySelector('.cnt input'), tot=lb.querySelector('.tot'), nm=lb.querySelector('.nm'), src=lb.querySelector('.src'),
      set=[], name='', at=0, back=null;
  function isOpen(){ return lb.classList.contains('on'); }
  function show(jump){
    if(!isOpen() || !set.length) return;
    var a=set[at], full=a.getAttribute('href');
    lbi.classList.add('loading'); lbi.onload=function(){ lbi.classList.remove('loading'); };
    lbi.src=full; lbi.alt=name+', photo '+(at+1)+' of '+set.length;
    num.value=at+1; nm.textContent=name;
    src.textContent='From '; var l=document.createElement('a'); l.href=full; l.target='_blank'; l.textContent=a.dataset.s; l.title='Open the original file'; src.appendChild(l);
    var old=strip.querySelector('.fs.on'); if(old){ old.classList.remove('on'); old.removeAttribute('aria-current'); old.tabIndex=-1; }
    var b=strip.children[at]; if(!b) return;
    b.classList.add('on'); b.setAttribute('aria-current','true'); b.tabIndex=0;
    strip.scrollTo({left:b.offsetLeft-strip.clientWidth/2+b.offsetWidth/2,behavior:jump?'auto':'smooth'});
    [at-1,at+1].forEach(function(k){ var n=set[(k+set.length)%set.length]; if(n) (new Image()).src=n.getAttribute('href'); }); // preload neighbours
  }
  function go(k){ if(!isOpen()) return; at=Math.max(0,Math.min(set.length-1,k)); show(); }
  function step(d){ if(!isOpen()) return; at=(at+d+set.length)%set.length; show(); }
  function jumpTyped(){ var n=parseInt(num.value,10); if(n>=1 && n<=set.length){ go(n-1); } else { num.value=at+1; } }
  function openLb(a){
    var sec=a.closest('.gsec'); set=Array.prototype.slice.call(sec.querySelectorAll('.t')); name=sec.dataset.name;
    back=a; at=Math.max(0,set.indexOf(a)); strip.innerHTML='';
    set.forEach(function(t,k){
      var b=document.createElement('button'); b.type='button'; b.className='fs'; b.tabIndex=-1; b.title='Photo '+(k+1); b.setAttribute('aria-label','Photo '+(k+1));
      var im=document.createElement('img'); im.loading='lazy'; im.src=t.querySelector('img').getAttribute('src'); im.alt=''; b.appendChild(im);
      b.addEventListener('click',function(){ go(k); }); strip.appendChild(b);
    });
    tot.textContent=set.length; lb.classList.add('on'); document.body.style.overflow='hidden'; show(true); lb.focus();
  }
  function closeLb(){
    if(!isOpen()) return;
    num.blur(); lb.classList.remove('on');
    lbi.onload=null; lbi.removeAttribute('src'); lbi.classList.remove('loading');
    strip.innerHTML=''; set=[]; document.body.style.overflow=''; if(back) back.focus();
  }
  main.addEventListener('click',function(e){ var a=e.target.closest('.t'); if(!a) return; e.preventDefault(); openLb(a); });
  lb.querySelector('.x').addEventListener('click',closeLb);
  lb.querySelector('.pv').addEventListener('click',function(){ step(-1); });
  lb.querySelector('.nx').addEventListener('click',function(){ step(1); });
  lb.querySelector('.stage').addEventListener('click',function(e){ if(e.target===this) closeLb(); });
  num.addEventListener('keydown',function(e){
    if(e.key==='Enter'){ e.preventDefault(); jumpTyped(); var b=strip.querySelector('.fs.on'); if(b) b.focus(); }
  });
  num.addEventListener('change',function(){ if(isOpen()) jumpTyped(); });
  num.addEventListener('focus',function(){ num.select(); });
  strip.addEventListener('wheel',function(e){ if(Math.abs(e.deltaY)>Math.abs(e.deltaX)){ strip.scrollLeft+=e.deltaY; e.preventDefault(); } },{passive:false});
  document.addEventListener('keydown',function(e){
    if(!isOpen()) return;
    if(e.key==='Escape'){ closeLb(); return; }
    if(e.key==='Tab'){ // keep focus inside the viewer
      var f=Array.prototype.slice.call(lb.querySelectorAll('button:not([tabindex="-1"]),a[href],input')), i=f.indexOf(document.activeElement);
      e.preventDefault(); f[(i+(e.shiftKey?-1:1)+f.length)%f.length].focus(); return; }
    if(e.target===num) return;
    var k={ArrowLeft:-1,ArrowRight:1,PageUp:-10,PageDown:10}[e.key];
    if(k===1||k===-1){ step(k); e.preventDefault(); }
    else if(k){ go(at+k); e.preventDefault(); }
    else if(e.key==='Home'){ go(0); e.preventDefault(); }
    else if(e.key==='End'){ go(set.length-1); e.preventDefault(); }
    else return;
    var b=strip.querySelector('.fs.on'); if(b && strip.contains(document.activeElement)) b.focus();
  });
  var x0=null; // swipe on phones
  lb.querySelector('.stage').addEventListener('touchstart',function(e){ x0=e.touches[0].clientX; },{passive:true});
  lb.querySelector('.stage').addEventListener('touchend',function(e){ if(x0===null) return; var dx=e.changedTouches[0].clientX-x0; x0=null; if(Math.abs(dx)>40) step(dx<0?1:-1); });
  // theme
  var root=document.documentElement;
  try{ var th=localStorage.getItem('hair-theme'); if(th) root.setAttribute('data-theme',th); }catch(e){}
  document.getElementById('theme').addEventListener('click',function(){
    var cur=root.getAttribute('data-theme'); var dark=cur?cur==='dark':window.matchMedia('(prefers-color-scheme: dark)').matches;
    var nxt=dark?'light':'dark'; root.setAttribute('data-theme',nxt); try{ localStorage.setItem('hair-theme',nxt); }catch(e){} });
})();
"""

DESC = (f"{len(ROWS):,} men's perm photos on medium and long hair, collected by AI agents from Asian salon sites, "
        f"Pinterest, Instagram and Reddit, sorted into {len(SECTIONS)} styles.")

page = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Men's Perm Lookbook 2026</title>
<meta name="description" content="{html.escape(DESC)}">
<meta property="og:title" content="Men's Perm Lookbook 2026">
<meta property="og:description" content="{html.escape(DESC)}">
<meta property="og:type" content="website">
<style>{CSS}</style>
</head>
<body>
<header class="wrap mast">
  <h1>Men's Perm Lookbook 2026</h1>
  <div class="tools"><button class="ib" id="theme" title="Light / dark" aria-label="Toggle light or dark theme">◐</button><a class="ib" href="{REPO}" target="_blank" rel="noopener" aria-label="View source on GitHub" title="View source on GitHub">{GH_SVG}</a></div>
  <p class="sub">AI agents collected these perm photos from Asian salon sites, Pinterest, Instagram and Reddit. Tap any photo to flip through its group.</p>
  <p class="stats"><span class="nw"><b>{len(ROWS):,}</b> photos</span> · <span class="nw"><b>{len(SECTIONS)}</b> styles</span> · <span class="nw"><b>{len(PDFS)}</b> salon magazines</span> · <span class="nw"><b>{N_SRC}</b> sources</span></p>
  <p class="hbtn"><a class="btn" href="#guide">Style guide: what to ask, cost, digital or cold →</a></p>
</header>

<nav class="gbar" aria-label="Styles"><div class="wrap chips">
  <a class="chip guide-chip" href="#guide">Style guide</a><a class="chip" href="#all" data-cat="all" aria-current="true">All <span>{len(ROWS):,}</span></a>{"".join(CHIPS)}
</div></nav>

<section class="wrap guide" id="guide" aria-labelledby="guide-h">
  <h2 id="guide-h">Style guide</h2>
  <p class="legend"><span class="badge b-digital">Digital perm</span> heat perm: looser waves, lasts longer (3–4 months), better for pushing back. <span class="badge b-cold">Cold perm</span> chemical only: tighter curl, cheaper, drops out in 1–2 months. <span class="badge b-either">Digital or cold</span> works either way.</p>
  <p class="legend">After any perm: no washing for 2–3 days, sulfate-free shampoo, and plan to re-perm about every 3 months.</p>
  <div class="ggrid">
{GUIDE_HTML}
  </div>
</section>

<main class="wrap" id="gallery">
{chr(10).join(SECTIONS)}
<section class="gsec" id="pdf" data-name="Salon magazines">
  {head("Salon magazines", "Free preview pages from Japanese hair magazines, as PDFs", f"{len(PDFS)} files")}
  <div class="pdfs">{PDF_HTML}</div>
</section>
</main>

<footer><div class="wrap">
  <p>How this was made: over two days (7–8 Sept 2026), Claude Code agents searched {N_SRC} sources (salon sites, Instagram, Pinterest, Reddit) and saved what they found. Photos are sorted by the words in their file names, not by an AI looking at each one, so a few are in the wrong group. Total AI cost: {cost_txt}.</p>
  <p class="links"><a href="{REPO}/blob/main/catalog.md">Full research notes</a> · <a href="{REPO}/blob/main/sources.md">Every source tried</a> · <a href="images/index.html">Old library view</a> · <a href="{REPO}">Project on GitHub</a></p>
  <p>Photos and PDFs belong to their salons, publishers and posters. Personal reference only.</p>
</div></footer>

<div id="lb" role="dialog" aria-modal="true" aria-label="Photo viewer" tabindex="-1">
  <div class="stage"><img alt=""><button class="nb x" aria-label="Close (Esc)">×</button><button class="nb pv" aria-label="Previous photo">‹</button><button class="nb nx" aria-label="Next photo">›</button></div>
  <div class="cap"><span class="nm"></span><span class="cnt"><input type="text" inputmode="numeric" aria-label="Photo number: type a number and press Enter to jump"> / <span class="tot"></span></span><span class="src"></span></div>
  <div class="strip" role="group" aria-label="All photos in this group"></div>
</div>

<script>{JS}</script>
</body>
</html>
'''

with open(os.path.join(HERE, "index.html"), "w", encoding="utf-8") as fh:
    fh.write(page)
print(N_TILES, "photos rendered of", len(ROWS), "in classified.csv;", len(PDFS), "PDFs")
for c, label in CATS:
    print(f"  {names(c, label)[0]:16s} {sum(r['category'] == c for r in ROWS)}")
