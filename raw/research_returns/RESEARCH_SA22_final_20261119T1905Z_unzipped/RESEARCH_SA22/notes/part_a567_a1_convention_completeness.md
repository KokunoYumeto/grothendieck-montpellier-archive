# Adversarial completeness audit: cuts, isotopies and phase conventions

Reviewer: part_a567, GPT-6 Astra Pro, OpenAI. Date:2026-11-19. This follows the current integrated A1 text, the attached transcription and the already visually read original scans079–082. No finite mathematical check was repeated and no existing TeX file was edited. The additional proof is `sections/part_a567_toric_descent.tex`.

## Outcome

The audit found one further genuine convention: **forget the actual embedded toric cut up to isotopy in the same conformal surface, while still computing its tensor from a freely chosen toric representative**. This is not the already treated convention of first replacing that representative by its geodesic. Initially this was an unproved descent assertion; the separate addition now **refutes it**, with a complete exact analytic counterexample. Thus no unresolved descent premise is being left inside the current A1 inverse statements.

The fixed-target R^E-fiber theorem alone did not settle this question. Its deformation retraction holds the capped normalization and tensors fixed and can change the welded conformal surface. We did not identify it with an isotopy in a fixed X. Instead, a new third-order plumbing calculation proves that two fixed-target weldings give different underlying four-pointed surfaces; comparison with the unique geodesic representative then supplies two isotopic toric cuts inside one fixed X with different tensors.

## Exact source distinction

All line locators below refer to `inputs/RESEARCH_SA22_transcriptions/transcriptions/MPL_67_053-101_transcription.tex`, not our manuscript.

- Lines799–810, scan074: cut X along C and use the canonical metric of the cut surface X′. No geodesic or paired-length equality is stated there.
- Lines837–839, scan075: objects are holomorphic compact cut surfaces and arrows are isomorphisms. This directly supports actual embedded cuts with conformal isomorphisms preserving them; it does not itself identify arbitrary isotopic embeddings.
- Lines939–944, scan079: the welded circles may not be geodesic, but determine unique geodesic circles. These are two separate operations.
- Lines946–963, scans079–080: the author asks whether the welded result is independent of polar disc choices and proposes that small reciprocal rescaling gives the same X with nearby Γ. The inserted warning says the asserted proportionality of the realized embedded discs is probably false. Our new proof addresses the stronger same-underlying-X independence as well, rather than treating the earlier cap-shape counterexample as automatically answering it.
- Lines973–977, scan080: the gluing is fixed by an actual θ in a unit-circle torsor. This supports circle phases, not an automatically chosen real lift or a chosen angular origin on each cap.
- Lines994–1015, scans081–082: the fundamental-group and tangent/étale questions are explicitly for a fixed cutting type. They do not assert compatibility with node-changing compactification topology.

Original scans079–082 were visually read in this session, with the nongeodesic, rescaling, fixed-type and tangent phrases confirmed. No additional resolution of the uncertain target notation at lines986–991 is required by the counterexample or the convention comparison.

## The newly proved non-descent, with transparent exact choices

Write r(λ) for the canonical one-cap pant radius at boundary length2πλ. Its normalized inverse cap germ is

    g_λ(z)=z+z²/2+[5/16+1/(16(λ²+4))]z³+O(z⁴).

The coefficient is derived from the three-point projective connection, with the cusp coefficient1/2 explicitly obtained from the Schwarzian of log q. For fixed germs g1,g2, the cross-ratio convention is first∞→∞, first1→1, second∞→0; the second1 then has

    Λ(t)=t−t²/2+[11/64+1/(64(λ1²+4)(λ2²+4))]t³+O(t⁴).

The proof supplies convergent Laurent matching, choosing small fixed node discs inside |z|,|w|<1/2 for coefficient evaluation at the marked1's. Its later larger parameter family is the holomorphic continuation using the actual extended cap coordinates.

Set r1=r(1), r*=r(1/2), r2=r*²/(4r1), r0=r*/2, R=r0²=r1r2. This fixes every pant without a search over radii. The unequal pair and equal pair have the same tensor Rη. Their cross-ratio difference Δ(c), with t=Rc, is holomorphic on an explicitly described disc |c|<ρ withρ>1. The half-collar extension radii are r(λ)exp(arctan(csch(πλ))/(2λ)). Its cubic coefficient is strictly less than−31R³/369920, so Δ is nonzero and has only finitely many zeros on the unit circle.

The phase is specified deterministically by N=min{n≥1:Δ(exp(i/n))≠0}, η*=exp(i/N). The identity theorem proves N exists, because exp(i/n) accumulates at1 strictly inside that holomorphy disc. **N is not numerically evaluated.** This is an exact analytic specification, not a claimed numerical example or an unreported finite certificate. In fact every phase outside a finite exceptional set works.

Take X to be the unequal welding atη*. Its actual seam C has tensor Rη*. Its unique geodesic C_geo is isotopic to C in this same labelled X. If its tensor were unchanged, the proved unique geodesic inverse would identify X with the equal-pair welding, contrary to their unequal cross-ratios. Thus raw surgery fails to descend under this isotopy identification. This directly disposes of the residual convention identified at the start of the audit.

The same construction also refutes universal local polar-rescaling independence: join the balanced and unequal radius splits by a path with fixed productR and fixedη*. Their underlying cross-ratios have different endpoint values. The dependence is real-analytic, so it is not locally constant everywhere on that path. This is not an assertion that every small rescaling changes X.

## Remaining convention branches

| Convention | Exact status and reason |
| --- | --- |
| Actual arbitrary smooth/analytic embedded cuts | Refuted as a source for the asserted tensor construction by A1-nontoric-cut; its boundary map is not a pointed-disc antiisomorphism. |
| Actual canonically toric cuts, paired lengths independent | Completely described by A1-toric-domain and A1-toric-full-discs: same support image, extra imbalance fibers for tensor/shadow targets, and separate full-shape equations. |
| All seams geodesic, or toric plus equality of every paired length | The proven geodesic model and its unique inverse onto the proper image. Equality is required at every edge for the restriction-of-metric argument. |
| Essential cut isotopy classes with geodesic replacement before surgery | Well-defined by unique simultaneous geodesic representatives; the source used in A1-cut-not-algebraic and the graph range theorem. |
| Essential cut isotopy classes with arbitrary toric representative and raw surgery | **Refuted** by A1-toric-nondescent. This is not silently identified with the preceding row. |
| Unit-disc coordinates or angular origins changed without changing the actual seam | Coordinate gauge: the rotations change the phase coefficient and cap derivatives inversely, leaving q invariant, as proved in A1-tensor. No new source object or invariant is introduced. |
| Full marking retaining a real Fenchel–Nielsen twist | Requires the stated Dehn-twist quotient or the matching phase cover. Recording a real lift only on the source gives an additional integer ambiguity; the text already excludes that mismatch. |
| Ordered versus unordered branches, graph labels, and permitted label permutations | Covered by equivariance. Tensor factors have their canonical interchange; imbalance signs reverse on branch exchange. Finite graph/curve automorphisms must be retained for orbifold statements. |
| Inverse pairing instead of a nonzero tangent tensor | Scan078 lines915–921 explicitly allows q^{-1}. This is an equivalent dual-line convention, not a new construction: invert the tensor coordinate and transport the image and phase accordingly. |
| Extra marked boundary points, parametrized circles, or retained full coordinate germs | These are additional structures, absent from the stated tensor target. They may be retained on both sides or forgotten/quotiented; the existing finite-dimensional isomorphism is not asserted after adding them only to the source. Arbitrary circle parametrizations would define a different, generally infinite-dimensional problem. |

For a smooth cut whose two canonical boundary structures are actually torically compatible, the analytic welding model constructed from those canonical cap coordinates has an analytic seam and is conformally the original surface: the matching map is conformal off the seam and extends across the analytic seam by Morera/reflection. Thus permitting smooth rather than analytic torically compatible representatives does not supply a new unmatched finite-dimensional branch of the construction. The arbitrary smooth, nontoric case already fails earlier.

The manuscript's arrows are holomorphic isomorphisms of surfaces. Whole-surface antiholomorphic maps and nonperipheral homotopy equivalences are not covertly included; A1-dimensions states the geometric marking convention and gives the explicit peripheral counterexample. The antiisomorphism at a seam is a local boundary identification, not a reversal of the whole-surface category.

## Review and records

Root independently confirmed the cap third jet and read the full descent proof, requesting the explicit cusp and small-disc typing clarifications now included. PartB independently derived the full cubic Laurent coefficient by hand and approved the collar domain, exact strict gap, deterministic phase and fixed-X bridge. No numerical phase, finite test, or priority claim is made. New labels: A1-pant-third-jet, A1-four-point-plumbing-jet, A1-toric-nondescent. The existing source-retrieval requirements are unaffected.
