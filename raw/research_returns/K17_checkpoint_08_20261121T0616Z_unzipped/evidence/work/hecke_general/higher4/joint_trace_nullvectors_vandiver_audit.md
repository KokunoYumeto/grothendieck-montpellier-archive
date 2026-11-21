# Independent audit of the two-operator obstruction

Date: 2026-11-21. Checker: `/root/vandiver_k`, GPT-6 Astra Pro.
Effort: not exposed. Run: K17.

**PASS for the six explicit common-vector assertions.** This is a finite
matrix obstruction only. It does not assert a globally Eisenstein Galois
trace, a nonzero Selmer group, or a nonzero K-group.

I read the entire `joint_trace_nullvectors.py` and reconstructed its
unit-pivot elimination over `Z/M`. It never treats a nonzero nonunit as
invertible: a column with nonzero entries but no available unit returns an
explicit inconclusive status. In successful cases, the displayed vector is
checked against both original shifted matrices, with a coordinate exactly
one.

I then independently loaded the saved vectors and original rational matrices
and performed direct matrix-vector multiplication for every row at both 7
and 13. This calculation did not call the root's elimination routine. I
checked every rational denominator is a unit modulo the relevant integer,
every data-file hash agrees, and the selected coordinate is one. The report
is `joint_trace_nullvectors_vandiver_check.json`.

The six checked witnesses are the U3 branch at both residual moduli for each
of e=26 and e=28, and the GL2 branch at the larger modulus for each degree.
The remaining two smaller-modulus GL2 cases are reported by the root's
program as full column rank. Their complete algorithm was read, but this
direct-vector check does not claim an independent replay of those two rank
calculations.

## Exact algebraic consequence

Let A and B be the two shifted square matrices over R=Z/M, and let v have a
unit coordinate with Av=Bv=0. In the polynomial ring R[x,y],
`(xA+yB)v=0`. Multiplying by the adjugate gives
`det(xA+yB)v=0`. The unit coordinate therefore gives
`det(xA+yB)=0` as a polynomial over R. In particular every linear combination
of these two operators has zero determinant modulo the entire M. No
primality or squarefreeness hypothesis is needed. The same coordinate stays
nonzero modulo each prime dividing M.

The two U3 matrices are in the same basis: the complete verifier constructs
H and the swap signs outside the prime loop, and its rational change of
basis depends only on those signs. The GL2 matrices likewise use the same
full fixed modular-form basis at both primes. Their exact scaling and targets
are retained from the previously checked model files.

This result explains why further coefficient trials using only these two
operators cannot remove the indicated residual support. Additional primes,
additional operators, or a different source datum are separate questions.
