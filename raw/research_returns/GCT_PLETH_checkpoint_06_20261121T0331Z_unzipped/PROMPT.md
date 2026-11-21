**The attached files.** Besides this file there is one ZIP, `GCT_PLETHYSM_through_Grothendiecks_lambda_rings.zip`. Unpack it once: it holds every file named below. Each ZIP named below is already unpacked inside, as a folder of the same name without `.zip` (for example `LIT_Borger_lambda_rings_field_with_one_element.zip` is the folder `LIT_Borger_lambda_rings_field_with_one_element/`), so there is nothing more to unpack; every other file is at the top level under its own name.

# GCT_PLETH: plethysm coefficients through Grothendieck's λ-rings and the theta correspondence

This prompt is one of six run in parallel on 20 November 2026. The others treat: Mulmuley's nonstandard Riemann hypothesis (24), plethysm through Grothendieck's λ-rings (25), Kronecker coefficients through his λ-operations on G-sets (26), Grothendieck's inequality and tensor norms (27), GRH and the ETH result in complexity (28), and the invariant Δ on the Grothendieck-Teichmüller group (29). Keep to this prompt's questions; the others are asked there.

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

## The question

Plethysm is composition in Λ, the free λ-ring on one generator: the composition of Schur functors. Its coefficients are
the multiplicities geometric complexity theory needs in the coordinate rings of orbits and orbit closures: Foulkes-Howe
(Sym^m Sym^n against Sym^n Sym^m), the Hadamard-Howe map, the Chow variety and the orbit closure of x_1⋯x_n.
Grothendieck created λ-rings (1957, for Riemann-Roch; SGA 6), and his pages attached (cote 133 and others, transcribed,
with the study of cote 133 from our sweep) work with plethysm and λ-operations. Alpöge's proof wins multiplicity by
chains of theta lifts and counts interlacing (Gan-Gross-Prasad periods, values 0 or 1); a chain of compact dual pairs
counts Gelfand-Tsetlin patterns. The question: do these give positive formulas, or the nonvanishing geometric
complexity theory needs, for the plethysm coefficients?

## The task

1. **His pages as mathematics.** Read every attached archive page; state each λ-ring or plethystic statement on it,
   with cote and scan, and prove or refute it. Say what each gives for plethysm coefficients.
2. **Plethysm in a theta correspondence.** Express plethysm coefficients, or the Foulkes-Howe and Hadamard-Howe
   multiplicities, as multiplicities in a theta correspondence or a branching along a chain of compact dual pairs (Howe
   duality), and derive positive formulas (counts of lattice points in polytopes) wherever this works. Where it does not,
   prove what blocks it.
3. **Foulkes-Howe and Hadamard-Howe.** Decide what the formulas of item 2 give for injectivity or surjectivity of the
   Hadamard-Howe map in the ranges open today, with exact statements.
4. **The rectangular cases** of Ikenmeyer-Panova: positivity and nonvanishing statements that follow, proved.

## The attached files

- `LIT_Ikenmeyer_Panova_rectangular_Kronecker_plethysm/`, `LIT_Burgisser_Ikenmeyer_Panova_no_occurrence_obstructions/`,
  `LIT_Borger_lambda_rings_field_with_one_element/`, `LIT_Landsberg_GCT_introduction_for_geometers/`,
  `LIT_Mulmuley_GCT_VII_nonstandard_quantum_group_plethysm/`: LaTeX sources.
- `ARCHIVE_<cote>_scan<NNN>.tex`: Grothendieck's pages (our transcription of the scans), and `SA17_STUDY_cote133_lambda.md`.
- `ALPOGE_remark.pdf`; `FABLE_PROGRAM_SUGGESTIONS_20261120.md` and `..._EXPLAINED.md` (suggestion 8 bears here; leads only).

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

The rule that governs everything below: push. Work on the main question first: positive formulas, or the nonvanishing geometric complexity theory needs, for the plethysm coefficients, through Grothendieck's λ-ring pages and the theta correspondence. Give it most of the time.
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
environment, once every 45 minutes of work, each under a new name, `GCT_PLETH_checkpoint_<NN>.zip` with `NN` counting up.
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

One final ZIP, `GCT_PLETH_final.zip`, holding:
1. **The paper**, `GCT_PLETH.tex`, in LaTeX:
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
