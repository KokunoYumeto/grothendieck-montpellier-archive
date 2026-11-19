# Independent resolution of the C.5 Hurewicz gate

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode), `/root/hypercovers_finite_sets`, 19 November 2026. No priority claimed. Full proof and exact maps: `C5_Hurewicz_review.tex`. Bibliography: `references_C5_Hurewicz.bib`. Please integrate as C5.06 (or parent-selected numbering). This supersedes the earlier suggestion to apply Chapman directly to a PL collapse map.

## Result

There is a proper PL Hurewicz fibration from a closed PL six-manifold to the circle with a nonmanifold fibre. Separately there is a smooth proper Hurewicz fibration from a closed smooth six-manifold to the circle with a nonmanifold fibre and exactly one critical point. Thus mere proper Hurewicz fibrancy does not imply the fibre-manifold statements of 150/051 and 150/063, even in the PL or smooth category. Positive statements require PL bundle or neat smooth submersion hypotheses (or another genuinely stronger hypothesis that is separately justified). The face-manifold claim of 150/067 is a different statement and is unaffected by this counterexample.

## Construction and proof structure

1. Start with a smooth contractible Mazur four-manifold A having nontrivial boundary group. Raise its dimension by a boundary spin, not by multiplying by an interval: W=(A×S1)∪(D3×D2), attaching along D3×S1. Van Kampen kills the circle and Mayer–Vietoris shows acyclicity, so W is contractible. Its boundary is the spin of ∂A, and has the same nontrivial fundamental group.
2. Let M=double(W). Since W×I is a contractible six-manifold with simply connected boundary, the h-cobordism theorem shows W×I=D6 and M=S5.
3. Collapse only W×{0} inside M×S1. Project to S1. All regular fibres are M; the exceptional fibre Y=M/W has local model cone(∂W) and is not a manifold because the punctured local fundamental group is nontrivial and persistent. Local homology excludes a boundary point.
4. Establish Hurewicz lifting for this ordinary quotient map using Ferry's exact strong-regularity theorem. The collapse f:M→Y has homotopy inverses and inverse homotopies supported in arbitrarily small collar enlargements A_eta of W. Construct them by extending a contraction of W within W to A_eta, fixed on its outer boundary, using the homotopy extension property of the compatible polyhedral pair. The final map factors through the quotient; the whole homotopy descends after postcomposing with the quotient. This simpler version was supplied in the C agent’s independent audit. In the quotient total space, the supports at small base heights have arbitrarily small diameter. This proves all of Ferry's movement estimates, not merely homotopy equivalence of fibres.
5. Obtain a PL map by replacing a polyhedral neighbourhood of the collapsed W with the abstract cone on its sphere boundary, and using linear cone extension of the height. A complete explicit height-preserving homeomorphism with the ordinary quotient is given. There is no assumption that the original collapse map is PL.
6. Obtain a smooth map independently using a smooth vector field V=beta(s)∂s+t∂t, with beta positive outside W and flat at its boundary. A suitable smooth Lyapunov neighbourhood has sphere boundary. Backward flow gives the exact local formula p(r,theta)=r h(theta), with h smooth and zero a regular value. Radial domain reparametrization r→g(r), flat at zero and identity near the outer boundary, makes p=g(r)h(theta) smooth, preserves the Hurewicz property by a domain homeomorphism, and has a unique critical point.
7. Put Sigma0=S1, Sigma1=E×I, Sigma01=E×∂I, target the whole-boundary embedding and source p on each component. There are no strict triples, and Sigma0 has no boundary. The manuscript properness, Hurewicz source and object-manifold hypotheses hold, but the fibre Y disjoint-union Y is not a manifold.

The proof is now complete. The C agent independently audited the PL cone, smooth flow and Ferry arguments and reported that they pass; his HEP simplification of the inverse-homotopy construction is incorporated. Every mathematical gate from the preliminary Chapman route has been replaced with a direct argument and an opened theorem.

## Opened sources and exact status

- **Used, primary full text:** E. C. Zeeman, *On the dunce hat*, Topology2(1964),341–358, printed p.347, passage before Theorem(5). It explicitly constructs the Mazur manifold and records the nonzero boundary fundamental group, with locator Mazur1961 p.227. Dotted M is boundary notation; visually inspected. https://webhomes.maths.ed.ac.uk/~v1ranick/papers/dunce001.pdf
- **Used, primary full text:** J. Milnor, *Lectures on the h-Cobordism Theorem*, Princeton1965, Theorem9.1 p.107, PropositionA pp.108–109; PDF zero-based pages111–113. https://webhomes.maths.ed.ac.uk/~v1ranick/papers/hcobord.pdf
- **Used, primary full text:** S. Ferry, *Strongly regular mappings with compact ANR fibers are Hurewicz fiberings*, PacificJMath75(1978),373–382, Definition p.373, Theorem1 pp.373–374. This is the exact theorem used for lifting. https://msp.org/pjm/1978/75-2/pjm-v75-n2-p07-s.pdf
- **Auxiliary only, book full text:** D. Rolfsen, *Knots and Links*, §11E pp.355–357, Exercise3 p.356; corrected AMS2003 scan visually inspected. The boundary group presentation is used solely for a finite nontrivial quotient certificate. https://webhomes.maths.ed.ac.uk/~v1ranick/papers/rolfsen.pdf
- **Opened, consulted, not used as a premise:** T. A. Chapman, *Piecewise linear fibrations*, PacificJMath128(1987),223–250, §2 p.227 item3. Its cylinder is simplicial, and the ordinary collapse of a codimension-zero W need not itself be PL. Direct application to our ordinary collapse was withdrawn. https://msp.org/pjm/1987/128-2/pjm-v128-n2-p02-s.pdf
- **Opened, consulted, not used as a premise:** M. M. Cohen, *Simplicial structures and transverse cellularity*, AnnMath85(1967),218–245, §4 p.225, §9 Props9.3–9.8 pp.238–240, Prop10.2' p.241. The simplicial/topological cylinder homeomorphism is not stated to preserve the required ordinary height, and standard extensions can add convex-cell fibres. We therefore avoided this route. https://webhomes.maths.ed.ac.uk/~v1ranick/papers/mcohen.pdf
- **Opened, corroboration only:** E. C. Zeeman, *A note on an example of Mazur*, AnnMath76(1962),235–236. https://www.lms.ac.uk/sites/default/files/1962%20A%20note%20on%20an%20example%20of%20Mazur.pdf
- **Opened abstract only, not used:** D. F. Addis, *A strong regularity condition on mappings*, GeneralTopologyAppl2(1972),199–213. Full-text fetch failed. Ferry provides the needed opened full theorem.
- **Original Mazur1961 full text not opened:** DOI10.2307/1970288; the bibliography/abstract was opened, JSTOR displayed no full text. No claim of opening that original article is made; the used primary source is Zeeman1964.

Fetched full copyrighted sources, OCRs and source screenshots under `references_B56/` are research scratch and must be excluded from the deliverable ZIP. Include our proofs, bibliographic locators, check events, scripts and outputs.

## Finite certificate

`code_B56/check_C5_boundary_group.py` and `.out` independently check the group presentation

    <x,y | y^5=x^7, y^4=x^2*y*x^2>

with permutations x=(0 1 2 3 4 5 6), y=(0 3 1 4 2). All 504 five-cycles are checked for fixed x; 14 solve the relation. The chosen pair generates A7, of order2520. Both relators are explicitly evaluated. UTC run2026-11-19T04:58:03.585352, runtime0.006783651seconds. This proves nontriviality of the recorded group; it does not replace geometric verification of a handle presentation.

## Other independent Part C checks

C1.03 simultaneous-cylinder formula originally omitted lower-prefix identifications. For I={0<1} and all Sigma spaces a point, the old transition families preserve max(e) and leave an isolated Sigma0 beside the interval. This was reported, acknowledged and corrected by the C agent using the additional maps C(d∩e_<a,e_≤a)→C(d,e) for every selected a∈d. A finite interval certificate is owned by the C agent.

For resolution, Albin2016 Theorem6.3(a–c), printed p.48, was opened and sent to C agent, together with the warning that collective boundary hypersurfaces retain disconnected links. ALMP2012 Props2.3 and2.7 use a minimal/connected-fibre collapse convention and cannot silently replace Albin's full collective statement in the nonnormal case.

## Follow-up original-source retrieval, 05:19–05:21 UTC

The exact original is Barry Mazur, *A note on some contractible 4-manifolds*, Annals of Mathematics73(1961)221–228, DOI <https://doi.org/10.2307/1970288>. Searches by full title, DOI and author-hosted location found its JSTOR record and Celebratio bibliography/abstract. The direct PDF <https://www.jstor.org/stable/pdf/1970288.pdf> and DOI redirect were inaccessible to the retrieval tool; the landing page exposed no paper text. **The Mazur original remains not opened.** Bibliographic metadata and a reproduced abstract are not treated as a full-text opening.

The primary E.C.Zeeman, *A Note on an Example of Mazur*, Annals76(1962)235–236, was fully opened at <https://www.lms.ac.uk/sites/default/files/1962%20A%20note%20on%20an%20example%20of%20Mazur.pdf>. Its p236 describes the handle construction and the untwisting after multiplication by an interval. It does not supply the boundary-group calculation, so it is contextual and is not an additional premise of the proof. The existence and auxiliary group claims continue to use the actually opened Zeeman1964p347 and Rolfsen11E.3p356, with their respective scope stated above.
