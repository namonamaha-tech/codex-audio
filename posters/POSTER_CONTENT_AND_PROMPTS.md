# Dr. A. Velumani Desk Posters: Content, Layout & Generation Prompts

Two A4 portrait posters (210 × 297 mm), designed for **black & white printing**.
They are a matched series ("Desk Manifesto Nº 01 / Nº 02") with the same grid, fonts and founder band.

| File | What it is |
|---|---|
| `poster-1-focus.pdf` / `.png` | Poster 1, print-ready (A4 PDF; PNG is 2481 × 3509 px = 300 dpi) |
| `poster-2-marathon.pdf` / `.png` | Poster 2, print-ready |
| `poster-1-focus.html` / `poster-2-marathon.html` | Editable versions. Open in Chrome, click the photo frame (or paste an image) to add Dr. Velumani's photo, then **Print → Save as PDF** (A4, margins *None*, scale 100%, *Background graphics* ON) |
| `src/` | Source (HTML/CSS, fonts, build script). Run `python3 posters/src/build.py` to rebuild. Put a file named `velumani.jpg` next to the built HTML files and it loads automatically |

> **Founder photo:** this environment can't download images, so the posters ship with a marked photo frame (46 × 61 mm). Use one of three ways to add the photo: (1) add it in the HTML version and re-export the PDF, (2) give the prompts below to an image tool together with a reference photo, or (3) print the poster and glue a 46 × 61 mm photo into the frame. Use an official Thyrocare / press photo you have the right to use.

---

## Design system (both posters)

- **Style:** Swiss-editorial / neo-brutalist. Heavy condensed headlines, thick black rules, halftone dot textures, outline numerals, registration marks in the corners, a vertical label on the right edge. Pure black on white with no greys that could turn muddy, so it prints crisply on any B&W laser printer.
- **Type:** *Anton* (condensed display headlines) · *Playfair Display Bold Italic* (quotes and the human voice) · *Space Grotesk* (body) · *Space Mono* (labels, data, captions).
- **Grid:** 11 mm side margins, 10 mm top. Content stacks top to bottom. The **founder band** is a full-bleed black block anchored to the bottom of both posters so his credentials read as one "signature".
- **Desk touch:** each poster has a write-in line ("My one thing today" / "Today's kilometre") so it gets used every day, not just looked at.

---

## Poster 1: "Successful or Distracted"

### Content, top to bottom

| # | Zone | Content | How it appears |
|---|---|---|---|
| 1 | Header strip | `DESK MANIFESTO [Nº 01]` · `FOCUS > DIVERSIFICATION` | Thick black top rule, mono caps, "Nº 01" in a black pill |
| 2 | Quote lead-in | **"People generally fall into two categories:** | Big Playfair italic with an oversized opening quote mark |
| 3 | **Hero split panel** (the highlight) | Left: *those who are* **SUCCESSFUL**. Right: *and those who were* **DISTRACTED."** | Two equal panels in one frame. **Left is solid black** with a white bullseye and one straight arrow hitting dead centre (caption "ONE TARGET · 01 → ∞"). **Right is white** with a mess of curvy, dashed arrows flying to many small targets (caption "TWELVE TARGETS · 12 → 0"). The letters of "DISTRACTED" are knocked off-angle, so the word looks distracted |
| 4 | Attribution | — DR. A. VELUMANI · FOUNDER, THYROCARE | Rule + spaced caps |
| 5 | Section head | **THE CORE PHILOSOPHY** *Focus vs. Diversification* · 3 RULES | Anton caps + Playfair italic subtitle |
| 6 | Rule 01 | **MONOTASK TO SCALE**: Do one thing and you can scale it *everywhere*. Do everything and you stay stuck in *one place*. | Big outline numeral "01", bold caps title, one line of body |
| 7 | Rule 02 | **BEWARE THE DISTRACTION TRAP**: Running a dozen operations? Name the one that brings the most happiness, profit & growth. Can't pick one? That isn't diversification. **It's distraction.** | "it's distraction." reversed out in a black highlight bar |
| 8 | Rule 03 | **FOLLOW THE SEQUENCE** ● → ●○○○: Succeed first at one single thing. Only then diversify. Never the other way round. | A small dot diagram shows "one first, then many" |
| 9 | Write-in box | **MY ONE THING TODAY:** ______ DATE __/__ | Bordered box with a dashed write-in line |
| 10 | **Founder band** | See "Founder band" below | Full-bleed black block |

### Image-generation prompt for Poster 1

```
Design a vertical A4 (210×297 mm, 2480×3508 px, 300 dpi) motivational desk poster, STRICTLY BLACK AND WHITE
(pure #000 ink on pure #fff paper, no grey gradients, no colour), optimised for a monochrome laser printer.
Style: Swiss editorial / neo-brutalist poster. Heavy condensed sans-serif headlines (like Anton or Bebas Neue),
elegant bold italic serif for quotes (like Playfair Display Italic), monospace for small labels. Thick black
horizontal rules, halftone dot textures, thin registration-mark crosses in the top corners, small vertical
text on the right edge reading "FOCUS · SCALE · THEN DIVERSIFY". 11 mm margins, generous whitespace, strong grid.

TOP: thin header strip with "DESK MANIFESTO Nº 01" on the left ("Nº 01" inside a black pill) and
"FOCUS > DIVERSIFICATION" on the right, under a thick black rule.

HERO (the main highlight, top 40% of the page): an oversized italic serif line
"“People generally fall into two categories:" and below it one wide frame split into two equal panels:
 - LEFT panel solid black: small italic "those who are" above a huge white condensed word "SUCCESSFUL".
   Below it a bold white line-art bullseye with ONE perfectly straight arrow hitting the exact centre,
   soft white halftone glow behind the target. Tiny caption "ONE TARGET   01 → ∞".
 - RIGHT panel white: small italic "and those who were" above a huge black condensed word "DISTRACTED.”"
   whose letters are slightly rotated and misaligned. Below it a chaotic tangle of many thin black curved
   and dashed arrows flying in every direction at small hollow circle targets, none hitting the centre.
   Tiny caption "TWELVE TARGETS   12 → 0".
Under the frame: "— DR. A. VELUMANI" left, "FOUNDER, THYROCARE" right in spaced caps.

MIDDLE: section heading "THE CORE PHILOSOPHY" (condensed caps) with italic serif "Focus vs. Diversification".
Three numbered rows with large OUTLINED numerals 01, 02, 03 and thin dividers:
 01 MONOTASK TO SCALE — "Do one thing and you can scale it everywhere. Do everything and you stay stuck in one place."
 02 BEWARE THE DISTRACTION TRAP — "Running a dozen operations? Name the one that brings the most happiness,
    profit & growth. Can't pick one? That isn't diversification — it's distraction." ("it's distraction."
    in white text on a black highlight bar)
 03 FOLLOW THE SEQUENCE (small icon: one filled dot → filled dot + three hollow dots) — "Succeed first at one
    single thing. Only then diversify. Never the other way round."
Then a bordered write-in box: "MY ONE THING TODAY: ________________  DATE __/__".

BOTTOM FOUNDER BAND (full-bleed solid black block, bottom 27% of page, white text):
 - Left: a portrait photo of Dr. A. Velumani (Indian man in his 60s, grey hair, warm confident smile, formal
   shirt) in high-contrast black-and-white, about 47×61 mm, white border with a second thin white outline and
   corner crop marks. [Attach a reference photo for likeness.]
 - Right: small spaced caps "THE MAN BEHIND THE WORDS"; very large condensed white name "DR. A. VELUMANI";
   italic serif "Founder of THYROCARE — India's low-cost diagnostics pioneer"; then a 3-column stat row with
   huge condensed numbers:
     "≈₹3,500 Cr"  FOUNDER'S NET WORTH* — Estimate after his 2021 exit
     "₹7,500 Cr"   THYROCARE'S VALUE TODAY — Market cap, Oct 2026
     "829× / 28 yrs" REVENUE GROWTH — ₹1 Cr (1998) → ₹829 Cr (FY26)
   Under it one line: "1996 ₹1 lakh of PF savings, a 200 sq ft room in Mumbai → 2016 IPO, 73× oversubscribed →
   2021 sold 66% to PharmEasy for ₹4,546 Cr → FY26 ₹829 Cr revenue, ₹163 Cr profit".
 - Tiny footnote in monospace: "*Forbes India estimate (2021). Market cap: NSE, Oct 2026."
Mood: bold, disciplined, energising, premium. All text must be spelled exactly as given, sharp and legible.
```

---

## Poster 2: "Startup Is Not a Race. It's a Marathon."

### Content, top to bottom

| # | Zone | Content | How it appears |
|---|---|---|---|
| 1 | Header strip | `DESK MANIFESTO [Nº 02]` · `THE LONG GAME` | Same as Poster 1 |
| 2 | **Headline** (the highlight) | **STARTUP IS NOT A ~~RACE.~~** / **IT'S A MARATHON.** | Huge Anton. "RACE." is outlined with a thick black strike-through. "IT'S A MARATHON." is the largest text on the page |
| 3 | **Illustration** | A long, winding road to the horizon under a halftone sun, with a runner in the foreground. Milestone signs along the road map Thyrocare's journey: **START · 1996 ₹1 lakh** → **KM 2 · 1998 ₹1 Cr sales** → **KM 20 · 2016 IPO · 73× subscribed** → **KM 25 · 2021 ₹4,546 Cr exit** → **KM 30 · FY26 ₹829 Cr sales** | Full-bleed scene. Black road, dotted fields, perspective lines. Signs shrink with distance. A circular race-bib badge reads "42.195 km · not 100 m" |
| 4 | His actual words | *"It is not a 100-metre dash. It's a marathon."* — Dr. A. Velumani, on building a company | Playfair italic |
| 5 | Section head | **HOW TO RUN IT** *4 rules for the long road* · KM 0 → 42 | |
| 6 | Rule 01 | **PACE YOURSELF**: Sprinters burst and fade. Those who rush find it hard to sustain success. Pick a pace you can hold for years. | 2 × 2 grid, outline numerals |
| 7 | Rule 02 | **LET IT COMPOUND**: Thyrocare grew about **25% a year for 25 years**. No magic, just the same good stride, year after year. | Stat in a black highlight bar |
| 8 | Rule 03 | **SHOW UP AT 5 A.M.**: "Define priorities and focus from 5:00 am, consistently." Stamina is built daily, not on race day. | His own line (from his X post) |
| 9 | Rule 04 | **RUN LIGHT, RUN ONE ROUTE**: No debt weighing you down, no four rabbits to chase. He built Thyrocare debt-free, on one problem. | Links back to Poster 1 |
| 10 | Write-in strip | **TODAY'S KILOMETRE** · ONE STEP I'LL TAKE TODAY: ____ | Strip with a "race tape" striped border |
| 11 | **Founder band** | Same as Poster 1 | |

### Image-generation prompt for Poster 2

```
Design a vertical A4 (210×297 mm, 2480×3508 px, 300 dpi) motivational desk poster, STRICTLY BLACK AND WHITE
(pure black ink on white, no colour, no soft grey gradients; use halftone dots for tone), for a monochrome
laser printer. Same series style as a Swiss editorial / neo-brutalist poster: heavy condensed sans headlines
(Anton / Bebas Neue), bold italic serif for quotes (Playfair Display), monospace labels, thick black rules,
registration crosses in the top corners, small vertical edge text "PACE · CONSISTENCY · STAMINA".

TOP: header strip "DESK MANIFESTO Nº 02" (Nº 02 in a black pill) left, "THE LONG GAME" right.

HEADLINE (the main highlight): two lines filling the width:
 "STARTUP IS NOT A RACE." — the word "RACE." in outlined letters with a thick black diagonal strike-through,
 "IT'S A MARATHON." — the largest, boldest line on the poster.

ILLUSTRATION (full-bleed band, about 25% of the page): graphic black-and-white landscape. A long, winding
solid black road with a white dashed centre line snakes from the foreground to a vanishing point on the
horizon. A large halftone-dot sun sits behind black silhouetted hills. Fields are a fine dot texture with
perspective lines. In the foreground, a bold pictogram runner (Olympic-pictogram style, thick rounded limbs,
round head) runs up the road with speed lines. Rectangular milestone signs on posts along the road, getting
smaller with distance, in monospace text:
 "START · 1996 / ₹1 lakh" (nearest), "KM 2 · 1998 / ₹1 Cr sales", "KM 20 · 2016 / IPO · 73× subscribed",
 "KM 25 · 2021 / ₹4,546 Cr exit", "KM 30 · FY26 / ₹829 Cr sales" (farthest).
A circular race-bib style badge in the sky, upper left: "42.195 km · not 100 m".

QUOTE: big serif quote mark + italic serif "It is not a 100-metre dash. It's a marathon."
with small caps "— DR. A. VELUMANI, ON BUILDING A COMPANY".

RULES: heading "HOW TO RUN IT" + italic "4 rules for the long road"; 2×2 grid with large outlined numerals:
 01 PACE YOURSELF — "Sprinters burst and fade. Those who rush find it hard to sustain success. Pick a pace you can hold for years."
 02 LET IT COMPOUND — "Thyrocare grew about 25% a year for 25 years. No magic — just the same good stride, year after year."
    ("25% a year for 25 years" white on a black bar)
 03 SHOW UP AT 5 A.M. — "“Define priorities and focus from 5:00 am, consistently.” Stamina is built daily, not on race day."
 04 RUN LIGHT, RUN ONE ROUTE — "No debt weighing you down, no four rabbits to chase. He built Thyrocare debt-free, on one problem."
Then a strip with a striped black-and-white "race tape" border: black block "TODAY'S KILOMETRE" + "ONE STEP I'LL TAKE TODAY: ______".

BOTTOM FOUNDER BAND: identical to the series. Full-bleed black block. Left: high-contrast B&W portrait photo of
Dr. A. Velumani (Indian man in his 60s, grey hair, warm confident smile) with a white border and crop marks
[attach a reference photo]. Right: "THE MAN BEHIND THE WORDS", huge white "DR. A. VELUMANI", italic
"Founder of THYROCARE — India's low-cost diagnostics pioneer", and three huge stats:
"≈₹3,500 Cr" FOUNDER'S NET WORTH*, "₹7,500 Cr" THYROCARE'S VALUE TODAY (market cap, Oct 2026),
"829× / 28 yrs" REVENUE GROWTH (₹1 Cr in 1998 → ₹829 Cr in FY26), then the journey line
"1996 ₹1 lakh of PF savings, a 200 sq ft room in Mumbai → 2016 IPO, 73× oversubscribed → 2021 sold 66% to
PharmEasy for ₹4,546 Cr → FY26 ₹829 Cr revenue, ₹163 Cr profit". Tiny footnote "*Forbes India estimate (2021)."
Mood: calm, patient strength; endurance over speed. All text spelled exactly as given and crisply legible.
```

---

## Founder band (shared): the facts and where they come from

| Item on poster | Value | Source / note |
|---|---|---|
| Name | Dr. Arokiaswamy Velumani (Dr. A. Velumani) | Founder of Thyrocare Technologies. Sold control in 2021 |
| **Founder net worth** | **≈ ₹3,500 Cr** | Forbes India (2021): roughly what he kept after the ₹4,546 Cr sale, having reinvested ₹1,500 Cr into PharmEasy. He later wrote that he lost ~₹1,400 Cr on that startup investment. **No verified current figure exists.** Some aggregator sites claim "₹5,000 Cr+" but cite nothing, so the poster uses the sourced estimate |
| **Company value** | **₹7,500 Cr** | Thyrocare market cap, NSE, late Oct 2026 (≈ ₹7,300–7,700 Cr depending on the day) |
| **Growth** | **829× in 28 years** | Revenue ₹1 Cr (1998, *The Weekend Leader*) → ₹829 Cr (FY26 consolidated, company results). In his own words: "25 percent CAGR for 25 years" (Forbes India) |
| Seed | ₹1 lakh of PF savings, 1996, a 200 sq ft room in Byculla, Mumbai | Some sources say ₹2 lakh |
| 2016 | IPO, oversubscribed 73× | FY16 revenue ≈ ₹241 Cr |
| 2021 | Sold 66.1% to PharmEasy (API Holdings) for ₹4,546 Cr | ₹1,300/share |
| FY26 | Revenue ₹829 Cr (+21%), PAT ₹163 Cr (+81%) | Company results |

**Quote notes**
- *"People generally fall into two categories: those who are successful and those who were distracted."* This is used as you gave it. I couldn't find this exact wording in indexed press, though his "focus on one thing" message is widely reported (YourStory, Tamil Nadu Story 2024). It most likely comes from a video or podcast.
- *"Startup is not a race, it's a marathon."* The headline is your phrasing. The quote line on the poster is his documented wording: *"it is not a 100 metre dash, it's a marathon race"* (The Core; People Matters; YourStory).
- *"Define priorities and focus from 5.00 am, consistently."* From his X post (@velumania).
