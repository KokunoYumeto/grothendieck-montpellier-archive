# The structural findings of 23 Nov, distributed over the Pro prompts

Main session 329fb1e6 (Claude Opus 5.5 at effort max), 23 Nov 2026 ~18:5x UTC. The user: [the user's words, omitted] The notes are in this folder; each item names its note and section. Every item enters a prompt as a lead or a
question for the run to work through, with its locator and its check state. Items marked "from memory" in a note must be
opened at the source by the run before use; nothing is graded.

## A. Waiting prompts, updated

### 69_BEYOND_DIRICHLET: the cubic rung (four notes converge here)
1. The single missing L-function: L_K(s, χ_{p,r}) with ζ_E = ζ_K·(ζ_F/ζ)^{r−1} on AGL₁(F_r). P017 (GRH_ALGORITHMS) and
   H04.4 (ALP_CONNES/ALP_MACHINE AM-H04) are the same one-sided estimate for its prime sum; the table of the four
   places. GRH_RUNGS §2.
2. The automorphic identity: ζ_F/ζ for F = Q(∛269) = L_K(s, χ) = the L-function of a weight-one dihedral newform of
   level 217083, the coefficient match checked prime by prime. The Rankin-Selberg square
   L(s, θ_χ × θ̄_χ) = ζ(s)·L(s, χ₋₃)·L(s, ρ) and its Landau positivity as the GL₂ × GL₂ form of AM-H04's window.
   NCG_ZETA Map 5, §2 statement 2.
3. The cubic analogue of Alpöge's sign step: Kubota-Patterson's cubic theta; the order-3 phase sign identity tested at
   χ_{269,3} (GRH_RUNGS §4, §7.3). The decisive question first: does the Weil representation of a cubic character carry
   an operator s of order 3 commuting with Frobenius, or only a reflecting one (ALP_MACHINE phase lemmas S1-S3)?
   KTHEORY_CM_THETA §4.5.
4. The 3-adic price of Q(ω): every integral projector polynomial over Q(ω) ≡ e_W has 3-adic denominator ≥ 3^{c(n)};
   compute c(n). HODGE §4.4 (quantifies AM-S2).
5. G219 through a 7-adic L-function: s(e) = ord₇ of a Katz 7-adic L-value (Rubin's main conjecture, from memory, to be
   opened). NCG_ZETA §4.2.
6. One family across runs: the cubic gate at p = 269 (ALP_CONNES) and at every hard p, r = 3 (GRH_ALGORITHMS); does the
   budget method extend uniformly in p? NCG_ZETA §4.4.
7. The composite pure-field identity for Kummer towers Q(ζ_n, a^{1/n}) (Hooley's input, AN_GRH) as one family of Hecke
   L-functions L_{Q(ζ_n)}(s, χ_{a,d}). GRH_RUNGS §7.1.
8. P145's dictionary made exact (the primes p where the cofactor algebra witnesses the χ_{p,r}-Frobenius condition).
   GRH_RUNGS §7.2.
9. What follows once the cubic RH holds: Koiran's HN ∈ AM for dihedral-cubic solution fields (CX-K01); P001's auxiliary
   prime at r = 3; cubic fields in poly(log p) (to trace against GRH_ALGORITHMS Q01). AG_HODGE_ANT B.7.2.
10. The same rung over other imaginary quadratic fields, as parallel test cases: the Hecke characters of Q(i) cutting out
    Q(i, 2^{1/4}) (D₄; GALOIS_GT §4.3) and the weight-one eta products of M24 and Co0 frame shapes, η(τ)η(23τ) over
    Q(√−23) (MOONSHINE B.3, B.9.8).
11. (R_B) for explicit S₅ fields of Calegari's family by certified computation (MAS_ARTIN; GRH_RUNGS §7.4).

### 68_CONNES_AFTER_RH: the trace formula and positivity
1. T50_K: the positivity half of the trace formula over K = Q(ω), unconditionally (the T50 argument with a Hecke
   Möbius bound); then T51 over K needs a K-analogue of AC-T49 and the K-version of the Connes-Consani-Marcolli
   criterion. NCG_ZETA §2.1, §4.1 (its forward half is 69's cubic family).
2. One mechanism in four places: positivity of a Toeplitz form detects zeros (Weil windows, backward-heat Toeplitz
   minors, Li sections, GCT structure constants); the defect is positive unconditionally and the hypothesis is that its
   limit vanishes. Compare the heat-flow failure order m_*(−a) with the Weil-window eigenvalue a₁(L) ~ λ⁹e^{−4πλ²} at
   a ~ 1/L²: ZETA_HEAT's limits may give ALP_CONNES's missing a₂ lower bound, or the reverse. NCG_ZETA §3(a)(b), §4.3.
3. The positivity obstruction at the next rung: Connes-type positivity fails for the Dedekind zeta of a non-abelian
   field by induction multiplicities (MT-M23); pose it per irreducible ρ (MT-M20). The positive-type measure with atoms
   at log p in AC-T51 and in MAS_ARTIN's difference datum (Cohen's theorem). GRH_RUNGS §3, §6.2.
4. The remainder as an honest trace: the Gysin kernel of the sign-only purity proof (cote 16) against the cutoff defect;
   SN-14: effectivity is weaker than positivity. HODGE §3.1-3.2.
5. The GL_n rung of the cutoff trace formula: what a finite-rank cutoff with asymptotically positive defect would be
   (the prolate selection's analogue). NCG_ZETA §2.3.
6. Bost-Connes and CMR systems (from memory, to be opened): the cubic gate as RH for one twisted partition function of
   the CMR system of Q(√−3). NCG_ZETA Map 6.

### 93_SPLIT_ZERO_AFTER_FGJM: the basepoint, the F₁ counts and the nonstandard RH
1. Counts with the basepoint ↔ the Witt ring of Euler products: c ↦ Z_c = Π ζ(s − j)^{a_j}, ζ the unit; purity of the
   counts = A on each Tate twist. NCG_ZETA Map 4.
2. The basepoint interpolation L_t(s) = ζ(s, 1 + t): track the zeros from t = 0 to t = 1 (Davenport-Heilbronn, from
   memory, to be opened). NCG_ZETA §4.5.
3. GCT's rung test at rank 4: the smallest ring over which Ȟ₄ has a positive basis; the dimension-ring minimum at rank
   4. GCT §4.2. A point-count model for k_n(s) (varieties with #Y_s(F_q) = k_n(s)). GCT §4.3.
4. When purity gives positivity and when not (the naive sign fails at roots of unity). GCT §3.2.

## B. New prompt (no waiting prompt touches it)

### FLEET_HARD_LINKS (new): the level spaces of the permanent and the monotone-circuit bounds
Coordinate with session 672ae3a0 (the fleet interface), which planned a Pro prompt for the S_k reduction: one prompt.
- Part A, L-gct-086: the connected Kneser route in cumulant form (c₅, c₆ on doubly centred matrices; a Kneser-type
  inequality with k growing linearly in n) (GCT §4.1); the matrix zeta function of a level space (GCT §4.5);
  Proposition B.2 with transposition and the torus-fixed points of Z_k ⊂ OG(k, N), computed at n = 4 (AG_HODGE_ANT
  B.7.1); the Klein slice over Q(√−7), exactly, then W ⊕ W̄ (MOONSHINE B.9.1, A2); frame shapes and rank-one level lines
  (MOONSHINE A5).
- Part B, monotone circuits 606/608/650: the tetracode completion of PG(2,3) (an AG(2,3) search at 44 gates plus the
  points at infinity), the Leech-root ladder (targets 39, 59, 125), the Golay code and PG(2,4) hyperovals (714/715)
  (MOONSHINE A3, A4, A8); the inverse-semiring lift's component lemma (MOONSHINE B.9.6; the reading itself is in 93).
- Part C, complexity and arithmetic: the Hasse-Witt scalar mod p ≥ 3 as #SAT mod p (GCT §4.4; AG_HODGE_ANT B.7.3); the
  witness degree c_t with a Q05-type dichotomy (AG_HODGE_ANT B.7.6); Chebotarev for class groups (B.7.4); heights in the
  DIV reduction (B.7.5); theta characteristics for L-pcx-071 (B.7.7).

## C. Continuations of earlier runs (built when their run allows)

### 70d_HODGE_NEXT (after HODGE_FINISH, 70c, final)
HODGE §4.1 (an explicit one-prime criterion over Q(i), Q(ω) through A: E_D effective, Q27), §4.2 (a rate for ghosts),
§4.3 (central-value detectors: Kudla-Millson cycles on U(n, n), Rallis sums at s = 1/2; LIFT077), §4.5 (the Mumford block
by tensor induction, the K3 side); with HODGE_FINISH's own open rows and gates (Schoen 2007 locator; Bolognesi-Laterveer).

### GT_AFTER_H17 (successor of DELTA23 and the GT tower line)
GALOIS_GT §4.1 (H¹(Λ₀, F₂)^{GT̂} against the quadratic characters vanishing on GT̂), §4.2 (GT̂ and the degeneracy maps
of Γ₀(N), N = 2, 3), §4.5 (the supersingular algebra (−1, −3) at 3 as an invariant of the frame pair); MOONSHINE B.9.3
(the level-12 GL₁ layer of H17's frames; E.65's Δ against H17's Δ).

### 75's successor (after NIGHT_AFTER_ALPOGE's final; Part C, the K-groups of Z, is still queued in the run)
KTHEORY_CM_THETA §4.1 (the order-5 gate needs an arithmetic annihilator: Stickelberger/Herbrand, the cyclotomic-unit
Euler system, norm surjectivity from the quintic layer of Q(μ_{p²})), §4.3 (the U(3) endoscopic part as a closed formula),
§4.4 (the CM-elliptic kernel with the pole method), §4.2 (explicit-exponent Galois orbits on Hodge-type Shimura
subvarieties, after H15); GALOIS_GT §4.4 (Ihara at the remaining plus characters, p = 37, non-Gorenstein Eisenstein ideal).

### Moonshine at the GL₁ rung (new candidate, to weigh with the user)
MOONSHINE B.9.2 (Θ_J's level-3 weight-12 newform and the 129 planes; also for the S6 lattice lane, session 5c7e951b),
B.9.4 (umbral multiplicities from L-values), B.9.5 (shadows: L(2s − 1, ψ)).



## State (18:48 UTC)
- DONE: 69 (item 9), 68 (item 5), 93 (questions 5-7) rebuilt and placed; NEW 70d_HODGE_EFFECTIVE and 95_GT_AFTER_H17 built and placed (lints PASS).
- ASKED: FLEET_HARD_LINKS of session 672ae3a0 (18:47 UTC).
- WAITING: 75's successor (after NIGHT_AFTER_ALPOGE's final); moonshine at the GL1 rung (the user's call).
