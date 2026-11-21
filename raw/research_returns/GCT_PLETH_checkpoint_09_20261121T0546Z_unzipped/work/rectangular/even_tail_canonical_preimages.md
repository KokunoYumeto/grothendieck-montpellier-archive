# Explicit canonical preimages for every even tail

## R-037. A uniform actual nonvanishing family

Let \(a\ge2\), let \(\rho\ne\varnothing\) be a partition
with \(\ell(\rho)\le a-1\), and put
\(d=|\rho|\), \(q=\rho_1\). For every integer
\(n\ge d+q\), and every vector space with
\(\dim V\ge\ell(\rho)+1\), set

\[
\lambda=(an-2d,2\rho_1,2\rho_2,\ldots).
\tag{EP.1}
\]

Then

\[
\boxed{\operatorname{mult}_{\lambda}\operatorname{im}h_{n,a}\ge1.}
\tag{EP.2}
\]

The maps below construct both a nonzero highest image vector and
its explicit preimage. This is a nonvanishing assertion; no
equality with the whole target multiplicity is asserted. No
historical novelty claim is made.

## 1. The exact graded multiplication morphism

For a vector space \(V\), the product map

\[
m_a:V^a\longrightarrow\operatorname{Sym}^aV,
\qquad(v_1,\ldots,v_a)\longmapsto v_1\cdots v_a
\tag{EP.3}
\]

is polynomial and invariant under slot permutations. Pullback
of polynomial functions gives the actual algebra homomorphism

\[
\Phi_a=m_a^*:
\operatorname{Sym}(\operatorname{Sym}^aV^*)
\longrightarrow\mathbb Q[V^a]^{S_a}.
\tag{EP.4}
\]

Its homogeneous degree-\(n\) part lands in separate slot
degree \((n^a)\), identified with
\(\operatorname{Sym}^a\operatorname{Sym}^nV^*\).
It is exactly the normalized map \(h_{n,a}\): for an
evaluation tensor \(v_1^n\cdots v_a^n\), transpose the
grid, and normalized symmetrization gives
\((v_1\cdots v_a)^n\), with scalar one. This is the same
tensor calculation as (SR.5). In particular, for any two
homogeneous elements \(A,B\),

\[
h_{r+s,a}(AB)=h_{r,a}(A)\,h_{s,a}(B).
\tag{EP.5}
\]

The right multiplication is ordinary multiplication of the
polynomials on \(V^a\). Thus (EP.5) fixes the graded map,
the product, and all normalization factors.

## 2. Every normalized column preimage

For \(1\le j\le a-1\), use \(j+1\) auxiliary slots
\((x_i,y_{i1},\ldots,y_{ij})\), let \(D_{j+1}\) be
their full determinant, and set

\[
P_{a,j}=
\frac{(-1)^j a^{j+1}(a-1)^j}{(j+1)!}
\left(\prod_{i=1}^{j+1}x_i\right)^{a-2}D_{j+1}^{2}
\in\operatorname{Sym}^{j+1}\operatorname{Sym}^aV^*.
\tag{EP.6}
\]

The determinant-square expression is the literal generator
\(F_{j+1,a,j}\) of R-035, with only one maximal minor.
The exact scalar (SR.14), with \(a,n\) exchanged and
\(n=j+1\), gives

\[
\boxed{h_{j+1,a}(P_{a,j})=F_{a,j+1,j}.}
\tag{EP.7}
\]

Indeed the map's scalar is
\((-1)^j(j+1)!/[a^{j+1}(a-1)^j]\), whose reciprocal is
precisely the coefficient in (EP.6). The image is the nonzero
polynomial (SR.4) on the common \(a\) slots.
All determinants in (EP.6) and (EP.7) use the same initial
coordinate flag, so the displayed vectors are highest vectors
with compatible weights.

The top-row padding element is the degree-one polynomial
\(x^a\in\operatorname{Sym}^aV^*\). Its actual image is
\(u=\prod_{i=1}^a x_i\), directly by (EP.3).

## 3. The complete preimage and its highest weight

Let \(j_1,\ldots,j_q\) be the column heights of \(\rho\),
in their usual order. They satisfy

\[
1\le j_l\le a-1,\qquad
\sum_{l=1}^qj_l=d,\qquad
\sum_{l=1}^q(j_l+1)=d+q.
\tag{EP.8}
\]

Form the following actual product in the symmetric algebra
in (EP.4):

\[
\boxed{
P_{a,n,\rho}=(x^a)^{n-d-q}\prod_{l=1}^qP_{a,j_l}.}
\tag{EP.9}
\]

It has degree \(n\); its exponent is nonnegative in the
stated range. Equations (EP.5) and (EP.7) give its exact image

\[
\boxed{
h_{n,a}(P_{a,n,\rho})
=u^{n-d-q}\prod_{l=1}^qF_{a,j_l+1,j_l}.}
\tag{EP.10}
\]

Every factor on the right is a nonzero polynomial on the common
slot space. The coordinate polynomial ring is an integral
domain, so their product is nonzero. Each factor is highest
for the same unipotent subgroup, as is \(u\), so the product
is highest. Its first coordinate weight is
\[
a(n-d-q)+\sum_l\bigl(a(j_l+1)-2j_l\bigr)=an-2d.
\]
Its \(i\)-th tail coordinate is twice the number of columns
of \(\rho\) of height at least \(i\), which is exactly
\(2\rho_i\). Thus its weight is precisely (EP.1), proving
(EP.2) by the explicit preimage (EP.9).

The partition condition also holds throughout the range:
\[
an-2d\ge(a-2)d+aq\ge2q=2\rho_1.
\]
The coordinate construction uses \(\ell(\rho)+1\)
coordinates, so it is nonzero in every dimension at least that
number; Schur functors give the corresponding stable statement.
At \(\rho=\varnothing\), omitted from the main notation,
the actual pure-power preimage \((x^a)^n\) gives the top-row
component for every \(n\ge0\).

For example, putting \(\rho=(2^k,1^j)\) gives the explicit
four-column-tail family

\[
\boxed{
a\ge j+k+1,\quad k\ge1,\quad j\ge0,\quad
n\ge j+2k+2:\quad
\operatorname{mult}_{(an-4k-2j,4^k,2^j)}
\operatorname{im}h_{n,a}\ge1.}
\tag{EP.11}
\]

Its preimage is the product of the two column preimages
\(P_{a,j+k}P_{a,k}\), with the prescribed pure-power padding.
This conclusion retains the possible additional target
multiplicities; (EP.10) specifies the particular nonzero line
that is reached.

## Exact geometric and Grothendieck transport

The image algebra in (EP.4) is the coordinate pullback of the
specified product morphism (EP.3). Its highest vector and
preimage are actual polynomial functions, and (EP.5) is equality
under that pullback. Applying the frame-torsor functor of
SGA6 VI Theorem3.3 to these rational natural tensor maps gives
the associated-bundle maps over a \(\mathbb Q\)-scheme;
the exact projector and weight extraction locators are those
fully specified in R-036 §5. In exact representation \(K_0\),
multiplication is induced by the same tensor and symmetric
multiplication morphisms. The cote133/028 comparison is A012's
explicit tensor-word/Young-coset and Schur-filtered map, with
its rational idempotent splitting. These constructions preserve
the identities (EP.5), (EP.7) and (EP.10) on every local
trivialization and hence globally.
