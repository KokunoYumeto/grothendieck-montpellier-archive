# A uniform positive formula for every stable hook tail

## G-037. Varying outer degree, hook length and outer Schur label

Let \(m\ge3\), \(a\ge1\), \(0\le r\le m-2\), \(t\ge0\),
and \(n\ge a+t\) be integers. Put
\[
\begin{gathered}
A=mn-a-(m-1)t-r,\qquad D=a+r,\\
\lambda=(A,a+t,(t+1)^r,t^{m-2-r}).
\end{gathered}
\tag{HK.1}
\]
For every \(\mu\vdash m\), the coefficient
\(p_{\mu,(n)}^\lambda\) equals the number of integer points
in one explicitly constructed bounded rational polytope.
It has at most \(m^2+3m-4\) variables and polynomially many
integer constraints. Its matrices are constructed directly below.
An exact rational-series evaluator computes the coefficient in
time polynomial in \(m\) and the binary parameter lengths.

The encoding assertion is precise. With \(m\) explicitly sized,
these are uniform polynomial bounds. For \(t\ge1\), all \(m\)
parts of \(\lambda\) are positive, so its ordinary explicit list
contains \(m\) entries. The bounds are polynomial in that binary-part
input length and give a \(\#P\) lattice verifier. At \(t=0\), a
compressed list can have far fewer than \(m\) entries; the bound
in \(m\) is retained without asserting a bound polynomial in
\(\log m\). The formulas and support include \(t=0\).

There is a complete support test. Put
\(\nu=\mu\) for even \(t\), and \(\nu=\mu'\) for odd \(t\).
For \(\nu\ne(m)\), let \(C_\nu\) be its cells except
\((1,1),(2,1)\), and put \(w(i,j)=j-i+1\).
Let \(L\) be \(b(\nu)=\sum_i(i-1)\nu_i\) plus the sum of
the \(r\) smallest weights in this multiset. Then
\[
\boxed{\begin{aligned}
p_{\mu,(n)}^\lambda>0\iff{}&D\ge L\ \text{and}\\
&\neg\bigl(D=L+1,\ \nu\text{ rectangular},\ r\in\{0,m-2\}\bigr).
\end{aligned}}
\tag{HK.2}
\]
For \(\nu=(m)\), put \(L_0=(r+2)(r+3)/2-1\). Then
\[
\boxed{\begin{aligned}
p_{\mu,(n)}^\lambda>0\iff{}&D\ge L_0\ \text{and}\\
&\neg\bigl(r=m-2,\ D=L_0+1\bigr).
\end{aligned}}
\tag{HK.3}
\]
The reflection-group identities used below are cited as known results.
The actual plethysm comparison, uniform polytope, support and
evaluation algorithm are specified in full.

## 1. The balanced chart and the actual hook module

The first gap is
\[
A-a-t=m(n-a-t)+(m-2)a-r\ge0.
\]
The remaining parts are ordered and sum to \(mn\). Thus every
declared parameter gives a partition, including
\(a=1,r=m-2,n=a+t\).

Let \(W=\mathfrak h_m\) be the sum-zero standard permutation
module. T032/C4–C8 gives the actual equivariant isomorphism
\[
(S_\lambda\mathbb Q^m)_{(n^m)}
\simeq S_{(a+t,(t+1)^r,t^{m-2-r})}W
\simeq\operatorname{sgn}^t\otimes S_{(a,1^r)}W.
\tag{HK.4}
\]
The first map substitutes the balanced flag minors and multiplies
by \(u^{n-a-t}\), with the proved inverse chart. The second
uses the exterior-volume tensor and rational Young projectors;
\(\det W=\operatorname{sgn}\). The Specht column/row Young
comparison identifies \([\mu]\otimes\operatorname{sgn}\)
with \([\mu']\). Thus the requested coefficient is the
\([\nu]\)-multiplicity in the displayed hook module.

Put \(P=\operatorname{Sym}W\). Define the Koszul differential
\[
\partial(f\otimes v_1\wedge\cdots\wedge v_j)
=\sum_{s=1}^j(-1)^{s-1}fv_s\otimes
v_1\wedge\cdots\widehat v_s\cdots\wedge v_j.
\tag{HK.5}
\]
Give polynomial degree \(d\) tensored with exterior degree \(j\)
total degree \(d+j\). These equivariant maps preserve total degree.
The exterior derivative \(d_P\) satisfies
\(\partial d_P+d_P\partial=D\,\mathrm{id}\) on total degree \(D\):
the product and exterior rules prove this on each monomial wedge.
Hence \(D^{-1}d_P\) is an explicit contracting homotopy for \(D>0\).

Write \(Z_j=\ker\partial_j\) for \(j\ge1\), and \(Z_0=P_+\).
The actual Young inclusion identifies
\[
(Z_r)_D\simeq S_{(D-r,1^r)}W\qquad(D-r\ge1).
\tag{HK.6}
\]
Indeed exterior Pieri decomposes
\(\operatorname{Sym}^{D-r}W\otimes\Lambda^rW\) into the two
Young-projector images of shapes \((D-r+1,1^{r-1})\) and
\((D-r,1^r)\). The target of \(\partial\) contains the first
and no second shape. On the first highest vector
\(x_1^{D-r}\otimes e_1\wedge\cdots\wedge e_r\), the differential
has the nonzero term
\(x_1^{D-r+1}\otimes e_2\wedge\cdots\wedge e_r\).
Thus its kernel is exactly the second Young image. At \(r=0\)
this is the identity in positive degree. This specifies the
comparison map, including the one-column endpoint.

## 2. The exact bivariate character and its positive cancellation

For a cycle type \(\rho\vdash m\), the polynomial/exterior trace is
\[
\frac{\det(1+u\rho\mid W)}{\det(1-q\rho\mid W)}
=\frac{1-q}{1+u}
\prod_{j\in\rho}\frac{1-(-u)^j}{1-q^j}.
\tag{HK.7}
\]
Multiply the eigenvalues of each literal permutation cycle and
remove the fixed trivial line to obtain this identity.
Taking its Frobenius inner product with \([\nu]\) computes the
actual multiplicity series of \(P\otimes\Lambda W\).

Macdonald, *Symmetric Functions and Hall Polynomials*, second
edition, I§3 Examples2–3, printed p.45, gives
\[
s_\nu\left[\frac{1-z}{1-q}\right]
=q^{b(\nu)}\prod_{c\in\nu}
\frac{1-zq^{\operatorname{ct}(c)}}{1-q^{h(c)}}.
\tag{HK.8}
\]
Its substitution is \(z=-u\), with exactly the power sums in
(HK.7). The source's polynomial interpolation proof from finite
principal specialization applies to this formal exterior variable.
T027/S13–S15 gives the complete standardization bijection
\[
f_\nu(q):=\sum_{T\in\operatorname{SYT}(\nu)}
q^{\operatorname{comaj}(T)}
=q^{b(\nu)}
\frac{\prod_{i=1}^m(1-q^i)}
{\prod_{c\in\nu}(1-q^{h(c)})}.
\tag{HK.9}
\]
Here \(\operatorname{comaj}(T)=\sum_{j\in\operatorname{Des}(T)}(m-j)\),
and a descent places \(j+1\) in a lower row.

Put \(Q_m(q)=\prod_{i=2}^m(1-q^i)\). Cancelling the factor
for the specified cell \((1,1)\) gives
\[
\operatorname{Hilb}_\nu(P\otimes\Lambda W;q,u)
=\frac{f_\nu(q)}{Q_m(q)}
\prod_{c\ne(1,1)}(1+u q^{\operatorname{ct}(c)}).
\tag{HK.10}
\]
The total-degree convention replaces \(u\) by \(qu\).
The actual short exact sequences from §1, with \(P/Z_0=\mathbb Q\),
give
\[
(1+u)\sum_{j\ge0}\operatorname{Hilb}_\nu(Z_j;q)u^j
=\operatorname{Hilb}_\nu(P\otimes\Lambda W;q,qu)
-\mathbf1_{\nu=(m)}.
\tag{HK.11}
\]
For \(\nu\ne(m)\), the cell \((2,1)\) exists and has content
\(-1\). Its factor on the right is exactly \(1+u\).
Consequently
\[
\boxed{
p_{\mu,(n)}^\lambda
=[q^D]\frac{f_\nu(q)\,
e_r(q^{w(c)}:c\in C_\nu)}{Q_m(q)}.}
\tag{HK.12}
\]
The elementary polynomial sums over \(r\)-element subsets of
the specified cells; repeated equal weights retain distinct choices.
Its product with \(f_\nu\) has nonnegative coefficients and
nonnegative exponents. For any chosen set \(J\),
\[
b(\nu)+\sum_{(i,j)\in J}(j-i+1)
=\sum_{(i,j)\notin J}(i-1)+\sum_{(i,j)\in J}j\ge0.
\]
Every fake-degree exponent is at least \(b(\nu)\). Thus negative
cell weights cause no negative exponent in the numerator.
The exact sequences and Young maps above establish the original
module comparison; (HK.9) and literal subset expansion give the
subsequent finite-set count.

## 3. The invariant branch and an actual monomial basis

For \(\nu=(m)\), the invariant polynomial ring on \(W\) is
\(I=\mathbb Q[e_2,\ldots,e_m]\). Solomon, *Invariants of finite
reflection groups*, Nagoya Math. J.22 (1963), §3, unnumbered
Theorem p.59, proof pp.59–61, identifies invariant differential
forms as the exterior algebra over \(I\) on \(de_2,\ldots,de_m\).
The actual map sends each generator to that differential; its
inverse is the unique invariant coefficient expansion.
Use the invariant rational dot product on \(W\) and its inverse
to identify these forms with \(P\otimes\Lambda W\).

Euler contraction gives \(\partial(de_j)=j e_j\).
The scaled generators \(\xi_j=de_j/j\) therefore give the
actual weighted Koszul complex
\[
I\otimes\Lambda(\xi_2,\ldots,\xi_m),\qquad
\partial\xi_j=e_j,\qquad
\deg e_j=\deg\xi_j=j.
\tag{HK.13}
\]
Rational averaging makes invariant projection exact, so its cycles
are precisely the required invariant cycles.

Give both \(e_j\) and \(\xi_j\) the \(j\)-th unit multidegree.
For \(\beta=(\beta_2,\ldots,\beta_m)\), let
\(J=\{j:\beta_j>0\}\) and \(i=\min J\).
The monomials \(e^{\beta-\mathbf1_S}\xi_S\), \(S\subseteq J\),
identify this multigraded complex with the exterior algebra on
basis \(v_j\), whose differential contracts \(v_j\mapsto1\).
Its degree-\(r\) kernel has the explicit basis
\[
e^\beta\bigwedge_{j\in T}
\left(\frac{\xi_j}{e_j}-\frac{\xi_i}{e_i}\right),
\qquad T\subseteq J\setminus\{i\},\quad |T|=r.
\tag{HK.14}
\]
Each expression is polynomial: in a nonzero wedge term each
denominator occurs at most once and has positive exponent in
\(\beta\). In the basis \(v_i,v_j-v_i\), contraction kills exactly
the exterior algebra in the latter vectors. This proves spanning
and independence. In exterior degree zero retain positive total
degree, giving \(Z_0=I_+\).

The unique least support index, the chosen subset and the remaining
monomial exponents give the positive series
\[
\boxed{
p_{\mu,(n)}^\lambda
=[q^D]\sum_{i=2}^m
\frac{q^i e_r(q^{i+1},\ldots,q^m)}
{\prod_{j=i}^m(1-q^j)}.}
\tag{HK.15}
\]
This counts the actual basis (HK.14).

## 4. The literal integer polytopes

For the nontrivial branch, use \(X_{c,j}\) for each cell
\(c\in\nu\) and label \(1\le j\le m\), descent bits
\(\delta_j\) for \(j<m\), subset bits \(Y_c\) for \(c\in C_\nu\),
and coin variables \(b_i\) for \(2\le i\le m\).
All \(X,\delta,Y\) lie in \([0,1]\) and all \(b_i\ge0\).
Impose
\[
\sum_jX_{c,j}=1,\qquad
\sum_cX_{c,j}=1,\qquad
\sum_{c\in C_\nu}Y_c=r.
\tag{HK.16}
\]
Put \(\ell_c=\sum_jjX_{c,j}\) and
\(R_j=\sum_c\operatorname{row}(c)X_{c,j}\).
For an adjacent right or lower cell \(c'\), impose
\(\ell_c+1\le\ell_{c'}\). Also impose
\[
1-m(1-\delta_j)\le R_{j+1}-R_j\le m\delta_j
\qquad(1\le j<m)
\tag{HK.17}
\]
and the degree equation
\[
\sum_{i=2}^m i b_i+
\sum_{j=1}^{m-1}(m-j)\delta_j+
\sum_{c\in C_\nu}w(c)Y_c=D.
\tag{HK.18}
\]
Include \(b_i\le\lfloor(D+m^2)/i\rfloor\).
These bounds follow from (HK.18), since all negative contributions
are bounded cell weights. At an integer point (HK.16) assigns
every label exactly once. The adjacency conditions give a standard
tableau. Equation (HK.17) uniquely fixes its descents, and the
\(Y\)'s choose its cell subset. Equation (HK.18) counts exactly
(HK.12). The converse fixes every variable, so this is a bijection.
The number of variables is \(m^2+3m-4\).

For the trivial branch use \(z_j,y_j,\beta_j\), \(2\le j\le m\),
with \(0\le z_j,y_j\le1\) and
\(0\le\beta_j\le\lfloor D/j\rfloor\). Impose
\[
\begin{gathered}
\sum_jz_j=1,\quad \sum_jy_j=r,\qquad
y_j\le\sum_{i<j}z_i,\\
\beta_j\ge z_j+y_j,\qquad
\beta_j\le D\sum_{i\le j}z_i,\qquad
\sum_{j=2}^m j\beta_j=D.
\end{gathered}
\tag{HK.19}
\]
The single nonzero \(z_i\) is the least positive exponent index:
lower exponents are zero and \(\beta_i\ge1\).
The \(y\)-indices lie above it and have positive exponents.
Thus each integer point is precisely one basis element (HK.14),
and conversely each such element fixes every variable.
This branch has \(3m-3\) variables.

All matrices are integer linear matrices of polynomial size.
The bit lengths of the coefficients and bounded integer witnesses
are polynomial in the declared encoding. Matrix multiplication
checks a witness in polynomial time. Both polytopes are bounded,
including when their lattice counts are zero.

## 5. Proof of the exact support test

T028/S23–S25 proves by semistandard tableaux that the lowest
coefficient of \(f_\nu\) is one in degree \(b(\nu)\), and its
next coefficient is the number of removable corners minus one.
The lowest elementary-subset degree in (HK.12) is the sum of
the \(r\) smallest weights. No degree below \(L\) occurs,
and degree \(L\) occurs. Since \(m\ge3\), coin weights two and
three occur in the denominator. Every integer at least two is
their nonnegative sum. Thus every degree at least \(L+2\)
occurs; only the next degree needs analysis.

A nonrectangular partition has at least two removable corners,
so its next fake-degree coefficient is positive.
For a rectangular non-row partition, the retained weights form
a consecutive integer interval. For a column these are
\(2-i\), \(3\le i\le m\). For a height-two rectangle of width
at least two, they range from one to the width.
For height at least three and width at least two, adjacent
row intervals overlap; removing the two specified cells removes
no weight value, since their values one and zero also occur
at \((2,2)\) and \((3,2)\).

Every nonempty proper minimum-cardinality subset of a nonconstant
consecutive multiset admits an increase of its sum by one.
At a strict sorted cut replace the largest selected value by
the next. At an equal cut value, replace a selected cut value
by a value one higher. At a cut at the maximum value, replace
a selected value one lower by an unselected maximum.
Consecutiveness and nonconstancy ensure the required values.
Thus \(0<r<m-2\) gives a positive next elementary coefficient.
At \(r=0,m-2\) the elementary polynomial has a single exponent.
The cases with at most one retained cell have no nonempty proper
subset. This proves exactly (HK.2).

For (HK.15), the minimum is
\(i=2,T=\{3,\ldots,r+2\}\), of degree
\(2+3+\cdots+(r+2)=L_0\). When \(r<m-2\), increasing the
largest selected index by one gives degree \(L_0+1\);
for \(r=0\), use \(i=3\).
At \(r=m-2\) the minimum tag is the only tag, and the
coins cannot add one. Its denominator includes weights two
and three, so all increments at least two occur.
This proves (HK.3).

## 6. Exact evaluation at binary-sized degrees

Compute (HK.9) to degree \(\binom m2\) by polynomial multiplication
and division by \(1-q^{h(c)}\). Its finite tableau expression
proves that degree bound and positivity. Compute each elementary
polynomial by cardinality-indexed dynamic multiplication.
The numerator in (HK.12) has degree \(O(m^2)\), nonnegative
exponents, and coefficient bit length \(O(m\log m)\).
Equation (HK.15) has at most \(m-1\) positive rational terms
with numerator and denominator degrees \(O(m^2)\).

Use Bostan–Mori, *A Simple and Fast Algorithm for Computing the N-th Term of a Linearly Recurrent Sequence*, SOSA2021, §2.1, proof of Theorem1 and Algorithm1 (OneCoeff), printed pp121–122, author PDF pp4–5, <https://specfun.inria.fr/bostan/BoMo21.pdf>. The following specialization records its exact parity map and the bit bound for these particular denominators.

For any one of these fractions \(P(q)/Q(q)\), put
\(S(q)=P(q)Q(-q)\) and \(T(q)=Q(q)Q(-q)\).
The latter has only even powers. Retain in \(S\) the powers
of the desired parity and halve their indices; in \(T\)
retain the even powers and halve their indices. These new
polynomials give the coefficient in degree \(\lfloor D/2\rfloor\).
Indeed expanding \(S/T\) and taking its even or odd part gives
exactly this identity. Iterate to degree zero and divide the
constant terms. This proves the exact parity algorithm used
by the evaluator.

There are \(O(\log(D+1))\) iterations with degree \(O(m^2)\).
Denominator roots remain roots of unity: the step squares
each root while retaining its multiplicity. The constant term
is one, so coefficients have magnitudes at most \(2^{O(m^2)}\).
Each numerator step increases its coefficient bit length by
only \(O(m^2)\). Thus the arithmetic has polynomial bit
complexity in \(m\) and \(\log(D+1)\). This proves the claimed
evaluation bound as well as the independent polytope construction.

## 7. Geometric dictionary and verification

The balanced flag chart (HK.4) is T032's actual coordinate and
section map. Its frame and Proj constructions use SGA3
I4.5/4.7.2–4.7.3 and EGA II2.4.1–2.4.2,2.5.2/2.5.4.
The hook is the coherent Koszul kernel on the affine space
associated to \(W\), with explicit Euler contraction and
homogeneous contracting homotopy. The invariant differential
map (HK.13), its scalar division and the basis (HK.14)
give the same cycle module through actual arrows.
Young projection, determinant volume and Specht sign retain
the original representation and its associated bundle.
Its class lies in SGA6 VI3.3; Schur/λ operations use SGA6
V4.2,4.4,4.8–4.9. Cote133/028 is carried by A012's
tensor-word, torus-weight and Young maps.
Rational maps spread over the base obtained by inverting their
finite denominators; multiplicities are on the characteristic-zero
generic fiber.

The final matrices count the literal tableaux, cell subsets
and monomial-cycle basis through the proved inverse encodings.
They give effective section multiplicities throughout this
stable-hook family with varying outer degree and hook length.
The general varying-shape positive-description gate is recorded
separately.

The file `stable_hook_positive.py` exports the sparse integer
matrices, validation function, exact support test and binary-degree
evaluator. The separate checker computes actual permutation-cycle
Schur traces through hook Jacobi–Trudi and literal
Murnaghan–Nakayama character inner products. It also checks
original plethysms through power-sum composition and every
generated small matrix witness. Its executed counts and outcome
are in `STABLE_HOOK_POSITIVE_RECEIPT.json`. Whole-proof and
source readings have separate dated events.

