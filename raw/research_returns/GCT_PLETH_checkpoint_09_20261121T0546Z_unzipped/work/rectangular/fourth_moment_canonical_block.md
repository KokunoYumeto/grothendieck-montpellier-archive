# An exact rank-two fourth-moment canonical block

## R-038. An explicit matrix refinement of the known two-row isomorphism

The whole two-row canonical rank theorem is already G-006 in
`work/root/degree_three_report.md`: Landsberg, *Geometric
Complexity Theory: an introduction for geometers*,
[arXiv:1305.7387v3](https://arxiv.org/pdf/1305.7387),
Theorem 7.21, §7.7, printed p.24, states the isomorphism of the
actual map for binary forms. His §7.2, printed pp.19–20,
defines the tensor regrouping, Exercise 7.4 fixes its scalar,
and Proposition 7.6 proves its ideal-kernel description.
Proposition 7.11, printed p.22, identifies the multiplication
pullback with that same normalized map. The additional result
here is the explicit matrix, determinant, inverse, and endpoint
extension line on the particular component below. Its rank
statement specializes the established theorem.

Let \(a,n\ge2\), \(an\ge8\), and \(\dim V\ge2\).
Set \(\lambda=(an-4,4)\). The actual canonical map
\(h_{n,a}:\operatorname{Sym}^n\operatorname{Sym}^aV
\to\operatorname{Sym}^a\operatorname{Sym}^nV\) reaches its
whole target \(\lambda\)-component. Its exact target and
image multiplicities are

\[
\boxed{
\operatorname{mult}_{\lambda}\operatorname{im}h_{n,a}
=a_{a,n}^{\lambda}
=\begin{cases}
2,&a,n\ge4,\\
1,&\min(a,n)\le3,\quad\max(a,n)\ge4,\\
0,&a=n=3.
\end{cases}}
\tag{FM.1}
\]

The proof gives the actual two-by-two canonical matrix, its
nonzero determinant, its inverse, and the exact extension line
at inner degree two or three. No comparison of multiplicities
is used in place of the rank calculation, and no historical
novelty claim is made.

## 1. The invariant basis and the exact small-degree extension

For \(a\) lower-coordinate variables \(w_i\), put
\(\bar w=a^{-1}\sum_iw_i\), \(z_i=w_i-\bar w\), and

\[
P_a=\sum_i z_i^4,\qquad
K_a=\left(\sum_i z_i^2\right)^2,\qquad
T_a=a^2-3a+3.
\tag{FM.2}
\]

They are symmetric and translation invariant. The degree-four
invariants of the sum-zero representation \(\mathfrak h_a\)
are spanned by \(P_a,K_a\). To check the spanning claim by
actual polynomials, expand products of power sums according to
the equality partitions of their indices. The discrete equality
partition gives the corresponding monomial-orbit sum with a
nonzero factorial coefficient; all other terms use fewer distinct
indices. This triangular expansion expresses every symmetric
degree-four polynomial in
\(p_4,p_3p_1,p_2^2,p_2p_1^2,p_1^4\).
Restriction to \(p_1=0\) leaves precisely \(p_4,p_2^2\).
The rational Reynolds projector makes restriction onto the
invariant quotient surjective, so this proves the asserted
spanning map on \(\mathfrak h_a\).

For \(a\ge4\), the centered specializations
\((1,-1,0,\ldots)\) and \((1,1,-1,-1,0,\ldots)\)
give pairs \((P_a,K_a)=(2,4)\) and \((4,16)\), whose
determinant is nonzero. Thus the two generators are independent.
For \(a=2,3\), the exact fourth elementary-symmetric identity

\[
24e_4=p_1^4-6p_1^2p_2+3p_2^2+8p_1p_3-6p_4
\tag{FM.3}
\]

has \(e_4=p_1=0\), giving \(K_a=2P_a\). The generator
is nonzero, so the invariant dimension is one.

For slots \((x_i,y_i)\) and \(u=\prod_i x_i\), use
the separate homogenizations

\[
\widehat P_{a,n}=u^nP_a(y_i/x_i),\qquad
\widehat K_{a,n}=u^nK_a(y_i/x_i).
\tag{FM.4}
\]

For \(n\ge4\), these are nonzero polynomials of degree
\(n\) in each slot, and highest coordinate weight
\((an-4,4)\). Their translation invariance is exactly the
raising equation from the first coordinate. T-032 identifies
them with the actual balanced invariant basis: its first
centered column is scaled by \(u\), so a tail degree-four
polynomial acquires \(u^4\); its factor \(u^{n-4}\)
gives (FM.4). This proves the target multiplicities just stated
whenever \(n\ge4\).

We determine the exact polynomial-extension subspace for
\(n=2,3\). The coefficients of \(w_i^4\) in (FM.2) are

\[
[w_i^4]P_a=\frac{(a-1)T_a}{a^3},\qquad
[w_i^4]K_a=\frac{(a-1)^2}{a^2}.
\tag{FM.5}
\]

Thus for \(a\ge4\) their unique nonzero linear combination
with this coefficient zero is

\[
J_a=a(a-1)P_a-T_aK_a.
\tag{FM.6}
\]

It in fact has degree at most two in every variable. For any
symmetric, translation-invariant quartic let \(A\) be its
coefficient of \(w_i^4\), and \(B\) its coefficient of
\(w_i^3w_l\) for \(i\ne l\). The coefficient of
\(w_i^3\) in its zero derivative \(\sum_l\partial_{w_l}\)
is \(4A+(a-1)B\). Hence \(A=0\) forces \(B=0\).
These are exactly all monomials with a variable exponent above
two. Consequently

\[
\widehat J_{a,n}=u^nJ_a(y_i/x_i)
\quad\text{is a nonzero polynomial for all }a\ge4,n\ge2.
\tag{FM.7}
\]

Separate homogenization is polynomial precisely when every
variable exponent of the dehomogenized polynomial is at most
\(n\); its inverse is evaluation at all \(x_i=1\).
This is exactly T-032's extension map in these coordinates.
For \(n=2,3\), (FM.5) therefore forces the line (FM.6),
and the degree bound just proved makes the whole line extend.
Its multiplicity is one. At \(a=3,n=3\), there is only the
single invariant \(P_3\), whose coefficient (FM.5) is
nonzero, so it fails extension and the target multiplicity is
zero. The other pairs with \(a,n\le3\) do not satisfy
\(an\ge8\). This proves every target count in (FM.1),
with its actual polynomial maps.

## 2. Four exact formal sample identities

Use a one-variable formal linear functional with moments
\(1,0,\mu_2,\mu_3,\mu_4\), and apply it independently
in \(a\) variables. Write \(S_l=\sum_i w_i^l\).
Direct expansion gives

\[
\begin{aligned}
P_a&=S_4-\frac4aS_1S_3+\frac6{a^2}S_1^2S_2
                    -\frac3{a^3}S_1^4,\\
K_a&=S_2^2-\frac2aS_1^2S_2+\frac1{a^2}S_1^4.
\end{aligned}
\tag{FM.8}
\]

Grouping the monomials by their equality patterns gives

\[
\begin{array}{c|c}
\text{Polynomial}&\text{Independent-slot evaluation}\\ \hline
S_4\text{ or }S_1S_3&a\mu_4\\
S_1^2S_2\text{ or }S_2^2&a\mu_4+a(a-1)\mu_2^2\\
S_1^4&a\mu_4+3a(a-1)\mu_2^2.
\end{array}
\tag{FM.9}
\]

Every term involving a singleton index vanishes because the first
moment is zero. For \(S_1^4\), the three two-pair partitions
give the factor three; for the middle row only its indicated
pair pattern survives. These exhaust all index patterns and
prove the table directly.

Substitution into (FM.8) gives

\[
L^{\otimes a}(P_a)=C_4\mu_4+C_{22}\mu_2^2,\qquad
L^{\otimes a}(K_a)=D_4\mu_4+D_{22}\mu_2^2,
\tag{FM.10}
\]

with the exact coefficients

\[
\begin{aligned}
C_4&=\frac{(a-1)(a^2-3a+3)}{a^2},&
C_{22}&=\frac{3(a-1)(2a-3)}{a^2},\\
D_4&=\frac{(a-1)^2}{a},&
D_{22}&=\frac{(a-1)(a^2-2a+3)}a.
\end{aligned}
\tag{FM.11}
\]

This is a polynomial-functional computation, so it imposes no
positivity assumption on its formal moments.

## 3. The literal two-by-two canonical matrix

Let \(n\ge4\), take linear factors \(\ell_k=(1,v_k)\),
and set \(Q=\prod_k\ell_k\). The normalized tensor pairing
(SR.6) says that the moment of order \(d\le4\) is the
average over ordered distinct indices, divided by
\(n(n-1)\cdots(n-d+1)\). Translation invariance permits
the replacement of all \(v_k\) by their centered values.
For \(\sum_kv_k=0\), put \(P_n=\sum_kv_k^4\),
\(K_n=(\sum_kv_k^2)^2\), and abbreviate

\[
N_2=n(n-1),\qquad N_4=n(n-1)(n-2)(n-3).
\]

The exact split-form moments are

\[
\mu_2^2=\frac{K_n}{N_2^2},\qquad
\mu_4=\frac{3K_n-6P_n}{N_4}.
\tag{FM.12}
\]

The second numerator is (FM.3) at \(p_1=0\):
\(24e_4=3p_2^2-6p_4\) is precisely the ordered-distinct
four-index sum. This proves the normalization including the
factor \(4!\).

The exact Chow evaluation (SR.5), followed by (FM.10)–(FM.12),
therefore gives the following matrix for \(h_{a,n}\), with
columns the source basis
\((\widehat P_{a,n},\widehat K_{a,n})\) and rows the
target basis \((\widehat P_{n,a},\widehat K_{n,a})\):

\[
\boxed{
M_{a,n}=\begin{pmatrix}
-6C_4/N_4&-6D_4/N_4\\
3C_4/N_4+C_{22}/N_2^2&3D_4/N_4+D_{22}/N_2^2
\end{pmatrix}.}
\tag{FM.13}
\]

For the basis assertion here take \(a,n\ge4\). The
polynomial identities continue to hold at \(a=2,3\), where
the source generators satisfy \(K_a=2P_a\).
As in R-035, equality on first coordinates one extends by
separate homogeneity to their dense nonzero open set and then
to a polynomial identity everywhere. Thus (FM.13) computes the
specified canonical morphism with its actual normalization.

The complete determinant computation is

\[
C_4D_{22}-D_4C_{22}
=\frac{(a-1)^2(a-2)(a-3)}a,
\tag{FM.14}
\]

because its remaining numerator simplifies as
\[
(a^2-3a+3)(a^2-2a+3)-3(a-1)(2a-3)
=a^2(a-2)(a-3).
\]
Consequently

\[
\boxed{
\det M_{a,n}
=-\frac{6(a-1)^2(a-2)(a-3)}
{a\,n^3(n-1)^3(n-2)(n-3)}\ne0
\qquad(a,n\ge4).}
\tag{FM.15}
\]

Both copies are reached. In particular, to give a preimage for
either target basis vector under \(h_{n,a}\), take its
coordinate column, multiply by
\(M_{n,a}^{-1}=\operatorname{adj}(M_{n,a})/\det M_{n,a}\),
and use those two rational coefficients on the source basis
\((\widehat P_{n,a},\widehat K_{n,a})\). Every matrix
entry and scalar in this preimage is explicit in (FM.11)–(FM.15).

## 4. Actual inner-degree-two and inner-degree-three maps

For \(a\ge4\), combine (FM.6) and (FM.10). The
\(\mu_4\) coefficient cancels identically, while the other
coefficient is

\[
a(a-1)C_{22}-T_aD_{22}
=-a(a-1)(a-2)(a-3).
\tag{FM.16}
\]

This follows from the same explicitly factored numerator in
(FM.14). Since \(J_a\) has degree at most two in each
variable, its independent-slot evaluation depends only on the
first two moments. Any arbitrary extension of those moments
to degrees three and four produces the same value; (FM.16)
has no dependence on that extension. It therefore applies
literally to the split form with \(n=2\) or \(n=3\).
The normalized second moment gives the actual identity

\[
\boxed{
h_{a,n}\widehat J_{a,n}
=-\frac{a(a-1)(a-2)(a-3)}{n^2(n-1)^2}
\widehat K_{n,a},
\qquad a\ge4,\quad n=2,3.}
\tag{FM.17}
\]

The target generator is nonzero and the scalar is nonzero.
Each relevant source and target multiplicity is one by §1.
Scalar-one transposition gives the same rank for the map with
\(a,n\) reversed, so all pairs in the second line of
(FM.1) have their asserted rank. The remaining pair \(a=n=3\)
has zero target by the exact extension calculation. This proves
(FM.1) in full, without substituting into the zero denominators
excluded from (FM.12)–(FM.15).

## 5. Scope, transport, and executed checks

All these polynomials are highest vectors for a two-row Schur
functor. The natural Cauchy/Young embeddings put the same
multiplicity spaces into every dimension at least two, and the
canonical map commutes with those embeddings. Thus the computed
matrices give the stated stable Schur multiplicities and the
actual ranks in every declared dimension. The rational frame,
coaction, weight, exact \(K_0\), and cote133/028 morphisms
are precisely those specified with exact SGA/EGA locators in
R-036 §5; applying them to (FM.13) and (FM.17) transports the
actual matrices and their inverse maps to the associated bundles.

The independent script `verify_fourth_moment_block.py` expands
the centered quartics in their literal slot variables, expands
the product linear form, and pairs monomials with exact
multinomial denominators. It checks both generators on two
independent centered specializations for every \(2\le a\le8\),
\(4\le n\le8\), with nonunit first coordinates. It also
checks \(J_a\)'s actual per-variable degree bound and every
\(4\le a\le8,n=2,3\) endpoint on those specializations.
All 160 literal pairings agree with the stated map. The receipt
is `FOURTH_MOMENT_CANONICAL_CHECK.tsv`.

Separately, binary monomial weights count partitions of four and
three inside the \(a\)-by-\(n\) rectangle; their difference
is the two-row multiplicity. The eight partitions involved
are enumerated directly. All 46 valid pairs \(2\le a,n\le8\),
\(an\ge8\) give the target dimensions in (FM.1).
This independent receipt is `FOURTH_MOMENT_BINARY_WEIGHT_CHECK.tsv`.
The ranks are established by the full matrix proof above.
