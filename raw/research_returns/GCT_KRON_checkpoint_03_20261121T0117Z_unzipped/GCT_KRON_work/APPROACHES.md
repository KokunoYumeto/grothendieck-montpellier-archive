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
