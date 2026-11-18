# Plan: the mathematical pass ("intake while pass") over the Montpellier transcriptions (17 Nov 2026)

Written by Claude Opus 5.5 at effort max (agent a7d5d89d, no sub-agents), after `METHOD_AUDIT_20261117.md` and
`METHOD_AUDIT_2_20261117.md`.

**Nothing in this plan runs until the user has read it.**

**The user, on what the pass is.** "Let that agent think through it, like you're a mathematician that cares about the
math." Claude Opus 5.5 at effort max works through the mathematics of each page. It takes in every Pro note, doubt and
test as it goes. The errors surface because they break the mathematics.

## 1. What the pass is for

Audit 2 measured the gap this pass fills:
- **Pro had flagged most of the trouble.** 69 % of the second pass's changes sit at Pro's marks, and 13 of the 29
  residual errors at places Pro had flagged.
- **Its flags were not worked.** 79 % of Pro's 631 doubt marks on five blocks were left as they were.
- **The mathematics was in Pro's own notes.** 9 of the 14 errors that working through the mathematics would have
  caught had their cue there: R24, R21, N22, N21.
- **The notes' mathematics was never checked.** The triage of 17 Nov routed the notes. Its 3,812 "nothing" verdicts
  hold, in a sample, mostly checkable mathematics of the kind the companion's groundwork needs (C1).

So the pass does five things for each page, in one reading:
1. **It gets the text right,** because the mathematics shows where the text is wrong. The ink decides.
2. **It writes the groundwork** that a career algebraic geometer needs next to his words (C1).
3. **It settles the status of his claims** on the page, with the evidence.
4. **It turns Pro's notes from leads into checked items, or discards them with a reason.**
5. **It tells the field experts and the waiting prompts what changed for them.**

## 2. What reading a page of his notes properly means

He writes research notes for himself:
- fast, with abbreviations;
- with conventions that drift from page to page (044 decides T for the bioriented groupoid, and the following pages
  keep the old use);
- with first thoughts struck and replaced;
- with "?", "sans doute", "C'est faux", "Exercice!", "à voir";
- with steps left out because they were obvious to him, and sometimes with a slip or a wrong claim.

Reading such a page properly is what a colleague who cares about the work does with a draft. It means eight things.

1. **Know where you are.** A page is a moment in an argument. The unit of reading is the mathematical unit, not the
   page: a construction, a definition with its examples, a proof attempt, a list of operations. For 148/044-058 the
   units are:
   - 044-046: the groupoids T, T^± and the table of subgroupoids;
   - 047-049: the graph functor and the genus formula;
   - 050-052: marks, torsors and the combinatorial contour;
   - 053-058: the operations of erasure, filling and cutting.

   Before reading, gather:
   - the notation in force: the cote's notation table, Pro's notation table, and the decisions he took on earlier pages;
   - what the previous unit established;
   - the cotes and the Longue Marche sections he builds on.
2. **Say what he is doing,** in two or three sentences of today's mathematics: the question, the construction, the
   claim. This account is the first output (section 4) and the frame for all the checks.
3. **Read every statement as a statement:** the hypotheses, the conclusion, the quantifiers, and the type of every
   symbol (domain, codomain, variance, index set). A symbol used outside its type is either a misreading or his slip.
   - r is defined on A, so r(ω) is a slip for r(a).
   - The boundary of a closed 1-submanifold is empty, so "du bord de Σ'_ℓ" is a slip.
4. **Decide each claim:**
   - true, with a proof sketch;
   - known, with the theorem and a source opened at a locator;
   - false, with a counterexample;
   - true under a hypothesis he did not state;
   - open, with what is missing.

   A claim he flags himself ("?", "sans doute") is decided as carefully as one he states flatly.
5. **Redo his computations.**
   - By hand where they are small.
   - By script where a computer settles them, for example: coset enumeration for a finite presentation, as 145 C4
     needs; a finite check of a combinatorial count; the arithmetic of a weight formula.
   - The script is kept beside the output, so the result can be reproduced.
6. **Read what he struck and what he inserted as part of the thinking.** The first thought shows what worried him;
   the correction shows the direction. On 148, the operation of 056 was first named "affaiblissement de marquage",
   then "surmarquage". 057 then says that partial erasure is a strengthening. One story.
7. **Follow his self-assessments across pages.** A "?" on 048 ("c'est un 0-isomorphisme ?") is his own open item.
   Does a later page settle it?
8. **Keep his words and ours apart.** His words are the transcription. Ours (the account, the checks, the
   corrections) go into our files, credited, and are never mixed with his text.

## 3. How the mathematics sends one back to the ink

**What counts as a break.**
- A symbol outside its type.
- A formula that contradicts the page before or after, or a Pro note's computation.
- A sentence that does not parse.
- A claim that is false where he is unlikely to have erred, as in a definition he then uses.
- A word outside his vocabulary for this object: on 145 the operation is "remonter" throughout, and "scindage"
  breaks that.
- A thread that breaks: on 148, "remplacée" on 047 and 050, then "unifiée" on 051.

**The protocol at a break.**
1. Record the place: scan, line, what breaks and why.
2. Make a crop at native resolution, with the margin rotated if needed.
3. Read the ink before looking at any reading. Write the letters and strokes seen: ascenders, descenders, dots,
   stroke count, struck or live.
4. Only then compare with Pro's reading, the second pass's reading, and Hua's witness (Claude Opus 5.5, his project,
   credited).
5. Decide on the ink, and give a confidence.
   - **The ink gives a reading that repairs the mathematics:** correct the text.
   - **The ink confirms the broken reading:** it is his slip. Record it in the claims status and the groundwork, with
     the corrected form, and leave the text as written.
   - **The ink does not decide:** keep every alternative. The mathematically expected reading may become an
     alternative only if the ink allows it, and it is never the first reading on mathematical grounds alone.

**The rule is the controls' lesson.** At three of the 29 residual places, the mathematics favours the wrong word:
"implique" for "indique", an "en prenant" before a display, "sommes disjointes". So the mathematics may only raise the
alarm. The logic-bearing words (implique/indique, si/sinon/sauf si, maximaux/minimaux, remplacer/unifier, negations,
quantifiers) are read on a crop every time, whether or not anything breaks.

**Omissions need a separate step.** Ten of the residual errors broke nothing: a struck comma, an insertion, an arrow,
"en fait". So every strip of every page also gets an ink-coverage step: each mark of ink is in the text, struck,
inserted, a drawing, noise, or illegible.

## 4. The outputs, and who uses them

For each block, under `second_pass/math_pass/<PKG>/<unit>/`. The folder is defined here and does not exist yet.

| File | What it holds | Who uses it |
|---|---|---|
| The page TeX, corrected | His text as the ink gives it | The edition, the readers, the translation |
| `PLACES.tsv` | One row per place worked. The place: scan, line, place id, source (a Pro TeX mark, a doubt-file row, a note's anchor, a mathematical alarm, the watch list, ink coverage). The reading: the readings by witness, the blind ink reading, the decision. The record: the crop file, the confidence, the reader (model and effort), status (settled, open, alternative). | The edition, the user's eye list of open places, later passes |
| `CHANGES.md` | The corrections, as now: old reading, new reading, evidence, confidence | The edition |
| `CONSEQUENCES.tsv` | Every register row, waiting prompt, companion line or edition matter that quotes a corrected reading: old and new reading, scan:line, confidence | The main session's same-day loop |
| `GROUNDWORK.md` (C1) | Per unit: the account (what he does, in today's terms); the questions a first reader asks, answered; his claims with their status; his slips with the corrected form; the connections to his other notes, to the Longue Marche and to the literature, sources opened with locators. In English, never mixed with his words, about twice the length of the text. | The companion's C1 layer, then its French version |
| `CLAIMS_STATUS.tsv` | Each claim of his on the unit: claims-map #n, note id or a new id; scan:line; the statement in today's terms; the status (proved with a sketch, known with source and locator, false with a counterexample, under an added hypothesis, open, convention); the checker; the CHECK_EVENTS reference | The research registers, the companion's status lines, the prompt writers |
| `NOTES_VERDICTS.tsv` | Each Pro note on the unit: anchor on the ink (confirmed or corrected); its mathematics (confirmed, corrected, refuted, not checkable, with the reason); the triage verdict (confirmed or overturned); where it went (C1, a claim, an expert, an edition matter, nothing with a reason) | The registers; it supersedes the triage verdicts for these pages |
| `FOR_EXPERTS.md` | For each field (the GT tower, anabelian, Dérivateurs, cycles, tame topology, ...): what in these pages bears on their open rows, with the evidence; questions worth a hunch (Fable, with the user's OK) or a Pro prompt | The field experts, the prompt writers |
| `CHECK_EVENTS.tsv` | One row per check: statement id, date, who (model, effort, agent), type (targeted proof check; independent re-proof; computation or formal certificate; used and rechecked in this run; carried as background without fault found; refuted, with the refined statement's id), outcome | The check ledger, the companion's status lines |
| `scripts/` | Every computation, rerunnable (`python -I -B`) | Anyone checking a claim |
| Final message | Counts, and the consequential corrections by confidence | The main session |

**Status lines follow the companion rules** (memories companion-ideology, companion-structure-follows-argument and
check-rubric). The outputs feed a companion structured by his argument, with a status line on each result. They never
split checked from unchecked into separate parts.

## 5. How Pro's notes are worked through and verified

A Pro note has six parts:
- a source (scan:lines);
- a kind;
- an anchor (a quotation from the first-pass reading);
- an argument, often with a finite test;
- the context it searched (other packages' notes);
- its links to our registers, with their status.

Each part gets its own work.

| Part or kind | What the pass does | Check event |
|---|---|---|
| **Anchor** | Read it on the ink first. A note built on a misreading is corrected or dropped before its mathematics is used. R17, U10 and T01 of 148 quoted misreadings. | none (a reading) |
| **Reading question** | It becomes a place (section 3). | none |
| **His unproved claim or conjecture** | Decide it (section 2, item 4). | targeted proof check, computation, or refuted |
| **Pro's own idea or unpursued implication** | Is it true? Is its test right? Does it answer a first reader's question (C1)? Is it research (for the experts)? | as it applies |
| **Test computation** | Redo it. R17's two disks with Jacobian signs (+1, −1); R23's Z/0Z = Z against the empty set; R38's (1,1,4) ↦ (2,2,−1). | computation |
| **Pointer to another page or cote** | Follow it and read what it points to. R24 points to 057 and 061 for the clear form of the 053 polarity. Following it would have caught the polarity error. | none, or used and rechecked |
| **Context searched (other packages' notes)** | Check that the linked note says what this one claims. Record the link in `LINKS.tsv`: same object, same notation, continuation, contradiction. | carried as background, or used and rechecked |
| **Register link** ("STRATA F.17 — Proved, return claim") | Does the corrected reading still support the link? If not, add a row to `CONSEQUENCES.tsv`. The pass does not re-prove the register row: that belongs to the run's own checks. | none |
| **Self-flag (his "?", "faux")** | Track it to where it is settled, or not. | as it applies |
| **Pro's confidence** | A prior, never a verdict. | - |
| **The triage verdict** (research item, edition matter, nothing) | Confirm it or overturn it, with the reason, in `NOTES_VERDICTS.tsv`. | - |

## 6. Where his mathematics is sketchy or wrong

**What gets recorded.**

| Case | Example | How it is recorded |
|---|---|---|
| Slip of the pen | 050 r(ω) for r(a); 054 π₀(Σ') = A_0 for A'_0 ⊂ A_0 | The corrected form, in `CLAIMS_STATUS.tsv` and the groundwork. The text stays as written. |
| Slip of thought, corrected by him later | 018 "C'est faux" then 020's added relations (145 N18) | The two stages, both kept. Our account names the correction. |
| Gap | 145/030 "sont conséquences" (relations claimed to follow) | Filled where it can be: 145 C4 has the τ = 1 quotient, and a coset enumeration settles the general case. Otherwise the missing step is stated exactly. |
| False as stated | 15/132 the cancelled norm claim over Q(i) (FR17); 149/101 "Sans doute pas" against a ramified-twist realization (RN101-01, unchecked) | A counterexample, checked; a check event; status "false as stated", with the corrected statement where one exists. |
| True under an extra hypothesis | A connectedness proviso, such as R17's | The hypothesis named, and the proof. |
| Convention drift | 044's T decision not carried into 045-065; the tilde reserved for lifts on 021 (N21) | Put in the cote's notation table, and told to the reader in the groundwork. |
| His open question | 048 "0-isomorphisme ?" | Status open; what later pages say; a pointer to the field expert if it bears on a run. |

**Three rules.** We never repair his text. We never lower his statement to match a proof we can give. We never present
our completion as his.

## 7. The "nothing" notes

**The sample.** In the sample of audit 2 (section 1), 8 of the 9 readable "nothing" notes carry checkable mathematics:
- small proofs;
- a counterexample to a cancelled claim of his;
- Deligne's Tate-twist convention, cited;
- an unfinished computation of his;
- a structural point on the tower at infinity;
- an elementary argument behind the semisimplicity request on cote 16.

**How the pass treats them.** It reads every note on its pages in full, whatever the triage said. Each "nothing" note
is verified like any other (section 5) and placed:
- C1 groundwork;
- the claims status;
- an expert's queue;
- an edition matter;
- or truly nothing, with the reason.

**There is no separate sweep of the 3,812.** They are taken page by page as the pass reaches their pages, so each is
read with its page, its ink and its mathematics at hand. The rest wait for their pages' turn.

## 8. The procedure of a block

**0. Preparation, by script, before the agent starts.**
- The unit boundaries, from Pro's notes and his own headings.
- The place list, built from:
  - Pro's TeX marks;
  - both tables of Pro's doubt file, parsed per package, with their line numbers;
  - the second pass's unresolved list, and its low- and medium-confidence changes.
- The Pro notes on the pages, in full, with their triage verdicts, the claims-map rows and the edition matters.
- The register rows and waiting prompts that cite these scans.
- Hua's modernised reading of the unit, as context with credit to his project.
- The cote's notation table so far.
- Native-resolution tiles of every page.

**1. The account.** Read the unit as mathematics: the current text with the scans beside it, plus Pro's notes. Write
what it does.

**2. The working-through:**
- every Pro mark and doubt-file row: decide it on the ink, blind first;
- every note: its anchor on the ink, then its mathematics, then its verdict;
- every statement and formula: type, truth, consistency.

Every alarm becomes a place (section 3).

**3. Ink coverage and the watch list,** strip by strip.

**4. The outputs** of section 4. Consequential corrections go out by confidence:
- a high one is reported as consequential;
- a medium one is reported as "reading changed (medium); recheck before use".

**Blocks.** One or two units, about 8-10 pages of dense hand. The notation table and the open self-flags carry over to
the next block.

**Decisions at low confidence where the reader's own earlier reading is at stake** go to a fresh Claude reader, blind,
or stay open. The verdict on CTRL-148 showed the same agent rereading the same ink differently once a second witness
disagreed (audit 1, section 2.3).

## 9. The pilots

### 9.1 Pages, and what is known about them

| Pages | Hand and mathematics | What is known (the key) |
|---|---|---|
| CTRL-148: cote 148, scans 44-58 | Dense hand. Combinatorial topology: the groupoids T, the graph functor, the operations on marked surfaces. | 16 residual errors of the second pass, plus 6 majority places; 5 slips of his (049 A_0, 050 r(ω), 054 π₀(Σ'), 055 "du bord", 056 a missing verb); Pro's 65 errors |
| CTRL-145: cote 145, scans 20-34 | Medium-dense hand. Group presentations and lifts: Z/2 * Z/3, the three lifts of τ̇, the commutant. | 13 residual errors; about 6 slips or inconsistencies (034 (9'), 033 SÊ̂, 026 against 037, the indices of 027/029, 028 Γ₂, 020 l∞); Pro's 34 errors |
| A unit of cote 149, scans 101-106 (no reading key) | The anabelian notes of 1983, the companion's heaviest chapter. RN101-01 claims that his "Sans doute pas" is refuted in the stated generality. | No reading truth. It tests the mathematics and the groundwork where a field expert can judge them. |

### 9.2 Keeping the pass blind to the answers

Each pilot folder is built by a script into a clean folder, with a manifest. The brief names only that folder and says
not to read outside it.

**It holds:**
- Pro's first pass, its doubt file, its notes;
- the triage files' rows for these notes;
- the claims-map rows;
- the edition matters;
- Hua's witness and modernised reading;
- the scans;
- for the third-pass variants, the second pass as it stood before the controls (`codex_web_20261113/third_pass_pilot/second_pass_before_controls/<ID>/`), with its changes and notes-checked files stripped of the addenda.

**It leaves out:**
- the control returns (CTRL-148, CTRL-148_SOL62, CTRL-145);
- the verdicts;
- the keys (`third_pass_pilot/keys/`);
- both audits;
- the RUNBOOK;
- the corrected second-pass files.

**The 145 notes-checked file** carries bracketed evening additions inside its notes, such as C9. The build script
removes them, and the result is compared line by line with the file's state before 19:00 UTC, if a backup exists.
Otherwise every removal is listed in the manifest.

**The agents who know the answers do not run any pilot:** a8ebc443, ac292d80, and this auditor, a7d5d89d.

### 9.3 The variants

**Variants for the reading on CTRL-148 and CTRL-145.**

| Variant | What runs | What it measures |
|---|---|---|
| **M1, third pass** | Claude Opus 5.5 at effort max, the full procedure of section 8, on top of the second pass as it stood before the controls | What the user asked for: how many of the 29 known residual errors the mathematics and Pro's marks and notes catch; the new errors; the slips; the notes verified; the groundwork; the cost |
| **M2, one pass in place of the second and third** | The same agent and procedure, on Pro's first pass alone, with no Claude second pass | Whether one mathematical pass does both jobs: its catches against all of Pro's errors (99) and the 29; its cost against the second pass plus M1 |
| **M3, order** | M1 with the steps reversed: ink first (every Pro mark and doubt row on the scans), then the mathematics | Whether reading the mathematics first, as section 8 orders it, catches more than reading the ink first, and at what cost |
| **M4, model** | M1 by Claude Fable 5.2 at effort max (needs the user's OK) | What the stronger mathematical model adds, in the reading and in the groundwork |
| **M5, Pro then Claude** | First a Pro prompt (GPT-6 Astra, ChatGPT Pro mode): Pro works through its own marks, doubt file and notes against the scans and the mathematics, and writes the same files. Then Claude Opus 5.5 at effort max checks Pro's decisions and verdicts and writes what remains. | How much of the Claude meter Pro can carry, and at what loss of catches. This is the split "as compute allows". |

**The groundwork test on 149/101-106.** A Claude Opus 5.5 at effort max run of M1. If the user agrees, Claude Fable
5.2 at effort max runs the same unit. It is graded by a field expert of the anabelian cluster.

**The order of runs.**
- **Stage 1:** M1 and M2 on both controls. Four runs.
- **Stage 2:** after the user reads stage 1, M3 on one control, M5 on both, and M4 if the user agrees.
- **Stage 3:** the unit of 149.

### 9.4 How the runs are graded

**The grader.** A fresh Claude Opus 5.5 at effort max who made none of the readings. A Claude Fable 5.2 at effort max
grader only with the user's OK. For the 149 unit, the anabelian field expert.

**Reading, on the controls.** The grader uses `codex_web_20261113/tools/reconcile_readings.py` and the keys:
- known errors caught: the 29, the 6 majority places, and, for M2, Pro's 99;
- new errors claimed, each checked on the scan blind: the grader reads the ink before it sees which variant said what;
- errors introduced, and the precision of the changes;
- Pro marks given a recorded decision, out of the 295 marks on the control pages: 164 on 148/044-058, 131 on
  145/020-034;
- open places, and how many were settled correctly where the truth is known.

**Mathematics.**
- His slips found, against the list in 9.1. A new slip counts once the grader confirms it.
- Note verdicts: the grader rechecks 20 drawn at random. Right or wrong.
- Claims classified: the grader opens 10 of the sources and checks the locators.
- Computations: rerun from the scripts.
- False mathematical claims: each counts as much as an unmarked reading error.
- "Nothing" verdicts overturned, with a reason the grader accepts.

**Groundwork (C1).** A rubric per unit:
- correct;
- answers the questions a first reader has;
- sources opened at locators;
- his words never mixed with ours;
- written in the field's language;
- about twice the length of the text.

The user is given two units to read.

**Cost.**
- Claude tokens and the weekly meter, read before and after each run.
- Wall time.
- Pro slots, for M5.
- Fable meter, for M4.

**The decision, stated before the runs.**
- **M2 replaces the second pass on new pages** if it catches at least as many of Pro's errors as the second pass did
  (71 of 99). It must also catch most of the 29 residual errors and keep its changes right at least 95 % of the time,
  at less cost than a second pass plus M1. Otherwise M1 runs as a third pass on the priority waves.
- **M5 takes the share of the work it can carry** if its catches come within about a tenth of M1's at clearly less
  Claude meter.
- **The order (M3) and the model (M4)** are set by catches per meter point, false claims counted against.
- **The groundwork must pass its rubric** before any of it goes into a companion chapter.

### 9.5 What the pilots cost [estimate]

- **Per page, for M1 and M2:** about 60-100k Claude tokens.
  - Pro's marks: about 11 a page on 148, each a crop and a decision.
  - The notes and doubt rows: about 1.3k tokens a page to read, far more to work through.
  - The mathematics, its computations, and the sources opened.

  The second pass cost about 34k a page.
- **Per control and variant:** about 1-1.5M tokens. Grading: about 0.4M per run.
- **By stage:**
  - Stage 1 (4 runs): about 5-6M plus 1.6M of grading, or about 7 points of the weekly all-models meter (about
    1 point per 1M tokens; RUNBOOK 3867).
  - Stage 2: about 5-7M more, plus two Pro slots for M5, plus the Fable meter if M4 runs.
  - Stage 3: about 1M, plus the expert's reading.
- **At scale, after the pilot sets the method [inference]:** about 60-100k tokens a page, or 6-10 points per 100
  pages. The priority waves of audit 1, section 7 (cotes 149, 147/003-137, 142, then 144, 146, 147/138-190) are about
  900 pages, or about 55-90 points, roughly one full week of the meter. The pilot measures the true rate before that
  is planned.

## 10. Risks, and how the plan meets them

| Risk | What the plan does |
|---|---|
| **Pro's notes mislead**, because some are built on misreadings | Each note's anchor is read on the ink before its mathematics is used (section 5). |
| **The mathematics pulls toward a wrong reading** | The ink decides; the watch list; blind reading first (section 3). |
| **References are made up or misplaced** | Every source is opened, with a locator, or marked "not located". The grader opens ten (section 9.4). |
| **The pass sinks into research** | The pass decides what the page needs. A question that needs research becomes an item for the field expert, with the evidence, not a long derivation. |
| **The reader is anchored on its own readings** | Low-confidence decisions go to a fresh reader, or stay open (section 8). |
| **The context fills up** | Blocks of one or two units. The notation table and the open flags are carried in files. |
| **The answers leak into a pilot** | Clean folders, a manifest, and agents with no knowledge of the controls (9.2). |

**Nothing above has been run.** The next step is the user's reading of this plan.
