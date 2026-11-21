# A47 independent whole-proof review

Reviewer: GPT-6 Astra Pro; effort not exposed; AN_GRH/gt_certificates.  
Date: 2026-11-21.  
Source: work/row_audit/A47_BOUNDED_PRIMITIVE_EXPONENT.tex.  
Whole-read final SHA256: 6fe00a4573c5df1288d66c1809116db4f97ffe96e1ba876c2b8df9df525b7aba.

## Verdict

PASS. I read the entire final statement, all five proof steps, the elliptic-configuration explanation, and the exact remaining-witness discussion. No mathematical correction was requested. This is an independent same-model whole-proof reading, not a separate reconstruction, numerical replay, or formal proof verification.

## Detailed checks

The actual integral primitive projector p_n is defined over the given field even when the deck group is nonconstant. From A p_n=n A and the p-unit n, the rational primitive exponent M_n kills A delta without enlarging constants. The exact order m of A delta is a p-power dividing M_n. The principal divisor m A(Q'-P') has degree 2^omega(n) m and coefficients exactly plus or minus m on disjoint free orbits. Exact order excludes a pth power, so the resulting map is separable.

Poonen's controlled-field consequence applies to the finite list of degree-d conjugate functions over the perfect algebraic closure. The numerical hypothesis rules out index one. The index e divides 2^s p^b and is coprime to n. The kernel of the cyclic action has order dividing both e and n; a point stabilizer would partition a fibre divisor into equal-weight orbits of an odd-prime length dividing n, which would divide e. Thus the action is faithful and free. The genus bound and unramified quotient formula force both intermediate and quotient curves to have genus one.

For identical image orbits I checked the shift in the literal group-ring coefficients. With v(P')=sigma^j v(Q'), the two equations are m A=r_Q H and -m A=r_P sigma^(-j) H. They imply r_Q A=-r_P A sigma^(-j). Iterating an odd number equal to the order of sigma^j yields (r_Q^t+r_P^t)A=0 in a torsion-free integral group ring. This is impossible. No equality of ramification indices, reduced-fibre assumption, or characteristic-two sign reduction is used.

For disjoint image orbits, a zero or pole fibre contains only points of the displayed divisor and at most one from either original orbit. Disjointness leaves one point, hence total ramification e. Its coefficient m gives e|m|M_n. The identity coefficient of A is one, so P' and Q' themselves are in the support; equivariance yields two full ramified n-orbits. Since e is a nontrivial p-power, the leading derivative vanishes and the local different exponent is at least e. The total different 2n(g-1) gives p<=e<=g-1, as claimed.

For descent, the subgroup of Gal(K/K^G) fixing F K^G is the kernel of its faithful action on F, so K=F K^G. Degree comparison gives [K^G:F^G]=e, and separability follows from K/F and F/F^G. The tensor product defining C x_E Z has dimension n over K^G and has compositum K of that same degree, so it is a field; this justifies the connected fibre product rather than merely a chosen component. Etale base change preserves ramification at P and Q. The stated elliptic obstruction is therefore on the original base curve.

The final explanatory configuration is consistent: fixed-point-free automorphisms of a genus-one curve are translations, so the projector kills a degree-zero class on that curve; total ramification pulls the principal divisor back with the positive factor e. The text correctly refrains from asserting an actual section collision in that configuration. The threshold comparison with the whole-Prym exponent and the precise open supply gate are correct. Constant extension cannot decrease the rational torsion exponent.

Poonen's Proposition 2.1 statement and complete Lemma 2.2/Corollary 2.3 proofs were directly reread during the preceding A46 check. The local-different input was checked in the A45 review. This event does not claim a new external primary reread or an arithmetic execution for A47.
