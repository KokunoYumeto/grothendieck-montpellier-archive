# Independent check of the sixfold projector and fourfold contraction

Date: 2026-11-21. Checker: GPT-6 Astra Pro, inherited effort not exposed; GHOSTS `/root/prime_arithmetic`. Entire source reviewed: `work/root_sixfold_extension.md`, especially R21 and R23, together with the root's subsequent R22 denominator/norm refinement. These are independent mathematical re-proofs. The supplementary exact-arithmetic script is `sixfold_constants.py`, with its actual output in `sixfold_constants.out`. No formal verification is claimed.

## Verdict and scope

R21 and R23 are correct. The refined isogeny denominator, norm, and degree factors in R22 are also correct. The arithmetic value of the proposed detector bound is

\[
D_6=57\,854\,793\,024\,000.
\]

Given the geometric detector hypothesis of R20, a valid integer bound on a principal sixfold is

\[
\boxed{C_6(\delta,U)
=516\,560\,652\,\delta D_6^4
\bigl(100+1029\lceil\sqrt U\rceil\bigr).}
\]

It bounds both integral effective numerator degrees and the positive multiplier. R20's source geometry and R22's rational Hermitian-lattice identification are separate review tasks; this note certifies neither merely from the numerical calculations. The estimates are upper certificates, not least-complexity calculations.

## R21a. Projector, effectivity, and the positive metric

Let the sixfold have an integral Eisenstein action with signature `(3,3)`, compatible with its principal polarization. On the character-count summand

\[
\bigwedge^aV_\sigma\otimes\bigwedge^{6-a}V_{\bar\sigma},
\]

the operators `R=[omega]^*` and `S=[sqrt(-3)]^*` have eigenvalues

\[
\omega^{-a},\qquad -27(-1)^a.
\]

Thus `1+R+R^2` keeps `a=0,3,6`, while `27-S` kills odd `a`. Their product is 162 on `a=0,6` and zero on every other summand. Consequently

\[
162e_W=(27-S)(1+R+R^2).
\]

The Weil plane is primitive of type `(3,3)`: multiplication by the polarization adds one eigenvector from each embedding and annihilates either full exterior line. The Hodge star is `-1` on this primitive middle space, so its positive metric is

\[
\langle x,y\rangle=-\int xy.
\]

Compatibility of the polarization and the Rosati involution makes the character spaces orthogonal. Therefore this spectral projector is also orthogonal for the Hodge metric.

If an effective three-cycle `Z` has degree at most `D6` and nonzero projection, put `u=162e_W[Z]`. An explicit signed integral representative is

\[
u=27(Z+RZ+R^2Z)-(SZ+SRZ+SR^2Z),
\]

where an operator on a cycle denotes its flat isogeny pullback. The unit maps preserve degree. Pullback by `sqrt(-3)` multiplies codimension-three degree on a sixfold by `3^6/3^3=27`. Each side therefore has degree at most `81D6`. In particular `u` is integral.

The flat metric has total volume one. A unit harmonic six-form is translation invariant and hence has pointwise norm one and comass at most one. Poincare duality, with the star on the test form, and the volume formula for complex three-cycles give

\[
\|[Z]\|\leq\frac{\deg Z}{3!}\leq D_6/6.
\]

It follows that the positive integer

\[
d=\langle u,u\rangle\leq162^2D_6^2/36
=729D_6^2=:M_6.
\]

This estimate uses translation invariance and fixed volume, so it does not lose uniformity when the complex structure varies.

## R21b. A second basis vector and the exact Gram matrix

Unlike the fourfold case, `R` is the identity on the sixfold Weil plane. It cannot provide a second basis vector. The replacement `alpha=2-omega` has norm seven and satisfies

\[
\alpha^3=1-18\omega,\qquad
\alpha^6=-323-360\omega.
\]

With the fixed complex embedding, the last value has real part `-143`, squared modulus `117649=343^2`, and squared imaginary part `97200`. For `T=[alpha]^*`, its eigenvalues on the Weil lines are this value and its conjugate. Since they are nonreal, `u,Tu` form a rational basis whenever `u` is a nonzero rational vector: if they were rationally dependent, a nonreal eigenvalue would have to be rational. Their positive Gram matrix is

\[
G=d\begin{pmatrix}1&-143\\-143&117649\end{pmatrix},
\qquad \det G=97200d^2.
\]

Flat pullback by `alpha` multiplies codimension-three degree by `7^3=343`. Each numerator for `Tu` therefore has degree at most `343*81D6`.

## R21c. Cramer's rule and all constants

For a rational Weil class `tau`, choose an integer `delta>0` with `delta*tau` integral, and let `U=<tau,tau>`. Set

\[
p=\langle\delta\tau,u\rangle,\quad
q=\langle\delta\tau,Tu\rangle,\quad
\Delta=97200d^2.
\]

These are integers. The inverse Gram matrix gives exactly

\[
\Delta\delta\tau=a u+bTu,
\quad a=d(117649p+143q),
\quad b=d(143p+q).
\]

There is no omitted denominator. Cauchy--Schwarz gives

\[
|p|\leq\delta\sqrt{Ud},\qquad
|q|\leq343\delta\sqrt{Ud},
\]

so

\[
|a|\leq166698\delta\sqrt U\,d^{3/2},\qquad
|b|\leq486\delta\sqrt U\,d^{3/2}.
\]

The precise arithmetic is

\[
117649+143\cdot343=166698,\quad
143+343=486,\quad
343\cdot486=166698.
\]

Combining signed representatives for `u` and `Tu` produces each numerator degree at most

\[
81D_6(|a|+343|b|)
\leq27\,005\,076\,\delta D_6\sqrt U\,M_6^{3/2}.
\]

The multiplier is `N=delta*Delta<=97200 delta M6^2`. Since

\[
729^2=531441,\qquad729^{3/2}=19683,
\]

the two coefficients after removing the common factor `delta*D6^4` are

\[
97200\cdot531441=51\,656\,065\,200,
\]
\[
27\,005\,076\cdot19683=531\,540\,910\,908.
\]

Their greatest common divisor is `516560652`, with quotients `100` and `1029`. Replacing `sqrt(U)` by its ceiling and adding the two bounds proves the displayed formula for `C6`. The proposed detector-degree arithmetic is also exact:

\[
3^6\frac{10!}{4!}=110224800,\quad
3^6\cdot6!\cdot27=14171760,
\]
\[
D_6=\frac{110224800\cdot14171760}{27}
=57854793024000.
\]

For a flat rational class in an integral local system, the denominator bound and intersection norm remain constant. Thus the extraction estimate has the claimed family uniformity once R20 supplies a uniform detector degree.

## R23a. The full rational Weil plane and the sign of contraction

Let `W_A` be the fourfold Weil plane and `W_E2` the Weil plane for the mixed action on `A'=E^2`. The divisor

\[
D=[\operatorname{Graph}_1]-[F_1]-[F_2]
\]

is in `W_E2`, with `D^2=-2` and `D*R'D=D*(R')^2D=1`. It is primitive for every diagonal polarization `H'=theta1+d theta2`: both coordinate polarizations pair trivially with this cross divisor.

Split by the two embeddings of `K`. The desired sixfold Weil lines are

\[
\bigwedge^4 V_{A,\sigma}\otimes\bigwedge^2V_{A',\sigma}
\quad\hbox{and their conjugates}.
\]

They are contained in `W_A tensor W_E2`. The two other tensor lines have opposite embedding labels. On the equal-label lines `R_A tensor R'` acts as `omega^(4+2)=1`, while on the other lines its eigenvalues are `omega` and `omega^2`. Hence

\[
\Pi=\frac{1+R_A\otimes R'+R_A^2\otimes(R')^2}{3}
\]

is precisely the projector from this four-dimensional rational tensor space onto the full two-dimensional rational sixfold Weil plane. This verifies the entire plane, not merely membership of one special class.

For

\[
\Gamma=-\Pi(t\otimes D),
\]

contraction against `D` is

\[
p_{A*}(\Gamma\,p_{A'}^*D)
=-\frac{-2t+R_At+R_A^2t}{3}=t,
\]

because `t+R_At+R_A^2t=0`. Consequently the map `t->Gamma` is injective. Domain and target both have rational dimension two, so its image is the full sixfold Weil plane and contraction is its inverse.

## R23b. Primitive product normalization and norm

Each summand `R_A^i t tensor (R')^iD` is primitive for `H+H'`, since its cup product with each of `H` and `H'` vanishes. Thus `Gamma` is Lefschetz primitive of type `(3,3)`. This use of the word primitive is distinct from being a primitive vector in an integral lattice.

Write `T=t^2>0`. In the square of the orbit average, the three diagonal pairings are `T*(-2)` and the six off-diagonal pairings are `(-T/2)*1`. The total is

\[
\Gamma^2=\frac{3(-2T)+6(-T/2)}9=-T,
\qquad \langle\Gamma,\Gamma\rangle=T.
\]

No extra factor of two, three, or factorial is present. Also `3 delta_t Gamma` is integral whenever `delta_t t` is integral.

For the explicit product class `t_star`, the supplementary exterior calculation checks all these identities in a twelve-generator integral exterior algebra. It obtains `t_star^2=24`, `D^2=-2`, `Gamma^2=-24`, and exact contraction to `t_star`. Its denominator is exactly three, and `3Gamma` has coefficient gcd two. Thus `delta_t=1`, but a valid and in fact least integral denominator for this `Gamma` is three. The original class `t_star` is twice a primitive integral class, as previously recorded.

## R23c. Effectivity and degree under contraction

Write `D=Dplus-Dminus`, where `Dplus` is the diagonal graph and `Dminus=F1+F2`. The divisor-class matrices show

\[
2(\theta_1+\theta_2)-D^+\text{ is nef},\qquad
D^-=\theta_1+\theta_2.
\]

For `d>=1`, this implies `Dplus<=2H'` and `Dminus<=H'` in the nef ordering. Translate the graph and coordinate fibers generically so they intersect any given finite collection of effective three-cycles properly. Their classes are unchanged, and their intersections and proper pushforwards are effective integral cycles.

For an effective three-cycle `X`, expansion of `(H+H')^3` has nonnegative terms and includes `3H^2H'`. Projection formula therefore gives

\[
\deg_H p_{A*}(X\,D^+)\leq\frac23\deg_{H+H'}X,
\qquad
\deg_H p_{A*}(X\,D^-)\leq\frac13\deg_{H+H'}X.
\]

These are upper bounds on integer degrees; no divisibility assumption is needed. If `N Gamma=Xplus-Xminus` and each degree is at most `C`, the positive numerator after expansion is the sum of `Xplus*Dplus` and `Xminus*Dminus`, and its degree is at most `(2/3+1/3)C=C`. The negative numerator obeys the same bound. The multiplier stays `N`. Thus contraction has no additional degree cost in this normalization.

## R22 refinement: transport denominator, norm, and final bound

Suppose a lattice isogeny `h:A x A' -> Q` has degree `e` and satisfies

\[
h^*\theta_Q=m^2(H+H').
\]

On rational cohomology, `h^*` is invertible, with inverse `h_*/e`. Hence

\[
\tau=(h^*)^{-1}\Gamma=h_*\Gamma/e,
\qquad \delta_\tau=3\delta_t e
\]

is a valid integral denominator. Pushforward preserves integral cohomology classes, so `3delta_t e tau=3delta_t h_*Gamma` is integral. This is a sufficient denominator and need not be the least one.

The top-degree projection formula gives

\[
\Gamma^2=e\tau^2,\qquad U_\tau=T/e.
\]

Flat pullback of an effective codimension-three cycle multiplies degree by

\[
F=\frac{e}{m^6}.
\]

The degree of the isogeny is

\[
e=m^{12}\chi(H+H'),
\]

so `F=m^6 chi(H+H')` is a positive integer and at least one. Consequently it bounds the multiplier as well as the numerator degrees after pullback. Combining the extraction, pullback, and contraction proves the proposed valid bound

\[
\boxed{C_4=\frac e{m^6}
C_6\left(3\delta_t e,\frac Te\right).}
\]

If the separate lattice argument identifies `d=chi(H)` and uses `H'=theta1+d theta2`, then `chi(H+H')=chi(H)chi(H')=d^2`, so `e=m^12 d^2` and `F=m^6 d^2`. This last substitution is conditional here on that separate lattice identification, rather than an additional theorem claimed from the norm calculation.

All quantities in this formula are fixed lattice and flat-class data. None is determined by ordinary versus supersingular prime type, and no part of this large upper bound computes a least complexity at a general family point.
