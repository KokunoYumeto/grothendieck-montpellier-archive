# Independent audit of the finite-base canonical ranges

Statement **A-057**, reviewing the entire R-032 report,
`work/rectangular/finite_base_canonical_ranges.md`, FK.1–FK.12,
its complete 28-row table and its finite-tail verifier.
Checked 21 November 2026 by GPT-6 Astra Pro,
run `/root/archive_audit`; effort setting not exposed.

**Complete proof PASS after the explicit chain-padding correction
described below.** The five surjectivity families and the positive
upper bound follow for the actual canonical map, including all
multiplicities, all dimensions and characteristic-zero base change.

## 1. Exact map and kernel membership

The averaged tensor evaluation pairing gives
\(h_{b,a}^*=h_{a,b}\) on the dual space, with scalar one.
Consequently the actual image annihilator is the displayed lower
canonical kernel; its Schur multiplicity equals the cokernel
multiplicity being bounded. This is the same exact pairing already
fully audited in A-053, and its use in FK.4 has the correct indices.

The normalized outer comultiplication \(\delta\) has
multiplication as a left inverse. For \(r+1\) outer slots,
the common coefficient extraction then gives exactly
\[
\Theta F(v_1,\ldots,v_r;x,y)=
\binom br^r\mathcal A_F
(x^rv_1^{b-r},\ldots,x^rv_r^{b-r},y^b).
\]
There is no unspecified scalar in this formula.

The lower-kernel membership proof was reread in full in R-024
P.9–P.16. A split form \((x^r+c y^r)Q\) is a product of
\(b\) linear forms over \(\mathbf C\). Its first coefficient
in \(c\) gives the vanishing with last argument \(y^rQ\).
Applying the \(b-r\) directional derivatives corresponding
to the factors of \(Q\) to the last argument \(y^b\)
gives exactly the scalar \(b!/r!\) times this vanishing.
Before derivative \(i\), the exchanged variables have degrees
\(b-i+1\) and \(r\), with positive difference
\(b-r-i+1\). On a two-letter string
\(\det^j\operatorname{Sym}^{p+q-2j}\), the derivative
has nonzero coefficient \(p-j\), since \(j\le q<p\).
It is therefore injective on the full bidegree and on every
multiplicity space. The other variables are spectators. Removing
the derivatives successively proves the required vanishing with
last argument \(y^b\). Evaluation in \(x,y\) separates
the two exterior symmetric factors, so the image lies in the
tensor product with the actual lower canonical kernel.

All maps and coefficients are rational; proving the polynomial
identities over \(\mathbf C\) proves their rational identities.
Extension to every characteristic-zero field preserves the kernels
and the injectivity of the resulting linear maps.

## 2. Full-multiplicity injection and its iteration

For \(b_{r+1}=C_{r+1}+t\), the exact recurrence gives
\(b_{r+1}-r=b_r\ge t\ge1\). After \(\delta\),
every first-factor type \(\nu\) contributing to a
\(\lambda\)-type is contained in \(\lambda\), by the
horizontal-strip Pieri rule. Thus \(\nu_2\le t\le b_r\).

The full R-018 proof was reread: every highest polynomial is a
linear combination of products of flag minors; after separate
dehomogenization, each slot block has degree at most
\(\nu_2\). At common vector \(e_1\), the coefficient map
multiplies a monomial of block degrees \(d_i\) by
\(\prod_i\binom{b-d_i}{r}\). Every factor is nonzero in
the stated range. Division by these exact factors gives an inverse
on the polynomial subspace. The equivariant kernel therefore has
no highest vector of the indicated type, proving injectivity on
the entire isotypic space rather than on a selected vector.

The direct sum of these first-factor types is still injective:
distinct isotypic images remain distinct before tensoring by the
last symmetric factor. Tensoring preserves injectivity. In the
resulting codomain every lower kernel type is contained in the
output type by two applications of Pieri, and hence has second
row at most \(t\). This proves exactly FK.9.

Iterating this specified map on its middle factor, using ordinary
factor permutations, gives FK.10. The degree identity
\((r+1)b_{r+1}-r b_r=r^2+b_{r+1}\) checks at every stage.
No projection onto an unspecified image or multiplicity basis is
needed in this iteration.

## 3. Complete finite tails and exact exclusions

The independent script `check_finite_base_tails_independent.py`
recomputed both plethysm multiplicities by the previously audited
selected-subset arrangement character for every one of the
**125** partitions in the second-row bands at \(t=1,2,3,4\).
Their differences give all base kernels, using the actual
transpose injectivity already proved in R-031. At \(t=5\),
the script selects the band from all eight previously checked
primary CIM square-map kernel types. The counts are exactly
\(0,3,4,19,2\), giving **28** rows; every partition and
multiplicity agrees, including the sole double occurrence
\((10,4,4,2)\).

Independent componentwise antichain extraction gives FK.5
exactly. Every one of the **251** sorted bounded four-coordinate
tails agrees with the stated exclusion formulas. A further
**4539** longer-tail comparisons confirm the full column-height
interpretation, including rows after the fifth. The receipt is
`FINITE_BASE_TAILS_INDEPENDENT_RECEIPT.json`; the finite comparison
does not replace the general inequality proof below.

For a nonzero target, its length is at most \(a\), and
\(\lambda_1\ge aC_a+t\ge30+t>5t\). Thus every base
first row fits, and containment is exactly a tail condition.
For \(2\le t\le4\), the minimal tails have the form
\((t-j,2^{j+1})\). Put \(p=\lambda_2\) and
\(q=\lambda'_2\). When \(p\ge2\), a contained tail
requires \(j\ge t-p\) and \(q\ge j+3\), and these
are sufficient. Exclusion is precisely \(p+q\le t+2\).
When \(p\le1\), containment is impossible and the same
inequality holds. At \(t=1\), the base kernel is zero.
At \(t=5\), exclusion of \((5,4,3,1)\) is exactly
the four alternatives in FK.3.

Every type in the codomain of FK.10 contains a base type.
The stated exclusions therefore remove the entire codomain
isotypic component. Injectivity removes the actual annihilator
component, and the exact pairing proves target surjectivity.

## 4. Pieri polytopes, corrected row padding and the sample rank

The successive tensor factors in FK.10 have strip sizes
\(25,b_6,36,b_7,\ldots,(a-1)^2,b_a\). The inequalities
\(\theta_i\ge\eta_i\ge\theta_{i+1}\), with the
specified size and fixed endpoints, are exactly the horizontal
strip conditions. Every intermediate shape is contained in the
final shape, so all these variables are bounded. A separate tag
for the double base multiplicity implements the stated positive
upper bound on the actual cokernel multiplicity.

The initial draft padded every chain to \(a\) rows even when
FK.11 permitted an endpoint of length greater than \(a\).
The actual target then vanishes, but the codomain count need not.
For example, at \(a=6,t=2,b=7\), the valid strips are
\[
(2,2,2,2,2)
\longrightarrow(25,2,2,2,2,2)
\longrightarrow(30,2,2,2,2,2,2),
\]
of sizes 25 and 7. This gives a positive codomain count with
seven rows. The report was corrected to pad to
\(\max\{a,\ell(\lambda)\}\) rows and now explicitly
retains this codomain count when the actual target is zero.
The corrected paragraph was reread. Its inequalities now realize
FK.11 literally in every stated case.

Finally, in FK.12 the relevant binary weights count unrestricted
partitions of 4 and 5 because \(a\ge6,b\ge10\). Their
counts 5 and 7 give two-row multiplicity 2 by adjacent-weight
subtraction. The shape has second row 5 and third row zero, so
FK.3 reaches its complete target component. The exact actual
image multiplicity is therefore 2, as asserted, in every dimension
at least two.
