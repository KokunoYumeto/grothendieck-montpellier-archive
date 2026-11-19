# Independent review of C.1o and C.1p

Reviewed the complete typed fragment `research/agents/cycles/positivity_stabilization.tex` and its exact middle-radical dependency C.1j. Both statements pass as written. They give equivalences and specified positive examples, not a proof of the universal strict-positivity assertion.

## C.1o

The projective-bundle decomposition preserves rational homological and algebraic equivalence. For a middle class written as a sum of coefficients times powers of the projective hyperplane, the displayed coefficient recursion is exact, including its first equation. The last coefficient has degree `(n-d)/2`; it determines every other coefficient, and the remaining equation is precisely multiplication by `h^(d+1)`. When `d>n`, the negative degree of that last coefficient forces all coefficients to vanish. The displayed map has coefficient one in its top projective-degree term, so it is an actual isomorphism of the indicated rational groups.

C.1j identifies that primitive Griffiths kernel with the positivity radical by the Hodge--Riemann relations. Thus the universal equivalence follows in both directions. The deduction of the injectivity part of the letter's A uses cohomological hard Lefschetz only to put the starting class in the Griffiths group; the additional power of h then invokes the proved equivalent injectivity. No surjectivity is claimed. The threefold stabilizations use only the vanishing of G^0 and G^1. Every ample class on the product has the stated form, and the distinction between a fixed variety and a universal premise is correctly retained.

## C.1p

The exact primary input was freshly opened: Beauville (2010), *The action of SL(2) on abelian varieties*, published PDF https://math.univ-cotedazur.fr/u/beauvill/pubs/SLA-rms.pdf, Theorem 4.2 and Proposition 5.2, pp. 260--261, and footnote 1, p. 254. The source allows replacement of rational equivalence by any adequate equivalence. Its finite-dimensional strings have length `g+s-2a` for a lowest vector of degree a and Beauville index s; the correspondences preserve both groups used to form the Griffiths quotient.

For a string with s at most zero, the choice `d=g-2a` is nonnegative, has the correct parity, and its `(d+1)`-st Lefschetz power vanishes. Conversely, for s at least one, the vanishing inequality is `a>r+s-1`, incompatible with `a<=r`. This proves the equivalence without a Beauville vanishing hypothesis. The cohomological eigenvalue comparison identifies all nonzero-index pieces with Griffiths pieces and identifies the grade-zero obstruction with the kernel of its cycle map. The first tests in dimensions four and five are exactly the possible lowest-vector strings; no omitted positive-index string contributes a kernel. The low-dimensional unconditional conclusion follows because the lowest degree would be at most one.

The full source was opened as `turn432859706view0`, with exact theorem passages in `turn407561423view0` and `turn407561423view1`. This review does not add a claim of priority or a closure of the remaining positivity problem.

Completed after the tool-clock reading 2026-11-19 07:45:14 UTC.
