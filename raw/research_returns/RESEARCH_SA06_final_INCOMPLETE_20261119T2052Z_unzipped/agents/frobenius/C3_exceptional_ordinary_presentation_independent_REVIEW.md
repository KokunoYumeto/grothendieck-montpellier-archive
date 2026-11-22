# Independent audit of the exceptional ordinary-quotient presentation

Reviewer: GPT-6 Astra (OpenAI), ChatGPT Pro, run RESEARCH_SA06, agent `/root/frobenius`; inherited effort not separately exposed.

Full typed file read at the 16:56:36 UTC tool-clock reading, 19 November 2026: `../real_weil/C3_exceptional_ordinary_presentation_draft.tex`, equations EP.1–EP.4 and all four proof steps.

**Verdict: PASS.** This is an exact comparison theorem under the hypotheses of the separately audited endpoint theorem EL. It is not a computation of the exceptional quotient in general and does not imply unrestricted top Chow vanishing.

1. FF.4 is an actual lambda-compatible restriction isomorphism after rationalization. On the projective exceptional surface the third gamma filtration is zero. The operation `(psi²-1)(psi²-2)/6` has values zero, zero, one on the eigenvalues 1, 2, 4, respectively. The filtration and distinct roots therefore identify its image precisely with filtration two. The finite-type smooth-model Chern-character argument identifies this space with CH² of the regular resolution.

2. The nilpotent pullback on the exceptional product is a rational lambda-ring isomorphism. Its inverse preserves rank and gamma filtration, either from the universal operations or by lifting their finite rank-zero expressions after clearing denominators. EL applies to the resulting class on D times P and produces an actual perfect family with exactly its two endpoint restrictions. FF.4 forces the endpoint classes to have pure weight two. Taking ch₂ then gives an ordinary cycle relation on the fixed product. This proves the first inclusion without asserting a lift of the original full exceptional family.

3. Conversely an actual codimension-two cycle family on the regular product has an inverse rational Chern character with only its degree-two component nonzero, on a single smooth finite-type model. Its pullback is a pure-weight-two perfect family. Restriction to the exceptional product preserves filtration two and supplies the claimed relation. Compactifying a smooth curve parameter and closing horizontal cycle components is legitimate on the fixed regular product, or on its fixed finite-type model before pullback; it does not require extending a vector bundle across a singular parameter product.

4. Chow localization is surjective, and the ordinary relation subgroup on the puncture is the image of that on the resolution. The reverse inclusion follows by closing the finitely many cycle components of a fixed-product family and then taking refined endpoint fibres; vertical terms do not alter its restriction to the original family. Consequently the displayed quotient by the exceptional cycle image is exact. The theta map correctly retains the actual embedding of the exceptional divisor in the resolution.

The fresh Weibel II source read is recorded in `C3_endpoint_family_lifting_independent_REVIEW.md`: Chapter II, Proposition 4.9, Splitting Principle 8.8.1, Corollary 8.8.2, Remark 8.8.5, and the following Chern-character discussion. This audit reuses the previously fully opened FF/EL/GH/Drinfeld and smooth Chern-character inputs; it does not claim a new original SGA6 reading, program rerun, or separate computational certificate. No unregistered statement identifier is inserted into the master event catalog.
