# Independent literal audit: RP3 relative homotopy normalization

Observed UTC: 2026-11-20T02:59:55.438986+00:00
Candidate: `agents/higher_comparison/logs/pending_RP3_relative_homotopy_normalization.tex`
SHA256: `44173842078ca109e6f48900f5a8c0739c2a0f838b8770cee3d788f54ea851d4`

Verdict: **PASS**, as a normalization/equivalence of the unresolved image problem. No computation of the PL-to-TOP component kernel or zero-CS image equality is obtained.

## Literal proof check

I read the entire candidate. Fixing the top uses an ordinary isotopy of its orientation-preserving RP3 endpoint. The trace removes it within the free-top concordance component. The level projections of the resulting both-end-fixed homeomorphism form a loop of homotopy equivalences: every level inclusion, the cylinder homeomorphism, and cylinder retraction are homotopy equivalences. The linear interpolation of the interval coordinate is relative to both ends.

Closing the cylinder gives an actual homeomorphism of S1 x RP3, so the associated homotopy equivalence has zero TOP normal invariant. The extra order-two coordinate in Jahren--Kwasik is consequently absent. This uses the original calculation and composition with homeomorphisms; it does not assume injectivity of a gluing map on structure sets or classify isotopies.

The surviving projective-orthogonal loop can be represented by a jointly PL automorphism loop using the already checked ordinary three-manifold comparison. Its trace is PL. Removing it leaves a representative homotopic to the identity relative to both ends, in the same free-top TOP component. The homotopy here is correctly not called an isotopy.

For the final equivalence, a free-top isotopy to a PL concordance is first normalized to a PL endpoint fixing both ends. Its top loop is removed by the explicit inverse trace. Replacement of that loop by a based jointly PL loop uses the ordinary pi1 comparison; a based homotopy of loops gives an actual rel-both-end TOP isotopy of their traces. The resulting endpoint is literally PL. This proves the stated relative reformulation, not its unresolved sufficiency assertion.

## Primary source independently opened in this audit

B. Jahren and S. Kwasik, *Free involutions on S1 x Sn*, Math. Ann. 351 (2011), 281--303, DOI10.1007/s00208-010-0599-y.
Full published PDF: https://link.springer.com/content/pdf/10.1007/s00208-010-0599-y.pdf
Tool references: turn799564411view0; turn129961059view0, turn129961059view1, turn129961059view2.
Read original Proposition3.5 and proof, printed294--296, and Remark3.6(ii), printed296. The proposition explicitly separates one Z/2 summand with nonzero normal invariant from summands represented by homeomorphisms. Remark3.6(ii) identifies pi1 Aut(RPn) with pi1 PSO(n+1) times that Z/2. No screenshot viewing is claimed in this audit.

## Separate OW23 scope check

Freshly opened original Ohta--Watanabe arXiv2303.13877v2 (18October2023), https://arxiv.org/pdf/2303.13877, reference turn689241528view0. Read printed1--4: Proposition1.3 gives the even theta-graph rank p3(n-6), zero at n=2 (RP3). Theorem1.5 concerns smooth stabilization for C(M x I), and Proposition1.7 a block quotient. These do not compute the ordinary PL-to-TOP component kernel. This is source-scope evidence only.
