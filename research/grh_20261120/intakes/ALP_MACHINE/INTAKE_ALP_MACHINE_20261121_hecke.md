# Intake of ALP_MACHINE (prompt 49), the Hecke part (AM-H01 to AM-H19), checkpoint 04, 21-22 Nov 2026

Intake by Claude Opus 5.5 at effort high (agent af2a18f62da23b48e), launched by the main session (Claude Opus 5.5 at
effort max). The run: GPT-6 Astra (ChatGPT Pro mode); its hecke agent is `/root/cm_hecke`. Another agent (abcaba9b)
takes the lifts, seesaw, oscillator_sign and grothendieck parts.

## 0. What was read, and the scope

- **Return folder:** `research_returns\ALP_MACHINE_checkpoint_04_20261121T2304Z_unzipped\parts\hecke\`.
- **Read:**
  - `section.tex` lines 1-345 (scope, **AM-H01 to AM-H05 in full with their proofs**) and the statements of AM-H06,
    AM-H07 (with the start of its proof) and AM-H08;
  - the setup and the statements of AM-H09 to AM-H11 (`sign_characters.tex`);
  - the statements of AM-H12 (`determinant_tie.tex`), AM-H13 (`rallis_factors.tex`), AM-H14 (`unitary_seed_bound.tex`),
    AM-H15 (`parity_character.tex`), AM-H16 (`host_unit.tex`), AM-H17 (`host_realization.tex`), AM-H18
    (`finite_host_transport.tex`) and AM-H19 (`host_determinant.tex`);
  - QUESTIONS.tsv (all 17 rows), ATTEMPTS.md (the route table), the run's CHECK_EVENTS.tsv for AM-H, the four
    INDEPENDENT_REVIEW_*.md files, and the certificates.
- **Not read:** the proofs of AM-H06, AM-H08 and AM-H09 to AM-H19.
- **Scripts rerun** with `python -I -B` from my work folder `%TEMP%\alp_hecke`, on copies of the part's .tex and .json
  files:
  - `check_kummer.py`: **all_passed true**. It needed `SYMPY_GROUND_TYPES=python`, set inside the interpreter, because
    the installed python-flint makes sympy's `factor_list` sort fail. That is an environment issue, not a fault of the
    script.
  - `check_sign_characters.py`: **pass** (weight divisibility 7, coefficient modulus 1344, coefficient field degree 384,
    Minkowski bounds 10400/2187 and 14/9).
  - `check_unitary_seed_bound.py`: **PASS** (87,380 subsets, ranks 2-16; certificate H14_COMPUTATION_CERTIFICATE.json).
- **The run's own record.** Every AM-H finding has an author whole-proof check; AM-H15 also has an independent PASS.
  None of the four INDEPENDENT_REVIEW files reviews AM-H01 to AM-H14 or AM-H16 to AM-H19: they cover SS11, SS15, ST08,
  L11, ST11 and ST12. So this intake is the first independent check of most of the Hecke part.

## 1. Verdicts, finding by finding

Setting: K = Q(ζ_r), F = Q(α), E = K(α), α^r = p, r an odd prime, χ = χ_{p,r} a nontrivial character of
Gal(E/K) ≅ C_r. A = Alpöge's archive theorems.

| id | statement (short) | verdict |
|---|---|---|
| **AM-H01** | Ind_N^G χ is the irreducible (r−1)-dimensional augmentation representation of G = F_r ⋊ F_r^× (traces r−1, −1, 0). χ is not a norm pullback, and L_K(s, χ) is not a finite product or quotient of Dirichlet L-functions, even with finitely many Euler factors removed or with rational exponents. L_K(s, χ) = ζ_F(s)/ζ(s) | **confirmed** (targeted proof check). [FK:K] = r holds also for p = r. The character norm is ((r−1)² + (r−1))/(r(r−1)) = 1. Complex conjugation sends χ to χ^{−1} ≠ χ. The product obstruction goes through logarithmic derivatives and qualitative Chebotarev, ending in ⟨V, 1-dim⟩ = 0. Agrees with GRH_NIGHT CX-ALG-024 and my check of it. |
| **AM-H02** | the exact Euler product L_K^S(s, χ) = ζ_K^S(s) ∏_{ℓ∈𝒞_{p,r}} (1 − ℓ^{−s})^r/(1 − ℓ^{−rs}), with 𝒞_{p,r} = {ℓ ≡ 1 (r) : p^{(ℓ−1)/r} ≢ 1 (ℓ)}; the coefficients b(ℓ^m)/log ℓ = (r−1)·1[ℓ^m ≡ 1 (r)] − r·1[ℓ ∈ 𝒞, r ∤ m]; the r = 3 table (H02.3) | **confirmed** (targeted proof check), and **computation** by rerunning check_kummer.py: 387 Euler denominators checked by factoring X^r − p mod ℓ. I checked the cycle types (multiplier ≠ 1: cycles 1, f, …, f; nonzero translation: an r-cycle) and the coefficient extraction. |
| **AM-H03** | no number field containing E embeds in a cyclotomic field; no CM field contains E; so no Host containing E satisfies the archive's `IsChiField` | **confirmed**. Every embedding of a CM field commutes with complex conjugation, so c_E would be central in Gal(E/Q). But c_E = τ_{−1} inverts σ. Classical in substance. |
| **AM-H04** | with G_{p,r}(y) = Σ_{n≤y} b(n)(y/n − 1) + y·D(1) and D = L′/L: Φ(s) = ∫₁^∞ G y^{−s−1} dy = (sD(1) − D(s))/(s(s−1)), with residue m_ρ/(ρ(1−ρ)) at each zero. **If for some δ > 0 and every θ > 1/2 there are arbitrarily large Y with G(y) ≤ C_θ y^θ on [Y, Y^{1+δ}] (H04.4), then RH holds for L_K(s, χ_{p,r}).** (H04.4) is not proved | **confirmed given the cited archive theorem** `Deduction.landau_window` (in A's Lean archive; its statement was read by the run, and it is generic in (g, Φ, Z)). I checked: the Mellin identity (∫_n^∞ (y/n − 1) y^{−s−1} dy = n^{−s}/(s(s−1)), and ∫₁^∞ y^{−s} dy = 1/(s−1)); the residue sign, positive for real zeros in (0,1); b(n) real with \|b(n)\| ≤ (r−1)Λ(n), since V is defined over Q; and the reflection, since the conjugate character has the same L-function. This is a Landau-type one-sided criterion; new only as its instantiation for the Kummer character. |
| **AM-H05** | p = r: X^r − X − a is irreducible over F_r for a ≠ 0, giving F_{r^r} with no RH | **confirmed** (Artin-Schreier; β^{r^j} = β + ja); **computation** (34 cases, rerun). It is right that CX-ALG-024's hypothesis p ≠ r must be cited. |
| AM-H06 | Shapiro transport of the strict Selmer/Sha interface: an exact decomposition over the characters χ^j after ⊗O for ℓ ≠ r; at ℓ = r the Fourier embedding O[C_r] → ⊕O(χ^j) has elementary divisors 1, λ, …, λ^{r−1} and cokernel length c_r = r(r−1)/2, giving the comparison −c_r(d₂ + d_loc) ≤ (r−1)a_E(e) − b(e) ≤ c_r d₁ | **statement level; c_r confirmed.** The cokernel length equals v_λ of the Vandermonde determinant, r^{r/2} up to unit, i.e. (r/2)(r−1). The comparison inequality's proof was not read. |
| **AM-H07** | for K = Q(ζ₃), S = primes above 3p, n = \|S\|: d₁ = n+1, d₂ = n−1, d_loc = n+3; so −6(n+1) ≤ 2a_E(e) − b(e) ≤ 3(n+1): [−18, 9] for p ≡ 2 (3), p ≠ 3, and [−12, 6] for p = 3 | **confirmed by independent re-derivation.** d₁ from Kummer theory: O_{K,S}^×/3 has dimension n + 1 (rank n plus μ₆/μ₆³), and Cl_S[3] = 0 since h = 1. d₂ from Tate's global Euler characteristic: χ = 1 − 2 = −1 with one complex place. d_loc: H¹(Q₃(ζ₃), F₃) has dimension 4 (local Euler characteristic with μ₃ ⊂ K_v), plus one tame inertia dimension for the prime above p. These give the stated intervals with c₃ = 3. |
| AM-H08 | reduction to one Kummer character: all r−1 nontrivial summands have the same length t_{ℓ,χ}(e); exact a_{E,ℓ} = a_{K,ℓ} + (r−1) t_{ℓ,χ} for ℓ ≠ r; bounded defect at ℓ = r | statement level. The equal lengths follow from the Gal(K/Q) action on χ with a Galois-stable S. |
| **AM-H09** | the unitary algebraic Hecke character with infinity type ϑ_e exists, conductor one, trivial on A_F^×, iff W(e) = Σ_{a∈Ψ} a e_a ≡ 0 (112); for e_a = ε_a B this is exactly 7 \| B | **the "exactly 7 \| B" clause confirmed by my own computation**: Σ_{a∈Ψ} a ε_a ≡ 48 (112), and 48B ≡ 0 (112) iff 7 \| B. Also **computation** (the rerun of check_sign_characters.py). The full criterion (the Hasse unit 1 + ζ₁₁₂ raising 56 to 112, and invariant principal ideals) is statement level. |
| AM-H10, AM-H11 | signed characters with the IsMu0 finite prescriptions exist iff W(e) = 0; rationality (the value field contains E₁ = Q(ζ₇)); rigidity (the same restriction to all finite ideles forces the same infinity type, so the DtTied tie cannot be kept with a changed e) | statement level, plus **computation** (rerun). AM-H11's rigidity is the standard fact that a Hecke character is determined by its finite part (A_f^× L^× is dense). |
| AM-H12 | an explicit finite-idele and rational determinant tie: 𝒟 = μ_N × I_L^−, E_𝒟 surjective with open kernel, 𝒰 = E_𝒟(U_L), \|𝒰\| = N | statement level |
| AM-H13 | the finite standard parameters of the step-j Rallis local family, and the factorization of 𝓛_j^fin(t) into shifted Hecke L-functions; finite L-values nonzero | statement level (question ALP-Q1-RALLIS: PROVED_FINITE_L_VALUES) |
| AM-H14 | a uniform bound \|α_{v,a}\| ≤ Q^{C(k)} on the Satake parameters of unitary spherical representations of U(k) (unramified nonsplit) and GL_k (split), and a nonzero seed value for an arbitrary unitary seed π₀ | statement level, plus **computation** (rerun: 87,380 subsets PASS). The bound is in the line of the trivial bound for unitary spherical representations (Satake parameters in a bounded set; Tadić's classification). New only as stated uniformly. |
| AM-H15 | a parity character η₀ of K₀ = Q(√−7), of conductor 𝔭, with η₀,∞(z) = z/\|z\| and η₀ restricted to A_Q^× equal to ω_{K₀/Q}; its norm pullback η_T has the required local signs | statement level; the run records an **independent PASS** (H15_CERTIFICATE) |
| AM-H16 | for p ≡ 7 (16): a unit u_p of F_p = Q(ζ₁₆, √−p)^+ with sign τ(u_p) = sign τ(√p) at every real place, and h(u_p) ≤ ((p−1)/2) log 2 + log 105 | statement level |
| AM-H17 | the enlarged Host with a principal Jacobian-type lattice for C = Q(ζ_{2^{e+2}}, ζ₇), e ≥ 230, with CRT primes q ≡ 3 (8), d ≡ 7 (16) | statement level |
| AM-H18 | one finite isometry a with a·ā = κ, a·e = e fixes the whole selected half packet, and T_{j+1} Z T_j^{−1} = aZ on every edge | statement level; the author corrected an induced-model sign during review |
| AM-H19 | determinant cancellation: ∏ k_τ = 1, so changing the CM type on the fixed lattice AA costs no determinant (covolume) height | statement level. ∏_τ \|τ(κ)\| = 1 is the norm of a unit, consistent with the statement. |

**Counts.**
- Confirmed with every step checked: 5 (AM-H01, H02, H03, H05, H07; H07 by independent re-derivation).
- Confirmed given the cited archive theorem: 1 (AM-H04).
- Partial confirmation: AM-H06 (c_r); AM-H09 (its "7 | B" clause, by computation).
- Computation by rerun: AM-H01, H02, H05 (check_kummer); AM-H09-H11 (check_sign_characters); AM-H14
  (check_unitary_seed_bound).
- Statement level: AM-H08, AM-H10-H13, AM-H15-H19.
- Gaps: 0. Refuted: 0.

## 2. What is new, and how it bears on the programme

**The Kummer gate (H04.4) is the run's main open question (ALP-Q3: OPEN), and it is exactly the cubic-phase question
for r = 3.**
- AM-H01 to AM-H04 transfer the *analytic* half of Alpöge's steps 5-6 and 20: the Landau window, poles and residues,
  and the functional equation, to L_K(s, χ_{p,r}) = ζ_{Q(p^{1/r})}/ζ.
- The *arithmetic* half, the windows, is what the archive's `CharFamily`, `IsChiField` and `HostRaw.dir` supply for
  Dirichlet characters, and AM-H03 proves it cannot be supplied by a cyclotomic or CM host.
- **What the gate says (AM-H02).** The coefficient b(n) is a Dirichlet part (controlled by A) minus r times the
  indicator of the Kummer non-split set 𝒞_{p,r}. So (H04.4) is a one-sided statement: on long windows, the primes ℓ ≡ 1
  (mod r) at which p is an r-th power nonresidue are never too few, up to an error y^θ for every θ > 1/2.
- **For r = 3.** By cubic reciprocity, ℓ ∈ 𝒞_{p,3} iff the cubic residue symbol of a prime π | ℓ of Q(ω), evaluated at
  p, is ≠ 1. So (H04.4) is a one-sided equidistribution statement for cubic residue symbols over the primes of Q(ω):
  the territory of Patterson's cubic theta (Kubota cover) and of Heath-Brown's cubic large sieve. It is the same family
  as MAS_ARTIN's test character ψ_{269,3} and PF26's d = 3 residual.
- **The attack**, in the programme's terms. Make Alpöge's power-sum step supply (H04.4): an identity in which the
  remainder for the cubic-twisted family is c_k ζ₃^n (unit modulus) times an honest trace. The function-field
  power-sum lemma, which holds with any unit-modulus factor, then bounds every eigenvalue. AM-H04 converts the
  resulting window bound into RH for L_K(s, χ_{p,3}).

**The integral side (AM-H06 to AM-H08).** The Sha/Selmer interface of step 17 transfers by Shapiro to the CM base with
Kummer coefficients, with an explicit lattice-change cost. On Q(ζ₃) the cost is evaluated exactly (AM-H07). This
closes the finite-coefficient part of the gluing. The open obligation is a uniform bound on t_{ℓ,χ}(e), the Selmer
length of the single nontrivial Kummer character.

**The signed-character line (AM-H09 to AM-H19).** This is the "signed definite repair" of the lift count (Alpöge's
steps 7-8, the GGP/theta-lift chain), built inside the archive's Host interfaces:
- the existence conditions are exact (AM-H09, H10: W(e) ≡ 0 (112));
- the tie rigidity (AM-H11) forces the determinant ties to be rebuilt, which is done explicitly (AM-H12);
- the Rallis finite L-values are nonzero (AM-H13), with a uniform seed bound (AM-H14), a parity character (AM-H15),
  and an enlarged Host (AM-H16, H17) carrying the finite half packet (AM-H18) with no height penalty (AM-H19).

These remove arithmetic obstructions in the chain. ALP-Q1-RALLIS is proved at the level of finite L-values, while the
global non-vanishing of the iterated chain belongs to the lifts and seesaw parts. They do not touch the Kummer gate.

**In Grothendieck's terms.**
- The Kummer character is the rank-one ℓ-adic local system over Spec O_K[1/pr] attached to the μ_r-torsor
  x ↦ x^r at p. V is the Artin motive of the pure field F = Q(p^{1/r}) minus the unit motive.
- AM-H02 is its Euler factor as an SGA 6 λ-polynomial. AM-H06 is Shapiro, i.e. the corestriction of étale cohomology
  along Spec O_E → Spec O_K (SGA 4 IX).
- The run's own module records these readings.

## 3. Errata and literature points

- **No errata in what I read.** Correctly recorded by the run: the p ≠ r hypothesis of CX-ALG-024 (AM-H05), and the
  author's own correction of a lattice sign in AM-H18.
- **Literature:**
  - AM-H04's criterion is Landau-type (Ingham, *The Distribution of Prime Numbers*, ch. V; one-sided bounds suffice by
    Landau's theorem on Laplace transforms). The run cites the archive's Lean theorem as its input, which is right for
    the project, but the classical precedent should be named in a write-up.
  - AM-H03 and AM-H05 are classical.
  - AM-H14 is in the line of the trivial bound for unitary spherical representations; Tadić's classification gives
    sharper exponents.
- **Environment note for the record:** `check_kummer.py` fails under python-flint-backed sympy unless
  `SYMPY_GROUND_TYPES=python` is set. A one-line guard in the script would make it reproducible.

## 4. Hexagon readiness (the five tests of `field_experts\HEXAGON_CANDIDATES.md`)

- **AM-H04 with AM-H01/H02 ("RH for the Kummer Hecke L-function ⇐ one explicit one-sided window inequality").**
  - 1, complete: yes.
  - 2, self-contained: it depends on the archive's `landau_window`, an A-input; a classical Landau theorem would do.
  - 3, stable: no; the run is going and the gate is open.
  - 4, checked: yes, by me.
  - 5, interest: modest without the inequality.
  - **Not a post.** It becomes one only together with a proof of (H04.4) for some (p, r), which would be RH for an
    explicit non-abelian Artin L-function.
- **AM-H07** (exact constants), **AM-H09** (the 112 criterion): correct and checked, but internal to Alpöge's archive.
  **Not posts.**
- **AM-H09 to H19 as a block:** internal repairs of the archive's lift-count interfaces. No post. Gate: independent
  reviews, and the lifts and seesaw part (agent abcaba9b).
- **No finding of the Hecke part passes all five tests.**


## Full depth (added 22 Nov, same agent)

What I read further: the proofs of AM-H06 (section.tex lines 497-627), AM-H08 (lines 745-800), AM-H09
(sign_characters.tex lines 60-181), AM-H10 (lines 209-300), AM-H12 (determinant_tie.tex lines 1-130) and AM-H19
(host_determinant.tex lines 34-140), and the statement of AM-H15 with its setting. The checks are recorded in the same
CHECK_EVENTS file.

| id | verdict at full depth |
|---|---|
| **AM-H06** | **confirmed in full.** Checked steps: Shapiro (coinduction preserves injectives) together with the local and inertia transport; the integral splitting by idempotents for ℓ ≠ r; the Smith factors λ^k from the Newton basis, since N_k(ζ^j) = 0 for j < k and N_k(ζ^k) = λ^k·unit; the dévissage of Q = B/A into c_r trivial F_r-quotients, using μ_r ⊂ K and χ ≡ 1 mod λ; and the kernel/cokernel bounds c_r d₁ and c_r(d₂ + d_loc). The source O-length is (r−1)a_E because O/Z_r is totally ramified of degree r−1. The sign of (H06.3) follows from (r−1)a_E − b = ker − coker. |
| **AM-H08** | **confirmed in full.** Conjugation by τ_a (χ ↦ χ^a, cyclotomic character invariant, S Galois-stable) gives equal lengths for all nontrivial j. The j = 0 summand is K's Selmer group ⊗ O. Dividing (H06.3) by r−1 gives c_r/(r−1) = r/2. The r = 3 intervals are [−9, 4] and [−6, 3]: d₁ = n+1, d₂ + d_loc = 2n+2. |
| **AM-H09** | **confirmed in full.** Necessity: for a unit u, u/ū = z^k and ϑ_e(u) = z^{−kW}; the unit u = 1 + z has u/ū = z, and Φ₁₁₂(−1) = 1, which gives 112 \| W (roots of unity alone give only 56). Sufficiency: (α) ↦ ϑ_e(α)^{−1} is well defined on P_L i(I_F)/i(I_F); it extends through the finite class quotient with unit-modulus algebraic values; ψ_e = ϑ_e·A_e∘𝔦 is trivial on L^× and on A_F^×. The signed sum 400 + 464 − 480 = 384 ≡ 48 (112) agrees with my own computation. |
| **AM-H10** | **confirmed (the main part).** γ on K₀ = Q(√−7) (norm-Euclidean, units ±1) via the ratio v_𝔭/v_𝔭̄ is well defined and trivial on A_Q^×. Γ = γ∘N_{L/K₀} is trivial on A_F^× because N_{L/K₀} restricted to F is N_{F/Q}. Complete splitting of g_k gives the unit characters ω_k^{−2}. μ_j = Γ^{j+1}ψ_e works, and the converse holds by uniqueness. D = 7⌈(d+2)/7⌉ ∈ [d+2, d+8]. The coefficient-field clause rests on the class numbers of Q(ζ₇) and Q(ζ₇)^+: standard. |
| **AM-H11** | **rigidity confirmed:** two Hecke characters agreeing on all finite ideles agree at infinity, because L^× is dense in L_∞^× (weak approximation). The rationality clause (the value field contains E₁) is statement level. |
| **AM-H12** | **main part confirmed:** I_L/i(I_F) ≅ I_L^− by 𝔞 ↦ 𝔞/𝔞̄, using that L/F is unramified at all finite places (AM-L5); Γ(U_L) = μ_N with N = M/2, from lcm((g₀−1)/2, (g₁−1)/2) = M/2 since 16 \| g_k − 1; hence E_𝒟 is surjective with open kernel. The characters μ̃_{j+1}, χ_𝒟 and the relative determinant (H12.3)-(H12.5) are statement level. |
| AM-H13 | statement level: the parameters and the Rallis finite L-factor factorization; finite L-values nonzero |
| AM-H14 | computation (rerun PASS) plus statement level for the proof. See the literature note below. |
| **AM-H15** | **(H15.1) independently re-proved.** K₀ has class number 1 and units ±1, and η_∞(−1) = −1 for η_∞(z) = z/\|z\|. So a character of conductor 𝔭 = (√−7) exists exactly with η_𝔭(−1) = −1 on F₇^×, i.e. η_𝔭 = the Legendre symbol mod 7, since (−1/7) = −1. Its restriction to A_Q^× is sign × (·/7) = ω_{K₀/Q}. (H15.2)-(H15.3), the local signs, are statement level; the run records an independent PASS. |
| AM-H16, AM-H17, AM-H18 | statement level (the explicit unit with prescribed signs; the enlarged Host; the finite half-packet isometry). Not opened further within this round's budget. |
| **AM-H19** | **(H19.1)-(H19.4) confirmed.** ∏_τ k_τ = \|N_{F/Q}(κ)\| = 1 for a unit; N(AA) = (√d/rd(E))^g from (ξ)·AA·ĀĀ·𝔇 = 1 with \|N(ξ)\| = d^{−g}; Euclidean covolume (√d/2)^g times metric density (2/√d)^g = 1; the Gaussian scaling z = √k_τ y gives the factor ∏ k_τ^{b_τ}. The height formula (H19.5)-(H19.6) rests on AGHMP (2018), Def 9.1.4, and AM-L4: background. |

**Updated counts for the Hecke part.**
- Confirmed in full: AM-H01, H02, H03, H05, H06, H07 (independent re-derivation), H08, H09.
- Confirmed given cited inputs: AM-H04.
- Main part confirmed: AM-H10, H11 (rigidity), H12, H15 ((H15.1), independent re-proof), H19 ((H19.1)-(H19.4)).
- Computation by rerun: H01, H02, H05, H09-H11, H14.
- Statement level: AM-H13, H14 (proof), H16, H17, H18.
- Gaps: 0. Refuted: 0.

**Literature locators.**
- **AM-H04: Landau's theorem.** A Laplace transform of a function bounded on one side cannot be continued past a
  real singularity. The classical one-sided criterion for zero-free half-planes follows from it.
  - Locators, from memory and to verify: Montgomery-Vaughan, *Multiplicative Number Theory I* (CUP, 2007), §15.1,
    Lemma 15.1 (Landau's theorem) and the one-sided oscillation theorems there; Ingham, *The Distribution of Prime
    Numbers* (Cambridge Tract 30, 1932), ch. V.
  - AM-H04's windowed form, which needs a bound only on windows [Y, Y^{1+δ}], is the form in Alpöge's archive
    (`Deduction.landau_window`). The classical theorem assumes the bound for all large y. The window version is a
    refinement whose proof the run did not reproduce.
- **AM-H14: Tadić.** For a unitary unramified representation of GL_k over a p-adic field, the Satake parameters
  satisfy q^{−(k−1)/2} ≤ \|α\| ≤ q^{(k−1)/2}. This follows from Tadić's classification of the unitary dual of GL_n:
  Ann. Sci. ÉNS (4) 19 (1986), 335-382; locator from memory, to verify. AM-H14's Q^{C(k)} is of this form, with an
  unspecified C(k); comparison with (k−1)/2 would sharpen it. For quasi-split unramified U(k) I give no locator, and
  that comparison is open.


### Full depth, continued (22 Nov): AM-H13, AM-H14's proof, AM-H15's local signs, AM-H16, AM-H17, AM-H18

| id | verdict |
|---|---|
| **AM-H13** | **the nonvanishing conclusion confirmed, given the parameter computation (H13.3).** In (H13.4)-(H13.5) the earlier character blocks contribute L_fin(b, μ_iμ_j^{−1}) at integers b ≥ 1. For i < j, μ_iμ_j^{−1} is nontrivial, since the infinity types differ by ε_a D ≠ 0 (AM-H10). So L(1, ·) is finite and nonzero (Hecke's nonvanishing on Re s = 1), and b ≥ 2 lies in absolute convergence. The initial block has arguments ≥ (d−k+2)/2 > 1. Every omitted local factor (1 − α q^{−s})^{−1} with \|α\| = 1 is finite and nonzero for Re s > 0. The local parameters P_{j,w} themselves (H13.3, through Mínguez's unramified theta correspondence and the split-place twists) are statement level. |
| **AM-H14** (proof) | **targeted check of the structure, with the final inversion certified by computation.** For unitary spherical π_v, the T_b-eigenvalue satisfies \|λ(T_b)\| ≤ ‖T_b‖_{L¹} = vol(K t_b K) ≤ [K : K(ϖ²)] ≤ Q^{2k²}, because K(ϖ²) ⊂ K ∩ t_bKt_b^{−1} for exponents in {−1, 0, 1}. The Satake transform is triangular with nonnegative coefficients and leading coefficient δ_B(t_b)^{−1/2} ≥ 1 (H14.10). The step from bounds on all m_b(z) to max\|z_i\| ≤ Q^{C(k)} is the inversion (H14.14), which the rerun script certifies for ranks 2-16 (87,380 subsets). The proof is the standard "trivial bound" argument, made explicit. |
| **AM-H15** (H15.2)-(H15.3) | **confirmed.** At w ∤ 7 the pullback η_0∘N_{E/K₀} is unramified. At w \| 7 (e = 3, f = 2) the residue norm a ↦ N_{F₄₉/F₇}(a)³ composed with λ is nontrivial, so the conductor exponent is 1. E/F is unramified at all finite places and split at 7: in Gal(E/Q) ≅ (Z/16)^× × (Z/7)^×, the decomposition group at 7 is ⟨7 mod 16⟩ × (Z/7)^×, and −1 = (−1, −1) is not in it because −1 ∉ {1, 7} mod 16; the inertia groups at 2 and 7 do not contain −1 either. Hence a nonsplit v does not lie over 7, η_{T,w} is unramified there, and η_{T,w}(ϖ_v) = η_{E/F,v}(ϖ_v) = −1. I also checked the principal-idele computation of (H15.4)-(H15.5) and η_{0,𝔭}(7) = λ(−1)(−i)² = 1. |
| **AM-H16** | **the unit and its relative norm confirmed; the final sign choice statement level.** Each 1 − tz^a (tz^a a primitive 8p-th root of unity) is a unit, since Φ_{8p}(1) = 1. The sum of the residues is 0 mod p, so P̄_p = (−t^{−1})^{h_p} P_p = tP_p because h_p ≡ 3 (8), hence v_p = rP_p is real. v_p σ_p(v_p) = t Φ_p(t) = t(1 − t^{−1})/(1 − t) = −1 since t^p = t^{−1}. So the two real conjugates over each real place of R have opposite signs. The choice of signs by the circular units c₃, c₅, c₇ of R (the four-embedding sign table) and the height bound (H16.2) were not re-derived. |
| **AM-H17** | **the prime-choice clause confirmed; the Host construction statement level.** Primes q, d > max(B, 4tr+1, 11) with q ≡ 3 (8), d ≡ 7 (16), (−d/q) = 1 and (−d/ℓ) = 1 for every odd ℓ ≤ B exist. Choose d by CRT on d mod 16 and mod each odd ℓ ≤ B (−d a nonzero square mod ℓ), then by Dirichlet in that progression; then q in a progression mod 8d with q ≡ 3 (8) and q a square class making (−d/q) = 1, by quadratic reciprocity and Dirichlet. The field, Frame/Host verification and principal polarization were not re-derived. |
| **AM-H18** | **core confirmed; the Weil/Heisenberg transport statement level.** a with aā = κ and ae = e exists: at selected split places take a = (1, κ); at other split places any splitting pair; at nonsplit unramified places use surjectivity of the unit norm, by Hensel lifting with the residue trace, valid also at 2. T_j = a^j I gives T̄_jᵀ(κ^{−j}I)T_j = (aā)^j κ^{−j} = I; T_{j+1}ZT_j^{−1} = aZ; βaā = ξ gives (H18.4); all factors are scalar units, so the lattices and AA are preserved. The literal equality (H18.6) Φ(a^{−1}z) = Φ(z) for half-supported Φ, and the Weil intertwiner (H18.5), were read only at statement level. |

**Final counts for the Hecke part.**
- Confirmed in full: AM-H01, H02, H03, H05, H06, H07, H08, H09; H15 (all of it, now including (H15.2)-(H15.3)).
- Confirmed given cited inputs: AM-H04 (the archive's landau_window), AM-H13 (given the parameters (H13.3)), AM-H14
  (given the script-certified inversion).
- Main or core part confirmed: AM-H10, H11, H12, H16, H17, H18, H19.
- Never only at statement level any more: every finding now has at least its core checked.
- Gaps: 0. Refuted: 0.
