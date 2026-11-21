# Independent audit of the two outer equal-row walls

Statement **A-055**, reviewing G-029,
work/root/end_wall_support_report.md, EW.1–EW.8,
all four sections and both complete exceptional-value tables.
Checked 21 November 2026 by GPT-6 Astra Pro,
run /root/archive_audit; effort setting not exposed.

**Complete proof PASS.** The finite closure exhausts the stated
infinite parameter sets through the explicit injections and section
isomorphisms. Both complement/sign transformations and every
exceptional multiplicity have been checked independently.

## 1. Both actual wall transformations

On the wall with equal last two entries, removing
\(d=\lambda_5\) gives
\[
\lambda^0=(a+b+c,b+c,c,0,0),\qquad
5n_0=a+2b+3c.
\]
The determinant section contributes \(\epsilon^d\).
For the other wall, put \(H=g_2+g_3+g_4\).
Its determinant-removed shape is
\((H,H,g_3+g_4,g_4,0)\).
Taking the complement in the width-\(H\) rectangle gives
\((H,g_2+g_3,g_2,0,0)\), whose gaps are
\((g_4,g_3,g_2,0)\). The perfect column pairing changes balanced
degree to \(H-(n-d)\), dualizes the module, and contributes
\(\epsilon^H\). Since the rational irreducible \(S_5\) modules
are self-dual, the effective exponent is exactly
\(d+g_2+g_3+g_4\). Thus the stated effective-label transpose
rules follow from the specified pairing on both walls.

For the first normalized wall, the G-027 parameters are
\[
k=\max(0,b+c-n_0),\qquad
\alpha=(b+c,b+c,b).
\]
The inequality \(k=0\) is exactly \(a\ge3b+2c\).
In that range the actual quotient-section and balanced-chart maps
identify the module with
\(\epsilon^{b+c}S_{(b+c,b+c,b)}\mathfrak h_5\).
Increasing \(a\) by five changes only the first highest weight
by five and the balanced degree by one. The chart inverse changes
by multiplication by \(u=\prod_iX_{i1}\); all other section data
and the sign remain fixed. This gives the stated actual stable
isomorphism, including its inverse through the common section model.

Subtracting a multiple of ten in EW.5 preserves positivity,
the weighted congruence and all parities. It occurs only in this
proved \(k=0\) range. Consequently the normal-form operation
has the exact module interpretation required for every graph use.

## 2. Seeds, monoid and a rigorous closure argument

For the three positive gaps write
\((a,b,c)=(1,1,1)+p+2t\).
The original \(t\) satisfies the required congruence, so a minimal
admissible \(u\le t\) exists. A total of at least five contains
a nonempty zero-sum subvector: list five indexed residues and
use equality of two of their six partial sums modulo five.
Removing it contradicts minimality. The total-at-most-four
enumeration therefore includes every minimal seed.

The same partial-sum argument shows that every indecomposable
nonzero increment has total at most five. A longer element
contains a proper zero-sum subvector of length at most five.
Recursive subtraction thus expresses every increment in terms
of the eight independently enumerated generators.
Every such increment has the actual G-024 invariant-section
embedding. Full positivity is therefore preserved by every
further monoid increment.

The graph is best interpreted as a set of actual inputs:
an unstable node represents one point, and a stable node
represents its whole nonnegative first-axis progression of
step ten. Every deficient seed belongs to this represented set.
For an unstable node, each stored edge directly places its
successor in that set or in the upward-closed full-support set.

For a stable point \(g+10q(1,0,0)\), adding a generator gives
\[
(g+2h)+10q(1,0,0).
\]
The multiplier for \(h\) and the first-axis multiplier commute
as elements of the same polynomial algebra. First use the stored
edge for \(g+2h\). If it is a full-support exit, all further
axis increments preserve full support. Otherwise retain its
normal representative and any actual stable offset already
removed. Apply the recorded first-axis edge successively for
the remaining finite number of increments. While the state is
unstable, this increases its first gap until it either exits or
reaches the new threshold. At a stable state, the further
increments are isomorphisms and its first-axis edge is a loop
in the represented set.

This explicitly treats an increment that raises \(b,c\) and
raises the stability threshold. It never assumes that the
normal form commutes with that increment. Induction on a finite
generator expression proves that every deficient input is
represented by a listed point or ray. Conversely every listed
point has a deficient computed module, and every represented
stable point has that same module by the actual isomorphism.
This proves both directions of the classification.

## 3. Independent complete finite reconstruction

The independent program check_three_row_support_independent.py
uses the separate integer Jacobi–Trudi and two-cycle
\(\mathbf F_{61}\) interpolation implementation.
It independently enumerates minimal parity vectors and proper
zero-sum subvectors, rather than accepting the supplied seed or
generator list.

It finds exactly 30 seeds, eight monoid generators, fourteen
initial deficient seeds, 24 retained deficient nodes, and
192 edges. For every edge it computes both its raw target and
its normal representative and checks equality of all class
traces, as well as agreement with the supplied multiplicity
vector. The revised graph's explicit seed, node and target
trace fields were all checked.

The computation includes:

- 1,554 seed/edge irreducible-multiplicity comparisons;
- 1,344 raw-versus-normal edge class-trace comparisons;
- 1,358 distinct class traces on 194 distinct gap vectors;
- 84 independent fixed-Schur character checks at the twelve
  stable nodes.

The largest inner degree is twelve. The interpolation degrees
are below 61, and the proved centered reconstruction bounds
\(n+1\le13\) for the double-two-cycle case and ten for the
three-two-cycle case are below \(61/2\).
The computation uses 1,526 single-cycle determinants and
835 two-cycle interpolations.

For each stable node the script also evaluates the literal
\(3\times3\) Schur determinant on \(\mathfrak h_5\), with
the required \(\epsilon^{b+c}\) factor, and checks the
step-five neighbor directly. The twelve nodes pair exactly into
the six displayed step-five rays. Each first gap is the actual
threshold \(3b+2c\), which automatically satisfies the size
congruence. The other twelve nodes give exactly the finite table.

Every exceptional vector and all claimed always-occurring
effective labels agree with the report. The exact receipt is
THREE_ROW_SUPPORT_INDEPENDENT_RECEIPT.json, including the updated
source graph hash and the complete finite/ray lists.
All other points have full support by the exhaustion proof,
not by an unproved numerical cutoff.

## 4. Geometric and canonical consequences

The edge maps, stable chart maps and exterior-column pairing
are the same explicit maps whose actions were checked above.
The report uses the corrected EGAII affine Proj and exact
graded-sheafification locators. Its locally free \(K_0\)
transport uses the finite equivariant resolution on the stated
base, as proved in A-050. No additional pullback exactness
is needed.

R-031's actual rank law was completely reviewed in A-053.
It therefore applies to the symmetric canonical map on both
walls with the stated low-degree source ranks, square-map
kernel subtraction and high-degree target surjectivity.
The support tables here concern all outer labels after their
precise sign conversions; the canonical-rank application uses
the specified symmetric map.
