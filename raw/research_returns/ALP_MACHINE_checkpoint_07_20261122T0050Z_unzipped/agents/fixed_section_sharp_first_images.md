# ALP-LIFT-13 — fixed finite first-image witnesses at 3 and 5

Author: /root/lift_accounting, GPT-6 Astra Pro, ALP_MACHINE,
21 November 2026 UTC.

This specializes the already constructed actual first theta
correspondence to AM-K020's sharp derivatives of one fixed
theta section. It does not reprove those derivative
congruences. Unlike the general permitted-orbit projector,
this untranslated specialization uses one unit-norm
automorphic character and one fixed finite Schwartz vector.

## 1. Actual vector and its exact coefficient

Retain \(E=\mathbf Q(\zeta_7)\), \(F=E^+\),
the actual compact pair \(T=U(1)\), \(G=U(I_2)\), and the
honest splitting of ALP-LIFT-09. Write
\[
 a_{i,n}=\partial_i^n\sigma_q(0),\qquad
 C=\theta[0;0](0;\tau)c .
 \tag{F1}
\]
The normalization of \(\sigma_q\) is the actual algebraic
Chern/source gauge established in AM-K014/K018 and
ALP-LIFT-08:
\(\sigma_q(u)=u_1u_3-u_2^2+\text{higher terms}\).
The global period \(C\) is retained.

On two ordinary Jacobian factors use the creation polynomial
\[
       P_{i,n}=\partial_{i,1}^{\,n}
                         \partial_{1,2}\partial_{3,2}.
 \tag{F2}
\]
The finite Schwartz vector is the same
\(\phi_{0,f}^{\otimes2}\) for every \(i,n\). Its finite
\(L^2\) norm is one. Let \(\phi_{i,n}\) have this finite
part and the actual Fock creation vector corresponding
to (F2). ALP-LIFT-09's exact Bargmann reading gives
\[
 \vartheta_{\phi_{i,n}}(1,1)
   =C^2\,P_{i,n}\bigl(\sigma_q(u_1)\sigma_q(u_2)\bigr)_{0}
   =C^2a_{i,n}.
 \tag{F3}
\]
Indeed the second factor contributes exactly
\(\partial_1\partial_3\sigma_q(0)=1\).
It is necessary to include this spectator derivative:
an undifferentiated second trace-one section vanishes
at the origin and would give zero.

The polynomial has one fixed multidegree across CM
embeddings: its degree vector is
\((n+1,0,1)\) if \(i=1\), and \((1,n,1)\) if \(i=2\).
Thus it is one torus weight, including the actual
vacuum shift, despite using two different eigenlines
on the spectator factor.

## 2. One actual source character, without a growing finite level

Let \(\beta_{i,n}\) be that actual infinity torus
character, and let \(\lambda_f\) be the character on
the fixed finite vacuum line. ALP-LIFT-09 proves
\[
 T(\mathbf A_{F,f})=T(F)K_0,\qquad
 T(F)\cap K_0=\mu_{14}.
 \tag{F4}
\]
For every \(a_{i,n}\ne0\), rational invariance of the
actual nonzero sum (F3) gives
\[
           \beta_{i,n}(\zeta)\lambda_f(\zeta)=1
                         \quad(\zeta\in\mu_{14}).
 \tag{F5}
\]
This is a consequence of the actual theta sum; no
compatibility is assumed from a hypothetical lift.

Consequently
\[
 \chi_{i,n}(\delta\,t_\infty k)
        =\beta_{i,n}(t_\infty)\lambda_f(k),
 \quad\delta\in T(F),\quad k\in K_0,
 \tag{F6}
\]
defines a unitary automorphic character. Independence
of the decomposition follows from (F5). The finite
compact character is fixed as \(n\) varies. In the
standard splitting its only nontrivial compact factor
is the orientation character \(\epsilon\) at7, by
AM-DO-020–021; the proof using the actual
\(\lambda_f\) does not require this optional explicit
description.

Normalize the compact torus quotient to volume one.
The equality of actual automorphic functions is
\[
 \Theta(\phi_{i,n},\chi_{i,n})(g)
       =\int_{[T]}\vartheta_{\phi_{i,n}}(g,t)
                                 \overline{\chi_{i,n}(t)}\,dt
       =\vartheta_{\phi_{i,n}}(g,1).
 \tag{F7}
\]
It follows because the theta function transforms by
\(\beta_{i,n}\lambda_f\), the group actions commute,
and (F4) represents every finite component. Hence
\[
 \|\chi_{i,n}\|_2=\|\chi_{i,n}\|_\infty=1,\qquad
 C^{-2}\Theta(\phi_{i,n},\chi_{i,n})(1)=a_{i,n}.
 \tag{F8}
\]
There is no finite Fourier projector and no factor
\(h_M^{\pm1/2}\) in (F7)–(F8).
The algebraic normalized value in (F8) is what will
be assigned a \(p\)-adic valuation. No \(p\)-adic
valuation is assigned to the unnormalized complex
period \(C^2\).

As a direct root-unit check, in the fixed Hom convention
\(X\mapsto Xt^{-1}\), the source vacuum shift is \(-1\)
at each CM place. Therefore the exponent of
\(\beta_{i,n}\) on \(\zeta_7\) is \(-in-10\).
Both witness sequences below have \(in\equiv4\bmod7\).
Their \(n\) are even, so \(\beta_{i,n}(-1)=-1\),
matching the finite orientation value
\(\lambda_f(-1)=-1\). This also verifies (F5)
explicitly for these sequences using the corrected
AM-DO-023 source shift. Formula (F5) remains the
coordinate-independent proof.

## 3. Exact sharp actual first values

AM-K020, jacobian_sharp_small_prime_directions.md,
equations (K21.1)–(K21.1a), supplies the nonzero
derivatives
\[
 n_3(r)=28\cdot3^r+18,\qquad
 n_5(r)=126\cdot5^r+30
 \tag{F9}
\]
and their exact valuations. Substitution into (F8)
gives the following actual first-image coefficients:
\[
 \begin{split}
 v_3\!\left(C^{-2}
       \Theta(\phi_{1,n_3(r)},\chi_{1,n_3(r)})(1)\right)
   &=\frac{3^r+3-s_3(n_3(r))}{2},\\
 v_5\!\left(C^{-2}
       \Theta(\phi_{2,n_5(r)},\chi_{2,n_5(r)})(1)\right)
   &=\frac{5^r-1}{4}.
 \end{split}
 \tag{F10}
\]
The new assertion in (F10) is their occurrence as
these specified actual theta-lift values. The numerical
derivative theorem itself belongs to AM-K020.

In particular the same first-image family, with fixed
finite vacuum and unit-norm source character, has
\[
 \liminf_{n\to\infty}
   \frac{v_3(C^{-2}\Theta(\phi_{1,n},\chi_{1,n})(1))}{n}
       =\frac1{56},\qquad
 \liminf_{n\to\infty}
   \frac{v_5(C^{-2}\Theta(\phi_{2,n},\chi_{2,n})(1))}{n}
       =\frac1{504},
 \tag{F11}
\]
where the family is indexed by the nonzero coefficients;
zero coefficients may be included with valuation \(+\infty\).
For a zero coefficient not satisfying (F5), no extra
character is being asserted by the definition of this
family. The global lower bounds and the witness
subsequences in AM-K020 give both directions of (F11).
Replacing the denominator \(n\) by the actual total
creation degree \(n+2\) leaves these limits unchanged.

At every fixed permitted level \(M=29^e\), take the
untranslated section \(s_M=[M]^*s_q\) on each factor.
ALP-LIFT-10, (O6)–(O11), gives exactly
\[
 M^{-(n+2)}P_{i,n}
       \bigl(\sigma_q(Mu_1)\sigma_q(Mu_2)\bigr)_{0}
                         =a_{i,n}.
 \tag{F12}
\]
The point \(t'=0\) is in the permitted half-orbit and
its finite phase is1, so the finite vector in that
identity is the unchanged \(\phi_{0,f}^{\otimes2}\).
The level can be fixed once and for all; no
interpolation condition \(M\asymp n\) is required for
these particular actual rows.

## 4. Costs that have and have not been determined

The source input in (F7) has norm one and the finite
Schwartz norm is one. The exact archimedean Schwartz
norm is not one. ALP-LIFT-09, (V23), gives
\[
 \|\phi_{i,n,\infty}\|_2^2
   =\det(2Y)^{-1}\,
           n!\left(\frac{\pi}{G_i}\right)^n
                    \frac{\pi^2}{G_1G_3}.
 \tag{F13}
\]
The two spectator creation operators lie in distinct
orthogonal modes and have factorial1. The first
factor contributes \(n!\); the two ordinary Gaussian
vacua contribute \(\det(2Y)^{-1}\). Thus
\[
 \log\|\phi_{i,n,\infty}\|_2
   =\frac12\log(n!)
      +\frac n2\log\frac{\pi}{G_i}
      -\frac12\log\det(2Y)
      +\log\pi-\frac12\log(G_1G_3).
 \tag{F14}
\]
Equations (F13)–(F14), the actual period \(C^2\),
and the change in infinity coefficient weight must
remain in any comparison of globally normalized
rows. A constant finite input cost is not a
zero total DP44 cost.

ALP-LIFT-11's fixed bilinear determinant repair
preserves all values in (F8) at the identity and
all scalar automorphic norms. ALP-LIFT-12 then
shows that each repaired nonzero first vector
survives some actual \(U(2)\to U(4)\) theta
kernel. That theorem does not preserve the exact
valuations (F10) at the second output.

The selected later harmonic row, its integral
lattice, and the source DP44 gain and error fields
therefore remain separate. This result supplies
actual fixed-finite first rows on ordinary \(J^2\);
it does not identify a DP65 conjugated-action
product with those ordinary factors.

## Dependencies and checks

AM-K020, equations(K21.1)–(K21.1a), is the exact
new derivative input; it is cited rather than
reproved here. ALP-LIFT-09, (V16), (V22)–(V32),
provides the actual oscillator, period and
class-one character calculation. ALP-LIFT-10,
(O6)–(O12), provides the exact permitted pullback
normalization. AM-DO-020–021 supplies the optional
explicit compact character and corrected DO023
the source vacuum shift. AM-K018 supplies the
ordinary-power source-gauge identification.

This specialization is a complete proof from
those inputs. Whole-proof checks are recorded
separately with their actual scope; no Lean
execution or second-output saturation is claimed.
