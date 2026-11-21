# Native harmonic producer audit

## Result and exact scope

PASS as an exact discovery producer and as an implementation equivalent to
the carried model on the fresh k=13 control. This audit does not replace the
separate complete standard-library certificate replay for any new higher
weight, and it does not promote an unfinished arithmetic case.

Files read in their entirety:

- `higher4/hecke_general/higher4/compute_higher_native.py` (126 lines),
  SHA256 `d08abca84ca74ac4003ce2deac5e40586af2f5a7b4c4553a2f1e578f13455e51`;
- its direct basis dependency `compute_higher_incremental.py` (160 lines),
  SHA256 `3f01946d37190a4ee6d66c6cb243270f9cc034651b2c5276ee561243e7f402bf`;
- predecessor `compute_higher_flint.py` (138 lines),
  SHA256 `534f24ae5542134b2f8ea12d0695d0be6b281e6acc74931053b95517b3b03275`;
- original `higher4/hecke_general/compute_harmonic_hecke.py` (243 lines),
  SHA256 `803e8fc403dd0ea87696a7d3c803968d0379693f959962f1f3f3fb2c81ab7709`.

The native and incremental drivers preserve the original mathematical
objects. Their numerical linear algebra uses exact FLINT rational/integer
types, not floating point.

## Harmonic kernel

The source and target enumerate exactly the original permutation orbits of
all bidegree monomials satisfying the mu6 diagonal invariance condition.
The contraction coefficient is the original sum of `a*b`, divided by the
target orbit size, with divisibility checked. The replacement also checks
that contraction commutes with the exchange of the two sets of variables.

The plus and minus span columns have the same order and normalization as
the original producer. Rational reduced row echelon form is unique. The
replacement constructs the standard free-column nullspace basis from its
pivots, then clears denominators, divides by the integer gcd and makes the
first nonzero entry positive, just as the original `primitive` operation
does. These steps give the same canonical rational harmonic basis.

The two parity-restricted ranks add to the full target dimension because
the contraction preserves parity. The code explicitly checks their sum,
the complete contraction identity, full column rank, expected nullity and
each column's exchange parity. No subfamily of harmonic columns is used.

## Point selection

Incremental row reduction is performed modulo the fixed screening prime
1000003. Each accepted row has a new pivot after reduction by the existing
normalized echelon rows. Rows are kept in pivot order; every new row has
zero in every previous pivot. This is ordinary exact Gaussian elimination
on the row span.

A nonzero determinant modulo that prime proves rational invertibility.
The code additionally computes and checks the actual integer determinant.
The screening prime can cause a rationally independent candidate point to
be skipped, so equality with the original rational point-selection sequence
is not asserted at every weight. This is harmless: once the final evaluation
map is invertible, the matrix on the same harmonic basis is independent of
the chosen identifying points. The k=13 control happens to select exactly
the original points. Failure to find enough points raises an error; it does
not supply an incomplete operator.

## Cached evaluations and matrices

`orbit_evaluations` precomputes, for every coordinate and every exponent
pair appearing in the original expanded orbits, the exact Eisenstein-ring
product `z_i^a w_i^b`. Multiplying these three cached factors and summing
over the same orbit gives the original `eval_orbits_eisenstein` value.
The ring operation and conjugation are unchanged:
omega squared plus omega plus 1 is zero.

`transformed` uses the same conjugated neighbor columns on the first
variables and the same un-conjugated columns on the second variables,
sums all neighbors, and multiplies by the full harmonic basis. The full
evaluation matrices B0 and B1 are retained. The rational solves satisfy
the checked identities `ev*M0=B0` and `ev*M1=B1`.

The exchange-conjugation identities are checked entrywise. Passing to the
rational real form uses the same delta-scaling, with delta squared equal
to −3, as the original producer: equal-parity entries stay a, plus-to-minus
entries become −3a, and minus-to-plus entries become a. The characteristic
polynomial is computed exactly; every coefficient is checked integral.
Two further identifying points are evaluated with all neighbors and checked
against both matrices. Exact polynomial factors are multiplied back to
the full polynomial. The comparison value is evaluated on that polynomial.

## Fresh completed control

`audit_native_producer.py` imported the current producer, redirected its
output to `lean_chain/native_producer_replay/`, and freshly ran k=13 at
both p=7 and p=13. It compared against the carried complete model

`input/RETURN_K17_checkpoint_08_20261121T0616Z/evidence/work/hecke_general/higher2/harmonic_k13_exact_exploration.json`.

Both 14-dimensional operators passed. The full orbit lists, contraction
matrix, harmonic basis, parities, identifying points, evaluation matrix
and determinant, all transformed evaluations, both coefficient matrices,
the rational real form, every characteristic-polynomial coefficient,
every exact factor with multiplicity, and the comparison values agree.
Polynomial display strings and runtime metadata are not mathematical data
and were not required to agree.

The carried input SHA256 is
`2d32e105d1a21c54941efd05e78dfd690f4f93f05033329732a104f87c5a7747`.
The fresh output SHA256 is
`bbceb443873f81ea00df78568e59f490d32f0b036a86ce22d5988991fd1ecab4`.
The complete reconciliation is `native_producer_audit.json`; the actual
run completed at 2026-11-21T17:02:23Z.

## Remaining verification boundary

The producer deliberately marks outputs exploratory. Progress files may
contain one completed prime before the second prime and final producer
metadata have been written. A file's existence is therefore not evidence
of a completed two-prime model. Even a completed producer output must pass
the separate full certificate replay before use in a new arithmetic
vanishing theorem. This boundary is retained for e=32,34,36.

