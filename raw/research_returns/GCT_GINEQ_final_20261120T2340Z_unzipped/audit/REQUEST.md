**The attached files.** Besides this file there is one ZIP, `GCT_GROTHENDIECK_INEQUALITY_and_tensor_norms.zip`. Unpack it once: it holds every file named below. Each ZIP named below is already unpacked inside, as a folder of the same name without `.zip` (for example `LIT_Burgisser_Ikenmeyer_Panova_no_occurrence_obstructions.zip` is the folder `LIT_Burgisser_Ikenmeyer_Panova_no_occurrence_obstructions/`), so there is nothing more to unpack; every other file is at the top level under its own name.

# GCT_GINEQ: Grothendieck's inequality and the projective tensor norm, against tensor rank

This prompt is one of six run in parallel on 20 November 2026. The others treat: Mulmuley's nonstandard Riemann hypothesis (24), plethysm through Grothendieck's λ-rings (25), Kronecker coefficients through his λ-operations on G-sets (26), Grothendieck's inequality and tensor norms (27), GRH and the ETH result in complexity (28), and the invariant Δ on the Grothendieck-Teichmüller group (29). Keep to this prompt's questions; the others are asked there.

## The question

Grothendieck's *Résumé de la théorie métrique des produits tensoriels topologiques* (1953) contains his inequality and
the projective and injective tensor norms. In complexity they meet: semidefinite approximation (Alon-Naor's cut norm);
the Grothendieck constant as the approximation threshold under the Unique Games Conjecture (Raghavendra-Steurer);
quantum XOR games (Tsirelson); the projective tensor norm as the nuclear norm, NP-hard to compute for tensors of order
three (Friedland-Lim); and, in geometric complexity theory, tensor rank and border rank (matrix multiplication; the
permanent against the determinant). The question: what do Grothendieck's inequality and his tensor norms give for rank
and border-rank lower bounds on the tensors geometric complexity theory studies?

## The task

1. **Norms against rank.** Prove lower bounds for rank and border rank of the matrix multiplication
   tensor and of the determinant and permanent tensors, from nuclear and injective norms and their duality; state how
   they compare with the flattening and Koszul-flattening bounds and the barriers known for them.
2. **Grothendieck's inequality as a certificate.** Decide whether semidefinite relaxations with Grothendieck's
   inequality give certifiable lower bounds of these kinds, and prove what they give.
3. **The constant.** State what is known of the Grothendieck constant against the Unique Games threshold, and what
   items 1-2 add.

## The attached files

- `LIT_Pisier_Grothendiecks_theorem_past_and_present/` (arXiv 1101.4195), `LIT_Friedland_Lim_nuclear_norm_of_tensors/`
  (arXiv 1410.6072), `LIT_Landsberg_GCT_introduction_for_geometers/`,
  `LIT_Burgisser_Ikenmeyer_Panova_no_occurrence_obstructions/`: LaTeX sources.

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

The rule that governs everything below: push. Work on the main question first: rank and border-rank lower bounds for the tensors of geometric complexity theory from Grothendieck's inequality and his tensor norms. Give it most of the time.
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
environment, once every 45 minutes of work, each under a new name, `GCT_GINEQ_checkpoint_<NN>.zip` with `NN` counting up.
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

One final ZIP, `GCT_GINEQ_final.zip`, holding:
1. **The paper**, `GCT_GINEQ.tex`, in LaTeX:
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
