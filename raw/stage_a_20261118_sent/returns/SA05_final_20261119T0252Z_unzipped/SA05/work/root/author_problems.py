#!/usr/bin/env python3
"""Manually formulated problem records, anchored in the previously read passages."""
import json
from pathlib import Path
P=Path(__file__).resolve().parent
items={int(x['id'].split('-')[1]):x for x in json.loads((P/'items.json').read_text())}
problems=[]
def p(n,title,ii,cc,as_he,now,state,why,worth,refs):
 occurrences=[]
 for i in ii:
  x=items[i]
  occurrences.append({'item':x['id'],'cote':x['cote'],'scans':x['scans'],'lines':x['lines'],'sources':x['sources']})
 problems.append({'id':f'MP-SA05-{n:02d}','title':title,'occurrences':occurrences,
  'as_he_states':as_he,'plausible_today':now,'state_of_art':'As of 2026-11-19: '+state,
  'why_open':why,'worth':worth,'refs':['R-'+x for x in refs],
  'claims':[f'SA05-C{x}' for x in cc], 'formulation_origin':'The first formulation follows the attached manuscript; the modern formulation and worth assessment are this run’s.'})

p(1,'The pure effective category and its realizations',[1,2],[1,2],
 'Construct the semisimple rational category of effective pure motives with the stated faithful realizations and weight-one abelian-variety part.',
 'For a fixed cycle equivalence, separate the construction of its pseudo-abelian correspondence category, numerical semisimplicity, and the conjectural faithfulness of a chosen realization.',
 'Jannsen, Theorem 1, proves numerical semisimplicity. Tate and Faltings prove the stated Hom comparisons for abelian varieties over finite fields and number fields. The October 2026 CM paper, Corollaries 8.3–8.4, states all-codimension rational Tate and the standard positivity consequences for abelian varieties; its full proof was not independently audited here. These do not construct the manuscript’s full category for arbitrary varieties.',
 'The sources identify missing cycle-equivalence and realization comparisons; they do not give a historical explanation for every deferred step in these leaves.',
 'Yes: a precise comparison chart by equivalence relation and coefficients would prevent the main conjectural dependencies from being concealed.',
 ['Jannsen1992','Tate1966','Faltings1983','CMHodge2026','MilneReport2026'])
p(2,'Level, coniveau and algebraically closed base extension',[3,5,7,8],[3,4,6,8,9],
 'Relate minimal Tate-adjusted effective level to supported cohomology and its behavior under algebraically closed base extension; the invariance sentence at scan 3 is cancelled.',
 'In a specified semisimple pure category, the decomposition by minimal level is formal. Equality with geometric coniveau, and invariance under the chosen base extension, must be stated as additional cycle/support results.',
 'Bloch–Ogus supplies the coniveau construction; DM 6.22 corrects an overstrong essential-surjectivity assertion. The 2026 CM result includes a generalized Hodge corollary for CM abelian varieties, not a theorem for every object in the draft.',
 'The manuscript itself removes one overstrong statement. No source establishes a single general level theorem with all the draft’s quantifiers.',
 'Yes: one run can distinguish the three filtrations and identify the exact standard-conjecture inputs, without proving the general conjecture.',
 ['BlochOgus1974','DM1982','CMHodge2026'])
p(3,'The proposed universal presentation by Künneth functors',[4],[5],
 'Recover tensor functors out of motives from contravariant smooth-projective functors satisfying Künneth and the written P1 condition.',
 'Specify correspondences, cycle classes, composition and the equivalence relation before asserting a universal property.',
 'Jannsen’s correspondence setting and Choudhury–Gallauer Theorem 9.1 give precise but different constructions. The latter compares Nori and Ayoub Hopf algebras for its stated characteristic-zero embedding and PID coefficients; it is not this two-axiom presentation.',
 'The fragment omits structural data needed to identify the exact intended universal theorem; no historical motive for the omission is documented.',
 'Yes: a definition audit is feasible in a few hours and would identify the missing data exactly.',
 ['Jannsen1992','CG2017'])
p(4,'Pure motives over regular bases and generic restriction',[10],[14],
 'Define motives over a regular base through generic correspondences, fully faithfully inside the generic-fibre category, and make pullback explicit.',
 'Work in a specified category over regular integral schemes; distinguish generic restriction, extension of objects and compatibility of realizations.',
 'Cisinski–Déglise supplies triangulated operations and continuity in stated settings; Kahn, Theorem 5.10 and the Nori application in §10, supplies exact descent under his assumptions. Neither automatically constructs the requested abelian generic category.',
 'The page labels the functoriality step as needing explanation. Later frameworks solve neighboring formal problems with different category choices.',
 'Yes: a comparison on regular curves could delimit the surviving extension problem concretely.',
 ['CD2019','Kahn2025'])
p(5,'Finite coefficient extensions and neutral fibre functors',[11,13],[15,16,18],
 'Prove that the tensor-generated category becomes neutral after a finite extension of coefficients, while retaining the supersingular obstruction over Q.',
 'Require a genuine characteristic-zero Tannakian category, not merely a rigid symmetric category; distinguish neutrality of the gerbe from a preferred rational fibre functor.',
 'DM 3.2 supplies the fibre-isomorphism torsor and Deligne 7.1 the nonnegative integral categorical-dimension criterion. The quaternion action rules out the specified rational two-dimensional supersingular realization, and a superline rules out an unrestricted rigidity criterion.',
 'The obstruction changes the coefficient/fibre requirement; it does not refute Tannakian descent with its proper hypotheses.',
 'Yes: a finite list of obstruction examples and a gerbe argument would close the local exposition gap.',
 ['DM1982','Deligne1990','Milne1994'])
p(6,'Comparison of Betti fibres at different embeddings',[12,14],[17,19],
 'Compare the groups coming from distinct complex embeddings and clarify association of a fibre with a geometric base point.',
 'For two fibre functors on the same specified Tannakian category, use their tensor-isomorphism torsor and retain the extra Artin-subcategory identification.',
 'DM 3.2 and the arithmetic discussion in 6.23 identify the torsor and quotient mechanisms. They do not choose a rational trivialization or a generic period point.',
 'The formal comparison is established; the draft’s point choices do not canonically disappear.',
 'Yes: useful for the companion commentary, with a bounded formal result rather than a new period conjecture.',
 ['DM1982','Kahn2025','Huber2020'])
p(7,'Geometric kernel, components and the Artin quotient',[15,16,17],[20,21,22,23,24],
 'Identify the component quotient with the arithmetic fundamental group and express Tate fullness as density; the first unconditional component isomorphism is cancelled.',
 'First prove the exact arithmetic/geometric sequence for a specified category, then state separately the connectedness and density hypotheses.',
 'DM 2.21 and 6.22–6.23 and Kahn 5.10 supply exact quotient statements. General full Tate and semisimplicity remain additional inputs; the new finite-field abelian cases have narrower scope.',
 'The author’s cancellation recognizes that the geometric kernel need not already have the asserted connectedness.',
 'Yes: the correction can be made explicit using a diagram and examples without developing a new theory.',
 ['DM1982','Kahn2025','CadoretHuiTamagawa','MilneReport2026'])
p(8,'Frobenius and a finite-field motivic protorus',[18,19],[25,26,27],
 'Use central Frobenius and Tate density to describe the finite-field motivic group and its rational conjugacy invariants.',
 'State the motive category, Tate fullness and semisimplicity before passing from Frobenius to the commutative group or Weil-number classification.',
 'Milne 1994, Propositions 2.4 and 2.6 and Remark 2.7, gives the conditional finite-field classification. The November 2026 report records newly stated abelian cases. Rational adjoint-quotient coordinates do not always give a rational representative.',
 'The general conjectural inputs are stronger than the formal centrality calculation; the sources do not justify removing them for arbitrary varieties.',
 'Yes: a finite-field case study would make the conditional chain precise and useful.',
 ['Milne1994','MilneReport2026','DM1982'])
p(9,'Splittings of filtered fibre functors',[22],[30],
 'Explain the unipotent torsor relating a filtered fibre functor to its associated graded.',
 'For the stated Tannakian setting, establish fpqc-local splittability and identify the sheaf of splittings as a torsor under the unipotent kernel.',
 'Ziegler 4.13 and 4.14 prove exactly these two steps. A global splitting over the original base is a different question.',
 'This is an open step on the pages with an exact later formal solution, not a current general research conjecture.',
 'Yes for exposition: reconstructing the hypotheses and torsor provides a short, complete companion note.',
 ['Ziegler2015'])
p(10,'Hodge tensors and the group denoted G0',[23,24],[31,32,33,34],
 'Identify the Hodge group with the group defined by algebraic-cycle invariants, and clarify positivity of invariant forms.',
 'Use polarizable rational Hodge structures, distinguish the Mumford–Tate tensor stabilizer from algebraicity of its Hodge tensors, and do not read the subscript 0 as an identity component without evidence.',
 'DM supplies the Tannakian and polarization models. The October 2026 paper states rational Hodge and generalized Hodge for CM abelian varieties; Remark 8.5 does not extend this to arbitrary complex abelian varieties. Invariance alone does not imply positivity.',
 'The cycle-fullness step remains a separate conjecture outside the proved or newly claimed scope; the draft’s positivity wording is also uncertain.',
 'Yes: a scope table and a few exact Hodge examples would prevent an incorrect blanket conclusion.',
 ['DM1982','CMHodge2026','MilneReport2026'])
p(11,'An abelian category over general bases with six operations',[26,28,30,31,32,33],[35,36,38,39,41,42,43,44],
 'Construct M(X), its derived operations, purity, Tate inversion, internal Hom and faithful realizations with the written finiteness conditions.',
 'Separate an established triangulated six-operation theory from existence of a compatible abelian motivic heart; retain regularity, constructibility, excellence and coefficient hypotheses.',
 'Cisinski–Déglise 2.4.50 provides the operation formalism; 14.4.1 gives absolute purity in the regular rational setting. Its constructibility results do not prove every proposed abelian-heart assertion. The purity display also needs the shift [-2d].',
 'The manuscript presents a programme. Later solutions provide much of its formalism but not the whole abelian package in this generality.',
 'Yes: an axiom-by-axiom correspondence with a fixed modern category is a useful bounded task.',
 ['CD2019','WeilII1980','DM1982'])
p(12,'Continuity and finite-stage descent',[27],[37],
 'Descend motives and the relevant direct-image data through essentially affine inverse limits.',
 'Fix the category and transition hypotheses, then distinguish compact-object descent, Hom continuity and compatibility of each operation.',
 'The checked Cisinski–Déglise introductory Theorem 7, with 15.2.4 and 15.1.6, gives the complete formalism in its separated finite-type setting over an excellent base of dimension less than 2. It does not establish the unspecified abelian-heart assertion.',
 'The gap is a mismatch of category and base hypotheses, not absence of every continuity theorem.',
 'Yes: a precise statement comparison can be completed in one run.',
 ['CD2019'])
p(13,'The cancelled coherent-realization programme',[29],[40],
 'The draft proposes an exact faithful coherent realization with functorial compatibilities, then cancels the paragraph.',
 'Any replacement must specify a de Rham or coherent realization and its actual target and exactness properties; it must remain a new reconstruction.',
 'Modern motivic realizations in Cisinski–Déglise provide context, but no exact surviving assertion is identifiable in the cancelled paragraph.',
 'Cancellation is visible. Neither the manuscript nor the opened source explains the author’s reason sufficiently to supply one.',
 'Only for historical commentary: do not revive the erased paragraph as an unqualified conjecture.',
 ['CD2019'])
p(14,'Independence of ell and characteristic data',[34,35,36],[45,46,47,48],
 'For a common motive, make lissity, ranks, traces and the weight tests independent of ell.',
 'Categorical traces follow from a rigid Q-linear tensor structure and compatible realizations; existence and lissity of the common object require separate theorems.',
 'DM proves the tensor formalism. Weil II 3.3.1–3.3.9 gives the checked weight and smooth-proper consequences for l-adic sheaves; current full Tate formulations still distinguish independence from the stronger cycle assertions.',
 'Formal trace rationality cannot itself construct the underlying common motive or show all realization compatibilities.',
 'Yes: disentangling the formal and geometric inputs is feasible and materially improves the dossier’s future use.',
 ['DM1982','WeilII1980','CadoretHuiTamagawa'])
p(15,'Dimension type, ordinary direct images and Ext',[38,39],[50,51,52],
 'Extend the early Tate-stable dimension filtration to ordinary direct images and internal Ext, and justify the stated vanishing for constant-twisted objects.',
 'Keep the early Tate-stable D separate from later generating dimension and Hodge level; distinguish internal Ext of locally free objects from global extension groups.',
 'The six-operation and weight theorems provide related bounds, but no exact theorem for this entire early D formalism was identified. Global extensions on a base need not vanish merely because the fibres are semisimple.',
 'The author flags these operations as uncertain; an ambiguity of Ext and a change of filtration prevent importing a later theorem verbatim.',
 'Yes: a carefully chosen curve example can settle which proposed bound is meaningful.',
 ['CD2019','WeilII1980','DM1982'])
p(16,'Primitive Tate strings and lambda operations',[40,41,42,43,44],[53,54,55,56,57,58,59],
 'Describe the Grothendieck ring by primitive Tate strings, classify the lowest primitives, use positivity for duality, and construct lambda operations via finite operator groups.',
 'In a specified finite-length tensor category, start from the simple-object basis and a fully faithful Tate shift. Repair the alpha=0 boundary and distinguish polynomial from Laurent notation before seeking multiplicative or lambda structure.',
 'The simple-basis and Tate localization arguments are formal. Weibel’s exact-category treatment shows what a lambda/endomorphism construction must specify. The primitive multiplication and general low-level classification are not proved by the subtraction rule.',
 'A literal boundary formula annihilates the unit, while multiplication needs additional structure constants; no source identifies a complete intended repair.',
 'Yes: a small exact example can test the ring presentation, but a new general classification exceeds one run.',
 ['Weibel2013','Jannsen1992','DM1982'])
p(17,'A motivic coniveau spectral sequence and its Ind terms',[45,49],[60,66],
 'Interpret the coniveau spectral sequence motivically from a suitable page or in Ind-motives, and extract the largest bipure part of the dense-open limit.',
 'Specify a category where the infinite direct limits exist, identify the E1 terms with residue-field objects, and prove the desired finite bipure subobject is representable.',
 'Bloch–Ogus gives the coniveau spectral sequence in cohomology; modern triangulated and birational theories give related constructions. The exact abelian Ind-motive extraction in the draft is not automatically supplied.',
 'The manuscript’s finite category is not by itself closed under the required infinite limits; this is a concrete categorical gap.',
 'Yes: the existence of the indicated finite subobject is a focused task after fixing the category.',
 ['BlochOgus1974','CD2019','KahnSujatha2016'])
p(18,'Dense-open level estimates and coefficient hypotheses',[46,61,62],[61,74,75,76,77],
 'Bound kernels and cokernels under dense-open restriction and bound ordinary or absolute cohomology of lisse coefficients by the stated weight windows.',
 'Separate smooth constant-coefficient estimates from arbitrary lisse pure coefficients. Use Deligne’s lower bound for ordinary cohomology and upper bound for compact support with their actual hypotheses.',
 'Weil II 3.3.5 provides the lower bound. The Legendre example from Stacks, Section 03VA, and the calculation in root_checks §4 contradict the sharper unrestricted lisse upper bound and its absolute-cohomology consequence. The weaker interval at scan 76 is not refuted by that example.',
 'The displayed statements conflate two coefficient regimes; several signs and indices also await the scans.',
 'Yes: an exact corrected lemma is both tractable and central to the later invariant programme.',
 ['WeilII1980','LegendreStacks'])
p(19,'The scissors ring and the top birational quotient',[47,48,53],[62,63,64,70],
 'Compare the scissors ring and its dimension quotient with the motive ring and primitive birational pieces; the first bijectivity proposal is cancelled and the ruled consequence rejected.',
 'Retain a motivic Euler-characteristic map where construction is established, and treat injectivity or quotient identification as additional statements.',
 'Gillet–Soulé Theorem 4 and Proposition 5 construct the characteristic and multiplicativity in characteristic zero. Larsen–Lunts identifies K0(Var_C)/(L) with stable-birational classes. The supersingular E×E example validates the author’s warning about a ruled conclusion from algebraic H2.',
 'The author supplies a counterexample to one proposed consequence; later scissors results preserve geometric information lost by pure homological motives.',
 'Yes: compare exactly the two quotients, without announcing an isomorphism between them.',
 ['GilletSoule1996','LarsenLunts2003','GorenLauter2006','KahnSujatha2016'])
p(20,'Lifting birational motive maps to rational maps',[49,50,51],[65,67,68],
 'Lift maps between the gamma invariants to field embeddings after stabilization; in particular, an isogeny of Jacobians should produce a dominant map after adjoining affine variables.',
 'The unrestricted formulation is false. Seek explicitly restricted geometric data that retains the polarization or another structure sufficient to recover a curve.',
 'Howe Theorem 1 supplies distinct genus-two curves with isomorphic unpolarized Jacobians. Maps from an affine-space stabilization to a positive-genus curve factor through the curve; Riemann–Hurwitz then rules out the desired dominant map between the pair. Separately, a section-retraction example prevents all nondominant maps being sent to zero by a nonzero functor.',
 'These are mathematical obstructions to the formulation, not merely a missing later literature hit.',
 'Yes for a negative companion theorem and a precise restricted question; a general reconstruction programme is larger.',
 ['Howe2005','MilneAV2008','KahnSujatha2016'])
p(21,'Does trivial positive birational motive imply unirationality?',[52,53],[69,70],
 'Ask whether entirely algebraic cohomology or vanishing of the positive gamma invariants forces unirationality; compare the subsequently rejected ruled consequence.',
 'The rational homological Tate-type formulation is false; any plausible replacement must retain substantially more geometry and specify the invariant.',
 'A complex Enriques surface has the required rational cohomological Tate type but is not unirational. Dolgachev’s survey provides the surface invariants; root_checks §3 supplies the implication and pluricanonical obstruction. No integral or Chow-motive strengthening is asserted.',
 'The invariant loses the relevant geometry. The manuscript’s own E×E example already rejects a related ruled conclusion.',
 'Yes: an exact negative result is short and prevents repeated rediscovery of an impossible conjecture.',
 ['Dolgachev2016','GorenLauter2006','MilneAV2008'])
p(22,'Effectivity from Frobenius integrality',[63,64,65],[78,79,80,81],
 'Characterize effective motives, and the proposed filtration, by Frobenius integrality; deduce finite monodromy in effective weight zero.',
 'Over a finite field in the specified semisimple Tate setting, distinguish the conditional motive classification from the elementary Kronecker theorem and from finite-image claims for arbitrary representations.',
 'Milne 1994, Remark 2.3 and Proposition 2.6, proves the relevant conditional effectivity/Weil-number description. Root-of-unity eigenvalues alone do not exclude infinite unipotent monodromy. The new 2026 abelian results alter the available inputs only in their stated scope.',
 'The integrality calculation does not independently prove full Tate or semisimplicity, and an eigenvalue test cannot detect unipotent extensions.',
 'Yes: a precise finite-field formulation and elementary counterexample are within one run.',
 ['Milne1994','DM1982','MilneReport2026'])
p(23,'A fundamental-group description of dimension type',[66],[82],
 'Find a better Galois description after the author rejects the naive filtration of the ordinary fundamental group.',
 'Distinguish the profinite quotient, algebraic monodromy groups, and tensor filtrations on a category of geometric representations.',
 'Kahn’s exact descent and the Tannakian formalism clarify these layers. The bounded search did not identify the exact proposed filtration as an established theorem.',
 'The author explicitly notes the failure of the naive construction; no source documents a unique replacement.',
 'Yes only after a fixed finite tensor subcategory and a test representation have been chosen.',
 ['Kahn2025','DM1982'])
p(24,'An ell-independent motivic Lie object',[67,68,69,70],[83,84,85,86,87],
 'Recover cycle invariants from Galois data and construct a common motivic Lie object whose realizations are the proposed Galois Lie algebras.',
 'Specify analytic image Lie algebra versus Lie algebra of the Zariski closure. The double commutant only recovers an associative envelope, and does not recover individual cycles or a group.',
 'The invariant-space result for an analytic compact image follows from open-subgroup stabilizers. SL2 and GL2 have the same standard associative envelope. A Frobenius example separates analytic and algebraic dimensions. Tannakian and current Tate sources provide comparison frameworks, not the unqualified common Lie object.',
 'The word Lie can refer to genuinely different objects; the ambiguity cannot be resolved from an associative commutant calculation.',
 'Yes: a precise two-dimensional test case can settle the required convention before further theory is attempted.',
 ['DM1982','Tate1966','Milne1994','CadoretHuiTamagawa'])
p(25,'Absolute cohomology with rational arithmetic comparisons',[71,74,76],[88,90,91,93,94],
 'Construct the absolute groups satisfying transitivity, continuity, cycle normalization and the indicated finite-field even/odd pattern.',
 'Specify motivic versus Weil-étale cohomology and the exact comparison map; do not demand simultaneously an odd rational unit class surviving restriction and its vanishing in the same continuous limit.',
 'Geisser Theorem 7.1 gives a rational Weil-étale splitting for smooth schemes over finite fields; Theorems 1.2–1.3 state the additional finiteness and special-value conjectural inputs. The draft’s simultaneous axioms are not all proved by this result.',
 'The written odd-unit normalization and continuity produce a concrete tension. Modern theories resolve different parts by choosing different complexes and hypotheses.',
 'Yes: a compatibility diagram for the unit over finite fields is a finite and decisive task.',
 ['Geisser2004','MilneADT2006','Tate1966'])
p(26,'Yoneda extensions, effaceability and Ind-motives',[73],[89],
 'Identify degree-one absolute cohomology with Yoneda extensions and determine higher effaceability, perhaps after passing to Ind-motives.',
 'Fix an abelian heart and an embedding into a triangulated category; compare Ext1 first, then state the exact higher universal-delta-functor or effaceability property.',
 'Cisinski–Déglise supplies triangulated formalism; it does not automatically supply the draft’s heart or the required higher Ext comparison. The Ind proposal remains a specific missing step in this formulation.',
 'The manuscript itself expresses doubt about effaceability; enlargement does not by itself prove the comparison.',
 'Yes: an explicit low-degree criterion is approachable, while construction of a general heart is not.',
 ['CD2019','DM1982','Geisser2004'])
p(27,'Arithmetic duality and the odd shift',[75,76],[92,93,94],
 'Give arithmetic duality with shift 2n+1 and explain the finite-field pairing with degrees summing to 1, including invariants and coinvariants.',
 'Separate finite-coefficient étale duality from rational Weil-style duality and impose the semisimplicity needed for the natural invariant-to-coinvariant map to be an isomorphism.',
 'Milne’s Arithmetic Duality Theorems provides precise arithmetic duality settings. Geisser supplies the rational Weil direction. A Jordan block shows why equality of dimensions does not make the natural invariant/coinvariant map invertible.',
 'The reused continuation supplies an arithmetic model, but the chosen absolute category and normalization remain part of the programme.',
 'Yes: the cyclic complex and pairings can be written completely in a short companion note.',
 ['MilneADT2006','Geisser2004'])
p(28,'Kummer, Sha finiteness and BSD',[78,79,80],[96,97,98,99,100,101,102,103],
 'Identify the rational-points contribution in H1(S,V_l A), kill the residual torsor Tate module, and relate the rank assertion essentially to BSD.',
 'Retain a regular model, an abelian scheme, ell invertible on the base, and the finite-cotype conditions needed to infer finiteness from vanishing of a Tate module; distinguish each BSD clause.',
 'The extension theorem and Kummer sequences are established. Kato–Trihan proves full BSD for an abelian variety over a global function field under finiteness of one primary Sha component. This is not an unconditional all-base Sha-finiteness theorem. The author later weakens one lattice comparison from bijective to finite kernel.',
 'The remaining Sha term is substantive; formal exactness cannot remove it. The sources do not identify a general solution to the manuscript’s broad formulation.',
 'Yes: a hypothesis-complete exact-sequence comparison is practical; a proof of general Sha finiteness is not.',
 ['Robert2023','SGA7IX','MilneADT2006','KatoTrihan2003','MilneBrauer1982'])
p(29,'Brauer–Sha comparison through Jacobians',[82],[106],
 'Ask whether the Sha-type assertion is approximately equivalent to surjectivity modulo finite groups of the proposed Brauer comparison.',
 'State the fibration, Jacobian and local-index hypotheses and distinguish prime-to-p statements from later p-primary refinements.',
 'Milne’s 1982 paper and author correction page specify the local-index assumption, the later relatively-prime weakening and the removal of a p-power qualification using later duality. The surface Artin–Tate and generic-Jacobian BSD equivalence is conditional in the stated way.',
 'The page says approximately because finite groups, indices and pairings matter; the later corrections confirm that these cannot be suppressed.',
 'Yes: the exact comparison sequence with finite error terms is a sharply bounded and valuable task.',
 ['MilneBrauer1982','KatoTrihan2003','MilneADT2006'])
p(30,'Higher cohomology of abelian schemes',[81,83,84],[104,105,107,108],
 'Establish higher primary finiteness and the later proposed vanishing, while retaining the worked constant-Jacobian example.',
 'Separate torsion sheaf cohomology H^i(S,A), its primary components, and rational cohomology of V_l A. Restrict any theorem to an explicit arithmetic base and degree.',
 'Milne ADT II.5.1 supplies the prime-to-characteristic finiteness/vanishing pattern over the stated global arithmetic curve setting; the 1972 Weil–Châtelet addendum supplies the local-field statement for all abelian varieties. Tate’s theorem gives the nonzero constant-Jacobian degree-two rational term, so the blanket later vanishing cannot be retained literally.',
 'A genuine contradiction survives between two draft passages; neither is visibly cancelled. Different coefficient objects also make a naive reconciliation unsafe.',
 'Yes: an exact degree-by-degree table on a proper curve would resolve the documentary conflict.',
 ['MilneADT2006','MilneWC1972','Tate1966'])
p(31,'High-degree Q_l(1) cohomology on proper schemes',[85,86,87],[109,110,111],
 'Ask for high-degree vanishing for proper schemes and compute the units, Picard and Brauer terms, including punctured curves.',
 'For proper smooth schemes over a finite field, apply the exact weight argument. Do not extend it to arbitrary proper singular schemes; for a curve minus r closed points retain the global residue relation.',
 'The SNC example in root_checks §4 has dim H4(X,Q_l(1))=4. Milne ADT II.2.1–2.2 gives Brauer corank r−1 for r≥1, rather than r. Weil II provides the smooth weight comparison.',
 'Both failures have explicit geometric or arithmetic mechanisms: singular weight contributions and one global residue relation.',
 'Yes: these counterexamples and corrected statements are complete short tasks, with no need for a new broad conjecture.',
 ['WeilII1980','MilneADT2006'])
p(32,'Positive forms, semisimplicity and isotypic cones',[88,89,90,91,92],[112,113,114,115,116,117],
 'Axiomatize positive forms, tensor and dual compatibility, and their cones; infer orthogonal splittings and reduce to simple endomorphism algebras.',
 'State the real topology of the form spaces, the target Q(-rho), twisted self-duality and nondegeneracy on subobjects. Distinguish weight zero from the trivial category.',
 'DM 4.10–4.11 and 5.12–5.13 provide the polarization model and formal splitting. The October 2026 abelian standard-positivity claim has its stated scope. End(h1(E)) disproves a universal identification of pure weight zero with ordinary vector spaces.',
 'The linear-algebra implications are conditional; they do not prove existence of the positive cones for all motives. A sign and a weight-zero phrase need scan review.',
 'Yes: a careful formal lemma and a Hodge example can clarify the entire local section.',
 ['DM1982','CMHodge2026','MilneReport2026'])
p(33,'Endomorphism categories over coefficient rings',[93,94,95,96],[118,119,120,121,122,123],
 'Extend the endomorphism Grothendieck-ring formalism from a field to a ring and use determinant, symmetric powers and traces.',
 'Use the exact category of finite projective modules for the rational-Witt theorem; separate reduced K0 from the zero-eigenvalue class and characteristic-zero ghost inversion from characteristic-p behavior.',
 'Weibel II, Application 7.4.3, states Almkvist’s theorem and the split K0(R) summand. The original Almkvist DOI was not opened successfully and is marked unverified. Elementary calculations verify the field kernel and the characteristic-p loss of ghost information.',
 'The field argument’s finite-length category cannot simply be retained over every ring; the chosen invariant also loses a zero-eigenvalue summand.',
 'Yes: the corrected field and finite-projective statements make a compact, complete companion result.',
 ['Weibel2013','Almkvist1974'])
p(34,'Coarse and relative L-invariants',[97,98,99],[124,125,126,127,128],
 'Recover virtual Frobenius data and coarse birational information from L, then extend the construction relatively modulo factors on proper closed base subsets; determine the needed smoothness and properness.',
 'Retain virtual semisimplification and Euler signs, specify coefficient purity, and formulate the relative quotient before asserting invariance.',
 'Weil II and Tate’s finite-field Hom theorem explain the constant-coefficient top-weight component/Albanese calculation. Kahn–Sujatha supplies a precise but different birational category. The 2026 Balkan–Schreieder function-field theorem is also different. No exact relative theorem matching the draft’s unspecified quotient was found in the recorded searches.',
 'The author explicitly leaves geometric hypotheses unsettled; characteristic polynomials also discard Jordan data.',
 'Yes: an exact relative definition and a test fibration are feasible, but this consolidation develops neither.',
 ['WeilII1980','Tate1966','KahnSujatha2016','BalkanSchreieder2026','Weibel2013'])

if __name__=='__main__':
 (P/'problems.json').write_text(json.dumps(problems,ensure_ascii=False,indent=2)+'\n')
 print(json.dumps({'problems':len(problems),'occurrences':sum(len(x['occurrences']) for x in problems)}))
