# HECKE_DIV research ledger

Run: `HECKE_DIV_20261121`. Start: 21 November 2026, approximately 00:49:30 UTC (01:49:30 Europe/Berlin).

The supplied prompt is the task specification. The archive was unpacked once into `source/`. All statements in the bridge sketch are being checked, not assumed.

## Review policy

The first elapsed-time review is due after approximately three hours; subsequent reviews are hourly. Two consecutive reviews without an open row changing status or a strictly smaller main gate end that work. Checkpoint ZIPs are due every 45 minutes of active work, starting approximately 01:34:30 UTC. No earlier checkpoint ZIP will be overwritten or included inside another checkpoint.

## Current rows

| ID | Question | Status | Current gate or finding |
|---|---|---|---|
| Q21 | Closedness and uniformity, sketch 2.1 | Proof under independent check | Fix a relatively ample line bundle, a finite-type irreducible base, positive integral clearing multipliers, and a global flat rational section. |
| Q22 | Hecke reduction, sketch 2.2 | Proof under independent check | Use the relevant tensor-preserving Shimura group; distinguish a chosen class from all Hodge classes. |
| Q23 | CM dichotomy, sketch 2.3 | Proof under independent check | Use André–Oort and sequences eventually outside every proper special subvariety. |
| Q24 | Lefschetz constructions, sketch 2.4 | Literal endomorphism-degree assertion refuted; corrected statement in preparation | Extra degree-one unipotent automorphisms exist at every point isogenous to a nontrivial elliptic power. Graph degree is the suitable invariant. |
| Q4 | Numerical bounds on the E^4 Hecke orbit | Qualitative existence established from cited Markman theorem; quantitative work open | Track sheaf characteristic classes, projector, and isogeny degrees separately. |
| Q8 | Uniform bounded division on the split E^8 Hecke orbit | Main question open in this run | Produce one uniformly bounded effective four-cycle with nonzero Weil projection on a dense subset; inspect newly located Severn Theorem A before using it. |
| QA | Equidistribution and GRH | Quantitative implication being checked | A fixed positive mass at bounded complexity would suffice. Equidistribution alone is not such an estimate. |
| QH | Colmez heights | Explicit conductor family being checked | Height grows within a fixed CM isogeny class; no cycle-complexity upper bound has been obtained. |
| QP | Positivity | Under check | Separate positivity on already existing algebraic classes from existence of representatives. |
| QG | Grothendieck archival locators and transcription | Evidence unavailable | Archive scans and previous run files are absent from the supplied ZIP; bridge-sketch pointers are not verified transcriptions. |

## Source conventions

Alpöge's RH/Dirichlet-GRH conclusions and the supplied CM-Hodge results are used in the convention requested by the prompt. Inspection of entrypoint Lean files is not kernel verification of the imported development. Masullo's Hecke-GRH claim is a conditional premise; only a statement index is supplied. A newly located manuscript is not silently promoted to an established input.

## Events

- Initial read: the sketch's putative proper moduli interpretation of Markman is not the active proof in the supplied TeX. The active globalization uses semiregularity and countable closed algebraicity loci.
- Initial correction: isogeny degree does not control the complexity of an extra endomorphism; a nontrivial unipotent automorphism has degree one.
- New approach opened: Severn, Hexagon 2610.00387v2, Theorem A claims algebraicity for split eightfolds for Q(sqrt(-3)). The proof and its exact computations are being audited.

## Research update at 01:34 UTC (supersedes the initial table)

No three-hour review is due yet; this is an ordinary research update. The first formal review remains due at03:49:30UTC. Checkpoint01 is due now, after45minutes; the next is due at02:19:30UTC.

| ID | Current state | Strongest current finding or remaining gate |
|---|---|---|
| Q21–Q23 | Proved with precise hypotheses; independently checked | R20–R23 fix integral effective cycles, the polarization, global flat section, tensor-preserving Hecke subgroup and strict special-genericity. |
| Q24 | Literal statements partly refuted; replacements proved | R24A–D distinguish effective divisor degree and graph degree from signed intersection and endomorphism isogeny degree. |
| Q4 qualitative | Proved | Markman Cor1.6.1 plus R21. |
| Q4 numerical | Substantial new progress; final transfer being completed | Output regularity112 and normalized-family regularity independently checked. GRR gives R=2065542 and source cycle degree3426088289770714707027306735206400. Fixed isogeny and E6→E4 contraction still being integrated and checked. |
| Q8 qualitative | Proved using checked cited manuscript | Severn TheoremA plus R21. Supplier chain, dominance and all finite monodromy data independently checked. |
| Q8 numerical | Explicit formula drafted; independent audit ongoing | SQ2–SQ9 bound supplier length, Schoen cycles, invariant-divisor contraction and integral Hermitian lattice comparison. Formula uses only G=39191040, factorials and fixed target data. It is not yet labelled independently checked. |
| Qseed | Proved and independently checked | P2b integral Weil basis cycles have degrees80/80 onE4 and147456/175104 onE8, with multiplier1. Raw Hecke transport grows as m4/m8. |
| Qprime | Proved in precise arithmetic form | P6/R26: uniform integral effective degree at infinitely many good primes lifts the fixed class, even with varying multipliers. |
| QA | Exact implication proved | A1 positive bounded-complexity mass or first moment suffices; equidistribution alone provides neither. |
| QH | Uniform-height shortcut refuted | A2 fixed-field conductor heights grow explicitly. |
| QP | Formal positivity shortcut refuted | A3 positive pairing does not control effective decomposition or integral saturation. |
| QG | Original cote16 checked | Two separate Coates letters; PDF44–47 and48–50, archive folios one lower. No CSG transcription error established. |

Actual movement since start: corrected the reduction; found smaller integral product seeds; closed the qualitative E8 question with an audited primary manuscript; removed the separate denominator gate; reduced Markman's degree problem from unspecified sheaf boundedness to explicit regularity and Chern intersections; drafted a fully numerical E8 supplier bound; proved the prime-lifting equivalence with varying multipliers.

The LaTeX draft has not yet incorporated all new quantitative proofs. Complete latest proofs, proposed formulas and independent checks are in `work/`. Final integration, full proof reading, event consolidation, compilation and visual QA remain to be done.
