# Approaches and gates

## Work in progress

1. Read all supplied archive transcriptions; separate tentative, deleted and uncertain text from mathematical assertions.
2. Test the proposed positive Burnside lambda operations by subgroup fixed-point marks.
3. Use linearization and the Young permutation basis to express Kronecker coefficients by exact orbit counts followed by integer basis inversion.
4. Seek positive quotients/kernel spaces and exact two-row/hook/rectangular generating series.
5. Compare support holes with GCT VI corrected saturation and with actual GCT candidate support.
6. Translate the operations into K0, group schemes, Schur functors and invariant schemes with integral-base-change hypotheses.

## Projection approach: successful refinements

- Direct monomial cycles gave determinant size 1+(m-1)binom(m+r-1,r-1).
- A sorted-prefix tree with shared padding tails improved this to binom(m+r-2,r-1)+m-1. This was independently checked but is superseded in the paper.
- Balanced prefix and suffix trees give size binom(m+p,p)+binom(m+q,q)-1 with p+q=r-1. Negative labels on all variable edges cancel the cycle-cover signs. This is the version proved in M007.
- Projection containment, rather than full ambient containment, is sufficient to compare actual multiplicities: M006. Thus four-row ambient equations do not contradict the stronger GCT row exclusions M008.
- The next unresolved step is permanent-specific containment or a quantitative comparison in higher-row multiplicity spaces. Dimension rules out extending the universal-all-forms projection construction past 2c+1 fixed rows at n=m^c; it does not rule out permanent-specific constructions.

## Further successful reductions

- Shape-sensitive highest-weight truncation: align padding by upper Borel, discard coefficients exceeding the tail weight box, and use bounded versions of the two trees. This is M009 and goes beyond the dimension barrier for universal full-form containment.
- Permanent-specific subset-lattice determinant: known Grenet bound2^m−1 gives a finite-m gate independent of row bounds.
- Evaluation rank: lambda operations determine ambient wreath invariants, but actual multiplicities are ranks of form-specific evaluation maps, F010. A smaller parameter space alone gives no rank inequality.
- Hessian highest-weight family: Cauchy computes scalar ambient multiplicity; explicit nondegenerate Hessians prove the relevant form-specific evaluations. Written proof in progress.

## Degree and stabilization approaches

- Known quadratic Foulkes–Howe stabilization (2026 Proposition3), after full written-proof review, gives no Chow equations in degree d when n>=d(d−1). Diagonal determinants transfer this to the actual determinant closure: M010.
- Keeping the GL type through the differential induction gives the second-row bound A020; an adaptive exponent refinement is being checked.
- Cauchy flag minors prove all-copy stabilization at base inner degree lambda2: F014. Combined with degree-balanced determinant tries O012 and the correct differential padding pullback, this rules out bounded second row in all outer degrees.
- Restricting the base coefficient space to the highest-weight box may improve the latter construction further; proof and graph count are being written separately and independently checked.

## 2026-11-21T02:44:03.864163+00:00 — actual obstructions and the boundary gate

The Hessian-bracket route succeeded at n=m, with exact ambient1, permanent1 and determinant0; subtracting a determinant square reduces its ordinary coefficient to a one-corner hook zero. Its stretch gives a positive ordinary coefficient from factor2 onward, but no stretched closure value has been established.

For the LMR degree12 shape, direct highest-weight linear algebra would require over one million monomials in its weight space. That route was rejected as unnecessarily large. The coefficient-projection route instead proved a49-dimensional permanent image dominant via a completely specified integer minor, yielding q6>K5. Endpoint projection witnesses extend fullq=a to m3–6 and length2m+2. An arbitrary-size endpoint proof remains an active attempt.

The fixed-entry version preserves six copies under internal padding. O027 simultaneously proves the determinant retains its full ambient multiplicity for the shifted shape at every n>=4. This attempted transfer of the small obstruction therefore fails for a proved reason.

Investigating the stretched Hessian example led to precise boundary-localization and support-saturation statements M020. The known support theorem gives a finite uniform stretching reduction, not all-large-stretch positivity. Boundary denominator clearing restores all orbit copies under full-rectangle translations; those translations leave internally padded permanent support whenm<n. Neither route settles the original large-padding positive-rank comparison.

## 2026-11-21T03:19:25.943520+00:00 — successful polynomial-algebra route

The stretched closure gate is now completely resolved for the Hessian ray by A034. Instead of clearing boundary denominators through an unknown invariant degree, multiply every binary core copy by the actual nonzero Hessian coefficient H0. This reaches the exact ordinary upper bound at every stretch. On the permanent side, fix the all-ones matrix with11entry3−n, where H=0 butP!=0. Diagonal perturbations give a triangular, nonzero-Jacobian map to all remaining binary coefficients. Centered coefficient polynomials remain algebraically independent on that hypersurface. Prime-factor valuations separate the additional bracket generator from every Hessian-times-core monomial, producing a polynomial subalgebra and strict multiplicity gaps at every stretch, for every unpadded size.

The arbitrary-size permanent transverse2-jet endpoint remains open. A032 proves the diagonal binary base fails at both r2m+1 andr2m+2 even after all binary tangent directions are allowed. F027 proves any isolated binary vertex also fails at those counts. Nonisolated block and cycle bases are being tested; finite m3–6 dominance is proved, not extrapolated.

## 2026-11-21T03:39:39.765562+00:00 — partial-Hessian transfer and residue endpoint

A035 closes the basic partial-Hessian transfer: everyproperr hasK=a1. Forr<=2n the entire binary/partial-Hessian coefficient algebra survives onDet, so that construction cannot supplya paddedadvantage among itsowncopies. A further proper-partial polynomial-algebra construction is beingwritten; itisnotyetrootchecked.

Thepermanentendpoint nowhas a preciseconditionalresiduetensor atbinarybasetJ+diag(a_i). Firstjetkernel hasdimensionm(m−1), andatR2m−1 the quadraticdifferentialissquare. Genericnonzeroa_i sparseorientedtwo-channellabels givefinitefullranksm3–6; settinga_m0 leavesonecokerneldirectionincheckedcases. Thefirst-order perturbationnecessarilyvanishes; second-order Schurcomplement isrequired. Exactpair/triangleidentities andfinitealternateembeddingtestsare saved undercomputations/root_residue_*. Naturalrow-columnlabelsfailwithdeficitbinom(m,2); scaledorientedlabelsworkinthesamefinitecases. Noneoftheseexperimentsprovesarbitrary-sizeinvertibility.

## Proper partial Hessians and the explicit permanent endpoint tensor

A035 proves K=a=1 on every basic proper partial Hessian weight; A036 proves algebraic independence of all constructed positive-ray generators on every proper determinant partial ray. Therefore the full-Hessian obstruction mechanism does not transfer through that constructed algebra under internal padding. This does not prove the entire proper-ray multiplicity. QA033-RJ replaces an unspecified Hessian-tuple problem by an exact directed-edge residue tensor for tJ+diag(a). O031 solves the pure-skew quadratic block for all m, but leaves the coupled symmetric/mixed blocks. Finite full ranks are kept separate from the missing arbitrary-size proof.
