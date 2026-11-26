# Primer: MAS_ARTIN (prompt 48), the narrow trace step and the S₅ Artin gate

Written 23 Nov 2026 by Claude Opus 5.5 at effort high (agent a25c2acbb3a6f11f7). It is a recall of the run and of our
intakes; nothing new.

**The run and the newest return read.** GPT-6 Astra (ChatGPT Pro mode). The newest return is checkpoint 15 (22 Nov
02:46 UTC): `research_returns\MAS_ARTIN_checkpoint_15_20261122T0246Z_unzipped\modules\` (below `M`).

**Our intakes.** Of checkpoints 02, 10 and 15, by Claude Opus 5.5 at effort high (agent af2a18f62da23b48e), in
`intakes/MAS_ARTIN/`. The cp15 intake rechecked the proofs below in full.

**Inputs.**
- A: Alpöge's theorem.
- M: GRH for the Hecke L-functions concerned. This was Masullo's claim; his draft is not a proof. This run builds its
  own model in Meyer's setting; nothing in it is a fix of the draft.
- PF26: OpenAI's factoring preprint of 4 Oct 2026.

## 1. Which narrow-strip trace statement is RH itself
**Setting** (`M\hilbert_meyer_bridge.tex`, §1).
- Fix a primitive unitary Hecke function and its completed zero divisor.
- 𝓔 is the exponential Schwartz space; 𝓘_η is its closed convolution ideal; Q = 𝓔/𝓘_η is Meyer's zero-space
  quotient (GRH_NIGHT MT-M18).
- For a ∈ ℝ, s ≥ 0 and I = [u, v], H is the space L² with weight max(e^{2ux}, e^{2vx})(1 + x²)^{s/2}. Then
  J = closure of T_a𝓘_η, where T_a f = e^{ax} f, and Z = H/J, with i_a : Q → Z.

**MA-HM-001** (l. 86-254), checked given MT-M18/M26. Assume the strip premise (MA-HM.2): all zero real parts lie in
[c₀, c₁], with [c₀ − a, c₁ − a] ⊂ (u, v). Then the series S̃_g z = Σ_n 𝒯_n M_{g,n} r_n z defines an order-zero nuclear map
S_g : Z → Q with S_g i_a = C^Q_{k_g} and i_a S_g = C^Z_g, where k_g = e^{−a·}g.
- Mechanism: block maps r_n, with uniformly bounded norms, to finite jet algebras J_n of dimension O(log n). The
  multipliers satisfy ‖M_{g,n}‖ ≤ b_n(g), rapidly decreasing by integration by parts.
- An Auerbach basis gives the nuclear representation with ℓ^p coefficients.

**MA-HM-003** (l. 387-507), checked in both directions given MT-M18/M26:
- i_a kills the whole jet block of every zero ρ with Re(ρ − a) ∉ [u, v].
- For a = 1/2: RH for this function ⇔ for every width α > 0 and every compact smooth g with g(0) = 0, convolution
  factors through i_a in both smoothing orders.

Mechanism:
1. The translation bound ‖U_y‖ ≤ 2^{s/4} max(e^{uy}, e^{vy})(1 + y²)^{s/4} on the image of a block.
2. An eigenvector with eigenvalue e^{ρ−a} would then violate this bound for Re(ρ − a) > v (and with U_{−1}, for < u).
3. A test g = e^{−(ρ−a)x} b(x) with 𝓜g(ρ − a) = 1 shows no return map exists.
4. The converse is MA-HM-001.

Use: it says exactly which operator statement in the narrow trace route is RH. It is the reason the route cannot be
completed without zero location.

**MA-JP-004** (`M\causal_trace_separation.tex`, from l. 4), checked: for a locally finite positive divisor D in a
vertical strip with log-count, τ_D(g) = Σ d_λ E_λ(g) on 𝒟₊ = C_c^∞((0, ∞)) vanishes identically iff D is empty. It
lies in the span of E_{a₁}, E_{a₂} iff D ⊂ {a₁, a₂}.
- Mechanism: test functions t^{k−1}e^{−κt} with cut-offs converge to the resolvent powers Γ(k)/(κ − λ)^k.
- So an identity τ_D = A₁E_{a₁} + A₂E_{a₂} becomes a meromorphic identity Σ d_λ(κ − λ)^{−k} = …, whose poles separate.

**MA-FT-002** (`M\full_test_slow_band.tex`, l. 305-359), checked given MA-FT-001 (statement level). At fixed (α, s), the
following are equivalent:
- the local and global slow-band limits agree for all compact g with g(0) = 0;
- the same for all g ∈ C_c^∞((0, ∞));
- the upper deficiency δ⁺_ρ = 0 for every ρ;
- r^st_ρ = m_ρ for every ρ.

Requiring this for every 0 < α < 1/2 is RH. Mechanism: JP-004 applied to the divisor D⁺ = Σ δ⁺_ρ[λ_ρ]; the symmetry
ρ ↦ 1 − ρ̄ gives δ⁻ = 0.

## 2. Artin's conjecture in Calegari's S₅ family, given one real-zero hypothesis
**Setting** (`M\s5.tex`).
- L/Q has group S₅, is unramified at 5, and complex conjugation and Frob₅ have type (12)(34).
- E = L^{A₅}, F = L^{F₂₀} (degree 6), H = EF, B = ζ_H/ζ_F = L_F(s, η_F).
- β, b, n are the orders at 1/2 of B, of L(s, η_E), and of Calegari's cuspidal GL₅ function L(s, ϖ); k = β − b − n.
- (R_B): B(σ) ≠ 0 for real σ ∈ (0, 1), σ ≠ 1/2.

**MA-S5-001** (l. 49-150), checked given Calegari's Lemmas 4.8-4.10 (Math. Ann. 356, publisher pp. 13-15): under (R_B),
k ≥ 0, and k = 0 ⇔ the exceptional set Ω is finite ⇔ ϖ and the five-dimensional W match at every place.
- Mechanism: the quotient R = G_ϖ A/(G_W L_W) = R_𝓑 D_Ω, with D_Ω = ∏_{p∈Ω}((1+p^{−s})/(1−p^{−s}))². An infinite Ω
  gives a real pole of the positive Euler series. (R_B) puts it at 1/2, where ord R = −k.
- It also corrects two slips in Calegari's printed Lemma 4.6 and Theorem 4.7.

**MA-S5-004** (from l. 471), checked to l. 560: if k > 0, Σ_{p≤X, p∈Ω} (log p)/√p ~ (k/4) log X, by a positive-measure
Tauberian argument, and π_Ω(X) = X^{1/2+o(1)}.

**MA-LD-001** (`M\booker_route.tex`, l. 38), checked given Booker (Math. Ann. 363), Proposition 2.1 and Theorems
1.6-1.7:
- The difference datum 𝓕_R = 𝓕_ϖ − 𝓕_W (degree 0) has its complete signed divisor on Re s = 1/2: its Euler logarithm
  converges on Re s > 1/2, and the functional equation reflects this.
- If k > 0 it has infinitely many poles and zeros, and N_R(T) ≠ o(T).

**MA-FQ-001** (`M\s5_crystal.tex`, l. 11), checked:
- K_R = 0, since the archimedean parameters of ϖ and W are equal, both Γ_ℝ(s)Γ_ℂ(s)².
- a(t) = −m_R(t) is an integer-valued positive-definite function on the discrete group ℝ_d, in B(ℝ_d) with norm k.
- Mechanism: Booker's (A4) gives the Fourier transform of −μ as M_Ω + B₀. Here M_Ω is positive, with atoms
  4(log p)p^{−j/2} at ±j log p for p ∈ Ω and j odd, and B₀ has finite total variation.
- Subtracting the continuous density of B₀ leaves a measure of positive type, and narrow bumps extract the atoms.

**MA-FQ-002** (`M\s5_coset.tex`, l. 12), checked given Sanders 2020, Theorem 12.3 (Cohen's idempotent theorem): a
locally finite set in the coset ring of ℝ_d is a finite union of progressions up to a finite set. So such a function a
is a finite integer combination of lattice combs and point masses.

**MA-FQ-003** (`M\s5_crystal_rigidity.tex`, l. 11-119), checked: if a(t) is integer-valued and positive definite, with
locally finite support, a tempered measure ν, and a purely atomic Fourier transform, then supp ν̂ lies in finitely
many lattices h_j ℤ. Hence only finitely many primes carry an atom at c log p.
- Mechanism: Poisson summation for each comb. Uniqueness of the Lebesgue decomposition kills the continuous part. And
  p^m = q^n is impossible for distinct primes.

**MA-FQ-004** (l. 121-172), checked given FQ-001/002/003, LD-001 and S5-001: under (R_B), β = b + n. Equivalently, Ω is
finite, and ϖ matches W at every place.
- Mechanism: if k > 0, every p ∈ Ω gives a nonzero atom 4(log p)p^{−1/2} at log p. FQ-003 makes Ω finite, and S5-001
  then gives k = 0.
- Consequence: automorphy and holomorphy of the nontrivial irreducible Artin factors in the family.
- GRH for the factors needs M; A does not give (R_B).

Use: it reduces Artin's conjecture in this family to one real-zero statement for one Hecke L-function, testable field
by field. This is the main theorem of Paper 1 in `reports_20261122/paper_seeds/SEED_MAS_ARTIN.md`, and it went to
prompt 69, Paper II.

## 3. Open rows (at checkpoint 15) and where the results went
**Open:**
- **The narrow step over Q:** unchanged. FT-002 keeps the upper-deficiency condition, which is RH (HM-003). Using A
  there is circular for an independent method.
- **Non-induced Hecke characters:** the narrow identity needs that character's own RH. This includes the cubic
  character ψ_{269,3} over Q(√−3) (MA-CH, MA-CC).
- **(R_B) removal:** the gate is MA-RB-014, an envelope and integer-cap inequality on nonreal zero backgrounds
  (`M\s5_nonreal_background.tex`, l. 44). MA-RB-016 (`M\s5_induced_spin_scope.tex`, l. 38) shows the induced spin
  Rankin-Selberg partner is an old product and gives no new inequality.
- **PF26:** its input classification is complete at its scope (MA-PF-001-005, statement level).
- The run recorded its first stalled review at checkpoint 15.

**Where the results went:**
- The seed's Paper 1 (S₅).
- Prompt 69 (BEYOND_DIRICHLET), Paper II.
- The Masullo defect table, `TO_SEND\PRO\_staging_20261121\cores\MASULLO_DEFECTS_20261121.md`.
- The ALP_CONNES and 68 lines, through HM-003.

**Corrections to our own intakes** (cp15 intake, §3):
- Stark's lemma does not give (R_B) from A.
- RH for the cubic Kummer family does not make Dunn-Radziwiłł unconditional.
- HM-003's equivalence holds in the run's model, not as a statement about the draft.
