# Fresh review of the equal-height open-orbit calculation

Reviewer: `/root/gct_statements`, GPT-6 Astra Pro; effort inherited/not exposed. Date/time: 2026-11-21 00:15 UTC. Review type: complete direct textual/full-proof review and independent dimension/stabilizer reconstruction.

Reviewed file: `agent_rectangular_sphericity.md`.

SHA-256: `536096b3061b29dc16e2711ddf1096b3b91ab9bbe3ec012180e67b173fe7a5e9`.

**Outcome: PASS. No mathematical correction is needed for the stated action and the stated range `1≤r≤n²`.**

## Borel quotient and the action under test

An injective map `W*→E` sends the fixed complete flag in the source to a partial flag of dimensions `1,...,r`. Two injections give the same flag exactly when they differ by the source Borel subgroup. The Borel action is free because the map is injective. Its fibers are therefore Borel torsors, and the quotient is the stated partial flag variety. Dualizing the source merely replaces the chosen Borel by its dual/opposite convention; it changes no dimension or orbit assertion.

The quotient map is smooth and surjective. The inverse image of a single `G` orbit is a single `G×B` orbit because the Borel is transitive in each fiber. Hence openness of those orbits is equivalent. The injection locus is nonempty open when `r≤dim E`, so an open orbit in the full tensor space necessarily meets it. This checks the geometric reduction, not only the dimension formulas.

## Dimensions

With `N=n²`, the full flag dimension is `N(N−1)/2`, the group dimension is `2(N−1)`, and their difference is `(N−1)(N−4)/2`. The displayed `n=3` values and the identical tensor-side deficit are correct.

For partial flags, `Nr−r(r+1)/2` follows either from successive choices of lines in the quotients or from subtracting the Borel fiber dimension from `Nr`. The `r=3` deficit is `N−4`; the increment from `r` to `r+1` is `N−r−1`. It is nonnegative through the full allowed range, with zero for the final redundant step adding `F_N=E`. Thus every `r≥3` in the stated range is excluded for `n≥3`.

## Independent r=2 stabilizer calculation

The open set of invertible matrix lines is a single `SL_n×SL_n` orbit over `C`: a scalar with the required determinant root exists, allowing a representative of determinant one. A generic plane through that line is `span(I,B)` with `B` regular semisimple.

For the action `X↦gXh^t`, stabilizing `CI` gives `gh^t=cI` with `c^n=1`. Stabilizing the plane reduces to `gBg^−1=aI+bB`, with `b≠0`. Since `B` has distinct eigenvalues, the affine map `x↦a+bx` permutes a finite set of at least two distinct points. Its images on two points determine it, so only finitely many possibilities occur. The identity component therefore has `c=1,a=0,b=1` and is precisely the determinant-one centralizer of a regular semisimple matrix, a torus of dimension `n−1`.

It follows that the generic orbit dimension is `2N−n−1`, and the codimension in the partial flag variety is `n−2`. This rules out an open orbit for `n≥3`, despite the naive ambient dimension inequality allowing one. The calculation correctly uses a dense open set, so no exceptional larger orbit elsewhere can be open without meeting the computed generic locus.

For `n=2`, the same calculation gives codimension zero, consistent with the known exceptional small-rank geometry. For `r=1`, the invertible matrix lines give the asserted open orbit, so the claimed boundary of the obstruction is exact.

## Scope and check-event wording

The result excludes the specified Manivel-style `SL_n×SL_n` and output-Borel open-orbit mechanism. It does not exclude more general invariant algebras, standard monomial rules, positive multiplicity formulas, or other auxiliary geometries. The report maintains that scope throughout.

Suggested event: `OPEN-ORBIT-GCT-INDEPENDENT-536096b3`, complete direct read and independent proof reconstruction, PASS. The earlier Manivel construction is cited primary background; no new full independent proof of its invariant-algebra theorem was undertaken here. No numerical approximation or formal proof assistant was used.
