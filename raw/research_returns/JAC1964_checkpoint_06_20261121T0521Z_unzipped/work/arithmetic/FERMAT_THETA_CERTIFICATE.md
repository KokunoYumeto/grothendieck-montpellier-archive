# A positive height for the nonzero complementary Fermat class

Run JAC1964-20261121. Author /root/arithmetic_sign; GPT-6 Astra Pro; effort setting not exposed. The finite-place input JAC-P10 is due to /root/programme_audit and was independently whole-read here and by /root/h9_height.

## Proposition AR-13

Let \(\eta=F_{\rm Zhang}(X_1)\) be the canonical Fourier-Ceresa class of the Fermat quartic specified in AR-8, and use the normalized raw Beilinson–Bloch height \(h_K\). Then
\[
h_K(\eta,\eta)>\frac1{100}>0.
\tag{AR.22}
\]
This class is nonzero modulo algebraic equivalence and belongs to the exact complementary Chow summand constructed in AR-8. The proposition proves the sign for this class and its rational span. It makes no dimension claim about the complementary Chow group and does not prove positivity for all its elements.

The proof below uses the known height formulas in AR-8, AR-9, AR-12 and the proved local lattice estimate JAC-P10. Its remaining analytic inequality is certified by finite theta evaluations. It uses no GRH and no height-to-\(L'\) identity.

## 1. Finite contribution, including the height normalization

Use the Hodge norm \((i/2)\int\omega\wedge\bar\omega\) throughout. For \(E:y^2=x^3-x\), the real period of \(dx/(2y)\) is
\[
\Omega_E=\int_1^\infty\frac{dx}{\sqrt{x^3-x}}
 =\frac{\Gamma(1/4)^2}{2\sqrt{2\pi}},
\]
by the Euler beta integral; its lattice is \(\Omega_E(\mathbf Z+i\mathbf Z)\). Its discriminant is \(64\). On a good-reduction model after finite extension, the invariant differential therefore differs from \(dx/(2y)\) by a factor of valuation \(1/2\), normalized by \(v(2)=1\). Hence
\[
h_E=-\log\Omega_E-\frac12\log2
   =-2\log\Gamma(1/4)+\log2+\frac12\log\pi.
\tag{AR.23}
\]
The minus sign in the finite term records that the original differential is a pole of order \(e_v/2\) in the good Hodge lattice.

JAC-P10 proves \(h_F(J)-3h_E\ge\frac14\log2\). Put
\[
c_\infty=-\frac1{18}\log\|\chi'_{18}\|_{\rm Hdg}
 =\frac{37}{18}\log2-3\log(2\pi)-\frac1{18}\log|T(\tau_F)|.
\]
Here \(\det\operatorname{Im}\tau_F=1/2\), and every complex embedding gives the same value. The primitive modular-form degree formula gives
\[
F_{18}:=\frac1{18[K:\mathbf Q]}
 \sum_{v\mid2}\operatorname{ord}_v(\chi'_{18})\log N(v)
 =h_F(J)-c_\infty
 \ge3h_E+\frac14\log2-c_\infty.
\tag{AR.24}
\]
The tree formula is \(\lambda(\Gamma_v)=2\delta_v/7\), while de Jong's bound used in AR-9 gives \(\operatorname{ord}_v(\chi'_{18})\ge6\delta_v\). Thus the entire normalized finite contribution satisfies
\[
B_{\rm fin}=F_{18}-\frac27D_2\ge\frac17F_{18}.
\tag{AR.25}
\]
The finite theta computation below gives, with outward enclosures,
\[
3h_E+\tfrac14\log2-c_\infty>0.1347786184,
\qquad B_{\rm fin}>0.0192540883.
\tag{AR.26}
\]
No integrality assertion about an isogeny height difference and no inferred node thickness is used.

## 2. An elliptic cover and the exact metrics

Use \(\tau_F\) of AR-12, and \(Y=\operatorname{Im}\tau_F\). Set
\[
T_0=
\begin{pmatrix}
-1&(-1+i)/2&(1+i)/2\\
-1&(1-i)/2&-(1+i)/2\\
0&0&-1-i
\end{pmatrix}.
\]
The columns of \(T_0\) and \(iT_0\) belong to \(\mathbf Z^3+\tau_F\mathbf Z^3\), so \(T_0\) gives an isogeny \(E_i^3\to J\). Direct exact multiplication gives
\[
T_0^*Y^{-1}T_0=2I_3,\qquad \det T_0=2,
\qquad\deg(T_0)=|\det T_0|^2/\det Y=8.
\]
For an explicit lattice check, write \(T_0=A+\tau_F B\) and \(iT_0=A'+\tau_F B'\), where
\[
A=\begin{pmatrix}-1&-1&0\\-1&1&0\\0&0&0\end{pmatrix},
\quad
B=\begin{pmatrix}0&1&0\\0&-1&0\\0&1&-1\end{pmatrix},
\quad
A'=\begin{pmatrix}0&0&-1\\0&0&1\\0&0&2\end{pmatrix},
\quad
B'=\begin{pmatrix}-1&-1&0\\-1&1&0\\0&-1&-1\end{pmatrix}.
\]
The theta divisor pulls back to a line with degree two in each elliptic coordinate. Frobenius' theta function is a section of twice the theta divisor, hence has degree four in each coordinate.

Let \(W=B^tT_0=\operatorname{diag}(0,-1+i,1+i)\). The functions
\[
h_2(u)=e^{\pi i u^tWu}\theta(T_0u,\tau_F),\qquad
h_4(u)=e^{2\pi i u^tWu}\phi(T_0u,\tau_F)
\]
are standard theta functions of degrees two and four in each elliptic coordinate, respectively. Their transformations under \(u_j\mapsto u_j+1\) and \(u_j\mapsto u_j+i\) verify this directly. The metrics are exactly
\[
\|\theta(T_0u)\|=(\det Y)^{1/4}
 e^{-2\pi|\operatorname{Im}u|^2}|h_2(u)|,\qquad
\|\phi(T_0u)\|=(\det Y)^4
 e^{-4\pi|\operatorname{Im}u|^2}|h_4(u)|.
\tag{AR.27}
\]
The identity follows by expanding the Gaussian exponent and using \(T_0^*Y^{-1}T_0=2I\). Pushforward by the isogeny preserves normalized Haar measure, so there is no extra factor eight in any mean.

## 3. A finite lower bound for the Frobenius-theta mean

Let \(g\) be the mean-zero logarithmic theta potential on \(E_i\), with a zero at the origin. Its distribution relation is
\[
\sum_{t\in E_i[n]}g(z+t)=g(nz).
\tag{AR.28}
\]
Indeed both sides have the same \(dd^c\), and both have Haar mean zero. Its maximum is
\[
M=\frac12\log2.
\]
For completeness, translating the argument does not change a maximum or mean, so for this calculation use \(\log\|\theta_3(z,i)\|-\log|\eta(i)|\), whose zero is at \((1+i)/2\). At fixed imaginary part, the triangle inequality bounds this theta norm by its value on the imaginary axis. Poisson summation bounds that Gaussian sum by its value at the origin. Its logarithmic mean is \(\log|\eta(i)|\), as follows from Jacobi's product and Jensen's circle formula. Finally \(\theta_3(0,i)/\eta(i)=\sqrt2\), using the standard theta product and \(\theta_2(i)=\theta_4(i)=2^{-1/4}\theta_3(i)\). Translating back gives the stated maximum for \(g\).

On an elliptic coordinate, the logarithmic norm of a section of degree four is a constant plus four translates of \(g\), counted with multiplicity. Equation (AR.28) therefore gives the one-sided bound
\[
\int_{E_i}\log\|s\|
\ge\frac1{n^2}\sum_{t\in E_i[n]}\log\|s(u+t)\|
       -\frac{4M}{n^2}.
\]
Iterate this inequality in all three coordinates of the elliptic cover:
\[
K:=\int_J\log\|\phi\|
\ge\frac1{n^6}\sum_{t\in E_i[n]^3}
           \log\|\phi(T_0(u_0+t))\|
       -\frac{6\log2}{n^2}.
\tag{AR.29}
\]
The chosen translated grid has certified nonzero values. Zeros of a restricted section cause no missing positive term in this lower bound.

## 4. A finite upper bound for the ordinary-theta mean

Partition the real six-dimensional torus \(E_i^3\) into \(n^6\) equal coordinate boxes \(R\). Jensen's inequality on each box gives
\[
H:=\int_J\log\|\theta\|
\le\frac1{2n^6}\sum_R
        \log\left(n^6\int_R\|\theta(T_0u)\|^2\,du\right).
\tag{AR.30}
\]
Only upper bounds on these logarithms are needed; zeros do not require excision.

For \(D=2,4\) use the normalized one-dimensional basis
\[
b_{D,r}(x+iy)=
\sum_{k\equiv r\pmod D}
 e^{-\pi(k+Dy)^2/D}e^{2\pi ikx},
\qquad 0\le r<D.
\]
Equations (AR.27) express the norms by tensors with \(2^3\) and \(4^3\) coefficients. For a rectangle \(R_x\times R_y\) on \(E_i\), the degree-two Gram entry is the absolutely convergent sum
\[
\operatorname{av}_{R_x\times R_y}
 b_{2,r}\overline{b_{2,s}}
=\sum_{\substack{k\equiv r(2)\\l\equiv s(2)}}
 e^{-\pi(k-l)^2/4}
 \operatorname{av}_{R_x}e^{2\pi i(k-l)x}
 \operatorname{av}_{R_y}e^{-4\pi(y+(k+l)/4)^2}.
\tag{AR.31}
\]
The first average is an exponential times a sinc; the second is a difference of erf values. Thus every six-dimensional cell mean in (AR.30) is a finite tensor contraction of rigorously enclosed one-dimensional integrals.

## 5. Reproducible finite certificate and truncation bounds

The calculation is in fermat_theta_certify.py, with output fermat_theta_certify.json. It uses Arb at 160-bit precision for coefficients, theta values, exponential/erf/sinc factors, and final logarithms. The tensor contractions use binary64 arithmetic with an explicit error enclosure described below.

The Frobenius coefficients first come from the one-dimensional space \(\Gamma_{00}\): in the eight second-order theta basis, impose the value and six Hessian conditions at zero. A certified invertible seven-by-seven subsystem fixes the last coefficient to one. Normalize its absolute scale using de Jong 2020, Theorem 4.1, at the two-torsion point \(z=(1/2,0,0)\): the absolute value is the product of the sixteen even thetanulls whose characteristic becomes odd after this translation. The remaining common unit phase has no effect.

The normalization value itself includes the additional tail ball \(10^{-45}\sum_p|c_p|\), independently of the coefficient intervals. This explicit tail was added following h9's implementation review; the final certificate was rerun after that correction.

The smallest eigenvalue of \(Y\) is \(1-1/\sqrt2>1/4\). Write \(q=k^tYk\). For the second-order series retain \(q\le100\); the omitted value and Hessian sums are bounded by \(10^{-45}\). One convenient bound is to split off \(e^{-0.4\pi q}\) and use
\[
\sum_{k\in\mathbf Z^3}e^{-0.1\pi k^tYk}
\le(1+\sqrt{40})^3.
\]
The Hessian weights satisfy \(|k_ik_j|\le4q\). For Frobenius evaluations at \(T_0(j/4)\), \(0\le j_i<4\), the imaginary part has squared \(Y^{-1}\)-norm at most \(9/8\). The tail is therefore bounded using
\[
-\tfrac12q+2\sqrt{9/8}\sqrt q
\le-0.1q-40+30/\sqrt2\quad(q\ge100).
\]
After multiplication by \(\pi\) and summation, this is less than \(10^{-22}\) times the largest coefficient. The script verifies that every normalized coefficient has absolute value below one and inserts the larger radius \(10^{-20}\).

For ordinary thetanulls retain \((n+a')^tY(n+a')\le50\). The same Gaussian estimate, now splitting off \(e^{-0.8\pi q}\), bounds the discarded part by less than \(10^{-45}\). The integer enumeration contains every retained term: for \(u=2n+2a'\), \(u^tYu\le200\) gives \(|u_{1,2}|\le\sqrt{300}\), \(|u_3|\le20\), using the diagonal of \(Y^{-1}\). Ordinary-theta evaluations on \(T_0(j/2)\) have imaginary squared norm at most \(1/2\); the estimate \(-q+\sqrt{2q}\le-0.2q-30\) for \(q\ge50\) bounds the tail by \((1+\sqrt{20})^3e^{-30\pi}<10^{-30}\). The product-basis coefficients are obtained by exact finite Fourier inversion from these \(D^3\) values. Their scalar divisors are convergent positive one-dimensional theta sums.

In the normalized one-dimensional bases, the script retains the indicated nine periods of Fourier indices in each direction, adding radius \(10^{-100}\). In the degree-two Gram formula it retains \(|k|,|l|\le12\), adding radius \(10^{-80}\). On \(|y|\le1/2\), the omitted one-dimensional terms are bounded by Gaussian geometric tails; these chosen radii are larger than those tails. All enumeration and phase exponents use integers or exact binary fractions.

For clarity about the finite floating calculations, let \(C\) be a coefficient tensor and \(B_j\) the three basis arrays. Arb conversion supplies complex centers and bounds on the sum of absolute real and imaginary errors. Put \(S=\sum|C|_1\), \(R_C=\sum r_C\), \(B_j=\max|B_j|_1\), and \(R_j=\max r_{B_j}\). The uniform complex error used for each contraction is
\[
R_C\prod(B_j+R_j)
 +S\left(\prod(B_j+R_j)-\prod B_j\right)
 +\gamma_{4096}S\prod B_j+2^{-1000},
\quad
\gamma_{4096}=\frac{4096\,2^{-53}}{1-4096\,2^{-53}}.
\tag{AR.32}
\]
Each contracted entry is evaluated using fewer than 4096 elementary real arithmetic operations along the expanded expression. The standard rounding-product bound gives (AR.32); the extra absolute term covers underflow. The computation has no overflow. Square, sum and square-root operations used for lower moduli are rounded outward with nextafter.

Final mean logarithms do not rely on the binary64 logarithm. Each enclosed positive input is binned using its exact binary exponent and a 12-bit dyadic mantissa, downward for lower logarithms and upward for upper logarithms. Histogram counts are exact integers; Arb evaluates the resulting integer logarithms and their weighted sum. This deliberately loses less than \(2^{-11}\) in each mean logarithm.

With \(n=16\), the certificate encloses 16,777,216 grid values and the same number of cell means. The smallest lower modulus is greater than \(5.8\cdot10^{-5}\), while the uniform tensor error is below \(9.3\cdot10^{-12}\). For the cell means the smallest upper input exceeds \(0.0057\), and the tensor error is below \(1.1\cdot10^{-11}\). The resulting one-sided bounds are
\[
\begin{aligned}
K&>-4.4783736734,\\
H&<-0.6702188747,\\
I=K-2H+\tfrac72\log2&>-0.7119207919,\\
A_\infty&>-0.0159882720.
\end{aligned}
\tag{AR.33}
\]
Combining (AR.26), (AR.33), and \(h_K(\eta,\eta)=\frac72(B_{\rm fin}+A_\infty)\) yields
\[
h_K(\eta,\eta)>0.0114303576>\frac1{100}.
\]
This proves (AR.22), subject only to the cited height formulas and the explicitly described finite arithmetic certificate. It is not a proof-assistant certificate.

## Reading and independent checks

The primary sources and exact metric locators are listed in FERMAT_THETA_GATE.md. The finite-place proof is work/programme/fermat_hodge_lattice.tex. Root and h9 independently checked the AR-12 constants. Agent h9 completed an independent whole-proof and implementation review: exact lattice/gauge identities, torsion distribution and maximum, degrees, absence of an isogeny-degree multiplier, cell Jensen, Gram/DFT phases, Gaussian tails, error propagation and dyadic logarithms passed after the explicit normalization-tail fix. The final self-contained certifier was rerun successfully. This review uses the stated IEEE binary64 arithmetic assumptions and is not a proof-assistant certificate.
