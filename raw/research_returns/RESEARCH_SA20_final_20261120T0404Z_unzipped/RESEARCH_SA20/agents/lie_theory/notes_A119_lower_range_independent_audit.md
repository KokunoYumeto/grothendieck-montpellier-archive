# Independent A119 lower-range audit

Date: 2026-11-19 16:41 UTC. Auditor: lie_theory. Verdict sent to root and singularities_duality: PASS, with the source dependency stated explicitly below. No checked root source was modified.

## Logical dependency of the full chi comparison

The proof uses the FULL corrected geometric exact-sequence theorem, as restated by Igusa in arXiv:2112.08293, Theorem3.1, printedp6, in the explicitly stated range dimM>=6. Its chi is the corrected Igusa map, not an unspecified map selected merely to make an abstract exact sequence. Igusa arXiv:2110.09659, introduction(0.2), printedp2, restates that same correction for the stable group. Jahren2010, Section2 and Corollary2.7, pp247–250, identifies the functorial A-theory sequence as Igusa's sequence and includes both the pi2 and Z/2 parts of the coefficient module. Under this cited full-theorem identification, the full chi relation subgroup is unchanged by MxI->M. The unavailable original1984 chapter is not claimed to have been opened or re-proved.

There is an important logical distinction to keep in the manuscript: the marked-lens square and compatibility of its framed invariant alone give only ker(theta_unstable) subset ker(theta_stable). They do NOT prove equality of those kernels. Similarly, the matrix expression in Igusa2112.08293 Th3.1 is explicitly only the pi2 component. The equality of relation subgroups is being imported from the identified FULL corrected exact-sequence theorem. The later functorial A-theory construction is a description of that whole named map, not an independent proof that arbitrary maps with the same pi2 projection agree.

## Fixed-index and boundary audit

Hatcher–Wagoner, original printedp184, PartI ChapterV Theorem3.1(a), allows 2<=i<=n-2 for the one-parameter two-index reduction. I rendered and visually read this original page; the inequalities are non-strict. PartII Section2, originalp244, explicitly applies it to representatives of the pseudoisotopy component group. Thus indices3,4 are allowed for every n>=6. Igusa2110.09659 Lemma1.10 pp9–10 then uses the available conditions k>=3 and n-k>=3 for the framed-circle realization and bordism simplification. The proof's displayed choice floor(n/2) is not an extra geometric requirement. No high-dimensional two-parameter reduction from Hatcher–Wagoner V.Th3.1(b) is substituted for the corrected chi theorem.

Igusa2110.09659 p1 defines C(M) with the lower and side boundary fixed, for arbitrary compact smooth manifolds; p3 takes functions equal to projection near the entire boundary. The constructions therefore apply to compact boundary models and to MxI^j after rounding corners. Hatcher–Wagoner's original boundary convention allows an isotopy on the side, so the direct fixed-side convention from Igusa is the cleaner citation here; collar normalization supplies the standard equivalent model used for suspension.

Igusa2112.08293 Section4.1 p8 gives the positive suspension on fixed polar rays. On the subgroup normalized near the lower/side boundary and product near the top it preserves composition. Section4.2 p9 explicitly compares the entire framed invariant under positive suspension, so it includes Z/2 as well as pi2. Keeping k=3 avoids parity-dependent changes of the stable sign convention. Hatcher–Wagoner PartI ChapterIV Section1, Remarkp130, supplies invariance of the first obstruction; the trajectory argument is PartI ChapterI Section5, equation(5.2), p60.

With the full common chi image as the above cited input, both outer arrows in the diagram of short exact sequences are identities. The middle positive-suspension arrow is consequently an isomorphism, by the elementary kernel/quotient argument. No splitting of the extension is used.

## Sources opened independently in this audit

- https://arxiv.org/pdf/2112.08293 ; web turn253108845view0; exact Theorem3.1 find turn295526290view0; suspension/framing find turn295526290view1.
- https://arxiv.org/pdf/2110.09659 ; web turn253108845view1; Theorem1.8 find turn295526290view2; Lemma1.10 and full proof find turn295526290view3. Introduction, compact boundary convention and marked-lens square read.
- https://www.maths.gla.ac.uk/~mpowell/Jahren2010_Article_PseudoisotopiesAndTheBokstedtT.pdf ; web turn253108845view2; full basic-diagram passages turn237293733view2–4; Cor2.7 turn295526290view4.
- https://www.maths.gla.ac.uk/~mpowell/Hatcher-Wagoner.pdf ; web turn571718199view0; original p184 screenshot turn263158509view0 and local image source_external/lie_theory/hw_p184.png; original p244 text read locally and web screenshot turn263158509view1.

The newly searched corroborating broad stability estimates were not used to lower the threshold. This audit does not change the original1984 access status.
