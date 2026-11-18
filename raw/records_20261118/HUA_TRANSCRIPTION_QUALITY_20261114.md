# Quality of Michel Hua's first-pass transcriptions of the Montpellier archive

14 Nov 2026, Claude Opus 5.5 (the agent that built and checked the Codex-web batches; launched at effort high, this
session's effort not set separately), for the main session (Claude Opus 5.5 at effort max), at the user's word: "Check
quality. If it's good, we'll use that as a basis for our second pass."

**Their text.** Commutator-IO/grothendieck-project, shallow clone of 14 Nov 12:50, commit
`aef7db2b760a4cda7bd97283f2d44233dd4d4db8`, in `C:\Users\user\Documents\ai_math_sources_20261114\hua_michel\
commutator_grothendieck-project\transcripts\`. Their page n is our scan n+1; I checked this on 142, 147, 149 and
156-7 by content.

**How their text was made.** By their file headers, the pages of 142, 147 and 149 were first passes by Opus 5.5
(claude-opus-5-5, effort not recorded) of 2–10 Oct 2026. Fable 5.2 (claude-fable-5-2, effort not recorded) read them
again on the facsimile on 12–14 Nov, which is in this clone. Their reader Michel Hua made a few place checks (#115,
#127, #145).

**Scripts and data** are in `hua_quality_20261114\`. They read files only.
- `align_hua.py`: a word alignment of the three texts, giving `pages.tsv` and `blocks_*.tsv`.
- `align_h156.py`: 156-7 against our graded Codex-web return.
- `witness.py`: Hua as a witness for our second-pass corrections.
- `coverage.py`: their pages against our routes, giving `coverage.json`.
- `show.py`: prints the three texts of a page.
- `halves.py`: page images from the archive PDFs.
- `img\`: those page images.

## 1. 142, 147, 149: their first pass and our Pro first pass against our checked second pass

**Method.**
- **Prose words only.** Mathematics, TikZ, diagram contents and editorial notes are dropped. For a doubt mark, the
  first reading counts.
- **Deletion flags.** Each word carries a flag for whether it is struck.
- **The alignment** is difflib's, per page.
- **The sample.** 381 pages are in all three texts. Seven of their pages are missing (142 #1, 2, 22, 66, 105, 107, 109;
  149 #1, 2); most are covers or blank.

| 381 pages, 43,062 words of our second pass | Words that differ, per 100 | Struck/live mismatches, per 100 | Doubt marks per 100 words |
|---|---|---|---|
| **Hua first pass** | **24.6** (142: 28.3; 147: 24.3; 149: 22.0). Per page: median 18, 10th–90th percentile 7–48 | 0.56 | 3.8 `\uncertain` + 3.2 `\ill` (1,598 + 1,341) |
| **Our Pro first pass (GPT-6 Astra, ChatGPT Pro mode)** | 0.92 | 0.06 | 3.3 `\unsure`, 0 `\illegible` (1,402) |

**Our second pass is built on the Pro text, so this comparison flatters Pro.** The second pass is the Pro text
corrected line by line by Claude Opus 5.5 at effort max, so an error Pro made that the second pass missed counts as
agreement. The independent rates for Pro on the same packages, from the sample checks in `returns\*_check\` (scored
against the scans), are:
- 142: 1.56 and 0.65 errors per 100 words;
- 147: 0.73, 2.15 and 0.38;
- 149: 0.52 and 1.03.

So **Pro makes about 1 error per 100 words, and Hua's text differs from the checked text on about 25 words in 100.**

### By eye, against the scans

I classified the disagreements by eye on five pages, chosen across the range of disagreement. I used the package
images in `second_pass\img\`; for 156-7 #3, the crops of `done\H156-01`.

| Page | Words | Hua errors (high and medium confidence) | Of which unmarked | What went wrong | Second pass right? |
|---|---|---|---|---|---|
| 142 #30 (a light page, 13 % disagreement) | 121 | 4 | 4 | *ici* for *en fait*; *correspondantes* for *constitutives*; *Les* for *les*; *pts* given live where it is struck | the second pass may be wrong once: *les* before *équations* looks struck, and Hua has it struck. Four places do not decide |
| 142 #100, top half (57 %) | ~110 | ≥ 8 | 2 | *quand*, *soit*, *dégager*, *cohomologie*, *peux me borner* for *que ces conditions*, *si on veut sont suffisantes*, *me rapprocher du point où*, *finira par apparaître*, *pense surtout*; struck *paraît* left out; the slanted margin note is nearly all `\ill` and its words differ | yes, where the ink decides |
| 147 #80 (69 %) | 123 | ≥ 8 | most | *qui se réduisent à un morphisme* for *ceci est une équivalence*; *généralisation* for *générisation*; whole clauses rewritten | yes |
| 149 #40 (16 %) | 132 | 5 | 2 | *montre* for *marche dès*; *s'envoie* for *s'injecte*; *exclu par* for *est le cas grâce à*; *autom.* expanded | maybe twice wrong: *au moins* (Hua: *maintenant*, which the ink seems to favour); *Idem, en remplaçant* (Hua: *dans ces arguments*) does not decide |
| 156-7 #3, against the Codex-web return H156-01 | 209 | 5 + a 60-word margin note given as fragments | 3 | *figures* for *lieux*; *étant* for *est*; *ne permettant* for *ne permet*; *reconstituer* for the written *réconstituer*; a clause given as `\ill` | Codex H156-01 is the reference (0.18 errors per 100 words by eye) |

**Rate.** On these pages Hua's first pass makes about **3–8 errors per 100 words**, plus about 3 `\ill` gaps per 100
words where our texts read the words. Between a third and a half of the errors carry a doubt mark.

**How the errors fall.** The script figure (24.6) counts every differing word; by eye, about a fifth to a third of
those are wrong readings by Hua. The rest are long rewritten clauses (one error, many words), places the ink does not
decide, and a few where our second pass is the one in doubt.

**For 156-7 as a whole** (scans 2–9), Hua's text differs on 54 words per 100 from the Codex-web return graded at 0.18,
with 53 `\ill` marks on eight pages. Part of that figure comes from diagram text, which the script drops from the
Codex text.

**The kinds of error, in order:**
1. **Plausible mathematical prose in place of the ink**, often whole clauses (147 #80, 142 #100). The errors are the
   expected word: grammar normalized (*ne permettant*, *étant*), a written slip corrected (*réconstituer*).
2. **Slanted margin notes reduced to `\ill` fragments.** Our texts read them.
3. **Struck text:** struck/live mismatches are 9 times Pro's rate (0.56 against 0.06 per 100 words).
4. **Abbreviations expanded** (*autom.*), **accents and ligatures modernized** (*nœthériens* and *Évidemment* on the
   typed 22 #10), and guillemets « » for his ".." quotation marks. Their preamble and notes say this is a reading
   edition, so these follow their own rules, but they are errors in a diplomatic transcription.

### As a witness

`witness.py` compares the two errors that matter for a second pass:
- **Where our second pass corrected the Pro text** (345 words), Hua's text has the corrected word in **49 %** of cases.
  Two independent readers are right together more often than chance, so Hua is a real second witness.
- **Where the Pro text was kept** (42,717 words), Hua disagrees in **17.3 %** of cases. As a pointer to Pro's errors,
  then, it flags about 7,400 places to find about 170 corrections: about 2 % precision.

## 2. Other cotes that only they transcribed

One page from each of three cotes of different kinds, against the archive PDF:

| Page | Kind | Words | Hua errors | Notes |
|---|---|---|---|---|
| 22 #10 (their p. 9) | typescript with his corrections (EGA) | ~330 | 2 (both modernizations: *nœthériens*, *Évidemment* for typed *noethériens*, *Evidemment*) | Good. The typed-over words, his insertions, the corrected labels (i)/(i bis), the circled clauses and the small diagram are all right; a vertical margin note is `\ill` |
| 53 #10 (p. 9) | his note on algebraic groups, a clear spaced hand | ~230 | 2–3 | Good. *[platitude ⇒ p ouvert + p fermé]* lost *platitude ⇒* (OM); a struck *les ensembles* is left out; one struck/live place does not decide |
| 13 #30 (p. 29) | his motives notes, a fast hand with formulas | ~200 | 4 + about 12 `\ill` | Weak. `\overline{\psi}=\psi^{-1}` for the written T̄^{pq} = T^{qp} (MS); *isom.* for *point* (MW); *sont des* for *définissent les* (MW); *variables* dubious |

Their accuracy depends on the hand. On typescripts and clear hands it is good: about 1 error per 100 words, about
Pro's level, but with modernizations. On his fast and his late hands it is several times worse than Pro and about
twenty times worse than Codex web at effort max.

## 3. Coverage

Their 165 folders hold 9,420 pages (`coverage.json`). Against our routes:

| Our route for those scans | Their pages |
|---|---|
| Pro packages not yet sent (184 packages touched; for example 79 → packages 51 and 109–113, 136 → 49 and 94–100, 57 → 225–231, 93 → 50 and 152–156) | **6,297** |
| Codex-web batch J (156-3 to 156-9, 13, 53, 71, 75, 81) | **804** |
| Other Codex-web folders (A, B, C, H) | 498 |
| Pro packages sent or returned | 456 |
| Not in the numbered packages of PLAN.json (cote 1 and other folders handled before the plan, or scans the plan left out) | 1,365 |

## 4. Verdict and proposal

**Verdict: not good enough to be the basis of our second pass.** The basis has to be at least as good as what we
would otherwise produce.
- **Their rate.** On the pages where all three texts exist, their first pass makes several times Pro's error rate
  and leaves about 3 words in 100 unread where we read them. Its errors are the kind a diplomatic second pass most
  fears: plausible clauses in place of the ink, modernized spelling, struck text given live.
- **Correcting it means re-reading it.** A second pass over their text would have to re-read nearly every line from
  the scan. That is a first pass, done with a misleading draft beside it.
- **Codex web is cheaper and better.** It now does a first pass at about 0.2 errors per 100 words, for 0.29 % of a
  week per page. So starting from their text saves no work: the 804 batch-J pages and the 6,297 waiting-Pro pages
  should be transcribed by us as planned.
- **The exception: typescripts and clear hands.** There (22, 53) their text is about as good as Pro's, and could be
  checked rather than redone. But our typed route through Codex web is cheap and already better, so this exception
  is not worth a separate workflow.

**Proposal:**
1. **Use their text as a witness, not as the base.** Give it to our second-pass reader beside our first pass, as the
   prompts already allow a draft: transcribe from the ink, consult the draft only after, and where they differ the
   ink decides or both readings go in `\unsure{ours|theirs}`. Measured value: it holds about half of the corrections
   our second pass made. It also flags too much (17 % of correct words) to be used as a list of places to check.
2. **Mapping of their marks to ours:**
   - `\uncertain{x}` → `\unsure{x}`;
   - `\ill{}` → `\illegible{1}` (they give no word count);
   - `\struck{x}` → `\deleted{x}`;
   - `\add{x}` → `\inserted{x}`;
   - `\marginal{x}` → `\margin{x}`;
   - `\supplied{x}` → a `%` comment, never text;
   - `\note{x}` → a `%` comment;
   - `\drawing{description}` → our `\figure` must be redrawn in TikZ;
   - their « » → his ``...'', and their modernized accents → the page's own spelling.
3. **Packages.** No new package type is needed. Where a waiting Pro package or a Codex-web folder covers a cote they
   have transcribed, their batch files can go in as `DRAFT_HUA_<cote>.tex` with the "attached draft" section of
   `codex_web_20261113\tools\PROMPT_TEMPLATE_HANDWRITING.md` (built for the Breen letters). Do that first on a pilot
   folder and measure whether it lowers our error rate, before adding it everywhere; an extra draft can also pull a
   reader towards its errors.
4. **Saving: none in Pro or Codex-web runs.** The gain is accuracy at the second pass, not work avoided.
5. **Credit.** Their text is not ours to license (`RIGHTS.md`: transcripts are "not ours to license"), so nothing from
   it is published. Where a reading of ours was settled with their help, the edition notes say so, by name and
   source. For example: "reading compared with the transcription of Michel Hua and the Commutator project
   (github.com/Commutator-IO/grothendieck-project, transcripts/142/batch-02.fr.tex, commit aef7db2), first pass by
   Claude Opus 5.5, revised by Claude Fable 5.2 (efforts not recorded)". The same line goes in each package's README
   and in the edition's sources list.

**Note on our own second pass.** In the eye sample, our second pass of 142, 147 and 149 may be wrong at two or three
places where Hua agrees with the ink: 142 #30 *les* struck, and 149 #40 *au moins* (Hua: *maintenant*). That is two or three
places in the roughly 500 words of those pages that I checked by eye: a small sample, so it gives no rate for the
second pass. The two places go to the
second-pass notes as items to recheck.
