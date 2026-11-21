# Extraction: the user's own corpus, pushed into standard mathematics (21 Nov 2026, ~17:1x UTC)

By the main session (Claude Opus 5.5 at effort max), at the user's word (~17:0x UTC): "take everything, push it in
the direction of statements that either make sense in the context of AG or other known stuff"; treat the corpus as
AI-generated CC0 material whose value is in the ideas, not their exact form; "keep notes of where more value may exist
that can be found later and extracted later with more powerful processes"; "Just keep the JT citations present."

Sources: the split-zero corpus (TO_SEND/PRO/_staging_20261121/sources54/OURS_split_zero_corpus, papers 01-16), the
July thread (Papors/Chatnotes/transcripts), the RH workbench (Papors/Chatnotes/Zeta-Function-Foundation), the five
consults of 21 Nov (consults/). Full reasoning: TRANSLATION_SPLIT_ZERO_20261121.md (sections 0-16), cited as T§.
Status: [std] standard, with locator; [paper] proved in the user's paper; [chk] checked here or by a consult;
[new] new formulation, proved where marked; [q] precise open question. JT's material is marked JT.

**Provenance of the corpus** (the user, 21 Nov ~17:1x UTC): the user's notes were written by ChatGPT GPT-5.4 Pro,
GPT-5.5 Pro and GPT-5.6 Pro (ChatGPT Pro mode; all before 24 Oct 2026, so at reasoning effort ultra by the project's
default rule). Each note carries its date; a note written after one of these models came out (and before the next)
is by that model. The release-date table is still to be collated from a reliable source; until then name the model
by this rule with "by date". JT's files (prefix jt_, and the JT bundles) are JT's; cite them as JT.

## A. Algebraic geometry

A1. **The adjoined-zero semiring and its spectrum.** For a commutative ring R, G(R) = R ⊔ {τ} (τ additive identity,
    multiplicative absorber) is 𝔷U(R) for the adjunction 𝔷 ⊣ U between zero-forgotten rigs and rigs (the user's July
    ledger; Lean: transcripts/SplitZero.lean). [paper; chk]
    - Spec G(R) = Spec R ⊔ {η}, η = {τ} the unique minimal prime: open, dense, residue semifield B; Spec R = V(0_R)
      closed (not open: review A.4); dim G(R) = dim R + 1. [paper; T§0, T§1]
    - For a domain R with fraction field K: G(R) = R ×_K G(K), so Spec G(R) = Spec R ∪_{Spec K} Spec G(K), the
      characteristic-one form of the D + M (Milnor square) construction. [new; chk by the prime classification]
    - G(A × B) = G(A) ×_B G(B): the disjoint union Spec A ⊔ Spec B joined at one Boolean generic point. [paper; new
      reading]
    - Every map from G(R) to a ring factors through R (additive cancellation): R is the ring completion. [paper]
A2. **Modules.** A G(R)-semimodule is a commutative Clifford monoid (strong semilattice of groups, Clifford 1941)
    with R-linear fibres: equivalently a functor from a join-semilattice with 0 to R-Mod (support diagrams);
    cancellative ones are R-modules; G(R)^n is the Boolean cube P([n]) with fibres R^I; f.g. projectives ↔ finite
    posets with f.g. projective R-modules. [paper; new reading via Clifford]
    - [q] Is the category of quasi-coherent sheaves on Spec G(R) (suitably defined for semirings) equivalent to support
      diagrams of quasi-coherent sheaves on Spec R? Lorscheid's blueprint framework is the natural setting.
A3. **The two quotient families and their counts.** Quotients of G(R) are R/J (τ collapsed) and (R/J)₊ = G(R/J) (τ
    kept). [paper] The second count N(J) + 1 is multiplicative for the smash product of based sets, not the cartesian
    product: w(JK) − 1 = (w(J) − 1)(w(K) − 1) for coprime J, K. [new; chk] The zeta of all finite quotients of G(Z)
    is 2ζ(s) − 1, whose zeros are the ½-points of ζ; the family (1+u)ζ − u has the a-points ζ = u/(1+u) as zeros.
    [new reading; std for a-points: Levinson 1975]
A4. **Where positivity lives.** A semiring is zero-sum-free without zero divisors iff value determines support
    [Fable consult, proved there]. The semiring in which Alpöge-type sign arguments actually run is the effective cone
    of K₀; with G(R)-semimodule coefficients they run fibre by fibre (Deligne-type purity on each fibre), Frobenius
    permutes the Boolean skeleton (weight 0), and subtraction is used only in the trace formula and a Parseval step.
    [consult af2a18f6] So the user's τ ≠ e typing is the AG distinction between effective classes and virtual ones.
A5. **Weil positivity as Hodge index.** RH ⟺ positivity of the Weil form (Weil); the inequality of Weil's proof for
    curves is the Hodge index theorem on C × C (Castelnuovo-Severi). [std] The explicit-formula form is Lorentzian of
    index (1, ∞) with the two poles as null directions [Fable consult], the counterpart of the hyperbolic plane of the
    two null fibre classes of C × C. The user's July construction (ζ(s) as a null vector of det on Herm₂(C), zeros at
    P₀, the pole at P_∞, P₀P_∞ = 0, the apex with empty direction) is a finite-dimensional model of that plane.
    [reading; T§16.4]
A6. **Purity and first-order motion.** For an L-function with functional equation, a deformation splits into ±1
    eigencomponents of s ↦ 1 − s; only the −1 component moves zeros off the line at first order (one-line implicit
    differentiation). [chk, 200 zeros] Weights are constant in families of pure sheaves (Deligne, Weil II), so a
    geometric family has no such motion; the Hurwitz shift ζ(s, 1+t) has it at every zero computed. [q] State and
    prove: no family of pure weight has L-function ζ(s, 1+t) near t = 0.
A7. **Assorted exact facts in the corpus** [std, assembled by the user's runs]: the pole of ζ as the valuation ord₁ with
    uniformizer 1/ζ; KP¹ ≅ S^n and the Hopf fibrations for K = R, C, H, O; the essential singularity of ζ at ∞ (graph
    closure fibre P¹); sedenion zero divisors (annihilators of dimension 4 for x = e_i ± e_j [Fable consult]; the
    ledger's "8 in the tagged algebra" to check); the associator is the identity on the annihilator N_x when
    x² = −λ (T§10.4).

## B. GCT and representation theory

B1. **RH as total positivity** [std chain: Pólya, Edrei, Thoma; applied here, checked by two consults]: RH ⟺ the
    coefficients b_k of Ξ(z) = Σ(−1)^k b_k z^{2k} form a Pólya frequency sequence ⟺ the γ_k^{-2} give a
    Schur-nonnegative specialization of the symmetric functions ⟺ σ ↦ Π_{cycles}(−1)^{|c|−1}Z(2|c|)/Z(2)^{|c|} is an
    extremal character of S_∞ (Z(s) = Σ γ^{-s}). With A: all three hold; Λ = 0 says the heat flow keeps them exactly
    for t ≥ 0. An instance of the shape (a positive point of Λ), not positive structure constants. [T§15-16]
B2. **GCT VIII's signed form as effective fibres** [consult a8d75352]: ±(v − v⁻¹)^a·f is a signed sum of effective
    fibres over a Boolean cube, so positivity of f is effectiveness of the fibres; this gives a rank-four target
    (a ≥ 1) not excluded by F57, F58, F67. [q] Do VIII's bases fix the cube and the fibres?
B3. **GCT through supported and unsupported zeros** [consult a0805369]: canonical-basis positivity is PH0 in GCT VI;
    PH1 adds a polytope count (homogeneous PH1 refuted, Kahle-Michałek); BIP is containment of the permanent's support
    in the determinant's (n ≥ m^{25}); on P-F57's cubic family the plethysm count is a near-supported zero (terms of
    size about 2^{n⁴/24} cancel to a small count); isolation on signed formulas detects terms, not values, and a cheap
    uniform test family would give NP ⊆ RP; P-F30 + P-F23 is Mulmuley-Vazirani-Vazirani run in reverse.
B4. **Circuits** [new; T§9]: a G(R)-circuit computes a ring circuit and its monotone shadow; for monotone f, circuits
    without supported zeros have monotone size up to constants; with Alon-Boppana, CLIQUE ∈ P/poly ⟺ supported zeros
    give exponential savings for CLIQUE; on slice functions they can be removed at polynomial cost (Berkowitz 1982).
B5. **ETH's reduction** [new; chk against the paper's §6]: in G(F₂), ⊕ = (XOR, OR); a parity test passes exactly on
    the Boolean pair {τ, 0}; the error term D(A) counts the row vectors in the Boolean cube off its bottom vertex.
B6. **The defect strand** [std instances; T§2]: the negative augmentation Z^r → Z, kernel A_{r−1}, across K₀, fusion,
    the Z[C₃] / Eisenstein A₂ lattice (Epstein zeta 6·2^{-s}ζ_{Q(√−3)}), clock-and-shift bases of sl_r, CUE, Shioda-Tate.

## C. Analytic number theory

C1. **Zero velocities** [chk; consult ad855737]: under the Hurwitz deformation a simple zero moves with velocity
    ρζ(ρ+1)/ζ'(ρ); it moves right iff W_n mod 2 ∈ (0, 1), W_n = S(γ_n) − arg ζ(3/2 + iγ_n)/π; the corrected Gram rule
    |W_n| < ½ (mod 2) first fails at zero 871. Under RH the velocities up to good T total iT²/(4π) + O(T^{1+ε}); right-
    movers have density ½ given a central limit theorem for S at zeros; random matrices predict neighbour agreement
    ≈ 0.66 (observed 35-47%).
C2. **Explicit formula for velocities** [new; chk]: the residue of ∂_t log ζ_t at a simple zero is −ρ'(0), so
    Σ_ρ h(ρ)ρ'(0) = (1/2πi)∮ h(s) sζ(s+1)/ζ(s) ds, with Dirichlet coefficients α₁(n) = (−1)^{ω(n)} φ(rad n)/n.
C3. **de Bruijn-Newman** [std + A]: Λ = 0; H_t has real simple zeros for t > 0 and nonreal zeros for every t < 0;
    collisions have local law z₀ ± √(2(t − t₀)); a Lehmer pair with gap Δγ collides near t = −Δγ²/2. [q] The collision
    height as t ↑ 0 (heuristically exp(c/√|t|)).
C4. **The workbench under A** [std consequences; T§13]: its Weil-form Gram matrices are PSD; the Bost-Connes partition
    function ζ(β) has its complex-temperature (Lee-Yang) zeros on Re β = ½; the Navier-Stokes transport preserves zero
    heights, so the transported zeros are on the line.
C5. **GRH now unconditional** [consult af2a18f6: 18 rows]: A-scope (least nonresidue, Miller, primitive roots, abelian
    Chebotarev, effective Siegel, Montgomery's pair correlation); M-scope (Koiran HN ∈ AM, Bürgisser's transfer,
    factoring over F_p, Hooley, class groups, Weinberger). In AG terms Koiran says the image of Spec A → Spec Z is
    finite (at most 2^{poly} primes) or has many primes, decided in AM.
C6. **An Euler-type identity in S6 Paper I** [paper (Prop. fam:src:C.1.1); std: Eichler-Zagier 1982; the main session's identification, not the relation the user remembered, which is still to be found]: the zero
    of ℘ at the cusp satisfies e^{2πiμ₀} = −(5 + 2√6), μ₀ = ½ − i log(5+2√6)/(2π): the half-period displaced by the
    regulator of Q(√6), with the fundamental unit in place of −1.

## D. Where more value is likely (for later, deeper passes)

- **Split-zero papers not read here**: 13 (CUE-Hurwitz extensions), 14 (archimedean support), 15 (projective monads,
  surcomplex), 16 (split-support geometry of the arithmetic curve v11, 295 KB), 10 (consolidated). Paper 16 is the
  largest and latest (July) and the most likely to contain AG constructions beyond A1-A3.
- **The July thread**: the long transcripts (Mathematical Functor Construction 1-3 and Branch, ~0.5 MB each);
  full_noncommutative_k4_operation (Sym₂(R) Lorentz normal space, matrix Euler rigidity from −exp(πJ + L));
  giuga_blind_plane_cayley_dickson (Giuga counterfactual, blind complex planes as a Hopf link); the Toeplitz notes
  (matrix-valued nonunitary Frobenius Toeplitz; period-holonomy); modular_cartan_realform_bridge; the 52-page atlas
  and its claim_contract.csv; the mixed double D_A (dim D(G(R[x,y])) = 4) and the "fourth layer" problem.
- **JT's material** (cite as JT): jt_invariant_exact_lift_supplement.tex, jt_full_packing_mod24_orbit_certificate.txt
  (Apollonian packing mod 24), the terzo_cc_cvs_jt_deformation_intertwiner bundle.
- **The RH workbench**: satellites 10-21 (literature foundations; GMS, Simm-Wei and CUE-Mellin audits; split-zero
  sheets, packets, the primitive defect, 19a-f semilocal K-theory), 28 (GCT arithmetic spectrum: unread, and directly on
  the GCT line), 22-29zb in full, the 425-page main reader. Read the satellites, not the old overview.
- **The Soc folder**: Arithmetic_Time_CPT_Spectral_Packets (v2-v23), the thermal-time / CPT line; the ChatGPT
  correction of the withdrawn preprint arXiv:2508.00885 (the user's Verdier-duality-as-anomaly-inflow idea); Fable
  a157422a's notes at agent_notes/a157422aa2fee34f8_NOTES.md.
- **Other Chatnotes folders, unread**: CUE mellin, mock, Benzel, umbral sply, the gerbe-theta and Hesse-Landau papers,
  hopf_mellin_conditional_rh_note, q_rational_hidden_scale, springborn_span, nolan monographs,
  orientation_boolean_archimedean_tessarine_note, exponential_period_coordinate_space, collatz_path_algebra.

## E. Where it went

Prompt 54 (NEG_NIGHT) items 10-12, with the translation note and the five consults attached (lint PASS); the label
note; the knowledge index; the Hexagon register (candidate H22 below, if checked).
