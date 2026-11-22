# Whole-proof review of AM-R-004

Reviewer: /root/lift_accounting, GPT-6 Astra Pro; reasoning effort not exposed.
Run ALP_MACHINE, 2026-11-21. Reviewed read-only:
`work/research/jacobian_period_theta.md`, the entire
`work/scripts/jacobian_theta_certificate.py`, its saved exact rational
output, and the targeted primary Tadokoro text for Proposition 3.2,
Proposition 4.1 and Theorem 4.4.

## Outcome

**PASS at the stated geometric and analytic scope.** This is a targeted
whole-proof check, not a Lean build, a proof of the arithmetic MainX ties,
or an independent re-proof of Tadokoro's theorem. No mathematical correction
to the saved proof was needed.

## Details checked

1. **The homology basis and period signs.** Tadokoro's Proposition 3.2
   uses paths denoted gamma in that paper; these are the paths called
   lambda in AM-R-004. Its natural cycles become
   `a_i^T = −γ_(2i−1)` and `b_i^T = Σ_(k=0)^(i−1) γ_(2k)` in the
   manuscript's adjacent-difference notation. The new a-cycles are
   successive differences of the old b-cycles; the new b-cycles are
   negative tail sums of the old a-cycles. Their intersection matrix is
   exactly symplectic. The factor −2i/7 in the path integral includes
   the return on the second sheet and has the correct sign.

2. **The integral CM lattice and Riemann form.** The six adjacent cycles
   form an integral basis, giving the columns of the embedding lattice
   of Z[ζ]. The cyclotomic trace gives +1 for adjacent exponents in the
   stated order and −1 in the reversed order. The positive imaginary
   signs of the three selected embeddings of ξ agree with the
   polarization convention. Its codifferent ideal has exponent −5,
   as required by discriminant 7^5. This does not substitute for the
   intersection calculation, which is explicitly given.

3. **Covolume versus the Hodge metric.** The expression
   `G = P Y conjugate(P)^T` is the Riemann bilinear Gram matrix in the
   actual integral-of-ω coordinates. Its determinant is the real
   covolume in those coordinates. The factor `7^(5/2)/8` is the
   usual half-complex embedding-lattice covolume for the degree-six
   cyclotomic ring. The manuscript correctly withholds identification
   of this Euclidean covolume with a MainX level or Haar normalization.

4. **The exact nonvanishing certificate.** Every series bound in the
   script uses Fraction arithmetic. The alternating arctangent bounds,
   sine bounds on arguments less than π/2, outward matrix rounding,
   Gershgorin bound, and sign-aware lower bounds on n^T Y n are valid.
   Inverting the positive Taylor partial sum gives an upper bound on
   exp(−t), and rounding it up preserves that direction. The complement
   of the cube is bounded with a union bound, hence overlap causes no
   issue. The rational final bound is strictly below 3/8. The proof
   then applies to all integer κ≥1 by monotonicity of every absolute
   Gaussian summand. The separately printed decimal is not used as a
   premise.

5. **The line and Chern gauge.** Reindexing n→n+b under z→z+a+τb
   gives precisely the L^κ factor of automorphy. The theta frame has
   connection coefficient `πκY^(−1)(z−bar z)`. The change
   `e′=exp(−Q)e` changes this to `−πκY^(−1)bar z`, so its restriction
   to formal holomorphic directions at zero is zero in all orders.
   Therefore the derivatives used in the proof are indeed the
   holomorphic covariant derivatives in that specified frame.

6. **The uniform analytic bound and level factor.** Completing the
   square gives the shifted Gaussian sum. The one-dimensional bound
   by 1 plus the Gaussian integral is valid after retaining a nearest
   sample, including the case of two nearest samples. Applying the
   eigenvalue bound and dividing by 5/8 gives 3125/64<49. The inverse
   metric transformation has the correct transpose: the quadratic
   form is bar(u)^T G^(−1)u. Polydisk optimization at
   `R_i²=α_iG_i/(πκ)` is exact, with zero orders handled by a limit.
   Thus `κ=M²` produces exactly `M^|α|`, which is removed by the
   source-shaped normalization.

7. **The L² integral.** Because κ is a positive integer, integration
   in the real x-coordinates kills precisely the Fourier cross terms
   with n≠m. The remaining sum over n and integral over t unfold into
   a single Gaussian integral on R³. This proves the determinant
   factor in (R4.12), with no missing factor κ³ or torus covolume
   because the measure was explicitly fixed to probability Haar.

## Scope retained

The proof constructs actual analytic sections and a unit value at zero.
It does not construct a nonzero prescribed positive-degree harmonic jet,
identify an arithmetic CM-stable representative of the chosen line, or
compare its rigidification with the primitive trace-one source frame.
The manuscript explicitly states each limitation. ALP-LIFT-05 and
ALP-LIFT-06 provide the compatible induced eigenbasis and the metric
comparison; those do not change the arithmetic limitations of AM-R-004.

