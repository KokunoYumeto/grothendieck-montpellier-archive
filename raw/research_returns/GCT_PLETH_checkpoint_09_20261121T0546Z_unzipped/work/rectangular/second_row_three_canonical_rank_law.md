# The complete second-row-three canonical rank law

## R-036. Exact unit components and their actual cubic-minor scalar

Let \(a,n\ge2\). In the whole band \(\lambda\vdash an\),
\(\lambda_2\le3\), the only nonzero target multiplicities in
\(\operatorname{Sym}^a\operatorname{Sym}^nV\) are the following,
each with multiplicity one:

\[
\begin{array}{ll}
(an),&\\
(an-2j,2^j),&1\le j\le a-1,\\
(an-2j-3,3,2^j),&n\ge3,\quad0\le j\le a-3.
\end{array}
\tag{CT.1}
\]

As usual, summands longer than \(\dim V\) vanish. The first
component is reached by \(h_{n,a}\) with scalar one. The second
is reached exactly for \(j<n\), by R-035. The third has the
actual image multiplicity

\[
\boxed{
\operatorname{mult}_{(an-2j-3,3,2^j)}\operatorname{im}h_{n,a}
=\begin{cases}1,&j\le n-3,\\0,&j\ge n-2,
\end{cases}
\quad a,n\ge3,\quad0\le j\le a-3.}
\tag{CT.2}
\]

Consequently \(h_{n,a}\) is surjective on the entire second-row
band \(\lambda_2\le3\) for all \(n\ge a\ge2\). For
\(a,n\ge3\), its cokernel in that band is exactly

\[
\boxed{
\bigoplus_{j=n}^{a-1}S_{(an-2j,2^j)}V
\ \oplus\
\bigoplus_{j=n-2}^{a-3}S_{(an-2j-3,3,2^j)}V.}
\tag{CT.3}
\]

Every summand occurs once; a range with lower endpoint above its
upper endpoint is empty. At \(n=2\), the second sum is absent,
and the first sum is precisely R-035's cokernel. These assertions
come from the explicit morphisms proved below. No historical
novelty claim is made.

## 1. An exact invariant-algebra map excluding all other tails

Let \(E=\mathbb Q^a\), \(W=\mathfrak h_a\), and let
\(P:E\to W\) be the rational orthogonal projection (UT.7).
Take a three-dimensional auxiliary space \(T\). We claim the
following actual surjective graded algebra map:

\[
\operatorname{Sym}(\Lambda^2T)\otimes\Lambda(\Lambda^3T)
\twoheadrightarrow\bigl(\Lambda(W\otimes T)\bigr)^{S_a}.
\tag{CT.4}
\]

Here the degree-two generator sends \(t\wedge t'\) to
\(\sum_i(Pe_i\otimes t)\wedge(Pe_i\otimes t')\), and the
degree-three generator is the corresponding sum of three factors
in the same row. The first generators are even and the last is
odd, so these formulas define the displayed graded-commutative
algebra morphism. It is \(GL(T)\)-equivariant.

To prove surjectivity, first work in \(\Lambda(E\otimes T)\),
using a basis of three Grassmann letters per row. For a nonempty
subset \(S\subseteq\{1,2,3\}\), define the row power sum
\(p_S\) by summing the product of its letters over all rows.
For an ordered list \(S_1,\ldots,S_l\), let
\(A(S_1,\ldots,S_l)\) be the sum of their products over
injective assignments to rows, retaining the displayed factor
order. Every nonzero invariant monomial-orbit sum is a nonzero
rational multiple of one of these \(A\)'s. An orbit with two
identical odd row types has zero average, since swapping those
rows changes its sign. All other stabilizer factors are positive
factorials after fixing the displayed ordering.

Expand \(p_{S_1}\cdots p_{S_l}\) and group its row assignments
by their equality partition \(\pi\) of \(\{1,\ldots,l\}\).
The discrete partition contributes exactly \(A(S_1,\ldots,S_l)\).
Every other partition contributes a signed \(A\) with fewer
occupied rows: merge the subsets inside each block, use zero when
a Grassmann letter repeats, and use the literal exterior-product
sign when ordering the remaining letters and blocks. This is an
exact expansion, because equality partitions partition all row
assignments. Induction on \(l\) proves that the \(p_S\)'s
generate every invariant. Thus this argument supplies the algebra
maps and their spanning proof, including every finite row count.

The exterior map induced by \(P\) is an equivariant surjection.
Its restriction on invariants is onto: the equivariant inclusion
\(W\hookrightarrow E\) supplies a lift, or equivalently one
can apply the rational Reynolds projector. After projection,
the singleton sums vanish because \(\sum_iPe_i=0\).
The remaining sums are exactly the generators of (CT.4), proving
that assertion.

In dimension three,
\(\Lambda^2T\simeq(\det T)\otimes T^*\) by exterior
contraction. Therefore the domain of (CT.4) has precisely the
irreducible \(GL(T)\)-summands

\[
S_{(p,p,0)}T\quad\text{and}\quad S_{(p+1,p+1,1)}T,
\qquad p\ge0,
\tag{CT.5}
\]

each once. This follows from the actual determinant-contraction
map and the symmetric power of the standard dual representation.
The rational skew Cauchy Young projectors identify the target of
(CT.4) with

\[
\bigoplus_{\nu_1\le3}
(S_\nu W)^{S_a}\otimes S_{\nu^t}T.
\tag{CT.6}
\]

Thus every invariant here has multiplicity at most one, and the
only possible nonempty tails are \((2^j)\) and \((3,2^j)\).
This conclusion is a consequence of the explicit surjection and
the commuting Young decompositions. R-033 determines the first
family. For the second, length gives zero at \(j\ge a-1\).
At \(j=a-2\), \(\dim W=a-1=j+1\), and exterior-column
multiplication gives the actual isomorphism

\[
S_{(3,2^{a-2})}W\simeq(\det W)^2\otimes W.
\tag{CT.7}
\]

The determinant-square character is trivial on \(S_a\), while
\(W\) has no invariants. This proves zero also at this endpoint.
The following explicit polynomial proves nonvanishing for all
remaining \(j\).

## 2. The centered cubic-minor polynomial

Put \(s=j+1\), so \(a\ge s+2\). For \(a\) vectors
\(w_i\in\mathbb Q^s\), set

\[
\bar w=\frac1a\sum_iw_i,\quad z_i=w_i-\bar w,\quad
S=\sum_i z_i z_i^t,\qquad
f_a(w)=\sum_i(z_i)_1\,z_i^t\operatorname{adj}(S)z_i.
\tag{CT.8}
\]

This is slot-symmetric and translation invariant. Under
\(w_i\mapsto g w_i\), its vector-valued version transforms
by \((\det g)^2g\), because
\(\operatorname{adj}(gSg^t)=(\det g)^2g^{-t}\operatorname{adj}(S)g^{-1}\).
This identity follows first for invertible \(S\) and then as
a polynomial identity. The first component is consequently the
highest vector of weight \((3,2^{s-1})\) in its lower
coordinates. Equivalently, the raising operators
\(\sum_i(w_i)_p\partial_{(w_i)_q}\), \(p<q\), kill
this component, and its diagonal degrees are \(3,2,\ldots,2\).

We need its exact degree in each slot. Let \(R\) be the matrix
whose rows are \(r_i=(1,w_i^t)\). For a subset \(I\) of
size \(s+1\), write \(R_I\) for its square row minor. The
following polynomial identity provides that degree bound:

\[
\boxed{
H_a(w):=a^2f_a(w)=
\sum_{|I|=s+1}
\left((a-s-1)\sum_{i\in I}(w_i)_1
      -(s+1)\sum_{i\notin I}(w_i)_1\right)\det(R_I)^2.}
\tag{CT.9}
\]

For a direct verification, center the last \(s\) columns by
a determinant-one column matrix. It sends \(R^tR\) to
\(\operatorname{diag}(a,S)\). The adjugate congruence then
gives
\(r_i\operatorname{adj}(R^tR)r_i^t=\det S+a z_i^t\operatorname{adj}(S)z_i\).
Use the weighted Gram matrix
\(R^t\operatorname{diag}(t_1,\ldots,t_a)R\), differentiate
Cauchy–Binet with respect to \(t_i\), and set all \(t_l=1\).
This same adjugate expression equals
\(\sum_{I\ni i}\det(R_I)^2\), since exactly those minors
carry that row weight. Multiply by \((z_i)_1\), sum over
\(i\), and use \(\sum_i z_i=0\). The result is
\(a f_a=\sum_I(\sum_{i\in I}(z_i)_1)\det(R_I)^2\).
Substitute \(z_i=w_i-\bar w\) and multiply by \(a\)
to obtain (CT.9), with both coefficients as displayed.
The argument is polynomial and remains valid at singular Gram
matrices. Formula (CT.9) has degree at most three in each slot.

The polynomial is nonzero for every \(a\ge s+2\). Take
the centered vectors

\[
e_1,e_1,e_2,\ldots,e_s,
-2e_1-e_2-\cdots-e_s,
\quad\text{and }a-s-2\text{ zero vectors}.
\tag{CT.10}
\]

Put \(D=\operatorname{diag}(2,1,\ldots,1)\) and
\(v=(2,1,\ldots,1)^t\). Then \(S=D+vv^t\),
\(\det S=2(s+2)\), and
\(S^{-1}=D^{-1}-D^{-1}vv^tD^{-1}/(s+2)\), as verified
by multiplication. The adjugate quadratic values on \(e_1\),
on each other \(e_i\), and on \(v\) are respectively
\(s,2(s+1),2(s+1)\). Hence

\[
f_a=-2(s+2)\ne0.
\tag{CT.11}
\]

For \(n\ge3\), use slots \((x_i,y_i)\), put
\(u=\prod_i x_i\), and define the highest polynomial

\[
G_{a,n,s}=u^nH_a(y_1/x_1,\ldots,y_a/x_a).
\tag{CT.12}
\]

This expression is polynomial. Its fully polynomial formula,
with \(X_I\) the minor of rows \((x_i,y_i)\), is

\[
\begin{split}
G_{a,n,s}=u^{n-3}\sum_{|I|=s+1}
\left(\prod_{i\notin I}x_i\right)^2\det(X_I)^2
\biggl(& (a-s-1)\sum_{i\in I}(y_i)_1\prod_{l\ne i}x_l\\
&-(s+1)\sum_{i\notin I}(y_i)_1\prod_{l\ne i}x_l\biggr).
\end{split}
\tag{CT.13}
\]

Each slot has degree \(n\), and the weight is
\((an-2s-1,3,2^{s-1})\). The translations in (CT.8)
are exactly the raising substitutions from the first coordinate;
the other raising operators were checked above. Thus this is a
nonzero slot-symmetric highest polynomial. It proves the invariant
line for every \(j=s-1\le a-3\).

The ordinary Cauchy highest-column construction identifies
\(H_a\) with the indicated vector of \(S_{(3,2^{s-1})}W\).
In T-032 (C.11), scaling the first centered column by \(u\)
multiplies it by \(u^3\); multiplication by the chart's
\(u^{n-3}\) is therefore exactly (CT.12). This fixes its
actual flag-component map. T-032's stable chart now proves every multiplicity in
(CT.1) for \(n\ge3\): its balanced module is
\(S_{(\lambda_2,\ldots,\lambda_a)}W\), with the ordinary
permutation action, and (CT.4)–(CT.13) exhaust its invariant
lines. A partition with more than \(a\) rows has zero target,
by inclusion in \((\operatorname{Sym}^nV)^{\otimes a}\)
and successive Pieri.

## 3. The exact inner-degree-two endpoint

At \(n=2\), T-032 still embeds the balanced space in its
tail module, with inverse given by its explicit polynomial
extension criterion. The tail classification (CT.4) therefore
still excludes every other family. For a cubic tail the possible
invariant line would have chart polynomial \(u^{-1}G_{a,3,s}\).
It is not polynomial, as the following actual specialization
proves.

Set \(x_1=0\), \(y_1=e_1\), and set every other \(x_i=1\).
Among the other lower vectors use \(0,e_2,\ldots,e_s\),
with the remaining vectors zero. In (CT.13), a minor subset not
containing row one contributes zero because of its outside
\(x_1^2\). In a subset containing row one, only the linear
summand with \(i=1\) survives. Its coefficient is
\(a-s-1>0\). The surviving sum is a positive multiple of a
sum of real determinant squares, with at least one square
nonzero. Thus \(x_1\) does not divide \(G_{a,3,s}\),
so \(u\) does not divide it. The exact chart criterion proves
that this entire possible invariant line is absent at \(n=2\).
R-035 determines the remaining two-column tails and top row,
which proves (CT.1) also at this endpoint.

## 4. The complete normalized third-moment calculation

We now compute the actual canonical map on (CT.12). Take
\(a\ge s+2\), \(n\ge3\), and \(n\) vectors
\(\ell_k=(1,v_k)\). Set \(Q=\prod_k\ell_k\).
The scalar-one Chow pairing (SR.5) gives

\[
(h_{a,n}G_{a,n,s})(\ell_1,\ldots,\ell_n)
=\mathcal A_{G_{a,n,s}}(Q,\ldots,Q).
\tag{CT.14}
\]

The one-slot functional
\(L_Q(q)=\langle x^{n-3}q,Q\rangle\) on cubics is also
applied to a lower-coordinate polynomial of degree \(d\le3\)
by multiplying it by \(x^{3-d}\). It has
degree-\(d\) lower-coordinate tensor, for \(0\le d\le3\),

\[
\frac1{n(n-1)\cdots(n-d+1)}
\sum_{k_1,\ldots,k_d\text{ distinct}}
v_{k_1}\otimes\cdots\otimes v_{k_d}.
\tag{CT.15}
\]

The expression is symmetric. Its evaluation on coordinate
monomials follows from the exact multinomial pairing (SR.6);
in particular it includes all repeated coordinate factors.
Translation invariance of (CT.9) allows all \(v_k\) to be
replaced by \(v_k-\frac1n\sum_l v_l\). We therefore carry
out the calculation with \(\sum_kv_k=0\). Then the first
moment is zero and the next two moments are

\[
C_2=-\frac{S_2}{n(n-1)},\qquad
C_3=\frac{2S_3}{n(n-1)(n-2)},\qquad
S_2=\sum_kv_kv_k^t,\quad S_3=\sum_kv_k^{\otimes3}.
\tag{CT.16}
\]

The first identity subtracts the repeated indices from
\((\sum v_k)^{\otimes2}=0\). For the second, the three
patterns with exactly two equal indices each sum to \(-S_3\);
the all-equal pattern is \(S_3\). Subtracting them from
the zero full tensor gives the distinct-index sum \(2S_3\).
This proves every coefficient in (CT.16).

We compute the formal independent-slot evaluation of (CT.9)
with these moments. The outside linear terms have zero evaluation.
For one minor subset of size \(s+1\), the quadratic matrix
is \(B=\operatorname{diag}(1,C_2)\). Put
\(B_1=L_Q(w_1\,r r^t)\), with \(r=(1,w^t)\).
The lower block of \(B_1\) is the slice \((C_3)_{1pq}\),
and its upper left entry is zero. Differentiating the exact
two-permutation identity (SR.10) gives

\[
L_Q^{\otimes(s+1)}
\left(\sum_{i=1}^{s+1}(w_i)_1\det(R_I)^2\right)
=(s+1)!\operatorname{tr}(\operatorname{adj}(B)B_1)
=(s+1)!\sum_{p,q}(\operatorname{adj}C_2)_{pq}(C_3)_{1pq}.
\tag{CT.17}
\]

The differentiation merely chooses the one row with the extra
linear factor in each determinant-product monomial. The block
adjugate calculation is polynomial, so no nonsingularity
assumption on the moments is used. There are
\(\binom a{s+1}\) minor subsets, and their inside coefficient
is \(a-s-1\). Hence

\[
\mathcal A_{G_{a,n,s}}(Q,\ldots,Q)
=\frac{a!}{(a-s-2)!}
\sum_{p,q}(\operatorname{adj}C_2)_{pq}(C_3)_{1pq}.
\tag{CT.18}
\]

Adjugation has degree \(s-1\). Inserting (CT.16) converts
the last contraction into

\[
\frac{2(-1)^{s-1}}{n^s(n-1)^s(n-2)}
\sum_k(v_k)_1v_k^t\operatorname{adj}(S_2)v_k
=\frac{2(-1)^{s-1}}{n^s(n-1)^s(n-2)}f_n(v).
\tag{CT.19}
\]

By (CT.9), \(H_n=n^2f_n\), also when the minor sum is
identically zero. Combining the actual maps proves the exact
scalar identity

\[
\boxed{
h_{a,n}G_{a,n,s}
=\frac{2(-1)^{s-1}a!}
{(a-s-2)!\,n^{s+2}(n-1)^s(n-2)}\,G_{n,a,s}.}
\tag{CT.20}
\]

For \(n\le s+1\), define the right-hand generator by the
same formula (CT.13). It is identically zero: for \(n<s+1\)
the subset sum is empty, while at \(n=s+1\) its inside
coefficient and its outside sum both vanish. At \(n\ge s+2\),
(CT.10)–(CT.11) prove it is nonzero. The scalar in (CT.20)
is always nonzero in its stated domain.

The calculation allowed an arbitrary mean to be removed by the
literal translation symmetry, so it proves equality for all
vectors with first coordinate one. Homogeneity in the \(n\)
slots extends it to the dense open set of nonzero first
coordinates, and polynomiality extends it everywhere. Thus
(CT.20) is an identity of the actual canonical morphisms.

## 5. Rank, endpoints, and exact transport

The multiplicity line of the source in (CT.20) is unique by
(CT.1). The target generator is nonzero exactly when
\(n\ge s+2\). Transposing the normalized grid map preserves
rank on each multiplicity space, so (CT.20) proves (CT.2) with
\(j=s-1\). For \(n\le s+1\), (CT.4)–(CT.7) also
give zero multiplicity on the opposite side; the literal zero
in (CT.20) retains the exact map at that endpoint.

Together with the determinant-square scalar of R-035 and the
complete exclusions in (CT.4), this proves every term of
(CT.3) and full surjectivity in the stated \(n\ge a\) band.
At degree one the canonical map is the actual symmetric-power
identity, as in R-035. At \(a=2\), there are no cubic-tail
components; R-035 handles the full band. Thus no endpoint is
obtained by substituting into a zero denominator.

All constructions use rational tensor maps, Reynolds and Young
projectors, exterior multiplication, coefficient extraction and
polynomial identities. Their exact associated-bundle transport
is the frame-torsor construction recorded for R-033–R-035; the
weight extraction is the diagonal coaction projector and the
canonical maps are the same normalized tensor morphisms in
every trivialization. The finite checks are recorded separately
from this full parameter proof. No input-dependent numerical
rank assumption occurs in the argument.

The precise representation-to-bundle map is
\(M\mapsto\mathscr F(E)\times_{GL(V)}M\), where
\(\mathscr F(E)\) is the frame torsor of a finite locally
free module \(E\) on a \(\mathbb Q\)-scheme. The same
formula sends every equivariant arrow in this proof to its
associated-bundle arrow. The rational Young and Reynolds
idempotents give actual direct-summand subbundles; hence their
kernels, images and rank statements are the local constant
matrices proved above and glue on overlaps. On exact
Grothendieck groups this is the frame-torsor morphism in
**SGA 6, Exposé VI, Theorem 3.3**, with its stated category
of bounded-rank locally free modules on a commutatively ringed
topos. **SGA 6 V, Proposition 4.2 and Definition 4.4** give
the evaluation of the free \(\lambda\)-ring, and
**V, Proposition 4.8 and Corollary 4.9** give its finite-rank
quotient. These exact statements and the frame proof were read
in the saved French mathematical transcription; this does not
claim inspection of an original SGA scan.

The coaction and exact diagonal weight projectors are those of
**SGA 3 I, §4.5 and Propositions 4.7.2–4.7.3**. The
T-032 chart uses the literal localization at \(u\). In its
projective flag presentation, the affine degree-zero localization
charts are **EGA II 2.4.1–2.4.2, p.28**; its graded-module
sheafification and exactness are **II 2.5.2 and 2.5.4, p.31**.
These EGA/SGA3 locators and their scope were independently checked
by the archive agent and are recorded in its source notes.
For the supplied archive **cote 133/028**, the actual map from
tensor words to Young cosets, followed by the torus-weight
extraction and Schur filtration, is the complete integral
construction A-012 (A12.2)–(A12.4). Applying its rational
projector splittings gives precisely the tensor/Schur classes
used here. This specifies the archive and Grothendieck transport
through actual morphisms.

## 6. Executed independent finite checks

The script `verify_second_row_three_rank_law.py` expands the
product of the input linear forms and both determinant permutation
sums, and pairs every monomial using its exact multinomial
denominator. Its 40 cases cover \(3\le a,n\le6\) and every
\(1\le s\le a-2\). The first coordinates are nonunit integers.
Every literal pairing agrees with (CT.20), including the sampled
zero endpoints \(n\le s+1\), and every asserted nonzero case
is nonzero. This calculation does not call the moment formulas
or a canonical-rank routine. The complete receipt is
`SECOND_ROW_THREE_CANONICAL_SCALAR_CHECK.tsv`.

The same script independently expands the plethysms in power sums
and uses the Murnaghan–Nakayama rule for all valid second-row-at-most-
three shapes at \(2\le a\le6,\ 2\le n\le4\). All 340
target coefficients and all 340 source coefficients agree with
the unit/zero classification, including the inner-degree-two
extension endpoint. The receipt is
`SECOND_ROW_THREE_BAND_MN_CHECK.tsv`. These finite comparisons
are checks of the full proof, and the actual canonical ranks
are established by the literal scalar identity (CT.20).
