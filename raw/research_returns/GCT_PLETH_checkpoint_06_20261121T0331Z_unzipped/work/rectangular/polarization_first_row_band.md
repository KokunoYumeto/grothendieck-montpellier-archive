# Exact common polarization on the first boundary row band

Statements **R-019** and **R-020**. Written and checked on 21 November
2026 UTC by GPT-6 Astra Pro, `/root/rectangular_cases`; effort setting
not exposed. R-019 is an explicit coefficient calculation. R-020 uses
the complementary Schur pairing and the multilinear Young-symmetrizer
map to identify the entire indicated band. No historical novelty claim
is made.

Throughout, \(T_{r,L,b}\) means the coefficient-extraction map

\[
T_{r,L,b}f(v_1,\ldots,v_r;w)
=[t_1^L\cdots t_r^L]f(v_1+t_1w,\ldots,v_r+t_rw),
\tag{N.1}
\]

from \(\operatorname{Sym}^r(\operatorname{Sym}^bV)\) to
\(\operatorname{Sym}^{rL}V\otimes
\operatorname{Sym}^r(\operatorname{Sym}^{b-L}V)\).
The product of ordinary differential operators is \((L!)^rT_{r,L,b}\).

## R-019. A nonrectangular boundary component with an exact coefficient

Let \(r\ge2\), \(L\ge1\), and \(rL\) be even. Put

\[
b=rL-1,\qquad C=r(L-1),\qquad
\lambda=((rL)^{r-1},C),\qquad
s=\lfloor r/2\rfloor,\quad t=r-s.
\tag{N.2}
\]

The source \(\lambda\)-isotypic component has multiplicity one, and
\(T_{r,L,b}\) is injective on that component in every ambient dimension.
Here a Schur functor of length greater than \(\dim V\) is zero.

An explicit highest vector in dimension \(r\) is as follows. Let
\(M=(v_1,\ldots,v_r)\) be the matrix of vector-slot generators. Write
\(D=\det M\), let \(B\) be its first \(r-1\) rows, and set

\[
y_i=(-1)^{r+i}\det B_{\widehat i},\qquad
f=D^C\prod_{i=1}^r y_i.
\tag{N.3}
\]

The hat deletes column \(i\). The same formula with \(D^0=1\) defines
the vector in dimension \(r-1\) when \(L=1\).

To specify an exact evaluation of its image, split the column indices
into \(I=\{1,\ldots,s\}\) and \(J=\{s+1,\ldots,r\}\). Let \(A\)
be the \((r-2)\times r\) matrix whose rows, in the indicated order, are

\[
e_i-e_s\quad(1\le i<s),\qquad
e_{s+j}-e_r\quad(1\le j<t),
\tag{N.4}
\]

and put \(c=-e_s+e_r\). Here \(e_i\) denotes a row coordinate vector
in this displayed matrix construction. Take the vector-slot matrix
\(M_0\) with first row zero, middle rows \(A\), and last row \(c\).
The common vector in (N.1) is the first vector-coordinate basis vector
\(e_1\). Then

\[
\boxed{
T_{r,L,b}f(M_0;e_1)
=(-1)^s
\binom{r(L-1)}{sL-t}
\frac{(sL)!\,(tL)!}{(L!)^r}
\ne0.}
\tag{N.5}
\]

For \(L=1\), the last row of \(M_0\) can be deleted: the polynomial
\(f\) does not use it. Thus the same evaluation proves the statement
in the minimum nonzero ambient dimension in that case.

### Proof of the highest vector and its slot symmetry

Every cofactor \(y_i\) is a flag minor of height \(r-1\), with row
highest weight \((1^{r-1},0)\). Their product has weight
\((r^{r-1},0)\). Multiplication by \(D^C\) adds \((C^r)\), giving
exactly \(\lambda\) in (N.2). The polynomial is nonzero because it is
a product of nonzero polynomials in an integral domain.

Each column belongs to \(r-1\) of the cofactor factors, so its total
degree in \(f\) is \(C+r-1=b\). A column permutation \(\sigma\)
sends the cofactor coordinates to
\(\operatorname{sgn}(\sigma)y_{\sigma(i)}\), with the inverse indexing
when the opposite permutation convention is used. Consequently its
effect on their product is \(\operatorname{sgn}(\sigma)^r\). The
determinant power contributes \(\operatorname{sgn}(\sigma)^C\).
The combined character is
\(\operatorname{sgn}(\sigma)^{C+r}
=\operatorname{sgn}(\sigma)^{rL}=1\).
Thus (N.3) belongs to the symmetric-slot source of (N.1).

### Proof of the coefficient and all signs

Replace the first row of \(M_0\) by independent variables
\(x=(x_1,\ldots,x_r)\), and write

\[
X=\sum_{i\in I}x_i,\qquad Y=\sum_{i\in J}x_i.
\]

The kernel of the matrix \(A\) in (N.4) consists exactly of vectors
constant on each of the two groups. The cofactor vector \(y\) of
\(B=[x;A]\) lies in that kernel and satisfies \(x\cdot y=0\).
Its last coordinate can also be computed directly:

\[
y_r=\det B_{\widehat r}=(-1)^{s-1}X.
\]

Indeed the rows belonging to the second group leave an identity block
on columns \(s+1,\ldots,r-1\), and the remaining determinant has rows
\((x_1,\ldots,x_s)\) and \(e_i-e_s\), \(1\le i<s\). Expansion gives
\((-1)^{s-1}\sum_{i\le s}x_i\). The two kernel conditions now give
the full vector, as polynomial identities:

\[
y_i=(-1)^sY\quad(i\in I),\qquad
y_i=(-1)^{s+1}X\quad(i\in J).
\tag{N.6}
\]

Expansion of \(D\) in its last row gives

\[
D=c\cdot y=(-1)^{s+1}(X+Y).
\tag{N.7}
\]

Combining (N.6)–(N.7), the specialization of (N.3) is

\[
(-1)^{(s+1)C+sr+t}(X+Y)^C X^tY^s.
\]

Since \(C+r=rL\) is even, its sign exponent is congruent to
\(C+t\equiv r+t\equiv s\pmod2\). Thus it equals

\[
(-1)^s(X+Y)^C X^tY^s.
\tag{N.8}
\]

To obtain \(\prod_i x_i^L\), the total \(X\)-degree must be \(sL\)
and the total \(Y\)-degree must be \(tL\). The unique relevant term
of \((X+Y)^C\) has \(X\)-degree \(sL-t\). Its coefficient is
\(\binom C{sL-t}\). Expansion of \(X^{sL}\) and \(Y^{tL}\) then
gives the two multinomial coefficients
\((sL)!/(L!)^s\) and \((tL)!/(L!)^t\).

For even \(r\), \(s=t\) and \(sL-t=s(L-1)\) lies between zero
and \(C\). For odd \(r\), the assumed evenness of \(rL\) makes
\(L\ge2\) even; then \(sL\ge t=s+1\) and \(tL\ge s\), which
give the same two bounds. All factorials are therefore defined and
the coefficient is nonzero.

Finally the first row of \(M_0\) is zero, so substitution in (N.1)
replaces this row exactly by \((t_1,\ldots,t_r)\). Hence the computed
coefficient is precisely the value in (N.5), with no omitted derivative
or averaging factor. This proves nonvanishing of the actual map.

The multiplicity-one assertion follows from the exact pairing and
multilinear identification in R-020 below. A nonzero map on a single
irreducible source copy is injective. The tensor map (N.1) is natural
and is given by tensor-position symmetrizations and permutations
independent of dimension. Thus its map on a Schur multiplicity space
is the same in every ambient dimension where that Schur functor is
nonzero. Alternatively the above construction already uses the
minimum possible dimension: \(r\) for \(C>0\), and \(r-1\) for
\(C=0\); embedding that space preserves the displayed highest vector
and its nonzero image.

### Actual examples and relation to the original boundary

\[
\begin{array}{c|c|c|c|r}
r&L&b&\lambda&Tf(M_0;e_1)\\\hline
3&2&5&(6,6,3)&-6\\
4&1&3&(4,4,4,0)&4\\
4&4&15&(16,16,16,12)&4527600\\
5&2&9&(10,10,10,10,5)&2700\\
6&1&5&(6,6,6,6,6,0)&-36
\end{array}
\tag{N.9}
\]

For every even \(r\ge2\), the original common power \(L=r\) gives
the explicit surviving component

\[
\lambda=((r^2)^{r-1},r^2-r)
\quad\text{at}\quad b=r^2-1.
\tag{N.10}
\]

Its second row is \(r^2\) for \(r\ge3\), outside the range
\(\lambda_2\le r(r-1)-1\) proved in R-018. This result concerns the
specified common-polarization morphism; it does not identify an
additional component of a different map without a further morphism
calculation.

## R-020. The complete band \(\lambda_1\le b+1\)

Fix \(r\ge2,L\ge1,b=rL-1\), and put \(H=b+1=rL\). In the source
\(\operatorname{Sym}^r(\operatorname{Sym}^bV)\), the sum of all
isotypic components with \(\lambda_1\le H\) is

\[
\boxed{
\begin{cases}
S_{(H^{r-1},H-r)}V,&H\text{ even},\\
S_{((H-1)^r)}V,&H\text{ odd},
\end{cases}}
\tag{N.11}
\]

with multiplicity one in each case. The map \(T_{r,L,b}\) is
injective on the entire band in the first line. In the second line
the entire displayed component is its kernel in that band. This
classifies the map on every source component with first row at most
\(b+1\), for every \(r,L\).

### 1. The exact complementary Schur pairing

Work first in the \(r\)-dimensional slot space \(E=\mathbf Q^r\).
Every partition in \((\operatorname{Sym}^bV)^{\otimes r}\) has at
most \(r\) rows. For \(\lambda\vdash rb\) inside the rectangle
\((H^r)\), define

\[
\nu=(H-\lambda_r,\ldots,H-\lambda_1).
\tag{N.12}
\]

It is a partition of \(rH-rb=r\). There is a nonzero perfect
\(GL(E)\)-equivariant pairing

\[
S_\lambda E\otimes S_\nu E\longrightarrow(\det E)^H.
\tag{N.13}
\]

An explicit construction uses the exterior columns. If the \(H\)
column heights of \(\lambda\), with zero heights included, are
\(h_1\ge\cdots\ge h_H\), those of \(\nu\) are
\(r-h_H,\ldots,r-h_1\). Embed each Schur module as its Cartan
component in the corresponding tensor product of exterior powers.
Reverse the factors of the second module and use, in each column,
the actual exterior multiplication

\[
\Lambda^{h_j}E\otimes\Lambda^{r-h_j}E\longrightarrow\Lambda^rE.
\]

Their tensor product gives (N.13). It is nonzero: pair the highest
vector formed from \(e_1\wedge\cdots\wedge e_{h_j}\) in each first
factor with the lowest vector formed from
\(e_{h_j+1}\wedge\cdots\wedge e_r\) in its paired second factor.
The value is \((e_1\wedge\cdots\wedge e_r)^{\otimes H}\).
Irreducibility makes the resulting pairing perfect.

Torus weights in this pairing add to \((H^r)\). It therefore
restricts to a perfect pairing between the balanced weight
\((b^r)\) on the first factor and the multilinear weight
\((1^r)\) on the second. Literal permutation matrices act on the
target by \(\operatorname{sgn}^H\). Consequently

\[
(S_\lambda E)_{(b^r)}
\simeq\operatorname{sgn}^H\otimes
\bigl((S_\nu E)_{(1^r)}\bigr)^*
\quad\text{as actual }S_r\text{-modules}.
\tag{N.14}
\]

### 2. The multilinear Young-symmetrizer map

Let \(e_1,\ldots,e_r\) be the basis of \(E\). The map

\[
\mathbf Q[S_r]\longrightarrow(E^{\otimes r})_{(1^r)},
\qquad
\sigma\longmapsto
e_{\sigma(1)}\otimes\cdots\otimes e_{\sigma(r)}
\tag{N.15}
\]

is an isomorphism: the displayed tensors form the entire multilinear
basis. Literal basis permutations act by left multiplication on the
group algebra. Give tensor positions the right action
\((v_1\otimes\cdots\otimes v_r)\rho
=v_{\rho(1)}\otimes\cdots\otimes v_{\rho(r)}\).
Then (N.15) also intertwines right multiplication.

Choose a tableau of shape \(\nu\), take its row symmetrizer and
column antisymmetrizer, and divide their product by its nonzero
Young-symmetrizer scalar to obtain a primitive Young idempotent
\(e_\nu\). The image \((E^{\otimes r})e_\nu\) is the corresponding
Schur-module realization \(S_\nu E\). Restricting (N.15) to the
left ideal \(\mathbf Q[S_r]e_\nu\) thus gives the exact map

\[
[\nu]\simeq\mathbf Q[S_r]e_\nu
\xrightarrow{\ \sim\ }(S_\nu E)_{(1^r)}.
\tag{N.16}
\]

Specht modules over \(\mathbf Q\) are self-dual: average any positive
definite rational form over the finite group and use it to identify
the module with its dual. Equations (N.14)–(N.16) prove

\[
(S_\lambda E)_{(b^r)}\simeq
\operatorname{sgn}^H\otimes[\nu].
\tag{N.17}
\]

The Cauchy balanced-weight identification identifies the highest
\(\lambda\)-multiplicity space of
\(\operatorname{Sym}^r(\operatorname{Sym}^bV)\) with the invariant
subspace of (N.17). Its dimension is one for
\(\nu=(r)\) when \(H\) is even, one for \(\nu=(1^r)\) when \(H\)
is odd, and zero for every other \(\nu\). Taking complements in
(N.12) gives exactly (N.11). This proves the complete source-band
description, including all zero multiplicities.

### 3. The map on the two actual bands

For even \(H=rL\), the sole source component is the component in
R-019. Formula (N.5) proves nonvanishing, so its multiplicity-one
source is mapped injectively.

For odd \(H=rL\), both \(r\) and \(L\) are odd and \(b=H-1\) is
even. The highest vector of the unique source component is
\(D^b\), which is symmetric under slot permutations. Every term in
the coefficient extraction (N.1) puts \(rL=b+1\) copies of the
common vector into \(b\) determinant factors. At least one factor
receives two copies and is zero by alternating multilinearity.
Thus \(T_{r,L,b}(D^b)=0\). Equivariance kills its entire irreducible
component, proving the second line of the band classification.

No other source component belongs to this band by (N.17). Combined
with R-018, the unclassified boundary components therefore satisfy
both

\[
\boxed{\lambda_1\ge rL+1,\qquad
       \lambda_2\ge(r-1)L.}
\tag{N.18}
\]

The determinant component in the odd case is already explicitly
classified and is not included in this remaining range. Statements
R-011, R-012, R-015 and R-016 give additional complete finite kernels;
(N.18) is a uniform consequence of the exact maps proved here.
