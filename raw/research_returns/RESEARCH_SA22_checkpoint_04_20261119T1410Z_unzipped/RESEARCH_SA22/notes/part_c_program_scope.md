# Program scope, finite counts, and recorded runtime

Recorded 2026-11-19T12:50:16+00:00 by GPT-6 Astra (OpenAI, ChatGPT Pro mode; inherited effort not separately exposed; part_c_algebra agent).

Each program listed below was actually run. Existing exhaustive checks and floating-point diagnostics were not rerun merely to increase a count. The three short scripts without saved runtimes were rerun once to measure the missing wall time. Internal times start after imports; wall times include interpreter startup, so the columns should not be used to compare algorithmic speed.

| Program (under `code/`) | Arithmetic and scope | Complete tested count | Seconds | What the computation does not prove |
|---|---|---|---:|---|
| part_c_finite_checks.py | Exact integers; exhaustive specified C4 and S3 systems | C4:8 chains,20 symmetry atoms,400 convolution atom pairs,64 alignments,16 torsion pairs; S3:30 profiles per factor,900 rearrangement pairs | 0.041654345 (internal) | A complete certificate for these finite examples and their counterexample values; not a classification of all finite groups. |
| part_c_extensions.py | Exact integers; two specified extensions of C2 | Each extension:4 chains,6 symmetric atoms,36 convolution pairs,16 alignments,8 kernel pairs;2 extension systems total | 0.000707238 (internal) | Certifies nonuniqueness via C4 and C2xC2; not a classification of all extensions. |
| part_a2b_checks.py | Float64 scipy loggamma/digamma; fixed seed22021119 | 1209 Hessians (1200 random+9 specified),30 finite-difference Jacobians,600 monotonicity pairs | 0.383141997 (internal) | Diagnostic evidence only, with no implication of general positivity/injectivity. The analytic proof is A2b-energy and A2b-image. |
| part_a1_cut_checks.py | Exact rational constants in one analytic welding | 2 assertions: derivative interval is strictly negative; endpoint derivatives differ | 0.049863184 (wall) | Certifies the finite arithmetic; collar holomorphicity and failure of a pointed-disc antiisomorphism are proved in the manuscript. |
| part_a1_bordered_checks.py | Exact Fraction arithmetic; one two-jet contradiction | 4 assertions: original jets,nonzero determinant,unique candidate coefficients,zero forced squared lengths | 0.037938974 (wall) | Certifies the 2x2 algebraic contradiction; does not numerically construct caps or establish the analytic range theorem. |
| part_c_b3_audit.py | Exact sparse polynomial arithmetic over Z,F7,F3 | 7 assertions:1 universal coefficient identity,2 discriminant+Cartier examples,1 Legendre coefficient,1 Legendre discriminant | 0.037317177 (wall) | Certifies arithmetic inputs only; cohomology, p-ranks and specialization are justified by the source theorems and proofs. |

## Diagnostic values

All 1209 normalized sampled Hessians were positive. Minimum sampled eigenvalue: 8.39697899191e-06. Maximum normalized symmetry residual: 1.81521464526e-14; maximum scaled finite-difference residual: 1.72401024196e-09. All 600 sampled monotonicity pairings were positive, with minimum 0.278718971118. No finite sample is used as a proof.

## Source-fetch and metadata utilities

`part_c_fetch_sources.py` made3 retrieval attempts: EGA_IV4 downloaded49,852,990 bytes in733.783871 s; HLP downloaded26,986,622 bytes in6.781591 s; Milne local fetch returned406 in4.799427 s (the primary web PDF was separately opened). `part_a2b_fetch_sources.py` made2 attempts: Ahlfors-Bers returned403 in11.651925 s (web PDF separately opened); Solynin downloaded4,227,450 bytes in31.946015 s. These are retrieval times, not mathematical tests; their original JSON outputs retain the SHA256 values and status.

`part_c_make_metadata.py`, `part_a2b_make_metadata.py`, and this final-audit program are record-generation utilities. They are not theorem verifiers and their generated ledger-row counts are not counted as independent mathematical checks.

The first C4 JSON-generation run reused the S3 variable `f` when serializing the C4 record. That output-only bug was fixed by retaining `c4_f`, and the mathematical certificate was rerun successfully. The attached current C4 JSON and the complete400-decomposition/64-alignment certificate are the corrected versions; no failed output is presented as a valid witness.
