# DEG_L dated research ledger

Run: `DEG_L_20261121`. Start: 21 November 2026, 01:47:14 Europe/Berlin (00:47:14 UTC).

## Rules for status

`OPEN` means the stated question remains undecided. `PROVED` or `REFUTED` requires a complete proof or counterexample and a recorded whole-proof check. A source statement accepted as background is not a new finding, and reading a source does not certify its proof. A corrected statement does not silently replace the original target.

## Main questions

| ID | Target | Status | Current gate |
|---|---|---|---|
| Q-T6 | Degree and level dependence | REFINED FORMULA PROVED; literal level-only assertion REFUTED | T6.10–T6.14 give exact finite spectral identities and exact finite-cover scaling. T6.15 refutes universal character-only source-parameter reduction by an actual balanced theta wedge and associated CM surface map; a preselected indecomposable switch relation is outside this counterexample. |
| Q-BOUNDS | Quantitative bounds on degrees and variation on Hecke orbits | OPEN | B17 controls existing split theta representatives. B19 computes the actual CM Hom metric and its exact core-index dependence, giving degree O(sqrt J) and complexity O(J) in a fixed simple CM isogeny class; normalized analytic energy is bounded there. B20–B21 prove reduced images of every bounded-degree source witness family still grow as sqrt J. Uniform target-dependent effective witnesses remain. |
| Q-T7 | Bloch semiregularity of the 032 surface in the product of CM factors | OPEN | Universal level-map assertion refuted S-05–S-06; fixed smooth image requires conormal surjectivity S-02; Perry Th1.2 reduces deformation to one gluable weakly target-equivariant semiregular object with full B-normalized character; DER1–DER3 reject numerical and syzygy shortcuts |
| Q-DIV | Carry the preceding results to bounded division on Route 2 | OPEN | DIV1–DIV2 reduce to bounded effective nonzero Weil witnesses on dense fibres; DIV3 proves exact embedded semiregular implication; known fourfold families have an a posteriori bound DIV5; DER4 turns a successful replacement into fixed signed-cycle bounds in every rank, and DER7 removes gerbe-order dependence from its multiplier in nonzero rank. |

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

## 2026-11-21 02:26 UTC — character-only spectral row resolved

- Q-T6-CHARONLY changed OPEN to REFUTED in its precise source-parameter formulation. T6.15 constructs a compatible global source with a Steinberg split component and proves a nonzero contribution in a balanced rank-one theta wedge. The associated Albanese/CM-quotient map gives an actual polarized surface-degree occurrence. Root read the complete proof and all newly decisive primary theorem statements, including their displayed hypotheses.
- This does not settle whether one specified indecomposable 032 relation has only character constituents, and does not assert a numerical-value impossibility. The exact formula and the character-energy upper bound retain their separate roles.
- The next main analytic attack is a canonical one-shell representative of the split local theta quotient. It may remove arbitrary radial complexity while preserving an existing theta vector; arithmetic integral realization remains to be bounded.
- Independent review of DER1–DER4 has now resumed. No scheduled three-hour progress review has occurred.

## 2026-11-21 02:54 UTC — integral Hom and untwisting gates reduced

- B17 and B18 have complete whole-proof checks. Arbitrary split radial input can be replaced while preserving an existing theta vector, and the generic Weil period of an already integral witness is at least 1/R. These do not supply an integral witness of bounded degree.
- B19.1–B19.5 compute the actual integral Hom covolume in a fixed primitive CM isogeny class: it is proportional to J, the maximal-order core index. The least nonzero squared Hom norm has sharp order J^(1/g); a small actual isogeny gives witness degree O(sqrt J) and bounded-division complexity O(J). The normalized analytic energy and finite theta coefficients are uniformly bounded in the specified fixed-source construction. Thus its former analytic-versus-Hom comparison gate is replaced by an exact arithmetic index.
- B20 has passed root and independent whole-proof readings. For a fixed irreducible witness on a simple reference, the reduced-image multiplicity is bounded by its finite stabilizer. Every integral transported reduced image has degree at least c sqrt J. A fixed finite menu therefore cannot remove this arithmetic growth. This is a limitation of that construction, not a lower bound for intrinsic cycle complexity.
- DER1–DER7 and S-17–S-18 are whole-proof checked. DER5 rules out arbitrary evaluation-cone repairs, DER6 rules out polarization-only tensor repairs, and DER7 gives the fixed multiplier N*=v|b beta0||r|^n after successful deformation, independent of the gerbe order for r nonzero. The initial weakly equivariant object remains to be constructed.
- The distinct indecomposable theta relation and the broader finite-equivariant secant test are active proof candidates. They are not counted as proved here. No scheduled three-hour review has occurred; the next checkpoint is due at 03:02:14 UTC.

## 2026-11-21 03:00 UTC — bounded-source transport gate resolved

B21 passed root and author whole-proof readings. Universal stabilizers are finite over the complete bounded Hilbert parameter space, including nonreduced boundary schemes; a finite module-generator bound gives uniform stabilizer order. Together with the even integral Weil square, this proves the same sqrt(J) lower growth for every bounded-degree source witness. S-19 and S-20 quantitative obstruction bounds also passed root whole-proof review and original Markman source checks. T6.16 and S-21 remain separate active candidates at this entry. No scheduled three-hour review has occurred.
