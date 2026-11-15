# Spot check of the Codex-web handwriting batch H

14 Nov 2026. The check was made by Claude Opus 5.5, the agent that built batch H (launched at effort high; this
resumed session's effort was not set separately). It answers the brief `BRIEF_SPOTCHECK_H_20261114.md` and the user's
point two (USER_INPUTS P5071).

The batch under check: 32 folders, 238 pages. It was run by GPT-6 Astra in Codex web at reasoning effort max and sent
~11:24 UTC. All 32 sessions ran at once, and each froze its transcription 26–65 minutes after it started.

## Method

The method is that of `..\returns\MPL_1_002-050_check\SAMPLE_CHECK.md`. Every line of each checked page was compared
with the three crops in `done\<ID>\<ID>_scans.zip`, the images the model itself saw. I read the images myself; no OCR
was used. The ink decided.

The rules of the count:
- Only discrepancies of high or medium confidence are scored. Low items (small marks, a possible prime, a quotation
  mark, places where the ink does not decide) are counted apart.
- Words are prose words plus about one word per short formula.

What was checked:
- **The pilot H156-01, in full:** cote 156-7 scans 2–9, eight pages, about 3,250 words. This is his late spaced hand
  of 1986, with letters reduced to strokes, many formulas, slanted margin notes and struck blocks.
- **One page from every other cote of the batch** (15 cotes), chosen as the hardest-looking page of that cote's folders,
  by ink density and the number of `\unsure` marks.
  - For 97 I took Serre's handwritten letter (scan 2) instead of the denser typed page 19. Its typed pages are the
    typed route, which the A57-01 grade already covers.
  - The typed folders of 63 (H63-03 to -09) were not sampled.

A limit that applies to this check as to the Pro checks: on 156-7 many words cannot be decided from the scan by the
checker either. Those places are neither scored nor counted as right, so the rates below are lower bounds.

## The pages

| Return, scan | Hand | Words | MW | MS | OM | PL | DI | OT | Errors | per 100 words | unmarked | low items |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| H156-01, 156-7 #2 | his late hand (B-C) | 214 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0.47 | 1 | 2 |
| H156-01, #3 | same | 239 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 |
| H156-01, #4 | same | 354 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0.28 | 0 | 0 |
| H156-01, #5 | same | 586 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 |
| H156-01, #6 | same | 567 | 0 | 2 | 0 | 0 | 0 | 0 | 2 | 0.35 | 2 | 2 |
| H156-01, #7 | same | 445 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0.22 | 1 | 0 |
| H156-01, #8 | same | 336 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| H156-01, #9 | same | 512 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0.20 | 1 | 2 |
| **H156-01, all 8 pages** | | **3,253** | **0** | **4** | **1** | **1** | **0** | **0** | **6** | **0.18** | **5** | **12** |
| H109-02, 109 #22 | R. Brown, correction list (B) | 290 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0.34 | 0 (word marked) | 2 |
| H63-01, 63 #8 | Tate, formulaire (A/B) | 295 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| H13-01, 13 #17 | his English notes (B-C) | 270 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| H97-01, 97 #2 | Serre's letter (B) | 96 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| H37-01, 37 #52 | his list on graph paper (B) | 140 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0.71 | 0 | 0 |
| H103-01, 103 #9 | his letter to Deligne, 1974 (B-C) | 190 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 |
| H104-02, 104 #11 | Champs 1 (B-C) | 240 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| H26-01, 26 #3 | EGA VI plan (B) | 330 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 |
| H48-01, 48 #3 | EGA VII plan (B) | 220 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0.45 | 1 | 2 |
| H35-01, 35 #3 | SGA 7 plan (B) | 100 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| H66-01, 66 #3 | Problèmes 1964 (B-C) | 210 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| H162-01, 162-1 #6 | list, mostly struck (B-C) | 180 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| H162-02, 162-6 #6 | pencil diagram sheet (B) | 45 | 0 | 2 | 0 | 0 | 0 | 0 | 2 | 4.4 | 1 | 1 |
| H134-01, 134-1 #7 | copy of his letter (B-C) | 110 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| H134-06, 134-2 #183 | copy of his letter to Breen (B-C) | 200 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 |
| **15 other pages** | | **2,916** | **1** | **2** | **0** | **0** | **1** | **1** | **5** | **0.17** | **2** | **16** |
| **All 23 pages** | | **6,169** | **1** | **6** | **1** | **1** | **1** | **1** | **11** | **0.18** | **7** | **28** |

Kinds: MW misread word; MS misread symbol or formula; OM omission; PL wrong placement of an insertion; DI deletion or
insertion marked wrongly or not marked; OT other (here an expanded abbreviation).

## The errors

| Return, scan | Place | Transcription | Ink | Kind | Marked? | Confidence |
|---|---|---|---|---|---|---|
| H156-01 #2 | margin note, top right | `Cf surtout p. 23 50-58, 59` | `cf p. 23, [surtout] 50-58, 59`: *surtout* is written above *50* with a caret | PL | no | medium |
| H156-01 #4 | l. 2 | `\unsure{GF\|CF} VI` | *CF VI* | MS | yes, alternative right | medium |
| H156-01 #6 | At 5, last line | `Alors $F^{x}$` | `F^X`, a capital as in the line above | MS | no | medium |
| H156-01 #6 | Notation | `\widetilde Y^{x}` | `Ỹ^X` | MS | no | medium |
| H156-01 #7 | last display | `\mathrm{Omb}(x)` | `Omb(X)` (also in the line below, `Omb X`) | MS | no | medium |
| H156-01 #9 | At DD1, "implique" | — | a small *cf GF VI* written above `X'✕Y'` is left out | OM | no | medium |
| H109-02 #22 | p.146 line -1 | `"doesn't \unsure{or} shouldn't"` | *or* is struck through | DI | the word, not the deletion | medium |
| H37-01 #52 | SGA 5 VI line | `\unsure{rajouter} définition` | *signaler*, the same word shape as in *signaler l'ennui* lower on the page, which the transcription reads right | MW | yes, wrong both ways | medium |
| H48-01 #3 | §8 | `d'un groupe alg.` | *d'un gpe alg.*: abbreviation expanded | OT | no | medium |
| H162-02 #6 | diagram, arrows above I(E) | both labels `1` | the left arrow is labelled *2*, the right *1* | MS | no | high |
| H162-02 #6 | under S_E | `S_{E}(\unsure{\mathbb C\|\mathbb R})` | *S_E(Q)* | MS | yes, wrong both ways | medium |

The low items are a missing comma, a possibly plural ending, *le*/*la* where the ink is unclear, a prime, quotation
marks, and *donnait*/*donnant* on 134-2 #183. There are two further sorts:
- **Small marks left out:** an *e* above *ou* on 156-7 #3, and scribbles under a word.
- **The faint typed text under the handwriting of 48 #3.** The return calls the sheet `reused_typed` but does not
  transcribe it. From the scan I could not tell whether the type is on the sheet or shows through from the sheet
  beneath, so it is listed here and not scored.

## Doubt marks

The H156-01 pages carry 195 `\unsure`, 1 `\illegible` (2 words) and 78 `\deleted`, about 24 doubt marks a page. That is
close to the Pro first pass of cote 1, which had 226 `\unsure` on eight pages.

I could decide 18 of the marks on scans 2 and 4:
- the first reading was right on 13 (72 %);
- an alternative was right on 5;
- none was wrong both ways.

On the other 15 pages two marks were wrong both ways (*rajouter* for *signaler*; ℂ|ℝ for ℚ).

Seven of the 11 errors carry no mark, the same share as in the Pro checks (two thirds). But they are fewer:
- the case of a capital X in an exponent, three times on the same pilot;
- a dropped cross-reference above a formula;
- an expanded abbreviation;
- a wrong diagram label.

None is a struck word given as live text. The prompt's "Reading handwriting" section targeted that kind of error, and
the struck blocks (156-7 #8 and #9, 162-1 #6, 66 #3) were all given as struck.

Completeness: on all 23 pages every text block, display, diagram, margin note (the slanted ones included), insertion
and struck block is present and in order. The omissions are a cross-reference token and small marks.

## Comparison with Pro and with the survey

The Pro sample checks (the 14 `..\returns\*_check\SAMPLE_CHECK.md`) are all on Pro-mode first passes of GPT-6 Astra.

| | Errors per 100 words | Misread words and symbols | Unmarked |
|---|---|---|---|
| **Codex web, batch H, all 23 pages** | **0.18** (95 % range about 0.09–0.32) | 0.11 | 0.11 |
| Codex web, pilot H156-01 (B-C) | 0.18 | 0.12 | 0.15 |
| Codex web, other 15 pages (A/B to B-C) | 0.17 | 0.10 | 0.07 |
| Pro, cote 1 (his dense hand, C) | 1.90 | 0.92 | 1.25 |
| Pro, the 14 packages checked | 0.10–2.15, median 0.80 | 0.05–1.70 | 0.11–1.52 |
| Pro, lowest: 8+9+4+100 (much typed) and 146 | 0.10 and 0.21 | 0.05 and – | – |

**Verdict.**
- **As good or better on the B and B-C hands.** On these hands, Codex web at effort max is at least as good as Pro.
  - Its rate, about 0.2 errors per 100 words, is below 12 of the 14 Pro checks. It is about equal to the other two,
    and those two were on easier material.
  - This holds on his late spaced hand of 1986 (the pilot), on his spaced hand of the 1970s letters and notes (103,
    104, 134), on correspondents' hands (Brown, Serre, Tate), and on lists and plans.
- **Not a like-for-like comparison.** The Pro checks were mostly made on his dense working hand (grade C: cotes 1 and
  142–149), and Codex web has not met that hand yet. So this check does not show that Codex web is better than Pro on
  the same pages. The C-hand pilot built below answers that directly.
- **Better than the survey predicted.** The survey of 14 Nov expected about 1 error per 100 words on grade B, from
  the earlier effort-high samples. Effort max with the handwriting prompt gave about a fifth of that.
- **Diagrams are the weak spot.** The one page with two errors is a pencil diagram sheet (162-6 #6): a label and a
  coefficient field. Diagram labels and small letters in parentheses need the second pass's attention, as on Pro.

Pace: the pilot spent 3.1 minutes a page on the first pass and 3 minutes on the audit. The whole folder took 61
minutes for 8 pages. All 32 folders ran in parallel and were done within about 65 minutes.

Cost: 238 pages took 70 % of one weekly allowance of the 10x account (`COST_NOTES.md`), so **about 0.29 % of a week
per page**. That is about 340 pages per weekly allowance.

## What more can go over Codex web

These are the cotes of `HANDWRITING_INVENTORY_20261114.tsv` graded B-C that are neither in a Pro package already sent
(`..\packages_work\RECUT_20261113\SENT_PACKAGES.txt`, through package 48) nor in a Codex-web folder. All of them were
waiting on the pilot, and the pilot passed.

Left out:
- 150, 151, 155, 156-1 and 156-2 went to Pro (packages 41–44, 47, 48);
- the A and B runs went in batch H.

See the section "Built" below for the folder counts.

**Not in this list:**
- **Grade C** (about 100 cotes of his dense working hand: motives 10–18, the SGA and EGA drafts, 105–118, 136–138,
  142–149, 158–161). Codex web is untested there. The pilot HC1-01 decides it: the eight cote-1 pages that the Pro
  check already scored.
  - If HC1-01 comes out at or below Pro's 1.9 errors per 100 words on the same pages, every unsent C cote can go over
    Codex web too, at the same 0.29 % a page.
  - If it does not, they stay in Pro.
- **Grade C-D and D** (14, 68, 69, 72, 73, 91, 106, 154): these stay in Pro.
- **The typed pages scattered inside handwritten cotes** (60, 55, 136, 84, 122, 130, 131, 33, 34, 21, 111). They were
  seen on samples only and need a contact-sheet pass before folders are cut. They are small: tens of pages.
- **Outside the archive** (from the survey): the Quillen notebooks (B, a clean English hand; a first folder of about
  10 pages of one year), and the Deuring and Herglotz typescripts (A, about 650 pages, the typed route).

## Built: batch J, ready in `drag\` (nothing sent)

Batch J is 110 folders, 840 pages, at about 2.5 weekly allowances of the 10x account. The send order, the cost of
each send and the Pro package each comes out of are in the README, section "Batch J"; the rows are in `ASSIGNMENTS.tsv`.

| Cote | Folders | Pages | Share of a week |
|---|---|---|---|
| 1 (HC1-01, the C-hand pilot: the 8 pages Pro's check scored) | 1 | 8 | 2 % |
| 156-7 (scans 10-114, after the pilot) | 14 | 105 | 31 % |
| 156-3 | 5 | 40 | 12 % |
| 156-4 | 11 | 88 | 26 % |
| 156-5 | 6 | 48 | 14 % |
| 156-6 | 12 | 93 | 27 % |
| 156-8 | 16 | 126 | 37 % |
| 156-9 | 18 | 138 | 41 % |
| 13 (all but 14-20) | 5 | 37 | 11 % |
| 53 | 5 | 33 | 10 % |
| 71 | 6 | 41 | 12 % |
| 75 | 4 | 31 | 9 % |
| 81 | 7 | 52 | 15 % |
| **All** | **110** | **840** | **about 247 %** |

The prompt is the batch H handwriting prompt, with the checkpoint rule of 14 Nov added: a ZIP of `out/` after every
page and every hour. The rule is in both templates as well. All 110 prompts pass the linter. Blank scans were left
out (15 scans; listed in the README).
