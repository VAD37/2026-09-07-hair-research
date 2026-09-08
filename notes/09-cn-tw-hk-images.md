# 09 — Chinese-language (CN / TW / HK) men's medium-long perm: images + catalog/book previews

Agent pass: 2026-09-08. Goal: fill the Chinese-language image gap left by the prior pass (which
only got TW price menus + 2 portal articles, near-zero images).

**Result: 168 images saved to `images/cn/` (20 MB).** 150 from 360 image search (`image.so.com`)
across 14 CN/TW/HK queries, 18 from StyleMap TW salon 作品 (1500×1500 originals).
Every file was eyeballed on a contact sheet before it was kept; women, children, short fades,
western barber-fade stock and duplicate ad banners were dropped.

---

## 0. The one technique that unlocked this (reuse it)

Baidu image search is dead for us: `image.baidu.com` **302-redirects to `www.baidu.com`** in the
user's Chrome, and its `acjson` API is CORS-blocked from any other origin.

**360 / Qihoo image search works and is the best CN image route:**

```
https://image.so.com/j?q=<urlencoded>&src=srp&sn=<offset>&pn=60
```

- Navigating Chrome to that URL renders raw JSON → `get_page_text` / `javascript_tool` reads it.
- Once on the `image.so.com` origin, `fetch()` to the same endpoint is **same-origin**, so a
  single `javascript_tool` call can sweep a dozen queries and stash results on `window`.
- Fields: `title`, `thumb` (360's own CDN cache — this is the file to download), `img`
  (original source URL, often hotlink-dead), `link` (source page), `width`/`height`, `dspurl`.
- Download `https://p2.ssl.qhimgs1.com/<imgkey>.jpg` with `Referer: https://image.so.com/`.
  The bare path is the **max cached size**; `/sdr/_240_/…` is a small variant. Cache tops out at
  ~400 px for old portal images but passes through 1080–3168 px for newer Douyin/Xiaohongshu
  sources. 103 of the 150 kept files are ≥400×400; the largest is 3168×1980.
- `javascript_tool` truncates output at **~1000 chars**, so export keys in slices of ~20–25.

**Visual vetting without burning context:** render all candidate thumbs into the page as a
112×142 grid with yellow index labels, then screenshot + scroll. ~96 images per screenshot,
7 screenshots covered 687 candidates. For local files, `python -m http.server` on a port and
navigate to `http://127.0.0.1:<port>/sheet.html` — **`file://` URLs are rejected** by the Chrome
MCP `navigate` tool (it prefixes `https://`).

---

## 1. Vocabulary learned this pass (CN / TW / HK are NOT the same words)

| Concept | 大陸 (CN) | 台灣 (TW) | 香港 (HK, Cantonese) |
|---|---|---|---|
| perm (verb/noun) | 烫发 | 燙髮 | **電髮** |
| texture perm | 纹理烫 | 紋理燙 | 紋理燙 / 法式紋理燙 |
| Korean-style perm | 韩式烫 / 韩系烫发 | 韓系燙髮 / 韓系捲度 | 韓式電髮 |
| digital / hot perm | 数码烫 / 热塑烫 | 熱塑燙 | 造型燙 |
| foil perm (tight, avoid) | 锡纸烫 | 錫紙燙 / **渣男燙** | 錫紙燙 / 港式錫紙燙 |
| down perm (flatten sides) | 下压烫 | 壓貼燙 | 壓貼燙 |
| air/volume perm | 空气烫 | 氣墊燙 | 氣墊燙 |
| micro-part fringe cut | 微分碎盖 | 微分碎蓋 | 微分碎蓋 |
| slick back / all back | 大背头 / 后梳 / 油头 | 後梳 / 背頭 | 背頭 |
| shoulder length | 及肩 / 齐肩 / 披肩 | 及肩 | 及肩 |
| medium-long | 中长发 | 中長髮 | 中長髮 |

New named styles found this pass:

- **渣男燙 (zhānán tàng, "scumbag perm")** — TW/CN slang for a men's 錫紙燙 variant. StyleMap's
  own definition: *"渣男燙是錫紙燙的一種… 因為抖音的一段影片「渣男錫紙燙，渣女大波浪，綠茶公主切」而爆紅"*.
  Tight foil-rod curl. **Too curly for the brief** — logged, only 2 images kept as reference.
- **鋼夾燙 (steel-clip perm)**, **摩根燙 (Morgan perm)**, **氣墊燙 (air-cushion perm)** — HK men's
  perm menu categories, see §4.
- **紳士波紋卷 (gentleman water-ripple curl)** — TW tag, loose S-wave; closest TW term to what the
  user wants at medium length.
- **韓系捲度** — TW tag, but in practice its gallery is ~80% women.

---

## 2. Images saved — grouped by silhouette

Filename convention: `<source>_<query-gloss>_<grid-index>_<hash>.<ext>`.
The grid-index is the position in this pass's contact sheet, kept so a future agent can
re-derive provenance. `so360_*` = harvested via 360 image search from the query named in the
filename; `stylemap_*` = TW salon 作品 from `style-map.com` tag galleries.

### A. Shoulder-length & past-shoulder, worn down, loose wave / big curl
The core of what the user asked for. Strongest group.

| Group | Query it came from | n | Notes |
|---|---|---|---|
| `so360_pijian-changfa-tang_*` | 男生披肩长发发型烫 (shoulder-draped long hair, permed) | 32 | Best group. Shoulder-to-past-shoulder, loose S-wave and big curl, mostly street/salon shots. Sources skew 大眾點評 (m.dianping.com) salon 作品 and Douyin — i.e. real clients, not editorials. Indices 362–380, 417–444. |
| `so360_changfa-wenlitang_*` | 男生长发纹理烫 (long hair texture perm) | 25 | Chin-to-shoulder textured perm. Mixed vintage: some 2015-era 发型站 stock (faxingsj.com, meifazhan.com), some current. |
| `so360_zhongchangfa-hanxi-tang_*` | 男生中长发韩系烫发 (Korean-style medium-long perm) | 24 | Chin-to-shoulder Korean centre-part + soft wave. Several 1080–2730 px. |

### B. Chin-length / jaw-length, permed, centre or curtain part
| Group | Query | n | Notes |
|---|---|---|---|
| `so360_zhongchangfa-tangfa_*` | 男生中长发烫发 | 26 | The generic query. Ear-to-chin permed, plus a few longer. Some 2010s-era portal stock (wenwen.soso.com, yidianzixun) — dated styling but the cut/wave reads fine. |
| `so360_zhongchangfa-weijuan_*` | 男士中长发微卷发型 (light wave) | 6 | Light wave, exactly the "微卷 not 羊毛卷" register the user asked for. |
| `so360_zhongchangfa-kongqitang_*` | 男生中长发空气烫 (air perm) | 7 | Airy root-volume perm at medium length. |
| `so360_jijian-tangfa-hanshi_*` | 男士及肩发烫发韩式 | 3 | Thin group — this query mostly returned women. |

### C. Slick-back / pushed-back compatible at length
| Group | Query | n | Notes |
|---|---|---|---|
| `so360_changfa-houshu-youtou_*` | 男生长发后梳油头 | 19 | **Mixed quality — read the caveat.** The query pulled a large block of western barber fades and pompadours, which I dropped. What survived is the good part: long Asian men's hair pushed straight back, half-up man-bun, low ponytail, and wet-look all-back at shoulder length. Includes the largest files in the set (2160×3840, 2048×3071). |
| `so360_tw-zhongchangfa-houshu_*` | 男生中長髮後梳 (TW spelling) | 4 | TW-sourced, same silhouette. |

### D. Taiwan salon 作品 (StyleMap) — real stylist work, 1500×1500
These are the ones with the printed-lookbook feel the user likes (each has a stylist + salon
behind it on style-map.com).

| File | Tag gallery | Read |
|---|---|---|
| `stylemap_nanshi-faxing_753339 / 754048 / 754567 / 755974 / 756613 / 756872 / 756973` | #男士髮型 → `/style/7984` | 7 files. Ear-to-chin, soft wave, natural fringe. The most "medium" of the TW set. |
| `stylemap_nansheng-hanxi-tangfa_742739 / 745591 / 752606 / 754769` | #男生韓系燙髮 → `/style/8991` | 4 files. Korean perm, chin-length, some curly. |
| `stylemap_nansheng-hanxi-wenlitang_744550 / 753613` | #男生韓系紋理燙 → `/style/10694` | 2 files. |
| `stylemap_hanxi-juandu_746512` | #韓系捲度 → `/style/4764` | 1 file (the only man in a 12-image gallery). |
| `stylemap_nanshi-feijitou_751464 / 756743` | #男士飛機頭 → `/style/4655` | 2 files, longer-top pomp — slick-back adjacent. |
| `stylemap_zhanan-tang_725241 / 737191` | #渣男燙 → `/style/11264` | 2 files, kept as **reference for what to avoid** (tight foil curl). |

CDN pattern for future StyleMap pulls: `https://cdn.style-map.com/post/photo/large/<id>.jpg`
(1500×1500; `/medium/` = 512, `/original/` = 404). Referer `https://style-map.com/`.
The image ids are embedded in the SSR HTML of each `/style/<id>` page — regex
`post/photo/medium/(\d+)\.jpg` after `fetch('/style/'+id)` from the style-map origin.

### E. Explicitly noted but NOT collected in quantity
- **锡纸烫 / 渣男燙 / 羊毛卷** — too curly for the brief. 2 reference files only.
- Western barber fades / pompadours — the 后梳油头 and 大背头 queries are heavily polluted with
  these; ~60 dropped at vetting.
- Women's 齐肩烫发 — the query 男士齐肩烫发 returns ~90% women. Do not re-run it.

---

## 3. What the CN/TW image landscape actually looks like (findings)

1. **Mainland men's medium-long permed hair is a real, current category**, but it lives on
   Douyin, Xiaohongshu and 大眾點評 salon 作品 — all three are login-walled on the web. 360 image
   search is the back door: it indexes and caches their images, and ~25 of the 150 harvested
   files trace back to `douyin.com` / `xiaohongshu.com` / `m.dianping.com` source pages.
2. **The old-school CN hairstyle catalog sites are alive but stale.** `faxingsj.com` has a real
   `男生长发` category (`/nanshengfaxing/nanshengchangfa/`) but its newest post is 2020-07 and the
   images are 300×210 / 500×350 thumbnails. Same family: `faxingw.cn`, `meifazhan.com`,
   `haofaxing.com`, `facang.com`, `hair.2liang.net`, `jj20.com`, `beauty.yxlady.com`,
   `3g.xiziwang.net`. Good "catalog page" *feel*, poor resolution, dated styling.
   `faxingw.cn/nanshengfaxing/` is a 404 — the live path is under `faxingsj.com`.
3. **Taiwan has almost no men's medium-long category.** StyleMap's men's taxonomy is
   飛機頭 / Undercut / 韓系捲度 / 男生韓系紋理燙 / 渣男燙 / 男生個性剪 / 男生韓系燙髮 / 紳士波紋卷 /
   栗子頭 / 男士燙髮 / 韓系歐巴髮型 / 男士逗號瀏海 / 嬉皮卷 / 型男必備. Its length categories are
   #男生短髮 only — there is **no #男生中長髮 or #男生長髮 tag at all**, while women get 女生長髮 and
   女生中長髮. TW men's salon work is overwhelmingly short.
4. **CN 发型书 (printed salon lookbooks) circulate as WeChat/Sohu photo posts**, e.g.
   sohu.com/a/345205203_643953 「金秋"潮流男发"发型书（剪烫染）」 — 15 pages at 1080×1416, each page a
   3×3 grid of styles. I downloaded and inspected these: **100% short cuts, fades and hair
   tattoos.** Not collected. Worth knowing the format exists; not worth mining for this brief.

---

## 4. Hong Kong

HK men's perm has its own specialist scene and its own vocabulary (電髮, not 燙髮).

**Canvas Texture / menpermhk.com** — 上環荷李活道252號, self-described as the only men's-perm-only
shop in 中上環, ~60 men's perms/week. Its `/services` index is effectively a HK men's perm
taxonomy, one page each:

| # | Style | URL slug |
|---|---|---|
| 01 | 韓式電髮 / 韓式紋理燙 (HK$880, 2.5 hr) | `/services/korean-texture-perm` |
| 02 | 鋼夾燙 | `/services/steel-clip-perm` |
| 03 | 摩根燙 | `/services/morgan-perm` |
| 04 | 法式紋理燙 | `/services/french-crop-perm` |
| 05 | 氣墊燙 | `/services/air-cushion-perm` |
| 06 | 微分碎蓋 | `/services/micro-part-perm` |
| 07 | 錫紙燙 | `/services/foil-perm` |

Useful line from the 韓式電髮 page on how the rods are set: 三角分區法 (triangular sectioning),
targeting 前額略向斜下、頂部蓬起、後頸自然落下 — forehead falling slightly diagonally, crown lifted,
nape falling naturally. Companion guide: `canvasblend.com` 「香港男士電髮2026 完整指南｜韓式 vs
法式紋理燙比較」 (dated 2026-04-22).

Other HK men's-perm salons surfaced (all IG-primary, so galleries are behind the IG wall):
Hankuk Hair 韓國髮型屋 (銅鑼灣, Korean stylists — @hankuk_hair), LaB Salon & Beauty (銅鑼灣, 4000 ft²),
E-KO 男士電髮專科 (尖沙咀, @eko_hair_stylist, Threads), Hair Alan (@hair.alan), Misso Hair (銅鑼灣),
Ming 微分碎蓋/假髮訂製. HK pricing signal seen in ads: men's perm HK$980 (list HK$1,580),
**Down Perm +HK$300**. Aggregator: hellotoby.com (1,800+ HK salons, 電髮 category).

HK is **short-hair dominated** too — every one of these shops markets 微分碎蓋 / 紋理燙 on short
hair. No HK medium-long men's gallery was found.

---

## 5. Books / printed catalog previews

| Item | Where | Preview? |
|---|---|---|
| 《時尚男士髮型》廖慶湰, 貝爾莎莉美容美髮出版社, 2017-09-01, NT$500 (9折 450) | books.com.tw/products/0010763436 | **絕版 (out of print)**, no 試閱 on the product page. The only TW-published men's-hairstyle photo book that exists on 博客來. |
| 博客來 search `男士髮型` | search.books.com.tw | **2 results total**, one of which is a comb. That is the whole TW market. |
| 博客來 search `髮型設計` | search.books.com.tw | ~20 results, all technique textbooks (剪吹, 編梳, 新娘, 小孩, 漫畫角色) or JP MOOK imports. Several carry 試閱 flags but none is a men's lookbook. |
| CN 男士发型书 / 发型图册 | JD.com (`jd.com/sptopic/17138159f78e1c82d4f8.html`, `jd.com/jiage/1713f3d9818a6fcdb389.html`), 苏宁 (`product.suning.com/0071520036/12352413571.html`) | Listing pages only; titles like 《型男新境界(500款发型)》, 《时尚发型258式图册》, 《2021新款发型书…卷发烫发》. These are salon counter-books sold by the piece on 阿里巴巴/1688 — **no online preview, no ISBN-grade metadata, and the sample images shown are short-cut heavy.** |
| 豆瓣 | — | Not reached; no 豆瓣 entries surfaced in search for these titles (they are trade goods, not catalogued books). |
| 当当 | — | Not reached this pass. |
| HK 商務印書館 | — | Not reached this pass. |

**Verdict: there is no downloadable Chinese-language men's medium-long perm lookbook preview.**
Nothing was saved to `images/pdf/`. The Chinese-language equivalent of the JP 立ち読み PDF simply
does not exist in this niche — CN 发型书 are physical salon props sold on 1688, TW publishes only
technique textbooks, and the one TW men's photo book is out of print.

---

## 6. Query log

Legend: ✓ useful · ◐ partial · ✗ dead/blocked. Tool in brackets.

### Image search
| Query / URL | Result |
|---|---|
| `image.baidu.com/search/index?...` (Chrome) | ✗ **302 → www.baidu.com**, never loads the image SERP |
| `image.baidu.com/search/acjson` via fetch from baidu.com (Chrome JS) | ✗ CORS `Failed to fetch` |
| `www.baidu.com` (Chrome) | ✓ loads fine — it is only the image vertical that redirects |
| `image.so.com/j?q=…` (Chrome navigate → JSON) | ✓ **the winning route**, see §0 |
| so.com 男生中长发烫发 (76 hits) | ✓ 26 kept |
| so.com 男士齐肩烫发 (102) | ✗ ~90% women — do not repeat |
| so.com 男生长发纹理烫 (124) | ✓ 25 kept |
| so.com 男生中长发大背头 (94) | ✗ western barber fades; 0 kept |
| so.com 男士中长发微卷发型 (96) | ✓ 6 kept |
| so.com 男生披肩长发发型烫 (152) | ✓ **best single query**, 32 kept |
| so.com 男士及肩发烫发韩式 (43) | ◐ 3 kept |
| so.com 男生中长发韩系烫发 (80) | ✓ 24 kept |
| so.com 男生长发后梳油头 (82) | ◐ 19 kept after dropping western fades |
| so.com 男生中长发空气烫 (30) | ◐ 7 kept |
| so.com 男生中長髮燙髮 (TW, 76) | ◐ all duplicates of mainland results after dedupe |
| so.com 男生及肩燙髮韓系 (TW, 57) | ◐ 4 kept |
| so.com 男生中長髮後梳 (TW, 63) | ◐ 4 kept |
| so.com 男仔長髮電髮 (HK, 45) | ◐ 0 unique after dedupe |

### Sites
| URL | Result |
|---|---|
| style-map.com/styles → /styles/man (Chrome) | ✓ full TW men's tag taxonomy, see §3.3 |
| style-map.com/style/4655, 4764, 7984, 8991, 10694, 11264 | ✓ 12 作品 each; 18 kept overall |
| style-map.com/search?keyword=… | ✗ 404 — StyleMap has no keyword search route |
| cdn.style-map.com/post/photo/large/<id>.jpg | ✓ 1500×1500 with Referer |
| faxingsj.com/nanshengfaxing/ | ✓ index reachable [WebFetch] |
| faxingsj.com/nanshengfaxing/nanshengchangfa/ | ◐ real 男生长发 category, newest post 2020, images ≤500×350 |
| faxingw.cn/nanshengfaxing/ | ✗ 404 [WebFetch] |
| sohu.com/a/345205203_643953 (金秋"潮流男发"发型书) | ◐ 15 × 1080×1416 发型书 page scans, downloaded and inspected — **all short cuts**, discarded |
| sohu.com/a/451895452_444147 (开春"潮流男发"发型书) | ◐ lazy-loads; only 1 image resolved before I moved on |
| cdn `5b0988e595225.cdn.sohucs.com/images/<date>/<key>.jpeg` | ✓ downloadable with Referer sohu.com (note: `p3.itc.cn` mirror returns a 432-byte stub) |
| menpermhk.com/services + /services/korean-texture-perm | ✓ HK men's perm taxonomy + technique + HK$880 |
| canvasblend.com 香港男士電髮2026 完整指南 | ◐ surfaced via Google, not fetched in full |
| google.com `男仔 長髮 電髮 韓式 香港 髮型屋` (Chrome) | ✓ produced the whole HK salon list |
| search.books.com.tw `髮型設計`, `男士髮型` | ✓ reachable, see §5 |
| books.com.tw/products/0010763436 | ✓ 絕版, no preview |
| search.books.com.tw `.../query/key=<term>` (no `/cat/all/key/`) | ✗ returns an empty keyword — must use `/search/query/cat/all/key/<term>` |
| ptt.cc/bbs/hairdo/index.html | ✓ readable logged-out |
| ptt.cc/bbs/hairdo/search?q=男+中長髮 | ◐ **1 result only** — 「[請益] 男 中長髮 中分 推薦設計師」. PTT hair board is thin for this. |
| dcard.tw/search?query=男生 中長髮 燙髮 | ✓ **readable logged-out** — 美髮 board has real threads (`/f/hairsalon/p/238131485` 男生中長髮日系燙, 256960561, 262073568, 235756223, 241943136, 258643201, 255188394, 254558401, 261907020, 261239563, 258291921, 255130078) |
| dcard.tw/f/hairsalon/p/238131485 | ◐ text yes, **no inline photos** (post links out to a Dcard video + FB/IG). Salon named: 西門町 染燙 x 學 Hair, Taipei, stylist Ting. |

### Login walls (all confirmed this pass, all skipped per instructions)
| Site | Status |
|---|---|
| **xiaohongshu.com** | ✗ **hard login wall** — search page renders "登录后查看搜索结果" + QR/phone login only. 4 images on page, none content. |
| **zhihu.com** | ✗ **CAPTCHA + login** — `/search` redirects to `/account/unhuman?…&need_login=true`, "系统监测到您的网络环境存在异常…请点击下方验证按钮". Not solvable without solving a CAPTCHA. Consistent with the prior pass's WebFetch 403 on zhuanlan.zhihu.com. |
| **douyin.com** | ✗ not opened directly (known wall); **its images are reachable indirectly via 360 image cache** — several kept files trace to douyin source pages |
| **weibo.com** | ✗ not attempted — known wall |
| **instagram.com** | ✗ known wall (prior pass); all the HK salons are IG-primary, which is why HK yielded text but no gallery |
| **dcard.tw** | ✓ **not walled** for reading (only a dismissible sign-in banner) |
| **ptt.cc** | ✓ not walled |

---

## 7. Not tried / next

**Highest value first:**

1. **Sweep more 360 queries** — the pipeline is built and cheap now (§0). Untried and likely
   productive: `男生长发中分烫`, `男生长卷发发型`, `男明星中长发烫发`, `男生齐肩发型 韩国`,
   `男生长发披肩 直发`, `男生中长发 狼尾 烫`, `男生 锁骨发` (collarbone length — a rising CN term),
   `男生 海藻烫`, `男生 慵懒卷`. Also try `sn=120,180` for deeper pages of the queries that worked.
2. **StyleMap remaining men's tags** — I only pulled 6 of ~16. Untried ids/tags: 紳士波紋卷,
   嬉皮卷, 栗子頭, 男士燙髮, 韓系歐巴髮型, 男士逗號瀏海, 男生個性剪, 簡單好整理. Get their `/style/<id>`
   from `style-map.com/styles/man` and reuse the CDN pull in §2D.
3. **Sogou image search** (`pic.sogou.com/napi/pc/searchList?…`) — untested, would give a
   second independent CN pool with different dedupe.
4. **大眾點評 (dianping) salon 作品 pages** — several of the best images trace here. Untested
   whether `m.dianping.com/shop/<id>` galleries are readable logged-out.
5. **canvasblend.com full article** and the other 6 menpermhk `/services/*` pages — for the
   HK perm-type comparison table (韓式 vs 法式紋理燙, 鋼夾 vs 摩根 vs 氣墊).
6. **Dcard 美髮 threads** — 12 thread URLs listed above, none read past the first. Worth a text
   pass for TW salon/stylist names and prices even though photos are absent.
7. **当当 / 豆瓣 / HK 商務印書館** book checks — not done. Expectation is low given §5.
8. **`hair.2liang.net`, `meifazhan.com`, `beauty.yxlady.com`, `3g.xiziwang.net`** — these
   surfaced as sources of kept images; their own category pages were never visited and may hold
   larger originals than the 360 cache (which capped several files at 400 px).
9. Upgrade resolution: for the ~48 files under 400 px, the 360 record's `img` field holds the
   original source URL. I did not export those (would have cost ~12 extra round trips). A future
   pass could re-run the queries and try `img` first, falling back to the CDN thumb.
