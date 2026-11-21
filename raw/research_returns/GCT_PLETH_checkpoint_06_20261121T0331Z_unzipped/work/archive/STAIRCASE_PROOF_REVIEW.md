# Complete independent staircase audits

Reviewer: GPT-6 Astra Pro, run /root/archive_audit; reasoning setting not exposed.

## A-040. G-022: the all-rank bound and actual canonical image

**Status: complete proof review PASS.** Read every section of
work/root/staircase_uniform_report.md, ST.1–ST.10 and the geometric
transport paragraph.

The alternant substitution has exponents
\((r+1)(m-i)\), so its Vandermonde quotient is the displayed product
of the two-variable complete symmetric functions. Evaluation at
\(\operatorname{diag}(t)g\), followed by extraction of the balanced
monomial, is the trace on the actual balanced normalizer module: only
weight spaces fixed by \(g\) contribute, and their monomials are products
of the cycle variables.

I independently checked the cycle factorization. For cycle lengths
\(a,b\), the cross resultant is
\[
\prod_{\alpha^a=A,\ \beta^b=B}(\alpha-\beta)
=(-1)^{a+\gcd(a,b)}
 (A^{b/\gcd(a,b)}-B^{a/\gcd(a,b)})^{\gcd(a,b)}.
\]
The numerator has the same resultant sign, so it cancels in the ratio.
Within a cycle, the powered roots are permuted by multiplication by
\(r+1\); its permutation sign is exactly the stated \(\kappa\).
A common divisor greater than one makes the numerator vanish while the
denominator remains nonzero over independent cycle parameters. Under
coprimality, an even cycle forces \(r\) even, which makes the within-cycle
exponent integral. Thus ST.6 includes every sign and exponent.

Multiplication of row \(i\) by its cycle length turns the equation matrix
into a nonzero column scaling of ordinary incidence. A spanning tree
therefore determines its edge variables uniquely over \(\mathbf Q\)
once all other variables are fixed. This proves the count bound with
the specified exponent \(D_g\), without assuming integral solutions
for arbitrary choices of free variables. For a nonidentity permutation,
the two elementary estimates in ST.8 have difference
\((c-2)(m-c-1)\ge0\). The one-cycle case has at most one solution.

The identity lower bound is also an explicit injection. For odd \(r\)
the parity condition makes \(m\) odd, so the cyclic regular tournament
gives a balanced integral center. Every one of its coordinates is at
distance at least \(\lfloor r/2\rfloor\) from the cube boundary.
Independent changes on edges among vertices \(2,\ldots,m\), followed
by the forced changes on edges incident to vertex one, remain inside
the cube. The total degree makes the last balance equation automatic.
The floor estimate in ST.9 follows from
\[
2q+1\ge\frac{r-m+1}{m-2}
\ge\frac{r}{2(m-2)}
\qquad(r\ge2(m-1)).
\]

The character bound is justified by a group-averaged positive Hermitian
form. Substitution into its actual projector gives ST.10. The exponent
identity \(2D-m+2=(m-2)^2\) gives precisely ST.2. For \(m\ge4\),
\[
m(m-2)-m-D=(m^2-3m-2)/2\ge1,
\]
so the simplified bound \(r\ge(2m)^m\) is strictly sufficient.
The \(m=3\) endpoint is handled separately as written. Multiplication
by the determinant section shifts the balanced content and twists the
finite action by \(\operatorname{sgn}^d\), proving the exact change of
outer label for every \(d\).

### Primary source and canonical-map convention

I read Sra, *The q-Foulkes problem III*, equation (1.1), Theorem 1.3
on printed p.2, the normalized invariant-tensor convention in §2,
Lemma 2.1 and its complete proof on pp.3–4, and the complete
annihilator argument in §2.2 on pp.4–5. The source is
<https://suvrit.github.io/papers/qfoulkes3/qfoulkes3-v1.pdf>, with the
saved copy work/external/sra_qfoulkes3-v1.pdf.

Its map sends a product of \(b\) pure \(a\)-th powers to the \(a\)-th
power of their product, using normalized symmetric averaging. It is
therefore precisely the stated \(h_{b,a}\). The proof's whole
polarization block is injective at degree excess equal to its block
size, including the boundary. The induction and all dimension-zero
and degree-one endpoints have the claimed range. Substitution
\((a,b)=(m,n)\) gives the exact surjection used by G-022.
Surjectivity after complex scalar extension gives the same rational
rank, because these are rational matrices. The positive target
component thus has an actual canonical preimage in the specified range.

## A-041. G-023: all fixed constants and every endpoint

**Status: complete proof review and independent fixed-data reconstruction
PASS.** Read every section of work/root/staircase_five_report.md,
SF.1–SF.7, and both root scripts.

The half assignment lies in the relative interior of the bounded
edge polytope, so its dimension is exactly its edge count minus the
incidence rank. At a vertex, unfixed edges form a forest: a cycle
would support a nonzero weighted circulation that permits both small
positive and negative perturbations. After multiplying row \(i\) by
\(\ell_i\), an edge has coefficient
\(\operatorname{lcm}(\ell_i,\ell_j)\). The row right-hand side is
integral, since \(\ell_i(5-\ell_i)\) is even. Summing along a cut
of the free forest determines its edge value as an integer divided by
that least common multiple. Consequently every vertex denominator
divides the least common multiple of the cycle lengths.

This also covers parallel edges: two free parallel edges would already
form a circulation and cannot both remain unfixed at a vertex. At the
identity the resulting vertices are integral. The sign and zero
conditions are periodic with the same cycle-length period. Thus the
exact degree and period statements justify interpolation from the
initial values, including zero.

### Primary Ehrhart locators

Opened and read Beck–Robins, *Computing the Continuous Discretely*,
second edition, author-corrected text dated 18 February 2023:
<https://matthbeck.github.io/papers/ccdnew.pdf>.
Theorem 3.8 is on printed p.68, with its cone/parallelepiped proof on
pp.70–71. Theorem 3.23 and its rational-cone proof are on pp.80–81.
The latter explicitly gives a period dividing the least common
multiple of the vertex coordinate denominators. Their use here
requires the intrinsic dimension of the affine polytope; the cone
and lattice argument applies to that affine span. No larger period
or eventual-polynomial assertion is introduced.

### Independent finite enumeration

The script work/archive/check_staircase_independent.py implements an
edge-by-edge monomial convolution. It retains the first \(c-1\)
cycle exponents, and the weighted total-degree identity forces the
last one. Parallel edges are multiplied separately. This differs from
the root's first-vertex recursion and its compressed parallel-edge
coefficients.

It independently verifies 106 complete trace samples: the identity
through \(r=9\), and every other class through \(r=15\). Its first
seven identity values are
\[
1,\ 24,\ 219,\ 1136,\ 4175,\ 12216,\ 30429,
\]
and its Newton coefficients are
\[
1,\ 23,\ 172,\ 550,\ 850,\ 630,\ 180.
\]
All other closed trace functions in SF.2 agree. An independent
Murnaghan–Nakayama calculation gives the seven-row \(S_5\) character
table used for the projector. From these traces the script reconstructs
all 2,940 fixed Newton constants and compares every one with the
delivered certificate. Their positive-order minimum is 107,377,819.
The complete exceptional zero sets agree as well.

Every convolution intermediate is bounded by the number of all edge
assignments, \((r+1)^{|E_g|}<2^{63}\), in the executed sample ranges.
Subsequent Newton and character sums use Python integers. The receipt
is work/archive/STAIRCASE_INDEPENDENT_RECEIPT.json, including the exact
coefficient-stream hash.

Finally, the fixed residue selects exactly the seven indicated tags.
Each lattice point consists of a tag coordinate and an increasing
subset, with the quotient fixed by its equality. This is a bijection,
including the empty chain. The positive first difference proves
support outside the initial residue interval. At \(r=0,1\), the
determinant transpose rule gives exactly the asserted endpoint
coefficients. These checks complete the whole stated formula.
