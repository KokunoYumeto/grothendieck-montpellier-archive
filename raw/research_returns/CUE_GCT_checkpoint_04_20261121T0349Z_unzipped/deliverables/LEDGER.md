# CUE_GCT research ledger

Run: CUE_GCT_20261121_R1.
Started: 2026-11-21T00:49:46.243176+00:00 (UTC). User-facing time zone: Europe/Berlin.
Model: GPT-6 Astra Pro; effort setting not exposed.

## Inputs and status conventions

Alpöge RH and Dirichlet GRH are accepted as stipulated theorem inputs. Masullo statements are conditional and known only through the supplied index. Proof checking here means model reading and exact finite computation when recorded, not formal certification.

## Initial gates

| Question | Status | Current gate | Owner |
|---|---|---|---|
| Q1 Rectangular bridge | Open | Extract rectangular Kronecker/plethysm coefficients without losing signs or determinant-boundary data | rectangular_bridge |
| Q2 Haar integrals | Open | Distinguish exact character projectors from positive coefficient formulas | rectangular_bridge |
| Q3 Isolation | Open | Convert path minimum uniqueness to cancellation-resilient, monomial-additive coefficient-basis isolation | isolation |
| Q4 Purity | Open | Control the tests needed for basis isolation with explicit conductor/degree/dimension bounds | purity_zero_status |
| Q5 Unconditional status | In progress | Match each theorem to its full analytic hypotheses | purity_zero_status |
| Q6 Grothendieck dictionary | In progress | Give integral and characteristic-zero scopes, exact source locators, and archive corrections only where supported | root |

## Review schedule

Checkpoint ZIPs are due after each 45 minutes of active elapsed work. Checkpoint01 has been created and persisted; subsequent checkpoint entries record their actual times. First substantive movement review is due at approximately three hours, followed by hourly reviews; two consecutive reviews without movement trigger stopping. Reviews will record actual elapsed times.

## 2026-11-21, approximately 01:33 UTC — substantive progress before the first checkpoint

This is a progress entry, not the three-hour movement review. Elapsed work is approximately44 minutes. There have not been two stagnation reviews, and no such stopping condition is claimed.

| Main question | Current state | Strongest established reduction or restricted closure |
|---|---|---|
| Q1 Rectangular bridge | Restricted formulas proved; general efficient positivity open | R01–R09 give exact transforms, ratios squared sums and closure Gram ranks. R10 closes height-two rectangles. G07 plus R12 gives the exact four-row per4-minus-det4 shifted plethysm formula. |
| Q2 Haar and boundary | Exact identities proved; efficient general extraction open | R05–R06 reduce closure multiplicities to explicit integral orbit-coefficient ranks; R08 identifies the indispensable quotient numerator. Generic energy shortcuts have stated lower bounds. |
| Q3 Isolation | Independent-variable transfer proved; general ROABP target open | I03–I04 give sufficient coefficient-matroid cones; I14 weakens this to joint coefficient-span preservation. I15 rules out bounded affine seed decoders; I18 identifies unit-minor preservation under regularization. |
| Q4 Purity | Sparse and actual-sheaf criteria proved; general encoding open | P09–P10 separate kernel avoidance from energy conditioning. P11 proves explicit common number-field points and integer hitting sets interconvert unconditionally in the rational model. |
| Q5 Zero statistics | Dependency audit completed for listed source statements | Supported Montgomery and Dirichlet-GRH first-zero statements are discharged under stipulated Alpöge; Hughes–Rudnick analytic moments were already unconditional. General Hecke examples are conditional on M; ILS target automorphic RH remains separate. |
| Q6 Grothendieck language | First complete dictionary written; independent review continuing | G01/G02 mathematical archive corrections; G03 finite-filtration counterexample; G04 integral rank specialization; exact SGA/FGA/EGA locators with source-check scope. |

### Further main-gate movement

- G05 proves ternary saturation, excluding all at-most-three-row multiplicity obstructions.
- G09 gives explicit finite low-variable determinant bounds of order m^((k−1)/2), with the already-known uniform-representation exponent credited to Boralevi et al. The consequence narrows permitted row lengths at a given padding size.
- R12 has integer per4 and per5 projection certificates; root independently verified all evaluation Jacobian entries using a different permanent formula.
- R13 has exact full-rank certificates for every permanent size1–16 and a dimension obstruction for all sizes≥17. A distinct Ryser-gradient method and separate modular elimination checked all3,348,864 certificate entries and residues; root whole-proof integration review is still in progress.
- R14 padding/dimension consequences are being written and independently reviewed; they are not silently counted as finalized until their full proof and events are present.

### Current verification and delivery work

The assembled single-file LaTeX manuscript, required registers, implications, complete agent work sources, and finite certificates exist. A native XeLaTeX build failed because this runtime lacks xelatex.fmt; an alternative TeX route is being investigated. No PDF verification is claimed yet. The first checkpoint will include all current work, including this limitation, and no earlier checkpoint ZIP.

## Checkpoint01 — 2026-11-21T01:35:07.755315+00:00

Actual elapsed work: 45.36 minutes. Full current deliverables and documentation packaged; no earlier checkpoint included. Persistence result is recorded beside the checkpoint after upload.


## 2026-11-21T02:04:27.835535+00:00 — rectangular shapes and width-three gate closed

This is an ordinary dated progress entry, not the scheduled three-hour review. No stagnation review has yet occurred.

| Main question | Current state | Strictly smaller gate or resolved subcase |
|---|---|---|
| Q1 Rectangular bridge | General uniform positive extraction open; new explicit restricted gaps proved | R15–R16 prove an unbounded genuine-padding range; G10 supplies a degree threshold; G11 specifies rectangular outer weights and a degree progression. G12 proves their exclusion for n>=4m/3. |
| Q2 Haar and boundary | Exact identities and stronger restricted orbit-closure ranks proved | The SL4 Haar projector is the rectangular invariant piece; the reductive quotient dimension and effective Veronese comparison force its positive multiplicity gap in G11. General orbit-boundary extraction remains open. |
| Q3 Isolation | Width<=3, one unknown order resolved by I21 | Explicit 21-parameter map and finite polynomial hitting set. Remaining gate: size and construction time polynomial jointly in growing width, length and degree. The matrix-invariant consequence needs this growing-width bound. |
| Q4 Purity/arithmetic | Width-three common algebraic point and integer hitting curve constructed in P12 | Explicit primitive field, bounded discriminant, and trace-dual coefficient-span preservation; no extra GRH input. General-width kernel-avoiding arithmetic or sheaf encoding remains open. |
| Q5 Zero statistics | Listed dependency audit complete | Source-specific RH predicates and support ranges retained; no new claim about full correlations or automorphic RH. |
| Q6 Grothendieck | Dictionary extended through R16, G12, I21, P12 | Quotient/Proj/Hilbert transport, cocharacter special fiber, local-Artin rank charts, finite flat arithmetic trace map. Original manuscript images remain unavailable. |

### Checks and source boundaries

Root whole-proof readings are recorded for R16, I21, P12, G10–G12. Independent full reviews of G10–G12 and R16 were obtained, with exact source checks. The broader claims of recent preprints are not substituted for these proved narrower statements. The three-hour review is still due at approximately03:49:46 UTC.

### Document status

The local XeLaTeX format was repaired and the manuscript now compiles. A current build and visual page inspection are being performed before the next checkpoint; no completed visual review is asserted in this entry.


## 2026-11-21T02:11:27.653700+00:00 — further proof-checked movement

R18 improves the unbounded genuine-padding ratio to every fixed value below sqrt(3/2), with explicit rectangular labels through G11. R17 gives exact determinant-image dimension and two concrete padded pairs where the forced four-row gaps must be nonrectangular. G13 reduces the first rectangular-gap degree bound to one whose logarithm is O(n²logn), using cumulative quotient filtrations instead of a factorial Veronese. I22–I25 precisely test the next growing-width repairs: false active-simple-block claims are refuted; every-seed Plücker-compatible code masks have quantified cost; preserved-rank words can require exponentially supported lowest components; invertible chunks nevertheless admit an intrinsic Grassmannian support bound. Root whole-proof checks and independent reviews are recorded. This is an ordinary progress entry, not the scheduled three-hour review.


### 2026-11-21T02:16:57.127476+00:00 — compatible row/column extension

R19 passed the full root proof reading and independent exact symbolic identity checks. It improves the unbounded genuine-padding ratio to every fixed value below sqrt(5/3), still below the rectangular exclusion at4/3. The stronger finite first-gap bound G13 applies to this range as well. A further staircase construction remains only a candidate because adjacent local support conditions conflict; no additional range is asserted.

## Checkpoint02 — 2026-11-21T02:20:54.104302+00:00

Actual elapsed work: 91.13 minutes. Full current deliverables and documentation packaged; no earlier checkpoint included. Persistence result is recorded beside the checkpoint after upload.


## 2026-11-21T02:22:55.994767+00:00 — first-jet boundary and centered interpolation test

G14 is proved and whole-proof checked: determinant pencils dominate their first two padding-coordinate jets, so every positive four-row padded-form multiplicity gap needs lambda1>=d(n-m)+2. The higher-jet extension has a precise remaining dominance gate. I26 supplies nonzero centered-SV_k annihilators of degree k+1 and width binom(2k+2,k+1), including a width-four one-pair example; it forces at least logarithmically many pairs within that particular generator family. Its commuting construction is compared with the established commuting-ROABP literature, and its monomial cocharacter repair is explicit. This is an ordinary progress entry, not the scheduled three-hour review.


## 2026-11-21T02:32:13.951226+00:00 — third-jet gate closed

G-Q15 changes from OPEN to PROVED by G15: a uniform explicit sl2 pencil dominates the full third jet. G-Q16 is refuted for the fourth and higher full jets by dimension. The multiplicity boundary is lambda1>=d(n-m)+4, with d(4m-3n)>=16 for rectangles. Root read the full proof and independently checked actual cofactor ranks for sizes2–18. I27 closes the filtered-code repair by a carry-free cocharacter argument, and I28 sharpens the width-three generator from ten to eight pairs using the endpoint hyperplane argument. This is an ordinary progress entry, not the scheduled three-hour review.


## 2026-11-21T02:49:47.282460+00:00 — exact rectangle range, arithmetic ranks, and rank-spectrum compression

R20 closes the eventual four-row rectangular padding range: all integers m>=8000001 and m<n<4m/3 admit the explicit G11/G13 gaps, while G12 excludes the complementary threshold. Its larger dimension range forces nonrectangular gaps. Root independently derived and checked the finite R20 certificate. R21 adds exact fixed-ambient-dimension orbit-multiplicity computation and arithmetic spectral bounds. I29 handles one singular rank with a polynomial pair budget, I30 gives six pairs at width3, and P13 gives the corresponding field degree(nD+1)^13. I31 has now passed independent root and purity full proof reviews and closes the original-coordinate fixed-width construction using matrix cones. Its growing-width recurrence and sampling exponent remain insufficient for the main target. This is an ordinary progress entry, not the scheduled three-hour review.


## 2026-11-21T02:51:28.366087+00:00 — a specified nonrectangular label in every certified padded range

G-Q17 changes to PROVED by G16. The enhanced Segre-Veronese cone extracts lambda=(d(n-m)+md/4,(md/4)^3); its stable Fermat tensor exists for arbitrary padding, so all dimension-certified pairs receive this exact nonrectangular family and explicit degree bounds. Root independently rederived the full proof and reopened the general Derksen finite-kernel bound on primary p956. This is an ordinary progress entry, not a scheduled review.


## 2026-11-21T02:57:28.097273+00:00 — stretched directions classified and coordinate deletion ruled out

G-Q18 is PROVED by G17: the exact four-row stretched-direction criterion in every dimension-certified padded pair is nu4>0 and nu1>(n-m)s. Root checked the entire proof, including Cartan coordinate rings, stable points and quantitative bounds. I32 refutes polynomial full-cone coordinate deletion at every rank-preserved common center, with an exact exponential threshold. I33 proves a small prime-cocharacter family and its scalar product repair in a known restricted PIT class; this is not counted as a solution of the general matrix gate. This is an ordinary progress entry, not a scheduled review.

## Checkpoint03 — 2026-11-21T03:04:56.574520+00:00

Actual elapsed work: 135.17 minutes. Full current deliverables and documentation packaged; no earlier checkpoint included. Persistence result is recorded beside the checkpoint after upload.


## 2026-11-21T03:28:49.944712+00:00 — every-stretch comparison and weaker isolation gates

G-Q19 and G-Q20 are PROVED by G18 after complete root and independent purity proof readings. The exact direction criterion now yields gaps at every sufficiently large integer stretch, including rectangles; the all-integer ratio and an effective reverse dimension range are proved. Every fixed four-row direction eventually has no occurrence obstruction. I34 passes root/purity full proof checks and an independent root exact example computation; bounded local nullity gives the stated dense prime family. P14 passes root/isolation full proof checks and replaces full matrix-cone preservation by scalar bridge conditions for rank-one/full-rank factors. This is an ordinary progress entry, not the scheduled three-hour review.


## 2026-11-21T03:36:20.545165+00:00 — uniform four-variable dimension ceiling reached asymptotically

RQ-26 is PROVED by R22 after author and independent root/isolation whole-proof checks, plus an independent purity check of sections6–9. For m>=99, c_m>=4m²−20m^(3/2)+2; every fixed padding ratio below sqrt(2) is now covered with a stated threshold. The remaining dimension transition is at most O(sqrt(m)) below sqrt(2)m. R22 lowers the exact eventual rectangular boundary threshold to m>=2025. G17–G18 supply all strict directions and every sufficiently large stretch; the G17 first-stretch bitlength corollary is checked separately. This is an ordinary dated progress entry, not the scheduled review, which remains due at03:49:46UTC.


## 2026-11-21T03:42:33.177105+00:00 — exact derived-restriction gate and one-pair counterexample

R23 identifies the permanent four-variable dimension defect with one degree-m Tor_1 group and proves all earlier Tor_1 degrees vanish generically. The old linear syzygies are explicitly controlled; unrestricted exactness after restriction is refuted by the positive defects for sizes3–16. Root checked the whole proof and exact primary-source locators. P15 refutes the tested one-pair width-three strengthening for the specified node conventions, with full root and isolation reviews. The latter closes a simplification attempt but is not counted as movement on the polynomial-in-width target. This is not the scheduled review.


## First scheduled movement review — 2026-11-21T03:49:47.471011+00:00

The three-hour review was due at 2026-11-21T03:49:46.243176+00:00 and actually performed at the timestamp above. The comparison baseline is the start of this run; earlier dated updates were not reviews. **Movement: YES. Consecutive reviews without movement: 0.** No stopping condition has been reached. The next actual review is due at 2026-11-21T04:49:46.243176+00:00.

Movement is supported by open rows changing state and by the strictly smaller gates below. Side calculations, repeated statements and packaging do not count. Fixed-width and restricted-rank results are not reported as polynomial-in-width PIT.

| Main question | Status and movement | Strongest remaining gate |
|---|---|---|
| Q1 Rectangular bridge | MOVEMENT: R22 reaches the asymptotic four-variable dimension ceiling, R23 identifies its exact remaining defect, and G17–G18 classify fixed strict directions and all sufficiently large stretches. | For m≥17 determine the single degree-m Tor defect ε_m. General ambient dimension and polynomial-size positive extraction remain open. The proved four-variable range covers every fixed n/m<√2; the exact eventual rectangular range m<n<4m/3 holds for m≥2025. |
| Q2 Haar integrals and orbit boundaries | MOVEMENT: R21 supplies exact fixed-ambient-dimension multiplicity computation; G17–G18 turn enhanced invariant quotients into fixed-direction comparison and an all-integer asymptotic ratio. | Control Schur-isotypic Gram ranks and boundary ideals with size polynomial in the growing parameters; positive ambient moments alone do not isolate a desired coefficient. |
| Q3 Isolation and matrix invariants | MOVEMENT: I31 closes the explicit unknown-order construction for every fixed width. I34 and P14 close bounded-local-nullity and rank-one/full-rank subcases. P15 closes a tested one-pair simplification by counterexample, without moving the general polynomial-in-width gate. | Obtain a seed budget and sampling/construction cost polynomial jointly in length, degree and growing width. The current rank-level recurrence and its sampling exponent remain too large; general intermediate-rank resets are unresolved. |
| Q4 Purity and arithmetic | MOVEMENT: P13 gives explicit arithmetic hitting points and exact trace-coordinate span recovery in every fixed width; P14 transports the sharper restricted generator. | Construct a uniformly efficient kernel-avoiding encoding or a purity family that tests arbitrary coefficient vectors without exponential feature size. P11 identifies the exact unproved encoding step. No additional Dirichlet GRH implication is inferred. |
| Q5 Zero statistics | RESOLVED AUDIT: source-specific RH/GRH predicates and support restrictions are tabulated under the stipulated Alpöge input; Masullo-dependent claims are marked conditional. | Unrestricted correlations, unrestricted support and automorphic hypotheses beyond Dirichlet/Hecke GRH remain additional statements. The stipulated theorem is used as requested, not truth-audited. |
| Q6 Grothendieck transport | MOVEMENT: the checked findings are restated in scheme, representation-ring, quotient, filtration, trace and derived-restriction language, including the new SGA6 Tor-independence dictionary. | Original cote133 scan images are unavailable, so transcription corrections are mathematical necessities, not verified readings of ink; the exact missing Masullo §1.2 numbered locator remains a source gate. |

### Complete row-by-row status at this review

All rows are reproduced so that no open row or remaining extension is omitted. A proved restricted statement and its open extension are distinct: an extension in the final column does not revoke the proved status. Draft I35 is not integrated or counted as movement in this review.

| ID | Question | State | Finding or current gate |
|---|---|---|---|
| RQ-01 | How exactly does the rectangular moment act on GCT rectangular Kronecker coefficients? | proved: R-01, R-02 |  |
| RQ-02 | Does positive finite CUE dimension force every desired coefficient positive? | refuted: R-03; g((3,1),(2,2),(2,2))=0 despite finite dimension20 |  |
| RQ-03 | Can the exact unitary swap sum be projected onto the multiplicities? | proved: R-02; sum/regularize before coefficient extraction |  |
| RQ-04 | Does the stated RH/GRH input justify arithmetic recipe off-diagonal estimates or a GL-character map? | current gate: a new off-diagonal theorem and an explicitly defined character comparison; neither is provided |  |
| RQ-05 | Can the Kronecker and plethysm multiplicities be represented by compact-group projectors and positive squares? | proved: R-02, R-04; no polynomial-size count claimed |  |
| RQ-06 | Can the single-power laws be made independent inside full plethysm? | refuted: R-04; mixed U2 moment2 versus independent value0 |  |
| RQ-07 | Can Haar moments recover actual orbit-closure multiplicities rather than only stabilizer upper bounds? | proved: R-05, R-06; exact Gram-rank identification |  |
| RQ-08 | Can signed Weingarten integration be replaced by positive finite data? | proved: R-06; Gaussian coefficient Gram and integral minors, with exponential size |  |
| RQ-09 | Can concrete highest-weight witnesses survive on determinant orbit closure? | proved: R-07; centered pencil basis in stable two-row range and all-two-row survival |  |
| RQ-10 | Can a length-at-most-two multiplicity obstruction separate padded permanent and determinant? | refuted: R-07; determinant multiplicity equals ambient upper bound |  |
| RQ-11 | Can the exact ratios theorem yield a nontrivial identity in the GCT coefficients? | proved: R-09; sum of squared coefficients and monotone length cutoffs |  |
| RQ-12 | Do these constructions solve efficient positivity or asymptotic determinant/permanent multiplicity separation? | current gate: explicit polynomial-size control of structured Schur-isotypic Gram minors after excluding the shape/padding sectors proved in the root findings |  |
| RQ-13 | Do the quantum-group papers prove any complete positive rectangular family? | proved cited case: R-10 resolves height two; conjugating both inner labels resolves width two |  |
| RQ-14 | Do these sources provide an unconditional general constructive rectangular/plethysm formula or a classical-RH implication? | source audit: proposed general basis and complexity properties remain conjectural; exact missing gates recorded in findings.tex |  |
| RQ-15 | Can degree<=3 padding be separated by a multiplicity obstruction with <=4 rows? | refuted: R-11, for every n>=m and every coordinate-ring degree over C |  |
| RQ-16 | Can the determinant four-row ideal be proved nonzero on a permanent orbit, beyond a potential equation? | proved: per4/per5 quaternary dominance; exact per4 multiplicity gap1 at d=320112+s and lambda=(320112+4s,320112,320112,320112) |  |
| RQ-17 | How far can permanent four-variable dominance sharpen the determinant boundary gate? | proved complete dominance range1..16; fails for every n>=17; finite multiplicity deficits exist for4..16 |  |
| RQ-18 | Does the four-variable rank result survive any genuine padding n>m? | proved finite padded ranges8<=m<=16 through n22; general criterion c_m+3>2n^2+2; no asymptotic generic-fiber theorem claimed |  |
| RQ-19 | Can the finite four-row gap extend to every unpadded matrix size without extrapolating a computed rank? | proved for all n>=4 by symbolic rank lift; the unbounded genuine-padding gate is subsequently crossed in R-16 |  |
| RQ-20 | Can a proved growing permanent projection rank support genuine padding for unbounded m? | proved: c_m>=2m^2+2+h_m(m-3), h_m=min(floor(m/2),m-3); n=m+1 all m>=8; any fixed ratio below sqrt(5)/2 eventually; no maximal generic-fiber formula claimed |  |
| RQ-21 | Is the determinant dimension bound attained, and can proven four-row gaps be forced away from rectangles? | proved: determinant dimension exact; pairs(15,20),(16,22) have four-row multiplicity gaps while G12 excludes the rectangular sector |  |
| RQ-22 | Can the unbounded padding range be increased without overlapping-row interference? | proved: use both exact local cofactor identities in disjoint blocks; dimension>=3m^2-O(m), padding ratios below sqrt(3/2), explicit G11 rectangular multiplicity gaps |  |
| RQ-23 | Can row and column cofactor identities coexist in one sparse deformation and improve the growing padding ratio? | proved: disjoint row triples preserve both exact supports; four independent classes per interior Fourier character give dimension>=(10/3)m^2-O(m), hence padding ratios below sqrt(5/3) |  |
| RQ-24 | Can a proved uniform projection-rank bound reach every integer below the rectangular padding boundary? | proved for m>=8000001: eight independent normal families per five-row motif, only boundedly many exceptional modes; rectangular gaps exist for all m<n<4m/3 and G12 excludes every n>=4m/3; nonrectangular gaps extend to fixed ratios below3/sqrt5 |  |
| RQ-25 | Can integer structure make rank recovery quantitative or efficient in a nontrivial restricted regime? | proved spectral gap and fixed-height counterexample; exact MxM kernel avoids N^D rows; fixed N gives polynomial-in-numerical-nd bit complexity, while growing N and random-integral evaluation costs remain separate gates |  |
| RQ-26 | Can a proved uniform motif reach every fixed padding ratio below the four-variable dimension ceiling? | proved: arbitrary b supplies2b-2 independent normal classes in one pencil; selecting parameters over all bidegrees removes the root-order gate; c_m=4m^2-O(m^(3/2)) and every fixed ratio below sqrt2 follows, while the dimension method itself cannot reach sqrt2 or superlinear padding |  |
| RQ-27 | Does the known full-variable linear strand prove exact maximal four-variable permanent dimension? | no: the precise extra term is Tor1(R/J_m,S)_m, positive generically for3<=m<=16; full regular-sequence restriction is impossible; vanishing of that graded piece for m>=17 is the remaining exact-dimension gate |  |
| I-Q01 | Transfer Hoza to polynomial-size hitting sets for arbitrary width-w ROABPs | OPEN | I-G01: explicit polynomial cocharacter family meeting ROABP coefficient-matroid cones, or weaker sufficient joint coefficient-span condition. |
| I-Q02 | Does Hoza give polynomial hitting sets for independent vertex/edge-variable path polynomials? | PROVED | I-01 |
| I-Q03 | Do graph min-isolating weights automatically descend under identification of equal ROABP variables? | REFUTED | I-02: two-path diamond; kernel of monomial map not preserved. |
| I-Q04 | Characterize basis isolation as flags, scalar-projection minima and open cocharacter cones | PROVED | I-03; I-10 |
| I-Q05 | Do projected coefficient-matroid vertices have unique indexed basis fibers, and do polynomial random weights suffice? | PROVED | I-04; randomized only. |
| I-Q06 | Does positive Gram determinant alone certify coefficient rank after monomial substitution? | REFUTED | I-05: e1*x+e2*y at x=y=t. |
| I-Q07 | Can every successful nonlinear exponent-filter lift be implemented by polynomially many fixed original black-box evaluations? | REFUTED | I-06: Hankel moment rank 2^n for actual Hoza three-symbol filters. Exact linear implementation only. |
| I-Q08 | Derive the precise matrix-invariant consequence of polynomial ROABP hitting sets | PROVED CONDITIONAL REDUCTION | I-08; antecedent remains I-G01. |
| I-Q09 | Can independent Haar averaging preserve state isolation while restoring conjugation invariance? | REFUTED | I-07: twirling makes each insertion scalar; correlated formula may be signed. |
| I-Q10 | Do squared coefficient norms supply a positive polynomial transfer identity? | PROVED | I-09; white-box identity only. |
| I-Q11 | Do direct exterior or subspace-state graph lifts close the transfer? | REFUTED FOR STATED CONSTRUCTIONS | I-11: determinant cancellation remains; literal subspace state counts are large. |
| I-Q12 | What exact arithmetic decision is needed to form the support graph before isolation? | PROVED | I-12: specified coefficient nonzero is coC_=L-complete in the stated integer ROABP model. |
| I-Q13 | Do the findings prove general PIT, permanent lower bounds or P versus NP? | OPEN | No such implication proved; main antecedent I-G01 remains open, and general GCT V Theorem5.14 requires stronger PIT than the matrix case. |
| I-Q14 | Can a polynomial number of fixed black-box evaluations reproduce coefficient energy through an exact universal quadratic formula? | REFUTED FOR STATED FORMULAS | I-13: Q >= (delta+1)^n already for width-one products; quadratic cross terms and signed weights allowed. |
| I-Q15 | Can several compatible monomial substitutions jointly preserve coefficients when no individual member is BIWA? | PROVED | I-14: exact rank/kernel/Plucker criterion and explicit complementary rank-one example. |
| I-Q16 | Can fixed bounded affine decodings or averages of Hoza seed masks give sufficient variable cocharacters, even jointly? | REFUTED FOR STATED DECODERS | I-15: subset-sum collision gives multilinear width-two binomial; same-alphabet decoder already fails on x1-x3. |
| I-Q17 | Does the exact q^w support automaton imply a polynomial uniform base-field hitting set? | REFUTED AS A GENERAL IMPLICATION | I-16: exact arithmetic lift exists, but base-field width-one hitting sets require (q/(q-delta))^n points. |
| I-Q18 | Give a fully explicit unknown-order hitting set for square generically invertible univariate factors and constant boundaries | PROVED RESTRICTED | I-17: common shift plus support at most w-1; field-size and cardinality explicit; AGKS prior restricted results cited. |
| I-Q19 | Does generic invertibility plus low-support sampling automatically survive specialization? | REFUTED; NEXT GATE IDENTIFIED | I-18: pair-difference counterexample and unit Plucker minor criterion; generic saturation alone is insufficient. |
| I-Q20 | Does a known positive construction handle arbitrary unknown-order univariate width two? | BACKGROUND POSITIVE RESULT | I-B06: Lemmas32/33 and Theorem34, rank-one cuts and scalar-product closure. |
| I-Q21 | Can higher-rank cuts and joint block compression close polynomial PIT? | FIXED-WIDTH CASE PROVED; POLYNOMIAL VARIABLE-WIDTH CASE OPEN | I-19 gives the exact coupled-block reduction; I-31 supplies a polynomial hitting set for every fixed width in original coordinates, including cut multiples. I-30 sharpens width three to six pairs. Polynomial dependence on variable width remains open. |
| I-Q22 | Can bounded total generic corank be handled uniformly with unknown variable order? | PROVED RESTRICTED | I-20: explicit grid, common shift and support budget w-1+kappa; size (nw(delta+1))^{O(w+kappa)}. |
| I-Q23 | Can arbitrarily many rank-two cuts in width three be handled uniformly when the variable order is hidden? | PROVED SPECIALIZATION; INDEPENDENTLY READ | I-21: t*1+SV10; all characteristics; exact polynomial sample count and extension-evaluation convention. Direct proof attributed to unrefereed source mechanism. |
| I-Q24 | Do current known-order or every-order results by themselves settle one hidden order? | SCOPE VERIFIED | I-B07 distinguishes the classes/promises; I-22 identifies false foundational reductions in Singh-Singh2026. I-21 is separately proved and does not rely on that preprint. |
| I-Q25 | Does the claimed active-simple-block reduction provide a valid existing fixed-width bound? | REFUTED PROOF STEPS; HEADLINE NOT DISPROVED | I-22: zero scalar with full generated algebra, and nonzero radical computation killed by every simple quotient. |
| I-Q26 | Can all binary Hoza seeds act diagonally while preserving every decomposable r-vector at logarithmic seed length? | REFUTED FOR THE STATED REPAIR | I-23: 2<=r<=w-2 forces code bits to be constants or single membership literals; ell>=w*d/2. |
| I-Q27 | Does preservation of every interval rank above one force polynomial-in-width support in rank-one tests? | REFUTED | I-24: h_w=3*2^(w-2)-2 exact monomial, every interior interval generic rank equals constant rank>=2, genuine final rank-one test. |
| I-Q28 | Can decomposability improve arbitrary compound-space compression for invertible chunks? | PROVED RESTRICTED | I-25: projective Grassmannian dimension retains <=r(w-r) variable positions; at most2 extra endpoint variables. Does not cover singular resets or every lowest-component monomial. |
| I-Q29 | Can a fixed number of centered SV pairs hit every growing-width rank-test polynomial? | REFUTED; LOGARITHMIC NUMBER REMAINS OPEN | I-26: centered SV_k annihilator of degree k+1, any-order unipotent width binom(2k+2,k+1), with all interior interval ranks preserved; k=1 has width-four example. Requires n>=3k+2 distinct nodes. |
| I-Q30 | Can a short actual Hoza code be repaired by retaining only decomposability-preserving seeds? | REFUTED FOR THE STATED REPAIR | I-27: coherent seeds form a coordinate face; every active bit is coherent; ell<=w-2 leaves two indistinguishable ground elements and an invertible width2 linear cancellation. Dense additions and arbitrary decoders remain outside the claim. |
| I-Q31 | Is a logarithmic pair bound still open for the commuting subclass of I26? | KNOWN POSITIVE; GENERAL HIDDEN-ORDER CASE OPEN | I-B08: FSS2014 Corollary4.3 gives SV with1+2floor(2log2w) pairs for the every-order class; the new open dense-generator question concerns the full rank-test class. Sampling the pairs still costs quasipolynomial size by interpolation. |
| I-Q32 | Must invertible compound chunks pay two extra endpoint support positions? | NO WHEN ENDPOINT CONSTANTS ARE NONZERO | I-28 uses the proper Grassmann hyperplane dimension drop to include both endpoints in r(w-r); this sharpens the width3 construction to t*1+SV8 with explicit polynomial sampling bound. |
| I-Q33 | Can unbounded noncommuting cuts at one fixed singular rank be handled with polynomially many interpolation pairs? | PROVED RESTRICTED; SAMPLE SIZE STILL EXPONENTIAL IN WIDTH | I-29: interval ranks in{r,w} give sharp support h=r(w-r)+w-1 and centered SV with2r(w-r)+w-1 pairs; arbitrary many rank-r cuts allowed. |
| I-Q34 | Can nonzero polynomial endpoints be absorbed while preserving singular interval ranks? | PROVED; WIDTH3 SAMPLER IMPROVED TO SIX PAIRS | I-30: unit-factor absorption preserves the full interval profile; rank2 tests need2 pairs and rank1 tests4, yielding t*1+SV6 in all characteristics with exact sample count. |
| I-Q35 | Can the compound-state exponential dimension be avoided for a bounded number of interval rank levels? | PROVED; FIXED-WIDTH ORIGINAL-COORDINATE CASE CLOSED | I-31: direct full matrix cones yield K_R<=2w^2(4w^2)^(L-1), polynomial pairs for bounded L and2^{O(wlogw)} for all ranks; sampling still has exponent K_R. Polynomial dependence on variable width remains open. |
| I-Q36 | Can a polynomial dimension charge preserve every full matrix cone by retaining residual coordinates at the common center? | REFUTED FOR THIS EXACT CRITERION | I-32: paired-reset words need exactly h=3*2^(w-2)-2 retained positions, with all interval ranks already preserved at every common center; centered SV1 still detects the distinguished scalar. |
| I-Q37 | Can polynomial integer weights separate dense products without expanding their monomials? | PROVED FOR TWO PRODUCTS AND SCALAR PRODUCT CLOSURE | I-33: n+1 prime-weight curves and a polynomial grid hit differences of two univariate products in every characteristic; raw family fails under products, but Lagrange interpolation repairs that closure with polynomial size. General matrix-product cancellations remain open. |
| I-Q38 | Can prime cocharacters be repaired for growing term count without expanding all monomials? | PROVED FOR BOUNDED LOCAL NULLITY; GENERAL NULLITY OPEN | I-34: a local factor coefficient matrix of nullity c needs at most max(1,c) varied coordinates, with polynomial weights and (n*delta)^{O(c)} samples. Three terms need one coordinate; tensor-rank4 already defeats every entire one-coordinate cylinder. Joint coefficient span is preserved over the working extension. |
| P-01 | Can pairwise trace cancellation imply hitting? | Proved restricted criterion | A Gram lower bound a−(s−1)b>0 ensures injective coefficient evaluation. Sparse sign polynomials satisfy it if epsilon(s−1)<1. Remaining: Need a controlled dimension/energy parameter; width alone is insufficient. |
| P-02 | Can purity give an explicit polynomial hitting set? | Proved for sparse multilinear class | Quadratic-character sampler p>16 n²s², size O(n²s²), hits all s-sparse multilinear polynomials in characteristic zero. Remaining: General ROABP support can be exponential; no general PIT conclusion. |
| P-03a | Does a polynomial sign sampler hit all width-one ROABPs? | Refuted | Every proper subset of the sign cube misses the width-one product attached to an omitted point. Remaining: Refutes this output alphabet/sampling transfer only. |
| P-03b | Does adding a common affine shift and scale repair sign sampling? | Refuted | The three-variable Vandermonde has width 3, individual degree 2, and vanishes whenever all coordinates use two common values. Remaining: Coordinate-specific/richer alphabets require a new argument. |
| P-04 | Can Schwartz–Zippel be applied to a pseudorandom curve grid? | Proved conditional-on-restriction criterion | q+1−2g√q−#boundary(Fq)>degree pole budget suffices when f restricts nontrivially to the curve. Remaining: The nonzero-restriction and explicit-enumeration gates remain. |
| P-05 | Can a bounded-pole union of curves annihilate low-width polynomials? | Proved obstruction | A common nonzero bivariate annihilator has each degree at most 2 sum delta_j and ROABP width at most 2 sum delta_j+1. Remaining: Does not exclude curve families with much larger total pole budget. |
| P-06 | What does monodromy-aware Frobenius orthogonality actually prove? | Proved restricted trace-space criterion | q>s²B² implies independence of s pairwise geometrically distinct pure irreducible trace functions; B is quantified by ranks, genus, boundary, Swan terms. Remaining: Need an actual ROABP encoding into this controlled function space, not just a purity slogan. |
| P-07 | Can a next explicit isolating-weight construction survive arbitrary coefficients? | Proved for bounded support | p>max(2,d,n binom(s,2)), w_i(t)=1+rep(t^i), yields injective support weights for some seed and hitting size p(ndp+1). Remaining: Coefficient-matroid basis isolation is needed to replace exponential support by width. |
| P-08 | Can number-field GRH transfer into a hitting set? | Conditional reduction proved; encoding unconstructed | A common Galois extension and Frobenius-to-nonvanishing map with polynomial degree/log-discriminant yield a polynomial hitting set via Chebotarev. Remaining: Abelian fields use stipulated Alpöge; arbitrary fields use Masullo conditionally. Common encoding gate remains. |
| P-Z01 | Which Montgomery conclusion follows after stipulated RH? | Dependency discharged in exact supported range | Weighted ordered-index pair correlation with support hat f compact in (−1,1), normalization T log T/(2pi), and explicit diagonal term. Remaining: Full-support and nearest-neighbor laws retain additional analytic gates. |
| P-Z02 | Are Hughes–Rudnick Gaussian moments newly unconditional? | Corrected hypothesis classification | Analytic mean/variance/restricted moments already unconditional with complex ordinates. Alpöge gives real ordinates and discharges §8 GRH. Remaining: Finite restricted Gaussian moments are not all microscopic Gaussian moments. |
| P-Z03 | Does Hecke GRH discharge ILS and all automorphic statistics? | No blanket transfer | ILS cuspidal GL2/symmetric-square GL3 target RH remains; Hypothesis S is additional. Gao–Zhao quadratic/quartic Hecke statistics are conditional-on-M examples. Remaining: One-dimensional Hecke characters are distinct from general Hecke cusp forms. |
| P-Z04 | Are function-field moments and arithmetic moment recipes all proved by purity/RH? | Scope separated | Fixed-parameter equidistribution, q-aspect bounds, and Sawin Cor1.8 unbalanced degree-aspect case are proved; general cohomology/uniformity and arithmetic CFKRS gates remain. Remaining: No universal claim about all later literature; listed source statements only. |
| P-Z05 | Does stipulated RH supply a quantum-chaotic operator? | No such deduction | Berry–Keating/BGS connection remains a symmetry/spectral-construction heuristic; a specified arithmetic Hamiltonian and universality are extra gates. Abstract diagonal realization is elementary once the real spectrum is supplied. Remaining: Memory-based qualitative account explicitly marked; bibliographic locators verified. |
| P-09 | Can positive approximate energy cubature remain polynomial-size for low width? | Proved deterministic obstruction | For all width-one products, two-sided constants a,b force M≥(δ+1)^n a/b; relative error ε gives M≥D(1−ε)/(1+ε). Remaining: This obstructs uniformly conditioned positive energy approximation, not hitting alone. |
| P-10 | What weaker positivity condition is sufficient for tensor-train PIT? | Proved equivalence and sharp width-one result | Kernel avoidance of the closed TT cone is equivalent to a positive minimum on its unit sphere; generic dim(TT cone) samples suffice existentially, also for unknown order by a finite union. Width one needs exactly nδ+1 points. Remaining: Generic existence does not construct a small explicit sampler; any M-point sampler has energy ratio at least D/M. |
| P-11 | Does an explicit common number-field nonvanishing point give a new GRH transfer? | Proved unconditional encoding equivalence | Primitive-element coordinate polynomials give an integer grid of size (nδ+1)(nδa+1) without GRH; a known integer hitting set conversely yields a polynomial-degree cyclotomic point over Q. Remaining: Constructing the common effective nonvanishing encoding already supplies the missing PIT information; no general-width encoding constructed. |
| P-12 | Can a common effective number-field point actually be constructed beyond products and bounded sparsity? | Proved for rational width-three ROABPs in one unknown order | Explicit SV10 parameter encoding gives algebraic integers in degree (nD+1)^21, an integer curve hitting set, and exact coefficient-row-span recovery by ordinary field traces. Remaining: The fixed-width theorem uses independently checked rank preservation; no general polynomial-in-width or Frobenius-purity transfer is claimed. |
| P-13 | How does a proved centered-SV pair budget give a common arithmetic point and coefficient-span map? | General encoding lemma with proved restricted specializations | K pairs give degree (nD+1)^(2K+1), explicit integer curve and exact ordinary-trace coefficient span. I30 gives K6/exponent13 for all width3; I29 gives exponent4r(w-r)+2w-1 for the two-rank promise. Remaining: The assumed generator and common-scaling closure are explicit. The two-rank promise gives degree (nD+1)^O(w²); arbitrary rank spectra use the I31 budget K=2^O(w log w). Neither yields degree polynomial jointly in growing width, length and degree. |
| P-14 | Can dense evaluation preserve coefficient rows through unbounded rank-one resets? | Proved restricted sampler and exact span preservation | For width w with every original factor rank in {1,w}, common-center plus SV_(w-1) hits every nonzero scalar contraction and preserves coefficient-row span; balanced RFE_(w-1)^(w-1) also hits. Every width-two ROABP is covered by one pair. Remaining: Arbitrary intermediate factor ranks are outside this proof; sample size is (nD+1)^{O(w)}, not polynomial in growing width. |
| P-15 | Can one centered interpolation pair be guaranteed for all width-three ROABPs? | Refuted for explicit node choices | A rational harmonic quadratic of exact width3 with every interval invertible vanishes on standard centeredSV1 at fourth-root nodes and on balancedRFE1^1 at rational harmonic nodes, including subset0,3,2,6 of the standard integer grid. Remaining: The fixed arithmetic-node ordinary center is a separate convention. Two pairs for all width3 with rank2 resets and the general growing-width RFE gate remain open here. |
| G-Q01 | Does the second-operation identity hold equivariantly? | REFUTED by G-01; correct special-lambda formula uses psi2. |  |
| G-Q02 | Can the universal product formula omit its terminal exterior variable? | REFUTED by G-02; lambda^i is required. |  |
| G-Q03 | Can finite gamma/Chern data determine all representation multiplicities? | REFUTED by G-03; parity sums of line characters. |  |
| G-Q04 | Can orbit coefficient maps and specialization gates be stated integrally? | PROVED G-04; nonzero maximal minors specify the good localization. |  |
| G-Q05 | Can at-most-three-row multiplicity obstructions separate a padded form from the determinant? | REFUTED in the characteristic-zero same-ambient setting by G-05. |  |
| G-Q06 | Is the first four-row determinant-ideal sector nonempty? | PROVED G-06 for n>=4; no target nonvanishing inferred here. |  |
| G-Q07 | Can the four-row determinant4 coordinate multiplicities be calculated exactly? | PROVED G-07; shifted plethysm subtraction with D320112. |  |
| G-Q08 | Can universal low-variable determinantal constructions bound obstruction length? | PROVED G-08 and sharper G-09; exact finite bounds and O_k(m^((k−1)/2)) for k>=3. |  |
| G-Q09 | Can the original handwriting or missing Masullo theorem number be certified from these files? | UNRESOLVED SOURCE GATE: original scan images and the numbered Masullo1.2 statement are not supplied; no such certification is claimed. |  |
| G-Q10 | Can the dimension-forced four-row gaps be given an explicit degree threshold? | PROVED G-10: all d>=r_n(n^(r_n−1)−1)+1 in the certified unpadded and padded ranges. |  |
| G-Q11 | Can the forced gap specify a rectangular outer highest weight and a degree progression? | PROVED G-11: explicit E_n,K_n and lambda=(nE_n k/4)^4 for every k>=K_n; unpadded n>=4 and stated genuinely padded dimension range with n<4m/3. |  |
| G-Q12 | Can these four-row rectangular gaps extend to n>=4m/3? | REFUTED G-12: no rectangular gap at or above that threshold for any padded degree-m form; strict inequality makes all positive-degree rectangular multiplicities zero. |  |
| G-Q13 | Can the first rectangular-gap degree be bounded without the factorial Veronese? | PROVED G-13: some d<=beta[(u+1)((n beta^2)^u−1)+1], with log bound O(n²logn), in all stated stable dimension-gap ranges; exact successful degree not specified. |  |
| G-Q14 | Can the standard first-row padding boundary be strengthened in the four-row sector? | PROVED G-14: the determinant first-jet projection is dominant; no positive padded-form multiplicity gap can have lambda1<=d(n-m)+1. Every gap needs lambda1>=d(n-m)+2. |  |
| G-Q15 | Can the padding exclusion be extended through the second or third jet? | PROVED G-15: explicit sl2 pencil has surjective third-jet differential in every size; lambda1<=d(n-m)+3 excludes a positive four-row gap. A rectangular gap requires d(4m-3n)>=16. No general strong Lefschetz assumption remains. |  |
| G-Q16 | Can the full fourth-jet map of quaternary determinant images also be dominant? | REFUTED for every m>=4 by G-15: its target dimension exceeds 2m²+2; order3 is maximal for full-jet dominance. |  |
| G-Q17 | Can one specify exact nonrectangular highest weights throughout the dimension-certified padded range, including n>=4m/3? | PROVED G-16: lambda=(d(n-m)+md/4,(md/4)^3), 4 divides md, has a positive gap at a bounded first degree and on an explicit progression whenever dim(P_m4)+3>2n²+2. No 4m/3 upper padding restriction remains for this label family. |  |
| G-Q18 | For a dimension-certified padded pair, which rational four-row partition directions contain a positive stretched multiplicity gap? | PROVED G-17: for nu partition ns, some positive stretch j has a gap iff nu4>0 and nu1>(n-m)s. Explicit first-stretch bound and every-term progression in the affirmative case; every stretch excluded on the two complementary faces. |  |
| G-Q19 | Can the successful stretch progression be upgraded to every sufficiently large integer stretch, including rectangles? | PROVED G-18: every strict four-row direction has both multiplicities positive for every j>=beta²; when c_m+3>2n²+2 the permanent multiplicity is larger for every j>=E(4u(pE)^(u-1)+1). Generic padding-line variation removes the finite projective stabilizer, including eta=0. |  |
| G-Q20 | What determines eventual comparison in a fixed four-row direction, and can occurrence obstructions persist along that direction? | PROVED G-18: ratio=kappa_nu*j^(c_m-2n²+1)(1+O(1/j)), kappa_nu>0; effective eventual determinant dominance if 2n²>4m²-2m+3, in particular n>=sqrt(2)m. Every fixed four-row direction has no occurrence obstruction at all sufficiently large stretches. Equality of quotient dimensions and individual finite-degree gaps remain separate comparisons. |  |

### Next attacks selected

The permanent-image route will test the degree-m Tor defect beyond size16 using restriction geometry and explicit Jacobian constructions, without assuming that a generic linear section preserves the known linear strand. The isolation route will test weaker scalar-boundary preservation at intermediate-rank resets, with synchronized seed dependence included in the statement. Purity and rational-evaluation ideas will be tested against this same remaining gate. These are active research targets, not claimed theorems.

## Checkpoint04 — 2026-11-21T03:49:47.492168+00:00

Actual elapsed work: 180.02 minutes. Full current deliverables and documentation packaged; no earlier checkpoint included. Persistence result is recorded beside the checkpoint after upload.
