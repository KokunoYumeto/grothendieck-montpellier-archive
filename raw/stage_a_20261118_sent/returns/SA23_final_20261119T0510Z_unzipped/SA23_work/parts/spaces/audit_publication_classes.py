"""Bounded manual A/B audit of the original A records in claims050–084.

Uses only the already opened sources and recorded reading extents. B here
records an established later exposition by other authors, not first priority.
"""
from pathlib import Path
import collections,csv,json
P=Path(__file__).parent

# These eighteen selections and judgments are manual, not inferred from titles.
DECISIONS={
50:('B','Faithful-flatness criteria were checked through the Stacks flatness reference and an independent proof; no exact opened EGA IV locator was recorded for this full formulation.'),
51:('B','The checked Stacks generalization-lifting and fppf-openness lemmas establish the formulation; no exact own-publication passage was opened for the complete bundle of assertions.'),
52:('B','The checked flat-base-change scheme-theoretic-image lemma and fpqc-descent references supply the hypotheses; no exact EGA/SGA own-publication match is recorded.'),
54:('B','The checklist was matched to separate Stacks descent lemmas; a general attribution to EGA does not identify a checked own-publication locator for every listed property.'),
56:('B','Stacks tag023S, Lemma35.5.1, and the checked module-descent proofs provide the cited evidence; no exact Grothendieck publication passage was read for this complete record.'),
57:('B','Stacks35.13.7 and35.35, including tag02VV, are the checked sources; no exact own-publication locus for this formulation is documented.'),
59:('B','Effective affine descent and its property consequences were checked in Stacks35.23/35.37; no exact EGA/SGA own-publication statement was opened.'),
60:('B','The exact checked relative-ampleness descent result is Stacks35.25.4, tag02LB. The separately read EGA II ampleness criteria do not themselves certify this full fpqc-descent record.'),
62:('B','The checked source is Stacks29.10/29.45 and its openness lemmas. Its pointer to EGA I second edition3.7.1 is an indirect lead; the original passage and the full combined formulation were not checked there.'),
63:('B','Quasi-affine and Zariski-main formulations were checked in Stacks. EGA II was cited broadly, but the opened EGA II4.5/4.6 passages do not certify the full quasi-affine/ZMT bundle here.'),
65:('A','Exact own-publication match directly read: Grothendieck, EGA II, Theorem4.5.2 and Proposition4.5.5–4.5.8, printed83–86; Proposition4.6.11 and4.6.13(ii), printed91–92. These are the recorded ampleness, positive-power and composed-morphism statements with their hypotheses.'),
67:('B','The checked source is the Stacks diagonal/separatedness treatment, supplemented by an independent equalizer proof. No exact original EGA locus was opened for this record.'),
68:('B','The checked higher-direct-image and flat-base-change statements are the Stacks coherent.tex lemmas at the recorded physical locators. No exact own-publication EGA/SGA locus was established in this audit.'),
69:('B','The projective-bundle and relative-Spec statements were checked in Stacks Constructions. Its reference to EGA II4.1.1 is an indirect pointer; the original full quotient/torsor formulation was not opened there.'),
70:('B','The checked adjunction is Stacks Schemes26.6.4. Its attribution to Tate and EGA II Err1 Proposition1.8.1 is a backward reference, not a directly checked own-publication match.'),
71:('B','The functor-gluing and sheaf/representability formulation was checked in Stacks Schemes at lemma-glue-functors; no exact original EGA/SGA statement was opened.'),
74:('B','The tensor-product fiber construction was checked in Stacks Schemes and by direct calculations. No exact own-publication passage for the entire point-set statement was recorded.'),
84:('B','The affine quasi-coherent sheaf result was matched to the checked Stacks lemma and independently reproved by clearing denominators; no exact own-publication locator was opened.'),
}
REVISED_FATES={
50:'The checked later Stacks flatness treatment and the direct faithful-flatness argument establish the criterion. The fiber test alone does not imply flatness: a nonflat module can have nonzero fibers everywhere.',
63:'The checked Stacks quasi-affine and Zariski-main formulations establish the stated results under their individual hypotheses. EGA II is a historical lead here, not an exact own-publication passage verified for this full record.',
69:'The checked Stacks Constructions projective-bundle and relative-Spec sections establish the functors, including arbitrary quasi-coherent M with the stated quotient interpretation. The EGA II4.1.1 pointer in that source is not recorded as an opened exact match.'
}
LIMIT='Class B reflects the checked later exposition by the Stacks Project Authors; no exact directly checked Grothendieck own-publication match is claimed here, and no claim of first discovery or priority is assigned to the Stacks Project.'

def apply_classifications(claims):
 for c in claims:
  n=int(c['id'].rsplit('-',1)[1])
  if n not in DECISIONS:continue
  cl,reason=DECISIONS[n]
  c['class']=cl;c['classification_reason']=reason
  c['publication_class_audit']='Manual source-authorship and exact-locator audit, 19 November 2026; classification is separate from mathematical truth and page status.'
  base=REVISED_FATES.get(n,c['fate'].split(' Publication-class limit: ')[0])
  c['fate']=base+(' Publication-class limit: '+LIMIT if cl=='B' else '')
  c['present_status']='As of 19 November 2026: '+c['fate']
  if cl=='B':
   c['publication_date_limit']='2026 is the checked Stacks version/access date. The first publication and first circulation of this precise result were not established by the recorded reference audit.'
  else:
   c['publication_date_limit']='EGA II volume published1961; received22July1960. The supplied manuscript leaf is undated, so its relative chronology is not established.'
 return claims

def save_audit():
 claims=json.loads((P/'claims.json').read_text());refs=json.loads((P/'reference_checks.json').read_text())
 old={c['id']:{'class':c['class'],'fate':c['fate']} for c in claims}
 prev={}
 if (P/'publication_class_audit.json').exists():
  prev={x['claim']:x for x in json.loads((P/'publication_class_audit.json').read_text())['decisions']}
 apply_classifications(claims)
 rows=[]
 for c in claims:
  n=int(c['id'].rsplit('-',1)[1])
  if n not in DECISIONS:continue
  rows.append({'claim':c['id'],'previous_class':'A','class':c['class'],
    'decision':'retain A' if c['class']=='A' else 'reclassify A to B',
    'reason':DECISIONS[n][1],
    'original_fate':prev.get(c['id'],{}).get('original_fate',old[c['id']]['fate']),
    'checked_sources':[{'key':r,'url':refs[r]['url'],'reading_extent_and_locator':refs[r]['annotation']} for r in c['refs']],
    'current_fate':c['fate'],'date_limit':c['publication_date_limit']})
 payload={'date':'2026-11-19','scope':'The18 original A records in C-SA23-spaces-050–084; bounded review of already-opened sources, no new literature search.',
   'class_rule':'A requires an exact checked result in Grothendieck’s own publication. Later Stacks exposition alone does not establish A.',
   'retained_A':1,'changed_to_B':17,'decisions':rows}
 (P/'claims.json').write_text(json.dumps(claims,ensure_ascii=False,indent=2)+'\n')
 (P/'publication_class_audit.json').write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n')
 # Preserve the refined source-question wording; append only the bibliographic
 # limit where a problem/editorial record depends on an affected claim.
 by={c['id']:c for c in claims}
 for filename in ['problems.json','editorial_tasks.json']:
  qs=json.loads((P/filename).read_text())
  for q in qs:
   ids=set(x['claim'] for x in q['occurrences'])|set(q.get('related_claims',[]))
   selected=[r for r in rows if r['claim'] in ids]
   if selected:
    q['publication_evidence_notes']=[{'claim':r['claim'],'class':r['class'],'reason':r['reason']} for r in selected]
    for r in selected:
     if r['current_fate'] not in q['state_of_art']:
      q['state_of_art']=q['state_of_art'].replace(r['original_fate'],r['current_fate'])
    suffix=' Publication-class limit: '+LIMIT
    while suffix+suffix in q['state_of_art']:
     q['state_of_art']=q['state_of_art'].replace(suffix+suffix,suffix)
  (P/filename).write_text(json.dumps(qs,ensure_ascii=False,indent=2)+'\n')
 with (P/'check_events.tsv').open(newline='') as f:
  rd=csv.DictReader(f,delimiter='\t');fields=rd.fieldnames;events=list(rd)
 events=[e for e in events if e['type']!='publication-class evidence audit']
 for r in rows:
  events.append({'statement_id':r['claim'],'date':'2026-11-19','who':'GPT-6 Astra Pro; owner spaces; SA23-20261119',
    'type':'publication-class evidence audit','outcome':r['decision']+'. '+r['reason']})
 with (P/'check_events.tsv').open('w',newline='') as f:
  wr=csv.DictWriter(f,fieldnames=fields,delimiter='\t');wr.writeheader();wr.writerows(events)
 logs=[json.loads(x) for x in (P/'search_log.jsonl').read_text().splitlines()]
 logs=[r for r in logs if not r.get('id','').startswith('CLASS-spaces-')]
 for r in rows:
  logs.append({'id':'CLASS-spaces-'+r['claim'].rsplit('-',1)[1],'date':'2026-11-19',
    'engine':'manual review of already opened publication evidence; no new query',
    'query':None,'claims':[r['claim']],'sources':r['checked_sources'],
    'outcome':r['decision']+'. '+r['reason'],'date_limit':r['date_limit']})
 (P/'search_log.jsonl').write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in logs))
 print(json.dumps({'publication_class_audit':'complete','retained_A':1,'changed_A_to_B':17,
                   'classes':dict(collections.Counter(c['class'] for c in claims)),
                   'events':len(events),'search_and_review_records':len(logs)}))

if __name__=='__main__':save_audit()
