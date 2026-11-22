# AM-R-009: an actual nonzero first lift on the common unramified mixed-CM host

Author: /root, GPT-6 Astra Pro, ALP_MACHINE, 21 November 2026 UTC.
This proof constructs the first image on the same field and polarized
abelian variety as AM-DO-022–024. It does not identify the rank-one
starting edge with the source's prescribed even-rank arithmetic chain.
The finite compact-vacuum assertion in section 3 has been checked
against Pan (2001), section 6.2, including the rank-one source case.
The source input has norm one with the specified probability Haar measure.

## 1. The precise host, period, and eigen-coordinate

Use the accepted DP57 host, as normalized in AM-DO-022:
\[
 E'=\mathbf Q(\zeta_{28})=\mathbf Q(\zeta_7,i),\qquad
 F'=E'^{+},\qquad A=J^2,\qquad \xi'=\xi/2.
 \tag{R9.1}
\]
The action of \(i\) on the two ordinary \(J\) factors is
\((u,v)\mapsto(-v,u)\). The trace form with coefficient \(\xi'\)
is exactly the product principal polarization, with no isogeny
or change to the underlying four Jacobian factors used below.
Put
\[
 w_j^+=u_j+iv_j,\qquad w_j^-=u_j-iv_j,\qquad
 s_A(u,v)=\sigma_q(u)\sigma_q(v),\qquad C=\theta_0c.
 \tag{R9.2}
\]
All symbols \(\sigma_q,\theta_0,c\), and \(G_j\) retain their
normalizations in AM-R-004–006. In particular
\(\sigma_q(u)=u_1u_3-u_2^2+\) terms of degree greater than two,
and the actual Bargmann theta realization of the original finite
vacuum is \(C\sigma_q\).

Since \(\zeta_{28}=\zeta_7^2i^{-1}\), its eigenvalue on \(w_j^+\)
has label \(8j-7\bmod28\), while its label on \(w_j^-\) is
\(8j+7\bmod28\). Thus
\[
 \Phi'=\{1,3,9,15,17,23\},\qquad w_2^+\text{ has label }9.
 \tag{R9.3}
\]
The derivative in that coordinate is
\[
 \partial_{w_2^+}=\tfrac12(\partial_{u_2}-i\partial_{v_2}).
 \tag{R9.4}
\]
The first nonzero homogeneous term of \(s_A\) has degree four.
Consequently, in its fourth derivative only the term with two
derivatives on each factor contributes:
\[
 \partial_{w_2^+}^{\,4}s_A(0)
   =2^{-4}\binom42(-i)^2(-2)(-2)=-\frac32.
 \tag{R9.5}
\]
This is an exact coefficient calculation, independent of analytic
tail estimates.

Take the target positive space \(V=E'^2\) and the source skew
line \(W\) with coefficient \(-2\xi'\), in the half-trace Hom
convention of AM-DO-022. On the underlying \(A^2=J^4\), let
\[
 P=\partial_{w_{2,1}^+}^{\,4}\partial_{w_{2,2}^+}^{\,4}.
 \tag{R9.6}
\]
The actual finite vacuum is the tensor of the four original finite
Schwartz vacua; its norm is one. Its Bargmann realization is
\[
 \mathcal R\phi_{00}=C^4s_A(z_1)s_A(z_2).
 \tag{R9.7}
\]
Apply the actual creation operators corresponding to \(P\), as in
ALP-LIFT-09, and denote the resulting global Schwartz vector by
\(\phi_P\). Equations (R9.5)–(R9.7) give
\[
 \boxed{\vartheta_{\phi_P}(1,1)=\frac94\,C^4\ne0.}
 \tag{R9.8}
\]
Its degree vector is eight at CM label 9 and zero at all other
labels. Hence this is a single source-torus isotypic Fock vector,
not a sum whose nonzero components remain unidentified.

The period \(C^4\) has not been set equal to one. In the algebraic
coordinate normalization the displayed coefficient is \(9/4\);
it is an \(11\)-adic unit. The coordinate change (R9.4) has a
dyadic denominator. No claim of integrality at 2 or at a changed
bad-prime Hodge basis is inferred from the coefficient at 11.

## 2. A globally admissible splitting, with its infinity labels

Let \(\mu_E\) be the explicit global character constructed in
ALP-LIFT-09, so that
\(\mu_E|_{\mathbf A_F^\times}=\epsilon_{E/F}\).
Define
\[
 \mu'=\mu_E\circ N_{E'/E},\qquad \chi_S=\mu',\qquad \chi_T=1.
 \tag{R9.9}
\]
The fields satisfy \(E'=EF'\) and \(E\cap F'=F\).
Restriction of the norm in (R9.9) to \(\mathbf A_{F'}^\times\)
is \(N_{F'/F}\). Compatibility of the quadratic idele-class
character with base change therefore gives
\[
 \mu'|_{\mathbf A_{F'}^\times}
   =\epsilon_{E/F}\circ N_{F'/F}
   =\epsilon_{E'/F'}.
 \tag{R9.10}
\]
This is the required restriction for a source skew line; the
even-dimensional target requires the trivial restriction and has
the chosen character 1. Use the same rationally compatible standard
Weil representation as in the cited constructions.

At the ordered CM labels \(1,3,9,15,17,23\), the exponents
\(\mu'_\tau(z)=(z/\bar z)^{m_\tau/2}\) are
\[
 \mathbf m=(-1,+1,-1,-1,+1,-1),\qquad
 \boldsymbol\nu=(\mathbf m+\mathbf1)/2=(0,1,0,0,1,0).
 \tag{R9.11}
\]
Indeed restriction to \(E\) gives the three labels \(1,3,2,1,3,2\);
ALP-LIFT-09 and the corrected AM-DO-023 give exponent \(-1\)
on labels 1 and 2 and \(+1\) on label 3.
The target compact type of the actual first image is accordingly
\[
 \pi_\infty=\mathop{\boxtimes}_{\tau\in\Phi'}
       \det^{\nu_\tau}\operatorname{Sym}^{d_\tau}\mathbf C^2,
 \quad d_9=8,\quad d_\tau=0\ (\tau\ne9).
 \tag{R9.12}
\]
For the Hom source action \(X\mapsto Xt^{-1}\), its actual torus
eigencharacter is
\[
 \beta(t)=\prod_{\tau\in\Phi'}\tau(t)^{-1}\,\tau_9(t)^{-8}.
 \tag{R9.13}
\]
Here the exponent \(-1\) at each place is the rank-two target's
vacuum shift with \(\chi_T=1\). The character \(\chi_S\) changes
the target action, not this source action. On the rational
generator \(\zeta_{28}\), (R9.13) has exponent
\[
 -\sum_{\tau\in\Phi'}\tau-8\cdot9=-68-72=-140\equiv0\pmod{28}.
 \tag{R9.14}
\]
Thus \(\beta\) is trivial on \(\mu_{28}\).

## 3. The torus quotient and the actual input

Put \(T'=U(1)(E'/F')\) and \(K_0=(\widehat{\mathcal O}_{E'})^1\).
Masley (1976), Main Theorem, printed pp. 179 and 184, implies
\(h(E')=1\): \(\varphi(28)=12\le24\), and 28 does not occur
in the displayed list with class numbers 2 through 10.
This published class-number result is an input, not a new
calculation or a computational class-group certificate.

It implies the exact torus decomposition
\[
 T'(\mathbf A_{F',f})=T'(F')K_0,\qquad
 T'(F')\cap K_0=\mu_{28}.
 \tag{R9.15}
\]
Here is a short proof of the first assertion in the required
norm-one form. For a norm-one finite idele \(t\), its fractional
ideal \(I(t)\) satisfies \(I(t)\overline{I(t)}=\mathcal O_{E'}\).
Every nonsplit prime therefore has exponent zero, and the
exponents at a split conjugate pair are opposite. Choose a
fractional ideal \(B\), supported on one prime in each such
pair, so that \(I(t)=B/\bar B\). Class number one gives
\(B=(b)\). The rational element \(b/\bar b\) has norm one
and exactly the same ideal as \(t\). Their quotient belongs
to \(K_0\). This proves the decomposition without assuming a
statement about signatures of real units. For the intersection,
a norm-one integral unit has every complex absolute value one;
Kronecker's theorem makes it a root of unity, and the roots
of unity of \(E'\) are precisely \(\mu_{28}\).

The source action preserves the actual one-dimensional finite
vacuum eigenspace, because norm-one integral units preserve its
trace lattice and semicharacter. Therefore it has an actual smooth
unitary character \(\lambda_f:K_0\to\mathbf C^\times\).
This is not an unspecified phase used to identify a moved
kernel: it is the character of the fixed finite representation
on its named one-dimensional line. Put \(K=\ker\lambda_f\)
and \(\Gamma=\mu_{28}\cap K\). Smoothness and compactness imply
that \(K\) has finite index. Equation (R9.15) gives
\[
 h_K=\#T'(F')\backslash T'(\mathbf A_{F',f})/K
     =\frac{[K_0:K]}{[\mu_{28}:\Gamma]}.
 \tag{R9.16}
\]
Rational invariance of the nonzero theta value (R9.8) gives
\(\beta(\zeta)\lambda_f(\zeta)=1\) for every
\(\zeta\in\mu_{28}\). Thus \(\beta|_\Gamma=1\);
in fact (R9.14) makes \(\lambda_f|_{\mu_{28}}=1\).

Normalize Haar measure on the compact torus quotient
\(T'(F')\backslash T'(\mathbf A_{F'})\) to have volume one.
Its \(h_K\) finite components have equal volume \(1/h_K\).
Define the actual input \(f_K\) to be \(h_K\beta(t_\infty)\)
on the identity finite component and zero on the other
components, using rational triviality to transport that
description. The condition \(\beta|_\Gamma=1\) makes this
definition unambiguous. Its exact norms are
\[
 \|f_K\|_2^2=h_K,\qquad \|f_K\|_\infty=h_K.
 \tag{R9.17}
\]
The source action on \(\phi_P\) is \(\beta\) at infinity
and is trivial on \(K\) at finite places. The target action
commutes with the source action. Integrating over the one
component supporting \(f_K\), with the convention
\[
 \Theta_P(g)=\int_{[T']}\vartheta_{\phi_P}(t,g)
                                      \overline{f_K(t)}\,dt,
 \tag{R9.18}
\]
therefore gives the equality of actual automorphic functions
\[
 \boxed{\Theta_P(g)=\vartheta_{\phi_P}(1,g),\qquad
        \Theta_P(1)=\frac94 C^4.}
 \tag{R9.19}
\]
For norm-one source input \(f_K/\sqrt{h_K}\), the output
is \(h_K^{-1/2}\Theta_P\). This proves a nonzero first
lift on the common host without any unproved claim that
\(\lambda_f\) is trivial.

**The actual compact character is trivial.** At every odd unramified
quadratic place the target identity plane is integrally hyperbolic,
as in AM-DO-022. Pan (2001), section 6.2, Lemma and equation (6.2.a),
printed p. 197, treats exactly a one-dimensional moving unitary space
and a two-dimensional isotropic opposite space. Its comparison has
\(\alpha=1\) and \(\beta=\chi((t-1)\delta)\). The opposite
character is \(\chi_T^{-1}=1\), so both factors are one. The
lattice-model action fixes the actual selfdual-lattice vacuum, as
specified in Pan section 3.3 and the normalization of AM-DO-022.
There is no assumption that the moving rank is even; this primary
lemma is itself the rank-one case. The other splitting character
\(\chi_S=\mu'\) affects the target action only. At relative split
places, including all dyadic places, AM-DO-020 gives the same
compact invariance with the retained trace-one convention, since
its source determinant-root factor is \(\chi_T(x)^{-1}=1\).
The identity element acts as one as well. These cases cover every
finite place of \(E'/F'\). Consequently
\[
 \boxed{\lambda_f=1,\quad K=K_0,\quad h_K=1,\quad
        \|f_K\|_2=\|f_K\|_\infty=1.}
 \tag{R9.27}
\]
Thus (R9.19) is already the first lift with norm-one source input.
The general-component calculation above records exactly how a
nontrivial finite character would have entered, without discarding
such a cost by convention.

## 4. Exact Fock normalization

In the \(w^\pm\) coordinates the positive Hermitian form
on \(A\) is
\[
 H_A=\sum_{j=1}^3
       \frac{|w_j^+|^2+|w_j^-|^2}{2G_j}.
 \tag{R9.20}
\]
The creation operator for \(w_2^+\) is one half of the
creation operator for \(u_2\) minus \(i\) times that for
\(v_2\). Orthogonality of the two modes and the normalization
in ALP-LIFT-09 give its one-creation squared norm
\(\pi/(2G_2)\). The actual Gaussian used in (R9.7), before applying creation
operators, has squared norm \(\det(2Y)^{-2}\), because there
are four ordinary Jacobian factors. Hence the exact squared norm of
the actual archimedean vector in (R9.6) is
\[
 \|\phi_{P,\infty}\|^2=\det(2Y)^{-2}(4!)^2
                                  \left(\frac{\pi}{2G_2}\right)^8.
 \tag{R9.21}
\]
The unit archimedean vector therefore has identity value
\[
 C^4\det(2Y)\frac{3}{32}\left(\frac{2G_2}{\pi}\right)^4.
 \tag{R9.22}
\]
Combining unit archimedean vector and norm-one source
input adds the factor \(h_K^{-1/2}\). The determinant factor is necessary: an earlier draft
used a norm relative to unit Gaussian and omitted it when normalizing
the actual theta Gaussian; the present formulas correct that error.
These are analytic normalizations; they do not replace the algebraic
coefficient \(9/4\) or the common period \(C^4\).

## 5. A fixed character repair for the literal bilinear second edge

This paragraph uses the corrected source convention of
AM-DO-023 and the literal bilinear theta integral in
ALP-LIFT-11's amended version. Let
\[
 c_\tau=2-\nu_\tau,\qquad
 \mathbf c=(2,1,2,2,1,2).
 \tag{R9.23}
\]
A global norm-one character with this infinity type can
be constructed explicitly from (R9.15). Choose a split
place over 29 with \(\zeta_{28}\mapsto2\pmod{29}\).
The element 2 generates \(\mathbf F_{29}^\times\).
The infinity character \(\beta_{\mathbf c}\) has
exponent
\[
 \sum_{\tau\in\Phi'}c_\tau\tau=116\equiv4\pmod{28}
 \tag{R9.24}
\]
on \(\mu_{28}\). Let its finite compact character be
trivial elsewhere and take the value
\(\exp(2\pi i\,24/28)\) on 2 at this place. Its
restriction to \(\mu_{28}\) is exactly
\(\beta_{\mathbf c}^{-1}\), so their product descends
through (R9.15) to a unitary automorphic character
\(\gamma\). Equivalently, for \(t_f=\delta k\), define
\(\gamma(t_\infty,t_f)
=\beta_{\mathbf c}(\delta_\infty^{-1}t_\infty)\rho(k)\).
Independence of the choice of \(\delta\) follows from the
displayed equality on roots of unity. Its finite conductor
divides this fixed place over 29; its compact values have
order dividing 7.

Replace \(\chi_S\) in (R9.9) by
\(\chi_S'=\mu'(\gamma\circ j)\), where \(j(x)=x/\bar x\);
leave \(\chi_T=1\). The restriction (R9.10) is unchanged.
The actual splitting ratio is \(\gamma(\det g)\) on
the target. To check every place, at nonsplit finite
places the local norm-one torus is its maximal compact,
and \(\gamma\) is trivial there; at split finite places
use the determinant-root formula of AM-DO-020; at real
places the corrected Fock formula changes the target
power by \(c_\tau\). Thus
\[
 \Theta'_P(g)=\gamma(\det g)\Theta_P(g)
 \tag{R9.25}
\]
as actual automorphic functions. All identity values and
scalar automorphic norms are preserved exactly. The
first target types become
\[
 \pi'_\tau=\det^2\operatorname{Sym}^{d_\tau}\mathbf C^2,
 \tag{R9.26}
\]
and every infinity exponent of \(\chi_S'\) is 3.

For the next positive Hom edge \(U(2)\to U(4)\) with
both splitting characters 1, the source Fock type of
partition \((d_\tau,0)\) is
\(\det^{-2}\operatorname{Sym}^{d_\tau}(\mathbf C^2)^*\).
It is exactly the contragredient of (R9.26), as required
by the literal bilinear integral \(\int\vartheta\,f\).
The degrees have not increased. This is local occurrence
and exact first-image preservation, not a proof of the
global second integral's nonvanishing.

The second edge now lies on precisely the E-prime host
of AM-DO-022–024, so its finite moved-vacuum formula,
positive direct-average sign, common period, and
probability-Haar theta-line pairing are available without
an extension-of-field comparison. A prescribed global
second image, its finite input, its automorphic mass and
its selected coefficient-lattice costs remain to be proved.

## 6. Geometric location and limits

The abelian variety is the ordinary product \(J^4\), with
the extra \(E'\)-action specified in (R9.1)–(R9.3);
there is no substitution of the conjugate E-action
product excluded from AM-K018. The value is an actual
jet of the trace-one Picard line, transferred through
its reduced Poincare trivialization to a global theta
integral. The integral source input is an automorphic
character of the norm-one torus; the repair is tensoring
an actual target representation by a rank-one character.
The exact FGA/SGA locators for these constructions are
those in GROTHENDIECK_DICTIONARY.md sections 2–5
(FGA 232 Theorem 3.1; FGA 236 Corollaries 1.7 and 2.3;
SGA 7 I VII 2.7 and 2.9; SGA 3 I Proposition 4.7.3).

This closes the previously separate-host obstruction for
these particular first and candidate second edges. It
does not instantiate the old elliptic VacIn, the
even-rank starting coefficient module, the full six
arithmetic identities, or the DP44 gain/cost data.

## References and exact inputs

Masley, J. M. (1976). Solution of small class number problems for
cyclotomic fields. *Compositio Mathematica, 33*(2), 179–186.
Main Theorem, pp. 179 and 184; the table was visually checked
on PDF pages 2 and 7 (one-based).
https://numdam.org/item/CM_1976__33_2_179_0.pdf

AM-R-004–006 (actual periods, metric, trace-one scalar);
AM-K018 (ordinary-product source gauge);
AM-DO-020, AM-DO-022–024 (fixed finite conventions and E-prime host);
corrected AM-DO-023 (DO23.3–DO23.9);
ALP-LIFT-09 (V7–V11 and V18–V38);
ALP-LIFT-11 (explicit torus-character extension and bilinear
repair, used with the newly proved E-prime torus decomposition).

Pan, S.-Y. (2001). Splittings of the metaplectic covers of some reductive dual pairs. Pacific Journal of Mathematics, 199(1), 163–226. Section6.2, Lemma and equation(6.2.a), p197; section3.3 for the lattice normalization. https://msp.org/pjm/2001/199-1/pjm-v199-n1-p10-p.pdf
