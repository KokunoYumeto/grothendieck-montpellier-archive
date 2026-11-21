# Fresh full review: F48 spectral supplement

Reviewer: `/root/rectangular_and_theta`. Date: 2026-11-21 UTC.
Source: `agent_tensor_weil_spectral_supplement.md`.
Reviewed SHA256: `a39df1249bb99292f3984625de80c569f4ee3214535909f31f50a1995fccc2a6`.
Scope: complete reading and independent reconstruction of S1--S5. This is a mathematical review, not a proof-assistant certificate or a check of an as-yet-unseen generated fragment.

**Result: PASS. No mathematical correction requested.**

## S1: convergent unit-circle traces

The first difference tends to zero. After equal roots have been grouped, its Cesàro mean square is exactly the sum of squared coefficient moduli in the limit, since each off-diagonal geometric average tends to zero. Thus every coefficient `m_alpha(alpha-1)` vanishes. Actual positive multiplicities prevent an invisible eigenvalue from disappearing during the initial grouping. This proves the claimed conclusion without assuming convergence of individual phases.

## S2: rational spectral retuning

The rational trace is bounded on the sequence `b^n`, hence its Laurent order at infinity is at most zero. Its values therefore converge to its finite limit at infinity. S1 gives unit eigenvalues at the base parameter. Spectral retuning now identifies every coefficient of the characteristic polynomial at infinitely many distinct regular parameter values; a rational function with these infinitely many zeros is identically zero. The family is unipotent by Cayley--Hamilton, with no diagonalizability hypothesis.

## S3: the actual full centralizer

For `b>1`, `D>4` and the displayed root difference is nonzero, so the actual split algebra has the four stated simple blocks. The element `F(b)-I` is nilpotent and central in the full commutant of `F(b)`. If that commutant is semisimple, its center contains no nonzero nilpotent, hence `F(b)=I`. Its full commutant is then a single matrix algebra, contradicting the actual nonsimple four-block algebra. Scalar extension preserves this calculation because a matrix commutant is the kernel of a finite system of linear equations. The conclusion excludes full-centralizer identifications, not faithful subalgebra actions.

The single integral weight normalization `v^{-w}F(v)` is rational, preserves every centralizer, and preserves the stated spectral retuning formula. Its modulus at `v=b` is one. The inverse-parameter variant follows by replacing `v` with `v^{-1}`. Mixed weights are correctly left outside this assertion.

## S4: exact matrix-law classification

In a constant Jordan basis for `F(b)`, each nonzero diagonal rational function has values `alpha^n`; ratios of consecutive values force `alpha=b^m` for an integer Laurent order `m`. Infinite equality then forces the function to be `v^m`.

If a Jordan block had length at least two, its first superdiagonal rational function would have values `n alpha^{n-1}`. The same ratio argument fixes its Laurent order at `m`, but division by `b^{mn}` would simultaneously converge to a finite leading coefficient and equal the unbounded sequence `n/alpha`. This contradiction eliminates every nontrivial Jordan block. All off-diagonal rational entries in the resulting constant diagonal basis vanish identically by infinitely many evaluations. The converse and pure-weight-zero specialization are immediate.

The distinction between matrix equality in one fixed trivialization and an unlabeled spectral condition is preserved throughout. In particular, the supplement does not incorrectly conclude that a unipotent rational family is the identity under spectral retuning alone.

## Scope

All arguments use the expressly imposed rational dependence and all-extension comparison. No step infers these hypotheses from fixed-field Weil purity, ordinary tensor actions, or a parameterwise isomorphism. No source theorem beyond the already checked actual rank-three decomposition is newly invoked.

## Addendum: complete second-supplement check

Also read in full: agent_tensor_weil_collision_supplement.md, SHA256
d6a44ebb1767988ce31406875a76fdaa2d8e48e94c0e7561f56544b866f8bba9.
Review scope: all of C1--C8, including the complete recurrence proof and the center lemma. **PASS; no mathematical correction requested.**

The finite power sum has a recurrence with nonzero constant coefficient because every eigenvalue is nonzero. Passing from infinitely many evaluations to the rational identity is valid after excluding the finitely many poles. At a nonzero finite pole of maximal modulus, every scaled term with a positive scale index has its poles at strictly smaller modulus; hence the term with the nonzero constant recurrence coefficient is the only singular term there. This proves Laurentness. Finite Vandermonde uniqueness then matches all actual eigenvalues, including multiplicities, to distinct positive real powers b^m. The characteristic-polynomial identity follows coefficientwise by infinitely many evaluations.

The center-of-centralizer proof works over every field for a nilpotent operator. Commutation with each cyclic-summand projection forces block diagonality; commutation with the quotient map from a largest cyclic block forces every block's polynomial to be the reduction of the same polynomial. Conversely that polynomial in the operator commutes with the entire commutant. A largest block identifies the kernel exactly as (t^s), so this center is local.

Regularity of the characteristic-zero rational matrix family at v=1 permits specialization of its proved characteristic polynomial, giving the single eigenvalue 1. The preceding center lemma therefore rules out the actual three-component collision center, regardless of auxiliary rank or Jordan sizes. This proves the mixed-weight extension under its specifically retained regularity and full-centralizer assumptions. The lemma's validity in arbitrary characteristic does not amount to an unmentioned reduction-mod-p theorem for the original complex rational family.

The inverse-parameter convention, parameter-dependent changes giving another regular model, and the exclusions for nonflat changing-rank objects, proper subalgebras of a commutant, and word-dependent coefficient objects are all correctly scoped. This proof does not infer all-extension retuning from a chosen arithmetic Frobenius.
