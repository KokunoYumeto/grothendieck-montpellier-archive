# Post-CP13 research notes (not promoted)

Recorded 2026-11-20, after the 09:44 integration manifest freeze. These notes do not alter checked statements or claim movement of the requested D rows.

## The nonreduced-fibre arithmetic term

Keep the hypotheses of `D:proper-curve-arithmetic-defect` except that the radial indices may exceed one. Let `B=pi_*O_{Y'}`, let `C=Y' x_Y E`, let `C_red` be its reduction, and let `N` be the nilradical, viewed as an O_E-module. Since every generic component dominates E, the reduced finite curve is O_E-torsion-free; hence it and N are locally free over E. Write n=rank B, m=rank O_{C_red}=sum_F [k(F):k(E)], let delta_red be the normalization defect of C_red, and let D be the trace discriminant divisor. Euler characteristic gives exactly

    delta_red - deg(N)
      = sum_F (1-g(F^nu)) - m(1-g(E)) + (D.E)/2.

If s_F is the separable residue degree and Delta_F is the different divisor of the separable curve map after removing its Frobenius factor, then

    2 delta_red - 2 deg(N) + sum_F deg(Delta_F)
      = 2(g(E)-1)(m-sum_F s_F) + D.E.

Thus the reduced-fibre proof does not extend by simply replacing n with m: an upper bound for deg(N) is also needed. The discriminant identity alone does not supply it. This is a proof gate, not a counterexample.

The intrinsic normalizations of the residual curves have an upper HN bound independent of their degrees: factor a finite curve map as a separable map to a Frobenius twist of E followed by Frobenius; separable pushforward of O has maximal slope at most zero by pullback to a Galois closure, and Frobenius-pushforward estimates give a fixed upper bound. This observation controls the reduced normalization algebra, but it does not yet bound the nilradical degree or the normalization defect.

## Projective versus linear simple representations

The checked q^{C r^2} bound controls simple families with faithful defining-characteristic linear dimension O(Lie rank) and log_q |S| comparable to rank squared. It does not automatically cover PSL_n(q): its n-dimensional standard representation is projective, whereas a faithful adjoint linear representation has dimension O(n^2). Applying the checked count to that representation gives q^{O(n^4)}, insufficient for a uniform polynomial-in-|S| multiplicity bound.

A projective-representation count with q^{O(n^2)} remains a separate gate. A possible approach is rank-n twisted bundles on prime-to-p central gerbes. Neither a rank-uniform bounded atlas for all relevant gerbes nor a controlled lifting to an ordinary linear representation has been proved here. Counting obstruction classes alone does not bound the twisted representation fibres. In particular one must not assume the Brauer group of a singular normal local puncture vanishes; regular-puncture purity does not apply.

## What the uniform cover annihilator does and does not provide

The checked C lemma supplies one ideal I^3 factoring multiplication on MCM modules over every finite normal punctured cover A/R. Its relative version gives fixed jet depth over all Artinian parameters. For chosen rank-r_M and rank-r_N A-modules, intrinsic Hom jets have length proportional to t r_M r_N, where t is the cover degree.

This does not itself give an object atlas in O(t r^2) coordinates. The explicit separability element multiplies to an element of I^2, not to 1. It therefore cannot be treated as an actual separability idempotent on the Artin quotient, and no Morita-equivalence or gauge-dimension subtraction follows merely from averaging. The object-atlas count remains the unresolved part of this route.
