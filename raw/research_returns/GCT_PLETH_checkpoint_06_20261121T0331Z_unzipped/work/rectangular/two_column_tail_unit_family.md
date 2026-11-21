# A unit-multiplicity family with an explicit invariant and canonical image

## R-033. The full two-column tail family

For every pair of integers \(a\ge2,n\ge2\) and every
\(1\le j\le a-1\), put

\[
\lambda=(an-2j,2^j).
\]

It is a partition: \(an-2j\ge2a-2j\ge2\). Its exact
symmetric plethysm multiplicity is

\[
\boxed{a_{a,n}^{(an-2j,2^j)}=1.}
\tag{UT.1}
\]

The proof below gives its actual invariant tensor, its exact
balanced flag morphism, and the exterior-power map determining
the invariant line. It also proves the following actual canonical
image families for
\(h_{n,a}:\operatorname{Sym}^n\operatorname{Sym}^aV
\to\operatorname{Sym}^a\operatorname{Sym}^nV\):

\[
\boxed{
\begin{array}{ll}
a\ge2,\quad n\ge2(a-1),\quad1\le j\le a-1,&
\operatorname{mult}_{\lambda}\operatorname{im}h_{n,a}=1,\\
a\ge6,\quad n\ge2a-5,\quad1\le j\le a-1,&
\operatorname{mult}_{\lambda}\operatorname{im}h_{n,a}=1.
\end{array}}
\tag{UT.2}
\]

All multiplicities are taken in dimension at least \(j+1\).
In a smaller dimension the Schur functor is zero. No historical
novelty claim is made for (UT.1) or for the literature inequality
used below.

## 1. An exact exterior transfer sequence

For any characteristic-zero vector space \(W\), define

\[
\begin{aligned}
D_j:\Lambda^jW\otimes\Lambda^jW
&\longrightarrow\Lambda^{j+1}W\otimes\Lambda^{j-1}W,\\
D_j((u_1\wedge\cdots\wedge u_j)\otimes
      (v_1\wedge\cdots\wedge v_j))
&=\sum_{\ell=1}^j(-1)^{\ell-1}
 (u_1\wedge\cdots\wedge u_j\wedge v_\ell)
 \otimes(v_1\wedge\cdots\widehat v_\ell\cdots\wedge v_j).
\end{aligned}
\tag{UT.3}
\]

Both alternating multilinear expressions show that this is
well-defined and natural in \(W\). Embed these two spaces as
the weights \((j,j)\) and \((j+1,j-1)\) in
\(\Lambda^{2j}(W\otimes\mathbb Q^2)\), writing all first-copy
factors before all second-copy factors. The Lie operator
\(E_{12}\) replaces one second-copy vector by its first-copy
vector. Moving the replaced vector past its \(\ell-1\)
preceding second-copy vectors gives exactly (UT.3), including
its sign and scalar.

The commuting Young projectors give the skew Cauchy decomposition

\[
\Lambda^{2j}(W\otimes\mathbb Q^2)
=\bigoplus_{k=0}^j
 S_{(2^k,1^{2j-2k})}W\otimes S_{(2j-k,k)}\mathbb Q^2.
\tag{UT.4}
\]

Terms with too many rows in \(W\) vanish. In its two-dimensional
factor write
\(S_{(2j-k,k)}\mathbb Q^2=\det^k\operatorname{Sym}^{2j-2k}\mathbb Q^2\).
The source line has vector
\(\det^k e_1^{j-k}e_2^{j-k}\), and its image is

\[
(j-k)\det^k e_1^{j-k+1}e_2^{j-k-1}.
\tag{UT.5}
\]

Every target line has \(k<j\), so the map is onto each
target summand. Exactly \(k=j\) is killed. Consequently
the actual maps form the short exact sequence

\[
0\longrightarrow S_{(2^j)}W
\longrightarrow\Lambda^jW\otimes\Lambda^jW
\xrightarrow{D_j}\Lambda^{j+1}W\otimes\Lambda^{j-1}W
\longrightarrow0.
\tag{UT.6}
\]

The first map is its column-antisymmetrized Young component
in the tensor space, with the usual rational Young projector.
Equations (UT.4)–(UT.5) identify its image with the literal
kernel, and fix the second map without a dimension-only
identification.

## 2. The invariant line for the standard permutation representation

Let \(E=\mathbb Q^a\), with its permutation basis \(e_i\),
let \(\mathbf1=\sum_i e_i\), and let

\[
W=\mathfrak h_a=\{(z_1,\ldots,z_a):\textstyle\sum_i z_i=0\},
\qquad P(e_i)=e_i-a^{-1}\mathbf1.
\tag{UT.7}
\]

For \(0\le q\le a-1\), the exact hook identification is

\[
[a-q,1^q]\simeq\Lambda^q\mathfrak h_a.
\tag{UT.8}
\]

Here is the explicit map and normalization. Send a tabloid of
shape \((a-q,1^q)\), with entries \(i_1,\ldots,i_q\) in
its ordered singleton rows, to
\(e_{i_1}\wedge\cdots\wedge e_{i_q}\). This is an
\(S_a\)-equivariant map on the tabloid permutation module.
For a polytabloid whose first column is
\((i_0,i_1,\ldots,i_q)\), column antisymmetrization gives

\[
q!\,(e_{i_1}-e_{i_0})\wedge\cdots\wedge(e_{i_q}-e_{i_0}).
\tag{UT.9}
\]

To check the factor, fix the entry omitted from the wedge.
The remaining \(q!\) column permutations give that same
ordered wedge after their two signs cancel. Expanding the
right side gives exactly these \(q+1\) possible omissions.
Taking \(i_0=a\) gives a spanning wedge basis. The hook
Specht dimension is \(\binom{a-1}{q}\): a standard hook
tableau is specified by its \(q\) first-column entries below
1. Thus the map restricts to the isomorphism (UT.8).
The characteristic-zero irreducibility of the Specht modules
then gives distinct irreducible representations for distinct
\(q\). This is also the precise hook/exterior identification
in Giannelli's Lemma 2.3.3 used and source-checked in R-003.

The ordinary dot product on \(E\) restricts nondegenerately
to \(\mathfrak h_a\), and its determinant form restricts
nondegenerately to each exterior power. These invariant forms
give the actual self-duality maps. Therefore

\[
\begin{aligned}
\dim(\Lambda^jW\otimes\Lambda^jW)^{S_a}&=1,\\
(\Lambda^{j+1}W\otimes\Lambda^{j-1}W)^{S_a}&=0
\qquad(1\le j\le a-2).
\end{aligned}
\tag{UT.10}
\]

The first equality is the endomorphism space of the irreducible
hook; the second is the homomorphism space between two distinct
hooks, under the specified dualities. At \(j=a-1\), the
first exterior power is the one-dimensional sign representation
and the target of (UT.6) is zero, yielding the same invariant
conclusion. The Reynolds operator \(a!^{-1}\sum_{g\in S_a}g\)
makes taking invariants exact. Applying it to (UT.6) proves

\[
\dim(S_{(2^j)}\mathfrak h_a)^{S_a}=1
\qquad(1\le j\le a-1).
\tag{UT.11}
\]

There is an explicit nonzero invariant in this kernel. Set
\(f_i=e_i-e_a\), \(1\le i<a\). In the wedge basis
\(f_I\), let \(G_j\) be the matrix of the induced determinant
form. Then

\[
\Omega_j=\sum_{I,J}(G_j^{-1})_{I,J}f_I\otimes f_J
\tag{UT.12}
\]

is its coevaluation tensor. It corresponds to the identity on
\(\Lambda^jW\), so it is nonzero and invariant.
Equation (UT.10) proves \(D_j\Omega_j=0\), including the
endpoint \(j=a-1\). The inverse of the first arrow in
(UT.6) on its kernel therefore supplies a specified generator
of the line in (UT.11).

## 3. Exact projected matching and flag morphisms

The invariant just constructed has a literal matching-tensor
description. In \(W\otimes W\), put

\[
J=(P\otimes P)\sum_{i=1}^a e_i\otimes e_i
=\sum_{i=1}^a P(e_i)\otimes P(e_i).
\tag{UT.13}
\]

Since \(P\) is the orthogonal projection onto \(W\),
this is exactly its coevaluation tensor. Place the \(j\)
copies of \(J\) in tensor positions \((1,j+1),\ldots,(j,2j)\).
Apply the exterior quotient in the first and last \(j\)
positions. The result is

\[
\sum_{i_1,\ldots,i_j}
 P(e_{i_1})\wedge\cdots\wedge P(e_{i_j})
 \otimes P(e_{i_1})\wedge\cdots\wedge P(e_{i_j})
=j!\,\Omega_j.
\tag{UT.14}
\]

Indeed the induced map \(\Lambda^jP\) is again an orthogonal
projection. Summing over increasing \(j\)-subsets gives
its coevaluation on its image, and summing over ordered
distinct indices contributes exactly \(j!\). Thus projection
of a fixed perfect matching, followed by the two exterior
quotients and division by \(j!\), gives precisely (UT.12).
This proves the matching-to-Schur morphism in every stated
rank; it does not require independence of all matching tensors.

To obtain the plethysm line, use an \(a\times a\) matrix
\(X\), put \(x_i=X_{i1}\), \(u=\prod_i x_i\), and define
for \(|I|=j+1\)

\[
v_{j+1,I}=\left(\prod_{i\notin I}x_i\right)
\det X_{I,\{1,\ldots,j+1\}}.
\tag{UT.15}
\]

The exact T-032 map identifies \(\Lambda^j\mathfrak h_a\)
with \(\mathbf1\wedge\Lambda^j\mathfrak h_a\) by
\(w\mapsto\mathbf1\wedge w\). On the open set \(u\ne0\),
its coordinates are
\(v_{j+1}=u\,\mathbf1\wedge\bar w_2\wedge\cdots\wedge\bar w_{j+1}\),
where \((w_k)_i=X_{ik}/x_i\) and \(\bar w_k\) subtracts
the mean coordinate. Substitution of these minors defines the
algebra morphism on the smaller flag algebra; it respects its
relations because these are actual minors of the matrix
\((u\bar w_2,\bar w_3,\ldots)\).

For the degree \((2^j)\) Schur component, its balanced
component map is exactly

\[
f\longmapsto u^{n-2}f(v_{j+1}).
\tag{UT.16}
\]

It has row weight \((n^a)\) and right weight
\((an-2j,2^j)\). For clarity its inverse on the dense chart
is also explicit: prescribe nonzero \(u_0\) and centered
columns \(F_1,\ldots,F_{a-1}\); choose \(\prod_i x_i=u_0\)
and set \(X_{i2}=x_i(F_1)_i/u_0\),
\(X_{ik}=x_i(F_{k-1})_i\) for \(k\ge3\). The prescribed
minor matrix is recovered exactly. Thus (UT.16) is injective.
For surjectivity, expand a balanced flag polynomial as flag
monomials and replace each higher minor by
\(u^{-1}(\prod_{i\in I}x_i)v_{|I|,I}\). Its right weight
has exactly two higher-minor factors; balance leaves precisely
\(u^{n-2}\) times smaller flag degree \((2^j)\). This
proves surjectivity. The exponent is nonnegative because
\(n\ge2\), so every element maps to a polynomial.

The row permutation action fixes \(u\) and commutes with
centering, so (UT.16) is \(S_a\)-equivariant with the
ordinary standard action on \(\mathfrak h_a\).
The exact Cauchy/Schur–Weyl balanced multiplicity map gives

\[
a_{a,n}^{(an-2j,2^j)}
=\dim(S_{(an-2j,2^j)}\mathbb Q^a)_{(n^a)}^{S_a}
=\dim(S_{(2^j)}\mathfrak h_a)^{S_a}=1.
\tag{UT.17}
\]

Its invariant generator is the polynomial image under (UT.16)
of the vector (UT.12) in the kernel component (UT.6).
This proves (UT.1) with its actual morphisms.

## 4. Actual canonical image and a rectangular-Kronecker consequence

Every partition in (UT.1) has second row two. Apply R-034
(LP.2), respectively (LP.4), at \(t=2\). The entire
target component is in the image for the two ranges (UT.2).
Its target multiplicity is exactly one by (UT.17), proving
the stated actual image multiplicity. This uses the annihilator
injections (LP.12) and (LP.20) and their scalar-one transpose
pairing; no dimension comparison is substituted for the map.

There is also the unconditional rectangular family

\[
\boxed{
a\ge2,\quad1\le j\le a-1,\quad n\ge2j:
\qquad g\bigl((an-2j,2^j),(a^n),(a^n)\bigr)\ge1.}
\tag{UT.18}
\]

Use the tail \(\rho=(2^j)\), of size \(2j\), in
Ikenmeyer–Panova Proposition 2.8, “Inequality of
Multiplicities,” p.7. Its stable range is \(n\ge|\rho|\),
and its plethysm term is exactly the one in (UT.17).
The source statement and full proof apply also at \(a=2\).
For the exact finite coordinate-ring maps, set
\(M=n\binom{n+n^2-1}{n}\) and
\(\lambda_M=(aM-2j,2^j)\). Proposition 2.6(b)'s padding
lift, Lemma 2.7's determinant realization, and coordinate
restriction give the finite chain

\[
1=a_{a,n}^{\lambda}
\le\operatorname{mult}_{\lambda_M}\mathbb C[\Gamma_n^M]_a
\le\operatorname{mult}_{\lambda_M}\mathbb C[\mathrm{Det}_M]_a
\le g(\lambda_M,(a^M),(a^M)).
\tag{UT.19}
\]

Here the middle inequality is the actual restriction from
\(\Gamma_n^M\subseteq\mathrm{Det}_M\); the last is the
determinant orbit Peter–Weyl comparison in Proposition 2.5.
Their Theorem 2.1's rectangular stability identifies the last
term with the one in (UT.18), since \(M,n\ge2j\).
The complete source-map chain was already written and checked
in R-014 and is specialized here without changing its maps.
The primary source is Ikenmeyer–Panova, *Rectangular Kronecker
coefficients and plethysms in geometric complexity theory*,
arXiv:1512.03798v2, <https://arxiv.org/pdf/1512.03798>.

All maps and all averaging and factorial scalars in this report
are rational. Scalar extension proves the same statements over
every characteristic-zero field.
