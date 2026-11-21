# Expanded TRACE_DET consistency audit

Snapshot: 2026-11-21 02:03:18 UTC. Reader: GPT-6 Astra Pro, effort setting not exposed, run TRACE_DET_20261121, child `/root/delivery_audit`.

This is a read-only release-consistency audit. It compares the user prompt, current source fragments, assembled source, question/implication/ledger registers, transcription notes and check-event coverage. It is not a new independent reading of every mathematical proof. No master deliverable was edited. The current PDF was not treated as final.

## Initial synchronization observations (resolved in follow-up)

1. **Check-event merge remains pending at this snapshot.** `deliverables/CHECK_EVENTS.tsv` has 381 data rows and no DET-18 or DET-19 events. Their saved local streams contain proof and whole-text checks; root's complete independent DET-18/19 reads are in `work/root_late_events.tsv`, lines 17 and 20. Include `weighted_endpoint_determinant_events.tsv`, `bessel_boost_obstruction_events.tsv`, `bessel_boost_independent_events.tsv`, `main_gate_challenge_events.tsv`, the late root rows, and the independent endpoint review when merging. This is a register synchronization issue, not evidence that those mathematical checks were omitted. Also retain the late DET-16 parity clarification and timeline-source event.

2. **Retain the precise hypothesis in the newest ledger summary.** `deliverables/LEDGER.md:133` drops “under RH” before “every bounded intertwiner from the arithmetic pure-point model is zero.” The full DET-19 statement at `work/paper_bessel_boost.tex:57–59` and `QUESTIONS.tsv:77` retain it. Add the qualification in the ledger; the unconditional non-C0 statement about the arithmetic scalar remains unconditional. The global stipulated theorem makes the conditional conclusion available, but its proof scope should stay explicit.

3. **Carry DET-18 into the remaining-gate narrative.** `work/paper_end.tex:11,20` / assembled `TRACE_DET.tex:3985,3994` still omit the just-completed weighted-character determinant and its exact Mellin/resolvent corrections. `IMPLICATIONS.md` currently ends at line 194 with DET-19 and has no DET-18 paragraph. Add the DET-18 closure with its integer multiplier, central half-multiplicity, ordinary scaled trace and GRH iff 0<=C<=4I distinction. Continue to leave the historical W / finite-determinant specialization and direct sign transfer open. The new determinant is constructed from the zero divisor; it does not establish that historical correspondence. The question register already contains DET-18's three rows, lines 78–80, and the framework table contains DET-18.

The earlier stale ledger tasks at lines 116–120 are now superseded by the dated update at lines 125–137. They are historical records and should not be erased. No remaining general Masullo S1 or small-time heat gate was found: QUESTIONS lines 59–61, IMPLICATIONS section 10, and paper U-MAS correctly say that MAS-10 closes it conditional on the full spectral-quotient claim.

## Coverage and source checks

- The assembled source contains DET-12, 13, 14, 15(a–d), 16, 17, 18, 19 and MAS-10, 11, 12. Their section starts are respectively lines 304, 541, 682, 916/1318, 2319, 1490, 1765, 2676, 3050, 3444 and 3602 in this snapshot. No new ID from this audit scope is absent from the question register.
- All completed DET-12–17 and MAS-10–12 have whole-proof reading coverage in the currently merged register. DET-18/19 have local whole-proof coverage awaiting merge. This audit verifies the existence and scope of those records; it does not relabel them as this reader's independent re-proofs.
- Read-only syntax crosschecks find no missing bibliography key, duplicate LaTeX label or unresolved ref/eqref in either the assembled source or the complete current source-fragment set.
- QUESTIONS has 79 distinct IDs and four columns throughout; TRANSCRIPTION_NOTES has 16 data rows and seven columns throughout; CHECK_EVENTS has six columns throughout. No malformed row or duplicate question ID was found.
- All 78 distinct Lean path references resolve to the mirrored source or the separately supplied entry files. The repeated basenames `TensorWeightedBesselGap.lean` and `Window.lean` are disambiguated by adjacent-directory wording. No source locator repair is needed for those references.
- Scope is consistent across the substantive registers: DET-14's dimension obstruction is specific to its finite target; DET-15 provides the fixed infinite Bessel model; DET-16 reconstructs integer multiplicities under RH, with cyclic atom weights distinguished from ordinary multiplicities; DET-17 rules out its exponent-2 prime weighting only; DET-19 rules out the indicated natural boost covariance only. MAS-10/11 determinant bridges and MAS-09/12 metric obstructions retain the stated Masullo spectral-claim dependence. The general Hecke statement is not mislabeled as an Alpöge Dirichlet-GRH consequence.

## Remaining mathematical and source gates

1. Exact chronology-to-declaration and specialization for Remark step 1, step 4 and all of step 7, including W's normalization, domain and linear/quadratic convention. Existing actual determinant and period identities do not uniquely establish that historical identity.
2. A source-supported direct sign certificate for the arithmetic kernel/operator, or a stronger exact finite-matrix/compression correspondence. The precise scalar certificate already stated in U-LIMIT would be sufficient through STEP6-03; a full operator equivalence is stronger and must not silently replace that smaller possible gate.
3. The actual weighted endpoint's divisor integrality if the explicit integer multiplier is to be omitted. DET-18 proves the exact criterion; it neither computes every actual coincident-zero multiplicity nor exhibits an actual fractional residue. This is a distinct refinement of an already constructed denominator-cleared determinant, not an open S1 construction gate.
4. Original manuscript images for attribution of the proved transcription repairs. The mathematics has been checked; paleographic attribution has not.

The truth of the complete Masullo draft and Deninger's specified arithmetic cohomology are not proved by this run; the former is a retained conditional source, and the latter remains an additional programme structure. Neither is a hidden gap in the displayed analytic determinant proofs.

## Recommended active/final status wording

As of this snapshot, work remains active through the current proof integration, event merge and final source/PDF verification. The fixed source-model existence gate, scalar arithmetic reconstruction under RH, and conditional actual quotient determinant gates are closed. Exact historical matching and direct finite-sign transfer remain open, with scoped obstructions and the next sufficient scalar certificate recorded. No universal nonexistence of an unnamed correspondence is asserted.

No scheduled three-hour movement review has occurred. The first is due 02:51 UTC on 21 November, and subsequent reviews are hourly if reached. The two-consecutive-no-movement stop criterion has not been triggered. Checkpoint03 is due 02:06 UTC; it must use a new ZIP name and include the current work, without nesting earlier checkpoints. Packaging is not mathematical movement.

Do not mark the work INCOMPLETE merely because packaging finishes. If the session itself ends before the unresolved identifications are settled, the final return may then be marked INCOMPLETE and must record the gates above, attempted routes and their exact failures, and the next source/specialization step. Do not invent a movement review or claim that all items have been proved/refuted.

## Snapshot identifiers

| File | Lines | SHA256 |
|---|---:|---|
| `deliverables/TRACE_DET.tex` | 4035 | `e059ae1ec4061ebce92588dc8245b964ccb32581cf1ba02da9b3d623e71e2e60` |
| `deliverables/QUESTIONS.tsv` | 80 | `df8a66a1e83737d4080ebedac2bf74924ccd308d5f4579beb254093404610e89` |
| `deliverables/IMPLICATIONS.md` | 205 | `c54c5adee7756cb1a6df2ed28e0f93eb1fcd4c375b3854e1cfe0275302c92172` |
| `deliverables/LEDGER.md` | 137 | `aef49fbd5e617ba045eb421057195b01d4d67eb928c3210ebea905d6e8740980` |
| `deliverables/CHECK_EVENTS.tsv` | 419 | `d7b257d9311820f2b07a6bab765cd34bdea79c3f2944c08d20c5970b4f5fbc6f` |
| `deliverables/TRANSCRIPTION_NOTES.tsv` | 17 | `231e0fe5288ad3f9c3c6c38f40c3c28082563d623880ca58ec2be4b5b15b7625` |

## Follow-up verification — 2026-11-21 02:04:11 UTC

All three concrete synchronization observations above are resolved in the live files:

- `CHECK_EVENTS.tsv` now has **418 data rows from 44 source streams**. DET-18 has 19 matching rows, including root's complete independent reading at row 360 and the independent endpoint review at rows 411–419. DET-19 has 14 matching rows, including root's complete independent reading at row 357 and the independent boost reading at row 38. No new finding in this audit scope lacks whole-proof check coverage. The four initial events of this audit were created after that merge, so this audit's own five-event stream remains to be included at the next merge.
- `LEDGER.md:125` now uses the actual 02:01 UTC update time; line 133 explicitly retains “under RH” for the pure-point intertwiner clause. The latest completed-gates entry supersedes the older dated progress entries.
- `IMPLICATIONS.md:197–205` now contains DET-18's determinant, integrality, central multiplicity and positivity consequences. `work/paper_end.tex:20` and assembled `TRACE_DET.tex:3994` state that the weighted scalar representation is closed while historical finite/window correspondence remains open.
- The refreshed assembled source has **4,035 lines**. A fresh read-only syntax check again finds no missing bibliography keys, duplicate labels or unresolved LaTeX references. QUESTIONS remains 79 rows.

**Conclusion:** no concrete unresolved release-consistency error remains in the audited scope. This conclusion does not certify the still-pending final PDF visual verification, final archive contents, checkpoint persistence, or future status updates. The work remains active; the remaining source/mathematical gates and stop-status obligations above still apply. No master file was changed by this auditor.
