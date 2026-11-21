# Whole characteristic-polynomial certificate: independent review

## Verdict

**KT-CYCLIC-CHARPOLY passes the whole-proof and whole-code review.**
The following were read in full:

- `exact_cyclic_charpoly_section.tex`;
- `hecke_general/higher4/cyclic_charpoly_certificate.py`;
- `hecke_general/higher4/replay_cyclic_charpoly.py`;
- the entire `replay_integral_faddeev.py` setup driver;
- the entire frozen `hecke_general/harmonic_hecke_certificate.py`.

No source was edited for this review, and no Lean kernel build is
claimed. The finite-model checks remain separate from the global
automorphic coverage and K-group arguments.

## Mathematical argument

For `B=D*A`, with D the exact positive common denominator, the scaled
candidate polynomial is `F(X)=D^n*f(X/D)`. Its descending coefficient
of index j is exactly `c_j*D^j`, as implemented. The code explicitly
checks that these scaled coefficients are integers and that the
candidate is monic of degree n.

The modular matrix consists of the full n columns
`v,Bv,...,B^(n-1)v`, in their correct order. Its determinant is computed
over a trial-division-verified prime field. A nonzero residue proves
that the corresponding integer determinant is nonzero, hence that
these columns are a basis over Q. Skipping primes that divide D is a
restriction on the search only and cannot produce a false positive.

Exact integer Horner evaluation starts from v and successively applies
`current=B*current+c_j*v`. Its final value is precisely `F(B)*v`.
Vanishing on this cyclic vector implies vanishing on the whole basis,
since F(B) commutes with B. Linear independence also rules out any
annihilator of degree less than n. The monic degree-n candidate
therefore equals both the minimal and characteristic polynomials of
B. Rescaling gives the characteristic polynomial of A. Repeated
factors cause no problem when the matrix is cyclic; a scalar matrix
of dimension greater than one is a legitimate inconclusive case.

The module uses exact integer matrix-vector multiplication and modular
determinants, without calling a characteristic-polynomial routine.
A failed witness search raises an explicit inconclusive error; a wrong
candidate fails the exact Horner assertion. The fact that the candidate
comes from the producer is harmless because the verifier proves it.

## Wrapper and retained checks

The wrapper executes only the setup part of the integral-Faddeev
driver, then requires a unique match for each substitution. The sparse
harmonic evaluator merely deletes zero terms and caches the same
columns by matrix identity. Progress additions do not remove any
assertion. The new polynomial function receives the original candidate
coefficients explicitly, collects its witness, and replaces the single
call in the frozen verifier.

Full orbit enumeration, complete contraction and kernel ranks,
evaluation determinant, every neighbor transform, operator equations,
conjugation-to-real-form equations, factor-product reconstruction,
comparison values, and the two extra-point identities are retained.
The active wrapper/module hashes are recorded in the separate shape
audit; neither file was changed during any replay.

## Current input shapes

The legacy verifier assumes some square-matrix cardinalities instead
of spelling them out in separate assertions. This review explicitly
checked those assumptions on all three current inputs and saved the
checks in `cyclic_shape_audit.py/json`. Harmonic dimensions are 155,
186 and 216 for e=32,34,36. Each input has exactly that many identifying
points, a square evaluation matrix, square transformed/operator
matrices at both primes 7 and 13, and the complete compatible harmonic
and contraction shapes. Input hashes are saved in the JSON. Therefore
this legacy omission does not affect these three concrete datasets.
Any optional hardening of a future wrapper should be a separate
version, preserving the provenance of the active computations.

## Executed checks and completion limits

The parent's saved `cyclic_charpoly_controls.json` was read in full.
It records successful scalar, split-diagonal, repeated-root Jordan,
and rational-denominator examples; rejection of an incorrect
polynomial; and an inconclusive noncyclic matrix. These controls were
executed by the parent, not independently rerun in this review.

The parent's `cyclic_charpoly_next_results.json` was also read in full.
It contains six completed standalone certificates, one at each of
7 and 13 in each of e=32,34,36. These certify the characteristic
polynomials of the supplied rational matrices. They alone do not
certify reconstruction of those matrices from the entire finite
Hecke model. The separately running full cyclic replays must complete
before that stronger finite-model conclusion is recorded.

At review time the module SHA-256 was
`d60f627730bbbe077da2511b2005a734b52fe265b757caecf7f56780e0a4bb58`,
the wrapper SHA-256 was
`a76f57fcf9a351d753b3edfb5b7b6f9cb0003b30a56a7b2e180f17fe985f0015`,
and the controls report SHA-256 was
`31f05cbc2467ab3dfe64cb3c62948dfad4214d6e1b412a6c477a01742f6ea1e4`.
