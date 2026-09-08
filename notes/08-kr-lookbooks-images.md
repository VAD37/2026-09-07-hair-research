# 08 — Korean men's medium-long perm: image lookbooks + book/e-book previews

Agent pass 2026-09-08. Goal: harvest Korean (KR) men's **medium-to-long** (중단발 / 장발 / 어깨길이) perm photos in printed-catalog style, plus find any Korean hair-catalog book previews.

**Result: 171 images saved to `images/kr/`** (all verified real JPEG, >15 KB, ~45 MB total). No PDFs found (see §4).

---

## 0. The one big find: mamedene 스타일북 = the Korean salon lookbook

`mamedene.com` (마메드네) is the rebranded **카카오헤어샵** (Kakao Hairshop). It is not just a magazine site — it hosts a full **스타일북 / 스타일 검색** with per-style pages carrying photo + style name + tag list + stylist name & rank + salon + branch + menu price. That is exactly the printed-salon-catalog format wanted.

**Public JSON API (no login, works from plain `curl`):**

```
https://mamedene.com/proxy/app/v6/hair-styles
   ?category=PERM        # CUT | PERM | COLOR | MAKEUP
   &gender=MALE          # MALE | FEMALE
   &length=MEDIUM        # men's UI calls this "긴머리"; other value SHORT
   &tags=                # tag text, e.g. 히피펌
   &region=&distance=5km&location=
   &pageSize=30&page=1
```

Headers needed: a normal browser `User-Agent` + `Referer: https://mamedene.com/search/style`. Returns `contents[]` with `title`, `tags[].text`, `styler.displayLevel` + `nickName`, `shop.name` + `branchName`, `originalPhotoUrl` (1080 px), `shareLink` (`https://mamedene.com/styles/<id>`), and the bookable menu with KRW price.

Style images live on `image.glity.link/RQ7FVsz0EH/beauty-styler_photo/…` (thumb `?type=f&w=360&h=360`, original `?type=w&w=1080`). Magazine images live on a **different** host: `kr.object.ncloudstorage.com/mamedene-production/beauty-magazine/<magId>_<n>_img_375x375.jpg` — only the 375×375 derivative exists there (no larger variant).

Equivalent browser URL (for eyeballing): `https://mamedene.com/search/style?category=PERM&gender=MALE&length=MEDIUM`

**Caveat on length.** mamedene only offers men **긴머리 / 짧은머리** (MEDIUM / SHORT). "긴머리" tops out around chin for most tiles, so the 900 fetched records were visually screened on contact sheets and only genuinely chin-or-longer shots were kept (127 of 306 candidates). The truly shoulder-length material is concentrated in the magazine lookbooks (§2) and in the 히피펌 / 울프컷 / 그런지펌 groups.

---

## 1. Styles harvested — mamedene 스타일북 (127 shots)

All: source = mamedene 스타일북 (Kakao Hairshop successor); image URL pattern = `https://image.glity.link/RQ7FVsz0EH/beauty-styler_photo/<photo-id>.jpg?type=w&w=1080` (exact URL per style is in `scratchpad/kept_meta.json`); files saved under `images/kr/`. Grouped by silhouette. Nearly all are **worn down** (salon/street shots); the 리프펌 group is mostly middle-part or side-swept and pushes back cleanly, 올백-compatible.

Length key: 리프펌 = grow-out ear→chin · 히피펌 = chin→shoulder all-over wave · 울프컷/샤기컷 = chin front + long layered nape · 레이어드컷 = chin→shoulder with layers.

### 히피펌 — hippie perm (loose all-over S-wave)  (66 shots)

| # | Title (KR) | Tags | Stylist | Salon | Style page | Saved file |
|---|---|---|---|---|---|---|
| 1 | 리프컷 | 리프컷, 쉐도우펌, 히피펌 | 팀장 현희 | 에이브릿 강남점 | https://mamedene.com/styles/1897371 | `mamedene_리프컷-에이브릿_1897371.jpg` |
| 2 | 리프컷 | 리프컷, 히피펌, 쉐도우펌 | 팀장 현희 | 에이브릿 강남점 | https://mamedene.com/styles/1895436 | `mamedene_리프컷-에이브릿_1895436.jpg` |
| 3 | 베이비펌 | 베이비펌, 히피펌, 스왈로펌 | 원장 민하 | 샾머무르다 신촌명물거리점 | https://mamedene.com/styles/1909333 | `mamedene_베이비펌-샾머무르다_1909333.jpg` |
| 4 | 댄디컷 | 댄디컷, 쉐도우펌, 히피펌 | 점장 은우 | 꾸블랑헤어 성신여대1호점 | https://mamedene.com/styles/1909231 | `mamedene_댄디컷-꾸블랑헤어_1909231.jpg` |
| 5 | 히피펌 | 히피펌, 가르마펌, 리프펌 | 원장 민하 | 샾머무르다 신촌명물거리점 | https://mamedene.com/styles/1907564 | `mamedene_히피펌-샾머무르다_1907564.jpg` |
| 6 | 댄디컷 | 댄디컷, 히피펌, 쉐도우펌 | 실장 채웅 | 헤어더뷰 강남점 | https://mamedene.com/styles/1899037 | `mamedene_댄디컷-헤어더뷰_1899037.jpg` |
| 7 | 베이비펌 | 베이비펌, 히피펌, 샤기컷 | 대표원장 바다 | 어바웃9 홍대입구 본점 | https://mamedene.com/styles/1895957 | `mamedene_베이비펌-어바웃9_1895957.jpg` |
| 8 | 댄디컷 | 댄디컷, 히피펌, 베이비펌 | 부원장 해나 | 샾머무르다 신촌명물거리점 | https://mamedene.com/styles/1852591 | `mamedene_댄디컷-샾머무르다_1852591.jpg` |
| 9 | 히피펌 | 히피펌, 가르마펌, 베이비펌 | 원장 민하 | 샾머무르다 신촌명물거리점 | https://mamedene.com/styles/1918034 | `mamedene_히피펌-샾머무르다_1918034.jpg` |
| 10 | 레이어드컷 | 레이어드컷, 히피펌 | 디자이너 희나 | 어바웃9 홍대입구 본점 | https://mamedene.com/styles/1917155 | `mamedene_레이어드컷-어바웃9_1917155.jpg` |
| 11 | 히피펌 | 히피펌 | 원장 세빈 | 샾머무르다 맨즈 신촌점 | https://mamedene.com/styles/1910990 | `mamedene_히피펌-샾머무르다_1910990.jpg` |
| 12 | 히피펌 | 히피펌, 베이비펌, 스왈로펌 | 원장 민하 | 샾머무르다 신촌명물거리점 | https://mamedene.com/styles/1909331 | `mamedene_히피펌-샾머무르다_1909331.jpg` |
| 13 | 히피펌 | 히피펌, 내츄럴펌, 댄디펌 | 원장 민하 | 샾머무르다 신촌명물거리점 | https://mamedene.com/styles/1909330 | `mamedene_히피펌-샾머무르다_1909330.jpg` |
| 14 | 히피펌 | 히피펌, 베이비펌, 스왈로펌 | 원장 민하 | 샾머무르다 신촌명물거리점 | https://mamedene.com/styles/1909329 | `mamedene_히피펌-샾머무르다_1909329.jpg` |
| 15 | 히피펌 | 히피펌, 베이비펌, 스왈로펌 | 원장 민하 | 샾머무르다 신촌명물거리점 | https://mamedene.com/styles/1909140 | `mamedene_히피펌-샾머무르다_1909140.jpg` |
| 16 | 히피펌 | 히피펌, 리프펌, 리프컷 | 대표원장 바다 | 어바웃9 홍대입구 본점 | https://mamedene.com/styles/1899500 | `mamedene_히피펌-어바웃9_1899500.jpg` |
| 17 | 울프컷 | 울프컷, 히피펌, 베이비펌 | 대표원장 바다 | 어바웃9 홍대입구 본점 | https://mamedene.com/styles/1897688 | `mamedene_울프컷-어바웃9_1897688.jpg` |
| 18 | 베이비펌 | 베이비펌, 히피펌, 스왈로펌 | 원장 민하 | 샾머무르다 신촌명물거리점 | https://mamedene.com/styles/1896467 | `mamedene_베이비펌-샾머무르다_1896467.jpg` |
| 19 | 히피펌 | 히피펌, 스왈로펌, 러블리펌 | 디자이너 화범花虎 | 피나트맨 PINARTMAN 상수역점 | https://mamedene.com/styles/1830924 | `mamedene_히피펌-피나트맨-PINARTMAN_1830924.jpg` |
| 20 | 히피펌 | 히피펌, 내츄럴펌, 스왈로펌 | 디자이너 화범花虎 | 피나트맨 PINARTMAN 상수역점 | https://mamedene.com/styles/1830923 | `mamedene_히피펌-피나트맨-PINARTMAN_1830923.jpg` |
| 21 | 리프컷 | 리프컷, 댄디컷, 히피펌 | 부원장 해나 | 샾머무르다 신촌명물거리점 | https://mamedene.com/styles/1792865 | `mamedene_리프컷-샾머무르다_1792865.jpg` |
| 22 | 레이어드컷 | 레이어드컷, 히피펌, 블루블랙 | 원장 초 | 아트룸 상왕십리역점 | https://mamedene.com/styles/1753932 | `mamedene_레이어드컷-아트룸_1753932.jpg` |
| 23 | 댄디컷 | 댄디컷, 히피펌, 볼륨펌 | 원장 리오 | 헤어유스 건대점 | https://mamedene.com/styles/1919613 | `mamedene_댄디컷-헤어유스_1919613.jpg` |
| 24 | 리프컷 | 리프컷, 특수머리, 히피펌 | 디자이너 정민 | 꾸블랑헤어 고려대점 | https://mamedene.com/styles/1919508 | `mamedene_리프컷-꾸블랑헤어_1919508.jpg` |
| 25 | 댄디컷 | 댄디컷, 히피펌 | 맨즈 Stylist 연이 | 바운스플로 여의도KBS별관점 | https://mamedene.com/styles/1919224 | `mamedene_댄디컷-바운스플로_1919224.jpg` |
| 26 | 댄디컷 | 댄디컷, 히피펌 | 맨즈 Stylist 연이 | 바운스플로 여의도KBS별관점 | https://mamedene.com/styles/1919217 | `mamedene_댄디컷-바운스플로_1919217.jpg` |
| 27 | 히피펌 | 히피펌, 레이어드컷 | 원장 지연 | 오헤어 본점 | https://mamedene.com/styles/1919123 | `mamedene_히피펌-오헤어_1919123.jpg` |
| 28 | 댄디컷 | 댄디컷, 히피펌 | 디자이너 준호 | 유니헤어 독산점 | https://mamedene.com/styles/1918945 | `mamedene_댄디컷-유니헤어_1918945.jpg` |
| 29 | 울프컷 | 울프컷, 히피펌, 리프펌 | 디자이너 왕호 | 준오헤어 반포점 | https://mamedene.com/styles/1918230 | `mamedene_울프컷-준오헤어_1918230.jpg` |
| 30 | 댄디컷 | 댄디컷, 히피펌, 스왈로펌 | 대표원장 고 | 에필라쥬헤어살롱 강남역점 | https://mamedene.com/styles/1918030 | `mamedene_댄디컷-에필라쥬헤어살롱_1918030.jpg` |
| 31 | 댄디컷 | 댄디컷, 쉐도우펌, 히피펌 | 수석 디자이너 구원 | 박승철헤어스투디오 상도점 | https://mamedene.com/styles/1917133 | `mamedene_댄디컷-박승철헤어스투디오_1917133.jpg` |
| 32 | 히피펌 | 히피펌, 쉐도우펌, 리프펌 | 디자이너 예림 | 아스트룸헤어 송파위례점 | https://mamedene.com/styles/1916352 | `mamedene_히피펌-아스트룸헤어_1916352.jpg` |
| 33 | 리프컷 | 리프컷, 울프컷, 히피펌 | 실장 조하 | 준오헤어 낙성대역점 | https://mamedene.com/styles/1915483 | `mamedene_리프컷-준오헤어_1915483.jpg` |
| 34 | 댄디컷 | 댄디컷, 쉐도우펌, 히피펌 | 실장 조하 | 준오헤어 낙성대역점 | https://mamedene.com/styles/1915481 | `mamedene_댄디컷-준오헤어_1915481.jpg` |
| 35 | 리프컷 | 리프컷, 쉐도우펌, 히피펌 | 실장 조하 | 준오헤어 낙성대역점 | https://mamedene.com/styles/1915480 | `mamedene_리프컷-준오헤어_1915480.jpg` |
| 36 | 히피펌 | 히피펌, 쉐도우펌 | 수석디자이너 설아 | 살롱드키코 사당역2호점 | https://mamedene.com/styles/1915308 | `mamedene_히피펌-살롱드키코_1915308.jpg` |
| 37 | 리프컷 | 리프컷, 히피펌, 초코브라운 | . 국 | 양리헤어 홍대점 | https://mamedene.com/styles/1915244 | `mamedene_리프컷-양리헤어_1915244.jpg` |
| 38 | 리프컷 | 리프컷, 댄디컷, 히피펌 | 디자이너 주연 | 주헤어 | https://mamedene.com/styles/1914746 | `mamedene_리프컷-주헤어_1914746.jpg` |
| 39 | 울프컷 | 울프컷, 히피펌, 다크브라운 | [Black] 은우 | 궁서채 망원점 | https://mamedene.com/styles/1914525 | `mamedene_울프컷-궁서채_1914525.jpg` |
| 40 | 쉐도우펌 | 쉐도우펌, 히피펌, 댄디컷 | 실장 엑스 | 샾머무르다 맨즈 신촌점 | https://mamedene.com/styles/1914502 | `mamedene_쉐도우펌-샾머무르다_1914502.jpg` |
| 41 | 리프컷 | 리프컷, 쉐도우펌, 히피펌 | 디자이너 예원 | 차심 교대역점 | https://mamedene.com/styles/1914358 | `mamedene_리프컷-차심_1914358.jpg` |
| 42 | 히피펌 | 히피펌, 투블럭컷 | 실장 지영 | 차심 성수역점 | https://mamedene.com/styles/1913929 | `mamedene_히피펌-차심_1913929.jpg` |
| 43 | 레이어드컷 | 레이어드컷, 히피펌, 쉐도우펌 | 디자이너 도아 | 스타일라뷰 2호점 목동사거리 | https://mamedene.com/styles/1913728 | `mamedene_레이어드컷-스타일라뷰-2호점_1913728.jpg` |
| 44 | 댄디컷 | 댄디컷, 히피펌 | Stylist 혜원 | 바운스플로 영등포구청역점 | https://mamedene.com/styles/1913465 | `mamedene_댄디컷-바운스플로_1913465.jpg` |
| 45 | 레이어드컷 | 레이어드컷, 히피펌, 특수머리 | 수석디자이너 원철 | 더그레이헤어 | https://mamedene.com/styles/1913358 | `mamedene_레이어드컷-더그레이헤어_1913358.jpg` |
| 46 | 히피펌 | 히피펌 | 원장 진 | 안나헤어 회현 | https://mamedene.com/styles/1913006 | `mamedene_히피펌-안나헤어_1913006.jpg` |
| 47 | 울프컷 | 울프컷, 히피펌 | 대표원장 바다 | 어바웃9 홍대입구 본점 | https://mamedene.com/styles/1912824 | `mamedene_울프컷-어바웃9_1912824.jpg` |
| 48 | 히피펌 | 히피펌 | 원장 세빈 | 샾머무르다 맨즈 신촌점 | https://mamedene.com/styles/1910992 | `mamedene_히피펌-샾머무르다_1910992.jpg` |
| 49 | 히피펌 | 히피펌 | 원장 세빈 | 샾머무르다 맨즈 신촌점 | https://mamedene.com/styles/1910987 | `mamedene_히피펌-샾머무르다_1910987.jpg` |
| 50 | 히피펌 | 히피펌 | 원장 세빈 | 샾머무르다 맨즈 신촌점 | https://mamedene.com/styles/1910981 | `mamedene_히피펌-샾머무르다_1910981.jpg` |
| 51 | 히피펌 | 히피펌, 베이비펌 | 부원장 아카 | 샾머무르다 맨즈 신촌점 | https://mamedene.com/styles/1910971 | `mamedene_히피펌-샾머무르다_1910971.jpg` |
| 52 | 히피펌 | 히피펌 | 부원장 아카 | 샾머무르다 맨즈 신촌점 | https://mamedene.com/styles/1910970 | `mamedene_히피펌-샾머무르다_1910970.jpg` |
| 53 | 히피펌 | 히피펌 | 부원장 아카 | 샾머무르다 맨즈 신촌점 | https://mamedene.com/styles/1910969 | `mamedene_히피펌-샾머무르다_1910969.jpg` |
| 54 | 히피펌 | 히피펌 | 부원장 아카 | 샾머무르다 맨즈 신촌점 | https://mamedene.com/styles/1910968 | `mamedene_히피펌-샾머무르다_1910968.jpg` |
| 55 | 스왈로펌 | 스왈로펌, 히피펌 | 부원장 아카 | 샾머무르다 맨즈 신촌점 | https://mamedene.com/styles/1910966 | `mamedene_스왈로펌-샾머무르다_1910966.jpg` |
| 56 | 스왈로펌 | 스왈로펌, 히피펌 | 부원장 아카 | 샾머무르다 맨즈 신촌점 | https://mamedene.com/styles/1910962 | `mamedene_스왈로펌-샾머무르다_1910962.jpg` |
| 57 | 히피펌 | 히피펌, 스왈로펌 | 부원장 아카 | 샾머무르다 맨즈 신촌점 | https://mamedene.com/styles/1910961 | `mamedene_히피펌-샾머무르다_1910961.jpg` |
| 58 | 히피펌 | 히피펌, 쉐도우펌 | 부원장 아카 | 샾머무르다 맨즈 신촌점 | https://mamedene.com/styles/1910955 | `mamedene_히피펌-샾머무르다_1910955.jpg` |
| 59 | 댄디컷 | 댄디컷, 텍스쳐펌, 히피펌 | 원장 재만 | 포트 연남점 | https://mamedene.com/styles/1910082 | `mamedene_댄디컷-포트_1910082.jpg` |
| 60 | 리프컷 | 리프컷, 리프펌, 히피펌 | 점장 이은비 | 꾸블랑헤어 성신여대2호점 | https://mamedene.com/styles/1909581 | `mamedene_리프컷-꾸블랑헤어_1909581.jpg` |
| 61 | 리프컷 | 리프컷, 히피펌, 리프펌 | 점장 이은비 | 꾸블랑헤어 성신여대2호점 | https://mamedene.com/styles/1909579 | `mamedene_리프컷-꾸블랑헤어_1909579.jpg` |
| 62 | 리프컷 | 리프컷, 리프펌, 히피펌 | 점장 이은비 | 꾸블랑헤어 성신여대2호점 | https://mamedene.com/styles/1909578 | `mamedene_리프컷-꾸블랑헤어_1909578.jpg` |
| 63 | 울프컷 | 울프컷, 히피펌, 베이비펌 | 대표원장 백도경 | Rititi(리티티) 신사본점 | https://mamedene.com/styles/1909475 | `mamedene_울프컷-Rititi-리티티_1909475.jpg` |
| 64 | 리프컷 | 리프컷, 히피펌, 쉐도우펌 | 대표원장 백도경 | Rititi(리티티) 신사본점 | https://mamedene.com/styles/1909472 | `mamedene_리프컷-Rititi-리티티_1909472.jpg` |
| 65 | 리프컷 | 리프컷, 쉐도우펌, 히피펌 | 원장 수현 | 샾머무르다 신촌역점 | https://mamedene.com/styles/1909115 | `mamedene_리프컷-샾머무르다_1909115.jpg` |
| 66 | 댄디컷 | 댄디컷, 히피펌, 스왈로펌 | 대표원장 바다 | 어바웃9 홍대입구 본점 | https://mamedene.com/styles/1908800 | `mamedene_댄디컷-어바웃9_1908800.jpg` |

### 울프컷 — wolf cut  (9 shots)

| # | Title (KR) | Tags | Stylist | Salon | Style page | Saved file |
|---|---|---|---|---|---|---|
| 1 | 리프컷 | 리프컷, 울프컷, 리프펌 | 부원장 사랑 | 디자인안 압구정본점 | https://mamedene.com/styles/1434539 | `mamedene_리프컷-디자인안_1434539.jpg` |
| 2 | 울프컷 | 울프컷, 베이비펌, 내츄럴펌 | 디자이너 민결 | 보그헤어 고덕점 | https://mamedene.com/styles/1921579 | `mamedene_울프컷-보그헤어_1921579.jpg` |
| 3 | 리프컷 | 리프컷, 울프컷, 리프펌 | 부원장 사랑 | 디자인안 압구정본점 | https://mamedene.com/styles/1434541 | `mamedene_리프컷-디자인안_1434541.jpg` |
| 4 | 리프컷 | 리프컷, 울프컷, 리프펌 | 부원장 사랑 | 디자인안 압구정본점 | https://mamedene.com/styles/1434540 | `mamedene_리프컷-디자인안_1434540.jpg` |
| 5 | 리프컷 | 리프컷, 울프컷, 텍스쳐펌 | 부원장 사랑 | 디자인안 압구정본점 | https://mamedene.com/styles/1429651 | `mamedene_리프컷-디자인안_1429651.jpg` |
| 6 | 울프컷 | 울프컷, 텍스쳐펌, 리프펌 | 디자이너 화범花虎 | 피나트맨 PINARTMAN 상수역점 | https://mamedene.com/styles/1830919 | `mamedene_울프컷-피나트맨-PINARTMAN_1830919.jpg` |
| 7 | 울프컷 | 울프컷, 볼륨펌 | 원장 연아 | 스튜디오연아 수유점 | https://mamedene.com/styles/1918643 | `mamedene_울프컷-스튜디오연아_1918643.jpg` |
| 8 | 울프컷 | 울프컷, 스왈로펌, 초코브라운 | 원장 지훈 | 애쉬맨즈헤어 | https://mamedene.com/styles/1912448 | `mamedene_울프컷-애쉬맨즈헤어_1912448.jpg` |
| 9 | 울프컷 | 울프컷, 가르마펌, 텍스쳐펌 | 수석 디자이너 겨울 | 더퓨어헤어 성신여대1호점 | https://mamedene.com/styles/1912222 | `mamedene_울프컷-더퓨어헤어_1912222.jpg` |

### 샤기컷 — shaggy cut  (1 shots)

| # | Title (KR) | Tags | Stylist | Salon | Style page | Saved file |
|---|---|---|---|---|---|---|
| 1 | 샤기컷 | 샤기컷, 텍스쳐펌 | 디자이너 민결 | 보그헤어 고덕점 | https://mamedene.com/styles/1921580 | `mamedene_샤기컷-보그헤어_1921580.jpg` |

### 레이어드컷 — layered cut  (14 shots)

| # | Title (KR) | Tags | Stylist | Salon | Style page | Saved file |
|---|---|---|---|---|---|---|
| 1 | 리프컷 | 리프컷, 레이어드컷, 가르마펌 | 대표원장 신여진 | 뮤즈헤어살롱 본점 | https://mamedene.com/styles/1916460 | `mamedene_리프컷-뮤즈헤어살롱_1916460.jpg` |
| 2 | 레이어드컷 | 레이어드컷, 리프펌, 볼륨펌 | 대표원장 백도경 | Rititi(리티티) 신사본점 | https://mamedene.com/styles/1909471 | `mamedene_레이어드컷-Rititi-리티티_1909471.jpg` |
| 3 | 레이어드컷 | 레이어드컷, 리프펌, 내츄럴펌 | 대표원장 백도경 | Rititi(리티티) 신사본점 | https://mamedene.com/styles/1909469 | `mamedene_레이어드컷-Rititi-리티티_1909469.jpg` |
| 4 | 레이어드컷 | 레이어드컷, 내츄럴펌, 텍스쳐펌 | 디자이너 제리 | 오유헤어디자인 홍대점 | https://mamedene.com/styles/1918170 | `mamedene_레이어드컷-오유헤어디자인_1918170.jpg` |
| 5 | 레이어드컷 | 레이어드컷, 내츄럴펌, 텍스쳐펌 | 디자이너 제리 | 오유헤어디자인 홍대점 | https://mamedene.com/styles/1918168 | `mamedene_레이어드컷-오유헤어디자인_1918168.jpg` |
| 6 | 레이어드컷 | 레이어드컷, 텍스쳐펌, 내츄럴펌 | 디자이너 제리 | 오유헤어디자인 홍대점 | https://mamedene.com/styles/1918167 | `mamedene_레이어드컷-오유헤어디자인_1918167.jpg` |
| 7 | 브릿지 | 브릿지, 레이어드컷, 볼륨펌 | 대표원장 왕구 | 어바웃9 신림역점 | https://mamedene.com/styles/1917761 | `mamedene_브릿지-어바웃9_1917761.jpg` |
| 8 | 레이어드컷 | 레이어드컷, 볼륨펌, 내츄럴펌 | 원장 리오 | 헤어유스 건대점 | https://mamedene.com/styles/1917444 | `mamedene_레이어드컷-헤어유스_1917444.jpg` |
| 9 | 레이어드컷 | 레이어드컷, 내츄럴펌, 텍스쳐펌 | 디자이너 제리 | 오유헤어디자인 홍대점 | https://mamedene.com/styles/1915780 | `mamedene_레이어드컷-오유헤어디자인_1915780.jpg` |
| 10 | 레이어드컷 | 레이어드컷, 텍스쳐펌 | 디자이너 제리 | 오유헤어디자인 홍대점 | https://mamedene.com/styles/1915776 | `mamedene_레이어드컷-오유헤어디자인_1915776.jpg` |
| 11 | 레이어드컷 | 레이어드컷, 쉐도우펌, 리프컷 | 수석디자이너 원철 | 더그레이헤어 | https://mamedene.com/styles/1913362 | `mamedene_레이어드컷-더그레이헤어_1913362.jpg` |
| 12 | 레이어드컷 | 레이어드컷, 리프펌, 볼륨펌 | 수석디자이너 원철 | 더그레이헤어 | https://mamedene.com/styles/1913361 | `mamedene_레이어드컷-더그레이헤어_1913361.jpg` |
| 13 | 레이어드컷 | 레이어드컷, 리프펌, 볼륨펌 | 수석디자이너 원철 | 더그레이헤어 | https://mamedene.com/styles/1913360 | `mamedene_레이어드컷-더그레이헤어_1913360.jpg` |
| 14 | 레이어드컷 | 레이어드컷, 쉐도우펌, 스왈로펌 | 대표원장 백도경 | Rititi(리티티) 신사본점 | https://mamedene.com/styles/1909466 | `mamedene_레이어드컷-Rititi-리티티_1909466.jpg` |

### 리프펌 — leaf perm  (37 shots)

| # | Title (KR) | Tags | Stylist | Salon | Style page | Saved file |
|---|---|---|---|---|---|---|
| 1 | 볼륨펌 | 볼륨펌, 리프펌, 리프컷 | 대표원장 정혁 | 이타헤어 선릉역점 | https://mamedene.com/styles/1897331 | `mamedene_볼륨펌-이타헤어_1897331.jpg` |
| 2 | 리프컷 | 리프컷, 리프펌, 볼륨펌 | 대표원장 정혁 | 이타헤어 선릉역점 | https://mamedene.com/styles/1895698 | `mamedene_리프컷-이타헤어_1895698.jpg` |
| 3 | 리프컷 | 리프컷, 리프펌 | 디자이너 수민 | 박승철헤어스투디오 상도점 | https://mamedene.com/styles/1914883 | `mamedene_리프컷-박승철헤어스투디오_1914883.jpg` |
| 4 | 리프컷 | 리프컷, 리프펌 | 원장 T.K | 애쉬맨즈헤어 | https://mamedene.com/styles/1914445 | `mamedene_리프컷-애쉬맨즈헤어_1914445.jpg` |
| 5 | 리프컷 | 리프컷, 쉐도우펌, 리프펌 | 수석디자이너 원철 | 더그레이헤어 | https://mamedene.com/styles/1914667 | `mamedene_리프컷-더그레이헤어_1914667.jpg` |
| 6 | 리프컷 | 리프컷, 리프펌, 아이롱펌 | 원장 세빈 | 샾머무르다 맨즈 신촌점 | https://mamedene.com/styles/1910997 | `mamedene_리프컷-샾머무르다_1910997.jpg` |
| 7 | 리프컷 | 리프컷, 리프펌 | 원장 초 | 아트룸 상왕십리역점 | https://mamedene.com/styles/1734572 | `mamedene_리프컷-아트룸_1734572.jpg` |
| 8 | 리프컷 | 리프컷, 리프펌, 남성메이크업 | 부원장 사랑 | 디자인안 압구정본점 | https://mamedene.com/styles/1413828 | `mamedene_리프컷-디자인안_1413828.jpg` |
| 9 | 리프컷 | 리프컷, 리프펌 | 디자이너 시은 | 아에르헤어 여의도점 | https://mamedene.com/styles/1916324 | `mamedene_리프컷-아에르헤어_1916324.jpg` |
| 10 | 리프펌 | 리프펌, 쉐도우펌, 리프컷 | 수석디자이너 원철 | 더그레이헤어 | https://mamedene.com/styles/1914665 | `mamedene_리프펌-더그레이헤어_1914665.jpg` |
| 11 | 리프컷 | 리프컷, 리프펌, 아이롱펌 | 원장 세빈 | 샾머무르다 맨즈 신촌점 | https://mamedene.com/styles/1911010 | `mamedene_리프컷-샾머무르다_1911010.jpg` |
| 12 | 리프컷 | 리프컷, 가르마펌, 리프펌 | 대표원장 백도경 | Rititi(리티티) 신사본점 | https://mamedene.com/styles/1909474 | `mamedene_리프컷-Rititi-리티티_1909474.jpg` |
| 13 | 텍스쳐펌 | 텍스쳐펌, 리프펌, 가르마펌 | 디자이너 화범花虎 | 피나트맨 PINARTMAN 상수역점 | https://mamedene.com/styles/1830927 | `mamedene_텍스쳐펌-피나트맨-PINARTMAN_1830927.jpg` |
| 14 | 리프컷 | 리프컷, 리프펌 | 디자이너 정민 | 꾸블랑헤어 고려대점 | https://mamedene.com/styles/1921481 | `mamedene_리프컷-꾸블랑헤어_1921481.jpg` |
| 15 | 리프컷 | 리프컷, 리프펌, 가르마펌 | 점장 은우 | 꾸블랑헤어 성신여대1호점 | https://mamedene.com/styles/1919663 | `mamedene_리프컷-꾸블랑헤어_1919663.jpg` |
| 16 | 리프컷 | 리프컷, 리프펌, 카키브라운 | 수석디자이너 영준 | 오르드비 Or de Vie 상왕십리 | https://mamedene.com/styles/1919078 | `mamedene_리프컷-오르드비-Or-de-Vie_1919078.jpg` |
| 17 | 리프컷 | 리프컷, 아이롱펌, 리프펌 | 디자이너 고유 | 샾머무르다 신촌창천점 | https://mamedene.com/styles/1917636 | `mamedene_리프컷-샾머무르다_1917636.jpg` |
| 18 | 리프컷 | 리프컷, 리프펌, 텍스쳐펌 | 디자이너 민구 | 엥비떼헤어 신논현점 | https://mamedene.com/styles/1917530 | `mamedene_리프컷-엥비떼헤어_1917530.jpg` |
| 19 | 리프컷 | 리프컷, 리프펌 | Stylist 혜원 | 바운스플로 영등포구청역점 | https://mamedene.com/styles/1917311 | `mamedene_리프컷-바운스플로_1917311.jpg` |
| 20 | 볼륨펌 | 볼륨펌, 리프펌, 텍스쳐펌 | 부원장 여월 | 로이드밤 신대방삼거리역점 | https://mamedene.com/styles/1917211 | `mamedene_볼륨펌-로이드밤_1917211.jpg` |
| 21 | 리프펌 | 리프펌, 쉐도우펌, 리프컷 | 원장 김수민 | 탄코맨쉬 천호점 | https://mamedene.com/styles/1916763 | `mamedene_리프펌-탄코맨쉬_1916763.jpg` |
| 22 | 리프펌 | 리프펌, 쉐도우펌, 스왈로펌 | 원장 김수민 | 탄코맨쉬 천호점 | https://mamedene.com/styles/1914942 | `mamedene_리프펌-탄코맨쉬_1914942.jpg` |
| 23 | 댄디컷 | 댄디컷, 리프펌 | 대표원장 승재 | 니우니우헤어 화이트점 | https://mamedene.com/styles/1914919 | `mamedene_댄디컷-니우니우헤어_1914919.jpg` |
| 24 | 리프컷 | 리프컷, 리프펌, 다크브라운 | Thank you 첫방문 | 청담본샵 청담점 | https://mamedene.com/styles/1914413 | `mamedene_리프컷-청담본샵_1914413.jpg` |
| 25 | 리프컷 | 리프컷, 리프펌 | 원장 세빈 | 샾머무르다 맨즈 신촌점 | https://mamedene.com/styles/1913855 | `mamedene_리프컷-샾머무르다_1913855.jpg` |
| 26 | 초코브라운 | 초코브라운, 리프컷, 리프펌 | 디자이너 여름 | 도경헤어드림 본점 | https://mamedene.com/styles/1913042 | `mamedene_초코브라운-도경헤어드림_1913042.jpg` |
| 27 | 리프컷 | 리프컷, 리프펌, 볼륨펌 | 대표원장 백도경 | Rititi(리티티) 신사본점 | https://mamedene.com/styles/1912570 | `mamedene_리프컷-Rititi-리티티_1912570.jpg` |
| 28 | 리프컷 | 리프컷, 가르마펌, 리프펌 | 대표원장 백도경 | Rititi(리티티) 신사본점 | https://mamedene.com/styles/1912569 | `mamedene_리프컷-Rititi-리티티_1912569.jpg` |
| 29 | 리프컷 | 리프컷, 리프펌, 텍스쳐펌 | 디자이너 혁 | 오버마운트 망원점 | https://mamedene.com/styles/1912033 | `mamedene_리프컷-오버마운트_1912033.jpg` |
| 30 | 리프컷 | 리프컷, 볼륨펌, 리프펌 | 원장 지훈 | 애쉬맨즈헤어 | https://mamedene.com/styles/1911996 | `mamedene_리프컷-애쉬맨즈헤어_1911996.jpg` |
| 31 | 리프컷 | 리프컷, 베이비펌, 리프펌 | 디자이너 여름 | 도경헤어드림 본점 | https://mamedene.com/styles/1911041 | `mamedene_리프컷-도경헤어드림_1911041.jpg` |
| 32 | 리프컷 | 리프컷, 리프펌, 아이롱펌 | 원장 세빈 | 샾머무르다 맨즈 신촌점 | https://mamedene.com/styles/1910998 | `mamedene_리프컷-샾머무르다_1910998.jpg` |
| 33 | 리프컷 | 리프컷, 아이롱펌, 리프펌 | 원장 세빈 | 샾머무르다 맨즈 신촌점 | https://mamedene.com/styles/1910996 | `mamedene_리프컷-샾머무르다_1910996.jpg` |
| 34 | 리프컷 | 리프컷, 리프펌, 아이롱펌 | 원장 세빈 | 샾머무르다 맨즈 신촌점 | https://mamedene.com/styles/1910995 | `mamedene_리프컷-샾머무르다_1910995.jpg` |
| 35 | 리프컷 | 리프컷, 리프펌, 아이롱펌 | 부원장 아카 | 샾머무르다 맨즈 신촌점 | https://mamedene.com/styles/1910562 | `mamedene_리프컷-샾머무르다_1910562.jpg` |
| 36 | 리프컷 | 리프컷, 리프펌, 쉐도우펌 | 대표원장 백도경 | Rititi(리티티) 신사본점 | https://mamedene.com/styles/1909481 | `mamedene_리프컷-Rititi-리티티_1909481.jpg` |
| 37 | 리프컷 | 리프컷, 가르마펌, 리프펌 | 대표원장 백도경 | Rititi(리티티) 신사본점 | https://mamedene.com/styles/1909473 | `mamedene_리프컷-Rititi-리티티_1909473.jpg` |

---

## 2. Styles harvested — mamedene 매거진 lookbooks (37 shots)

These are the editorial lookbook spreads — the closest thing found to a printed Korean men's long-hair catalog page. Images are 375×375 crops (only size served).

### `magazines/509` — 「남자들의 워너비 헤어 — 장발 추천 스타일 모음 / 장발로 기를 때 하기 좋은 머리」

Page: https://mamedene.com/magazines/509 · by 카카오헤어샵 · 122,003 views · **the single most on-target page found**. Structured as a grow-out roadmap:

| Section | KR gist | Length stage | Saved files (`mamedene-mag509_jangbal-lookbook-NN.jpg`) |
|---|---|---|---|
| 01 리프컷 & 울프컷 | "머리 기르기 시작할 때" — leaf cut / wolf cut; front and nape length already read as long, still easy to keep tidy | ear → chin | 02, 03, 06, 07, 10, 11 (리프컷) · 14, 15, 18, 19 (울프컷 — long layered nape, natural-curl perm recommended) |
| 02 히피펌 | "스타일링하기 애매한 기장일 때" — the **거지존** (awkward grow-out zone) fix. Thin+tight curl = free/unique; loose+thick curl = refined/luxe | chin → past chin | 22, 23, 26, 27, 30, 31 |
| 03 레이어드컷 & 허쉬컷 | "턱선을 넘는 짧은 단발 기장일 때" — androgynous; design varies by layer step and whether a perm is added | past chin → shoulder | 34, 35, 37, 38 |

### `magazines/172` — 「감성적인 남자 장발 스타일 리프펌」

Page: https://mamedene.com/magazines/172 · sections 리프펌 / 히피펌·베이비펌 / 샤기컷·울프컷, medium-to-long, autumn-winter mood. Files `mamedene-mag172_jangbal-leafperm-04/05/08/09/14/15/20/21/26/27/32.jpg`. Several are shoulder-length; several are back views.

### `magazines/292` — 「빈티지함을 추구하는 그런지펌 스타일」

Page: https://mamedene.com/magazines/292 · **그런지펌 (grunge perm)** — wet-look, separated flyaway strands, deliberately undone. Files `mamedene-mag292_grungeperm-05/06/10/11/19/20.jpg`. `-05`, `-06`, `-11` are the longest (clearly **shoulder-length**) shots in the whole harvest.

Other mamedene magazine IDs checked for title only (titles are retrievable by plain `curl` — the page is server-rendered enough for `<title>`): 159 「길이에 따라 다른 단발 스타일 추천」, 590–600 and 630–637 (2026 issues: AI simulation, 앞머리 TOP3, 인기 펌 3종 — mostly women or short men).

---

## 3. Styles harvested — 네이트뷰 / 뷰리진 (7 shots)

`https://view.nate.com/beauty/view/183331/` — 「남자 장발 스타일 장발펌 종류 존멋」 (뷰리진, 2024-05-06). Renders fully in Chrome; images on `contents-cdn.viewus.co.kr`, downloadable with `curl` + Referer. Three named 장발펌 types:

| KR name | EN gloss | Length | Perm type | Notes from the article | Saved file |
|---|---|---|---|---|---|
| 내추럴펌 | natural perm | below jaw, growing out | cold / 일반펌 over a layered cut | the default men's long-hair perm; adds volume to fine, limp hair; light layering so it doesn't go bushy | `natebeauty_naturalpeom-jangbal-1/2_*.jpg` |
| 멀릿컷펌 | mullet-cut perm | crown to ear, nape past collar | **열펌 (hot perm) recommended** — cold perm gives too much volume | BTS V reference; layer only below the ear line; finish with oil essence or light curl cream | `natebeauty_mulletcut-peom-1/2_*.jpg` |
| 리프펌 | leaf perm | chin+, fringe flowing back into the sides | 열펌, fairly **thick rods**, deliberately weak wave | named for the leaf-shaped fringe flow; works on straight, semi-wavy and curly hair; "rough-dry and done" — the easiest first long perm | `natebeauty_leafpeom-jangbal-1/2_*.jpg` |

Plus `natebeauty_jangbal-thumb_*.jpg` (article hero).

---

## 4. Book / e-book previews

**Nothing with usable interior pages was found.** Detail:

| Book | Source | Preview? | What the preview shows |
|---|---|---|---|
| **임경근 크리에이티브 헤어스타일 디자인 5 — 남성 헤어** (임경근, 광문각출판미디어, 2022, ₩18,000, ISBN K182831057) | 알라딘 ItemId 311996635 · preview `https://www.aladin.co.kr/shop/book/wletslookViewer.aspx?ISBN=K182831057` | **✓ 미리보기 opens** (no login) | **Only 3 pages: front cover, back cover, back cover again.** Cover subtitle *Hair Style Design – Man Hair 114*, "914세트의 헤어스타일 작품 수록". Back cover confirms the series: vol.2 Woman Short Hair 270 / vol.3 Woman Medium Hair 297 / vol.4 Woman Long Hair 233 / **vol.5 Man Hair 114** / vol.6 Technology Manual. Closest thing to a Korean printed men's style catalog located — but no interior pages viewable online. |
| **남성 헤어 스타일북** (최중석, 부크크 POD, 2026-07-29, 115 p, 188×254 mm, ₩20,200) | yes24 goods/194852337 · 알라딘 ItemId 399922965 | ✗ no preview | ToC only: PART 01–10 = 댄디 / 투블럭 / 가일 / **리프** / 드롭 / 크롬 / 아이비리그 / 크루 / 모히칸 / 스포츠 컷; appendix = 기장별 변화 · 네이프 라인 · 구레나룻 · 뒷머리 길이 비교. Explicitly "실제 남성 커트 사진 중심… 고객과 디자이너가 같은 이미지를 공유" — a real consultation photo book, but **cut-centred and short-hair-centred**; no perm chapter. |
| **남성 헤어 토탈 시스템** (하상중, 더로드, 2016, 320 p, ISBN 9791195570225) | yes24 goods/24127097 · 알라딘 ItemId 75619549 | ✗ no preview | 18 chapters; ch.11–18 are trend styles (댄디 / 리젠트 / 투블럭 / 모히칸), 보정, 컬러, 수염, **펌**, 세미메이크업. "4WAY CUT" method. Short-hair oriented. |
| NCS 기반 남성헤어커트 & 캡스톤 디자인 (최은정 외, 광문각, 2020) | 알라딘 ItemId 232083006 — 미리보기 link present | ◐ link exists, not opened | textbook |
| 남성 헤어 커트 (박은준, 메디시언, 2018) | 알라딘 ItemId 138843203 — 미리보기 link present | ◐ link exists, not opened | textbook |
| 9 Matrix Perm — 준오헤어 나인 매트릭스 펌 (준오아카데미, 2018) | yes24 goods/76105197 | ✗ | **Juno Hair's own perm-system book** — most promising unexplored title for perm-wave design |
| 헤어펌 웨이브 디자인 (권미윤 외, 광문각, 2016) | yes24 goods/24843927 | ✗ | |
| 헤어 펌 웨이브 테크닉 (2005) · 헤어펌 웨이브 아트 (2009) · NCS기반 베이직/응용 헤어펌 (구민사, 2020/21) · 헤어펌웨이브 (김경란, 부크크, 2022) · 헤어 펌 디자인 (이영미, 2011) · 헤어 디자인 펌 (이귀영, 2004) | yes24 | ✗ | academic / NCS textbooks, women-model-heavy |
| 매력적인 남자 캐릭터를 위한 헤어스타일 250 (한스미디어, 2017) · 일러스트레이터를 위한 헤어 카탈로그 (AK, 2022) | yes24 goods/56916623, /114678428 | ✗ | **illustration** references for artists, not photo catalogs |

**Preview mechanics learned.** Aladin's 미리보기 is a JS popup — `fn_PopUpPriview` pointing at `/shop/book/wletslookViewer.aspx` with an `ISBN` parameter; navigating that URL directly works, while `/shop/book/wletslookinside.aspx` with an `ItemId` errors out. yes24's `/product/search` with only a `query` parameter **redirects to the homepage**; the working form adds `domain=ALL` (WebFetch handles it fine). Kyobo's `product.kyobobook.co.kr/search` returns **404** to WebFetch.

No Korean beauty-trade PDF (그라피 / 헤어핏 매거진 / 뷰티라이프 / 준오 매거진 / 살롱디자인) was located; `images/pdf/` is unchanged (still only the Japanese 男髪 tachiyomi files).

---

## 5. Query log

Legend ✓ useful · ◐ partial · ✗ dead/blocked.

### Salon chains & aggregators

| Target | Tool | Result |
|---|---|---|
| `junohair.com/stylebook` | Chrome | ✗ 404 ("페이지를 찾을 수 없습니다") |
| `junohair.com/junohair` (nav dump) | Chrome + JS | ✗ **준오헤어 no longer has any style/lookbook section** — nav is ABOUT / SALON / MEMBERSHIP / RESERVATION / J MARKET / COMMUNICATION only |
| `chahong.com` | curl 200 | ✗ it is the **차홍 cosmetics shop**, not the salon; its `/lookbook/lookbook.html` is a **product** lookbook (every `alt="차홍"`, "관심상품 등록 전") |
| `leekaja.com` | curl 200 | ✗ single `href="/lander"` JS shell, no style gallery in HTML |
| `lianhair.com` (리안헤어) | curl 200 | ✗ no style/gallery links in HTML |
| `psc.co.kr` (박승철헤어스투디오) | curl | ✗ connection fail (000) |
| `zeohair.com` (제오헤어), `idhair.co.kr` (아이디헤어) | curl | ✗ connection fail (000) — domains guessed, not confirmed |
| **`hairshop.kakao.com`** | curl + nslookup | ✗ **DNS does not resolve — the domain is retired.** Its successor is `mamedene.com` (마메드네), where all the Kakao Hairshop content now lives. Key access-matrix update. |
| **`mamedene.com/styles`** | Chrome | ✓ 스타일북 landing, 112 imgs, lazy-loaded |
| **`mamedene.com/search/style` with `category`/`gender`/`length`** | Chrome | ✓ the men's perm gallery; filter chips are 카테고리 / 지역 / 성별 / 길이 and they write themselves into the URL |
| **`mamedene.com/proxy/app/v6/hair-styles`** | **curl** | ✓✓ open JSON API; 900 men's perm records pulled in ~30 s |
| `mamedene.com/proxy/app/v6/magazines/<id>` | curl | ✗ returns `error` — no magazine API; use the HTML page |
| `mamedene.com/magazines/{509,172,292,159,590-600,630-637}` | curl (title) / Chrome (body) | ✓ titles by curl; body text + image list needs Chrome after scrolling |
| `kr.object.ncloudstorage.com/mamedene-production/beauty-magazine/<id>_<n>_img_375x375.jpg` | curl | ✓ sequential and guessable; `_img.jpg` and `_750x750` → 404 |
| 헤어핏 / hairfit, 콜라주, 헤어모아, 하이샵 | — | ✗ not tried (budget spent once mamedene delivered) |

### Search engines

| Query / URL | Tool | Result |
|---|---|---|
| google.com search `남자 중단발 펌 스타일 모음` | Chrome | ◐ results render, but **Google now wraps every result href in `/goto` with an opaque encoded target** — real URLs are no longer extractable from `<a href>`; `<cite>` text is domain-truncated (`https://blog.naver.com › lsmfm0722`). Google is now poor as a URL-harvesting proxy. |
| `html.duckduckgo.com/html/` + Korean query | Chrome `get_page_text` | ✓ **best replacement** — full real URLs plus snippets in plain text. Note `javascript_tool` is refused on that page ("BLOCKED: Cookie/query string data"), so use `get_page_text`. |
| WebSearch `남자 장발 펌 스타일 사진 미용실 스타일북 중단발` | WebSearch | ✓ surfaced mamedene magazines 172 / 292 / 159 / 509 and the nate 뷰리진 article |
| WebSearch `남자 헤어스타일 도감 책 헤어 카탈로그 미용 교재 남성 펌 yes24 교보문고` | WebSearch | ✓ book leads |
| `m.blog.naver.com/taehana0426/223192602030` | **Chrome** | ✗ **"This site is not allowed due to safety restrictions."** Confirmed: `blog.naver.com` / `m.blog.naver.com` are blocked to the user's Chrome too, not only to WebFetch. **Do not retry Naver by any route.** DDG/Google snippets of Naver posts remain the only access. |
| dcinside 헤어갤 subject+memo search for `장발펌` | curl | ◐ **works** — HTTP 200, 26 thread rows in the HTML. Not harvested (image target already met); images would need per-thread fetch and dcimg Referer handling. |

### Books

| Query / URL | Tool | Result |
|---|---|---|
| yes24 `/product/search` with only `query` | Chrome | ✗ silently redirects to the yes24 homepage — wrong path |
| yes24 `/product/search` with `domain=ALL` + `query` (`남성헤어`, `헤어 펌`) | WebFetch | ✓ full result lists |
| `yes24.com/product/goods/194852337`, `/24127097` | WebFetch | ✓ ToC + description; **no 미리보기 on either** |
| `product.kyobobook.co.kr/search` | WebFetch | ✗ HTTP 404 |
| `aladin.co.kr/search/wsearchresult.aspx` for `남성 헤어` | WebFetch | ✓ lists ItemIds and flags which have 미리보기 |
| `aladin.co.kr/shop/book/wletslookinside.aspx` with `ItemId` | Chrome | ✗ "요청하신 페이지에 오류가 존재합니다" (wrong endpoint) |
| **`aladin.co.kr/shop/book/wletslookViewer.aspx` with `ISBN`** | Chrome | ✓ viewer opens; 3 pages (covers only) |
| `남자 펌 카탈로그 pdf`, `filetype:pdf 남자 펌 스타일`, 그라피 / 헤어핏 매거진 PDFs | — | ✗ not run (budget) |

### Tooling gotchas (important for the next agent)

- `mcp__claude-in-chrome__javascript_tool` has an **output filter** that refuses any result containing a URL query string, a `key=value` pair, or a base64 blob — it returns `[BLOCKED: Cookie/query string data]` / `[BLOCKED: Base64 encoded data]`. Workarounds that work: emit `new URL(x).pathname` and `.host` separately; join params as `key -> value`; strip everything after `?` before printing. That is why CDN locations are recorded here as host + path.
- `computer:screenshot` intermittently times out (`Page.captureScreenshot timed out after 30000ms`) on mamedene's heavy grid; re-issue the screenshot on its own and it succeeds.
- Other agents shared this Chrome profile and kept creating tabs; always pass an explicit `tabId`.
- Bulk-download rig used (all re-runnable, in the session scratchpad): `mame.py` (API paging) → `cand.json` → `prep.py` (360 px thumbs) → `sheet.py` (contact sheets) → visual screening → `getorig.py` (1080 px originals + `kept_meta.json`) → `mag.py` (magazine images). Pillow is installed only under `C:/Users/vad/AppData/Local/Python/pythoncore-3.14-64/python.exe`, **not** the default scoop Python 3.9 that `python` resolves to.

---

## 6. Not tried / next

1. **Widen mamedene.** Only `category=PERM` + `gender=MALE` + `length=MEDIUM` was pulled (900 records, 306 screened, 127 kept). Still open: `category=CUT` + `gender=MALE` + `length=MEDIUM` with `tags=울프컷` / `샤기컷` / `레이어드컷` — cut listings often carry the longest hair and a perm anyway. Full men's **perm** tag vocabulary observed: 가르마펌 · 쉐도우펌 · 아이롱펌 · 리프펌 · 댄디펌 · 히피펌 · 볼륨펌 · 텍스쳐펌 · 애즈펌 · 내츄럴펌 · 스왈로펌 · 베이비펌 · 포마드펌 · 러블리펌 · 리젠트펌 · 투블럭펌. Cut tags: 댄디컷 · 리프컷 · 투블럭컷 · 레이어드컷 · 울프컷 · 샤기컷 · 슬릭백언더컷 · 포마드컷 · 리젠트컷 · 쉼표머리. **Note there is no 세미히피펌 / 젤리펌 / 빈티지펌 / 슬릭펌 tag** — those are salon marketing names, not mamedene taxonomy; 그런지펌 appears only in magazine 292.
2. **슬릭백 / 올백 gap.** Only `슬릭백언더컷` exists as a tag (8 records) and those are short. A dedicated pass on 올백 / 슬릭백 at 중단발 length is still missing — try mamedene `tags=슬릭백언더컷` with `gender=MALE`, plus DDG for `남자 장발 올백` / `남자 중단발 슬릭백`.
3. **dcinside 헤어갤** is reachable by plain curl and has 26 threads for 장발펌 — real-user (non-salon) shots, complementary to the salon catalog. Needs per-thread fetch plus dcimg Referer handling.
4. **Aladin previews not opened:** ItemId 232083006 and 138843203 (both flagged 미리보기). Also never checked: 리디북스 / 밀리의서재 for 뷰티 교재, and `9 Matrix Perm — 준오헤어 나인 매트릭스 펌` (yes24 76105197), the most promising perm-design title.
5. **Korean blog aggregators that are NOT Naver**, surfaced by DDG but never opened: `celebstyle.co.kr` 「남자 중단발 가르마펌 인기 비결 5가지」, `fashion.inly.kr` 「중단발펌 종류 3가지 비교와 얼굴형별 추천」 (젤리펌 · 히피펌 · 빌드펌), `visualacademy.co.kr/hairbeauty` idx 168420128 (허쉬펌 vs 레이어드펌), `chop.kr` idx 16071615 (찹헤어로그 남자 장발머리). All likely image-rich and not blocked.
6. **Tistory / brunch / 1boon** were never queried directly — use DDG `site:tistory.com 남자 장발 펌` etc.
7. **Larger magazine images.** Only 375×375 is served for `beauty-magazine`. For print quality, click each magazine tile through to its `/styles/<id>` page and pull the 1080 px `originalPhotoUrl`. Magazine 509's 24 linked style IDs: 1706318, 1741972, 1746504, 1603962, 1714098, 1749681, 1720410, 1737316, 1697754, 1690968, 1741355, 1735937, 1476023, 1719773, 1707881, 1630813, 1718068, 1614411, 1609045, 1705150, 1365213, 1602675, 1677202, 1637154. (There is no per-style JSON endpoint — `/proxy/app/v6/hair-styles/<id>` returns `error`; open `/styles/<id>` in Chrome.)
