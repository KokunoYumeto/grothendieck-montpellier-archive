# A093. Full audit of the higher hook jet map and second-order positive formula

**Result: PASS.** The complete combined T062/T063 proof,
HJ.1–HJ.16 and all five construction sections, and the whole
second-order positive evaluator were read. The all-order
jet map has the stated actual equivariant right inverse.
At order two the branching count and explicit point deletions
give the claimed positive bounded-polytope formula.

Reviewed sources are
work/theta/unstable_hook/higher_hook_jets_report.md and
work/theta/unstable_hook/second_unstable_hook_positive.py.
The first-order section/pushforward map and G037 cycle
polytope are the actual constructions checked in A090
and A086 respectively.

## 1. Parameters and the complete jet sheaf

The first gap of the partition in HJ.1 is
$(m-2)a-mk-r$. At $a=2k+1$ and $r=m-2$ it is
$(m-4)k\ge0$; every other allowed parameter increases it.
The tuple has size $mn$ for $n=a+t-k$.
Its ideal order is exactly $\lambda_2-n=k$.
The exterior flag pushforward therefore gives
$\mathcal I_Z^k\otimes\mathcal O(a)\Lambda^rQ^*
=\mathcal I_Z^k\otimes\Omega^r(a+r)$, with the outside
character $\operatorname{sgn}^t$ from the full determinant
columns.

The points are disjoint and reduced. At each point their
ordinary sheaf ideal power is the maximal-ideal power.
The kernel of restriction to order-less-than-$k$ jets is
therefore exactly the displayed sheaf section space.
The T061 product-chart pushforward argument remains valid
after tensoring its vector-space Čech maps with this ideal
module. No flatness of the ideal module is assumed.

## 2. Every quadratic derivative and its actual inverse

After a projective frame change, the points are the
coordinate points of a space of dimension $m-1$ and
the all-ones point. The quadrics
$x_jx_l-x_1x_2$, omitting the zero member, are precisely
the spanning presentation from G016.

At a coordinate point $e_h$ with $h>2$, the pairs $(h,j)$
give all transverse coordinate derivatives. At $e_1$,
the pairs $(1,j)$ and $(2,j)$, $j\ge3$, give
$dx_j-dx_2$ and $-dx_2$, hence every transverse direction.
The calculation at $e_2$ is its exchanged version.
At the all-ones point the derivatives are
$dx_j+dx_l-dx_1-dx_2$. Taking the pairs $(1,j)$ and
$(2,j)$ gives every difference relative to coordinates
one and two, including their difference. They span the
full sum-zero projective cotangent space. This works
already with three affine coordinates, so includes $m=4$.

Changing to the specified chart $\ell_i=1$ only changes
these differentials by the invertible coordinate map
and a nonzero trivialization factor, since the quadrics
vanish at the point. Thus HJ.4 is the actual surjective
derivative map at every frame point.

Its Gram right inverse
$\partial_i^*(\partial_i\partial_i^*)^{-1}$ is rational.
The invariant positive forms make the inverse well
defined after extension to $\mathbb R$, hence over
$\mathbb Q$ as the inverse of a rational nonsingular
matrix. Both forms and the chart are fixed by the point
stabilizer, so the inverse is stabilizer-equivariant.
Literal frame permutations carry one such map to another.

## 3. The all-order simultaneous interpolation

The separators $p_i$ have value one at their own affine
frame vector and zero at all others, as checked in A090.
For $f_h=\sigma_i(u_h)$, the quotient $y_h=f_h/p_i$
has zero constant term and linear term $u_h$ on the
chart $\ell_i=1$. Hence it gives an automorphism of
the truncated local algebra. Its inverse is obtained
by successively removing homogeneous terms of orders
one through $k-1$; all maps are finite rational
polynomial substitutions.

For each multiindex $|\beta|<k$, the polynomial
$$
p_i^{\,k-|\beta|}\prod_h f_h^{\beta_h}
$$
has homogeneous degree $2k$. At its own point it is
$p_i^k y^\beta$, and multiplication by $p_i^k$ is a
unit on the finite local algebra. These jets thus form
a basis. At every other point every displayed factor
is in its maximal ideal, and their total number,
counting multiplicity, is exactly $k$. Consequently
the polynomial has order at least $k$ at that point.
This proves simultaneous scalar jet interpolation.

For $\phi\in\Lambda^r\operatorname{ann}(v_i)$, the form
$H_i(\phi)=\iota_z(\ell_i\wedge\phi)$ has coefficient
degree one and is horizontal. On $\ell_i(z)=1$, it is
$$
\phi-\ell_i\wedge\iota_z\phi.
$$
Restriction to $W_i=\ker\ell_i$ is exactly $\phi$.
Every horizontal form is uniquely determined by that
restriction, because $E=\mathbb Qz\oplus W_i$ on
this chart. This proves the bundle trivialization
and its inverse, including $r=0$ and the top exterior
degree.

Multiplying each scalar interpolator by $H_i(\phi)$
and by $\ell_i^{a-2k-1}$ gives a global horizontal
form of coefficient degree $a$. The exponent is
nonnegative in the proved range. Its local form-valued
jet basis is the scalar basis times the fixed exterior
basis, and its other-point jets vanish.
The finite coordinate inverse, the unit inverse and
the horizontal restriction supply the actual right
inverse of restriction.

The construction is independent of a chosen coordinate
basis when expressed by symmetric powers of $\sigma_i$.
The coordinate substitution and its unique finite
inverse are equivariant, as is multiplication by the
stabilizer-fixed unit $p_i^k$. Summing the local maps
over the frame orbit gives an $S_m$-equivariant rational
right inverse.

The stabilizer acts linearly on the chart centered at
its fixed affine vector. Its entire truncated Taylor
algebra, not just its associated graded, is
$\bigoplus_{j<k}\operatorname{Sym}^jW_i^*$.
The horizontal frame is $\Lambda^rW_i^*$, and the
fixed vector trivializes the homogeneous line with
no scalar character. The invariant dot forms identify
these duals with $\mathfrak h_{m-1}$.
This proves exactly the induced target and split
sequence in HJ.2, including every linearization.

## 4. Order-two correction and its bounded branching

At $k=2$, the Taylor factor is the literal permutation
module $\mathbb Q\oplus\mathfrak h_{m-1}$.
The coset tensor map
$g\otimes(hL\otimes v)\mapsto gh\otimes h^{-1}v$
respects both the $K$-relations and the $L$-relations:
changing the intermediate representative transfers
the same inverse action to $v$. Its inverse on each
coset summand gives the displayed isomorphism.

On $S_{m-2}$ the standard module of $S_{m-1}$ splits
as its standard module plus the invariant line with
coordinates $(1,\ldots,1,-(m-2))$. Exterior powers
therefore give exactly the two hooks
$(q-1,1^r)$ for $q\ge2$ and
$(q,1^{r-1})$ for $r\ge1$.
Two successive one-box Young maps give the stated
path multiplicity.

For a fixed starting hook and final diagram, the two
new boxes have at most two orders. There are at most
two starting hooks, so the multiplicity is at most
four. The row label can occur only from a starting
row; this happens once for $r=0$ and once for $r=1$,
and not otherwise. A hook with only two new boxes
cannot contain a three-by-three square; its Durfee
size, and therefore the length of every diagonal,
is at most two. All extreme hook legs are covered
by the explicitly omitted zero exterior powers.

The actual split jet sequence proves the exact
subtraction of these zero-to-four multiplicities
from the stable hook module, with the same determinant
parity. The primary one-box induction/Pieri passages
used here were checked in A090; no new source read
is claimed for that repeated use.

## 5. Completeness of the small-excess search

For a non-row affected label, the numerator minimum
$L$ is the row-superstandard comajor degree plus
the least retained-cell weight sum. The positive
G037 series has constant-one denominator.
The Koszul kernel has no total degree at most $r$:
negative polynomial degree is absent, and a constant
positive-degree exterior form annihilated by every
coordinate contraction is zero; at $r=0$ the cycle
convention is $P_+$. Thus $L\ge r+1$.

Choose the parity base $a_0=5$ or $6$. Surjectivity
of the just-proved jet map gives at least the required
$d\le4$ lattice points at this base. Every such point
has numerator and coin excess at most
$a_0+r-L\le5$.

The semistandard enumeration is complete. The minimal
semistandard filling of a standard tableau puts at
label $j$ the number of earlier descents. Its total
entry sum is comajor. It is weak along rows and
strict down columns: between two labels in the
same column there must be a descent, since otherwise
the row indices could never increase. Its entries
are at least the row index minus one.
Within an equal-entry run, labels move weakly upward
and strictly rightward, so ordering ties left to
right recovers the original tableau. Thus the
increment arrays of total at most five contain
every needed tableau. Their number is bounded by
$\binom{m+5}{5}$.

For the retained subset, write $w_0$ for the
$r$th smallest weight. Omitting a cell of weight
below $w_0-5$ forces replacement by a cell of
weight at least $w_0$, costing more than five.
Choosing a cell above $w_0+5$ similarly forces
omission of a smaller one at cost more than five.
The remaining eleven diagonal weights contain
at most 22 cells. Their subset enumeration has
a constant upper bound independent of $m$.
The cases $r=0$ and full retained subset are
handled separately and uniquely. All remaining
coin degrees are at most five.

Tableau standardization removes duplicates; the
subset and coin enumerations themselves have no
duplicates. Hence taking the first $d$ complete
points is well defined and terminates by the
proved evaluation surjection.
Adding $(a-a_0)/2$ to each weight-two coin is
injective on these points and satisfies the new
degree equation and upper bound.

For the row label, the two displayed elementary
coin constructions have positive weight-two
exponent. At $r=1$, the chosen further support
index is four in even total degree at least six
and three in odd total degree at least seven.
The G037 least-support and subset constraints
hold at every endpoint.

## 6. Sequential owner cells and executable bounds

Each specified point is an integer point of the
original bounded polytope and is distinct from
earlier deleted points. The current cells partition
the remaining integer points, so it has one owner.
Replacing only that owner by its two first-difference
pieces for each coordinate removes exactly that
point and preserves the disjoint lattice partition.
After $d$ deletions the number of cells is
$1+d(2N-1)\le8N-3$.
All retain the original bounded inequalities.

The code implements the two starting hooks and
both box additions, the semistandard enumeration,
the bounded diagonal window, the parity shift,
and the unique-owner replacement literally.
Its constraints preserve the complete previous
cell before appending prefix equalities and the
new offset inequality.
The total output and bit length are polynomial
in the stated explicit-$m$ and binary parameters.
The coefficient evaluator uses the already proved
stable coefficient and the finite path count.
The positive interpretation follows from the
exact split sequence and the disjoint lattice
deletions. No matrix-rank conjecture is used.

## 7. Focused independent execution

The fresh implementation
work/archive/check_higher_hook_jets_independent.py
and receipt
work/archive/HIGHER_HOOK_JETS_INDEPENDENT_RECEIPT.json
record the following actual executions.

In a frame $e_1,\ldots,e_{m-1},-\sum e_i$, the
cross-quadrics and a derivative right inverse were
constructed independently with exact rational
arithmetic. At $m=4,5,7$ and $k=1,2,3,4$, all
12 resulting jet-coordinate matrices were inverted
and their products with the inverses checked.
The 139 basis polynomials give the identity
associated leading matrix at their own point.
All 704 other-point truncated jets are exactly zero.
This comparison constructs the scalar interpolation
map directly; the all-leg horizontal trivialization
was checked algebraically in §3.

For affected shapes at $m=4,\ldots,8$, all standard
tableaux were independently generated by removable
corners and filtered by their literal comajor.
All 312 complete low-comajor sets agree with the
semistandard search output. Exhaustive retained-cell
subsets give 894 complete low-subset sets agreeing
with the diagonal-window search. All 298 resulting
parity-base point sets have the required cardinality
and literal witnesses.

No original plethysm comparison sweep was rerun.
The finite checks test the newly proved interpolation
and bounded search mechanisms; the all-order
surjectivity and order-two polynomial bound follow
from their full proofs above.

## 8. Geometry and scope

The point ideal powers, bundle-valued jets, homogeneous
polynomial lifts and flag pushforwards are explicit
equivariant sheaf maps on the same projective frame
model. Their rational sections and Young/coset
maps supply the claimed module and K0 transport
through the already verified archive/EGA/SGA
dictionary. They spread after inverting their
finite denominators, with the asserted coefficient
theorems on the characteristic-zero fiber.

T062 proves its exact split sequence for every
$a\ge2k+1$. T063 proves its positive small-polytope
conversion for all $k=2,a\ge5$. Those stated
conclusions and the code have no remaining
mathematical gate in this audit.
