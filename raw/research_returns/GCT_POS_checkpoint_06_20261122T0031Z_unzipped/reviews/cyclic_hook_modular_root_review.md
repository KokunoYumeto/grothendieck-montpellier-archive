# Complete root review: cyclic trace, hook geometry and modular pole transfer

Reviewer: `/root`; model: GPT-6 Astra Pro; effort: not exposed; run: GCT_POS.
Date: 2026-11-21, completed 22:47 UTC. Type: targeted proof check by reading each complete proof and reconstructing the argument. The finite computation below is a separate check, not an all-dimension proof.

## Proofs read in full

- K-023, `branches/kronecker/CYCLIC_TRACE_HOOK_IDENTITY.tex`.
- R-NEW-004, `branches/root/hook_chain_lie.tex` (root-authored; independently read in full by both specialist reviewers).
- K-024, `branches/kronecker/HOOK_CHAIN_POLE.tex`.
- PNEW-013, `branches/plethysm/modular_pole_transfer.tex`, including both limitation examples and the geometric corollary.

All pass within their stated scopes. The inherited full support theorem ALPOGE_GCT P-F30 and local Hilbert formula P-F23 were previously read in their entirety in this run; their hypotheses were checked again at the points where K-024 uses them. These are dependencies with recorded proof checks, not unchecked statement-level imports.

## K-023

The Schur-Weyl multiplicity space is the diagonal symmetric-group invariant space in the third tensor power of the rectangular Specht module. Cyclic trace composed with the averaging projector is the average of the character at the cube of a permutation. Cubing a cycle either preserves its length or splits a cycle of length divisible by three into three cycles. The resulting exponential cycle index agrees exactly with the symmetric algebra on the direct sum of the defining module and its (2,1) Schur module. The respective weighted degrees are one and three. Extracting the rectangular Schur coefficient gives the required invariant dimension, with total weighted degree divided by n.

The coordinate/representation duality is justified by the contragredient group automorphism. It preserves cyclic factor permutation, so no unrecorded sign or determinant twist appears. The rational representation of the cyclic group of order three splits into trivial lines and two-dimensional rational summands. Dimension minus trace is therefore three times a nonnegative integer. The identity is a specialization of the known root-number/higher Lie-character identity; no priority claim for the general identity is justified.

## R-NEW-004 and K-024

The repeated-letter coefficient equation in the Lie calculation was reconstructed. It kills the diagonal and all but the first-column and first-superdiagonal entries, with one possible extra entry. The distinct-letter equations then kill these remaining entries; the coefficient determinant three is explicitly used only in characteristic zero. No reduction-of-invariants or modular smoothness claim is made.

For K-024 the positive rational masses solve each diagonal moment equation, and no off-diagonal root difference occurs between supported weights. The coefficient-one chain is diagonally equivalent to this critical representative, and the diagonal matrix normalizes SL_n, so closedness is preserved. The simple-spectrum cyclic element has centralizer of size M. Character-column orthogonality exhausts that size with the first M determinant powers. Every nonlinear constituent of the defining module must therefore have antipodally paired eigenvalues. There is just one possible two-plane, and the determinant kernel fixes a nonzero vector there. Its finite SL_2 action is trivial. This proves the full stabilizer, rather than only its diagonal subgroup.

The lift argument allows arbitrary two-power order before classification. Replacing a supported linear weight by three times that weight preserves its rational span and exact invariance under the two-primary lift. P-F30 therefore applies to the resulting cubic support, including its rank-deficient and higher-lift cases. Its equality case forces the chain. The hook representation has no cube weight, so the final cube must have arisen from the linear summand. All supported chain weight spaces are one-dimensional. Thus every nonzero fixed quotient point is on the same grading orbit.

Smoothness follows from the closed orbit with trivial SL_n stabilizer. The fixed tangent has dimension one. The degree semigroup of the orbit closure has group M Z and is cofinite after division by M, giving normalized density one. The moving Euler factor is the displayed adjoint-over-ambient product. Every nonzero dyadic factor 1 minus a root of unity is a unit after inverting two. Thus the normalized residue is a unit at every prime over three. Finally any grading subgroup of order M times a positive power of three would have to fix a nonzero point on the same orbit, contradicting its full grading stabilizer M. The fixed scheme is supported at the origin, and the finite-length Koszul argument excludes all these higher-order poles.

As a direct check of the fixed-space count, the exponents of the diagonal element have distinct two-adic valuations. A distinct-letter triple cannot sum to zero because its least valuation occurs once. A repeated-letter hook weight can sum to zero only at consecutive chain positions. The only fixed linear weight is the last one. This proves the full fixed space count independently of a generic-support argument.

## PNEW-013

The cyclotomic reduction identity was reconstructed from the quotient formula for Phi_(e p^r), for e prime to p. Its roots have exact order e after reduction. A rational series with integral coefficients and only root-of-unity poles admits an integral cyclotomic denominator normalized to constant term one; multiplication by the integral series then proves numerator integrality.

For the auxiliary series, the exclusion of every higher M p^r pole makes the remaining denominator a local unit at the reduction of a primitive M-th root. Separability also makes (1-t^M)/Phi_M a local unit there. The assumed unit normalized residue consequently forces the reduced numerator to be nonzero. This proves an actual pole of the reduced rational function, not merely a vanishing unreduced denominator. Equality of formal power series modulo p gives equality of rational functions because the denominators have constant term one. A reduced characteristic-zero cyclotomic factor of the tensor series must then have prime-to-p part exactly M. It is an actual pole, since that numerator and denominator are coprime over Q.

Both warning examples were checked algebraically. In particular a unit residue alone is insufficient: poles at orders M and pM can coalesce and cancel after reduction. The exact-order example has difference 3z/(1+z^3), preserves nonnegative integral coefficients after the added term, and shifts the relevant characteristic-zero pole from M to 3M. Therefore the theorem does not imply r=0.

## Exact computation replay

Read all of `branches/kronecker/verify_cyclic_trace_hook.py`, then executed it independently. PASS: nineteen symmetric-group character averages agree with a separately constructed weight dynamic programme and Weyl alternant for the auxiliary representation. The n=2 through 14 checks verify positive masses, the complete fixed-weight multiplicities, simple spectrum and the unique antipodal plane. Receipt: `branches/kronecker/cyclic_trace_hook_checks.json`.

These finite checks calibrate conventions only. The all-n conclusions follow from the proofs above.

## Consequence and remaining scope

For every n at least two, the tensor Hilbert series has an actual pole at an order 2^(n-1) times a power of three. Every denominator product of factors 1-t^a must consequently contain an exponent at least 2^(n-1). This refutes the existence clause of numerical PH3 with unified parameter rank(x)=n^2+5n and introductory h=n^4+O(n), and therefore also its canonical clause. The argument does not determine that power of three, prove a pole at the exact dyadic order in every dimension, or establish a strict positivity-index or saturation-index lower bound. Those remain main questions.
