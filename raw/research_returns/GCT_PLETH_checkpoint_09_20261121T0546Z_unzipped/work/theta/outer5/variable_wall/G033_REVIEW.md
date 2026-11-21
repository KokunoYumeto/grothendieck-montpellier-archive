# Independent review of the complete central-wall formula

**Reviewed statement:** G-033, `work/root/all_order_zero_twist_report.md`,
the complete text (ZW.1)–(ZW.10), both support tables, and the added
stable and complementary wall paragraphs.

**Reviewer:** GPT-6 Astra Pro, `/root/theta_plethysm`; effort setting
not surfaced. **Date:** 21 November 2026.

**Result:** the complete mathematical proof passes. The independent
finite check described in §6 passes all7260 cases. This review does
not claim an independent replay of either complete1512000-entry
base cube or either full phase-polynomial certificate; those have
separate root and archive records.

## 1. The actual module and the retained restriction terms

The parameters in (ZW.1) give size5n, final partd, middle
parts equal, and first gap2b+x−5k. Thus the displayed inequality
is exactly the missing partition condition. The rank-two
normal-order substitution, its balanced inverse, the Young
projection and the determinant twist in (ZW.3) are the actual
maps established in G027 and T049. They give the stated
`S_5` module, including the sign exponentd+b+x.

In cone A, direct substitution gives

\[
2b+x-5k=X+K,\qquad b-2(k-1)=5+K,
\qquad k-t=6+K.
\]

In cone B these three quantities are respectively

\[
K,\qquad S+6+K,\qquad S+7+K.
\]

All the required inequalities therefore hold at their endpoints.
The section degree is at least5k. Every selected set of at least
four frame points contains four independent line directions, so
the relevant quotient has degree at most4(k−1); its selected
Schur component vanishes. The singleton and pair restrictions
are exactly the actual maps of T054. The straightening argument
extends the singleton character to allx≥0 because its only
index requirement isb≥k−1. The pair comparison is valid because
b>2(k−1). Affine substitution into the fixed phase polynomials
therefore uses their proved character identities in these cones,
even though the old upper-chamber coordinateB becomes negative.

## 2. The triple character, with both boundary terms

Writep_{r,s} for the coefficients of the literal normal polynomial
Pη(U,V). The two-variable alternant gives the normal Schur
coefficientp_{p,q}−p_{p+1,q−1}. The actual complementary-line
Pieri map is present precisely for the horizontal-strip
inequalitiesa≥p≥b≥q≥0, and contributesε^{a+b−p−q}.

The normal total degree is at mostM=3(k−1). Sincep≥b>2(k−1),
every nonzero term hasq≤M−b<k−1<b. Thus extending theq sum
to all nonnegative integers introduces no terms. In the second
alternant summand, putp′=p+1 andq′=q−1. The exponent becomes
a+b−p′−q′ exactly. Entries atq′=−1 are zero. Interiorp-columns
cancel, leaving onlyp=b andp=a+1. This proves (ZW.4) by an
actual reindexing of a finite sum, with no dropped boundary.

For a selected cycle of lengthℓ, puti=k−1−r in its normal
factor. Its reversal contributesε^{ℓ(k−1)} and the series

\[
\sum_{r=0}^{k-1}\sum_{j=0}^{r}
\epsilon^{\ell(j-r)}z^{\ell r}.
\]

At coefficient degreeh<k, no omittedr≥k can contribute.
Writingr=j+l converts this to the two geometric factors
(1−z^ℓ)^{-1}(1−ε^ℓz^ℓ)^{-1}. Consequently both boundary
columns are given by (ZW.5), with deficitst andt−x−1. The
former is belowk in both cones, while a negative latter deficit
is genuinely absent. The overall phase is

\[
\epsilon^{a+b+3(k-1)}=
\epsilon^{x+k-1}.
\]

For a selected three-subset, the complex sign is−1 and its
orientation character is(−1)^{3−#cycles}; their product is
(−1)^{#cycles}, exactly as in (ZW.7). The normal factor swap
and complementary eigenvalue were therefore both retained.

## 3. Polynomial continuation and positive counting

The roots of every denominator in (ZW.5) have orders dividing
the actual full permutation order. There are at most six
factors. Proper partial fractions consequently give, from the
initial nonnegative index, degree at most five on each residue
class. Six values determine the phase polynomial without an
unknown continuation range.

The saved character polynomials are constructed by fixed affine
substitution and these rational series. The positive-difference
argument uses the exact irreducible-character inequality
|χ(g)|≤χ(1), proved by averaging a positive Hermitian form.
Coefficientwise nonnegative domination polynomials with positive
constant terms imply every listed nonzero Newton coefficient is
strictly positive throughout its orthant. Order-zero coefficients
are actual module multiplicities. Finite differences preserve
integrality, and the displayed complete active-order sets give
the finite Newton identity. No unproved positivity of a
subtraction is used here.

The polytope variables in (ZW.9) have the stated bijection:
the equalities determine the quotient coordinates; the selector
accounts for the fixed coefficient; and the increasing chains
are the chosen subsets counted by the binomials. Their total
number is at most4+|δ|≤9. Strict inequalities become integer
gaps of one. The determinant parity selects the effective outer
label and does not change the constraints.

Strict positivity of all three first-order differences shows that
a zero can occur only when all quotient coordinates vanish.
Thus the complete base cubes prove the printed support lists.
I read those support statements and their computational scope;
I did not independently replay these cubes in this review.

## 4. Every complement and the stable endpoint

For the complementary-column pairing withH=λ1, the partition
and degree are exactly

\[
\lambda^c=(3b+2x-5k,3b+x-5k,2b+x-5k,
             2b+x-5k,0),\qquad n^c=2b+x-4k.
\]

The raw ideal order isb−k, the new quotient parameters are
x′=2b+x−5k,b′=0,c′=b, and the outer label is transposed
precisely whenH is odd. These follow from the actual perfect
pairing into(det Q^5)^H, followed by the finite symmetric-group
self-duality already established with a rational invariant form.

Forb<k, putk′=0. The complementary first row exceeds the
standardized first row by5(k−b), while its degree exceeds the
standardized degree byk−b. Thus the precise correcting map is
multiplication byu^{k−b}, not an alteration ofc′ or an
additional sign. Forb≥k, the order isk′=b−k. Whenb≤2k,
c′−2k′=2k−b≥0. Whenb=2k+s for1≤s≤3, the exact defect
isc′=2k′−s. All routed evaluator families therefore have
the printed parameters and endpoint hypotheses.

Forb≥2k+4, sett=3k−3−b. Ift<0, integrality givesb≥3k−2,
which is T054. Otherwise0≤t≤k−7. The inverse cone-A map is
(x−t,t,k−t−6) whenx≥t. Whenx<t, the inverse cone-B map is
(x,t−x−1,2b+x−5k). Each coordinate is nonnegative, and direct
substitution recoversx,b,k. This proves the exhaustive routing.

The added initial stable map also checks. Forλ2=λ3 andn>λ2,
sete=n−λ2 and subtract5e from the first part. Its new first
gap is2λ2−λ4−λ5≥0. Multiplication byu^e returns the original
balanced module and preserves the outer label. Finally, when
λ3=λ4, the actual complementary partition satisfies
λ2^c=λ3^c and has degreeH−n. Applying the completed wall
formula, including that stable map, proves the entire second
central wall through the same determinant pairing.

## 5. Reproducibility clarification

The historical enlargement script initially transformed the old
T054 polynomial file. That input was later replaced by its
directly regenerated enlarged version. Reapplying the old change
to the new input would transform it twice. This was reported to
the root; it is an input-version issue in that historical script,
not a defect in the saved enlarged polynomial data, which the
archive independently reconstructed. The G033 certificates read
the correct saved enlarged data. Their literal polynomial
identities and the exact character proof above remain unchanged.

## 6. Executed independent triple test

`check_triple_tail_identity.py` imports neither the root formula
nor any certificate. It constructs each normal polynomial by
integer convolution, extracts its rank-two Schur coefficients,
and sums every actual horizontal-strip term. It compares this
with a separately generated geometric-tail recurrence.

All7260 cases pass:2≤k≤12; selected cycle types111,21,3;
complementary eigenvalues±1;0≤t≤k−2; and0≤x≤2k. In849
cases the second boundary is nonzero;6411 have zero second
boundary. The full method, ranges and stream hash are in
`TRIPLE_TAIL_IDENTITY_RECEIPT.json`. This establishes the stated
finite verification scope independently of the mathematical
reindexing proof and independently of the phase certificates.
