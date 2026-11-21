# Independent whole-proof review: THETA3-C36

Reviewer: `/root/definite_bridge`, GPT-6 Astra Pro, effort inherited/not exposed.
Date: 2026-11-21 UTC.
Result: **PASS at the stated product-target scope.**

I read the entire saved `work/paper_C36.tex` and independently reconstructed its proof. I also reread the complete C12, C15–C16 source/transfer arguments; the even-level transfer paragraph of C24; the actual torsion prescription and transfer in C25; the relevant C13 projector construction; and the previously independently checked C32 cycle input. I reread Schoen's primary 2014 paper, printed p.133, including its fifth-power equations, two Fermat projections, degree-five quotient and étale double cover. This is a complete review of C36 with these named prior inputs, not a new transitive audit of every input proof.

## Common connected cover and exact bounds

The curve construction is explicit before any ball base change. The C16 normalization gives a connected étale cover D→C of degree at most dN², and Schoen's C→C0 has degree2. Every target here is a degree-two hyperelliptic cover, so D→C0 has degree at most4N². C24 proves the same local normalization for even N. Thus C25's N=104 gives e0≤4·104²=43264 and the C16 elliptic constructions give ej≤4pj². These are actual curve-cover bounds, not deductions from corresponding ball-cover bounds.

A connected component of the fibre product of the finitely many connected étale curve covers surjects onto each factor: the projection is finite étale with nonempty open-and-closed image. The nonconstant maps to H and the Fj persist. Their simple, mutually nonisogenous Jacobian targets give an injective direct sum on rational H¹, hence the asserted product quotient of J(D).

For the exact original ball degree, on y03=1 the primary equations are y01^5=1−u^5, y02^5=1−v^5, y12^5=u^5−v^5. The radicand has valuation1 along the generic diagonal of C5², so the Kummer extension has degree5. Each independent C5→C0 quotient has degree5. Therefore Y→C0² has generic degree125. Any connected component X of the étale base change by D² is proper and surjects onto Y; its image in the irreducible D² has dimension2 because the latter is finite over C0². Thus that image is all of D², and its generic degree is at most125. Pull-push on H¹ gives the asserted Albanese surjection. The degree bounds e≤∏ej and deg(X/Y)≤e² follow directly. The two independent Fj copies come from the two distinct J(D) factors.

## Eigenlines, projector and exact signs

For rho(x,y)=(−y,x), rho* u1=−u2 and rho* u2=u1, so u1+i u2 and v1+i v2 have eigenvalue i. The diagonal is the zero divisor of the difference map, giving exactly beta±=D±iE with D=omega1−omega2 and E=omega1+omega2−[Delta]. Exterior multiplication gives beta±²=0, integral beta+ beta−=−4 and integral beta±D=−2.

For b=2+i, b/bar(b)=(3+4i)/5 is not a root of unity in Q(i). Hence all degree2n eigenvalues b^r bar(b)^(2n−r) are distinct. Conjugation fixes both displayed root polynomials, so they lie in Z[t]; the Sylvester-adjugate Bezout construction gives the advertised resultant denominator. The polynomial in the actual pullback [b]* selects exactly the two all-equal embedding lines of H^{2n}, without requiring a Chow idempotent.

Expanding the product of the Dj contributes 2^(−m). Each contraction contributes −2 and each mixed elliptic self-pairing contributes −4. All relevant factor degrees are even. Consequently the contraction is (−1)^m cl(CJ), and the square is 2^(−2m)(−4)^m·73728=(−1)^m73728. Multiplying the rational projector by the stated positive resultant gives an actual integral signed cycle, with the squared denominator factor in its self-intersection. The same formulas include m=0.

## Entire Weil space exceptional

Hom(J,B)=0, including the dual formulation after polarization, because J is simple of dimension4 and the B factors are elliptic. The normalized Poincaré decomposition therefore makes NS(J×B) the direct sum of the two pullback groups. Its divisor algebra is their tensor-product algebra. Multiplication by the displayed B divisors followed by integration over B sends this algebra to the divisor algebra of J.

On the entire two-dimensional Weil space the same contraction has nonzero multipliers (−2)^m on both embedding lines, and respects rational conjugation. It is an isomorphism to the Weil space of J. C25's zero intersection with the divisor algebra therefore proves the claimed zero intersection on An. Finally b^(2n) is nonreal by the same non-root-of-unity argument, so any nonzero rational Weil vector and its [b]* pullback are independent.

The conclusion concerns the explicit product An. It does not assert that the original higher-genus C24 Jacobians are simple or have Néron–Severi rank1, and it does not identify the exceptional cycle with the image of the ball surface through a product of curves.
