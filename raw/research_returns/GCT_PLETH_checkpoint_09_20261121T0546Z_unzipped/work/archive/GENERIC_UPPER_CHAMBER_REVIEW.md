# A-078. Independent audit of the unbounded-twist upper chamber T-058

**Status: PASS.** Reviewer: GPT-6 Astra Pro; effort not exposed; run
/root/archive_audit. The complete `generic_twist_upper_report.md`,
GU.1–GU.14 and all seven sections, was read, including the final
rational highest-space comparison added after GU.8. The full
polynomial constructor and evaluator were also read. Independent
phase, margin, support and evaluator calculations are described below.

## 1. Actual representation and retained complex

For nonnegative $(X,B,K,C)$, the parameters are
$x=X$, $c=C$, $k=C+K+4$, $b=C+3K+10+B$.
Direct substitution gives first partition gap $K+2B+X$,
$b+c-2k=K+B+2$, and $|\alpha|-5k=K+2B+X$.
The degree and all five parts in GU.1 have the stated sum.
The determinant parity is exactly $d+b+x+c=\lambda_2$.

The G027/T049 normal substitution, balanced homogenization and
Young projector identify the actual multiplicity module with
the stated isotypic part of $J_k$. Four selected independent
directions have quotient degree at most $4(k-1)$, less than
$|\alpha|\ge5k$; the full five-point quotient is a further
quotient. A three-point term has a complementary line. Its
horizontal-strip inequalities require
$\rho_1\ge b+c$ and $\rho_2\ge c$, hence
$|\rho|\ge b+2c\ge3k-2>3(k-1)$.
This exceeds its entire normal degree. The actual quotient
complex therefore truncates to GU.4 with its original arrows
and orientation lines.

The singleton is exactly the corrected $c<k$ formula of
A-077. Here $b\ge k+1$, every shifted second part is at
least two, and the remaining triangle order is $k-l\ge4$.
Thus both the actual exterior-column pairing and the exact
first-row-cutoff involution are valid throughout the range.

## 2. The general pair determinant and its actual equivariant map

Every two-slot normal Schur shape is $\rho=(p,q)$, with
$p\le2(k-1)<H=b+c$. Put $A=a+c$. Expanding the final
row of the three-row skew determinant gives the three
minors with outer/inner pairs

$$
((A,H),(p,q)),\quad
((A+1,H+1),(p+1,0)),\quad
((A+1,H+1),(q,0)).
$$

Their signs are respectively positive, negative, positive.
The last-row indices are $c$, $c-q-1$, and $c-p-2$.
The exact two-row exterior-dual/Clebsch–Gordan comparisons
apply because $p<H$, including the two shifted minors.
Factoring their common $D^H\operatorname{Sym}^xW$ gives
precisely GU.6.

Summing its three terms in $z$ gives GU.7. For eigenvalues
$u,v$ of $W^*$, the three-variable alternant for
$s_{(p,q,0)}(u,v,z)$, expanded along the $z$ row, is

$$
\frac{uv\,s_{(p,q)}(u,v)-z^{q+1}h_{p+1}(u,v)
+z^{p+2}h_q(u,v)}{(u-z)(v-z)}.
$$

Dividing by $uv$ gives exactly the same rational expression,
since $D=(uv)^{-1}$. The apparent denominator cancels because
the expression is that Schur polynomial. Hence every coefficient,
including $p=0$, $p=q$, and coefficients beyond its degree,
has the exact value stated in GU.8.

The right-hand coefficient is the actual last-line weight
subspace of a Young-projected tensor module. Its generating
operators replace $\xi\in W^*$ by $\xi(w)z$, summed over
tensor positions. The two replacement operators commute.
Together with the internal matrix-unit lowering in $GL(W^*)$,
they generate the Schur module from its Levi highest space;
ordering these three explicit lowerings gives the stated
triangular tensor/PBW spanning argument. This specifies a
rational, graded, equivariant surjection.

The final added comparison also gives an actual rational
isomorphism, rather than only its character. In each
$GL(W)$ weight $(r,s)$, take the ordered rational raising-kernel
basis on the skew Young space and on the proposed tensor/weight
space. The proved character identity and complete reducibility
give equal highest-space dimensions. Match these bases and map
each divided lowering string $E_{21}^jv/j!$ to the matching
string. The raising identity
$E_{12}E_{21}^jv=j(r-s-j+1)E_{21}^{j-1}v$
proves that both matrix units commute with the map, and
the weight construction gives torus equivariance.
The strings form bases by complete reducibility.
Their finite exponentials and Gaussian decomposition therefore
give $GL(W)$ equivariance. Tensoring the identity on each
normal Schur multiplicity space preserves the selected-slot
permutation action. This meets the exact map requirement.
It is auxiliary to the fixed positive evaluator.

For a pointwise fixed pair, weight $c$ in the product of
truncated symmetric algebras is the exact sum
$\sum_{l=0}^c T_{k-l}(W^*)T_{k-c+l}(W^*)$.
Both orders are positive because $c<k$. For an interchange,
only even $c$ occurs, with trace
$T_{k-c/2}(W^{*2})$ and negative subset orientation.
The squared action is the square of the actual permutation,
not a replacement representation. The invariant dot product
identifies $W^*$ and $W$ as stated.

## 3. Initial indices, physical phases and degree bounds

Every ordinary complete-function coefficient is a proper
root-of-unity quasipolynomial from index zero. The ambient
determinant can additionally use indices $-1,-2$.
For the four-dimensional standard module, the denominator
$D_\gamma(z)$ has degree four and nonzero leading coefficient.
Its exact recurrence at degrees three, two and one forces
the unique backward continuation to have
$h_\gamma(-1)=h_\gamma(-2)=h_\gamma(-3)=0$.
The quasipolynomial solution satisfies that recurrence for
all integers, proving those same initial zeros. Thus the
constructor does not extrapolate an incorrect negative value.

For the singleton and fixed-pair outer sums, write
$l=s+Lq$. Their bound is at least $-1$, and the polynomial
summation identity gives zero at that endpoint.
The inner triangles have order at least four, within the
already proved initial range. A negative determinant sign
has even permutation period, so it is constant on each
chosen physical residue.

The swapped-pair half-index has the correct period as well.
For a complementary permutation of order $r$, its square
has order $r/\gcd(r,2)$; the full permutation period is
$\operatorname{lcm}(2,r)$. Half of the latter is divisible
by the order of the square. Hence an even physical residue
$c\bmod L$ determines $c/2$ modulo the required squared
period. This verifies the constructor's half-residue use.

The exact fixed phases have total degrees
$(6,3,2,1,0,0,0)$ and 2,291 physical phase keys.
The independent interpolation used the larger, proved bounds

$$
(6,4,4,3,0,3,0).
$$

For the identity, the ambient Weyl dimension has degree six;
the singleton triangle has degree at most five before the
outer $l$ sum, and the fixed pair has degree at most six.
For a transposition, its complete function is a quadratic
polynomial plus a constant alternating term. In the ambient
three-row determinant the purely quadratic part has degree
three, while a term using the alternating rank-one part has
degree at most four. Its rank-three complement has a
two-row determinant of degree at most one: the quadratic
leading product cancels. Two triangle sums and the outer
sum add at most three degrees, giving four.

For $221$, the ambient products have degree at most three,
and the same leading cancellation in the rank-three
complement gives the safe singleton bound four. For $311$,
the ambient products have degree at most three and the
complement's two-row character is periodic; its three sums
give at most three. The $32$ and $5$ cases are periodic.
For $41$, the periodic complement likewise gives at most
three. The binary pair formulas do not exceed these bounds.
This proves unisolvence before any comparison to the proposed
coefficients, so the reconstruction does not infer a degree
bound merely from matching sampled values.

## 4. Positivity, fixed counts and complete support

All 144 identity monomials are positive and their support
is exactly the printed inequalities GU.11. The displayed
factorization and every one of its 14 grouped rows are
correct. All 143 nonzero step-60 differences have the
reported coefficientwise nonnegative character-triangle
margin and a positive constant; the minimum is **1,583,020**.
All omitted orders vanish by the support downset.

The invariant Hermitian bound on irreducible characters
therefore proves strictly positive multiplicity differences.
Order-zero values are actual module multiplicities and
hence nonnegative; all differences are integers.
No enumeration of the four-dimensional residue cube is
needed for this conclusion. The exact Newton identity
then gives the 144-tag positive formula.

Four fixed quotient coordinates, one selector and at most
six chain coordinates give at most eleven integer variables.
The increasing-subset chains and selector give the literal
bijection in GU.13; the evaluator's matrices enforce exactly
the equalities, nonnegative bounds and unit gaps.
Every fixed evaluation coordinate is at most 419.

For support, increasing $C$ by two adds $(4,4,2,0,0)$
to the partition and two to the balanced row degree.
The explicitly oriented product $p_{135}p_{24}$ has row
degree one in every row and right weight $(2,2,1)$.
The sum of its squared translates is invariant, has the
required doubled weights, and is nonzero at the real
Vandermonde matrix. Multiplication inside the single
flag-polynomial domain is therefore an injective
$S_5$ map on precisely the specified balanced modules.
The effective determinant parity is unchanged.

At $C=0$, the old coordinates are $(X,B,K+1)$ in T054.
Filtering the independently verified old zero list gives
exactly the seven displayed effective-label exceptions.
At $C=1$, $B=0$ is T056 and $B\ge1$ is T055, with
$k\ge5$, so every entry is positive.
At $C=2$, the four printed seed vectors are positive.
The actual multiplication transports all odd values
from $C=1$ and all even values from $C=0$ or those
four $C=2$ seeds. This proves the complete stated support.

## 5. Independent executed reconstruction and evaluator audit

The new C++ oracle uses the literal singleton interlacing
sum and direct two-slot normal Pieri components. For
pointwise fixed slots, the multiplicity of $S_{(p,q)}$
is the number of integers

$$
\max(q,p+q-k+1)\le r\le\min(k-1,p).
$$

This counts the two symmetric degrees with their actual
horizontal-strip map. For swapped slots, only equal degrees
survive; the component $(2r-q,q)$ has trace $(-1)^q$.
The sign follows directly from the highest vector containing
$q$ alternating brackets under exchanging the two slots.
The complementary skew Schur character is evaluated by its
three-by-three determinant itself. Thus the oracle uses
neither GU.8 nor its simplified pair traces.

All **2,291** phase polynomials reconstructed from **16,166**
literal class traces agree coefficient for coefficient.
Python interpolation and margin arithmetic use unbounded
integers and exact rational numbers. Native oracle arithmetic
is signed 128-bit with an explicit proved bound:
all requested complete indices are at most 400 and $k\le100$,
and every intermediate absolute prefix is bounded by

$$
(1+45\cdot100^3)\,6\binom{403}{3}^{\,3}<2^{127}.
$$

The script verifies the input bounds before execution and
the oracle asserts them again. This is a proved arithmetic
bound, not an unchecked machine-integer assumption.

The independent literal-translation calculation reproduces
all **143** full margin polynomials, the minimum constant,
all **144** identity exponents, and the distinct-phase
counts $(1,14,10,25,3,3,3)$.
The original branching oracle also independently gives all
**28** entries of the four $C=2$ seed vectors.
The Vandermonde sum is independently computed as
$12\sum_{|I|=3}(\Delta_I\Delta_{I^c})^2=27,840$.

The evaluator audit verifies all **14** printed factor rows
and all **seven** $C=0$ zero entries. It checks **168**
coefficients with both determinant parities at twelve
parameter points, **24,178** literal matrix systems and
**4,828** witnesses, including large continuations.

Files: `generic_upper_trace_oracle.cpp`,
`check_generic_upper_independent.py`,
`GENERIC_UPPER_UNISOLVENT_QUERIES.txt`,
`GENERIC_UPPER_POLYNOMIALS_INDEPENDENT.json`,
`GENERIC_UPPER_INDEPENDENT_RECEIPT.json`,
`check_generic_upper_evaluator.py` and
`GENERIC_UPPER_EVALUATOR_RECEIPT.json`.
No full 60-to-the-fourth residue cube was executed or claimed.
