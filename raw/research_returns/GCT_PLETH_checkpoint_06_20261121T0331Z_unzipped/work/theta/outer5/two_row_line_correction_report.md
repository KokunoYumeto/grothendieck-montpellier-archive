# The pair-line cohomology correction and a further positive family

## T-046. Exact correction and statement

Let \(E=\mathfrak h_5\), let \(Z=\{[\ell_i]\}_{i=1}^5\subset
\mathbf P(E)\) be the canonical projective frame, let \(\mathcal I\)
be its ideal sheaf, and let \(Q=E/\mathcal O(-1)\). For every
\(a\ge b\ge0\) and \(k\ge5\), restriction to the ten pair lines
induces the actual equivariant isomorphism
\[
\boxed{H^1\bigl(\mathcal I^k(2k-2)S_{(a,b)}Q\bigr)
\simeq\operatorname{Ind}_{S_2\times S_3}^{S_5}
       (\operatorname{sgn}_{S_2}\otimes S_{(a,b)}\mathfrak h_3).}
\tag{L.1}
\]
All cohomology in degrees at least two is zero. The proof specifies
the restriction maps, proves their surjectivity by explicit jet
functionals, and identifies the induced Schur insertion quotient.

Write \(a=b+x\). For \(x,b,d\ge0\), \(k\ge5\), and
\(2b+x+k\ge6\), set
\[
\begin{aligned}
n&=d+b+x+k-2,\\
\lambda&=(d+3b+2x+3k-8,d+b+x+2k-2,d+b+x,d+x,d).
\end{aligned}
\tag{L.2}
\]
Then every coefficient \(p_{\mu,(n)}^\lambda\), \(\mu\vdash5\),
has the positive formula in §7: at most 55 contributing polytopes,
each with at most ten integer variables, after selecting three
residues. Its complete fixed integer certificate has 120,960,000
entries. No historical novelty claim is made.

## 1. Actual scalar restriction maps

For an unordered pair \(e=\{i,j\}\), put
\(P_e=\operatorname{span}(\ell_i,\ell_j)\) and
\(L_e=\mathbf P(P_e)\). No other frame point lies on \(L_e\).
Let
\[
\mathcal J_{e,k}(r)=
 \mathcal O_{L_e}(r)(-k[\ell_i]-k[\ell_j]).
\]
Restriction of a local function gives the sheaf map
\[
\mathcal I^k(r)\longrightarrow (i_e)_*\mathcal J_{e,k}(r).
\tag{L.3}
\]
At either endpoint it is the quotient of the power of the
three-variable maximal ideal onto the power of the one-variable
maximal ideal; away from the endpoints it is ordinary restriction.
Thus the map has the stated point orders. It commutes with
multiplication by every linear form and with all permutations of the
five points.

Use the ordered basis \((\ell_i,\ell_j)\) of \(P_e\), with dual
coordinates \((X,Y)\). Multiplication by \((XY)^k\) identifies
\[
\mathcal J_{e,k}(r)=(XY)^k\mathcal O_{L_e}(r-2k).
\tag{L.4}
\]
The one-dimensional factor spanned by \((XY)^k\) is fixed by the
pair stabilizer: swapping the endpoints swaps \(X,Y\), and the
other three letters fix both. At \(r=2k-2\), the first cohomology
is \(\det P_e\); at \(r=2k-3\), it is
\(P_e\otimes\det P_e\). These identifications follow from the
two-chart Čech pairing, or from
\(K_{\mathbf P(P_e)}=\det(P_e)^*\mathcal O(-2)\).
Multiplication by a linear form \(\phi\in E^*\) induces exactly
\[
P_e\otimes\det P_e\longrightarrow\det P_e,
\qquad v\otimes\omega\longmapsto\phi(v)\omega.
\tag{L.5}
\]
This fixes the representation twist and the multiplication map, not
only the dimensions of these line cohomology spaces.

## 2. Explicit overlap functionals and surjectivity

For a nonnegative twist \(r\), the ideal evaluation sequence gives
\[
H^1(\mathcal I^k(r))=
\operatorname{coker}\left(H^0\mathcal O(r)
 \longrightarrow\bigoplus_i\mathcal O(r)_{[\ell_i]}/\mathfrak m_i^k\right),
\tag{L.6}
\]
because \(H^1\mathcal O(r)=0\). The analogous line formula
describes \(H^1\mathcal J_{e,k}(r)\). The restrictions in (L.3)
are induced by restricting the actual point jets to their line jets.

Write \(\alpha_{i,s}^{e}\) for the coefficient of
\(Y^sX^{r-s}\) in the jet at \([\ell_i]\), restricted to the
line with the preceding ordered basis. Write \(\alpha_{j,t}^{e}\)
for the coefficient of \(X^tY^{r-t}\) in the jet at the other
endpoint. A global degree-\(r\) binary polynomial has
\(\alpha_{i,s}^{e}=\alpha_{j,r-s}^{e}\) whenever both coefficients
occur in the truncated jets.

At \(r=2k-2\) there is exactly one overlap, giving the functional
\[
R_e=\alpha_{i,k-1}^{e}-\alpha_{j,k-1}^{e}.
\tag{L.7}
\]
At \(r=2k-3\) there are exactly two overlaps; choose
\[
R_{i\to j}=\alpha_{i,k-1}^{e}-\alpha_{j,k-2}^{e},\qquad
R_{j\to i}=\alpha_{j,k-1}^{e}-\alpha_{i,k-2}^{e}.
\tag{L.8}
\]
All remaining binary coefficients occur at just one endpoint and can
be filled freely. Therefore (L.7), respectively (L.8), is a full
basis of the dual line cokernel. Each functional vanishes on the
restrictions of global polynomials, so it descends to the dual of
(L.6).

The four tangent directions \([\ell_j\bmod\ell_i]\), \(j\ne i\),
at a fixed frame point form a projective frame in \(\mathbf P^2\).
Indeed every three are independent and their four vector representatives
sum to zero. Their degree-\(s\) evaluation functionals are independent
for every \(s\ge2\). Here is an explicit interpolation proof. In
coordinates where the four directions are
\([1,0,0],[0,1,0],[0,0,1],[1,1,1]\), separating quadrics are
\[
z_1^2-z_1z_2,\quad z_2^2-z_1z_2,\quad
z_3^2-z_1z_2,\quad z_1z_2.
\tag{L.9}
\]
They have the four corresponding delta-value vectors. Multiply each
by \((z_1+z_2+z_3)^{s-2}\) and divide by its nonzero value at the
chosen point to obtain degree-\(s\) delta interpolation. Rescaling
the direction representatives only rescales these evaluations by
nonzero constants.

In any one affine chart at \([\ell_i]\), the highest homogeneous
part of \(\alpha_{i,k-1}^{e}\) is nonzero scalar evaluation of the
degree-\(k-1\) jet along that direction. Changing the line chart or
the line-bundle trivialization changes it only by lower-order jet
terms. Likewise \(\alpha_{i,k-2}^{e}\) involves no jet of degree
\(k-1\). This follows by substituting the linear tangent term into
the Taylor expansion; all nonlinear chart terms lower the degree of
the jet coefficient on which the resulting functional depends.

For \(k\ge3\), a relation among the ten functionals (L.7), restricted
to the degree-\(k-1\) jet at just one point, gives a relation among
four independent evaluations. Its four incident coefficients vanish;
doing this at all points kills the relation. Thus the map
\[
H^1(\mathcal I^k(2k-2))\longrightarrow
\bigoplus_e H^1\mathcal J_{e,k}(2k-2)
\tag{L.10}
\]
is onto. For (L.8), the same top layer at point \(i\) contains only
the four functionals \(R_{i\to j}\); the oppositely directed
functionals have order at most \(k-2\) there. Therefore all twenty
functionals are independent. Consequently
\[
H^1(\mathcal I^k(2k-3))\longrightarrow
\bigoplus_e H^1\mathcal J_{e,k}(2k-3)
\tag{L.11}
\]
is onto for every \(k\ge3\). This proves the source surjectivity
needed below without any assertion that reduced lines capture all
of that source cohomology.

## 3. The scalar target has exactly dimension ten

The actual Cox map in A-028 sends the section space
\(H^0(\mathcal I^k(c))\) to the \(SL_2\)-invariants of six binary
columns with weights
\[
(c-k,c-k,c-k,c-k,c-k,3c-5k).
\tag{L.12}
\]
The map is explicitly
\(p_{i6}\mapsto e_i\) and
\(p_{ij}\mapsto(q_i-q_j)/\prod_{h\notin\{i,j\}}e_h\);
the inverse is the additive-group slice. Its point-order valuation
proof identifies the whole sheaf section space, including degrees
below ordinary-power generation. This complete exact map has been
read and checked here.

For \(c=2k-2\), write \(m=k-2\) and \(q=k-6\). For \(k\ge6\),
the dimension of (L.12) is the multiplicity of \(\operatorname{Sym}^q\)
in \((\operatorname{Sym}^m\mathbf Q^2)^{\otimes5}\).
Subtracting the weight-\(q+2\) multiplicity from the weight-\(q\)
multiplicity proves that this dimension equals
\[
[z^{2k-2}]\frac{(1-z^{k-1})^5}{(1-z)^4}
 =\binom{2k+1}{3}-5\binom{k+2}{3}+10.
\tag{L.13}
\]
Only numerator terms zero, one and two contribute; all higher terms
have negative residual degree. The same final expression is zero
at \(k=5\). At that endpoint the sixth column weight is \(-1\),
so the actual Cox component is zero as well. Equivalently the two
binary weights \(-1\) and 1 have equal multiplicity.

The fat-point quotient has length \(5\binom{k+2}{3}\), and
\(H^2,H^3\mathcal I^k(2k-2)=0\). Thus its Euler characteristic is
\(\binom{2k+1}{3}-5\binom{k+2}{3}\). Equation (L.13) proves
\[
\dim H^1\mathcal I^k(2k-2)=10\quad(k\ge5).
\tag{L.14}
\]
The already onto map (L.10) has a ten-dimensional target. It is
therefore an equivariant isomorphism. This uses dimensions only after
constructing and proving surjectivity of the actual restriction map.

## 4. The exact Schur cokernel

Tensor the fully specified Schur complex (R.4) by
\(\mathcal I^k(c)\), \(c=2k-2\), and denote its three terms by
\(F_2,F_1,F_0\). Every scalar twist is nonnegative, so all their
\(H^2,H^3\) vanish. The two short exact sequences obtained by its
middle image prove
\[
H^{i\ge2}(\mathcal I^k(c)S_{(a,b)}Q)=0,
\]
\[
H^1(\mathcal I^k(c)S_{(a,b)}Q)
=\operatorname{coker}(H^1(F_1)\longrightarrow H^1(F_0)).
\tag{L.15}
\]
In particular no vanishing of \(H^1(F_1)\) or \(H^1(F_2)\) is
being asserted.

By (L.10),(L.14), the target of the map in (L.15) is
\(\bigoplus_e\det P_e\otimes S_{(a,b)}E\). By the surjectivity
of (L.11), restriction of its source maps onto
\[
\bigoplus_e(P_e\otimes\det P_e)\otimes
       (S_{(a-1,b)}E\oplus S_{(a,b-1)}E).
\]
The diagram with the two cohomology differentials commutes, because
both restrictions arise from sheaf maps and (L.5) is the induced
linear-form multiplication. Therefore its image is exactly the sum
of the individual Schur insertion images
\[
\det P_e\otimes
\operatorname{im}\left(P_e\otimes
       (S_{(a-1,b)}E\oplus S_{(a,b-1)}E)
                 \longrightarrow S_{(a,b)}E\right).
\tag{L.16}
\]
The quotient by this image is precisely \(S_{(a,b)}(E/P_e)\).
To verify the kernel directly in the chosen model, the kernel of
\(E^{\otimes(a+b)}\to(E/P_e)^{\otimes(a+b)}\) is the sum of
tensors with at least one factor in \(P_e\). Applying the primitive
Young idempotent preserves that exact quotient. Marking one such
factor is exactly the insertion map whose degree-one Schur branching
is the middle term in (L.16). Hence its image is the entire kernel.
This proves the quotient claim with the same maps and scalars as
the original Schur complex.

We obtain the actual isomorphism
\[
H^1(\mathcal I^k(c)S_{(a,b)}Q)
\simeq\bigoplus_{\{i,j\}}\det P_{ij}\otimes S_{(a,b)}(E/P_{ij}).
\tag{L.17}
\]
It is induced by restriction followed by the canonical quotient
\(Q|_{L_{ij}}\to E/P_{ij}\). The pair stabilizer acts on
\(\det P_{ij}\) by its endpoint sign. The quotient \(E/P_{ij}\)
identifies with the standard representation on the other three
letters: their zero-sum coordinate subspace is a complementary
two-plane. The endpoint transposition fixes that quotient. The
ten summands are permuted transitively. This proves (L.1), including
its action, for every \(a\ge b\ge0\), including the empty shape.

## 5. Flag transport and the explicit correction character

For (L.2), the exact flag map is
\[
\boxed{(S_\lambda\mathbf Q^5)_{(n^5)}
\simeq\epsilon^{d+b+x}\otimes
H^0(\mathcal I^k(2k-2)S_{(b+x,b)}Q).}
\tag{L.18}
\]
The relative quotient weight on \(Q^*\) is \((b+x,x,0)\), with
first-line twist \(b+x+2k-2\), after removing determinant power
\(d\). The same complementary-column pairing as T-044 changes
the twist to \(2k-2\) and supplies the displayed sign. Point order
\(\lambda_2-n=k\) and inverse \(F\mapsto u^{-k}F(v(X))\)
are unchanged. The inequality in (L.2) is exactly
\(\lambda_1\ge\lambda_2\).

Let \(P_g(x,b,k;c)\) be the three-term Schur/Euler trace (R.7),
with \(2k\) there replaced by \(c\). By (L.15), Euler
characteristic and (L.1), the actual zeroth-cohomology trace is
\[
\boxed{P_g(x,b,k;2k-2)+J_g^{\rm line}(x,b).}
\tag{L.19}
\]
There is no higher cohomology sign left unspecified: only \(H^1\)
is added back to the Euler class.

Write \(\tau(x)=(1,-1,0)_{x\bmod3}\). In the class order of
(R.6), the seven correction traces are
\[
\boxed{J_g^{\rm line}(x,b)=
\bigl(10(x+1),\ 3(-1)^b\mathbf1_{2\mid x}-(x+1),\
-2(-1)^b\mathbf1_{2\mid x},\ \tau(x),\ -\tau(x),\ 0,\ 0\bigr).}
\tag{L.20}
\]
To check this directly from (L.17), a fixed pair is either two fixed
letters or one two-cycle. The latter contributes the endpoint minus
sign. On the complement, rank-two Schur duality gives
\(S_{(b+x,b)}\mathfrak h_3=\operatorname{sgn}_{S_3}^b
\operatorname{Sym}^x\mathfrak h_3\).
Its symmetric-power traces are \(x+1\), \(\mathbf1_{2\mid x}\)
and \(\tau(x)\) on the three \(S_3\) classes. Counting fixed pairs
gives every entry of (L.20).

## 6. The complete fixed positive certificate

Put \(k=K+5\), so \(c=2K+8\). On every residue class modulo 60
in \((x,b,K)\), (L.19) is a polynomial of separate degrees
\((3,4,3)\). Its identity polynomial is
\[
\begin{aligned}
&\frac{(x+1)(b+x+2)(b+1)}{12}
\bigl[(2K+9)(b+2K+10)(b+x+2K+11)\\
&\hspace{42mm}-5(K+5)(K+6)(K+7)\bigr]+10(x+1).
\end{aligned}
\tag{L.21}
\]
It has 54 positive ordinary monomials and zero constant term. Its
total degree is six; the downward closure of its exponent support
is the same 55-element set (R.10). Exact phase substitutions of
(R.6) and (L.20) give total degree at most three for nonidentity
classes, at most one for the three-cycle class, and periodic traces
for the remaining classes. The negative Schur indices \(-1,-2\)
are covered by their exact residue-polynomial extensions. Thus the
polynomial statement holds from the initial point of every residue.

Define the fixed constants by (R.9), taking the irreducible inner
product of the actual trace (L.19), and using \((x,b,K)\) as
parameters. `two_row_line_correction_certificate.py` checks all
120,960,000 constants. All are nonnegative. The 25 inactive orders
are identically zero; every nonconstant active order is strictly
positive, with minimum 979. The largest constant is 171650016000,
below \(2^{38}\). The maximum proved bound on a weighted signed-64-bit
intermediate is 20598005160000. All exact divisibilities are checked.

`TWO_ROW_LINE_CORRECTION_SUMMARY.json` retains the full minima,
maxima, phase degrees, zero triples, intermediate bounds and per-label
hashes, with the stream and byte order stated. The concise receipt is
`TWO_ROW_LINE_CORRECTION_CHECK.txt`. The exact calculation uses three
separable Euler products plus the explicit correction (L.20); the
cohomology isomorphism establishing that correction was proved before
this computation.

## 7. Positive formula and complete support

Set \(\nu=\mu\) for even \(d+b+x\), and \(\nu=\mu^t\)
for odd \(d+b+x\). Write \((x,b,K)=r+60q\). With the constants
just defined, the exact positive formula is
\[
\boxed{p_{\mu,(n)}^\lambda
=\sum_{\alpha\in D} C^{\rm line}_{\nu,r;\alpha}
             \prod_{i=1}^3\binom{q_i}{\alpha_i},}
\tag{L.22}
\]
where \(D\) is (R.10). The ordinary multivariate Newton identity
proves this for every parameter, using the exact phase degree bound.
The finite certificate proves every fixed coefficient is nonnegative.

The bounded polytopes are exactly (R.12), now with the constants
\(C^{\rm line}\) and parameters \((x,b,K)\). Their literal bijection
to a coefficient choice and three subsets proves the summand counts.
There are at most 55 contributing tags and at most ten variables;
before selecting the unique residue, the fixed tag set has
\(60^3\cdot55\) elements. Every variable has logarithmic input bit
length plus the absolute 38-bit constant interval. The count uses
boundedly many arithmetic operations and bounded-order binomials.

All first-order constants are positive, so every zero is in the
residue cube. Apart from the invalid origin \((x,b,K)=(0,0,0)\),
which appears once in each label's row, the complete six zero cases
are
\[
\begin{array}{c|c}
\nu& (x,b,K)\\\hline
(5)&(0,1,0)\\
(3,1,1)&(0,0,1)\\
(2,1,1,1)&(0,0,1)\\
(1^5)&(0,0,2),(1,0,0),(1,0,1).
\end{array}
\tag{L.23}
\]
The other three labels have no valid zeros. Apply the effective-label
conversion before (L.22) for the actual outer partition.

`two_row_positive.py --ray line` evaluates (L.22) and exports every
constraint matrix. Its fixed constants are calculated only at the
bounded arguments of the stated finite differences, then cached.
The count calls no representation library, unknown coefficient
routine or elimination process. Its operations at input size are
bounded-order binomials, multiplication and addition.

The shared evaluator passed 1882 exact continuation, branch and
fixed-coin comparisons, together with 57 literal matrix witnesses;
receipt `TWO_ROW_EVALUATOR_CHECK.txt`.

The rectangular agent independently checked all 217 valid actual
plethysm coefficients with \(n\le6\) and all seven outer labels.
It used cycle-index expansion and Murnaghan–Nakayama on the plethysm
side. It independently computed the correction from literal fixed
two-subsets and the complementary three-letter action, rather than
using (L.20). All passed. Its receipt is
`work/rectangular/OUTER5_TWO_BELOW_RAY_INDEPENDENT_CHECK.tsv`.

## Sources and exact scope

The primary Cox-ring locator is Castravet–Tevelev,
[*Hilbert's 14th problem and Cox rings*, Remark 3.9, p.1487](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/116C1106A59A410F79236A57C5477270/S0010437X06002284a.pdf/hilberts-14th-problem-and-cox-rings.pdf).
That remark was opened and read in the published primary PDF. The
exact action and multigraded component map used here are the explicit
ones proved in A-028, whose full proof was independently read.
The line Čech groups and multiplication pairing are
[Stacks Project, Lemmas 30.8.1 and 30.8.2](https://stacks.math.columbia.edu/tag/01XS),
with the determinant factor tracked in (L.4)–(L.5).
The Schur complex is the actual signed tensor/projector construction
checked in the archive appendix. G-015 supplies the exact balanced
flag chart, with its valuation proof and the determinant pairing
written in (L.18).

The theorem covers \(k\ge5\). At \(k=3,4\) the scalar first
cohomology has dimensions 15 and 16, so the scalar restriction map
is not an isomorphism onto the ten reduced-line groups. Those small
orders are not folded into (L.1). The proof here isolates precisely
the range where the actual restriction map has been proved an
isomorphism and evaluates every two-row quotient in that range.
