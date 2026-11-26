# Primer: HECKE_DIV (prompt 38): bounded division on Hecke orbits

By Claude Opus 5.5 at effort high (agent aaf694615cb43adc1), 23 Nov 2026. The sources are my intakes
`INTAKE_HECKE_DIV_20261121.md` (checkpoint 01) and `INTAKE_HECKE_DIV_20261121_part2.md` (final), with their check
events.

- **Return:** `research_returns\HECKE_DIV_final_20261121T0204Z_unzipped\HECKE_DIV.tex`. The run is GPT-6 Astra (ChatGPT
  Pro mode), 00:49–02:04 UTC on 21 Nov 2026.
- **Locators:** HECKE_DIV.tex lines, as used in SEED_HODGE_DIVISION: P0 at 80, R21 at 106, R22 at 134, R23 at 155,
  SQ1 at 1619.

## Setting

- A polarized family of abelian varieties over a connected base, with a flat Hodge class t.
- c_t(s) = least max(N, deg Z⁺, deg Z⁻) with N·t_s = [Z⁺] − [Z⁻], with Z^± effective integral cycles.
- "Bounded division" means c_t is bounded.

## 1. The exact reduction (P0, R21–R23, A1; all targeted checks)

- **P0 (degree controls the multiplier).** N ≤ (deg Z⁺ + deg Z⁻)/(d!·√V·h), with V = ∫θ^g/g! and h = ‖t‖.
  - Mechanism: β = *t is flat and harmonic, of constant pointwise norm h/√V; its comass is at most that norm;
    Wirtinger gives |∫_Z β| ≤ (h/√V)·deg Z/d!; pair with N·t.
  - Superseded in HODGE_BOUNDED_CYCLES by the characteristic-free Poincaré-pairing bound.
- **R21 (closed loci and uniformity).** {c_t ≤ C} is Zariski closed (relative bounded-degree Chow, Kollár I.3.21; flat
  class differences; properness). By Baire on a ball: algebraic everywhere ⟺ c_t bounded ⟺ bounded on a dense set.
- **R22 (Hecke orbits).** A tensor-compatible Hecke orbit H(Q)·x is dense (real approximation, Milne, *Shimura
  varieties*, 5.4; Riemann's isogeny correspondence). So bounded division on one such orbit, or on the CM points, is
  equivalent to algebraicity.
  - Correction to our sketch: a general unitary similitude moves the Weil plane through its K-determinant, so the group
    must be tensor-compatible.
- **R23 (dichotomy).** If c_t is unbounded, then c_t → ∞ along every strictly special-generic CM sequence. Input:
  André–Oort, Tsimerman 2018, Th. 1.3.
- **A1.** Weak convergence and a proper closed S_C give limsup μ_j(S_C) = 0 (portmanteau). So equidistribution alone
  cannot give bounded division.
- **A2.** Colmez heights grow along a fixed-field orbit: h(E_{7^r}) = h(E) + (r/2)log 7, since 7 splits in Q(ω).

**Good for:** this is the reduction the Hodge-line papers rest on; it is now Paper A of HODGE_FINISH.

## 2. Corrections of our sketch (R24A–R24F)

- **R24A′:** the signed-degree reading of sketch 2.4 is false (an integral class of degree 0).
- **R24C:** 1 + v with v² = 0 is an automorphism of isogeny degree 1, so the endomorphism-degree claim is false. The
  right invariant is effective or graph degree.
- **R24D:** on varieties isogenous to E^g (E = C/Z[ω]), Hodge classes are divisor-generated (= HODGE_SIGN SG-04).
- **R24E (order-stable subvarieties do not detect).**
  - If ι(a)Z = Z, then ι(a)_*cl(Z) = q^n cl(Z), since f: Z → Z has degree q^n.
  - On the Weil lines pushforward acts by a^{2n} and ā^{2n}, neither equal to q^n unless (a/ā)^n = 1.
  - So e_W cl(Z) = 0.
- **R24F:** divisor products do not vanish on CM elliptic powers: u_n + ωv_n = ±∏(U_j + ωV_j).

## 3. Arithmetic lifting (P6; targeted check)

**Statement.** Bounded integral effective degree at infinitely many good primes (with N_v allowed to vary) is equivalent
to algebraicity in characteristic 0.

**Mechanism:**
- bounded Chow over the base (Suslin–Voevodsky 4.4.11, 4.4.13; Anderson's flattening);
- non-dominant components lie over finitely many places;
- a trait through a horizontal component;
- injectivity of specialization (SGA 4 XVI 2.2; cycle classes, SGA 6 X App. 7.13.10);
- Betti–étale comparison.

**Precedent:** Brünjes–Serpé, arXiv 0901.4853, Th. 3.4. So P6 is not new in principle; its varying-multiplier form
equals GHOSTS B06.

## 4. Explicit bounded division, conditional

- **P1, P3:** the Weil projector and seed criterion (a resultant projector; one detector spans the plane). The same as
  THETA3 C13.
- **P2b:** integral divisor-product seeds: 80/80 on E⁴, 147456/175104 on E⁸. Raw transport grows like m^{2n}.
- **M1, M5–M10 (split Q(ω) fourfolds, conditional on Markman, arXiv 2502.03415v2, Th. 1.5.1, Cor. 1.6.1):**
  N ≤ 1080·q·H₃, degrees ≤ 3240·H₃·B₃·D₆·(|a|+|b|). Statement level.
  - The principal component was later made unconditional by GHOSTS R10–R12 (Schoen), and by 36 in HODGE_FINISH.
- **P4, SQ1–SQ9 (split Q(ω) eightfolds, conditional on Severn, Hexagon 2610.00387v2, unrefereed):** SQ1 gives an
  explicit seed degree. SQ9 (deduction checked) gives a uniform cap:
  - Weil classes are primitive; Hodge–Riemann makes the Gram form definite; mass and comass give ‖y_i‖ ≤ B;
  - 1 ≤ d ≤ B⁴; Cramer;
  - globalized by R21.
  - The integers involve factorials of G = 39,191,040 = |G₃₄|.
  - The run's S1–S3 audit of Severn: the group reconstructed, 17 monodromy matrices recomputed.
  - Later reconstructed without Severn's theorem as a premise in HODGE_DIVISION D-G34; the bound became quadratic (HD-U).
- **G1 (archive):** cote 16 folio = our scan − 1. Two Coates letters: our scans 044–047 (4.1.67) and 048–050 (dated
  6.1.1966 as written).

## 5. Open rows at the end

| Row | Gate |
|---|---|
| Q24-LEFSCHETZ | "invalid inference; final exclusion not established" |
| Unconditional E⁸ route | P2b seeds with P6 at split ordinary primes, where End(E_v) = End(E); or a re-proof of Severn's supplier |
| Optimality of the integers | not claimed |

## 6. Where it went

- P0 and R21–R23 became the reduction of the attack (R1–R2), of HODGE_DIVISION, and of HODGE_BOUNDED_CYCLES /
  HODGE_FINISH Paper A.
- SQ1–SQ7 fed HODGE_DIVISION D-G34 (G₃₄ eightfolds).
- P6 is GHOSTS B02/B06 together with Brünjes–Serpé.
- H12/H19/H25 in the Hexagon register.
