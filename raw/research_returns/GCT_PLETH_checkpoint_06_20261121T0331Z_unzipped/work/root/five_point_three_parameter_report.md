# Symmetric quotient powers throughout the nonnegative twist region

## G-020. A four-parameter positive coefficient formula

Let \(a,k,t,d\ge0\), and put
\[
n=d+a+k+t,\qquad
\lambda=(d+2a+3k+4t,d+a+2k+t,d+a,d+a,d).
\tag{TP.1}
\]
These are partitions of \(5n\); zero parts are omitted. Every coefficient
\(p_{\mu,(n)}^\lambda\), \(\mu\vdash5\), has the following fixed
positive formula. It uses at most 36 active lattice tags, each with at
most nine integer variables, after computing the residues of \(a,k,t\)
modulo 60. A single uniform description before selecting residues has
at most \(60^3\cdot36=7,776,000\) tags. All constants are specified
by the seven elementary trace functions in (TP.8) and the fixed finite
formula (TP.11). No large lookup table or input-dependent representation
calculation is required by the evaluator.

The effective outer label is
\[
\nu=\begin{cases}\mu,&d+a\text{ even},\\\mu',&d+a\text{ odd}.
\end{cases}
\tag{TP.2}
\]
For each such label, positivity fails at only the explicitly listed
triples in §5. There are 115 exceptional triples in total across the
seven effective labels. Thus the result gives a complete nonvanishing
decision in the entire family (TP.1). It contains G-019 at \(t=0\)
and T-042 at \(t=1\), with the same actual sheaf comparison.

## 1. Exact flag transport and complete cohomology calculation

Retain \(E=\mathfrak h_5\), the canonical five-point scheme \(Z\),
its ideal \(\mathcal I\), and the tautological rank-three quotient
bundle \(Q\). Write \(c=2k+t\), and define
\[
M_{a,k,t}=H^0(\mathbf P(E),\mathcal I^k(c)
                                      \otimes\operatorname{Sym}^aQ).
\tag{TP.3}
\]
The point order of (TP.1) is \(\lambda_2-n=k\), its first-line gap
is \(c\), and its relative quotient weight is \((a,a,0)\). The exact
G-015 chart and the complementary exterior pairing of T-039 give
\[
\boxed{(S_\lambda\mathbf Q^5)_{(n^5)}
\simeq\operatorname{sgn}^{d+a}\otimes M_{a,k,t}.}
\tag{TP.4}
\]
In detail the first-line twist before dualizing the relative quotient
is \(a+c\). The isomorphism
\(S_{(a,a)}Q^*\simeq(\det Q^*)^a\otimes\operatorname{Sym}^aQ\),
with \(\det Q^*=\det E^*\otimes\mathcal O(-1)\), leaves precisely
\(\mathcal O(c)\) and the character in (TP.4). The inverse balanced
chart is \(f\mapsto u^{-k}f(v(X))\). G-015 proves its extension
condition to be the ordinary sheaf power in (TP.3).

The locally split symmetric quotient sequence, tensored by the ideal,
is
\[
0\to\mathcal I^k(c-1)\otimes\operatorname{Sym}^{a-1}E
\longrightarrow\mathcal I^k(c)\otimes\operatorname{Sym}^aE
\longrightarrow\mathcal I^k(c)\otimes\operatorname{Sym}^aQ\to0.
\tag{TP.5}
\]
For \(a=0\), the left term is zero. Its maps multiply by the
tautological vector and apply the quotient, exactly as in (SQ.4).

A-029 proves the required regularity for every \(k\ge2\):
\(H^1(\mathcal I^k(c))=H^1(\mathcal I^k(c-1))=0\) for \(c\ge2k\).
The precise known inputs, with the local hypotheses checked in A-029,
are Kustin–Polini–Ulrich, formula (6.1.4), printed p. 1509, Lemma 6.3
and Corollary 6.4, p. 1510, in
[Algebra & Number Theory 11 (2017), 1489–1525](https://msp.org/ant/2017/11-7/ant-v11-n7-p01-p.pdf).
For \(k=1\), degree-two evaluation is onto, so the same vanishings hold
except at \(c=2\), where
\(H^1(\mathcal I(1))=\mathbf1\). For \(k=0\), the line-bundle
cohomology in all used degrees is given by Stacks Project, Lemma 30.8.1,
tag 01XS, with \(\mathcal O(-1)\) acyclic.

For all the parameters, \(H^i(\mathcal I^k(c-1))=0\) for \(i=2,3\):
the fat-point quotient has dimension zero, and \(c-1\ge-1\), so this
follows from the same scalar projective cohomology. Also
\(H^{i>0}(\mathcal I^k(c))=0\). The long sequence of (TP.5) therefore
proves that its quotient has no positive cohomology for every
\(a,k,t\ge0\). The exceptional source group at \((k,t)=(1,0)\)
contributes to its degree-zero sections exactly as in T-039; it does
not create higher cohomology. Consequently its character is the
Euler-class difference of the two left terms of (TP.5), including
that endpoint.

## 2. The actual jet evaluation and seven elementary trace functions

For \(g\in S_5\), write \(f_g\) for its fixed-letter count and
\(h_N(g)=\operatorname{tr}(g\mid\operatorname{Sym}^NE)\), with
\(h_{-1}=0\). The invariant affine trivializations and normal-coordinate
maps in G-018 §2 identify the full order-\(k\) jet representation with
the induced sum of the first \(k\) symmetric powers of \(\mathfrak h_4\).
In particular its actual trace is
\[
J_k(g)=f_g h_{k-1}(g).
\tag{TP.6}
\]
This is independent of the line-bundle degree: the stabilizer fixes the
canonical vector \(\ell_i\), so the affine linear function equal to
one there gives an invariant trivialization of every twist. The finite
evaluation sequence thus has Euler character
\(h_N(g)-J_k(g)\) in each nonnegative degree \(N\). The sole negative
degree needed is \(-1\), which occurs with \(k=0\); both terms are
zero there. Combining this sequence with (TP.5) gives
\[
\boxed{\chi_{M_{a,k,t}}(g)=
h_a(g)h_{2k+t}(g)-h_{a-1}(g)h_{2k+t-1}(g)
-f_gh_{k-1}(g)\bigl(h_a(g)-h_{a-1}(g)\bigr).}
\tag{TP.7}
\]
Every subtraction is the Euler character of the explicit maps just
proved, and the left side is the degree-zero section representation.

The seven trace functions have the following closed forms for \(N\ge0\),
recorded as table (TP.8).
These follow by expanding
\((1-z)/\prod_{\ell\in\operatorname{cyc}(g)}(1-z^\ell)\).

| cycle type | \(f_g\) | \(h_N(g)\) |
|---|---:|---|
| \(1^5\) | 5 | \(\binom{N+3}{3}\) |
| \(2\,1^3\) | 3 | \((\lfloor N/2\rfloor+1)(\lceil N/2\rceil+1)\) |
| \(2^2\,1\) | 1 | \(N/2+1\) for even \(N\), and zero for odd \(N\) |
| \(3\,1^2\) | 2 | \(\lfloor N/3\rfloor+1\) |
| \(3\,2\) | 0 | the periodic list \((1,-1,1,0,0,0)\) modulo six |
| \(4\,1\) | 1 | one for \(N\equiv0\pmod4\), and zero otherwise |
| \(5\) | 0 | the periodic list \((1,-1,0,0,0)\) modulo five |

For example the transposition series is
\((1-z)^{-2}(1-z^2)^{-1}\); summing its coefficient gives the product
in the table. The \((3,2)\) series is
\((1-z+z^2)/(1-z^6)\), giving its six values. The other expansions
are direct. The convention \(h_{-1}=0\) agrees with every relevant
shifted series \(z\sum_{N\ge0}h_Nz^N\).

## 3. Fixed constants and the exhaustive sign proof

Use the class sizes and irreducible character table in G-019 §2.
All seven characters are real. For residues \(0\le r,s,v<60\), define
the following fixed differences, separately for each class \(g\):
\[
\begin{aligned}
A_i^\delta(r;g)
 &=\sum_{u=0}^i(-1)^{i-u}\binom iu h_{r+60u-\delta}(g),\\
B_{j,l}^\delta(s,v;g)
 &=\sum_{u=0}^j\sum_{w=0}^l(-1)^{j+l-u-w}
       \binom ju\binom lw h_{2s+v+120u+60w-\delta}(g),\\
K_j(s;g)
 &=\sum_{u=0}^j(-1)^{j-u}\binom ju h_{s+60u-1}(g),
\qquad \delta=0,1.
\end{aligned}
\tag{TP.9}
\]
Here \(0\le i,j,l\le3\); every index is between \(-1\) and 717.
Let
\[
\mathcal D=\{(i,j,l)\in\mathbf Z_{\ge0}^3:
i\le3,\ j+l\le3,\ i+j+l\le5\}.
\tag{TP.10}
\]
It contains exactly 36 triples. The fixed constant for a label and tag is
\[
\boxed{c_{\nu,r,s,v,i,j,l}
=\frac1{120}\sum_g |g^{S_5}|\chi_\nu(g)
\left[A_i^0 B_{j,l}^0-A_i^1 B_{j,l}^1
-\mathbf1_{l=0}f_g(A_i^0-A_i^1)K_j\right].}
\tag{TP.11}
\]
Arguments in the brackets are those in (TP.9). This is an explicit
formula in a fixed number of integers of fixed size. In particular it
does not invoke the coefficient in (TP.1) to define a polytope constant.

Every constant (TP.11) is a nonnegative integer. The full exact check
was carried out twice independently over all seven labels, all
\(60^3\) residue triples and all \(4^3\) difference positions: this is
96,768,000 entries. The root computation obtains the traces by the
ordinary cycle-geometric-series recurrence; the independent archive
computation uses precisely the seven closed functions (TP.8) and
universal finite-difference matrices. Both use integer arithmetic and
check divisibility by 120 before division. Both agree on the complete
coefficient-stream hashes, every minimum and maximum, every zero order,
and every vanishing triple. Their complete scripts and receipts are
included in the package.

For auditability, the independent computation bounds every intermediate
signed integer in absolute value by 22,422,562,560,000, below \(2^{63}\),
before using its signed-64 arrays. The root code independently checks a
conservative Python-integer bound for each difference position. Thus
the array calculations implement exact integers, without modular or
floating-point substitution. The largest final constant is 1,021,264,200.

All 28 positions outside \(\mathcal D\) are identically zero. Within
\(\mathcal D\), all 35 positive-order coefficients are strictly
positive for every residue. Their minima, together with the complete
zero counts of the order-zero values, are:

| \(\nu\) | minimum positive-order constant | number of zero triples |
|---|---:|---:|
| \((5)\) | 418 | 5 |
| \((4,1)\) | 1487 | 2 |
| \((3,2)\) | 1735 | 3 |
| \((3,1,1)\) | 1978 | 7 |
| \((2,2,1)\) | 1575 | 10 |
| \((2,1,1,1)\) | 1167 | 21 |
| \((1^5)\) | 258 | 67 |

The order-zero values are nonnegative also by (TP.7) and the finite-group
projector: they are multiplicities in the specified section module.
The exact check supplies all signs of the higher differences, as well
as the stated finite support data. The files are
`five_point_three_parameter_certificate.py`,
`FIVE_POINT_THREE_PARAMETER_SUMMARY.json`,
`work/archive/check_three_parameter_analytic.py`, and
`work/archive/THREE_PARAMETER_ANALYTIC_RECEIPT.json`.

## 4. The polynomial identity in all degrees and the positive polytopes

For each class, the series for \(h_N(g)\) and \(h_{N-1}(g)\), indexed
by \(N\ge0\), have denominator dividing \((1-z^{60})^4\), with common
numerator degree at most 239. These fourteen exact identities follow
by substituting (TP.8); they were also checked independently by polynomial
division. The residue argument of (W.14) proves that each is a polynomial
of degree at most three in its quotient variable from the first residue
value, including every initial zero.

Write
\[
a=60p+r,\qquad k=60q+s,\qquad t=60u+v,
\qquad0\le r,s,v<60.
\]
Then \(2k+t=60(2q+u)+(2s+v)\). The fixed number \(2s+v\) may require
an additional residue carry of zero, one, or two; all such carries are
nonnegative. Hence both \(h_{2k+t}\) and \(h_{2k+t-1}\) are polynomials
of total degree at most three in \(q,u\), for every \(q,u\ge0\).
Equation (TP.7) is consequently polynomial of degree at most three in
\(p\) and total degree at most three in \(q,u\).

Its terms of degree three in both blocks vanish. At the identity its
dimension is
\[
\begin{aligned}
\dim M_{a,k,t}={}&
\binom{a+2}{2}\left[\binom{2k+t+3}{3}
                         -5\binom{k+2}{3}\right]\\
&+\binom{a+2}{3}\binom{2k+t+2}{2}.
\end{aligned}
\tag{TP.12}
\]
This follows by inserting the identity trace into (TP.7), and it has
total degree at most five. For every nonidentity class, (TP.8) shows
that each trace has degree at most two on a residue, so the products
have total degree at most four. Thus the \(p^3\)-terms of total
\((q,u)\)-degree three vanish in every class. These observations also
prove algebraically that exactly the possible difference positions
lie in \(\mathcal D\).

The multivariate Newton identity therefore gives, in every degree,
\[
\boxed{p_{\mu,(n)}^\lambda
=\sum_{(i,j,l)\in\mathcal D}
c_{\nu,r,s,v,i,j,l}\binom pi\binom qj\binom ul.}
\tag{TP.13}
\]
Its coefficients are precisely the differences (TP.11). The exact
polynomial argument proves the identity outside the finite range used
to determine those constants.

For a uniform polytope description, take a tag
\((r,s,v,i,j,l)\), with constant \(c>0\), and variables
\(p,q,u,y,x_1,\ldots,x_i,z_1,\ldots,z_j,w_1,\ldots,w_l\).
The equations and bounds are
\[
\begin{gathered}
60p+r=a,\quad60q+s=k,\quad60u+v=t,\qquad p,q,u\ge0,\\
0\le y\le c-1,\\
1\le x_1<\cdots<x_i\le p,\qquad
1\le z_1<\cdots<z_j\le q,\qquad
1\le w_1<\cdots<w_l\le u.
\end{gathered}
\tag{TP.14}
\]
Empty lists impose no condition and contribute one choice. Strict
inequalities are replaced by integer differences at least one. The
equations fix the three quotient variables and every remaining variable
lies in a finite displayed interval. There are at most
\(4+i+j+l\le9\) variables. Its lattice points are in bijection with
the independent choice of \(y\) and the three ordered subsets, so its
count is the corresponding term of (TP.13). The disjoint tagged union
proves the positive formula. Only one residue triple can contribute.

The constants in (TP.11) use only indices at most 717 and the fixed
seven-character table; computing them is a constant-size arithmetic
operation. The binomial arguments in (TP.13) have binary length bounded
by the input length. Thus the evaluator performs a fixed number of
integer operations with polynomial bit cost, and does not loop to
\(a\), \(k\), or \(t\).

## 5. The complete exceptional support

Every triple with at least one coordinate at least 60 has positive
coefficient, since the corresponding first directional difference in
(TP.13) is strictly positive. In the residue cube the complete zeros
are described below. An entry \((a,k):T\) means precisely the triples
\((a,k,t)\) with \(t\in T\); every pair omitted has no zero values.

For \(\nu=(5)\):
\[
(0,0):\{1\},\qquad(0,1):\{0,1\},\qquad(1,0):\{0,1\}.
\]
For \(\nu=(4,1)\): \((0,0):\{0\}\), \((0,1):\{0\}\).
For \(\nu=(3,2)\): \((0,0):\{0,1\}\), \((1,0):\{0\}\).

For \(\nu=(3,1,1)\):
\[
(0,0):\{0,1,2\},\quad
(0,1),(0,2),(1,0),(2,0):\{0\}.
\]
For \(\nu=(2,2,1)\):
\[
(0,0):\{0,1,2,3\},\quad
(0,1),(1,0):\{0,1\},\quad(2,0),(3,0):\{0\}.
\]
For \(\nu=(2,1,1,1)\):
\[
\begin{array}{c|l}
(a,k)&T\\\hline
(0,0)&0,1,2,3,4,5\\
(0,1)&0,1,2,3\\
(0,2)&0,1\\
(1,0)&0,1,2\\
(1,1)&0\\
(2,0)&0,1\\
(3,0),(4,0),(5,0)&0
\end{array}
\]
For \(\nu=(1^5)\):
\[
\begin{array}{c|l}
(a,k)&T\\\hline
(0,0)&0,1,2,3,4,5,6,7,8,9,11\\
(0,1)&0,1,2,3,4,5,6,7,9\\
(0,2)&0,1,2,3,4,5,7\\
(0,3)&0,1,2,3,5\\
(0,4)&0,1,3\\
(0,5)&1\\
(1,0)&0,1,2,3,4,5\\
(1,1)&0,1,2,3\\
(1,2)&0,1\\
(2,0)&0,1,2,3\\
(2,1)&0,1\\
(3,0)&0,1,2\\
(3,1)&0\\
(4,0),(5,0)&0,1\\
(6,0),(7,0),(8,0),(9,0),(11,0)&0
\end{array}
\]
These are exactly the order-zero entries verified in the two independent
certificates. All other triples are positive. The parity rule (TP.2)
then gives the complete coefficient support for the original outer label.

## 6. Exact geometric and lambda-ring dictionary

The object (TP.3) is a Schur functor of the tautological locally free
quotient, tensored with an ordinary point-ideal power and a specified
line bundle. Its higher cohomology vanishes by the complete sequence
argument above. Its class is therefore the actual direct-image
representation, and the Euler-class formula is carried by (TP.5) and
the jet evaluation sequence. The relative exterior pairing and balanced
chart (TP.4) identify it with the stated Schur-operation multiplicity.

The frame-torsor transport, exact representation \(K_0\), and universal
lambda-ring operations have the verified locators SGA 3 I 4.5 and
4.7.2–4.7.3; SGA 6 V 4.2, 4.4, 4.8–4.9 and VI 3.3. The ideal,
coordinate evaluation and multiplication maps are the EGA I 9.5.1–9.5.3
constructions. Their Hilbert/Quot family interpretation is FGA Exposé221,
Theorems3.1–3.2, through the same explicit graded modules in the separate
dictionary. All these representation and cohomology conclusions are
proved in characteristic zero.
