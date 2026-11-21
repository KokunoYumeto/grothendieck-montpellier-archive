# A complete positive first-power family at zero twist

## G-026. Positive coefficients and exact support

Let \(x,b,d\ge0\) and \(2b+x\ge5\). Set
\[
\begin{aligned}
n&=d+b+x-1,\\
\lambda&=(d+3b+2x-5,d+b+x,d+b+x,d+x,d).
\end{aligned}
\tag{ZT.1}
\]
For every \(\mu\vdash5\), the coefficient
\(p_{\mu,(n)}^\lambda\) has a positive formula in at most
seventeen bounded rational polytopes with eight integer variables
after selecting two residues. The branches \(b=0,1,2\) each use
at most four polytopes with five variables after selecting one
residue. All matrices, constants, support exceptions and comparison
maps are specified below. The bulk branch includes the remaining
central first-power slice with zero twist and a two-row quotient;
the three boundary branches agree with
the corresponding complementary formulas of G-021.

Write \(E=\mathfrak h_5\), \(Q=E/\mathcal O(-1)\),
\(\mathcal I=\mathcal I_Z\), and \(a=b+x\). The actual module is
\[
(S_\lambda\mathbf Q^5)_{(n^5)}
\simeq\epsilon^{d+b+x}H^0(\mathcal I\otimes S_{(a,b)}Q).
\tag{ZT.2}
\]
The proof gives all the polynomial and sheaf morphisms, and then
evaluates this module by fixed positive Newton constants.

## 1. The exact section and arrangement maps

The balanced flag chart G-015 and the exterior-column complement
pairing have first-line weight \(b+x\), quotient-flag weight
\((b+x,x,0)\), and order \(\lambda_2-n=1\). The pairing
\(\det Q^*=\det E^*\otimes\mathcal O(-1)\) cancels the whole
line twist, leaving precisely \(S_{(a,b)}Q\) and sign
\(\epsilon^{d+a}\). The inverse chart is
\(F\mapsto u^{-1}F(v(X))\), with
\(u=\prod_iX_{i1}\), and its extension is the order-one ideal
condition proved in G-015. This proves (ZT.2) with its actual map.

Apply G-027 with \(m=5\), \(F=\mathbf Q^3\),
\(\alpha=(a,b,0)\), \(k=1\), and \(N=a+b=2b+x\ge5\).
In \(S=\operatorname{Sym}(E\otimes F)\) put
\(I_i=(\ell_i\otimes F)\). The quotient substitution
\(Y_{0c}\mapsto-\sum_jx_jY_{jc}\) in (FA.8) identifies
normal order at each frame point exactly with membership in
\(I_i\). Thus the section space is the \(S_{(a,b)}F\)
multiplicity in \(\bigcap_iI_i\). The product/saturation
comparison and the full signed restriction complex (FA.3)–(FA.4)
apply in this degree. Their exact maps, local contraction and
global acyclicity were proved there, including all orientation
characters.

At \(k=1\), every normal truncation is the constants. Taking
the indicated Schur component of that exact complex gives
\[
\begin{aligned}
[H^0(\mathcal I S_{(a,b)}Q)]
={}&[S_{(a,b)}\mathfrak h_5]
-[\operatorname{Ind}_{S_1\times S_4}^{S_5}
          (1\otimes S_{(a,b)}\mathfrak h_4)]\\
&+[\operatorname{Ind}_{S_2\times S_3}^{S_5}
          (\operatorname{sgn}_2\otimes S_{(a,b)}\mathfrak h_3)]\\
&-[\operatorname{Ind}_{S_3\times S_2}^{S_5}
          (\operatorname{sgn}_3\otimes S_{(a,b)}\mathfrak h_2)].
\end{aligned}
\tag{ZT.3}
\]
The maps are restrictions with their ordered-subset signs. The
stabilizer splitting is (FA.13), not an unspecified isomorphism
between representations of the same dimension. In particular the
last term is zero at \(b\ge1\), since its Schur functor has
two nonzero rows on a line.

At \(b=0\), the same normal-order argument may use one auxiliary
column. The five ideals are principal with pairwise nonproportional
linear generators, so their intersection is their product. Literal
multiplication by \(\prod_i\ell_i\) gives
\[
H^0(\mathcal I\operatorname{Sym}^xQ)
\simeq\operatorname{Sym}^{x-5}E\quad(x\ge5).
\tag{ZT.4}
\]
This product is invariant under frame permutations. Formula (ZT.4)
therefore also checks the determinant character in the boundary.

## 2. Explicit finite character data and polynomial degrees

For a cycle partition \(\gamma\) of an integer \(t\), define
\[
h_\gamma(q)=[z^q]\frac{1-z}{\prod_{c\in\gamma}(1-z^c)},
\qquad
s_\gamma(a,b)=h_\gamma(a)h_\gamma(b)
-h_\gamma(a+1)h_\gamma(b-1),
\tag{ZT.5}
\]
with \(h(q)=0\) for \(q<0\), and the usual zero Schur
functor beyond the rank. At \(b=0\), the second expression is
\(h_\gamma(a)\). These are the literal symmetric and two-row
Schur traces of \(\mathfrak h_t\): diagonalizing the permutation
gives the first generating series, and the two-row Jacobi–Trudi
identity gives the second. For \(g\in S_5\), (ZT.3) has trace
\[
t_g(x,b)=s_{\operatorname{cyc}(g)}(b+x,b)
+\sum_{s=1}^3(-1)^s
 \sum_{\substack{|A|=s\\gA=A}}
 \operatorname{sgn}(g|A)
 s_{\operatorname{cyc}(g|A^c)}(b+x,b).
\tag{ZT.6}
\]
Thus the trace is completely specified by finite subset tests and
the elementary generating series (ZT.5). Character averaging gives
\[
f_\nu(x,b)=\frac1{120}\sum_{g\ {
m classes}}
 |g^{S_5}|\chi_\nu(g)t_g(x,b).
\tag{ZT.7}
\]
The seven class sizes and character rows are the fixed S5 table
printed in T-044 and in the evaluator. All numbers in (ZT.7) are
integers because (ZT.3) is the character of an actual module.

Here are complete degree bounds for the finite-difference proof.
All eigenvalues in (ZT.5) have order dividing 60. Partial fractions
therefore make every \(h_\gamma(q)\) polynomial on a residue
class modulo 60, of degree at most the largest eigenvalue multiplicity
minus one. For the identity on \(E\), the exact Weyl product is
\[
s_{1^5}(b+x,b)
=\frac{(x+1)(b+x+2)(b+x+3)(b+1)(b+2)}{12}.
\tag{ZT.8}
\]
It has total degree five and separate degrees \((3,4)\).
For a nonidentity element of S5, the only eigenvalue of multiplicity
three occurs at a transposition; all others have multiplicity at
most two. In the transposition case the degree-four term in the
two products of (ZT.5) is the same and cancels. Shifting the index
by one affects only lower degrees of that unique eigenvalue's
quadratic part. The other eigenvalue has multiplicity one, so its
cross terms have degree at most two. Thus its determinant has total
degree at most three. All the other classes have degree at most two.
The S4-standard identity term has total degree three; its other
classes have degree at most two. The S3-standard terms have degree
at most one on fixed residues, and the line terms are bounded.
These statements prove separate degrees \((3,4)\), total degree
five, for \(f_\nu(x,B+3)\). For each fixed \(b=0,1,2\),
the degree in \(x\) is at most three. At these boundaries (ZT.5)
is evaluated with its exact zero convention, so there is no omitted
negative-index exception.

## 3. Fixed nonnegative constants and literal polytopes

In the bulk put \(B=b-3\), write
\((x,B)=(r_1,r_2)+60(q_1,q_2)\), and define
\[
C_{\nu,r;i,j}=
\sum_{u=0}^i\sum_{v=0}^j
(-1)^{i+j-u-v}\binom iu\binom jv
 f_\nu(r_1+60u,r_2+60v+3),
\tag{ZT.9}
\]
where \(0\le r_1,r_2<60\), \(0\le i\le3\),
\(0\le j\le4\). The finite polynomial Newton identity and
the proved degree bounds give, for every input,
\[
\boxed{p_{\mu,(n)}^\lambda
=\sum_{i,j}C_{\nu,r;i,j}\binom{q_1}{i}\binom{q_2}{j},
\qquad
\nu=\begin{cases}\mu&d+b+x\text{ even},\\
\mu^t&d+b+x\text{ odd}.
\end{cases}}
\tag{ZT.10}
\]
The sum can be restricted to the seventeen orders
\(0\le i\le3,0\le j\le4,i+j\le5\).

`first_power_zero_twist_certificate.py` evaluates exactly all
\(7\cdot60^2\cdot4\cdot5=504000\) constants in (ZT.9).
Every constant is nonnegative, all three excluded orders vanish,
and every positive active order is strictly positive. The largest
constant is 456593400. The minimum among positive orders is 3145;
the first differences in the second variable have minimum 12175.
The largest input value is 27204212124, and the bound
\(2^{3+4}\) times that value is 3482139151872, below \(2^{63}\).
This proves that every signed-64-bit operation in this fixed
certificate is exact. Values entering that array are calculated by
unbounded Python integers. The receipt stores each label's byte-stream
hash, extrema, every order's minimum and maximum, and every zero
residue pair. Its loops and finite bounds specify a reproducible
integer certificate, rather than an extrapolation from test inputs.

For every positive constant, use integer variables
\(q_1,q_2,y,z_1,\ldots,z_i,w_1,\ldots,w_j\), subject to
\[
\begin{gathered}
60q_1=x-r_1,\qquad60q_2=B-r_2,\qquad q_1,q_2\ge0,\\
0\le y<C_{\nu,r;i,j},\\
0\le z_1<\cdots<z_i<q_1,\qquad
0\le w_1<\cdots<w_j<q_2.
\end{gathered}
\tag{ZT.11}
\]
An empty chain has one choice. Its number of points is exactly
the corresponding summand of (ZT.10). The tags keep distinct orders
disjoint. At most \(2+1+5=8\) variables occur. Selecting residues
uses at most seventeen tags; retaining all residues in one fixed
specification uses at most 61200 tags. The coefficient and all
matrices are fixed independently of the input, apart from the
displayed affine right sides.

For \(b=0,1,2\), set \(x=X+5-2b\), \(X\ge0\),
and use one-variable differences of \(f_\nu(X+5-2b,b)\)
on residues modulo 60, of orders zero through three. The same
Newton proof gives the coefficient. Each branch has exactly 1680
fixed constants, all nonnegative. Their respective maxima are
21780, 65520 and 130500, and their respective minima over positive
orders are 258, 926 and 1816. The three computed overflow bounds
are retained in the same receipt and lie below \(2^{63}\).
The polytopes are (ZT.11) with one quotient and one chain, so there
are at most four selected tags, five variables and 240 uniform tags.

## 4. Complete support and the direct evaluator

Strict positivity of both first differences in the bulk proves that
every zero has \(q_1=q_2=0\). The complete bulk zero set, stated
in coordinates \((x,B)=(x,b-3)\), is

| Effective label \(\nu\) | Zero pairs |
|---|---|
| \((5)\) | \((0,0),(0,2)\) |
| \((3,2)\) | \((0,0)\) |
| \((2,2,1)\) | \((0,0)\) |
| \((2,1,1,1)\) | \((0,0)\) |
| \((1^5)\) | \((0,0),(0,2),(1,0),(1,1),(2,0)\) |

The labels \((4,1)\) and \((3,1,1)\) have no bulk zeros.
At a boundary, strict positivity of its first difference puts all
zeros in \(0\le X<60\). Their complete lists are:

| \(\nu\) | \(b=0\), zero \(X\) | \(b=1\), zero \(X\) | \(b=2\), zero \(X\) |
|---|---|---|---|
| \((5)\) | 1 | 0,1 | 0 |
| \((4,1)\) | 0 | none | 0 |
| \((3,2)\) | 0,1 | 0 | none |
| \((3,1,1)\) | 0,1,2 | 0 | 0 |
| \((2,2,1)\) | 0,1,2,3 | 0,1 | 0 |
| \((2,1,1,1)\) | 0,1,2,3,4,5 | 0,1,2 | 0,1 |
| \((1^5)\) | 0,1,2,3,4,5,6,7,8,9,11 | 0,1,2,3,4,5 | 0,1,2,3 |

Use the sign conversion in (ZT.10) for the requested outer label.
These tables exhaust the domain because all constants are
nonnegative and the cited first-order constants are strictly positive.

`first_power_zero_twist_positive.py` is the direct standard-library
evaluator, full constraint-matrix exporter and lazy witness generator.
It calculates its cached constants only at the bounded arguments of
(ZT.9), then uses bounded-order binomials at the input values.
Its witness iterator never materializes a range of input size.
The underlying exact character routine was compared against the
independent balanced-cycle algorithm in 427 actual plethysm
comparisons, all passing; this is a separate check from the fixed
constant certificate. Dedicated exported-matrix and witness checks
are recorded with their actual execution scope.

## 5. Exact geometric transport and sources

The construction consists of the quotient of a locally free sheaf,
the five specified coherent ideals, their actual normal-order maps,
the signed restriction complex and Schur extraction. G-027 proves
the required product/saturation comparison using Conca–Herzog,
Theorem3.1, Lemma3.2 and Corollary3.3, preprint p.6 and proofs p.7.
At this reduced first-power specialization, Derksen–Sidman,
*A sharp bound for the Castelnuovo–Mumford regularity of subspace
arrangements*, Theorem2.1, p.154, also supplies regularity at most
five; its algebra-to-sheaf convention is Theorem1.2, p.153.
The independent full proof of G-027 specifies exactly which of these
statements is needed for (ZT.3).

The frame/comodule action is SGA3 I4.5 and I4.7.2–4.7.3;
the Schur and exterior-column operations are SGA6 V4.2,4.4,4.8–4.9,
transported from cote133/024–029 by A-010. The exact complex gives
(ZT.3) in the representation \(K_0\). For its geometric class,
resolve each finitely generated graded module by finite equivariant
graded free modules, sheafify, and take the alternating class of
the resulting locally free resolution. These resolutions exist:
choose finite-dimensional invariant generator spaces at each graded
syzygy using reductivity over \(\mathbf Q\), and use the finite
projective dimension of the regular polynomial ring. This specified
map puts the coherent complex into the bounded-rank locally free
\(K_0\) of SGA6 VI3.3. The defining ideal and its projective
coordinate maps are the explicit Proj constructions of EGA II2.4.1–2.4.2 (p.28)
and EGA I9.5.2. The positive count is carried back to the original
balanced module by (ZT.2), and the scalar sign is the determinant
character of that displayed pairing. Thus its geometric meaning
uses the same actual maps as its coefficient calculation.
