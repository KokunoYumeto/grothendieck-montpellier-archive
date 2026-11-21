# Two cofactor families beyond the first-row boundary

Statement **R-025**. Written and checked on 21 November 2026 UTC by
GPT-6 Astra Pro, agent /root/rectangular_cases; effort setting not exposed.
Every assertion below concerns the displayed actual polynomial maps.
No historical novelty claim is made.

## 1. Explicit canonical image components at the critical degree

Let \(a\ge3\), put \(r=a-1\), \(b=r^2-1\), and \(H=r^2+1=b+2\).
Use the normalized canonical grid map
\[
h_{b,a}:\operatorname{Sym}^b(\operatorname{Sym}^a V)
\longrightarrow\operatorname{Sym}^a(\operatorname{Sym}^b V).
\tag{Cof.1}
\]

For every **odd \(a\ge3\)**, equivalently every even \(r\ge2\), set
\[
\lambda_{\mathrm{odd}\ a}
=(r^2+1,(r^2)^{r-2},r^2-2,r^2-r).
\tag{Cof.2}
\]
For every **even \(a\ge4\)**, equivalently every odd \(r\ge3\), set
\[
\lambda_{\mathrm{even}\ a}
=((r^2+1)^r,r^2-2r-1).
\tag{Cof.3}
\]
Both are partitions of \(ab\). In every dimension at least their
number of rows,
\[
\boxed{
[S_\lambda V:\operatorname{im}h_{b,a}]
=[S_\lambda V:\operatorname{Sym}^a(\operatorname{Sym}^b V)]
=1
}
\tag{Cof.4}
\]
for the corresponding displayed \(\lambda\).

The proof supplies a highest vector in the dual target whose
last-slot common polarization is nonzero. The exact annihilator
inclusion (K.22) then proves (Cof.4). Thus this is a statement about
the canonical map on its unique target copy.

For example the families include
\[
\begin{array}{c|c|c}
a&b&\lambda\\\hline
3&3&(5,2,2)\\
4&8&(10,10,10,2)\\
5&15&(17,16,16,14,12)\\
6&24&(26,26,26,26,26,14)\\
7&35&(37,36,36,36,36,34,30).
\end{array}
\tag{Cof.5}
\]
Their first row is \(r^2+1\). Apart from coincidences with previously
established full-map cases, these labels lie outside the two
component ranges \(\lambda_1\le r^2\) and
\(\lambda_2\le r(r-1)-1\) of R-022.

## 2. Two actual highest polynomials

First use \(n\ge3\) slots and \(n\) coordinate rows. Write
\[
X=(X_{ij})_{1\le i,j\le n},\qquad
x_j=X_{1j},\qquad D=\det X.
\]
Let \(C_{ij}=(-1)^{i+j}\det X_{\widehat i,\widehat j}\) be the
cofactor matrix, and put
\[
y_j=C_{nj},\qquad z_j=C_{n-1,j},\qquad
\mathcal S(X)=\sum_{j=1}^n x_j z_j^2\prod_{i\ne j}y_i.
\tag{Cof.6}
\]

For every odd integer \(H\ge n+1\), define
\[
F_{n,H}=D^{H-n-2}\mathcal S(X).
\tag{Cof.7}
\]
The possible exponent \(-1\), occurring at \(H=n+1\), is
interpreted by the actual polynomial quotient
\(\mathcal S(X)/D\). This quotient is polynomial: on the dense
rank-\((n-1)\) locus of \(D=0\), all nonzero rows of the cofactor
matrix are proportional. In its fraction field \(z_j=c\,y_j\),
and
\[
\mathcal S=c^2\left(\prod_i y_i\right)\sum_jx_jy_j=0.
\]
The last equality is the cofactor identity
\(\sum_jX_{1j}C_{nj}=0\). The determinant hypersurface is integral
(the generic determinant is irreducible), so vanishing on this
dense open subset gives \(D\mid\mathcal S\) in the polynomial ring.
The same conclusion holds on charts where another cofactor row
is nonzero; one dense chart already proves the divisibility.

Each column of \(\mathcal S\) has degree \(n\). Thus (Cof.7)
has degree \(H-2\) in each slot, and its row weight is
\[
\lambda^F_{n,H}
=(H,(H-1)^{n-3},H-3,H-n).
\tag{Cof.8}
\]
This is a partition for \(n\ge3\) and \(H\ge n+1\).

Here is a direct highest-vector verification. Under a row
transvection \(X\mapsto (I+tE_{j,i})X\), \(i<j\), the cofactor
matrix changes by \(C\mapsto(I-tE_{i,j})C\), and \(D\) and the
first row stay fixed. The row \(y\) stays fixed. The only such
change affecting \(z\) is \(z\mapsto z-t y\). Under that change,
the difference of the two numerators in (Cof.6) is
\[
-2t\left(\prod_i y_i\right)\sum_jx_jz_j
+t^2\left(\prod_i y_i\right)\sum_jx_jy_j=0.
\tag{Cof.9}
\]
Both sums are zero cofactor identities, since \(n-1,n\ne1\).
Therefore \(F_{n,H}\) is a highest polynomial of weight (Cof.8).

A permutation of columns multiplies \(D\) by its sign and each
cofactor row by that sign while permuting its entries. Hence the
numerator in (Cof.6) has sign character to the power \(n+1\).
The total permutation character of (Cof.7) is
\(\operatorname{sgn}^{H-1}=1\). It consequently belongs to
\(\operatorname{Sym}^n(\operatorname{Sym}^{H-2}V)\).

The second polynomial, for every even \(H\ge2n\), is
\[
G_{n,H}=D^{H-2n}\prod_{j=1}^n y_j^2.
\tag{Cof.10}
\]
It is polynomial, symmetric in the slots, and highest by the
same transvection formulas. Its separate slot degree is \(H-2\),
and its row weight is
\[
\lambda^G_{n,H}=(H^{n-1},H-2n).
\tag{Cof.11}
\]

## 3. Exact multiplicity-one identification

We give the complement morphism that determines the multiplicities
of these highest vectors. For every partition \(\lambda\) fitting
in the \(n\times H\) rectangle, put
\[
\nu=(H-\lambda_n,\ldots,H-\lambda_1).
\]
Exterior multiplication of complementary columns gives the perfect
\(GL_n\)-equivariant pairing
\[
S_\lambda\mathbf Q^n\otimes S_\nu\mathbf Q^n
\longrightarrow(\det\mathbf Q^n)^H.
\tag{Cof.12}
\]
For precision, apply the wedge pairing on each column after
realizing both Schur modules by their column alternations and row
symmetrizations. On the complementary standard highest and lowest
tableaux it is a nonzero product of coordinate determinants.
Its map from either irreducible Schur factor to the dual of the
other, with determinant twist, is therefore nonzero and hence an
isomorphism. This proves perfectness and fixes the determinant
character.

Restrict (Cof.12) to content \(((H-2)^n)\) in the first factor and
content \((2^n)\) in the second. Diagonal weights add to \((H^n)\),
so these are perfectly paired weight spaces. Permutation matrices
act on the one-dimensional target by \(\operatorname{sgn}^H\).
Taking permutation invariants, and using the Cauchy decomposition
of matrix polynomials, gives the exact multiplicity equalities
\[
[S_\lambda:\operatorname{Sym}^n\operatorname{Sym}^{H-2}]
=
\begin{cases}
[S_\nu:\Lambda^n(\operatorname{Sym}^2)],&H\text{ odd},\\
[S_\nu:\operatorname{Sym}^n(\operatorname{Sym}^2)],&H\text{ even}.
\end{cases}
\tag{Cof.13}
\]
The second step is the literal content-\((2^n)\) matrix-polynomial
space \((\operatorname{Sym}^2\mathbf Q^n)^{\otimes n}\).
Its sign-isotypic projector is \(n!^{-1}\sum_\sigma
\operatorname{sgn}(\sigma)\sigma\), whose image is
\(\Lambda^n(\operatorname{Sym}^2\mathbf Q^n)\) under the usual
normalized alternating inclusion. Its invariant projector gives
the symmetric power. These are the actual maps in (Cof.13).

For (Cof.8), the complementary partition is
\[
\nu=(n,3,1^{n-3},0).
\]
Its weight space in \(\Lambda^n(\operatorname{Sym}^2\mathbf Q^n)\)
has dimension one. To see this, view a wedge basis as a set of
distinct quadratic monomials, with a loop counting twice toward a
vertex degree. No monomial uses the \(n\)-th variable. Degree \(n\)
at the first variable forces its loop and all \(n-2\) available
edges to the other variables. The one remaining quadratic must
be the loop at the second variable, which raises its degree from
one to three. Thus the unique wedge is
\[
e_1^2\wedge e_1e_2\wedge\cdots\wedge e_1e_{n-1}
\wedge e_2^2.
\tag{Cof.14}
\]
It is highest: replacing any higher-index variable by a
lower-index variable yields either zero or a repeated wedge
factor. Thus its irreducible type occurs once. For (Cof.11) the
complement is the row \((2n)\), whose unique highest vector in
\(\operatorname{Sym}^n(\operatorname{Sym}^2)\) is
\((e_1^2)^n\). This also occurs once. Equation (Cof.13) proves
multiplicity one for both displayed original types.

## 4. A concrete cofactor specialization

We specify matrices producing the needed positive coefficients.
Let the slot set be a disjoint union \(I\sqcup J\), with
\(|I|=s\), \(|J|=t\), \(s+t=n\), both sets nonempty. Choose a
reference slot \(q\in I\). There exists an explicit unimodular
\((n-1)\times(n-1)\) matrix \(A\) whose last row is the indicator
of \(J\), in the coordinates excluding \(q\): take one \(j_0\in J\),
keep every coordinate row except \(e_{j_0}\), and replace that row
by \(\sum_{j\in J}e_j\), putting it last.

For \(F\), also choose a nonempty singleton \(K=\{p\}\subset
I\setminus\{q\}\), and put the row \(e_p\) penultimate. The
remaining coordinate rows, in increasing order, precede these
last two rows. This explicitly gives the required unimodular
matrix in this case.

Let \(B_0\) have rows \(e_i-e_q\), for \(i\ne q\), in the same
coordinate order, and set
\[
B=A^{-T}B_0,\qquad
X=\begin{pmatrix}x_1&\cdots&x_n\\B\end{pmatrix},\qquad
X_I=\sum_{i\in I}x_i,\quad Y_J=\sum_{j\in J}x_j,\quad
S=X_I+Y_J.
\tag{Cof.15}
\]
All entries of \(B\) are integers. Direct solution of the equations
\(B_0v=(v_i-v_q)_{i\ne q}\) shows
\[
D=\eta S,\qquad
C_{\ell+1,i}=\eta\bigl(S A_{\ell,i}
                       -\sum_j A_{\ell,j}x_j\bigr),
\quad \eta\in\{1,-1\},
\tag{Cof.16}
\]
where the missing column \(A_{\ell,q}\) is zero. The scalar
\(\eta=D(1,0,\ldots,0)\) is the signed determinant of the displayed
constant row matrix and is a unit. Formula (Cof.16) is also the
identity \(C=D X^{-T}\); it fixes its scalar exactly.

The last two chosen rows give
\[
y_i/\eta=
\begin{cases}-Y_J&i\in I,\\X_I&i\in J,\end{cases}
\qquad
z_i/\eta=S\,1_{i=p}-x_p.
\tag{Cof.17}
\]
Writing \(Z=x_p\) and \(R=X_I-Z\), direct substitution into the
sum (Cof.6) gives
\[
\mathcal S(X)
=\eta^{n+1}(-1)^{s+1}S^2
 ZR\,X_I^{t-1}Y_J^{s-1}.
\tag{Cof.18}
\]
For example, divide temporarily by \(\prod y_i\): the two group
sums are
\[
-\frac{ZS^2+(X_I-2S)Z^2}{Y_J}
+\frac{Y_JZ^2}{X_I}
=-\frac{S^2Z(X_I-Z)}{X_IY_J}.
\]
Multiplication by the actual product
\(\eta^n(-1)^sY_J^sX_I^t\), together with the additional
cofactor factors in the ratio, proves (Cof.18) as a polynomial
identity.

Since \(H\) is odd in (Cof.7), the total power of \(\eta\) is
\(H-1\), which is even. Since \(H\) is even in (Cof.10), its
total power is \(H\), also even. Therefore the specialized
highest polynomials are exactly
\[
\boxed{
F_{n,H}=(-1)^{s+1}S^{H-n}ZR
              X_I^{t-1}Y_J^{s-1},\qquad
G_{n,H}=S^{H-2n}X_I^{2t}Y_J^{2s}.}
\tag{Cof.19}
\]
The first identity includes \(H=n+1\), using the polynomial
division already proved. These evaluations prove that both
highest vectors are nonzero whenever their displayed parameters
apply.

## 5. Proof of the canonical image assertions

Set \(n=a=r+1\), \(H=r^2+1\), \(b=H-2\), and \(W=V^*\).
The exact R-022 annihilator construction gives
\[
\delta:\mathcal K_{a,b}(W)\hookrightarrow
\ker T_{r,r,b}(W)\otimes\operatorname{Sym}^bW.
\tag{Cof.20}
\]
Indeed its only lower-map input is \(h_{b-r,r}\) surjective.
Here
\[
b-r=r^2-r-1\ge(r-1)^2
\]
for every \(r\ge2\), with equality at \(r=2\). This is Sra's
Theorem 1.3 in precisely its proved range; the freeing and
polarization maps and scalars are K.16–K.22, also P.9–P.16.

Suppose first that \(r\) is even. Use \(F_{a,H}\), choose
\[
s=(r+2)/2,\qquad t=r/2,\qquad K=\{a\}\subset I,
\]
and choose the reference slot in \(I\setminus\{a\}\).
Keep the last slot's first coordinate equal to one. Give each of
the first \(r\) slots first coordinate zero, and polarize these
slots in the common direction \(e_1\). Their resulting first
coordinates are \(u_1,\ldots,u_r\).

The required value of \((T_{r,r,b}\otimes\mathrm{id})\delta F\)
is the coefficient of \(u_1^r\cdots u_r^r\).
The first-row homogeneity \(H=r^2+1\) says that it is the
coefficient of \(x_1^r\cdots x_r^r x_a\) in (Cof.19). The factor
\(Z=x_a\) already supplies that last degree. Set \(Z=0\) in
the remaining factors. Since \(s-1=t=r/2\), this coefficient is
\[
\boxed{
(-1)^{s+1}
\binom{r^2-r}{\,r(r-1)/2\,}
\frac{\bigl((r^2/2)!\bigr)^2}{(r!)^r}\ne0.}
\tag{Cof.21}
\]
The binomial splits the two group sums; their multinomial
coefficients supply the two displayed factorials. Every lower
factorial argument is nonnegative.

For odd \(r\ge3\), use \(G_{a,H}\), and let \(s=t=(r+1)/2\),
with the last slot in \(I\). The same coefficient extraction
applied to the second expression in (Cof.19) gives
\[
\boxed{
\binom{r^2-2r-1}{\,r(r-3)/2\,}
\frac{\bigl(r(r-1)/2+1\bigr)!\,
      \bigl(r(r+1)/2\bigr)!}{(r!)^r}\ne0.}
\tag{Cof.22}
\]
The remaining exponent in the binomial is
\((r+1)(r-2)/2\ge0\), and its upper argument is at least two.
The group containing the last slot has total degree
\(r(r-1)/2+1\); its last coordinate has exponent one, giving the
first numerator factorial and denominator \((r!)^{s-1}\).
The other group gives the second numerator factorial and
denominator \((r!)^t\).

Equations (Cof.21) and (Cof.22) show that the unique source
highest line of the respective type in the annihilator ambient
space is not killed by the map in (Cof.20). The multiplicity-one
proof in §3 and equivariance imply that no copy of that type is
in \(\mathcal K_{a,b}\). The exact transpose pairing of (P.6)
proves (Cof.4).

## 6. Two infinite common-polarization families

The same polynomials prove additional parameter families directly
for \(T_{r,L,rL-1}\).

For every \(r\ge3\), \(L\ge1\) with \(rL\) even, set
\[
H=rL+1,\qquad
\lambda=(H,(H-1)^{r-3},H-3,H-r).
\tag{Cof.23}
\]
This source type has multiplicity one and \(T_{r,L,rL-1}\)
is injective on it. Put \(s=\lceil r/2\rceil\), \(t=\lfloor r/2\rfloor\),
choose \(K=\{1\}\subset I\), and take first-row base \(x_1=1\),
all other first-row bases zero. Formula (Cof.19) shows that
the common-polarization coefficient is
\[
\boxed{
(-1)^{s+1}(L+1)
\frac{((s-1)L)!\,(tL)!}{(L!)^{r-1}}
\binom{r(L-1)+1}{\,sL-t\,}
\binom{sL-1}{L}\ne0.}
\tag{Cof.24}
\]
To derive this exact expression, first use first-row homogeneity:
the coefficient at exponent \(L\) in every slot after translation
of the first coordinate by one is \(L+1\) times the coefficient
at exponents \((L+1,L,\ldots,L)\) before translation. Expand
\(X_I^{t-1}=(Z+R)^{t-1}\) in (Cof.19). The resulting finite
binomial sum is
\[
\sum_j\binom{t-1}{j}
\frac{1}{(L-j)!\,((s-1)L-t+j)!}
=\frac{\binom{sL-1}{L}}{(sL-t)!},
\tag{Cof.25}
\]
where terms with negative factorial arguments are zero.
This is the elementary coefficient identity for
\((1+z)^{t-1}(1+z)^{sL-t}\). The remaining group multinomials
give (Cof.24). Its arguments are all valid: at \(L=1\), parity
forces even \(r\ge4\), so \(s=t\ge2\); for odd \(r\), \(L\)
is even and at least two. In every case \(sL-t\ge0\),
\(tL-s+1\ge0\), and \(sL-1\ge L\).

For every odd \(r\ge3\) and odd \(L\ge3\), put
\[
H=rL+1,\qquad \lambda=(H^{r-1},H-2r).
\tag{Cof.26}
\]
This source type again has multiplicity one and is mapped
injectively. Use \(G_{r,H}\), \(s=(r-1)/2\), \(t=(r+1)/2\),
and put the first-row base one in a slot of \(I\). The exact value is
\[
\boxed{
\binom{rL+1-2r}{\,sL+1-2t\,}
\frac{(sL+1)!\,(tL)!}{(L!)^r}\ne0.}
\tag{Cof.27}
\]
The other binomial argument is \(tL-2s\). They are nonnegative
for every displayed \(r,L\), including \(r=L=3\).
This follows directly from the second product in (Cof.19).

For these families the polynomial-generator construction uses
exactly \(r\) coordinate rows. Inclusion into larger vector
spaces commutes with coefficient extraction and the Schur
realizations. A map nonzero on a multiplicity-one irreducible
component is injective on it in every dimension where it exists.
This proves all ambient-rank statements in §§1 and 6.
