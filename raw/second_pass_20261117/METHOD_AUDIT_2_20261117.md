# The Claude second pass, audit 2: what Pro had already marked, what the second pass did with it, and what the mathematics would have caught (17 Nov 2026)

Written by Claude Opus 5.5 at effort max, agent a7d5d89d, with no sub-agents. It follows `METHOD_AUDIT_20261117.md`,
whose recommendation 1 is withdrawn at the user's word. The user, on reading it: "You have a reading, you just never
used it ... You just need to not just visually inspect, you need to work through the math. You just told me that Pro
already marked everything, you just never looked. ... You should make an audit where you actually look."

**What changes from audit 1.** The first pass, GPT-6 Astra (ChatGPT Pro mode), is already the other model family's
reading, with its doubt marks, its doubt files and its notes. No extra blind reading is needed for Pro-transcribed
pages. For pages that Codex (GPT-6 Astra at reasoning effort max) transcribed first, the Codex and Pro readings go
ahead as already planned.

**What I looked at.** I compared the second pass against Pro's own material on five blocks:
- the two controls: 148/044-058 and 145/020-038;
- 149/001-018 (13 Nov, the oldest method);
- 150/085-099 (17 Nov, wave 2);
- 143/001-017 (17 Nov, pilot).

On each, I set Pro's doubt marks, line by line, against:
- every change the second pass made;
- every residual error the controls exposed;
- the second pass's own pages.

I read Pro's doubt files and notes at the error places, and the notes-triage files. I drew a seeded sample of the
triage's "nothing" verdicts and read the full notes behind them.

The scripts are in my scratchpad: `pro_marks.py`, `residual_in_pro.py` and `sample_nothing.py`. **[measured]** marks
what I computed or read myself; **[reported]** marks what comes from a file, named with it.

## 0. In brief

1. **Pro had flagged most of the trouble. The second pass saw the flags but did not work them.**
   - **[measured]** 145 of the second pass's 209 change rows in the five blocks (69 %) sit on lines where Pro had put a
     doubt mark.
   - Pro's pages in those blocks carry 631 doubt marks. The second pass settled or changed 132 of them (21 %) and left
     499 (79 %) exactly as Pro left them, with no recorded decision.
   - Of the 29 residual errors on the controls:
     - 13 sit where Pro had flagged the place itself, in its TeX or its doubt file;
     - 6 sit on a line where Pro had flagged a neighbouring word;
     - 10 had no Pro mark on the line.
2. **When the second pass did work a Pro mark, the right reading was usually not Pro's guess.**
   **[measured]** On 148/044-058 the second pass changed 28 places at a Pro mark:
   - Pro's first reading was confirmed at 7;
   - Pro's other alternative won at 3;
   - a new reading, neither of Pro's, at 14;
   - the alternatives were widened at 4.

   4 of the 28 were later found wrong. Pro's marks point to the trouble, not to the answer, which is why each needs
   working through.
3. **Pro's doubt files carry more than the marks in the TeX, and the second pass did not use them.**
   - **[measured]** For 148/044-058 the doubt file has 153 index rows and 74 rows of readings needing attention.
   - The second pass's files cite none of them.
   - Two residual errors (A8, B1) were flagged only there.
4. **The mathematics would have caught about half the residual errors, often by following Pro's own notes.**
   **[measured, my reading of the pages and notes]** Of the 29:
   - 6 are strongly cued:
     - R24 points to 057 for the polarity of 053;
     - R21 and the pages 047 and 050 make "replaced" the thread that "unifiée" breaks;
     - N22 and display (15) say 145/021 must announce three lifts of τ̇.
   - 8 are cued moderately, and 6 weakly.
   - At 3, the mathematics favours the wrong word.
   - Two of his slips, r(ω) and "du bord de Σ'_ℓ", sit on lines that Pro's notes quote and discuss without seeing the
     type error.
5. **Pro's notes were triaged, but not checked.**
   - **What the triage did.** The triage of 17 Nov, 02:00-05:13 UTC (a9ebc3d6, Claude Opus 5.5 at effort max) read
     4,578 note entries as text and routed them:
     - 56 research items went into the waiting prompts' results blocks, FOR_ASTRA and the notes;
     - about 710 edition matters went to the second pass.
   - **What it did not do:**
     - it did not check the notes' mathematics, the readings they quote, or their references, which were given "from
       memory";
     - nobody has re-examined its 3,812 "nothing" verdicts;
     - it judged 1,247 of those "nothing" verdicts from a few hundred characters of digest.
   - **The sample.** **[measured]** In a seeded sample, 8 of the 9 readable "nothing" notes carry checkable mathematics
     of the kind the companion's groundwork layer needs.
6. **The method, revised on the user's terms (section 5).**
   - The second pass becomes a working-through of every Pro mark, every doubt-file row and every note, and of the
     mathematics of each page. The errors surface because they break the mathematics, and the ink decides.
   - There is no extra blind reading for Pro-transcribed material.
   - The design of the mathematical pass and its pilots is in `PLAN_MATH_THIRD_PASS_20261117.md`. Nothing runs before
     the user has read it.

## 1. What the notes triage did and did not do

**[reported]** RUNBOOK lines 3739-3751; the three files' "Scope and method" sections.

| Pass, time (17 Nov, UTC) | Entries | How read | Research items | Edition matters | "Nothing" |
|---|---:|---|---:|---:|---:|
| Follow-ups, 02:1x-02:2x (`field_experts/FOLLOWUPS_FROM_NOTES_20261117.md`) | 1,669 own ideas and unpursued implications | 1-1125 from a compressed copy (search logs and paths dropped, quotations cut to 160 characters); 1126-1669 as digests (header, location, first 260 characters), from about 715k tokens of context on | 41 | 495 | 1,133 |
| Claims, 03:36-04:22 (`CLAIMS_FROM_NOTES_20261117.md`) | 1,137 unproved claims and conjectures naming no run | all in full, from the compressed copy; "references for known results were given from memory, without searching, as the brief asked" | 9 | 115 | 1,013 |
| Gap, 04:23-05:13 (`GAP_FROM_NOTES_20261117.md`) | 1,772 entries the first two missed: kind not on a "Kind:" line, or untyped | g1-g840 in full (compressed); g841-g1772 as digests (title and first 360 characters) | 6 | 100 | 1,666 |
| **Total** | **4,578** | | **56** | **~710** | **3,812** |

**What it did: routing.**
- **Research items:**
  - into the results blocks of the waiting packages, by `tools_20261113/followup_items.py` (10, 15 and 11 packages
    refreshed);
  - into the last section of `UNPROMPTED_IDEAS_AUDIT_20261117.md`;
  - FOR_ASTRA A6 and A7, FOR_FABLE F19, and `claude_math_notes/NOTES_20261117.md` sections 6-7.
- **Edition matters:** into `second_pass/edition_matters_20261117/`, as step 5 of the second pass. A further 1,387
  claims were mapped by script, with no verdict (`GROTHENDIECK_CLAIMS_MAP_20261117`).

**What it did not do** (from the same files):
- **It did not check the mathematics.** Each verdict judges whether a note is worth following, not whether its proof,
  counterexample or computation is right. The notes' own test computations were not rerun.
- **It did not check the readings.** It worked without scans, so notes built on misreadings were routed as they
  stood. The CTRL-148 verdict, line 145, names R17 "Ceci n'a un sens", U10 "aura" and T01 "raffinement". The second
  pass corrected their quotations later, on its own pages only.
- **It did not open the literature.** Its known-result pointers are from memory and marked "check before citing".
- **Nobody has checked the "nothing" verdicts.** No file or RUNBOOK line records any re-examination of the 3,812.
- **The digest-read part** is 1,247 "nothing" verdicts: 367 in Follow-ups and 880 in Gap **[measured]**, each judged
  on 260-360 characters.

**[measured] What the "nothing" pile holds: a seeded sample.** The draw was 14 entries (seed 20261117):
- 6 digest-read Follow-ups entries;
- 5 digest-read Gap entries;
- 3 Follow-ups entries read in full.

Nine could be matched to their full notes; the rest have headings my matcher did not find (chat-B files and other
heading forms). Eight of the nine carry checkable mathematics:

| Entry | What the full note holds | For the companion |
|---|---|---|
| Follow-ups #1153, 18/027-029 C06 | The orientation choice and the Tate line, α∞(u) = (2√−1 π)⁻¹ v; Deligne's convention Z(n) = (2πi)ⁿZ, cited as [D71, §§2.1.13-2.1.14] | C1 groundwork; the reference to verify |
| Follow-ups #1418, 43/130-133 with 47/7-8, F03 | His unfinished Fourier test at the unit, to be done: evaluate the pullback of θ in every degree | An unfinished computation of his (C1/C3) |
| Gap #1180, 147/171-172 | The "nouveaux" elementary topoi D × D* and D* × D first occur in (281); any minimal system of building blocks must justify omitting a mixed piece | The tower at infinity, a structural point |
| Gap #1082, 136 N73 | Weighted products recover a primitive square: binom(4,2)·binom(4,2) − binom(7,3) = 6·6 − 35 = 1 | C1; the arithmetic checked by me |
| Gap #1225, 149/101 RN101-01 | His "Sans doute pas" to "est-elle admissible ?" is refuted in the stated generality by a ramified quadratic twist (RN103-03/04) | Cote 149; a claim about his claim, unchecked |
| Gap #1353, 15/132 FR17 | His cancelled "L est engendré par un λ tel que λλ̄ = Q" fails over Q(i) with Q = 3: x² + y² = 3z² has no primitive solution (mod 3) | C1; I checked the proof (below) |
| Follow-ups #1123, 16/049 S13 | Positivity kills the radical of a finite rational algebra; Kleiman 1968, §§3.11-3.14 | C1; cote 16 is cited 119 times |
| Follow-ups #574, 146/036-040 R044 | The homotopy squares organised as compatible path comparisons; the compatibility with every defining relation is still to be checked | A proof obligation (C1/C3) |
| Gap #905, cote 11 | The reused typed sheets of other authors | Genuinely nothing further |

**Two check events of mine,** in the form of the 17 Nov rule:
- **MPL_15_087-138 FR17, targeted proof check, confirmed.** Squares mod 3 are 0 and 1. So x² + y² ≡ 0 forces
  3 | x, y; then 3 | z, and descent leaves no primitive solution. Hence 3 is not a norm from Q(i).
- **MPL_136_235-281 N73, computation, confirmed for the arithmetic only.** The application to the manuscript stays
  conditional, as the note says.

So "nothing further" meant "nothing to route to a research prompt or to the edition". It did not mean "nothing of
use": the pile is in large part the companion's C1 material, unverified.

## 2. Were the second pass's corrections, and its residual errors, at places Pro had marked?

### 2.1 The second pass's corrections, against Pro's marks [measured]

**How the script classes each change row.** It tests, in this order:
- does the first-pass reading carry a doubt mark (`\unsure`, `\illegible`)?
- does Pro's page have a doubt mark on that line, or on a line next to it?
- does a row of Pro's doubt index name that line?
- does a Pro note's "Source:" range cover it?

The line numbers of the first and second pass agree. Only 145 scan 020 is shifted, by one line.

| Block | Change rows | Pro mark on the changed word or line | On an adjacent line | Note only | No Pro mark found |
|---|---:|---:|---:|---:|---:|
| 148/044-058 | 43 | 29 | 4 | 6 | 4 |
| 145/020-038 | 42 | 36 | 2 | (notes not parsed) | 4 |
| 149/001-018 | 26 | 16 | 4 | (not parsed) | 5, and 1 with no line |
| 150/085-099 | 44 | 32 | 1 | (not parsed) | 11 |
| 143/001-017 | 54 | 32 | 7 | (not parsed) | 15 |
| **All** | **209** | **145 (69 %)** | **18 (9 %)** | **≥ 6** | **39 (19 %)** |

The note formats differ from package to package. My parser read the "Source:" lines of 148 only, so the
"note only" count is a floor.

### 2.2 The 29 residual errors, against Pro's marks [measured]

The error ids are those of `METHOD_AUDIT_20261117.md`, Appendix C. The Pro text is the line of its page TeX; the doubt
rows are from its doubt file.

| Where Pro's marks were | Errors | What the second pass did there |
|---|---|---|
| **Pro had flagged the place itself** (the word, the phrase or the whole margin, in its TeX or its doubt file) | A1, A2, A4 (044 margin: "tout pris en détail", "au", "œcuménique", "groupe" marked; the doubt file: "The sloping marginal note is partly clipped ... provisional", low); A8 (doubt file: "disjointes ... The inserted adjective ending is slightly uncertain", medium); A11 (`\unsure{sauf si\|si}`, `\unsure{doive\|doit}` low; the doubt file: "The entire marginal argument is low confidence"; note R24 declines to use the polarity); B1 (doubt file: "MD = modulaire; Mumford–Deligne ... modulaire is a provisional reading"); 46, 47 (σ̃_{i\|0}, low); 49-52 (`\unsure{miroirs}`, `\unsure{d.}`, medium); 53 (the brace label marked) — **13** | Left doubtful: A1, A2, 46, 47, 51, 52, 53, and 49-50 unmarked inside the marked phrase. Settled wrongly: A4 (to Hua's alternative) and A11 (polarity). Flag in the doubt file not used: A8, B1. **None of the 13 was resolved correctly.** |
| **Same line, Pro flagged another word** | A10 and B3 (`\unsure{où}` on 051:5); B2 (`\unsure{aussi}` on 051:4); A12 ("pq", "liées" on 055:19); 45 (σ̃_{i\|0} later on 021 L22); 54 (marks on 028 L8) — **6** | The flagged neighbour was worked; the unflagged word beside it was accepted. |
| **No Pro mark on the line** | A6, A7 (Pro was right; the second pass introduced the error), A9, B4, B5, B6, 43, 44, 48, 55 — **10** | Small omissions and added words: struck marks, insertions, an arrow, "en fait", "-traduction", "du Γ". These are found by ink coverage, not by any mark. |

## 3. How many of Pro's marks the second pass checked, and what checking found

| Block | Pro's doubt marks on the pages | Settled or changed by the second pass | Left exactly as Pro left them | Second pass's marks after |
|---|---:|---:|---:|---:|
| 148/044-058 | 164 | 38 | 126 | 167 |
| 145/020-038 | 161 | 32 | 129 | 157 |
| 149/001-018 | 87 | 14 | 73 | 81 |
| 150/085-099 | 112 | 25 | 87 | 120 |
| 143/001-017 | 107 | 23 | 84 | 112 |
| **All** | **631** | **132 (21 %)** | **499 (79 %)** | **637** |

**[measured]** A mark left in place may have been looked at and found undecidable. Or it may never have been looked at.
The method keeps no record of a decision per mark, so the files cannot tell which. Some were plainly not re-read: "The
first pass's other doubt marks on these scans that I did not re-read one by one (chiefly the many tokens of the 053
diagonal margin ...) are kept as they were" (148 changes file, lines 114-115). That 053 margin is where the polarity
error sat.

**What checking found, where it was done [measured on 148/044-058].** The second pass changed 28 places that carried a
Pro mark:

| Outcome | Places | Rows | Later found wrong |
|---:|---:|---|---|
| Pro's first reading confirmed | 7 | 21, 22, 24, 30, 35, 36, 43 | |
| Pro's other alternative right | 3 | 6, 33, 38 | 33, the polarity |
| A new reading, neither of Pro's | 14 | 2, 3, 5, 7, 13, 15, 16, 19, 25, 26, 29, 32, 34, 40 | 2 |
| Alternatives widened | 4 | 1, 4, 20, 41 | 1, 4 |

So a Pro mark is a reliable pointer to trouble, but its alternatives are often not the answer. Each mark needs real
work on the ink, and the mathematics.

**The doubt files.**
- **[measured]** 148's doubt file has three parts:
  - a notation table;
  - "Readings requiring attention": 74 rows for scans 44-58, with position, reading, reason and confidence;
  - an "Index of local doubt marks": 153 rows for scans 44-58, each with the page TeX line.

  The second pass's changes and notes files cite none of these rows.
- The formats differ by package. 145, 150 and 143 also give TeX line numbers, so each package's file needs its own
  parse into one place list.

**The notes.** The second pass checked every note's quotation on its pages:
- about 1,139 kept, 186 corrected and 9 dropped, in 46 files (audit 1, section 3.2);
- on 148/044-058 about 36 entries.

It did not work through what the notes say (section 4).

## 4. Where working through the mathematics would have caught an error

**[measured: my reading of the corrected pages, Pro's pages and Pro's notes at each place]**

| Error | What the mathematics or sense says, and where the cue was | Strength |
|---|---|---|
| A11 (148/053:40, polarity) | Pro's R24 left the polarity open and said "the clearer partial/total formulations are on 057 and 061". 057:11 reads: "le gommage partiel est en fait un renforcement de structure, pas un affaiblissement". So total erasure on a component weakens, and partial erasure strengthens. The 053 margin must say "lorsqu'on gomme tous les repères ... sinon ... renforcement". The second pass even wrote the clash down (its N4), and reconciled it in prose. | strong |
| B3 (148/051:5, "unifiée") | The thread of 047-051 is replacement. 047:33 margin: "remplacée par celle d'un pol. comb."; 050:4: "la partie ρ de la pondération est \deleted{complétée} \inserted{remplacée} par une structure"; Pro's R21: "050 explicitly replaces the numerical ρ-part by sets R_a". "la famille des R_a serait remplacée par un contour combinatoire" continues it; "unifiée par" breaks it. | strong |
| 49-52 (145/021 L36) | Display (15) follows at once and gives the three lifts τ₀, τ₁, τ∞ of τ̇. Pro's N22: "Three lifts of complex conjugation ... 028–029, the lifts τ₀, τ₁, τ∞". The line must announce lifts: "remonter τ̇ en trois manières, à savoir". "revenir à nos trois miroirs, d. par" announces nothing. | strong (4 errors) |
| A1, A2, A4 (148/044 margin) | The margin decides which groupoid gets the plain name T. In the arithmetic setting, complex conjugation reverses orientation, so T^± against T^+ is exactly an arithmetic question. "tout pris en détail, au point de vue œcuménique" is empty. "tant qu'on ne travaille pas au point de vue arithmétique" is the expected content (the second pass's N8, written after the correction). | moderate (3) |
| A10 (148/051:5) | "Il peut être plus commode dans la donnée d'ensemble de la structure" does not parse as French. | moderate, by sense |
| 45-47 (145/021 L22) | Pro's N21: "The author then proposes changing the tilde notation and reserving it for lifts to Sℰ"; the "Critique" margin is on this page. A reader following N21 examines every tilde on 021, and finds the struck tilde of φ(σ̇_a) and the index a. | moderate (3) |
| 54 (145/028, "scindage") | His word for this operation on 021-035 is "remonter" ("remonter τ̇", "aimerait remonter à Sℰ", "remonter les 2-groupes"). "le remontage correspondant" keeps the vocabulary. | moderate |
| B5, B1, 43-44, 53, 55 | B5: "for each object, reconstruct (up to unique isomorphism) the corresponding graph", singular. B1: a "!" inside a definition is odd. 43-44: "en fait" against N18's corrected presentation. 53: the brace says what the group is. 55: the margin's relations. | weak |
| A6, A7, A9, A12, B4, B6, 48 | Struck marks, insertions, added or omitted small words, with no mathematical content. They need ink coverage. | none |
| B2, A9, A8 | The mathematics favours the wrong word: "implique" for "indique", an "en prenant" before a display, "sommes disjointes". | wrong way |

**In total:** 6 strong, 8 moderate, 6 weak, 7 none and 3 wrong-way, out of 29. The weak count includes 43 and 44
separately. The three wrong-way places overlap with the other groups.

**Pro's notes held the cue for 9 of the 14 strong and moderate catches:** R24, R21, N22 and N21. So the user's
statement holds in substance: the material was there, and the second pass looked at it as quotations, not as
mathematics.

**His slips.**
- **050:54, r(ω) = 1 ou r(ω) = 2.** r is defined on A (r : A → N), so r(a) is meant. Pro's R22 quotes this very line
  ("Même si ... 1 ... 2") and discusses "the r = 1, 2 cases" without seeing the type error. The second pass also
  missed it. GPT-6 Astra's control notes caught it.
- **055:7, "les composantes connexes du bord de Σ'_ℓ".** Σ'_ℓ is a closed 1-submanifold of ∂X, so it has no
  boundary. Pro's Q3a, Q3e and R34 cover 055:4-8. The second pass kept them ("No change on these lines"). GPT-6.2
  Sol's control notes caught it.

Working through the types catches both.

**The rule this confirms.** At three of the 29 places, the mathematics favours the wrong word. So mathematics raises
the alarm and sends the reader back to the ink, and the ink decides. Where the ink stays open, the expected reading may
become an alternative, never the first reading.

## 5. The method, revised on the user's terms

1. **No extra blind reading for Pro-transcribed pages.** The Pro first pass is the second family's reading, and its
   marks, doubt files and notes are the place list.
   - For pages the Codex route transcribed first (GPT-6 Astra at reasoning effort max): the Codex reading, plus the
     Pro second passes with notes, as already planned (`SECOND_PASS_CODEX_NOTES_TEMPLATE.md`, folder 4).
   - Hua's transcription stays a credited witness. It is Claude Opus 5.5, the same family as the checker, so it is
     never enough alone.
2. **The pass works through everything Pro marked, and records a decision for each:**
   - **every doubt mark in the TeX:** confirmed, Pro's alternative, a new reading, or open with all the alternatives,
     each with its crop;
   - **every row of the doubt file,** both tables. These are parsed per package into `PLACES.tsv` before the pass
     starts;
   - **every note on the pages:**
     - its anchor read on the ink;
     - its mathematics worked through: tests rerun, claims checked, pointers followed (R24 to 057);
     - a verdict, with a CHECK_EVENTS row (17 Nov rule);
   - **every triage verdict on these notes,** including the "nothing" ones: confirmed, or overturned, with the reason.
3. **The pass works through the mathematics of each page.** This is the design of
   `PLAN_MATH_THIRD_PASS_20261117.md`:
   - what each unit does;
   - the type of every symbol;
   - consistency with the pages before and after, and with the notes;
   - his claims and slips.

   Every alarm goes back to the ink as a place, read blind on a native-resolution crop before the alternatives are
   seen.
4. **Ink coverage stays,** for the omissions no mark announces: 10 of the 29 residual errors. Every mark of ink on the
   strip is accounted for.
5. **Kept from audit 1:**
   - native-resolution crops (C5);
   - the watch list of logic-bearing words (C4);
   - `PLACES.tsv`, now seeded with Pro's marks and doubt-file rows (C7);
   - for low-confidence decisions, an adjudicator who is not the reader of record (C8);
   - consequential corrections reported by confidence (C11);
   - notes routed with CHECK_EVENTS (C10);
   - normalised diffs where two readings are compared (C12).

   **Withdrawn:** C1 (a blind reading first for Pro pages). C2 and C3 now act on Pro's place list, and on the
   mathematics' alarms. The economy paragraph and the 120-call cap go: the work is budgeted by the number of Pro marks
   and notes.
6. **Splitting the work between Claude and Pro, as compute allows:**
   - **Claude Opus 5.5 at effort max:** the working-through of Pro's marks and notes and of the mathematics, on the
     companion's chapters first (waves A and B of audit 1, section 7). Also the adjudication, and the C1 drafts.
   - **Pro:**
     - the remaining first passes;
     - notes for pages transcribed by the Codex route (folder 4);
     - possibly a Pro pass that works through its own marks and notes against the scans and the mathematics before
       Claude, if the pilot shows that Pro-then-Claude matches Claude alone at less Claude meter.

     Pro costs no money per prompt (a flat subscription). Its limit is slots: about 200 on account 4 until 21 Nov,
     then accounts 1 and 3.
   - **The rule:** Claude's weekly meter goes to the pages where the mathematics matters most. Pro's slots go to
     reading and notes everywhere. The pilot in the plan decides whether Pro takes a share of the working-through.
     The user's word of 17 Nov, 22:3x UTC ("Second pass is go at max") stands: the pass of record is Claude at effort
     max.

## 6. Corrections to audit 1

- **Recommendation 1** (a blind reading by another family first) is withdrawn at the user's word. The text is marked
  so in `METHOD_AUDIT_20261117.md`.
- **The notes were used.** The triage of a9ebc3d6 routed them (section 1). Audit 1's "Pro's notes are checked for
  their quotations, not processed" holds for the second pass only, and is corrected there.
- **"About 1,200 unresolved places"** in audit 1 are the second pass's own lists, not Pro's.
- **Pro's own flags** are the 631 TeX marks on the five blocks examined here. For 148/044-058 its doubt file holds 227
  further rows (153 in the index, 74 needing attention).
- **"About 3,800 'nothing'"** are the triage's verdicts on Pro's notes, not unread notes.
