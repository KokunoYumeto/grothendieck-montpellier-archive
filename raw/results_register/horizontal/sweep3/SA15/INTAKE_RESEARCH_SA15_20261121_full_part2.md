# Full intake of RESEARCH_SA15 (checkpoint 37), part 2 of 3: ids 319-636 of the unchecked list

Claude Opus 5.5 at effort max, agent a8d07e7854f1cb9b4 (the builder of the RESEARCH_SA15 prompt and the sweep-3 reader of cotes 9
and 100), 21-22 Nov 2026 (machine-clock UTC: round 1 written 21 Nov 23:54 to 22 Nov 00:05, round 2 from 22 Nov 00:05 to about 01:05). Brief: the coordinator's message of 21 Nov ~23:5x UTC (the user: [the user's words, omitted]). Return: `grothendieck_archive_transcription_20261110/research_returns/RESEARCH_SA15_checkpoint_37_20261120T0635Z_unzipped`
(GPT-6 Astra, ChatGPT Pro mode). My list: ids 319-636 of `field_experts/INTAKE_LEDGER.md` section 9, row RESEARCH_SA15, from
`lem:DE-Lang-wedge-pole-bound` to `rem:B-RD52-scope`: 318 named rows, no `auto:*` rows. Ids 1-318 are afcdf31b's, 637-955
a1cf7c6b's. Check events: `INTAKE_RESEARCH_SA15_20261121_full_part2_CHECK_EVENTS.tsv` (round 1: one row per id, 318 rows; round 2 appended 249 rows, 567 in all; see section 6.5). Work file:
`agent_notes/a8d07e7854f1cb9b4_NOTES.md`. Scripts (my work folder, never inside the return): the session scratchpad,
`a8d07e78_intake/` (extract, show, `chk_BRD43.py`, `chk_BRD29.py`, `chk_groups.py`, `chk_simple.py`).

## 0. What I read, and the honest scope

- Every one of the 318 statements was read from the register (`RESEARCH_SA15_results.csv`) and from its TeX environment in
  `sections/` (located by its `\label`). The statements of Parts B, C, D, F and the other A sections were read in full or in their
  first 420-1400 characters; the 171 rows of `A_monodromy.tex` in their first 210 characters, more where checked.
- The proofs total about 916,000 characters (about 230,000 tokens), more than this session had left when the task arrived (its
  context guard was past 70 % at the start). I therefore read the proofs of the rows below that carry the main answers to the
  prompt's questions, checked them, and recorded every other row honestly as **statement read only (no check)**.
- Round-1 counts by check type (rows of the TSV, one per id; the final counts after round 2 are in section 6.5): targeted proof check 33; independent re-proof 16; computation or formal
  certificate 9; carried as background without fault found 12; **statement read only 248**. So 70 of 318 rows are checked in
  some form, 58 of them at the level of a targeted check, a re-proof or a computation.
- Where the rows sit: `A_monodromy.tex` 171 (the characteristic-two monodromy of abelian surfaces, theta divisors and Cartier
  operators), `B.tex` 85 (Part B, the inertia character and Raynaud's criterion for l = p), `D.tex` 14 and `F.tex` 4 (Parts E
  and the R-rows), `C.tex` 4 (Part C, 100:3), other A sections 40 (A.1 counterexamples, ppav lemmas, root-group lemmas).

## 1. What was checked, by Part

### Part A.1: Grothendieck's admitted integral weak Lefschetz fails (A_integral_counterexample, A_surface_counterexample)

- **prop:OC-product-integral-counterexample** (targeted proof check, every step): for a surface X with A very ample and
  h^1(X, A^{-1}) = a > 0, Z = X x P^1 and B = A (x) O(m) with a(m-1) > h^0(X, Omega^1): for every smooth Y in |B|,
  T^2(Z) -> T^2(Y) is not onto and H^2_cris(Z/W) -> H^2_cris(Y/W) has a cokernel with torsion. Checked: Kunneth gives
  H^1(Z, B^{-1}) = 0 and H^2(Z, B^{-1}) = H^1(X, A^{-1}) (x) H^1(P^1, O(-m)); multiplication by any section of B lands in
  H^1(X, O) (x) H^1(P^1, O) = 0, so q(Y) = q(X) + a(m-1); b(Y) = b(Z) (rational weak Lefschetz in degree one); with the torsion
  lemma below, t(Y) - t(Z) >= a(m-1) - h^{1,0}(X) > 0. So (8.3.1) and the torsion-freeness of E(Y), which 8.3 "admet", are
  **false for degree-one sections of threefolds**.
- **lem:OC-first-degree-torsion** (targeted check): dim H^1_dR = b + t (H^1_cris is free); the Hodge spectral sequence gives
  <= q + h^{1,0}; the conjugate spectral sequence gives >= q (its E_2^{1,0} = H^1(V^(1), O) has no differentials).
- **lem:OC-Kummer-very-ample** and **prop:OC-generated-Raynaud** (targeted checks): the input surface. Raynaud's construction
  (as in Mukai 2011, Zheng 2017) gives S with L ample and generated and H^1(S, L^{-1}) != 0 (checked: global generation from
  f_*L = N + N^{p+1}; nonvanishing from the last eigensheaf, N^{p^2-p-2} = T^{p-2}); Kummer covers of degree prime to p make it
  very ample with H^1(S, L^{-1}) a direct summand. Only the very ampleness of L^{(p+1)^2} was read without re-derivation.
- **lem:OC-generated-Tango-root** (independent re-proof of the numerology: g, (dx) = pd P_inf, (p+1) | d, global generation).
- **prop:projective-generic-hw-rank** (targeted check): degenerating to d general hyperplanes shows that the generic
  hypersurface of P^r has bijective Frobenius on H^{r-1}(O). This settles A.3 ("n° 7") for X = P^r.
- **rem:A-cyclic-degree-scope** (read): coherent restriction H^{n-1}(X, O) -> H^{n-1}(Y, O) fails to be injective at degree one
  on a fixed sixfold embedding and is injective for d >= max(1, reg omega_X); this answers, negatively in low degree, the
  question that R1 (8.5.7) had left open.

### Part B (9:10-14): the ordinary case, the refutation of Lead B', explicit examples

- **prop:B-RD3** (independent re-proof): potentially good ordinary reduction, mu_p in K and A[p] unramified imply good reduction,
  in every dimension. This is exactly the statement I proved in sweep 3, before the run (c9_c100.md, part 1 section 3).
- **prop:B-RD4** "Refuted as stated" (independent re-proof of the refutation with my own example): the extension of Q_p by Q_p
  with class log(chi_cyc) is not Hodge-Tate, its graded pieces have good reduction, so the manuscript's monodromy condition
  is weaker than potential semistability; Lead B' (character = inertia trace on D_pst) is false as stated and true with the
  extra hypothesis (prop:B-RD4-dictionary, read).
- **prop:B-RD5** (targeted check): in height one the character is the Teichmuller lift of the mod-p character, nu = 0.
- **prop:B-RD15** (targeted check): full rational p^n-torsion forces p^{n-1}(p-1) | e, so the threshold n = s+2 is vacuous; split
  Tate curves (times canonical lifts) show it is the least one. Correct, but empty: the substantive question is in the
  potentially good class (the run says so).
- **prop:B-RD43** (computation, exact in Q(omega)): P = (0,0) has exact order 8 on E; v_K(q) = 2.
- **prop:B-RD29** and **rem:B-RD37-known-example** (computation, partial): the curve B has Delta = -2*3^9, j = -(3*17)^3/2,
  v_3(j) = 3, so it is potentially supersingular; the Tate parameter has v_K(q) = 12. B[9] = T_q[9] itself not recomputed.
- **prop:B-RD36** (consistency only, t = 2 for that B). **prop:B-RD18** (read; the logic det(T_pM) = chi_p => mu_{p^n} in K
  checked): it extends my R3(b) Kisin construction to level p^n with a Honda group and a Drinfeld full-level construction.
- The other 76 rows of B.tex (the long case analysis of the least index nu in B.4 for p = 2, 3, 5 and p >= 5, e = p-1, ...,
  B-RD20 to B-RD100) were read at the level of the statement only.

### Part C (cote 100, 100:3)

- **prop:C-RD5** (independent re-proof): the explicit counterexample S = Spec Z_5[e]/(e^2), E: y^2 = x^3+x+1 (Delta = -496, a
  5-adic unit), A_U: y^2 = x^3+x+1+e (a nontrivial first-order deformation: dj/db != 0). It is the sweep-3 counterexample of
  c9_c100.md, made explicit.
- **prop:C-RD3** (targeted check): with p locally nilpotent the essential image is decided on S_red (Serre-Tate).
- **prop:C-RD2** (independent re-proof by hand): Hom(Q_p/Z_p, mu_{p^inf}) is not formally unramified for the non-noetherian
  square-zero thickening Z_p + Q_p/Z_p.
- **prop:C-RD1** (background; its rigidity input checked on Z_p[e]/(e^2)): C.3 answered yes, proper epimorphisms of noetherian
  schemes are descent morphisms for Hom of p-divisible groups.

### Part D and E (D.tex, F.tex)

- **lem:DE-kappa** (targeted check): the 8:81 class is the lifting obstruction; the split list is R5 (re-proved twice in sweep 3).
- **E.2 (6:7, the flat case of 1.8)**: lem:DE-crystal-Fdiv and prop:DE-E2-relative-Frobenius (crystals = F-divided systems, no
  smoothness), prop:DE-E2-Fpure (F-pure X: crystals = stratified modules, arbitrary coefficients) and prop:DE-E2-cusps (the
  cusp, not F-pure for any p: Fedder's criterion recomputed) checked; prop:DE-E2-coherent and -flat-charzero checked at their
  local steps; prop:DE-E2-flat-Noetherian (flat coefficients, via Jiang 2023) and -coherent-faithfulness read.
- **E.10 (7:17-19)**: prop:DE-old-proper (test (b) false for the supersingular curve y^2 = x^3-x over F-bar_3: the Cartier identity
  and H^1_et(E, Z/3) = 0 re-derived) and prop:DE-old-site (test (a) false integrally: x^{p-1}dx is p-torsion in H^1_MW) checked.
- **prop:DE-R7, -R8** (independent re-proofs: they are my sweep-3 R7, R8), **prop:DE-R9** (Legendre Hasse polynomial t at
  p = 3 checked), **prop:DE-R10** (targeted check). prop:DE-LT (alpha = 0; the lattices differ for pi^{p+1} = p) read only.

### Root-group and theta lemmas (other A sections, A_monodromy)

- Computations (scripts in my work folder): the radical-generation lemmas FR3 and its corollary by brute force over F_2 for
  n <= 4 (all 7 and 127 sets S for n = 2, 3); 2^a - 1 has a primitive prime divisor for 8 <= a <= 60; |GL_r(F_2)| is no n!/2
  for 8 <= r <= 40 (GL_4(2) = A_8 found as a sanity check); #C(F_16) = 33 for y^2+y = x^5; the Lagrangian counts 15, 40.
- Re-proofs: lem:root-single-transvection-class, lem:root-theta-torsion-delta-bound, prop:root-theta-avoiding-Lagrangian,
  lem:compatible-line-averaging, lem:ppav-three-distinct-values (it holds without the smooth-theta hypothesis: |3Theta| is cut
  out by quadrics, so no trisecant lines), lem:symmetric-independent-diagonal-squarefree (matching expansion of a symmetric
  determinant in characteristic 2), prop:root-full-radical-parabolic-form (from FR3).
- Targeted checks of short proofs: lem:root-corank-one-Lang-inertia, lem:labelled-transposition-wreath-candidate,
  lem:picard-finite-quotient, lem:DE-theta-invariant-divisor-degree, lem:DE-odd-Cartier-evaluation-three (logic, given its two
  inputs), lem:prime-Heisenberg-two-contractions, prop:root-dual-kernel-differential; in Part B, prop:B-RD16 (the "cas test" of
  9:13 refuted by an additive supersingular curve and a canonical lift with the same constant p^n-torsion, as my sweep-3 lead
  proposed; it rests on thm:B-RD12, outside my slice) and prop:B-RD78-CM; prop:B-RD30 read (Bondarko's extension theorem).
- The 150 other rows of A_monodromy.tex (the characteristic-two candidate routes: mixed products, nonordinary ppav, Moore and
  Heisenberg tensors, uniform 7/11/13 constructions, supersingular rectangular systems) were read at statement level only.

## 2. Refuted or corrected

- Nothing in my slice was found false. The run's own refutations in the slice were confirmed where checked: prop:B-RD4 (Lead
  B' refuted as stated) and prop:DE-old-proper / prop:DE-old-site (Grothendieck's tests (a), (b) of 7:19 for his site of W-M
  lifts fail integrally); prop:root-f1-bad-five-kernel records the run's refutation of a stronger nodality claim (its curve,
  genus and two-rank, and the two marked points checked).
- Precisions: lem:ppav-three-distinct-values is true for every principally polarized abelian surface (my re-proof);
  lem:compatible-line-averaging needs |J| odd (the setting has D = (Z/l)^2 with l odd); prop:B-RD15 is correct but vacuous.

## 3. What is new (in this slice, as far as checked)

- Grothendieck's "Nous admettrons" of 8.3 is false as stated: integral crystalline weak Lefschetz (torsion-free E(Y), and
  Tors(X) = Tors(Y)) fails for degree-one sections of threefolds built from Raynaud surfaces; the coherent injectivity left open
  by R1 fails in degree one in dimension six and holds in high degree.
- Grothendieck's question 6:7 (crystals = stratified modules for flat, non-smooth S -> R) is answered for F-pure X, for the cusp
  and for flat coefficients; his tests 7:19 for the site of W-M lifts fail integrally.
- The ordinary case of 9:14 (B-RD3) is a theorem; Lead B' is false as stated; explicit p = 2 and p = 3 pairs exist (B-RD29,
  B-RD43). Corollary 3 of 100:25 is true (C-RD1).

## 4. Hexagon readiness (field_experts/HEXAGON_CANDIDATES.md, the five tests)

- **Candidate: "Grothendieck's admitted integral weak Lefschetz fails"** (OC-product-integral-counterexample with
  OC-first-degree-torsion, OC-generated-Raynaud, OC-Kummer-very-ample). Test 1 (complete): the chain is written in full; I have
  checked every step except the very ampleness of L^{(p+1)^2}. Test 2 (self-contained): inputs are Mukai 2011, Zheng 2017,
  Illusie 1979 and Nakkajima-Yobuko 2022 (arXiv, version 3; a published locator to be found). Test 3 (stable): **a literature
  search is still needed** (torsion in the crystalline cohomology of hyperplane sections from Kodaira non-vanishing may be known),
  and the run's checkpoint is not final. Test 4 (checked): targeted proof checks are recorded here; an independent re-proof
  or an explicit computation is still missing. Test 5: moderate (it settles the hypothesis 8.3 of cote 4). **Two gates left:
  the literature search and one independent re-proof.**
- **9:14 "faux par Tate"**: the ordinary half (B-RD3) is checked twice (my sweep-3 proof and this intake); the supersingular
  counterexamples are thm:B-RD12/13 (outside my slice) and B-RD18 (read). Gates: a literature search on Raynaud's semi-stable
  reduction criterion with l = p, and the check of thm:B-RD12 by whoever holds ids 1-318 or 637-955. Not ready.
- Nothing else in my slice passes tests 1-4.

## 5. Scope left for a later pass

The 260 rows recorded as "statement read only": the B.4 case analysis (B-RD20 to B-RD100, many with exact certificates in
`code/reduction_descent/`), the characteristic-two monodromy lemmas of A_monodromy.tex, prop:C-RD1's general rigidity
argument, prop:DE-LT, and the D-section crystal comparisons that rest on Jiang and Gaitsgory-Rozenblyum. A Pro intake prompt,
or a reader with a fresh context, would take them in the TSV's order.

## 6. Round 2 (22 Nov 2026, the coordinator's second message): the 248 rows read at statement level

### 6.1 Independent re-proof of the Hexagon candidate: Grothendieck's admitted integral weak Lefschetz fails

Statement (prop:OC-product-integral-counterexample, sharpened only in its inputs). Let k be algebraically closed of
characteristic p, X a smooth projective connected surface, A very ample on X with a = h^1(X, A^{-1}) > 0, and m >= 1 with
a(m-1) > h^0(X, Omega^1_X). Put Z = X x P^1 and B = A (x) O(m) (very ample). For every smooth Y in |B|, with
u_i: H^i_cris(Z/W) -> H^i_cris(Y/W) and T^2 the torsion of H^2_cris:
(i) T^2(Z) -> T^2(Y) is not surjective, so (8.3.1) of 4:4 fails; (ii) coker(u_2) is not torsion-free, so "E(Y) sans torsion" fails
(here n = 3, n-1 = 2).

My proof, with external inputs different from the run's where it matters:
1. Y is connected (an ample divisor on a smooth connected projective threefold).
2. Kunneth: H^1(Z, B^{-1}) = H^0(A^{-1}) (x) H^1(O(-m)) + H^1(A^{-1}) (x) H^0(O(-m)) = 0, and H^2(Z, B^{-1}) = H^1(X, A^{-1}) (x)
   H^1(P^1, O(-m)), of dimension a(m-1). Kunneth is compatible with cup products, so multiplication by any section
   s = sum s_i (x) t_i of B sends this group into H^1(X, O) (x) H^1(P^1, O) = 0. The divisor sequence gives
   0 -> H^1(Z, O) -> H^1(Y, O) -> H^2(Z, B^{-1}) -> 0, hence q(Y) = q(X) + a(m-1); and q(Z) = q(X), h^{1,0}(Z) = h^{1,0}(X).
3. Betti numbers (input different from the run's Nakkajima-Yobuko): rank H^1_cris(V/W) = b_1(V) for smooth proper V (H^1_cris
   (x) Q is the Dieudonne module of Pic^0_red), and the l-adic Lefschetz hyperplane theorem (Artin vanishing on the affine
   Z - Y) gives H^1(Z, Q_l) = H^1(Y, Q_l). So b := b(Y) = b(Z).
4. For smooth proper V: H^1_cris is free (degree-0 universal coefficients), and h^1_dR(V) = b(V) + t(V) with
   t(V) = dim_k H^2_cris(V/W)[p]. The conjugate spectral sequence (Cartier) has E_2^{1,0} = H^1(V', O) with no differentials
   in or out, so h^1_dR >= q(V); the Hodge spectral sequence gives h^1_dR <= q(V) + h^{1,0}(V).
5. t(Y) - t(Z) = h^1_dR(Y) - h^1_dR(Z) >= q(Y) - q(Z) - h^{1,0}(Z) = a(m-1) - h^{1,0}(X) > 0.
6. For a finite W-module T, dim T[p] = dim T/pT is its least number of generators; t(V) is that number for T^2(V). A
   module cannot surject onto one needing more generators: (i).
7. (Input different from the run's.) u_2 is injective after (x) Q: followed by the Gysin map H^2_cris(Y) -> H^4_cris(Z) it is
   the cup product with c_1(B), an isomorphism H^2 -> H^4 by rational crystalline hard Lefschetz (Katz-Messing, transferred
   to algebraically closed k by spreading out). So im(u_2) meets T^2(Y) exactly in u_2(T^2(Z)), and the nonzero finite
   module T^2(Y)/u_2(T^2(Z)) injects into coker(u_2): (ii).
8. Existence of (X, A): Raynaud's surface (prop:OC-generated-Raynaud, checked in section 1: L ample, globally generated,
   H^1(S, L^{-1}) != 0) and a Kummer cover of degree q prime to p with L^q very ample (lem:OC-Kummer-very-ample, checked),
   which keeps H^1(S, L^{-1}) as a summand of H^1(X, A^{-1}). Any large q prime to p will do; the run's explicit exponent
   (p+1)^2 is not needed for existence.

Verdict: the statement is right; the failure is of the admitted integral form of weak Lefschetz for degree-one sections. It
does not touch the rational statements, and the run shows (thm:A-high-degree, outside my slice) that high degrees behave.
**Hexagon (H-candidate "integral weak Lefschetz fails"):** tests 1 and 4 are now met (targeted proof checks of the whole
chain, and this independent re-proof). Remaining gates: test 3 (a literature search: whether torsion growth of H^2_cris of
hyperplane sections from Kodaira non-vanishing is already in print; and whether a successor of RESEARCH_SA15 will extend it)
and test 2 (the cited constructions: Mukai 2011 Thm 1.2 and Zheng 2017 Prop. 2.2 are published; rational crystalline hard
Lefschetz and Lefschetz hyperplane are classical).

### 6.2 Group 1 of round 2: the other A sections (17 rows, all moved up)

All 17 rows of the other A sections that round 1 had left at statement level now carry a check event (events appended,
the read-only rows kept). One computation, sixteen targeted proof checks. What they establish:

- **The threefold counterexample chain (A_injectivity_counterexample.tex).** lem:OC-positive-Tango-iteration (Mukai's
  iteration re-derived at its identities: the eigensheaf formula, the normalization w^k = s^{k-2}, the new Tango function
  with T^k = S^2 - f, ampleness by Nakai-Moishezon, H^1_et unchanged), prop:OC-Tango-threefold (y^2 + y = x^843, g = 421,
  (dx) = 840 P_inf, D_1 = 21(10 N_0), D_2 = 10 L_2, D_3 = 2L, H^1(R, L^{-2}) != 0, dim H^1_et(R, Q_3) = 842).
  **lem:OC-threefold-negative-degrees (computation by hand): h^0(B) = 24, h^0(B^5) = 336, h^1(R, L^{-1}) = 360,
  h^1(R, L^{-2}) = 1, and the multiroot sum h^1(X, A^{-1}) = 360 + 843 = 1203 at d = 1, 1 at d = 2, 0 for d >= 3: all the run's
  numbers agree.** lem:OC-integral-first-lattice (Stein factorization and Riemann-Hurwitz force degree one; the isogeny of
  Picard varieties has odd kernel, so integral H^1_cris agree), lem:OC-explicit-differential-bound (h^0(Omega^1_S) <= 35, each
  summand <= 591), lem:OC-threefold-differential-degrees, lem:OC-threefold-multiroot (843 tuples; Betti numbers kept by Artin
  vanishing for j_!L_chi on an affine smooth threefold).
- **Where the admitted weak Lefschetz fails, and where it holds.** prop:OC-product-saturation-criterion: H^2_cris(Z) ->
  H^2_cris(Y) is **injective for every degree d** (H^1(K) = 0 for K = Omega_Z(log Y)(-Y), then the snake lemma and rational
  injectivity), and its cokernel is torsion-free under vanishing hypotheses that lem:OC-surface-uniform-negative-bounds
  verifies **for d >= p^2 - p** (characteristic two: d >= 2, d >= 3). So the failure of section 6.1 is a low-degree
  phenomenon; the statement "Tors(X) = Tors(Y), E(Y) torsion-free" holds for sections of high degree. This is consistent with
  thm:A-high-degree (outside my slice) and sharpens what a Hexagon note can say: "fails in degree one, holds for d >= p^2 - p
  on these products".
- **Supersingular and nonordinary surfaces (A_nonordinary, A_root sections).** lem:ss-rectangular-even-bound (Cartier
  multiplicative on closed forms, kills exact ones; rank bounds mn - 2 and mn - 3), lem:surface-frobenius-distributions (the
  invariant operators 1, d_1, d_2, d_1 d_2 of the K-torsor; stable rank = two-rank), prop:root-marked-normalization-inertia (the
  Lang scheme of H^1(C, O) is etale; inertia fixes H^1_et(Y, F_2)), lem:linear-covectors-any-nil-length (pole-order argument and
  induction on exponents), lem:root-nonordinary-Cartier-stability-candidate (a non-stable T gives a cubic curve E with
  Theta.E = 1, which splits the polarization: excluded for nonproducts; Rains-Sam 2.12, 3.1, 3.3 as background),
  lem:root-nonordinary-Coble-identification-candidate (h^0(I(2)) = 9 from Sym^2 H^0(3Theta) = 45 onto H^0(6Theta) = 36;
  Beauville's uniqueness of the Coble cubic as background), lem:root-nonordinary-nonproduct-three-neighbor-candidate (a
  maximal isotropic subgroup of A[3] other than E[3]; Cartier rank 1 of y^2 + y = f_5(x) versus 0 on a supersingular product),
  lem:root-nonordinary-three-theta-clean-boundary-candidate (determinant 3 of the map on triples, so etale in characteristic two;
  Theta.Theta = 2; (3Theta)^2 = 18).
- Nothing in group 1 was found false. Group 2 (C, D, F) had no rows left at statement level after round 1.

### 6.3 Group 3 of round 2: Part B (B.tex, 73 rows, all moved up)

Every row of B.tex that round 1 had left at statement level now has a check event (ev16-ev37 in my work folder): 17
computations (12 recomputations of my own, 5 reruns of the run's programs) and 56 targeted proof checks. Each event names
the lemmas outside my slice that the row uses as inputs (thm:B-RD12, B-RD26-wild, B-RD34, B-RD42, B-RD49, B-RD52, B-RD67
and the lemma families lem:B-RD31-*, B-RD37-*, B-RD46-*, B-RD49-*, B-RD60-break, B-RD64-weighted-kernel, B-RD69-rules,
B-RD69-quotients, B-RD71-*, B-RD87-*, B-RD94-terminal ...): those inputs were not re-proved here.

- **Dictionary and general bounds.** prop:B-RD4-dictionary (the convention check on Q_p/Z_p and mu_{p^inf}, slopes 1, 0
  against 0, -1); prop:B-RD20 (e_min(n) = 2*3^{2n-2}; e_min(2) = 18 although 6 and 12 pass the cyclotomic test);
  prop:B-RD24-finite-test (the decision procedure: discriminant bound, disc(psi_m) = c_m Delta^{N(N-1)/6}, the resultant
  Res(psi_m, 4f) = (-1)^{(m-1)/2} Delta^{N/2} recomputed for m = 3, 5 and the pointwise identity for m = 3, 5, 7, Hensel,
  elimination over F_p-bar); prop:B-RD25-basechange-obstruction (every valuation re-derived: 288 = 6*9 + 2*117, breaks 1052
  and 80, 87 is neither 27 nor 351).
- **p = 2, e = 1.** prop:B-RD22 recomputed exactly (P = (1+2zeta_3, ...) and Q = (3,6) of order 4 on y^2 = x(x-1)(x+3),
  Delta = 2^8 3^2, j = 2^4 13^3/9): M[4] does not determine the character. prop:B-RD44 (both groups potentially supersingular
  and elliptic, orders {1,2,4,8} against {3,6,24}), prop:B-RD44-realization, prop:B-RD46 (the four-torsion matrices
  I + 2A(sigma) checked on three Legendre parameters by exact radicals), prop:B-RD47, prop:B-RD48 (the root formulas
  A = -6ab, B = -2a^3-4b^3, Delta = -1728(a^3-2b^3)^2 by hand).
- **p = 3, e = 2.** prop:B-RD31-mixed, -32, -33 (graph closure is ker F^r x ker F^r), -35 (every remaining pair is a pair of
  elliptic curves), -37 (Fisher's nine-congruences; the two cube-deviation computations), -38 and -39 (recomputed: the Hesse
  family j(t), h(t) = (t+2)/(t-1), c_4 = 9t(t^3+8D), Delta = 27D(t^3-D)^3, both valuation tables entry by entry), -40
  (recomputed: det M = -3c, F_t(MX) = 3(1-t)F_{h(t)}(X), the Weierstrass coefficients), -41 (recomputed: Velu's quotient has
  j = 27t^3(9t^3-8D)^3/(D^3(t^3-D))). So after B-RD41 only the C_4 row (B-RD41.5) survives; its exclusion (thm:B-RD42) is
  outside my slice.
- **p >= 5 (e = p-1, p(p-1), 2N, (p+2)(p-1), ...).** B-RD49-mixed through B-RD97: the graph-closure and tame-projector
  arguments (B-RD50, B-RD64, B-RD77), the cycle of normalized types (B-RD53, recomputed for every p <= 47), the leading-
  coefficient ramification arguments (B-RD55, -56, -79, -80, -81, -97-two: every branch ends in "a fixed scalar equals
  Frobenius on F_q"), the break inequalities of B-RD60 through B-RD84 (each re-derived with s = e(p+1)), and at p = 5 the
  ramification tables recomputed by script: B-RD88 (lower breaks (6,336), (24,234)), B-RD90 (terminal lower breaks
  7896, 11646, 769146, 937896), B-RD93 (the coset-maximum equation has the unique solution M = 234), B-RD94 (exactly nine
  profiles; the lower-break formulas hold for each), B-RD95 (the nine V, W, T formulas reproduced symbolically), B-RD96
  (the second and third columns of its table), B-RD97-trace ((B-RD97.16) = pN(p-1)(p^3-p^2-1)).
- **The five scope remarks** (rem:B-RD49-, -50-, -51-, -52-, -100-scope) make claims about the run's programs. I copied the
  five programs unchanged into my work folder and reran them (python -I -B): all print status PASS with exactly the counts
  the remarks state (for example 8,243,000 logarithm inequalities, 292,614 character pairs, 5,296 arcs). This confirms the
  programs' outputs, not an independent program.
- Nothing in Part B was found false. One caution for the Hexagon register: the B.4 rows are a long chain of reductions whose
  inputs sit in the other two slices (in particular thm:B-RD12 and thm:B-RD42); no B.4 statement is a Hexagon candidate
  until that chain has been checked end to end.

### 6.4 Group 4 of round 2: A_monodromy.tex (158 rows, all moved up)

These rows build the characteristic-two monodromy of curves in linear systems on abelian surfaces (products of ordinary,
supersingular and mixed elliptic curves; nonordinary principally polarized surfaces; odd isogenies and their norm curves),
towards full GL images and irreducible Hasse divisors. Every row now has a check event (ev38-ev108): 3 independent re-proofs,
21 computations and 134 targeted proof checks. As in Part B, each event names the inputs it takes from outside my
slice (among them thm:product-char2-two-full-groups, thm:ss-uniform-GL8-block, thm:ss-all-odd-full-groups,
thm:ss-all-odd-Hasse, thm:ppav-three-theta-jets, thm:DE-A3-ppav-ranks, thm:ppav-non-two-torsion-cross-Cartier,
thm:odd-cover-full-hyperplane-inertia, thm:prime-Heisenberg-birational-radical, and lemma families such as the
labelled-transposition wreath lemma), and the run's certificates I did not rerun (the Groebner collision checks, the large
resultants and Bezout certificates of the 7/11/13 constructions).

Computations of my own (scripts in my work folder, all exact unless marked):
- Cartier matrices: the ordinary symmetrizer R M(s) (by hand, #406), the supersingular Hessian identity J M(s) = Hess(det S),
  M(s)s = 0 and grad Q = J s^[2] over F_2 (#627), the mixed identities over F_2(a, z) with the stable-loss test vector (#606),
  the type-(1,3) Euler matrix and its determinant c^2(1+t^3+u^3) (by hand, #334).
- Finite-field witnesses with my own F_64 and F_4096 arithmetic: the contact and tangent-triple data of #456, #457 (points, det S
  = 43, 55, 62, Q-values, ds, u(P)+u(Q) = 60, the kernel elements G, H), the orbit counts of #460, the thirteen-isogeny
  automorphisms of #486 (all relations (T13.12) consistent).
- Universal identities over F_2: #473 (det S = FTU, Q_H(S) is the Artin-Schreier relation, M(s)vec(SR^tS) = det(S)s^[2] mod Q_H),
  #599 (Pfaffians and the birational inverse for m = 2, 3, 4), #323 (Schur complement), #483/#484 (the 7-construction identities,
  irreducible factors of B(r) of degree 97, the gcd z^3+z^2+1), #479/#488 (D_12 H_4 = V^16+V, D_12^5+H_4^12 = sum V^{3i}), #376 (the
  degree-32 irreducible nonreciprocal certificate polynomial).
- Recounts that reproduce the run's numbers exactly: the Coble polar minors det = 1 (two-rank 0) and det = b^4 (two-rank 1) by my
  own 81x81 elimination (#414, #413); the Moore determinant (55,296 monomials, 2,080 coefficients, 400 excluded and 111 surviving
  supports, #321); the Heisenberg Pfaffian supports for p = 5, 7, 11, 13, 17 (for p = 17: 1,465,345 terms, 43,263 coefficients,
  255 witnesses, #614).
- Random-point tests over F_4096 (probabilistic, so labelled): det C(T) = det(T)^3 (#463) and the binary nonic (TAS4) (#464),
  300 points each.
- Re-proofs: lem:char2-genus-two-three-total-ramifications-candidate (both cases; the S_3-case Cartier matrix H and (det H)^2 =
  ab+c = F(sqrt b)), lem:root-nonordinary-odd-theta-nodality, lem:prime-Severi-Brauer-diagonal-trace (Fermat's little theorem on
  the p diagonal coefficients).

Nothing in group 4 was found false. Two points for the record: lem:ppav-nonordinary-strata-candidate states two corrections to
Ekedahl-van der Geer 2009 (the degree-one wording of Example 12.2 for all four strata, and the semisimple-rank expression in
Example 3.4); I did not reopen that source, so these stand as the run's claims. And lem:principal-theta-addition-perfect corrects
a sentence in the proof of Lemma 8.31 of Edixhoven-van der Geer-Moonen (geometric characters do not span O(K) for local-local K);
the replacement Hopf-ideal argument is correct as written.

### 6.5 Final state of part 2 (both rounds)

- Every one of the 318 ids has a check event above statement level. Best level per id: **independent re-proof 20, computation or
  formal certificate 48, targeted proof check 238, carried as background without fault found 12**. The TSV has 567 rows: the 318
  round-1 rows (including the 248 "statement read only" rows, kept as instructed) and 249 round-2 events (re-proof 4, computation
  39, targeted 206). No row is refuted.
- **Refutations:** none in my slice. The run's own refutations that fall in it were confirmed (prop:B-RD4, Lead B' false as
  stated; prop:DE-old-proper and prop:DE-old-site, Grothendieck's tests (a), (b) of 7:19; prop:root-f1-bad-five-kernel).
- **Hexagon (field_experts/HEXAGON_CANDIDATES.md):** one candidate, "Grothendieck's admitted integral weak Lefschetz fails"
  (prop:OC-product-integral-counterexample with its chain). Tests 1 and 4 are met (complete chain checked; independent re-proof in
  6.1; the threefold numbers recomputed in 6.2). Gates left: test 3 (literature search on torsion growth of H^2_cris of
  hyperplane sections from Kodaira non-vanishing; stability against a successor run) and test 2 (published locators for the
  inputs). Its sharpened form: the admitted statement fails in degree one and holds for d >= p^2-p on these products. A possible
  minor note, not yet a candidate: lem:char2-genus-two-three-total-ramifications-candidate (a genus-two curve in characteristic two
  with a trigonal map having three total ramification points is ordinary) is complete, self-contained and re-proved here; gates: a
  literature search (it may be known) and a judgement of interest. Part B and A_monodromy are long chains whose key theorems lie in
  the other two slices (thm:B-RD12, thm:B-RD42 and the GL-image theorems); nothing there is a candidate before those are checked.
- Scripts (work folder `a8d07e78_intake/` in the session scratchpad): chk_BRD22, chk_BRD24, chk_BRD38_39, chk_BRD40_41, chk_BRD46,
  chk_BRD53, chk_BRD88_90, chk_BRD93_94, chk_BRD95, chk_ssHasse, chk_F64, chk_F64_orbits, chk_uniform_contact, chk_mixed,
  chk_coble_minor, chk_seven, chk_F4096, chk_pfaff, chk_cross_det, chk_moore, chk_moore2, chk_heis (with chk_heis_17.out), and
  rerun/ (the run's five programs, copied unchanged). All run with python -I -B outside the return.
