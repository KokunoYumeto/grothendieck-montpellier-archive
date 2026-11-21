# Every two-row quotient in the nonnegative twist region

## G-021. A positive formula and complete support for five parameters

Let \(x,b,k,t,d\ge0\), put \(a=b+x\), and define
\[
\begin{aligned}
n&=d+b+x+k+t,\\
\lambda&=(d+3b+2x+3k+4t,\ d+b+x+2k+t,\\
&\hspace{36mm}d+b+x,\ d+x,\ d).
\end{aligned}
\tag{TR.1}
\]
Every coefficient \(p_{\mu,(n)}^\lambda\), \(\mu\vdash5\), has the
positive formula (TR.15). It uses at most 122 active lattice polytopes,
each of dimension at most eleven, and fixed constants given by finite
differences of the seven elementary functions (TP.8). All constants
with positive difference order are strictly positive. The complete
zero set consists of the 155 explicitly recorded quadruples in §7,
after the sign twist (TR.3). This is a fixed description for the entire
family; the constants require no representation calculation at input
size. No claim of historical novelty is made.

## 1. The exact representation and bundle comparison

Retain the standard representation \(E=\mathfrak h_5\), the five
canonical points \(Z\subset\mathbf P(E)\), their ordinary ideal sheaf
\(\mathcal I\), and the tautological quotient \(Q\) of rank three.
Write \(c=2k+t\) and
\[
M_{x,b,k,t}=H^0\bigl(\mathbf P(E),
          \mathcal I^k(c)\otimes S_{(b+x,b)}Q\bigr).
\tag{TR.2}
\]
The G-015 normal-coordinate map and inverse balanced homogenization
give the actual equivariant isomorphism
\[
(S_\lambda\mathbf Q^5)_{(n^5)}
 \simeq\operatorname{sgn}^{d+b+x}\otimes M_{x,b,k,t}.
\tag{TR.3}
\]
Here is the relative-flag dictionary in full. The four-row weight is
\((d+a+c,d+a,d+x,d)\). After removing its determinant power \(d\),
the quotient weight is \((a,x,0)\) on \(Q^*\), and the first-line
twist is \(a+c\). Exterior-column contraction gives the perfect
pairing
\[
S_{(a,x)}Q^*\simeq(\det Q^*)^a\otimes S_{(a,b)}Q,
\qquad b=a-x.
\]
The identity \(\det Q^*=\det E^*\otimes\mathcal O(-1)\) changes
the twist to \(c\) and supplies the constant sign power \(a\).
Together with the removed determinant this is (TR.3). The point order
is exactly \(\lambda_2-n=k\). G-015 proves, through its displayed
normal ratios and inverse \(f\mapsto u^{-k}f(v(X))\), that extension
is exactly membership in \(\mathcal I^k\). Thus all maps used in
(TR.3) are specified bundle or polynomial maps.

For the outer character define
\[
\nu=\mu\quad(d+b+x\text{ even}),\qquad
\nu=\mu'\quad(d+b+x\text{ odd}).
\tag{TR.4}
\]
The required plethysm coefficient is \([\nu:M_{x,b,k,t}]\).

## 2. The complete two-row Schur complex

Put \(L=\mathcal O(-1)\subset E\). For \(N=a+b\), take the
tensor power of the complex \([L\to E]\), with \(L\) in degree
minus one. The permutation of tensor positions uses Koszul signs.
For line positions \(J\), its differential replaces position
\(j\in J\) by the tautological inclusion with sign
\((-1)^{|\{i\in J:i<j\}|}\). The two orders of replacing a pair
cancel, so this is a complex. Apply the primitive Young projector
\(e_T=c_Tr_T/h_{a,b}\) for the row-filled tableau of shape \((a,b)\).
The signed action commutes with the differential.

Its degree-minus-\(j\) term is obtained from
\(\operatorname{Ind}_{S_{N-j}\times S_j}^{S_N}
(E^{\otimes(N-j)}\otimes L^j\otimes\operatorname{sgn}_{S_j})\).
Exterior Pieri gives exactly the shapes obtained by deleting a vertical
\(j\)-strip. This identity follows directly by multiplying a Schur
alternant by \(e_j\): increase distinct exponents by one, discard
collisions, then divide by the Vandermonde. Multiplicities are one.
There are only two rows, so the resulting augmented complex is
\[
\begin{aligned}
0\longrightarrow& L^2 S_{(a-1,b-1)}E\\
\longrightarrow& L\bigl(S_{(a-1,b)}E\oplus S_{(a,b-1)}E\bigr)\\
\longrightarrow& S_{(a,b)}E\longrightarrow S_{(a,b)}Q\longrightarrow0.
\end{aligned}
\tag{TR.5}
\]
Only valid partition terms are retained. The detailed rational
polytabloid prescription in the appendix *The exact two-row quotient
complex*, (S.1)–(S.5), specifies each identification: solve the
adjacent-transposition intertwiner equations, choose the first nonzero
solution with first nonzero coordinate one, use the explicitly summed
Frobenius-reciprocity map, and evaluate at \(e_T\). Conjugating the
specified tensor differential by these rational maps fixes the maps
in (TR.5), including their scalars. They commute with frame change.

Locally split \(E=L\oplus Q\). The tensor complex contracts onto
\(Q^{\otimes N}\); average the contraction over \(S_N\) and
restrict to the idempotent image. This proves locally split exactness
of (TR.5). Its homotopy remains an identity after tensoring with
\(\mathcal I^k(c)\), so that tensoring preserves exactness.

For \(a=b>0\) the first middle summand is absent; for \(b=0<a\)
(TR.5) is the symmetric-quotient sequence; for \(a=b=0\) the
augmentation is the identity. At \(a=b=1\), its two maps are
\(l^2\mapsto l\otimes l\) and \(l\otimes e\mapsto l\wedge e\).
These include every boundary of (TR.1).

A-029 gives \(H^{q>0}(\mathcal I^k(c))=0\) for \(k\ge2\) and
\(c\ge2k\). Its precise known input is Kustin–Polini–Ulrich,
formula (6.1.4), p.1509, Lemma 6.3 and Corollary 6.4, p.1510,
with the local hypotheses verified there. For \(k=1\), degree-two
point evaluation and multiplication prove the same assertion; for
\(k=0\) it is scalar projective cohomology. The latter source is
Stacks Project, Lemma 30.8.1, tag 01XS. For the other two terms,
\(H^2=H^3=0\): the point quotient has finite support and their twists
are at least \(-2\). In the cohomology spectral sequence of (TR.5),
the only remaining \(H^1\)'s have total degrees zero or minus one.
There is no term of positive total degree. Exactness therefore proves
\[
H^{q>0}(\mathcal I^k(c)\otimes S_{(a,b)}Q)=0.
\tag{TR.6}
\]
The exceptional scalar groups at \(k=1,c=2\) are included in this
argument. No asserted surjectivity between those groups is needed.

## 3. Seven exact character polynomials

Write \(h_j(g)=\operatorname{tr}(g\mid\operatorname{Sym}^jE)\),
with \(h_{-1}=h_{-2}=0\), and let \(f_g\) be the fixed-letter
count. The exact affine-jet morphism of G-018 and A-033 gives
\(J_k(g)=f_gh_{k-1}(g)\). The line-bundle trivialization is fixed by
the stabilizer of the point, so this jet trace is independent of the
twist. In every twist of (TR.5), the scalar Euler trace is
\(h_j-J_k\). Define
\[
\begin{aligned}
s_{A,B}(g)&=h_A(g)h_B(g)-h_{A+1}(g)h_{B-1}(g),\\
S_0&=s_{a,b},\qquad
S_1=s_{a-1,b}+s_{a,b-1},\qquad Z=s_{a-1,b-1},\\
R&=S_0-S_1+Z,\qquad T=S_1-2Z.
\end{aligned}
\tag{TR.7}
\]
These Jacobi–Trudi formulas automatically give zero for every omitted
boundary term. The actual character of (TR.2), by (TR.5) and (TR.6), is
\[
\begin{aligned}
P_g(x,b,k,t)
&=S_0(h_c-J_k)-S_1(h_{c-1}-J_k)+Z(h_{c-2}-J_k)\\
&=R(h_c-J_k)+T(h_c-h_{c-1})
                  +Z(h_c-2h_{c-1}+h_{c-2}).
\end{aligned}
\tag{TR.8}
\]
The functions \(h_j\), class sizes and characters are exactly (TP.8)
and the seven-row character table in G-019. Their rational generating
functions are \((1-z)/\prod_{\ell\in\operatorname{cyc}(g)}(1-z^\ell)\).
Every formula in (TP.8), extended by its residue polynomial, also gives
zero at \(-1,-2\). Thus (TR.8) is polynomial on each of the
\(60^4\) residue classes, including their initial points.

For the identity class, direct expansion of (TR.7) gives
\[
R=\frac{(b+1)(x+1)(b+x+2)}2,\quad
T=R\frac{2b+x}{3},\quad Z=R\frac{b(b+x+1)}6.
\]
Consequently
\[
P_1=\frac{(b+1)(x+1)(b+x+2)}{12}
\bigl((c+1)(b+c+2)(b+x+c+3)-5k(k+1)(k+2)\bigr).
\tag{TR.9}
\]
With \(c=2k+t\), its 122 nonzero ordinary coefficients are positive.
Their exponent set is the following downset \(D\), with the first
pair denoting the exponents of \(x,b\):
\[
\begin{array}{c|c|r}
\text{first pair}&\text{last pair }(j,l)&\text{count}\\\hline
(0,0),(1,0),(0,1),(2,0),(0,2),(1,1),(2,1),(1,2)&j+l\le3&80\\
(3,0),(0,3),(3,1),(2,2),(1,3)&j+l\le2&30\\
(0,4),(1,4),(2,3),(3,2)&j+l\le1&12
\end{array}
\tag{TR.10}
\]
Nonnegative integer exponents are understood. The largest total
exponent is six. Expanding the displayed factors in (TR.9) proves
(TR.10); the certificate records all 122 rational coefficients.

## 4. Coefficientwise proof that every positive difference is positive

For a multiindex \(\alpha\), let \(\Delta^\alpha\) mean forward
difference of step 60 in the four variables \((x,b,k,t)\). For a
monomial \(X^e\), the exact rule in variable \(i\) is
\[
\Delta_i X^e=\sum_{q=0}^{e_i-1}
\binom{e_i}{q}60^{e_i-q}X^{e-(e_i-q)e_i^{\rm unit}}.
\tag{TR.11}
\]
All its coefficients are positive. In particular every
\(\Delta^\alpha P_1\), \(\alpha\in D\), has positive constant
coefficient, and every difference outside \(D\) vanishes.

Here is a small exact coefficient certificate for all the other
classes. For a residue phase \(p\), substitute in (TR.7)–(TR.8)
\[
h_N(2\,1^3)=\frac{N^2+4N+4-(N\bmod2)}4,\quad
h_N(2^2\,1)=\begin{cases}(N+2)/2,&N\text{ even},\\0,&N\text{ odd},\end{cases}
\]
\[
h_N(3\,1^2)=\frac{N+3-(N\bmod3)}3.
\tag{TR.12}
\]
The phases are the 16 four-tuples modulo two in each of the first two
cases and the 81 four-tuples modulo three in the last case. Expanding
(TR.8) gives total degrees at most three, two and one, respectively.
For the remaining three conjugacy classes every trace in (TP.8) is
periodic, so every positive step-60 difference vanishes.

For \(1\le|\alpha|\le3\), and each ordinary monomial exponent
\(\beta\), let \(B_{g,\alpha,\beta}\) be the maximum absolute
coefficient of \(X^\beta\) in \(\Delta^\alpha P_g\) over those
16, 16 or 81 phases. Define the explicit rational polynomial
\[
D_\alpha=\Delta^\alpha P_1-
\sum_\beta(10B_{2,\alpha,\beta}+15B_{22,\alpha,\beta}
                         +20B_{3,\alpha,\beta})X^\beta.
\tag{TR.13}
\]
Every coefficient is nonnegative, and its constant coefficient is
strictly positive. The following complete table records, for all 34
orders, the smallest nonzero coefficient margin and the constant
margin. It is checked by expanding only the explicitly specified
rational polynomials (TR.9),(TR.12), using (TR.11). The delivered
`two_row_quotient_polynomial_bound.py` performs exactly these finite
rational operations; its JSON records every identity coefficient,
all downset exponents, and every comparison. A separate agent's
independent reconstruction is recorded in the verification appendix.

| order in x,b,k,t | least coefficient margin | constant margin |
|---|---:|---:|
| 0,0,0,1 | 5 | 29260 |
| 0,0,0,2 | 600 | 205200 |
| 0,0,0,3 | 108000 | 216000 |
| 0,0,1,0 | 10 | 103320 |
| 0,0,1,1 | 1200 | 626400 |
| 0,0,1,2 | 216000 | 432000 |
| 0,0,2,0 | 2400 | 640800 |
| 0,0,2,1 | 432000 | 864000 |
| 0,0,3,0 | 324000 | 648000 |
| 0,1,0,0 | 5 | 1206640 |
| 0,1,0,1 | 600 | 286641600 |
| 0,1,0,2 | 36000 | 693612000 |
| 0,1,1,0 | 1200 | 910333200 |
| 0,1,1,1 | 72000 | 1795464000 |
| 0,1,2,0 | 144000 | 2333808000 |
| 0,2,0,0 | 600 | 15952800 |
| 0,2,0,1 | 36000 | 1905804000 |
| 0,2,1,0 | 72000 | 5515488000 |
| 0,3,0,0 | 216000 | 39744000 |
| 1,0,0,0 | 5 | 29260 |
| 1,0,0,1 | 300 | 145951200 |
| 1,0,0,2 | 72000 | 557460000 |
| 1,0,1,0 | 600 | 492800400 |
| 1,0,1,1 | 144000 | 1523160000 |
| 1,0,2,0 | 288000 | 1789200000 |
| 1,1,0,0 | 600 | 286641600 |
| 1,1,0,1 | 72000 | 50797548000 |
| 1,1,1,0 | 144000 | 157825656000 |
| 1,2,0,0 | 36000 | 1905804000 |
| 2,0,0,0 | 600 | 205200 |
| 2,0,0,1 | 72000 | 557460000 |
| 2,0,1,0 | 144000 | 2028240000 |
| 2,1,0,0 | 36000 | 693612000 |
| 3,0,0,0 | 108000 | 216000 |

The character bound \(|\chi_\nu(g)|\le\dim\nu\) follows by averaging
an inner product and diagonalizing the finite-order unitary operator.
For every nonnegative residue vector \(r\), the triangle inequality
applied coefficientwise to (TR.13) therefore proves
\[
\frac1{120}\sum_g|g^{S_5}|\chi_\nu(g)
                         (\Delta^\alpha P_g)(r)
\ \ge\ \frac{\dim\nu}{120}D_\alpha(r)>0
\quad(1\le|\alpha|\le3).
\tag{TR.14}
\]
For \(|\alpha|\ge4\) every nonidentity term is zero. Positivity
then follows directly from (TR.9)–(TR.11) for \(\alpha\in D\).
Outside \(D\) all terms vanish. This proves the sign assertion for
all residues without a computation over their \(60^4\) choices.
The differences are integers because they are differences of the
actual character multiplicities in (TR.3),(TR.8).

## 5. The positive Newton formula and exact lattice maps

For \(r\in\{0,\ldots,59\}^4\) and \(\alpha\in D\), set
\[
C_{\nu,\alpha}(r)=\frac1{120}\sum_g|g^{S_5}|\chi_\nu(g)
                                    (\Delta^\alpha P_g)(r).
\]
All these constants are nonnegative integers. The zeroth one is an
actual multiplicity by (TR.3); every other one is strictly positive
by (TR.14). Write \((x,b,k,t)=r+60q\). The finite Newton identity
in four variables gives exactly
\[
\boxed{p_{\mu,(n)}^\lambda
 =\sum_{\alpha\in D}C_{\nu,\alpha}(r)
                  \prod_{i=1}^4\binom{q_i}{\alpha_i}.}
\tag{TR.15}
\]
One proof of this interpolation identity is to apply successively
\(f(q)=\sum_j\Delta^jf(0)\binom qj\) in each variable. The latter
identity follows by induction from
\(\Delta\binom qj=\binom q{j-1}\). Degrees and (TR.10) make every
omitted coefficient zero, so the expansion terminates exactly as
stated.

For each fixed residue and exponent, introduce integer variables
\(q_1,\ldots,q_4,y\), and, for each \(i\), a chain
\(z_{i,1},\ldots,z_{i,\alpha_i}\). The polytope is specified by
\[
60q_i=X_i-r_i,\quad q_i\ge0,\quad
0\le y<C_{\nu,\alpha}(r),\quad
0\le z_{i,1}<\cdots<z_{i,\alpha_i}<q_i,
\tag{TR.16}
\]
with empty chains omitted. Convert strict inequalities to differences
at most minus one. Every coordinate and inequality has now been
specified. The bijection sends a point to its \(y\)-choice and its
four subsets of \(\{0,\ldots,q_i-1\}\); its inverse writes each
subset in increasing order. Its number of points is precisely the
summand in (TR.15). Since \(|\alpha|\le6\), at most eleven integer
variables occur. There are 122 active tags, or
\(60^4\cdot122=1,581,120,000\) tags in the uniform description
before selecting the unique residue. This large fixed number is
stated explicitly; the evaluator selects the active residue first.

All constants are given by fixed finite sums with input-independent
indices. The largest possible trace index in a conservative rectangular
bound is 539. Thus evaluation uses a fixed number of integer arithmetic
operations, followed by binomial coefficients of order at most four.
With elementary integer multiplication its bit complexity is
\(O(\log^2(2+x+b+k+t+d))\). The polytope right-hand sides have the
same logarithmic bit size plus fixed constants. The finite-group
projectors and Young functors here are over \(\mathbf Q\); their
integral models and required denominators are carried by the actual
maps, as explained in the geometric dictionary.

## 6. Independent overlap and finite computations

The residue-zero-order check streams all
\(7\cdot60^4=90,720,000\) multiplicities. Its factors are first
computed with arbitrary-precision integers. The bound on every weighted
class partial sum is 2,493,689,811,648, established before conversion
to signed 64-bit integers. Every value is integral and nonnegative.
The delivered `TWO_ROW_QUOTIENT_SUPPORT.json` records exact zero
quadruples, extrema and per-label SHA256 hashes; the stream order and
integer byte order are specified. This is a computation certificate,
not a proof-assistant verification.

The rectangular agent independently computed all 882 actual plethysm
coefficients with \(x+b+k+t+d\le4\), using the Murnaghan–Nakayama
rule in the full symmetric group, and obtained agreement for every
outer label. The theta agent independently computed all 120,960,000
Newton constants on the slice \(t=0\), using three separable Euler
products and cycle recurrences. All agree with the nonnegativity
statement; that slice has 55 active orders and 70 total zeros.
These checks corroborate the exact representation morphisms and sign
in (TR.3), while §§2–5 prove the whole parameter family.

## 7. The complete exceptional support

Every first-order constant is strictly positive. Thus a positive
quotient \(q_i\) makes (TR.15) positive, using its order-one term.
Every zero therefore lies inside the residue cube. Its complete
155-element list follows, grouped by effective outer label \(\nu\).
The four entries of each tuple are \((x,b,k,t)\). The parameter
\(d\) affects only the sign twist (TR.4).

### Effective label 5 — 19 zeros

`(0,0,0,1)` `(0,0,1,0)` `(0,0,1,1)` `(0,1,0,0)` `(0,1,0,1)`

`(0,1,0,2)` `(0,1,0,3)` `(0,1,0,4)` `(0,1,1,0)` `(0,1,1,1)`

`(0,1,1,2)` `(0,1,2,0)` `(0,3,0,0)` `(0,5,0,0)` `(1,0,0,0)`

`(1,0,0,1)` `(1,1,0,0)` `(1,1,0,1)` `(2,1,0,0)`


### Effective label 41 — 4 zeros

`(0,0,0,0)` `(0,0,1,0)` `(0,1,0,0)` `(0,1,0,1)`


### Effective label 32 — 4 zeros

`(0,0,0,0)` `(0,0,0,1)` `(0,1,0,0)` `(1,0,0,0)`


### Effective label 311 — 8 zeros

`(0,0,0,0)` `(0,0,0,1)` `(0,0,0,2)` `(0,0,1,0)` `(0,0,2,0)`

`(0,2,0,0)` `(1,0,0,0)` `(2,0,0,0)`


### Effective label 221 — 11 zeros

`(0,0,0,0)` `(0,0,0,1)` `(0,0,0,2)` `(0,0,0,3)` `(0,0,1,0)`

`(0,0,1,1)` `(0,1,0,0)` `(1,0,0,0)` `(1,0,0,1)` `(2,0,0,0)`

`(3,0,0,0)`


### Effective label 2111 — 24 zeros

`(0,0,0,0)` `(0,0,0,1)` `(0,0,0,2)` `(0,0,0,3)` `(0,0,0,4)`

`(0,0,0,5)` `(0,0,1,0)` `(0,0,1,1)` `(0,0,1,2)` `(0,0,1,3)`

`(0,0,2,0)` `(0,0,2,1)` `(0,1,0,0)` `(0,2,0,0)` `(1,0,0,0)`

`(1,0,0,1)` `(1,0,0,2)` `(1,0,1,0)` `(1,1,0,0)` `(2,0,0,0)`

`(2,0,0,1)` `(3,0,0,0)` `(4,0,0,0)` `(5,0,0,0)`


### Effective label 11111 — 85 zeros

`(0,0,0,0)` `(0,0,0,1)` `(0,0,0,2)` `(0,0,0,3)` `(0,0,0,4)`

`(0,0,0,5)` `(0,0,0,6)` `(0,0,0,7)` `(0,0,0,8)` `(0,0,0,9)`

`(0,0,0,11)` `(0,0,1,0)` `(0,0,1,1)` `(0,0,1,2)` `(0,0,1,3)`

`(0,0,1,4)` `(0,0,1,5)` `(0,0,1,6)` `(0,0,1,7)` `(0,0,1,9)`

`(0,0,2,0)` `(0,0,2,1)` `(0,0,2,2)` `(0,0,2,3)` `(0,0,2,4)`

`(0,0,2,5)` `(0,0,2,7)` `(0,0,3,0)` `(0,0,3,1)` `(0,0,3,2)`

`(0,0,3,3)` `(0,0,3,5)` `(0,0,4,0)` `(0,0,4,1)` `(0,0,4,3)`

`(0,0,5,1)` `(0,1,0,0)` `(0,1,0,1)` `(0,1,0,2)` `(0,1,1,0)`

`(0,1,2,0)` `(0,2,0,0)` `(0,2,0,1)` `(0,2,0,3)` `(0,2,1,1)`

`(0,3,0,0)` `(0,5,0,0)` `(1,0,0,0)` `(1,0,0,1)` `(1,0,0,2)`

`(1,0,0,3)` `(1,0,0,4)` `(1,0,0,5)` `(1,0,1,0)` `(1,0,1,1)`

`(1,0,1,2)` `(1,0,1,3)` `(1,0,2,0)` `(1,0,2,1)` `(1,1,0,0)`

`(1,1,0,1)` `(1,2,0,0)` `(2,0,0,0)` `(2,0,0,1)` `(2,0,0,2)`

`(2,0,0,3)` `(2,0,1,0)` `(2,0,1,1)` `(2,1,0,0)` `(3,0,0,0)`

`(3,0,0,1)` `(3,0,0,2)` `(3,0,1,0)` `(3,1,0,0)` `(3,2,0,0)`

`(4,0,0,0)` `(4,0,0,1)` `(4,1,0,0)` `(5,0,0,0)` `(5,0,0,1)`

`(6,0,0,0)` `(7,0,0,0)` `(8,0,0,0)` `(9,0,0,0)` `(11,0,0,0)`


## 8. Exact coverage of both outside regions

The formula evaluates every partition \(\lambda\vdash5n\) with at
most five parts satisfying
\[
\lambda_2+\lambda_3\le2n
\quad\text{or}\quad
\lambda_3+\lambda_4\ge2n.
\tag{TR.17}
\]
The following explicit maps prove this larger formulation.

For the first inequality, set
\[
\begin{gathered}
d=\lambda_5,\quad x=\lambda_4-\lambda_5,\quad
b=\lambda_3-\lambda_4,\quad k=\max(0,\lambda_2-n),\\
t=\lambda_2-\lambda_3-2k,\qquad e=\max(0,n-\lambda_2).
\end{gathered}
\tag{TR.18}
\]
All six integers are nonnegative, and \(ke=0\). The base partition
in (TR.1) has the same last four parts and first part
\(\lambda_1-5e\); its inner degree is \(n-e\). At \(e=0\),
(TR.1) applies directly. At \(e>0\), \(k=0\), and G-015's two
balanced-chart expressions differ by multiplication by
\(u^e=(\prod_{i=1}^5X_{i1})^e\). Their coefficient space is the
same full flag-section space because neither chart imposes a positive
point order. The inverse divides by \(u^e\) on this image; the
normal-order argument proves polynomial extension in both descriptions.
The polynomial \(u\) is fixed by slot permutations. Thus this is an
actual \(S_5\)-equivariant isomorphism of the two balanced spaces,
proving equality of every outer coefficient.

For the second inequality, set \(H=\lambda_1\),
\(n^c=H-n\), and
\(\lambda^c=(H-\lambda_5,\ldots,H-\lambda_1)\). These are
nonnegative partition data, and
\(\lambda^c_2+\lambda^c_3\le2n^c\). Complementary-column exterior
multiplication gives the perfect equivariant pairing
\[
S_\lambda\mathbf Q^5\otimes S_{\lambda^c}\mathbf Q^5
 \longrightarrow(\det\mathbf Q^5)^H.
\tag{TR.19}
\]
It pairs the weight \((n^5)\) perfectly with \(((H-n)^5)\).
Permutation matrices act on its target by \(\operatorname{sgn}^H\).
All rational irreducible \(S_5\) modules are self-dual, as is also
seen from their real characters. Thus the outer coefficient at
\((\lambda,n,\mu)\) equals that at
\((\lambda^c,n^c,\mu)\) for even \(H\), or at
\((\lambda^c,n^c,\mu')\) for odd \(H\). Applying (TR.18) to the
complement proves the second region through this exact pairing.

The remaining direct outer-five evaluation gate after G-021 is
therefore the strictly smaller region
\(\lambda_2+\lambda_3>2n>\lambda_3+\lambda_4\). In the first
chart its ideal-twisted two-row quotient has \(c<2k\). The general
terminating positive construction G-010 already applies there; the
remaining task is to replace that preprocessing by an evaluated small
formula such as (TR.15).
