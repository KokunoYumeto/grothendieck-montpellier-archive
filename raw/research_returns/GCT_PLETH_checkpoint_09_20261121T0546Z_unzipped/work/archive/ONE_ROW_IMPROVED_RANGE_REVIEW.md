# A094. One-row-earlier actual canonical range in arbitrary width

**Result: PASS.** The complete R048 report, OI.1–OI.21
and all six sections, and its finite verification script
were read. The general Pfaffian highest-vector proof,
the actual last-layer restriction, the ordinary moment
comparison and the nonzero varying-width family all check.

Reviewed files are
work/rectangular/one_row_improved_canonical_range.md and
work/rectangular/verify_one_row_improved_stability.py.
The exact R046 factorization and R047 layer comparison
are the maps independently checked in A089 and A091.

## 1. The entire omitted row layer

The two stated families have matching parity of size
$D$ and width $t$, with $t\ge2$. Set
$N=(D+t)/2$ and $M=N-1$.
In the actual ordered-row exterior decomposition,
a degree-$D$ term occupying $N$ rows satisfies
$$
D\ge2N-e_1\ge2N-t=D.
$$
Equality forces all $t$ singleton factors and only
degree-two factors in every other occupied row.
Their exact module is
$$
L=\det T\otimes
\operatorname{Sym}^{(D-t)/2}(\Lambda^2T),
\qquad T=\mathbb Q^t.
$$
At every lower scalar degree the occupancy bound is
at most $M$, using the matching parity. Thus the
literal decomposition
$C_s=\Lambda T\otimes B_s$ and degree induction
give this same complete difference for $B_N$ and
$B_M$ at degree $D$.

The orthogonal transpose $q:W_N\to W_M$ of zero-padding
has the displayed values on the centered basis vectors.
Every exterior row power sum maps with scalar one,
so the complete orbit spanning argument makes the
actual map $B_N\to B_M$ surjective. Its kernel
therefore has exactly character $L$.
This identifies the module whose constituents must
be excluded; no kernel rank is inferred merely
from equality of the original plethysm coefficients.

## 2. General Pfaffian highest maps, including action conventions

In the abstract polynomial algebra
$\operatorname{Sym}(\Lambda^2T)$, the variable
$X_{ij}$ represents $e_i\wedge e_j$.
For a matrix acting on basis columns, its action
on the alternating matrix of these variables is
$A\mapsto u^tAu$. In particular an upper unipotent
matrix preserves the span of its first $2i$
columns with determinant one. Each leading
Pfaffian $P_i$ is consequently a highest polynomial
of weight $(1^{2i},0^{t-2i})$. On the displayed
alternating blocks it is $z_1\cdots z_i$, with
the sign convention in OI.9.

The exact block multiplication was checked:
for
$A=\left(\begin{smallmatrix}J&B\\-B^t&C\end{smallmatrix}\right)$
and
$u=\left(\begin{smallmatrix}I&-J^{-1}B\\0&I\end{smallmatrix}\right)$,
$$
u^tAu=\operatorname{diag}(J,C+B^tJ^{-1}B).
$$
The plus sign follows from $J^{-t}=-J^{-1}$.
The lower block is alternating. The matrix $u$
is upper unipotent in the original ordered basis.
Repeated elimination is therefore an allowed
highest-weight group operation, with denominators
nonzero on the specified open set.

This open set is nonempty, as witnessed by nonzero
alternating blocks, and hence is dense in the
generic alternating matrix space. Successive
leading Pfaffians give the block parameters
$z_i=P_i/P_{i-1}$. For odd dimension the final
one-dimensional alternating block is zero.

A highest polynomial is invariant under these
upper unipotent substitutions. Its restriction
to the blocks determines it on the dense open
set. A diagonal-weight vector restricts either
to zero or to one scalar monomial
$z_1^{c_1}\cdots z_r^{c_r}$, because those
variables have independent paired torus weights.
Polynomiality gives nonnegative integer exponents;
dominance gives $c_1\ge\cdots\ge c_r$.
The product
$P_1^{c_1-c_2}\cdots P_r^{c_r}$
has exactly the same restriction and weight.
Subtracting it leaves a highest polynomial
vanishing on a dense open set, hence zero.

Thus every possible paired weight occurs once
and no other highest weight occurs. The explicit
products and rational Young/cyclic Schur maps
give the actual decomposition OI.8 by complete
reducibility. The proof covers both parities
of $t$, including $t=2$ and $3$.

## 3. The precise parity exclusion and faithful ordinary map

Write $\gamma=\nu^t$, with exactly $t$ positive
parts. At even $t$, the determinant shift of
OI.8 has exactly the constituents whose adjacent
part pairs of $\gamma$ are equal. At odd $t$,
it has those equal pairs and final part one.
Their sizes already equal $D$; subtracting
the determinant leaves a nonnegative paired
shape, so these conditions are sufficient
as well as necessary.

The gap $\gamma_i-\gamma_{i+1}$ is the number
of parts of $\nu$ equal to $i$. Therefore at
even width the omitted layer requires no odd
part at all. At odd width it requires exactly
one odd part, equal to the maximum part $t$.
The theorem's two families have respectively
at least two or at least three odd parts,
and their required Schur factor is absent.

The actual skew-Cauchy multiplicity map is
$S_\nu(q)$, so it is an isomorphism at the
new boundary. R046 supplies the same conclusion
for all larger row counts. Ordinary and
exterior realizations use the same tensor
Young projectors, which commute with $q^{\otimes D}$.
Choosing a sufficiently large row count where
the ordinary power-sum map is an isomorphism
then proves
$p_s=S_\nu(q)p_S$ on the exact component.
Thus the particular ordinary evaluation
in OI.14 is an isomorphism for every $s\ge M$.
This statement is independent of auxiliary
rank once that rank supports $S_\nu$.

Both allowed families satisfy $D\ge t+2$:
at even width two odd parts accompany the
largest even part, and at odd width two
additional odd parts accompany a largest
odd part. Hence $M\ge t$. This checks all
falling-factorial denominators and the
separate row-degree extension at the new
boundary.

## 4. The actual normalized canonical map

The highest-space chart and its inverse
homogenization are exactly those of R046.
The column antisymmetrizer bounds each
row degree by $t$, so all invariants extend
when $n\ge M\ge t$.

The opposite canonical map is the same
specified composition
$$
h_{a,n}|_\nu=p_n\Psi_n E_a.
$$
Independent-row polarization $E_a$ is
injective after the proved normalization
and recentering of the functional.
The split-moment substitution is the
full equality-partition Möbius sum with
its labeled tensor positions. Its
one-block coefficient is
$(-1)^{d-1}(d-1)!/(n)_d$ in degree $d$,
and all remaining terms use lower-degree
generators. For every $2\le d\le t$
this is nonzero in the stated range,
so the substitution is an invertible
equivariant triangular algebra map.
Finally, the exact $p_n$ is faithful
by §3.

This gives injectivity of the actual
opposite map on the complete multiplicity
space. The scalar-one transpose pairing
therefore proves full surjectivity of
$h_{n,a}$, not just a comparison of
dimensions. With both parameters at least
$M$, the proof applies in both directions
and gives the asserted isomorphism and
formal moment multiplicity.

## 5. Nonzero varying-width family

The polynomial from R040 has exact
highest weight $(4,3,1)$, is invariant
under translations and row permutations,
and is nonzero for every $a\ge5$.
The complementary-minor formula in
OI.20 agrees with the previously
checked HC.7–HC.14 polynomial; it
extends across singular covariance
matrices because its alternating
inverse expression is a signed minor.

The centered power sums $P_2$ and
$P_3$ are nonzero invariant highest
polynomials of weights $(2)$ and
$(3)$. For example, centered first
coordinates $(1,-1,0,\ldots)$ show
$P_2\ne0$, and $(1,1,-2,0,\ldots)$
show $P_3\ne0$. The centered polynomial
algebra is a domain, so their products
with the displayed nonzero vector
are nonzero. Raising operators are
derivations, proving the required
highest weights $(w,3,1)$.

Even $w\ge4$ uses the appropriate
power of $P_2$; odd $w\ge7$ first
uses $P_3$. These cover exactly the
stated $w=4$ or $w\ge6$ range.
Their row degree is at most $w$,
so they homogenize at $n\ge w+1$.
In both parities $D=w+4$ and
$M=w+1$. The explicit first-row
bound $an-w-4\ge4w+1\ge w$ gives
valid partitions. Applying the
actual canonical range to these
vectors proves the claimed nonzero
image in every supporting dimension.

## 6. Executed independent checks and exact receipt scope

The fresh program
work/archive/check_one_row_pfaffian_independent.py
and receipt
work/archive/ONE_ROW_PFAFFIAN_INDEPENDENT_RECEIPT.json
import no source implementation.

Twenty-seven rational alternating-matrix
examples in dimensions two through ten
were constructed on the specified chart.
The complete upper-unipotent elimination,
its accumulated congruence and its
resulting block form all agree exactly.
Seventy-five leading Pfaffians, computed
by independent recursive expansion, equal
their prescribed block products.

Forty-nine character identities, at
$t=2,\ldots,8$ and symmetric degree
zero through six, were checked by
independent Weyl alternants for the
paired Schur modules and complete
symmetric powers of the literal
pair weights $x_ix_j$.
All pass. These finite calculations
check the signs and conventions of
the newly used polynomial maps; the
dense-open argument proves them in
every dimension and degree.

The author's 96-row coefficient
receipt was read, not rerun.
Inspection of its exact scope shows
91 rows in the theorem's declared
width range and five auxiliary
width-one zero cases at degrees
3, 5, 7, 9 and 11. All 22 positive
comparisons are in the declared
range. This scope precision was
sent to the author for its report.
The actual canonical rank is proved
by the maps in §§1–4 and is not
inferred from these coefficient
comparisons.

## 7. Geometry and final status

All restrictions, congruences, Young
maps, averages, substitutions and
transpose pairings are rational
and are specified on their exact
domains. They extend to arbitrary
characteristic-zero fields and
every finite ambient dimension
supporting $S_\lambda$.
The Chow/frame/K0 transport is
through the already verified
maps cited in R046 and R048.

The entire R048 proof passes in
both parity families, with all
small-width and zero endpoints.
No mathematical gate remains in
its stated one-row-earlier range.
