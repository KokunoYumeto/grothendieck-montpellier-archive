# Intake of SIGN_NEXT, part 2: checkpoint 02, the final return (prompt 45)

By Claude Opus 5.5 at effort high (agent abcaba9b6ae84b747), 21 Nov 2026, round 5. Part 1 read checkpoint 01. Check
events: `INTAKE_SIGN_NEXT_20261121_part2_CHECK_EVENTS.tsv`.

## 0. What I read

**The return:** `research_returns\SIGN_NEXT_checkpoint_02_20261121T0430Z_unzipped\`, from 04:30 UTC. **By the user's rule
of 20 Nov the run has ended at this return**: its newest return is more than three hours old.

**What I read:**
- `LEDGER.md`, "Further observed movement after checkpoint 01" and the Checkpoint 02 entry;
- the `QUESTIONS.tsv` rows and states.

Everything new is at statement level; my context is near its limit. **The findings I checked in part 1 (SN-C01 to
SN-C05, SN-10 to SN-14, IF-01, IF-03, SN-44-01 to SN-44-05) are unchanged, and none is withdrawn.**

## 1. Verdicts on the new findings (statement level)

All of the new work is on Q6g, the integral theta/Lefschetz comparison.

| Finding | What it states |
|---|---|
| IF-10 | An explicit algebraic coefficient realization, with CM-character and 2-adic lattice normalization (Q6g-CM-GEOMETRY proved). It identifies no automorphic motive |
| SN-15 | All-rank index matrices and integral row/shift reduction, with exact invariant factors at n = 5, 6 by two algorithms. **It extends IF-03,** which I recomputed independently for n ≤ 4 (part 1). The order-index question is now a bounded explicit computation in every rank |
| IF-11 | An inhabited genuine m = 2 theta-jet construction, with correct derivative normalization and coefficient algebraicity (Q6g-ACTUAL-JETS) |
| IF-12 | Genuine CM theta kernels do not commute with the fixed root (Q6g-THETA-ROOT refuted) |
| SF-Q6-01, 02, 03 | numEx/numBig as a numerical host, the small-size witness, and the rank-window constructor: all refuted |
| SF-Q6-04 | The actual stabilizer denominator, and a positive full F − E expression under stated ties. Its realization was still under construction |
| SF-Q6-05 | The common-pin condition removed for a single family |
| SF-Q6-06 | The diamond Fourier test and a refined-level definite nonzero-period theorem; the fixed indefinite anchor still active |
| SF-Q6-07 | The constant-twist row completion: refuted |
| SF-Q6-08 | The fixed inert-prime estimate from the actual local data |
| IF-13 | Written, not reviewed, not inserted |

**At the end:**
- **Q6g-GLOBAL-GEOMETRY is still "active research".** The single global m = 2 instance, with a complete positive bound,
  was not realized.
- Q44 (the corrected Th. 5) is unchanged: proved.
- The main question (scan 050, C and I) is unchanged: proved in its corrected form, with the abelian case conditional on
  032.

## 2. What is new

- **The integral Lefschetz order indices are now computable in every rank** (SN-15). With IF-03 (n ≤ 4, my independent
  recomputation), this is the full answer to the "integral form of cote 16 no 7" question (our scan 014, §7, "(sur Z !)")
  of the Hodge sketch's Route 4. The n = 5, 6 values are at statement level.
- **Q6g, the identification of Alpöge's lift chain with the Lefschetz sl₂:** many precise refutations of shortcut
  realizations. No positive global identification.

## 3. The two proofs, and H01

No RH or GRH, no Masullo. 032 is as in part 1 (SN-11). H01 is not changed.

## 4. Integration

- **Hodge sketch, Route 4:** add "SN-15: order indices in every rank by an explicit integral reduction (n = 5, 6
  computed); IF-03: n ≤ 4, independently recomputed."
- **HODGE_SIGN's U-04 and U-05:** U-04 is partly constructed (IF-10, IF-11). U-05 is refuted as a lift-count assertion.
  The global instance stays open.

## 5. Hexagon

- **H04 (cote 44 Th. 5):** unchanged, complete mathematically (SN-44 together with JAC1964). The gates: the scan-004 image
  check, and the write-up. **The run's end is now fixed, which settles the "stability" part of test 3 for SIGN_NEXT's
  side.**
- **H11:** unchanged; it still waits on 032.
- No new candidate.

## 6. What the successor needs (the run has ended)

1. **Q6g:** realize one actual global m = 2 datum with SF-Q6-04's ties (RealPack/DivInputs), and evaluate its Smith
   factors. Review IF-13 and insert it.
2. **SN-15:** tabulate the n = 5, 6 invariant factors in the paper with the certificate. They should be rerun
   independently.
3. **Scan 050:** carry the second-pass row (read C, not A) into `TRANSCRIPTION_NOTES.tsv`, as in part 1.
4. **Beyond abelian varieties:** test SN-C04's corrected criterion (R₀ + G_{L,0} on X×X) on a variety with known B but
   unknown I.
