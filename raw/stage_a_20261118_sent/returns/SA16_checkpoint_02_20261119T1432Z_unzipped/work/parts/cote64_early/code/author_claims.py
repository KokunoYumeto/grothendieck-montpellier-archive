"""Manually authored claim decisions; imports only previously authored statements.
No status, class or verdict is inferred by text matching or a computation.
"""
import json
from pathlib import Path
from author_records import items
from polish_prose import polish
ROOT=Path(__file__).resolve().parents[1]
I={int(x['id'].split('-')[-1]):x for x in items}
claims=[]
def c(n, ns, status, cls, fate, date, present, refs, confidence='high', computation='No numerical computation is required; see proof_supplement.md.', group='', statement=None, his=None, refinement=None):
    base=I[ns[0]]
    row={'id':f'C-SA16-{n}','items':[f'SA16-{j}' for j in ns],'cote':64,
      'scans':sorted(set(s for j in ns for s in I[j]['scans'])),
      'lines':[loc for j in ns for loc in I[j]['lines']],
      'his_statement':base['his_words'] if his is None else his,
      'statement':base['statement'] if statement is None else statement,
      'status_on_pages':status,'computation':computation,'class':cls,'fate':fate,
      'fate_date':date,'present_status':present,'refs':refs,'confidence':confidence,
      'literature_search_group':group,'as_of':'2026-11-19'}
    if refinement: row['refined_statement_id']=refinement
    claims.append(row)

c(211,[211,212],'corrected by himself later (same scan3, lines16–29)','E',
 'The corrected affine-plane/Klein statement is classical finite permutation-group theory. Burnside1897 §171 identifies automorphisms of elementary abelian groups with linear groups; the normal regular action here is its order4 instance. The exact torsor presentation is an exposition, not an identified new theorem.',
 'Known by1897; no manuscript composition date is inferred from the reused1982 circular.',
 'Correct with affine in place of vector-space and centralizer in place of normalizer. A choice of one point is needed for an origin.',
 ['Burnside1897'],computation='code/finite_groups.py → outputs/finite_groups.json: V4 regular; centralizer V4; normalizer S4. Proof supplement§1.',group='FINITE')
c(213,[213,214],'proof sketched; scan6 numeral conflicts with scan4–5 construction','E',
 'Burnside1897 §173 proves the symmetric group has no outer automorphisms except degree6; §142 gives the point-stabilizer reconstruction. The groupoid equivalence follows from this classical fact. Searches for the exact four-Sylow wording did not identify a separate later theorem.',
 '1897 publication; earlier Hölder1895 attribution was found secondarily but its original was not opened and is not used for priority.',
 'Correct for invertible morphisms. There are four Sylow3 subgroups; literal trois at scan6 is an unresolved reading alarm.',
 ['Burnside1897','SGA1'],computation='finite_groups.py:24 automorphisms of S4; four Sylow3 subgroups. All30 subgroups retained in s4_subgroups.json.',group='FINITE')
c(214,[214],'false as stated under the current uncertain reading','E',
 'The four Sylow3 subgroups are an elementary consequence of the eight3-cycles. Historical finite-group references and our exact enumeration contradict the numeral3; literature cannot decide the ink.',
 'Classical finite group calculation, present recheck2026-11-19.',
 'Literal reading false; refined reconstruction is C-SA16-213. No transcript edit made.',
 ['Burnside1897'],computation='finite_groups.py counts8 elements of order3 and4 generated subgroups.',group='FINITE',refinement='C-SA16-213')
c(215,[215],'proved there as a convention discussion','D',
 'Searches of finite-group literature, arXiv, MathOverflow and the relevant published descent sources did not locate this exact pair of natural orientation conventions as a named theorem. Both sign choices are immediate equivariant torsor identifications; lack of an exact hit is not a novelty claim.',
 'No separate historical development identified as of2026-11-19.',
 'Correct. A functorial identification exists in two sign variants, and the author chooses one. No open mathematical problem remains.',
 ['Burnside1897','SGA1'],computation='finite_groups.py verifies the associated sign characters; proof_supplement§1 records the two choices.',group='FINITE')
c(216,[216],'false as stated in the cyclic-centralizer label','E',
 'The centralizer calculation is classical. A double transposition in S4 has centralizer D8 of order8, while its square roots generate the unique C4 inside it. The erroneous label has no valid broader fate.',
 'Known before these notes; rechecked2026-11-19.',
 'Refuted with all hypotheses: x=(12)(34) belongs to the normal Klein group and its centralizer has8 elements. Replace the C4 label by D8, or change the operation to the appropriate cyclic subgroup.',
 ['Burnside1897'],computation='finite_groups.py enumerates all24 permutations and obtains centralizer size8 for each of the three nonzero Klein elements.',group='FINITE',refinement='C-SA16-306')
c(217,[217,223],'proof sketched through explicit constructions','E',
 'The underlying square, cycle and dihedral descriptions are classical (Burnside1897, dihedral presentation in §203). Transport of the finite constructions to torsors uses ordinary descent, for which SGA1 V4.1 and VIII2 are exact structural sources. No claim that SGA1 prints this five-model square dictionary is made.',
 'Finite group ingredients1897 or earlier; descent seminar1960–61, book1971.',
 'Correct as equivalences of groupoids. Relative versions require the same data as finite étale sheaves and follow by descent.',
 ['Burnside1897','SGA1'],computation='finite_groups.py standardD8 action; proof_supplement§2 gives the inverse product/incidence constructions.',group='FINITE')
c(220,[220,227],'proved there; initial verification closed on scans14 and25','E',
 'The invariant three-character relation is elementary D8 character theory. Literature searches found the ordinary dihedral structure, not an independent theorem under this notation. The torsor identity is proved locally and descends; the product of chosen representatives additionally depends on multiplication convention.',
 'Classical finite-group content; current convention audit2026-11-19.',
 'Correct invariant identity. The written ordered product is read using the author’s explicit convention; reversing order can change it by the central involution.',
 ['Burnside1897','SGA1'],computation='finite_groups.py: a concrete example has rcd=r² and dcr=1 under function composition; this illustrates order sensitivity without changing the manuscript convention.',group='FINITE')
c(221,[221],'proof sketched on scan17 after question on scan16','D',
 'The fact Aut(D8)≅D8 is elementary classical group theory, but the exact reflection-square equivalence was not located as a separately published theorem in the recorded square/groupoid searches. Our full-faithfulness argument settles the local question without making a priority claim.',
 'Exact packaging not located as of2026-11-19.',
 'Correct: the four noncentral involutions form a square and generateD8, making Aut(D8)→Aut(square) faithful of equal order8. Q↦Aut(Q) is a different, nonfaithful functor.',
 ['Burnside1897','SGA1'],computation='finite_groups.py counts8 automorphisms,4 inner automorphisms and4 noncentral involutions; proof_supplement§2.',group='FINITE')
c(222,[222],'false as a literal complete presentation','E',
 'Classical dihedral presentations include order relations; Burnside1897 §203 is a historical printed reference. Searching the exact commutator-only presentation gave no legitimate replacement theorem. The issue is incompleteness of the recorded relations.',
 'Classical corrected presentation; present literal-presentation refutation2026-11-19.',
 'The literal presented group surjects ontoZ by x↦1, a↦0, satisfying every written commutator relation. Add x²=a²=1, centrality ofa, and x′=ax for the intended D8. The repaired statement is C-SA16-322.',
 ['Burnside1897'],computation='No enumeration can prove a literal presentation finite; the explicitZ quotient refutes it. D8 enumeration verifies the repaired presentation.',group='FINITE',refinement='C-SA16-322')
c(224,[224,225],'proved there for counts; inclusion diagram left open','E',
 'S4 subgroup enumeration is part of classical permutation-group theory. Burnside1897 §146 treats low-degree transitive groups and §§142,173 the symmetric-group structure. The exact30-node diagram is supplied here as a finite certificate rather than attributed to that book.',
 'Classical classification before these notes; diagram completed2026-11-19.',
 'Correct counts:30 subgroups,11 conjugacy classes; order distribution1:1,2:9,3:4,4:7,6:4,8:3,12:1,24:1. The requested full Hasse diagram has66 edges.',
 ['Burnside1897'],computation='finite_groups.py → s4_subgroups.json and s4_hasse_edges.json (all sets and66 cover relations).',group='FINITE')
c(226,[226],'stated without full proof','E',
 'The two transitive six-point actions of S4 are the coset actions with stabilizers C4 and nonnormalV4. This is classical subgroup/coset theory; searches did not turn the distinction into an all-level modular theorem.',
 'Classical finite-group content; exact action characters rechecked2026-11-19.',
 'Both six-covers exist and are inequivalent as S4-sets. Their cube orientation characters differ; identifying them without changing the action is incorrect.',
 ['Burnside1897'],computation='finite_groups.py enumerates both six-sets, their fibers and action characters on all24 elements.',group='FINITE')
c(228,[228],'false as a torsor-group label','E',
 'The distinction between a product torsor and a contracted product is the standard torsor construction in SGA1 XI§4.1. The threefold product acts underF2³, while contraction along addition givesF2.',
 'SGA1 seminar/book1960–61/1971; no later resolution of the ink located.',
 'The wedge has two elements, not eight, so it cannot be a torsor underF2^J. Corrected statement: the Cartesian product has that action, the contracted product hasF2 action.',
 ['SGA1'],computation='finite_groups.py parity fibers; proof_supplement§2 gives the cardinality argument.',group='FINITE',refinement='C-SA16-328')
c(229,[229,249],'stated without all correspondences; explicit maps requested','E',
 'Classical cube rotations realizeS4 and their transitive sets are classified by stabilizers. Burnside1897 §§202–203 treats the polyhedral groups. The complete ten-feature dictionary is an elementary completion, not a new moduli theorem.',
 'Polyhedral-group description printed1897; explicit table rechecked2026-11-19.',
 'Correct after choosing rotation group Aut⁺(cube). All ten nontrivial transitive sets and stabilizers are supplied; the face-diagonal negation is isolated in C-SA16-230.',
 ['Burnside1897'],computation='cube_and_pgl.py → cube_and_pgl.json:24 signed-coordinate rotations and10 transitive feature sets with stabilizer orders/classes.',group='FINITE')
c(230,[230],'false as stated under the current reading','E',
 'The stabilizer class is a classical cube calculation. The actual half-turn is a double transposition inS4. No literature search can decide whether the negative word is a transcription or author error.',
 'Classical corrected fact; refuted2026-11-19.',
 'The stabilizer isC2 contained in the normal KleinV, contradicting ne sont pas dansV. Refined statement C-SA16-330.',
 ['Burnside1897'],computation='cube_and_pgl.py identifies the face-diagonal stabilizer permutation on four body diagonals as a double transposition.',group='FINITE',refinement='C-SA16-330')
c(231,[231,232,283,284],'proof sketched; contraction subscript ill-typed','B',
 'Brau–Jones2016 proof ofLemma3.1, equation26 and its invariant-plane table, gives the split mod4 matrix structure. It does not print the zero-sum lift-torsor model. The explicit symmetric augmentation module in the earlier notes provides a direct proof of this canonical presentation and its descent.',
 'Brau–Jones first arXiv2014-06-05, electronic2015-07-08, volume2016; exact canonical packaging not located elsewhere.',
 'Correct with P acted on by kerΣ. There are16 zero-sum lifts, naturally an End(M0)-torsor. The underlying additive extension ofM0 byM0 remains nonsplit.',
 ['BrauJones2016','SGA1'],computation='finite_groups.py enumerates64 lift triples/16 zero-sum triples and verifies the reference r_j vectors and basis determinants.',group='MOD4')
c(233,[233,258,259],'proved/sketched twice, scans27–28 and42–43','B',
 'Brau–Jones2016, proof ofLemma3.1 after equation26, explicitly lists the two invariant planes inM2(F2). Their table matchesA andW. The canonical identification with the orientation permutation module and the trace description are checked directly here; no blanket commutativity is in Grothendieck’s text.',
 'First circulation2014-06-05; electronic publication2015-07-08; volume2016.',
 'Correct. A⊕W=End(V), W≅F4, sl(V)=A⊕F2id, and W’s trace extension is nonsplit. The scalar line is self-orthogonal only withinW.',
 ['BrauJones2016'],computation='finite_groups.py checks all16 matrices, conjugation by6 elements, orthogonality, multiplication inW and invariant line{0,id}.',group='MOD4')
c(234,[234],'correct formula with ill-typed explanatory prose','B',
 'Brau–Jones equation26 and Detinko–Flannery–HulpkeLemma2.6 give the standard congruence-kernel formulas. The latter explicitly gives the trace-zero kernel forSL and additive multiplication.',
 'Brau–Jones2014/2016; Detinko–Flannery–Hulpke preprint2016, publication2018 (opened later revision2022).',
 'Correct mathematical map u↦1+2ũ; reduction of its image is1. The conflicting description of its composite with reduction remains a reading/typing alarm.',
 ['BrauJones2016','DetinkoFlanneryHulpke2018'],computation='finite_groups.py checks all16 kernel matrices; (1+2u)(1+2v)=1+2(u+v) mod4.',group='MOD4')
c(235,[235,236],'proof sketched via semidirect product and quotient torsors','C',
 'The abstract split group and invariant-plane ingredients are explicit in Brau–Jones2016. The exact canonical equivalence M↔(I,Q,k) and its relative descent were not located in the recorded searches. They are proved here from the natural action, with no claim of historical priority.',
 'Published ingredients2016; exact package not located as of2026-11-19.',
 'Correct. The natural action has96 distinct elements and equals S4×_{C2}D8 with the codiagonal character. The groupoid equivalence descends étale locally.',
 ['BrauJones2016','SGA1'],computation='finite_groups.py verifies I,Q cardinalities4,4; natural action image96; quotient kernels and codiagonal character.',group='MOD4')
c(237,[237],'stated without detailed computation','B',
 'The full mod4 group structure is given by Brau–Jones2016 equation26 and invariant subspaces; this determines the derived groups. Searches located modern congruence-group work but no exact earlier first publication of both abelianizations. The identities themselves are independently certified.',
 'Explicit published mod4 ingredients2016; earliest occurrence of the paired abelianization formulas not established.',
 'Correct: GLab=C2², SLab=C4, derived orders24 and12, centers{±I}; the order12 derived subgroup ofSL isA4.',
 ['BrauJones2016','DetinkoFlanneryHulpke2018'],computation='finite_groups.py computes every commutator and generated subgroup, centers, coset sizes and exponent of each quotient.',group='MOD4')
c(238,[238],'stated with choice-dependent product descriptions','C',
 'The matrix-kernel and invariant-subspace components occur in Brau–Jones2016. Searches for the exact five cartesian squares in the author’s geometric notation did not locate them. Each square is checked as a concrete subgroup intersection in this run.',
 'Related published components2016; exact diagram package not located as of2026-11-19.',
 'All five squares are correct with the indicated trivialization choice. No canonical additive orSL splitting is inferred.',
 ['BrauJones2016'],computation='finite_groups.py: subgroup_intersections_verified=5, with every group listed from its explicit predicate.',group='MOD4')
c(239,[239],'the GL splitting is sketched; the SL distinction is a labelled implication','B',
 'Brau–Jones equation26 constructs an integralS3 complement. The MathOverflow2023 discussion directs to Detinko–Flannery–Hulpke; their currentTheorem2.5 concerns proper supplements, not necessarily complements, so it must not be quoted as the exact nonsplitting theorem. Our direct involution calculation proves theSL assertion.',
 'GL complement first circulated2014 in the cited paper; MathOverflow discussion2023; historical firstSL nonsplitting not identified.',
 'GL reduction splits. SL reduction does not: an order2 element ofSL2(Z/4) has trivial reduction, whileS3 contains transpositions. Proper supplements inSL are compatible with this.',
 ['BrauJones2016','DetinkoFlanneryHulpke2018','MO443624'],computation='finite_groups.py constructs an order6 complement inGL and checks every square-one element ofSL reduces to1.',group='MOD4')
c(240,[240,247],'proof sketched; redundant prime reading in later formula47','B',
 'The projective mod4 group is a48-element octahedral group. A MathOverflow2017 answer explicitly correctsGL versusPGL in this identification; Brau–Jones supplies its matrix decomposition. Exact canonical vertex/edge/face packaging is checked here.',
 'Related explicit mod4 structure2014/2016; cited projective identification discussed2017.',
 'Correct quotient GL/{±I}=Aut_oct(Δ) of order48. The extra prime at scan37 is not needed and, if it means another central quotient, is false.',
 ['BrauJones2016','MO275292'],computation='finite_groups.py:12 primitive vectors,6 sign classes, kernel{±I}, projective image48,8 faces.',group='MOD4')
c(241,[241,286,287],'proof sketched, repeated in relative notation','C',
 'The finite action follows from publishedGL2(Z/4) structure; Conrad’s level-structure notes§3 distinguish actual frames and isomorphisms of marked elliptic curves. Searches did not locate this preciseP_M/± face-torsor presentation in independent literature.',
 'Published matrix ingredients2016; Conrad handout undated; exact canonical presentation not located as of2026-11-19.',
 'Correct two-element fiber. Negating both basis vectors preserves the Weil pairing but changes the frame; it is absorbed by[−1] as an isomorphism of marked elliptic curves.',
 ['BrauJones2016','ConradLevel'],computation='finite_groups.py:16 P-points,8 faces,each fiber2; det(−I)=1. Proof supplement§4 distinguishes groupoid objects.',group='MOD4')
c(242,[242],'stated with character computations','B',
 'Brau–Jones’s split description separates determinant and mod2 sign. The particular geometric labels ω,Or,C are manuscript-specific; the finite character comparison in this run checks all labels rather than importing them from the literature.',
 'Published matrix components2016; precise geometric labeling rechecked2026-11-19.',
 'Correct: the three nontrivial characters are sign,determinant and their product, with the manuscript’s indicated torsors.',
 ['BrauJones2016'],computation='finite_groups.py verifies all96 character values on the square/cube/permutation actions.',group='MOD4')
c(243,[243],'construction stated to work','D',
 'Searches for the exact orientation-twist operation in this finite octahedral setting found no separate later theorem. It is a formal contracted-product construction using the orientation character and antipodism; the descent formalism is standard inSGA1.',
 'No exact separate development located as of2026-11-19.',
 'Correct: the orientation torsor of the twisted object is canonically trivial. The original object has not been given a chosen orientation.',
 ['SGA1'],computation='proof_supplement§4 applies the product of the orientation character with itself, giving the trivial character.',group='MOD4')
c(244,[244,248],'open on the pages; reduced to square lifting on scan38','C',
 'Central lifting is standard obstruction theory. The exactD8 factor set is thecup product; Merkurjev–Scavia2024 Example1.4 states the general unipotent lifting/cup equivalence, andU3(F2)=D8. Their field interpretation is not the entire relative geometric dictionary; that dictionary is supplied here by the manuscript reduction and descent.',
 'General obstruction theory predates the notes; opened precise modern statementJuly2024. Earliest printed version of this exact octahedral application not found.',
 'The finite lifting question is mathematically resolved by C-SA16-245. A given projective torsor lifts iff its associated two-character cup obstruction vanishes; the universal extension remains nonsplit.',
 ['MerkurjevScavia2024','SGA1'],computation='finite_groups.py factor-set certificate on16 pairs; proof_supplement§5 explains the obstruction and torsor of lifts.',group='LIFTING')
c(245,[245],'not stated on the pages; earlier-run reconstruction of the open step','B',
 'Merkurjev–Scavia2024 Example1.4 identifies the obstruction to lifting a pair ofF_p characters toU3 with their cup product;§2.1 treatsp=2. General torsor descent gives the same central obstruction on a site. Ledet2001 was located bibliographically, but its cited§0.4 was not accessible and is not used as a checked exact result.',
 'Opened modern exact resultJuly2024; earlier classical origin not dated from memory.',
 'Correct for a site/topos with the usual abelianH² obstruction theory: obstruction c∪d; when zero, the groupoid of lifts is a torsor underF2-torsors. A fixed lift has automorphismsH0(F2).',
 ['MerkurjevScavia2024','SGA1','Ledet2001'],computation='finite_groups.py computes theD8 section factor set c(g)d(h) on all16 pairs. proof_supplement§5 is an independent cocycle derivation.',group='LIFTING')
c(246,[246],'not asserted on the pages; earlier-run implication','B',
 'The projective central extension is determined by the finite mod4 group structure. The nonsplitting criterion is an elementary restriction to a cyclic subgroup; it is compatible with the general obstruction framework and does not require a global arithmetic hypothesis.',
 'Modern matrix structure explicitly published2016; this certificate rechecked2026-11-19.',
 'Correct. Both lifts of the relevant projective involution have order4, so there is no homomorphic section of the central extension.',
 ['BrauJones2016','MerkurjevScavia2024'],computation='finite_groups.py verifies T²=−I forT=(0,3;1,0), and(−T)²=−I.',group='LIFTING')
c(250,[250],'open/uncertain wording, not a determinate mathematical statement','F',
 'The nearby face-torsor and character results were searched withMOD4/LIFTING. No title or theorem search can recover the illegible words or decide the attachment ofOn verra; a precise conjecture is not identifiable from this transcription.',
 'Unresolved reading as of2026-11-19.',
 'ClassF concerns only the uncertain marginal promise, not the proved surrounding face construction. It remains inStage4 for an image check.',
 [],confidence='low',computation='No computation would determine the ink.',group='MOD4')

c(260,[260,272],'proof sketched; constancy hypothesis explicitly removed','E',
 'The identities are ordinary twisting by an exponent2 group. SGA1 XI§4.1 gives the contracted-product framework; the specific cubic/Klein reference construction is not a separately identified later theorem. The searched literature does not justify replacing a prescribed monodromy identification by geometric connectedness.',
 'General descent/torsor framework1960–61/1971; exact normalization rechecked2026-11-19.',
 'Correct: I=K∧F_t and K=I∧F_t, withoutI constant. Admissibility retains the identity marking ofV_J; six possibleGL2(F2) identifications are not one marked cover.',
 ['SGA1'],computation='proof_supplement§7 gives the cocycle identity and the inverse twist; finite_groups.py verifies |GL2(F2)|=6.',group='TWISTS')
c(261,[261],'proof sketched in local coordinates','C',
 'Beauville2010 gives the finitePGL2 field classification under its prime-to-characteristic convention. Hua2026 §42 explicitly leaves the relative normal form unproved. The present proof supplies the relative étale-local diagonalization and square-root normalization; it does not claim a prior published relative proof was found.',
 'Beauville first arXiv2009-09-22, book chapter2010; Hua preprintNovember2026.',
 'Correct for fiberwise faithful Klein subgroup schemes and2 invertible, on étale forms ofP1. Characteristic3 is included; applying Beauville’s prime-to-charS4 theorem there would be invalid.',
 ['Beauville2010','Hua2026','SGA1'],computation='cube_and_pgl.py checks axes and actions inF9,F5,F13,F17; proof_supplement§6 supplies the relative proof, which is not inferred from finitely many fields.',group='OCTAHEDRAL')
c(262,[262],'proof sketched; direct extension requested locally','C',
 'Beauville2010 Thm4.2 proof gives the field normalizer generators. Hua2026 §42 records the remaining relative correspondence as not proved there. This run verifies the explicit group and its étale descent, includingchar3 andchar5 with opposition retained.',
 'Field account2009/2010; relative theorem still listed as unproved in the openedNovember2026 preprint.',
 'Correct structured normalizer of rank24 overZ[1/2]. It is anS4-form, with rational sections depending on the base; it need not be a constant subgroup ofPGL2(S).',
 ['Beauville2010','Hua2026','SGA1'],computation='cube_and_pgl.py: structured stabilizer24 in all four tested fields; proof_supplement§6 constructs24 distinct transformations étale locally and rules out extra structured ones.',group='OCTAHEDRAL')
c(263,[263,264],'false as stated; rejected intermediate arithmetic does not retract conclusion','B',
 'Hua2026 §42 Thm42.1 and Counterexample42.2 explicitly prove the5(a−1) identity and the characteristic5 exception over fields. The manuscript’s universal bare-divisor equality and uniqueness are therefore not valid; the relative correction is separated in C-SA16-363.',
 'Opened primary reconstruction/preprintNovember2026; prior attached notes already creditHua, and no earlier priority is asserted.',
 'Refuted overS=SpecF5,2 invertible,i=2: Δ=P1(F5), full stabilizer120, structured stabilizer24, nontrivial fixerz↦2z+1. There are five regular oppositions, so forgetting opposition is not faithful to the stated classification.',
 ['Hua2026','Beauville2010'],computation='cube_and_pgl.py enumerates PGL2(F5), all15 opposite-pair partitions, and the witness;5 stabilizers24,10 stabilizers12. No Lean source compiled.',group='OCTAHEDRAL',refinement='C-SA16-363')
c(265,[265,266],'proof sketched; one extension step explicitly requested','C',
 'The field ingredients are inBeauville2010. Hua2026 §42 prints the relative statement but labels it unproved and notes the uncertain orientation insertion. Our exact refinement retains opposition and uses its tangent-multiplier orientation; it is not a report that an unconditional published theorem already matches every word.',
 'Beauville2009/2010; HuaNovember2026; exact relative refinement proved in this run2026-11-19.',
 'Correct with the stated regular fixed-point-free opposition. Its axes, normalKlein and structured direct group are mutually inverse after étale localization; orientation is canonicallyμ4*.',
 ['Beauville2010','Hua2026','SGA1'],computation='proof_supplement§6 supplies inverse constructions and tangent multipliers; cube_and_pgl.py verifies the standard configuration.',group='OCTAHEDRAL')
c(267,[267,268],'stated without proof; orientation insertion has uncertain attachment','C',
 'Forms classified by torsors are standard descent (SGA1), andBeauvilleProp1.1 discusses field rationality restrictions. Hua2026 §42 does not prove this relative corollary. The present proof uses the constant signed-permutationS4 on the reference conic and distinguishes the compulsory orientation compatibility from an extra arbitrary choice.',
 'Descent framework1971; Beauville2010; corollary left unproved inHuaNovember2026.',
 'Correct for structured conics with the canonical orientation compatibility. An independently chosen second orientation isomorphism would alter the category and is not silently supplied. SplitP1_R and the anisotropic reference conic have different rational normalizers.',
 ['SGA1','Beauville2010','Hua2026'],computation='proof_supplement§6: signed permutation action, quartic trace-zero quadratic model, eight real normalizer points on splitP1; finite counts checked in cube_and_pgl.py.',group='OCTAHEDRAL')
c(269,[269],'construction sketched in margins','C',
 'The construction follows standard finite étale-algebra descent, but no exact published cubic trace-conic/square quotient with these markings was located in the recorded Numdam, arXiv and Grothendieck bibliography searches. Its local model is elementary and supplies a complete proof over arbitrary bases with2 invertible.',
 'Exact packaging not located as of2026-11-19; general descent predates the notes.',
 'Correct, includingcharacteristic3. Tr(1)=0 in characteristic3 does not make the trace map or trace pairing degenerate.',
 ['SGA1','Beauville2010'],computation='proof_supplement§7 splitsA locally asO³, checks the gradient2y_i and coordinate-square quotient of degree4; no unsupported finite-field extrapolation.',group='TWISTS')
c(270,[270],'not written in this normalized form; earlier-run comparison','E',
 'The fixed field of the standardKlein action is a classical rational invariant. Searches in the finitePGL2 and quotient literature located the normal form; the particular affine normalizationg2=(2−q)/4 is an immediate identity, independently checked here.',
 'Classical invariant theory; exact normalization rechecked2026-11-19.',
 'Correct local identity with2 invertible. The cited cote142/146 project endpoints remain unavailable, so only the algebraic identity is established.',
 ['Beauville2010'],computation='symbolic_checks.py verifiesg2=(2−q)/4; proof_supplement§7 identifies the three branch pairs.',group='TWISTS')
c(271,[271],'proposition stated; later formulas supply proof','E',
 'The Klein subgroup of the anharmonic action on four points is classical; finitePGL2 literature and the Legendre quotient discussion inConrad’s handout supply matching context. The unique extension of the three double transpositions is explicitly proved here with the manuscript formulas.',
 'Classical four-point geometry; opened modern referencesBeauville2010 and undatedConrad handout.',
 'Correct for disjoint four sections after étale localization, witht andt−1 units. It says only the canonicalV4 extends, not everyS4 permutation.',
 ['Beauville2010','ConradLevel','SGA1'],computation='symbolic_checks.py verifies involutions, productσ0σ1=σ∞ and invariance ofF_t; proof_supplement§7 gives determinants and descent.',group='TWISTS')
c(273,[273,276],'proof sketched with explicit local origin formulas','E',
 'This is the standard classification by twisting a fixed object through its automorphism sheaf, here translations byE0[2]. SGA1 gives the descent framework; searches for an independent exact fixed-locus formulation did not establish a separate first-publication date. The origin-change proof is provided directly.',
 'Twisting/descent established before these notes; exact formulation’s earliest print not identified.',
 'Correct with2 invertible: fixed locusI is anE0[2]-torsor, E=I∧E0, andE/E0[2]→E0 isx↦2x−a. The later specializationE=E0 is a simplifying hypothesis.',
 ['SGA1','ConradLevel'],computation='proof_supplement§7 checks x′=x−b,a′=a−2b and invariance of2x−a, plus the fixed-locus/twist inverse.',group='TWISTS')
c(274,[274,240],'the degree2 label is misplaced under the present reading','E',
 'The standard degree of[m] on an elliptic curve is treated inConrad’s handout§1; for4 invertible, E[4] has16 points. The primitive subset has12 and its sign quotient six. These classical counts determine which arrow has degree2.',
 'Classical elliptic isogeny theory; opened sourceConradLevel (undated).',
 'The cardinality computation is correct; the degree2 underbrace cannot describe the six-point target. Image check needed for placement, not a new mathematical conjecture.',
 ['ConradLevel'],computation='finite_groups.py primitive-vector count12 and sign-quotient count6.',group='TWISTS')
c(275,[275],'open on the pages as a requested verification','C',
 'SGA1 provides descent and tame local models, but no exact independent theorem matching this labelled almost-cartesian square was located. The normalization of the local node and the torsor reconstruction prove the intended qualified assertion; a literal cartesian replacement is false at the branch.',
 'Standard normalization/tame ingredients predate the notes; exact diagram verification2026-11-19.',
 'Resolved geometrically with its qualifier: cartesian off the branch divisor; a geometric local model v²=u² has two smooth branches after normalization. Over a nonnormal base the precise relative statement should use the canonical smooth branch model, not an unqualified absolute-normalization assertion.',
 ['SGA1'],computation='proof_supplement§7 proves the local normalization and explains branch/torsor compatibility.',group='TWISTS')
c(277,[277,278],'open request on scan63; coordinate solution follows on64–65','E',
 'Elliptic multiplication descended to the quotient is the classicalLattès construction; Milnor2004 Thm3.1 gives a precise complex statement. The intrinsic finiteKlein quotient also works algebraically when2 is invertible and is proved directly here. The literature does not supply this author’s target labelling automatically.',
 'Classical complex construction byLattès1918 (original sought); Milnor circulated2004, later publication2006.',
 'Resolved: quotient the canonicalKlein group ofJ∪{t}, then identify the three branch labels withJ. Degree4 and multiplicity constraints, not just four point values, provide uniqueness.',
 ['Milnor2004','ConradLevel'],computation='symbolic_checks.py proves the coordinate map invariant with coprime numerator/denominator; proof_supplement§8 gives the quotient argument.',group='DOUBLING')
c(279,[279],'false as the written radical','E',
 'The roots are determined by the displayed Möbius fixed-point quadratic; no later theory is needed. The nearby duplication/Lattès literature agrees with the corrected quadratic but cannot decide the ink.',
 'Elementary algebra; present refutation2026-11-19.',
 'With2,t,t−1 invertible, the written radical has residual−2t(t−1) and is false. Correct roots aret±√(t(t−1)); refinementC-SA16-379.',
 ['Milnor2004'],computation='symbolic_checks.py substitutes both radicals intoz²−2tz+t, returning−2t(t−1) and0.',group='DOUBLING',refinement='C-SA16-379')
c(280,[280,281],'coordinate proof and final check; OK closes it','E',
 'This is a normalized duplication map, within classical elliptic addition/Lattès theory. Milnor2004 supplies the exact quotient-by-multiplication framework overC; our universal polynomial proof handles the written formula overZ[1/2,t,1/(t(t−1))]. No historical first occurrence of this particular coordinate normalization is claimed.',
 'Classical duplication; opened modernLattès account circulated2004, publication2006.',
 'Correct final formula withc_t=t. The intermediate ratio atz=1 is−1, and a preceding equality drops a factor; both are local arithmetic/reading alarms that do not change the final rational map.',
 ['Milnor2004','ConradLevel'],computation='symbolic_checks.py: all three invariances, resultant4t(t−1)², tA²−B²=(t−1)(z²−t)², four marked values and normalization.',group='DOUBLING')
c(282,[282],'iteration stated; scheme-image equality false if read scheme-theoretically','E',
 'Iteration of a quotient of multiplication is classicalLattès theory (MilnorThm3.1 and local-degree equation3). The reduced-image/full-fiber distinction is an immediate ramification consequence, not an all-level representation theorem. No exact earlier publication of the manuscript’s ambiguous sentence was identified.',
 'Classical complex iteration; current exact multiplicity check2026-11-19.',
 'Iteration is correct. A full fiber has multiplicities1 at four2-torsion images and2 elsewhere; for m=4 it has degree16 and ten support points. The reduced scheme-image reading is refined inC-SA16-382.',
 ['Milnor2004','ConradLevel'],computation='symbolic_checks.py exact homogeneous second-iterate factorization at t=2, degree16/support10; proof_supplement§8 proves the formula for allm=2^n.',group='DOUBLING',refinement='C-SA16-382')
c(286,[286,283,285],'proof sketched as relative torsor formulas','C',
 'Brau–Jones supplies the matrix group andConrad§3 discusses full level structures. No exact independent occurrence of the symmetric zero-sum reference module with this trace notation was located. The explicit3e_j−Σe_k model proves the claimed relative torsor description and base-change compatibility.',
 'Published group ingredients2016; exact reference model rechecked2026-11-19.',
 'Correct: aJ-labeling and a zero-sum lift give a basis;16 lifts times six labelings gives96 frames. The trace here is addition overJ, not matrix trace.',
 ['BrauJones2016','ConradLevel','SGA1'],computation='finite_groups.py reference vectors/basis determinant,16 P-values,96 group elements; proof_supplement§4.',group='MOD4')
c(289,[289],'construction stated without full proof','E',
 'The determinant norm is standard (StacksTag0BD2, Lemma31.18.6). SGA1 XIII§2 supplies the tameKummer setting. The exact sign comparison between norm and leading jet is our independent local calculation; neither reference is quoted as silently fixing the author’s tangent convention.',
 'Tame covering theory publishedSGA1 in1971; current norm reference accessed2026-11-19.',
 'Correct once the chosen norm normalization is retained. Inx=u y^n, determinant norm givesN(y)=(−1)^{n−1}x/u; leading-jet and norm tangent maps differ by that sign.',
 ['SGA1','Stacks0BD2'],computation='symbolic_checks.py computes multiplication-matrix determinants for n=2,…,8; proof_supplement§9 proves the general companion-matrix determinant.',group='KUMMER')
c(290,[290],'stated with local construction','E',
 'Tame inertia is cyclic and identified by the tangent character in theKummer local form; SGA1 XIII§2 is the relevant published framework. The injection is part of the pointed cover, which is precisely why it cannot be independently chosen in the later abstract target.',
 'Tame local theory publishedSGA1 in1971; exact matching of the displayed injection checked2026-11-19.',
 'Correct under the page’s tame local hypotheses and group action extending toX′. The tangent character is faithful and its image isμ_n.',
 ['SGA1'],computation='proof_supplement§9 checks y↦ζy on the local parameter and the exact stabilizer.',group='KUMMER')
c(291,[291],'false as the unrestricted listed category equivalence','C',
 'SGA1’s tame-cover results and StacksKummer theory include actual ramification/action data; they do not assert this unrestricted target equivalence. Recorded searches for a tangent-root classification found the validμ2 special case in modernLegendre descriptions, not a theorem allowing arbitraryi independent ofξ.',
 'SGA1 publication1971; Antieau–Meier firstarXiv2016-08-02, journal2020; current counterexample rechecked2026-11-19.',
 'Refuted by the specifiedC2² cover overC: all smoothness, finiteness, torsor-away-from0 and tame-index2 hypotheses hold, but actual inertia is the first factor and listedi may be the second. A compatible-inertia refinement is C-SA16-391; its full general categorical formulation still requires explicit morphisms.',
 ['SGA1','Stacks03PK','AntieauMeier2020'],computation='code/kummer_counterexample.py → outputs/kummer_counterexample.json; proof_supplement§9 checks every scheme-theoretic hypothesis, not just the finite permutation.',group='KUMMER',refinement='C-SA16-391')
c(292,[292],'uniqueness stated; rigidification must be specified','E',
 'Stacks03PK equation59.28.4.1 explicitly describes the isomorphism set of root pairs as aμ_n-torsor when nonempty. That is the exact obstruction to treating a bare root object as uniquely isomorphic. Full tangent comparison can rigidify it.',
 'ClassicalKummer theory; opened current exact root-groupoid formula2026-11-19.',
 'Retain uniqueness only for the full structured comparison with compatible morphisms. An unrigidified root hasμ_n automorphisms; a chosen square root does not make the groupoid discrete.',
 ['Stacks03PK'],computation='proof_supplement§9: scalarζ acts onT and preservesT^n precisely whenζ^n=1.',group='KUMMER')
c(293,[293],'stated without complete relative proof','B',
 'Antieau–Meier2020 Def4.4, Prop4.5 andLemma4.7 identify the usualLegendre atlas as a square-root torsor andM(2) asBμ2 over the parameter line. This verifies the quadratic-twist mechanism; descent across permutations gives the unlabelledJ form, whose tangent convention is explicitly checked here.',
 'FirstarXiv2016-08-02; journal2020; openedarXivv3 dated2020-05-05.',
 'Correct for2 invertible as a groupoid of(J,t,T,T²≅TΣ,t), with the stated norm/jet convention. The broader arbitraryG counterexample does not refute this special case.',
 ['AntieauMeier2020','Stacks03PK','ConradLevel'],computation='proof_supplement§9 constructs the local four-branch double cover, tracksμ2 scalars and descends; no numerical certificate substitutes for descent.',group='KUMMER')
c(295,[295],'stated canonical isomorphism','E',
 'The relative tangent bundle follows from the tautological projective-bundle sequence. Stacks01OA supplies the quotient convention; EGAII section4.2 is the historical comparison, with its exact reading status recorded in reference_audit.tsv. The sign-line tangent formula is independently derived here.',
 'EGAII publication1961; current specific orientation computation2026-11-19.',
 'Correct: TΣ=O(2)⊗orientation(J). Either line/quotient convention dualizes the determinant, harmless for this self-dual sign line.',
 ['EGAII','StacksProjectiveBundle'],computation='proof_supplement§10 derives Hom(L,W/L)=L^−2⊗detW and computesdetW=sign(J).',group='PINNING')
c(296,[296,299],'construction and square calculation stated','C',
 'Kummer root torsors are standard (Stacks03PK); Antieau–Meier treats the usualLegendre square root but not this exactμ4 normalization. Hua2026 §42 explicitly lists that symmetric strictification as not established there. The local twist power identity is proved in this run, without claiming the later full moduli action has been settled here.',
 'UsualLegendre root description circulated2016/published2020; Hua preprintNovember2026 distinguishes the missingμ4 refinement.',
 'Correct local/relative twist: squaring aμ4-character factors throughμ2 and insertsD(Q0). WithD(Q0)≅ω_J one gets the required tangent root;κ changes sign under[−1].',
 ['Stacks03PK','AntieauMeier2020','Hua2026'],computation='proof_supplement§10 checks character powers and the sign action. The later erroneous tensor-power formula atscan80 is handled by the continuation owner.',group='PINNING')
c(297,[297],'open promise atscan76, fulfilled atscan78 (attached continuation)','C',
 'The root-torsor mechanism is standard, but the specific standard-square normalization is the manuscript’s additional choice. Hua2026 §42 andAntieau–Meier do not give this exact normalization as a completed independent result. Both manuscript endpoints were read in this run.',
 'Local closure in manuscript scan78; external exact historical development not located as of2026-11-19.',
 'The promisedQ0 is defined byμ4≅Aut⁺Q0 and a chosen side with endpoints indexed byμ4*, satisfying s_i′=i s_i; thenD_Q0≅μ4*. This is not the coordinate equationx⁴=−4, which belongs to an earlier-run realization.',
 ['Stacks03PK','Hua2026'],computation='proof_supplement§10 checks the four vertices, opposite pairs and side relation; later endpointMPL_64_078-115_transcription.tex lines6–31.',group='PINNING')
c(298,[298],'stated, first over algebraically closed field then with relative qualification','B',
 'Stacks03PK equation59.28.4.1 gives exactly the torsor of compatible root isomorphisms. Antieau–Meier’sLegendre atlas andConrad’sLegendre structure explain the same twofold rigidification with different normalization choices.',
 'Kummer backgroundclassical; Antieau–Meier2016/2020; openedcurrentStacks formula2026-11-19.',
 'Correct as aμ2-torsor, geometrically two elements; no global section is guaranteed over an arbitrary base. VaryingJ requiresα:ω_J≅D_Q0 as the page says.',
 ['Stacks03PK','AntieauMeier2020','ConradLevel'],computation='proof_supplement§10 shows two compatibleκ differ by a unit withsquare1; with2 invertible this is the finiteétaleμ2-torsor.',group='PINNING')

# Additional explicit computations/definitions in the transcriptions, not separate
# note headings; each has been read, given a status, and included in a search family.
c(305,[213,224],'proved there by enumeration','E',
 'The cycle-type classification and counts are classical permutation theory, already in nineteenth-century finite-group treatments. The current certificate checks every element rather than quoting a table from memory.',
 'Classical by1897; rechecked2026-11-19.',
 'Correct counts inS4: identity1; double transpositions3;3-cycles8; transpositions6;4-cycles6. Squaring4-cycles maps two-to-one onto the nonzero normalKlein elements.',
 ['Burnside1897'],computation='finite_groups.py exhausts24 permutations; proof_supplement§1 records count and square-map checks.',group='FINITE',
 statement='The scan6 cycle-type partition ofS4 and scan7 square map have counts1,3,8,6,6, with six4-cycles mapping two-to-one to the three nontrivial elements ofV.',his='éléments d’ordre3; éléments d’ordre4; leurs carrés')
c(306,[216,217,218,219],'proved/sketched in the square discussion; refines the false centralizer label','E',
 'Burnside1897 §203 supplies thedihedral relations. All relevant subgroup/character facts follow fromr⁴=s²=1,srs=r⁻¹ and are verified independently. This is the precise classical correction used forC-SA16-216.',
 'Printedclassicaldihedral presentation1897.',
 'D8 center=derived subgroup=⟨r²⟩; its abelianization isC2², its rotation subgroupC4, and it has two furtherindex2 Klein subgroups. The centralizer inS4 ofr² isD8.',
 ['Burnside1897'],computation='finite_groups.pyD8 enumeration andS4 centralizers; proof_supplement§2.',group='FINITE',
 statement='For a squareQ with antipodisma, AutQ≅D8, Z(D8)=[D8,D8]=⟨a⟩, D8ab≅C2², and the three nonzero quotient characters correspond to orientation,diagonal,codiagonal data.',his='centre; abélianisé; sous-groupes d’indice2')
c(322,[222],'current refinement of incomplete recorded presentation','E',
 'Equivalent to theclassicaldihedral presentation inBurnside§203; no new theorem is asserted.',
 'Classical; correctionrecorded2026-11-19.',
 'The repaired relations imply that every word has form a^εx^ηy^θ for two adjacent reflectionsx,y; they generate an8-element quotient realized by the standard square, hence exactlyD8.',
 ['Burnside1897'],computation='proof_supplement§2 gives the normal forms and matrix realization; finite_groups.py checks all8 elements.',group='FINITE',
 statement='Add a²=x²=1, a central, x′=ax for each opposite pair, and[x,y]=a for adjacent reflections. This presentation yieldsD8.',his='No additional words supplied: this is a labelled repair ofscan17.')
c(328,[228],'current refinement of the torsor-group label','E',
 'This is the contracted-product construction ofSGA1XI§4.1 specialized toC2.',
 'Classicaldescentpublished1971.',
 'Correct for arbitraryC2-torsors on a site: theproduct is aC2³-torsor; pushout bysum:C2³→C2 is thecontracted product.',
 ['SGA1'],computation='proof_supplement§2 computes quotient by thefour-elementsum-zero kernel.',group='FINITE',
 statement='For threeC2-torsorsL_j, ∏L_j is aC2^J-torsor and∧L_j is aC2-torsor.',his='No new manuscript quote: explicit mathematical correction.')
c(330,[230],'current refinement of the false negation','E',
 'Thecorrectedstabilizer is elementary cube/S4 theory; Burnside§§202–203 supplies the historical rotation-group identification.',
 'Classical; exactcertificate2026-11-19.',
 'A face diagonal has a two-element rotationalstabilizer generated by a double transposition; it lies inV.',
 ['Burnside1897'],computation='cube_and_pgl.py verifies stabilizer and action on body diagonals.',group='FINITE',statement='Stab_{Rot(cube)}(face diagonal)≅C2⊂V4⊂S4.',his='No new manuscript quote: correction of ne sont pas dansV.')
c(363,[263,265],'current refinement of the false bare-stabilizer assertion','C',
 'Hua2026Thm42.1 proves thefield fixer identity; Beauville gives thefieldnormalizer. Our relative proof retains opposition overZ[1/2], or inverts5 to recover it from the bare divisor. The exact relative correctedstatement was not located as a fullyproved independent publication.',
 'Field correctionopenedNovember2026; relative derivationchecked2026-11-19.',
 'Structuredstabilizer is finiteétale rank24 for2 invertible. Bare stabilizer is the same when5 is also invertible; overchar5 it has120 geometricpoints and theuniversalbarestabilizer is notflat/étale. Five regularoppositions occur inthatfiber.',
 ['Hua2026','Beauville2010','SGA1'],computation='cube_and_pgl.py plus proof_supplement§6; theargument overgeneralbases uses closed subschemes of thefinitepermutation scheme andexplicit sections, not onlypointcounts.',group='OCTAHEDRAL',
 statement='For the standard six-axis divisor of a Klein action, preserve its regular opposition when2 is invertible; if opposition is forgotten require5 invertible for the rank24 equality. The characteristic5 fiber isPGL2(F5) withfive regularoppositions.',his='Refinement, not a manuscript emendation.')
c(379,[279],'current algebraic refinement','E',
 'Elementary solution of thefixed-pointquadratic, independently verified.',
 'Rechecked2026-11-19.',
 'Correct quadratic and radical; ink remainsunresolved.',
 ['Milnor2004'],computation='symbolic_checks.py correctedsubstitution=0.',group='DOUBLING',
 statement='Fix(σ∞) is cut out byz²−2tz+t=0; after adjoining its square root,thepoints aret±√(t(t−1)).',his='Refinement of formula35; not substituted into thetranscription.')
c(382,[282],'current refinement of the image/fiber distinction','E',
 'Milnor’s localdegree equation forquotients oftorus maps gives thecomplex ramification mechanism; thealgebraic argument usesétaleness of[m] and ramificationindex2 ofE→E/±. Both hypotheses hold fordyadicm with2 invertible.',
 'Classicalmultiplicationquotient; exactdivisorformulachecked2026-11-19.',
 'Correct for everym=2^n: degree m²,support m²/2+2,multiplicity1 onfour2-torsionimages and2 onotherpairs.',
 ['Milnor2004','ConradLevel'],computation='symbolic_checks.py n=2 specialization plus proof_supplement§8 for alln.',group='DOUBLING',
 statement='Letq:E→E/±,t=q(0),F_m q=q[m],m=2^n. ThenF_m*([t])=q_*[E[m]] as effective divisors; the reduced scheme image ofE[m] has the same support but usually smaller length.',his='Labelled refinement ofscan65NB.')
c(391,[291,293],'current restricted formulation; not claimed proved in full generality','C',
 'SGA1 tame-cover theory and theopenedKummer/Legendre root descriptions establish localcyclic andquadratic versions. They do not bythemselves supply allmorphisms and descentobstructions oftheauthor’s broad varyingG target. The exact generalstatement remains to be formulated with genuine inertia compatibility.',
 'SGA1 1971; Antieau–Meier2016/2020; status2026-11-19.',
 'Necessary correction proved: i must be the tangent-inertia embedding ofξ. Full arbitraryG equivalence under a minimally repaired target is not asserted here; the validμ2special case isC-SA16-293.',
 ['SGA1','Stacks03PK','AntieauMeier2020'],confidence='medium',computation='kummer_counterexample.py and proof_supplement§9 show necessity; no falseclaim of a full general equivalence proof.',group='KUMMER',
 statement='Restrict target data(G,n,i,ξ,T,κ) to compatible pointedtamecovers: i must coincide with the actual localinertia character ofξ, and morphisms must respect the inducedpower map oninertia andtangentroots. This is a candidate precise reformulation, with theμ2case proved.',his='Not written as an explicit extra condition; this is a labelled reconstruction.')

c(307,[202,233],'not stated in this formula on these pages; earlier-run comparison','E',
 'The trace-zero scalar quotient is elementary F2 representation theory. BrauJones2016 gives the matching invariant-plane decomposition. Exact searches for the canonical formula did not locate a separate priority source; the LM_140-2 scan569/R17 endpoint is unavailable.',
 'Classical finite representation content; specific local formula rechecked2026-11-19.',
 'Correct local algebra: A maps to the class of v↦det(v,Av), with scalar kernel and image F2^J/diagonal. In coordinates (a,b;c,a) the class is delta_(b,c), delta_0=0. This does not verify the missing external LM endpoint.',
 ['BrauJones2016','Burnside1897'],computation='code/scalar_quotient.py → outputs/scalar_quotient.json:64 additivity pairs,48 equivariance pairs,8 coordinate comparisons; kernel scalars and image size4.',group='MOD4',
 statement='For V=F2² and J=V minus0, sl(V)/F2 id is naturally GL(V)-equivariantly isomorphic to F2^J/diagonal via A↦[v↦det(v,Av)].',
 his='No manuscript formula quoted: this is the earlier-run scalar-quotient comparison.')

# Explicit locator correction for the additional cycle-count claim.
for row in claims:
    if row['id']=='C-SA16-305':
        row['scans']=[6,7]
        row['lines']=[{'file':'MPL_64_002-039_transcription.tex','start':144,'end':200}]

def write():
    for row in claims:
        for key in ('statement','status_on_pages','computation','fate','fate_date','present_status'):
            row[key]=polish(row[key])
    (ROOT/'claims.json').write_text(json.dumps(claims,ensure_ascii=False,indent=2)+'\n')
if __name__=='__main__': write()
