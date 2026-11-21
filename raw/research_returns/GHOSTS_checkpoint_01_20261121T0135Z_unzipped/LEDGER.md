# GHOSTS dated research ledger

Run GHOSTS-20261121. Started 21 November 2026, approximately 01:50 CET (00:50 UTC).
Status: IN PROGRESS. No final theorem claims at initialization.

## Authorized scope

Prove sketch 2.5; check 032 Remark 8.5 and CM transport; carry out T9; compute and uniformly bound local Weil-class complexity in T5, then carry this to Route 2. The sketch is an unchecked map. Cited 2026 results are treated as inputs with their exact scope; the Masullo input remains conditional where the sketch marks it so.

## Open rows

| ID | Question | State | Current strongest gate | Owner |
|---|---|---|---|---|
| Q1 | Arithmetic bounded complexity, sketch 2.5 | In progress | Construct bounded-degree cycle parameter locus with the prescribed realization | bounded_specialization |
| Q2 | 032 Remark 8.5 | In progress | Inspect cited transport Corollaries 3.4 and 6.4, absent from ZIP | cm_transport |
| Q3 | T9 degree and denominator | In progress | Specify transport choices and prove a quantitative pullback bound | cm_transport/root |
| Q4 | Least local complexity in T5 | In progress | Fix A, polarization and class normalization; investigate generic minimum and finite exceptional primes | root |
| Q5 | GRH distribution to uniform complexity | In progress | Separate prime counts from geometric degree control; derive strongest consequence | prime_arithmetic/root |
| Q6 | Route 2 family gate | In progress | Uniformity in the family parameter, beyond a fixed arithmetic fiber | root |
| Q7 | Exact Grothendieck locators | In progress | Obtain original cotes/scans, and FGA/SGA/EGA references | root/bounded_specialization |

## Evidence and attempts

### 21 November 2026, 01:50–02:00 CET

- Unpacked the supplied ZIP once, into sources/. No nested archives were present.
- Read the prompt and relevant sketch sections. Extracted text from the five supplied PDFs.
- Delegated independent proof tasks for bounded specialization, CM transport, and prime arithmetic.
- Initial possible strengthening: least local complexity may stabilize to the geometric characteristic-zero minimum outside finitely many primes. This remains under proof check.
- T5 is covered by existing fourfold theorems. A uniform bound for each fixed class follows from a global cycle, but this does not give the numeric minimum or an effective family bound.
- The supplied transport is a reference to a missing paper; source retrieval underway.
- Personal Context retrieval was attempted narrowly for prior normalization/transcriptions and returned disabled. No prior data are assumed.

## Timed requirements

Checkpoint ZIPs are due at elapsed 45-minute intervals only, beginning at about 02:35 CET. The first progress review is due at elapsed three hours, about 04:50 CET, then hourly. No checkpoint has yet fallen due. Checkpoints exclude earlier checkpoint ZIPs.

### 21 November 2026, 02:30–02:35 CET: first checkpoint preparation

- Q1 moved to proved in its integral-cycle formulation: B01–B02; B02a refutes the literal prescribed-N rational-cycle reading. B03 proves eventual exact constancy of the minimum; B04 gives a single-prime gate; B06 removes a separate denominator hypothesis when integral numerator degrees are bounded.
- Q2 moved to checked deduction from the cited inputs after retrieving the exact October transport PDF. C02 identifies the unsupported same-dimensional/same-family inference. C03–C05 give explicit pullback costs.
- Q4a moved to proved for a fully specified normalized class t_star on E^4: minimum16 at every good prime, independently checked. The proof handles arbitrary effective cycles, all positive multipliers, characteristic2, and inseparability. Characteristic3 after potential good reduction is being documented separately. t_star is integral but not primitive.
- The attempted unrestricted positive-characteristic period inequality was refuted by explicit quaternionic automorphism graphs. A low-degree classification replaced it and proved the exact minimum. This is a strict reduction of the main gate.
- Ordinary/supersingular residue classes are determined for the Eisenstein product isogeny class; an explicit C^4 example refutes extending that criterion to the whole Weil family. Prime-count estimates leave a geometric bound unproved.
- R10–R11 extract every rational Weil vector from one effective surface of bounded degree with explicit constants. R12 proposes D0=132269760 from Schoen; support, polarization, and moduli-component details remain under independent adversarial review.
- No three-hour progress review has yet fallen due. The first45-minute checkpoint is due02:35 CET/01:35 UTC.

Checkpoint01 captured at 2026-11-21T01:35:10.187535+00:00. It contains all current authored deliverables and proof/check documentation; original supplied attachments remain available separately.
