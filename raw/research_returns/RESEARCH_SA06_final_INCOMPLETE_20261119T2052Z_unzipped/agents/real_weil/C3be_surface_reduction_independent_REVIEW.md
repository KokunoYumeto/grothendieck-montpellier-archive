# C.3be: independent proof and source audit

**Outcome: PASS of the complete strengthened draft.**

Actual certification clock: **2026-11-19 12:54:25 UTC**.

Reviewer: GPT-6 Astra (OpenAI), ChatGPT Pro mode, run RESEARCH_SA06, agent `/root/real_weil`; inherited effort setting not separately exposed. This is an independent targeted proof and primary-source audit. It is not an independent re-proof of the cited surface-resolution or K-theoretic descent theorems.

Full mathematical file read: `research/agents/frobenius/C3_surface_reduction_Fpbar_draft.tex`, strengthened version beginning with an arbitrary excellent henselian local domain. The earlier algebraizable-only draft is superseded and retained by the owner under `output/C3_surface_reduction_Fpbar_algebraizable_initial.tex`. The old finite-model argument is not required for this stronger proof.

## 1. Exact scope checked

Let (R,m,k) be an excellent henselian local domain, k isomorphic to Fpbar, and dim R=N>=2. There is no normality, finite-type-model, equal-characteristic, or regular-puncture assumption on R. The proved groups are

    CH_1(Spec R)_Q = 0,
    CH^{N-1}(Spec R minus {m})_Q = 0.

The dimension function is delta(p)=dim(R/p) and is restricted unchanged to the puncture. Since a catenary local domain has ht(p)+dim(R/p)=N, the displayed codimension index is correct; deleting the closed point is not a reason to replace N by the puncture's smaller Krull dimension. The ordinary quotient is asserted only where its equivalence convention is defined. In particular the text does not impose coefficient-field product families on a mixed-characteristic ring.

The result does not assert integral vanishing or a uniform annihilating integer. It does not extend the residue field to an arbitrary transcendental algebraically closed field. Those distinctions are explicit and necessary.

## 2. Surface geometry checked

For a normal excellent local surface B, normality supplies a regular puncture, and excellence gives normal completion. Stacks54.14.5 applies with its exact condition (4), and its proof together with54.6.5 supplies normalized closed-point blowups over the singular closed point. Finite normalization is ensured by excellence. These modifications are projective and preserve the puncture simultaneously. In the regular case, the first modification is the blowup of the closed point.

Embedded resolution of the entire closed fibre uses Stacks54.15.6 on a regular surface; finite normalization of its curve components follows from excellence. Its proof uses closed-point blowups supported on that fibre. The final reduced fibre E is a projective strict normal-crossings curve; each component is smooth over the perfect residue field k. This reasoning does not import the threefold resolution theorem or its affine-cover projectivity issue.

The effective exceptional divisor with ample negative is also constructed, not presumed. For an ordinary blowup the exceptional F is effective Cartier and O(-F)=O(1). Pullback to a finite normalization remains Cartier because the normalization is dominant between integral schemes; finite pullback preserves relative ampleness, checked locally over an affine open of the preceding stage. For a subsequent step h, the divisor F_h+a h*D_0 is effective and its negative is ample for the composite once a is sufficiently large. This is exactly the sign in Stacks29.38.8. The first exceptional divisor has the entire first closed fibre as support, so its total transform ensures every final exceptional component occurs with a positive coefficient. No unproved conjunction of projectivity and regular-open preservation remains.

## 3. Finite K0 detection and determinant checked

KST TheoremA/(1.6) applies to the noetherian abstract blowup square with centre the closed point. K0(B) and K0(B/n^b) are Z. Quotienting the diagonal graph of the structure-sheaf class leaves the constant pro-group K0(Z), which maps monomorphically to the system K0(E_b). The levelwise kernel groups are decreasing subgroups of that fixed group, with inclusion transition maps. A pro-zero system of inclusions has an actually zero term. Thus some finite thickening detects K0(Z); no inference from vanishing of an inverse limit alone is used.

The mixed-characteristic extension is justified exactly: p lies in n, hence p^b=0 on E_b. Geisser--Hesselholt TheoremA printedp29 assumes p is nilpotent in the ring, not that the ring is an Fp-algebra. On each affine of the finite detecting thickening, the nilpotent reduction to E is therefore a K-equivalence after inverting p. A finite affine cover and Thomason--Trobaugh Zariski descent give the rational K0 comparison globally. No p-nilpotence on B or Z is asserted.

For a line bundle L of multidegree zero on E, the normalization/gluing argument is valid. Each component restriction is a point of a Jacobian over Fpbar and is torsion; after a common power trivializes these restrictions, only finitely many node-gluing scalars remain. They lie in k* and are torsion. A further power makes the restriction actually trivial on E, even if the dual graph has several connected components.

Consequently [L^M]-[O_Z] is zero in K0(E), hence zero rationally in K0(Z). Some integer multiple is zero integrally in K0(Z). The determinant homomorphism then gives L^{Mn}=O_Z. The proof correctly takes an actual tensor power before applying K0; it does not confuse the additive class [L]-1 with the assertion that L has finite tensor order. Z is projective over affine and has the resolution property; Stacks36.38.5 identifies perfect-complex and vector-bundle K0, and Stacks17.26/17.26.1 gives the required determinant map. Thus the multidegree map Pic(Z)_Q→Q^c is injective without a rational Chern-character theorem or a smooth finite-type model.

## 4. Intersection matrix and divisor localization checked

M_ij=deg(O_Z(E_j)|E_i) is symmetric, with nonnegative off-diagonal intersection lengths. The effective divisor D=Σa_iE_i with -D ample gives Ma<0. With Q=diag(a)Mdiag(a), the identity

    x^t Q x = Σ_i (Σ_j Q_ij)x_i^2 − Σ_{i<j}Q_ij(x_i−x_j)^2

is exact. It proves negative definiteness and invertibility. The exceptional line bundles consequently span all rational multidegrees and, by injectivity, all Pic(Z)_Q. Taking the Weil-divisor closure of a Cartier divisor on the regular puncture supplies Pic(Z)→Pic(U) surjectivity; Z is regular and locally factorial. Exceptional bundles restrict trivially. Hence Pic(U)_Q=0.

For the normal local surface, CH_1(Spec B)→CH_1(U)=Pic(U) is an isomorphism by localization: the closed point has delta-dimension zero, so carries no one-cycles. This surface conclusion has exactly the arbitrary-excellent henselian and mixed-characteristic scope needed later.

## 5. All-dimensional finite pushforward checked

For each curve prime p of the possibly nonnormal domain R, a saturated chain from0 to m through p has a preceding prime q with dim(R/q)=2. Catenarity supplies the exact lengths; N=2 is handled by q=0. The quotient R/q is an excellent henselian local domain. Its normalization T is finite by excellence and remains a domain. Stacks15.106.23 identifies it as henselian local; its finite residue extension is k because k is algebraically closed. Integral extension preserves dimension, so T is a normal local surface to which the preceding argument applies. No algebraization or simultaneous descent of q and its normalization is necessary.

A prime P above p/q is neither zero nor maximal: its contraction is nonzero and nonmaximal. In dimension2 it is therefore height1. The composite Spec T→Spec(R/q)→Spec R is finite. Its proper pushforward sends [V(P)] to the positive finite field degree [kappa(P):kappa(p)] times [V(p)]. Stacks42.20.3 applies over the excellent universally catenary base with its specified dimension function. Rational equivalences are preserved, so the surface vanishing kills each ambient curve generator rationally. Localization removes the closed point without changing CH_1. This proves the all-N claim without a resolution theorem in dimension>N=2.

## 6. Primary sources freshly opened and read for this audit

- Stacks54.14.5, Tag0BGP: full statement/proof of the surface-resolution criterion; Section54.14, especially Definitions54.14.1--2 and the proof's normalized-blowup reduction, also read.
- Stacks54.6.5, Tag0BFZ: full closed-point normalized-blowup gluing statement/proof.
- Stacks54.15.6, Tag0BIC, and Section54.15: full embedded-resolution statement/proof and its point-blowup construction.
- Stacks31.33.4, Tag02OS: full effective-exceptional and tautological-sign proof; Section31.33's blowup convention.
- Stacks30.17.2, Tag0B5V, and29.38.8, Tag0C4K: full finite-pullback ampleness and composition statements/proofs.
- Kerz--Strunk--Tamme, arXiv1611.08466v4,16August2017,48-page author PDF: TheoremA and its equivalent exact sequence(1.6), authorpp2--3, freshly read. The theorem's base hypothesis is noetherianity. The published citation remains Inventiones211(2018),523--577.
- Geisser--Hesselholt, *On relative and bi-relative algebraic K-theory of rings of finite characteristic*, published JAMS24(2011),29--49: full TheoremA printedp29 freshly read, including p-nilpotent scope and all integer K-degrees. TheoremC printedp30 was also inspected. The finite affine descent step uses TT Theorem8.1, which was already opened and checked in this run's C3bc audit; no fresh rereading of the entire TT paper is claimed here.
- Stacks36.38.5, Tag0FDJ: full proof of vector-bundle/perfect K0 comparison. Stacks17.26, Tag0B37, especially Lemma17.26.1 and the determinant paragraph: full required construction read.
- Stacks15.106.23, Tag092X, and10.153.4, Tag04GH: full integral-henselian and finite-algebra local-factor statements/proofs.
- Stacks42.19.3, Tag02RX, and42.20.3, Tag02S2: complete localization and proper-pushforward proofs in the dimension-function framework.

The original finite-model draft's Stacks37.19.4 Tag0CBM and10.156.2 Tag05WQ were freshly opened too; their normalization/quotient compatibility checks passed, but they are not needed in the strengthened proof.

## 7. Literature history and version distinctions

The literature search used normal surface Q-factoriality over Fpbar, henselian local class-group torsion, and Chow one-cycles over local rings. It found and opened the following primary antecedents:

1. Tanaka, *Minimal models and abundance for positive characteristic log surfaces*, Nagoya Mathematical Journal216(2014),1--70, DOI10.1215/00277630-2801646. Full published PDF opened; Theorem4.5 printedp42 and its proof/Remark4.9 printedp43 read. It states Q-factoriality of normal surfaces over Fpbar. This is a finite-type equal-characteristic antecedent, not the source of the arbitrary-excellent mixed-characteristic extension.
2. Esser, *Non-torsion Brauer groups in positive characteristic*, ProceedingsAMS151(2)(2023),527--531, DOI10.1090/proc/16140. The clean five-page author PDF at `https://web.math.princeton.edu/~le3339/NonTorsionBrauerGroups.pdf` was opened and the complete Theorem2.4 proof on authorpp4--5 read. It explicitly proves torsion of the henselian local class group, crediting Artin's argument. The separately opened annotated six-page `NonTorsionBrauerGroupsComment.pdf` puts the same theorem onpp5--6; that pagination is not assigned to the clean version. The final draft uses the clean-version locator correctly.

No priority claim is supported or made. These source reads do not claim a full audit of Tanaka's MMP or of every theorem in the surrounding papers.

## 8. Computation/build boundary and conclusion

This review checked the complete typed proof and the exact primary hypotheses above. It did not independently run a finite certificate or a LuaLaTeX build, and no such computation is counted. The result is a theorem, so no bounded numerical experiment is offered in place of its universal proof. I found no mathematical correction needed in the strengthened draft.

The theorem closes the rational top-Chow branch under the stated residue-field condition. It does not settle the remaining arbitrary-transcendental-field top quotient or the high positive-characteristic ordinary restriction ranges. Its finite-field residue scope must remain visible in the parent status table.

## 9. Same-ID nonhenselian refinement: independent PASS

**Typed refinement reread and certified at 2026-11-19 13:06:03 UTC.** The final file now assumes only that R is an excellent local domain with residue field Fpbar. This is a strengthening of the same statement, not a correction of a false earlier conclusion. The formerly certified henselian version is retained by the owner.

No step of the normal-surface proof uses henselianity. The resolution and the effective negative-ample exceptional divisor require excellence and locality; both K0 groups of base rings are Z because the rings are local; the finite-level nilpotent theorem, determinant, and exceptional intersection calculation are unchanged. Properness over a local base makes the closed fibre projective over its residue field without requiring a henselian base.

For an arbitrary surface quotient B=R/q, its normalization T is finite, normal, integral, and semilocal. Every localization at a maximal ideal is an excellent normal local ring of dimension at most two, with residue field Fpbar. Its class group is torsion by the surface proof in dimension two and is zero in dimensions zero and one. Given a Weil divisor G, choose one common positive integer e killing the finitely many localized classes. The rank-one coherent reflexive module of eG is free at every maximal localization, hence finite locally free of rank one on Spec(T). A semilocal ring has trivial Picard group, so that module is globally free and eG is principal. Thus Cl(T)_Q=0.

The revised proof correctly retains the pulled-back dimension function. A finite map has zero residue transcendence degrees; its generic point has delta-value two. The explicit identification Cl(T)=CH_1(T) therefore applies. A prime above p/q is nonzero and nonmaximal, hence height one in the two-dimensional domain T, and its finite pushforward has the required positive residue-field degree. No selection of one normalization branch is necessary. The whole semilocal normalization is used in the proper pushforward.

Fresh primary reads for this refinement: Stacks Lemma10.78.7, Tag02M9 (semilocal constant-rank finite locally free modules are free, with the Chinese-remainder/Nakayama proof hints); Lemma31.30.2, Tag0EBM (complete reflexive-module/Weil-class proof); Lemma29.53.3, Tag02JW (complete induced dimension-function proof); and Section42.24, Tag02SI, the paragraph immediately after Definition42.24.1 explicitly identifying Cl with CH in the inherited dimension convention. Lemma29.53.1, Tag02JU, was also opened and read: in this finite birational universally catenary situation it in fact implies equality of local dimensions over each base point, but the typed argument needs only the weaker bound and does not rely on that additional claim. No independent program or build rerun was performed. No mathematical correction is requested.
