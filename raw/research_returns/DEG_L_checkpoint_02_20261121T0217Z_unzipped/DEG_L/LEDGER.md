# DEG_L dated research ledger

Run: `DEG_L_20261121`. Start: 21 November 2026, 01:47:14 Europe/Berlin (00:47:14 UTC).

## Rules for status

`OPEN` means the stated question remains undecided. `PROVED` or `REFUTED` requires a complete proof or counterexample and a recorded whole-proof check. A source statement accepted as background is not a new finding, and reading a source does not certify its proof. A corrected statement does not silently replace the original target.

## Main questions

| ID | Target | Status | Current gate |
|---|---|---|---|
| Q-T6 | Degree and level dependence | REFINED FORMULA PROVED; literal level-only assertion REFUTED | T6.10–T6.14 give exact finite spectral identities and exact finite-cover scaling. The separate character-only factorization question remains open and is being tested by a Steinberg constituent construction. |
| Q-BOUNDS | Quantitative bounds on degrees and variation on Hecke orbits | OPEN | Fixed generic Weil projector and quadratic extraction proved B6–B8; finite Hom-lattice covolume criterion B10; retain generic degree as B11 shows essential cancellation; B14 gives sharp local support/seminorm bounds and refutes sufficiency of level plus unit L2 norm; uniform normalized witness energy remains |
| Q-T7 | Bloch semiregularity of the 032 surface in the product of CM factors | OPEN | Universal level-map assertion refuted S-05–S-06; fixed smooth image requires conormal surjectivity S-02; Perry Th1.2 reduces deformation to one gluable weakly target-equivariant semiregular object with full B-normalized character; DER1–DER3 reject numerical and syzygy shortcuts |
| Q-DIV | Carry the preceding results to bounded division on Route 2 | OPEN | DIV1–DIV2 reduce to bounded effective nonzero Weil witnesses on dense fibres; DIV3 proves exact embedded semiregular implication; known fourfold families have an a posteriori bound DIV5; DER4 turns a successful replacement into explicit fixed signed-cycle bounds without a virtual-rank assumption |

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

## 2026-11-21 02:07 UTC — stricter geometric and analytic reductions

- The complete T6.12–T6.13 proofs have now been read by root and an independent agent. The exact surface degree is a finite standard-L(1) expression; the character-L(3/2) energy formula remains the direct global-factor upper bound. T6.14 checks all finite-level scaling constants.
- B1a computes the actual infinity factor, (2pi)^(-[F:Q]), and B14 gives a sharp fixed-level local counterexample together with the missing positive support/seminorm estimates. Conductor, compact level and Schwartz localization are distinct data.
- S-14 closes the implication from one weakly equivariant gluable perfect object to bounded division. S-15 and DER2–DER3 show why canonical cover, Fourier–Mukai-equivalence and syzygy repairs do not eliminate an established full trace kernel.
- DER4 supplies a constructive refinement: the finite Kummer gerbe in the deformation theorem permits an integral Adams operation of homogeneous weight equal to its band order. This descends even in virtual rank zero and preserves M^n times the Weil component. A finite bundle presentation and an effective Chern degeneracy cycle give fixed N and D, carried to all fibres by DIV1. The successful object itself remains the main deformation gate.
- Original SGA7 biextension pages and SGA6 Adams-operation pages have been visually verified and retained as source witnesses. The live LaTeX manuscript now compiles; layout cleanup continues.
- The next checkpoint is due at 02:17:14 UTC. No scheduled three-hour review has yet occurred.
