# AM-DO-036: the unchanged first raw kernel survives at maximal 29-level

Author: GPT-6 Astra Pro, ALP_MACHINE `/root/definite_oscillator`.
22 November 2026 UTC. Inherited reasoning effort is not separately exposed.

The first raw T factor has a uniform nonzero local test on every unitary
source vector with its prescribed mirabolic invariance when `b>=4a`.
The proof separates its compact term from an explicitly bounded
nonunit-determinant tail. The raw G and Q tests are exact compact
projectors. Together with the checked spherical tests elsewhere and
AM-R-017's actual class-supported input, these facts prove nonvanishing
with the **unchanged full first G/T/Q finite kernel and the maximal
vacuum at29**. No auxiliary29 Heisenberg translate is inserted.

The statement uses the new mixed theta realization and its actual stage
characters. It does not instantiate the unchanged elliptic `VacIn`, the
source's `Fields.Kq` record, every `ChIdx.Ok` clause, an integral prior
image lattice, or the MainX terminal-mass comparison. A positive
target quotient mass remains in the exact norm identity.

## 1. Exact local convention and the full-rank period operator

Let F be a nonarchimedean characteristic-zero local field, O its ring,
q its residue cardinality, and

\[
 G=\operatorname{GL}_a(F),\quad K=\operatorname{GL}_a(O),\quad
 K_b=\operatorname{GL}_b(O),\quad b\ge4a,\quad z=b/2.
 \tag{DO36.1}
\]

Normalize group Haar by `vol(K)=vol(K_b)=1` and matrix Haar by
`vol(M_(b,a)(O))=1`. Let eta be the actual unitary local splitting
component. The genuine Hom Weil action is

\[
 [\omega(g)f](X)=\eta(\det g)^{-1}|\det g|^{b/2}f(Xg).
 \tag{DO36.2}
\]

This is the source formula of AM-DO-020/024 and ALP-LIFT-20, and
the common global character is exactly `mu_0 xi`, as checked in
DO035 from `LevChiEqOne.lean`61,100. In particular it is
unramified at T, has residue chi at Q, and is tame with the
prescribed residue character at G.

Let pi be any unitary representation of G on a Hilbert space V.
Use conjugate-linear-first inner products. Put `X_0=[I_a;0]` and
define the Bochner integral

\[
 B_f(v;k)=\int_G f(kX_0h)|\det h|^{b/2}
                   \eta(\det h)^{-1}\pi(h)v\,dh,
                       \qquad k\in K_b.
 \tag{DO36.3}
\]

For the raw functions below `|f|<=1_(M_(b,a)(O))`. Since `kX_0`
has an integral left inverse, `f(kX_0h)!=0` implies `h in M_a(O)`.
The convergence and all interchanges follow from the exact bound
proved in Section 2.

The exponent is **b/2**, with no unrecorded modular-character
shift. Directly, for `g in G`, simultaneous replacement of
`f,v` by `omega(g)f,pi(g)v` gives the integral with variable `hg`.
The determinant powers cancel after `t=hg`, and

\[
 \eta(\det g)^{-1}\eta(\det(tg^{-1}))^{-1}
                         =\eta(\det t)^{-1}.
\]

Hence

\[
                 B_{\omega(g)f}(\pi(g)v;k)=B_f(v;k).
 \tag{DO36.4}
\]

This is the simultaneous coinvariant convention for the literal
bilinear theta lift. It checks both the character sign and the
half-determinant exponent without importing a different local
induced-model normalization.

Write

\[
 C_{a,b}(q)=\prod_{i=0}^{a-1}(1-q^{i-b}).
 \tag{DO36.5}
\]

The exact full-rank disintegration proved in LIFT16(S6) is

\[
 \int_{M_{b,a}(F)}H(X)dX
   =C_{a,b}(q)\int_{K_b}\int_G
                    H(kX_0h)|\det h|^b\,dh\,dk.
 \tag{DO36.6}
\]

For clarity, every full-rank X has such a presentation because
its column space intersected with `O^b` is a saturated direct
summand. The two measures have the same right Jacobian; their
constant is the probability that a residue `b by a` matrix has
rank a, which is precisely (DO36.5). The rank-deficient set has
additive measure zero. These facts also give a direct proof of
(DO36.6) in the present convention.

Substitution into the squared norm of (DO36.3), with the second
integration variable written `t=hg`, now proves the exact identity

\[
 \boxed{\quad
 Z_f(v):=\int_G\langle f,\omega(g)f\rangle
                    \langle v,\pi(g)v\rangle\,dg
       =C_{a,b}(q)\int_{K_b}\|B_f(v;k)\|^2dk\ge0.
 \quad}
 \tag{DO36.7}
\]

Indeed the two eta factors on the squared-norm side become
`eta(det h) eta(det t)^(-1)=eta(det g)^(-1)`; the two determinant
powers become `|det h|^b |det g|^(b/2)`, and the vector inner
product is `<v,pi(g)v>`. Equation (DO36.6) gives the other matrix
coefficient. With the opposite convention for writing both
matrix coefficients, simultaneous `g -> g^(-1)` gives the same
real value. This is the actual local doubling test after the
Hom/tensor and bilinear/conjugated-input transport of DO028.

## 2. Exact integrability and the uniform tail inequality

For `z>a-1`, define

\[
 D_a(z;q)=\int_{G\cap M_a(O)}|\det h|^zdh
          =\prod_{i=0}^{a-1}(1-q^{i-z})^{-1},
 \qquad E_a(z;q)=D_a(z;q)-1.
 \tag{DO36.8}
\]

Here is a self-contained normalization check. For additive
matrix measure, let `J_a(s)=int_(M_a(O)) |det X|^s dX`.
The first column has exact common valuation n with measure
`q^(-an)(1-q^(-a))`. A primitive first column is carried to
`e_1` by an integral invertible matrix. The remaining columns
then contribute a free first row and an `(a-1)` square matrix.
Therefore

\[
 J_a(s)=\frac{1-q^{-a}}{1-q^{-a-s}}J_{a-1}(s),\qquad J_0(s)=1.
\]

The multiplicative Haar measure is
`dh=prod_(i=1)^a(1-q^(-i))^(-1)|det h|^(-a)dX`, because K has
the displayed additive measure. Substitute `s=z-a` to obtain
(DO36.8). The convergence condition is `s>-1`, equivalently
`z>a-1`. In particular, `E_a` is exactly the integral over
integral matrices with nonunit determinant, not a heuristic
count of Cartan double cosets.

For `x_i=q^(i-z)` put

\[
 S_a(z;q)=\sum_{i=0}^{a-1}x_i
                =q^{-z}\frac{q^a-1}{q-1}.
\]

When `z>=2a`,

\[
 q^a S_a(z;q)\le\frac{1-q^{-a}}{q-1}<1.
\]

The elementary inequality `prod(1-x_i)>=1-sum x_i` consequently
gives

\[
 \boxed{\quad
 0<E_a(z;q)\le\frac{S_a(z;q)}{1-S_a(z;q)}
                 <\frac1{q^a-1}\qquad(z\ge2a).
 \quad}
 \tag{DO36.9}
\]

This includes q=2. It is strictly stronger than needed at the
actual T primes of R017.

The bound `||B_f(v;k)||<=D_a(z;q)||v||` proves the absolute
convergence in Section 1. For the Fubini step in (DO36.7), take
absolute values before integrating h,t,k; the result is bounded
by `C_(a,b) D_a(z;q)^2 ||v||^2`. Thus the positive identity is
proved by absolutely convergent integrals, with no meromorphic
continuation or local theta-occurrence theorem substituted for
this fixed-vector calculation.

## 3. The untouched T incidence factor has a positive test

Use the actual source and target residue covectors `u!=0,v_0!=0`
and the raw T function from DO035:

\[
       f_T(X)=1_{M_{b,a}(O)}(X)1_{\{v_0\bar X=u\}}.
 \tag{DO36.10}
\]

Its prescribed source compact is

\[
 J_T=\{g\in K:u\bar g=u\},\qquad
                     \operatorname{vol}(J_T)=\frac1{q^a-1}.
 \tag{DO36.11}
\]

Choose a primitive integral matrix X* of rank a with `v_0 X*=u`
modulo q. Such a choice exists because b>a: after an integral
target-coordinate change make `v_0` the last-coordinate functional,
use `I_a` in the first a rows, u in the last row and zero elsewhere.
Extend its primitive columns to `k* in K_b`, so `k* X_0=X*`.

Let `v in V^(J_T)`. The compact part of (DO36.3) is exactly

\[
 \int_K f_T(X*h)\eta(\det h)^{-1}\pi(h)v\,dh
                   =\frac{v}{q^a-1}.
 \tag{DO36.12}
\]

Indeed eta is unramified at T, the condition is precisely
`h in J_T`, and pi fixes v there. The remaining integral has
norm at most `E_a(b/2;q)||v||`, by unitarity of pi and eta.
Define

\[
 \Delta_T(a,b;q)=\frac1{q^a-1}-E_a(b/2;q)>0.
 \tag{DO36.13}
\]

Then `||B_(f_T)(v;k*)||>=Delta_T||v||`. The same equality of
the integrands holds for every k congruent to k* modulo q:
the raw function depends only on reduction inside integral
matrices, and every such primitive matrix has an integral
left inverse. This open subset has measure
`|GL_b(F_q)|^(-1)`. Equation (DO36.7) proves

\[
 \boxed{\quad
 Z_{f_T}(v)\ge
 \frac{C_{a,b}(q)}{|\operatorname{GL}_b(\mathbf F_q)|}
       \Delta_T(a,b;q)^2\|v\|^2>0\quad(v\ne0).
 \quad}
 \tag{DO36.14}
\]

This uses the raw incidence function, not the character-filtered
auxiliary vector of DO035. A nontrivial T diamond character of
the source input is fully compatible with its `J_T` invariance;
the lemma makes no claim that a T coefficient is spherical.

## 4. The raw G and Q tests are exact compact projectors

At a G place let U be the upper unitriangular subgroup of
`GL_a(F_q)`, let psi_U be the exact source generic character,
and let `J_G` be its full reduction preimage in K. ALP-LIFT-20
identified the actual first raw G/GS function, for the admitted
class `y=q^(-1)e_a mod O^b`, as

\[
 f_G(X)=\psi_U(\bar h)
       \quad\text{if }X\in M_{b,a}(O),\ \bar X=X_0\bar h,
                        \ \bar h\in U,
 \tag{DO36.15}
\]

and zero otherwise. If
`pi(j)v=psi_U(bar j)^(-1)v` for j in J_G, then

\[
 B_{f_G}(v;1)
      =\frac{|U|}{|\operatorname{GL}_a(\mathbf F_q)|}\,v.
 \tag{DO36.16}
\]

To check this, `f_G(X_0h)!=0` forces `h in J_G`; its determinant
has residue one, so the tame eta factor is one. The two generic
characters cancel. There is no nonunit-determinant tail, since
every residue matrix in U is invertible. The same equation
holds on `K_b(1)`, giving

\[
 Z_{f_G}(v)\ge
 \frac{C_{a,b}(q)}{|\operatorname{GL}_b(\mathbf F_q)|}
   \left(\frac{|U|}{|\operatorname{GL}_a(\mathbf F_q)|}\right)^2
                      \|v\|^2.
 \tag{DO36.17}
\]

This works on the whole actual inverse-generic source space;
it is not limited to one chosen Steinberg multiplicity line.

At Q use (DO35.8), the same admissible global `ybSet` class,
and the actual label `eta=mu_0 xi`. For every K-fixed vector,

\[
                      B_{f_Q}(v;1)=v.
 \tag{DO36.18}
\]

Here nonzero support forces `h in K`, and the factor
`chi(det h)` in the raw function cancels `eta(det h)^(-1)`.
The same open `K_b(1)` argument gives

\[
             Z_{f_Q}(v)\ge
              \frac{C_{a,b}(q)}{|\operatorname{GL}_b(\mathbf F_q)|}
                                       \|v\|^2.
 \tag{DO36.19}
\]

Thus all the first raw factors have a strictly positive fixed
test on their actual initial source spaces. Finite nonzero
Schwartz functions alone would not imply these statements;
the projector and tail calculations are essential.

## 5. Maximal vacua at every other finite place

At a split place outside G/T/Q, eta is unramified and
`f=phi_0=1_(M_(b,a)(O))`. For every K-fixed v, (DO36.3) has
compact term v and tail at most `E_a(b/2;q)||v||`, independently
of k. Hence

\[
 Z_{\phi_0}(v)\ge
       C_{a,b}(q)(1-E_a(b/2;q))^2\|v\|^2.
 \tag{DO36.20}
\]

In particular this applies at all the relative split29 places,
including their absolute ramification index seven, and at the
dyadic split places. The trace coefficient and additive character
are the actual ones; the unitary identification with this
Schrodinger model is DO022/034. Changing the absolute base-field
ramification does not change the local residue-field calculation.

At an odd nonsplit place the extension is unramified, the even
identity lattices are integrally hyperbolic, and the stage
character is trivial: it is unramified and trivial on the base
field. The actual fixed vacuum calculation LIFT16(S19–20), from
Liu's unramified doubling section, gives on a unit spherical vector

\[
 Z_v= L_v(s_*,\pi_v)\prod_{i=1}^a(1-(-1)^i q_v^{-d-i}),
 \quad d=b-a,\quad s_*=(d+1)/2.
 \tag{DO36.21}
\]

The additive-character/codifferent rescaling and the actual
lattice section were verified there and in DO022; no new choice
of local section is made here. Macdonald's bounded spherical
parameter criterion, in the form checked in LIFT14(E18), gives
`|alpha|<=Q^((a-1)/2)` with `Q=q_v^2`. Consequently, putting
`x_v=q_v^(-(b-2a+2))`, a uniform positive lower bound is

\[
 Z_v\ge (1+x_v)^{-a}
                   \prod_{i=1}^a(1-q_v^{-d-i})>0.
 \tag{DO36.22}
\]

The local L-value is positive in this region. The unitary
spherical parameter is stable under conjugate-inverse, and
the unramified unitary-group standard parameter is stable under
inverse. Thus its eigenvalue multiset is conjugation-stable.
Nonreal conjugate factors have positive product, and every
real factor `1-alpha Q^(-s_*)` is positive because its absolute
correction is less than one. The lower bound follows from
`|1-alpha Q^(-s_*)|<=1+x_v`. This also proves finiteness without
a temperedness assumption.

The bounds (DO36.20), (DO36.22) differ from one by a summable
quantity as the finite places vary. In the split case
`E_a=O_a(q^(-(b/2-a+1)))`, with exponent at least a+1>=2;
in the nonsplit case the exponent is at least2a+2. Their
infinite product is therefore strictly positive. This proves
the needed fixed-vacuum assertion at29 as part of the same
global family, without any later change of finite input.

## 6. A direct convergent global norm identity in the correct range

Let E/F be either actual mixed host of K031 or K032, and
`G=U(I_a)`, `H=U(I_b)`, with the positive real signatures,
the exact common stage character, and the actual CM vacuum.
The fields and trace coefficients are the ones proved in
K030/K032 and DO034; this is not an extension of the old
elliptic constructor. Both groups are anisotropic over F.
For the two concrete first edges,

\[
 (a,b)=(42,1802)\quad\text{or}\quad(168,1802),
                              \qquad b\ge4a.
 \tag{DO36.23}
\]

Take the complete first raw finite vector from DO035 with the
single admitted global Y class and the source/target T
decorations of R017. At29 and every other place outside G/T/Q
keep the maximal vacuum. At infinity take the actual selected
highest polynomial P_nu from DO034, with its source vector w
and its true positive norm N_infty. Choose R017's real matrix
coefficient from this same w, so the input lies on the paired
contragredient line at each real place. This is a choice of
the matched vector in the known selected summand, not an
inference that any source vector pairs with a rigid highest
polynomial.

The source function F is now the **unchanged actual function**
of R017, with the inverse character-name convention explained
in the independent review of that finding. It is nonzero,
maximal at29, has the initial inverse G character, the T
mirabolic invariance and zero diamond sum, and the full
trivial Q level. Its exact norm for maximal finite compact
volumes one and real compact volume one is

\[
                    \|F\|^2=\frac1{28d_T^f d_\rho d_G}.
 \tag{DO36.24}
\]

### Correct literature interface

GQT Theorem11.4 assumes `a<b<=2a`; it must **not** be cited
directly for (DO36.23). Instead use GQT Theorem7.1, printed
p.33: for the anisotropic target, its Siegel--Weil formula
holds in every dimension, with constant `c_(b,a)=1` when
`s_0=(b-a)/2>0`. The doubling construction of section11.3,
printed p.52, and the unfolding in sections11.5–11.6,
printed pp.53–54, are the same absolutely convergent
identities in this range. The character/conjugation transport
is exactly DO028. No continuation through a pole is needed.

There is an especially direct unfolding here. The source
Hermitian space is anisotropic. Every rational maximal
isotropic subspace of its doubled space `S plus (-S)` has
zero intersection with either summand. Its two projections
are therefore isomorphisms, so it is the graph of a rational
isometry. Hence the rational double cosets in the doubling
unfolding have just the open graph orbit, with stabilizer the
diagonal G. Unfolding the Eisenstein sum is consequently the
ordinary integral of a matrix coefficient against the right
regular automorphic coefficient; there are no other rational
orbits to dispose of.

Let dg be the chosen source Haar measure, let dh be the chosen
target Haar measure, and put `V_H=vol_dh(H(F)\\H(A))`. Use the
source inner product with dg. The resulting identity is

\[
 \boxed{\quad
 \|\Theta_\phi^{\rm bil}F\|_{dh}^{2}
       =V_H\int_{G(\mathbb A)}
            \langle\phi,\omega(g)\phi\rangle
            \langle F,R(g)F\rangle_{dg}\,dg.
 \quad}
 \tag{DO36.25}
\]

Here `Theta^bil` is the integral against F, as in the literal
source. For Tamagawa target measure `V_H=2`; this is the
factor `[E:F]` in the doubled identity. Indeed GQT7.1 uses
the normalized target theta integral and states
`tau(H)/[E:F]=1` for the present unitary group. Thus the
unnormalized target integral is `[E:F]` times the Siegel--Weil
Eisenstein value. Scaling dh scales both sides of (DO36.25)
by the same constant. Scaling dg scales the theta lift by
that constant and scales the integral on the right twice,
once through dg and once through the source inner product.
This checks (DO36.25) for the measures used in R017 without
assigning the target quotient mass the value one.

All interchanges are legitimate. The source and target
quotients are compact, so their theta integrals are uniformly
convergent on compact representatives. The remaining adelic
matrix-coefficient integral is absolutely convergent: at each
bad finite place Section 2 bounds it by `C_(a,b)D_a(b/2)^2`;
at almost every split place its absolute integral is exactly
that same expression for the maximal vacuum, which is
`1+O_a(q^(-(b/2-a+1)))`. At nonsplit places the hyperspherical vacuum coefficient is
nonnegative. Indeed compact invariance reduces it to a Cartan
diagonal in the Levi of an integral hyperbolic polarization;
the trivial splitting character gives the positive dilation
action on the lattice indicator. The unitary change from that
polarization preserves the selfdual lattice vacuum. Apply the
same fixed-vacuum formula (DO36.21) to the trivial spherical
source representation: it computes its absolute integral, and
the parameter bound gives `1+O_a(q^(-(b-2a+2)))`. This is a
summable majorant. Infinity is compact. This is the
ordinary convergent Siegel--Weil/unfolding regime, stronger
than the continuation required by the second-term theorem.

## 7. Strict positivity for the fixed global input, including multiplicities

For a local factor define the bounded convolution operator

\[
 Q_v=\int_{G(F_v)}\langle\phi_v,\omega(g)\phi_v\rangle
                                               R(g)\,dg.
 \tag{DO36.26}
\]

At every split finite place (DO36.7) proves positivity of this
operator on any unitary representation, including the actual
automorphic Hilbert space. At G it preserves the inverse-generic
subspace; at T it preserves the `J_T`-fixed subspace; at Q and
all spherical places it preserves the maximal-compact fixed
subspace. These preservation assertions follow from the
corresponding left/right compact covariance of its coefficient.
At G/T/Q its restriction has the strictly positive uniform
lower bounds (DO36.17), (DO36.14), (DO36.19). The nonsplit
spherical operators are positive and have (DO36.22) on their
fixed spaces. One may obtain the latter statement by decomposing
the unitary spherical representation; the bound is uniform in
its bounded spherical parameter.

At infinity compact Schur orthogonality gives, on the specified
source contragredient line,

\[
                         Q_\infty=\frac{N_\infty^2}{d_\rho}.
 \tag{DO36.27}
\]

The actual F lies in that line in every real representation
copy, by its matrix-coefficient construction in R017. It lies
in the required fixed/type subspace at every finite place.
Operators at different places commute. Finite products of
these positive operators are bounded below on this subspace
by the products of their displayed lower bounds. At the
unramified places the deviations from one are uniformly
summable, so the products converge on this subspace and
their lower-bound product is still positive. Equivalently,
decompose the finite-level, fixed-real-type automorphic space
into its finitely many irreducible constituents, retaining
their Hilbert multiplicity spaces; the same uniform bounds
apply to every copy. The convolution operators act trivially
on those multiplicity spaces. No multiplicity-one assumption
and no choice of a favored irreducible projection is needed.

Let `ell_v` denote (DO36.20) or (DO36.22) at the remaining
spherical places and let `c_G,c_T,c_Q` be the lower-bound
constants in (DO36.17),(DO36.14),(DO36.19). Then

\[
 \begin{split}
 \|\Theta_\phi^{\rm bil}F\|_{dh}^{2}
 &\ge V_H\frac{N_\infty^2}{d_\rho}
       \prod_{P\in G}c_{G,P}
       \prod_{P\in T}c_{T,P}
       \prod_{P\in Q}c_{Q,P}
       \prod_{v\notin G\cup T\cup Q}\ell_v\ \|F\|^2\\
 &>0.
 \end{split}
 \tag{DO36.28}
\]

This proves that the exact nonzero R017 input survives the
complete fixed first raw kernel at maximal29 level. The
target value at the identity need not be nonzero; the proved
assertion is positive global norm and hence a nonzero actual
target automorphic form. It is stronger than a nonzero
unrestricted local theta lift and addresses the particular
finite input which the raw first coupled factor prescribes.

## 8. Costs, source scope and range audit

The finite raw Schwartz norm is exactly DO035(26). The real
norm `N_infty^2` is the actual DO034 Fischer/Gaussian/hook
norm, including the pi_B coordinate scalar and, on K032,
its weighted quadratic metric. All finite projector and
tail constants in (DO36.28) are explicit functions of the
fixed ranks and residue cardinalities. They can be very
small; this proof does not label them negligible. There is
no auxiliary29 principal-level cost and no29 translation
depth in this theorem. The T characters and their finite
coefficient field are exactly those retained by R017.

The norm formula retains `V_H`, the actual target quotient
mass. Its positivity is enough for the present analytic
nonvanishing. It is not an identification with the source's
terminal mass or a solution of the MainX scalar equation.
The construction is a genuine mixed-theta first image with
the actual raw local G/T/Q factors and source compact types;
the unchanged `Fields.Kq`, the integral row comparisons and
all later restricted-image contents remain separate.

Finally, the range distinction in Section 6 does not correct
an earlier checked theorem. LIFT12 uses a=2,b=4, the allowed
upper endpoint of GQT11.4. LIFT14(E23) explicitly applies
that theorem only to later j>=1, where a=N_j>d and
`a<b=a+d<2a`; its initial edge was constructed separately.
LIFT16 continues those later edges, and LIFT19 has the same
later-edge hypotheses after DO033's initial construction.
The new first edge is the case requiring the separate
GQT7.1 convergent-range derivation above.

## 9. Primary references and proof checks

- Gan, W. T., Qiu, Y., & Takeda, S. (2014). The regularized
  Siegel--Weil formula (the second term identity) and the
  Rallis inner product formula. *Inventiones Mathematicae,
  198*, 739–831. arXiv:1207.4709v3. Theorem7.1, printed p.33;
  doubling section11.3, p.52; sections11.5–11.6, pp.53–54;
  the actual range restriction of Theorem11.4, p.54.
  <https://arxiv.org/pdf/1207.4709>. These portions were read
  directly in the primary PDF/text; its omitted conjugation
  bars use the already checked rendered-PDF convention in DO028.
- Macdonald's bounded spherical criterion and Liu's actual
  unramified vacuum test are used in the exact checked form
  LIFT14(E18) and LIFT16(S19–20), with their primary locators.
  No new local theta classification is being asserted.
- Literal raw factors, characters and target class: DO035
  Sections1–4 and its source locators; LIFT20's raw first G
  equality; R017's exact source class, central compatibility
  and mass; DO034's actual new-host polynomial and metric.

The author whole-proof review and independent local review
are recorded separately after the complete text is read.
No Lean build is claimed.
