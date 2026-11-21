# Isolated parallel replay: code-equivalence audit

Date: 21 November 2026. Author: `/root/tripod_integral`. Object: `verify_ring_schur_parallel.py`, SHA-256 `30af40a8ad6f0f7745973afef14b710d9a4457a03892dab86619c2206fba90ff`.

Status: **code equivalence checked; no parallel numerical execution claimed in this note.** Existing serial programs, active cases, and reports are unchanged.

The complete diff against the audited higher4 serial verifier is saved as `verify_ring_schur_parallel.diff`. The new `independent_row` function consists exactly of the original row body: it evaluates the same basis and all thirteen frames at the same identifying point and forms the same Schur evaluation row. The parent stores each returned row at its original index. It rejects out-of-range indices, duplicate rows, incorrect row dimensions, missing rows, and an incorrect final count. Consequently scheduling order cannot change either matrix.

All fifteen existing arithmetic functions have mechanically identical abstract syntax trees. The complete frame reconstruction, source and target orbit enumeration, contraction kernel, identity minor, text--JSON agreement, denominator conditions, and independent serial column-determinant routine are unchanged. The only added report fields identify the explicit worker count and the new verifier's hash. The separate output filename `verify_ring_schur_parallel.json` prevents replacement of a prior serial report.

The owner read the entire diff and each new block and checked syntax. `/root/vandiver_k` independently read the complete 335-line file and the entire diff, independently checked all fifteen AST identities and the exact new row body, and reported PASS. This certifies the preservation of the mathematical computation, not any unexecuted result.

The caller must supply the worker count. This environment exposes CPU affinity 0–8 but no cgroup mount, `cpu.max`, or `cpu.stat`; `/proc/self/cgroup` reports only `0::/`. The actual CPU quota cannot be inferred from affinity. No additional workers were launched before coordination of the active workload.
