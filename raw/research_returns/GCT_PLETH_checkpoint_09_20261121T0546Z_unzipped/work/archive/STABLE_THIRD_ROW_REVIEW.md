# A095. Complete audit of cubic polarization and its positive formula

**Result: PASS.** The complete G039 report,
SR3.1–SR3.23 and all eight sections, the whole
positive executable, its verification program
and saved receipt were read. The actual
cokernel action, Ricci splitting and homogeneous
cover cancellations prove the nonnegative
free numerator and both weighted cycle terms.

Reviewed files are work/root/stable_third_row_report.md,
work/root/stable_third_row_positive.py,
work/root/check_stable_third_row_positive.py, and
work/root/STABLE_THIRD_ROW_POSITIVE_RECEIPT.json.
The earlier exact free-module argument is
the construction checked in A092.

## 1. Stable transport and the whole cubic transfer

The partition in SR3.1 has size $mn$.
Its first gap is at least $(m-2)a-3\ge a-3$,
and its second gap is $a-3$. Its second part
is at most $n$, so the actual stable flag
chart applies. Removing the full determinant
columns gives $\operatorname{sgn}^t\otimes
S_{(a,3)}\mathfrak h_m$, with the stated
effective outer label.

The cubic transfer
$$
\phi(f\otimes uvw)=fu\otimes vw+fv\otimes uw+fw\otimes uv
$$
is homogeneous, $P$-linear and $GL(W)$-equivariant.
In the two-letter highest-vector calculation,
$\phi=x\partial_X+y\partial_Y$ and it kills
$xY-yX$. Thus its scalar on the Pieri vector
with second part $i$ is exactly $3-i$.
The first three scalars are nonzero and
the fourth is zero. This gives the actual
kernel $S_{(D-3,3)}W$ for every $D\ge6$.

The low degrees give the entire cokernel:
$\operatorname{Sym}^2W$ at total degree two,
$S_{(2,1)}W$ at degree three, and
$S_{(2,2)}W$ at degree four. At degree five
the three target summands all have the
nonzero scalars three, two and one;
all higher degrees are covered by the
same highest vectors. Smaller absent
degrees have zero target. No further
cokernel component occurs.

These calculations also hold when $\dim W=2$,
though the invariant action at that dimension
is treated by the separate exact determinant
map in §7.

## 2. The actual quadratic action and the Ricci inverse

The four-index tensor map
$$
\mathcal K(A,B)_{ijkl}
=A_{ik}B_{jl}+A_{jl}B_{ik}
-A_{il}B_{jk}-A_{jk}B_{il}
$$
has both pair antisymmetries, pair interchange,
and the cyclic Bianchi identity. It is
symmetric in its two symmetric inputs,
so it kills the $(3,1)$ factor. Its
full four-slot symmetrization is zero,
so it kills $(4)$. Its value on
$x^2\otimes y^2$ is nonzero.
The exact three-term Pieri decomposition
then shows that this is a quotient map
from the degree-four target, with precisely
the transfer image as kernel, onto the
specified $S_{(2,2)}W$ realization.

In the invariant metric coordinates,
$e_2=-\tfrac12\sum z_i^2$.
Consequently multiplication by the actual
quadratic invariant is $-\tfrac12\mathcal K(g,-)$
under this chosen quotient. This identifies
the action on the cokernel, including its
nonzero scalar.

Contraction of the first and third slots
gives, term by term,
$$
\operatorname{Ric}\mathcal K(g,B)
=(d-2)B+(\operatorname{tr}_gB)g.
$$
Its trace is $2(d-1)\operatorname{tr}_gB$.
The displayed formula in SR3.13 therefore
recovers $B$ exactly for every $d\ge3$.
For an arbitrary curvature tensor $R$,
applying that formula to $\operatorname{Ric}R$
and then applying $\mathcal K(g,-)$ gives
the component with the same Ricci tensor.
Subtracting it is the equivariant projector
onto $\mathcal R=\ker\operatorname{Ric}$.
The denominators $d-2$ and $2(d-1)$ are
nonzero for all declared $m\ge4$.

All maps are equivariant under the rational
orthogonal group of the form and therefore
under the specified symmetric-group action.
This proves the actual injection, direct
complement and inverse, not only their
dimension relation.

## 3. The full invariant-ring cokernel

The only positive invariant that can act
nontrivially on the listed cokernel degrees
is $e_2$, from degree two to degree four.
Its action is injective by §2. Its next
multiple is zero, and every invariant of
degree at least three kills every cokernel
component by its degree support.

Thus the complete $I,S_m$-module is exactly
$$
\bigl(I/(e_2^2,e_3,\ldots,e_m)\bigr)[2]
\otimes\operatorname{Sym}^2W
\ \oplus\
(I/I_+)[3]\otimes S_{(2,1)}W
\ \oplus\
(I/I_+)[4]\otimes\mathcal R.
$$
For the first summand the chosen head maps
to its literal degree-two class and its
$e_2$ multiple maps to the actual transfer
cokernel action, with the scalar fixed above.
The Ricci complement supplies the last
degree-four summand. This proves the module
isomorphism with every invariant action
retained. The two-degree chain has length
exactly two.

At $m=4$, the curvature space and the
symmetric-square space have the same
dimension and the Ricci kernel is zero;
the displayed formulas still apply.
At $m=3$ the injectivity statement is
not used, and its denominator obstruction
is handled by the separate determinant
isomorphism below.

## 4. Cancelling the actual free covers

The averaged invariant/coinvariant section
makes both covariant domains finite graded
free over $I$. The cokernel just determined
has a specified minimal generator cover
$M_0$ and minimal relation cover $M_1$,
with the polynomials $C_0,C_1$ in SR3.4.
The relation lists are the literal
generators of $(e_2^2,e_3,\ldots,e_m)$
or of $I_+$. They are independent modulo
$I_+$ times their respective ideals,
including the two distinct degree-four
generators $e_2^2$ and $e_4$.

The basis changes in §3 of the report
were checked at both stages. In the
target free module, homogeneous lifts
of the specified cyclic heads can be
chosen with their exact images.
Complementary residue vectors have
images in $I_+C$ and can be adjusted
by positive-invariant combinations
of those lifts. The resulting matrix
preserves the residue basis and is an
invertible homogeneous basis change,
by the graded Nakayama/projective
argument already proved in G038.

The free summand with zero cokernel
image is in the actual image of
$\phi_\nu$. Lifting and cancelling it
leaves a free domain mapping onto
$L_1=\ker(M_0\to C_\nu)$.
The minimal relation generators have
independent residues in $L_1/I_+L_1$.
Their lifts form part of a homogeneous
free basis of the new domain.
The complementary vectors map into
$I_+L_1$; subtracting the corresponding
positive-coefficient combinations of
the relation lifts kills those images
by an invertible triangular change.

This proves the actual direct sum
$$
K_\nu\simeq\mathcal F_\nu\oplus
\ker(M_1\longrightarrow M_0).
$$
Its free basis polynomial is
$A_\nu-B_\nu+C_0-C_1$.
All its coefficients are therefore
nonnegative integers. The bound
$N+3$ includes every source basis
degree and every correction degree,
since $m+4\le N+3$ for $m\ge4$.
The argument retains the kernel of
the original transfer through the
specified isomorphisms.

## 5. Both cycle bases, support, and literal matrices

The monomial-difference basis
$z^\beta(\xi_j/z_j-\xi_i/z_i)$,
with $i$ the first positive index,
is polynomial and is an exact kernel
basis in each multidegree. It gives
$Z_{\mathbf w}$ for any ordered
positive weight list; the weights
need not be increasing.

For the modified sequence use
$J=\mathbb Q[e_2^2,e_3,\ldots,e_m]$.
These generators are algebraically
independent, and
$I=J\oplus e_2J$ is a literal free
module decomposition. Tensoring the
cycle map with this free module
preserves its kernel. Its two basis
copies give the factor $1+q^2$.
The occurrences of weight four in
the ordered list label different
variables and remain distinct in
both the formula and the code.

The least-support polytope has a
unique inverse: its $z$ bit identifies
the first positive exponent and its
$y$ bit the chosen later positive
index. The exponent inequalities
force exactly that support behavior.
The generator coordinate records
multiplicity; the extra bit records
the basis $1,e_2$ over $J$.
Their degree equations therefore
count the actual cycle bases.
The largest number of variables
is $3m-1$ and the number of pieces
is at most $N+7$.

Ordinary cycles for $m\ge4$ occur
in every degree at least five.
For the modified sequence the
first three weights are $4,3,4$.
Its first-index-one branches give
degrees seven and eight; multiplying
by the remainder basis element
gives degree nine, and further
weight-three multiplication covers
all later degrees. No pair of
distinct generator indices has
smaller total weight than seven.
This proves the exact modified
support threshold, including its
smallest parameter $m=4$.
The shifted support tests in
SR3.21 follow exactly.

The evaluator's cycle sums retain
each generator index when equal
weights occur. Its denominators
and numerators have degree
$O(m^2)$ and the same proved
root-of-unity bit bounds as G037.
All polytope bounds and coefficient
shifts agree with the actual
free and cycle decomposition.

## 6. Finite character computations and corner conventions

The monomial orbits of
$\operatorname{Sym}^3\mathbb Q^m$
are the point, ordered-pair and
unordered-triple modules.
Subtracting the actual
$\operatorname{Sym}^2\mathbb Q^m$
decomposition through
$\mathbb Q^m=\mathbf1\oplus W$
gives exactly the symmetric-cube
identity in SR3.17.

The ordered-pair tensor operator
counts two removal and two
addition paths with multiplicity.
The unordered-triple operator
uses each intermediate shape once
and the three $S_3$ restriction
multiplicities. The $(2,1)$ entry
is exactly the horizontal-two-strip
plus one-box count minus the
horizontal-three-strip count,
because $s_2s_1=s_3+s_{21}$.
The code uses distinct intermediate
shapes where required and retains
ordered path multiplicities where
required. The fixed Schur modules
then follow from the displayed
two actual Pieri decompositions.
All tensor operators have a fixed
number of corner steps and thus
polynomial size in $m$.

The fake-degree computation,
degree truncation and coefficient
bit bound are the proved ones
from G037/G038. The free numerator
is computed explicitly and its
nonnegativity was proved by the
module argument, independently
of the subtraction used to
calculate its coefficients.

## 7. The complete dimension-two endpoint

For $m=3$, the three full exterior
columns give the actual pairing
$$
S_{(a,3)}W\simeq(\det W)^3
\otimes\operatorname{Sym}^{a-3}W.
$$
The determinant is the symmetric
group sign, so the effective label
is conjugated once more.
The degree-zero case $a=3$ is
included explicitly in the code.
For every larger degree its
fake-degree series over
$(1-q^2)(1-q^3)$ is exactly the
stated symmetric-power multiplicity.
The three $S_3$ fake polynomials
give at most two positive pieces,
with the complete zero-or-at-least-two
coin support test. This endpoint
does not invoke the higher-dimensional
Ricci inverse.

## 8. Independent executed checks and geometry

The fresh implementation
work/archive/check_stable_third_row_independent.py
and receipt
work/archive/STABLE_THIRD_ROW_INDEPENDENT_RECEIPT.json
record the following actual work.

The cubic monomial map was rebuilt
in every total polynomial multidegree.
A tensor cubic monomial with exponent
vector $\gamma$ has the literal column
whose entries are its multiplicities
$\gamma_i$, at the quadratic rows
$\gamma-e_i$.
Exact rational elimination checks
28 degree maps at dimensions
two through five and total degrees
two through eight, covering 1,974
multidegree blocks. The complete
kernel and all three cokernel
dimensions agree.

Using a nonorthonormal rational
Gram matrix, 52 symmetric basis
tensors in dimensions three through
six satisfy the literal four-index
symmetries, Ricci contraction and
displayed inverse exactly.
The curvature quotient also kills
all 118 tested literal degree-four
transfer columns in dimensions
two through four, retaining every
repeated-index coefficient.

All 38 free numerators for
partitions of $m=4,\ldots,7$
were reconstructed from independent
Young-permutation/Jacobi–Trudi
character rows and direct
standard-tableau fake degrees.
All 840 symmetric-square/cube
tensor operator entries and the
three cokernel multiplicities
agree with the positive executable.
The helper routines are the
independent A092 routines; neither
the root's MN checker nor its
hook-quotient computation is used
on the comparison side.

The author's saved 2,295 module
and support checks, 90 original
plethysms, 208 polytope cases
and 5,912 witnesses were read
but were not independently
rerun here.

The stable flag map, transfer,
Ricci projection, minimal covers
and basis changes are actual
equivariant module and sheaf maps.
The extension from $\operatorname{Spec}J$
uses its exhibited free two-element
basis. Their rational characteristic-zero
and finite-denominator transport
is exactly the one stated in
the report's checked geometric
dictionary.

The whole G039 theorem and
executable pass, including the
smallest outer degree, the
two degree-four generators,
all support endpoints and the
claimed positive size bounds.
