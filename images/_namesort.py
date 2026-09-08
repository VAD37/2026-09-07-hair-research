"""Name-based sort of images/<folder>/* into category + digital/cold verdict. No vision.
Writes images/classified.csv and images/index.html (grouped by category, verdict badge + filter)."""
import os, re, csv, html
import pymupdf
ROOT = os.path.dirname(os.path.abspath(__file__))
FOLDERS = ['jp','kr','social','cn','sea','direct']

CATS = [
 ('A_center_part',   'Center part / curtain / leaf (worn down)',      r'centerpart|center-part|centrepart|curtain|가르마|중분|zhongfen|leaf|리프|middle-part|middlepart|jangbal-leaf|mai-bay|sidepart|rẽ|hub1|hub2|comma-hair'),
 ('B_pushed_back',   'Pushed back / all-back / man-bun',               r'manbun|allback|all-back|kakiage|slick|houshu|youtou|vuot-nguoc|pushed|올백|슬릭|backhair'),
 ('C_wolf_layered',  'Wolf / mullet / layered / shag / hush',          r'wolf|mullet|layer|shag|hush|울프|레이어드|샤기|허쉬|mulletcut|wolfcut|langwei|狼尾'),
 ('D_mash_long',     'Mash-long / bob / long one-length',              r'bob|ronge|mash|mush|pijian|changfa|zhongchangfa|jijian|long-medium|_long|jangbal-lookbook|toc-nam-dai|man-bob|manbob|중단발|장발'),
 ('E_hippie_grunge', 'Hippie / grunge / vintage / natural all-over wave', r'hippie|히피|grunge|그런지|vintage|빈티지|natural|내추럴|naturalpeom|messy|ruffled'),
 ('F_spiral_tight',  'Spiral / twist / tight curl',                    r'spiral|twist|con-sau|premlock|zhanan|xizhi|锡纸|ringlet|foil|스왈로|swallow|베이비|baby|dread|afro|screw'),
 ('G_comma_short',   'Comma / two-block / short-medium K-style',       r'comma|two-block|twoblock|투블럭|댄디|dandy|feijitou|undercut|fade|crop'),
 ('H_generic_perm',  'Generic perm / unknown name',                    r'.'),
]
# perm-type keywords → verdict (checked before category default)
VERD = [
 ('digital', r'digital|デジタル|디지털|setting|셋팅|shadowperm|shadow|c-curl|s-curl|magazineperm|dijital'),
 ('cold',    r'hippie|히피|grunge|그런지|vintage|빈티지|natural|내추럴|spiral|twist|con-sau|premlock|zhanan|xizhi|스왈로|베이비|baby|kongqitang|air-perm|wenlitang|texture|텍스쳐|uon-phong|phong-chan|volume|dadwolum|comma|two-block|투블럭|댄디|dandy|feijitou|fade|undercut|dread|screw|surf|서프|러프|rough'),
 ('either',  r'namimaki|wave|wavy|ウエーブ|웨이브|nuance|ニュアンス|feather|featherperm|han-quoc|korean|hanxi|hanshi|weijuan|xoan-nhe|ruffled|leaf|리프|layer|레이어드|wolf|울프|manbun|houshu|youtou|slick|allback|kakiage|centerpart|center-part|pijian|zhongchangfa|jangbal|perm|펌|tang|uon'),
]
CAT_DEFAULT = {'A_center_part':'either','B_pushed_back':'digital','C_wolf_layered':'either','D_mash_long':'digital',
               'E_hippie_grunge':'cold','F_spiral_tight':'cold','G_comma_short':'cold','H_generic_perm':'unknown'}
CUT_ONLY = r'컷|cut\b|-cut|cut-'

def classify(name):
    n = name.lower()
    cat = next(c for c,_,rx in CATS if re.search(rx, n))
    verdict = next((v for v,rx in VERD if re.search(rx, n)), None)
    if verdict is None: verdict = CAT_DEFAULT[cat]
    # cut-only tags (리프컷/울프컷/레이어드컷): perm unspecified → category default, but cut is digital-compatible base
    if re.search(CUT_ONLY, n) and not re.search(r'perm|펌', n):
        verdict = CAT_DEFAULT[cat] if CAT_DEFAULT[cat] != 'unknown' else 'either'
        basis = 'cut-name only'
    else:
        basis = 'perm keyword' if verdict in ('digital','cold') and re.search(VERD[0][1]+'|'+VERD[1][1], n) else 'category default'
    return cat, verdict, basis

rows = []
for d in FOLDERS:
    p = os.path.join(ROOT, d)
    if not os.path.isdir(p): continue
    for f in sorted(os.listdir(p)):
        if not f.lower().endswith(('.jpg','.jpeg','.png','.webp','.gif')): continue
        cat, v, basis = classify(f)
        rows.append({'folder':d,'file':f,'category':cat,'verdict':v,'basis':basis})

with open(os.path.join(ROOT,'classified.csv'),'w',newline='',encoding='utf-8') as fh:
    w = csv.DictWriter(fh, fieldnames=['folder','file','category','verdict','basis']); w.writeheader(); w.writerows(rows)

# ---- summary
from collections import Counter
print('rows', len(rows))
print('by category:', Counter(r['category'] for r in rows).most_common())
print('by verdict :', Counter(r['verdict'] for r in rows).most_common())
print('cat x verdict:')
cv = Counter((r['category'], r['verdict']) for r in rows)
for c,_,_ in CATS:
    print(' ', c, {v:cv[(c,v)] for v in ['digital','either','cold','unknown'] if cv[(c,v)]})

# ---- gallery
T = os.path.join(ROOT,'_thumbs')
BADGE = {'digital':'#2e8b57','either':'#b8860b','cold':'#b22222','unknown':'#555'}
def card(r):
    th = '_thumbs/'+r['folder']+'__'+r['file'].rsplit('.',1)[0]+'.jpg'
    return (f'<a class="c v-{r["verdict"]}" data-v="{r["verdict"]}" href="{html.escape(r["folder"]+"/"+r["file"])}" target="_blank" title="{html.escape(r["file"])}">'
            f'<img loading="lazy" src="{html.escape(th)}"><b style="background:{BADGE[r["verdict"]]}">{r["verdict"]}</b><span>{html.escape(r["folder"]+" · "+r["file"])}</span></a>')
sections = []
for c,label,_ in CATS:
    rs = [r for r in rows if r['category']==c]
    if not rs: continue
    vc = Counter(r['verdict'] for r in rs)
    sub = ' · '.join(f'{k} {vc[k]}' for k in ['digital','either','cold','unknown'] if vc[k])
    sections.append(f'<section id="{c}"><h2>{html.escape(label)} <small>{len(rs)} — {sub}</small></h2><div class="g">{"".join(card(r) for r in rs)}</div></section>')
# PDFs
pdfs = sorted(f for f in os.listdir(os.path.join(ROOT,'pdf')) if f.lower().endswith('.pdf'))
pc = ''.join(f'<a class="c" href="pdf/{html.escape(f)}" target="_blank"><img loading="lazy" src="_thumbs/pdf__{html.escape(f[:-4])}.jpg"><span>{html.escape(f)} · {pymupdf.open(os.path.join(ROOT,"pdf",f)).page_count} pp</span></a>' for f in pdfs)
sections.append(f'<section id="pdf"><h2>Preview PDFs <small>{len(pdfs)}</small></h2><div class="g">{pc}</div></section>')
nav = ' · '.join(f'<a href="#{c}">{c}</a>' for c,_,_ in CATS if any(r["category"]==c for r in rows)) + ' · <a href="#pdf">pdf</a>'
page = f'''<!doctype html><meta charset="utf-8"><title>hair-research library (name-sorted)</title>
<style>body{{font:14px system-ui;margin:16px;background:#111;color:#ddd}}h2{{margin:28px 0 8px}}h2 small{{color:#888;font-weight:normal;font-size:12px}}
nav{{position:sticky;top:0;background:#111;padding:8px 0;border-bottom:1px solid #333;z-index:2}}nav a{{color:#8cf}}nav button{{margin-left:4px;cursor:pointer}}
.g{{display:grid;grid-template-columns:repeat(auto-fill,minmax(150px,1fr));gap:6px}}.c{{display:block;position:relative;color:#aaa;text-decoration:none;font-size:10px;overflow:hidden}}
.c img{{width:100%;height:190px;object-fit:cover;background:#222;border-radius:4px}}.c b{{position:absolute;top:4px;left:4px;color:#fff;padding:1px 5px;border-radius:3px;font-size:10px}}
.c span{{display:block;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}}body.f-digital .c:not(.v-digital),body.f-cold .c:not(.v-cold),body.f-either .c:not(.v-either){{display:none}}</style>
<nav><b>hair-research library</b> — {nav} &nbsp; filter: <button onclick="document.body.className=''">all</button><button onclick="document.body.className='f-digital'">digital</button><button onclick="document.body.className='f-either'">either</button><button onclick="document.body.className='f-cold'">cold</button>
<br><small>Sorting is by FILENAME keywords only (no image inspection). Verdict: digital = digital perm reproduces it; either = both work; cold = needs cold/spiral/hippie wind or too short. See catalog.md §14.</small></nav>{''.join(sections)}'''
open(os.path.join(ROOT,'index.html'),'w',encoding='utf-8').write(page)
print('gallery written')
