# Consult: the counting construction, and whether the rank-three realizations compose

By agent a157422a (Claude Fable 5.2 at effort max), for the main session (Claude Opus 5.5 at effort max).
Written 21 Nov 2026, 19:06 UTC.

**Read for this:** `SPLIT_ZERO_IN_CONNES_CONSANI_TERMS_20261121.md` (whole); `consults\E4_RANK_FOUR_20261121.md` (whole);
`consults\E4_scripts\e3_constants.json` (all 132 rows, by script). Nothing else was opened.

**Scripts** (beside this file; run with `python -I -B`):
- `consult_a157422a_counting_checks.py`: the closed formulas of Theorem 2 against the 132 stored constants;
- `consult_a157422a_dimension_ring_search.py`: the search of section 4.4;
- `consult_a157422a_dimension_ring_verify.py`: the full check of the dimension ring of Theorem 7;
- `consult_a157422a_dimension_ring_unimodal.py`: the search behind Theorem 7′.

**Status marks:** [proved here]; [computed] with the script named; [standard] (cited from memory, no paper opened);
[rests on A]; [open]. A is Alpöge's RH and GRH for Dirichlet L-functions; I have not read it.

**Notation.** v, q = v², t = v − v⁻¹, D = (v + v⁻¹)² = q + 2 + q⁻¹ = t² + 4. T_s is the normalized generator,
(T_s − v)(T_s + v⁻¹) = 0; C′_s = T_s + v⁻¹, C_s = T_s − v; P_s = C′_s⊗C′_s + C_s⊗C_s. The basis E^opp(3) is Σ, γ¹_x, γ²_x
(x ∈ {1, 12, 2, 21}) and μ = 1, as in the E4 file. 𝔸 = Z[q^±][ε]/(ε² − 1).

## Summary

1. **The open step has a positive answer, but not for the realizations of the E4 file.** There is a monoidal category
   of sign-twisted Tate objects whose Grothendieck ring is free over 𝔸 on E^opp(3) and becomes Ȟ₃ with its 132
   structure constants at ε = −1 (Theorem 7, explicit, verified on all 1000 triples). It can be chosen with all 132
   dimension polynomials symmetric and unimodal (Theorem 7′). The realizations of E4 §7 do not compose: their dimensions violate associativity on the triple (γ¹₁, γ¹₁, Σ) (Proposition 5).
2. **Why:** the two cells have opposite signs, δ₁ = −δ₂, and that sign cannot stay inside its cell. In every composing
   realization the bottom cell Σ carries cancelling pairs (Proposition 6). Each cancelling pair is the class 1 + ε:
   two conjugate points, globally the zeta function of Z[i].
3. **Ȟ₃ in closed form.** All 132 constants are explicit polynomials in D (Theorem 2, 0 mismatches against the stored
   table). This explains the E4 tables: a is even, f is bar-invariant of Tate type with even weights, the count is
   132 = 19 + 1 + 16 + 32 + 32 + 32, and the six failures are the one value (D − 4)(D − 1)(D − 2)².
4. **The ground ring is Z[D] at every rank** (Theorem 1). So at rank four, for any basis of Q(D)-combinations of
   P-words, every structure constant has even a and even-weight Tate type, before E(4) is computed.
5. **Counting.** c ↦ Z_c is a ring homomorphism to a Witt-type ring of Euler products in which ζ is the unit; the
   bar involution is s ↦ 1 − s; with the sign it is multiplicative over Z[1/2] (Theorem 4). The supported zero e of
   G(Z) is the class of two conjugate points.
6. **What A adds** is the location of the zeros of every such zeta. What decides the nonstandard question at a
   given rank is the existence of a dimension ring; at rank three it exists.

---

## 1. The ground ring, and Ȟ₃ in closed form

**Theorem 1 (ground ring, all ranks) [proved here].**
(a) H_r has integral structure constants in Z[t] in the basis T_w. So σ (identity on the T_w, v ↦ −v⁻¹ on scalars) and
    β (T_w ↦ (−1)^{ℓ(w)}T_w, v ↦ −v) are ring automorphisms of H_r; σ(C′_s) = C_s and β(C′_s) = −C′_s, β(C_s) = −C_s.
(b) P_s = 2T_s⊗T_s − t(T_s⊗1 + 1⊗T_s) + t² + 2, and P_s is fixed by σ⊗σ and β⊗β.
(c) These generate a group Γ ≅ (Z/2)² acting on H_r⊗H_r semilinearly over Gal(Q(v)/Q(D)). The Q(D)-span of the
    P-words is a Q(D)-form of Ȟ_r. In any basis of Q(D)-combinations of P-words the structure constants lie in
    Q(D); in Z[D] if the basis and the relations are integral, as at r = 3.
(d) Z[D] = Z[q + q⁻¹] is the ring of bar-invariant Laurent polynomials in q. So such a constant is of Tate type with
    even weights, is bar-invariant, and vanishes to even order at v = 1: in VIII's form ±(v − v⁻¹)^a f, a is even.
Proof. (a) T_s² = tT_s + 1 and the braid relations have coefficients in Z[t]; t is fixed by v ↦ −v⁻¹ and negated by
v ↦ −v, and the braid relations are homogeneous in length. (b) Expand; the three terms are fixed by both maps.
(c) The module of linear relations among the P-words is stable under Γ, so by Galois descent it is spanned by
relations with coefficients in the fixed field Q(v)^Γ = Q(D). (d) A function of D is a function of t² = D − 4. ∎

σ is v ↦ −v⁻¹, the map Koszul duality induces on Grothendieck groups; β is the parity twist v ↦ −v, the sign ε. So
P_s is the sum of the Kazhdan–Lusztig element of (s, s) and its image under σ⊗σ. [reading]

**Theorem 2 (rank three in closed form) [proved here; computed: `consult_a157422a_counting_checks.py`, 132 of 132].**
Put λ₁ = D, λ₂ = (D − 2)², δ_i = λ_i − λ_{3−i}, so δ₂ = −δ₁ = (D − 1)(D − 4) = [3]_v·t².
(a) Ȟ₃ = ⟨P₁, P₂ | P_i² = D·P_i, P₁(P₂P₁ − λ₁)(P₂P₁ − λ₂) = P₂(P₁P₂ − λ₁)(P₁P₂ − λ₂)⟩. Its representations are: the
    trivial one θ (P_i ↦ D), the zero one (P_i ↦ 0), and two of dimension two, ρ₁ and ρ₂, with P₁P₂P₁ = λ_iP₁.
(b) Σ is the common value of the two sides of the relation, and γ^i_x = P_x(P_{yx} − λ_{3−i}). γ^i vanishes on ρ_{3−i}
    and acts on ρ_i as δ_i·P_x.
(c) For words x, y let P_xP_y = D^α λ^β P_z in a two-dimensional block (β ∈ {0, 1}). Then
    - γ^i_x γ^i_y = δ_i D^α λ_i^β · γ^i_z + D^{|z|+α−1} K^i_β · Σ, with K^i_0 = 1 and K^i_1 = D² + δ_i
      (K¹₁ = 5D − 4, K²₁ = 2D² − 5D + 4);
    - γ^i_x γ^j_y = D^{|x|+|y|−1} · Σ for i ≠ j;
    - Σ γ^i_x = γ^i_x Σ = D^{|x|}(D² − λ_{3−i}) · Σ, that is 4D^{|x|}(D − 1) for i = 1 and D^{|x|+1}(D − 1) for i = 2;
    - Σ² = D(D² − λ₁)(D² − λ₂) · Σ = 4D²(D − 1)² · Σ.
Proof. In ρ_λ, P₁ = [[D, a], [0, 0]], P₂ = [[0, 0], [a, D]], a² = λ; this gives (a), (b) and the first coefficient of
(c). The coefficient of Σ is found by applying θ, since θ(Σ) ≠ 0 and Σ acts by zero elsewhere. ∎

**What it explains in the E4 tables.**
- 132 = 19 (unit) + 1 (Σ²) + 16 (Σγ, γΣ) + 32 (γ^iγ^j, i ≠ j) + 32 (within cells) + 32 (their Σ-parts).
- The 32 constants with a = 2 are the within-cell ones, 16 with sign − (cell 1, δ₁) and 16 with sign + (cell 2).
- Positivity of all f is the positivity of five Laurent polynomials: D, D − 1, D − 2, 5D − 4, 2D² − 5D + 4.
- The six failures are the within-cell constants of cell 2 with β = 1 and α = 0: δ₂λ₂ = (D − 4)(D − 1)(D − 2)².
- The non-cyclotomic parts 5q² + 6q + 5 and (q² + q + 2)(2q² + q + 1) of E4 §7 are K¹₁ and K²₁.

**Theorem 3 (group-like form) [proved here].** ς_s = (T_s + T_s⁻¹)/(v + v⁻¹) is an involution of H_r, and
P_s = (D/2)(1 + ς_s⊗ς_s). So Ȟ_r⊗Q(v) is the linear span of the group generated by the involutions u_i = ς_i⊗ς_i.
For r = 3 it is the quotient of the group algebra of the infinite dihedral group in which the rotation
ρ = u₁u₂ satisfies (ρ − 1)(ρ² − (z + z⁻¹)ρ + 1)(ρ² − (z² + z⁻²)ρ + 1) = 0, z + z⁻¹ = −2(D − 2)/D. The two angles are
tied: cos²θ₁ = 1/D and θ₂ = π − 2θ₁. At D = (1 + √5)², z is a primitive fifth root of unity and Ȟ₃ is the group
algebra of the dihedral group of order 10.
Proof. (2T_s − t)² = 4(tT_s + 1) − 4tT_s + t² = D. The projections P_i/D have angle cos²θ = λ/D² in ρ_λ, and
4λ₂/D² − 2 = (2(D − 2)/D)² − 2. ∎
In sheaf terms T_s and T_s⁻¹ are the classes of j_! and j_* on P¹, so ς_s = ([j_!] + [j_*])/[2], and their difference
[j_!] − [j_*] = t·[δ] is the boundary defect with t = v⁻¹·#G_m(F_q). [reading; the dictionary is standard]

## 2. Counting with the basepoint

**Theorem 4 [proved here; the Witt-ring statement is standard: Ramachandran 2015].**
(a) For c = Σ_j a_j q^j ∈ Z[q^±] put Z_c(s) = Π_j ζ(s − j)^{a_j}. Then c ↦ Z_c is an isomorphism from (Z[q^±], +, ·)
    onto the ring of such products, with addition the product of functions and multiplication ⋆ determined by
    ζ(s − j) ⋆ ζ(s − k) = ζ(s − j − k). The unit is Z₁ = ζ. For X of finite type over Z with X₊ = X ⊔ Spec Z:
    Z_{X₊} = Z_X · ζ.
(b) c is bar-invariant iff the completed product Π ξ(s − j)^{a_j} is invariant under s ↦ 1 − s.
(c) [rests on A] Every nontrivial zero of Z_c lies on a line Re s = j + ½ with a_j ≠ 0. For the words P₁^k acting on
    the tensor module, Z_k = Π_{a=−k}^{k} ζ(s − a)^{40·C(2k, k+a)}. By Theorem 1 every structure constant of Ȟ_r in a
    Q(D)-rational basis has a zeta of this kind with a functional equation.
(d) For ĉ = Σ_j (a_j⁺ + ε a_j⁻) q^j ∈ 𝔸 put Ẑ_ĉ(s) = Π_j ζ(s − j)^{a_j⁺} L(s − j, χ₋₄)^{a_j⁻}. Its local factor at an odd
    prime p is the zeta function of the count N_n = Σ_j (a_j⁺ + χ₋₄(p)^n a_j⁻) p^{nj}. Over Z[1/2] (Euler factors at odd
    primes) ĉ ↦ Ẑ_ĉ is a ring homomorphism for ⋆. At p = 2 it is additive only: ε² = 1 fails there, because
    L(s, χ₋₄)⋆L(s, χ₋₄) is the L-function of the principal character mod 4.
(e) **Reading the object from its zeta [rests on A for the location on the lines].** In the completed product
    (ξ and the completed L in place of ζ and L) the pole at s = j + 1 has order a_j⁺ + a_{j+1}⁺, so the pole orders
    determine the a_j⁺ by a triangular system. The number of zeros on Re s = j + ½ up to height T is
    (a_j⁺ + a_j⁻)(T/2π) log T (1 + o(1)). So the dimension a_j⁺ + a_j⁻ is a zero density, and the trace follows from
    it and the pole orders. ĉ is effective iff Ẑ_ĉ has no pole at a nontrivial zero of a factor ζ(s − j) or
    L(s − j, χ₋₄); the first zeros of ζ and of L(s, χ₋₄) differ, so a negative exponent cannot be hidden.
(f) **Split and inert primes.** At p ≡ 1 mod 4 the count is the dimension polynomial d = a⁺ + a⁻ at p^n. At p ≡ 3 mod 4
    it is the trace polynomial c = a⁺ − a⁻ for n odd and d for n even.
Proof. (a) is the Euler product; ⋆ is the Witt product, which is the product of varieties. (b) ξ(1 − s − j) = ξ(s + j).
(d) χ₋₄(p)^n is the trace of the n-th power of Frobenius on ε. (e) ξ(s − j) has simple poles at s = j and s = j + 1 and the completed L is entire; ζ and L(s, χ₋₄) each
have (T/2π) log T zeros up to height T. ∎

**Proposition 4′ (the supported zero) [proved here].** N[ε]/(ε² − 1) → G(Z), a⁺ + εa⁻ ↦ a⁺ − a⁻ for (a⁺, a⁻) ≠ 0 and
0 ↦ τ, is a surjective semiring homomorphism. The supported zero e = 0_Z is the image of the nonzero classes of
trace 0, the multiples of 1 + ε. Over F_p, p ≡ 3 mod 4, 1 + ε is Spec F_{p²}: two conjugate points, not empty, with no
F_p-point. Globally it is Spec Z[i], with zeta ζ(s)L(s, χ₋₄) = ζ_{Q(i)}(s), and τ is the empty scheme.
Proof. The trace is a ring homomorphism, and a product in N[ε] is zero only if a factor is. ∎

So the pair (trace, dimension) refines (value, support): d ≥ |c|, d ≡ c mod 2, and a supported zero is c = 0 < d.

## 3. The categorification question, stated exactly

Sign-twisted Tate objects are graded super vector spaces with parity ε; their category 𝒯_ε is semisimple with simple
objects L^jε^k, and K₀(𝒯_ε) = 𝔸 ⊂ Z[q^±]², ĉ ↦ (d, c) = (ε ↦ 1, ε ↦ −1), with image the pairs congruent mod 2.

**Theorem 5 (criterion) [proved here].** The following are equivalent for (Ȟ₃, E^opp(3)), and for any based ring:
(i) there is a monoidal category, linear over 𝒯_ε, with objects b̂ (b in the basis) and b̂⊗b̂′ ≅ ⊕ M(b, b′; b″)⊗b̂″,
    whose Grothendieck ring is free over 𝔸 on the b̂ and specializes at ε = −1 to the given ring with its constants;
(ii) the constants lift to effective elements ĉ ∈ N[q^±] ⊕ N[q^±]ε satisfying associativity in 𝔸;
(iii) there is a **dimension ring**: an associative unital structure d(b, b′; b″) ∈ N[q^±] on the same basis with
     d ≥ |c| coefficientwise and d ≡ c mod 2.
Proof. (ii) ⟺ (iii) is the embedding 𝔸 ⊂ Z[q^±]². (i) ⟹ (ii) by taking classes. (ii) ⟹ (i): the left regular
representation b ↦ L̂_b is faithful with effective entries. In the monoidal category Mat_n(𝒯_ε) of n × n matrices of
objects (n the rank), let b̂ be the matrix of objects M(b, b′; b″). Objects of Mat_n(𝒯_ε) are determined by their
classes, so b̂⊗b̂′ ≅ ⊕ M(b, b′; e)⊗ê; the unit is the identity matrix and associativity is inherited. ∎

**Cells lift at once [proved here].** The cell algebra with γ_xγ_y = δ D^α Λ^β γ_z is associative for all values of
(D, Λ, δ). With t̂² = q + 2ε + q⁻¹ (dimension D, trace D − 4), â₂ = q + (1 + ε) + q⁻¹ and the sign − lifted to ε, the
within-cell constants ε·t̂²[3]D^{α+β} (cell 1) and t̂²[3]D^α â₂^{2β} (cell 2) are effective. The question is only the
gluing to Σ, that is the lift of the trivial representation θ.

**Where the functorial lift fails [proved here].** Lifting λ₂ = a₂² to â₂² turns θ(γ¹_x) = D^{|x|}(D² − λ₂) into
D^{|x|}(D − 1)(2 − 2ε): a virtual object of dimension 0 and trace 4D^{|x|}(D − 1). The number 4 in the bottom cell is
(1 − ε)² at ε = −1, and (1 − ε)² is not effective.

**Proposition 5 (the realizations of E4 §7 do not compose) [proved here].** E4 realizes the constants with a = 0 in
the bottom cell split (dimensions = traces): θ(γ¹₁) = 4D(D − 1), θ(Σ) = 4D²(D − 1)², c(γ¹₁, γ¹₁; Σ) = D; and it realizes
c(γ¹₁, γ¹₁; γ¹₁) = −t²[3]_v[2]_v² with dimensions D·(D − 1)·D. With these dimensions,
  (γ¹₁γ¹₁)Σ = 8D³(D − 1)²·Σ and γ¹₁(γ¹₁Σ) = 16D²(D − 1)²·Σ,
which differ by 8D²(D − 1)²(D − 2). So the dimension counts of E4's realizations are not associative.

**Proposition 6 (the bottom cell cannot be split) [proved here].** In every dimension ring for (Ȟ₃, E^opp(3)), of
any shape, at least one of d(Σ, γ¹₁; Σ), d(Σ, Σ; Σ), d(γ¹₁, γ¹₁; Σ) is strictly larger than the true constant.
Proof. If all three equal the true values g, s, κ, associativity on (γ¹₁, γ¹₁, Σ) gives
Σ_b d(γ¹₁, γ¹₁; b)·d(b, Σ; Σ) = g² − κs, summed over b ≠ Σ. The right side is the true value δ₁D·g, which is negative
at every real q > 1 since δ₁ = −(D − 1)(D − 4). The left side is a sum of products of Laurent polynomials with
nonnegative coefficients. ∎
So the sign of cell 1 forces cancelling pairs 1 + ε in the bottom cell: supported zeros that no single structure
constant shows.

## 4. The construction

**4.1 The shape.** Keep the support of the multiplication table. At ε = +1 the unknowns are Laurent polynomials
δ_i, Λ_i (cell parameters), G_i (with θ⁺(γ^i_x) = D^{|x|−1}G_i), S = θ⁺(Σ). The Σ-parts are then
W = G₁G₂/S (i ≠ j, times D^{|x|+|y|−2}), U_i = G_i(G_i − δ_iD)/S and V_i = G_i(DG_i − δ_iΛ_i)/S (within cell i, times a
power of D). All of these must have nonnegative coefficients, dominate the absolute values of the true constants
coefficientwise, and agree with them mod 2 (conditions C0–C6 of the search script). Associativity is automatic: the
algebra is a subalgebra of (cells) × (scalars) through θ⁺.

**4.2 Lemma [proved here].** U₁U₂ < W² at every real q > 1, so W = D is impossible at ε = +1 (at ε = −1 it holds
with U₁ = U₂ = W = D, because there δ₁ + δ₂ = 0). With δ₁ = δ₂ = δ, W = ωD, U_i = μ_iD:
G₁ = Dδ·ω(ω + μ₁)/(ω² − μ₁μ₂), G₂ = Dδ·ω(ω + μ₂)/(ω² − μ₁μ₂), and V_i = D·U_i + Wδ_i(D² − Λ_i)/G_{3−i}.

**Theorem 7 (a dimension ring exists) [computed: `…_search.py` finds 268 solutions in its window;
`…_verify.py` checks the one below on all 1000 triples: 132 nonzero constants, 0 negative coefficients, 0 domination
failures, 0 parity failures, 0 associativity failures].** The following is a dimension ring for (Ȟ₃, E^opp(3)):
- cells: δ⁺ = D(D − 3) = q² + q + q⁻¹ + q⁻² for both cells (the coefficientwise absolute value of δ₂);
  Λ₁⁺ = D(4D − 9), Λ₂⁺ = 3D² − 10D + 4, with q-coefficients (4, 7, 6, 7, 4) and (3, 2, 2, 2, 3);
- trivial character: θ⁺(γ¹_x) = 10D^{|x|+1}(D − 3), θ⁺(γ²_x) = 15D^{|x|+1}(D − 3), θ⁺(Σ) = 30D³(D − 3)²;
- Σ-parts: W = 5D, U₁ = 3D, U₂ = 7D, V₁ = D(2D + 3), V₂ = 6D² + 5D − 2.
That is: γ^i_xγ^i_y = δ⁺D^α(Λ_i⁺)^β γ^i_z + κΣ with κ = D^{|z|+α−1}·(U_i/D or V_i), γ^i_xγ^j_y = 5D^{|x|+|y|−1}Σ, Σγ = θ⁺(γ)Σ,
Σ² = θ⁺(Σ)Σ. It corresponds to (ω, μ₁, μ₂) = (5, 3, 7) in the Lemma.

**Theorem 7′ (a dimension ring with unimodal dimensions) [computed: `…_unimodal.py` finds 144 in the same window;
the one below was checked on all 1000 triples with the functions of `…_verify.py`: 0 failures of positivity,
domination, parity and associativity, and all 132 constants symmetric and unimodal].** Keep W = 5D, U₁ = 3D, U₂ = 7D,
Λ₁⁺ = D(4D − 9), Λ₂⁺ = 3D² − 10D + 4, V₁ = D(2D + 3), V₂ = 6D² + 5D − 2, and replace δ⁺ by
  δ⁺ = (D − 1)(D − 2) = q² + q + 2 + q⁻¹ + q⁻²,
so that θ⁺(γ¹_x) = 10D^{|x|}(D − 1)(D − 2), θ⁺(γ²_x) = 15D^{|x|}(D − 1)(D − 2), θ⁺(Σ) = 30D(D − 1)²(D − 2)². In this ring the
six constants of P-F-E3-01 have dimensions (3, 5, 10, 11, 14, 11, 10, 5, 3), against traces
(1, −1, 2, −3, 2, −3, 2, −1, 1). So VIII's unimodality, asked of dimensions as in the main session's §6.3, holds for a
realization that composes. It is a different realization from E4's (1, 5, 11, 14, 11, 5, 1) times the torus.

**Corollary 8 (the categorification) [proved here from Theorems 5 and 7].** With ĉ = (d + c)/2 + ε(d − c)/2, the
objects b̂ ∈ Mat₁₀(𝒯_ε) of Theorem 5 form a monoidal category of sign-twisted Tate objects whose Grothendieck ring is
free over 𝔸 on E^opp(3), is the dimension ring at ε = +1, and is Ȟ₃ with its 132 structure constants at ε = −1.
By Theorem 4(f): at primes p ≡ 3 mod 4 its odd Frobenius traces are the nonstandard structure constants, and at
primes p ≡ 1 mod 4 its counts are the dimension ring.

**What the construction is not.**
- It is not canonical. The window of the search already contains 268 dimension rings; nothing selects one.
- Its dimensions are not unimodal: δ⁺ has q-coefficients (1, 1, 0, 1, 1), and the six failing constants have
  dimensions (3, 5, 4, 7, 10, 7, 4, 5, 3) against traces (1, −1, 2, −3, 2, −3, 2, −1, 1).
  This is a feature of that solution only: see Theorem 7′.
- It is built from the structure constants; it does not explain their positivity. A construction that would do so
  has to produce the objects b̂ first, for instance from the Hecke category of S₃ × S₃ and the pair (σ, β) of
  Theorem 1, and that is [open].
- The pentagon holds because the category sits inside matrices of objects; no duality or rigidity is claimed.

## 5. What A, the F_{1²}-curve and the split zero do together

- **The split zero alone** types the two zeros: e is present with value 0, τ is absent. Counting with the basepoint
  gives the Tate tower and the unit ζ (Theorem 4(a)). Over a finite field everything it counts is Tate, and purity
  is not in question.
- **The sign ε alone** (Connes–Consani's F_{1²}, globally χ₋₄) makes a negative trace the trace of an honest object,
  and makes e an object: 1 + ε, two conjugate points, ζ_{Q(i)} (Proposition 4′).
- **A alone** locates zeros of ζ and of L(s, χ₋₄).
- **Together [rests on A]:** every effective class ĉ has a zeta whose zeros lie on the lines Re s = j + ½, whose
  pole orders are the a_j⁺ and whose zero densities are the dimensions (Theorem 4(e)); the functional equation is
  bar-invariance; the multiplication of Ȟ₃ lifts to these zetas over Z[1/2] (Corollary 8 with Theorem 4(d)). The
  prime 2, where ε² = 1 fails, is the ramified prime of the Gaussian avatar; it is the same phenomenon as "ε forces
  n odd" in Connes–Consani's Frobenius.

**What this resolves.**
1. The open step (3) of the brief: composing realizations exist (Corollary 8); E4's do not (Proposition 5); every
   composing one hides cancelling pairs in the bottom cell (Proposition 6).
2. F42 (no single finite Weil object carries all words): the 132 multiplicity objects are fixed finite objects, and
   every word is obtained from them by composition in a monoidal category. The unification is categorical, not a
   single Frobenius module.
3. The form of the rank-three data: Theorems 1 and 2 derive it, including the parity of a and the single failing
   value.
4. The reduction "nonstandard RH = A plus a realization question per rank" becomes exact: the realization question
   at rank r is the existence of a dimension ring for (Ȟ_r, E(r)). The zeros are then on the lines by A, for any
   lift; A is not what is hard. The existence of a dimension ring is not automatic (Proposition 6 shows the
   obstruction that had to be absorbed), and at rank three it holds.

**What it does not resolve.**
- Unimodality of dimensions holds in the ring of Theorem 7′, but that ring is one of 144 found; nothing yet ties it
  to a Lefschetz operator.
- Positivity of the f is an input, not an output.
- Rank four needs E(4). Theorem 1 gives, before any computation, even a and even-weight Tate type there, for a
  Q(D)-rational basis; whether VIII's E(4) is Q(D)-rational is to be checked from its definition.

## 6. Open points, in order

1. A principle that selects one dimension ring among the unimodal ones (a Lefschetz operator on the multiplicity
   objects, or minimality in a stated sense).
2. A canonical dimension ring: from the Hecke category of S₃ × S₃ with the involutions σ⊗σ and β⊗β, where
   P_s = (1 + σ⊗σ)(C′_s⊗C′_s). The cancelling pairs of Proposition 6 should be the non-stable (induced) summands.
3. The general-rank form of Theorem 3: Ȟ_r as the span of the group generated by the ς_i⊗ς_i, and its relation ideal.
4. E(4), then Theorem 5 at rank four.
