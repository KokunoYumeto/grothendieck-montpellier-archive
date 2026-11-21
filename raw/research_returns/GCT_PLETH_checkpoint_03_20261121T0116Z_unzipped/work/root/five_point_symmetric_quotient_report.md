# Every symmetric quotient power on the five-point quadratic ray

## G-019. A three-parameter positive plethysm family

Let \(a,k,d\ge0\). Define
\[
n=d+a+k,\qquad
\lambda=(d+2a+3k,d+a+2k,d+a,d+a,d).
\tag{SQ.1}
\]
Zero parts are removed; at \(a=k=d=0\) the partition is empty.
For every \(\mu\vdash5\), the coefficient \(p_{\mu,(n)}^\lambda\)
has a positive formula in a fixed family of at most 57,600 bounded
rational polytopes of dimension at most nine. At most sixteen tags
contribute after the two residues \(a\bmod60\) and \(k\bmod60\)
are selected. The evaluator requires a fixed number of integer
arithmetic operations on the input parameters. All constants are
explicitly defined in (SQ.10)–(SQ.12) and supplied in a complete exact
table; no input-dependent character or plethysm computation is required.

This evaluates all symmetric quotient powers together with all point
orders in the geometric model, and includes T-039 at \(k=1\), G-017
at \(a=1\), and the full scalar ray at \(a=0\). The underlying
module comparison is proved for every parameter, before the finite
positive coefficient conversion.

## 1. The actual sheaf module and all cohomological endpoints

Use the five-point scheme \(Z\subset\mathbf P(E)\), with
\(E=\mathfrak h_5\), ideal \(\mathcal I\), and quotient bundle \(Q\).
Put
\[
M_{a,k}=H^0\bigl(\mathbf P(E),\mathcal I^k(2k)
                                      \otimes\operatorname{Sym}^aQ\bigr),
\qquad C_k=H^0(\mathcal I^k(2k)).
\tag{SQ.2}
\]
For (SQ.1), the flag model has point order \(k\), first-line gap
\(2k\), and relative weight \((a,a,0)\). The exterior pairing used
in (5F.7) identifies
\(S_{(a,a)}Q^*\simeq(\det Q^*)^a\otimes\operatorname{Sym}^aQ\).
The full determinant and relative determinants therefore give the
actual equivariant isomorphism
\[
\boxed{(S_\lambda\mathbf Q^5)_{(n^5)}
\simeq\operatorname{sgn}^{d+a}\otimes M_{a,k}.}
\tag{SQ.3}
\]
Its relative frame maps and inverse chart are the maps in G-015 and
T-039 §1, with \(u^{-k}\) replacing \(u^{-1}\). In particular the
point-power condition has already been proved to be exactly the
polynomial extension condition; (SQ.3) retains its full linearization.

For \(a\ge1\), the symmetric quotient sequence is the actual exact
sequence of sheaves
\[
0\to\mathcal I^k(2k-1)\otimes\operatorname{Sym}^{a-1}E
\longrightarrow\mathcal I^k(2k)\otimes\operatorname{Sym}^aE
\longrightarrow\mathcal I^k(2k)\otimes\operatorname{Sym}^aQ\to0.
\tag{SQ.4}
\]
Its first map multiplies by the tautological vector, and its last map
is the symmetric power of the quotient. Before tensoring the ideal,
it is an exact locally split sequence of vector bundles: on a line
\(L\subset E\), the kernel in the symmetric algebra is
\(L\operatorname{Sym}^{a-1}E\), and multiplication by the nonzero line
vector is injective. Tensoring by \(\mathcal I^k(2k)\) preserves this
locally split exactness.

Let \(A_k=H^0(\mathcal I^k(2k-1))\). A-029 proves
\(H^1(\mathcal I^k(2k-1))=0\) for \(k\ge2\), using the verified
Kustin–Polini–Ulrich complexes, formula (6.1.4), p. 1509, Lemma 6.3
and Corollary 6.4, p. 1510. The complete applied proof checks the ideal's
local hypotheses and the passage to ordinary powers. At \(k=0\),
\(\mathcal O(-1)\) is acyclic. At \(k=1\),
\(A_1=0\), \(H^1(\mathcal I(1))=\mathbf1\), and
\(H^1(\mathcal I(2))=0\), by the actual five-point evaluation maps.
Consequently the long cohomology sequence of (SQ.4) is short exact for
\(k\ne1\); at \(k=1\) its sole additional term is
\(\operatorname{Sym}^{a-1}E\), exactly as in T-039 (5F.15).

The case \(a=1\) is the module \(M_k\) proved in G-017. Its own
tautological sequence gives the equality in the exact representation
group
\[
[M_k]=[E][C_k]-[A_k]+\mathbf1_{k=1}[\mathbf1].
\tag{SQ.5}
\]
Combining the actual sequences just described, including their identical
\(k=1\) connecting terms, proves for every \(a,k\ge0\)
\[
\boxed{[M_{a,k}]
=[\operatorname{Sym}^aE][C_k]
+[\operatorname{Sym}^{a-1}E]\bigl([M_k]-[E][C_k]\bigr).}
\tag{SQ.6}
\]
Here \(\operatorname{Sym}^{-1}E=0\); this convention proves the formula
also at \(a=0\). At \(k=0\) it reduces to \(M_{a,0}=\operatorname{Sym}^aE\).
Thus no unverified vanishing for varying Schur bundles is used.

## 2. A completely specified bivariate character series

Write \(e_g=\chi_E(g)\), \(u_g=\chi_{[3,2]}(g)\), and
\(\epsilon_g=\operatorname{sgn}(g)\). T-038 and A-029 identify
\(\bigoplus C_k\) with the cubic algebra
\(\operatorname{Sym}(U)/(F)\), whose relation has sign character.
G-017 supplies its quotient-bundle module with the proved presentation.
Their exact trace series are
\[
C_g(t)=\frac{1-\epsilon_gt^3}{\det(1-tg\mid U)},\qquad
M_g(t)=\frac{e_g+t-u_gt^2}{\det(1-tg\mid U)}.
\tag{SQ.7}
\]
Taking the traces of (SQ.6) gives the exact rational identity
\[
\boxed{\sum_{a,k\ge0}\chi_{M_{a,k}}(g)s^at^k
=\frac{1+st-u_gst^2-\epsilon_gt^3+
               \epsilon_ge_gst^3}
 {\det(1-sg\mid E)\det(1-tg\mid U)}.}
\tag{SQ.8}
\]
The numerator follows directly by summing
\(C_g\operatorname{Sym}^aE+(M_g-e_gC_g)\operatorname{Sym}^{a-1}E\).

For a complete finite specification, use the following seven-column
data. Columns correspond to the ordinary cycle types in the first row.

| datum | \(1^5\) | \(2\,1^3\) | \(2^2\,1\) | \(3\,1^2\) | \(3\,2\) | \(4\,1\) | \(5\) |
|---|---:|---:|---:|---:|---:|---:|---:|
| class size | 1 | 10 | 15 | 20 | 20 | 30 | 24 |
| \(\chi_{(5)}\) | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| \(\chi_{(4,1)}\) | 4 | 2 | 0 | 1 | -1 | 0 | -1 |
| \(\chi_{(3,2)}\) | 5 | 1 | 1 | -1 | 1 | -1 | 0 |
| \(\chi_{(3,1,1)}\) | 6 | 0 | -2 | 0 | 0 | 0 | 1 |
| \(\chi_{(2,2,1)}\) | 5 | -1 | 1 | -1 | -1 | 1 | 0 |
| \(\chi_{(2,1,1,1)}\) | 4 | -2 | 0 | 1 | 1 | 0 | -1 |
| \(\chi_{(1^5)}\) | 1 | -1 | 1 | 1 | -1 | -1 | 1 |

The character table is the fixed table already verified in T-038 and
T-039. It can be checked by the ordinary permutation actions for
\(E,U\), their exterior powers and sign twists, followed by the
class-size inner products. In particular every entry in (SQ.8) is fixed.
The two determinants can be written without eigenvalue choices:
\[
\det(1-sg\mid E)=
\frac{\prod_{\ell\in\operatorname{cyc}(g)}(1-s^\ell)}{1-s},
\quad
\det(1-tg\mid U)=
\frac{\prod_{\ell\in\operatorname{cyc}_6(g)}
                      (1-\epsilon_g^\ell t^\ell)}{1-\epsilon_gt}.
\tag{SQ.9}
\]
Here the exact six-letter cycle list, by T-038's intertwiner, is
\(1^6,2^3,2^21^2,3^2,6,41^2,51\), in the same column order.

## 3. Fixed integer constants and the proof of their positivity

Define the fixed-degree coefficient function
\[
b_\nu(a,k)=\frac1{120}\sum_{\text{seven classes }g}
|g^{S_5}|\,\chi_\nu(g)\,[s^at^k]\text{(SQ.8)}.
\tag{SQ.10}
\]
For \(0\le r,v<60\) and \(0\le i,j\le3\), set
\[
\boxed{c_{\nu,r,v,i,j}=
\sum_{h=0}^i\sum_{l=0}^j
(-1)^{i+j-h-l}\binom ih\binom jl\,
b_\nu(r+60h,v+60l).}
\tag{SQ.11}
\]
Equations (SQ.8)–(SQ.11), together with the displayed character table,
are explicit definitions of 403,200 fixed integers. Only coefficients
with indices below 240 occur. The complete table is stored as
`FIVE_POINT_SYMMETRIC_QUOTIENT_TABLE.json`, in the order
`labels[nu][r][v][4*i+j]`. It is a single fixed table, independent of
every input parameter in (SQ.1).

The following exact finite certificate proves all their signs. For
each of the seven classes, compute coefficients of
\((1-s)/\prod(1-s^\ell)\) by multiplying the cycle geometric series.
Similarly multiply the six signed geometric series in (SQ.9), then
multiply by \(1-\epsilon_gt\), to obtain the coefficients \(u_k\)
of \(\det(1-tg\mid U)^{-1}\). The two required \(t\)-coefficient
arrays are exactly
\[
C_k=u_k-\epsilon_gu_{k-3},\qquad
X_k=u_{k-1}-u_gu_{k-2}+\epsilon_ge_gu_{k-3},
\tag{SQ.12}
\]
with negative indices zero. The class coefficient in (SQ.10) is
\(s_aC_k+s_{a-1}X_k\). Multiplication by the displayed integer class
sizes and characters, summation and division by 120 give (SQ.10)
exactly; every division in the executed certificate had zero remainder.
Successive forward differences of the four-by-four blocks then give
(SQ.11). `five_point_symmetric_quotient_certificate.py` contains this
entire algorithm, with all iteration limits fixed at 240, 60, four,
and seven. All 403,200 resulting integers were checked exactly.

The \((i,j)=(3,3)\) coefficient is zero in every case. Every other
coefficient with \(i+j>0\) is strictly positive. The following table
records the minimum over all 3600 residue pairs and all fourteen such
index pairs. The zeroth coefficients are nonnegative, both by this
calculation and because (SQ.10) is the multiplicity of the actual module.

| \(\nu\) | minimum of the fourteen positive difference coefficients | number of zero zeroth entries |
|---|---:|---:|
| \((5)\) | 418 | 2 |
| \((4,1)\) | 1487 | 2 |
| \((3,2)\) | 1735 | 2 |
| \((3,1,1)\) | 1978 | 5 |
| \((2,2,1)\) | 1575 | 5 |
| \((2,1,1,1)\) | 1167 | 9 |
| \((1^5)\) | 258 | 19 |

The summary certificate retains the separate minima and maxima of all
sixteen difference positions, for each label. These are exhaustive
finite integer checks with the complete reproducible recurrences
(SQ.9)–(SQ.12), rather than evidence inferred from sampled parameters.

## 4. The rational identity that extends the formula to all parameters

We verify the range of the Newton interpolation exactly. For each class,
the four one-variable factors
\[
\frac1{\det(1-sg\mid E)},\quad
\frac{s}{\det(1-sg\mid E)},\quad
C_g(t),\quad M_g(t)-e_gC_g(t)
\tag{SQ.13}
\]
have denominator dividing \((1-s^{60})^4\) or \((1-t^{60})^4\),
respectively, and common numerator of degree at most 239. Substitution
of the seven cycle lists in (SQ.9), cancellation and polynomial division
verify these 28 identities. All numerator remainders are zero in the
exact certificate, and each numerator degree is checked explicitly.

The argument of G-018 §3 now applies in each variable. On a fixed
residue, a numerator term indexed by \(h\le3\) contributes
\(\binom{q-h+3}{3}\); it equals zero in all early cases \(0\le q<h\).
Thus the full residue sequence is a polynomial from its first value,
with degree at most three. The two products in (SQ.8) consequently give
a polynomial of degree at most three in each quotient parameter.
Its unique Newton expansion, fixed by its four-by-four grid of values,
is therefore
\[
\boxed{b_\nu(60p+r,60q+v)
=\sum_{i=0}^3\sum_{j=0}^3
c_{\nu,r,v,i,j}\binom pi\binom qj
\quad(p,q\ge0).}
\tag{SQ.14}
\]
This proves the identity for every input. The finite sign check in §3
and this rational identity perform distinct, specified jobs.

At the identity the dimension formula offers a useful independent
algebra check:
\[
\dim M_{a,k}
=\binom{a+2}{2}\frac{(k+1)(k^2+2k+2)}2
+\binom{a+2}{3}(k+1)(2k+1).
\tag{SQ.15}
\]
It follows by expanding (SQ.6) using (Q.16) and (Q.15), with the
\(k=1\) correction retained. Its bidegree is at most \((3,3)\),
and its coefficient of \(a^3k^3\) is zero, consistent with the
vanishing mixed third difference. The full character identity, rather
than only this dimension check, proves (SQ.14).

## 5. Positive polytopes, evaluation cost, and complete support

For the input (SQ.1), set \(\nu=\mu\) when \(d+a\) is even and
\(\nu=\mu'\) when \(d+a\) is odd. For each fixed tag
\((r,v,i,j)\) whose table entry is \(c>0\), use integer variables
\(p,q,y,x_1,\ldots,x_i,z_1,\ldots,z_j\) satisfying
\[
\begin{aligned}
60p+r&=a,&60q+v&=k,&p,q&\ge0,&0\le y&\le c-1,\\
1\le x_1&<\cdots<x_i\le p,
&&1\le z_1<\cdots<z_j\le q.
\end{aligned}
\tag{SQ.16}
\]
An empty list of ordered variables contributes one choice. Each strict
integer inequality is written equivalently with a difference at least
one. The equations fix \(p,q\); every other variable lies in a displayed
finite interval. This is a bounded rational polytope with at most nine
variables. Its lattice points are in bijection with a choice of \(y\),
an \(i\)-element subset of \(\{1,\ldots,p\}\), and a \(j\)-element
subset of \(\{1,\ldots,q\}\). Its count is exactly the corresponding
positive term in (SQ.14). The disjoint tagged union of (SQ.16), together
with (SQ.3), proves the announced plethysm formula.

There are at most \(60^2\cdot16=57,600\) fixed tags. Only one residue
pair admits integer \(p,q\), so direct evaluation selects that pair
and uses at most sixteen products of binomial polynomials of degree
at most three. The table lookup is fixed. Integer bit lengths are
\(O(\log(a+2)+\log(k+2)+\log(d+2))\), and schoolbook arithmetic
gives a polynomial bit-cost bound, with the counting arithmetic
quadratic in the combined input bit length.

There is a complete small exceptional set for vanishing. All coefficients
are positive for \(a\ge60\) or \(k\ge60\), by the strictly positive
\((1,0)\) and \((0,1)\) differences. Inside the 60-by-60 square, the
only zeros are the following 44 pairs \((a,k)\), with the effective
label \(\nu\) just specified:

| \(\nu\) | all zero pairs \((a,k)\) |
|---|---|
| \((5)\) | \((0,1),(1,0)\) |
| \((4,1)\) | \((0,0),(0,1)\) |
| \((3,2)\) | \((0,0),(1,0)\) |
| \((3,1,1)\) | \((0,0),(0,1),(0,2),(1,0),(2,0)\) |
| \((2,2,1)\) | \((0,0),(0,1),(1,0),(2,0),(3,0)\) |
| \((2,1,1,1)\) | \((0,0),(0,1),(0,2),(1,0),(1,1),(2,0),(3,0),(4,0),(5,0)\) |
| \((1^5)\) | \((0,k)\) for \(0\le k\le4\); \((1,k)\) for \(0\le k\le2\); \((2,k),(3,k)\) for \(0\le k\le1\); \((a,0)\) for \(4\le a\le9\) or \(a=11\) |

Every other pair is positive. This statement follows from the exhaustive
zeroth-entry check and the positive Newton terms; it includes both axes
and the empty partition. In particular it gives a complete nonvanishing
decision for every outer label in the three-parameter family (SQ.1).

## 6. Exact Grothendieck-framework transport

The sheaf in (SQ.2) is a symmetric Schur functor of the tautological
quotient, tensored with an ordinary ideal power of the specified reduced
point scheme. The balanced chart, relative exterior pairing and
determinant line in (SQ.3) identify its global-section representation
with the normalizer module of the Schur functor. Taking the constant
\(S_5\)-covariant summand is the exact projector T-003.

The equality (SQ.6) lives in exact representation \(K_0\), and is
proved by the displayed exact sheaf and cohomology sequences. Its
lambda-ring interpretation is composition of the Schur operations,
transported by the frame torsor as in SGA 3 I 4.5, 4.7.2–4.7.3 and
SGA 6 VI 3.3. The universal lambda-ring locators are SGA 6 V 4.2,
4.4, 4.8 and 4.9. The projective ideal and its multiplication maps
are the explicitly graded EGA I 9.5.1–9.5.3 construction, and the
corresponding flat-family Hilbert and Quot interpretation is FGA
Exposé 221, Theorems 3.1–3.2. These are the same verified exact
locators and associated-bundle maps in the separate dictionary.
The positive lattice formula follows by the proved finite rational
identities, without an additional unconstructed purity or period map.
