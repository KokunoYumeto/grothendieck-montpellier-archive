# GHOSTS dated research ledger

Run GHOSTS-20261121. Started 21 November 2026, approximately 01:50 CET (00:50 UTC).
Status: IN PROGRESS. No final theorem claims at initialization.

## Authorized scope

Prove sketch 2.5; check 032 Remark 8.5 and CM transport; carry out T9; compute and uniformly bound local Weil-class complexity in T5, then carry this to Route 2. The sketch is an unchecked map. Cited 2026 results are treated as inputs with their exact scope; the Masullo input remains conditional where the sketch marks it so.

## Initial task map at 00:50 UTC

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

### 21 November 2026, 02:35–03:15 CET: explicit uniformity and primitive minimum

- R12's full support, polarization-kernel, quotient and principal-component argument passed independent review. Q6a moved from candidate to proved: detecting degree D0=132269760, followed by the displayed integral Gram-matrix division.
- R20–R24 removed the fixed principal-polarization restriction. The genus-four cyclic-cover Prym supplies a sixfold detector of degree D6=57854793024000. A terminating rational Hermitian-lattice construction, finite isogeny, sixfold projector, and explicit contraction charge every multiplier and degree cost. Q6b is proved for every fixed T5 lattice and flat rational vector, including rational actions after a charged preliminary isogeny.
- V01–V04 established the primitive class t0=t_star/2, exact complex and p>3 minimum16, and a fixed-variety, fixed-polarization, fixed-norm sequence with unbounded rational denominators. The norm alone therefore cannot determine or bound complexity.
- V05 classified every nonzero-Weil surface of degree at most14 as a translated abelian graph, in every characteristic. V06 then excluded all dominant/nondominant/product pairs and their possible low-degree corrections in characteristics2 and3. Root and prime_arithmetic read the whole proof; the primitive minimum is16 at every geometric good reduction. A proposed degree14 characteristic3 representative failed its full exterior-cohomology check and was explicitly rejected.
- R30–R31 were independently checked. With a computed exceptional integer b, Dirichlet GRH finds a prime outside it by max(exp14,4log b+4) in either nonzero class mod3. An unconditional finite certificate is a set of bounded-degree local representatives whose distinct rational primes have product greater than b. These statements keep the missing geometric input explicit.
- R40–R41 are under final proof writing: an explicit finite-field cycle and complete bounded parameter scheme permit an exact intersection-vector search using the cited Tate theorem. The algorithm does not pretend that an unspecified abstract flat class is already a computable local cycle.
- The auxiliary rational class w=e_W[Gamma1] still has complex minimum in[16,24]. Its exact minimum is the next local-complexity target; the earlier catalog of unit graphs was not an exhaustive proof for arbitrary cycles.
- The archive audit corrected a bibliographic grouping: cote16 scans48–50 belong to a separate letter dated6.1.1966, whereas scans44–47 are the Coates letter4.1.1967. This is a source-locator correction, not a mathematically forced correction of a supplied Grothendieck transcription.
- The three-hour progress review is not yet due. No no-movement review has been recorded.

## Current main gates at 02:19 UTC

| Question | Current state | Strongest gate or completed result |
|---|---|---|
| Sketch2.5 | Proved in precise integral form | B01–B06; one good prime outside b_D already suffices |
| Remark8.5 | Checked deduction | C01–C02; auxiliary dimension and realization compatibility explicit |
| T9 | Quantitative formula and concrete example proved | C03–C07,C18; canonical raw growth refuted by C06; arbitrary chosen constructions require their normalization |
| T5 exact normalized classes | Proved | t_star and primitive t0 have minimum16 at all good geometric reductions |
| T5 fixed-family bound | Proved | R12,R20–R24 with all lattice, isogeny and contraction costs |
| GRH arithmetic gate | Proved | R30–R31 finite explicit prime range for known b_D |
| Exact function for specified arithmetic input | Proved with explicit inputs | R40–R41 finite Tate-intersection search and finite exceptional table |
| Auxiliary rational class w | Open | Exact minimum between16and24 overC; extend low-degree analysis beyond14 or find a smaller complete cycle identity |
| Effective generic-input construction | Open computational refinement | Need effectively exhaustive bounded Hilbert equations and exact Betti marking; no oracle assumed |

The two remaining rows are being attacked. No stopping review has yet fallen due.

Checkpoint02 captured at 2026-11-21T02:20:04.587523+00:00. All current authored deliverables and work documentation are included; no earlier checkpoint ZIP is nested.

## Strict gate reductions after checkpoint02

- 02:39 UTC: R42 constructs the complete bounded cycle parameter scheme from actual equations, using Hoa regularity and integral Hilbert-scheme equations. R43 computes the generic exact minimum and an attaining cycle from an explicit marked Betti cocycle. R44 computes a generic-flatness integer by tracked monic Gröbner bases. R45 therefore closes the algorithmic-input gate: the entire good-prime function is a computable generic integer plus a finite exceptional table. Root read every proof; independent source and proof checks are recorded in CHECK_EVENTS.tsv. No numerical execution for an unspecified member is claimed.
- V07 determines the saturated integral Weil lattice by a two-row unimodular coefficient minor. This completes Q4g and makes the exact denominators in V04 unconditional in the stated integral Betti setting.
- The remaining auxiliary exact-minimum question Q4e is being reduced to a complete finite abelian-surface calculation. A graph-only catalog was rejected as insufficient: zero-Weil degree14 surfaces with primitive Plücker norms3 and4 must also be included. No conclusion from an incomplete catalog is accepted.

These are work entries, not the first timed progress review, which is due at03:50 UTC.

## Mathematical completion at 02:50 UTC

- Q4e moved from open to proved: W01–W04 give exact complex minimum24 for w. The complete geometric replacement includes nonabelian surfaces and the primitive-minor degree14 exceptions; exact finite enumeration rejects all remaining degrees16,18,20,22. Root independently reran the full catalog and comparison with identical counts.
- Q4f is complete with explicit arithmetic equations and a marked Betti cocycle: R40–R45 compute the generic minimum, a generic-flatness integer, and every exceptional good local value. V07 settles the integral Weil lattice; the source audit Q7 is complete at the stated scope.
- All treated QUESTIONS.tsv rows now have proved or refuted dispositions. The final paper and audit integration are being checked. No three-hour or hourly stagnation review has yet occurred; mathematical completion precedes the first review scheduled for03:50 UTC.

## Final package verification — 2026-11-21 02:56:37 UTC

The69-page paper and all requested audit files are complete. All21 treated question rows are resolved at their stated scopes. Every accepted proof has a complete-read event. The portable W04 certificate and the separate root rerun pass. The final PDF has no unresolved references/citations or overfull boxes, and all pages have been visually reviewed. Final archive CRC and per-file SHA-256 checks are performed by the packaging script. Completion precedes the next45-minute checkpoint and the first three-hour progress review; no unscheduled checkpoint or stagnation review is added.
