# Independent audit of the native residual-ring certificate

Date: 2026-11-21 UTC. Reviewer: `/root/lean_chain`, GPT-6 Astra Pro; effort not exposed. Updated completed-report reconciliation cutoff: 16:26 UTC (initial cutoff 15:59 UTC). `certificate_audit_snapshot.json` records the exact reconciliation time and hashes. All six alternate unitary cases and all three initial-field full computations now have complete reports.

## Verdict

**The native determinant and wrapper preserve the exact residual-ring unit criterion.** The verifier still reconstructs the complete source and target invariant spaces, the whole harmonic kernel, all thirteen neighbor frames, every identifying evaluation, and both determinant-unit conditions. Its algebra is over a finite quadratic algebra modulo an arbitrary integer. No primality or squarefreeness assertion is used.

I read the complete 336-line archived `verify_ring_schur_parallel.py`, the complete native `ring_determinant.cpp`, the complete original and revised `ktower_complete_ring.py`, and both requested original proofs:

- K17-MINUS7-GENERAL-SOURCE, `input/RETURN_K17_checkpoint_08_20261121T0616Z/evidence/work/hecke_minus7/minus7_general_source_section.tex`, all 163 lines.
- K17-U3-RESIDUAL-RING, `.../hecke_minus7/higher3/u3_residual_ring_section.tex`, all 199 lines, including its full numerical-provenance paragraph.

The earlier group, lattice-class, local-packet, conductor, and harmonic-realization results used by those proofs remain carried background. They have not been re-proved in this audit. No Lean kernel run is claimed.

At the updated cutoff, complete reports certify all six alternate unitary comparisons and all six classical comparisons for e=26,28,30. The full initial-field e=26 calculation has carried complete reports whose hashes and entire input object have been freshly reconciled; the new full e=28 and e=30 integer-Faddeev replays are also complete and reconciled. Consequently these arguments prove **K52(Z)=K56(Z)=K60(Z)=0** under the stated source contract, theorem **KT-K52-K56-K60-VANISH**. The earlier identifiers KT-K52-VANISH and KT-K52-K56-VANISH are valid restrictions.

## 1. Native quadratic-algebra arithmetic

The coefficient algebra is

`B_M = (Z/MZ)[w]/(w^2-w+2)`.

For `x=a+bw`, the conjugate is `(a+b)-bw`, and its scalar norm is `a^2+ab+2b^2`. The formulas in `ring_determinant.cpp:12–22` implement precisely these identities, with exact GMP integers and reduction modulo positive M. An element is a unit if and only if its scalar norm is coprime to M: the inverse is its conjugate multiplied by the modular inverse of the norm. Conversely the determinant of multiplication by a unit is a unit; equivalently multiplying the element and its conjugate gives a scalar unit. This argument works even when B_M is a product or has nilpotents.

The determinant loop, lines31–42, uses row elimination. At stage k it searches the current column below the diagonal for a norm-unit pivot. A swap changes the accumulated determinant sign. Swapping only the still-active suffix is valid because all earlier column entries in both rows have already been set to zero. The update subtracts a multiple of the pivot row and preserves the determinant. Since the pivot is a unit, the usual block determinant identity shows inductively that the initial determinant equals the accumulated signed pivot product times the determinant of the remaining block. The final diagonal entry is multiplied without inversion. Thus every successful return is the exact determinant over B_M. The routine also correctly gives determinant one for the empty matrix.

If no individual unit pivot exists, the native routine exits with code2 and `unit pivot unavailable`. It makes no singularity assertion. This matters over composite rings: the matrix `[[2,3],[3,2]]` over Z/6Z has unit determinant one, although neither first-column entry is a unit. This matrix is included among the new controls and correctly yields an inconclusive result. A failed pivot therefore cannot be used as evidence of a nonunit automorphic comparison.

The wrapper requires successful process termination, exactly three output integers, the expected n-1 inversions, and residue representatives in `[0,M)`. It separately checks that the evaluation determinant and Schur-operator determinant have norm gcd one. A nonunit final diagonal entry can be returned by the determinant routine, but cannot pass the final unit criterion.

## 2. Independent small controls

The original `ring_determinant_controls.json` records twelve statuses and expected determinants but omits its input matrices and generator. It is therefore insufficient on its own to replay those exact controls. This is a provenance limitation, not a discovered arithmetic error.

The new `audit_native_controls.py` supplies 34 fully specified controls, storing every matrix and the random seed. It computes the expected determinant by the literal Leibniz permutation sum, independent of elimination. It tests both the existing native executable and a fresh executable compiled directly from the audited source. The moduli include composite integers, prime powers, the ramified modulus49, and a large residual integer. It also includes an explicit row swap, a nonunit final entry, and the invertible-without-unit-pivot example above.

Results: **28 exact returns, all equal to the Leibniz determinant, and six correctly inconclusive pivot searches**. Both executable versions agree in every case. Three malformed-input tests are rejected. The complete matrices, outputs, source and binary hashes, compiler command, and compiler version are in `audit_native_controls.json`. This check does not rerun any large 732-, 915-, or1125-dimensional model.

## 3. The retained complete-model checks

The original verifier is byte-for-byte equal to the frozen intake version, SHA256 `30af40a8ad6f0f7745973afef14b710d9a4457a03892dab86619c2206fba90ff`.

Its frame enumeration is exhaustive. The completed-square norm formula bounds the possible scalar coordinates for norms at most four; it constructs all orthogonal triples and applies the exact residue conditions from the carried frame theorem. It compares signatures after signed permutations and verifies the six norm-two and seven norm-four classes. It does not accept a selected subset merely because that subset matches a desired answer.

The complete signed-permutation orbit sets are recomputed at lines123–141. Each harmonic column is checked against the full contraction at lines155–173, with duplicate sparse indices rejected. The count is exactly the difference of source and target ranks, and distinct free coordinates give an identity minor. Under the checked factorial and group-order hypotheses, the carried split-contraction theorem gives constant kernel rank. Reduction at every maximal ideal, together with the identity-coordinate splitting and Nakayama, shows that the saved columns span the whole kernel over B_M. This is the exact argument of K17-U3-RESIDUAL-RING; no field-rank inference is made over a composite ring.

Lines179–194 check all consumed text data against the JSON model. Lines198–232 reconstruct each polynomial and all substituted values. Lines244–270 evaluate every identifying row, preserve its original index, and reject duplicate, missing, out-of-range, or wrong-size rows. The row computation is read-only in the shared model. Its parallel ordering therefore cannot affect either matrix. The two additional saved points are not checked by this residual-ring verifier; no extra-point claim is made.

The new wrapper changes the two determinant calls and the report/provenance handling. `certificate_audit_snapshot.py` mechanically compares all fifteen unchanged functions by AST and compares the entire pre-determinant validation segment byte-for-byte against every present generated script. All checks pass.

The revised wrapper uses a separate generated script for each case, records the native source and executable hashes, and accurately labels a producer-free computation as a **complete exact certificate**, not an independent numerical replay. If a producer `schur.json` exists, the modulus, weight, dimension, comparison point, and all three determinant values must agree with it. When no producer exists, all model checks and the final norm-unit test still remain. The older in-flight e28 script predates the new native-hash fields; the native source and binary hashes are separately captured in this audit snapshot.

## 4. Exact Schur semantics

Let `E=1+2^e+2^(2e)` and `k=e-1`. The carried two-class operator has block form `[[S11,inc],[S21,0]]`. When E is a unit, its full scaled comparison is invertible exactly when the endomorphism

`D_e = E^2 I - E 2^k S11 - 2^(2k) inc S21`

on the first invariant module is invertible. The inherited denominator cancellation identifies its evaluation matrix with

`S = E^2 A0 - E B2 - B4`.

The reconstructed rows are exactly this expression, with the same full six- and seven-frame sums. Since `det(A0)` is a unit, the ratio `det(S)/det(A0)` is the actual determinant of D_e. A unit norm for this ratio therefore proves the full two-class comparison is a unit at every coefficient place above every prime dividing M. The test includes both factors at split primes; it is stronger than a test at only one embedding. The carried integral conjugation involution gives the opposite minuscule direction as well.

The snapshot recomputes gcds with `336(2e-1)!` and E, both determinant norm gcds, the determinant-ratio identity, every recorded input hash, and the common frame hash. It does not infer completion from a producer status or from a progress line.

## 5. Completed numerical evidence at the cutoff

Define the residual moduli:

| e | label | M |
|---:|:---:|---:|
|26|1|697446897311|
|26|2|1346178024590512195284390892511906772585800385915601|
|28|1|323026426255399|
|28|2|1850161514202910077636429426241454885347275557889859421603|
|30|1|236017358500033404991|
|30|2|17825126775144482230877986030193435571179905679430331|

Completed unitary reports give the following scalar residues (the omega coefficient is zero):

| e,label | harmonic dimension | det(A0) | det(D_e) | status |
|:---:|---:|---:|---:|---|
|26,1|732|65303065346|243170653113|complete independent replay|
|26,2|732|1151061946436479205314087272743639226699780220614009|268141211335182978418440922413180866515460840367849|complete independent replay|
|28,1|915|222297174863416|110403897672730|complete independent replay|
|28,2|915|52319251349733998033648500176324776672876486412159569342|1469637909832672408423505694160941756010299985599249215332|new complete exact computation; no prior producer determinant claimed|
|30,1|1125|129139130004479025515|166602791931417452321|new complete exact computation; no prior producer determinant claimed|
|30,2|1125|11603147216938395361272501808831427722560693296986105|8004246273119905385907729021266082827377552171226936|new complete exact computation; no prior producer determinant claimed|

The two e26 rows have complete source and target dimensions 5197 and 4465; both e28 rows have 6942 and 6027; both e30 rows have 9094 and 7969. All identifying rows are recomputed in every case. Each norm gcd, the factorial/group-order gcd, and the scalar-pivot gcd is one. The e30 small report's SHA256 is `78b3cce4339c7f11a862234dc1e7fcae167d33cca31906cfc0bd2a830a1cf289`; the large report's is `7bad0979c5d24d2e1d1c101ebc53c1c97cb32cfc4c7d2568c641d3716628f5d2`. Both reports explicitly record the native source and executable hashes and the generated verifier hash. Their Schur evaluation determinants are respectively 195566545701080939166 and 14806090891308210598760418083384300028806578171116871; exact multiplication verifies `det(D_e)*det(A0)=det(S_e)` modulo each M. The labels in this table are taken directly from the final JSON fields; in particular, the small e30 `det(A0)` and `det(D_e)` must not be interchanged.

The full classical determinants `J_e=det((1+2^(2e))^3 I-T2^3)` have all six completed unit residues:

| e,label | full dimension | J_e mod M |
|:---:|---:|---:|
|26,1|101|564487428902|
|26,2|101|540110375711722242001383842413974682809788702229075|
|28,1|109|291047394117369|
|28,2|109|1361695747498278489585646473526121447210917280902628497429|
|30,1|117|106624733533355298729|
|30,2|117|11520444014513425541585786124609238893503523917343666|

I freshly checked every recorded determinant pivot is coprime to its modulus, each comparison point, the final residue gcd, and exact agreement of the support moduli and support-file hashes. These are report-reconciliation checks. The completed classical q-series computations and their prior code audits remain carried evidence; I have not counted them as fresh executions by this reviewer.

## 6. Arithmetic conclusions for e26, e28 and e30

The carried initial-field full e26 reports, original/sparse/integer-Faddeev, each have SHA256 `d68b88a445f2c3726ce84aee3465c290a03e184b2eed8f521d71c010642c2515`. Their data SHA256 is `e9983ef4e49a20d08e00b291d1345d5530851197b88edd5107638a414d20a119`. I verified that this is the current exact-data wrapper's hash and that its entire degree object equals the producer object now used by the residual-support collector. The neighbor hash also agrees. This is fresh reconciliation of carried full computations, not a rerun.

The new full e28 integer-Faddeev replay is complete in `ktower_full_replay_e28.json`, report SHA256 `93a510c1136be190c45333eac43e62598b7b275d2bb28f8466489dbb190b4c84`, input data SHA256 `e5f4785307ebaec12f692c36e08e84cca2e9a8264204d11c5f9c879c3697df85`. I reconciled its input hash, entire degree object, and neighbor hash against the current files. It reports complete neighbor evaluations, exact characteristic polynomials, and both extra points for the entire105-dimensional harmonic module. This is reconciliation of root's new execution, not another full execution by this reviewer.

The new full e30 integer-Faddeev replay is complete in `ktower_full_replay_e30.json`, report SHA256 `b1ddcc47506e3fa0613a39f83f82eb14a8bbc37a0d3960bb88bfc7f7bae8255a`, input data SHA256 `629d1a34dbeaae989d471f10178c4813d3b056b98530f7a9474b8fcce01d1cc0`. Its source, target and harmonic dimensions are 1057, 932 and 125. Every neighbor evaluation, both exact characteristic polynomials, and both extra points at each test prime pass. The snapshot reconciles its entire degree object and neighbor hash as well as its input hash. This is reconciliation of the completed execution, not another large-model execution by this reviewer.

For e in {26,28,30}, the independently checked exact support certificate proves that every prime at least 2^31 in the gcd of the full initial-field comparisons at 7 and 13 divides one of the two corresponding residual moduli. The smaller removed factors are explicitly proved primes below 100000; no large primality assertion is used. Repeated exact gcd division consumes the entire remaining integer, which is sufficient for prime support even when exponents are not retained in the modulus list.

Fix e in {26,28,30}. If K_(2e)(Z) had a nonzero primary part at a prime l, the carried Rognes–Weibel theorem excludes l=2 and the stipulated Vandiver/Kurihara input excludes every odd l<2^31. For l>=2^31, both 7 and 13 differ from l and the exact E=-3 GD condition holds. The closed OneChar theorem plus the full initial-field coverage therefore forces l into the displayed residual support. Both corresponding E=-7 unitary comparisons and classical cubic comparisons are units. Since l>2e+1, every hypothesis of K17-MINUS7-GENERAL-SOURCE is satisfied; it forces the strict Selmer group, hence by VK-PT the same K_(2e) primary part, to vanish. This contradiction excludes every prime. Finiteness gives K52(Z)=K56(Z)=K60(Z)=0. This is the full argument of KT-K52-K56-K60-VANISH, and it has been read in its entirety after the final e30 reports were reconciled.

## 7. What remains for all weights

The source criterion and coverage are uniform in e. Indeed the only use of `l>2e+1` in the complete K17 alternate-field proof is to ensure `(l-1) does not divide2e`. The same proof works under the sharper explicit arithmetic hypotheses: e>=2 even, l>=5 prime, l!=7, and `(l-1) does not divide2e`. All local weight arguments concern a positive characteristic-zero slope difference, not a Fontaine–Laffaille interval. This removes a source-range restriction, but does not prove the determinant-unit hypotheses.

The unresolved global assertion is a uniform exclusion of prime divisors common to the initial-field residual support and the alternate-field comparison determinants. For fixed e, let R_e have the remaining prime support of the full gcd at7 and13 after known vanishing primes are removed. Let F_e be the full integral two-class unitary comparison over E=-7 and J_e the full classical cubic comparison. A sufficient uniform assertion is

`gcd(R_e, Norm(F_e) * J_e)=1`

for every e, with any exceptional source characters removed separately. A failure of this sufficient test would only exhibit a common automorphic congruence; it would not construct a nonzero Selmer or K-class. The completed finite cases supply no theorem that this gcd remains one in all weights. The quartic size bound limits its size for each e and does not bound its prime support uniformly in e.

The modular harmonic/Schur implementation also has removable model restrictions. The factorial denominator must be a unit, as must the scalar pivot E. A saturated integral characteristic-zero harmonic lattice, obtained for example by exact integer normal forms, can avoid the split-contraction restriction; computing the full two-class determinant can avoid the scalar Schur pivot. Neither restriction is an intrinsic obstruction to the global criterion.

There is an elementary precise warning about the latter pivot: **the prime support of E_e is unbounded even for even e**. Given any B>=7, choose e positive even and divisible by p-1 for every prime5<=p<=B. Then E_e is congruent to3 modulo each such p. Also v3(E_e)=1, since2^e is congruent to1 modulo3 and `x^2+x+1` is congruent to3 modulo9 when x is congruent to1 modulo3. As E_e>3 and is odd, it has a prime divisor l>B. Moreover any l!=3 dividing E_e satisfies `(l-1) does not divide2e`: the opposite would imply x^2=1 and x^2+x+1=0 modulo l, hence x=-2 and l divides3. Thus a fixed small-prime cutoff cannot by itself justify the scalar pivot in every weight, even in the generic GD range. This observation does not claim those pivot primes lie in R_e; it only identifies why the current modular shortcut cannot be declared uniform without another argument.

## Check records

`CHECK_EVENTS.tsv` in this directory records the full-proof/code audit, native-control execution, generated-code equivalence, and exact report reconciliation as separate events. Carried background and carried computations are labeled as such. `certificate_audit_snapshot.py` may be rerun after new complete reports appear; that updates only this audit's JSON snapshot and cannot create a missing mathematical certificate.
