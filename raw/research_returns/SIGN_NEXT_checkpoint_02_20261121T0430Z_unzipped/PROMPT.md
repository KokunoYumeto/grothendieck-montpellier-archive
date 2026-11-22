**The attached files.** Besides this file there is one ZIP, `SIGN_NEXT_Grothendiecks_Hodge-index_route_after_the_sign-onl.zip`. Unpack it once: it holds every file named below. Each ZIP named below is already unpacked inside, as a folder of the same name without `.zip` (for example `RETURN_HODGE_SIGN_final_20261121T0057Z.zip` is the folder `RETURN_HODGE_SIGN_final_20261121T0057Z/`), so there is nothing more to unpack; every other file is at the top level under its own name.

# SIGN_NEXT: Grothendieck's Hodge-index route after the sign-only proof of purity

This prompt continues HODGE_SIGN (our prompt 32). Its return (`RETURN_HODGE_SIGN_final_*`), our intake of it, and an
independent check of its proof are attached.

**What is settled.** HODGE_SIGN's SG-08 to SG-11 prove Deligne's purity theorem (Weil I, Théorème 1.6, and Weil II,
Théorème 3.3.1 over a point) by the sign-only route of Alpöge's footnote 3, without monodromy. The proof was checked
twice: by Claude Opus 5.5 at effort high, and independently by Claude Fable 5.2 at effort max, who re-proved every step and
took the generic weak Lefschetz input from Deligne's proof in the appendix of Katz's paper (A.3-A.5) instead of the
printed proof of Katz's Corollary 3.4.1 (`CHECK_a3ccbc11_20261121.md`). Cite SG-08 to SG-11, with GCT_NSRH's F03, as the
sign-only theorem; do not prove them again.

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

## The task

1. **Main question: the next step of Grothendieck's Hodge-index route.** With purity proved without weights,
   Grothendieck's route in cote 16 (scans 049-050) needs his conjectures C(X) and I(X×X).
   - Attack his Proposition on scan 050: A(X) ⟺ C(Y) + A′(X×X)⁰ + A″(X×X)⁰. Where the critical-degree conditions hold
     (abelian varieties, through 032's Corollary 8.4; powers of CM elliptic curves, through SG-04), derive C and I.
   - Decide whether the sign-only identity, applied to X×X with correspondences as coefficients, gives Grothendieck's
     semisimplicity statement (scan 049). State exactly what positivity it would need, and prove what can be proved.
2. **Q2c (U-02).** It is closed by 032 (the rational Hodge conjecture for CM abelian varieties: OpenAI's result of
   6 Oct 2026, with a human proof by van Hoften and Sempliner, Hexagon 2610.00259) together with Milne 2002, Theorem 3.3.
   State it so, with the exact locators.
3. **Q6g (U-04, U-05).** HODGE_SIGN stopped at a gate here. Attack: the integral intertwiner, by the Fock model; the
   indices on the actual exterior model; and a test against the step-10 data with m = 2. A gate that depends on data not
   supplied is an item to construct, not a reason to deliver.
4. **Cote 44.** HODGE_SIGN's AR-01 refutes Theorem 5 of cote 44 (scan 004) as displayed: on P²×P², with
   Z = a² − ab + b² and the pencil diag(λ, λ+μ, λ+2μ), the generic member is the flag threefold, Z restricts to 0 there,
   and Z² = 3a²b². Prove the corrected Theorem 5, with the correction from the singular fibres when E = 0, and compute
   the contribution of each nodal fibre in this example.

The archive files are cited by their file names, which are our scan numbers.

## The attached files

- The predecessor: `PREVIOUS_PROMPT_32.md` and its attachments (Alpöge's note and Lean files, cote 16, 34 and 44 scans,
  our bridges files, Fable's suggestions, the war-game hunches).
- `RETURN_HODGE_SIGN_final_*/`: the run's paper and registers. `INTAKE_HODGE_SIGN_20261121.md`, with its check events.
  `CHECK_a3ccbc11_20261121.md`, the independent check.
- `INTAKE_THETA3_20261121.md` and `INTAKE_HECKE_DIV_20261121.md`: our intakes of prompts 37 and 38 (the Fock model and
  bounded division).
- `032_The-rational-Hodge-conjecture-for-CM-abelian-varieties-October-6-2026.pdf`, the van Hoften-Sempliner deposit
  (Hexagon 2610.00259) and Milne's report (Hexagon 2611.00244).

## The language of the results

State every finding also in the language of algebraic geometry and of Grothendieck's frameworks (schemes over Z,
λ-rings, K-theory, ℓ-adic sheaves and weights, motives and their L-functions), and say where it lives in his texts: the
archive by cote and scan, the SGA, EGA or FGA by exact locator, and our runs by run and statement id. Then every result
can be used in our programme, whatever else comes of it.

## How to work

The rule that governs everything below: push. Work on the main question first: the next step of Grothendieck's Hodge-index route in cote 16: his Proposition on scan 050, and C and I where the critical-degree conditions hold. Give it most of the time.
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
environment, once every 45 minutes of work, each under a new name, `SIGN_NEXT_checkpoint_<NN>.zip` with `NN` counting up.
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

One final ZIP, `SIGN_NEXT_final.zip`, holding:
1. **The paper**, `SIGN_NEXT.tex`, in LaTeX:
   - every finding with its proof (a finding is a new result of this work), each under its id;
   - checked and unchecked findings in separate parts;
   - every cited result with an exact locator (Alpöge's by step and Lean file; Masullo's by statement number; the
     literature by work and statement number; Grothendieck's archive by cote and scan; our runs by run and statement id).
2. **`QUESTIONS.tsv`**, one row for each question treated: id, the source and locator, the question, its state (proved,
   with the finding ids; refuted, with the counterexample; or, if the session ends, its current gate).
3. **`LEDGER.md`** and **`CHECK_EVENTS.tsv`**.
4. **`IMPLICATIONS.md`**: what the findings change: for our programme on Grothendieck's work (cote and scan),
   for our runs' open rows (run and statement id), and for the open conjectures named in the task.

A known result is cited with an exact locator and is not proved again, except for a short proof of a form its source
does not state. Every new result is proved in full. An item is finished only when it is proved or refuted. A return may
be marked INCOMPLETE only when the session itself ends. It then gives the state reached, every approach tried with where
it failed, and the next step.
