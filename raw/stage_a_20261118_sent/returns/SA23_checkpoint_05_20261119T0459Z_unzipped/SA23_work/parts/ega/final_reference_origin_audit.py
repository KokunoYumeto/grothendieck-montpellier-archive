"""Explicit final reference/provenance audit; no heading or keyword verdicts.

All fifteen decisions and all source-origin exceptions were manually assessed.
This is the final overlay after the other core serializers.
"""
from pathlib import Path
import json,csv

HERE=Path(__file__).resolve().parent
PARTS=HERE.parent
cs=json.loads((HERE/'claims.json').read_text())
by={int(c['id'].rsplit('-',1)[1]):c for c in cs}

# refs, exact role, historical limit (the latter is not inferred from standardness)
decisions={
14:(['Stacks00DV'],'Lemma10.20.1(9)–(11) supplies the nilpotent devissage step. The complete topological criterion is independently checked from its associated-graded and inverse-limit argument.','No exact pre-manuscript publication of this topological formulation was verified. E refers to the elementary nilpotent/filtered mechanism, not a documentary priority finding.'),
15:(['Stacks059H'],'Propositions10.89.2–3 and proofs exactly distinguish finite generation/surjectivity and finite presentation/bijectivity of the tensor-to-arbitrary-product map.','The modern exact theorem is verified. The prior wording established before these notes overstated the historical evidence; no first-publication or pre-manuscript date is established here.'),
27:(['StacksNorms'],'Section31.18, especially the degree-d norm condition and Lemma31.18.2, verifies the norm-of-pullback power law in its stated finite norm context. The placewise e/f and repartition assertions are independently reconstructed with the no-defect hypotheses explicitly retained.','The reused typescript remains unidentified. The reference supports the norm-law component, not every valuation or idelic hypothesis, and does not establish the identity or date of this leaf.'),
31:([],'The Maurer–Cartan linearization is independently checked from the surviving coordinate argument; the missing earlier formula prevents a full sign audit.','F: exact paper and author not identified after the recorded phrase and bibliography searches. No unrelated deformation reference is inserted as a match.'),
32:([],'Finite formal-series identities, the complete convergence argument and the dual-number counterexample are direct checks. Cote68 provides a separate archival witness, recorded in the cross-owner review.','The attempted Grinberg logid.pdf opening timed out again. No exact pre-manuscript printed reference for the full complete-topological formulation was verified; E is restricted to classical formal-calculus content, not documentary priority.'),
41:([],'The naturality and product identity follows directly from h u=u′h and the defined action g↦u g v^−1; proof recorded in the claim.','No independently matched published theorem is asserted. E concerns the elementary categorical identity, not the priority or publication of this exact jet construction.'),
44:([],'The surviving change-of-frame calculation is read, but its structure species and conditionC are missing.','F: no exact Bourbaki or reused-typescript identification. Generic associated-bundle literature would not identify the truncated assertion and is not supplied as a substitute.'),
47:(['StacksUnramified','RydhDescent'],'Stacks00US supplies the unramified algebraic framework; Rydh concerns effective descent of étale morphisms under specific subtrusiveness hypotheses. Neither is an exact theorem for the whole displayed gluing claim.','C remains: the arbitrary unramified/nonnoetherian gluing assertion is not closed by these references. Their role is explicitly a comparison framework.'),
48:(['RydhDescent','SGA4VIII'],'Rydh’s étale descent theorem and SGA4VIII9.4 supply exact neighboring descent categories and hypotheses. Finite scheme epimorphism with the stated surjective test for unramified sections is a different formulation.','C remains: no exact publication proving all of the source quantifiers has been found. Merely surjective is not substituted for epimorphism.'),
73:([],'The cancelled graded-category formulas and shifting conventions are recorded diplomatically.','F: exact formulation remains unidentified; later triangulated-category vocabulary does not resolve the incomplete definitions.'),
78:(['Stacks00DV'],'Lemma10.20.1(9)–(11) gives the nilpotent module-generation mechanism on degree truncations; the augmented-composition equivalence and its counterexample are independently proved.','No exact pre-manuscript printed version of this graded extension lemma was verified. The opened tag027W is Hilbert-function definitions/exercises, not this theorem, and is not used as a theorem citation.'),
79:(['Stacks00H9'],'Definition10.39.1 and Lemmas10.39.4,10.39.7 verify the flatness operations used here. Projective direct-summand/tensor arguments and section independence are independently proved in proof_notes.md.','No exact publication of the full arbitrary-module triangular section-independence lemma was matched. E concerns its elementary algebraic mechanism, not a proved priority claim.'),
80:(['Stacks00NX','Stacks00DV'],'Lemma10.78.2 gives finite-projective/local-free equivalence; Lemma10.20.1(2),(6) supplies the finite-module Nakayama step. After prior surjectivity, the split kernel has zero fibre rank and vanishes.','These are exact modern supporting lemmas, not an attribution of the whole manuscript rank criterion. Its omitted surjectivity is detected by the saved counterexample.'),
81:(['Stacks00H9'],'Lemma10.39.7 proves flat base change for(ii), and Lemma10.39.4 proves transitivity for(iii). The literal(i) is refuted by the independent k[t]→k Tor computation.','No separate historical theorem is needed to derive the two valid implications. The source’s false first arrow is not made true by citing flatness background.'),
82:([],'The polynomial universal property gives an algebra section after homogeneous generator lifts; the already corrected section-independence lemma gives the isomorphism. This is an independent proof.','No exact printed antecedent of this combined graded corollary was identified. E is limited to the elementary universal-property mechanism; no documentary priority or novelty claim is made.'),
}
for n,(refs,role,limit) in decisions.items():
    c=by[n]
    c['refs']=refs;c['references']=refs
    c['reference_role']=role
    c['historical_identification_limit']=limit
    c['fate']=role+' '+limit
    c['literature_fate']=c['fate']

old='Surjectivity alone can fail for merely finite generation with infinitely many relations.'
correct='Finite generation already implies surjectivity. Failure of finite presentation can cause failure of injectivity; no noetherian hypothesis is needed for the stated finitely presented case.'
by[15]['present_check']=by[15]['present_check'].replace(old,correct)
by[15]['present_status']=by[15]['present_status'].replace(old,correct)
by[15]['present_run_correction']='Final audit corrected this run’s earlier surjectivity sentence; the manuscript lemma and its finite-presentation hypothesis were already correct.'
# Keep the initial source serializer from reintroducing the erroneous sentence.
builder=HERE/'build_claims.py'
builder.write_text(builder.read_text().replace(old,correct))

new_refs=[
 ('Stacks059H','Interchanging direct products with tensor','059H','Propositions10.89.2–3 and their proofs read19November2026: finite generation iff all tensor/product maps are surjective; finite presentation iff they are bijective. This corrects one present-run commentary sentence, not the manuscript.'),
 ('Stacks00H9','Flat modules and flat ring maps','00H9','Definition10.39.1 and Lemmas10.39.4,10.39.7 read19November2026: exactness, flat composition and flat base change. Used only for the specified flatness components of C079/C081.'),
 ('Stacks00NX','Finite projective modules: Lemma10.78.2','00NX','Statement and local-free/direct-summand proof steps read19November2026. Used for the finite-projective rank criterion; not an arbitrary-module projectivity theorem.'),
 ('Stacks00DV','Nakayama’s lemma: Lemma10.20.1','00DV','Parts(2),(6),(9)–(11) and their proof mechanisms read19November2026. Finite and nilpotent variants kept distinct. Used for the stated supporting steps, not as a complete source for the manuscript’s topological or graded theorems.'),
]
bib=json.loads((HERE/'bibliography_records.json').read_text())
bmap={b['key']:b for b in bib}
for key,title,tag,note in new_refs:
    bmap[key]={'key':key,'kind':'misc','author':'The Stacks Project Authors','title':title,'year':'2026','url':'https://stacks.math.columbia.edu/tag/'+tag,'note':'verified','annote':note}
bmap['StacksGraded']['annote']='Tag027W was opened and reread19November2026. It is Section111.26, Hilbert functions, definitions and exercises. It does not prove the full graded-extension, section-independence, Poincaré-isomorphism or flatness claims. Those are independently checked and now have appropriately limited supporting references.'
bib=list(bmap.values())
(HERE/'bibliography_records.json').write_text(json.dumps(bib,ensure_ascii=False,indent=2)+'\n')

def brace(s):return str(s).replace('{','\\{').replace('}','\\}')
bibtext=[]
for b in bib:
    bibtext.append('@'+b.get('kind','misc')+'{'+b['key']+',\n'+',\n'.join('  '+k+' = {'+brace(v)+'}' for k,v in b.items() if k not in ['key','kind'])+'\n}\n')
(HERE/'references.bib').write_text('\n'.join(bibtext))

problems=json.loads((HERE/'problems.json').read_text())
for p in problems:
    n=int(p['id'].rsplit('-',1)[1])
    if n in {42,43,44}:
        p['refs']={42:['Stacks00DV'],43:['Stacks00NX','Stacks00DV'],44:['Stacks00H9']}[n]
        p['reference_role']='Exact supporting algebraic lemmas only; the full corrected graded statement and counterexample are independently proved in this run. Stacks027W is not cited as a theorem match.'
(HERE/'problems.json').write_text(json.dumps(problems,ensure_ascii=False,indent=2)+'\n')

# Origin review: every top-level record below is anchored in an actual source
# assertion/question/definition. Present-run corrections are subrecords/checks.
# These explicit sets were manually reviewed from all182 title/status/source rows.
core_questions={6,19,21,24,25,45,48,51,55,56,57,61,69,76,77,79,81,86,87,88,89,90,91,92,93,94,95,96,98}
core_definitions={37,40,63,73,83}
analysis_questions={25,33,37,40,43,62,70,73,78,80,83}
analysis_definitions={13,16,51}

origin_report=[]
for part,rows,questions,definitions in [('ega',cs,core_questions,core_definitions),('analysis_curves',json.loads((PARTS/'analysis_curves/claims.json').read_text()),analysis_questions,analysis_definitions)]:
    for c in rows:
        n=int(c['id'].rsplit('-',1)[1])
        c['record_origin']='source question or qualified assertion' if n in questions else ('source definition or program' if n in definitions else 'source assertion')
        c['verification_origin']='Present-run proof, calculation and literature comparison are separate from the source assertion. A corrected modern formulation does not emend the transcription.'
        if 'refined_statement' in c:
            c['refined_statement']['record_origin']='present-run reconstruction'
        if part=='ega' and n==21:
            c['verification_origin']='The discrete-formal-smoothness question and negative expectation are authorial. The projective-differential/rank counterexample is the present-run verification, using the separately credited earlier-run nonprojectivity lead.'
        if part=='ega' and n==23:
            c['verification_origin']='The nonsplitting proposition and unfinished coefficient argument are authorial; the completed finite-support proof is this run’s reconstruction. The stronger nonprojectivity development belongs to the earlier run (SA23-141) and is not a separately authorial claim.'
        if part=='ega' and n==35:
            c['verification_origin']='The derivation/automorphism equivalence and BCH specialization are authorial. The tensor-operator proof and square-zero test were supplied by the earlier run; the polynomial-in-integers proof is checked independently in this run.'
        if part=='analysis_curves' and n in {12,17,65,67,80,83}:
            c['verification_origin']='The source assertion/question is quoted in his_statement. The explicit counterexample, repaired interpretation or bounded parameter-range statement in present_status is the present run’s analysis, not an assertion found on the manuscript leaf.'
        origin_report.append({'id':c['id'],'record_origin':c['record_origin'],'verification_origin':c['verification_origin']})
    (PARTS/part/'claims.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
(HERE/'record_origin_audit.json').write_text(json.dumps(origin_report,ensure_ascii=False,indent=2)+'\n')

events=list(csv.DictReader((HERE/'check_events.tsv').open(),delimiter='\t'))
fields=list(events[0])
for e in events:
    if old in e['outcome']:
        e['outcome']='SUPERSEDED by the final19November2026 reference audit: the earlier present-run claim about failure of surjectivity for a finite module was wrong. '+correct+' The finitely presented manuscript lemma remains valid.'
new_events=[]
for n,(refs,role,limit) in decisions.items():
    new_events.append({'statement_id':f'C-SA23-ega-{n:03}','date':'2026-11-19','who':'GPT-6 Astra Pro; effort not independently exposed; SA23-20261119; owner ega','type':'targeted proof check' if n in [15,79,80,81] else 'reference scope and historical identification audit','outcome':role+' '+limit})
for key,title,tag,note in new_refs:
    new_events.append({'statement_id':key,'date':'2026-11-19','who':'GPT-6 Astra Pro; effort not independently exposed; SA23-20261119; owner ega','type':'used and rechecked in this run','outcome':note})
for e in new_events:
    if e not in events:events.append(e)
with (HERE/'check_events.tsv').open('w') as f:
    w=csv.DictWriter(f,fieldnames=fields,delimiter='\t');w.writeheader();w.writerows(events)

log=[json.loads(s) for s in (HERE/'search_log.jsonl').read_text().splitlines()]
audit_search={
 'id':'S-ega-refaudit-01','date':'2026-11-19',
 'commands':{'system2_search_query':[
  {'q':'site:stacks.math.columbia.edu "finitely presented" "tensor product" "products" modules'},
  {'q':'site:stacks.math.columbia.edu "filtered" "complete" "isomorphism" associated graded'},
  {'q':'site:stacks.math.columbia.edu "flat" "composition" "tensor" "Lemma 10.39"'},
  {'q':'site:stacks.math.columbia.edu "finite projective" "surjective" "same rank"'}]},
 'claim_ids':[f'C-SA23-ega-{n:03}' for n in [14,15,78,79,80,81]],
 'urls':['https://stacks.math.columbia.edu/tag/'+s for s in ['059H','00H9','00NX','00DV','027W']],
 'match_and_limit':'Exact tensor/product theorem found; finite generation gives surjectivity, correcting this run. Flat base change/composition and finite-projective/Nakayama supporting lemmas opened. No exact full adic or graded-extension historical match inferred.',
 'raw_evidence':'sources/external/ega/raw_search/refaudit_search.json; refaudit_open.json; refaudit_open2.json (internal caches excluded from final ZIP)'}
audit_open={'id':'S-ega-refaudit-02','date':'2026-11-19','commands':{'open':[{'ref_id':'https://stacks.math.columbia.edu/tag/'+s} for s in ['059H','00H9','027W','0BCX','00NX','00DV']]+[{'ref_id':'https://www.cip.ifi.lmu.de/~grinberg/algebra/logid.pdf'}]},'claim_ids':[f'C-SA23-ega-{n:03}' for n in decisions],'urls':['https://stacks.math.columbia.edu/tag/'+s for s in ['059H','00H9','027W','0BCX','00NX','00DV']]+['https://www.cip.ifi.lmu.de/~grinberg/algebra/logid.pdf'],'match_and_limit':'Read precise statement/proof portions recorded in reference_role.027W is definitions/exercises, not the graded-extension theorem. Grinberg PDF opening timed out; no verified reference or theorem is inferred from that URL. Unidentified source fragments remain without invented bibliographic matches.','raw_evidence':'sources/external/ega/raw_search/refaudit_open.json; refaudit_open2.json (internal caches excluded from final ZIP)'}
for a in [audit_search,audit_open]:
    log=[x for x in log if x.get('id')!=a['id']];log.append(a)
for x in log:
    for n in decisions:
        if x.get('id')==f'FATE-C-SA23-ega-{n:03}':
            x['refs']=by[n]['refs'];x['match_and_limit']=by[n]['fate']
            if 'S-ega-refaudit-02' not in x['search_operations']:x['search_operations'].append('S-ega-refaudit-02')
(HERE/'search_log.jsonl').write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in log))

audit=[{'id':f'C-SA23-ega-{n:03}','refs':r,'reference_role':role,'historical_identification_limit':limit} for n,(r,role,limit) in decisions.items()]
(HERE/'empty_reference_audit.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2)+'\n')
(HERE/'empty_reference_audit.md').write_text('# Final reference audit\n\nFifteen previously empty-reference claim records were individually reviewed. Nine now cite exact supporting sources with their limited role; six remain uncited for explicit identification or independent-proof reasons (031,032,041,044,073,082). No broad title is substituted for an exact theorem. In particular, tag027W is a Hilbert-functions exercise section and does not prove the manuscript’s graded extension sequence.\n\nThe audit corrected one error of this run: in C015, finite generation already gives surjectivity of the tensor/product map, while finite presentation gives bijectivity. Stacks10.89.2–3 and both proofs were read. The source lemma itself was correct.\n\nThe E classifications for elementary algebraic mechanisms are retained with explicit historical limits. An exact pre-manuscript printed antecedent is not claimed merely because an argument is elementary. The complete per-claim decisions, exact roles and limits are in empty_reference_audit.json. Four precise modern supporting references were added.\n\nAll182 top-level core/analysis claim records were also reviewed for origin. Each has an actual source assertion, definition or question. Pure present-run corrections remain labeled inside refined_statement or verification_origin. The stronger differential-module nonprojectivity lead is credited to the earlier run in SA23-141 and the C021/C023 notes, not presented as a separate authorial assertion.\n')

# Keep authored counts current; no source status or class is changed by this audit.
coverage=(HERE/'coverage.md').read_text().replace('Bibliography:81 records.','Bibliography:85 records.')
coverage+='\n## Final integration audit\n\nTwenty additional Codex subjects supply exact direction provenance; all82 indexed-entry verdicts are unchanged. The15 formerly empty-reference claims were reviewed in empty_reference_audit.json, with9 precise/limited reference additions and6 explicitly documented nonmatches or independent checks. C015’s present-run surjectivity sentence was corrected against Stacks10.89.2–3. All182 core/analysis claims have manually reviewed record_origin and verification_origin labels. The separate cross-owner review proposes3 indexed subject mergers and a conditional cocharacter-subsubject consolidation; no other owner’s registers were mutated.\n'
if '## Final integration audit' not in (HERE/'coverage.md').read_text():(HERE/'coverage.md').write_text(coverage)
rebuild=(HERE/'REBUILD.md').read_text().replace('13. `validate_core.py`','13. `final_reference_origin_audit.py` (precise supporting citations, source-origin labels and final correction)\n14. `validate_core.py`')
(HERE/'REBUILD.md').write_text(rebuild)
print(json.dumps({'claims_reviewed':len(decisions),'refs_added_to_claims':sum(bool(v[0]) for v in decisions.values()),'remaining_empty_refs':[c['id'] for c in cs if not c['refs']],'bibliography_records':len(bib),'origin_labels':len(origin_report),'new_check_events':len(new_events)}))
