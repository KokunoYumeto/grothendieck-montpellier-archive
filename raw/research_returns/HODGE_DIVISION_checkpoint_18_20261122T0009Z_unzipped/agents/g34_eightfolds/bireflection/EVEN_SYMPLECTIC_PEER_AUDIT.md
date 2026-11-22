# Whole-proof audit: D-ESC01–03

**PASS.** Reviewer `/root/g34_eightfolds`, GPT-6 Astra Pro, effort
inherited/unexposed, HODGE_DIVISION, 2026-11-21, approximately
18:12–18:14 UTC. I read the whole proof, bibliography, source record,
original-input builder, both exact checkers and the complete GAP
exporter. The reviewed proof SHA-256 is
`2fd6be44c6023f9debf6803401cb5db1532051c65e03b62d74b9e6b0b02645b9`.

I independently reconstructed every new generic coefficient inequality
and every selected small-group spectrum. No author arithmetic module,
selected-row list, coefficient certificate or scan output was imported.

## Complete table inputs and source boundary

I freshly opened the official complete table inventory at
<https://oscar-system.github.io/GenericCharacterTables.jl/stable/tables_list/>.
Its `Sp4.0` entry explicitly records the errors in Enomoto's printed
table and the replacement computation by Frank Lübeck using
Deligne–Lusztig theory. The corrected official mathematical input is
therefore essential to the stated proof. The paper alone is not being
claimed as an exact transcription of the implemented entries.

I also opened the original published Enomoto article,
<https://ir.library.osaka-u.ac.jp/repo/ouka/all/8596/ojm09_01_07.pdf>.
The complete-character purpose on p.75, construction beginning in
§4 on p.80, completeness assertion on p.85, and Tables IV-1/IV-2
on pp.92–94 agree with the bibliography. This audit verifies the
coverage and provenance statements, not a new derivation of the
original character classification or every printed table entry.

For `Sp6.0`, the official inventory explicitly distinguishes the whole
ordinary table from `uniSp6.0`, whose twelve row types comprise only
the unipotent subtable. I read Lübeck's full retained author text at
the cited Introduction pp.3–4, §2.2 pp.18–21, and §9 pp.78–79.
It states the complete ordinary-character result, explains the
Lusztig-series and additional nonuniform functions, and supplies the
full tables as CHEVIE files. The downloaded primary source has
SHA-256 `5d336441c90390b3f2072ed7ceaaacdfb83776549954d9d830dbabe4967af070`.
The source is a dissertation and official mathematical data source;
the proof correctly avoids labelling it a refereed journal article.
The browser extractor rejected its `application/x-pdf` content type;
the local primary PDF/text was available and used for the actual read.

The exceptional multiplier and ATLAS metadata conventions retain the
earlier independently checked primary inputs of D-BI21/22 and D-G2T.
The exact small-table records, source strings and fusions were read
again here. Their group identities and outer automorphism labels are
explicit mathematical inputs, not deductions from orthogonality.
I do not claim a fresh proof of those finite-group classifications.

## Generic inequalities and all-field validity

Every generic entry is a sum of rational polynomials times phases of
absolute value one. Collecting formal phase monomials and then applying
the triangle inequality to translated coefficients yields an upper
bound for every real q at least the specified threshold. Additional
relations among phases can only improve that bound. Thus this is a
uniform polynomial proof, not an extrapolation from finitely many
field sizes.

The independent parser checks the original entry extraction against
both frozen Julia files, including their hashes, declared degree and
class-length arrays. It verifies the trivial row and identity column.
All nonidentity class lengths have nonnegative translated coefficients
and constant term greater than one. All nontrivial degree polynomials
have nonnegative translated coefficients, with the printed minimum
constant terms. This excludes a hidden central or small-field
specialization inside the asserted ranges.

The complete new checks are:

| Input | Nontrivial row types | Entries | Threshold | Character ratio | Minimum degree |
|---|---:|---:|---:|---:|---:|
| Sp4.0 |18|324|8|1/4|196|
| Sp6.0 |65|4225|4|17/63|378|

The conversion to every finite-order linear normalizer uses the
previously proved complex commutator bound, including nonidentity
scalar commutators. Taking c=17/63 gives (1−c)/4=23/126;
the Sp4 quarter-character estimate is slightly stronger. No assumption
that outer elements occur in a generic core table is made.

## Small spectra and complete normalizers

My own exact restriction-norm calculation selects extension rows anew.
I additionally match each surviving restriction pointwise against a
core character. Both fusions preserve element orders and all prime
power maps; their class-size unions verify normal inclusion. The
complete linear characters are trivial on the core and contain a
character of the asserted full quotient order, verifying the cyclic
quotient data.

All 104 selected rows and 3,442 nonscalar spectra pass an independent
Ramanujan Fourier reconstruction. All multiplicities are nonnegative
integers summing to the degree. The per-table counts are 26/676,
20/580, 16/464 and 42/1722, respectively. The only quarter-bound
failures in `2.S6(2)` are exactly rows 2, 5 and 6, with
(degree,minimum ratio) equal to (7,1/7), (21,5/21), (27,2/9).
The degree-seven row is rational and its Frobenius–Schur indicator
is independently recomputed as +1. The complete degree list at most
nine is exactly seven and eight.

The fixed cyclic-extension argument is valid even without a split
extension: after adjusting the inner automorphism, Schur's lemma gives
the scalar discrepancy in the dth-power relation, and a dth-root
rescaling removes it. Thus the test includes every compatible outer
normalizer of Sp4(4). For Sp6(2), the trivial outer group and universal
perfect cover give scalar times a core operator. Keeping every
nonlinear universal-cover row includes all central kernels.

## Tensor and source consequences

The intrinsic factor algebras are permuted by the normalizer. A
factor-preserving nonscalar operator inherits the weakest factor
eigenspace bound. On a nontrivial tensor cycle, diagonalizing the
product twist gives weighted basis-word orbits. A fixed eigenvalue
occurs at most once per orbit. Constant words and the remaining
orbits imply the quarter bound, which is stronger than each bound
used here. Mixed ranks and field sizes in part (1) cause no problem.

The actual intermediate-cover factorization rules out positive genus
for a rank-nine source in these degrees and forces r≥12 with total
moving rank 2e+6. The bound 23e/126 gives e≤63/2. This excludes every
generic single factor and every tensor product; Sp4(4)'s stronger
one-third bound excludes the remaining single factor.

For a transitive Sp6(2) core with factor degree different from seven,
the 2/9 estimate gives e≤9. The only possible degree-eight single
factor violates the stronger integer quarter budget. For degree-seven
factors, the invariant symmetric bilinear form makes the full
normalizer a similitude group. Its multiplier must be nontrivial
because the inducing character field contains the original imaginary
quadratic field. At least two inertias then have totally isotropic
fixed spaces. Their half-degree costs and the ten remaining seventh
costs give e≤14, so exactly one degree-seven factor remains.

That endpoint is removed only by the previously proved D-BI17 within
the precise eight-field, non-Eisenstein, nonsplit scope. The proof does
not assert an all-fields degree-seven exclusion or equality of the
original and inducing fields. Its explicit nonsimple Sp4(2) boundary
and its record of the failed stronger generic probes are correct.

## Reproducibility

The reviewer-owned `audit_even_symplectic.py` reuses only the reviewer's
previously authored sparse AST parser and Fourier helpers. Its first
complete run passed in 1.023 seconds. All counts, exact input hashes,
reviewed proof hash and detailed per-row results are retained in
`audit_even_symplectic.json`. The universal proof was read separately;
the computation is not presented as a substitute for the geometric
or normalizer arguments. No TeX compilation was performed.
