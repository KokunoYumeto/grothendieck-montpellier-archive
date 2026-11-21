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
