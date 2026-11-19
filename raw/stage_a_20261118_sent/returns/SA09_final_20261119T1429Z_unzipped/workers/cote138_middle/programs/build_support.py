#!/usr/bin/env python3
"""Serialize manually authored problem, reading, and link records."""
import csv,json
from pathlib import Path
OUT=Path(__file__).resolve().parents[1]
problems=[]; readings=[]; links=[]
def problem(n,title,occ,his,today,art,why,worth,refs):
    problems.append(dict(id=f'MP-SA09-{n:02}',title=title,occurrences=occ,as_he_states=his,plausible_today=today,state_of_art=art,why_open=why,worth=worth,refs=refs))
def reading(scan,line,current,alternative,evidence,weight='high',confidence='high mathematical evidence; ink undecided'):
    readings.append(dict(cote='138',scan=str(scan),line='MPL_138_046-089_transcription.tex:'+line,reading=current,alternative=alternative,evidence=evidence,weight=weight,confidence=confidence))
def link(kind,fr,to,what,evidence,notes):
    links.append(dict(kind=kind,**{'from':fr,'to':to},what=what,evidence=evidence,note_ids=';'.join('MPL_138_046-089#'+str(n) for n in notes)))

problem(100,'Rational coordinates for odd conic powers',
 ['138/49 lines158–174','138/51 lines371–381','138/55 lines522–561','SA09-212','CL-SA09-138M-004'],
 'The source asks whether the displayedx′,y′,z′ are rational functions ofx,y,z, suggestsz′=z^n, and labelsn odd in the related diagram.',
 'ForC/Q:x²+y²+z²=0 andu=(y−ix)/z overQ(i), the power mapu↦u^n descends exactly for oddn; its homogeneous formula is(A_n:B_n:z^n), with(y−ix)^n=B_n−iA_n.',
 'Solved for this family by the independent norm/descent proof and exact computations in proof_audit.md §2. The surrounding descent framework is classical(SGA1 VIII); Faber supplies the conic/PGL₂ context. No first publication of the exact coordinate question was identified.',
 'The pages leave the field/model switch unstated; there is no evidence explaining why the author did not finish the written verification.',
 'Worth one short editorial task: write the all-odd formula and mark the split-field and rational-field domains explicitly; there is no unresolved theorem in this specified family.',
 ['M-SGA1','M-Faber2011'])
problem(101,'Unresolved slot in the roots-of-unity tower',
 ['138/53 lines467–494','138/54 lines496–518','SA09-216','CL-SA09-138M-007'],
 'A question mark occupies the third slot after correspondences involving0′,1′,∞′ in a crowded covering diagram.',
 'No strongest theorem can be stated until the arrows, domains and intended relation in that slot are recovered; the elementary quotientΠ_n=μ_n³/μ_n≅μ_n² is certain.',
 'SGA1 V/IX and the explicit Fermat/dihedral calculations give a standard covering-theoretic framework but do not identify this missing assertion. The literature search therefore has an F outcome, not an unresolved named conjecture.',
 'The scope of the question is absent from the supplied diplomatic text; no historical reason for abandonment is given.',
 'Worth a scan-first reconstruction task because the tower connects several explicit families, but not a speculative theorem-development run before the arrows are known.',
 ['M-SGA1'])
problem(102,'Normalizer of the two-object graph action',
 ['138/62 lines802–825','138/63 lines827–829','SA09-220','CL-SA09-138M-012'],
 'The source replaces “commutant” by “normalisateur deG” after describing a two-vertex multiedge graph and a transitive action on its two objects.',
 'Specify the actingG, its relation to the earlier polygon groupD, and whether the normalizer lies in graph, groupoid or profinite outer automorphisms; then compute that particular normalizer.',
 'The root/ray formula in GAP Groupoids §6 makes the finite groupoid case explicit, but it is not a theorem about an unspecified profinite mapping-class normalizer. The exact manuscript target remains unidentifiable.',
 'The text changes both the operation to compute and the group letter, then stops; no reason beyond this unfinished revision is documented.',
 'Worth a few-hour task after checkingD/G on the scans: the connected groupoid coordinate model makes small finite examples directly computable.',
 ['M-GAPGroupoids2026','M-FarbMargalit2012'])
problem(103,'Finish the four-branch-point tame exclusion',
 ['138/66 lines956–961','138/68 lines1035–1047','SA09-222','CL-SA09-138M-015'],
 'The source starts the case with at least four branch points and returns to the inequality on68; the latter contains a weak sign alongside the strict formula.',
 'For a tame GaloisP¹-cover over an algebraically closed field, eachd_i≥2 givesΣ(1−1/d_i)≥2 when there are at least four branch points, contrary to2/N>0.',
 'Closed by the elementary Riemann–Hurwitz argument, matched to Faber §5 and Stacks §53.12. The finite signature enumeration is supplementary only.',
 'The interruption and sign discrepancy are visible, but no reason for dropping the computation is stated.',
 'Worth completing in the commentary, with the strict sign explained; no new research theorem is needed.',
 ['M-Faber2011','M-Stacks0C1B'])
problem(104,'Genus zero after the cancelled quadratic Kummer reduction',
 ['138/68 lines1067–1072','SA09-225','CL-SA09-138M-018'],
 'Inside a wholly cancelled paragraph, the author leaves a verification ofgenus(X′)=0 and writes“facile”.',
 'For the concrete tame dihedral model, take the connected components of the normalization after the indicated quadratic base change; each is rational. An arbitrary wild-cover version requires a different statement.',
 'The exact factorization(w−z)(w−z⁻¹) proves the specified case in this run. Faber’s tame classification and Stacks Riemann–Hurwitz explain the hypotheses; neither supports extending it to the whole cancelled wild draft.',
 'The surrounding argument is cancelled; the pages do not explain whether this step or another issue caused the cancellation.',
 'Worth a short commentary calculation with the two components shown, while retaining the withdrawn status of the larger argument.',
 ['M-Faber2011','M-Stacks0C1B'])
problem(105,'Pass from marked groupoid objects to additional punctures',
 ['138/72 lines1167–1168','138/73 lines1170–1174','138/74 lines1178–1180','SA09-227','CL-SA09-138M-020'],
 '“On devra expliciter” the passage between the two descriptions: deletedpointsS and groupoidobjectsJ.',
 'For finite disjointS,J in a compact oriented surface, construct the comparison withX−(S∪J), retaining the filling morphisms and peripheral data needed to recover the marked groupoid onJ.',
 'Farb–Margalit §4.2 establishes the finite point-pushing/filling framework; Theorem8.8 gives the peripheral mapping-class comparison. The whole proposed functorial∞-groupoid presentation is not contained in those individual results.',
 'The author explicitly defers the construction. No external source documents a reason it was left unwritten in this packet.',
 'Worth one focused run to spell out the functor and its hypotheses; do not replace the source’s unspecified discrete-set convention by an unannounced infinite-set theorem.',
 ['M-FarbMargalit2012'])
problem(106,'Marked ∞-isotopy and the annulus/torus exceptions',
 ['138/74 lines1210–1213','138/75 lines1215–1236','SA09-229','CL-SA09-138M-022'],
 'The source proposes an∞-isotopic description using a nonempty marked groupoid and adds“vérifier”, after naming theK(Z,1) andK(Z²,1) exceptions.',
 'With finite markings, pointwise fixation and the usual compact-open topology, each relevant identity component has trivial higher homotopy once the annulus/torus rotation-translation exception is removed by a marked point. Mapping-class components remain separate.',
 'Hamstrom1974 Theorem1.5.2, Gramain1973/1974 Theorem1 and Remarks, and Farb–Margalit Theorem1.14, §4.2, Theorems8.1/8.8 give the precise ordinary-surface framework. The evaluation-fibration deduction is recorded separately in proof_audit.md §6.',
 'Only a verification flag is present. Nothing states that an operator-fixed subgroup has the same homotopy type, or explains a later abandonment.',
 'Worth a precise finite-marking reformulation; an equivariant centralizer version is a separate task and must not be inferred from the ordinary theorem.',
 ['M-Hamstrom1974','M-Gramain1974','M-FarbMargalit2012'])
problem(107,'Repair the proposed reversal without confusing Aut and Out',
 ['138/85 lines1571–1590','SA09-242','CL-SA09-138M-029','CL-SA09-138M-030'],
 'A naive reverse tuple is cancelled; a conjugated one is inserted with“vérifier?” and an unresolved0|1 lower index.',
 'Determine which index is written. Under the relation-preserving lower1 reading, the displayed lift squares toInn(λ₀⁻¹), while its outer class is involutive. A different strict lift, if desired, is a separate choice problem.',
 'The exact word problem is settled conditionally here for allν by telescoping and independently checked through rank9. Dehn–Nielsen–Baer and Guillot’sGT presentation explain the established outer context; they do not choose the ink.',
 'The source itself flags the repaired tuple. No evidence says that failure of strict order2 led to abandoning the construction.',
 'High-value short scan-and-algebra task: decide the lower index, record the inner defect, and compare an explicitly chosen based lift if needed.',
 ['M-FarbMargalit2012','M-Guillot2014'])
problem(108,'Canonical comparisons of the groups Tν!',
 ['138/87 lines1655–1662','SA09-247','CL-SA09-138M-032','CL-SA09-138M-033','CL-SA09-138M-034'],
 'The author would like canonical isomorphismsT₂!≅T₂^(S₃) andT₂!≅Tν!, with a marginalquestionmark and an interrupted generalisation.',
 'First specify the tilded/pure groups and actual comparison morphisms; test which family of automorphisms is compatible with puncture filling, finite covers and the required higher relations. Equality withG_Q is not a consequence of similar definitions.',
 'Guillot§5.6 identifies a precise rank2centralizer withGT₀; fullGT additionally requires a pentagon. Collas2026 §§2–4 gives higher-levelGT and BGT constructions with explicit added hypotheses. Bortnovskyi etal.2026 settles specifieddihedralquotients, not unrestrictedcross-rank equality.',
 'The packet stops during the proposed extension. Later sources show that compatibility conditions become essential, but they do not establish why this particular draft stopped.',
 'High-interest, moderate short-run tractability: a few hours can settle a dictionary and produce one compatibility test, not the full arithmetic-image problem.',
 ['M-Guillot2014','M-Collas2026','M-BDHPE2026','M-Grothendieck1984'])
problem(109,'Structure of the peripheral outer quotient',
 ['138/89 lines1703–1724','continuation138/90 lines4–48','SA09-247','CL-SA09-138M-025','CL-SA09-138M-035'],
 'After definingΓν=Aν/Fhat_ν and proving inner normality, the author says“on veut élucider sa structure”. The following leaf asks more specific discrete-image normality/equality questions.',
 'Separate the full peripheral outer group, its multiplier kernel, the closure/completion of the pure mapping-class image, and the arithmetic subgroup. Investigate each comparison with its actual map.',
 'The specific normality/equality questions are consolidated with the late-package problemsMP-SA09-70ff. SGA1 and Belyi establish the arithmetic action; Guillot and Collas show substantial later structure under extra relations. These do not identify the entireΓν.',
 'This is a continuing research aim, not a failed proof; the continuation is supplied in the next package and is part of the dossier.',
 'Worth developing only after the notation is fixed and the already refuted equalities and non-normality cases in the late-package audit are removed.',
 ['M-SGA1','M-Belyi1980','M-Guillot2014','M-Collas2026'])

reading(47,'58–60','μ∞ inD∞, with no transition maps','Specify inverse-systemμ_n with power maps, or distinguish the torsion direct limit','138/81 lines1460–1464 explicitly useslim μ_n; these limits have different torsion/topological properties. The comparison does not choose an earlier convention.','medium')
reading(49,'175–184','Doubtful corrected coefficient9/3 in cubic expansion','Coefficient3 inx⁴y² andx²y⁴ terms','Exact polynomial expansion in computations.json; changing the coefficient changes divisibility by the conic equation.')
reading(51,'311–381','Positive conic next to(1−t²,2t,1+t²)','Minus sign beforez² for the parametrized model, or an explicitz↦iz model change overQ(i)','Substitution gives positive-form2(1+t²)² and negative-form0; theQ-conics are not isomorphic.','critical')
reading(51,'341–381','Same lettert used in a parametrisation and a later ratio/trigonometric expression','Distinguish parametrisation variable from the projective ratioy/x and identify source/target chart','The inverse of the split parametrisation is not simplyy/x. No algebraic inconsistency licenses changingtwithout the diagram.','medium','medium; domains and ink undecided')
reading(55,'522–561','Doubtful signs inA_n,B_n and cubic coordinates','Choose signs consistently with(y−ix)^n=B_n−iA_n, conditional on that coordinate','The norm identity and cubic test determine a consistent family, but changingconjugatecoordinate also changes signs.','high','medium; several coordinate conventions remain possible')
reading(49,'195–216','λ=p′/q′ without a written nonzero condition','Retainp′−λq′=0, or supplyq′≠0 where division is used','p=x²,q=1 at0 is critical andq′=0; a missing qualifier or an abandoned division should be checked.')
reading(53,'467–493','Doubtful arrows/equalities and a barequestionmark','Recover arrow directions and identify the object in the third slot','A covering/torsor problem cannot be specified merely from therank-two quotientΠ_n.','high','low ink confidence; exact theorem unidentified')
reading(61,'763–783','Equivalence criterion using only components and vertex groups with earlier targetcategory','A target-groupoid qualifier, or the omitted invertibility/full-Hom conditions of59','Finite one-object monoid{0,1} counterexample satisfies the abbreviated tests but is not fully faithful.','critical')
reading(60,'731–759','Connectedness only in a deleted setup before liveAut formulas','Check cancellation boundary or an intended live connectedness assumption','A disconnected groupoid with isotropy1 andC₂ cannot realize the object swap.','critical')
reading(62,'802–825','Polygon groupD followed byG acting transitively on two objects','An explicit identificationG=D, orG enlarged by vertex swap','The described polygon action on edges need not swap the two graph vertices; transitivity is an extra action datum.','high','medium mathematical diagnosis; group meaning unresolved')
reading(64,'859–863','Doubtful0|1 index inrho definition','Index giving composable bijection transitions whose product telescopes','The typesE±→D_ij must match. Computation checks cancellation conditionally, not the written subscript.','high','medium; conditional on six bijections')
reading(68,'1035–1047','A weak inequality beside the strict2/N>0 argument','Strictpositive inequality retained throughout the spherical exclusion','Fourbranchpoints each contributeat least1/2; a weakinequality admitsEuclideansignatures and doesnotprove impossibility.')
reading(68,'1049–1065','inséparable inside the cancelled finite-group quotient discussion','séparable, or a different explicitly delimited scope for the adjective','Translationquotientx↦x^p−x has derivative−1 and isGalois; group fixed-fieldextensions areseparable.','critical','high conditional obstruction; low ink certainty')
reading(68,'1055–1065','Doubtful2 versusp in an elementaryabelianp-group description','p in(C_p)^r for the finitep-subgroup','FaberLemma4.3: a finitep-subgroup is a translationF_p-vectorspace;C₂ onlywhenp=2. Entireblockcancelled.','high','high conditional mathematics; ink undecided')
reading(68,'1067–1072','kummérienne/non kummérienne and a genus-zero assertion within deletion','Identify the quadratic tame basechange and its connected normalization component','The explicitdihedralfibreproduct splitsinto twocomponents. A silent connectedness assumption changes the genus claim.','high','medium; cancelled scope uncertain')
reading(74,'1200–1209','Rank-oneT isomorphic to the whole(Λ²H₁)dual','An alternating form/invariant subline or a different arrow, to be decided visually','RankΛ²H₁=g(2g−1)>1 forg≥2; genus1doesnotrepair generalstatement.','critical')
reading(75,'1221–1228','à bouts/à bout','Possibleàlacets abbreviation; retainliteralalternatives','PeripheralHomext(T,π) structures match groupsàlacets in the openedLM§13discussion; linguistic ink remains undecided.','medium','low ink confidence; high object-level identification')
reading(76,'1238–1241','groupesprolibres/problèmesspéciaux','Quelquesproblèmesspéciaux is an earliermodernizer’s proposal','Later80and89define specialprofinitegroups, but neighbouringmath cannot determine titlewords.','low','low; no mathematical emendation')
reading(77,'1285','σ₀σ₂=σ₂σ₀=(s″,f″), where1279alsoassignsσ₂(s,f)=(s″,f″)','A distinctflag on the right, or different indices/bars','Ifσ₂isinvertible, literalσ₀σ₂=σ₂forcesσ₀=id; this degenerates the ordinaryflaginterpretation.','critical','high conditional algebra; drawing interpretation uncertain')
reading(77,'1310–1312','Doubtfulbars, f₁/f₂ and underlines inσ_i formulas','Restore the three distinctcoordinate-changing involutions according to incidence types','The fibreproduct condition must be preserved; without correctindices the maps neednotlandinE.','high','medium; requires scan and intendedflagconvention')
reading(80,'1398;1440–1443','ν≥1 followed by injective inneraction','ν≥2, as explicitly requiredon89, orInn(π) instead ofπ','Atν=1,π=Zhat and inneractioniszero. Scan90inherits89’sν≥2, so no freshmissingrangealarmthere.','critical')
reading(81,'1446–1449','ProseΓν° but displayedΓν asAν°/π','CircledΓν° in the display','The precedingdefinition fixes the quotient; the uncircledgroup also carries the puncturepermutation quotient.')
reading(83,'1510–1511','π₁(k₀/k) in the arithmeticextension','Check ordering/notation forGal(k/k₀)','SGA1IX6.1 and the immediately precedingΓ=Gal(k/k₀) identify the expectedquotient; no newconventionisdefined.','medium')
reading(84,'1541–1546','Γ→μ_n≅Z/n for the root-permutationaction','Γ→Aut(μ_n)≅(Z/n)×','Exponent2onμ₅is1+4cycle, nottranslation5cycle; scan85alreadyhasχ_nintounits.','critical')
reading(85,'1586','q_i=λ_(0|1)…λ_(i−1)','Lower1 preserves the product relation; lower0doesnot','Exactfreereduction and all-rank telescoping prove the distinction. The lower1lift stillsquares toaninnerautomorphism.','critical')
reading(85,'1604','iν/tν ambiguity in a compatibilityformula','Check whichmaphas the domain required by the neighbouringdihedralidentity','The arithmeticembedding and the geometricinvolution are differenttypes; replacingonewiththeotherchangesmeaning.','high','medium; typecheck only')
reading(86,'1611–1624','Tν!subgroupofuntildedTν','Tildedambientgroup if puncturepermutationsare retained','Forμ_n,rationalGaloisactionsusuallypermutepunctures; pureambient plusallcyclotomicunits conflictswithcompatibility.','critical')
reading('81–87','1444–1662','Γ andscriptT, circles, tildes and!vary','Keepglyphs; build a separate definitiondictionary ratherthan uniformreplacement','Differentgroups are definedandmodernizerexplicitlynormalizesletters; alphabetic resemblance cannot certify group equality.','high','high scope evidence; no ink judgment')
reading(89,'1669–1679','T/L for rank-one module and choicee','Keep the rank-one Tate module distinct from the freegroupLν','Typecheckingrequires e∈(rank-one module)× whileλ_i∈freegroup; eitherlettercanbechosen onlyafterinkreview.','medium','medium; semantics fixed, glyph undecided')

link('folder','138/49 lines158–184','138/55 lines546–561','Same cubic self-map of the positiveconic','Both coordinate triples were read and independently substituted; the later occurrence repeats the earlier computation.',[5,6,9])
link('folder','138/47 lines34–65','138/68 lines1067–1072','Concrete dihedral model explains the cancelled quadratic Kummer genus test','Both sourcepassages read; exactfibreproductfactorizationchecks the specifiedmodelonly.',[3,19])
link('folder','138/58–59 lines654–727','138/61 lines763–783','Targetcategory qualifier is lost in the abbreviated equivalence criterion','Bothendsread; finite monoid counterexample shows why the omissionmatters.',[11,12])
link('folder','138/60 lines731–759','138/61–62 lines786–796','Connectedness cancellation affects the ensuing automorphism sequence','Bothendsread; disconnectedisotropycounterexampletested.',[13])
link('folder','138/64 lines831–878','138/77–78 lines1243–1333','Two signed flag diagrams and product-one permutations','Bothendsread; formalbijectionidentitychecked but doubtfulindices kept.',[15,27])
link('folder','138/80–81 lines1397–1445','138/89–90 lines1673–1724; latefilelines4–48','Rank restriction and continuity of the specialprofinite/discrete comparison','Bothendsread;89suppliesν≥2to90, while81stillhasrank1counterexample.',[29,30,41])
link('folder','138/83–84 lines1499–1546','138/85 lines1591–1605','Rootaction target versuscyclotomicunitformula','Bothendsread; exactμ₅permutationdistinguisheddifferentactions.',[33,35,38])
link('published work','138/83 lines1496–1514','SGA1 IX, Théorème6.1, originalp253; re-editionp195','Arithmeticfundamentalexactsequence andoutertransport','OpenedfullSGA1PDF; theoremhypothesisquasi-compact/geometricallyconnectedchecked. Inertialmultiplierproved separatelybylocalKummercalculation.',[32,33])
link('published work','138/64,77–78; lines831–878,1243–1380','Esquisse §3, printedpp13–17','Cartographicdictionary versusconcreteincidenceandcoverexamples','Bothsourcesread; Esquisse explicitlystates broaderdictionaryandBelyiconverse; presentpacketdoesnot.',[15,27,28,43])
link('published work','138/83,87; lines1499–1514,1653','Esquisse §2, printedpp9–10','Arithmeticouteraction versuslaterfaithfulnessassertion','Bothsourcesread; localarrowisnotlabelledinjective; Esquisseassertsfaithfulness alreadyonthetriplypuncturedline.',[33,40,42])
link('published work','138/87 lines1655–1662','Esquisse §2, printedpp9–10; §4, printedpp18–20','Compatibilityprogramme andstructurequestion','Bothsourcesread; laterprogrammecontainssewing/fillingconditionsandexactimagequestions, notaretroactiveproof ofTν!identifications.',[41,46])
link('our projects','138/74–75 lines1195–1236','PublicCarmona–Künzer LMtranscription, §13, printedp45; §§20–24 headingsonly','Verifiedpublicmanuscript comparison, distinctfromabsentprojectreports','OpenedpublicPDF: §13givesorientationH²datum; §§20–24arelargelyunfilledheadings, so they do notverifytheearlierrun’sequivariantproofclaims.',[22,23,24,25])
link('our projects','138/83,87 lines1499–1514,1653','PublicCarmona–Künzer LMtranscription, §35, printedpp150–155','Verifiedlaterfaithfulnessstatementwithitsownproofdependencies','Opened§35Theorem1andfootnote “Démontrémodulolelemme2”; this supportscomparisonofsourceclaims, notacertificateofeveryLMproof.',[42])
link('our projects','138/78 lines1365–1380','PublicCarmona–Künzer LMtranscription, §37, printedpp184–190','VerifiedS₃orbit/j-quotientcomparison supportingtheearlierrun’scandidateR','Bothsourceobjectsread; quotientfibres0,1,∞/−1,1/2,2/twosixthrootsmatchup tobase-normalization. R remainsareconstruction, notwrittenon78.',[28])
link('our projects','SA09-209,SA09-210,SA09-238–250; source138/46–55,80–89','EXIT_TOWER E.24,E.23,E.35,E.36,E.39,E.45; notes/RESULTS_STATE.md; README B6','Reportedleads about arithmeticimageandlabelledtowercompatibility','Earliernotes’endverified; namedresearchreturns/register notsupplied. Theirreported “Open/Proved” statuses are not adopted asresults. No assertionthat both research endpointswereinspected.',[1,3,4,30,32,33,34,35,39,40,41,42,44,46])
link('our projects','138/62,66–75,85','LM4 C.12,D.12,F.7; LM4_SUCCESSOR B.38,B.39; EXIT_TOWER B.27','Reportedoperator, torsion,polyhedron andcentralizercomparison leads','Onlysourceandearliernoteendavailable; currentpagescontainordinarygroupoids,tametypesandreversal, notthereportedfullcomparisonproofs.',[14,16,17,20,23,24,36,38])
link('our projects','138/46,53,55; SA09-210,SA09-212,SA09-253','LM7_PUSH E.58,E.65,E.3; EXIT_TOWER E.49; LM6 A.22','ReportedCM-character, pronilpotentliftingandresidualprocyclicnormalizerleads','Namedreturnsabsent. EarliernotereportsE.58/E.65asrefereed,E.3open,E.49unrefereed; theseareprovenancereports only. Explicitconic/Fermatcalculationsdonotdecide them.',[4,6,47])
link('our projects','138/64,77,87; SA09-221,SA09-233,SA09-247','MPL_147_003-047 N075; WG2 §1.7 #10 and §Summary #1; INTAKE 20261114 §11.2; WG H5','Reportedhighercompatibility,cote145centralizerandcongruenceleads','Cotes145/147andnamedworkingreturnsarenotattached; publicEsquisse/GTcomparisonisverifiedseparately. Theseentriesremainleads,notresults.',[33,40,41,46])
link('our projects','Allmiddlepacketitems, especiallySA09-207','hua_project/138.modern.tex andcontextLM_140-1_text.tex throughLM_140-4_text.tex','Earlier-runcontextprovenanceandeditorialnormalizations','The notes explicitlyname thesefiles; originalsarenotattached. PublicHua2026paperandpublicLMtranscriptionarenotassumedidentical tothesecontextversions.',[1,2,5,7,12,22,26,31,34,35,39,45])

(OUT/'problems.json').write_text(json.dumps(problems,ensure_ascii=False,indent=2)+'\n')
for name,rows,fields in [('readings.tsv',readings,['cote','scan','line','reading','alternative','evidence','weight','confidence']),('links.tsv',links,['kind','from','to','what','evidence','note_ids'])]:
    with(OUT/name).open('w') as f:
        w=csv.DictWriter(f,fieldnames=fields,delimiter='\t');w.writeheader();w.writerows(rows)
print(json.dumps({'problems':len(problems),'readings':len(readings),'links':len(links)}))
