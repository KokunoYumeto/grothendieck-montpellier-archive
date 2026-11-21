# Exact native full-row evaluator

## Verdict and scope

The complete new `ring_full_evaluator.cpp` and
`ktower_complete_native_ring.py` were read, including the original
verifier's unchanged structural prefix and evaluation formulas.
The native code computes every identifying row over the exact
quadratic algebra, using all six norm-two and seven norm-four frames,
then computes both determinants with certified unit pivots. The
mathematical proof is `native_full_rows_section.tex`, proposition
**KT-NATIVE-FULL-ROWS**. This is an ordinary source and mathematical
audit plus actual computations; no Lean kernel build is claimed.

Parent `/root` independently reported a whole-code read of both new
files with a PASS verdict for arithmetic, alias handling, orbit caching,
linearity, concurrency and determinant invariants. Its requested
comparison with the legacy `verify_ring_schur.json` report has been
added to the wrapper. The wrapper also captures its own source hash
at the beginning of a run. No original script or completed report was
modified.

## Why the acceleration is exact

If `o(P)` is the full orbit-evaluation row and `C` is the sparse harmonic
basis matrix, every old frame evaluation is `o(FP) C`. The new evaluator
first forms `E^2 o(P) - E sum_F2 o(FP) - sum_F4 o(FP)` and then multiplies
by `C`. This uses distributivity over the same commutative ring and
changes no coefficient. Every distinct permutation of an orbit is still
included exactly once. Cached coordinate powers and exponent-pair
products merely reuse values. Each thread has separate temporary
objects and writes one original matrix row, so completion order does
not change the matrix. The first matrix is checked to be scalar; its
scalar modular elimination agrees with elimination inside the quadratic
algebra.

The structural prefix independently re-enumerates all neighbor frames,
the entire invariant orbit spaces and contraction, verifies all harmonic
columns and the identity minor, and checks every integer of `model.txt`.
The full harmonic-kernel conclusion uses the carried split-contraction
argument in K17-U3-RESIDUAL-RING. The new native program alone is not a
replacement for that structural prefix.

All inverses are justified by a scalar or quadratic-norm gcd equal to
one. Failure to find an individual unit pivot is inconclusive, even
when the matrix itself happens to be invertible. A nonunit final
determinant is detected exactly. Moduli need not be prime or squarefree.
The successful certificate requires every row and both determinants;
progress logs and producer objects do not establish it.

## Completed e26 control

At modulus `697446897311`, weight parameter `k=25`, harmonic dimension
`732`, source dimension `5197`, target dimension `4465`:

| Quantity | Exact residue; w-coordinate zero |
|---|---:|
| det A | 65303065346 |
| det S | 212516823907 |
| det D | 243170653113 |

All 732 rows completed; both determinant norm gcds and the comparison
parameter gcd are one. Original Python pointwise evaluations agree at
rows 0, 366, 731, 732 and 733. The last two are extra points, not an
operator-identity check. The native part took 71.1724 seconds on this
run; the whole wrapper including prefix and five Python comparisons
took 77.17712617500001 seconds. This timing is an observation, not a
performance guarantee.

The separate `native_full_e26_reconciliation.json` checks every reported
parameter, the full-row count, all three determinant residues, input
hashes and frame hash against the carried full original-Python
`verify_ring_schur.json` report. No new full Python execution was
performed. The already completed native control report is unchanged.

| Artifact | SHA-256 |
|---|---|
| New complete native e26 report | `def7f10685284e52a8d561d15ccf43995346220a682dc5d021d6d088f10ba29c` |
| Carried complete Python e26 report | `f393d4e2ee009ab67b55f500cfbea66f9deb6b847dc2973a680f92d22bcb57a8` |
| Explicit comparison report | `072fda5f567b801d59b8cd5558f38ef11d3548a4bf514d4ffbc332795f8f960d` |
| Native source | `e8170f9e53c107002a22c71c4a6f07fad6f767a92247e61bb663d047ea97c921` |
| Native executable | `9ff58fce3a3f82819bb8269c0e7faba23795e21e64232b910d857493b0128ea7` |
| Wrapper used by completed control | `11f57266c9ab28e65778b9138fa82e1076b9ba1eb62a442b0a084f515f0265b1` |
| Wrapper after legacy-comparison addition | `bab107a497fa9327b5b9956c6673305958d539d4875a844cf53afa5179e48c95` |

## Exact controls

`audit_full_ring_native.py` and its saved PASS report use Python integer
permutation determinants independently of elimination. All 24 random
matrices returned exact matching determinants and unit statuses. They
cover dimensions 1 through 4 and moduli 15, 35, 49, 77, 1000003 squared,
and 697446897311. An invertible matrix with no individual unit in its
first column correctly produces an inconclusive result. An explicit
one-by-one nonunit is detected. Four malformed determinant inputs and
four malformed or nonunit-denominator model inputs are rejected.

These tests do not replace full-row computations. Higher-weight status
must be read from completed per-case reports. Two e32 native cases were
launched with two threads each after the complete e26 control passed;
their status is not promoted by this document.
