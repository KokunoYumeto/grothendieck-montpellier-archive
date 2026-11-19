"""Serialize explicitly authored records, never infer a verdict from a heading/cue.

Every call below is a manual decision after reading the note and its manuscript
passage. The helpers only normalize IDs/filenames and write the requested schema.
"""
import csv, json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
A='MPL_64_002-039'; B='MPL_64_040-077'
items=[]; entries=[]
def item(n, src, kind, loci, words, statement, reconstruction, check, reason, verdict='kept', overrides=None):
    source_ids=[f'{A if p=="a" else B}#{e}' for p,e in src]
    locations=[{'file':f'{A if p=="a" else B}_transcription.tex','scan':s,'start':lo,'end':hi} for p,s,lo,hi in loci]
    row={'id':f'SA16-{n}','sources':source_ids,'kind':kind,'cote':64,
         'scans':sorted(set(s for p,s,lo,hi in loci)), 'lines':locations,
         'his_words':words,'statement':statement,'reconstruction':reconstruction,
         'check':check,'check_reason':reason}
    items.append(row)
    for k,e in enumerate(source_ids):
        v,why=(overrides or {}).get(e,(('merged into item '+str(n)) if k else (verdict+' (as item '+str(n)+')'),reason))
        entries.append({'entry_id':e,'item_id':row['id'],'verdict':v,'reason':why})

item(201,[('a',1),('b',1)],'unpursued implication',[('a',37,1581,1603),('b',77,887,910)],'remonter un torseur',
 'The attached scans 2–77 construct finite level-2/4 objects and tangent data. They do not construct the modular cusp, a Tate family, or the place at infinity invoked by the earlier context.',
 'A scope conclusion of the earlier runs, confirmed only for these supplied leaves. Cote 149 and the claimed Longue Marche boundary results are unavailable endpoints, not assertions of this manuscript.',
 'agrees','The passages culminate in a central lifting problem and a tangent pinning, with no degeneration or cusp construction. Retain the negative scope conclusion locally, not globally.')
item(202,[('a',2),('b',4)],'unpursued implication',[('a',27,998,1055),('a',28,1080,1132),('a',29,1141,1173),('b',69,711,732)],'M_0=M/2M; triplets (I,Q,k)',
 'For a locally free rank-two Z/4-module M, reduction M0 has rank two over F2 and its congruence kernel End(M0) splits canonically as the natural two-dimensional representation and a two-dimensional orientation-permutation representation; the resulting finite torsors encode M. This supplies a finite comparison, not an all-level congruence theorem.',
 'The names bridge B5 and earlier R17 comparison belong to the previous research context. The canonical finite constructions are on these pages; no first-solution or priority claim is inferred.',
 'agrees','The explicit theorem and the later relative torsors match the finite claim. The unseen LM endpoint cannot be checked here.')
item(203,[('a',3)],'idea of the earlier run',[('a',33,1331,1361),('a',36,1450,1556)],'Δ_M=M*/{±1}',
 'The mod-4 matrix U=((1,0),(1,1)) acts on primitive vectors modulo sign with a 4-cycle and two fixed points, determinant +1 and odd reduction permutation. It is a finite quarter-turn example.',
 'U and the proposed cusp comparison are the earlier run’s construction, not a displayed computation by Grothendieck. A cusp interpretation needs the missing LM/cote149 endpoint.',
 'agrees','The six-point object and characters are present; the extra example is compatible and is independently computed in this run.')
item(204,[('a',4),('b',46)],'unpursued implication',[('a',26,945,986),('a',39,1640,1688),('b',69,711,732)],'Λ=Z/4Z',
 'Nothing in this finite-level construction establishes a compatible action on the full congruence tower, an arithmetic image theorem, or the GT conclusions named in earlier research registers.',
 'This is a bounded assessment of the supplied packet. Claims in LM2, LM4_SUCCESSOR, EXIT_TOWER and LM7_PUSH remain unadjudicated because their sources are absent.',
 'agrees','The pages fix Λ=Z/4 and discuss finite torsors; no inverse-limit construction or arithmetic-image quantifiers appear.')
item(205,[('a',5),('b',5)],'unpursued implication',[('a',33,1331,1361),('b',75,816,843)],'droite projective sur Λ; T_{E,0}',
 'The finite projective line P1(Z/4) and later tangent line data do not themselves supply a Gauss–Manin connection, a Cartier operator, or the claimed planning conjecture S20.',
 'S20 is an external planning label, not an authorial conjecture in these leaves. The claim is restricted to scans 2–77; later cote64 pages are separately assessed.',
 'agrees','Neither local anchor contains the differential objects the external claim requires.')
item(206,[('a',6)],'unpursued implication',[('a',28,1080,1117),('b',75,816,843)],'vect. de rg 2; courbe elliptique',
 'A complex elliptic curve’s integral local system can be compared with the finite module and tangent data here only after a family and compatible identifications are specified.',
 'The reported analytic line-and-lattice construction in LM_140-3 scans19–20 and49–50 is an unavailable external endpoint. It is a lead, not a verified cross-text result in this run.',
 'agrees','The note correctly distinguishes a potentially useful analytic comparison from an established differential identification.')
item(207,[('a',7)],'idea of the earlier run',[('a',28,1080,1117)],'Λ-modules libres de rg 2',
 'Any proposed Cartier or positive-characteristic nonabelian Hodge comparison needs an actual connection and its p-curvature hypotheses; the finite module equivalence supplies neither.',
 'This literature boundary is the earlier run’s commentary, not a claim by Grothendieck on this page. Katz and Ogus–Vologodsky are checked as background with their characteristic and liftability hypotheses.',
 'agrees','The transcript is finite combinatorics. Retain the warning against importing differential conclusions, with no assertion about a missing connection.')
item(208,[('a',8)],'idea of the earlier run',[('a',28,1080,1117),('b',77,887,910)],'une équivalence de groupoïdes',
 'An indigenous-bundle or projective-connection interpretation requires the curve, connection, oper-type condition and characteristic assumptions to be specified; no such object is defined in scans2–77.',
 'Bouw–Wewers/Hoshi and the proposed interpretation belong to the earlier contextual research. The pages themselves define finite torsors and tangent pinning.',
 'agrees','The suggested comparison is retained as a lead only; it cannot be deduced from the displayed equivalence.')
item(209,[('a',9),('b',61)],'idea of the earlier run',[('a',39,1640,1688),('b',77,887,910)],'épingle; κ',
 'A future differential comparison should first specify a Legendre family, its de Rham/local-system objects and the intended map from pinning data, then test the relevant characteristic-p hypotheses.',
 'This is a research proposal of the earlier runs, not an open question stated by Grothendieck here. It is not developed in this consolidation.',
 'agrees','The finite and tangent constructions provide possible input but no differential comparison theorem.')
item(210,[('a',10),('b',60)],'other',[('a',39,1640,1688),('b',77,887,910)],'premiers rappels; épinglage',
 'Only the Hua claims whose manuscript endpoints lie in scans2–77 can be assessed here. Claims assigned by the earlier context to later pages or other cotes are not supported by this subsection alone.',
 'Hua is an earlier research-run label. Its full report is not attached; no global validation or refutation is made.',
 'agrees','The local constructions match the stated finite scope, but the prior report’s wider conclusions require absent or separately owned endpoints.')
item(211,[('a',11)],'withdrawn in the same text',[('a',3,16,24)],'structure canonique d’espace affine',
 'Every four-element set I has a canonical affine-plane structure under its regular normal Klein subgroup V⊂S_I. It has no canonical origin and hence no canonical vector-space structure on I itself.',
 'Today’s distinction between an affine torsor and a pointed vector space merely spells out the author’s visible correction.',
 'agrees','The word vectoriel is deleted in favour of affine; the note follows the live reading.')
item(212,[('a',12)],'withdrawn in the same text',[('a',3,21,29)],'centralisateur',
 'For the regular normal Klein four subgroup V of S4, C_{S4}(V)=V while N_{S4}(V)=S4. The corrected word centralisateur is mathematically essential.',
 'The two group equalities are independently enumerated, not silently substituted into the diplomatic text.',
 'agrees','The deletion normalisateur and replacement centralisateur are present and are correctly treated as a local correction.')
item(213,[('a',13)],'unproved claim',[('a',4,64,95),('a',5,101,133)],'on ne prend pour morphismes ... invertibles',
 'The groupoids of four-sets, affine F2-planes and abstract groups isomorphic to S4 are equivalent. The S4 group reconstructs the four-set as its four Sylow-3 subgroups; Aut(S4)=Inn(S4). Only invertible arrows are included.',
 'The fully faithful argument is made explicit by the conjugation action on the four Sylow-3 subgroups. No equivalence of all-homomorphism categories is asserted.',
 'agrees','The margin explicitly restricts to invertible morphisms; that restriction must not be reported as missing.')
item(214,[('a',14)],'reading question',[('a',6,137,142)],'trois sous-groupes de Sylow',
 'The four-set reconstruction requires four Sylow-3 subgroups of S4. The current uncertain reading trois is incompatible with both this construction and the eight elements of order three counted immediately afterwards.',
 'Four is a mathematical alternative for the next image check, not a revised transcription.',
 'agrees','The anomaly is real and retained unresolved; the finite enumeration gives exactly four subgroups of order3.')
item(215,[('a',15),('a',49)],'self-flagged step',[('a',7,202,225)],'fonctoriel; soumis cependant à un choix',
 'The orientation torsors of I and its three partitions J have two natural identifications differing by sign. A convention using the first or last selected element fixes one; functoriality alone does not choose between them.',
 'The note’s distinction between naturality and a selected normalization is retained. This is an explicit convention issue, not an uncompleted theorem.',
 'agrees','The text changes can. to fonctoriel and itself discusses the two conventions.')
item(216,[('a',16)],'reading question',[('a',7,229,256),('a',20,798,811)],'centralisateur de x',
 'For a nonzero x in the normal Klein group of S4, its centralizer is a dihedral group of order8. Its unique cyclic subgroup of order4 consists of the two square roots of x and {1,x}; the cyclic subgroup is not the whole centralizer.',
 'This refutes the literal arrow/marginal centralizer label while leaving the underlying square/Sylow correspondence intact.',
 'agrees','Both suspect occurrences have the same order mismatch; the group computation verifies order8.')
item(217,[('a',17),('a',60)],'unproved claim',[('a',8,260,292),('a',9,297,359)],'Structures de carré',
 'A combinatorial square can be encoded by four vertices with a fixed-point-free opposition, by the associated vertex/edge incidence cycle, by its flags with the specified D8 action, or by the cyclic rotation data described here; the conversions preserve isomorphisms.',
 'The equivalence is checked on the standard square and transported by isomorphisms. A cyclic order alone is taken modulo reversal when orientation is not part of the datum.',
 'agrees','The five descriptions are followed by actual conversions; the notes correctly avoid treating all five as five separate unsolved problems.')
item(218,[('a',18)],'reading question',[('a',10,371,434)],'𝔇_ab^+ ≃ 𝔇/{1,a}',
 'For D8 the abelianization is D8/⟨a⟩≅C2², where a is the antipodal central involution. A superscript plus on this quotient conflicts with the separately defined rotation subgroup D8^+≅C4.',
 'The suggested deletion of the superscript is an image-check alternative. Also, index-two subgroups under discussion are inverse images in D8 of lines in its quotient.',
 'agrees','The order and character discussion determine the intended quotient, but not the ink.')
item(219,[('a',19)],'reading question',[('a',11,439,494)],'B|D; S|C',
 'The last line’s two-element sets should be compared with D, the diagonal set, and C, the codiagonal set. The uncertain B/S readings must not create new objects.',
 'The mathematical naming alternative follows the preceding definitions but does not decide the handwritten letters.',
 'agrees','No independent B or S with the required two-element role is defined there; Stage4 retains both doubts.')
item(220,[('a',20),('a',50),('a',51)],'self-flagged step',[('a',12,501,550),('a',13,555,613),('a',14,626,646)],'On vérifie ... ϖcd=1',
 'For the three C2-torsors of square orientation, codiagonals and diagonals there is a canonical trivialization ω_Q∧C∧D. The representative product relation depends on the stated order/composition convention; dualizing reverses the induced rotation orientation.',
 'Our matrix/permutation test separates the invariant torsor identity from an order-sensitive product. It does not replace the author’s convention.',
 'agrees','The verification and explanation of the apparent dual sign conflict occur on scan14; this is closed locally rather than an outstanding doubt.')
item(221,[('a',21),('a',52)],'self-flagged step',[('a',16,681,698),('a',17,703,720)],'qui mériterait d’être comprise; est une équivalence',
 'Sending an abstract D8 to its four noncentral involutions, with opposition x↦ax, gives an equivalence of groupoids with combinatorial squares. In contrast Q↦Aut(Q) loses the antipodal automorphism and is not that equivalence.',
 'Faithfulness follows because the four reflections generate D8; Aut(D8) has order8 and acts as the full square group. This supplies the proof behind the local construction.',
 'agrees','The question on scan16 is answered by the reflection construction on scan17. Its displayed presentation needs the separate repair recorded in item222.')
item(222,[('a',22)],'reading question',[('a',17,707,719)],'[x,y]=a si y≠x,x′',
 'The printed group presentation is incomplete if interpreted literally: the displayed commutator relations do not impose a²=1, x²=1, centrality of a or x′=ax. Adding these relations gives the intended D8 presentation.',
 'The minimal repaired presentation and the infinite cyclic quotient of the literal presentation are current/earlier-run mathematical reconstructions; no omitted relations are inserted into the text.',
 'agrees','Sending all x-generators to1 in Z and a to0 satisfies the written commutator relations, so the literal group is not forced to have order8.')
item(223,[('a',23)],'unproved claim',[('a',18,726,741),('a',19,746,776),('a',20,778,795)],'S≃∏ A_c; A≃∏ S_d',
 'A square is equivalently a two-set C and an F2^C-torsor S, or a degree-two map A→C with S the set of sections. The dual construction gives A=∏_{d∈D}S_d and the contracted-product identities D=∧_c A_c, C=∧_d S_d.',
 'Products and contractions are interpreted in the category of finite torsors, and the same formulas descend for finite étale sheaves. This interpretation supplies the categorical precision.',
 'agrees','The formulas and inverse constructions are written explicitly on scans18–20.')
item(224,[('a',24),('a',53)],'self-flagged step',[('a',21,816,845),('a',22,850,862)],'Quels sont les sous-groupes; 30; 11',
 'S4 has30 subgroups in11 conjugacy classes. The nonnormal Klein-four subgroups number3, not6; the normal Klein subgroup is V, not its three-element puncture V*. The open enumeration question is answered on the next page.',
 'The complete enumeration, subgroup order distribution and conjugacy orbits are independently recomputed. The live correction six→trois is distinguished from the unresolved V* typography.',
 'agrees','The page itself corrects the multiplicity and closes the count; no global open classification remains.')
item(225,[('a',25),('a',54)],'idea of the earlier run',[('a',22,850,862)],'diagramme ... inclusions',
 'A full inclusion diagram of the30 subgroups is requested but not drawn here. The current computation supplies the66 cover relations and the11 conjugacy classes as an auditable finite output.',
 'The Hasse table is our executable completion of a requested finite check, not a newly transcribed figure or a historical claim.',
 'agrees','The enumeration is present, while the requested inclusion diagram is absent from the supplied continuation.')
item(226,[('a',26)],'idea of the earlier run',[('a',23,869,887)],'deux revêtements de J à six éléments',
 'The six 4-cycles of S4 (opposite by inversion) and the six 2-subsets of a four-set (opposite by complement) give different equivariant six-covers of J. Their stabilizers are respectively C4 and a nonnormal V4; only the former has the usual orientation-preserving octahedral action.',
 'The comparison of their orientation characters is an earlier-run implication, checked here on all24 permutations.',
 'agrees','The text explicitly distinguishes the six-covers; the extra character calculation respects that distinction.')
item(227,[('a',27)],'unproved claim',[('a',24,894,925),('a',25,937,940)],'OK',
 'Choosing one member of each of three opposite pairs gives eight sections, split by parity into two four-sets. The parity torsor has a canonical trivialization once the stated orientation convention is fixed.',
 'We retain the author’s local OK as closure of his check and independently verify the finite signs; it is not merely a prior-run assertion.',
 'agrees','The question at scan24 is explicitly assented to on scan25.')
item(228,[('a',28)],'reading question',[('a',24,894,925)],'∧_j (C_j) ... F2^J-torseur',
 'The Cartesian product of three C2-torsors is an F2^J-torsor of size8; their contracted product is a C2-torsor of size2. The written group label on the wedge conflates these two operations.',
 'The alternative is F2 for the contracted product, leaving the diplomatically recorded label unresolved.',
 'agrees','Cardinalities and the immediately adjacent parity argument force the distinction.')
item(229,[('a',29),('a',56)],'unproved claim',[('a',25,937,940)],'10 ensembles homogènes',
 'The ten nontrivial transitive S4-sets can be represented geometrically by cube features, with stabilizers from the ten non-whole subgroup conjugacy classes. They include vertices, edges, faces, body diagonals, opposite-edge pairs, opposite-face pairs, directed edges, the two tetrahedra, face diagonals and ordered distinct face directions.',
 'The complete stabilizer-to-feature correspondence is supplied by this run; the terse manuscript does not list every map.',
 'understates','The count is correct but its explicit verification is not written out. Our cube enumeration records every stabilizer and orbit size.')
item(230,[('a',30)],'reading question',[('a',25,937,940)],'ne sont pas dans V',
 'For the rotation action of S4 on cube face diagonals, the stabilizer of a face diagonal is generated by a double transposition and lies in the normal Klein V. A literal statement that it is outside V is false.',
 'Possible loss or insertion of a negation is left for the ink. The correct subgroup membership is computationally and geometrically checked.',
 'agrees','The half-turn about the normal through the face preserves its chosen diagonal and exchanges the four body diagonals in two pairs.')
item(231,[('a',31)],'unproved claim',[('a',26,945,986),('a',27,991,996)],'P_M; somme nulle',
 'For M≅(Z/4)² and J=M0\{0}, the64 triples of lifts of the three nonzero mod2 vectors contain16 zero-sum triples. This P_M is a torsor under ker(Σ:M0^J→M0), naturally End(M0).',
 'All16 triples and their action are enumerated independently. The natural map End(M0)→kerΣ sends u to (u(j))_j.',
 'agrees','The definition and cardinalities agree with the manuscript; the next item isolates its contraction-subscript error.')
item(232,[('a',32)],'reading question',[('a',27,991,996)],'P_M ∧_{M0^J} ...',
 'P_M is acted on transitively by V_J(M0)=kerΣ, not by all M0^J, which has64 elements. The contracted-product subscript must be compared with V_J(M0) when forming the torsors attached to its two quotient modules.',
 'This is a mathematical alternative for scan27, not an edit of its ink.',
 'agrees','The all-triples torsor and the zero-sum fiber have different acting groups, already distinguished on scan26.')
item(233,[('a',33),('b',7),('b',9)],'unproved claim',[('a',27,998,1055),('a',28,1061,1076),('b',42,108,149),('b',43,152,157)],'End(V)=V′⊕W',
 'For a two-dimensional F2-space V, A={0}∪{the three involutions in GL(V)} is a two-dimensional GL(V)-submodule canonically isomorphic to V. W={0}∪Aut⁺(V) is a field F4 with orientation-permutation action. End(V)=A⊕W is orthogonal for Tr(uv); sl(V)=A⊕F2·id. The trace sequence0→F2·id→W→F2→0 is nonsplit as an S3-module.',
 'The complete16-matrix verification and the invariant-line argument are our recheck. W has a multiplicative field structure; A is a linear summand, not a subalgebra.',
 'agrees','The repeated exposition on scans42–43 reinforces the earlier decomposition and distinguishes the trace-zero summand correctly.')
item(234,[('a',34)],'reading question',[('a',28,1119,1132)],'u↦id_M+2u',
 'The congruence kernel map is u↦1+2ũ for any lift ũ∈End_{Z/4}(M) of u∈End_F2(M0); it is independent of the lift. Its reduction is id, so the prose description as a composite with reduction having that formula is ill-typed.',
 'The corrected domain/codomain explanation is ours; the formula itself is standard and valid with the lift convention.',
 'agrees','The note distinguishes the correct matrix formula from the erroneous surrounding typing.')
item(235,[('a',35)],'unproved claim',[('a',28,1080,1117)],'est une équivalence de groupoïdes',
 'The groupoid of free rank-two Z/4-modules is equivalent to triples(M0,I,S), where M0 has rank2 overF2, I is an M0-torsor and S an F2^{ω(M0)}-torsor. Morphisms are isomorphisms compatible with all data.',
 'Our proof is that the natural automorphism homomorphism on the two quotient torsors is injective and has image of order96, equal to the target group; both groupoids are connected over a point. For sheaves the equivalence descends étale locally.',
 'agrees','The theorem, quotient torsors and semidirect-product explanation are actually on the page, though not expanded to a full proof.')
item(236,[('a',36)],'unproved claim',[('a',29,1141,1173)],'triplets (I,Q,k)',
 'Equivalently, M corresponds to a four-set I, a square Q, and an isomorphism k:ω(I)→C(Q) to the codiagonal torsor. Thus GL2(Z/4)≅S4×_{C2}D8, using sign on S4 and the codiagonal character on D8.',
 'The pullback uses the codiagonal character, not an arbitrarily chosen nontrivial D8 character; our action computation checks this exact choice.',
 'agrees','Corollaries2–3 state this precise equivalence and cartesian square.')
item(237,[('a',37)],'unproved claim',[('a',30,1197,1211),('a',31,1237,1259)],'groupe dérivé; abélianisé',
 'The centers of GL2(Z/4) and SL2(Z/4) are{±I}; their commutator subgroups have orders24 and12, respectively. GL2(Z/4)ab≅C2² via determinant and mod2 sign; SL2(Z/4)ab≅C4, and its derived subgroup is isomorphic to A4.',
 'All group operations, commutators, quotient orders and quotient element orders are recomputed; the manuscript prime is not misread as a derived-group symbol.',
 'agrees','The finite claims match the pages and pass the enumeration.')
item(238,[('a',38)],'unproved claim',[('a',32,1265,1325)],'diagrammes cartésiens',
 'The five displayed intersections/preimages of GL,SL, their congruence kernels and the two canonical End-summands are cartesian. Descriptions as products or semidirect products use a choice of trivialization of the zero-sum lift torsor.',
 'Our certificate checks all five subgroup intersections. It preserves the manuscript’s stated choice rather than claiming canonical splittings of the resulting products.',
 'agrees','Each square is explicit and the chosen-section qualification is part of the text.')
item(239,[('a',39)],'idea of the earlier run',[('a',28,1093,1117),('a',32,1265,1325)],'produit ½ direct; sg(g)e(Tr u)=1',
 'Reduction GL2(Z/4)→GL2(F2) splits, but SL2(Z/4)→SL2(F2) does not. In a GL splitting lifted transpositions have determinant−1, and the SL condition is sg(g)(−1)^{Tr u}=1.',
 'The explicit S3 complement and the nonsplitting proof are independent checks of the earlier-run observation, not an additional manuscript theorem.',
 'agrees','The marginal determinant condition prevents the erroneous inference that the SL reduction also splits.')
item(240,[('a',40)],'unproved claim',[('a',33,1331,1361),('a',34,1368,1390)],'Δ_M=M*/{±1}; Aut_oct',
 'Primitive vectors of M modulo± form six projective points in three opposite pairs, hence an octahedron. Its twelve edges and eight faces have the stated residue/lift descriptions, and GL(M)/{±I} acts as the full48-element octahedral group.',
 'The equality includes orientation-reversing symmetries; its index-two rotation subgroup must be specified separately.',
 'agrees','The six-vertex construction and exact quotient are explicit and independently enumerated.')
item(241,[('a',41),('b',42)],'unproved claim',[('a',35,1398,1445),('b',68,711,717),('b',69,718,732)],'P/±1; faces de l’octaèdre',
 'The16 zero-sum lift triples map onto the eight octahedral faces, with each fiber exactly the pair(r,−r). A face therefore loses precisely the simultaneous sign of the frame.',
 'This is checked directly on P_M and is distinct from a claim that two opposite frames define different points of an unrigidified elliptic moduli problem.',
 'agrees','The two endpoints identify the same quotient; the fiber has cardinality2 in the computation.')
item(242,[('a',42)],'unproved claim',[('a',36,1450,1556)],'ω; Or; C',
 'The three C2-torsors are related by a single character identity: sign of the mod2 permutation, determinant, and their product. Under the manuscript identifications ω gives mod2 sign, Or(Δ) gives determinant, and the remaining torsor gives their product.',
 'All96 group elements are checked against the associated finite actions. This fixes which character belongs to which geometric torsor.',
 'agrees','The page explicitly differentiates the three torsors and states their relation.')
item(243,[('a',43)],'unproved claim',[('a',37,1562,1578)],'Or(Δ)∧Δ',
 'Twisting an octahedron by its orientation torsor through antipodism produces a new octahedron with canonical orientation. It does not select an orientation of the original octahedron.',
 'The distinction is categorical: the twist changes the object before trivializing its orientation torsor.',
 'agrees','The construction’s target is the contracted-product object, just as the note says.')
item(244,[('a',44),('a',58)],'self-flagged step',[('a',37,1581,1603),('a',38,1608,1633)],'remonter un torseur',
 'Given a projective octahedral torsor, recover a rank-two Z/4 local system by lifting through1→{±I}→GL2(Z/4)→Aut_oct(Δ)→1. The pages reduce this to finding a square with specified diagonal and codiagonal torsors but do not state an obstruction criterion.',
 'The cohomological obstruction and classification of lifts are supplied separately as the earlier-run/current reconstruction, not attributed to this passage.',
 'agrees','The double brackets enclose a real next-step problem; scan38 gives a reduction but no existence theorem.')
item(245,[('a',45)],'idea of the earlier run',[('a',38,1608,1633)],'deux ens. à deux éléments C et D',
 'For specified C2-torsors C,D on a site, the D8 central extension has obstruction c∪d∈H²(−,F2); a lift exists exactly when that class vanishes, and the groupoid of lifts is a torsor under the groupoid of C2-torsors.',
 'This is a labelled cohomological reconstruction of the earlier run’s proposal. The factor set is independently computed using a section b^d a^c; different conventions give a cohomologous reversed cup product.',
 'agrees','The page poses the square-lifting problem; it does not write H² or the cup product. The exact mathematical obstruction is checked separately.')
item(246,[('a',46)],'idea of the earlier run',[('a',34,1368,1390),('a',37,1581,1603)],'GL(M)′',
 'The central extension GL2(Z/4)→GL2(Z/4)/{±I} does not split: the projective involution represented by T=((0,−1),(1,0)) has two lifts, T and−T, both squaring to−I.',
 'This explicit obstruction is an earlier-run observation independently recomputed here; it is not a proof of nonexistence of every individual torsor lift.',
 'agrees','The projective quotient is the manuscript object, and the test correctly shows the universal extension is nonsplit.')
item(247,[('a',47)],'reading question',[('a',37,1581,1603)],'Aut_oct(Δ)′',
 'The quotient GL(M)′ already equals the full octahedral automorphism group. An extra prime on Aut_oct in formula47 would quotient again by antipodism and has the wrong order24 for that exact sequence.',
 'The alternative is the unprimed octahedral group; the notation remains unresolved on the ink.',
 'agrees','The previous exact identification has order48, fixing the mathematical target.')
item(248,[('a',48)],'unpursued implication',[('a',39,1640,1688)],'ne permet pas ... Q',
 'Projectivization retains the octahedron and the four-set information but loses the square’s central lifting data. Recovering a linear module requires the additional compatible square/torsor lift.',
 'This is not a statement that the abstract isomorphism class of a free module over a point is undetermined; it concerns functorial reconstruction and relative twisting.',
 'agrees','The recap expressly says that the projective data do not recover Q.')
item(249,[('a',55)],'self-flagged step',[('a',24,894,925)],'il faudrait ... expliciter',
 'The requested explicit correspondences between cube features and S4 subgroup data are only partly written; the full orbit/stabilizer table can be completed finitely.',
 'Our cube table supplies the maps by invariant coordinate features; the manuscript’s terse suggestion is not promoted to a complete written proof.',
 'agrees','This is a genuine expository completion request, now computationally resolved in the supplementary proof.')
item(250,[('a',57)],'reading question',[('a',35,1445,1448)],'On verra; [illegible margin]',
 'The uncertain On verra and adjacent illegible material do not identify a sufficiently definite mathematical conjecture beyond the surrounding face torsor construction.',
 'No conjecture is reconstructed from illegible words. The passage is assigned classF if included in the claims map.',
 'agrees','The exact reading and grammatical attachment are unresolved; the known surrounding construction cannot fill the missing ink.')
item(251,[('a',59)],'other',[('a',2,2,9),('a',35,1445,1448)],'unsure; illegible (editorial macros)',
 'Editorial uncertainty markers in the transcription are not Grothendieck’s question marks or conjectures. Only mathematically consequential reading alternatives enter Stage4.',
 'This is an editorial distinction rather than a theorem of the manuscript.',
 'agrees','The notes explicitly separate machine/transcriber doubts from authorial open steps.')
item(252,[('a',61)],'title, date or page count',[('a',2,2,9)],'I; Fourbis combinatoires',
 'The packet opens a sectionI with the uncertain title Fourbis combinatoires. The alternative spelling/word remains a reading question; it is not normalized.',
 'No date is inferred from this heading.',
 'agrees','The title and uncertain word are present; the title is separate from later headings.')
item(253,[('a',62)],'title, date or page count',[('a',2,2,9),('a',39,1640,1688)],'(40)',
 'Scans2–39 contain38 scan pages. The pencil mark(40), author foliation and archival foliation are different kinds of counts and cannot be identified as a reliable total of this section from the transcription alone.',
 'The physical scan count is ours; the origin and scope of the pencil numeral are unresolved.',
 'agrees','The note correctly distinguishes author numbering, archive marks and supplied scan extent.')
item(254,[('a',63)],'title, date or page count',[('a',8,260,292),('a',20,798,811),('a',26,945,986),('a',39,1640,1688)],'Structures de carré; Complément; Rappels',
 'The internal headings follow four-sets, squares, S4 subgroups, rank-two Λ-modules and a partial recap. The final recap does not make the preceding lifting problem disappear.',
 'This is a structural inventory of supplied leaves, not a new thematic division attributed to the author.',
 'agrees','The note’s local heading list tracks the actual progression.')

item(255,[('b',2)],'unpursued implication',[('b',71,744,760),('b',72,765,774)],'norme; T′⊗n→T',
 'The local norm construction for a tame ramified cover produces a power relation between tangent lines. Comparing it with the norm functoriality named in Longue Marche requires the actual external cover and its tangent conventions.',
 'The LM2 norm link is the earlier run’s contextual lead. The present manuscript endpoint is checked, but the cited LM source is not attached.',
 'agrees','The norm and tangent construction is present; the external functorial comparison is not thereby established.')
item(256,[('b',3)],'idea of the earlier run',[('b',71,744,760),('b',77,887,910)],'épingle; T′',
 'A future cusp test could compare this tangent-root datum with a specified Tate degeneration and its inertia generator, including the normalization of local parameters.',
 'This proposal comes from the earlier run’s context; no cusp or Tate model is asserted to occur in these leaves.',
 'agrees','The tangent construction is a possible input for the proposal, while its geometric degeneration endpoint is absent.')
item(257,[('b',6)],'other',[('b',75,816,843)],'courbe elliptique E',
 'Cote93, cited by the earlier notes for indigenous or differential constructions, is not in this topic attachment. Its claims cannot be used to complete a differential statement here.',
 'This is an access-and-scope conclusion, not a verdict on the mathematics of the missing cote93.',
 'agrees','The local pages introduce tangent pinning; no cote93 passage is supplied to verify the proposed match.')
item(258,[('b',8)],'reading question',[('b',42,108,149)],'F2·1 est son propre orthogonal',
 'The scalar line is self-orthogonal inside the two-dimensional W for the trace pairing. Inside all End(V), its orthogonal is the three-dimensional trace-zero space, so the ambient space is essential.',
 'The mathematical clarification follows the preceding W restriction; it does not require changing the words if their local scope is W.',
 'agrees','The earlier note correctly prevents a four-dimensional reading of this marginal self-orthogonality assertion.')
item(259,[('b',10)],'other',[('b',42,108,149)],'End(V)=V′⊕W',
 'No live assertion that End(V), or its three-dimensional trace-zero subspace, is commutative occurs at this endpoint. Only W is asserted to carry the field structure F4.',
 'The commutativity issue belongs to Hua’s earlier modernization/context and is not imported as a false manuscript claim.',
 'agrees','Reading the complete proposition supplies no such blanket commutativity sentence.')
item(260,[('b',11),('b',25)],'unproved claim',[('b',40,6,46),('b',55,364,386),('b',56,387,406),('b',57,407,418)],'I≃K∧_V F_t; l’hypothèse ... constant ... superflue',
 'For the reference Klein cover with fiber F_t, the four-point torsor I and the twisting torsor K satisfy I≅K∧_V F_t and K≅I∧_V F_t. Since V has exponent2, this relation removes the temporary assumption that I is constant. I, the degree-three cover J, the complementary section/cover S and K are distinct data.',
 'The crowded scan40 diagram is interpreted only through the later explicit formulas. The canonical triviality of P∧_V P for a V-torsor uses exponent2.',
 'agrees','The later formulas and margin explicitly justify the removal of constancy; they do not choose a section of any torsor.')
item(261,[('b',12)],'unproved claim',[('b',45,168,185),('b',46,186,201),('b',47,202,219)],'z↦−z; z↦1/z; z↦−1/z',
 'Over a base with2 invertible, a fiberwise faithful Klein-four subgroup of the automorphism group of an étale form of P1 is étale locally conjugate to{z,−z,1/z,−1/z}. The three nonidentity involutions have six distinct fixed points in three pairs.',
 'Étale localization chooses the eigensections and a square root of the remaining unit. Fiberwise faithfulness, not merely a set-theoretic injection on global points, is the relative hypothesis.',
 'agrees','The normal-form calculation and local trivializations are on the pages and extend to non-split conics by descent.')
item(262,[('b',13)],'unproved claim',[('b',47,202,219),('b',51,287,303),('b',52,308,325)],'normalisateur; forme de S4',
 'The normalizer of the standard Klein group is a finite étale S4-form of rank24 over bases with2 invertible. It is the group of projective automorphisms preserving the chosen regular opposition on the six axes, including in characteristic3 and5.',
 'The relative proof is by the explicit24 transformations in a splitting étale cover, then descent. Beauville’s field-level prime-to-characteristic result alone does not cover characteristic3.',
 'agrees','The structured normalizer claim is correct; it must be distinguished from the larger bare-divisor stabilizer claimed nearby.')
item(263,[('b',14),('b',15)],'idea of the earlier run',[('b',48,228,237),('b',49,241,253),('b',50,256,282),('b',51,287,303),('b',53,327,343)],'Γ est étale; au plus une',
 'In characteristic5 the standard six axes equal P1(F5), whose full projective stabilizer is PGL2(F5), of order120. The structured stabilizer has order24, and there are five regular opposition structures. Thus the universal bare stabilizer is not étale across characteristic5, and uniqueness of the opposition is false there. Inverting5, or retaining opposition, repairs the assertion.',
 'This correction is credited by the earlier notes to Hua; our finite-field and partition enumeration independently verifies it. It is not claimed as new. A proof over arbitrary bases is given for the structured group and for the unstructured group over Z[1/10].',
 'agrees','The note precisely identifies the overbroad live theorem; no later correction of this exception occurs in scans2–77.')
item(264,[('b',16)],'self-flagged step',[('b',50,256,282),('b',51,287,303)],'faux; Il faut un petit argument',
 'Two local arithmetic exclusions are visibly rejected, and an extension argument is requested/sketched. The concluding assertion that every non-opposite pair has trivial fixer is still maintained; the characteristic5 exception is not retracted.',
 'The rejection marks apply to the nearby calculations, not automatically to the whole theorem. The current proof instead uses the sum identity5(a−1)=0 when5 is invertible.',
 'agrees','The notes correctly separate withdrawn calculations from an unretracted overgeneralization.')
item(265,[('b',17)],'unproved claim',[('b',51,287,303),('b',52,308,325),('b',53,327,343)],'structure octaédrale régulière',
 'For a fixed étale form X of P1 over a base with2 invertible, Klein-four subgroup schemes, finite étale S4-form subgroup schemes, and six-point étale divisors with a regular fixed-point-free opposition correspond. The maps are axes, the unique normal Klein subgroup, and the direct group of the chosen regular structure.',
 'The c→b formula is read mathematically as the chosen structured direct group, not the full unstructured divisor stabilizer in characteristic5. This is an explicitly stated refinement of the literal wording.',
 'agrees','The regularity condition supplies extension of the direct group; the inverse constructions agree after the explicit local normal form.')
item(266,[('b',18)],'unproved claim',[('b',51,287,303),('b',53,327,343)],'μ4*',
 'The orientation double cover of a regular geometric octahedron is canonically the primitive fourth roots μ4*. At a vertex, a selected direct quarter-turn acts on the tangent line by i or−i; reversing the orientation interchanges them.',
 'The tangent-multiplier proof is expanded in this run. It is invariant under change of vertex and descends without choosing i globally.',
 'agrees','The margin states the orientation identification and the conic corollary uses it; the note’s proof matches those objects.')
item(267,[('b',19),('b',20)],'unproved claim',[('b',53,327,343)],'x²+y²+z²=0; totalement anisotrope',
 'Structured conics of this type are forms of the reference conic x²+y²+z²=0 with its signed-permutation S4, hence are classified by S4-torsors, equivalently four-sheeted étale covers. An S4-form subgroup scheme need not have24 rational points: the standard Klein group on split P1_R has normalizer with eight real points, while the anisotropic reference conic has constant S4.',
 'The equivalence is a descent statement. The quartic trace-zero quadratic model is a current/earlier-run explicit realization; it is not written in this form on scan53.',
 'agrees','The text says locally isomorphic and explicitly notes the anisotropic conic. These qualifications prevent the rational-point misinterpretation.')
item(268,[('b',21)],'reading question',[('b',47,202,219),('b',52,308,325),('b',53,327,343),('b',54,348,360),('b',56,387,406)],'icosaédrales; points fixes; V*',
 'The six-vertex construction calls for octahedral terminology, fixed-point-free opposition, and a V-torsor rather than a torsor under its three-element puncture V*. The crowded orientation insertion in Corollary2 may describe compatibility with the canonical orientation isomorphism rather than an independent choice.',
 'These are separate image-check alarms, including the D2/D4 naming and missing puncture on a displayed Σ equality. None changes the diplomatic reading.',
 'agrees','The mathematics indicates the intended objects, but the source’s exact words and insertion attachment require the scans.')
item(269,[('b',22)],'unproved claim',[('b',55,364,386),('b',56,387,406)],'Q(u)=Tr(u²); L(u)=0',
 'For a cubic finite étale algebra A over a base with2 invertible, Q(y)=Tr_A(y²)=0 in P(A) is a smooth conic. The square map y↦y² lands in the separate projective line Tr_A(x)=0 and gives a degree4 quotient by F2^J/F2, branched along three sections after splitting. No inversion of3 is required.',
 'Smoothness and degree are checked after an étale splitting: the trace pairing is nondegenerate, even if Tr(1)=0 in characteristic3.',
 'agrees','The two margin formulas supply the descent model, while the detailed base-change argument is our expansion.')
item(270,[('b',23)],'unpursued implication',[('b',55,364,386),('b',56,387,406)],'revêtement de référence',
 'For the local Klein action, q(z)=z²+z⁻² and g2(z)=−(z²−1)²/(4z²) define the same degree4 quotient because g2=(2−q)/4. Their branch supports are{0,∞},{±1},{±i}.',
 'The coordinate identity is an earlier-run cross-project calculation redone symbolically here. The cited cote142/146 passages themselves are unavailable and remain leads.',
 'agrees','The manuscript’s reference cover is compatible with this identity; no broader modular-cover equivalence is inferred.')
item(271,[('b',24)],'unproved claim',[('b',54,348,360),('b',64,574,587)],'l’action de V_I ... se prolonge',
 'For an étale degree-four divisor I in a genus-zero curve over a base with2 invertible, the canonical double-transposition Klein action on I extends uniquely to the curve. In coordinates I={∞,0,1,t}, the three maps are(z−t)/(z−1), t/z and t(z−1)/(z−t), with t and1−t units.',
 'Uniqueness on three disjoint sections gives relabelling compatibility and descent. The assertion concerns the canonical Klein subgroup, not all permutations of I.',
 'agrees','The later formulas supply the elementary proof of the proposition’s exact scope.')
item(272,[('b',26)],'unpursued implication',[('b',55,364,386),('b',56,387,406)],'l’identité de V_J',
 'The admissible V_J-cover of the punctured line is required to have the specified identity monodromy on the elementary-two quotient. Geometric connectedness alone leaves six possible identifications after J is split.',
 'The count is the order of GL2(F2), already independently enumerated. This is a distinction of marked covers, not six necessarily different unmarked covers.',
 'agrees','The inserted identity condition is stronger than the deleted connectedness formulation.')
item(273,[('b',27),('b',28)],'unproved claim',[('b',58,424,460),('b',59,461,489)],'σx=a−x; E=I∧_V E0',
 'A genus-one torsor E under E0 equipped with an involution inducing−1 is reconstructed from its fixed-point E0[2]-torsor I by E≅I∧_{E0[2]}E0. In a local origin σ(x)=a−x, I=[2]⁻¹(a), and E/E0[2]→E0 is canonically x↦2x−a.',
 'The origin-change check supplies descent and makes the word canonically precise. These are equivalences of groupoids, retaining torsor automorphisms.',
 'agrees','The local formulas and reconstruction are explicitly stated on scans58–59.')
item(274,[('b',29)],'reading question',[('b',61,496,527)],'degré2 underbrace in(27)',
 'E0[4] minus E0[2] has12 points and its quotient by± has six. The quotient map has degree2; a degree2 underbrace attached to the six-point target conflicts with the claimed octahedron.',
 'This records a placement/label issue rather than changing the clearly read numeral2.',
 'agrees','The surrounding cardinalities determine which arrow can have degree2; the doubts file says the digit itself was legible.')
item(275,[('b',30)],'self-flagged step',[('b',61,528,537),('b',62,538,542)],'presque cartésien; il doit être facile de vérifier',
 'The square relating the Klein cover, its twist and the elliptic quotient is cartesian off the branch divisor; over geometric fibers it is recovered by normalization. Over a nonnormal base use the canonical smooth branch model, since absolute normalization need not commute with base change.',
 'The local normalization proof and descent reconstruction are supplied here. No blanket claim that every displayed ramified square is literally cartesian is made.',
 'agrees','The qualifier presque and the request for a verification are genuine; the next simplification does not prove a stronger cartesian assertion.')
item(276,[('b',31)],'other',[('b',62,538,542)],'supposons ... E=E0',
 'After the relative torsor discussion, the text explicitly specializes to the neutral elliptic curve E=E0 for the following computation. It does not prove that arbitrary genus-one torsors have rational origins.',
 'This is a scope restriction visible in the text; the earlier notes correctly preserve it.',
 'agrees','The change of setting is announced, and the preceding nontrivial I-torsor data are not erased.')
item(277,[('b',32)],'idea of the earlier run',[('b',63,545,569)],'donner une ... description intrinsèque',
 'The requested intrinsic doubling map is the quotient by the canonical Klein group of the four-set I=J∪{t}, followed by the unique identification of the target branch trisection with the original labelled J.',
 'This construction is our/earlier-run answer to the author’s question. The given branch labelling is essential; no arbitrary target coordinate is selected.',
 'agrees','The page asks for an intrinsic description and supplies the relevant involutions/branch data, but not this categorical formulation in full.')
item(278,[('b',33)],'self-flagged step',[('b',63,545,569),('b',64,591,622)],'f2^t; s’annuler ... double',
 'The images of a finite set alone do not determine a rational map. The subsequent degree4 and double-zero/pole conditions, together with the three branch labels and value at I, uniquely determine the normalized doubling map.',
 'The uniqueness proof uses divisors or the fixed field of the Klein action; it is not inferred from interpolation on the four marked points alone.',
 'agrees','The next page supplies the degree and multiplicity conditions missing from the initial informal wording.')
item(279,[('b',34)],'reading question',[('b',64,574,587)],'t±√(t(1−t))',
 'The fixed points of z↦t(z−1)/(z−t) satisfy z²−2tz+t=0, hence are t±√(t(t−1)). The literal radical t(1−t) has the wrong sign.',
 'The corrected radical is a mathematical alternative; the original note and doubts say1−t was clearly read, so an authorial slip remains possible.',
 'agrees','Substitution gives the nonzero residual−2t(t−1) for the written alternative under the standing unit hypotheses.')
item(280,[('b',35)],'unproved claim',[('b',64,591,622),('b',65,627,631)],'f2^t(z)=t((z²−2z+t)/(z²−2tz+t))²',
 'Over Z[1/2,t,1/(t(t−1))], the displayed rational map has degree4, is invariant under the three Klein involutions, takes all four marked points to t, and has the required three ramified fibers. Its normalization constant is c_t=t.',
 'The symbolic certificate verifies invariance, resultant4t(t−1)² and tA²−B²=(t−1)(z²−t)². A malformed intermediate equality is isolated rather than invalidating the final formula.',
 'agrees','The final formula is correct. The note appropriately separates intermediate algebra slips from the final result.')
item(281,[('b',36)],'self-flagged step',[('b',65,627,631)],'Il reste à vérifier; OK; Pour0,∞,1 on trouve1',
 'The final verification is locally marked OK. Before squaring, A/B equals −1 at z=1,t and +1 at 0,∞; after squaring the value f2^t=t is correct at all four points.',
 'The missing minus is a reading/arithmetical alarm only for the intermediate unsquared value. It does not reopen the final doubling theorem.',
 'agrees','The author’s closure marker is present, and the direct substitution confirms the final assertion while detecting the sign slip.')
item(282,[('b',37),('b',38)],'unproved claim',[('b',65,627,631)],'itérée ... 2^n; schéma image',
 'Iteration gives the quotient of multiplication by m=2^n. Over a field of characteristic≠2 the set f_m⁻¹(t) is the image of E[m] in E/±. As a divisor, f_m*([t])=q_*([E[m]]): multiplicity1 at the four images of E[2] and2 at other pairs. For m≥4 the reduced scheme image is not the full fiber.',
 'This is the earlier-run multiplicity correction, independently verified at m=4 and proved by ramification degrees. The manuscript’s scheme-image wording is kept distinct from the corrected divisor identity.',
 'agrees','The iteration claim survives; identifying the scheme image with the whole fiber would discard multiplicities.')
item(283,[('b',39)],'idea of the earlier run',[('b',66,638,661),('b',67,662,709)],'relèvements ... somme nulle',
 'A symmetric reference module is M_J=ker(Σ:(Z/4)^J→Z/4). The vectors r_j=3e_j−Σ_k e_k, namely(2,3,3),(3,2,3),(3,3,2), have zero sum and reduce to the three nonzero vectors; any two form a basis.',
 'This is an earlier-run explicit model, not a formula attributed to the manuscript. Its permutation equivariance supplies a descent proof for the relative zero-sum lift torsor.',
 'agrees','The stated reference vectors agree with the note and the independent certificate; their determinant in an augmentation basis is3.')
item(284,[('b',40)],'idea of the earlier run',[('b',66,638,661),('b',67,662,709)],'0→M0→M→M0→0',
 'The natural additive extension0→M0→M→M0→0 is nonsplit as an extension of abelian groups: every homomorphism from an exponent2 group lands in2M, hence has zero reduction. This does not contradict the GL automorphism-group splitting.',
 'The distinction is the earlier run’s warning, independently proved here.',
 'agrees','The source’s lifted-vector torsor must not be confused with an additive splitting of M.')
item(285,[('b',41)],'reading question',[('b',67,662,709)],'Tr_M',
 'The trace map on J-indexed lifts is their sum, with kernel the zero-sum torsor. It is different from matrix trace End(M0)→F2 used for determinant on the congruence kernel.',
 'The notation is disambiguated by domain and codomain, without changing either symbol.',
 'agrees','Both constructions are present in the packet but occur on different objects.')
item(286,[('b',43)],'unproved claim',[('b',66,638,661),('b',68,711,717),('b',69,718,732)],'épinglage absolu',
 'After the three nonzero mod2 vectors are labelled, a zero-sum lift triple gives a full Z/4-basis; there are16 such lifts. Allowing the six labelings gives96 frames. A face retains eight choices after the labeling, losing simultaneous sign.',
 'The counts are the explicit P_M and GL2(Z/4) counts, redone in this run.',
 'agrees','The page distinguishes a labeling of J from a section of P, exactly the two factors in the count.')
item(287,[('b',44)],'idea of the earlier run',[('b',69,718,732)],'relèvement',
 'For an elliptic curve with a full level4 frame α, the objects(E,α) and(E,−α) are isomorphic via[−1]. Thus sign loss of a frame cannot be turned directly into two distinct points of the ordinary level-structure moduli groupoid. A fixed underlying object with a specified identity map is a different comparison.',
 'This corrects a possible overinterpretation of the earlier finite ambiguity. It does not deny that the map of frame torsors has two-element fibers.',
 'agrees','The note correctly separates frame sets from isomorphism classes of marked curves.')
item(288,[('b',45)],'unpursued implication',[('b',56,387,406),('b',69,718,732),('b',75,816,843)],'conique; épinglage',
 'The trace conic and level4 pinning provide a concrete finite geometric input for the Jacobi/conic comparison named in the LM context; they do not identify all analytic or arithmetic structures in that separate proposal.',
 'The LM_140-2 scan570 endpoint is not attached, so its strongest interpretation remains a prior-run lead.',
 'agrees','The local ingredients are present but the external comparison is not proved in this packet.')
item(289,[('b',47),('b',48)],'unproved claim',[('b',71,744,760)],'homomorphisme canonique T′⊗n→T',
 'For a smooth relative curve and a section, a tame totally ramified local cover x=u y^n with n invertible gives an isomorphism(T_y)^{⊗n}→T_x from its leading jet. If constructed using the determinant norm of y, N(y)=(−1)^{n−1}x/u, so the two normalizations differ by that sign.',
 'The norm-versus-jet sign comparison is the earlier run’s observation, rechecked by multiplication matrices for n=2,…,8. It is a convention distinction, not automatically a manuscript error.',
 'agrees','The page states the tangent map through norms; the note correctly identifies where a sign convention enters.')
item(290,[('b',49)],'unproved claim',[('b',72,765,774)],'μ_n↪G',
 'The stabilizer/inertia at a chosen ramification point acts faithfully on its tangent line and is canonically identified with μ_n in the tame cyclic local model. Its inclusion into the covering group is determined by the pointed cover, not an independent arbitrary injection.',
 'The local action y↦ζy supplies the exact character; this condition becomes critical for the next equivalence.',
 'agrees','The source constructs i from the tangent action before later listing it among abstract data.')
item(291,[('b',50),('b',51)],'unproved claim',[('b',72,765,774),('b',73,775,804)],'une équivalence ... (n,G,i,ξ)',
 'The unrestricted listed target(n,G,i,ξ) is too broad unless i is required to match the actual inertia of ξ. Over C take X=A1_x, Y=A1_y×{0,1}, x=y², G=C2² acting by(a,b)(y,c)=((−1)^a y,c+b). The cover is smooth, finite, a G-torsor off0 and has a chosen point above0, but choosing i as the second factor contradicts its actual first-factor inertia.',
 'This counterexample is the earlier run’s construction, fully checked here. The plausible corrected theorem concerns compatible tame pointed covers and full tangent-root data; no blanket equivalence of the written unrestricted categories is retained.',
 'agrees','The necessary compatibility is used in the construction but absent from the target’s written conditions; all stated geometric hypotheses of the counterexample hold.')
item(292,[('b',52)],'reading question',[('b',73,775,804)],'à isomorphisme unique près',
 'An unrigidified n-th root of a line has μ_n automorphisms. Uniqueness up to unique isomorphism can hold only for an object with the complete specified root/tangent comparison and compatible morphisms, not for a bare root line.',
 'This is a typing/rigidification qualification, not a claim that the root groupoid is a set.',
 'agrees','The note appropriately separates uniqueness of a comparison once full data are fixed from the automorphisms of the underlying root object.')
item(293,[('b',53)],'unproved claim',[('b',74,806,811),('b',75,816,843)],'T⊗2≃T_Σ,t',
 'With2 invertible, an elliptic curve with its three nonzero2-torsion labels is equivalent to a branch parameter t on the complementary projective line and a line T with T²≅T_{Σ,t}, as a groupoid of square-root data. The root encodes the quadratic twist.',
 'The general G counterexample does not refute this μ2 special case; the four-branch double-cover construction and root-line automorphisms give the correct formulation.',
 'agrees','The specialization to quadratic covers fixes the inertia automatically and retains the needed tangent-root datum.')
item(294,[('b',54)],'reading question',[('b',74,806,811)],'étale au-dessus de X; Σ_J* fibré en droites projectives',
 'The ramified cover is étale over X\{t}, not over the whole X. The punctured Σ_J* is an open complement of the branch trisection, not a complete projective-line fibration.',
 'The proposed missing stars/complement qualifiers remain reading alternatives; the associated complete Σ is the projective-line bundle.',
 'agrees','The preceding ramified local model and the defined puncture force these distinctions.')
item(295,[('b',55)],'unproved claim',[('b',75,816,843)],'T_Σ≃O(2)(Or)',
 'For Σ_J=P(ker Tr_{O_J/O_S}), the relative tangent line is O(2) twisted by the determinant/orientation line of the rank2 trace-zero bundle. Forgetting that sign line changes the relative descent when J is nonconstant.',
 'The projective-space convention may dualize det, but a sign line is canonically self-dual; the claimed orientation factor is therefore convention-independent here.',
 'agrees','The author includes the orientation twist and uses it in the following μ4 construction.')
item(296,[('b',56)],'unproved claim',[('b',76,848,883)],'O_t(1)∧_{μ4}Q0',
 'A μ2 twist leaves a line’s square unchanged; a μ4 twist changes its square through the quotient μ2. The standard oriented square Q0 with C(Q0) trivial and D(Q0)≅μ4* therefore twists O_t(1) to the required square root of O_t(2) with orientation factor.',
 'The construction requires the specified character and torsor identifications; the explicit standard square is only promised here and supplied on scan78.',
 'agrees','The page’s power calculation is correct when its specified oriented-square data are retained.')
item(297,[('b',57)],'self-flagged step',[('b',76,848,883)],'qu’on précisera',
 'The reference square Q0 is postponed at scan76. The attached continuation defines its oriented μ4 action and codiagonal/diagonal data at scan78, so this local promise is closed later in the supplied topic.',
 'The later endpoint is separately read and cited in the link/proof records; x⁴=−4 and s_i=1−i are earlier-run coordinate models, not words on this page.',
 'agrees','The note is right about the local postponement; its open status is updated using the available continuation.', verdict='corrected')
item(298,[('b',58)],'unproved claim',[('b',77,887,910)],'κ; deux épinglages',
 'For fixed branch data and the chosen reference square, compatible isomorphisms κ between the tangent root lines form a μ2-torsor. Over an algebraically closed field there are exactly two; over a general base there need not be a global section.',
 'The geometric two-element count is not promoted to two global choices on every base. Varying J also requires its stated labeling α.',
 'agrees','The compatibility square is explicit; the root-torsor formulation gives the correct relative interpretation.')
item(299,[('b',59)],'unpursued implication',[('b',77,887,910)],'κ',
 'The tangent pinning κ changes sign under[−1], unlike an octahedral face or the Weil pairing of a basis (since det(−I)=1). It is therefore sensitive to the sign lost by P_M→faces.',
 'This is a comparison of the specified actions, not a claim of two nonisomorphic unrigidified marked elliptic curves.',
 'agrees','The κ map is additional tangent data and the finite sign action has been explicitly checked.')
item(300,[('b',62)],'title, date or page count',[('b',40,6,46)],'I c',
 'The uncertain I c at scan40 labels a crowded continuation diagram. It is not securely a new independent title.',
 'The interpretation as an internal continuation label is editorial and remains uncertain.',
 'agrees','The diagram continues objects from the preceding section; the letters themselves need an image check.')
item(301,[('b',63)],'title, date or page count',[('b',44,158,162),('b',45,168,185),('b',69,718,732)],'II. Structure octaédrale de la droite projective',
 'SectionII begins on scan44 and its mathematical body runs through scan69. The parenthetical pencil notation is not a secure authorial total; scans45–69 comprise25 leaves in the supplied numbering.',
 'The scan count is mechanical; the sense of the ambiguous v/p mark is left unresolved.',
 'agrees','The heading and section boundaries are explicit and distinct from archive pencil counts.')
item(302,[('b',64)],'title, date or page count',[('b',70,733,737),('b',71,744,760)],'III. Épinglage de Legendre',
 'The headingIII Épinglage de Legendre appears on scan70, followed by the tangent-space subheading on scan71. It is the author’s new section, not a title retroactively applied to scans45–69.',
 'No date is inferred from the heading.',
 'agrees','Both heading and starting tangent construction are present.')
item(303,[('b',65)],'title, date or page count',[('b',54,348,360),('b',58,424,460),('b',63,545,569),('b',71,744,760),('b',75,816,843)],'Proposition; f2^t; Épinglage',
 'The packet’s internal progression is Klein geometry, four-pointed quotients and twists, genus-one reconstruction, intrinsic doubling, relative frames, and tangent/Legendre pinning.',
 'This inventory follows actual subsection labels and displayed constructions while keeping the sectionII/III division.',
 'agrees','The note’s internal heading list agrees with the leaf order.')
item(304,[('b',66)],'title, date or page count',[('b',41,47,105)],'9 mars1982; L. Thaler',
 'Scan41 is a reused university election circular dated9 March1982, signed/typed in another administrative voice. Its date dates that printed sheet, not by itself the composition of the surrounding mathematical manuscript.',
 'The reused sheet provides a possible material terminus only if its relation to the handwriting is established from the original; no exact manuscript date is inferred here.',
 'agrees','The different genre and named administrative author are explicit in the transcription.')

def write():
    ROOT.mkdir(parents=True,exist_ok=True)
    (ROOT/'items.json').write_text(json.dumps(items,ensure_ascii=False,indent=2)+'\n')
    with (ROOT/'entries.tsv').open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=['entry_id','item_id','verdict','reason'],delimiter='\t');w.writeheader();w.writerows(entries)

if __name__=='__main__': write()
