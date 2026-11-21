# R20–R24: candidate quantitative compensation through sixfolds

Root derivation, GHOSTS 21 November 2026. DRAFT, awaiting independent review.

## R20. Bounded detection in the principal Eisenstein sixfold family

Use Schoen1998 sections11–13, the dominant Prym map for unramified cyclic triple covers C→X with g(X)=4, g(C)=10. Let B=Prym dimension6, L=Theta_J|B. Complementary polarization gives type(1,1,1,3,3,3), hence L^6=6!*27=19440. KernelL=(Z/3)^6 is fixed by deck action, so choose O_K-stable maximal isotropic order27 subgroup, quotient to principal sixfold Q.

The r=0 cycles lie over |K_X|=P3 in Sym^6X. As in R12, some reduced three-dimensional component of W6(C) intersect a translate of B has nonzero Weil projection. With3Theta embedding of J dimension10,

deg W6=3^6*10!/4!=110224800;
deg B=3^6*19440=14171760;
D6=110224800*14171760/3^3.

The same support, finite symmetric-product map, nonvanishing and general Bezout proof applies. Need verify Schoen1998 actually gives dominance for the whole appropriate sixfold component, not only a different quotient family. Unimodular Eisenstein Hermitian lattice signature(3,3) is U^3 by repeated Meyer splitting and final binary determinant−1 argument. Kill determinant monodromy by degree≤6 cover.

## R21. An explicit projector and extraction bound on a principal sixfold

Let R=[omega]^*, S=[sqrt(-3)]^* on H6. On character count a (a=0,...,6), R has eigenvalue omega^(-a), S has eigenvalue -27(-1)^a. Thus

162 e_W=(27-S)(1+R+R²).

For effective3cycle Z of degree≤D6, u=162 e_W[Z] has integral signed representative with each numerator degree≤81D6. The positive primitive norm is <x,y>=-∫xy on W. Flat PPAV volume1 and complex3cycle volume degree/6 give

d=<u,u>≤162²(D6/6)²=729 D6²=:M6.

Choose alpha=2−omega, norm7. alpha³=1−18omega, alpha^6=−323−360omega, real part−143, modulus343. Let T=[alpha]^* on H6. Then u,Tu form a basis and their positive Gram matrix is

d [[1,−143],[−143,117649]], determinant97200d².

Tu has effective numerator degree≤343*81D6. For a rational Weil class tau, delta tau integral and U=<tau,tau> >0, let p=<delta tau,u>, q=<delta tau,Tu>. With Delta=97200d²,

Delta delta tau=a u+bTu,
a=d(117649p+143q), b=d(143p+q).

Cauchy gives |a|≤166698 delta sqrt(U) d^(3/2), |b|≤486 delta sqrt(U)d^(3/2). Thus one may choose

N≤97200 delta M6²,
degree numerator≤27005076 delta D6 sqrt(U) M6^(3/2).

The integer sum of the two right sides with ceil(sqrt(U)) substituted and M6^(3/2)=19683D6³ gives an explicit uniform C6(delta,U), extending from the dense Prym quotient image by the closed class loci.

## R22. Compensation for any fixed polarized fourfold Weil family

Fix an integral O_K Weil lattice of signature(2,2) with compatible polarization H, not necessarily principal; rational O_K-actions can first be made integral by a fixed isogeny of lattices. Its Hermitian determinant class is d in Q_{>0}/Norm K*. Choose a positive integer representative d (multiplying by rational squares as necessary). Put A'=E^2 with mixed K action and polarization H'=theta1+d theta2. Its Hermitian determinant class is−d, so A×A' has signature(3,3), determinant−d², equal modulo norms to−1. By the classification of rational Hermitian spaces over an imaginary quadratic field (Schoen1998 section7, referring to Deligne–Milne p50), its rational polarized Weil lattice is isometric to that of the principal sixfold component. A rational isometry can be multiplied by a fixed positive integer m to give an integral lattice map, defining an isogeny h:A×A'→Q on the associated families. Its multiplier, degree and pullback polarization are constant in the family. If h^*theta_Q=m²(H+H') under the chosen rational isometry, then deg h=m^12 (H+H')^6/6! and pulling back a codimension3 cycle scales H+H' degree by deg h/m^6. The statement uses this explicit input m; no bound in d alone is asserted.

For a rational desired class Gamma on A×A', transport it as tau=(h^*)^{-1}Gamma. Its integral denominator delta_tau and norm U_tau are computable from the rational matrix h on exterior powers and the fixed Gamma. R21 gives a bounded representative of tau, whose pullback has the same N and numerator degree at most (deg h/m^6)C6. This is uniform over the family because all lattice data are constant. Finite isogeny pullback is effective, no translation required.

## R23. Explicit contraction back to the fourfold

On A'=E^2 with mixed action put D=[Graph_1]−[F1]−[F2]. This belongs to its Weil plane, D²=−2. With R'=[omega]^* acting on A', one has D·R'D=D·(R')²D=1. Let R_A act on the fourfold Weil plane, satisfying1+R_A+R_A²=0. Define

Pi=(1+R_A tensor R'+R_A² tensor(R')²)/3,
Gamma=−Pi(t tensor D).

This is in the sixfold Weil plane: only the two equal K-character exterior lines remain. Contraction against D, namely p_A*(Gamma·p_A'^*D), equals t, since (−2t+R_A t+R_A²t)/3=−t. Its positive norm is−Gamma²=t², and 3delta_t Gamma is integral if delta_t t is integral.

Write D=D+−D− with D+=Graph1, D−=F1+F2. On E², 2(theta1+theta2)−D+ is nef (matrix [[1,1],[1,1]]) and D−=theta1+theta2≤H' in the nef ordering. Thus D+≤2H', D−≤H'. For any effective dimension3 cycle X on A×A', choose general translates of D+ and the two components of D− so intersections are proper and effective. Projection formula and nef comparison give

deg_H p_*(X·D+)≤(2/3)deg_{H+H'}X,
deg_H p_*(X·D−)≤(1/3)deg_{H+H'}X.

Indeed 3H²H' is one nonnegative summand of(H+H')³ on X. If N Gamma=X+−X− with both degrees≤C, the signed intersection expansion represents Nt with both numerator degrees≤(2/3+1/3)C=C. This contraction adds no degree cost to the bound.

## R24. Scope

This would quantitatively implement Schoen1998 Proposition10 for every fixed polarized fourfold Weil family, including arbitrary determinant type. The resulting uniform constant is explicit in a rational lattice isometry and its denominator m, the polarization degree, and the class coordinates. It is not the numeric least minimum at arbitrary family points, and does not apply to arbitrary higher-dimensional Weil families. It removes the restriction of R12 to the principal signature(2,2) family, but does not give a constant uniform over all changes of polarization/order/lattice.
