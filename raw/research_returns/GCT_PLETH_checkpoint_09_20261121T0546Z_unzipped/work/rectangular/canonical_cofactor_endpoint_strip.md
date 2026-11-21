# A complete strip of canonical cofactor components

## R-028. Statement

For every integer \(r\ge2\), and every integer \(j\) satisfying
\[
0\le j\le r-2,\qquad j\equiv r\pmod2,
\tag{ES.1}
\]
put
\[
a=r+1,\quad H=r^2+j,\quad b=r^2-r+1+j,
\qquad \lambda=(H^r,j+1).
\tag{ES.2}
\]
For the normalized canonical map
\[
h_{b,a}:\operatorname{Sym}^b\operatorname{Sym}^a V
\longrightarrow\operatorname{Sym}^a\operatorname{Sym}^b V,
\]
the target multiplicity and image multiplicity of \(S_\lambda V\)
are both exactly one. This statement holds for every ambient vector
space in which the label exists; for smaller dimensions the Schur
functor is zero.

The even \(r\), \(j=0\) endpoint is already included in R-026,
and the odd \(r\), \(j=1\) endpoint in R-027. The proof below
establishes every parameter in (ES.1). It makes no historical
novelty claim.

## 1. Highest polynomial and the actual complement pairing

Use an \(a\times a\) matrix whose columns are the \(a\) slot
vectors. Let \(D\) be its determinant and let \(y_i=C_{a,i}\)
be its last-row cofactors. The polynomial is
\[
G=D^{j+1}\prod_{i=1}^a y_i^{r-1}.
\tag{ES.3}
\]
It is separately of degree
\((j+1)+(a-1)(r-1)=b\) in every column. Its first \(a-1=r\)
row weights are \((j+1)+a(r-1)=H\), and its last row weight
is \(j+1\). A raising substitution from an earlier row into a
later row leaves each relevant determinant or cofactor unchanged,
or produces a repeated row. Hence (ES.3) is highest of weight
\(\lambda\). A column permutation multiplies it by
\(\operatorname{sgn}^{j+1+a(r-1)}=\operatorname{sgn}^{H}=1\).
It is a nonzero symmetric slot polynomial in the indicated target.

For completeness, the multiplicity assertion uses the actual perfect
complement pairing of BS.10–BS.13. Wedge complementary column
vectors into the fixed volume tensor, then apply the primitive
Young projectors on the two tensor powers. Its perfectness identifies
\(S_\lambda\) with
\(\det^H\otimes S_{(a(r-1))}^*\). On the balanced weight
spaces it pairs content \((b^a)\) with \(((r-1)^a)\), and a
slot permutation changes the pairing by \(\operatorname{sgn}^H\).
Since \(H\) is even, the literal symmetric projectors
\(a!^{-1}\sum_\sigma\sigma\) on the two sides correspond.
Thus the target multiplicity is the multiplicity of the row
\((a(r-1))\) in
\(\operatorname{Sym}^a\operatorname{Sym}^{r-1}\).
Its highest weight space is spanned by \((e_1^{r-1})^a\), so it
has dimension one. This is the same explicit pairing and projector
construction proved in BS.10–BS.13, applied with \(k=r-1\).

## 2. The canonical annihilator map to be detected

Write \(K_{a,b}\) for the kernel of the transpose canonical map
\(h_{a,b}\); polynomial duality uses the normalized tensor
pairing of K.16–K.22. Retaining one of the \(a\) symmetric slots
defines the injective normalized map \(\delta\). The literal
coefficient-extraction map \(T_{r,r,b}\) polarizes the other
\(r\) slots by \(r\) copies of their common vector.

The exact annihilator inclusion proved in K.16–K.22 and P.9–P.16
applies here because
\[
b-r=(r-1)^2+j\ge(r-1)^2.
\tag{ES.4}
\]
Sra's Theorem 1.3 supplies surjectivity of the lower canonical map
\(h_{b-r,r}\). The specified morphisms therefore give
\[
\delta K_{a,b}\subset
\ker T_{r,r,b}\otimes\operatorname{Sym}^b V^*.
\tag{ES.5}
\]
All normalized scalar factors in this inclusion are those already
computed in the cited equations. In particular none is zero.

Since the relevant target multiplicity is one, a nonzero value of
\((T_{r,r,b}\otimes1)\delta G\) proves that its entire copy lies
in the image of \(h_{b,a}\). We now compute that value. Set the
first-row bases of the first \(r\) columns to zero, polarize in
direction \(e_1\), and retain the first-row coordinate \(w\) in
the last column. The coefficient to be detected is
\[
[x_1^r\cdots x_r^r w^j]G.
\tag{ES.6}
\]
Its first-row total degree is exactly \(r^2+j=H\).

## 3. Literal cofactor specialization

Let \(\zeta_1,\ldots,\zeta_r\) be the distinct roots of
\(z^r+1\), put \(a_i=2+\zeta_i\) for \(i\le r\), and put
\(a_{r+1}=0\). All \(a_i\), \(i\le r\), are nonzero.
Form the invertible matrix
\[
A=\begin{pmatrix}
a_1^2&\cdots&a_r^2\\
\vdots&&\vdots\\
a_1^r&\cdots&a_r^r\\
a_1&\cdots&a_r
\end{pmatrix},\qquad
B=A^{-T}(I_r\mid-\mathbf1).
\tag{ES.7}
\]
Factoring \(a_i\) from column \(i\) leaves a permutation of the
Vandermonde exponents \(0,1,\ldots,r-1\), proving invertibility.
Use \(B\) as the lower \(r\) rows of the slot matrix. Put
\[
\eta=(-1)^r(\det A)^{-1},\quad
S=\sum_{i=1}^r x_i,\quad Z=\sum_{i=1}^r a_i x_i,
\quad Q(s,z)=(z-2s)^r+s^r.
\]
The cofactors, computed by their defining minors, are exactly
\[
D=\eta(S+w),\qquad y_i=\eta((S+w)a_i-Z).
\tag{ES.8}
\]
One direct verification is that \(B\mathbf1=0\) and
\(B(a_1,\ldots,a_r,0)^T=e_r\). The displayed cofactor row
has zero pairing with the first row and pairs with each lower row
as the determinant times the appropriate Kronecker delta; the last
first-row cofactor is \((-1)^r(\det A)^{-1}\), fixing the scalar.

Multiplying (ES.8), with every sign retained, gives
\[
G=(-1)^{r-1}\eta^H(S+w)^{j+1}Z^{r-1}
Q(S+w,Z)^{r-1}.
\tag{ES.9}
\]
Indeed \(\prod_{i\le r}(s a_i-z)=(-1)^rQ(s,z)\), while the
last cofactor contributes \((-z)^{r-1}\).

## 4. Exact binary contraction

For two binary forms of degree \(N\), use the unnormalized apolar
pairing
\[
\langle P,R\rangle_N=P(-\partial_z,\partial_s)R\big|_{s=z=0}.
\tag{ES.10}
\]
Extraction of the \(w^j\) coefficient in (ES.9) is
\(j!^{-1}\partial_s^j\). Extraction of \(x_1^r\cdots x_r^r\)
then applies
\((r!)^{-r}\prod_i(\partial_s+a_i\partial_z)^r\).
Since \(Q(-\partial_z,\partial_s)=
\prod_i(\partial_s+a_i\partial_z)\), the result is exactly
\[
\frac{(-1)^{r-1}\eta^H}{j!(r!)^r}
\left\langle z^jQ^r,
s^{j+1}z^{r-1}Q^{r-1}\right\rangle_H.
\tag{ES.11}
\]
The extra factor \(z^j\) supplies precisely \(\partial_s^j\).
The chain rule for the determinant-one substitution \(z\mapsto
z-2s\), already explicitly checked in BS.28–BS.30, changes the
pairing to
\[
\left\langle (z+2s)^jQ_0^r,
s^{j+1}(z+2s)^{r-1}Q_0^{r-1}\right\rangle_H,
\qquad Q_0=z^r+s^r.
\tag{ES.12}
\]

Choose the \(z^{ri}\) term of the first power of \(Q_0\), and
the \(z^\ell\) term of its extra factor. The other argument
must use the \(z^{r(r-i)}\) term and extra \(z^{j-\ell}\).
These are the only matches: the sum of the two extra exponents is
congruent to \(j\) modulo \(r\), lies between zero and
\(j+r-1\), and \(j<r\). Thus it equals \(j\).
In particular \(1\le i\le r\) and \(0\le\ell\le j\).
All powers of 2 multiply to \(2^{r-1}\). As \(H\) is even,
the apolar sign can be written as \((-1)^{ri+\ell}\). Therefore
(ES.12) is exactly \(2^{r-1}F_{r,j}\), where
\[
\boxed{F_{r,j}=
\sum_{i=1}^r\sum_{\ell=0}^j
(-1)^{ri+\ell}
\binom ri\binom{r-1}{r-i}
\binom j\ell\binom{r-1}{j-\ell}
(ri+\ell)!\,(H-ri-\ell)!.}
\tag{ES.13}
\]
We next prove that this actual integer is strictly positive.

## 5. A uniform strict factorial bound

First take \(r\ge5\). In the endpoint \(i=r\), let
\(t_\ell\) denote the absolute value of its \(\ell\)-th term.
For \(\ell<j\),
\[
\frac{t_{\ell+1}}{t_\ell}
=\frac{(j-\ell)(r^2+\ell+1)}
       {(\ell+1)(r-j+\ell)}
\ge\frac{r^2+j}{j(r-1)}>1.
\tag{ES.14}
\]
The first factor is minimized at \(\ell=j-1\); so is the
second ratio, since its numerator minus denominator is positive
and constant. The last term has sign
\((-1)^{r^2+j}=1\). Pairing consecutive terms backwards gives
the endpoint contribution at least \(t_j-t_{j-1}\). For \(j=0\)
the same bound holds with \(t_{-1}=0\). Consequently it is at least
\[
H!\left(1-\frac{j(r-1)}{r^2+j}\right)
\ge H!\frac{4(r-1)}{r^2+r-2}.
\tag{ES.15}
\]
The last rational function decreases in \(j\), and its value at
\(j=r-2\) is the displayed lower bound.

For \(1\le i\le r-1\), selecting a term in the binomial
convolution proves
\[
\binom H{ri+\ell}
\ge\binom{r^2}{ri}\binom j\ell,
\qquad
\binom{r^2}{ri}\ge{\binom ri}^{r}.
\tag{ES.16}
\]
The second inequality selects degree \(i\) in each of the \(r\)
factors \(((1+z)^r)^r\). Also
\(\binom{r-1}{r-i}=(i/r)\binom ri\) and
\(\binom ri\ge r\). Divide the absolute terms of (ES.13) by
\(H!\), apply (ES.16), cancel \(\binom j\ell\), and sum
\(\binom{r-1}{j-\ell}\) over \(\ell\). The total absolute
interior contribution is at most
\[
H!\,(r-1)2^{r-1}r^{2-r}
<H!\frac{4(r-1)}{r^2+r-2}.
\tag{ES.17}
\]
For the strict inequality, \(r\ge5\) gives
\((2/r)^{r-2}\le(2/r)^3=8/r^3<2/(r^2+r-2)\).
The final inequality is equivalent to
\(4(r^2+r-2)<r^3\); subtracting its left side gives at least
\(r^2-4r+8=(r-2)^2+4>0\), since \(r-4\ge1\).
Equations (ES.15)–(ES.17) prove \(F_{r,j}>0\).

The remaining four pairs \((r,j)\) have the following exact
values, obtained by the finite factorial sum (ES.13):

| \((r,j)\) | \(F_{r,j}/(r!)^r\) |
|---|---:|
| \((2,0)\) | 8 |
| \((3,1)\) | 12,960 |
| \((4,0)\) | 63,705,600 |
| \((4,2)\) | 13,208,832,000 |

Each is positive. These exhaust all the parameters of (ES.1) with
\(r<5\).

## 6. Exact conclusion and verification scope

Combining (ES.11)–(ES.17), the literal coefficient (ES.6) is
\[
\boxed{\frac{(-1)^{r-1}\eta^H2^{r-1}}{j!(r!)^r}
F_{r,j}\ne0.}
\tag{ES.18}
\]
This detects the actual polarization in (ES.5). Its nonvanishing,
the one-dimensional target multiplicity, and the perfect transpose
pairing prove the claimed image multiplicity one. Extending the
coefficient field to the splitting field used in (ES.7) detects a
nonzero rational polynomial map, because field extension is
injective. Inclusion into a larger ambient vector space commutes
with the tensor projectors, retained-slot map and polarization,
giving the stated ambient-dimension transfer.

The lower-map primary source is Sra, *The q-Foulkes problem III:
On Foulkes' conjecture with a graded inner factor*, Theorem 1.3,
[primary PDF](https://suvrit.github.io/papers/qfoulkes3/qfoulkes3-v1.pdf).
The full morphism normalization is K.16–K.22 and P.9–P.16; the
complement pairing is BS.10–BS.13. These are the actual inputs,
with the new parameter verification (ES.4).

The companion audit `verify_cofactor_endpoint_strip.py` compares
fully expanded rational binary forms to (ES.13), checks literal
matrix minors and coefficient extraction over finite fields, and
records its exact receipts separately. Those calculations support
the explicit identities; the uniform nonvanishing proof is
(ES.14)–(ES.17).
