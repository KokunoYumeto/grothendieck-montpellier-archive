# Pilot verdict: OBJ_H035, the first working-through object run (19 Nov 2026)

- **Judge:** Claude Opus 5.5 at effort max (sub-agent a7d5d89d). The judgement follows
  `grothendieck_archive_transcription_20261110/second_pass/PLAN_WORKING_THROUGH_PRO_20261118.md`, section 5, and
  was written on 19 Nov 2026, from about 11:00 to 12:30 UTC.
- **Run judged:** `001_OBJ_H035_O`, made by GPT-6 Astra (ChatGPT Pro mode). The run says that its environment did not
  show an effort setting.
  - It started at 02:54:34 UTC.
  - Under the user's rule, checkpoint 04 (05:54:37 UTC) is the final: the run has been silent since then.
  - By its own checkpoint script, checkpoint 05 was due at 06:39:34 UTC. It had not arrived in
    `working_through_20261118/returns/` at 11:55 UTC.
- **Return:** `working_through_20261118/returns/OBJ_H035_checkpoint_04_20261119T0554Z_unzipped/OBJ_H035/`.
- **Prompt as sent:**
  `TO_SEND/_SENT/PRO/F_Archive_working_through_200/17_working_through_wave1_001-040/batch_1_001-017/001_OBJ_H035_O/PROMPT.md`.
- **Labels:** [measured] means I read or computed it myself. [reported] means the run or another file says it.

## Verdict: adjust the prompt and the builder, then scale

1. **The mathematics is strong.** The run took the object over its whole span on the page, scans 2-24, not only the
   12 scans the notes cite.
   - It covers 46 statements and gives each a precise modern form.
   - Proofs, counterexamples and literature locators are in `PROOFS.tex`, and every one of the 6 entries is split
     into 44 subclaims.
   - I worked through ten statuses again. The mathematics held in all ten [measured].
   - Its best find is real: Grothendieck's marginal claim on scan 11 is false (H035.21). The claim says that the
     conditions of EGA IV 6.11.8 suffice for a generic canonical module.
2. **Two of the ten statuses are wrong, for reasons the prompt can prevent.**
   - **H035.5 is a misreading.** Proposition 3 is called "false as written" because the zero quotient is not excluded.
     But "non nul" is inserted in the ink on scan 4. The supplied transcription also has it
     (`transcriptions/cote_94.tex`, line 79).
   - **H035.44 is an anachronism.** "Fibré vectoriel V(F)" with F coherent is called false because V(F) need not be
     locally free. But fibré vectoriel is the EGA term for Spec Sym(F) with any quasi-coherent F (EGA II 1.7.8; I
     cite this locator from memory, and it is still to be checked).
   - **The 13 rows "false as written" mix three kinds:**
     - 3 errors in his mathematics;
     - 8 slips of the pen or omitted conventions;
     - the 2 cases above.

   A reader of the entry cannot tell these kinds apart.
3. **The entry does not give his statements in his terms.**
   - In all 46 rows, the column `his_words` holds a label of at most 40 characters (« Théorème 12 »), not his
     statement.
   - Section 3 of `ENTRY.md` goes straight to "Our precise formulation".
   - 26 rows have the status "proved in the explicitly stated reconstruction", which does not say whether his
     statement holds as he wrote it.
   - The column `later` is boilerplate in 30 of 46 rows, and `confidence` in 44 of 46 [measured].
4. **Time.**
   - The plan gave the run 24 minutes (`OBJECTS_PLAN.tsv`, line 338).
   - The run needed 2 h 03 min to reach a complete entry, and settled its main statement at 1 h 58 min [measured,
     `progress.log`].
   - Under the prompt's stop rule it would have gone on at least until about 07:54 UTC (5 h). The two items holding it
     there are a programme with no definition on the page and a side question.
   - 606 of the 675 objects in the plan carry open-question entries [measured, `OBJECTS_PLAN.tsv`]. Most object runs
     would therefore have the same tail.
5. **The rest of the format was followed.**
   - Checkpoints came every 45 minutes, without nesting.
   - The results zip was opened only after the entry had been frozen with a sha256.
   - The check events do not overclaim: a self-recheck is recorded as a "targeted proof check".
   - Every program the run ran is kept, with its output.

The changes are listed in section 7. Prompts 002-200 should be rebuilt with them before any further one is sent.

## 1. Time and checkpoints [measured, `progress.log`]

| UTC (19 Nov) | Elapsed | Event |
|---|---:|---|
| 02:54:34 | 0:00 | start |
| 02:59:32 | 0:05 | fetched `https://grothendieck.umontpellier.fr/94.pdf` (`scripts/fetch_archive.out`); rendered scans 15-24, which were not attached (`scripts/render_scans.out`) |
| 03:39:50 | 0:45 | checkpoint 01 |
| 04:20:08 | 1:26 | second checks of H035.1-21 done |
| 04:24:44 | 1:30 | checkpoint 02 |
| 04:52:27 | 1:58 | main theorem H035.30 second-checked; all 44 note subclaims have verdicts; H035.39-40 open |
| 04:57:19 | 2:03 | pre-results entry written and frozen (sha256 in `research/ENTRY_BEFORE_RESULTS.sha256`) |
| 04:57:32 | 2:03 | results opened: zero citing rows; `CONSEQUENCES.tsv` correctly left with its header only |
| 05:05-05:29 | 2:11-2:35 | two reductions of H035.39 (composition of "constructible" functors) |
| 05:49:43 | 2:55 | "no new gate movement since 05:29" |
| 05:54:37 | 3:00 | progress review 01, "movement = yes" (H035.30 was proved inside the review period, so this is correct); checkpoint 04 |

- **The checkpoints.** `scripts/checkpoint.py` refuses to write a checkpoint before 45 × N minutes have passed and never
  overwrites one. It leaves out every .zip file and the attached sources. All four checkpoints came within 20 seconds
  of their due time.
- **What the stop rule would have done.** The next review was due at 06:54 UTC. Neither open item could change status:
  - H035.40 has no definition on the page;
  - H035.39 is a research question.

  So the reviews at 06:54 and 07:54 would both have found no movement, and the rule stops the work after two such
  reviews: about 5 h of run time in all. Without that tail, the object took about 2 h.
- **The plan's estimate.** `est_minutes(6 entries, 1,806 words, 12 pages) = 24` (`build_object_prompts.py`, line 197).
  The builder's docstring quotes the user: "200 prompts that take like 30 minutes or an hour". Two things made the
  real object larger than the estimate:
  - its statements run over 23 pages, not the 12 the notes cite;
  - it has 46 statements of his, not 6 entries.

## 2. The corrections, checked on the scan (section 5, item 1)

**What I compared.** I checked all 32 rows of `READINGS.tsv` against the run's own crops in `readings/`, reduced to the
scan's native resolution. For three places I also looked at the attached scans themselves. The run also rendered
scans 15-24 from the archive PDF; for those pages I compared its crops with the supplied transcription. I read every
place myself and used no OCR. [measured]

**The result: 31 rows confirmed or fairly graded, 1 row wrong, and that row changes a status.**

| Row | Place | The run says | The ink, as I read it |
|---|---|---|---|
| 5 | 94/004, Prop. 3 (iv) | "No nonzero qualification visible at this locus" (medium-high); hence H035.5 "false as written" | "non nul" is written small under "lim" on the line above, with a curved leader down to "B" in "Pour tout quotient B de A". It is the same gesture as the "non nul" over B in Théorème 12 (vi) on scan 16, which the run did read. The supplied transcription has `\inserted{non nul}` (cote_94.tex, line 79), and the Work note said "nonzero quotient". **Wrong.** |

**Rows confirmed on the ink, where the decision turns on a word:**

| Row | Place | What the ink shows |
|---|---|---|
| 15 | 94/010 | `Tor_1(M,H^1(K·)) = Tor_1(M,Z^1(K·)) = 0`, with Z^1 |
| 17 | 94/010 | `K·: 0 → L_0^∨ ⊗ P → L_1^∨ ⊗ P → 0`: P twice |
| 19 | 94/011, margin | "il suffit qu'il soit excellent, ou seulement qu'il satisfasse les conditions de EGA IV 6.11.8" |
| 21-22, 24 | 94/012, typescript | "tout élément n.1 est une racine de l'unité"; "un nombre réel s"; "f(x)=0 entraîne x=0" |
| 28 | 94/016, Th. 12 (vi) | "non nul" inserted over B |
| 30 | 94/021, Lemme 17 | "il existe un ouvert dense U de S tel que ∀ s ∈ S" |
| 32 | 94/023 | `Hom(F, f^*(M)) ≃ Hom(P,M)`, with no f_* |
| 33 | 94/024 | "par l'exposé Murre, th. 3" |
| 12 | 94/008 | "Utilisant le fait que F(N) est de type fini" |
| 3 | 94/003, Lemme 2 | the test modules are "M un Â-module de t.f.", with Â = lim A/(f^n) |
| 6 | 94/005, Prop. 4 (iv) | "(il suffit que ce soit vrai pour M de t.f. sur A)" |

**Rows where the run kept a doubt, and the doubt is fair:**
- row 10: the mark after "représentable" on scan 7;
- row 11: égal/égale (I lean to "égale"; no consequence);
- row 16: the final index s/n;
- row 20: whether "de" is cancelled;
- row 29: the graded symbol (the run withdrew its own earlier reading);
- row 2: the mark after Ω^1 on the cover.

**Rows I checked only in part:**
- **Row 27** (scan 15, strictness): the crop shows "filtrant strict" inside the cancelled draft. For the rewrite, the
  supplied transcription (line 327) has no "strict" and no "de t.f.", while the use of the corollary on scan 17 (line
  399) has both. This agrees with the run.
- **Row 13** (scan 8, the normality clause): checked against the transcription (line 163) only.

**On scope.** Scans 15-24 were not attached; the run fetched cote 94's PDF from the archive and cropped them itself
(`scripts/fetch_archive.py`, `render_scans.py`, `readings/CROP_MANIFEST.tsv`). On those pages it read its own
renderings correctly wherever I checked. A Pro session without network access would have had to decide the ink there
from the transcription alone. See builder change B2.

## 3. Ten claim statuses worked through again (item 2)

My checks are at the level of the argument: I re-derived the key steps and recomputed the counterexamples by hand. I
did not open the literature, as the context guard requires at this point. So the run's locators in Hall 2014, Lyu 2025,
Murre exp. 294 and the Stacks tags are not checked by me.

| Id | The run's status | My check [measured] | Outcome |
|---|---|---|---|
| H035.30 (Théorème 12, the main question) | proved "in the explicitly stated reconstruction" | Necessity re-derived: (vi) from Corollaire 7 on a CM open, which exists by Corollaire 10. In the sufficiency chain I followed every step (H035.5 → .7 → .10 → .8 → .19 → .29) and re-derived the decisive one: F(Ω) finite makes the strict chain Hom(P_i,Ω) stabilize; the parameter comparisons sandwich Hom(P_{i0}, Ω_p/q) ↪ Hom(P_j, Ω_p/q) ↪ colim, so both maps are isomorphisms; H035.27 then gives (P_j)_p ≅ (P_{i0})_p. | **Confirmed.** His theorem holds as he wrote it, including the "non nul" he inserted in (vi). The status words should say so. |
| H035.27 (Cor. 10 c) | proved | Re-derived without reading the run's proof: Matlis duality over the artinian A/q turns the Hom isomorphisms into R/qR ≅ R'/qR' for every parameter ideal; parameter ideals are cofinal with the m-adic topology; completion is faithfully flat. | **Confirmed.** The surjectivity he assumes is indeed not needed. |
| H035.29 (Cor. 11, scan 15) | false as written | Ink and transcription as in row 27. The counterexample holds: P_i = k with zero transitions gives F = 0 = Hom(0,−), and the system is never stationary. The corrected statement follows by the H035.30 argument. | **Confirmed. A slip:** "strict" and "t.f." were dropped in the rewrite, and he has both in the draft and where he uses the corollary. |
| H035.5 (Prop. 3) | false as written: zero quotient | Ink and transcription have "non nul" (section 2, row 5). He also writes "A ≠ 0" at the head of the proof on scan 5. | **Refuted. His statement holds as written**, by the run's own proof of its "corrected" statement, which is his. |
| H035.10 (Remarque 5 bis, converse) | false as written | L = Σ_p (1/p)Z ⊂ Q: torsion-free, hence flat; L_(p) ≅ Z_(p); dim L/pL = 1 = dim L⊗Q; no L[1/n] is finitely generated. The repair (F(B) finite) holds: on the constant-rank open, μ(Q_p) = generic rank makes Q_p free, and F ≅ F(B)⊗−. | **Confirmed. An error in his mathematics:** he uses "F(N) est de type fini" (scan 8), which his hypotheses do not give; he supplies it later as Théorème 12 (iv). |
| H035.14 (the Hom complex) | false as written | The crop shows ⊗P twice. With P = k and Q = k², Hom(P,Q) = k² while the written complex gives k. | **Confirmed. A slip:** P for Q. |
| H035.15 (the Z^1 criterion) | false as written | Recomputed: A = k[x,y]/(xy), M = A/(x), K = [A →y A]. Then Tor_1(A/x, A/y) = 0 (x acts injectively on k[x]) and Z^1 = K^1 = A is free, while H^0⊗M = xA/x²A ≅ k and H^0(K⊗M) = ker(y on k[y]) = 0. With B^1 the criterion holds; I re-proved it from the two short exact sequences. | **Confirmed. An error in his mathematics** (the criterion). The Corollaire 7 it serves is true. |
| H035.21 (the margin on EGA IV 6.11.8) | false as written | The margin text is confirmed (row 19). The counterexample holds in outline: localize k[t_i^3, t_i^4, t_i^5 : i ≥ 1] at the complement of the union of the block ideals. The result is noetherian by Nagata's criterion: each local ring is noetherian, and each nonzero element lies in finitely many maximal ideals. It is one-dimensional and CM. The semigroup ⟨3,4,5⟩ is not symmetric, so the local rings are not Gorenstein, and every nonempty open contains such a point. A rank-one canonical module would be free on a smaller open, so those points would be Gorenstein. | **Confirmed. An error in his mathematics** (an overreach in his margin), and the run's best catch. |
| H035.38 (Lemme 17) | false as written: ∀ s ∈ S | The crop confirms "∀ s ∈ S". The counterexample is recomputed: on P^1 over k[t], take the extension of O by O(−2) with class t. The connecting map O(P^1) → H^1(O(−2)) = k[t] is multiplication by t, so H^0(E) = 0; at t = 0 the extension splits, and H^0(E_0) = k. | **Confirmed. A slip:** he introduces U and then writes S. |
| H035.44 (the 1st case of Th. 19) | false as written: "vector bundle" for coherent F, and f_* missing | The f_* is indeed missing (crop, row 32). But the page says "Z est un fibré vectoriel V(F), avec F cohérent" (transcription line 564). In EGA's language this is a definition (V(E) = Spec Sym(E) for any quasi-coherent E, EGA II 1.7.8; locator from memory, to be checked), not a claim of local freeness. | **Refuted in part.** The "vector bundle" falsity is withdrawn, since it is his and EGA's term, translated wrongly. The f_* slip stands. |

**What the ten show.**
- The run's mathematics is reliable. Its labels are not:
  - one status rests on a misreading;
  - one rests on reading a 1965 term in its 2026 sense;
  - "false as written" is used for slips and for real errors alike.
- **All 13 "false as written" rows, sorted from my checks of the ink and the transcription:**
  - errors in his mathematics: H035.10, H035.15, H035.21;
  - slips or omitted conventions:
    - H035.8 (f ≠ 0 in Lemme 5 (v));
    - H035.14;
    - H035.22, H035.24, H035.25, H035.26, the typescript leaf on scan 12. For example, n·1 = 0 at n = p, and the
      trivial absolute value is not excluded;
    - H035.29;
    - H035.38;
  - H035.5: misread;
  - H035.44: a slip, plus the anachronism.

## 4. Ten note verdicts worked through again (item 3)

The notes are 6 Work notes (GPT-6.2 Astra at reasoning effort max, ChatGPT Work). The run gave verdicts on 44 subclaims
of them (`NOTES_VERDICTS.tsv`). Ten of those, worked through again [measured]:

| Entry and subclaim | The run's verdict | Mine |
|---|---|---|
| #1, Proposition 3 | "corrected anchor": the note "silently says nonzero quotient" | **Wrong.** The note was right; "non nul" is on the page. |
| #2, "Nécessité claire" | confirmed, "Proposition 3 must exclude the zero quotient" | **Partly wrong.** The boundary part rests on the same misreading; the rest stands. |
| #1, Remarque 5 bis | forward implication confirmed; converse refuted | Right (section 3, H035.10). |
| #1, Corollaire 7 | result confirmed; the proof's P and Z^1 corrected | Right (H035.14, H035.15). |
| #1, Corollaire 10 and its margin | main hypotheses confirmed; margin partly refuted | Right (H035.21). |
| #2, the two-Tor criterion | refuted, not merely unproved | Right (H035.15). |
| #3, the mark after "est représentable" | not checkable as a question mark | Right: the mark is ambiguous on the crop. |
| #4 S10.1, P in the complex | correction confirmed | Right. |
| #4 T12.1, the root-of-unity sentence | literal sentence refuted; "nonzero" repair confirmed | Right: a slip. |
| #5, the pointer to EGA IV 6.11.8 | pointer confirmed; the enlargement refuted | Right. |

**Result: 8 right, 2 wrong.** Both wrong verdicts come from the one misread insertion. The run also confined its "no
other conjecture" verdict on #3 to scans 2-13 and recorded the programme on scan 22 separately (H035.39-40). That is
correct: the crop of scan 22 shows Remarque 18:
- the class: the "foncteurs satisfaisant aux conditions du th. 12, sauf l'exactitude à gauche (ii)";
- in the margin, "(additifs ?)";
- the programme itself: "Il faudrait ... définir de même la notion de foncteurs constructibles Qcoh(Y) → Qcoh(X). Il y
  aurait à voir : composé de foncteurs constructibles est constructible, foncteurs Ext, Tor, R^q f_* ...".

## 5. One unit's groundwork, read as the expert reader would read it (item 4)

An object entry has no units. I read the groundwork of its central unit, Théorème 12: its block in section 3 of
`ENTRY.md` (lines 511-524), section 4, "The proof of the central criterion" and the inputs table (lines 749-825), and
section 5 (lines 826-851).

**What serves the reader.**
- The proof map is correct, and so is its account of why the theorem survives the defective drafts it rests on.
- The literature table is real work, with page locators and URLs: EGA III₂ 7.7.6-9; EGA IV₂ 6.11.8-9; Murre, exp. 294;
  SGA 3 VIII 6.4; Jaffe; Hartshorne; Hall 2014; Lyu 2025.
- It distinguishes Théorème 14 from EGA III 7.7.8's extra hypothesis.
- It refuses a novelty claim.

**What an algebraic geometer would miss beside his page.**
- **His statement.** The block shows « Théorème 12 » and then "Our precise formulation". It never says what he wrote, in
  his notation and order. The prompt asks for this under Rules ("His terms first"), but its output specification
  does not require it. The run generated section 3 from `STATEMENTS.tsv`, whose `his_words` column holds labels.
- **The terms of his time.** The terms "proreprésentable", "strictement proreprésentable", "faisceau fondamental" and
  "fibré vectoriel" are given only in today's sense, without the definitions his sources gave them:
  - FGA and Bourbaki exp. 195 for pro-representability;
  - EGA II for V(F).

  The error in H035.44 comes from this.
- **What was known when he wrote.** The prompt asks for this in section 4 of the entry; it is absent. The inputs table
  cites Stacks tags, not the EGA, FGA and Bourbaki results of 1960-65 that he used.
- **Whether his statement holds as written.** The status words do not say. For H035.30 the answer is yes, and the reader
  should find it in one word.
- **One reference to check.** The bibliography entry `Murre294` is titled "Les schémas de Picard". As far as I know,
  exp. 294 is Murre's "Representation of unramified functors. Applications" (I am citing this from memory, so it still
  has to be checked against Numdam). All 33 entries carry `note={verified}`.

## 6. Format (item 5)

**Against the template's "What to return":**
- All nine deliverables are there, and `ENTRY.md` has its eight sections.
- The columns of `STATEMENTS.tsv` (12), `NOTES_VERDICTS.tsv`, `READINGS.tsv` and `CHECK_EVENTS.tsv` (6) are as
  specified.
- `CHECK_EVENTS.tsv` has 145 rows. Its types are not overclaimed: the same run's second pass is recorded as a "targeted
  proof check — independent second pass from hypotheses", and background sources as background.
- **`LINKS.tsv` holds its header only.** The context zip gave the nearby objects' tags and names, not their statements,
  so no relation could carry evidence. The run says so in section 6 of the entry; that is honest, but useless to a
  reader.
- **`CONSEQUENCES.tsv` holding its header only is correct:** `RESULTS_CITING.tsv` had zero rows.
- The first line of `ENTRY.md` says "Working entry"; at a checkpoint this is correct.

**Against `COMPANION_DESIGN_20261118.md`, section 2.7** (the fields of claims.json):
- `STATEMENTS.tsv` maps onto claims.json except for three fields:
  - "as he left it (status and date)": the run's status is our verdict, not his;
  - "unit": object runs have none;
  - "developed further".
- The column `later` would feed claims.json's "later". It holds boilerplate in 30 rows.

## 7. The adjustment

### 7.1 In `OBJECT_PROMPT_TEMPLATE.md`

**T1. Status words.** Add this after the (a)/(b) list in "What the outcome must be":

> **Status words.** A status says first whether his statement holds as he wrote it, read in the sense his terms had
> when he wrote: EGA, SGA, FGA and the Séminaire Bourbaki define most of them (give the locator).
> - *True as written.*
> - *Slip*: the statement holds once an evident slip of the pen or an omitted standard convention is fixed (a nonzero
>   ring, a positive exponent, the open set he has just introduced). Name it, give the evidence on his pages (the same
>   condition elsewhere, the notation just introduced), mark the judgement as ours, and put the counterexample to the
>   literal wording in `PROOFS.tex`.
> - *False*: his mathematics fails as he meant it. Give the counterexample and the corrected statement.
> - *Known*, or *open*.
>
> A term whose modern sense differs from his (fibré vectoriel, préschéma, proreprésentable, faisceau fondamental) is
> translated, never refuted.

The phrase "proved in the explicitly stated reconstruction" goes. A slip and a false statement remain decided
outcomes (b), so nothing is lowered.

**T2. Readings against the supplied reading.** Add this to step 3:

> Where your reading differs from the supplied reading of the page (`PASSAGES.md`, `transcriptions/`) by an insertion,
> a deletion or a word, the `READINGS.tsv` row quotes the supplied reading and says what the ink shows. No statement is
> called false on a reading that leaves out part of the supplied reading without such a row.

This would have caught H035.5.

**T3. His terms in the outputs.**
- In `STATEMENTS.tsv`:
  - `his_words`: "his statement in his notation and order: his short quotations joined by a close paraphrase, enough
    to read the statement without the page";
  - a new column `as_he_left_it`, after `date`: stated / proved on the page / sketched / asked / hoped / cancelled /
    programme;
  - `later`: what became of the statement (his published work, the work of others, today), never a pointer to our
    proof;
  - `confidence`: per row, with its reason.
- `ENTRY.md`, section 3, prints `his_words` before today's statement.
- This also gives claims.json its "as he left it" (section 6).

**T4. Programmes.** Add this to "The items":

> A programme or a question whose terms the page leaves undefined is an item through the precise versions the page
> supports. Decide each version as its own row. The programme's row records what it asks and the definitions it would
> need, with the status *programme*.

H035.40 would then not be held "open" forever. H035.39 is his own question (Remarque 18: is a composite of constructible
functors constructible?) and stays an item. This is a new status word, so the coordinator should decide whether it
fits the user's push rule. I think it does, because only statements can be proved or refuted.

**T5. The stop, scaled to an object run.** Replace the heading and the first sentence of the progress check with:

> **Progress check at one hour** (the user's rule of 13 November 2026, amended on 17 November 2026, on the clock of an
> object run). After about one hour of work, and every 30 minutes after that, review the work against a dated ledger
> ...

The rest stays word for word: "Movement means only ...", "two consecutive reviews". This is how an object run stops
once its main statement is settled. After the main question moves to proved or refuted, any item that stalls ends the
work within an hour: two 30-minute reviews in which no open row changes status.
- With T4 and T5, H035 would have stopped at about 05:54 UTC with H035.39 open at its gate, instead of 07:54 or later.
- On a small object whose main statement settles in 30 minutes, the run ends within about 1.5 h instead of 5 h.
- This changes the clock of the user's own rule for one class of prompts, so it needs **the user's word**. It also
  needs a lint key (B3).
- The alternative already in the design is the A/B cut of `COMPANION_DESIGN_20261118.md` 2.7. Under it, the object run
  ends when every item is decided or reduced to an exact research gate, and the gates go to text-only prompts, one per
  cluster. That needs a second prompt per cluster.

**T6. No time figure in the prompt.** A time budget in a Pro prompt acts as a cheaper alternative under the push rule.
The time expectation belongs in the builder and the plan (B1).

### 7.2 In `build_object_prompts.py`

**B1. The time estimate, for scheduling only.** `est_minutes` (line 197) counts entries and cited pages. The pilot
measured 2 h 03 min for a span of 23 pages with 46 statements: about 5.3 minutes per page of the span. The proposed
formula:
- `15 + 5.5 × span_pages`, plus 60 when `open_question_entries > 0` (the tail under T5);
- for H035 this gives 15 + 126 + 60 ≈ 3 h 20 min, against about 3 h under T5.

The figure goes into README, BUILD.json and `OBJECTS_PLAN.tsv`.

**B2. Attach the object's span, not only the pages the notes cite.**
- **Choosing the pages:** the cited pages, extended over the numbered sequence they belong to in the folder
  transcription (the \uline{Lemme|Proposition|Théorème|Corollaire|Remarque} numbering). For cote 94 this is scans 2-24:
  Lemme 1 on scan 3 to Remarque 21 on scan 24.
- **Packing:** attach those scans, in zip parts under 10 MB.
- **The estimate:** `span_pages` for B1 comes from the same range.
- **Why:** here the main statement (scans 16-17) was not attached. The run had to download the archive's PDF itself.

**B3. The lint.** If T5 is taken, `claude_tools/push_rule_pro_prompts.py` (line 157, `THREE_HOUR_KEYS`) needs a
variant for object prompts that accepts "**Progress check at one hour**", with the same other keys.

**B4. Links.** Put the nearby objects' statement lines in the context zip (from `OBJECTS.tsv` or
`GLOBAL_OBJECTS.tsv`), not only their tags. A link can then carry evidence; otherwise `LINKS.tsv` will stay empty in
every run.

The changes T1-T5 are template text: the builder substitutes placeholders and needs no other change for them.

### 7.3 This return, at intake

- **H035.5:** the status becomes *true as written* (with "non nul" inserted on scan 4). Correct `READINGS.tsv` row 5 and
  `NOTES_VERDICTS.tsv` rows 5 and 17 to match.
- **H035.44:** withdraw the "vector bundle" falsity once EGA II 1.7.8 is confirmed. The f_* slip stands.
- **Relabel as *slip*:** H035.8, H035.14, H035.22, H035.24, H035.25, H035.26, H035.29 and H035.38.
- **H035.10, H035.15 and H035.21 stay *false***: they are errors in his mathematics, with proved repairs.
- **H035.30 becomes *true as written*:** his central criterion, proved by the run. No exact published match is known to
  the run.
- **H035.39 goes to the research register as his question,** with the run's gate: the residue-field finite-output
  question over an uncountable local base, and the countable case proved.
- **H035.40 becomes a *programme*.**
- **Check `Murre294`'s title.**
- If a checkpoint 05 or a final zip arrives, judge only what changed after 05:54.

### 7.4 Cost at scale

These figures extrapolate from one pilot.
- **To the frozen entry:**
  - for H035, 2 h against 24 minutes estimated: a ratio of about 5;
  - for the 200 built prompts, of the order of 400-700 Pro-hours. On a single account running 2 at a time, that is
    200-350 hours of wall-clock time.
- **The tail under the present stop rule:** an object with an item that cannot be settled runs at least 5 h.
  Open-question entries are present in 606 of the 675 planned objects, so most runs would hit this rule. With T4 and
  T5, the tail is at most about an hour.

## 8. What I did not check

- **The literature.** The context guard forbids further literature reading at this point, so I opened none of the run's
  locators:
  - Lyu 2025; Hall 2014; Murre, exp. 294; SGA 3 VIII; Jaffe; Hartshorne;
  - the Stacks tags;
  - EGA III₂ and IV₂.
- **Statements not among the ten:** H035.19-20 (generic canonical modules under regular embedding or excellence), the
  geometric statements H035.32-46 apart from H035.38 and H035.44, and the composition reductions of H035.39.
- **The run's scripts** were not run.
- **The ink of scans 15-24** I saw only through the run's own crops.

The check events of this verdict are in `PILOT_VERDICT_OBJ_H035_20261119_CHECK_EVENTS.tsv`.
