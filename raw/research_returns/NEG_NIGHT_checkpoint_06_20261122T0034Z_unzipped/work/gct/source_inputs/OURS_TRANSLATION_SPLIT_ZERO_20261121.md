# The split-zero programme in standard terms (started 21 Nov 2026, 15:45 UTC)

By the main session (Claude Opus 5.5 at effort max). The user (P8837-P8841, ~15:4x UTC): translate the findings into
the format of what we already work on, so that anything new can be placed as a theorem in AG or analytic number
theory; "not ... finding what is already stated necessarily ... more just genuinely translating it and see what it
says".

Source of the corpus: `TO_SEND/PRO/_staging_20261121/sources54/OURS_split_zero_corpus/` (latest LaTeX of each paper,
copied from `Papors/Chatnotes/`). Numbers 01-16 below are its file prefixes. Statement extracts used:
scratchpad `extract_statements.py`.

Status marks:
- **[standard]**: a known fact; named, or proved here in a line.
- **[paper]**: proved in the user's paper; not re-proved here unless marked [checked].
- **[checked]**: verified here (a proof written here, or a computation with its script).
- **[new here]**: found in this translation, with its proof or check.

## 0. Dictionary

| The programme's term | Standard term |
|---|---|
| split-zero / globalization semiring G(R) = R ⊔ {τ} | R with an external zero adjoined (Golan); the comonad FU of the adjunction F ⊣ U, F = adjoin a zero, U = forget that morphisms preserve 0 (semirings → semirings without distinguished zero). Analogues: X ↦ X₊ (disjoint basepoint), Dorroh unitization with the zero in place of the unit |
| τ, "unsupported global zero" | the adjoined zero, additive identity and multiplicative absorber |
| 0_R, "supported arithmetic zero" | the old zero, now an idempotent e: e² = e = e + e |
| coordinate model D_R = {(0,0)} ∪ (R × {1}) ⊂ R × B | G(R) as the subdirect product {(x, b) ∈ R × B : b = 0 ⇒ x = 0} |
| Boolean pair A = {0_R, τ} ≅ B | the corner e·G(R); F₁ = {0, 1} with 1 + 1 = 1 (characteristic one) |
| p_R (τ ↦ 0) | the counit of F ⊣ U; also the ring completion of G(R) (the additive group completion of (G(R), +) is R) |
| χ_R (support, x ↦ [x ≠ τ]) | the B-point of G(R) at the generic point; G(R) is zero-sum-free and entire with respect to τ |
| support prime s_R = {τ} | the unique minimal prime: open, dense, residue semifield B (Frac G(R) ≅ B) |
| supported arithmetic zero prime z_R = {τ, 0_R} | the generic point of the closed subset V(A) ≅ Spec R |
| Spec G(R) | Spec R with a Boolean generic point glued on; G(R) = R ×_K G(K) (K = Frac R, R a domain): the characteristic-one form of the D + M construction / Milnor square, Spec G(R) = Spec R ∪_{Spec K} Spec G(K) |
| congruences ρ_J, ρ'_J ("doubled ideal lattice") | the two quotients R/J (τ collapsed into J: Bourne quotient) and G(R/J) = (R/J) ⊔ {τ} (τ kept apart: the based quotient) |
| classical (ideal) zeta sheet | Σ_{J≠0} |R/J|^{-s}: the Dedekind zeta ζ_K (R = O_K) |
| separated zeta sheet | Σ_{J≠0} (|R/J| + 1)^{-s}: counts the based quotients; over Z it is ζ(s) − 1 = ζ(s, 2) |
| the interpolation L_t = e^{-tD}L, D = s·T | the Hurwitz-type shift Σ a_n (n+t)^{-s} = Σ_k binom(−s, k) t^k L(s+k); over Z, ζ(s, 1+t) |
| jet formula ∂_t L_t(s) = −s L_t(s+1) | ∂_a ζ(s, a) = −s ζ(s+1, a) |
| quotient coordinate u = s(s−1), lift coordinate v = 2s−1 | the invariant and the anti-invariant of the functional-equation involution ι: s ↦ 1−s; v² = 1 + 4u; −u = s(1−s) is the Laplace eigenvalue, = 1/4 + γ² on the line |
| critical-line separation | an ι-invariant (anti-invariant) function real on R is real (imaginary) on Re s = 1/2, the fixed locus of s ↦ 1 − s̄ (Hardy's Z-function mechanism) |
| primitive defect −Σ : Z^r → Z | the negative augmentation; its kernel is the root lattice A_{r−1} |

## 1. The construction (globalization note; "Error correction and review (12)", appendix B)

1. G(R) is a commutative semiring; p_R and χ_R are semiring maps; (p_R, χ_R) embeds G(R) in R × B. [paper] [checked]
2. Ideals: {τ} and J ∪ {τ} for J ◁ R. Primes: {τ}, and P ∪ {τ} for P ∈ Spec R. {τ} is the generic point; Spec G(R)
   is irreducible; Spec R is the closed set V(A), not an open dense subset (review A.4 corrects an earlier claim).
   [paper] Standard reading: the ideal lattice of R with a new bottom element; Spec R with a new generic point.
3. Congruences: exactly ρ_J and ρ'_J; quotients R/J and G(R/J). [paper]
4. Localization: M^{-1}G(R) = G(M^{-1}R) for 0 ∉ M; localizing at all of R gives B. [paper] Standard reading: the
   residue semifield at the generic point is B; at the other points it is the residue field of R.
5. Hom(G(R), A) = Hom(R, A) for every ring A (review B.4); Hom(G(R), G(R')) = Hom(R, R') for nonzero R, R' (B.5);
   so G(R) ≅ G(R') iff R ≅ R'. [paper] Standard reading: G is fully faithful on nonzero rings, and every map to a
   ring factors through the ring completion p_R (additive cancellation forces f(0_R) = 0).
6. No unital map B → G(R): 1 + 1 = 1 would force 2 = 1 in R. [paper] [checked]
7. Cl(G(O_K)) ≅ Cl(K) and ζ_{G(O_K)} = ζ_K. [paper] Standard reading: invariants defined through the finite-norm
   ideals J ∪ {τ} (J ≠ 0) see only the Bourne quotients O_K/J, so they factor through p.
8. The multiplicative monoid (Deitmar's F₁ side) has an infinite-dimensional prime spectrum, not homeomorphic to
   Spec G(Z); the contracted monoid algebra splits as a product. [paper] Standard reading of the splitting: the
   idempotent e = [0_R] splits the monoid algebra, e·Z₀[M] ≅ Z.

## 2. The defect strand (03 split_zero_defect_preprint, 04 primitive_support_defects_preprint)

The papers' unifying map is the negative augmentation δ = −Σ : Z^r → Z, kernel A_{r−1}. The instances:

1. **Support linearization** (03 §4, 04 §2): the composite G(R)^I → B^I = P(I) → Z^I → Z, J ↦ −|J|; its kernel is
   A_{|I|−1}. [paper] Standard reading: the B-point χ_R coordinatewise, then the counting measure.
2. **Rank/dimension characters** (03 §3): K₀(C(Y)) with rank, R(G) with dimension, a pointed fusion category with FPdim,
   Z[C_r] with augmentation; the kernel for r dimension-one simples is A_{r−1}. [standard]
3. **Semilocal crossed products** (03 §7, 04 §5; Connes-Consani's visible semilocal models): the K-theory boundary map
   sends each finite-prime boundary class and each archimedean sector class [p_±] to −1; for S = {p, ∞} the triplet
   has defect −3 and kernel A₂; K₀(A_S) ≅ Z^{n+1}, K₁(A_S) ≅ Z^n. [paper] Standard reading: index maps of
   Toeplitz-type extensions (Morita: I_p ~ C₀(R), Q_p ~ C(S¹)); −1 per generator is the orientation convention.
4. **Cyclic and Eisenstein** (03 §8, 04 §8): the augmentation ideal of Z[C₃] is A₂; Z_{A₂}(s) = 6·2^{-s}ζ(s)L(s, χ₋₃)
   = 6·2^{-s}ζ_{Q(√−3)}(s). [standard]
5. **Weyl operators** (03 §9, 04 §6): the clock-and-shift (generalized Pauli) matrices W_{a,b} form a basis of M_r(C);
   the non-identity ones span sl_r. [standard]
6. **CUE** (03 §10, 04 §9): E_{U(N)}|Λ'(1)|² = Σ_{m≤N} m² (orthonormality of the characters of ∧^j). The derivative
   moment exponent s² + 2s (Hughes; Conrey-Rubinstein-Snaith; Dehaye) equals dim sl_{s+1}, matched by
   End(W) ⊕ W ⊕ W^∨ ≅ sl_{s+1} (the Levi and the two nilradicals of a maximal parabolic). [standard] The match is a
   dimension count; a structural cause is not given.
7. **Stone endpoint algebra** (03 §6): X = {ξ₁, ξ_*} is the multiplicative monoid of B (= F₁ with its zero); functions on
   X with Δf(x,y) = f(xy). a_λ = u + λv is a character of X iff λ ∈ {0, 1}; the defect is (λ − λ²)v⊗v. Pulled back
   along n ↦ [n = 1] it gives c_λ = (1−λ)δ₁ + λ·1 and Z_λ = (1−λ) + λζ, whose failure of multiplicativity on coprime
   pairs is (λ − λ²) times C(s,t) = ζ(s)ζ(t)/ζ(s+t) − ζ(s) − ζ(t) + 1. [standard] [checked] (C(0,0) = 3/2; D₂(0,0) = −3.)
8. **Shioda-Tate** (03 §12): ρ(X) = 2 + Σ_v rk Φ_v + rk MW. [standard]
9. **The critical-line piece** (03 §5): Λ_t(s) = π^{-s/2}Γ(s/2)ζ(s, 1+t) has residues −1−2t at 0 (= −2B₁(1+t)) and
   1 at 1; its polar part is (1+t)/u − t·v/u. The anti-invariant coefficient −t = ζ(0, 1+t) − ζ(0) measures the first-
   order failure of the functional equation s ↦ 1−s. [paper] [checked] On the line, invariant parts are real and
   anti-invariant parts imaginary. [standard]

**What this strand gives together with the zero motion of 21 Nov (checked; elementary: consult ad855737 calls it
one-line implicit differentiation, not to be presented as new; what is specific here is that the off-line driver is
the anti-invariant defect the user's §5 isolates).** Let Λ₀ be the completed zeta,
Z(γ) = Λ₀(1/2 + iγ) (real), Φ = ∂_tΛ_t|_{t=0} = −s·π^{-s/2}Γ(s/2)ζ(s+1), and Φ_± = (Φ(s) ± Φ(1−s))/2. For every simple
zero ρ = 1/2 + iγ:

  Re ρ'(0) = Im Φ₋(ρ) / Z'(γ),    Im ρ'(0) = −Φ₊(ρ) / Z'(γ).

Proof: ρ' = −Φ(ρ)/Λ₀'(ρ) and Λ₀'(ρ) = −i Z'(γ); Φ₊(ρ) is real and Φ₋(ρ) imaginary by critical-line separation.
Checked on the first 200 zeros: relative error below 10⁻²⁶ for both parts (`antiinvariant_drives_offline.py`).

So the invariant part of the deformation moves a zero along the critical line, and the anti-invariant part, which
03 §5 isolates as the defect, moves it off. The Boolean label of BOOLEAN_LABEL_OF_ZEROS_20261121.md is
sign(Im Φ₋(ρ)/Z'(γ)): the anti-invariant defect evaluated at each zero. The same holds for any one-parameter
deformation of a self-dual L-function with real coefficients; the label is defined wherever the zero is simple.

What the strand says, translated: one integer-valued character (the augmentation) recurs across K-theory, fusion,
lattices and random matrices; the instances are standard. The split-zero contribution is its support-theoretic origin
(item 1) and the critical-line decomposition (item 9), which now connects to the zero dynamics above.

## 3. The algebra of G(R) beyond the baseline (01 secondary note, 02 repair dossier, 12 §2)

1. **Semimodules = Clifford monoids with R-linear fibres.** For a G(R)-semimodule M, (M, +) is a commutative inverse
   (Clifford) monoid: m + (−1)m = em is an idempotent and m + em = m. Clifford's structure theorem (a strong
   semilattice of abelian groups; Clifford 1941, Howie Thm 4.2.1) gives M = ⊔_{l ∈ eM} M_l over the join-semilattice
   eM, with structure maps T_{l,l'}; R acts on each fibre. The papers' equivalence G(R)-SMod ≃ Diag_R (functors from a
   join-semilattice with 0 to R-Mod) is this theorem with the R-linear structure added. [paper] Standard reading [new
   here]: Clifford's theorem.
   - Cancellative semimodules = R-modules (a Clifford monoid is cancellative iff it is a group). [paper; standard]
   - G(R)^n has skeleton the Boolean lattice P([n]) with fibres R^I. [paper]
   - f.g. projective semimodules ↔ finite posets J with f.g. projective R-modules Q_j (U ↦ ⊕_{j∈U} Q_j on order
     ideals). [paper (02)]
   - M ↦ eM is base change along χ_R (left adjoint of restriction); M ↦ ker ε_M is coinduction along p_R. [paper]
2. **Products.** G(A × B) ≅ G(A) ×_B G(B). [paper] Standard reading [new here]: Spec G(A × B) is Spec A ⊔ Spec B with
   one Boolean generic point joining them; G makes every spectrum irreducible.
3. **Reconstruction.** G(R) = N[M_S] / ([a]+[b] = [a+b], [x]+[τ] = [x]). [paper] Standard reading: G(R) is the
   semiring of a blueprint in Lorscheid's sense, with these pre-additions.
4. **Universal properties.** R is the universal ring quotient (ring completion); χ_R is the unique map to B; no section
   R → G(R) of p_R; Aut G(R) = Aut R. [paper]
5. **Factorization.** Units and nonzero irreducibles are those of R; e = 0_R is divisibility-prime but reducible
   (e = e·e), so G(R) is not a UFD-type semiring. [paper]
6. **Ideals and the norm.** I_J I_K = I_{JK}; class monoid unchanged. A multiplicative ideal norm extending N must
   vanish on {τ} and on {e, τ} (scalar norm collapse). [paper]
7. **The separated weight.** w(J) = N(J) + 1 is not multiplicative. [paper] Standard reading [new here]: w is the
   cardinality of the based quotient (R/J)₊. For coprime J, K the product theorem gives G(R/J × R/K) =
   G(R/J) ×_B G(R/K), the smash product of the based quotients, so w(JK) − 1 = (w(J) − 1)(w(K) − 1). The
   multiplicative object is w − 1 = N: the separated sheet is Eulerian for the smash product and non-Eulerian for the
   cartesian product.
8. **Erdős-Straus certificates** (02 §12): G(N) records "count = 0" as τ against positive counts; the criterion is the
   ordinary existence statement. [paper] Notational.
9. **Coprimality matrices** C_q^+ (indicator of gcd = 1) unimodular exactly for q ≤ 3. [paper] Not rechecked.

## 4. The deformation (01 §5-8, 02 §14, 12 §3-5)

1. L_t = Σ_m (−1)^m (s)_m/m! t^m L(s+m) = e^{−tD}L; ∂_t^n L_t = (−1)^n (s)_n L_t(s+n); semigroup law. [paper]
   Standard: the binomial series of (n+t)^{−s}; for L = ζ, ζ(s, 1+t).
2. Pole rigidity: L_t has only the pole at 1, with the same residue. [paper] [checked] ((s)_m vanishes at the pole
   1 − m of L(s+m).)
3. Logarithmic cumulants: the partition (Faà di Bruno) formula. [standard]
4. ζ(s+r)/ζ(s) = Σ α_r(n) n^{−s}, α_r(p^k) = −(p^r − 1)p^{−rk}; ∂_t log ζ_t|₀ = −s Σ α₁(n) n^{−s},
   α₁(n) = (−1)^{ω(n)} φ(rad n)/n. [paper] [checked] Same over number fields.
   - **New here: the residue of the first log jet at a simple zero is minus the zero's velocity**,
     Res_ρ ∂_t log L_t = ∂_tL(ρ)/L'(ρ) = −ρ'(0). So for a test function h,
     Σ_ρ h(ρ) ρ'(0) = (1/2πi)∮ h(s) s ζ(s+1)/ζ(s) ds,
     and on Re s > 1 the integrand is s Σ α₁(n) n^{−s}: an explicit formula for the zero velocities, of the type
     Gonek and Hejhal use for Σ 1/ζ'(ρ). It is the route to the mean and the distribution of the Boolean labels.
5. Hurwitz package: F_t(−m) = −B_{m+1}(1+t)/(m+1); F_t'(0) = log Γ(1+t) − ½ log 2π (Lerch); D_q(−m) = Σ_{n≤q} n^m
   (Faulhaber); e^{−D_q'(0)} = q!. [standard]
6. Non-Eulerianity for 0 < t < 1 (frequencies log(n+t)); at t = 1, ζ − 1 has a₁ = 0. [paper] [standard]
7. The two-sheet family 𝒵_{1,u} = (1+u)ζ − u, coefficients c(1) = 1, c(n) = 1+u. [paper] Standard reading [new here]:
   at u = 1 it is 2ζ − 1 = ζ(s) + ζ(s, 2), the zeta of all finite quotients of G(Z) (both congruence families). Its
   zeros are the 1/2-points of ζ; in general the zeros of 𝒵_{1,u} are the a-points ζ(s) = u/(1+u) (Bohr-Landau-
   Littlewood; Levinson 1975: almost all lie near the line; Garunkštis-Steuding on their asymmetry). In u, a zero
   moves with velocity 1/ζ'(ρ) at u = 0.
8. **Zero motion** (12, Thm zero-motion): for a compactly supported μ, the zero of Z_{μ,t} = ∫ζ(s,1+ty)dμ(y) through a
   simple ρ is ρ + Σ c_N t^N with an all-order recursion; c₁ = m₁(μ) ρζ(ρ+1)/ζ'(ρ); c₂ explicit. [paper] The
   velocity of 21 Nov is this c₁ (μ = δ₁). New here: its sign and its split (section 2).
9. Hurwitz's theorem gives zero-count convergence for Bernstein approximants of μ. [paper; standard]

## 5. The zeta-divisor sheaves (05, 07, 08, 09)

1. F₁(ρ) = −1 at every zero; −1 is the unique unit of order 2 in G(Z); Fix(−1) = A ≅ B. For a domain R,
   Fix_{G(R)}(u) = {τ} ∪ Ann_R(u − 1). [paper]
2. V_D(U) = Π_{x∈U∩|D|} A^{m_x}, A_D(U) = Π A: products of skyscraper sheaves of Boolean cubes; A_D is a split retract
   (join and diagonal); V_D ≅ A_D iff all multiplicities are 1. [paper] Standard reading: the divisor D as a sheaf of
   B-modules; "V_ζ ≅ A_ζ" is the simple-zero conjecture restated.
3. Jets: O_x/m^m has the chain of ideals C_m; C_m ⊂ B_m = P([m]) as terminal segments, with L ⊣ i ⊣ R. [paper; standard
   order theory] The class of f in O_x/m^{m+1} generates the minimal ideal, coefficient f^{(m)}(x)/m!. [standard]
4. Tails: for j: C → P¹, (j_*F)_∞ = Π M_x / finite modification; 0 → j_! → j_* → i_{∞*}Tail → 0. [standard]
5. Packets: the Klein four group ⟨s ↦ s̄, s ↦ 1−s⟩ acts on the zeros of ξ; orbits of size 2 on the line, 4 off it;
   the sheaves descend to the orbit space; λ_{1−ρ} = (−1)^m λ_ρ, λ_ρ̄ = conj λ_ρ. [standard]
6. Analytic completion (08): Hadamard product of Ξ(z) = ξ(½+z) over sign pairs; packet polynomials (quadratic on the
   line, quartic off it); **RH ⟺ no quartic packet factor**; Taylor coefficients of ξ at ½ are (−1)^n σ_n(α^{−2});
   packet-grouped ζ'/ζ. [standard] Standard reading: Pólya's form of RH (Ξ(iz) has only real zeros, the
   Laguerre-Pólya class); the Taylor coefficients at ½ are those of the Jensen-polynomial programme (Pólya;
   Griffin-Ono-Rolen-Zagier 2019).
7. Spectral coordinate (09): Φ(s) = i(s − ½) sends zeros to the Connes-Consani spectral divisor (ζ(½ − iz) = 0);
   −ρ(1−ρ) = −Φ(ρ)² − ¼; critical zeros ↔ real z; ζ-cycles of length 2π/|γ|. [standard + Connes-Consani]
8. Trivial zeros: ζ'(−2n) = (−1)^n (2n)!/(2(2π)^{2n}) ζ(2n+1). [standard]

What this strand says, translated: the zero divisor of ζ, its multiplicities and its functional-equation symmetry,
written as sheaves of Boolean cubes; the analytic content is classical (Hadamard, the functional equation, Pólya). The
papers state that the pointwise shadow is constant and look for a refinement. **The Boolean label of section 2 is such
a refinement: a non-constant global section of A_ζ over the simple zeros, invariant under conjugation, hence a section
of the packet sheaf.**

## 6. CUE-Hurwitz (12; 13 and 14 below)

1. Principal part of Λ_{μ,t}: (1 + t m₁)/u − t m₁ v/u; the finite residue defect −2t m₁ is cancelled by +2t m₁ at ∞
   (d log u has residues 1, 1, −2). [paper; standard: the residue theorem on P¹]
2. Residue parity reversal: ι^*(f ds) = −f(1−s) ds, so invariant functions have opposite residues at 0 and 1 and
   anti-invariant ones equal residues. [standard]
3. CUE derivative observables X = |Φ_N^{(a)}(1)|² are bounded, so their Haar push-forwards are compact measures and
   enter only through their moments m_n = E X^n; E|Φ_N'(1)|² = N(N+1)(2N+1)/6; exact N = 3 moments 14, 375, 15510,
   847280, 55331424. [paper] The CUE enters the zeta side only through these moments.
4. GMS exponent |μ| + |ν| + s² = dim(End(C^s) ⊕ J_μ ⊕ J_ν^∨); for μ = ν = (1^s) this is sl_{s+1}. [paper] A dimension
   count (section 2, item 6).
5. Weyl-Heisenberg basis of sl_r; A_{r−1} as the diagonal augmentation lattice inside it. [standard]
6. N = 3 trace algebra R[u,X,J]/(J² + S): the ±1 eigenspaces of an involution, orthogonal for the trace form.
   [paper; standard]

## 7. The ETH reduction in split-zero terms (the user's question, 21 Nov, between 15:50 and 16:32 UTC)

Source: OpenAI, "The Exponential Time Hypothesis is False" (25 Oct 2026), `sources54/LIT_OpenAI_ETH_is_False/
main_full_version.tex`, §6 (Lemma sparse-checks, Lemma greedy-hashes, eq. hash-query).

1. **The word "support" there** is Hamming support: the set of nonzero coordinates of the violation vector
   v(x) ∈ F₂^m (§6.1: a Tanner-code matrix A⁽⁰⁾ "rejects every nonzero violation vector with small support"), and the
   entries of a low-degree matrix polynomial f(W₀) (§2.7: "low degree gives restricted support"). In split-zero terms
   that is the value-nonzero predicate p(x) ≠ 0, not the support predicate x ≠ τ; the two differ exactly at 0_R.
2. **The exact relation** [new here; checked by hand against §6]. G(F₂) = {τ, 0, 1} = {(0,0), (0,1), (1,1)} ⊂ F₂ × B, and
   ⊕ is (XOR, OR). Lift each violation bit to 1 (violated) or τ (satisfied). The ⊕-sum over a test row is τ (no
   violated clause in the row), 0_R (an even number ≥ 2, cancelled), or 1 (an odd number). Then:
   - x passes row i (P_i(x) = 0 over F₂) ⟺ its row value lies in p⁻¹(0) = {τ, 0_R} = A, the Boolean pair;
   - x satisfies F ⟺ every row value is τ (every clause lies in some row);
   - the paper's error term D(A) = N(A) − #F counts the assignments whose row vector lies in the Boolean cube A^rows
     but off its bottom vertex τ^rows: rows where violations cancelled to the supported zero.
   §6 removes them: the Tanner code excludes violation vectors of small Hamming weight, and 3n rows chosen by
   conditional expectations (each candidate scored by a common-zero count) give N(A) = #F.
3. **The mechanism, stated in the framework** [new here; a formulation]: on the set being counted, choose ring-side
   tests (which cancel) so that no supported zero occurs: p(x) = 0 ⇒ x = τ. Then the ring computation answers the
   support question exactly. The algorithm itself runs entirely in the ring coordinate (interpolation over Q of
   counts of F₂-zeros); the B coordinate cannot count (1 + 1 = 1).
4. **Where a transfer could do work** [open]. Only where support information is hidden behind cancellation:
   - On the zeta sheets, nothing to recover: the separated sheet is determined by the classical one (same a_n), and the
     τ-class is present in every quotient.
   - In GCT the same split is the central issue: positivity or nonvanishing of a structure constant is a support
     statement, its formulas are alternating sums. Purity (GCT VII-VIII, Weil II; the GCT_NSRH route) excludes
     cancellation by putting everything in one weight; §6 of the ETH paper excludes it combinatorially (codes and
     many counted tests). Whether a §6-type family exists for a GCT structure constant is open; no construction here.
5. **Consequence for item 10(a) of prompt 54** [new here; from the classification of section 3]: coefficients in
   G(R)-semimodules are R-coefficients on fibres over a Boolean skeleton. So the analytic part of any purity statement
   with such coefficients is the ordinary one, fibre by fibre; the new content sits in the skeleton, which is this
   support (OR) coordinate.

## 8. The two dual conditions: no supported zeros, no unsupported elements (the user, 21 Nov, between 15:50 and 16:32 UTC)

The user: "what about if you say the support is at no unsupported as opposed to no supported". Agreed first: "no
supported zeros" (nothing lands on 0_R) is what the ETH refutation's §6 already does; restating it adds nothing.

"No unsupported" (χ ≡ 1: nothing lands on τ) [readings new here; the facts used are standard]:
1. **Counting.** χ ≡ 1 on a witness sum means witnesses always exist: a total search problem. If moreover the F₂-count
   is 0, the sum is a supported zero, so there are at least two witnesses. This is the parity principle behind PPA
   (Papadimitriou 1994) and exactly Chevalley-Warning: the number of common zeros is ≡ 0 mod p, the trivial zero makes
   the count supported, so a nontrivial zero exists (Ax-Katz sharpens the congruence: the parity route of prompt 54).
   ETH uses the absence of 0_R to detect existence; Chevalley-Warning uses its presence to prove existence.
2. **ETH §6 uses both, in order.** After the Tanner code, every nonsatisfying survivor violates at least m/P clauses
   ("this lets a short random test catch each such assignment with constant probability", before Lemma
   greedy-hashes): a short random row is supported with constant probability, and parity then rejects. So §6 first
   makes rows supported, then excludes supported zeros.
3. **GCT.** Occurrence is support. Bürgisser-Ikenmeyer-Panova (J. AMS 32 (2019), "No occurrence obstructions in
   geometric complexity theory"): in the relevant range, every irreducible occurring in the coordinate ring of the
   padded permanent's orbit closure occurs in the determinant's (for n ≥ m^{25}). The determinant's multiplicity
   function has no unsupported entries on the permanent's support [corrected by consult a0805369: not "everywhere"],
   so occurrence obstructions (supported on one side, τ on the other) cannot exist, and only multiplicity
   obstructions (both supported, values compared) remain. After BIP, GCT lives on the supported sheet, where section
   3's classification makes G(R)-structure ordinary R-module structure; the framework's own content can act there only
   through supported zeros, i.e. cancellation in the multiplicity formulas: canonical-basis positivity (PH0 in GCT VI)
   and PH1 (a cancellation-free formula that also counts points of a polynomial-size polytope; its homogeneous form
   refuted by Kahle-Michałek), item 10(b) of prompt 54. [PH labels corrected by consult a0805369: "no supported zeros"
   alone is trivial, since exponential-size cancellation-free formulas exist.] The consult also found that on P-F57's
   cubic family the plethysm count is a near-supported zero of its pole expansion: terms of size about 2^{n⁴/24} cancel
   down to a small count; P-F57 broke GCT VI's saturation certificate, not the support question (the support is
   eventually full beyond a polynomial threshold: P-F54, P-F62, statement level), and SH(b) is untouched.

## 9. Computing in G(R) with the predicate "≠ τ" (the user's proposal, 21 Nov, between 15:50 and 16:32 UTC)

The user: take the whole of G(R) as the space, and read answers by "≠ τ" (allowing 0_R) instead of "≠ 0"; ETH would
then be one case of a broader question in which P vs NP could be posed, defined by the τ programme, not heuristically.

Definitions and facts [new here, elementary; the cited lower bounds are standard]:
1. A G(R)-circuit (gates ⊕, ⊙; constants in G(R)) evaluated in D_R ⊂ R × B computes a pair: an R-circuit (τ ↦ 0)
   and its Boolean shadow, the monotone circuit with ⊕ ↦ OR, ⊙ ↦ AND, every constant in R ↦ 1. The shadow is 1 where
   some formally generated monomial is supported, including monomials that cancel in R. Where the R-value is 0 and the
   shadow 1, the output is a supported zero 0_R.
2. Reading the answer by "≠ τ" reads the shadow alone: a circuit decides f this way iff its shadow equals f. So the
   "≠ τ" world is monotone computation. For a monotone Boolean f (inputs 1 ↦ 1, 0 ↦ τ in G(F₂); OR = x ⊕ y ⊕ xy):
   - size of G(F₂)-circuits for f with no supported zeros = Θ(monotone circuit size of f);
   - size of G(F₂)-circuits for f, supported zeros allowed = Θ(Boolean circuit size of f).
   The gap between monotone and general complexity is exactly the use of supported zeros.
3. In the "≠ τ" world the separations are theorems, for problems in P as well: bipartite perfect matching needs
   n^{Ω(log n)} monotone circuits (Razborov 1985), CLIQUE exponential ones (Alon-Boppana 1987), and some monotone
   function in P needs exponential monotone size (Tardos 1988). Even det_n is outside VP(G(R)): its shadow is bipartite
   perfect matching, every term ±Π x being supported. So this world's "P vs NP" is decided, by the absence of
   cancellation, and does not reach the ring question.
4. The way back is the supported zero. Given the exponential monotone bound for CLIQUE:
   CLIQUE ∈ P/poly ⟺ supported zeros give exponential savings for CLIQUE.
   PM and Tardos's function show such savings exist for some monotone functions, so a proof that they do not exist for
   CLIQUE must use CLIQUE's structure. ETH's refutation is an instance where supported zeros give large savings
   (cancellation over Q and F₂ in the counting engine), removed at the end (§6) to read off #F.
5. So the broadened category splits P vs NP into its monotone part (proved) and the power of supported zeros (open, and
   equivalent to the classical question). The framework names that open part exactly; it does not by itself supply a
   handle on it.
6. Where supported zeros are known to be cheap to remove: slice functions (f = 0 below weight k, 1 above). Berkowitz
   (1982): their monotone and general circuit sizes are polynomially related (¬x_i is replaced by the monotone
   threshold "at least k among the other variables"). In this language: on slices, supported zeros can be eliminated
   at polynomial cost. Hence an exponential monotone lower bound for an NP-complete slice function (a slice of CLIQUE)
   would give NP ⊄ P/poly. This is the known route, and the place where the "no supported zero" condition costs
   nothing; Razborov's approximation method does not reach slice functions.

## 10. The July thread (Papors/Chatnotes/transcripts; first pass, 21 Nov, before 16:32 UTC)

Read so far: SplitZero.lean, nullity_adjunction_audit.py, the prompts of the first transcript, the statements of
zeta_projective_infinity_k4.tex and cumulative_nullity_k4_ledger.tex. Pending: full_noncommutative_k4_operation,
giuga_blind_plane_cayley_dickson, the Toeplitz notes, modular_cartan_realform_bridge, the illustrated atlas's claim
contract, the long transcripts. Files prefixed jt_ are JT's material: used where useful, always cited as JT's (the
user, 21 Nov: "use JT material just to keep track of which is which, and keep the citation clear").

1. **The nullity adjunction is the user's own (10 Jul 2026):** 𝔷 ⊣ U between zero-forgotten rigs Rig^{¬0} and rigs;
   G = 𝔷U; counit identifies e with τ; Lean formalization SplitZero.lean (CommSemiring instance, e + e = e, the ring
   reflection, hom_kills_e, Fix(u) = {τ} ∪ Ann(u − 1)). Section 0's "comonad" entry is this adjunction.
2. dim G(A) = dim A + 1 [ledger] = the Boolean generic point of section 0 adding one to every maximal chain.
3. Mixed double D_A = G(A) ⊕ G(A), (a,b)⋆(c,d) = (ac − bd, ad + bc): the Gaussian double with each leg separately
   absent or present; Boolean support shadow in B[C₂] (absent, first leg, second leg, both); dim D_A = dim A + 2;
   dim D(G(R[x,y])) = 4 ("K = 4 candidate", existence only). [ledger]
4. **Binary nullity, ternary recovery** [ledger; checked]: in a unital nonassociative algebra with x² = −λ·1, on the
   right annihilator N_x = {z : xz = 0}, −λ^{-1}[x,x,z] = z, since (xx)z = −λz and x(xz) = 0. Associative (indeed
   alternative) algebras have N_x = 0 for such x; the sedenions do not (explicit pair with XY = 0, X² = Y² = −2, an
   annihilator the ledger gives as 8-dimensional "in the tagged algebra"; consult a157422a computes dimension 0 or 4
   for x = e_i ± e_j in the standard sedenions, which matches the known 4-dimensional annihilators of sedenion zero
   divisors: the 8 is to be checked against the ledger's tagged algebra). In split-zero terms: x ⊙ z = e is a supported zero of multiplication that keeps its
   content z, recoverable by the ternary operation; τ keeps none.
5. zeta_projective_infinity_k4 [standard facts, assembled]: ζ: C → P¹ with ∞ only at s = 1 (simple); 1/ζ a normalized
   uniformizer; ord₁ the unique such valuation; oriented blow-up degrees ±1; Hermitian Lorentz space and its null
   cone (Dir(0) = ∅ at the apex); the Bloch/Riemann-sphere projector P(w), P₀P_∞ = 0; Hopf lift; the essential
   singularity at s = ∞ gives the whole P¹ as graph-closure fibre (Casorati-Weierstrass); the functional equation as a
   Klein four action on the centered sphere; RH ⟺ every zero on the great circle X_s = 0 (restatement); KP¹ ≅ S^n and
   the Hopf fibrations for K = R, C, H, O; zero divisors break regular coefficient lines at the sedenions; the "pole-
   valued recovery" pord₁(f)·(−κ^{-1}[x,x,·]) (a homomorphism times a fixed endomorphism: I(1) = 0, I(ζ) = id).
6. Literature items in the ledger: Terzo's exponential-ring theorem under Schanuel's conjecture; Ford circles;
   Carathéodory-Fejér (a singular PSD Toeplitz kernel polynomial has unimodular zeros); Shioda-Tate; (Z/24)^× ≅ (Z/2)³.
   The ledger itself marks the Schanuel-Riemann bridge and the global fourth layer as open problems.

## 11. The shape between the lines (the user, 21 Nov, before 16:32 UTC: "continue looking for the shape between the lines")

Reading [an organizing reading, not a theorem]. The configuration the corpus keeps building is: a canonical structure;
its supported zeros (present, evaluating to zero), kept distinct from absence (τ: no element, no direction, empty
origin); that locus is small, often one line; and either it carries zeros onto a symmetric locus, or the next
operation turns it into an identity. Each instance below is exact:
1. G(R): e is present with value 0; τ is absent; χ records presence.
2. The Lorentz form det on Herm₂(C): its supported zeros are the null cone minus the apex, each with a direction in
   S² = P¹; the apex has Dir = ∅. ζ(s) is encoded as a null vector N_ζ(s) whose direction is its value; zeros go to
   P₀, the pole to P_∞.
3. A PSD Toeplitz form of corank one: its supported zeros are one line, and that line's polynomial has all zeros on
   the unit circle (Carathéodory-Fejér). The continuous analogue the ledger points at: Connes-Consani-Moscovici's
   minimal eigenvectors of the Weil form on finite intervals, whose Fourier zeros numerically match the zeta zeros
   (Weil positivity ⟺ RH).
4. The exponential: the supported zeros of E − 1 are the periods, a rank-one lattice Z·2πi (the "one relation"
   e^{iπ} + 1 = 0 of the Terzo item).
5. A nonassociative algebra: the supported zeros of L_x are the annihilator N_x; the associator is the identity on it.
6. The pole of ζ: 1/ζ turns it into a simple zero; ord₁ counts it (the 0/1 law pord(1) = 0, pord(ζ) = 1).
7. The zeros of ζ: the Boolean label of section 2 is the side to which the zero tips when the s ↦ 1−s symmetry is
   broken, i.e. the anti-invariant part of the deformation at the zero.

In standard terms, the configuration is the one behind Weil positivity and the Connes programme: positivity confines
the supported zeros of a canonical form to a minimal null direction, and that direction carries real zeros. The
typing τ ≠ e separates "no direction" (the apex) from "the null direction" (the kernel line), which standard language
writes alike. Against sections 8-9: RH-type rigidity comes from supported zeros confined by positivity; computational
power comes from supported zeros left free (cancellation). The two lines the user works on are the two regimes of the
same object. ~~No theorem here connects them.~~ Corrected at the user's word (21 Nov, before 16:32 UTC: "except the
generalized Riemann theorem which you can work back from since, you know, it's proved"): see section 12.

## 12. The S6 "higher Euler identity", and GRH as the bridge (21 Nov, before 16:32 UTC)

**A relation of Euler type in S6 Paper I** [the main session's identification; the user, 21 Nov 17:0x UTC: it is not the relation they remembered, which is still to be found; the reading below is the main session's idea, not invalid] (S6 series Paper I, Proposition fam:src:C.1.1 "The normalized theta period",
deposit_cp10/S6_series_I.tex): μ is a zero of the Weierstrass function, ℘(μ, τ) = 0 (Prop. inv:A2.3, citing
Duke-Imamoḡlu 2008, Thm 1, eq. (5)); at the cusp, sin²(πμ₀) = 3, equivalently u² + 10u + 1 = 0 for u = e^{2πiμ₀}, and
  e^{2πiμ₀} = −(5 + 2√6),  μ₀ = ½ − i·log(5 + 2√6)/(2π).
[paper] Readings [new here; the cusp constant is classical]:
- 5 + 2√6 = (√2 + √3)² is the fundamental unit ε of Q(√6) (norm 1; Pell x² − 24y² = 1). Euler's identity says the
  half-period goes to the torsion unit, e^{2πi·½} = −1; this says the same half-period, displaced vertically by the
  regulator log ε /(2π), goes to −ε. Euler's identity with the torsion unit replaced by sign × fundamental unit; and
  of degree two in u (u² + 10u + 1 = 0) where Euler's is (u + 1)² = 0 (sin² = 1).
- It is the cusp value of the Eichler-Zagier formula for the zeros of ℘ (Math. Ann. 258 (1982) 399-407):
  z_± = ½ ± [log(5+2√6)/(2πi) + 144πi√6 ∫_τ^{i∞} (t − τ)Δ(t)/E₆(t)^{3/2} dt].
- **Euler's identity and this one are factors of one Eulerian polynomial** [consult a157422a, item 8; its script reproduces it]: A₄(u) = 1 + 11u + 11u² + u³ = (u + 1)(u² + 10u + 1). The factor u + 1 vanishes at u = e^{2πi·½} = −1 (Euler); the factor u² + 10u + 1 at u = e^{2πiμ₀} = −(5 ± 2√6) (the cusp zero of ℘). The zeros of the derivatives of ℘ at the cusp are roots of Eulerian polynomials, all real negative, on Re z = ½ (℘″: 2 ± √3, from A₃ = 1 + 4u + u²); sin²(πμ₀) = 3 = −1/(4ζ(−1)).
- The shape of section 11 again: ℘(v) = ℘(1 − v), so Re v = ½ is ℘'s fixed line; for rectangular lattices (τ = iT)
  the paper proves exactly one zero on it (℘ real there, a sign change, no critical point); off the imaginary axis
  the zero leaves the line, and the Eichler-Zagier integral is the exact motion. At the cusp the zero is pinned by
  a unit and its regulator.

**GRH as the bridge between the two regimes** [the instances are standard theorems; the reading is new here]. In the
known GRH-based complexity theorems, GRH is used exactly to let counts decide support:
- Koiran (J. Complexity 12 (1996)): HN ∈ AM under GRH. A system with no complex point has points mod p only for the
  primes dividing a nonzero certificate (few); a system with a complex point has points mod p for a positive density
  of primes, and effective Chebotarev under GRH makes that density visible among primes of polynomial bit length. So
  the support over C (τ or present) is read off from the counts of supports mod p; GRH keeps the error terms (zeros
  off the line would be the cancellation) below the gap.
- Bürgisser (TCS 2000): #P ⊄ P/poly ⇒ VP ≠ VNP over C, under GRH, by the same passage to good primes (one direction).
- Deterministic number-theoretic algorithms (nonresidues, factoring over F_p) use it the same way.
With GRH a theorem here (A for the abelian case, M beyond it, M's defect table pending), these hold unconditionally
within that scope; the project records "HN ∈ AM under M" as CX-K02. Item 10(c) of prompt 54 ("what GRH forces on
the attached Boolean structure") has Koiran's theorem as a known instance: GRH forces the support pattern of the
reductions mod p to decide the support over C at polynomial scale.

**Corrections to section 12 (consult af2a18f6, Claude Opus 5.5 at effort high, 21 Nov ~16:4x UTC;
consults/CONSULT_af2a18f6_GRH_BACKWARD.md):** Koiran's input is the prime ideal theorem for the zeta function of one
solution field E (no Galois closure), so M-scope; the "few primes" side is unconditional; GRH is needed for the range
of primes, not for the density; "read off" means approximate counting. Section 14's "no unsupported small window"
holds for initial windows, not arbitrary short windows, and is A-scope only when L/Q is abelian. In AG terms
(consult Q1′): Koiran is a statement about the image of Spec A → Spec Z (finite, at most 2^{poly} primes, or with many
primes), decidable in AM; effective Chebotarev gives small Frobenius classes of finite étale covers; deterministic
factoring computes connected components of a finite étale algebra.

## 13. Working back from RH/GRH (the user, 21 Nov, before 16:32 UTC)

The user: "because RH is true, this implies backwards that X, Y, Z about the construction here that didn't assume
GRH"; go back over today's items asking what GRH being true says; bias warning: drop reflexive "no bearing on the
Millennium problem" lines and read the arguments. Scope of "true": RH and GRH for Dirichlet L-functions (hence zeta_K for
K abelian over Q) by A; Hecke L-functions over other number fields, including zeta_L for L not abelian over Q, by M
(defect table pending).

**Today's items under RH** [consequences; elementary unless cited]:
1. Packets (08, 09): every packet is quadratic; the Klein four action on zeros reduces to conjugation (σ = c on every
   zero); the spectral packet space is all critical: every zero gives a Connes-Consani ζ-cycle length 2π/γ, so the map
   Λ: Y_E^crit → R of 09 is defined on all of Y_E.
2. The Boolean label and the split of section 2 apply to every simple zero (no off-line zeros to exclude); the label
   is a ±-sequence on all simple zeros. (Simplicity is not implied by RH.)
3. The velocity explicit formula (section 4, item 4): on RH the contour moves to Re s = ½, which is the route to the
   mean of the velocities with power-saving error, hence to the statistics of the labels.
4. Under the Hurwitz deformation the zeros leave the line for t > 0 (ζ(s, a) has zeros off the line for a ≠ ½, 1:
   Davenport-Heilbronn, Cassels); with RH the t = 0 sheet is exactly on it. So t = 0 is the boundary point of the
   deformation where all zeros are on the line, and the first jet (the anti-invariant part) says how each leaves.
5. The two-sheet family (1+u)ζ − u: RH does not put its zeros (the a-points) on the line; Levinson's near-line theorem
   is unconditional.

**The workbench (Zeta-Function-Foundation, satellites 22-29zb, Sep 2026; its goal was a counterexample search)**
[consequences of RH, with the theorems used]:
1. Weil form: RH ⟺ Weil positivity, so the complete Weil form is positive semidefinite. Every finite Gram matrix of the
   complete form (the retained Weil test algebra; the even/odd cross-term matrices; the endpoint, ξ₄ and theta forms,
   insofar as they are compressions of the complete form) is PSD. The search for a negative certified full-form value
   has no positive outcome; a negative eigenvalue of a finite matrix locates an approximation or truncation error.
2. de Bruijn-Newman: Rodgers-Tao (Forum Math. Pi 2020) give Λ ≥ 0; RH gives Λ ≤ 0; so Λ = 0. For every t > 0, H_t has
   only real simple zeros (Csordas-Smith-Varga: simple for t > Λ), so the positive-time double-zero system has no
   solution; for every t < 0, H_t has nonreal zeros, so zero collisions occur at negative times accumulating at 0
   (Rodgers-Tao: at large height). In the workbench's Burgers picture (zeros as poles of the Burgers field −∂ log H_t):
   pole collisions for every negative time near 0, none for positive time. ζ is a critical datum of the flow, sitting
   exactly at the collision threshold.
3. Bost-Connes: the partition function is ζ(β); its zeros in the complex β-plane (Fisher / Lee-Yang zeros) all lie on
   Re β = ½ in the critical strip. RH is the Lee-Yang property of the BC system; in statistical mechanics such
   theorems come from positivity, matching item 1.
4. The spectral-support observables (poles at the zeta zeros): every pole in the strip is on the line.
5. The Navier-Stokes chain (29i, read 21 Nov, before 16:32 UTC): it imports the released NS construction
   (openaiNS2026release, 166-page revision; existence imported, its lemmas not independently verified there) and
   transports it by an explicit real translation ζ ↦ a + ζ of the spectral coordinate, a = S_j(X_{ν,t}(q)); the
   workbench proves this map preserves zero heights (Re ρ = ½ − Im ζ unchanged), so the blowup appears in the
   derivative singularity of the terminal arithmetic profile, not in the zeros. With RH: every transported zero lies
   on the critical line at every time before 1, including the terminal fibres. The "vacuum blowup" of the user's
   original directive is item 2: ζ sits exactly at the collision threshold of the heat/Burgers flow.
6. Next questions RH makes concrete [open]: the rate at which the negative-time collisions approach t = 0 as height
   grows (the workbench's collision calculus, now about a true picture); the mean and distribution of the velocity
   labels via the explicit formula on Re s = ½; the catalogue of GRH-conditional complexity theorems now unconditional.

## 14. What GRH being true says about the rest of this conversation (21 Nov, 16:3x UTC; clock read 16:32)

The user: not only the workbench; "what you have been discussing so far in this context". Scope marks: [A] needs RH and GRH
for Dirichlet L-functions only (so zeta_K for K abelian over Q); [M] needs GRH for Hecke L-functions over other number fields,
including zeta_L for L not abelian over Q.
1. **P vs NP thread.** Bürgisser's transfer (#P ⊄ P/poly ⇒ VP ≠ VNP over C) and Koiran's HN ∈ AM become unconditional
   [M; Bürgisser's exact GRH requirement still to be pinned]. In this framework, GRH is the theorem that lets the
   support (B) coordinate be read off ring-side counts at polynomial scale: effective Chebotarev (Lagarias-Odlyzko,
   Bach) says every Chebotarev class is supported among the primes below c(log d)², i.e. "no unsupported small window"
   (the §8 condition, at small scale). Abelian instances [A]: the least quadratic nonresidue is < 2 log² p (Ankeny,
   Bach) and the least prime in a progression mod q is O((φ(q) log q)²); hence deterministic polynomial-time square
   roots mod p and nonresidues, and Miller's primality test. The project's GRH_NIGHT / AN_GRH / CX_GRH runs already
   catalogue such consequences (CX-K02 is from there).
2. **GCT thread.** GRH for number fields does not give GCT's nonstandard RH (purity over F_q for nonstandard quantum
   groups, a Weil-type statement); what could transfer is A's method, which is item 10(a) of prompt 54.
3. **CUE thread.** Montgomery's pair correlation theorem (zeros match GUE/CUE pair correlation for test functions with
   Fourier support in (−1, 1)) assumed RH and is now unconditional [A]; the CUE-Hurwitz papers (12-14) compare zeta
   with CUE, and this range of the comparison is now a theorem. Moment conjectures (CFKRS, Hughes) stay conjectures.
4. **Zeta and split-zero thread.** Section 13: packets all quadratic, labels on all simple zeros, Weil positivity,
   Λ = 0, Lee-Yang for Bost-Connes, transported zeros on the line. Not implied: simple zeros (V_ζ ≅ A_ζ); zeros of
   the separated sheet or of (1+u)ζ − u on the line.
5. **Hexagon register.** H18 (K_{4k}(Z) = 0 for k ≤ 12) rests on OneCharU_s, inside riemannHypothesis's closure in
   Alpöge's archive (round 5): it now stands on A, with the closure check as recorded.
6. Not GRH-related: the ETH refutation itself; the GCT VI refutations and BIP; isolation results (VV, MVV, Hoza); the
   S6 higher Euler identity (Eichler-Zagier); the defect strand.

## 15. A stated in GCT and AG terms (the user, 21 Nov ~16:4x UTC: "bring it back to the terminology of GCT and AG";
## "especially ... my own explorations ... I'm not married to the terminology that I invented")

1. **Total positivity / characters of S_∞** [the chain of equivalences is standard: Pólya (Laguerre-Pólya class),
   Edrei (Pólya frequency sequences), Thoma (characters of S_∞); its application here new, to be checked by the
   consults]. Write Ξ(z) = ξ(½ + iz) = Σ_k (−1)^k b_k z^{2k}, b_k > 0, and F(x) = Σ b_k x^k, so F(−z²) = Ξ(z) and F has
   order ½ with zeros at x = −γ_j². Then RH ⟺ every zero of F is negative real ⟺ F(x) = F(0) Π_j (1 + x/γ_j²) with γ_j
   real ⟺ (b_k) is a Pólya frequency sequence: every minor of the Toeplitz matrix (b_{j−i}) is nonnegative. Scaling x
   so that Σ_j β_j = 1 with β_j = γ_j^{-2}/Z(2), Z(s) = Σ_{γ>0} γ^{-s} (the secondary zeta function of the zeros), this
   is a point of the Thoma simplex with α = 0, and the multiplicative central function
     χ_Ξ(σ) = Π_{cycles c of σ} (−1)^{|c|−1} Z(2|c|)/Z(2)^{|c|}
   on S_∞ is an extremal character. Conversely, positive definiteness of χ_Ξ forces RH (Thoma: extremal characters have
   real nonnegative parameters, and power sums determine the β_j). So **A gives an extremal character of the infinite
   symmetric group whose values are normalized secondary zeta values of the zeros**; its positive definiteness is an
   infinite family of positivity inequalities on Z(2ℓ). Total positivity is the shape of Lusztig's positivity of
   canonical bases, which GCT VI's PH0 asks for (PH1 asks in addition for a polytope count).
2. **Λ = 0 in these terms**: H_t stays in the Laguerre-Pólya class, hence gives a Thoma point, exactly for t ≥ 0; the
   de Bruijn-Newman flow leaves the Thoma simplex at t = 0 going backward.
3. **Weil positivity in AG terms**: the inequality behind Weil's proof for curves over F_q is the Hodge index theorem on
   C × C (Castelnuovo-Severi). For ζ, A gives the corresponding positivity of the Weil form; every Gram matrix of the
   workbench (section 13) is an instance of that index inequality.
4. **The anti-invariant split in AG terms**: for an L-function with functional equation, the involution s ↦ 1 − s
   splits a deformation into its ±1 eigencomponents; only the −1 component moves zeros off the line at first order
   (section 2). In a family of pure ℓ-adic sheaves the weights are constant (Deligne, Weil II), so geometric families
   have no such first-order motion; the Hurwitz shift has one at every zero computed, so it is not a family of pure
   weight. [reading; precise statement to be written]

## 16. The shape, made precise (consult a157422a, Claude Fable 5.2 at effort max, 21 Nov 16:56 UTC;
## consults/CONSULT_a157422a_FABLE_SHAPE.md; literature cited from memory there, RH used on the brief's word;
## checks in consults/consult_a157422a_checks.py)

1. **Section 11's configuration** is a totally positive point of a based ring at or next to the boundary of its
   positive part, with two layers:
   - typing: τ against e is absence against support, i.e. j_! against j_*, the defect projection of the Toeplitz
     extension;
   - confinement: Weil positivity, which is the Hodge index theorem.
   The finite-rank theorem (proved there): the kernel line of a corank-one positive Toeplitz form is the characteristic
   polynomial of a unitary (Carathéodory-Fejér). In AG this is Weil's theorem for curves, Zariski's lemma being the
   corank-one case.
2. **Section 15.1 checked:** RH ⟺ the Taylor coefficients of ξ at ½ form a Pólya frequency sequence ⟺ the zeros give
   a Schur-nonnegative specialization of the ring of symmetric functions Λ ⟺ the S_∞ central function with values
   Z(2ℓ)/Z(2)^ℓ is positive definite. These are three coordinate forms of one positive point: an instance of the shape,
   not a stronger statement. It gives a positive point of Λ, whereas GCT asks for positive structure constants.
3. **The two regimes (sections 8-9, 11):**
   - precise as a dichotomy with one criterion (proved there): a semiring is zero-sum-free without zero divisors ⟺
     its value determines its support;
   - precise as a Fourier duality for zeta functions: RH ⟺ Weil positivity ⟺ square-root cancellation in Σ_{n≤x} μ(n).
     Confinement of the zeros on the spectral side is maximal cancellation on the arithmetic side; the explicit
     formula is the transform between the regimes;
   - it breaks for circuits, where no transform plays the explicit formula's part.
4. **What A changes (Q3):** at every finite stage ζ is strictly inside the positive part: the Weil form is positive
   definite on every window; every finite Li-Toeplitz section K(m,n) = λ_m + λ_n − λ_{|m−n|} (Li coefficients λ_n) is
   positive definite; every Schur function of the γ_k^{-2} is positive. The kernel line of the Toeplitz picture exists
   only in the limit. The explicit-formula form is Lorentzian of index (1, ∞) with the two poles as null directions.
   [Main session's reading: this is the arithmetic counterpart of the hyperbolic plane spanned by the two fibre classes
   of C × C in Weil's proof (both null), whose orthogonal complement carries the definite form; the user's July
   construction (section 10, item 5: the zeta value as a null vector of the Lorentz form on Herm₂, with the zero at P₀
   and the pole at P_∞, P₀P_∞ = 0) is a finite-dimensional model of that hyperbolic plane.]
5. **Two items to act on:** (i) the scope of A: if A covered Hecke characters over every number field, ζ_L (the
   trivial character over L) would be A-scope and Koiran and Bürgisser with it; the project records A as Dirichlet
   L-functions, so they stay M-scope (brief corrected 16:57 UTC). (ii) Section 10.4's annihilator dimension: see the
   correction there.


## 17. "Look underneath, not above": the sign layer (the user, 21 Nov ~17:5x UTC; reading by the main session)
The user: Alpöge's method goes up (GRH, ERH, grand RH); the nonstandard RH is a layer down; F1 as "just a sign"; the ghost as a sign-valued integration constant; P vs NP lives below. Precise counterparts [standard objects; the reading is ours]:
1. F1 as a sign: the sign hyperfield S = {0, +, −} (Viro; Connes-Consani), image of R under x ↦ sgn x, with + plus − = {−, 0, +}; matroids over S are oriented matroids (Baker-Bowler). B (or Krasner's K) is its unsigned shadow.
2. The layer under RH is signature: RH ⟺ Weil positivity ⟺ every Li-Toeplitz section has exactly one positive eigenvalue (checked to size 9, consults/check_li_toeplitz_signature.py), a statement about signs of eigenvalues only. Alpöge's sign-only mechanism lives there.
3. The ghost as a sign: global ± data fixed by local data: root numbers ε = ±1 of self-dual L-functions; polarization signs in Hodge-Riemann; the parity ± = sgn of the a-th derivative in GCT VIII's ±(v − v⁻¹)^a f; the Boolean labels of the zeros.
4. The complexity of only the sign: PP = signs of GapP functions (counts with cancellation); NP ⊆ PP; Toda, PH ⊆ P^PP; sign-rank (Forster). GCT's positivity hypotheses say S-valued invariants of structure constants are constant (+): the E(4) computation (consults/E4_RANK_FOUR_20261121.md) is such a sign test at rank four.
5. Reference the user names for this layer (21 Nov ~18:0x UTC): Connes-Consani(?), "the absolute twistor line and the geometry of Spec Z", arXiv:2609.00299v1 (https://arxiv.org/html/2609.00299v1): their latest direct F1 work, with an F1 object that keeps track of direction (the user's "it's just a sign"). Not yet read; read it first when this line resumes, and place S, the signature form of RH and the root-number signs against it.
6. The user's reading (21 Nov ~18:0x UTC, marked as speculation): Alpöge's sign-only mechanism may be an F1-type construction under a name intuitive to non-specialists. Testable when 2609.00299 and Alpöge's argument are read side by side: does his sign mechanism factor through the sign hyperfield S, or through Connes-Consani's absolute (F1) objects?
7. **arXiv:2609.00299 read (21 Nov ~18:1x UTC, web-fetch agent, Claude Opus 5.5 at effort max): Connes-Consani, "The Absolute Twistor Line and the Geometry of \overline{Spec Z}" (31 Aug 2026).** Their base is F_{1²} := F_1[{0, 1, ε : ε² = 1}], "the signed extension" of F1, which keeps "the minimal additive datum—the canonical sign ε"; every commutative ring is an F_{1²}-algebra by ε ↦ −1 (only the sign and x ↦ −x survive). A Bombelli generator J² = ε gives the twistor line; the ε-twisted inversion T ↦ −1/T ("guided by the Weyl symmetry") yields the twistor real structure z ↦ −1/z̄ (Thm 1.2 = 5.1); Frobenius only for odd n (ε must be fixed), realizing Adams operations; odd primes split mod 4 by the Dirichlet character mod 4 (Prop. 7.5). No hyperfields, no zeta zeros, no positivity, no RH in the paper. Reading [ours]: this is the user's "F1 is just a sign" in Connes-Consani's own terms; and in G(R) the sign ε = −1 fixes exactly the Boolean pair {0, τ} (Fix(−1) = A ≅ B): the split-zero construction is where the F_{1²} sign meets Boolean addition.
8. **The six non-unimodal constants (P-F-E3-01) are not a hexagon** (a8d75352, 21 Nov ~18:1x UTC; E4_RANK_FOUR §6, E4_scripts/hexagon.py, hexagon_sym.py): the symmetry group of the rank-three table has order 8 (Dynkin swaps, anti-involution); orbits 4 + 2; the trace form's dual basis is not a permutation of the basis, so the cyclic slot relation adds nothing; no element of order 3, so no dihedral group of order 12 and no matching with the A₂ roots of χ². The six are the alternating products in the χ² cell minus the two shortest; they share one value with no symmetry explaining it. The user's Erdős-Straus "Kneser star": no text file in Papors/Chatnotes mentions Kneser (grep over .tex/.md/.txt, 21 Nov ~18:1x UTC); look in PDFs, zips or Codex workspaces next.
9. Split zero in Connes-Consani's terms: reports_20261120/split_zero/SPLIT_ZERO_IN_CONNES_CONSANI_TERMS_20261121.md.
