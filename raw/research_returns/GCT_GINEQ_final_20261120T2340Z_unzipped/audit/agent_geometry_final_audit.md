# Actual final-draft geometry proof audit

Reviewer: GPT-6 Astra Pro, agent `/root/geometry_dictionary`. Reasoning-effort setting was not exposed. Completed 2026-11-20 23:32:31 UTC. This is a whole-proof mathematical model review, not formal verification or external refereeing.

## Reviewed checkpoint and scope

Read the complete statements, proofs, and immediate qualifications for F-15–F-22 directly in `deliverable/GCT_GINEQ.tex`. The checkpoint hash recorded at the start of this review was SHA256 `91a60a42b494ae2116937be659c5baa70322dd62cc06de0f431a67c59fa81f2a`. The parent may continue editing the draft; this review concerns the text actually read in this checkpoint, not uninspected subsequent revisions. Also read F-13's complete proof as a dependency of F-18, the crosswalk, the nonreduced-base qualification, and the relevant bibliographic entries. No main TeX edits were made.

| Finding | Result | Entire-proof checks |
|---|---|---|
| F-15 | PASS | Coordinate image embeds in the source polynomial domain and is torsion-free over Z; torsion-free Z-modules are flat. Flat base change to C preserves the defining kernel. The complex scheme image is the affine closure of sums; polynomial identities remain identities under any ring substitution. The nonflat reduction caveat is explicitly retained. |
| F-16 | PASS | Contraction and exterior multiplication define the natural bundle map and commute with base change. For universal atom parameters the rational rank bound makes every specified integral minor the zero polynomial, hence the identities hold integrally and after all base changes. The Fitting index is target-rank minus minor-size, namely f−s−1. |
| F-17 | PASS | Nondegeneracy and r≤dim V give a nonempty independent-point open; integrality gives its density. The graph closure is projective and its tautological projective bundle has the stated dense open. The proper image is exactly the secant closure. Retaining the limiting plane avoids the incorrect claim that an arbitrary limiting scheme necessarily spans that whole plane. |
| F-18 | PASS | The line-to-universal-quotient zero locus is closed; its projection from a product with the projective secant is proper. F-13's fixed independent columns give q-planes converging to the actual image; the larger pure-atom span, basis selection, and dimension intersection give membership of every approximating q-plane in the same incidence locus. Closedness passes to the limit. |
| F-19 | PASS | Homogeneity contradicts full-GL norm invariance. The diagonal family lies in one product-GL orbit; the Hilbert, injective, and projective norms are exactly those stated, including the dual lower certificate for the projective norm. The ratios therefore vary while rank/orbit data remain fixed. |
| F-20 | PASS | Zero and identity have equal source/target classes and equal virtual complex class but different ranks. Equality of the inputs forces equality of every lambda/gamma expression in them. The z·id family and nonsplit additive-group extension supply the announced degeneration and extension examples without claiming a general K-theory impossibility theorem. |
| F-21 | PASS | Both rational points are abstractly Spec F_q, with constant Q_l stalk and H^0 carrying Frobenius eigenvalue one, weight zero, and the unit point motive. Their ambient tensor ranks differ. The hypothesis l≠char F_q and the restriction to these specified invariants are explicit. |
| F-22 | PASS | Normalized squarefree degree-n symmetric coefficient tensors require the 1/n! coefficients. The coproduct defines the integral divided-power-domain Hasse matrix. Nonzero determinant/permanent columns are complementary minors/permanents; different row-column complements have disjoint supports with primitive coefficients, giving a free image of rank binomial(n,k)^2 over every field. The pure-power coproduct has outer-product rank ≤1, including possible vanishing in small characteristic. The polynomial-power versus complete Veronese distinction is explicitly retained. |

The relative image-Grassmannian qualification at the end of the crosswalk is correct: use the actual determinantal rank-q stratum, with vanishing (q+1)-minors and locally invertible q-minors. Fiberwise constant rank alone is not substituted for this condition over a nonreduced base.

## Historical/archival crosswalk audit

All printed-page and one-based scan-leaf entries in the present table agree with the independently recorded original scans in `work/agent_geometry.md`: Résumé p.8/leaf8, p.8′/leaf9, pp.59–62/leaves60–63; EGA I pp.176–177/leaves175–176; SGA3 p.29/leaf42; SGA6 pp.314–317/leaves321–324 and p.325/leaf332, p.331/leaf338; FGA pp.259–260/leaves12–13 and pp.265–266/leaves18–19; Weil II p.153/leaf17. The published-work identifier CSG17 is correctly distinguished from an unpublished-manuscript shelfmark. The 1953/1956 catalogue discrepancy is correctly left unexplained rather than turned into an invented chronology.

The SGA4 VII §1.2 reference is an exact internal textual locator, not a claim to a verified original scan leaf. No nonexistent SGA5 rank theorem is cited.

### Additional verified EGA II anchor for incidence

The incidence dictionary can be strengthened by adding a primary properness locator:

- EGA II, Definition 5.4.1 and Proposition 5.4.2, printed p.100, original PDF zero-based index96 / one-based leaf97.
- EGA II, Theorem 5.5.3(i), printed p.104, original PDF zero-based index100 / one-based leaf101: projective morphisms are proper.
- NUMDAM publication identifier `PMIHES_1961__8__5_0`, DOI `10.1007/BF02699291`.
- Official catalogue: https://www.numdam.org/item/PMIHES_1961__8__5_0/
- Original scan: https://www.numdam.org/article/PMIHES_1961__8__5_0.pdf

Both original pages were visually inspected during this final-draft review. This is a published-source archive identifier and scan, not a manuscript cote. Suggested table key: `EGA-proper`; use it in the F-13/F-14/F-18 row and in a new F-23 coordinate-restriction row if adopted. No existing proof requires correction to add this citation.

## Changes and limitations

No proof correction is required for F-15–F-22 in the reviewed checkpoint. The only suggested addition is the verified EGA II properness anchor. An optional later coordinate-restriction finding needs its own proof-check events and crosswalk; it is not silently covered by these eight events. The unpublished-cote question is being researched separately and does not affect any mathematical proof above.

## Later final-draft F-23 audit

At 2026-11-20 23:35:28 UTC I read F-23's entire statement, proof, and adjacent scope qualifications directly in the updated draft, checkpoint SHA256 `4f8853bf84c1ee0dee03a2d52f1d2932375942f43232b8a4f3dd739196fd817b`. Result: **PASS**. A nonzero residual coefficient is isolated by the indicated coordinate projection for both row and both polynomial families; every other same-size support is annihilated. Products of linear maps preserve atoms or zero and border closures. Split inclusion gives an attaining residual generator of exactly the smaller border rank. F-13 then gives the recursion, and the b=2 bilinear matrices have rank4. The fixed-field and CP-versus-symmetric qualifications are correct.

The arithmetic consequences of the adjacent external inputs are correct (100+17−1=116, 400+17−1=416, and the corresponding16 inputs give115 and415). This F-23 proof review does not claim to have re-proved or fully audited the cited external CP equalities17 and16; those are literature inputs being verified separately by the parent/team.
