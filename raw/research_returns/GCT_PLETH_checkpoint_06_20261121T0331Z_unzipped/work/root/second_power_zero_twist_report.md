# A positive second-power formula and the complete first two ideal orders

## G-030. Zero twist at order two, with all boundary cases

Let \(x,b,d\ge0\), \(2b+x\ge10\), and put
\[
\begin{aligned}
n&=d+b+x-2,\\
\lambda&=(d+3b+2x-10,d+b+x,d+b+x,d+x,d).
\end{aligned}
\tag{ZS.1}
\]
Every \(p_{\mu,(n)}^\lambda\), \(\mu\vdash5\), has the
positive formula (ZS.8). The branch \(b\ge5\) uses at most
seventeen bounded integer polytopes with eight variables after
selecting two residues. Each of the five branches \(0\le b\le4\)
uses at most four polytopes with five variables. The fixed constants,
complete support lists and direct constraint matrices are specified
below. This also completes every outer-five coefficient of ideal
order at most two, through the exact comparisons in §5.

## 1. Actual Schur extraction from the restriction complex

Write \(a=b+x\), \(E=\mathfrak h_5\), and let \(Q\) be the
rank-three tautological quotient on \(\mathbf P(E)\). The exact
balanced chart and exterior-column pairing of G021/TR3 give
\[
(S_\lambda\mathbf Q^5)_{(n^5)}
\simeq\operatorname{sgn}^{d+a}
H^0\bigl(\mathcal I_Z^2\otimes S_{(a,b)}Q\bigr).
\tag{ZS.2}
\]
The point order is \(\lambda_2-n=2\), and the line twist is
\(\lambda_2-\lambda_3=0\). The inverse chart is \(u^{-2}F(v(X))\),
with \(u=\prod_iX_{i1}\); G027's normal-order calculation proves
its polynomial extension precisely on the displayed ideal sections.

Use the rank-adaptive form of G027/T049 with auxiliary space
\(F=\mathbf Q^2\), \(\alpha=(a,b)\) and
\(N=a+b=2b+x\ge10\). The normal substitution and Cauchy
Young projector identify (ZS.2), before its sign, with
\[
\operatorname{Hom}_{GL(F)}
\left(S_{(a,b)}F,\left(\bigcap_{i=1}^5
(\ell_i\otimes F)^2\right)_N\right).
\tag{ZS.3}
\]
The full exact restriction complex of G027 has, for a selected
subset \(A\) of size \(s\le3\), the quotient
\[
\left(\bigotimes_{i\in A}(\mathbf Q\oplus F)\right)
\otimes\operatorname{Sym}(\mathfrak h_{5-s}\otimes F),
\]
and the orientation line \(\bigwedge^s\mathbf Q^A\).
Its degree \(N\) terms for larger subsets vanish: their available
degree is at most four, below \(N\). The stabilizer splitting,
quotient maps and orientation are exactly FA13–17. Thus the
alternating Schur extraction computes an actual module through
specified polynomial maps.

Here is an explicit character of every term. For a permutation
cycle type \(\gamma\), let
\[
h_\gamma(j)=[z^j]\frac{1-z}{\prod_{\ell\in\gamma}(1-z^\ell)},
\qquad h_\gamma(j)=0\quad(j<0).
\]
For \(\rho=(p,q)\subseteq(a,b)\), set
\[
K_\gamma(a,b;p,q)=
h_\gamma(a-p)h_\gamma(b-q)
-h_\gamma(a-q+1)h_\gamma(b-p-1).
\tag{ZS.4}
\]
Use zero when \(\rho\) is not contained. This is precisely the
skew Schur trace \(s_{(a,b)/(p,q)}(\mathfrak h_{|\gamma|})\):
Macdonald, *Symmetric Functions and Hall Polynomials*, second
edition, Chapter I §5, (5.3)–(5.4), printed p.70, and
(5.7), p.71. The primary text and its derivation were read.
The multiplicity-space identification is Cauchy extraction
followed by the rational Young projectors, as in G027.

For selected cycle type \(\eta\), the cyclic tensor trace of its
truncated normal factors is
\[
P_\eta(X,Y)=\prod_{\ell\in\eta}(1+X^\ell+Y^\ell)
=\sum_{p\ge q\ge0}c_\eta(p,q)s_{(p,q)}(X,Y).
\tag{ZS.5}
\]
All the needed polynomials are the following finite table:

| \(\eta\) | Schur expansion \(P_\eta\) |
|---|---|
| empty | \(1\) |
| \((1)\) | \(1+s_1\) |
| \((1,1)\) | \(1+2s_1+s_2+s_{11}\) |
| \((2)\) | \(1+s_2-s_{11}\) |
| \((1,1,1)\) | \(1+3s_1+3s_2+3s_{11}+s_3+2s_{21}\) |
| \((2,1)\) | \(1+s_1+s_2-s_{11}+s_3\) |
| \((3)\) | \(1+s_3-s_{21}\) |

These identities follow by expanding the displayed products and
using \(s_{(p,q)}=\sum_{i=q}^pX^iY^{p+q-i}\).
In particular their coefficient is
\([X^pY^q]P_\eta-[X^{p+1}Y^{q-1}]P_\eta\), including
negative values when the first monomial is absent.

For \(g\in S_5\), its complete section trace is consequently
\[
t_g(x,b)=
\sum_{\substack{A\subseteq\{1,\ldots,5\}\\ |A|\le3,\ gA=A}}
(-1)^{\#\operatorname{cyc}(g|A)}
\sum_{p\ge q}c_{\operatorname{cyc}(g|A)}(p,q)
K_{\operatorname{cyc}(g|A^c)}(b+x,b;p,q).
\tag{ZS.6}
\]
The sign equals the restriction-complex sign
\((-1)^{|A|}\) times its actual orientation character
\((-1)^{|A|-\#\operatorname{cyc}(g|A)}\).
Character averaging gives
\(f_\nu(x,b)=120^{-1}\sum_{\text{classes }g}|g^{S_5}|
\chi_\nu(g)t_g(x,b)\).
The fixed seven character rows and sizes are those in T044.
The values are integral because the complex computes (ZS.3).

## 2. Exact residue-polynomial bounds

Every root in the generating series for \(h_\gamma\) has order
dividing60. Partial fractions make each nonnegative-index sequence
polynomial on residues modulo60. The empty-subset contribution is
the ordinary two-row Schur trace on \(E\). At the identity its
dimension is
\[
\frac{(x+1)(b+x+2)(b+x+3)(b+1)(b+2)}{12},
\]
of total degree five and separate degrees \((3,4)\).
At a transposition its unique eigenvalue of multiplicity three
has a quadratic contribution to \(h\); the degree-four products
cancel in its two-row determinant. All other eigenvalues have
multiplicity at most two. Thus every nonidentity term has total
degree at most three. These are the exact bounds proved in G026§2.

For a singleton subset, the complementary space has rank three.
Its identity complete traces are quadratic. The degree-four
terms in (ZS.4) agree and cancel, leaving degree at most three.
The degree in \(x\) is at most two. Each nonidentity complementary
class has maximum eigenvalue multiplicity two, so its products
have degree at most two. For a two-element subset the complement
has rank two; the identity products have degree two with equal
leading terms, and the other classes have bounded residue traces.
For a three-element subset the complement is a line, whose
nonnegative-index complete traces are periodic.

All normal partitions in the finite table have \(p\le3,q\le1\).
On the bulk \(b=B+5\), \(B\ge0\), every index in (ZS.4) is
nonnegative. Therefore the bounds just proved hold on every
entire bulk residue class, starting at zero: separate degrees at
most \((3,4)\), total degree at most five.

At a boundary \(0\le b\le4\), put
\(x=X+10-2b\). Then \(a=b+x\ge10-b\ge6\);
every varying index involving \(a\) is nonnegative. The indices
involving \(b\) alone are fixed constants, and negative ones
are assigned their exact zero values. The noncontainment tests
also involve only fixed \(b,q\). Thus each boundary residue
function is polynomial in \(X\) from \(X=0\), of degree at most
three. This checks every initial-range and partition-boundary issue.

## 3. Every fixed positive constant and its lattice polytope

In the bulk write \((x,B)=(r_1,r_2)+60(q_1,q_2)\), with
\(0\le r_i<60\), and define
\[
C_{\nu,r;i,j}=
\sum_{u=0}^i\sum_{v=0}^j
(-1)^{i+j-u-v}\binom iu\binom jv
f_\nu(r_1+60u,r_2+60v+5),
\quad0\le i\le3,\quad0\le j\le4.
\tag{ZS.7}
\]
The finite polynomial Newton identity gives
\[
\boxed{p_{\mu,(n)}^\lambda=
\sum_{\substack{0\le i\le3,\ 0\le j\le4\\i+j\le5}}
C_{\nu,r;i,j}\binom{q_1}{i}\binom{q_2}{j},\qquad
\nu=\begin{cases}\mu&d+b+x\text{ even},\\
\mu^t&d+b+x\text{ odd}.\end{cases}}
\tag{ZS.8}
\]
The sign follows from (ZS.2), so no parity is implicit.

The exact certificate second_power_zero_twist_certificate.py
evaluates all504000 constants (ZS.7) by unbounded Python integer
traces before its finite-difference array. Every constant is
nonnegative. All seventeen active orders are present; all
positive orders are strictly positive. Their minimum is6473,
and the first difference in the second variable has minimum13572.
The maximum constant is465751800. The maximum input is27757274460;
the bound \(128\cdot27757274460=3552931130880<2^{63}\)
proves every finite-difference operation in the signed64 array
is exact. All hashes, extrema, order bounds and zero positions
are in SECOND_POWER_ZERO_TWIST_CERTIFICATE.json.

For \(b=0,1,2,3,4\), take the one-variable differences through
order three of \(f_\nu(X+10-2b,b)\), on its60 residues.
Each branch has1680 constants. All are nonnegative and all
positive orders are positive. Their maxima are respectively
21780,65520,131400,218700,326700; their minima over positive
orders are258,926,1891,3225,4735. The receipt proves the five
overflow bounds as933152,2811264,5645184,9389600,13997280.
Hence all512400 constants have a fixed exhaustive certificate.

For each positive bulk constant, impose the integer constraints
\[
\begin{gathered}
60q_1=x-r_1,\quad60q_2=B-r_2,\quad q_1,q_2\ge0,\qquad
0\le y\le C_{\nu,r;i,j}-1,\\
0\le z_1<\cdots<z_i<q_1,\qquad
0\le w_1<\cdots<w_j<q_2.
\end{gathered}
\tag{ZS.9}
\]
Replacing each strict inequality by an integer gap of at least
one gives literal rational-polytope constraints. The independent
choice of \(y\) and the two increasing subsets is a bijection
with the corresponding summand in (ZS.8). Empty chains have one
choice. Distinct order tags keep the union disjoint. There are
at most \(2+1+i+j\le8\) variables and seventeen selected tags;
retaining all residues gives61200 fixed tags. The boundary uses
one quotient and one chain, at most five variables and four
selected tags, or240 fixed tags with all residues retained.
This proves the positive formula, including its complete matrices.

## 4. Complete support and direct evaluation

Both bulk first differences are strictly positive. A zero therefore
has \(q_1=q_2=0\), and the complete zero pairs in coordinates
\((x,B)=(x,b-5)\) are:

| Effective label | All bulk zero pairs |
|---|---|
| \((5)\) | \((0,0),(0,2),(1,0)\) |
| \((4,1)\) | \((0,0)\) |
| \((3,2)\) | \((0,0)\) |
| \((3,1,1)\) | none |
| \((2,2,1)\) | \((0,0)\) |
| \((2,1,1,1)\) | \((0,0)\) |
| \((1^5)\) | \((0,0),(0,2),(1,0),(2,0)\) |

Every boundary first difference is positive, so its zeros have
\(0\le X<60\). The complete lists are:

| Effective label | \(b=0\) | \(b=1\) | \(b=2\) | \(b=3\) | \(b=4\) |
|---|---|---|---|---|---|
| \((5)\) | 1 | 0,1 | none | 0 | none |
| \((4,1)\) | 0 | none | none | none | none |
| \((3,2)\) | 0,1 | 0 | none | none | none |
| \((3,1,1)\) | 0,1,2 | 0 | 0 | none | 0 |
| \((2,2,1)\) | 0,1,2,3 | 0,1 | 0 | 0 | none |
| \((2,1,1,1)\) | 0, 1, 2, 3, 4, 5 | 0,1,2 | 0,1 | 0 | 0 |
| \((1^5)\) | 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11 | 0, 1, 2, 3, 4, 5 | 0,1,2,3 | 0,1,2 | 0,1 |

Use the effective label in (ZS.8) and the shift \(x=X+10-2b\).
All remaining inputs have positive coefficient, by nonnegativity
and the strict first-order bounds.

The evaluator second_power_zero_twist_positive.py computes only
the bounded constants (ZS.7) and bounded-order binomials at the
input. It exports the full integer matrices and lazily enumerates
witnesses, using the increasing-subset iterator already specified
in G023. The generic restriction-character implementation
zero_twist_arrangement.py was checked against1442 actual balanced
plethysm multiplicities at orders1,2,3; the separate fixed
certificate proves the infinite positive formula. Independent
constant, actual-character and literal-matrix checks are logged
with their precise executed scopes as they finish.

## 5. Completion of both first ideal orders and exact transport

For an arbitrary five-row partition of size \(5n\), set
\[
d=\lambda_5,\quad x=\lambda_4-\lambda_5,\quad
b=\lambda_3-\lambda_4,\quad
k=\max(0,\lambda_2-n),\quad c=\lambda_2-\lambda_3.
\tag{ZS.10}
\]
For positive \(k\), the exact flag dictionary is
\[
n=d+b+x+c-k,\qquad
\lambda=(d+3b+2x+4c-5k,d+b+x+c,d+b+x,d+x,d),
\]
with validity \(2b+x+3c\ge5k\). Its bundle is
\(\operatorname{sgn}^{d+b+x}\mathcal I^k(c)S_{(b+x,b)}Q\).
The following disjoint cases exhaust the first two ideal orders:

| Order | Twist | Complete positive formula |
|---|---|---|
| \(k=1\) | \(c=0\) | G026 |
| \(k=1\) | \(c=1\) | T045 |
| \(k=1\) | \(c\ge2\) | G021 |
| \(k=2\) | \(c=0\) | G030 |
| \(k=2\) | \(c=1\) | T051 |
| \(k=2\) | \(c=2\) | T050 |
| \(k=2\) | \(c=3\) | T045 |
| \(k=2\) | \(c\ge4\) | G021 |

Each row uses the actual chart (ZS.10); hence the coefficient,
parity and support comparisons agree exactly. At \(k=0\), G021
and its explicit \(u^{\,n-\lambda_2}\) stable chart in TR18
already give the complete positive count.

It follows that all seven coefficients are positively evaluated
for every five-row shape with
\[
\boxed{\lambda_2\le n+2\quad\text{or}\quad\lambda_4\ge n-2.}
\tag{ZS.11}
\]
For the second region use \(H=\lambda_1\),
\(\lambda^c=(H-\lambda_5,\ldots,H-\lambda_1)\),
\(n^c=H-n\). The exterior-column pairing TR19 identifies its
balanced module with the dual original module times
\(\operatorname{sgn}^H\), and
\(\lambda^c_2-n^c=n-\lambda_4\le2\). This is the exact
morphism proving the second region and its outer-label transpose.

The schemes are the affine and Proj coordinate models of the
five explicit linear ideals. G027's quotient substitution and
normal-order comparison, followed by its signed restriction
complex and Young projector, are the exact maps in (ZS.3).
EGA II2.4.1–2.4.2 (p.28) supplies the Proj charts and
II2.5.2,2.5.4 (p.31) the exact associated-sheaf functor.
The frame action is the comodule action of SGA3 I4.5,
I4.7.2–4.7.3. The Schur operations are SGA6
V4.2,4.4,4.8–4.9 and cote133/024–029 via A010.
The finite equivariant free resolutions explicitly constructed
in G027§6 carry the coherent complex to locally free \(K_0\)
in SGA6 VI3.3. Thus its geometric class and every coefficient
use the same specified morphisms. R031 then gives the actual
symmetric canonical ranks on these evaluated components.
