**The attached files.** Besides this file there is one ZIP, `ZETA_NEXT_effective_class_numbers_Lambda_schemes_and_the_non.zip`. Unpack it once: it holds every file named below. Each ZIP named below is already unpacked inside, as a folder of the same name without `.zip` (for example `LIT_Borger_Lambda_rings_and_the_field_with_one_element.zip` is the folder `LIT_Borger_Lambda_rings_and_the_field_with_one_element/`), so there is nothing more to unpack; every other file is at the top level under its own name.

# ZETA_NEXT: effective class numbers from Alpöge's theorem, the bad fibres of Λ-schemes, and the non-CM gate

This prompt continues ZETA_TWO (our prompt 35). Its return (`RETURN_ZETA_TWO_final_*`) and our intake of it
(`INTAKE_ZETA_TWO_20261121.md`) are attached. Build on them and cite them by statement id. Do not redo what they settled:
the dependency tables of what needs Alpöge's theorem and what needs Masullo's are in `CONDITIONAL_AUDIT.tsv`, and
ZETA_TWO's IA01 audit stands.

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

## The task

1. **Main question: effective Brauer-Siegel for normal fields from Alpöge's theorem, and what it makes effective.**
   Stark (Invent. Math. 23 (1974); the locators Lemma 8 and Theorem 1′ are to be checked) places every exceptional zero
   of the Dedekind zeta function of a normal number field K in the zeta function of a quadratic subfield, so in a
   quadratic Dirichlet L-function, where Alpöge's theorem excludes it. Our intake confirmed this reduction (ZETA_TWO
   IA05) at the level of its logic; its constants were read only at statement level.
   - State and prove the resulting effective lower bound for h_K R_K for every normal K, with explicit constants, and
     carry it through the Galois closure to CM fields of fixed degree.
   - Then decide which known proofs become effective with it: the Galois-orbit lower bounds for CM points in A_g
     (Tsimerman's proof of André-Oort with the averaged Colmez formula), and the Siegel-type class-number bounds for CM
     fields. For each, give the effective statement with its constants and its proof, or locate the step that stays
     ineffective and attack it.
2. **The bad fibres of Λ-schemes.** ZETA_TWO's ZT05 shows that ζ of Spec Z[1/p], which is a Λ-scheme, has the zeros
   2πik/log p on Re s = 0. So a Riemann hypothesis for Λ-schemes can only say that all non-real zeros and poles lie on
   the lines Re s ∈ ½Z. The conjecture to decide: for a Λ-scheme X, flat and of finite type over Z, every bad-fibre
   factor of the finite factor R_{X,S} of ZETA_TWO's ZT04 is a product of factors (1 − ζ p^{j−s})^{±1}, with ζ a root
   of unity and j ∈ Z. It holds for Spec Z[1/n], for the rings of integers of abelian fields and their localizations,
   and for split tori.
   - Prove it or refute it with a counterexample. Borger's Frobenius lifts at the bad prime p (ψ_p lifts the absolute
     Frobenius of the fibre X_p) are the tool to try first. DP_MULT's DP11 gives the criterion for a ring to be a
     Λ-ring (binomial rings).
   - For a proper flat Λ-scheme, decide whether Borger's splitting of the cohomology holds for RΓ_c(X_{F̄_p}) at the bad
     primes as well.
3. **The non-CM gate.** For X a curve or an abelian variety over Q, compute ZETA_TWO's ZT06 list exactly, using
   Faltings' semisimplicity, and name the non-CM L-functions on which the Riemann hypothesis for ζ_X then waits. Close
   ZT06's gap, the splitting of H^j into CM and non-CM summands, in every case where Faltings' theorems and Deligne's
   absolute Hodge cycles give it.

The links between these questions and the two proofs are real. Where a route meets an obstacle, locate it exactly and
take the next route; an obstacle is never an end point.

## The attached files

- The predecessor: `PREVIOUS_PROMPT_35.md` and its attachments (Alpöge's note and Lean files, our bridges files, our
  intakes of 20 Nov, Deligne-Goncharov's LaTeX, Masullo's draft and our index of its statements).
- `RETURN_ZETA_TWO_final_*/`: the run's paper, registers and audits. `INTAKE_ZETA_TWO_20261121.md` with its check
  events.
- `RETURN_DP_MULT_*/`: the paper of the divided-powers run (DP11), with our intakes of it.
- `LIT_Borger_Lambda_rings_and_the_field_with_one_element/`: Borger, arXiv:0906.3146, LaTeX.

## The language of the results

State every finding also in the language of algebraic geometry and of Grothendieck's frameworks (schemes over Z,
λ-rings, K-theory, ℓ-adic sheaves and weights, motives and their L-functions), and say where it lives in his texts: the
archive by cote and scan, the SGA, EGA or FGA by exact locator, and our runs by run and statement id. Then every result
can be used in our programme, whatever else comes of it.

## How to work

The rule that governs everything below: push. Work on the main question first: the effective Brauer-Siegel bound for normal fields from Alpöge's theorem with Stark's reduction, with explicit constants, and its consequences for CM points and class numbers. Give it most of the time.
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
environment, once every 45 minutes of work, each under a new name, `ZETA_NEXT_checkpoint_<NN>.zip` with `NN` counting up.
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

One final ZIP, `ZETA_NEXT_final.zip`, holding:
1. **The paper**, `ZETA_NEXT.tex`, in LaTeX:
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
