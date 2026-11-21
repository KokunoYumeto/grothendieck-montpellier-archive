# An actual canonical-map range from tail moments

## R-046. Surjectivity for \(D+t\le2n+1\)

Let \(a,n\ge2\), let \(\lambda\vdash an\), and write
\[
\nu=(\lambda_2,\lambda_3,\ldots),\qquad
D=|\nu|,\qquad t=\nu_1 .
\]
For the empty tail put \(D=t=0\). The actual normalized map
\[
h_{n,a}:\operatorname{Sym}^n(\operatorname{Sym}^aV)
 \longrightarrow\operatorname{Sym}^a(\operatorname{Sym}^nV)
\]
is surjective on the entire \(\lambda\)-isotypic component
throughout the finite parameter family
\[
\boxed{D+t\le2n+1.}
\tag{TM.1}
\]
The assertion holds over every characteristic-zero field
and in every finite dimension. The component is zero
in dimensions below \(\ell(\lambda)\).

The proof gives the actual factorization, including all
tensor normalizations,
\[
\boxed{\begin{gathered}\text{independent-row polarization}\\
 \longrightarrow\ \text{invertible split-moment substitution}\\
 \longrightarrow\ \text{finite centered power-sum evaluation}\end{gathered}}
\tag{TM.2}
\]
It proves injectivity of \(h_{a,n}\) on the dual component;
the scalar-one transpose identity SR.5–SR.6 then gives
(TM.1). Every factor in (TM.2) is specified below.

### Established coefficient input and scope

The numerical threshold
\[
N(\nu)=\left\lfloor\frac{D+t}{2}\right\rfloor
\tag{TM.3}
\]
for stable coefficients is already Sarkar's Theorem D,
numbered Theorem 6.4 in *Stability of plethysm coefficients
and modified polynomial induction*, arXiv:2610.07929v2.
It is recorded as T-010. Its coefficient formula has
inner parameter at least \(t\), outer parameter at least
\(N(\nu)\), and the displayed first-row partition condition.
The complete §6 proof and Proposition 7.1 were read from
the retained primary source work/theta/sarkar/main.tex.
The source URL is https://arxiv.org/src/2610.07929v2.
No historical novelty claim is made for that threshold
or for its stable character.

The present proof includes a finite-row power-sum
faithfulness argument and the exact canonical factorization
(TM.2), so its asserted conclusion concerns the specified
map. It applies with arbitrary target outer degree \(a\);
the condition is \(n\ge N(\nu)\).
The earlier Bowman–Paget Theorems A and B, in
arXiv:1809.08128v2, printed pp.1–2, give the stable
coefficient and its decomposition at their stated larger
parameter range. Their statement scope was checked in the
primary PDF https://arxiv.org/pdf/1809.08128.
They are background to the explicit proof below.

## 1. The actual highest-space chart and row-degree bound

For \(s\ge1\), write \(E_s=\mathbb Q^s\),
\[
W_s=\left\{(u_i):\sum_i u_i=0\right\},\qquad
P_s e_i=e_i-\frac1s\sum_j e_j.
\]
The rational dot product identifies \(W_s\) with its dual
as an \(S_s\)-module. Every use of centering is the actual
linear projection \(P_s\).

Write the \(a\) vector slots as \((x_i,y_i)\), with the
first coordinate separated. On \(\prod_i x_i\ne0\),
a highest polynomial of weight \(\lambda\) has the
unique expression
\[
F(x_i,y_i)=\left(\prod_i x_i\right)^n
                 f(y_1/x_1,\ldots,y_a/x_a).
\tag{TM.4}
\]
The highest equations in the first coordinate are the
common-translation equations for \(f\). Thus \(f\)
factors through \(P_a\), and slot symmetry makes it
\(S_a\)-invariant. Its remaining highest weight is
\(\nu\), of total degree \(D\).

The rational Cauchy projectors identify this highest
multiplicity space with \((S_\nu W_a)^{S_a}\), subject
to the separate slot-degree bound needed for (TM.4)
to be polynomial. For specificity, one may use the
rational Young idempotent \(c_T r_T/H_\nu\), where
\(r_T,c_T\) are the row symmetrizer and column
antisymmetrizer and \(H_\nu\) is the hook product.
The usual tensor Cauchy maps, with the same projector
at every node, are natural in the row vector space.

Every vector of \(S_\nu E_a\) has each row-basis weight
at most \(t=\nu_1\). Indeed in a semistandard column
basis each column contains a fixed basis letter at
most once, and there are exactly \(t\) columns.
Equivalently the column antisymmetrizer kills every
tensor assigning the same row letter twice in one
column. This proves that the image of
\(S_\nu W_a\hookrightarrow S_\nu E_a\) has separate
row degrees at most \(t\). Consequently all invariants
in this component homogenize polynomially in (TM.4)
as soon as \(n\ge t\).

For a nonempty tail \(D\ge t\); therefore
\(N(\nu)\ge t\). Under (TM.1) we have \(n\ge N(\nu)\).
The chart is thus an actual isomorphism of the relevant
highest spaces in the entire stated range. Its inverse
is the explicit homogenization in (TM.4).

## 2. Ordinary centered moments and their actual evaluation maps

For a finite-dimensional auxiliary space \(U\), let
\[
\mathcal M(U)
=\operatorname{Sym}\left(\bigoplus_{d\ge2}
                  \operatorname{Sym}^d U\right).
\tag{TM.5}
\]
A generator in \(\operatorname{Sym}^dU\) has scalar
degree \(d\). The centered row power sums define
the \(GL(U)\)-equivariant graded-algebra map
\[
p_s:\mathcal M(U)\longrightarrow
       \bigl(\operatorname{Sym}(W_s\otimes U)\bigr)^{S_s}.
\tag{TM.6}
\]
On a polarized generator \(u_1\cdots u_d\), its image is
the sum over \(i\) of the products
\((P_s e_i\otimes u_1)\cdots(P_s e_i\otimes u_d)\).
There is no scalar multiplier.

The map is surjective. First use the uncentered row
space \(E_s\) and include the degree-one generators.
A product of row power sums expands over all assignments
of its factors to rows. Its discrete equality partition
is the injective row-assignment sum. All other equality
partitions merge at least two nonempty row types.
Induction on occupied rows expresses every orbit sum
in the power sums. Repeated row types contribute their
explicit nonzero factorial; characteristic zero
permits division by it. These orbit sums span the
ordinary invariant polynomial algebra.
The equivariant decomposition
\(E_s=\mathbb Q\mathbf1\oplus W_s\) identifies the
uncentered invariant algebra with
\(\operatorname{Sym}(U)\otimes
(\operatorname{Sym}(W_s\otimes U))^{S_s}\).
Setting the first summand to zero is exactly centering
and kills the degree-one power sums. This proves
(TM.6), including its finite-row scope.

For \(s\ge D\), the map (TM.6) is an isomorphism through
degree \(D\). In the uncentered argument, every power-sum
monomial of degree at most \(D\) uses at most \(D\)
nonempty rows. Its injective-assignment term therefore
exists. Ordering by the number of occupied rows gives
a triangular change of basis from power-sum monomials
to orbit sums, with nonzero factorial diagonal.
Hence the uncentered free-algebra map is an isomorphism
in these degrees. Quotienting the explicitly identified
degree-one polynomial factor gives the asserted
centered isomorphism.

Only degrees \(2,\ldots,t\) in (TM.5) contribute to its
\(S_\nu U\)-isotypic component. A factor
\(\operatorname{Sym}^d U\) with \(d>t\), in any polynomial
tensor product, requires a horizontal \(d\)-strip by
the actual symmetric Pieri projection. Such a strip
uses \(d\) distinct columns, while \(\nu\) has only
\(t\) columns. Thus this component lies in
\[
\mathcal M_{\le t}(U)
=\operatorname{Sym}\left(\bigoplus_{d=2}^t
                      \operatorname{Sym}^dU\right).
\tag{TM.7}
\]

## 3. Faithfulness already at \(s\ge N(\nu)\)

The following finite-row argument recovers the numerical
threshold while retaining the power-sum morphism.

Set \(T=\mathbb Q^t\), and define
\[
C_s(T)=\bigl(\Lambda(E_s\otimes T)\bigr)^{S_s},
\qquad
B_s(T)=\bigl(\Lambda(W_s\otimes T)\bigr)^{S_s}.
\]
Exterior multiplication along the ordered rows gives
an actual equivariant identification
\(\Lambda(E_s\otimes T)\cong(\Lambda T)^{\otimes s}\),
with the Koszul signs in row permutations.
Averaging \(1/s!\) identifies its invariants with the
degree-\(s\) supersymmetric tensor power of \(\Lambda T\).
Decomposing \(\Lambda T\) into its exterior degrees
therefore gives the direct sum
\[
C_s(T)\cong
\bigoplus_{\substack{e_0+\cdots+e_t=s\\ e_i\ge0}}
 \left(\bigotimes_{\substack{i\ge2\\ i\ {\rm even}}}
       \operatorname{Sym}^{e_i}(\Lambda^iT)\right)
 \otimes
 \left(\bigotimes_{\substack{i\ge1\\ i\ {\rm odd}}}
       \Lambda^{e_i}(\Lambda^iT)\right).
\tag{TM.8}
\]
The \(e_0\)-factor is the one-dimensional unit.
These are literal symmetrizer/antisymmetrizer maps;
they also explain the zero produced by a repeated odd
row type.

A summand of scalar degree \(e\) uses
\(k=\sum_{i\ge1}e_i\) nonempty rows. Since
\(e_1\le\dim T=t\) and every other type has degree
at least two,
\[
e=\sum_i i e_i\ge e_1+2(k-e_1),
\qquad
k\le\left\lfloor\frac{e+t}{2}\right\rfloor.
\tag{TM.9}
\]
For every \(e\le D\), all possible nonempty factors in
(TM.8) are therefore present once \(s\ge N(\nu)\);
the unit fills exactly \(e_0=s-k\) rows.
Thus the complete \(GL(T)\)-character of \(C_s(T)\)
through degree \(D\) is constant in this range.

The fixed linear decomposition of \(E_s\) gives the
actual exterior-algebra isomorphism
\[
C_s(T)\cong\Lambda T\otimes B_s(T).
\tag{TM.10}
\]
In degree zero the \(\Lambda T\) factor is the identity.
In each subsequent degree, (TM.10) determines the
character of \(B_s(T)\) from the degree-\(e\) character
of \(C_s(T)\) and lower-degree terms already determined.
Induction on \(e\le D\) therefore proves that the
character of \(B_s(T)\) is constant for \(s\ge N(\nu)\).

The skew-Cauchy Young maps give
\[
B_s(T)_D
=\bigoplus_{\eta\vdash D,\ \eta_1\le t}
     (S_\eta W_s)^{S_s}\otimes S_{\eta^t}T.
\tag{TM.11}
\]
All maps are induced by the same tensor column and row
projectors. In particular
\(\dim(S_\nu W_s)^{S_s}\) is constant for
\(s\ge N(\nu)\).

We now turn this dimension statement into faithfulness
of the specified map (TM.6). For \(S\ge s\), zero-padding
is an injection \(\iota:W_s\hookrightarrow W_S\).
Its rational orthogonal transpose \(q:W_S\to W_s\)
satisfies
\[
q(P_S e_i)=
\begin{cases}
P_s e_i,&i\le s,\\
0,&i>s.
\end{cases}
\tag{TM.12}
\]
Indeed restriction to the first \(s\) coordinates
followed by subtracting their mean has exactly these
values. On both ordinary and exterior power sums,
(TM.12) sends every degree-\(d\) generator to the
same degree-\(d\) generator with scalar one.
Consequently it gives surjections on the corresponding
invariant algebras. Its ordinary and skew-Cauchy
multiplicity maps are the same actual Schur morphism
\(S_\nu(q)\) on \(S_\nu W\), because Young projectors
commute with tensor powers of \(q\).

Choose \(S\ge\max(s,D)\). At this row count (TM.6)
is an isomorphism in degree \(D\), by §2.
For \(s\ge N(\nu)\), (TM.11) gives equal dimensions
on its \(\nu\)-multiplicity and at row count \(S\).
The surjection \(S_\nu(q)\) is therefore an isomorphism.
The commuting equality
\(p_s=\operatorname{Sym}(q\otimes1)\,p_S\),
proved on every generator by (TM.12), now proves
\[
\boxed{p_s\text{ is injective and surjective on the }
S_\nu U\text{ component for }s\ge N(\nu).}
\tag{TM.13}
\]
This argument specifies the morphism whose
faithfulness is used later.

## 4. Independent-row polarization is injective

View a row-symmetric polynomial \(f\) as an element of
\(\operatorname{Sym}^a A_t\), where
\(A_t=\mathbb Q[U]_{\le t}\). Its independent-row
functional is
\[
E_a(f)(L)=L^{\otimes a}f.
\tag{TM.14}
\]
Rational polarization of the diagonal polynomial makes
this an injective linear map. Restricting to
\(L(1)=1,L(U)=0\) remains injective on the
common-translation-invariant subspace:
for normalized \(L\) with mean vector \(v\), the
functional \(L_0(p)=L(p(w-v))\) has mean zero and
gives the same value on \(f\). Homogeneity restores
all \(L\) with \(L(1)\ne0\), a dense open set.
This is the exact morphism and proof DF.7–DF.9.

The coordinates of such an \(L\) are the formal
symmetric moment tensors \(\mu_d\), \(2\le d\le t\).
Hence (TM.14) maps into \(\mathcal M_{\le t}(U)\),
preserving scalar degree and the \(GL(U)\)-action.
For \(f\) in the tail-\(\nu\) component, its image lies
in the \(S_\nu U\)-component to which (TM.13) applies.

## 5. The full triangular split-moment automorphism

Let \(w_1,\ldots,w_n\) be centered factor rows, and
write \(p_d=\sum_iw_i^{\otimes d}\); thus \(p_1=0\).
The exact normalized monomial pairing with
\(\prod_i(x+w_i\cdot y)\) is the distinct-factor tensor
\[
\mu_d=\frac1{(n)_d}
 \sum_{\substack{i_1,\ldots,i_d\\\text{all distinct}}}
       w_{i_1}\otimes\cdots\otimes w_{i_d},
\qquad 2\le d\le t.
\tag{TM.15}
\]
The tensor on the right is symmetric. For a monomial
with multiplicities \(\beta\), its component is the
product-form coefficient multiplied by
\((n-d)!\prod_j\beta_j!/n!\). This is exactly the
pure-power normalization SR.5–SR.6, including every
repeated-index factorial.

Expand the distinct-index sum by Möbius inversion on
the lattice of set partitions of \([d]\).
The Möbius coefficient of a block \(B\) is
\((-1)^{|B|-1}(|B|-1)!\). Thus
\[
\boxed{
\mu_d=
\frac1{(n)_d}
 \sum_{\substack{\pi\in\Pi([d])\\|B|\ge2\ {\rm for\ all}\ B}}
 \prod_{B\in\pi}
       (-1)^{|B|-1}(|B|-1)!\,p_{|B|}.}
\tag{TM.16}
\]
Products in this equation mean the symmetric tensor
product with the indicated coordinate positions;
equivalently polarize both sides. Each set partition
is retained once. The block coefficient follows by
inclusion–exclusion, or by the recurrence
\(\sum_{\pi\in\Pi([d])}\prod_B(-1)^{|B|-1}(|B|-1)!=0\)
for \(d>1\), which is the signed permutation count
by cycle partition. Singleton blocks vanish because
\(p_1=0\).

There is precisely one one-block term in (TM.16).
All other terms involve generators of strictly
smaller degree. Consequently the substitution
\[
\begin{gathered}\Psi_n:\mathcal M_{\le t}(U)\longrightarrow
                    \mathcal M_{\le t}(U),\\
\mu_d\longmapsto
 \frac{(-1)^{d-1}(d-1)!}{(n)_d}p_d
   +\text{the printed lower-degree products}\end{gathered}
\tag{TM.17}
\]
is an explicit graded \(GL(U)\)-equivariant algebra
automorphism for \(n\ge t\).
Its inverse is obtained successively in degrees
\(2,3,\ldots,t\), dividing only by the displayed
nonzero rational scalars. This is the exact
triangular morphism, with no unspecified change
of generators.

## 6. Exact factorization of the canonical map

For the highest vector \(F\) in (TM.4), evaluate
\(h_{a,n}F\) on \(n\) split-factor rows. On the affine
chart with first coordinates one, the grid pairing
is precisely \(L^{\otimes a}f\), with \(L\) given by
(TM.15). Thus the dehomogenized output is exactly
\[
\boxed{p_n\,\Psi_n\,E_a(f).}
\tag{TM.18}
\]
No additional scalar occurs: (TM.15) was obtained
from the same normalized tensor pairing.

The calculation on centered rows determines the full
affine output. The original highest equations and
equivariance of \(h_{a,n}\) make both sides invariant
under common translations. Subtracting the common
mean is the explicit unipotent substitution
\((x,y)\mapsto(x,y-\bar w x)\).
First-coordinate homogeneity then multiplies the
affine output by \((\prod_j x_j)^a\), restoring the
polynomial identity on the dense chart and hence
everywhere. Individual formal expressions need not
separately extend in slot degree \(a\); their actual
composition extends because it is the displayed
canonical polynomial.

Under (TM.1), \(n\ge N(\nu)\ge t\).
The first map in (TM.18) as read from right to left
is injective by §4, the middle map is invertible by
§5, and the last map is injective on the precise
Schur component by (TM.13).
Therefore \(h_{a,n}\) is injective on the whole
highest multiplicity space. Every map is equivariant,
so it is injective on the entire corresponding Schur
isotypic component. The scalar-one transpose pairing
identifies its rank with that of \(h_{n,a}\) on the
dual component. This proves (TM.1).

The empty tail is immediate from the actual tensor
map \(h_{n,a}((v^a)^n)=(v^n)^a\), with coefficient one.

## 7. Concrete unconditional consequences

First, for every integer \(b\ge2\), \(a\ge2\), and
\[
\boxed{n\ge\left\lfloor\frac{ab}{2}\right\rfloor,}
\tag{TM.19}
\]
the map \(h_{n,a}\) is surjective in every component
with \(\lambda_2\le b\).
Components of length greater than \(a\) are zero in
the target, by the tensor-slot Young projection.
For the remaining components,
\(D\le(a-1)\lambda_2\), so
\(N(\nu)\le\lfloor a\lambda_2/2\rfloor
\le\lfloor ab/2\rfloor\).
This proves the entire second-row band, with all
multiplicities and no upper bound on \(a\) or \(b\).

For second row at most four the explicit consequence is
\[
\boxed{n\ge2a\quad\Longrightarrow\quad
 h_{n,a}\text{ is surjective in every }\lambda_2\le4
 \text{ component}.}
\tag{TM.20}
\]
The sharper tail-sensitive range is \(n\ge\lfloor D/2\rfloor+2\)
for width exactly four. R-044 and R-045 supply their
already proved additional finite-row ranges.

Second, let \(\rho\ne\varnothing\) be a partition,
\(a\ge\ell(\rho)+1\), and
\[
n\ge|\rho|+\rho_1,\qquad
\lambda=(an-2|\rho|,2\rho).
\]
Then \(N(2\rho)=|\rho|+\rho_1\), so
\[
\boxed{\operatorname{mult}_\lambda\operatorname{im}h_{n,a}
       =a_{a,n}^{\lambda}\ge1.}
\tag{TM.21}
\]
The complete multiplicity equality is (TM.1).
The last inequality also has the explicit product
preimage of R-037 EP.3–EP.5. The first-row inequality
is literal: for \(r=\ell(\rho)\ge1\),
\(an-2|\rho|\ge(r-1)|\rho|+(r+1)\rho_1\ge2\rho_1\).
Thus every displayed weight is a partition.

Finally, for every fixed tail the fully stable source
and target range
\[
a,n\ge N(\nu),\qquad an-D\ge t
\tag{TM.22}
\]
gives an actual isomorphism on that component, by
applying (TM.1) in both directions. In this range
the common dimension is the known stable character
coefficient \([S_\nu U:\mathcal M(U)]\).
This is the same formal moment module in (TM.5).

## 8. Rational and geometric transport; executed checks

All row projections, Young projectors, invariant
averages, polarization operators and inverse
substitutions above are rational. Their denominators
are explicitly nonzero in the asserted integer ranges.
They therefore extend to every characteristic-zero
field. Naturality in \(V\) gives the same multiplicity
maps in each rank supporting \(S_\lambda V\).

The actual graded coordinate-ring morphism is the
Chow pullback R-037 EP.3–EP.5, whose degree-\(n\)
piece is \(h_{n,a}\) with scalar one.
The associated-bundle morphism on a frame torsor,
and the exact SGA 6 VI Theorem 3.3, SGA 6 V §4,
SGA 3 I §4 and EGA II §§2.4–2.5 locators, are the
construction recorded in R-036 §5.
The injective/surjective maps were proved before
passing to representation \(K_0\).

The exact script verify_tail_moment_stability.py
independently checks all 276 pairs consisting of a
tail of degree \(1\le D\le10\) and row count
\(N(\nu)\) or \(N(\nu)+1\).
It computes the finite \((S_\nu W_s)^{S_s}\)
multiplicity by averaging the Schur character on
literal permutations of \(s\) letters; power traces
are the number of fixed points of the relevant
permutation power minus one.
It independently computes the formal moment
multiplicity by expanding the tensor products of
the ordinary plethysms for all moment-degree
partitions without parts one.
All 276 values agree.
The receipt is TAIL_MOMENT_STABILITY_CHECK.tsv.

The same script checks (TM.15)–(TM.16) against
actual product linear forms for degrees two through
eight, two row counts per degree, two centered
configurations, and every two-coordinate monomial.
All 168 exact normalized moment entries pass.
The receipt is GENERAL_SPLIT_MOMENT_CHECK.tsv.
These computations check the finite character and
normalization identities; the general canonical-map
claim is proved by the explicit factorization above.

