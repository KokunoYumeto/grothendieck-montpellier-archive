# Every symmetric quotient power on the odd five-point ray

## T-042. A complete three-parameter positive family

For \(a,k,d\ge0\), set
\[
n=d+a+k+1,\qquad
\lambda=(d+2a+3k+4,d+a+2k+1,d+a,d+a,d).
\tag{OS.1}
\]
For every \(\mu\vdash5\), the coefficient \(p_{\mu,(n)}^\lambda\)
is a positive count in a fixed family of at most 54,000 bounded rational
polytopes, each with at most eight variables. At most fifteen tags
contribute after the two residues \(a\bmod60\), \(k\bmod60\) are
selected. The evaluator uses a fixed number of integer arithmetic
operations; all constants are explicitly specified below and supplied
in `Q_PLUS_SYMMETRIC_TABLE.json`.

The entire support is described by 27 exceptional pairs across the seven
untwisted outer labels, listed in §6. The proof evaluates the section
space first, using actual maps, and converts its exact rational
characters into positive finite constants. It includes T-040 at \(a=1\).

## 1. The actual sheaf sequence and the plethysm comparison

Use the same \(E=\mathfrak h_5\), five frame points \(Z\), ideal
\(\mathcal I=\mathcal I_Z\), and tautological rank-three quotient
\(Q\) as in T-038–T-040. Put
\[
N_{a,k}=H^0\bigl(\mathbf P(E),\mathcal I^k(2k+1)
                                      \otimes\operatorname{Sym}^aQ\bigr),
\]
\[
C_{0,k}=H^0(\mathcal I^k(2k)),\qquad
C_{1,k}=H^0(\mathcal I^k(2k+1)).
\tag{OS.2}
\]
The partition (OS.1) satisfies \(\lambda_2-n=k\), its first gap is
\(\lambda_2-\lambda_3=2k+1\), and the rank-three quotient weight
after complement is \((a,0,0)\). G-015's exact flag chart and the
exterior-column pairings used in T-039 consequently give
\[
\boxed{(S_\lambda\mathbf Q^5)_{(n^5)}
\simeq\epsilon^{d+a}\otimes N_{a,k}.}
\tag{OS.3}
\]
To fix the linearization explicitly, remove the full determinant power
\(d\). The first-line weight is then \(a+2k+1\), and the relative
quotient-flag module is \(S_{(a,a)}Q^*\). The actual rank-three wedge
map identifies it with
\((\det Q^*)^a\otimes\operatorname{Sym}^aQ\).
Since \(\det Q^*=\det E^*\otimes\mathcal O(-1)\), the remaining
line twist is \(2k+1\), and the determinant character is exactly
\(\epsilon^{d+a}\). The inverse flag map is
\(F\mapsto u^{-k}F(v(X))\). G-015 proves that membership in the
order-\(k\) ideal in (OS.2) is precisely what makes that expression
a polynomial. Thus (OS.3) specifies the geometric and representation
comparison, including its extension condition.

For \(a\ge1\), multiplication by the tautological vector gives the
locally split exact bundle sequence, and hence the ideal-tensored
exact sequence,
\[
0\to\mathcal I^k(2k)\otimes\operatorname{Sym}^{a-1}E
\to\mathcal I^k(2k+1)\otimes\operatorname{Sym}^{a}E
\to\mathcal I^k(2k+1)\otimes\operatorname{Sym}^{a}Q\to0.
\tag{OS.4}
\]
Fiberwise its first map is \(l\otimes v\mapsto lv\) and the last
is the quotient of symmetric algebras. The kernel is exactly
\(L\operatorname{Sym}^{a-1}E\); multiplication by a nonzero line
vector is injective. Local splitting preserves exactness after the
possibly nonflat ideal tensor.

The cohomology vanishing \(H^1(\mathcal I^k(2k))=0\) is (QP.5):
A-029 proves it from the linear powers for \(k\ge2\); at \(k=1\)
degree-two evaluation onto the five point values proves it; and at
\(k=0\) it is the scalar \(\mathcal O\) calculation. Therefore the
actual global-section sequence is
\[
\boxed{0\to C_{0,k}\otimes\operatorname{Sym}^{a-1}E
\to C_{1,k}\otimes\operatorname{Sym}^{a}E
\to N_{a,k}\to0.}
\tag{OS.5}
\]
There is no exceptional \(k=1\) correction in this twist. At \(a=0\),
use \(\operatorname{Sym}^{-1}E=0\), and the assertion is simply
\(N_{0,k}=C_{1,k}\). This proves every endpoint as well as the exact
maps underlying the character identity below.

## 2. The full bivariate rational character

Let \(U=[3,2]\), \(e_g=\chi_E(g)\), \(u_g=\chi_U(g)\), and
\(\epsilon_g=\operatorname{sgn}(g)\). The cubic algebra and the
scalar-piece resolution (QP.11) give
\[
C_{0,g}(t)=\frac{1-\epsilon_gt^3}{\det(1-tg\mid U)},\qquad
C_{1,g}(t)=\frac{e_g-\epsilon_gu_gt+\epsilon_gt^2}
                     {\det(1-tg\mid U)}.
\tag{OS.6}
\]
These are traces of the actual Rees pieces in (OS.2); their saturation
and presentation comparison was proved in T-040 §§1–2. Taking traces
of (OS.5) yields
\[
\boxed{\sum_{a,k\ge0}\chi_{N_{a,k}}(g)s^at^k
=\frac{e_g-s-\epsilon_gu_gt+\epsilon_gt^2+
                         \epsilon_gst^3}
 {\det(1-sg\mid E)\det(1-tg\mid U)}.}
\tag{OS.7}
\]
The numerator is exactly \(C_{1,g}-sC_{0,g}\) times the symmetric
algebra series of \(E\). All determinant denominators are fixed by the
seven ordinary cycle types and T-038's explicit signed six-letter map.

There is an independent exact trace formula using the point jets. For a
cycle type \(\eta=(\eta_1,\ldots,\eta_\ell)\vdash5\), define
\[
h_\eta(r)=[x^r]\frac{1-x}{\prod_{i=1}^{\ell}(1-x^{\eta_i})},
\qquad h_\eta(r)=0\quad(r<0),
\tag{OS.8}
\]
and let \(m_1(\eta)\) be its number of fixed letters. Then
\[
\chi_{C_{j,k}}(\eta)
=h_\eta(2k+j)-m_1(\eta)h_\eta(k-1),\qquad j=0,1.
\tag{OS.9}
\]
Here is the scheme and action calculation. The exact evaluation sequence
for \(\mathcal I^k(2k+j)\) is right exact on global sections by the
vanishing already checked. The permutation trace on its fat-point
quotient receives a contribution only from fixed frame points. At such
a point, the canonical representative \(\ell_i\) is literally fixed
by its stabilizer \(S_4\), so the twisting line has trivial stabilizer
action. An invariant affine chart identifies its tangent coordinates
with \(E/\mathbf Q\ell_i\). The completed local ring modulo the
\(k\)-th maximal-ideal power has the actual filtration with quotients
\(\operatorname{Sym}^r(E/\mathbf Q\ell_i)^*\), \(0\le r<k\).
The coordinate action is linear on this chart, so it is also their
direct sum as a stabilizer module. The removed line is trivial, hence
the generating series of these cumulative jets, as \(k\) varies, is
\[
\frac{t}{1-t}\frac1{\det(1-tg\mid E/\mathbf Q\ell_i)}
=\frac{t}{\det(1-tg\mid E)}.
\]
Summing over the \(m_1\) fixed points proves (OS.9). This describes
the evaluation morphism and its finite-group trace directly, without
assuming that the point-jet action is an unproved permutation module.

The seven irreducible character rows and class sizes are the complete
fixed tables in §4 of T-040. Equations (OS.5), (OS.8) and (OS.9) give
the following explicit integer for the multiplicity of \([\nu]\):
\[
\begin{aligned}
b_\nu(a,k)=\frac1{120}\sum_{\eta\vdash5}
|\mathcal C_\eta|\chi_\nu(\eta)\bigl[&h_\eta(a)
 (h_\eta(2k+1)-m_1h_\eta(k-1))\\
&-h_\eta(a-1)(h_\eta(2k)-m_1h_\eta(k-1))\bigr].
\end{aligned}
\tag{OS.10}
\]
This finite signed expression is used only to specify and verify the
fixed constants in §4. The delivered coefficient formula itself is
the positive lattice count in §5.

## 3. Exact polynomial behavior on every residue pair

For each of the seven classes, each of the four one-variable factors
\[
\det(1-sg\mid E)^{-1},\quad
s\det(1-sg\mid E)^{-1},\quad C_{0,g}(t),\quad C_{1,g}(t)
\tag{OS.11}
\]
has denominator dividing \((1-v^{60})^4\), and its numerator after
using this common denominator has degree at most 239. This follows
from the displayed fixed determinants, or by direct polynomial
division; all 28 exact identities are in the certificate script.
The roots of the denominators have orders dividing 60. Their largest
pole order is four; for the identity the factor \(1-t\) in each
scalar numerator cancels the fifth-dimensional symmetric-algebra pole.

Consequently, for every \(0\le r,s<60\),
\[
(q,p)\longmapsto b_\nu(r+60q,s+60p)
\tag{OS.12}
\]
is a polynomial of degree at most three in each variable, valid for
all \(q,p\ge0\). To see the initial range as well, group a common
numerator by its residues: each residue series has denominator
\((1-v)^4\) and numerator of degree at most three. Its coefficient
is a linear combination of \(\binom{q-j+3}{3}\), \(0\le j\le3\).
For \(q<j\), the polynomial binomial value is already zero, so the
polynomial is valid beginning at zero. Products of these two exact
one-variable descriptions prove (OS.12).

The coefficient of bidegree \((3,3)\) is zero. For a nonidentity
class the multiplicities of eigenvalues on the four-dimensional
standard module are at most three. Its \(a\)-residue polynomial
therefore has degree at most two. At the identity, the coefficient of
\(a^3\) in (OS.5)'s dimension is proportional to
\(\dim C_{1,k}-\dim C_{0,k}\). Their series difference is
\((3+t)/(1-t)^3\), a degree-two polynomial in \(k\). Thus a third
difference in each variable kills every class term. This proves
the bidegree assertion without relying on finite sampling.

## 4. Every fixed positive constant

For \(0\le i,j\le3\) define
\[
\boxed{c_{\nu,r,s;i,j}=
\sum_{u=0}^i\sum_{v=0}^j
(-1)^{i+j-u-v}\binom iu\binom jv\,
b_\nu(r+60u,s+60v).}
\tag{OS.13}
\]
Every argument on the right is below 240. In (OS.8), the largest
coefficient needed to compute them is below 480. Thus (OS.8),
(OS.10), the seven fully listed fixed character rows, and (OS.13)
are a complete finite arithmetic specification of all constants.
They are also supplied literally in the complete table file, indexed
by `labels[nu][r][s][4*i+j]`.

The exact integer certificate verifies all 403,200 constants and gives
\[
\boxed{c_{\nu,r,s;i,j}\ge0;\qquad
c_{\nu,r,s;3,3}=0.}
\tag{OS.14}
\]
Every other positive-order coefficient is strictly positive. In
particular, all \(c_{\nu,r,s;1,0}\) and
\(c_{\nu,r,s;0,1}\) are positive. The minimum among all positive-order
coefficients other than \((3,3)\) is 926. The maximum among all
constants is 607840200, less than \(2^{30}\).

This finite verification is reproducible in
`q_plus_symmetric_certificate.py`. It builds the scalar traces using
the independent point-jet formula (OS.9), verifies their agreement with
the presentation expressions (OS.6), takes the seven character inner
products, and takes exact integer forward differences. It checks
integrality and nonnegativity of every entry, not numerical rounding.
`Q_PLUS_SYMMETRIC_SUMMARY.json` records the minimum and maximum of each
of the sixteen difference orders for every label. The full table is
`Q_PLUS_SYMMETRIC_TABLE.json`; the concise receipt is
`Q_PLUS_SYMMETRIC_CHECK.txt`.

The archive agent independently reconstructed all constants using the
\(\mathsf B(T)\)-presentation character and Newton identities for
the characteristic polynomial of \(U\), without using point jets.
All 403,200 entries, all 28 rational degree bounds, and all zero pairs
agreed. Its independent receipt is
`work/archive/Q_PLUS_SYMMETRIC_PRESENTATION_RECEIPT.json`.

Applying the ordinary two-variable Newton identity to (OS.12) now
proves the positive formula
\[
\boxed{b_\nu(r+60q,s+60p)=
\sum_{i=0}^3\sum_{j=0}^3
c_{\nu,r,s;i,j}\binom qi\binom pj\qquad(q,p\ge0).}
\tag{OS.15}
\]
The sole bidegree-six tag is zero by (OS.14). This identity holds for
all parameters, by the rational-function proof of §3; the finite
certificate supplies the exact signs of its fixed coefficients.

## 5. The actual polytopes and evaluator

For the outer label in (OS.1), set
\[
\nu=\begin{cases}\mu,&d+a\text{ even},\\\mu^t,&d+a\text{ odd}.
\end{cases}
\tag{OS.16}
\]
For each fixed tag \((r,s,i,j)\), \(0\le r,s<60\),
\(0\le i,j\le3\), \((i,j)\ne(3,3)\), use the rational polytope
\[
\begin{gathered}
60q=a-r,\qquad60p=k-s,\qquad q,p\ge0,\\
0\le z\le c_{\nu,r,s;i,j}-1,\\
1\le x_1<\cdots<x_i\le q,\qquad
1\le y_1<\cdots<y_j\le p.
\end{gathered}
\tag{OS.17}
\]
Omit an empty chain when its length is zero. Strict inequalities on
integer points mean the closed inequalities
\(x_{h+1}-x_h\ge1\), and likewise for \(y\). A zero constant makes
the polytope empty. These are bounded polytopes: the two equalities
bound \(q,p\), the interval bounds \(z\), and the chains bound every
remaining coordinate.

Only the actual two residues contribute integer points. For them, the
chains choose an \(i\)-subset of \(\{1,\ldots,q\}\) and a
\(j\)-subset of \(\{1,\ldots,p\}\); the independent coordinate
\(z\) supplies exactly \(c_{\nu,r,s;i,j}\) choices. Therefore the
disjoint tagged lattice count is
\[
\boxed{p_{\mu,(n)}^\lambda=b_\nu(a,k).}
\tag{OS.18}
\]
This follows from (OS.3), the balanced-space covariant projector T-003,
and (OS.15). There are at most \(60^2\cdot15=54000\) fixed tags;
at most fifteen contribute for a given pair of residues. The number
of variables is \(3+i+j\le8\). Every variable and nonconstant right
side has \(O(\log(a+k+2))\) bits; the fixed coefficient interval has
an absolute thirty-bit bound.

`q_plus_symmetric_positive.py` evaluates (OS.15) directly from the
fixed table and exports the complete matrices of (OS.17). It validates
all three nonnegative integer parameters and the outer partition. The
count requires at most fifteen products of cubic binomial polynomials;
its integer arithmetic cost is polynomial in the input bit length.
No runtime character, elimination, or unknown coefficient computation
is part of the evaluator.

## 6. Complete support and explicit propagation maps

For the untwisted label \(\nu\), the complete zero sets of
\(b_\nu(a,k)\), \(a,k\ge0\), are:

| \(\nu\) | zero pairs \((a,k)\) |
|---|---|
| \((5)\) | \((0,0),(0,1),(1,0)\) |
| \((4,1)\) | none |
| \((3,2)\) | \((0,0)\) |
| \((3,1,1)\) | \((0,0)\) |
| \((2,2,1)\) | \((0,0),(0,1),(1,0)\) |
| \((2,1,1,1)\) | \((0,j),(j,0)\), \(0\le j\le2\) |
| \((1^5)\) | \((0,j),(j,0)\), \(0\le j\le5\), and \((1,1),(1,2),(2,1)\) |

The pair \((0,0)\) is counted once in each union. There are 27 pairs
in total across the seven rows. The full residue computation proves
this immediately: inside the \(60\)-by-\(60\) box, these are exactly
the zero constants of order \((0,0)\). Outside it at least one
quotient \(q,p\) is positive, and the corresponding strictly positive
first-difference term in (OS.15) proves positivity.

There is also a smaller geometric verification of the same finite
support reduction. The invariant nondegenerate quadratic tensor
\(\sigma\in\operatorname{Sym}^2E\) gives a nonzero section of
\(\operatorname{Sym}^2Q\) on every fiber. Its image could vanish on
\(E/L\) only if \(\sigma\in L E\); such a tensor has rank at most
two, whereas \(\sigma\) has rank four. Multiplication by this section
therefore gives an equivariant injection
\[
N_{a,k}\hookrightarrow N_{a+2,k}.
\tag{OS.19}
\]
Locally, multiplication by a nonzero quadratic in the symmetric
algebra of the quotient fiber is injective, with constant rank; thus
tensoring by the point ideal preserves the bundle inclusion.

For the other parameter, T-038's six forms have invariant elementary
symmetric polynomial \(e_2(T)\). Its image in \(R/(F)\) is nonzero,
since it has degree two and \(F\) has degree three. It is a section
of \(\mathcal I^2(4)\). Multiplication gives the actual equivariant
injection
\[
N_{a,k}\hookrightarrow N_{a,k+2}.
\tag{OS.20}
\]
The ideal tensored with a vector bundle is torsion-free on integral
projective space, and a nonzero scalar polynomial has no kernel on
its sections. These maps prove coefficientwise support propagation
by two in either parameter.

The 448 values with \(0\le a,k\le7\) and all seven labels, computed
from the fixed expression (OS.10), already have exactly the table's
zero pairs, and every entry in rows or columns six and seven is
positive. Reduce any larger parameter by an even number to six or
seven and apply (OS.19)–(OS.20). This is an independent finite support
argument using only that smaller box and the explicit injection maps.
For the actual outer partition, apply the sign conversion (OS.16).

## 7. Verification record and scope

The full rational identities and all 403,200 fixed constants were
independently reconstructed as described in §4. In addition,
`check_q_plus_symmetric_evaluator.py` passed 3542 exact evaluator
comparisons: 2534 specializations to the independently proved T-040
formula at \(a=1\), and 1008 literal polytope-matrix counts. It
checked 10,589 explicit endpoint witnesses against every matrix
inequality. Receipt: `Q_PLUS_SYMMETRIC_EVALUATOR_CHECK.txt`.

The only ideal-power input is the fully applied A-029 proof, based on
[Kustin–Polini–Ulrich, *The equations defining blowup algebras of height three Gorenstein ideals*](https://msp.org/ant/2017/11-7/ant-v11-n7-p01-p.pdf),
formula (6.1.4), p. 1509, Lemma 6.3 and Corollary 6.4, p. 1510, with
the proof on p. 1511. Its local hypotheses, ordinary-power linearity,
and saturation range were checked for this actual five-point ideal.
The relative flag and dual conventions are the specified Schur maps
of [Magyar, Propositions 1 and 4](https://arxiv.org/pdf/alg-geom/9411014),
transported by the exterior-column identities above and in T-039.

This evaluates every symmetric quotient power on the twist \(2k+1\).
G-019 evaluates the adjacent twist \(2k\); both use the same actual
five-point scheme and flag-chart morphism. T-041 evaluates a separate
hook quotient-bundle family at point power one. The assertions here
do not require new vanishing statements for general Schur quotient
bundles, and no global novelty claim is made.
