# ALP-LIFT-08: the normalized actual trace-one section and its complete finite scalar content

Run ALP_MACHINE; `/root/lift_accounting`, GPT-6 Astra Pro; reasoning effort
not separately exposed. This uses ALP-LIFT-05's good models and integral
Hodge bases and ALP-LIFT-07's integral identification of the trace-one
line with the theta characteristic \(2\infty\). It is a theorem about
the actual principal section and its first nonzero jet. It does not
assert integral reduced-theta coefficients from an integral first jet.

## Statement

Let \(C:y^2=x^7-1\), \(J=\operatorname{Jac}(C)\), and
\(\omega_i=x^{i-1}dx/y\), \(1\leq i\leq3\). Let \(L\) be
the symmetric rigidified trace-one line \(L_{w_0}\) of DP49,
identified integrally by ALP-LIFT-07 with the rigidified principal
theta line for \(2\infty\). In logarithmic differential coordinates
\(u_i\), with \(du_i=\omega_i\) at the origin, put
\[
 q_\omega(u)=u_1u_3-u_2^2.
 \tag{Q1}
\]
There is a unique algebraic section
\[
 s_q\in H^0(J,L)
 \tag{Q2}
\]
whose initial homogeneous jet in any origin-normalized formal frame
is precisely \(q_\omega\). A formal frame is origin-normalized if
its value at the identity agrees with the given rigidification.
Changing such a frame cannot alter this first nonzero degree-two jet.
The section is defined over \(\mathbb Q\) after using the canonical
identification with the \(2\infty\) theta line, and in particular
over \(E=\mathbb Q(\zeta_7)\) in the trace-one description.

At a finite place after the good-model extensions of ALP-LIFT-05,
let \(s_{\mathrm{prim}}\) be any primitive generator of the rank-one
module \(H^0(\mathcal J,\mathcal L)\). Define the scalar content by
\[
 c_p(s_q)=v_p(a),\qquad s_q=a\,s_{\mathrm{prim}},\qquad v_p(p)=1.
 \tag{Q3}
\]
This is independent of the generator. Then
\[
 \boxed{c_2(s_q)=8/7,\qquad c_7(s_q)=-1/2,
             \qquad c_p(s_q)=0\quad(p\nmid14).}
 \tag{Q4}
\]
The negative entry means a pole relative to the primitive integral
section module. These are finite scalar contents of the entire
section, not just valuations of two selected Taylor coefficients.

More explicitly, write \(v_i\) for tangent/logarithmic coordinates
dual to the primitive local Hodge basis \(\eta_i\) of ALP-LIFT-05.
Only their linear terms are needed. At 2 and 7 respectively,
\[
 q_\omega=\frac{\alpha^4}{\iota^2}(v_1v_3-v_2^2),
 \qquad
 q_\omega=\frac{\lambda^4}{\beta^2}(v_1v_3-v_2^2)
          =\lambda^{-3}(v_1v_3-v_2^2),
 \tag{Q5}
\]
where \(\alpha^7=-4\), \(\iota^2=-1\),
\(\lambda=\zeta_7-1\), and \(\beta^2=\lambda^7\).

If \(\sigma_q\) denotes the reduced CM germ of \(s_q\), its
initial term is again \(q_\omega\), since a normalized reduced frame
has value one at the origin. The comparison of this germ with the
classical hyperelliptic sigma, and integrality of its Hurwitz
coefficients, are separate assertions proved by the Kummer agent.
Likewise the moved germ called \(\Sigma_{\mathrm{tr}}\) in
AM-DO-015 is a scalar multiple \(c\sigma_q\); it is not normalized
by (Q1). Root's derivative-Thomae calculation determines that separate
scalar. These notations must not be interchanged.

## Full proof

### 1. The integral cohomology at the characteristic \(2\infty\)

Let \(R\) be one of the complete good-model DVRs. Write
\(\mathcal B=\mathcal O_{\mathcal C}(2\infty)\), to distinguish
the curve line from the theta line on its Jacobian. On each good
model, let \(X\) be its degree-two hyperelliptic coordinate. The
modules
\[
 U=H^0(\mathcal C,\mathcal B),\qquad
 W=H^0(\mathcal C,\omega_{\mathcal C/R}\otimes\mathcal B^{-1})
 \tag{Q6}
\]
have integral bases
\[
 U=(1,X),\qquad W=(\eta_1,\eta_2),
 \tag{Q7}
\]
where \(\eta_2=X\eta_1\) and \(\eta_3=X^2\eta_1\).
Indeed \(X\) has its only pole, of order two, at infinity, and the
other curve generator has pole order seven. Thus the functions with
pole at most two are precisely \(\langle1,X\rangle\) on every
fibre. The integral Hodge forms have respective orders four, two,
and zero at infinity, as verified in ALP-LIFT-05; vanishing by at
least two selects precisely \(\eta_1,\eta_2\). Cohomology and base
change, or reduction followed by Nakayama, proves these are the full
integral modules. Relative Serre duality gives
\[
 H^1(\mathcal C,\mathcal B)=W^*.
 \tag{Q8}
\]
Both cohomology modules are consequently free of rank two, including
at 2 and 7.

### 2. A two-by-two determinant with integral first-order matrix

The determinant construction of the relative theta divisor is the
same one used in ALP-LIFT-07: on the completed Picard space at the
class of \(\mathcal B\), a perfect two-term free complex computes
the universal line's cohomology, and its determinant is a local theta
equation. This standard construction is recalled in Casalaina-Martin
and Kass (2010, Definition 3.1, pp. 9–10), with its determinant
invariance in Stacks Project Tag 0FJI.

At the origin, the cohomology in (Q6)–(Q8) is free. The specialized
complex therefore splits into these two cohomology modules, with zero
differential, plus an acyclic free summand. To see that this splitting
is integral, the images, kernels and cohomology are free over the DVR,
so every short exact sequence with free quotient splits. Lifting the
chosen decompositions to the completed base and eliminating the
invertible acyclic block by row/column operations leaves a two-by-two
matrix \(d\), all of whose entries belong to the origin ideal. The
eliminated block has unit determinant. Thus the initial quadratic
theta equation is, up to an integral unit, the determinant of the
linear part \(d_1\).

We give the first-order identification explicitly. A tangent vector
to the Picard scheme is a class \(\xi\in H^1(\mathcal O_C)\).
If transition functions \(g_{ij}\) for \(\mathcal B\) are deformed
to \(g_{ij}(1+\epsilon\xi_{ij})\), then a section \(s\) lifts to
first order precisely when the Čech cocycle \(\xi_{ij}s_j\) is a
coboundary (a simultaneous overall sign has no effect on the
two-by-two determinant). The first differential on cohomology is
therefore cup product
\[
 U\longrightarrow H^1(\mathcal B),\qquad s\longmapsto\xi\smile s.
 \tag{Q9}
\]
Under the Serre duality (Q8), its matrix entries are the pairings of
\(\xi\) with the products \(s_a t_b\in H^0(\omega)\), for the
bases in (Q7). Those products are exactly
\[
 \begin{pmatrix}\eta_1&\eta_2\\\eta_2&\eta_3\end{pmatrix}.
 \tag{Q10}
\]
Since \(H^1(\mathcal O_C)\) is integrally dual to
\(H^0(\omega)\), in the tangent coordinates \(v_1,v_2,v_3\)
dual to these forms the first-order matrix and its determinant are
\[
 d_1=\begin{pmatrix}v_1&v_2\\v_2&v_3\end{pmatrix},\qquad
 \det d_1=q_\eta=v_1v_3-v_2^2.
 \tag{Q11}
\]
This polynomial has an integral-unit coefficient at every place,
including residue characteristic two. In particular it is nonzero
there; no division by 2 or characteristic-not-two theorem was used.
The argument is the usual determinant/cup-product mechanism of the
Riemann–Kempf tangent cone, with the present integral case established
directly rather than inferred from a complex tangent-cone statement.

The origin fibre of the determinant theta line identifies with
\(\det U^{-1}\otimes\det W^{-1}\). The bases in (Q7) give it a
primitive generator. Passing to its rigidification and using the
integral isomorphism with \(\mathcal L_{w_0}\) from ALP-LIFT-07,
one sees that the degree-two jet map on the actual principal section
module has image exactly
\[
 R\,q_\eta\subset\operatorname{Sym}^2 e^*\Omega^1_{\mathcal J/R}.
 \tag{Q12}
\]
Here a remaining integral unit in the determinant presentation can
be absorbed in the primitive section generator. The principal theta
section module is free of rank one and formation commutes with base
change, by the standard principal-polarization cohomology theorem
used in DP59. Therefore (Q12) is a saturated rank-one image; it
determines the scalar content of the *entire section* from its
quadratic jet.

### 3. Algebraic normalization and finite contents

Over the original characteristic-zero field use
\(U=(1,x)\), \(W=(\omega_1,\omega_2)\). The same calculation
gives the jet line spanned by (Q1). Its generator is defined over
\(\mathbb Q\), as are the curve, infinity, the rigidified
\(2\infty\) theta line, and this quadratic tensor. The nonzero
degree-two jet map from a one-dimensional section space has a unique
inverse image of \(q_\omega\). This proves the existence, uniqueness
and field assertion in (Q2). A change of origin-normalized formal
frame multiplies a local representative by a power series with
constant term one, and cannot change its first nonzero degree-two
term.

At 2, ALP-LIFT-05 gives
\(\omega_i=\alpha^i\iota^{-1}\eta_i\). Thus at the tangent level
\(u_i=\alpha^i\iota^{-1}v_i\), and
\[
 q_\omega=\alpha^4\iota^{-2}q_\eta,
 \qquad v_2(\alpha^4\iota^{-2})=8/7.
 \tag{Q13}
\]
Equation (Q12) proves \(c_2(s_q)=8/7\).

At 7, ALP-LIFT-05 gives
\[
 \begin{aligned}
 u_1&=(\lambda/\beta)v_1,\\
 u_2&=(\lambda/\beta)(v_1+\lambda v_2),\\
 u_3&=(\lambda/\beta)(v_1+2\lambda v_2+\lambda^2v_3).
 \end{aligned}
 \tag{Q14}
\]
Substitution cancels the \(v_1^2\) and \(v_1v_2\) terms and
gives
\[
 q_\omega=(\lambda^4/\beta^2)q_\eta
           =\lambda^{-3}q_\eta,
 \qquad v_7(\lambda^{-3})=-1/2.
 \tag{Q15}
\]
Again (Q12) proves the stated content. At every other prime the
original basis is already primitive, so (Q12) gives content zero.
This proves (Q4)–(Q5).

There is also an independent determinant-frame check of the two
scalings. At 2, relative to (Q7), the determinant valuations of
\((1,x)\) and \((\omega_1,\omega_2)\) are \(2/7\) and
\(6/7\). At 7 they are respectively \(1/6\) and
\(v_7(\lambda^3/\beta^2)=-2/3\). Their sums are exactly
\(8/7\) and \(-1/2\). These sums agree with (Q13) and (Q15),
as required by the determinant line
\(\det U^{-1}\otimes\det W^{-1}\).

## Consequence at the actual prime 11, and scope

The section \(s_q\) is now an explicitly normalized generator of
the actual integral principal section module at 11. It can be used
as the fixed primitive base section in accepted DP59 and DP62. This
removes an unspecified scalar from their application to this Jacobian.
Their permitted subgroup, square level, theta-group lift and
selected-jet conditions are unchanged. Their integral-span statements
are cited as accepted results, not re-proved here.

The conclusion does not infer full reduced-theta integrality from the
quadratic term. The scalar content at 7 is measured in the primitive
stable Hodge/line model. It is compatible with separate Hurwitz
integrality in the original \(\omega\)-coordinates, because those
coordinates are not primitive at 7. The dyadic content also says
nothing by itself about the norm-two, nonunit trace-one kernel
parameter. Finally a principal section and its allowed translates
still require an actual theta-lift row/column identification and all
global costs before any integer chain improvement follows.

## Literature and status

The determinant and relative-duality inputs are the same directly
checked primary sources as in ALP-LIFT-07: Casalaina-Martin and Kass
(2010), arXiv:0907.0212v2, Definition 3.1, pp. 9–10; Stacks Project
Tags 0FJI and 0E6N. The Čech first-order argument and the integral
splitting argument needed here are written in full above.

The classical tangent-cone theorem is due to Kempf, G. (1973), *On
the geometry of a theorem of Riemann*, Annals of Mathematics, 98(1),
178–185, https://doi.org/10.2307/1970910 . The original publication
metadata was checked on the Annals site; its paywalled full text was
not inspected. The related cup-product matrix description was read
in Hitching and Hoff, arXiv:1610.03456v2, §3.1, p. 11. Their stated
Petri-injective setup is not asserted for this hyperelliptic curve;
our integral proof does not use that hypothesis or their reconstruction
theorem. No whole-proof check of those literature results is claimed.
