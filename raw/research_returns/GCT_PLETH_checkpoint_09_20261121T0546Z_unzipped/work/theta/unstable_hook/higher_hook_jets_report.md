# Hook jets on a projective frame in varying outer degree

## T-062. An explicit surjective jet map in every ideal order

Let \(m\ge4\), \(k\ge1\), \(a\ge2k+1\), \(0\le r\le m-2\),
\(t\ge0\), and \(\mu\vdash m\). Set
\[
\begin{aligned}
n&=a+t-k,\\
\lambda&=((m-1)a+t-mk-r,a+t,(t+1)^r,t^{m-2-r}),\\
\nu&=\mu\quad(t\text{ even}),\qquad
\nu=\mu'\quad(t\text{ odd}).
\end{aligned}
\tag{HJ.1}
\]
The first gap is nonnegative: its minimum is
\((m-2)(2k+1)-mk-(m-2)=(m-4)k\). Thus these parameters
always define a partition of \(mn\).

Write \(E=\mathfrak h_m\), \(v_i=e_i-m^{-1}\mathbf1\), and
\(Z=\{[v_i]\}\subset\mathbb P(E)\). Let \(Q\) be the tautological
quotient. There is an actual split exact sequence of rational
\(S_m\)-modules
\[
\begin{split}
0\longrightarrow
H^0\bigl(\mathcal I_Z^k\otimes\Omega^r(a+r)\bigr)
\longrightarrow S_{(a,1^r)}E^*
\xrightarrow{\operatorname{jet}_k}
\operatorname{Ind}_{S_{m-1}}^{S_m}
\left(\bigoplus_{j=0}^{k-1}
\operatorname{Sym}^j\mathfrak h_{m-1}
\otimes\Lambda^r\mathfrak h_{m-1}\right)
\longrightarrow0.
\end{split}
\tag{HJ.2}
\]
The duals in the target are identified by the specified rational dot
forms. G015's actual flag map, with T061's exterior pushforward, gives
\[
(S_\lambda\mathbb Q^m)_{(n^m)}
\simeq\operatorname{sgn}^t\otimes\ker\operatorname{jet}_k.
\tag{HJ.3}
\]
Consequently the plethysm coefficient is the stable-hook multiplicity
of \([\nu]\) minus its multiplicity in the explicit induced module.
All maps and the splitting are given below. The positive polytope
conversion in T063 is proved for \(k=2\); (HJ.2) itself holds for
every displayed \(k\).

### 1. Quadratic coordinates for all normal directions

Let \(U=H^0(\mathcal I_Z(2))\). At every point, differentiation on
the affine chart \(\ell_i=1\), where \(\ell_i=mz_i/(m-1)\), gives
a surjection
\[
\partial_i:U\longrightarrow W_i^*,\qquad W_i=\ker\ell_i.
\tag{HJ.4}
\]
Here is an explicit rank proof. Use \(s=m-1\ge3\) frame vectors as
a basis. The projective points are the coordinate points and
\([1:\cdots:1]\). Their quadratic ideal is spanned by
\(x_jx_l-x_1x_2\), with \(j<l\), omitting the zero member.
This is the actual ideal presentation proved in G016; its degree-two
part also follows by evaluating a general quadratic. At a coordinate
point \(e_h\), \(h\notin\{1,2\}\), the pairs \((h,j)\) give every
transverse derivative \(dx_j\). At \(e_1\), the pairs \((1,j)\)
and \((2,j)\), \(j\ge3\), give \(dx_j-dx_2\) and \(-dx_2\);
the argument at \(e_2\) is identical. At the all-ones point the
derivatives are \(dx_j+dx_l-dx_1-dx_2\). Taking a third index
shows that these span every coordinate difference, the full
projective cotangent space. This proves (HJ.4).

Give \(U\) the invariant positive rational form inherited from
\(\operatorname{Sym}^2E^*\). The explicit rational map
\[
\sigma_i=\partial_i^*(\partial_i\partial_i^*)^{-1}:
W_i^*\longrightarrow U
\tag{HJ.5}
\]
is a derivative right inverse. It commutes with the stabilizer of
\(v_i\), and all \(\sigma_i\) are related by literal permutations.
The inverse exists by the proved surjectivity and positivity, so
no unspecified generic rank is used.

Use the quadratic separators
\[
p_i=\frac m{m-2}z_i^2-
\frac{\sum_jz_j^2}{(m-2)(m-1)}.
\tag{HJ.6}
\]
They satisfy \(p_i(v_j)=\delta_{ij}\), as computed in T061.
Choose a basis \(u_1,\ldots,u_{m-2}\) of \(W_i^*\), and write
\(f_h=\sigma_i(u_h)\). At \(v_i\), the functions \(y_h=f_h/p_i\)
have zero constant term and independent linear terms \(u_h\).
Thus substitution induces an isomorphism of finite jet algebras
\[
\mathbb Q[y_1,\ldots,y_{m-2}]/(y)^k
\xrightarrow{\sim}
\mathcal O_{\mathbb P(E),[v_i]}/\mathfrak m_i^k.
\tag{HJ.7}
\]
An exact inverse is obtained by successively removing homogeneous
terms of orders \(1,\ldots,k-1\). This finite triangular construction
proves the isomorphism and specifies its rational map.

The homogeneous polynomials
\[
p_i^{\,k-|\beta|}f_1^{\beta_1}\cdots f_{m-2}^{\beta_{m-2}},
\qquad |\beta|<k,
\tag{HJ.8}
\]
all have degree \(2k\). Their jets at \([v_i]\) form a basis,
because (HJ.8) is \(p_i^k y^\beta\), with \(p_i^k\) a unit there.
At every other point each \(p_i\) and \(f_h\) belongs to the
maximal ideal; the total number of factors is \(k\). They therefore
vanish to order at least \(k\) at all other points. This is the exact
simultaneous scalar interpolation map.

### 2. The horizontal lift and the equivariant jet splitting

For \(\phi\in\Lambda^r\operatorname{ann}(v_i)\), put
\[
H_i(\phi)=\iota_z(\ell_i\wedge\phi).
\tag{HJ.9}
\]
This is a horizontal form of coefficient degree one. On the affine
chart \(\ell_i=1\), it gives a bundle isomorphism from the constant
space \(\Lambda^rW_i^*\) to horizontal forms: restriction to \(W_i\)
is its inverse. The Euler contraction squares to zero, proving
horizontality directly.

Multiply (HJ.8) times (HJ.9) times \(\ell_i^{a-2k-1}\). The
exponent is nonnegative, and the coefficient degree is exactly \(a\).
The resulting horizontal forms are global sections of
\(\Omega^r(a+r)\). Their jets at point \(i\) form a basis of all
form-valued jets, and their jets at all other points vanish.
The finite inverse in (HJ.7), with the unit factor \(p_i^k\)
removed, constructs an actual right inverse at that point.
Expressed through the symmetric powers of (HJ.5), this construction
is independent of the chosen basis and stabilizer-equivariant.
Summing over the points gives an \(S_m\)-equivariant rational
right inverse to \(\operatorname{jet}_k\).

On \(\ell_i=1\), the stabilizer fixes \(v_i\) and acts linearly
on \(W_i\cong\mathfrak h_{m-1}\). Its action on the order-\(<k\)
Taylor algebra is exactly \(\bigoplus_{j<k}\operatorname{Sym}^jW_i^*\).
The specified affine vector trivializes the homogeneous line without
a further character. The horizontal basis contributes
\(\Lambda^rW_i^*\). This proves the precise target and every twist.

The ideal power in (HJ.2) is the ordinary power as a sheaf. At each
of the disjoint reduced points it is the maximal ideal power, so
its kernel is exactly order-\(k\) jet vanishing. G015's actual flag
extension criterion uses this same sheaf. T061's exterior pushforward
and tensor-with-ideal comparison apply on each product chart, giving
(HJ.3).

## T-063. A polynomial-size positive formula at second ideal order

Take \(k=2\) in (HJ.1), so \(a\ge5\). Let
\(c_{m,a,r}(\nu)=[\,[\nu]:S_{(a,1^r)}\mathfrak h_m\,]\)
be G037's stable hook coefficient. Define \(d_{m,r}(\nu)\) by
the following finite Young-graph rule. Put \(q=m-1-r\).
Start with
\[
(q-1,1^r)\quad(q\ge2),\qquad
(q,1^{r-1})\quad(r\ge1).
\tag{HJ.10}
\]
From each displayed partition of \(m-2\), add two boxes in successive
partition-preserving steps. Count the paths ending at \(\nu\). Then
\[
\boxed{
p_{\mu,(a+t-2)}^\lambda
=c_{m,a,r}(\nu)-d_{m,r}(\nu),\qquad
0\le d_{m,r}(\nu)\le4.}
\tag{HJ.11}
\]
Every such coefficient is the lattice count of at most
\(8(m^2+3m-4)-3\) bounded rational polytopes in at most
\(m^2+3m-4\) variables. Complete matrices are constructed in time
polynomial in \(m\) and the binary input lengths; the exact coefficient
and nonvanishing have the same polynomial bit bound. For ordinary
binary-part encoding this gives the corresponding polynomial and
counting bounds when \(t\ge1\). At \(t=0\), the assertion retains
an explicit/unary \(m\) parameter, as in G037 and T061.

### 3. The actual two-step branching map

For \(k=2\), the fiber in (HJ.2) is
\((\mathbb Q\oplus\mathfrak h_{m-1})\otimes
\Lambda^r\mathfrak h_{m-1}\). Its first factor is the literal
permutation module on \(m-1\) coordinates. If \(G=S_m\),
\(K=S_{m-1}\), \(L=S_{m-2}\), and
\(H=\Lambda^r\mathfrak h_{m-1}\), the tensor-induction isomorphism is
\[
g\otimes(hL\otimes v)\longmapsto gh\otimes h^{-1}v:
\operatorname{Ind}_K^G(\mathbb Q[K/L]\otimes H)
\xrightarrow{\sim}
\operatorname{Ind}_L^G\operatorname{Res}_L^K H.
\tag{HJ.12}
\]
Representative changes and the defining induced-module relations give
the same image, and the displayed formula has its inverse on the coset
summands. Under \(L\), the standard module splits as
\(\mathfrak h_{m-2}\oplus\mathbb Q\): the second line is spanned
by the vector with its first \(m-2\) coordinates equal to one and
its last equal to \(-(m-2)\). Taking exterior powers gives the two
hooks in (HJ.10), with out-of-range exterior powers zero. Two
applications of one-box Pieri through rational Young projections
give exactly the path rule.

For each starting hook and final label there are at most two orders
for adding the specified pair of boxes. There are at most two starting
hooks, proving \(d\le4\). Every resulting diagram is a hook plus
two boxes, so it has at most two boxes on any diagonal. The row
label \((m)\) has \(d=1\) exactly for \(r=0,1\), and otherwise
has \(d=0\). These observations include all short-row and maximal-leg
endpoints. Equation (HJ.11) follows from the actual split sequence
(HJ.2), including its determinant twist.

### 4. Polynomially many candidates for the points to delete

Suppose \(d=d_{m,r}(\nu)>0\), first with \(\nu\ne(m)\).
G037's single polytope records a standard tableau \(T\), an
\(r\)-subset \(S\) of
\(C_\nu=\nu\setminus\{(1,1),(2,1)\}\), and coins of weights
\(2,\ldots,m\), with total
\[
\operatorname{comaj}(T)+
\sum_{(i,j)\in S}(j-i+1)+\sum_{h=2}^m h\beta_h=a+r.
\tag{HJ.13}
\]
Write \(b(\nu)=\sum(i-1)\nu_i\), and let \(L\) be \(b(\nu)\)
plus the sum of the \(r\) smallest retained weights. G037's positive
numerator has smallest exponent exactly \(L\). The Koszul cycle space
has no total degree \(D\le r\): for \(r>0\), a constant exterior
form killed by every coordinate contraction is zero; for \(r=0\)
the cycle convention is \(P_+\). The positive numerator and
constant-one denominator therefore prove
\[
L\ge r+1.
\tag{HJ.14}
\]

Choose \(a_0=5\) when \(a\) is odd and \(a_0=6\) when \(a\)
is even. The surjective jet map at \(a_0\) proves that the stable
polytope has at least \(d\) lattice points. Every such point has
numerator excess at most \(a_0+r-L\le5\). The following enumeration
finds \(d\) explicit distinct points among polynomially many candidates.

Enumerate semistandard fillings \(u(i,j)\) satisfying
\[
u(i,j)\ge i-1,\qquad
\sum_{(i,j)\in\nu}(u(i,j)-(i-1))\le5.
\tag{HJ.15}
\]
There are at most \(\binom{m+5}{5}\) nonnegative increment arrays.
Retain the weak-row, strict-column fillings. Standardize by increasing
entry, with equal entries ordered from left to right, and remove
duplicates. This finds every standard tableau with
\(\operatorname{comaj}(T)-b(\nu)\le5\): its minimal semistandard
filling puts at label \(j\) the number of descents at indices less
than \(j\). Its entry sum is comajor, every entry is at least the
row index minus one, and the indicated standardization recovers \(T\).
These are the actual standardization maps of T028/G037.

For the subset, sort the retained weights and let \(w_0\) be the
\(r\)-th smallest. In a subset with excess at most five, every cell
of weight below \(w_0-5\) is forced in, and every cell of weight
above \(w_0+5\) is forced out. Otherwise replacing the missing
smallest cell or the oversized chosen cell already costs more than
five. The intervening eleven weight levels contain at most 22 cells
by the diagonal bound after (HJ.12). Enumerate their subsets of the
required size. The cases \(r=0\) and \(r=|C_\nu|\) have a unique
subset. After the tableau and subset are fixed, the remaining coin
degree is at most five, so enumerate those partitions directly.
Check (HJ.13) and take the first \(d\) distinct complete points
in the fixed enumeration order. The proved surjection ensures
termination.

For general \(a\) of the same parity, increase each point's
weight-two coin by \((a-a_0)/2\). This injective map of complete
tableau/subset/coin data produces exactly \(d\) distinct specified
points of the stable polytope for \(a\).

For the row label there is one point to delete and \(r=0,1\).
Use HK.19's invariant-form polytope, always with least-support index
two. For \(r=0\), represent \(a\ge5\) by twos and threes, with a
single three precisely when \(a\) is odd. For \(r=1\), put
\(D=a+1\). When \(D\) is even, choose one four, subset \(\{4\}\),
and fill the remainder with twos. When \(D\) is odd, use one three,
subset \(\{3\}\), and fill the remainder with twos. The exponent
of two is always positive and every HK.19 inequality holds.

### 5. At most four successive point deletions

Start with G037's bounded polytope in \(N\) ordered variables.
For each of the at most four specified points, locate its unique
current cell by checking the literal inequalities. Replace only
that cell by the \(2N\) first-difference cells of T061 UH.10.
All other cells remain. Distinctness and disjointness ensure that
the owner exists and is unique. Induction gives a disjoint
bounded-polytope decomposition of the original lattice set minus
exactly the \(d\) points, with
\[
1+d(2N-1)\le8N-3
\tag{HJ.16}
\]
cells when \(d>0\); when \(d=0\), retain the original cell.
The copied constraints are complete matrices, so this includes
every tag and added row. No character calculation or elimination
is hidden in point selection.

The exact coefficient is G037's proved rational-series coefficient
minus the two-box path count. Its bit bound is polynomial in \(m\)
and the parameter lengths, as is (HJ.15), the constant-size subset
search, the explicit coin shift, and every polytope matrix operation.
The actual jet splitting proves that this positive count is the
requested multiplicity. This does not identify the deleted monomial
vectors with the image of that splitting: the dimension identity is
proved by (HJ.2)/(HJ.12), and its lattice-set bijection is the stated
cell partition.

The executable is second_unstable_hook_positive.py. It returns the
exact coefficient or all literal matrices and deleted points. The
two one-box steps use Macdonald I§7(7.1)–(7.3), pp112–113, and
I§5(5.16), p73, freshly checked for T061; the actual hook/Koszul
and single-polytope maps are G037. Scheme transport is G015's exact
flag map and T061's local ideal pushforward, with the same checked
EGA/SGA tensor, Schur, and rational-spreading conventions.

## Proof and computation status

The author has read all of HJ.1–HJ.16 and the complete executable.
The scalar quadratic interpolation, local finite-coordinate inverse,
horizontal degree and group action, both induced-module maps, every
bounded-excess enumeration step, and the multiple-point cell
partition passed that reading. The root agent subsequently read
the entire proof and code, and the archive agent completed the
independent A093 review; both passed. The archive narrative is
`work/archive/HIGHER_HOOK_JETS_REVIEW.md`.

The script `check_second_unstable_hook.py` passed 6,840 coefficient
comparisons for every label at \(m=4,\ldots,8\), every leg,
\(a=5,\ldots,14\), and both determinant parities. The comparison
uses original hook Jacobi–Trudi cycle traces and literal fixed-point
first-jet induction, without the small-label formula. All 342 target
multiplicity comparisons passed; the maximum correction was four.
There were 4,190 removed-point matrix validations for \(m=4,\ldots,15\)
at degrees \(5,6,7,8,10^{20}+1\). In 86 small cases the 6,766
exported polytopes partitioned 267 original witnesses into 155
retained witnesses and exactly the stated removed points.
The receipt is `SECOND_UNSTABLE_HOOK_RECEIPT.json`.

Separately, the rectangular agent compared 392 original plethysm
coefficients at \(m=4,5,6\), \(a=5,6\), all legs and both
parities, using literal Schur cycle traces and point-jet induction;
all passed. Its receipt is
`work/rectangular/SECOND_UNSTABLE_HOOK_MN_CHECK.tsv`.

The archive separately computed 12 exact finite-jet inverses at
\(m=4,5,7\), \(k=1,\ldots,4\), checking 139 basis
polynomials and 704 other-point zero jets. Its independent complete
enumerations matched 312 low-comajor tableau sets, 894 bounded-excess
subset sets and 298 parity-base point sets. These are recorded in
`work/archive/HIGHER_HOOK_JETS_INDEPENDENT_RECEIPT.json`.

Whole-proof readings and computations have separate ledger events.
T062 asserts the range \(a\ge2k+1\); T061 independently handles
its valid degree-two endpoint at \(k=1\).

