# The Claude second pass of the Montpellier transcriptions: an audit of the method (17 Nov 2026)

> **Correction notice, 17 Nov 2026 (night), at the user's word. Read `METHOD_AUDIT_2_20261117.md` with this file.**
> - **Recommendation 1 is withdrawn.** That is the blind reading by another model family before the Claude pass:
>   section 0 item 6, section 5.1 C1, the arms A1 and D-blind in section 6, and the related lines of 5.3. The first
>   pass, GPT-6 Astra (ChatGPT Pro mode), already is the other family's reading. Its doubt marks, doubt files and
>   notes are the place list the second pass did not work through. Codex and Pro readings for Codex-transcribed
>   (Astra Max) pages stay as already planned. The user: "You have a reading, you just never used it. ... you need to
>   work through the math."
> - **Pro's notes were used.** On 17 Nov, 02:00-05:13 UTC, a9ebc3d6 (Claude Opus 5.5 at effort max) triaged them in
>   three passes: 56 research items routed to the waiting prompts, FOR_ASTRA and the notes; about 710 edition matters
>   to the second pass. Where this file says the notes are "checked for their quotations, not processed" (section 0
>   item 4, section 3.2), that holds for the second pass only. What the triage did not do (check the notes'
>   mathematics, their readings, their references, and its own 3,812 "nothing" verdicts) is measured in audit 2,
>   section 1.
> - **The "about 1,200 unresolved places"** in this file are the second pass's own unresolved lists, not Pro's marks.
>   Pro's marks are counted in audit 2: 631 doubt marks on five blocks, 79 % left exactly as Pro left them.
> - The rest of this file (the measured error rates, the error types, the mathematical-reading findings, the
>   priority) stands. The improved method is replaced by audit 2, section 5, and by
>   `PLAN_MATH_THIRD_PASS_20261117.md`.

Written by Claude Opus 5.5 at effort max (agent a7d5d89d, no sub-agents) on the brief of the main session (Claude
Opus 5.5 at effort max), at the user's word of 17 Nov ~22:4x UTC: "We need to audit the method. We're not cheap."
Two additions from the user came in while I worked, and both are answered here:
- the second pass is also mathematical reading (section 4);
- the idea of a dual second pass by two models at once (section 5.3).

**How to read the marks:**
- **[measured]** means I computed or checked it myself for this audit. The scripts are in my scratchpad:
  `sp_stats.py`, `sp_count2.py`, `priority_data.py`, `image_tokens.py`. I also looked at three scan crops and grepped
  the control returns and Hua's text.
- **[reported]** means it is taken from a file, with the file and its lines.

My classifications of the residual errors are listed one by one in Appendix C, so anyone can check them.

## 0. The verdict in brief

1. **The second pass is a good corrector with one systematic hole.**
   - On the two controls, it removed nearly three quarters (72 %) of the first pass's errors.
   - Its own changes are right about 95 % of the time: 3 wrong, and 1 more withdrawn by majority, out of 87 on the
     control pages.
   - What survives is mostly fluent first-pass words that it read with the first pass's text in view and accepted
     without a mark.
   - **[measured]** The residual errors, after the controls' corrections and scan checks, are 29 in 5,619 words:
     **0.52 per 100 words, of which 0.36 unmarked.** Of the 29:
     - 26 are inherited from the first pass;
     - 19 sit at places where the second pass recorded neither a change nor a doubt;
     - 3 were introduced by the second pass, one of them a polarity reversal that was reported as consequential.

   These are lower bounds (section 2.1).
2. **The causes are in the method as written, not in the agents.**
   - The block prompt sets up a verification of a given text. "Compare every word" is done with the first pass beside
     the image.
   - It caps the work: "make an enlarged crop only where the first pass and your reading still disagree", and "no more
     than about 120 tool calls" for 15-19 scans. So where anchoring makes the checker agree, nothing triggers a closer
     look.
   - The only second witness is Michel Hua's transcription. It is read by Claude Opus 5.5, the same model as the
     checker, and it is opened only at places already in doubt.
   - The triple check of 15 Nov had already measured this mechanism: "Reading a page with our text in view lets the
     transcript's word pass when it is plausible."
3. **Adjudication by the agent that made the reading is anchored too.**
   - In the first verdict round, the judge (the same agent as the second pass) looked at the scan and kept three of its
     own wrong readings against a correct Codex reading. One of them is recorded as "checked and kept".
   - It reversed them only when a third reading agreed with Codex.
   - So the first round recovered 10 of the 16 errors that the two control readings together exposed.
4. **Pro's notes are checked for their quotations, not processed.**
   - What the second pass does: it confirms or corrects each note's anchor against the corrected text, and it adds
     notes of its own.
   - What it does not touch:
     - the notes' links to our research registers;
     - their test computations;
     - their links to other cotes;
     - the roughly 3,800 entries that the notes readers sorted as "nothing further". Many of these are known results
       named from memory, which is exactly the groundwork layer (C1) of the companion.
   - The registers were built from first-pass text and are not updated by the second-pass corrections.
5. **The mathematical reading happens, but only by chance.**
   - Some agents did real mathematics, for example 145 C4, C8 and C9, and 148 N2, N3 and N8.
   - Mathematical tension was the signal of a misreading at least twice:
     - the 053 polarity, where the agent's own note N4 saw the tension and explained it away;
     - 145 C8.
   - The prompt does not ask for this work. It does not supply the context for it (the LM text, other cotes, the
     literature, computation). It does not route the results to the companion.
6. **The improved method (section 5).** Twelve changes:
   - every page gets at least one blind machine reading from a different family before the Claude pass;
   - disagreements are read blind on native-resolution crops, before the alternatives are seen;
   - an ink-coverage step catches omissions;
   - a watch list covers the logic-bearing words (implique/indique, si/sinon, maximaux/minimaux);
   - unresolved places become data (a `PLACES.tsv` file), and are routed;
   - adjudication is not done by the reader of record;
   - a mathematical reading pass whose alarms go back to the ink, never straight into the text;
   - notes are routed to registers, with check events.

   The user's dual second pass (two models, each independently) is a candidate arm.
7. **The pilot (section 6).** It runs on the two controls with known errors. The arms are:
   - the current method replayed by a fresh agent;
   - the improved reading;
   - the improved reading with the mathematical layer;
   - the dual second pass;
   - the four Sol third-pass variants already built (V1-V4).

   A grader who made none of the readings scores them, blind, on one table: errors caught, errors introduced, scan-check
   load, cost, and the mathematical findings.
8. **Priority (section 7).** Waves in this order:
   - first, re-pass cote 149, then 147/003-137, then 142. They carry the companion's heaviest chapters and were done on
     13 Nov under the oldest method.
   - then the unpassed tower cotes 144, 146 and 147/138-190;
   - then the much-cited small cotes 44, 47 and 54;
   - then the packages whose notes most feed our runs.

## 1. How the second pass is done now (from the files)

### 1.1 Versions and runs

| When | Blocks, scans | Cotes | Instructions the agents had |
|---|---|---|---|
| 13 Nov: pilot, waves 2-3 | 23 blocks, 390 scans | 142, 147/003-137, 149 | The block prompt from `make_second_pass.py` only. No witness, no edition matters. |
| 17 Nov: pilot | 3 blocks, 50 scans | 141, 143 | Block prompt plus four additions in the launch brief: Hua as a witness for unresolved places, the cote's conventions, a precise notes check, consequential corrections in the final message. |
| 17 Nov: waves 1-2 | 24 blocks, 368 scans | 145, 148, 16, 150, 151, 152, 120 | As the 17 Nov pilot. Edition-matters step 5 where a file exists. |

**[reported]** Sources for the table:
- RUNBOOK lines 1480, 1497, 1515, 1526 (13 Nov); 3834, 3852, 3866, 3874 and 3894 (17 Nov);
- the launch brief of a8ebc443, in its transcript, first user message of 14:48 UTC;
- registry rows 69, 71 and 94-96.

**[measured]** The brief said "about 70 packages done". In fact:
- 70 output folders exist under `second_pass/out/`, since prompts were made for all of them;
- 16 packages hold output: 50 blocks, 808 scans, 141,547 words of corrected text by my count, which is 2.6 % below
  the verdict's count on 148/044-058.

### 1.2 Inputs

The prompt is built by `make_second_pass.py`, lines 120-163. A sample is
`prompts/PROMPT_MPL_148_029-072_148-044-148-058.md`. Its inputs are:
- the first pass: one TeX file per scan, by GPT-6 Astra (ChatGPT Pro mode);
- the package's `_notes.md`, `_doubts.md` and `_inventory.csv`. For 148/029-072 these are 106 KB, 98 KB and 127 KB
  for 44 scans;
- the Pro prompt the first pass ran on, for its macros and conventions;
- since 17 Nov 03:55 UTC, the package's edition matters, `edition_matters_20261117/<PKG>.md`, where the file exists.
  For 148/029-072 that is 8 items; for 145, 4;
- a chat-B Pro run of the package, where one exists;
- three images per scan: the whole page, and two halves.
  - **[measured]** The pages are 1682 × 2358 px. That is the source PDF's own embedded image at 250 ppi
    (`pdfimages -list`, 148.pdf p. 51), so no better image exists locally.
  - The halves are 1682 × 1259 px, about 2.1 megapixels.
  - The first pass and the second pass both read at this source resolution. Whether the halves reach the model
    downscaled is not established here; the pilot measures legibility per tile size (5.2, C5).
- since 17 Nov, Hua's transcription of the cote, by launch brief, not in the prompt file.
  - **[measured]** It is a Claude Opus 5.5 reading. The headers of `transcripts/148/batch-03.fr.tex`, lines 10-11, say
    "Pass: Opus 5.5 (claude-opus-5-5), 2026-09-26 ... Revised: Opus 5.5 ... 2026-11-12". His README, lines 215-217,
    says every skill has run on Opus 5.5 since 19 Oct, and earlier passes on Fable 5, Fable 5.1 and Opus 5.
  - The triple check of 15 Nov (`triple_check_20261115/TRIPLE_CHECK_20261115.md`, line 5) says the same.

**Not given:**
- any reading by another model family;
- the notes of neighbouring packages, and the register rows and waiting prompts that cite these pages;
- the Longue Marche text;
- the literature;
- a computation tool, or any instruction to compute;
- since 17 Nov 22:2x UTC, the CHECK_EVENTS paragraph. **[measured]** Neither `make_second_pass.py` nor any block
  prompt contains it, and the procedure update (`claude_tools/PROCEDURE_UPDATE_20261117.md`) covered the Pro second
  passes, not these.

### 1.3 What the agent does, in order

The method is the block prompt's steps 1-5 and its economy paragraph, as in the 148/044-058 prompt, lines 36-48.
1. Read the prompt, then go scan by scan, line by line, "with the image halves". Compare every word, symbol, index,
   sign, deletion, insertion and margin note with the first-pass text.
2. Settle each doubt mark of the first pass where the ink allows; otherwise keep `\unsure{...}` with the alternatives.
3. Look for what the first pass missed. No procedure is given for this.
4. Correct only where the image settles it. Keep the conventions, never expand or modernise, and do not guess.
5. Check the edition matters that fall on these scans. This step exists only where the file exists.

**The economy paragraph (lines 46-48).** It says:
- "Read each scan's two halves once and settle what you can from them";
- "make an enlarged crop only where the first pass and your reading still disagree, or where a symbol decides the
  mathematics";
- "no more than about 120 tool calls for the block";
- "Write each output file once, at the end."

**The 17 Nov additions** (launch brief):
- "Read the ink first";
- "Open Hua's text only for the places still unresolved after that, and for hard places where your reading and the
  first pass disagree";
- give the unresolved counts before and after consulting Hua;
- for each first-pass note, say whether the corrected text still supports it, with scan and line;
- give the consequential corrections one per line.

**[measured]** In practice, on the 148/044-058 block:
- The agent made about 46 crops named by scan (s0NN_*), about 3 a scan; a few of the s044 crops served the verdict
  too. It made 17 more for the two verdicts (v0NN_*, w0NN_*). The folder
  `work/MPL_148_029-072_148-044-148-058/` holds 69 files with its scripts.
- It applied its changes by a script.
- Its file says outright that some doubt marks were not re-read: "The first pass's other doubt marks on these scans
  that I did not re-read one by one (chiefly the many tokens of the 053 diagonal margin, and 046 'close', 047
  'Grabipond', 050 'suppléments', 056 l.7 cancelled block) are kept as they were" (changes file, lines 114-115).

**[reported] Cost:**
- 13 Nov pilot: ~26k tokens a scan (RUNBOOK 1480);
- 17 Nov pilot: ~33k (3854);
- 17 Nov wave 1: ~33.5k (3866);
- 17 Nov wave 2: ~35k (3894);
- 25-43 minutes a block;
- about 1 point of the weekly all-models meter per 1M agent tokens (3867).

### 1.4 Outputs

- The corrected TeX files.
- `_changes.md`: a table of changes, with first-pass reading, corrected reading, evidence and confidence, then the
  unresolved places as a prose list.
- `_notes_checked.md`: each first-pass note kept, corrected or dropped, then the agent's own notes.
- A short final message with the counts and the consequential corrections. The main session puts these into the
  RUNBOOK and the registry, and from there into editions and waiting prompts.

**[measured]** The totals over the 50 blocks are below; per-package figures are in Appendix A.
- **Change rows:** 2,169, of which 351 high, 1,099 medium and 676 low. Block 16/001-018 is not split by confidence.
  - That is 1.53 per 100 words, or 2.7 a scan.
  - Under the 13 Nov method: 1.29 per 100 words. Under the 17 Nov method, with Hua and edition matters: 1.74. The
    cotes differ, so this is not a controlled comparison.
- **Unresolved places:** about 1,200, counted approximately from the list items of the unresolved sections. They exist
  only as prose inside the changes files.
- **Notes verdicts:** about 1,139 keep, 186 correct and 9 drop, in the 46 notes files my parser read.
- **Own notes:** about 154.

### 1.5 How Pro's notes are processed before and around the second pass

Three readers did this, all Claude Opus 5.5 at effort max, reading the first-pass notes as text, without scans.

| Reader | Entries read | Research items | Edition matters | Nothing further |
|---|---:|---:|---:|---:|
| Follow-ups (`field_experts/FOLLOWUPS_FROM_NOTES_20261117.md`) | 1,669 | 41 | 495 | 1,133 |
| Claims (`field_experts/CLAIMS_FROM_NOTES_20261117.md`) | 1,137 | 9 | 115 | 1,013 |
| Gap (`field_experts/GAP_FROM_NOTES_20261117.md`) | 1,772 | 6 | 100 | 1,666 |
| **Total** | **4,578** | **56** | **710** | **3,812** |

**[reported]** The claims map behind the claims reader lists 1,387 unproved claims and conjectures
(`GROTHENDIECK_CLAIMS_MAP_20261117.md`). Its references to known results were "given from memory, without searching,
as the brief asked".

**Only the edition matters reach the second pass**, through `split_edition_matters_20261117.py` and step 5.

## 2. The measured error rate of the second pass on the controls

### 2.1 What the controls measure, and their limits

The controls are the only pages with three independent readings and a scan check:
- **CTRL-148**, cote 148, scans 44-58:
  - the Pro first pass;
  - GPT-6 Astra at reasoning effort max (Codex web);
  - GPT-6.2 Sol at reasoning effort max (ChatGPT Work).
- **CTRL-145**, cote 145, scans 20-34:
  - the Pro first pass;
  - GPT-6 Astra at reasoning effort max (Codex web).

**The truth is the second pass's corrected text, with its addenda.** The verdict files set it:
- `codex_web_20261113/returns_control/CTRL-148/VERDICT_CTRL-148_20261117.md`;
- `CTRL-148_SOL62/VERDICT_CTRL-148_SOL62_20261117.md`;
- `CTRL-145/VERDICT_CTRL-145_20261117.md`.

**The addenda:**
- 148 changes file, A1-A12 (lines 117-149) and B1-B12 (lines 151-171);
- 145 changes file, rows 43-55 (lines 137-161).

**How the second pass's errors were found:** wherever a control reading differed, the judge looked at the scan. On
148, a two-of-three rule applied where the ink does not decide.

**Limits:**
- **The judge is not independent.** Each judge was the agent that made the second pass of those pages. On 148 the
  first round missed 6 of the 16 errors (2.3).
- **What no reader saw stays unseen.** Errors that every reader shares are invisible. About 25-38 places on 148 were
  left out as undecided (SOL62 verdict, line 57; CTRL-148 verdict, lines 185-205).
- **145 had a single control reading,** so its residual is the less complete of the two.
- **Two hands, 30 pages.** Both controls sit in one cluster, the tower cotes.

### 2.2 The rates

**[measured]**: counts from the addenda rows, my classification in Appendix C. **[reported]**: the Pro figures, from
the verdicts.

| | 148/044-058 | 145/020-034 | Both |
|---|---:|---:|---:|
| Words (the verdicts' count) | 2,665 | 2,954 | 5,619 |
| Pro first pass: errors, all / unmarked (per 100 words) [reported: SOL62 l.51; CTRL-145 l.41] | 65 / 39 (2.44 / 1.46) | 34 / 25 (1.15 / 0.85) | 99 / 64 (1.76 / 1.14) |
| **Second pass, residual errors found by the controls and confirmed on the scan** | **16 (0.60)** | **13 (0.44)** | **29 (0.52)** |
| of which unmarked | 12 (0.45) | 8 (0.27) | 20 (0.36) |
| of which marked (inside a doubt mark or the unresolved list) | 4 | 5 | 9 |
| inherited from the first pass | 13 | 13 | 26 |
| introduced by a second-pass change | 3 | 0 | 3 |
| at places with neither a change row nor a doubt mark ("confident") | 11 | 8 | 19 |
| Not counted: reopened by the two-of-three rule only (B7-B12) | 6 | - | 6 |
| Second-pass changes on these pages: total / wrong | 45 / 3, plus 1 withdrawn by majority | 42 on scans 20-38 / none reversed on 20-34 | 87 / 3 |
| Share of Pro's errors the second pass removed (places still wrong: the inherited ones, plus A4 and A11 where Pro was also wrong) | 50 of 65 (77 %) | 21 of 34 (62 %) | 71 of 99 (72 %) |

The third-pass pilot's keys count these places at another grain: 23 entries on 148 and 9 on 145, with 6 majority
entries on 148 (`codex_web_20261113/PILOT_PLAN_THIRD_PASS.md`, lines 40-43). The places are the same.

**[measured] The extra readers all but cover the residual.** I grepped the two control returns at the 16 places of 148:
- GPT-6 Astra (Codex web) had the right reading at all 16. That holds by construction for A1-A12, and the SOL62 verdict
  confirms B1-B6.
- GPT-6.2 Sol had it at 11 at least: A1, A9, A10, A11 (partly), A12, and B1-B6.
- Neither had it at A4 and A8 except Astra.
- Sol produced no correction outside this set.

Read as a capture-recapture count, the two GPT readers have exposed nearly all the errors that readers of that family
can see. The floor is the shared errors, which no count of this kind sees.

**[measured] My own look at three crops.** I am the same model as the judge, but with a fresh context.
- `w051_impl.png`: i-n-d-i-que, one ascender, no p descender. I agree with B2, "indique".
- `w051_unif.png`: the word ends "-acé" after one tall looped stroke. I agree with B3, "remplacée", at medium.
- `v058.png`: one tall d, no t or l. I agree with the second pass's "anodine", against both controls ("élémentaire",
  "ci-dessus|en dedans"). This is a place where majority voting among the machines would have been wrong had they
  agreed.

### 2.3 The errors by type, and where in the procedure each arises

| Type | 148 | 145 | All | Unmarked | Where it arises |
|---|---:|---:|---:|---:|---|
| Misread word or phrase (letters) | 10 | 5 | 15 | 10 | Step 1, comparing with the first pass in view. A crop is triggered only by disagreement. The halves are below crop scale. Hua, the same model, was consulted at A1 and A4 and supplied wrong alternatives. |
| Polarity: a small word that reverses the statement | 1 (A11) | 0 | 1 | 1 | Step 4: a medium reading "settled" from a crop. The meaning was then argued from it. The tension with 057:11, noted as N4, was not turned back on the ink. |
| Omitted word, symbol or mark (struck comma, struck l, "du Γ", "-traduction", "en fait", an arrow, "=") | 3 | 4 | 7 | 6 | Step 3 has no procedure. Nothing makes the reader account for every ink mark. A6 was "seen in this pass, not recorded" (A6, line 131): there is no per-place log. |
| Added word ("en prenant", "les") | 1 | 1 | 2 | 2 | Step 1: the first pass's fluent text, accepted. |
| Symbol or index misread (σ̃_i for σ̃_a; the struck tilde of φ(σ̇_a)) | 0 | 3 | 3 | 1 | Step 1. The crop was made, but the first pass's index was kept. |
| Struck or overwritten text read wrongly | 1 (A7) | 0 | 1 | 0 | An over-confident second-pass change, later reverted to an open alternative. |
| **Total** | **16** | **13** | **29** | **20** | |

**Two consequences beyond the counts:**
- **Notes built on misreadings.** On 148 the second pass's notes built three items on its own misreadings, all since
  withdrawn:
  - R24/U18 "polarity settled" and N4, both from A11 (notes file, lines 26, 42, 68-75 and 96-102);
  - R22's "'unifiée' is checked and kept", from B3 (lines 113-115 and 124-127).

  On 145, N18, N22 and C9 are marked as touched by rows 43-52.
- **The logbook.** The wrong polarity went into the RUNBOOK within the hour as "053 margin 'si' not 'sauf si' ...
  (settles notes R24/U18)" (line 3857). It was withdrawn at line 3943. It did not reach the edition matters or the
  reference page.

**Adjudication [reported, my reading of the verdicts].** In the first round on 148, the judge listed three readings
as Codex errors: "ou" for "!" (046), "indique" for "implique" and "remplacée" for "unifiée" (051). Of these:
- "unifiée" was recorded as "checked and kept" on the scan;
- all three were reversed after the Sol reading agreed with Codex (CTRL-148 verdict, lines 5-16 and 63-71; changes
  file, lines 139-141 and 160-162).

So the first round recovered 10 of the 16. The same agent read the same ink differently when two readings disagreed
with it instead of one. That is anchoring on its own earlier reading.

**The same mechanism was measured before.** The triple check of 15 Nov (Claude Opus 5.5 at effort max) found it:
- **Reading with the text in view undercounts.** "Reading a page with our text in view lets the transcript's word pass
  when it is plausible. The misses are small words, insertions and struck words" (`triple_check_20261115/`
  `TRIPLE_CHECK_20261115.md`, lines 22-25). Its direct reading of eight pages found 0 errors where a witness diff
  predicted about 10 (lines 130-136).
- **A witness diff decided on the ink is the measurement that exposes errors** (lines 16-21).

### 2.4 What this implies for the 808 scans already second-passed (inference)

**The residual on what is already done.** At the controls' residual of 0.36-0.45 unmarked errors per 100 words, the
141,547 words already second-passed carry roughly 500-650 unmarked errors, plus the marked ones. No control measures
the 13 Nov blocks (142, 147, 149). They were done without any witness, and with fewer changes per word (1.29 against
1.74).

**Hua's text as a witness [measured].**
- On 148, at the 14 residual places I could match in his `batch-03.fr.tex` (A7 and A8 not matched):
  - Hua is right at 5: A9 (":"), A11 ("lorsqu'on « gomme »"), A12 ("enlever"), B3 ("remplacée") and B6 ("du Γ");
  - Hua is wrong or silent at 9: A1, A2, A4, A6, A10, B1, B2 ("implique", as the second pass had), B4 and B5 (the
    plural, as the second pass had).
- On 145 he shares the wrong reading at rows 45, 49-52 and 54:
  - batch-01 line 1237: "les opérations des σ̃_i";
  - line 1262: "On peut maintenant revenir à nos trois";
  - batch-02 line 385: "est le scindage correspondant".

So his text adds coverage. But it is a same-model witness, and it shares the confident errors more often than it
breaks them. Under the 17 Nov rule it was opened only where the checker already doubted. The four places where it was
right and the checker unmarked (A9, A12, B3 and B6) were never compared.

## 3. What Pro's notes contain that the second pass does not process yet

### 3.1 What a Pro note holds

Take 148's R17-R24 (`returns/MPL_148_029-072_unzipped/MPL_148_029-072_notes.md`, lines 370-449). Each note has:
- **Source** (scan:lines) and **Kind**: unproved claim, self-flagged, reading question, own idea, unpursued
  implication, or withdrawn;
- an **Anchor**, quoted from the first-pass reading;
- the argument;
- often a **finite test computation**. For example R17's two disks with Jacobian signs (+1, −1), R23's Z/0Z = Z
  against the empty set, and in the edition matters R38's (1,1,4) ↦ (2,2,−1) and R40's bigon count;
- a **Confidence**;
- **Context searched**: notes of other packages, such as 146/103 R08 and 147/010-013 N011;
- **Results**: rows of our research registers with their status, such as "STRATA F.17 — Proved, return claim",
  "LM4 C.12 — Open, return claim", "WG2 §1.8 #5 — unchecked plan" and "IMPL P3 — open candidate prompt item".

**Pro was also careful about readings.** R24 explicitly declines to infer the 053 polarity because the reading is
unresolved (line 444). That caution was right; the second pass's "settlement" was wrong.

### 3.2 What the second pass does with them now

It does three things:
- It checks each note's anchor against the corrected text. **[measured]** In the 46 files parsed: about 1,139 keep,
  186 correct and 9 drop.
- It checks the edition matters on its scans.
- It adds its own notes.

**What it does not do:**
1. **The research links.** No step checks whether a corrected reading changes a register row or a waiting prompt.
   The main session does this ad hoc from the final message. For example (RUNBOOK 3883): "notes
   F12/N15/T04/T06/T09 quote the wrong word".
2. **The test computations.** They are kept, not redone. 148 R28: "The note's finite example is unaffected". 145
   A01-A04: "KEEP".
3. **The cross-cote links.** A block cannot see the notes it is linked to in other packages.
4. **The "nothing further" mass.** 3,812 of 4,578 entries, among them most "known result" pointers, with references
   given from memory and not searched. These are the companion's C1 material (memory `companion-ideology`): the
   questions an algebraic geometer would ask, answered from the literature next to the text.
5. **Writing back to the registers.** The claims map, FOLLOWUPS, CLAIMS and GAP quote first-pass readings. No field
   records a second-pass correction. For example, R24 sits there with "sauf si|si".
6. **Check events.** None are recorded. The rule of 17 Nov, 22:2x, is not in these prompts.
7. **The unresolved places.** About 1,200 sit as prose. Lesson 1 of `CLAUDE_SECOND_PASS_METHOD_AND_LESSONS_20261117.md`
   (lines 56-59) says "route them, do not just record them". They are not routed.

### 3.3 How the second pass should process them

| Item in the notes or registers | What the second pass does | Where it goes |
|---|---|---|
| Reading question, convention, page error, dating (@n, #n, g edition matters, the notes' "reading question" kind) | Settle it on the ink under the place protocol (5.2, C3). | Changes table and `PLACES.tsv`. Status line for the register row: settled, corrected or open. |
| His unproved claim, conjecture or self-flagged doubt (claims map #n, the notes' kinds) | Check the quotation against the corrected text. State the claim in today's terms. Classify it: known (source opened, with locator), short proof (sketch), computation (run it), or open. | `NOTES_ROUTED.tsv` (claim id, scan:line, class, source). `CHECK_EVENTS.tsv` per the 17 Nov rule ("reading a statement while transcribing it is not a check of it"). The C1 draft. |
| Research link ("Results": run and row) | If the corrected reading changes the anchor, record the run, row and prompt, with the old and new reading. | `CONSEQUENCES.tsv`, for the main session's same-day loop (the LM5 loop of 13 Nov). |
| Test computation | Re-run it in Python, under `python -I -B`, in the block's own work folder. Or mark it "not recomputed". | `CHECK_EVENTS.tsv` (computation or formal certificate). |
| Cross-cote link ("Context searched") | Record the link with its kind: same object, same notation, continuation, contradiction. | `LINKS.tsv`, for the companion's chapter map. |
| "Known result" pointer from the readers' "nothing further" | Open the source, give the locator, or say it was not located. | The C1 draft (`GROUNDWORK.md`). |
| Own mathematical notes | See section 4. | The C1 draft. Candidate research items go to the field expert. |

## 4. The second pass as mathematical reading (the user's addition)

### 4.1 What the second passes do now

**[measured, from reading the notes files]** Some agents worked the mathematics hard. In 145/020-038, own notes C1-C9
(notes file, lines 154-195):
- **C8** is a computation in ⟨σ₀, ρ | σ₀² = ρ³ = 1⟩ ≅ Z/2 * Z/3. It shows that the margin's l∞ as read,
  (ρ⁻¹σ₀)², cannot equal (ρσ₀)². So either the ink was misread or he slipped. This is mathematics used as a reading
  instrument.
- **C4** proves the 030 claim in the quotient τ = 1. It says that a coset enumeration would settle the general claim,
  and does not run one.
- **C9** identifies the group with PSL₂(Z) and the loop group with Γ(2)/{±1}.

**In 148/044-058:**
- N2 and N3 caught two of his slips: A_0 for A_ℓ, and π₀(Σ') = A_0;
- N8, after the correction, explains the arithmetic clause: orientation reversal is complex conjugation.

**[reported] Elsewhere:**
- a counterexample on 149/130 (N5, unchecked; RUNBOOK 1526);
- 150/092 "rare", which removes the counterexample in register row A10 (RUNBOOK 3894).

**But four things are missing:**
- **The prompt does not ask for this work.** It asks only for "your own notes of the same kinds".
- **No context is given:** the Longue Marche text, the neighbouring cotes, the literature, computation.
- **No checks are recorded,** and claims are left "unchecked".
- **Nothing is routed** to the companion's C1 layer.

**The slips show the gap [measured, from the verdicts].**
- On 148/044-058 the readers' notes together found five slips of his: 049 A_0, 050 r(ω), 054 π₀(Σ'), 055 "du bord de
  Σ'_ℓ" and 056 a missing verb. The second pass found two of them; GPT-6 Astra's notes three; Sol's three.
- On 145/020-034 about six were found: 034 (9'), 033 SÊ̂, 026 against 037, the indices of 027/029, 028 Γ₂ and 020 l∞.
  The second pass found three.

### 4.2 Mathematics as a reading instrument, on the controls

Of the 29 residual errors, about eight sit where a check of sense or mathematics raises a flag:
- **145/021 L36**, "revenir à nos trois miroirs, d. par" (rows 49-52). The next display (15) gives the three lifts τ₀,
  τ₁, τ∞ of τ̇, so the line must announce lifts: "remonter τ̇ en trois manières, à savoir".
- **148/053**, polarity (A11). The agent's own N4 saw the clash with 057:11 and reconciled it in prose.
- **148/051**, "unifiée" (B3). 050 has just replaced p by the torsor family, and the sentence continues that
  replacement.
- **148/051:5**, "dans la donnée d'ensemble de" (A10). It does not parse as French.
- **148/052**, the plural (B5). "For each object, reconstruct the corresponding graph".
- **Possibly 145/028**, "scindage" for "remontage" (row 54), in the same lifting context.

**The converse also holds.** At about three places, mathematical plausibility favours the wrong word:
- "implique" for "indique" (B2);
- "exclure" for "enlever" (A12);
- an added "en prenant" (A9).

That is the first pass's own failure mode: "fluent misreadings that put a plausible mathematical word where the ink
says something else" (the block prompt, line 5). **So the rule is: mathematics raises a flag and sends the reader back
to the ink, as a blind place under C3. It never changes a reading by itself.** Where the ink stays open, the
mathematically expected reading may become an alternative with a note, never the first reading.

### 4.3 What the second pass should do

A step after the reading of each mathematical unit (a definition, a display chain, a section). It writes six things:
1. **The running account.** The notation in force, kept in a cote-level notation table that later blocks inherit. What
   each display asserts. The steps of the argument. Where it continues from or into other pages and cotes.
2. **Checks of every formula:**
   - domains and types: r is defined on A, so r(ω) is a slip;
   - indices, signs and variance;
   - consistency with the page before and after (026 against 037);
   - impossibilities: the boundary of a closed 1-manifold.

   Each alarm becomes a place in `PLACES.tsv`, read again on the ink.
3. **His claims.** For each one: true or false, known (source opened, with locator), a short proof, a computation run,
   or open. Where a computer settles it, run it: finite group presentations by coset enumeration, small cases,
   numerical checks.
4. **Connections:**
   - his other cotes, through `notes_crosslinks_20261117.tsv` and the registers;
   - the Longue Marche;
   - Hua's modernised reading, as context with credit to his project (memory `hua-project-relations`);
   - the modern literature.
5. **The C1 draft (`GROUNDWORK.md`).** The questions an algebraic geometer would have on a first reading of the unit,
   each answered: what the objects are in modern terms, why the step holds or where it does not, what it became in
   the literature. In English. Never mixed with his words in a paragraph.
6. **Check events,** per the 17 Nov rule, for every claim checked, computed or refuted.

### 4.4 What it costs

**[inference from the measured rates]**
- **Today:** ~33-35k Claude tokens a scan.
- **The improved reading (section 5):** I expect ~45-55k.
- **The mathematical layer on dense pages:** plus ~20-40k. Reading the Pro notes of a 44-scan package alone is about
  27k tokens, and opening sources costs more.
- **The full method:** ~70-90k a scan, about 2-2.5 times today. At about 1 point of the weekly all-models meter per
  1M tokens (RUNBOOK 3867):

| Method | Claude tokens a scan | Meter points per 100 scans |
|---|---:|---:|
| Today | ~34k | ~3.4 |
| Improved reading | ~50k | ~5 |
| Improved reading with the mathematical layer | ~80k | ~8 |

**What that means for the program:**
- **Wave A** (149, 147/003-137, 142; 390 scans): ~31 points.
- **The 3,476 returned scans that have no Claude second pass yet [measured]:** ~280 points at the full method. That is
  nearly three weeks of the whole meter, or 8-11 weeks at the pace of 25-35 % a week.

So the order of section 7 matters. The pilot (section 6) replaces these estimates with measurements.

### 4.5 How the pilot measures the mathematical layer

The pilot's mathematical score has seven parts:
- **Slips found** against the list in 4.1: five on 148 and about six on 145. New slips found count only after
  verification.
- **Claims classified,** with sources opened. The grader checks ten locators per control.
- **Computations run and verified.**
- **Mathematical alarms** that led to a confirmed reading correction, against alarms that did not.
- **False mathematical claims.** Each one counts as heavily as an unmarked reading error.
- **The C1 drafts,** graded on a rubric: correct, answers the questions a first reader has, sources located, never
  mixed with his words.
- **Cost:** tokens and minutes.

## 5. The improved method

### 5.1 The changes, each with its reason

| # | Change | Why (evidence) |
|---|---|---|
| C1 | **An independent machine reading from another family on every page, before the Claude pass.** GPT-6 Astra at reasoning effort max (Codex web) on dense hands. A blind full reading, never a check of the first pass. For pages that the Codex route transcribed first (batch K), the second reading is the Pro first pass or GPT-6.2 Sol at reasoning effort max (ChatGPT Work). | 26 of the 29 residual errors were inherited first-pass readings, and the GPT controls had the right reading at nearly all of them (2.2). Their errors and Pro's are largely disjoint: "Codex has the right reading at 26 of Pro's 34 errors", Pro at 33 of Codex's 41 (CTRL-145 verdict, l.43-47). Astra is the stronger control reader on dense hands: 0.79 unmarked against Sol's 1.24 (SOL62, l.51). |
| C2 | **Diff first.** A script (`codex_web_20261113/tools/reconcile_readings.py`) lists every disagreement between the readings and Hua, after conventions are normalised (C12). The Claude pass reads every place, then the whole page. | The diff finds the confident errors that comparing in view does not (2.3). The whole-page reading stays, for the errors that all the witnesses share. |
| C3 | **Read blind before seeing the alternatives.** At each place the checker sees a native-resolution crop and its context, and writes its own reading with the letter evidence (ascenders, descenders, dots, stroke counts). Only then does it see the witnesses' readings, and it decides. The first blind reading is kept in `PLACES.tsv`. | The judge kept three of its own wrong readings after looking at the scan (2.3). The triple check found the same with a text in view. |
| C4 | **A watch list for logic-bearing words:** implique/indique, si/sinon/sauf si, maximaux/minimaux, remplacer/unifier, the negations, quantifiers and connectives, and the operation words (enlever/exclure, contraction/restriction). Each is read on a crop whether or not the readers agree. | The consequential error (A11) and the meaning-changing errors (B2, B3) are such words. The Codex audit's G2 list (minimaux/maximaux, loc/lac, cohérente/évidente) is of the same kind. |
| C5 | **Native-resolution tiles.** Quarter-page strips with overlap, plus 2-3× crops of every formula line, every margin (rotated), and every struck or inserted passage. The economy paragraph and the 120-call cap go. The work is budgeted by place count. | The halves are 2.1 MP; tile-scale crops avoid any downscaling for viewing. The cap makes "crop only where you disagree" the rule, and anchoring decides what you disagree with. The triple check missed struck words and sub- and superscripts at about 0.6 of scale (l.130-136). |
| C6 | **Ink coverage.** For every strip, each ink mark is accounted for: in the text, struck, inserted, drawing, noise, or illegible. | 7 of the 29 errors are omissions of small marks. One was "seen in this pass, not recorded". |
| C7 | **`PLACES.tsv`, one row per place:** scan, line, place id; the reading of each witness (Pro, Codex or Sol, Hua, the Claude blind reading); the decision; the crop file; the confidence; the adjudicator (model and effort); status (settled, open, or majority alternative). Open places are routed: a short list per cote for the user's eye, and the hardest to a further blind reader. | About 1,200 unresolved places sit as prose today. Lesson 1 of 13 Nov said to route them. |
| C8 | **Adjudication not by the reader of record.** Where the checker's own reading is one side and its confidence is below high, a fresh adjudicator decides blind, or the place stays open with every alternative. The two-of-three rule only adds alternatives, never replaces a reading silently, as the SOL62 verdict already practised. | The same agent read the same ink differently with one disagreeing reading than with two (2.3). |
| C9 | **The mathematical step of section 4.** Its alarms go back to C3. | Section 4.2. |
| C10 | **Notes routing (3.3) and `CHECK_EVENTS.tsv`.** | Section 3.2. The rule of 17 Nov 22:2x. |
| C11 | **Consequential corrections by confidence.** High confidence, or a second blind look: reported as consequential. Medium: reported as "reading changed (medium); recheck before use". `CONSEQUENCES.tsv` names every register row and prompt touched. | A11 went into the logbook within the hour and was withdrawn later (RUNBOOK 3857, 3943). |
| C12 | **Normalise conventions before diffing:** macros, quotation marks, abbreviations written out, line breaks. | A raw three-way diff gave 301 disagreement regions on 213 lines for 15 pages, mostly noise (`PILOT_PLAN_THIRD_PASS.md`, l.85-94). |

Two existing practices stay:
- Every agent keeps its scripts in its own crop folder, never in a shared scratchpad (RUNBOOK 1526, 3843).
- Hua's text stays a credited witness, now in the diff for all places, recorded as "Claude Opus 5.5 (Michel Hua's
  project)". It is never enough alone to settle a place.

### 5.2 The procedure of a block

**Step 0, by script, before the agent.**
- Gather the readings: Pro, the C1 reading, Hua.
- Normalise them (C12) and diff them into a draft `PLACES.tsv`.
- Make the native tiles, and the crops of the watch-list hits.
- Put together:
  - the cote's notation table, from earlier blocks and Pro's notes;
  - the register rows and waiting prompts that cite these scans (`notes_crosslinks_20261117.tsv`, the three readers'
    TSVs, the claims map);
  - the edition matters.

**Step 1, layout and structure, per scan.** The whole page: what is on it, its mathematical units, margins,
insertions, struck blocks.

**Step 2, reading, per scan.**
- Read the strips with the reconciled text, its disagreement places masked.
- Settle each place under C3.
- Do the ink coverage (C6) and the watch list (C4).
- Write the TeX.

**Step 3, mathematics, per unit** (section 4.3). Alarms go back to step 2.

**Step 4, notes, per block** (section 3.3).

**Step 5, outputs:**
- the TeX;
- `_changes.md`;
- `PLACES.tsv`;
- `NOTES_ROUTED.tsv`;
- `CHECK_EVENTS.tsv`;
- `CONSEQUENCES.tsv`;
- `LINKS.tsv`;
- `GROUNDWORK.md`;
- the final message.

**Block size.** It is set by the context: about 8-10 scans of dense hand rather than 15-19, with the cote's notation
table carried from block to block. The pilot measures tokens a scan and decides.

Any prompt built from this method passes `claude_tools/push_rule_pro_prompts.py --lint` before use. It asks for the
whole task, with no cap and no cheaper fallback.

### 5.3 Candidate: the dual second pass (the user's idea)

**The idea.** Two models each do the second pass independently on the same first pass: Claude Opus 5.5 at effort
max, and a model of another family, such as GPT-6 Astra at reasoning effort max (Codex web). Their disagreements are
read on the ink.

**Why it addresses the main weakness.** Most of the residual sits in confident readings: 19 of 29 with neither a mark
nor a change row. A second checker with different blind spots disagrees exactly there.

**The design question: verification or blind reading.**

| Variant | What model 2 does | Disagreements per page | What it can miss |
|---|---|---|---|
| D-ver | Checks the Pro first pass against the scans, as the Claude pass does. | Fewer: both start from the same text. Not measured; plausibly well under the ~20 regions a page of raw full-reading diffs. | Fluent first-pass words that both checkers accept. Both are anchored on the same text. Whether a GPT checker anchors less than Claude is exactly what V4 (Sol checking a text) measures. |
| D-blind | Reads blind, as the controls did, then compares its reading with the first pass. | More (~20 raw regions a page before C12). | Only the errors shared by the families. On the controls this design exposed nearly all the confident errors. |

D-blind with the Claude pass is in effect C1-C3: the blind reading made in parallel instead of before.

**Cost per page:**
- **Claude [estimate]:** one second pass (~34-50k tokens), plus adjudication of the places. At ~1.5k tokens a place, that is
  ~8-15k for D-ver if it yields 5-10 places a page, and ~12-18k for D-blind after normalisation.
- **Model 2:**
  - GPT-6 Astra Max in Codex web costs about 0.03x of a weekly Codex allowance a page (`codex_web_20261113/`
    `METHOD_AUDIT_AND_PLAN_20261117.md`, l.23).
  - On Work, round 1 moved the account-4 meter by about 25 points of a 20x week for ~500 pages while still running
    (RUNBOOK 3999).
  - Sol is cheaper on the meter (its pilot measures by how much) and ran in under half the wall time.

**Against the Sol third pass:**
- **The third pass is sequential and cheaper.** V1-V4 run after the Claude pass, on its text. V4 checks the second
  pass's text, so it inherits that text's anchoring as well as its own.
- **The dual pass is parallel, and each checker starts from the first pass.** Their disagreements include the errors
  one of them corrected and the other did not.

The pilot puts all of these in one table (section 6).

**My expectation, to be tested:** D-blind or C1 performs best, D-ver second, single pass with V4 last. V3 (blind
targeted places) is a cheap complement to any of them. The figure that decides is errors caught per unit of total
cost, with false alarms and introduced errors counted against.

## 6. The pilot: measuring the improved method on known truth

### 6.1 Pages and keys

**The pages.** CTRL-148 (148/044-058) and CTRL-145 (145/020-034): 30 pages, 5,619 words.

**The keys.**
- `codex_web_20261113/third_pass_pilot/keys/CTRL-148_known_second_pass_errors.tsv` (23 entries) and
  `CTRL-145_known_second_pass_errors.tsv` (9).
- The second pass as it stood before the controls is `third_pass_pilot/second_pass_before_controls/<ID>/`.
- Never shown to a model under test.

**Fair inputs.** On 148, the GPT-6 Astra and GPT-6.2 Sol readings built the key, so no arm may use them.
- For 148, a fresh GPT reading: the GPT-6.2 Astra at reasoning effort max rerun CTRL-148_2 when it lands (not in
  `returns_control/` when this was written), or a new GPT-6 Astra Max Codex-web run.
- For 145, only CTRL-145 (GPT-6 Astra) built the key, so V1-CTRL-145 (Sol) is a fair input.

**Fresh agents.** Every arm is run by an agent new to these pages. a8ebc443 and ac292d80 know the answers: they serve
for the scan checks of the grading under the blind protocol, and not as graders of their own pages' arms.

### 6.2 The arms

All Claude arms are Claude Opus 5.5 at effort max, 0 sub-agents.

| Arm | What runs | It measures |
|---|---|---|
| A0 | The current block prompt and brief, replayed by a fresh agent on the Pro first pass. | Run-to-run variance of the current method, against the known pre-control text. |
| A1 | The improved reading (C1-C8, C11, C12), with one fresh GPT reading and Hua as inputs. No mathematical layer. | The reading gain alone. |
| A2 | A1 plus the mathematical layer and notes routing (C9, C10): the full method. | The added catches from mathematics, and their cost. |
| D-ver | Claude with C3-C8 but no blind reading as input, in parallel with GPT-6 Astra Max (Codex web) checking the Pro first pass. Reconcile, then a blind Claude adjudication. | The user's dual second pass, verification form. |
| D-blind | Identical to A1, except the GPT reading is made in parallel. If inputs are equal, A1 is D-blind; run it apart only if the timing changes what the Claude agent sees. | - |
| V1-V4 | The four Sol third-pass folders already built (`codex_web_20261113/drag_split_third/`), on the pre-control second pass, graded by `PILOT_PLAN_THIRD_PASS.md`. | The sequential alternative. |

### 6.3 The grading

**[proposal]** A grader who made none of the readings: a fresh Claude Opus 5.5 at effort max. A Claude Fable 5.2 at
effort max grader would need the user's OK.

**How it grades.** It uses `reconcile_readings.py` against the keys. Every place where an arm differs from the truth
and the key is silent is read blind on the scan:
- the grader writes its reading before it sees which arm said what;
- a8ebc443 and ac292d80 give second looks where the grader is not at high confidence.

**One table for all arms, per control and in total:**
- known errors caught, split into wrong first readings, alternatives and majority entries;
- new errors found and confirmed on the scan;
- errors introduced: wrong changes, and the precision of the changes;
- residual unmarked errors per 100 words: known missed plus new ones found by any arm;
- unresolved places: count, correctly settled, wrongly settled;
- anchoring: places where an arm's blind reading (C3) and its final decision differ, and which was right;
- scan-check load: places a Claude adjudicator had to read;
- cost: Claude tokens, tool calls, wall time, and the Codex or Work meter for the external runs;
- for A2: the mathematical score of 4.5.

**The key's bias.** The key favours arms with a blind reading (A1, A2, D-blind, V1, V2), because it was built from
blind readings (`PILOT_PLAN_THIRD_PASS.md`, l.48-52). So:
- new errors confirmed count fully;
- for D-ver and V4 the table also reports the catch rate on errors those arms could see.

### 6.4 The decision

**[proposal, to state before the runs]**
- **The reading arm.** Adopt the one with the most errors caught (known plus new) per unit of total cost, whose
  changes are at least 95 % right. Among arms within about a tenth of each other, take the one with the lower scan-check
  load.
- **The mathematical layer.** Keep it if it does three things:
  - finds at least half the listed slips;
  - makes no more than one false mathematical claim per ~1,000 words;
  - passes the C1 rubric on most units.

  Its cost per scan then sets which pages get the full layer (section 7).
- **A second test.** Then one fresh dense control, 15 pages not yet second-passed: 144/001-015 or 146/001-015, the
  same cluster. Its truth is built by three machine readings and blind adjudicators who are not its readers. This
  tests the chosen method where the truth was not made by the current judges.

**Pilot cost [inference].** For the Claude arms: about 0.6-1.2M tokens per arm and control for A0, A1, A2 and D-ver, plus
grading of ~0.3M per arm and control. In all, about 6-10M, or 6-10 points of the weekly meter. On top come the
external runs: two to four Codex or Work folders of 15 pages, and V1-V4 as already planned.

## 7. Priority order for the waves

### 7.1 Criteria

- **Companion weight.** The LM companion outline places 3,929 statements, and five chapters hold 71 % of them
  (`lm_companion_plan_20261117/COMPANION_OUTLINE_LM_20261117.md`, l.55-64):
  - cote 149: 969;
  - the tower at infinity (cotes 143-148, 150): 364;
  - LM §§30-31: 504; §46: 348; §51: 614. These are text of La Longue Marche itself, whose edition and readers exist.
- **Note density.** Notes per cote, and citations from other cotes' notes (`reports_20261117/archive_report_data.json`).
  Research items and edition matters per package (the three readers' TSVs). Notes that name our runs, because their
  claims feed research prompts.
- **Hand difficulty.** The first pass's doubt marks per 100 words. The change density of finished second passes.
- **Method age.** The 13 Nov blocks had no witness, no edition matters, and the economy clause.
- **First-pass-only pages [measured].** 76 returned packages, 3,476 scans and 720,265 words have no Claude second
  pass. They carry 5,095 note entries, 39 research items and 518 edition matters.

### 7.2 The order

**Wave A: re-pass the heaviest chapters with the improved method.** All three were done on 13 Nov, under the oldest
method.
- **Cote 149,** 135 scans: 969 companion statements, 405 notes, cited 47 times.
  - Its 13 Nov second pass made 1.09 change rows per 100 words on 001-090 and 1.71 on 091-136.
  - Its consequential readings (the 130 counterexample, 133-135) fed LM5 and ANABELIAN_149_PUSH.
- **Cote 147/003-137,** 135 scans: 438 notes, cited 42 times.
- **Cote 142,** 119 scans: 406 notes.

**Wave B: the unpassed tower cotes and the LM neighbourhood.**
- 144: 176 scans first-passed, 312 notes; 25 edition matters on 001-061.
- 146: 123 scans, 226 notes; 4 research items and 27 edition matters on 001-099.
- 147/138-190: 53 scans, 136 notes.

**Wave C: small, much-cited cotes.** 44, 47 and 54: 25 pages in all, cited 58, 29 and 33 times (duality on abelian
varieties, intermediate Jacobians). They are the two blocks of MPL_16+47+54+44 that never ran:
`PROMPT_MPL_16+47+54+44_16-054-54-003.md` and `_54-004-44-009.md`.

**Wave D: packages whose notes most feed our runs and registers.**
- 105: 374 notes, 351 of them naming runs.
- 134-8: 509 notes, 361 naming runs. This is the API route; check whether it is typed. A typed page needs a lighter
  reading and the full notes processing.
- 84/146-193: 123 notes naming runs.
- 121, both packages: 7 research items, 34 edition matters, cited 17 times.
- 156-1+156-2: 3 research items, 16 edition matters.
- 131: 3 research items, 19 edition matters.
- 144/122-167, 14/002-044, 11/043-058+56, 36/053-085+39, 146/100-134.

**Wave E: the 17 Nov cotes, re-passed only after the pilot measures the gain.** 141+143, 145, 148, 150, 151, 152+120
and 16, where the controls put the residual at 0.44-0.60 per 100 words. The diff against a fresh GPT reading (C1-C3)
alone may be enough there. The pilot shows whether the full re-pass is needed.

**Then the rest,** by book and hand difficulty. The highest doubt densities among first-pass-only packages
**[measured]**:
- 154/127-176: 9.5 per 100 words;
- 1/002-050: 8.7;
- 108+112-115: 7.1;
- 146/100-134: 6.6;
- 36/002-052: 6.4;
- 154/077-126 and 81/038-055+154/046-076: 6.3;
- 43/094-142: 6.1;
- 58/020-067: 6.0.

**The Codex-web batch K pages** (about 2,700 by Friday) also need second passes. They have no Pro research notes,
only the light G1 notes. So the mathematical layer (section 4) matters more there, and their second reading is Pro or
Sol (C1).

**Where the mathematical layer goes in full:** waves A and B, and every page a companion chapter or a waiting prompt
quotes. Elsewhere, the cost measured in the pilot decides.

## 8. Limits of this audit

- **Small sample.** Two controls, 30 pages, two hands, one cluster. The truth was built by the agents who made the
  second pass, and on 148 by a two-of-three rule at undecided places.
- **The 29 errors are my classification.** They are listed one by one in Appendix C for checking.
- **My counts are approximate where the file formats differ.** Block 16/001-018 has no confidence split. The
  unresolved and notes counts come from a pattern parser.
- **I did not re-read any page.** I looked at three crops.
- **I am the same model as the second pass and its judge:** Claude Opus 5.5 at effort max.

**Models named in this audit:**
- **First passes:** GPT-6 Astra (ChatGPT Pro mode).
- **Controls:** GPT-6 Astra at reasoning effort max (Codex web); GPT-6.2 Sol at reasoning effort max (ChatGPT Work).
- **Claude Opus 5.5 at effort max:** the second passes, the verdicts, the notes readers, the triple check and this
  audit.
- **Claude Opus 5.5 at effort high:** the third-pass pilot builder, a302cb2d, and the procedure update, aca6a341.
- **Hua's transcriptions:** Claude Opus 5.5. His file headers name the model; his project does not record the effort.

## Appendix A. Second-pass outputs per package [measured]

Words are by my count. "Rows" are change rows; the addenda after the controls are given separately.

| Package (cotes) | Date | Blocks | Scans | Words | Rows (high / medium / low) | Rows per 100 words |
|---|---|---:|---:|---:|---|---:|
| MPL_142_001-093 | 13 Nov | 5 | 90 | 16,661 | 160 (18 / 81 / 61) | 0.96 |
| MPL_142_094-122 | 13 Nov | 2 | 29 | 5,273 | 74 (10 / 46 / 18) | 1.40 |
| MPL_147_003-047 | 13 Nov | 3 | 45 | 6,154 | 114 (15 / 80 / 19) | 1.85 |
| MPL_147_048-137 | 13 Nov | 5 | 90 | 14,134 | 199 (41 / 103 / 55) | 1.41 |
| MPL_149_001-090 | 13 Nov | 5 | 90 | 15,471 | 168 (21 / 110 / 37) | 1.09 |
| MPL_149_091-136 | 13 Nov | 3 | 46 | 7,791 | 133 (39 / 59 / 35) | 1.71 |
| MPL_143+141 | 17 Nov | 3 | 50 | 5,890 | 159 (21 / 75 / 63) | 2.70 |
| MPL_144_168-184+148_001-028 (148 part only) | 17 Nov | 2 | 28 | 4,460 | 92 (8 / 46 / 38) | 2.06 |
| MPL_145 | 17 Nov | 2 | 38 | 7,423 | 85 (17 / 49 / 19), plus 13 addenda | 1.15 |
| MPL_148_029-072 | 17 Nov | 3 | 44 | 7,887 | 167 (18 / 76 / 73), plus 24 addenda | 2.12 |
| MPL_16+47+54+44 (cote 16; 3 of 5 blocks) | 17 Nov | 3 | 51 | 12,295 | 147 (43 not split; 32 / 41 / 31) | 1.20 |
| MPL_150_001-043 | 17 Nov | 3 | 41 | 9,752 | 181 (14 / 107 / 60) | 1.86 |
| MPL_150_044-084 | 17 Nov | 3 | 41 | 8,422 | 123 (29 / 59 / 35) | 1.46 |
| MPL_150_085-099+151_001-031 | 17 Nov | 3 | 43 | 7,014 | 136 (22 / 60 / 54) | 1.94 |
| MPL_151_032-075 | 17 Nov | 3 | 44 | 7,089 | 118 (20 / 54 / 44) | 1.66 |
| MPL_152+120 | 17 Nov | 2 | 38 | 5,831 | 113 (26 / 53 / 34) | 1.94 |
| **Total** | | **50** | **808** | **141,547** | **2,169 (351 / 1,099 / 676, plus 43 not split)** | **1.53** |

The other 54 folders under `second_pass/out/` are empty: their prompts exist, but no block has run.

## Appendix B. Packages without a Claude second pass, by notes feeding our work [measured]

"Doubts/100w" is the first pass's `\unsure` marks per 100 words. "Notes → runs" counts the notes entries that name one
of our runs.

| Package | Scans | Doubts/100w | Notes | Notes → runs | Research items | Edition matters |
|---|---:|---:|---:|---:|---:|---:|
| MPL_105 | 48 | 3.3 | 374 | 351 | 2 | 10 |
| MPL_134-8_043-087 | 44 | 5.0 | 509 | 361 | 1 | 6 |
| MPL_121_049-073+153+155 | 44 | 2.6 | 129 | 43 | 3 | 27 |
| MPL_156-1+156-2 | 46 | 5.8 | 122 | 45 | 3 | 16 |
| MPL_121_001-048 | 43 | 5.8 | 93 | 41 | 4 | 7 |
| MPL_146_001-099 | 90 | 5.8 | 130 | 0 | 4 | 27 |
| MPL_84_146-193 | 48 | 4.8 | 224 | 123 | 0 | 3 |
| MPL_131 | 38 | 3.6 | 97 | 6 | 3 | 19 |
| MPL_14_002-044 | 40 | 3.7 | 97 | 5 | 2 | 15 |
| MPL_11_043-058+56 | 50 | 3.3 | 107 | 2 | 1 | 24 |
| MPL_136_047-094 | 46 | 5.2 | 70 | 10 | 2 | 10 |
| MPL_144_001-061 | 59 | 3.6 | 174 | 0 | 1 | 25 |
| MPL_36_053-085+39 | 49 | 3.7 | 103 | 2 | 1 | 24 |
| MPL_154_127-176 | 50 | 9.5 | 77 | 14 | 1 | 17 |
| MPL_144_122-167 | 43 | 4.1 | 57 | 53 | 0 | 4 |
| MPL_146_100-134 | 33 | 6.6 | 96 | 0 | 0 | 5 |
| MPL_147_138-190 | 53 | 5.2 | 136 | 0 | 0 | 5 |
| MPL_144_062-121 | 59 | 3.3 | 10 | 8 | 0 | 5 |

The full table (92 packages) comes from `priority_data.py` in my scratchpad. The Codex-web and API pages have no Pro
notes and are not in it.

## Appendix C. The 29 residual errors of the second pass on the controls

The columns are: id, scan:line, second-pass reading, truth, type, mark, origin. "Inherited" means the first-pass
reading was kept. A row number refers to the second-pass changes file.

**148/044-058** (changes file, A1-A12 at lines 126-137, B1-B6 at lines 160-165):

| Id | Scan:line | Second pass | Truth | Type | Mark | Origin |
|---|---|---|---|---|---|---|
| A1 | 044:17-18 | "tout pris en détail \| pour [ill] travaux", "au point de vue œcuménique \| [ill] ultérieurs" | "tant qu'on ne travaille pas au point de vue arithmétique" | misread phrase | marked | inherited; Hua's alternative added |
| A2 | 044:18 | "c'est le cas" | "c'est le gr." | misread word | marked | inherited |
| A4 | 044:21 | "groupoïde \| groupe ... s'appelle \| s'appellera" | "gr. or. ... de s'appeler" | misread words | marked | introduced (row 4, from Hua) |
| A6 | 048:12 | no mark | a struck comma | omitted mark | unmarked | inherited; seen, not recorded |
| A7 | 048:15 | struck "est un" | struck "∈A \| est un" | struck text | marked | introduced (row 17) |
| A8 | 048:44 | "disjointes" | "discrète \| directe \| disjointes" | misread word | unmarked | inherited |
| A9 | 050:41 | "supplémentaire en prenant" | "supplémentaire :" | added words | unmarked | inherited |
| A10 | 051:5 | "dans la donnée d'ensemble de la structure" | "de la donner d'emblée dans la structure" | misread phrase | unmarked | inherited |
| A11 | 053:40 | "si ... l'on doive « gommer » ... alors" | "lorsqu'on « gomme » ... sinon" | polarity | unmarked ("si") | introduced (row 33) |
| A12 | 055:19 | "exclure" | "enlever" | misread word | unmarked | inherited |
| B1 | 046:60 | "!" | "ou" | misread word | unmarked | inherited |
| B2 | 051:4 | "implique" | "indique" | misread word | unmarked | inherited; kept by the judge in round 1 |
| B3 | 051:5 | "unifiée" | "remplacée" | misread word | unmarked | inherited; "checked and kept" in round 1 |
| B4 | 052:19 | "description" | "description-traduction" | omitted word | unmarked | inherited |
| B5 | 052:21 | "les graphes ... correspondants" | "le graphe ... correspondant" | misread (number) | unmarked | inherited |
| B6 | 056:9 | (inserted gloss without "du Γ") | "du Γ, i.e. ..." | omitted word | unmarked | inherited |

**145/020-034** (changes file, rows 43-55, lines 149-161); all inherited:

| Row | Scan:line | Second pass | Truth | Type | Mark |
|---|---|---|---|---|---|
| 43 | 020 margin, L17 | (no "en fait") | "en fait" | omitted words | unmarked |
| 44 | 020 margin, L17 | "avec les relations" | "avec relations" | added word | unmarked |
| 45 | 021, L22 | σ̃_i | σ̃_a | index | unmarked |
| 46 | 021, L22 | σ̃_{i\|0} | σ̃_a | index | marked |
| 47 | 021, L22 | φ(σ̃_{i\|0}) | φ(σ̇_a), with the tilde struck | struck symbol | marked |
| 48 | 021, L22 | l∞ | a struck l, then l∞ | omitted struck mark | unmarked |
| 49 | 021, L36 | "revenir" | "remonter" | misread word | unmarked |
| 50 | 021, L36 | "à nos" | "τ̇ en" | misread (symbol and word) | unmarked |
| 51 | 021, L36 | "miroirs" | "manières" | misread word | marked |
| 52 | 021, L36 | "d. par" | "à savoir" | misread words | marked |
| 53 | 027, L3 | (no sign under the brace) | "=" | omitted symbol | in the unresolved list |
| 54 | 028, L8 | "scindage" | "remontage" | misread word | unmarked |
| 55 | 030 margin, L33 | (no arrow) | "⟶" | omitted symbol | unmarked |
