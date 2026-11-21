# A-074. Independent audit of the complete one-twist walls G-034

**Status: PASS.** Reviewer: GPT-6 Astra Pro; effort not exposed; run
/root/archive_audit. The complete saved all_order_one_twist_report.md,
OW.1–OW.14 and all six sections, both lower-cone constructors, the
direct/residue checker, immutable upper input and the whole unified
evaluator were checked. A-072/A-073 separately audit T055/T056.

## 1. Exact module and a complete check of the general triple telescope

The balanced normal-order substitution gives
$\operatorname{Hom}_{GL(F)}(S_{(a+c,b+c,c)}F,J_k)$, with the
specified degree and determinant character. At $c=1$, the shape,
degree, twist $\operatorname{sgn}^{d+a+1}$ and partition coordinates
are exactly those in A-072. The new cone formulas retain the actual
quotient arrows and their subset-orientation lines.

The general selected-triple calculation was checked for its full
stated range, not only at $c=1$. Let $M_0=3(k-1)$ and
$N=a+b+3c$, with $a=b+x$, $x,b,c\ge0$, $k\ge1$ and $b+c\ge2k$.
A normal Young shape $\rho=(p,q,r)$ contributes to the complementary
line exactly when

$$
a+c\ge p\ge b+c\ge q\ge c\ge r\ge0.
$$

This is the actual horizontal-strip Pieri projection, with line
eigenvalue $\epsilon^{N-|\rho|}$. The normal multiplicity is extracted
by the three-row alternant
$(1-V/U)(1-W/U)(1-W/V)$.

Replace the normal polynomial by
$P_\epsilon=P_\eta(\epsilon U,\epsilon V,\epsilon W)$ and put
$F_\epsilon=P_\epsilon(1-V/U)(1-W/U)$. All its terms retain
total degree at most $M_0$; only the exponent of $U$ can be negative.
At $p\ge b+c\ge2k$, the other exponents have sum at most $k-3$.
Thus $q\le b+c$ and $p\ge q$ are automatic on the required range.
The coefficients $f_{p,q,r}$ of $F_\epsilon$ have nonnegative
$V,W$ exponents and are symmetric in $q,r$.

For every fixed $p$, summing the last alternant factor gives the
literal finite identity

$$
\sum_{q\ge c,\ 0\le r\le c}
(f_{p,q,r}-f_{p,q+1,r-1})
=
\sum_{q\ge c}f_{p,q,c}
+\sum_{r=0}^{c-1}f_{p,c,r}
=
\sum_{q\ge0}f_{p,q,c}.
$$

The second equality uses the symmetry just proved, including $c=0$
where the second sum is empty. Summing $p=b+c,\ldots,a+c$ then
telescopes the factor $1-1/U$, leaving exactly the two boundary
columns $b+c$ and $a+c+1$. This proves OW.7, including its signs.

For each selected cycle of length $\ell$, write
$i=k-1-j-h-s$. Its term after reversal is

$$
\epsilon^{\ell(k-1)}U^{\ell(k-1)}
z^{\ell j}(Wz)^{\ell h}(\epsilon z)^{\ell s}.
$$

The required reversal deficit is at most
$M_0-b-c\le k-3<k$. Therefore the original constraint
$j+h+s<k$ imposes no further restriction on any coefficient being
extracted. The three geometric series are exact there. Multiplying
by $1-Wz$ and taking the $W^c$ coefficient gives
$z^c h_\eta(c)$. The remaining two factors are precisely the
series $A_{\eta,\epsilon}$. Their two indices are
$t-2c$ and $t-x-2c-1$, where $t=M_0-b$.

The overall phase is $\epsilon^{N+M_0}$.
Its exponent differs from $x+c+k-1$ by an even integer, proving
the reported phase. Negative tail indices are zero, so this
argument also covers all empty ranges. At $c=0$ it recovers the
previous two-row triple formula through the same coefficient map.
At $c=1$, $h_\eta(1)=m_1(\eta)-1$ and the selected-triple
orientation times the complex sign is $(-1)^{\#\mathrm{cycles}(\eta)}$.
This gives OW.9 exactly, with no additional determinant sign.

## 2. Both lower cones and their fixed positive formulas

For cone A the actual parameters are
$k=T+7+K$, $x=T+X$, $b=2T+16+3K$.
For cone B they are
$k=X+2S+9+K$, $x=X$, $b=2X+5S+21+3K$.
Their first partition gaps are respectively $X+K$ and $K$.
Both have $b+1\ge2k$. Thus the singleton straightening and
the rank-three pair contraction proved in A-072 remain valid.
Four selected directions vanish because the full degree is at
least $5k$, beyond their quotient-degree bound $4(k-1)$.

The new triple deficits are $\tau=T$ on A and $\tau=X+S+1$
on B. The second tail argument is respectively $-X-1$ and $S$.
The displayed substitutions into the immutable upper physical phase
table are correct. In particular the phase key always remains the
residue of the actual $(a,b,k)$ before that substitution.

The tail generating functions have at most six denominator factors.
Their root periods divide the full permutation order: when
$\epsilon=-1$, the complementary pair contributes the factor two
to that order. Their rational functions are proper, so the phase
polynomials hold from index zero. The exact computed total degrees
are $(5,2,1,1,0,0,0)$; the separate degree caps are $(3,3,4)$
and $(3,2,4)$. The reported downsets contain all monomial supports.

All 46 positive A orders and 33 positive B orders have coefficientwise
nonnegative character-triangle margins and positive constant.
The minimum constants are **427,680** and **29,700**. The finite-group
Hermitian character bound therefore proves strictly positive
multiplicity differences. Their integer values are actual character
inner products, and order zero is the actual module multiplicity.

The fixed Newton expansion is exact. The selector and three
increasing-subset chains give the literal bounded-polytope bijection.
Each polytope has at most nine integer variables, with 47 and 34
disjoint order tags. Positive first differences reduce support to
the base cube. Exactly two effective A labels vanish at its origin,
$5$ and $1^5$; every B coefficient is positive.

## 3. Exhaustion and the two actual wall transports

The $k=0,1,2,3$ routes are respectively G021, T045 at $c=1$,
T051 at $c=1$ and G032 at $c=1$. Their validity inequalities
are the stated partition inequality $2b+x+3\ge5k$.

For $k\ge4$ and $b\le2k+1$, the complementary-column pairing
with $H=\lambda_1$ gives the new degree $H-n$ and character
$\operatorname{sgn}^H$. Direct subtraction gives

$$
x'=2b+x+3-5k,\quad b'=1,\quad c'=b,\quad
k'=\max(0,b+1-k),\quad d'=0.
$$

When $b+1<k$, the removed stable power is $k-b-1$ and its
inverse is the actual multiplication by $u^{k-b-1}$.
For $b\le2k-2$, $c'\ge2k'$; the bulk provider applies.
For $b=2k-2+s$, $s=1,2,3$, the defect is exactly $s$.
The three cited below-ray providers therefore cover these points.

The remaining region has $b\ge2k+2$. Its upper part is T055,
and $b=3k-4$ is T056. In the latter branch the inequalities
force $k\ge6$, within the strip range. Else
$\tau=3k-5-b\ge0$. For $x\ge\tau$ the inverse cone-A coordinates
are $(x-\tau,\tau,k-\tau-7)$, whose last coordinate is
$b-2k-2\ge0$. For $x<\tau$ the inverse B coordinates are
$(x,\tau-x-1,2b+x+3-5k)$. Every coordinate is nonnegative,
and substitution recovers the original point. These disjoint cases
exhaust every valid tuple.

For a partition on the first wall with $\lambda_2<n$, subtracting
$5e$ from its first row, $e=n-\lambda_2$, leaves first gap
$3\lambda_2-\lambda_3-\lambda_4-\lambda_5\ge0$.
The stable-chart map is the actual multiplication by $u^e$ and
preserves the outer label. The remaining tuple has $k=0$.
For the second wall $\lambda_3-\lambda_4=1$, the perfect
complementary-column pairing makes the first central gap one;
the sign is again exactly $\operatorname{sgn}^{\lambda_1}$.
The partition wrapper implements these two maps and both parity
changes. Greater-than-five-row inputs vanish by the stated Schur
antisymmetrizer/column projection.

The final exporter correctly retains the degree-one coin tags,
which have no Newton constant field. Its default value one
passes those tags to the actual weighted-sum constraints.
Positive weights and a fixed sum make these polytopes bounded;
negative right side gives the empty polytope. The other providers
retain their original fixed Newton constraint maps.

## 4. Independently executed certificates and evaluator checks

The independent reconstruction imports only prior archive helpers.
It evaluates unexpanded rank-three normal polynomials and all six
Weyl shifts, including the selected triples. It does not transform
the proposed upper polynomials or use the proposed triple formula
to generate its samples.

Safe phase-degree bounds are $(5,4,3,2,0,2,0)$, as in A-072.
The new triple correction does not exceed these: identity degree
at most five; for a transposition only the selected $111$ triple
contributes, with signed denominator $(1-z^2)^3$ and degree two;
selected $21$ has $h_{21}(1)=0$; a selected $3$ has degree one
with a fixed complementary pair and degree zero with an interchanged
pair. Classes $41$ and $5$ have no selected triple. Consequently
the interpolation simplex is unisolvent by a proved bound.

All **898** phase polynomials reconstructed from **3,494** exact
normal-Weyl traces match the final data. Repeated literal translations
recover all **79** complete margins and the stated minima. The
complete two base cubes, **3,024,000** multiplicities, were recomputed
with unbounded Python integers. All 14 hashes, extrema and zero sets
agree: two A origin zeros and no B zeros. The immutable upper snapshot
was also directly compared against all 449 current T055 phases and
matches.

The unified evaluator was checked on **176** valid parameter cases
covering all nine provider routes, with **1,232** independent class
traces, **2,464** both-parity coefficients and **2,464** direct
partition-wrapper calls. It additionally passed **532**
complementary-wall calls, **56** stable first-row extensions and
**14** greater-than-five-row zeros. Large cone continuations give
another **112** coefficients, **4,536** literal matrix systems
and **2,828** witnesses.

Files: `check_one_wall_cones_independent.py`,
`ONE_WALL_CONE_A_POLYNOMIALS_INDEPENDENT.json`,
`ONE_WALL_CONE_B_POLYNOMIALS_INDEPENDENT.json`,
`ONE_WALL_CONES_INDEPENDENT_RECEIPT.json`,
`check_one_wall_routing_independent.py` and
`ONE_WALL_ROUTING_EVALUATOR_RECEIPT.json`.
