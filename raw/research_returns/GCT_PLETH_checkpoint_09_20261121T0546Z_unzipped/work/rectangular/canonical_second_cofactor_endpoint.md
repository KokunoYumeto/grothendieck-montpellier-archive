# A second canonical cofactor endpoint in every even outer rank

## R-029. Statement and actual highest polynomial

For every odd integer \(r\ge3\), put
\[
a=r+1,\quad b=r^2-r+2,\quad H=r^2+2,
\qquad
\lambda=(H,(H-1)^{r-2},H-3,3).
\tag{SE.1}
\]
The normalized canonical map
\(h_{b,a}:\operatorname{Sym}^b\operatorname{Sym}^aV
\to\operatorname{Sym}^a\operatorname{Sym}^bV\)
has target and image multiplicity exactly one at \(\lambda\),
in every ambient dimension where this label exists.

Use the \(a\times a\) matrix of slot vectors, its determinant
\(D\), first-row entries \(x_i\), and cofactors
\(y_i=C_{a,i}\), \(z_i=C_{a-1,i}\). Define
\[
\mathcal S=\sum_i x_i z_i^2\prod_{h\ne i}y_h,
\qquad F=D\mathcal S\prod_i y_i^{r-2}.
\tag{SE.2}
\]
This is exactly the polynomial \(F_{a,H,r}\) of BS.8. Its slot
degree is \(H-r=b\), and its row weights are those in (SE.1).
The raising substitutions and literal cofactor identities in
BS.8–BS.9 prove that it is a symmetric highest polynomial.
Here the determinant exponent is one, so no division is involved.

The perfect complementary-column pairing and primitive Young
projectors BS.10–BS.15 identify its target multiplicity with that of
\[
\nu=(a(r-1),3,1^{a-3},0)
\quad\hbox{in}\quad\Lambda^a\operatorname{Sym}^r.
\tag{SE.3}
\]
The alternation is fixed by the odd value of \(H\). The entire
weight space at (SE.3) is the single wedge of
\(e_1^r\), the \(a-2\) monomials \(e_1^{r-1}e_i\)
for \(2\le i\le a-1\), and \(e_1^{r-2}e_2^2\).
Indeed these are precisely the \(a\) distinct monomials with the
smallest possible total degree \(a\) away from the first variable;
the displayed remaining weights force the final choice. Every
raising operator produces a repeated factor or zero. Thus it is
highest and the target multiplicity is one, with the actual pairing
and alternating projector specified above.

The exact retained-slot annihilator inclusion K.16–K.22 applies,
since the lower canonical inner degree is
\[
b-r=(r-1)^2+1\ge(r-1)^2.
\tag{SE.4}
\]
Sra's Theorem 1.3 supplies that lower-map surjectivity. Consequently
the nonzero common-polarization value computed below excludes this
unique highest line from the transpose kernel and proves the
stated actual image multiplicity.

## 1. Cofactor matrix with two distinguished rows

Let \(\zeta_i\) be the distinct roots of \(z^r+1\), and set
\(a_i=2+\zeta_i\) for \(i\le r\), \(a_{r+1}=0\).
Set \(b_i=0\) for \(i\le r\), and \(b_{r+1}=1\).
Take reference column 1. With columns indexed by \(2,\ldots,r+1\),
let \(A\) have rows
\[
(a_i^2-a_1^2)_i,\ldots,(a_i^{r-1}-a_1^{r-1})_i,
\quad(b_i)_i,\quad(a_i-a_1)_i.
\tag{SE.5}
\]
This is invertible: a linear relation among its rows gives a
polynomial of degree at most \(r-1\) vanishing at all \(r\)
distinct \(a_i\), \(i\le r\), so its polynomial coefficients
vanish; the last column then kills the remaining \(b\)-coefficient.
Set \(B=A^{-T}B_0\), where the rows of \(B_0\) are
\(e_i-e_1\), \(2\le i\le r+1\). Use \(B\) as the lower
rows of the slot matrix and write \(\eta=(\det A)^{-1}\).

Put \(S=\sum_{i\le r}x_i\), \(Z=\sum_{i\le r}a_i x_i\),
\(w=x_{r+1}\), and \(s=S+w\). The literal minors give
\[
D=\eta s,\quad y_i=\eta(sa_i-Z),\qquad
z_i=-\eta w\ (i\le r),\quad z_{r+1}=\eta S.
\tag{SE.6}
\]
These formulas also follow from \(B\mathbf1=0\),
\(Ba=e_r\), \(Bb=e_{r-1}\), and their adjugate pairings; the
first-column cofactor fixes exactly the scalar \(\eta\).

Define
\[
Q(s,z)=\prod_{i\le r}(z-a_i s)=(z-2s)^r+s^r,
\qquad Q_i=Q/(z-a_i s).
\]
Substitute (SE.6) in (SE.2). Since \(r\) is odd, the result is
\[
F=-\eta^{r^2+1}sZ^{r-2}
\left(wS^2Q(s,Z)^{r-1}
 +Zw^2Q(s,Z)^{r-2}\sum_{i\le r}x_iQ_i(s,Z)\right).
\tag{SE.7}
\]
For the signs, \(\prod_{i\le r}(sa_i-z)=(-1)^rQ\), while
the last \(y\)-cofactor is \(-\eta Z\). The terms in the sum
\(\mathcal S\) from first \(r\) columns use \(z_i^2=\eta^2w^2\),
and its last term uses \(z_{r+1}^2=\eta^2S^2\). This gives
both terms and the minus sign in (SE.7).

## 2. Both terms of the actual polarization coefficient

The required coefficient is
\([x_1^r\cdots x_r^r w^2]F\). Extract \(w^2\) in (SE.7)
first. The first term differentiates its factor \(sQ^{r-1}\)
once, and the second is evaluated at \(s=S\).
For binary forms use
\(\langle P,R\rangle_N=P(-\partial_z,\partial_s)R|_0\).
Coefficient extraction in the first \(r\) variables is
\((r!)^{-r}\prod_i(\partial_s+a_i\partial_z)^r\).
Its polynomial symbol is \(Q^r\).

Multiplication of the second argument by \(s^2\) transfers to
\(\partial_z^2\) on the first argument, by the Leibniz rule.
Its \(\partial_s\) transfers to multiplication by \(z\).
In the second term of (SE.7), each factor \(x_i\) instead
replaces its corresponding differential power by
\(r(\partial_s+a_i\partial_z)^{r-1}\). Consequently the exact
coefficient is
\[
-\frac{\eta^{r^2+1}}{(r!)^r}
\left(A+rB\right),
\tag{SE.8}
\]
where, with \(N=r^2-1\),
\[
A=\langle z\,\partial_z^2(Q^r),\ s z^{r-2}Q^{r-1}\rangle_N,
\quad
B=\sum_i\langle Q^{r-1}Q_i,\ s z^{r-1}Q^{r-2}Q_i\rangle_N.
\tag{SE.9}
\]
Each pair of arguments has degree \(N\); these identities retain
both contributions to the coefficient.

Translate \(z\mapsto z-2s\) in the actual apolar pairing.
Then \(Q\) becomes \(Q_0=z^r+s^r\), \(z\) becomes \(z+2s\),
and \(\partial_z\) is unchanged. Moreover
\[
Q_i\longmapsto q_i=
\sum_{t=0}^{r-1}\zeta_i^t s^t z^{r-1-t}.
\tag{SE.10}
\]
The root sum is \(\sum_i\zeta_i^h=r\) at \(h=0\),
\(-r\) at \(h=r\), and zero for all other
\(0\le h\le2r-2\). This fixes the whole sum of pairings in
\(B\) without selecting or approximating individual roots.

## 3. Evaluation of the first term

Set
\[
D_i=\binom ri^2(ri)!\,[r(r-i)]!,\qquad
U_r=\sum_{i=0}^r(-1)^i(r-2i)D_i.
\tag{SE.11}
\]
Matching the extra exponents modulo \(r\) in the translated first
pairing allows exactly two terms. The result is
\[
\frac{A}{2^{r-2}}=
\sum_{i=1}^r(-1)^i\binom ri\binom{r-1}{r-i}
(ri)!\,[r(r-i)]!
\left((r-2)(r^2+1)+1-r(r-1)i\right).
\tag{SE.12}
\]
To see the two terms explicitly, the extra \(z\)-degree in the
first argument is zero or one, and the extra \(z\)-degree in
the second is its complement to one. The second derivative gives
\((ri)(ri-1)\). The two remaining factorials are respectively
\((ri-2)!,[r(r-i)+1]!\) and
\((ri-1)!,[r(r-i)]!\). Simplification gives exactly (SE.12).

Use \(\binom{r-1}{r-i}=(i/r)\binom ri\), include the zero
\(i=0\) term, and pair \(i\) with \(r-i\).
Here \(D_{r-i}=D_i\) and \((-1)^{r-i}=-(-1)^i\).
For the quadratic
\(g(i)=(i/r)((r-2)(r^2+1)+1-r(r-1)i)\),
\[
g(i)-g(r-i)=\frac{r^2-r+1}{r}(r-2i).
\]
It follows that
\[
\boxed{A=2^{r-2}\frac{r^2-r+1}{2r}\,U_r.}
\tag{SE.13}
\]

## 4. Exact telescoping of the second term

After the translation, exponent matching forces the extra
\(z\)-degree in \((z+2s)^{r-1}\) to be one. Its coefficient
is \((r-1)2^{r-2}\). The root sum (SE.10) then gives
\[
B=r(r-1)2^{r-2}\beta_r,
\tag{SE.14}
\]
with the following explicit integer sum:
\[
\begin{aligned}
\beta_r={}&\sum_{v=0}^{r-2}
\binom{r-1}v\binom{r-2}{r-2-v}
(-1)^{rv+r-1}(rv+r-1)!(N-rv-r+1)!\\
&-\sum_{v=1}^{r-1}
\binom{r-1}v\binom{r-2}{r-1-v}
\sum_{p=rv}^{rv+r-2}(-1)^p p!(N-p)!.
\end{aligned}
\tag{SE.15}
\]
The first line uses the root powers \(0,0\). The second uses
the powers \(t,r-t\), \(1\le t\le r-1\), with their
root-sum minus sign. This explains every endpoint and sign.

For \(f(p)=(-1)^p p!(N-p)!\), define
\(g(p)=(-1)^p(p+1)!(N-p)!\). Direct cancellation gives
\[
g(p)-g(p-1)=(N+2)f(p).
\tag{SE.16}
\]
Use (SE.16) on each interval in (SE.15). Set
\(C= r(2r^2-r+1)-1\) and \(T=2r^2-r\).
Combining the endpoint factorials gives exactly
\[
\beta_r=
\frac{\sum_{i=0}^r(-1)^{i-1}D_i\,i(C-Ti)}
{(r^2+1)r^3(r-1)}.
\tag{SE.17}
\]
Here is a direct check of the binomial combination, including the
endpoints. The three coefficients at the factorial
\((ri)![r(r-i)]!\), before the common denominator, use
\[
\begin{aligned}
\binom{r-1}{i-1}\binom{r-2}{i-1}
 &=\frac{i^2(r-i)}{r^2(r-1)}\binom ri^2,\\
\binom{r-1}{i-1}\binom{r-2}{i-2}
 &=\frac{i^2(i-1)}{r^2(r-1)}\binom ri^2,\\
\binom{r-1}i\binom{r-2}{i-1}
 &=\frac{i(r-i)^2}{r^2(r-1)}\binom ri^2.
\end{aligned}
\tag{SE.18}
\]
Their numerator becomes
\(i((r-i)(2r^2-r+1)+i-1)=i(C-Ti)\), as in (SE.17).
Terms outside the original ranges are zero in these displayed
polynomial expressions, so this combination includes \(i=0,r\).

Finally \(C-Tr=r-1\). Antisymmetrizing the quadratic
\(i(C-Ti)\) under \(i\mapsto r-i\) therefore gives
\[
\boxed{\beta_r=\frac{U_r}{2r^3(r^2+1)},\qquad
rB=2^{r-2}\frac{r-1}{2r(r^2+1)}\,U_r.}
\tag{SE.19}
\]
All manipulations are finite exact factorial identities.

## 5. Nonvanishing and the canonical conclusion

The endpoints \(i=0,r\) in (SE.11) contribute
\(2r(r^2)!\). For every interior index,
\[
\frac{D_i}{(r^2)!}
=\frac{\binom ri^2}{\binom{r^2}{ri}}
\le{\binom ri}^{2-r}\le r^{2-r}.
\tag{SE.20}
\]
The first inequality selects degree \(i\) from every factor of
\(((1+z)^r)^r\). The total absolute interior contribution is
at most \((r-1)(r-2)r^{2-r}(r^2)!<r(r^2)!\), because
\(r^{2-r}\le1/r\) and \((r-1)(r-2)<r^2\).
Thus \(U_r>0\) for every odd \(r\ge3\), including the endpoint.

Adding (SE.13) and (SE.19), the exact coefficient (SE.8) is
\[
\boxed{-\frac{\eta^{r^2+1}2^{r-2}}{(r!)^r}
\frac{r(r^2-r+2)}{2(r^2+1)}\,U_r\ne0.}
\tag{SE.21}
\]
It detects the actual retained-slot/common-polarization map.
The lower-map parameter check (SE.4), the exact annihilator
inclusion, and the multiplicity-one complementary-column pairing
prove R-029. Field extension to the displayed root splitting field
and inclusion into larger ambient spaces commute with all of these
maps, just as in ES.18.

The primary lower-map input is Sra, *The q-Foulkes problem III:
On Foulkes' conjecture with a graded inner factor*, Theorem 1.3,
[primary PDF](https://suvrit.github.io/papers/qfoulkes3/qfoulkes3-v1.pdf).
The exact kernel map is K.16–K.22 and P.9–P.16, and the highest
polynomial and complement maps are BS.8–BS.15. The scalar reduction
in this report is an exact evaluated family, without a historical
novelty claim.
