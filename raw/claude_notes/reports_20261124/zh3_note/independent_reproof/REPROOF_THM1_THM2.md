# Independent re-proof of Theorems 1 and 2 of the ZH3 note

Claude Opus 5.5 at effort high (agent a25c2acbb3a6f11f7), 24 Nov 2026. The proofs were written from
`STATEMENTS_FOR_REPROOF.md` and Suzuki's paper only, before zh3_note.tex was opened.

**Input A.** Alpöge's theorem: every zero of Ξ is real.

**Notation.** As in the statements file: Γ, m_γ, E(T), n(T), γ_*, Q, the space 𝓗 = ℓ²(Γ, m), the operator C (multiplication
by 1/γ), V_N, the projection P_N, C_N = P_N C P_N, S_k, D_{N,k}, H_{N,k}, and the bases b_j with matrices G_N, H_N.
Throughout, Q(u, v) is the zero-side form Σ m_γ û(γ) \overline{v̂(γ)}.

## Suzuki's results used, checked at the source
`screwzzwolf_6.tex` (arXiv:2610.32704):
- **(2.2)** (`eq_202`, line 424): σ = Σ_{γ∈Γ} m_γ γ^{−2} < ∞, from the order of Ξ and Ξ(0) = ξ(1/2) ≠ 0. **Used.**
- §1, after Theorem 1.2 (line 235): "The multiplicities of the zeros are not recovered by this product". Context only.
- **(4.1)** (`eq_401`, line 1104): ‖Π_a C Π_a − C‖_{𝔖₂} → 0 when Π_a → I strongly and C ∈ 𝔖₂. Not used as a citation; the
  general fact is proved in Lemma 3, because our projections are onto other subspaces.
- The sampling isomorphism (`eq:sampling`, line 594, citing his earlier paper, Lemma 5.4). Not used; the density needed
  is proved directly in Lemma 2.

## Lemma 0 (elementary facts)
(a) **Γ is infinite**, and every zero counted with multiplicity is at most polynomially frequent: the number of zeros
with |γ| ≤ T, counted with multiplicity, is O(T log T) (Riemann-von Mangoldt). Hence 𝓗 is infinite-dimensional.

(b) **C is compact, self-adjoint, injective and Hilbert-Schmidt.**
- e_γ = δ_γ/√m_γ, γ ∈ Γ, is an orthonormal basis of 𝓗.
- C e_γ = γ^{−1} e_γ, and ‖C‖²_{HS} = Σ_{γ∈Γ} γ^{−2} ≤ σ < ∞.
- The eigenvalue 1/γ has the one-dimensional eigenspace ℂe_γ, since the γ ∈ Γ are distinct.
- tr C^{2k} = Σ_{γ∈Γ} γ^{−2k} = 2 Σ_{γ>0} γ^{−2k}, by Γ = −Γ.

(c) **S_k = 2 Σ_{γ>0} m_γ γ^{−2k}.**
- Ξ is entire of order 1 and even, with Ξ(0) ≠ 0. Hadamard gives Ξ(z) = Ξ(0) e^{bz} ∏_ρ (1 − z/ρ) e^{z/ρ}.
- Pair ±γ: the factors e^{z/γ} e^{−z/γ} cancel, and evenness forces b = 0. So
  Ξ(z)/Ξ(0) = ∏_{γ>0} (1 − z²/γ²)^{m_γ}, which converges absolutely by σ < ∞.
- For |z| < γ_1 := min{γ > 0}, log(Ξ(z)/Ξ(0)) = −Σ_{γ>0} m_γ Σ_{k≥1} z^{2k}/(kγ^{2k}). This double series converges
  absolutely, because Σ m_γ γ^{−2k} ≤ γ_1^{2−2k} σ.
- So −2k [z^{2k}] log(Ξ/Ξ(0)) = 2 Σ_{γ>0} m_γ γ^{−2k}.

(d) **Consequently** S_k − tr C^{2k} = 2 Σ_{γ>0} (m_γ − 1) γ^{−2k} =: R_k ≥ 0.

## Lemma 1 (the windows are well defined and nested)
- **Finite norm.** Each u ∈ V_N is Lipschitz with compact support, so |û(t)| ≤ min(‖u‖_1, ‖u′‖_1/|t|) by one integration
  by parts. Hence Σ m_γ |û(γ)|² ≤ ‖u′‖²_1 σ < ∞, and the sampling map V_N → 𝓗 is defined.
- **Nested.** V_N ⊂ V_{N+1}: the grid 2^{−N−1} refines the grid 2^{−N}, (−N, N) ⊂ (−N−1, N+1), and the mean is still
  zero.
- So W_N := image of V_N satisfies W_N ⊂ W_{N+1}, and the projections satisfy P_N ≤ P_{N+1}.
- **Dimension.** dim W_N ≤ dim V_N = d_N < ∞. The sampling map on V_N need not be injective; this is where G_N may be
  singular.
- **The basis.** The b_j = t_j − t_0 (0 < |j| < N2^N) are linearly independent, by evaluation at the grid points. They
  have mean zero (∫t_j = h for all j) and span V_N: an f ∈ V_N is Σ_{|j|<N2^N} f(jh) t_j with Σ f(jh) = 0, and
  Σ_j f(jh) t_j = Σ_{j≠0} f(jh)(t_j − t_0) when Σ_j f(jh) = 0.

## Lemma 2 (density: ⋃_N W_N is dense in 𝓗)
**Step 1. Sampling of C_c^∞ is dense.** Let v ∈ 𝓗 be orthogonal to (û(γ))_γ for every u ∈ C_c^∞(ℝ).
- The distribution T(φ) = Σ_γ m_γ \overline{v_γ} φ(γ) is tempered. By Cauchy-Schwarz,
  |T(φ)| ≤ ‖v‖ (Σ m_γ |φ(γ)|²)^{1/2} ≤ ‖v‖ sup_t (1 + t²)|φ(t)| · σ′^{1/2}, where
  σ′ = Σ m_γ (1 + γ²)^{−2} < ∞ by Lemma 0(a).
- T(û) = 0 for all u ∈ C_c^∞. The Fourier image of C_c^∞ is dense in Schwartz space, since C_c^∞ is dense in 𝓢 and
  Fourier is a homeomorphism of 𝓢. So T = 0.
- A Schwartz φ equal to 1 near one ordinate γ₀ and vanishing at all others, which is possible as Γ is discrete, gives
  m_{γ₀} \overline{v_{γ₀}} = 0. Hence v = 0.

**Step 2. Mean-zero C_c^∞ suffices.**
- Fix h ∈ C_c^∞ with ∫h = 1 and put h_R(x) = R^{−1} h(x/R).
- Then |ĥ_R(γ)| = |ĥ(Rγ)| ≤ ‖h′‖_1/(R|γ|), so ‖h_R‖²_𝓗 ≤ ‖h′‖²_1 σ/R² → 0.
- For u ∈ C_c^∞, u − (∫u) h_R is in C_c^∞ with mean zero, and tends to u in 𝓗.

**Step 3. Each mean-zero u ∈ C_c^∞ is a limit of elements of V_N.**
- Let supp u ⊂ (−M, M), h = 2^{−N}, N > M + 1, and let I_N u be the piecewise-linear interpolant on the grid. It
  vanishes outside (−M−h, M+h) ⊂ (−N, N).
- Put w = u − I_N u. Then ‖w′‖_∞ ≤ h‖u″‖_∞ (the standard interpolation estimate on each cell), and w is supported in
  [−M−1, M+1]. So ‖w′‖_1 ≤ (2M+2) h ‖u″‖_∞, and by Lemma 1, ‖w‖²_𝓗 ≤ ‖w′‖²_1 σ → 0.
- I_N u need not have mean zero: c_N := ∫ I_N u = −∫w, and |c_N| ≤ (2M+2)‖w‖_∞ ≤ (2M+2) h² ‖u″‖_∞.
- Let τ(x) = (1 − |x|)_+. It is in V_N for N ≥ 2, being piecewise linear on every dyadic grid with support
  [−1, 1] ⊂ (−N, N), and ∫τ = 1.
- Then f_N := I_N u − c_N τ ∈ V_N, and ‖u − f_N‖_𝓗 ≤ ‖w‖_𝓗 + |c_N| ‖τ‖_𝓗 → 0.

Steps 1-3 together: ⋃_N W_N is dense in 𝓗.

## Lemma 3 (convergence of the compressions)
P_N → I strongly: by Lemma 2 and the nesting, for each x the distance from x to W_N decreases to 0. Then
‖C_N − C‖_{HS} → 0, because
‖P_N C P_N − C‖_{HS} ≤ ‖(P_N − I) C P_N‖_{HS} + ‖C(P_N − I)‖_{HS} ≤ ‖(P_N − I) C‖_{HS} + ‖C(P_N − I)‖_{HS}.
- ‖(P_N − I) C‖²_{HS} = Σ_γ ‖(P_N − I) C e_γ‖². Each term tends to 0 and is at most γ^{−2}, which is summable, so the
  sum tends to 0 by dominated convergence.
- The second term is the HS norm of the adjoint of the first.

This is Suzuki's (4.1) mechanism, proved here for these subspaces. It follows that tr C_N^{2k} → tr C^{2k} for k ≥ 1:
A^{2k} − B^{2k} = Σ_{i=0}^{2k−1} A^i (A − B) B^{2k−1−i}, and |tr(X Y)| ≤ ‖X‖_{HS} ‖Y‖_{HS}, with ‖C_N‖_{HS} ≤ ‖C‖_{HS}.
So |tr C_N^{2k} − tr C^{2k}| ≤ 2k ‖C_N − C‖_{HS} ‖C‖_{HS}^{2k−1} → 0.

## Lemma 4 (trace comparison for compressions)
Let B be compact self-adjoint, P an orthogonal projection, f(x) = x^{2k}, k ≥ 1. Then
tr f(PBP) ≤ tr P f(B) P ≤ tr f(B).
If B is injective and P ≠ I, the second inequality is strict.

**Proof.**
- On ran P, take an orthonormal eigenbasis (u_i) of the compact operator PBP|_{ran P}, with eigenvalues μ_i = ⟨Bu_i, u_i⟩.
  Off ran P, PBP = 0 and f(0) = 0.
- So tr f(PBP) = Σ_i f(⟨Bu_i, u_i⟩) ≤ Σ_i ⟨f(B)u_i, u_i⟩ = tr P f(B) P. The inequality is Jensen for the spectral
  probability measure of B in the state u_i, since f is convex.
- Then tr f(B) − tr P f(B) P = tr (I−P) f(B) (I−P) = ‖f(B)^{1/2}(I−P)‖²_{HS} ≥ 0, using f(B) ≥ 0.
- It is > 0 when f(B)^{1/2} = |B|^k is injective and I − P ≠ 0.

The same argument with P_N ≤ P_{N+1}, applied to B = C_{N+1} and P = P_N, gives P_N C_{N+1} P_N = C_N and so
tr C_N^{2k} ≤ tr C_{N+1}^{2k}.

## Proof of Theorem 1
1. **Strict lower bound.** By Lemma 4 with B = C (injective) and P = P_N (ran P_N finite-dimensional, 𝓗 not, so
   P_N ≠ I): tr C_N^{2k} < tr C^{2k}. Hence D_{N,k} = S_k − tr C_N^{2k} > S_k − tr C^{2k} = R_k (Lemma 0(d)).
2. **Second inequality.** R_k = 2 Σ_{γ>0} (m_γ − 1) γ^{−2k} ≥ 2 Σ_{0<γ≤T} (m_γ − 1) T^{−2k} = 2E(T)/T^{2k}, since all
   terms are ≥ 0.
3. **Monotone limit.** By Lemma 4 (second paragraph), D_{N,k} is nonincreasing in N. By Lemma 3, D_{N,k} → R_k. In
   particular D_{N,k} > 0, so H_{N,k} is defined.
4. **sup H_{N,k} ≤ γ_*.** If γ_* < ∞, then D_{N,k} > R_k ≥ 2(m_{γ_*} − 1) γ_*^{−2k} ≥ 2 γ_*^{−2k}, so H_{N,k} < γ_*.
5. **sup H_{N,k} ≥ γ_*.** Fix k. By step 3, H_{N,k} increases to (2/R_k)^{1/(2k)}, which is +∞ if R_k = 0.
   - If γ_* = ∞, then R_k = 0 and the sup is ∞.
   - If γ_* < ∞, write R_k = 2γ_*^{−2k} B_k with B_k = (m_* − 1) + Σ_{γ>γ_*} (m_γ − 1)(γ_*/γ)^{2k}, where m_* = m_{γ_*}.
     Each term of the sum tends to 0 as k → ∞ and is at most m_γ γ_*² γ^{−2}, which is summable. So B_k → m_* − 1 ≥ 1
     by dominated convergence.
   - Then (2/R_k)^{1/(2k)} = γ_* B_k^{−1/(2k)} → γ_*. So the sup is at least γ_*, and sup H_{N,k} = γ_*.
6. **First equivalence.**
   - (⇐) If D_{N,k} < 2/T^{2k}, then 2E(T)/T^{2k} < 2/T^{2k} by step 1, so E(T) = 0, i.e. every m_γ = 1 for
     0 < γ ≤ T. Under A the zeros with 0 < Im ρ ≤ T are ρ = 1/2 + iγ with these γ.
   - (⇒) If they are all simple, then γ_* > T. By step 5, sup H_{N,k} = γ_* > T, so some H_{N,k} > T, i.e.
     D_{N,k} < 2/T^{2k}.
7. **Second equivalence.** All zeros are simple ⇔ γ_* = ∞ ⇔ sup H_{N,k} = ∞, by steps 4-5. ∎

## Proof of Theorem 2
1. **The form.** For c ∈ ℂ^{d_N}, put w(c) = Σ_j c_j b̂_j ∈ W_N, where b̂_j is the sampling vector. Then
   c*(T H_N − G_N)c = T⟨C w, w⟩ − ⟨w, w⟩ = ⟨(TC − I) w, w⟩.
2. **Reduction to W_N, including singular G_N.** The map c ↦ w is onto W_N with kernel K = ker G_N, since
   c*G_N c = ‖w‖². The form q(c) = ⟨(TC − I)w(c), w(c)⟩ vanishes on K.
   - A subspace U ⊂ ℂ^{d_N} on which q is positive definite meets K only in 0. So it maps injectively onto a subspace of
     W_N on which q_W(w) = ⟨(TC − I)w, w⟩ is positive definite.
   - Conversely, a positive subspace of W_N lifts to one of the same dimension.
   - So ι_N(T) = ind_+(T H_N − G_N) = ind_+(q_W).
   - Moreover q_W(w) = ⟨(T C_N − I)w, w⟩ on W_N, because w = P_N w. So ind_+(q_W) is the number of eigenvalues μ of the
     self-adjoint operator C_N|_{W_N} with Tμ − 1 > 0, i.e. μ > 1/T, counted with multiplicity. These are exactly the
     eigenvalues > 1/T of C_N on 𝓗, since C_N vanishes on W_N^⊥.
3. **Min-max.** For a compact self-adjoint A let λ_k(A) = sup_{dim U = k} min_{u∈U, ‖u‖=1} ⟨Au, u⟩. Then
   #{eigenvalues > 1/T} = max{k : λ_k(A) > 1/T}. For compressions, λ_k(PAP) ≤ λ_k(A): if U ⊂ ran P, then
   ⟨PAPu, u⟩ = ⟨Au, u⟩; and a U not inside ran P contains a unit vector u with ⟨PAPu, u⟩ ≤ 0 < 1/T, which is
   irrelevant above the level 1/T > 0.
   - **Nondecreasing:** C_N = P_N C_{N+1} P_N gives λ_k(C_N) ≤ λ_k(C_{N+1}).
   - **Upper bound:** λ_k(C_N) ≤ λ_k(C). The eigenvalues of C above 1/T are 1/γ for the distinct γ ∈ (0, T), each simple
     (Lemma 0(b)). Since Ξ(T) ≠ 0, T ∉ Γ, so their number is K(T) := #{γ ∈ Γ : 0 < γ ≤ T}, the number of distinct
     ordinates in (0, T].
   - **Equality for large N:** by Lemma 3, ‖C_N − C‖ ≤ ‖C_N − C‖_{HS} → 0, and |λ_k(A) − λ_k(B)| ≤ ‖A − B‖ (Weyl).
     λ_{K(T)}(C) = 1/γ_{K(T)} > 1/T strictly, because T ∉ Γ. So λ_{K(T)}(C_N) > 1/T for large N, and ι_N(T) ≥ K(T).
     With the upper bound, ι_N(T) = K(T).
4. **The equivalence.** n(T) = Σ_{0<γ≤T} m_γ ≥ K(T), with equality iff all these m_γ are 1, i.e. iff the zeros with
   0 < Im ρ ≤ T are simple. Since ι_N(T) ≤ K(T) ≤ n(T) for all N:
   - if ι_N(T) ≥ n(T) for some N, then K(T) = n(T), so the zeros are simple;
   - conversely, if they are simple, then ι_N(T) = K(T) = n(T) for large N. ∎

## Remarks
- **Which hypothesis does what.** A is used only to make Γ real, so that Q is the positive form Σ m|û(γ)|² and the
  ordinates are the imaginary parts. Theorems 1-2 as stated use Q in this zero-side form. The explicit formula enters
  only in computing G_N and H_N from primes, which is outside these proofs.
- **Exactness.** Nothing requires G_N invertible (Theorem 2, step 2), nor V_N → W_N injective.
