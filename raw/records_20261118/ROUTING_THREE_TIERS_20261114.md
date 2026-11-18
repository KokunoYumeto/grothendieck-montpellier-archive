# Routing the remaining transcription work over three external resources

**What this is.** A plan to look at; nothing is sent or run. Written on 14 Nov 2026 by Claude Opus 5.5 at effort high
(a sub-agent of the main session, effort set at launch), at the user's word: spare the Claude allowance and send the
work out in three tiers.
- **API.** Easy pages go to the Anthropic API: Claude Opus 5.5 at effort high, Message Batches.
- **Codex web.** Semi-easy pages go to Codex web: GPT-6 Astra at reasoning effort max.
- **Pro.** The hard rest goes to ChatGPT Pro: GPT-6 Astra in Pro mode.

**Files.**
- The table: `ROUTING_THREE_TIERS_20261114.tsv`, one row per unit (a Pro package, a batch-J folder, or the
  no-package pages of one cote), with pages by grade, the tier, and the tier if HC1-01 comes back good.
- The script: `hua_quality_20261114/routing.py`. It reads `PRIORITY_FOR_PRO_20261114.tsv`.

## A correction to the priority lists first

`PRIORITY_FOR_PRO_20261114` counted 664 typed pages as open that the API already transcribed on 12–13 Nov. Its
coverage read only the *Pursuing Stacks* and *Esquisse* keys. The pages, with their runs:

| Cote | Pages | What |
|---|---|---|
| 25 | 181 | EGA V, run ega25b |
| 24 | 73 | EGA V, Blass translation, run ega24b |
| 119 | 259 | the *Esquisse* dossier: runs r119 and esq119 |
| 129 | 74 | Montreal seminar, run mtl129 |
| 162-5 | 51 | Tapis de Quillen, run t162 |
| 134-2 | 26 | Brown's translations, run brown |

So the typed pages with no transcription are nearly all done. What is left is handwritten.

## The tiers and what puts a page in each

### API: Claude Opus 5.5 at effort high, Message Batches

**For** clean typescripts and typed letters: the typed body.

**Our measured record** (`api_typescripts_20261112/`), 1,361 pages over 14 batches, $93.4 billed:
- **Recall.** On the 28-page pilot, the API caught 178 of the 184 differences that our check against the scans had
  found (96.7 %). The pilot pages had an edition draft.
- **Errors.** The spot check of 13 Nov graded one page from each of five runs. On the typed body it found 0 misread
  words. Reading errors per 100 words: 0, 0, 0.6, 0.9, and 1.7 on Brown's letter, which is full of formulas.
- **Cost a page:**
  - $0.035–0.066 without a draft;
  - $0.086–0.092 with the *Pursuing Stacks* draft;
  - $0.05 used here.

**Where it failed:**
- **The handwritten layer on typescripts.** It dropped handwriting marks; 162-5 needs a second pass on its
  handwritten layer.
- **Formula-dense typed letters.** Brown's letter F needs a second pass.
- **Following the edition draft against the ink.** "stabilise" for his "stablilise", and a struck word given live.
- **Worn or low-resolution copies.** When it checked the SGA 5–7 typescripts, the same model over the API found about
  half the errors that the sub-agents found (9 Nov). Bad scans stay off the API.

**Good enough as is:**
- the typed body of a clean typescript or typed letter, with no draft in the prompt, as a first pass;
- the scripted markup fixes of the spot check.

**Not good enough:**
- his ink on a typescript;
- worn copies;
- anything handwritten.

These go to Codex web, or to Pro, as a second pass.

### Codex web: GPT-6 Astra at reasoning effort max

**For grades B and B-C**, from the batch-H spot check: 23 pages, 0.18 errors per 100 words.
- **B-C:** his spaced late hand (156-x), and one page each of his letters and spaced notes. Confidence high.
- **B:** fair hands and lists. Confidence medium; one pencil sheet came out at 4.4 errors per 100 words.
- **C:** only if the pilot HC1-01 comes back good. Its 8 pages are built, unsent, and now going to Codex web.

**Allowance:** about 0.5 % of a weekly allowance a page (39 % for 86 pages).

### Pro: GPT-6 Astra in Pro mode

**For the rest:** C (his working notes, the dense hand), D (faint pencil, drawings), and anything not yet graded.

**Allowance:** one run per package of about 45 pages; at most 3 runs at a time.

## The routing: base case (HC1-01 not yet graded)

Each unit goes whole to the tier of the majority of its pages.

| Units | Tier | Pages | Cost |
|---|---|---|---|
| Batch J: 109 folders, 13 cotes (13, 53, 71, 75, 81, 156-2 to 156-9) | Codex web | 832 | 4.2 weeks |
| 183 Pro packages (the other 17 of the 200 lie wholly inside batch J) | Pro | 7,431 | 183 runs |
| Pages with no package: 119 (19), 134-2 (37), 162-5 (3), 134-8 (2), 129, 147, 153 (1 each), all C | Pro | 64 | 2 runs, if packed into two packages |
| No package: 134-4 (1 typed page) | API | 1 | under $0.10 |
| No package: 155 (1 page, B-C) | Codex web | 1 | 0.005 weeks |
| **Total** | **API** | **1** | **under $0.10** |
| **Total** | **Codex web** | **833** | **4.2 weeks** |
| **Total** | **Pro** | **7,495** | **185 runs** (183 packages + 2) |

**Held, not routed:** the *Dérivateurs*, 157-1 to 157-5, 2,135 pages, B-C.
- A human edition exists: Künzer, Malgoire, Maltsiniotis. It should be weighed first.
- If they are transcribed, they go to Codex web: 10.7 weeks. The hand looks like the 1986 hand on the contact sheets
  but has not been tested.

**Typed pages inside the Pro packages.**
- No Pro package has 10 or more pages graded typed, so no package is split.
- Grades are per cote, so typed sheets inside the typed-cote packages are counted as C here. These are cotes 10, 12,
  15, 21, 23, 29, 37, 63, 93 and 161-5.
- Codex-web batches A–C took out the typed runs we had found (303 pages). A per-page typed inventory of these packages
  would move the rest to the API at about $0.05 a page.

**The 29 two-witness second passes** in `second_pass_pro_20261114/` (S001–S029) are Pro runs as well. They compete
with these 185 for the same Pro capacity.

## If HC1-01 comes back good

Then every C page moves to Codex web; D stays in Pro.

| Tier | Pages | Cost |
|---|---|---|
| API | 1 | under $0.10 |
| Codex web | 7,634 (batch J 832; 166 former Pro packages 6,737; 65 no-package pages) | 38.2 weeks |
| Pro | 694 (17 packages whose majority is D: cotes 14, 68, 69, 72 with 74, 91, 154) | 17 runs |

That is a trade:
- **Pro:** from 185 runs to 17.
- **Codex web:** from 4.2 weeks to 38.2 weeks, plus 10.7 more if the *Dérivateurs* go too.

**HC1-01 is a single test.** It is 8 pages of one cote. Before the 166 packages move, its result should come with:
- a second C test on a dense cote (the 142/147/149 kind, where Hua's text had 3–8 errors per 100 words);
- a look at whether the light-C figure holds on his 1960s working notes.

A middle course:
1. Move the light C cotes first.
2. Keep the dense cotes in Pro until a dense test is graded.

## Per-tier totals

| | API (Claude Opus 5.5 at effort high, Message Batches) | Codex web (GPT-6 Astra at effort max) | Pro (GPT-6 Astra, Pro mode) |
|---|---|---|---|
| Base | 1 page, under $0.10 | 833 pages, 4.2 weeks | 7,495 pages, 185 runs |
| HC1-01 good | 1 page, under $0.10 | 7,634 pages, 38.2 weeks | 694 pages, 17 runs |
| *Dérivateurs* (held) | — | 2,135 pages, 10.7 weeks | — |
| Already done over the API (12–13 Nov) | 664 typed pages, in the $93.4 billed | — | — |

**API credit.** The amount left is not recorded here; the console balance should be read before any run. On this
plan the API's part of the new first passes is close to nothing. Its real use from here is second passes:
- the typed body of the 664 pages against Hua's text where Hua has it;
- the handwritten layers flagged in the spot check, which go to Codex web or Pro.
