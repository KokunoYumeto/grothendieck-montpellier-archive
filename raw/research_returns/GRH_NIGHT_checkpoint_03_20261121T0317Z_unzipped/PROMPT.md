**The attached files.** Besides this file there is one ZIP, `GRH_NIGHT_everything_that_follows_from_the_two_proofs.zip`. Unpack it once: it holds every file named below. Every file is at the top level under its own name.

# GRH_NIGHT: everything that follows from the two proofs of 20 November 2026

This is tonight's whole task, and it is open-ended by design. Two proofs of generalized Riemann hypotheses appeared on
20 November 2026, one formalized and one a long draft. Grind out everything they imply: every consequence that follows
from them, that you know or can derive, each proved or located, and organized into one catalogue we can read along with
you as the checkpoints come in.

## The results cited

**Alpöge.** On 20 November 2026 Levent Alpöge (a number theorist: Bhargava's student; Harvard Society of Fellows)
posted a four-page note and a complete Lean formalization of a proof of the Riemann hypothesis and of GRH for Dirichlet
L-functions, found with Claude. `ALPOGE_Main.lean` proves Mathlib's `RiemannHypothesis` and the Dirichlet statements
(defined in `ALPOGE_Statements.lean`); a text scan of all 175,187 source files (`ALPOGE_LEAN_SCAN.tsv`) finds no sorry,
axiom or native_decide. It has not been refereed, and that is not our concern here: its theorems are cited as theorems,
L. Alpöge, *Remark*, https://alpo.ge/remark.pdf (attached as `ALPOGE_remark.pdf`), with its Lean archive. The steps of
the note used below (numbered as in its pages 1-4): step 2, p-adic divisibility of derivatives of CM theta values at
inert primes; steps 3 and 5, the count qN = M^k + R on the path quadric and the "sign-only proof of Weil and Deligne"
(a definite sign from middle cohomology, square-root cancellation by iterated Parseval, opposite signs forbidding
cancellation of inverse roots); steps 4 and 7, positivity by determinants and Gan-Gross-Prasad periods (values 0 or 1
for interlacing weights); step 8, iterated theta lifts between totally definite unitary groups, each winning one order
of multiplicity; step 13, the Bost slope inequality; step 17, the groups H^1(o_E[1/l], Q_l/Z_l(-e)) and a weakening of
Vandiver's conjecture.

**Masullo.** A. M. Masullo, *The Music of the Primes* (940 pages, a draft posted 20 November 2026 and announced by
R. Vakil), proposes a proof of GRH for the Hecke L-functions of every number field (its §1.2), by adelic θ-functions,
idelic zeta functions and a trace formula on "orbital Schauder bases". It is neither refereed nor formalized: cite its
statements as the draft's claims, by chapter and statement number (`MASULLO_STATEMENTS_INDEX.md` lists all 336 numbered
statements with their PDF pages), and mark every finding that depends on it as conditional on it.

**Masullo, readable.** `MASULLO_MATH_VERSION_20261121.md` gives each page of the draft: its prose from the PDF's text
layer, and each formula in LaTeX under its line. The formulas were transcribed by a model over an API (Claude Opus 5.5
at effort high, Message Batches API, 21 Nov 2026) from page images; the source is not public. So when a formula looks
wrong, it may be a mistranscription. Check the page in `MASULLO_the-music-of-the-primes.pdf` (same page number) before you
conclude that the draft is wrong, and say which you checked.

## The task

Derive everything that follows from the two results and from their methods. For each consequence, give:
- its statement;
- its exact input: GRH for Dirichlet L-functions (Alpöge, a theorem); GRH for Hecke L-functions (Masullo, conditional);
  or more, with what more;
- a proof, or the exact locator of a classical proof;
- where it lives in our work.

The territory, all of it:
1. **Number theory.** The theorems that were conditional on these GRH statements and are now theorems or conditional on
   Masullo only:
   - primes in progressions, least non-residues and primitive roots, class numbers, effective Chebotarev;
   - Artin's primitive-root conjecture (Hooley);
   - Montgomery's pair correlation and the random-matrix statistics of low-lying zeros;
   - moments, the Lindelöf consequences, zero-density.
   Each with its constants where the classical proof gives them.
2. **Algebraic geometry and motives.** The zeta functions of schemes over Z, Artin-Tate and CM motives, purity-type
   statements, special values and K-groups where the zeros bear on them, and what the methods (theta lifts, positivity,
   the adelic trace formula) prove on their own.
3. **Our programme on Grothendieck's work.** What changes in his texts (cote 1's trace formula, cote 16, cote 34, cote
   44, cote 149, the anabelian and Grothendieck-Teichmüller line) and in the open rows of our runs.
4. **Complexity.** Derandomization, Koiran's Nullstellensatz, factoring, primality, and geometric complexity theory.
5. **The two proofs against each other.** Each used on the other: Alpöge's mechanisms to check Masullo's steps; Masullo's
   adelic framework to carry Alpöge's method to Hecke characters. Then the two together on what neither reaches alone
   (GL_2, Artin holomorphy).

The links to each of these are real. No consequence needs to be a mere corollary to be worth deriving, so do not ask
whether a link holds: show how it works, prove what follows, and where a route meets an obstacle, locate it and take the
next route.

## What we already found (attached): use it, do not redo it

These are our results so far. They are background for you to build on, correct where wrong, and cite by file and id:
- our intakes of 20-21 Nov (`OURS_INTAKE_*.md`);
- the bridges run (`OURS_BRIDGES_*`);
- the Hodge sketch (`OURS_HODGE_BRIDGE_SKETCH_20261121.md`);
- the Δ sextic answer (`OURS_DELTA_SEXTIC_20261121.md`);
- our Fable agent's suggestions (`OURS_FABLE_PROGRAM_SUGGESTIONS_*.md`);
- the IMPLICATIONS and LEDGER files of tonight's returns (`RETURN_<TAG>_*.md`);
- `ORDER_tonight.md`, the questions put to other runs tonight. Other runs are working on those questions; you do not
  have to, but use and extend what any of them gives you.

## The attached files

- `ALPOGE_remark.pdf`, `ALPOGE_Main.lean`, `ALPOGE_Statements.lean`, `ALPOGE_LEAN_SCAN.tsv`, `ALPOGE_LEAN_MAP_20261120.md`.
- `MASULLO_the-music-of-the-primes.pdf`, `MASULLO_MATH_VERSION_20261121.md` (read the caveat above),
  `MASULLO_STATEMENTS_INDEX.md`.
- The files named in the previous section.

## The language of the results

State every consequence also in the language of algebraic geometry and of Grothendieck's frameworks. Tate's thesis and
the adelic language sit beside his trace formula of cote 1, Weil's explicit formula, purity (Weil I and II), motives and
their L-functions, λ-rings, Shimura varieties and theta correspondences. Say where it lives in his texts: the archive by
cote and scan, the SGA, EGA or FGA by exact locator, and our runs by run and statement id. Then every result can be used
in our programme, whatever else comes of it.

## How to work

The rule that governs everything below: push. Work on the main question first: the full catalogue of consequences of the two results and their methods, each proved or located with its exact input, kept current in CONSEQUENCES.tsv through every checkpoint. Give it most of the time.
When one approach stalls, take the next one. Deliver nothing while an item is undecided and an untried approach
remains. A gap in a proof is an undecided step: attack it, never paper over it.

**Progress check at three hours**. After about three hours of work, and every hour after that, review the work against
a dated ledger (`LEDGER.md`): every open row with its status, and for each main question its current gate (the strongest
proved reduction). Movement means only an open row changing status, or a main question proved to reduce to a strictly
smaller gate. Restating the same gate, side results that leave every gate as it was, and packaging are not movement.
After two consecutive reviews without movement, stop that work, write the final package with every item's state, and
deliver it; this check takes precedence over the rule about untried approaches.

For every statement, record its check events in `CHECK_EVENTS.tsv`: statement id, date, who (model, effort, run), type
(targeted proof check / independent re-proof / computation or formal certificate / used and rechecked in this run /
carried as background without fault found / refuted, with the refined statement's id), outcome. Give each event the type
of what actually happened, neither more nor less. Cited statements you use get their events too.

Every proof is checked before the package is final, by a reading of the whole proof, and the check is recorded with
who, how, model, effort and date. A proof that fails its check is reported with its gap.

**Checkpoints.** Save a checkpoint ZIP to the user's Library, or wherever files survive the loss of the execution
environment, once every 45 minutes of work, each under a new name, `GRH_NIGHT_checkpoint_<NN>.zip` with `NN` counting up.
Never overwrite, rename or delete an earlier checkpoint, and put no earlier checkpoint ZIP inside a checkpoint. Save
checkpoints once every 45 minutes and at no other time. A checkpoint is one ZIP holding every deliverable written so far
and everything that documents the work, so that a new session can continue from it and the attached files. It is never
a JSON file, a recovery file, a summary, or an export of the newest part only. Each checkpoint zip holds the current
deliverables and documentation; earlier checkpoints are not copied into it.

**If the execution environment fails**, that does not end the task. Retry at intervals for as long as this session
lasts. When it is back, restore your work from the newest checkpoint, redo what you had done after that checkpoint, and
continue to the end. Do not write files out in this chat instead: the work reaches us only through checkpoint ZIPs and
the final ZIP.

## What to deliver

One final ZIP, `GRH_NIGHT_final.zip`, holding:
1. **The paper**, `GRH_NIGHT.tex`, in LaTeX:
   - every finding with its proof (a finding is a new result of this work), each under its id;
   - checked and unchecked findings in separate parts;
   - every cited result with an exact locator (Alpöge's by step and Lean file; Masullo's by statement number; the
     literature by work and statement number; Grothendieck's archive by cote and scan; our runs by run and statement id).
2. **`QUESTIONS.tsv`**, one row for each question treated: id, the source and locator, the question, its state (proved,
   with the finding ids; refuted, with the counterexample; or, if the session ends, its current gate).
3. **`LEDGER.md`** and **`CHECK_EVENTS.tsv`**.
4. **`IMPLICATIONS.md`**: what the consequences change: for our programme on Grothendieck's work (cote and scan),
   for our runs' open rows (run and statement id), for the open conjectures.
5. **`CONSEQUENCES.tsv`**, the catalogue, one row per consequence, with these columns:
   - id; statement;
   - input: Alpöge / Masullo (conditional) / both / neither, plus the extra input it needs;
   - status: proved here / classical with an exact locator / conditional on what / open, with its gate;
   - where the proof is;
   - where it lives in our work.
   Keep it current in every checkpoint, so it can be read along.

A known result is cited with an exact locator and is not proved again, except for a short proof of a form its source
does not state. Every new result is proved in full. An item is finished only when it is proved or refuted. A return may
be marked INCOMPLETE only when the session itself ends. It then gives the state reached, every approach tried with where
it failed, and the next step.
