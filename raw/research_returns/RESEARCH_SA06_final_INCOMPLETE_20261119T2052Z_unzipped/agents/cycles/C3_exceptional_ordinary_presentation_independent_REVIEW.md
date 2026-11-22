# Independent review of the exceptional ordinary presentation

**Reviewer:** `/root/cycles`. **Completed:** 2026-11-19 16:56:59 UTC.
I read all of `agents/real_weil/C3_exceptional_ordinary_presentation_draft.tex`
(EP.1–EP.4) after completing the full endpoint-lifting audit.

**PASS under the exact displayed hypotheses:** an algebraizable excellent
henselian local coefficient-field ring of dimension three in positive
characteristic, a regular projective modification with SNC reduced
exceptional divisor, and an effective full-support exceptional Cartier
divisor with ample conormal.  This is a comparison theorem, not a
calculation of the intrinsic perfect-family subgroup for every SNC
surface.

1. The point restriction isomorphism from the already audited FF argument
   is compatible with lambda and Adams operations.  On a projective
   surface, the integral vanishing of the third gamma filtration and
   the distinct rational eigenvalues 1, 2, 4 identify the second gamma
   filtration with the weight-two part.  The projector written in the
   proof is correct: `(psi^2-1)(psi^2-2)/6` takes the values 0, 0, 1.

2. Nilpotent invariance after inverting the characteristic gives an
   actual lambda-ring isomorphism on rational perfect K_0 of `D x P`
   and `E x P`.  The inverse preserves the rational gamma filtration.
   Clearing denominators and using the universal special lambda-ring
   identities is sufficient; no nonsmooth cycle-class comparison is
   hidden in this step.

3. For an exceptional perfect-family relation, EL supplies a class on
   the fixed `Z x P` with the correct two endpoint restrictions.  The
   point restriction isomorphism forces those endpoint classes to have
   weight two.  Taking the second Chern-character component therefore
   gives exactly the prescribed ordinary relation.  The proof does not
   claim that the original perfect family lifts at every parameter point
   or that the negative K group of the parameter product vanishes.

4. In the converse direction, the inverse rational Chern character on
   a single smooth finite-type model supplies a pure weight-two perfect
   class for the cycle family.  Its pullback belongs to the second gamma
   filtration, so restriction yields one of the stated exceptional
   relations.  All finite data descend together to one pointed etale
   model.  Shrinking around the proper exceptional fibre gives a regular
   model, which is smooth over the perfect coefficient field.

5. Closing finitely many horizontal cycles over a projective
   compactification of a parameter curve preserves the chosen refined
   fibres.  Likewise, closing an actual family from `X x P` in `Z x P`
   proves that the image of the ordinary subgroup on `Z` is the whole
   ordinary subgroup on `X`.  Thus quotienting Chow localization gives
   exactly EP.4, with the actual exceptional embedding retained in
   theta.

I freshly opened and read Weibel, *The K-book*, Chapter II,
Corollary 8.9.1 and its proof, author p. 84, at
<https://sites.math.rutgers.edu/~weibel/Kbook/Kbook.II.pdf>.
The session reference is `turn272074632view0`.  The exact gamma dimension
and Adams inputs on pp. 83 and 32 were freshly opened in the immediately
preceding EL audit.  The KST/Drinfeld and nilpotent-comparison inputs are
reused from the already audited FF/EL proofs; this receipt does not claim
new primary openings of them.  No finite program was run for EP.

The scope paragraph correctly preserves the remaining issue: separately
constructed double-curve families may have nonzero restrictions at triple
points.  They need not glue to a perfect family on `E x P`.  EL removes
the ambient endpoint-lifting obstruction after such a family exists; it
does not remove these intrinsic gluing conditions.
