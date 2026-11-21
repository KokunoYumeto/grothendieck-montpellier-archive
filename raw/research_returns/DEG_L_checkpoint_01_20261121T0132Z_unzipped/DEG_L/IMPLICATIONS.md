# DEG_L — implications and limits

This file is a live research deliverable. The session remains in progress; open questions below have not been promoted to theorems. All findings use run ID `DEG_L_20261121`; their check events are collected in `CHECK_EVENTS.tsv`.

## The degree and L-value question

T6.1 identifies the effective surface degree with a positive sum of norms of all pulled-back polarization-coordinate wedges. T6.2 separates it from the pure four-factor codimension-two output, whose degree for the product polarization is zero. T6.3 refutes a raw degree determined by source level alone, because the construction permits multiplication of its denominator-clearing maps at the same level. The meaningful normalized Chow cycle is unchanged under auxiliary covers and these map multiplications once its divisor kernels are chosen as biextensions (T6.4–T6.5).

T6.7 removes a proposed analytic obstruction: algebraic norm and trace clear the nonzero extracted period without requiring a lower bound for its individual complex absolute value. T6.8 bounds the effective degrees created by fixed divisor kernels. These statements retain the coefficient field, integral generator lattice and kernel constants explicitly.

T6.9 uses the supplied human proof and the checked theta spanning literature to cover every pulled-back holomorphic coordinate. The Hodge-index estimate B5 therefore reduces the effective surface degree to a finite character-theta Gram form. The global character factor occurs at 3/2 and has uniform elementary Euler-product bounds for fixed field degree (B1). Uniformity of integral maps, local factors and normalization is a separate issue. The exact wedge-norm computation through a rank-two source is being pursued; no character-only factorization has been assumed.

## Route 2 and the Hodge conjecture

B6 constructs the Weil projector using only a fixed generic imaginary quadratic action, with an explicit resultant denominator. B7 bounds the projected component of an effective cycle by its degree in a positive, flat Weil metric. B8 turns any nonzero effective Weil witness into a representative of every fixed Weil class, with both denominator and signed effective degree bounded quadratically in the witness degree. DIV1 supplies the proper parameter-space argument; DIV2 carries a uniform witness bound on a dense set to every fibre.

This is a strict reduction of the denominator and projector problem. It is not a proof of uniformly bounded witnesses in the open Weil families. No new general Hodge-conjecture case is asserted from the presently established estimates. The supplied Markman theorem yields a posteriori bounded complexity for abelian fourfold families by DIV5. That existence argument gives no numerical constant or explicit theta representative.

## Semiregularity and deformation

The 032 paper supplies a morphism with two-dimensional image, not a smooth embedded surface. S-01 shows that its permitted covers do not even preserve injectivity of that morphism. S-02 is the exact conormal-cohomology test for an actual smooth embedding. S-03 and S-11 refute general shortcuts from a nonzero period or from an ample complete intersection to semiregularity.

For the rigid ball-quotient source, S-04 forces the generated quotient to remain constant in any embedded semiregular deformation of its entire class. S-05–S-06 refute universal semiregularity of all deeper-level morphism presentations even for the full generalized map: the obstruction space grows beyond its fixed Hodge target. S-07 removes that cover growth by equivariant descent but returns to the base-level obstruction.

S-09 produces a perfect-complex K-class whose surviving Chern character is the desired projected class plus a chosen polarization polynomial. It removes extraneous Hodge conditions at the K-class level. It does not construct a semiregular object. S-10 explains why an equivalence alone does not remove an existing full trace kernel. S-12 shows that preserving a pure Weil character without polarization data can force a contradiction with Voisin's nonprojective torus family for coherent sheaves. The remaining geometric problem is a specific object with an injective obstruction trace and compatible full Hodge data. DIV3 states precisely how a successful embedded construction would imply bounded division.

## GRH hypotheses

The task's Alpöge Dirichlet GRH theorem is admitted, with the supplied Lean declarations as its exact formal statement. Consequently the cited conditional Dirichlet edge estimates may be used without a further GRH assumption in this run. The full Lean dependency archive was not supplied or compiled.

General Hecke edge estimates are conditional on the Masullo claim identified by the prompt as §1.2. The supplied index does not contain the complete claim or proof and does not identify a numbered Hecke-GRH theorem. Its numbered trace formulas have not been substituted for such a statement. No Hecke GRH hypothesis is needed for the absolutely convergent 3/2 factor. A nonabelian rank-two standard L-function is outside the stated Dirichlet/Hecke scope unless a factorization is established.

## Tate and standard conjectures

The supplied 032 and Milne consequences remain the background theorems requested by the task: CM Hodge, Tate for abelian varieties over finite fields in the cited formulation, and the Hodge standard conjecture for abelian varieties. The new degree estimates do not enlarge their scope. The correspondences in B6 exist algebraically and define projectors in homological realizations and numerical motives; their cohomological calculation alone does not claim idempotence in the Chow ring. A positive cohomological norm does not by itself construct an effective cycle or control an integral saturation index.

## Grothendieck locators and the previous runs

- **FGA, Bourbaki exposé 221, Lemme 2.4 p.255 and Théorème 3.2 p.260:** bounded reduced subvarieties and projective fixed-Hilbert-polynomial parameter spaces give DIV1–DIV3 their precise algebraic-geometric mechanism.
- **SGA 7 I, Exposé VII, (2.4.2), Example 2.9.5 and Remark 2.9.6:** biextension additivity gives the exact cancellation T6.5. Original scan verification is being completed.
- **SGA 7 I, Exposé VI:** the deformation framework belongs to obstruction theory, with the precise semiregularity maps supplied by Bloch and Buchweitz–Flenner, not by a positivity assertion in the archive.
- **Cote 16, the Coates letter, PDF page 45 / archive footer 44, and PDF page 46 / footer 45:** the displayed equivalence involving algebraic Lefschetz inverse and cycle-rank symmetry is consistent with retaining the algebraic projector as a separate datum. The current results do not infer missing cycles from positivity alone.
- **Cote 44, PDF page 2 / archive footer 1, Th.4; PDF page 4 / footer 3, Th.5:** polarization and the intersection/height form remain distinct from the unnormalized degree of the 032 surface. No new claim about the arithmetic height formula is made in this run.

The sketch uses PDF-page numbering, including the cover, for several of these scan references. We record both PDF and archive-footer numbers; this is a locator convention, not a mathematical transcription correction.

The rows directly treated are `HODGE_BRIDGE_SKETCH_20261121` T6, T7, Route 2 §2.1, and the generic-projector/witness part of §2.4. T8 is affected only by the reduction DIV2; its higher-dimensional cases remain open here. Other runs named SA06, SA07, H7, H8 and H9 were not supplied beyond quotations in the sketch; no unseen row is declared proved or changed.
