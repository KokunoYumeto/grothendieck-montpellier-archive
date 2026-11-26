# Primer: THETA3 (prompt 37, HODGE_THETA): three signatures

By Claude Opus 5.5 at effort high (agent aaf694615cb43adc1), 23 Nov 2026. The sources are my intakes
`INTAKE_THETA3_20261121.md` (checkpoint 01) and `_part2` (checkpoint 03), `_part3` (checkpoint 04) and `_part4`
(checkpoint 07, the final by the three-hour rule), with their check events.

- **Returns:** `research_returns\THETA3_checkpoint_0N_…_unzipped\THETA3.tex`. The run is GPT-6 Astra (ChatGPT Pro mode),
  from 00:49 UTC on 21 Nov 2026.
- **Labels:** 11 targeted proof checks (Q1–Q9, C12, C13); the rest statement level.
- **Archive numbering:** THETA3 cites folios. Its "cote 16 scans 43–46" is our 044–047, and "cote 44 scans 7–8" is our
  008–009.

## The question

The Hodge sketch's 1.7: one seesaw pairing that links the signature-(2,1) theta machine of OpenAI's CM Hodge proof
(032 §§4.5–4.7) with the totally definite groups of Alpöge's chain (MainX).

**At the end: PARTLY PROVED.**
- The analytic seesaw and the finite transform are proved.
- The arithmetic MainX matching is open.

## 1. Effective continuity of 032's non-vanishing (Q1–Q9; targeted checks)

- **Q1 (period perturbation):** Cauchy–Schwarz and the reverse triangle inequality. The sign uses ∫ξ∧ξ̄ > 0 for
  (2,0)-forms; the factor d comes from a degree-d cover.
- **Q2 (Gaussian isolation):** a shell count (2j+3)^d and r e^{−πλr²/2} ≤ 1/√(πeλ). The certificate:
  c = 2πe^{−2π} ≈ 0.011733, E(6) ≈ 1.77·10⁻⁸, c² ≈ 1.3767·10⁻⁴ > 1.37·10⁻⁴ (thin, positive).
- **Q3:** rational rounding.
- **Q4/Q5, Q7 (given A1):** A1 is the anisotropic zero-orbit identity, the averaged theta coefficient = Φ(0). Then
  maximum ≥ mean, automorphy, and a Lipschitz shell bound.
- **Q6 (the Fock determinant):** ‖P_{u,v}‖² = 2(‖u‖²‖v‖² − |⟨u,v⟩|²).
- **Q8:** volume normalizations.
- **Q9 (resultant projector):** uf + vg = R gives e = 1 on ker f(T) and 0 on ker g(T). The same as HECKE_DIV P1.

**Meaning:** 032's non-vanishing is Gaussian concentration plus continuity, with no Rallis or Bessel identity. This
corrects the sketch's Route 1 reading.

**Good for:** explicit constants for that step.

## 2. Weil-space extraction (C13, C14)

- **C13 (checked):** an explicit algebraic projector onto W.
  - a = M + b₀ with 0 < arg a < 1/(2n);
  - e_W = R⁻¹v(T)g(T) composed with the Künneth projector;
  - since a^{2n} ∉ Q, one nonzero projection α gives the spanning pair (α, Tα);
  - one nonzero period suffices.

  This is the device later made quantitative in Theorem W, HD-WQ and HD-U.
- **C14 (statement level):** constructions from curve products miss W when NS(A)_Q = Qθ, by stability of the Lefschetz
  algebra under homomorphism pushforward and Pontryagin product.

## 3. The seesaw and its gate (A1–A17, B9–B30)

- **B17:** the actual wedge is a literal double lift V → P → V with a common positive Q⁻¹, plus the last-step Bessel
  seesaw.
  - **G1 (the limit, from the run's Part II):** the upper space is A ⊥ H, of signature (3,1) at every real place, not
    totally definite.
- **A7:** the multiplicity space is totally definite exactly when the selected first-list CM types agree.
- **B21:** the residual raw scalar is a full Hodge-determinant period ratio; linear CM-type balance does not make it
  algebraic.
- **A16:** refutes "universal field-preserving full-host enlargement" (an explicit non-normal quartic CM field).
- **B10:** no direct rank-three specialization of the global matching.
- **B4, B6:** no lower bound from scalar rescaling or two rank-one projections.
- **C01:** on congruence ball quotients the whole Albanese is CM.

## 4. Sources on ball quotients, and an exceptional cycle (C12–C38)

- **C12 (checked):** a period of 500 on Schoen's surface: degree 5·5·5·4, F with j = 2048 non-CM. It is a product of
  diagonals, not a new Hodge case.
- **C16, C20:** non-CM and simple non-CM weight-one sources occur as Albanese quotients of covers of one ball surface. In
  C20 a genus-two Jacobian with End = Z (y² = (x−a)φ(x), a = x(P), P ∈ E[7]) occurs at degree ≤ 1764; End = Z is
  checked by reductions over F₃₇ and F₃₇².
- **C25:** a geometrically simple Q(i)-Weil fourfold, a hyperelliptic Jacobian with branch points from 8- and 13-torsion
  of y² = x³ − 30x − 25, with End = Z[i] and NS rank 1. It is an Albanese quotient of a ball cover of degree ≤ 43264.
  Its Weil classes are already algebraic by Markman; it is a test object.
- **C27:** the map-based route reduces to a finite quartic cup test F_X on Hom_K⁰(Alb X, A) (at most 5^m combinations);
  a fixed-source deformation is obstructed, since Kodaira–Spencer is injective. The test vanishes on the covers of C28
  and C30.
- **C32 (the notable final finding):**
  - for H: y² = z∏_{j=1}^4(z² − a_j²) with ρ(z,y) = (−z, iy), the Jacobian carries an explicit integral C_A ∈ CH² with
    0 ≠ cl(C_A) ∈ W_{Q(i)}, ∫cl(C_A)² = 73728;
  - the family includes C25's fourfold;
  - the method is Schoen 1988, Th. 2.0 (p. 11) and Cor. 3.1 (p. 24), in a ramified case with paired branch points; not
    the theta machine, and not Markman;
  - [2+i]^* gives the second direction.
- **C36:** products in every even dimension (not new exceptional cases).
- **C30:** two-base Pryms and single-fibration towers give no new sources.
- **C06/C07:** local Kudla–Rapoport-type examples. C06 has Int = q + 2 − q² < 0 for q ≥ 3 at L = πI₃ (Li–Zhang
  Th. 3.4.1, 3.5.1 cited); C07 has Int = a + 1. Novelty unsearched.
- **C22:** the weaker slope is sharp for an actual theta section (y² = 4x³ − 4x, p = 7).

## 5. Open rows

| Row | Gate |
|---|---|
| Q1 (1.7) | choose CM types with A7's space totally definite; solve the MainX kernel/covolume and terminal-mass equations there; give the analytic correction operator an arithmetic meaning |
| C32 quantitative | record deg_θ C_A; then HD-WQ/HD-U give explicit c_t on the C25 fourfold |
| Proofs | A15–A17, B29–B30 and C37–C38 were not integrated in the paper at checkpoint 07 |

## 6. Where it went

- C13 became the projector of the division attack and HODGE_DIVISION.
- C32 was cited in the attack's §2.1.
- The MainX gate passed to ALP_MACHINE (Q2, the definite pairing) and NIGHT_AFTER_ALPOGE Part B.
