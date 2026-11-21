# Canonical image families with first row one above the polarization degree

Statement **R-027**, 21 November 2026 UTC. GPT-6 Astra Pro,
/root/rectangular_cases; effort setting not exposed.

## 1. The unconditional families

Let \(r\ge2\), \(a=r+1\), and \(H=r^2+1\). Use the actual
normalized canonical grid map
\[
h_{b,a}:\operatorname{Sym}^b\operatorname{Sym}^a V
\longrightarrow\operatorname{Sym}^a\operatorname{Sym}^b V.
\tag{NR.1}
\]
For **even \(r\ge2\)** and every integer \(2\le k\le r\), put
\[
b=H-k,\qquad
\lambda=(H,(H-1)^{r-2},H-3,H-(k-1)(r+1)).
\tag{NR.2}
\]
For **odd \(r\ge3\)** and every integer \(2\le k\le r-1\), put
\[
b=H-k,\qquad
\lambda=(H^r,H-k(r+1)).
\tag{NR.3}
\]
For both families, in every dimension at least the number of positive
parts of \(\lambda\),
\[
\boxed{[S_\lambda V:\operatorname{im}h_{b,a}]
=[S_\lambda V:\operatorname{Sym}^a\operatorname{Sym}^b V]=1.}
\tag{NR.4}
\]
All displayed labels are partitions of \(ab\). Their last part is
at least two; their first row is exactly \(r^2+1\). Family (NR.2)
covers every \(b\) from \(r^2-r+1\) through \(r^2-1\), and
(NR.3) covers every \(b\) from \(r^2-r+2\) through \(r^2-1\).
At \(k=2\) these are exactly R-025's two canonical families.
No historical novelty claim is made.

## 2. The highest vectors and the canonical transfer

Retain the literal determinant, cofactor rows, and polynomial
\(\mathcal S\) of BS.5:
\[
D=\det X,\qquad y_j=C_{a,j},\qquad z_j=C_{a-1,j},\qquad
\mathcal S=\sum_jX_{1j}z_j^2\prod_{i\ne j}y_i.
\]
Use the integral highest polynomials
\[
F_{a,H,k}=D^{H-a(k-1)-2}\mathcal S\prod_jy_j^{k-2}
\quad\text{for (NR.2)},
\tag{NR.5}
\]
\[
G_{a,H,k}=D^{H-ak}\prod_jy_j^k
\quad\text{for (NR.3)}.
\tag{NR.6}
\]
The determinant exponents in this report are nonnegative. Their slot
degrees, row weights, highest transvections, and symmetric slot actions
are proved by the explicit maps BS.5–BS.11. Their multiplicity is
exactly one by the perfect exterior-column pairing BS.12 and the literal
symmetric or alternating projectors BS.13. For \(F\), its complementary
highest weight is \((a(k-1),3,1^{a-3},0)\), and the unique wedge is
BS.15. For \(G\), the complement is the single row \((ak)\).
These are precise applications of those already proved maps, with
\(a=r+1\), \(H=r^2+1\), and separate slot degree \(H-k=b\).

Let \(\delta\) distinguish the last slot of the dual target, and
let \(T_{r,r,b}\) extract the common-polarization coefficient
\([u_1^r\cdots u_r^r]\) in the first \(r\) slots. The actual
annihilator inclusion of BS.32 applies throughout (NR.2)–(NR.3), since
\[
b-r-(r-1)^2=r-k\ge0.
\tag{NR.7}
\]
Its lower canonical map \(h_{b-r,r}\) is therefore surjective by
Sra's Theorem 1.3 in its stated range. To exclude the multiplicity-one
highest line from that annihilator, it suffices to give a nonzero
value of \((T_{r,r,b}\otimes\mathrm{id})\delta\) on the actual
polynomial (NR.5) or (NR.6).

Give the first \(r\) slots first-row base zero and the last slot
first-row base one, and use common direction \(e_1\). Since the
first-row degree is \(H=r^2+1\), the resulting value is exactly
\[
[x_1^r\cdots x_r^r x_{r+1}]F_{a,H,k}
\quad\text{or}\quad
[x_1^r\cdots x_r^r x_{r+1}]G_{a,H,k}.
\tag{NR.8}
\]
The last-slot inclusion is normalized so that its evaluation on a
symmetric slot polynomial retains the same polynomial. Thus no extra
slot factorial occurs in (NR.8).

## 3. The interior parameters by exact group-sum coefficients

Use the same explicit unimodular matrices BS.16–BS.18; let the last
slot belong to \(I\), with group sizes \(s,t\).

For even \(r\ge4\) and \(2\le k\le r-1\), take
\[
s=r/2+1,\quad t=r/2,\quad
h=H-(r+1)(k-1),\quad u=r(r-k+1)/2,
\]
and choose the distinguished slot \(p=r+1\). Its coordinate \(Z\)
already supplies the power one of the last variable in BS.18, so set
that variable zero in every other factor. The exact coefficient is
\[
\boxed{(-1)^{s(k-1)+1}\binom hu
\frac{((r^2/2)!)^2}{(r!)^r}\ne0.}
\tag{NR.9}
\]
Both groups then have \(r/2\) first slots, each with required degree
\(r\). The fixed powers of their sums are \(t(k-1)\) and
\(s(k-1)-1\); the remaining split of \(S^h\) is \((u,h-u)\).
The second quantity is
\(r^2/2-s(k-1)+1\ge3\), so every factorial and binomial argument
in (NR.9) is valid and its magnitude is positive.

For odd \(r\ge5\) and \(2\le k\le r-2\), take
\[
s=t=(r+1)/2,\quad h=H-(r+1)k,\quad
d_I=r(s-1)+1,\quad d_J=rt,\quad u=d_I-kt.
\]
The last coordinate has exponent one inside the first group, while its
other \(s-1\) variables and all \(t\) second-group variables have
exponent \(r\). Formula BS.17 gives exactly
\[
\boxed{(-1)^{sk}\binom hu
\frac{d_I!\,d_J!}{(r!)^r}\ne0.}
\tag{NR.10}
\]
Here \(u\ge2\), with equality at \(k=r-2\), and
\(h-u=s(r-k)>0\). These inequalities verify every endpoint of this
interior range. The two remaining endpoint constructions follow.

## 4. The even-r endpoint: a positive apolar sum

Let \(r\ge2\) be even and take \(k=r\). Then the highest
polynomial and label are
\[
F_{r+1,H,r}=\mathcal S\prod_jy_j^{r-2},\qquad
\lambda=(r^2+1,(r^2)^{r-2},r^2-2,2).
\tag{NR.11}
\]
Choose the distinct roots \(\zeta_i\) of \(z^r+1\) and put
\(a_i=1+\zeta_i\) for \(1\le i\le r\), \(a_{r+1}=0\).
Also put \(b_i=0\) for \(i\le r\), and \(b_{r+1}=1\).
Take reference slot \(q=1\). In the coordinates excluding slot one,
define the \(r\)-by-\(r\) matrix \(A\) by these rows in order:
\[
(a_i^2-a_1^2)_i,\ldots,(a_i^{r-1}-a_1^{r-1})_i,
\qquad (b_i)_i,\qquad(a_i-a_1)_i.
\tag{NR.12}
\]
The first list is empty at \(r=2\). Expanding along the \(b\)-row
leaves a nonzero Vandermonde determinant on \(a_1,\ldots,a_r\):
divide each remaining column by \(a_i-a_1\), and use the monic
polynomials \((T^j-a_1^j)/(T-a_1)\), of distinct degrees
\(0,\ldots,r-2\). This proves \(\det A\ne0\) with the actual
matrix (NR.12).

Let \(B_0\) have rows \(e_i-e_1\), \(i\ne1\), in increasing
order, and put \(B=A^{-T}B_0\) in the lower rows of \(X\).
Write \(\eta=(\det A)^{-1}\),
\(S=\sum_{i\le r}x_i\), \(Z=\sum_{i\le r}a_i x_i\),
and \(w=x_{r+1}\). Direct cofactor evaluation gives
\[
\begin{aligned}
D&=\eta(S+w),& y_i&=\eta((S+w)a_i-Z)\quad(i\le r),\\
y_{r+1}&=-\eta Z,&z_i&=-\eta w\quad(i\le r),&
z_{r+1}&=\eta S.
\end{aligned}
\tag{NR.13}
\]
For this reference slot, \(\det(x;B_0)=\sum x_i\), fixing the
displayed scalar. Shifting all entries of \(a\) by \(-a_1\)
does not change \((\sum x_i)a_j-\sum_i a_i x_i\); this proves
the last-row formula from the row in (NR.12), including the omitted
reference coordinate. The same calculation applies to \(b\).

In the numerator \(\mathcal S\), each summand indexed by a first
slot has the factor \(z_i^2=\eta^2w^2\). Therefore only the
last summand contributes to \([w]\) of (NR.11). With
\(Q(s,z)=(z-s)^r+s^r\), it gives exactly
\[
[w]F_{r+1,H,r}=\eta^{r^2} S^2 Z^{r-2}Q(S,Z)^{r-1}.
\tag{NR.14}
\]
All cofactor signs cancel here: their total exponent of minus one is
\(r(r-1)+r-2=r^2-2\), even for this range of \(r\).

Use the exact pairing
\(\langle P,R\rangle_N=P(-\partial_z,\partial_s)R|_0\)
of BS.28. The chain rule and normalized coefficient extraction give
\[
[x_1^r\cdots x_r^r w]F_{r+1,H,r}
=\frac{\eta^{r^2}}{(r!)^r}
\left\langle Q^r,s^2z^{r-2}Q^{r-1}\right\rangle_{r^2}.
\tag{NR.15}
\]
Under the actual substitution \(z\mapsto z-s\), the chain-rule
invariance proved in BS.28–BS.30 transforms this pairing into
\[
\left\langle Q_0^r,s^2(z+s)^{r-2}Q_0^{r-1}\right\rangle_{r^2},
\qquad Q_0=z^r+s^r.
\]
Only the term with \(z\)-exponent zero in the extra factor can
pair with a monomial of \(Q_0^r\): all its exponents are divisible
by \(r\), whereas that extra exponent is between zero and \(r-2\).
The surviving factor is \(s^r\). Hence the exact value is
\[
\boxed{\frac{\eta^{r^2}}{(r!)^r}
\sum_{i=0}^{r-1}\binom ri\binom{r-1}{i}
(ri)!\,[r(r-i)]!\ne0.}
\tag{NR.16}
\]
Every summand is a positive integer, and \(\eta\ne0\). This
also proves the \(r=2\) case of the statement.

## 5. The odd-r endpoint: an exact factorial inequality

Let \(r\ge3\) be odd and take \(k=r-1\). Now
\[
G_{r+1,H,r-1}=D^2\prod_jy_j^{r-1},\qquad
\lambda=((r^2+1)^r,2).
\tag{NR.17}
\]
Choose \(a_i=2+\zeta_i\), where the \(\zeta_i\) are the
distinct roots of \(z^r+1\), and put \(a_{r+1}=0\).
The \(a_i\) are distinct and nonzero. With reference slot \(r+1\),
take the matrix whose rows are \((a_i^2)_i,\ldots,(a_i^r)_i,(a_i)_i\),
and again use \(B=A^{-T}(I_r\mid-\mathbf1)\). This is the
explicit nonzero Vandermonde matrix of BS.25. Since \(r\) is odd,
the exact determinant scalar is
\(\eta=-(\det A)^{-1}\).

Set \(S=\sum_{i\le r}x_i\), \(Z=\sum_{i\le r}a_i x_i\),
and \(w=x_{r+1}\). The same literal cofactors now give
\[
G_{r+1,H,r-1}=\eta^H(S+w)^2 Z^{r-1}Q(S+w,Z)^{r-1},
\qquad Q(s,z)=(z-2s)^r+s^r.
\tag{NR.18}
\]
The sign from the product of the \(r+1\) cofactor factors is one,
because \((r+1)(r-1)\) is even. Differentiation in \(w\)
acts as \(\partial_s\). Consequently the exact coefficient is
\[
\frac{\eta^H}{(r!)^r}
\left\langle zQ^r,s^2z^{r-1}Q^{r-1}\right\rangle_H.
\tag{NR.19}
\]
The extra factor \(z\) in the first argument gives precisely this
\(\partial_s\) in the apolar differential operator.

Translate by \(z\mapsto z-2s\). The pairing in (NR.19) becomes
\[
\left\langle (z+2s)Q_0^r,
s^2(z+2s)^{r-1}Q_0^{r-1}\right\rangle_H,
\qquad Q_0=z^r+s^r.
\tag{NR.20}
\]
There are only two possible exponent matches modulo \(r\).
Write the extra \(s\)-exponent in the first argument as
\(\ell\in\{0,1\}\). In the second argument, the extra
\(z\)-exponent must equal \(\ell\), since it lies between
zero and \(r-1\). Expanding these two contributions gives
\[
2^{r-1}\sum_{i=0}^{r-1}(-1)^i\binom ri\binom{r-1}{i}
(ri)!\,[r(r-i)]!\,(r^2-r+2-r^2 i).
\tag{NR.21}
\]
This is an exact signed intermediate expression, whose positivity
is proved next.

Define
\[
D_i=\binom ri^2(ri)!\,[r(r-i)]!,\qquad
U_r=\sum_{i=0}^r(-1)^i(r-2i)D_i.
\tag{NR.22}
\]
The identity \(\binom{r-1}{i}=(r-i)\binom ri/r\), followed by
pairing the terms indexed by \(i\) and \(r-i\), transforms
(NR.21) exactly into
\[
2^{r-1}\frac{r^2-r+2}{2r}\,U_r.
\tag{NR.23}
\]
In this calculation \(D_{r-i}=D_i\) and
\((-1)^{r-i}=-(-1)^i\); the terms involving \(r^2i(r-i)\)
cancel. These identities prove (NR.23), including its scalar.

Here is a uniform strict lower bound. The terms \(i=0,r\) in
\(U_r\) sum to \(2r(r^2)!\). For every \(1\le i\le r-1\),
\[
\frac{D_i}{(r^2)!}
=\frac{\binom ri^2}{\binom{r^2}{ri}}
\le{\binom ri}^{2-r}\le r^{2-r}.
\tag{NR.24}
\]
The first inequality follows by selecting the term of degree \(i\)
in each of the \(r\) factors in
\((1+z)^{r^2}=((1+z)^r)^r\):
\(\binom{r^2}{ri}\ge\binom ri^r\).
The second follows from \(\binom ri\ge r\), verified by the
successive binomial ratio up to the middle and then symmetry.
Therefore the total absolute contribution of the interior terms is at
most
\[
(r-1)(r-2)r^{2-r}(r^2)!<r(r^2)!<2r(r^2)!.
\tag{NR.25}
\]
For the strict inequality, \(r\ge3\) gives
\(r^{2-r}\le1/r\) and \((r-1)(r-2)<r^2\).
It follows that \(U_r>0\). The exact endpoint coefficient is thus
\[
\boxed{\frac{\eta^H}{(r!)^r}
2^{r-1}\frac{r^2-r+2}{2r}\,U_r\ne0.}
\tag{NR.26}
\]
This establishes every odd endpoint, including \(r=3\).

## 6. Completion and scope

The nonzero values (NR.9), (NR.10), (NR.16), and (NR.26), the
multiplicity-one morphisms in §2, and the actual annihilator inclusion
with parameter check (NR.7) prove (NR.4). The explicit evaluations in
the splitting fields detect the original rational polynomial maps:
scalar extension of a zero rational vector remains zero under the
injective field map. Inclusion of coordinate rows into larger ambient
spaces commutes with every tensor projector and coefficient map, so
the same conclusions hold in every stated dimension.

The source range used in (NR.7) is Sra, *The q-Foulkes problem III:
On Foulkes' conjecture with a graded inner factor*, Theorem 1.3,
[primary PDF](https://suvrit.github.io/papers/qfoulkes3/qfoulkes3-v1.pdf).
The normalized annihilator morphism is proved in K.16–K.22 and
P.9–P.16. All polynomial and apolar comparisons used here are the
actual maps displayed above and in BS.5–BS.18, BS.28–BS.30.
