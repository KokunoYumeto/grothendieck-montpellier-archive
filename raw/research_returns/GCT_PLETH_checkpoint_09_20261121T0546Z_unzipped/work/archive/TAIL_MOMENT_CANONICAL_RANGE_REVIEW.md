# A-089. Whole-proof audit of R046

**Status: PASS.** I read all of work/rectangular/tail_moment_canonical_range.md, TM.1–TM.22 and all eight sections, and the complete verification program. The actual canonical factorization, finite-row faithfulness and full-isotypic surjectivity in $D+t\le2n+1$ pass. I also independently checked 160 exact normalized split-moment entries in three coordinates.

## 1. Exact highest-space chart and degree bound

For a nonempty tail, $D\ge t$, so
$N=\lfloor(D+t)/2\rfloor\ge t$.
The integer inequality $D+t\le2n+1$ is exactly $n\ge N$. Thus the stated range guarantees the slot-degree bound needed by the chart.

The dehomogenized highest vector is translation invariant and factors through the actual sum-zero projection. The Cauchy and fixed rational Young projectors identify its lower highest component with the invariant Schur space. Every row-basis weight in $S_\nu E_a$ is at most $\nu_1=t$: each of the $t$ columns contains a given basis letter at most once. Since the inclusion $W_a\hookrightarrow E_a$ and its Schur map are actual linear maps, this bounds the separate row degrees of every vector under consideration. Hence the displayed homogenization is an inverse on the entire invariant highest space for $n\ge t$.

## 2. Ordinary moment algebra and its evaluation

The degree-$d$ generator map is the literal centered row power sum, with scalar one. In the uncentered algebra, products expand by equality partitions of occupied rows. The discrete partition gives the corresponding injective row-assignment sum, and every other term merges row types. The induction and the nonzero factorial multiplicities give surjectivity in every finite row count.

When $s\ge D$, all row assignments needed in scalar degrees at most $D$ exist. Ordering the monomial types by occupied rows gives a triangular basis change with nonzero diagonal, proving injectivity as well. The fixed decomposition into the trivial row line and $W_s$ gives the degree-one polynomial factor; setting it to zero is precisely centering. Quotienting that identified factor proves the centered isomorphism through degree $D$.

A generator of degree $d>t$ cannot contribute to the $S_\nu U$ component. The actual Pieri projection from a factor $\operatorname{Sym}^dU$ requires a horizontal strip with $d$ distinct columns, whereas $\nu$ has only $t$ columns. This proves the precise formal moment truncation used in the factorization.

## 3. Finite-row faithfulness of the specified power-sum map

The ordered-row exterior identification carries the true permutation action to supersymmetric tensor permutations with their Koszul signs. Decomposing by row exterior degree gives TM.8 through literal symmetric and alternating projectors. A nonzero term has at most $t$ degree-one rows, because that factor is an exterior power of $T=\mathbb Q^t$. All other nonempty rows have degree at least two. Therefore a degree-$e$ term uses at most $\lfloor(e+t)/2\rfloor$ rows.

For $e\le D$ and $s\ge N$, every possible term occurs, with the remaining rows filled by the unit. The full $GL(T)$ character of the uncentered invariant exterior algebra is consequently constant in these degrees. The actual decomposition
$C_s(T)=\Lambda T\otimes B_s(T)$
has constant term one in its first factor. Degree induction therefore proves constancy of the centered character, and skew-Cauchy extracts constancy of the precise $\nu$ multiplicity.

The proof then supplies the required morphism. The orthogonal transpose $q$ of zero-padding satisfies
$q(P_Se_i)=P_se_i$ for $i\le s$ and zero otherwise.
This identity makes both ordinary and exterior power-sum generators restrict with scalar one. The ordinary restriction is surjective; the equality-partition argument gives the same conclusion for the exterior generators. Tensor powers of $q$ commute with the fixed Young projectors, so both Cauchy descriptions induce the same $S_\nu(q)$ on row multiplicity spaces.

Choose $S\ge\max(s,D)$. At $S$, the ordinary moment map is an isomorphism by the basis argument above. The invariant restriction onto row count $s\ge N$ is surjective and its domain and target multiplicities have the equal dimensions just proved. Thus it is an isomorphism on this precise component. The generator identity
$p_s=\operatorname{Sym}(q\otimes1)p_S$
then proves injectivity and surjectivity of this particular $p_s$. This is the actual finite-row faithfulness needed later.

## 4. Independent-row polarization and triangular moment substitution

The independent-row evaluation is injective by rational polarization of its diagonal functional. On translation-invariant polynomials it remains injective after normalization and setting first moments to zero: recenter a normalized functional by its own mean, then restore nonnormalized functionals by homogeneity on the dense open set $L(1)\ne0$. This is the same exact argument already checked in A085, in arbitrary finite auxiliary dimension.

Its output is a polynomial in the formal moments of degrees two through $t$, preserves scalar degree and is $GL(U)$-equivariant. It therefore remains in the $S_\nu U$ component on which the preceding faithfulness applies.

For a repeated-coordinate monomial with multiplicities $\beta$, the ordered distinct-factor sum is $\prod\beta_j!$ times the corresponding coefficient of the product linear form. Dividing by $(n)_d$ gives exactly $(n-d)!\prod\beta_j!/n!$, the scalar-one normalized pairing. This verifies every repeated-index normalization in TM.15.

Möbius inversion on equality partitions gives the block coefficient
$(-1)^{|B|-1}(|B|-1)!$.
The signed permutation count by cycle partition verifies its recurrence. Each set partition occurs once with its coordinate positions retained. The first moments vanish, so singleton blocks disappear. The one-block contribution is
$(-1)^{d-1}(d-1)!p_d/(n)_d$;
every other contribution uses lower-degree generators. For $n\ge t$, all displayed leading scalars are nonzero. Recursive substitution in degrees $2,\ldots,t$ therefore gives an actual graded equivariant algebra automorphism and its inverse.

## 5. Exact canonical factorization and rank

On the first-coordinate chart, the normalized grid pairing on a row-symmetric highest polynomial is exactly the same row functional in each of its $a$ rows. Hence the output is
$p_n\Psi_nE_a(f)$,
with no extra scalar. The calculation on centered rows determines the entire affine output: common translation is the explicit first-coordinate unipotent substitution. The actual output is highest and satisfies these equations by equivariance. Restoring separate first-coordinate homogeneity proves the global polynomial identity. Only this actual composition is required to extend to the target slot degree.

The first factor is injective on the input highest space, the middle is invertible, and the last is injective on its exact Schur component for $n\ge N$. Thus $h_{a,n}$ is injective on the whole highest multiplicity space. Equivariance and complete reducibility make it injective on the full isotypic component. The actual scalar-one transpose pairing then gives full target rank for $h_{n,a}$.

The empty tail is supplied directly by the pure-power tensor identity. Insufficient ambient rank gives zero by the actual column antisymmetrizer. Rational definitions and nonzero displayed denominators give the same result after every characteristic-zero scalar extension.

## 6. Consequences and source scope

For a target component of length at most $a$, one has $D\le(a-1)t$. Therefore $n\ge\lfloor ab/2\rfloor$ reaches every target with $t\le b$; longer target shapes are already zero by the tensor-slot Young map. The width-four and tail-sensitive bounds follow by substitution.

For tail $2\rho$, the threshold is exactly $|\rho|+\rho_1$. The report's first-row calculation proves validity of the displayed partition, and the previously checked actual even-tail product construction supplies nonzero multiplicity. Applying the theorem in both directions gives the asserted stable-range canonical isomorphism.

I reread the retained primary Sarkar source, §6, the theorem labeled thm-perp and its full proof. Its coefficient assertion has inner parameter at least the tail width and outer parameter at least $\lfloor(D+t)/2\rfloor$, with the first-row partition condition. This agrees with the report's attribution. The present proof obtains faithfulness of the actual power-sum map by the independent finite-row construction above. The Bowman–Paget statement is retained as the report's cited background; no fresh read of that source is claimed here.

## 7. Independent executed normalization check

check_tail_moment_independent.py expands three-coordinate product linear forms directly and independently computes the set-partition Möbius sum by choosing the block containing the first labeled factor through submultisets. It uses exact fractions and imports no source implementation.

For degrees two through six, row counts $d,d+1$, and every three-coordinate monomial of each degree, all 160 normalized entries agree. The receipt is `TAIL_MOMENT_NORMALIZATION_INDEPENDENT.json`.

The original 276 stable-character comparisons and 168 two-coordinate moment checks were read and remain attributed to the original verifier. They were not rerun. The complete unbounded canonical range is established by the whole factorization proof checked in §§1–5.
