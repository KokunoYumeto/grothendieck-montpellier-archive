# Root check of the Cha 2026 cylinder scope

We obtained the original PDF of Jae Choon Cha, *Topological mapping class
groups of non-simply connected 4-manifolds*, arXiv:2610.26400v1
(19 October 2026), from <https://arxiv.org/pdf/2610.26400>.
Its 450,008 bytes have SHA256
`27171c8dcde308b910bc8575bdd1637778e083b6729dcd7f81478499f69f207e`.
Our temporary copy is `/tmp/SA20_Cha_2026/cha.pdf`; the independently
obtained identical original is outside the authored project in
`source_external/Cha2026_mapping_classes.pdf`.

We read the introduction and definitions through printed page 9,
then the precise converse in Proposition 4.1, pages 15–16, and the
sphere hypotheses and statements in Section 8.1, pages 29–31.
Proposition 4.1 retains the boundary geometric-dual hypothesis.
Theorem A supplies an invariant without a completeness assertion.
The sphere construction also requires a geometric dual. These are
the original passages relevant to the route we checked, not a claim
to have audited the entire paper.

We independently checked both elementary exclusions in the agent's
`logs/Cha2026_mapping_class_scope_audit.md`. If a neat disk lies in
`B×I` for closed `B`, its boundary loop lies in one end. That end
includes by a homotopy equivalence, so the loop is nullhomotopic
there and has zero mod-two intersection with every boundary sphere.
It therefore cannot have a boundary geometric dual. Also, one end
surjects onto `H_2(B×I; F_2)`, so the map to relative second homology
vanishes. The closed interior intersection pairing consequently
vanishes, excluding two geometrically dual interior spheres.

We have not computed the Dax group of `RP^3×I` and have not inferred
any zero-invariant sufficiency theorem. The source check does not
change the actual PL image, the comparison kernel, an original row,
or the size of a named main gate. The independent authored source
note preserves the remaining exact locators and retrieval details.
