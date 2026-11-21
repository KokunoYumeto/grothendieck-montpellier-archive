# Independent audit of the generic level-seven residual-ring model

**PASS.** `/root/tripod_integral`, GPT-6 Astra Pro, 21 November 2026.

I read the entire `gl2_residual_ring_section.tex` and every line of
`gl2_twist_residual_certificate.py`. I reconstructed the full space,
integral lattice, diamond action, Hecke formula, and determinant-unit
argument. I then checked the saved five-case report against its exact
source hash, all full matrix dimensions, all unit-triangular identifying
matrices, every reported unit pivot, and the five final integer gcds.
I did not rerun the full q-series construction; the actual root/vandiver
executions and archive audit are separate events.

## Entire coefficient space and lattice

The previously checked integral conic ring in the generators z1,z2,z3
has relation z1z2+z2z3+z3z1=0. The change
A=z3+z1, B=z1, C=z1+z2 is unimodular, with the stated inverse, and gives
AC=B² exactly. The monic leading term AC gives the complete standard
monomial basis A^(m-j)B^j (0<=j<=m), B^(m-j)C^j (1<=j<=m).
Since A,B,C have leading terms1,Q,Q², its successive leading orders
are0 through2m, all with coefficient1. Multiplication by the proved
cusp divisor D shifts these to1 through2m+1.

The six simple cusp zeros and absence of an interior zero imply
S_(2e+1)=D M_(2e-2), including e2. The triangular coefficient matrix
independently proves saturation of the full Fourier lattice, avoiding
any inference from rational spanning alone. Thus the dimensions77,85,93
for e20,22,24 are the entire spaces.

## Diamond action and actual Hecke operator

The source's cycle z1->z2->z3->z1 gives exactly
A->C, B->C-B, C->A+C-2B. The eta cusp form is fixed by diamond2,
because its quadratic character has value1 at2. Consequently the
full-space Fourier formula is

    coefficient_n(T2 F) = coefficient_(2n)(F)
                           + 2^(2e) coefficient_(n/2)(diamond2 F)

when n is even, with the second term absent when n is odd. This is
the usual character formula on each eigenspace and hence on their
direct sum. The formula preserves the integral Fourier lattice.
The unit-triangular identifying map therefore determines the actual
operator over every residue ring, not merely a fitted truncation.

The code's eta product loop is exact: it starts with Q and applies
three copies of each (1-Q^n) and (1-Q^(7n)), using descending indices.
It constructs every basis form and its actual diamond image, solves
by forward substitution without division, and verifies all additional
coefficients to the stated precisions170,186,202. The matrices are
stored with the correct column convention; ordinary matrix cubing
therefore gives the stated operator T2³.

## Arbitrary-modulus unit proof and observed records

The identity det(t³I-T2³)=product_(zeta³=1)det(tI-zeta T2) holds after
a coefficient extension. All eigenvalues are integral, so an integral
unit product makes every individual eigenvalue difference a unit at
every place over every prime divisor of the modulus. This does not
require a chosen cube root in the quotient ring, primality, or
squarefreeness.

The determinant implementation uses only pivots with gcd1 and verifies
their extended-Euclidean inverses. It reports a missing unit pivot as
an unresolved calculation, not a field-rank claim. The saved report has
all five required cases, with dimensions4e-3, square matrices of those
dimensions, unit lower-triangular identifying matrices, and a full list
of unit pivots. The final residues and directly recomputed gcds are:

| e | M | residue | gcd |
|---|---:|---:|---:|
|20|9496386083|4822435123|1|
|20|552972895573825165951583191|205886586892358540462732749|1|
|22|80348736972167|79920658975217|1|
|22|2789260013036301774436972122687974510453|729501190808707622310038510098001514556|1|
|24|3369865772726176603506574274451733385689247|1165633710051053709364161260919098058495500|1|

No mathematical correction was requested. This proves the stated full
finite GL2 model test; the separate U3, residual-integer coverage, and
actual source hypotheses remain distinct inputs to any K-group theorem.
