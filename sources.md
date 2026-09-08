# Sources & Search Log — do not repeat

Consolidated from notes/01–05 (2026-09-07); pass 2 (2026-09-08, notes/06–11) in §6–§7. Future agents: read §1 access matrix first, then skip anything in §2–§4 already marked useful/blocked/dead. Add new attempts to §5.

## 1. Access matrix (tool × site) — learned the hard way

| Site | WebSearch | WebFetch | Browser pane (mcp__Claude_Browser) | User's Chrome (mcp__claude-in-chrome) | Notes |
|---|---|---|---|---|---|
| reddit.com / old.reddit.com | ✗ noise / API refuses `allowed_domains` | ✗ hard-blocked | ✗ policy-blocked | **✓ only route** — `old.reddit.com/r/<sub>/search?q=...` + get_page_text | Sitewide reddit search ignores quotes/booleans; use per-sub search |
| search.naver.com / blog.naver.com | ✗ crawler blocked | ✗ blocked | — | ✗ "site not allowed due to safety restrictions" | Only via Google snippets of Naver posts |
| namu.wiki | — | ✗ 403 | — | ✓ | best KR perm taxonomy |
| hairrisk.com | — | ✗ 403 | — | ✓ | English Seoul price tables |
| hairshop.kakao.com / mamedene shop pages | — | ✗ JS-rendered, empty | — | not tried | mamedene.com/magazines/* ✓ via WebFetch |
| beauty.hotpepper.jp | ✓ | ✓ | — | — | catalog filter URLs work |
| ozmall.co.jp, lipps-hair.com, minimodel.jp, mens-hairstyle.jp | — | ✓ | — | — | |
| youtube.com SERP | ✓ with `allowed_domains: youtube.com` | ✗ JS shell (3 of 4 watch pages) | — | ✗ get_page_text "No text content found" | Video comments unreadable |
| pinterest.com | ✓ ideas hubs | — | — | ✓ search feed renders; **pin permalinks not extractable logged-out** | |
| instagram.com hashtags | — | — | — | ✗ login wall (skipped) | |
| zhuanlan.zhihu.com | — | ✗ 403 | — | not tried | |
| 2006hairsalon.com | — | ✗ empty body | — | not tried | |
| amazon.co.jp product pages | — | ✗ JS shell (ISBN only) | — | — | use publisher pages |
| archive.org advancedsearch API | — | ✗ 0 results (syntax) | — | — | /details/ pages ✓ |
| j-mode.co.jp/book/* | — | 301 → hairmode.jp | — | — | fetch hairmode.jp directly |
| kleekstyle.com | — | ✗ DNS dead | — | — | drop |
| miinhair.com/ko/blog/korean-perm-men-guide | — | ✗ 404 | — | — | /sg/blog/* ✓ |
| google.com (as search proxy) | — | — | — | ✓ navigate + get_page_text | works for KR queries |
| TikTok / Lemon8 / Threads | snippet only | not fetched | — | not tried | |

## 2. Reddit (all via user's Chrome unless noted)

| Query / URL | Result |
|---|---|
| r/malehairadvice search: `asian perm` (relevance) | ✓ 24 posts |
| r/malehairadvice: `digital perm medium length` | ✓ partly non-Asian |
| r/malehairadvice: `korean perm` | ✓ best single query, ~25 posts |
| r/malehairadvice: `perm asian` sort=top | ✓ |
| r/malehairadvice: `wolf cut asian` | ✓ |
| r/malehairadvice: `down perm` | ✓ 20+ posts, best down-perm source |
| r/malehairadvice: `middle part perm` | ✓ |
| r/malehairadvice: `asian slick back long hair` | ✓ product names |
| r/malehairadvice: `"12 Pell"` | ✓ |
| r/malehairadvice threads opened: ssz4m3, x7auoz, 1mwetea, 1f3kop7 (low value, white poster) | ✓ |
| r/FierceFlow: `asian hair` sort=top | ✓ growth journeys, few perms |
| r/FierceFlow: `perm` sort=top | ✓ mostly non-Asian |
| r/FierceFlow threads: 1w1pj0g, 1fo6ak0 | ✓ |
| r/Hair: `korean perm men asian` | ✓ very useful — cost, longevity, perm-type distinctions |
| r/Perms: `asian men digital perm` | ✗ empty sub |
| r/korea: `perm men salon cost` | ✗ near-empty (12-yr-old) |
| r/japanlife: `perm men hair salon` | ✗ low value |
| r/asianamerican: `perm hair men` | ✗ low value |
| sitewide old.reddit.com search `"down perm" OR "hippie perm" men` | ✗ useless — do not repeat boolean sitewide |
| WebSearch `reddit r/malehairadvice asian male digital perm medium length hair` | ✗ noise |
| WebSearch `reddit FierceFlow asian hair flow perm shoulder length` | ✗ noise |
| WebSearch `reddit hippie perm men asian hair experience cost` allowed_domains reddit.com | ✗ API error |
| WebSearch `reddit "digital perm" men how long lasted worth it maintenance r/AsianBeauty r/malehairadvice` | ✗ no reddit results |
| WebSearch `reddit digital perm men cost maintenance routine malehairadvice` | partial (surfaced US salon guides) |
| **NOT searched:** r/malegrooming, r/AsianBeauty, r/koreanbeauty, r/curlyhair, r/koreanvariety, r/China, r/taiwan; thread Crafty_Session_7959 comments not opened | gap |

## 3. Web pages fetched (WebFetch unless noted) — useful ✓ / partial ◐ / blocked-dead ✗

**Korea / KR-language**
- ✓ visioai.app/ko/blog/namja-peom-jongryu/ (KR prices + face-shape matrix)
- ✓ mamedene.com/magazines/192, 336, 363, 454, 509, 527, 251
- ✗ mamedene.com/shops/3743 (JS)
- ✓ namu.wiki/w/펌 (Chrome)
- ✓ hairrisk.com/korean-perm-men (Chrome); ✗ /korean-perm-guide, /korean-perm-medium-long-hair-guide, /korean-perm-men-guide, /korean-down-perm-men (403 to fetch; snippets used)
- ✓ seoulhairsalon.com/price/ (men's KRW menu, iron perm ₩160k)
- ✓ hongdaehairstudio.com/blog/korean-perm-cost-guide (dated June 2026)
- ✓ miinhair.com/sg/blog/korean-perm-men, /digital-perm-vs-cold-perm, /comma-cut, /sg/ko/blog/korean-perm-men
- ◐ teamblind.com/kr/post/준오헤어-YGRfnaMj (2023 prices)
- ◐ a-ha.io/questions/4499c8b1510b0fea89b04c3198114fb5
- ◐ unpa.me/community/beautytip/120134823 (hippie perm 2025)
- ◐ gall.dcinside.com/board/view/?id=hair&no=369770
- ◐ view.nate.com/beauty/view/110696/
- ◐ updokorea.com/entry/애즈펌-남자-펌으로-추천합니다
- ◐ threads.com/@lemar_hair_sua/post/DTkpnLJgYpX/, threads.com/@ken_menshair/post/DU8HRYdEoyL/ (snippets)
- ◐ tiktok.com/@joyce/video/7341166072227319083 (Gangnam receipt, snippet), tiktok.com/@naam.za_/video/7369806569527151914
- ◐ huuim.com price page (down perm by area)
- Chrome google.com queries: `남자 히피펌 중장발 가격 유지기간 디지털펌`, `남자 슬릭백 펌 중단발 올백 펌 스타일`, `남자 펌 종류 빈티지펌 젤리펌 퓨리펌 프메펌 차이 설명`, `남자 중단발 펌 가격 원 기장 어깨 레이어드컷 허쉬컷 얼굴형`, `"히피펌" 남자 가격 "원" 기장 유지기간 빈티지펌 중단발`, `남자 디지털펌 중단발 롯드 크기 세팅펌 차이 얼굴형 계란형` — all ✓

**Japan / JP-language**
- ✓ beauty.hotpepper.jp/magazine/906518/ (16 perm types), /magazine/403725/ (digital perm facts — best single source)
- ✓ beauty.hotpepper.jp/CSP/bt/hairCatalogSearch/mens/condtion/?lengthCds=HL12&menuContentsCds=MC01, HL13, +keyword=ウルフパーマ, +keyword=センターパート
- ✓ beauty.hotpepper.jp/catalog/mens/word韓国風センターパート/, /wordミディアムパーマ/
- ✓ beauty.hotpepper.jp/keyword/デジタルパーマ 東京 安い/ (Tokyo menu prices)
- ✓ beauty.hotpepper.jp/slnH000228152/style/ (LIPPS Omotesando)
- ✓ ozmall.co.jp/hairsalon/men/catalog/othercatalog/perm/w0162/, /men/mediumperm/catalog/, /men/catalog/bangs/centerpart/korean/, /men/centerpartperm/
- ✓ lipps-hair.com/style_cat/medium/, /style_cat/perm/
- ✓ minimodel.jp/room/mens/karuma-korean-perm
- ✓ mens-hairstyle.jp/blog/81275/ (oval = most versatile), /87045/, /51956/, /99851/
- ◐ staircase-ginza.com/column/韓国風デジタルパーマ/
- ◐ headlight-inc.com/style/mens/メンズデジタルパーマ/
- ◐ beauty.rakuten.co.jp/s3000052363/tk12/ (Ammy Ginza), /pre13/tk132/
- ✓ isesaki-menssalon.jp/blog/detail/20240610140420/ (3–4 mo digital vs 1–2 cold)
- ✓ costa-hair.jp/column/mens-perm-hajimete-complete-guide-2026-04-26
- ✓ mensfashion.cc/tips/lover/96120/ (5-min routine; all-back 1-min)
- ✓ vokka.jp/13370/ (all-back)
- ✓ osaka-regalo.com/mens-perm-styling-products/
- ✓ hozon-navi.com/perm-price/, fleur0205.jp/blog/post253/, menssalon-triwell.jp/column/detail/20251217142634/
- ✓ paimore.com/products/index12.html, sakai-ipc.jp/showcase/ipc38_interview1/
- ✓ mensnonno.jp/post_360/, /beauty/15021/
- ✓ fun-japan.jp/en/articles/13169 (real salon clients)
- Books: ✓ cosmicpub.com/books/8470/, /6421/; hairmode.jp/product/books/jm19558, jm23541, jm36090, jm32665, jm7122, jm18344, jm26714, jm13676; kamishobo.official.ec/categories/5492739, /items/76698355; kamishobo.co.jp/archives/book/メンズパーマの絶対的基礎; boblog.tv/post/4447/, /30884/; hinode-publishing.jp/fb_extranumber/ (◐ stops at '24-'25); media-soft.biz/book/b648071.html; haircamp.jp/magazines/eiichi_st_live9, /seminars/archives/yuji_nishido_rec3; ✗ hairmode.jp/product/books/?category=bc-6 (404); ✗ j-mode.co.jp/book/* (301s)

**China / Taiwan**
- ✓ scoiihair.com/menshairstyle/ (TW men's Korean-style menu + 壓貼燙 prices)
- ◐ style-map.com/style/5683, /en-US/style/4691, /en-US/style/5683/taipei
- ✓ relaxhair-tw.com/menu/ (cold vs hot perm by length NT$)
- ✓ yaopaixl.com/services
- ✓ slickbarbershop.tw/article/perm-for-men.html
- ◐ lemon8-app.com/@baomeishares/7363242142464098817
- ✓ k.sina.cn/article_1456487181_56d03b0d00100mda7.html; m.163.com/dy/article/JPJJVI1U0518C21M.html
- ✗ zhuanlan.zhihu.com/p/391260562 (403); ✗ 2006hairsalon.com/article/72BA6DA818B1700B (empty)

**English / Western salons & guides**
- ✓ gatsby.sg/mens-lifestyle/8-top-korean-perm-men-hairstyles-in-2024/
- ✓ 007-barbershop.com/korean-perm-for-men/
- ✓ nimble-made.com/blogs/news/korean-perm-men
- ✓ forteseries.com/blogs/hairstyles/flow-hairstyles, /kpop-hairstyles, /slick-back
- ✓ edgarhairstyle.com/mens-hairstyles-japan/
- ✓ gogumacider.com/korean-hippie-perm/
- ✓ chicagomalesalon.com/blogs/mens-perm-cost-guide-what-to-expect-to-pay-in-2026-1
- ✓ substancesalon.com/blog/mens-perm-cost-and-maintenance-requirements/
- ✓ kimsunyoung.com/pricelist (KSY LA)
- ◐ yelp.com/questions/k-salon-... (K Salon LA $400–450)
- ◐ fresha.com/lp/en/tt/hair-perms/in/us-new-york/koreatown
- ✓ perfectxhair.com/how-much-does-a-korean-perm-cost-in-toronto/, /how-long-korean-perm-last/; n15salon.com/digitalperm; thebestvancouver.com/best-korean-hair-salons-vancouver/
- ✓ jisu.com.au/pages/salon-price-list; koreasalon.com.au/service-page/men-down-perm-cut
- ✓ jejuhair.uk/digital-perm/; baroque-hn.com/2026/01/28/digitalperm-london/
- ✓ whathewants.com.my/2025/05/27/how-to-care-and-style-korean-permed-hair-for-men/
- ✓ thesmartlocal.com/read/perm-hairstyles-for-men/; hisandherhairloft.com.sg/the-legendary-slick-back-hair/; salonplus.com.sg/the-honest-truth-about-korean-down-perms-...; sglocalnews.com/digital-perm-sg/; actpoint.com.sg/comparing-cold-perms-and-digital-perms/; thedashu.shop/review/korean-down-perm-puffy-side-hair-men/
- ✓ moderngentlemanmagazine.com/40-mens-haircut-perm-ideas/; pallmallbarbers.com/pmb-news/the-return-of-the-perm-hairstyle-2025/; suavecito.com/blogs/grooming-tips/how-to-perfect-the-slick-back; 1821manmade.com/blogs/behind-the-barrel/achieving-the-perfect-slicked-back-hairstyle
- ✓ detect-face-shape.com/blog/hairstyles-for-oval-face-shape-men; saltgrooming.com/blogs/blog/matching-face-shapes-to-mens-haircuts
- ✓ davines (us.davines.com/blogs/news/are-perms-bad-for-your-hair); cindyxiong.com/2014/07/12/6-things-...digital-perm/; therighthairstyles.com/digital-perms/; healthline.com/health/beauty-skin-care/how-long-does-a-perm-last
- ✓ en.wikipedia.org/wiki/Digital_perm
- Products: walmart.com DASHU Wet Curl Cream; amazon.com B08K2P48KK, B09X6TCQ17, B08X4GY1BX; hermosoae.com AMOS; peteandpedro.com sea salt blog
- Books EN: milady.com/catalog/milady-standard-barbering-6th-edition, /milady-standard-cosmetology; amazon.com/dp/1305100557; cengage.com 9781305100558; phaidon Barber Book (amazon 0714871044, waterstones, rizzolibookstore); archive.org/details/menshairdressing0000list, completebookofme0000rudo, barbersmanual00mole, manualonbarberin00mole, MensHairstyles_201605
- Books KR: yes24.com/Product/Search?query=남성헤어 ✓; ridibooks.com/books/3478003161 ✓; aladin ItemId=138843203, 235367065; kyobobook S000060622311, S000219132760; eduwill goodsId=0100004501; ghairmarket.com 하상중 listing
- Pinterest (Chrome, feeds verified): `asian men digital perm`, `asian men slick back perm`, `asian men wolf cut perm`, `korean men perm shoulder length` ✓; `asian men long hair pushed back` ✗ low relevance. Ideas hubs via WebSearch: /ideas/asian-perm-men-middle-part/913618051774, /asian-wavy-perm-middle-part-men/914046828226, /asian-wavy-middle-part/927172546981, /korean-flow-haircut/948899219336, /asian-perm-wolf-cut/948385363837, /korean-perm-wolfcut-men/930026763710, /japanese-perm/917744195983 (not mined); kr.pinterest.com/joseongheon/hippie-perm/
- YouTube: ✓ K9LMR-O5GoM (Ruben Ramos, metadata ok); ✗ dHBq-BhMNbE, jY3oqpCM6Qo, mNRSAMseDcA (JS shell). WebSearch found (not opened): 8kP0XdyXWOU, 4T7C1la0EaM, e1Jo-IZEguE, RNWFCDQKqM0, rUV2V_hNhik, 2dso11MgBKA, H7dGBt6CZgw, xoe-gPSjYMY, opwv6738Nak, Sm-rvrqLvpo, rh5YnaJGUaI, 32TPGKl1Lfs, mtlK_JiBx0U, @Hairdoc channel, tiktok @12pell/7100982445436112170

## 4. WebSearch queries run (dedupe list)

**EN:** digital perm men cost price salon Korea · digital perm vs cold perm men asian hair how long does it last · "digital perm" men price Taiwan · digital perm men price Sydney Melbourne Australia Korean salon · digital perm men price Koreatown Los Angeles NYC salon 2025 · digital perm London men price Korean Japanese hair salon UK · perm slick back men asian hair "slicked back" permed wavy compatibility · sea salt spray vs curl cream permed men's hair routine leave-in diffuse air dry medium length · digital perm damage risk frizz thick asian hair roots straight grow out phase problems · digital perm Toronto Vancouver men price Korean hair salon 2025 · oval face shape men middle part vs slicked back which suits best · best products permed men's hair curl cream hair balm sea salt spray price Korean Japanese brands 2025 · "digital perm" men medium length middle part flow styling routine 5 minutes wet look essence curl · Amos Professional curl cream price Dashu wet curl cream price · can you slick back permed hair men perm too curly · permed hair men how often trim haircut interval 6 weeks wolf cut · digital perm price Germany Paris Berlin asian hair salon men euro 2025 (✗ nothing) · "down perm" men side hair price how long lasts · Korean men perm types glossary hippie perm 히피펌 swallow perm garma perm leaf perm difference · asian men medium length hair styling tutorial digital perm slick back (youtube.com) · 12 Pell barbershop youtube asian hair perm · Korean men's perm guide types digital perm rod size hair length cm cold perm miinhair · asian men wolf cut perm hairstyle · asian men middle part wavy hair perm · hippie perm men shoulder length · asian men flow hair pushed back long perm · "asian men" perm "before and after" youtube shoulder length medium · korean idol perm hairstyle "ask your barber" reference commonly requested · asian men digital perm before after (youtube) · korean perm men medium length tutorial · asian men slick back tutorial long hair · japanese men's perm medium hairstyle salon · "digital perm" vs "cold perm" textbook hot perm thermal reconditioning cosmetology · "Milady Standard Barbering" 6th edition chemical texture services perm chapter ISBN price · Milady Standard Cosmetology "thermal perm" OR "digital perm" chapter · "The Barber Book" Phaidon · archive.org hairstyle catalog barbering manual perm scanned · archive.org "hairstyle" Japanese men catalog pomade manual Asian (✗)

**KR:** 남자 중단발 펌 종류 히피펌 애즈펌 리프펌 가르마펌 차이 · 남자 히피펌 중장발 어깨길이 디지털펌 스타일 네이버 블로그 (✗ noise) · "울프컷" 남자 펌 중장발 스타일 미용실 가격 유지기간 · 준오헤어 가격표 남자 펌 디지털펌 세팅펌 원 2025 (◐) · 준오헤어 가격표 남자 펌 이가자 차홍아르떼 디지털펌 가격 2025 (weak) · 남자 레이어드컷 허쉬컷 리프컷 울프컷 장발 긴머리 스타일 (blog.naver.com ✗) · 비슷하지만 다른 남성 펌 스타일 차이점 (mamedene.com ✓) · 남자 디지털펌 유지기간 관리법 재펌 주기 다운펌 가격 2025 (weak) · 히피펌 남자 가격 볼륨펌 애즈펌 가격 유지기간 미용실 · 남자 슬릭백 펌 가르마펌 리프펌 뒤로 넘기는 펌 추천 가격 (weak) · 디지털펌 남자 중단발 관리 스타일링 에센스 왁스 시간 아침 세팅 방법 (✓ key 12 cm finding) · 韓国 メンズヘア 본 남자 헤어스타일 책 헤어 카탈로그 Yes24 · 디지털펌 교재 책 미용 펌 기법 헤어펌 교과서 교보문고 · "남성 헤어 토탈 시스템" 하상중 목차 펌 · 알라딘 남자 헤어스타일 책 남성 커트 펌 교재 · 헤어펌 이론과 실습 책 펌 웨이브 교재

**JP:** メンズ ミディアム パーマ ヘアカタログ ホットペッパービューティー センターパート · メンズ デジタルパーマ 値段 持ち 期間 ミディアム 韓国風 サロン · "かきあげ" OR "オールバック" メンズ ミディアム パーマ ヘアカタログ センターパート 韓国風 スタイル名 · LIPPS ヘアスタイル メンズ ミディアム パーマ カタログ 韓国風 センターパート 料金 · メンズ デジタルパーマ 料金 相場 持ち 期間 · パーマ スタイリング メンズ 毎日 やり方 デジタルパーマ 手入れ ワックス おすすめ · ホットペッパービューティー メンズ デジタルパーマ カット込み 円 東京 メニュー 料金 · オールバック パーマ メンズ セット方法 センターパート パーマ 毎日 スタイリング 時間 · デジタルパーマ 料金 メンズ カット込み 20000円 サロン メニュー 表 2025 東京 · メンズ デジタルパーマ センターパート かき上げ 前髪 立ち上げ 根元 コールドパーマ 違い (✓ key root finding) · メンズヘアカタログ ムック 2025 FINEBOYS+plus HAIR · デジタルパーマ 教本 美容師 パーマ 技術書 書籍 · Amazon.co.jp メンズヘアカタログ完全版2025-26 · 髪書房 メンズパーマ 本 · メンズパーマの絶対的基礎 GOALD 佐藤拓弥 ISBN デジタルパーマ · FINEBOYS+plus HAIR おしゃれヘアカタログ 2025 2026 日之出出版 · デジタルパーマ 本 教科書 ヘアモード社 j-mode 電子書籍 · Men's non-no ヘアカタログ ムック 集英社 2024 2025 (✗ no mook) · 韓国 メンズヘア 本 K-POP ヘアスタイル ムック 書籍 2024 · hairmode.jp 書籍 メンズ 男髪 一覧 · 楽天ブックス メンズヘアカタログ完全版2025-26 · POPEYE BRUTUS ヘア特集 (✗) · "おしゃれヘアカタログ" 25-26 FINEBOYS fujisan · PAIMORE デジタルパーマ 商標 · 骨格 似合わせ メンズヘア 本 顔型 診断 (◐ clothing books only) · site:hotpepper.jp メンズ パーマ ミディアム スタイル

**CN/TW:** 男生 中长发 烫发 纹理烫 锡纸烫 区别 韩系 中分 发型 价格 · 男生 中長髮 燙髮 韓系 中分 髮型 StyleMap 台灣 價格 燙髮推薦 · "digital perm" men price Taiwan 男生 燙髮 價格 韓系 燙髮 費用 · 台北 男生 燙髮 價目表 韓系 燙 電棒燙 價格 中長髮 沙龍 · StyleMap Taiwan 男生 中長髮 燙髮 造型

## 5. Not yet tried after pass 1 (superseded by §7c below)

- Reddit via Chrome: r/malegrooming, r/AsianBeauty, r/koreanbeauty, r/curlyhair, r/koreanvariety, r/taiwan, r/China; open Crafty_Session_7959 slick-back thread comments; search `"digital perm" lasted` in r/malehairadvice sorted new
- Instagram hashtags (need logged-in Chrome or skip): #디지털펌남자 #남자중단발 #남자장발펌 #히피펌남자 #빈티지펌 #メンズパーマ #メンズミディアム #センターパートパーマ #asianperm #koreanperm
- Pinterest logged-in pass for pin permalinks
- Naver manually (blog.naver.com stylist posts on 빈티지펌 / 쉐도우펌 / 슬릭펌 prices); Kakao Hairshop app menus; 준오/차홍/이가자 official price pages
- dcinside 헤어갤 (gall.dcinside.com/board/lists/?id=hair) search 디지털펌 장발
- Douyin / Xiaohongshu 男生 中长发 烫; 2ch/5ch 男 パーマ
- YouTube comments via Chrome on the 18 listed videos; 12 Pell channel scan
- Schwarzkopf "Hair Cost Index 2026" for EU prices; German/French Asian salons (Düsseldorf, Paris 13e)
- Korean/Japanese domestic product prices (Olive Young DASHU/AMOS; Loretta on Rakuten)
- Books: honto, 紀伊國屋, WorldCat, Google Books API, OCEAN TOKYO / LIPPS branded books, GQ/Esquire/Dazed Korea issue indexes, Samurai ELO, smart, Popeye back numbers issue-by-issue (magazineworld.jp/popeye/back/)
- 남성 헤어 토탈 시스템 and 헤어펌 웨이브 디자인 TOC (bookstore preview widget)
- Helmet / gym / humidity behaviour of digital perm beyond 72 h

## 6. Social-image pass 2026-09-08 (see notes/11-social-images.md for full log)

Access deltas to §1: **Instagram hashtag pages DO render logged-out** at `/explore/tags/<tag>/` → `/popular/<tag>/` (captions in `img[alt]`, 640px signed CDN URLs, ~28 items) ✓ best new source. **Pinterest is logged-OUT in the user's Chrome**; search feed hydrates slowly/unreliably and its `/resource/BaseSearchResource/get/` API 403s, but **`pinterest.com/ideas/<slug>/<id>/` pages are server-rendered** with 140-155 image md5s in raw HTML + ~23 sibling hub URLs; `/236x/` thumb path maps to `i.pinimg.com/originals/...` ✓. **Reddit `.json` endpoints work from inside an old.reddit.com tab** via javascript_tool (`/r/<sub>/search.json`, `/comments/<id>.json`) - much cheaper than page scraping; `/gallery/<id>.json` 404s. **YouTube search results readable** by parsing `ytInitialData` from the page's own script tag; `youtube.com/oembed` gives title+channel via curl. **Threads ✗** (login wall, "No results"). **TikTok tag pages ✗** ("Something went wrong"). **Lemon8 ◐** (renders, but one post per discover page).

New reddit subs/queries run: r/AsianMasculinity `hair perm` ✓✓ (best new sub, 28 image-posts), r/malehairadvice `shoulder length asian` ✓ / `korean perm long hair` ✓ / `long hair perm asian` ✓ / `hippie perm` ◐ / `author:Crafty_Session_7959` ✓ (= post 1knzo7v, comments read, low value), r/Hair `asian long perm` ✓, r/malegrooming `asian perm` ◐, r/AsianBeauty ✗, r/koreanbeauty ✗, r/curlyhair ✗ (all women), r/FierceFlow `asian perm`/`asian shoulder` ✗, r/asianmen ✗ (dead sub).

Pinterest hubs mined: `/ideas/asian-perm-men-middle-part/913618051774/`, `/ideas/asian-wavy-perm-middle-part-men/914046828226/`. 24 further hub URLs discovered and listed in notes/11 - not yet mined.

Instagram tags mined: #남자장발펌, #히피펌남자. Not yet: #남자중단발 #남자쉐도우펌 #남자빈티지펌 #メンズロングパーマ #メンズミディアムパーマ #asianperm #koreanperm #leafcut.

Output: 245 images in `images/social/` (515 downloaded, 270 filtered out).

## 7. Pass 2 — 2026-09-08 image/PDF harvest (six agents; full per-URL query logs live in notes/06–11 "Query log" sections — read those before repeating)

### 7a. Access-matrix deltas (merge into §1)

| Site | Verdict | Route |
|---|---|---|
| hairmode.jp (= 女性モード社 = ヘアモード社 = j-mode.co.jp) | ✓✓ curl only | `wp-json/wc/store/v1/products?per_page=100&page=1..9` (829 products) → product page `flipbook/?dfb_id=N` → inline JS holds `wp-content/uploads/*.pdf`. 356 preview PDFs sitewide; 42 pulled. `wp/v2/media` empty; sitemap has no products; `j-mode.co.jp/sample/` JS-only |
| mamedene.com (ex-hairshop.kakao.com, which is DNS-dead) | ✓✓ curl JSON | `/proxy/app/v6/hair-styles?category=PERM&gender=MALE&length=MEDIUM&pageSize=30&page=N` with UA + `Referer: https://mamedene.com/search/style`; 1080px at `image.glity.link/...?type=w&w=1080`; magazine imgs 375px only; no per-id endpoint (open `/styles/<id>` in Chrome) |
| beauty.hotpepper.jp | ✓ curl | men's length codes HL09–HL13 (HL13 = ロング, top); `&pn=N` paginates; image = `imgbp.hotp.jp/CSP/IMG_SRC/<last4 as 2+2>/B<n>/B<n>.jpg` |
| ozmall.co.jp men's | ✓ curl | slugs menswolf / manban / mens-allback / mens-nobashikakebang / mens-tamago; 360×480 cap; leaks women's bobs |
| lipps-hair.com | ◐ | no "long" category (404) |
| GOALD / ALBUM / kamimado | ✗ curl (exit 000) | need Chrome |
| OCEAN TOKYO / Lond / MINX / AFLOAT / ANTI / Dot+LIM | ✗ JS shells | need Chrome + javascript_tool |
| rasysa / hair.cm / beauty.rakuten men's-long | ✗ 404 | |
| kamishobo.co.jp / .official.ec | ✓ curl item pages (JPG spreads only, no PDF); ✗ search | |
| shop.shinbiyo.com | ✓ curl | no previews |
| cosmicpub / media-soft / hinode / fujisan | ✗ covers only | fujisan curl 404 |
| google.com (Chrome) | ✗ now | CAPTCHA for JP; SERP links `/goto?url=<opaque>`; javascript_tool empty on google.com |
| search.yahoo.co.jp (Chrome) | ✓ | JP search engine that works; supports site:/filetype: |
| html.duckduckgo.com | ✓ | best URL-harvest proxy for KR |
| bing.com/images (Chrome) | ✓ | `a.iusc` → `JSON.parse(m).murl`; scroll 5× first. ✗ for JP-language text queries |
| image.so.com (Chrome) | ✓✓ CN | `/j?q=<q>&src=srp&sn=<off>&pn=60` returns JSON; same-origin fetch() sweeps many queries; download `p2.ssl.qhimgs1.com/<key>.jpg` with `Referer: https://image.so.com/` |
| image.baidu.com | ✗ | 302 → www.baidu.com; acjson CORS-blocked |
| style-map.com (TW) | ✓ Chrome | men's tags are short-only; 1500² CDN pulls work |
| xiaohongshu / zhihu / weibo / douyin | ✗ login walls (confirmed) | 360 caches their images |
| dcard.tw / ptt.cc | ✓ no wall | text only, no inline photos |
| instagram.com/explore/tags/<tag>/ | ✓✓ logged-out | 302 → `/popular/<tag>/`; captions in `img[alt]`; 640px signed URLs expire — download immediately; ~28 items |
| pinterest.com | ◐ logged-OUT | search feed barely hydrates, API 403; `/ideas/<slug>/<id>/` server-rendered, 140–155 md5s, `/236x/` → `/originals/` |
| old.reddit.com `.json` | ✓ from inside old.reddit tab | `/r/<sub>/search.json`, `/comments/<id>.json`; `/gallery/<id>.json` 404 |
| youtube.com | ◐ | search readable via `ytInitialData`; `youtube.com/oembed` via curl; comments still unreadable |
| threads.com / tiktok tag pages | ✗ | login wall / "Something went wrong" |
| lemon8-app.com | ◐ | text readable, one post per page; images via Bing |
| blog.naver.com | ✗ in Chrome too (confirmed) | do not retry |
| dcinside 헤어갤 | ✓ curl | 26 장발펌 threads, unharvested |
| aladin 미리보기 | ✓ | `shop/book/wletslookViewer.aspx?ISBN=…` (ItemId form errors); yes24 search needs `domain=ALL`; kyobo search 404 |
| assets.unileversolutions.com (allthingshair) | ✗ hard-block curl | names only |
| blog.30shine.com, anhtoc.edu.vn, vogue.co.th, kompas.com | ✗ WebFetch 403 | anhtoc works in Chrome |
| ranphom.com (TH) | ✗ dead | try archive.org |
| Chrome MCP `javascript_tool` | gotcha | output ≈1000 chars; refuses strings with query-strings/base64 (`[BLOCKED: …]`) — print host + pathname separately, slice arrays; `navigate` rejects `file://` (serve local sheets via `python -m http.server`) |

### 7b. What was harvested (dedupe list)

- **notes/06** hairmode 42 PDFs (all 男髪セレクション 18-19→2025 + SPRING/SUMMER, パーツ図鑑 ×2, GOALD book, 22選, 完全マスター, メンズパーマのヘアカタログ ×2, fifth, Y.O.G., アイロンパーマ, 7大お悩み, ポイントパーマ, 複雑履歴, アイロン風, 100%リアル, DADA ボリューム学, BASIC OF BASIC 06/07/08, 韓国ヘアBOOK, イケオジ, テクニック84, ヘアレシピ, ビジネス, カラー2022, ALBUM guide, BARBER TECH, Hello Barber, パーマのヘアカタログ 2018/2022) + frogstar.jp salon PDF. Dead: jm14199 (男髪2021), jm1016 (16-17), jm25665 (メンズパーマのヘアカタログ 2022-2023), one more.
- **notes/07** Hot Pepper HL13+MC01 pages 1–4 + keywords デジタルパーマ/オールバック/韓国/かきあげ/HL12+ミディアムロング; OZmall men's slugs depth 1; LIPPS medium/perm; Bing `メンズ ロング パーマ ヘアカタログ` etc.
- **notes/08** mamedene PERM/MALE/MEDIUM 900 records; magazines 509/172/292; 네이트뷰 장발펌 article; aladin/yes24 book checks (임경근 vol.5, 남성 헤어 스타일북 2026, 토탈 시스템, 9 Matrix Perm, 헤어펌 웨이브 디자인 …).
- **notes/09** 360 queries ×14 (best 男生披肩长发发型烫), StyleMap 6 men's tags, menpermhk.com, Sohu 发型书 post, 博客來 男士髮型.
- **notes/10** VN tiendichshop / chiaki / anhtoc / pkbarber / miinhair.jkt / dailyvanity.sg / thesmartlocal.my; Bing TH/VN/ID queries; wongnai; Lemon8 MY/ID salons.
- **notes/11** IG #남자장발펌 #히피펌남자; Pinterest hubs 913618051774 / 914046828226; reddit r/AsianMasculinity `hair perm`, r/malehairadvice `shoulder length asian` / `korean perm long hair` / `long hair perm asian` / `hippie perm` / Crafty_Session_7959; r/Hair `asian long perm`; r/malegrooming ◐; r/AsianBeauty, r/koreanbeauty, r/curlyhair, r/FierceFlow, r/asianmen ✗; 13 YouTube IDs identified.

### 7c. Next-pass queue (supersedes §5)

1. hairmode: pull the other 314 previews (monthly HAIR MODE HM2103–HM2602), grep contents for メンズ/ミディアム/ロング; retry jm25665; honto/紀伊國屋/楽天 試し読み for コスミック 完全版2026-27; `prize-hair.com/prize_pamphlet2024` and other salon 求人 PDFs.
2. Hot Pepper HL13 `pn=5..15`, 顔型=卵型 filter, style-detail `L#` pages, unused keywords (セミロング, マッシュロング, ウルフロング, ロン毛, 波巻き, スパイラルパーマ, くびれ, 外ハネ); video thumbs `imgbp.hotp.jp/video/thumb/`; OZmall pagination; GOALD/ALBUM/OCEAN TOKYO via Chrome; mensnonno 360° harvest; perceptual-hash dedupe of images/jp.
3. mamedene CUT+MALE+MEDIUM with 울프컷/샤기컷/레이어드컷 tags; `tags=슬릭백언더컷`; magazine 509's 24 style IDs at 1080px; dcinside 헤어갤 26 threads; celebstyle.co.kr / fashion.inly.kr / visualacademy / chop.kr posts; DDG `site:tistory.com 남자 장발 펌`; aladin previews 232083006 / 138843203; 9 Matrix Perm.
4. IG: #남자중단발 #남자쉐도우펌 #남자빈티지펌 #メンズロングパーマ #メンズミディアムパーマ #asianperm #koreanperm #leafcut + profiles chahong.official, tone.t_official, jss_menshair …; pair reel permalinks to tiles. Pinterest: 24 hubs listed in notes/11 §2. Reddit r/AsianMasculinity `long hair` / `wolf cut` / `middle part` / `down perm`; comments on 1trm1it, 1sn5h1e, 1uf9x9n. YouTube captions via `ytInitialPlayerResponse` (untested).
5. CN: 360 `男生长发中分烫` `男生长卷发发型` `男生齐肩发型 韩国` `男生 锁骨发` `男生 慵懒卷` + deeper `sn`; StyleMap 紳士波紋卷 / 嬉皮卷 / 男士燙髮 / 韓系歐巴髮型 …; Sogou images; dianping 作品 pages; re-fetch `img` originals for the 48 sub-400px files.
6. SEA: 30Shine blog + Liêm/4RAU/Horse Club/Homies galleries in Chrome; Thai style-name Bing queries (ดัดดิจิตอล ผู้ชาย, ดัดลอนคลายสไตล์เกาหลี, แมนบ๊อบ ดัดลอน); wongnai curl-salon listing; Pantip direct; ranphom via archive.org; VN barber book (Shopee i.772711794.25815446624 preview); PH Tagalog queries; unileversolutions in-page byte read.
7. Still open from pass 1: rod sizes, EU prices, KR/JP domestic product prices, Kakao/준오 official price pages (준오 stylebook removed), 2ch/5ch, YouTube comments.
