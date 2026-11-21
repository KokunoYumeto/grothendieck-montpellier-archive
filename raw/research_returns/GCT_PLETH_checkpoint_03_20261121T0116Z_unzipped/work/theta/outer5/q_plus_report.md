# The five-point quotient bundle one degree above the quadratic ray

## T-040. Statement

Let \(k,d\ge0\), and put
\[
n=d+k+2,\qquad
\lambda=(d+3k+6,\ d+2k+2,\ d+1,\ d+1,\ d).
\tag{QP.1}
\]
These are partitions of \(5n\). For every outer partition \(\mu\vdash5\),
the plethysm coefficient \(p_{\mu,(n)}^\lambda\) has a positive count by
at most 240 fixed tagged rational polytopes, each using at most five
integer variables. Only four tags can contribute after the residue of
\(k\) modulo 60 is fixed. Equations (QP.19)–(QP.22) below give every
constant and inequality. The full fixed table is
`Q_PLUS_NEWTON_TABLE.json`; a standalone evaluator is
`q_plus_positive.py`.

For the symmetric outer power the exact support criterion is
\[
\boxed{
p_{(5),(n)}^\lambda>0\quad\Longleftrightarrow\quad
\begin{cases}
k\ge3,&d\text{ even},\\
k\ge1,&d\text{ odd}.
\end{cases}}
\tag{QP.2}
\]
We prove the actual module presentation first and derive the positive
count from its seven finite-group traces. No character calculation or
elimination is required when evaluating the final fixed-table formula.

## 1. The scalar Rees pieces and the precise geometric map

Retain T-038's five-point ideal
\[
I=(xz-xy,xw-xy,yz-xy,yw-xy,zw-xy)
\subset S=\mathbf Q[x,y,z,w],
\]
with its literal \(S_5\) action, and put
\(E=\mathfrak h_5\), \(U=I_2=[3,2]\), \(\epsilon=\operatorname{sgn}\).
Use \(Q\) for the tautological rank-three quotient bundle on
\(\mathbf P(E)\). Write
\[
R=\operatorname{Sym}(U)=\mathbf Q[A,B,C,D,E_0],
\quad T=(A,B,C,D,E_0)^t,
\quad F=AD(E_0-B-C)-BC(E_0-A-D).
\tag{QP.3}
\]
Each variable of \(R\) has degree one, corresponding to polynomial
degree two in \(S\). The names \(E\) and \(E_0\) distinguish the
representation from the fifth scalar variable.

Define the graded spaces
\[
\mathcal A_k=H^0(\mathcal I_Z^k(2k)),\qquad
\mathcal C_k=H^0(\mathcal I_Z^k(2k+1)),\qquad
\mathcal N_k=H^0(\mathcal I_Z^k(2k+1)\otimes Q),
\tag{QP.4}
\]
and take their direct sums over \(k\ge0\). Multiplication by the five
quadrics makes them graded \(R\)-modules.

The primary-source application A-029 establishes the following exact
facts for this ideal:
\[
\mathcal A_k=(I^k)_{2k},\qquad
\mathcal C_k=(I^k)_{2k+1},\qquad
H^1(\mathcal I_Z^k(2k))=0.
\tag{QP.5}
\]
For \(k\ge2\), these follow from its proved \(2k\)-linear resolution
and saturation bound. For \(k=1\), the ideal is saturated and degree-two
evaluation is onto the five point values. For \(k=0\), these are the
ordinary projective-space statements. The source input is
Kustin–Polini–Ulrich, formula (6.1.4), printed p. 1509, Lemma 6.3 and
Corollary 6.4, p. 1510, with the corollary proof on p. 1511. A-029 checks
the actual alternating presentation and the local generator condition at
every prime, and proves the Tor and saturation deductions. These passages
and the complete applied proof were independently read for this result.

In the coordinates (QP.3), the exact Rees presentation from that same
application is
\[
\mathcal R(I)=S[T]/(T^t\varphi,F),
\tag{QP.6}
\]
where \(\varphi\) is (5R.14). The map sends each \(T_i\) to its
displayed quadratic generator times the Rees parameter. Its component
of \(S\)-degree zero is
\(\mathcal A=R/(F)\). Its component of \(S\)-degree one is
\(\mathcal C\). Thus the relationship of the ordinary powers, saturated
sections and the presentation is through specified maps, with the degree
ranges in (QP.5).

For (QP.1), the flag parameters of G-015 are
\[
\lambda_2-n=k,\qquad \lambda_2-\lambda_3=2k+1,
\qquad(\lambda_3-\lambda_5,\lambda_3-\lambda_4)=(1,0).
\]
The same relative exterior-column calculation as (5F.6)–(5F.9), now
with \(a=1\), starts with first-line weight \(2k+2\). The determinant
pairing removes one copy of \(\mathcal O(1)\), leaving twist
\(2k+1\), and gives
\[
\boxed{(S_\lambda\mathbf Q^5)_{(n^5)}
\simeq\epsilon^{d+1}\otimes\mathcal N_k.}
\tag{QP.7}
\]
Explicitly, the relative quotient-flag module is
\(S_{(1,1)}Q^*=\Lambda^2Q^*=Q\otimes\det Q^*\), and
\(\det Q^*=\det E^*\otimes\mathcal O(-1)\).
The original full determinant contributes \(\epsilon^d\), so their
product is exactly \(\epsilon^{d+1}\). The inverse to the flag chart
is \(F_{\rm flag}\mapsto u^{-k}F_{\rm flag}(v(X))\), and G-015 proves
its polynomial extension precisely from the order-\(k\) five-point
ideal. This proves the transport without suppressing its linearization.

## 2. A four-by-five scalar-piece presentation

Write \(T^t\varphi=(x,y,z,w)\mathsf B(T)\). The actual matrix is
\[
\mathsf B=\begin{pmatrix}
0&0&D-E_0&E_0-C&C-D\\
E_0-B&A-E_0&0&0&B-A\\
0&D&0&-B&0\\
-C&0&A&0&0
\end{pmatrix}.
\tag{QP.8}
\]
It satisfies
\[
\mathsf B T=0,\qquad
(-1)^{i-1}\det\mathsf B_{\widehat i}=-FT_i\quad(1\le i\le5).
\tag{QP.9}
\]
Here \(\mathsf B_{\widehat i}\) deletes column \(i\). The maximal
minors are nonzero, so the fraction-field kernel has dimension one.
The five entries of \(T\) have gcd one; the UFD denominator argument of
T-038 proves that the entire polynomial kernel is \(RT\).

The matrix
\[
\mathsf Q=\begin{pmatrix}
AB&AD&-A(A+C-E_0)&-B(A+D-E_0)\\
AB&BC&-A(B+C-E_0)&-B(B+D-E_0)\\
BC&CD&-C(A+C-E_0)&-D(B+C-E_0)\\
AD&CD&-C(A+D-E_0)&-D(B+D-E_0)\\
AB&CD&-AC&-BD
\end{pmatrix}
\tag{QP.10}
\]
obeys \(\mathsf B\mathsf Q=F I_4\), as verified by direct multiplication.
Consequently every degree-one-in-\(S\) consequence of the relation
\(F\) is already in the linear-syzygy image. Equations (QP.5)–(QP.6)
therefore give an exact presentation and resolution
\[
\boxed{
0\longrightarrow\epsilon\otimes R(-2)
\mathrel{\mathop{\longrightarrow}^{T}}
(\epsilon\otimes U)\otimes R(-1)
\mathrel{\mathop{\longrightarrow}^{\mathsf B}}
E^*\otimes R\longrightarrow\mathcal C\longrightarrow0.}
\tag{QP.11}
\]
The action on the first syzygy space is the one inherited from T-038's
five linear syzygies. The final kernel character is also fixed by that
resolution: after its constant basis change \(P\), its last column is
\(f\), an equivariant map from the sign line. Replacing the five
quadratic coefficients \(f_i\) by the five variables \(T_i\) gives
the column \(T\) in (QP.11), with the same sign source. This explains
both actions directly. The invariant form identifies \(E^*\) with
\(E\) whenever character notation is used below.

## 3. The quotient-bundle exact sequence and a full resolution

Tensor the tautological sequence by \(\mathcal I_Z^k(2k+1)\).
It remains exact because its quotient \(Q\) is locally free. By (QP.5),
taking global sections gives the actual exact sequence
\[
0\longrightarrow\mathcal A_k
\mathrel{\mathop{\longrightarrow}^{\iota}}
E\otimes\mathcal C_k\longrightarrow\mathcal N_k\longrightarrow0,
\qquad
\iota(s)=\sum_{i=1}^4 e_i\otimes x_i s.
\tag{QP.12}
\]
The tensor \(\sum e_i\otimes x_i\) is the identity, independent of
the choice of dual bases. Summing over \(k\) gives an exact sequence of
graded equivariant \(R\)-modules.

There is also the following explicit resolution of the quotient:
\[
\boxed{
0\longrightarrow
\bigl(\epsilon E\otimes R(-2)\bigr)\oplus
\bigl(\epsilon\otimes R(-3)\bigr)
\longrightarrow
(\epsilon E\otimes U)\otimes R(-1)
\longrightarrow
(\operatorname{End}E/\mathbf1)\otimes R
\longrightarrow\mathcal N\longrightarrow0.}
\tag{QP.13}
\]
To specify the maps in the chosen bases, represent the middle free
module by \(4\times5\) matrices \(Y\). Its map is
\[
Y\longmapsto[Y\mathsf B^t]\in
\operatorname{Mat}_{4\times4}(R)/(R I_4),
\]
and a lift of the first map is
\[
(r,s)\longmapsto rT^t+s\mathsf Q^t,
\qquad r\in R^4, s\in R.
\tag{QP.14}
\]
The cokernel is exactly (QP.12): the constant identity generator has
been removed from \(E\otimes E^*\), while the remaining relations
are \(E\) tensored with (QP.11).

Here is a direct check of exactness at the two preceding terms. If
\(Y\mathsf B^t=hI_4\), reduce this identity modulo \(F\). The matrix
\(\mathsf B\) has rank exactly three over the fraction field of
\(R/(F)\): all its maximal minors vanish by (QP.9), whereas its minor
using rows \(2,3,4\) and columns \(1,2,3\) is
\(AD(E_0-B)\), not a multiple of the irreducible cubic \(F\).
A scalar matrix of rank four cannot factor through a matrix of rank
three. Therefore \(h=Fs\) for some \(s\in R\). Subtracting
\(s\mathsf Q^t\) leaves a matrix whose every row lies in \(\ker\mathsf B\),
which is \(RT\). Thus \(Y=rT^t+s\mathsf Q^t\), proving exactness.
If this last expression is zero, multiply by \(\mathsf B^t\): it
gives \(sF I_4=0\). Since \(R\) is a domain, \(s=0\), and then
\(rT^t=0\) implies \(r=0\). The first map is injective.

The submodule \(rT^t\) has character \(\epsilon E\), as in (QP.11).
The quotient of the kernel by that submodule is the line of coefficients
\(h/F\), so its generator has character \(\epsilon\) because \(F\)
does. A graded equivariant choice of the displayed quadratic lift is
obtained by averaging its translates over \(S_5\); the identity
\(\mathsf B\mathsf Q=FI_4\) is preserved. This identifies the
equivariant free modules in (QP.13), even though a particular unaveraged
matrix \(\mathsf Q\) need not itself be an equivariant choice of basis.

The dimension series immediately follows:
\[
\sum_{k\ge0}\dim\mathcal N_k t^k
=\frac{15-20t+4t^2+t^3}{(1-t)^5}
=\frac{15-5t-t^2}{(1-t)^4},
\]
\[
\boxed{\dim\mathcal N_k
=\frac{(k+1)(3k^2+22k+30)}2.}
\tag{QP.15}
\]
In particular the four invariant parameters of degrees \(2,4,6,10\)
used for G-017 are not a regular sequence on this module. Multiplying
(QP.15) by their four factors gives a polynomial with coefficient
\(-1\) in degree 20. A regular sequence would give the Hilbert series
of its actual finite quotient by the successive exact multiplication
sequences, and such a coefficient is impossible. This is a concrete
obstruction to that parameter route for this specific module.

## 4. Seven exact character series

For a group element \(g\), write
\(e_g=\chi_E(g)\), \(u_g=\chi_U(g)\), and
\(\epsilon_g=\epsilon(g)\). Taking the graded trace in the actual
resolution (QP.13) gives
\[
\sum_{k\ge0}\chi_{\mathcal N_k}(g)t^k
=\frac{e_g^2-1-\epsilon_g e_gu_g t
             +\epsilon_g e_g t^2+\epsilon_g t^3}
        {\det(1-tg\mid U)}.
\tag{QP.16}
\]
T-038's signed six-coordinate intertwiner gives every denominator.
After cancellation the seven series and class sizes are as follows.

| class | size | series in (QP.16) |
|---|---:|---|
| \(1^5\) | 1 | \((15-5t-t^2)/(1-t)^4\) |
| \(21^3\) | 10 | \((3-t-t^2)/((1-t)^3(1+t))\) |
| \(2^21\) | 15 | \(-(1+t+t^2)/(1-t^2)^2\) |
| \(31^2\) | 20 | \(t/(1-t^3)\) |
| \(32\) | 20 | \(-t/(1-t^3)\) |
| \(41\) | 30 | \(-(1-t+t^2)/(1-t^4)\) |
| \(5\) | 24 | \(-t^2(1-t)/(1-t^5)\) |

Every denominator divides \((1-t^{60})^4\). The numerator after
multiplication by this common denominator has degree at most 238;
this follows either from the displayed fractions, or from the proper
fraction in (QP.16). Hence the multiplicity of any fixed \([\nu]\)
in \(\mathcal N_{r+60q}\), for fixed \(0\le r<60\), is a polynomial
of degree at most three in \(q\), valid for every \(q\ge0\). Indeed,
grouping the common numerator by residues gives
\(h_r(s)/(1-s)^4\), where \(\deg h_r\le3\). Its coefficients are
linear combinations of \(\binom{q-j+3}{3}\), \(0\le j\le3\).
For \(q\ge0\), the values with \(q<j\) are zero even as polynomial
binomial values, so there is no initial exceptional range.

For completeness all fixed character rows used in taking the inner
product are listed here, in the same class order as the preceding table.

| \(\nu\) | character row |
|---|---|
| \((5)\) | \(1,1,1,1,1,1,1\) |
| \((4,1)\) | \(4,2,0,1,-1,0,-1\) |
| \((3,2)\) | \(5,1,1,-1,1,-1,0\) |
| \((3,1,1)\) | \(6,0,-2,0,0,0,1\) |
| \((2,2,1)\) | \(5,-1,1,-1,-1,1,0\) |
| \((2,1,1,1)\) | \(4,-2,0,1,1,0,-1\) |
| \((1^5)\) | \(1,-1,1,1,-1,-1,1\) |

This is the same finite primary character table used and checked in
T-038/T-039.

## 5. Explicit positive Newton constants

Let \(m_\nu(k)\) be the multiplicity of \([\nu]\) in
\(\mathcal N_k\). Write
\[
f=\dim[\nu],\quad a=\chi_\nu(21^3),\quad
b=\chi_\nu(2^21).
\]
For each \(r\in\{0,\ldots,59\}\), define four constants
\(c_{\nu,r,j}\), \(0\le j\le3\). The first is the following
entirely explicit fixed integer:
\[
\begin{aligned}
c_{\nu,r,0}=\frac1{120}\bigl(&fP(r)+10aT(r)+15bD(r)\\
&+20(\chi_\nu(31^2)-\chi_\nu(32))\mathbf1_{r\equiv1\ (3)}\\
&+30\chi_\nu(41)L(r)+24\chi_\nu(5)M(r)\bigr),
\end{aligned}
\tag{QP.17}
\]
where
\[
\begin{aligned}
P(r)&=(r+1)(3r^2+22r+30)/2,\\
T(2h)&=h^2+5h+3,&T(2h+1)&=(h+1)(h+5),\\
D(2h)&=-(2h+1),&D(2h+1)&=-(h+1),\\
(L(0),L(1),L(2),L(3))&=(-1,1,-1,0)\quad\text{periodically modulo }4,\\
(M(0),\ldots,M(4))&=(0,0,-1,1,0)\quad\text{periodically modulo }5.
\end{aligned}
\tag{QP.18}
\]
The other three constants have short closed forms:
\[
\boxed{\begin{aligned}
c_{\nu,r,1}
&=\frac{f(9r^2+590r+12352)+a(10r+350)
      -b\bigl(30\mathbf1_{r\text{ even}}+15\mathbf1_{r\text{ odd}}\bigr)}4,\\
c_{\nu,r,2}&=f(270r+16950)+150a,\\
c_{\nu,r,3}&=16200f.
\end{aligned}}
\tag{QP.19}
\]
They are the first, second and third forward differences of
\(m_\nu(r+60q)\) at \(q=0\). This follows by applying the difference
operator of step 60 to the coefficients of the seven fractions in
(QP.16). In particular \(P(k)=(3k^3+25k^2+52k+30)/2\),
\(T(k)=k^2/4+5k/2\) plus a parity constant, \(D(k)\) is linear on
each parity, and the last four traces are constant on each residue.
Taking these differences gives (QP.19) directly.

All four constants are nonnegative integers. Integrality follows from
their forward-difference interpretation in actual finite-group modules.
For \(j=0\), the constant is the actual multiplicity \(m_\nu(r)\),
and the 420 constants (QP.17) have also been evaluated in the fixed
table. For \(j\ge1\), positivity follows without a table search from
\(|a|,|b|\le f\). In the first row of (QP.19), the numerator is at
least \(f(9r^2+580r+11972)>0\). In the second it is at least
\(f(270r+16800)>0\), and the third is positive.

Newton's polynomial identity now gives the positive formula
\[
\boxed{
m_\nu(r+60q)=\sum_{j=0}^3 c_{\nu,r,j}\binom qj
\qquad(q\ge0),}
\tag{QP.20}
\]
where \(\binom qj=0\) for \(j>q\). This identity covers all \(k\),
including \(k=0\); it is not just an asymptotic quasipolynomial.

## 6. The polytopes, coefficient, and support

Put
\[
\nu=\begin{cases}\mu,&d+1\text{ even},\\\mu^t,&d+1\text{ odd}.
\end{cases}
\tag{QP.21}
\]
For each fixed tag \((r,j)\), \(0\le r<60\), \(0\le j\le3\),
take the polytope in variables \(q,z,x_1,\ldots,x_j\) defined by
\[
\boxed{
60q=k-r,\quad q\ge0,\quad
0\le z\le c_{\nu,r,j}-1,\quad
1\le x_1<x_2<\cdots<x_j\le q.}
\tag{QP.22}
\]
The final chain is omitted when \(j=0\). Its strict inequalities are
the closed rational inequalities \(x_{i+1}-x_i\ge1\) on integer
points. A zero constant makes the polytope empty. Every coordinate is
bounded by the equality or the displayed bounds, so these are bounded
rational polytopes, each with at most five variables.

There is at most one contributing residue. For it, the choices of the
strictly increasing chain are exactly the \(j\)-subsets of
\(\{1,\ldots,q\}\), and the independent coordinate \(z\) supplies
the factor \(c_{\nu,r,j}\). Consequently the disjoint tagged lattice
count of (QP.22) is
\[
\boxed{p_{\mu,(n)}^\lambda=m_\nu(k),}
\tag{QP.23}
\]
by (QP.7), the balanced-weight dictionary T-003, and (QP.20).
This specifies a bijection from every tag's lattice witnesses to the
positive summands of the formula. It uses at most 240 fixed tags
uniformly, and at most four after computing \(k\bmod60\).

The fixed constants have at most six decimal digits. The largest entry
is 197280; thus their bit lengths are absolute constants. The remaining
right sides and integer witnesses have \(O(\log(k+2))\) bits. Evaluating
(QP.20) uses four binomial polynomials of degree at most three, so it
requires a constant number of arithmetic operations on integers of
\(O(\log(k+2))\) bits, after the partition and parity checks.

For all seven labels the exact support is particularly simple:

| \(\nu\) | condition for \(m_\nu(k)>0\) |
|---|---|
| \((5)\) | \(k\ge1\) |
| \((4,1),(3,2),(3,1,1)\) | all \(k\ge0\) |
| \((2,2,1),(2,1,1,1)\) | \(k\ge1\) |
| \((1^5)\) | \(k\ge3\) |

For \(0\le k<60\), these statements are direct substitution into the
fixed 420 constants (QP.17). The complete values are in the table
file, and the listed zero sets were checked exactly. For \(k\ge60\),
the \(j=1\) term of (QP.20) is positive because \(q\ge1\) and
\(c_{\nu,r,1}>0\). This proves the table for every integer \(k\), and
(QP.2) follows by the sign twist (QP.21).

## 7. Checks, source use, and scope

`check_q_plus_family.py` verifies (QP.9), all five signed minors and
their common primitive kernel. It also checks that each exact class
series has the asserted common denominator and degree bound, computes
all 1680 nonnegative Newton constants, checks their closed formulas
(QP.19), and compares all 2520 coefficients through \(k=359\) with the
Newton polynomials. These last comparisons are additional finite checks;
the rational-function degree argument proves the identity for all \(k\).
Receipts: `Q_PLUS_NEWTON_CHECK.tsv` and `.txt`.

The rectangular agent independently expanded the outer Schur cycle
indices and applied Murnaghan–Nakayama to every output in this family
with \(k,d\ge0\), \(d+k+2\le6\), for all seven outer partitions.
All 105 comparisons passed. The proposed traces were computed from the
literal unordered-pair character of \(U\), independently of the Newton
table. Code: `work/rectangular/verify_outer5_odd_q_family.py`; receipt:
`work/rectangular/OUTER5_ODD_Q_INDEPENDENT_CHECK.tsv`.

The source-derived facts (QP.5)–(QP.6) are the precisely applied results
in A-029, `work/archive/FIVE_POINT_POWERS.md`. The primary source is
[Kustin–Polini–Ulrich, *The equations defining blowup algebras of height three Gorenstein ideals*](https://msp.org/ant/2017/11-7/ant-v11-n7-p01-p.pdf),
*Algebra & Number Theory* 11 (2017), 1489–1525, DOI
10.2140/ant.2017.11.1489; the exact locators are given in §1. The
explicit five-point matrices and sign labels are T-038, and the
relative Schur/wedge maps in (QP.7) are spelled out here and in T-039.

The presentation (QP.13) and the positive count (QP.22) evaluate this
particular higher-flag family in full. The parameter obstruction after
(QP.15) records exactly why G-017's four-parameter free-module proof
does not extend to this module with those parameters. The new count
uses its explicit resolution and fixed quasipolynomial coefficients;
it does not assume a new freeness or cohomology-vanishing assertion.
