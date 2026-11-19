# Finite jets, fixed bundles, and the remaining actual-family problem

Root research, 19 November 2026, after checkpoint 14. This records an attempted route to the unrestricted characteristic-zero rational top quotient. It does not change a numbered theorem or the movement ledger.

Let E be a projective exceptional variety, L an ample conormal line bundle on E, and C a fixed smooth projective parameter curve over the coefficient field. If a vector bundle F0 on E×C is fixed, relative Serre vanishing for the projection to C gives

    H²(E×C, End(F0) ⊗ pr_E*L^n) = 0

for all sufficiently large n: all positive higher direct images vanish, and C has coherent cohomological dimension one. This removes the high-order deformation obstructions for that fixed restriction. The bound depends on F0. Moreover, pr_E*L is not ample on the entire product, so it would be incorrect to infer vanishing of every positive cohomology group on E×C; H¹ coming from C can remain.

The unresolved step is to represent the desired relative K0 classes by a compatible family with a fixed mod-E object and a controlled bound. An equality of vector-bundle classes in K0(E×C) does not imply a stable isomorphism of the bundles: exact-sequence relations need not split on a projective scheme. Finite detection of an endpoint class, or eventual constancy in a particular Adams weight, therefore does not by itself supply the compatible objects to which Grothendieck existence could be applied. We have not established that stronger representability statement. The already proved descent from an existing completed actual family remains available, but does not construct that family.

## Exact neighboring source checked

We freshly read the indexed primary author PDF of Ballico, Gasparim, and Köppe, *Local moduli of holomorphic bundles*, at https://sitios.ucn.cl/~etgasparim/Xjpaa2.pdf. The direct PDF opening timed out, and the publisher opening returned 403; a subsequent find/open against the indexed author source returned the actual text. We read Theorem 3.2, Lemmas 3.3–3.4 with their proofs, Theorem 3.5 with its proof (author pp. 3–4), and Remark 4.2 and Theorem 4.3 (pp. 5–6). These are text readings; no new local binary or visual inspection is claimed.

The filtrability/algebraicity argument in Section 3 explicitly concerns a curve as exceptional locus. Remark 4.2 formulates the obstruction groups for a fixed restricted bundle. The formal principle in Theorem 4.3 starts with an already existing formal locally free sheaf. None of these statements constructs the missing K0 family on the higher-dimensional product E×C. We use this source only to check the boundary of the attempted argument.

Published metadata was checked against the publisher's indexed primary record: Journal of Pure and Applied Algebra, 213(4), 397–408 (2009), DOI 10.1016/j.jpaa.2008.07.008. The exact locators above belong to the opened author version. No fresh opening of the Peternell originals cited there is claimed.

Searches included “K0 algebraization ample,” “K-theory formal completion ample,” “K-theory formal functions algebraization vector bundles,” and “vector bundles ample conormal algebraization.” They produced this neighboring curve theorem and the already scoped formal-functions inputs, without providing the required actual-family construction. Search failure is not a proof that no such theorem exists.

## Independent check of the constant-curve K2 limitation

We independently reconstructed the proof now preserved in `agents/frobenius/C3_top_characteristic_zero_lifting_RESEARCH.md`, Sections 3.1–3.4. For a proper smooth complex curve P and R=(C[t]_(t))^h, an actual K2(P_R) class descends to P×U for a pointed étale curve U. Compactifying U gives only disjoint vertical boundary curves. The localization boundary lies in K1(P); its determinant is a constant unit, so the relative-C logarithmic two-form has zero residue and extends holomorphically to the proper product. Rational Betti compatibility implies that the difference of its class and its complex conjugate is a divisor class. Hodge types (2,0), (0,2), and (1,1) then force the class to vanish; proper Hodge theory makes the form itself zero. This last step is not an assertion that exact forms vanish on an open surface.

We freshly opened the actual primary text of Asakura's 6 April 2006 v4 through the CiteSeer PDF mirror at https://citeseerx.ist.psu.edu/document?doi=61dbd9b70382036d04617d370ecd0a688b024b88&repid=rep1&type=pdf and read the complete introduction passage surrounding equation (1.1), p. 1. The direct arXiv opening failed; no root-local PDF download or image inspection is claimed. The owner independently obtained the original PDF and visually inspected that page, as its acquisition record states. Only the rational-Betti inclusion is used, not the conjectural equality that follows it.

The explicit first-jet differential d(epsilon) wedge dx/y on the constant elliptic curve y²=x³−x is nonzero. We checked the separate passage from the relative K2 sheaf to a rational global Quillen class: the one-dimensional descent spectral sequence has no H² obstruction. The owner explicitly records the already audited Goodwillie and Thomason–Trobaugh inputs; BEK's Milnor-sheaf formula alone would not justify this global passage. This rules out a blanket first-jet K2 algebraization principle. It neither constructs a top ordinary Chow class nor supplies the missing transfer from a K0 family on an exceptional resolution to this constant-curve K2 group. The unrestricted main gate is unchanged.
