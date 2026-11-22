# Effective perfect C1-field extension

Five full numbered proofs are in `sections/C_finish_C1_fields_draft.tex`, pending independent audit. Primary-source/search details are in `logs/C_C1_fields_search.json`; draft metadata remain under notes until promotion.

## Main new constructive step

For a finite k-algebra E, enumerate surjective maps to finite products of matrix algebras over explicitly presented finite extensions, and accept exactly nilpotent kernels. Every candidate has finite verification. Since perfect C1 fields have only commutative finite division algebras, a valid semisimple quotient certificate exists; the positive search therefore terminates. Primitive idempotents lift by a polynomial congruent0 modulo T^N and1 modulo(T-1)^N. This is an ordinary algorithm under the stated countable enumeration and factorization access, not a bare existence reduction to finding an idempotent.

## Canonical indices and forms

Module isomorphism over infinite k is decided by whether the determinant polynomial on a linear Hom space vanishes identically. The least isomorphic tuple code is found by finitely many checks up to the input code. The indecomposability predicate is decided by the finite-algebra certificate. Thus the canonical indices are a decidable complete set without an unknown representation orbit quotient; unlike the algebraically closed construction, the fixed-size index set need not be finitely parameterized by polynomial templates.

C1 norm surjectivity reduces the residual hermitian groups to ranks and determinant square classes. For actual tensor/exterior forms, representation decomposition and canonical intertwiners give the block entries q_i^{-1}B_uv; projection to the residue field produces the exact multiplicity form. Its determinant provides the symmetric square-class coordinate. This avoids a new isometry search. Square-class canonicalization is a finite least-code search using X^2-a/b factorization.

## Scope and concrete nonclosed family

The ordinary algorithm explicitly requires an infinite countable perfect C1 field, effective enumeration/arithmetic/equality, and factorization over the field and every explicit finite extension. It is not asserted for arbitrary computable field presentations. The fixed towers union_a F_(p^(ell^a)), with p odd and ell a fixed prime, supply all these procedures: factor degrees stabilize after removing their ell-parts. This is compatible with the independently audited halting obstruction for arbitrary towers whose future extension degrees depend on an undecidable event.

## Promotion — 2026-11-19T17:24:47Z

Root and dieudonne each read all five actual written proofs and passed. The section is now `sections/C_finish_C1_fields.tex`; final own result/check files are `results_C_C1_fields.csv` and `checks_C_C1_fields.tsv`. The independent peer events remain in `checks_C_C1_fields_dieudonne_audit.tsv`. Root owns compiled inclusion and its own audit events.
