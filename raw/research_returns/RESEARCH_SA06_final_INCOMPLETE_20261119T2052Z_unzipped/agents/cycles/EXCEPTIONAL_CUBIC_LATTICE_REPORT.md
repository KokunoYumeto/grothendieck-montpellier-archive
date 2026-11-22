# Integral cubic exceptional lattices: current auxiliary record

**Record saved:** 2026-11-19T15:20:28Z.  **Status:** proved auxiliary lemmas, with independent agent audits; no separate main result ID is claimed here.

## Exact mathematical result

The complete proof is `exceptional_cubic_lattice_draft.tex`.  The historical filename does not mean its EC.1–EC.11 proofs are unverified.  EC.1–EC.6 prove the integral (r=3,m=1) exceptional multiplication injection, retaining every torsion point of the curve Picard group.  EC.7–EC.11 give the exact kernel for every (m\geq0,s\geq1): if (T=\mathbb P^m\times\prod_{i=1}^sW_i), (b=h+\sum A_i), and (L=L_T\boxtimes K_C), then the kernel of multiplication by (L) on \(\mathrm{CH}^s(T\times C)\) is the kernel of the free lattice map (b:B_{s-1}\to B_s) tensored with the full divisible point group \(\operatorname{Pic}^0(C)(k)\).  In Smith bases it is the direct sum of \(\operatorname{Pic}^0(C)(k)[d_i]\).

The proof uses the explicit integral cubic blow-up ring with arbitrary products and an elementary positive-adjoint calculation over the free rational Chow lattice.  It does not assert integral hard Lefschetz or use a numerical realization to discard Picard torsion.  The first endpoint proof and the general Smith-kernel proof have both been independently re-proved by `/root/frobenius`; `/root/real_weil` separately re-proved the first endpoint and inspected the nine-case certificate.  Those receipts expressly distinguish their scopes.

## Exact programs and observed outcomes

- `code/check_cubic_exceptional_lattices.py` constructs the full integral multiplication matrices, performs unimodular unit pivots, and computes the residual Smith normal form.  Sparse matrices and residual matrices are retained in `output/cubic_exceptional_lattice_matrices.json`; the certificate is `output/cubic_exceptional_lattice_certificate.json`; full stdout is retained beside the program.
- The initial six-case execution is retained separately with suffix `_initial_145931`: started 14:59:31.812057 UTC, runtime 0.532179358000576 seconds, 22 checks.
- The expanded nine-case execution started 15:03:32.933566 UTC, runtime 0.7236748529976467 seconds, 31 checks.  The cases are exactly ((r,m)=(2,0),(2,1),(3,0),(3,1),(3,2),(4,0),(4,1),(4,2),(4,3)).  Nonunit invariant factors occur in ((3,0)) as (3); ((4,0)) as fifteen copies of (3), one (9), one (27); ((4,1)) as (3,9); and ((4,2)) as (3).  Other listed cases have unit factors only.
- `code/compile_exceptional_cubic_lattice.py` produced the current standalone PDF in four successful commands, started 15:07:10.372414 UTC and completed 15:07:13.508498 UTC, runtime 3.136094444002083 seconds.  The final diagnostics list is empty.  Earlier failed or overfull passes and their distinct logs remain retained; they are not represented as successful final runs.  No independent visual render is claimed by this record.

These finite computations certify only their finite integer matrices and coefficient identities.  The all-(m,s) theorem is proved in the text.  In particular, three-primary Smith torsion does not disappear merely because the ground field has characteristic different from three.

## Primary-source grounding

Fresh primary reads in this window were Jiang's published *On the Chow theory of projectivizations*, Section 1.2, Theorems 2.4 and 2.8(3), including the integral displayed maps, and the Stacks project Lemma 42.36.2, Tag 02TX, including its proof.  These justify the projective-bundle and product blow-up formulas in all characteristics.  The cubic blow-up input is Huybrechts, *The Geometry of Cubic Hypersurfaces*, Chapter 4, Proposition 2.4, p.178, already opened and checked in the preceding geometry audits.  Existing bibliography keys are `cyJiang2023`, `cyStacksProject`, and `D_HuybrechtsCubics`; no new unverified source is introduced.

## Relation to the pending broader construction

The exact Smith-kernel description was used in Frobenius's separately audited PB.1–PB.18 whole-boundary argument.  That argument now kills the complete exceptional image by a free integral primitive quotient and a unique relative Milnor class.  It is stronger than asserting the exceptional multiplication map is injective.  A combined local theorem still requires its own geometry, actual-family and nonzero-cup audit; this auxiliary record does not promote such a theorem by itself.
