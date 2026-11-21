**The attached files.** Besides this file there is one ZIP, `DP_MULT_divided_powers_and_the_multiplicity_of_step_2.zip`. Unpack it once: it holds every file named below. Each ZIP named below is already unpacked inside, as a folder of the same name without `.zip` (for example `LIT_Borger_lambda_rings_field_with_one_element.zip` is the folder `LIT_Borger_lambda_rings_field_with_one_element/`), so there is nothing more to unpack; every other file is at the top level under its own name.

# DP_MULT: the multiplicity of step 2 as a divided-power structure, and Grothendieck's crystals

This prompt is one of six run in parallel on 21 November 2026 on what the two proofs of 20 November (Alpöge's, cited as a theorem; Masullo's, a draft) make true in Grothendieck's programme. The others treat: the anabelian and Galois line (30), step 17 and the K-groups of Z (31), the sign-only proof as the Hodge-index route (32), the trace formula of cote 1 (33), divided powers and the multiplicity of step 2 (34), and the zeta functions of schemes and motives (35). A second set (24-29) treats P versus NP through geometric complexity theory and the invariant Δ on the Grothendieck-Teichmüller group. Keep to this prompt's questions; the others are asked there.

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

## Where our files stand

- **Alpöge's step 2** (9 Oct). On a CM curve the invariant derivation D satisfies D^p ≡ 0 for p inert in K, and
  D^a θ(0)/Ω^a is divisible by p^(a/p + a/p³ + ... − O(log a)). Page 1 names the obstacle that multiplicity meets over Z:
  "differentiating whole numbers".
- Our Fable agent (Claude Fable 5.2 at effort max; the attached suggestions file, unchecked: leads, not results), suggestion 2, gives a proof that has not been checked.
  - **The bound.** For a one-dimensional formal group F of height h over W(k):
    v_p(D^a f(0)) ≥ v_p(a!) − a/(p^h − 1) − O(log a).
  - For h = 2 the gain is a·p/(p² − 1) = a/p + a/p³ + ..., the note's exponent. For h = 1 there is none, which is why
    p must be inert.
  - **The proposed use.** CM abelian varieties whose reduction has a formal summand of large height win multiplicity
    faster, with a gain of 1/(p − 1) − 1/(p^h − 1) per derivative.
- **Grothendieck:**
  - cote 54, scans 5-7: the extension S_A as an extension of p-Lie algebras; his boxed "t_A^∨ est muni de la puiss.
    p-ième nulle"; "comparer ... avec ce que donne la dualité de Cartier";
  - the crystals (cote 4; the letter to Tate);
  - divided powers in cote 16 (scan 14) and cote 47 (scan 9), and hunch H8.
  The agent also cites Katz, "Divisibilities, congruences, and Cartier duality" (1981), from memory: this exponent for
  Hurwitz numbers.
- **Suggestion 9** of the same file: Borger's λ-rings and F_1, binomial rings, and Grothendieck's 1976 notes (cotes 133,
  153, 136-137).

## The task

1. **The bound.** Prove it, or refute it with the corrected statement, for every height h, with the exact error term.
2. **Step 2.** Decide whether the note's divisibility is exactly the case h = 2 of item 1 (supersingular reduction, the
   Hasse invariant D^p ≡ 0), and if not, what else it uses.
3. **Higher height.** State and prove the multiplicity gain for CM abelian varieties whose reduction has a formal summand
   of height h. Decide whether a chain of such lifts gives the multiplicity of step 8 with fewer lifts: the shorter
   proof the note expects.
4. **Grothendieck's text.** Read cote 54, scans 5-7, and cote 4 against items 1-3: his p-Lie algebras with zero p-th
   power and Cartier duality. Say what he asks and what is now proved.
5. **Suggestion 9.** Decide whether Frobenius lifts that are the identity (binomial structures) give the homotopy side
   of "differentiating whole numbers". Give a precise statement with its proof.

## The attached files

- The pages of cotes 54, 47 and 4; `ARCHIVE_16_scan014.tex` to `ARCHIVE_16_scan018.tex`.
- `WARGAME_MATH_HUNCHES_20261112.md` (H8).
- `LIT_Borger_lambda_rings_field_with_one_element/`: LaTeX source.
- `ALPOGE_remark.pdf`, `ALPOGE_Main.lean`, `ALPOGE_Statements.lean`, `ALPOGE_LEAN_SCAN.tsv`, `ALPOGE_LEAN_MAP_20261120.md`.
- `FABLE_PROGRAM_SUGGESTIONS_20261120.md` and `..._EXPLAINED.md`.

## The language of the results

State every finding in the language of algebraic geometry and of Grothendieck's frameworks: schemes over Z, ℓ-adic
sheaves, weights and purity (SGA 4, SGA 5, Weil I and II), crystals and divided powers, λ-rings, motives where they apply.
For each finding, say where it lives in Grothendieck's texts: the archive by cote and scan, the SGA, EGA or FGA by exact
locator.

## How to work

The rule that governs everything below: push. Work on the main question first: the divided-power bound for formal groups of height h, whether it is exactly the multiplicity mechanism of Alpöge's step 2, and then the higher-height gain. Give it most of the time.
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
environment, once every 45 minutes of work, each under a new name, `DP_MULT_checkpoint_<NN>.zip` with `NN` counting up.
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

One final ZIP, `DP_MULT_final.zip`, holding:
1. **The paper**, `DP_MULT.tex`, in LaTeX:
   - every finding with its proof (a finding is a new result of this work), each under its id;
   - checked and unchecked findings in separate parts;
   - every cited result with an exact locator (Alpöge's by step and Lean file; Masullo's by statement number; the
     literature by work and statement number; Grothendieck's archive by cote and scan; our runs by run and statement id).
2. **`QUESTIONS.tsv`**, one row for each question treated: id, the source and locator, the question, its state (proved,
   with the finding ids; refuted, with the counterexample; or, if the session ends, its current gate).
3. **`LEDGER.md`** and **`CHECK_EVENTS.tsv`**.
4. **`IMPLICATIONS.md`**: what the findings change in our programme: Grothendieck's texts by cote and scan, the
   open rows of our runs by run and statement id, and the conditional statements of the literature that become
   theorems (unconditional by Alpöge, or conditional on Masullo only).
5. **TRANSCRIPTION_NOTES.tsv**: every place where the mathematics shows that our text of record misreads
   Grothendieck's page (a formula, an index, a sign, a twist, a word), one row each: cote, scan, line, our reading,
   the reading the mathematics requires, the reason, and how sure you are. Our transcription of his archive is the
   project's base layer; these rows go to its second pass against the scans.

A known result is cited with an exact locator and is not proved again, except for a short proof of a form its source
does not state. Every new result is proved in full. An item is finished only when it is proved or refuted. A return may
be marked INCOMPLETE only when the session itself ends. It then gives the state reached, every approach tried with where
it failed, and the next step.
