# Certified nonvanishing of the pure-cubic Hecke L-function at two thirds

For \(E=\mathbb Q(\sqrt{-3})\) let \(\psi_{269}\) be either faithful cubic Kummer character of \(E(\sqrt[3]{269})/E\). The two choices have the same L-function because complex conjugation on \(E\) exchanges them. The following bounds are strict:

\[
2.54362759809209<L_E(2/3,\psi_{269})<2.54362759809211.
\]

The companion value satisfies \(5.40163146502760<L_E(1/3,\psi_{269})<5.40163146502764\). Both conclusions are unconditional and concern these specific real arguments.

## Completion and local factors

Put \(F=\mathbb Q(\sqrt[3]{269})\). The arithmetic \(L\)-function is \(L(s)=\zeta_F(s)/\zeta(s)\): the three-dimensional permutation representation on the cubic roots is the trivial representation plus the standard \(S_3\)-representation induced from \(\psi_{269}\). Its conductor is \(Q=217083=3\cdot269^2\). Indeed the conductor of \(\psi_{269}\) over \(E\) is the inert prime ideal \((269)\), where the extension is tamely totally ramified. At 3, \(-269\equiv1\bmod 9\) is a cube in \(\mathbb Q_3\). To see this, solve \(t+3t^2+3t^3=-30\) by Hensel and cube \(1+3t\). Negation yields a cube root of 269. Since \(E\) contains the cube roots of unity, the local extension at the prime above 3 splits. At every prime outside \(3\cdot269\) the polynomial discriminant is a unit. These facts also give \(D_F=-217083\) via the conductor–discriminant identity for the permutation representation.

The field \(F\) has signature \((1,1)\). The quotient of the two completed Dedekind zetas gives the functional equation
\[
\Lambda(s)=\Lambda(1-s),\qquad
\Lambda(s)=c^{-s}\Gamma(s)L(s),\qquad c=\frac{2\pi}{\sqrt Q}.
\]
The displayed normalization drops an inessential constant from the complex gamma factor. The completed Hecke function is entire since the inducing finite-order character is nontrivial. This sign and root discriminant do not invoke RH.

Write \(L(s)=\sum A(n)n^{-s}\) in its region of absolute convergence. The coefficients are multiplicative. For \(k\geq1\), the full local table is

| Prime \(p\) | \(A(p^k)\) |
|---|---|
| \(3\) | \(1\), from the unique norm-3 prime with trivial local value |
| \(269\) | \(0\), since the local character is ramified |
| \(p\equiv2\bmod3,\ p\ne269\) | \(1\) for even \(k\), zero for odd \(k\) |
| \(p\equiv1\bmod3,\ 269^{(p-1)/3}\equiv1\bmod p\) | \(k+1\) |
| Other \(p\equiv1\bmod3\) | \(1,-1,0\) according as \(k\bmod3=0,1,2\) |

For inert \(p\), rational Frobenius is a transposition, so its square is the identity at the degree-two prime of \(E\). For \(p\) splitting \(E\), the two cubic values are either both one or the two primitive cube roots. In the latter case the local generating series is \((1-T)/(1-T^3)\). Consequently \(|A(n)|\leq\tau(n)\leq n\). An independent exact check counts roots of \(X^3-269\) modulo each good prime up to 600: the number of roots minus one equals the code’s \(A(p)\) throughout this range.

## A finite interval proof

Let \(\Theta(t)=\sum_{n\ge1}A(n)e^{-cnt}\). Its Mellin transform is \(\Lambda(s)\); the functional equation gives \(\Theta(t)=t^{-1}\Theta(1/t)\). One can recover this inversion by shifting the inverse Mellin contour for the entire completed Hecke function, using gamma decay on vertical lines. Splitting the Mellin integral at one and setting \(s=2/3\) gives
\[
\Lambda(s)=\sum_{n\ge1}A(n)W_s(cn),\quad
W_s(x)=\frac{\Gamma(s,x)}{x^s}+\frac{\Gamma(1-s,x)}{x^{1-s}}.
\]
Here \(W_s(x)=\int_1^\infty e^{-xt}(t^{s-1}+t^{-s})\,dt\). For real \(0<s<1\), both powers of \(t\) are at most one, giving \(0<W_s(x)\leq2e^{-x}/x\). The discarded part of the *completed* value is bounded explicitly by
\[
\left|\sum_{n>N}A(n)W_s(cn)\right|
\leq \frac{2}{c}\,\frac{e^{-c(N+1)}}{1-e^{-c}} .
\]

The accompanying script builds \(A(n)\) by an integer smallest-prime-factor sieve and evaluates the finite sum with certified Arb real balls using python-flint 0.9.0. It adds the complete symmetric tail interval *before* dividing by the positive completion factor. At \(N=3000\) and 160-bit precision the completed tail is less than \(2.94\cdot10^{-14}\). The resulting completed value is within \(3.09\cdot10^{-14}\) of \(60.7946523619134\). The code checks both strict rational decimal bounds directly by interval comparison. A shorter run with \(N=1200\) and 96 bits already proves positivity. The companion value uses \(\Lambda(1/3)=\Lambda(2/3)\) and its own positive gamma factor. [Arb ball arithmetic and upper incomplete gamma](https://python-flint.readthedocs.io/en/latest/arb.html)

Run this command in the directory containing the code:

~~~text
python -I -B certify_cubic_real_value.py
~~~
