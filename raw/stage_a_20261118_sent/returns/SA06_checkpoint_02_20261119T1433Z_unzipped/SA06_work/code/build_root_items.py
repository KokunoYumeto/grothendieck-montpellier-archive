#!/usr/bin/env python3
"""Serialize manually authored entry-by-entry research judgments.

No heading/keyword classifiers are used. Every specification below was authored
after reading the complete note and the relevant numbered transcription passage.
"""
from pathlib import Path
import json,csv,datetime
ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'SA06_work/parts/root'
OUT.mkdir(parents=True,exist_ok=True)
items=[];entries=[];events=[]
RUN='GPT-6 Astra Pro; effort not exposed; SA06-part2/root'
DATE='2026-11-19'

def add(n,p,src,kind,scans,lines,words,statement,reconstruction,check,reason,verdicts=None):
    sid=f'SA06-{n}'
    item=dict(id=sid,sources=[f'{p}#{s}' for s in src],kind=kind,cote='15',scans=scans,
              lines={'file':f'SA06_texts/pro/{p}_transcription.tex','ranges':lines},
              his_words=words,statement=statement,reconstruction=reconstruction,check=check,check_reason=reason)
    items.append(item)
    for i,s in enumerate(src):
        verdict=(verdicts or {}).get(s, 'kept' if i==0 else 'merged into '+sid)
        if verdict=='kept':verdict=f'kept (as {sid})'
        entries.append(dict(entry_id=f'{p}#{s}',item_id=sid,verdict=verdict,reason=reason))
    events.append(dict(statement_id=sid,date=DATE,who=RUN,type='used and rechecked in this run',
                       outcome='Textual comparison: '+check+'. '+reason+' This event does not certify an external theorem.'))

p='MPL_15_170-194r'
add(800,p,[1],'other',[],[], '',
    'Editorial source-key entry defining Current, CT, CN, N87, N195, RS, Hua and Oda69. It asserts no manuscript theorem.',
    'Current-run locators replace per-page fragment line numbers by physical lines of the supplied complete transcription. N87 is supplied; CT, N195, Hua and RESULTS_STATE are not supplied as independent documents.',
    'agrees','The note itself identifies a citation convention. Its contextual paths are provenance data, not evidence that those absent endpoints were read in this consolidation.')
add(801,p,[2],'other',[170,179,180,182,183,185,187,189,190,191,193],[[4,47],[84,129],[156,193],[225,284],[324,397],[445,506]],
    'À examiner; supposons que les degrés ... soient pairs; il n’y a pas en général de sections',
    'The omnibus planning entry distinguishes agenda headings, Frobenius distribution, and fibre comparisons. Its linear/anabelian comparisons, Hua sectioning and modern Nori statements are editorial context, not manuscript assertions.',
    'The current corpus extends the available evidence: cotes 14 and 15/195–206 are supplied through Codex. Claims about other projects remain separately indexed; no anabelian theorem is attributed to these pages.',
    'understates','The local descriptions match the text, but the historical run’s restricted scan boundary is narrower than this consolidation. Its embedded four comparison pairs are kept as earlier-run context and not silently promoted to motivic claims.',{2:'corrected'})
add(802,p,[3],'conjecture',[170],[[6,9]],'VA ... à la Weil ... motifs purs de poids impair ... Conditions de Hodge–Riemann',
    'Agenda: investigate abelian varieties associated with odd-weight pure motives under Hodge–Riemann conditions. No functor, representability theorem, or precise class of motives is specified.',
    'A modern intermediate-Jacobian or weight-one realization interpretation requires an explicit Hodge-level restriction and a polarization; these are possible formulations, not a completed statement on the page.',
    'agrees','The note correctly treats item 0 as an agenda and retains the absent construction and hypotheses.')
add(803,p,[4,49],'self-flagged step',[170],[[47,47]],'Positivité à la Hodge ... diviseurs ... éclatement|éclatements ... pinceaux ??',
    'Investigate reducing Hodge-type positivity to divisor questions by blowups or pencils; the manuscript leaves both the route and the singular-fibre corrections unstated.',
    'Cote 16/47 is an unavailable contextual endpoint. Available cote 14 cycle/Lefschetz material must be compared on its own; it cannot establish the exact reported retraction on cote 16.',
    'understates','The agenda reading is faithful. The older assertion that cote 14 is unavailable no longer applies: this run reviews its supplied folders. That change supplies comparison material, not a missing positivity proof.',{49:'corrected'})
add(804,p,[5],'unpursued implication',[170],[[22,36]],'comparaison des réseaux canoniques; Relations de 4) avec mes notes anciennes',
    'Compare transcendental lattices attached to different places, transcendental and Hodge lattices, and ℓ-adic lattices. The insertion explicitly ties the old-notes reference to item 4.',
    'Comparison torsors require fixed realization functors and coefficient rings. Recovery of an archimedean place from such data is an earlier-run proposal, not a claim made by this table.',
    'agrees','Read the three rows of the displayed table and the inserted reference; neither a reconstruction theorem nor a period-transcendence formula occurs there.')
add(805,p,[6,60],'reading question',[170],[[15,19],[38,45]],'Relations avec le corps de classes; Fonctions L : équation fonctionnelle; Hyp. de Riemann ??',
    'Class fields, L-function functional equations, a topology on Z, and the Riemann hypothesis are listed as intended investigations. No identified CM/Taniyama group or cyclotomic-normalizer theorem is stated.',
    'The phrase Riemann hypothesis is too broad here to identify a zeta function, measure, or exact conjecture. Keep these as agenda items with class F, not as a new precise conjecture.',
    'agrees','The finite list and its question marks contain no construction or proof; the local negative finding in Q01 is valid for these eighteen scans.')
add(806,p,[7],'reading question',[170],[[12,13]],'Extension des ... groupes ... définis par des ... présentiques|présentations',
    'An extension/fundamental-group agenda is written, but the uncertain noun prevents identifying its exact extension problem.',
    'The cleaner wording attributed to Hua is absent as an independently supplied source and cannot resolve the diplomatic alternatives.',
    'agrees','The transcription expressly marks the key word unsure. Nearby motivic vocabulary does not determine the ink.')
add(807,p,[8],'withdrawn in the same text',[179],[[86,116]],'est un groupe de torsion pour p>0; est bijectif modulo torsion ... i≥1',
    'The deleted Leray argument claims H^p(X,i_*G_m) is torsion for p>0. The live Cartier-divisor sequence and connecting map H^i(X,Div_X)→H^{i+1}(X,G_m), bijective modulo torsion for i≥1, remain. The live exact sequence explicitly assumes noetherian X without embedded associated primes.',
    'A sufficient modern proof requires an appropriate rational-function sheaf, torsion of its adjacent cohomology, and the long exact sequence. The deletion alone establishes neither falsity of the assertion nor a live proof.',
    'agrees','The outer deleted block ends before the divisor sequence. The note accurately separates the withdrawn justification from the surviving assertion.')
add(808,p,[9],'reading question',[179],[[101,116]],'(1.1.); un isomorphisme de faisceaux étales :',
    'The sequence is labelled (1.1.); the factoriality sentence ends at a colon and supplies no codimension-one direct-sum display in this transcription.',
    'The usual divisor decomposition for geometrically locally factorial integral schemes is a later-source comparison, not text to insert here.',
    'agrees','Physical lines 103 and 116 verify the number and incomplete ending. Hua’s reported (5.1) and continuation cannot be imported into this witness.')
add(809,p,[10,22],'withdrawn in the same text',[183,185],[[167,169],[227,239]],'la plupart des [deleted]; certaines [inserted]; supposons que les degrés ... soient pairs',
    'The reduction to an even-degree subcategory is promised only for certain distribution questions. A real motivic point is then chosen; this does not prove neutrality of the unrestricted category.',
    'A comparison with the real quaternionic obstruction must retain the category, coefficient field and polarization data. Evenness by itself is not established here as a universal neutrality criterion.',
    'agrees','The correction narrows the quantifier in the opening paragraph; HG03 correctly prevents transporting an obstruction or neutrality statement across the restriction without further work.')
add(810,p,[11],'idea of the earlier run',[185,187],[[227,239],[275,284]],'i(s′)|μ₂; rayons définis par les v(s′)',
    'Earlier-run test: t↦t and t↦t^−1 in G_m restrict identically to μ₂ while giving opposite real cocharacter rays. Order-two data alone cannot determine the signed cone.',
    'This is a test of information loss, not a counterexample satisfying every unspecified preferred-type condition in the manuscript. Retain full cocharacters before discussing effectivity.',
    'agrees','The note labels its calculation as its own and explicitly limits its application; the page’s finite-order restriction and later ray language motivate the test.')
add(811,p,[12,13,14,40,45],'unproved claim',[183,185],[[167,191],[227,238]],'choisissons un pt R-motivique; le noyau de; déterminé ... conjugaison; doivent être identiques',
    'Starting with a finite-type motivic category over S of finite type over Z, restricted to even degrees, and a chosen real motivic point, the page associates to each closed point with a preferred cocharacter a twist ξ(s′) in H¹(R,ker(ε:G_R⁰→G_m)) and a map into the twisted real group, determined up to the indicated real conjugation and compatible with the transported polarization.',
    'Existence of the category, real point, preferred cocharacter and needed torsors is assumed. No full arithmetic sequence with absolute Galois quotient is displayed. Identifying the band with a geometric motivic group would require additional descent.',
    'agrees','The notes correctly distinguish assumption from construction and conjugacy from a preferred representative. The uncertain superscript and second structural-map letter remain reading alerts.')
add(812,p,[15,16],'self-flagged step',[185],[[238,239]],'fini ... si G est commutatif en tous cas ! ... ? à vérifier',
    'The finite-polarization assertion is explicitly unchecked; its later domain is written μ_C without a visible subscript, and “classes de” is deleted. If the domain is μ₂ and the target a complex torus of rank r, the Hom set has 2^r elements. For GL₂(C), the Hom set itself can be infinite although the displayed family lies in one conjugacy orbit.',
    'The torus count and conjugate involution matrices are earlier-run calculations rechecked here. They do not establish that every involution is an admissible polarization or determine the unsubscripted μ_C.',
    'agrees','The note preserves all three material qualifications: domain, admissibility and set versus orbit. Its example is not a direct refutation of an unspecified polarization condition.')
add(813,p,[17,18,19,52],'unproved claim',[183,185,187],[[173,173],[241,241],[275,284]],'conjectures de Tate ... retrouver la structure d’effectivité; dans tte représentation ... entiers algébriques',
    'Conditional proposal: recover effectivity from the family u(s′), via rays and Frobenius integrality. The literal quantifier over every representation of a rigid group category forces every eigenvalue and its reciprocal to be integral, hence units; a nontrivial Tate eigenvalue q^n violates this. For fixed lattice M with cocharacters ν_s, the reconstructed effective monoid is M∩cone(ν_s)^∨, without finite-generation conclusion.',
    'The dual-unit argument and cone-lattice model are earlier-run reconstructions. A valid motivic criterion must specify effective representations, full cocharacters, a common torus and the precise Tate conjectures. Nori–Ayoub or André comparisons do not supply that missing criterion.',
    'agrees','The manuscript explicitly invokes Tate conjectures but gives no complete cone definition. The notes correctly identify the dual-closed quantifier problem and refrain from claiming an unconditional theorem.')
add(814,p,[20],'unpursued implication',[182,185,187],[[158,161],[238,241],[275,284]],'distribution; condition non tautologique; condition arithmétique',
    'These leaves constrain the twisting, polarization and integrality of Frobenius data. They specify no probability measure, counting order, density, or equidistribution limit.',
    'A Sato–Tate comparison is a later interpretive direction attributed to Hua, not an exact claim on these pages.',
    'agrees','Complete reading of the distribution leaves confirms that the proposed measure and averaging problem are absent.')
add(815,p,[21],'reading question',[183],[[167,191]],'géomologiques|géométriques; G^{00}; J_R|j_R',
    'The category adjective, kernel superscript and second structural map remain uncertain diplomatic readings.',
    'Hua’s reported alternatives G^{0u} and i are useful scan-review candidates only. The kernel formula, not an assumed standardized symbol, controls the current mathematical interpretation.',
    'agrees','The unsure marks remain in the supplied transcription; no scan or second-pass correction is supplied to decide them.')
add(816,p,[23,36,41],'unproved claim',[183,191],[[169,169],[339,397]],'il n’y a pas en général de sections; de façon canonique [deleted]',
    'The pro-fundamental objects T_α need not have global sections even when realizations exist after changing coefficients. The page deletes an unqualified canonicity phrase and leaves the reduced object questioned.',
    'Gerbes of fibre functors and torsors of isomorphisms between chosen fibres are distinct. A neutral real realization or a later Nori arithmetic exact sequence does not select a rational neutralization.',
    'agrees','The denial of sections, deleted canonicity phrase, and question mark are all explicit. The note’s restraint is supported, independently of the unverified Hua comparison.')
add(817,p,[24],'self-flagged step',[191],[[347,376]],'provenant sans doute; hensélisé; hensélisé strict.',
    'The ℓ-adic and Witt-valued objects are proposed to descend to smaller henselian coefficient rings, with the origins explicitly tentative.',
    'Any modern descent statement must specify the tensor category, lattice, smoothness and integral coefficient ring; existence after completion alone is insufficient. K15-08 scan195 repeats the tentative ℓ-adic origin.',
    'agrees','The two sans doute phrases qualify the lifts, not just the displayed completed realizations; the Z/Q and subscript ambiguities remain unresolved.')
add(818,p,[25,26,27,53],'self-flagged step',[191,193],[[353,380],[472,473]],'travailler dans la catégorie dérivée; structure filtrée; FV=p',
    'A derived and filtered de Rham–Hodge reduction is required, while the p-adic margin supplies semilinear F,V with FV=p. In degree one of an abelian variety over a perfect field, the precise Oda comparison is available. An unmodified integral tensor category with F⊗F,V⊗V cannot obey FV=p in every tensor degree.',
    'The rank-one test F=p,V=1 over Z_p gives FV=p² on the tensor square; forcing V=p^−1 is nonintegral. That test limits a possible universal reading; the manuscript does not specify its intended tensor target.',
    'agrees','The note faithfully records the question and derived/filtered qualification, and explicitly labels the tensor test as earlier-run work rather than text or a full refutation of the unknown intended category.')
add(819,p,[28],'self-flagged step',[191],[[387,392]],'sans doute uniques à isom près; th. de Lang; k fini',
    'After normalization on effective weight-zero motives, uniqueness of the isomorphism class of integral fibre objects is suggested using Lang. A sufficient modern hypothesis is a represented torsor under a smooth finite-type group over a henselian local ring, with connected special fibre over a finite residue field.',
    'Lang supplies a residue-field point and henselian smooth lifting supplies a section. The manuscript has not verified these group-scheme hypotheses. This gives a conditional justification, not literal uniqueness of an isomorphism.',
    'agrees','The note does not confuse uniqueness of a class with a unique arrow and does not silently add connectedness or smoothness to the page.')
add(820,p,[29],'self-flagged step',[191],[[391,392]],'k parfait de dim ch 1 (?)',
    'An extension from finite fields to perfect fields of uncertain “dim ch 1” is separately proposed and questioned.',
    'Reading ch as cohomological dimension suggests a torsor-vanishing question, but neither the abbreviation nor the relevant integral band is established. Cohomological dimension one does not remove all hypotheses on the group.',
    'agrees','The inserted phrase and independent question mark prevent absorbing this case into the finite-field Lang theorem.')
add(821,p,[30,31],'conjecture',[191],[[393,400]],'il est possible ... T_∞(k)=lim T_α(k) ... un élém. à isom près',
    'Although finite stages may have several classes, the inverse-limit groupoid is hoped to have only the de Rham–Hodge class. A necessary separate question is whether compatible isomorphisms exist between proposed systems.',
    'For I_α=Isom^⊗(ω_α,η_α), pointwise nonemptiness need not imply lim I_α(k)≠∅. A countable cofinal tower of nonempty sets with surjective transition maps does suffice. This is a sufficient criterion, not verified motivic input.',
    'agrees','The possibility is marked explicitly. The margin’s reference to Manin is too uncertain to identify a theorem; it remains a source lead.')
add(822,p,[32],'reading question',[193],[[446,449],[484,492]],'à isom non unique près; non uniq.',
    'The ℓ-adic comparison between geometric base points is nonunique and carries π₁ ambiguity. It is distinct from uniqueness of an isomorphism class.',
    'Hua’s reported unique-isomorphism wording would be an overstatement; only the current supplied nonunique wording is independently checked here.',
    'agrees','Both occurrences of nonuniqueness are visible, with the π₁ action in the first paragraph.')
add(823,p,[33,34],'self-flagged step',[193],[[451,480]],'il ne semble pas ... des isom; autom de k sur k(x); 1/2 linéaire',
    'Different perfect-field-valued points need not give isomorphic p-adic fibres. Automorphisms fixing the residue field act semilinearly on the fibre, whereas other field automorphisms move the point and its fibre; the stated same-localization algebraically closed case is a conjugacy assertion.',
    'The absence of an a priori π₁ action means no automatic linear monodromy action on this chosen fibre model; it is not a theorem forbidding every Galois action. Modern comparisons must retain the coefficient field, point and descent datum.',
    'agrees','The manuscript itself distinguishes these cases. The note keeps its tentative non-isomorphism claim separate from the asserted semilinear descent behavior.')
add(824,p,[35],'reading question',[191,193],[[382,384],[457,458]],'H^{2|1}(Q,G); partie continue ... H^{1|2}',
    'Two cohomological degrees are uncertain. A gerbe-neutralization obstruction and an isomorphism torsor between chosen objects occur in different cohomological degrees.',
    'For a fixed abelian band, gerbes have H² classes and forms/torsors H¹ classes; nonabelian bands require the appropriate nonabelian formalism. This distinction raises an alarm without deciding either exponent.',
    'agrees','The note preserves the alternatives and does not infer the ink from the modern degree convention.')
add(825,p,[37,56,57],'other',[192,194],[[405,441],[509,542]],'ALGÈBRES de LIE SEMI-SIMPLES (9); (8); tout idéal commutatif ... est nul',
    'These are reused Lie-algebra editorial leaves requesting proofs, changed hypotheses and source reorganization. Their mathematical root-space and semisimplicity statements are audited separately from the motivic claims.',
    'Codex K15-08 scans196–206 supply the continuation (7)–(3) and title sheet. Rep(G_m) is semisimple with nontrivial tensor-group center; Lie semisimplicity here cannot prove a motivic center-free claim.',
    'understates','The source-separation judgment is correct; the present corpus directly supplies more of the same editorial sequence than the earlier note’s contextual evidence.',{56:'corrected'})
add(826,p,[38,39],'idea of the earlier run',[183,191,193],[[179,184],[387,392],[446,473]],'le noyau de; motifs effectifs de poids 0; π₁(X) opère; n’opère pas',
    'The notes compare motivic weights with a separate anabelian criterion involving procyclic cusp inertia, an arithmetic normalizer with open image, and cyclotomic conjugation. None of those subgroup data is supplied on these pages.',
    'The comparison is retained exclusively as a prior-project lead. Open arithmetic image does not logically imply the separate character premise; no status in LM6, LM7 or FLAGGED_149 is updated.',
    'agrees','Full reading of the cited passages supplies no normalizer construction or anabelian Hom assertion.')
add(827,p,[42,50,51],'unpursued implication',[170,183,191],[[8,9],[167,191],[339,397]],'une catégorie de motifs; il n’y a pas en général de sections',
    'Earlier-run modern comparisons concern rational Nori Galois descent, the Nori–Ayoub Hopf-algebra comparison in the Betti setting, and the pure Nori/André motivated category. They are not identifications of the manuscript’s unspecified category or its algebraic-cycle morphisms.',
    'Keep each external theorem with its coefficient, field and fibre-functor hypotheses and distinguish circulation from publication. No canonical splitting, algebraic-cycle fullness, Frobenius effectivity theorem or characteristic-p integral target follows merely from these comparisons.',
    'agrees','The local anchors are not source statements of the later theorems. The notes explicitly preserve this boundary; their bibliographic content is rechecked independently in Stage 2.')
add(828,p,[43,44],'reading question',[170,183,191],[[22,36],[167,191],[339,400]],'comparaison des réseaux canoniques; foncteurs fibres',
    'No period-field transcendence-degree equality, genericity of a period point, or algebraic-independence assertion is written in this eighteen-scan package. The notes report positive statements on cote18/11–13, outside this part.',
    'The cote18 conjectures are retained as unverified external archive leads, with the alleged live/cancelled/live distinctions preserved. They are not assigned new part-2 manuscript claims.',
    'agrees','The bounded negative claim is supported by the full transcription; the word transcendant in a lattice comparison does not itself express a period conjecture.',{44:'corrected'})
add(829,p,[46,47],'idea of the earlier run',[183,185],[[188,191],[227,239]],'compatible aux ε_R, J_R|j_R; i(s′)|μ₂',
    'The earlier run separates the Lefschetz sl₂ action on h(P¹)=1⊕L from tensor automorphisms fixing the unit, and separates diag(1,s²) from diag(s^−1,s) by a scalar factor.',
    'The prescribed raising operator sends the unit to the Lefschetz class, ruling out that particular tensor-group action; it does not rule out arbitrary abstract SL₂ subgroups in every motivic group. The current page states no such embedding.',
    'agrees','The notes label this as a previously supplied calculation and accurately avoid attributing an embedding or a new impossibility theorem to the page.')
add(830,p,[48],'reading question',[170],[[47,47]],'Positivité à la Hodge',
    'The A–D dictionary is a report about missing cote16 definitions, not a definition on this page. Its suggested operational matches must be kept attached to that unavailable witness.',
    'In this part the actual cote14 A,A′,A″,B labels are read separately; they must not be silently normalized using the cote16 dictionary or the 1969 printed standard-conjecture lettering.',
    'agrees','No A–D list occurs in this package. The note’s secure/qualified distinction is editorial, and no external cote16 endpoint is newly verified here.')
add(831,p,[54,55],'reading question',[184,186,188],[[198,222],[248,271],[290,320]],'from (15), (18); O_V(−E_φ)[nE]≅O_V[(n−1)E]',
    'The reused coherent-cohomology proof fragments run in source order 70, [71 missing],72,73, followed by the supplied c15/126 source folio74. They use the effective-Cartier-divisor exact sequence, twisting and the induced cohomology sequence to reduce base-point questions to the divisor.',
    'The thresholds and earlier assumptions are only partially visible; the Moishezon attribution is a bibliographic identification to search, not inferred from notation. The formal long-exact-sequence step is checked independently.',
    'understates','The sequence and source folio numbers are exact. Unlike the earlier local run, this consolidation has the c15/126 endpoint, allowing that crosslink to be checked.',{54:'corrected'})
add(832,p,[58],'other',[171],[[53,80]],'SYSTÈMES de RACINES (20); Groupe de Weyl W de E₇',
    'A reused root-system exercise sheet relates E₆ and E₇ Weyl groups to finite orthogonal and symplectic groups; the leaf number 20 and Tribu59 are source identifiers, not motivic dossier extent.',
    'The exact finite-group calculations are claims of the reused source, with unknown individual authorship. They are verified separately and not attributed as new Grothendieck motivic results.',
    'agrees','Title, exercise form, and internal numbers make the source distinction explicit.')
add(833,p,[59],'title, date or page count',[170,171,179,180,181,182,183,184,185,186,187,188,189,190,191,192,193,194],[[4,544]],'FIN LISTE; Théorie de Galois des Motifs; Foncteurs fibres motiviques',
    'The entry includes the nonmathematical listing and complete standing registers U01–U11/T01–T10. The eighteen selected scans contain no announced total extent or date; titles, source folios, archive foliation and row identifiers remain distinct. All mathematical flags in the omnibus tables are covered by items SA06-802–832 and the supplementary claims/readings.',
    'The administrative names and identifiers are irrelevant to the mathematics and are not repeated. Editorial unsure marks alone are not authorial questions; deleted hesitations are not counted as live doubts.',
    'agrees','The full entry, including all subsequent ## tables up to the next ###, was read. Each title and foliation statement matches the transcription; the scope is selected scans, not the archive’s total pages.')
add(834,p,[61],'reading question',[183,191,193],[[167,191],[339,397],[445,506]],'degrés ... pairs; F et V',
    'No universal supersingular-correspondence or Brandt-groupoid assertion occurs in this particular late packet. Such material is present elsewhere in supplied cote15, especially scans34–78 and the B15 transcription.',
    'The earlier-run statement is a bounded absence, not a claim of absence from the topic. Named ANABELIAN_SUCCESSOR/LM7/FLAGGED_149 tasks remain contextual project leads.',
    'agrees','The negative finding is correct locally; the dossier now directs readers to the actual Deuring/Brandt witnesses rather than extending the negative claim to all part2.')
add(835,p,[62],'other',[170,183,185,187,191,193],[[4,47],[167,191],[227,284],[339,400],[445,506]],'À examiner; il est possible',
    'The final omnibus entry reports project-register effects, gives a bibliography, and lists reading priorities. It edits no external register and supplies no new manuscript theorem. Each externally cited result is subjected to the current run’s independent reference check.',
    'The historical statuses of inaccessible project files are reported as such, not adopted as current mathematical verdicts. Cote14 and Codex continuation evidence newly available here revise the old missing-evidence statements.',
    'understates','The entry’s current-scan caution is sound. Its source-boundary assertions are historical and need the present corpus expansion stated explicitly.',{62:'corrected'})

def save():
    (OUT/'items.json').write_text(json.dumps(items,ensure_ascii=False,indent=2)+'\n')
    for name,rows,fields in [('entries.tsv',entries,['entry_id','item_id','verdict','reason']),
                             ('CHECK_EVENTS.tsv',events,['statement_id','date','who','type','outcome'])]:
        with (OUT/name).open('w') as f:
            w=csv.DictWriter(f,fieldnames=fields,delimiter='\t');w.writeheader();w.writerows(rows)
    report={'items':len(items),'verdicts':len(entries),'unique_entries':len({r['entry_id'] for r in entries})}
    (OUT/'build_items_output.json').write_text(json.dumps(report,indent=2)+'\n')
    print(report)

if __name__=='__main__':save()
