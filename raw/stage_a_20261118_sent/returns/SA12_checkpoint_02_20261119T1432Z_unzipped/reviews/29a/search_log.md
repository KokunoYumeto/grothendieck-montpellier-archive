# Literature search and source-access log — 29a

Review date: 2026-11-19 UTC. The batches are in execution order; exact per-call clock times were not recorded and are not reconstructed from file mtimes. Every claim has a manually assigned searched target in `claim_search_map.json`. The search map carries the full quantifiers, so broad topic similarity is never the asserted basis for exact settlement.

## Method and negative-search limits

Searches used the two available web search engines, with stronger primary-source verification when needed. Named zbMATH Open, arXiv, MathOverflow and Numdam searches are preserved verbatim below. The zbMATH and MathOverflow queries were targeted web-index searches, not claims to have exhaustively queried every database record. EGA/SGA originals, author-hosted papers, publisher contents and author bibliographies were followed backwards. Modern AI translations and search snippets were leads only; no theorem-level verification rests on them.

A returned search result is not an opened source. Requests below distinguish search, open, find and screenshot. Bibliography `verified` records access, and its annote states whether theorem text, proof, metadata or only a table of contents was read. No hit, failed access, or an unavailable preliminary proposition does not establish novelty or present openness.

## Claim coverage

### CL-SA12-001

**Exact target:** A finite étale covering of X trivial over its geometric generic fibre descends to a finite étale covering of normal integral Y, under the faithfully flat finite-type and reduced-fibre qualifier on initial scan48; that qualifier is unresolved.

**Search batches:** web_batch_01.json, web_batch_20.json, web_batch_22.json, web_batch_24.json, web_batch_25.json, web_batch_26.json, web_batch_27.json. **Opened reference keys:** SGA1_1971, Stacks0BUM, Stacks0BQJ, KatzLang1981.

**Result and limit:** The field-base generic-fibre assertion is SGA1 IX §6. Normalization and generic descent have established forms, but the precise nonproper flat biréduit/réduit version on these leaves was not matched to an opened theorem. Stacks 0BUM proves a proper flat finite-presentation variant and does not settle this exact qualifier. The unresolved remainder is identification of the written hypotheses, not an assertion that generic descent is open. Katz–Lang1981, Preliminaries Lemma2 (PDFpp8–9), explicitly proves the generic-fibre exact sequence for smooth surjective finite-type X→S, with S normal connected locally noetherian and connected geometric generic fibre. This settles the smooth variant, not an unidentified broader reduced-fibre adjective.

### CL-SA12-002

**Exact target:** With the same hypotheses as CL-SA12-001 and geometric basepoints, the generic-fibre sequence is exact if the preceding covering-descent lemma holds.

**Search batches:** web_batch_01.json, web_batch_20.json, web_batch_22.json, web_batch_24.json, web_batch_25.json, web_batch_26.json, web_batch_27.json. **Opened reference keys:** SGA1_1971, Stacks0BUM, Stacks0BN6, KatzLang1981.

**Result and limit:** The Galois-category deduction from the asserted covering descent is valid. SGA1 IX §6 and the proper homotopy theorem are established comparisons; no passage opened establishes the unresolved biréduit/réduit nonproper generality verbatim. Katz–Lang1981, Preliminaries Lemma2 (PDFpp8–9), explicitly proves the generic-fibre exact sequence for smooth surjective finite-type X→S, with S normal connected locally noetherian and connected geometric generic fibre. This settles the smooth variant, not an unidentified broader reduced-fibre adjective.

### CL-SA12-003

**Exact target:** For finite-type f:X→Y with Y locally noetherian universally Japanese, direct image of a constructible finite-set étale sheaf is constructible.

**Search batches:** web_batch_01.json, web_batch_03.json, web_batch_05.json, web_batch_06.json, web_batch_15.json, web_batch_18.json, web_batch_21.json. **Opened reference keys:** DegliseGabber2007.

**Result and limit:** Déglise, Finitude et constructibilité en cohomologie étale, Theorem1.1 (account of Gabber), proves the stronger degree-zero result for every noetherian base, with no excellence hypothesis. Theorem1.2 concerns R¹ under different torsion and quasi-excellence assumptions and is not used to strengthen the manuscript claim.

### CL-SA12-004

**Exact target:** For a noetherian universally Japanese X, a finite locally closed partition X_i, and finite constant G, restriction H¹(X,G)→∏H¹(X_i,G) has finite fibres.

**Search batches:** web_batch_01.json, web_batch_03.json, web_batch_05.json, web_batch_06.json, web_batch_15.json, web_batch_18.json, web_batch_21.json. **Opened reference keys:** DegliseGabber2007, SGA1_1971.

**Result and limit:** The finite reconstruction/gluing problem is closely tied to constructibility of finite sheaves. Searches for the exact universal-Japanese partition lemma did not locate its numbered published form. Déglise Theorem1.1 verifies the needed degree-zero finiteness framework, not this entire nonabelian finite-fibre conclusion. No proof certification is assigned.

### CL-SA12-005

**Exact target:** For constructible finite-set étale sheaves F,G on a noetherian scheme, Hom(F,G) is finite.

**Search batches:** web_batch_01.json, web_batch_03.json, web_batch_05.json, web_batch_06.json, web_batch_15.json, web_batch_18.json, web_batch_21.json. **Opened reference keys:** DegliseGabber2007.

**Result and limit:** This is standard constructible-sheaf finiteness: choose a common finite stratification into connected locally closed pieces where both are finite locally constant; finitely many geometric stalk maps determine a morphism. The elementary proof is independently supplied. The opened constructibility reference supplies the setting; no exact priority date is claimed.

### CL-SA12-006

**Exact target:** For a noetherian universally Japanese base S and finite G, finiteness of H¹(X,G) for every finite-type X/S is reduced to smooth affine X→S′ with nonempty geometrically connected fibres, where S′ is finite étale over a normal integral affine subscheme S₀ of S, after shrinking the base to a nonempty open.

**Search batches:** web_batch_01.json, web_batch_04.json, web_batch_06.json, web_batch_07.json, web_batch_18.json, web_batch_20.json, web_batch_21.json, web_batch_22.json, web_batch_27.json. **Opened reference keys:** SGA1_1971, DegliseGabber2007.

**Result and limit:** The required normal-base covers, shrinking, and dimension induction are explicit. SGA1 X2.12 gives Lang–Serre finiteness over algebraically closed fields, and modern Gabber constructibility handles a key sheaf-theoretic input. Searches did not identify an exact published theorem with all these base quantifiers. The precise equivalence is retained as a searched historical proof task, not declared a new open theorem.

### CL-SA12-007

**Exact target:** A sufficient H¹-finiteness criterion combines finiteness for geometric fibres with finiteness on all required base covers for every subgroup H≤G×G; for abelian G the author says G alone suffices.

**Search batches:** web_batch_01.json, web_batch_04.json, web_batch_06.json, web_batch_07.json, web_batch_18.json, web_batch_20.json, web_batch_21.json, web_batch_22.json, web_batch_27.json. **Opened reference keys:** SGA1_1971, DegliseGabber2007.

**Result and limit:** The G×G quantifier belongs to the descent comparison of two torsors and cannot be replaced by a statement only about H¹(S,G). The exact quantified sufficient criterion was searched alongside CL-SA12-006 and not found verbatim in the opened sources. Neither finite H¹ for every target nor this criterion implies finite generation of an arbitrary profinite group.

### CL-SA12-008

**Exact target:** The proposed global H¹-finiteness consequences restrict G to order prime to all residue characteristics and require the preceding normal-base finiteness assumptions.

**Search batches:** web_batch_01.json, web_batch_04.json, web_batch_06.json, web_batch_07.json, web_batch_18.json, web_batch_20.json, web_batch_21.json, web_batch_22.json, web_batch_27.json. **Opened reference keys:** SGA1_1971, ESS2021.

**Result and limit:** Prime-to-characteristic geometric finiteness is established in SGA1 X and XIII. The complete arithmetic-base version still inherits the quantified assumptions of CL-SA12-006/007, whose exact generality was not matched to a printed theorem. Removing the restriction on affine schemes is false: Artin–Schreier classes x^m, p∤m, yield infinitely many Z/p-torsors on A¹ in characteristic p.

### CL-SA12-009

**Exact target:** If every smooth algebraic curve over a fixed field k has finitely many finite étale covers of each degree, does every finite-type k-scheme have that property?

**Search batches:** web_batch_01.json, web_batch_04.json, web_batch_06.json, web_batch_07.json, web_batch_18.json, web_batch_20.json, web_batch_21.json, web_batch_22.json, web_batch_27.json. **Opened reference keys:** SGA1_1971, DegliseGabber2007, ESS2021.

**Result and limit:** The curve-fibration and constructibility reduction is a plausible route; SGA1 proves the important geometric prime-to-p/proper cases, while affine wild covers show that the premise is substantial. Exact all-fields, all-finite-type quantifiers were searched but not matched. This record does not call the question presently open: its exact published fate remains unlocated.

### CL-SA12-010

**Exact target:** The induction seeks, after dense-open shrinking and appropriate treatment of constants, a smooth curve fibration with nonempty geometrically connected fibres and a lower-dimensional base.

**Search batches:** web_batch_01.json, web_batch_18.json, web_batch_20.json, web_batch_22.json, web_batch_24.json, web_batch_27.json. **Opened reference keys:** SGA1_1971, Stacks0G4C, KatzLang1981.

**Result and limit:** Generic projection, separating transcendence bases, and shrinking give such fibrations under the relevant separability assumptions. The arbitrary-field formulation needs those assumptions stated, and the page does not supply them. The exact construction was searched within the finiteness and Bertini references; no unrestricted version is certified. Katz–Lang1981 §2 uses Artin good neighbourhoods/elementary fibrations and cites SGA4 XI3.1; this supplies a precise backward reference for the smooth geometric reduction.

### CL-SA12-011

**Exact target:** For an algebraic scheme over an algebraically closed field of characteristic exponent p, the maximal prime-to-p quotient of its étale fundamental group is topologically finitely generated.

**Search batches:** web_batch_04.json, web_batch_06.json, web_batch_07.json, web_batch_08.json, web_batch_11.json, web_batch_12.json, web_batch_13.json, web_batch_16.json, web_batch_17.json, web_batch_18.json, web_batch_21.json. **Opened reference keys:** SGA1_1971, ESS2021, LSS2023.

**Result and limit:** The generic-section and tame-curve method appears in SGA1 X and XIII; finite generation in the stated geometric setting is established. Full étale finite generation for an affine variety in positive characteristic is false. ESS2021 strengthens the tame group for a smooth variety with a good compactification to finite presentation, and LSS2023 proves finite presentation for all connected proper schemes; those are different hypotheses.

### CL-SA12-012

**Exact target:** For a finite étale cover of U×Y tame along the indicated normalized codimension-one boundary, triviality on the fibre over a chosen rational point y should imply descent from a neighbourhood of y in Y. The normal/proper hypotheses differ between witnesses.

**Search batches:** web_batch_04.json, web_batch_06.json, web_batch_07.json, web_batch_08.json, web_batch_11.json, web_batch_12.json, web_batch_13.json, web_batch_16.json, web_batch_17.json, web_batch_18.json, web_batch_21.json. **Opened reference keys:** SGA1_1971, EK2016, EKerr2016.

**Result and limit:** Tame homotopy and product theorems have established forms, but exact recovery here depends on properness, geometric tameness, and the chosen compactification. SGA1 XIII and Esnault–Kindler supply precise related theorems; neither is cited as settling every witness variant. The remaining task is a quantified reconstruction and comparison.

### CL-SA12-013

**Exact target:** Extend the fibrewise tame-covering descent argument from a normal ambient X to a nonnormal X by descent.

**Search batches:** web_batch_04.json, web_batch_06.json, web_batch_07.json, web_batch_08.json, web_batch_11.json, web_batch_12.json, web_batch_13.json, web_batch_16.json, web_batch_17.json, web_batch_18.json, web_batch_21.json. **Opened reference keys:** SGA1_1971, EK2016, GM1971.

**Result and limit:** Finite étale coverings satisfy effective descent in the usual descent settings, but compatibility of the page’s normalization-boundary definition of tameness requires its own argument. The exact nonnormal extension was searched in SGA1 and the tame-covering literature without locating a theorem that matches these abbreviated hypotheses.

### CL-SA12-014

**Exact target:** The proposed tame product formula uses compactifications and tameness at boundary divisors; its exact formulation is conditional on the preceding descent statement.

**Search batches:** web_batch_04.json, web_batch_06.json, web_batch_07.json, web_batch_08.json, web_batch_11.json, web_batch_12.json, web_batch_13.json, web_batch_16.json, web_batch_17.json, web_batch_18.json, web_batch_21.json. **Opened reference keys:** SGA1_1971, ESS2021, EK2016.

**Result and limit:** Tame product results are established with specified notions of tameness. No unconditional identification of every boundary-tame quotient in this draft is made here. SGA1 XIII and modern tame finiteness references were searched, and the missing hypotheses remain explicit.

### CL-SA12-015

**Exact target:** For connected algebraic schemes over an algebraically closed field, the prime-to-characteristic fundamental group obeys the product formula in the indicated geometric setting.

**Search batches:** web_batch_04.json, web_batch_06.json, web_batch_07.json, web_batch_08.json, web_batch_11.json, web_batch_12.json, web_batch_13.json, web_batch_16.json, web_batch_17.json, web_batch_18.json, web_batch_21.json. **Opened reference keys:** SGA1_1971, ESS2021.

**Result and limit:** The prime-to-p product theorem is part of SGA1 XIII’s tame framework. It does not assert the unrestricted affine product formula: z^p−z=xy gives the obstruction in characteristic p. Proper-factor product theorems have different scope.

### CL-SA12-016

**Exact target:** For connected schemes over an algebraically closed field with geometric basepoints and the finite-type geometric hypotheses here, the full product map of étale fundamental groups is surjective.

**Search batches:** web_batch_04.json, web_batch_06.json, web_batch_13.json, web_batch_21.json. **Opened reference keys:** SGA1_1971.

**Result and limit:** The section maps induced by fixed geometric points show that the image in the product contains each of its two factors, hence is the whole product. This does not assert that the chosen lifted subgroups commute in the source. The elementary argument does not prove injectivity. SGA1 supplies the framework.

### CL-SA12-017

**Exact target:** For a proper normal compactification, the quotient of π₁ of its open part obtained by killing wild inertia at codimension-one boundary is asserted finitely generated; Codex instead reads finitely presented.

**Search batches:** web_batch_04.json, web_batch_06.json, web_batch_07.json, web_batch_08.json, web_batch_11.json, web_batch_12.json, web_batch_13.json, web_batch_16.json, web_batch_17.json, web_batch_18.json, web_batch_21.json. **Opened reference keys:** SGA1_1971, ESS2021, LSS2023, EK2016, EKerr2016.

**Result and limit:** Finite generation via a fixed tame curve is compatible with SGA1 XIII and Lefschetz. Finite presentation is proved by ESS2021 for smooth varieties admitting good compactifications, and LSS2023 for proper schemes; these do not automatically cover arbitrary singular compactifications and this exact divisorial quotient. The FG/FP reading is a material unresolved issue.

### CL-SA12-018

**Exact target:** If X is a proper normal variety over an algebraically closed field and Z⊂X has codimension at least two, π₁(X∖Z) is claimed topologically finitely generated.

**Search batches:** web_batch_06.json, web_batch_07.json, web_batch_13.json, web_batch_17.json, web_batch_18.json, web_batch_22.json, web_batch_24.json, web_batch_32.json, web_batch_33.json. **Opened reference keys:** SGA1_1971, Stacks0BN6.

**Result and limit:** The fixed generic-curve connectedness argument independently gives the claimed finite generation in the normal setting, using the established SGA1 X hyperplane method. The opened printed lemma itself treats proper normal schemes, so the codimension-two open variant is labelled a reconstruction rather than a verbatim theorem match. Normality ensures connected finite covers remain irreducible on the dense open. The separate question about finite generation of the kernel is not settled by this assertion.

### CL-SA12-019

**Exact target:** The codimension-two finite-generation argument is extended through irreducible components and gluing; the written reduction also invokes Chow’s lemma.

**Search batches:** web_batch_06.json, web_batch_07.json, web_batch_13.json, web_batch_17.json, web_batch_18.json, web_batch_22.json, web_batch_24.json, web_batch_32.json, web_batch_33.json. **Opened reference keys:** SGA1_1971, LSS2023.

**Result and limit:** Finiteness can be treated by finite component/gluing arguments, but the statement that the full inverse image of a codimension-two omitted set stays codimension two under a projective modification is false. The target theorem must be separated from that step; modern proper finite presentation alone does not prove this open-subscheme assertion.

### CL-SA12-020

**Exact target:** The full inverse image of the excluded codimension-two set is assumed to have codimension at least two after an unspecified Chow modification.

**Search batches:** web_batch_06.json, web_batch_07.json, web_batch_13.json, web_batch_17.json, web_batch_18.json, web_batch_22.json, web_batch_24.json, web_batch_32.json, web_batch_33.json. **Opened reference keys:** StacksBlowup.

**Result and limit:** Blowing up a closed point on a smooth surface produces an exceptional divisor, so the claimed automatic codimension preservation fails. This is an independent refutation of the inference; the exact placement as an assumption versus conclusion needs the scan. The corrected statement must separately control exceptional divisors.

### CL-SA12-021

**Exact target:** The indicated generic linear-section irreducibility theorem over an arbitrary field requires geometric irreducibility of X when the generic parameter field is algebraically closed.

**Search batches:** web_batch_06.json, web_batch_07.json, web_batch_13.json, web_batch_17.json, web_batch_18.json, web_batch_22.json, web_batch_24.json, web_batch_32.json, web_batch_33.json, web_batch_34.json, web_batch_35.json, web_batch_36.json, web_batch_37.json, web_batch_38.json, web_batch_39.json. **Opened reference keys:** SGA1_1971, Stacks0G4C, PoonenSlavov2020.

**Result and limit:** P²_C viewed over R is integral but splits after algebraic closure, refuting the ordinary-irreducibility version. Cote29 scan113 explicitly says geometrically irreducible (parent checked its endpoint), and SGA1 X2.10–2.11 has the precise geometric hyperplane setting. This later refinement is mathematical evidence, not a decision about scan67’s ink. Poonen–Slavov, Theorem1.8 and Lemma7.1 with§7 proof, independently establish the general morphism version after geometric irreducibility is imposed: when the image has dimension at least2, the bad hyperplane locus has dimension at most r−1. Iterating generic hyperplanes gives the codimension-s form. This exact modern development needs neither properness nor normality; Theorem1.5 alone would require equidimensional fibres. ArXiv first circulation23 January2020; author PDF dated4 August2020. Jouanolou1983 is their backward reference, not a book opened here.

### CL-SA12-022

**Exact target:** Replacing irreducibility by connectedness in the generic-section connectedness statement is proposed and rejected.

**Search batches:** web_batch_06.json, web_batch_07.json, web_batch_13.json, web_batch_17.json, web_batch_18.json, web_batch_22.json, web_batch_24.json, web_batch_32.json, web_batch_33.json. **Opened reference keys:** SGA1_1971.

**Result and limit:** The rejection is correct: two projective planes meeting only at one point form a connected scheme, while a general hyperplane misses the intersection point and cuts two disjoint curves. The normal/geometrically irreducible hypotheses in SGA1’s theorem avoid this example.

### CL-SA12-023

**Exact target:** Under normality and geometric irreducibility, a sufficiently general complete-intersection curve has surjective π₁ map to the ambient variety/open in the stated setup.

**Search batches:** web_batch_06.json, web_batch_07.json, web_batch_13.json, web_batch_17.json, web_batch_18.json, web_batch_22.json, web_batch_24.json, web_batch_32.json, web_batch_33.json. **Opened reference keys:** SGA1_1971, Stacks0BN6.

**Result and limit:** SGA1 X2.10–2.11 proves the proper normal hyperplane comparison, using connectedness of inverse images under finite étale covers. The generic connected-cover step is the same mechanism. Claims for arbitrary nonproper special sections require additional control and are separated as CL-SA12-024.

### CL-SA12-024

**Exact target:** Replace the generic section by a suitable special section while retaining surjectivity of π₁.

**Search batches:** web_batch_06.json, web_batch_07.json, web_batch_13.json, web_batch_17.json, web_batch_18.json, web_batch_22.json, web_batch_24.json, web_batch_32.json, web_batch_33.json. **Opened reference keys:** SGA1_1971, EK2016, EKerr2016.

**Result and limit:** SGA1 X2.10–2.11 explicitly supplies a proper normal special-hyperplane form, via connectedness. For open/tame pairs, Esnault–Kindler Theorem1.1 has regular proper/SNC and Lef/Leff hypotheses. Its normal-variety theorem6.1 needs the complete-intersection-of-ample-divisors condition added in the 2016 erratum.

### CL-SA12-025

**Exact target:** For the fixed normal projective model and fixed smooth complete-intersection curve C of genus g avoiding the excluded codimension-two set, the induced quotient π₁(U) is generated by at most 2g elements.

**Search batches:** web_batch_06.json, web_batch_07.json, web_batch_13.json, web_batch_17.json, web_batch_18.json, web_batch_22.json, web_batch_24.json, web_batch_32.json, web_batch_33.json. **Opened reference keys:** SGA1_1971, ESS2021.

**Result and limit:** SGA1 X2.9–2.11 combines a curve and the proper normal connectedness argument; SGA1 XIII2.12 gives the prime-to-p/tame curve presentation input. The genus is tied to the chosen model and polarization, not a birational invariant. The claim is a bound, not a presentation of π₁(U).

### CL-SA12-026

**Exact target:** Fix a regular open of one proper normal model. A rational map to each other proper normal model is defined away from codimension two; purity for the regular source and normality of the target produce compatible surjections to all model fundamental groups.

**Search batches:** web_batch_01.json, web_batch_02.json, web_batch_05.json, web_batch_09.json, web_batch_17.json, web_batch_18.json, web_batch_20.json, web_batch_22.json. **Opened reference keys:** Stacks0BX7, Stacks0BMB, SGA1_1971.

**Result and limit:** The individual tools are established: valuative extension to proper targets, purity of the branch locus on regular schemes, and connected-cover surjectivity for a dense open in a normal scheme. The single-source compatibility is reconstructed in independent_checks.md. No exact published statement under the author’s birational terminology was located.

### CL-SA12-027

**Exact target:** The inverse limit of π₁ of all proper normal models of a fixed function field over an algebraically closed field is a quotient of one finitely generated group and hence finitely generated.

**Search batches:** web_batch_01.json, web_batch_02.json, web_batch_05.json, web_batch_09.json, web_batch_17.json, web_batch_18.json, web_batch_20.json, web_batch_22.json. **Opened reference keys:** SGA1_1971, Stacks0BMB.

**Result and limit:** With the single fixed regular open in CL-SA12-026, finite intersections of compact fibres give surjectivity onto the inverse limit. This establishes the compressed implication. Exact terminology/priority was not located in the searched birational literature. It does not imply that the inverse system stabilizes.

### CL-SA12-028

**Exact target:** If a proper regular model exists, the system of fundamental groups of proper normal models is essentially constant.

**Search batches:** web_batch_01.json, web_batch_02.json, web_batch_05.json, web_batch_09.json, web_batch_17.json, web_batch_18.json, web_batch_20.json, web_batch_22.json. **Opened reference keys:** SGA1_1971, Stacks0BMB, Stacks0BX7.

**Result and limit:** Purity implies birational invariance for proper regular models, and normal graph closures give a cofinal subsystem dominating the fixed regular model. This is the established mechanism; no unrestricted resolution assumption is introduced. The exact draft formulation was not found verbatim in a published source.

### CL-SA12-029

**Exact target:** For arbitrary function fields, without a proper regular model assumed, is the system of π₁ of proper normal models essentially constant?

**Search batches:** web_batch_01.json, web_batch_02.json, web_batch_05.json, web_batch_09.json, web_batch_17.json, web_batch_18.json, web_batch_20.json, web_batch_22.json. **Opened reference keys:** SGA1_1971, LSS2023.

**Result and limit:** Searches in SGA1, arXiv, MathOverflow, zbMATH-targeted queries and birational-Picard literature did not locate a theorem settling this exact all-model stabilization question. This is a search result, not a claim of current openness or novelty. A uniform generator bound does not suffice, as Z/ℓ^m shows. The regular-model case is CL-SA12-028.

### CL-SA12-030

**Exact target:** For any proper normal model X, does its regular locus U already have the birational fundamental group; equivalently, can every finite étale cover of U become étale on some proper modification?

**Search batches:** web_batch_01.json, web_batch_02.json, web_batch_05.json, web_batch_09.json, web_batch_17.json, web_batch_18.json, web_batch_20.json, web_batch_22.json. **Opened reference keys:** Stacks0BMB, Stacks0BX7, SGA1_1971.

**Result and limit:** A complex projective quotient X=(P¹×P¹)/⟨(x,y)↦(−x,−y)⟩ has four isolated quotient singularities. Its regular locus has a connected étale double cover from the complement of the fixed points. Writing the invariant field as C(a,t), a=x², t=y/x, the extension C(x,y)/C(a,t) ramifies at the a-adic valuation. That valuation has a centre on every proper model, so the cover cannot extend étale on any of them. A regular proper rational model has trivial π₁. This independently checked example answers the exact question negatively; it is not a novelty claim.

### CL-SA12-031

**Exact target:** For proper normal X and codimension-two Z, is ker(π₁(X∖Z)→π₁(X)) topologically finitely generated?

**Search batches:** web_batch_01.json, web_batch_02.json, web_batch_05.json, web_batch_09.json, web_batch_17.json, web_batch_18.json, web_batch_20.json, web_batch_22.json. **Opened reference keys:** SGA1_1971, LSS2023, ESS2021.

**Result and limit:** Exact searches in MathOverflow, arXiv, SGA1 and the modern finite-presentation literature did not settle this geometric kernel question. A two-generator profinite semidirect product with infinitely generated kernel only refutes an abstract inference from surrounding finite generation; it is not a geometric counterexample. The 2023 proper finite-presentation theorem does not itself control this kernel.

### CL-SA12-032

**Exact target:** The author suggests an algebraic or proalgebraic formulation of the birational fundamental group, with an unresolved adjective and no specified category.

**Search batches:** web_batch_01.json, web_batch_02.json, web_batch_05.json, web_batch_09.json, web_batch_17.json, web_batch_18.json, web_batch_20.json, web_batch_22.json. **Opened reference keys:** SGA1_1971.

**Result and limit:** Searches for the phrase and nearby birational group constructions produced no unique identification. Proalgebraic, tannakian and profinite formulations are not interchangeable. The category must be recovered from the scan/context before a mathematical fate can be assigned.

### CL-SA12-033

**Exact target:** For a proper birational map f:X→Y between integral normal proper k-schemes with Y regular, pullback on Pic^τ is asserted to be an isomorphism of group schemes; geometric normality/smoothness and projectivity are questioned in the margins.

**Search batches:** web_batch_01.json, web_batch_02.json, web_batch_05.json, web_batch_06.json, web_batch_07.json, web_batch_08.json, web_batch_09.json, web_batch_14.json, web_batch_15.json, web_batch_16.json, web_batch_17.json, web_batch_18.json, web_batch_19.json, web_batch_21.json. **Opened reference keys:** Kleiman2005, KLOS, RuellingSaito2022, Groth236.

**Result and limit:** Classical birational invariance of the reduced Picard/Albanese variety and smooth proper variants are established, but those statements do not alone settle this normal-source, possibly nonreduced Pic^τ assertion. Kleiman2005 gives Picard representability/properness and restriction results, while KLOS distinguishes the classical rational Albanese from the morphism Albanese of a normal model. Exact searches did not locate an opened theorem matching every written hypothesis. The page’s points-plus-tangents endpoint is insufficient on its own; the main theorem is not thereby refuted.

### CL-SA12-034

**Exact target:** Under universal f_*O_X=O_Y and suitable representability, pullback Pic_Y→Pic_X is a monomorphism; restricted to proper Picard group schemes it is a closed immersion.

**Search batches:** web_batch_01.json, web_batch_02.json, web_batch_05.json, web_batch_06.json, web_batch_07.json, web_batch_08.json, web_batch_09.json, web_batch_14.json, web_batch_15.json, web_batch_16.json, web_batch_17.json, web_batch_18.json, web_batch_19.json, web_batch_21.json. **Opened reference keys:** Kleiman2005, Groth236.

**Result and limit:** The monomorphism follows from descent of an isomorphism of pulled-back line bundles using the projection formula and f_*O_X=O_Y, universally in the base. A proper monomorphism is a closed immersion. Kleiman’s Picard framework is a checked reference for representability/properness; those hypotheses must be supplied, not inferred from normality over a nonperfect field.

### CL-SA12-035

**Exact target:** Restriction from the regular target Y to an open U with codimension-two complement is an isomorphism on line-bundle classes; the display instead reads Pic(X).

**Search batches:** web_batch_01.json, web_batch_02.json, web_batch_05.json, web_batch_06.json, web_batch_07.json, web_batch_08.json, web_batch_09.json, web_batch_14.json, web_batch_15.json, web_batch_16.json, web_batch_17.json, web_batch_18.json, web_batch_19.json, web_batch_21.json. **Opened reference keys:** Stacks0BMB, StacksBlowup.

**Result and limit:** A regular scheme is locally factorial, so a Cartier divisor extends uniquely across codimension two; this proves the target-Y statement. For a blowup X→Y, a nontrivial exceptional divisor restricts trivially on U, so the displayed source-X version is false. Both transcriptions read X; this review does not alter it.

### CL-SA12-036

**Exact target:** A τ-trivial Cartier divisor supported on the exceptional locus of a proper birational morphism to a regular target must have all coefficients zero.

**Search batches:** web_batch_01.json, web_batch_02.json, web_batch_05.json, web_batch_06.json, web_batch_07.json, web_batch_08.json, web_batch_09.json, web_batch_14.json, web_batch_15.json, web_batch_16.json, web_batch_17.json, web_batch_18.json, web_batch_19.json, web_batch_21.json. **Opened reference keys:** Kleiman2005, KLOS, NeronSamuel1952.

**Result and limit:** Negativity/intersection arguments establish familiar projective forms of exceptional-divisor independence. The exact arbitrary-dimensional normal-source/proper formulation and the attachment of insuffisant were not recovered from the opened sources. This is a local proof obligation of CL-SA12-033; neither the author’s phrase known nor later reduced-Picard invariance counts as its verification.

### CL-SA12-037

**Exact target:** The proposed proof endpoint would infer equality of proper group schemes from equality on geometric points and tangent spaces of a closed inclusion.

**Search batches:** web_batch_01.json, web_batch_02.json, web_batch_05.json, web_batch_06.json, web_batch_07.json, web_batch_08.json, web_batch_09.json, web_batch_14.json, web_batch_15.json, web_batch_16.json, web_batch_17.json, web_batch_18.json, web_batch_19.json, web_batch_21.json. **Opened reference keys:** SGA3_VIII, Kleiman2005.

**Result and limit:** For characteristic p, the inclusion α_p⊂α_{p²} of Frobenius kernels in G_a has the same single geometric point and induces an isomorphism on one-dimensional tangent spaces, but the lengths are p and p². Thus further infinitesimal control is required. This does not disprove the Picard theorem itself.

### CL-SA12-038

**Exact target:** For the normal-source/regular-target proper birational map under suitable geometric hypotheses, the author seeks an isomorphism on H¹(O), using Artin–Schreier fixed vectors and iterated Frobenius kernels in characteristic p, then spreading out in characteristic zero.

**Search batches:** web_batch_01.json, web_batch_02.json, web_batch_05.json, web_batch_06.json, web_batch_07.json, web_batch_08.json, web_batch_09.json, web_batch_14.json, web_batch_15.json, web_batch_16.json, web_batch_17.json, web_batch_18.json, web_batch_19.json, web_batch_21.json. **Opened reference keys:** Stacks0EC0, Stacks0AY6, Kleiman2005, RuellingSaito2022.

**Result and limit:** The separate local ingredients in CL-SA12-040–042 are valid. The all-iterates exponent is essential, and the spread-out argument needs cohomological base change and preservation of geometric hypotheses. Smooth birational cohomological invariance has published modern forms, but the opened Rülling–Saito Corollary11.24 is about torsion Picard groups in a specified smooth/fibred setting and is not substituted for this normal-source H¹ theorem. No complete scheme-level proof certification is assigned.

### CL-SA12-039

**Exact target:** A map of finite-dimensional semilinear Frobenius modules is an isomorphism if it compares the appropriate fixed/étale parts and all iterated Frobenius kernels; comparing only ker F is insufficient.

**Search batches:** web_batch_01.json, web_batch_02.json, web_batch_14.json, web_batch_17.json, web_batch_21.json, web_batch_23.json. **Opened reference keys:** StacksArtinSchreier.

**Result and limit:** The linear-algebra statement with all iterates follows from the nilpotent/invertible decomposition. A two-dimensional nilpotent Jordan block and its one-dimensional kernel refute a one-iterate substitute. Semilinear fixed-vector descent requires an algebraically closed/perfect ground field in the stated application. The exact ink exponent remains unresolved.

### CL-SA12-040

**Exact target:** For a proper connected reduced scheme over an algebraically closed field of characteristic p, H¹_et(X,F_p) is the F=1 subspace of H¹(X,O_X).

**Search batches:** web_batch_01.json, web_batch_02.json, web_batch_14.json, web_batch_17.json, web_batch_21.json, web_batch_23.json. **Opened reference keys:** StacksArtinSchreier.

**Result and limit:** The Artin–Schreier sequence and surjectivity of a↦a^p−a on the global constant field give exactly this identification. Without control of H⁰(O), a connecting term must be retained. This finite-level statement is independently checked from the long exact sequence.

### CL-SA12-041

**Exact target:** If R is a normal domain of characteristic p, then R^(1/p^ν)/R is torsion-free as an R-module.

**Search batches:** web_batch_01.json, web_batch_02.json, web_batch_14.json, web_batch_17.json, web_batch_21.json, web_batch_23.json. **Opened reference keys:** Stacks0AY6.

**Result and limit:** If r·b lies in R for nonzero r∈R and b∈R^(1/p^ν), then b lies in Frac(R) and is integral over R, hence b∈R by normality. This elementary integrality argument verifies the precise claim and yields injectivity on restriction to a dense open.

### CL-SA12-042

**Exact target:** For regular finite-type Y over a perfect field, Frobenius is finite flat; its iterated root quotient by O_Y is locally free and sections extend across a codimension-two complement.

**Search batches:** web_batch_01.json, web_batch_02.json, web_batch_14.json, web_batch_17.json, web_batch_21.json, web_batch_23.json. **Opened reference keys:** Stacks0EC0, Stacks0CC6, Stacks0AY6.

**Result and limit:** Finiteness follows from finite type over a perfect field, flatness from Kunz, and the quotient is locally free since the unit section is locally part of a basis. Reflexive extension on a normal scheme gives the codimension-two conclusion. Stacks tags 0EC0, 0CC6 and 0AY6 were opened for these distinct inputs. Normality of Y alone would not supply flat Frobenius.

### CL-SA12-043

**Exact target:** Spread the characteristic-zero proper birational situation to a finite-type integral arithmetic base; shrink to cohomological base-change loci and a constant-rank cokernel, then use positive-characteristic fibres to force that rank to vanish.

**Search batches:** web_batch_01.json, web_batch_02.json, web_batch_05.json, web_batch_06.json, web_batch_07.json, web_batch_08.json, web_batch_09.json, web_batch_14.json, web_batch_15.json, web_batch_16.json, web_batch_17.json, web_batch_18.json, web_batch_19.json, web_batch_21.json. **Opened reference keys:** Kleiman2005, Groth236, RuellingSaito2022.

**Result and limit:** The strategy is standard, but a proof must construct a model preserving the geometric assumptions, prove the relevant characteristic-p comparison, and justify base change and constant rank. The reviewed sources supply the tools, not a verification of every model choice on this page. It remains a bounded proof-completion task rather than a claimed new open theorem.

### CL-SA12-044

**Exact target:** For smooth proper models of a fixed function field, the Picard objects under discussion should agree birationally, with scheme-level τ invariance inherited from CL-SA12-033.

**Search batches:** web_batch_01.json, web_batch_02.json, web_batch_05.json, web_batch_06.json, web_batch_07.json, web_batch_08.json, web_batch_09.json, web_batch_14.json, web_batch_15.json, web_batch_16.json, web_batch_17.json, web_batch_18.json, web_batch_19.json, web_batch_21.json. **Opened reference keys:** KLOS, Kleiman2005, RuellingSaito2022.

**Result and limit:** Classical Picard/Albanese birational invariance and modern smooth proper torsion-Picard invariance are established. The precise nonreduced τ-scheme formulation still requires the full theorem and is not inferred from reduced varieties or from each Pic[n] group separately.

### CL-SA12-045

**Exact target:** Assuming a proper smooth model and the full scheme-level birational Pic^τ theorem, the directed system of Pic^τ along normal proper models is essentially constant.

**Search batches:** web_batch_01.json, web_batch_02.json, web_batch_05.json, web_batch_06.json, web_batch_07.json, web_batch_08.json, web_batch_09.json, web_batch_14.json, web_batch_15.json, web_batch_16.json, web_batch_17.json, web_batch_18.json, web_batch_19.json, web_batch_21.json. **Opened reference keys:** KLOS, Kleiman2005.

**Result and limit:** Normal closures of graphs give a cofinal subsystem mapping to the fixed smooth model; CL-SA12-033 then supplies the asserted isomorphisms. The cofinality argument is valid. This is explicitly conditional on the scheme theorem, and is distinct from the unconditional all-model question.

### CL-SA12-046

**Exact target:** Without a smooth proper model assumed, does the directed system of Pic^τ of proper normal models stabilize?

**Search batches:** web_batch_01.json, web_batch_02.json, web_batch_05.json, web_batch_06.json, web_batch_07.json, web_batch_08.json, web_batch_09.json, web_batch_14.json, web_batch_15.json, web_batch_16.json, web_batch_17.json, web_batch_18.json, web_batch_19.json, web_batch_21.json. **Opened reference keys:** KLOS, Kleiman2005, NeronSamuel1952.

**Result and limit:** Exact searches in Picard literature, arXiv, Numdam, zbMATH-targeted results and classical Albanese sources did not locate the all-model nonreduced τ-scheme stabilization statement. KLOS proves birational invariance and model realization for the reduced classical Picard variety Cl⁰, which is a weaker/different object. No current openness or novelty claim is inferred from the search failure.

### CL-SA12-047

**Exact target:** The proposed stabilization criterion uses uniform bounds on dimension, torsion and h¹(O) of model Picard schemes; the meaning of torsion is not specified securely.

**Search batches:** web_batch_01.json, web_batch_02.json, web_batch_05.json, web_batch_06.json, web_batch_07.json, web_batch_08.json, web_batch_09.json, web_batch_14.json, web_batch_15.json, web_batch_16.json, web_batch_17.json, web_batch_18.json, web_batch_19.json, web_batch_21.json. **Opened reference keys:** SGA3_VIII, Kleiman2005.

**Result and limit:** The chain α_{p^m} has constant dimension0, one geometric point and tangent dimension1 but unbounded scheme length. Thus bounds interpreted using geometric-point torsion do not imply stabilization. If torsion means the order of an entire finite subgroup scheme, this example does not meet a uniform bound. The word’s meaning must be read on the scan, and the special birational geometry remains separate.

### CL-SA12-048

**Exact target:** A uniform bound on h¹(X,O_X) gives a uniform bound on dim Pic_X because the tangent space of Pic_X at the identity is H¹(X,O_X).

**Search batches:** web_batch_01.json, web_batch_02.json, web_batch_05.json, web_batch_06.json, web_batch_07.json, web_batch_08.json, web_batch_09.json, web_batch_14.json, web_batch_15.json, web_batch_16.json, web_batch_17.json, web_batch_18.json, web_batch_19.json, web_batch_21.json. **Opened reference keys:** Kleiman2005, ConradPic.

**Result and limit:** The tangent-space identification and local dimension≤embedding dimension give the assertion. This does not bound infinitesimal length and does not prove stabilization. Kleiman’s Picard-scheme account and Conrad’s Picard handout supply the relevant infinitesimal framework.

### CL-SA12-049

**Exact target:** Dimensions of the Picard varieties of proper normal models of a fixed geometrically integral function field are uniformly bounded, by the rank of a fixed prime-to-characteristic abelianized π₁ quotient or by a fixed curve.

**Search batches:** web_batch_01.json, web_batch_02.json, web_batch_05.json, web_batch_06.json, web_batch_07.json, web_batch_08.json, web_batch_09.json, web_batch_14.json, web_batch_15.json, web_batch_16.json, web_batch_17.json, web_batch_18.json, web_batch_19.json, web_batch_21.json. **Opened reference keys:** KLOS, MoonenTateBT, Kleiman2005.

**Result and limit:** The corrected ℓ-adic argument requires ℓ≠p and the dual Tate-module identification. Independently, KLOS §§10.3.4–5 define a birationally invariant classical Picard variety and §10.3.13 bounds its dimension by the genus of a suitable complete-intersection curve. This controls the reduced dimension, not all nonreduced Picard structure.

### CL-SA12-050

**Exact target:** For the proper normal geometric setting and ℓ≠char(k), the rank of T_ℓ Pic⁰ equals twice the dimension of its reduced abelian variety; T_ℓ Pic is H¹_et(Z_ℓ(1)), dual to π₁^ab with a Tate twist.

**Search batches:** web_batch_01.json, web_batch_14.json, web_batch_21.json, web_batch_24.json, web_batch_25.json, web_batch_27.json. **Opened reference keys:** MoonenTateBT, Stacks03PK, Sutherland2012.

**Result and limit:** The prime-to-characteristic rank statement is standard abelian-variety theory; Moonen chapterX gives the dual Tate-module and fundamental-group statements, and Kummer gives the cohomological form. For ℓ=p it fails: the supersingular elliptic curve y²=x³−x over F₃ has p-rank0 and dimension1. The dual/twist distinction affects functoriality even though it leaves the rank unchanged. Sutherland2012, Introduction, gives the opened criterion #E(F_q)≡1 mod p for supersingularity, which verifies the p-rank interpretation of the saved point count.

### CL-SA12-051

**Exact target:** The reduction treats K⊗_k k̄ as a field under geometric normality alone.

**Search batches:** web_batch_01.json, web_batch_02.json, web_batch_14.json, web_batch_21.json, web_batch_24.json. **Opened reference keys:** KLOS, Kleiman2005.

**Result and limit:** C is geometrically normal over R, but C⊗_R C≅C×C. Geometric integrality, an appropriate constant-field assumption, or a chosen geometric component is necessary. The exact historical usage of normal sur k remains a contextual reading question.

### CL-SA12-052

**Exact target:** Find a direct genus bound for dimensions of Picard schemes over all proper normal models, avoiding the fundamental-group argument and not taking properness of Pic^τ as an input.

**Search batches:** web_batch_01.json, web_batch_02.json, web_batch_05.json, web_batch_06.json, web_batch_07.json, web_batch_08.json, web_batch_09.json, web_batch_14.json, web_batch_15.json, web_batch_16.json, web_batch_17.json, web_batch_18.json, web_batch_19.json, web_batch_21.json. **Opened reference keys:** KLOS, Kleiman2005, NeronSamuel1952.

**Result and limit:** KLOS §§10.3.4–5 and10.3.13 supply a precise classical-Picard route: Cl⁰ is birationally invariant and restricts with finite kernel to the Jacobian of a suitable complete-intersection curve contained in the nonsingular locus. This gives the desired numerical dimension bound once the comparison to each normal model’s reduced Picard variety is made. It does not prove nonreduced stabilization. Kleiman Remark5.8 records the related finite-kernel restriction issue and cautions that some proofs use compactness of Pic⁰.

### CL-SA12-053

**Exact target:** Tame coverings should satisfy the indicated fppf/fpqc descent and form the associated stack, under the boundary conventions of the reviewed manuscript.

**Search batches:** web_batch_04.json, web_batch_08.json, web_batch_13.json, web_batch_14.json, web_batch_15.json, web_batch_16.json, web_batch_17.json, web_batch_18.json, web_batch_19.json, web_batch_21.json. **Opened reference keys:** GM1971, SGA1_1971.

**Result and limit:** Grothendieck–Murre1971 has a chapter specifically on descent of tamely ramified coverings (pp110–121), verified at table-of-contents level. Full theorem text was not accessible, so the exact topology and boundary hypotheses of this request have not been matched. Ordinary finite-étale descent is not by itself a proof of every stated tame descent assertion.

### CL-SA12-054

**Exact target:** Supply compatible local Kummer equations and extend the ordinary Kummer algebra characterization to the generalized class needed in the formal argument.

**Search batches:** web_batch_04.json, web_batch_08.json, web_batch_13.json, web_batch_14.json, web_batch_15.json, web_batch_16.json, web_batch_17.json, web_batch_18.json, web_batch_19.json, web_batch_21.json. **Opened reference keys:** GM1971, Stacks0BSE, SGA1_1971.

**Result and limit:** The local tame Kummer mechanism and Abhyankar lemma are established; the published Grothendieck–Murre book opens with Kummer coverings (pp1–29). The exact generalized algebra characterization corresponding to draft2.1.8 was not checked in full text. Murre explicitly says the existing characterization is only for ordinary coverings, so the missing generalization is retained.

### CL-SA12-055

**Exact target:** Develop the requested Lefschetz variant for tame coverings of a divisor-complement pair.

**Search batches:** web_batch_04.json, web_batch_08.json, web_batch_13.json, web_batch_14.json, web_batch_15.json, web_batch_16.json, web_batch_17.json, web_batch_18.json, web_batch_19.json, web_batch_21.json. **Opened reference keys:** EK2016, EKerr2016, SGA1_1971.

**Result and limit:** Esnault–Kindler2016 Theorem1.1: for regular connected proper X over k, an SNC divisor D, and a suitable section Y transverse to D, Lef(X,Y) gives surjectivity of tame π₁; Leff plus meeting every effective divisor gives an isomorphism. Their broader normal-variety Theorem6.1 needs Y to be a complete intersection of ample divisors in good position, as the September2016 erratum states. These precise theorems answer standard forms of the request, not an unspecified strongest version.

### CL-SA12-056

**Exact target:** The requested local finite-generation statement is narrowed to the prime-to-p quotient in an abbreviated formal/local setting.

**Search batches:** web_batch_04.json, web_batch_08.json, web_batch_13.json, web_batch_14.json, web_batch_15.json, web_batch_16.json, web_batch_17.json, web_batch_18.json, web_batch_19.json, web_batch_21.json. **Opened reference keys:** GM1971, DegliseGabber2007.

**Result and limit:** The local geometric hypotheses are not specified sufficiently to identify a single theorem. Grothendieck–Murre’s final chapter concerns the punctured spectrum of a two-dimensional complete local ring; Déglise/Gabber Theorem1.4 gives finite H¹ for each finite G in a strict local normal excellent dimension-two setting, which is weaker than finite generation. Neither is silently substituted for the unexpanded request.

### CL-SA12-057

**Exact target:** A specialization path is encoded by a choice of lift of a geometric generization to a strict localization, giving the corresponding map of fibre functors/stalks; a product-of-fields description needs assumptions on that fibre.

**Search batches:** web_batch_04.json, web_batch_17.json, web_batch_20.json, web_batch_23.json. **Opened reference keys:** SGA1_1971, StacksSpecialization.

**Result and limit:** The étale fibre-functor construction and strict-localization description are established in SGA1 and the Stacks specialization discussion. Geometric specialization runs from the chosen generization lift toward the special point; the induced sheaf-stalk map runs from the special stalk to the generization stalk. Reversing either convention silently is not harmless. The unqualified product-of-fields assertion is not certified.

### CL-SA12-058

**Exact target:** An equivalence between the unnamed chapter-VII categories is conjectured.

**Search batches:** web_batch_01.json, web_batch_04.json, web_batch_10.json, web_batch_14.json, web_batch_15.json, web_batch_16.json, web_batch_19.json, web_batch_20.json, web_batch_23.json, web_batch_25.json. **Opened reference keys:** GM1971, SGA1_1971.

**Result and limit:** The categories are not defined in these leaves. Searching the published Grothendieck–Murre structure, EGA formal-étale comparisons and draft labels did not uniquely identify this equivalence. A published table of contents cannot settle it.

### CL-SA12-059

**Exact target:** Quasi-coherent modules are to glue across the intended square, with finite type, finite presentation and local freeness detected on the pieces.

**Search batches:** web_batch_01.json, web_batch_04.json, web_batch_10.json, web_batch_14.json, web_batch_15.json, web_batch_16.json, web_batch_19.json, web_batch_20.json, web_batch_23.json, web_batch_25.json. **Opened reference keys:** GM1971.

**Result and limit:** These are valid in several effective-descent and formal-patching settings, but false for arbitrary unspecified diagrams. Searches in EGA and the Grothendieck–Murre published structure did not recover the exact square. The absent hypotheses prevent a theorem-level fate assignment.

### CL-SA12-060

**Exact target:** A finite flat cover is asserted tame exactly when its restrictions to the pieces of the omitted gluing setup are tame.

**Search batches:** web_batch_01.json, web_batch_04.json, web_batch_10.json, web_batch_14.json, web_batch_15.json, web_batch_16.json, web_batch_19.json, web_batch_20.json, web_batch_23.json, web_batch_25.json. **Opened reference keys:** GM1971, Stacks0BSE.

**Result and limit:** Locality of tameness depends on valuations, normalizations and the cover topology; the unnamed gluing situation cannot be identified from this sentence. The published descent chapter is a relevant lead, not verification of this iff.

### CL-SA12-061

**Exact target:** A cancelled draft proposes inverse image for quasi-coherent stratified modules with a compatibility/lifting condition involving an unresolved m.u. abbreviation.

**Search batches:** web_batch_04.json, web_batch_05.json, web_batch_17.json, web_batch_19.json, web_batch_20.json, web_batch_23.json, web_batch_25.json. **Opened reference keys:** SGA1_1971.

**Result and limit:** No unique category or assertion is determined by the available words. Searches for stratified inverse-image and formal unramified lifting do not justify replacing the abbreviation by a guessed modern concept. Cancellation is recorded independently of mathematical truth.

### CL-SA12-062

**Exact target:** If the lifting phrase is read as unique deformation of an unramified object across a nilpotent thickening, that reading is too strong; formal unramifiedness gives uniqueness for maps to a fixed target.

**Search batches:** web_batch_04.json, web_batch_05.json, web_batch_17.json, web_batch_19.json, web_batch_20.json, web_batch_23.json, web_batch_25.json. **Opened reference keys:** StacksUnramified.

**Result and limit:** Spec(k) and Spec(k[ε]/ε²), each as an unramified scheme over Spec(k[ε]/ε²), restrict to the same closed-fibre object but are different lifts. Thus object-uniqueness cannot follow from unramifiedness alone. This tests a possible reading and does not refute the formally unramified morphism property.

### CL-SA12-063

**Exact target:** For a noetherian adic base S=Spec(V) complete and separated, a smooth finite-type group A with semiabelian identity component on the special fibre, isotrivial T₀ and algebraizable formal abelian quotient yields a Raynaud group whose identity component is an extension of B by T.

**Search batches:** web_batch_10.json, web_batch_16.json, web_batch_19.json. **Opened reference keys:** SGA7_IX.

**Result and limit:** The original SGA7 I ExposéIX7.2.2–7.2.5, printed pp406–407, gives the exact construction and corrects the draft splice: the full Raynaud group may have a finite étale component group, and the displayed torus-by-abelian extension is 0→T→(A^♮)⁰→B→0. The isotriviality insertion is retained. This is an exact visually checked counterpart, not an inferred thematic resemblance.

### CL-SA12-064

**Exact target:** The Raynaud group has a canonical formal-completion isomorphism with the original group along the special fibre, characterized by the coherent finite-level isomorphisms.

**Search batches:** web_batch_10.json, web_batch_16.json, web_batch_19.json. **Opened reference keys:** SGA7_IX.

**Result and limit:** SGA7 I IX7.2.3, p407, states the exact completion isomorphism; IX7.2.1 supplies full faithfulness of completion in the specified category. The printed proof leaves the direct full-faithfulness verification to the reader in7.2.1.4; this review verifies the statement match, not a full independent proof.

### CL-SA12-065

**Exact target:** The Raynaud group and its torus-by-abelian identity-component extension depend functorially on A and commute with base change induced by a homomorphism of noetherian adic rings.

**Search batches:** web_batch_10.json, web_batch_16.json, web_batch_19.json. **Opened reference keys:** SGA7_IX.

**Result and limit:** SGA7 I IX7.2.6, p407, states this functoriality and adic base-change compatibility exactly. The hypotheses of7.2.1–7.2.2 are retained; this is not an assertion about arbitrary formal groups or arbitrary maps without adic compatibility.

### CL-SA12-066

**Exact target:** For a finite locally free group H over the complete noetherian adic base in the Raynaud construction, H-torsors are equivalent to coherent systems of H_n-torsors, and this algebraizes the relevant finite-component extensions.

**Search batches:** web_batch_10.json, web_batch_16.json, web_batch_19.json. **Opened reference keys:** SGA7_IX.

**Result and limit:** SGA7 I IX7.2.1.3, printed p405, is the exact published torsor argument, followed on p406 by representability/descent for the resulting extension. The finiteness of H is essential; this statement is not generalized to arbitrary nonproper formal objects.

### CL-SA12-067

**Exact target:** The construction extends from complete traits/local bases to noetherian adic V; its key issue is algebraizing the formal abelian quotient, which the draft asserts under normality of S.

**Search batches:** web_batch_10.json, web_batch_16.json, web_batch_19.json. **Opened reference keys:** SGA7_IX.

**Result and limit:** SGA7 I IX7.1.5, p402, proves algebraizability and projectivity of the abelian quotient when S is normal. Remark7.1.6 on the same page says algebraizability also holds without normality, referring to13.5.3(a). This review read the proposition and remark but has not independently checked the cited reduction. IX7.2.1–7.2.6 supplies the general adic construction.

### CL-SA12-068

**Exact target:** Finite-order point-supported distributions carry the module structure dual to multiplication on the finite jet algebra; the induced coproduct and associativity identities are compatible with that action.

**Search batches:** web_batch_02.json, web_batch_05.json, web_batch_09.json, web_batch_19.json, web_batch_22.json, web_batch_24.json, web_batch_25.json, web_batch_26.json. **Opened reference keys:** Schwartz1947.

**Result and limit:** These are standard finite-jet duality identities, independently reconstructed from (A/m^(r+1))*. Searches for N°385 and the six printed-page fragments did not identify their source or establish a priority date. In particular Bourbaki talk385 is Raynaud’s different work and is not assigned as provenance. Class E describes the standard calculus, not an established date or authorship for the sheets. Schwartz1947–1948 §1, pp7–9, was opened as a primary historical source for distributions and multiplication by smooth functions; it does not identify these six sheets.

### CL-SA12-069

**Exact target:** Pushforward of a finite-order distribution under a smooth map satisfies the projection formula with pullback of functions, within the indicated differentiability/order range.

**Search batches:** web_batch_02.json, web_batch_05.json, web_batch_09.json, web_batch_19.json, web_batch_22.json, web_batch_24.json, web_batch_25.json, web_batch_26.json. **Opened reference keys:** Schwartz1947.

**Result and limit:** The formula follows directly from applying the functional to the product of a pulled-back function and a test function. The finite-jet proof is checked. Searches of the distribution literature and the unidentified sheet number did not recover an exact original source; the differentiability glyph remains undecided. Schwartz1947–1948 §1, pp7–9, was opened as a primary historical source for distributions and multiplication by smooth functions; it does not identify these six sheets.

### CL-SA12-070

**Exact target:** External products of point-supported distributions obey the tensor/module identity and the total-order filtration: orders i and j produce order at most i+j.

**Search batches:** web_batch_02.json, web_batch_05.json, web_batch_09.json, web_batch_19.json, web_batch_22.json, web_batch_24.json, web_batch_25.json, web_batch_26.json. **Opened reference keys:** Schwartz1947.

**Result and limit:** The total-order finite-jet construction proves the formula. The full rectangular tensor product of two order≤r spaces is not the same as total order≤r on the product; the modern reconstruction explicitly preserves this distinction. Source-identification searches remain negative. Schwartz1947–1948 §1, pp7–9, was opened as a primary historical source for distributions and multiplication by smooth functions; it does not identify these six sheets.

### CL-SA12-071

**Exact target:** First-order distributions annihilating constants identify with tangent vectors, equivalently derivations at the point or the dual of m/m².

**Search batches:** web_batch_02.json, web_batch_05.json, web_batch_09.json, web_batch_19.json, web_batch_22.json, web_batch_24.json, web_batch_25.json, web_batch_26.json. **Opened reference keys:** Schwartz1947.

**Result and limit:** The Leibniz rule exactly expresses vanishing on m², giving the standard tangent-space identification. The proof was independently repeated; the manuscript source remains unidentified despite searches. Schwartz1947–1948 §1, pp7–9, was opened as a primary historical source for distributions and multiplication by smooth functions; it does not identify these six sheets.

### CL-SA12-072

**Exact target:** The tangent map in local coordinates is represented by the Jacobian and obeys the chain rule.

**Search batches:** web_batch_02.json, web_batch_05.json, web_batch_09.json, web_batch_19.json, web_batch_22.json, web_batch_24.json, web_batch_25.json, web_batch_26.json. **Opened reference keys:** Schwartz1947.

**Result and limit:** This is the standard first-jet chain rule. The arbitrary symbolic-coordinate calculation was redone; no novel claim or historical priority is attributed to the unidentified reused pages. Schwartz1947–1948 §1, pp7–9, was opened as a primary historical source for distributions and multiplication by smooth functions; it does not identify these six sheets.

### CL-SA12-073

**Exact target:** Distributions carried by an embedded submanifold are characterized by annihilation of its defining ideal, with the appropriate finite-order quotient.

**Search batches:** web_batch_02.json, web_batch_05.json, web_batch_09.json, web_batch_19.json, web_batch_22.json, web_batch_24.json, web_batch_25.json, web_batch_26.json. **Opened reference keys:** Schwartz1947.

**Result and limit:** Duality of the quotient jet algebra identifies exactly the annihilator. This is independently checked in the finite-jet setting; global analytic formulations would require their own topology and regularity assumptions. The source attribution is unresolved. Schwartz1947–1948 §1, pp7–9, was opened as a primary historical source for distributions and multiplication by smooth functions; it does not identify these six sheets.

### CL-SA12-074

**Exact target:** For an abelian group M, D_S(M)=Spec(O_S[M]) represents the character functor Hom(M,O_T^×); for a general group the functor factors through abelianization.

**Search batches:** web_batch_04.json, web_batch_06.json, web_batch_12.json, web_batch_13.json. **Opened reference keys:** SGA3_VIII.

**Result and limit:** SGA3 VIII §1, especially1.1–1.4, is the exact published counterpart. The group-algebra Hopf structure and the character universal property are directly checked. The typed operator gaps in the archival witness remain unfilled.

### CL-SA12-075

**Exact target:** Formation of D_S(M) commutes with arbitrary base change.

**Search batches:** web_batch_04.json, web_batch_06.json, web_batch_12.json, web_batch_13.json. **Opened reference keys:** SGA3_VIII.

**Result and limit:** SGA3 VIII §1 proves this through the base-change identity for the group algebra. No flatness assumption on the base change is needed.

### CL-SA12-076

**Exact target:** The internal Hom between the indicated diagonalizable groups is representable under the stated finite-generation hypothesis on the relevant character group.

**Search batches:** web_batch_04.json, web_batch_06.json, web_batch_12.json, web_batch_13.json. **Opened reference keys:** SGA3_VIII.

**Result and limit:** The exact counterpart is SGA3 VIII1.5 and the reeditor’s expanded Proposition1.7. The opened reedition explicitly notes the original assertion/proof issue and supplies a finite-generation-sensitive treatment. A blanket representability claim for arbitrary character groups is not made.

### CL-SA12-077

**Exact target:** Character duality recovers M from D(M), and diagonalizable groups are reflexive under the relevant double-dual functor.

**Search batches:** web_batch_04.json, web_batch_06.json, web_batch_12.json, web_batch_13.json. **Opened reference keys:** SGA3_VIII.

**Result and limit:** SGA3 VIII §§1–2 gives the exact duality and biduality statements. The proof identifies group-like elements of the group algebra componentwise; its functorial setting matters over disconnected bases.

### CL-SA12-078

**Exact target:** For finite abelian T, D(T) is finite locally free of rank|T|. Over an algebraically closed field of characteristic p, its geometric points count only the prime-to-p part; equality with|T| requires p∤|T|.

**Search batches:** web_batch_04.json, web_batch_06.json, web_batch_12.json, web_batch_13.json. **Opened reference keys:** SGA3_VIII.

**Result and limit:** SGA3 VIII2.1 states the finite/smooth criteria. The example μ_p has length p and one geometric point, so group-scheme order cannot be replaced by point count. This distinction is relevant to the finite tame coefficient quotients on scan88.

### CL-SA12-079

**Exact target:** D_S(M) is flat, is of finite type when M is finitely generated, and has the smoothness/étaleness properties dictated by torsion orders being invertible on S.

**Search batches:** web_batch_04.json, web_batch_06.json, web_batch_12.json, web_batch_13.json. **Opened reference keys:** SGA3_VIII.

**Result and limit:** SGA3 VIII2.1 is the exact published statement; the opened text distinguishes finite type, finite, and smooth/étale criteria. The review does not fill the missing archival symbols by copying the printed text.

### CL-SA12-080

**Exact target:** An exact sequence of abelian character groups dualizes to an exact sequence of diagonalizable group schemes for the fpqc topology; the right-hand morphism is faithfully flat and quasi-compact.

**Search batches:** web_batch_04.json, web_batch_06.json, web_batch_12.json, web_batch_13.json. **Opened reference keys:** SGA3_VIII.

**Result and limit:** SGA3 VIII3.1 gives the exact theorem. A basis of the larger group algebra indexed by coset representatives proves faithful flatness over the smaller group algebra; kernel identification follows on characters. This algebraic proof was independently repeated.

### CL-SA12-081

**Exact target:** Let 𝔛 be regular connected noetherian formal, X₀ a regular Cartier special divisor, and X₀ plus the remaining divisors a normal-crossings boundary. Set U=X₀ minus the induced remaining boundary. The tame formal group maps onto π₁^t(U), with inertia I₀ a quotient of the prime-to-residue-characteristic roots-of-unity module μ.

**Search batches:** web_batch_01.json, web_batch_02.json, web_batch_04.json, web_batch_14.json, web_batch_15.json, web_batch_16.json, web_batch_17.json, web_batch_19.json, web_batch_21.json, web_batch_23.json, web_batch_28.json, web_batch_29.json, web_batch_30.json. **Opened reference keys:** GM1971, Stacks0BSE, SGA1_1971.

**Result and limit:** Grothendieck–Murre1971 has the exact object in chapters5 and7 (pp69–81 and97–109), verified from the publisher contents. The full theorem text was inaccessible; hence the precise generality and exceptional hypotheses of the draft have not been certified by that bibliographic match. Local Kummer theory supports the inertia mechanism; realization is separately recorded.

### CL-SA12-082

**Exact target:** The quotient action of π₁^t(U) on inertia is induced by the cyclotomic action on μ; the extension need not be central.

**Search batches:** web_batch_01.json, web_batch_02.json, web_batch_04.json, web_batch_14.json, web_batch_15.json, web_batch_16.json, web_batch_17.json, web_batch_19.json, web_batch_21.json, web_batch_23.json, web_batch_28.json, web_batch_29.json, web_batch_30.json. **Opened reference keys:** SGA7_IX, SGA1_1971, GM1971.

**Result and limit:** The roots-of-unity/cyclotomic action is standard tame inertia and is explicitly present in SGA7 I ExposéI §1. The formal setup has the same coefficient action. A tame S₃ extension over F₂((t)) gives a concrete noncentral instance; centrality holds only after trivializing the relevant action.

### CL-SA12-083

**Exact target:** For a finite constant prime-to-characteristic coefficient group J, H¹ on the universal tame pro-cover vanishes because each J-torsor is killed by a finite stage.

**Search batches:** web_batch_01.json, web_batch_02.json, web_batch_04.json, web_batch_14.json, web_batch_15.json, web_batch_16.json, web_batch_17.json, web_batch_19.json, web_batch_21.json, web_batch_23.json, web_batch_28.json, web_batch_29.json, web_batch_30.json. **Opened reference keys:** SGA1_1971, Milne2008.

**Result and limit:** This is the defining torsor-killing argument for a universal covering pro-object. It does not automatically extend to inverse limits of coefficient groups: continuous cohomology and possible lim¹ terms must be controlled. The finite-coefficient proof is independently repeated.

### CL-SA12-084

**Exact target:** An unqualified marginal suggestion that all higher cohomology vanishes on the tame universal cover of every smooth curve is too broad.

**Search batches:** web_batch_01.json, web_batch_02.json, web_batch_04.json, web_batch_14.json, web_batch_15.json, web_batch_16.json, web_batch_17.json, web_batch_19.json, web_batch_21.json, web_batch_23.json, web_batch_28.json, web_batch_29.json, web_batch_30.json. **Opened reference keys:** Milne2008, SGA1_1971, Stacks03PK.

**Result and limit:** For P¹ over an algebraically closed field and n invertible, π₁(P¹)=1 but H²(P¹,μ_n)≅Z/n, so its universal cover does not have the asserted vanishing. Later cote29 scan96, CodexK29-07 lines51–64, was read directly and explicitly excludes P¹ with empty boundary from the π₂-vanishing example. That later refinement does not decide the ink of the earlier margin. It also does not justify the separate later assertion that the inertia extension is trivial; the degree-one elliptic-line-bundle counterexample in formal_elliptic_nonsplitting.md addresses that assertion, recorded by root as CL-SA12-203.

### CL-SA12-085

**Exact target:** Under finite coefficients and a compatible tame étale homotopy framework, the degree-two term on the universal cover is related to Hom(π₂^t(U),J), and a low-degree spectral sequence compares it with group cohomology of π₁.

**Search batches:** web_batch_01.json, web_batch_02.json, web_batch_04.json, web_batch_14.json, web_batch_15.json, web_batch_16.json, web_batch_17.json, web_batch_19.json, web_batch_21.json, web_batch_23.json, web_batch_28.json, web_batch_29.json, web_batch_30.json. **Opened reference keys:** GM1971, Milne2008.

**Result and limit:** The π₂ reading is mathematically consistent with the intended H²/transgression mechanism; π₁ would conflict with the preceding H¹ vanishing. The precise tame homotopy model and profinite coefficient conventions are not defined here. Grothendieck–Murre’s comparison chapter is a relevant exact-object lead, but its theorem text was not accessible. No derived/project-context theorem is imported to fill the gap.

### CL-SA12-086

**Exact target:** The inertia group-extension class α maps to the Kummer Chern class β of the normal line bundle, with pushforward/restriction maps and a fixed normal-versus-conormal sign convention.

**Search batches:** web_batch_01.json, web_batch_02.json, web_batch_04.json, web_batch_14.json, web_batch_15.json, web_batch_16.json, web_batch_17.json, web_batch_19.json, web_batch_21.json, web_batch_23.json, web_batch_28.json, web_batch_29.json, web_batch_30.json. **Opened reference keys:** GM1971, Stacks03PK, Milne2008.

**Result and limit:** Grothendieck–Murre1971 chapter6, pp82–96, is explicitly titled Comparison of two 2-cohomology classes. A finite-level Čech calculation with chosen roots independently proves the indicated cocycle comparison once conventions and the extension model are fixed. It is not a proof of every pro-limit step. Murre’s cited Giraud letter is absent and not checked.

### CL-SA12-087

**Exact target:** The kernel of μ→I₀ is proposed to equal the image of the normal-bundle map from π₂^t(U); one containment follows from the Chern comparison, the other requires realizing finite quotients as inertia.

**Search batches:** web_batch_01.json, web_batch_02.json, web_batch_04.json, web_batch_14.json, web_batch_15.json, web_batch_16.json, web_batch_17.json, web_batch_19.json, web_batch_21.json, web_batch_23.json, web_batch_28.json, web_batch_29.json, web_batch_30.json. **Opened reference keys:** GM1971, Milne2008.

**Result and limit:** The published Grothendieck–Murre continuation treats the same inertia object, but its exact theorem hypotheses were not available. The draft’s reverse inclusion is not certified by the Chern identity alone. A degree-d line bundle over P¹ predicts the prime-to-p cyclic quotient of order the prime-to-p part of|d| for d≠0, and infinite procyclic inertia for d=0; this example remains conditional on the stated homotopy realization.

### CL-SA12-088

**Exact target:** For a fixed finite coefficient quotient, a class vanishing in the filtered limit over finite tame covers vanishes at one finite stage.

**Search batches:** web_batch_01.json, web_batch_02.json, web_batch_04.json, web_batch_14.json, web_batch_15.json, web_batch_16.json, web_batch_17.json, web_batch_19.json, web_batch_21.json, web_batch_23.json, web_batch_28.json, web_batch_29.json, web_batch_30.json. **Opened reference keys:** Milne2008, Stacks03PK.

**Result and limit:** This is the finite-level meaning of filtered-colimit vanishing. The stage may depend on the coefficient quotient. One finite cover generally cannot kill all levels simultaneously: pullback of a degree-one line bundle on an elliptic curve multiplies its degree by the finite cover degree, which cannot be divisible by every n. This distinction is independently checked.

### CL-SA12-089

**Exact target:** Every appropriate finite quotient J of μ/Imπ₂ should be realizable as inertia of a tame formal covering after a suitable finite tame base cover.

**Search batches:** web_batch_01.json, web_batch_02.json, web_batch_04.json, web_batch_14.json, web_batch_15.json, web_batch_16.json, web_batch_17.json, web_batch_19.json, web_batch_21.json, web_batch_23.json, web_batch_28.json, web_batch_29.json, web_batch_30.json. **Opened reference keys:** GM1971, Stacks04DY, Stacks03PK, Lipman1974.

**Result and limit:** The draft needs finite-stage vanishing, a root-line-bundle construction, effectiveness, and descent. The root-pair correction CL-SA12-093 repairs the finite-level Kummer step; it does not supply the entire realization theorem. Grothendieck–Murre chapters5–7 are the precise published-object comparison, but exact hypotheses remain unverified without full text.

### CL-SA12-090

**Exact target:** For regular X₀ and U obtained by deleting boundary Cartier divisors D_i, n-divisibility of a line bundle on U means that its class on X₀ is divisible by n modulo the subgroup generated by [D_i].

**Search batches:** web_batch_03.json, web_batch_14.json, web_batch_15.json, web_batch_16.json, web_batch_17.json, web_batch_19.json, web_batch_23.json, web_batch_24.json, web_batch_25.json, web_batch_26.json, web_batch_27.json. **Opened reference keys:** StacksDivisorLocalization, Stacks03PK.

**Result and limit:** The divisor-localization sequence for Picard groups gives the corrected boundary term. Extending a divisor from U proves the assertion on regular X₀; pairwise disjointness of the D_i is unnecessary for this isolated localization step. The earlier stronger conclusion without the boundary sum was cancelled.

### CL-SA12-091

**Exact target:** For n invertible, the kernel of Pic(𝔛)→Pic(X₀), or of Pic across a nilpotent thickening, is asserted uniquely n-divisible without properness/global-unit hypotheses.

**Search batches:** web_batch_03.json, web_batch_14.json, web_batch_15.json, web_batch_16.json, web_batch_17.json, web_batch_19.json, web_batch_23.json, web_batch_24.json, web_batch_25.json, web_batch_26.json, web_batch_27.json. **Opened reference keys:** Stacks0C6R, Stacks0C6S, Stacks04DY, Stacks03PK.

**Result and limit:** The explicit first-order deformation of E×G_m over C has ker Pic=H¹(O)/(Z·a), with nonzero n-torsion a/n mod Z·a. The formal deformation z_j=z_i exp(t a_ij) gives the same defect in a regular connected noetherian formal scheme with regular Cartier special fibre and no other boundary. Every hypothesis and the exact global-unit boundary image are checked. The opened Stacks tag0C6S currently contains the same unrestricted Pic[n] assertion; its proof omits the global-unit connecting contribution and is flagged as unreliable for this use. No novelty claim is made and no external edit was attempted. CL-SA12-093 is the corrected root-pair statement.

### CL-SA12-092

**Exact target:** The formal Picard group is identified with the inverse limit of Picard groups of infinitesimal thickenings.

**Search batches:** web_batch_03.json, web_batch_14.json, web_batch_15.json, web_batch_16.json, web_batch_17.json, web_batch_19.json, web_batch_23.json, web_batch_24.json, web_batch_25.json, web_batch_26.json, web_batch_27.json. **Opened reference keys:** Lipman1974.

**Result and limit:** Lipman1974 §2.4 explains surjectivity and the role of the Mittag–Leffler condition on global units for injectivity, within the proper setting of §2.2. Compatibility of chosen isomorphisms is essential; a possible lim¹ of units cannot be dropped in the unrestricted nonproper setup. The draft requires an explicit effectiveness/limit argument.

### CL-SA12-093

**Exact target:** Refinement supplied by this review: for n invertible and a nilpotent thickening X₀⊂X, the groupoid of specified nth-root pairs (M,φ:M^n≅L) for a fixed L on X is invariant under restriction, with compatible isomorphisms.

**Search batches:** web_batch_03.json, web_batch_14.json, web_batch_15.json, web_batch_16.json, web_batch_17.json, web_batch_19.json, web_batch_23.json, web_batch_24.json, web_batch_25.json, web_batch_26.json, web_batch_27.json. **Opened reference keys:** Stacks04DY, Stacks03PK, Stacks0C6R.

**Result and limit:** Topological invariance of the étale site and the étale μ_n-gerbe/root-pair description prove the finite-level statement; equivalently principal units have unique nth roots. This remains valid although the unframed Picard kernel can have n-torsion. Passing to an infinite formal system and algebraization is a separate question.

### CL-SA12-094

**Exact target:** Is pairwise disjointness of the induced boundary divisors necessary for the complete formal inertia-realization proof?

**Search batches:** web_batch_03.json, web_batch_14.json, web_batch_15.json, web_batch_16.json, web_batch_17.json, web_batch_19.json, web_batch_23.json, web_batch_24.json, web_batch_25.json, web_batch_26.json, web_batch_27.json. **Opened reference keys:** GM1971, Stacks0BSE, StacksDivisorLocalization.

**Result and limit:** It is unnecessary for the Picard localization step CL-SA12-090. Murre’s letter traces the assumption to the ordinary-Kummer restriction in draft7.1.5 used in9.3.3. The full generalized-Kummer replacement and realization theorem were not verified from the unavailable published chapter text; that is the exact remaining comparison, not an asserted obstruction.

### CL-SA12-095

**Exact target:** Murre uses the comparison between formal étale morphisms and coherent inductive systems of ordinary étale morphisms of the thickenings.

**Search batches:** web_batch_04.json, web_batch_14.json, web_batch_15.json, web_batch_16.json, web_batch_19.json, web_batch_23.json, web_batch_24.json, web_batch_25.json, web_batch_26.json. **Opened reference keys:** EGAI1960, Stacks04DY.

**Result and limit:** The cited EGA I10.12.3 is a precise source lead and the nilpotent étale equivalence is established in Stacks04DY. The exact EGA page and formal convention must be compared directly; this review records the foundational finite-level result and does not turn every formal object into an algebraic one.

### CL-SA12-096

**Exact target:** Formal étale neighbourhoods in the stated local setup are claimed locally to arise as completions of ordinary étale neighbourhoods; Murre identifies this as an input to the later lifting argument.

**Search batches:** web_batch_04.json, web_batch_14.json, web_batch_15.json, web_batch_16.json, web_batch_19.json, web_batch_23.json, web_batch_24.json, web_batch_25.json, web_batch_26.json. **Opened reference keys:** EGAI1960, Stacks04DY, StacksFormalEtale, GM1971.

**Result and limit:** Local étale lifting across nilpotent thickenings is established, and EGA’s formal-étale theory is the intended source. General algebraization of arbitrary formal morphisms is stronger and not inferred. Exact searches did not recover the draft1.1.13 hypotheses from the fragment or full published text.

### CL-SA12-097

**Exact target:** Murre asks for a characterization of the algebra of a generalized Kummer covering analogous to the existing ordinary-Kummer characterization.

**Search batches:** web_batch_01.json, web_batch_04.json, web_batch_05.json, web_batch_10.json, web_batch_14.json, web_batch_15.json, web_batch_16.json, web_batch_19.json, web_batch_23.json, web_batch_24.json, web_batch_25.json, web_batch_26.json. **Opened reference keys:** GM1971, Stacks0BSE.

**Result and limit:** Published Grothendieck–Murre chapter1 addresses Kummer coverings, and modern Abhyankar/Kummer local theory is established. The exact generalized characterization needed to remove disjointness in draft7.1.5 was not checked in accessible theorem text; the distinction remains explicit.

### CL-SA12-098

**Exact target:** Murre reports a delicate argument that the indicated geometric data determine the covering, requiring revision/verification.

**Search batches:** web_batch_01.json, web_batch_04.json, web_batch_05.json, web_batch_10.json, web_batch_14.json, web_batch_15.json, web_batch_16.json, web_batch_19.json, web_batch_23.json, web_batch_24.json, web_batch_25.json, web_batch_26.json. **Opened reference keys:** GM1971.

**Result and limit:** The referenced draft proposition is not reproduced, and its data/category cannot be uniquely reconstructed from the letter. Searches of the book structure and theorem numbers did not identify an exact theorem. This is retained as a historical proof task rather than replaced by a generic uniqueness theorem.

### CL-SA12-099

**Exact target:** The proof of preliminary proposition3.5.5 is only indicated.

**Search batches:** web_batch_01.json, web_batch_04.json, web_batch_05.json, web_batch_10.json, web_batch_14.json, web_batch_15.json, web_batch_16.json, web_batch_19.json, web_batch_23.json, web_batch_24.json, web_batch_25.json, web_batch_26.json. **Opened reference keys:** GM1971.

**Result and limit:** The proposition itself is absent from the supplied letter pages. The published book’s chapter numbering does not allow a unique match from this label alone. Search completed without identifying a statement to certify.

### CL-SA12-100

**Exact target:** A canonical-isomorphism assertion in preliminary8.1.6 is crucial for8.1.9(iii).

**Search batches:** web_batch_01.json, web_batch_04.json, web_batch_05.json, web_batch_10.json, web_batch_14.json, web_batch_15.json, web_batch_16.json, web_batch_19.json, web_batch_23.json, web_batch_24.json, web_batch_25.json, web_batch_26.json. **Opened reference keys:** GM1971.

**Result and limit:** Neither complete assertion is present in these pages; the number also has a competing reading in the editorial notes. The published comparison-of-classes/inertia chapters are relevant, but no theorem-level identity is asserted without the absent draft or full chapter text.

### CL-SA12-101

**Exact target:** Murre’s preliminary plumbing construction is intended to have a geometric interpretation; a chapter parallel to Mumford remains unwritten and later geometry is described as difficult.

**Search batches:** web_batch_01.json, web_batch_04.json, web_batch_05.json, web_batch_10.json, web_batch_14.json, web_batch_15.json, web_batch_16.json, web_batch_19.json, web_batch_23.json, web_batch_24.json, web_batch_25.json, web_batch_26.json. **Opened reference keys:** GM1971.

**Result and limit:** The supplied pages establish a circulation stage and an unfinished programme, not a uniquely specified algebraic theorem. Searches in the Grothendieck–Murre bibliography and book structure do not identify a completed theorem for this exact unwritten chapter. No modern logarithmic or anabelian project is substituted for it.

### CL-SA12-102

**Exact target:** The editorial notes request an explicit statement and placement of Abhyankar’s lemma and its local Kummer consequences.

**Search batches:** web_batch_01.json, web_batch_04.json, web_batch_05.json, web_batch_10.json, web_batch_14.json, web_batch_15.json, web_batch_16.json, web_batch_19.json, web_batch_23.json, web_batch_24.json, web_batch_25.json, web_batch_26.json. **Opened reference keys:** SGA1_1971, Stacks0BSE.

**Result and limit:** SGA1 XIII and Stacks58.31 give precise tame-ramification/Kummer statements. The mathematical lemma is established, but the correct insertion into the preliminary formal-covering manuscript is an editorial task, not a new theorem or a proof of every generalized formal version.

## Exact calls, returned sources and assessed results

### Batch 1

Initial targeted searches for constructibility over universally Japanese bases, exact birational Pic^tau invariance, Grothendieck–Murre9.2.3 and stationarity of birational fundamental groups. Déglise primary notes and SGA sources emerged; modern AI transcriptions were only leads.

```json
{
  "system1_search_query": [
    {
      "q": "SGA 4 direct image faisceaux ensembles constructibles universellement japonais f_* IX 2.14"
    },
    {
      "q": "Grothendieck birational invariance Pic tau normal regular H1 structure sheaf Picard scheme theorem"
    },
    {
      "q": "\"The tame fundamental group of a formal neighbourhood\" \"9.2.3\""
    },
    {
      "q": "\"birational\" \"fundamental group\" \"essentially constant\""
    }
  ],
  "response_length": "long"
}
```

Returned source records (titles and URLs; presence here alone does not certify opening or proof):

- Exposé IX · 2. Faisceaux constructibles — SGA 4 — https://grothendiecksga.com/read/sga4/fr/IX-2.html; retrieval ID `turn724516686search0`.

- 2. FAISCEAUX CONSTRUCTIBLES — https://www.normalesup.org/~forgogozo/SGA4/tomes/tome3.pdf; retrieval ID `turn724516686search4`.

- Exposé IX · 2. Constructible sheaves — SGA 4 — https://grothendiecksga.com/read/sga4/en/IX-2.html; retrieval ID `turn724516686search1`.

- 2  FRÉDÉRIC DÉGLISE — https://perso.ens-lyon.fr/frederic.deglise/docs/2007/gabber.pdf; retrieval ID `turn724516686search5`.

- Exposé XIV · 1. Théorème de finitude pour un morphisme propre. — SGA 4 — https://grothendiecksga.com/read/sga4/fr/XIV-1.html; retrieval ID `turn724516686search2`.

- SGA 2, Exposé XIII — Problems and conjectures | English Translation — https://jcreinhold.github.io/sga/ii/13-problems-and-conjectures.html; retrieval ID `turn724516686search3`.

- The Brauer–Grothendieck group — https://wwwf.imperial.ac.uk/~anskor/brauer.pdf; retrieval ID `turn724516686search6`.

- **Lemme 9.3.** — Supposons \(f\) universelleme — https://www.normalesup.org/~forgogozo/SGA4/08/08.pdf; retrieval ID `turn724516686search7`.

- Étale cohomology — https://en.wikipedia.org/wiki/%C3%89tale_cohomology; retrieval ID `turn724516686search8`.

- M. ARTIN, A. GROTHENDIECK, J.-L. VERDIER — https://media.githubusercontent.com/media/storagelfs/books/main/Pure%20Mathematics/Grothendieck/Grothiendieck.%20SGA%204.3.pdf; retrieval ID `turn724516686search9`.

### Batch 2

Alternative formulations of birational Picard invariance, formal tame comparison and point-supported distributions. No exact normal-source nonreduced Pic^tau theorem or N385 provenance was identified.

```json
{
  "system2_search_query": [
    {
      "q": "\"birational\" \"Picard scheme\" \"normal\" \"regular\""
    },
    {
      "q": "\"tame fundamental\" \"9.2.3\""
    },
    {
      "q": "\"birational fundamental group\" Grothendieck"
    },
    {
      "q": "\"distributions et vecteurs tangents\" Bourbaki"
    }
  ],
  "response_length": "long"
}
```

Returned source records (titles and URLs; presence here alone does not certify opening or proof):

- Introduction to birational anabelian geometry — https://library.slmath.org/books/Book59/files/20bog.pdf; retrieval ID `turn168918990search48`.

- The Grothendieck Conjecture on the Fundamental Groups of Algebraic Curves — https://citeseerx.ist.psu.edu/document?doi=a157bf626ca5071e25f9f3dbcbf50fcddac68f69&repid=rep1&type=pdf; retrieval ID `turn168918990search49`.

- INTRODUCTION TO BIRATIONAL ANABELIAN — https://math.nyu.edu/~tschinke/papers/yuri/10msri/msri7.pdf; retrieval ID `turn168918990search50`.

- On the Hom-form of Grothendieck’s birational — https://empslocal.ex.ac.uk/people/staff/ms220/Site/Publications_files/hom2.pdf; retrieval ID `turn168918990search51`.

- The pro-p Hom-form of the birational — https://faculty.lawrence.edu/corrys/wp-content/uploads/sites/4/2014/01/Corry-Pop_Revised.pdf; retrieval ID `turn168918990search52`.

- MFO Workshop: Homotopic & Geometric Galois Theory — https://pro.univ-lille.fr/fileadmin/user_upload/pages_pros/pierre_debes/V6-MFOreport2021.pdf; retrieval ID `turn168918990search53`.

- Exposé XIII · Problems related to local Picard groups — SGA 2 — https://grothendiecksga.com/read/sga2/en/XIII-5.html; retrieval ID `turn168918990search0`.

- The Picard Scheme — https://www.researchgate.net/publication/260022664_The_Picard_Scheme; retrieval ID `turn168918990search1`.

- GROTHENDIECK-SERRE CORRESPONDENCE — https://paperzz.com/doc/8948803/grothendieck-serre-correspondence; retrieval ID `turn168918990search2`.

- -------------------------------------------------------------------------------- — https://deposit.dnb.de/cgi-bin/dokserv?dok_ext=htm&dok_var=1&id=4024062&prov=M; retrieval ID `turn168918990search3`.

- Exposé XI · Projective spaces, unirational varieties — SGA 1 — https://grothendiecksga.com/read/sga1/en/XI-1.html; retrieval ID `turn168918990search4`.

- Ordinary varieties with trivial canonical bundle are not uniruled — https://link.springer.com/article/10.1007/s00208-021-02165-y; retrieval ID `turn168918990search5`.

- Birational anabelian Grothendieck Conjecture for curves over arbitrary cyclotomic extension fields of number fields — https://www.sciencedirect.com/science/article/pii/S0001870823005236; retrieval ID `turn168918990search6`.

- SGA 2, Exposé XIII — Problems and conjectures | English Translation — https://jcreinhold.github.io/sga/ii/13-problems-and-conjectures.html; retrieval ID `turn168918990search7`.

- Alexandre Grothendieck. A Mathematical Portrait - Schneps L. - 2014 — https://djvu.online/file/xSj2S14E8ZZOG; retrieval ID `turn168918990search8`.

- Fundamental Groups of Schemes · Stacks — https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/pione.html; retrieval ID `turn168918990search9`.

- Introduction to birational anabelian geometry — https://paperzz.com/doc/9186743/introduction-to-birational-anabelian-geometry; retrieval ID `turn168918990search10`.

- The Grothendieck conjecture for affine curves — https://www.cambridge.org/core/journals/compositio-mathematica/article/grothendieck-conjecture-for-affine-curves/1992BA14A2D63FA076DB39A34EC45E83; retrieval ID `turn168918990search11`.

- Singularities of local models — https://link.springer.com/article/10.1007/s00208-024-03036-y; retrieval ID `turn168918990search12`.

- ISBD view › Central Library, Shahjalal University of Science & Technology catalog — https://opac.library.sust.edu/cgi-bin/koha/opac-ISBDdetail.pl?biblionumber=45952; retrieval ID `turn168918990search13`.

- On the birational section conjecture over finitely generated fields — https://www.researchgate.net/publication/350698607_On_the_birational_section_conjecture_over_finitely_generated_fields; retrieval ID `turn168918990search14`.

- SGA 1, Exposé X — Theory of Specialization of the Fundamental Group | English Translation — https://jcreinhold.github.io/sga/i/10-specialization-of-the-fundamental-group.html; retrieval ID `turn168918990search15`.

- Specialization for the pro-étale fundamental group — https://www.cambridge.org/core/journals/compositio-mathematica/article/specialization-for-the-proetale-fundamental-group/9FF5AAC3BAFD65AA505EF8268C8641CB; retrieval ID `turn168918990search16`.

- The Picard group of the compactified universal Jacobian — https://www.researchgate.net/publication/45931337_The_Picard_group_of_the_compactified_universal_Jacobian; retrieval ID `turn168918990search17`.

- On the "Section Conjecture" in anabelian geometry — https://arxiv.org/abs/math/0305226; retrieval ID `turn168918990academia54`.

- Bounding geometrically integral del Pezzo surfaces — https://www.researchgate.net/publication/384923219_Bounding_geometrically_integral_del_Pezzo_surfaces; retrieval ID `turn168918990search18`.

- What Determines an Algebraic Variety? 9780691246833, 9780691246802 - DOKUMEN.PUB — https://dokumen.pub/what-determines-an-algebraic-variety-9780691246833-9780691246802.html; retrieval ID `turn168918990search19`.

- Birational geometry — https://en.wikipedia.org/wiki/Birational_geometry; retrieval ID `turn168918990search55`.

- Segre classes and integral dependence — https://link.springer.com/article/10.1007/s00208-026-03532-3; retrieval ID `turn168918990search20`.

- Recently Active 'picard-group' Questions - Page 3 - MathOverflow — https://mathoverflow.net/questions/tagged/picard-group?page=3&tab=active; retrieval ID `turn168918990search21`.

- The Birational Invariance of Fundamental Group Schemes — https://arxiv.org/abs/2604.23997; retrieval ID `turn168918990academia56`.

- Paper reviews, audits, and errata — https://www.daniellitt.com/published-paper-reviews.html; retrieval ID `turn168918990search22`.

- Maps between local Picard groups — https://www.researchgate.net/publication/264123244_Maps_between_local_Picard_groups; retrieval ID `turn168918990search23`.

- SGA 1, Exposé XI — Examples and Complements | English Translation — https://jcreinhold.github.io/sga/i/11-examples-and-complements.html; retrieval ID `turn168918990search24`.

- Alexander Grothendieck — https://en.wikipedia.org/wiki/Alexander_Grothendieck; retrieval ID `turn168918990search57`.

- Descent obstruction and fundamental exact sequence — https://arxiv.org/abs/1005.1302; retrieval ID `turn168918990academia58`.

- Anabelian geometry — https://en.wikipedia.org/wiki/Anabelian_geometry; retrieval ID `turn168918990search59`.

- Points rationnels et groupes fondamentaux : applications de la cohomologie $p$-adique — https://arxiv.org/abs/math/0303052; retrieval ID `turn168918990academia60`.

- New foundations for geometry — https://www.academia.edu/99190322/New_foundations_for_geometry; retrieval ID `turn168918990search25`.

- Jakob Stix — https://en.wikipedia.org/wiki/Jakob_Stix; retrieval ID `turn168918990search61`.

- Simone Diverio - A birational version of Gromov's Kähler hyperbolicity - YouTube — https://www.youtube.com/watch?v=tuS6nFa_5eM; retrieval ID `turn168918990youtube62`.

- 2026-27 Courses | Institut des sciences mathématiques — https://ism.uqam.ca/accueil/formation-courses/?language=default; retrieval ID `turn168918990search26`.

- Divisor (algebraic geometry) — https://en.wikipedia.org/wiki/Divisor_%28algebraic_geometry%29; retrieval ID `turn168918990search63`.

- Chaos Theory | PDF | Distribution (Mathématiques) | Transformation de Laplace — https://fr.scribd.com/document/422115498/chaos-theory; retrieval ID `turn168918990search27`.

- Complete algebraic curve — https://en.wikipedia.org/wiki/Complete_algebraic_curve; retrieval ID `turn168918990search64`.

- Rio de Janeiro 2024-06-24 Completo | PDF — https://www.scribd.com/document/772757520/Rio-de-Janeiro-2024-06-24-Completo-1; retrieval ID `turn168918990search28`.

### Batch 3

Opened Déglise Theorems1.1–1.4, LSS arXiv record, Stacks0C6S and Kleiman. The constructibility theorem is exact; Pic[n] invariance became a target for independent checking, not trusted background.

```json
{
  "open": [
    {
      "ref_id": "https://perso.ens-lyon.fr/frederic.deglise/docs/2007/gabber.pdf"
    },
    {
      "ref_id": "https://arxiv.org/html/2102.13424v2"
    },
    {
      "ref_id": "https://arxiv.org/abs/2303.11161"
    },
    {
      "ref_id": "https://stacks.math.columbia.edu/tag/0C6S"
    },
    {
      "ref_id": "https://arxiv.org/pdf/math/0504020"
    }
  ],
  "response_length": "long"
}
```

Returned source records (titles and URLs; presence here alone does not certify opening or proof):

- [2303.11161] Fundamental groups of proper varieties are finitely presented — https://arxiv.org/abs/2303.11161; retrieval ID `turn231756711view2`.

- Lemma 37.4.2 (0C6S)—The Stacks project — https://stacks.math.columbia.edu/tag/0C6S; retrieval ID `turn231756711view3`.

- -------------------------------------------------------------------------------- — https://arxiv.org/pdf/math/0504020; retrieval ID `turn231756711view4`.

Access failure occurred in this batch. The full diagnostic is preserved in the local raw record. No failed URL is represented as a checked theorem.

### Batch 4

Opened SGA1 primary reedition, SGA3 VIII primary reedition, ESS arXiv, Grothendieck–Murre publisher contents and Esnault–Kindler record. Bibliographic and theorem-text access are distinguished.

```json
{
  "open": [
    {
      "ref_id": "https://arxiv.org/abs/2102.13424"
    },
    {
      "ref_id": "https://arxiv.org/pdf/math/0206203"
    },
    {
      "ref_id": "https://www.wstein.org/sga/SGA3/Exp8-8nov09.pdf"
    },
    {
      "ref_id": "https://link.springer.com/book/10.1007/BFb0069608"
    },
    {
      "ref_id": "https://arxiv.org/abs/1509.08160"
    }
  ],
  "find": [
    {
      "ref_id": "turn231756711view4",
      "pattern": "birational"
    },
    {
      "ref_id": "turn231756711view4",
      "pattern": "Remark 5.8"
    },
    {
      "ref_id": "turn231756711view4",
      "pattern": "Exercise 6.13"
    }
  ],
  "response_length": "long"
}
```

Returned source records (titles and URLs; presence here alone does not certify opening or proof):

- [2102.13424] Finite presentation of the tame fundamental group — https://arxiv.org/abs/2102.13424; retrieval ID `turn581975326view0`.

- arXiv:math/0206203v2  [math.AG]  4 Jan 2004 — https://arxiv.org/pdf/math/0206203; retrieval ID `turn581975326view1`.

- -------------------------------------------------------------------------------- — https://www.wstein.org/sga/SGA3/Exp8-8nov09.pdf; retrieval ID `turn581975326view2`.

- The Tame Fundamental Group of a Formal Neighbourhood of a Divisor with Normal Crossings on a Scheme | Springer Nature Link — https://link.springer.com/book/10.1007/BFb0069608; retrieval ID `turn581975326view3`.

- [1509.08160] Lefschetz theorems for tamely ramified coverings — https://arxiv.org/abs/1509.08160; retrieval ID `turn581975326view4`.

- -------------------------------------------------------------------------------- — https://arxiv.org/pdf/math/0504020; retrieval ID `turn581975326view5`.

- -------------------------------------------------------------------------------- — https://arxiv.org/pdf/math/0504020; retrieval ID `turn581975326view6`.

- -------------------------------------------------------------------------------- — https://arxiv.org/pdf/math/0504020; retrieval ID `turn581975326view7`.

### Batch 5

Named-service searches including zbMATH, Numdam, MathOverflow and the alleged distribution/Bourbaki385 source. Found Picard bibliographic leads; no exact fate of the unrestricted model questions.

```json
{
  "system1_search_query": [
    {
      "q": "site:zbmath.org \"tame fundamental group\" Grothendieck Murre"
    },
    {
      "q": "site:numdam.org Grothendieck \"Picard\" \"birationnel\""
    },
    {
      "q": "site:mathoverflow.net \"fundamental group\" \"regular locus\" \"finitely generated\""
    },
    {
      "q": "\"Distributions et vecteurs tangents\" \"Bourbaki\""
    }
  ],
  "response_length": "long"
}
```

Returned source records (titles and URLs; presence here alone does not certify opening or proof):

- Numdam — https://www.numdam.org/; retrieval ID `turn220466055search0`.

- Technique de descente et théorèmes d'existence en géométrie algébrique. VI. Les schémas de Picard : propriétés générales — https://www.numdam.org/item/SB_1961-1962__7__221_0/; retrieval ID `turn220466055search1`.

- Technique de descente et théorèmes d'existence en géométrie algébrique. V. Les schémas de Picard : théorèmes d'existence — https://numdam.org/book-part/SB_1961-1962__7__143_0/; retrieval ID `turn220466055search2`.

- La variété de Picard d'une variété normale — https://www.numdam.org/article/AIF_1952__4__1_0.pdf; retrieval ID `turn220466055search7`.

- BULLETIN DE LA S. M. F. — https://www.numdam.org/item/10.24033/bsmf.1573.pdf; retrieval ID `turn220466055search8`.

- Recently Active 'fundamental-group' Questions - MathOverflow — https://mathoverflow.net/questions/tagged/fundamental-group?tab=Active; retrieval ID `turn220466055search3`.

- La variété de Picard d'une variété normale — https://www.numdam.org/item/AIF_1952__4__1_0/; retrieval ID `turn220466055search4`.

- The Picard group of a scheme over an Artin ring — https://www.numdam.org/item/PMIHES_1976__46__15_0/; retrieval ID `turn220466055search5`.

- Grothendieck and vanishing cycles — https://numdam.org/articles/10.5802/afst.1667/; retrieval ID `turn220466055search6`.

### Batch 6

Opened Bourbaki236 and Néron–Samuel metadata, SGA1 X finiteness/hyperplane passages and SGA3 Hom representability footnote. The Picard metadata is not an exact theorem proof.

```json
{
  "open": [
    {
      "ref_id": "turn581975326view3",
      "lineno": 48
    },
    {
      "ref_id": "turn581975326view0",
      "lineno": 8
    },
    {
      "ref_id": "turn581975326view4",
      "lineno": 8
    },
    {
      "ref_id": "turn231756711view4",
      "lineno": 2930
    },
    {
      "ref_id": "https://www.numdam.org/item/SB_1961-1962__7__221_0/"
    },
    {
      "ref_id": "https://www.numdam.org/item/AIF_1952__4__1_0/"
    }
  ],
  "find": [
    {
      "ref_id": "turn581975326view1",
      "pattern": "Théorème 2.12"
    },
    {
      "ref_id": "turn581975326view1",
      "pattern": "6.1"
    },
    {
      "ref_id": "turn581975326view1",
      "pattern": "3.4"
    },
    {
      "ref_id": "turn581975326view2",
      "pattern": "1.5"
    },
    {
      "ref_id": "turn581975326view2",
      "pattern": "3.1"
    }
  ],
  "response_length": "long"
}
```

Returned source records (titles and URLs; presence here alone does not certify opening or proof):

- The Tame Fundamental Group of a Formal Neighbourhood of a Divisor with Normal Crossings on a Scheme | Springer Nature Link — https://link.springer.com/book/10.1007/BFb0069608; retrieval ID `turn955962640view0`.

- [2102.13424] Finite presentation of the tame fundamental group — https://arxiv.org/abs/2102.13424; retrieval ID `turn955962640view1`.

- [1509.08160] Lefschetz theorems for tamely ramified coverings — https://arxiv.org/abs/1509.08160; retrieval ID `turn955962640view2`.

- -------------------------------------------------------------------------------- — https://arxiv.org/pdf/math/0504020; retrieval ID `turn955962640view3`.

- Technique de descente et théorèmes d'existence en géométrie algébrique. VI. Les schémas de Picard : propriétés générales — https://www.numdam.org/item/SB_1961-1962__7__221_0/; retrieval ID `turn955962640view4`.

- La variété de Picard d'une variété normale — https://www.numdam.org/item/AIF_1952__4__1_0/; retrieval ID `turn955962640view5`.

- arXiv:math/0206203v2  [math.AG]  4 Jan 2004 — https://arxiv.org/pdf/math/0206203; retrieval ID `turn955962640view6`.

- arXiv:math/0206203v2  [math.AG]  4 Jan 2004 — https://arxiv.org/pdf/math/0206203; retrieval ID `turn955962640view7`.

- arXiv:math/0206203v2  [math.AG]  4 Jan 2004 — https://arxiv.org/pdf/math/0206203; retrieval ID `turn955962640view8`.

- -------------------------------------------------------------------------------- — https://www.wstein.org/sga/SGA3/Exp8-8nov09.pdf; retrieval ID `turn955962640view9`.

- -------------------------------------------------------------------------------- — https://www.wstein.org/sga/SGA3/Exp8-8nov09.pdf; retrieval ID `turn955962640view10`.

### Batch 7

Read ESS and Esnault–Kindler precise scope, Grothendieck–Murre chapter structure, and Kleiman Remark5.8. Finite-kernel curve restriction is weaker than an arbitrary nonreduced birational Picard isomorphism.

```json
{
  "find": [
    {
      "ref_id": "turn581975326view0",
      "pattern": "Abstract"
    },
    {
      "ref_id": "turn581975326view4",
      "pattern": "Abstract"
    },
    {
      "ref_id": "turn581975326view3",
      "pattern": "Comparison"
    },
    {
      "ref_id": "turn231756711view4",
      "pattern": "compactness"
    }
  ],
  "response_length": "long"
}
```

Returned source records (titles and URLs; presence here alone does not certify opening or proof):

- [2102.13424] Finite presentation of the tame fundamental group — https://arxiv.org/abs/2102.13424; retrieval ID `turn192748983view0`.

- [1509.08160] Lefschetz theorems for tamely ramified coverings — https://arxiv.org/abs/1509.08160; retrieval ID `turn192748983view1`.

- The Tame Fundamental Group of a Formal Neighbourhood of a Divisor with Normal Crossings on a Scheme | Springer Nature Link — https://link.springer.com/book/10.1007/BFb0069608; retrieval ID `turn192748983view2`.

- -------------------------------------------------------------------------------- — https://arxiv.org/pdf/math/0504020; retrieval ID `turn192748983view3`.

### Batch 8

Followed author/bibliography leads to KLOS and Rülling–Saito. Their smooth/classical Picard results were separated from the manuscript normal-source infinitesimal problem.

```json
{
  "system1_search_query": [
    {
      "q": "\"Picard scheme\" \"birational invariance\" normal"
    },
    {
      "q": "\"Pic\" \"tau\" \"birational\" Grothendieck normal"
    },
    {
      "q": "\"H^1\" \"birational\" \"normal\" \"smooth\" Picard"
    },
    {
      "q": "\"fundamental group\" \"models\" \"essentially constant\""
    }
  ],
  "response_length": "long"
}
```

Returned source records (titles and URLs; presence here alone does not certify opening or proof):

- SGA 1, Exposé XI — Examples and Complements | English Translation — https://jcreinhold.github.io/sga/i/11-examples-and-complements.html; retrieval ID `turn198160574search0`.

- On the cohomology of reciprocity sheaves — https://www.cambridge.org/core/journals/forum-of-mathematics-sigma/article/on-the-cohomology-of-reciprocity-sheaves/B934B4AE25F5D69369B8C868BCF4B1BB; retrieval ID `turn198160574search1`.

- The Brauer–Grothendieck group — https://wwwf.imperial.ac.uk/~anskor/brauer.pdf; retrieval ID `turn198160574search7`.

- 10.3. PICARD GROUP, CLASS GROUP AND ALBANESE VARIETY 177 — https://williamsawin.com/ReconstructionBook.pdf; retrieval ID `turn198160574search8`.

- The Picard functor and the Picard scheme of a curve — https://openmaths.org/courses/AG-GS/prerequisites/AG-HP/the-picard-functor-and-the-picard-scheme-of-a-curve.html; retrieval ID `turn198160574search2`.

- The Picard Scheme — https://www.researchgate.net/publication/260022664_The_Picard_Scheme; retrieval ID `turn198160574search3`.

- A characterization of ordinary abelian varieties by the Frobenius push-forward of the structure sheaf — https://link.springer.com/article/10.1007/s00208-015-1352-3; retrieval ID `turn198160574search4`.

- algebraic geometry - Picard group of product of spaces - Mathematics Stack Exchange — https://math.stackexchange.com/questions/493005/picard-group-of-product-of-spaces/1674937; retrieval ID `turn198160574search5`.

- Compact Manifold - an overview | ScienceDirect Topics — https://www.sciencedirect.com/topics/mathematics/compact-manifold; retrieval ID `turn198160574search6`.

### Batch 9

Further MathOverflow/zbMATH and N385 queries gave no exact theorem or source identification. This is a bounded negative search, not evidence of novelty or current openness.

```json
{
  "system1_search_query": [
    {
      "q": "site:mathoverflow.net \"kernel\" \"fundamental group\" \"singular\" \"finitely generated\""
    },
    {
      "q": "site:arxiv.org \"étale\" \"birational\" \"Picard\" \"normal\""
    },
    {
      "q": "site:zbmath.org \"Grothendieck\" \"Murre\" \"208\""
    },
    {
      "q": "\"Bourbaki\" \"385\" distributions"
    }
  ],
  "response_length": "long"
}
```

Returned source records (titles and URLs; presence here alone does not certify opening or proof):

- at.algebraic topology - Cohomology class of the group extension from a principal bundle - MathOverflow — https://mathoverflow.net/questions/171622/cohomology-class-of-the-group-extension-from-a-principal-bundle; retrieval ID `turn364350923search0`.

- Newest 'galois-groups' Questions - MathOverflow — https://mathoverflow.net/questions/tagged/galois-groups?tab=Newest; retrieval ID `turn364350923search1`.

- ag.algebraic geometry - Examples where it's useful to know that a mathematical object belongs to some family of objects - MathOverflow — https://mathoverflow.net/questions/74214/examples-where-its-useful-to-know-that-a-mathematical-object-belongs-to-some-fa/75154; retrieval ID `turn364350923search2`.

- Compactification du module des courbes — https://www.numdam.org/item/SB_1970-1971__13__47_0/; retrieval ID `turn364350923search3`.

- SÉMINAIRE N. BOURBAKI — https://www.numdam.org/article/SB_1970-1971__13__47_0.pdf; retrieval ID `turn364350923search5`.

- SÉMINAIRE N. BOURBAKI — https://www.numdam.org/article/SB_1964-1966__9__385_0.pdf; retrieval ID `turn364350923search6`.

- SÉMINAIRE N. BOURBAKI — https://www.numdam.org/article/SB_1962-1964__8__385_0.pdf; retrieval ID `turn364350923search7`.

- Séminaire BOURBAKI, 1948/49 à 2025/26 — https://bourbaki.fr/table.pdf; retrieval ID `turn364350923search8`.

- Is every virtual knot group an HNN extension? - MathOverflow — https://mathoverflow.net/questions/54549/is-every-virtual-knot-group-an-hnn-extension/54566; retrieval ID `turn364350923search4`.

### Batch 10

Opened tame-ramification and proper-homotopy framework; found SGA7 and author bibliography leads. An AI transcription of SGA7 was not accepted as primary proof evidence.

```json
{
  "system1_search_query": [
    {
      "q": "site:stacks.math.columbia.edu \"geometrically reduced\" \"generic\" \"fundamental\""
    },
    {
      "q": "site:stacks.math.columbia.edu \"constructible\" \"Hom\" \"finite\" \"sheaves\""
    },
    {
      "q": "\"SGA 7\" \"7.2.5\" \"Raynaud\""
    },
    {
      "q": "\"Lefschetz theorems for tamely ramified coverings\" published"
    }
  ],
  "response_length": "long"
}
```

Returned source records (titles and URLs; presence here alone does not certify opening or proof):

- Section 58.30 (0BUQ): Specialization maps in the smooth proper case—The Stacks project — https://stacks.math.columbia.edu/tag/0BUQ; retrieval ID `turn153152310search0`.

- FUNDAMENTAL GROUPS OF SCHEMES 39 — https://stacks.math.columbia.edu/download/pione.pdf; retrieval ID `turn153152310search7`.

- Section 58.15 (0BUM): Homotopy exact sequence—The Stacks project — https://stacks.math.columbia.edu/tag/0BUM; retrieval ID `turn153152310search1`.

- Section 61.29 (09C0): A suitable derived category—The Stacks project — https://stacks.math.columbia.edu/tag/09C0; retrieval ID `turn153152310search2`.

- Section 33.6 (035U): Geometrically reduced schemes—The Stacks project — https://stacks.math.columbia.edu/tag/035U; retrieval ID `turn153152310search3`.

- Exposé IX · 7. The Raynaud extension G over S attached to the abelian scheme A_K with semi-stable reduction. Duality of the abelian schemes B,B' over S. — SGA 7 — https://grothendiecksga.com/read/sga7/en/9-7.html; retrieval ID `turn153152310search4`.

- Lefschetz theorems for tamely ramified coverings — https://arxiv.org/abs/1509.08160; retrieval ID `turn153152310academia8`.

- Esnault: Publications — https://page.mi.fu-berlin.de/esnault/helene_publ.html; retrieval ID `turn153152310search5`.

- Vol. 144, No. 12, December 2016 of Proceedings of the American Mathematical Society | JSTOR — https://www.jstor.org/stable/procamermathsoci.144.issue-12; retrieval ID `turn153152310search6`.

### Batch 11

Opened author publication list and followed ESS/LSS primary links. Used this to check stronger modern finiteness assertions in the earlier context.

```json
{
  "system2_search_query": [
    {
      "q": "SGA 7 I pdf \"Raynaud\" \"7.2.2\""
    },
    {
      "q": "SGA 1 IX 6.1 6.2 \"séparable\""
    },
    {
      "q": "\"Picard\" \"birationnelle\" \"tau\""
    },
    {
      "q": "\"Finite presentation of the tame fundamental group\" 2022"
    }
  ],
  "open": [
    {
      "ref_id": "https://page.mi.fu-berlin.de/esnault/helene_publ.html"
    }
  ],
  "response_length": "long"
}
```

Returned source records (titles and URLs; presence here alone does not certify opening or proof):

- Finite presentation of the tame fundamental group — https://researchconnect.suny.edu/en/publications/finite-presentation-of-the-tame-fundamental-group/; retrieval ID `turn759777763search0`.

- Finite presentation of the tame fundamental group — https://researchconnect.buffalo.edu/en/publications/finite-presentation-of-the-tame-fundamental-group/; retrieval ID `turn759777763search1`.

- Finite presentation of the tame fundamental group — https://weizmann.elsevierpure.com/en/publications/finite-presentation-of-the-tame-fundamental-group/; retrieval ID `turn759777763search2`.

- Finite presentation of the tame fundamental group — https://dialnet.unirioja.es/servlet/articulo?codigo=8236816; retrieval ID `turn759777763search3`.

- Finite presentation of the tame fundamental group — https://cris.iucc.ac.il/en/publications/finite-presentation-of-the-tame-fundamental-group/; retrieval ID `turn759777763search4`.

- Crossmark — https://crossmark.crossref.org/dialog/?doi=10.1007%2Fs00029-021-00732-4; retrieval ID `turn759777763search5`.

- Finite presentation of the tame fundamental group — https://arxiv.org/abs/2102.13424; retrieval ID `turn759777763academia47`.

- fundamental group — https://etd.adm.unipi.it/t/etd-09062023-171300/; retrieval ID `turn759777763search6`.

- École doctorale de Sciences Mathématiques de Paris Centre — https://theses.fr/2022SORUS294.pdf; retrieval ID `turn759777763search48`.

- FINITe PRESENTATION OF THE TAME FUNDAMENTAL GROUP — https://page.mi.fu-berlin.de/esnault/preprints/helene/141_ess.pdf; retrieval ID `turn759777763search49`.

- SGA 1, Exposé IX — Descent of Étale Morphisms. Application to the Fundamental Group | English Translation — https://jcreinhold.github.io/sga/i/09-descent-of-etale-morphisms.html; retrieval ID `turn759777763search7`.

- Esnault: Publications — https://page.mi.fu-berlin.de/esnault/helene_publ.html; retrieval ID `turn759777763search8`.

- ANNALES DE L’INSTITUT FOURIER — https://www.numdam.org/item/10.5802/aif.1069.pdf; retrieval ID `turn759777763search50`.

- Fundamental groups of proper varieties are finitely presented — https://comptes-rendus.academie-sciences.fr/mathematique/articles/10.5802/crmath.518/; retrieval ID `turn759777763search9`.

- Dr. Mark Shusterman | Weizmann Institute of Science — https://www.weizmann.ac.il/pages/people/76240; retrieval ID `turn759777763search10`.

- Volume 28, Issue 2 (May) (2022) — Selecta Mathematica | DeepDyve — https://www.deepdyve.com/browse/journals/1022-1824/2022/v28/i2?rows=10&start=0; retrieval ID `turn759777763search11`.

- Glossary français → English — SGA (Séminaire de Géométrie Algébrique du Bois-Marie) — https://grothendiecksga.com/glossary.html; retrieval ID `turn759777763search12`.

- - Geometria_Pisa - Mailing list — Dipartimento di Matematica, UniPI — https://lists.dm.unipi.it/hyperkitty/list/geometria_pisa%40lists.dm.unipi.it/latest?count=200&page=2; retrieval ID `turn759777763search13`.

- 444.dvi — https://www.math.uni-bielefeld.de/lag/man/444.pdf; retrieval ID `turn759777763search51`.

- M. ARTIN, A. GROTHENDIECK, J.-L. VERDIER — https://media.githubusercontent.com/media/storagelfs/books/main/Pure%20Mathematics/Grothendieck/Grothiendieck.%20SGA%204.3.pdf; retrieval ID `turn759777763search52`.

- SGA 1 Par A. Grothendieck | PDF | Groupe (Mathématiques) | Structures mathématiques — https://fr.scribd.com/document/746087845/SGA-1-par-A-Grothendieck; retrieval ID `turn759777763search14`.

- 12) “Stratified vector bundles on simply connected varieties in positive characteristic p > 0”, IMU Special seminar, RIMS, Kyoto, Japan, 4th April, 2016. — https://twas.org/sites/default/files/cv/cv-2025-vasudevan-srinivas.pdf; retrieval ID `turn759777763search53`.

- Finite presentation of the tame fundamental group -- Hélène Esnault (Freie Universität Berlin) - YouTube — https://www.youtube.com/watch?v=0vHLOJzfgSI; retrieval ID `turn759777763youtube54`.

- SGA 1, Exposé X — Theory of Specialization of the Fundamental Group | English Translation — https://jcreinhold.github.io/sga/i/10-specialization-of-the-fundamental-group.html; retrieval ID `turn759777763search15`.

- Motivic and $$\ell $$ -adic realizations of the category of singularities of the zero locus of a global section of a vector bundle — https://link.springer.com/article/10.1007/s00029-021-00734-2; retrieval ID `turn759777763search16`.

- Exposé XII · 7. Comments on the conditions of validity of the Lefschetz formula. — SGA 5 — https://grothendiecksga.com/read/sga5/en/XII-7.html; retrieval ID `turn759777763search17`.

- Categorification of Intersection Product | PDF | Category Theory | Functions And Mappings — https://www.scribd.com/document/962145614/2511-10527v1; retrieval ID `turn759777763search18`.

- Exposé X · The homotopy exact sequence for a proper and separable morphism — SGA 1 — https://grothendiecksga.com/read/sga1/en/X-1.html; retrieval ID `turn759777763search19`.

- Esnault: Publications — https://page.mi.fu-berlin.de/esnault/helene_publ.html; retrieval ID `turn759777763view0`.

### Batch 12

Opened ESS author PDF and SGA3 exactness passages. LSS publisher URL returned403; its arXiv record remained available. The failed publisher access is not labelled a checked proof.

```json
{
  "find": [
    {
      "ref_id": "turn759777763view0",
      "pattern": "118."
    },
    {
      "ref_id": "turn581975326view2",
      "pattern": "Théorème 3.1"
    },
    {
      "ref_id": "turn581975326view1",
      "pattern": "6.1."
    }
  ],
  "open": [
    {
      "ref_id": "https://comptes-rendus.academie-sciences.fr/mathematique/articles/10.5802/crmath.518/"
    },
    {
      "ref_id": "https://page.mi.fu-berlin.de/esnault/preprints/helene/141_ess.pdf"
    },
    {
      "ref_id": "https://www.numdam.org/item/SB_1961-1962__7__221_0/"
    }
  ],
  "response_length": "long"
}
```

Returned source records (titles and URLs; presence here alone does not certify opening or proof):

- -------------------------------------------------------------------------------- — https://page.mi.fu-berlin.de/esnault/preprints/helene/141_ess.pdf; retrieval ID `turn558723927view1`.

- Technique de descente et théorèmes d'existence en géométrie algébrique. VI. Les schémas de Picard : propriétés générales — https://www.numdam.org/item/SB_1961-1962__7__221_0/; retrieval ID `turn558723927view2`.

- Esnault: Publications — https://page.mi.fu-berlin.de/esnault/helene_publ.html; retrieval ID `turn558723927view3`.

- -------------------------------------------------------------------------------- — https://www.wstein.org/sga/SGA3/Exp8-8nov09.pdf; retrieval ID `turn558723927view4`.

- arXiv:math/0206203v2  [math.AG]  4 Jan 2004 — https://arxiv.org/pdf/math/0206203; retrieval ID `turn558723927view5`.

Access failure occurred in this batch. The full diagnostic is preserved in the local raw record. No failed URL is represented as a checked theorem.

### Batch 13

Opened SGA3 VIII§§2–3, SGA1 X2.8–2.12, KLOS, Rülling–Saito Cor11.24, Esnault–Kindler and its erratum. Exact good-compactification, smooth/fibred, Lef/Leff and ample-complete-intersection hypotheses retained.

```json
{
  "click": [
    {
      "ref_id": "turn759777763view0",
      "id": 115
    },
    {
      "ref_id": "turn759777763view0",
      "id": 116
    },
    {
      "ref_id": "turn558723927view2",
      "id": 13
    }
  ],
  "open": [
    {
      "ref_id": "turn581975326view2",
      "lineno": 430
    },
    {
      "ref_id": "turn581975326view1",
      "lineno": 11845
    },
    {
      "ref_id": "https://williamsawin.com/ReconstructionBook.pdf"
    },
    {
      "ref_id": "https://www.cambridge.org/core/journals/forum-of-mathematics-sigma/article/on-the-cohomology-of-reciprocity-sheaves/B934B4AE25F5D69369B8C868BCF4B1BB"
    }
  ],
  "response_length": "long"
}
```

Returned source records (titles and URLs; presence here alone does not certify opening or proof):

- arXiv:math/0206203v2  [math.AG]  4 Jan 2004 — https://arxiv.org/pdf/math/0206203; retrieval ID `turn641590707view1`.

- -------------------------------------------------------------------------------- — https://williamsawin.com/ReconstructionBook.pdf; retrieval ID `turn641590707view2`.

- On the cohomology of reciprocity sheaves | Forum of Mathematics, Sigma | Cambridge Core — https://www.cambridge.org/core/journals/forum-of-mathematics-sigma/article/on-the-cohomology-of-reciprocity-sheaves/B934B4AE25F5D69369B8C868BCF4B1BB; retrieval ID `turn641590707view3`.

- pdf — https://page.mi.fu-berlin.de/esnault/preprints/helene/118-EK.pdf; retrieval ID `turn641590707view4`.

- pdf — https://page.mi.fu-berlin.de/esnault/preprints/helene/118b-EK.pdf; retrieval ID `turn641590707view5`.

- MathSciNet — https://mathscinet.ams.org/mathscinet-getitem?mr=1611207 ; rewritten summary of https://mathscinet.ams.org/mathscinet/relay-station?mr=1611207; retrieval ID `turn641590707view6`.

### Batch 14

Targeted Picard and formal-comparison searches followed by KLOS10.3.4–5,10.3.9,10.3.13. Classical birational Cl0 and the normal morphism-Albanese were distinguished; no nonreduced stabilization conclusion inferred.

```json
{
  "open": [
    {
      "ref_id": "turn641590707view5"
    },
    {
      "ref_id": "turn558723927view2",
      "lineno": 65
    }
  ],
  "find": [
    {
      "ref_id": "turn641590707view2",
      "pattern": "10.3.4"
    },
    {
      "ref_id": "turn641590707view3",
      "pattern": "11.24"
    },
    {
      "ref_id": "turn231756711view4",
      "pattern": "birationally"
    }
  ],
  "system2_search_query": [
    {
      "q": "\"Picard\" \"proper birational\" \"normal\" \"regular\" scheme"
    },
    {
      "q": "\"SGA 7\" \"Raynaud\" \"7.2.2\" pdf"
    },
    {
      "q": "\"Grothendieck Murre\" \"9.2.3\" pdf"
    },
    {
      "q": "\"schémas de Picard\" \"birationnel\" \"4.12\""
    }
  ],
  "response_length": "long"
}
```

Returned source records (titles and URLs; presence here alone does not certify opening or proof):

- Picard schemes of formal schemes; application to rings with discrete divisor class group — https://www.math.purdue.edu/~jlipman/papers-older/%5B1974%5D%20Picard%20schemes%20of%20formal%20schemes%3A%20application%20to%20rings%20with%20discrete%20divisor%20class%20group.pdf; retrieval ID `turn168732812search45`.

- Letter to H. Hironaka — https://csg.igrothendieck.org/wp-content/uploads/2024/04/L27d.pdf; retrieval ID `turn168732812search46`.

- Exposé IX · 7. The Raynaud extension G over S attached to the abelian scheme A_K with semi-stable reduction. Duality of the abelian schemes B,B' over S. — SGA 7 — https://grothendiecksga.com/read/sga7/en/9-7.html; retrieval ID `turn168732812search0`.

- ag.algebraic geometry - Picard groups, ample cones, and proper birational maps - MathOverflow — https://mathoverflow.net/questions/221883/picard-groups-ample-cones-and-proper-birational-maps; retrieval ID `turn168732812search1`.

- Suppose now by contradiction that \(X\) is not rational. By the classification of log canonical singularities [Kol13, Corollary 3.39], the exceptional divisor \(E\) is either an elliptic curve, a nodal curve or a circle of smooth rational curves. In the first case \(\mathrm{Pic}^0(E)\simeq E(k)\), while in the latter cases \(\mathrm{Pic}^0(E)\simeq k^*\). By [Lip69, Lemma 14.3], the restriction map \(\mathrm{Pic}(W)\to \mathrm{Pic}(E)\) is surjective. Considering the exact sequence \(0\to \mathrm{Pic}^0(E)\to \mathrm{Pic}(E)\to \mathbb{Z}^n\to 0\), we can deduce that the map \(\mathrm{Pic}^0(W)\to \mathrm{Pic}^0(E)\) is surjective. This is a contradiction as \(\mathrm{Pic}^0(W)\) is torsion while \(k^*\) and \(E(k)\) are not. □ — https://federation-margaux.math.cnrs.fr/wp-content/uploads/2024/10/2306.07000v1.pdf; retrieval ID `turn168732812search47`.

- AstérisqueLAURENT MORET-BAILLY — https://www.numdam.org/item/AST_1985__129__1_0.pdf; retrieval ID `turn168732812search48`.

- Chow motives of genus one fibrations — https://www.researchgate.net/publication/357927751_Chow_motives_of_genus_one_fibrations; retrieval ID `turn168732812search2`.

- DEL PEZZO SURFACES IN POSITIVE CHARACTERISTIC 62 — https://www.math.uni-duesseldorf.de/~schroeer/publications_pdf/DelPezzoMori_final.pdf; retrieval ID `turn168732812search49`.

- Bielliptic surfaces over arbitrary ground fields — https://d-nb.info/1375603507/34; retrieval ID `turn168732812search50`.

- Rims 1624 | PDF | Group (Mathematics) | Geometry — https://www.scribd.com/document/1077666463/Rims-1624; retrieval ID `turn168732812search3`.

- Néron models — https://openmaths.org/courses/AG-GS/AG-GS-07.html; retrieval ID `turn168732812search4`.

- The Picard Scheme — https://www.researchgate.net/publication/260022664_The_Picard_Scheme; retrieval ID `turn168732812search5`.

- Boundedness of total Cartier indices for rational singularities in families — https://www.researchgate.net/publication/405132380_Boundedness_of_total_Cartier_indices_for_rational_singularities_in_families/download; retrieval ID `turn168732812search6`.

- Picard Groups - Examples and Counterexamples in Elementary Algebraic Geometry — https://waerden001.github.io/Examples_and_Counterexamples_in_Elementary_Algebraic_Geometry/computations/picard/; retrieval ID `turn168732812search7`.

- N\'eron models, minimal models, and birational group actions — https://www.researchgate.net/publication/389168054_N%27eron_models_minimal_models_and_birational_group_actions; retrieval ID `turn168732812search8`.

- SGA 2, Exposé XIII — Problems and conjectures | English Translation — https://jcreinhold.github.io/sga/ii/13-problems-and-conjectures.html; retrieval ID `turn168732812search9`.

- What Determines an Algebraic Variety? 9780691246833, 9780691246802 - DOKUMEN.PUB — https://dokumen.pub/what-determines-an-algebraic-variety-9780691246833-9780691246802.html; retrieval ID `turn168732812search10`.

- Algebraic Groups: Structure and Actions 9781470426019, 1470426013 - DOKUMEN.PUB — https://dokumen.pub/algebraic-groups-structure-and-actions-9781470426019-1470426013.html; retrieval ID `turn168732812search11`.

- Maps between local Picard groups — https://www.researchgate.net/publication/264123244_Maps_between_local_Picard_groups; retrieval ID `turn168732812search12`.

- Glossary of algebraic geometry — https://en.wikipedia.org/wiki/Glossary_of_algebraic_geometry; retrieval ID `turn168732812search51`.

- Pmihes 1985 62 145 0 | PDF | Module sur un anneau | Structures mathématiques — https://fr.scribd.com/document/850785084/PMIHES-1985-62-145-0; retrieval ID `turn168732812search13`.

- Motivic and $$\ell $$ -adic realizations of the category of singularities of the zero locus of a global section of a vector bundle — https://link.springer.com/article/10.1007/s00029-021-00734-2; retrieval ID `turn168732812search14`.

- Lectures on Pure Motives Theory | PDF | Mathematical Concepts | Algebraic Geometry — https://www.scribd.com/document/810075606/Lectures-on-the-theory-of-pure-motives-Jacob-P-Murre-Jan-Nagel-Chris-A-M-Peters-Z-Library; retrieval ID `turn168732812search15`.

- Categorification of Intersection Product | PDF | Category Theory | Functions And Mappings — https://www.scribd.com/document/962145614/2511-10527v1; retrieval ID `turn168732812search16`.

- The Picard scheme — https://www.researchgate.net/publication/299680183_The_Picard_scheme; retrieval ID `turn168732812search17`.

- pdf — https://page.mi.fu-berlin.de/esnault/preprints/helene/118b-EK.pdf; retrieval ID `turn168732812view0`.

- Technique de descente et théorèmes d'existence en géométrie algébrique. VI. Les schémas de Picard : propriétés générales — https://www.numdam.org/item/SB_1961-1962__7__221_0/; retrieval ID `turn168732812view1`.

- -------------------------------------------------------------------------------- — https://williamsawin.com/ReconstructionBook.pdf; retrieval ID `turn168732812view2`.

- -------------------------------------------------------------------------------- — https://arxiv.org/pdf/math/0504020; retrieval ID `turn168732812view4`.

Access failure occurred in this batch. The full diagnostic is preserved in the local raw record. No failed URL is represented as a checked theorem.

### Batch 15

Opened Bourbaki236 primary PDF, Stacks0C6R units/Picard exact sequence and04DY nil-invariance. Named-service searches for the formal comparison did not expose the final theorem text.

```json
{
  "system1_search_query": [
    {
      "q": "SGA 7 I pdf Grothendieck Raynaud 288"
    },
    {
      "q": "Grothendieck Murre tame fundamental group formal neighbourhood LNM 208 pdf"
    },
    {
      "q": "site.zbmath.org \"tame fundamental group\" \"formal\""
    },
    {
      "q": "site.numdam.org Grothendieck \"Picard\" \"1962\" \"pdf\""
    }
  ],
  "open": [
    {
      "ref_id": "https://www.numdam.org/item/SB_1961-1962__7__221_0.pdf"
    },
    {
      "ref_id": "https://stacks.math.columbia.edu/tag/0C6R"
    },
    {
      "ref_id": "https://stacks.math.columbia.edu/tag/04DY"
    }
  ],
  "response_length": "long"
}
```

Returned source records (titles and URLs; presence here alone does not certify opening or proof):

- Résumé des premiers exposés de A — https://library.slmath.org/nonmsri/sga/sga/pdf/sga7-1.pdf; retrieval ID `turn218461547search14`.

- Séminaire de géométrie algébrique — Textes originaux et Canon — https://zenodo.org/records/22985823; retrieval ID `turn218461547search0`.

- Alexandre Grothendieck and collaborators — SGA 1–7: compact English readers, French editions, TeX, and provenance — https://zenodo.org/records/22060305; retrieval ID `turn218461547search1`.

- Complete PDF Archive - Grothendieck Documents — https://geotoppos.org/pdf-archive.html; retrieval ID `turn218461547search2`.

- Bibliography entry—The Stacks project — https://stacks.math.columbia.edu/bibliography/SGA7-I; retrieval ID `turn218461547search3`.

- Groupes de Monodromie en Géométrie Algébrique — https://link.springer.com/book/10.1007/BFb0068688; retrieval ID `turn218461547search4`.

- Bibliography entry—The Stacks project — https://stacks.math.columbia.edu/bibliography/Grothendieck-Murre; retrieval ID `turn218461547search5`.

- The Tame Fundamental Group of a Formal Neighbourhood of a Divisor with Normal Crossings on a Scheme — https://link.springer.com/book/10.1007/BFb0069608; retrieval ID `turn218461547search6`.

- Published Works - CSG Istituto Grothendieck — https://csg.igrothendieck.org/published-works/; retrieval ID `turn218461547search7`.

- Lecture Notes in Mathematics — https://ftp.math.utah.edu/pub/tex/bib/toc/lnm1970.html; retrieval ID `turn218461547search8`.

- The Tame Fundamental Group of a Formal Neighbourhood of a Divisor with Normal Crossings on a Scheme — https://cir.nii.ac.jp/crid/1360574094581431168; retrieval ID `turn218461547search9`.

- The tame fundamental group of a formal neighbourhood of a divisor with normal crossings on a scheme / Alexandre Grothendieck, Jacob P. Murre — https://catalogue.bnf.fr/ark%3A/12148/cb44687699z; retrieval ID `turn218461547search10`.

- Technique de descente et théorèmes d'existence en géométrie algébrique. VI. Les schémas de Picard : propriétés générales — https://www.numdam.org/item/SB_1961-1962__7__221_0.pdf; retrieval ID `turn218461547view0`.

- Lemma 37.4.1 (0C6R)—The Stacks project — https://stacks.math.columbia.edu/tag/0C6R; retrieval ID `turn218461547view1`.

- Section 59.45 (04DY): Topological invariance of the small étale site—The Stacks project — https://stacks.math.columbia.edu/tag/04DY; retrieval ID `turn218461547view2`.

### Batch 16

SGA7 web parser rejected the large PDF; direct fetch later succeeded and the Raynaud pages were read visually. Grothendieck collected bibliography, Lipman1974 and Esnault–Kindler exact theorem were opened. Grothendieck–Murre full publisher PDF remained inaccessible.

```json
{
  "open": [
    {
      "ref_id": "https://library.slmath.org/nonmsri/sga/sga/pdf/sga7-1.pdf"
    },
    {
      "ref_id": "https://csg.igrothendieck.org/published-works/"
    },
    {
      "ref_id": "https://link.springer.com/content/pdf/10.1007/BFb0069608.pdf"
    },
    {
      "ref_id": "https://www.math.purdue.edu/~jlipman/papers-older/%5B1974%5D%20Picard%20schemes%20of%20formal%20schemes%3A%20application%20to%20rings%20with%20discrete%20divisor%20class%20group.pdf"
    }
  ],
  "find": [
    {
      "ref_id": "turn218461547view0",
      "pattern": "biration"
    },
    {
      "ref_id": "turn641590707view4",
      "pattern": "Theorem 1.1"
    },
    {
      "ref_id": "turn168732812view0",
      "pattern": "replaced"
    }
  ],
  "response_length": "long"
}
```

Returned source records (titles and URLs; presence here alone does not certify opening or proof):

- Published Works - CSG Istituto Grothendieck — https://csg.igrothendieck.org/published-works/; retrieval ID `turn845758054view1`.

- Picard schemes of formal schemes; application to rings with discrete divisor class group — https://www.math.purdue.edu/~jlipman/papers-older/%5B1974%5D%20Picard%20schemes%20of%20formal%20schemes%3A%20application%20to%20rings%20with%20discrete%20divisor%20class%20group.pdf ; rewritten summary of https://www.math.purdue.edu/~jlipman/papers-older/%5B1974%5D%20Picard%20schemes%20of%20formal%20schemes:%20application%20to%20rings%20with%20discrete%20divisor%20class%20group.pdf; retrieval ID `turn845758054view3`.

- Technique de descente et théorèmes d'existence en géométrie algébrique. VI. Les schémas de Picard : propriétés générales — https://www.numdam.org/item/SB_1961-1962__7__221_0.pdf; retrieval ID `turn845758054view4`.

- pdf — https://page.mi.fu-berlin.de/esnault/preprints/helene/118-EK.pdf; retrieval ID `turn845758054view5`.

- pdf — https://page.mi.fu-berlin.de/esnault/preprints/helene/118b-EK.pdf; retrieval ID `turn845758054view6`.

Access failure occurred in this batch. The full diagnostic is preserved in the local raw record. No failed URL is represented as a checked theorem.

### Batch 17

Read the Esnault–Kindler erratum, purity, Kunz/Frobenius, reflexive extension, Kummer, Lipman§2.4 and Kleiman proper Pic^tau passages. These constrain the reconstructed proofs but do not fill omitted hypotheses.

```json
{
  "open": [
    {
      "ref_id": "turn641590707view5",
      "lineno": 0
    },
    {
      "ref_id": "https://stacks.math.columbia.edu/tag/0BMB"
    },
    {
      "ref_id": "https://stacks.math.columbia.edu/tag/0EC0"
    },
    {
      "ref_id": "https://stacks.math.columbia.edu/tag/0CC6"
    },
    {
      "ref_id": "https://stacks.math.columbia.edu/tag/0AY6"
    },
    {
      "ref_id": "https://stacks.math.columbia.edu/tag/03PK"
    }
  ],
  "find": [
    {
      "ref_id": "turn845758054view1",
      "pattern": "CSG89"
    },
    {
      "ref_id": "turn845758054view3",
      "pattern": "Mittag"
    },
    {
      "ref_id": "turn231756711view4",
      "pattern": "6.13"
    }
  ],
  "response_length": "long"
}
```

Returned source records (titles and URLs; presence here alone does not certify opening or proof):

- pdf — https://page.mi.fu-berlin.de/esnault/preprints/helene/118b-EK.pdf; retrieval ID `turn634899531view0`.

- Lemma 58.21.4 (0BMB): Purity of branch locus—The Stacks project — https://stacks.math.columbia.edu/tag/0BMB; retrieval ID `turn634899531view1`.

- Lemma 51.17.6 (0EC0): Kunz—The Stacks project — https://stacks.math.columbia.edu/tag/0EC0; retrieval ID `turn634899531view2`.

- Section 33.36 (0CC6): Frobenii—The Stacks project — https://stacks.math.columbia.edu/tag/0CC6; retrieval ID `turn634899531view3`.

- Lemma 31.13.13 (0AY6)—The Stacks project — https://stacks.math.columbia.edu/tag/0AY6; retrieval ID `turn634899531view4`.

- Section 59.28 (03PK): Kummer theory—The Stacks project — https://stacks.math.columbia.edu/tag/03PK; retrieval ID `turn634899531view5`.

- Published Works - CSG Istituto Grothendieck — https://csg.igrothendieck.org/published-works/; retrieval ID `turn634899531view6`.

- Picard schemes of formal schemes; application to rings with discrete divisor class group — https://www.math.purdue.edu/~jlipman/papers-older/%5B1974%5D%20Picard%20schemes%20of%20formal%20schemes%3A%20application%20to%20rings%20with%20discrete%20divisor%20class%20group.pdf ; rewritten summary of https://www.math.purdue.edu/~jlipman/papers-older/%5B1974%5D%20Picard%20schemes%20of%20formal%20schemes:%20application%20to%20rings%20with%20discrete%20divisor%20class%20group.pdf; retrieval ID `turn634899531view7`.

- -------------------------------------------------------------------------------- — https://arxiv.org/pdf/math/0504020; retrieval ID `turn634899531view8`.

### Batch 18

Additional searches on boundary-tame finite generation, partition H1 finiteness and regular-locus Picard comparison; opened tame, connected-cover and Bertini framework. No blanket FG/FP identification made.

```json
{
  "system2_search_query": [
    {
      "q": "\"tame fundamental group\" \"finitely generated\" \"normal\" \"compactification\""
    },
    {
      "q": "\"fundamental group\" \"universally Japanese\" finite"
    },
    {
      "q": "\"H^1\" \"constructible\" \"finite fibres\" \"stratification\" Grothendieck"
    },
    {
      "q": "\"Pic\" \"birational\" \"regular\" \"tau\" scheme"
    }
  ],
  "find": [
    {
      "ref_id": "turn581975326view1",
      "pattern": "2.12. —"
    },
    {
      "ref_id": "turn581975326view1",
      "pattern": "3.3. —"
    },
    {
      "ref_id": "turn231756711view0",
      "pattern": "1.1."
    }
  ],
  "open": [
    {
      "ref_id": "https://stacks.math.columbia.edu/tag/0BSE"
    },
    {
      "ref_id": "https://stacks.math.columbia.edu/tag/0BN6"
    },
    {
      "ref_id": "https://stacks.math.columbia.edu/tag/0G4C"
    }
  ],
  "response_length": "long"
}
```

Returned source records (titles and URLs; presence here alone does not certify opening or proof):

- 4. **Lecture 4: Interlude on some Similarity between the Fundamental Groups in Characteristic 0 and p > 0** — https://page.mi.fu-berlin.de/esnault/preprints/helene/147_eilenberg.pdf; retrieval ID `turn809280941search48`.

- FINITE PRESENTATION 3 — https://page.mi.fu-berlin.de/esnault/preprints/helene/141_ess.pdf; retrieval ID `turn809280941search49`.

- HÉLÈNE ESNAULT, VASUDEVAN SRINIVAS AND JAKOB STIX — https://page.mi.fu-berlin.de/esnault/preprints/helene/142_ess.pdf; retrieval ID `turn809280941search50`.

- GENERATORS AND RELATIONS FOR THE ´ETALE FUNDAMENTAL — https://citeseerx.ist.psu.edu/document?doi=ac4985be2a5fdf21ba0f55edaa56aadb16313c24&repid=rep1&type=pdf; retrieval ID `turn809280941search51`.

- H. Esnault, V. Srinivas and J. Stix — https://content.algebraicgeometry.nl/2023-3/2023-3-011.pdf; retrieval ID `turn809280941search52`.

- SIMPLY CONNECTED VARIETIES IN CHARACTERISTIC \(p>0\) 2 — https://page.mi.fu-berlin.de/esnault/preprints/helene/113-ES_B.pdf; retrieval ID `turn809280941search53`.

- Local Systems in Algebraic Arithmetic Geometry pdf version | PDF | Geometry | Arithmetic — https://www.scribd.com/document/1078254966/Local-Systems-in-Algebraic-Arithmetic-Geometry-pdf-version; retrieval ID `turn809280941search0`.

- Secure Local Systems in Algebraic Arithmetic Geometry | PDF | Geometry | Arithmetic — https://www.scribd.com/document/1072391530/Secure-Local-Systems-in-Algebraic-Arithmetic-Geometry; retrieval ID `turn809280941search1`.

- On different notions of tameness in arithmetic geometry — https://studyres.com/doc/19718667/on-different-notions-of-tameness-in-arithmetic-geometry; retrieval ID `turn809280941search2`.

- [Literature Review] Tame fundamental groups of rigid spaces — https://www.themoonlight.io/review/tame-fundamental-groups-of-rigid-spaces; retrieval ID `turn809280941search3`.

- The Tate Conjecture for Surfaces of Geometric Genus One -- Overcoming Singularities — https://www.researchgate.net/publication/388529439_The_Tate_Conjecture_for_Surfaces_of_Geometric_Genus_One_--_Overcoming_Singularities; retrieval ID `turn809280941search4`.

- au:Stix_J in:math - SciRate Search — https://scirate.com/search?q=au%3AStix_J+in%3Amath; retrieval ID `turn809280941search5`.

- Étale fundamental group — https://en.wikipedia.org/wiki/%C3%89tale_fundamental_group; retrieval ID `turn809280941search54`.

- [Papierüberprüfung] Tame fundamental groups of rigid spaces — https://www.themoonlight.io/de/review/tame-fundamental-groups-of-rigid-spaces; retrieval ID `turn809280941search6`.

- Alexandre Grothendieck. A Mathematical Portrait - Schneps L. - 2014 — https://djvu.online/file/xSj2S14E8ZZOG; retrieval ID `turn809280941search7`.

- Specialization for the pro-étale fundamental group — https://www.cambridge.org/core/journals/compositio-mathematica/article/specialization-for-the-proetale-fundamental-group/9FF5AAC3BAFD65AA505EF8268C8641CB; retrieval ID `turn809280941search8`.

- Nine Mathematical Challenges: An Elucidation 1470454904, 9781470454906 - DOKUMEN.PUB — https://dokumen.pub/nine-mathematical-challenges-an-elucidation-1470454904-9781470454906.html; retrieval ID `turn809280941search9`.

- Specialization for the pro-étale fundamental group — https://www.researchgate.net/publication/363902420_Specialization_for_the_pro-etale_fundamental_group; retrieval ID `turn809280941search10`.

- The adic tame site — https://www.researchgate.net/publication/366999476_The_adic_tame_site; retrieval ID `turn809280941search11`.

- au:Srinivas_V in:math - SciRate Search — https://scirate.com/search?q=au%3ASrinivas_V+in%3Amath; retrieval ID `turn809280941search12`.

- Section 58.31 (0BSE): Tame ramification—The Stacks project — https://stacks.math.columbia.edu/tag/0BSE; retrieval ID `turn809280941view0`.

- Lemma 58.4.1 (0BN6)—The Stacks project — https://stacks.math.columbia.edu/tag/0BN6; retrieval ID `turn809280941view1`.

- Section 37.32 (0G4C): Bertini theorems—The Stacks project — https://stacks.math.columbia.edu/tag/0G4C; retrieval ID `turn809280941view2`.

- arXiv:math/0206203v2  [math.AG]  4 Jan 2004 — https://arxiv.org/pdf/math/0206203; retrieval ID `turn809280941view3`.

- arXiv:math/0206203v2  [math.AG]  4 Jan 2004 — https://arxiv.org/pdf/math/0206203; retrieval ID `turn809280941view4`.

- -------------------------------------------------------------------------------- — https://perso.ens-lyon.fr/frederic.deglise/docs/2007/gabber.pdf; retrieval ID `turn809280941view5`.

### Batch 19

Further N385, zbMATH SGA7 and MathOverflow Picard searches; opened SGA7 publisher metadata. The reused distribution source and exact omitted draft propositions remained unlocated.

```json
{
  "open": [
    {
      "ref_id": "https://link.springer.com/book/10.1007/BFb0068688"
    },
    {
      "ref_id": "https://link.springer.com/book/10.1007/BFb0069608"
    }
  ],
  "system2_search_query": [
    {
      "q": "\"N° 385\" \"Distributions\" Bourbaki"
    },
    {
      "q": "\"distributions\" \"D_a\" \"m\" \"Schwartz\" finite order point support"
    },
    {
      "q": "site.zbmath.org \"Raynaud\" \"Groupes de monodromie\""
    },
    {
      "q": "site.mathoverflow.net \"Picard\" \"birational invariance\" scheme"
    }
  ],
  "response_length": "long"
}
```

Returned source records (titles and URLs; presence here alone does not certify opening or proof):

- Microsoft Word - Découvrir-Transmettre.doc — https://www.wstein.org/sga/circle/aherreman.pdf; retrieval ID `turn487519088search48`.

- SEMINAIRE DE GEOMETRIE ALGEBRIQUE DU BOIS-MARIE — https://library.slmath.org/nonmsri/sga/sga/pdf/sga7-1.pdf; retrieval ID `turn487519088search49`.

- 134  CHAPTER 5. BIRATIONAL INVARIANCE — https://www.imo.universite-paris-saclay.fr/~jean-louis.colliot-thelene/BGgroup_book.pdf; retrieval ID `turn487519088search50`.

- Groupes de Monodromie en Geometrie Algebrique — https://books.google.com/books/about/Groupes_de_Monodromie_en_Geometrie_Algeb.html?id=WbSp0QEACAAJ; retrieval ID `turn487519088search0`.

- Groupes de Monodromie en Géométrie Algébrique — https://link.springer.com/book/10.1007/BFb0068688; retrieval ID `turn487519088search1`.

- Transformation de Fourier, constantes d'équations fonctionnelles et conjecture de Weil — https://www.numdam.org/item/PMIHES_1987__65__131_0/; retrieval ID `turn487519088search2`.

- Rankless | Michèle Raynaud — https://www.rankless.org/authors/michele-raynaud; retrieval ID `turn487519088search3`.

- Bibliography entry—The Stacks project — https://kiwix.presumenothing.net/content/stacks.math.columbia.edu_en_all_2024-12/stacks.math.columbia.edu/bibliography/SGA7-I; retrieval ID `turn487519088search4`.

- Groupes de monodromie finie des variétés abéliennes — https://staff.math.su.se/severin.philip/Groupes_de_monodromie_finie_des_vari%C3%A9t%C3%A9s_ab%C3%A9liennes.pdf; retrieval ID `turn487519088search51`.

- Exposé VII : $1$-motifs et monodromie géométrique — https://archive.numdam.org/item/AST_1994__223__295_0/; retrieval ID `turn487519088search5`.

- SGA 7 — Groupes de Monodromie en Géométrie Algébrique — Table des matières — https://grothendiecksga.com/read/sga7/fr/; retrieval ID `turn487519088search6`.

- Analytic States in Quantum Field Theory on Curved Spacetimes — https://link.springer.com/article/10.1007/s00023-024-01419-0; retrieval ID `turn487519088search7`.

- Fractional Itô Calculus for Randomly Scaled Fractional Brownian Motion and its Applications to Evolution Equations — https://link.springer.com/article/10.1007/s10959-026-01484-7; retrieval ID `turn487519088search8`.

- Semi-groupes de mesures complexes et calcul symbolique sur les générateurs infinitésimaux de semi-groupes d'opérateurs — https://www.numdam.org/item/10.5802/aif.342.pdf; retrieval ID `turn487519088search52`.

- SGA Table of Contents — https://brianhwang.com/sga-table-of-contents/; retrieval ID `turn487519088search9`.

- Archives nationales (France) — https://www.archives.developpement-durable.gouv.fr/IMG/pdf/19770738.pdf; retrieval ID `turn487519088search53`.

- Transformation de Fourier, constantes d'équations fonctionnelles et conjecture de Weil — https://numdam.org/articles/10.1007/BF02698937/; retrieval ID `turn487519088search10`.

- Recherche documentaire | Bibliothèques de l'université d'Orléans | Un réseau de bibliothèques à votre service :: SCD d'Orléans — https://catalogue.univ-orleans.fr/Search/Results?filter%5B%5D=-language%3A%22Moyen+fran%C3%A7ais%22&filter%5B%5D=format%3A%22Livre+papier%22&filter%5B%5D=language%3A%22Anglais%22&filter%5B%5D=language%3A%22Fran%C3%A7ais%22&filter%5B%5D=publisher%3A%22verlag%22&filter%5B%5D=topic_facet%3A%22G%C3%A9om%C3%A9trie+alg%C3%A9brique%22&type=AllFields; retrieval ID `turn487519088search11`.

- Hauteurs et isogénies — https://www.numdam.org/item/AST_1985__127__199_0/; retrieval ID `turn487519088search12`.

- Théorie de Dieudonné sur un anneau de valuation parfait — https://archive.numdam.org/articles/10.24033/asens.1381/; retrieval ID `turn487519088search13`.

- Androma Notation — Code - Androma — https://androma.org/notation/code?path=content%2F9-differential-geometry&section=content; retrieval ID `turn487519088search14`.

- ag.algebraic geometry - Singular cohomology and birational equivalence - MathOverflow — https://mathoverflow.net/questions/253980/singular-cohomology-and-birational-equivalence?noredirect=1; retrieval ID `turn487519088search15`.

- algebraic geometry - Picard group of product of spaces - Mathematics Stack Exchange — https://math.stackexchange.com/questions/493005/picard-group-of-product-of-spaces/1674937; retrieval ID `turn487519088search16`.

- ag.algebraic geometry - Singular cohomology and birational equivalence - MathOverflow — https://mathoverflow.net/questions/253980/singular-cohomology-and-birational-equivalence/253999; retrieval ID `turn487519088search17`.

- Groupes de Monodromie en Géométrie Algébrique: Séminaire de Géométrie Algébrique du Bois-Marie 1967-1969. (SGA 7 I) | Springer Nature Link — https://link.springer.com/book/10.1007/BFb0068688; retrieval ID `turn487519088view0`.

- The Tame Fundamental Group of a Formal Neighbourhood of a Divisor with Normal Crossings on a Scheme | Springer Nature Link — https://link.springer.com/book/10.1007/BFb0069608; retrieval ID `turn487519088view1`.

### Batch 20

Targeted generic-fibre descent and reduced-fibre adjective searches. Found Katz–Lang as a later primary route; Stacks proper homotopy, normalization and proper-target rational-map inputs were read with their scopes.

```json
{
  "system1_search_query": [
    {
      "q": "\"geometric generic fibre\" \"exact\" \"fundamental\" \"normal\" \"reduced\""
    },
    {
      "q": "\"fibre générique\" \"réduit\" \"suite exacte\" \"groupe fondamental\""
    },
    {
      "q": "\"faisceaux constructibles\" \"japonais\" \"image directe\""
    },
    {
      "q": "\"H1\" \"G × G\" \"finitude\" Grothendieck"
    }
  ],
  "open": [
    {
      "ref_id": "https://stacks.math.columbia.edu/tag/0BUM"
    },
    {
      "ref_id": "https://stacks.math.columbia.edu/tag/0BQJ"
    },
    {
      "ref_id": "https://stacks.math.columbia.edu/tag/0BX7"
    }
  ],
  "response_length": "long"
}
```

Returned source records (titles and URLs; presence here alone does not certify opening or proof):

- Homotopy Exact Sequence for the Pro-Étale Fundamental Group — https://www.researchgate.net/publication/352637062_Homotopy_Exact_Sequence_for_the_Pro-Etale_Fundamental_Group; retrieval ID `turn411015661search0`.

- Exposé X · Application du théorème d'existence de faisceaux: théo­rème de semi-con­ti­nu­i­té pour les groupes fondamentaux des fibres d'un morphisme propre et séparable — SGA 1 — https://grothendiecksga.com/read/sga1/fr/X-2.html; retrieval ID `turn411015661search1`.

- Finiteness theorems in geometric classfield theory, Enseign — https://www.researchgate.net/publication/277290725_Finiteness_theorems_in_geometric_classfield_theory_Enseign; retrieval ID `turn411015661search2`.

- Comparison between the fundamental group scheme of a relative scheme and that of its generic fiber — https://jtnb.centre-mersenne.org/articles/10.5802/jtnb.731/; retrieval ID `turn411015661search3`.

- Homotopy Exact Sequence for the Pro-\'Etale Fundamental Group II — https://www.researchgate.net/publication/337048192_Homotopy_Exact_Sequence_for_the_Pro-%27Etale_Fundamental_Group_II; retrieval ID `turn411015661search4`.

- Travaux de Gabber sur l'uniformisation locale et la cohomologie etaledes schemas quasi-excellents. Seminaire a l'Ecole polytechnique 2006--2008 — https://www.academia.edu/126973279/Travaux_de_Gabber_sur_luniformisation_locale_et_la_cohomologie_etaledes_schemas_quasi_excellents_Seminaire_a_lEcole_polytechnique_2006_2008; retrieval ID `turn411015661search5`.

- Travaux de Gabber sur l'uniformisation locale et la cohomologie etale des schemas quasi-excellents. Seminaire a l'Ecole polytechnique 2006--2008 — https://www.academia.edu/74546881/Travaux_de_Gabber_sur_luniformisation_locale_et_la_cohomologie_etale_des_schemas_quasi_excellents_Seminaire_a_lEcole_polytechnique_2006_2008; retrieval ID `turn411015661search6`.

- Torseurs, fibrés vectoriels et schéma en groupes fondamental | ANR — https://anr.fr/Projet-ANR-13-PDOC-0015; retrieval ID `turn411015661search7`.

- Comparison between the fundamental group scheme of a relative scheme and that of its generic fiber — https://www.numdam.org/item/JTNB_2010__22_3_537_0/; retrieval ID `turn411015661search8`.

- Section 58.15 (0BUM): Homotopy exact sequence—The Stacks project — https://stacks.math.columbia.edu/tag/0BUM; retrieval ID `turn411015661view0`.

- Section 58.11 (0BQJ): Fundamental groups of normal schemes—The Stacks project — https://stacks.math.columbia.edu/tag/0BQJ; retrieval ID `turn411015661view1`.

- Lemma 29.43.5 (0BX7)—The Stacks project — https://stacks.math.columbia.edu/tag/0BX7; retrieval ID `turn411015661view2`.

### Batch 21

Revisited Déglise exact statements, ESS tame-curve input and LSS dates. Opened Milne cohomology, Conrad Picard curves and Moonen Tate modules as precise background for finite coefficients and Picard rank.

```json
{
  "open": [
    {
      "ref_id": "turn231756711view0",
      "lineno": 0
    },
    {
      "ref_id": "turn558723927view1",
      "lineno": 45
    },
    {
      "ref_id": "turn231756711view2",
      "lineno": 15
    },
    {
      "ref_id": "https://www.jmilne.org/math/CourseNotes/LEC210.pdf"
    },
    {
      "ref_id": "https://math.stanford.edu/~conrad/248BPage/handouts/pic.pdf"
    },
    {
      "ref_id": "https://www.math.ru.nl/~bmoonen/BookAV/TateBT.pdf"
    }
  ],
  "response_length": "long"
}
```

Returned source records (titles and URLs; presence here alone does not certify opening or proof):

- -------------------------------------------------------------------------------- — https://page.mi.fu-berlin.de/esnault/preprints/helene/141_ess.pdf; retrieval ID `turn154454136view1`.

- [2303.11161] Fundamental groups of proper varieties are finitely presented — https://arxiv.org/abs/2303.11161; retrieval ID `turn154454136view2`.

- Lectures on Etale Cohomology — https://www.jmilne.org/math/CourseNotes/LEC210.pdf; retrieval ID `turn154454136view3`.

- -------------------------------------------------------------------------------- — https://math.stanford.edu/~conrad/248BPage/handouts/pic.pdf; retrieval ID `turn154454136view4`.

- AV — https://www.math.ru.nl/~bmoonen/BookAV/TateBT.pdf; retrieval ID `turn154454136view5`.

### Batch 22

Queries for Katz–Lang generic exactness, Picard invariance, formal9.2.3 and distributions. Located the author-hosted Katz–Lang scan; opened the blowup definition and an SGA1 homotopy passage.

```json
{
  "system2_search_query": [
    {
      "q": "Katz Lang finiteness theorems geometric classfield theory 1981 pdf lemma 2 fundamental group generic fiber"
    },
    {
      "q": "proper birational morphism normal smooth Picard scheme Pic tau isomorphism"
    },
    {
      "q": "Grothendieck Murre tame fundamental group formal neighbourhood scheme 9.2.3 pdf"
    },
    {
      "q": "point supported distributions finite order jets tensor product Bourbaki Lie groups 385"
    }
  ],
  "open": [
    {
      "ref_id": "https://stacks.math.columbia.edu/tag/01OF"
    },
    {
      "ref_id": "https://arxiv.org/pdf/math/0206203",
      "lineno": 11450
    }
  ],
  "response_length": "long"
}
```

Returned source records (titles and URLs; presence here alone does not certify opening or proof):

- L'Enseignement Mathématique — https://web.math.princeton.edu/~nmk/old/AbsFinThm.pdf; retrieval ID `turn264819157search48`.

- The tame fundamental group of a formal neighbourhood of a divisor with normal crossings on a scheme / Alexandre Grothendieck, Jacob P. Murre — https://catalogue.bnf.fr/ark%3A/12148/cb44687699z; retrieval ID `turn264819157search0`.

- Finiteness theorems in geometric classfield theory, Enseign — https://www.researchgate.net/publication/277290725_Finiteness_theorems_in_geometric_classfield_theory_Enseign; retrieval ID `turn264819157search1`.

- The Tame Fundamental Group of a Formal Neighbourhood of a Divisor with Normal Crossings on a Scheme — https://link.springer.com/book/10.1007/BFb0069608; retrieval ID `turn264819157search2`.

- The Zariski topology, linear systems, and — https://max.lieblich.us/wp-content/uploads/2021/09/reconstructionweb.pdf; retrieval ID `turn264819157search49`.

- Published Works - CSG Istituto Grothendieck — https://csg.igrothendieck.org/published-works/; retrieval ID `turn264819157search3`.

- The Tame Fundamental Group of a Formal Neighbourhood of a Divisor with Normal Crossings on a Scheme — https://cir.nii.ac.jp/crid/1360574094581431168; retrieval ID `turn264819157search4`.

- Bibliography entry—The Stacks project — https://stacks.math.columbia.edu/bibliography/Grothendieck-Murre; retrieval ID `turn264819157search5`.

- The Tame Fundamental Group of a Formal Neighbourhood of a Divisor with Normal Crossings on a Scheme door A. Grothendieck en J. P. Murre - Managementboek.nl — https://www.managementboek.nl/boek/9783540054993/the-tame-fundamental-group-of-a-formal-neighbourhood-of-a-divisor-with-normal-crossings-on-a-scheme-a-grothendieck; retrieval ID `turn264819157search6`.

- Tame Fundamental Group of a Formal Neighbourhood of a Divisor with Normal Crossings on a Scheme | Central Library, Indian Institute of Technology Delhi — https://dspace.apps.iitd.ac.in/node/95917; retrieval ID `turn264819157search7`.

- The tame fundamental group of a formal neighbourhood of a divisor with normal crossings on a scheme / | Library Search — https://libcat.canterbury.ac.nz/Record/859199; retrieval ID `turn264819157search8`.

- The Tame Fundamental Group of a Formal Neighbourhood of a Divisor with Normal Crossings on a Scheme (1971) by Alexander Grothendieck | Open Library — https://openlibrary.org/works/OL20733357W/The_Tame_Fundamental_Group_of_a_Formal_Neighbourhood_of_a_Divisor_with_Normal_Crossings_on_a_Scheme; retrieval ID `turn264819157search9`.

- Finiteness theorems in geometric classfield theory. (With an appendix by Kenneth A. Ribet) - MaRDI portal — https://portal.mardi4nfdi.de/wiki/Finiteness_theorems_in_geometric_classfield_theory._%28With_an_appendix_by_Kenneth_A._Ribet%29; retrieval ID `turn264819157search10`.

- The tame fundamental group of a formal neighbourhood of a divisor with normal crossings on a scheme [by] Alexandre Grothendieck [and] Jacob P. Murre. (Lecture notes in mathematics, 208) | NDLサーチ | 国立国会図書館 — https://ndlsearch.ndl.go.jp/books/R100000002-I000006204951; retrieval ID `turn264819157search11`.

- Let Pic^0_{X/k} — https://www.imo.universite-paris-saclay.fr/~jean-louis.colliot-thelene/BGgroup_book.pdf; retrieval ID `turn264819157search50`.

- DFG-Forschergruppe Regensburg/Freiburg — https://studyres.com/doc/19162019/dfg-forschergruppe-regensburg-freiburg; retrieval ID `turn264819157search12`.

- The affine part of the Picard scheme — https://www.cambridge.org/core/services/aop-cambridge-core/content/view/ACD9AD2E0BDD8B37B49284408AC2C9EF/S0010437X08003710a.pdf/affine_part_of_the_picard_scheme.pdf; retrieval ID `turn264819157search51`.

- The Tame Fundamental Group of a Formal Neighbourhood of a Divisor with Normal Crossings on a Scheme by A. Grothendieck, J. P. Murre - Books on Google Play — https://play.google.com/store/books/details/A_Grothendieck_The_Tame_Fundamental_Group_of_a_For?id=7wd8CwAAQBAJ; retrieval ID `turn264819157search13`.

- 8.4 Properties                                                                 233 — https://www.math.stonybrook.edu/~kamenova/homepage_files/Bosch_Raynaud_Neron_Model_tc.pdf; retrieval ID `turn264819157search52`.

- Higher Class Field Theory — https://www.mathi.uni-heidelberg.de/~witte/lehre/HauptseminarSoSe11/OSHCFTSS11e.pdf; retrieval ID `turn264819157search53`.

- Exposé XIII · Problems related to local Picard groups — SGA 2 — https://grothendiecksga.com/read/sga2/en/XIII-5.html; retrieval ID `turn264819157search14`.

- The Tame Fundamental Group of a Formal Neighbourhood of a Divisor with Normal Crossings on a Scheme - RNIB Bookshare — https://www.rnibbookshare.org/book/4796032; retrieval ID `turn264819157search15`.

- Section 31.33 (01OF): Blowing up—The Stacks project — https://stacks.math.columbia.edu/tag/01OF; retrieval ID `turn264819157view0`.

- arXiv:math/0206203v2  [math.AG]  4 Jan 2004 — https://arxiv.org/pdf/math/0206203; retrieval ID `turn264819157view1`.

### Batch 23

Named-service/formal-étale searches and exact Stacks Artin–Schreier, unramified and specialization pages. Katz–Lang primary PDF opened. Specialization direction and object-versus-morphism lifting distinguished.

```json
{
  "system1_search_query": [
    {
      "q": "site.stacks.math.columbia.edu formal schemes etale morphisms completion etale neighbourhood"
    },
    {
      "q": "site.zbmath.org Grothendieck Murre tame fundamental group formal neighbourhood 1971"
    },
    {
      "q": "site.numdam.org distributions support ponctuel jets dérivées"
    },
    {
      "q": "site.mathoverflow.net Picard group thickening torsion global units"
    }
  ],
  "open": [
    {
      "ref_id": "https://web.math.princeton.edu/~nmk/old/AbsFinThm.pdf"
    },
    {
      "ref_id": "https://stacks.math.columbia.edu/tag/0A3J"
    },
    {
      "ref_id": "https://stacks.math.columbia.edu/tag/02G3"
    },
    {
      "ref_id": "https://stacks.math.columbia.edu/tag/0GJ2"
    }
  ],
  "response_length": "long"
}
```

Returned source records (titles and URLs; presence here alone does not certify opening or proof):

- Section 37.35 (02LD): Étale neighbourhoods—The Stacks project — https://stacks.math.columbia.edu/tag/02LD; retrieval ID `turn738562895search0`.

- Section 37.8 (02HF): Formally étale morphisms—The Stacks project — https://stacks.math.columbia.edu/tag/02HF; retrieval ID `turn738562895search1`.

- Section 37.39 (0CAT): Étale neighbourhoods and Artin approximation—The Stacks project — https://stacks.math.columbia.edu/tag/0CAT; retrieval ID `turn738562895search2`.

- Bibliography entry—The Stacks project — https://stacks.math.columbia.edu/bibliography/Grothendieck-Murre; retrieval ID `turn738562895search3`.

- The Tame Fundamental Group of a Formal Neighbourhood of a Divisor with Normal Crossings on a Scheme — https://link.springer.com/book/10.1007/BFb0069608; retrieval ID `turn738562895search4`.

- Lecture Notes in Mathematics — https://ftp.math.utah.edu/pub/tex/bib/toc/lnm1970.html; retrieval ID `turn738562895search5`.

- Numdam — https://numdam.org/; retrieval ID `turn738562895search6`.

- Distributions involutives singulières — https://archive.numdam.org/articles/10.5802/aif.761/; retrieval ID `turn738562895search7`.

- PDF-Export ETH-Konsortium: Dokumente — https://web.math.princeton.edu/~nmk/old/AbsFinThm.pdf; retrieval ID `turn738562895view0`.

- Section 59.63 (0A3J): The Artin-Schreier sequence—The Stacks project — https://stacks.math.columbia.edu/tag/0A3J; retrieval ID `turn738562895view1`.

- Section 29.36 (02G3): Unramified morphisms—The Stacks project — https://stacks.math.columbia.edu/tag/02G3; retrieval ID `turn738562895view2`.

- Section 59.75 (0GJ2): Specializations and étale sheaves—The Stacks project — https://stacks.math.columbia.edu/tag/0GJ2; retrieval ID `turn738562895view3`.

### Batch 24

Targeted divisor localization, supersingularity, EGAI10.12.3 and Schwartz searches. Located the exact Katz–Lang Lemma2 and primary Sutherland/Schwartz/EGA leads.

```json
{
  "system2_search_query": [
    {
      "q": "site.stacks.math.columbia.edu Picard group complement prime divisors exact sequence regular scheme"
    },
    {
      "q": "Sutherland identifying supersingular elliptic curves trace divisible p 2012 pdf"
    },
    {
      "q": "EGA I 1960 10.12.3 morphismes etales schemas formels numdam"
    },
    {
      "q": "site.numdam.org Schwartz distributions support un point dérivées"
    }
  ],
  "find": [
    {
      "ref_id": "turn738562895view0",
      "pattern": "Lemma 2"
    },
    {
      "ref_id": "turn581975326view1",
      "pattern": "Corollaire 2.10"
    }
  ],
  "response_length": "long"
}
```

Returned source records (titles and URLs; presence here alone does not certify opening or proof):

- LMS J. Comput. Math. 15 (2012) 317–325 — https://www.cambridge.org/core/services/aop-cambridge-core/content/view/FA031913F61784866AC19A6532F0EE80/S1461157012001106a.pdf/identifying_supersingular_elliptic_curves.pdf; retrieval ID `turn543697393search47`.

- Identifying supersingular elliptic curves — https://www.cambridge.org/core/journals/lms-journal-of-computation-and-mathematics/article/identifying-supersingular-elliptic-curves/FA031913F61784866AC19A6532F0EE80; retrieval ID `turn543697393search0`.

- Identifying supersingular elliptic curves — https://math.mit.edu/~drew/AMS2012.pdf; retrieval ID `turn543697393search48`.

- §10. Formal Schemes - EGA — Éléments de Géométrie Algébrique (English Translation) — https://jcreinhold.github.io/ega/i/01-10-formal-schemes.html; retrieval ID `turn543697393search1`.

- Note — https://paperzz.com/doc/9220858/note; retrieval ID `turn543697393search2`.

- Search — https://www.cambridge.org/core/search?filters%5Bkeywords%5D=14H52+%28secondary%29; retrieval ID `turn543697393search3`.

- Search results for Mathematics — https://www.cambridge.org/core/browse-subjects/mathematics/msc-classifications/msc-2010-number-theory/11yxx?pageNum=6; retrieval ID `turn543697393search4`.

- Théorie des distributions et transformation de Fourier — https://www.numdam.org/item/AUG_1947-1948__23__7_0.pdf; retrieval ID `turn543697393search49`.

- Identifying supersingular elliptic curves — https://arxiv.org/abs/1107.1140; retrieval ID `turn543697393academia50`.

- Andrew V. Sutherland — https://klein.mit.edu/~drew/; retrieval ID `turn543697393search5`.

- Andrew V. Sutherland — https://math.mit.edu/~drew/index.html; retrieval ID `turn543697393search6`.

- dblp: Andrew V. Sutherland — https://dblp.org/pid/81/4339.html; retrieval ID `turn543697393search7`.

- Distributions Supported at a Point — Statement & Proof - Androma — https://androma.org/theorems/451; retrieval ID `turn543697393search8`.

- DIVISORS 69 — https://stacks.math.columbia.edu/download/divisors.pdf; retrieval ID `turn543697393search51`.

- Advanced Cryptography – Master SCCI — https://www-fourier.univ-grenoble-alpes.fr/~viva/teaching/SCCI/AC_lectures.pdf; retrieval ID `turn543697393search52`.

- EGAI/docs/references.md at main · CBirkbeck/EGAI · GitHub — https://github.com/CBirkbeck/EGAI/blob/main/docs/references.md; retrieval ID `turn543697393search9`.

- Identifying supersingular elliptic curves — https://www.researchgate.net/publication/51915132_Identifying_supersingular_elliptic_curves; retrieval ID `turn543697393search10`.

- CHAPITRE 4. LA THÉORIE DE SCHWARTZ — https://www.math.ens.psl.eu/shared-files/10357/?analyse-fonctionnelle2013-2.pdf=; retrieval ID `turn543697393search53`.

- Elements de geometrie algebrique (EGA): French Originals, English Working Readers, and Source Archives — https://zenodo.org/records/21714514; retrieval ID `turn543697393search11`.

- Elements de Geometrie Algebrique (EGA): French Originals and English Translation Working Draft — https://zenodo.org/records/20453302; retrieval ID `turn543697393search12`.

- Identifying supersingular elliptic curves Andrew V. Sutherland January 6, 2012 — https://studylib.net/doc/10496742/identifying-supersingular-elliptic-curves-andrew-v.-suthe...; retrieval ID `turn543697393search13`.

- Section 55.13 (0CAA): Picard groups of models—The Stacks project — https://stacks.math.columbia.edu/tag/0CAA; retrieval ID `turn543697393search14`.

- Théorie des distributions à valeurs vectorielles. I — https://www.numdam.org/item/AIF_1957__7__1_0/; retrieval ID `turn543697393search15`.

- Elements de geometrie algebrique (EGA): French Originals, English Working Readers, and Source Archives — https://zenodo.org/records/21712610; retrieval ID `turn543697393search16`.

- Section 55.13 (0CAA): Picard groups of models—The Stacks project — https://kiwix.presumenothing.net/content/stacks.math.columbia.edu_en_all_2024-12/stacks.math.columbia.edu/tag/0CAA; retrieval ID `turn543697393search17`.

- PDF-Export ETH-Konsortium: Dokumente — https://web.math.princeton.edu/~nmk/old/AbsFinThm.pdf; retrieval ID `turn543697393view0`.

- arXiv:math/0206203v2  [math.AG]  4 Jan 2004 — https://arxiv.org/pdf/math/0206203; retrieval ID `turn543697393view1`.

### Batch 25

Opened EGAI bibliographic metadata, Schwartz1947 primary PDF, Sutherland primary PDF, formally étale definition and Stacks divisor chapter. EGA metadata alone did not certify the numbered proposition.

```json
{
  "open": [
    {
      "ref_id": "https://www.numdam.org/item/PMIHES_1960__4__5_0/"
    },
    {
      "ref_id": "https://www.numdam.org/item/AUG_1947-1948__23__7_0.pdf"
    },
    {
      "ref_id": "https://arxiv.org/pdf/1107.1140"
    },
    {
      "ref_id": "https://stacks.math.columbia.edu/tag/02HF"
    },
    {
      "ref_id": "https://stacks.math.columbia.edu/download/divisors.pdf"
    },
    {
      "ref_id": "turn738562895view0",
      "lineno": 189
    }
  ],
  "response_length": "long"
}
```

Returned source records (titles and URLs; presence here alone does not certify opening or proof):

- Éléments de géométrie algébrique : I. Le langage des schémas — https://www.numdam.org/item/PMIHES_1960__4__5_0/; retrieval ID `turn382597057view0`.

- Théorie des distributions et transformation de Fourier — https://www.numdam.org/item/AUG_1947-1948__23__7_0.pdf; retrieval ID `turn382597057view1`.

- -------------------------------------------------------------------------------- — https://arxiv.org/pdf/1107.1140; retrieval ID `turn382597057view2`.

- Section 37.8 (02HF): Formally étale morphisms—The Stacks project — https://stacks.math.columbia.edu/tag/02HF; retrieval ID `turn382597057view3`.

- -------------------------------------------------------------------------------- — https://stacks.math.columbia.edu/download/divisors.pdf; retrieval ID `turn382597057view4`.

- PDF-Export ETH-Konsortium: Dokumente — https://web.math.princeton.edu/~nmk/old/AbsFinThm.pdf; retrieval ID `turn382597057view5`.

### Batch 26

Read Katz–Lang proof and divisor-class presentation; EGAI PDF exceeded web parser size. Read Schwartz§1 only as historical background, not as identification of N385.

```json
{
  "open": [
    {
      "ref_id": "turn738562895view0",
      "lineno": 238
    },
    {
      "ref_id": "https://www.numdam.org/item/PMIHES_1960__4__5_0.pdf"
    }
  ],
  "find": [
    {
      "ref_id": "turn382597057view4",
      "pattern": "divisors removed"
    },
    {
      "ref_id": "turn382597057view4",
      "pattern": "Pic(X)"
    },
    {
      "ref_id": "turn382597057view1",
      "pattern": "produit"
    },
    {
      "ref_id": "turn382597057view1",
      "pattern": "ponctuel"
    }
  ],
  "response_length": "long"
}
```

Returned source records (titles and URLs; presence here alone does not certify opening or proof):

- PDF-Export ETH-Konsortium: Dokumente — https://web.math.princeton.edu/~nmk/old/AbsFinThm.pdf; retrieval ID `turn600131709view0`.

- -------------------------------------------------------------------------------- — https://stacks.math.columbia.edu/download/divisors.pdf; retrieval ID `turn600131709view2`.

- -------------------------------------------------------------------------------- — https://stacks.math.columbia.edu/download/divisors.pdf; retrieval ID `turn600131709view3`.

- Théorie des distributions et transformation de Fourier — https://www.numdam.org/item/AUG_1947-1948__23__7_0.pdf; retrieval ID `turn600131709view4`.

- Théorie des distributions et transformation de Fourier — https://www.numdam.org/item/AUG_1947-1948__23__7_0.pdf; retrieval ID `turn600131709view5`.

Access failure occurred in this batch. The full diagnostic is preserved in the local raw record. No failed URL is represented as a checked theorem.

### Batch 27

Read Katz–Lang Lemma2 proof and§2 elementary-fibration references in full at the targeted passage. Smooth-surjective normal-base version is exact; broader reduced-fibre wording remains unresolved. Divisor localization proof checked separately.

```json
{
  "open": [
    {
      "ref_id": "turn738562895view0",
      "lineno": 256
    },
    {
      "ref_id": "turn382597057view4",
      "lineno": 3370
    }
  ],
  "response_length": "long"
}
```

Returned source records (titles and URLs; presence here alone does not certify opening or proof):

- PDF-Export ETH-Konsortium: Dokumente — https://web.math.princeton.edu/~nmk/old/AbsFinThm.pdf; retrieval ID `turn179698758view0`.

- -------------------------------------------------------------------------------- — https://stacks.math.columbia.edu/download/divisors.pdf; retrieval ID `turn179698758view1`.

### Batch 28

Targeted primary search for Mumford theta groups and Weil pairing to make the elliptic nonsplitting example algebraic before formal completion.

```json
{
  "system1_search_query": [
    {
      "q": "Mumford On the equations defining abelian varieties I theta group commutator Weil pairing pdf"
    },
    {
      "q": "site.math.ru.nl bmoonen theta groups Weil pairing Heisenberg group line bundle"
    }
  ],
  "response_length": "long"
}
```

Returned source records (titles and URLs; presence here alone does not certify opening or proof):

- On the Equations Defining Abelian Varieties. I — https://dash.harvard.edu/entities/publication/73120378-82a4-6bd4-e053-0100007fdf3b; retrieval ID `turn758143310search0`.

- On the equations defining abelian varieties. I — https://pazuki.perso.math.cnrs.fr/index_fichiers/Mumford66.pdf; retrieval ID `turn758143310search4`.

- Webpage of Ben Moonen — https://www.math.ru.nl/~bmoonen/research.html; retrieval ID `turn758143310search1`.

- Chapter VIII. — https://www.math.ru.nl/~bmoonen/BookAV/ThetaGr.pdf; retrieval ID `turn758143310search5`.

- -------------------------------------------------------------------------------- — https://mathweb.ucsd.edu/~doprea/206w24.html; retrieval ID `turn758143310search2`.

- A trace–path integral formula over function fields — https://londmathsoc.onlinelibrary.wiley.com/doi/full/10.1112/jlms.70664; retrieval ID `turn758143310search3`.

- Homogeneous projective bundles over abelian varieties — https://www-fourier.ujf-grenoble.fr/~mbrion/hpba_new.pdf; retrieval ID `turn758143310search6`.

### Batch 29

Opened Mumford1966 and Moonen theta-group chapter. Read symmetric multiplication formula, group extension and commutator definitions.

```json
{
  "open": [
    {
      "ref_id": "https://pazuki.perso.math.cnrs.fr/index_fichiers/Mumford66.pdf"
    },
    {
      "ref_id": "https://www.math.ru.nl/~bmoonen/BookAV/ThetaGr.pdf"
    }
  ],
  "response_length": "long"
}
```

Returned source records (titles and URLs; presence here alone does not certify opening or proof):

- On the equations defining abelian varieties. I — https://pazuki.perso.math.cnrs.fr/index_fichiers/Mumford66.pdf; retrieval ID `turn687716350view0`.

- AV — https://www.math.ru.nl/~bmoonen/BookAV/ThetaGr.pdf; retrieval ID `turn687716350view1`.

### Batch 30

Read Mumford§1 Theorem1 pp293–294 and Moonen8.24–8.25. Nondegenerate theta commutator supports the explicit finite tame covering, whose formal completion was then checked independently.

```json
{
  "find": [
    {
      "ref_id": "turn687716350view0",
      "pattern": "non-degenerate"
    },
    {
      "ref_id": "turn687716350view0",
      "pattern": "Corollary 1"
    },
    {
      "ref_id": "turn687716350view1",
      "pattern": "8.24"
    }
  ],
  "response_length": "long"
}
```

Returned source records (titles and URLs; presence here alone does not certify opening or proof):

- On the equations defining abelian varieties. I — https://pazuki.perso.math.cnrs.fr/index_fichiers/Mumford66.pdf; retrieval ID `turn777327259view0`.

- On the equations defining abelian varieties. I — https://pazuki.perso.math.cnrs.fr/index_fichiers/Mumford66.pdf; retrieval ID `turn777327259view1`.

- AV — https://www.math.ru.nl/~bmoonen/BookAV/ThetaGr.pdf; retrieval ID `turn777327259view2`.

### Batch 31

SGA4I PDF URL exceeded the web parser size. The parent-fetched original PDF was read visually at I8.13.2–4 and8.3.2–3. Exact categorical hypotheses saved in SGA4_8133_check.md; this is an auxiliary check for root scans105/183.

```json
{
  "open": [
    {
      "ref_id": "https://library.slmath.org/nonmsri/sga/sga/pdf/sga4-1.pdf"
    }
  ],
  "response_length": "short"
}
```

Access failure occurred in this batch. The full diagnostic is preserved in the local raw record. No failed URL is represented as a checked theorem.

### Batch 32

Reopened exact SGA1 X2.10–2.11 for the cross-package Bertini audit. The proper normal hyperplane theorem does not alone justify arbitrary local-property clauses or naive iteration through nonnormal special sections.

```json
{
  "find": [
    {
      "ref_id": "https://arxiv.org/pdf/math/0206203",
      "pattern": "2.10."
    },
    {
      "ref_id": "https://arxiv.org/pdf/math/0206203",
      "pattern": "2.11."
    }
  ],
  "response_length": "long"
}
```

Returned source records (titles and URLs; presence here alone does not certify opening or proof):

- arXiv:math/0206203v2  [math.AG]  4 Jan 2004 — https://arxiv.org/pdf/math/0206203; retrieval ID `turn873764662view0`.

- arXiv:math/0206203v2  [math.AG]  4 Jan 2004 — https://arxiv.org/pdf/math/0206203; retrieval ID `turn873764662view1`.

### Batch 33

Targeted local Bertini, geometric-unibranch and morphisme net searches. Relevant SGA2/EGA and later Zhang leads appeared; no exact combined draft local-property theorem was identified from primary text. Root was advised to retain classC for that combined claim.

```json
{
  "system1_search_query": [
    {
      "q": "\"Bertini\" \"géométriquement unibranche\" \"EGA\""
    },
    {
      "q": "\"EGA\" \"6.14\" \"Bertini\" normal"
    },
    {
      "q": "\"Bertini\" \"morphisme net\" Grothendieck"
    }
  ],
  "response_length": "long"
}
```

Returned source records (titles and URLs; presence here alone does not certify opening or proof):

- Exposé XIII · Problèmes liés au \pi_0: théorèmes de Bertini locaux — SGA 2 — https://grothendiecksga.com/read/sga2/fr/XIII-2.html; retrieval ID `turn623546237search0`.

- Exposé X · 5. Schéma des homomorphismes d'un groupe de type multiplicatif dans un autre. Groupes constants tordus et groupes de type multiplicatif — SGA 3 — https://grothendiecksga.com/read/sga3/fr/X-5.html; retrieval ID `turn623546237search1`.

- PUBLICATIONS MATHÉMATIQUES DE L’I.H.É.S. — https://wstein.org/sga/circle/EGAIV.2.pdf; retrieval ID `turn623546237search8`.

- Analytic branches and hypersurface sections — https://www.researchgate.net/publication/44197259_Analytic_branches_and_hypersurface_sections; retrieval ID `turn623546237search2`.

- Foncteurs fibres, supports, etude cohomologique des morphismes finis — https://fabrice.orgogozo.perso.math.cnrs.fr/SGA4/originaux/SGA4-VIIIo.pdf; retrieval ID `turn623546237search9`.

- Exposé XVII · 3. La variété duale — SGA 7 — https://grothendiecksga.com/read/sga7/fr/17-3.html; retrieval ID `turn623546237search3`.

- SGA 1 Par A. Grothendieck | PDF | Groupe (Mathématiques) | Structures mathématiques — https://fr.scribd.com/document/746087845/SGA-1-par-A-Grothendieck; retrieval ID `turn623546237search4`.

- § 6. Compléments d’algèbre commutative 149 — https://williamstein.org/sga/ega1.pdf; retrieval ID `turn623546237search10`.

- Exposé I · Quelques compléments — SGA 1 — https://grothendiecksga.com/read/sga1/fr/I-11.html; retrieval ID `turn623546237search5`.

- Flat morphisms — SGA 1 — https://grothendiecksga.com/read/sga1/en/IV.html; retrieval ID `turn623546237search6`.

- Morphismes plats — SGA 1 — https://grothendiecksga.com/read/sga1/fr/IV.html; retrieval ID `turn623546237search7`.

### Batch 34

Targeted Jouanolou1983 locators and book access. Publisher/library metadata did not expose the book; Poonen’s primary talk slides gave a useful exact-quantifier lead.

```json
{
  "system2_search_query": [
    {
      "q": "Jouanolou Théorèmes Bertini applications 1983 6.10 pdf"
    },
    {
      "q": "\"Jouanolou\" \"6.10\" \"geometrically irreducible\""
    }
  ],
  "response_length": "long"
}
```

Returned source records (titles and URLs; presence here alone does not certify opening or proof):

- Bibliography entry—The Stacks project — https://stacks.math.columbia.edu/bibliography/Jou; retrieval ID `turn641120173search0`.

- Théorèmes de Bertini et applications — https://books.google.com/books/about/Th%C3%A9or%C3%A8mes_de_Bertini_et_applications.html?id=Q0vvAAAAMAAJ; retrieval ID `turn641120173search1`.

- Théorèmes de Bertini et Applications af Jean-Pierre Jouanolou | bibliotek.dk — https://bibliotek.dk/materiale/theoremes-de-bertini-et-applications_jean-pierre-jouanolou/work-of%3A800010-katalog%3A99122433387205763; retrieval ID `turn641120173search2`.

- Théorèmes de Bertini et applications (1979) by Jean-Pierre Jouanolou | Open Library — https://openlibrary.org/books/OL57367304M/Th%C3%A9or%C3%A8mes_de_Bertini_et_applications; retrieval ID `turn641120173search3`.

- BULLETIN BIBLIOGRAPHIQUE — https://www.e-periodica.ch/cntmng?pid=ens-001%3A1984%3A30%3A%3A97; retrieval ID `turn641120173search24`.

- Théorèmes de Bertini et applications (1979) by Jean-Pierre Jouanolou | Open Library — https://openlibrary.org/books/OL3173456M/The%CC%81ore%CC%80mes_de_Bertini_et_applications?show_page_status=1; retrieval ID `turn641120173search4`.

- Théorèmes de Bertini et applications (1979) by Jean-Pierre Jouanolou | Open Library — https://openlibrary.org/books/OL61640128M/Th%C3%A9or%C3%A8mes_de_Bertini_et_applications; retrieval ID `turn641120173search5`.

- Bertini irreducibility theorems via statistics — https://math.mit.edu/~poonen/slides/bertini_locus.pdf; retrieval ID `turn641120173search25`.

- www.oeaw.ac.at — https://www.ricam.oeaw.ac.at/files/reports/18/rep18-26.pdf; retrieval ID `turn641120173search26`.

- [Jou83] J.P. Jouanolou. *Théorèmes de Bertini et applications.* Progress in mathematics (Birkhäuser) 42. Birkhäuser, 1983. — https://web.dm.uba.ar/files/tesis_lic/2023/Lanciano.pdf; retrieval ID `turn641120173search27`.

- Horizon Information Portal — https://library.hs.ias.edu/ipac20/ipac.jsp?aspect=basic_search&menu=search&profile=hslib&session=K78133955FM97.2341903&source=~%21horizon&term=Bertini%27s+theorems&uindex=SW; retrieval ID `turn641120173search6`.

- LE T — https://archive.numdam.org/item/10.24033/bsmf.2619.pdf; retrieval ID `turn641120173search28`.

- these.dvi — https://www.math.ens.psl.eu/~debarre/conduche.pdf; retrieval ID `turn641120173search29`.

- Théorèmes de Bertini et applications — https://ci.nii.ac.jp/ncid/BA00556045.amp; retrieval ID `turn641120173search7`.

- Journal of the American Mathematical Society — https://doi.org/10.1090/jams/847; retrieval ID `turn641120173search8`.

- References mmj455 — https://www.mathnet.ru/links/6ba8641620817b04fac7f53aba686b55/mmj_455_refs_eng.htm; retrieval ID `turn641120173search9`.

- An application of Bertini Theorem — https://www.researchgate.net/publication/327644079_An_application_of_Bertini_Theorem; retrieval ID `turn641120173search10`.

- Points entiers et théorèmes de Bertini arithmétiques - Tome (2001) no. 595 — https://archive.numdam.org/item/BJHTUP11_2001__0595__A1_0/?source=AIF_2001__51_6_1507_0; retrieval ID `turn641120173search11`.

- ag.algebraic geometry - Connected variety has almost everywhere connected reduction? - MathOverflow — https://mathoverflow.net/questions/514289/connected-variety-has-almost-everywhere-connected-reduction; retrieval ID `turn641120173search12`.

- Theorem of Bertini — https://en.wikipedia.org/wiki/Theorem_of_Bertini; retrieval ID `turn641120173search30`.

- The Tate Conjecture for Surfaces of Geometric Genus One -- Overcoming Singularities — https://www.researchgate.net/publication/388529439_The_Tate_Conjecture_for_Surfaces_of_Geometric_Genus_One_--_Overcoming_Singularities; retrieval ID `turn641120173search13`.

- eoinmackall – Page 2 – Colorful Algebra — https://eoinmackall.wordpress.com/author/eoinmackall/page/2/; retrieval ID `turn641120173search14`.

- Geometry, integrability and bifurcation diagrams of a family of quadratic differential systems as application of the Darboux theory of integrability — https://www.academia.edu/77260988/Geometry_integrability_and_bifurcation_diagrams_of_a_family_of_quadratic_differential_systems_as_application_of_the_Darboux_theory_of_integrability; retrieval ID `turn641120173search15`.

- Families of rationally simply connected varieties over surfaces and torsors for semisimple groups — https://www.researchgate.net/publication/2207463_Families_of_rationally_simply_connected_varieties_over_surfaces_and_torsors_for_semisimple_groups; retrieval ID `turn641120173search16`.

- Abelian Varieties Milne | PDF | Teaching Methods & Materials — https://www.scribd.com/doc/290817169/abelian-varieties-milne; retrieval ID `turn641120173search17`.

- On the possible genera of smooth curves contained in some forms of projective space – Colorful Algebra — https://eoinmackall.wordpress.com/2019/09/16/on-the-possible-genera-of-smooth-curves-contained-in-some-forms-of-projective-space/; retrieval ID `turn641120173search18`.

- Algebraic Groups: Structure and Actions 9781470426019, 1470426013 - DOKUMEN.PUB — https://dokumen.pub/algebraic-groups-structure-and-actions-9781470426019-1470426013.html; retrieval ID `turn641120173search19`.

- A Fulton–Hansen theorem for almost homogeneous spaces — https://link.springer.com/article/10.1007/s40574-021-00302-8; retrieval ID `turn641120173search20`.

- The geometry of algebraic cycles. Proceedings of the conference, Columbus, OH, USA, March 25–29, 2008 — https://www.academia.edu/85737235/The_geometry_of_algebraic_cycles_Proceedings_of_the_conference_Columbus_OH_USA_March_25_29_2008; retrieval ID `turn641120173search21`.

- Bloch's formula for 0-cycles with modulus and higher dimensional Class Field Theory — https://www.researchgate.net/publication/339066036_Bloch%27s_formula_for_0-cycles_with_modulus_and_higher_dimensional_Class_Field_Theory; retrieval ID `turn641120173search22`.

- hypersurfaces in projective schemes and a moving lemma — https://paperzz.com/doc/7229748/hypersurfaces-in-projective-schemes-and-a-moving-lemma; retrieval ID `turn641120173search23`.

### Batch 35

Opened Poonen’s8 May2020 slides and Stacks Bertini chapter; located the Poonen–Slavov primary research paper. No conclusion was drawn from its abstract alone.

```json
{
  "system1_search_query": [
    {
      "q": "Poonen Slavov Bertini irreducibility theorems statistics pdf"
    },
    {
      "q": "Jouanolou Bertini 6.10 1983 pdf theorem geometric irreducibility"
    }
  ],
  "open": [
    {
      "ref_id": "https://math.mit.edu/~poonen/slides/bertini_locus.pdf"
    },
    {
      "ref_id": "https://stacks.math.columbia.edu/tag/0G4C"
    }
  ],
  "response_length": "long"
}
```

Returned source records (titles and URLs; presence here alone does not certify opening or proof):

- THE EXCEPTIONAL LOCUS IN THE — https://math.mit.edu/~poonen/papers/bertini_locus.pdf; retrieval ID `turn368939067search7`.

- The Exceptional Locus in the Bertini Irreducibility Theorem for a Morphism — https://dspace.mit.edu/entities/publication/80e77923-1c5a-4869-bb02-8e996f0f7ada; retrieval ID `turn368939067search0`.

- Bertini irreducibility theorems via statistics — https://math.mit.edu/~poonen/slides/bertini_locus.pdf; retrieval ID `turn368939067search8`.

- Bertini irreducibility theorems via statistics | Mathematics — https://mathematics.stanford.edu/events/algebraic-geometry/bertini-irreducibility-theorems-statistics; retrieval ID `turn368939067search1`.

- Bjorn Poonen — https://klein.mit.edu/~poonen/index.html; retrieval ID `turn368939067search2`.

- Bertini theorems over ﬁnite ﬁelds — https://www.math.mcgill.ca/goren/cnta7/invited/Poonen.pdf; retrieval ID `turn368939067search9`.

- Bibliography entry—The Stacks project — https://stacks.math.columbia.edu/bibliography/Jou; retrieval ID `turn368939067search3`.

- Bertini irreducibility theorems via statistics — https://math.mit.edu/~poonen/slides/bertini_locus.pdf; retrieval ID `turn368939067view0`.

- Section 37.32 (0G4C): Bertini theorems—The Stacks project — https://stacks.math.columbia.edu/tag/0G4C; retrieval ID `turn368939067view1`.

### Batch 36

Opened Poonen–Slavov author PDF and located Theorems1.5/1.8; reopened Stacks37.32.3 and its algebraic proof. Theorem1.5’s equidimensional-fibre assumption was not omitted.

```json
{
  "open": [
    {
      "ref_id": "https://math.mit.edu/~poonen/papers/bertini_locus.pdf"
    }
  ],
  "find": [
    {
      "ref_id": "https://math.mit.edu/~poonen/papers/bertini_locus.pdf",
      "pattern": "Jouanolou"
    },
    {
      "ref_id": "https://stacks.math.columbia.edu/tag/0G4C",
      "pattern": "37.32.3"
    }
  ],
  "response_length": "long"
}
```

Returned source records (titles and URLs; presence here alone does not certify opening or proof):

- -------------------------------------------------------------------------------- — https://math.mit.edu/~poonen/papers/bertini_locus.pdf; retrieval ID `turn494904871view1`.

- Section 37.32 (0G4C): Bertini theorems—The Stacks project — https://stacks.math.columbia.edu/tag/0G4C; retrieval ID `turn494904871view2`.

### Batch 37

Read Poonen–Slavov Theorem1.8 and Lemma7.1 with§7 proof. The exceptional-divisor hyperplanes form a proper locus, so image dimension≥2 gives generic geometric irreducibility for arbitrary morphisms. This exactly supplies the corrected generic statement needed for root240 and earlier67.

```json
{
  "open": [
    {
      "ref_id": "turn494904871view0",
      "lineno": 65
    }
  ],
  "response_length": "long"
}
```

### Batch 38

Searched publication and circulation dates for Poonen–Slavov; located arXiv2001.08672 and publisher metadata.

```json
{
  "system2_search_query": [
    {
      "q": "arxiv \"The exceptional locus in the Bertini irreducibility theorem for a morphism\""
    }
  ],
  "response_length": "short"
}
```

Returned source records (titles and URLs; presence here alone does not certify opening or proof):

- The exceptional locus in the Bertini irreducibility theorem for a morphism — https://arxiv.org/abs/2001.08672; retrieval ID `turn814842623academia12`.

- The Exceptional Locus in the Bertini Irreducibility Theorem for a Morphism — https://dspace.mit.edu/entities/publication/80e77923-1c5a-4869-bb02-8e996f0f7ada; retrieval ID `turn814842623search0`.

- The Exceptional Locus in the Bertini Irreducibility Theorem for a Morphism — https://dspace.mit.edu/entities/publication/5101c574-cabb-4c43-aaae-14f0eddd4413; retrieval ID `turn814842623search1`.

- The Exceptional Locus in the Bertini Irreducibility Theorem for a Morphism — https://academic.oup.com/imrn/article-abstract/2022/6/4503/5879258; retrieval ID `turn814842623search2`.

- THE EXCEPTIONAL LOCUS IN THE — https://math.mit.edu/~poonen/papers/bertini_locus.pdf; retrieval ID `turn814842623search13`.

- Bjorn Poonen — https://klein.mit.edu/~poonen/index.html; retrieval ID `turn814842623search3`.

- The exceptional locus in the Bertini irreducibility theorem for a morphism — https://scixplorer.org/abs/2020arXiv200108672P/abstract; retrieval ID `turn814842623search4`.

- Volume 2022 Issue 6 | International Mathematics Research Notices | Oxford Academic — https://academic.oup.com/imrn/issue/2022/6; retrieval ID `turn814842623search5`.

- The Exceptional Locus in the Bertini Irreducibility Theorem for a Morphism - MaRDI portal — https://portal.mardi4nfdi.de/wiki/The_Exceptional_Locus_in_the_Bertini_Irreducibility_Theorem_for_a_Morphism; retrieval ID `turn814842623search6`.

- Volume 2022 Issue 6 | International Mathematics Research Notices | Oxford Academic — https://academic.oup.com/imrn/issue/2022/6?browseBy=volume; retrieval ID `turn814842623search7`.

- The exceptional locus in the Bertini irreducibility theorem for a morphism — https://shamra-academia.com/index.php/en/show/5d39a941ccb87; retrieval ID `turn814842623search8`.

- The exceptional locus in the Bertini irreducibility theorem for a morphism — https://shamra-academia.com/en/show/5d39a941ccb87; retrieval ID `turn814842623search9`.

- The Exceptional Locus in the Bertini Irreducibility Theorem for a Morphism — https://sonar.ch/global/documents/234198; retrieval ID `turn814842623search10`.

- A BERTINI TYPE THEOREM FOR PENCILS OVER FINITE — https://personal.math.ubc.ca/~dghioca/papers/0627_Bertini_for_pencils.pdf; retrieval ID `turn814842623search14`.

- The exceptional locus in the Bertini irreducibility theorem for a morphism — https://www.emergentmind.com/papers/2001.08672; retrieval ID `turn814842623search11`.

- BJORN POONEN — https://math.berkeley.edu/~poonen/papers/cv.pdf; retrieval ID `turn814842623search15`.

- A BERTINI TYPE THEOREM FOR PENCILS OVER FINITE FIELDS — 11 — https://webpages.scu.edu/ftp/sasgarli/bertini-for-pencils.pdf; retrieval ID `turn814842623search16`.

- Davide Gori – Curriculum Vitae — https://phd.uniroma1.it/dottorati/cartellaDocumentiWeb/84bee7ca-ba87-4fa5-b039-47fedb85feec.pdf; retrieval ID `turn814842623search17`.

- Bjorn Poonen C.V. — https://math.mit.edu/~poonen/papers/cv.pdf; retrieval ID `turn814842623search18`.

### Batch 39

Opened arXiv record confirming first23 January2020 and revised4 August2020. Publisher article URL redirected to an inaccessible endpoint; print issue metadata is reported only as a search lead.

```json
{
  "open": [
    {
      "ref_id": "https://arxiv.org/abs/2001.08672"
    },
    {
      "ref_id": "https://academic.oup.com/imrn/article-abstract/2022/6/4503/5879258"
    }
  ],
  "response_length": "short"
}
```

Returned source records (titles and URLs; presence here alone does not certify opening or proof):

- [2001.08672] The exceptional locus in the Bertini irreducibility theorem for a morphism — https://arxiv.org/abs/2001.08672; retrieval ID `turn477998028view0`.

Access failure occurred in this batch. The full diagnostic is preserved in the local raw record. No failed URL is represented as a checked theorem.

## Direct PDF fetches and visual inspection

`fetch_primary.py` and `fetch_primary.out` record the successful public SGA7I download, HTTP status, byte length and SHA-256. The original PDF was read at IX7.1.5–7.2.6, printed pp402–407, and adjacent construction pages. `read_log.md` records the exact page ranges. The full copyrighted book and extracted page images remain in the excluded reference cache.

The original SGA4I PDF was supplied locally by root. This reviewer opened its URL in batch31, which the web parser rejected for size, then read the local page images at I8.13.2–4 pp136–138 and8.3.2–3 pp75–76. The trial OCR on PDF90 hung and was interrupted; no OCR text was used. Exact conclusions are in `SGA4_8133_check.md`.

`fetch_egai.py` records an additional attempt to retrieve the original EGAI PDF after the web parser size failure. Its actual completion/failure is in `fetch_egai.out`; the bibliography and reading alert are updated only if the exact original proposition is subsequently read.

Cross-package later Bertini and curve-extension endpoints were read directly as recorded in `read_log.md`; root owns their claim rows. Absent Hua, LM1, S6, RESULTS_STATE and other project documents were not searched as though their assertions were established mathematics. Their presence in earlier notes is an attributed lead only.
