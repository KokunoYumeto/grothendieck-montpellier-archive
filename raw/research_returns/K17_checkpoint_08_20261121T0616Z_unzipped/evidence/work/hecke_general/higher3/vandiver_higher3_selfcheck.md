# Higher3 complete-model and integral-ring check

Date: 2026-11-21 UTC. Reviewer: /root/vandiver_k.
Model: GPT-6 Astra Pro. Effort: not exposed. Run: K17.

## Scope and verdict

PASS for the full finite models and their exact integer comparisons.
This check does not claim the final arithmetic conclusion by itself:
the generic source/coverage lemma and the separate level-seven unitary
tests are additional inputs.

The complete proof in higher_harmonic_section.tex was read back in full.
The whole unchanged harmonic_hecke_certificate.py was freshly read,
including complete orbit enumeration, differentiation, exact ranks,
Hermitian neighbor identities, every transformed evaluation, the rational
form change, characteristic polynomials, factor multiplication, and two
additional point tests. Its actual full replay on the new e20/e22/e24
data completed with exit code zero and a PASS report. The report hash
was compared with the actual current full-data hash and agrees.

The full gl2_higher3_certificate.py wrapper was freshly read and rerun.
It uses the previously read and checked level-three integral arithmetic
module. Every identifying Fourier correction is retained, including
indices divisible by 7 or 13. The actual new run completed successfully.
The complete combined_higher3_certificate.py was freshly written,
read back, and executed successfully. It verifies exact Horner values
and gcds and the whole residual decomposition. Small factors alone
are asserted prime, using exact trial division. Large residual entries
are deliberately treated only as positive integers.

## Full level-seven GL2 basis

The complete proof in
../../hecke_minus7/higher3/gl2_residual_ring_section.tex and the complete
gl2_twist_residual_certificate.py were read back. The actual full five-case
run completed with all five determinant residues units.

The unimodular change A=z3+z1, B=z1, C=z1+z2 converts the complete
published integral conic to AC=B². Its standard monomials in degree m
have leading Fourier orders 0 through 2m with coefficient one; after
multiplication by eta³ eta7³ these become 1 through 2m+1. This proves
the full integral basis and an injective identifying coefficient map
over every integer residue ring.

The preceding eta-divisor proof was retained as a cited previously
checked lemma: D is nonzero in the upper half-plane and has a simple
zero at each of the six Gamma1(7) cusps. Hence D times the entire
weight-(2e-2) conic piece is the entire cusp space.

The published Meier–Ozornova Lemma 2.6 was freshly checked again:
[3] sends z1 to -z3, z2 to -z1, z3 to -z2. Squaring gives exactly
the [2] cycle used in the program. D has diamond value one at 2.
This verifies the full-space Hecke correction rather than inserting
a single nebentypus into the full Gamma1(7) matrix.

Every determinant pivot is a checked unit modulo its stated integer
M; an unavailable unit pivot would cause an unresolved result, not
an invalid inverse or a singularity assertion. All five actual runs
found unit pivots. Factoring t³I-T³ over a coefficient extension
containing the cube roots of unity proves the simultaneous twist-unit
conclusion. No primality, field, or splitting assumption on M occurs.

## Exact output

- e20, M9496386083: dimension 77, residue 4822435123, gcd 1.
- e20, M552972895573825165951583191: dimension 77,
  residue 205886586892358540462732749, gcd 1.
- e22, M80348736972167: dimension 85, residue 79920658975217, gcd 1.
- e22, M2789260013036301774436972122687974510453: dimension 85,
  residue 729501190808707622310038510098001514556, gcd 1.
- e24, M3369865772726176603506574274451733385689247: dimension 93,
  residue 1165633710051053709364161260919098058495500, gcd 1.

The companion manifest records the current exact paths and hashes.
The full matrices, identifying coefficient arrays, determinant pivots,
and exact characteristic polynomials remain in the certificate files.
