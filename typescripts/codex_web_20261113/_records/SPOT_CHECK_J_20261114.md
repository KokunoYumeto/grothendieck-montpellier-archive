# Spot check of the Codex-web handwriting batch J

**Who checked.** 15 Nov 2026 (UTC), by Claude Opus 5.5, the agent that wrote the batch-H check. It was launched at
effort high; the effort of this resumed session was not set separately. The brief is the main session's message of
14 Nov ~23:2x UTC.

**The batch under check.**
- **Model:** GPT-6 Astra in Codex web, at reasoning effort max.
- **What came back:** 53 of the 109 J folders, 402 pages, from 9 of the 12 cotes. Six of them (J156-3-01,
  J156-5-05, J156-6-01 to -04) were filed on 15 Nov at 09:49 UTC and checked in the addendum below.

| Cote | Folders back |
|---|---|
| 13 | 5 of 5 |
| 53 | 5 of 5 |
| 71 | 6 of 6 |
| 75 | 4 of 4 |
| 81 | 7 of 7 |
| 156-3 | 5 of 5 (J156-3-01 added 15 Nov) |
| 156-4 | 11 of 11 |
| 156-5 | 6 of 6 (J156-5-05 added 15 Nov) |
| 156-6 | 4 of 12 (J156-6-01 to -04, 15 Nov) |

- **Not checked:** 156-7, 156-8 and 156-9 have no J folder back yet, so this check gives no verdict on them.

## Method

**As in `SPOT_CHECK_H_20261114.md`:**
- **One page from every returned cote:** the hardest-looking page of that cote's folders. It was chosen by script,
  by the number of `\unsure` marks and the size of the page image, which stands for ink density.
- **Every line compared with the crops the model saw:** the three thirds `_s1`–`_s3` in `done\<ID>\<ID>_scans.zip`.
  I read the images myself, with no OCR; the ink decided.
- **What is scored:** only discrepancies of high or medium confidence. Low items are counted apart: small marks, a
  possible prime or dot, case, and places where the ink does not decide.
- **Words:** prose words plus about one word per short formula or diagram node.

**Kinds:**
- MW: misread word;
- MS: misread symbol;
- OM: omission;
- PL: placement;
- DI: deletion or insertion state;
- OT: other.

**A limit.** As on 156-7 in batch H, many places on these pages cannot be decided from the scan by the checker either:
- the diagonal insertion block of 156-4 #19;
- the slanted margin notes of 81 #27 and 156-3 #18;
- the struck working at the top of 53 #4.

Those places are neither scored nor counted as right, so the rates are lower bounds. Nothing in `returns\`, `done\`
or the packages was changed.

## The pages

| Return, scan | Hand | Words | MW | MS | OM | PL | DI | OT | Errors | per 100 words | unmarked | low items |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| J13-03, 13 #37 | his notes on motives: a full sheet of boxed diagrams, then a numbered list (C/B-C) | 382 | 0 | 0 | 1 | 0 | 1 | 0 | 2 | 0.52 | 2 | 2 |
| J156-3-03, 156-3 #18 | his late hand of 1986, letters reduced to strokes, margins (B-C) | 313 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 |
| J156-4-03, 156-4 #19 | the same hand, with a block of diagonal insertions (B-C) | 188 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 |
| J156-5-03, 156-5 #18 | the same hand, with a ruled-through margin note (B-C) | 240 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0.42 | 0 (marked) | 3 |
| J53-01, 53 #4 | his working notes on group schemes, ruled paper, struck blocks (C) | 354 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 |
| J71-06, 71 #48 | a fair copy in another hand (signed, Montpellier, 15 July 1976), with his margin notes (B) | 327 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0.31 | 1 | 3 |
| J75-04, 75 #26 | his spaced hand: orientations and torsors (B-C) | 154 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 |
| J81-04, 81 #27 | his late hand, with a long slanted margin note (B-C) | 187 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0.53 | 0 (marked) | 2 |
| J156-6-04, 156-6 #31 (15 Nov) | his late hand of 1986: figures and strata, struck and interlined blocks, slanted margins (B-C) | 220 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 |
| **All 9 pages** | | **2,365** | **2** | **0** | **2** | **0** | **1** | **0** | **5** | **0.21** | **3** | **21** |

## The scored discrepancies

| Return, scan | Place | Transcription | Ink | Kind | Marked? | Confidence |
|---|---|---|---|---|---|---|
| J13-03 #37 | d), "Il en résulte aussi que le diagramme", top arrow | `\pi_1(S(\mathbb C),\xi)\arrow[r]` with no label | a `w` stands above the arrow, joined by a short stroke from above | OM | no | medium |
| J13-03 #37 | d), "de type fini sur …" | `de type fini sur $\mathbb Z$` | the `Z` is crossed through with an X | DI | no | medium |
| J156-5-03 #18 | "A partie fermée … de L" | `\uline{\unsure{par ordre\|pour ordre\|par ordinaire}}` | *modérée*, underlined, as in *partie fermée modérée* on 156-3 #18 | MW | yes, all readings wrong | medium |
| J71-06 #48 | line 1, right edge | — | a boxed `XIX` after *appartiennent à* (a reference to lemma XIX) | OM | no | medium |
| J81-04 #27 | line after the first chain | `\unsure{nos diagrammes\|un diagramme}` | *un diagramme* | MW | yes, alternative right | medium |

**Low items.** These were not scored.
- 13 #37: `G(\mathbb Q)` for `G(\mathbb Q_\ell)` in the struck last line.
- 156-3 #18: the dot over `I` in the margin formula `(I∩J)^· ⊂ I^· ∪ J^·`.
- 156-4 #19: *alors* for *donc* in the struck Contr₂.
- 156-5 #18:
  - a small *NB* before "(la définition de A°" left out;
  - whether *fermées* in "(i.e. fermés dans F)" is struck.
- 53 #4: the boxed margin note "Or G×W→W×W est générisant et G" given as struck. A ruled line crosses it, but that
  may be the strike of the main text.
- 71 #48:
  - `Λ^{1'}` against `Λ''`;
  - `A(Λ^1)` against `A(Λ')`;
  - *bon sommet s de* against *bon sommets de*.
- 75 #26:
  - `E(I,x)` against `E(I,X)`;
  - whether *comp.* is struck.
- 81 #27:
  - whether *très* is struck;
  - a `X` that may be struck at a line end.

**What the model did well.** These are the places where the hand is hardest.
- 13 #37: the whole layout of boxed diagrams, with their labels A–G.
- 81 #27: the overwritings, `Σ_{~~1~~2}^-` and `~~E~~Σ₁₂`.
- 75 #26: `{~~0~~1,2,…,n}`.
- 71 #48: the student's own spellings, *foçon*, *corespondant* and *montent*, kept as written.
- Doubt marks fall on the genuinely hard words. As in batch H, they are dense: 25–50 `\unsure` on these pages.

## Comparison

| | Errors per 100 words | Unmarked per 100 words |
|---|---|---|
| **Batch J, 9 pages (this check, with 156-6)** | **0.21** | 0.13 |
| Batch H, 23 pages | 0.18 | 0.11 |
| Codex web on grade C, HC1-01 (cote 1, 8 pages) | 1.11 | 0.72 |
| Our Pro first pass, cote 1 (same 8 pages) | 1.90 | 1.25 |

Batch J sits with batch H. These are the B and B-C hands, and 53 and 13 are on the C side of B-C. They are much
better than the grade-C test HC1-01.

## Verdict per cote

A cote **passes** when its hardest page's text can stand as the transcription, so that its scans can leave the
waiting Pro packages.

| Cote | Verdict | Basis |
|---|---|---|
| 13 | **pass** | 0.52 per 100 words on its densest sheet: 2 unmarked slips, an arrow label and a struck Z |
| 156-3 | **pass** | 0 scored on #18; several margin places undecidable for the checker too |
| 156-4 | **pass** | 0 scored on #19; the diagonal insertion block undecidable |
| 156-5 | **pass** | 0.42; one marked misreading (*modérée*) |
| 53 | **pass** | 0 scored on #4 |
| 71 | **pass** | 0.31; one omitted boxed reference numeral |
| 75 | **pass** | 0 scored on #26 |
| 81 | **pass** | 0.53; one marked misreading, alternative right |
| 156-6 | **pass** | 0 scored on #31 (220 words); the overwritten `Omb(X)` and two possible strikes undecidable or low |
| 156-7, 156-8, 156-9 | **no verdict** | no J folder back yet; 156-7 has the batch-H pilot H156-01 at 0.18 |

**Follow-up.** The pages these cotes return still need what batch H needed: a second pass at the review stage, aimed
at the marked places, the deletion state and the slanted margins. That is not a Pro first pass, so none of these
cotes needs one.

## Addendum, 15 Nov 2026: the returns filed at 09:49 UTC

Checked by Claude Opus 5.5 (launched at effort high; this resumed session's effort was not set separately), at the
coordinator's request, by the method above. Nothing in `returns\`, `done\` or the packages was changed.

**Cote 156-6 (new).**
- The page: J156-6-04, scan 31 (ms. page 30). The script picked it as the hardest-looking of the 32 pages in
  J156-6-01 to -04: 34 `\unsure` marks and a 619 KB image.
- The checked text: 220 words. The page is on M-figures and strata (At\*2₀, At\*3₀), with a struck heading, two
  interlined rewrites of "Ceci dit, …" and slanted margin notes (cf GF IV p. 54–55, 58; "c'est la multistrate
  définie par A"; "C'est C1 pour F_M").
- **Scored discrepancies: none.** The two diagrams (`M ⥲ M̃* ⊂ P(M)` and the square `F_M ⥲ F̃` over `P(P(M)) ⊃`,
  `P(M)`), the struck `(1.79)`, the boxed GF IV reference and all the interline insertions are right. The missing
  closing parenthesis in `P(P(M)` is in the ink too.
- **Low items (not scored):**
  - whether *on* in "Ceci dit, on ~~demande que~~" is struck. The ink inserts only *veux que* above it; the model
    strikes *on* and marks its reading `Je veux|on veut|on veux`;
  - whether *soit* before *préadmissible* is struck;
  - `d'un~~e~~`, where the strike may cover only *partie*.
- **Undecidable:** the overwritten argument inside `{Omb(X) | X ∈ F}`.
- **Verdict: pass** (0 per 100 words, 0 unmarked).

**J156-3-01 and J156-5-05.** No new page was checked, because their hand does not differ from the pages already
checked for those cotes.
- J156-3-01 scan 2 ("Réseaux via découpages", 8 juin 86) is the same late 1986 hand as 156-3 #18: reduced letters,
  a struck slanted margin block.
- J156-5-05 scan 39 is the same hand as 156-5 #18. Its margin runs vertically, not slanted, but it is of the same
  kind as the ruled-through margin note scored there.

The cotes 156-3 and 156-5 keep their pass.
