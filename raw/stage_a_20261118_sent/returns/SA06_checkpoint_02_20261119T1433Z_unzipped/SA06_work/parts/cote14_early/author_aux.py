#!/usr/bin/env python3
"""Individually authored problems and scan alarms after the complete assigned reading."""
import csv,json
from pathlib import Path
O=Path(__file__).resolve().parent
P=[]
def p(n,title,occ,as_he,plausible,art,why,worth,refs):
 P.append(dict(id=f'MP-SA06-{n:02d}',title=title,occurrences=occ,as_he_states=as_he,
 plausible_today=plausible,state_of_art=art,why_open=why,worth=worth,refs=refs))
p(1,'Recover the ambient effectivity data',['14/002–003 Pro3–30; SA06-6,7; C-SA06-1'],
 'Describe structure4° on an already givenM/G_Q, and compare rational and complex descriptions.',
 'Specify a neutral Tannakian category overQ, Tate character, weight cocharacter and descent-invariant effective tensor subcategory before asking classification questions.',
 'Deligne–Milne1982 Theorem3.2 supplies fibre-functor torsors, not the absent structures1°–3°. Nori/André are possible modern settings but are not named by these pages.',
 'The preceding axioms are absent from the assigned fragment; the text calls for further axioms rather than providing them.',
 'High value as documentary reconstruction: locate antecedent definitions before formalizing a theorem.', ['DeligneMilne1982','HuberMuellerStach2017'])
p(2,'Meaning of finitely many effective types',['14/003 Pro27–28;14/015 Pro310; SA06-8,28; C-SA06-20'],
 'Finitely many types of effective motives of fixed weight?',
 'For a specified finite-type quotient and an explicitly defined class of simple objects, ask a lattice finiteness question; all isomorphism classes cannot be intended.',
 'Milne2004 Proposition15.6 identifies torus simples by Galois character orbits. Arbitrary direct sums give an elementary obstruction to the unrestricted formulation; no theorem about the undefined types has been identified.',
 'The source writes question marks and leaves types undefined; no later explanation is in this segment.',
 'Worth a short run only after recovering the quantifier; otherwise it is not a determined mathematical problem.', ['Milne2004Shimura'])
p(3,'Infinite intersections and eventual Tate effectivity',['14/005 Pro64–65;14/009 Pro135–137; SA06-11,14; C-SA06-4'],
 'Take intersections ofP(i), with a caveat about the final grading condition.',
 'Require a uniform lower bound for every finite weight set relative to the positive Tate degree, or a suitable compactness/interior condition.',
 'The explicitG_m² familyi_m=(t,t^m) destroys a uniform twist; weight-category facts inMilne2004 reduce the issue to an elementary inequality. This is a counterexample to an unrestricted assertion, not to absent polarization axioms.',
 'The text itself recognizes a possible failure and never specifies its needed uniformity.',
 'Worth developing as a precise finite-dimensional cone lemma; the first step is to choose the topology and normalized cocharacter slice.', ['Milne2004Shimura'])
p(4,'Saturation and cone classification',['14/007 Pro90–107;14/009 Pro135–146; SA06-12–16; C-SA06-5–8'],
 'ClassifyW-invariant cones or intersections ofP(i) with a saturation condition that is not specified.',
 'Distinguish monoids, their rational convex cones, and normalized admissible cocharacters; formulate double-polar closure only for a chosen pairing/topology.',
 'Finite-rank torus descent and character positivity are established; they do not determine the manuscript’s missing saturation. The2N/N comparison is only a warning that positivity tests lose lattice saturation.',
 'The author explicitly says the saturation condition is not being made precise.',
 'Worth a focused reconstruction, with provenance labels preventing an editorial cone theorem from becoming an attributed conjecture.', ['Milne2004Shimura'])
p(5,'Injectivity of polarization/effectivity data',['14/011 Pro182–190; SA06-17; C-SA06-9'],
 'Question injectivity near the mapsI^a(G)→Pol(G)×Eff(G) andI(G)→Eff(G).',
 'After definingI(G), study whether two admissible cocharacters giving the same effective representation subcategory are conjugate under the stated real or complex group.',
 'Deligne–Milne1982 Theorem5.16 andPropositions5.18–5.19 classify related polarization data, but do not identify this undefined domain or prove these maps injective.',
 'Two adjacent formulations and missing axioms make the intended equivalence relation ambiguous; no source explains its abandonment.',
 'High interest once the definitions are recovered; a torus test can settle small cases in one run.', ['DeligneMilne1982','Milne2004Shimura'])
p(6,'One cocharacter for motivic effectivity',['14/011 Pro188–192; SA06-18,19; C-SA06-10,11'],
 'Do effectivity structures arising from motives lie inImI(G), independently of the fibre functor?',
 'For a chosen motivic category and admissibility condition stable under inner twisting, separate existence of one defining cocharacter from transport between fibre functors.',
 'Theorem3.2 ofDeligne–Milne proves the torsor transport mechanism. HMS pureNori/André comparison does not prove the one-cocharacter existence assertion.',
 'The page suggests intrinsicity but neither specifies the category nor proves the arithmetic existence statement.',
 'Worth separating into a formal descent lemma and a category-specific existence problem.', ['DeligneMilne1982','HuberMuellerStach2017'])
p(7,'Relative effectivity and de Rham realization',['14/011–013 Pro192–232; SA06-20; C-SA06-12'],
 'Extend the structures to motives over connectedS with a rational point and a de Rham fibre functor; a following formulation is deleted.',
 'Fix a relative motivic category and check exactly which filtrations, weights and fibre functors exist and descend overS.',
 'Arapura2013 §6.4 constructs a pure motivic-sheaf comparison for smoothS over a subfield ofC, under its own definitions. It is not a completion of the four unspecified structures.',
 'This is a brief program with a cancelled sentence; no construction is given.',
 'Low priority until the category and the role of the deleted de Rham condition are recovered.', ['Arapura2013'])
p(8,'Frobenius formulations of the extra structures',['14/011 Pro196;14/041 Pro893–915; SA06-22; C-SA06-13,53'],
 'Expect deeper arithmetic properties in terms of Frobenius elements.',
 'Choose a field of definition, a realization and a Frobenius torus, then formulate weight/effectivity inequalities on its characters.',
 'Milne2001 AppendixA gives explicit Lefschetz/Tate-group criteria for abelian varieties. No exact condition matching the unspecified four structures was found.',
 'The page contains an expectation without quantifiers, andg(k) is undefined in the later fragment.',
 'Worth only after making the Frobenius and category data explicit; a finite-field elliptic case is manageable.', ['Milne2001Tate','Milne2004Shimura'])
p(9,'Compact Tate kernel and the rejected field change',['14/013 Pro244–250;14/015 Pro310; SA06-24,25,28; C-SA06-16,17'],
 'Assertker(epsilon) compact; reject replacingQ byR; scope ofFausse remains unclear.',
 'Under polarized Tate-triple hypotheses a torus has compactker(epsilon); fixed-weight finiteness overQ is a separate Galois-lattice question.',
 'Deligne–Milne1982 Theorem5.16/Remark5.17 supplies the compact-kernel criterion with an additional parity condition for neutralness. The real-torus example disproves only an unrestricted field substitution.',
 'The proposed proof is cancelled and the marginal withdrawal is not scoped securely without scans.',
 'Worth a short comparison with the later real-fibre pages; the first task is a scan-level scope check.', ['DeligneMilne1982','Milne2004Shimura'])
p(10,'Character positivity versus effectivity',['14/015 Pro300–308; SA06-26,27; C-SA06-18,19'],
 'Ask whether nonnegative values on positive real points characterize effectivity; also consider boundedness toward the boundary.',
 'For actual characters of a specified torus and cocharacter, boundedness ast→0 is equivalent to nonnegative weights; real pointwise positivity alone is insufficient.',
 'The counterexamplesx^-1 andx²−x+1 separate the notions; the Laurent lowest-exponent proof is elementary. Milne2004 supplies the representation/character interpretation.',
 'The author writes question marks; no later decision appears here.',
 'Worth resolving as a small clarifying lemma, not as a new positivity theorem.', ['Milne2004Shimura'])
p(11,'Moving representatives in Albanese equivalence',['14/025–028 Pro522–602;14/055–056 K14-04:181–188; SA06-46,100; C-SA06-24,82'],
 'Verify good-position replacements for pullback and intersections; omitLemma1.5 as standard.',
 'Work in smooth projective Chow correspondence theory with refined pullback, then identify which raw-cycle formulations require explicit simultaneous moving.',
 'Stacks43.24.3 supplies simultaneous projective moving for finite lists. This settles the proper-incidence step in theSorites but does not by itself establish every quasi-projective or arbitrary-base variation.',
 'The source explicitly marks the earlier pullback stepàvérifier and omits the later proof for brevity.',
 'High tractability: write one exact common moving lemma and trace each application.', ['StacksMoving2026','Kleiman1968'])
p(12,'What is the Albanese-equivalence quotient?',['14/024–030 Pro506–647; SA06-42–54; C-SA06-22–32'],
 'Define cycles generated by images of degree-zero Albanese kernels under correspondences, ask how the resulting quotient compares with familiar equivalences.',
 'CompareN_Alb(X) with Samuel abelian equivalence and Picard/incidence kernels, preserving integral coefficients and both universal directions.',
 'Samuel1958/1960§2.5 and Kleiman1971pp446–447 use kernels of regular homomorphisms; Hernandez–Pelaez2025§4.1 retains that convention. Equality with the archive’s generated subgroup was not established by those sources.',
 'The archive builds its own equivalence and quotient before proposing representability; the later literature often uses the same adjective for a different definition.',
 'Very high value: derive the universal comparison maps and test their kernels in codimensions1,2,dimX.', ['Samuel1960Equivalence','Kleiman1971Finiteness','HernandezPelaez2025'])
p(13,'Albanese equivalence versus rational equivalence',['14/029–030 Pro616–647; SA06-50–52; C-SA06-28–31'],
 'Question equality with rational equivalence and exhibit box cycles lying in an Albanese kernel.',
 'Equality holds for divisors, but generally fails for0cycles on surfaces with nonzero holomorphic2forms.',
 'Mumford1969 gives the obstruction; onE×E the box cycles generate a nonzero Albanese kernel, while their degree andAlbanese sum vanish by direct calculation.',
 'The author’s question predatesMumford’s result; no claim is made that a specific box from the page was proved nonzero individually.',
 'Settled negative in general; useful now as a benchmark for any quotient comparison.', ['Mumford1969','Samuel1960Equivalence'])
p(14,'Square-zero with numerical triviality',['14/030 Pro647;14/034 Pro755; SA06-53; C-SA06-32,38'],
 'Ask whether the product of an algebraically trivial class and a numerically trivial class vanishes modulo Albanese equivalence.',
 'The proven version replaces numerical bytau-triviality. The numerical strengthening needs an exact comparison of the cycle relations.',
 'Divisibility proves thetau version. Grothendieck1969 andKleiman1968 distinguish numerical/homological assumptions; incidence filtration results inPelaez–Reyes2025 do not state this exact integral quotient identity.',
 'The later page proves a weaker statement, with no justification for the numerical strengthening.',
 'High interest afterMP-SA06-12; begin with surfaces and a precisely fixed quotient.', ['Grothendieck1969Standard','Kleiman1968','PelaezReyes2025'])
p(15,'Integral versus multiple universal cycle',['14/032–034 Pro681–755;14/051 K14-04:88–99; SA06-56,57,99; C-SA06-35,89'],
 'Construct a familyU inducingmultiplicationn onAlb(Y); ask whether denominators can be avoided for inverse comparison maps.',
 'Positive-degree miniversalcycles always suffice for rational inverses. Integral universal0cycles require a separate geometric condition.',
 'ACV2023Lemma4.7 gives miniversalcycles. Voisin2025Definition1.1,§2 andTheorem1.4 show the integral inverse can fail even for a smooth projective complex threefold with representableCH0.',
 'The manuscript invokes an isogeny multiple, and the later margin explicitly asks about denominators; modern counterexamples explain the obstruction, not the author’s historical decision.',
 'Very high value as a precise negative resolution of one denominator question, with other dual cases kept separate.', ['AchterCasalainaMartinVial2023','Voisin2025Universal0'])
p(16,'Saturation of algebraic point families',['14/035 Pro760–787; SA06-61; C-SA06-40,91'],
 'IfNphi is algebraic, isphi algebraic?',
 'Yes within the subgroup already factoring through the gradedAlbanese group; false for arbitrary point maps with torsion values.',
 'The savedP1→E[2] discontinuous point-map example refutes the unrestricted reading. The refined statement is a denominator multiplication identity; no external theorem is needed.',
 'The page first defines a factorization condition, then gives a terse saturation assertion whose ambient group may have been implicit.',
 'Worth resolving as a scope/reading issue; the corrected statement is immediate.', ['AchterCasalainaMartinVial2023'])
p(17,'Algebraicity of inverse P-group maps',['14/037 Pro808–810; SA06-64; C-SA06-45'],
 'Does a bijective algebraic group homomorphism of the manuscriptP-groups have algebraic inverse?',
 'For represented abelian varieties up to isogeny, yes; for abstract cycle quotients the representation hypothesis is an additional problem.',
 'Tate/isogeny theory verifies the represented case. The regular-homomorphism literature does not identify the generalP-groups with abelian varieties or settle every abstract inverse.',
 'The source explicitly postpones the question; no historical explanation of abandonment was found.',
 'Worth developing after establishing the representable range ofMP-SA06-12.', ['Tate1966','AchterCasalainaMartinVial2023'])
p(18,'Independence of transpose duality',['14/037 Pro812–825; SA06-65,66; C-SA06-46,47'],
 'Verify that transposition depends only on aP-group homomorphism, not its cycle representative, first forA(k)→P^i(X), then generally.',
 'EndpointPicard–Albanese cases are canonical; arbitrary codimension requires a well-defined quotient pairing and suitable representability.',
 'ACV2025 provides distinguished codimension2 autodualities under decomposition hypotheses. It does not prove the unrestricted transposition statement for this archive quotient.',
 'The text explicitly saysilfautvérifier; representative-independence is the missing step.',
 'High interest and moderate tractability: isolate the kernel-annihilation criterion before constructing dual objects.', ['AchterCasalainaMartinVial2025','Grothendieck1962Picard'])
p(19,'Vanishing family map and odd cohomology',['14/038–039 Pro830–878; SA06-67–74; C-SA06-48,50–52'],
 'u_Z=0 should imply the transpose correspondence acts as0 onH^(2(n−i)+1)(X)→H1(A); proofnotdone.',
 'State first in the regular-algebraic-representative setting and in the codimensions for which aTate-module comparison is proved; then compare its kernel withN_Alb.',
 'ACV2023§8 supplies precise realization comparisons, whileHernandez–Pelaez2025 gives motivic descriptions for Samuel’s relation. Neither has been identified as the unrestricted theorem for the archive quotient. TheJacobian reduction and curve projectors are valid, but the middle component remains.',
 'The source stops after the reduction and explicitly labels the proof unfinished.',
 'Highest research priority: one run can complete a rigorous reduction diagram and determine which published comparison would suffice.', ['AchterCasalainaMartinVial2023','HernandezPelaez2025'])
p(20,'Converse from rational cohomological vanishing',['14/038 Pro849; SA06-73; C-SA06-49'],
 'Ask whether the cohomological-vanishing implication has a converse.',
 'Separate integral pointwise vanishing from rational vanishing and restrict to a specified represented quotient; torsion cannot be detected byQ_l alone.',
 'The openedTate-module andregular-homomorphism sources establish qualified comparisons; no exact all-codimension integral converse was found.',
 'The source asks a question immediately after the unproved forward implication, without specifying torsion corrections.',
 'Worth a parallel kernel/torsion analysis afterMP-SA06-19 is formalized.', ['AchterCasalainaMartinVial2023','Tate1966'])
p(21,'Pseudoalgebraicity in Tate’s trick',['14/041–042 Pro893–929; SA06-82–84; C-SA06-53–55'],
 'Under the divisor Tate conjecture and pseudoalgebraicity or a two-eigenspace alternative, invariants should be decomposable.',
 'Replace the undefined pro-Lie algebra and eigenvalue words by an explicit Frobenius/Lefschetz group condition; the elliptic-power case is established.',
 'Tate1966MainTheorem andMilne2001AppendixA verify the elliptic case. The ordinaryE/F5 counterexample shows the normalized-root-of-unity sentence cannot describe every elliptic curve.',
 'The fragment offers only a sketch and an informal bracketed definition; the alternative hypotheses must not be collapsed.',
 'Worth a short invariant-theory reconstruction with all characters and Tate twists explicit.', ['Tate1966','Milne2001Tate'])
p(22,'Draft Lefschetz conjecture modulo algebraic equivalence',['14/044 Pro935–945;14/045 K14-04:4–8; SA06-79,81,98; C-SA06-56,58,92'],
 'ConjectureA isLefschetz on cycles modulo algebraic equivalence tensorQ;A′ is the hyperplane pushforward surjectivity form, with qualified reduction.',
 'Use algebraic cohomology classes for the standard Lefschetz conjecture; keep the draft relation as a historical, false stronger proposal.',
 'Clemens1983Theorem0.2 disproves the draft on very general quinticthreefolds. Grothendieck1969§3 gives the publishedA/B framework with different equivalence groups.',
 'The letter already recognizes that a cohomological formulation loses its desired geometric character. No checked source identifies a precise date when he abandoned the stronger draft.',
 'High historical value, mathematically settled negative: track the change of equivalence rather than attempt to prove the draft.', ['Clemens1983','Grothendieck1969Standard'])
p(23,'Draft positivity and the Hodge standard conjecture',['14/045 K14-04:12–14; SA06-80,98; C-SA06-57'],
 'Positive definiteness on primitive middle classes modulo algebraic equivalence.',
 'The published standard conjecture is positive definiteness on primitive algebraic cohomology classes, with the prescribedHodge sign.',
 'Grothendieck1969§4 gives the exact cohomological conjecture and itsWeil implication; characteristic0 is covered byHodge theory. The literal stronger quotient formulation has not been refuted here without a qualifying primitive even-dimensional example.',
 'The source gives no proof and suggests intermediateJacobians may enter; this does not identify a historical reason it remained unresolved.',
 'Worth an exact comparison and a carefully hypothesized counterexample search, not an unsupportedGriffiths shortcut.', ['Grothendieck1969Standard','Kleiman1968'])
p(24,'Pushing cycles to infinity',['14/046–047 K14-04:20–28; SA06-85,98; C-SA06-59,65'],
 'A″ predicts high-codimension cycles vanish moduloalgebraic equivalence on smoothaffines, and asks for a deformation pushing them to infinity.',
 'Cohomological affineLefschetz vanishing is true; algebraic-equivalence vanishing needs further restrictions and fails for suitablequintichyperplane complements.',
 'SGA4XIV3.2 gives the cohomological theorem. Clemens1983 plus localization and finiteNS of the boundary refutes the proposedcycle analogue.',
 'The letter explicitly says he has just started thinking and has no idea for the deformation.',
 'Worth a historical comparison with affinecycle theory; the broad proposed theorem is not a viable research target.', ['SGA4XIV1973','Clemens1983','SGA6XIII1971'])
p(25,'Algebraic intermediateJacobians and positivity',['14/037–039 Pro812–878;14/046 K14-04:18; SA06-66–75,98; C-SA06-47–49,64'],
 'Construct abelian parameter varieties, duality and oddcohomology relations fromA/B; perhaps use them in provingB.',
 'Separate existence ofalgebraic representatives, canonical symmetric autoduality, and positivity/principalpolarization under precise hypotheses.',
 'Kleiman1971pp446–447 recordsGrothendieck’s1964Picard-equivalence construction. Kahn2021 settles a gap in codimension2representability. ACV2025Theorem12.12 supplies qualifiedautoduality, whileConjecture5.1 leaves principalpolarization positivity open inits statedpositive-characteristic setting.',
 'The manuscript marks the programtentative. Modernsources identify specific proofgaps andpositivity questions, but do not explain this folder’s stopping point.',
 'Very high value: compare the archive’s exactquotient with the three modernnotions before proposing an extension.', ['Kleiman1971Finiteness','Kahn2021Regular','AchterCasalainaMartinVial2025'])
p(26,'Frommotivicsemisimplicity toGaloissemisimplicity',['14/046 K14-04:18; SA06-98; C-SA06-63,95,96'],
 'A/B should makepuremotives semisimple and imply theGaloissemisimplicity expectedwithTate.',
 'Keep numericalmotivicsemisimplicity separate from existence/fullfaithfulness ofaGaloisrealization and from the choice ofcycleequivalence.',
 'Jannsen1992Theorem1 proves numericalsemisimplicity. Tate1966 gives thefinite-fieldabelian comparison. Neither yields semisimplicity ofeveryGaloisrepresentation from anabstractendomorphismalgebrastatement alone.',
 'The letter compresses severalhypothesis bridges intooneparagraph; no fullargument ispresent.',
 'Worth a formal implicationdiagram; the next step is to write theexactfullness andtensorclosure assumptions.', ['Jannsen1992','Tate1966','Grothendieck1969Standard'])
p(27,'A reference for numericaldivisorialcorrespondences',['14/053 K14-04:135–147; SA06-100; C-SA06-78'],
 'Request a reference that a numericaldivisorclass produces the relevant canonicaldivisorialcorrespondence.',
 'Use the quotient ofdivisorclasses modulo pullbacks andalgebraic equivalence, together withtorsion-freeness ofHom(AlbY,AlbX).',
 'SGA6XIII4.6 identifies numerical andtau-equivalence forlinebundles; Grothendieck1962§3 suppliesPicard–Albaneseduality. These give the precise missinginput in the reconstructed proof.',
 'The source contains an explicitmarginalreference request.',
 'High tractability: supply a one-page proofwiththe correct divisorquotient rather than anunqualified appeal tonumericalcycles.', ['SGA6XIII1971','Grothendieck1962Picard'])
p(28,'RelativeSorites overarbitrarybase',['14/057–058 K14-04:208–211; SA06-102; C-SA06-85'],
 'Extend theAlbanesecorrespondence construction toCK-classes overarbitraryS, assumingthe relevantAlbanese schemeexists.',
 'State a representability/base-change theoremwiththe exactintersectiontheory andhypotheses required forrelativePicardfunctors.',
 'Grothendieck1962Theorem3.3 constructs therelativeAlbanesetorsor when thecanonicalabeliansubscheme ofPicardexists;Remark3.4 warns thatitneednotexist on arbitrarybases. ACV2023 givesrelative regularhomomorphisms underits ownbase hypotheses.',
 'The text marks this asaremark and conditions existence; no proof ofthearbitrary-SCKcompatibility appears.',
 'Worth developing, but only afterchoosing abasesetting wherebothPicardandintersectionoperations are defined.', ['Grothendieck1962Picard','AchterCasalainaMartinVial2023'])
p(29,'Mixedample degree-oneLefschetz map',['14/050 K14-04:52; SA06-99; C-SA06-88'],
 'Promise an isogeny forcupproduct byn−1 possiblydifferentampledivisors onH1.',
 'Prove thedegree-one mixedample statement using a smoothcomplete-intersectioncurve andthe inducedpolarization.',
 'ClassicalPicard/Albanesetheory andKleiman’sWeilcohomologyformalism give this restricted claim. It must not be expanded to all-degree mixedhardLefschetz inarbitrarycharacteristic withoutnew input.',
 'The summary saysNousverrons anddefers theargument beyondthe summarypages.',
 'High tractability as a local proofcheck; verify the preciseisogeny andmultiplicity factors.', ['Grothendieck1962Picard','Kleiman1968'])

byid={q['id']:q for q in P}
byid['MP-SA06-12']['state_of_art']='Samuel (1960), §2.5, and Hernandez–Pelaez (2025), §4.1, use kernels of regular homomorphisms. Saito (1979), Theorem 3.6, represents the common-kernel incidence quotient in all codimensions. Correspondence functoriality proves that the archive subgroup lies in the incidence kernel; equality of these integral relations is not established by the opened sources.'
byid['MP-SA06-12']['refs'].append('Saito1979Intermediate')
byid['MP-SA06-13']['state_of_art']='Mumford (1969), theorem on p. 200, supplies the obstruction. Grothendieck’s own letter to Mumford of 20 November 1968, Letter 46, p. 151, explicitly draws the negative answer for box cycles on a product of two elliptic curves. The cycle degree and Albanese sum are independently checked here.'
byid['MP-SA06-13']['why_open']='This question predates the result. Grothendieck’s letter records that Mumford’s preprint answered it negatively by 20 November 1968; that historical conclusion does not date or amend the archive sheet.'
byid['MP-SA06-13']['refs'].append('Grothendieck1968LetterMumford')
byid['MP-SA06-15']['state_of_art']='ACV (2023), Lemma 4.7, supplies a miniversal cycle of positive degree. Voisin (2025), Theorem 1.4 and §2, gives a published smooth projective complex threefold with representable CH_0 and no integral universal zero-cycle. Alexandrou (2026), Theorem 1.3, gives surface examples for its specified elliptic Albanese varieties, as a checked preprint result. A multiple remains available.'
byid['MP-SA06-15']['refs'].append('Alexandrou2026Universal0')
byid['MP-SA06-18']['plausible_today']='For integral correspondences from an abelian source A, transpose independence follows from the seesaw argument checked in this run. The full statement for arbitrary P-groups, and division by a denominator in Hom_alg, remain separate problems.'
byid['MP-SA06-18']['state_of_art']='The independent proof in proof_checks.md §8 establishes the integral A-source case for smooth projective varieties over an algebraically closed field. Saito (1979), Theorem 4.4 and Corollary 4.5, proves transposition for the different incidence quotient. ACV (2025), Theorem 12.12, supplies further qualified codimension-two autoduality.'
byid['MP-SA06-18']['worth']='High interest for the general and denominator-divided assertions; first isolate the exact kernel-annihilation condition beyond the integral abelian-source case already checked.'
byid['MP-SA06-18']['refs'].append('Saito1979Intermediate')
byid['MP-SA06-19']['plausible_today']='For k=C and integral Z on X×A, u_Z=0 in the archive quotient implies rational cohomological vanishing in every codimension. The arbitrary-characteristic version needs a separate realization argument.'
byid['MP-SA06-19']['state_of_art']='The independent argument in proof_checks.md §9 uses the earlier run’s observation that N_Alb is killed by Abel–Jacobi, then the family map to the algebraic intermediate Jacobian and Poincaré duality. ACV (2023), Proposition 8.2, separately embeds the Tate module of a surjective regular quotient using a miniversal cycle of degree r, for i=1,2,dim X and primes not dividing pr; this does not identify the archive quotient.'
byid['MP-SA06-19']['worth']='Worth extending to positive characteristic after fixing the quotient and its realization; the complex forward implication need not be reproved in a new run.'
byid['MP-SA06-19']['refs'].append('Saito1979Intermediate')
byid['MP-SA06-25']['state_of_art']='Kleiman (1971), pp. 446–447, records Grothendieck’s 1964 Picard-equivalence construction. Saito (1979), Theorems 3.6 and 4.4, constructs all-codimension incidence quotients and isogeny duality. Kahn (2021) repairs a gap in universal regular representability in codimension two. ACV (2025), Theorem 12.12, supplies qualified autoduality, while Conjecture 5.1 separates positivity in positive characteristic. None identifies every archive quotient with these objects.'
byid['MP-SA06-25']['refs'].append('Saito1979Intermediate')
(O/'problems.json').write_text(json.dumps(P,ensure_ascii=False,indent=2)+'\n')

R=[]
def r(scan,line,reading,alternative,evidence,weight='high',confidence='high'):
 R.append(dict(cote='14',scan=str(scan),line=line,reading=reading,alternative=alternative,evidence=evidence,weight=weight,confidence=confidence))
r(4,'Pro40','C1 for split endomorphism algebras','C1′, as onscan6 Pro82','Distinguishes allcentral-separable fromsplit; quaternionexample refutes unprimeduniversal reading. Noinkdecision.')
r(7,'Pro107','Gamma=S(C)','Gamma′=S(C) afterquotientbyW','The precedingdefinition isGamma′=Gamma/W; the unprimedorbitset has the wrongtype.')
r(11,'Pro194','Sl(2,Q)|Gl(2,Q)','Resolve theinitialletter on thescan','SL2 has no nontrivialTatecharacter;GL2 hasdet. The displayedstructure needs itsdistinguishedcharacter, andthe twoexamples have differentforce.')
r(13,'Pro cancelledcocharacter, near244–250','first coordinate0|1','1 ifthisis theG_m² torusnormalization','epsilon∘i=id requires thefirstexponent1; thepassage iscancelled andthis doesnotrestoreit.')
r(15,'Pro310','Fausse withunclearscope','Determine whetherthe cancellationmarks thefieldreplacement orcompactkernel assertion','TheQ→Rreplacement andpolarizedtorus compactness are mathematicallydistinct; noautomaticwithdrawal ofallprecedingclaims.')
r(19,'Pro395','i′ arrow inselfintersection diagram','Reverse arrow if itis thedisplayedclosed immersion','Pushforwardandrestriction must match thecyclecodimension; thediagram’swritten direction isilltyped.')
r(21,'Pro460–463','p_*(Theta²) withsupportfactor andc/c′','Determinecorrectprojection/domain andc′','ThePoincaré square hasdegree−2 onE×E; the extraEfactor changeswhichpushforward isdefined. Savedintersectioncalculation tests thetypedformula.')
r(24,'Pro506margin versusCodexK14-02 samepage','ConjecturesdeWeil','ConsulterWeil is theCodex alternative','Bothtranscriptionsareavailablebut noscan; thewordchangesfromresearchconjecture toreferencelead.','medium','medium')
r(26,'Pro543margin versusCodexK14-02 samepage','Lemmed’isog','Lemmeàdégager inCodex','Thepassage is theone-parameter/presentation construction; noimageallowschoosingone reading.','medium','medium')
r(29,'Pro625','[ ,1.2.] blankreference','PossibleSoritesCor1.2 onscan52','ThelaterCor1.2states exactly preservationofAlbanesekernel bycorrespondences. Mathematicalmatchdoesnotfilltheblankink.','medium','medium')
r(33,'Pro712–744','U(a)=nnu','Equality inAlbanesequotient, notnecessarilyrawcycles','Theuniversalcycle induces[n] afterAlbanese; rawcycleequality isstronger andnotproved. Maybescopecompressionratherthanmisread.','high','medium')
r(34,'Pro751','diviseur inarbitrarycodimensioni','cycle ifi is unrestricted','Thecorrespondence hascodimensioni; diviseur isvalidonlyifi=1. Noinkchange.')
r(35,'Pro783','SiNphi estalg.,phi l’est withoutambientqualification','KeepfactorizationthroughgradedAlbanese asanexistinghypothesis','A pointmapP1→E[2] mayhave2phi=0 whilebeingnonconstant; denominatorclearing onlyproves saturationinsidefactoredmaps. Likelymathematicalscopeomission, notdetermined ink.')
r(38,'Pro838,848','H^(n−i+1)(X)','H^(2(n−i)+1)(X)','Codimensionicorrespondence shiftsdegree by2i−2n; thetargetH1forces the2. SymboliccheckA03/A04.')
r(38,'Pro861','H^3(C)|H^1(C)','H^1(C)','Thecurve contribution ofanoddclass hasdegree1; H3 ofasmoothprojectivecurve is0.')
r(38,'Pro863','C(k)→A(k)surjective','J(C)(k)→A(k)surjective','A curveinsideanabeliansurface isaproperclosedsubset. ItsJacobian canmapontoA; thenextpage’sargument uses thatversion.')
r(39,'Pro876','H^(N−2|N−1)(X)⊗H^(2|1)(C)','H^(N−2)(X)⊗H²(C)','TotaldegreeN andthethreecurveKünnethcomponentsforce thispair.')
r(41,'Pro897–900','T_K(A)=T_l(A)','T_K(A)=T_l(A)⊗_(Q_l)K, ifT_l isalreadyrationalized','K-vector-space andg_Kactionrequire scalar extension; theintegral/rationalTate-module conventionalsoneedschecking.')
r(41,'Pro905–909','pseudoalgebraic meansnormalizedFrobeniusroots ofunity','Checkbrackets, alternatives andnormalization','TheordinaryE/F5example refutes a universalellipticreading, whilethetwo-eigenspacealternative survives. Noautomaticcorrection tosupersingular ismade.')
r(50,'K14-04:47','H^(deleted2n−1)1(B_T)','H¹(B_T) withthedeletionretained','ThetopoddcohomologyofT isdual todegree1ofPic0(T); thecancelledexponent doesnotbelongtoB_T.')
r(51,'K14-04:66–68','phi_X onthetopodd verticalarrow','psi_X accordingtoadjacentdefinitions','Thefour-casegridusesphi fortheAlbaneseH1map andpsi fortopoddPicardcomparison. Checkarrowlabelsandtwists.')
r(53,'K14-04:143','z′′·Theta|theta','theta′, thepullbacktoB×X′×Y','ThePoincaréclassmustbeon thesame tripleproductbeforeintersection.')
r(54,'K14-04:164','diviseur varpi onY','0cycle varpi onY','Thm1.1acts ondegree-zero0cycles; a divisor hasthatdimensiononlyforcurves.')
r(54,'K14-04:166','Pic0(A_X)','Pic0(B), B=(A_X)^vee','Biduality givesA_X≃Pic0(B), andscan55:170,175 explicitlyplacesbothsides inPic0(B).')
r(55,'K14-04:181–185','left/righttransposes withdeletions','Resolve ZversustZ fromdomainsbeforechoosingglyph','BothsidesmustbedivisorcyclesonB afterpushingthe0cyclefromY toX; noinkdecision.')
r(58,'K14-04:226','S_Y|S_X','S_Y','pr2pushforwardproduces a0cycleonY, henceAlbY; displayedu:B_X→A_Y independentlyforcesS_Y.')
r(20,'Pro417','S′ followed by S for the union of the hyperplanes','Use the same union in the complement and component statement','The argument studies one hyperplane arrangement throughout. This is a notation alarm only; the ink has not been checked.','low','medium')
r(4,'Pro51','M3=Hom_mathfrakM(M1,M2) is of finite type as a mathfrakM-module','Possibly A-module, or a missing specified commutant action','Hom over a noncommutative algebra does not generally inherit that same algebra action. If M1 is finite projective over mathfrakM, this Hom is a direct summand of a finite power of M2 as an A-module, which gives the required finiteness. The ambiguous glyph and missing action must be checked on the scan.','high','high')

def tsv(path,rows,fields):
 with (O/path).open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=fields,delimiter='\t');w.writeheader();w.writerows(rows)
tsv('readings.tsv',R,['cote','scan','line','reading','alternative','evidence','weight','confidence'])
print(f'{len(P)} individually formulated problems; {len(R)} undecided scan alarms written')
