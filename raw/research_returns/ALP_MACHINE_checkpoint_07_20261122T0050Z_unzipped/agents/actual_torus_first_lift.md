# ALP-LIFT-09: an actual first compact unitary theta lift from the primitive CM Jacobian

Run ALP_MACHINE; `/root/lift_accounting`, GPT-6 Astra Pro; inherited
reasoning effort not separately exposed. This finding uses the actual
period matrix and reduced theta of AM-R-004, the trace-one section of
ALP-LIFT-07–08, and AM-DO-017–018's finite Heisenberg input. Those
inputs retain their own proof/check records. The arithmetic class
calculation below was also obtained independently by the root agent;
it is recorded once here, as agreed. This is a genuine first theta
lift, not a `thetaG_exists` construction with arbitrary operators.

## The result and its boundary

Put $E=\mathbf Q(\zeta_7)$, $F=E^+$,

\[
 T=\operatorname{U}(1)(E/F),\qquad
 K_0=\{k\in(\widehat{\mathcal O}_E)^\times:k\bar k=1\}.
 \tag{V1}
\]

The following statements hold.

1. $T(\mathbb A_{F,f})=T(F)K_0$, and
   $T(F)\cap K_0=\mu_{14}$. Consequently
   $[T]\simeq(T(F_\infty)\times K_0)/\mu_{14}$ as a compact
   group. For an open subgroup $K\subset K_0$ with
   $K\cap\mu_{14}=1$, its finite component count is exactly
   $h_K=[K_0:K]/14$.
2. For the actual trace-one finite Schwartz vacuum of the Jacobian,
   the whole $K_0$ preserves its one-dimensional eigenline. For
   any fixed honest global unitary Weil splitting, its action is an
   actual finite-image character $\lambda_f$ of $K_0$.
3. Let a homogeneous Fock jet have archimedean character
   $\beta_\infty$, including the vacuum shift for that same
   splitting. If its actual theta value is nonzero, then
   $\beta_\infty\lambda_f$ descends to one automorphic character
   $\chi$ of $T$. With probability Haar measure on $[T]$,
   its theta lift is exactly the original theta function on the
   target group. There is no finite averaging denominator.
4. This gives an explicit nonzero example for the totally definite
   target $\operatorname U(2)$: take two copies of the actual
   Jacobian vacuum and take the $u_1u_3$ derivative in each copy.
   The lift at the identity is
   $(\theta[0;0](0;\tau)c)^2\ne0$, where
   $\Sigma_{\mathrm{tr}}=c\sigma_q$ and
   $\partial_1\partial_3\sigma_q(0)=1$.
5. For an arbitrary finite Schwartz span fixed by a common $K$,
   one fixed finite-coset automorphic input realizes every theta
   function of one fixed archimedean torus weight. Its exact
   squared $L^2([T])$ norm is $h_K$. This is the appropriate
   generalization when Heisenberg translations do not preserve the
   original lattice eigencharacter.

The splitting, Schwartz vector, automorphic character and theta
integral below are actual objects. However, this result does not
identify a chosen character with an independently prescribed
source character, instantiate the old elliptic `VacIn`, construct an
entire iterated tower, or prove its six `AdmS` identities and terminal
mass equation. The target automorphic $L^2$ norm and the whole
integral row lattice are not computed here. In particular, the
displayed nonzero first lift is not a proof that Q1's requested lift
count can be shortened.

## 1. The norm-one torus has one maximal-integral finite class

We give the arithmetic proof, rather than assume a torus class-number
formula. The basic inputs are Minkowski's ideal-class bound and
Dirichlet's unit theorem (Milne, 2020, Theorems 4.3 and 5.1).

The cyclotomic discriminant is $\lvert d_E\rvert=7^5$. Its
Minkowski bound satisfies

\[
 \left(\frac4\pi\right)^3\frac{6!}{6^6}\sqrt{7^5}<5.
 \tag{V2}
\]

For an entirely rational check, use $\pi>3$ and

$\sqrt7<8/3$; the resulting upper bound is
$31360/6561<5$. The order of $2\pmod7$ is three and the
order of $3\pmod7$ is six. Thus every prime ideal over 2 has
norm 8 and every prime ideal over 3 has norm $3^6$. There are no
nontrivial integral ideals of norms 2, 3 or 4. Each ideal class has
an integral representative of norm at most 4 by (V2), so

\[
                    \operatorname{Cl}(\mathcal O_E)=1.
 \tag{V3}
\]

For later reference, $d_F=49$ gives Minkowski bound $14/9<2$,
so $\operatorname{Cl}(\mathcal O_F)=1$ too; the latter is not
needed to prove (V5).

Let $a=\zeta+\zeta^{-1}$ and $b=\zeta^2+\zeta^{-2}$.
They are units, since their common minimal polynomial is

$X^3+X^2-2X-1$. At the embeddings indexed by $1,2,3$,
their signs and the signs of $-1$ are

| Unit | Signs |
|---|---|
| $a$ | $+,-,-$ |
| $b$ | $-,-,+$ |
| $-1$ | $-,-,-$ |

These three sign vectors generate $\{\pm1\}^3$: their
negative-sign vectors $011,110,111$ are independent over
$\mathbf F_2$. Dirichlet gives
$\#(\mathcal O_F^\times/(\mathcal O_F^\times)^2)=8$,
because $F$ is totally real of degree three and its roots of unity
are $\{\pm1\}$. The surjective signature map between these
two groups of order 8 is an isomorphism. Therefore

\[
 \mathcal O_F^{\times,+}=(\mathcal O_F^\times)^2.
 \tag{V4}
\]

Take $t\in T(\mathbb A_{F,f})$. Its fractional
$\mathcal O_E$-ideal $I(t)$ satisfies
$I(t)\overline{I(t)}=\mathcal O_E$. By (V3), write

$I(t)=a_0\mathcal O_E$. Then $a_0\bar a_0$ is a totally
positive unit of $F$. By (V4), it is $b_0^2$ for a unit
$b_0\in\mathcal O_F^\times$. Thus
$\gamma=a_0/b_0\in T(F)$ has the same fractional ideal as

$t$, and $\gamma^{-1}t\in K_0$. This proves

\[
                 T(\mathbb A_{F,f})=T(F)K_0.
 \tag{V5}
\]

A rational element in $K_0$ is an algebraic unit whose conjugates
all have absolute value one. The kernel of the logarithmic unit map
is the roots of unity, so it is in $\mu(E)=\mu_{14}$.
Conversely every such root lies in $T(F)\cap K_0$.
The assertion about $\mu(E)$ also follows directly from the
ramification of the cyclotomic field: an additional prime in the
root's order, a factor 4, or a factor $7^2$ would force an
excluded ramified prime or a subfield of degree greater than six.

It follows that the natural map $T(F_\infty)\times K_0\to[T]$
is onto, with kernel the diagonally embedded $\mu_{14}$.
It is an isomorphism after taking that quotient: the source is
compact and the target Hausdorff. In particular, the automorphic
quotient is compact without an appeal to reduction theory. If
$K\cap\mu_{14}=1$, then

\[
 T(F)\backslash T(\mathbb A_F)/(T(F_\infty)K)
       =K_0/(\mu_{14}K),\qquad
 h_K=[K_0:K]/14.
 \tag{V6}
\]

Such levels exist. For example, intersect any given open subgroup
with the principal congruence subgroup at 3. Roots of order dividing
14 inject under reduction at 3, so this kills the intersection with
$\mu_{14}$. No unknown torus class representatives enter (V6).

## 2. A completely specified honest global splitting exists here

Let $V=E^n$ with its positive definite Hermitian form
$\sum x_i\bar y_i$, and let $W=E$ be the skew-Hermitian
line with coefficient $-\xi$, where
$\xi=(\zeta-\zeta^{-1})/7$. On restriction to $\mathbf Q$,
the tensor alternating form is

\[
 \mathfrak b(x,y)=-\operatorname{Tr}_{E/\mathbf Q}
       \left(\xi\sum x_i\bar y_i\right).
 \tag{V7}
\]

This is precisely the form $E_H=\operatorname{Im}H$ in
AM-DO-018. Use the global additive character with
$\psi_\infty(r)=e^{2\pi ir}$ and
$\psi_f(r)=e^{-2\pi ir}$ on rational numbers, and over $F$
compose it with $\operatorname{Tr}_{F/\mathbf Q}$.
Thus the finite Heisenberg formula below and the chosen tensor
symplectic form have the same convention. This explicit sign
choice is part of this construction; it is not an identification
with an independently fixed source pin.

Here is an explicit choice of the required splitting characters.
Put $K_- =\mathbf Q(\sqrt{-7})$, $\varpi=\sqrt{-7}$ with
positive imaginary part, and let
$\epsilon_7:(\mathcal O_{K_-}/\varpi)^\times\to\{\pm1\}$
be the quadratic character of $\mathbf F_7^\times$.
The Minkowski bound $(2/\pi)\sqrt7<2$ proves that $K_-$
has class number one. For an ideal $\mathfrak a=(a)$ prime
to $\varpi$, set

\[
             u(\mathfrak a)=\epsilon_7(a)\,a/|a|.
 \tag{V8}
\]

This is independent of the generator because the only units are
$\pm1$ and $\epsilon_7(-1)=-1$. It is multiplicative.
Define a unitary idele-class character $\mu_-$ by the
unramified local ideal values (V8), and by

\[
 \mu_{-,\infty}(z)=|z|/z,\qquad
 \mu_{-,\varpi}(v)=\epsilon_7(v)\ (v\text{ a unit}),\qquad
 \mu_{-,\varpi}(\varpi)=i.
 \tag{V9}
\]

To verify rational triviality, write any $a\in K_-^\times$
as $a=\varpi^m b$ with $b$ a $\varpi$-adic unit.
The unramified finite factors multiply to
$\epsilon_7(b)b/|b|$; the ramified factor is
$i^m\epsilon_7(b)$; the infinite factor is
$(i^mb/|b|)^{-1}$. Their product is one. This verifies the
idele-class character, including its ramified normalization.
Its restriction to $\mathbb A_\mathbf Q^\times$ is
$\epsilon_{K_-/\mathbf Q}$: away from 7 the uniformizer
value is the quadratic residue character, at 7 its value on units
is $\epsilon_7$ and its value on 7 is one, and at infinity
it is the sign character. These are the local components of the
quadratic character of discriminant $-7$.

Since $E=FK_-$, put

\[
                   \mu_E=\mu_-\circ N_{E/K_-}.
 \tag{V10}
\]

The norm compatibility of quadratic class-field characters gives
$\mu_E|_{\mathbb A_F^\times}=\epsilon_{E/F}$.
Choose $\chi_W=\mu_E$, and choose
$\chi_V=1$ when $n$ is even and
$\chi_V=\mu_E$ when $n$ is odd. They satisfy exactly

\[
 \chi_W|_{\mathbb A_F^\times}=\epsilon_{E/F}^{\dim W},
 \qquad
 \chi_V|_{\mathbb A_F^\times}=\epsilon_{E/F}^{\dim V}.
 \tag{V11}
\]

Fix the global unitary Weil splitting determined by these data.
The construction and its rational compatibility are the standard
global splitting theorem, in the explicit form stated by Borade
et al. (2025), §§3.1 and 4.1.1. We use only that construction and
the definition of the theta integral from §4.1, not their
root-number or central-$L$-value nonvanishing theorem.
The two unitary actions commute and agree with the canonical
rational splitting on rational points. Thus they give an honest
representation of $G(\mathbb A_F)\times T(\mathbb A_F)$,
where $G=\operatorname U(V)$. All scalar phases below refer to
this fixed representation. In particular they are not phases that
may be adjusted separately on different lattices.

The Schrödinger position space used in (V12) is the rational
Lagrangian supplied by the integral period basis. It need not be
$F$-stable. This causes no change in the representation: taking
the trace of the central coordinate identifies the $F$-Heisenberg
representation with the representation of the underlying rational
symplectic space having the displayed character. A rational change
of polarization transports both the Schwartz representation and
the rational theta distribution. Thus the usual global unitary
splitting acts on this specified rational Schrödinger model, and
the theta sum in that model is indexed by $\mathbf Q^{3n}$.

## 3. The actual finite vacuum and its maximal-compact eigencharacter

Use the actual period coordinates (u=Pz), $Y=\operatorname{Im}\tau$
from AM-R-004. In each copy take
$\delta=(1,1,1)^t$, $\varepsilon=(1,0,1)^t$, and

\[
 \phi_{0,f}(q)=
   -i\,1_{\delta/2+\widehat{\mathbf Z}^{\,3}}(q)
        \psi_f(-q^t\varepsilon/2).
 \tag{V12}
\]

This is the actual input of AM-DO-016/018, not a variable in a
formal theta-family interface. For $n$ copies use its tensor
power. On the rational period vector $t=A+\tau B$, its
Heisenberg action is

\[
 (W_t\phi)(q)=\psi_f(-A^tq+A^tB/2)\phi(q-B).
 \tag{V13}
\]

Let $\widehat\Lambda$ be the completion of the product period
lattice identified with $\widehat{\mathcal O}_E^n$, and put
$w_0=-(\zeta+\zeta^2+\zeta^4)$. Its finite trace-one
Heisenberg eigencharacter (a semicharacter for the operators $W_x$) is

\[
 \alpha_f(x)=\psi_f\bigl(\mathfrak b(x,w_0x)/2\bigr),
       \qquad x\in\widehat\Lambda.
 \tag{V14}
\]

This is an adelic additive-character expression. The notation
$e^{\pi i\mathfrak b(x,w_0x)}$ is not used for arbitrary
adelic $x$. On the rational integral lattice (V14) equals the
sign semicharacter of AM-DO-018, since its value is $\pm1$.
The eigenrelations (V13) for (V12) therefore extend from that
dense rational lattice to all of $\widehat\Lambda$, by
continuity.

The finite eigenspace

\[
 \mathscr V_\Lambda=
 \{\phi:W_x\phi=\alpha_f(x)\phi
                         \text{ for all }x\in\widehat\Lambda\}
 \tag{V15}
\]

inside the finite Schwartz representation has dimension one.
Here is a direct justification tied to the actual theta model.
AM-DO-018's reading map $R$ is injective on finite Schwartz
functions and intertwines (V13) with normalized Mumford translation.
It sends (V15) into the principal theta line on the actual
complex torus, which has dimension one. Formula (V12) supplies
a nonzero vector in (V15), proving equality of dimensions.
For tensor powers the same reading map and the product principal
theta line prove the identical assertion. This is also the usual
selfdual-lattice vacuum uniqueness in the Heisenberg representation.

Every $k\in K_0$ preserves $\widehat\Lambda$, preserves
$\mathfrak b$, and commutes with $w_0$. Consequently it
preserves (V14). Heisenberg covariance of the *fixed* honest Weil
representation shows that it preserves (V15). There is therefore
a unique scalar

\[
 \omega_f(k)\phi_{0,f}^{\otimes n}
       =\lambda_f(k)\phi_{0,f}^{\otimes n}.
 \tag{V16}
\]

The group law makes $\lambda_f$ a character. Unitarity makes
its values have absolute value one; smoothness makes its kernel
open in $K_0$, so its image is finite and consists of roots of
unity. This proves that the scalar is an actual finite-order
character, without guessing a Weil index. For an explicit evaluation
prescription, the value of (V12) at $q=\delta/2$ is $i$;
therefore

\[
 \lambda_f(k)=i^{-n}
   (\omega_f(k)\phi_{0,f}^{\otimes n})
                 (\delta/2,\ldots,\delta/2).
 \tag{V17}
\]

The same line argument applies to every selfdual
$\mathcal O_E$-lattice vacuum of AM-DO-018, because scalar
norm-one integral units preserve that lattice and its trace-one
character. It does not assert that an arbitrary finite Heisenberg
translate has the same character (V14).

## 4. The reduced algebraic jet is an actual homogeneous Fock vector

For one copy put

\[
 K(z,x)=\exp\left(\frac\pi2z^tY^{-1}z
                    +\pi i x^t\tau x+2\pi i x^tz\right),
 \qquad \varphi_{0,\infty}(x)=K(0,x).
 \tag{V18}
\]

The first factor is exactly the Chern reduction used throughout
this run. Define the commuting creation operators

\[
 r_j=-\frac i2\sum_k(Y^{-1})_{jk}
           \left(\partial_{x_k}-2\pi i(\bar\tau x)_k\right).
 \tag{V19}
\]

A direct calculation gives

\[
 r_jK(z,x)=\left(2\pi ix_j+\pi(Y^{-1}z)_j\right)K(z,x)
                  =\partial_{z_j}K(z,x).
 \tag{V20}
\]

Replace the operators by their linear combinations dual to $u=Pz$:

$r_{u_i}=\sum_j(P^{-1})_{ji}r_j$. Thus for every
multi-index $\alpha$,

\[
 \varphi_{\alpha,\infty}(x)
    =\left.\partial_u^\alpha K(P^{-1}u,x)\right|_{u=0}
    =r_u^\alpha\varphi_{0,\infty}(x).
 \tag{V21}
\]

It is a polynomial times a positive Gaussian, hence Schwartz.
The real torus $T(F_\infty)\simeq(S^1)^3$ preserves the
positive complex polarization. Its action preserves the vacuum
line and acts diagonally on the three CM creation directions.
One may check preservation directly: the differentiated real
Heisenberg operator with parameter $(A,B)$ acts on the vacuum
as $-2\pi i(A+\tau B)^t x$. Its complex annihilator is therefore
the kernel of $A+\tau B$, which is preserved by the CM torus.
Its unique Schwartz vacuum line is consequently preserved.
Consequently a monomial of fixed CM multidegree is an eigenvector.
For $n$ copies and a multi-index $\alpha=(\alpha_{ij})$,
define its actual eigencharacter by

\[
 \omega_\infty(t)\varphi_{\alpha,\infty}
      =\beta_\alpha(t)\varphi_{\alpha,\infty}.
 \tag{V22}
\]

This fixes the sign and the vacuum character for the splitting in
§2. The action on creation operators determines the relative
weights, while the action on the vacuum supplies its scalar shift.
No replacement of (V22) by an unshifted polynomial degree is made.
The eigenspace assertion can equivalently be checked from (V19):
Heisenberg covariance transports the holomorphic creation space
by the three CM characters, and the simultaneous monomials have
the corresponding characters multiplied by the vacuum character.

For clarity, the actual Gaussian norm is also explicit. With
Lebesgue measure in the fixed rational position coordinates,

\[
 \|\varphi_{\alpha,\infty}\|_2^2
  =\det(2Y)^{-n/2}\,
       \prod_{i,j}\alpha_{ij}!\left(\frac\pi{G_i}\right)^{\alpha_{ij}}.
 \tag{V23}
\]

Indeed the vacuum norm is $\det(2Y)^{-n/2}$. From (V19),
$[r_{u_i}^{*},r_{u_j}]=\pi\delta_{ij}/G_i$, and
$r_{u_i}^{*}\varphi_{0,\infty}=0$. Moving annihilation
operators past creation operators proves (V23) by induction.
The finite vector (V12) has norm one, because its support has
volume one and every nonzero value has absolute value one.
Thus (V23) is also the global Schwartz norm for this input.

The theta series at the identity is

\[
 \vartheta_\alpha(1,1)
   =\sum_{q\in\mathbf Q^{3n}}
       \phi_{0,f}^{\otimes n}(q)\varphi_{\alpha,\infty}(q)
   =\left.\partial_u^\alpha
                  R(\phi_{0,f}^{\otimes n})(u)\right|_{u=0}.
 \tag{V24}
\]

This is an equality of an actual adelic theta sum and an actual
reduced CM derivative. Differentiation is legitimate because the
finite support lies in a bounded-denominator rational lattice and
the positive Gaussian gives locally normally convergent series.

AM-DO-018 gives

\[
 R(\phi_{0,f}^{\otimes n})(u)
   =\theta[0;0](0;\tau)^n\prod_{j=1}^n\Sigma_{\mathrm{tr}}(u_j).
 \tag{V25}
\]

ALP-LIFT-08 gives $\sigma_q(u)=u_1u_3-u_2^2+\text{higher terms}$,
and AM-DO-015 identifies
$\Sigma_{\mathrm{tr}}=c\sigma_q$ with $c\ne0$.
Taking $\alpha_{1j}=\alpha_{3j}=1$,
$\alpha_{2j}=0$ for every $j$, gives the exact nonzero value

\[
             \vartheta_\alpha(1,1)
                  =(\theta[0;0](0;\tau)c)^n\ne0.
 \tag{V26}
\]

For this input the norm (V23) is
$\det(2Y)^{-n/2}(\pi^2/(G_1G_3))^n$.
Neither (V26) nor that norm replaces the common period by an
unrecorded scalar.

## 5. One actual character gives the nonzero theta lift

For the fixed splitting, write

\[
 \vartheta_\alpha(g,t)=
       \sum_q(\omega(g,t)\varphi_\alpha)(q),
 \qquad
 \varphi_\alpha=\phi_{0,f}^{\otimes n}
                           \otimes\varphi_{\alpha,\infty}.
 \tag{V27}
\]

The theta function is left invariant under rational points, by
the rationally compatible global Weil construction. Its two group
actions commute. Equations (V16) and (V22) therefore give

\[
 \vartheta_\alpha(g,t_\infty k)
       =\beta_\alpha(t_\infty)\lambda_f(k)
                            \vartheta_\alpha(g,1).
 \tag{V28}
\]

For $\zeta\in\mu_{14}$, the diagonal element is rational.
Evaluating (V28) at $g=1$ and using the already established
nonzero value (V26) proves

\[
                  \beta_\alpha(\zeta)\lambda_f(\zeta)=1.
 \tag{V29}
\]

This is precisely the finite-root-unit compatibility which is
sometimes lost if only the polynomial degree is retained. Its
proof uses the actual theta series and rational splitting; it is
not an imposed compatibility condition assumed for a hypothetical
lift.

By (V5)–(V6) and (V29), the formula

\[
 \chi_\alpha(\gamma t_\infty k)
        =\beta_\alpha(t_\infty)\lambda_f(k),
 \quad \gamma\in T(F),\ t_\infty\in T(F_\infty),\ k\in K_0,
 \tag{V30}
\]

is well-defined and is a continuous unitary automorphic character.
All automorphic forms on this anisotropic torus are cuspidal,
since a torus has no proper parabolic subgroups. Equation (V28),
together with rational automorphy and (V5), now holds for every
adelic $t$ in the form

\[
            \vartheta_\alpha(g,t)
                   =\chi_\alpha(t)\vartheta_\alpha(g,1).
 \tag{V31}
\]

Choose Haar measure on $[T]$ of total mass one and use the
theta-lift convention with a conjugated automorphic input. Then

\[
 \boxed{\Theta(\varphi_\alpha,\chi_\alpha)(g)
   =\int_{[T]}\vartheta_\alpha(g,t)\overline{\chi_\alpha(t)}\,dt
   =\vartheta_\alpha(g,1).}
 \tag{V32}
\]

There is no limiting procedure, convergence regularization, or
unproved nonvanishing theorem in this calculation. The quotient is
compact; (V31) makes the integral elementary. The source character
has $L^2$ norm one. Taking $n=2$ proves the claimed actual
nonzero $U(1)\to U(2)$ lift. With a different fixed Haar measure,
the right side is multiplied by its explicitly retained total
volume.

The common-period-normalized identity value is exactly one by
(V26). This identifies one actual nonzero matrix value. It is not
an assertion that the whole automorphic function is primitive in
the source's mass-weighted integral row module, and no valuation
is assigned to a transcendental period itself.

## 6. General finite inputs: an exact common first-image projector

This extension explains exactly what remains for translated inputs.
Let $\mathcal S$ be a finite-dimensional span of finite Schwartz
functions. Let $K\subset K_0$ fix every vector in
$\mathcal S$, and shrink it at 3 so that
$K\cap\mu_{14}=1$. Such a common open subgroup exists by
smoothness and finite dimensionality. Keep any fixed homogeneous
archimedean weight $\beta$. The statement applies to any
finite-dimensional subspace of that weight, not only a single
monomial. Write $h=h_K$.

The identity finite component of $[T]/K$ is the image of
$T(F_\infty)K$, and it is an injective copy of
$T(F_\infty)$, because $K\cap\mu_{14}=1$. Define

\[
 f_{K,\beta}(t)=
 \begin{cases}
 h\,\beta(t_\infty),&[t]=[t_\infty k],\ k\in K,\\
 0,&\text{on the other finite components}.
 \end{cases}
 \tag{V33}
\]

This is a well-defined smooth automorphic form of weight $\beta$,
with

\[
             \|f_{K,\beta}\|_2^2=h,
                 \qquad \|f_{K,\beta}\|_\infty=h.
 \tag{V34}
\]

Each component has measure $1/h$. For any
$\phi_f\in\mathcal S$ and any archimedean vector of weight
$\beta$, the theta function on the identity component is
$\beta(t_\infty)\vartheta_\phi(g,1)$. Hence

\[
                \boxed{\Theta(\phi,f_{K,\beta})(g)
                           =\vartheta_\phi(g,1).}
 \tag{V35}
\]

The same input $f_{K,\beta}$ works for the entire specified
finite span. If the source automorphic input is required to have
norm one, replacing it by $h^{-1/2}f_{K,\beta}$ multiplies
the output by $h^{-1/2}$. Thus the exact added normalization
cost is $\frac12\log h$ in logarithmic norm, not an
unspecified projection constant.

There is also an explicit finite character decomposition. Set
$A=K_0/K$, with its embedded subgroup $\mu_{14}$.
Let

\[
 \mathcal X_\beta=
   \{\eta\in\widehat A:
               \eta|_{\mu_{14}}=\beta^{-1}|_{\mu_{14}}\}.
 \tag{V36}
\]

Every character of a subgroup of a finite abelian group extends:
one may extend successively over cyclic generators by choosing
the necessary roots of unity. The extensions form a torsor for
$\widehat{A/\mu_{14}}$. Thus
$\#\mathcal X_\beta=h$, all its finite values are roots
of unity, and each

$\chi_\eta(t_\infty k)=\beta(t_\infty)\eta(k)$
descends to $[T]$. Finite character orthogonality gives

\[
                 f_{K,\beta}=\sum_{\eta\in\mathcal X_\beta}\chi_\eta.
 \tag{V37}
\]

No coefficient $1/h$ occurs in (V37). For one component, choosing
representatives $a\in A/\mu_{14}$ gives the exact projection

\[
 \Theta(\phi,\chi_\eta)(g)
   =\frac1h\sum_{a\in A/\mu_{14}}
                   \overline{\eta(a)}\vartheta_\phi(g,a).
 \tag{V38}
\]

The summand is independent of representative because rational-root
automorphy cancels the two characters. Formula (V38) displays the
only averaging denominator; its $p$-adic contribution is
at worst $v_p(h)$ once the specified theta values have actually
been placed in a common integral lattice. If (V35) is nonzero,
at least one of the $h$ irreducible-character lifts in (V37)
is nonzero. This is a consequence for the explicitly specified
finite family; it is not nonvanishing for a freely prescribed
Hecke character.

## 7. What this closes, and what it does not close

The trace-one scalar torus argument supplies an actual nonzero
first compact lift with the primitive mixed CM type. It also
supplies a common actual first-image map for any selected finite
Schwartz span at one weight, with an exact finite-index
normalization. In that limited first-lift setting, existence of an
automorphic input is no longer a merely formal interface.

For the base vacuum, the finite and archimedean input normalizations
are (V12), (V23), and the norm-one character in (V30). The unknown
target automorphic mass norm is a different quantity. The exact
finite character (V16) is fixed by the global splitting; identifying
it with a source-prescribed determinant-root character requires
the corresponding local calculation. AM-DO-020 performs that
calculation at relative split places, including 11, for the stated
unramified splitting. No omitted ramified phase is declared equal
to one here.

For DP59/DP65's permitted translated sections, applying §6 requires
an actual common stabilizer $K$, the exact archimedean weight,
and the source's allowed automorphic input space. An unrestricted
finite Schwartz span may be larger than the prescribed one. The
finite-coset input in (V33) is generally a sum of characters, and
its cost (V34) must be retained if the source requires unit norm.
The accepted DP59/DP65 field-span and sharp-jet results are not
re-proved or promoted here to a full iterated-image statement.

Nothing in (V32) or (V35) supplies the later branching map,
all-degree `ClsK.Core` with its specified phases, simultaneous
terminal mass identities, the global `MainX` laws, or a changed
DP44 cost with all $g_j,e_j,H$ identified. Those are the
remaining gates for Q1's requested shorter tower.

## Primary references actually consulted

Borade, N., Franzel, J., Girsch, J., Yao, W., Yu, Q., & Zelingher, E.
(2025). *On tori periods of Weil representations of unitary groups*
(arXiv:2402.16808v2). https://arxiv.org/html/2402.16808v2.
Exact used locators: §3.1, tensor alternating form and Heisenberg
representation; §3.1.1, splitting characters; §4.1, rational global
splitting, theta sum, and conjugated-input theta integral;
§4.1.1, global character restrictions and tensor-product splitting.
No nonvanishing theorem from that paper is used.

Milne, J. S. (2020). *Algebraic number theory* (Version 3.08).
https://www.jmilne.org/math/CourseNotes/ANT.pdf.
Exact used locators: Theorem 4.3, printed pp. 70–71, Minkowski
bound; Theorem 5.1, printed p. 85, unit rank; the logarithmic
kernel discussion in §5, printed pp. 86–87.

Prasad, D. (2000). Theta correspondence for unitary groups.
*Pacific Journal of Mathematics, 194*(2), 427–438.
https://www.math.iitb.ac.in/~dprasad/pacific.pdf.
Used as an independent convention check: §1, printed pp. 427–428,
the dependence on two splitting characters and the passage from
metaplectic to honest unitary representations.

## Check status

The author read the complete saved proof, including the arithmetic
class and character construction, finite trace-one eigenline,
Chern/Fock derivative and Gaussian norm calculation, single-character
integral, and general finite-coset projector. The exact algebra
certificate in actual_torus_certificate.py passed. Actual check
events and their scope are recorded in lift_accounting_CHECK_EVENTS.tsv.
No Lean compilation or formal proof is claimed.
