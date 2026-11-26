# Intake pile, cluster ZETA_GRH: zeta and L-functions, GRH algorithms, theta and trace runs

Written 24 Nov 2026 by a cluster reader launched by the main session 329fb1e6 (Claude Opus 5.5 at effort max); the reader is
Claude Opus 5.5 at effort high. Brief: `reports_20261124/INTAKE_PILE_20261124/BRIEF.md`. Running notes:
`agent_notes/20261124T2111Z_Intake_pile_zeta_and_GRH_cluster_NOTES.md`. Items: `ZETA_GRH_ITEMS.tsv`. Check events:
`INTAKE_<RUN>_20261124_CHECK_EVENTS.tsv`, one per run, in this folder.

**Runs.** GRH_ALGORITHMS (67), GRH_ALGORITHMS_FINISH (67c), GRH_NIGHT (42), ZETA_HEAT (62), ZETA_NEXT (43), ZETA_TWO (35),
THETA3 (37), TRACE_DET (33), HECKE_DIV (38), DEG_L (41), SIGN_NEXT (45). Every run is GPT-6 Astra (ChatGPT Pro mode); TRACE_DET
and DEG_L record their effort as "not exposed" (the mode is ChatGPT Pro). Codex's edition of 67c is by GPT-6.2 Astra at
reasoning effort ultra.

**Inputs named throughout.**
- **A** = Alpöge's theorem (20 Nov 2026, Lean-formalized): RH for ζ and for every Dirichlet L-function. Used as a theorem.
- **M** = GRH for Hecke L-functions as claimed in Masullo's draft. Not a proof: results resting on M are conditional and
  get no credence (memory note "Masullo's draft: not a fix, no credence").
- **PF26** = OpenAI's preprint "Deterministic Polynomial Factorization over Prime Fields" (4 Oct 2026). **032** = OpenAI's
  family-032 proof of the Hodge conjecture for CM abelian varieties (unrefereed; human proof van Hoften–Sempliner, Hexagon
  2610.00259).

**Paths.** Run folders are under `grothendieck_archive_transcription_20261110/research_returns/`; earlier intakes and
primers under `field_experts/intake_20261121/intakes/<RUN>/`.

**What is new since the earlier intakes.** No run of this cluster has a return newer than its last intake: every newest
folder (GRH_ALGORITHMS cp08, FINISH cp07, GRH_NIGHT cp07, ZETA_HEAT final, ZETA_NEXT final, ZETA_TWO final, THETA3 cp07,
TRACE_DET final, HECKE_DIV final, DEG_L cp06, SIGN_NEXT cp02) was already taken in, and each run has a primer of 23 Nov that
folds its intakes together. Since then:
- the 67c paper was **posted on Hexagon as 2611.00987v1** (24 Nov 11:25 UTC, session 672ae3a0, Claude Opus 5.5 at effort
  max; record `reports_20261124/grh_algorithms_67c/RECORDS.md`);
- this intake recorded **eighteen new check events** across all eleven runs (§ "Checks made by this intake" at the end), among them the first reading by us of
  the proofs of the posted paper's new headline theorem (P148, P149, and part of P147), the first check of ZETA_HEAT's
  all-window lower rate, of THETA3's explicit Weil cycle C32, of DEG_L's B20–B21, and a computation of GRH_NIGHT's S₅
  induction table.

**Check labels.** "Checked by us" = a check event by Claude Opus 5.5 at effort high in an intake (the agent is named). "Run
only" = the run's own checks (GPT-6 Astra, ChatGPT Pro mode). TPC = targeted proof check.

---

## 0. The cluster's most interesting items, ranked by usefulness

1. **Finite fields of prime degree: the 67c paper, now on Hexagon (GRH_ALGORITHMS_FINISH, P144/P145/P149, with
   P125/P126).** Lenstra's problem: given p and a prime r, construct F_{p^r} deterministically. The paper proves an
   *unconditional* construction in time polynomial in r, log p and the cofactor of Φ_d(p) left after removing 2, r and
   every prime ℓ ≤ L with r ∤ ℓ−1 (P144, P145; d = ord_r p), and, under A, the stronger Theorem 1.2 (P149): for fixed r
   and t one may also remove every ℓ ≤ L with v_r(ℓ−1) ≤ t. Under A it also settles every fixed stratum (r, b) of the
   r-adic valuation v_r(p^d−1) = b by CM theta functions and Pila's point counting (P125/P126). Why it matters: these are
   deterministic constructions whose only analytic input is Dirichlet GRH, now a theorem, on explicit input classes; the
   paper itself says the general problem is already solved by OpenAI's prime-field theorem with Shoup's reduction (and by
   a further cited paper the user asked not to be read), so its value is the A-only and unconditional routes. Checks:
   P144/P145 TPC by us (a25c2acb, 23 Nov); the five Codex fixes checked by us (24 Nov); **P148 and P149 (given P147) TPC
   by this intake, P147 read in part.** Codex (GPT-6.2 Astra at reasoning effort ultra) read all 18 new statements.
   Where: `reports_20261124/grh_algorithms_67c/source_v1/grh_algorithms.tex`, Thm 1.2 at l.202, Prop 16.1 l.3714,
   Lemma 16.3 l.4178, proof of Thm 1.2 l.4261.

2. **Effective class-number and CM-orbit bounds from A (ZETA_NEXT NX01–NX02, NC01–NC04; Hexagon candidate H15).** For
   every normal K ≠ Q, Res_{s=1} ζ_K > 1/(173 log D_K); for every K of degree n, > 1/(173·n!·log D_K) (NX01, NX02); hence
   explicit lower bounds h_E ≥ h_E/h_F > c_g D_E^{1/4}/(log D_E)^g for CM fields (NC01), an explicit averaged-Colmez height
   bound (NC02) and Galois-orbit lower bounds for CM points with explicit exponent (NC03, NC04). Why: Stark's descent sends
   the only possible exceptional zero of a normal field to a quadratic Dirichlet L-function, which A excludes; so
   Siegel-ineffective constants in the Brauer–Siegel/André–Oort chain become explicit. Checked by us step by step
   (ad855737). Superseded in its exponent by NIGHT_AFTER_ALPOGE A.ORBIT (1/(4g)), which is now H15. Where:
   `ZETA_NEXT_final_20261121T0340Z_unzipped/normal/findings.tex`, `cm/findings.tex`.

3. **An exact arithmetic test for the simplicity of the Riemann zeros (ZETA_HEAT thm:fd-arithmetic-complete and
   prop:fd-inertia-complete).** Under A, with Suzuki's compressions C_N of the Weil operator: D_{N,k} = S_k − tr C_N^{2k}
   decreases in N to 2Σ(m_γ−1)γ^{−2k}; the zeros up to height T are all simple iff some D_{N,k} < 2/T^{2k}, iff the
   integer ind₊(TH_N − G_N) reaches n(T) for some N. Every quantity is computed from Λ(n) and archimedean integrals, with
   no zero ordinate. Why: a finite, prime-side, exact criterion; the run certifies it to height 97.632. Checked by us
   (afa2696b: proof, six certificate rows replayed, the integer test computed at three heights). The certificate height is
   tiny against known verifications of simplicity; the interest is the criterion. Where:
   `ZETA_HEAT_final_20261123T2219Z_unzipped/workbench/paper/sections/arithmetic_compressions.tex`, `inertia_density.tex`.

4. **Corrected forms of two of Grothendieck's statements on the Hodge-index route (SIGN_NEXT SN-C04, SN-44-01; H04).**
   Cote 16 scan 050: C_G(X) ⟺ C_G(Y) + R₀(T,W) + G_{L,0}(T,W), with W a hyperplane section of T = X×X and the missing
   factor L_T restored (in substance Kleiman 1968, Th. 2.13). Cote 44 Theorem 5: the height pairing needs the correction
   −Σ_s a_s(Z)ᵗG_s⁻¹a_s(Z′) over singular fibres; explicit P²×P² example 0 = 3 − (1+1+1). Why: citable correct versions of
   archive statements, needed for the cote 16 and cote 44 companions. Checked by us (aaf69461). Where:
   `SIGN_NEXT_checkpoint_02_20261121T0430Z_unzipped/SIGN_NEXT.tex` l.334 (SN-C04), l.4229 (SN-44 block).

5. **Bounded division is equivalent to algebraicity, and the Hecke-orbit dichotomy (HECKE_DIV R21–R23, P0).** For a flat
   Hodge class t on a polarized abelian family, {c_t ≤ C} is Zariski closed; t is algebraic everywhere iff c_t is bounded
   on a Zariski-dense set; a tensor-compatible Hecke orbit is dense; if c_t is unbounded it tends to ∞ along every
   strictly special-generic CM sequence (André–Oort, Tsimerman). Why: the reduction that the Hodge-division papers stand
   on (HODGE_FINISH Paper A). Checked by us (aaf69461; R21 checked again by this intake). Where:
   `HECKE_DIV_final_20261121T0204Z_unzipped/HECKE_DIV.tex` l.80–162.

6. **Two corrections to published algorithms literature (GRH_NIGHT CX-ALG-016; 67c P163).** (a) The literal
   fixed-generator resolvent in Bhargava–Ivanyos–Mittal–Saxena, ISSAC 2017, Theorem 3.1, can vanish: in F₇[X]/(X³−2) with
   ζ = 4, L = α + 4α⁷ + 2α⁴⁹ = 21α = 0; the proof divides by L. CX-ALG-017 repairs it (some basis power gives a nonzero
   resolvent). (b) The literal power-replacement loop of Guo's thesis (arXiv:1706.10028v2, Lemma B.1, with Hypothesis (*)
   needing "a supplied prime k | p^d − 1") misses solutions: F₁₉, x = 4, y = 9 = x⁴. Neither refutes the source's main
   theorem. Checked by us (af2a18f6; a25c2acb). These are corrections to report to their sources.

7. **Where the poles of S₅ Artin L-functions can be (GRH_NIGHT MT-S506).** For every S₅ extension of Q, with orders
   (a,b,c,d,x,y,e) of ζ, L_η, L_V, L_{Vη}, L_W, L_{Wη}, L_X at z in the critical strip: a+c, b+d, a+y, b+x, e, c+e, d+e ≥ 0,
   so every pole of an irreducible Artin factor lies at a zero of ζ or of L_η, hence on Re z = ½ by A. Why: a clean
   unconditional-given-A statement on Artin holomorphy for S₅, the seed of MAS_ARTIN's S₅ chain. Checked by us
   (af2a18f6, given the induction table); **the seven induction identities computed by this intake.** Novelty
   unsearched (the method is the classical Heilbronn–Stark character argument). Where:
   `GRH_NIGHT_checkpoint_07_20261121T0617Z_unzipped/GRH_NIGHT.tex` l.25778–25918.

8. **No positive Hilbert realization of the zeros of ζ_L for nonabelian L/K (GRH_NIGHT MT-M20, MT-M23).** For a fixed
   L(s,η), "GRH with all zeros simple" ⟺ a faithful positive-definite continuous inner product on the full jet quotient
   with bounded convolutions and C_{h∗h♯} ≥ 0 (MT-M20); since ζ_L has infinitely many multiple zeros for nonabelian L/K
   (after Hu–Kaneko–Martin–Schildkraut, Thm 1.1), no such completion exists for ζ_L (MT-M23). Why: it limits every
   "positive operator whose spectrum is the zeros" programme for Dedekind zeta functions. Checked by us (af2a18f6, given
   MT-M18/M19 and HKMS). Where: GRH_NIGHT.tex l.18843, l.19513.

9. **An explicit integral Weil cycle on a fourfold Jacobian (THETA3 C32).** For H: y² = z∏_{j=1}^4(z²−a_j²) with
   ρ(z,y) = (−z,iy), the Jacobian A carries an integral C_A ∈ CH²(A) with 0 ≠ cl(C_A) ∈ W_{Q(i)}(A) and
   ∫cl(C_A)² = 73728, built from a plane in Sym⁴P¹ through three blowups (Schoen 1988, Th. 2.0 and Cor. 3.1, in a
   ramified case). The family contains C25's simple Q(i)-Weil fourfold. Why: an explicit test object with a computed
   self-intersection, usable for quantitative bounded-division constants. **Checked by this intake** (cohomological and
   numerical steps; the blowup inertia argument read). Algebraicity itself is Schoen's (and Markman's for C25). Where:
   `THETA3_checkpoint_07_20261121T0604Z_unzipped/THETA3.tex` l.14285–14807.

10. **An all-window lower rate for the Weil form (ZETA_HEAT thm:cosine-lower-rate).** a₁(L), b_L, a₂(L) ≥
    exp{−C μ^{1/d_MT} log μ (1 + log log μ)}, μ = e^{2L}, d_MT = 5/4 − cot(1/√2)/(2√2) = 0.836250…. **Checked by this
    intake** (given Mori's Lemmas 3.3–3.5 and Voss's Theorem 2). It improves Mori's exponent 6/5 = 1.2 to 1/d_MT =
    1.19581…: a marginal improvement, far from the needed e^{−4πμ} scale. Where:
    `.../sections/uniform_cosine_sampling_lower.tex`.

11. **Grothendieck's cote 1 corrected (TRACE_DET ARC-01–ARC-04) and the cote 1 positive forms of RH (DET-16, DET-18).**
    The genus-zero lemma of scans 111–112 needs three corrections; the product ∏(1 − z/n^α) has order 1/α (scan 110); 1/ρ
    is a liminf (scan 113). DET-16: RH ⟺ the explicit-formula kernel k is bounded ⟺ k is of positive type, now
    unconditional by A. DET-18 (checked in full by this intake): an ordinary Fredholm determinant det(I − s(1−s)C) for the
    weighted character family of Alpöge's Lean, with 0 ≤ C ≤ 4I ⟺ GRH for that family. Classical in substance; useful for
    the archive. Where: `TRACE_DET_final_20261121T0218Z_unzipped/TRACE_DET.tex`.

12. **The core-index obstruction to transporting Weil witnesses (DEG_L B19–B21).** For a fixed simple CM source and a
    target with core index J = [Λ:Λ⁻], every reduced image of a source witness of degree ≤ D₀ under an E-linear
    homomorphism has degree ≥ c√J, and some has degree ≤ C√J. So no fixed-source transport gives uniform bounded division
    along CM sequences with J → ∞. Checked by us (B19, ad855737; **B20–B21 by this intake**). Where:
    `DEG_L_checkpoint_06_20261121T0517Z_unzipped/DEG_L/DEG_L.tex` l.3135–3335.

---

## 1. GRH_ALGORITHMS (prompt 67), checkpoint 08 (23 Nov 02:24 UTC)

Return: `GRH_ALGORITHMS_checkpoint_08_20261123T0224Z_unzipped/`. Prompt: `TO_SEND/PRO/1_Archive_research_by_topic/SENT/67_GRH_ALGORITHMS`.
Intakes: cp04, cp05, cp08 and the primer (a25c2acb). The thread is beyond reach; its mathematics continues in 67c (§2) and
is printed in the posted paper.

**1. Useful or not.** Useful. It classified what A makes unconditional among eighteen classical GRH-dependent algorithmic
statements, and proved the first A-only and unconditional constructions that 67c finished.

**2. What it proved** (ids GRH-Pnnn; the posted paper's labels in brackets).
- **P001** [thm:kummer], under A: RH(ζ_{Q(p^{1/r})}) ⟺ RH(ζ_{Q(ζ_r, p^{1/r})}); either gives an auxiliary prime
  ℓ ≪ r² log²(rp), ℓ ≡ 1 mod r, p^{(ℓ−1)/r} ≢ 1 mod ℓ, hence Adleman–Lenstra. Mechanism: on AGL₁(F_r) the regular
  representation is abelian characters plus copies of one induced order-r Hecke character, ζ_E = ζ_K(ζ_F/ζ)^{r−1}. Run
  only here; the same statement is GRH_NIGHT CX-ALG-024, checked by us (af2a18f6).
- **P004** [thm:teich], unconditional: F_{p^r} and an equivariant r-primary unit η ∈ F_p[Z]/Φ_r(Z) of order r^a with
  σ_c(η) = η^{ω_a(c)} are interconvertible in deterministic polynomial time (Lenstra 1991, Thms 3.1, 5.1, 5.2,
  reformulated). Checked by us via GRH_NIGHT CX-ALG-023.
- **Classical table** (Q03), under A: Miller's test below 2 log² n; r-th nonresidues for r | p−1; primitive roots given
  p−1 factored (Shoup g(p) ≪ log⁶ p); least prime in a progression ≤ (φ(q) log q)² (LLS Cor. 1.2); Rubinstein–Sarnak's
  limiting distribution. Still beyond A: strict race densities, Hooley's Artin density, Bach's class-group bound,
  isogeny expanders, CM split-prime selection. Run only (the run's independent reconstruction).
- **P006** [thm:nonresidue], under A: nonresidues in a presented extension. Run only.
- **P058, P074** [thm:fixed-r-almost-all-auxiliary], under A: for C_r > (r−1)/(2 log r), all but O(√P log log P) primes p
  in (P/2, P] have an auxiliary ℓ ≤ C_r log P log log P. Checked by us (a25c2acb, TPC).
- **P092–P095** [thm:almost-all-small-tate], under A: for C > 1/log 3, Y³ − (k+3)Y² + kY + 1 is irreducible mod p for
  some k ≤ C log P, for all but O(√P log log P) primes. Mechanism: private prime divisors of k² + 3k + 9 (after
  Cilleruelo). Checked by us (a25c2acb, TPC).
- **P125/P126** [thm:fixed-wild-cm, cor:fixed-wild-prime-degree-field], under A: for fixed odd r and b ≥ 2, if
  v_r(p^d − 1) ≥ b, an equivariant U of order r^b is computed in time C_{r,b}(log p)^{c_{r,b}}; at valuation exactly b,
  F_{p^r} is constructed. Mechanism: imaginary quadratic E = Q(√−q) with q ≪ log² p in which p splits; the compositum with
  the degree-r^{b−1} real subfield R_b of Q(ζ_{r^b}) carries a primitive CM type; theta constants, Pila's point counting,
  Frobenius supports. Run (adversarial audit and statement-only reconstruction). **This intake checked the auxiliary-field
  step** (posted TeX l.3245–3290): the indicator ¼(1 − χ₋₄)(1 + χ_{D_p}) with D_p ∈ {p, 4p} fundamental, four characters mod
  4p, one principal; q ≪ log² p; (−q/p) = (p/q) = 1; p splits completely in R_b because p^d ≡ 1 mod r^b and d | r−1.
- **P119**, under A: cubic fields when v₃(p+1) = 2. Run only.
- **P128/P131** [thm:small-cyclotomic-cofactor, cor:two-primary-cyclotomic-cofactor], unconditional: cost
  poly(r, log p, M₂), M₂ = Φ_d(p)/(2^{v₂} r^a) (after Bach–von zur Gathen–Lenstra). Root-extraction lemma checked by us
  (a25c2acb, cp08).

**3. New since the last intake.** Nothing in the run. Its results are now public in hexagon:2611.00987v1.

**4. Open.** Q02 (classical auxiliary prime ≪ poly(r, log p) from A alone): gate = the one-sided window inequality for the
induced order-r Hecke function (prop:window, P017), or pure-field RH. Q07 (density route), Q08 (elliptic trace with
discriminant valuation exactly 1), Q09 (CM discriminant with prime class outside r·Cl): open. Q01 continued in 67c.

**5. Relations.** GRH_NIGHT CX-ALG-016–028 (its seed); 67c (its finish); SEED_MAS_ARTIN Paper 2; P vs NP fleet ANT-07.
Literature: Lenstra 1991 (Invent. Math. 104); Adleman–Lenstra 1986; Bach–von zur Gathen–Lenstra 2001; Pila 1990; Shoup
1990; LLS 2015 (corrected arXiv 1309.3595v3). Grothendieck: a residue map O_K → F_p is an F_p-point of Spec O_K, and the
constructions read Frobenius off CM motives (theta-marked CM abelian varieties); P004 is Galois descent along
Gal(Q(ζ_r)/Q).

**6. Candidates.** None separate from 67c (posted).

**7. Problems.** None found in what was read.

## 2. GRH_ALGORITHMS_FINISH (prompt 67c), checkpoint 07 (23 Nov 20:59 UTC), and Codex's edition

Return: `GRH_ALGORITHMS_FINISH_checkpoint_07_20261123T2059Z_unzipped/` (paper
`workbench/work/unfiled/v1/papers/grh_algorithms.tex`, 190 pp., 164 statements, 575 check events). Codex's edition (second
witness, 191 pp.): `Codex/2026-11-22/the-two-tracks-share-no-sound/outputs/67c_PUBLICATION_DRAFT/checkpoint-07/`. Posted
text: `reports_20261124/grh_algorithms_67c/source_v1/grh_algorithms.tex` = Codex's edition with three effort-naming edits.
Prompt: `SENT/67c_GRH_ALGORITHMS_FINISH`. Intakes: cp04, cp07, primer, Codex literature and handoff notes (a25c2acb).

**1. Useful or not.** Useful: posted as hexagon:2611.00987v1, "Constructing finite fields of prime degree from small
cyclotomic cofactors and at fixed valuation, after Bach, von zur Gathen, Lenstra, and Pila".

**2. What it proved.**
- **P144** [thm:threshold-cyclotomic-cofactor = Thm 1.1], unconditional: F_{p^r} in time (r + L + C_L + log p)^c, C_L the
  cofactor of N = Φ_d(p) after removing 2, r^a and every ℓ^k ∥ N with ℓ ≤ L, r ∤ ℓ−1. TPC by us (a25c2acb, 23 Nov).
- **P145** [thm:selected-cyclotomic-cofactor = Thm 5.1], unconditional: for disjoint sets S (order-ℓ roots supplied) and
  T (r ∤ ℓ−1), cost (r + C + Σℓ + log p)^c. Mechanism: projected primary root extraction, shift search with the rational
  function H, odd-prime commutator, and for ℓ ∈ T adjoin A₀[Y]/Φ_ℓ(Y), take the norm and use Bézout with r ∤ ℓ−1. TPC by
  us (a25c2acb).
- **P147** [prop:quantitative-real-residue = Prop. 16.1], under A: for fixed m ≥ 3 and a totally real Galois K of degree m
  given by an integral basis with table height H, a ring map O_K → F_p is constructed for every p split completely in K,
  in time c_m(H + D_K + 1 + log p)^{C_m}. Run (author checks and statement-only reconstruction); Codex targeted reading.
  **Read in part by this intake**: the sole conditional step (a prime q ≡ 3 mod 4 with (p/q) = 1 in an index-4 coset of
  (Z/QZ)^×, Q = 4pD_K·P₀ with P₀ the product of the primes ≤ Q₀, so that q > Q₀ automatically; LLS Thm 1.4 bounds q by
  (H + D_K + log p)^{O_m(1)}); the CM type Φ = {(g,1): g ≠ 1} ∪ {(1,c)} has trivial left and right stabilizers for m ≥ 3;
  the Frobenius masks e_τ = (τπ)^{p−1} separate the primes above p through the trivial right stabilizer of Φ⁻¹. Not
  re-derived: the theta atlas, the height chain (von Känel–Kret (7.7), Pazuki Cor. 1.3), extension of the marking,
  Pila's algorithm.
- **P148** [lem:cyclotomic-primary-quotient = Lemma 16.3], under A: for fixed r and b ≥ 1, primes p, ℓ ≠ r with ℓ | Φ_d(p)
  and v_r(ℓ−1) = b, a monic G_ℓ | Φ_ℓ over F_p of degree h_ℓ = (ℓ−1)/r^b (prime to r) is constructed in time
  poly(ℓ + log p); B_ℓ = A[T]/G_ℓ is finite étale of rank h_ℓ with components F_{p^d}. **TPC by this intake, confirmed:**
  K_ℓ = Q(ζ_ℓ)^{H_ℓ} has degree r^b and is real (h_ℓ is even, so −1 ∈ H_ℓ); the Gaussian periods are an integral basis
  (orbit sums of the permutation basis ζ^a, 1 ≤ a ≤ ℓ−1); ord_ℓ p | d | r−1, so Frobenius is trivial in the r-group and p
  splits completely; gcd(Φ_ℓ, η_j(T) − t_j) selects exactly the h_ℓ roots restricting to the chosen residue map.
- **P149** [thm:bounded-congruence-cofactor = Thm 1.2], under A for fixed (r, t), unconditional for t = 0 (= P144):
  F_{p^r} in bit time c_{r,t}(L + C_{r,t,L}(p) + 1 + log p)^{C_{r,t}}, where C_{r,t,L} removes from N = Φ_d(p) the
  factors 2^s, r^a and ℓ^{v_ℓ(N)} for every odd ℓ ≤ L, ℓ ≠ r, ℓ | N, v_r(ℓ−1) ≤ t; the r-primary unit U and the
  simultaneous root interface come with it. **TPC by this intake given P147, confirmed:** the order-ℓ element ε is
  nonconstant on each rank-r component and lies in ⟨θ⟩ there, so some comparison with θ^j gives a proper factor of
  X^r − z of degree j ∈ (0, r); b = (−1)^j f(0), b^r = z^j and Bézout give the root in B; the norm n = N_{B/A}(y) has
  n^r = z^{h_ℓ} and gcd(h_ℓ, r) = 1. The closing limitation (a partial subfield of degree r^j, j < b, leaves rank divisible
  by r, so Bézout cannot reach exponent one) is also right. Example: p = 251, r = 3, L = 7, p + 1 = 2²·3²·7.
- **P150, P161** (genus-two Frobenius collisions): point counts recomputed by us (a25c2acb, 24 Nov).
- **P151–P155** (cyclic descent interface and its limits), **P157–P159** (trace-one local units, ideal profiles, fixed
  rational shift menus fail at positive density), **P162** (restricted CM reflex obstructions): run plus Codex.
- **P160, P163, P164, P156** (as corrected by Codex): checked by us (a25c2acb, 24 Nov): the third quotient v² = u³ + 1
  (j = 0 against 54000); Guo's literal loop fails on F₁₉ (x = 4, y = 9 = x⁴) and on F_{109³}; P164 "detects residue degree
  one"; P156 wording.
- **P143** (any k = ⌈log P/(2 log r)⌉ menu primes), **P146** (fixed-set cubic cofactor): run only.

**Second witness.** Over Lemma 16.3 and the proof of Theorem 1.2 the run's cp07 text and Codex's edition differ only in
Codex's two edits: the explicit b = (−1)^j f(0) with Bézout (the run wrote "the constant term ... and a Bezout identity");
and "each base branch has at most one prime-order auxiliary algebra open at a time" during each simultaneous-root call,
where the run wrote "at most one prime-order auxiliary adjunction on any base branch", which is too strong as worded.

**3. New since the last intake.** Posted on Hexagon (24 Nov 11:25 UTC, commit receipt 2611.00987v1). The cp07 intake had
not read P147–P149; this intake read P148 and P149 in full and P147 in part (above).

**4. Open** (QUESTIONS.tsv at cp07).
- Q01, uniform construction from A alone: gate = the residual cofactor C_{r,t,L} when the valuation, t or r grows (the CM
  exponent grows with r^b). Proved: fixed (r, b) and fixed (r, t) strata under A; C_L polynomial unconditionally.
- Q02: the one-sided window inequality (prop:window, P017) for the induced order-r Hecke function; pure-field RH suffices.
- Q07, Q08, Q09: as in §1. Q06 (paper): done by the posting.
- The run's CONTINUATION.md (19:58 UTC) records review 03 without movement and a research stop due if review 04
  (20:44 UTC) also found none; cp07 (20:59 UTC) is the last return we hold.

**5. Relations.** GRH_NIGHT CX-ALG-023/024 (the Teichmüller and pure-field equivalences); NIGHT_AFTER_ALPOGE (A-only
inputs). Literature: Lenstra 1991; BGL 2001 (Theorems 1–3, §5); Pila 1990, Section 3; Mumford 1967, Section 6; Milne
1999, Prop. 2.1; von Känel–Kret 2023, (7.7), Lemma 7.10; Pazuki 2012, Cor. 1.3; Buchmann–Lenstra 1994, Alg. 6.1; IKRS 2012,
Thm 1.5; Rónyai 1992 (GRH factoring via splitting fields; the paper says it makes "rational Dirichlet GRH suffices"
explicit in fixed degree); Guo 2017 thesis. Grothendieck: schemes over Z (completely split primes, Spec O_K(F_p)),
CM motives and their Frobenius (Shimura–Taniyama), finite étale algebras and Galois descent throughout.

**6. Candidates.**
- Posted (H29). A later version could name our checks of P144/P145, P148/P149 and the recomputations (the method note
  omits them; an understatement, not an error).
- Correction to report: Guo, thesis arXiv:1706.10028v2, Lemma B.1 (literal loop) and Hypothesis (*) quantifier (P163).
- Next prompt: Q02's one-sided window inequality, or Q01 with growing t, only if the user wants the line continued.
- Codex's nine reviews and its post-freeze COFACTOR_LAYERS result are taken in separately: `ZETA_GRH_67C_CODEX.md`. Their
  corrections are all in the posted text. COFACTOR_LAYERS holds; it is a v2 remark, not a note.

**7. Problems.** None in the corrected text as far as read. Gate left for full certainty on Theorem 1.2: an independent
check of P147's quantitative CM chain (theta recognition, height bounds, good reduction of the marked object).

## 3. GRH_NIGHT (prompt 42), checkpoint 07 (21 Nov 06:17 UTC)

Return: `GRH_NIGHT_checkpoint_07_20261121T0617Z_unzipped/GRH_NIGHT.tex`. Prompt: `SENT/42_GRH_NIGHT_...`. Intakes: three
(cp02, cp04, cp07) and the primer (af2a18f6).

**1. Useful or not.** Useful in parts: the finite-field rows seeded 67/67c; MT-M23 and MT-S506 are clean statements; the
Masullo defect table and the cote 34 repair are concrete.

**2. What it proved.**
- **CX-ALG-016** (l.13989), refutation of a literal formula: BIMS 2017 Thm 3.1 resolvent can vanish (example in §0
  item 6). Checked by us (arithmetic, af2a18f6; recomputed here: α⁷ = 4α, α⁴⁹ = 2α, 1 + 16 + 4 = 21 ≡ 0).
- **CX-ALG-017** (l.14011), unconditional repair: some basis power α^j gives β = Σζ^i(α^j)^{Q^i} ≠ 0, since the linear
  map has degree Q^{r−1} < |E|; then β is an r-th nonresidue. Checked by us.
- **CX-ALG-018** (l.14067), unconditional: the even-degree quadratic case without GRH. Checked by us.
- **CX-ALG-023** (l.14621), unconditional: supplied F_{p^r} ⟺ maximal coefficient Teichmüller unit (after Lenstra 1991,
  Thms 5.1–5.2). Checked by us.
- **CX-ALG-024** (l.14723), under A: the pure-field equivalence (= 67's P001), with q ≤ O(r⁴ log²(rp)) via Bach–Sorenson.
  Checked by us.
- **CX-ALG-027** (l.15371), under PF26 + M: factoring of degree d over F_{p^m} in poly(d, m log p). Conditional on M.
- **MT-M20** (l.18843), **MT-M23** (l.19513): §0 item 8. Checked by us given MT-M18/M19 and HKMS Thm 1.1.
- **MT-S506** (l.25778), under A: §0 item 7. Checked by us given the table; **table computed by this intake.**
- **MT-A01** (l.15734): A gives GRH for every unitary Hecke character of Q (finite image on Ẑ^× times |·|^{it}). Checked.
- **MT-ART01**, under M + Khare–Wintenberger: odd irreducible 2-dimensional Artin L-functions over Q are entire and satisfy
  GRH. Conditional on M.
- **Masullo defects** (statements about the draft): MT-M01 (p. 425, Lemma 9.3.2.4: the O(log T) zero count fails,
  Mφ(s) = e^{s²} sin(s²)); MT-M02 (p. 426: the intersections W_{≤T} decrease); MT-M05 (pp. 425–426: needs closure of the
  ideal); MT-M36 (p. 495: the section average is identically zero, Haar measure on I_F¹ being atomless; found
  independently by ALPOGE_BRIDGES F-SM-19); MT-M34 (p. 480: in the Q trivial sector the two closures coincide). Checked
  by us (core lemmas).
- **AG-C34-REPAIR, -INDEX, -SECTION** (Grothendieck cote 34, Remark 1.17): K = closure of ⟨[p,h]⟩ is open in H with
  H/K ≅ (H^{ab})_{π₀}; |coker(F−1 | M)| = |T^F|·ℓ^{v_ℓ det(1−F)}; with a section and H solvable the action commutators are
  open. Checked by us. AG-C34-TYPE: the literal remark fails for infinite π₀.

**3. New since the last intake.** Nothing in the run. This intake computed the S₅ induction table (check events).

**4. Open.** Q-MAS-GEOMETRIC-NARROW (the geometric trace equality on narrow strips; MAS_ARTIN MA-HM-003 showed it equivalent
to RH in the corrected model); GL₂ GRH in weight ≥ 2 (NT-Z07); general Artin holomorphy (MT-ART02, the Heilbronn matrix
gate) and the S₅ central gate β − b − n ≥ 1 (continued in MAS_ARTIN); full GUE statistics; general derandomization.

**5. Relations.** 67/67c (CX-ALG rows); MAS_ARTIN (MT-M18–M26, MT-S506/S508); ALPOGE_BRIDGES (F-SM-19); ZETA_TWO ZT02.
Literature: BIMS ISSAC 2017; Lenstra 1991; Bach–Sorenson; Khare–Wintenberger (Cor. 10.2); Hu–Kaneko–Martin–Schildkraut
Thm 1.1; Prasad–Yogananda (Artin holomorphy report, §2.1). Grothendieck: Artin motives and their L-functions (MT-S506 is
an identity in the representation ring of S₅, i.e. among Artin motives); cote 34 (local π₁, inertia, Frobenius on Tate
modules).

**6. Candidates.**
- Correction to report: BIMS 2017 Thm 3.1 (CX-ALG-016, with the CX-ALG-017 repair).
- Masullo defect table: `TO_SEND/PRO/_staging_20261121/cores/MASULLO_DEFECTS_20261121.md` (staged, not sent).
- Hexagon: MT-M23 as a short note only after a literature search (the HKMS input does most of the work).

**7. Problems.** The run's MT-S506 remark "a new reduction using classical character theory" (l.26221) is a novelty claim
with no search behind it. Our own earlier intake phrases "every literal defect has a repair" and "the trace identity over
Q is known to hold" were corrected in the primer (§4).

## 4. ZETA_HEAT (prompt 62), final (23 Nov 22:19 UTC)

Return: `ZETA_HEAT_final_20261123T2219Z_unzipped/` (paper `workbench/paper/`, 169 pp.). Prompt: `SENT/62_ZETA_HEAT`.
Intakes: cp01, cp03, final, primer (afa2696b). Paper: "The simplicity question for the Riemann zeros after Alpöge's
theorem". Status: 9 rows proved, 2 refuted, 9 INCOMPLETE under the two-review rule; main question open.

**1. Useful or not.** Useful as a criterion paper (an exact, prime-side, finite test of simplicity, and an integer form of
it); marginal in its certified height (97.632) and in its window lower rate (exponent 1.1958 against Mori's 1.2).

**2. What it proved** (labels in `sections/`).
- **thm:fd-limits** (finite_detection.tex): √a·m_*(−a) → min x𝔯_{m_x}/(2√2) and a·j_*(−a) → x_*²/8 along the backward heat
  flow; simplicity ⟺ L_T = ∞ ⟺ L_J = ∞. Analytic part checked by us (afa2696b); 𝔯₂ = π, 𝔯₃ = 2π/√3 checked.
- **thm:fd-arithmetic-complete**: §0 item 3; proof checked by us (Suzuki's HS convergence carried); the six certificate
  rows replayed non-rigorously by us to 10 digits; the run's Arb enclosure is the certificate: every zero with
  0 < Im ρ ≤ 97.632 is simple.
- **prop:fd-inertia-complete**: simplicity of the packet through T ⟺ ind₊(TH_N − G_N) ≥ n(T) for some N; Schur form
  ind₊(T²KᵀG₊⁻¹K − G₋). TPC and computation (ι = 6, 14, 28 at T = 39.913, 62.413, 97.632) by us.
- **prop:fd-even-operator** (‖C − C_N‖ ≤ (2/√3)D_{N,k}^{1/(2k)}), **prop:fd-certificate-size** (dimension ≥ 2n(T)),
  **prop:finite-simple-deflation**, **prop:fd-arithmetic-precision** (perturbation step), **lem:fd-multiplicity-log**
  (m_γ < ¾ log γ for γ ≥ 10), **prop:orbital-unimodal-bound** (𝔯_m² ≥ 4π²(m+1)/(3m²)), **cor:fd-global-growth-numeric**
  (L_T > 216.88, L_J > 4766.003712): checked by us (afa2696b), the last except the cited 𝔯_m ≤ π√(m−1).
- **thm:strong-inertia-density, thm:fd-inertia-density**: ind₊(TH_N − G_N) ≥ (d_MT − η)n(T) with N = ⌈A_η log T⌉. Run only.
- **thm:cosine-lower-rate**: §0 item 10. **TPC by this intake** (below).
- **thm:isolated-pair** (κ = 0 term checked by us), **thm:positive-directions**, survival below 0.67250… for
  −c/(log T)² ≤ t ≤ 0, **thm:nonreal-height**, CUE laws (Weibull-3/2 first collision, label agreement 0.666546601837…):
  run only except as marked. Refuted: PAIR-Q2 (periodic triple cluster, κ ≥ 4/9), PAIR-Q3 (Lagarias–Rodgers Thm 3.1); the
  δ-free motion rule fails at zero 1169. Character-limit obstruction (real case checked by us).

**3. New since the last intake.** Nothing in the run. This intake checked thm:cosine-lower-rate: the weighted-norm
algebra ((2/κ)∫₀^κ u w(u/κ)du = κB; the archimedean term ≤ Aℓ⁺(L⁺+C)²/κ); the positive pair average (each ordered pair at
distance < h, the diagonal included, contributes ≥ 2π(1 − C/κ)); the packing (an h-separated set of size
≥ max{N_J − P_h, N_J²/(N_J + 2P_h)}); the exact scalar comparison max{3/2 − ρ/2, 1/ρ} ≥ dβ (difference
(1−β)((3−A)β − A)/(2β) for β ≥ 3/5, and 50/57 > 7/8 below); the rescaling with ε = 1/s and D = O(sμ^{1/d}); the Weil
normalization F(x) = f̂(πx/L) ∈ PW_π with ‖F‖² = 2L‖f‖². Numerically d = 0.8362504, 1/d = 1.1958141, A = 1.00613,
B = 0.32137, A + B = 1.32750 = ½ + c cot c. Carried: Mori's Lemmas 3.3–3.5 and Lemma 2.2, Voss 1999 Thm 2.

**4. Open** (all INCOMPLETE): MAIN-SIMPLE (sup H_{N,k} = ∞, equivalently ind₊ = n(T) for finite N at unbounded zero-free
T; N = O(log T) reaches the fraction d_MT − η); MAIN-MOMENTS; MAIN-CONTOURS; MAIN-TRACE; MAIN-RATIO (needs
a₂ ≳ λ^{9+α}e^{−4πλ²}, 0 < α ≤ 4; proved only the cosine rate); THETA-LOWER; MOTION-Q3; PAIR-Q2 (exterior control);
PAIR-Q4.

**5. Relations.** ALP_CONNES S47–S52 and cp44 (RZ.5) (the window side); prompt 68 item 5; SEED_ALP_CONNES. Literature:
Suzuki arXiv:2610.32704 (compressions; not opened by us); Montgomery–Taylor (d_MT, 0.6725); Mori 2026 (6/5 rate);
Alpöge–Furman, Lamzouri, Knausgård (the same density proportions; credit split unmade); Voss 1999; Olshanski; Weil's
explicit formula. Grothendieck: the Weil positivity here is the arithmetic analogue of the Hodge standard conjecture
(positivity of the intersection form on primitive classes), the analogy behind cote 16's Hodge-index route.

**6. Candidates.** Hexagon paper: gates as in the final intake (title per theorem or a split; credit split against
Alpöge–Furman/Lamzouri/Knausgård; open Suzuki at its locator; our checks in the method note; the workbench URL live; the
PDF check). This intake removes one gate: thm:cosine-lower-rate is now checked by us (given Mori and Voss). Next prompt:
only for MAIN-SIMPLE's integer deficit, if the user wants the line continued.

**7. Problems.** Our final intake and the primer call thm:cosine-lower-rate "the first lower bound on the window side"
(`INTAKE_ZETA_HEAT_20261124_final.md` §2 item 3: "Usefulness: the first lower bound on the window side"). That is wrong:
the run's own text (uniform_cosine_sampling_lower.tex l.10–12) says Mori proved the lower rate with exponent 6/5; the run
improves the power to 1.1958. No error found in the run's text.

## 5. ZETA_NEXT (prompt 43), final (21 Nov 03:40 UTC)

Return: `ZETA_NEXT_final_20261121T0340Z_unzipped/` (normal/, cm/, lambda/, noncm/findings.tex). Prompt:
`SENT/43_ZETA_NEXT_...`. Intake: final, primer (ad855737); KTOWER cp11 rows.

**1. Useful or not.** Useful: effective constants from A in the class-number and CM-orbit chain (H15), and a decisive
answer on Λ-schemes.

**2. What it proved.**
- **NX01, NX02**: §0 item 2. Checked step by step by us (ad855737); constant agrees with Garcia–Lee's extraction.
- **NX03** (effective Brauer–Siegel for normal fields, with Louboutin 2001 Thm 1(1)), **NX04** (h_K ≤ √D_K(1 + ½ log D_K)^{n−1},
  classical in form): checked.
- **NC01–NC04**: §0 item 2; NC01 constant chain, NC02 proof (averaged Colmez and Wei's 75/2 carried), NC03/NC04 step by
  step: checked by us (ad855737). NC04: |Gal·x| ≥ s_g⁻¹T_g^{−1/P_g}|disc R_x|^{1/P_g}, P_g = 28672g⁴ (exponent superseded
  by A.ORBIT's 1/(4g)).
- **NX-L01**: gluing two copies of A^d_Z along A^d − |Z| gives a flat nonseparated Λ-scheme with ζ_X = ζ(s−d)Z(Z, p^{−s});
  for Z: y² = x³ − x over F₅ the bad factor (1 + 2t + 5t²)/(1 − 5t) has inverse roots of modulus √5. Refutes ZETA_TWO's
  conjecture as worded. Checked by us (and recomputed here: #E(F₅) = 8, a₅ = −2).
- **NX-L02, NX-L03** (statement level): proper flat X/Z_p with a Frobenius lift has bad fibres that are integral
  Artin–Tate (perfectoid tilting; Borger Cor. 6.2). **NX-L06** (checked given L03): every non-real divisor of ζ_X of a
  proper flat Λ-scheme has Re s ∈ ½Z. **NX-L07**: Z[ζ₅] has no Frobenius lift at 5.
- **NG01**: a pure motive M of abelian type over Q (absolute Hodge cycles) splits canonically over Q as
  M = C(M) ⊕ N(M), H_B(C(M)) = H_B(M)^{D_M}, D_M = (G_M°)^{der}; C(M) is the maximal potentially-CM subobject.
  **TPC by this intake, confirmed** given Deligne–Milne Prop. 6.5, 6.23, Thm 6.25 and Commelin §4.13–4.16: D_M is
  characteristic in G_M° hence normal in G_M, so the isotypic split is G_M-equivariant and descends by Tannaka duality;
  the identity component on the invariants is a quotient of the torus G_M°/D_M; a connected semisimple group maps
  trivially to a torus, giving maximality. The run correctly refuses to identify the ℓ-adic (G_ℓ°)^{der}-invariants with
  C(M)_ℓ without Mumford–Tate.
- **NG02–NG06** (statement level): exact residual lists for curves, abelian varieties, the full Sp_{2g} case, E^m.
  **NG07** (statement level): Jac(y³ = x⁵ − x − 1) is absolutely simple non-CM, yet its primitive h⁴ has a CM summand of
  types (3,1),(1,3).

**3. New since the last intake.** Nothing in the run. NG01 checked by this intake (it was statement level).

**4. Open.** Effective André–Oort for A_g (now cited from Jaswal, Hexagon 2611.00339, with Cureton–Thorner, Hexagon
2610.00200; our questions are the exponent and an unconditional orbit bound); separated nonproper Λ-schemes; NG07's Hecke
character (an infinite-order character over Q(ζ₃), so M).

**5. Relations.** ZETA_TWO (ZT06 gap closed by NG01; IA05 seed); NIGHT_AFTER_ALPOGE A.ORBIT (H15); KTOWER (SEED_KTOWER
Paper 2); DP_MULT DP11. Literature: Stark 1974 (Lemmas 3–4, 7–9); Louboutin 2001; Garcia–Lee; Gaudron–Rémond
(*Polarisations et isogénies*, Thm 1.4; 2023); Tsimerman 2018; Borger (Λ-rings); Scholze (perfectoid). Grothendieck: zeta
functions of schemes over Z and their weights; λ-rings (Borger's Λ-schemes, the Adams operations as Frobenius lifts);
motives of abelian type and the Tannakian group (NG01 is a Tannakian splitting).

**6. Candidates.** H15 via A.ORBIT (one gate: the literature comparison with Jaswal and Gaudron–Rémond 2023). The NX-L01
example is a short note candidate only as part of a Λ-scheme write-up.

**7. Problems.** None new. NX-L02 rests on a statement-level perfectoid comparison; NX-L06 is checked only given it.

## 6. ZETA_TWO (prompt 35), final (21 Nov 00:32 UTC)

Return: `ZETA_TWO_final_20261121T0032Z_unzipped/ZETA_TWO.tex`. Prompt: `SENT/35_ZETA_TWO_...`. Intake: final, primer
(ad855737): 21 findings checked step by step, none refuted.

**1. Useful or not.** Marginal on its own (a careful organization of what A and M give for ζ_X); useful as the seed of
ZETA_NEXT and of H15 (IA05).

**2. What it proved.**
- **ZT01** (l.255): exact Artin–Tate counts at every p give ζ_X = ∏L(V_i, s − i); in the abelian case A puts every
  non-integer divisor on Re s = i + ½. **ZT03** (l.365): RH for ζ_K, by A for abelian K, by M in general. **ZT04/ZT05**:
  identities off a finite set; Spec Z[1/p] has zeros 2πik/log p on Re s = 0 (refutes "RH for every Λ-scheme" as glossed).
  **ZT06** (l.491): every scheme of finite type reduces to bad fibres and L^S(H^j(Y_a), s)^{±n_a} (Bittner Thm 3.1; EGA IV₃
  8.8.2). **ZT07** (l.575): ζ_E = ζ^S(s)ζ^S(s−1)/L^S(E, s); under A, in ½ < Re s < 3/2 off Re s = 1 the order of ζ_E is
  minus that of L(E, s). **ZT08**: the Euler factor is a λ-ring invariant (SGA 6 V §2). All checked by us.
- **CM01**, under M: RH for CM motives via Anderson 1986 Cor. 5.7.2. Conditional.
- **IA02, IA03, IA05**: A-effective arithmetic (LLS v3 Thm 1.5; supersingular count c_p h(−D_p); no Siegel zero for CM
  Faltings heights by Stark's descent). **IA06–IA09** recomputed by us. **IA09** (l.1233): for every odd prime p some
  odd χ mod p has |L(1,χ)| ≤ π/√6, since the mean of |L(1,χ)|² over odd χ is π²(p−1)(p−2)/(6p²). **Re-proved and
  computed by this intake** (p = 3 to 997; e.g. p = 997: minimum 0.338).
- SV01/02, ML01/02, ALP01/02: small rows, checked.

**3. New since the last intake.** Nothing in the run. IA09 rechecked here.

**4. Open.** Q01/Q02, RH for ζ_X in general: gate = RH for the non-CM summands N(M) (ZETA_NEXT NG01/NG07), first case h¹(E)
for E non-CM. Bad fibres of Λ-schemes: decided by ZETA_NEXT (refuted for nonseparated, proved for proper).

**5. Relations.** ZETA_NEXT; ALPOGE_BRIDGES F1 and BR-AT-01 (= ZT01); DP_MULT DP11; H05 (CM01, held as conditional).
Grothendieck: Hasse–Weil zeta of schemes over Z, weights (lines Re s = i + ½), λ-ring structure of the Euler factor
(SGA 6 V), motives (Brauer induction among Artin motives).

**6. Candidates.** None beyond H15 (via ZETA_NEXT). H05 stays on hold (conditional on M).

**7. Problems.** None found in what was read.

## 7. THETA3 (prompt 37, HODGE_THETA), checkpoint 07 (21 Nov 06:04 UTC; final by the three-hour rule)

Return: `THETA3_checkpoint_07_20261121T0604Z_unzipped/THETA3.tex`. Prompt: `SENT/37_HODGE_THETA_three_signatures`.
Intakes: four parts and the primer (aaf69461). Folio numbering: "cote 16 scans 43–46" is our 044–047.

**1. Useful or not.** Marginal to useful: explicit constants for 032's non-vanishing step (Q1–Q9), the projector later
used by the division attack (C13), and an explicit Weil cycle (C32). The main question (1.7, one seesaw linking 032's
signature-(2,1) theta machine to Alpöge's definite groups) is open.

**2. What it proved.**
- **Q1–Q9**: 032's non-vanishing is Gaussian concentration plus continuity (no Rallis or Bessel identity), with explicit
  constants (c = 2πe^{−2π} ≈ 0.011733, c² > 1.37·10⁻⁴). TPC by us (aaf69461).
- **C13**: explicit algebraic projector onto the Weil plane (a resultant projector, a^{2n} ∉ Q, one nonzero period
  suffices). TPC by us. C12 (Schoen's surface, period 500): TPC by us.
- **C32**: §0 item 9. **TPC by this intake** of the cohomological and numerical steps: weights (1,3,2,2,2,2) of
  y⁴ = t∏(t − b_j)² (degree 9 gives weight 3 at ∞); genus 4; ρ has eigenvalues ±i with multiplicity four and
  z^j dz/y has eigenvalue i for j even, −i for j odd, so the determinant lines are of type (2,2); N-invariance forces the
  four characters to agree, so the primitive part of H⁴(W₀) is ∧⁴H¹_i ⊕ ∧⁴H¹_{−i}; |G| = 4³·4! = 1536; on the plane P₀
  the norm ℓ₀ℓ_∞³∏ℓ_{b_j}² is a scalar times (u₁u₂u₃)⁴, so the cover splits into four planes; c(Ω¹_{P²}(1)) = 1 − H + H²,
  so (Q₀ − Q₂)² = 2; ∫_{H⁴}cl(C_H)² = 1536·2 = 3072; a: H⁴ → A has generic degree 24 and a* identifies W_{Q(i)}(A) with
  q*U₀ (same-eigenvalue cup products vanish in H²(H)); ∫_A cl(C_A)² = 24·3072 = 73728. The inertia argument (C32l–n) was
  read, not re-derived.
- **C14, C20, C25, C27, C30, C36, B17, A7, B21, A16, B10, C06/C07, C22**: statement level (run only). C25: a geometrically
  simple Q(i)-Weil fourfold (End = Z[i], NS rank 1) as an Albanese quotient of a ball cover of degree ≤ 43264.

**3. New since the last intake.** Nothing in the run. C32 checked here (it was "carried as background").

**4. Open.** Q1 (1.7): choose CM types with A7's multiplicity space totally definite; solve the MainX kernel/covolume and
terminal-mass equations there; give the analytic correction operator an arithmetic meaning. C32 quantitative: deg_θ C_A,
then HD-WQ/HD-U constants on C25's fourfold. A15–A17, B29–B30, C37–C38 not integrated in the paper.

**5. Relations.** HECKE_DIV P1 (= C13); HODGE_DIVISION and its attack §2.1 (C32); ALP_MACHINE Q2 and NIGHT_AFTER_ALPOGE
Part B (MainX gate). Literature: Schoen 1988 (Compositio 65, Th. 2.0 p. 11, Cor. 3.1 p. 24); Markman (Weil classes);
Li–Zhang (Kudla–Rapoport). Grothendieck: algebraic cycles and the Hodge conjecture for Weil classes; correspondences
(the cycle is a correspondence H⁴ → A); cote 16 scans 044–047 (the 4.1.67 Coates letter, cited by folio).

**6. Candidates.** A short Hexagon note on C32 (the explicit integral cycle and its self-intersection, all even dimensions
2n via C32u), after a literature search against Schoen 1988 and van Geemen's examples. Gate: an independent re-derivation
of the inertia step (C32n).

**7. Problems.** The archive numbering: THETA3 cites folios (scan − 1); any companion text must convert.

## 8. TRACE_DET (prompt 33), final (21 Nov 02:18 UTC)

Return: `TRACE_DET_final_20261121T0218Z_unzipped/TRACE_DET.tex` (81 pp., 79 rows, 426 events; INCOMPLETE on five rows when
the session ended). Prompt: `SENT/33_TRACE_DET_...`. Intakes: cp02, final, primer (a8d75352).

**1. Useful or not.** Marginal for mathematics: the main answer is no (Alpöge's determinants are not det(1 − wB)), and
the positive forms DET-16/DET-18 are classical in substance. Useful for the archive: ARC-01 to ARC-04 correct cote 1.

**2. What it proved.**
- **B-01**: Ξ(√w)/Ξ(0) = det(1 − wB), B = diag(γ_j^{−2}); B ≥ 0 ⟺ RH. **DET-04**: a rank-one non-selfadjoint perturbation
  keeps determinant and traces. **B-02**: no trace-class T has det = Ξ. **DET-11** (re-proved by us): C = B(I + B/4)⁻¹
  gives det(I − s(1−s)C) = 2ξ(s). TPC by us (a8d75352).
- **DET-16** (l.2319): RH ⟺ k(t) = Σ_ρ N_ρ e^{(ρ−½)t}/(ρ(1−ρ)) bounded ⟺ of positive type; unconditional by A. TPC by us.
- **DET-18** (l.1765–1993): for the primitive weighted family of Alpöge's Lean (weights α_i ∈ {1, d^{−1}}, M = 2(3o+1)),
  𝒫_M(s) = det(I − s(1−s)C_{𝓛,M}) with C diagonal (entries [ρ(1−ρ)]⁻¹ with multiplicity MS_ρ, 4 at the centre); GRH for
  the family ⟺ 0 ≤ C ≤ 4I. **TPC of the whole proof by this intake** (was [part]): paired factors symmetric
  (ε_χε_{χ∨} = 1); even central order; D_M of order ≤ ½ hence genus zero; diagonal S₁ operator; resolvent identity by
  v′ = 1 − 2s; GRH gives entries (¼ + t²)⁻¹ ∈ (0, 4].
- **DET-05/06/10** (statement level): the Gram matrix is indefinite; the sign is an inertia balance; the bridge that would
  suffice is a finite arithmetic family of positive finite-rank approximants converging in S₁.
- **MAS-10** (conditional on Masullo Thm 10.2.2.1): det(I − wR₊) = Ξ(√w)/Ξ(0) on his weighted quotient. **MAS-BOUND**
  ((10.3.2.4), p. 454, one derivative order too many), **MAS-SRC-03** (Thm 13.3.1.2, p. 522, empty), **MAS-03**: TPC by us.
- **ARC-01–ARC-04** (cote 1 scans 110–113), **TOY-01/02**: TPC by us.

**3. New since the last intake.** Nothing in the run. DET-18 checked in full here.

**4. Open.** Q-STEP1/4/7 (the historical determinants of Alpöge's steps 1, 4, 7 with parameters from his Lean);
Q-DIRECT-BRIDGE (DET-05's S₁-convergent positive finite-rank family); Q-TRANSCRIPTION (16 cote 1 repairs need the scan
images).

**5. Relations.** HODGE_SIGN (DET-10's inertia sign beside the Hodge index); GCT_NSRH F50 (PRG-FF); ZETA_TWO (DET-16/18 as
cote 1 forms of RH/GRH); the SA23 companion (B ≥ 0 ⟺ DET-16 ⟺ RH). Grothendieck: cote 1 (det(1 − wB), trace formula),
and his own theory of nuclear operators and Fredholm determinants (the trace class S₁ and order-½ products of DET-18 are
exactly that setting).

**6. Candidates.** Cote 1 companion paper (ARC-01–04) after the image check; nothing for Hexagon on the determinant side.

**7. Problems.** None in what was read. DET-18's identification of the Lean family rests on file and line locators in
Alpöge's development, which we have not opened.

## 9. HECKE_DIV (prompt 38), final (21 Nov 02:04 UTC)

Return: `HECKE_DIV_final_20261121T0204Z_unzipped/HECKE_DIV.tex`. Prompt: `SENT/38_HODGE_HECKE_DIVISION_...`. Intakes: cp01,
final, primer (aaf69461).

**1. Useful or not.** Useful within the Hodge-division programme: R21–R23 are the reduction its papers rest on; the
argument is a standard bounded-Chow-plus-Baire argument, so its novelty is modest.

**2. What it proved.**
- **P0** (l.80): N ≤ (deg Z⁺ + deg Z⁻)/(d!√V h) (comass of *t, Wirtinger). TPC by us; superseded by the
  characteristic-free Poincaré-pairing bound in HODGE_BOUNDED_CYCLES.
- **R21** (l.106): {c_t ≤ C} is Zariski closed; algebraic everywhere ⟺ c_t bounded on a Zariski-dense set; fixed-N
  uniformity. TPC by us (aaf69461) and **again by this intake** (Chow components where the flat class difference vanishes
  are open and closed, proper over S; Baire on a ball in the smooth locus; (iv) ⇒ (iii) by closedness).
- **R22** (l.134): a tensor-compatible Hecke orbit is dense; bounded division on it ⟺ algebraicity. **R23** (l.155): if
  c_t is unbounded, c_t → ∞ along every strictly special-generic CM sequence (Tsimerman 2018 Thm 1.3). **A1** (portmanteau:
  equidistribution alone cannot give bounded division), **A2** (h(E_{7^r}) = h(E) + (r/2)log 7): TPC by us.
- **R24A′, R24C, R24E, R24F** (corrections of our sketch), **P6** (bounded degree at infinitely many good primes ⟺
  algebraicity; precedent Brünjes–Serpé arXiv 0901.4853 Th. 3.4), **SQ9** (a uniform cap under Severn): TPC by us.
- **M1, M5–M10** (conditional on Markman), **P4, SQ1–SQ8** (conditional on Severn, Hexagon 2610.00387v2): statement level.

**3. New since the last intake.** Nothing in the run. R21 rechecked here.

**4. Open.** Q24-LEFSCHETZ ("invalid inference; final exclusion not established"); the unconditional E⁸ route (P2b seeds
with P6 at split ordinary primes, or a re-proof of Severn's supplier); optimality of the integers.

**5. Relations.** HODGE_DIVISION (D-G34, HD-U), HODGE_BOUNDED_CYCLES/HODGE_FINISH Paper A, GHOSTS B02/B06 and R10–R12,
THETA3 C13 (= P1), HODGE_SIGN SG-04 (= R24D). Literature: Kollár, Rational curves, I.3.21; Milne, Shimura varieties 5.4,
6.9; Tsimerman 2018; Suslin–Voevodsky 4.4.11–13; SGA 4 XVI 2.2; SGA 6 X App. 7.13.10. Grothendieck: Chow and Hilbert
schemes (FGA 221) as the bounded families; specialization of cycles (SGA 4, SGA 6); the Hodge and standard conjectures;
cote 16 (Coates letters, our scans 044–047, 048–050).

**6. Candidates.** Already in H12/H19/H25 and HODGE_FINISH Paper A. Nothing new.

**7. Problems.** None found.

## 10. DEG_L (prompt 41), checkpoint 06 (21 Nov 05:17 UTC; no final)

Return: `DEG_L_checkpoint_06_20261121T0517Z_unzipped/DEG_L/DEG_L.tex`. Prompt: `SENT/41_HODGE_DEGREES_ARE_L_VALUES_...`.
Intakes: parts 1–2, cp06, primer (ad855737). End state: 72 proved, 41 refuted, 4 open.

**1. Useful or not.** Marginal: it refuted its prompt's premise (T6.2) and found where the difficulty is not (B1: the
L-values are harmless); its useful output is the √J obstruction (B19–B21) and the failure of semiregularity at depth
(S-05/S-06).

**2. What it proved.**
- **T6.1–T6.3**: deg_H f_*[S] = ½Σ∫ξ_ab∧ξ̄_ab; the 032 output class has degree 0 against the product polarization;
  [M]∘f multiplies the degree by M⁴. TPC by us.
- **T6.11–T6.13** (proof read; Haan Thm 3.4 and GQT Thm 11.4(ii) carried): the energy is a finite sum of L-values at
  s = 3/2 and s = 1. **B1**: ζ_K(2σ)/ζ_K(σ) ≤ |L_K(σ,χ)| ≤ ζ_K(σ) for σ > 1. TPC.
- **B19** (TPC by us): covol Hom_E(A₀, A) = 2^{−g}√|D_E|(V/V₀)J; minimal isogeny degree in [J, K_E^g J/g^g]; a Weil-type
  witness of degree O(√J); J ≤ N(f_A).
- **B20, B21** (l.3135–3335): §0 item 12. **TPC by this intake**: generic fibre of h|_{Z₀} = x + (ker h ∩ Stab Z₀);
  h*h_* = deg h on rational cohomology, so ‖e_A h_*w‖ = √(deg h)‖w‖; αI₀ is O_E-stable in Λ, hence in Λ⁻, so
  deg h ≥ J; the universal stabilizer over the Hilbert scheme is proper with finite fibres, hence finite, which bounds
  |Stab Z₀| uniformly in the degree. Carried: B7 (comass), B18 (q₀ ∈ 2Z).
- **S-05, S-06**: for a compact ball quotient Y → A with surface image, dim ker τ_f ≥ g·q(Y) − C(2g, g−2), and q → ∞ along
  congruence covers, so Buchweitz–Flenner semiregularity fails at depth. TPC by us. **S-01** TPC.
- **T6.25, B22a, S-14, S-30–S-41**: statement level.

**3. New since the last intake.** Nothing in the run. B20–B21 checked here.

**4. Open.** Q-BOUNDS, Q-T7-FIXED, Q-DIV, Q-T7-REPLACEMENT (primer).

**5. Relations.** HODGE_DIVISION (46) and its attack (B19, B21; Proposition O = S-14); 46b. Literature: Haan; Gan–Qiu–Takeda;
Milne ANT 4.19, 4.26; Ullmo–Yafaev arXiv 1610.01488 Prop. 4.1; Venkataramana; Calabi–Vesentini; Buchweitz–Flenner; Perry.
Grothendieck: FGA 221 (Lemme 2.4 p. 255, Théorème 3.2 p. 260) for the bounded families; correspondences and pushforward
of cycles; the standard conjectures' positivity (Hodge index in T6.11).

**6. Candidates.** None for Hexagon alone.

**7. Problems.** **Our prompt 46b, sent 22 Nov, carries the overstatement the DEG_L primer warned about.**
`TO_SEND/PRO/1_Archive_research_by_topic/SENT/46b_HODGE_DIVISION_FOLLOWUP_1_DEG_L_open_rows/PROMPT.md` l.27–28: "The
survivors must have rank divisible by the squarefree RM radicand, and rank ≥ 4 if a vector bundle (S-30-S-36)", and l.34–35:
"Start from Markman's construction for n = 2: verify that it passes S-30-S-36, which it must since his theorem holds". The
run proves S-30–S-41 only under restrictive hypotheses (balanced-RM, gluable, simple or nonequivariant, principal
maximal-local-order). Whoever takes in 46b's return should read its answers to these lines with that in mind.

## 11. SIGN_NEXT (prompt 45), checkpoint 02 (21 Nov 04:30 UTC; final by the three-hour rule)

Return: `SIGN_NEXT_checkpoint_02_20261121T0430Z_unzipped/SIGN_NEXT.tex`. Prompt: `SENT/45_SIGN_NEXT_...`. Intakes: cp01,
cp02, primer (aaf69461).

**1. Useful or not.** Useful for the archive: corrected forms of cote 16 scan 050's Proposition and cote 44 Theorem 5
(H04), with a worked example; SN-14 locates the limit of the sign-only method.

**2. What it proved.**
- **SN-C04** (l.334): §0 item 4; **SN-C03** (A₀(T) ⟺ R₀ + G_{L,0}), **SN-C02** (l.198; the literal reading fails on
  P¹×P¹), **SN-C05** (a formal module with R₀, G₀ true and A₀ false), **SN-C01** (the overtyped letter on scan 050 is C):
  TPC by us (aaf69461).
- **SN-10** (classical), **SN-11** (conditional on 032: C, I and semisimplicity for products of abelian varieties;
  unconditional for powers of CM elliptic curves), **SN-12** (l.533; a simple CM fourfold, E = FK, F = Q(α),
  α⁴ − 5α² + α + 1 = 0, K = Q(i), whose Weil lines are not divisor-generated; algebraic by 032), **SN-13**, **SN-14**
  (l.670; in a rigid tensor countermodel all traces factor through R/rad R, so sign-only identities cannot give scan 049's
  positivity): TPC by us. **This intake computed** that α⁴ − 5α² + α + 1 is irreducible and totally real (roots −2.2904,
  −0.3620, 0.5828, 2.0696), with discriminant 6809 = 11·619 and irreducible resolvent cubic z³ + 5z² − 4z − 21, so its
  Galois group is S₄.
- **SN-44-01–05** (l.4229 on): the corrected cote 44 Theorem 5, the node form, the dichotomy, the P²×P² example
  (0 = 3 − (1+1+1)), orthogonal idempotents: TPC by us; agrees with JAC1964 H9-T1/T2.
- **IF-01** (integral Fock intertwiner), **IF-03** (indices on Grothendieck's exterior order, n = 1–4; re-proved by us);
  IF-02, IF-05–IF-12, SN-15, SF-Q6-*: statement level or refuted as listed in the primer.

**3. New since the last intake.** Nothing in the run. SN-12's field recomputed here.

**4. Open.** Q6g-GLOBAL-GEOMETRY (one global m = 2 datum and its Smith factors; IF-13 unreviewed); SN-C04 beyond abelian
varieties (test R₀ and G_{L,0} on X×X for a variety with known B and unknown I); SN-44-06 (nodal factoriality with E ≠ 0
in characteristic p).

**5. Relations.** HODGE_SIGN (H01, SG-04); JAC1964 (H9); C44_POS (51); SA14_SA19 J5. Literature: Kleiman 1968 (2.13, 2A11,
3.11–3.14); Lieberman; Milne 2002 Th. 3.3; Kahn 2024; Chen arXiv 2512.22788 Th. 7.9; SGA 7 XVIII 6.6. Grothendieck: the
standard conjectures B, C, I and of Hodge type (cote 16 scans 034–050; the 4.1.67 letter, scans 044–045); cote 44's 1964
programme of heights on cycles.

**6. Candidates.** H04 (complete mathematically; gates: the scan-004 image check and the write-up as a cote 44 companion);
transcription correction `16_scan050.tex`: `\unsure{C|A}` → C (SN-C01).

**7. Problems.** None found.

---

## Checks made by this intake (all 24 Nov 2026, Claude Opus 5.5 at effort high)

| run | statement | type | outcome |
|---|---|---|---|
| GRH_ALGORITHMS_FINISH | GRH-P148 | targeted proof check | confirmed |
| GRH_ALGORITHMS_FINISH | GRH-P149 | targeted proof check | confirmed, given P147 |
| GRH_ALGORITHMS_FINISH | GRH-P147 | targeted proof check (in part) | conditional step, type primitivity, mask separation confirmed; theta, height and reduction chain not re-derived |
| GRH_ALGORITHMS_FINISH | edition vs cp07 text over §16.2 | used and rechecked | only Codex's two edits differ |
| GRH_ALGORITHMS | GRH-P125 (auxiliary field) | targeted proof check | confirmed |
| GRH_NIGHT | MT-S506 (S506.5–S506.6) | computation | table orthonormal; all seven induction rows confirmed |
| GRH_NIGHT | CX-ALG-016 | computation | 21α ≡ 0 confirmed |
| ZETA_HEAT | thm:cosine-lower-rate | targeted proof check | confirmed given Mori and Voss; constants computed |
| ZETA_NEXT | NG01 | targeted proof check | confirmed given Deligne–Milne and Commelin |
| ZETA_NEXT | NX-L01 example | computation | #E(F₅) = 8, factor 1 + 2t + 5t² |
| ZETA_TWO | IA09 | independent re-proof and computation | confirmed |
| THETA3 | THETA3-C32 | targeted proof check | numerical and cohomological steps confirmed; inertia step read |
| TRACE_DET | DET-18 | targeted proof check | confirmed in full |
| HECKE_DIV | HECKE_DIV-R21 | targeted proof check | confirmed |
| DEG_L | DEG-L.B20, DEG-L.B21 | targeted proof check | confirmed, B7 and B18 carried |
| SIGN_NEXT | SN-12 (the field) | computation | totally real S₄ quartic confirmed |

Scripts (non-rigorous floating point except the exact S₅ and sympy computations): the session scratchpad folder `zg`
(`<local>/AppData\Local\Temp\claude\f2c80a22394db22f\329fb1e6-0570-47be-9060-a2a454bf3e15\scratchpad\zg\`:
`s5.py`, `cos.py`, `ia09.py`).

## What I could not read

Nothing was refused. Not read, by choice of scope: the proofs of 67c's P150–P164 beyond the earlier intake and Codex;
ZETA_HEAT's density theorems, survival and CUE proofs; THETA3's A/B seesaw rows; DEG_L's S-14–S-41; the PDFs of the cited
literature (Suzuki, Mori, Voss, Schoen, LLS, von Känel–Kret, Pazuki), which were taken at the runs' locators. No Tang
paragraph of the 67c paper was opened.
