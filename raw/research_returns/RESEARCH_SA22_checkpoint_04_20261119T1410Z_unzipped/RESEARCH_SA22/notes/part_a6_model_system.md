# Canonical compactification systems: supplementary proof and scope

Date: 2026-11-19. Author: GPT-6 Astra (OpenAI, ChatGPT Pro mode; inherited effort not separately exposed), agent `part_c_algebra`.

## Task and result

The literal question 67/049(c), as transcribed in `inputs/RESEARCH_SA22_transcriptions/transcriptions/MPL_67_002-052_transcription.tex:1081`, asks for a definition of an anabelian compactification of a smooth anabelian variety in characteristic zero and its behavior under specialization. The active A6 section already supplies a chosen logarithmic compactification, all-dimensional existence, a finite-cover specialization theorem, the counterexample to recovery of an arbitrary chosen compactification, and an ample-log-canonical recovery criterion.

The additional fragment `sections/part_a6_model_system.tex` strengthens the answer without imposing an arbitrary choice of compactification. It contains two complete proofs:

1. `A6-model-system`: the category of all smooth proper strict-normal-crossings compactifications of a fixed smooth geometrically connected separated finite-type variety over a characteristic-zero field, with arrows restricting to the identity on the interior, is nonempty, essentially small, thin and cofiltered. Every arrow is proper and has preimage of the interior exactly that interior. Its scheme-valued inverse system with marked common interior is independent of all initial models and small-skeleton choices. An isomorphism of interiors extends uniquely to a marked pro-isomorphism. An explicitly assumed Isom-anabelian theorem consequently reconstructs the full system, not one preferred model.
2. `A6-model-specialization`: over the same trait `Spec k[[t]]` and the same generic open `U/k((t))`, the category of regular proper integral models with strict-normal-crossings complement is nonempty and cofiltered. The equivalences between finite étale covers of `U`, finite Kummer-étale covers of each model, and finite Kummer-étale covers of its strict closed log fibre commute with every transition map. Common-refinement comparisons are independent up to the unique natural isomorphism normalized by the identity on covers of `U`. The augmented groups and their tangential specializations for the same frame agree.

## Complete proof audit points

- Smooth and geometrically connected over a field implies geometrically integral: a regular scheme has disjoint irreducible components locally, and a noetherian connected regular scheme has just one component.
- Two arrows agreeing on the dense interior are equal because the source is reduced and the target separated.
- For an arrow `f:X→Y`, the inverse image `W=f^{-1}(U)` contains the original copy of `U` as a section of the separated morphism `W→U`. That section is closed and also open. Since `W` is a nonempty open of an integral scheme, it is irreducible; hence `W=U`. This avoids any unproved assertion about exceptional loci.
- The graph closure in `X1×X2` is integral, proper, and contains `U` as an open. The last point uses the fact that the graph is closed over the open `U` of either factor; it is not inferred from density alone.
- Principalize the reduced complement, which contains all singular points, while fixing `U`. The resulting regular model has strict-normal-crossings reduced boundary. This gives common domination. Uniqueness of arrows makes the equalizer condition automatic.
- Models dominating any one model, or any finite list, form a cofinal inverse-indexing category: the relevant comma categories are nonempty and cofiltered, hence connected.
- The marked interior is essential. The assertion does not identify `U` merely from an unmarked underlying pro-scheme. In dimension one, for example, the common smooth proper model alone would forget its deleted set.
- Reconstruction of each normal torus gives the family of tangential fibre functors; it does not select a distinguished nonzero normal vector or a rational point.
- Over `R=k[[t]]`, `F=R[1/t]` is a finite-type `R`-algebra, so the compactification theorem applies to `U` as a finite-type `R`-scheme. Every integral model dominating the trait is flat because its coordinate rings are torsion-free over the DVR. Excellence is preserved under finite type.
- The divisor of `t` is supported on the boundary; locally it is a unit times a monomial in the boundary parameters. Thus the divisorial log structure has the canonical morphism to the base log trait.
- The finite-cover comparisons are pullback/restriction comparisons, with contravariant variance. An arrow from a dominating model to another yields pullback from the latter cover category to the former; every square has the identity functor on `FEt(U)` at the bottom.
- Full faithfulness of restriction makes any comparison isomorphism unique once it is required to induce the identity on `FEt(U)`. This gives refinement independence and the cocycle condition, rather than claiming an unnormalized strict equality of arbitrarily chosen quasi-inverse functors.
- All specialization assertions concern actual models of the same generic open over the same trait. No unrelated compactification over `k` is silently treated as a model of a family.
- The log-special-fibre cover statement does not assert equality with the ordinary singular special fibre, nor does it assume that an ordinary singular fibre preserves the geometric fundamental group.

## Opened primary sources and exact locators

1. Michael Temkin, *Functorial desingularization over Q: boundaries and the embedded case*, author arXiv0912.2570v2 (6 September 2016), full 34-page PDF: `https://math.huji.ac.il/~temkin/papers/Embedded_Desingularization.pdf`. Independently opened as web reference `turn601754405view0` and exact theorem finds `turn521022071view0`/`turn521022071view1`.
   - Theorem1.1.11, printed p.4: weak principalization on a noetherian quasi-excellent characteristic-zero scheme, supported on the closed set together with its singular locus; output regular with strictly monomial total transform.
   - Theorem1.1.15, printed p.5: a regular separated finite-type scheme over a noetherian quasi-excellent characteristic-zero base, with an existing SNC boundary, has a regular proper compactification with SNC total boundary.
   - Proof §3.5.3, printed p.24: the compactification/principalization construction preserves the prescribed regular open and explains density. These are the exact hypotheses used over both a field and `k[[t]]`.
2. Abramovich–Karu–Matsuki–Włodarczyk, *Torification and factorization of birational maps*, author arXiv:math/9904135v4, full PDF `https://arxiv.org/pdf/math/9904135`, independently opened as `turn601754405view1`.
   - Theorem0.3.1, pp.2–3, especially(6): weak factorization for complete nonsingular varieties over an arbitrary characteristic-zero field, respecting the boundary by normal-crossing centers outside the fixed open. This is a zigzag. The common-domination proof does not invoke strong factorization, nor claim that both maps from the common model are sequences of smooth-center blowups.
3. Yuichiro Hoshi, *The exactness of the log homotopy sequence*, original author preprint RIMS1558, July2006, `https://www.kurims.kyoto-u.ac.jp/preprint/file/RIMS1558.pdf`, opened and used in the existing `A6-log-specialization` proof.
   - PropositionA.10, pp.57–58: log-regular finite Kummer-étale covers correspond to interior covers tame at the boundary.
   - Corollary3.9, pp.31–32: properness over a complete local base and log regularity give the strict closed-log-fibre cover equivalence. Residue characteristic zero makes all finite boundary ramification tame here.

The bibliography keys are already present in `sources/part_a567.bib`; no duplicate source entries were introduced.

## Independent reviews and limits

The A567 author independently read both complete proofs and reported no gap in graph closure, common domination, preimage equality, pro-map uniqueness, variance or specialization hypotheses. The requested precision that one reconstructs the family of normal frames, not a distinguished frame, is now explicit. The B agent independently completed a second review and saved `notes/part_b_a6_model_system_audit.md` and `checks/part_b_a6_model_system_events.tsv`; no substantive flaw was found. Its two wording refinements are included: the morphism is from the model log scheme to the base log scheme, and special-fibre comparison uniqueness is explicitly normalized by chosen equivalences `E_X` to `FEt(U)`. The root independently approved the full proof and authorized insertion before the mapping-class subsection of `part_a6.tex`; that insertion is now made.

These theorems supply an invariant replacement for a chosen compactification. They do not prove that every smooth anabelian variety has an ample smooth log-canonical compactification, or that every boundary stratum is anabelian. The amended scope is stronger than a choice-dependent definition while preserving those distinctions.

No finite example or computational search occurs in these proofs. No new computational test was warranted or run.
