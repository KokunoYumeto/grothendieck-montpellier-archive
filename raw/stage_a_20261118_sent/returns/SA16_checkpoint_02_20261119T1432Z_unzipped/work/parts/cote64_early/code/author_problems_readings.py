"""Explicitly authored problem and mathematical-reading decisions."""
import csv,json
from pathlib import Path
from author_records import items
ROOT=Path(__file__).resolve().parents[1]
I={int(x['id'].split('-')[-1]):x for x in items}
problems=[]
def p(n,title,ns,as_he,modern,state,why,worth,refs,extra=None):
 row={'id':f'MP-SA16-{n}','title':title,'occurrences':[{'item':I[i]['id'],'locations':I[i]['lines']} for i in ns],
      'as_he_states':as_he,'plausible_today':modern,'state_of_art':state,'why_open':why,'worth':worth,'refs':refs,'as_of':'2026-11-19'}
 if extra:row['additional_occurrences']=extra
 problems.append(row)
p(81,'Choose the natural orientation comparison',[215],
 'Compare the orientations of the four-set I and the triangle of its partitions; the comparison is functorial but subject to a choice.',
 'There are exactly two equivariant identifications of the associated C2-torsors; a stated convention chooses one.',
 'Closed locally by the author. The sign characters agree, and the two identifications differ by -1; independent proof supplement §1 and the finite character certificate. SGA1 XI §4 supplies the torsor formalism.',
 'The text explicitly identifies a convention choice, not an unresolved existence theorem.',
 'Low research value; preserve the convention for later normalized formulas.',['Burnside1897','SGA1'])
p(82,'Verify the ordered square-orientation identity',[220],
 'On scans12–13 he asks to verify the orientation convention and the effect of passing to the dual square.',
 'The invariant character identity holds, while the ordered representative identity uses the chosen convention; duality changes the indicated orientation.',
 'The verification on scan14 closes the earlier question. Proof supplement §2 and finite_groups.py check the D8 character identity and demonstrate the noncommutative order sensitivity.',
 'Closed later in the same packet; no evidence of subsequent abandonment.',
 'Low research value; useful as an editorial convention check, not a new problem.',['Burnside1897'])
p(83,'Recover a dihedral group from its reflection square',[221,222],
 'Scan16 asks whether a group of type D4 is equivalent to its square of noncentral involutions; scan17 gives the construction.',
 'The reflection-square construction is an equivalence of groupoids; a complete presentation includes involution, centrality and opposite-pair relations.',
 'Resolved by the following page and the independent proof supplement §2. Aut(D8) acts faithfully on four generating reflections and has order8. The literal commutator-only presentation is incomplete (C-SA16-222/322).',
 'The functor Q→Aut(Q) was not faithful, prompting a different reflection construction; the following page supplies it.',
 'Low research value; repair the presentation explicitly in commentary and check the omitted relations on the image.',['Burnside1897','SGA1'])
p(84,'Classify all subgroups of S4',[224],
 'State the classification and check that all subgroups have been counted.',
 'There are30 subgroups in11 conjugacy classes, with the exact distribution stored in the certificate.',
 'The page reaches the count; exhaustive enumeration rechecks it. Burnside1897 §§142,146,173 provides the classical permutation-group setting, not a claim to our precise table.',
 'Closed by the author’s list and count; the diagram is separately unfinished.',
 'Low research value; the enumeration is complete and reusable.',['Burnside1897'])
p(85,'Draw the subgroup and homogeneous-space diagram',[225],
 'Il faudrait faire un diagramme: inclusion relations or the corresponding morphisms between homogeneous spaces.',
 'The30 actual subgroups form a poset with66 cover inclusions; S4/H morphisms additionally depend on transporter cosets, not merely subgroup conjugacy classes.',
 'The subgroup-poset part is completed in s4_subgroups.json and s4_hasse_edges.json. For transitive sets, Hom_G(G/H,G/K)={gK:g^-1Hg⊂K}; proof supplement §1 supplies the subgroup data and this standard formula gives all morphisms.',
 'The packet contains the request but no drawn completion. No source explains why it was not drawn.',
 'Moderate expository value; one short run could render both poset and transporter category from the saved exact data.',['Burnside1897','SGA1'])
p(86,'Write the cube correspondences explicitly',[229,249],
 'The forward reference on scan7 and request on scans23–24 ask for explicit conversion maps between cube features and group-theoretic objects.',
 'The ten nontrivial transitive rotational cube sets correspond to the ten proper subgroup conjugacy classes; the face-diagonal stabilizer lies in V4.',
 'cube_and_pgl.py supplies each concrete set, orbit and stabilizer. The orientation calculation is marked OK on scan25; the other conversions are completed here. Burnside1897 §§202–203 gives the classical rotation group.',
 'Only parts are spelled out on the pages; no historical reason for the omitted maps is documented.',
 'Moderate expository value; drawings of the certified features would make the finite dictionary easier to use.',['Burnside1897'])
p(87,'Uncertain forward promise beside the face torsor',[250],
 'The possible words On verra are uncertain and the following marginal span is illegible.',
 'No determinate mathematical conjecture can be reconstructed beyond the adjacent face/character discussion.',
 'Class F for the uncertain marginal promise. The surrounding face quotient is checked by C-SA16-241, but searches cannot determine the missing words.',
 'The obstruction is missing visual evidence, not a documented mathematical difficulty.',
 'Image check first; no research development should be built on this fragment.',['BrauJones2016'])
p(88,'Lift projective mod-4 data through the central extension',[244,245,246,248],
 'Scans37–38 ask when a projective torsor lifts through GL(M)→GL(M)/{±1}, then reduce it to reconstructing a square from diagonal and codiagonal torsors.',
 'For the two C2 classes c,d, the obstruction is c∪d in H2; when it vanishes, lifts form the groupoid of C2-torsor twists of a chosen lift. The universal extension does not split.',
 'C-SA16-244–246, finite factor-set certificate and proof supplement §5 resolve the question. MerkurjevScavia2024 §1.1 Example1.4 proves the exact profinite-group cup criterion; the relative cocycle/gerbe argument is given separately. Ledet2001 metadata was opened but its cited exact section remains unverified.',
 'The bracketed discussion ends after the reduction; no criterion or reason for stopping is stated before the recap.',
 'High expository value; a short run can package the obstruction in the precise relative category used later.',['MerkurjevScavia2024','SGA1','Ledet2001'])
p(89,'Prove uniqueness of extending octahedral symmetries',[262,263,264,265],
 'The small argument on scan51 is requested to justify extension and uniqueness; scans48–53 also assert the full bare six-point stabilizer equals the direct octahedral group.',
 'With2 invertible, retain the regular opposition and obtain rank24. If opposition is forgotten, also invert5. In characteristic5 the bare stabilizer has120 geometric elements and five regular oppositions.',
 'The structured relative proof and counterexample are in proof supplement §6 and cube_and_pgl.json. Hua2026 §42 Thm42.1/Counterexample42.2 settles the field fixer calculation but explicitly leaves the relative theorem unproved; Beauville2010 gives a field normalizer under its prime-to-characteristic convention.',
 'Rejected arithmetic is visible on scan50, but the false general conclusion is not withdrawn. No external source explains why he stopped.',
 'High value; a short run can turn the relative correction into a concise, checked commentary theorem.',['Hua2026','Beauville2010','SGA1'])
p(90,'Interpret the four-cover/conic corollary and orientation insertion',[267,268],
 'The corollary identifies structured octahedral conics with four-covers and includes an orientation identification whose attachment is uncertain.',
 'Use forms of the reference conic x²+y²+z²=0 with opposition and its canonical orientation identification with μ4*. An independent extra orientation choice would change the groupoid.',
 'Our signed-permutation reference proof supplies the relative equivalence (supplement §6). BeauvilleProp1.1 provides the rationality restriction; Hua§42 records this corollary as unproved and flags the insertion.',
 'Both an omitted proof and uncertain insertion remain on these pages; the next image run must decide its attachment.',
 'High editorial value; the mathematical alternatives are now distinct enough for an exact image check.',['Beauville2010','Hua2026','SGA1'])
p(91,'Remove the constancy assumption in the Klein twist',[260],
 'The page first supposes I constant and then says that hypothesis is superfluous.',
 'I=K∧F_t and K=I∧F_t hold for arbitrary V_J-torsors with their prescribed action identification.',
 'Closed in the same text and verified by exponent-two cocycles, supplement §7. SGA1 XI §4 gives the exact associated-torsor construction.',
 'The author expressly drops the hypothesis; it is not an open conjecture at the end.',
 'Low research value; retain the dropped hypothesis as a local correction.',['SGA1'])
p(92,'Check the almost-cartesian square',[275],
 'Scan62 requests verification of the qualified almost-cartesian diagram.',
 'Off the branch the square is cartesian. Geometric completed local fibers have equation v²=u² and recover the smooth branches by normalization; over general nonnormal bases use the canonical smooth branch model rather than an unqualified absolute-normalization claim.',
 'The local algebra and torsor comparison are proved in supplement §7. SGA1 supplies descent and tame background; no exact independent published theorem with this diagram and all relative wording was located.',
 'The author asks for the check but gives no completed verification or explanation of why it was omitted.',
 'Moderate value; a short run can formalize the relative square and state the precise universal property.',['SGA1'])
p(93,'Define doubling intrinsically on the four-point line',[277,278],
 'Scan63 asks for a definition of f2^t intrinsic in the four-point geometry, without first selecting an elliptic curve.',
 'Quotient by the canonical Klein subgroup and identify the target by the three branch labels; degree4 and those labels determine the normalized map.',
 'Resolved by the quotient proof and subsequent coordinate formula (C-SA16-277/280). Milnor2004 Thm3.1 matches the complex Lattès quotient framework; our algebraic proof keeps2 invertible and t,t−1 units.',
 'The following two pages perform the calculation; the intrinsic wording is not expanded there into a separate theorem.',
 'Moderate expository value; a short proof makes a useful bridge between his combinatorics and the classical multiplication map.',['Milnor2004','ConradLevel'])
p(94,'Verify the final duplication normalization',[280,281],
 'The final formula is followed by Il reste à vérifier and OK.',
 'F_t=t((z²−2z+t)/(z²−2tz+t))² has the required invariant quotient and branch normalization.',
 'Closed on scan65. The symbolic identities, resultant and fixed-point computations are rerun in symbolic_checks.py. Intermediate sign and dropped-factor alarms do not invalidate the final map.',
 'The visible OK closes the question; it should not remain on an unresolved-problem list.',
 'Low research value; preserve the correction alarms for the next transcription pass.',['Milnor2004'])
p(95,'Make the tangential Kummer classification precise',[289,290,291,292],
 'Scans72–74 claim a categorical equivalence from pointed tame G-covers to listed data G,n,i,ξ,T,κ, with only ad hoc morphisms.',
 'At minimum i must be the actual tangent-inertia embedding of ξ, and morphisms must respect the induced power maps. A full general equivalence for a minimally repaired target is not claimed.',
 'The literal statement is refuted by the C2² example with every hypothesis checked (C-SA16-291, supplement §9, saved code/output). SGA1 XIII§2 gives tame framework; Stacks03PK gives the cyclic root groupoid. The quadratic special case is validated by AntieauMeierDef4.4/Prop4.5.',
 'No proof or explicit inertia compatibility is given. The text then specializes to μ2, where this particular obstruction disappears; it does not state why the broader claim was dropped.',
 'Highest mathematical value; a short run should first formulate exact categories and test full faithfulness before claiming a repaired theorem.',['SGA1','Stacks03PK','AntieauMeier2020'])
p(96,'Specify the standard square Q0',[297],
 'Scan76 promises Q0 to be described below, with diagonal torsor identified with μ4*.',
 'The continuation specifies rotations μ4 and a marked side with s_i′=i s_i; this determines the required reference data. The optional equation x⁴=−4 is a separate earlier-run realization.',
 'Closed at MPL_64_078-115_transcription.tex scan78 lines6–31, personally read. Our item297 links to the continuation owner’s SA16-501/C-SA16-501; the prior explicit realization is its SA16-502.',
 'A forward reference fulfilled immediately after this packet, not an abandoned construction.',
 'Low research value; carry the precise normalization into the later comparison.',['Stacks03PK'],extra=[{'file':'MPL_64_078-115_transcription.tex','scan':78,'start':6,'end':31}])
p(97,'State the dependence of pinning on orientation',[295,296,298,299],
 'Scans75–77 give a tangent-root pinning and two choices, initially with fixed J, and qualify the formulation when J varies.',
 'The square-root isomorphisms form a μ2-torsor once the orientation identification is included; global existence is not automatic. The subsequent level4 comparison has additional symmetric normalization data.',
 'C-SA16-295–298 proves the bundle and torsor identities. ConradLevelProp3.2 already gives a canonical map from suitable level4 data to ordinary Legendre structures; Remark2.8 excludes an ordinary S3 action. This does not settle the later exact symmetric normalization.',
 'The page records the relative qualification. The later open comparison is owned in the continuation dossier and must not be conflated with existence of any level4 construction.',
 'High connective value; first compare the two normalization conventions against continuation claims C-SA16-515 and C-SA16-535.',['ConradLevel','AntieauMeier2020','Stacks03PK','StacksProjectiveBundle'])

readings=[]
def r(scan,lo,hi,reading,alt,evidence,weight='high',confidence='high',item=None,part='a'):
 readings.append({'cote':64,'scan':scan,'line':f'MPL_64_{"002-039" if part=="a" else "040-077"}_transcription.tex:{lo}-{hi}',
  'reading':reading,'alternative':alt,'evidence':evidence,'weight':weight,'confidence':confidence,'item_id':f'SA16-{item}' if item else '', 'decision':'Unresolved on ink; no transcription changed.'})
r(6,137,142,'trois sous-groupes de Sylow','quatre','Eight3-cycles give four cyclic subgroups; scans4–5 explicitly say four.','high','high',214)
r(7,229,256,'cyclic order4 label for centralizer of a nonzero Klein element','D8 centralizer, with distinguished C4 inside','Exhaustive centralizer size8; both square roots lie in its C4.',item=216)
r(10,371,434,'plus in or beside D_ab label','plain D_ab, or separately defined plus subgroup','D_ab is C2²; no automatic plus operation is defined at this point.','medium','medium',218)
r(10,413,434,'index2 subgroups identified directly with quotient lines','inverse images of quotient lines','A quotient line has order2; its inverse image inD8 has order4.','medium','high',218)
r(11,439,494,'B|D and S|C in square table','retain local alternatives pending image','The diagonal and cyclic objects have different roles; notation alone does not determine the stroke.','medium','medium',219)
r(12,501,550,'ordered product varpi c d','retain or reverse only if composition convention warrants','Invariant character identity is sound; products of representatives can differ by central antipodism.','high','medium',220)
r(17,703,720,'relations only [x,x′]=1 and [x,y]=a','possible omitted order/central/opposite relations','Literal presentation maps ontoZ. Mathematical repair C-SA16-322 does not establish omitted ink.',item=222)
r(20,798,811,'cyclic centralizer label reappears','D8, or intended distinguished cyclic subgroup','Same order8 centralizer calculation as scan7.',item=216)
r(21,816,845,'V* described as a subgroup','V, with star removed','V* has three nonidentity elements and lacks identity, so is not a subgroup.',item=224)
r(24,894,925,'contracted wedge labeled F2^J-torsor','product is F2^J-torsor; wedge is F2-torsor','Cardinalities8 and2; independent contracted-product calculation.',item=228)
r(25,937,940,'Aut(Cube) without plus','Aut⁺(Cube) if rotations are intended','Full cube symmetry group has order48; the claimed S4 has order24.',item=229)
r(25,937,940,'face-diagonal stabilizers ne sont pas dans V','sont dans V, if that is the actual noun','The half-turn is a double transposition in the normal KleinV.',item=230)
r(27,991,996,'contraction indexed by M0^J','ker(Σ:M0^J→M0)','The zero-sum lift torsor has16 elements, not64.',item=232)
r(28,1119,1132,'kernel injection described through reduction as nontrivial linear map','u↦1+2ũ; its reduction is identity','All kernel elements reduce to1, so prose types cannot be correct literally.',item=234)
r(35,1448,1448,'On verra followed by illegible marginal words','no mathematical completion proposed','Adjacent formulas cannot determine the promise or its attachment.','high','low',250)
r(37,1581,1603,'extra prime on automorphism group in formula47','remove only if ink warrants','The projective action already quotients by±1; another quotient changes the group.','high','medium',247)
r(42,108,149,'Aut(V)≃G_J^- or decorated S with upper dash','Aut⁻ if a coset is intended; otherwise ordinary S_J','Aut(V) has6 elements; a minus coset would have3. Source doubt table retains ambiguity.','high','medium',259,'b')
r(42,108,149,'scalar line self-orthogonal without repeated ambient','withinW, not allEnd(V)','Perpendicular dimensions1 inW,3 inEnd(V); surrounding W discussion supports the restricted reading.','high','high',258,'b')
r(43,152,157,'sl(V)|gl(V) for trace kernel','sl(V)','Trace kernel has dimension3, while gl(V) has4.','high','high',233,'b')
r(47,208,219,'D3|D2 inserted as Klein group','D2 in the order4 convention','The displayed generators commute and have order2; no order6 group fits.','high','high',268,'b')
r(48,228,237,'bare Aut(Δ) étale S4 under only2 invertible','structured Aut(Δ,a), or additionally5 invertible','Characteristic5 gives120 automorphisms; mathematical hypothesis alarm, not evidence that ink included5.','high','high',263,'b')
r(51,287,303,'regular involution may omit sans point fixe','regular fixed-point-free opposition','An opposition is a three-pair partition; an involution fixing vertices is different data.','high','medium',268,'b')
r(52,308,320,'icosaédrale','octaédrale as mathematical alternative','There are six vertices, three axes and rotationalS4; icosahedral group would beA5.','medium','high',268,'b')
r(53,327,343,'Aut_X(Δ) in the structured correspondence','Aut_X(Δ,a), or5 invertible','Opposition is necessary at characteristic5.','high','high',267,'b')
r(53,333,343,'orientation insertion in Corollary2, attachment uncertain','canonical compatibility rather than an arbitrary extra choice','An independent choice would change automorphism groups and the asserted four-cover equivalence.','high','medium',267,'b')
r(54,348,360,'V* called Klein group','V, or underlying nonidentity labels only','Three nonidentity elements do not form a group.','high','high',271,'b')
r(56,389,402,'unstarred target Sigma in restricted-cover diagram','Sigma* if the arrow is asserted étale','The full quotient branches along the three marked points.','high','medium',260,'b')
r(60,496,525,'degree2 underbrace apparently on six-point target','attach degree2 to twelve-to-six quotient','PrimitiveE[4] has12 points, sign quotient6, each fiber2.','high','high',274,'b')
r(64,574,587,'t±sqrt(t(1−t))','t±sqrt(t(t−1))','Substitution into z²−2tz+t gives residual−2t(t−1) versus0.','high','high',279,'b')
r(64,591,622,'intermediate equality drops a factor','retain the preceding factor in that intermediate line','Symbolic expansion detects the mismatch; finalc_t=t remains correct.','medium','high',280,'b')
r(65,627,631,'unsquared ratio at1 reported as1','−1 at1 andt; +1 at0 and∞','Direct substitution; squaring leaves the final map correct.','medium','high',281,'b')
r(65,627,631,'scheme image of E[2^n] equated to full fiber','support/reduced image, or divisor pushforward q_*[E[m]]','Atm4 full fiber has length16 and support10; reduced image has length10.','high','high',282,'b')
r(66,638,658,'N|V_J in reference augmentation module','V_J if the repeated module notation is intended','Repeated scan67 definition and zero-sum kernel matchV; exact glyph remains visual.','medium','medium',283,'b')
r(68,690,709,'Trace without explicit type','sum of the J-indexed tuple, not matrix trace','The source is a tuple module and values lie inM0.','medium','high',285,'b')
r(73,783,804,'arbitrary mono i:μ_n→G independent ofξ','require actual tangent-inertia embedding ofξ','C2² counterexample refutes unrestricted target. No hidden ink condition is presumed.','high','high',291,'b')
r(74,806,811,'étales au dessus deX','X*=X∖t','Total ramification at t contradicts étaleness at t.','high','high',294,'b')
r(75,816,843,'punctured Sigma_J* called projective-line fibration','Sigma_J is projective; Sigma_J* is its open complement','Removing the trisection destroys properness.','medium','high',294,'b')
r(76,848,883,'μ4 versus primitive-root torsor in orientation formula','μ4* for the two-element orientation torsor','μ4 has four geometric elements, primitive roots two; scan78 specifies the diagonal torsor.','high','high',296,'b')
r(77,887,910,'two pinnings withJ varying and no repeatedα','include α:ω_J≃D_Q0','The text adds precisely this relative qualification; two means aμ2-torsor, not global sections.','high','high',298,'b')
(ROOT/'problems.json').write_text(json.dumps(problems,ensure_ascii=False,indent=2)+'\n')
with (ROOT/'readings.tsv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=list(readings[0]),delimiter='\t');w.writeheader();w.writerows(readings)
print(f'{len(problems)} problems; {len(readings)} mathematical reading alarms')
