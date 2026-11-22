# Complete proof review of the uniform lift bound K-009

Date: 2026-11-22. Reviewer: `/root/plethysm_proof`, GPT-6 Astra Pro;
effort not exposed; run GCT_POS.

**PASS.** Read all of `branches/root/lift_bound.tex`. The reviewer
independently reconstructed a weaker Cauchy–Binet/Hadamard determinant
bound before being directed to this existing stronger proof. No new
order-bound finding is claimed by the reviewer. The Rayleigh improvement
and arbitrary-rank lattice passage were reconstructed from the full text.

For an independent subset of support columns, enlarging the lattice by
dependent support columns quotients its finite torsion, so cannot increase
its order. Enlarging by rationally independent new tensor columns has zero
intersection with the old torsion, which therefore injects into the new
torsion. This verifies the reduction to full rank3n−2, including sparse
and lower-rank supports.

The two block-sum differences span the full left kernel. Their primitive
exterior product has minor0 for two rows in one block and minor±1 for
two rows in different blocks. Complementary maximal minors therefore all
have common nonzero absolute value d; the Smith-form gcd identifies d
with the torsion order. There are exactly3n² nonzero minors, giving
det(B^tB)=3n²d².

The Gram trace is3r. Its Rayleigh quotient on the all-one column vector
is sum(row degree²)/r≥3r/n. For largest eigenvalue Lambda, AM–GM bounds
the other product by ((3r−Lambda)/(r−1))^(r−1). The scalar function
u((3r−u)/(r−1))^(r−1) decreases for u≥3. Substitution at3r/n gives
3(r/n)^r, since r−1=3(n−1). Hence d≤(3−2/n)^((3n−2)/2)/n exactly.

The margin-one relation puts the determinant character in the torsion
of the support character group. Splitting this finitely generated abelian
group supplies a finite diagonalizable factor and the asserted finite
lift, including its two-primary version. For a nonzero grading-fixed
quotient point, the unique closed special-linear orbit supplies a full
stabilizer lift; Jordan decomposition preserves its character, and torus
semistability supplies the margin relation after diagonalization. Thus
every grading stabilizer order has the stated bound.

The final no-pole implication is the already checked moving-generator
Koszul argument: if the fixed scheme is supported only at the vertex,
the supported homology modules have finite length, so the Hilbert series
is regular after multiplication by local units. No smoothness of the
quotient or of the fixed scheme is assumed.

Combining this checked theorem with PNEW013 yields the additional exact
integer range PNEW-M11–12 for the modular-lift exponent. That corollary
is elementary and is separately checked arithmetically through n=500;
the all-n validity comes from the two proved theorems, not extrapolation.
