# Remaining archive and binomial gates after the checks

Agent `/root/archive_binomial`; GPT-6 Astra Pro; effort not exposed by the runtime; 2026-11-21. This is a scope assessment, not a claim that every possible further comparison is impossible.

## Restricted p-powers

There is no remaining identified proof gap in DP10. The additive vector-kernel operation is zero, the Cartier exact sequence is classical, Oda reconstructs the Hodge F,V-module from A[p], and the explicit Cech symbolic-power calculation identifies the actual restricted operation with Oda's Frobenius. Replacing that calculation by the statement that any semilinear map defines a restricted abelian Lie algebra would have been insufficient; that gap has been closed.

The follow-up about a ramified integral base did expose a concrete scope question beyond DP10. It has been addressed in `ramified_cm_scope.md`: DP19 proves the full bounds under an integral unramified CM action, while DP20 gives an actual ramified deformation where the height-only asymptotic coefficient fails. Special-fibre endomorphisms or a special-fibre summand alone do not furnish the integral action/subgroup.

## Crystals and the particular auxiliary function

The local scalar estimate does not determine a connection on a theta line bundle. This is a missing datum, rather than an omitted short lemma about the estimate. The next concrete check, once an actual line bundle and connection are specified, is to compute its integral connection matrix in the claimed frame, prove the required topological quasi-nilpotence and PD-stratification compatibilities, and check that its iterated covariant derivative is exactly the normalized theta expression. None of these choices is specified merely by a scalar lower bound.

A direct countermodel makes the distinction precise. On the trivial line over A[[t]], the flat connection `nabla=d+dt` has, after reduction to characteristic p,

`nabla_(partial_t)=partial_t+1`,

and hence `nabla_(partial_t)^p=1`, because `partial_t^p=0` on k[[t]]. Also `partial_t^[p]=0`. Its p-curvature is therefore the identity. In particular the iterates on the section 1 are all 1, so the connection is not topologically quasi-nilpotent and does not define the quasi-nilpotent crystal described by Stacks 07JH. On the very same underlying scalar function 1, every positive-order ordinary invariant derivative D^n(1) is zero, for every formal group. Thus scalar divisibility cannot distinguish this connection from a suitable one. The calculation is exact, including p=2. This does not deny that the structure sheaf with its usual connection has a crystal interpretation; it denies the inference to an unspecified theta connection.

This countermodel uses the inspected criterion in Stacks Project, Proposition 60.17.4, https://stacks.math.columbia.edu/tag/07JH . The one-dimensional connection is integrable because dt wedge dt=0; the failed condition is quasi-nilpotence.

## Binomial homotopy

There is no remaining identified proof gap in the exact statements DP11--DP14. The torsion-free Fermat criterion has a complete elementary proof; the associated-graded Hopf calculation includes its antipode; and the mapping-space assertion has the correct contravariance and uses Horel's stated hypotheses. Horel's model-category/reconstruction theorem is an existing cited input, not an unproved new claim in this report.

An automatic bridge back to the original integral formal-disc lattice is false. For example a ring map `Int(Z)->Z_p[[t]]` sending the numerical variable x to t cannot exist: preservation of `p! binom(x,p)=product_(i=0)^(p-1)(x-i)` would require a coefficient with denominator p, whereas the product on the right at x=t has linear coefficient a p-adic unit. Passing to a binomial envelope is possible as a different algebraic construction, but that envelope contains `(t^p-t)/p` and therefore has enlarged the original integral lattice. It cannot silently be identified with Z_p[[t]]. This is the same precise obstruction as DP14, not a claim excluding every possible comparison functor.

A richer comparison among formal-group distributions, crystalline structures and derived binomial cochains would require an actual functor and a theorem specifying which integral lattices and filtrations it preserves. No such functor is defined by the supplied suggestion. There is therefore no concrete missing proof to finish until that proposed comparison is specified. The unprovided cotes and B7 also cannot be converted into checkable statements by guessing their contents.

## Historical questions beyond these statements

Cote4's family monodromy/motivic questions, H8(iv)'s order-index claim and cote47's integral Chow/K-theory formula are not decided by the local estimate. Their precise later status is a separate source question. No global impossibility assertion or claim that these are all still open in the literature is made here.
