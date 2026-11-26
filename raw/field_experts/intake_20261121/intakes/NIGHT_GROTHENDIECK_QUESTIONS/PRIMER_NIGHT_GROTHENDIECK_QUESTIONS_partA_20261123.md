# Primer: NIGHT_GROTHENDIECK_QUESTIONS, Part A (cotes 15, 123, 133), as of checkpoint 13 (24 Nov 2026, 00:37 UTC)

By agent a0805369bae2ebddc (Claude Opus 5.5 at effort high), for the main session to read after a compaction. It
restates; it does not develop. Run: prompt 76, GPT-6 Astra (ChatGPT Pro mode), effort not exposed. Return:
`research_returns\NIGHT_GROTHENDIECK_QUESTIONS_checkpoint_13_20261124T0037Z_unzipped`; papers under `papers\`.
- Only Part A is active; Parts B and C had not started by cp13.
- Since cp04 only A133 changed (now 111 pages); A15 and A123 are byte-identical.
- The cp04 version of this primer is in `integration_backups\20261123\NIGHT_GROTHENDIECK_QUESTIONS\`.

**Check labels**, from the intakes `..._20261123_cp04_partA.md` and `..._20261124_cp13_partA.md`:
- `[TPC]`: targeted proof check;
- `[COMP]`: our computation;
- `[stmt]`: statement level.

## Cote 133: which coefficient rings make symmetric-group lattices polynomial (`papers\A133_lattices`)

**The question.** Scan 29, ms p. 28: for which k is R(k) = ⊕_n K_0(Lat_k(S_n)), with induction product, the polynomial
ring ℤ[ρ_1, ρ_2, …] on the trivial classes? Is a local ring enough, or more generally K_0(k) = ℤ? Here Lat means
modules finite free over k, with all coefficient-split short exact sequences. Φ_A is the comparison map from the
polynomial ring.

**Answer as of cp13.** Characteristic 0 is necessary, and locality is not enough. In the curvilinear case the answer
is: generation holds iff the ring is regular.

### Main result (new at cp13): Thm 26.1, Cor. 26.3, Thm 27.1 and Cor. 27.3

**Thm 26.1** `[TPC lines 1-600]` `[COMP]` (`singular_distinguished_monic.tex`; NGQ-A133-051, -054).
- **Statement.** Let O be a characteristic-0 DVR with v_O(p) = 1; the residue field is arbitrary and O need not be
  complete. Let F = tⁿ + Σa_i tⁱ with n ≥ 2, every a_i ∈ pO and a₀ ∈ p²O, and A = O[t]/(F). Let r be the least i ≥ 1
  with a_i ∉ p²O, and N = min(n, pr) (N = n if there is none). Then for G = C_p and G = S_p, K₀(Lat_A(G)) has a split
  subgroup ⊕_ℕ ℤ/N. It lies in the kernel of extension to A[1/p], and its retraction kills every Young permutation
  lattice. So Φ_A is not surjective in degree p.
- **Mechanism, step by step.** Write g(X) = (1+X)^p − 1, with X = σ − 1.
  1. **The root.** For a unit c, a finite recursion gives α_c ∈ D[t] of degree < N with g(α_c) + cF = t^N U_c.
     - Every division by p is integral: a_i ∈ p² below r, and the residual part has t-order r, so its p-th power
       starts at pr ≥ N.
     - Let β = a_r/p. The residue of U_c(0) is c̄ if n < pr, (−c̄β̄)^p if pr < n, and c̄ + (−c̄β̄)^p if n = pr. The
       c_j are chosen so that it is nonzero.
  2. **The lattices.** The factorization [[X − α_c, tⁱ], [−U_c t^{N−i}, h_c]] of g + cF gives lattices M_i for
     0 ≤ i ≤ N. Each is free of rank p on the basis e, f, …, X^{p−2}f, and its X-operator has characteristic
     polynomial g + cF.
  3. **The relations.** M_0 ≅ M_N ≅ A[C_p]. The coefficient-split mesh sequences M_i → M_{i−1} ⊕ M_{i+1} → M_i,
     with maps diag(t, I) and diag(1, tI), give x_i = i·x_1 and N·x_1 = 0.
  4. **The generic fibre.** M_i[1/p] is free, because Z^p − 1 is separable.
  5. **The detector.** Supported length: for T complete regular local of dimension 2 and S = T[t]/(t^N), the length
     map K₀(D^b_Z(S)/Perf_Z(S)) → ℤ/N exists. The reasons are that Res ≃ N·G at the spectrum level (by the
     filtration by t^a S) and that K₋₁ = 0.
  6. **The evaluation.** Burke-Walker's generic-hypersurface equivalence and the root section X = α(z, t) at the
     chart z = c_j carry M_i to the ideal (p, tⁱ) ⊂ D̂[[w,t]]/(t^N). Its value is i mod N.
  7. **The splitting.** Points c_j with pairwise distinct free F_p^×-orbits give the coordinates. The Mackey sum for
     S_p contributes only the identity label.
- **External inputs,** taken at the run's locators and not opened by us:
  - Blumberg-Gepner-Tabuada, Thm 9.8 and 9.33-9.34;
  - Antieau-Gepner-Heller, Thm 1.1;
  - Orlov 2011, Lemmas 2.1, 2.5 and 2.6;
  - Burke-Walker 2012, Thm 2.10, Rem. 3.19, Cor. 3.18 and 3.20.

**Cor. 26.3** `[TPC]`. For F ≡ tⁿ mod p, these are equivalent: Φ_A is an isomorphism; Φ_A is surjective; A is regular;
a₀ ∈ pO∖p²O.
- If a₀ ∈ pO∖p²O, F is Eisenstein and A is a DVR, which is positive by the regular-local theorem.
- If a₀ ∈ p²O, then F ∈ (p,t)², so A is singular and Thm 26.1 applies.

**Cor. 26.4** `[TPC]`. If F̂ is irreducible, then N = n: the bound v(a_i) ≥ (n−i)ν/n forces r ≥ n/2.

**Thm 27.1 and Cor. 27.3** `[stmt]` (`curvilinear_special_fiber.tex`; NGQ-A133-055, -059).
- **Statement.** Let A be finite free and local over any mixed-characteristic DVR, or complete and p-torsion-free with
  A/pA Artinian. Suppose edim(A/pA) ≤ 1. Then Φ_A is an isomorphism iff A is regular, and a singular A has the split
  ⊕_ℕ ℤ/N in the generic kernel.
- **The reduction.** A Cohen ring O ⊂ Â with uniformizer p presents Â = O[t]/(F), F ≡ tⁿ mod p. Then Thm 25.1 and
  Thm 26.1 apply.
- **Scope.** It covers every monogenic local algebra over an unramified DVR, inseparable residue extensions included.

### Other results (new at cp13, `[stmt]` unless marked)

- **All truncations fail.** O[t]/(tⁿ) fails for every n ≥ 2, over every characteristic-0 DVR.
  - Over Z_p and Z_(p) there is a split countable ℤ/n (Thm 13.1, `all_truncations.tex`, NGQ-A133-033). Its generator
    satisfies T^p = I `[COMP]`.
  - For p ∤ n, over any DVR, there is an exact order-n class (Thm 18.1, NGQ-A133-047; mesh lemma and surface lemma
    `[TPC]`). The detector is the divisor class of (X, t) on the normal surface O[[X,t]]/(g(X) + tⁿ), where
    div(X) = n·(X, t).
  - For p | n there is a vertical-ideal class of value n/p (Thm 19.1; exact order p, Thm 19.7).
- **Odd ramified dual numbers fail** (Cor. 18.8, NGQ-A133-046). Every DVR of odd residue characteristic has an exact
  order-2 class. The cp04 parity detector vanishes when v₂(e) > v₂(p−1) (Thm 17.1); that is a limit of that invariant
  only.
- **Quadratic orders.** A Z_p-order in a quadratic field is polynomial iff it is maximal, at every prime (Thm 23.1).
- **Residue degree.** A distinguished monogenic order whose generic field has residue degree f > 1 has a ⊕ℤ/f quotient
  of its generic kernel (Thm 30.1).
- **Congruent coefficients.** Over Z_p, algebras congruent mod p^r with r > 2v_p|G| have the same lattice K₀,
  compatibly with the operations (Thm 24.1).
- **Completion.** Over any characteristic-0 DVR, completion is injective on lattice K₀ and identifies the generic
  kernels; split subgroups lift (Thm 25.1).
- **Monic families** (F ≡ tⁿ mod p² or p³, shallow top coefficient; Thms 25.5, 28.x, 29.x): mostly subsumed by
  Thm 26.1.

### Results from cp04, still standing

- **Characteristic 0 is necessary** `[TPC]` (`positive_characteristic.tex`). If m·1 = 0, then P_m(ρ_1..ρ_m) = 0. The
  proof uses the Koszul relation H(t)E(−t) = 1 and ∑(−1)ⁱ[ΛⁱV] = 0 for V = ker(sum).
- **Flat dual numbers ℤ_(p)[ε]/ε²** `[TPC]` `[COMP]` (`dual_numbers*.tex`). There is a nonzero class
  [Ind_{C_p}^{S_p} L_p] − [A[S_p]], detected by a mod-2 Tate-boundary parity. The lattice is T = [[1, εa], [εb, C]],
  where C is the companion of Φ_p.
- **Square-zero extensions** `[TPC part]` (`arbitrary_idealizations.tex`). ℤ_(p) ⋉ M is polynomial iff M is a
  ℚ-vector space.
- **The positive side** `[stmt]`. Coherent regular local rings of characteristic 0 and local ℚ-algebras are
  polynomial, and Φ is split injective in characteristic 0. On scan 28, the tensor-power formula holds integrally.

### Open rows at cp13, with their gates

- **A133-classification:** singular rings with edim(A/pA) ≥ 2 (non-monogenic orders).
- **A133-normal-singular:** normal two-dimensional counterexamples exist at every prime, but there is no intrinsic
  criterion.
- **Arbitrary-DVR kernel refinements:** the exact orders and splittings over ramified DVRs.

## Cote 15: minimal field of definition of an isogeny class (`papers\A15_finite_fields`)

- **Prop. 5.2, central CM formula `[TPC]`** (`central_cm.tex`).
  - Statement: let D be the geometric endomorphism division algebra, of degree d over a CM field K, with slopes λ_v.
    Put a = lcm den(e_vλ_v), I = ∏𝔭_v^{a e_v λ_v}, t = ord[I] in Cl(K), and s ∈ {1, 2} the order of u = ηη̄/p^{at}
    in the totally positive units of K⁺ modulo norms. Then the central-Frobenius model exponents are exactly the
    multiples of a·t·s. This is the minimum over all models when D = K.
  - Mechanism: slopes force a | n; the ideal of β is I^m, so t | m; the Weil condition is u^r N(ε) = 1. Conversely
    Honda-Tate and equal powers give the model.
  - Example: the ARCH_ALG threefold over ℚ(√−23) gives a = 3, t = 3, s = 1, so n = 9.
- **Thm 1.1:** the threefold has no model over F₈, and exponents are exactly the multiples of 9 (checked in the
  ARCH_ALG intake on the lines read). The Chow constructions are at `[stmt]`.
- **Open:** a noncentral Frobenius in a noncommutative D, and a sharp unrestricted bound.

## Cote 123: the letter to Kostant (`papers\A123_tori`)

- **Thm 1.1 `[stmt]`, inherited:** |W|²/(hzφ(h)) classes; every choice is opposite exactly in A_{p−1}, B₂, G₂;
  Out-fixed classes exist exactly outside A_{2m}.
- **Prop. 6.1:** the type-A fixed-class count; my count agrees for n ≤ 9.
- **Thm 1.2 `[stmt]`:** natural rules under isomorphisms are the Out-fixed classes, and central isogenies add no
  selection.
- **Prop. 7.1 `[stmt]`:** in A₃, 16 of 18 classes are opposite, including all 8 fixed ones.
- **Prop. 7.2 `[TPC]`:** a split PGL_n quadruple over k exists iff ζ_n ∈ k, by the Fourier cross-ratio. So no
  split-real choice of a distinguished class is possible.
- **Prop. 9.1 `[stmt]`:** symplectic folding leaves (2^m m!)²/(2nφ(n)) classes, 4 for n = 4.
- **Thm 8.1:** the subregular rank is r − 1 (known: Richardson 1987, Lemma 5.1, after Slodowy).
- **Open:** a geometrically preferred class (A123-natural).

## Where it went

- `results_register\horizontal\sweep3\SA17\STUDY.md` (the scan 29 entry), edited.
- Board rows and seed pointers: for the main session (intake §5, §7).
- cp13 (24 Nov): the same STUDY.md block gained "Further answers at cp13". The board edits (replace A133a, add A133b)
  are for the main session (cp13 intake, section 5).

## The Thakur correction (A15)

Thakur, arXiv:2001.00210v1, Prop. 2.9 (a model over F_{p^h}) fails for ℚ(√−23), p = 2, d = 3: there is no model over
F₈, and the model field is F_{2⁹}. The proof's π₀ with (π₀) = 𝔭^h gives an ordinary elliptic curve.
- **The corrected statement:** the central models are exactly those over F_{pⁿ} with n₀ = dt/gcd(t, 2j−d) dividing n.
  So there is always a model over F_{p^{dh}}.
- **A non-central Frobenius can do better:** for ℚ(i), p = 5, d = 3 there is a model over F₅. So no bound in h alone
  is right in general.
- **The draft:** `EMAIL_DRAFT_Thakur_20261123.md`. It holds at cp13 and awaits the run's final and the user's yes.
