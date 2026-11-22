# AM-DO-030: auxiliary finite kernels and simultaneous selected jets in the actual permitted half-orbit

Author: GPT-6 Astra Pro, ALP_MACHINE /root/definite_oscillator;
inherited reasoning effort is not separately exposed; 21 November 2026 UTC.

The carried inputs are DP59/DP62, AM-K018/022, AM-DO-022/026/029,
and AM-R-012. This finding keeps a **fixed nonzero auxiliary finite
Heisenberg operator**, proves simultaneous integral jet interpolation
on the actual DP59 half-orbit, and selects one permitted translate
that remains nonzero after that operator. Its finite norm, coefficient
valuation and an explicit sufficient level are retained. A prescribed
local Q-factor at29 is not absorbed into an operator supported away
from29.

## 1. Actual variety, orbit and auxiliary vector

For the even-rank positive edge \(U(a)\to U(b)\), use

\[
 X=A^{ab}=J^{2ab},\qquad g=\dim X=6ab,\qquad
 \mathcal L=L_{2\infty}^{\boxtimes 2ab}.
 \tag{DO30.1}
\]

Its ordinary product CM action, principal trace-one line, common
vacuum period \(C^{2ab}\), actual invariant differential coordinates,
and finite vacuum \(\phi_0\) are the ones already checked in the
carried inputs. In particular the finite vacuum has norm1; its
archimedean Gaussian norm is separate. No conjugated \(J\)-factor
is substituted for an ordinary factor.

Let

\[
 \alpha=(1+2\sqrt{-7})^e,\qquad M=29^e,\qquad
 \alpha\bar\alpha=M,\qquad e\ge1.
 \tag{DO30.2}
\]

The actual allowed section lattice is

\[
 \mathcal W_M=[\alpha]^*H^0(X,\mathcal L^M)
          \subset H^0(X,\mathcal L^{M^2}).
 \tag{DO30.3}
\]

It has the **actual** integral DP59 product basis
\(\mathcal S_\lambda\), indexed by the prescribed quotient of
\(X[\alpha^2]\). Its rescaled parameters are

\[
 x_\lambda=M t'_\lambda\in X[\alpha].
 \tag{DO30.4}
\]

The corresponding finite vectors are
\(\phi_\lambda=\epsilon_\lambda W_{x_\lambda}\phi_0\), with their
specified finite-order scalars \(\epsilon_\lambda\). These scalars
are units at11 and have complex absolute value1. AM-K022 identifies
this basis and its exact level-normalized reading; it is not replaced
by all sections of \(\mathcal L^{M^2}\).

Fix an odd integer \(d\) with \(\gcd(d,11\cdot29)=1\). Let
\(\mathcal Q\) be finite places supported on the rational primes
dividing \(d\). Choose finite Heisenberg parameters \(y\), supported
on \(\mathcal Q\), with \(dy\in\widehat\Lambda\), where
\(\Lambda\) is the actual perfect trace lattice. Consider

\[
 \mathcal O=\sum_y b_yW_y,\qquad
 \phi_{\rm aux}=\mathcal O\phi_0\ne0.
 \tag{DO30.5}
\]

The \(b_y\) are algebraic, and the operator is fixed before choosing
the29 orbit. This includes the finite incidence and other
auxiliary-place combinations in AM-DO-029 whenever all their
parameters are supported away from29 and11. It does not assume
that a general such combination is an idempotent projector.

Combine terms that differ by an integral auxiliary lattice vector,
using the actual Weyl phase and lattice semicharacter. On the
vacuum, and on the whole29-only span, this produces

\[
 \mathcal O=\sum_{j=1}^{s} b_jW_{y_j},\qquad b_j\ne0,
 \tag{DO30.6}
\]

where the \(y_j\) have distinct classes modulo
\(\widehat\Lambda\). In (DO30.6) equality is an equality of
operators **on that span**; it is not asserted on every Schwartz
vector. Indeed an integral auxiliary Heisenberg operator acts on
the fixed auxiliary vacuum by its actual scalar, and commutes
with every29-local operator.

The classes define distinct points \(t_j\in X[d]\). The
correspondence follows by rational approximation modulo the
integral lattice, or directly from the finite quotient
\(d^{-1}\Lambda/\Lambda\). Distinct classes remain distinct
after reduction at11, since \(X[d]\) is finite étale on the
good11-adic model and becomes constant after an unramified
extension. We may further extend the coefficient DVR to
contain the \(b_j\); this extension need not be unramified.
The valuation is always normalized by \(v_{11}(11)=1\).

The finite vectors \(W_{y_j}\phi_0\) are orthonormal. This is
the selfdual-lattice character argument used in AM-DO-017/029:
a nonintegral difference is detected by a lattice Heisenberg
eigencharacter. Consequently

\[
 S_{\rm aux}^2:=\|\phi_{\rm aux}\|^2
                    =\sum_{j=1}^{s}|b_j|^2>0.
 \tag{DO30.7}
\]

Since the auxiliary and29 factors are disjoint,

\[
 \|\mathcal O\phi_\lambda\|^2=S_{\rm aux}^2
 \quad\text{for every allowed }\lambda.
 \tag{DO30.8}
\]

More generally \(\mathcal O\) restricts to a scaled isometry
from the29 span, with scale \(S_{\rm aux}\). This follows by
writing that span as its variable29 factor tensored with the
fixed vacuum elsewhere. There is no interpolation-coefficient
norm in (DO30.8).

## 2. A common torsion representative and its exact phase

A rational representative of an auxiliary finite parameter need
not act by a fixed scalar correction on every29-translated vacuum.
We choose a representative that does.

Because \(M\) is invertible modulo \(d\), put

\[
 z_j=[M]^{-1}t_j\in X[d].
 \tag{DO30.9}
\]

Choose a lift \(z_j\in d^{-1}\Lambda\), and put \(r_j=M z_j\).
Then \(r_j\) represents the finite class \(y_j\), and its
component at29 lies in \(M\widehat\Lambda_{29}\). Thus

\[
 \delta_j=y_j-r_j\in\widehat\Lambda,\qquad
 (\delta_j)_{29}\in M\widehat\Lambda_{29}.
 \tag{DO30.10}
\]

Every allowed \(x_\lambda\) is supported at29 with denominator
dividing \(M\). Perfectness of the integral trace pairing gives
\(\psi_f(B(\delta_j,x_\lambda))=1\). At all other places the
second parameter is0. Therefore \(W_{\delta_j}\) acts on the
whole permitted orbit by the same scalar as on \(\phi_0\).
Applying the Weyl law gives the explicit root of unity

\[
 \varepsilon_{j,M}
 =\psi_f(-B(r_j,\delta_j)/2)\alpha_\Lambda(\delta_j).
 \tag{DO30.11}
\]

In the convention of AM-DO-026, the reading identity is

\[
 W_{y_j}\phi_\lambda
       \ \longleftrightarrow\
 \varepsilon_{j,M}\,U_{r_j}^{H}F_\lambda.
 \tag{DO30.12}
\]

All phases in (DO30.11) are part of the actual finite reading.
They are independent of \(\lambda\), and are11-adic units.
Here \(F_\lambda\) is the reduced principal-level function
whose pullback by \([M]\) is \(\mathcal S_\lambda\).

The reduced translation formula gives the exact identity

\[
 (U_{r_j}^{H}F_\lambda)(Mu)
       =U_{z_j}^{M^2H}\bigl(F_\lambda(Mu)\bigr).
 \tag{DO30.13}
\]

Indeed both sides have argument \(Mu+Mz_j\), linear
exponential term \(-\pi M^2H(u,z_j)\), and constant term
\(-\pi M^2H(z_j,z_j)/2\). Thus the auxiliary operator, after
the common pullback, evaluates the section at the **distinct**
points \(z_j\), with the fixed phases (DO30.11). After
\([\alpha]^*\), the points on the base of (DO30.3) are

\[
 q_j=[\alpha]z_j=[\bar\alpha]^{-1}t_j.
 \tag{DO30.14}
\]

They remain distinct, including modulo11, because \(\alpha\)
is invertible on \(X[d]\).

### The translated line and the11-adic fibre scalar

Usually \(z_j\notin K(\mathcal L^{M^2})\), since its order
is prime to \(M\). Thus \(U_{z_j}^{M^2H}\) is a comparison
with a **translated line**, differing by the corresponding
torsion line in \(\operatorname{Pic}^0(X)\). It is not an
automorphism in the theta group of \(\mathcal L^{M^2}\).

This causes no loss of an integral fibre unit at11. Pull
back by \([d]\). The reduced identity now uses the point
\(z_j/d\), whose order divides \(d^2\), on
\(\mathcal L^{d^2M^2}\). Since \(d^2\mid d^2M^2\), that
point belongs to its actual theta kernel. DP62's relative
theta group and odd symmetric normalization apply: the
finite-order lift is integral, and its multiplier in any
primitive integral fibre frames is a unit. The normalized
analytic reduced lift differs by the fixed finite-order
scalar, also a unit. The pullback is finite étale at11,
and its map on the formal neighbourhood of the zero
section is an isomorphism after choosing the zero
preimage. The fibre at zero of the pulled-back line
is the original fibre. Consequently the constant in
the given translated-line formal comparison is this
same unit. This is a local fibre assertion, not a
global trivialization of the nontrivial torsion line.

The argument asserts a unit **fibre comparison**, not a
unit value of the translated theta section. It does not
divide by a theta-null. AM-K018 gives the same normalized
canonical gauge on the ordinary \(J\)-product; its positive
character CM type is unchanged by a torsion translation.
The higher coefficients of this gauge need not be integral
ordinary power-series coefficients, and no such claim is
used below.

## 3. Simultaneous integral jets with an explicit threshold

Let \(R\) be a complete coefficient DVR over11 on which
the points \(q_1,\ldots,q_s\), the abelian scheme and the
line are defined. Their specializations are distinct.
For \(D\ge0\), set

\[
 M_0(s,D)=3(s-1)(D+1)+3D+2=3s(D+1)-1.
 \tag{DO30.15}
\]

Then for every \(M\ge M_0(s,D)\), restriction is surjective:

\[
 H^0(X,\mathcal L^M)\longrightarrow
 \bigoplus_{j=1}^{s}
 H^0\!\left(X,\mathcal L^M\otimes
                     \mathcal O_X/I_{q_j}^{D+1}\right).
 \tag{DO30.16}
\]

This is a simultaneous-point extension of AM-K022's
single-point argument. The geometric inputs remain the
same carried facts: \(\mathcal L^3\) is very ample on an
abelian variety, every \(\mathcal L^r\) with \(r\ge2\) is
generated at each point, and positive powers have the
integral \(H^0\) base change used in DP59/K022. Exact
primary locators are given in §7.

**Proof.** Fix \(j\). Choose a section \(h_{j0}\) of
\(\mathcal L^3\) whose value at \(q_j\) is a unit, and
sections \(h_{j1},\ldots,h_{jg}\) vanishing there whose
ratios \(h_{j\ell}/h_{j0}\) form integral formal
parameters. Very ampleness on the special fibre gives
the required independent cotangent vectors. Integral
base change lifts them; subtracting their values times
\(h_{j0}\) makes their vanishing exact. Only unit
inverses are needed.

For each \(k\ne j\), choose \(k_{jk}\) in
\(H^0(X,\mathcal L^3)\) with unit value at \(q_j\) and
value0 at \(q_k\). Very ampleness separates the two
special-fibre points. Lift such a section, and subtract
its value at \(q_k\) times a section normalized to1
there. That subtracted scalar is in the maximal ideal,
so the value at \(q_j\) remains a unit. Put

\[
 H_j=\prod_{k\ne j}k_{jk}^{D+1}.
 \tag{DO30.17}
\]

It is a section of
\(\mathcal L^{3(s-1)(D+1)}\), is a unit in the fibre at
\(q_j\), and vanishes to order at least \(D+1\) at
every other \(q_k\). Put

\[
 r=M-3(s-1)(D+1)-3D\ge2.
 \tag{DO30.18}
\]

Choose \(\eta_j\in H^0(X,\mathcal L^r)\) with unit
value at \(q_j\). The section
\(H_j\eta_jh_{j0}^{D}\) is a local frame of
\(\mathcal L^M\) through the required jet order at
\(q_j\). Express any desired jet in this frame as
\(\sum_{|\beta|\le D}c_\beta t_j^\beta\), with
\(c_\beta\in R\). The global section

\[
 H_j\eta_j
   \sum_{|\beta|\le D}c_\beta
       h_{j0}^{D-|\beta|}
            \prod_{\ell=1}^{g}h_{j\ell}^{\beta_\ell}
 \tag{DO30.19}
\]

has that jet at \(q_j\) and zero \(D\)-jet at every
other point. Summing these sections over \(j\)
realizes all desired jets. This proves (DO30.16)
over \(R\), without division by factorials or
interpolation determinants of nonunit valuation.
\(\square\)

Pulling back by the actual étale isogeny \([\alpha]\)
and its DP59 rigidified line isomorphism gives

\[
 \mathcal W_M\twoheadrightarrow
   \bigoplus_{j=1}^{s}
       \operatorname{Jet}^{D}_{z_j}(\mathcal L^{M^2}).
 \tag{DO30.20}
\]

The formal tangent maps are invertible over \(R\):
\(\alpha\bar\alpha=M\) and \(M\) is a unit at11.
All line comparison constants are units. Thus this
is surjectivity from the actual permitted lattice,
not from a larger section space.

One explicit permitted level is

\[
 e(s,D)=\max\{1,\lceil\log_{29}(3s(D+1)-1)\rceil\},
 \quad M=29^{e(s,D)},\quad
 M_0(s,D)\le M<29M_0(s,D).
 \tag{DO30.21}
\]

The threshold recovers \(3D+2\) when \(s=1\).

## 4. The selected functional and exact factorial valuation

Let \(P=\sum_{|\beta|=D}c_\beta Z^\beta\) be a
nonzero homogeneous polynomial in the actual integral
CM invariant tangent basis. Define

\[
 B_P=\min_{\beta\in\operatorname{supp}P}
                              v_{11}(c_\beta\beta!),
 \qquad \beta!=\prod_\ell\beta_\ell!.
 \tag{DO30.22}
\]

For the selected primitive bideterminant \(P_\nu\)
of AM-K022, its diagonal coefficient is1, so

\[
 B_P\le B_\nu=\sum_{\tau,i}v_{11}(\nu_{\tau,i}!).
 \tag{DO30.23}
\]

For \(S\in\mathcal W_M\), form the exact auxiliary
functional

\[
 \ell_{\mathcal O,P,M}(S)
 =M^{-D}\left[P(\partial_u)
     \sum_{j=1}^{s}b_j\varepsilon_{j,M}
             U_{z_j}^{M^2H}F_S(u)\right]_{u=0},
 \tag{DO30.24}
\]

where the translated functions are read in their
actual translated-line formal charts, as in §2.
All constants are the fixed ones in the reading
map and the primitive fibre comparisons, not
section-dependent gauge choices.

If \(M\) obeys (DO30.21), at least one **individual**
permitted basis section satisfies

\[
 \boxed{\ell_{\mathcal O,P,M}(\mathcal S_\lambda)\ne0,
 \qquad
 v_{11}\!\left(\ell_{\mathcal O,P,M}(\mathcal S_\lambda)\right)
       \le \min_j v_{11}(b_j)+B_P.}
 \tag{DO30.25}
\]

**Proof.** Choose \(j\) with \(v_{11}(b_j)\) minimal
and a monomial \(\beta\) attaining \(B_P\). By
(DO30.20), prescribe zero \(D\)-jets at all
\(z_k\), \(k\ne j\). At \(z_j\), choose integral
formal parameters with first derivatives the
given invariant basis. Prescribe the algebraic
coefficient jet \(M^D t^\beta\) in a primitive
line frame. The scalar \(M^D\) is an11-adic unit.

The translated source/Chern gauge has a unit
constant \(u_{j,M}\). Its higher coefficients
are immaterial: the chosen algebraic jet has
no term of degree below \(D\). Consequently
its degree-\(D\) reduced term is precisely
\(u_{j,M}M^D u^\beta\). All other points make
zero contribution. Thus for this integral
section \(S\),

\[
 \ell_{\mathcal O,P,M}(S)
    =b_j\varepsilon_{j,M}u_{j,M}c_\beta\beta!.
 \tag{DO30.26}
\]

The two displayed comparison scalars are units,
so this value has valuation
\(\min_jv_{11}(b_j)+B_P\) and is nonzero.
Expand \(S\) in the **integral** basis
\(\{\mathcal S_\lambda\}\) of \(\mathcal W_M\).
If every basis value had strictly larger
valuation, their integral linear combination
could not equal (DO30.26). This proves
(DO30.25). No archimedean norm of that
interpolating linear combination is used;
the final selected input is one basis vector.
\(\square\)

This proof also explains why the factorial is
unavoidable: an ordinary coefficient prescribed
to1 has derivative \(\beta!\). It does not
prove a unit derivative at arbitrary degree.
It also does not require integral coefficients
for the full canonical reduced gauge.

The all-polynomial reading AM-DO-026 and the
exact level cancellation (DO30.13) give

\[
 \vartheta_{r_P\mathcal O\phi_\lambda}(1,1)
   =C^{2ab}\,\ell_{\mathcal O,P,M}(\mathcal S_\lambda).
 \tag{DO30.27}
\]

This is a nonzero **actual** selected kernel
value, with the one common period retained.
The polynomial still lies in the actual
selected compact type, since every auxiliary
operator is finite and commutes with the
archimedean creation action.

## 5. Exact cost and one explicit source compact level

The chosen finite Schwartz vector is
\(\mathcal O\phi_\lambda\). Its coefficients
in its reduced auxiliary orbit are the
\(b_j\) times unit phases; its exact norm
is \(S_{\rm aux}\) from (DO30.7). There is
no dependence on \(M\) in that finite norm.
The full Schwartz norm is

\[
 \|r_P\phi_{0,\infty}\|\,S_{\rm aux};
 \tag{DO30.28}
\]

the period, highest-vector hook factor and
Gaussian covolume remain those of AM-R-011/012.
Normalizing the finite vector to norm1 would
divide its value by \(S_{\rm aux}\); that
extra scalar is not silently made integral.

For the actual \(T\)-incidence product of
AM-DO-029, with \(a\)-dimensional source
residue space at each selected \(T\)-place,
the reduced frequency set and coefficients
are

\[
 s=\prod_{P\in v_T}q_P^a,\qquad
 |b_j|=s^{-1},\qquad
 S_{\rm aux}^2=s^{-1}.
 \tag{DO30.29}
\]

The distinct frequencies are the rank-one
matrices \(v_P^t\eta_P\). If no \(q_P\) is11,
then \(v_{11}(b_j)=0\); thus (DO30.25)
retains the same factorial bound \(B_P\).
The sufficient level is now
\(M\ge3s(D+1)-1\). For one rational prime
\(T\) split into six selected half places,
\(s=T^{6a}\), not \(T^{6ab}\).
Other prescribed \(G/Q\) factors are
included by their exact reduced coefficients
from (DO29.11), with their actual \(s\),
norm and minimum valuation.

Here is an explicit finite stabilizer for
the new first lift. Suppose the auxiliary
places are odd relative split places,
the original compact vacuum is fixed there,
and each \(y_j\) has denominator at most
\(\varpi_v^{c_v}\) at \(v\), \(c_v\ge1\).
Take principal congruence

\[
 K_{{\rm aux},a,v}
   =1+\varpi_v^{2c_v}M_a(\mathcal O_v)
       \ \subset\mathrm{GL}_a(\mathcal O_v),
 \tag{DO30.30}
\]

and similarly on the target. Intersect
with the kernel of any separately specified
vacuum determinant character if it is
ramified there. For the R012 character,
which has compact conductor only at29,
that extra intersection is unnecessary.

To check fixation, a matrix in (DO30.30)
changes \(y_j\) by
\(\delta\in\varpi_v^{c_v}\widehat\Lambda_v\).
Both \(B(y_j,\delta)/2\) and the
trace-one lattice exponent for \(\delta\)
are integral at this odd place. Their
character values are1. Thus the Weyl
covariance formula fixes each
\(W_{y_j}\phi_0\), with its actual
central phase, not merely its line.
At29 use the existing principal
congruence of exponent \(e\); at all
other places use the original vacuum
compact subgroup.

In the unramified split situation its
source index is explicitly

\[
 I_{{\rm aux},a}
    =\prod_{v\in\mathcal Q}
      q_v^{a^2(2c_v-1)}
                    |\mathrm{GL}_a(\kappa_v)|.
 \tag{DO30.31}
\]

The exponent comes from the \(2c_v-1\)
successive additive matrix kernels.
It is the index of the sufficient
stabilizer, not an assertion that it is
minimal. There can be11-factors in
\(|\mathrm{GL}_a(\kappa_v)|\), even when
the residue characteristic is not11.

Substitution into the checked
class-supported construction R012 gives
source identity-class mass
\[
 \frac1{I_a(M)I_{{\rm aux},a}},
\]
primitive compact-matrix-coefficient
input norm squared
\[
 \frac1{I_a(M)I_{{\rm aux},a}d_\rho},
\]
and actual lifted value

\[
 \frac{C^{2ab}\,
       \ell_{\mathcal O,P,M}(\mathcal S_\lambda)}
          {I_a(M)I_{{\rm aux},a}d_\rho}.
 \tag{DO30.32}
\]

This uses the same trivial rational
stabilizer supplied by the29 congruence,
and the same compact Schur orthogonality.
It does not change the selected real
weights or the common splitting.
These are source mass factors; they
are distinct from the finite Schwartz
norm (DO30.8).

For a fixed auxiliary operator, \(s,d\),
\(I_{{\rm aux},a}\) and \(S_{\rm aux}\)
are fixed and \(\log M=O(\log(D+2))\).
If they vary with \(D\), the actual
bound is

\[
 \log M<\log29+\log(3s(D)(D+1)-1),
 \tag{DO30.33}
\]

with the displayed auxiliary index and
coefficient data retained. In particular
one must not call the overhead logarithmic
in \(D\) while silently allowing an
exponentially growing \(s(D)\).

## 6. Exact remaining raw-array equation

The theorem now proves nonvanishing after
every fixed auxiliary operator \(\mathcal O\) supported
away from29 and11 for which \(\mathcal O\phi_0\ne0\). It does so
on the actual permitted29 half-orbit,
with a single selected basis vector.
It is stronger than nonvanishing of
some unrestricted finite Schwartz input.

It does **not** identify that new input
with a fixed complete xiAt. Its finite
half-function has the form

\[
 \Phi_{\rm aux}(t_{\rm aux})
                \Phi_{\lambda,29}(t_{29}),
 \tag{DO30.34}
\]

where \(\Phi_{\lambda,29}\) is the
actual29-translated vacuum. If the
prescribed array also contains a
fixed local Q-factor at29, the
required equation is still
\[
 \Phi_{\lambda,29}
       \stackrel{?}{=}\Phi_{Q,29},
\]
or membership of the corresponding
family in the actual source's allowed
local-index span, with all its frame
and character rules. Neither K022's
interpolation nor (DO30.25) proves
that equation.

Applying a nonzero operator supported
at29 cannot simply be included in this
proof: the disjoint-factor tensor
argument and the invertibility of
\(\alpha\) on its torsion points are
then unavailable. The fixed Q29
image, and the resulting prescribed
row/operator identity, therefore remain
precise open gates. Later restricted
image saturation, Kval, terminal
mass and the MainX inequalities are
also not consequences of (DO30.32).

### 6.1 Literal reference-character and prime-set audit

The two source symbols called mu0 have different types
and must be distinguished. In
Development/AbelianVarietyTheory/Definitions/AutomorphicMembership/
TrueColumnChoicesHeckeCharReferenceEqOne.lean:

| Locator | Actual object or condition |
|---|---|
| 175–190 | the index \(I.\mathrm{mu0}\), with \(\mathrm{tup}(I.\mathrm{mu0})=1\) |
| 202–205 | \(I.\mathrm{glob.mu0}=I.C.\mathrm{mu0}\), the family of reference Hecke characters |
| 211–215 | \(I.Q(a)=\mathrm{QE}(\mathrm{sel},\mathrm{tup}(a))\) |
| 222–226 | the actual tying of the reference characters to Chars |
| 273–280 | the proved identity \(I.Q(I.\mathrm{mu0})=\varnothing\) |
| 295–299 | the reference twisting character \(I.\xi(I.\mathrm{mu0})=1\) |

Thus the Q-set records the **finite-order twisting tuple**;
it is not the conductor of the reference splitting
character. In particular a Q29 factor is not forced
merely by saying that a chosen reference character has
conductor29.

However the reference character cannot have arbitrary
ramification. In
Formalism/LocalToGlobal/Columns/AbelianHostFieldConditions.lean,
IsMu0, lines314–323, requires it to be unramified away
from the two G-primes, tame everywhere, and to have
the specified residue character at each G-place.
Chars.Tied, lines325–334, imposes these conditions
on every reference character. Chars.Ok.chi_om,
lines302–305, prescribes
\[
 \chi_{j,P}=\omega_G^{\,2(j+1)}
\]
for one faithful residue character at each rational
G-prime, and chi_inj requires the characters to be
distinct as \(j\) varies. Consequently the R012
reference character, **when its29 compact character
is nontrivial**, is incompatible with keeping both
G-primes away from29. Replacing it by a source-tied
reference character is an additional explicit
construction, with these residue conditions retained.
If29 is one of the G-primes, its G-factor rather
than a Q-factor remains in the raw array. If the
particular29 compact character is trivial, this
ramification obstruction does not apply; the other
source tying conditions still do.
Moreover, the later good-data clause g_big in that same
file, line488, requires \(2fk<g_i-1\). On the actual
mixed host \(f=6\), and the allowed ranks have \(k\ge6\),
so \(g_i>73\). Therefore29 cannot be one of these G-primes.
For a reference character whose29 compact component is
nontrivial, relabelling29 as G does not repair the full
source compatibility. This is a further literal prime
condition; the analytic characters and theta chain do
not claim to satisfy it.

Even when the reference tuple is used and every
G/T auxiliary prime avoids29, the new input in
(DO30.27) is not automatically the same raw datum.
The literal TwDat.Is.idem in
Definitions/LatticeFrames/LevChiEqOne.lean, line62,
requires the predicate
\[
 \operatorname{IsIdemSum}
   \bigl(A.e,\operatorname{Sall}(I.\mathrm{sel},I.\mathrm{tup}(a),u)\bigr).
\]
The definition in
Formalism/LocalToGlobal/IndefiniteReal/DatumVec.lean,
lines78–80, is exactly
\[
 \bigl(\exists (e_P)_P,\;
   (\forall P\in S,\operatorname{IsIdemAt}(e_P,P))
   \ \land\ e=\sum_{P\in S}e_P\bigr)
       \ \land\ e\,\overline e=0.
 \tag{DO30.34a}
\]
There is no function named IdemSum in this assertion.
The support conclusion follows from the literal predicate,
not from its name. In
Formalism/LocalToGlobal/HeckeThetaElements/IsHeckeElt.lean,
lines68–70, IsIdemAt is IsSplitIdem together with
\[
 x\in P\quad\Longleftrightarrow\quad
       (e_P/x)_f\notin\widehat{\mathcal O}_E
 \qquad(0\ne x\in\mathcal O_E).
 \tag{DO30.34b}
\]
Here IsSplitIdem includes \(e_P^2=e_P\),
\(e_P\overline{e_P}=0\), and
\(e_P+\overline{e_P}\) equal to one finite base-place
idempotent; see BesselHermitianTheta/TiedWeil.lean,
lines68–72. Its infinite component is zero, as also
proved in EqZeroOrEqOfPlaceIdem.lean, lines134–140.

For completeness, the finite support implication has a
short direct proof. Identify the finite tensor adelic
algebra with the product of the completions of \(E\).
Idempotence says that each component of \(e_P\) is0 or1.
For any prime \(Q\ne P\), choose a nonzero
\(x\in Q\setminus P\), possible because distinct
maximal ideals are comaximal. If the \(Q\)-component
of \(e_P\) were1, then the \(Q\)-component of
\(e_P/x\) would be nonintegral. This would contradict
(DO30.34b), since \(x\notin P\). Thus every such
component is0. The \(P\)-component must be1: otherwise
all finite components vanish, and any nonzero
\(x\in P\) contradicts (DO30.34b). Consequently
\(e_P\) is exactly the finite idempotent supported
at \(P\). Formula (DO30.34a) therefore gives a zero29
component whenever Sall has no place above29.
The normalized place model
then sends its half-indicator to the **fixed**
vacuum. Thus the fixed array gives
\(\mathcal O\phi_0\), while (DO30.27) gives
\(\mathcal O W_{x_\lambda}\phi_0\). The extra29
factor remains an actual change of finite input.
One cannot add a29 component to \(e\) and still
claim the same literal idem clause.

There is also a precise obstruction to absorbing
a nonzero29 position shift by the available
linear frame/evaluation actions. At a relative
split29 place, the positive Hom polarization
identifies every unitary-pair action with
\(t\mapsto h^{-1}tg\), times its nonzero
determinant-root and Jacobian scalar. Hence
every linear translate of the vacuum has
position function a nonzero scalar times
the indicator of a lattice **containing0**.
A pure position translate by \(x\notin L\)
has function \(1_L(t+x)\), whose support
does **not** contain0. They cannot be equal.
This proves the claimed obstruction for
all such linear source/target evaluations
at29, not only integral frames. It does
not rule out equality of an isolated
theta value, a finite linear combination
of group translates, or a genuinely
enlarged datum with new affine parameters.
It also does not assert that the selected
tuple in (DO30.25) is nontrivial: if the
zero tuple already works, it is an actual
raw witness. The theorem does not force
that special outcome.

Accordingly the empty-Q choice removes
one possible misidentification of the
ramification set, but does not eliminate
the raw-array matching equation. The
finite linear source model fixes the
origin; its frame changes cannot be
used as undeclared affine Heisenberg
translations.

## 7. Exact sources and check scope

- AM-K022, selected_schur_permitted_jets.md, J1–J5:
  actual permitted lattice and its integral basis;
  J6–J17: the carried single-point interpolation
  and highest-symbol factorial argument.
- DP59, research/theta_translate_span_DP59.md,
  §§3–8; DP62, research/theta_translate_norm_integrality_DP62.md,
  TN2–TN5 and §§2–4: actual rigidified multiplication,
  odd symmetric theta lifts and integral finite-order
  normalization. These supplied results are used as
  carried inputs, not reproved in full.
- Milne, J. S. (2008). *Abelian varieties* (Version2.0),
  I, §6, “Ample divisors,” printed p.30,
  paragraph before Example6.5.
  https://www.jmilne.org/math/CourseNotes/AVc.pdf.
  The arbitrary-characteristic very-ampleness input
  is the one already read in AM-K022.
- Mumford, D. (1966). On the equations defining
  abelian varieties. I. *Inventiones Mathematicae, 1*,
  287–354, §1(II), p.289.
  https://pazuki.perso.math.cnrs.fr/index_fichiers/Mumford66.pdf.
  The positive-power cohomology/base-change input
  is carried from DP59/K022.
- Polishchuk, A. *Analogue of Weil representation
  for abelian schemes*, author preprint
  arXiv:alg-geom/9712021, §1, pp.4–5,
  definition preceding Lemma1.1,
  Proposition1.2 and Corollary1.3.
  https://arxiv.org/pdf/alg-geom/9712021.
  The precise relative theta-group input is
  the one already checked in DP62.
- AM-K018, jacobian_source_gauge_match.md,
  §§3–5: exact canonical reduced gauge on
  the ordinary product; no integral reduced
  power-series gauge is assumed.
- AM-DO-026, (DO26.2a)–(DO26.4):
  actual adelic-to-Mumford phase and
  all-polynomial reading. AM-DO-029,
  (DO29.11)–(DO29.23): exact prescribed
  finite coefficients and norms.
- AM-R-012, §§2–3: the actual compact
  selected first input, stabilizer mass,
  and Schur-orthogonality factor.

Proof-check events are recorded only when
actually performed in the agent TSV.
No Lean compilation or complete source
MainX instance is asserted.
