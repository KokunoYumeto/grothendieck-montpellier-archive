"""Human-authored consolidation of all five direction lists.
The code canonicalizes explicit IDs, renders Markdown and checks coverage; it never chooses mathematical priorities or merges by keywords.
"""
import csv,json,re,hashlib
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'deliverable'
def I(*ns):return [f'SA13-{n}' for n in ns]
def C(*ns):return [f'C-SA13-{n:03}' for n in ns]
def M(*ns):return [f'MP-SA13-{n:02}' for n in ns]
records=[]
def D(n,title,area,interest,reach,items,claims,problems,sources,goal,known,first,deliverable):
 records.append(dict(rank=n,id=f'D{n:02}',title=title,area=area,interest=interest,few_hour_reach=reach,items=items,claims=claims,problems=problems,source_directions=sources,would_establish=goal,known_scope=known,first_concrete_step=first,achievable_output=deliverable))
D(1,'Fix the quantifier in the Frobenius specialization lemma','Specialization and trace','Very high','High',
 I(367),C(355,363),M(149),['p3-D1'],
 'The exact valid specialization statement needed by A36 Lemma7.5, with a clear distinction between an arbitrary generization in a normal ambient scheme and the generic point of a normal integral base.',
 'The literal arbitrary-point version of Lemma7.8 is refuted in the dossier by a rank-one Frobenius module on a smooth ambient scheme and a nonsplit nodal specialization. The generic-point repair is proved using the finite étale fixed locus and its henselian finite part; Stacks0BTN,04GK and02LP supply the precise ingredients.',
 'Inspect the wording and insertions on36:026–027, then follow the use of7.8 in7.5. Record whether the intended reduction changes the normalization or special residue field.',
 'A corrected companion proposition, a dependence diagram for7.5, and an explicit statement of the residue-field obstruction. The established counterexample is a test for the proposed wording; the task does not seek to prove the refuted statement.')
D(2,'Type the local Verdier pairing and its global comparison','Derived functors and traces','Very high','High',
 I(32,33,34,35,37,100,101,102,103,104,106,107,108,109,111,112,122),C(36,37,38,100,101,102,103,104,105,124,125,165,166,167),M(9,30,31,33),['p1-D1','p2-D1'],
 'One map-by-map construction of the local correspondence pairing, its pushforward through the support counit, and its precise relation to integration of the global trace.',
 'Perfect evaluation and the published Lefschetz–Verdier formalism are available. The manuscript’s local existence, local isomorphism and global trace compatibility are separate assertions; finite Tor dimension alone does not supply every constructibility or boundedness condition.',
 'Write the four objects, both Hom factors and each adjunction arrow in the33:144→146→148→160 sequence. Compare that single typed diagram with original SGA5 III§4, fixing shifts, supports and Koszul signs.',
 'A verified diagram and a hypothesis table for one correspondence. The local and global assertions remain separately labelled, even though their source entries have been consolidated.')
D(3,'State trace additivity with its precise enhancement data','Derived functors and traces','High','High',
 I(25,26,36,110),C(24,25,26,39,125),M(7,32),['p1-D3','p2-D1'],
 'A companion statement distinguishing strict cone-compatible endomorphisms, arbitrary morphisms of distinguished triangles, and intrinsic trace of a perfect object presented by an unbounded complex.',
 'The elementary supertrace proofs and counterexamples are already checked in the dossier. They determine the necessary diagram data, but they do not decide the ink of the deleted boundedness qualification or turn every triangle morphism into a compatible cone endomorphism.',
 'Collate the boundedness marks and the exact published additivity statement. In one fixed cone model, identify the homotopies or enhancement that make the endomorphism diagram compatible.',
 'A minimal correct theorem, one counterexample explaining each omitted condition, and a clear account of resolution independence. This is a finite commentary task, not a request for a new general trace theory.')
D(4,'Resolve internal Ext, support polygons and top-edge conventions','Derived functors and depth','Very high','High after scan access',
 I(117,118,125,126,127,128,129,130,133,134,135,136,137,138),C(109,110,111,112,115,116,117,118,119,162,163),M(36,37,39,40,41),['p2-D2'],
 'One fully indexed local-to-global Ext spectral sequence with the correct sheaf/global convention, support dimension, and top-edge assertion.',
 'The finite-field and purity counterexamples in the dossier show that the missing sheaf mark and dimension normalization change the theorem. ILO XVII6.2 is an exact modern comparator; it does not identify a guessed polygon before the original indices are fixed.',
 'Check the Ext mark, codimension word, spectral-sequence page and total-degree indices on33:172–180. Then compute the support region and edge map for a single clearly specified bounded complex.',
 'A corrected support diagram and a short list of hypotheses for the uniform bound and localization duality. The distinct constructible-approximation question is reserved for D16.')
D(5,'Audit the Néron and p-adic implication diagrams','Reduction and arithmetic monodromy','Very high','High for one implication; medium for the full audit',
 I(224,250,257,258,267,274,277,278,432,433,435,436),C(213,214,215,251,256,257,310,432,433,435,436),M(60,64,65,72,75,78,99,100,175),['p2-D5','p3-D8'],
 'A source-based hypothesis table for the editorial Néron limit objections, the arithmetic orthogonality proof, and the good-reduction/inertia implications at ell different from p and at ell=p.',
 'The dossier has a good-reduction ordinary elliptic example with nonsplit p-adic inertia representation. Original SGA7 IX5.12–5.13 distinguishes the prime-to-p criterion from Barsotti–Tate extension. Completion base change, arbitrary limits, torsion subgroup closure and orthogonal-complement equality have different assumptions.',
 'Inspect the p-adic parenthesis on34:068–069 and match the two directions separately to IX5.11–5.13. Then attach the36:004 Remark2.6(a) objection to the relevant IX2.4–2.6 proof step without assuming identical draft numbering or scope.',
 'One complete implication diagram and a separate ledger for completion, finite étale lifting, henselianity, excellence and finite residue fields. The categorical torsion-extension question and the independent completion question must remain visible within that ledger.')
D(6,'Identify the finite invariant-cycle sequence and its vertical torsion obstruction','Picard groups and invariant cycles','Very high','High bibliographic; medium mathematical',
 I(414,417,419,421,425,428),C(414,417,419,421,428),M(93,95,97),['p4-D1','p4-D3'],
 'An exact statement of the amended finite invariant-cycle sequence, including its Brauer term and p-primary topology, together with the obstruction to replacing the torsion Picard component P^tau by P^0 in higher dimension.',
 'Raynaud1970 supplies the divisor/Picard ingredients and the curve comparison; §6.4.1 uses P^tau. In the curve case P^tau=P^0. The earlier CRAS announcements and every amended draft case have not been matched completely. The vertical kernel is different from the later component-group cokernel.',
 'Retrieve the original CRAS264 pages941–943 and1001–1004, identify the cited theorem3 and proposition7(ii), and write their hypothesis matrix. Use that matrix to specify one regular proper higher-dimensional degeneration whose vertical torsion can be followed into P^tau/P^0.',
 'A concordance for the finite sequence and a precisely defined obstruction group; a small example is a reasonable next output. The bibliographic matching and the higher-dimensional example are distinct work packages within the same vertical-Picard problem.')
D(7,'Separate whole-space trace variation from the nonconiveau conclusion','Specialization and trace','Very high','Medium',
 I(354,356,358,359,360,361,362,363,364,365,366,371,372),C(337,339,341,342,343,344,345,346,347,348,349,350,351,352,353,359,360),M(142,144,145,146,147),['p3-D2'],
 'A precise fate statement for the strong Hasse–Witt whole-space trace claim, and a separate complete finite-field deduction of the nonconiveau conclusion from stable-rank growth.',
 'The weaker invariant-subspace assertion does not imply the strong theorem or its every-residue corollary. Katz, SGA7 XXI1.4, proves nonnilpotence; Koblitz1975 I§5 Theorem2 gives stable-rank growth. The dossier’s finite-field deduction retains the fixed ambient zeta factors. None of these is the original every-whole-space-trace statement.',
 'Fix one family, base field and whole-space quantifier. Trace that exact assertion through the primary bibliography, while writing the determinant factorization for the stable-rank argument with each ambient factor displayed.',
 'Two explicitly separate propositions: the established finite-field implication with its scope, and an exact statement of what remains unidentified in the stronger trace-distribution claim. A short run should not promise the general converse from eigenvalue divisibility to correspondences.')
D(8,'Complete the categorical gluing theorem for biextensions','Biextensions and finite torsion','Very high','Medium',
 I(317,320,321,322),C(291,292,293,294,295,439),M(132,133),['p3-D3'],
 'An equivalence of the actual Picard groupoids described on36:048–050: a restricted biextension plus all compatible finite torsion pairings, with the one-variable and two-variable hypotheses stated correctly.',
 'The quotient tensor vanishing is proved. SGA7 VII2.7 and VIII1–2 give the long exact and Tor/pairing machinery, but no complete proof at the draft’s full generality was certified. The bounded-torsion example shows that retaining only the Tate pairing can lose information.',
 'Write the long exact Biext sequence, including automorphisms, and identify the obstruction and ambiguity maps. Construct a candidate quasi-inverse before iterating in the second variable.',
 'Either a fully faithful, essentially surjective reconstruction with explicit morphisms or a sharply identified missing hypothesis. Agreement of isomorphism classes alone is insufficient; the finite-level system remains part of the data.')
D(9,'Test faithful flatness for the actual H+D families','Formal geometry','Very high','Medium',
 I(463),C(463),M(112),['p4-D2'],
 'Whether the specified inverse and divided-derivative axioms force the ambient formal-series ring to be faithfully flat over the chosen family, when the constant extension is faithfully flat.',
 'The polynomial-family counterexample refutes a D-only interpretation. It does not satisfy the additional H axiom and therefore does not answer the H+D question. Standard Weierstrass systems impose further hypotheses that cannot be imported without checking them.',
 'Inspect the ambiguous axiom letter d. Fix a coherent local intermediate ring satisfying the full family axioms, and check locality, unit reflection and flatness one at a time.',
 'A proved subclass, a genuine full-family counterexample, or a precise missing-axiom statement. The unrestricted theorem should not be promised within a few hours.')
D(10,'Separate the compatibility and semisimplicity conjectures','Arithmetic monodromy and weights','Very high','Medium',
 I(217,223),C(185,186,187,188,209,210),M(163,164,174),['p2-D8'],
 'A theorem-by-theorem status table separating degreewise inertia trace, alternating trace, Weil–Deligne compatibility, a common rational form, geometric semisimplicity and weight–monodromy.',
 'The negative-trace example already refutes the literal nonnegativity assertion. Geometric semisimplicity is different from arithmetic Frobenius semisimplicity. The inspected Kato/Lu–Zheng results and the 2026 hyperkähler preprint have explicit scopes and do not settle every cell of the manuscript’s broad formulations.',
 'For each claim on34:033–036, index smoothness, properness, residue field, coefficient prime, degree and semisimplification. Attach one exact primary theorem or an explicit remaining gap to each cell.',
 'A reliable compatibility table with separate rational-form and motivic-extension questions. The task updates precise formulations, not a single universal status label for all compatibility problems.')
D(11,'Reduce one weight-piece independence question to correspondence ranks','Arithmetic monodromy and weights','Very high','Low for the general conjecture; medium for one reduction',
 I(68),C(655,662),M(202),['root-D8'],
 'The exact conditional implication from algebraic correspondence ranks to ell-independence for one chosen normal-crossing weight complex.',
 'The dossier records van Dobben de Bruyn’s equivalence theorem. Purity separates weights but does not determine the ranks of all restriction or Gysin maps. The general independence assertion remains conjectural at the stated scope.',
 'Choose one differential d1 or d2, identify the algebraic correspondence that would represent it, and list the precise standard-conjecture or rank-independence input required.',
 'A finite conditional theorem or a known-case reduction with every dependency named. The expected few-hour result is a rigorous reduction, not a solution of the general independence conjecture.')
D(12,'Fix the residue and d2 signs in a normal-crossing complex','Local cohomology and weights','High','High for one example',
 I(488,68),C(834,659,660,661,662),M(234,203),['p4-C2','root-D1'],
 'A coherent sign convention connecting the local Kummer-residue induction with the restriction/Gysin differentials in one proper normal-crossing spectral sequence.',
 'The local admitted square can be checked after fixing cup order and the Gysin convention. Coefficients must extend across the ambient strict-local scheme; the broader interpretation has a counterexample. Weight separation allows d2 and gives E3 degeneration, not automatic E2 degeneration. The motivic rank compatibility remains a separate assertion.',
 'Choose a two-component proper model. Write the support and open-complement localization triangles over the same cochain algebra, compute the r=2 residue square, and then identify the resulting d2 with its duality sign.',
 'One local compatibility lemma and one completely signed spectral-sequence example. These are two distinct calculations sharing the same boundary convention; neither is replaced by a broad appeal to purity.')
D(13,'Join the four-space cone diagram to the degree-and-depth conventions','Local cohomology and depth','High','Very high for a companion diagram',
 I(63,504,500,501),C(609,610,611,612,879,605),M(194,242,240),['p4-C3','root-D3'],
 'A single typed account of the local spaces, the two different localization triangles, the delayed cone comparison, and the specialization degree boundaries.',
 'The manuscript uses Phi_man=RΦ[−1]. Its punctured-fibre step needs vanishing throughout that punctured fibre, not merely at the removed point. Localization, codimension-one purity, derived inertia invariants and the checked degree bounds supply the ingredients; part(b) and a boundary sign still need coherent maps.',
 'Put both localization triangles in one fixed cone model. Record the rectified-depth convention and the lower and upper specialization endpoints, then compare the four-space diagram with Illusie2003’s variation diagram.',
 'A definitive degree/sign table and one verified cone diagram, including the later isolated-lci degree n+1 statement. The uniform-support hypothesis must be visible at the arrow where it is used.')
D(14,'Recover the sharp geometric-depth comparison','Local cohomology and depth','High','Medium to high',
 I(62),C(603,604),M(190,191),['root-D2'],
 'The exact localization and flat-local-map inequality for geometric depth defined by the minimum number of generators of a regular-presentation ideal, including the role of the residue extension.',
 'SGA2 XIV5 and Illusie’s finite-type relative version are identified. The invariant is neither ordinary depth nor a definition using arithmetic rank. The full all-noetherian wording and removal of the extra residue-field hypothesis were not matched.',
 'Express the invariant through the first two terms of the cotangent complex for a regular presentation. Follow every use of separability or formal smoothness in the flat-map comparison.',
 'A sharp hypothesis statement, with one proved special case or obstruction for removing the residue-extension condition. The documentary ambiguity must be resolved before a purported general proof is attempted.')
D(15,'Find the valid boundary of the infinite-root dimension bound','Local cohomology and depth','High','High for a precise boundary; medium for a new case',
 I(499),C(868),M(239),['p4-C1'],
 'A narrower correct dimension-reduction statement for the Kummer root tower, with excellence, regularity or geometric normal-crossing hypotheses made explicit.',
 'The arbitrary noetherian assertion is false by the dossier’s Orgogozo example and Cartan–Leray deduction. The regular-parameter Kummer computation and geometric local results provide positive cases. The already-refuted unrestricted statement is not an open conjecture.',
 'Compare the dimension-two nonexcellent example, the simultaneous-root calculation, Gabber affine Lefschetz and the known geometric-local setting in one hypothesis table.',
 'An exact boundary theorem or primary-source match, and a well-posed remaining case. A few hours can clarify which assumption fails; they do not justify promising a new unrestricted theorem.')
D(16,'Test constructible approximation with injective stalks','Sheaves and topoi','High','Medium',
 I(131,132),C(113,114),M(38),['p2-D3','p2-D2'],
 'A precise positive result or counterexample for writing a sheaf with injective stalks as a filtered colimit of constructible sheaves with injective stalks.',
 'The arrow-category example distinguishes injectivity of stalks from injectivity of the sheaf. It does not settle the actual approximation question. No exact match in the searched literature was found, which is not evidence that the question is presently open.',
 'Fix a noetherian scheme and a finite self-injective coefficient ring. Model one finite stratification by a diagram category and test both the stalk condition and the transition maps in the proposed filtered system.',
 'A verified finite-stratification theorem or a counterexample meeting the actual hypotheses. The first run should produce a useful test case and an exact statement, rather than extrapolating from stalkwise injectivity alone.')
D(17,'Trace the publication of the arithmetic coinvariant exposé','Arithmetic fundamental groups','High','High for concordance',
 I(219,220),C(198,199,200,202,217,218,219,220,221,222,223,224,225,226,227,228),M(169,176),['p2-D4'],
 'A publication concordance for the finite geometric abelian coinvariants theorem and its almost-all-primes conclusion, preserving the generic-curve reduction and boundary Tate twist.',
 'The dossier checks the finite-Jacobian proof, the dual invariants/coinvariants distinction and the open-curve localization sequence. C198 has been corrected to retain the generic parameter and valuation-control step. The printed SGA7 II exposé is a different text; numbering alone does not prove identity.',
 'Trace citations backwards from SGA7 I and the arithmetic fundamental-group literature. Match normality, geometric connectedness, finite generation, the finite-field reduction and the almost-all-primes quantifier one statement at a time.',
 'A dated source concordance with exact theorem numbers and a complete dependency map. The task should not redo a weakened curve proof that drops the generic-parameter or inertia-image requirement.')
D(18,'Repair the solvable-monodromy and constant-part reductions','Arithmetic monodromy','High','Medium to high',
 I(215,221,222),C(180,181,201,202,203,204,205,206,207,208,211,212),M(161,170,171,172,173),['p2-D6'],
 'A correct chain from solvable or unipotent Tate action to the appropriate constant-part or CM conclusion, with each field extension, radicial isogeny and torus quotient stated exactly.',
 'The claimed arbitrary-radical isogeny has a counterexample. The CM quadratic twist shows that a general finite cover cannot be replaced by a constant-field extension. C203–204 remain classC because the exact application of Grothendieck1966 Proposition4.4 is not fully verified; this is not a declaration of new mathematical openness. The nilpotent Frobenius-density argument is a distinct checked special case.',
 'Obtain Proposition4.4 in full and align its hypotheses with the geometric abelian-scheme setup. Then rewrite the radical argument using the correct torus quotient and list which steps require a cover, a constants extension or a radicial isogeny.',
 'A qualified implication diagram, an exact publication match where available, and an explicit list of the still-missing adaptations. Preserve the finite-level rigidity and CM steps as separate sublemmas.')
D(19,'Realize the ordinary-factor lifting counterexample','Abelian schemes','High','Medium',
 I(269),C(254),M(155),['p3-D5'],
 'A fully specified algebraic family completing the page’s proposed counterexample to lifting the largest ordinary abelian subvariety.',
 'If the generic abelian surface is geometrically simple, a positive-dimensional proper special abelian factor cannot lift as an abelian subvariety. The missing point is an exact family with the ordinary/nonordinary product as special fibre and the required generic simplicity. Formal and p-divisible subgroups are different objects.',
 'State the intended meaning of a lift, then locate a primary deformation or moduli theorem for that precise ordinary-times-nonordinary special fibre. Check that its hypotheses yield an algebraic abelian scheme with geometrically simple generic fibre.',
 'An explicit family or a complete cited existence argument, followed by the already-understood simplicity obstruction. A short run should not upgrade the original sketch before the family is checked.')
D(20,'Compute the weighted component-pairing comparison','Picard groups and pairings','High','High for a small example',
 I(443,444,445,446),C(443,444,446,481),M(103),['p4-D4'],
 'The integral comparison between the weighted divisor lattice and Grothendieck’s geometric component pairing in one concrete relative-curve model.',
 'The abstract discriminant construction is checked. Residue weights can make the apparent dual lattice have nontrivial index. Bosch–Lorenzini4.6–4.7 gives a qualified Jacobian comparison and perfectness conditions; those hypotheses must remain attached to the geometric claim.',
 'Choose a regular curve model with nontrivial residue degrees delta_i. Compute the actual integral dual lattice, the intersection map, the two finite groups and the induced comparison pairing.',
 'A completely worked example showing the finite index defect or proving its absence under the chosen hypotheses. This is a tractable calculation, without a promise of a new general perfectness theorem.')
D(21,'Recover the early pairing equality and its normalization','Biextensions and pairings','High','High once the two formulas are found',
 I(254,275,286,287,290,292,316),C(265,266,267,268,290),M(63,76,81,82),['p3-D4'],
 'The exact equality, sign and Tate-twist convention between the two pairings questioned in the early SGA7 editorial leaves.',
 'Finite perfectness does not determine an overall sign. Deligne10.2.4 and SGA7 VIII2.3 provide transition and transposition comparisons, but the two formulas referred to as A.M. and “yours” are absent. The later weighted curve pairing in D20 is related evidence, not an established identification of those early maps.',
 'Recover both draft formulas, the operation R and the one-factor versus two-factor transition. Normalize them on one elliptic-curve example before proving the categorical comparison.',
 'A finite-level equality with explicit conventions and a verified passage to the Tate limit. If one formula remains unidentified, the output should be a precise archival locator and an unresolved comparison, not an inferred equality.')
D(22,'Write the complete rigidity-to-NS continuation','Biextensions and Picard groups','High','High for a companion; medium for the unfinished lift',
 I(324,326,327,329,406,408),C(296,297,298,299,300,405,406,407,408,409,478),M(134,92),['p3-D7'],
 'One coherent statement across36:052 and054–058 covering group-Hom versus pointed-map vanishing, primitive torsors, biextensions, the symmetric NS defect and the proposed doubled Picard splitting.',
 'The one-variable primitive-torsor result and formal kernel injection are proved under universal rigidity. The continuation imposes extra additivity and an explicit special-case equivalence. Original SGA7 VII2.9 and VIII4.10–4.14 supply the qualified geometric comparisons. The quadratic sign alarm and unfinished canonical lift still need their own treatment.',
 'Join parts a,b,c with the same coefficient group and base-change convention. State which hypothesis makes each forgetful functor fully faithful, then identify the diagonal lift and verify its homomorphism and canonicity conditions.',
 'An annotated theorem chain and a separate last proposition for the doubled lift. The consolidated problem MP-SA13-134 retains that unresolved substep within the continuous NS object.')
D(23,'Reconstruct the finite-to-adic trace passage','Derived functors and traces','High','Medium',
 I(21,22,25,28,30),C(24,30,34,35),M(6,8),['p1-D5'],
 'The exact compatible system, uniform amplitude, finite-generation and inverse-limit hypotheses needed by the adic trace construction.',
 'The finite-projective matrix calculation is checked. SGA5 V–VI provides the historical finite-to-adic framework and explicitly does not construct a full modern adic derived category. An elementary congruence alone does not supply the required uniform derived bounds.',
 'Write the finite-level system used on33:128 and follow it through one proper-pushforward or compact-support example, recording every use of uniform Tor amplitude and limit exactness.',
 'A complete statement for one geometric system and a table of the missing conditions in the broader wording. This remains distinct from D24’s uniform descent of group-scheme data and D8’s retention of finite pairing information.')
D(24,'Find one model controlling an entire Tate tower','Reduction and finite torsion','High','Medium',
 I(436,439),C(436,439),M(101,133),['p4-D5'],
 'A justified passage from levelwise finite descent to a single finite amount of model data controlling all torsion levels in the stated adic setup.',
 'The quantifier gap between “for every level there exists an extension” and “one extension works for every level” is explicit. SGA7 IX2.6(a) handles its own arithmetic setting. Detecting a finite torsion point after a finite extension does not create a compatible rational division tower.',
 'List the finite-presentation objects used for every nu and identify one group scheme, multiplication map, filtration or biextension that determines them all. Check its descent hypotheses once, before iterating the torsion level.',
 'A uniformity lemma with exact assumptions or a precisely located failure. The task concerns uniform model data, not a claim that every finite pairing is recoverable from a Tate-module pairing.')
D(25,'Prove one named projection or Künneth coherence square','Derived functors','High','High for one square',
 I(9,10,11),C(12,13),M(3),['p1-D2'],
 'One resolution-independent base-change or composition compatibility for the projection and Künneth maps that the manuscript marks for checking.',
 'SGA4 XVII5.2.9 and5.4.3 gives the canonical maps; some auxiliary compatibility diagrams are left to the reader. The already-established general framework does not identify which exact omitted square is intended on the leaf.',
 'Choose one square on33:114–116 and follow every arrow through the original bounded resolutions, including the comparison maps between two choices.',
 'A complete proof of that named square and a reusable convention statement. A few hours can settle one compatibility; the task is not an unspecified reconstruction of the six-functor formalism.')
D(26,'Formulate the singular Picard–torsor comparison correctly','Picard groups and duality','High','Medium',
 I(296,297,298,299,300,302,304,305),C(272,273,274,275,276,277,278,279,280,281),M(84,85,86,87),['p3-D6'],
 'A precise singular or relative H1(X,A)–Picard/Ext statement, with the site, Picard component, base terms and internal/global distinction fixed.',
 'The nodal infinite-order abelian torsor and the real Brauer class rule out two unrestricted interpretations. Raynaud6.2.1 proves a finite locally free relative Cartier-dual Picard formula. That theorem does not automatically give the manuscript’s unspecified absolute abelian-torsor comparison.',
 'Choose one pointed nodal curve over an algebraically closed field and write the normalization and derived Picard sequences. Specify the relative site and retain the base-cohomology terms before comparing Ext groups.',
 'A valid special-case theorem or a diagram exhibiting the missing correction term. The direct-limit Q/Z correction and the distinction among Pic^0, Pic^tau and the full Picard functor must remain explicit.')
D(27,'Recover the functors in the higher-duality programme','Derived functors and Picard groups','Medium to high','Medium',
 I(295,304,305,306,307,309,310),C(271,280,281,282,283,284,285),M(87,88,89,154),['p3-D11'],
 'One well-posed finite bounded adjunction or duality comparison behind the handwritten f_! and higher-Picard formulas.',
 'The current symbols leave the site, variance, dualizing object and degree conventions underdetermined. Finite-free exchange and split evaluation are checked special cases. The cancelled divisor argument only produces a Weil divisor without additional Cartier hypotheses; derived filtrations and differentials cannot be replaced by an unexplained direct sum.',
 'Locate the missing definitions in the adjacent archive material, including33:166–167. Fix one f_! comparison and write its edge maps and competing terms before asking for a theorem.',
 'A typed formulation with a short verified special case and a list of documentary dependencies. Broad derived-category terminology is not itself a resolution of the programme.')
D(28,'Specify the noetherian-base cohomological-dimension hope','Cohomological dimension','Medium to high','Medium',
 I(8),C(9),M(2),['p1-D4'],
 'A hypothesis table separating noetherianity, finite dimension, finite type, excellence and coefficient invertibility in the proposed relative cohomological-dimension bound.',
 'The specified Gabber–Illusie finite-dimensional prime-to-characteristic theorem is an established comparator. It does not settle the broader literal wording. The later nonexcellent examples show why changing the base hypotheses can be decisive.',
 'Compare the quantifiers on33:110 with the exact ILO statement and one counterexample from the depth or infinite-root leaves. Identify the smallest formulation that the printed theorem actually proves.',
 'A precise statement of the established range and one sharply formulated remaining case. Keep this relative-bound question distinct from the particular Kummer-tower dimension reduction in D15.')
D(29,'Match the nonabelian depth proposal to local Lefschetz theorems','Local fundamental groups','Medium to high','Medium',
 I(62),C(607,608),M(192,193),['root-D7'],
 'The exact boundary between the trait theorem for low-degree or prime-to-p torsor specialization and the proposed arbitrary excellent local-base extension.',
 'Raynaud1974 and Orgogozo2003 have precise base and codimension restrictions. The manuscript’s geometric resolution and local Lefschetz dependencies are stronger than a generic subject-level reference to a modern theorem.',
 'Make a table with base, codimension, coefficient group, degree and geometric-depth assumption for the manuscript and each exact comparison theorem. Resolve which ambient space carries the singular-locus codimension.',
 'A theorem-by-theorem concordance and a well-defined broader proposal. A short run can locate the exact remaining hypothesis without claiming to settle all excellent-base nonabelian specialization.')
D(30,'State the arithmetic model-group Tate theorem completely','Arithmetic model groups','Medium to high','High',
 I(66,67),C(650,652,653),M(200,201),['root-D4'],
 'A complete proposition realizing the manuscript’s Tate endomorphism expectation in the arithmetic-model representation category, including normal-base extension and removal of finite component obstructions.',
 'The arithmetic Tate Hom theorem and Gajda–Petersen’s normal-base lemma settle the qualified model setup. Moret-Bailly XII2.4–2.5 gives the positive-characteristic provenance. Replacing the arithmetic model system by the ordinary geometric fundamental group would change the statement.',
 'Define the filtered Hom category for a normal qcqs base and check that an individual commuting matrix and the needed geometric data descend to a finite stage. Identify the later stage where the relevant component quotient vanishes.',
 'A complete exact-scope theorem and proof with the publication/circulation distinctions preserved. This is a completion of settled mathematics in the manuscript’s notation, not a new Tate conjecture.')
D(31,'Separate analytic, algebraic and profinite reconstruction','Arithmetic model groups','Medium to high','High',
 I(65,66),C(631,633,635,637,647,648),M(198,199),['root-D5'],
 'An exact comparison statement replacing the conflicting recovery sentence and the claim that both arithmetic Lie dimensions are always infinite.',
 'The dossier already checks fibre-functor reconstruction, recovery of the profinite component quotient, the obstruction to rational points meeting every component, and the finite-field example with analytic dimension one and algebraic dimensions unbounded.',
 'Translate the categories and natural arrows on34:185–188 into one diagram. Distinguish an isomorphism of pro-objects, equality of Lie algebras, openness of an analytic image and equality with all rational points.',
 'A corrected diagram and concise propositions explaining the two counterexamples. The task should preserve the role of the fibre functor and avoid replacing the actual Zariski-envelope density by a false general component-group criterion.')
D(32,'Prove BCH membership from the exact flow axioms','Formal geometry','High','High for a test case; medium for the full argument',
 I(453),C(453),M(106),['p4-D6'],
 'Whether the manuscript’s permitted flows and substitutions are sufficient to keep the BCH group law and induced homomorphisms inside the chosen A-family.',
 'The ambient formal BCH theorem is established. The leaf’s Ado reduction is unfinished, and an ambient matrix-group construction does not itself prove membership in A. Formal evaluation at1 is not automatically permitted.',
 'Work through a nilpotent matrix example with a multigrading and only allowed substitutions. Then isolate the exact closure statement needed to pass through the nonnilpotent Ado construction.',
 'A complete low-nilpotence case and a precise list of remaining A-membership obligations. The initial deliverable is bounded and testable even if the full axiom implication needs additional assumptions.')
D(33,'Test restricted-class Frobenius and quotient effectivity','Formal geometry','High','Medium',
 I(454,469,470),C(454,469,470,489),M(107,116),['p4-D7'],
 'When the first integrals of an involutive distribution and the effective quotient of its relation remain inside A, rather than only existing in the ambient formal category.',
 'The characteristic-zero constant-rank formal Frobenius theorem is established. The manuscript treats A-effectivity as an additional closure axiom. The rank-one flow comparison does not by itself prove the higher-rank restricted-class assertion.',
 'Specify a rank-two integrable distribution in an explicitly generated A-family. Construct local first integrals and check their chart transitions against the permitted substitutions and quotient criterion.',
 'A verified restricted-class example, a sufficient closure lemma, or a counterexample satisfying all initial axioms. Preserve the distinction between existence of an ambient quotient and membership of its maps in A.')
D(34,'Compare minimal inverse-closed families with henselization','Formal geometry','Medium to high','Medium',
 I(449,450),C(449,450),M(104),['p4-D8'],
 'The exact relation between closure under formal inverses and the algebraic power-series henselization, including the limits of a converse for arbitrary families.',
 'The henselian-pair criteria and ambient inverse theorem are checked. Henselianity solves algebraic implicit systems; it does not automatically imply closure under inverses of every chosen formal series. The minimal algebraic power-series example is a specific valid family.',
 'Fix the field and augmentation. Construct finite stages of the minimal H-closed family and compare them with explicit étale neighborhoods of the polynomial local ring.',
 'A precise minimality statement or a finite-stage obstruction to the proposed converse. The expected result is a useful formulation and test case, not an unqualified identification of all henselian families.')
D(35,'Resolve the integral saturation qualifier in monodromy','Arithmetic monodromy','Medium to high','Medium',
 I(483),C(819),M(238),['p4-C4'],
 'The precise integral filtration intended by the word pure or saturated, beyond the established rational unipotence bound.',
 'The q+1 nilpotence theorem is established. A canonical spectral filtration, its rationalization and the intersections of rational subspaces with an integral lattice are different constructions. Saturation is not automatic in an arbitrary spectral sequence with torsion.',
 'Inspect the adjective on the scan and identify which of those filtrations is meant. Test that definition on a torsion example before seeking a geometric saturation theorem.',
 'An exact convention and either a verified restricted statement or an explicit extra hypothesis. The task does not reopen the already-established broad monodromy theorem.')
D(36,'Descend A-coordinates and principal parts for projective modules','Formal geometry','Medium to high','Medium',
 I(457,465,467,468),C(457,465,467,468,485,486),M(108,114,115),['p4-D11'],
 'Coordinate-independent A-structures for finite projective modules, their principal parts and the associated induced smooth structures.',
 'Affine chart calculations work under the relevant H+D hypotheses. Finite projectives require transition and descent arguments; arbitrary finite modules may be singular and need a larger category. The local calculations alone do not certify global coordinate independence.',
 'Choose a rank-two projective module on a two-open cover. Write its transition cocycle and verify that the Hasse-derivative and principal-parts constructions respect it; then check one induced smooth completion.',
 'A transition-cocycle lemma and a worked projective example. Keep the singular finite-module extension outside the initial theorem while recording it as a separate later enlargement.')
D(37,'Audit the rational-point interpolation threshold','Finite-field constructions','Medium to high','Medium to high',
 I(368,369,370,372),C(356,357,358,361),M(150,151,152),['p3-D9'],
 'A correct explicit degree threshold, or a precisely stated limitation of the proposed bound, for sections with a prescribed finite number of rational points.',
 'Broad existence follows from finite-point interpolation after a finite field extension. The norm forms are valid and may be geometrically reducible. The sharper same-degree construction and coprime-product improvement require separate control of selected sets and disjoint rational zero loci.',
 'Reconstruct the actual finite split complete intersection and its selected subset. Check N≤r*d1^n, the final zero-set notation, and the dependence of the field extension and degree on N before optimizing the degree arithmetic.',
 'A verified bound in one fixed dimension or a concrete obstruction to the written threshold. Preserve the distinction between singular-section existence and a smooth-section assertion.')
D(38,'Determine the geometric content of the multiplicity-gcd insertion','Picard groups and invariant cycles','Medium','High for the source question; uncertain for realization',
 I(416),C(416,479),M(94),['p4-D9'],
 'Whether a hidden geometric constraint justifies the written product of gcds, or whether it is a genuinely false insertion in the multiplicity/index formula.',
 'The bare numerical identity gcd(mu_i*d_i)=gcd(mu_i)*gcd(d_i) fails. The numerical counterexample has not been realized by the regular-model geometry of the manuscript. Raynaud’s total-multiplicity definitions supply the correct comparison target.',
 'Resolve the ink and inspect those exact definitions. Then seek the smallest regular relative-curve model in which the two families of factors vary independently.',
 'A definitive source correction or a sharply specified geometric realization problem, with one small model if feasible. Numerical failure alone must not be presented as a checked geometric counterexample.')
D(39,'Recover Roos’s stronger minimum-topos criterion','Sheaves and topoi','Medium to high','Medium',
 I(169,170,171,172,173,195),C(130,131,132,133,134,135,164),M(46,47),['p2-D7'],
 'The exact representable criterion behind the minimum-topos characterization, including its affine-homeomorphism quantifier and universe bookkeeping.',
 'The ordinary Zariski retraction and Jacobson comparison are checked. SGA4 VII acknowledges Roos, but its4.1 is not automatically the stronger draft assertion. Conditions (A),(A′),(B) and the representable local-isomorphism lemma have different content.',
 'Order the reused leaves, compare the three conditions literally, and formulate the local-isomorphism lemma in one universe before comparing the small/big-site variants.',
 'A precise criterion and a source concordance, or an exact gap in the stronger wording. The task should reuse the already-checked retraction argument instead of treating it as the unresolved theorem.')
D(40,'Identify the quadratic-transform source and its missing dependencies','Local algebra','Medium','Medium',
 I(183,184,185,186),C(156,157,158),M(51),['p2-D10'],
 'The exact valuation and quadratic-chain theorem behind the cropped local-algebra sheets, with the genuinely missing dependencies identified.',
 'The dossier has already recovered Lemma2’s actual two-ring hypotheses by joining printed pages12–14 across scans33:173→137→135. The barred overring is not assumed to be a completion. The blowup-chart calculation is standard; the supplied sheets do not establish universal termination of quadratic chains.',
 'Identify references [A6]/[A7] and the still-absent Lemmas9–12. Determine the dimension, valuation and overring hypotheses they contribute to the chain argument.',
 'An exact source match and a qualified chain statement. Do not spend the run re-proving a falsely reconstructed common-completion lemma that the joined text has already corrected.')
D(41,'Test the fixed-square Bertini suggestion','Local fundamental groups','Medium','Medium',
 I(64),C(622),M(196),['root-D6'],
 'A small-degree example or obstruction for the prescribed-section hyperplane claim when the chosen line bundle is squared, rather than replaced by an unspecified sufficiently high power.',
 'The published hyperplane reduction and Orgogozo’s prime-to-p Lefschetz theorem do not prove the fixed exponent-two suggestion. The source also requires the prescribed section and boundary transversality, not merely existence of a smooth hyperplane.',
 'Recover the line bundle and section constraints on34:177. Test the lowest-dimensional embedded examples, keeping all those constraints and the fundamental-group condition visible.',
 'A verified special case or an explicit obstruction at exponent two. A successful sufficiently-ample argument alone does not answer the task.')
D(42,'Write a constructive preparation companion with controlled precision','Formal algebra','Medium','High',
 I(471),C(471,487),M(117),['p4-D10'],
 'A readable proof and an explicit division/preparation algorithm in the full separated complete linear-topology setting of the source.',
 'The theorem is established and re-proved in the dossier. The lower coefficients are topologically nilpotent, and the reduction of the distinguished series is a full unit series times Z^N; replacing that unit by one scalar is the identified defect.',
 'Rewrite the nilpotent-filtration inverse of the division map with explicit precision at each quotient. Check compatibility of those finite-precision solutions and compare the formulation with Strickland33.1.',
 'A clear algorithm and proof with a usable error/precision bound. This is an editorial and constructive task, not a claim that the preparation theorem is open.')
D(43,'Finish the historical curve-trace concordance','Derived functors and traces','Medium','High',
 I(18,19,20),C(19,20,21),M(5),['p1-D6'],
 'The exact relationship between the early curve plan and the published SGA5 XII, III and III B arguments, including nonconstant coefficients and local terms.',
 'The theorem and the documented1968 and1974–1975 compatibility history are established. Those publication and circulation facts do not date each individual archival leaf. The singular-coefficient case needs its own exact comparison.',
 'Choose one singular-coefficient curve statement and compare it with a numbered proposition of SGA5 XII. Record the additional local-term, support and coefficient hypotheses.',
 'A dated concordance and one complete annotated case. The outcome should distinguish historical dependency from mathematical implication and avoid assigning unsupported manuscript dates.')
D(44,'Identify the unmatched printings and the Griffiths citation','Source identification','Medium historical interest','Medium; high only when a candidate page is accessible',
 I(174,175,176,177,178,179,180,181,182,187,188,189,190,191,193,331,332,333,334,335,483),C(150,151,152,153,154,155,159,160,161,231,232,233,234,235,236,237,238,239,240,241,301,302,303,304,305,306,307,308,820),M(48,49,50,52,53,135,136,178,232),['p2-D9','p3-D10','p4-B1'],
 'Exact source identities for five still-distinct bibliographic tasks: the EVT revisions and cap exercise; the singular-operator theorems and integral normalization; the reused Lie p98/no316 leaf; the Čech T.F citation; and the complex-analytic monodromy statement attributed to Griffiths.',
 'The mathematics checked in those leaves does not determine a physical edition or author. Bourbaki and Godement remain candidates for particular leaves. The Griffiths monodromy reference at34:097–098 is not the A36 Griffiths-group theorem. The EVT and operator sources likewise remain separate families. The EVT task retains the cap, completeness and vague-metrizability dependencies; the operator task retains the symbol algebra, compact-kernel and multiplier-normalization questions. The Čech comparison must keep its empty-object convention.',
 'Select one of the five tasks for a bounded run. For EVT, locate Tribu63 and the old cap definition; for operators, locate4.5.2/4.5.4 and[18a]; for Lie, match p98/no316; for Čech, inspect the exact ChapterII§5 Theorem10.2; for Griffiths, trace the precise complex-analytic exponent-i+1 statement.',
 'A verified page-level identity, or a documented rejection of the best candidate. Each of the five tasks retains its own output and proof obligations; they are grouped as a source-search queue, not merged into one mathematical claim. No attribution or novelty inference follows from physical proximity.')
D(45,'Collate the identified GIT and Haar drafts against their editions','Source concordance','Medium historical interest','High for one source family',
 I(400,401,402,403,404,410,411,412,413,474),C(400,401,402,403,404,410,411,412,413),M(90,91),['p4-D12'],
 'An exact draft-to-print concordance for the two identified reused source families, including which marginal revisions changed hypotheses and which concern only presentation.',
 'The source families are identified as Mumford/GIT and Bourbaki Intégration. Draft dates and every edition-specific revision are not established. The quotient questions and Haar/subgroup-limit theorems are different mathematics and must retain separate source tracks.',
 'For GIT, compare the retained page numbers, free-action hypotheses, flat-versus-smooth projection and finite-type quotient questions with the first and second editions. For Haar material, compare the subgroup and covolume passages with Bourbaki VIII§5 and its compact-generation assumptions.',
 'A page-level concordance for one family in a few hours, with a separate ledger ready for the other. This task does not seek a new quotient theorem or a new Haar-limit theorem.')

# Canonicalize only the explicitly authored provenance lists.
alias_rows=list(csv.DictReader((OUT/'SA13_aliases.tsv').open(),delimiter='\t'))
aliases={r['alias']:r['canonical'] for r in alias_rows}
def canon(s):
 seen=set()
 while s in aliases:
  if s in seen:raise ValueError('Alias cycle: '+s)
  seen.add(s);s=aliases[s]
 return s
alias_uses=[]
for d in records:
 for key in ['items','claims','problems']:
  original=d[key][:]
  d[key]=list(dict.fromkeys(canon(x) for x in original))
  for x in original:
   if canon(x)!=x:alias_uses.append({'direction':d['id'],'kind':key,'alias':x,'canonical':canon(x)})
 # Space explicit source locators and theorem numbers in reviewer prose.
 for key in ['would_establish','known_scope','first_concrete_step','achievable_output']:
  d[key]=re.sub(r'\b(Lemma|Proposition|Theorem|Remark|Corollary|chapter|on|by|for|of|and|with|original|printed|the|pages|Tribu)(?=\d)',r'\1 ',d[key])
  d[key]=re.sub(r'\b(XXII|XXI|XVIII|VIII|VII|III|IX|XX|II|XIV)(?=\d)',r'\1 ',d[key])
  d[key]=re.sub(r'(?<=[,;])(?=[A-Za-z])',' ',d[key])
 # Resolve textual IDs in prose as well, so no retired identifier remains a current target.
 for key in ['would_establish','known_scope','first_concrete_step','achievable_output']:
  d[key]=re.sub(r'(?:MP-SA13-|C-SA13-|SA13-)\d+',lambda m:canon(m.group()),d[key])

# Metadata and coverage are derived only from these human-authored records.
source_files={name:OUT/'shards'/name/'directions.md' for name in ['p1','p2','p3','p4','root_codex']}
expected_sources=({f'p1-D{i}' for i in range(1,7)}|{f'p2-D{i}' for i in range(1,11)}|{f'p3-D{i}' for i in range(1,12)}|{f'p4-D{i}' for i in range(1,13)}|{f'p4-C{i}' for i in range(1,5)}|{'p4-B1'}|{f'root-D{i}' for i in range(1,9)})
actual_sources={x for d in records for x in d['source_directions']}
assert expected_sources==actual_sources,(sorted(expected_sources-actual_sources),sorted(actual_sources-expected_sources))
assert [d['rank'] for d in records]==list(range(1,46))
# Shard data are current even while the parent is rebuilding consolidated tables.
known={'items':{},'claims':{},'problems':{}}
for shard in ['p1','p2','p3','p4','root_codex']:
 for kind in known:
  for r in json.loads((OUT/'shards'/shard/(kind+'.json')).read_text()):known[kind][canon(r['id'])]=r
missing=[]
for d in records:
 for key in known:
  for x in d[key]:
   if x not in known[key]:missing.append({'direction':d['id'],'kind':key,'id':x})
assert not missing,missing

intro='''# SA13 — Ranked research directions

## How to use this list

This list consolidates all five reviewers’ proposed directions into **45 ranked directions**, covering all **52 source direction units**, including p4’s additional Codex directions and its separate Griffiths bibliography task. Every entry states the question to settle, the scope already established, a first concrete step, and a realistic output from a few hours of work. These are proposals for subsequent work; this consolidation does not develop them.

The order balances mathematical consequence, precision of the current formulation, and the chance of obtaining a concrete result promptly. **Interest and few-hour reach are assessed separately.** A high-reach editorial task may produce a complete companion lemma; a very-high-interest conjectural task may only produce a sharp reduction. A failed source search is never treated as proof that a problem is new or presently open. Results already refuted in the dossier are starting points for repairs, not propositions to attempt again.

All provenance IDs below are the **current canonical IDs** after applying `SA13_aliases.tsv`, including p2’s added Codex-only items. Distinct claims remain distinct even when their source items have been merged. The five unmatched bibliographic tasks in D44 are explicitly retained as separate work packages within a common search queue; the two identified families in D45 likewise keep separate edition tracks. Their grouping does not claim that the source texts or mathematical assertions coincide.

Source-dependent tasks begin with scan or edition inspection when the ink or missing definitions determine the theorem. The present dossier contains transcriptions, not a new decision on those scans. Exact publication references and the limits of their inspection are recorded under the cited claim and problem IDs and in `SA13_references.bib`.

## Priority map

| Priority | Direction | Interest | Progress plausible in a few hours |
|---:|---|---|---|
'''
lines=[intro]
for d in records:lines.append(f"| {d['rank']} | **{d['id']} — {d['title']}** | {d['interest']} | {d['few_hour_reach']} |\n")
lines.append('\n## Task specifications\n')
for d in records:
 lines.append(f"\n### {d['id']}. {d['title']}\n\n")
 lines.append(f"**Interest:** {d['interest']}. **Few-hour reach:** {d['few_hour_reach']}. **Area:** {d['area']}.\n\n")
 lines.append('**Item provenance:** '+', '.join(d['items'])+'.\n\n')
 lines.append('**Claim provenance:** '+', '.join(d['claims'])+'.\n\n')
 lines.append('**Problem provenance:** '+', '.join(d['problems'])+'.\n\n')
 lines.append('**Would establish:** '+d['would_establish']+'\n\n')
 lines.append('**Known scope:** '+d['known_scope']+'\n\n')
 lines.append('**First concrete step:** '+d['first_concrete_step']+'\n\n')
 lines.append('**Achievable output:** '+d['achievable_output']+'\n\n')
 lines.append('**Source directions:** '+', '.join(d['source_directions'])+'.\n')
lines.append('''
## Consolidation and completeness

The source labels use the original ordinal direction numbers: `p1-D1` through `p1-D6`, `p2-D1` through `p2-D10`, `p3-D1` through `p3-D11`, and `p4-D1` through `p4-D12`. `p4-C1` through `p4-C4` denote its new Codex table; `p4-B1` is its separately stated Griffiths bibliographic follow-up. `root-D1` through `root-D8` denote the root Codex appendix directions.

The consolidation combines the overlapping local trace work while keeping trace additivity separate; joins the Néron/p-adic hypothesis audit without deleting the independent completion and torsion questions; treats the vertical-torsion obstruction as a specific part of the finite invariant-cycle programme; aligns the two normal-crossing sign calculations; and joins the local cone comparison to its shifted-degree and uniform-support conventions. It retains the early pairing-equality question separately from the concrete weighted component pairing, the Tate model uniformity question separately from finite-to-adic trace and biextension reconstruction, and analytic/profinite reconstruction separately from the Tate endomorphism theorem.

The accompanying coverage table maps every source direction to its destination. The alias-use table records every replaced provenance ID. The reproducible builder only applies those explicit mappings and checks ID/coverage consistency; it does not infer priorities or mathematical overlap from keywords.
''')
(OUT/'SA13_directions.md').write_text(''.join(lines))
(OUT/'outputs/final_directions_records.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n')
coverage=[]
for src in sorted(expected_sources):coverage.append({'source_direction':src,'final_directions':';'.join(d['id'] for d in records if src in d['source_directions'])})
with (OUT/'outputs/final_directions_coverage.tsv').open('w') as f:
 w=csv.DictWriter(f,fieldnames=['source_direction','final_directions'],delimiter='\t');w.writeheader();w.writerows(coverage)
with (OUT/'outputs/final_directions_aliases.tsv').open('w') as f:
 w=csv.DictWriter(f,fieldnames=['direction','kind','alias','canonical'],delimiter='\t');w.writeheader();w.writerows(alias_uses)
validation={'directions':len(records),'source_direction_units':len(expected_sources),'missing_source_directions':sorted(expected_sources-actual_sources),'missing_provenance_ids':missing,'alias_replacements':len(alias_uses),'source_files':[{'file':str(p.relative_to(OUT)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in source_files.values()],'alias_file_sha256':hashlib.sha256((OUT/'SA13_aliases.tsv').read_bytes()).hexdigest(),'word_count':len(''.join(lines).split())}
(OUT/'outputs/final_directions_validation.json').write_text(json.dumps(validation,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(validation,ensure_ascii=False,indent=2))
