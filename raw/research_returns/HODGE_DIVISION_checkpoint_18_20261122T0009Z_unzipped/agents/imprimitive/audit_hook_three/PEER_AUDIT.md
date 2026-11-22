# Independent whole-proof audit: D-HK301–03

**PASS.** Reviewer `/root/imprimitive`, GPT-6 Astra Pro; reasoning effort
inherited and not separately exposed; run HODGE_DIVISION. The whole
mathematical/source/computational review was completed by the actual
clock reading **2026-11-21 23:38:47 UTC**. No mathematical repair was
requested.

Frozen proof:
`agents/g34_eightfolds/bireflection/hook_three_section.tex`, SHA-256
`6f3918af33aa3f23c2c89d4ac445635a64c00bd981a0d7f5557636a7eb5c6130`.
I read the complete proof, every line of `check_hook_three.py`, its
complete JSON output, bibliography and `HOOK_THREE_STATUS.md`.
The author's first-run22,517-class/51,784,139-triple calculation is
attributed to the author; I did not rerun that program.

## 1. Representation and published inputs

The exterior cube of the deleted permutation representation is the
ordinary hook `(n−3,1,1,1)`, of degreeC(n−1,3). Fulton–Harris
Proposition3.12 supplies irreducibility; the published Garsia–Goupil
character polynomial identifies the exact label independently of an
unproved exercise. For n≥15 the label is not self-conjugate, so the
accepted ordinary alternating-core interface gives an irreducible
restriction to A_n and its rational S_n extension. No spin or projective
alternating representation is being substituted.

I freshly read the complete Proposition3.12 and proof on printed
pp31–32 in the local institutional Fulton–Harris PDF. The proof counts
signed subset stabilizers and obtains the exterior permutation-character
norm2, giving the irreducible standard exterior powers by induction.
The attempted fresh web open rejected the file as too large; the full
local primary institutional copy was available and read. Source:
<https://websites.math.leidenuniv.nl/edixhoven/teaching/2019-2020/CIMPA/Fulton-Harris.pdf>,
local SHA`83a1d9cb639aa8c548de87682dc4f4a799dfde06c8f46977a386a524c1e3eeb1`.

I freshly opened the published Garsia–Goupil PDF and read PropositionI.1
and its domain on p2, the complete invoked proof(2.1)–(2.6) on pp9–11,
and Table5.1 p31. The exact expanded hook-three row is
`((f−1)(f−2)(f−3))/6 −(f−1)u+v`. Its expanded version and the
exterior determinant identity agree; no ambiguous OCR reading of the
compact falling-factorial notation is needed. Source:
<https://www.combinatorics.org/ojs/index.php/eljc/article/download/v16i2r19/pdf>,
Electronic Journal of Combinatorics16(2)(2009),R19,
DOI10.37236/85, local SHA
`f3f9de4eb2d202bb355aa64a479818329f09a5daddbf2fd321915dd2e8f2f0b8`.

The alternating normalizer, scalar-field inclusion, actual intermediate
cover and weighted-cycle interfaces were already checked fully in this
run and are reused with their exact stated hypotheses. The cyclic-average
method was supplied by root; this report is an independent whole-proof
audit, not a claim that the shared method originated independently here.

## 2. D-HK301: every target eigenspace

For f=0 the character is−1+u+v, giving both its lower bound and the
upper bound n/2−1. For f≥1 the falling cubic term is nonnegative and
the negative two-cycle term gives the global floor
`−(n−1)^2/8`. Dropping that term and using3v≤n−f gives the exact
character-defect coefficient c_f. I independently divided the
polynomials and checked c_f−c and the f=0 endpoint.

The cyclic average of moved letters is exactly the natural indexI.
The real character floor controls the Fourier difference between any
target-root multiplicity and the fixed multiplicity by b. Thus the
argument genuinely bounds every eigenspace; it does not assume that
the largest one has eigenvalue1 or that a scalar preserves a special
nonreal-eigenvalue bound.

For I≥(n−2)/2, the identity c−A=n/2 gives the full positive constantB.
For smaller positive index, every power fixes at least f0=n−2I letters.
Monotonicity of c_f improves the whole cyclic average, including identity
powers with zero defect. The remaining polynomial has second derivative
12−6f, is concave on[2,n−2], and its two endpoint values are positive
for every n≥15. I checked both endpoint formulas and their shifted
positive coefficients. This proves the all-n support estimate and its
full B term.

## 3. D-HK302: the actual one-factor source

The rational S_n image meets the scalars trivially: a scalar image
centralizes the faithful nontrivial A_n image, so its permutation
centralizes A_n and is the identity. Thus both coordinates are actual
homomorphisms and the n-letter quotient cover is genuine and transitive.

The actual multiplicity Euler identity excludes base genus≥2. Genus1
has at most six genuine marks and cannot have image rank9. The sphere
case has at least twelve genuine marks, total moving rank2a+6, and
natural quotient index at least2n−2. Nonidentity permutation marks
contribute AI+B; a genuine scalar contributes a≥B. The resulting
polynomial margin is `(n²−6n−13)/6`, strictly greater than6 for n≥15.
No conductor hypothesis or equality of original and inducing fields
is needed.

## 4. D-HK303: all transitive tensor counts

The tensor-wreath rational image has trivial scalar intersection by its
faithful conjugation action on the simple factors. A non-Eisenstein
imaginary quadratic subfield of the inducing character field therefore
forces a scalar image not contained in mu6. Generation and product one
give two distinct marks outside mu6. The proof uses only the inclusion
of the original field in the inducing field.

For every power of a rational tensor-wreath operator, a negative trace
product contains a negative factor bounded in magnitude by b, while
all other factors are bounded by a. This gives the correct trace floor
`−(b/a)e`. Rational cyclotomic multiplicities bound every root outside
orders1,2,3,6 by e/4, except order4. In that exception the two primitive
roots have equal multiplicity and the square-trace inequality supplies
exactly the displayed marked support. Thus scalar extraction and
spectral convolution are kept separate and valid.

The uniform baseline and factor-moving bounds use the verified
inequalities d0≥40, b≤d0 and2d0≤a−1. Three moving-factor entries would
allow the two scalar marks plus a distinct third moving entry; the nine
remaining marks force the displayed excess. Exactly two moving-factor
entries remain. Their permutations are inverse, and transitivity makes
them full t-cycles.

The actual connected nt-letter quotient has total index
`2n(t−1)+H+N`, so its Riemann–Hurwitz inequality givesH+N≥2n−2.
At a block-fixing entry, averaging over its active factors retains the
entire B, not B/t. The weighted-cycle estimate retains its exact R_t
error; it uses only AI for the cycle product and therefore includes an
identity cycle product. The cases t2 and t≥3 both give the stated
uniform error2. I checked the final algebra and the strict positive
quadratic. The actual Euler budget is contradicted for every n≥15,t≥2
in the stated non-Eisenstein scope.

No actual tuple existence, unlabelled character family, nontransitive
core, or positive cycle supplier is inferred.

## 5. Distinct exact reconstruction

Own program: `independent_check.py`; output:`independent_checked.json`.
No author program, arithmetic helper, selected spectrum or output row
is imported. The author program was read before writing this program,
which is disclosed.

The author enumerates exterior eigenvalue triples and selected signed
subset orbits. My program instead computes the coefficient of t³ in
`det(1+tP(x^j))/(1+t)` by truncated integer polynomial products. It then
reconstructs every primitive-root-order multiplicity using an independently
written divisor/Mobius/Ramanujan Fourier formula. Dimension sums, original
trace reconstruction, integrality and nonnegativity are all checked.

The successful execution took **0.412597899 seconds** and checked:

- 6,830 partition classes, all n15 through24;
- 48,606 exact power-character values and root-order multiplicities;
- the all-target support bounds and global character floors;
- the minimum support margin289/8, agreeing with the author's result;
- eight independently derived universal shifted-positive polynomials,
  the concavity identity and final source identities.

The first execution completed the finite spectra but failed an
overly literal SymPy structural equality: `6*(2−f)` was compared with
`12−6*f`. The expanded difference is exactly zero. That first program
and failure record are retained as `independent_check_first_attempt.py`
and `first_attempt_record.json`; changing the comparison to expanded
zero produced the successful run. No mathematical estimate, spectrum,
source or proof text was changed.

The finite reconstruction is supplementary. The universal claim rests
on the complete written proof checked above. No new TeX compilation,
published-classification re-proof or author-program rerun is claimed.
