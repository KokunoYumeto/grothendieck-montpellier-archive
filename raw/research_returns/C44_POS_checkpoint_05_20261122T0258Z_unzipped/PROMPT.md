**The attached files.** Besides this file there is one ZIP, `C44_POS_positivity_in_Grothendieck_s_1964_programme_cote_44_.zip`. Unpack it once: it holds every file named below. Each ZIP named below is already unpacked inside, as a folder of the same name without `.zip` (for example `LIT_Gu_BB_heights_generalized_Ceresa.zip` is the folder `LIT_Gu_BB_heights_generalized_Ceresa/`), so there is nothing more to unpack; every other file is at the top level under its own name.

# C44_POS: positivity in Grothendieck's 1964 programme (cote 44) and his correspondence route (cote 16, scans 048-050), in every characteristic

This prompt continues two runs:
- **JAC1964** (our prompt 40), Grothendieck's seven theorems on intermediate Jacobians of cote 44;
- **SIGN_NEXT** (our prompt 45), his Hodge-index route through the ring of correspondences of cote 16.

Both were GPT-6 Astra (ChatGPT Pro mode) runs, and both have ended. Attached for each run: its final return
(`RETURN_JAC1964_*`, `RETURN_SIGN_NEXT_*`), our intakes of it, and the check events of those intakes. Our intakes are by
Claude Opus 5.5 at effort high. Cite the runs' findings by their statement ids, and build on them. Do not prove again what
is settled below.

**Grothendieck's texts.** They are attached as our transcriptions, cited by file name: our scan number is the PDF page.
- **Cote 44.** It is the "Programme de travail" of 1964:
  - Th. 1–4 on scan 002;
  - Th. 5 ("Néron") and Th. 6 ("Lefschetz") on scan 004;
  - Th. 7 ("Matsusaka") on scan 006;
  - the letter to Serre of 12.8.1964 on scans 008–009. There, Hodge positivity is reduced to the positivity of
    D = r_*(p^*z · q^*z), with the margin "il faut tenir compte de la décomposition primitive".
- **Cote 16, scans 048–050.** These hold the letter dated 6.1.1966:
  - on scan 049, the semisimplicity of the ring of correspondence classes, from C(X) together with the index relation
    I(X×X);
  - on scan 050, the Proposition relating A(X) to C(Y), A′ and A″, and "the deduction of the Weil conjectures from the
    conjectures C and A".

## Where it stands

### Inputs used as stated, and conditional

- **OpenAI family 032.** It proves the rational Hodge conjecture for CM abelian varieties, with a Lean statement and a human
  proof by van Hoften and Sempliner (Hexagon 2610.00259).
- **Milne's report** (Hexagon 2611.00244). It derives:
  - the Tate conjecture for abelian varieties over finite fields (032, Corollary 8.3);
  - the Hodge standard conjecture for all abelian varieties in every characteristic (032, Corollary 8.4).
  - Its §3.6 prints the primitive form without its sign (−1)^r. Our GHOSTS intake recorded this as C15; use the signed form.

Every result below that uses 032 or Milne's report is **conditional on these unrefereed preprints**. Say so in each
statement. Alpöge's theorem and Masullo's draft play no role here: JAC1964 showed that the Dirichlet GRH alone gives no
height sign (its Q35-GRH).

### Settled, with the check each received

**Th. 4 of cote 44 for abelian varieties in every characteristic: JAC1964 JAC-T4.1 to T4.5.**
- On Saito's higher Picard variety P^m(A) of an abelian variety A of dimension 2m − 1, the primitive summand
  B = P^m(A)_prim carries the rational polarization ((−1)^m/2)Δ^*d_B. This holds over every field, in every characteristic.
- The proof is a curve test on J(C) × A, with 032 Corollary 8.4 as input. Every step has been checked:
  - JAC-P01, JAC-T4.1, JAC-T4.3 and JAC-T4.5: a targeted proof check by our intake;
  - JAC-T4.2: recomputed independently.
- On the full middle factor, Th. 4 is false (JAC-P03, on E³).
- Extensions read only at the level of the statement:
  - H9-T4, H9-T6 and H9-T6a: generic ample sections;
  - H9-T13: odd complete intersections in abelian varieties, in the generic-last-section scope.

**Th. 5 of cote 44 is false as displayed, and corrected.**
- JAC1964 H9-C1: a quadric pencil, in every characteristic, with every fibre geometrically integral.
- SIGN_NEXT SN-44-04: P² × P², where each of the three nodes contributes 1.
- The corrected formula: JAC1964 H9-T1, equal to SIGN_NEXT SN-44-01. Grothendieck's formula holds after one Schur
  correction for each singular fibre.
- No correction is needed when specialization is injective at the singular fibres (H9-T2), equivalently when the vanishing
  cycles are nonzero (SN-44-03).
- All of this was checked by our intakes. SN-44-01's identification with the Néron–Tate pairing on the higher Picard
  variety rests on Kahn and on Chen (arXiv 2512.22788), and is held at the level of the statement.

**After a finite cover (JAC1964 H9-T17, recomputed by our intake).**
- The height on homologically trivial codimension-2 cycles splits orthogonally:
  - into a part with alb(hz) = 0, positive semidefinite in characteristic 0 by S.-W. Zhang (arXiv 1001.4788, Thm. 1);
  - and a Lefschetz part h·Pic⁰, negative definite modulo trace by Kahn.
- An explicit class on an E⁴ pencil has height −12d³, in every characteristic. So the corrected Th. 5 holds only on the
  Albanese-primitive domain: the Chow-theoretic form of the scan 008 margin.

**The height on pencils.**
- H9-T7 splits the height on the whole homologically trivial group into:
  - the ambient primitive form on A_X;
  - an axis form on A_B = ker(κ_*: Alg^{m−1}(B) → H^{2m+2}(X)).
- Here X is an abelian 2m-fold, B the smooth axis of a Lefschetz pencil, and Alg the image of rational Chow groups in
  ℓ-adic cohomology.
- Positivity is proved in these cases (statement level, except as marked):
  - for fourfolds (H9-T8);
  - for every axis in characteristic 0 (H9-T8a);
  - for geometric-generic axes of degree d ≥ 3, where A_B = 0 (JAC-P09).
- H9-T8b reduces the remaining axis sign to axes and cycles over finite fields.

**Covers.**
- H9-T18 makes the positive-characteristic cover sign equivalent to ∫v² ≥ 0 on Alg²(X) ∩ ker(k_*), for one smooth
  incidence fourfold X.
- H9-T19 to H9-T26 kill that space for the geometric-generic families:
  - rational covers of every degree;
  - Kummer covers and every hyperelliptic genus;
  - wild Artin–Schreier covers;
  - full generic triple covers with g ≥ 2;
  - degree N > 2g − 2 when N is even or 3 | N;
  - elliptic triple covers.
- All of these are at statement level.

**Th. 6 and Th. 7.**
- Th. 6 holds for every variety of geometric abelian type (JAC-P16, statement level).
- Th. 7 (numerical = τ-equivalence) is false in characteristic 0 (JAC-P05, through Bloch's Theorem 4.1; Griffiths-type).
- Th. 7 is true over finite fields and F̄_p for abelian type, conditional on 032 with Kahn's theorem (JAC-P15, statement
  level).

**The Fermat arithmetic sign.**
- The motive is N = h³(J)^G of the Fermat quartic Jacobian (JAC-P13, JAC-P17), with its Ceresa-type class η over Q.
- AR-13: h(η, η) > 1/100, by an enclosed numerical certificate, independently rerun by the run.
- AR-11: L′(2) > 7/20 for its weight-four L-function.
- AR-19 with H9-T15: the Bloch–Kato Selmer group has dimension 1 over Q and 2 over Q(i).
- AR-23: η realizes the Selmer line.
- AR-16a: full positivity on CH²(N) over Q follows from ker AJ₅ = 0, where AJ₅ is the 5-adic Abel–Jacobi map of CH²(N)
  over Q, scalar-extended to Q₅.
- Equivalent tests:
  - AR-21: one curve;
  - AR-24: a projected Gross–Schoen cycle;
  - AR-25: sixteen tensor intersections. Positivity there is an instance of S.-W. Zhang's Gross–Schoen Conjecture 2.4.1.
- AR-27: curves with a canonical marked point.
- Refuted routes, in their stated cones: AR-20, AR-22, AR-26, AR-28, AR-29.
- P18: an algebraically trivial radical would give a nonzero homologically trivial cycle on C × J.
- All of these are at statement level, except AR-13's rerun.

**Cote 16, scan 050, corrected (SIGN_NEXT SN-C03 and SN-C04, checked by our intake).**
- Write T = X × X and W for a smooth hyperplane section of T. Then:
  - C_G(X) ⟺ C_G(Y) + R₀(T, W) + G_{L,0}(T, W);
  - A₀(T) ⟺ R₀ + G_{L,0};
  - G_{L,0} ⟺ G₀ + A₀(W).
- Definitions:
  - C_G(X) is Kleiman's B(X): the Lefschetz operator Λ is algebraic.
  - R₀ says that restriction to W is onto on algebraic classes in the critical degree.
  - G_{L,0} is the Lefschetz-weighted Gysin condition: L_T ∘ j_* is onto algebraic classes in the critical degree.
- This restores the factor L_T missing from his A″. The left letter on scan 050 is read as C (SN-C01).
- SN-11: for products of abelian varieties, scan 049's semisimplicity follows from 032 through Milne 2002, Th. 3.3.
- SN-14: the sign-only method cannot by itself give scan 049's positivity, even with correspondences as coefficients.

**The Hodge division attack** (`HODGE_DIVISION_ATTACK_20261121.md`, Theorem W, step 5). It uses, on the Weil plane W of a
complex abelian 2n-fold, the Hodge–Riemann positivity of primitive (n,n) classes. That positivity is the complex case of
cote 44 Th. 4. In characteristic p the same step needs the Hodge standard conjecture, known for abelian varieties under 032
(SN-11).

## The task

1. **Main question: the fixed-axis sign in characteristic p (JAC1964 QH9-axis).**
   - **Setting.** Let X be an abelian 2m-fold over F̄_p, with m > 2, and h an ample class giving a Lefschetz pencil with
     smooth axis B. B is a smooth complete intersection of two members of |h|, of dimension 2m − 2.
   - **The statement to prove or refute.** On A_B = ker(κ_*) ⊂ Alg^{m−1}(B), the axis form of H9-T7 is semidefinite
     with the sign that makes the height semipositive. H9-T7's isomorphism gives that form exactly, in its normalization;
     start by restating it.
     - In characteristic 0 this sign is the Hodge–Riemann sign on B (H9-T8a).
     - So the question is a case of the Hodge standard conjecture for the algebraic middle classes of B lying in ker(κ_*).
       Note that κ^*κ_* is multiplication by h²|_B, so these classes satisfy h²x = 0; identify the exact primitive
       decomposition that H9-T7 uses.
     - By H9-T7 this sign is exactly what the full positivity of the height on CH^m(Y)_hom needs, in Th. 5 of cote 44
       (scan 004), for pencils on abelian varieties.
   - **What is known.**
     - Characteristic 0 is done by Hodge–Riemann (H9-T8a).
     - A_B = 0 for geometric-generic axes of degree ≥ 3 (JAC-P09).
     - The test can be made over finite fields (H9-T8b).
     - So the open case is the special axes over F̄_p, where A_B ≠ 0.
   - **Attack in this order:**
     - (a) Decide whether every class in A_B lifts, with B, to characteristic 0. For classes that lift, the sign follows
       from H9-T8a and the specialization of the intersection form. Determine exactly which special axes carry
       non-liftable algebraic classes, starting with supersingular A.
     - (b) For non-liftable classes, transfer the sign from X, where it is known under 032, by correspondences between B
       and abelian varieties. These are curve tests in the manner of JAC-T4.2, through J(C) × X for curves C ⊂ B. JAC-P19
       excludes a dominant rational map from an abelian variety to B; correspondences are not excluded.
     - (c) The finite-field Newton witness (H9-T5): find a slope outside [m − 1, m] that forces the relevant variable part
       to vanish.
   - **Deliverable.** Prove the sign for every axis, or give a special axis over F̄_p with a primitive algebraic class of the
     wrong sign. In the second case, state the corrected Th. 5 that holds there.
2. **Special covers (JAC1964 QH9-cover-primitivep).**
   - By H9-T18, the positive-characteristic cover sign is equivalent to ∫v² ≥ 0 on Alg²(X) ∩ ker(k_*) for the smooth
     incidence fourfold X attached to an abelian-fourfold pencil and a cover C → P¹.
   - H9-T19 to H9-T26 settle the geometric-generic families. Treat the special loci:
     - first, the special loci of lowest codimension in the Hurwitz spaces of the families already done;
     - then the special hyperelliptic and triple-cover strata.
   - Prove the sign on each, or give a special cover with a new algebraic middle class and compute its height. Use the
     same monodromy tools as T19–T26 (middle-convolution Fourier blocks, lisse trace-kernel towers).
3. **The Fermat arithmetic sign: ker AJ₅ = 0 over Q (JAC1964 QFermat-AJ and Q35-full).**
   - Prove that the 5-adic Abel–Jacobi map CH²(N)_hom ⊗ Q₅ → H¹_f(Q, V₅) is injective for the Fermat motive N. Here V₅ is
     its 5-adic realization and H¹_f the Bloch–Kato Selmer group, which is one-dimensional (AR-19, H9-T15).
   - By AR-16a, injectivity gives the full height positivity on CH²(N) over Q. With AR-11 and AR-23, it gives the
     Beilinson–Bloch equality rank CH²(N)_hom = 1 = ord L(N, s) at the center for this motive.
   - Routes:
     - (a) Euler systems of diagonal or generalized Heegner cycles for this CM motive, in the form of Lilienfeldt–Shnidman
       (arXiv 2408.04375) and Loeffler–Zerbes.
     - (b) The Gross–Schoen height formula and Zhang's Conjecture 2.4.1, through AR-24 and AR-25.
     - (c) The algebraically trivial radical: decide P18's fourfold component on C × J (componentwise cycle-class
       injectivity, or Murre's conjecture (D) there; Xu–Xu prove (A) and (B) for an abelian threefold times a curve).
   - Prove the injectivity, or locate the exact step at which the Euler-system bound fails to reach CH²(N), and attack that
     step.
4. **Scan 050 beyond abelian varieties (SIGN_NEXT SN-C04, with scan 049).**
   - Take a smooth projective X over F̄_p for which B(X) is known and the Hodge standard conjecture I(X × X) is not.
   - First establish that status exactly, with locators. Candidates to examine: supersingular Fermat hypersurfaces of even
     dimension ≥ 4, where Tate is known (Shioda–Katsura) and B holds for complete intersections.
   - On that X:
     - verify each side of SN-C04: C_G(Y), R₀(T, W) and G_{L,0}(T, W), for T = X × X and an explicit hyperplane section W;
     - then decide I(X × X) in the critical degree, and with it scan 049's semisimplicity for X.
   - State which of Grothendieck's conditions on scans 049–050 hold for X, and why.
5. **Theorem W in characteristic p, and the final form of Th. 4 and Th. 5.**
   - **Theorem W.** For an abelian 2n-fold over F̄_p with an imaginary quadratic order acting with signature (n,n), state
     and prove Theorem W's step 5 using JAC-T4.3 or 032 Corollary 8.4. That is the positive definiteness of the Gram
     matrix of the two integral generators y₁, y₂ in the Weil plane. Then prove the full characteristic-p Theorem W, with
     the detector degree and the division bound. Step 3 (norm from degree, by Wirtinger) is archimedean: replace it by an
     ℓ-adic or crystalline bound on the classes of effective cycles of given degree, and prove that bound.
   - **Th. 4, extended.** Extend JAC-T4.3 beyond abelian varieties: to varieties of geometric abelian type, and to the
     complete intersections of H9-T13 without the generic-last-section hypothesis.
   - **Th. 5, final form.** Give one statement covering:
     - the Schur corrections (H9-T1);
     - the injective case (H9-T2);
     - finite covers, through the Albanese-primitive domain of H9-T17;
     - the axis term of H9-T7.

## The language of the results

State every finding also in Grothendieck's terms:
- **Cote 44:** Th. 1–7, with our scan numbers 002, 004, 006, 008 and 009, and the incidence higher Picard varieties
  P^i(X) of his Th. 1–3.
- **Cote 16:** scans 048–050, with his conditions A, A′, A″, C and I, as read in SIGN_NEXT SN-C01 to SN-C04.
- **His frameworks:** Weil cohomology and the standard conjectures, SGA 7 for Lefschetz pencils, and Chow motives.

For each finding, give the cote 44 theorem or cote 16 statement it settles or corrects, and the JAC1964 or SIGN_NEXT row
it closes.

## The attached files

- `RETURN_JAC1964_checkpoint_06_20261121T0521Z/`: the run continued: its paper (Th. 4-7 of cote 44, H9-T1-T26, JAC-P00-P20, AR-1-AR-29), QUESTIONS.tsv, LEDGER.md, CHECK_EVENTS.tsv (146 files: the run's paper, registers, scripts and certificates)
- `RETURN_SIGN_NEXT_checkpoint_02_20261121T0430Z/`: the run continued: SN-C01-C05 (scan 050 corrected), SN-11, SN-14, SN-44-01-06 (221 files: the run's paper, registers, scripts and certificates)
- `INTAKE_JAC1964_20261121.md`: our intake of JAC1964 cp03: checks of JAC-T4.1-4.5, H9-C1, H9-T1, H9-T2; cote 44 locators against our text
- `INTAKE_JAC1964_20261121_part2.md`: our intake of the final: H9-T17 and JAC-P01 checks, what was settled and left open, successor needs
- `INTAKE_JAC1964_20261121_CHECK_EVENTS.tsv`: check events of the intake
- `INTAKE_JAC1964_20261121_part2_CHECK_EVENTS.tsv`: check events of the intake of the final
- `INTAKE_SIGN_NEXT_20261121.md`: our intake of SIGN_NEXT: checks of SN-C02-C05, SN-11-14, SN-44-01-05
- `INTAKE_SIGN_NEXT_20261121_part2.md`: our intake of the final, with its successor list (item 4 is task 4 here)
- `INTAKE_SIGN_NEXT_20261121_CHECK_EVENTS.tsv`: check events of the intake
- `PREVIOUS_PROMPT_40.md` and its attachments: its ZIP carries Grothendieck's texts (ARCHIVE_44_scan001-009, ARCHIVE_16_scan001-056 incl. 048-050), 032 and its companion, van Hoften-Sempliner, Milne's report, Markman
- `HODGE_DIVISION_ATTACK_20261121.md`: Theorem W, whose step 5 is the positivity of task 5
- `HODGE_BRIDGE_SKETCH_20261121.md`: the map of the Hodge line (3.4, 3.5, H9) that JAC1964 answered
- `LIT_Zhang_positivity_heights_codim2_char0/` (arXiv:1001.4788, LaTeX source): S.-W. Zhang, positivity of heights of codimension-2 cycles over function fields in characteristic 0 (used in H9-T17)
- `LIT_heights_refined_pairing_2009.00533/` (arXiv:2009.00533, LaTeX source): the height-pairing source JAC1964 used for H9-T1 and H9-T17 (Kahn's refined height pairing)
- `LIT_Gu_BB_heights_generalized_Ceresa/` (arXiv:2609.33223, LaTeX source): Gu, Beilinson-Bloch heights of generalized Ceresa cycles (task 3)
- `LIT_Lilienfeldt_Shnidman_generalized_Heegner/` (arXiv:2408.04375, LaTeX source): derivatives of Rankin-Selberg L-functions and heights of generalized Heegner cycles (task 3, route a)
- `LIT_Laga_Shnidman_Ceresa_bielliptic_Picard/` (arXiv:2312.12965, LaTeX source): Ceresa cycles of bielliptic Picard curves (task 3)

## The language of the results

State every finding also in the language of algebraic geometry and of Grothendieck's frameworks (schemes over Z,
λ-rings, K-theory, ℓ-adic sheaves and weights, motives and their L-functions), and say where it lives in his texts: the
archive by cote and scan, the SGA, EGA or FGA by exact locator, and our runs by run and statement id. Then every result
can be used in our programme, whatever else comes of it.

## How to work

The rule that governs everything below: push. Work on the main question first: Prove or refute the sign of the axis form of JAC1964 H9-T7, on the algebraic middle classes in ker κ_* of the axis of every Lefschetz pencil on an abelian 2m-fold over F̄_p (m > 2): the one input left for the full positivity of Grothendieck's height on pencils (cote 44, Th. 5, scan 004; JAC1964 QH9-axis). Give it most of the time.
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
environment, once every 45 minutes of work, each under a new name, `C44_POS_checkpoint_<NN>.zip` with `NN` counting up.
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

One final ZIP, `C44_POS_final.zip`, holding:
1. **The paper**, `C44_POS.tex`, in LaTeX:
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
