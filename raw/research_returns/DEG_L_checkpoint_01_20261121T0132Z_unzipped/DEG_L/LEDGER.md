# DEG_L dated research ledger

Run: `DEG_L_20261121`. Start: 21 November 2026, 01:47:14 Europe/Berlin (00:47:14 UTC).

## Rules for status

`OPEN` means the stated question remains undecided. `PROVED` or `REFUTED` requires a complete proof or counterexample and a recorded whole-proof check. A source statement accepted as background is not a new finding, and reading a source does not certify its proof. A corrected statement does not silently replace the original target.

## Main questions

| ID | Target | Status | Current gate |
|---|---|---|---|
| Q-T6 | Degree of the 032 cycle for a four-factor relation as an explicit Rallis L-value, with level dependence | OPEN | Exact geometric Gram formula T6.1; exact finite Hecke-L energy T6.10–T6.11; rank-two standard-L degree formula T6.12–T6.13 drafted and under independent check; integral/local normalization and level uniformity remain |
| Q-BOUNDS | Quantitative bounds on degrees and variation on Hecke orbits | OPEN | Fixed generic Weil projector and quadratic extraction proved B6–B8; finite Hom-lattice covolume criterion B10; retain generic degree as B11 shows essential cancellation; uniform normalized witness energy remains |
| Q-T7 | Bloch semiregularity of the 032 surface in the product of CM factors | OPEN | Universal level-map assertion refuted S-05–S-06; fixed smooth image requires conormal surjectivity S-02; weak target-equivariant semiregular replacement is being checked via Perry Th1.2 |
| Q-DIV | Carry the preceding results to bounded division on Route 2 | OPEN | DIV1–DIV2 reduce to bounded effective nonzero Weil witnesses on dense fibres; DIV3 proves exact embedded semiregular implication; known fourfold families have an a posteriori bound DIV5 |

## 2026-11-21 00:53 UTC — source audit

- Extracted all 12 archive entries once; recorded hashes.
- 032 Theorem 1.1 and Proposition 3.1 are used as supplied background, not re-proved.
- Main paper, Introduction §§1.2–1.3, distinguishes the surface period from the final codimension-two class.
- Initial independent readings agree: §7 selects a term from finite expansions, and Proposition 3.1 applies divisor kernels and scalar division. No exact formula for effective degree has yet been obtained from those steps.
- Scheduled checkpoints and three-hour review are tracked in `provenance/SESSION.md`.

## Open approach queue

1. Expand polarized surface degree into the Gram form on wedge products and compare it to rank-one and rank-two Rallis identities.
2. Calculate exact scaling under finite covers, multiplication isogenies, and Hecke correspondences; separate raw degree from normalized rational class and integral saturation.
3. Identify the semiregularity map for a specified image, normalization, graph, or derived pushforward; test what follows from the source construction.
4. Prove a precise geometric sufficient criterion for bounded division and test it in the cases covered by Markman.
5. Verify exact FGA/SGA/EGA and manuscript locators; report absence of evidence rather than invent a transcription correction.

## 2026-11-21 01:30 UTC — main-gate progress before checkpoint 01

- T6.1–T6.8 distinguish all cycle objects, prove exact auxiliary-cover/biextension cancellations, and clear the algebraic period by norm and trace without a lower L-value bound.
- T6.9 removes the existence gate for theta expansions of all polarization coordinates. T6.10–T6.11 give an explicit finite Hecke-L(3/2) energy identity with coframe and Haar normalization. The exact rank-two degree identity T6.12–T6.13 is written and awaiting root whole-proof review.
- B6–B8 remove the point-dependent CM projector and integral extraction gates. B10 supplies a short-map criterion from the integral Hom covolume. B11 shows why the generic degree must remain in that criterion. B12 records a variational equivalence, not an effective new witness construction.
- S-01–S-12 identify the genuine deformation object, refute universal deeper-level semiregularity, and remove several ineffective repairs. The later weak-equivariant theorem of Perry is being applied with its exact target-group hypotheses.
- DIV1–DIV5 received independent whole-proof checks; DIV1 was improved using the perfect universal Hilbert sheaf and its global Chern character. The main open geometric requirement is uniformly bounded nonzero Weil witnesses or a verified weakly target-equivariant replacement object.
- No scheduled three-hour review has yet occurred. The first checkpoint is due at 01:32:14 UTC.
