# Independent check of the effective extraction bound R10--R11

Date: 2026-11-21. Checker: GPT-6 Astra Pro, inherited effort not exposed; GHOSTS /root/prime_arithmetic. Source reviewed in full: `work/root_family_bound.md`, R10 and R11. This is an independent mathematical re-proof, not a formal certificate. R12 is a separate geometric input and is not certified here.

## Verdict

R10 and R11 are correct under their stated hypotheses: an integral Eisenstein action compatible with a principal polarization on a complex abelian fourfold, an effective surface Z of theta-degree at most D0 with nonzero Weil projection, and a fixed nonzero rational Weil class t. The coarse bound

C = 531441 delta D0^4 (1+4 ceil(sqrt(T))), T=t^2,

is valid, where delta*t is integral. It bounds the multiplier and both effective numerator degrees. It is uniform for flat t when D0 is uniform. No prime-counting input is used.

## Full check

1. The commuting endomorphisms R=eta(omega)^* and S=eta(sqrt(-3))^* have the five weight eigenvalues specified in R10. Thus e_W=(9+S)(2-R-R^2)/54 is a projector onto the two Weil lines. The K action is compatible with the polarization. On H1 the Rosati involution is its Hodge adjoint; consequently the induced actions on exterior powers are normal, their joint weight spaces are orthogonal, and e_W is orthogonal for the Hodge metric.

2. In dimension four the Weil lines are primitive of type(2,2): cup product with theta introduces one sigma and one conjugate factor and vanishes on either top exterior power. The Hodge star is +1 on primitive(2,2) middle cohomology. Hence its Hodge inner product is its positive intersection form.

3. Put u=54e_W[Z]. The polynomial has integral coefficients, so u is integral. The displayed positive and negative representatives have respective weighted degree sums18D0+2*9D0=36D0 and9D0+9D0+9D0+9D0=36D0. The multiplication by sqrt(-3) has polarization similitude3 and degree81; its codimension-two flat pullback multiplies theta-degree by81/3^2=9. Unit maps preserve degree. The representative for Ru has the same bounds.

4. The polarized flat metric has total volume theta^4/4!=1. Every harmonic form is translation invariant. Therefore a unit L2 harmonic4-form has pointwise norm1. Its comass is at most1. For an effective complex surface, including singular surfaces by integration over the smooth locus with multiplicities, Wirtinger's formula gives volume(Z)=theta^2[Z]/2. If alpha is the harmonic representative of [Z], Poincare duality yields <alpha,beta>=integral_Z *beta; taking the supremum over unit beta gives ||alpha||<=D0/2. This is valid uniformly as the torus varies, even near a degeneration, because translation invariance and total volume1 are exact.

5. Orthogonality now gives d=u^2=||u||^2<=54^2 D0^2/4=729D0^2=M. Nonzero projection gives d>0. Since R is an isometry and1+R+R^2=0, the two off-diagonal pairings equal-d/2. They are integers, so d is even. Thus the Gram determinant Delta=3d^2/4 is a positive integer.

6. For p=(delta t,u), q=(delta t,Ru), both integers, Cramer's rule gives

Delta delta t = (d p+(d/2)q)u+((d/2)p+d q)Ru.

No denominator is omitted: the multiplier on t is exactly delta*Delta, and the coefficients are integral because d is even. Positive-definite Cauchy--Schwarz gives |p|,|q|<=delta sqrt(Td), and hence |a|+|b|<=3delta sqrt(T)d^(3/2).

7. Combining signed effective representatives for u,Ru gives each numerator degree at most36D0(|a|+|b|)<=108delta D0 sqrt(T)M^(3/2). The multiplier is delta*Delta<delta M^2. The numerical identities are

729^2=531441,
729^(3/2)=19683,
108*19683=2125764=4*531441.

Therefore the displayed integer C exceeds both bounds. Its extra factor1+4ceil(sqrt(T)) is deliberately coarser than the maximum of the two separate factors, and causes no problem.

8. For a flat rational section t of an integral local system, an integer delta making one fiber integral makes all fibers integral; parallel transport preserves the lattice. The pairing T=t^2 is also locally constant. Thus the extraction bound has precisely the claimed family uniformity once a uniform effective detector-degree D0 is supplied. The existence and claimed value of D0 in R12 still require the independent geometry review.

## Minor expository recommendations

- Say explicitly that the norm bound for alpha uses the star of the test form; this makes the Poincare-duality identification immediate.
- The evenness of d also follows from the Gram relation and integrality, without a separate appeal to the even exterior-power lattice.
- The theorem gives a computable upper certificate, not the least complexity. Preserve that distinction throughout the final paper.
