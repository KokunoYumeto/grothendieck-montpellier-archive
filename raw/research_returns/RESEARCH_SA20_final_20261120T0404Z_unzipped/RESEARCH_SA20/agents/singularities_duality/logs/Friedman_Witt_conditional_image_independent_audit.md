# Independent literal audit: conditional Friedman--Witt implication

Auditor: singularities_duality. Date: 2026-11-20, after observed 03:27:06 UTC.

Candidate read in full (169 lines):
`agents/higher_comparison/logs/Friedman_Witt_conditional_image_scope_20261120.tex`.
SHA256: `0cf95bcaf665a6f48149c5081ba8ad5c3022189caeeef6403295d70e2c3c8a31`.

**Verdict: PASS as a conditional scope implication.** It does not evaluate the PL image or any concordance component group.

The single-map smoothing step is correctly relative only to a bottom collar. The compressed PL map G pulls the fixed product smoothing back to a second compatible smoothing on the same PL four-manifold. The two reductions agree near the bottom. The vanishing of the homotopy groups of PL/O through degree six supplies their relative stable concordance. The actual DIFF-subset-PL product and isotopy theorem has no dimension restriction, and its relative-open-set version gives an isomorphism to the pulled-back smoothing which is PL-isotopic to the identity near the bottom. Composing with G gives a smooth concordance. Its top map need only be TOP-isotopic to the original PL top map; the proof does not claim that this original map is smooth.

The conclusion uses no projection-preserving smoothing of a four-dimensional isotopy. It is existence for one supplied PL map. The ordinary Diff-to-TOP comparison on the closed three-dimensional top boundary then replaces the resulting smooth endpoint by the specified smooth endpoint through a smooth isotopy. Concatenation with product collars gives the required exact smooth pseudo-isotopy endpoint.

A.145 is applied to the punctured finite-fundamental-group prime summands. Their supported classes span the connected sum's H^2 with mod-two coefficients. The proof does not incorrectly assert that the connected sum itself has finite fundamental group. The correcting TOP concordance R has literal identity top and bottom; hence F R^{-1} retains the exact endpoint f while cancelling c_B. Assuming the stated kernel-image equality, a TOP component path to a PL concordance then gives the endpoint TOP isotopy needed in the single-map argument.

The source scopes match the prior independent Quinn audit in
`agents/singularities_duality/logs/Quinn_single_PL_concordance_smoothing_audit.md`:
Quinn 2010 Definition2.1/Theorem2.2 pp.304--305 and Notes2.3(2),(5), p.305. No stronger smooth/PL family comparison is inferred. The candidate's Cerf closed-three-manifold component comparison is the already audited ordinary comparison used in A.162. The precise relation to the cited Friedman--Witt/Kwasik--Schultz examples is conditional throughout.

No correction requested. No original-task completion, main-gate reduction, or review movement is claimed by this note.
