# Consult: what the extracted statements imply (items 1–10 of the user's direction, and three combinations)

By agent a157422a (Claude Fable 5.2 at effort max), for the main session (Claude Opus 5.5 at effort max).
Written 21 Nov 2026, 17:42 UTC. Section letters are those of `EXTRACTION_20261121.md`; "consult 1" is my
`CONSULT_a157422a_FABLE_SHAPE.md`.

**Read for this:** `EXTRACTION_20261121.md` (whole); `IMPLICATIONS_REPORT_20261121.md` (lines 1–418, and of section 10:
lines 878–912, 1010–1040, 1047–1082); `HODGE_DIVISION_ATTACK_20261121.md` (lines 1–150); the register entries H02, H12,
H19; the consults a8d75352 (whole), af2a18f6 (opening only), a0805369 (lines 100–146 and its headings); the label
consult's script and its run files; GCT VIII `main.tex` (lines 1560–1636, 1700–1722, 1925–1950, 2120–2140).

**Script:** `consult_a157422a_implications_checks.py` beside this file (mpmath 1.3.0, numpy 2.4.4).

**Status marks:** [proved here]; [computed] with the script; [standard] with the source named (every literature citation
is from memory, no paper was opened, except GCT VIII as listed); [rests on A], [rests on M], [rests on E]; [open].
A is Alpöge's RH and GRH for Dirichlet L-functions; M is Masullo's draft; E is OpenAI's refutation of ETH. I have read
none of the three.

## Summary

1. K₀ of Spec G(R) is the monoid ring of connected finite posets decorated by projective R-modules. It contains the
   ring of Dirichlet polynomials, with n^{−s} the class of (R^n)₊, and Σ_j (rk Q_j)^{−s} is a ring homomorphism for
   every s. Pic is Pic(R); the divisor of the Boolean direction is idempotent.
2. ζ^sep_K is meromorphic with the one pole of ζ_K; for K = Q it is ζ − 1 and has no functional equation of Selberg
   type; the zeros of (1+u)ζ − u reach the abscissa σ with ζ(2σ)/ζ(σ) = u/(1+u) (1.5780 for 2ζ − 1).
3. RH is equivalent to: every Toeplitz section (λ_{|j−k|}) of the Li coefficients has exactly one positive
   eigenvalue. Under A the Li coefficients are the Lorentz products of a Z-orbit of null vectors, and √λ_{|m−n|} is a
   Hilbert-space distance.
4. The central measure of χ_Ξ is the law of the RSK shape of a word whose letters are zeros of ζ drawn with
   probability γ^{−2}/Z(2); its limit shape is the graph of the zero-counting function. Sampling the Pólya frequency
   function with transform 1/Ξ gives characters of U(∞) whose Voiculescu parameters are 1/(e^{hγ_k} − 1).
5. GCT VIII's signed form is, up to a half twist, the class of a torus G_m^a with effective coefficients; the cube
   is the coordinate stratification, a is the order of vanishing at v = 1, and 90 of the 114 dimensions of the
   rank-four algebra vanish there.
6. The exponent 1/24 of the P-F57 wave is ∫₀¹(1 − m)m²/2 dm; the count and its off-class constituent are two sheets
   differing by twice the wave.
7. Neighbour agreement of the labels at finite height is given by a two-parameter Gaussian formula that reproduces
   the observed 0.39–0.44; the limit 0.667 is out of computational reach. Collision heights at time −|t| follow
   |t|^{−3/2}/log⁴, with all pairs collided only beyond exp(π√2/√|t|).
8. e^{2πiμ₀} = −(5 + 2√6) says sin²(πμ₀) = 3 = −1/(4ζ(−1)), and is the Kummer class of a unit in the limit mixed
   Hodge structure; the zeros of all derivatives of ℘ at the cusp are the roots of the Eulerian polynomials.
9. For 0 < |t| < ½ the function ζ(s, 1+t) is not cQ^s times any Euler product. The labels are the signs of the
   residues of one explicit meromorphic function.
10. The point side of a trace formula holds over every commutative semiring; the Boolean skeleton has weight 0;
    purity in the effective cone is effectivity after the weight-parity sign.

---

## Item 1 (A1–A2). Quasi-coherent sheaves, K₀ and Pic of X_R = Spec G(R)

Input [paper, as the note's sections 1 and 3 record it]: G(R)-semimodules are functors from a join-semilattice with 0
to R-modules; M^{−1}G(R) = G(M^{−1}R); finitely generated projectives are the pairs (J, Q), J a finite poset, Q_j
nonzero finitely generated projective R-modules, with skeleton the lattice O(J) of down-sets and fibre ⊕_{j∈U} Q_j.

**1.1 Quasi-coherent sheaves [proved here from the input].** On the affine semiring scheme X_R (Toën–Vaquié's relative
schemes, or Lorscheid's blue schemes), QCoh(X_R) = G(R)-SMod. The point η = {τ} is open and lies in every nonempty
open set, and Spec R = V(e) is closed. For a sheaf M:
- its restriction to η is the join-semilattice L = eM (base change along χ_R);
- its restriction to V(e) is the R-module R ⊗ M = colim_L M_l (base change along p_R);
- M itself is the functor L → R-Mod.
So QCoh(X_R) is the Grothendieck construction ∫_L Fun(L, QCoh(Spec R)): a support diagram of quasi-coherent sheaves
on Spec R indexed by a semilattice living at the Boolean point. For a fixed finite L it is the module category of
the incidence algebra R[L]; the projective (J, Q) is the sum of the representable functors at the join-irreducibles
↓j with multiplicity modules Q_j. This answers [q] of A2 affirmatively, in this sense.

**1.2 The trait [proved here].** For a field K, G(K) has the two primes {τ} ⊂ {τ, e}: its spectrum is a Sierpiński
space with open point of residue semifield B and closed point of residue field K. The maximal ideal is generated by
the idempotent e. So G(K) is a rank-one valuation semiring whose value monoid is {0 < ω < ∞} with ω + ω = ω. The
Milnor square G(R) = R ×_K G(K) says that X_R is Spec R placed as the closed fibre of this characteristic-one trait.
This is the exact sense in which G adds one dimension.

**1.3 Theorem (K₀) [proved here from the input].** Let 𝒞(R) be the set of isomorphism classes of connected decorated
posets (J, Q). Then:
(a) the monoid of finitely generated projectives under ⊕ is free commutative on 𝒞(R);
(b) (J, Q) ⊗ (J′, Q′) = (J × J′, Q_j ⊗ Q′_{j′}), so 𝒞(R) is a monoid and K₀(X_R) = Z[𝒞(R)], with effective cone N[𝒞(R)];
(c) p_*: K₀(X_R) → K₀(R) is (J, Q) ↦ Σ_j [Q_j], and χ_*: K₀(X_R) → K₀(B) is (J, Q) ↦ [J];
(d) K₀(B) is the Grothendieck ring of finite posets under disjoint union and product, a polynomial ring on the
    product-indecomposable connected posets with at least two elements (Hashimoto 1951, unique factorization of
    connected posets) [standard];
(e) for R connected, D_s(J, Q) = Σ_{j∈J} (rk Q_j)^{−s} is a ring homomorphism K₀(X_R) → C for every s ∈ C.
    D₀ = |J| is the Boolean rank, D_{−1} is the rank of p_*, and D_{−1} ≥ D₀ on the effective cone, with equality
    exactly when every Q_j is a line bundle.
Proof. (a) A decorated poset is uniquely the disjoint union of its connected components, and ⊕ is disjoint union.
(b) Base change is monoidal: the skeleton of M ⊗ N is O(J) ⊗_B O(J′) = O(J × J′) (tensor product of finite
distributive lattices as join-semilattices; Fraser 1976), and the fibres multiply. For one-point posets I checked it
directly: a G-bilinear map Q₊ × Q′₊ → N lands in one fibre N_l, l = β(0, 0), and is R-bilinear there, so
Q₊ ⊗ Q′₊ = (Q ⊗_R Q′)₊. A product of connected posets is connected. (c) and (e) follow: D_s is additive on disjoint
unions and Σ_{(j,j′)} (r_j r′_{j′})^{−s} factors. ∎

**Consequences.**
- (R^m)₊ ⊕ (R^n)₊ is not (R^{m+n})₊ (the skeletons have 4 and 2 elements), but (R^m)₊ ⊗ (R^n)₊ = (R^{mn})₊. So for a
  field k the classes [n] = [(k^n)₊] span a copy of the ring of Dirichlet polynomials Z[(N_{≥1}, ×)] inside K₀(X_k),
  with [n] ↦ n^{−s} under D_s. The counit is evaluation at s = −1; the Boolean point is evaluation at s = 0.
  Adjoining τ turns the rank from an additive invariant into a multiplicative variable.
- For R = O_K: decorations are pairs (r, c) ∈ N_{≥1} × Cl(K) (Steinitz) [standard]. The one-point classes form the
  monoid {r + cε : ε² = 0} under multiplication, (r, c)(r′, c′) = (rr′, r′c + rc′), with unit group Cl(K).
  p_*(J; r, c) = (Σr_j, Σc_j) ∈ Z ⊕ Cl(K). The characters of the one-point monoid are
  (r, c) ↦ r^{−s}ψ(r^{−1}c) for r prime to the order of ψ ∈ Cl(K)^∨, and 0 otherwise.

**1.4 Pic and divisors [proved here].** Units of G(R) are those of R, and the stalk at η is B with trivial unit group.
An invertible semimodule has a one-point skeleton, so Pic(X_R) = Pic(R): for O_K it is Cl(K), with the class of 𝔞
represented by 𝔞₊ (the note's section 1, item 7). The Boolean point changes divisors instead: X_R has exactly one
prime of height one, {τ, e}, and V(e) = Spec R is the divisor of e. Since e² = e, n·V(e) = V(e): the divisor
semigroup in the Boolean direction is B. The nonzero principal ideals form (R∖0)/R^× with one absorbing element (e)
adjoined.

## Item 2 (A3). The separated sheet, 2ζ − 1 and (1+u)ζ − u

**2.1 Continuation [proved here].** ζ^sep_K(s) = 2^{−s} + Σ_{k≥0} C(−s, k)(ζ_K(s+k) − 1), where the series converges
absolutely on compacta away from s = 1 (ζ_K(s+k) − 1 = O(2^{−k})). The pole of ζ_K(s+k) at s = 1 − k is cancelled by
the zero of C(−s, k) for k ≥ 1. So ζ^sep_K is meromorphic on C with one simple pole, at s = 1, with the residue of
ζ_K. Its values at s = −m are finite sums of values ζ_K(k − m) plus one residue term.

**2.2 No functional equation for K = Q [standard, applied here].** ζ^sep_Q = ζ − 1. Its coefficients are 0, 1, 1, …
It does not satisfy ζ's functional equation (Hamburger 1921: only multiples of ζ do). It satisfies no functional
equation of Selberg type at all: its zeros number (T/2π) log T up to height T, so its degree would be 1, and
Kaczorowski–Perelli (Acta Math. 182, 1999) show that the coefficients of a degree-one function are, after a twist
n^{iθ}, periodic. For [K:Q] ≥ 2 the same statement is [open].

**2.3 Zeros.** [standard unless marked]
- The zeros of ζ^sep_Q are the 1-points of ζ. Along the path ζ(s, 1+t), 0 ≤ t ≤ 1, the n-th zero drifts upward at mean
  rate γ/log γ per unit t (from N(T; a) = (T/2π) log(T/(2πea)) + O(log T)), which is the total iT²/(4π) of C1.
- The zeros of (1+u)ζ − u are the a-points, a = u/(1+u). N_a(T) = (T/2π) log(T/(2πe c_a)) + O(log T), c_a = 1 for
  a ≠ 1 and c₁ = 2 (Landau). Almost all lie within (log log T)²/log T of the line (Levinson 1975).
- **In the half-plane of absolute convergence [proved here from Bohr's theorem].** For 0 < a < 1, (1+u)ζ − u has
  no zero with real part > σ_a, where ζ(2σ_a)/ζ(σ_a) = a, and it has zeros with real part arbitrarily close to every
  σ ∈ (1, min(σ_a, 1.78)); for a ≤ 0.585 (u ≤ 1.41) that is the whole interval (1, σ_a). Reason: the values of ζ on Re s = σ are dense in {Π_p (1 − p^{−σ}e^{iθ_p})^{−1}}, whose least
  modulus is ζ(2σ)/ζ(σ), and for σ < 1.78 this set has no hole. [computed] σ_{1/2} = 1.5780171 for 2ζ − 1. For the
  1-points the abscissa is about 1.78 (where the prime sum P(σ) equals 2^{1−σ}; circle approximation).
- **What A gives [rests on A].** At u = 0 every zero is on the line. For u > 0 the zeros are not on the line: by
  Selberg's argument under RH about 3/4 of the a-points lie to the left and 1/4 to the right (Selberg 1992; the
  exact hypotheses are to be verified). At first order in u a zero moves with velocity 1/ζ′(ρ), whose real part is
  −sin θ(γ)/Z′(γ); this is positive whenever Gram's law holds at that zero. So the zeros leave to the right at first
  order where Gram's law holds, and three quarters of them end on the left for fixed u.

## Item 3 (A5). The Lorentzian form, its lattice, and the Li coefficients

**3.1 The form [proved here given the explicit formula; consult 1, Q3 item 5].** For a test function f with Mellin
transform F, put a = F(0), b = F(1). The sum over places is G(f, f) = 2Re(a b̄) − Σ_ρ F(ρ)·conj F(1 − ρ̄).
- **Hyperbolic plane.** The functions with transform in ξ(s)·C[s] vanish at every zero. Modulo ξ(s)s(s−1)C[s], which
  is in the radical, they form a plane with basis e₁ = [2(1−s)ξ] (a = 1, b = 0) and e₂ = [2sξ] (a = 0, b = 1);
  G(e_i, e_i) = 0 and G(e₁, e₂) = 1. These are the two rulings; H = e₁ + e₂ is the ample class, G(H, H) = 2.
- **Néron–Severi analogue.** V = (test functions)/radical. Convolution is composition of correspondences, f ↦ f* is
  transposition, the Dirac mass at λ is the graph of the scaling by λ, and the unit δ is the diagonal with
  δ² = 2 − #{zeros}, the analogue of 2 − 2g.
- **Hodge index [rests on A].** On H^⊥ = {a + b = 0}, G = −2|a|² − Σ_ρ|F(ρ)|² ≤ 0. Castelnuovo–Severi is
  G(f, f) ≤ 2Re(a b̄).
- **The sphere.** In the coordinate u = 1 − 1/s the critical line is the unit circle, the zeros lie on it [A], and
  the poles s = 1, 0 are u = 0, ∞, exchanged by the reflection u ↦ 1/ū. This is the July picture (A5): the zeros on
  a great circle and the two poles at the two points exchanged by the reflection.

**3.2 Theorem (Li–Hodge index) [proved here; computed].** Let λ_n be Li's coefficients, λ₀ = 0, and
L_N = (λ_{|j−k|})_{0≤j,k≤N}. The following are equivalent:
(i) RH;
(ii) for every N, L_N has exactly one positive eigenvalue (signature (1, N));
(iii) −Σ c_j c_k λ_{|j−k|} ≥ 0 for all real c with Σc_j = 0;
(iv) (Z, d(m, n) = √(2λ_{|m−n|})) embeds isometrically in a Hilbert space.
Proof. (i) ⟹ (iii): with u_ρ = 1 − 1/ρ on the circle and P(z) = Σc_j z^j, P(1) = 0, one has
Σ_ρ|P(u_ρ)|² = −Σ c_j c_k λ_{|j−k|}. It is positive for P ≠ 0 because the u_ρ are infinitely many. (iii) ⟹ (ii): L_N is
negative definite on a hyperplane and has zero trace and positive entries. (ii) ⟹ (i): a principal submatrix has at most one positive eigenvalue and zero trace, so the principal 3 × 3
minor on (0, m, m+n), which is 2λ_mλ_nλ_{m+n}, is ≥ 0. Let n₀ be the least index with λ_{n₀} < 0; n₀ ≥ 2 since λ₁ > 0.
The minor on (0, 1, n₀) forces λ_{n₀−1} = 0 (so n₀ ≥ 3). The principal submatrix on (0, 1, n₀−1, n₀) is then
[[0, B], [Bᵀ, 0]] with B = [[λ₁, λ_{n₀}], [λ_{n₀−2}, λ₁]] in the order (0, n₀−1 | 1, n₀), and det B = λ₁² − λ_{n₀−2}λ_{n₀} > 0, so
it has two positive eigenvalues: a contradiction. Hence λ_n ≥ 0 for all n, and Li's criterion applies. (iii) ⟺ (iv) is Schoenberg's theorem; the embedding is n ↦ v_n = (1 − u_ρ^n)_ρ. ∎
[computed] L₃, L₆, L₁₁ each have one positive eigenvalue.

**3.3 The structure under A [proved here, given A].**
- L(c, c) = 2·deg(c)·ℓ(c) − ‖Σc_j v_j‖², with deg(c) = Σc_j and ℓ(c) = Σc_jλ_j. The two linear forms deg and ℓ span
  the hyperbolic plane; the unit vectors δ_n are null vectors with pairwise products λ_{|m−n|} > 0. The Li
  coefficients are the Lorentz products of the orbit of a null vector under the shift.
- n ↦ v_n is a 1-cocycle of Z in the unitary representation (ℓ²(zeros), multiplication by u_ρ). It is not a
  coboundary, since λ_n ~ (n/2) log n is unbounded: the vector (1)_ρ that would bound it is the diagonal class and is
  not in ℓ². Z acts on ℓ²(zeros) by affine isometries with displacement ‖v_n‖² = 2λ_n.
- **Inequalities.** (a) |√λ_m − √λ_n| ≤ √λ_{|m−n|} ≤ √λ_m + √λ_n. (b) λ_{kn} ≤ k²λ_n. (c) λ_{m+n} + λ_{|m−n|} ≤ 2λ_m + 2λ_n,
  with defect ½Σ_ρ|1−u_ρ^m|²|1−u_ρ^n|². (d) For every k ≥ 1,
  2Σ_{j=1}^{k} (−1)^{j−1} C(2k, k+j) λ_j = Σ_ρ (ρ(1−ρ))^{−k}, an identity that holds without RH; under A the right side
  is Σ|ρ|^{−2k} > 0, so the central differences of λ at 0 alternate in sign.
  [computed] k = 2: 2(4λ₁ − λ₂) = 7.4201·10⁻⁵; k = 3: 2.8736·10⁻⁷. λ₂ = 4λ₁ − 3.71·10⁻⁵: inequality (b) is nearly an
  equality because the zeros are near u = 1.
- **For the sections K(m, n) of consult 1:** K = −L restricted to differences from the base point 0; K_N is the Gram
  matrix of v₁, …, v_N, so det K_N > 0 and det K_N ≤ Π 2λ_n (Hadamard).

## Item 4 (B1). The character χ_Ξ, its central measure, and U(∞)

**4.1 [standard: Thoma 1964; Vershik–Kerov 1981; applied here; rests on A].** χ_Ξ is extremal, so its spectral measure
on the Thoma simplex is the Dirac mass at (α = 0; β_j = γ_j^{−2}/Z(2)). Its central measure on diagrams with n cells is
M_n(λ) = f^λ·s_{λ′}(β), the law of the transposed RSK shape of a word of n independent letters, each equal to the j-th
zero with probability β_j. [computed] β₁ = 0.21663, β₂ = 0.09794, β₃ = 0.06919.

**4.2 Limit shape [standard law of large numbers; statement made here].** λ′_j/n → β_j almost surely for every j, and
no row has macroscopic length. For x > 0 not equal to any β_j, the row of index ⌈xn⌉ has length N₊((xZ(2))^{−1/2}) for
all large n, where N₊(T) counts the zeros with 0 < γ ≤ T. So the limit shape is the graph of the zero-counting
function in the coordinate x = 1/(Z(2)T²). The column fluctuations are Gaussian of order √n with multinomial
covariance (Féray–Méliot; Bufetov) [standard]. The growth of the first row is [open] (heuristically
n^{1/3}(log n)^{2/3}, from nβ_K ≈ K).

**4.3 The probability law behind it [proved here, given A].** Ξ(0)/Ξ(it) = Π_k (1 + t²/γ_k²)^{−1} is the characteristic
function of X = Σ_k L_k/γ_k with independent standard Laplace variables L_k. The density of X is Ξ(0)·Λ_Ξ, where
Λ_Ξ(x) = (1/2π)∫ e^{ixy} dy/ξ(½ + y) has bilateral Laplace transform 1/Ξ(s) for |Re s| < γ₁. By Schoenberg (1951), Λ_Ξ
is a Pólya frequency function, and that property is equivalent to RH (Gröchenig 2020 states this form) [standard].
Var X = 2Z(2), and **β_k is the share of the variance of X carried by the k-th zero.**

**4.4 Characters of U(∞) [proved here from Edrei 1953 and Voiculescu 1976, given A].** For every h > 0 the sequence
a_n = Λ_Ξ(hn), n ∈ Z, is a two-sided Pólya frequency sequence (a restriction of a totally positive kernel). Its
generating function on the circle is the periodization G_h(e^{iφ}) = (Ξ(0)/h)·Σ_{m∈Z} 1/ξ(½ + (φ + 2πm)/h). Since
Λ_Ξ(x) is asymptotically a combination of e^{−γ_k|x|}, G_h has poles exactly at u = e^{±hγ_k}. So Φ_h = G_h/G_h(1) is
the Voiculescu function of an extreme character of U(∞) with
  α_k^+ = α_k^− = 1/(e^{hγ_k} − 1),
the Bose–Einstein occupation numbers of the zeros at inverse temperature h; the remaining factor has only negative
real zeros. **Relation to the CUE:** U ↦ Π_j Φ_h(u_j) is a positive definite class function on U(N) for every N; its
coefficient on the irreducible character of signature λ is the Toeplitz minor det[φ_{λ_i − i + j}] ≥ 0, and its CUE
mean is the Toeplitz determinant D_N(Φ_h) (Heine), with Szegő asymptotics. All of these are positive under A, and
their positivity for all h and N is equivalent to RH.

## Item 5 (B2). GCT VIII's signed form

GCT VIII, Conjecture "Positivity" (label cposkroneckerright, TeX lines 1610–1625): in the Kronecker case every
structural constant of the canonical basis E(r) of the nonstandard Hecke algebra is ±(q^{1/2} − q^{−1/2})^a f, with f
bar-invariant, positive and unimodal. VIII reports a computer check at r = 3 (lines 1925–1950).

**5.1 The cube and its fibres [proved here].** With v = q^{1/2}: (v − v^{−1})^a = v^{−a}(q − 1)^a = v^{−a}·#G_m^a(F_q). So
  ±(v − v^{−1})^a f(v) = ± Tr(Frob | H_c^*(G_m^a) ⊗ F)(a/2),
with F a pure effective graded space of character f. The Boolean cube P([a]) is the coordinate stratification of
A^a: G_m^a = A^a minus the coordinate hyperplanes, and inclusion–exclusion over the hyperplanes is the Möbius sum of
consult a8d75352, Q1-ii-a. "f positive" says that the coefficient object is effective; the sign is the parity of
the cohomological degree, since H_c^{a+j}(G_m^a) = Q(−j)^{C(a,j)}.

**5.2 The basis fixes the cube [proved here].** If c = ±(v − v^{−1})^a f with f ∈ N[v, v^{−1}] nonzero, then f(1) > 0, so
a is the order of vanishing of c at v = 1 and the sign is that of the a-th derivative there. So a, the sign and f
are functions of c; what is not determined is a graded space with character f. The answer to [q] of B2: the cube and
the characters of its fibres are fixed by the structure constants; the fibres themselves need a categorification.

**5.3 The cone [proved here].** The classes Σ_a t^a f_a with t = v − v^{−1}, f_a ∈ N[v, v^{−1}], form a proper cone in
Z[v, v^{−1}]: its elements are ≥ 0 at v = 1 (where only f₀(1) survives, the count of zero-dimensional strata). VIII's
conjecture says more: each structure constant is, up to sign, one monomial t^a f in this cone, supported on one layer
|I| = a of the skeleton.

**5.4 Rank four [computed].** dim Ȟ_r at generic v and at v = 1: r = 2: 2 and 2; r = 3: 10 and 6; r = 4: 114 and 24
(cyclic module of 1 ⊗ 1 in H_r ⊗ H_r, v = 1.37). At v = 1 the algebra is the group algebra of the diagonal S_r. So the
elements vanishing at v = 1 have dimension 4 at rank three and 90 at rank four: at rank four the constants with
a ≥ 1 are the bulk. The explicit rank-four constants need VIII's basis E(4) (its minimum-degree construction),
which I did not implement: [open].

## Item 6 (B3–B4). The near-supported zero on P-F57's family

From consult a0805369 (lines 100–146); I did not open the run's files.

**6.1 Two sheets [proved here from P-F56d as quoted].** Let q_r be the constituents and W_n the dyadic wave, with
q_r − q_{r+L/2} = 2W_n(r). At an argument x the true count is f_n(x) = q_x(x) = A + W and the off-class value is
q_{x+L/2}(x) = A − W, with A the half-sum. For x ≈ 2^{cn}, c < ¼: f_n(x) ≤ 2^{(c/6)n⁴ + …} while 2W ≥ 2^{n⁴/24 − 2n³ − 1}. So
A = −W(1 − ε) with ε ≤ 2^{−(1/24 − c/6)n⁴ + O(n³ log n)}: a two-term cancellation to that relative precision. The count
and its ghost constituent are two sheets differing by 2W; GCT VI's saturation asks both to be positive.

**6.2 The exponent 1/24 [my reading; to be checked against P-F56].** If the wave is the fixed-point contribution of
an element g of order 2^{n−1} in the stabilizer of the chain cubic, acting on x_i by ζ^{±2^i}, then its size is
Π_m |1 − χ_m(g)|^{−1} over the cubic monomials m = x_i x_j x_k, and log₂ of the factor is about n − max(i, j, k). The sum
is Σ_k (n − k)·C(k+1, 2) = n⁴/24 + O(n³), which is the run's leading term. On this reading the wave is large because
g is close to the identity on most of the tangent space: a near-pole of order ~n³/6 at t = 1 seen from a nearby root
of unity.

**6.3 Circuits [proved here].**
- A formula with nonnegative terms for f_n(x) has every term ≤ f_n(x). So the dyadic term is not a subsum of any
  positive formula at these arguments.
- A ring evaluation of the pole expansion needs working precision n⁴/24 − O(n³) bits per term for an answer of at most
  (c/6)n⁴ + O(n³ log n) bits: the supported zero costs a constant factor 1/(4c) in bit length, which is polynomial in
  n. The cost of the cancelling route lies in the number of conjugate poles (2^{n−2} for the dyadic wave), not in
  precision.
- In the language of consult 1 (corollary to Theorem 6): the monotone majorant of the pole expansion is
  ≥ 2^{n⁴/24}, the value is ≤ 2^{(c/6)n⁴}, and their ratio is the size of the supported zero.

## Item 7 (C1–C3). Labels, their correlation, and collision heights

**7.1 The increment [computed; corrects a first guess].** W_{n+1} − W_n = 1 − δ_n − (φ_{n+1} − φ_n)/π, with δ_n the
normalized gap and φ = arg ζ(3/2 + iγ). The φ-term does not vanish at computable heights (it is up to 0.4 for the
first 5000 zeros) and it reduces the variance: Var(W_{n+1} − W_n) = 0.102 against Var(δ) = 0.152 there.

**7.2 Density ½ [proved here].** The indicator of (0, 1) mod 2 is ½ + (2/π)Σ_{k odd} sin(πkW)/k. So the density of
right-movers is ½ if either the law of W_n mod 2 is asymptotically symmetric under W ↦ −W, or E e^{iπkW_n} → 0 for
odd k. A central limit theorem for W_n/σ does not give the second (lattice variables are a counterexample); what is
needed is decay of the characteristic function at the fixed frequencies πk. In the Gaussian model it is
(log T)^{−k²/4}; for the CUE the analogue is exact, E e^{−ik Im log Z_N} = Π_{j≤N} Γ(j)²/(Γ(j + k/2)Γ(j − k/2))
(Keating–Snaith) [standard], which is of order N^{−k²/4} for k = 1 and vanishes identically for k = 2. For ζ the
decay is [open], also under A. [computed] Mean of W over the first 5000 zeros: 0.0000; right-movers 2500 of 5000.

**7.3 Neighbour agreement at finite height [proved here in the Gaussian model; computed].** If (W_n, W_{n+1}) is
bivariate Gaussian with variance v and correlation r, the probability that consecutive labels agree is
  A(v, r) = ½ + (4/π²)Σ_{j,k odd} (jk)^{−1}[e^{−π²v(j²+k²−2jkr)/2} − e^{−π²v(j²+k²+2jkr)/2}].
For small v this is ½ + arcsin(r)/π. With σ² = Var(W_{n+1} − W_n) = 2v(1 − r) fixed and v → ∞ it tends to
½ + (4/π²)Σ_{k odd} e^{−π²k²σ²/2}/k², which is 0.6667 for the GUE gap variance 0.180: this is the "0.66" of C1.

| zeros | Var W | corr(W_n, W_{n+1}) | agreement observed | A(v, r) |
|---|---|---|---|---|
| 1–1000 | 0.0318 | −0.298 | 0.3914 | 0.4036 |
| 1001–3000 | 0.0419 | −0.219 | 0.4252 | 0.4297 |
| 3001–5000 | 0.0469 | −0.192 | 0.4382 | 0.4386 |

So the observed 35–47% is the finite-height value of the same law. The agreement is below ½ because consecutive
values of W are negatively correlated, and it reaches 0.667 only when Var W ≫ 1/π², that is when log log T is of
order ten. That limit cannot be observed.
**What is a theorem and what is not.** The correlation of labels at a lag of many mean spacings follows from the
variance of S(t + h) − S(t) (Fujii; Selberg), unconditionally or under A. The correlation at lag one needs the
nearest-neighbour gap law, which Montgomery's theorem, now unconditional in its range, does not give.

**7.4 Collision heights [rests on A for Λ = 0; on the GUE small-gap law, which is a conjecture].** Backward in time
two zeros with gap Δγ collide at t = −Δγ²/2 (Csordas–Smith–Varga dynamics; two-body approximation). With
P(δ ≤ ε) ≈ (π²/9)ε³, the expected number of collided pairs below height T at time −|t| is
  ((2|t|)^{3/2}/(144π²))·T·log⁴(T/2π).
So the first non-real pair of H_t appears near T₁ ≍ |t|^{−3/2}/log⁴(1/|t|), a power law. [computed] T₁ ≈ 2.3·10¹³ for
t = −10⁻¹¹; the Lehmer pairs behind the known lower bounds on Λ of that size lie within about two orders of magnitude
of this height (from memory). The height exp(π√2/√|t|) is where the collision threshold
√(2|t|) equals the mean spacing: above it essentially all zeros are non-real. C3's heuristic exp(c/√|t|) is this
second scale, not the first collision. The density of non-real pairs at height γ is
(log(γ/2π)/2π)·F(√(2|t|)·log(γ/2π)/2π), F the GUE gap distribution function.

## Item 8 (C6). The cusp identity

**8.1 The identity [proved here; computed].** At q = 0, ℘/(2πi)² = 1/12 + u/(1−u)², u = e^{2πiz}, and
(1−u)²/u = −4 sin²(πz). So ℘ = 0 at the cusp says −4 sin²(πμ₀) = −12 = 1/ζ(−1):
  sin²(πμ₀) = 3,  u₀ + 1/u₀ = −10,  u₀ = −(5 ± 2√6).
Euler's identity is the case sin² = 1. [computed] The zero of ℘ at τ = 1.5i, 2i, 3i is u = −0.0995715, −0.1009584,
−0.1010204, tending to −(5 − 2√6) = −0.1010205.

**8.2 The family [proved here].** ℘/(2πi)² = c at the cusp gives u + 1/u = 2 + 12/(12c − 1). The value u is a unit
exactly when k = 12/(12c − 1) is an integer, and then it is a unit of Q(√(k(k+4))), or a root of unity. Writing
−4 sin²(πμ) = k:

| sin²(πμ) | k | u | field |
|---|---|---|---|
| ¼, ½, ¾, 1 | −1, −2, −3, −4 | roots of unity of order 6, 4, 3, 2 | torsion |
| 5/4 | −5 | −(3 ± √5)/2 | Q(√5) |
| 3/2 | −6 | −(2 ± √3) | Q(√3) |
| 2 | −8 | −(3 ± 2√2) | Q(√2) |
| 3 | −12 | −(5 ± 2√6) | Q(√6) |

The norm is always 1, since u ↦ 1/u is the conjugation. The level c = 0 is the only one defined modularly (℘ has
weight 2), which is why 12 = −1/ζ(−1) is the constant that appears.

**8.3 Hodge-theoretic meaning [proved here, standard theory].** The points ±P₀ with x(P₀) = 0 in the short
Weierstrass form are canonical on every elliptic curve. τ ↦ (τ, z₀(τ)) is the period map of the 1-motive
[Z → E_τ, 1 ↦ P₀], a variation of mixed Hodge structure with graded pieces Z(0) and H₁(E_τ): an admissible normal
function. Eichler–Zagier's formula is its inhomogeneous Picard–Fuchs equation:
  d²z₀/dτ² = 144πi√6·Δ(τ)/E₆(τ)^{3/2},
a form of weight 3 with a branch point where E₆ = 0 (τ = i). There the two zeros of ℘ collide at a 2-torsion point;
at τ = e^{2πi/3} they are 3-torsion (fixed by the automorphism of order 3). At the cusp the 1-motive degenerates to
the Kummer 1-motive [Z → G_m, 1 ↦ u₀]: **the limit mixed Hodge structure is the extension of Z(0) by Z(1) with class
the unit −(5 + 2√6) of Q(√6)**. Its torsion part is the sign (Euler's e^{iπ} = −1), and log(5 + 2√6) is its real
period, the regulator. It is a unit because P₀ is an integral point: the equation (1−u)² + 12u = 0 is monic with
constant term 1.

**8.4 Other cusps [proved here].** ℘(z/(cτ+d), γτ) = (cτ+d)²℘(z, τ), so the zero set is equivariant and every cusp of
every modular family is locally the Tate curve at ∞. Hence the zero of ℘ gives the same unit −(5 + 2√6) at every
cusp, in the canonical coordinate of the identity component. Other units come from other canonical multisections.

**8.5 Theorem (derivatives) [proved here; computed].** For m ≥ 1, ℘^{(m)}/(2πi)^{m+2} at the cusp equals
Σ_{n≥1} n^{m+1}u^n = u·A_{m+1}(u)/(1−u)^{m+2}, with A_{m+1} the Eulerian polynomial. So the cusp values of the zeros of
℘^{(m)} are the roots of A_{m+1}. These are real, negative and simple (Frobenius) and A_{m+1} is monic palindromic with
integer coefficients. Therefore every such cusp value is −ε with ε a totally real positive unit, and
μ = ½ − i·log ε/(2π) lies on the line Re z = ½, the fixed line of z ↦ 1 − z̄.
- ℘″: A₃ = 1 + 4u + u², unit 2 + √3.
- ℘‴ = 12℘℘′: A₄ = (1 + u)(1 + 10u + u²), the 2-torsion point and the S6 unit 5 + 2√6.
- ℘⁗: A₅ = 1 + 26u + 66u² + 26u³ + u⁴, with u + 1/u = −13 ± √105.
Real-rootedness of the Eulerian polynomials is a Pólya frequency statement about the Eulerian numbers. So at the
cusp the zeros of the derivatives of ℘ are confined to the fixed line by total positivity: the shape of consult 1,
here as a theorem. [computed] All roots of A₃, A₄, A₅, A₈, A₁₂ are real and negative.

## Item 9 (A6). Hurwitz is not an L-function; deformations with tangent motion

**9.1 Theorem [proved here; uses only the uniqueness theorem for general Dirichlet series (Hardy–Riesz)].** Let
0 < |t| < ½. Then ζ(s, 1+t) is not of the form c·Q^s·D(s) with D an ordinary Dirichlet series with constant term 1; in
particular it is not c·Q^s times a finite product of integer powers of Euler products. So it is not the L-function,
in any normalization, of an ℓ-adic sheaf on a scheme of finite type over Z or of a motive over a number field, pure
or mixed. Purity is not needed.
Proof. The frequencies of ζ(s, 1+t) are log(n + t), n ≥ 1, all with coefficient 1. Those of cQ^sD(s) are log(m/Q)
with m = 1 present and least. Uniqueness gives 1/Q = 1 + t and (n + t)/(1 + t) ∈ N for every n. For n = 2 this is
1 + 1/(1+t) ∈ N, so 1 + t = 1/k with k ∈ N: t = 0 or t ≤ −½. ∎
The exception t = −½ is real: ζ(s, ½) = 2^s·Π_{p odd}(1 − p^{−s})^{−1}.

**9.2 Further facts.**
- [standard: Davenport–Heilbronn 1936, by Bohr's method] For transcendental t > −1, ζ(s, 1+t) has infinitely many
  zeros in every strip 1 < σ₁ < Re s < σ₂ < σ*(t), where (1+t)^{−σ} = ζ(σ, 2+t) at σ = σ*(t). [computed] σ*(0) = 1.7286472
  (ζ(σ) = 2). Under A the function at t = 0 has no zero with Re s > ½. So the zero-free half-plane is discontinuous
  at t = 0: the zeros with Re s > 1 come in from height of order (1/|t|) log(1/|t|).
- [proved here] The tangent direction is not tangent to Euler products: ∂_t log ζ(s, 1+t) at 0 is −sΣα₁(n)n^{−s}, with
  α₁(6) = 1/3 ≠ 0 at a non-prime-power and with the factor s.

**9.3 Proposition (characterization) [proved here].** Let Λ₀ be a completed L-function with Λ₀(1−s) = Λ₀(s), real on
the real axis, with simple zeros on the line, and Λ_t = Λ₀ + tΦ + o(t) with Φ meromorphic, real on the real axis,
regular at the zeros. Then Re ρ′(0) = 0 at every zero if and only if
  Φ = Φ₊ + g·Λ₀,
with Φ₊ invariant under s ↦ 1 − s and g meromorphic, anti-invariant and regular at the zeros. That is: to first
order the deformation is one that keeps the functional equation, composed with a multiplicative gauge Λ₀ ↦ e^{tg}Λ₀
(which fixes the zeros; g = (log Q)(s − ½) is a change of conductor).
Proof. ρ′ = −Φ(ρ)/Λ₀′(ρ); Λ₀′(ρ) is imaginary, Φ₊(ρ) real and Φ₋(ρ) imaginary on the line. So Re ρ′ = 0 iff Φ₋(ρ) = 0,
iff g = Φ₋/Λ₀ is regular at ρ. Anti-invariance of g is automatic. ∎

**9.4 Corollary (the labels as residues) [proved here].** For any deformation as above, Re ρ′(0) = −Res_{s=ρ}(Φ₋/Λ₀).
For the Hurwitz deformation, with χ(s) = π^{s−½}Γ((1−s)/2)/Γ(s/2),
  Re ρ′(0) = Res_{s=ρ} G,  G(s) = [sζ(s+1) − (1−s)χ(s)ζ(2−s)] / (2ζ(s)).
G is meromorphic and G(1−s) = −G(s). The Boolean label of ρ is the sign of the residue of G at ρ, and G is regular
at ρ exactly when the label is undefined. Sums of Re ρ′(0) over zeros are contour integrals of G; on Re s > 1 the
first term of G is (s/2)Σα₁(n)n^{−s}.

## Item 10 (A4). Trace formulas over semirings, the skeleton's weight, purity in the effective cone

**10.1 Theorem (point side) [proved here].** Let S be a commutative semiring, X a finite set with a self-map F, and
(M_x) free S-modules of finite rank with maps F_x: M_{F(x)} → M_x. Then Tr(F | ⊕_x M_x) = Σ_{F(x)=x} Tr(F_x | M_x) in S.
The trace of a block matrix is the sum of the traces of its diagonal blocks; no subtraction occurs. So the Lefschetz
formula for finite sets holds over every commutative semiring, B and G(R) included.

**10.2 The cohomological side [standard: transfer principle, Reutenauer–Straubing 1984].** An identity P = Q between
polynomials with coefficients in N that holds over Z holds in every commutative semiring. So each ring identity of
the trace-formula type holds over semirings once its negative terms are moved across: Cayley–Hamilton as
p⁺(A) = p⁻(A), the identity between closed walks and the determinant, Newton's identities. In G(R) the element −1
exists and x ⊕ (−x) = e: G(R) is a semiring with symmetry (Akian–Gaubert–Guterman) whose balanced elements are the
Boolean pair, and "balanced" means equal under p_R. A trace formula in G(R) is therefore the ring formula together
with its Boolean shadow.

**10.3 Which semirings carry a Weil-type formula for varieties [proved here].** Counting points is a semiring
homomorphism from effective classes to N, and X ↦ [X(F_q) ≠ ∅] is its Boolean shadow (consult 1, Theorem 6). A
formula without signs is available on effective polynomial classes:
- [X] ∈ N[L] (affine pavings): #X(F_{q^n}) ∈ N[q^n], even cohomology only;
- [X] ∈ N[T], T = L − 1 = [G_m] (torifications): #X(F_{q^n}) = Σ_k a_k (q^n − 1)^k, a_k the number of k-dimensional tori.
T = q − 1 counts the supported nonzero elements of F_q and q = T + 1 adds the zero. A^n = (G_m ⊔ {0})^n is the Boolean
cube P([n]) with fibres G_m^I: this is the skeleton of G(R)^n, the smash-product rule of A3 (w − 1 multiplicative),
and the cube of item 5. The value at T = 0 is the number of zero-dimensional strata.

**10.4 The weight of the skeleton [standard: Boolean matrix theory, index and period].** An endomorphism of a free
G(R)-semimodule is a pair (A, B), A a matrix over R and B a Boolean matrix with supp A ≤ B, and
Tr(φ^k) = (Tr A^k, Tr_B B^k), where Tr_B B^k = 1 iff the support digraph has a closed walk of length k. The sequence B^k
is eventually periodic, so the generating function of Tr_B B^k has poles only at roots of unity. The Boolean skeleton
carries weight 0; the weights live on the fibres, where Deligne's theorem applies fibre by fibre. On the toric
skeleton the rank |I| filters by the dimension of the stratum, and H_c^{k+j}(G_m^k) = Q(−j)^{C(k,j)} gives the weights of
each layer.

**10.5 Purity in the effective cone [proved here from Deligne's theorem].** Let K₀ be the Grothendieck group of
Frobenius modules, graded by weight, and ε the involution multiplying the weight-w part by (−1)^w. For X smooth and
proper, ε[RΓ(X)] = Σ_w [H^w] is effective. Equivalently: (H^i)_i ↦ Σ(−1)^i[H^i] loses nothing, because classes of
different degrees have different weights and cannot cancel. Without purity (open or singular X) numerator and
denominator factors of the zeta function can cancel. A supported zero of the count is an X ≠ ∅ with X(F_q) = ∅; for
curves purity confines these to q + 1 ≤ 2g√q.

## Combinations with the project's other results

**C-1. Ghosts are what Chevalley's theorem forbids [proved here from R3 of the Hodge attack; one part rests on M].**
For a Hodge class t on X/U let H_{≤C}(t) → U be the projective scheme of representations N·t = [Z⁺] − [Z⁻] of
complexity ≤ C (the Hodge attack, R3).
- The image of a scheme of finite type is constructible, so finite or cofinite in U. A ghost is a class for which
  the ind-scheme ∪_C H_{≤C}(t) covers every closed point and misses the generic point; this is impossible for each
  H_{≤C}. With 032's input: **the Hodge conjecture for t is the statement that the image of ∪_C H_{≤C}(t) is
  constructible.**
- Effective form [standard: arithmetic Nullstellensatz, Krick–Pardo–Sombra 2001]: if H_{≤C}(t) has empty generic
  fibre, the primes in its image divide one nonzero integer a_C with log|a_C| bounded in terms of the degrees and
  heights of its equations. So a ghost has c(v) > C for every v with Nv > |a_C|, and at most log₂|a_C| primes with
  c(v) ≤ C: an explicit lower bound for the growth of ghost complexity.
- [rests on M] "c_t ≤ C" is an instance of Hilbert's Nullstellensatz, and Koiran's theorem (CX-K01, CX-K02) applies:
  it is decided in AM by testing H_{≤C}(t) at random primes of polynomial bit length in the size of the instance. R3's
  "bounded division at infinitely many primes" becomes "at a random prime in an explicit window".

**C-2. A detector test by 2n + 1 intersection numbers [proved here; not compared with Proposition G of the attack].**
In the setting of Theorem W, let Y be an n-cycle and I_j = Y·(a^j)^{−1}(Y). Then
I_j = Σ_{i=0}^{2n} q_i·(a^i ā^{2n−i})^j with q_i = ∫ y_{2n−i} ∪ y_i, y_i the eigencomponents of [Y]. The 2n + 1 eigenvalues are
distinct, so q is obtained from I₀, …, I_{2n} by a Vandermonde system, and
  e_W[Y] ≠ 0 ⟺ q₀ ≠ 0 ⟺ a^{2n} is a characteristic root of the recurrence satisfied by (I_j);
then (−1)^n q₀ = T(e_W[Y])/2 > 0, and |q₀| ≥ m_W/(2R²) with R the resultant of Theorem W and m_W the minimum of T on
integral Weil classes. All eigenvalues have modulus Nm^n: the normalized operator is unitary, but the weights q_i
alternate in sign, so the Toeplitz form of (I_j) is indefinite. This is the precise sense in which purity sees
nothing of cycles (HECKE_DIV A3): the spectrum is on the circle by the polarization, not by positivity on classes
of cycles. Also [proved here]: a Weil class has degree 0 against θ^n (if t·θ^n ≠ 0 then a^{2n} = Nm^n, so a/ā is a root
of unity). Every representation N·t = [Z⁺] − [Z⁻] of a Weil class is therefore a balanced cancellation,
deg Z⁺ = deg Z⁻: Weil classes are supported zeros of the degree, and c_t measures the size of that zero.

**C-3. On k-SAT the cancelling regime beats the positive one exponentially [rests on E].** E decides
unsatisfiability of k-CNF in time 2^{o(n)}. For random 3-CNF with a linear number of clauses: resolution needs size
2^{Ω(n)} (Chvátal–Szemerédi 1988; Ben-Sasson–Wigderson 2001); polynomial calculus needs degree Ω(n) in every
characteristic (Ben-Sasson–Impagliazzo 1999; Alekhnovich–Razborov 2001); sum-of-squares needs degree Ω(n)
(Grigoriev 2001; Schoenebeck 2008) [standard]. So E's counting argument is simulated neither by resolution, the
proof system of the Boolean coordinate, nor by low-degree positivity certificates, nor by low-degree polynomial
calculus. Also [standard reductions; rests on E]: #k-SAT in 2^{o(n)} gives the permanent of 0/1 matrices with a
bounded number of ones per row and column, and the other bounded-degree counting problems with linear-size
reductions to #SAT, in time 2^{o(n)}. A circuit lower bound for E^{NP} follows from the failure of ETH by
Jahanjou–Miles–Viola 2015; the exact circuit class is to be verified.

## Open points, in order of promise

1. E(4): the rank-four structure constants in VIII's basis, with their a (item 5.4).
2. The decay of E e^{iπkW_n} for ζ, which gives density ½ of the labels (item 7.2).
3. The limit of the heat-flow path of extremal characters χ_t, t → ∞. If the zeros of H_t become an arithmetic
   progression on a growing window (Rodgers–Tao), the limit is the character of cos, with value
   2^{3ℓ}(1 − 2^{−2ℓ})ζ(2ℓ)/π^{2ℓ} on an ℓ-cycle (2/3, 8/15, …). For t < 0 the function is not positive definite
   (Λ = 0), and the order of the first failing minor tends to infinity as t ↑ 0.
4. The functional-equation question for ζ^sep_K, [K:Q] ≥ 2 (item 2.2).
5. Whether the units of item 8.5 (roots of Eulerian polynomials) generate the unit groups of their fields, and what
   the corresponding statement is for the zeros of ℘^{(m)} away from the cusp (Eichler–Zagier-type integrals).
6. The comparison of C-2 with Proposition G, and an explicit a_C for one Weil fourfold (C-1).

## Check by the main session (21 Nov ~17:5x UTC; Claude Opus 5.5 at effort max): item 3, Li-Toeplitz signature
Script: check_li_toeplitz_signature.py (mpmath, 50 digits; Li coefficients by λ_n = (1/(n−1)!) dⁿ/dsⁿ [s^{n−1} log ξ(s)] at s = 1). λ₁..λ₄ = 0.0230957089661, 0.092345735228, 0.207638920554, 0.368790479492 (match the known values). The Toeplitz sections (λ_{|j−k|}), λ₀ = 0, of sizes 2 to 11 each have exactly one positive eigenvalue and all others negative, as the consult states. The smallest |eigenvalue| falls from 2.3e-2 (size 2) to 7e-27 (size 9) and 1.3e-34 (size 11): sizes up to 9 are well above the working precision; sizes 10-11 need a higher-precision rerun before they count.
