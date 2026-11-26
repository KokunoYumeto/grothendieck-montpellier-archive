# An ideal-divisor criterion for the cubic Kummer character at 269

Let \(E=\mathbb Q(\omega)\), \(\omega=e^{2\pi i/3}\). Let \(\psi\) be either faithful cubic character of \(E(\sqrt[3]{269})/E\), interpreted as a finite-order Hecke character of \(E\). Write \(\eta(\mathfrak a)=\chi_{-4}(N\mathfrak a)\) on odd integral ideals. The prime \(\mathfrak l=(3+\omega)\) has norm \(9-3+1=7\) and \(\eta(\mathfrak l)=-1\). Let \(S\) consist of all prime ideals above \(2,3,7,269\). Each summation variable \(\mathfrak a\) below is a nonzero integral ideal coprime to \(S\). Divisor counts on an auxiliary ideal such as \(\mathfrak l^2\mathfrak a\) include the factors above 7.

For every ideal divisor \(\mathfrak d\mid\mathfrak c\) of an odd ideal, make two distinguishable tags carrying signs \(\eta(\mathfrak d)\) and \(\eta(\mathfrak c)\eta(\mathfrak d)\). Define \(W(\mathfrak c)\) as the number of ordered pairs of tags with opposite signs. For \(j=0,2\) form the smooth sums
\[
 B_j(X;w)=\sum_{\substack{\mathfrak a\perp S\\\eta(\mathfrak a)=1}}
    \psi(\mathfrak a)W(\mathfrak l^j\mathfrak a)\,w(N\mathfrak a/X).
\]
The twist and the norm in the test function both use the base ideal \(\mathfrak a\).

**Theorem.** RH for the single Hecke function \(L_E(s,\psi^2)\) is equivalent to
\[
 |B_0(X;w)|+|B_2(X;w)|\ll_{w,\epsilon} X^{1/4+\epsilon}
 \quad(X\ge1)
 \tag{1}
\]
for every \(\epsilon>0\) and every smooth test function compactly supported in \((1,2)\). A single explicitly specified nonnegative dyadic test function also suffices. The two sums can alternatively be replaced by the single unrestricted-base-ideal sum in (5). The two faithful choices of \(\psi\) yield the same Hecke \(L\)-function, since conjugation of the ideals exchanges the characters. This criterion tests a named nonabelian degree-two Artin factor over \(\mathbb Q\) through its degree-one Hecke realization over \(E\).

## Two exact products

Put \(t(\mathfrak c)=\sum_{\mathfrak d\mid\mathfrak c}1\) and \(b(\mathfrak c)=\sum_{\mathfrak d\mid\mathfrak c}\eta(\mathfrak d)\). The total number of tags is \(2t\). Their signed sum is \((1+\eta(\mathfrak c))b\). If there are \(n_+\) and \(n_-\) tags of the respective signs, \(W=2n_+n_-=\big((n_++n_-)^2-(n_+-n_-)^2\big)/2\). When \(\eta(\mathfrak a)=1\), this gives
\[
 W(\mathfrak a)=2t(\mathfrak a)^2-2b(\mathfrak a)^2,\qquad
 W(\mathfrak l^2\mathfrak a)=18t(\mathfrak a)^2-2b(\mathfrak a)^2.
\]
Indeed \(t(\mathfrak l^2)=3\) and \(b(\mathfrak l^2)=1-1+1=1\). If \(\eta(\mathfrak a)=-1\), some prime with negative \(\eta\) occurs to an odd exponent, so multiplicativity gives \(b(\mathfrak a)=0\).

Write
\[
 P(s)=L_E^{(S)}(s,\psi),\qquad Q(s)=L_E^{(S)}(s,\psi\eta),\qquad
 Z(s)=L_E^{(S)}(2s,\psi^2).
\]
Here the superscript deletes the Euler factors over \(S\). At a good prime ideal \(\mathfrak p\) use \(x=\psi(\mathfrak p)(N\mathfrak p)^{-s}\). The local series for \(\psi t^2\) is \((1-x^2)/(1-x)^4\), by summing \((k+1)^2x^k\). Twisting by \(\eta\) gives the same formula with \(x\) replaced by \(\eta(\mathfrak p)x\). The local series for \(\psi b^2\) is
\[
 \frac{1-x^2}{(1-x)^2(1-\eta(\mathfrak p)x)^2}.
\]
For positive \(\eta(\mathfrak p)\) its coefficients are again \((k+1)^2\). For negative \(\eta(\mathfrak p)\) it is \(1/(1-x^2)\), exactly the even exponents. Absolute convergence on \(\Re s>1\) now yields \(P^4/Z,Q^4/Z,P^2Q^2/Z\) for the three respective global series. Projecting \(t^2\) with \((1+\eta)/2\) and using the support of \(b^2\), the series \(D_j(s)\) of the weights in \(B_j\) are
\[
 D_0(s)=\frac{(P^2-Q^2)^2}{Z},\qquad
 D_2(s)=\frac{9(P^4+Q^4)-2P^2Q^2}{Z}.
 \tag{2}
\]
These identities give meromorphic continuations. The numerator factors \(P,Q\) are entire, since each inducing character is nontrivial. Every local inverse Euler factor deleted from a finite-order Hecke \(L\)-function is nonzero on \(\Re s>0\).

## Holomorphy and the zero iteration

Write \(\widehat w(s)=\int_0^\infty w(t)t^{s-1}\,dt\). For \(\Re s>1\), substitution and absolute convergence give
\[
 \int_0^\infty B_j(X;w)X^{-s-1}\,dX=\widehat w(s)D_j(s).
 \tag{3}
\]
The integrand vanishes for \(X\le 1/2\). Under (1) its Mellin integral is holomorphic on \(\Re s>1/4\), using an exponent \(\epsilon<\Re s-1/4\) on compact subsets. For any prospective pole \(s_0\), a nonnegative bump supported sufficiently close to any point of \((1,2)\) has \(\widehat w(s_0)\ne0\), since the integrand's phase then ranges in an open semicircle. Thus both quotients in (2) are holomorphic throughout that half-plane.

Suppose \(L_E(s,\psi^2)\) has a zero \(\rho\) with \(1/2<\Re\rho<1\). The denominator in (2) vanishes at \(\rho/2\). Holomorphy forces both numerators to vanish there. The first gives \(P^2=Q^2\); with this substitution the second is \(16P^4\). Hence \(P(\rho/2)=0\). Local factors and gamma factors are nonzero at this point, so the primitive Hecke functional equation for \(\psi\) gives
\[
 L_E(1-\rho/2,\bar\psi)=0,\qquad \bar\psi=\psi^2.
 \tag{4}
\]
The map \(T(\rho)=1-\rho/2\) preserves the open right half of the critical strip and \(T^k(\rho)=2/3+(-1/2)^k(\rho-2/3)\). For \(\rho\ne2/3\) the distinct zeros thus accumulate at an interior point of an entire function nonzero on \(\Re s>1\), a contradiction. For the one remaining point, the certified interval is \(2.54362759809209<L_E(2/3,\psi^2)<2.54362759809211\). The companion calculation gives the completion, every bad Euler factor, and a finite interval proof. This excludes the fixed point and completes the converse by the functional equation, with conjugation symmetry (also \(L_E(s,\psi)=L_E(s,\psi^2)\)). [Real-value certificate](CUBIC_REAL_VALUE.md) · [Reproducible Arb calculation](certify_cubic_real_value.py) · [Tate, *Fourier Analysis in Number Fields and Hecke’s Zeta-Functions*](https://books.google.com/books/about/Fourier_Analysis_in_Number_Fields_and_He.html?id=FjZFywAACAAJ)

Conversely, under this single RH, \(1/Z(s)\) is holomorphic and polynomially bounded on every closed strip \(1/4+\delta\le\Re s\le2\). For the bound, start with the usual fixed-conductor polynomial vertical bounds for the Hecke function and take a holomorphic logarithm of its primitive value on a disk centered at \(2+it\) with left edge \(1/2+\delta\). At its center the Euler-product logarithm is bounded. Borel–Carathéodory on the concentric smaller disk gives \(|\log L_E(\sigma+it,\psi^2)|\ll_\delta\log(3+|t|)\) for \(1/2+2\delta\le\sigma\le2\); the Euler product suffices further right. The finitely many deleted factors and their reciprocals are bounded on these strips. The entire numerator factors have the same standard polynomial vertical upper bounds, without any RH assumption for \(Q\). Mellin inversion and the rapid vertical decay of \(\widehat w\) allow a shift to \(\Re s=1/4+\delta\) without residues. This proves (1).

## One auxiliary prime and one test function

For every base ideal, \(b(\mathfrak l\mathfrak a)=0\) and \(t(\mathfrak l\mathfrak a)=2t(\mathfrak a)\). Thus both signs of the base ideal give \(W(\mathfrak l\mathfrak a)=8t(\mathfrak a)^2\). The single signed census
\[
 B_*(X;w)=\sum_{\mathfrak a\perp S}
    \psi(\mathfrak a) W(\mathfrak l\mathfrak a)\,w(N\mathfrak a/X)
 \quad\text{has series}\quad 8P^4/Z .
 \tag{5}
\]
Holomorphy at a denominator zero now gives \(P(\rho/2)=0\) immediately. The same forward estimate and (4) therefore give the full equivalence for \(|B_*|\ll_{w,\epsilon}X^{1/4+\epsilon}\). There is also a version in which the marked ideal always has positive sign. Use \(\mathfrak l\mathfrak a\) when \(\eta(\mathfrak a)=-1\) and \(\mathfrak l\bar{\mathfrak l}\mathfrak a=(7)\mathfrak a\) when \(\eta(\mathfrak a)=1\). The two primes above 7 are distinct. Their individual alternating divisor sums vanish, so the tag counts in these two cases are \(8t(\mathfrak a)^2\) and \(32t(\mathfrak a)^2\). Giving the second case the scalar weight \(1/4\) recovers (5) exactly.

For an explicit single test in \(C_c^\infty((1,2))\), let \(L=\log 2\), \(\ell_k=L/2^{k+1}\), \(k\ge1\), and take independent uniform random variables \(U_k\) on \([0,\ell_k]\). Let \(g\) be the density of \(L/4+\sum_k U_k\), supported on \([L/4,3L/4]\). It is smooth because the first \(r\) uniform factors give Fourier decay \(O_r((1+|t|)^{-r})\) for every \(r\), while every subsequent factor has modulus at most one on the Fourier axis. Put \(w(x)=g(\log x)\). Its Mellin transform is
\[
 \widehat w(s)=e^{Ls/4}\prod_{k\ge1}\frac{e^{\ell_k s}-1}{\ell_k s}.
\]
Each factor is nonzero for \(\Re s>0\), and on compact sets the sum of the absolute deviations of the tail factors from 1 converges because \(\sum_k\ell_k<\infty\). Hence the product has no zero on \(\Re s>0\), so (3) for this single \(w\) detects every possible pole. This applies to either (1) or (5).

Direct enumeration on all 6,662 eligible ideals of norm at most 30,000 compares the ordered pairs of tags with the local Euler coefficients for (2) and with both forms of (5). All six combinations of norm sign and cubic-character value occur. [Exact coefficient checker](check_ideal_shell.py)

The tags use the norm sign of **ideal divisors**. A term ranges over the full eligible ideal semigroup, with prime powers and composites included. The criterion supplies no estimate for a prime-restricted census and no pointwise assertion about rational Erdős–Straus decompositions.
