# A096. Complete fixed-order hook audit

**Result: PASS.** The complete T064 report, FK.1–FK.15,
all four construction sections and its final check-scope
section, the whole positive executable and the complete
verification program were read. The proof gives the stated
fixed-parameter positive construction, including the
actual correction module, its uniform bound, and every
degree transport. This event records a whole-proof and
code review; the author's exhaustive calculations were
not independently rerun.

Reviewed files:
work/theta/unstable_hook/fixed_order_hook_report.md,
work/theta/unstable_hook/fixed_order_hook_positive.py,
work/theta/unstable_hook/check_fixed_order_hook.py.

## 1. Exact correction module and its positive computation

The all-order jet sequence is the actual split map
checked in A093. With $N=m-1$ and $j=k-1$,
the homogeneous expansion of
$P_N=\mathbb Qu\oplus\mathfrak h_N$ gives the isomorphism
$$
\bigoplus_{h=0}^j\operatorname{Sym}^h\mathfrak h_N
\longrightarrow\operatorname{Sym}^jP_N,\qquad
f\longmapsto u^{j-h}f.
$$
The invariant vector and the direct-sum inverse are
specified, so this step preserves the affine Taylor
module and its character.

A monomial of exponent partition $\rho$ has exactly
the stated stabilizer: its zero exponents form one
block and equal positive exponents form the other
blocks. The coset-to-monomial map is bijective.
The actual tensor-induction isomorphism then gives
FK.8, with the extra fixed coordinate of $S_m$
accounted for by the final factor $s_{(1)}$.

Subtracting the mean separately on each nonempty
block gives the precise direct sum of block standard
modules and the trivial space
$\{(c_b):\sum n_bc_b=0\}$.
Taking exterior powers gives the hooks and the
binomial multiplicity in FK.10–11. Size-one blocks
have zero-dimensional standard module and allow
only leg zero. A zero-size block is omitted.
At $j=0$ there is only the large block, and the
formula reduces to the first-order one-box induction.
When the zero block is absent, all $m$ letters
belong to a computation of size at most $k$.

For a nonempty zero block, its exterior leg is
determined by the other legs and the chosen trivial
exterior degree. It is checked, not enumerated.
All other choices depend only on $k$. After the
large hook is chosen, the remaining skew shapes
have at most $k$ cells. The executable considers
only intermediate diagrams contained in the
requested output. Its LR recursion reads right
to left and top to bottom, imposes weak rows,
strict columns, fixed content and every prefix
lattice inequality. Its completion count is
therefore the literal LR count used in the proof.

I independently read the retained primary
Macdonald text, Chapter I §9, printed pp.142–147,
including (9.1)–(9.7), the complete reversible
Littlewood–Robinson construction, the tableau
preservation lemma, the recording-tableau argument
and the inverse reconstruction completing (9.4).
The exact rule is (9.2), printed p.143. Its
right-to-left row convention matches the code.
The source files are work/archive/Macdonald.pdf
and Macdonald.txt; the public primary copy is
https://math.berkeley.edu/~corteel/MATH249/macdonald.pdf.
The induction characteristic map is the one
already read in A090.

## 2. The uniform bound and every support endpoint

Normalized symmetrization injects the symmetric
power of the permutation module into its tensor
power. Tensoring with the exterior hook and
inducing are exact, so this is an actual injection
of the correction module into the ordered-word
module. Its orbits are indexed by set partitions
of the $j$ word positions, with $p$ distinct
coordinate values and stabilizer $S_{N-p}$.

For $N-p\ge1$, restriction of the standard module
is $\mathfrak h_{N-p}\oplus\mathbb Q^p$.
The exterior decomposition has total hook
multiplicity at most $2^p$. Induction to $S_m$
adds $p+1$ boxes; for each fixed hook and output
the number of standard skew tableaux is at
most $(p+1)!$. When $N-p=0$, the remaining
representation has dimension at most $2^p$,
and induction from the trivial group has
each multiplicity at most $m!=(p+1)!$.
Summing the actual word orbits proves precisely
the displayed $D_k$ bound, including $k=1$.

Every affected label is consequently a hook
plus at most $k$ boxes, or has total size at
most $k$. A hook has one cell on each content
diagonal, so the diagonal-width bound $k+1$
follows directly. For the row label, all
positive block exterior hooks are nontrivial,
so only the exterior power of the trivial
block-mean space contributes. This gives
FK.13 exactly and implies $r\le k-1$.
It covers the all-zero-exponent orbit and
all size-one-block cases.

## 3. Complete point selection and both degree transports

The base degree is $a_0=2k+1$ or $2k+2$
according to parity. The checked actual
jet surjection supplies at least $d$
points in the stable polytope there.
For non-row labels, the exact Koszul
minimum gives $L\ge r+1$, so every needed
point has tableau/subset/coin excess at
most $2k+1$.

The semistandard increment enumeration is
the complete minimum-filling standardization
proved in A093, now with this larger bounded
budget. The number of increment arrays is
$\binom{m+2k+1}{2k+1}$. Omitting a cell
below the stated window or including a
cell above it costs more than the whole
budget by the same exchange argument.
There are $4k+3$ retained weight levels
and at most $k+1$ cells at each, giving
FK.15. The empty and full subsets are
handled separately. Coin degree is
bounded by the same budget. Distinct
tableaux, subsets and coin vectors give
distinct complete points.

Adding the fixed nonnegative integer
$(a-a_0)/2$ to the weight-two coin
is injective for non-row labels and
satisfies the new degree equation and
upper bound.

For the row label, $r\le k-1$ gives
base degree at most $3k+1$.
The coin and positive-support-subset
enumeration is therefore bounded by
a function of $k$, apart from writing
the $m$ coordinate entries. At positive
degree shift, the exponent of two is
increased and the least-support bit
is reset to two. Every unchanged
subset index exceeds the old minimum
and hence exceeds two. The selected
exponents remain positive, and the
new exponent of two is positive.
All original inequalities are valid.
Subtracting the known shift recovers
the old exponents and then the old
least-support bit; the subset was
unchanged. This proves the claimed
injective inverse, even when the
least index changes. At zero shift
the map is the identity.

## 4. Positive cells, exact complexity and code scope

The unique-owner deletion procedure is
the exact integer-lattice partition
checked in A090 and A093. Each new
point has one current owner because
the points are distinct. Replacing
only that cell by its first-difference
pieces adds exactly $2N_{\rm poly}-1$
cells. The final number is
$1+d(2N_{\rm poly}-1)$ and obeys FK.3.
All cells retain the original bounded
constraints. The actual jet sequence
proves the correction dimension, and
the explicit deletions give the
positive lattice count.

The correction computation has only
parameter-dependent orbit partitions
and small block choices. Its LR
diagrams contain at most $k$ additional
cells and hence have at most $2^k$
intermediate subsets; the cost of
handling the long hook is polynomial
in $m$. This proves the stated
$f(k)\operatorname{poly}(m)$ arithmetic
bound. Its integer output is at most
$D_k$, controlling its bit length.
Combining it with G037 gives the
claimed exact coefficient and support
time bound.

Constructing the positive matrices
uses at most the displayed binomial
number of tableau increments, the
parameter-only subset window and
bounded coin degrees, followed by
at most $D_k$ deletions. The matrix
sizes and binary right sides add
only a polynomial factor. Thus
$f(k)(m+k+1)^{2k+O(1)}$ is justified.
The explicit-$m$ convention at $t=0$
and the ordinary output-part convention
at $t\ge1$ are stated accurately.

The code implements each orbit and
block formula, the small LR paths,
both point transports and the full
owner constraints. The Stirling
recursion includes its empty-set
case. The absent-zero-block branch,
large-block leg bound, and row-label
least-support reset were all checked.

The author's 2,910 correction checks,
11,640 coefficient/parity comparisons,
3,036 removed-point cases and 58
literal-cell cases were read with
their code and stated scopes; no
execution of those sweeps is claimed
by this audit. T062's all-order
actual map was independently checked
in A093, including exact finite
jet matrices.

The same rational flag, jet, coset
and Young maps give the stated
geometric transport. T064 has no
remaining mathematical gate in
its stated fixed-order range.
