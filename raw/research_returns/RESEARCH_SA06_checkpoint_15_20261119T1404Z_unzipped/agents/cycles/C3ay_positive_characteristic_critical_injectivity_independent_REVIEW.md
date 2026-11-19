# Independent full proof and source audit: C.3ay

**Result: PASS.** We read the complete typed draft `agents/real_weil/C3_positive_characteristic_critical_injectivity_draft.tex` and independently rederived the construction and its integral Chow identities. This review does not claim an independent rerun of the author's finite certificate.

## Exact scope

For every prime p and every r at least 2, the construction produces a specified normal excellent strictly henselian local ring of dimension 2r over the indicated algebraically closed transcendental field, with regular puncture and regular principal-divisor puncture. Its ordinary codimension-r restriction has an infinite-order kernel class. The restriction is zero integrally, including when p divides r. The statement does not concern nonzero rational ordinary classes over the algebraic closure of a finite field itself.

## Complete proof checks

1. The two displayed elliptic equations are smooth in every prime. In characteristic two their gradient is (U²,W²,V²). In odd characteristic the given separation into W=0 and V=0 verifies smoothness also in characteristic three. The geometric generic point cannot belong to any finite group scheme E[n], so its degree-zero Picard class has infinite order, without a prime-to-p restriction. The displayed diagonal line bundle is an actual proper-curve family.
2. Each horizontal line V=bW has three simple intersections with the cubic under the stated exact conditions. Distinct lines meet only at the point (1:0:0), which is outside the cubic. Their divisors are consequently disjoint. The finite-field enumeration terminates because the excluded polynomial has finitely many roots (and is the nonzero constant 4 in characteristic three).
3. For s_i=y_i ell_i, the common zero scheme consists precisely of the coordinate vertex e_i over the three points of D_i. On the indicated chart the r differential directions are independent. Hence its scheme structure is reduced, with exactly 3r points; no generic transversality assertion is needed.
4. The incidence divisor is a projective bundle off this base and is smooth on the base by the differential calculation. On it the map O^r to A kills the tautological line and induces a section of U-dual tensor A. The chart equation eliminates one of the r local parameters, leaving a regular sequence of length r-1. Its zero scheme is exactly P^(r-1) times B, of the correct codimension.
5. The integral top Chern formula is precisely the sum of (-h)^j a^(r-1-j). The twist formula has coefficient one in top degree, and c_j(U)=h^j. Pullback of the Picard class is trivial on each component of the zero scheme; projection formula therefore annihilates the entire stated Chern polynomial times lambda in integral Chow.
6. Eliminating h=-(h_y+c) in CH(E)[h,h_y]/(h^r,h_y^r) leaves h_y^r=0 and r h_y^(r-1)c=0, because c²=0 on the curve. In degree r the exact quotient is Pic(E)/Z(M^r), with no additional relation. Degree shows that Pic⁰(E) injects. The chosen source class maps to r lambda and has infinite order even when p divides r; the integer multiplier is not replaced by a scalar in the field.
7. The plane cubic full section ring, Veronese/Segre section multiplications, and full-section valuation description establish exactly the normal degree-one cone hypotheses. The local dimension is 2r. Smoothness of both punctures is the line-bundle description and the smooth incidence divisor, with no assumption about normality of the quotient at the closed point.
8. The strict-cone injection preserves the exhibited infinite order. The source class is an actual ordinary class, because the original diagonal family is pulled back and acted on by the fixed integral Chern operator before comparing its fibres. On the principal puncture, L is trivial, hence h=-a. Every term of the annihilating Chern polynomial becomes a^(r-1), and its sum is r a^(r-1). This kills exactly the chosen source class integrally. No division by r occurs.

## Primary statements freshly opened and read

- Stacks Project, Section 42.44, Tag 0FA8, Lemma 42.44.1 and its proof: regular-section zero schemes compute the top Chern class with the required multiplicities. https://stacks.math.columbia.edu/tag/0FA8 (opened ref `turn364368412view0`).
- Stacks Project, Section 42.39, Tag 02UB, Lemma 42.39.1 and its proof, especially equation 42.39.1.1: the integral twist formula. https://stacks.math.columbia.edu/tag/02UB (opened ref `turn364368412view1`).
- Stacks Project, Lemma 42.36.2, Tag 02TX, with its full injectivity/surjectivity proof: the integral projective-bundle formula. https://stacks.math.columbia.edu/tag/02TX (opened ref `turn364368412view2`).

The standard finite multiplication map on an elliptic curve and C.3e's all-characteristic strict-cone injection are previously audited antecedents; no new source reread is claimed for those two inputs. No mathematical correction remains. Together with C.3aw, this closes the negative injectivity range r+1 through 2r in every positive characteristic, with the exact coefficient-field qualification retained.

Actual completed audit receipt: 2026-11-19T11:31:19.776876+00:00
