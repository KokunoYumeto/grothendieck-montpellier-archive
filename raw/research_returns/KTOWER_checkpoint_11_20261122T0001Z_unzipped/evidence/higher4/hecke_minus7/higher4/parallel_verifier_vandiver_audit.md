# Independent review of the parallel row-evaluation wrapper

Date: 2026-11-21. Checker: `/root/vandiver_k`, GPT-6 Astra Pro.
Effort: not exposed. Run: K17.

Reviewed file: `verify_ring_schur_parallel.py`, SHA256
`30af40a8ad6f0f7745973afef14b710d9a4457a03892dab86619c2206fba90ff`.

**PASS for exact arithmetic equivalence.** I freshly read the entire file
and the full diff against `verify_ring_schur.py`. An actual AST comparison
confirmed that all 15 pre-existing arithmetic functions are unchanged. The
sole new function, `independent_row`, is the previous serial row body: it
evaluates the same point and all the same six and seven neighbor frames,
then forms the same Schur row with the same E and E-squared coefficients.

The model, basis, orbits and frame lists are fully checked before the fork
pool is created. Row evaluation reads those objects and mutates only local
variables. The parent assembles results by the original row index, rejects
duplicate or out-of-range indices, checks row lengths, and finally checks
the complete row count and absence of missing rows. Therefore unordered
completion changes only execution order, not the matrices. All previous
assertions remain. Both determinant computations and their comparisons with
the producer remain serial and unchanged.

The new output filename is separate, so this wrapper does not overwrite the
existing serial certificates. Its worker budget is explicit and bounded by
four; resource allocation is an execution decision separate from this
mathematical equivalence check. No parallel numerical replay was performed
as part of this audit, and no additional residue case is certified by it.
