# R30–R31: an explicit finite-prime gate from the cited Dirichlet GRH

Root derivation, GHOSTS, 21 November2026. Draft pending independent check.

Let b be a positive integer. Under Dirichlet GRH, for either a=1 or2 there is a prime p≡a mod3 with p not dividing b and

p ≤ X(b):=max(exp(14), 4 log b+4).

Proof. Lee2023 arXiv2301.13457v2, Corollary1.1 (theta inequality, printedp2) and Table1 rowlogx0=10 give, forx≥exp10,

|theta(x;3,a)−x/2| < (logx/(8π)+log3/(2π)+9.29179) sqrt(x)logx−8311.79.

Drop the negative constant. With y=logx≥14, π>3 andlog3<1.1 bound the relative error by

F(y)=(y/24+9.5)y exp(−y/2).

F is strictly decreasing fory≥4, since its derivative has sign (y/12+9.5)−(y²/48+4.75y)<0 there. At14,
F(14)=(14/24+9.5)*14/exp7 <1/4.

For a rational elementary bound: exp7>(1+1+1/2+1/6+1/24)^7=(65/24)^7>1000, while4*(14/24+9.5)*14<565; hence strict. Thus theta(x;3,a)>x/4 forx≥exp14. If every prime inthatclass≤X divided b, their product woulddivide b andtheta(X;3,a)≤logb. Buttheta>X/4≥logb+1, contradiction.

R31. For B04's polarized arithmetic model and degree D, enlarge its exceptional integer b_D to a positive integer b containing the excluded rational residue characteristics. If at least one place over each prime p≡a mod3,p≤X(b),p good supports an integral numerator pair ofdegrees≤D for some multiplierN_p, then the globalclassis algebraic. In fact it is enough to produce such certificates for a finite setP ofdistinct rationalprimes with sumlogp>logb: then somep doesnotdivide b; B04 lifts its particular pair withits ownN unchanged. No independent denominator bound isneeded. For the Eisenstein product isogenyclass, a1and2 correspond respectivelytoordinaryandsupersingular reduction. For the fullWeilfamily, they areonlycongruenceclasses andnoNewtonclaimis inferred.

This gives a finite explicit search range once b_D is computed. It does not supply the local degreeD, compute b_D for unspecifiedA, or convert an estimate D(p) growing withp into a uniformdegreebound. It is a strictly finite form oftheprimegate withthemissing geometricinput keptvisible.

Source: Ethan Simpson Lee, The prime number theorem for primes in arithmetic progressions at large values, arXiv2301.13457v2, Cor1.1 andTable1, printedp2. Rootread originalPDF inequalities/table andderivative above. The citedGRHinput is Alpoge suppliedMain.lean Dirichlet declarations, nottheconditionalHeckeinput.
