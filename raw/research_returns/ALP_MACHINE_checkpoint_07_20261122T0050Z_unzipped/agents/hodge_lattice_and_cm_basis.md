# ALP-LIFT-05: stable Hodge lattices and a normalized induced CM eigenbasis

Run ALP_MACHINE; authors /root/lift_accounting and /root, GPT-6 Astra Pro.
Reasoning effort is not exposed. The construction at 7 and the positive
trace polarization were suggested independently by /root and checked here.
This is an actual geometric normalization theorem. It does not identify an
arithmetic theta lift with an automorphic lift, or determine a SizeData₂ gain
or division-error field.

## Statement

Write \(\zeta=\zeta_7\), \(E=\mathbb Q(\zeta)\),
\(K=\mathbb Q(\sqrt{-7})\), and
\[
 C:y^2=x^7-1,\qquad J=\operatorname{Jac}(C),\qquad
 \omega_i=x^{i-1}dx/y\quad(1\le i\le3).
 \tag{H1}
\]
For a finite place above a rational prime \(p\), use the valuation
normalized by \(v_p(p)=1\). Fix algebraic numbers
\[
 \iota^2=-1,\quad \alpha^7=-4,\quad
 \lambda=\zeta-1,\quad \beta^2=\lambda^7,\quad \rho^4=7.
 \tag{H2}
\]
After adjoining these numbers, the following assertions hold.

**(a) Actual stable Hodge lattices.** At a place above 2, the good model
and its integral differential basis are
\[
 Y^2+Y=X^7,\qquad
 \eta_i^{(2)}=X^{i-1}dX/(2Y+1),\qquad
 \omega_i=\alpha^i\iota^{-1}\eta_i^{(2)}.
 \tag{H3}
\]
At a place above 7, they are
\[
 Y^2=f_\lambda(X):=\frac{(1+\lambda X)^7-1}{\lambda^7},\qquad
 \eta_j^{(7)}=X^{j-1}dX/Y,
 \tag{H4}
\]
with
\[
 \omega_i=\frac{\lambda}{\beta}
       \sum_{k=0}^{i-1}\binom{i-1}{k}\lambda^k\eta_{k+1}^{(7)}.
 \tag{H5}
\]
Here and below an integral differential basis means a basis of
\(e^*\Omega^1_{\mathcal J/R}\), identified through the Abel map with
\(H^0(\mathcal C,\Omega^1_{\mathcal C/R})\), for the good model over
the local valuation ring \(R\). Consequently the signed determinant
valuations of \(\omega_1\wedge\omega_2\wedge\omega_3\) are exactly
\[
 \begin{array}{c|c}
 p&v_p(\omega_1\wedge\omega_2\wedge\omega_3)
       \text{ relative to an integral generator}\\ \hline
 2&12/7\\
 7&-3/4\\
 p\nmid14&0.
 \end{array}
 \tag{H6}
\]
The negative entry is a valuation of a rational section, not a positive
index of an inclusion of integral lattices.

**(b) Complete determinant metric and height.** Give the determinant
Hodge line the normalization
\[
 \|s\|_{L^2}^{\,2}
   =\frac{\mathrm i^{g^2}}{2^g}\int_{A(\mathbb C)}s\wedge\overline{s}
 \quad(g=\dim A).
 \tag{H7}
\]
Let \(G=\operatorname{diag}(G_1,G_2,G_3)\) be the Gram matrix of
(H1), already computed in ALP-LIFT-03:
\[
 G_i=\frac{2\pi}{7}
 \frac{\Gamma(i/7)\Gamma(1/2-i/7)}
      {\Gamma(1-i/7)\Gamma(1/2+i/7)}.
 \tag{H8}
\]
Then
\[
 \boxed{h_{F,L^2}(J)=\frac{12}{7}\log2-\frac34\log7
                       -\frac12\log\det G.}
 \tag{H9}
\]
This equals the Wilms normalization used in ALP-LIFT-02. Numerically it
is \(-3.80116074543404940138079328403117913069\ldots\); the decimal
is a cross-check of the exact expression.

**(c) An actual comparison variety and compatible principal polarization.**
Take the elliptic curve of full CM by \(\mathcal O_K\)
\[
 B:y^2+xy=x^3-x^2-2x-1,\qquad \psi=dx/(2y+x),
 \tag{H10}
\]
and put \(G_B=(\mathrm i/2)\int_{B(\mathbb C)}\psi\wedge\overline\psi\),
where \(\mathrm i\) is the usual positive imaginary unit in each
complex metric, not the image of the algebraic symbol \(\iota\)
under an arbitrary embedding.
This is LMFDB 49.a4, Cremona 49a1; the full CM discriminant \(-7\)
is the only catalogued fact used about it. Its Weierstrass coefficients,
discriminant, local changes of variables and all following metrics are
computed below.

The basis \(1,\zeta,\zeta^2\) identifies the Serre tensor variety
\(A_{\mathrm{ind}}=\mathcal O_E\otimes_{\mathcal O_K}B\) with
\(B^3\) as in ALP-LIFT-02. Put
\[
 S=\zeta+\zeta^2+\zeta^4=(-1+\sqrt{-7})/2,\qquad
 u=-(\zeta-\zeta^{-1})^{-2}.
\]
The matrix of the positive Hermitian trace form
\(\operatorname{Tr}_{E/K}(u\overline x y)\) in that basis is
\[
 H=\begin{pmatrix}
 2&-1&1+S\\
 -1&2&-1\\
 -S&-1&2
 \end{pmatrix},\qquad \det H=1.
 \tag{H11}
\]
It defines an \(\mathcal O_E\)-compatible principal polarization on
\(A_{\mathrm{ind}}\). The product polarization is not silently used
as that compatible polarization.

Let \(\psi_a\), \(a=0,1,2\), denote the product invariant
differentials on \(B^3\). For \(i\in\Psi=\{1,2,4\}\), set
\[
 \vartheta_i=(\zeta^i-\zeta^{-i})^{-1}
                     \sum_{a=0}^{2}\zeta^{ia}\psi_a.
 \tag{H12}
\]
These are CM eigenforms of type \(\Psi\). Their change-of-basis
matrix \(W\), with rows in the order \(1,2,4\), has determinant
\(-1\), and both \(W\) and \(W^{-1}\) have entries integral away
from 7. They are therefore a primitive integral CM eigenbasis at
every prime \(p\nmid7\). For the principal polarization (H11), their
Hodge Gram matrix is exactly
\[
                         G_B I_3.
 \tag{H13}
\]
Their determinant section has normalized valuation \(-3/4\) at 7
and zero at every other prime, even though their individual lattice
at 7 is not asserted to be the primitive Hodge lattice. In particular
\[
 3h_{F,L^2}(B)=-\frac34\log7-\frac32\log G_B.
 \tag{H14}
\]

**(d) Exact comparison in these CM coordinates.** With \(\delta_7\)
from ALP-LIFT-02 and
\(\delta_{7,\{2,7\}}=\delta_7-(12/7)\log2\) from ALP-LIFT-04,
\[
 \boxed{\delta_{7,\{2,7\}}
       =-\frac12\log\frac{G_1G_2G_3}{G_B^3}.}
 \tag{H15}
\]
Thus the order-linear difference of the equal-direction Cauchy bounds
in these actual diagonal CM coordinates is exactly the order-linear
difference of the bare prime certificates over \(p\nmid14\).
The precise analytic statement and its scope are given after the proof.

## Proof of (a): the good model at 2

Make the change \(x=\alpha X\), \(y=\iota(2Y+1)\). Since
\(\alpha^7=-4\), the original equation becomes exactly
\(Y^2+Y=X^7\). Complete this affine chart by the chart
\[
 U=X^{-1},\qquad V=YU^4,\qquad V^2+U^4V=U.
 \tag{H16}
\]
On their common locus the changes are inverse to one another. Both
charts are finite free of rank two over their respective affine
charts of \(\mathbb P^1\), with bases \(1,Y\) and \(1,V\).
They therefore form a finite flat double cover of \(\mathbb P^1\),
which is proper. The algebra generators transform by \(V=U^4Y\),
so the underlying rank-two pushforward is
\(\mathcal O\oplus\mathcal O(-4)\); its Euler characteristic is
\(1-3=-2\), giving arithmetic genus three in every fiber.

In residue characteristic 2 the finite equation has derivative 1
with respect to \(Y\). In (H16) the derivative with respect to
\(U\) of \(V^2+U^4V-U\) is \(-1\). Thus the whole special fiber
is smooth, including the point at infinity \((U,V)=(0,0)\).
The special fiber is geometrically integral: if
\(Y^2+Y-X^7\) were reducible over \(\overline k(X)\), then
\(X^7=h^2+h\) for a rational function \(h\). Any finite pole of
\(h\) would produce a finite pole of \(h^2+h\), and the pole at
infinity of a nonconstant polynomial \(h^2+h\) has even order.
Both alternatives contradict \(X^7\). The generic fiber is the
original smooth curve. This proves that (H16) is a smooth proper
genus-three model with an infinity section over the local valuation
ring, and remains so after any finite base extension.

The residue differential on a plane curve \(F(X,Y)=0\) is
\(dX/F_Y=-dY/F_X\) on the respective smooth open subsets. Thus
\(\eta_i^{(2)}\) is regular on the finite chart. On the other chart
it is
\[
                  -U^{3-i}\frac{dU}{2V+U^4}.
 \tag{H17}
\]
The same residue description shows regularity at infinity: when
\(2V+U^4\) is not a unit, the alternate denominator
\(4U^3V-1\) is a unit. The power \(U^{3-i}\) is nonnegative for
all three indices. Reduction on the finite chart gives
\(X^{i-1}dX\). These three differentials are independent over the
residue field, since the Artin–Schreier function-field extension is
separable and \(dX\ne0\).

For completeness, their being an integral basis follows without any
unproved saturation assumption. They are a basis on the generic
fiber because the genus is three. Express any global regular
differential as \(\sum a_i\eta_i^{(2)}\) with coefficients in the
fraction field. If some coefficient has negative valuation, multiply
by the smallest positive power of a uniformizer that makes all
coefficients integral and at least one a unit. This product, as a
multiple of the original integral differential, reduces to zero,
contradicting the independence just proved. Hence all coefficients
are integral. This also proves the claim after further ramified
base change.

The infinity section supplies the Abel map to the relative Jacobian.
The smooth proper curve has an abelian relative Picard scheme, and
the Abel map identifies its invariant differentials with those of the
curve. The precise references are Milne (2021), Proposition 2.2,
pp. 6–7, and Theorem 8.1 with the following paragraph, pp. 27–28;
the relative assertion follows also by applying the field assertion
on every fiber and Nakayama's lemma to the rank-three modules. This
is the same FGA input already accepted in DP22, not a new Picard
representability claim.

Finally, direct substitution gives (H3). Since
\(v_2(\alpha)=2/7\), the determinant valuation is
\((1+2+3)(2/7)=12/7\).

## Proof of (a): the good model at 7 and the remaining primes

The local cyclotomic uniformizer has \(v_7(\lambda)=1/6\). Write
\(f_\lambda(X)=\sum_{k=1}^{7}f_kX^k\). Its top coefficient is
1, and for \(1\le k\le6\),
\[
 f_k=\binom7k\lambda^{k-7},\qquad v_\lambda(f_k)=k-1.
\]
Here \(v_\lambda(7)=6\) and the binomial coefficients have exactly
one factor of 7. The cyclotomic identity \(\Phi_7(1+\lambda)=0\)
can be rearranged as
\[
 \frac7{\lambda^6}
 (1+3\lambda+5\lambda^2+5\lambda^3+3\lambda^4+\lambda^5)=-1.
\]
It follows that \(f_1\equiv-1\), while
\(f_2,\ldots,f_6\equiv0\). The reduction of (H4) is therefore
\(Y^2=X^7-X\). Its affine chart is smooth because
\(d(X^7-X)/dX=-1\) in characteristic 7. The polynomial has simple
roots and is not a square, so this special fiber is geometrically
integral.

The infinity chart is
\[
 U=X^{-1},\quad V=YU^4,\qquad
 V^2=U+f_6U^2+f_5U^3+\cdots+f_1U^7.
 \tag{H18}
\]
Away from \(U=0\) it is already covered by the finite chart. At
\(U=0\) its only point is \(V=0\), and its equation has derivative
\(-1\) with respect to \(U\). Thus all of this fiber is smooth.
As before, the two monic charts give a proper finite flat double
cover with pushforward \(\mathcal O\oplus\mathcal O(-4)\),
genus three and an infinity section. Its generic fiber is the
original curve by \(x=1+\lambda X\), \(y=\beta Y\).

The three differentials in (H4) are regular, since 2 is a unit and
\(dX/Y\) is twice the plane residue differential. On the infinity
chart they become \(-U^{3-j}dU/V\); again this is a unit multiple
of the residue differential times a nonnegative power of \(U\).
Their reductions are independent on the separable hyperelliptic
function field. The saturation argument above proves that they form
the full integral Hodge basis. Substitution of the change of
variables gives (H5). Its triangular diagonal entries are
\(\lambda^i/\beta\), so its determinant is
\[
                      \lambda^6/\beta^3.
\]
Its normalized valuation is
\(6/6-3(7/12)=-3/4\), proving the second row of (H6).
An explicit inverse formula, useful for the lattice rather than
only its determinant, is
\[
 \eta_j^{(7)}=\beta\lambda^{-j}
    \sum_{a=0}^{j-1}\binom{j-1}{a}(-1)^{j-1-a}\omega_{a+1}.
 \tag{H19}
\]

At a prime not dividing 14, the original two-chart hyperelliptic
model is smooth: 2 is a unit and its branch polynomial has
squarefree reduction. The same residue and independence argument
gives precisely the basis (H1), proving the last row of (H6).
These local models can also be made global over a common number
field containing (H2). Model (H3) is smooth over
\(\mathcal O_M[1/7]\); model (H4) is smooth over
\(\mathcal O_M[1/2]\). On their overlap the specified changes of
variables give an isomorphism, preserving infinity. Gluing yields a
smooth proper curve over \(\mathcal O_M\) and hence an abelian
scheme with generic fiber \(J_M\).

## Proof of (b): the determinant degree

The Hodge line is \(\det e^*\Omega^1_{\mathcal J/\mathcal O_M}\).
Use its nonzero rational section
\(s=\omega_1\wedge\omega_2\wedge\omega_3\). By definition of
the degree of a metrized line,
\[
 \frac{\widehat{\deg}(\overline\omega_{\mathcal J})}{[M:\mathbb Q]}
 =\frac1{[M:\mathbb Q]}
   \left(\sum_{v\text{ finite}}\operatorname{ord}_v(s)\log Nv
              -\sum_{\sigma:M\hookrightarrow\mathbb C}
                           \log\|s\|_\sigma\right).
 \tag{H20}
\]
The local orders from (H6) give exactly
\((12/7)\log2-(3/4)\log7\) after division by the degree:
\(\sum_{v\mid p}e_vf_v=[M:\mathbb Q]\). The original curve and
the three differentials are rational, so their complex metric is
the same under every \(\sigma\). The Riemann bilinear relation
identifies (H7) with \(\det G\) on this section; this is precisely
the determinant convention fixed in ALP-LIFT-03. Thus the
archimedean term is \(-\tfrac12\log\det G\), proving (H9).
It is the stable height because the chosen model is an abelian
scheme, and further base extension leaves the normalized degree
unchanged. This proof does not use isogeny invariance of height.

## Proof of (c): the comparison lattice

The Weierstrass coefficients of (H10) give
\(c_4=105\), \(c_6=1323\), and discriminant \(-343\); these
follow by the usual polynomial discriminant identities and can
also be checked by completing the square as follows. Put
\(y'=y+x/2\), \(z=x-1/4\). The equation becomes
\[
                   y'^2=z^3-\frac{35}{16}z-\frac{49}{32}.
\]
At 7 make the substitution \(z=\rho^2 Z\), \(y'=\rho^3 T\),
where \(\rho^4=7\). The resulting equation is
\[
                  T^2=Z^3-\frac5{16}Z-\frac{\rho^2}{32}.
 \tag{H21}
\]
Its discriminant is exactly \(-1\), either by dividing the old
discriminant by \(\rho^{12}=7^3\), or by direct substitution
in \(-16(4a^3+27b^2)\). It is a smooth proper elliptic model;
its special fiber is \(T^2=Z^3+Z\). The differential transforms as
\[
                        \psi=\rho^{-1}\frac{dZ}{2T}.
 \tag{H22}
\]
The invariant differential on the right after removing
\(\rho^{-1}\) is primitive, so \(v_7(\psi)=-1/4\).
At every prime different from 7 the original integral Weierstrass
model has unit discriminant, and \(\psi\) is primitive. Applying
(H20) in dimension one proves
\(h_{F,L^2}(B)=-(1/4)\log7-(1/2)\log G_B\), and thus (H14).
The value of \(G_B\) is approximately
\(4.9445046002825467364981969682\); this agrees with the independent
LMFDB period-area entry, but the proof of (H14) does not use that
numerical entry.

## Proof of (c): the compatible polarization and eigenforms

The integral basis \(1,\zeta,\zeta^2\) was proved in
ALP-LIFT-02; it gives the specified product coordinates. Each real
embedding of \(E^+\) sends
\(u=-(\zeta-\zeta^{-1})^{-2}\) to
\(1/(4\sin^2(2\pi i/7))>0\). Direct cyclotomic reduction gives
\[
 u=\frac{6+3\zeta^2+\zeta^3+\zeta^4+3\zeta^5}{7}.
\]
Taking the trace over the embeddings \(\zeta\mapsto\zeta^i\),
\(i=1,2,4\), gives (H11). Its entries belong to
\(\mathcal O_K\); its leading principal minors are \(2,3,1\),
which proves both positive definiteness and determinant one.
Multiplication by an element of \(E\) is adjoint to multiplication
by its complex conjugate for this trace form. In particular,
multiplication by \(\zeta\) preserves it.

Let \(\lambda_0\) be the product principal polarization on \(B^3\).
The integral Hermitian matrix \(H\) is an endomorphism of that
product; the homomorphism \(\lambda_H=\lambda_0\circ H\) has
integral positive Riemann form, and is therefore a polarization.
This standard polarization criterion is the Riemann-form criterion
in Milne (2022), Section 16, p. 31. Since \(H^{-1}\) has integral
entries by the adjugate formula and \(\det H=1\), \(H\) is an
automorphism, so \(\lambda_H\) is principal. Its Rosati involution
restricts to conjugation on \(E\) by the trace identity just proved.
Thus it is the required compatible principal polarization. The
polarization homomorphism is defined over a number field after the
CM endomorphisms are; an ample line realizing it can be chosen
after a further finite extension if necessary. No special theta
trivialization is asserted at this step.

For the metric calculation, let
\[
 V_{i,a}=\zeta^{ia}\quad(i=1,2,4;\ a=0,1,2),\qquad
 U=\operatorname{diag}\bigl(\sigma_i(u)\bigr).
\]
Then
\[
                         H=V^*UV.
 \tag{H23}
\]
In product differential coordinates, the Hodge Gram for
\(\lambda_H\) is \(G_B H^{-1}\). One may check this directly:
the normalized product Kähler form has coefficient matrix
\(G_B^{-1}H^t\); integrating
\((\mathrm i/2)\psi_a\wedge\overline\psi_b\) against its second
power divided by \(2!\) gives the corresponding cofactor, hence
\(G_B(\det H)H^{-1}\). Here \(\det H=1\). This computation fixes
the transpose convention and does not identify covectors with
tangent vectors without taking the inverse metric.

The rows of \(V\) are eigen-covectors for multiplication by
\(\zeta\), with eigenvalues \(\zeta,\zeta^2,\zeta^4\).
Indeed evaluation at \(\zeta^i\) sends multiplication by \(\zeta\)
on \(E\) to multiplication by \(\zeta^i\). It follows from
(H23) that
\[
 V(G_BH^{-1})V^*=G_B U^{-1}
     =G_B\operatorname{diag}(|\zeta^i-\zeta^{-i}|^2).
 \tag{H24}
\]
Dividing the corresponding eigenforms by
\(\zeta^i-\zeta^{-i}\) therefore proves (H13).

The Vandermonde determinant and the cyclotomic product are
\[
 \det V=-\sqrt{-7},\qquad
 \prod_{i=1,2,4}(\zeta^i-\zeta^{-i})=\sqrt{-7},
\]
with the same square-root convention \(2S+1=\sqrt{-7}\).
Their quotient gives \(\det W=-1\). Each denominator is a unit
away from 7, so all entries of \(W\) are integral there; its
adjugate gives the same conclusion for its inverse. This proves
primitivity at those primes. At 7 the determinant section equals
\(-\psi_0\wedge\psi_1\wedge\psi_2\), exactly, so its valuation
is still \(-3/4\) by (H22), regardless of the nonintegral entries
of \(W\). There has been no assertion that a general change of
coordinates transforms a product of derivatives by a determinant.
The CM eigenbasis (H12) is chosen first, and the derivatives are
then its dual coordinate directions.

Finally subtract (H14) from (H9). ALP-LIFT-02 identifies the left
side with \(\delta_7\), and the finite 7-adic contributions cancel
exactly. This gives
\[
 \delta_7=\frac{12}{7}\log2-
                    \frac12\log\frac{\det G}{G_B^3},
\]
which is (H15) and completes the proof. \(\square\)

## Exact differential rescaling and the 2-adic limitation

Let \(D_i\) be the invariant derivations dual to \(\omega_i\),
and let \(E_i\) be dual to \(\eta_i^{(2)}\). Formula (H3) gives
the exact operator identities
\[
 D_i=\iota\alpha^{-i}E_i,\qquad
 D_1^{n_1}D_2^{n_2}D_3^{n_3}
  =\iota^{n_1+n_2+n_3}\alpha^{-(n_1+2n_2+3n_3)}
                         E_1^{n_1}E_2^{n_2}E_3^{n_3}.
 \tag{H25}
\]
The associated valuation shift is
\(-\sum_i(2i/7)n_i\). The same identity holds for covariant
derivatives when the connection and local frame are transported
along the same isomorphism: connections are linear in a vector
field, the scaling factors are constant, and the individual
operators are composed in the displayed order. This is a statement
about the same section and connection, not a comparison of two
independently normalized theta frames.

For the abstract DP64 slope certificate at 2, the three directions
of \(\Phi=\{1,2,3\}\) have slopes respectively
\(2/7,4/7,6/7\); the induced type \(\Psi\) has slope zero in
each direction. These numerical slopes equal the valuations of
the coefficients in (H3). The equality gives a concrete geometric
interpretation of the omitted \((12/7)\log2\) in ALP-LIFT-04.
It does not extend the accepted good-model theta theorem to 2.
In particular the trace-one endomorphism
\(w_0=-(\zeta+\zeta^2+\zeta^4)\) has
\(w_0+w_0^\dagger=1\) but \(w_0w_0^\dagger=2\), so one of
its 2-adic conjugates is a nonunit. The odd-prime unit-path
hypotheses used in DP49 do not follow there. The primitive theta
frame, gauge and selected gain still need their own comparison.

## Precise equal-direction Cauchy consequence

This paragraph states exactly what part of a theta estimate is fixed
by the calculation. Let \(F_J\) and \(F_A\) be holomorphic functions
in the universal-cover coordinates dual to \(\omega_i\) and
\(\vartheta_i\), respectively, satisfying
\[
 |F_J(z)|\le C_J\exp\!\left(\frac\pi2
                       \sum_{i=1}^3|z_i|^2/G_i\right),\qquad
 |F_A(t)|\le C_A\exp\!\left(\frac\pi{2G_B}
                       \sum_{i=1}^3|t_i|^2\right)
 \tag{H26}
\]
for positive constants independent of the derivative order.
These are the Chern-frame growth inequalities for bounded-norm
sections of the respective principal theta lines; /root's AM-R004
constructs the specific analytic germ on \(J\) and supplies its
constant separately. Define the logarithmic Cauchy upper bounds,
with equal order \(n\ge1\) in the three chosen CM directions, by
\[
 \mathcal C_J(n)=\log C_J+3\log(n!)+
               \frac{3n}{2}\log(\pi e/n)-\frac n2\log\det G,
\]
and the same expression with \(C_A\) and \(G_B^3\) for
\(\mathcal C_A(n)\). Cauchy's formula on a polydisk of radii
\(R_i^2=nG_i/\pi\) proves the bound for \(J\); replacing the
three \(G_i\) by \(G_B\) proves the other. Subtraction and (H15)
give the exact difference of these **upper-bound expressions**:
\[
 \mathcal C_J(n)-\mathcal C_A(n)
     =\log(C_J/C_A)+n\delta_{7,\{2,7\}}.
 \tag{H27}
\]
Therefore ALP-LIFT-04 implies, for its bare integer certificate
\(D_{\{2,7\}}(n;X)\) and every joint limit
\(n\to\infty\), \(X\to\infty\),
\[
 \frac{D_{\{2,7\}}(n;X)
              -\bigl(\mathcal C_J(n)-\mathcal C_A(n)\bigr)}n
                         \longrightarrow0.
 \tag{H28}
\]
The same identity holds after multiplying both displayed budgets
by the source's common factor 2. A tensor level \(\kappa\) in
the exponent replaces \(\pi\) by \(\kappa\pi\); the added
\((3n/2)\log\kappa\) cancels between the two bounds.

Neither (H27) nor (H28) is an equality between actual derivative
values. The constants can change under arithmetic normalization
of a theta section, and no primitive integral frame or selected
automorphic row is identified by choosing an analytic sup norm.
Thus this closes the order-linear **bare certificate versus
specified diagonal Cauchy metric** comparison in actual CM
coordinates, while leaving the source gain, division error,
bad-prime theta normalization, row content, and kernel matching
as separate inputs to DP44. It gives no shorter valid lift chain
and no universal sign assertion for its full cost.

## Grothendieck and source scope

The smooth models above give an actual relative Picard scheme and
its Hodge bundle, not merely a characteristic-zero CM type. The
Picard representability and smoothness locators are those already
accepted in DP22: FGA V, Bourbaki 232, Theorem 3.1, pp. 148–149;
FGA VI, Bourbaki 236, Corollary 1.7, p. 229, Corollary 2.3,
p. 232, and Proposition 2.10(ii), p. 236. Those source results are
used with their accepted status, not re-proved or claimed newly
scan-checked. The Hodge line is the determinant of the degree-one
de Rham realization of this Picard scheme. Its metric and finite
lattices are evaluated explicitly in (H6)–(H15).

The principal polarization is the homomorphism to the dual Picard
scheme determined by its Poincaré biextension. The trace identity
in (H11) makes the \(E\)-action and its conjugate adjoint, so it
is compatible with that biextension. This is the concrete content
relevant to SGA 7 I, Exposés VII–VIII and the previously accepted
DP49 trace-one construction; no further comparison theorem is
ascribed to those references. No new claim about a lambda-ring,
an unrelated K-theory class, or weights of an automorphic sheaf
is needed for this Hodge determinant calculation.

## References and exact retrievals

* Milne, J. S. (2021, June 12). *Jacobian varieties*. Proposition
  2.2, printed pp. 6–7; Theorem 8.1 and following paragraph,
  printed pp. 27–28. https://www.jmilne.org/math/xnotes/JVs.pdf
  Primary text opened this run; current retrievals
  turn963921859view0, turn794617041view1, turn794617041view2.
* Milne, J. S. (2022, January 2). *Abelian varieties*. Section 16,
  printed p. 31, nondegenerate positive Riemann-form criterion;
  Section 13, printed p. 25, principal-polarization convention.
  https://www.jmilne.org/math/xnotes/AVs.pdf
  Current retrievals turn794617041view0 and turn892289938view0.
* The LMFDB Collaboration. (2026). *Elliptic curve 49.a4: Data*.
  The ec_curvedata row identifies coefficients [1,−1,0,−2,−1],
  CM discriminant −7 and Cremona label 49a1; the ec_mwbsd row
  contains the independent period-area decimal. Retrieved
  November 21, 2026, from
  https://www.lmfdb.org/EllipticCurve/Q/data/49.a4
  Current retrieval turn963921859view1.
* ALP-LIFT-02, ALP-LIFT-03 and ALP-LIFT-04 in
  `work/agents/lift_accounting.md`, with their exact cited
  Colmez–Obus, Wilms, DLMF and fixed-modulus prime-theorem inputs.
* DP_MULT DP22, DP49 and DP64, with intake status unchanged.
  The actual theta gain is not identified with the abstract
  DP64 floor certificate, at 2 or at any other prime.

