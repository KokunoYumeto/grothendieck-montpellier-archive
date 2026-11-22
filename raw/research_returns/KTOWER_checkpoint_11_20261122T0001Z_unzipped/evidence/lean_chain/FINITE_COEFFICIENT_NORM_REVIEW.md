# Whole review of the finite-coefficient norm comparison

Reviewer: /root/lean_chain, GPT-6 Astra Pro; effort not exposed.

**PASS** for the entire 131-line proof in
unitary_audit/reducible_comparison/finite_coefficient_norm.tex,
SHA-256 0ff58707446a6198aa2058b31bd1bc34442d26c46bc791ed3473e7503712a3a3.
The theorem is KT-CUBIC-FINITE-COEFFICIENT-NORM.

## Checks

The defining coefficient characters have values in Fp. Continuous
cochains with finite k-coefficients therefore form a finite direct sum
of the Fp cochain complexes. Cohomology, the displayed local kernels,
and the relative quotient commute with scalar extension. Finiteness
of the degree-one groups for this fixed finite ramification set is
the standard carried finite-coefficient Galois input.

Choosing linear cocycle representatives and a defining cochain for
each basis pair gives a bilinear global choice of w. The ordinary
condition is preserved: the local primitive of v at p is unique
because the relevant H0 vanishes, and the correction in CM.8 is
bilinear. The previously checked uniqueness of w up to global
coboundary identifies this choice with the same intrinsic obstruction.

The proof also preserves the local primitives of the relative class,
which is essential. At p, local H2 vanishes and all local H1 is
allowed, so a linear choice of primitive has no effect on the class.
At q dividing D, the quadratic family factors through
G_Qq/I_E,q. This quotient is an extension of the procyclic unramified
group by an inertia group of order at most two. Since p is odd, its
p-cohomological dimension is at most one. The rational character ψ
is unramified there; its H1 on this quotient is precisely the
unramified H1 under inflation, since the remaining finite inertia has
no positive-degree p-cohomology.

Consequently primitives can be chosen linearly in the quotient
cochain complex, and their ambiguity is exactly the allowed local
space. The relative pair has bidegree (2,1), not only its raw global
two-cocycle. Expanding that homogeneous polynomial gives FC.2 with
the stated polarization and no missing factor of two.

Each basis vector and sum of two distinct basis vectors is a nonzero
Fp-valued cohomology class. Restriction to K=E(μp) preserves it
because the degree is prime to p, and the coefficient character then
becomes trivial. Its image is therefore cyclic of order p. The
matched norm theorem applies separately to these finitely many
inputs. No additive group of an arbitrary finite field is incorrectly
treated as cyclic.

The zero-space cases give the empty sum. The final paragraph
correctly retains the unevaluated-ideal, injectivity, and source-to-jet
limitations.

## Review scope

The complete new proof was read. The relevant CM.8–CM.15 local
construction, representative-independence argument, and previously
whole-reviewed CE comparison were checked against the new uses.
No new primary arithmetic theorem, numerical computation, or Lean
kernel build is asserted. This extends the exact comparison to
finite coefficient fields; it does not prove a nonzero value.
