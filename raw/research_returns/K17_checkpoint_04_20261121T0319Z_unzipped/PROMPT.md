**The attached files.** Besides this file there is one ZIP, `STEP17_K-groups_of_Z_Soule_and_pro-l_kernels.zip`. Unpack it once: it holds every file named below. Each ZIP named below is already unpacked inside, as a folder of the same name without `.zip` (for example `LIT_Deligne_Goncharov_mixed_Tate_motives.zip` is the folder `LIT_Deligne_Goncharov_mixed_Tate_motives/`), so there is nothing more to unpack; every other file is at the top level under its own name.

# K17: step 17 of Alpöge's note, the K-groups of Z, Soulé's characters and the pro-ℓ kernels of the tripod

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

- **Alpöge's step 17** (page 4 and footnote 6): for the classes in H^1(o_E[1/ℓ], Q_ℓ/Z_ℓ(−e)) that twisting cannot
  kill, the note proves "a significant weakening of Vandiver". He believes the vanishing of a number of K-groups of Z
  follows ("I had Lichtenbaum"). Our map of the Lean archive found no file named for Vandiver, so the exact statement is
  taken from the note.
- **The literature, cited from memory; verify each locator before use:**
  - Kurihara (1992): Vandiver's conjecture at ℓ is equivalent to the vanishing of K_{4k}(Z) ⊗ Z_ℓ for all k.
  - Soulé: his characters κ_m (m odd, m ≥ 3) are nonzero, and their images are governed by the ℓ-parts of the
    K-groups of Z.
  - Sharifi: for regular ℓ, the kernel field of G_Q → Out π_1^(ℓ)(P^1 − {0, 1, ∞}) is the maximal pro-ℓ extension of
    Q(μ_ℓ) unramified outside ℓ.
  - Deligne-Goncharov (LaTeX attached) and Brown: mixed Tate motives over Z.
- **Our runs:**
  - LM6 A.44-A.45: the kernel question, open at ℓ = 2 and at the irregular primes (its intake is attached);
  - bridge B3 of the war game: grt_1 and mixed Tate motives over Z (the war-game file is attached);
  - SA06's E.4 rows, which tabulate groups H^1(o_E[1/ℓ], ...);
  - cote 149, scans 79-85: Grothendieck's H^1(S, T) and Kummer sequences, with T = Ẑ(1).
- Our Fable agent (Claude Fable 5.2 at effort max; the attached suggestions file, unchecked: leads, not results), suggestion 5, proposes that if the K_{4k}(Z) of footnote 6 vanish, then two things hold beyond the
  regular primes: the generators σ_{2k+1} of the Galois image in the pro-ℓ group of the tripod exist integrally, and
  the kernel field is the maximal pro-ℓ extension of Q(μ_ℓ) unramified outside ℓ.

## The task

1. **Step 17.** State it exactly: the fields E, the twists e, the primes ℓ and the classes. Prove it from the note's
   argument and the theorems it cites.
2. **The K-groups of Z.** Decide which K_{4k}(Z) ⊗ Z_ℓ vanish as a consequence, for which k and ℓ, and state the
   relation to Vandiver's conjecture at ℓ exactly.
3. **LM6 A.44-A.45.** Decide them at the irregular primes and at ℓ = 2 with what items 1 and 2 give.
4. **B3, integrally.** For the ℓ that item 2 covers, decide whether the generators σ_{2k+1} of the image in the
   pro-ℓ group of the tripod exist integrally. Give the consequences for grt_1 and for the Deligne-Ihara statement over
   Z_ℓ.
5. **Cote 149, scans 79-85.** Read Grothendieck's H^1(S, T) and Kummer sequences against items 1-4: what his text asks,
   and what is now proved.

## The attached files

- `ARCHIVE_149_scan079.tex` to `ARCHIVE_149_scan085.tex`.
- `INTAKE_LM6_FINAL_20261114.md`; `INTAKE_RESEARCH_SA06_20261120.md` (the E.4 rows); `PROGRAM_WARGAME_ROUND2_20261112.md`
  (bridge B3, S9).
- `LIT_Deligne_Goncharov_mixed_Tate_motives/`: LaTeX source.
- `ALPOGE_remark.pdf`, `ALPOGE_Main.lean`, `ALPOGE_Statements.lean`, `ALPOGE_LEAN_SCAN.tsv`, `ALPOGE_LEAN_MAP_20261120.md`
  (our map of the Lean archive); `BRIDGES_QUESTIONS.tsv` (Q06).
- `FABLE_PROGRAM_SUGGESTIONS_20261120.md` and `..._EXPLAINED.md`.

## The language of the results

State every finding in the language of algebraic geometry and of Grothendieck's frameworks: schemes over Z, ℓ-adic
sheaves, weights and purity (SGA 4, SGA 5, Weil I and II), crystals and divided powers, λ-rings, motives where they apply.
For each finding, say where it lives in Grothendieck's texts: the archive by cote and scan, the SGA, EGA or FGA by exact
locator.

## How to work

The rule that governs everything below: push. Work on the main question first: the exact statement of step 17 and what it proves about the K-groups of Z and Vandiver's conjecture, then LM6 A.44-A.45 at the irregular primes and at ℓ = 2. Give it most of the time.
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
environment, once every 45 minutes of work, each under a new name, `K17_checkpoint_<NN>.zip` with `NN` counting up.
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

One final ZIP, `K17_final.zip`, holding:
1. **The paper**, `K17.tex`, in LaTeX:
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
