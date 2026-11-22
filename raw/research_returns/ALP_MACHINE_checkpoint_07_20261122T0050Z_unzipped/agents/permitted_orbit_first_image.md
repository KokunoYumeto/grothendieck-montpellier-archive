# ALP-LIFT-10: the permitted half-torsion orbit in an actual first theta image

Run ALP_MACHINE; /root/lift_accounting, GPT-6 Astra Pro; inherited
effort not separately exposed. This result uses accepted DP59 and
DP62 for the algebraic permitted sections and their canonical
normalizations. It does not re-prove their integral span or jet
separation. It uses ALP-LIFT-09 for the actual global unitary
splitting, first-lift integral, and torus class calculation, and
AM-DO-020–021 for the fixed split and ramified compact phases.

## Statement

Let $J$, $L$, $s_q$, $\sigma_q$, $\Lambda$, and $H$ have the
normalizations of ALP-LIFT-08–09. Thus $\sigma_q$ is the actual
Chern-reduced germ of $s_q$ with leading term $u_1u_3-u_2^2$,
and $s_q$ is primitive at every odd prime other than7. Put
\[
 \delta_7^2=-7,\qquad
 \alpha=(1+2\delta_7)^e,\qquad M=29^e,\qquad \kappa=M^2,
 \qquad e\ge1.
 \tag{O1}
\]
Here $\delta_7=1+2(\zeta+\zeta^2+\zeta^4)$, so the choice is
exactly DP59's actual level. For every permitted root
$t'\in J[\alpha^2]$, let $s_{t'}$ be the canonical symmetric
theta translate of $[M]^*s_q$ from DP59.

Fix an even positive integer $n$, and use the actual compact pair
$T=U(1)(E/F)$ and $G=U(I_n)(E/F)$, with the honest splitting
$\chi_V=1,\chi_W=\mu_E$ of ALP-LIFT-09. Let $P$ be any
polynomial differential operator in the $3n$ algebraic differential
coordinates, homogeneous of total degree $N$ and of a fixed
degree at each of the three CM embeddings. All such polynomials
have one fixed archimedean torus weight, denoted $\beta$; it
includes the actual vacuum character.

There is one explicitly defined automorphic input $f_{M,\beta}$
on $T$, independent of the allowed tuple
$\mathbf t'=(t'_1,\ldots,t'_n)$ and of $P$ inside this weight,
such that an actual theta lift has identity value
\[
 \Theta(\phi_{\mathbf t',P},f_{M,\beta})(1)
  = C^n M^{-N}
       P(\partial_u)
         \left(\prod_{j=1}^n
                    \sigma_{s_{t'_j}}(u_j)\right)_{u=0},
 \qquad C=\theta[0;0](0;\tau)c.
 \tag{O2}
\]
The notation $\sigma_{s_{t'}}$ denotes the specified
Chern-reduced germ of the algebraic section $s_{t'}$, in the
line of curvature $\kappa H$. The constant $c\ne0$ is fixed by
$\Sigma_{\rm tr}=c\sigma_q$; it is independent of $M$ and the tuple.
The finite Schwartz vector in (O2) is an explicitly specified
Heisenberg translate of the fixed vacuum, with coefficients roots
of unity and finite $L^2$ norm one.

The automorphic input is supported on one finite component and has
the exact norms
\[
 \|f_{M,\beta}\|_2^2=h_M
       =56^2\,29^{3(e-1)},\qquad
 \|f_{M,\beta}\|_\infty=h_M.
 \tag{O3}
\]
Consequently its normalization to norm one multiplies the
right side of (O2) by $h_M^{-1/2}$ and has logarithmic cost
\[
 \log\sqrt{h_M}
      =\frac32\log M+\log56-\frac32\log29.
 \tag{O4}
\]
Every prime divisor of $h_M$ lies in $\{2,7,29\}$, so both
the projection and norm normalization have zero valuation cost
at11, and at every prime outside this displayed exceptional set. At the DP59 levels $M=O(N)$, the new logarithmic norm
cost is $O(\log N)$.

This is a simultaneous realization of the specified fixed-weight
jet functionals by actual first theta lifts. It is not an
identification of the entire section module with an automorphic
representation, an assertion about one freely prescribed
irreducible torus character, or a construction of the later
definite lifts.

## 1. Exact multiplication and translation of the actual reduced section

Write
\[
 (U_x^H F)(v)
       =\exp\bigl(-\pi H(v,x)-\pi H(x,x)/2\bigr)F(v+x).
 \tag{O5}
\]
This is the normalized Mumford translation used in AM-DO-017–018.
The rigidified multiplication isomorphism
$[M]^*L\simeq L^{M^2}$ carries the reduced section to
$\sigma_q(Mu)$ exactly. Indeed the pullback Hermitian form is
$M^2H$, its semicharacter is
$\alpha_{\rm tr}(M\lambda)=\alpha_{\rm tr}(\lambda)^{M^2}$,
and the two normalized Appell–Humbert presentations have
the same multiplier and the same origin rigidification. Their
isomorphism is therefore the identity in these presentations;
no extra quadratic exponential appears.

Choose a rational period representative
$r\in\kappa^{-1}\Lambda$ of $t'$, and put $x=Mr$.
The equality of the two translated functions is immediate from
(O5):
\[
 U_r^{M^2H}\bigl(\sigma_q(Mu)\bigr)
                 =(U_x^H\sigma_q)(Mu).
 \tag{O6}
\]
Both linear exponential terms are
$-\pi M^2H(u,r)$, both constant exponential terms are
$-\pi M^2H(r,r)/2$, and both arguments are $Mu+Mr$.

The canonical symmetric lift in DP59 differs from $U_r^{M^2H}$
by an explicitly determined sign only. To see this, let
$\iota$ be normalized inversion in the line presentation.
Then
\[
 \iota U_r^{M^2H}\iota^{-1}=U_{-r}^{M^2H}
                       =(U_r^{M^2H})^{-1}.
 \tag{O7}
\]
Since the alternating self-pairing is zero,
$(U_r^{M^2H})^\kappa=U_{\kappa r}^{M^2H}$, and the latter
is the scalar
$\alpha_{\rm tr}(\kappa r)^\kappa
 =\alpha_{\rm tr}(\kappa r)\in\{\pm1\}$.
Because $\kappa$ is odd, multiplying $U_r^{M^2H}$ by
\[
                        \epsilon_r=\alpha_{\rm tr}(\kappa r)
 \tag{O8}
\]
gives an operator whose $\kappa$-th power is one and which
still satisfies (O7). The uniqueness of the symmetric
finite-order lift, already proved in DP59 §4, identifies it
with the permitted lift. In particular,
\[
                 \sigma_{s_{t'}}(u)
                    =\epsilon_r(U_x^H\sigma_q)(Mu).
 \tag{O9}
\]
Changing the representative gives the same section by that
uniqueness. All phases introduced in (O8) are algebraic units.

The point represented by $x$ lies in the smaller subgroup
\[
                        [M]J[\alpha^2]=J[\alpha]\subset J[M].
 \tag{O10}
\]
The inclusion follows from
$\alpha M=\alpha^2\bar\alpha$ and
$\alpha\bar\alpha=M$. Equality follows from the accepted DP59
kernel calculation: the kernel of $[M]$ on $J[\alpha^2]$ is
$J[\alpha]$, so the image has the same order as $J[\alpha]$.
This is where the actual permitted half-orbit is used; replacing
it by all of $J[M]$ would lose the sharper level below.

Taking tensor products of (O9), and using homogeneity of $P$,
gives the all-degree identity
\[
 M^{-N}P(\partial_u)\prod_j\sigma_{s_{t'_j}}(u_j)\big|_0
   =\left(\prod_j\epsilon_{r_j}\right)
            P(\partial_v)\prod_j(U_{x_j}^H\sigma_q)(v_j)\big|_0.
 \tag{O11}
\]
The factor $M^{-N}$ from the source therefore cancels the
multiplication pullback exactly.

## 2. The exact finite Schwartz family

Let $\phi_{0,f}$ be ALP-LIFT-09 (V12). For the selected representatives
define
\[
 \phi_{\mathbf t',f}
       =\bigotimes_{j=1}^n\bigl(\epsilon_{r_j}W_{x_j}\phi_{0,f}\bigr).
 \tag{O12}
\]
The $W_x$ are the explicit finite operators (V13).
Their translates and modulation factors preserve compact support
and local constancy. Their nonzero values have absolute value one
and are roots of unity, because all period coefficients are
rational. They are unitary, so (O12) has norm one.

The exact reading identity of AM-DO-018 and
$R\phi_{0,f}=C\sigma_q$ give
\[
 R\phi_{\mathbf t',f}(v)
       =C^n\left(\prod_j\epsilon_{r_j}\right)
                      \prod_j(U_{x_j}^H\sigma_q)(v_j).
 \tag{O13}
\]
There is one common period $C^n$ for the whole family. Use the
actual archimedean Schwartz vector
\[
                   \phi_{P,\infty}
                         =P(r_u)\varphi_{0,\infty}^{\otimes n},
 \tag{O14}
\]
with the creation operators of ALP-LIFT-09 (V19)–(V21).
Its actual torus character is $\beta$. Formula (V20) identifies
the theta sum at the identity with the derivative of (O13).
Thus the identity value on the right side of (O2) is already
an actual theta series. It remains to realize it by one common
automorphic input with its normalization controlled.

## 3. The fixed compact vacuum character for even rank

For the fixed splitting $\chi_V=1$ and even $n$, the scalar
norm-one compact character of the base vacuum is
\[
                  \lambda_f(k)=\epsilon_7(k_7)^{n/2},
 \tag{O15}
\]
where $\epsilon_7(t)$ is the residue of $t$ in
$\{1,-1\}$ at the unique ramified prime over7.
All other finite local factors are trivial.

Here is the precise justification of the unramified part, supplementing
AM-DO-020–021's calculations. At every odd unramified quadratic
place, the norm on integral units is surjective. For example the
residue norm is surjective, and successive correction in the
principal units uses the surjective residue trace. Choose a unit
of norm $-1$. It gives an integral primitive isotropic vector of
$I_2$; an integral pairing partner can be adjusted, using that
2 is a unit, to make an integral hyperbolic pair. Therefore
$I_n$ is an integral orthogonal sum of hyperbolic planes.
Pan (2001), Lemma 6.2, printed p.197, gives scalar
$\alpha(t)\beta^Y(t)=\chi_V((t-1)\delta)=1$
against each such plane, with the identity element treated directly.
His tensor identity (3.6.e) gives one for their sum.
The selfdual trace-lattice normalization is the same lattice-model
normalization identified in AM-DO-021 §1.

At relative split places, including2, AM-DO-020 gives the exact
split determinant-root scalar. It is one on the compact torus
when $\chi_V=1$. The only remaining ramified place is7, and
AM-DO-021 (DO21.12) gives exactly (O15). The simultaneous sign
transport in ALP-LIFT-09 does not change this residual real sign.
Thus the fixed compact subgroup
\[
                  K_7^+=\ker\epsilon_7\subset K_{0,7}
 \tag{O16}
\]
has index2 and fixes the vacuum for every even $n$. When
$4\mid n$ this restriction is redundant, but retaining it gives
one uniform exact level and cost for all even ranks.

## 4. The permitted half-orbit is fixed at level $M$, not $M^2$

The prime29 splits completely in $E/\mathbf Q$. There are
three places $v$ of $F$ above29, each with
$F_v=\mathbf Q_{29}$ and
$E_v=F_v\times F_v$. Since the ideals $(\alpha)$ and
$(\bar\alpha)$ are coprime and their product is $(M)$, the
two valuations of $\alpha$ in each relative pair are $(e,0)$
in one order.

The actual lattice decomposes at such a place into its two
relative split isotropic summands,
\[
                      \Lambda_v=X_v\oplus Y_v.
 \tag{O17}
\]
Both are stable under $w_0$ and the scalar norm-one torus. A
point of $J[\alpha]$ can be represented modulo $\Lambda_v$
entirely in the summand on which $\alpha$ has valuation $e$,
with its coordinate in $29^{-e}X_v$ (or in
$29^{-e}Y_v$ in the other order).

Replacing a representative by an integral vector changes
$W_x\phi_{0,f}$ by a fixed root of unity: this follows from
the Heisenberg multiplication law and the lattice vacuum
eigenrelation. Such a scalar does not affect its stabilizer.
It is therefore legitimate to use the pure isotropic
representative at each place when computing the common
stabilizer of the actual vectors (O12).

Take
\[
 K_v(M)=\{t=(a,a^{-1})\in K_{0,v}:
                                  a\equiv1\pmod{29^e}\}.
 \tag{O18}
\]
For $x\in29^{-e}X_v$ and $t\in K_v(M)$, put
$d=(t-1)x$. Then $d\in X_v\subset\Lambda_v$.
Both $x$ and $d$ lie in the same isotropic space, so
\[
                  \mathfrak b(x,d)=0,\qquad
                  \mathfrak b(d,w_0d)=0.
 \tag{O19}
\]
The lattice eigencharacter of $d$ is consequently one, and
the half-pairing in the multiplication law is zero. Thus
\[
                         W_{tx}\phi_{0,f}=W_x\phi_{0,f}.
 \tag{O20}
\]
The base compact scalar is one by (O15). Heisenberg covariance
therefore proves that $K_v(M)$ fixes every allowed translated
vacuum exactly. The identical argument applies when the
denominator lies in $Y_v$.

At every finite prime not dividing29, the vector $x$ is integral
in the trace lattice, so $W_x\phi_{0,f}$ is already a scalar
multiple of the base vacuum. Every compact element fixing the
base vacuum fixes that translate. Consequently the explicit
product subgroup
\[
 K_M=K_7^+\times\prod_{v\mid29}K_v(M)
             \times\prod_{v\nmid7\cdot29}K_{0,v}
 \tag{O21}
\]
fixes every finite vector (O12), and their entire span, for
every allowed tuple.

## 5. Exact finite index and automorphic input

The three factors at29 have indices
\[
 [K_{0,v}:K_v(M)]
       =\#(\mathbf Z/29^e\mathbf Z)^\times
       =28\,29^{e-1}.
 \tag{O22}
\]
The index at7 is2. Reduction at29 is injective on
$\mu_{14}$, since its order is prime to29, so
$K_M\cap\mu_{14}=1$. No extra auxiliary prime is required.
ALP-LIFT-09 (V6) now gives
\[
 h_M=\frac{2(28\,29^{e-1})^3}{14}
       =56^2\,29^{3(e-1)}.
 \tag{O23}
\]
In particular $v_{11}(h_M)=0$.

Define $f_{M,\beta}$ by ALP-LIFT-09 (V33), with $K=K_M$:
it equals $h_M\beta(t_\infty)$ on the identity finite
component and zero on all other finite components. The
definition is unambiguous because $K_M$ kills the rational
root-unit stabilizer. That component has measure $1/h_M$.
Consequently
\[
 \Theta(\phi_{\mathbf t',f}\otimes\phi_{P,\infty},
                             f_{M,\beta})(g)
       =\vartheta_{\mathbf t',P}(g,1).
 \tag{O24}
\]
This is a genuine automorphic theta integral for the fixed
global splitting. Equations (O11), (O13), and (O14) give
(O2) on setting $g=1$. The elementary measure calculation
in (V34) gives (O3), and taking its square root gives (O4).
The same input works simultaneously for every allowed tuple
and every $P$ in the specified torus weight.

The input may be decomposed into $h_M$ automorphic characters
by (V36)–(V38). Its finite coefficients are $h_M$ times roots
of unity. Individual-character projections divide by $h_M$;
the simultaneous input (O24) has no such denominator.
Even after normalization to norm one, $h_M^{-1/2}$ is an
11-adic unit after a finite coefficient-field extension. Thus
the algebraic value in (O2), after removing the retained common
period $C^n$, has exactly the same 11-adic valuation with the
unit-norm input as it had before that normalization. This
assertion is about the displayed value; it does not assert
primitivity of every target row or compute the target mass norm.

For $n=2$ this applies directly to pairs of DP59's ordinary
allowed sections, including any homogeneous two-column
differential chosen on ordinary powers of $J$. Tensoring a
fixed number of ordinary factors does not change the torus
level index (O23).

## 6. Extracting one norm-one character without losing the local valuation

The simultaneous input is useful for realizing a whole specified
finite span. For an existence statement one may instead extract
one of its irreducible-character components with norm one. The
finite torus $K_0$ preserves $J[\alpha]$, since its scalar
integral action commutes with $\alpha$. Therefore, for every
$k\in K_0$, Heisenberg covariance gives
\[
 \omega_f(k)\phi_{\mathbf t',f}
       =\lambda_f(k)\bigotimes_j
                    \bigl(\epsilon_{r_j}W_{kx_j}\phi_{0,f}\bigr).
 \tag{O26}
\]
The tuple $(kx_j)_j$ still belongs to the permitted half-orbit.
Choosing preimages under $[M]:J[\alpha^2]\to J[\alpha]$
and their rational period representatives identifies (O26) with
an allowed tuple's vector, up to a root of unity. In particular,
there is still the same common period $C^n$.

Let $f_{M,\beta}=\sum_\eta\chi_\eta$ be (V37). At the
identity, each normalized character lift is an average
\[
 C^{-n}\Theta(\phi_{\mathbf t',P},\chi_\eta)(1)
       =\frac1{h_M}\sum_{a\in K_0/(\mu_{14}K_M)}
                   \overline{\eta(a)}\,J_a,
 \tag{O27}
\]
where every $J_a$ is the normalized Chern jet of an allowed
tuple, multiplied by a root of unity. Thus all these values
are algebraic in a finite common coefficient field. The only
displayed averaging denominator has valuations
\[
 v_2(h_M)=6,\qquad v_7(h_M)=2,\qquad
 v_{29}(h_M)=3(e-1),\qquad v_p(h_M)=0\quad(p\nmid2\cdot7\cdot29).
 \tag{O28}
\]
These are exact costs of the written projection formula; actual
cancellation may improve them.

Since summing (O27) over all characters recovers the value in
(O2), the ultrametric inequality has the following useful
consequence. If a nonzero normalized Chern jet in (O2) has
$p$-adic valuation $V$, then at least one actual character
lift in (O27) has valuation at most $V$. Every such input
character has probability-Haar $L^2$ norm one. At11, and
indeed at every $p\nmid2\cdot7\cdot29$, (O27) additionally
lies in the local integer-ring span of the displayed Chern-jet values.
Neither assertion identifies in advance which character occurs.

There is an exact archimedean comparison as well. If the allowed
normalized Chern jets in this fixed orbit are all bounded by
$B_P$, then each average in (O27) has absolute value at most
$B_P$: its $h_M$ coefficients have modulus $1/h_M$. A bound
of this kind follows directly from the actual Gaussian estimate
for $\sigma_q$. If
\[
 |\sigma_q(u)|\le A\exp\left(\frac\pi2\sum_i|u_i|^2/G_i\right),
 \tag{O29}
\]
then (O5) preserves this same envelope exactly: expanding the quadratic
form at $u+x$ cancels its cross term and its $H(x,x)$ term
against the two real translation exponents. For
$P=\sum_\nu a_\nu D^\nu$ on $n$ copies, polydisk Cauchy gives
\[
 B_P=A^n\sum_\nu|a_\nu|\,\nu!
       \prod_{i,j:\nu_{ij}>0}
           \left(\frac{\pi e}{\nu_{ij}G_i}\right)^{\nu_{ij}/2}.
 \tag{O30}
\]
The multiplication factor $M^N$ has already canceled in
(O11). This is a bound for these identity values; it is not
an evaluation of the target automorphic $L^2$ norm or of all
source row-operator norms.

Thus two exact normalizations are available. One common input
for the entire span has norm cost (O4). An extracted character
has norm one, while its finite projection formula has the
explicit denominator (O28). The latter has total logarithmic
size $\log h_M=3\log M+O(1)$, supported at the specified
exceptional primes. Neither bookkeeping choice makes these
costs disappear from a subsequent global comparison.

## 7. Exact source-gauge transfer and explicit sharp first-image values

### The source formal gauge is now matched on ordinary powers

Equations (O2), (O9), and (O11) identify the actual
Chern-reduced germs of the permitted algebraic sections with
an actual first theta integral. AM-K018 now proves the required
comparison with the source's canonical formal gauge:
\[
 \text{the source selected formal jet in its canonical gauge}
   =\text{the normalized Chern jet appearing in (O2)}.
 \tag{O25}
\]
This is the same full-$\mathcal O_E$ canonical gauge in the same
integral biextension frame, including the DP47 normalized integral
unit. The difference of two such gauges is adjoint-balanced
bilinear in group logarithms, and no pair of ordinary holomorphic
labels $1,2,3$ is opposite modulo7. AM-K018 consequently identifies
the Chern frame exactly with $f_sU^\kappa B^{-\kappa}$, with no
quadratic-exponential ambiguity. Its statement applies to all
ordinary powers and every tensor level and permitted section here.
I read that full proof and the consequential source clauses;
the independent review is review_kummer_source_gauge.md.

This comparison does not say that the reduced frame is integral.
It identifies the nonintegral primitive-kernel factor with the
precise source normalization whose derivative estimates were
proved in DP54/DP58/DP59.

### One actual sharp harmonic first image

Take $n=2$, and retain the first-row two-column harmonic
operator $P_{a,b}$ of DP51/DP58, with
\[
 a=11^q,\qquad b=121\cdot11^q,\qquad
 N=a+b=122\cdot11^q,\qquad V_q=(11^q-1)/10 .
 \tag{O31}
\]
Use the global algebraic eigenvectors dual to
$\omega_3$ and $\omega_2$ for its two directions.
Its supported monomials all have total degree $a$ in the
first direction and total degree $b$ in the second,
across the two columns. Hence it has one CM torus weight,
even though it has several differential monomials. The
DP49 unit-arrow eigenvectors differ from these actual
algebraic CM eigenvectors by diagonal 11-adic units.
Homogeneity in each label multiplies the entire selected
harmonic value by a single unit, so the sharp valuation is
unchanged. No algebraicity of those display-normalization
comparison units is assumed or needed; the Fock polynomial
itself uses the global algebraic directions just specified.

DP59, used as an accepted theorem, supplies $M=29^e=O(N)$
and an allowed pair for which the source-normalized derivative
has valuation exactly $V_q$. Equation (O25) transfers that
assertion to the actual Chern jet in (O2). Thus an actual
$U(1)\longrightarrow U(2)$ theta lift has
\[
 v_{11}\!\left(C^{-2}
       \Theta(\phi_{\mathbf t',P_{a,b}},f_{M,\beta})(1)\right)
   =V_q .
 \tag{O32}
\]
The common input has squared norm $h_M$ as before; its
normalization by $\sqrt{h_M}$ is an 11-adic unit.

More strongly, at least one of the actual norm-one character
inputs in (O27) has the same exact valuation $V_q$. To check
equality rather than only an upper bound, every orbital term
in (O27) is a permitted pair, up to a root of unity. DP59's
matching harmonic lower bound gives valuation at least $V_q$
for each term. The denominator $h_M$ is an 11-adic unit,
so each projected value also has valuation at least $V_q$.
Their sum is (O32); at least one therefore has valuation
exactly $V_q$. This proves existence of an actual irreducible
torus input, although it does not specify which character in
advance.

The new conclusion is the first-image realization and its
explicit projection cost. The sharp valuation and existence
of the algebraic permitted pair themselves are the accepted
DP59 result, not new assertions of this note.

### Ordinary mixed-line values require several torus weights

For an ordinary DP58 line with one nonzero dual eigenaxis,
use the global algebraic operator
$P=(D_3+D_j)^N$, with $j=1$ or2. In the unit-arrow
coordinates it becomes $(uD_X+vD_Y)^N$, with
$u,v$ units, exactly as admitted by DP58/DP59. Put
$N=(11^j+1)11^q$. It has $N+1$ distinct
CM multidegrees. It must not be inserted into the one-weight
statement while keeping a single input $f_{M,\beta}$.

Choose a permitted spectator section with unit value at the
origin. Such a section exists by DP59's integral zero-jet
surjectivity and integral permitted-orbit basis: if all its
basis sections vanished modulo11 at the origin, no integral
linear combination could have unit value. The Chern gauge
has constant term one, so the same statement holds in the
actual reduced frame. We work with this spectator in the
second ordinary $J$ factor, and the ordinary sharp section
in the first, keeping target rank2.

Decompose $P=\sum_{\ell=0}^N P_\ell$ into its distinct
CM weights $\beta_\ell$, including the binomial and
direction coefficients. Put
\[
 \phi_{P,\infty}=\sum_{\ell=0}^N\phi_{P_\ell,\infty},
 \qquad
 f_{M,P}=\sum_{\ell=0}^N f_{M,\beta_\ell}.
 \tag{O33}
\]
Orthogonality of the different characters on the compact
archimedean torus kills every cross term in the theta
integral. The lift of this pair is exactly the sum of the
individual-weight lifts, so at the identity it is the desired
full ordinary derivative, multiplied by the spectator value
and $C^2$. Orthogonality also gives the exact input norm
\[
 \|f_{M,P}\|_2^2=(N+1)h_M .
 \tag{O34}
\]
Thus the normalized algebraic identity value has valuation
$V_q=(11^q-1)/10$, and the additional input logarithmic
norm cost is
\[
 \frac12\log(N+1)+\frac32\log M+
                  \log56-\frac32\log29=O(\log N).
 \tag{O35}
\]
Here $N+1$ is an 11-adic unit at every displayed degree:
for $q>0$ it is $1$ modulo11, and for $q=0$ it is $2$
modulo11. Normalizing the whole input to norm one therefore
does not change its 11-adic valuation. Other prime factors of
$N+1$ are real additional normalization denominators and are
retained; the exceptional set (O28) alone applies only to the
one-weight construction.

One may extract an individual automorphic character from
(O33), obtaining a value of valuation at most $V_q$.
Equality for that selected weight does not follow from the
ordinary-line lower bound, because the latter bounds the sum
of its CM-weight components. No separate lower bound for
arbitrary mixed monomial derivatives is asserted here.

## 8. Remaining full-row and later-image comparisons

### The full mixed-action row product and later lifts

The compact pair here uses ordinary powers $J^n$. DP65's
full-row product is instead $J^P\times\bar J^{\,Q}$ with
the conjugated $E$-action retained on the second block.
Conjugating the scalar $E$-action changes the sign of the
trace alternating form in that block. A single scalar-torus
dual pair with this action is naturally realized with
Hermitian signature $(P,Q)$, not the positive form $I_{P+Q}$.
The projection argument by itself does not remove this
real-form distinction. Thus (O24) is not silently promoted
to DP65's complete mixed-action harmonic image.

Even for the ordinary compact family, $f_{M,\beta}$ is a
specific finite sum of automorphic characters. Requiring one
prescribed irreducible character, requiring an earlier
selected image, or passing through a next definite theta
lift imposes further representation-theoretic conditions.
The exact first-image values and small additional cost in
(O2)–(O4) do not prove survival through those conditions.
No complete six-identity family or terminal mass pairing is
constructed here.

There is a further global field distinction. The actual torus
and first target here are over $E/F=\mathbf Q(\zeta_7)/F$.
AM-DO-022's all-finite even-rank family instead uses the DP57
host $E'=\mathbf Q(\zeta_{28})$ acting on $J^2$. These are
not already a common tower. A restriction/extension-of-scalars
kernel comparison or a new first-torus construction over that
host would be required to join them.

## Exact accepted and primary locators

DP_MULT checkpoint06, DP59: DP_MULT.tex, theorem at lines4815–4853,
especially (TS1)–(TS4) and the factor $M^{-n}$ in (TS5);
research/theta_translate_span_DP59.md, §§1,3,4,5,8.
The subgroup, canonical symmetric finite-order lifts and
integral span are carried accepted inputs.

DP_MULT checkpoint06, DP62: DP_MULT.tex, theorem at lines5321ff;
research/theta_translate_norm_integrality_DP62.md. Its canonical
section norm and good-prime integrality are carried accepted
inputs, not identified with a target automorphic mass norm.

ALP-LIFT-09, actual_torus_first_lift.md, (V1)–(V38);
AM-DO-018, definite_oscillator_moved_family.md, (DO18.5)–(DO18.7);
AM-DO-020 split-place phase calculation; AM-DO-021,
definite_oscillator_ramified_phase.md, especially (DO21.12).
AM-K018, jacobian_source_gauge_match.md, sections2–5 and
(K19.1)–(K19.13), supplies the exact ordinary-power source
gauge comparison used in (O25). Its independent review is
review_kummer_source_gauge.md.

Pan, S.-Y. (2001). Splittings of the metaplectic covers of some
reductive dual pairs. Pacific Journal of Mathematics, 199(1),
163–226. https://msp.org/pjm/2001/199-1/pjm-v199-n1-p10-p.pdf.
Directly checked here: Lemma6.2, printed p.197, including its
displayed proof and concluding scalar; the ramified compact
specialization is cited under AM-DO-021's separately checked proof.

## Check status

The author read the entire saved proof, including (O1)–(O30),
the fixed compact phases, the exact permitted half-orbit stabilizer,
the finite index, both input normalizations, and the named remaining
real-form and later-image gates. The gauge-transfer and sharp-first-image
extension (O25), (O31)–(O35) received a separate complete reading after
the whole-proof review of AM-K018. The exact finite algebra certificate
permitted_orbit_certificate.py passed. Events and their scopes are
recorded in lift_accounting_CHECK_EVENTS.tsv. No formal proof
assistant execution is claimed.
