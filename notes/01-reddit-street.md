# 01 — Reddit / street-level research: East Asian men, medium-to-long hair, digital perm / light wave

Research date: 2026-09-07
Target: Asian male, oval face, straight thick (1A/1B) hair, wants chin-to-shoulder length with light waves that can also be pushed/slicked back.
Scope: real people — Reddit posters, forum posts, barber/salon channels, YouTube tutorials. NOT editorial/celebrity hair.

**Method note:** `WebFetch` is hard-blocked for `reddit.com` and `old.reddit.com`, and `mcp__Claude_Browser__navigate` refuses old.reddit by policy. The **only** working path was the user's Chrome (`mcp__claude-in-chrome__navigate` + `get_page_text`) against `old.reddit.com/r/<sub>/search?q=...`. Future agents: go straight there. Plain `WebSearch` for Reddit content returned garbage (Walmart/Wikipedia noise) — do not bother.

---

## Styles found

### 1. Korean light perm / "loose perm" (한국식 펌 · 느슨한 펌) — the baseline style
- **Category:** soft all-over wave, usually worn as middle part or lightly pushed back
- **Length band:** chin to just past jaw (posters report needing ~2 months of growth minimum before a salon will perm it)
- **Perm type:** cold perm most commonly; digital/iron perm at higher-end Korean salons
- **Origin:** Korean salon street standard; the single most-requested thing by Asian men on r/malehairadvice
- **Source posts:**
  - https://old.reddit.com/r/malehairadvice/comments/x7auoz/perm_before_and_after/ — "Perm before and after", 134 pts, 20 comments. OP `-Pike`: *"Had my first perm today. Really helps with my flat/stubborn asian hair."* Confirmed in comments he got a **cold perm**.
  - https://old.reddit.com/r/malehairadvice/search?q=korean+perm — the whole cluster of "Korean perm" posts
- **What posters say (routine / cost / cadence):**
  - Wait 48–72 h before first wash; several posters broke this and reported curl loss (r/Hair "First Perm and Washed Within 24 hours").
  - Cost data point: **$150 USD** for a Korean perm in North America (r/Hair, `CameraHelpMe`, "Korean Hair Perm Almost Gone After Just a Month").
  - Longevity is the #1 complaint on thick straight Asian hair: reports of **4 days**, **1 month**, and **1.5 months** vs. a promised 2–3 months. See "Perm-longevity problem" section below.
  - Product stack repeatedly named: curl shampoo → conditioner → leave-in → curl cream/gel, then low-heat blowdry, then wax or sea-salt spray.
- **Oval face + slick back:** Good. The wave is what lets thick straight hair actually bend backwards instead of standing up; multiple posters explicitly want it *for* a slick back (see style 6).
- **Quotes (<15 words):**
  - *"Thats how asians make this korean hairstyle. They perm it."* — `15InchesOfPain`
  - *"Can be anywhere between tight curls to a wave, depending on what size rollers you use"* — OP `-Pike`
  - *"my whole life is a lie cuz now i know how those trendy asians do it"*

### 2. Korean middle part perm (중간 가르마 펌)
- **Category:** middle part / curtain
- **Length band:** chin to jaw; bangs long enough to reach the nose when pulled down
- **Perm type:** cold perm or light digital; some posters get the result without a perm using a hair band + blowdry
- **Origin:** Korean idol street → global
- **Source posts:**
  - https://old.reddit.com/r/malehairadvice/comments/1mwetea/ — "Korean Middle Part Help", `DarkestTeddyGames` (posted 6× across the sub). Very detailed real-world account.
  - https://old.reddit.com/r/malehairadvice/search?q=middle+part+perm — "Taking care of a Korean perm (middle part)", `LootBoxesAreRigged`, 8 pts / 5 comments
- **Routine / effort:** `DarkestTeddyGames` grew 3–6 months to get there; uses a **hair band after showering** to train the part; says the hard part is *layer length variation*, not the perm. Reports barbers default to a two-block and don't understand the middle-part flow.
- **Cons reported:** wind destroys it; hair "sits on the edges rather than on my forehead"; bed head is a daily problem (`LootBoxesAreRigged` asked specifically about this).
- **Oval face + slick back:** middle part is a *forward* style — it fights the slick-back goal. Poster `ardauo2012` (https://old.reddit.com/r/malehairadvice/comments/ied1vc/) permed long straight hair and complained it *automatically* parts in the middle and he dislikes it — relevant warning: at longer lengths a perm tends to default to centre part unless cut/styled against it.
- **Quote:** *"There's nothing on Youtube or online that has a haircut tutorial for this"*

### 3. Wave perm / body-wave perm (웨이브 펌 · 바디펌)
- **Category:** loose S-wave, worn messy or pushed back
- **Length band:** jaw to shoulder
- **Perm type:** digital (heat) perm — this is where "digital perm" is named explicitly
- **Source posts:**
  - https://old.reddit.com/r/malehairadvice/search?q=asian+perm — `VegetableShops`, "Straight asian hair - normal for a perm to not even last 2 months?": *"I got a digital (wave) perm about 2 months ago and the waves went away like 1.5 months in even though my stylist said it usually lasts 2-3 months. They did say my hair is quite strong."*
  - https://old.reddit.com/r/malehairadvice/comments/1uv14ts/ — `Vegetable-Rub-2664` waiting for a **body wave perm + fade** appointment
  - https://old.reddit.com/r/malehairadvice/comments/1akhf0s/ — `CEHyper` posted a full multi-year photo timeline incl. "right after I got a wavy perm" and "the wavy perm after ~3 months once it was longer and lost its curls"
- **Cadence:** `CEHyper` — the perm was hard to manage once grown out with length. Re-perm cadence implied ~3 months.
- **Oval face + slick back:** best fit of all styles for this brief. Wave + length = the hair will actually lie back.
- **Quote:** *"this was hard to manage with all the length"* — `CEHyper`

### 4. Down perm (다운펌) — the enabling technique, not a style
- **Category:** corrective perm applied to sides/sideburns/nape so hair lies flat instead of flaring out
- **Length band:** any; critical at medium length where Asian side hair flares ("porcupine hair", "Asian afro")
- **Perm type:** down perm (straightening chemistry, opposite direction from a wave perm)
- **Origin:** Korean salons; heavily discussed by Asian men in Western cities who can't find it locally
- **Source posts:**
  - https://old.reddit.com/r/malehairadvice/search?q=down+perm — 15+ posts
  - https://old.reddit.com/r/malehairadvice/comments/ (bbqyak) "The possible solution to asian 'porcupine' hair" — 21 pts, 21 comments. Links salon before/after `http://evanstyle.co.kr/manshair/hair/ES101_INFO03.jpg` and a demo video `https://www.youtube.com/watch?v=rh5YnaJGUaI`. Reports Innisfree DIY down-perm product **"does not work"**; DIY kits <$30, claimed to last up to a month.
  - `Fraaaann` — *"I've been getting korean texture perms for a few sessions now, and I used to get a down perm sometimes but that just added to costs"* → down perm is billed as a **separate line item** on top of the texture perm.
  - DASHU For Men Premium Ultra Bond Gel Down Perm 100ml named as an at-home product (r/malehairadvice, `PhilcobSuzuki15`)
- **Suitability:** **Highly relevant to this brief.** The standard pro combo for thick straight Asian hair at medium length is **wave/digital perm on top + down perm on the sides**. Warning from `heinhtet5293`: a bad down-perm-sides + wave-top combo made his round face look *"like a pineapple"* — i.e. the combo must be matched to face shape, oval should be safer.
- **Cons:** extra cost; chemical smell when hair gets wet (`ANUS_DESTROYER_`: *"I don't like how my hair smells like chemicals whenever it gets wet"*); scalp bleeding reported by one poster when rods were too tight.

### 5. Volume perm (볼륨펌) vs. regular perm
- **Category:** root-lift perm, no visible curl on the lengths
- **Source:** https://old.reddit.com/r/Hair/ — `RadiantImprovement4`, "Difference between a volume perm and regular perm (men's)?" — Korean salon priced **regular perm and volume perm separately, volume perm more expensive**.
- **Note:** relevant if the goal is push-back — volume at the root is what stops medium-length Asian hair from lying flat/greasy against the skull.

### 6. Asian long slick-back / pushed-back flow (no fade)
- **Category:** pushed-back / slick-back flow
- **Length band:** jaw to shoulder, sides grown out long enough to tuck behind ears
- **Perm type:** none required, but posters converge on **down perm on the sides** to make it work on Asian hair
- **Source posts:**
  - https://old.reddit.com/r/malehairadvice/comments/ (Crafty_Session_7959) "How to Achieve This Hairstyle?" — image ref https://i.redd.it/ebargb5m151f1.jpeg . Wants slick back **without fading the sides**; reference is the YouTube channel **12 Pell**; currently uses **O'douds Multi Purpose Pomade**. Asks exactly the questions in this brief (can perm + down perm do it, how long to grow, what product).
  - https://old.reddit.com/r/malehairadvice/comments/ome17m/ — `Random_DayDream3r`, "Asian porcupine hair… slicked back my hair and really liked it"
  - `curiousbg` "[Asian Hair] Get hair to stay back" — problem: long thick hair still falls *forward* when dry.
  - `tonyjyoo` "Down perm products to flatten asian hair? Want help getting my slickback flat and not always resting straight up."
- **Products named by real posters for this look:** O'douds Multi Purpose Pomade; By Vilain Gold Digger / Silver Fox (very strong hold, but one poster reports it **rips strands out** on application); Hanz de Fuko Claymation; Layrite Cement Clay; Pete & Pedro Putty; Suavecito (called too weak for stiff Asian hair).
- **Oval face:** favourable — this is the style the brief is aiming at. The consistent real-world finding is that **straight thick Asian hair will not stay back on product alone**; a light wave or down perm is what makes it hold.
- **Quote:** *"it just stands straight up, it doesnt bend back… like most caucasian hair does"* — `Genoo7`

### 7. Korean wolf cut (울프컷) — permed and un-permed
- **Category:** layered shag / wolf cut, often with mullet-y back
- **Length band:** jaw at the front, past-nape to shoulder at the back
- **Perm type:** usually a light perm on the layers; the recurring question is whether it works *without* one
- **Source posts:**
  - https://old.reddit.com/r/malehairadvice/ — `noPIIaccount`, "Does the korean wolfcut work on straight A1 hair without perm/blowdry styling", 7 pts / 6 comments. He explicitly wants a **very low maintenance** cut, no blowdry, no product.
  - `-Eternal_sigh-` https://www.reddit.com/gallery/1ndyf3b — *"my hair is the classic a1 asian straight ass hair with no curl whatsover"*
  - `Vrede2125` (Philippines) https://www.reddit.com/gallery/1liu656
  - `Antique-Advance-1370` https://www.reddit.com/gallery/1uwq58u — wants a perm + **low fade, "more soft mullet"**, doubts he can pull off "the big wavy front"
  - `Goku-MUI-` https://www.reddit.com/gallery/1sxz36m — got a wolf cut, 69 pts / 38 comments. **Key update in the post: "brushing it back has 100% helped"** — i.e. a wolf cut styled backwards rather than forward. Plans to add a **diffuser and volume powder**.
  - `Repulsive_Engine_259` https://i.redd.it/q487zbkzwthh1.png — DIY wolf cut, back "looks like asian bowl cut"; cautionary tale
- **Origin:** Korean/Chinese street + Douyin; adopted heavily by Asian men 2022–2026
- **Suitability:** compatible with pushing back (see Goku-MUI- update). Risk: DIY/bad execution reads as a bowl cut on straight Asian hair.

### 8. Two-block grown long / "long two block"
- **Category:** disconnected sides, long top
- **Length band:** top at chin/jaw, sides short
- **Perm type:** digital perm on top is the classic ask
- **Source:** https://old.reddit.com/r/malehairadvice/comments/ (jpwj96) — *"asian male with super thick and straight hair. Currently with a two block cut… my straight hair makes styling upwards extremely difficult… How do i reach this hairstyle? Digital perm?"* Image ref https://i.redd.it/yyfzbwk2uka51.jpg
- **Note:** `DarkestTeddyGames` reports Asian barbers **default to a two-block** even when you ask for a longer middle-part flow. Relevant risk for the target person: say explicitly you do NOT want a two-block.

### 9. Permed mullet / "mullet-y" long flow
- **Category:** mullet-flow
- **Length band:** shoulder at the back
- **Perm type:** perm (unspecified) — kept for "a few years"
- **Source:** https://old.reddit.com/r/FierceFlow/comments/1fo6ak0/ — `dvdvd77`, 68 pts. *"Perming my hair basically changed my life and helped me feel way more confident in growing length."* Gallery: https://www.reddit.com/gallery/1fo6ak0
- **Note:** This is the strongest "perm as a growing-out enabler" testimonial found. The perm was what made the awkward growing-out stage tolerable.

### 10. Leaf perm (리프펌)
- **Category:** side-part fringe perm; wave concentrated in the bangs only
- **Length band:** medium (jaw)
- **Perm type:** light wave
- **Origin:** Korean, K-drama actors
- **Source:** https://gatsby.sg/mens-lifestyle/8-top-korean-perm-men-hairstyles-in-2024/ (Gatsby brand blog, Singapore) — blowdry for lift, apply GATSBY Meta Rubber Balm Smart, sweep fringe to the side.
- **Suitability:** partial — fringe-only wave doesn't help a full push-back.

### 11. Shadow perm (섀도우펌)
- **Category:** voluminous fringe, soft curls, "casts a shadow on your face"
- **Length band:** medium
- **Perm type:** curly/textured
- **Source:** gatsby.sg (as above). Styling: hair wax to keep curls light and bouncy.

### 12. Gail / Gale perm (가일펌 · garma perm)
- **Category:** 60:40 side part, wavy mid-length fringe styled **up and to the side**
- **Length band:** medium
- **Perm type:** combines root-boosting + root-flattening in different zones
- **Origin:** Korean ("oppa" salon style, named after the Street Fighter character Guile)
- **Source:** gatsby.sg; https://www.hairrisk.com/korean-perm-guide (403 to WebFetch, listed in search results only)
- **Suitability:** **High for this brief.** This is the closest named Korean style to "light wave that can be pushed back" — the whole point of the gail perm is directing hair up and back rather than forward.

### 13. Hippie perm (히피펌)
- **Category:** small curls root-to-tip, 1970s bohemian volume
- **Length band:** medium to shoulder
- **Perm type:** hippie perm (small rods, all-over)
- **Origin:** Korean; the "unpolished" cousin of the standard Korean perm
- **Source:** WebSearch synthesis of nimble-made / vegamour / perfectxhair guides. *"A Korean perm borrows a little of that hippie perm look with a more polished, less-frizzy finish."*
- **Suitability:** **Low** for the slick-back goal — too much curl to push back cleanly. Included for vocabulary completeness.
- **Gap:** no first-person Reddit account of a male hippie perm was found.

### 14. Spin swallow perm (스핀스왈로펌)
- **Category:** alternating outward/inward spin direction for randomised natural curl
- **Length band:** medium
- **Perm type:** cold or digital with alternating rod direction
- **Origin:** Korean salon technique
- **Source:** WebSearch synthesis (nimble-made, protrimhair). No Reddit first-person account found.

### 15. Iron perm / setting perm (아이롱펌) vs cold perm
- **Category:** technique distinction, not a style
- **Source:**
  - https://old.reddit.com/r/malehairadvice/ — `dasupertrooper`, "Korean Iron Perm Vs Cold Perm", 5 pts: *"iron perm requires using a curling iron on permed hair for the curls and cold perm using rollers… only a few places do iron perms."*
  - `Canadianuserxxx`, "Iron Perm on Asian Hair" — researching DIY, references https://www.youtube.com/watch?v=Sm-rvrqLvpo
  - `Bobsclutch1` — *"I got a Korean perm 5 days ago… I believe it's considered a digital perm because they used heat."* → confirms lay usage: "Korean perm" is an umbrella; **digital = heat**.
  - https://old.reddit.com/r/Hair/ — `StellarPando`, "Difference between Korean Perm, Digital Perm and Cold Perm?" — **cold perm and "Korean perm" priced notably cheaper than digital perm** at his local salons.
- **Practical takeaway for the target person:** ask for a **digital (heat) wave perm on large rods** for a soft push-backable wave; cold perm is cheaper but reads curlier/kinkier and dropped fastest in the reports below.

### 16. "Disguised Toast light perm" — a named real-person reference
- **Category:** long Asian hair + light perm
- **Source:** https://old.reddit.com/r/malehairadvice/comments/ssz4m3/long_asian_hair_can_i_pull_off_this_perm_or_try/ — OP `Commercial-Coach-703` with long Asian hair. *"Never had a haircut I liked disguisedtoast's korean light perm, as he calls it."* Gallery: https://www.reddit.com/gallery/ssz4m3
- **Comment consensus:** unanimously yes. *"Yeah you can pull off man your hair is thick"*, *"Easily bro"*.
- **Suitability:** direct precedent for "long Asian hair + light perm" — this is the closest single post to the target person's brief.

### 17. Perm-longevity problem on thick straight Asian hair (cross-cutting finding)
Not a style but the most consistently reported real-world constraint:
- `VegetableShops` (r/malehairadvice): digital wave perm, waves gone at **1.5 months**, stylist promised 2–3.
- `mahjong-maxxing` (r/Hair): cold chemical perm lasted **4 days maximum**, redo lasted barely longer.
- `CameraHelpMe` (r/Hair): Korean perm nearly gone after **1 month**, paid **$150**.
- Root cause named by stylists in these threads: *"my hair is quite strong"* / thick coarse 1A hair resists.
- Mitigations posters were told: no daily shampoo, no hot irons, low-heat blowdry only, curl cream before drying, wax + hairspray to set.
- **Implication:** budget for a re-perm roughly every 2–3 months, and treat any quoted "lasts 6 months" as marketing.

### 18. Perm damage / regret (cross-cutting)
- `PerspectiveEvening56` (r/FierceFlow, 159 pts, 8 days old): https://old.reddit.com/r/FierceFlow/comments/1w1pj0g/ — *"I just wanted to try it once in my life, don't think I'll keep getting it cuz I would rather have a better hair quality"*
- French commenter `chamanedaniel`: you'll have to keep re-perming as it grows out, and the treatment is not kind to the hair fibre.
- `Any-Calendar-8161`: one week after a Korean perm, hair *"extremely dry, almost like a rough sponge"* when dry, fine when wet.
- `hkandbakfbsk`: rods too tight → **scalp bleeding/scabbing**.
- `marketinghelppp`: worried about follicle damage/balding from Korean perms (no authoritative answer given in thread).

---

## Image reference list

| URL | What it shows | Source |
|---|---|---|
| https://www.reddit.com/gallery/x7auoz | Asian male perm before/after, cold perm, flat→textured | r/malehairadvice `-Pike` |
| https://www.reddit.com/gallery/ssz4m3 | Long Asian hair + "Disguised Toast korean light perm" reference | r/malehairadvice `Commercial-Coach-703` |
| https://www.reddit.com/gallery/1fo6ak0 | Shoulder-length permed mullet-flow, Asian male, multi-year | r/FierceFlow `dvdvd77` |
| https://www.reddit.com/gallery/1w1pj0g | Recent (2026) first perm before/after, 159 pts | r/FierceFlow `PerspectiveEvening56` |
| https://www.reddit.com/gallery/1akhf0s | Same guy across wavy perm / middle part / crop / quiff | r/malehairadvice `CEHyper` |
| https://i.redd.it/ebargb5m151f1.jpeg | Target slick-back reference (12 Pell), no fade | r/malehairadvice `Crafty_Session_7959` |
| https://www.reddit.com/gallery/ome17m | Asian "porcupine" hair grown long and slicked back | r/malehairadvice `Random_DayDream3r` |
| https://i.redd.it/yyfzbwk2uka51.jpg | Two-block target, asking if digital perm needed | r/malehairadvice `jpwj96` |
| https://www.reddit.com/gallery/1uwq58u | Korean perm + low fade "soft mullet" reference set | r/malehairadvice `Antique-Advance-1370` |
| https://www.reddit.com/gallery/1sxz36m | Wolf cut, brushed back (OP update: brushing back helped) | r/malehairadvice `Goku-MUI-` |
| https://www.reddit.com/gallery/1ndyf3b | A1 straight Asian hair, wolf cut aspiration | r/malehairadvice `-Eternal_sigh-` |
| https://www.reddit.com/gallery/1liu656 | Filipino, wolf cut growing-out reference | r/malehairadvice `Vrede2125` |
| https://i.redd.it/ha2jtpi3jn8f1.jpeg | "Achievable with styling from straight Asian hair, or perm?" ref | r/malehairadvice `Big_Host_3442` |
| https://i.redd.it/acnphqboan8f1.jpeg | Same question, second reference image | r/malehairadvice `Big_Host_3442` |
| https://i.redd.it/f3nvpoij5qwe1.jpeg | TikTok guy's post-perm look, "1 hr after his perm" | r/malehairadvice `AnnualWild6123` |
| https://i.redd.it/8j3ussrotoad1.png | Asian hair texture target, perm needed? | r/malehairadvice `GeneralSpecific4695` |
| https://www.reddit.com/gallery/18qqh94 | Side part vs perm decision, textured/wavy goal | r/malehairadvice `MNightmare503` |
| https://i.redd.it/hpqrtvbmovwc1.jpeg | Kpop-idol waves target, M23 Asian | r/malehairadvice `stickmadeofbamboo` |
| https://www.reddit.com/gallery/1hznwmd | 1a straight Asian hair → target texture, no perm | r/malehairadvice `Own_Demand5504` |
| https://preview.redd.it/oxqazhdjk8wd1.png?width=874&format=png&auto=webp&s=bc0c905aa19cc881a81e80b74d73cc5208d34df3 | Perm target, asking required length top/sides/back | r/malehairadvice `Gaming_Legend_666` |
| https://www.reddit.com/gallery/1c72v3l | "This is my hair when I got it permed" — result photo | r/malehairadvice `depressedCBC` |
| https://www.reddit.com/gallery/1bx2si4 | Permed middle part, one side flows one side sticks out | r/malehairadvice `47shiz` |
| https://www.reddit.com/gallery/146odfs | Curled-hair target for a "wavy not curly" perm ask | r/malehairadvice `YourInlaw` |
| https://www.reddit.com/gallery/ied1vc | Permed long straight hair that defaults to middle part | r/malehairadvice `ardauo2012` |
| https://imgur.com/wMBFVdk | "friendly neighborhood non-model Asian guy", full long-hair shot | r/FierceFlow `pupunoob`, 196 pts |
| http://imgur.com/a/9O3XQ | Asian long hair 2-year growth journey | r/FierceFlow `Joffreyng92`, 79 pts |
| https://i.redd.it/zot1jhrbx3vf1.jpeg | "The Black Tsunami — Long Asian Hair" | r/FierceFlow `Lifestyle_OF_ACE5` |
| https://www.reddit.com/gallery/1sr1k1k | Asian hair with slight wave, tying back for formal event | r/FierceFlow `katanastormshadow88` |
| https://www.reddit.com/gallery/1chdzdr | Fine straight Asian hair, awkward stage, wants texture | r/FierceFlow `sontoyolo` |
| https://www.reddit.com/gallery/1v3nmbt | 2 yrs growth, "residual perm that jump started my growth journey" | r/FierceFlow `4greements` |
| https://www.reddit.com/gallery/1oyvvgz | Wavy perm grown out 1.5 yrs, wants it wavy again | r/FierceFlow `HighprincessLau` |
| https://www.reddit.com/gallery/1rdneur | 1A fine hair, considering perm, product Qs (22 comments) | r/FierceFlow `Nervous-Goal-1896` |
| http://evanstyle.co.kr/manshair/hair/ES101_INFO03.jpg | Korean salon down-perm before/after (sides flare → flat) | linked by r/malehairadvice `bbqyak` |
| https://www.reddit.com/gallery/1n2gc7x | Korean perm + haircut gone wrong, "ball" head shape | r/malehairadvice `letepluie` |
| https://preview.redd.it/yzeolhezl0rf1.png?width=778&format=png&auto=webp&s=3ce271372bd6ded244f2b4cf35f221fa8206e1c7 | Korean/Japanese perm inspiration, loose wave | r/Hair `thoughtful_thots` |
| https://preview.redd.it/w4k25ak5m0rf1.png?width=756&format=png&auto=webp&s=f208f9b440a7a9051789d8c14d86a13bb5e71c8e | Same poster, curlier variant | r/Hair `thoughtful_thots` |

### YouTube / video references (titles + URLs + channel)

| Title | URL | Channel / note |
|---|---|---|
| Corrective Down Perm for Straight Asian Hair | https://www.youtube.com/watch?v=mNRSAMseDcA | Salon demo, Dec 2022. Directly about hair that won't slick back |
| Korean Down Perm for thick side hair — Dos and Don'ts | https://www.youtube.com/watch?v=mtlK_JiBx0U | DIY at-home down perm walkthrough, Aug 2023 |
| How To Get An Asian Slick Back Hairstyle \| Men's Hair Tutorial | https://www.youtube.com/watch?v=jY3oqpCM6Qo | Jul 2021; key advice = grow the top as long as possible |
| 3 ways to style permed hair! (korean perm) | https://www.youtube.com/watch?v=xoe-gPSjYMY | Jul 2024, personal channel |
| Medium Length Modern Slick Back Tutorial \| Mens Long Hair 2021 | https://www.youtube.com/watch?v=8kP0XdyXWOU | Medium-length slick back |
| Medium Length Slicked Back Hairstyle Tutorial | https://www.youtube.com/watch?v=4T7C1la0EaM | Oct 2020, for guys growing hair out |
| Modern Slick Back for Medium Hair (Trending 2025 Style) | https://www.youtube.com/watch?v=e1Jo-IZEguE | Aug 2025 |
| Asian Gentlemen's Hairstyle Tutorial! \| Haircut & Styling | https://www.youtube.com/watch?v=RNWFCDQKqM0 | tagged #stiffasianhair |
| Asian Haircut for Men \| High Skin Fade & Long Textured Slickback | https://www.youtube.com/watch?v=dHBq-BhMNbE | 2019 barber tutorial |
| Consultation — Asian Hair Makeover! \| 12 Pell | https://www.youtube.com/watch?v=rUV2V_hNhik | **12 Pell** (NYC Asian-hair barbershop), Jan 2022 |
| ASMR Barber — The Combover For Asians! \| 12 Pell | https://www.youtube.com/watch?v=2dso11MgBKA | 12 Pell, Feb 2022 |
| Professional And Casual Asian Style Tutorial \| 12 Pell | https://www.youtube.com/watch?v=H7dGBt6CZgw | 12 Pell |
| 12 Pell channel (all videos) | https://www.youtube.com/@Hairdoc/videos | Channel name "Hairdoc". Shop: https://12pell.com/ |
| Asian Hair Perm Consultation for Textured Crop Hairstyle | https://www.tiktok.com/@12pell/video/7100982445436112170 | 12 Pell TikTok |
| Men's Perm Asian Hair Raw Cut (personal vlog) | https://youtu.be/opwv6738Nak | Posted by r/Hair user `rebelrock12` / IG Leonard_Bui |
| Iron perm at home (referenced by a redditor researching DIY) | https://www.youtube.com/watch?v=Sm-rvrqLvpo | linked by r/malehairadvice `Canadianuserxxx` |
| Korean salon down perm demo (old link, may be dead) | https://www.youtube.com/watch?v=rh5YnaJGUaI | linked by r/malehairadvice `bbqyak` |
| "Down Perm" product demo for Asian sideburns | https://www.youtube.com/watch?v=32TPGKl1Lfs | linked by r/malehairadvice `lightng79` |

**Named real-world shops (Asian-hair specialists, cited by redditors):** 12 Pell — NYC (https://12pell.com/); Klukcuts — California. Both named in r/malehairadvice as places that do genuine consultations on face shape / hair type / maintenance.

---

## Sources searched

| URL or query | Tool used | Result |
|---|---|---|
| "reddit r/malehairadvice asian male digital perm medium length hair" | WebSearch | empty (returned Walmart/Wikipedia noise) |
| "reddit FierceFlow asian hair flow perm shoulder length" | WebSearch | empty (noise) |
| https://old.reddit.com/r/malehairadvice/search?q=asian+perm... | WebFetch | **blocked** — "Claude Code is unable to fetch from old.reddit.com" |
| https://www.reddit.com/r/FierceFlow/search.json?q=asian... | WebFetch | **blocked** — reddit.com not fetchable |
| https://old.reddit.com/... | mcp__Claude_Browser__navigate | **blocked by policy** ("old.reddit.com is blocked by policy") |
| https://old.reddit.com/r/malehairadvice/search?q=asian+perm&sort=relevance | claude-in-chrome | **useful** — 24 posts |
| https://old.reddit.com/r/malehairadvice/search?q=digital+perm+medium+length | claude-in-chrome | useful (partly non-Asian) |
| https://old.reddit.com/r/FierceFlow/search?q=asian+hair&sort=top | claude-in-chrome | **useful** — long Asian hair growth journeys, few perms |
| https://old.reddit.com/r/FierceFlow/search?q=perm&sort=top | claude-in-chrome | **useful** — perm before/afters, mostly non-Asian |
| https://old.reddit.com/r/Perms/search?q=asian+men+digital+perm | claude-in-chrome | **empty** — "there doesn't seem to be anything here" |
| https://old.reddit.com/r/malehairadvice/search?q=korean+perm | claude-in-chrome | **useful** — ~25 posts, best single query |
| https://old.reddit.com/r/malehairadvice/search?q=wolf+cut+asian | claude-in-chrome | **useful** |
| https://old.reddit.com/search?q="down perm" OR "hippie perm" men (sitewide) | claude-in-chrome | **useless** — sitewide search ignored quotes, returned r/pics etc. Do not repeat sitewide reddit search with boolean/quoted terms. |
| https://old.reddit.com/r/korea/search?q=perm+men+salon+cost | claude-in-chrome | near-empty (2 results, 1 relevant, 12 yrs old) |
| https://old.reddit.com/r/malehairadvice/comments/ssz4m3/ | claude-in-chrome | **useful** — Disguised Toast light perm, 7 comments |
| https://old.reddit.com/r/FierceFlow/comments/1w1pj0g/ | claude-in-chrome | useful — perm regret quote; poster not confirmed Asian |
| https://old.reddit.com/r/malehairadvice/search?q=down+perm | claude-in-chrome | **useful** — 20+ posts, best source on down perms |
| https://old.reddit.com/r/malehairadvice/comments/1f3kop7/ | claude-in-chrome | low value — poster was a white redhead, thread derailed into Ed Sheeran jokes |
| https://old.reddit.com/r/malehairadvice/search?q=asian+slick+back+long+hair | claude-in-chrome | **useful** — product names, slick-back struggles |
| https://www.youtube.com/results?search_query=asian+men+digital+perm+medium+length+hair | claude-in-chrome | **dead** — get_page_text returns "No text content found" on YouTube SERPs. Use WebSearch with allowed_domains youtube.com instead. |
| https://old.reddit.com/r/japanlife/search?q=perm+men+hair+salon | claude-in-chrome | low value — salon-anxiety rants, no Asian-male perm styles |
| https://old.reddit.com/r/asianamerican/search?q=perm+hair+men | claude-in-chrome | low value — 2 hair posts, rest off-topic |
| https://old.reddit.com/r/FierceFlow/comments/1fo6ak0/ | claude-in-chrome | useful — permed mullet-flow testimonial |
| https://old.reddit.com/r/malehairadvice/search?q=perm+asian&sort=top | claude-in-chrome | **useful** — top-voted Asian perm posts |
| https://old.reddit.com/r/malehairadvice/comments/x7auoz/ | claude-in-chrome | **useful** — cold perm confirmed, 20 comments |
| https://old.reddit.com/r/malehairadvice/search?q="12 Pell" | claude-in-chrome | useful — found the slick-back thread + shop names |
| https://old.reddit.com/r/Hair/search?q=korean+perm+men+asian | claude-in-chrome | **very useful** — cost ($150), longevity failures, perm-type distinctions |
| https://old.reddit.com/r/malehairadvice/search?q=middle+part+perm | claude-in-chrome | **useful** — middle part perm care, `DarkestTeddyGames` |
| "Korean men perm types glossary hippie perm 히피펌 swallow perm garma perm leaf perm difference" | WebSearch | **useful** — style vocabulary |
| https://www.hairrisk.com/korean-perm-guide | WebFetch | **dead** — HTTP 403 |
| https://gatsby.sg/mens-lifestyle/8-top-korean-perm-men-hairstyles-in-2024/ | WebFetch | **useful** — 7 named styles + products |
| "asian men medium length hair styling tutorial digital perm slick back" (allowed_domains youtube.com) | WebSearch | **useful** — 10 video URLs |
| "12 Pell barbershop youtube asian hair perm medium length slick back video" | WebSearch | **useful** — channel + video URLs |
| "reddit hippie perm men asian hair experience cost" (allowed_domains reddit.com) | WebSearch | **blocked** — reddit.com is not accessible to the WebSearch user agent |
| r/malegrooming, r/AsianBeauty, r/koreanbeauty, r/curlyhair | not searched | **not attempted** — ran out of budget; see Gaps |

---

## Gaps

1. **No first-person male account of a hippie perm (히피펌) or spin-swallow perm.** Those names come only from salon/brand blogs (gatsby.sg, nimble-made, protrimhair), never from a real poster. Someone should search Korean-language sources (네이버 블로그, 디시인사이드 헤어갤) or r/korea in Korean.
2. **Almost no hard cost data.** Only two numbers surfaced: $150 USD for a Korean perm in North America, and "volume perm costs more than regular perm" at a Korean salon. Nothing from Korea/Japan/Taiwan in local currency. r/korea and r/japanlife searches came back nearly empty on this.
3. **No detailed daily styling routine from anyone with the exact target look** (chin-to-shoulder + light perm + pushed back). Posts either describe the perm OR the slick back, never both with a step-by-step. `Crafty_Session_7959`'s thread asks exactly the right questions but got only 4 comments — its comment body was not read (thread ID not captured); worth opening.
4. **Not searched at all:** r/malegrooming, r/AsianBeauty, r/koreanbeauty, r/curlyhair, r/koreanvariety, r/China / r/taiwan. Also no Douyin/Xiaohongshu (Chinese) or 2ch/Japanese salon-blog coverage — the brief's "Taiwanese / Chinese Douyin" origin angle is entirely unexplored.
5. **Instagram barber before/afters not covered.** Only reachable via the Chrome tools with login walls; not attempted. 12 Pell's TikTok is the closest substitute found.
6. **Face-shape guidance is thin.** Nobody in these threads discusses *oval* face specifically. The only face-shape data points are negative: a round face + down-permed sides read as "a pineapple"; a wide/round head made short styles look bad. Oval is generally treated as the easy case, which is likely why nobody posts about it.
7. **YouTube in-browser search is unusable** via `get_page_text`. Video *comments* (often the best source for real routines) were therefore not read at all.
8. **Re-perm cadence** is inferred (~2–3 months from longevity complaints) rather than stated by anyone as a maintenance schedule. Nobody said "I re-perm every N months and it costs X".
