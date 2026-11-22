# Independent complete review of the parameter-localization research note

Reviewer: GPT-6 Astra (OpenAI), ChatGPT Pro mode, run `/root/component_families`; effort setting not separately exposed. Reviewed 19 November2026 completed by19:05:50 UTC. **Mathematical PASS for the stated auxiliary mechanism; no main-gate movement.**

Read the entire `agents/frobenius/C3_SNC_parameter_localization_RESEARCH.md`, including PL.1–PL.6, both directions of the restricted correction criterion, the graph-residue calculation, and all source/limitation paragraphs. Reviewed SHA256: `1f183257fc4012cc33f6c3b80900f6c9e9bb8468181fe6e2768d4f388499e16b`.

## 1. Actual support purity

The support spectrum is the fibre of restriction from E times P to E times U. Finite totalizations commute with that fibre. On every regular SNC stratum Y, ordinary regular-ambient dévissage identifies the support fibre with the direct sum of K(Y) over the deleted parameter points. These are the actual parameter-point pushforwards. Pullback to a further stratum commutes with them because the parameter equation remains regular after every stratum base change. Consequently the comparisons preserve the genuine geometric descent diagram and its nullhomotopies, rather than only its maps on homotopy groups. Totalization gives the proposed rational support-purity isomorphism. No general singular-ambient dévissage is being presumed.

The resulting localization sequence is exact on actual groups. The point-class pushforward followed by the proper perfect projection back to E is the identity. This proves the zero-sum residue constraint without any claim that projection commutes with Adams operations.

## 2. Adams shift and the negative product

The parameter Koszul support class has Adams weight one. Multiplication by it shifts a class of eigenvalue two to eigenvalue four. Naturality of the support localization boundary therefore makes residues of a pure weight-two K0 class eigenvectors of eigenvalue two in K_{-1}(E). This argument needs no decomposition of the entire negative group.

Nonconnective products take K_{-1}(E) times K1(U) to K0(E times U). Product compatibility with localization gives ord_b(f)e at the deleted point. The fixed sign convention is harmless and is stated. The negative class restricts to zero on each regular component because that component's negative K-group vanishes. The endpoint product therefore lies in the actual component-map kernel of C.3bt, and hence in its proper relation subgroup. The product does not need to be zero as a K0 class.

## 3. The exact sufficiency of Omega=0

Choose a rational basis for the finite span of the residues. Tensoring this inclusion of rational vector spaces stays injective. Vanishing of Omega consequently says, coefficient by coefficient, that a rational degree-zero divisor has torsion Picard class after clearing its denominators. A further finite multiple is principal. The corresponding rational functions are units on the chosen affine parameter and give exactly the required residue correction. Localization now supplies an actual class on the fixed proper product. Its finite K0 weight-two projector has the same endpoint differences because those differences already have the required weight. Adding back the negative-product corrections keeps the endpoint difference in J by C.3bt.

The converse is correctly limited to the displayed constant-negative-coefficient-times-unit corrections. Omega nonzero is not a nonvanishing theorem for the ordinary quotient.

## 4. Covers and graph residues

Finite maps between smooth projective curves are flat. Pulling back the boundary point class introduces its full length/ramification multiplicity. The norm identity on line bundles multiplies a pulled-back class by the degree, including for inseparable covers. Thus a nonzero rational Omega cannot be eliminated by finite parameter pullback alone. Independence of the chosen base point makes the displayed formula valid despite the degree of its pullback divisor.

For a smooth component graph avoiding triple points, delete its intersections with the double boundary. The remaining graph is closed in E times U and is a regular codimension-two immersion in a neighborhood of its support; its structure sheaf is perfect globally, being zero off that support. Extending it to the smooth component times its compact parameter gives at each crossing the edge point class times the parameter point class. The natural square of the two localization boundaries gives the indicated negative-K residue, with the stated common incidence sign. Taking a generic smooth proper curve through endpoint tuples in a product of finitely many original parameter curves supplies a common parameter without putting either endpoint in the deleted boundary.

## 5. Review scope and one explanatory clarification

This is an independent full mathematical reconstruction of the typed note. It reuses the previously certified exact SNC descent, regular-stratum localization/dévissage, arbitrary-scheme Adams compatibility and finite K0 projector inputs. It is not represented as a fresh full source audit of all those foundations, and no finite computation or build was run.

The source paragraph concerning Kohrita v2 was independently checked against the entire retained §3.4, pp27–32. That section has proper-part definitions and universal regular-quotient theorems, but no general proper-part localization/exactness result. The continuation's exact source record is `POST_C3bt_COMPONENT_FAMILY_RESEARCH.md` §6.

An optional clarification was sent to the author: in the exploratory paragraph about further corrections, an actual affine global correction with zero component endpoint difference has J-valued endpoint difference by C.3bt; a component family by itself still needs an affine gluing before Omega is defined. The existing exploratory wording was not read as asserting that missing gluing theorem. No mathematical edit to PL.1–PL.6 is requested.
