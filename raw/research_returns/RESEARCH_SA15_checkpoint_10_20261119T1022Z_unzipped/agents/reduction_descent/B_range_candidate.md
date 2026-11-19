> SUPERSEDED: the tame construction and all-n criterion have now been fully proved and independently audited; see B_ranges.tex and B_higher_tame.tex. This file records earlier exploration only.

# Sharp elliptic torsion range: candidate proof under audit

2026-11-19 03:31 UTC. NOT YET A CERTIFIED THEOREM. Necessity is proved below; sufficiency has an equivariant monomial-arc gate requiring audit. This file is an intermediate research note, not a substitute for unresolved B.2/B.3.

Fix p≥5, n≥1, defect m>1. Potential ordinary reduction is excluded by B-RD3. Therefore special reduction is supersingular and m∈{2,3,4,6}, m|(p+1). Extend the base unramified to algebraically closed residue and let L/K be the tame degree-m good-reduction extension. Normalize v_L. Average a good formal parameter under tame inertia to get an exact eigenparameter. For every K-rational torsion point its nonzero parameter has valuation congruent to a fixed q modulo m, gcd(q,m)=1.

Let B be the least valuation of a primitive p^n-torsion point, and let A be the greatest such valuation. There is a basis X,Y of E[p^n] with valuations A,B: if A>B, a minimal-valuation Y cannot lie in the mod-p line of X, because p-divisible multiples have valuation strictly greater than B. If A=B any basis works. Thus A≥B≥1 and A≡B≡q modm.

For a height2 formal group the least p^n valuation is b1/p^(2n−2), where b1 is the least p-torsion valuation. This follows by the Newton polygon of [p](T)−z for a least-valuation p^{n−1} point z; its roots all have valuation v(z)/p². Consequently v([p^j]Y)=p^(2j)B, 0≤j≤n−1.

The power series [p^n](T)/[p^{n−1}](T) has constant term p and distinguished degree p^(2n)−p^(2n−2). Its roots are exactly primitive p^n-torsion points. Thus e(L)=sum of their valuations. Quotient primitive vectors by units (Z/p^n)^×. The projective lines consist of p^n vectors (a,1), of valuation B, and the vectors (1,b) with b divisible by p, including b=0 of valuation A. For v_p(b)=j, the valuation is min(A,p^(2j)B); equality cannot cancel because X was chosen maximal among primitive points. There are (p−1)p^(n−j−1) such b. Hence necessarily

m e = p^(n−1)(p−1) [ A+p^n B + Σ_{j=1}^{n−1}(p−1)p^(n−j−1)min(A,p^(2j)B) ].

In particular e≥(p²−1)p^(2n−2)/m. At n1 this reads e=(p−1)(A+pB)/m. Since A,B≡q modm, it implies (p−1)|e and e≥(p²−1)/m.

## Proposed sufficiency

Choose a supersingular elliptic curve C/k having an automorphism α of orderm. For m3/6 choose j0 (p≡−1mod3); for m4 choose j1728(p≡−1mod4); for m2 any supersingular curve. Let R_n be its universal deformation ring with full Drinfeld p^n-level structure. Carter–Strauch2021 Theorem2.1.2 and Proposition2.2.3(i) give a complete regular local ring of dimension2 with parameters x,y the universal basis coordinates.

The framing action of α preserves the labelled level structure and gives semilinear descent on the universal elliptic family. Tame averaging chooses an eigen formal coordinate t with α(t)=ζ^q t. Thus x,y are exact scalar eigenparameters. The Cohen presentation is R_n=W(k)[[x,y]]/(F), with F=p−f(x,y), and may be chosen μ_m-invariant by averaging its generator. Substitute x=π^A,y=cπ^B for a generic Teichmuller c∈W(k)×. The resulting W(k)[[π]]/(F(π^A,cπ^B)) is a complete DVR: F has constant p times a unit and its modp substitution is nonzero, whose weighted leading term is nonzero for generic c. The induced action π↦ζπ has orderm and fixes the defining equation because A≡B≡q modm. Its invariant DVR is K with e(L/K)=m.

The universal elliptic curve algebraizes over this DVR (Serre–Tate plus canonical degree3 line bundle at zero), and descends over L/K. The labelled torsion is fixed by descent, so it is K-rational. Its special inertia action is α, hence defect exactlym. For genericc, no equality between valuations of x and [p^j]y produces cancellation, so A is maximal and B minimal among primitive points, and the displayed formula gives the resulting ramification.

### Audit gate

Need check precisely (i) averaging the formal coordinate simultaneously with semilinear action on the universal deformation and labelled level; (ii) invariant Cohen presentation constant p coefficient; (iii) genericc excludes every needed equality cancellation after substitution, including higher-order p-dependent terms; (iv) the no-cancellation assertion really produces exactly desired A,B, rather than only minimumB. These are plausible finite conditions but must be fully justified before upgrading sufficiency.

For n1 the gate is much simpler: primitive coordinates have linear leading forms ax+by, and only A=B requires excluding finitely many c∈Fp. Choosing B=1 and A=1+m(e/(p−1)−(p+1)/m) would give every e≥(p²−1)/m divisiblep−1. The same tame construction atp3 permits m4 for every positiveevene, and m2 for evene≥4. Wild m3,6,12 still need separate analysis.

## Fixed cyclotomic field

Over K=Qp(ζp), p≥5, e=p−1 and residueFp. An additive elliptic curve has no p-primary component-group part (component order≤4), and E0/E1≅(Fp,+). Its additive formal group has no nonzero p-torsion at e≤p−1: coefficients of [p](T) of degrees2,...,p−1 are p-divisible and all nonlinear coefficients are in the maximal ideal because special formal group is additive. For v(T)≥1, pT uniquely has minimum valuation. Thus E(K)[p] embeds inFp and has rank≤1. This excludes fullp. Atp3 the componentgroup canhave3torsion and B-RD2 givesfull3. Need write primary citation for componentgroup bound and formal coefficient fact, or provide an elementary proof.
