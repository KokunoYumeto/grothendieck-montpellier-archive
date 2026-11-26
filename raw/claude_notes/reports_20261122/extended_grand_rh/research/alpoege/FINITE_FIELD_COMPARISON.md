# Alpöge’s finite-field sign and the cubic prime race for 269

The published Hexagon version is **2611.00789v1**, dated 21 November 2026. Its sole source file is `deligne_sign_only_v5.tex`. I compared the public source API, the member of the public ZIP and the local file in `Documents/reports_20261120/deligne_sign_only_paper`. All three are exactly 39,107 bytes with SHA-256 `52d5e171cf7ec01d7958d1e2961dac8e018a47aabe706b5429a12376a548597f`. [Public TeX](https://hexagonmath.org/api/v1/works/2611.00789v1/source?path=deligne_sign_only_v5.tex) · [Deposit and provenance](https://hexagonmath.org/2611.00789v1)

**What carries over.** In Lemma 2 (TeX lines 193–219), positive multiplicities prevent cancellation of a pole of the generating function of traces. Proposition 4 (lines 269–308) supplies the sign by identifying the two residual terms as traces on a tensor power and the kernel of a surjective Gysin map. Lemma 3 (lines 226–250) supplies a *different* ingredient: orthogonality of an additive character makes each nondegenerate path kernel a scalar multiple of a unitary matrix. Section 7 bounds the resulting sums over every finite extension of a single base field. For the cubic number field the no-cancellation step already exists: each constituent \(L(s,\rho\otimes\chi)\) is entire, so a zero contributes its positive multiplicity in the product \(P_m\). The transform \((2^s-1)P_m'(s)/(sP_m(s))\) has positive residue at a positive real zero. The missing part is a prime-sum estimate varying the rational prime. A local weight bound controls neither the frequency nor the positions of the primes with negative trace. [Finite-field proof, Lemmas 2–3 and Proposition 4](https://hexagonmath.org/pdf/2611.00789v1) · [Analytic window theorem](https://github.com/CocoSgt/riemann-hypothesis-lean/blob/7cbf7a0c32fca1badf05931879a37c3f8a2b03b4/src/Development/AutomorphicArithmetic/DedekindLFunctions/LandauTheorems/landauWindow.lean#L83)

**The exact fixed-radicand target.** For fixed \(3\mid m\), let \(\mathcal P=\{y<p\le 2y:p\equiv1\bmod m,\ p\nmid269\}\), let \(W=\sum_{\mathcal P}\log p\), and write \(W_{\rm cube}\) for the same sum restricted to primes at which 269 is a cube. The dyadic statistic of `machine69/cubic_prime_windows.tex`, lines 23–48, is exactly \(3W_{\rm cube}-W\). The needed lower bound is \(3W_{\rm cube}\ge W-C_{m,\epsilon}y^{1/2+\epsilon}\) throughout arbitrarily late windows \(Y\le y\le Y^{1+\delta}\), with a fixed \(\delta>0\) and each \(0<\epsilon<1/2\). Dirichlet GRH already gives \(W=y/\varphi(m)+O_m(\sqrt y\log^2(2y))\). Thus it suffices to prove the lower bound \(W_{\rm cube}\ge y/(3\varphi(m))-O_{m,\epsilon}(y^{1/2+\epsilon})\) on those windows. At \(m=3\) it tests the untwisted standard representation of the splitting field of \(X^3-269\); varying \(m\) gives its Dirichlet twists. The cubic splitting condition remains in the main estimate.

**An exact analogue of Fourier orthogonality.** For \(p\equiv1\bmod3\) and any integer \(a\), put \(t_a(p)=\#\{x:x^3=a\bmod p\}-1\), and let \(e_p(v)=\exp(2\pi iv/p)\). Additive character inversion gives

\[
t_a(p)=\frac1p\sum_{h=1}^{p-1}e_p(-ha)S_p(h),\qquad
S_p(h)=\sum_{x\bmod p}e_p(hx^3).
\]

For a chosen cubic character \(\chi_p\), extended by zero at zero, \(t_a(p)=\chi_p(a)+\overline{\chi_p(a)}\). This follows directly from the three-element kernel of the cube map on the units. In particular, \(t_0=0\), and among \(a\ne0\), a third have value 2 and two-thirds have value \(-1\). Thus the sum over all \(a\bmod p\) vanishes and \(\sum_{a\bmod p}|t_a(p)|^2=2(p-1)\). Parseval gives \(\sum_{h=1}^{p-1}|S_p(h)/p|^2=2(1-1/p)\).

**What this actually proves across primes.** Write \(T_a=\sum_{p\in\mathcal P}t_a(p)\log p\). The fractions \(h/p\) occurring in the displayed Fourier expansion are pairwise distinct modulo one and spaced by at least \(1/(4y^2)\). Applying the dual additive large sieve to their coefficients gives, for every positive integer \(H\),

\[
\sum_{a=1}^{H}|T_a|^2\ \le\
2(H-1+4y^2)\sum_{p\in\mathcal P}(1-1/p)(\log p)^2
\ \ll\ (H+4y^2)y\log(2y).
\]

The last estimate uses Chebyshev’s bound. At \(H=\lfloor y^2\rfloor\), the root mean square over \(a\) is \(O(\sqrt{y\log(2y)})\). The factor with \(4y^2\) is the cost of separating the frequencies across primes. [Additive large sieve, Theorem 1, and separation of the rational frequencies](https://kskedlaya.org/18.785/largesieve2.pdf)

The cube symmetry provides a check on using this average for the prescribed integer 269. For \(1\le b\le(H/269)^{1/3}\) at \(H=\lfloor y^2\rfloor\) and \(y\) large, every \(p\in\mathcal P\) exceeds \(b\). Hence \(t_{269b^3}(p)=t_{269}(p)\) for every prime in the interval. Keeping these \(\asymp y^{2/3}\) nonnegative summands from the second moment yields only \(|T_{269}|\ll y^{7/6}\sqrt{\log(2y)}\). Even the elementary estimate \(|T_{269}|\le2W\) is stronger. As a separate test, for any finite list of such primes the Chinese remainder theorem supplies an integer \(a\) that is a noncube at every one, giving \(T_a=-W\). It can depend on the list. Neither test rules out cancellation for fixed 269. Both exhibit exactly which data are lost if the particular integer is replaced by an average.

**Checks.** Enumeration modulo \(7,13,19,31,37\) gives \(t_{269}=-1,-1,-1,-1,2\), and the sums of the squared coefficients are \(12,24,36,60,72\). For unit weights on \(7,13,19\), the exact CRT second moment over \(7\cdot13\cdot19=1729\) residues is 9432, in agreement with the sum of the three individual variances times 1729. The proofs above hold for every prime \(p\equiv1\bmod3\).
