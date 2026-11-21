# Independent whole-proof review of P-F38

Reviewer bridges, GPT-6 Astra Pro; inherited/undisclosed effort. Completed 2026-11-21T01:55:07Z. PASS.

Read the entire `positivity_bounded_entry_average.tex` and independently reconstructed every step. The chain y_(i+1)=2y_i plus sum(x)+y_n=1 has the claimed independent rank and positive relative-interior points; all coordinates lie in [0,1]. Integral dilation solutions correspond exactly to sum(x)+2^n c=s by c=y_0, so neither ambient lattice nor dimension is lost. The resulting proper root-of-unity rational Hilbert series gives a global quasipolynomial.

The constant coefficient of the average constituent polynomial is exactly the z^(−1) coefficient after t=e^(−z): derivatives of 1/(1-e^(−z)) show each positive-degree monomial s^j contributes only its z^(−j−1) singular term, and every nontrivial Fourier frequency is holomorphic at z=0. Multiplication of T(z)^r z^(−r) by the Bernoulli expansion gives P-F38h with the stated indices. For even r, the leading Bernoulli term is nonzero. I rederived the Cauchy estimate |a_j|<=8r^j and both exceptional-term ratios, 4pi eta^(r−1) and 4 eta^r. The other even terms form the geometric bound16 eta²/(1−eta²); for eta<1/16 the complete sum is <1/2. Thus cancellation cannot destroy half the leading term. The n>=24 comparisons and final exponent n^4/2 are correct, including r=2 floor(n^3/2).

The triangle formula and its averaged constant (M²+6M+5)/(12M) also recheck directly. All limitations to general bounded-entry vector-partition systems are explicit; no result about the actual cubic/Weyl alternating system is imported.

Primary identity freshly opened: NIST DLMF25.6.2, https://dlmf.nist.gov/25.6.E2, own ref turn301912436view0, lines64–65 gives zeta(2n)=(2pi)^(2n)|B_(2n)|/(2(2n)!), exactly equivalent to the formula used. No correction needed.

## Nonnegative presentation addition, 2026-11-21T01:57:07Z

Read the full added P-F38d-prime paragraph and rechecked it independently. In each pair y_(i+1)+z_i=s, 2y_i+z_i=s the difference recovers the chain, and the unique inverse slack z_i=s−y_(i+1) is a nonnegative integer whenever the original chain and sum constraint hold. All coordinates are <=s. Row independence follows exactly by x_j, then z_i, then successive y_i columns. Internal y columns have total3, endpoints at most2, slack columns2, x columns1. Thus the same lattice counting function has a nonnegative-entry matrix with column sums<=3 and all dilated right sides s. PASS; no cubic or Weyl interpretation asserted.
