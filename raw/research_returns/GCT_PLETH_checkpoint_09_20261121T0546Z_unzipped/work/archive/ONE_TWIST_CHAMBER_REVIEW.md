# A-072. Independent audit of the one-twist chamber T-055

**Status: PASS.** Reviewer: GPT-6 Astra Pro; effort not exposed; run
/root/archive_audit. This records a complete reading of T055/OT.1–OT.12,
all six sections, the polynomial constructor, residue checker and positive
evaluator. Executed independent calculations are recorded separately below.
No new primary-source read is asserted in this event.

## Actual module and exact deletion of the higher terms

Put $a=b+x$, $k\ge3$, $b\ge3k-3$, and
$\alpha=(a+1,b+1,1)$. The partition's first gap is
$2b+x+3-5k=K+2B+X$ in coordinates $X=x,B=b-3k+3,K=k-3$.
Every point in the nonnegative orthant is valid, including its origin;
the weight sum is $5n$. The actual G027/T049 balanced substitution gives
the stated Young-isotypic part of $J_k$ and determinant character
$\operatorname{sgn}^{d+a+1}=\operatorname{sgn}^{\lambda_2}$.
The reported conjugation of the outer label is therefore correct.

The restriction complex has actual quotient arrows and the exterior
orientation line of each selected subset. Extracting a polynomial
$GL(F)$-isotypic component is exact in characteristic zero. Four selected
independent block directions give quotient degree at most $4(k-1)$;
adding the fifth direction gives a further quotient. The degree here is
$a+b+3\ge5k$, so these terms vanish. For three points, the remaining
standard module is a line. A nonzero skew Schur factor requires
$\rho_1\ge b+1\ge3k-2>3(k-1)$, exceeding the entire selected normal
degree. This proves the exact sequence OT.4 through its actual complex.

## Singleton and pair maps, including the endpoints

The singleton horizontal-strip inequalities are exactly
$i\le a-b=x$, $j\le b$, $l\in\{0,1\}$ and $i+j+l<k$.
The $j$ bound is automatic. For $l=0$, the exterior-column pairing
removes the height-three column, producing the determinant of the
three-dimensional complement and the indicated two-row Schur factor.
For $l=1$, the outer shape is shifted and the order is $k-1$;
there is no extra determinant. The involution
$(i,j)\mapsto(x+j+1,i-x-1)$ preserves the forbidden region $i>x$
and its total. It changes the two-row determinant's sign. Fixed points
have equal shifted rows and determinant zero. This proves the exact
character-triangle extension in OT.6.

For a pair, the normal Young shape is $\rho=(p,q)$, with
$p\le2(k-1)<b+1$. At $q\ge1$, the last row of the skew determinant is
$(0,0,h_1(W))$. The two-row exterior-dual comparison gives
$(\det W)^{b+1}\operatorname{Sym}^{a-b}W\otimes S_{(p,q)}W^*$.
Tensoring the last factor with $W$ removes one corner of $\rho$ by
contraction followed by the corresponding rational Young projection.
For $p>q$ both removable corners occur; for $p=q$ only the lower one
occurs. These are precisely the weight-one components of
$S_\rho(W^*\oplus z)$. The maps respect the complementary symmetric
group and the selected-slot action.

For $q=0$, the last row is $(0,1,h_1(W))$. The additional negative
minor is the two-row skew determinant with outer $(a+2,b+2)$ and inner
$(p+1,0)$. Its exterior-dual image is
$(\det W)^{b+2}\operatorname{Sym}^{a-b}W\otimes
\operatorname{Sym}^{p+1}W^*$. The displayed sequence

$$
0\longrightarrow\det W\otimes\operatorname{Sym}^{p+1}W^*
\longrightarrow W\otimes\operatorname{Sym}^pW^*
\longrightarrow\operatorname{Sym}^{p-1}W^*\longrightarrow0
$$

uses the exact maps
$(u\wedge v)\otimes f\mapsto
u\otimes\partial_vf-v\otimes\partial_uf$ and
$w\otimes f\mapsto\partial_wf$.
Their composite is zero. The first is injective, the second is onto
for $p\ge1$, and their dimensions give exactness. At $p=0$ the target
is zero and the first map is the determinant-dual isomorphism. Thus
the empty normal shape contributes zero, as required. This verifies
OT.7 at every endpoint through its specified tensor maps.

For a pair fixed pointwise, weight one in
$T_k(W^*\oplus z)^{\otimes2}$ is
$2T_k(W^*)T_{k-1}(W^*)$. For an interchange, the trace cycle uses
$z^2$, so the weight-one trace vanishes. The negative subset orientation
then multiplies zero. The pointwise-fixed pair has positive orientation.
The invariant rational dot product identifies $W^*$ with $W$ as an
actual representation. All factors and signs in OT.8 follow.

## Phase ranges, positivity and counting

Expansion of the ambient determinant gives OT.9, including its two
correction terms and $h_1(E)=m_1-1$. The shifted singleton triangle
has order $k-1\ge2$. Its residue bound can be $M=-2$: both the
empty triangle and $\binom{M+2}{p+q+2}$ are zero there. Thus the
phase identity includes the initial range.

The 449 phases have periods $1,2,2,3,6,4,5$ and actual total degrees
$(5,2,1,1,0,0,0)$. The identity polynomial has the stated 17 grouped
rows, all positive coefficients, and the stated 46-element downset.
Each of the 45 positive differences has a coefficientwise nonnegative
character-triangle margin and a strictly positive constant. For an
irreducible character, $|\chi(g)|\le\chi(1)$ follows from a finite-group
invariant positive definite Hermitian form. This proves strict positivity
of those multiplicity differences; their integrality follows from the
actual class inner products. Order-zero values are actual multiplicities.

The Newton identity is exact on every residue class. The selector and
the three increasing-subset chains give a literal bijection with the
reported disjoint lattice-point sets. Three fixed quotient coordinates,
one selector and at most five chain coordinates give at most nine
integer variables. The evaluator's equalities, lower/upper bounds and
unit-gap inequalities implement this bijection. The positive first
differences reduce every zero to the residue cube. The only zeros are
the three origin entries for effective labels $5,221,1^5$; the origin
multiplicity vector is $(0,1,1,2,0,1,0)$.

## Independent executed reconstruction

The script check_one_twist_independent.py imports only prior archive
audit helpers. Its samples use the unexpanded three-variable normal
polynomial on every stable cycle subset, the six Weyl shifts, and closed
complete characters of the complementary standard module. It does not
use the proposed pair formula or the root/theta trace constructors.
The third normal exponent is retained through one: the third
highest-weight coordinate is one and every Weyl shift there is
nonpositive, so higher exponents cannot contribute.

The safe phase bounds, proved before interpolation, are
$(5,4,3,2,0,2,0)$. The identity ambient dimension is degree five,
its singleton triangle has degree at most five, and its pair term
has degree at most five. The transposition's ambient products have
degree at most four and its triangle at most three. For $221$, these
bounds are two and three; for $311$ both are at most two. The $32$
and $5$ cases are periodic. The $41$ periodic-complement triangle
has degree at most two. Partial fractions and triangular summation
prove genuine phase polynomials on the full initial range. Hence
the respective degree simplex is unisolvent.

All **449** polynomials reconstructed from **1,747** exact normal-Weyl
trace values agree coefficient for coefficient with the saved data.
Repeated literal translations $P(Z+60e_i)-P(Z)$ independently recover
all **45** complete margins; their minimum constant is **2,431,040**.
All **1,512,000** base multiplicities were recomputed with Python
unbounded integer/object arithmetic. All seven hashes, extrema and
the complete three-element zero set agree.

The separate evaluator audit checks the 17 printed identity rows,
the nine printed margin rows, **140** coefficients with both determinant
parities at ten parameter triples including large continuations,
**6,434** literal matrix systems, and **2,676** witnesses. Every
check passes. The exact files are:

- ONE_TWIST_POLYNOMIALS_INDEPENDENT.json;
- ONE_TWIST_INDEPENDENT_RECEIPT.json;
- check_one_twist_evaluator.py;
- ONE_TWIST_EVALUATOR_RECEIPT.json.

The shared receipts' T056 checks are reviewed separately in A-073.
