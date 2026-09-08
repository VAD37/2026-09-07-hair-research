# 06 — Japanese salon-catalog / perm-book FREE preview PDFs (立ち読み) & sample spreads

Run date: 2026-09-08. Goal: find MORE material like the two 男髪セレクション 立ち読み PDFs the user
already loved, biased toward **medium-to-long men's styles with perm/wave**.

## 0. The key discovery — hairmode.jp preview PDFs are fully enumerable

**女性モード社 = ヘアモード社 = hairmode.jp = j-mode.co.jp** (one publisher, three names;
`j-mode.co.jp/book/*` 301s to `hairmode.jp/product/books/*`). So target "女性モード社" and
"ヘアモード社" collapse into one source — and that one source turned out to hold essentially
every Japanese pro men's hair/perm catalog worth having.

Mechanism (reusable):

1. WooCommerce Store API is public and unauthenticated:
   `https://hairmode.jp/wp-json/wc/store/v1/products?per_page=100&page=1..9` → **829 products**
   (books + monthly magazines), with name, permalink, price, description.
2. Each product page carries a dFlip flipbook link: `https://hairmode.jp/flipbook/?dfb_id=<N>`.
   **357 of 829 products have one.**
3. That flipbook page's inline JS contains the raw PDF URL:
   `https://hairmode.jp/wp-content/uploads/<name>.pdf` — **356 resolvable preview PDFs sitewide.**
   Filenames are either descriptive (`otokogami2025_tachiyomi.pdf`, `GOALD_tachiyomi.pdf`) or an
   md5 hash. Some are percent-decoded Japanese (`男髪セレクション2021-SUMMER_ヘアカタ_立ち読み.pdf`).
   The JS embeds them JSON-escaped (`\/` and `\uXXXX`) — you must un-escape before fetching.
4. Plain `curl`/`urllib` with a normal UA downloads them. No login, no referer needed, no rate limit hit.

Gotchas: `wp-json/wp/v2/media?mime_type=application/pdf` reports `X-WP-Total: 366` but returns an
empty array (attachments not exposed). `hairmode.jp/sitemap_index.xml` has **no** product sitemap.
`j-mode.co.jp/sample/` ("立ち読み＆DVDお試し" index) is JS-rendered and returns nothing useful —
the API route above is strictly better.

---

## 1. Downloaded — `images/pdf/` (42 PDFs, ~321 MB, 1,192 preview pages)

All from **ヘアモード社 (hairmode.jp)** unless noted. "M/L" = pages in the *preview* showing
medium-or-longer men's styles. ✔ = I visually audited the whole preview via a contact sheet;
`~` = estimated from contents pages / category structure, not page-by-page audited.

### 1a. 男髪セレクション (Otoko-gami Selection) — the exact series the user liked, ALL years

| Year / title | Price | Pages | File | M/L men |
|---|---|---|---|---|
| 男髪セレクション2025 (101 styles) `jm36090` | ¥4,200 | 21 | `hairmode_jm36090_otokogami-selection-2025.pdf` | ✔ ~6 (No.050, 051, 076, 077 + MEDIUM section opener) |
| 男髪セレクション2024 (100 styles) `jm32665` | ¥4,000 | 31 | `hairmode_jm32665_otokogami-selection-2024.pdf` | (user already had) |
| 男髪セレクション2023-2024 甘＆辛 `jm28111` | ¥4,000 | 38 | `hairmode_jm28111_otokogami-selection-2023-2024.pdf` | ✔ ~8 (甘 AMA-style No.01/02/04/05, 51, 52, 59 all medium wavy) |
| 男髪セレクション2023 「小顔に見える」 `jm26714` | ¥3,900 | 30 | `hairmode_jm26714_otokogami-selection-2023.pdf` | (user already had) |
| 男髪セレクション2022 (50 styles) `jm21104` | ¥3,900 | 28 | `hairmode_jm21104_otokogami-selection-2022.pdf` | ~4 |
| 男髪セレクション2022 SPRING `jm23114` | ¥3,900 | 22 | `hairmode_jm23114_otokogami-selection-2022-spring.pdf` | ~3 |
| 男髪セレクション2022 SUMMER `jm24450` | ¥3,900 | 22 | `hairmode_jm24450_otokogami-selection-2022-summer.pdf` | ~2 |
| 男髪セレクション2021 SUMMER `jm17832` | ¥3,900 | 22 | `hairmode_jm17832_otokogami-selection-2021-summer.pdf` | ~2 (fade/short-heavy) |
| 男髪セレクション2019-2020 (100 styles) `jm9192` | ¥3,800 | 16 | `hairmode_jm9192_otokogami-selection-2019-2020.pdf` | ~2 |
| 男髪セレクション18-19 `jm1049` | ¥3,800 | 46 | `hairmode_jm1049_otokogami-selection-18-19.pdf` | ~3 (largest preview of the series) |
| 男髪セレクション特別編集 メンズテクニック集 `jm13676` | ¥3,200 | 20 | `hairmode_jm13676_otokogami-mens-technique-collection.pdf` | ~2 |
| 男髪パーツ図鑑 (544 parts) `jm12746` | ¥3,000 | 27 | `hairmode_jm12746_otokogami-parts-encyclopedia.pdf` | parts-only; nape/length axis |
| メンズヘアパーツ図鑑 (200+ parts) `jm22769` | ¥3,200 | 24 | `hairmode_jm22769_mens-hair-parts-encyclopedia.pdf` | parts-only; シルエット/毛流れ axes |

Missing from the series: **男髪セレクション2021 (`jm14199`)** and **16-17 (`jm1016`)** — see §3 (dead).

### 1b. Men's PERM books — the highest-value group for this project

| Title | Price | Pages | File | Notes |
|---|---|---|---|---|
| **TOKYO MEN'S HAIR BOOK / GOALD** `jm25971` | ¥3,900 | 32 | `hairmode_jm25971_goald-tokyo-mens-hair-book.pdf` | ✔ **best find.** Sections VERY SHORT / SHORT / **MEDIUM (p32-37)** / **2WAY (p38-43)** / 4WAY STYLE CHANGE. Contains a **WAVE & CURL strength scale** (10-30% / 40-50% / 60-70% / 80%+ with side photos) = literally an "how curly do I want it" order chart. Also スパイラルパーマ process, WILD CURL, "flowing hair" editorial. Nakamura Tomekichi's GOALD. |
| **いま知っておきたい メンズパーマテクニック22選** `jm33684` | ¥4,200 | 33 | `hairmode_jm33684_mens-perm-technique-22.pdf` | ✔ **2nd best.** 22 *named* men's perm techniques w/ full-page model photos, many medium-length: モイストパーマ / シャドウパーマ / フェザーパーマ / サーフカール / ラフミックスカール / ウエーブルーズ / ファジーウエーブ / スパイキーツイスト / 縦落ち重心マッシュ / ウィービングパーマ / テクスチャーパーマ / アンニュイムーブ / スレンダーツイスト / コンパクトカール / プードルスパイラル / ソフトムーブカール / スペインカール / ワイルドグロッシーウエーブ / パラシュートウエーブ / スクリュースパイラル / タルフカール. Part 3 = GOALD式, Part 4 = ROOTS & RESSUAL. |
| メンズパーマテクニック完全マスター `jm29830` | ¥4,000 | 42 | `hairmode_jm29830_mens-perm-technique-master.pdf` | 42-page preview, design-setting + 似合わせ |
| メンズパーマのヘアカタログ 2021-2022 `jm19558` | ¥3,900 | 38 | `hairmode_jm19558_mens-perm-haircatalog-2021-2022.pdf` | ✔ 100% men's perm but categories are all SHORT: STANDARD SHORT×PERM / MUSH SHORT×PERM / PARTING STYLE×PERM / BUSINESS STYLE×PERM. **M/L ≈ 0.** Still gold for technique: ツイストスパイラル / ツイスト / 波巻き / 骨格補正パーマ / 2WAYがかなえるパーマ, ON↔OFF styling change, 顔周り・バング編 parts grid |
| メンズパーマのヘアカタログ (60 styles, 1st ed.) `jm7122` | ¥3,200 | 17 | `hairmode_jm7122_mens-perm-haircatalog.pdf` | short-length focused |
| fifthのメンズパーマ必修テキスト `jm35360` | ¥4,000 | 24 | `hairmode_jm35360_fifth-mens-perm-textbook.pdf` | 2025, fifth salon, 1-min video-linked |
| Y.O.G.パーマメソッド (貴龍) `jm27040` | ¥3,800 | 32 | `hairmode_jm27040_yog-perm-method.pdf` | men's rod-division method |
| メンズアイロンパーマ攻略本 `jm27997` | ¥4,000 | 34 | `hairmode_jm27997_mens-iron-perm-strategy.pdf` | 8mm round iron perm; 5 masters' style set |
| ＋パーマで簡単補整 メンズヘアの7大お悩み解決BOOK `jm26034` | ¥4,200 | 22 | `hairmode_jm26034_mens-hair-7-problems-perm.pdf` | **directly relevant**: 直毛/硬毛/軟毛/乾燥毛/ミックス毛/クセ毛/ハチ張り solved with perm — the "my hair is too straight and thick" problem |
| 「ポイントパーマ」簡単活用BOOK `jm21052` | ¥3,500 | 30 | `hairmode_jm21052_point-perm-book.pdf` | partial/root perms (= down-perm adjacent) |
| 複雑履歴毛のためのパーマブック `jm30868` | ¥4,000 | 38 | `hairmode_jm30868_perm-book-damaged-history-hair.pdf` | perming damaged/bleached hair |
| アイロン風パーマまるわかりBOOK `jm31978` | ¥4,200 | 24 | `hairmode_jm31978_iron-style-perm-book.pdf` | コテ巻き風 / 韓国風 / 波巻き風 (mostly female models) |
| 100％リアルパーマ！テクニック `jm13840` | ¥3,200 | 30 | `hairmode_jm13840_100-real-perm-technique.pdf` | no-iron finish philosophy |
| 見るだけで学べる【パーマ編】ボリューム学 (DADA 西戸裕二) `jm5033` | ¥2,800 | 46 | `hairmode_jm5033_perm-volume-technique-dada.pdf` | ± volume control |
| BASIC OF BASIC 06 パーマ〈レイヤー上〉 `jm879` | ¥1,400 | 26 | `hairmode_jm879_basic-of-basic-06-perm-layer-a.pdf` | textbook, layer + perm |
| BASIC OF BASIC 07 パーマ〈レイヤー下〉+ケミカル `jm885` | ¥1,400 | 24 | `hairmode_jm885_basic-of-basic-07-perm-layer-b.pdf` | |
| BASIC OF BASIC 08 パーマ〈グラデーション〉 `jm890` | ¥1,400 | 24 | `hairmode_jm890_basic-of-basic-08-perm-graduation.pdf` | |

### 1c. Korean-style men's hair

| Title | Price | Pages | File | M/L men |
|---|---|---|---|---|
| **メンズ韓国ヘアBOOK** `jm23541` | ¥3,500 | 25 | `hairmode_jm23541_mens-korean-hair-book.pdf` | ✔ ~5. Mostly mush/short (アイドル系 vs 俳優系), but styles 040/041/042 are ear-to-jaw wavy. Has **PERM STYLE** section (029, 030 = ツイストパーマ, 前髪ウエーブ+バックの毛流れ), コンマバング, シースルーダンディカット, a **襟足(nape) catalog** with a short→long axis, and a **波巻きパーマ術** (wave-winding perm) process spread. Stylist credits incl. GUNHEE TOKYO, ALBUM, gnico |

### 1d. Other men's catalogs / adult men

| Title | Price | Pages | File | M/L men |
|---|---|---|---|---|
| **イケオジのヘアカタログ (60 styles, 40s men)** `jm27189` | ¥4,000 | 28 | `hairmode_jm27189_ikeoji-mature-men-haircatalog.pdf` | ✔ ~7. PERM section; No.15/16/25/26/31/32/49/**50** (medium wavy pushed-back). 2WAY HAIR. IKEOJI BANGS parts grid indexed by hair length short→long. 薄毛カットテクニック |
| メンズヘアテクニック84選 `jm25373` | ¥3,200 | 25 | `hairmode_jm25373_mens-hair-technique-84.pdf` | 7 categories incl. Korean men's hair |
| お客さまの人生を変えるメンズヘアレシピ (DIECE 大月渉) `jm21692` | ¥3,900 | 21 | `hairmode_jm21692_mens-hair-recipe.pdf` | before/after driven |
| メンズビジネスヘアカタログ (65 styles) `jm20296` | ¥3,500 | 22 | `hairmode_jm20296_mens-business-haircatalog.pdf` | ON/OFF styling; short |
| メンズカラーのヘアカタログ 2022 (70 styles) `jm22302` | ¥3,800 | 44 | `hairmode_jm22302_mens-color-haircatalog-2022.pdf` | color, but 44 pages of men |
| ALBUM パーフェクトガイド `jm13842` | ¥980 | 20 | `hairmode_jm13842_album-perfect-guide.pdf` | ALBUM salon; perm + SNS |
| THE BARBER TECH `jm31100` | ¥4,000 | 42 | `hairmode_jm31100_the-barber-tech.pdf` | barber short/fade + perm |
| Hello Barber 新バーバー時代のデザイン＆ロジック `jm1032` | ¥4,000 | 14 | `hairmode_jm1032_hello-barber.pdf` | barber |

### 1e. Unisex perm catalogs (women-dominant, but wave/curl reference)

| Title | Price | Pages | File | Note |
|---|---|---|---|---|
| パーマのヘアカタログ 2022 `jm23548` | ¥3,900 | 42 | `hairmode_jm23548_perm-haircatalog-2022.pdf` | ✔ split **SHORT&BOB / MEDIUM&LONG**; the MEDIUM&LONG spreads (styles 36-40: ウエーブ, ワンカール, ゆるスパイラル, ラフスパイラル) are female models but the *rod/curl recipes and a full rod-size chart* transfer. 2 male models in the styling-change section |
| パーマのヘアカタログ 2018 `jm1043` | ¥3,200 | 22 | `hairmode_jm1043_perm-haircatalog-2018.pdf` | older edition |

### 1f. Salon-published PDF (non-publisher)

| Title | Pages | File | Note |
|---|---|---|---|
| FROG STAR「MEN'S HAIR CATALOG 完全版 2019-20」 | 3 | `salon_frogstar_mens-hair-catalog-2019-20.pdf` | http://www.frogstar.jp/image/concept/mens.pdf — a salon price/menu leaflet with a small men's style grid + ナチュラルパーマ ¥6,900. Thin, but it is a genuine free salon lookbook PDF |

---

## 2. Downloaded — `images/jp-samples/` (23 sample images, 5.2 MB)

**髪書房 KAMISHOBO** (publisher of monthly *BOB*; `boblog.tv` is theirs). No PDF previews anywhere —
they publish loose JPG spreads on the book page and on their BASE shop.

| Book | Files | Note |
|---|---|---|
| **メンズパーマの絶対的基礎 THE THEORY OF MEN'S PERM** (GOALD 佐藤拓弥, 2023) | `kamishobo_mens-perm-zettaiteki-kiso_page-0001/0002/0004.jpg` + `_spread.jpg` + `kamishobo-ec_..._01..08.jpg` | 4 large spreads from kamishobo.co.jp + 8 shop preview images from `kamishobo.official.ec/items/76698355`. `page-0003` and `0005+` are 404 — only 1/2/4 exist |
| 令和のレイヤー完全攻略本 (2023) | `kamishobo_reiwa-layer-book_*.jpg` ×9 | layer-cut book; layered medium/long shapes (unisex) |
| メンズカットのすべて (2022) | `kamishobo_mens-cut-no-subete_spread.jpg` | single small spread only |
| パートカット全部 (2023) | `kamishobo_part-cut-zenbu_spread.jpg` | single spread |

---

## 3. Found but DEAD / blocked

| Item | Why |
|---|---|
| 男髪セレクション2021 `jm14199` | flipbook points to `otokogami2021_cata_tachiyomi.pdf` → **HTTP 404 on hairmode's own server.** Probed all `/wp-content/uploads/YYYY/MM/` variants 2016-2026: none. Not in Wayback (CDX returns 0 PDFs for the domain). Broken on the publisher's site |
| メンズパーマのヘアカタログ 2022-2023 `jm25665` | same — `662bef...pdf` 404. **This is the one real content gap** (it's the direct successor to jm19558) |
| 韓国ヘアBOOK 〜オルチャンスタイル＆テクニック集〜 `jm18344` | same — `25e2ae...-2.pdf` 404 |
| パーマのヘアカタログ 2021 `jm15570` | same — 404 |
| 男髪セレクション 16-17 `jm1016` | product page has **no flipbook at all** (no 立ち読み was ever made) |
| Google web search | **CAPTCHA / `google.com/sorry`** from the user's IP. Did not attempt to solve. Use **`search.yahoo.co.jp`** instead — it works fine in Chrome and supports `site:` and `filetype:` |
| Bing | returns unrelated zhihu.com results for JP queries — useless |
| Fujisan.co.jp | `/search/result/?keyword=` → 404; `/product/1281680822/` → 404; direct curl 404s. FINEBOYS+plus HAIR mooks don't appear to be listed there |
| Amazon.co.jp なか見!検索 / Kindle sample | requires login → **skipped per rules** |
| コスミック出版 (cosmicpub.com) | book pages carry **cover images only**, zero interior preview, no PDF. Confirmed for `/books/8470/` and `/books/6421/` |
| 新美容出版 (shinbiyo.com / shop.shinbiyo.com) | crawled all 64 items in カット/パーマ/カタログ/新刊 categories — **cover thumbnail only, no interior previews.** Their 試し読み is a JS (flickity) widget on magazine issue pages with no image URLs in the HTML |
| 女性モード社 (joseimode.co.jp / josei-mode.co.jp) | **DNS dead — the company IS hairmode.jp.** Not a separate target |
| PREPPY (preppy-web.com) | DNS dead |
| media-soft.biz (メディアソフト レングス別メンズヘアカタログ) | no preview markers, no PDFs on the book page |
| hinode-publishing.jp (FINEBOYS+plus HAIR) | no preview markers, no PDFs |
| Google Books API | HTTP 429 rate-limited on first call; retry later |
| `hairmode.jp/wp-json/wp/v2/media?mime_type=application/pdf` | reports 366 total but returns `[]` (unattached media hidden) |

---

## 4. Query log

### URLs fetched (curl/urllib unless noted)

| URL | Result |
|---|---|
| `hairmode.jp/product/books/jm36090/` | ✓ revealed the `flipbook/?dfb_id=50943` pattern |
| `hairmode.jp/flipbook/?dfb_id=50943` | ✓ revealed `wp-content/uploads/otokogami2025_tachiyomi.pdf` |
| `hairmode.jp/wp-json/wc/store/v1/products?per_page=100&page=1..9` | ✓✓ 829 products |
| `hairmode.jp/wp-json/` (route list) | ✓ found `/wp/v2/media`, `/wp/v2/book_category` |
| `hairmode.jp/wp-json/wp/v2/media?mime_type=application/pdf` | ✗ empty array despite `X-WP-Total: 366` |
| `hairmode.jp/sitemap_index.xml`, `page-sitemap.xml` | ◐ no product sitemap |
| all 829 `hairmode.jp/product/books/*` pages (threaded crawl) | ✓ 357 with flipbooks |
| all 409 `hairmode.jp/flipbook/?dfb_id=*` | ✓ 356 PDF URLs |
| 42 × `hairmode.jp/wp-content/uploads/*.pdf` | ✓ downloaded |
| 4 × ditto | ✗ 404 (see §3) |
| `web.archive.org/cdx/search/cdx?url=hairmode.jp...pdf` | ✗ 0 PDF captures |
| `hairmode.jp/wp-content/uploads/{2016..2026}/{01..12}/<name>.pdf` (×8 files × 133 paths, HEAD) | ◐ 4 of 8 resolved at the *root* path after all (transient 404s on first GET); 4 truly gone |
| `www.j-mode.co.jp/sample/` | ◐ JS-rendered, empty |
| `www.kamishobo.co.jp/sitemap.xml` → `book-sitemap.xml` | ✓ 186 book pages |
| all 186 kamishobo book pages (threaded) | ✓ found the JPG-spread books |
| `kamishobo.co.jp/wp-content/uploads/2023/05/page-000{1..15}.jpg` | ◐ only 0001, 0002, 0004 exist |
| `kamishobo.official.ec/items/76698355` | ✓ 8 preview images |
| `kamishobo.official.ec/?keyword=メンズ` | ✗ keyword filter is client-side; same 24 items for any keyword |
| `boblog.tv/` + sitemap | ◐ BOB = 髪書房; no separate previews |
| `shop.shinbiyo.com/` + `/view/category/{ct6,ct7,ct8,ct13}` + 64 item pages | ✗ covers only |
| `www.shinbiyo.com/`, `/sitemap.xml`, `/shinbiyo-2026年9月号/` | ✗ 試し読み is a JS widget |
| `www.cosmicpub.com/books/8470/`, `/books/6421/`, `/?s=メンズヘア` | ✗ covers only. (Noted: **メンズヘアカタログ完全版2026-2027** exists at `/books/8470/` — newer than the 2025-26 in notes/03) |
| `www.media-soft.biz/book/b648071.html` | ✗ |
| `www.hinode-publishing.jp/fb_extranumber/` | ✗ |
| `www.boblog.tv/post/4447/` | ✗ no preview |
| `www.fujisan.co.jp/search/result/?keyword=ヘアカタログ`, `/product/1281680822/` | ✗ 404 |
| `www.josei-mode.co.jp`, `preppy-web.com` | ✗ DNS dead |
| `http://www.frogstar.jp/image/concept/mens.pdf` | ✓ downloaded (3 pp) |
| `googleapis.com/books/v1/volumes?q=…` ×6 | ✗ HTTP 429 |

### Search queries

| Engine | Query | Result |
|---|---|---|
| Google (Chrome) | `メンズ ヘアカタログ 立ち読み pdf` | ✗ **CAPTCHA wall** — abandoned Google entirely |
| Bing (Chrome) | `メンズ ヘアカタログ 立ち読み pdf` | ✗ returned zhihu.com noise |
| **Yahoo! JAPAN (Chrome)** | `メンズ ヘアカタログ 立ち読み pdf` | ✓ surfaced frogstar.jp salon PDF + j-mode `/sample` |
| Yahoo! JAPAN | `filetype:pdf メンズ ヘアカタログ パーマ` | ✓ confirmed hairmode uploads path; found frogstar, prize-hair.com, trunk-ehairdesign.com, tayanet.jp, heritage.inc 媒体資料 (all thin/ad material) |
| Yahoo! JAPAN | `男髪 立ち読み pdf ヘアモード` | ✓ found `j-mode.co.jp/sample`, catapoke.com (HAIR MODE subscription viewer — paywalled) |
| Yahoo! JAPAN | `site:hairmode.jp filetype:pdf` (pages 1-2) | ◐ only re-surfaced PDFs the API crawl already had, plus monthly `HM####_tachiyomi.pdf` / `PLAN####_tachiyomi.pdf` magazine previews |
| Yahoo! JAPAN | `site:frogstar.jp pdf メンズヘアカタログ` | ✓ exact PDF URL |
| Yahoo! JAPAN | `メンズ ミディアム パーマ カタログ 試し読み` | ✗ only Hot Pepper / Men's Non-no web catalogs (already in notes/02) |
| Yahoo! JAPAN | `メンズ ロング ヘアカタログ 本 2025 2026 パーマ` | ◐ surfaced メンズヘアカタログ完全版2025-2026 on Amazon (no free preview) |
| Yahoo! JAPAN | `女性モード社 書籍 メンズ パーマ 立ち読み` | ✓✓ **confirmed 女性モード社 == ヘアモード社 == hairmode.jp** |

### Tool notes (add to sources.md §1)

- **hairmode.jp**: plain `curl`/`urllib` ✓ everything. Do NOT bother with the browser.
- **Google search from this IP**: ✗ CAPTCHA. **`search.yahoo.co.jp` via Chrome is the working JP search engine** (supports `site:` and `filetype:`; extract result links with `javascript_tool` → `document.querySelectorAll('a')` filtered on `.pdf`).
- **Bing**: ✗ garbage for Japanese queries.
- kamishobo.co.jp ✓ curl; kamishobo.official.ec ✓ curl for item pages, ✗ for search.
- shop.shinbiyo.com ✓ curl (MakeShop); category pages list `/view/item/\d+`.
- cosmicpub.com ✓ curl.
- fujisan.co.jp ✗ curl (404s) and its search paths have changed.

---

## 5. Not tried / next

1. **The 314 other hairmode preview PDFs** I did not download — full URL map is reproducible in
   ~3 minutes with the §0 recipe. Notably the **monthly 月刊 HAIR MODE** previews
   (`HM2103_tachiyomi.pdf` … `HM2602_tachiyomi.pdf`, ~90 issues, 2018-2026, ~10-20 pp each).
   Each monthly has a men's feature a few times a year; worth grepping their contents pages for
   「メンズ」「ミディアム」「ロング」. Cheap, high volume.
2. **Buy-only gap**: メンズパーマのヘアカタログ 2022-2023 (`jm25665`, ¥3,900) — preview dead, and it is
   the most on-topic single title after the 22選 book. Consider the **電子版 (ebook) variation** on
   the same product page, or ask hairmode support to re-upload.
3. **catapoke.com/jbooks** — "HAIR MODE Web Viewer", a 読み放題 subscription that carries the full
   books. Paywalled; not attempted (no login).
4. **新美容出版「大人男子のパーマBOOK」** (`shop.shinbiyo.com/view/item/000000000124`) and
   **「格好いいMEN'S HAIRの仕立て方」** (`/000000000114`) — identified, no preview exists online.
   Only route is purchase or a bookstore 立ち読み widget (honto / 紀伊國屋 / 楽天ブックス — **not yet tried**).
5. **honto / 紀伊國屋 / 楽天ブックス / 7net / Yodobashi 試し読み** for メンズヘアカタログ完全版2026-2027
   (cosmicpub `/books/8470/`) — not attempted this run.
6. **Google Books API** — retry after the 429 cools down; query 男髪セレクション / メンズヘアカタログ完全版
   for `viewability: PARTIAL`.
7. **Salon lookbook PDFs**: only frogstar hit. LIPPS / OCEAN TOKYO / GOALD / Dot+LIM / ALBUM / Lond
   publish styles as web galleries, not PDFs. Try `site:*.jp filetype:pdf サロン 求人 メンズ スタイル`
   (recruiting brochures often embed 20-30 style photos) — `prize-hair.com/prize_pamphlet2024` was
   one such hit and was **not** downloaded.
8. **KR/CN equivalents**: no Korean or Chinese publisher preview PDFs were searched this run — the
   brief was JP-only. Korean 미용 전문서적 publishers (청구문화사, 구민사) and Taiwanese 博客來 試閱
   are untouched.
9. Contact sheets for all 42 PDFs live in the scratchpad only. If a permanent per-page audit is
   wanted, re-render with `pymupdf` at 300px/page into `images/pdf/_sheets/`.
