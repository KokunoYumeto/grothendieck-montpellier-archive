# AM-R-010: the permitted first-image family on the common E-prime host

Author: /root, GPT-6 Astra Pro, ALP_MACHINE, 21 November 2026 UTC.
This extends the actual first-image construction, not an iterated
nonvanishing or a cost computation for the full source chain.

## 1. Statement and exact finite index

Use \(E'=\mathbf Q(\zeta_{28})\), \(F'=E'^+\), \(A=J^2\),
and the exact polarization and standard splitting of AM-R-009.
Let the positive target have an even rank \(n\), and the source
be \(T'=U(1)\). Thus the underlying theta variety is
\(A^n=J^{2n}\), and its fixed vacuum period is \(C^{2n}\).
For the level parameter \(M=29^e\), \(e\ge1\), use the same
odd norm element
\[
 \alpha=(1+2\sqrt{-7})^e,\qquad \alpha\bar\alpha=M
 \tag{R10.1}
\]
as ALP-LIFT-10 and DP59, now acting on \(A\) through
\(\mathcal O_E\subset\mathcal O_{E'}\). This \(M\) is an
arithmetic level, not the number of theta lifts in DP44.

Let \(K_M'\subset K_0=(\widehat{\mathcal O}_{E'})^1\)
be principal congruence modulo \(29^e\) at all six split
places of \(F'\) over 29, and full maximal compact elsewhere.
The common finite stabilizer, finite class count, and its
prime contents are
\[
 \boxed{\quad
 h_M'=\#T'(F')\backslash T'(\mathbf A_{F',f})/K_M'
       =28^5\,29^{6(e-1)}.
 \quad}
 \tag{R10.2}
\]
In particular
\[
 v_2(h_M')=10,\quad v_7(h_M')=5,\quad
 v_{29}(h_M')=6(e-1),\quad v_\ell(h_M')=0
 \quad(\ell\notin\{2,7,29\}).
 \tag{R10.3}
\]
There is no ramified-7 index-two correction on this host.
Every permitted translated theta germ of DP59 on these ordinary
Jacobian factors, and every polynomial jet of total degree at
most \(D\), is an actual first theta image. For a single fixed
CM weight the common input has squared source norm \(h_M'\).
For a finite set \(\mathcal B\) of weights, the single input
realizing their entire direct sum has squared norm
\[
                         |\mathcal B|\,h_M'.
 \tag{R10.4}
\]
All polynomials of degree at most \(D\) require at most
\[
                         |\mathcal B|\le\binom{D+6}{6}.
 \tag{R10.5}
\]
This count concerns six total CM degrees, not the number
of matrix entries in the target.

The corresponding unit-input logarithmic norm cost is exactly
\[
 \frac12\log(h_M'|\mathcal B|)
 =3\log M+\frac52\log28-3\log29
                        +\frac12\log|\mathcal B|.
 \tag{R10.6}
\]
For \(M\) polynomially bounded in \(D\), it is \(O(\log(D+2))\).
This assertion concerns the torus input and its normalization.
The actual archimedean Fock norm, period, target mass, and
later lift costs are separate and retained.

## 2. Why the indicated subgroup fixes the actual finite family

The underlying abelian variety and trace form are the ordinary
product of the ones in ALP-LIFT-10. Its identity
\[
 U_r^{M^2H}\bigl(s(Mu)\bigr)=(U_x^H s)(Mu),
 \qquad x=Mr,
 \tag{R10.7}
\]
including the canonical finite-order lift sign, applies to
each factor and hence to their tensor product. This is the
actual equality of theta-group translations used in that
proof, not a new formal substitution for a selected theta
germ. The normalized derivative \(M^{-d}\) cancels the
factor \(M^d\) from a homogeneous derivative of degree \(d\).

The allowed half-orbit has local representatives supported
at 29 with denominators dividing \(29^e\) in one of the
two isotropic factors at each relative split place. The
same property remains true after the extension \(E'/E\):
29 splits completely in \(E'\), and the valuation of
\(\alpha\) at a selected prime is repeated at the two
primes above it. Conjugation exchanges the selected
and unselected factors. Thus the local allowed
representatives are still in a single isotropic
position lattice with denominator \(29^e\).

For \(t\equiv1\pmod{29^e}\), the displacement
\((t-1)x\) is integral in that same isotropic factor.
Its Heisenberg pairing with \(x\) is zero. At the odd
prime 29 the trace-one character on that integral
factor is one. Heisenberg covariance therefore gives
\[
 \omega_f(t)W_x\phi_{00}
       =W_{tx}\omega_f(t)\phi_{00}=W_x\phi_{00}.
 \tag{R10.8}
\]
The initial finite vacuum is fixed by the entire source
maximal compact. For target rank two this is AM-R-009,
equation (R9.27). For any even target rank, decompose its
integrally hyperbolic lattice at an odd unramified place
into orthogonal hyperbolic planes and apply the same
Pan section6.2 comparison to each plane. Every source
factor uses the opposite character 1, so their product
is one. At relative split places, including dyadic
places, the same assertion follows from AM-DO-020.
The character of the odd source affects the target
action and does not enter this calculation.

Away from 29 the permitted translation is integral,
and its Heisenberg line is the same original line
with its specified scalar. The compact source
therefore fixes it. Tensoring over entries and places
proves that \(K_M'\) fixes the entire allowed finite
Schwartz span, not only an individual chosen vector.

At each of the six places over 29 the unit quotient
has order \(28\,29^{e-1}\), so
\[
 [K_0:K_M']=(28\,29^{e-1})^6.
 \tag{R10.9}
\]
The reduction of \(\mu_{28}\) at any one such place
is injective, because 2 has order 28 modulo 29.
Hence \(K_M'\cap\mu_{28}=1\).
AM-R-009 proves \(T'(\mathbf A_f)=T'(F')K_0\).
Dividing (R10.9) by 28 gives (R10.2), and the
prime valuations give (R10.3).

## 3. One actual source input for every retained weight

Let \(\beta\) be an actual archimedean source-torus
weight occurring among the chosen creation vectors.
Define \(f_\beta\) to equal \(h_M'\beta\) on the
identity finite component of \([T']/K_M'\), and
zero on the other components. Here the component
is a copy of the full compact real torus, since
its rational stabilizer is \(K_M'\cap\mu_{28}=1\).
There is consequently no extra rational-root
restriction on \(\beta\).

The components have probability-Haar mass \(1/h_M'\).
If \(\phi_\beta\) is any allowed finite Schwartz
combination with this Fock weight, compact invariance,
commutation of the two unitary actions, and character
orthogonality give
\[
 \int_{[T']}\vartheta_{\phi_\beta}(t,g)
                    \overline{f_\beta(t)}\,dt
       =\vartheta_{\phi_\beta}(1,g),\qquad
 \|f_\beta\|_2^2=h_M'.
 \tag{R10.10}
\]
This is an equality of actual automorphic functions
for every target \(g\), with the fixed splitting
and source measure of AM-R-009.

For distinct weights \(\beta,\beta'\), the analogous
cross integral is zero by compact real character
orthogonality, and \(f_\beta,f_{\beta'}\) are
orthogonal. Set \(f_{\mathcal B}=\sum_{\beta\in\mathcal B}f_\beta\).
For \(\phi=\sum_{\beta\in\mathcal B}\phi_\beta\),
\[
 \Theta(\phi,f_{\mathcal B})(g)
      =\sum_{\beta\in\mathcal B}\vartheta_{\phi_\beta}(1,g),
 \quad
 \|f_{\mathcal B}\|_2^2=|\mathcal B|h_M',
 \quad
 \|f_{\mathcal B}\|_\infty=|\mathcal B|h_M'.
 \tag{R10.11}
\]
The supremum equality follows at the identity real torus
point, where all characters equal one. The input depends
only on the finite weight set, not on the coefficients
or chosen translates of \(\phi\).

In the six eigen-coordinates of \(A\), a degree-\(d\)
monomial has a total-degree vector in \(\mathbf N^6\)
of sum \(d\). Its source character is this vector,
with sign reversed and with the same vacuum shift.
Different vectors give distinct characters of the
full real torus. Counting all vectors of total
degree at most \(D\) proves (R10.5). A polynomial
in the original ordinary-Jacobian coordinates
has such a finite decomposition because
\(u_j=(w_j^++w_j^-)/2\) and
\(v_j=(w_j^+-w_j^-)/(2i)\).
Those transformations have only dyadic denominators;
they are integral and invertible at 11.
The decomposition is orthogonal in the actual
Fock Hermitian metric. It introduces no additional
archimedean norm beyond the norm of the original
vector, although the source input cost (R10.4)
must be retained.

## 4. What the construction transfers, and what it does not

Equations (R10.7) and (R10.10) transfer every specified
permitted jet value on the ordinary product \(J^{2n}\)
to an actual first image on the E-prime host, with
the exact period \(C^{2n}\). AM-K018 identifies its
full-\(\mathcal O_E\) source gauge with the actual
Chern gauge on those ordinary powers. The extra
\(i\)-action mixes two ordinary copies; it does not
replace a factor by the conjugate E-action. Thus
the comparison excluded for the latter product
is not used here.

For example, an already established DP59 harmonic
witness on two ordinary Jacobian factors can be
tensored with two permitted spectator sections
having unit zero-jet, as in ALP-LIFT-10 section7.
Its value on \(A^2=J^4\) and its normalized
11-adic valuation are then unchanged. Decomposing
its polynomial into the six CM weights and using
(R10.11) realizes that exact value in the actual
first image. For a single chosen weight, the
further finite-character averaging has denominator
\(h_M'\), which is an 11-adic unit. One must not
assume that an individual weight summand has the
same valuation unless its lower bound is also
proved; the exact combined value already follows
from (R10.11).

The fixed determinant repair of AM-R-009 depends
only on the vacuum shifts, not on these six
degrees. It therefore gives local bilinear
compatibility with the next positive
\(U(2)\to U(4)\) edge for every such first
image when \(n=2\). That next edge is over
the same E-prime host as AM-DO-022–024.
No scalar, finite index, or coordinate
denominator is discarded in making this
common-host statement.

The present result does not choose the next
finite Schwartz vector, compute its integral
content or norm, identify the first images
with the source's prescribed starting module,
or verify the six arithmetic row identities.
In particular (R10.6) is not the full \(e_j\)
of DP44, and the copied derivative valuation
is not automatically the determinant gain
\(g_j\). These are precise remaining
comparisons, not consequences of first-image
existence.

## 5. Framework and exact inputs

The finite part is a theta-group representation on
the section line of a Picard scheme, transported
along the actual odd isogeny and its isotropic
kernel. Its six weights are characters of the
diagonalizable CM torus, and its norm formula
uses a finite compact quotient with probability
measure. The corresponding exact framework
locators are FGA232 Theorem3.1; FGA236
Corollaries1.7 and2.3; SGA7 I VII2.7/2.9;
SGA3 I Proposition4.7.3, with the qualifications
in GROTHENDIECK_DICTIONARY.md.

The exact carried inputs are DP59 (permitted
half-orbit and zero-jet spectators), AM-K018
(ordinary-product gauge), ALP-LIFT-10 (O1–O28
and section7), AM-R-009 (R9.1–R9.27), and
AM-DO-020/022 (finite split and unramified
normalizations). Pan (2001), section6.2,
Lemma and equation(6.2.a), p197, supplies the
rank-one compact comparison used in each
hyperbolic plane. No Lean execution is claimed.
