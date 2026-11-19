"""Manual provenance review of every alleged open question; no keyword classification."""
from pathlib import Path
import json,copy,datetime
P=Path(__file__).parent
ps=json.loads((P/'problems.json').read_text());cs={c['id']:c for c in json.loads((P/'claims.json').read_text())}
# Also accept the separated final registers. This preserves the manual decisions
# when the provenance audit is rerun without rebuilding mathematical claims.
if (P/'editorial_tasks.json').exists():
 old={q['id']:copy.deepcopy(q) for q in ps if int(q['id'].rsplit('-',1)[1])<=67}
 for q in json.loads((P/'editorial_tasks.json').read_text()):
  oid=q['original_id']
  if oid not in old:
   x=copy.deepcopy(q);x['id']=oid;old[oid]=x
 ps=sorted(old.values(),key=lambda q:q['id'])
# Tuple: origin, source cue/reason, narrowly authorial question (when retained).
A='authorial question or deferred step';E='present-run editorial task';T='translator editorial request'
D={
1:(A,'Blass5–6: “We shall see that ... Div(P/S) is representable”; the next page proposes adding the determination as an example to§19.','Determine the relative effective-divisor functor of P(E), as promised for later exposition; the dual correction is this run’s reading alarm.'),
2:(E,'Corollary2.4 is asserted and argued; the irreducibility repair is this run’s counterexample, not an authorial question. The separate reference-needed cue in2.6 is not a cue for this question.',''),
3:(A,'Blass13–14: explicit “(ref)” placeholders in2.8 and “One must give the different references assuring that Z is closed” after2.11.','Supply the references for local module properties and the closedness/constructibility of the regular, normal and R_k loci. Undefined historical wording remains an editorial issue.'),
4:(E,'Theorem2.12 presents its argument as a proof; the missing incidence repair is diagnosed here, without a corresponding authorial doubt.',''),
5:(A,'Blass3.1.1 explicitly delegates the proof: “I leave it up to you”.','Locate and insert a proof of the primary-field lemma used in Bertini–Zariski.'),
6:(A,'Blass21: “a lemma that ought to appear in par.6 ... with Hartshorne’s theorem”.','State the component-chain characterization for deletion of finite-image closed subsets.'),
7:(A,'Blass25: “error in the statement”; Blass30–31 expressly asks to generalize the connectedness formulation.','Correct C_(m+1)→C_m by the actual image/quasi-finite hypotheses and formulate the broader connectedness statement.'),
8:(A,'Blass§5 expressly asks to locate references and provide the lists of properties in5.6–5.7.','Supply the exact relative-Bertini property lists and their references under the stated flatness assumptions.'),
9:(A,'Blass30–31: asks the recipient to carry out the generalization as an exercise, or at least mention it as a remark.','Generalize proper connectedness of all hyperplane sections to the stated dimension-sensitive connectedness conditions.'),
10:(A,'Blass32: “I must ... point out [un remords] ... should have been announced in a slightly more general form”;7.3 explicitly requires making the reservation.','Extend the construction to properties holding away from a dimension-bounded bad locus and state the module/geometric reservations in its iteration.'),
11:(E,'Blass35 physical1332–1338 asserts that examples can be given; it does not ask for one or promise a later proof. The only Ask AG in the adjacent7.4 passage is a translator request at1321. Identifying the nonprojective example is our editorial task.',''),
12:(T,'Blass37 explicitly asks “is it two ask Grothendieck” about an unreadable threshold.',''),
13:(T,'Blass38: “Footnote(?) Fairly illegible ask Grothendieck”; recovering five absent lines is the translator’s request.',''),
14:(A,'Blass41: “I am afraid that the write up is quite ... sloppy” because the argument used geometric points without saying so.','Clean up the geometric proof of the codimension criterion, preserving the component conditions.'),
15:(T,'Blass41–42 marks the missing Z_n definition and several words “Ask A.G”; the inequality corrections are present-run alarms.',''),
16:(A,'Blass47 says of the differential identification: “the verification ought to be essentially mechanical”.','Verify the displayed intrinsic differential identification giving the singular incidence scheme. Restoring illegible diagram labels remains editorial.'),
17:(E,'Blass8.7(b) asserts the ordinary-point equivalence; its characteristic2 repair is our source comparison. Cote25 has an authorial correction, but this Blass task is not itself his open question.',''),
18:(A,'Blass64: “One would have to announce8.8 in a manner such as not to exclude the case where f is not an immersion”.','Formulate the intended extension of8.8 for unramified maps without falsely carrying over embedded birationality.'),
19:(A,'Blass8.12 explicitly says the author is too lazy to construct the examples;8.17 retracts the chosen terminology.','Give the inseparable-duality examples and replace the rejected use of “ruled”.'),
20:(A,'Blass56: “I may have somewhat exaggerated the case R_k ... (S_1) and perhaps ... equidimensionality”.','Determine what additional assumptions make the questioned R_k necessity implication valid.'),
21:(E,'Proposition8.16 gives its argument; matching it to a modern source is our literature task, not an authorial question.',''),
22:(A,'Blass60: “we ask the question ... if ... Y is geometrically irreducible”; the variant is said to belong in§3.','Characterize geometric irreducibility of the generic section in a linear subsystem with a fixed linear base.'),
23:(A,'Blass66: “Finally we must combine the latter with9.2 in order to find a recapitulating theorem”.','Write the promised combined theorem for suitable Veronese sections and pencils; the later characteristic2 correction limits its possible wording.'),
24:(E,'Proposition9.3 supplies polynomial ratios; making inherited base-locus hypotheses explicit is our repair. An unassigned “???” does not establish that this particular request is authorial.',''),
25:(T,'Blass66 labels9.5 illegible and says “Ask Grothendieck”; recovering absent text is a translator/scan task. The actual deferred synthesis is MP23.',''),
26:(T,'Blass10.1 includes a translator correction and uncertain overbar; deciding the mark is editorial, not a distinct authorial mathematical question.',''),
27:(A,'Blass68 requests extraction of the general situation G→O_X; Blass70 says10.3 would belong with regular immersions.','State and prove the general regular-section lemma behind the pencil/blowup result; retain the cancelled10.3 separately.'),
28:(E,'The Grassmann representability and finiteness statements are asserted; the Plucker/exterior-power and quasi-compactness repairs are ours.',''),
29:(A,'Blass73 announces that the intrinsic smooth degree-one characterization will be given in a later chapter.','Give the promised intrinsic characterization of relative projective linear subspaces.'),
30:(E,'The naturality/coefficient formulation of the stated criterion is our clarification; the text credits the result to Quillen/Artin–Mazur. The independent presheaf-topos doubt is now MP67.',''),
31:(E,'The source’s Π and “Si!” corrections are retained in C036; reconciling copies is present editorial work, not a further authorial open question.',''),
32:(A,'Tapis4: “Je pense que ce résultat ... doit pouvoir se généraliser ainsi”; local homotopical triviality is then proposed.','Prove the proposed derived-local-system equivalence for the specified class of locally homotopically trivial topoi.'),
33:(A,'Tapis5: “J’ignore si on peut dans a) se borner aux systèmes locaux commutatifs”.','Can the homotopism criterion be restricted to abelian local coefficients, and what local-system-category hypothesis is retained?'),
34:(A,'The multiple-category discussion explicitly requests the relation between m-categories in n-Cat and the corresponding multiple simplicial objects.','Specify the globularity and Segal data in the proposed comparison.'),
35:(A,'Tapis8 records objections beside the commutative Picard assertion and deletes its strengthening.','Resolve the strict-commutativity obstruction identified in the withdrawn Picard claim; the commutative self-braiding invariant is essential.'),
36:(A,'Tapis10: “Il faudrait encore expliciter ... en termes d’un complexe RHom”; the general n statement is hoped for.','Specify the higher morphisms and RHom model for strict abelian higher categories.'),
37:(A,'Tapis9: “Demander à Quillen ... forment-ils des catégories équivalentes par le foncteur espace des lacets?”','Are connected pointed homotopy objects and group objects related by the stated loop-space equivalence?'),
38:(A,'Tapis10–11: “On suppose qu’on pourra ... tout cela dans un sens à préciser”; asks whether Quillen has a direct semisimplicial definition.','Define the proposed higher group completion and its K_i, distinguishing additive and abelian/exact inputs.'),
39:(A,'Tapis13: “ceci aussi devrait être formalisé au cas des correspondances générales”.','Formalize the correspondence universal property and its product/pullback/Gysin compatibility axioms.'),
40:(A,'Second Tapis witness45 inserts “il est douteux qu’il soit ... compatible avec multiplication” and question marks.','Does the Thom splitting admit the intended multiplicative section?'),
41:(A,'Second witness45: “Quillen ignore si ... le relèvement est compatible aussi avec les hom. de Gysin”.','Can the chosen splitting commute with the covariant Gysin maps?'),
42:(E,'Full faithfulness and shift/idempotent completion are asserted, not queried. Specifying compactness and shifts is our scope clarification. The actual later abelian-envelope expectation is MP68.',''),
43:(A,'Both copies explicitly ask “Pourquoi cette condition est-elle déjà nécessaire?” after the Steenrod-annihilation criterion.','Why should a submanifold class satisfy the stated Steenrod-annihilation condition?'),
44:(A,'Tapis17/48: “Quelle est la structure de G”; Quillen’s pro-nilpotent/pro-unipotent description is qualified.','Determine the structure of the dual Steenrod group G. Left/right convention repair is a present-run part of the answer.'),
45:(A,'Tapis17/48 explicitly doubts that the completion gives an abelian category or all finite-dimensional representations of G.','Does the completed geometric S-correspondence category realize all finite-dimensional graded representations of G?'),
46:(E,'Quillen’s positivity paper presents a completed proof; resolving the lower-order polynomial notation is our mathematical reading check.',''),
47:(A,'Quillen’s attached paper explicitly calls the etale argument incomplete and leaves the sphere-fibration construction conditional.','Complete the precise etale sphere-fibration/comparison step required for this potential proof of Adams. Source author: Daniel Quillen.'),
48:(E,'The prime-to-p completion argument is supplied conditionally; restating its obstruction hypotheses is our clarification.',''),
49:(A,'Quillen63: “We conjecture ... but ... will not need this fact”;64: “Let us assume that further analysis will show ...”.','Separate the stronger pro-sphere representability conjecture from the conditional rigidification/comparison actually required. Source author: Daniel Quillen.'),
50:(E,'Quillen65–67 proves conditional additivity and explicitly says the proof of C is complete. Locating later functorial rigidification belongs to the MP49 gap and historical commentary, not a new independent authorial open question.',''),
51:(E,'The final K0 lemma has a written proof; checking twist/dual signs is our reading task.',''),
52:(A,'Handwritten§1 explicitly asks whether the formal category is a formal groupoid.','Does the stated formal-category structure force inverses under its precise hypotheses?'),
53:(A,'Handwritten§1 says “suite à développer” after the distribution/differential-operator construction.','Develop the formal-category dual algebra and the indicated operator filtration.'),
54:(A,'Handwritten§2 margin explicitly says “dégager un lemme ...”; the claimed extension to a square-zero derivation is the surrounding subject.','Extract the precise exterior-differential lemma requested in the margin. The necessary degree1 square-zero condition is our correction, not a quotation from the page.'),
55:(A,'Handwritten bracket/Jacobi calculation: “Pourquoi zéro ??”.','Justify the Jacobi-zero step from the actual differential hypotheses.'),
56:(E,'“Th. de Quillen” is an attributed assertion without a local proof; no question or deferred-proof request is attached to that sentence. Identifying its exact source is this run’s literature task. The genuine crystalline reduction question is MP61.',''),
57:(A,'Handwritten§6: “À voir si ... il faut ... des relations ... puiss. divisées ... Δ”.','Specify compatibility of divided powers with comultiplication in the proposed variant.'),
58:(A,'Handwritten§7: “il suffit qu’elle soit vraie à l’ordre2 ...??”.','Does the order2 descent condition already force the stated square-zero connection operator, and what converse is justified under the flat-conormal setting?'),
59:(A,'Handwritten§9 margin: “Attention signes !”.','Check the sign convention comparing the two curvature tensors. Duplicated arguments are a separate transcription alarm.'),
60:(E,'The last equivalence is asserted; the missing integrability qualifier is diagnosed by the present curved-connection counterexample.',''),
61:(A,'Handwritten§11: “Peut-il s’y ramener, en raisonnant dans un topos convenable?!”','Can the formal-groupoid/cohomology comparison be reduced to the fundamental crystalline theorem in a suitable topos?'),
62:(E,'The arbitrary fixed nonzero coefficient-ring converse is asserted. Its Moore-space repair and coefficient question arise in this run, not as a source doubt.',''),
63:(E,'The chosen-basis Grassmann chart is asserted. The scope of “canonical” is our present clarification, not an explicit authorial question.',''),
64:(A,'Blass8.17(a) is an unsupported wider proposal; the matching cote25 paragraph expressly labels the same arbitrary-morphism bound a conjecture.','Does the codimension-two irreducibility bound survive arbitrary morphisms with image dimension at least3?'),
65:(T,'Blass8.17(b) has repeated “illegible” and “Ask AG” around the dual-map qualifier. Recovering that qualifier is the translator’s request.',''),
66:(E,'Blass59 physical2241–2247 says the normalization argument is immediate and omits its details; that is not an explicit deferred proof. The transition2249–2250 leads directly to the fixed-base question2259–2271, already MP-SA23-forms-22. No distinct normalization question is written.',''),
67:(A,'Tapis2/32: “n’a plus rien de pleinement fidèle, semble-t-il??”.','Is the presheaf-topos construction fully faithful like the nerve construction?')
}
assert {int(q['id'].rsplit('-',1)[1]) for q in ps}==set(D)
audit=[];keep=[];editor=[]
for q in ps:
 n=int(q['id'].rsplit('-',1)[1]);origin,cue,question=D[n]
 q['origin']=origin;q['source_cue']=cue
 audit.append({'original_id':q['id'],'origin':origin,'cue_or_reason':cue,'original_task_title':q['title']})
 if origin==A:
  q['former_reader_task_title']=q['title'];q['as_he_states']=question+' Source cue: '+cue
  q['record_type']='authorial problem'
  if n==1:q['title']='The deferred relative-divisor classification'
  if n==3:q['title']='References for local module properties and singular loci'
  if n==44:q['title']='Structure of the dual Steenrod group'
  if n==54:q['title']='The promised exterior-differential lemma'
  if n==58:q['title']='The order-two descent test for integrability'
  if n==22:
   q['source_cue']+=' Its introductory deferred explanation is Blass59 physical2249–2250; the explicit fixed-base question follows at2259–2271.'
   q['occurrences']=[x for x in q['occurrences'] if x.get('role')!='transition to the same fixed-base question; not a separate normalization proof request']
   q['occurrences'].append({'claim':'C-SA23-forms-025','cote':'24','scans':['24/59','24/60'],
      'lines':'sources/texts/api/ega_v_cote24_blass_combined.tex:2249-2250,2259-2271',
      'role':'transition to the same fixed-base question; not a separate normalization proof request'})
   # The exact duplicate is removed on repeat application, without merging any
   # distinct source occurrences.
   q['occurrences']=list({json.dumps(x,sort_keys=True):x for x in q['occurrences']}.values())
   audit[-1]['cue_or_reason']=q['source_cue']
  if n in (47,49):q['source_author']='Daniel Quillen'
  else:q['source_author']='Alexander Grothendieck; translation/editorial uncertainty retained where stated'
  keep.append(q)
 else:
  q['original_id']=q['id'];q['id']=f'ED-SA23-forms-{n:02d}';q['record_type']='editorial task';q['cue_or_reason']=cue
  if n in (11,66):
   q['former_as_he_states']=q['as_he_states']
   q['as_he_states']=('The source asserts the existence of proper smooth nonprojective counterexamples; no construction request is written.' if n==11 else 'The source calls the normalization reasoning immediate and omits its details; the following deferred explanation leads to MP-SA23-forms-22.')
   q['task']=('Identify and verify the intended nonprojective counterexample and the conflicting statement scopes.' if n==11 else 'Check the asserted normalization reduction and recover the damaged adjective; keep the fixed-base question under MP-SA23-forms-22.')
   q['why_open']='Not an authorial open question; this is a reader or translator verification task.'
   q['worth']=('A bounded editorial investigation is worthwhile because the two asserted scopes conflict, even though the author does not ask for a counterexample.' if n==11 else 'Commentary and source clarification are worthwhile because the compressed normalization assertion and damaged adjective affect the theorem’s scope; no new authorial question is inferred.')
   source=P.parents[2]/'sources/texts/api/ega_v_cote24_blass_combined.tex'
   ls=source.read_text().splitlines()
   ranges=[(1301,1321),(1330,1338)] if n==11 else [(2193,2207),(2241,2250),(2259,2271)]
   q['source_cues']=[{'source':'sources/texts/api/ega_v_cote24_blass_combined.tex','physical_lines':[lo,hi],'verbatim':'\n'.join(ls[lo-1:hi])} for lo,hi in ranges]
   audit[-1]['source_cues']=q['source_cues'];audit[-1]['decision']='reclassify_to_editorial_task';audit[-1]['confidence']='high'
  editor.append(q);audit[-1]['editorial_id']=q['id']
# Newly isolated actual source questions discovered during the final provenance reread.
def fresh(n,title,claimnums,question,plausible,art,why,worth,refs,cue):
 selected=[cs[f'C-SA23-forms-{x:03d}'] for x in claimnums]
 q={'id':f'MP-SA23-forms-{n:02d}','title':title,'occurrences':[{'claim':c['id'],'items':c['items'],'cote':c['cote'],'scans':c['scans'],'lines':c['lines']} for c in selected],'as_he_states':question,'plausible_today':plausible,'state_of_art':art,'why_open':why,'worth':worth,'refs':refs,'origin':A,'record_type':'authorial problem','source_cue':cue,'source_author':'Alexander Grothendieck'}
 keep.append(q);audit.append({'original_id':q['id'],'origin':A,'cue_or_reason':cue,'original_task_title':title})
fresh(68,'The expected abelian envelope and the withdrawn noetherian question',[50,51],'The author expects the abelian category generated by the bordism correspondence category to be finitely presented Λ-modules; he crosses out the question whether Λ is noetherian and replaces it with coherence.','The coherent infinite polynomial ring has an abelian category of finitely presented modules. Closing finite projectives under kernels and cokernels inside Λ-modules gives that category. A different universal meaning of abelian envelope needs its own specification.','The finite-variable flat-descent proof establishes coherence; the cancelled noetherian suggestion is false because there are infinitely many polynomial generators. No exact stronger universal-envelope theorem is inferred from the word generated.','The pages themselves replace the noetherian question by the coherent-ring observation; they do not specify the full universal property of the abelian envelope.','A short commentary is worthwhile because the coherence repair is settled while the word generated may encode a stronger categorical requirement.',['forms_Thom','forms_StacksCoherent','forms_LocalChecks'],'Tapis15/46, physical642–653 and1280–1290: “on s’attend”; deleted “est-il noethérien ... fini?” replaced by coherence.')
fresh(69,'What structure is required on the orientation space H?',[54],'For the extension to H-oriented correspondences, the source asks parenthetically whether H is commutative, associative and unital.','Separate the structure needed for a bordism category from stronger coherent A-infinity/E-infinity Thom-spectrum constructions; the map to BO must carry the compatible orientation data required by the chosen construction.','Ando–Blumberg–Gepner–Hopkins–Rezk2014, Definition4.4 and Theorems4.2/4.6, gives a precise coherent commutative Thom-algebra and orientation theory. Their§1.2–1.3 distinguishes the associative module construction. This is a sufficient modern formulation, not an identification of the weakest intended1968 H-space axioms.','The parenthesis itself leaves the coherence level unspecified; no historical reason for abandoning the formulation is supplied.','A bounded formulation task is worthwhile because ordinary orientation composition and an E-infinity Thom theory demand different data.',['forms_ABGHR','forms_May','forms_LocalChecks'],'Tapis17/48, physical718–734 and1348–1363: “H ... (commutatif, associatif et unitaire?)”.')
fresh(70,'The requested dimension-invariance reference',[4],'After Proposition2.6, the author requests a reference for dim(X_k(eta))=dim(X).','For every finite-type k-scheme X and every field extension K/k, dim(X_K)=dim(X).','Stacks10.116.5,tag00P3, proves the affine statement by finite injective Noether normalization and flat base change; an affine cover gives the scheme statement. Full proof read.','The source gives no reason beyond a missing reference.','Commentary only: the exact short proof is available and resolves the stated reference request.',['forms_StacksFieldDim','forms_LocalChecks'],'Blass12, physical455–467: “reference needed for the last equality”.')
(P/'problems.json').write_text(json.dumps(keep,ensure_ascii=False,indent=2)+'\n')
(P/'editorial_tasks.json').write_text(json.dumps(editor,ensure_ascii=False,indent=2)+'\n')
(P/'problem_origin_audit.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2)+'\n')
with (P/'progress.log').open('a') as f:f.write(datetime.datetime.now(datetime.timezone.utc).isoformat()+f' Manually separated {len(keep)} authorial problems and {len(editor)} editorial/translator tasks; stable former IDs retained.\n')
print(len(keep),'authorial problems;',len(editor),'editorial tasks;',len(audit),'origin decisions')
