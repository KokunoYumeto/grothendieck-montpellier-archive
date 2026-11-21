# Explicit canonical image families below the square bound

Statement **R-026**. Written on 21 November 2026 UTC by GPT-6 Astra Pro,
agent /root/rectangular_cases; effort setting not exposed. The proof
uses the actual canonical map, its transpose annihilator, and explicit
highest polynomials. No historical novelty claim is made.

## 1. The two unconditional parameter families

For integers \(r\ge3\), set \(a=r+1\). The canonical map is the
normalized grid transpose followed by symmetric projection:
\[
h_{b,a}:\operatorname{Sym}^b(\operatorname{Sym}^a V)
\longrightarrow\operatorname{Sym}^a(\operatorname{Sym}^b V).
\tag{BS.1}
\]
In every dimension at least the number of positive parts in the
displayed partition, the following assertions hold.

**Even \(r\ge4\).** For every integer \(2\le k\le r-1\), put
\[
b=r^2-k,\qquad
\lambda=((r^2)^r,\ r^2-k(r+1)).
\tag{BS.2}
\]
Then
\[
\boxed{[S_\lambda V:\operatorname{im}h_{b,a}]
=[S_\lambda V:\operatorname{Sym}^a\operatorname{Sym}^b V]=1.}
\tag{BS.3}
\]

**Odd \(r\ge3\).** For every integer \(2\le k\le r-1\), put
\[
b=r^2-k,\qquad
\lambda=(r^2,(r^2-1)^{r-2},\ r^2-3,
                         \ r^2-(k-1)(r+1)).
\tag{BS.4}
\]
The same equality (BS.3) holds.

At \(k=r-1\), the last part in (BS.2) is one; at its other
parameters it is at least \(r+2\). The last part in (BS.4) is
always at least \(r+2\). These are no larger than the preceding part, so the
formulas are partitions. Their sizes are respectively
\((r+1)(r^2-k)=ab\). Their first row is exactly \(r^2\).

For example:

| \(a\) | \(b\) | \(\lambda\) |
|---:|---:|---|
| 4 | 7 | \((9,8,6,5)\) |
| 5 | 14 | \((16,16,16,16,6)\) |
| 5 | 13 | \((16,16,16,16,1)\) |
| 6 | 23 | \((25,24,24,24,22,19)\) |
| 6 | 22 | \((25,24,24,24,22,13)\) |
| 6 | 21 | \((25,24,24,24,22,7)\) |
| 7 | 34 | \((36,36,36,36,36,36,22)\) |
| 7 | 33 | \((36,36,36,36,36,36,15)\) |
| 7 | 32 | \((36,36,36,36,36,36,8)\) |
| 7 | 31 | \((36,36,36,36,36,36,1)\) |
| 8 | 43 | \((49,48,48,48,48,48,46,9)\) |

Both parity families reach every degree from \(r^2-r+1\) to
\(r^2-2\). The partitions and actual image
multiplicities at all these parameters are the formulas above.

## 2. General cofactor highest polynomials

Use an \(n\)-by-\(n\) matrix of independent variables \(X\), with
\(n\ge3\). Set
\[
D=\det X,\qquad x_j=X_{1j},\qquad
y_j=C_{nj},\qquad z_j=C_{n-1,j},
\quad
\mathcal S=\sum_j x_jz_j^2\prod_{i\ne j}y_i,
\tag{BS.5}
\]
where \(C_{ij}\) is the signed cofactor. All these are literal
polynomials with integral coefficients.

For every **even \(H\ge nk\)** and every \(k\ge1\), define
\[
G_{n,H,k}=D^{H-nk}\prod_{j=1}^n y_j^k.
\tag{BS.6}
\]
It has separate slot degree \(H-k\), row weight
\[
\lambda^G=(H^{n-1},H-nk),
\tag{BS.7}
\]
and is symmetric in the slots. Indeed a column permutation acts on
\(D\) by its sign and on the cofactor row by its sign times the
same entry permutation; the resulting character is
\(\operatorname{sgn}^{H-nk+nk}=1\).

For every **odd \(H\ge n(k-1)+1\)** and every \(k\ge2\), define
\[
F_{n,H,k}
=D^{H-n(k-1)-2}\mathcal S\prod_{j=1}^n y_j^{k-2}.
\tag{BS.8}
\]
The exponent of \(D\) is at least minus one. The quotient at that
endpoint is an actual polynomial: \(D\mid\mathcal S\), as proved
in Cof.6–Cof.9. Explicitly, on the generic rank-\((n-1)\) locus,
\(z_j=c y_j\), so \(\mathcal S=c^2\prod_i y_i\sum_jx_jy_j=0\)
by the cofactor identity. Irreducibility of the determinant then
gives divisibility in the polynomial ring.

The separate slot degree of (BS.8) is \(H-k\), and its row weight is
\[
\lambda^F=(H,(H-1)^{n-3},H-3,H-n(k-1)).
\tag{BS.9}
\]
Its slot-permutation character is
\[
\operatorname{sgn}^{H-n(k-1)-2+n+1+n(k-2)}
=\operatorname{sgn}^{H-1}=1.
\tag{BS.10}
\]
These are highest polynomials under the same actual transvections
as R-025: for \(i<j\), the substitution
\(X\mapsto(I+tE_{j,i})X\) fixes \(D\), \(x\), and \(y\).
Only \(z\mapsto z-t y\) can affect \(\mathcal S\), and its
change is
\[
-2t\Bigl(\prod y_i\Bigr)\sum_jx_jz_j
+t^2\Bigl(\prod y_i\Bigr)\sum_jx_jy_j=0.
\tag{BS.11}
\]
Thus the displayed polynomials are actual highest vectors once
their nonzero evaluations below are supplied.

## 3. The exact complement morphism and multiplicity one

For \(\lambda\) in the \(n\)-by-\(H\) rectangle, let
\(\nu=(H-\lambda_n,\ldots,H-\lambda_1)\). The exterior-column
pairing of Cof.12 is a nonzero perfect equivariant pairing
\[
S_\lambda\mathbf Q^n\otimes S_\nu\mathbf Q^n
\longrightarrow(\det\mathbf Q^n)^H.
\tag{BS.12}
\]
It pairs the content \(((H-k)^n)\) perfectly with content
\((k^n)\), because their diagonal weights add to \((H^n)\).
On the right permutation matrices act by \(\operatorname{sgn}^H\).
Taking the invariant or alternating projector on the second content
space, and applying the literal Cauchy decomposition of matrix
polynomials, gives
\[
[S_\lambda:\operatorname{Sym}^n\operatorname{Sym}^{H-k}]
=
\begin{cases}
[S_\nu:\operatorname{Sym}^n\operatorname{Sym}^{k}],&H\text{ even},\\
[S_\nu:\Lambda^n\operatorname{Sym}^{k}],&H\text{ odd}.
\end{cases}
\tag{BS.13}
\]
Precisely, the content-\((k^n)\) matrix-polynomial space is
\((\operatorname{Sym}^k\mathbf Q^n)^{\otimes n}\). The projectors
are \(n!^{-1}\sum_\sigma\sigma\) and
\(n!^{-1}\sum_\sigma\operatorname{sgn}(\sigma)\sigma\);
their normalized symmetric and alternating inclusions are the maps
used in (BS.13).

For (BS.7), the complement is the row \((nk)\). Its only weight
vector of that weight is \((e_1^k)^n\), so the required symmetric
plethysm multiplicity is one.

For (BS.9), the complement is
\[
\nu=(n(k-1),3,1^{n-3},0).
\tag{BS.14}
\]
Its entire weight space in \(\Lambda^n\operatorname{Sym}^k\)
is one-dimensional. Here is a direct count. No chosen monomial
uses the last variable. The total degree away from the first
variable is \(n\). Among distinct degree-\(k\) monomials in the
first \(n-1\) variables, there is one with that degree zero, and
there are \(n-2\) with that degree one. For \(n\) distinct
monomials, the minimum sum of those degrees is consequently
\(0+(n-2)+2=n\). Equality forces all of those first \(n-1\)
monomials and a single monomial of degree two away from the first
variable. The remaining specified weights force it to be
\(e_1^{k-2}e_2^2\). Thus the unique wedge is
\[
e_1^k\wedge e_1^{k-1}e_2\wedge\cdots\wedge
e_1^{k-1}e_{n-1}\wedge e_1^{k-2}e_2^2.
\tag{BS.15}
\]
Every raising replacement of a variable produces a repeated wedge
factor or zero, so this is a highest vector. Hence (BS.14) occurs
once and (BS.13) proves multiplicity one for (BS.9).

## 4. Exact specialization and coefficients

Use exactly the integral matrix construction in Cof.15–Cof.17.
Partition the \(n\) slots into nonempty groups \(I,J\) of sizes
\(s,t\); choose a reference \(q\in I\). Let \(A\) be the
specified unimodular matrix whose last row is the indicator of
\(J\) in the coordinates excluding \(q\). For \(F\), choose
\(p\in I\setminus\{q\}\), put \(e_p\) in the penultimate row,
and use the remaining coordinate rows before these last two rows.
With \(B=A^{-T}B_0\), where the rows of \(B_0\) are
\(e_i-e_q\), form the matrix whose first row is \(x\) and whose
lower rows are \(B\). Write
\[
X_I=\sum_{i\in I}x_i,\quad Y_J=\sum_{j\in J}x_j,\quad
S=X_I+Y_J,\quad Z=x_p,\quad R=X_I-Z.
\]
The exact cofactor identities are
\[
\begin{gathered}
D=\eta S,\quad y_i/\eta=-Y_J\ (i\in I),\quad y_j/\eta=X_I\ (j\in J),\\
\mathcal S=\eta^{n+1}(-1)^{s+1}S^2ZR X_I^{t-1}Y_J^{s-1},\quad\eta\in\{1,-1\}.
\end{gathered}
\tag{BS.16}
\]
Substitution in (BS.6) and (BS.8) gives, with all signs retained,
\[
\boxed{G_{n,H,k}=(-1)^{sk}S^{H-nk}X_I^{kt}Y_J^{ks},}
\tag{BS.17}
\]
\[
\boxed{F_{n,H,k}=(-1)^{s(k-1)+1}
S^{H-n(k-1)}ZR X_I^{t(k-1)-1}Y_J^{s(k-1)-1}.}
\tag{BS.18}
\]
The powers of \(\eta\) are \(H\) and \(H-1\), respectively,
and are even in their stated ranges. These formulas are polynomial
identities, including the quotient endpoint in (BS.8).

For the canonical families, take \(n=r+1\), \(H=r^2\),
and put the last slot in \(I\). Give all slots first-row base
zero. In the first \(r\) slots, polarize in the common direction
\(e_1\); keep the last slot fixed. The required value is the
coefficient of
\[
x_1^r\cdots x_r^r x_{r+1}^{\,0}.
\tag{BS.19}
\]
Thus set \(x_{r+1}=0\) in (BS.17) or (BS.18). This base choice
is allowed: the lower rows are the explicit constant matrix \(B\),
and the polarization coefficient is a polynomial evaluation at it.

For **even \(r\ge4\)** and \(2\le k\le r-2\), use
\[
s=r/2+1,\quad t=r/2,\quad h=r^2-k(r+1),\quad
u=r(r-k)/2.
\]
There are \(r/2\) unfixed variables in each group. Formula (BS.17)
therefore gives exactly
\[
\boxed{(-1)^{sk}\binom hu
\frac{((r^2/2)!)^2}{(r!)^r}\ne0.}
\tag{BS.20}
\]
Indeed the group degrees are both \(r^2/2\), so the required
power of \(X_I\) from \(S^h\) is \(u\), and the remaining
degree is \(h-u=r^2/2-k(r/2+1)\). This is at least two for all
the displayed parameters. Both multinomial coefficients are the
displayed factorial ratios. This proves the nonzero value including
the endpoint \(k=r-2\).

For **odd \(r\ge5\)** and \(2\le k\le r-1\), use
\[
s=t=(r+1)/2,\quad h=r^2-(k-1)(r+1),\quad
d_I=r(s-1),\quad d_J=rt,\quad
u=s(r-k-1).
\tag{BS.21}
\]
Choose \(p\) in the first \(r\) slots of \(I\), and take the
last slot as reference \(q\). There are \(s-1\ge2\) first
\(r\) slots in \(I\), so after setting the last coordinate zero,
\(R\) still contains at least one variable. Formula (BS.18) gives
the exact coefficient
\[
\boxed{(-1)^{s(k-1)+1}\binom hu
\binom{d_I-2}{r-1}
\frac{(d_I-r)!\,d_J!}{(r!)^{r-1}}\ne0.}
\tag{BS.22}
\]
To obtain it, the \(S^h\) split must contribute
\(X_I^uY_J^{h-u}\), since
\(u=d_I-t(k-1)-1\). The resulting first-group factor is
\(ZR(Z+R)^{d_I-2}\). Its \(Z^r\) coefficient is
\(\binom{d_I-2}{r-1}R^{d_I-r}\). The remaining first-group
variables have exponent \(r\) each, as do the \(t\) variables
of the second group, giving the two multinomial coefficients.
Every argument is valid: \(u\ge0\),
\(h-u=s(r-k+1)+1>0\), and \(d_I-r=r(s-2)\ge0\).
The binomial \(\binom{d_I-2}{r-1}\) is positive because
\(s-1\ge2\) and \(r\ge5\).

The odd endpoint \(r=3,k=2\) is also explicit. Choose
\(s=3,t=1\), put the last slot in \(I\), and choose \(p\)
among its first two slots. Then \(h=5,d_I=6,d_J=3,u=4\).
The same coefficient extraction is
\[
\binom54\binom42\frac{3!\,3!}{(3!)^2}=30\ne0.
\tag{BS.23}
\]

## 5. The even-r endpoint by an explicit apolar evaluation

Let \(r\ge4\) be even and take \(k=r-1\), \(n=r+1\),
\(H=r^2\). The polynomial (BS.6) at this endpoint is
\[
G_{n,H,r-1}=D\prod_{j=1}^{r+1}y_j^{r-1},\qquad
\lambda=((r^2)^r,1).
\tag{BS.24}
\]
We give another concrete matrix evaluation of its coefficient (BS.19).
Let \(\zeta_1,\ldots,\zeta_r\) be the distinct roots of
\(z^r+1\), put \(a_i=1+\zeta_i\), and set \(a_{r+1}=0\).
The first \(r\) values are distinct and nonzero: \(-1\) is not
a root of \(z^r+1\) for even \(r\). They therefore give the
explicit nonzero determinant matrix
\[
A=\begin{pmatrix}
a_1^2&\cdots&a_r^2\\
\vdots&&\vdots\\
a_1^r&\cdots&a_r^r\\
a_1&\cdots&a_r
\end{pmatrix},\qquad
\det A=(-1)^{r-1}\Bigl(\prod_i a_i\Bigr)
                       \prod_{i<j}(a_j-a_i)\ne0.
\tag{BS.25}
\]
Take \(B_0=(I_r\mid-\mathbf1)\), \(B=A^{-T}B_0\), and
use \(B\) for the lower rows of \(X\). This specifies the actual
matrix over the splitting field. No unimodular normalization is
made in this evaluation. Write
\[
S=\sum_{i=1}^r x_i,\qquad Z=\sum_{i=1}^r a_i x_i,
\qquad \eta=(\det A)^{-1}.
\]
After setting \(x_{r+1}=0\), the determinant and cofactor identities
give exactly
\[
D=\eta S,\qquad y_i=\eta(a_iS-Z)\ (1\le i\le r),
\qquad y_{r+1}=-\eta Z.
\tag{BS.26}
\]
For the determinant, the matrix \(B_0\) gives
\((-1)^r\sum x_i\); its lower row transformation has determinant
\((\det A)^{-1}\). Since \(r\) is even, this is the stated
\(\eta\). The cofactor formulas follow from \(C=DX^{-T}\),
exactly as in Cof.16, with the last row of \(A\) equal to \(a\).

Let
\[
Q(s,z)=\prod_{i=1}^r(z-a_i s)=(z-s)^r+s^r,
\qquad Q_0(s,z)=z^r+s^r.
\]
Substituting (BS.26) into (BS.24) gives the exact binary expression
\[
G_{n,H,r-1}=-\eta^{r^2}S Z^{r-1}Q(S,Z)^{r-1}.
\tag{BS.27}
\]
For degree-\(N\) binary forms define the bilinear pairing
\[
\langle P,R\rangle_N
=\left.P(-\partial_z,\partial_s)R(s,z)\right|_{s=z=0}.
\tag{BS.28}
\]
The chain rule for the two displayed linear forms \(S,Z\) identifies
the required coefficient, with its full normalization, as
\[
[x_1^r\cdots x_r^r]G_{n,H,r-1}
=-\frac{\eta^{r^2}}{(r!)^r}
\left\langle Q^r,\ s z^{r-1}Q^{r-1}\right\rangle_{r^2}.
\tag{BS.29}
\]
Indeed differentiation in \(x_i\) acts as
\(\partial_s+a_i\partial_z\); the product of its \(r\)-th
powers is exactly \(Q(-\partial_z,\partial_s)^r\).
The factor \((r!)^{-r}\) is the ordinary monomial coefficient
normalization.

The substitution \(\tau R(s,z)=R(s,z-s)\) preserves the pairing
(BS.28). This follows directly from the chain rule:
\((\partial_s+\partial_z)\tau R=\tau(\partial_sR)\) and
\(\partial_z\tau R=\tau(\partial_zR)\). Substitution in
\((\tau P)(-\partial_z,\partial_s)
=P(-\partial_z,\partial_s+\partial_z)\), followed by evaluation
at zero, proves \(\langle\tau P,\tau R\rangle=\langle P,R\rangle\).
Applying this actual change of variables to (BS.29) gives
\[
\left\langle Q^r,s z^{r-1}Q^{r-1}\right\rangle_{r^2}
=\left\langle Q_0^r,s(z+s)^{r-1}Q_0^{r-1}\right\rangle_{r^2}.
\tag{BS.30}
\]
Every exponent of \(s\) or \(z\) in a monomial of \(Q_0^r\)
is a multiple of \(r\). In the extra factor
\(s(z+s)^{r-1}\), the \(z\)-exponent lies between zero and
\(r-1\). Consequently only its term \(s^r\) can pair
nontrivially with \(Q_0^r\) after multiplication by \(Q_0^{r-1}\).
Expanding these two binomial powers now gives
\[
\boxed{[x_1^r\cdots x_r^r]G_{n,H,r-1}
=-\frac{\eta^{r^2}}{(r!)^r}
\sum_{i=0}^{r-1}\binom ri\binom{r-1}{i}
(ri)!\,[r(r-i)]!\ne0.}
\tag{BS.31}
\]
The differential sign in each term is \((-1)^{ri}=1\), since
\(r\) is even. Every integer summand is positive and
\(\eta\ne0\). This proves the endpoint for every even \(r\)
in the statement, by a fully specified algebraic evaluation of the
same integral highest polynomial. The field inclusion from \(\mathbf Q\)
into this splitting field is injective. A zero polynomial image over
\(\mathbf Q\) remains zero after that scalar extension, so the
nonzero value detects the original map as well.

## 6. Transfer to the actual canonical image

Let \(W=V^*\), and let \(\mathcal K_{a,b}(W)\) be the
annihilator of the image of (BS.1) under the normalized symmetric
tensor pairing. The actual last-slot inclusion and coefficient
polarization from K.16–K.22 give
\[
\delta\mathcal K_{a,b}(W)
\subset\ker T_{r,r,b}(W)\otimes\operatorname{Sym}^bW
\tag{BS.32}
\]
throughout both displayed families. To verify its lower-map input,
\[
b-r-(r-1)^2=r-k-1\ge0.
\tag{BS.33}
\]
Thus Sra's Theorem 1.3 proves that the actual lower canonical map
\(h_{b-r,r}\) is surjective at every parameter used here.

The inclusion \(\delta\) is the normalized last-slot splitting
of a symmetric \((r+1)\)-tensor; polynomial evaluation on symmetric
slot functions identifies it with retaining the same polynomial
and distinguishing the last variable. The map \(T_{r,r,b}\)
extracts the coefficient of \(u_1^r\cdots u_r^r\) after the
substitution \(v_i\mapsto v_i+u_i x\) in its first \(r\) slots.
These are the literal maps of (BS.32). The derivation, including
the nonzero factorial and binomial scalars in the annihilator
inclusion, is K.16–K.22 and P.9–P.16; (BS.33) checks precisely
its application range here.

Equations (BS.20), (BS.22), (BS.23), and (BS.31) are nonzero values of
\((T_{r,r,b}\otimes\mathrm{id})\delta\) on the respective
highest polynomials. By (BS.13)–(BS.15), each corresponding
type occurs exactly once in the entire annihilator ambient
module \(\operatorname{Sym}^{r+1}\operatorname{Sym}^bW\).
Equivariance and (BS.32) exclude that single copy from
\(\mathcal K_{a,b}\). The perfect transpose pairing therefore
proves exactly (BS.3).

All constructions use \(a\) coordinate rows. Inclusion into any
larger vector space commutes with symmetric projection, grid
transpose, column alternation, and the displayed coefficient maps.
The polynomial-functor multiplicity of each label with at most
\(a\) rows is unchanged: the highest vectors involving those
coordinate rows and their raising equations give the same Schur
multiplicity space. Hence the same nonzero canonical component
persists in every stated ambient dimension.

The lower-map source is Suvrit Sra, *The q-Foulkes problem III: On
Foulkes' conjecture with a graded inner factor*, Theorem 1.3,
[primary PDF](https://suvrit.github.io/papers/qfoulkes3/qfoulkes3-v1.pdf).
The exact range used is \(h_{B,r}\) surjective for
\(B\ge(r-1)^2\). The remaining maps, polynomial identities,
parameter arithmetic, and nonzero coefficients have been proved
explicitly above.
