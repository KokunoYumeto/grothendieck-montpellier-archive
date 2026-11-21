# Independent review of purity findings P-01–P-06

Date: 2026-11-21 (Europe/Berlin). Reviewer: `/root/rectangular_bridge`,
GPT-6 Astra Pro, inherited effort (not exposed), run CUE_GCT-20261121.

This event is a targeted whole-proof check by a different agent, not a
formal verification and not an independent literature review of every cited theorem.
The complete statements and complete proofs in `work/purity/findings.tex`
were read. No mathematical gap was found in P-01–P-06.

- **P-01:** Re-expanded the Hermitian Gram quadratic form and checked the
  off-diagonal estimate `b((sum|c|)^2−sum|c|²) ≤ b(s−1)sum|c|²`.
  The sign-cube specialization uses the symmetric difference of supports
  and gives the displayed coefficient-energy criterion exactly.
- **P-02:** Checked distinctness of roots modulo `p`, the degree and
  nonsquare hypotheses in the quadratic character sum, and the zero-value
  repair. At each changed parameter there is exactly one zero factor and
  the product changes from zero to a unit, so the additive error is at
  most `|T|`, not `2|T|`. The stated prime threshold implies the strict
  Gram inequality. The evaluation matrix is integral, and a nonzero
  integer maximal minor proves independence over every characteristic-zero
  field. No characteristic-p conclusion follows or is claimed.
- **P-03(a):** Checked the width-one product at every sign vector. It is
  nonzero only at the omitted vector and has value `2^n` there. The converse
  tensor Vandermonde matrix is invertible precisely under the stated
  characteristic restriction.
- **P-03(b):** Multiplied the displayed row and matrix: the result is
  `(x2−x1, x2²−x1², x1*x2*(x2−x1))`. Multiplication by the final column
  gives `(x2−x1)(x3−x1)(x3−x2)`. The two-symbol alphabet forces a repeated
  coordinate and hence zero, in every characteristic.
- **P-04:** Checked pole-divisor domination term by term, treatment of
  nonzero constants, degree-zero principal divisors, and subtraction of
  excluded rational points. The conclusion correctly assumes a nonzero
  pullback and does not assert that purity proves that assumption.
- **P-05:** Checked that all `(2δ+1)^2` monomials lie in `L(4δD)`, of
  dimension at most `4δ²+1`. The stated divisor-space estimate is valid
  after algebraic closure and descends. The product relation is nonzero
  in `k[X,Y]`, has the claimed bidegree, and the displayed coefficient row
  gives width at most the individual degree plus one.
- **P-06:** Checked that weight zero identifies conjugated traces with
  dual traces; that affine-curve lisse sheaves have `H_c^0=0`; and that
  geometric Schur orthogonality gives `H_c² = Q_l(−1)` on the diagonal
  and zero off it. Arithmetic Frobenius fixes the scalar endomorphism,
  so the diagonal main term is exactly `q`, not an unspecified phase.
  The `H_c¹` weight bound yields entrywise error at most `B*sqrt(q)` and
  operator error at most `s*B*sqrt(q)`. The strict hypothesis also forces
  at least one rational point, justifying the division by `Q`.

P-07 was present in the file and read; its collision-polynomial proof also
has no gap apparent to this reviewer. P-08 was read but its precise
Lagarias–Odlyzko locator and arithmetic estimate were not independently
verified, so no proof-check event is claimed for P-08 here.

No changes to the mathematical statements were required by this review.
