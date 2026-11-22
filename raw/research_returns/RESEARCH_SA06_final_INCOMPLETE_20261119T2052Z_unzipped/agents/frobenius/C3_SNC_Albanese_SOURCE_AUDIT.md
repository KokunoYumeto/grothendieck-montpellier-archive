# Weighted exceptional Albanese matrix: source and proof record

**Scope:** finalized C.3bo, with root and both peer full proof/source passes. No quotient-vanishing claim or priority claim.

The complete proof is in C3_SNC_Albanese_matrix.tex, equations AM.1–AM.9. It uses the geometry and exact ordinary/perfect-family comparison of C.3bm and EP. Its additional conclusion is that actual exceptional Picard families remove every component Albanese coordinate, so the residual quotient can be represented by componentwise degree-zero Albanese-kernel classes.

## Exact sign source newly opened and read

Milne, J. S. (2021, June 12). *Jacobian varieties* (corrected author version of the 1986 chapter in *Arithmetic geometry*, pp.167–212). https://www.jmilne.org/math/xnotes/JVs.pdf

The complete official 50-page PDF was opened. Proposition6.1 and proof, authorpp19–20, and Lemma6.9 with full proof and Remark6.10(c), authorp23, were read. PDFp23 was also visually inspected. The current author's title page dates this version12June2021 and says the original numbering is unchanged.

The exact lemma says that minus the pullback map f^vee is inverse to the theta polarization. Thus f*lambda=-id, and the canonical Albanese map into Pic0(C)^vee is -lambda composed with the usual degree-zero divisor Abel map. This gives the minus sign in the intersection homomorphism.

The existing bibliography key D_MilneJacobians2021 is reused. Its prior note records different opened pages; this source ledger records the additional fresh exact locators without silently claiming that the old note already contained them.

Primary refs in this run: turn325903584view0 (fullPDF), turn751702673view0/1 (exact§6), turn827226539view0 (p23screenshot).

Local PDF: sources/Milne_Jacobians2021.pdf,532382bytes,SHA25636c3f09c7462dbbd4ae1f8b81a02bd9ff84f03c5a346351d7d5d78fc3f173486.
Rendered page: sources/Milne_Jacobians2021_p23.png.
The initial www-URL direct downloader returned406. A fresh non-www request with a browser User-Agent succeeded in12.826459382995381s; this is an acquisition time, not a proof/computation runtime.

## Other primary sources freshly reread

- Stacks Project, Lemma30.17.2, Tag0B5V, full statement and proof, https://stacks.math.columbia.edu/tag/0B5V . We use only its forward finite-pullback-ampleness implication, after restricting the target to the closed image. Existing key frC3beStacksFiniteAmple.
- Stacks Project, Lemma30.17.1, Section30.17 Tag01XO, full statement and proof, https://stacks.math.columbia.edu/tag/01XO . Serre vanishing applied to omega_V tensor H^n, combined with surface Serre duality, yields H1(H^-n)=0. Existing key frC3azStacksSerre.
- Stacks Project, Lemma45.8.3, Tag0FH7, **the prescribed-point Bertini argument in its proof**, https://stacks.math.columbia.edu/tag/0FH7 . The formal statement concerns divisibility; its proof supplies the exact smooth connected curve through two points used here. Existing key frC3azStacksBertini.

The canonical Picard/Albanese duality and normalized Poincare family on a smooth projective variety with a k-point are the same previously used Picard-scheme inputs. No new nonreduced Picard representability theorem is asserted. All Picard varieties in the matrix are the reduced connected abelian varieties.

## Independent proof details

For an ample H on a surface, a sufficiently high smooth curve C in |H^n| has tangent-injective Picard restriction by H1(H^-n)=0. Hence the restriction of the reduced Picard variety has finite kernel. Pulling the canonical theta polarization back proves that n times the negative intersection-to-Albanese homomorphism is a polarization. This avoids assuming a characteristic-p full-Picard Lefschetz isomorphism.

For the exceptional matrix Lambda, the diagonal is minus mu_Ni and the off-diagonal is minus r_i^vee lambda_C r_j. After multiplication on both sides by diag[a_i], the exact identity AM.8 is a sum of positive ample diagonal terms and difference-map theta pullbacks. Multiplying by a common positive integer realizes this as one actual theta-product pullback under a finite-kernel map. Hence Lambda is an isogeny in all characteristics.

The Picard inputs have actual Poincare families on fixed E_i times a proper curve. Push these cycles into the fixed regular Z product, then use EP.3. Thus theta(Pic0) already lies in J_K, rather than merely in an abstract exceptional subgroup. This is essential to the denominator splitting in AM.4.

## Computation and build

The initial standalone LuaLaTeX build started17:39:12.254322UTC and finished17:39:16.969269UTC; elapsed4.71488980200229s. All five passes returned0,3pages131754bytes, no warnings. Program code/build_SNC_Albanese_matrix.py and full output/JSON are retained. This build is of the proposed unnumbered draft, not of a final master integration.

The cycles agent independently read the complete AM.1–9 and the exact primary pages, including the local p23image, and sent a full PASS at17:39–17:40. The peer's own formal receipt is separate. No source or computation rerun is attributed to that peer beyond its explicit report.

## Remaining mathematical limitation

The argument does not kill Albanese-kernel zero-cycles on an exceptional surface, or prove that their proper parameter families glue across the SNC double curves. Pointwise surjectivity of a semiabelian extension cannot be used in place of those actual families. The specific two-component fixed-node model is covered by the separate cycles lemma FN.1–7; its compatible-family construction is not extended to arbitrary SNC surfaces.


## Final certification and clean final-path build

Root full proof/source PASS at17:40:42UTC (the earlier rounded17:41 wording was explicitly corrected against the tool clock). Cycles full PASS17:39:51UTC; real_weil full PASS17:41:29UTC. Final promotion preserves the audited draft under output and makes the former draft path a pointer. The existing Milne bibliography note was updated by its owner with the freshly read exact §6 locators.

Final-path build started17:43:07.396902UTC, finished17:43:11.808744UTC,4.411783577001188s, five commands returned0,3pages132365bytes, warnings empty. Final source SHA25600129cadee03abe37622eef744745efeb5d5ac99411ed63d39912198c2057382. The builder reads current owner bibliography entries, not a stale generated aggregate.
