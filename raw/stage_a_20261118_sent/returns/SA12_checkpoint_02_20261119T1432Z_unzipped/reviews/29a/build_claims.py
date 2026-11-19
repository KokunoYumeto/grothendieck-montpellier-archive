"""Serialize claims individually formulated after reading the original passages.
Shared locators are inherited from the manually written item map, not inferred by keywords.
"""
import json
from pathlib import Path
P=Path(__file__).parent
I={x['id']:x for x in json.loads((P/'items.json').read_text())}
C=[]
def c(n,items,words,statement,status,cls,fate,refs,computation='No numerical computation on the page; see stated proof obligations.',confidence='medium',date='As of 2026-11-19; publication dates specified in fate.',scans=None,lines=None):
    ii=[I[f'SA12-{i}'] for i in items]
    C.append(dict(id=f'CL-SA12-{n:03}',items=[i['id'] for i in ii],cote=29,
        scans=scans or sorted({s for i in ii for s in i['scans']}),lines=lines or list(dict.fromkeys(l for i in ii for l in i['lines'])),
        his_statement=words,statement=statement,status_on_pages=status,computation=computation,
        **{'class':cls},fate=fate,fate_date=date,present_status=f'2026-11-19: {fate}',refs=refs,confidence=confidence))

c(1,[3],'je crois; revêtement étale de Y',
'A finite étale covering of X trivial over its geometric generic fibre descends to a finite étale covering of normal integral Y, under the faithfully flat finite-type and reduced-fibre qualifier on initial scan48; that qualifier is unresolved.',
'proof sketched; self-flagged','C',
'The field-base generic-fibre assertion is SGA1 IX §6. Normalization and generic descent have established forms, but the precise nonproper flat biréduit/réduit version on these leaves was not matched to an opened theorem. Stacks 0BUM proves a proper flat finite-presentation variant and does not settle this exact qualifier. The unresolved remainder is identification of the written hypotheses, not an assertion that generic descent is open.',
['SGA1_1971','Stacks0BUM','Stacks0BQJ'],scans=[48,50])
c(2,[3],'π₁(X_ȳ) → π₁(X) → π₁(Y) → 0',
'With the same hypotheses as CL-SA12-001 and geometric basepoints, the generic-fibre sequence is exact if the preceding covering-descent lemma holds.',
'proof sketched; conditional on descent','C',
'The Galois-category deduction from the asserted covering descent is valid. SGA1 IX §6 and the proper homotopy theorem are established comparisons; no passage opened establishes the unresolved biréduit/réduit nonproper generality verbatim.',
['SGA1_1971','Stacks0BUM','Stacks0BN6'])
c(3,[4],'f_*(F) est constructible',
'For finite-type f:X→Y with Y locally noetherian universally Japanese, direct image of a constructible finite-set étale sheaf is constructible.',
'stated without proof','B',
'Déglise, Finitude et constructibilité en cohomologie étale, Theorem1.1 (account of Gabber), proves the stronger degree-zero result for every noetherian base, with no excellence hypothesis. Theorem1.2 concerns R¹ under different torsion and quasi-excellence assumptions and is not used to strengthen the manuscript claim.',
['DegliseGabber2007'],confidence='high',date='Gabber result presented in the opened 2007 course notes; precise first circulation not established.')
c(4,[5],'l’application … est à fibres finies',
'For a noetherian universally Japanese X, a finite locally closed partition X_i, and finite constant G, restriction H¹(X,G)→∏H¹(X_i,G) has finite fibres.',
'stated without proof','C',
'The finite reconstruction/gluing problem is closely tied to constructibility of finite sheaves. Searches for the exact universal-Japanese partition lemma did not locate its numbered published form. Déglise Theorem1.1 verifies the needed degree-zero finiteness framework, not this entire nonabelian finite-fibre conclusion. No proof certification is assigned.',
['DegliseGabber2007','SGA1_1971'])
c(5,[6],'Hom(F,G) est fini',
'For constructible finite-set étale sheaves F,G on a noetherian scheme, Hom(F,G) is finite.',
'proof sketched','E',
'This is standard constructible-sheaf finiteness: choose a common finite stratification into connected locally closed pieces where both are finite locally constant; finitely many geometric stalk maps determine a morphism. The elementary proof is independently supplied. The opened constructibility reference supplies the setting; no exact priority date is claimed.',
['DegliseGabber2007'],computation='Independent proof in independent_checks.md §1; no numerical experiment.',confidence='high')
c(6,[7],'Les conditions suivantes sont équivalentes',
'For a noetherian universally Japanese base S and finite G, finiteness of H¹(X,G) for every finite-type X/S is reduced to smooth affine X→S′ with nonempty geometrically connected fibres, where S′ is finite étale over a normal integral affine subscheme S₀ of S, after shrinking the base to a nonempty open.',
'proof sketched','C',
'The required normal-base covers, shrinking, and dimension induction are explicit. SGA1 X2.12 gives Lang–Serre finiteness over algebraically closed fields, and modern Gabber constructibility handles a key sheaf-theoretic input. Searches did not identify an exact published theorem with all these base quantifiers. The precise equivalence is retained as a searched historical proof task, not declared a new open theorem.',
['SGA1_1971','DegliseGabber2007'],scans=[54,56])
c(7,[7],'sous-groupes de G×G; si G est abélien',
'A sufficient H¹-finiteness criterion combines finiteness for geometric fibres with finiteness on all required base covers for every subgroup H≤G×G; for abelian G the author says G alone suffices.',
'proof sketched','C',
'The G×G quantifier belongs to the descent comparison of two torsors and cannot be replaced by a statement only about H¹(S,G). The exact quantified sufficient criterion was searched alongside CL-SA12-006 and not found verbatim in the opened sources. Neither finite H¹ for every target nor this criterion implies finite generation of an arbitrary profinite group.',
['SGA1_1971','DegliseGabber2007'],computation='The earlier-run small-but-not-finitely-generated profinite example is proved in independent_checks.md; it tests an inference, not this theorem.')
c(8,[7,9],'ordre premier aux caractéristiques résiduelles',
'The proposed global H¹-finiteness consequences restrict G to order prime to all residue characteristics and require the preceding normal-base finiteness assumptions.',
'proof sketched','C',
'Prime-to-characteristic geometric finiteness is established in SGA1 X and XIII. The complete arithmetic-base version still inherits the quantified assumptions of CL-SA12-006/007, whose exact generality was not matched to a printed theorem. Removing the restriction on affine schemes is false: Artin–Schreier classes x^m, p∤m, yield infinitely many Z/p-torsors on A¹ in characteristic p.',
['SGA1_1971','ESS2021'],computation='Artin–Schreier polynomial reductions in checks.py/checks.out, with the infinite-family degree argument in independent_checks.md.',confidence='high')
c(9,[81],'Prop ? … courbe … lisse',
'If every smooth algebraic curve over a fixed field k has finitely many finite étale covers of each degree, does every finite-type k-scheme have that property?',
'open on the pages','C',
'The curve-fibration and constructibility reduction is a plausible route; SGA1 proves the important geometric prime-to-p/proper cases, while affine wild covers show that the premise is substantial. Exact all-fields, all-finite-type quantifiers were searched but not matched. This record does not call the question presently open: its exact published fate remains unlocated.',
['SGA1_1971','DegliseGabber2007','ESS2021'])
c(10,[10],'à fibres géom. connexes non vides, de dim 1',
'The induction seeks, after dense-open shrinking and appropriate treatment of constants, a smooth curve fibration with nonempty geometrically connected fibres and a lower-dimensional base.',
'proof sketched; construction left to detail','C',
'Generic projection, separating transcendence bases, and shrinking give such fibrations under the relevant separability assumptions. The arbitrary-field formulation needs those assumptions stated, and the page does not supply them. The exact construction was searched within the finiteness and Bertini references; no unrestricted version is certified.',
['SGA1_1971','Stacks0G4C'])
c(11,[11],'topologiquement de génération finie',
'For an algebraic scheme over an algebraically closed field of characteristic exponent p, the maximal prime-to-p quotient of its étale fundamental group is topologically finitely generated.',
'proof sketched','A',
'The generic-section and tame-curve method appears in SGA1 X and XIII; finite generation in the stated geometric setting is established. Full étale finite generation for an affine variety in positive characteristic is false. ESS2021 strengthens the tame group for a smooth variety with a good compactification to finite presentation, and LSS2023 proves finite presentation for all connected proper schemes; those are different hypotheses.',
['SGA1_1971','ESS2021','LSS2023'],confidence='high')
c(12,[13,85],'Question; Quid ?; Si on sait',
'For a finite étale cover of U×Y tame along the indicated normalized codimension-one boundary, triviality on the fibre over a chosen rational point y should imply descent from a neighbourhood of y in Y. The normal/proper hypotheses differ between witnesses.',
'open on the pages; competing theorem/question readings','C',
'Tame homotopy and product theorems have established forms, but exact recovery here depends on properness, geometric tameness, and the chosen compactification. SGA1 XIII and Esnault–Kindler supply precise related theorems; neither is cited as settling every witness variant. The remaining task is a quantified reconstruction and comparison.',
['SGA1_1971','EK2016','EKerr2016'],scans=[62])
c(13,[13],'À détailler',
'Extend the fibrewise tame-covering descent argument from a normal ambient X to a nonnormal X by descent.',
'self-flagged proof step','C',
'Finite étale coverings satisfy effective descent in the usual descent settings, but compatibility of the page’s normalization-boundary definition of tameness requires its own argument. The exact nonnormal extension was searched in SGA1 and the tame-covering literature without locating a theorem that matches these abbreviated hypotheses.',
['SGA1_1971','EK2016','GM1971'],scans=[63])
c(14,[13,27],'π₁^t(X×Y)',
'The proposed tame product formula uses compactifications and tameness at boundary divisors; its exact formulation is conditional on the preceding descent statement.',
'proof sketched; dependent on preceding step','C',
'Tame product results are established with specified notions of tameness. No unconditional identification of every boundary-tame quotient in this draft is made here. SGA1 XIII and modern tame finiteness references were searched, and the missing hypotheses remain explicit.',
['SGA1_1971','ESS2021','EK2016'],scans=[63])
c(15,[27],'π′₁(X×Y)≃π′₁(X)×π′₁(Y)',
'For connected algebraic schemes over an algebraically closed field, the prime-to-characteristic fundamental group obeys the product formula in the indicated geometric setting.',
'proof sketched','A',
'The prime-to-p product theorem is part of SGA1 XIII’s tame framework. It does not assert the unrestricted affine product formula: z^p−z=xy gives the obstruction in characteristic p. Proper-factor product theorems have different scope.',
['SGA1_1971','ESS2021'],computation='Mixed Artin–Schreier class xy tested in checks.py/checks.out and justified by highest-degree terms in independent_checks.md.',confidence='high',scans=[63,65])
c(16,[27],'π₁(X×Y) → π₁(X)×π₁(Y) est surjectif',
'For connected schemes over an algebraically closed field with geometric basepoints and the finite-type geometric hypotheses here, the full product map of étale fundamental groups is surjective.',
'proof sketched','E',
'The section maps induced by fixed geometric points show that the image in the product contains each of its two factors, hence is the whole product. This does not assert that the chosen lifted subgroups commute in the source. The elementary argument does not prove injectivity. SGA1 supplies the framework.',
['SGA1_1971'],confidence='high',scans=[65])
c(17,[11,19],'génération finie | présentation finie',
'For a proper normal compactification, the quotient of π₁ of its open part obtained by killing wild inertia at codimension-one boundary is asserted finitely generated; Codex instead reads finitely presented.',
'stated without proof; strength unresolved','C',
'Finite generation via a fixed tame curve is compatible with SGA1 XIII and Lefschetz. Finite presentation is proved by ESS2021 for smooth varieties admitting good compactifications, and LSS2023 for proper schemes; these do not automatically cover arbitrary singular compactifications and this exact divisorial quotient. The FG/FP reading is a material unresolved issue.',
['SGA1_1971','ESS2021','LSS2023','EK2016','EKerr2016'])
c(18,[11,18],'codim ≥2; génération finie',
'If X is a proper normal variety over an algebraically closed field and Z⊂X has codimension at least two, π₁(X\u2216Z) is claimed topologically finitely generated.',
'proof sketched','C',
'The fixed generic-curve connectedness argument independently gives the claimed finite generation in the normal setting, using the established SGA1 X hyperplane method. The opened printed lemma itself treats proper normal schemes, so the codimension-two open variant is labelled a reconstruction rather than a verbatim theorem match. Normality ensures connected finite covers remain irreducible on the dense open. The separate question about finite generation of the kernel is not settled by this assertion.',
['SGA1_1971','Stacks0BN6'],confidence='medium')
c(19,[14],'composantes … codim ≥2',
'The codimension-two finite-generation argument is extended through irreducible components and gluing; the written reduction also invokes Chow’s lemma.',
'proof sketched with a defective intermediate inference','C',
'Finiteness can be treated by finite component/gluing arguments, but the statement that the full inverse image of a codimension-two omitted set stays codimension two under a projective modification is false. The target theorem must be separated from that step; modern proper finite presentation alone does not prove this open-subscheme assertion.',
['SGA1_1971','LSS2023'],scans=[66])
c(20,[14],'Y′ … de codim ≥2',
'The full inverse image of the excluded codimension-two set is assumed to have codimension at least two after an unspecified Chow modification.',
'false as an automatic inference; possible extra hypothesis','C',
'Blowing up a closed point on a smooth surface produces an exceptional divisor, so the claimed automatic codimension preservation fails. This is an independent refutation of the inference; the exact placement as an assumption versus conclusion needs the scan. The corrected statement must separately control exceptional divisors.',
['StacksBlowup'],computation='Explicit surface blowup chart in checks.py/checks.out; geometric dimension verification in independent_checks.md.',confidence='high',scans=[66])
c(21,[16],'k corps; X irréductible',
'The indicated generic linear-section irreducibility theorem over an arbitrary field requires geometric irreducibility of X when the generic parameter field is algebraically closed.',
'false as transcribed; strengthened later on scan113','A',
'P²_C viewed over R is integral but splits after algebraic closure, refuting the ordinary-irreducibility version. Cote29 scan113 explicitly says geometrically irreducible (parent checked its endpoint), and SGA1 X2.10–2.11 has the precise geometric hyperplane setting. This later refinement is mathematical evidence, not a decision about scan67’s ink.',
['SGA1_1971','Stacks0G4C'],computation='C⊗_R C≅C×C verified algebraically in independent_checks.md and checks.py.',confidence='high',scans=[67])
c(22,[15],'connexe ? non',
'Replacing irreducibility by connectedness in the generic-section connectedness statement is proposed and rejected.',
'corrected by himself on the same page','A',
'The rejection is correct: two projective planes meeting only at one point form a connected scheme, while a general hyperplane misses the intersection point and cuts two disjoint curves. The normal/geometrically irreducible hypotheses in SGA1’s theorem avoid this example.',
['SGA1_1971'],computation='Independent geometric example in independent_checks.md.',confidence='high',scans=[67])
c(23,[17],'π₁(X_u) → π₁(X_K) surjectif',
'Under normality and geometric irreducibility, a sufficiently general complete-intersection curve has surjective π₁ map to the ambient variety/open in the stated setup.',
'proof sketched','A',
'SGA1 X2.10–2.11 proves the proper normal hyperplane comparison, using connectedness of inverse images under finite étale covers. The generic connected-cover step is the same mechanism. Claims for arbitrary nonproper special sections require additional control and are separated as CL-SA12-024.',
['SGA1_1971','Stacks0BN6'],confidence='high')
c(24,[90],'section … spéciale',
'Replace the generic section by a suitable special section while retaining surjectivity of π₁.',
'self-flagged step','A',
'SGA1 X2.10–2.11 explicitly supplies a proper normal special-hyperplane form, via connectedness. For open/tame pairs, Esnault–Kindler Theorem1.1 has regular proper/SNC and Lef/Leff hypotheses. Its normal-variety theorem6.1 needs the complete-intersection-of-ample-divisors condition added in the 2016 erratum.',
['SGA1_1971','EK2016','EKerr2016'],confidence='high')
c(25,[18,26],'au plus 2g générateurs',
'For the fixed normal projective model and fixed smooth complete-intersection curve C of genus g avoiding the excluded codimension-two set, the induced quotient π₁(U) is generated by at most 2g elements.',
'proof sketched','A',
'SGA1 X2.9–2.11 combines a curve and the proper normal connectedness argument; SGA1 XIII2.12 gives the prime-to-p/tame curve presentation input. The genus is tied to the chosen model and polarization, not a birational invariant. The claim is a bound, not a presentation of π₁(U).',
['SGA1_1971','ESS2021'],confidence='high')
c(26,[20,21],'pureté; codim ≥2',
'Fix a regular open of one proper normal model. A rational map to each other proper normal model is defined away from codimension two; purity for the regular source and normality of the target produce compatible surjections to all model fundamental groups.',
'proof sketched','C',
'The individual tools are established: valuative extension to proper targets, purity of the branch locus on regular schemes, and connected-cover surjectivity for a dense open in a normal scheme. The single-source compatibility is reconstructed in independent_checks.md. No exact published statement under the author’s birational terminology was located.',
['Stacks0BX7','Stacks0BMB','SGA1_1971'],computation='Independent argument in independent_checks.md §4; no numerical computation.',confidence='high')
c(27,[21],'groupe fondamental birationnel',
'The inverse limit of π₁ of all proper normal models of a fixed function field over an algebraically closed field is a quotient of one finitely generated group and hence finitely generated.',
'proof sketched','C',
'With the single fixed regular open in CL-SA12-026, finite intersections of compact fibres give surjectivity onto the inverse limit. This establishes the compressed implication. Exact terminology/priority was not located in the searched birational literature. It does not imply that the inverse system stabilizes.',
['SGA1_1971','Stacks0BMB'],computation='Independent compactness proof in independent_checks.md §4.',confidence='high')
c(28,[22],'si on a un modèle régulier',
'If a proper regular model exists, the system of fundamental groups of proper normal models is essentially constant.',
'proof sketched','C',
'Purity implies birational invariance for proper regular models, and normal graph closures give a cofinal subsystem dominating the fixed regular model. This is the established mechanism; no unrestricted resolution assumption is introduced. The exact draft formulation was not found verbatim in a published source.',
['SGA1_1971','Stacks0BMB','Stacks0BX7'],confidence='high')
c(29,[22],'essentiellement constant ?',
'For arbitrary function fields, without a proper regular model assumed, is the system of π₁ of proper normal models essentially constant?',
'open on the pages','D',
'Searches in SGA1, arXiv, MathOverflow, zbMATH-targeted queries and birational-Picard literature did not locate a theorem settling this exact all-model stabilization question. This is a search result, not a claim of current openness or novelty. A uniform generator bound does not suffice, as Z/ℓ^m shows. The regular-model case is CL-SA12-028.',
['SGA1_1971','LSS2023'],computation='Cyclic-system counterexample in independent_checks.md/tests; finite generation of the limit does not force stationarity.',confidence='low')
c(30,[23],'π₁(U) … isomorphisme ?',
'For any proper normal model X, does its regular locus U already have the birational fundamental group; equivalently, can every finite étale cover of U become étale on some proper modification?',
'open on the pages; false in this generality','C',
'A complex projective quotient X=(P¹×P¹)/⟨(x,y)↦(−x,−y)⟩ has four isolated quotient singularities. Its regular locus has a connected étale double cover from the complement of the fixed points. Writing the invariant field as C(a,t), a=x², t=y/x, the extension C(x,y)/C(a,t) ramifies at the a-adic valuation. That valuation has a centre on every proper model, so the cover cannot extend étale on any of them. A regular proper rational model has trivial π₁. This independently checked example answers the exact question negatively; it is not a novelty claim.',
['Stacks0BMB','Stacks0BX7','SGA1_1971'],computation='Field invariants, valuation, quotient singularities and regular-locus hypotheses checked in independent_checks.md §4; algebraic substitutions in checks.py.',confidence='high')
c(31,[25],'ker … est-il … de génération finie ?',
'For proper normal X and codimension-two Z, is ker(π₁(X\u2216Z)→π₁(X)) topologically finitely generated?',
'open on the pages','D',
'Exact searches in MathOverflow, arXiv, SGA1 and the modern finite-presentation literature did not settle this geometric kernel question. A two-generator profinite semidirect product with infinitely generated kernel only refutes an abstract inference from surrounding finite generation; it is not a geometric counterexample. The 2023 proper finite-presentation theorem does not itself control this kernel.',
['SGA1_1971','LSS2023','ESS2021'],computation='Independent F_p[[T]]⋊Z_p example in independent_checks.md; no geometric realization asserted.',confidence='low')
c(32,[91],'comme groupe alg. …',
'The author suggests an algebraic or proalgebraic formulation of the birational fundamental group, with an unresolved adjective and no specified category.',
'open on the pages; insufficient specification','F',
'Searches for the phrase and nearby birational group constructions produced no unique identification. Proalgebraic, tannakian and profinite formulations are not interchangeable. The category must be recovered from the scan/context before a mathematical fate can be assigned.',
['SGA1_1971'],confidence='low')

c(33,[28,30,31],'Y … régulier; Pic^τ(Y) → Pic^τ(X)',
'For a proper birational map f:X→Y between integral normal proper k-schemes with Y regular, pullback on Pic^τ is asserted to be an isomorphism of group schemes; geometric normality/smoothness and projectivity are questioned in the margins.',
'proof sketched; hypotheses and final scheme argument self-flagged','C',
'Classical birational invariance of the reduced Picard/Albanese variety and smooth proper variants are established, but those statements do not alone settle this normal-source, possibly nonreduced Pic^τ assertion. Kleiman2005 gives Picard representability/properness and restriction results, while KLOS distinguishes the classical rational Albanese from the morphism Albanese of a normal model. Exact searches did not locate an opened theorem matching every written hypothesis. The page’s points-plus-tangents endpoint is insufficient on its own; the main theorem is not thereby refuted.',
['Kleiman2005','KLOS','RuellingSaito2022','Groth236'],confidence='medium')
c(34,[28],'monomorphisme; immersion fermée',
'Under universal f_*O_X=O_Y and suitable representability, pullback Pic_Y→Pic_X is a monomorphism; restricted to proper Picard group schemes it is a closed immersion.',
'proof sketched','E',
'The monomorphism follows from descent of an isomorphism of pulled-back line bundles using the projection formula and f_*O_X=O_Y, universally in the base. A proper monomorphism is a closed immersion. Kleiman’s Picard framework is a checked reference for representability/properness; those hypotheses must be supplied, not inferred from normality over a nonperfect field.',
['Kleiman2005','Groth236'],confidence='high')
c(35,[29],'Pic(X) → Pic(U)',
'Restriction from the regular target Y to an open U with codimension-two complement is an isomorphism on line-bundle classes; the display instead reads Pic(X).',
'false with displayed X in general; reading question','C',
'A regular scheme is locally factorial, so a Cartier divisor extends uniquely across codimension two; this proves the target-Y statement. For a blowup X→Y, a nontrivial exceptional divisor restricts trivially on U, so the displayed source-X version is false. Both transcriptions read X; this review does not alter it.',
['Stacks0BMB','StacksBlowup'],computation='Blowup divisor example checked in independent_checks.md and checks.py.',confidence='high')
c(36,[30],'un lemme bien connu; vérifier ?',
'A τ-trivial Cartier divisor supported on the exceptional locus of a proper birational morphism to a regular target must have all coefficients zero.',
'stated as known; verification requested','C',
'Negativity/intersection arguments establish familiar projective forms of exceptional-divisor independence. The exact arbitrary-dimensional normal-source/proper formulation and the attachment of insuffisant were not recovered from the opened sources. This is a local proof obligation of CL-SA12-033; neither the author’s phrase known nor later reduced-Picard invariance counts as its verification.',
['Kleiman2005','KLOS','NeronSamuel1952'])
c(37,[31],'un isom sur les espaces tangents',
'The proposed proof endpoint would infer equality of proper group schemes from equality on geometric points and tangent spaces of a closed inclusion.',
'false as a bare criterion; whether asserted unconditionally is uncertain','C',
'For characteristic p, the inclusion α_p⊂α_{p²} of Frobenius kernels in G_a has the same single geometric point and induces an isomorphism on one-dimensional tangent spaces, but the lengths are p and p². Thus further infinitesimal control is required. This does not disprove the Picard theorem itself.',
['SGA3_VIII','Kleiman2005'],computation='Coordinate rings k[t]/(t^p) and k[t]/(t^(p²)), tangent quotients and lengths checked in checks.py/checks.out.',confidence='high')
c(38,[28,32,33,34,35,36],'H¹(Y,O_Y) → H¹(X,O_X)',
'For the normal-source/regular-target proper birational map under suitable geometric hypotheses, the author seeks an isomorphism on H¹(O), using Artin–Schreier fixed vectors and iterated Frobenius kernels in characteristic p, then spreading out in characteristic zero.',
'proof sketched','C',
'The separate local ingredients in CL-SA12-040–042 are valid. The all-iterates exponent is essential, and the spread-out argument needs cohomological base change and preservation of geometric hypotheses. Smooth birational cohomological invariance has published modern forms, but the opened Rülling–Saito Corollary11.24 is about torsion Picard groups in a specified smooth/fibred setting and is not substituted for this normal-source H¹ theorem. No complete scheme-level proof certification is assigned.',
['Stacks0EC0','Stacks0AY6','Kleiman2005','RuellingSaito2022'])
c(39,[32],'F^{ν|1}',
'A map of finite-dimensional semilinear Frobenius modules is an isomorphism if it compares the appropriate fixed/étale parts and all iterated Frobenius kernels; comparing only ker F is insufficient.',
'proof sketched; exponent uncertain','E',
'The linear-algebra statement with all iterates follows from the nilpotent/invertible decomposition. A two-dimensional nilpotent Jordan block and its one-dimensional kernel refute a one-iterate substitute. Semilinear fixed-vector descent requires an algebraically closed/perfect ground field in the stated application. The exact ink exponent remains unresolved.',
['StacksArtinSchreier'],computation='Jordan-block kernels and iterates explicitly computed in checks.py/checks.out; proof in independent_checks.md.',confidence='high')
c(40,[33],'Le premier hom s’écrit',
'For a proper connected reduced scheme over an algebraically closed field of characteristic p, H¹_et(X,F_p) is the F=1 subspace of H¹(X,O_X).',
'used in a proof sketch','E',
'The Artin–Schreier sequence and surjectivity of a↦a^p−a on the global constant field give exactly this identification. Without control of H⁰(O), a connecting term must be retained. This finite-level statement is independently checked from the long exact sequence.',
['StacksArtinSchreier'],confidence='high')
c(41,[34],'sans torsion',
'If R is a normal domain of characteristic p, then R^(1/p^ν)/R is torsion-free as an R-module.',
'proof sketched','E',
'If r·b lies in R for nonzero r∈R and b∈R^(1/p^ν), then b lies in Frac(R) and is integral over R, hence b∈R by normality. This elementary integrality argument verifies the precise claim and yields injectivity on restriction to a dense open.',
['Stacks0AY6'],computation='Independent proof in independent_checks.md §5, no numerical calculation.',confidence='high')
c(42,[35],'Y lisse sur k (!)',
'For regular finite-type Y over a perfect field, Frobenius is finite flat; its iterated root quotient by O_Y is locally free and sections extend across a codimension-two complement.',
'proof sketched','B',
'Finiteness follows from finite type over a perfect field, flatness from Kunz, and the quotient is locally free since the unit section is locally part of a basis. Reflexive extension on a normal scheme gives the codimension-two conclusion. Stacks tags 0EC0, 0CC6 and 0AY6 were opened for these distinct inputs. Normality of Y alone would not supply flat Frobenius.',
['Stacks0EC0','Stacks0CC6','Stacks0AY6'],confidence='high')
c(43,[36],'coh. plats … en dim1; r=0',
'Spread the characteristic-zero proper birational situation to a finite-type integral arithmetic base; shrink to cohomological base-change loci and a constant-rank cokernel, then use positive-characteristic fibres to force that rank to vanish.',
'proof sketched; preservation and base change left implicit','C',
'The strategy is standard, but a proof must construct a model preserving the geometric assumptions, prove the relevant characteristic-p comparison, and justify base change and constant rank. The reviewed sources supply the tools, not a verification of every model choice on this page. It remains a bounded proof-completion task rather than a claimed new open theorem.',
['Kleiman2005','Groth236','RuellingSaito2022'])
c(44,[28,37],'modèles lisses',
'For smooth proper models of a fixed function field, the Picard objects under discussion should agree birationally, with scheme-level τ invariance inherited from CL-SA12-033.',
'deduced in the draft','C',
'Classical Picard/Albanese birational invariance and modern smooth proper torsion-Picard invariance are established. The precise nonreduced τ-scheme formulation still requires the full theorem and is not inferred from reduced varieties or from each Pic[n] group separately.',
['KLOS','Kleiman2005','RuellingSaito2022'])
c(45,[37],'le système … est essentiellement constant',
'Assuming a proper smooth model and the full scheme-level birational Pic^τ theorem, the directed system of Pic^τ along normal proper models is essentially constant.',
'conditional implication','C',
'Normal closures of graphs give a cofinal subsystem mapping to the fixed smooth model; CL-SA12-033 then supplies the asserted isomorphisms. The cofinality argument is valid. This is explicitly conditional on the scheme theorem, and is distinct from the unconditional all-model question.',
['KLOS','Kleiman2005'],confidence='high')
c(46,[38],'Question; système inductif',
'Without a smooth proper model assumed, does the directed system of Pic^τ of proper normal models stabilize?',
'open on the pages','D',
'Exact searches in Picard literature, arXiv, Numdam, zbMATH-targeted results and classical Albanese sources did not locate the all-model nonreduced τ-scheme stabilization statement. KLOS proves birational invariance and model realization for the reduced classical Picard variety Cl⁰, which is a weaker/different object. No current openness or novelty claim is inferred from the search failure.',
['KLOS','Kleiman2005','NeronSamuel1952'],confidence='low')
c(47,[38],'(i) … (ii) … (iii)',
'The proposed stabilization criterion uses uniform bounds on dimension, torsion and h¹(O) of model Picard schemes; the meaning of torsion is not specified securely.',
'open on the pages; insufficient as a general group-scheme criterion','C',
'The chain α_{p^m} has constant dimension0, one geometric point and tangent dimension1 but unbounded scheme length. Thus bounds interpreted using geometric-point torsion do not imply stabilization. If torsion means the order of an entire finite subgroup scheme, this example does not meet a uniform bound. The word’s meaning must be read on the scan, and the special birational geometry remains separate.',
['SGA3_VIII','Kleiman2005'],computation='Finite local algebra lengths and tangent dimensions in checks.py/checks.out.',confidence='high')
c(48,[43],'(i) résulte de (iii)',
'A uniform bound on h¹(X,O_X) gives a uniform bound on dim Pic_X because the tangent space of Pic_X at the identity is H¹(X,O_X).',
'stated without proof','E',
'The tangent-space identification and local dimension≤embedding dimension give the assertion. This does not bound infinitesimal length and does not prove stabilization. Kleiman’s Picard-scheme account and Conrad’s Picard handout supply the relevant infinitesimal framework.',
['Kleiman2005','ConradPic'],confidence='high')
c(49,[39,40,42],'dim Pic = 1/2 rang …',
'Dimensions of the Picard varieties of proper normal models of a fixed geometrically integral function field are uniformly bounded, by the rank of a fixed prime-to-characteristic abelianized π₁ quotient or by a fixed curve.',
'proof sketched','B',
'The corrected ℓ-adic argument requires ℓ≠p and the dual Tate-module identification. Independently, KLOS §§10.3.4–5 define a birationally invariant classical Picard variety and §10.3.13 bounds its dimension by the genus of a suitable complete-intersection curve. This controls the reduced dimension, not all nonreduced Picard structure.',
['KLOS','MoonenTateBT','Kleiman2005'],confidence='high')
c(50,[39,40],'1/2 rang',
'For the proper normal geometric setting and ℓ≠char(k), the rank of T_ℓ Pic⁰ equals twice the dimension of its reduced abelian variety; T_ℓ Pic is H¹_et(Z_ℓ(1)), dual to π₁^ab with a Tate twist.',
'used without a visible ℓ≠p qualification','C',
'The prime-to-characteristic rank statement is standard abelian-variety theory; Moonen chapterX gives the dual Tate-module and fundamental-group statements, and Kummer gives the cohomological form. For ℓ=p it fails: the supersingular elliptic curve y²=x³−x over F₃ has p-rank0 and dimension1. The dual/twist distinction affects functoriality even though it leaves the rank unchanged.',
['MoonenTateBT','Stacks03PK'],computation='Point count #E(F₃)=4 and nonsingularity checked in checks.py/checks.out; p-rank interpretation separately justified.',confidence='high')
c(51,[41],'K⊗_k k̄',
'The reduction treats K⊗_k k̄ as a field under geometric normality alone.',
'false with only the stated geometric-normality hypothesis','C',
'C is geometrically normal over R, but C⊗_R C≅C×C. Geometric integrality, an appropriate constant-field assumption, or a chosen geometric component is necessary. The exact historical usage of normal sur k remains a contextual reading question.',
['KLOS','Kleiman2005'],computation='Factorization and product decomposition checked in checks.py/checks.out.',confidence='high')
c(52,[42],'démonstration directe ???',
'Find a direct genus bound for dimensions of Picard schemes over all proper normal models, avoiding the fundamental-group argument and not taking properness of Pic^τ as an input.',
'open on the pages','B',
'KLOS §§10.3.4–5 and10.3.13 supply a precise classical-Picard route: Cl⁰ is birationally invariant and restricts with finite kernel to the Jacobian of a suitable complete-intersection curve contained in the nonsingular locus. This gives the desired numerical dimension bound once the comparison to each normal model’s reduced Picard variety is made. It does not prove nonreduced stabilization. Kleiman Remark5.8 records the related finite-kernel restriction issue and cautions that some proofs use compactness of Pic⁰.',
['KLOS','Kleiman2005','NeronSamuel1952'],confidence='high')
c(53,[44],'descent; champ',
'Tame coverings should satisfy the indicated fppf/fpqc descent and form the associated stack, under the boundary conventions of the reviewed manuscript.',
'self-flagged editorial request','C',
'Grothendieck–Murre1971 has a chapter specifically on descent of tamely ramified coverings (pp110–121), verified at table-of-contents level. Full theorem text was not accessible, so the exact topology and boundary hypotheses of this request have not been matched. Ordinary finite-étale descent is not by itself a proof of every stated tame descent assertion.',
['GM1971','SGA1_1971'],confidence='medium')
c(54,[45,131],'equations; generalized Kummer coverings',
'Supply compatible local Kummer equations and extend the ordinary Kummer algebra characterization to the generalized class needed in the formal argument.',
'self-flagged step; Murre letter30-4-1969','C',
'The local tame Kummer mechanism and Abhyankar lemma are established; the published Grothendieck–Murre book opens with Kummer coverings (pp1–29). The exact generalized algebra characterization corresponding to draft2.1.8 was not checked in full text. Murre explicitly says the existing characterization is only for ordinary coverings, so the missing generalization is retained.',
['GM1971','Stacks0BSE','SGA1_1971'])
c(55,[46],'Lefschetz',
'Develop the requested Lefschetz variant for tame coverings of a divisor-complement pair.',
'self-flagged editorial request','B',
'Esnault–Kindler2016 Theorem1.1: for regular connected proper X over k, an SNC divisor D, and a suitable section Y transverse to D, Lef(X,Y) gives surjectivity of tame π₁; Leff plus meeting every effective divisor gives an isomorphism. Their broader normal-variety Theorem6.1 needs Y to be a complete intersection of ample divisors in good position, as the September2016 erratum states. These precise theorems answer standard forms of the request, not an unspecified strongest version.',
['EK2016','EKerr2016','SGA1_1971'],confidence='high',date='arXiv circulation2015; publication2016; erratum dated29 September2016.')
c(56,[47],'tame [deleted]; prime to p [inserted]',
'The requested local finite-generation statement is narrowed to the prime-to-p quotient in an abbreviated formal/local setting.',
'corrected by himself on the page','F',
'The local geometric hypotheses are not specified sufficiently to identify a single theorem. Grothendieck–Murre’s final chapter concerns the punctured spectrum of a two-dimensional complete local ring; Déglise/Gabber Theorem1.4 gives finite H¹ for each finite G in a strict local normal excellent dimension-two setting, which is weaker than finite generation. Neither is silently substituted for the unexpanded request.',
['GM1971','DegliseGabber2007'],confidence='low')
c(57,[48],'specialization paths',
'A specialization path is encoded by a choice of lift of a geometric generization to a strict localization, giving the corresponding map of fibre functors/stalks; a product-of-fields description needs assumptions on that fibre.',
'editorial explanation with a requested check','A',
'The étale fibre-functor construction and strict-localization description are established in SGA1 and the Stacks specialization discussion. Geometric specialization runs from the chosen generization lift toward the special point; the induced sheaf-stalk map runs from the special stalk to the generization stalk. Reversing either convention silently is not harmless. The unqualified product-of-fields assertion is not certified.',
['SGA1_1971','StacksSpecialization'],confidence='high')
c(58,[49],'equivalence of categories anyhow!! to check',
'An equivalence between the unnamed chapter-VII categories is conjectured.',
'self-flagged step','F',
'The categories are not defined in these leaves. Searching the published Grothendieck–Murre structure, EGA formal-étale comparisons and draft labels did not uniquely identify this equivalence. A published table of contents cannot settle it.',
['GM1971','SGA1_1971'],confidence='low')
c(59,[50],'finite type; finite presentation; locally free',
'Quasi-coherent modules are to glue across the intended square, with finite type, finite presentation and local freeness detected on the pieces.',
'stated without proof; ambient square omitted','F',
'These are valid in several effective-descent and formal-patching settings, but false for arbitrary unspecified diagrams. Searches in EGA and the Grothendieck–Murre published structure did not recover the exact square. The absent hypotheses prevent a theorem-level fate assignment.',
['GM1971'],confidence='low')
c(60,[50],'tame iff …; must be trivial',
'A finite flat cover is asserted tame exactly when its restrictions to the pieces of the omitted gluing setup are tame.',
'stated as immediate; hypotheses omitted','F',
'Locality of tameness depends on valuations, normalizations and the cover topology; the unnamed gluing situation cannot be identified from this sentence. The published descent chapter is a relevant lead, not verification of this iff.',
['GM1971','Stacks0BSE'],confidence='low')
c(61,[51],'Il faudrait vérifier',
'A cancelled draft proposes inverse image for quasi-coherent stratified modules with a compatibility/lifting condition involving an unresolved m.u. abbreviation.',
'withdrawn draft; self-flagged step','F',
'No unique category or assertion is determined by the available words. Searches for stratified inverse-image and formal unramified lifting do not justify replacing the abbreviation by a guessed modern concept. Cancellation is recorded independently of mathematical truth.',
['SGA1_1971'],confidence='low')
c(62,[51],'non ramifié',
'If the lifting phrase is read as unique deformation of an unramified object across a nilpotent thickening, that reading is too strong; formal unramifiedness gives uniqueness for maps to a fixed target.',
'ambiguous in a cancelled draft','F',
'Spec(k) and Spec(k[ε]/ε²), each as an unramified scheme over Spec(k[ε]/ε²), restrict to the same closed-fibre object but are different lifts. Thus object-uniqueness cannot follow from unramifiedness alone. This tests a possible reading and does not refute the formally unramified morphism property.',
['StacksUnramified'],computation='Dual-number object comparison in independent_checks.md.',confidence='high')
c(63,[54],'groupe de Raynaud; 0→T→A^♮→B→0',
'For a noetherian adic base S=Spec(V) complete and separated, a smooth finite-type group A with semiabelian identity component on the special fibre, isotrivial T₀ and algebraizable formal abelian quotient yields a Raynaud group whose identity component is an extension of B by T.',
'reused typescript with internal revisions','A',
'The original SGA7 I ExposéIX7.2.2–7.2.5, printed pp406–407, gives the exact construction and corrects the draft splice: the full Raynaud group may have a finite étale component group, and the displayed torus-by-abelian extension is 0→T→(A^♮)⁰→B→0. The isotriviality insertion is retained. This is an exact visually checked counterpart, not an inferred thematic resemblance.',
['SGA7_IX'],confidence='high',date='Seminar1967–1969; SGA7 I publication1972. Exact date of reused typescript not established.')
c(64,[54],'(A^♮)^∧≃Â',
'The Raynaud group has a canonical formal-completion isomorphism with the original group along the special fibre, characterized by the coherent finite-level isomorphisms.',
'stated in revised typescript','A',
'SGA7 I IX7.2.3, p407, states the exact completion isomorphism; IX7.2.1 supplies full faithfulness of completion in the specified category. The printed proof leaves the direct full-faithfulness verification to the reader in7.2.1.4; this review verifies the statement match, not a full independent proof.',
['SGA7_IX'],confidence='high')
c(65,[54,133],'dépend fonctoriellement; tout changement de base',
'The Raynaud group and its torus-by-abelian identity-component extension depend functorially on A and commute with base change induced by a homomorphism of noetherian adic rings.',
'stated without separate proof','A',
'SGA7 I IX7.2.6, p407, states this functoriality and adic base-change compatibility exactly. The hypotheses of7.2.1–7.2.2 are retained; this is not an assertion about arbitrary formal groups or arbitrary maps without adic compatibility.',
['SGA7_IX'],confidence='high')
c(66,[133],'catégorie des torseurs … systèmes cohérents',
'For a finite locally free group H over the complete noetherian adic base in the Raynaud construction, H-torsors are equivalent to coherent systems of H_n-torsors, and this algebraizes the relevant finite-component extensions.',
'proof sketched in reused continuation','A',
'SGA7 I IX7.2.1.3, printed p405, is the exact published torsor argument, followed on p406 by representability/descent for the resulting extension. The finiteness of H is essential; this statement is not generalized to arbitrary nonproper formal objects.',
['SGA7_IX'],confidence='high')
c(67,[133],'7.6.3; S normal',
'The construction extends from complete traits/local bases to noetherian adic V; its key issue is algebraizing the formal abelian quotient, which the draft asserts under normality of S.',
'stated without full proof in the fragment','A',
'SGA7 I IX7.1.5, p402, proves algebraizability and projectivity of the abelian quotient when S is normal. Remark7.1.6 on the same page says algebraizability also holds without normality, referring to13.5.3(a). This review read the proposition and remark but has not independently checked the cited reduction. IX7.2.1–7.2.6 supplies the general adic construction.',
['SGA7_IX'],confidence='high')

c(68,[52,53],'f.μ; Δ; distributions',
'Finite-order point-supported distributions carry the module structure dual to multiplication on the finite jet algebra; the induced coproduct and associativity identities are compatible with that action.',
'proved on reused typescript, with some continuations missing','E',
'These are standard finite-jet duality identities, independently reconstructed from (A/m^(r+1))*. Searches for N°385 and the six printed-page fragments did not identify their source or establish a priority date. In particular Bourbaki talk385 is Raynaud’s different work and is not assigned as provenance. Class E describes the standard calculus, not an established date or authorship for the sheets.',
[],computation='General dual-algebra proof and low-order multivariable symbolic checks in independent_checks.md §6 and checks.py/checks.out.',confidence='high')
c(69,[53],'projection formula',
'Pushforward of a finite-order distribution under a smooth map satisfies the projection formula with pullback of functions, within the indicated differentiability/order range.',
'proved on reused typescript','E',
'The formula follows directly from applying the functional to the product of a pulled-back function and a test function. The finite-jet proof is checked. Searches of the distribution literature and the unidentified sheet number did not recover an exact original source; the differentiability glyph remains undecided.',
[],computation='Explicit truncated-polynomial pushforward/product identities in checks.py/checks.out.',confidence='high')
c(70,[53],'(f.μ)×(g.ν)=(f×g).(μ×ν)',
'External products of point-supported distributions obey the tensor/module identity and the total-order filtration: orders i and j produce order at most i+j.',
'proved on reused typescript','E',
'The total-order finite-jet construction proves the formula. The full rectangular tensor product of two order≤r spaces is not the same as total order≤r on the product; the modern reconstruction explicitly preserves this distinction. Source-identification searches remain negative.',
[],computation='Multiindex derivative/binomial checks and filtration dimensions in checks.py/checks.out.',confidence='high')
c(71,[53],'vecteur tangent; dérivation',
'First-order distributions annihilating constants identify with tangent vectors, equivalently derivations at the point or the dual of m/m².',
'proved on reused typescript','E',
'The Leibniz rule exactly expresses vanishing on m², giving the standard tangent-space identification. The proof was independently repeated; the manuscript source remains unidentified despite searches.',
[],computation='First-jet product and derivation tests in checks.py/checks.out.',confidence='high')
c(72,[53],'matrice jacobienne',
'The tangent map in local coordinates is represented by the Jacobian and obeys the chain rule.',
'proved on reused typescript','E',
'This is the standard first-jet chain rule. The arbitrary symbolic-coordinate calculation was redone; no novel claim or historical priority is attributed to the unidentified reused pages.',
[],computation='Symbolic Jacobian composition verified in checks.py/checks.out.',confidence='high')
c(73,[53],'sous-variété; idéal',
'Distributions carried by an embedded submanifold are characterized by annihilation of its defining ideal, with the appropriate finite-order quotient.',
'proof sketched; surrounding continuation incomplete','E',
'Duality of the quotient jet algebra identifies exactly the annihilator. This is independently checked in the finite-jet setting; global analytic formulations would require their own topology and regularity assumptions. The source attribution is unresolved.',
[],computation='Quotient/annihilator jet calculations in checks.py/checks.out.',confidence='high')
c(74,[55],'D_S(M)',
'For an abelian group M, D_S(M)=Spec(O_S[M]) represents the character functor Hom(M,O_T^×); for a general group the functor factors through abelianization.',
'proved on typescript','A',
'SGA3 VIII §1, especially1.1–1.4, is the exact published counterpart. The group-algebra Hopf structure and the character universal property are directly checked. The typed operator gaps in the archival witness remain unfilled.',
['SGA3_VIII'],computation='Group-algebra/counit/comultiplication checks in independent_checks.md §6 and checks.py/checks.out.',confidence='high',date='SGA3 seminar1962–1964; first book publication1970; opened reedition2009/2011.')
c(75,[55],'changement de base',
'Formation of D_S(M) commutes with arbitrary base change.',
'proved on typescript','A',
'SGA3 VIII §1 proves this through the base-change identity for the group algebra. No flatness assumption on the base change is needed.',
['SGA3_VIII'],computation='Universal group-algebra argument in independent_checks.md §6.',confidence='high')
c(76,[55],'Hom; type fini',
'The internal Hom between the indicated diagonalizable groups is representable under the stated finite-generation hypothesis on the relevant character group.',
'proved on typescript; typed gaps','A',
'The exact counterpart is SGA3 VIII1.5 and the reeditor’s expanded Proposition1.7. The opened reedition explicitly notes the original assertion/proof issue and supplies a finite-generation-sensitive treatment. A blanket representability claim for arbitrary character groups is not made.',
['SGA3_VIII'],confidence='high')
c(77,[55],'Un groupe diagonalisable est réflexif',
'Character duality recovers M from D(M), and diagonalizable groups are reflexive under the relevant double-dual functor.',
'proved on typescript','A',
'SGA3 VIII §§1–2 gives the exact duality and biduality statements. The proof identifies group-like elements of the group algebra componentwise; its functorial setting matters over disconnected bases.',
['SGA3_VIII'],confidence='high')
c(78,[56],'n éléments; premier à p',
'For finite abelian T, D(T) is finite locally free of rank|T|. Over an algebraically closed field of characteristic p, its geometric points count only the prime-to-p part; equality with|T| requires p∤|T|.',
'proved on typescript','A',
'SGA3 VIII2.1 states the finite/smooth criteria. The example μ_p has length p and one geometric point, so group-scheme order cannot be replaced by point count. This distinction is relevant to the finite tame coefficient quotients on scan88.',
['SGA3_VIII'],computation='μ_p coordinate ring and point/length comparisons in checks.py/checks.out.',confidence='high')
c(79,[55,56],'type fini; plat; lisse',
'D_S(M) is flat, is of finite type when M is finitely generated, and has the smoothness/étaleness properties dictated by torsion orders being invertible on S.',
'proved on typescript','A',
'SGA3 VIII2.1 is the exact published statement; the opened text distinguishes finite type, finite, and smooth/étale criteria. The review does not fill the missing archival symbols by copying the printed text.',
['SGA3_VIII'],confidence='high')
c(80,[57],'Théorème3.1',
'An exact sequence of abelian character groups dualizes to an exact sequence of diagonalizable group schemes for the fpqc topology; the right-hand morphism is faithfully flat and quasi-compact.',
'proved on typescript','A',
'SGA3 VIII3.1 gives the exact theorem. A basis of the larger group algebra indexed by coset representatives proves faithful flatness over the smaller group algebra; kernel identification follows on characters. This algebraic proof was independently repeated.',
['SGA3_VIII'],computation='Coset-basis algebra check in independent_checks.md §6 and checks.py/checks.out.',confidence='high')
c(81,[58,59,63],'1→I₀→π₁^t(𝔛,D)→π₁^t(U)→1',
'Let 𝔛 be regular connected noetherian formal, X₀ a regular Cartier special divisor, and X₀ plus the remaining divisors a normal-crossings boundary. Set U=X₀ minus the induced remaining boundary. The tame formal group maps onto π₁^t(U), with inertia I₀ a quotient of the prime-to-residue-characteristic roots-of-unity module μ.',
'stated with proof sketch','C',
'Grothendieck–Murre1971 has the exact object in chapters5 and7 (pp69–81 and97–109), verified from the publisher contents. The full theorem text was inaccessible; hence the precise generality and exceptional hypotheses of the draft have not been certified by that bibliographic match. Local Kummer theory supports the inertia mechanism; realization is separately recorded.',
['GM1971','Stacks0BSE','SGA1_1971'])
c(82,[58],'opère … via … μ',
'The quotient action of π₁^t(U) on inertia is induced by the cyclotomic action on μ; the extension need not be central.',
'stated in the setup','A',
'The roots-of-unity/cyclotomic action is standard tame inertia and is explicitly present in SGA7 I ExposéI §1. The formal setup has the same coefficient action. A tame S₃ extension over F₂((t)) gives a concrete noncentral instance; centrality holds only after trivializing the relevant action.',
['SGA7_IX','SGA1_1971','GM1971'],computation='S₃ conjugation and Frobenius action checked in checks.py/checks.out.',confidence='high')
c(83,[60],'H¹(Ũ^t,J)=0',
'For a finite constant prime-to-characteristic coefficient group J, H¹ on the universal tame pro-cover vanishes because each J-torsor is killed by a finite stage.',
'proof sketched','E',
'This is the defining torsor-killing argument for a universal covering pro-object. It does not automatically extend to inverse limits of coefficient groups: continuous cohomology and possible lim¹ terms must be controlled. The finite-coefficient proof is independently repeated.',
['SGA1_1971','Milne2008'],confidence='high')
c(84,[61],'courbes',
'An unqualified marginal suggestion that all higher cohomology vanishes on the tame universal cover of every smooth curve is too broad.',
'overbroad early margin; explicitly refined on later scan96','C',
'For P¹ over an algebraically closed field and n invertible, π₁(P¹)=1 but H²(P¹,μ_n)≅Z/n, so its universal cover does not have the asserted vanishing. Later cote29 scan96, CodexK29-07 lines51–64, was read directly and explicitly excludes P¹ with empty boundary from the π₂-vanishing example. That later refinement does not decide the ink of the earlier margin. It also does not justify the separate later assertion that the inertia extension is trivial; the degree-one elliptic-line-bundle counterexample in formal_elliptic_nonsplitting.md addresses that assertion, recorded by root as CL-SA12-203.',
['Milne2008','SGA1_1971','Stacks03PK'],computation='Cohomological argument in independent_checks.md; no numerical experiment.',confidence='high')
c(85,[60,63],'Hom(π₁|π₂,J); spectral sequence',
'Under finite coefficients and a compatible tame étale homotopy framework, the degree-two term on the universal cover is related to Hom(π₂^t(U),J), and a low-degree spectral sequence compares it with group cohomology of π₁.',
'proof sketched; π₁/π₂ reading disagreement','C',
'The π₂ reading is mathematically consistent with the intended H²/transgression mechanism; π₁ would conflict with the preceding H¹ vanishing. The precise tame homotopy model and profinite coefficient conventions are not defined here. Grothendieck–Murre’s comparison chapter is a relevant exact-object lead, but its theorem text was not accessible. No derived/project-context theorem is imported to fill the gap.',
['GM1971','Milne2008'],confidence='medium')
c(86,[63,132],'ρ(α)=σ(β); 9.2.3',
'The inertia group-extension class α maps to the Kummer Chern class β of the normal line bundle, with pushforward/restriction maps and a fixed normal-versus-conormal sign convention.',
'self-flagged comparison; Murre says proof omitted in the preliminary draft','C',
'Grothendieck–Murre1971 chapter6, pp82–96, is explicitly titled Comparison of two 2-cohomology classes. A finite-level Čech calculation with chosen roots independently proves the indicated cocycle comparison once conventions and the extension model are fixed. It is not a proof of every pro-limit step. Murre’s cited Giraud letter is absent and not checked.',
['GM1971','Stacks03PK','Milne2008'],computation='Čech root cocycle/sign calculation in independent_checks.md §7 and checks.py/checks.out.',confidence='high')
c(87,[62,70],'I₀=μ₀/Imπ₂^t(U)',
'The kernel of μ→I₀ is proposed to equal the image of the normal-bundle map from π₂^t(U); one containment follows from the Chern comparison, the other requires realizing finite quotients as inertia.',
'proof sketched; reverse containment self-flagged','C',
'The published Grothendieck–Murre continuation treats the same inertia object, but its exact theorem hypotheses were not available. The draft’s reverse inclusion is not certified by the Chern identity alone. A degree-d line bundle over P¹ predicts the prime-to-p cyclic quotient of order the prime-to-p part of|d| for d≠0, and infinite procyclic inertia for d=0; this example remains conditional on the stated homotopy realization.',
['GM1971','Milne2008'],computation='Prime-to-p quotient computation, including d=0, in checks.py/checks.out; realization not claimed from this computation.')
c(88,[65],'déjà … à un … fini',
'For a fixed finite coefficient quotient, a class vanishing in the filtered limit over finite tame covers vanishes at one finite stage.',
'proof sketched','E',
'This is the finite-level meaning of filtered-colimit vanishing. The stage may depend on the coefficient quotient. One finite cover generally cannot kill all levels simultaneously: pullback of a degree-one line bundle on an elliptic curve multiplies its degree by the finite cover degree, which cannot be divisible by every n. This distinction is independently checked.',
['Milne2008','Stacks03PK'],computation='Divisibility tests plus general degree argument in checks.py/checks.out and independent_checks.md.',confidence='high')
c(89,[70,71],'J₀ apparaît comme groupe d’inertie',
'Every appropriate finite quotient J of μ/Imπ₂ should be realizable as inertia of a tame formal covering after a suitable finite tame base cover.',
'self-flagged construction','C',
'The draft needs finite-stage vanishing, a root-line-bundle construction, effectiveness, and descent. The root-pair correction CL-SA12-093 repairs the finite-level Kummer step; it does not supply the entire realization theorem. Grothendieck–Murre chapters5–7 are the precise published-object comparison, but exact hypotheses remain unverified without full text.',
['GM1971','Stacks04DY','Stacks03PK','Lipman1974'])
c(90,[66],'β₀=nγ₀+Σλ_iβ^i',
'For regular X₀ and U obtained by deleting boundary Cartier divisors D_i, n-divisibility of a line bundle on U means that its class on X₀ is divisible by n modulo the subgroup generated by [D_i].',
'corrected by himself on scan94','E',
'The divisor-localization sequence for Picard groups gives the corrected boundary term. Extending a divisor from U proves the assertion on regular X₀; pairwise disjointness of the D_i is unnecessary for this isolated localization step. The earlier stronger conclusion without the boundary sum was cancelled.',
['StacksDivisorLocalization','Stacks03PK'],computation='Independent divisor-class proof in independent_checks.md §7.',confidence='high')
c(91,[67],'uniquement divisibles par n',
'For n invertible, the kernel of Pic(𝔛)→Pic(X₀), or of Pic across a nilpotent thickening, is asserted uniquely n-divisible without properness/global-unit hypotheses.',
'false as stated','C',
'The explicit first-order deformation of E×G_m over C has ker Pic=H¹(O)/(Z·a), with nonzero n-torsion a/n mod Z·a. The formal deformation z_j=z_i exp(t a_ij) gives the same defect in a regular connected noetherian formal scheme with regular Cartier special fibre and no other boundary. Every hypothesis and the exact global-unit boundary image are checked. The opened Stacks tag0C6S currently contains the same unrestricted Pic[n] assertion; its proof omits the global-unit connecting contribution and is flagged as unreliable for this use. No novelty claim is made and no external edit was attempted. CL-SA12-093 is the corrected root-pair statement.',
['Stacks0C6R','Stacks0C6S','Stacks04DY','Stacks03PK'],computation='Full independent counterexample in independent_checks.md §8; truncated exponential/cocycle calculations and torsion check in checks.py/checks.out.',confidence='high')
c(92,[69],'Pic(𝔛)=lim Pic(𝔛_n)',
'The formal Picard group is identified with the inverse limit of Picard groups of infinitesimal thickenings.',
'used without sufficient justification in the general setting','C',
'Lipman1974 §2.4 explains surjectivity and the role of the Mittag–Leffler condition on global units for injectivity, within the proper setting of §2.2. Compatibility of chosen isomorphisms is essential; a possible lim¹ of units cannot be dropped in the unrestricted nonproper setup. The draft requires an explicit effectiveness/limit argument.',
['Lipman1974'],confidence='high')
c(93,[68,71],'β₀=nγ₀; dégager un lemme',
'Refinement supplied by this review: for n invertible and a nilpotent thickening X₀⊂X, the groupoid of specified nth-root pairs (M,φ:M^n≅L) for a fixed L on X is invariant under restriction, with compatible isomorphisms.',
'modern reconstruction of a self-flagged step; not a verbatim authorial theorem','E',
'Topological invariance of the étale site and the étale μ_n-gerbe/root-pair description prove the finite-level statement; equivalently principal units have unique nth roots. This remains valid although the unframed Picard kernel can have n-torsion. Passing to an infinite formal system and algebraization is a separate question.',
['Stacks04DY','Stacks03PK','Stacks0C6R'],computation='Finite-order binomial/exponential identities in checks.py/checks.out; independent root-pair argument in independent_checks.md §8.',confidence='high')
c(94,[71,131],'à vérifier si ceci est indispensable',
'Is pairwise disjointness of the induced boundary divisors necessary for the complete formal inertia-realization proof?',
'open on the pages; explicit doubt','C',
'It is unnecessary for the Picard localization step CL-SA12-090. Murre’s letter traces the assumption to the ordinary-Kummer restriction in draft7.1.5 used in9.3.3. The full generalized-Kummer replacement and realization theorem were not verified from the unavailable published chapter text; that is the exact remaining comparison, not an asserted obstruction.',
['GM1971','Stacks0BSE','StacksDivisorLocalization'])
c(95,[131],'EGAI10.12.3',
'Murre uses the comparison between formal étale morphisms and coherent inductive systems of ordinary étale morphisms of the thickenings.',
'stated as a foundational input in the letter','C',
'The cited EGA I10.12.3 is a precise source lead and the nilpotent étale equivalence is established in Stacks04DY. The exact EGA page and formal convention must be compared directly; this review records the foundational finite-level result and does not turn every formal object into an algebraic one.',
['EGAI1960','Stacks04DY'],confidence='medium')
c(96,[131],'1.1.13;7.1.5→9.3.3',
'Formal étale neighbourhoods in the stated local setup are claimed locally to arise as completions of ordinary étale neighbourhoods; Murre identifies this as an input to the later lifting argument.',
'stated in letter; proof/reference task','C',
'Local étale lifting across nilpotent thickenings is established, and EGA’s formal-étale theory is the intended source. General algebraization of arbitrary formal morphisms is stronger and not inferred. Exact searches did not recover the draft1.1.13 hypotheses from the fragment or full published text.',
['EGAI1960','Stacks04DY','StacksFormalEtale','GM1971'])
c(97,[131],'2.1.8; generalized Kummer',
'Murre asks for a characterization of the algebra of a generalized Kummer covering analogous to the existing ordinary-Kummer characterization.',
'open step in letter30-4-1969','C',
'Published Grothendieck–Murre chapter1 addresses Kummer coverings, and modern Abhyankar/Kummer local theory is established. The exact generalized characterization needed to remove disjointness in draft7.1.5 was not checked in accessible theorem text; the distinction remains explicit.',
['GM1971','Stacks0BSE'],confidence='medium')
c(98,[132],'3.6.5',
'Murre reports a delicate argument that the indicated geometric data determine the covering, requiring revision/verification.',
'self-flagged in letter','F',
'The referenced draft proposition is not reproduced, and its data/category cannot be uniquely reconstructed from the letter. Searches of the book structure and theorem numbers did not identify an exact theorem. This is retained as a historical proof task rather than replaced by a generic uniqueness theorem.',
['GM1971'],confidence='low')
c(99,[132],'3.5.5; only an indication',
'The proof of preliminary proposition3.5.5 is only indicated.',
'self-flagged omitted proof','F',
'The proposition itself is absent from the supplied letter pages. The published book’s chapter numbering does not allow a unique match from this label alone. Search completed without identifying a statement to certify.',
['GM1971'],confidence='low')
c(100,[132],'8.1.6;8.1.9(iii)',
'A canonical-isomorphism assertion in preliminary8.1.6 is crucial for8.1.9(iii).',
'self-flagged dependency in letter','F',
'Neither complete assertion is present in these pages; the number also has a competing reading in the editorial notes. The published comparison-of-classes/inertia chapters are relevant, but no theorem-level identity is asserted without the absent draft or full chapter text.',
['GM1971'],confidence='low')
c(101,[130,132],'plumbing; geometric interpretation',
'Murre’s preliminary plumbing construction is intended to have a geometric interpretation; a chapter parallel to Mumford remains unwritten and later geometry is described as difficult.',
'open programme in letter30-4-1969','F',
'The supplied pages establish a circulation stage and an unfinished programme, not a uniquely specified algebraic theorem. Searches in the Grothendieck–Murre bibliography and book structure do not identify a completed theorem for this exact unwritten chapter. No modern logarithmic or anabelian project is substituted for it.',
['GM1971'],confidence='low')
c(102,[103],'Abhyankar lemma',
'The editorial notes request an explicit statement and placement of Abhyankar’s lemma and its local Kummer consequences.',
'self-flagged exposition step','A',
'SGA1 XIII and Stacks58.31 give precise tame-ramification/Kummer statements. The mathematical lemma is established, but the correct insertion into the preliminary formal-covering manuscript is an editorial task, not a new theorem or a proof of every generalized formal version.',
['SGA1_1971','Stacks0BSE'],confidence='high')

# Additional opened-source matches from the last targeted batches.
for x in C:
    n=int(x['id'].split('-')[-1])
    if n in (1,2):
        x['refs'].append('KatzLang1981')
        x['fate']+=' Katz–Lang1981, Preliminaries Lemma2 (PDFpp8–9), explicitly proves the generic-fibre exact sequence for smooth surjective finite-type X→S, with S normal connected locally noetherian and connected geometric generic fibre. This settles the smooth variant, not an unidentified broader reduced-fibre adjective.'
    if n==10:
        x['refs'].append('KatzLang1981')
        x['fate']+=' Katz–Lang1981 §2 uses Artin good neighbourhoods/elementary fibrations and cites SGA4 XI3.1; this supplies a precise backward reference for the smooth geometric reduction.'
    if n==50:
        x['refs'].append('Sutherland2012')
        x['fate']+=' Sutherland2012, Introduction, gives the opened criterion #E(F_q)≡1 mod p for supersingularity, which verifies the p-rank interpretation of the saved point count.'
    if n==21:
        x['class']='B'
        x['refs'].append('PoonenSlavov2020')
        x['fate']+=' Poonen–Slavov, Theorem1.8 and Lemma7.1 with§7 proof, independently establish the general morphism version after geometric irreducibility is imposed: when the image has dimension at least2, the bad hyperplane locus has dimension at most r−1. Iterating generic hyperplanes gives the codimension-s form. This exact modern development needs neither properness nor normality; Theorem1.5 alone would require equidimensional fibres. ArXiv first circulation23 January2020; author PDF dated4 August2020. Jouanolou1983 is their backward reference, not a book opened here.'
    if 68<=n<=73:
        x['refs'].append('Schwartz1947')
        x['fate']+=' Schwartz1947–1948 §1, pp7–9, was opened as a primary historical source for distributions and multiplication by smooth functions; it does not identify these six sheets.'
    x['present_status']='2026-11-19: '+x['fate']

def save():
    (P/'claims.json').write_text(json.dumps(C,ensure_ascii=False,indent=2)+'\n')
save()
print(f'Saved {len(C)} manually formulated claims.')
