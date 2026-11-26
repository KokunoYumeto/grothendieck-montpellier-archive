# NCG and the zeta zeros: how Alpöge's theorem runs through Connes's programme, and toward global Langlands

Structural note, 23 Nov 2026, by Claude Opus 5.5 at effort high (agent afa2696b67cad55de). Brief:
`field_experts/structural_maps_20261123/BRIEF.md`.

Sources:
- our primers `intakes/ALP_CONNES/PRIMER_ALP_CONNES_20261123.md` and `intakes/ZETA_HEAT/PRIMER_ZETA_HEAT_20261123.md`;
- the intakes beside them;
- the recall report `reports_20261123/NONSTANDARD_RH_SLICES_20261123.md`, whose content is the user's statements and
  our earlier notes, cited by its section numbers;
- the H27 editor's records `reports_20261123/h27_note/RECORDS.md` (Claude Fable 5.2 at effort max).

Status words come only from our check events. Facts quoted "from memory" are marked so and are to be opened before use.
Nothing here is graded.

A = Alpöge's theorem: RH for every Dirichlet L-function, ζ included. This is GRH for the automorphic representations of
GL_1 over Q.

## 1. The maps, written out

### Map 1. A ⇔ Connes's trace formula over Q, at an explicit cutoff (ALP_CONNES T51)
- **Objects.** On one side, the Dirichlet characters χ, i.e. the unitary characters of the idele class group
  C_Q = Ẑ^× × R_+^×, and the zeros of L(s, χ). On the other side, the Hilbert spaces of prolate cutoffs, one per χ, with
  the projections Q_{χ,Λ} and the action R of C_Q.
- **Correspondence.** The theta map E_χψ(x) = √x Σχ(n)ψ(nx), and for χ = 1 the two polar lines.
- **What is transported.**
  - The trace Tr(Q_Λ R(h)) has the asymptotic expansion 2 log Λ·h(1,1) − (the sum over zeros) + (polar terms).
  - Under A this equals Weil's distribution, so the formula holds (T41, T44-T46).
  - Conversely, the formula gives Weil positivity, hence A (T50, T51).
- **What we proved:** checked by us at cp18, given T25-T43 and T47-T48.
- **Credit (H27):** the statement is Connes's; ours is the proof at this cutoff. The positivity half (T50) is
  unconditional.
- **Structure.** This is the GL_1/Q trace formula in Connes's form. A sits on the spectral side as "the zeros give a
  positive measure", and the geometric side is the semilocal explicit formula.

### Map 2. Weil completion ↔ finite prime matrices (S50, which is Suzuki's)
- Under A, the Weil form makes the completion H ≅ ℓ²(Γ, m), and D⁻¹ is compact.
- Its compressions to finite dyadic spaces are computed from finitely many prime powers. Their eigenvalues converge to
  1/γ, and a fixed probe recovers each m_γ.
- Checked by us at cp24. H27 credits it to Suzuki, arXiv:2610.32704.
- **Structure.** A as a statement about a compact operator: the zeros are an honest spectrum (Connes's spectral
  realization), and arithmetic enters only through the matrix entries.

### Map 3. Simplicity of zeros ↔ the growth rate of a finite positivity test (ZETA_HEAT thm:fd-limits)
- **Objects.** On one side, the multiplicities m_x of the zeros of Ξ. On the other, the Taylor coefficients b_k(a) of
  the backward heat flow H_{−a}, and the first order of failure m_*(−a) of total positivity of the Toeplitz matrix
  (b_{j−i}).
- **Correspondence.** √a·m_*(−a) → min_{m_x≥2} x𝔯_{m_x}/(2√2). Here 𝔯_m is the first spread at which the unitary
  orbital integral of the Hermite roots turns negative.
- **What is transported.** Simplicity becomes the divergence of √a·m_*(−a).
- **What we proved:** checked by us, the analytic part, plus 𝔯₂ = π and 𝔯₃ = 2π/√3 by HCIZ.
- **Structure.** This sits one level above A. A is the Laguerre-Pólya property of Ξ (all zeros real, i.e. PF_∞ of the
  coefficient sequence at a = 0). Simplicity is how that positivity degrades under the backward flow.

### Map 4. The counting with the basepoint ↔ the Witt ring of Euler products (recall report §2.2, §2.4)
- **Objects.** Counts c(q) = Σ a_j q^j of sign-twisted Tate objects, and their global zetas
  Z_c(s) = Π_j ζ(s − j)^{a_j}, with χ₋₄ for the ε-part.
- **Correspondence.** c ↦ Z_c, a ring map that sends products of counts to ⋆-products of Euler factors. ζ is its unit
  (the basepoint: |X₊| = |X| + 1, and q + 1 = |P¹_{F₁}(F_q)|).
- **What is transported.** Purity of the counts, i.e. their zeros on Re s = j + 1/2, which is A on each Tate twist.
- **What our runs proved there:** the rank-three nonstandard RH reduction (recall §2.4: "purity by A, positivity by 1,
  composition by the dimension ring"). This is GCT's, carried here.
- **Structure.** The GL_1 slice of Grand RH realized on Connes-Consani's F₁ objects: the absolute line and the twistor
  sign ε.

### Map 5. The cubic gate ↔ GL_1 over K = Q(ω) ↔ dihedral GL_2 over Q (ALP_CONNES Q7, AM-H04)
Let F = Q(∛269) and L(s) = ζ_F(s)/ζ(s).
- **Galois side.** L = L(s, ρ), with ρ the 2-dimensional standard representation of S_3 = Gal(F^{gal}/Q). And
  ρ = Ind_K^Q χ, with χ the cubic Kummer character of 269 on G_K.
- **Automorphic side.** By automorphic induction, L(s, ρ) = L_K(s, χ). This is a Hecke L-function on GL_1 over K, and it
  is the L-function of a weight-one dihedral newform on GL_2/Q of level |D_K|·N(f_χ) = 3·269² = 217083 (the conductor
  Q of AC-K09).
- **The identity checked at the level of coefficients** (my derivation, at every unramified p):
  - for p ≡ 2 mod 3, x³ = 269 has exactly one root mod p, so a_p = 1 − 1 = 0, matching an inert p in K;
  - for p ≡ 1 mod 3, there are 3 or 0 roots, so a_p = 2 or −1. This is χ(π) + χ(π̄) = 2 or 2Re ω = −1, according as
    269 is a cube mod p or not.
- **What A gives here:** nothing directly. The gate is RH on the next rung, GL_1 over K, equivalently a dihedral form on
  GL_2/Q.
- **What our runs proved on the way:**
  - the exact 3-adic Selmer and K-groups of E = Q(ω, ∛269) (checked by us);
  - Weil positivity of this L-function on windows t ≤ 4 with no RH (AC-K09, checked by us);
  - the window criterion AM-H04 (checked by us at cp04);
  - the arithmetic budget, including the nonzero coefficient-7 Selmer groups O/7^{s(e)} of G219 (steps 1-5 checked
    by us).

### Map 6. Bost-Connes systems: GL_1 by construction (from memory; to be opened)
- The BC system (C*(Q/Z) ⋊ N^×, σ_t) has partition function ζ(β). Its symmetry group is Ẑ^× = Gal(Q^ab/Q). Its
  extremal KMS_∞ states take values in Q^ab, with the class field theory action.
- Restricting the trace to a χ-isotypic part of Ẑ^× gives L(β, χ). So A is the statement that every χ-twisted BC
  partition function has its nontrivial zeros on Re β = 1/2 after continuation.
- **The K-version** (the Connes-Marcolli-Ramachandran system of an imaginary quadratic K, with symmetry Gal(K^ab/K) and
  partition function ζ_K) carries L_K(β, χ) as its χ-twisted partition function. So the cubic gate of Map 5 is RH for
  one twisted partition function of the CMR system of Q(√−3).
- The GL_2 Connes-Marcolli system (with partition function ζ(β)ζ(β−1)) is the next rung of the same family.
- ALP_CONNES's BCM follow-up row records "A does not imply a new phase transition, finite-order cubic RH, or local weight
  purity" (review 34): A acts on the zeros, not on the KMS structure.

## 2. The rungs of global Langlands
| rung | automorphic | Galois / motivic | our results there |
|---|---|---|---|
| GL_1/Q | Dirichlet characters | Artin-Tate motives, Q^ab | A (Alpöge); T51 (Map 1); S50 (Suzuki, Map 2); ZETA_HEAT (Map 3); the counts of Map 4; CX_GRH/GRH_ALGORITHMS consequences |
| GL_1/K, K = Q(ω) | Hecke characters of K | characters of G_K, CM motives | the cubic gate, H04.4; the K-groups, Selmer groups and G219 as its arithmetic side |
| GL_2/Q, dihedral | weight-one theta series θ_χ | Ind_K^Q χ, the S_3 standard representation | the same gate, viewed through automorphic induction |
| GL_2/Q, general | modular forms | elliptic curves, H¹ | ALP_MACHINE's theta-lift chain (Alpöge's mechanism, steps 2-20) |
| GL_5/Q (S_5) | Calegari's cuspidal ϖ | the rank-five Artin representation | MAS_ARTIN: all-place matching given R_B (checked by us at cp15) |
| GL_n trace formula | Arthur-Selberg | — | none yet |

**What the next rung needs, as concrete statements.**
1. **T51 over K (GL_1/K).**
   - Statement: for K = Q(ω) and its prolate cutoffs per Hecke character (theta map E_χψ(x) = Σ_𝔞 χ(𝔞)ψ(N𝔞·x)), the
     trace formula holds iff GRH holds for every Hecke L-function of K.
   - The ⇐ half needs (a) a K-analogue of AC-T49, i.e. Möbius-twisted Hecke sums bounded by √N/(log N)^B at polynomial
     frequencies, from the classical zero-free region, and (b) the K-version of the Connes-Consani-Marcolli criterion.
   - **The positivity half T50_K should be unconditional, as T50 is.** It is the natural first theorem to prove.
2. **H04.4 as a GL_2 statement.** The window inequality for the dihedral form θ_χ of level 217083. The run's route is
   the arithmetic budget. An automorphic route would use the Rankin-Selberg square. Since χ^c = χ̄ = χ², one has ρ ⊗ ρ̄ = 1 ⊕ η_K ⊕ ρ, so
   L(s, θ_χ × θ̄_χ) = ζ(s)·L(s, χ₋₃)·L(s, ρ): the square contains the gate's own L-function next to two GL_1/Q factors
   covered by A. The coefficients of −L'/L for this square are Λ(n)·|tr ρ(Frob)|² ≥ 0 at unramified prime powers. This is the Landau positivity that AM-H04's
   window exploits; it can be written as a GL_2 × GL_2 statement.
3. **The GL_n rung of the trace formula.**
   - A cutoff on GL_n(Q)\GL_n(A) whose spectral side, restricted to cuspidal π, carries the zeros of L(s, π) through a
     theta map built from the Godement-Jacquet zeta integral.
   - The statement would be: the cutoff trace formula for GL_n holds iff GRH for GL_n.
   - What is missing is the analogue of the prolate selection: a finite-rank cutoff whose defect is asymptotically
     positive unconditionally.

## 3. Structural notes: one mechanism in several fields

**(a) Positivity of a Toeplitz form detects zeros.** Four instances.
| | Weil / Connes (Map 1) | backward heat (Map 3) | Li-Toeplitz (recall §2.7) | GCT positivity (Map 4) |
|---|---|---|---|---|
| form | the Weil form on a window [−L, L], a convolution (Toeplitz) operator | the Toeplitz minors of b_k(a) | Li coefficient Toeplitz sections | structure constants ±t^a f |
| what positivity encodes | RH (Weil) | at a = 0, RH (Laguerre-Pólya); its rate under a > 0, simplicity | RH, as one positive eigenvalue per section | purity of the Tate objects (free by A) plus a separate effectivity |
| failure scale | λ = e^L: trial q(v_L) ≪ λ^{9+ε}e^{−4πλ²} (S47; ZETA_HEAT prop:prolate-upper), a₂ ≪ λ^{13+ε}e^{−4πλ²} (ZETA_HEAT cp03 prop:odd-prolate-upper); needed a₂ ≳ λ^{9+α}e^{−4πλ²}, 0 < α ≤ 4 (ALP_CONNES cp44 RZ.5); proved unconditionally a₁, a₂ ≥ exp{−Cμ^{1/d_MT}log μ(1+log log μ)}, μ = λ², d_MT = 0.83625… (ZETA_HEAT final thm:cosine-lower-rate, after Mori's μ^{6/5}) | m_*(−a) ~ c/√a | — | the dimension ring |

The dictionary between the first two:
- H_{−a}(z) = ∫ e^{−au²}Φ(u)cos(zu) du **damps** the theta kernel by a Gaussian in the logarithmic variable u.
- The Weil window **truncates** test functions to |u| ≤ L.
- Both are one-parameter deformations of the same positivity of Φ's transform, by Gaussian weight versus sharp cutoff.

**(b) Defect positivity is unconditional; identification of the limit is the hypothesis.**
- In T50/T51 the cutoff defect is asymptotically positive with no hypothesis, and A is exactly the identification of
  its limit with W.
- In ZETA_HEAT the trace defect 𝒟_N ≥ 0 always, and simplicity is 𝒟_N → 0 (prop:trace-height,
  E(T) ≤ (T²/2)𝒟_N).
- The same shape appears twice: a positive defect, and a conjecture that it vanishes in the limit.
- ZETA_HEAT cp03 (thm:fd-arithmetic-complete, checked by us 23 Nov) makes the heat and window sides one invariant at the
  level of limits: with D_{N,k} = S_k − tr(C_N^{2k}) for Suzuki's compressions on the window [−N, N] and
  H_{N,k} = (2/D_{N,k})^{1/(2k)}, sup_{N,k} H_{N,k} = γ_* (the first multiple ordinate) and lim a·j_*(−a) = ½γ_*².
  The Toeplitz limit L_T is pinned to L_J within logarithms (cor:fd-global-growth-numeric). No rate matching a to N
  is proved.

**(c) The sign and the parity.** The recall report (§2.7) gives four instances:
- ε in F_{1²};
- χ₋₄ as the global sign;
- root numbers;
- Alpöge's (−1)^{D−1}.

The G219 computation has the same parity structure at coefficient 7. Complex conjugation exchanges the two cubic labels
χ and χ², so one exceptional residue serves both (𝓔₁ = 𝓔₂).

**(d) Induction relates two rungs.** Map 5 is automorphic induction K → Q, and the AGL_1 identity of CX_GRH
(ζ_{Q(p^{1/r})}/ζ = L(s, Ind ψ)) is the same move for every odd r. The pure-field zeta functions of GRH_ALGORITHMS
(RH for ζ_{Q(p^{1/r})}, the gate of its finite-field construction) are therefore the dihedral and AGL_1 rung, one step
above A. The cubic gate of ALP_CONNES and the field-construction gate of GRH_ALGORITHMS at r = 3 are the same family of
L-functions: RH for ζ_{Q(∛p)}/ζ, at p = 269 in one and at every hard p in the other.

## 4. What it suggests, most promising first
1. **Prove T50_K unconditionally** (the positivity half of the trace formula over Q(ω)). It is the T50 argument with a
   Hecke-character Möbius bound. The forward half would then be equivalent to the cubic gate's whole family. This puts
   the next rung in the same exact form as A.
2. **Compute 𝓔 of G219 through a 7-adic L-function** (from memory: Rubin's main conjecture for imaginary quadratic
   fields at a split prime; to be opened). Conjecture to test: s(e) = ord₇ of the Katz 7-adic L-value at
   χ^j ξ₇^a c₇^{−e}. That would identify the exceptional class 𝓔 and the s(e) that G219 leaves uncomputed.
3. **Compare the two deformations of §3(a) quantitatively.** At the level of limits this is done (§3(b), ZETA_HEAT cp03:
   lim a·j_*(−a) = ½ sup_{N,k} H_{N,k}², both sides equal to ½γ_*²). What is left is the rate: under A, bound
   m_*(−a) or j_*(−a) at a given a by D_{N,k} at an explicit N(a), k(a), and compare with the window eigenvalue
   a₂(L), whose needed lower scale is λ^{9+α}e^{−4πλ²}, λ = e^L, 0 < α ≤ 4 (upper scale λ^{13+ε}, ZETA_HEAT
   prop:odd-prolate-upper). The heuristic match a ~ 1/L² (earlier text here) is not supported by cp03. Direct compact
   cutoff of the theta profiles K^{(j)} only reaches e^{−2πλ²} (eq:theta-hier-22), half the prolate exponent.
   The final (23 Nov 22:19 UTC) adds an integer form of the same test, ind_+(TH_N − G_N) = n(T) at zero-free heights
   (prop:fd-inertia-complete, checked by us), and an unconditional all-window lower rate with exponent μ^{1/d_MT} in place
   of the needed μ = λ² (thm:cosine-lower-rate). The gap to close is that power of μ in the exponent.
4. **Treat the cubic gate across both runs** (the gate of ALP_CONNES at p = 269, and of GRH_ALGORITHMS at every hard p,
   r = 3) as one family of dihedral GL_2 L-functions. The GRH_ALGORITHMS almost-all theorems already bound the
   exceptional p. Ask whether ALP_CONNES's budget method extends uniformly in p.
5. **The basepoint interpolation L_t(s) = ζ(s, 1 + t)** (recall §2.6(b)). From memory (to be opened: Davenport-Heilbronn
   1936): for rational and transcendental shifts other than the classical ones, Hurwitz zeta functions have zeros with
   Re s > 1. So the interpolation leaves the Euler-product world strictly between the sheets t = 0 and t = 1. The
   statement to compute is where the zeros of ζ(s, 1 + t) go as t runs from 0 to 1, starting from those of ζ on the
   critical line.
