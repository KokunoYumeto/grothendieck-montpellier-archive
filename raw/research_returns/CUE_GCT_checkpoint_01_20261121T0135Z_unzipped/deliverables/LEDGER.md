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

Checkpoint ZIPs are due after each 45 minutes of active elapsed work. No checkpoint has yet been created. First substantive movement review is due at approximately three hours, followed by hourly reviews; two consecutive reviews without movement trigger stopping. Reviews will record actual elapsed times.

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
