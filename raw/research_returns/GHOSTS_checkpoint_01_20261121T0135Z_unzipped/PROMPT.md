**The attached files.** Besides this file there is one ZIP, `HODGE_GHOST_CLASSES_at_supersingular_and_ordinary_primes.zip`. Unpack it once: it holds every file named below. Each ZIP named below is already unpacked inside, as a folder of the same name without `.zip` (for example `LIT_Markman_Hodge_abelian_fourfolds_2502.03415.zip` is the folder `LIT_Markman_Hodge_abelian_fourfolds_2502.03415/`), so there is nothing more to unpack; every other file is at the top level under its own name.

# GHOSTS: Hodge classes as ghosts: algebraic at every good prime, and the least complexity of their representatives

This prompt is one of five run in parallel on 21 November 2026 on the Hodge conjecture after the two GRH proofs of 20 November and OpenAI's proof of Hodge for CM abelian varieties. Statement labels (1.7, 2.1-2.5, T3-T9, 3.3-3.5, H8, H9) are those of the attached `HODGE_BRIDGE_SKETCH_20261121.md`, by our Claude Fable 5.2 (effort max) expert. The sketch is unchecked: use it as a map, never as a result. The others treat: the theta machine in three signatures (37), bounded division on Hecke orbits (38), ghost classes at primes (39), Grothendieck's 1964 Jacobians programme of cote 44 (40), degrees of cycles as L-values (41). Keep to this prompt's questions.

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

## The Hodge results cited

- **OpenAI family 032:** the rational Hodge conjecture for every complex CM abelian variety, in every dimension and
  codimension, with a Lean statement. Attached as `OPENAI_032_*.pdf`, with its companion papers.
- **van Hoften-Sempliner:** a human proof following that work, *The Hodge Conjecture for CM abelian varieties* (Hexagon
  2610.00259v2). Attached.
- **Milne:** *On the Hodge, Tate, and standard conjectures for abelian varieties* (Hexagon 2611.00244v1). It derives the
  Tate conjecture for abelian varieties over finite fields and the Hodge standard conjecture for all abelian varieties.
  Attached.
- **Markman:** the Hodge conjecture for abelian fourfolds of Weil type (arXiv 2502.03415). LaTeX attached.

## The question

A ghost is a class that passes every local test (here: algebraic modulo every good prime, by 032's Remark 8.5 and its
CM transport) and whose global status is the question. Our expert proposes to measure, prime by prime, the least
complexity of the representative t_v, at supersingular and at ordinary primes. That measure is how the local algebraicity
of Remark 8.5 becomes the bounded-division gate of Route 2.

These links are real, and none of them is a mere corollary, or it would already be known. So the task is not to ask
whether they hold. It is to show exactly how they work, and then to use the new results to attack the open problem. Where
a route meets an obstacle, locate it exactly and attack it with the next tool the new results give. An obstacle is never
an end point.

## The task

1. Prove the sketch's 2.5.
2. Check 032's Remark 8.5 with its CM transport.
3. Carry out T9.
4. For the Weil class of the sketch's T5, compute the least complexity of t_v at supersingular and at ordinary primes,
   as a function of v.
5. Use the arithmetic the new results give (the effective distribution of supersingular and ordinary primes in the
   relevant families, under the two GRH results) to bound that complexity uniformly. Then carry the bound to Route 2's
   gate.

## The attached files

- `HODGE_BRIDGE_SKETCH_20261121.md` (2.5, T5, T9).
- `OPENAI_032_*.pdf`, `HEXAGON_*.pdf`, `LIT_Markman_*/`.
- `ALPOGE_remark.pdf`, Lean files, `MASULLO_STATEMENTS_INDEX.md`.

## The language of the results

State every finding in the language of algebraic geometry and of Grothendieck's frameworks: motives and correspondences,
algebraic cycles modulo homological and numerical equivalence, the standard conjectures, Hodge and ℓ-adic realizations,
Shimura varieties and their integral models, Hecke correspondences. For each finding, say where it lives in
Grothendieck's texts: the archive by cote and scan, the SGA, EGA or FGA by exact locator.

## How to work

The rule that governs everything below: push. Work on the main question first: the least complexity of the representatives t_v of the Weil class of T5 at supersingular and ordinary primes as a function of v, bounded uniformly, and carried to the bounded-division gate. Give it most of the time.
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
environment, once every 45 minutes of work, each under a new name, `GHOSTS_checkpoint_<NN>.zip` with `NN` counting up.
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

One final ZIP, `GHOSTS_final.zip`, holding:
1. **The paper**, `GHOSTS.tex`, in LaTeX:
   - every finding with its proof (a finding is a new result of this work), each under its id;
   - checked and unchecked findings in separate parts;
   - every cited result with an exact locator (Alpöge's by step and Lean file; Masullo's by statement number; the
     literature by work and statement number; Grothendieck's archive by cote and scan; our runs by run and statement id).
2. **`QUESTIONS.tsv`**, one row for each question treated: id, the source and locator, the question, its state (proved,
   with the finding ids; refuted, with the counterexample; or, if the session ends, its current gate).
3. **`LEDGER.md`** and **`CHECK_EVENTS.tsv`**.
4. **`IMPLICATIONS.md`**: what the findings change: for the Hodge, Tate and standard conjectures; for Grothendieck's
   texts by cote and scan; for the open rows of our runs (run and statement id).
5. **`TRANSCRIPTION_NOTES.tsv`**: every place where the mathematics shows that our text of record misreads
   Grothendieck's page: cote, scan, line, our reading, the reading required, the reason, how sure you are.

A known result is cited with an exact locator and is not proved again, except for a short proof of a form its source
does not state. Every new result is proved in full. An item is finished only when it is proved or refuted. A return may
be marked INCOMPLETE only when the session itself ends. It then gives the state reached, every approach tried with where
it failed, and the next step.
