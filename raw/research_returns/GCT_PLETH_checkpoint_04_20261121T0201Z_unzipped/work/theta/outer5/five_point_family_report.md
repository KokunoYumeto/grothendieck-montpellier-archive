# A positive higher-flag family in outer degree five

## T-039. The coefficient formula

For integers \(a,d\ge0\), set
\[
n=d+a+1,\qquad
\lambda=(d+2a+3,\ d+a+2,\ d+a,\ d+a,\ d).
\tag{5F.1}
\]
This is a partition of \(5n\). Let \(E=\mathfrak h_5\),
\(U=[3,2]\), and \(\epsilon=\operatorname{sgn}_{S_5}\). There is an
actual equivariant isomorphism
\[
\boxed{
(S_\lambda\mathbf Q^5)_{(n^5)}
\simeq\epsilon^{d+a}\otimes
\left(U\otimes\operatorname{Sym}^a E
\;\oplus\;\operatorname{Sym}^{a-1}E\right),}
\tag{5F.2}
\]
where \(\operatorname{Sym}^{-1}E=0\). The direct sum is a splitting of a
specified equivariant short exact sequence; it need not be a canonical
splitting. Consequently every outer Schur coefficient
\(p_{\mu,(n)}^\lambda\), \(\mu\vdash5\), is a sum of at most 36
fixed, four-variable lattice-point counts. The numbers and inequalities
are specified in §4 below. There is no coefficient precomputation depending
on \(a\), \(d\), or \(n\).

The passage from the balanced weight space to (5F.2) is the polynomial
chart and extension morphism of T-032/G-015, followed by explicit exterior
pairings and the exact resolution (5R.3). We prove each remaining step.

## 1. From the flag model to a quotient-bundle section

Use the canonical \(S_5\)-invariant form on \(E\) to identify \(E\)
and \(E^*\). On \(\mathbf P(E)\), which parametrizes lines, let
\[
0\longrightarrow\mathcal O(-1)\longrightarrow E\otimes\mathcal O
\longrightarrow Q\longrightarrow0
\tag{5F.3}
\]
be the tautological quotient sequence. Thus \(Q\) has rank three. Let
\(Z=\{[e_i-\frac15\mathbf1]:1\le i\le5\}\), and write
\(\mathcal I=\mathcal I_Z\).

The numbers in (5F.1) satisfy
\[
\lambda_2-n=1,\qquad \lambda_2-\lambda_3=2,
\qquad\lambda_3-\lambda_4=0,\qquad\lambda_3-\lambda_5=a.
\tag{5F.4}
\]
G-015 therefore identifies the balanced module with
\[
H^0\!\left(\operatorname{Flag}(E),
\mathcal L_{(d+a+2,d+a,d+a,d)}\otimes\pi^*\mathcal I\right),
\tag{5F.5}
\]
where \(\pi\) remembers the first line. This is the actual comparison
map: a flag polynomial \(F\) is sent back to the original matrix ring by
\(u^{-1}F(v(X))\). G-015 proves that membership in (5F.5) is precisely
what makes this rational expression a polynomial, using the exact
transverse ratios along every first-column coordinate divisor.

We describe the pushforward in (5F.5), including all determinant factors.
The full determinant factor of \(\mathcal L\) is
\((\det E^*)^d\). After removing it, the first weight is \(a+2\)
and the relative quotient-flag weight is \((a,a,0)\). The standard
Plücker evaluation on the flag of the rank-three quotient gives
\[
\pi_*\mathcal L_{(d+a+2,d+a,d+a,d)}
\simeq (\det E^*)^d\otimes\mathcal O(a+2)
                  \otimes S_{(a,a)}Q^*.
\tag{5F.6}
\]
The relative identification can be checked on every open set trivializing
\(Q\): there it is the usual Schur realization by the degree-\((a,a)\)
flag minors, and changes of quotient frame act by that same Schur functor.
The local maps therefore glue. This is the Borel–Weil/Schur comparison in
Magyar, Proposition 1, printed pp. 5–6, and Proposition 4(a)–(c), printed
p. 10, with the bundle linearization specified by its exterior columns.

For a rank-three vector space or bundle, the wedge pairing is the actual
map
\[
\Lambda^2Q^*\simeq Q\otimes\det Q^*.
\tag{5F.7}
\]
Its \(a\)-th symmetric power identifies
\(S_{(a,a)}Q^*=\operatorname{Sym}^a(\Lambda^2Q^*)\) with
\((\det Q^*)^a\otimes\operatorname{Sym}^aQ\). The asserted equality
with the Schur functor follows as well from the map on the highest vector
\((q_1^*\wedge q_2^*)^a\): its irreducible span has weight \((a,a,0)\)
and the dimensions on both sides are \(\binom{a+2}{2}\). Taking
determinants in (5F.3) gives
\[
\det Q^*\simeq\det E^*\otimes\mathcal O(-1).
\tag{5F.8}
\]
Thus (5F.6) becomes
\[
\pi_*\mathcal L\simeq
(\det E^*)^{d+a}\otimes\mathcal O(2)\otimes\operatorname{Sym}^aQ.
\tag{5F.9}
\]

Projection with the ideal factor causes no hidden flatness assumption.
Locally on the base, the flag bundle is a product with the fixed flag
variety. A finite affine Čech complex for its line bundle consists of
modules obtained from vector spaces over \(\mathbf Q\), tensored with
the base ring. Tensoring this complex with the local ideal commutes with
its degree-zero cohomology: every exact sequence of vector spaces over
\(\mathbf Q\) splits. These local maps agree on overlaps. Equivalently
one can use the usual relative Schur section map and its base-change
property. Hence (5F.5)–(5F.9) give the specified isomorphism
\[
\boxed{
(S_\lambda\mathbf Q^5)_{(n^5)}
\simeq \epsilon^{d+a}\otimes
H^0(\mathbf P(E),\mathcal I(2)\otimes\operatorname{Sym}^aQ).}
\tag{5F.10}
\]
Here \(\det E=\epsilon\), because the full five-dimensional permutation
module is \(\mathbf1\oplus E\). This determines the twist directly.

## 2. The three bundle cohomology calculations

Write \(B_a=\operatorname{Sym}^aQ\). Multiplication by the tautological
line in (5F.3) is the first map of the exact sequence
\[
0\longrightarrow\mathcal O(t-1)\otimes\operatorname{Sym}^{a-1}E
\longrightarrow\mathcal O(t)\otimes\operatorname{Sym}^{a}E
\longrightarrow B_a(t)\longrightarrow0.
\tag{5F.11}
\]
The sequence is exact fiber by fiber: the kernel of
\(\operatorname{Sym}^aE\to\operatorname{Sym}^a(E/L)\) is exactly
\(L\operatorname{Sym}^{a-1}E\), and multiplication by a nonzero vector
of the line \(L\) is injective in a symmetric algebra. It is therefore
an exact sequence of locally free sheaves. For \(a=0\), its left term
is zero.

The projective-space cohomology used here is
\[
H^i(\mathbf P^3,\mathcal O(t))=0\quad(0<i<3),
\]
with \(\mathcal O(-1),\mathcal O(-2),\mathcal O(-3)\) acyclic and
\(H^3(\mathcal O(-4))=\det E\). The scalar vanishing ranges follow
from the full monomial Čech calculation in Stacks Project, Lemma 30.8.1,
tag 01XS. The determinant action can be read from its top Čech generator:
for an ordered coordinate basis \(x_1,\ldots,x_4\), it is the class of
\(1/(x_1x_2x_3x_4)\); the ordered Čech orientation and change of basis
make its action \(\det E\). The same conclusion follows from the
canonical-bundle identification
\(\omega_{\mathbf P(E)}=\mathcal O(-4)\otimes\det E^*\).

Apply (5F.11) with \(t=0,-1,-3\). It gives all the following groups,
not merely their Euler characteristics:
\[
\begin{array}{c|c|c}
\text{bundle}&\text{only possible nonzero cohomology}&\text{module}\\\hline
B_a&H^0&\operatorname{Sym}^aE\\
B_a(-1)&\text{none}&0\\
B_a(-3)&H^2&\epsilon\otimes\operatorname{Sym}^{a-1}E.
\end{array}
\tag{5F.12}
\]
The last row is zero when \(a=0\), as required.

## 3. The positive exact sequence

Sheafify the exact resolution (5R.4), twist by \(\mathcal O(2)\), and
tensor with the locally free sheaf \(B_a\). This gives
\[
0\longrightarrow\epsilon\otimes B_a(-3)
\longrightarrow(\epsilon\otimes U)\otimes B_a(-1)
\longrightarrow U\otimes B_a
\longrightarrow\mathcal I(2)\otimes B_a\longrightarrow0.
\tag{5F.13}
\]
Let \(K\) be the image of its middle map into \(U\otimes B_a\).
The first short exact sequence and (5F.12) give
\[
H^0(K)=0,\qquad
H^1(K)=\operatorname{Sym}^{a-1}E,
\qquad H^i(K)=0\ (i\ge2).
\tag{5F.14}
\]
The two sign factors in \(H^1(K)\) are the last syzygy character of
(5R.4) and the top projective cohomology character of (5F.12); their
tensor product is trivial. The second short exact sequence therefore
gives
\[
\boxed{
0\longrightarrow U\otimes\operatorname{Sym}^a E
\longrightarrow H^0(\mathcal I(2)\otimes B_a)
\longrightarrow\operatorname{Sym}^{a-1}E
\longrightarrow0.}
\tag{5F.15}
\]
The first arrow multiplies a quadratic vanishing at \(Z\) by a constant
section of \(\operatorname{Sym}^aE\), followed by the quotient
\(\operatorname{Sym}^aE\to B_a\). The last arrow is the connecting
homomorphism of the actual resolution. This specifies the morphisms
underlying the positive decomposition.

Every sequence of finite-dimensional \(\mathbf Q[S_5]\)-modules splits:
average any linear section over the 120 group elements. Applying this
to (5F.15) and composing with (5F.10) proves (5F.2). It also proves
\[
\dim(S_\lambda\mathbf Q^5)_{(n^5)}
=5\binom{a+3}{3}+\binom{a+2}{3}.
\tag{5F.16}
\]
The equality for \(a=0\) is the single module \(U\), with no extra
cohomology term.

## 4. Fixed positive polytopes for every outer partition

Define the bounded rational polytope
\[
P(R)=\{(x_2,x_3,x_4,x_5)\in\mathbf R_{\ge0}^4:
2x_2+3x_3+4x_4+5x_5=R\},
\qquad C(R)=\#(P(R)\cap\mathbf Z^4).
\tag{5F.17}
\]
For \(R<0\) it is empty. Every integer coordinate is at most
\(\max(0,R)/2\), so no unbounded component is being counted.

The seven multisets below are the comajor indices of standard tableaux
of the indicated shape. For a tableau of size five, our convention is
\(\operatorname{comaj}T=\sum_{i:\,i+1\text{ is below }i}(5-i)\).
Repeated entries are distinct tableau tags.

| \(\rho\) | multiset \(D_\rho\) | dimension |
|---|---|---:|
| \((5)\) | \(0\) | 1 |
| \((4,1)\) | \(1,2,3,4\) | 4 |
| \((3,2)\) | \(2,3,4,5,6\) | 5 |
| \((3,1,1)\) | \(3,4,5,5,6,7\) | 6 |
| \((2,2,1)\) | \(4,5,6,7,8\) | 5 |
| \((2,1,1,1)\) | \(6,7,8,9\) | 4 |
| \((1^5)\) | \(10\) | 1 |

The exact standardization argument of T-027 gives
\[
\dim\operatorname{Hom}_{S_5}([\rho],\operatorname{Sym}^aE)
=\sum_{r\in D_\rho}C(a-r).
\tag{5F.18}
\]
In that proof, weak entries in a semistandard tableau become a standard
tableau plus nonnegative increments, and the forced strict inequalities
contribute precisely its comajor. The constant-line factor in the
permutation module removes the denominator of degree one, leaving the
four denominators \(2,3,4,5\) in (5F.17). Thus (5F.18) has an actual
tableau-to-lattice bijection. Here all tableau tags are already listed.

Let \(K_{\rho\nu}\) be the multiplicity of \([\nu]\) in
\(U\otimes[\rho]\). It is completely specified by the following table;
repetition denotes multiplicity two.

| \(\rho\) | summands of \(U\otimes[\rho]\) |
|---|---|
| \((5)\) | \((3,2)\) |
| \((4,1)\) | \((4,1),(3,2),(3,1,1),(2,2,1)\) |
| \((3,2)\) | \((5),(4,1),(3,2),(3,1,1),(2,2,1),(2,1,1,1)\) |
| \((3,1,1)\) | \((4,1),(3,2),(3,1,1),(3,1,1),(2,2,1),(2,1,1,1)\) |
| \((2,2,1)\) | \((1^5),(2,1,1,1),(2,2,1),(3,1,1),(3,2),(4,1)\) |
| \((2,1,1,1)\) | \((2,1,1,1),(2,2,1),(3,1,1),(3,2)\) |
| \((1^5)\) | \((2,2,1)\) |

This finite tensor table follows by multiplying the seven character rows
of the primary Table 1 quoted in T-038 and taking the class-size-weighted
inner products. In particular it requires no variable-size Kronecker
coefficient computation. All 49 entries were also recomputed by an
independent Murnaghan–Nakayama implementation.

For \(\mu\vdash5\), put
\[
\nu=\begin{cases}\mu&d+a\text{ even},\\\mu^t&d+a\text{ odd}.
\end{cases}
\tag{5F.19}
\]
Taking the \([\mu]\)-covariant part in the balanced-space dictionary
T-003 and then using (5F.2) and (5F.18) yields
\[
\boxed{
p_{\mu,(n)}^\lambda
=\sum_{\rho\vdash5}K_{\rho\nu}
       \sum_{r\in D_\rho}C(a-r)
 +\sum_{r\in D_\nu}C(a-1-r).}
\tag{5F.20}
\]
Each summand has a fixed tag \((\rho,\text{copy},\text{tableau})\) or
\((\nu,\text{tableau})\), followed by one point of (5F.17). This is a
finite disjoint union of bounded lattice polytopes. Negative right sides
give empty polytopes and may be retained in the uniform list.

All these modules are self-dual. Hence
\(\sum_\rho K_{\rho\nu}\dim[\rho]=5\dim[\nu]\), by the dimension
of \(U\otimes[\nu]\). The second sum has \(\dim[\nu]\) tags. The
total number is exactly \(6\dim[\nu]\le36\), including empty tags.
Each polytope has four variables, one displayed equality, and four
nonnegativity inequalities. Its coefficients are fixed and its right
side has \(O(\log(a+2))\) bits. This gives a fixed-dimensional positive
formula in the ordinary binary input encoding for \(a,d\).

## 5. The symmetric outer power and its complete support criterion

For \(\mu=(5)\), (5F.20) is particularly short:
\[
\boxed{
p_{(5),(n)}^\lambda=
\begin{cases}
\displaystyle\sum_{j=1}^{6}C(a-j),&d+a\text{ even},\\[2mm]
\displaystyle\sum_{j=4}^{8}C(a-j)+C(a-11),&d+a\text{ odd}.
\end{cases}}
\tag{5F.21}
\]
Both lists have six tags. The numerical semigroup generated by
\(2,3,4,5\) is \(\{0\}\cup\{r:r\ge2\}\): every even \(r\ge2\)
uses twos and every odd \(r\ge3\) uses one three and twos. Therefore
\[
\boxed{
p_{(5),(n)}^\lambda>0
\quad\Longleftrightarrow\quad
\begin{cases}
a\ge1,&d+a\text{ even},\\
a\ge4,&d+a\text{ odd}.
\end{cases}}
\tag{5F.22}
\]
To check the endpoints explicitly, in the first case \(a=1\) uses the
tag \(j=1\), and \(a=2\) uses \(j=2\); larger \(a\) use either a
zero residual or a residual at least two. In the second case the tags
\(j=4,5\) handle \(a=4,5\), and \(j=4\) handles every \(a\ge6\).
Below these thresholds all listed right sides are negative.

## 6. Exact implementation, independent checks, and scope

`five_point_positive.py` is a standalone Python standard-library
evaluator. It contains exactly the two fixed tables above, exports the
tagged equations, and enumerates their integer witnesses. It accepts
\(a,d,\mu\), checks that \(a,d\) are nonnegative integers and that
\(\mu\) is a partition of five, and returns (5F.1) and (5F.20).
For example:

```text
python work/theta/outer5/five_point_positive.py --a 4 --d 0 --outer 5 --polytopes
```

The implementation uses the positive coin recurrence for evaluation;
its polytope description has fixed size, regardless of that elementary
counting implementation. No character, elimination, or plethysm oracle
is called by the evaluator.

`check_five_point_positive.py` recomputed all seven tableau degree lists,
all 49 tensor entries, the seven exact rational character identities
behind (5F.18), and every equivariant resolution numerator of T-038.
It also compared the positive count with literal tagged lattice
enumeration in 434 cases, producing 118,334 explicit witnesses. Every
check passed. Receipts: `FIVE_POINT_POSITIVE_CHECK.tsv` and `.txt`.

Independently, the rectangular agent computed all seven outer Schur
cycle indices and used Murnaghan–Nakayama on the output partitions.
All 147 cases with \(a,d\ge0\), \(d+a+1\le6\), matched (5F.2).
On the proposed side, that calculation used permutation-cycle traces
for \(\operatorname{Sym}^a\mathfrak h_5\) and the character
\(\binom{m_1}{2}+m_2-m_1\) for \([3,2]\), independently of the
resolution and the fixed tag table. Code and receipt:
`work/rectangular/verify_outer5_fivepoint_family.py` and
`work/rectangular/OUTER5_FIVEPOINT_INDEPENDENT_CHECK.tsv`.

The same independent reader subsequently read the complete T-038 and
T-039 proofs, including every bundle map, the two sign cancellations,
the finite tag lists and all support endpoints, and found no gap.

Primary sources read for this proof:

- [Magyar, *A Borel–Weil Construction for Schur Modules*](https://arxiv.org/pdf/alg-geom/9411014),
  Proposition 1, printed pp. 5–6, and Proposition 4(a)–(c), printed p. 10.
  The exterior-column comparison fixes the precise dual convention in
  (5F.6); the maps (5F.7)–(5F.9) then determine all twists.
- [Stacks Project, Lemma 30.8.1, tag 01XS](https://stacks.math.columbia.edu/tag/01XS),
  including its monomial Čech proof. Only the three exact bundle
  cohomology computations in (5F.12) are imported from these scalar
  vanishings.
- [Dolgachev–Farb–Looijenga, *Geometry of the Wiman–Edge pencil I*](https://www.math.uchicago.edu/~farb/papers/wiman.pdf),
  §2.3, Table 1, printed p. 10, for the fixed \(S_5\) labels and table.

For \(a>0\), the section space in (5F.10) has the nontrivial quotient
bundle \(\operatorname{Sym}^aQ\), and (5F.15) evaluates it in full.
The result is an explicit bounded family within the general
projective-frame model. It makes no global novelty claim and assumes
no vanishing for arbitrary point powers or arbitrary Schur quotient
bundles. G-010 provides the general terminating positive count; T-037
already gives a fixed finite formula for every outer partition of four.
