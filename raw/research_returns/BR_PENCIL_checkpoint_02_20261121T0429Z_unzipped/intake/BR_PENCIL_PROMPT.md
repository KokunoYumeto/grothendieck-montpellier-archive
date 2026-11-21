**The attached files.** Besides this file there is one ZIP, `BR_PENCIL_border_rank_of_det4_and_per4_by_multi-dimensional_.zip`. Unpack it once: it holds every file named below. Each ZIP named below is already unpacked inside, as a folder of the same name without `.zip` (for example `LIT_Burgisser_Ikenmeyer_Panova_no_occurrence_obstructions.zip` is the folder `LIT_Burgisser_Ikenmeyer_Panova_no_occurrence_obstructions/`), so there is nothing more to unpack; every other file is at the top level under its own name.

# BR_PENCIL: border rank of the 4×4 determinant and permanent by substitution of more than one dimension

This prompt continues GCT_GINEQ (our prompt 27). Its return (`RETURN_GCT_GINEQ_final_*`) and our intake of it are
attached; cite them by finding id.

**Where it stands.** GCT_GINEQ proved, without norms (its F-23): the minimum over 0 ≠ u ∈ U_{n,b} of the border rank of
the residual u equals BR(T_b), hence BR(T_n) ≥ C(n,b)^s + BR(T_b) − 1, and this gives border rank ≥ 39 for the 4×4
determinant and permanent. Our intake confirmed all 23 findings with full proofs, and the run's scripts pass on rerun.
A literature check on 21 Nov 2026 (in `INTAKE_GCT_KRON_cp03_20261121.md`) found no published lower bound of 39 or more
for either polynomial: Farnsworth's 38 is for the symmetric border rank of the determinant (arXiv:1505.05079), the
catalecticant bound gives 36 for the permanent, and Landsberg-Teitler's 40 bounds the rank, not the border rank
(arXiv:0901.0487).

## The task

1. **Main question: substitution of more than one dimension (the intake's 5.1b) on the four families.** Determine the
   minimum, over the Grassmannian Gr(j, U_{n,b}), of the border rank of the residual pencil, through Koszul flattenings
   of the pencil, with an exact computation at n = 4, b = 2, j = 2. The aim is a lower bound above 39 for det_4 and
   per_4. Prove every bound you obtain, with its certificate.
2. **The SDP question.** Certify α(U) by the DPS hierarchy, with proved error bounds, for one residual image outside the
   four families (GCT_GINEQ's open row Q-30).
3. **Fields.** State and prove F-23 over every algebraically closed field, using F-18 (properness) and F-22 (the integral
   catalecticant).
4. **Orbits.** Treat the orbit-invariant version of α (the maximum over the GL orbit, through Kempf-Ness) against F-19.
5. **Literature.** Before any bound is called new, check it against the bounds on the border rank of det_n and per_n
   after Farnsworth (2015), and against Conner-Harper-Landsberg's border apolarity.

## The attached files

- The predecessor: `PREVIOUS_PROMPT_27.md` and its attachments (Bürgisser-Ikenmeyer-Panova, Friedland-Lim, Landsberg's
  introduction to GCT, Pisier on Grothendieck's theorem, as LaTeX).
- `RETURN_GCT_GINEQ_final_*/`: the run's paper, registers, checks and scripts. `INTAKE_GCT_GINEQ_20261121.md` and
  `INTAKE_GCT_KRON_cp03_20261121.md`, with their check events.
- `LIT_Farnsworth_Koszul_Young_flattenings_det/` (arXiv:1505.05079) and `LIT_Landsberg_Teitler_ranks_of_polynomials/`
  (arXiv:0901.0487), as LaTeX.

## The language of the results

Whatever the outcome for P versus NP, the mathematics of this prompt has to transfer to our programme on Grothendieck's
work. So every finding is also stated, with its proof or the exact dictionary that carries the proof across, in the
language of algebraic geometry and of Grothendieck's own frameworks: schemes and group schemes over Z (SGA 3), λ-rings,
K_0 and the γ-filtration (SGA 6), representation rings as K_0 of categories of representations, Schur functors as
operations on locally free sheaves, orbit closures as schemes over Z with their Hilbert and Quot schemes (FGA), ℓ-adic
sheaves, weights and purity (SGA 4, SGA 5, Weil II), motives where they apply. For each finding, say where it lives in
Grothendieck's texts: the archive by cote and scan, the SGA, EGA or FGA by exact locator. A finding proved in
combinatorial, representation-theoretic or complexity language is stated again in this language in the paper, in a
part of its own, with the dictionary.

## How to work

The rule that governs everything below: push. Work on the main question first: a lower bound above 39 for the border rank of det_4 and per_4, by substitution of a subspace of dimension j > 1 in F-23 through Koszul flattenings of the residual pencil, with the computation at n = 4, b = 2, j = 2. Give it most of the time.
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
environment, once every 45 minutes of work, each under a new name, `BR_PENCIL_checkpoint_<NN>.zip` with `NN` counting up.
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

One final ZIP, `BR_PENCIL_final.zip`, holding:
1. **The paper**, `BR_PENCIL.tex`, in LaTeX:
   - every finding with its proof (a finding is a new result of this work), each under its id;
   - checked and unchecked findings in separate parts;
   - every cited result with an exact locator (Alpöge's by step and Lean file; Masullo's by statement number; the
     literature by work and statement number; Grothendieck's archive by cote and scan; our runs by run and statement id).
2. **`QUESTIONS.tsv`**, one row for each question treated: id, the source and locator, the question, its state (proved,
   with the finding ids; refuted, with the counterexample; or, if the session ends, its current gate).
3. **`LEDGER.md`** and **`CHECK_EVENTS.tsv`**.
4. **`IMPLICATIONS.md`**: what the findings change, for P versus NP through geometric complexity theory and for
   Grothendieck's texts (cote and scan).

A known result is cited with an exact locator and is not proved again, except for a short proof of a form its source
does not state. Every new result is proved in full. An item is finished only when it is proved or refuted. A return may
be marked INCOMPLETE only when the session itself ends. It then gives the state reached, every approach tried with where
it failed, and the next step.
