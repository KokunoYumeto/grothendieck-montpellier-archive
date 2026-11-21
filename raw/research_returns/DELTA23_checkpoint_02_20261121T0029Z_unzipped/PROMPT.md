**The attached files.** Besides this file there is one ZIP, `DELTA_2-3_reciprocity_of_frames_on_GT.zip`. Unpack it once: it holds every file named below. Each ZIP named below is already unpacked inside, as a folder of the same name without `.zip` (for example `DELTA_ON_GT.zip` is the folder `DELTA_ON_GT/`), so there is nothing more to unpack; every other file is at the top level under its own name.

# DELTA23: the invariant Δ on the Grothendieck-Teichmüller group as a 2-3 reciprocity of frames

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

## Where our runs stand

- **LM7_PUSH** (GPT-6 Astra, Pro mode; results and sections attached). The objects are these:
  - the modular group B = C_2 ∐ C_3 = ⟨s, r | s^2 = r^3 = 1⟩, with s at the harmonic point j = 1728 (CM by Z[i]) and r
    at the equianharmonic point j = 0 (CM by Z[ω]);
  - GT̂_0, the "gentle group": the part of GT̂ cut out by the relations at these two points, without the pentagon;
  - the frames of F ∈ GT̂_0: the conjugators β_F, A_F with F(s) = β_F s β_F^-1 and F(r) = A_F r A_F^-1.

  E.65 proves that the CM parity is a continuous character of the full gentle group. E.58 constructs, by relative
  pronilpotent lifting, an element in the extra CM coset. E.3 (open) asks whether the full GT̂ reaches that coset.
- **DELTA_ON_GT** (GPT-6 Astra, Pro mode, checkpoint 05; attached). Its proved and open rows are these:
  - A.6 (proved): the frame sign u ∈ {1, 5, 7, 11} ⊂ (Z/12)^× is the CRT encoding of two parities, u ≡ (−1)^(a_3)
    mod 3 and u ≡ (−1)^(a_2) mod 4, with Δ = a_2 + a_3 mod 2.
  - A.5 (proved): the plain product formula, Weil reciprocity for the Kummer class of 1 − 1728/j with residues (1, 1, 0)
    at (0, 1728, ∞), does not by itself compare the two CM frames. Identifying (−1)^Δ with an independently defined
    local datum is an additional comparison.
  - Open: A.84 (the main quadratic decision on the full profinite pentagon group), A.24 (the missing passage from these
    fields to order-five frame characters), A.86 (the level-six Atkin-Lehner comparison) and B.40 (all relative
    quadratic characters of the gentle group).
- **Our Fable agent** (Claude Fable 5.2 at effort max; suggestion 1 of the attached file, unchecked) proposes the
  missing comparison:
  - Δ = χ_12(u), with χ_12 = χ_{−4} χ_{−3} the character of Q(√3), the real subfield of Q(i, ω);
  - a_2 and a_3 as local symbols at 2 and at 3 (Hilbert or Kubota) of the pair of frames;
  - Δ = 0 on Galois as a reciprocity law, and A.84 as the question whether the pentagon forces that product formula.
    Elements with unequal bits pass each local test and fail the product formula.

  It also points to:
  - the metaplectic reciprocity in Alpöge's steps 3 and 5: Gauss sums of order #μ_K on the #μ_K-fold cover, and "the
    reciprocity law of y(c·c′) against y(c)·y(c′)";
  - the quaternion algebra (−1, −3), ramified at 3 and ∞, the endomorphism algebra of the supersingular curve in
    characteristic 3, where j = 0 and j = 1728 coincide;
  - the quotients Ẑ[ω] ⋊ C_6 and Ẑ[i] ⋊ C_4 of the tripod group, the (2,3,6) and (2,4,4) triangle groups.

## The task

1. **The comparison.** Prove or refute: a_2 and a_3 are local symbols at 2 and at 3 of the pair of frames, for a
   definition you state, so that (−1)^Δ is their product. Evaluate on the element of E.58.
2. **The main question, A.84.** Decide whether the hexagon and pentagon relations force a_2 = a_3 on GT̂, that is,
   whether Δ = 0 on the full profinite Grothendieck-Teichmüller group (E.3 of LM7_PUSH).
3. **Order five, A.24.** The pentagon lives on M_{0,5}: give the passage from the fields of item 1 to order-five frame
   characters, and decide what it says about Δ.
4. **Level six, A.86.** Make the level-six Atkin-Lehner comparison well defined and decide it; relate it to the
   quaternion algebra of discriminant 6 (the Hilbert symbol (2, 3) is −1 exactly at 2 and 3) if it bears.
5. **B.40.** Determine all relative quadratic characters of the gentle group.

## The attached files

- `DELTA_ON_GT/`: the checkpoint-05 return:
  - the report and the results CSV;
  - `sections/*.tex`, which hold every statement with its proof;
  - `agent_five/five_point_results.tex`;
  - `agent_lifting/`.
- `LM7_PUSH/`: the results CSV and the sections of E.1-E.65 (`E_agent.tex`, `E_relative_cm_lift_agent.tex`,
  `E_cm_character_agent.tex`).
- `ALPOGE_remark.pdf`.
- `FABLE_PROGRAM_SUGGESTIONS_20261120.md` and `..._EXPLAINED.md` (suggestion 1). These are leads, not results.

## How to work

The rule that governs everything below: push. Work on the main question first: whether Δ = 0 on the full profinite Grothendieck-Teichmüller group (A.84), through the 2-3 comparison of frames. Give it most of the time.
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
environment, once every 45 minutes of work, each under a new name, `DELTA23_checkpoint_<NN>.zip` with `NN` counting up.
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

One final ZIP, `DELTA23_final.zip`, holding:
1. **The paper**, `DELTA23.tex`, in LaTeX:
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
