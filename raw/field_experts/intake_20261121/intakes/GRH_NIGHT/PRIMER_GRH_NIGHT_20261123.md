# Primer: GRH_NIGHT (prompt 42), "everything that follows from the two proofs"

Written 23 Nov 2026 by Claude Opus 5.5 at effort high (agent a25c2acbb3a6f11f7). It is a recall of the run and of our
intakes; nothing new.

**The run and its final.** GPT-6 Astra (ChatGPT Pro mode). The final return is checkpoint 07 (21 Nov 06:17 UTC). Line
numbers below refer to
`research_returns\GRH_NIGHT_checkpoint_07_20261121T0617Z_unzipped\GRH_NIGHT.tex`.

**Our intakes.** Three, of checkpoints 02, 04 and 07, by Claude Opus 5.5 at effort high (agent af2a18f62da23b48e), in
`intakes/GRH_NIGHT/`.

**Inputs.**
- A: Alpöge's theorem, RH for every Dirichlet L-function.
- M: GRH for the Hecke L-functions concerned. This was Masullo's claim. His draft is not a proof, so M is an open
  hypothesis.
- PF26: OpenAI's preprint "Deterministic Polynomial Factorization over Prime Fields", 4 Oct 2026, Theorem 1.2 and
  Proposition 10.1.

## 1. Finite fields and factoring
**CX-ALG-016** (l. 13989), refuted by counterexample: the literal fixed-generator resolvent of Bhargava-Ivanyos-Mittal-
Saxena 2017, Theorem 3.1, can vanish. In F₇[X]/(X³ − 2) with ζ = 4, L = α + 4α⁷ + 2α⁴⁹ = 21α = 0. The cubes mod 7
are {0, ±1}. Arithmetic checked.

**CX-ALG-017** (l. 14011), unconditional, checked: the repair. Some basis element α^j gives β = Σ ζ^i (α^j)^{Q^i} ≠ 0,
because the linear map has degree Q^{r−1} < |E|. Then β^{Q−1} = ζ^{−1}, and S/r ≡ 1 mod r makes β an r-th nonresidue.

**CX-ALG-018** (l. 14067), unconditional, checked: the even-degree quadratic case without GRH.
- If Q ≡ 1 mod 4, take u = α^Q − α.
- Otherwise use F_{p²} = F_p(i) and norm-one square-root doubling: (x + yi)² = a + bi, with δ₊δ₋ = −b²/4 a non-square.

**CX-ALG-023** (l. 14621), unconditional, checked: for primes r ≠ p, a supplied F_{p^r} gives the maximal coefficient
Teichmüller unit η ∈ 𝒟_r = F_p[T]/Φ_r, of order R = r^a with ρ_c(η) = η^{ω(c)}, and conversely (after Lenstra 1991,
Theorems 5.1-5.2).
- Mechanism: from a normal basis element β with σ(β) = ζ^{−1}β, form y = ∏ ρ_c(δ)^{ω(c)^{−1}}; then y^R = ζ.
- Descent to 𝒟_r uses gcd(s, r) = 1.

**CX-ALG-024** (l. 14723), under A, checked: RH(ζ_{Q(p^{1/r})}) ⇔ RH(ζ_{Q(ζ_r, p^{1/r})}).
- Mechanism: on AGL₁(F_r), reg_G = (r−1)(P − 1) + Q, where P is the permutation character on F_r, i.e.
  ζ_E = ζ_K (ζ_F/ζ)^{r−1}.
- With |D_E| ≤ r^{r(2r−3)} p^{(r−1)²}, Bach-Sorenson gives q ≤ O(r⁴ log²(rp)) with p^{(q−1)/r} ≢ 1, hence F_{p^r}.
- Use: it names the one zeta function per bad prime that A leaves.

**At statement level:** CX-ALG-025/026 (factoring and construction under A plus RH for the pure fields, only at the
encountered bad r), and CX-ALG-021 (genus quotient mixing under A).

**CX-ALG-027** (l. 15371), PF26 + M, confirmed as a transfer (PF26 not opened by us): factoring of degree d over a
supplied F_{p^m} in time poly(d, m log p).
- Analytic input: RH for ζ_Q and for E_{p,r} = Q(ζ_{12r}, p^{1/r}), r ≤ d.
- It gives an explicit auxiliary prime ℓ ≤ [16r² log(12r²) + 16r(r−1) log p + 10r² + 5]² with ℓ ≡ 1 mod 12r and
  p^{(ℓ−1)/r} ≠ 1. 2, 3, p and r are excluded by ramification.
- Small characteristic p ≤ B^{200000} is handled by Berlekamp; the passage to F_{p^m} goes through the Berlekamp
  subalgebra.

**CX-ALG-028** (l. 15501), PF26 + A + the pure fields at bad r: the same; the first part was read.

These became GRH_ALGORITHMS (prompt 67); see its primers.

## 2. Positivity and Hilbert completions (the zero-side infrastructure)
**MT-M20** (l. 18843), checked given MT-M18/M19: for a fixed L(s, η), "GRH with all nontrivial zeros simple" ⇔ "there
is a faithful positive-definite continuous inner product on the full jet quotient, with bounded convolutions and every
C_{h∗h♯} ≥ 0".
- (1) ⇒ (2): diagonal trace class from the zero count; under GRH, h♯ has conjugate entries.
- (2) ⇒ (1): an off-line pair of idempotents gives h∗h♯ = −(e + e†), which is negative. A multiple zero gives a
  nilpotent N with iN self-adjoint, from h_u = e + iuN at u = ±1, so N = 0.

**MT-M23** (l. 19513), checked given Hu-Kaneko-Martin-Schildkraut, Theorem 1.1: for every nonabelian Galois L/K, ζ_L has
infinitely many multiple zeros (immediate from ζ_L = ∏ L(ρ)^{dim ρ}). So its full-jet quotient has no faithful positive
Hilbert completion. Also limsup I_L(X)/(log X)³ > 0 for the Möbius mean square.
- Use: it limits every "positive operator realizing the zeros" programme for Dedekind zeta functions.

At statement level:
- MT-M18/M19: unconditional closed-ideal synthesis, nuclear convolution, trace positivity ⇔ GRH.
- MT-M24/M26: Meyer's quotient and the trace-class strip quotient.

These feed MAS_ARTIN's MA-HM-001/003.

## 3. Artin L-functions
**MT-S506** (l. 25778), under A, checked given the induction table (S506.6): for every S₅ extension of Q, the orders
(a, b, c, d, x, y, e) of ζ, L_η, L_V, L_{Vη}, L_W, L_{Wη}, L_X at a point z satisfy a+c, b+d, a+y, b+x, e, c+e, d+e ≥ 0.
- Mechanism: each left side is a Hecke L-function attached to an induced representation, e.g. Ind_J 1 = 1 + V and
  Ind_T α = V + X, so it is holomorphic in the strip.
- Consequence: every pole of an irreducible Artin factor in the strip lies at a zero of ζ or L_η, and so on the line
  by A.

**MT-ART01**, under M plus Khare-Wintenberger (Corollary 10.2), confirmed as a deduction: every odd irreducible
two-dimensional Artin representation of G_Q has an entire L-function satisfying GRH. Holomorphy comes from Serre's
conjecture; zero location from Brauer induction and M.

At statement level: MT-S504/505/507/508 (the Calegari family reduced to one central-order inequality β − b − n ≥ 1,
continued in MAS_ARTIN), and MT-ART02/09/10.

**MT-A01** (l. 15734), checked: A gives GRH for every unitary Hecke character of Q, χ₀|·|^{it}. Ẑ^× is profinite, so the
character has finite image.

## 4. Masullo's draft: located defects, checked against its PDF
These are statements about the draft, which is not a proof.
- **MT-M01** (p. 425, Lemma 9.3.2.4): the O(log T) zero count is false for general φ. φ(e^u) = (g_{1+i} − g_{1−i})/2i
  has Mφ(s) = e^{s²} sin(s²), with zeros i√(kπ). The proof needs a lower bound that it never derives.
- **MT-M02** (p. 426, Theorem 9.3.2.6): the proof uses W_{≤T} ⊂ W_{≤T′}, but these intersections decrease.
  Counterexample: one zero at 0. The repair is MT-M03.
- **MT-M05** (pp. 425-426, Lemma 9.3.2.5): false without closure of the ideal. Take Mh = s e^{bs²} and
  Mφ = s e^{as²} with a > b.
- **MT-M36** (p. 495, (11.3.2.2)): under the draft's own conventions the section average is identically zero, since
  Haar measure on I_F¹ is atomless, so the normalization (12.2.1.2) on p. 505 fails. Found independently by
  ALPOGE_BRIDGES F-SM-19.
- **MT-M34** (p. 480, Theorem 11.1.2.1(2)): in the Q trivial sector both cut-off closures coincide for every Λ, so the
  claimed strict inclusion fails. Core lemma checked; the identification with the source spaces is statement level.
- **The decisive gap**, left open by the run: Q-MAS-GEOMETRIC-NARROW, the geometric trace equality on narrow strips
  independent of zero location (§§12.3-12.4). MAS_ARTIN later showed that this step is equivalent to RH in the
  corrected model (MA-HM-003).
- **Corrections to our own intakes:**
  - "Every literal defect has a repair" was too strong: p. 480 needs a missing condition, and some later rows have none.
  - "The trace identity over Q is known to hold" meant only the numerical identity F-SM-13, at statement level.
  - §12.3 was not checked on the PDF by us.

## 5. Grothendieck, cote 34, Remark 1.17 (our bridges Q03)
- **AG-C34-REPAIR**, checked: for any pro-ℓ quotient H of inertia with π-stable kernel, K = closure of ⟨[p, h]⟩ is open
  in H, H/K ≅ (H^{ab})_{π₀}, and [H : K] ≤ |I(ℓ)_{π₀}| < ∞. This is by Grothendieck's own Theorem 1.1 of cote 34
  (PDF p. 53).
- **AG-C34-INDEX**, checked: |coker(F − 1 | M)| = |T^F|·ℓ^{v_ℓ det(1−F)}. For a curve it is ℓ^{v_ℓ #J(F_q)}.
- **AG-C34-SECTION**, checked: with a chosen section and H solvable of finite derived length, the action commutators
  are open.
- AG-C34-TYPE: the literal remark is false for infinite π₀.

## 6. Open rows and where the results went
**Open:**
- Q-MAS-GEOMETRIC-NARROW (now: equivalent to RH, MA-HM-003);
- GL₂ GRH in weight ≥ 2 (NT-Z07);
- general Artin holomorphy (MT-ART02, the Heilbronn matrix gate) and the S₅ central gate (continued in MAS_ARTIN);
- full GUE statistics; general derandomization.

**Where the results went:**
- CX-ALG-016-028 → GRH_ALGORITHMS (prompt 67, 67c).
- MT-M18-M26 → MAS_ARTIN (prompt 48).
- MT-S506/S508 → MAS_ARTIN's S₅ chain and seed `SEED_MAS_ARTIN.md`, Paper 1.
- The Masullo defect table → `TO_SEND\PRO\_staging_20261121\cores\MASULLO_DEFECTS_20261121.md`.
