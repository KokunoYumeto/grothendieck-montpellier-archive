# What to transcribe next, against Michel Hua's first pass: two ordered lists

> **Correction, 15 Nov 2026 ~10:5x UTC (the user, through the coordinator):** Michel Hua's text is never used as the basis of a transcription. It may serve as a witness only. Every page is transcribed from the scans. The 80 grade-T pages once routed "Hua + check" (cotes 25, 119, 134-2, 162-5) had already been transcribed from the scans over the API on 12-13 Nov (Claude Opus 5.5 at effort high, Message Batches), and no folder, package or prompt ever started from his text. The verdicts "(i) basis" below are withdrawn. The text as it was is in `PRIORITY_FOR_PRO_20261114_before_no_basis_20261115.md`.

14 Nov 2026, Claude Opus 5.5 at effort high (Claude Code sub-agent, effort set at launch), at the user's word relayed
by the main session (Claude Opus 5.5 at effort max): "Most difficult shit that is never transcribed by anyone first",
for the Pro prompts; and for Codex web: "the easier to transcribe stuff that still needs retranscription, where theirs
falls short. But where our Astra prompt shows that it may be possible to do it."

**Their text.** Commutator-IO/grothendieck-project, commit `aef7db2`; 165 folders, 9,420 pages. It is an AI
transcription, by Claude Opus 5 and Opus 5.5, read again in part by Claude Fable 5.2 (efforts not recorded). It is
free to use with credit.

**Sources of the figures.**
- `HUA_TRANSCRIPTION_QUALITY_20261114.md`: 381 pages compared by script, 5 by eye.
- `HUA_SAMPLE_PER_GRADE_20261114.md`: 36 pages by eye, by grade.
- `codex_web_20261113/SPOT_CHECK_H_20261114.md`: Codex web, 23 pages graded.

**Files.**
- `PRIORITY_FOR_PRO_20261114.tsv`: every run of scans of the 178 cotes, blanks left out. Columns: tier, grade, Hua,
  ours, existing edition, Pro package, J folder, Codex route.
- `PRIORITY_FOR_PRO_20261114_PACKAGES.tsv`: all 200 waiting Pro packages in order.
- Scripts in `hua_quality_20261114/`:
  - `priority_data.py` and `priority.py`, which read files only;
  - `contact.py`, which made the contact sheets `cs/sheet_*.jpg`.

## What they did well and what they did not, by kind of page

| Kind of page (grade) | Hua's errors per 100 words | Readable words left as gaps per 100 | Done well | Done badly |
|---|---|---|---|---|
| Typed by others; his typed letters (A) | **0.5** | 0 | Typed body exact; typed x-outs marked; clipped letters restored and marked | «» for his "..."; his ink tagged as the transcriber's supply; typed-over words dropped without a mark |
| His typescripts with his ink corrections (T) | **1.3**, all in the ink (0 in the typed body) | 0 | Typed body; most insertions and deletions | His corrections of numbers missed (3.13 for 4.13); struck spans given live; insertions misplaced or dropped; spelling modernized (*nœthériens*). None of these errors is marked |
| Others' fair hands (Brown, Serre) and his lists (B) | **1.4** (0.7 without quote marks) | 0.2 | Brown's fair copies and the EGA VI lists clean | His letter to Mumford, 13 #19: 4 unmarked errors in 60 words, one of them a clause rewritten |
| His spaced late hand, 1976–86 (B-C) | **1.4**, 3 of 7 marked | **2.0**, plus slanted margin notes given as fragments | The main text mostly right; struck and inserted structure kept | Abbreviations expanded; the margins; struck symbols as gaps |
| His working notes (C) | **1.5** on light pages; **3–8** on dense pages (142, 147, 149: 24.6 words in 100 differ from our checked text, over 381 pages) | 1.1 (light); about 3 (dense) | Formulas and displays; the run of the argument | Plausible prose in place of the ink, often whole clauses; struck text given live at 9 times Pro's rate (0.56 against 0.06 per 100 words); margins unread |
| Faint pencil, drawings (D) | **2.2**, half marked | 1.9 | Clear spaced pages (154 #90 clean) | Text not on the page (*est tel que*); live text given struck; drawing pages described in a note instead of transcribed (154: 51 pages of descriptions) |
| Formularies and correction lists (63 Tate, 109 Brown) | — | — | — | **Not transcribed at all:** a note describes the page. 63 #3–94 and 109 #13–38 |

**For comparison**, over the same kinds of page:
- Our Pro first pass (GPT-6 Astra, ChatGPT Pro mode): about 1 error per 100 words on C, 1.9 on cote 1.
- Codex web (GPT-6 Astra at reasoning effort max): 0.18 on B-C and B.

**Their place.** A witness only, on every kind of page (15 Nov: never a basis).

## How the lists were made

**Grades.**
- Per scan, from `HANDWRITING_INVENTORY_20261114.tsv`: five scans per cote, plus the run rows of A and B pages.
  Typed scans come from the API typed inventory and from the Codex-web typed batches A–C.
- The 37 cotes outside the inventory were graded by a look at contact sheets: three bands per cote, in
  `hua_quality_20261114/cs/`.
  - T: 4, 24, 25, 134-3 to 134-7.
  - C: 5–9, 16, 44, 47, 54, 100, 140-1, 141, 142, 144, 146–148.
  - B-C: 140-2 to 140-4, 143, and the *Dérivateurs* 157-1 to 157-5 (his 1990 hand, letters reduced to strokes, like
    the 1986 series).
  - D: 145 and 149 (faint pencil).
- **The grade is per cote, with run overrides.** A C cote can hide typed or neat pages, so grades are good per cote,
  not per page.

**Blanks.** A scan is blank when it lies in a built package's range but not in that package's scans zip (the builder
drops blank scans). For cotes with no built package (157-x, 24, 25, 119), blank pages are still counted.

**Ours** means any of:
- a Pro package returned, or sent (`SENT_PACKAGES.txt`, `returns/`);
- a Codex-web folder returned (A, B, C, H);
- the API typescripts: *Pursuing Stacks*, *Esquisse*, and pilots of 24 and 25;
- the *Longue Marche* readers: 140-1 to 140-4, all scans covered by returned packages.

**Hua** has, per scan, one of three states, as in `route_jh.py`: transcribed, description only, or absent.

**Tiers.**
1. **Nobody:** no text from Hua and none from us. If a human edition exists, the tier is **1b** instead.
2. **Hua's weak draft only:** grades D, C, B-C.
3. **Hua usable:** grades B, A, T.
9. **Ours.** Not listed.

| Tier | D | C | B-C | T | Total pages |
|---|---|---|---|---|---|
| 1, nobody | 138 | 1,181 | 39 | 115 | **1,473** |
| 1b, a human edition only | — | 86 | 2,135 (*Dérivateurs*) | 458 (EGA V 24, 25; *Esquisse* 119) | 2,679 |
| 2, Hua's weak draft only | 596 | 5,506 | 794 | — | **6,896** |
| 3, Hua usable | — | — | — | 80 | 80 |
| 9, ours | 173 | 1,474 | 1,894 | 891 T, 76 B, 74 A | 4,582 |

The 1,181 C pages of tier 1 are mostly stretches of cotes Hua's batches do not reach. For example, of cote 136 Hua
has 247 pages; 116 non-blank scans have nothing from anyone.

## List 1: Pro packages, hardest never-transcribed first

**Order.**
- **Class 1:** packages with 10 or more pages nobody has transcribed. Sorted by the main grade of their pages (D,
  then C, then B-C), then by the number of such pages.
- **Class 2:** the rest. Same grade order, then by size.
- Each package's pages are split as follows: *nobody* = no text anywhere; *Hua* = only Hua's weak draft.

**Class 1, in full (59 packages, 2,562 pages, of which 933 are transcribed by nobody):**

| # | Package | Grade | Pages | Nobody | Hua only | Note |
|---|---|---|---|---|---|---|
| 1 | 174_MPL_154_127-176 | D | 50 | 24 | 26 | pseudo-lines, colour drawings; Hua describes the drawing pages |
| 2 | 173_MPL_154_077-126 | D | 49 | 23 | 26 | same |
| 3 | 83_MPL_14_087-132 | D | 41 | 13 | 28 | algebraic cycles |
| 4 | 81_MPL_14_002-044 | D | 40 | 12 | 28 | |
| 5 | 145_MPL_72_035-081 | D | 47 | 11 | 36 | regular polyhedra |
| 6 | 202_MPL_91_099-143 | D | 38 | 11 | 27 | Néron, faint pencil |
| 7 | 66_MPL_134-8_043-087 | C | 44 | 43 | 1 | his notes on computer-listing paper (SGA 7 IX, XIII); in no edition |
| 8 | 50_MPL_93_002-046 | C | 42 | 30 | 12 | |
| 9 | 211_MPL_33_098-146 | C | 49 | 24 | 25 | SGA 1965 draft |
| 10 | 210_MPL_33_050-097 | C | 48 | 24 | 24 | |
| 11 | 186_MPL_84_146-193 | C | 48 | 24 | 24 | |
| 12 | 92_MPL_15_195-228+18_002-017 | C | 49 | 23 | 26 | motives |
| 13 | 209_MPL_33_002-049 | C | 48 | 23 | 25 | |
| 14 | 95_MPL_136_095-141 | C | 46 | 22 | 24 | De Rham |
| 15 | 90_MPL_15_087-138 | C | 48 | 21 | 27 | |
| 16 | 97_MPL_136_189-234 | C | 45 | 20 | 25 | |
| 17 | 138_MPL_11_002-042 | C | 39 | 19 | 20 | |
| 18 | 73_MPL_105 | C | 48 | 18 | 30 | Champs 2 |
| 19 | 98_MPL_136_235-281 | C | 46 | 18 | 28 | |
| 20 | 93_MPL_18_018-062 | C | 45 | 18 | 27 | |
| 21 | 230_MPL_57_226-270 | C | 43 | 18 | 25 | Picard |
| 22 | 141_MPL_60_036-070 | C | 35 | 18 | 17 | |
| 23 | 212_MPL_33_147-181+34_002-017 | C | 49 | 17 | 32 | |
| 24 | 96_MPL_136_142-188 | C | 46 | 17 | 29 | |
| 25 | 140_MPL_60_002-035 | C | 34 | 17 | 17 | |
| 26 | 94_MPL_136_047-094 | C | 46 | 16 | 30 | |
| 27 | 74_MPL_106+107 | C | 41 | 16 | 25 | Champs 3 (listings) |
| 28 | 193_MPL_45_033-080 | C | 39 | 16 | 23 | |
| 29 | 139_MPL_11_043-058+56 | C | 50 | 15 | 35 | |
| 30 | 156_MPL_93_221-236+161-5 | C | 43 | 15 | 28 | |
| 31 | 223_MPL_131 | C | 38 | 15 | 23 | |
| 32 | 220_MPL_122 | C | 32 | 15 | 17 | |
| 33 | 91_MPL_15_139-194 | C | 45 | 14 | 31 | |
| 34 | 218_MPL_36_053-085+39 | C | 49 | 13 | 36 | |
| 35 | 232_MPL_62_002-050 | C | 46 | 13 | 33 | |
| 36 | 231_MPL_57_271-315 | C | 43 | 13 | 30 | |
| 37 | 194_MPL_46_002-048 | C | 42 | 13 | 29 | |
| 38 | 246_MPL_2 | C | 41 | 13 | 28 | Riemann-Roch |
| 39 | 199_MPL_90+91_002-018 | C | 39 | 13 | 26 | |
| 40 | 217_MPL_36_002-052 | C | 31 | 13 | 18 | |
| 41 | 80_MPL_133 | C | 50 | 12 | 38 | |
| 42 | 206_MPL_31_002-051 | C | 46 | 12 | 34 | |
| 43 | 190_MPL_43_094-142 | C | 46 | 12 | 34 | |
| 44 | 60_MPL_22+23_002-016 | C | 44 | 12 | 32 | 22 is a typescript (Hua T, 1.3) |
| 45 | 185_MPL_84_097-145 | C | 48 | 11 | 37 | |
| 46 | 88_MPL_12_150-168+15_002-033 | C | 45 | 11 | 34 | |
| 47 | 99_MPL_136_282-327 | C | 45 | 11 | 34 | |
| 48 | 198_MPL_58_020-067 | C | 44 | 11 | 33 | |
| 49 | 227_MPL_57_089-132 | C | 43 | 11 | 32 | |
| 50 | 117_MPL_83_178-222 | C | 43 | 11 | 32 | |
| 51 | 204_MPL_98 | C | 43 | 11 | 32 | |
| 52 | 152_MPL_93_047-091 | C | 42 | 11 | 31 | |
| 53 | 101_MPL_138_046-089 | C | 42 | 11 | 31 | |
| 54 | 70_MPL_116+117 | C | 34 | 11 | 23 | |
| 55 | 224_MPL_130 | C | 44 | 10 | 34 | |
| 56 | 228_MPL_57_133-179 | C | 43 | 10 | 33 | |
| 57 | 69_MPL_108+112+113+114+115 | C | 40 | 10 | 30 | |
| 58 | 249_MPL_129_077-115 | C | 37 | 10 | 27 | |
| 59 | 169_MPL_71 | B-C | 41 | 14 | 27 | all 41 pages also in batch J |

**Class 2: 141 packages, 5,728 pages, of which 450 are transcribed by nobody.**
- Order: the D packages first (12 packages: 91, 72, 14, 154, 69, 68, 81), then 114 of C, then 20 of B-C.
- The full order is in `PRIORITY_FOR_PRO_20261114_PACKAGES.tsv`.

**Overlap with Codex-web batch J.** These 21 Pro packages cover the same pages as J:
- 84_MPL_13, 196_MPL_53+55, 169_MPL_71, 107_MPL_70_110-126+75 and 171_MPL_80_057-073+81_002-037;
- part of 172_MPL_81_038-055+154_046-076;
- the 15 packages of 156-3 to 156-9: 124–131 and 162–168.

If J runs on Codex web, these drop out of the Pro order, except the 154 part of package 172.

**Hard pages with no Pro package yet** (2,863 pages in all):

| Pages | Grade | What | Others' text |
|---|---|---|---|
| *Dérivateurs* 157-1 to 157-5: 2,135 | B-C | his 1990 hand | a human edition (Künzer, Malgoire, Maltsiniotis, online; not checked here). No package |
| 134-2: 37 | C | the handwritten leaves of the *Pursuing Stacks* dossier not in packages 58/69 | |
| 134-8: 2 | C | | |
| 162-5: 9 | C | | |
| 147: 1, 129: 1 | C | stray scans | |
| 119: 35 | C | the *Esquisse* dossier's handwritten pages | |
| 129: 74 | T | Hua only describes these | |
| 24: 73 and 25: 179 | T | EGA V typescripts | partial human editions (Blass translations; the web edition of EGA V) |
| 119: 243 | T | *Esquisse* dossier typescripts | the *Esquisse* edition covers only part |
| 134-2: 26 | T | | |
| 162-5: 45 | T | | |

So **the hardest pages without a package are the *Dérivateurs*.** Whether to transcribe them depends on the existing
edition; that is a question for the Dérivateurs field expert.

## List 2: Codex-web folders (GPT-6 Astra at reasoning effort max)

**Evidence that Codex web can do the hand** (`SPOT_CHECK_H_20261114.md`, 23 pages graded by eye, 0.18 errors per 100
words in all):
- **B-C, high.** 156-7 #2–9: 3,253 words, 0.18. Then one page each, all with 0 errors: 13 (his English notes), 103
  (letter to Deligne), 104 (Champs 1), 66, 162-1, 134-1, 134-2 (letter copies).
- **B, medium.** Six pages of fair hands and lists, 0.17. One pencil sheet, 162-6 #6, gave 4.4.
- **A/T, high.** The typed route of batches A–C.
- **C, D: no evidence.** The C pilot HC1-01 is built but not sent. **These go to Pro**, as in list 1.
- **How far the evidence reaches.** It is strongest for the 1986 series (156-x), the hand it was tested on. It also
  covers his other spaced letters and notes, one page each. The *Dérivateurs* hand of 1990 looks like the 1986 hand on
  the contact sheets but has not been tested.

**Order: largest shortfall in Hua's text first, then confidence.**

| # | Pages | Grade | Hua's shortfall | Confidence | Folders | Allowance at 0.5 % a page |
|---|---|---|---|---|---|---|
| 1 | B-C pages with no text from anyone: 39 (13, 53, 71, 75, 81, 156-8, 156-9; one page of 155) | B-C | total | high | 38 pages already in J folders (see the `codex_web_folder` column); 1 page new (155) | 20 % |
| 2 | Typed pages with no text and no edition: 115 (129: 74, 134-2: 19, 162-5: 14, 15: 5, 37: 2, 12: 1) | T | total; Hua only describes 129 | high | about 15 new folders | 58 % |
| 3 | B-C pages where Hua has only a draft: 794 (13, 53, 71, 75, 81, 156-3 to 156-9) | B-C | 1.4 errors and 2.0 gaps per 100 words; margins in fragments | high (156-x); medium (13, 53, 71, 75, 81) | **the existing J folders** (109 folders, 832 pages with item 1) | 397 % |
| 4 | *Dérivateurs*: 2,135 | B-C | total (no Hua) | medium: hand like 156-x, not tested | about 267 new folders | about 1,070 % (10.7 weeks) |
| 5 | Typed pages with partial human editions: 458 (EGA V 24, 25; 119; 134-4) | T | total (no Hua) | high | about 57 new folders | 229 % |

**What stays off Codex web:**
- **Typed pages where Hua has text** (grades A and T, 80 pages in tier 3, and the typed parts of C cotes): Hua's text
  plus a check is cheaper, about 0.3 % a page.
- **All C and D pages** go to Pro (list 1) until a Codex-web C pilot (HC1-01) is graded.

**For the second account,** in the order of the table:
- Items 1–3: about 4.75 weeks of allowance.
- Item 4: about 10.7 weeks. It decides between itself and the Open Logic translations; the existing *Dérivateurs*
  edition should be weighed first.

## Caveats

- **Grades are per cote**, from five scans or three bands a cote. A C cote can contain typed or neat pages, and those
  are listed here as C.
- **"Nobody" counts only what we hold.** It does not count transcriptions by others beyond the editions named
  (Pursuing Stacks, Esquisse, EGA V, Dérivateurs, the Longue Marche witnesses). The Grothendieck Circle and CSG have
  transcribed some letters; the edition check (`EXISTING_EDITIONS_CHECK_20261112.md`) lists those it found.
- **Blanks.** For the 157 cotes, 24, 25 and 119, blank scans could not be removed, so their page counts are upper
  bounds.
