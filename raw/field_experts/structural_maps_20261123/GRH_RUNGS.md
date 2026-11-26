# Our GRH consequences on the rungs of global Langlands

Written 23 Nov 2026 by Claude Opus 5.5 at effort high (agent a25c2acbb3a6f11f7), for the main session 329fb1e6.

It is built from our intakes and primers in `field_experts/intake_20261121/intakes/`:
- GRH_NIGHT, CX_GRH, GRH_ALGORITHMS and GRH_ALGORITHMS_FINISH, MAS_ARTIN, ALPOGE_BRIDGES;
- AN_GRH, whose primer is by agent a28ea31f, Claude Opus 5.5 at effort max;
- ALP_CONNES and ALP_MACHINE (Hecke half).

**Status.** Every status below is a check event recorded in those intakes: "checked" means a targeted proof check by
Claude Opus 5.5 at effort high or max, as the intake records. The runs are GPT-6 Astra (ChatGPT Pro mode). Nothing here
is labelled from memory.

**Notation.**
- A: Alpöge's theorem, RH for every Dirichlet L-function. This is the GL₁/Q rung.
- M: GRH for the Hecke L-functions of a number field. This was Masullo's claim; his draft is not a proof, so M is an
  open hypothesis, used only conditionally.

## 0. The picture in one paragraph
Over Q the automorphic side runs GL₁ (Dirichlet) → GL₁ over number fields (Hecke characters) → Artin representations
(automorphic on GL_n by functoriality where known) → GL₂ (modular forms, theta series) → GL_n (symmetric powers, base
change). On the Galois side: finite abelian characters of G_Q, then of G_K, then finite-image representations of G_Q,
then 2-dimensional ℓ-adic ones, then their tensor and symmetric powers.

Almost everything our runs did is one of four moves:
1. **Descent by induction:** Artin formalism writes an L-function of the higher rung as a product of lower-rung ones,
   so A covers whatever lands in GL₁/Q.
2. **The single missing factor:** where induction does not land in GL₁/Q, the obstruction is isolated as one explicit
   L-function of the next rung.
3. **Positivity and trace:** a positive form or trace formula at one rung, and the exact way it breaks at the next.
4. **Avoiding the rung:** an algebraic or averaging argument replaces the analytic input entirely.

## 1. Rung GL₁/Q: Dirichlet L-functions (A, a theorem)
**What our runs made unconditional through A.**
- Algorithms:
  - Miller's test with bases below 2 log² n (CX_GRH CX-N01, checked);
  - r-th nonresidues for r | p−1 (CX-N02, checked), and in every supplied F_{p^m} (CX-N13, checked);
  - primitive roots from the factorization of p−1 (CX-N03, checked), and Shoup's g(p) ≪ log⁶ p (CX-N04, checked);
  - the order/factoring equivalence;
  - the least prime in a progression, ≤ (φ(q) log q)², and the Rubinstein-Sarnak limiting distribution
    (GRH_ALGORITHMS table, Q03).
- Abelian Dedekind ζ_K for K/Q abelian, via ζ_K = ∏_χ L(s, χ) (CX_GRH CX-R01, checked).
- Abelian Artin-Tate motives: L(⊕(χ ⊗ Q(n))^m, s) = ∏ L(χ, s+n)^m (ALPOGE_BRIDGES BR-AT-01, checked).
- Every unitary Hecke character of Q, χ₀|·|^{it} (GRH_NIGHT MT-A01, checked).
- Through Borger Λ-schemes over Spec Z[1/p], whose cohomology consists of Tate-twisted finite abelian characters
  (ALPOGE_BRIDGES CC-F01b, statement level).
- **Average versions over the input prime**, all under A (GRH_ALGORITHMS):
  - P074, P092-P095, checked;
  - P068 and P143, at statement level by us.

**The trace formula at this rung.** ALP_CONNES AC-T51: Connes's global trace formula over Q, for an explicit prolate
cutoff, is equivalent to A (deduction checked; the H27 editor notes that the statement is Connes's own). AC-S50, whose
proof we checked, reconstructs Ξ/Ξ(0) from prime-side data under A; it follows from Suzuki's norm convergence and is
his.

**What the next rung needs.** The GL₁/Q argument stops at the first L-function whose Galois side is not a character of
an abelian extension of Q. The two places our runs hit this are §2 (Kummer characters) and §3 (non-abelian Artin).

## 2. Rung GL₁/K: Hecke characters of number fields
**The one missing factor (GRH_NIGHT CX-ALG-024, checked; GRH_ALGORITHMS P001).**
- For F = Q(p^{1/r}), K = Q(ζ_r), E = K(p^{1/r}), the group G = AGL₁(F_r) = F_r ⋊ F_r^× has
  reg_G = (r−1)(P − 1) + Q, with P the permutation character on F_r.
- Hence ζ_E = ζ_K · (ζ_F/ζ)^{r−1}, and ζ_F/ζ = L_K(s, χ_{p,r}) for the order-r Kummer Hecke character χ_{p,r} of K,
  since P − 1 = Ind_{F_r^×}^{G} of a nontrivial character of the translations.
- ζ_K is covered by A. So the Hecke rung enters through exactly one L-function: **RH(L_K(s, χ_{p,r})) ⇔ RH(ζ_F) ⇔
  RH(ζ_E)** under A.

**The same object recurs in four places.**
| place | what L_K(s, χ_{p,r}) controls there |
|---|---|
| GRH_ALGORITHMS Q02 / P001 / P017 | the auxiliary prime ℓ ≪ r² log²(rp), hence F_{p^r}; a one-sided finite-window inequality for its prime sum suffices (P017) |
| ALP_MACHINE AM-H04 (H04.4) | the Landau-ramp window inequality G_p(y) ≤ C_θ y^θ on [Y, Y^{1+δ}], for every θ > 1/2, gives RH for it (checked given landau_window) |
| ALP_CONNES Q7 (p = 269, r = 3) | its arithmetic budget, as strict Selmer vanishing at coefficient primes (G114-G220); the exact 3-adic Selmer lengths and K-groups (AC-G22, K12, K21-K23, checked) |
| AN_GRH (Hooley) | Hooley's Artin density needs Dedekind GRH for Q(ζ_n, a^{1/n}), composite n (Kummer towers), already non-abelian at n = 3 (AN_GRH primer) |

So **P017 and H04.4 are the same gate**: a one-sided estimate for the prime sum of one Kummer Hecke character. The ALP
runs attack it from the arithmetic (Selmer and Iwasawa) side, and GRH_ALGORITHMS from the algorithmic side. AC-K09
proves the positive Weil window for r = 3, p = 269 through λ = 4 (checked, margin 1.282). That is a bounded window, not
the unbounded ramp.

**What the next rung, or a proof at this one, would need.** RH for L_K(s, χ_{p,r}). Concretely, a lower bound
Re Σ_{ℓ≤y} b_p(ℓ)(y/ℓ − 1) ≥ −C y^θ on late windows.
- The routes our records name (none tried to completion):
  - a cubic-phase analogue of Alpöge's sign mechanism through Patterson's cubic theta;
  - elliptic-unit index bounds uniform over host characters (AC-K25);
  - the K021 ray-theta Mellin period (ALP_MACHINE Q3), with a new arithmetic comparison.
- For r = 3 this is GL₁ over Q(ω). Dunn-Radziwiłł's bias of cubic Gauss sums assumes GRH for Hecke L-functions over
  Q(ω), a larger family than these Kummer characters (MAS_ARTIN cp15 intake, correction 2).

**Avoiding the rung.** Three ways appear.
1. **The small cofactor** (GRH_ALGORITHMS_FINISH P145/P144, checked). F_{p^r} is built with no Riemann hypothesis. The
   analytic auxiliary prime is replaced by algebra in the cyclotomic piece Φ_d(p) of the group order:
   - project to it;
   - search shifts, where the rational function H^{rC} must be constant;
   - use the odd-prime commutator;
   - for primes ℓ with r ∤ ℓ−1, adjoin Φ_ℓ, take the root, then the norm, then Bézout.

   The Hecke character χ_{p,r} is never touched: its Frobenius condition p^{(ℓ−1)/r} ≢ 1 is exactly what the cofactor
   algebra produces internally. **The dictionary:** an auxiliary prime ℓ with χ_{p,r}(Frob_ℓ) ≠ 1 corresponds to a
   non-scalar coboundary τ(c)/c of order prime to r in F_q[X]/(X^r − z).
2. **CM at fixed valuation** (P125/P126, the run's checks). For fixed (r, b) the needed root of unity comes from
   Frobenius of a CM abelian variety of dimension r^{b−1}, by Pila's point counting.
   - A is used only to find a small imaginary quadratic field in which p splits; that is GL₁/Q.
   - **So a Hecke-rung question is answered by the GL₁/Q rung plus CM geometry:** the CM Hecke character is algebraic,
     and its values are read off the variety, not off an L-function.
3. **Averaging over the input** (P074, P092, P143). Under A alone the auxiliary prime exists for all but O(√P log log P)
   primes p.
   - The Hecke rung's single-field question is replaced by orthogonality of Dirichlet characters modulo
     M = ∏ ℓ over the varying p.
   - The exceptional set is the exact shadow of the missing Hecke RH.

## 3. Rung: Artin L-functions
**Poles from the GL₁/Q rung** (GRH_NIGHT MT-S506, checked given the induction table). For every S₅ extension, the orders
of ζ, L_η, L_V, L_{Vη}, L_W, L_{Wη}, L_X satisfy seven linear inequalities, because Ind_J 1 = 1 + V,
Ind_T α = V + X, and so on, are Hecke L-functions. So every pole of an irreducible Artin factor in the strip lies at a
zero of ζ or L_η, and on the line by A. **A locates the poles of Artin L-functions; it does not remove them.**

**The S₅ gate reduced to one Hecke L-function** (MAS_ARTIN MA-FQ-004 with S5-001, LD-001, FQ-001-003, checked given
Calegari, Booker and Sanders). In Calegari's family, assume (R_B): B = ζ_H/ζ_F = L_F(s, η_F), a quadratic Hecke
L-function over the sextic F, has no real zero in (0, 1) other than 1/2. Then β = b + n, the GL₅ form ϖ matches the
Artin W at every place, and the irreducible Artin factors are automorphic and entire.
- The Hecke-rung input is not GRH but only the absence of real zeros, a Siegel-type statement.
- The Artin rung is reached through GL₅ automorphy (Calegari's base change BC(ϖ) = Sym⁴(π_E) ⊗ det^{−2}, as cited in
  MA-FQ-001).
- The positivity step: an excess central zero would make −m_R an integer-valued positive-definite function on ℝ_d,
  with atoms at log p for the infinitely many exceptional primes, which Cohen's theorem forbids.

**Zero location for Artin under M** (CX_GRH remark, §3 of its intake). By Brauer induction,
L(ρ, s) = ∏ L(ψ_i, s)^{n_i} with finite-order Hecke characters. So M places every zero of every factor on the line,
while holomorphy on the line is not given.

**The positivity obstruction at this rung** (GRH_NIGHT MT-M23, checked given HKMS, and MT-M20, checked given
MT-M18/19). For non-abelian Galois L/K, ζ_L = ∏ L(ρ)^{dim ρ} has infinitely many multiple zeros. So its full-jet
quotient has no faithful positive Hilbert completion. MT-M20 says this completion exists for a single L(s, η) iff GRH
with simple zeros holds. **The Connes-type positivity that works at GL₁ (AC-T51) fails at the Dedekind zeta of a
non-abelian field, by induction multiplicities.** It must be posed per irreducible ρ, not per field.

**What the next step needs.**
- (R_B) for explicit fields, by certified computation; or removal of (R_B). The gate is MA-RB-014's envelope
  inequality; MA-RB-016 shows the induced spin partner gives nothing new.
- For general Artin holomorphy, GRH_NIGHT names the matrix gate MT-ART02 (Θ_{s₀} positive semidefinite).

## 4. Rung GL₂: modular forms, theta series
**What our runs reached.**
- GRH_NIGHT MT-ART01, confirmed as a deduction: under M plus Khare-Wintenberger (Serre's conjecture, Corollary 10.2,
  as cited), every odd irreducible 2-dimensional Artin representation of G_Q has an entire L-function satisfying GRH.
  Holomorphy comes from GL₂ modularity; zero location from Brauer and M.
- Weight ≥ 2 GL₂ GRH is open (GRH_NIGHT NT-Z07).
- Alpöge's own mechanism lives here. His remark (p. 3, step 3, as our coordinator relayed on 21 Nov) averages
  χ ↦ χ(disc) through normalized Gauss sums carried by theta on the #μ_K-fold metaplectic cover of GL₂. So **the
  GL₁/Q theorem is proved from a GL₂ (metaplectic) theta object**.
- ALP_MACHINE builds the theta-lift chain (its lifts half is with agent abcaba9b). Its LIFT54/55 make the chain length
  m exceed 2^7778 under the formal size interface (SizesAt).
- ALP_CONNES uses GL₂ forms as tools at the cubic rung:
  - an auxiliary ordinary newform of conductor 3·3229 with nebentype ηθ (G119);
  - Eisenstein congruences at 269 that exclude the original Type II points (G116/G128);
  - all under retained modularity inputs.

**What the next rung needs.** The cubic analogue of Alpöge's step. Gauss sums of order 3 over Q(ω) are Fourier
coefficients of Kubota-Patterson's cubic theta on the 3-fold (with μ₆, 6-fold) cover of GL₂. An order-3 phase version of
the sign identity, the power-sum lemma with ζ₃^n in place of (−1)^n (deligne_sign_only_v5, Lemma tensor), would aim at
RH for Hecke L-functions over Q(ω), the first case of §2. This route is named in our records and not carried out.

## 5. Symmetric powers and GL_n
- **Calegari's Sym⁴** is the only higher-rank functoriality our runs used, through GL₅ in the S₅ chain (§3).
- **ALP_CONNES**:
  - ordinary rank-three forms at 269 with a determinant quotient, under retained automorphy inputs (statement level);
  - the M1-M5 model conditions for sixteen character/weight combinations (G139, statement level).
- **AN_GRH and Hooley:** the Kummer towers Q(ζ_n, a^{1/n}) need Dedekind GRH. By §2 these split under A into products
  of Kummer Hecke L-functions L_{Q(ζ_n)}(s, χ_{a,d}) for d | n. That reduction is exactly the pure-field identity
  applied to each prime-power layer, which our runs proved for prime r (CX-ALG-024) and not for composite n.

**What the next rung needs.** For Sym^k of a GL₂ form, RH would follow from GL_{k+1} GRH. None of our runs reached any
case.

## 6. The mechanisms that repeat
1. **Induction from AGL₁ or S_n down to GL₁.**
   - Instances: CX-ALG-024 (AGL₁(F_r)); MT-S506 (S₅); CX-R01 (abelian); the Brauer remark (all Artin).
   - Dictionary: a permutation character minus the trivial one is an induced character of a subgroup. The subgroup's
     abelian part is Dirichlet when the field is abelian over Q, and Hecke otherwise.
   - The rung reached equals the field over which the inducing character is defined.
2. **A positive form, and how it breaks.**
   - Instances: Weil positivity ⇔ RH at GL₁ (AC-T02, T51); MT-M20 (positivity on jets ⇔ GRH with simple zeros, one
     L-function); MT-M23 (fails for non-abelian Dedekind zeta, by dim ρ ≥ 2); MA-FQ-001-004 (positive-definite integer
     functions plus Cohen, at the Artin/GL₅ comparison).
   - The same object, a positive-type measure with atoms at log p, appears in AC-T51's Weil distribution and in MA-FQ's
     difference datum. In the first, positivity is equivalent to RH. In the second, positivity is automatic, from the
     Euler-factor signs at the exceptional primes, and integrality plus Cohen turns it into finiteness.
3. **One-sided window ⇒ RH.**
   - Instances: AM-H04 (Landau ramp on [Y, Y^{1+δ}]); P017 (finite window for the pure-field prime sum); AC-K09 (Weil
     window through λ = 4).
   - All three are the Landau-Ingham principle: a one-sided bound on a positive-coefficient Dirichlet series forbids
     zeros to the right. AC-K09 is the bounded-window case, the other two the asymptotic one.
4. **Algebra in place of analysis.**
   - Instances: P145 (the cyclotomic cofactor); P126 (CM Frobenius); P092 and P074 (averaging); A05 of AN_GRH (A1
     without GRH, by pro-r Kummer theory: AN_GRH primer §1).
   - The common shape: the analytic input chooses a prime ℓ with a Frobenius condition. The algebraic substitute
     produces the corresponding Galois-theoretic object directly, inside a finite étale algebra or a curve's
     fundamental group, where the Frobenius condition becomes an order condition on an explicit element.
5. **A Selmer or K-group length as the arithmetic side of a Hecke L-value.**
   - Instances: AC-K12/K23 (K_{2e}(O_E)_{(3)} ≅ Z₃[ω]/λ^κ with κ = 5 + 2v₃(e) + [e ≡ 2 mod 3]); the strict-vanishing
     families G114-G220; ALPOGE_BRIDGES R-KGROUP (K_{2n}(Z)/p as the ω^{−n} class component).
   - These are the Bloch-Kato / Lichtenbaum side of the same L_K(s, χ_{p,r}) whose zeros §2 needs. The ALP runs try to
     bound the zero side by the arithmetic side.

## 7. What it suggests, most promising first
1. **Prove the composite pure-field identity.** Under A, RH for ζ of Q(ζ_n, a^{1/n}) should reduce to the Kummer Hecke
   L-functions L_{Q(ζ_n)}(s, χ_{a,d}), d | n. Write the regular representation of the Galois group of the Kummer tower
   as a sum of induced characters, as for AGL₁(F_r). This would state Hooley's input (AN_GRH) as one family of Hecke
   L-functions, the same family as GRH_ALGORITHMS Q02.
2. **Make P145's dictionary exact.** Characterize the primes p for which the cofactor method succeeds without analysis
   as those whose χ_{p,r}-Frobenius condition is witnessed inside Φ_d(p). This would turn the algorithmic gap into a
   statement about the distribution of C_L, and of smooth values of Φ_d(p) over p.
3. **Pose the cubic sign identity at one test case.** For K = Q(ω) and χ = χ_{269,3}, compute the order-3 phase
   analogue of Alpöge's power-sum remainder, and see whether its trace is positive. This is the shortest path from the
   GL₂ (metaplectic) mechanism to §2's single missing factor.
4. **(R_B) on explicit S₅ fields.** Certify the absence of real zeros for B = L_F(s, η_F) on a few fields of Calegari's
   family, by interval arithmetic of the kind used in ALP_CONNES's class certificates. This would make the Artin
   automorphy of MA-FQ-004 unconditional field by field.
