# Spot checks by hand density: Pro and Codex on dense and non-dense hands (17-18 Nov 2026)

**Who checked.** Claude Opus 5.5 at effort max (agent a7d5d89d), at the main session's word (17 Nov, 23:2x UTC). The
user: "Do a few more spot checks. Dense versus non-dense. Codex on dense versus non-dense where that exists."

**The question it serves.** Which route takes the remaining ~5,550 pages: GPT-6 Astra at reasoning effort max (Codex
or Work), or GPT-6 Astra (ChatGPT Pro mode)? The user: "that demands that all the very, very dense shit be readable.
And if Pro is better at that, there's a question."

**What was changed.** Nothing in `returns\`, `codex_web_20261113\done\`, `codex_web_20261113\returns\`, `packages\`
or `second_pass\`. The crops are in my scratchpad.

## Method

The method follows `codex_web_20261113/SPOT_CHECK_J_20261114.md` and the CTRL verdicts.

**Choice of pages, by script** (`density_select.py`):
- **Ink-density proxy:** the rank by `\unsure` and `\illegible` marks plus the rank by size of the page image.
- **In each cell:** the densest page, and the page at the median of that rank sum. That is the "ordinary" page.
- **Excluded:** pages under 100 words, and the typed pages the hand inventory names.

**Reading.**
- Every line of the transcription was compared with the ink, on strips of the page cut at native resolution.
- For Codex these are cut from the same page image whose thirds the model saw (`done/<ID>/<ID>_scans.zip`). Zooms and
  rotations were made where needed.
- I read the images myself, with no OCR.
- Where a Claude second pass exists (cote 150), its changes served as leads only. The ink decided.

**Scoring.**
- **Errors:** only errors of high or medium confidence are scored.
- **Kinds:** MW misread word; MS misread symbol; OM omission; PL placement; DI deletion or insertion state; OT other.
- **Marked or unmarked:** an error is "marked" when the transcription puts a doubt mark on it.
- **Not scored:** places the ink does not decide for me, misreadings inside struck text, and convention questions
  (`\mspage` holding the archive's pencil number, dashes against `\cdots`).

**A limit, said before the numbers.** I read with the transcription in view. The triple check of 15 Nov
(`triple_check_20261115/TRIPLE_CHECK_20261115.md`, lines 22-25 and 130-136) showed that this kind of reading lets a
plausible word pass, and finds about half or less of what a second witness exposes. On the reduced hand of cote 34
many words were not decidable for me at all.

**What the numbers below are.** Floors. "0" means no error I could establish. It does not mean an error-free page.

## The eight pages

| Cell | Route | Page (return, scan) | Why chosen | Hand | Words | Marks (per 100 words) | Errors: MW / MS / OM / PL / DI / OT | Errors | Unmarked | Per 100 words (unmarked) |
|---|---|---|---|---|---:|---:|---|---:|---:|---|
| 1 Pro on B-C | GPT-6 Astra (ChatGPT Pro mode) | MPL_150_001-043, 150 #4 | densest of 192 pages in 150, 151, 156-1, 156-2 (33 marks, 1,878 KB); a landscape double page | his spaced late hand, packed sheet on pink paper (B-C) | 682 | 33 (4.8) | 5 / 1 / 0 / 0 / 0 / 0 | **6** | 4 | 0.88 (0.59), floor (below) |
| 1 | Pro | MPL_150_044-084, 150 #57 | median of the same pool | spaced late hand (B-C) | 193 | 8 (4.1) | 0 | 0 | 0 | 0 |
| 2 Pro on dense C | Pro | MPL_33_002-049, 33 #6 | densest of 162 pages of cote 33 (16 marks, 942 KB) | SGA-period draft (1965), on a reused typed sheet; struck paragraph, slanted margins (C) | 250 | 16 (6.4) | 0 | 0 | 0 | 0 |
| 2 | Pro | MPL_33_050-097, 33 #96 | median of the same pool | a page of derived-category formulas with braces and labels (C) | 139 | 8 (5.8) | 0 | 0 | 0 | 0 |
| 3 Codex on dense C | GPT-6 Astra at reasoning effort max (Codex/Work, K template) | K34-04, 34 #74 | densest of 30 pages of K34-01 and K34-04 (27 marks) | SGA 7 notes, letters reduced to strokes; a vertical margin note, a circled crossed margin, a struck boxed block (C, dense) | 385 | 27 (7.0) | 0 | 0 | 0 | 0, many places undecidable for me |
| 3 | Codex | K34-04, 34 #67 | median of the same pool (both of the cell's pages fell in K34-04) | same hand: a struck boxed block, a slanted margin (C, dense) | 255 | 19 (7.5) | 0 | 0 | 0 | 0 |
| 4 Codex on medium C | Codex | K43-06, 43 #92 | densest of 61 pages of K70-01/05/07, K43-06, K46-03 (30 marks) | definitions of the Weil topology, 𝕍, 𝕂, 𝒞_S; slanted margin (C) | 229 | 30 (13.1) | 0 | 0 | 0 | 0 |
| 4 | Codex | K70-07, 70 #104 | median of the same pool | a scratch page of formulas and diagrams, upside down, crossed through whole (C) | 135 | 15 (11.1) | 0 | 0 | 0 | 0 |

**By cell:**

| Cell | Pages | Words | Errors (unmarked) | Per 100 words (unmarked) | 95 % upper bound if 0 (rule of three) |
|---|---:|---:|---|---|---|
| 1 Pro on B-C | 2 | 875 | 6 (4) | 0.69 (0.46), floor | - |
| 2 Pro on dense C (cote 33) | 2 | 389 | 0 | 0 | 0.77 |
| 3 Codex on dense C (cote 34) | 2 | 640 | 0 | 0 | 0.47 |
| 4 Codex on medium C | 2 | 364 | 0 | 0 | 0.82 |

**150 #4 was checked as a floor.**
- **What I checked:** this landscape double page carries 682 words. I verified on the ink the 10 places where the Claude second pass
  (Claude Opus 5.5 at effort max, 17 Nov) had changed Pro's reading, and read the three crops around them in full.
- **What I did not do:** read the other lines word by word.
- **What I confirmed:** 6 of the 10 changed places are Pro errors. The other 4 are not decided by me: the struck-or-live
  "stratifiante" of l.102, the insertion block of l.66-68, the pen trials of the margin, and the extent of the strike
  on l.77-79.

**The scored errors.**

| Page, line | Pro reading | Ink | Kind | Marked? | Confidence |
|---|---|---|---|---|---|
| 150 #4, l.5 (insertion) | `\uline{surjective}` | *surjection*: the underlined word ends in -tion | MW | no | medium |
| 150 #4, l.97 | "la top. quotient de I est **bien**" | "est **celle**", two tall l | MW | no | medium |
| 150 #4, l.107 | "et **les** familles (à iso près)" | "et **l'ens des** familles" | MW | no | medium |
| 150 #4, l.129 | `\uline{stratifiée} \uline{stricte}` | *stratifiante* stricte (ending -ante; it is the term defined on this page) | MW | no | medium |
| 150 #4, l.132 | `Conditions \unsure{2°) et 1°)}` | "Conditions 1°) et 2°)" | MS | yes | medium |
| 150 #4, l.133 | `\unsure{Partitions stratifiées}` | "Partitions *stratifiantes*" | MW | yes | medium |

The second pass and Hua's witness (Claude Opus 5.5, his project) read the same at all six places.

**Low items and places I could not decide** (not scored):
- **150 #57:**
  - the subscript of `\Sigma_{<x}`: the ink may be ≤, but the mathematics wants strict;
  - a possible struck word at the start of "correspondant aux morphismes cofinaux".
- **33 #6:**
  - `Y'-Y` where the ink may carry an arrowhead;
  - `k'` against a capital-looking K';
  - whether "de" in "F de torsion" is struck;
  - in the struck *Remarque*, "voisinage ouvert Y' de **Y**". The ink is a Y-shaped glyph; the mathematics wants the
    point y, since Y' is a neighbourhood of y with A = 𝒪_{Y,y}.
- **33 #96:** the `\mspage{95}` holds the archive's pencil number. That is the known convention point, not a reading
  error.
- **34 #74:**
  - **in the struck line 2:** Codex reads "Il reste à". The ink begins with a clear capital J, "Je v…", so this is a
    misreading inside struck text, low.
  - **places I could not decide:** "fractions/fonctions", the primes on ξ, "valeur(s) absolue(s)", "= 1" or "= 0" in
    (2.5.5), the "⊗" call sign against a struck X.
- **34 #67:**
  - "Il" written over "Je";
  - whether "supposons" is struck;
  - the wording of the struck block.
- **43 #92:**
  - "complète/complet" (inside a doubt mark);
  - "finie" with an overwritten first letter, not struck.

**What the models did well.**
- **Codex:**
  - on 34 #74 it got the whole mathematical skeleton right: (2.5.4)-(2.5.6), the H⁰(S, R¹f_*), the
    Ker/Coker (1−f) chain, the vertical *Remarque 2.6* with T_ℓ(A)_π and Gal(K̄'/K');
  - on 70 #104 it saw that the page is upside down and wholly struck, and got every formula: Φ_n(c) = 0,
    X² − cX + 1, ζ = (c ± √(c² − 4))/;
  - on 43 #92 it got the double-struck 𝕍 and 𝕂 and the struck-or-overwritten details.
- **Pro:**
  - on 33 #96 it got the whole duality chain with its braces and labels;
  - on 33 #6 the struck *Remarque* and both margins.

## Every check on record, by route and hand

Errors per 100 words, unmarked in brackets, with the pages and words behind each figure.

| Hand | GPT-6 Astra at reasoning effort max (Codex web / Work) | GPT-6 Astra (ChatGPT Pro mode) | Head to head on the same pages? |
|---|---|---|---|
| Typed (A) | not in this check | not in this check | - |
| B, B-C | **0.18** (0.11): batch H, 23 pages. **0.21** (0.13): batch J, 9 pages, 2,365 words. **0.21** (0): 156-7, 479 words. | **0.69** (0.46): this check, 2 pages, 875 words, a floor. All 6 errors on the densest sheet, 150 #4: 0.88 there; 0 on 150 #57. | **no**: different cotes |
| Light C (cote 1) | **1.11** (0.72): HC1-01, 8 pages, 1,526 words | **1.90** (1.25): same pages | **yes**, `GRADE_HC1-01_20261114.md` |
| C, medium | **0**: this check, K43-06 and K70-07, 2 pages, 364 words | median **~0.8**: Pro sample checks of 14 packages, grade C (`returns/*_check/`). Triple check of 15 Nov: about 1.9 per 100 prose words (1.4 with formulas), a floor by witness diff. | no |
| C, dense | **1.39** (0.79): CTRL-148, 15 pages, 2,665 words. **1.39** (0.78): CTRL-145, 15 pages, 2,954 words. **0**: this check, K34-04, 2 pages, 640 words, many places undecidable for me. | **2.44** (1.46): CTRL-148. **1.15** (0.85): CTRL-145. **0**: this check, cote 33, 2 pages, 389 words. | **yes** on CTRL-148 and CTRL-145, verdicts in `codex_web_20261113/returns_control/` |
| C-D | **untested** | **untested** | - |
| For comparison, on dense C | GPT-6.2 Sol at reasoning effort max (Work): **1.73** (1.24) on CTRL-148 | Claude second pass (Claude Opus 5.5 at effort max) residual: **0.60** (0.45) on 148, **0.44** (0.27) on 145 | - |

## What the sample can and cannot carry

**It cannot separate the routes.** Eight pages, 2,268 words, judged by one reader with the text in view. At rates near
1 per 100 words, 400 words carry about four errors, so 0 on two pages is likely by chance as well as by quality. Each
"0" here caps the rate at about 0.5-0.8 per 100 words (rule of three), before allowing for my detection limit.

**It can say three things.**
- **No gross failure of the K template on dense C.** On the densest K34 page the mathematics of every display is right.
- **Pro is not clean on the denser B-C sheets.** 150 #4 has six errors at medium confidence, four of them unmarked.
  They are plausible words for the ink: "bien" for "celle", "les" for "l'ens des", "stratifiée" for "stratifiante".
  Codex's B and B-C checks run at about 0.2, but on other cotes.
- **No sign that Pro reads dense hands better than Codex.** On cote 33 Pro made no error I could establish, and on
  cote 34 Codex made none.

**The evidence that decides dense C is still the head-to-head on the same pages:**
- CTRL-148: Codex 1.39 against Pro 2.44.
- CTRL-145: 1.39 against 1.15, with Codex's unmarked rate the lower, 0.78 against 0.85, and the two routes' errors
  largely disjoint.
- HC1-01 (light C): 1.11 against 1.90.

**Still untested:**
- **C-D hands, on both routes.** Cote 34 is graded C in `HANDWRITING_INVENTORY_20261114.tsv`, not C-D.
- **Pro on typed pages.**
- **A head-to-head on B-C.**
- **The other 30 K round-1 returns,** and the K34-01 return: both of cell 3's pages fell in K34-04.

**The test that would settle the route for dense hands:** one C-D folder transcribed by both routes and graded like
the CTRL verdicts.

## One-line verdict per cell

1. **Pro on B-C:** not clean on the dense B-C sheet. Six errors on 150 #4, four unmarked, against Codex's ~0.2 on B and
   B-C elsewhere.
2. **Pro on dense C (cote 33):** no error I could establish in 389 words. A weak floor.
3. **Codex on dense C (cote 34, K template):** no error I could establish in 640 words, with the mathematics right. A
   weak floor: the hand is so reduced that many words were undecidable for me.
4. **Codex on medium C (K43-06, K70-07):** no error in 364 words. The upside-down, wholly struck formula page was
   handled right.

The new pages give no reason to prefer Pro for dense hands. The head-to-head controls still favour Codex on 148, and
show the two routes about even on 145.

Per-page data: `SPOT_CHECKS_DENSITY_20261117.tsv`. Check events: `CHECK_EVENTS.tsv`, both beside this file.
