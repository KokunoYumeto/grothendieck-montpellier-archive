# Program scope and runtime audit — A.5–A.7 and targeted supplements

Researcher: GPT-6 Astra (OpenAI), `part_a567`, this run, 19 November 2026. This ledger distinguishes actual executed assertions from descriptive values printed by a script. A program supplements the complete proofs in the TeX; a finite sample is never the proof for all characteristics or for a continuous analytic family.

## Main exact-check program: three preserved versions

### Initial version: `code/part_a567_checks_initial.py` and `.out`

The executed finite octahedron phase covers the 24 odd primes from 3 through 97: 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97. For primes congruent to 1 modulo 4 it works over F_p with a chosen square root of -1; otherwise it works over F_(p^2)=F_p[i]. For each prime it enumerates all 6*5*4=120 ordered images of a projective triple, hence 2,880 candidate projective transformations in total. It retains exactly those preserving the six-set, examines all pairs of its nonidentity involutions for Klein subgroups with that fixed-point union, computes the normalizer of the standard Klein subgroup, and examines all 15 complementary-pair harmonic tests per prime (360 such tests overall). All these assertions passed. It also evaluates the three exact exceptional-characteristic expressions 2, 5, and 5/4.

The next matrix phase failed: its initial choice r2=diag(1,-1) did not invert rho=ST, so r3=r2*rho was not an involution. This was a wrong selection of generators, not evidence for a false presentation. The failure is preserved. The characteristic-2 size in this version is a descriptive printed value, not an independently executed enumeration; the later dedicated characteristic-2 script supplies that certificate.

**Runtime:** no end-to-end runtime was retained for this failed version: the timer print was after the failed assertion. We do not invent a time or rerun this already completed exhaustive phase merely to obtain one.

### Second version: `code/part_a567_checks_second.py` and `.out`

The same 2,880 projective-triple candidates and 360 harmonic complementary-pair tests passed again. The reflection choice was corrected to r2=((0,1),(1,0)); all three involution square relations and the displayed SL2/GL2 product relations passed.

This version then failed on a structural SymPy equality between two mathematically identical polynomial matrices: `(A-I)*(A+I)==f*I` had not been simplified. The preserved failure was resolved by simplifying the difference to zero. No proposition used the failed unsimplified expression as a proof.

**Runtime:** likewise not retained because execution stopped before the final timer print. No retrospective runtime is claimed.

### Final version: `code/part_a567_checks.py` and `.out`

All assertions passed. The final program covers:

* The same 24 primes, 2,880 projective-triple candidates, all involution-pair candidates in each resulting stabilizer, and 360 complementary-pair harmonic tests. Stabilizer orders are 24 except for 120 at p=5; the numbers of Klein subgroups with that fixed-point union are 1 except for 5 at p=5; each normalizer has order24. Harmonic complementary pairs number3 except for15 at p=5.
* The three exact harmonic exceptional-characteristic expressions and all displayed integral reflection/product relations. Completeness of the abstract presentations is proved in the manuscript, not inferred from matrix multiplication.
* All 4^4=256 matrices modulo4, retaining the48 of determinant1. The explicitly listed four-element W is checked for closure (16 products), squares, and normality (48*4=192 conjugations). The eight-element mod2 kernel, the12 quotient cosets, the binary-dihedral relations, and all12 normal forms are checked.
* The universal-domain involution matrix and its matrix factorization by f=x^2+yz-1; every entry of its relation matrix vanishes at the specified residue point. Domain, exactness of the matrix factorization, generic rank and failure of invertibility are proved in the manuscript; their printed descriptions are not substitutes for those proofs.
* The25 candidate pairs (m,n) in [-2,2]^2 for norm m^2+mn+3n^2=1, yielding exactly (+-1,0). The manuscript's inequality restricts all units to this bounded set and proves the norm-Euclidean bound15/16, the F4 residue field and the three gluing classes. The field name, gluing count and Euclidean bound printed by the script are descriptions of that proof, not additional independent finite-field computations.
* The exact hexagonal Gram-matrix ratio3. The two H1 orders printed at the end are reported values from the separate cohomological proof, not computed cohomology by the script.

**Recorded runtime:** 0.236781 seconds, from the script's `time.monotonic()` timer started after imports. This is internal computation time, not process wall time including Python and SymPy startup. This already timed exhaustive program was not rerun for the present reporting audit.

## New finite characteristic-3 certificate

`code/part_a567_char3_inertia.py`, `.out`, and `_timed.out` enumerate all3^4=81 matrices over F3. The48 invertible matrices yield24 projective matrices and24 distinct permutations of all four points of P1(F3). It then explicitly evaluates all six anharmonic transforms at lambda=2=-1 and verifies that every value is2. This certifies the merged exceptional inertia S4 of order24; it does not replace the fixed-point-equation proof of the generic inertia statement.

The original output had no runtime. A single timing-only rerun at the parent's request passed with byte-for-byte identical output: **0.074782 seconds process wall time**, including interpreter startup. Original output preserved.

## New excluded-characteristic-2 certificate

`code/part_a567_char2_edge.py`, `.out`, and `_timed.out` implement F4=F2[a]/(a^2+a+1) exactly. All16 products of its four translations are checked. Each of its three nonidentity translations is checked to square to the identity and to fix exactly infinity among all five P1(F4) points. All four possible i are tested for i^2=1, with unique solution i=1. The standard displayed four maps are checked to have only two distinct values, and the six-set to have three points. The proof that no additional geometric fixed point appears after algebraic closure is the equation z+a=z forcing a=0.

The first output had no explicit timer. One timing-only rerun preserved it and reproduced it exactly: **0.049693 seconds process wall time**. This small new edge certificate is separate from the already timed odd-prime enumeration.

## Explicit collar certificate

`code/part_a567_collar_explicit.py`, `.out`, and `_timed.out` check the fixed example n=10000, epsilon=10^-14, with conformal collar cutoff heights1/100 and1/50. This is symbolic and rational arithmetic, not a sampled PDE solution. The exact scopes are:

* the separated-mode differential equation and its value/normal derivative at0;
* the quintic cutoff's two endpoint values and four vanishing endpoint derivatives, its factored first and second derivatives, and the exact extrema bounds obtained from the two critical points of the second derivative;
* two algebraic forms of the exact graph-curvature expression from the displayed connection;
* the rational collar-embedding estimates, cutoff derivative bounds, L(H)<=-1700, residual coefficient40600102300<2^100, and the supersolution sign;
* every fixed-parameter derivative/normal/curvature error inequality used in the text, especially 10*epsilon*n^3+epsilon^2*n^4=1/10+10^-12<1;
* the exact strict upper bound u<=-9991/2000000000000000 at the specified boundary point.

The continuous maximum-principle comparison, the collar theorem, and the area argument for positivity somewhere else are proved or precisely sourced in the manuscript; this script does not numerically approximate them.

The original output lacked an explicit timer. One timing-only rerun passed and exactly reproduced it: **2.734516 seconds process wall time**, including SymPy startup. Both outputs are kept. Parent and C researcher independently checked the full continuous proof; those are proof reviews, not additional numerical experiments.

## Independent exact plumbing review

`code/part_a567_plumbing_review.py`, `.out`, and `_timed.out` use only exact `Fraction` arithmetic for the parent's fixed numerical witness: R=3/2, A=420/569, B=3/4, c=289/4, t=9/11. Independent quotient-rule evaluation gives first derivative numerator0, second derivative271040/371353867, and cross-ratio323680/323761. These are exact evaluations at one completely specified parameter, not a parameter search. The global coordinate injectivity, retained images, and annulus overlap are proved separately in the review notes; the prose descriptions printed by the script report those arguments and do not themselves execute a topological check.

One timing-only rerun exactly reproduced the original output: **0.066977 seconds process wall time**. The parent's independent original witness program is outside this ledger; this row records only the child's independent arithmetic review.

## Timing record and nonmathematical scripts

The machine-readable timing record is `code/part_a567_timing_audit.json`. Every timing-only rerun returned exit code0 and `matches_original:true`; the original outputs were not overwritten. The only programs rerun in this timing audit were the four small scripts listed above, the fourth being the newly added characteristic-2 edge check. No exhaustive main version was rerun.

`part_a567_fetch_sources.py`, `part_a567_retrieval_metadata.py`, `part_a567_legacy_ids.py`, and `part_a567_audit_update.py` perform retrieval or ledger maintenance. They are not mathematical experiments, and their HTTP or file-writing times must not be interpreted as proof-verification runtimes. The original failed retrievals and both failed mathematical prototypes remain documented rather than silently discarded.
