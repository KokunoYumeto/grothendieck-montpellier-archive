"""Serialize a manually adjudicated, bounded cross-folder duplicate review.

No similarity score, heading rule, or text-matching heuristic supplies a verdict.
The only automated checks below validate identifiers and snapshot the inputs.
This program writes its own integration report, never an owner register or plan.
"""
from pathlib import Path
import json, hashlib

W=Path(__file__).resolve().parents[1]
B=W.parent

def endpoint(file, start, end, scans, claim_ids=()):
    return {'file':'sources/texts/codex/'+file+'_transcription.tex',
            'physical_lines':[start,end], 'scans':scans,
            'claim_ids':list(claim_ids), 'read_directly':True}

field_endpoints=[
 endpoint('K161-3-02',937,969,[40],['C-SA23-spaces-033','C-SA23-spaces-034']),
 endpoint('K161-3-03',34,49,[42],['C-SA23-spaces-035']),
 endpoint('K161-2-06',407,423,[93],['C-SA23-groupes-096']),
]
yoneda_endpoints=[
 endpoint('K161-3-02',687,753,[36],['C-SA23-spaces-032']),
 endpoint('K161-3-02',804,873,[38],['C-SA23-spaces-032']),
 endpoint('K161-2-06',47,88,[82],['C-SA23-groupes-087']),
 endpoint('K161-2-06',142,173,[84,85],['C-SA23-groupes-087']),
 endpoint('K161-2-07',95,206,[99,100],['C-SA23-groupes-087']),
]
reconstruction_endpoints=[
 endpoint('K161-3-03',90,119,[44],['C-SA23-spaces-036']),
 endpoint('K161-3-03',155,192,[46],['C-SA23-spaces-036']),
 endpoint('K161-3-03',216,232,[48],['C-SA23-spaces-036']),
 endpoint('K161-2-05',1,83,[66,67,68,69],['C-SA23-groupes-075','C-SA23-groupes-076','C-SA23-groupes-077']),
 endpoint('K161-2-07',490,595,[106,107],['C-SA23-groupes-077','C-SA23-groupes-104']),
]
sierpinski_endpoints=[
 endpoint('K161-2-02',241,264,[25],['C-SA23-groupes-031']),
 endpoint('K161-3-03',80,88,[43],['C-SA23-spaces-040']),
 endpoint('K161-3-03',121,124,[45],['C-SA23-spaces-040']),
]
presheaf_endpoints=[
 endpoint('K161-1-01',558,571,[16],['C-SA23-groupes-014','C-SA23-groupes-015']),
 endpoint('K161-3-03',128,153,[45],['C-SA23-spaces-041','C-SA23-spaces-042']),
]
density_endpoints=[
 endpoint('K161-1-01',639,727,[18,19,20],['C-SA23-groupes-018','C-SA23-groupes-019','C-SA23-groupes-020','C-SA23-groupes-021']),
 endpoint('K161-3-01',622,935,[18,19,20,21],['C-SA23-spaces-012','C-SA23-spaces-013','C-SA23-spaces-014']),
]
topos_endpoints=[
 endpoint('K161-1-01',558,575,[16],['C-SA23-groupes-015']),
 endpoint('K161-3-02',918,935,[39],['C-SA23-spaces-030']),
 endpoint('K161-3-03',1,8,[41],['C-SA23-spaces-037']),
]
essential_endpoints=[
 endpoint('K161-2-06',40,45,[81],['C-SA23-groupes-086']),
 endpoint('K161-3-03',234,248,[49],['C-SA23-spaces-019']),
]

item_merges=[
 {'target':'SA23-922','sources':['SA23-731','SA23-732'],
  'reason':'Exact repeated field/pseudofield investigation, not merely a common ring-theory topic. The live cote161-3 scan40 and cote161-2 scan93 use the same class of ring maps detected as bijections on all field-valued points, equivalently spectrum bijections with trivial residue extensions. Both then use the identical map Z[t] -> Z[t,t^-1] x Z and its presentation Z[x,y]/(x(xy-1),y(xy-1)). Cote161-3 scan42 is wholly cancelled and concludes incorrectly that its orthogonality test recognizes fields; cote161-2 scan93 explicitly recognizes pseudofields and says the converse is known. The subject is one investigation with materially different witnesses.',
  'overrides':{'statement':'Fields, pseudofields, the universal quasi-inverse test, and the corrected field classifier'},
  'source_endpoints':field_endpoints,
  'preserve':['Keep C-SA23-spaces-033, C-SA23-spaces-034, C-SA23-spaces-035 and C-SA23-groupes-096 as distinct claim records: nonexistence for a finite-product theory, the field-valued-point criterion, the cancelled false field-recognition conclusion, and the pseudofield identification are different assertions.',
              'Keep the explicit cancellation of the entire cote161-3 scan42 draft and its unfinished connectedness attempt.',
              'Do not call the cote161-2 passage a chronologically later correction: the supplied endpoints do not establish their relative dates.',
              'Keep MP-SA23-spaces-24, MP-SA23-spaces-25 and MP-SA23-groupes-55 distinct. Their questions concern different conclusions and drafting states.',
              'Keep the zero ring convention and the separate sheaf-topos field classifier; a categorical product of rings is not a presheaf coproduct.']},
 {'target':'SA23-921','sources':['SA23-730'],
  'reason':'Both witnesses define a type of structures as a pseudofunctor over a fixed doctrine of limit-preserving functors, explicitly assume it is represented, and write the same equivalence Hom(T,F) ~= F(R), followed by Hom(T,tau) ~= R. Cote161-3 calls the representative beta and the construction category Gamma; cote161-2 calls them R and rho(T). This is the same conditional construction, not an inferred universal representability theorem.',
  'overrides':{'statement':'Doctrines, categories of constructions, and conditional two-Yoneda representation'},
  'source_endpoints':yoneda_endpoints,
  'preserve':['Preserve the explicit representability hypothesis in cote161-3: Supposons qu il existe.',
              'Preserve finite-limit versus all-limit doctrine, the chosen universe, pseudonatural transformations/modifications, and underlying-object compatibility.',
              'Preserve the corrected direction T -> sigma rho(T), the cancelled reverse arrow and universal-reflection sentence, and the size question in cote161-2.',
              'The transcription notes long oblique strokes on cote161-3 scans36/38. Do not infer an ink-level cancellation beyond what the supplied transcription actually marks.',
              'Do not merge MP-SA23-spaces-23 with MP-SA23-groupes-48 or -71: conditional representation, local smallness of all constructions, and an intrinsic representability criterion are different questions.']},
 {'target':'SA23-918','sources':['SA23-733'],
  'reason':'The same displayed reconstruction occurs at cote161-3 scan46 line178 and cote161-2 scan68 lines53-65 / scan106 lines511-538: T(C) is the full category of functors C^op -> S=T(Set) whose specified underlying presheaves beta_i composed with the functor are representable. Both use the 2-cartesian square over C^I and the pointwise equivalence for T(PSh(C)).',
  'overrides':{'statement':'Pointwise models, target change, and recovery from set-valued models'},
  'source_endpoints':reconstruction_endpoints,
  'preserve':['Keep C-SA23-spaces-036 and C-SA23-groupes-077 as separate claims. Spaces assumes the full-embedding/2-pullback and presheaf-model conditions for an abstract T; Groupes establishes the test for a represented limits-only theory with a genuinely generating basis. The full hypotheses are not identical.',
              'Preserve the question how T acts on a general lambda-functor, the separate free-object/representation question, and the cancelled cocompletion passage on cote161-3 scan48.',
              'Preserve the distinction between a chosen construction category inside Fun(S,Set) and recovery from the bare category S alone.',
              'Keep MP-SA23-spaces-26, MP-SA23-groupes-40, MP-SA23-groupes-60 and MP-SA23-groupes-61 distinct; the formula shared by their surrounding passages does not identify these questions.']},
]

claim_merges=[
 {'target':'C-SA23-groupes-087','sources':['C-SA23-spaces-032'],
  'reason':'The entire substantive conditional two-Yoneda assertion in spaces032 is repeated explicitly in groupes087: when T is represented by R, transformations T -> F correspond to F(R), and the category of constructions Hom(T,tau) is equivalent to R. Symbols beta/Gamma versus R/rho are the only change in this component. The additional variance, evaluation-direction and size qualifications remain attached to their own witnesses.',
  'overrides':{'statement':'For a type T represented by R in a fixed doctrine, the two-Yoneda equivalence PsNat(T,F) ~= F(R), naturally in F, gives PsNat(T,tau) ~= R and uniqueness of R up to the appropriate equivalence. Representability is a hypothesis. The evaluation arrow is T -> sigma rho(T), variance in R is contravariant, and the category of constructions must lie in the chosen universe.'},
  'source_endpoints':yoneda_endpoints,
  'preserve_source_records':True},
]

record_updates=[
 {'kind':'items','id':'SA23-737',
  'append_fields':{'cote':['161-2'],'scans':[25],
    'lines':['sources/texts/codex/K161-2-02_transcription.tex:248–264'],
    'source_occurrences':[
      {'cote':'161-3','scans':[43,45],'lines':'sources/texts/codex/K161-3-03_transcription.tex:80–88,122–124','claim_ids':['C-SA23-spaces-040']},
      {'cote':'161-2','scans':[25],'lines':'sources/texts/codex/K161-2-02_transcription.tex:248–264','claim_ids':['C-SA23-groupes-031']}]},
  'reason':'Same represented functor: subobjects of the terminal object of a variable topos. Cote161-2 asks for its classifier V; cote161-3 identifies the two-point Sierpinski topos. This consolidates the subject occurrence only; the quotient-lattice assertions and topological embedding assertion remain distinct claims.'},
 {'kind':'claims','id':'C-SA23-groupes-031','set_fields':{'items':['SA23-737']},
  'reason':'Assign the repeated subterminal-classifier subject to its existing precise Spaces item. Preserve the claim ID, its open/closed quotient-lattice assertions, its source question and MP-SA23-groupes-14.'},
 {'kind':'items','id':'SA23-908',
  'set_fields':{'statement':'Elementary quotient theories and model-category exactness; the subterminal-classifier occurrence is consolidated under SA23-737'},
  'reason':'The elementary-quotient dossier remains intact; only its separately indexed subterminal-classifier occurrence is assigned to the common subject. No other claim or question is merged.'},
 {'kind':'items','id':'SA23-738',
  'set_fields':{'statement':'Presheaf morphisms, Kan adjoints, and left-exact extension'},
  'append_fields':{'cote':['161-1'],'scans':[16],
    'lines':['sources/texts/codex/K161-1-01_transcription.tex:558–571'],
    'source_occurrences':[
      {'cote':'161-3','scans':[45],'lines':'sources/texts/codex/K161-3-03_transcription.tex:143–153','claim_ids':['C-SA23-spaces-042']},
      {'cote':'161-1','scans':[16],'lines':'sources/texts/codex/K161-1-01_transcription.tex:558–571','claim_ids':['C-SA23-groupes-014']}]},
  'reason':'The positive component is exactly the same universal property for C small with finite limits and E a topos: Lex(C,E) corresponds to geometric inverse images PSh(C) -> E. Cote161-1 states left exactness of the canonical cocontinuous extension; cote161-3 gives the equivalent Hom_top(E,PSh(C)) formula. Keep the converse-direction point formula and the arbitrary-target exactness question separate.'},
 {'kind':'claims','id':'C-SA23-groupes-014',
  'set_fields':{'items':['SA23-738']},
  'append_fields':{'lines':['sources/texts/codex/K161-1-01_transcription.tex:558–571']},
  'reason':'Assign the common lex-presheaf universal-property occurrence to the precise existing item without merging the broader compound claim spaces042. The added actual locator includes the topos qualification at line571, beyond the former endpoint566. Keep the Set^op warning and MP-SA23-groupes-06.'},
 {'kind':'items','id':'SA23-903',
  'set_fields':{'statement':'Functor constructions, contravariant exactness obstruction, and the dense left-exact topos criterion'},
  'reason':'Keep the distinct claims012,013,015 on this archival unit after its positive presheaf universal-property component014 is assigned to SA23-738. All original source wording remains preserved.'},
]

kept_distinct=[
 {'id':'GS-D01','claims':['C-SA23-groupes-018','C-SA23-groupes-019','C-SA23-groupes-020','C-SA23-groupes-021','C-SA23-spaces-012','C-SA23-spaces-013','C-SA23-spaces-014','C-SA23-spaces-015'],
  'problems':['MP-SA23-groupes-08','MP-SA23-spaces-09','MP-SA23-spaces-10','MP-SA23-spaces-11'],
  'decision':'Keep separate; verified structural relationship, not a whole-claim duplicate.',
  'reason':'Cote161-1 starts with a full inclusion C -> E and therefore obtains beta alpha = id on every C-functor (lines639-676). Cote161-3 starts with an arbitrary site map C -> Sh(C); its unit is invertible only under a further condition, expressly said to be automatic only for a subcanonical topology (line768). Both use density for fully faithful restriction, but the general density-presentation/finality problem and the site-localization/bicovering criterion have different hypotheses and residual questions. The site-localization argument is completed with OK at line903; the general finite-colimit cofinality shortcut is not thereby proved.',
  'source_endpoints':density_endpoints},
 {'id':'GS-D02','claims':['C-SA23-groupes-015','C-SA23-spaces-030','C-SA23-spaces-037'],
  'problems':['MP-SA23-groupes-06','MP-SA23-spaces-21'],
  'decision':'Keep separate; link a sufficient dense-generator criterion to the topos definition and its generator construction.',
  'reason':'Groupes tests exactness of extension for a specified dense lex functor into a candidate E. Spaces030 gives the definition/equivalent Giraud axioms, and spaces037 starts inside a topos and constructs the generator embedding. The common reflective-localization mechanism does not make the direction, data, or question identical.',
  'source_endpoints':topos_endpoints},
 {'id':'GS-D03','claims':['C-SA23-groupes-086','C-SA23-groupes-094','C-SA23-spaces-019','C-SA23-spaces-020'],
  'problems':['MP-SA23-groupes-47','MP-SA23-spaces-15','MP-SA23-spaces-16'],
  'decision':'Keep separate; the spatial/localic specialization is not the general essential-point reconstruction theorem.',
  'reason':'Groupes describes arbitrary topoi with enough essential points and the reconstruction of a category subject to Karoubi completion. The checked Spaces passage asks when PSh(C) is a topological-space topos and characterizes a sober space using a basis of minimal neighborhoods. Its separate morphism problem concerns preorders versus all or essential geometric morphisms. These additional localic/spatial restrictions and morphism conventions are substantive.',
  'source_endpoints':essential_endpoints},
 {'id':'GS-D04','claims':['C-SA23-groupes-077','C-SA23-spaces-036'],
  'problems':['MP-SA23-spaces-26','MP-SA23-groupes-40','MP-SA23-groupes-60','MP-SA23-groupes-61'],
  'decision':'Same subject consolidated by item merge; keep both claims and all questions.',
  'reason':'The displayed reconstruction is exact at both ends, but the represented-theory theorem and the abstract-T reconstruction under additional axioms are not the same complete assertion. The unsolved action-on-functors and intrinsic-recovery questions must not disappear when the subject is consolidated.',
  'source_endpoints':reconstruction_endpoints},
 {'id':'GS-D05','claims':['C-SA23-groupes-096','C-SA23-spaces-033','C-SA23-spaces-034','C-SA23-spaces-035'],
  'problems':['MP-SA23-groupes-55','MP-SA23-spaces-24','MP-SA23-spaces-25'],
  'decision':'Same subject consolidated by item merge; keep all claim and question witnesses.',
  'reason':'A cancelled false field criterion is not interchangeable with the live pseudofield identification, and neither is identical to the finite-product nonrepresentability obstruction or the field-point characterization of the inverted arrows.',
  'source_endpoints':field_endpoints},
 {'id':'GS-D06','claims':['C-SA23-groupes-031','C-SA23-spaces-040'],
  'problems':['MP-SA23-groupes-14'],
  'decision':'Same classifier occurrence consolidated by record updates; no whole-claim or problem merge.',
  'reason':'The represented subterminal-object functor agrees exactly. The Groupes quotient-lattice problem and the Spaces T0-embedding conclusion are different additions.',
  'source_endpoints':sierpinski_endpoints},
 {'id':'GS-D07','claims':['C-SA23-groupes-014','C-SA23-spaces-042'],
  'problems':['MP-SA23-groupes-06'],
  'decision':'Same lex-presheaf universal-property occurrence consolidated by record updates; no whole-claim merge.',
  'reason':'The positive lex-extension theorem is identical. Spaces042 also treats morphisms in the other direction through points/Pro(C); Groupes014 retains the failed unrestricted-target extension. Those complete assertions are not duplicates.',
  'source_endpoints':presheaf_endpoints},
 {'id':'GS-D08','claims':['C-SA23-groupes-026','C-SA23-spaces-031'],
  'problems':['MP-SA23-spaces-22'],
  'decision':'Keep separate after comparison of complete claim statements; no source-endpoint-based merge proposed.',
  'reason':'Every topos is the classifier of a geometric theory and the qualified lecture suggestion that structures have classifying topoi are converse-facing claims with different quantifiers. A shared word classifier does not identify them.',
  'source_endpoints':[]},
 {'id':'GS-D09','claims':['C-SA23-groupes-034','C-SA23-spaces-038','C-SA23-groupes-052','C-SA23-spaces-043','C-SA23-groupes-062','C-SA23-spaces-062'],
  'problems':['MP-SA23-groupes-16','MP-SA23-groupes-23','MP-SA23-groupes-30','MP-SA23-spaces-27','MP-SA23-spaces-35'],
  'decision':'Keep separate after comparison of complete claim statements; no source-endpoint-based merge proposed.',
  'reason':'These are respectively torsor classification versus fiber functors/cohomology; representable subterminal-slice localization versus arbitrary slicing; and geometric axiomatizability of ring-map properties versus the scheme-theoretic universal-homeomorphism characterization. Common definitions or special cases alone do not identify their full claims or questions.',
  'source_endpoints':[]},
]

links=[
 {'kind':'folder','from':'C-SA23-groupes-018–021; K161-1-01 scans18–20','to':'C-SA23-spaces-012–015; K161-3-01 scans18–22','what':'Dense extension and site extension share a Kan formula but have different unit and continuity conditions.','evidence':'Direct comparison of K161-1-01:639–727 and K161-3-01:622–935; the latter explicitly singles out subcanonical sites at768 and completes localization at903.','note_ids':'MP-SA23-groupes-08; MP-SA23-spaces-09–11'},
 {'kind':'folder','from':'C-SA23-groupes-015; K161-1-01 scan16','to':'C-SA23-spaces-030,-037; K161-3-02 scan39 / K161-3-03 scan41','what':'Dense lex extension criterion and the reflective-localization definition of a topos.','evidence':'K161-1-01:558–575, K161-3-02:918–935, K161-3-03:1–8 read directly; directions of the assertions differ.','note_ids':'MP-SA23-groupes-06; MP-SA23-spaces-21'},
 {'kind':'folder','from':'C-SA23-groupes-086; K161-2-06 scan81','to':'C-SA23-spaces-019; K161-3-03 scan49','what':'Enough essential points and the distinct spatial presheaf-topos criterion.','evidence':'K161-2-06:40–45 and K161-3-03:234–248 read directly; the second has localic/sobriety hypotheses.','note_ids':'MP-SA23-groupes-47; MP-SA23-spaces-15'},
]

source_locator_observations=[
 {'claim':'C-SA23-groupes-014','current_locator':'K161-1-01:546–566','actual_relevant_locator':'K161-1-01:558–571','observation':'The positive topos statement and converse begin at571, outside the current claim endpoint566. The proposed record update appends the precise range; no transcription is changed.'},
 {'claim':'C-SA23-groupes-019','current_locator':'K161-1-01:673–699','actual_relevant_locator':'K161-1-01:678–685,700–707','observation':'The density calculation and fully faithful restriction conclusion are physically on scan20 at704–707; scan19 is mostly blank. Suggested locator addition only, not a change in mathematical assessment.'},
 {'claim':'C-SA23-spaces-019','current_locator':'K161-3-02:226–256','actual_relevant_locator':'also K161-3-03:234–248','observation':'The separate scan49 occurrence is already described in the owner section/problem, and directly confirms the spatial specialization used here. It can be appended to the claim locator if desired.'},
]

records={}
snapshots=[]
for owner in ['groupes','spaces']:
    records[owner]={}
    for kind in ['items','claims','problems']:
        p=W/'parts'/owner/(kind+'.json')
        rows=json.loads(p.read_text())
        records[owner][kind]=rows
        snapshots.append({'file':str(p.relative_to(W)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'count':len(rows)})

all_ids={r['id'] for owner in records.values() for rows in owner.values() for r in rows}
errors=[]
for kind,specs in [('item',item_merges),('claim',claim_merges)]:
    for spec in specs:
        for ident in [spec['target']]+spec['sources']:
            if ident not in all_ids:errors.append({'type':'unknown merge ID','id':ident})
for spec in record_updates:
    if spec['id'] not in all_ids:errors.append({'type':'unknown update ID','id':spec['id']})
for entry in kept_distinct:
    for ident in entry['claims']+entry['problems']:
        if ident not in all_ids:errors.append({'type':'unknown reviewed ID','id':ident})
for spec in item_merges:
    byid={r['id']:r for owner in records.values() for r in owner['items']}
    if any(byid[ident]['sources'] for ident in [spec['target']]+spec['sources']):
        errors.append({'type':'unexpected indexed subject in additional-only review','target':spec['target']})

all_endpoints={json.dumps(e,sort_keys=True):e for es in [field_endpoints,yoneda_endpoints,reconstruction_endpoints,sierpinski_endpoints,presheaf_endpoints,density_endpoints,topos_endpoints,essential_endpoints] for e in es}
for e in all_endpoints.values():
    p=B/e['file'];lines=p.read_text().splitlines()
    if not (1<=e['physical_lines'][0]<=e['physical_lines'][1]<=len(lines)):
        errors.append({'type':'invalid source interval','endpoint':e})
    e['source_sha256']=hashlib.sha256(p.read_bytes()).hexdigest()

plan=json.loads((W/'integration/consolidation_plan.json').read_text())
existing_removed={x for kind in ['item','claim','problem'] for spec in plan.get(kind+'_merges',[]) for x in spec['sources']}
overlap=sorted(existing_removed & {x for specs in [item_merges,claim_merges] for spec in specs for x in spec['sources']})

report={
 'date':'2026-11-19',
 'reviewer':'GPT-6 Astra Pro, ega; manual bounded exact-duplicate review',
 'scope':'Current Groupes cotes161-1/2 versus Spaces cotes161-3/4. Already handled product-topos and cocharacter mergers excluded. No literature search, research direction, source repair or owner mutation.',
 'method':'Read all 198 claim statements and all 115 problem question summaries, then the complete selected claim/problem records. Manually compare mathematical objects, universal properties, hypotheses and question scope. Read the actual transcription endpoints for every proposed merger and occurrence consolidation. Metadata-only neighboring candidates are explicitly labelled and never merged.',
 'inventory_counts':{o:{k:len(v) for k,v in ks.items()} for o,ks in records.items()},
 'inventory_reviewed_ids':{o:{k:[r['id'] for r in ks[k]] for k in ['claims','problems']} for o,ks in records.items()},
 'input_snapshots':snapshots,
 'summary':{'additional_item_aliases':4,'item_merge_groups':3,'whole_claim_aliases':1,'whole_problem_aliases':0,'narrow_shared_occurrence_assignments':2,'indexed_entry_rows_changed':0},
 'item_merges':item_merges,
 'claim_merges':claim_merges,
 'problem_merges':[],
 'record_updates':record_updates,
 'additional_links':links,
 'kept_distinct':kept_distinct,
 'source_locator_observations':source_locator_observations,
 'source_checks':list(all_endpoints.values()),
 'validation':{'errors':errors,'overlap_with_already_removed_plan_sources':overlap,'owner_files_mutated':False,'manual_plan_mutated':False,'whole_claim_merge_requires_source_records':True},
 'integration_instruction':'These are proposals. Root may append the item_merges/claim_merges/record_updates/additional_links to the manual plan after review. Keep all original witnesses and occurrence-specific statuses; do not propagate a cancelled false-field refutation to the live pseudofield theorem. Do not infer a relative chronology from the cross-folder agreement.'
}
out=W/'integration/groupes_spaces_review.json'
out.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'saved':str(out),'summary':report['summary'],'errors':errors,'existing_alias_conflicts':overlap},ensure_ascii=False))
raise SystemExit(bool(errors))
