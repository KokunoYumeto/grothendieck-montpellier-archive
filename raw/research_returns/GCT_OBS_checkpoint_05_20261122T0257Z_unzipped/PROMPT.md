**The attached files.** Besides this file there is one ZIP, `GCT_OBS_explicit_multiplicity_obstructions_for_the_padded_pe.zip`. Unpack it once: it holds every file named below. Each ZIP named below is already unpacked inside, as a folder of the same name without `.zip` (for example `GCT_OBS_intake_scripts.zip` is the folder `GCT_OBS_intake_scripts/`), so there is nothing more to unpack; every other file is at the top level under its own name.

# GCT_OBS: explicit multiplicity obstructions for the padded permanent, and the border rank of the 4×4 determinant and permanent

This prompt continues three runs of 20-21 Nov 2026, all GPT-6 Astra (ChatGPT Pro mode). They are:
- GCT_KRON (our prompt 26): Kronecker coefficients, λ-operations and actual orbit-closure multiplicities;
- CUE_GCT (our prompt 36): random matrices and isolation through geometric complexity theory;
- BR_PENCIL (our prompt 44): border rank of the 4×4 determinant and permanent by multidimensional substitution.

Their final returns (`RETURN_GCT_KRON_*`, `RETURN_CUE_GCT_*`, `RETURN_BR_PENCIL_*`) are attached. So are our intakes of
them and the scripts our intake used for its independent checks. Cite their findings by run and statement id; do not
re-derive what is settled.

**Notation.**
- Let W = Mat_n(C), with N = n² variables. Det_n is the GL_N-orbit closure of det_n in Sym^n W*. The padded permanent
  is z^{n−m} per_m, with z a variable independent of the m² permanent variables; Z_{m,n} is the closure of its orbit.
- For a partition λ ⊢ nd, write:
  - a_λ for the multiplicity of the Schur module S_λ in Sym^d(Sym^n C^N), the ambient multiplicity;
  - K_n(λ) for its multiplicity in the degree-d part of C[Det_n];
  - q_λ for its multiplicity in the degree-d part of C[Z_{m,n}].
- A multiplicity obstruction is a λ with q_λ > K_n(λ). An occurrence obstruction is one with K_n(λ) = 0 < q_λ.
- BR denotes CP border rank. For the polynomials det_4 and per_4 it is the border rank of their coefficient tensors in
  (C^16)^{⊗4}. Write μ_j for the minimum, over j-dimensional subspaces L of the 36-dimensional image of the 2|2
  flattening, of the border rank of the tautological tensor of L in C^j ⊗ C^16 ⊗ C^16.

## Where it stands

**Explicit obstructions with no padding (n = m).**
- *GCT_KRON A-030.* For n ≥ 3, R = n², q = R(n−2), d = R+1 and λ_n = (n+q+1, 3, 2^{R−2}), one has a_λ = 1,
  K_n(λ_n) = 0 = g(λ_n, (d^n), (d^n)) and q_λ = 1.
  - *The separating equation.* It is the Hessian-bracket covariant Θ(F) = q·H(F) dF − nF·dH(F), with H(F) the full
    Hessian determinant.
  - *What makes it work.* Θ vanishes on Det_n because H(det_n) = c_n det_n^{n(n−2)}. It is nonzero on per_n at the
    Mignon-Ressayre point.
- *GCT_KRON A-034.* It extends A-030 to every stretch s ≥ 1: q(sλ_n) ≥ p_n(s) > h_n(s) = K_n(sλ_n), where p_n(s) counts
  partitions of s into parts at most n and h_n(s) those into parts 2, ..., n.
  - *The ray algebra.* The determinant ray algebra is exactly C[U_2, ..., U_n]. The permanent ray algebra contains
    C[Z, U_2, ..., U_n].
- *Checks.*
  - Our intake (Claude Opus 5.5 at effort high) confirmed A-030 and A-034 by a targeted proof check.
  - It confirmed by computation F-024 (a_λ = 1) at nine pairs (n, d), the Mignon-Ressayre point (n = 3, 4, 5), the
    identity H(det_n) = c_n det_n^{n(n−2)} (n = 3, 4), and the point A_* of A-034 (n = 3, 4, 5).
- *GCT_KRON F-025.* At n = m = 3, d = 12, λ = (19, 7, 2^5): q = 6 > K = 5. This is a multiplicity obstruction that is
  not an occurrence obstruction.
  - *Checked:* the permanent side, by our intake's recomputation of the 49×49 Jacobian rank.
  - *Not recomputed:* the determinant side, which is cited from Landsberg-Manivel-Ressayre, Comment. Math. Helv. 88
    (2013), §3.2, p. 476.
- *Limits found by GCT_KRON.*
  - A-035 and A-036: the Hessian and partial-Hessian algebra survives on Det_n for every proper partial dimension, so
    it gives no obstruction under padding m < n.
  - A-037: the binary-cubic/partial-Hessian pair algebra misses a fourth highest-weight copy, S(F)F_0²I_2, so it is
    not exhaustive.

  All three are at statement level in our intake.

**Existence of four-row multiplicity obstructions under genuine padding (CUE_GCT).**
- *R-14 (confirmed by our intake's proof check).* Let c_m be the dimension of the closure P_{m,4} of the image of
  (A_1, ..., A_4) ↦ per_m(x_1A_1 + ... + x_4A_4). The projection of Z_{m,n} to four variables is
  {ℓ^{n−m} q : ℓ linear, q ∈ P_{m,4}}, of dimension c_m + 3. The quaternary determinantal locus D_{n,4} has dimension
  at most 2n² + 2 (G-06, confirmed). So if c_m + 3 > 2n² + 2, then for all large d some λ with exactly four rows has
  q_λ > K_n(λ).
  - *Why the rows count is four.* Four-row multiplicities of Z_{m,n} and Det_n equal those of their four-variable
    images, and G-05 (Beauville) rules out at most three rows.
- *R-13.* c_m = C(m+3, 3) for 4 ≤ m ≤ 16.
  - *Our check.* Independently confirmed by our intake for m = 4-10: the Jacobian rank at a random point mod 2^61 − 1
    equals 35, 56, 84, 120, 165, 220, 286.
  - *Not rechecked by us:* m = 11-16. They rest on the run's own certificates.
- *R-27, with R-23, R-24, R-25, R-26.* The exact value c_m = min(C(m+3, 3), 4m² − 2m + 2) for all m.
  - *G-20.* For m ≥ 17 a four-row gap exists in large degree exactly when n² ≤ 2m² − m + 1.
  - *Status.* At statement level in our intake; the run records root and independent readings.
- *What is non-explicit.* These gaps are non-explicit in λ and degree. G-10 and G-13 give degree bounds, but they are
  astronomically large.
- *G-15.* Any positive four-row gap needs λ_1 ≥ d(n−m) + 4. At statement level.
- *The method's ceiling.* The dimension method cannot pass n/m = sqrt 2 (RQ-26). Higher variable counts r give
  smaller ratios (G-24).

**Necessary conditions in the large-padding range (GCT_KRON).** At n ≥ m^25 any actual obstruction needs:
- m ≥ 190 and 52 rows or more;
- the staircase λ_{2j} ≥ 28 − j;
- λ_3 ≥ 557 or λ_52 ≥ 3;
- M019's λ_4 ≥ 27 or λ_2 ≥ 239063403;
- jet-dominance failure: M-013 and M016 to M019.

Our intake confirmed M-006 (projection containment compares all copies) and M-013 (jet dominance).
- *The weak point.* M-013's survival step rests on the support lemma F-016: every coefficient in a highest-weight
  vector of weight λ has degree at most λ_j outside the first j − 1 coordinates. F-016 is used throughout (M-013, F-025,
  the jet theorems) but is not written as a numbered finding with a full proof. Our intake tested it by computation in
  nine cases, finding no violation.
- *The open row.* QMMAIN (compare all remaining actual multiplicities). Its precise obstacle, in F010, is the ranks of
  the permanent and determinant evaluation tensors.

**Border rank (BR_PENCIL).**
- *R-01 (all fields).* BR(T) ≥ q − j + μ_j, where q is the dimension of the flattening image.
- *P-01.* The torus reduction makes μ_j the least value taken over coordinate j-subsets of the 36 minors.
- *R-07.* μ_j − j is nondecreasing.
- *The minima at n = 4.* μ_2, ..., μ_9 = 6, 8, 9, 11, 12, 14, 15, 16 for both polynomial families.
- *The bounds.*
  - BR(det_4), BR(per_4) ≥ 42 over every algebraically closed field (R-05, with R-04 for the exceptional permanent
    five-plane).
  - BR(det_4), BR(per_4) ≥ 43 over C (R-08 for det, R-10 for per), from μ_7 = 14.
- *Checks.*
  - *Mine (the intake's).* Proof check of R-01, P-01 to P-08, R-02 to R-05, R-07, R-08 and R-10. All 22 of the run's
    verifiers pass on rerun.
  - *Independent recomputations by the intake's own code:*
    - all coordinate subsets for j ≤ 5;
    - R-04, exactly over Q;
    - the full seventh-minimum cover for the permanent: 1,543,608 low-support seven-subsets in 1517 disjoint orbits;
    - all Koszul cases of the seventh minimum: 1506 permanent orbits and 11 determinant order ideals.
  - *Not recomputed by us:* the remaining 25 seventh-minimum cases (14 determinant ideals: P-09, P-12, P-14, P-15;
    11 permanent orbits: P-13, P-15, P-16, P-19). They rest on the run's prolongation (border-apolarity) certificates,
    which pass on rerun but which our own simpler test does not reach.
- *Field scope.* The 43 is characteristic zero only: its certificates are minors mod 1000003.
- *44, at the end of the run (Q-17).* It needs μ_10 ≥ 18.
  - Determinant: 35 of 59 Borel ten-plane ideals remain (P-17 excludes 18; Koszul maps exclude 6).
  - Permanent: 17 ≤ μ_10 ≤ 18, the upper bound from P-20's finite-difference curve.
- *The cubic route.* P-18 caps it at 41 (det) and 38 (per), so it cannot beat 43.
- *Literature.* No published border-rank lower bound of 39 or more for either polynomial was found, by the run's audit
  or by our searches. Farnsworth's 38 bounds the symmetric border rank of det_4 (arXiv:1505.05079, Th. 1.6); the
  catalecticant gives 36. The Waring-rank bounds (Landsberg-Teitler 43 and 40; Boij-Teitler 50 for det_4) bound a
  different quantity.

**Inputs that are not settled.** These are named as such and are to be proved before they are used as inputs:
- GCT_KRON's statement-level findings (A-033, A-035 to A-038, F-028, O-031);
- CUE_GCT's R-22 to R-33 and G-18 to G-28;
- BR_PENCIL's P-11, P-17, P-18, P-20, R-11.

The two proofs of 20 Nov 2026 (Alpöge's GRH for Dirichlet L-functions; Masullo's draft, conditional) enter nowhere in
this prompt.

## The task

1. **Main question: an explicit multiplicity obstruction for the padded permanent at (m, n) = (8, 9).**
   - *Why (8, 9).* R-14 with R-13 proves that some four-row λ ⊢ 9d has q_λ > K_9(λ) for z·per_8 against det_9. By
     R-13, P_{8,4} is the whole space of quaternary octics (c_8 = 165 = C(11, 3)). So the four-row multiplicities of
     Z_{8,9} are exactly those of the coordinate ring of the variety V = {ℓq : ℓ ∈ (C^4)*, q ∈ Sym^8(C^4)*} of
     quaternary nonics with a linear factor (dimension 168). Those of Det_9 are exactly those of the determinantal
     quaternary nonics D_{9,4}, whose dimension is 164 (CUE_GCT R-17).
   - *The task.* Exhibit an explicit partition λ with exactly four rows, a degree d, and an explicit highest-weight
     polynomial that proves q_λ > K_9(λ). The complete comparison of the two isotypic components is required, not
     only one copy.
     - *Determinant side.* Bound the λ-isotypic multiplicity of C[D_{9,4}]_d from above by explicit equations of
       D_{9,4}, its ideal in degree d.
     - *Padded side.* Bound the multiplicity of C[V]_d from below by highest-weight functions nonzero on V.
   - *Constraints and tools.*
     - Obey G-15 (λ_1 ≥ d(n−m) + 4 = d + 4) and the stretched-direction criterion G-17/G-18 (ν_4 > 0, ν_1 > (n−m)s).
     - Use GCT_KRON A-034's ray-algebra method: centered binary invariants, characters under the Borel, valuation
       along a divisor where one side degenerates.
     - The geometry to use: D_{9,4} lies in a Noether-Lefschetz-type locus. A smooth surface F = det M carries the
       arithmetically Cohen-Macaulay sheaf coker M (Beauville, *Determinantal hypersurfaces*). Every member of V is
       reducible.
   - *Degree.* The G-10/G-13 bounds are not to be accepted as the answer. Find the actual first degree in which a gap
     occurs in the chosen direction, or a proved upper bound for it that a computation can reach, and then the
     explicit witness.
   - *(17, 23).* Do the same at m = 17, n = 23, the largest n with n² ≤ 2m² − m + 1 = 562. There c_17 = 1124
     (CUE_GCT R-24), and the four-variable padded image has dimension 1127 against 2·23² + 2 = 1060.
   - *Results in GCT terms.* State the resulting obstructions in GCT's own terms: which representation, which degree,
     which equation of Det_n fails on Z_{m,n}. State them also in Grothendieck's terms: the GL-equivariant coherent
     ideal sheaf of D_{n,4} in P(Sym^n C^4) and its Hilbert function against that of V.

2. **Border rank 44 for det_4 and per_4.** Prove μ_10 ≥ 18 for both polynomial families, giving 36 − 10 + 18 = 44.
   Equivalently, find the first j with μ_j − j ≥ 8 and prove it. Start from BR_PENCIL's Q-17 state.
   - *Determinant.* The 35 remaining Borel ideals of P-17. The run's own next step was substitution in a used-variable
     factor and exact treatment of the remaining Borel parameter families.
   - *Permanent.*
     - Decide whether μ_10 is 17 or 18. Look for a 17-term degeneration of a ten-plane, or prove the lower bound 18 by
       hereditary seven-subset bounds and prolongation (border apolarity).
     - If μ_10 = 17 for one family, determine μ_11 and μ_12 for that family; the target is still μ_j − j ≥ 8.
   - *Certificates.* Give every bound with a certificate that the next item's checker can verify.
   - *If 44 holds.* State the exact value of the first μ_j that gives it, and whether 45 is reachable by the same route.

3. **43 in every characteristic.** BR_PENCIL's 43 rests on minors mod 1000003 lifted to Q.
   - For every characteristic p, decide whether BR(det_4) ≥ 43 and BR(per_4) ≥ 43 hold over an algebraically closed
     field of characteristic p. Use the integral (divided-power) coefficient tensors of BR_PENCIL FL-01.
   - Give unit-minor (integer determinant ±1) versions of the 2997 + 6041 minors of R-08 and R-10 and of the
     prolongation certificates. Where a minor's integer determinant has a prime factor p, give a replacement minor
     or a separate argument in characteristic p.
   - In characteristic 2 the two tensors coincide; use that.

4. **Rerunnable certificates for every computational input above.** For each, give a standalone checker in Python's
   standard library (or with SymPy only), short enough to read, whose output a reader can rerun:
   - BR_PENCIL's 25 prolongation cases of the seventh minimum (P-09, P-12, P-13, P-14, P-15, P-16, P-19);
   - CUE_GCT's R-13 for m = 11 to 16;
   - R-24 and R-25 (c_17 = 1124 and c_18);
   - R-27's finite endpoint certificate, with the insertion argument stated so that the uniform claim follows from
     the checked finite data;
   - for each, the torus-invariant extension enumeration written so that an independent script can redo it.

   Our intake's scripts are attached (`GCT_OBS_intake_scripts/`) as a second implementation to compare against. Their
   simple unique-extension prolongation test (the one that settled BR_PENCIL R-04) is inconclusive on the 25 cases,
   because there the rank of Φ_A on A ⊗ U is below 78. Write the certificates so that a test of that kind can verify
   them, or explain exactly why it cannot.

5. **Covariants outside the Hessian algebra, and the padded continuation of A-034.**
   - A-035 and A-036 close the Hessian and partial-Hessian route under padding. A-037 exhibits a highest-weight copy
     outside the pair algebra (S(F)F_0²I_2).
   - Construct covariants of degree-n forms, built from higher-order derivative determinants or from the A-037 copy,
     that vanish on Det_n and do not vanish on Z_{m,n} for some m < n. Prove each claim.
   - Give the largest n − m for which such a covariant, with ambient multiplicity one in its isotypic component,
     separates. Test it against GCT_KRON's exclusions and the (8, 9) data of item 1.
   - First prove the statement-level inputs A-035 to A-037 as needed.

6. **Multiplicity comparisons beyond n/m = sqrt 2.** The dimension method is capped there (CUE_GCT RQ-26). Compare
   multiplicities without a dimension count, by the ranks of explicit orbit-coefficient matrices (CUE_GCT R-05, R-06,
   G-04) on explicit families of λ. Decide, for a fixed family of four-row or five-row directions, whether gaps exist
   at some n > sqrt 2 · m, and prove the answer.

7. **The support lemma F-016.** State it as a numbered finding and prove it in full: for a highest-weight vector of
   weight λ in Sym^d(Sym^n C^r), every coefficient variable occurring in it has degree at most λ_j outside the first
   j − 1 coordinates. Then list every GCT_KRON finding that depends on it and confirm each dependency.

8. **Landsberg-Manivel-Ressayre p. 476, recomputed.** Recompute independently the ambient multiplicity a = 6 and the
   ideal multiplicity 1 for det_3 at d = 12, λ = (19, 7, 2^5), on which GCT_KRON F-025's K = 5 rests. Then state F-025
   with both sides proved.

9. **The literature, before any result is called new.** Check:
   - items 1, 5 and 6 against Kadish-Landsberg (padded polynomials), Bürgisser-Ikenmeyer-Panova,
     Ikenmeyer-Panova, Dörfler-Ikenmeyer-Panova (multiplicity against occurrence obstructions), Ikenmeyer-Kandasamy,
     and Landsberg's *Geometry and Complexity Theory*;
   - items 2 and 3 against Conner-Harper-Landsberg, Conner-Huang-Landsberg, Buczyńska-Buczyński's border apolarity,
     and the papers after Farnsworth (2015);
   - A-030 and A-034 against Kumar (2015) and Bürgisser-Ikenmeyer-Hüttenhain (2017).

   Give exact locators.

The links between these questions are real. The four-variable reduction of item 1 is exactly where CUE_GCT's existence
theorem and GCT_KRON's explicit method meet. The certificates of item 4 carry both border-rank items. Where a route
meets an obstacle, locate it exactly and take the next route; an obstacle is never an end point.

## The attached files

- `RETURN_GCT_KRON_*`, `RETURN_CUE_GCT_*`, `RETURN_BR_PENCIL_*`: the three runs' final returns, with papers, registers,
  certificates and checkers.
- Our intakes (each with its check events):
  - GCT_KRON parts 1-3 and the checkpoint 03 addendum;
  - CUE_GCT parts 1-4;
  - BR_PENCIL parts 1-2;
  - GCT_GINEQ (for F-23).
- `GCT_OBS_intake_scripts/`: the intake's independent checkers: quaternary dominance, plethysm coefficients, the F-016
  test, the F-025 Jacobian, the Hessian identities, the coordinate-subset lower bounds, R-04, the seventh-minimum cover,
  and the support-factor Koszul maps.
- LaTeX sources:
  - Bürgisser-Ikenmeyer-Panova;
  - Ikenmeyer-Panova;
  - Landsberg-Manivel-Ressayre;
  - Kadish-Landsberg;
  - Buczyńska-Buczyński;
  - Landsberg-Michałek;
  - Conner-Huang-Landsberg;
  - Farnsworth;
  - Landsberg-Teitler;
  - Beauville's *Determinantal hypersurfaces*.

## The attached files

- `RETURN_GCT_KRON_checkpoint_07_20261121T0415Z/`: explicit unpadded obstructions A-030/A-034, F-025, the exclusion ledger (M-006..M-020, O027), F-016 uses, A-035..A-037 limits (351 files: the run's paper, registers, scripts and certificates)
- `RETURN_CUE_GCT_checkpoint_08_20261121T0649Z/`: R-13/R-14 existence criterion, R-17 determinant dimension, R-24..R-27 exact c_m, G-10..G-28, certificates to be made rerunnable (572 files: the run's paper, registers, scripts and certificates)
- `RETURN_BR_PENCIL_checkpoint_02_20261121T0429Z/`: R-01..R-11, P-01..P-21, certificate files (det7, per7, det10_borel, per10_upper18) for items 2-4 (431 files: the run's paper, registers, scripts and certificates)
- `INTAKE_GCT_KRON_20261121.md`: part 1: cote 133 corrections, verdicts
- `INTAKE_GCT_KRON_20261121_CHECK_EVENTS.tsv`: check events of part 1
- `INTAKE_GCT_KRON_cp03_20261121.md`: M-006, M-013 checks; literature status of F-23
- `INTAKE_GCT_KRON_cp03_20261121_CHECK_EVENTS.tsv`: check events
- `INTAKE_GCT_KRON_20261121_part2.md`: A-030, F-024, F-025, F-016 test
- `INTAKE_GCT_KRON_20261121_part2_CHECK_EVENTS.tsv`: check events
- `INTAKE_GCT_KRON_20261121_part3.md`: A-034 check; what the run settled and left open
- `INTAKE_GCT_KRON_20261121_part3_CHECK_EVENTS.tsv`: check events
- `INTAKE_CUE_GCT_20261121.md`: part 1: G-01..G-06, scope table
- `INTAKE_CUE_GCT_20261121_CHECK_EVENTS.tsv`: check events
- `INTAKE_CUE_GCT_20261121_part2.md`: R-14 proof check, c_m for m=4..8
- `INTAKE_CUE_GCT_20261121_part2_CHECK_EVENTS.tsv`: check events
- `INTAKE_CUE_GCT_20261121_part3.md`: R-22 at statement level
- `INTAKE_CUE_GCT_20261121_part3_CHECK_EVENTS.tsv`: check events
- `INTAKE_CUE_GCT_20261121_part4.md`: final state: R-27, G-20, c_9 and c_10, what is open
- `INTAKE_CUE_GCT_20261121_part4_CHECK_EVENTS.tsv`: check events
- `INTAKE_BR_PENCIL_20261121.md`: part 1: 42, independent enumeration j<=5, R-04 recheck
- `INTAKE_BR_PENCIL_20261121_CHECK_EVENTS.tsv`: check events
- `INTAKE_BR_PENCIL_20261121_part2.md`: part 2: 43 in char 0, the 25 prolongation cases not recomputed, 44 state
- `INTAKE_BR_PENCIL_20261121_part2_CHECK_EVENTS.tsv`: check events
- `INTAKE_GCT_GINEQ_20261121.md`: F-23 background, the predecessor of BR_PENCIL
- `GCT_OBS_intake_scripts`: the intake's independent checkers, a second implementation for item 4
- `LIT_Burgisser_Ikenmeyer_Panova_no_occurrence/` (arXiv:1604.06431, LaTeX source): no occurrence obstructions at n>=m^25 (item 9)
- `LIT_Ikenmeyer_Panova_rectangular_Kronecker_plethysm/` (arXiv:1512.03798, LaTeX source): rectangular Kronecker positivity, n>3m^4 (item 9)
- `LIT_Landsberg_Manivel_Ressayre_degenerate_duals/` (arXiv:1004.4802, LaTeX source): Hessian equations and the p.476 values for item 8 (verify the id before packing)
- `LIT_Kadish_Landsberg_padded_polynomials/` (arXiv:1204.4693, LaTeX source): padded polynomials and inheritance (items 1, 9) (verify the id before packing)
- `LIT_Buczynska_Buczynski_border_apolarity/` (arXiv:1910.01944, LaTeX source): border apolarity, the prolongation certificates of items 2-4
- `LIT_Landsberg_Michalek_substitution/` (arXiv:1608.07486, LaTeX source): border substitution, Prop. 2.3 (R-01)
- `LIT_Conner_Huang_Landsberg_laser/` (arXiv:2009.11391, LaTeX source): Prop. 2.1 prolongation lemma, BR(per_3)=16
- `LIT_Farnsworth_Koszul_Young_det/` (arXiv:1505.05079, LaTeX source): the 38 bound, literature comparison
- `LIT_Landsberg_Teitler_ranks/` (arXiv:0901.0487, LaTeX source): catalecticant 36 and Waring bounds
- `LIT_Beauville_determinantal_hypersurfaces/` (arXiv:math/9910030, LaTeX source): determinantal hypersurfaces and ACM sheaves for item 1; G-05 input (verify the id before packing)

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

The rule that governs everything below: push. Work on the main question first: An explicit multiplicity obstruction for the padded permanent at (m, n) = (8, 9): a four-row partition λ, a degree d and an explicit highest-weight polynomial proving q_λ > K_9(λ) for z·per_8 against det_9, through the four-variable reduction to quaternary nonics with a linear factor against determinantal quaternary nonics, and then the same at (17, 23). Give it most of the time.
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
environment, once every 45 minutes of work, each under a new name, `GCT_OBS_checkpoint_<NN>.zip` with `NN` counting up.
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

One final ZIP, `GCT_OBS_final.zip`, holding:
1. **The paper**, `GCT_OBS.tex`, in LaTeX:
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
