# The complete second-row-two canonical rank law

## R-035. An exact determinant-square scalar

Work in characteristic zero. All canonical grid maps use normalized
tensor symmetrization, so the transpose identity is the scalar-one
identity of R-031 (OF.6). Let \(a,n\ge2\), \(1\le j\le a-1\),
and put \(\lambda_j=(an-2j,2^j)\). The exact target and image
multiplicities are

\[
\boxed{
a_{a,n}^{\lambda_j}=1,\qquad
\operatorname{mult}_{\lambda_j}\operatorname{im}h_{n,a}
=\begin{cases}1,&j<n,\\0,&j\ge n.\end{cases}}
\tag{SR.1}
\]

The first assertion is R-033. Below we prove the second by an
explicit nonzero scalar for the actual map, and prove that these
are all the nonzero components with second row two. In particular,

\[
\boxed{
a\ge2,\quad n\ge a:\quad h_{n,a}\text{ reaches the entire
target second-row band }\lambda_2\le2.}
\tag{SR.2}
\]

For \(2\le n<a\), the cokernel in this band is exactly

\[
\boxed{
\bigoplus_{j=n}^{a-1} S_{(an-2j,2^j)}V,}
\tag{SR.3}
\]

each summand once. All statements include the natural convention
that an overly long Schur functor vanishes in the given dimension.
Thus (SR.2) holds in every dimension. The missing summands in
(SR.3) are present whenever their lengths fit. No historical
novelty claim is made.

## 1. The actual invariant polynomial and normalized Chow evaluation

Use \(a\) vector slots with first \(j+1\) coordinates
\((x_i,y_{i1},\ldots,y_{ij})\). Write \(u=\prod_{i=1}^a x_i\),
and let \(X_I\) be the \((j+1)\times(j+1)\) matrix in the
slots \(I\), with these columns in that order. Define

\[
F_{a,n,j}
=u^{n-2}\sum_{\substack{I\subseteq\{1,\ldots,a\}\\|I|=j+1}}
 \left(\prod_{i\notin I}x_i\right)^2\det(X_I)^2.
\tag{SR.4}
\]

Every slot has degree \(n\). The polynomial is slot-symmetric,
because determinants are squared. Its coordinate weight is
\((an-2j,2^j)\): the lower \(j\) coordinates each have
degree two and total degree is \(an\). The initial-column
determinants and first coordinates are fixed by the relevant
highest-weight unipotent group, so this is a highest polynomial.
It is nonzero: take all \(x_i=1\), and take the lower
coordinate vectors in the slots to include \(0,e_1,\ldots,e_j\),
with all remaining lower vectors zero. At least one determinant
in (SR.4) is nonzero, and the sum of real squares is positive.
Thus (SR.4) spans the highest multiplicity line proved in R-033.

Let \(\mathcal A_F\) be the symmetric \(a\)-linear form on
\(\operatorname{Sym}^nV\) determined by
\(\mathcal A_F(v_1^n,\ldots,v_a^n)=F(v_1,\ldots,v_a)\).
For \(n\) vectors \(\ell_1,\ldots,\ell_n\), set
\(Q=\ell_1\cdots\ell_n\). The normalized canonical map
satisfies exactly

\[
(h_{a,n}F)(\ell_1,\ldots,\ell_n)
=\mathcal A_F(Q,\ldots,Q).
\tag{SR.5}
\]

To verify the normalization, represent the evaluation tensor as
the normalized symmetric product of
\(\ell_1^a,\ldots,\ell_n^a\). After transposing the grid,
every one of its \(a\) rows contains
\(\ell_1,\ldots,\ell_n\). Normalized inner symmetrization
turns each row into \(Q\), and all rows are identical, so the
outer symmetrization leaves \(Q^a\). Thus the opposite grid
map sends this evaluation tensor exactly to \(Q^a\).
The perfect normalized tensor pairing and its scalar-one adjoint
identity give (SR.5), without any additional factorial.

For a monomial in one slot, the corresponding pairing is

\[
\left\langle x^{n-|\beta|}y^\beta,
e_0^{n-|\beta|}e^\beta\right\rangle
=\frac{(n-|\beta|)!\prod_p\beta_p!}{n!}.
\tag{SR.6}
\]

This follows by counting the permutations matching the letters
in normalized symmetric tensors. We retain this normalization
in the next calculation.

## 2. Evaluation by the exact quadratic pairing matrix

First take \(\ell_k=(1,v_k)\), \(v_k\in\mathbb Q^j\),
and write

\[
s=\sum_{k=1}^n v_k,\qquad
T=\sum_{k=1}^n v_kv_k^t,\qquad
\mu=\frac{s}{n},\qquad
M=\frac{ss^t-T}{n(n-1)}.
\tag{SR.7}
\]

Define the linear functional on quadratics
\(L_Q(q)=\langle x^{n-2}q,Q\rangle\). Expanding
\(Q=\prod_k(e_0+\sum_p(v_k)_pe_p)\) and using (SR.6)
gives exactly

\[
L_Q(x^2)=1,\qquad L_Q(xy_p)=\mu_p,\qquad
L_Q(y_py_q)=M_{pq}.
\tag{SR.8}
\]

For \(p\ne q\), the numerator of the last expression is
\(\sum_{k\ne l}(v_k)_p(v_l)_q\) and its normalization is
\(1/(n(n-1))\). For \(p=q\), the polynomial coefficient
sums over \(k<l\), and the pairing factor is
\(2/(n(n-1))\), giving the identical matrix formula. Thus
both repeated and distinct coordinate indices are accounted for.
The matrix of this quadratic functional is

\[
B=\begin{pmatrix}1&\mu^t\\\mu&M\end{pmatrix},\qquad
\det B=\det(M-\mu\mu^t).
\tag{SR.9}
\]

For one subset \(I\) in (SR.4), expand the determinant
square into its two permutation sums. Applying the independent
slot functionals \(L_Q\) gives

\[
\sum_{\sigma,\tau\in S_{j+1}}
 \operatorname{sgn}(\sigma)\operatorname{sgn}(\tau)
 \prod_{i=1}^{j+1}B_{\sigma(i),\tau(i)}
=(j+1)!\det B.
\tag{SR.10}
\]

For each fixed \(\sigma\), reindexing the product converts
the sum over \(\tau\) into the determinant of \(B\).
Every outside slot in (SR.4) contributes \(L_Q(x^2)=1\).
There are \(\binom a{j+1}\) subsets. Consequently

\[
\mathcal A_{F_{a,n,j}}(Q,\ldots,Q)
=\frac{a!}{(a-j-1)!}\det(M-\mu\mu^t).
\tag{SR.11}
\]

No probabilistic interpretation is needed: (SR.8)–(SR.11)
are identities of rational polynomial functionals on the stated
tensor powers.

The exact matrix simplification is

\[
M-\mu\mu^t
=-\frac1{n(n-1)}\left(T-\frac{ss^t}{n}\right).
\tag{SR.12}
\]

It follows by putting the coefficients of \(ss^t\) over the
denominator \(n^2(n-1)\): their difference is \(1\).
The coefficient of \(T\) is \(-1/(n(n-1))\).
This verifies both the sign and the complete denominator.

## 3. The exact canonical-map scalar

For the \(n\) rows \((1,v_k)\), let \(Z\) denote their
\(n\times(j+1)\) matrix. Cauchy–Binet and its block Gram
matrix give

\[
\begin{aligned}
F_{n,a,j}(\ell_1,\ldots,\ell_n)
&=\sum_{|I|=j+1}\det(Z_I)^2
=\det(Z^tZ)\\
&=\det\begin{pmatrix}n&s^t\\s&T\end{pmatrix}
=n\det\left(T-\frac{ss^t}{n}\right).
\end{aligned}
\tag{SR.13}
\]

For \(j+1>n\), the sum is empty and the Gram determinant
is zero, so the same identity holds with both sides zero.
For \(j+1\le n\), this is exactly the polynomial (SR.4)
with \(a,n\) exchanged, evaluated at first coordinates one.
Combining (SR.5), (SR.11), (SR.12) and (SR.13) proves

\[
\boxed{
h_{a,n}F_{a,n,j}
=(-1)^j\frac{a!}{(a-j-1)!\,n^{j+1}(n-1)^j}
 F_{n,a,j}.}
\tag{SR.14}
\]

Here \(F_{n,a,j}=0\) for \(j\ge n\). The calculation
was on first coordinates one. Every vector with nonzero first
coordinate is a scalar multiple of such a vector. Both sides
have degree \(a\) in each of their \(n\) slots, so homogeneity
proves equality on the dense open set with all first coordinates
nonzero. Both sides are polynomials, proving (SR.14) everywhere.
Thus the equality is an actual morphism identity, including its
normalization, rather than a comparison of multiplicities.

For \(j<n\), the right-hand polynomial is nonzero, by the
same explicit specialization used after (SR.4). One numerical
specialization making the scalar visible takes
\(v_1=e_1,\ldots,v_j=e_j\) and all remaining \(v_k=0\).
Then \(T-ss^t/n=I-\mathbf1\mathbf1^t/n\), whose determinant
is \((n-j)/n\), by its eigenspaces \(\mathbf1\) and
\(\mathbf1^\perp\). Equation (SR.11) becomes the nonzero
rational number

\[
(-1)^j\frac{a!}{(a-j-1)!}
\frac{n-j}{n^{j+1}(n-1)^j}.
\tag{SR.15}
\]

For \(j\ge n\), the target of \(h_{a,n}\) has at most
\(n\) rows, by its inclusion in
\((\operatorname{Sym}^aV)^{\otimes n}\) and successive
Pieri. Thus its entire \(\lambda_j\)-component is zero,
also verified literally in (SR.14). Scalar-one transposition
preserves the rank on each highest multiplicity space. Since
R-033 proves that the target line of \(h_{n,a}\) has
multiplicity one, this proves the full rank assertion (SR.1).

## 4. The full second-row band, including all one-box tails

Let \(\lambda\vdash an\), \(\lambda_2\le2\), and
\(\ell(\lambda)\le a\). The exact stable flag chart applies
because \(n\ge2\). Write its tail as
\(\nu=(2^j,1^k)\), where \(j+k\le a-1\). The chart
and its ordinary permutation action give the actual equality

\[
a_{a,n}^{\lambda}=\dim(S_\nu\mathfrak h_a)^{S_a}.
\tag{SR.16}
\]

For \(k>0\), put \(p=j+k\), \(q=j\). The weight
\((p,q)\) version of the same skew Cauchy construction used
in (UT.4) gives the actual Young-component embedding

\[
S_{(2^j,1^k)}\mathfrak h_a
\hookrightarrow\Lambda^{j+k}\mathfrak h_a
                    \otimes\Lambda^j\mathfrak h_a.
\tag{SR.17}
\]

Indeed the skew Cauchy summand with two-dimensional factor
\(S_{(j+k,j)}\mathbb Q^2\) has the required weight line
\((p,q)\); the other factor is its transposed shape
\((2^j,1^k)\). The inclusion is obtained by the same
column-antisymmetrized rational Young projector, so it is
\(S_a\)-equivariant. By (UT.8) and its explicit invariant
self-dualities, the right-hand invariant space is
\(\operatorname{Hom}_{S_a}([a-j-k,1^{j+k}],[a-j,1^j])\).
These are distinct irreducible hooks, including \(j=0\).
The homomorphism space is zero. The injective map (SR.17)
therefore proves zero invariants in (SR.16).

For \(k=0,j>0\), (UT.11) gives one invariant. For
\(j=k=0\), the tail is empty and the top-row component is
one-dimensional in multiplicity; the canonical map sends its
pure-power generator to itself with scalar one. Finally,
\(\ell(\lambda)>a\) gives zero target by the same
successive-Pieri bound. These exhaust every partition in the
stated second-row band. Together with (SR.1), they prove
(SR.2) and (SR.3).

The case \(n=1\), excluded only to keep the denominators in
(SR.7) uniform, is the actual identity
\(\operatorname{Sym}^aV\to\operatorname{Sym}^aV\).
The case \(a=1\) is the corresponding identity. Thus all
degree-one endpoints are also determined explicitly.

## Scope and exact transport

The normalized grid/pairing identities are R-031 (OF.6), the
unit multiplicity and hook maps are R-033, and the flag map is
T-032 with its explicit substitution and dense inverse. Every
operator, invariant, pairing scalar and polynomial identity in
(SR.4)–(SR.17) is over \(\mathbb Q\). Base change therefore
gives the same maps and ranks in characteristic zero. For an
associated vector bundle, applying its principal \(GL\)-bundle
functor to these natural tensor maps gives the corresponding
bundle maps; all displayed identities hold in each local
trivialization and hence glue. No identification of a canonical
image with an auxiliary product ideal is used in this proof.
