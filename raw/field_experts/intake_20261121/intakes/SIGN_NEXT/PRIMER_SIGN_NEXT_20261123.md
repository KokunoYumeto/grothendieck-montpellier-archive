# Primer: SIGN_NEXT (prompt 45): Grothendieck's Hodge-index route after the sign-only proof

By Claude Opus 5.5 at effort high (agent aaf694615cb43adc1), 23 Nov 2026. The sources are my intakes
`INTAKE_SIGN_NEXT_20261121.md` (checkpoint 01) and `INTAKE_SIGN_NEXT_20261121_part2.md` (checkpoint 02, the final by the
three-hour rule), with their check events.

- **Returns:** `research_returns\SIGN_NEXT_checkpoint_01_20261121T0344Z_unzipped\` and `…checkpoint_02_20261121T0430Z…`
  (SIGN_NEXT.tex). The run is GPT-6 Astra (ChatGPT Pro mode).
- **Numbering:** cote 16 scans are ours (= PDF page; folio = scan − 1).

## 1. The corrected Proposition of cote 16, scan 050 (SN-C01–SN-C05)

**Statement (SN-C04).** C_G(X) ⟺ C_G(Y) + R₀(T,W) + G_{L,0}(T,W).
- Y is a smooth hyperplane section of X.
- W is a hyperplane section of T = X×X, not Y×Y.
- R₀ is the restriction condition; G_{L,0} is surjectivity of L_T∘j_* on algebraic classes in the critical degree.
- C_G = Kleiman's B(X): Λ algebraic.

This is Grothendieck's Proposition (A″ with the missing factor L_T restored), and in substance Kleiman 1968, Th. 2.13
(i), (ii′).

**Lemmas and mechanism.**
- **SN-C03.** L_T² = g·L_W·r = L_T·j_*·r; then A₀(T) ⟺ R₀ + G_{L,0}, and G_{L,0} ⟺ G₀ + A₀(W). Each direction is a few
  lines from hard Lefschetz injectivity and the weak Lefschetz isomorphisms r, g.
- **SN-C02 (the literal reading fails).** j_*Alg^{m−1}(W) = Alg^m(T) is false. On P¹×P¹ with a (1,1)-curve, j_*1 = a + b
  spans one line against Alg¹ = Qa ⊕ Qb.
- **SN-C05:** a formal module with R₀ and G₀ true but A₀ false.
- **SN-C01 (the source):** the overtyped letter on scan 050 is read as **C** (Kleiman 2.13; the 4.1.67 letter's
  Proposition (ii bis), our scans 044–045; the CSG transcription L11d, p. 3).

**Good for:** a citable correct form of Grothendieck's remark, and a transcription correction (`16_scan050.tex`:
`\unsure{C|A}` → C).

## 2. C and I for abelian varieties (SN-10–SN-13)

- **SN-10:** the abelian Lefschetz theorem (Kleiman 2A11; Lieberman) makes Λ algebraic. Λ_Y = j^*Λ_A²j_* is our scan 040.
  Classical.
- **SN-11 (conditional on 032):**
  - the chain: 032 Th. 1.1 (Hodge for CM abelian varieties, unrefereed; human proof van Hoften–Sempliner, Hexagon
    2610.00259) → Milne 2002 Th. 3.3 (= Th. 4.6 of 2002aS; the Hodge standard conjecture for abelian varieties) →
    Kleiman 3.11, 3.12, 3.14;
  - conclusion: C, I and semisimplicity, with algebraic splittings, for all products of abelian varieties;
  - unconditional for powers of CM elliptic curves (HODGE_SIGN SG-04 with Milne, Remarks 3.7–3.8).
- **SN-12 (refutes the literal U-02):** a simple CM fourfold with CM field E = FK, F = Q(α), f = T⁴ − 5T² + T + 1
  (Galois group S₄), K = Q(i), CM type of signature (2,2).
  - NS rank is 4, and divisor products have K-bidegree (2,2), so the Weil lines (4,0) and (0,4) are not
    divisor-generated. They are algebraic by 032.
  - The phenomenon is classical; the explicit field is new.
- **SN-13:** v = (u^†u)^{−1}u^† in eRf. Positivity makes u^†u invertible, and its inverse is a polynomial in it.

## 3. The limit of the sign-only method (SN-14)

**Statement.** In a rigid tensor countermodel, N is a single Jordan block and F = c·exp(N), so Tr(aF^s) = 3a₀c^s. All
traces factor through R/rad R, while τ(N^†N) = 0.

**Consequence:** the sign-only identity (H01) cannot by itself give the positivity of scan 049 (semisimplicity), even
with correspondences as coefficients.

## 4. The corrected Theorem 5 of cote 44 (SN-44-01–SN-44-06; H04)

**Statement (SN-44-01).** ⟨z,z′⟩_G = (−1)^m(deg ZZ′ − Σ_s a_s(Z)^t G_s^{−1} a_s(Z′)).
- The sum is over singular fibres.
- a_s are the components on the non-Cartier vertical classes, and G_s their Gram matrices.

**Mechanism.** Orthogonal projection onto the vertical classes modulo the radical:
- smooth-fibre classes are radical, since N_F is trivial;
- an admissible extension exists (Kahn 2024, cited);
- the identification with Néron–Tate rests on Chen, arXiv 2512.22788, Th. 7.9 (over C; preprint).

**Supporting results:**
- **SN-44-02 (the node form):** deg(DD′) = (−1)^m ν(D)ν(D′), with ν = u − v on the exceptional quadric. Here
  p^*D = D̄ + (−1)^{m+1}δE^m and E^{2m} = −1.
- **SN-44-03 (the dichotomy):** if E_van ≠ 0 there is no correction, since the defect maps are injective (SGA 7 XVIII
  6.6). If E_van = 0 the height is zero.
- **SN-44-04 (the worked example):** on P²×P² with Z = a² − ab + b² and three nodal fibres, D_i = {x = e_i, s = s_i}×P²_y,
  with N_{D_i} = Q_y^∨, D_i² = 1 and π^*Z·D_i = 1. So **0 = 3 − (1+1+1)**.
- **SN-44-05:** p_s = (−1)^m D_s × D_s are orthogonal idempotents.

**Agreement:** the same corrected formula as JAC1964 H9-T1/H9-T2, derived independently.

## 5. The integral Lefschetz order (IF-01–IF-13, SN-15; Q6g)

- **IF-01:** the integral Fock intertwiner Φ_n: F_n → Λ*(Z^{2n}) is a bijection of integral bases, with
  y_a∂_{x_a} ↔ p_a∧ and divided powers preserved. It does not identify a global theta integral.
- **IF-02:** the divided-power order Z[L^{(r)}, D^{(r)}] = Q[L,D] ∩ End_Z, of rank (n+1)(n+2)(2n+3)/6.
- **IF-03 (recomputed by me):** indices on Grothendieck's actual exterior order Φ₀ ⊂ End(ΛM₀) (cote 16 scan 014, §7):
  - [A : Z[L,D]] = 1, 2⁷, 2²⁷3⁴, 2⁸¹3³³ for n = 1–4;
  - [A : Z[L,D,π]] = 1, 2², 2¹⁰3², 2³²3¹⁰.
- **SN-15:** all-rank index matrices; n = 5, 6 computed (statement level).
- **IF-10, IF-11:** an algebraic coefficient realization; an inhabited m = 2 theta-jet construction.
- **Refuted:** IF-12 (CM theta kernels do not commute with the fixed root); SF-Q6-01–03 and SF-Q6-07 (shortcut
  realizations); U05 as a lift-count assertion (IF-05, IF-07, IF-09).

## 6. Open rows

| Row | Gate |
|---|---|
| Q6g-GLOBAL-GEOMETRY | one actual global m = 2 datum with SF-Q6-04's ties, and its Smith factors; IF-13 written, not reviewed |
| SN-C04 beyond abelian varieties | test R₀ and G_{L,0} on X×X for a variety with known B and unknown I |
| SN-44-06 | E ≠ 0 nodal factoriality in characteristic p |

## 7. Where it went

- **H04** (cote 44 Th. 5 fails as displayed; the corrected formula): complete mathematically. Its gates are the
  scan-004 image check and the write-up.
- **H11** (Th. 4, C, I for abelian varieties): it waits on 032.
- **H01 v2:** a remark citing SN-14, and the locator "cote 16, scans 034–040" for E^{n−1}.
