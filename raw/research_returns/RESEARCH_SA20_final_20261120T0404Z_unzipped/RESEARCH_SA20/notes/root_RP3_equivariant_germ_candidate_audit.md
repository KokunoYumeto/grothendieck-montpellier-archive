# Root full audit: the projective-three-space joint-germ fibre

We completed this literal proof and primary-source audit at 2026-11-20T02:08:20.346246+00:00. The audited file is `agents/higher_comparison/logs/pending_RP3_equivariant_germ_fibre.tex`, SHA256 `65d269d360f1a6d93d1489b8f54e3e844fb8b41aaef9ca38e9d777d82635652e`. We read all301 lines. It is a complete candidate reduction, not an evaluation of the remaining TOP comparison and not movement credit.

## Mathematical audit

1. Joint germs are taken along the whole compact parameter zero section. Finite horn-face equalities therefore give a common ball on which equality holds. This is stronger than pointwise germ equality and is necessary in the proof.
2. Edwards–Kirby supplies a continuous deformation, fixed at the inclusion and outside a compact collar. For the compact quotient annulus, equality near its boundary fixes the image region. The correction f composed with the inverse deformed embedding is an ambient isotopy. Its identity-started lift through the double cover is odd and normalized. Close lifts on the connected collar select the required sheet.
3. The inner local map and outer correction agree on an annular neighborhood of the joining sphere. The inner image is the component containing zero and the outer image is its complementary annulus; thus the pasted map is globally a homeomorphism. Compact-parameter evaluation and inversion are continuous.
4. The individual extension uses only the ordinary annulus theorem and the free equivariant annulus theorem. A constant-in-radius change of product coordinate corrects the prescribed inner parametrization exactly. No parametric conclusion is inferred from the individual annulus theorem.
5. A horn retract supplies the global preliminary family. Dividing its germ out produces an actual local family equal to the identity on a common ball over the horn. After a fixed domain restriction, uniform continuity on the compact parameter–time space supplies one finite time subdivision. Successive normalized local extension factors give exact prescribed horn values and germs. The multiplication order in EG.6–EG.7 is correct.
6. The strict fibre is the union in the simplicial sense of common-ball identity families. An expanding radial conjugacy moves any finite representative into the fixed-radius subgroup and preserves that subgroup throughout. The same conjugacy on a nullhomotopy, with its boundary track attached, proves injectivity. This avoids assuming a topology on individual germs.
7. The fixed-radius subgroup is naturally the full bottom-fixed projective concordance group, by the uniquely identity-marked lift on the inner boundary. The outer boundary is allowed to move, as required.
8. Boundary restriction of odd ball homeomorphisms has radial coning as a section, and its boundary-fixed kernel contracts by the equivariant Alexander formula. The induced map to germs is the cone-germ map.
9. The projective Smale theorem and the ordinary Diff-to-TOP3 comparison lift through the natural double covers to the specific linear inclusion O(4) into odd sphere homeomorphisms. A nonequivariant sphere equivalence alone would not justify this step.
10. Orientation separates the two components of the germ group; vertex extension and the middle equivalence prove that there are only those components. The long exact sequence therefore gives the stated cokernel on pi0. The group pi1(O(4)) is Z/2. The coset-fibration loop description is a weak-type reduction, not a computation of the coset space.

We found one typesetting typo, `r_t|_Z=operatorname{id}`, and asked the author to insert the missing backslash. This does not affect the argument.

## Original-source audit

| Original | Exact opened locator and scope | Retrieval |
|---|---|---|
| Boyle–Chen–Conway, Involutions on S4, arXiv2512.22724v1 | Theorem2.3 and proof, printedp6: free involution on S3×I preserving both ends is conjugate to antipodal×identity. This is an individual TOP product conclusion. | https://arxiv.org/pdf/2512.22724 ; turn446099388view2 |
| Bamler–Kleiner, Ricci flow and contractibility of spaces of metrics, arXiv1909.08710v1 | Theorem1.3, printedp2: the actual isometry inclusion is an equivalence for every round spherical quotient, including RP3. | https://arxiv.org/pdf/1909.08710 ; turn500771395view1 |
| Edwards–Kirby, Deformations of spaces of imbeddings | Theorem5.1(1), printedp70, and proof of Corollary1.2, printedp79: normalized continuous compactly supported deformation and ambient correction. | https://math.berkeley.edu/~kirby/papers/Edwards%20and%20Kirby%20-%20Deformations%20of%20spaces%20of%20imbeddings%20-%20MR0283802.pdf ; turn108334551view0/1 |
| Cerf, Groupes d’automorphismes…,1959 | Theorem5 and Corollary1, printedpp327–328, with its Smale input explicitly identified. | https://archive.numdam.org/item/10.24033/bsmf.1528.pdf ; turn108334551view2 |
| Cerf, Topologie de certains espaces de plongements,1961 | Full thesis ChapterIII§3.2.1, Theorem8 printedp365 and Corollary1p366. The statement explicitly assumes the Smale conjecture, discharged by the preceding modern theorem. | https://www.numdam.org/article/BSMF_1961__89__227_0.pdf ; turn108334551view3 |

## Outcome

**PASS as a precisely scoped fibre-model reduction**, pending the independent full audit. We do not infer the PL-image equality, the comparison kernel, a zero-Casson–Sullivan sufficiency theorem, or a computed whole TOP model. The original A.1(b) row remains open, and the reduction alone is not qualifying movement under the user's rule.
