"""Manual subject/clause correspondence; scripts only attach already-read locators."""
from pathlib import Path
import json,csv
P=Path(__file__).parent;H=P.parent/'hyperplanes'
fc={x['id']:x for x in json.loads((P/'claims.json').read_text())};hc={x['id']:x for x in json.loads((H/'claims.json').read_text())}
fp={x['id']:x for x in json.loads((P/'problems.json').read_text())};hp={x['id']:x for x in json.loads((H/'problems.json').read_text())}
rows=[];editor_rows=[]
ed={x['original_id']:x for x in json.loads((P/'editorial_tasks.json').read_text())} if (P/'editorial_tasks.json').exists() else {}
hed={x['original_id']:x for x in json.loads((H/'editorial_tasks.json').read_text())} if (H/'editorial_tasks.json').exists() else {}
def add(kind,source,targets,relation,action,scope,reason):
 prefix={'claim':('C-SA23-forms-','C-SA23-hyp-',3),'item':('SA23-','SA23-',0),'problem':('MP-SA23-forms-','MP-SA23-hyp-',2)}[kind]
 def sid(x,pre):return pre+(str(x).zfill(prefix[2]) if str(x).isdigit() else str(x))
 src=sid(source,prefix[0]);tgs=[sid(x,prefix[1]) for x in targets]
 d={'kind':kind,'source':src,'targets':tgs,'relation':relation,'action':action,'scope':scope,'reason':reason,'decision_basis':'Manual mathematical comparison of the fully read Blass witness with root’s fully read cote25 witness; exact source clauses and discrepancies retained.'}
 if kind=='claim':
  d['source_location']={'cote':fc[src]['cote'],'scans':fc[src]['scans'],'lines':fc[src]['lines']}
  d['target_locations']=[{'id':t,'cote':hc[t]['cote'],'scans':hc[t]['scans'],'lines':hc[t]['lines']} for t in tgs]
 elif kind=='problem':
  q=fp.get(src,ed.get(src));d['source_occurrences']=q['occurrences']
  live=[t for t in tgs if t in hp];editorial=[t for t in tgs if t in hed]
  assert len(live)+len(editorial)==len(tgs),(src,tgs)
  def target_claims(t):
   a=hp.get(t,hed.get(t));return a.get('claims',[x.get('claim') for x in a.get('occurrences',[])])
  d['target_claims']={t:target_claims(t) for t in tgs}
  if src in ed:
   d['source']=ed[src]['id'];d['original_id']=src;d['kind']='editorial association'
   d['targets']=live+[hed[t]['id'] for t in editorial]
   d['former_target_ids']=editorial
   d['target_claims']={hed[t]['id'] if t in hed else t:target_claims(t) for t in tgs}
   d['relation']='editorial comparison of related source assertions or requests'
   d['action']='keep outside authorial problem index; no MP merge'
   editor_rows.append(d);return
  if editorial:
   # Different provenance in the two witnesses must not turn an asserted
   # counterpart into an authorial question or create an MP→ED merger.
   assoc=dict(d);assoc['kind']='editorial association';assoc['targets']=[hed[t]['id'] for t in editorial]
   assoc['former_target_ids']=editorial;assoc['action']='related editorial counterpart only; no MP merge'
   assoc['relation']='authorial source request with editorial counterpart in other witness'
   assoc['target_claims']={hed[t]['id']:target_claims(t) for t in editorial};editor_rows.append(assoc)
   d['targets']=live;d['target_claims']={t:target_claims(t) for t in live}
   if not live:
    d['relation']='no matching authorial question established in cote25';d['action']='keep distinct'
 rows.append(d)
# Each row below is a deliberate assessment. R-suffix targets are modern refinements,
# never additional witnesses of the manuscript's wording.
add('claim',1,[1],'same assertion','merge','universal hyperplane, incidence and projective convention','Same functor, base-change and incidence construction; retain both source line ranges.')
add('claim',2,[60],'same divisor functor with later corrected witness','merge, retaining different erroneous displays','degree-d relative effective Cartier divisor parameter','Directly read cote25 scans106–107 physical4235–4310: Proposition2.2 andCorollaries2.3–2.4 give P((Sym^dE)^vee). Blass has P(Sym^dE), while early cote25 has Sym^d(E^vee); neither mistaken formula is silently made equal to the correction.')
add('claim',3,[2,3],'compound repeated assertion','merge by clause','generic irreducibility; closed-point/finite-image emptiness test','Forms combines two independently stated propositions which cote25 separates. No hypothesis is transferred between them.')
add('claim',4,[4,'004R',5],'compound repeated assertion with refinement','merge by clause','Corollary2.4 equality/containment; component dimension clause','Both witnesses have the invisible-component issue.004R is the present-run corrected irreducibility formulation;005 receives only the dimension/component clause.')
add('claim',5,[5,6],'compound repeated assertion','merge by clause','associated supports; depth/codepth and Serre comparisons','Same generic-incidence argument; preserve uncertainty over historical module terminology and all geometric assumptions.')
add('claim',6,[7,8,'008R'],'theorem and faulty proof shortcut repeated','merge by clause','Bertini smoothness; generic linear combination; incidence repair','The true theorem, false shortcut and present-run repair must remain distinguished in the canonical records.')
add('claim',7,[9],'same assertion','merge','Bertini–Zariski and primary-field lemma','Same image-dimension and geometric irreducibility assumptions, including outsourced field lemma.')
add('claim',8,[10],'same assertion','merge','component-chain connectedness','Both use removal of finite-image closed subsets and image dimension at least2 on every component.')
add('claim',9,[11],'same assertion','merge','constructibility and open good-parameter loci','Same passage organizing local properties. Exact EGA openness assumptions remain in the source records rather than treating every listed property uniformly.')
add('claim',10,[12],'same corrected assertion','merge','C_m generic-section correction','Both explicitly correct the arbitrary-morphism statement by quasi-finiteness/image dimension.')
add('claim',11,[13],'same assertion','merge','fiberwise regularity and relative Bertini lists','Same flat module, regular section and missing-property-list problem.')
add('claim',12,[15],'same assertion','merge','proper connectedness of every hyperplane section','Both add properness and retain the component/image hypotheses. The present-run Stein proof permits a purely inseparable generic extension.')
add('claim',13,[16],'same assertion','merge','rational parameters, residue extension and iterated cuts','Same infinite/finite residue-field choices. Retain finite etale over a Zariski neighborhood, which is stronger than merely an etale neighborhood.')
add('claim',14,[17],'same contradictory pair','merge','Proposition7.4 versus Remark7.5','Both properness formulations conflict with the explicit projectivity qualification; cancellation extent differs and remains visible.')
add('claim',15,[18,'018R'],'same assertion with refinement','merge by clause','nonregular locus codimension and depth shift','Both need codimension at least2, not equality2, and distinguish S_k→S_(k−1) from preservation of the same S_k.')
add('claim',16,[18],'independently stated subclaim of common passage','keep atomic; associate','8.3 non-CM surface and depth2 normal-threefold examples','Cote25 physical1344–1379 contains these examples inside the broad018 source span, but its canonical statement does not separately assert them. Keep this atomic claim unless root explicitly splits that target.')
add('claim',17,[19,'019R'],'same assertion with refinement','merge by clause','codimension drop and missing component clause','Same local-lemma variable problem and component conditions; refinements do not repair the ink.')
add('claim',18,[20],'strict specialization with damaged hypotheses','keep qualified variant','same-S_k criterion for finite versus quasi-finite f','Blass says finite in the simplified formulation; cote25 says quasi-finite. Their depth threshold agrees, but the quantifier difference must survive.')
add('claim',19,[21],'same construction','merge','conormal incidence and Euler sequence','Same smooth/unramified relative setup and incidence dimension. Published result is Katz-authored, classB.')
add('claim',20,[21,22,78,29],'criterion plus cross-witness correction','keep atomic; crosslink','ordinary versus nonsupersingular Hessian condition','The exact polar criterion occurs in021/022, but078 and029 carry distinct later corrections. Cote25 scans139–141 are early definitions; scans158–160 contain the explicit smooth tangent-quadric correction. Do not merge all these propositions solely by topic.')
add('claim',21,[22],'same embedded assertion; wider translated scope','merge shared clause, retain qualification','embedded reflexivity and smooth-dual locus','The immersed theorem is repeated. Forms separately checks that a merely unramified map can have higher conormal degree via an etale isogeny; preserve that extra reconstruction and do not weaken the target hypotheses.')
add('claim',22,[23],'same characteristic-zero and terminology assertion','merge shared clause, retain example','characteristic0 separability; rejected ruled terminology','The positive-characteristic Fermat example is the explicitly requested illustration. Preserve its scope separately from the characteristic0 theorem and from pencil existence.')
add('claim',23,[24],'same damaged criterion','merge','R_k, reducedness, normality and questioned converse','Both witnesses preserve the revised sufficient criterion and unresolved necessity question; neither supplies missing ink.')
add('claim',24,[25],'same assertion','merge','normal integral sections outside codimension2','Same properness, normality, depth and unramified-off-codimension2 hypotheses.')
add('claim',25,[28,'028R'],'same assertion with missing fixed-divisor hypothesis','merge by clause','fixed linear base and projection criterion','The moving-part theorem and fixed-divisor obstruction coincide. Preserve the corrected image-field and projection-dimension readings in forms.')
add('claim',26,[29,32,33],'compound synthesis with separability correction','merge by clause','Veronese separability clause; general/curve-pencil clauses','029 receives the overstrong separable-duality assertion and correction.032/033 receive only the explicit pencil existence clauses, not unrelated blowup details. Katz’s established ordinary-pencil theorem is classB.')
add('claim',27,[30],'same construction','merge','low-degree fixed-point and tangent-jet ratios','Same degree2/3 constructions and inherited base-locus assumptions.')
add('claim',28,[31],'same incomplete mathematical fragment','merge','blank9.4 and unfinished9.5','Both incomplete mathematical headings are classF. The heading is not repaired from a later theorem; this is not mere cover metadata.')
add('claim',29,[32],'independently stated subclaim of common passage','merge shared avoidance clause','closed bad-locus and generic pencil avoidance','Cote25’s compound032 includes this same clause. Preserve the translated constructible/closure ambiguity and its counterexample; the blowup clause is different.')
add('claim',30,[32],'same assertion','merge shared blowup clause','regular rank2 incidence equals blowup; deleted higher-rank exercise','Same regular-sequence/Rees argument. Preserve the separately cancelled10.3 and missing proof request.')
add('claim',31,[33],'same assertion','merge','generically etale curve pencil with simple/double fibers','Same sufficiently suitable degree and infinite-field requirements; ordinary double fibers in characteristic2 need not be tame.')
add('claim',32,[34,35,'035R'],'compound repeated assertion with false finiteness clause','merge by clause','Grassmann representability/Plucker; arbitrary-module quasi-compactness','034 receives representability;035 the source’s overstatement;035R the finite-rank correction. Do not count the refinement as manuscript authorship.')
add('claim',33,[34,37],'compound repeated assertion','merge by clause','finite-free affine charts; projective subspaces, duality and rational lifting','Separate finite-rank chart theorem from quotient/subspace and polarity statements; empty impossible-rank functors excluded.')
add('claim',81,[36,'036R'],'same chart with scope ambiguity','merge with all qualifiers','chosen-basis chart versus a general exact-sequence retraction functor','Both source contexts explicitly start with chosen basis decompositions. The canonical chart is valid relative to that choice. Local splitting is needed for a retraction torsor; no arbitrary-sequence falsehood is attributed to the source without qualification.')
add('claim',82,[26,'026R'],'same conjecture and counterexample','merge by clause','8.17(a) arbitrary-morphism codimension bound','Same dimension≥3 conjecture; Bl_p(P³) refutes it. Poonen–Slavov Th1.5/1.8 isolate equidimensional and fiber-jump refinements; these are distinct from the original conjecture.')
add('claim',83,[27],'independently stated surface clause','merge shared clause','8.17(b), at most two curve components and tangent quadric','027 combines this surface statement with8.18. Preserve the unreadable separability qualifier and do not identify it with the later iff criterion.')
add('claim',84,[27],'same finite-exceptional-set criterion','merge shared clause','8.18 iff and normalization sketch','Same finiteT witnesses and singular irreducible member. Preserve singular/nonsingular uncertainty, d−1 versus1 and the unproved normalization step.')
# Subject-level items can have more than one canonical target; mathematical claims remain clause-aware.
itemmap={801:[501,560],802:[502,503],803:[504,505],804:[505,506],805:[507,508],806:[509],807:[510],808:[511],809:[512],810:[513],811:[515],812:[516],813:[517],814:[518],815:[518],816:[519],817:[520],818:[521],819:[578,529],820:[522],821:[523],822:[524],823:[525],824:[528],825:[529,532,533],826:[530],827:[531],828:[532],829:[532],830:[533],831:[534,535],832:[534,536,537],833:[526],834:[527],835:[527]}
for a,b in itemmap.items():
 action='merge subject; preserve all claim scopes'
 if a in (815,817,819):action='associate subject; retain separate qualified/atomic item if needed'
 add('item',a,b,'same subject or explicitly identified subsubject',action,'See claim-level rows for exact scope.','Subject consolidation does not authorize merging unequal hypotheses or a later correction into the earlier wording.')
# Questions are mapped only where the actual authorial request agrees.
add('problem',5,[1],'same question','merge','reference/proof of primary-field lemma','Both outsource the same field lemma.')
add('problem',6,[3],'subquestion of common generalization','merge shared component-chain request','component-chain lemma','The general C_m problem includes this precise lemma; keep finite-image exceptional-family hypothesis.')
add('problem',7,[3],'same question','merge','C_m quasi-finite/image-dimension correction','Same authorial correction and request to generalize.')
add('problem',8,[4],'same question','merge','explicit relative-Bertini property lists','Same request for lists and references; no new theorem inferred.')
add('problem',9,[3],'subquestion of common generalization','merge shared proper-connectedness request','generalization following proper connectedness','Retain properness and all-section versus generic-section distinction.')
add('problem',10,[6],'related but different provenance','keep distinct','module qualifications in iteration','Blass explicitly requests module/geometric reservations; the nonprojective obstruction in cote25 is an asserted example now classified as an editorial task, not the same authorial question.')
add('problem',11,[6],'editorial counterpart','keep outside MP index','nonprojective finite-etale obstruction and cancellation','Both passages assert the conflicting scopes without posing a counterexample question. Preserve Blass’s explicit smoothness in the announced example; this remains an editorial verification and cancellation task.')
add('problem',14,[8],'related editorial counterpart','keep distinct','cleanup of codimension lemma','The mathematical defect is shared, but Blass explicitly comments on the faulty write-up whereas the cote25 proof-check record is editorial. No authorial-question alias is established.')
add('problem',15,[9],'same criterion with witness qualification','merge with finite/quasi-finite distinction','same-S_k and codepth strata','The depth criterion is common; finite versus quasi-finite scope remains separately displayed.')
add('problem',16,[10],'same question','merge','conormal/differential diagram verification','Same mechanical local comparison.')
add('problem',17,[53],'same correction problem across distinct witnesses','merge with all occurrences','ordinary versus nonsupersingular qualification','Keep early definitions139–141 separate from explicit correction158–160.')
add('problem',19,[13,14],'compound question','merge by clause','inseparable example; rejected terminology','Two independently identifiable requests correspond to two root questions.')
add('problem',20,[15],'same question','merge','necessity for R_k criterion','Same doubtful converse and possible extra assumptions.')
add('problem',22,[18],'same question','merge','fixed-base divisor and projection criterion','Same prescribed linear-base irreducibility question.')
add('problem',23,[19,12],'compound correction/pencil question','merge by clause','Veronese nonsupersingularity; general pencil formulation','The two clauses have different positive answers and must remain distinguished.')
add('problem',24,[20],'same question','merge','low-degree point/tangent-jet construction','Same degree2/3 argument.')
add('problem',25,[21],'same incomplete question','merge','missing9.4 and9.5 conclusion','No completed fundamental-group assertion is invented.')
add('problem',27,[22],'same question','merge','higher-rank regular-section/Rees exercise','Rank2 argument does not supply the omitted general proof.')
add('problem',28,[23],'same question','merge','Grassmann representability and finiteness','Same arbitrary-module versus finite-rank boundary.')
add('problem',29,[24],'same question','merge','intrinsic degree-one projective subspace criterion','Same announced later characterization.')
add('problem',63,[23],'subquestion of common chart problem','merge shared chart qualification','relative canonical origin of chart','Chosen basis is explicit in both; general exact-sequence extrapolation is separately qualified.')
add('problem',64,[16],'same conjecture','merge','arbitrary-morphism irreducibility bound','Exact counterexample and refined modern hypotheses coincide.')
add('problem',65,[17],'related surface clause; not the whole iff','keep separate subquestion','dual-map qualifier in8.17(b)','Root17 asks for8.18 iff. Unreadable surface qualifier is retained even though root027 groups both claims.')
add('problem',66,[17],'editorial counterpart','keep outside MP index','finite-exceptional-set iff and normalization','Both witnesses assert the criterion and omit normalization details. The actual following fixed-base question is forms22/hyp18; no independent normalization question is created.')
add('problem',3,[2],'same reference request','merge','local-property and singular-locus references','The explicit reference requests, rather than the present-run historical-word repair, justify this authorial alias.')
for n,scope in [(1,'deferred degree-d divisor functor'),(2,'Corollary2.4 missing irreducibility'),(4,'faulty Bertini proof shortcut'),(12,'unreadable first depth threshold'),(13,'missing8.3 footnote'),(18,'wider nonimmersion reflexivity formulation'),(21,'normality-bound proof'),(26,'constructible-set closure in pencil avoidance')]:
 add('problem',n,[],'no exact question alias established','keep distinct',scope,'A nearby shared claim does not by itself identify the authorial question. Preserve this source-specific request or reading alarm.')
obj={'date':'2026-11-19','author':'owner forms; manual mathematical assessments','instructions':'Merge only the stated clauses. Preserve every source_record, source hypothesis, correction status and present-run refinement. Empty targets mean no exact alias. Item associations do not override claim-level keep-distinct decisions. R-suffix targets are present-run reconstructions. Do not mutate owner files during integration.','rows':rows}
(P/'cote24_25_editorial_associations.json').write_text(json.dumps(editor_rows,ensure_ascii=False,indent=2)+'\n')
(P/'cote24_25_concordance.json').write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')
with (P/'cote24_25_concordance.tsv').open('w',newline='') as f:
 w=csv.writer(f,delimiter='\t');w.writerow(['kind','source','targets','relation','action','scope','reason'])
 for r in rows:w.writerow([r['kind'],r['source'],';'.join(r['targets']),r['relation'],r['action'],r['scope'],r['reason']])
print(len(rows),'manual concordance rows saved')
