# Perfect-field descent audit and arithmetic boundary

The three statements in the actual root draft passed independent written audit. Exact source openings and event rows are in `logs/C_perfect_descent_groups_audit.json` and `checks_C_perfect_descent_audit.tsv`.

## A short independent Noether–Deuring proof for this application

An isomorphism after algebraic closure is defined over a finite extension L/k. Forgetting L-scalars identifies the two modules repeated [L:k] times. Krull–Schmidt power cancellation gives the original isomorphism. The same argument reflects direct-summand inclusion, since multiplicities are multiplied by the same finite degree. This handles finite base fields as well as infinite ones. The draft's determinant-grid argument also proves the stronger arbitrary-extension version over infinite fields.

## Coefficient degree

The split orthogonal Hopf algebra and filtration have prime-field coefficients. Galois conjugation preserves the vanishing or nonvanishing of the top-degree coaction coefficients, and a constant change of basis preserves the filtration. Faithful field extension reflects containment in each filtration step. Hence every absolute index in a Galois orbit and its associated k-indecomposable have exactly the same minimal coefficient degree. Restriction of scalars is regular-matrix encoding and constant idempotent summands do not increase degree.

## Constructive part of form transfer

Given an actual indecomposable over k, symmetric and alternating invariant forms are explicit linear spaces. A nonzero determinant polynomial supplies a nonsingular form over infinite k by a finite grid (or finite enumeration over a finite field). Its adjoint involution is computed by matrix inversion and transpose. Nilpotent radical reduction is constructive: a self-adjoint unit congruent to1 has a finite inverse-square-root polynomial, using only division by2; this corrects an isometry lifted from the quotient. Self-adjoint idempotents likewise lift by a polynomial separating0 and1. QSS therefore reduces actual orthogonal coefficients to explicit hermitian matrices over the finite residue division algebra with involution.

That reduction does not itself classify or decide congruence of the resulting hermitian matrices over every perfect field. Already the trivial-action map GW(k)→WG_sp(BO_m/k) splits the forgetful map, so ordinary field-form arithmetic is a genuine part of the desired ring. Effective primitive-idempotent and Schur-index extraction from a general finite central-simple algebra is also retained explicitly. No impossibility theorem is inferred merely from this observation.

## Primary-source boundary

Benson–Reichstein Lemma3.3 descends a module to its stabilizer field only under condition(1.1): every algebraic extension has zero Brauer group. It must not be used over arbitrary perfect fields. The draft correctly avoids it by descending a multiple through restriction of scalars and recording the Schur index.
