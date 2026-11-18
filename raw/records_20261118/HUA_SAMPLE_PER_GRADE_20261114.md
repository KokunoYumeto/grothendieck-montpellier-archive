# Michel Hua's first pass by hand grade, and batches J and H routed against it

> **Correction, 15 Nov 2026 ~10:5x UTC (the user, through the coordinator):** Michel Hua's text is never used as the basis of a transcription. It may serve as a witness only. Every page is transcribed from the scans. The 80 grade-T pages once routed "Hua + check" (cotes 25, 119, 134-2, 162-5) had already been transcribed from the scans over the API on 12-13 Nov (Claude Opus 5.5 at effort high, Message Batches), and no folder, package or prompt ever started from his text. The verdicts "(i) basis" below are withdrawn. The text as it was is in `HUA_SAMPLE_PER_GRADE_20261114_before_no_basis_20261115.md`.

14 Nov 2026, Claude Opus 5.5 at effort high (Claude Code sub-agent, effort set at launch), at the brief
`BRIEF_HUA_SAMPLE_PER_GRADE_20261114.md` of the main session (Claude Opus 5.5 at effort max).

**Their text.** Commutator-IO/grothendieck-project, commit `aef7db2`. By its file headers, it was transcribed by
Claude Opus 5 and Claude Opus 5.5 in Sept–Oct 2026 and read again in part by Claude Fable 5.2 in Nov; efforts not
recorded. Their page n is our scan n+1. The earlier whole-text check is in `HUA_TRANSCRIPTION_QUALITY_20261114.md`.

**How Codex web is costed here.** Codex web is GPT-6 Astra at reasoning effort max, on the second account. Its
error rate is 0.18 per 100 words: batch H, 23 pages graded by eye in `SPOT_CHECK_H_20261114.md`. Its cost is 0.5 % of
a weekly allowance per page (measured: 39 % for 86 pages). Of the 4–5 minutes a page takes, the second reading is
2.5–3, so a check of an existing text is estimated at 0.3 % a page.

## Verdict per grade

| Grade | What | Hua, errors per 100 words | Hua, readable words left as gaps per 100 | Verdict | Checking Hua's text against a new Codex-web transcription |
|---|---|---|---|---|---|
| **A** | Typescripts typed by others, and his typed letters (97, 37) | **0.5**. No misreading: «» for "...", his ink tagged as the transcriber's supply, a typed-over word left out | 0 | **(i) basis**: withdrawn 15 Nov, a witness only | **Cheaper.** About 0.3 % a page against 0.5 %, for the same final quality. The fixes are conventions: the quote marks can go by script, and the rest is a light check |
| **T** | His typescripts with his ink corrections (22, 10, 57) | **1.3**. All of them in his ink: corrections of numbers missed, struck spans given live, insertions misplaced or left out. The typed body is right | 0 | **(i) basis**: withdrawn 15 Nov, a witness only | **Cheaper**, about 0.3 % against 0.5 %, but only if the checker reads every correction on the scan. That is where all the errors are, and they carry no doubt mark |
| **B** | Fair hands of others (Brown, 109) and his clear letters and lists (13 Mumford letter, 26) | **1.4** (0.7 without quote marks). Others' hands: only «». His letter 13 #19: 4 errors in 60 words, unmarked | 0.2 | **(ii) marked draft** | **Not cheaper.** Every handwritten line must be read again, so the check costs a reading, and its misreadings are unmarked. A new Codex-web transcription reaches 0.18 |
| **B-C** | His spaced hand of 1976–86 (the 1986 series 156-x, 150, 81): **all of batch J** | **1.4**. Of the 7 errors, 3 carry their doubt mark | **2.0**, plus slanted margin notes given as fragments | **(ii) marked draft** (a second witness) | **Not cheaper.** About 2 readable words in 100 are gaps, and the margin notes need a full reading, so the check is a new transcription. A new Codex-web transcription gives 0.18 for 0.5 % |
| **C** | His working notes (19, 34, 12). From the first check, dense pages of 142, 147 and 149: 3–8 errors | **1.5** on these pages (3–8 on dense pages) | 1.1 (about 3 on dense pages) | **(ii) marked draft** | Not cheaper, for the same reason |
| **D** | Faint pencil and drawings (69, 91, 154) | **2.2**. Text not on the page (*est tel que*), live text given as struck, *induisant* for *invariante*; half of the errors carry a doubt mark | 1.9 | **(iii) not to be used** as a basis. As a witness its noise is too high | Not applicable |

**The sample.**
- **Size.** 36 pages, 2,969 words: six per grade (five for D, seven for B-C with 156-7 #3 from the first check).
- **Which pages.** Middle and end of three cotes per grade, read by eye against the archive scans. Only a band of each
  page was read, its top 30–50 %, 20–190 words.
- **Exception, A.** Grade A has only two cotes with Hua's text. Of the inventory's grade-A pages, Hua gives
  descriptions only for 63 (Tate's formulaire and its typescript) and 109 #13–38. So 37's typed letters stand in for
  a third cote.
- **Per page:** `hua_quality_20261114/sample_per_grade.tsv`, which also gives the second witness where one exists.
  For 13 #19, Codex web H13-01 reads "relative motive over the complex analytic space" where Hua has "relative complex
  analytic space over the corresponding [ill]". For 156-7 #3 the witness is H156-01.
- **How firm the rates are.** Each grade has 3–12 errors, so a rate per grade is good to about a factor of 2. The
  order is firm: typescripts best, his own hand worse, pencil worst.
- **His own hand.** The grade does not say everything. His hand in a clear letter (13 #19) erred as often as his
  working notes did.

**What this means.**
- **Typed material.** Hua's text is as good as or better than our Pro first pass (about 1 per 100 words). Started
  from with a check of the ink marks, it saves about 40 % of a new Codex-web run. (Withdrawn 15 Nov: never a basis; a witness only.)
- **Everything handwritten.** It is a draft and a second witness, not a basis. Its gaps and margin notes must be
  read anyway, and a new Codex-web run is about eight times as accurate (0.18 against 1.4).

## Batches J and H against Hua (`codex_web_20261113/BATCH_J_H_VS_HUA_20261114.tsv`)

**Method.**
- One row per folder of `ASSIGNMENTS.tsv`, giving: cote, scans, grade, and Hua's coverage per scan (transcribed /
  description only / absent).
- A scan counts as covered only when Hua's page holds transcribed text, not only a `\note` or `\drawing`
  description.
- **The routes:**
  - `hua+check`: start from Hua's text and check it, for grades A and T;
  - `both`: Codex web, with Hua's text attached as a marked draft, for B, B-C and C;
  - `codex_web`: for D, or where Hua has no transcribed text.

  A folder only partly covered is routed by its covered pages, and its rest goes to Codex web.
- Script: `hua_quality_20261114/route_jh.py`.

| Batch | Route | Folders | Pages | Pages with Hua text | State | Weekly allowance at 0.5 % a page |
|---|---|---|---|---|---|---|
| **J** (all grade B-C: 156-3 to 156-9, 13, 53, 71, 75, 81) | **both** | **109** | **832** | 794 (38 with descriptions only or absent) | built, not sent | **416 %**, about 4.2 weeks |
| H | both | 21 | 153 | 139 | returned, except HC1-01 (8 pages of grade C, cote 1: built, not sent, 4 %) | spent (HC1-01: 4 %) |
| H | codex_web | 8 | 61 | 0 (Hua describes 63 and most of 109; he does not transcribe them) | returned | spent |
| H | hua+check (on its Hua pages) | 4 | 32 | 13 (63 #96–100, 97) | returned | spent |

**For the choice between batch J and OLP on the second account:**
- **Hua's text frees no Codex-web allowance in batch J at our quality bar.** All of J is grade B-C, where Hua's text
  is a draft (1.4 errors and 2.0 gaps per 100 words, margins in fragments) and checking it costs as much as a new
  transcription.
- **So the choice is between two things:**
  - **Run J:** about 4.2 weeks of the second account's allowance, for about 0.2 errors per 100 words, with Hua's text
    attached as a second witness.
  - **Keep Hua's text** as the reading text of the 1986 series for now, and give the allowance to the Open Logic
    translations.
- **Where Hua's text would save allowance** is the typed material, grades A and T. In J and H that is only 13 pages,
  already returned. It applies instead to the typescripts still in the waiting Pro packages and future Codex-web
  folders, such as cotes 10, 21, 22, 27, 32 and 57. For those, Hua's text plus a check of the ink marks is the cheaper
  route.

## The two places of our second pass

- **142 #30**, *on trouve les équations*. Hua gives *les* struck. On the scan (crop
  `hua_quality_20261114/smp/z142_030.jpg`) no stroke crosses the word; only its final *s* has an overwrite blot.
  **Our reading (*les*, not struck) stands, and Hua's is wrong.** Whether the *s* was corrected cannot be decided.
  No correction.
- **149 #40**, *Dans le cas du genre 1, on en conclut ___ que*. Ours had *au moins*, Hua *maintenant*. The scan
  (crop `z149_040.jpg`) shows one long word with a t-stroke in the middle and a final -nant; there is no gap for two
  words. **Hua is right; ours was wrong.** Corrected in `second_pass/out/MPL_149_001-090/MPL_149_001-090_scan040.tex`
  and logged, with credit to Hua's transcription, as a new section "Later correction (14 Nov 2026)" (confidence high)
  of `MPL_149_001-090_037-054_changes.md`.

## Files

- **This report:** `HUA_SAMPLE_PER_GRADE_20261114.md`.
- **The page table:** `hua_quality_20261114/sample_per_grade.tsv`.
- **The bands read:** `hua_quality_20261114/smp/`.
- **The routing:** `codex_web_20261113/BATCH_J_H_VS_HUA_20261114.tsv`.
- **Scripts in `hua_quality_20261114/`:**
  - `band.py` cuts the bands from the archive PDFs;
  - `hua_pagelist.py` lists Hua's pages with word and mark counts;
  - `route_jh.py` builds the routing.
