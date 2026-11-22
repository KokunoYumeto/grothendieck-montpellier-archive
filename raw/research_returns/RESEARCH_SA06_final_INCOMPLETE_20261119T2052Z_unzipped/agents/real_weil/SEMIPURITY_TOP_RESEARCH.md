# Semipurity and the residual top ordinary quotient

Research record by `/root/real_weil`, GPT-6 Astra in the current OpenAI team run, 19 November 2026, 15:27–15:41 UTC. This is an unnumbered investigation. It proves no new range statement and records no main-gate movement.

## 1. The source actually inspected

Weber, A. (2012). Purity of boundaries of open complex varieties. *Journal of Singularities, 4*, 171–179. https://doi.org/10.5427/jsing.2012.4j . The full nine-page primary journal PDF was opened and its Proposition 3, Theorems 11–14, Remarks 13 and 16, and the complete Section 7 proof were read: <https://www.journalofsing.org/volume4/weber.pdf>. Exact fresh retrievals include `turn463263277view0` and `turn265769872view0`. The existing bibliography key is `rootWeber2012BoundaryPurity`; no duplicate entry is needed.

Theorem 11(iii), printed p.176, gives purity in degree k at least dim(U)+s, where s is the dimension of the singularity locus of the compactified pair. Remark 13, p.177, explicitly localizes the assertion at an end. For an isolated N-dimensional complex singularity, this applies to the exceptional boundary in degrees k at least N. Proposition 3 identifies its lower-weight boundary and link contributions. These are statements about rational mixed Hodge structures. They do not identify Chow kernels or construct actual proper-parameter families on the resolution.

The author's separate `purend.pdf` URL returned403 in this investigation. The arXiv abstract page for *Purity at the end*, 0809.1885v3, was opened and verifies the version date6 September2009; direct opening of that version's PDF failed. No theorem from its unopened full text is used. The full 2012 journal text suffices for the exact purity statements above.

## 2. The degree in which the tetrahedral candidate lives

In local dimension N=3, semipurity begins with H³(E). A dual complex homeomorphic to S² can still give a weight-zero contribution to H²(E). Thus the prospective tetrahedral exceptional boundary is not excluded merely by the published purity bound.

The parent's proposed hypersurface with leading term xyzw and a degree-five correction has not been promoted to a counterexample. At the candidate blow-up, the triple vertices are smooth if the correction is nonzero there; zeros on double edges produce the local equation uv=tau w. A globally compatible regular projective resolution and all its intersection maps are still required. The geometry is recorded separately in `../../notes/ROOT_TOP_SEMIPURITY_RESEARCH.md`.

The numerical degree-unit edge obstruction has a different status. The previously written exact weighted-square identity in `../frobenius/C3_SNC_energy_lemma.tex` kills that edge quotient when a positive exceptional combination has negative ample restriction. It does not kill a dual-S² coefficient term or prove an actual-family theorem. This is the same identity now independently encountered in the parent's semipurity investigation, not a new numbered result.

## 3. Ordinary K-theory, homotopy K-theory, and a coefficient class

The distinction between K and KH is material here. In characteristic p, the closed-union excision used in C.3bc follows after inverting p from Geisser–Hesselholt's nilpotent/birelative comparison. In characteristic zero, one cannot import that argument for ordinary K-theory. The automatic SNC descent calculation is a calculation in KH or cdh motivic cohomology; a comparison to actual K₀(E) must be supplied separately.

The local primary text of Burke–Popa–Shen (2026), `../frobenius/sources/burke_popa_shen2026_negativeK.pdf` and its extracted text, was reread in Section3, pp16–17, and Sections8–9, pp25–31. Section3 explicitly distinguishes K from KH and gives the hyperresolution spectral sequence (3.13). Lemmas8.2–8.4 handle the point K₂ and curve K₁ terms under their stated weight hypotheses. Theorem9.1 imposes projectivity and isolated klt-type singularities, or rational singularities with its additional Bloch-conjectural input. Neither arbitrary strict localization nor arbitrary exceptional ordinary families is a conclusion of that theorem.

Suppose an abstract blow-up square with regular Z and closed residue field k is in a setting where KH descent is available. Its K(k)-linear exact sequence contains

    KH₀(Z) ⊕ KH₀(k) → KH₀(E) → KH₋₁(R),

and its negative segment identifies KH₋₂(E) with KH₋₃(R), since the negative groups of regular Z and k vanish. For κ in KH₋₂(E) and u in K₂(k), the connecting image of uκ is exactly u times the connecting image of κ. Consequently, knowing that κ maps nontrivially does not establish either vanishing or injectivity for multiplication by u. One must compute that module action.

A splitting of a constant dual-complex summand in KH(E) alone is insufficient. Even if the exceptional configuration is defined over Fpbar and has rational Tate strata, newly arising classes on the strict-local resolution after extension to k need not be K(k)-linear base changes of classes over Fpbar. There is no established equality

    KH(Z_k) = KH(Z_Fpbar) tensor over K(Fpbar) K(k)

in this situation. C.3y's strict-local divisor quotient already warns against assuming such base-field invariance. Thus the connectiveness of KH(Z_Fpbar)_Q cannot by itself prove that the prospective K₂(k) coefficient has injective negative-K boundary over k. A compatible splitting of the local descent triangle, or another direct proof of the module action, is still missing.

## 4. Why a bare field K₂ term is not an ordinary invariant

The complete integral proper-curve symbol lemma in `TOP_QUOTIENT_RESEARCH.md` Section2 remains applicable in every characteristic. For each Milnor symbol u={a,b}, it constructs a smooth proper connected curve P, points p,q and an actual ξ in K₂(P) with ξ_p−ξ_q=u. The explicit curve equation, tame-residue checks and Quillen localization/Gersten locators are retained there. Multiplying ξ by a fixed class κ gives an actual proper-parameter KH₀ relation on E whenever the proposed coefficient is the product uκ.

This rules out the assertion that the field coefficient itself is constant on proper curves. It does not prove a relation on Z. The exact remaining requirements are:

1. The coefficient class must lie in the image of K₀(Z), not just in a graded term of KH₀(E).
2. Its proper-parameter KH relation must have an appropriate ordinary-K representative when that comparison is needed.
3. The relation must lift to an actual perfect complex or Chow class on the fixed product Z×P with the prescribed endpoints.

The actual-family completion-descent lemma already proved in `TOP_QUOTIENT_RESEARCH.md` Section7 solves descent from the completion once such an actual completed family exists. It does not construct a compatible family on all exceptional thickenings, and finite-level K₀ detection does not supply that construction.

## 5. Current scope of the remaining top case

The general characteristic-zero smooth-surface case still has the separate absolute-differential/actual-family issue, even with no SNC gluing. The specific Fermat quintic is already settled by C.3au, which uses its degree-five correspondence from a blown-up product of curves. It must not be listed as an unresolved example. An arbitrary or generic irregularity-zero quintic is outside that special construction.

Over Fpbar, C.3be is already stronger than the resolution-specific discussion: the certified finite-semilocal-normalization argument proves the stated rational one-cycle vanishing for every excellent local domain with residue Fpbar, including mixed characteristic and without a henselianity assumption. Nothing in this note narrows that completed theorem.

No new vanishing, counterexample, universal range, or finite-dimensionality assertion follows from the present semipurity or tetrahedral analysis. The exact next question is the image and actual-family behavior of the top coefficient summand in the local descent triangle, rather than cohomological purity alone.

## 6. An exact primary affine tetrahedron calculation

Dayton, B. H., and Weibel, C. A. (1980). K-theory of hyperplanes. *Transactions of the American Mathematical Society, 257*(1),119–141. https://doi.org/10.1090/S0002-9947-1980-0549158-6 . The complete published scan was opened at <https://sites.math.rutgers.edu/~weibel/archive/papers-dir/DaytonWeibel-1980.pdf>. The introduction's admissibility hypotheses, pp119–120, and Theorem5.2 with its proof, Corollaries5.3–5.4, and Assertion5.5 with its proof sketch, pp136–137, were read directly. Exact new bibliography entry: `D_DaytonWeibel1980Hyperplanes` in `SEMIPURITY_references.bib`.

For the union of four affine planes in general position in affine three-space, Corollary5.4 gives actual K₀ equal to K₀(k) direct sum K₂(k); the coefficient ring is assumed regular. Assertion5.5 describes the corresponding graded Karoubi–Villamayor module/ring structure. Thus the K₂ coefficient is a rigorous ordinary-K phenomenon for this exact affine model, also in characteristic zero. The complement of a general hyperplane in the unmodified projective coordinate tetrahedron is such an affine arrangement. The theorem does not compute the modified projective exceptional divisor or its restriction map from the regular local resolution. It supplies no missing actual-family lift on that resolution.

The two primary PDFs and extracted texts are retained under `sources/weber2012_boundary_purity.*` and `sources/dayton_weibel1980_hyperplanes.*`. Acquisition source is `code/fetch_semipurity_sources.py`, full output the matching `.out`, and exact times/hashes `output/semipurity_sources_manifest.json`. The run began15:47:37.086468UTC and finished15:47:48.473957UTC, taking11.387489030996221seconds. This was source acquisition only, not a mathematical certificate.

## 7. A concrete coherent calculation, conditional on the proposed resolution

Assume that the small-resolution construction does produce the specified SNC surface E with four components E_i, each a blow-up of the corresponding coordinate P² at finitely many nonvertex edge points. Assume its double curves remain the strict transforms of the six coordinate lines, its triple points remain the four vertices, and its Cartier conormal L restricts to the pullback of O(1) on each component. These are hypotheses of the following calculation, not a certification of the outstanding global resolution construction.

For n>0, H²(E_i,Ω¹_Ei tensor L_i^n)=0. Indeed, Serre duality on the smooth surface identifies the dual with H⁰(E_i,Ω¹_Ei tensor L_i^(−n)). On the complement of the finitely many blow-up centres, such a section is a section of Ω¹_P²(−n). It extends across those codimension-two points because that bundle is locally free, and the Euler sequence makes its global section space zero. Also H¹(P¹,Ω¹_P¹(n))=H¹(P¹,O(n−2))=0 for n>0.

The local SNC differential calculation gives the exact sequence

    0 → Ω¹_E/torsion → direct-sum Ω¹_Ei → direct-sum Ω¹_Dij → 0.

At a triple point this is checked separately in k[x,y,z]/(xyz): compatible coefficients on the coordinate planes lift coefficient by coefficient, and the restrictions of a one-form along the two coordinate axes in each plane can be independently prescribed. The torsion sheaf is supported in dimension at most one. The preceding vanishings therefore give H²(E,Ω¹_E tensor L^n)=0.

The normalization complex for O_E tensor L^n has the same global-section complex as that for the unmodified coordinate boundary, since the line bundles on the blown-up components are pulled back and the edges/vertices are unchanged. Its higher component cohomology vanishes for n>0. Hence H¹(E,L^n)=H²(E,L^n)=0; equivalently these vanishings follow on the original boundary from its degree-four hypersurface exact sequence in P³. The conormal differential map L→Ω¹_Z|E is injective: locally E is a reduced product of distinct regular parameters in regular Z, and their gradient has zero annihilator in O_E. Its cokernel is Ω¹_E. Consequently H²(E,Ω¹_Z|E tensor L^n)=0 as well.

This calculation removes specified coherent groups; it does not algebraize a virtual K₀ system. A family over a proper curve P has closed-fibre dimension three, so the top-on-E weight-two complex still has possible degree-three terms. Rational nilinvariance at one detecting finite thickening gives no automatic actual perfect representative on Z×P, and no one bounded p-power denominator has been produced. An exact perfect-family lifting theorem or a direct cycle construction is still required.

## 8. Dated supersession after checkpoint18: geometry, spectrum, and point lifting

The earlier conditional descriptions in Sections2–3 and7 record the state before the following completed checks. They must not be read as the current scope. The ordered tetrahedral resolution is now completely proved in `../frobenius/C3_tetrahedral_resolution.tex`, TG.1–TG.5, and independently checked in `C3_tetrahedral_resolution_independent_REVIEW.md` and the parent's full receipt. The resolved exceptional surface has components Bl15, Bl10, Bl5 and P², six unchanged projective-line double curves, four triple vertices and no quadruple point. Its actual conormal is the pullback of O(1), which is nef rather than ample. A separate positive exceptional combination has negative relatively ample line bundle. The retained36-check finite program/output was inspected in full without a second run. Thus the geometric hypotheses of Section7 are now supplied by this exact example.

The audited unnumbered auxiliary `C3_tetrahedral_K_spectrum.tex`, TS.1–TS.4, compares the entire natural restriction diagram under external products before choosing any cellular basis. Ordinary K-theory closed-union descent after inverting p and the rational finite-field calculation give, for every indicated Noetherian parameter product, the natural external-product equivalence and a fixed noncanonical splitting

    K(E₀×P)_Q ≃ K(P)_Q^33 ⊕ Σ^(−2)K(P)_Q.

The finite rational complex has Picard rank34 mapping surjectively onto six edge degrees; its remaining degree-zero dimension is33 and its sole negative term is Q in degree−2. The κ·K₂(P) coefficient is therefore an actual ordinary-K summand compatible with parameter evaluation, not merely a graded KH class. Root and both peers completed full proof/source checks. The former draft is a supersession pointer; no new numbered theorem or main-range movement is registered.

The point-lifting question is now settled by a separate exact primary theorem. Drinfeld, arXiv math/0309155v4 (11October2004), Theorem3.7 and Remark(ii), authorp8, proves K₋₁(R)=0 for every commutative henselian local ring. The complete proof, including finite-algebra factorization and idempotent lifting, was directly read by the owner, root and Frobenius. The fixed-product KST/GH exact sequence in `../frobenius/C3_fixed_family_negative_K.tex`, combined with K₀(R)=K₀(k)=Z, consequently gives

    K₀(Z)[1/p] ≅ K₀(E)[1/p]

for the henselian point parameter. In particular every individual κ·u lifts, and its negative-K boundary is forced to vanish. The prospective point-faithfulness approach in Section3 is thereby excluded, rather than remaining an open possible route.

For a fixed smooth proper parameter curve P, however, SpecR×P is not a henselian local scheme. The exact residual cokernel remains

    coker[K₀(Z×P)[1/p] → K₀(E×P)[1/p]] ≅ K₋₁(SpecR×P)[1/p].

Neither Drinfeld's local theorem nor the external-product splitting computes this group or lifts the actual proper-curve K₂ relation. Clausen–Mathew–Morrow's published2021 introduction, p414, was freshly read and expressly leaves negative K and general smooth proper henselian schemes outside its rigidity comparison; it supplies no shortcut here. The ordinary rational top Chow quotient therefore remains unresolved by this calculation.

Exact new source record: `SEMIPURITY_references.bib` uses chapter-specific `D_Weibel2013KbookIV`, whose opened URL is the full ChapterIV PDF, for Corollary1.13p10 and Example2.6p20. The existing `frDrinfeld2004Tate` key is reused from Frobenius's fixed-family bibliography. Quillen1972 original publisher metadata was obtained, but its original proof was not freshly opened; the finite-field theorem is used through the directly read K-book statement. The full fixed-family independent audit is `C3_fixed_family_negative_K_independent_REVIEW.md`.

## 9. Audited endpoint resolution of the tetrahedral example, 2026-11-19T16:59:39.474217+00:00

This dated result supersedes Section8’s open ordinary-quotient wording for the exact tetrahedral construction. `C3_tetrahedral_raw_Chow.tex` proves CH2(X)_Q=K2(k)_Q. The fully audited `C3_endpoint_family_lifting.tex` now realizes every proper-curve symbol difference by an actual fixed-product cycle family on Z, using perfect gamma-two degeneracy representatives, regular supporting hypersurfaces, one finite p-power Picard lift, and exact finite endpoint identities. Consequently B2(X)_Q=0 for this tetrahedral family over every algebraically closed field of positive characteristic. The prescribed whole K0 family may still have a nonzero FF boundary; only its endpoints are lifted.

The separately audited `C3_exceptional_ordinary_presentation.tex` gives the general comparison under its regular-threefold/SNC/positive-D hypotheses: B2(X)_Q is Fgamma2 K0(E)_Q modulo actual proper-product perfect-family endpoint relations and the exceptional CH1 image. Both relation-group inclusions and localization are proved. Thus ambient endpoint lifting is removed in this exact scope. Computing the exceptional-family quotient is still substantive: separately moving edge SK1 generators can leave nonzero K1(P) restrictions at triple strata, so they cannot be silently treated as global E×P families. No general finiteness or higher-dimensional vanishing is inferred.

## 10. Finalized all-dimensional comparison and intrinsic source audit,17:43UTC

C.3bm supplies the general algebraizable positive-characteristic threefold geometry, and finalized C.3bn (`C3_all_dimension_endpoint.tex`) proves the endpoint comparison in every stated resolved dimension, with arbitrary reduced exceptional support. Earlier general ambient-lifting questions in this note are superseded in precisely those scopes. Neither theorem computes the remaining intrinsic exceptional quotient or asserts arbitrary-dimensional resolution existence.

`INTRINSIC_TOP_SOURCE_SCOPE.md` now records fresh primary readings of Binda–Krishna2022 Theorems8.3–8.4, Kohrita1512.02320v3 Definition2.3/Proposition2.10/Remark3.16, and the explicitly limited read of Levine2609.32599v1. The distinction between rational equivalence, arbitrary smooth-parameter motivic algebraic parts, and our proper-perfect-family relation is retained. In particular, Kohrita's reduction from semiabelian to abelian parameters in the classical smooth proper case uses ordinary Chow localization surjectivity; it is not an automatic theorem for singular exceptional perfect classes. No additional universal vanishing follows from these sources.
