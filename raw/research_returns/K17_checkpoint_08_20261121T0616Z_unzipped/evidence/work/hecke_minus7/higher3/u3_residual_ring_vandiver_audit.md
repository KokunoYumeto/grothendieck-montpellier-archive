# Independent whole-proof audit: unitary residual integer rings

Date: 2026-11-21 UTC. Reviewer: /root/vandiver_k.
Model: GPT-6 Astra Pro. Effort: not exposed. Run: K17.

## Final verdict

PASS for the complete generic lemma and all five numerical rows,
including e24. The final five-row proof was read again in full,
and the complete fifth independent replay is now observed PASS.
Its precise numerical check is recorded in the addendum below.

## First checkpoint: the four-row proof

PASS for the complete generic lemma and the four-row numerical
proposition, covering both e20 and both e22 residual integers.
The e24 calculation is omitted from the reviewed proposition
and is not certified by this event.

I read the entire u3_residual_ring_section.tex, all of
prepare_ring_model.py, both complete C++ producers, and the
complete final independent verify_ring_schur.py. The original
two-class U3 proof was also reread in full. The exact Loeffler
class-set and correspondence inputs were fully reviewed in my
preceding fixed-weight audit and are unchanged here.

## Generic proof

The complete class set and actual six/seven neighbor frames are
independent of the coefficient weight. The explicit contraction
right inverse uses only primes at most 2k+1. The checked gcd
with 336(2k+1)! makes this splitting and both averaging
idempotents valid at every prime dividing M.

The complete signed-permutation source/target orbit modules
are free with disjoint-support bases. The saved harmonic columns
are killed by the full contraction and have an identity minor
on distinct free coordinates. At every maximal ideal their
dimension equals the entire kernel dimension. The identity
projection splits their inclusion; Nakayama kills the finite
complement. This proves a full basis over the possibly nonreduced
quadratic integer quotient, with no field assumption.

For omega²-omega+2, the norm of a+b omega is a²+ab+2b².
Norm coprimality with M is precisely invertibility and treats
both coefficient places at every split prime simultaneously.
No irreducibility, primality, or squarefreeness hypothesis
has been introduced.

The exact block Hecke matrix has lower-left map into the full
second invariant module and upper-right inclusion. With E_e
a checked scalar unit, ordinary block elimination proves
equivalence to the first-space Schur operator. The scale factors
cancel by homogeneity exactly as stated. An invertible identifying
evaluation matrix identifies the full endomorphism; no basis
of the second invariant module is needed.

The full-space conjugation involution remains integral at all
primes under discussion and exchanges the two directions.
The theorem therefore gives a unit for either Satake direction.

## Complete code review

Both producer implementations use the correct quadratic
multiplication and conjugation. The optimized formula is
algebraically identical to the original one. In the 64-bit
version Q<2^63 prevents overflow of additions and unsigned
128-bit products cover all multiplication; the larger cases
use GMP. Scalar inverses use extended Euclid with unit checks.
Only norm-unit pivots are inverted. A final diagonal entry is
multiplied without inversion, and an earlier nonunit pivot
failure is inconclusive rather than a false field-rank result.

The independent Python verifier reconstructs all thirteen
integral frame classes from exhaustive norm bounds, all orbit
bases, the complete differentiated contraction, and the
identity-coordinate minor; it rejects repeated sparse indices.
It verifies the complete integer text input against the JSON.
Every polynomial evaluation for every frame at every identifying
point is recomputed. It then uses column elimination, independent
of the producer's row elimination, to obtain both determinants.
The producer result is read only after those independent
determinants have been computed.

The higher-weight verifier uses exactly d identifying points.
The two additional stored points are not claimed as checked;
the final proof correctly states that scope. Injectivity and
actual correspondence equivariance already suffice.

## Observed execution and exact data checks

All four independent replay reports exist and report PASS:

- e20, M9496386083: dimension 333, determinant 1026900898.
- e20, M552972895573825165951583191: dimension 333,
  determinant 514586621306233221634475202.
- e22, M80348736972167: dimension 444, determinant 38390168543202.
- e22, M2789260013036301774436972122687974510453: dimension 444,
  determinant 875682305527210214142517183562570591024.

Each has zero omega coefficient and norm gcd one.
The producer and independent full replay executions were performed
by tripod_integral; I do not claim another redundant full replay.
I independently executed a check of every report's input hashes,
frame hash, identifying-row count, displayed residue agreement,
all denominator gcds, E_e-unit conditions, and determinant gcds.
All passed. The companion manifest records the reviewed proof,
all complete code, and every current case input and report.

No final K-group vanishing is claimed by this finite model
audit alone. The separate general arithmetic coverage and
full classical determinant tests are still the required
arithmetic interface.

## Final fifth-case addendum

I read the entire final five-row TeX again, with SHA256
8ad5e4d8bf53e41b979bcc96075b85ad033f22459063738ddcee19cb5684dfee.
The only mathematical exposition additions define the full
algebraic modular-form space and spell out that a scalar unit
in the free quadratic algebra is already a unit in the base
ring, by comparing constant coefficients in its inverse equation.
Both are correct. The numerical fifth row uses the same proof
and complete coefficient-space construction.

The fifth independent standard-library replay completed PASS:
e24, M3369865772726176603506574274451733385689247, dimension 576.
It independently recomputes all 576 identifying evaluations
for all 13 frames and obtains:

- identifying determinant 2572436762101187088545429364476974169239383;
- Schur-evaluation determinant 2173925231642651684114904966829963259418807;
- Schur-operator determinant 445305974135918810894106170147365896254386.

Each has zero omega coefficient. The Schur-operator norm has
gcd one with M. I independently verified the current complete
report hashes, frame hash, exact dimension and row count,
all factors of 336·47!, the comparison-scalar unit, and the
displayed determinant residues. All passed. The author's
independent Python replay took 401.48 seconds; no additional
redundant full replay by this reviewer is claimed.

The companion manifest now includes the final five-row proof,
the corrected residual-ring docstring, all unchanged complete
programs, and every fifth-case input and report. The final
numerical model verdict is PASS for all five rows.

## Editorial final readback

The final completed-status comment and explicit naming of both C++
producer files were read back in the entire section. Its current hash is
e0c7fba63e5ff7b2f49cd0ccacee35103b98ce8789d193afe844af8cbea3c6b8.
The mathematical statement, proof, numerical inputs and five-case PASS
verdict are unchanged.
