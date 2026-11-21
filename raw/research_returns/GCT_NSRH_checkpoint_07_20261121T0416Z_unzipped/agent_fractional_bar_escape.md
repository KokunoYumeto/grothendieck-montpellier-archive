# F55 supplement: the one-place model can also preserve the actual formal tensor bar

Author: /root/rectangular_and_theta. Date: 21 November 2026 UTC.

This note refines the actual one-place construction of F55 Part1. It retains the actual right action, ordinary identity-trace retuning and marked-X retuning, and additionally commutes with an explicitly specified extension of the actual F43 tensor bar. It still has a pole at the other collision place, fails ordinary left invariance, and fails the fixed generator-word comparisons. No assertion about VIII's prescribed globalization or an arithmetic duality is made.

## 1. Actual module and the extended bar

Use the same actual rank-64 module and regular F43 bimodule comparison as in F55 Part1. In the block basis it has 20 scalar-plus dimensions, 4 scalar-minus dimensions, 16 copies of N(delta), and 4 copies of N(D-2). The final rank-eight multiplicity space is W1^V tensor W1^W, with the actual determinant twists retained.

Every vector of this adapted basis is fixed by the actual ordinary tensor-product bar, as proved in F43 from the source's canonical tensor vectors. That bar covers the parameter involution v -> v^-1.

Let s=sqrt(2)>0, K0=Q(s), v=t², and extend the coefficient involution by

\[
 \overline t=t^{-1},\qquad \overline s=s.
 \tag{B1}
\]

This is an explicit involution of the cover and extends v -> v^-1. The extension on the algebraic constant s is a choice, stated here; no uniqueness of a bar on an unspecified algebraic coefficient field is asserted.

Keep

\[
 \Delta(v)=\frac{(D(v)-1)(D(v)-4)}{D(v)^2},\qquad
 \eta=\Delta(2)=189/625.
\]

The actual marked operator X is zero on all other sectors and Delta times the identity on the final rank-eight sector.

## 2. Bar-invariant functions

Replace the functions of F55 Part1 by

\[
 g(t)=\frac{2(1+t)^2}{t}=4+2t+2t^{-1},
 \qquad h(t)=\frac{\eta g(t)}{\Delta(t^2)},
\]
\[
 \lambda(t)=\frac{h(t)}2-2-s,\qquad
 u(t)=1+\frac{g(t)-h(t)}{20}.
 \tag{B2}
\]

All four functions are fixed by (B1), since g(t^-1)=g(t) and Delta(v^-1)=Delta(v). The exact cancellation formula is

\[
 h(t)=\frac{2\eta(t^4+1)^4}
 {t(t-1)^2(t^2+1)^2(t^8+t^4+1)}.
 \tag{B3}
\]

At the base and the selected negative collision,

\[
\begin{array}{c|cccc}
t&g(t)&h(t)&u(t)&\lambda(t)\\ \hline
s&4+3s&4+3s&1&s/2=s^{-1}\\
-1&0&-126/625&6313/6250&-1313/625-s.
\end{array}
 \tag{B4}
\]

Thus the functions are regular at t=-1 and u,lambda are nonzero there.

## 3. One bar-stable finite localization contains all extension points

Let R0 be the pullback of the same S0 from F55 Part1, with t inverted, and further invert t-1 and t²+1. As before, t^8+t^4+1 is already a unit through D(t²)-1. Define

\[
 R=R_0[u^{-1},\lambda^{-1}].
 \tag{B5}
\]

This ring is stable under the involution (B1). The inherited factors are bar invariant; t-1 goes to -(t-1)/t; t²+1 goes to (t²+1)/t²; u and lambda are bar invariant.

All inherited factors and the two added polynomial factors are nonzero at t=-1 and at t_n=s^n for n>=1. At t=-1, (B4) checks u and lambda. At n=1, u=1 and lambda=s^-1.

For all n>1, Delta(2^n)>eta by the monotonicity proved in F55 Part1. Since g(t_n)>0, h(t_n)<g(t_n), hence u(t_n)>1.

It remains to prove lambda(t_n) is nonzero for every n, without relying on a finite numerical check. Put d_n=Delta(2^n), a positive rational number.

If n is even, t_n is rational. Then h(t_n)/2-2 is rational and

\[
 \lambda(t_n)=\bigl(h(t_n)/2-2\bigr)-s\ne0.
\]

If n=2r+1 is odd, put

\[
 c_r=2^r+2^{-r-1}\in\Q.
\]

As t_n+t_n^-1=s c_r,

\[
 \lambda(t_n)
 =2\left(\frac{\eta}{d_n}-1\right)
  +s\left(\frac{\eta c_r}{d_n}-1\right).
 \tag{B6}
\]

At n=1 this is s/2. For odd n>1, d_n>eta, so the rational coefficient of 1 in (B6) is nonzero. Linear independence of 1,s over Q therefore gives lambda(t_n) nonzero. This proves every required point survives the same finite localization.

The ring also contains the inverse-parameter points t_n^-1 by bar stability and invariance of the functions. The collision order at t=-1 remains two, as v-1=(t-1)(t+1) has a simple zero there and Delta has its original order-two vanishing.

## 4. The actual bar-compatible right-module automorphism

Use the same three other blocks as in F55: scalar u on the full rank-20 epsilon-plus block, and identity on the rank-36 sum of epsilon-minus and N(delta) sectors. On the final multiplicity factor in the order (++,+-,-+,--), put

\[
 F(t)=\operatorname{diag}(1,1,s,\lambda(t))\otimes I_2.
 \tag{B7}
\]

Its full determinant is

\[
 \det F=2u^{20}\lambda^2\in R^\times.
\]

Thus it is an actual regular automorphism over R. Transport it to the original tensor module by the same regular F43 isomorphism iota, using iota^-1 F_block iota, with the rightmost map applied first. The actual named right generators are retained by this comparison.

Right-action commutation follows because the operator acts on multiplicity factors. Formal-bar commutation is equally explicit: its matrix entries are fixed by (B1), and every adapted basis vector is fixed by the actual tensor bar. Thus

\[
 \beta F=F\beta
 \tag{B8}
\]

as semilinear maps over the involutive coefficient ring R. Transport by the actual bar-compatible F43 comparison preserves this equality on the original tensor lattice.

This is a formal parameter involution, taking the fiber at t to that at t^-1. It is not claimed to be a Frobenius-equivariant isomorphism between different weight lines at one fixed arithmetic parameter, nor a construction of Verdier duality.

## 5. Both trace laws

On the marked sector the trace is

\[
 2(1+1+s+\lambda)=h.
\]

Consequently exactly as in F55,

\[
 \operatorname{Tr}(X(t^2)F(t))=\eta g(t),\qquad
 \operatorname{Tr}F(t)=56+g(t).
 \tag{B9}
\]

At the base, the marked spectrum is

\[
 1^{\,4},\quad s^{\,2},\quad (s^{-1})^{\,2},
\]

where the superscripts record multiplicities. The full base spectrum is

\[
 1^{\,60},\quad s^{\,2},\quad (s^{-1})^{\,2}.
 \tag{B10}
\]

For every n>=1, substitution t_n=s^n gives

\[
 \operatorname{Tr}(F(s)^n)
 =60+2s^n+2s^{-n}=56+g(t_n),
\]
\[
 \operatorname{Tr}(X(2)F(s)^n)
 =\eta(4+2s^n+2s^{-n})=\eta g(t_n).
 \tag{B11}
\]

Equations (B9)--(B11) prove the identity and marked trace-retuning laws for every extension degree. They use the actual operator family and actual X, together with actual formal-bar compatibility (B8).

At base q=4 under v=q^(1/2), the marked weights are 0,+1/2,-1/2. They are fractional and have different radii. No integral mixed-geometric or pure total realization is asserted.

## 6. Exact boundaries still hold

The ordinary left action still fails. At the base the vector g_- tensor g_+ has multiplicity eigenvalue s while g_+ tensor g_+ has eigenvalue1. Therefore the same actual E_V gives

\[
 (F(s)E_V-E_VF(s))(g_-\otimes g_+)
 =(1-s)(g_+\otimes g_+)\ne0.
\]

The generator trace calculation still gives

\[
 \operatorname{Tr}(P_1(v)F(t))
   =D(v)\left(36+g(t)-h(t)/2\right).
\]

At the base it is

\[
 \operatorname{Tr}(P_1(2)F(s)^n)
   =D(2)\left(38+s^n+s^{-n}\right)
   =D(2)\left(36+g(t_n)/2\right).
\]

For n>1, h(t_n)<g(t_n) and D(2^n)>D(2), so the first expression is strictly larger. The same conclusion for P_1² follows by its actual quadratic relation. There is no all-word fixed-operator retuning.

Full spectral retuning also fails without labels: the base power has eigenvalue1 of multiplicity60, while the retuned operator at n>1 has that eigenvalue with multiplicity at most42 (36 unchanged dimensions, four fixed marked dimensions, and at most two additional dimensions if lambda=1). The u and s eigenvalues cannot contribute one.

At t=+1, (B3) has a pole of order two. Hence so do u and lambda, with leading terms -h/20 and h/2. They are actual eigenvalue functions, so no finite free lattice change makes the operator regular there. The bar fixes t=+1 and t=-1 separately; it does not exchange the two places. Thus bar compatibility does not imply all-places regularity or continuity from the positive arithmetic sheet to the negative collision.

The scalar functions g and 56+g themselves are regular at both places, with g(-1)=0 and g(1)=8. Their operator-level cancellations remain exactly the exception detected by the stronger F55 Part2 argument.

## 7. Separate Grothendieck dictionary and check record

The finite coefficient cover now has a stated involution lifting the parameter-torus inversion, and the actual coherent module automorphism is equivariant for that involution and the actual tensor bar. This is additional algebraic descent/equivariance data, not a new point-Weil or geometric-duality identification. The affine coherent module and representation framework is the already audited EGA I and SGA3 dictionary; no new archive statement is needed.

The choice of lift on the algebraic cover is explicit. It is not an assertion about the unique prescribed extension or globalization asked for in VIII. The existing F43 proof supplies the actual bar-fixed adapted basis, and the present calculation supplies the compatible operator family.

The cancellations, symmetry identities, base/collision values and determinant were checked by exact symbolic arithmetic. The all-n nonvanishing proof is the rational/irrational decomposition (B6), not a finite sample. A fresh full independent review is required before integration. No previously reviewed report or fragment has been changed.

