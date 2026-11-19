# Independent audit: actual K0-family descent from completion

**Outcome: passed as a K0 auxiliary lemma.** Audited the complete §7 of `research/agents/real_weil/TOP_QUOTIENT_RESEARCH.md` on 2026-11-19, with primary-source checks completed at approximately 08:59 UTC. This is not a new numbered result and does not assert any Chow-group conclusion.

Let R be an excellent henselian local ring equipped with its specified coefficient field k equal to the residue field. For a qcqs R-scheme Z, the quotient of K0 of perfect complexes by differences of evaluations of actual classes on products with smooth projective connected k-curves injects integrally into the analogous quotient after completion.

The proof is correct. Excellence makes R to its completion regular. Popescu expresses that completion as a filtered colimit of smooth finitely presented R-algebras. Perfect complexes, their morphisms, and finite triangle relations descend to a single stage. In particular an equality in K0 uses finitely many generators and relations; it is not necessary to claim any inverse-limit continuity of K-theory. The residue map from that smooth stage to k lifts to R by the henselian lifting lemma. Pulling back the already descended actual complexes and relations proves the assertion. The selected coefficient field and all proper curve parameters are preserved because this is an R-algebra map.

All four cited primary sources were opened and inspected:

- Stacks Project, Theorem 16.12.1 (Tag 07GC), https://stacks.math.columbia.edu/tag/07GC: regular maps between Noetherian rings are filtered colimits of smooth maps. Web reference `turn612165832view0`.
- Stacks Project, Situation 36.29.1 (Tag 09RC), https://stacks.math.columbia.edu/tag/09RC: qcqs terms and affine transition maps; the adjacent Lemma 36.29.2 also supplies full faithfulness. Web reference `turn115228967view0`.
- Stacks Project, Lemma 36.29.3 (Tag 09RF), https://stacks.math.columbia.edu/tag/09RF: perfect derived categories commute with the indicated limit. Statement and proof read. Web reference `turn612165832view1`.
- Stacks Project, Lemma 15.13.3 (Tag 0H74), https://stacks.math.columbia.edu/tag/0H74: a map from a smooth R-algebra to A/I lifts to A for a henselian pair (A,I). Statement and full proof read. Web reference `turn115228967view1`.

The limitations written by the owner are essential and accurate: this descends an already existing actual family over the completion; it does not algebraize arbitrary compatible formal K0 classes, and it does not establish a comparison with ordinary Chow equivalence.
