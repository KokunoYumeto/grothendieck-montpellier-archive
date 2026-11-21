# C25 independent whole-proof review

Reviewer: GPT-6 Astra Pro, effort inherited/not separately exposed, run THETA3/noncm_integral. Date: 2026-11-21.

**Result: PASS**, at the precise hypotheses and scope of `paper_C25.tex` read in full. This is an explicit exceptional Weil-type fourfold accessible from the arithmetic ball tower; it does not construct the projected exceptional cycle.

## Independent arithmetic

`check_C25_independent.py` uses different extension fields from the parent computation: quadratic u^2=6, cubic v^3=3, quartic w^4=6 over F109. All four exhaustive exact point counts agree: 134, 11794, 1294958, 141166026. Newton identities give the stated degree-eight Frobenius polynomial. The middle coefficient is prime to109. Gaussian quartic product, irreducibility modulo61, all thirteen power-basis determinants modulo37, and the primitive order168 computation modulo13 all pass. A separate direct repeated-squaring check confirms the two specific equations in (C25j).

`check_C25_torsion_independent.py` uses a separately written standard-library elliptic group law over F109[s]/(s^2-2). It verifies every supplied point, exact orders4,8,8,13, all Frobenius identities, all eight distinct branch x-values, and the complete degree-ten branch polynomial by multiplication. It independently counts E(F7)=6 and checks irreducibility of the Frobenius quadratic modulo13.

## Whole-proof reconstruction

Prime-to109 torsion lifts are unique in the finite etale torsion group. Their Frobenius identities preserve the full branch divisor, including the U+R pair, so its monic polynomial belongs to Q109 and its coefficient field has the claimed residue field. Squarefreeness gives an actual smooth genus-four reduction with two rational points at infinity.

The quartic over Q(i) is irreducible modulo the stated Gaussian prime. A rational minimal polynomial containing it must contain its distinct conjugate, proving degree-eight irreducibility. I reread the complete original Howe–Zhu Proposition3 and Lemma5 proof, preprint pp4–5. A first failure of Q(pi^d)=Q(pi) is excluded by the x^7 coefficient or reduces to phi(d)|8. The displayed thirteen integers are exactly that set, and every associated power basis is independent. Absolute simplicity follows, and injective specialization of geometric endomorphisms makes the generic fourfold geometrically simple too.

At13, the primitive order168 Frobenius at7 acts transitively on all nonzero E[13]. Since some nonzero13-torsion point is formal, this particular R becomes formal at a suitable place. Injectivity on E[8] preserves the other branch orbits, so the full C24 two-node proof applies at13 without modification. The resulting toric rank2 persists after finite extension.

After defining all endomorphisms over a finite extension, they act on this rank2 torus. The unital action of the geometric division algebra is faithful. Its rational character space is a nonzero module of Q-dimension2, forcing the algebra dimension to divide2. The existing Q(i) action makes the algebra exactly Q(i); integrality and the maximal order give End=Z[i]. Rosati conjugation leaves only Q, giving NS rank1. Divisor squares lie in K-eigenbidegree(2,2), whereas the two Weil lines have bidegrees(4,0) and(0,4), so their intersection is zero.

The even-level torsion transfer gives degree at most4*104^2=43264 and a surjection from the ball-cover Albanese to the Jacobian. This and the exact exceptional target are established; the nonzero exceptional projected correspondence remains separate.

Only the known typesetting typo `,qquad` was observed. The parent is inserting the exact primary locator for the standard NS/Rosati identification.
