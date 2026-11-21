# Independent audit of zero twist at ideal order two

Statement **A-058**, reviewing the full G-030 report,
`work/root/second_power_zero_twist_report.md`, ZS.1–ZS.11,
every support table, certificate code and direct evaluator.
Checked 21 November 2026 by GPT-6 Astra Pro,
run `/root/archive_audit`; effort setting not exposed.

**Complete proof PASS.** The exact rank-two restriction model,
its skew-character extraction, all initial residue ranges and the
positive formulas have the stated domains. The first-two-order
and complementary-region corollaries use the actual flag and
exterior-column maps with the correct signs.

## 1. Exact section and restriction model

For \(a=b+x\), the partition in ZS.1 has size
\(5(d+a-2)\). Its first gap is \(2b+x-10\), and its
other gaps are \(0,b,x\). Thus the validity condition is
precisely the stated \(2b+x\ge10\). Its ideal order is
\(\lambda_2-n=2\), its line twist is zero, and its balanced
flag module has sign \(\operatorname{sgn}^{d+a}\).

The rank-adaptive normal-order argument in T-049 §6, already
fully audited in A-051 and reread here, permits two auxiliary
columns for \(\alpha=(a,b)\). A nonzero maximal minor of
the remaining row matrix makes the normal images independent;
the polynomial substitution therefore preserves the least normal
degree. The Young-complex evaluation and its acyclic negative
twists give the actual isomorphism between the displayed ideal
Schur multiplicity and the section space. At \(b=0\), using
two columns still contains the same one-row Schur functor, and
the argument applies without a change of map.

The total auxiliary degree is \(a+b\ge10\), exactly the
range required for the five order-two ideals. A selected slot
has the truncated quotient \(\mathbf Q\oplus F\).
The stabilizer splitting leaves the standard complementary
space \(\mathfrak h_{5-s}\), with the explicit quotient maps
of G-027. Four selected independent frame lines span \(E\),
so their quotient has maximum degree four; every later quotient
is also zero in the degree being used. Thus the full exact
complex has precisely the displayed terms of sizes zero through
three. Its alternating sign times its orientation is
\((-1)^{\#\operatorname{cyc}(g|A)}\), including the empty
subset sign \(+1\).

## 2. Skew extraction and all seven normal characters

For a selected cycle of length \(\ell\), the cyclic tensor
trace on its truncated factors is
\(1+X^\ell+Y^\ell\). Products over cycles give ZS.5.
The coefficient of a rank-two Schur character is the difference
of the monomial coefficients at \((p,q)\) and
\((p+1,q-1)\). This rule includes negative trace coefficients;
for example the selected transposition has coefficient \(-1\)
at \(s_{11}\). Each of the seven printed polynomial identities
was independently expanded and checked.

Tensoring the normal Cauchy component \(S_\rho F\) with
the complementary Cauchy factor and applying the fixed rational
Young projectors gives the Littlewood–Richardson multiplicity
space. Its complementary trace is exactly
\(s_{(a,b)/\rho}\). The primary derivation was independently
reread in Macdonald, second edition, Chapter I §5:
(5.1)–(5.3) define this adjoint multiplicity character, and the
complete Cauchy/alternant coefficient calculation on printed
p.70 gives (5.4). Its two-row determinant is literally
\[
h(a-p)h(b-q)-h(a-q+1)h(b-p-1).
\]
The proof of containment and (5.7) on printed p.71 gives zero
when \(\rho\) is not contained. The local primary files are
`Macdonald.pdf` and `Macdonald.txt`, from
https://math.berkeley.edu/~corteel/MATH249/macdonald.pdf .
The text and full displayed derivation were read; no new visual
inspection of the scanned pages is claimed by this event.

Combining these exact extractions with the oriented restriction
complex gives ZS.6. Averaging its genuine section character
against a complete irreducible row gives integral multiplicities.
No equality of virtual dimensions is being substituted for the
section-space map.

## 3. Initial ranges and polynomial degrees

All complete-function eigenvalues have orders dividing 60.
Partial fractions therefore give a polynomial on each residue
class for every nonnegative index. The empty-subset identity
trace is the printed rank-four two-row Weyl product, of total
degree five and separate degrees three and four. At the
transposition, only eigenvalue 1 has multiplicity three. Its
quadratic complete-function leading coefficient is independent
of the index shift, so the two degree-four products cancel.
Every other contribution has degree at most three.

For a singleton complement, the largest rank is three. The
two quadratic leading products in the skew determinant cancel,
leaving total degree at most three and degree in \(x\) at
most two. Its nonidentity products have degree at most two.
For two selected letters, the complementary rank is two; the
identity linear leading products cancel, and the other residues
are bounded. At three selected letters the complementary rank
is one, so the remaining trace is periodic.

In the bulk \(b=B+5\), every normal type satisfies
\(p\le3,q\le1\), and every complete-function argument is
nonnegative. The polynomial formulas consequently start at
the residue origin. On a fixed boundary \(0\le b\le4\),
the shift \(x=X+10-2b\) ensures \(a\ge6\). All
varying indices are nonnegative; the other indices and all
noncontainment tests are constant on that branch and use their
exact zero values. Its degree in \(X\) is at most three.
This proves the Newton formulas on the whole stated domains,
including their initial parameters.

## 4. Fixed certificate, polytopes and independent checks

The finite certificate evaluates all 504000 bulk and 8400
boundary constants. Its source arithmetic uses unbounded integers.
The sum of absolute finite-difference coefficients is bounded
by \(2^{3+4}\) in the bulk and \(2^3\) at a boundary.
The recorded input maxima give the printed signed-64-bit bounds,
so the subsequent array operations are exact. The complete code,
extrema, order set and support specifications were read. The
separate full reconstruction of these 512400 constants passed
in the rectangular agent's run: all 42 bulk/boundary label hashes,
extrema and zero sets agree, using unbounded integers throughout.
Its receipt is `work/rectangular/SECOND_POWER_ZERO_TWIST_CERTIFICATE_INDEPENDENT_CHECK.txt`;
that computation is not counted as this audit's run.

The independent script
`check_second_power_zero_twist_independent.py` instead tests the
unexpanded normal monomial products and the two Weyl alternant
shifts, using selected-cycle masks and the actual orientation.
It uses no skew-Schur expansion for its independent traces.
The following executed checks all pass:

- All seven finite normal-character identities.
- 833 class traces on 119 valid parameter pairs.
- 168 direct evaluator coefficients, covering all labels, both
  determinant parities, every boundary, and continuation to
  \(x=251,b=307\).
- 1690 exported polytope matrices, decoded independently from
  their quotient equalities and chain orders.
- All inequalities and equalities for 614 lazy witnesses.

The receipt is `SECOND_POWER_ZERO_TWIST_INDEPENDENT_RECEIPT.json`.
This is separate evidence from the author's 1442 balanced-value
checks and the other agent's exhaustive fixed-constant run.

For each tag, the quotient equalities fix the two quotient
variables; the interval contributes exactly the constant; and
each strictly increasing chain contributes its binomial count.
The inverse bijection is literal coordinate reading. The degree
bound removes exactly three of the twenty possible orders, giving
seventeen tags with at most five chain variables, two quotients
and one interval variable. The boundary has one quotient and
at most three chain variables, hence at most five variables.
The first-difference positivity proves the exact finite support
decision from the saved residue zeros. The outer transpose is
exactly the sign \(d+b+x\).

## 5. Completion of the two orders and complementary region

For a general five-row shape, ZS.10 reads the last three gaps
without ambiguity. At positive ideal order,
\(n=d+b+x+c-k\), and summing the five rows gives the first
row \(d+3b+2x+4c-5k\). Its remaining validity condition is
\(2b+x+3c\ge5k\). The actual complementary-column bundle
is \(\operatorname{sgn}^{d+b+x}\mathcal I^k(c)S_{(b+x,b)}Q\).

Every row of the order/twist table matches precisely the validity
range and bundle of its cited theorem. In particular, at
\(k=2\), twists 1 and 2 give respectively
\(2b+x\ge7\) and \(2b+x\ge4\), exactly T-051 and
T-050; twist 3 is T-045. At order zero, the stable chart and
G-021 apply with arbitrary nonnegative line twist. Thus the
first region \(\lambda_2\le n+2\) is fully covered.

For \(H=\lambda_1\), the exterior-column perfect pairing
identifies the complement balanced module with the original
dual times \(\operatorname{sgn}^H\). Its inner degree is
\(H-n\ge0\), and its excess is
\(\lambda^c_2-n^c=n-\lambda_4\). Consequently
\(\lambda_4\ge n-2\) is carried exactly into the first
region, with the stated outer-label transpose. The equality case
\(H=n\) is the rectangular shape and gives the constant
complement module, covered by the order-zero chart. This proves
ZS.11 with its actual morphism and all endpoints.
