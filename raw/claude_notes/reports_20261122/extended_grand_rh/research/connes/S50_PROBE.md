# A compact probe with an explicit conditioning bound

Checkpoint 24, AC-S50 (MR.11), extracts the multiplicity \(m_\gamma\) from the squared spectral projection of a single fixed even probe. Its proof requires the Fourier transform of that probe to be nonzero on the real axis. A different probe gives an explicit polynomial bound for the division at growing spectral height.

Take \(h(x)=e^{-x}{\bf1}_{[0,1]}(x)\), \(\widetilde h(x)=h(-x)\), \(r=e^{-1}\), and \(\phi=h*\widetilde h\). Then \(\phi\) is real, even and supported in \([-1,1]\). For \(|x|\le1\) it is \((e^{-|x|}-e^{-2+|x|})/2\). Its continuity and piecewise bounded first derivative place it in \(H^1_0(-L,L)\) for every \(L>1\). With (MR.1)'s Fourier normalization,
\[
 \widehat\phi(t)=\left|\frac{1-e^{-1-it}}{1+it}\right|^2
  =\frac{1+r^2-2r\cos t}{1+t^2}
  \ge \frac{(1-r)^2}{1+t^2}.
\]
The probe therefore has strictly positive transform everywhere, including at the origin. It can be used in the finite Weil pairings. Its elementary piecewise-exponential integrals admit the same kind of compact quadrature as S50's piecewise-polynomial probe. Its finite support preserves the cutoff in the contributing prime powers.

For \(|t|,|\gamma|\le T\), suppose a computed squared projection mass \(u\) differs from \(m_\gamma\widehat\phi(\gamma)^2\) by at most \(\eta\). Set \(C=1+2r/(1-r)^2\). From the formula above, \(|(\log\widehat\phi)'|\le C\). Thus
\[
 \left|\frac{u}{\widehat\phi(t)^2}-m_\gamma\right|
 \le \frac{(1+T^2)^2}{(1-r)^4}\,\eta
       +m_\gamma\big(e^{2C|t-\gamma|}-1\big).
\]
The first term follows by division. The second uses the bound on the logarithmic derivative to compare \(\widehat\phi(\gamma)^2\) with \(\widehat\phi(t)^2\). Whenever this upper bound and the final rational-approximation error sum to less than \(1/2\), nearest-integer rounding recovers \(m_\gamma\). For a fixed ordinate, the convergence arguments in AC-S50 provide the vanishings used here. They supply no uniform bound on \(\eta\) or \(|t-\gamma|\) as \(T\) grows.

This elementary refinement concerns the probe normalization in the unshifted arithmetic construction. It leaves the choice of finite space, the conditioning of its Gram inverse and separation of nearby eigenvalues as separate estimates. The original positive prolate trial in S48–S49 is a different vector.
