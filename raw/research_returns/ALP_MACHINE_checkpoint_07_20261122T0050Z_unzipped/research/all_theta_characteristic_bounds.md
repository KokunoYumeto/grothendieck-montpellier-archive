# AM-R-005: a uniform bound for every nonsingular even theta characteristic

Author: GPT-6 Astra Pro, `/root`; ALP_MACHINE, 21 November 2026 UTC.
Reasoning effort is not separately exposed. This extends the one-characteristic
archimedean calculation AM-R-004 to all algebraic conjugates and to normalized
Mumford translates. It does not assert finite-place integrality of the reduced
formal frame, membership in the selected arithmetic rows, or a lift-cost sign.

## Statement

Retain the actual curve, differentials, period matrix and metric of AM-R-004:
\[
C:y^2=x^7-1,\quad E=\mathbf Q(\zeta_7),\quad
\omega_i=x^{i-1}dx/y,\quad u=Pz,\quad Y=\operatorname{Im}\tau,
\quad P Y\overline P^{\,t}=\operatorname{diag}(G_1,G_2,G_3).
\tag{A1}
\]
For a three-element subset \(S\subset\{0,\ldots,6\}\), let
\(D_S=\sum_{j\in S}W_j-\infty\), with \(W_j=(\zeta_7^j,0)\).
Let \(\delta_S=[a_S;b_S]\) be its nonsingular even half-characteristic
in this period basis, with \(a_S,b_S\in\{0,1/2\}^3\). Put
\[
F_S(u)=\exp\!\left(\frac\pi2 z^tY^{-1}z\right)
       \frac{\theta[\delta_S](z;\tau)}{\theta[\delta_S](0;\tau)}.
\tag{A2}
\]
The classification and nonsingularity of these 35 characteristics are
AM-DO-012. Their exact identification includes
\(S_0=\{1,3,5\}\), whose characteristic is zero, in ALP-LIFT-07.

For all such \(S\),
\[
\left|\frac{\theta[\delta_S](0;\tau)}{\theta[0;0](0;\tau)}\right|
   >\frac18,
\qquad
\boxed{|F_S(u)|<392\exp\!\left(\frac\pi2
                           \sum_{i=1}^3 |u_i|^2/G_i\right).}
\tag{A3}
\]
In particular \(|\theta[\delta_S](0;\tau)|>5/64\).
The constant is deliberately a simple certified uniform bound, not an optimum.
For every multi-index \(\alpha\in\mathbf N^3\), with the usual convention
for a zero component,
\[
|\partial^\alpha F_S(0)|
 \le392\,\alpha!\prod_{\alpha_i>0}
             \left(\frac{\pi e}{\alpha_iG_i}\right)^{\alpha_i/2}.
\tag{A4}
\]
The same bound holds for every normalized Mumford translate of \(F_S\),
even when the translated section vanishes at the origin. For its pullback
under \([M]\), the level-normalized derivative \(M^{-|\alpha|}\partial^\alpha\)
again satisfies (A4).

Each \(F_S\) has coefficients in \(E\). If
\(\sigma_a(\zeta_7)=\zeta_7^a\), then coefficientwise conjugation in the
rational differential coordinates satisfies
\[
                    \sigma_a(F_S)=F_{aS}.
\tag{A5}
\]
Consequently (A4) bounds every conjugate of each algebraic derivative.
For the Mumford translates, every embedding of their finite torsion field
is bounded in the same way, after the corresponding torsion translation;
the possible change of a period representative is a factor of absolute value one.

## Proof of the theta-null comparison

The only external theta-constant input is the classical first Thomae formula
in the precise form stated by Eilers (2018), Theorem 2.1, equation (2.17),
with the partition convention of equations (2.12)--(2.16). It applies to an
odd-degree hyperelliptic equation with the branch point at infinity omitted
from the Vandermonde products. Taking absolute values and a ratio removes
both its common period factor and its eighth-root-of-unity ambiguity. Thus
\[
\left|\frac{\theta[\delta_S](0)}{\theta[\delta_{S_0}](0)}\right|^4
 =\frac{\displaystyle
     \prod_{i<j\in S}|\zeta_7^i-\zeta_7^j|
     \prod_{i<j\notin S}|\zeta_7^i-\zeta_7^j|}
    {\displaystyle
     \prod_{i<j\in S_0}|\zeta_7^i-\zeta_7^j|
     \prod_{i<j\notin S_0}|\zeta_7^i-\zeta_7^j|}.
\tag{A6}
\]
Every numerator and denominator has exactly
\(\binom32+\binom42=9\) factors.

For distinct indices every factor is between \(2\sin(\pi/7)\) and 2.
The lower bound is strictly greater than \(4/5\). One elementary
verification uses \(\pi>3\), the monotonicity of sine on \([0,\pi/2]\),
and its alternating Taylor lower bound:
\[
 \sin(\pi/7)>\sin(3/7)\ge 3/7-(3/7)^3/6
                 =285/686>2/5.
\]
It follows from (A6) that its right side is greater than \((2/5)^9\).
The exact integer inequality \(2^{21}=2097152>1953125=5^9\) says
\((2/5)^9>1/8^4\). Taking the positive fourth root gives the first
inequality of (A3). AM-R-004 gives
\(|\theta[0;0](0)|>5/8\), proving the asserted absolute lower bound.

## Proof of the global growth and derivative bounds

For real half-characteristic vectors \(a,b\) and \(z=x+iy\), completing
the real quadratic form in the absolutely convergent theta series gives
\[
 e^{-\pi y^tY^{-1}y}\,|\theta[a;b](z;\tau)|
 \le\sum_{n\in\mathbf Z^3}
 e^{-\pi(n+a+Y^{-1}y)^tY(n+a+Y^{-1}y)}.
\tag{A7}
\]
The phase containing \(b\) has absolute value one. AM-R-004 proves
\(\lambda_{\min}(Y)>6/25\) and the shifted one-dimensional Gaussian
bound used there. Hence the right side of (A7) is at most
\[
                         C_0=(1+5/\sqrt6)^3.
\]
The same exact inequalities in AM-R-004 give
\(C_0/|\theta[0;0](0)|<49\). Combining this with (A6) bounds
\(C_0/|\theta[\delta_S](0)|\) by 392. Finally
\[
 \operatorname{Re}(z^tY^{-1}z)/2+y^tY^{-1}y
                         =z^tY^{-1}\overline z/2,
\]
and (A1) turns this into \(\tfrac12\sum_i|u_i|^2/G_i\).
This proves the second inequality of (A3).

Apply polydisk Cauchy with \(R_i^2=\alpha_iG_i/\pi\) when
\(\alpha_i>0\). For a zero component let its radius decrease to zero.
The resulting product is exactly (A4). No equality of actual derivative
size with this upper bound is claimed.

Let \(H(u,v)=\sum_i u_i\overline v_i/G_i\). A normalized translation by
a period-cover representative \(t\) has the analytic form
\[
 (U_tF)(u)=\varepsilon_t
       e^{-\pi H(u,t)-\pi H(t,t)/2}F(u+t),\qquad |\varepsilon_t|=1.
\tag{A8}
\]
This is Bannai--Kobayashi's normalized translation convention; its
Mumford version has the explicitly specified finite theta-group factor.
Since
\[
 H(u+t,u+t)-2\operatorname{Re}H(u,t)-H(t,t)=H(u,u),
\]
the exponential cross terms cancel exactly in the absolute-value bound.
Thus (A3) and (A4) hold for \(U_tF_S\) with the same constant. Substitution
of \(Mu\) and the chain rule prove the level-normalized assertion.
Replacing \(t\) by \(t+\lambda\), \(\lambda\in\Lambda\), changes
the normalized translate only by its semicharacter and the exponential
of a purely imaginary pairing, both of absolute value one.

## Algebraicity and the conjugation assertion

AM-DO-011 applies Bannai--Kobayashi (2010), arXiv v4 Proposition 2.1,
to these symmetric algebraic divisors, their admissible polarization,
the algebraic differential coordinates, and value 1 at the origin.
The same hypotheses hold for every \(D_S\), so
\(F_S\in E[[u_1,u_2,u_3]]\).

We justify (A5), since algebraicity alone is not a statement about the
analytic growth of conjugates. The coefficient construction in the proof
of that proposition is Galois equivariant in this situation. More
explicitly choose \(b\in2\mathcal O_E\) there so that every positive-degree
multi-index has unequal eigenvalue products for \(b\) and \(\overline b\).
The normalized periodic function
\[
 R_{S,b}(u)=F_S(\iota(b)u)/F_S(\iota(\overline b)u)
\tag{A9}
\]
is the unique rational function of value 1 at the origin with divisor
\(\iota(b)^*\Theta_S-\iota(\overline b)^*\Theta_S\).
Its Taylor coefficients are algebraic, and (A9) recursively determines
every coefficient of \(F_S\) from the earlier ones. The nonzero
coefficient multiplying the next unknown is exactly the difference of
the two displayed eigenvalue products. These facts are the proof of
the cited proposition, not a new replacement for its algebraicity theorem.

The curve and \(\omega_i\) are rational, while
\(\sigma_a\iota(b)=\iota(\sigma_ab)\) because the generating endomorphism
is \((x,y)\mapsto(\zeta_7x,y)\). Conjugation commutes with \(\sigma_a\),
and \(\sigma_aD_S=D_{aS}\). Therefore \(\sigma_aR_{S,b}\) is exactly
\(R_{aS,\sigma_ab}\), by its normalized rational divisor description.
The transformed eigenvalues are the corresponding eigenvalues of
\(\iota(\sigma_ab)\) on the same rational differentials. The recursive
equations and initial value 1 now agree; induction proves (A5).

For torsion translations use the canonical algebraic isomorphisms in
Bannai--Kobayashi Proposition 2.3 and Theorem 2.9. Formation of those
isomorphisms commutes with coefficient-field embeddings. Analytically
they are the translations (A8) by the embedded torsion point, up to
the specified finite-order factor. The period-representative observation
following (A8) removes that harmless ambiguity from absolute values.
This proves the final assertion and completes the proof. \(\square\)

## Scope for the main question and Grothendieck's frameworks

This closes the uniform archimedean normalization subgate for the 35
normalized even theta germs and their canonical algebraic torsion
translations on this fixed Jacobian. It retains the exact metric
\(G_i\), instead of substituting an arbitrary complex-coordinate norm.
Together with ALP-LIFT-06 it shows that passing to a different such
theta characteristic changes this certified bound by a fixed additive
constant, not by an order-linear metric advantage. This does not bound
the height of a general varying linear combination, the finite
denominators of its theta-group projector, or its actual vanishing and
divisibility. Those data remain in Q1 and THETA3 G1.

Geometrically the characteristic change is translation of the relative
Picard theta line by a section of its finite etale two-torsion scheme
over \(\mathbf Z[\zeta_7,1/14]\). The compatible translation
isomorphisms belong to the symmetric-line/theta-group structure and
the Poincare biextension, not to an arbitrary identification of
functions. The Hodge metrics and determinant lines are the ones in
ALP-LIFT-05; the precise FGA, cote54 and SGA7 dictionary is recorded
separately. No new claim about number-field L-function zeros or finite-field
weights follows from the uniform analytic norm bound.

## References and check provenance

- Eilers, K. (2018). Rosenhain--Thomae formulae for higher genera
  hyperelliptic curves. *Journal of Nonlinear Mathematical Physics,
  25*(1), 86--105. https://doi.org/10.1080/14029251.2018.1440744.
  Exact input: Theorem 2.1, equation (2.17), and the odd-degree partition
  convention (2.12)--(2.16). The primary article text was read at
  https://www.atlantis-press.com/journals/jnmp/125950502/view.
- Bannai, K., & Kobayashi, S. (2010). Algebraic theta functions and the
  p-adic interpolation of Eisenstein--Kronecker numbers. *Duke
  Mathematical Journal, 153*(2), 229--295.
  https://doi.org/10.1215/00127094-2010-024. Exact text used:
  arXiv:math/0610163v4, Definition 1.8, Proposition 2.1 and its proof,
  Proposition 2.3, and Theorem 2.9. No ordinary-integrality result is
  extended to a nonordinary prime here.
- AM-R-004; AM-DO-011--013; ALP-LIFT-06--07. These dependencies retain
  their separate whole-proof-check events. The elementary bound above
  is a new corollary of the cited known Thomae formula, whose proof is
  not repeated.
