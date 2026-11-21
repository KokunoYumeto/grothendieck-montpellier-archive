# Bridges: Alpöge's RH and GRH into algebraic geometry, Deligne's work and Grothendieck's

You are Claude Opus 5.5 at effort max. Before any mathematics, read `C:\Users\user\Documents\AGENTS_MATHEMATICS.md` in
full: it says how mathematics is written, proved and checked here, and how to use the literature corpus.

## The input: a research return, taken in and cited to its author

On 20 Nov 2026 Levent Alpöge posted a note and a Lean formalization of a proof of the Riemann Hypothesis and of the
Generalized Riemann Hypothesis for Dirichlet L-functions, found with Claude. It is taken in here as a research return,
like any of our runs, and its results are cited to him: L. Alpöge, *Remark* (https://alpo.ge/remark.pdf, 20 Nov 2026),
and the Lean archive (https://alpo.ge/lean.tar.gz.part01 to part14), by theorem name and file.

- The files: `C:\Users\user\Documents\Papors\Chatnotes\Zeta-Function-Foundation\literature\alpoge_rh_20261120\`
  (`README.md` first; `remark.pdf`; the archive extracted in `lean_tree/`). The files of the archive are read as text;
  nothing from it is built or run.
- The intake map: `C:\Users\user\Documents\reports_20261120\alpoge_rh\ALPOGE_LEAN_MAP_20261120.md` and its `INDEX/`,
  made by Claude Opus 5.5 at effort medium: the statements proved (`Main.lean`, `Statements.lean`), the proof chain,
  the note's twenty steps matched to the Lean, and the algebraic-geometry and function-field parts.

## The task

Grothendieck and Deligne asked questions throughout their work. Find every question of theirs that the statements
Alpöge proves, or the method of his proof, settle, and resolve each one: prove it or refute it.

- **Through the bridges of the field:** the arithmetic consequences of RH and GRH; Deligne's purity and the theory of
  weights (*La conjecture de Weil* I and II); motives and their L-functions; pure and mixed Tate motives Q(n) and their
  Artin-Tate twists; the standard conjectures; and wherever else the mathematics leads.
- **Through his method:** the note describes a Stepanov-type argument whose multiplicity is won by iterated theta
  lifts, and a "qN = M^k + R sign-only proof of Weil and Deligne". Work out what the method gives in algebraic geometry,
  from the Lean where the Lean has it.
- **Through our own mathematics.** We have a very large body of new mathematics built on Grothendieck's algebraic
  geometry; bridge the results into it. `C:\Users\user\Documents\knowledge\INDEX.md` is the map of all of it. The main
  parts:
  - the transcription of his Montpellier archive: `grothendieck_archive_transcription_20261110/text_of_record/pages/`
    with `MANIFEST.tsv`; the archive topic by topic and its six books in `PROJECT_RECORD.md` sections 2b and 2c;
    `grothendieck_archive_transcription_20261110/notes_headlines/PROGRAMME_MAP.md`;
  - our editions of EGA, SGA, FGA, Deligne's papers, *La Longue Marche* and *Les Dérivateurs*:
    `knowledge/05_editions/`;
  - our research lines and their results: `knowledge/04_research/` (the research lines; the register of our results
    and how far each claim is checked), `PROJECT_RECORD.md` section 3, `field_experts/INTAKE_LEDGER.md`,
    `longue_marche_pro_pilot_20261104/answers/`, `derivateurs_companion_20261109/`, and the sweeps;
  - the literature corpus: `Papors/Chatnotes/Zeta-Function-Foundation` (start at `RECOVERY_ENTRYPOINT.md`; query
    through `scripts/query_corpus.py`);
  - the intakes of our research runs, being made now: `field_experts/intake_20261120/`. Its `BRIDGE_FLAGS.tsv`
    lists every row of those runs that uses, assumes or would follow from RH, GRH, purity or weights, the Weil
    conjectures, L-functions or Tate motives; the readers' intake files are added there as they finish.

**The people whose life's work bears on RH, credited and bridged** (the user, 20 Nov 2026: "Let's start ... paying some
respect to people who actually spend their entire life working on the kinds of mathematics that might bear on RH, and
bridge the proof of ... GRH to their ... work"):
- Find the theorems proved under RH, or under GRH for Dirichlet L-functions, that the cited statements now make
  unconditional. Give each with its author, work and statement number, and say exactly which hypothesis it used. For
  example:
  - Montgomery's pair-correlation theorem;
  - Selberg and Cramér on primes in short intervals and on gaps;
  - Littlewood's bounds for L(1, χ);
  - Bach's explicit bounds;
  - Lagarias-Odlyzko's effective Chebotarev for abelian fields;
  - the effective forms of Siegel's theorem;
  - Miller's primality test;
  - the results of Iwaniec, Sarnak and the others conditional on these statements.
  Where a result needs more than what is cited (GRH for non-abelian Artin L-functions, for L-functions of elliptic
  curves or of automorphic forms), say exactly what more.
- The programmes built to reach RH: Weil's explicit formula and positivity, Hilbert-Pólya, Connes and Connes-Consani,
  Deninger, the F_1 programme, Katz-Sarnak, de Branges, Li and Beurling-Nyman. Say what each criterion or programme
  now states as a theorem, and what part of each is still its own open question.
- Algebraic geometry, built as the road to the Riemann hypothesis: Weil, Grothendieck, Deligne, Katz, Drinfeld,
  L. Lafforgue, and the cohomologies and trace formulas. Bridge the cited statements to their work, and to the
  analogies between Spec Z and a 3-manifold (Artin-Verdier duality, arithmetic topology).

**P versus NP through geometric complexity theory** (the user, 20 Nov 2026: "The real research direction ... is P versus
NP via geometric complexity theory"):
- Bridge the cited statements and Deligne's purity to Mulmuley's programme:
  - the positivity hypotheses of the flip (Kronecker and plethysm coefficients) and the nonstandard quantum groups;
  - Kazhdan-Lusztig positivity through purity;
  - orbit closures and occurrence obstructions;
  - Koiran's Nullstellensatz in AM under GRH, with exactly which GRH it uses;
  - the derandomization of polynomial identity testing and Noether normalization.
- The user says the Exponential Time Hypothesis has been disproved in a run of OpenAI's. Find the result and its
  source, and bridge it too.
- Alpöge's note credits a "(2, 3, 6)-triangle group trick" and works on a sixfold cover of GL_5. Bridge them to the
  hexagons of our own work: the Grothendieck-Teichmüller hexagon relations, and the hexagons and pants of
  Grothendieck's sheets on Teichmüller spaces (cotes 67-68, the letter to Bers; the SA22 intake has them).

For each question:
- state it as Grothendieck or Deligne states it, with its source and an exact locator (for the archive: cote and scan);
- say what settles it, and prove it.

A known result is cited with an exact locator and is not proved again, except for a short proof of a form its source
does not state. Every new result is proved in full. An item is finished only when it is proved or refuted.

## How to work

The rule that governs everything below: push. Work on the main question first: the questions of Grothendieck and
Deligne that these statements settle. Give it most of the time. When one approach stalls, take the next one. Deliver
nothing while an item is undecided and an untried approach remains. A gap in a proof is an undecided step: attack it,
never paper over it.

**Progress check at three hours**. After about three hours of work, and every hour after that, review the work against a dated ledger (`LEDGER.md`): every
open row with its status, and for each main question its current gate (the strongest proved reduction). Movement
means only an open row changing status, or a main question proved to reduce to a strictly smaller gate. Restating the
same gate, side results that leave every gate as it was, and packaging are not movement. After two consecutive reviews
without movement, stop that work, write the final package with every item's state, and deliver it; this check takes
precedence over the rule about untried approaches.

For every statement, record its check events in `CHECK_EVENTS.tsv`: statement id, date, who (model, effort, run), type
(targeted proof check / independent re-proof / computation or formal certificate / used and rechecked in this run /
carried as background without fault found / refuted, with the refined statement's id), outcome. Give each event the
type of what actually happened, neither more nor less. The statements you cite to Alpöge get their events too.

Every proof is checked before the package is final, by a reading of the whole proof, and the check is recorded with who,
how, model, effort and date. A proof that fails its check is reported with its gap.

**Checkpoints.** Save a checkpoint ZIP of the package folder (`bridges/`, with your scripts and notes) into
`bridges/checkpoints/` once every 45 minutes of work, each under a new name, `BRIDGES_checkpoint_<NN>.zip` with `NN`
counting up. Never overwrite, rename or delete an earlier checkpoint. Save checkpoints once every 45 minutes and at no
other time. A checkpoint is one ZIP of every deliverable written so far and everything that documents the work, so
that a new session can continue from it. It is never a JSON file, a summary, or an export of the newest part only.
Each checkpoint zip holds the current deliverables and documentation; earlier checkpoints are not copied into it. If
your session is interrupted and resumed, restore your work from your newest checkpoint, redo what you had done after
that checkpoint, and continue to the end.

Use scripts for counting and searching over large folders. Never run the Grep or Glob tools over the whole of
`C:\Users\user\Documents` or over the extracted Lean tree; name a narrow folder, or search through an index. Write
the package early and keep it current: a session that ends keeps only what is written down.

## What to deliver

In `C:\Users\user\Documents\reports_20261120\alpoge_rh\bridges\`:

1. **The paper**, `BRIDGES_20261120.tex`, in LaTeX:
   - every finding with its proof (a finding is a new result of this work), each under its id;
   - checked and unchecked findings in separate parts;
   - each question with its source and locator;
   - every cited result with an exact locator (Alpöge's by theorem name and file; the literature by work and
     statement number; Grothendieck's archive by cote and scan).
2. **`QUESTIONS.tsv`**, one row for every question found: id, who asked it, the source and locator, the question as
   stated, its state (proved, with the finding ids; refuted, with the counterexample; or, if the session ends, its
   current gate), and the bridges used.
3. **`LEDGER.md`** (the dated ledger) and **`CHECK_EVENTS.tsv`**.
4. **`IMPLICATIONS.md`**: what the findings change, for each of our research lines and for the open places of the
   archive (cote and scan).

A return may be marked INCOMPLETE only when the session itself ends. It then gives the state reached, every approach
tried with where it failed, and the next step.

## Final reply

At most 400 words:
- the questions resolved, each with its finding id and one line;
- the bridges that carried them;
- what is left at which gate;
- the paths of the files.

Name every model with its effort.
