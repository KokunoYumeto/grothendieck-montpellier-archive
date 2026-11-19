"""Author's questions and explicit proof obligations, manually consolidated."""
import json
from pathlib import Path
B=Path(__file__).resolve().parents[1];C={int(x['id'].rsplit('-',1)[1]):x for x in json.loads((B/'claims.json').read_text())};P=[]
def p(n,title,claims,as_he,plausible,art,why,worth,refs):
 occurrences=[]
 for k in claims:
  c=C[k];occurrences.append({'file':'SA09_texts/pro/MPL_138_090-133_transcription.tex','cote':'138','scans':c['scans'],'lines':c['lines'],'items':c['items'],'claim':c['id']})
 P.append(dict(id=f'MP-SA09-{n}',title=title,occurrences=occurrences,as_he_states=as_he,plausible_today=plausible,state_of_art=art,why_open=why,worth=worth,refs=refs))
p(70,'Normality of the extended geometric subgroup',[4],
'Is T̂ν normal inΓν, for the pure peripheral groups of scans89–90 andν≥2?',
'No: the same definitions yield nonnormality for everyν≥2; no stronger ambient-group equality is needed.',
'CL-SA09-138L-004 and proofs.md §2 give the all-rank deduction. Bétréma–Zvonkin1993 §4.3 gives the S3 sextic orbit; Belyi1980 §4 and SGA1 XIII supply the arithmetic action; Jones2013 Example7.7 makes the mirror/3-cycle obstruction explicit.',
'The sheets record a question without discussing its obstruction. No historical reason for its nonresolution is supplied; modern GT identifications impose extra compatibility.',
'Worth a short exact write-up because a finite orbit answers the literal normality question and separates it from stronger arithmetic-image programmes.',['BetremaZvonkin1993','Belyi1980','SGA1','Jones2013','Collas2026'])
p(71,'Normality inside the common-character kernel',[5],
'Is T̂ν° normal inΓν°?',
'Theν=2 case is yes becauseT̂2°=1; forν≥3 retain the exact ambient-group question without inferring an answer from full nonnormality.',
'McReynolds2012 Theorem1.1 identifies the genus-zero congruence closure. Collas2026 §§2.2,4.2 works with more constrained tower/Belyi-compatible groups; neither settles the literalν≥3 question in the located material.',
'No historical explanation on the page or in the opened sources; the obstruction for the extended group uses reflection, which is absent here.',
'Worth targeted group-theoretic investigation once the exact ambient definition is frozen; one run could test quotients but is unlikely to settle profinite normality.',['McReynolds2012','Collas2026'])
p(72,'Equality with the cyclotomic kernel',[6],
'When is T̂ν°=Γν°? The author adds that it is false forν=2.',
'With the inherited pure peripheral definition it is false for everyν≥2.',
'CL-SA09-138L-006 proves this by forgetting extra punctures and using a Galois commutator acting as a3-cycle on the1993 sextic orbit; the commutator has character1.',
'The rank-two failure is already acknowledged; the text does not pursue the forgetful-map implication.',
'Worth recording as a bounded completed correction, not reopening as an arithmetic-image equality conjecture.',['BetremaZvonkin1993','Belyi1980','Oesterle2003'])
p(73,'Faithfulness of the facet functor',[15,16],
'The facet functor is called obvious and conservative; a margin asks or tentatively states faithfulness for isomorphisms.',
'A corrected map category has a conservative facet functor, but cell data alone need not detect automorphisms; the literal precursor morphisms also fail closure under composition.',
'The permutation category in Guillot author PDF §§1.6–1.8 gives the complete incidence structure. The torusC2 kernel and the explicit precarte composition failure are certified in finite_maps.py.',
'The page changes its morphism equations and contains a tentative margin; no later source explains the abandonment.',
'Worth one run to compare minimal repairs of the actual morphism rule with the established permutation category.',['GuillotDessins'])
p(74,'Verify rigidity before fine moduli',[17,19,20,22],
'The category of cell-pinned maps is said to be rigid, with a genuine vérifier margin on100; representability and stabilizer formulas use it.',
'Cell pinning is insufficient in all genera. Flag pinning can give rigidity; the finite Galois set of geometric classes still defines a finite étaleQ-scheme, while the raw rational isomorphism-class functor is not representable.',
'CL017/019/020/022 and proofs.md §§4–5 supply a torusC2 automorphism, corrected orbit-stabilizer counts and explicit quadratic-twist failure of étale separation. Stacks Lemma58.2.2 supplies the valid finite-class scheme.',
'The verification margin identifies precisely the unproved dependency. No historical explanation for dropping it is found.',
'High-value repair: a focused run can state the smallest extra marking and distinguish a stack from its finite geometric-class space.',['GuillotDessins','Stacks03QR','SGA1'])
p(75,'Supply the omitted class-set definitions',[19,26],
'At scan99 line281: Définir ici C_C0 et C_C0^α.',
'Define the unpinned isomorphism classes, pinned isomorphism classes and fixed monodromy-type subset separately, using the actual automorphism action.',
'The finite permutation model gives explicit sets, with the orbit formula established in proofs.md §4; Stacks58.2.2 then translates a finite continuous Galois action into a finite étale scheme.',
'This is an explicit drafting instruction, not a conjecture or a historical open problem.',
'Worth completing in the companion commentary because it prevents three different sets from being conflated.',['GuillotDessins','Stacks03QR'])
p(76,'Compute the elementary arithmetic action',[36,37,46,79],
'Try to determineγ×Γ on elementary examples (scan103 line331).',
'Compute specified finite passports and label actions, with no inference to full faithfulness or a universal orbit classifier.',
'The star has theχ3 action on two pinned classes. The sextic orbit is explicitly in the spring1992 catalogue and Bétréma–Zvonkin1993 §4.3; our certificates reproduce it. Wood2006 Proposition4 separates two specific degree10 dessins using a new invariant, not all dessins.',
'The source deliberately begins with small cases; Bétréma–Zvonkin1993 §5 explains rising algebraic-computation complexity, not the author’s personal reason for stopping.',
'Worth expanding to one carefully chosen passport in a later run; the present sextic is already fully understood.',['BPZ1992','BetremaZvonkin1993','Wood2006'])
p(77,'Can a zero of P also annihilate the discriminant?',[40,41,42,43,44,45],
'But could the zeros ofP(c) be zeros ofδ(c)? (scan112 lines755–757).',
'Yes: P=−δR/7776. Keepδ≠0 for the intended two-distinct-critical-points passport;δ=0 gives a different valid Shabat passport.',
'Exact factorization and collision derivatives are certified in exact_arithmetic.py. Lando–Zvonkin2004 §2.2.2.3 explicitly treats the same parasitic factor; Bétréma–Zvonkin1993 §4.3 already isolatesR.',
'The page stops before factoringP; no external historical explanation is available.',
'Closed finite question; worth integrating into a corrected calculation, not treating as current open research.',['LandoZvonkin2004','BetremaZvonkin1993'])
p(78,'Cancelled transposition trials',[37],
'Scan107 lines487–494 asks which transpositions occur, but the entire trial is deleted.',
'Retain as a withdrawn computation; use the surviving permutation tables and the complete passport classification.',
'finite_maps.py checks the surviving tables and three oriented classes; Jones2013 Example7.7 confirmsS6 and the arithmeticS3 orbit.',
'The author cancels the trial locally. There is no evidence of a surviving general conjecture.',
'No separate research task is warranted; preserve the deletion in the commentary.',['Jones2013'])
p(79,'Axiomatize spherical operations',[54,55,57,79],
'The section heading explicitly says axiomatique provisoire (scan121 line1125), and proposes natural operations through functors with finite-quotient descent.',
'Specify a category, isotopy relation and descent condition before claiming a universal classification; rational Belyi-extending maps provide a well-defined subclass.',
'Ellenberg §3 (2000/2002) and Wood Proposition2 (2003/2006) establish Galois-equivariant postcomposition overQ. They do not classify all functor-valued operations.',
'Provisional status is explicit; source definitions and proofs remain incomplete. No historical account of abandonment was located.',
'Worth a few-hour reconstruction of one exact finite category, with universal classification deferred.',['Ellenberg2002','Wood2006','SGA1'])
p(80,'The formal global-section limit',[56],
'A formal argument is said to identify global sections with the printed varinjlim over normal finite-index subgroups.',
'A limit of compatible values is plausible after defining arrows and checking cofinality; a direct limit is not justified as printed.',
'SGA1 ExposéV and Stacks §58.7 justify passing to normal Galois covers by normal cores, but do not determine the unfinished diagram’s variance.',
'Transition maps are omitted. The arrows may be an ink issue or a convention issue; neither is decided.',
'Worth one short formal reconstruction after the scan is checked; no novelty should be presumed.',['SGA1','Stacks03SF'])
p(81,'Classify subset operations on the reference sphere',[57,58],
'The oriented powerset quotient is unfinished; an unoriented conjugation-invariant quotient is then written.',
'Pullback of a reference subset gives an operation, and reflection compatibility is necessary in the unoriented category. Surjectivity of the proposed classification needs precise naturality and topology.',
'Wood Proposition2 establishes the arithmetic rational subclass, while the hemisphere descent is elementary. No exact full classification was found in searched operations, Numdam, arXiv and MathOverflow material.',
'The denominator is visibly unfinished; no independent reason for noncompletion is known.',
'Worth formalizing in tandem withMP-SA09-79; one run can settle finite graph operations under explicit conventions.',['Wood2006','Ellenberg2002','GuillotDessins'])
p(82,'Universal graph and cellularity pullback tests',[59,60,61],
'The page says the graph test is immediate and gives a damaged necessary-and-sufficient cellularity condition.',
'For finite embeddedA, graph pullback is automatic; union graphness is an extra condition; cellularity for every cover is equivalent to A cellular and at most one branch value in each face.',
'proofs.md §8 supplies the exact finite proof and double-cover annulus obstruction, using the classical cover dictionary fromSGA1 XII and Zvonkin2004.',
'The surviving text has uncertain negations, a questionableS¹ and an unfinished union condition; no cause beyond the local draft is documented.',
'Worth a scan-led corrected lemma because the distinction between A and its complementary faces changes the theorem.',['SGA1','Zvonkin2004'])
p(83,'The exceptional old white endpoint',[62,76,82],
'What happens in the exceptional case when1 is a leaf of the new reference graph? (125,128).',
'An old clean index2 converts the leaf into an ordinary edge interior; the exact composition index is the product of the two local indices.',
'CL062/076 and proofs.md §9 give the full strict-clean criterion. Wood Proposition2 supplies only general Belyi preservation, so the endpoint exception remains a separate local condition.',
'The draft explicitly leaves the case for later and the fragment’s map letters are uncertain.',
'Worth including in the repaired operation definition; a short local calculation resolves the finite case.',['Wood2006','Ellenberg2002'])
p(84,'Finite isotopy kernel implies trivial kernel',[63],
'The revised theorem says the kernel is finite and sketches b⇒a through a finite-order disc assertion.',
'For finite connected cellular maps and map-preserving isotopies the kernel is torsion-free, hence finite means trivial.',
'Constantin–Kolev1994 Proposition3.2 proves the needed periodic-disc boundary theorem; proofs.md §10 checks reduction through vertices, edges and face boundary incidences.',
'The proof is interrupted on the page. The relevant periodic-disc theorem was classical; no source documents why the author did not complete this draft.',
'Closed under the stated finite hypotheses; worth a concise proof in the companion.',['ConstantinKolev1994'])
p(85,'Invariant rigidification and combinatorial realization',[64],
'The theorem lists existence of a G-invariant rigidification and realization of a combinatorialG-action as equivalent to the finite-kernel conditions.',
'A version is plausible for a specified finite cellular model and appropriate topology, but the missing definition prevents a determinate universal statement.',
'Constantin–Kolev supplies only the torsion obstruction. Esquisse §4 treats canonical conformal realization. Neither proves this exact undefined equivariant-rigidification statement.',
'No definition of rigidification was found in this package or the supplied adjacent scans; b⇒c is merely called evident.',
'Worth a definition-first archival task; a few hours can specify candidate spaces but should not claim contractibility by analogy.',['ConstantinKolev1994','Esquisse1984'])
p(86,'Contractibility of invariant rigidifications',[64],
'When the equivalent conditions hold, the space ofG-invariant rigidifications is contractible.',
'Only meaningful after the space and topology are fixed; contractibility of ordinary Teichmüller space or disc-homeomorphism spaces is not a substitute.',
'Exact searches found no matching theorem for this undefined object. Morvan2017 §11 Proposition8 concerns canonical representatives of fully marked dessins, not this invariant-rigidification space.',
'The space is unnamed beyond its phrase and no topology/proof is supplied. No historical explanation was located.',
'Potentially worthwhile afterMP-SA09-85; not suitable for an immediate theorem claim.',['ConstantinKolev1994','Morvan2017'])
p(87,'Literal uniqueness of a compatible Belyi function',[67,68,69,70],
'Is the compatibleφ unique? The author immediately says no on the sphere.',
'Uniqueness holds only up to the specified biholomorphic cover isomorphism; literal uniqueness additionally requires a trivial holomorphic map-isotopy kernel.',
'Guillot map/cover equivalence and SGA1 XII give the up-to-isomorphism result. The positive-dilation familyF_n(az) certifies literal nonuniqueness; fixed cell sets alone also fail to detect map isotopy on the torus.',
'The author himself retracts unconditional uniqueness and seeks a geometric repair.',
'Worth a precise distinction in the companion; no new proof of the standard correspondence is needed.',['GuillotDessins','SGA1','BetremaZvonkin1993'])
p(88,'A face of order at least three',[71],
'Does one face of order at least3 in each component restore uniqueness? He thinks yes, at least for finite maps.',
'Yes for finite tame cellular maps when map isotopy fixes the boundary prime ends: three distinct fixed prime ends kill the disc automorphism.',
'proofs.md §11 gives the conformal-disc proof with repeated boundary incidences counted correctly; classical realization is inSGA1 XII. This is a sufficient criterion, not the proposed complete exception classification.',
'The page explicitly asks to finish the conformal-representation argument; no later historical account was found.',
'Worth a short rigorous finite lemma and an exact statement of what fails in infinite settings.',['SGA1','ConstantinKolev1994'])
p(89,'Classify exceptional spherical maps',[72],
'It seems the only exceptions areI,II,III; oranges ofordern≥2 allegedly have no nontrivial holomorphic automorphism.',
'The list must include every radial n-orange map, which has positive-dilation freedom. A complete corrected classification is not supplied here.',
'Exact modelsF_n=4z^n/(1+z^n)² verify the counterfamily. Standard marked-dessin theorems (Guillot; Morvan2017 Definition8/Proposition8) retain white vertices and do not imply rigidity for the manuscript’s unmarked midpoints.',
'The tentative list follows an incorrect assertion about oranges. Earlier-run notes credit Hua for noticing the dilation obstruction; this run independently verifies the strict models.',
'High-interest bounded direction: classify finite spherical embeddings with a nontrivial holomorphic identity component, starting from Möbius one-parameter subgroups.',['GuillotDessins','Morvan2017'])
p(90,'Extend the conformal argument to infinite maps',[74],
'See whether the argument applies to infinite maps.',
'A locally finite, finite-face-degree version can be posed; the unrestricted wording has no fixed boundary or accumulation hypotheses.',
'Esquisse §4 printedp20 repeats the infinite-cartography programme. Cañas etal.2022 §§1,2.1–2.3 explicitly work with finite vertex degrees, finite-sided disc faces and locally finite branched covers; their Theorem2 concerns tame countable-group actions, not this unrestricted rigidity question.',
'The author explicitly leaves it for later. Modern results make extra hypotheses that the draft does not state.',
'Worth a bounded hypothesis audit before any infinite proof; one run can compare definitions and locate exact obstructions.',['Esquisse1984','CanasEtAl2022'])
p(91,'Add face centres or edge midpoints',[73],
'Face centres eliminateI,II,III; edge midpoints eliminateII,III but notI.',
'This is correct for the displayed examples and follows from real Möbius stabilizers; it is not by itself a universal uniqueness theorem.',
'proofs.md §11 checks the stabilizers. Morvan2017 §11 works with a fully marked bipartite dessin and canonical conformal realization, a distinct and stronger datum.',
'The text proposes a normalization without completing the general exception classification.',
'Worth using as a repair mechanism afterMP-SA09-89; a few hours can compare minimal markings case by case.',['Morvan2017','BetremaZvonkin1993'])
p(92,'Compare six holomorphic operation requirements',[75],
'Conditionsa,b,c and primed versions requiring equal holomorphic automorphism groups are listed on132 without a declared equivalence.',
'Distinguish same-surface compatibility, canonical-surface isomorphism, simultaneous union compatibility and equality of automorphism groups; implications need precise representatives.',
'Ellenberg §3 and Wood Proposition2 supply rational postcomposition preserving the source surface, but do not prove all six equivalent or preserve full graph-symmetry groups.',
'The source is an unfinished list; no historical explanation is available.',
'Worth a small implication diagram with counterexamples after the finite operation category is fixed.',['Ellenberg2002','Wood2006'])
p(93,'Characterize special maps preserving clean structures',[62,66,76,82],
'The proposed specialφ has ramification≤2 over1, maps0,∞ to0,∞ and may send1 to0,1,∞ with an unramified exception.',
'For universal strict cleaning replace≤2 away from the old1 by exactly2 and apply the full local-degree criterion inCL076; folded-edge maps are a different category.',
'Wood Proposition2 establishes Belyi preservation. The exact strict-clean refinement is proved in proofs.md §9; q=(2t−1)² shows why branch preservation alone is insufficient.',
'The inequality, exception and map letters are actively revised in the source.',
'Worth a precise definition and a low-degree enumeration in a separate run; the logical local criterion is already checked here.',['Wood2006','Ellenberg2002'])
for problem in P:
 if problem['id']=='MP-SA09-75':
  problem['occurrences'].insert(0,{'file':'SA09_texts/pro/MPL_138_090-133_transcription.tex','cote':'138','scans':[99],'lines':['SA09_texts/pro/MPL_138_090-133_transcription.tex:281'],'items':['SA09-289'],'claim':'CL-SA09-138L-026'})
 if problem['id']=='MP-SA09-79':
  problem['occurrences'].insert(0,{'file':'SA09_texts/pro/MPL_138_090-133_transcription.tex','cote':'138','scans':[121],'lines':['SA09_texts/pro/MPL_138_090-133_transcription.tex:1123-1127'],'items':['SA09-334'],'claim':'CL-SA09-138L-079'})
(B/'problems.json').write_text(json.dumps(P,ensure_ascii=False,indent=2)+'\n');print(len(P),'problems saved')
